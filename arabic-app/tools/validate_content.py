#!/usr/bin/env python3
"""Validate Qissa content packages before publishing.

Usage:
    python3 tools/validate_content.py content/samples/wasiyyat-abi-hanifa \
        [--grammar-dir content/samples/grammar]

Checks (E = error, blocks publish; W = warning):
  E manifest.json: required fields, level range, chapter files exist
  E chapters: sentences have ids, translations (en required), tokens well-formed
  E tashkeel layers: stripping diacritics from `full` and `smart` must equal `bare`
  E lex references: every token/segment lex exists in glossary.json
  E grammar references: every grammar id resolves to a note file in the grammar dir
  E audio spans: [start, end] with start < end, non-overlapping, monotonic per chapter
  E morphology.json: verbs exist in glossary, paradigm sizes (mazi/mudari=14, amr=6),
      forms are Arabic-only, required fields (bab, wazn, masdar, ismFail)
  E grammar notes: required fields; commonMistakes entries need wrong/right/why
  W i'rab coverage below 100% of tokens
  W glossary entries never referenced by any chapter
  W verb (pos=verb in glossary) with no morphology entry
  W grammar note has no example sourced from a story

Exit code 0 = no errors (warnings allowed), 1 = errors found.
"""
import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

# Arabic diacritics: tanwin/harakat/shadda/sukun (064B-0652), quranic marks
# commonly used in vocalized text (0653-0655), dagger alif (0670).
DIACRITICS = re.compile(r"[ً-ٰٕ]")
ARABIC_ONLY = re.compile(r"^[؀-ۿ\s]+$")

REQUIRED_MANIFEST = ["id", "title", "level", "version", "published", "access", "chapters"]
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED_NOTE = ["id", "title", "level", "group", "explanation", "examples", "commonMistakes"]
NOTE_GROUPS = {"sarf", "nahw", "awamil", "balagha"}


def strip_diacritics(text: str) -> str:
    return DIACRITICS.sub("", unicodedata.normalize("NFC", text))


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def dump(self) -> int:
        for w in self.warnings:
            print(f"  W  {w}")
        for e in self.errors:
            print(f"  E  {e}")
        print(f"\n{len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0


def load_json(path: Path, rep: Report):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        rep.error(f"{path}: file missing")
    except json.JSONDecodeError as exc:
        rep.error(f"{path}: invalid JSON — {exc}")
    return None


def check_manifest(pkg: Path, rep: Report):
    manifest = load_json(pkg / "manifest.json", rep)
    if manifest is None:
        return None
    for field in REQUIRED_MANIFEST:
        if field not in manifest:
            rep.error(f"manifest.json: missing required field '{field}'")
    level = manifest.get("level")
    if not isinstance(level, int) or not 1 <= level <= 6:
        rep.error(f"manifest.json: level must be an integer 1-6, got {level!r}")
    title = manifest.get("title", {})
    if not isinstance(title, dict) or "ar" not in title or "en" not in title:
        rep.error("manifest.json: title must contain at least 'ar' and 'en'")
    # The date the story entered the library, not the date the text was written —
    # the library's "New" shelf is about what the reader has not seen yet. It is
    # authored, not derived: a rebuild must never silently re-date the catalogue.
    published = manifest.get("published")
    if published is not None:
        if not isinstance(published, str) or not ISO_DATE_RE.match(published):
            rep.error(f"manifest.json: published must be YYYY-MM-DD, got {published!r}")
        else:
            try:
                when = date.fromisoformat(published)
            except ValueError:
                rep.error(f"manifest.json: published is not a real date: {published!r}")
            else:
                # A future date makes the story permanently "not yet new" in the
                # reader, which reads as a missing badge rather than as an error.
                if when > date.today():
                    rep.error(f"manifest.json: published is in the future: {published}")
    for ch in manifest.get("chapters", []):
        n = ch.get("n")
        chapter_file = pkg / "chapters" / f"{n}.json"
        if not chapter_file.exists():
            rep.error(f"manifest.json: chapter {n} declared but {chapter_file.name} missing")
    attribution = manifest.get("attribution", {})
    if attribution.get("reviewStatus") != "approved":
        rep.warn(
            f"manifest.json: attribution.reviewStatus is "
            f"{attribution.get('reviewStatus')!r} — scholarly review required before publish"
        )
    return manifest


def check_token(tok: dict, where: str, glossary: dict, grammar_ids: set,
                rep: Report, stats: dict):
    surface = tok.get("surface")
    if not isinstance(surface, dict):
        rep.error(f"{where}: token missing 'surface' object")
        return
    for layer in ("full", "smart", "bare"):
        if layer not in surface:
            rep.error(f"{where}: surface missing layer '{layer}'")
    full, smart, bare = (surface.get(k, "") for k in ("full", "smart", "bare"))
    if full and bare and strip_diacritics(full) != unicodedata.normalize("NFC", bare):
        rep.error(f"{where}: strip(full) '{strip_diacritics(full)}' != bare '{bare}'")
    if smart and bare and strip_diacritics(smart) != unicodedata.normalize("NFC", bare):
        rep.error(f"{where}: strip(smart) '{strip_diacritics(smart)}' != bare '{bare}'")
    if DIACRITICS.search(bare):
        rep.error(f"{where}: bare layer '{bare}' still contains diacritics")

    lex = tok.get("lex")
    if not lex:
        rep.error(f"{where}: token missing 'lex'")
    elif lex not in glossary:
        rep.error(f"{where}: lex '{lex}' not in glossary.json")
    else:
        stats["used_lex"].add(lex)

    for seg in tok.get("segments", []):
        slex = seg.get("lex")
        if slex not in glossary:
            rep.error(f"{where}: segment lex '{slex}' not in glossary.json")
        else:
            stats["used_lex"].add(slex)
        if not seg.get("form"):
            rep.error(f"{where}: segment missing 'form'")

    phrase = tok.get("phrase")
    if phrase:
        plex = phrase.get("lex")
        if plex not in glossary:
            rep.error(f"{where}: phrase lex '{plex}' not in glossary.json")
        else:
            stats["used_lex"].add(plex)
        if not isinstance(phrase.get("span"), int) or phrase["span"] < 2:
            rep.error(f"{where}: phrase span must be an integer >= 2")

    for gid in tok.get("grammar", []):
        if gid not in grammar_ids:
            rep.error(f"{where}: grammar id '{gid}' has no note file in grammar dir")
        else:
            stats["used_grammar"].add(gid)

    stats["tokens"] += 1
    if tok.get("irab"):
        irab = tok["irab"]
        if not irab.get("ar") or not irab.get("en"):
            rep.error(f"{where}: irab must contain both 'ar' and 'en'")
        stats["irab_tokens"] += 1


def check_chapter(path: Path, glossary: dict, grammar_ids: set, rep: Report, stats: dict):
    data = load_json(path, rep)
    if data is None:
        return
    prev_end = None
    seen_ids = set()
    for sen in data.get("sentences", []):
        sid = sen.get("id", "?")
        where = f"{path.name}:{sid}"
        if sid in seen_ids:
            rep.error(f"{where}: duplicate sentence id")
        seen_ids.add(sid)
        translation = sen.get("translation", {})
        if "en" not in translation:
            rep.error(f"{where}: missing English translation")
        audio = sen.get("audio")
        if audio is not None:
            if (not isinstance(audio, list) or len(audio) != 2
                    or not all(isinstance(x, (int, float)) for x in audio)):
                rep.error(f"{where}: audio must be [startMs, endMs]")
            else:
                start, end = audio
                if start >= end:
                    rep.error(f"{where}: audio start {start} >= end {end}")
                if prev_end is not None and start < prev_end:
                    rep.error(f"{where}: audio overlaps previous sentence "
                              f"(starts {start} < previous end {prev_end})")
                prev_end = end
        tokens = sen.get("tokens", [])
        if not tokens:
            rep.error(f"{where}: sentence has no tokens")
        for i, tok in enumerate(tokens):
            check_token(tok, f"{where}[{i}]", glossary, grammar_ids, rep, stats)
            ph = tok.get("phrase")
            if ph and isinstance(ph.get("span"), int) and i + ph["span"] > len(tokens):
                rep.error(f"{where}[{i}]: phrase span {ph['span']} runs past the end of the sentence")


def check_morphology(pkg: Path, glossary: dict, rep: Report):
    path = pkg / "morphology.json"
    if not path.exists():
        rep.warn("morphology.json: not present (verbs will have no sarf tables)")
        return
    data = load_json(path, rep)
    if data is None:
        return
    verbs = data.get("verbs", {})
    for lex, m in verbs.items():
        where = f"morphology.json:{lex}"
        if lex not in glossary:
            rep.error(f"{where}: verb not in glossary.json")
        for field in ("bab", "wazn", "masdar", "ismFail"):
            if not m.get(field):
                rep.error(f"{where}: missing '{field}'")
        # The Emsile-i Muhtelife table needs the governed mudari' forms. They are
        # stored rather than derived because hollow/defective verbs break the
        # sound-verb rule (يَقُولُ -> لَمْ يَقُلْ), so a missing one is a warning:
        # the muhtelife tab is simply hidden for that verb.
        missing_gov = [f for f in ("mansub", "majzum", "majzum2") if not m.get(f)]
        if missing_gov:
            rep.warn(f"{where}: no {'/'.join(missing_gov)} — "
                     f"the Emsile-i Muhtelife table will be hidden for this verb")
        for tense, size in (("mazi", 14), ("mudari", 14), ("amr", 6)):
            forms = m.get(tense)
            if not isinstance(forms, list) or len(forms) != size:
                rep.error(f"{where}: '{tense}' must have exactly {size} forms, "
                          f"got {len(forms) if isinstance(forms, list) else type(forms).__name__}")
                continue
            for i, form in enumerate(forms):
                if not form or not ARABIC_ONLY.match(form):
                    rep.error(f"{where}: {tense}[{i}] '{form}' is empty or not Arabic-only")
    glossary_verbs = {k for k, v in glossary.items() if v.get("pos") == "verb"}
    for missing in sorted(glossary_verbs - set(verbs)):
        rep.warn(f"morphology.json: glossary verb '{missing}' has no paradigm entry")


def check_grammar_notes(grammar_dir: Path, rep: Report) -> set:
    ids = set()
    if not grammar_dir.is_dir():
        rep.error(f"{grammar_dir}: grammar directory missing")
        return ids
    for path in sorted(grammar_dir.glob("*.json")):
        note = load_json(path, rep)
        if note is None:
            continue
        nid = note.get("id")
        if nid != path.stem:
            rep.error(f"{path.name}: id '{nid}' does not match filename")
        ids.add(path.stem)
        for field in REQUIRED_NOTE:
            if field not in note:
                rep.error(f"{path.name}: missing required field '{field}'")
        if note.get("group") not in NOTE_GROUPS:
            rep.error(f"{path.name}: group must be one of {sorted(NOTE_GROUPS)}, "
                      f"got {note.get('group')!r}")
        title = note.get("title", {})
        if "ar" not in title or "en" not in title:
            rep.error(f"{path.name}: title must contain 'ar' and 'en'")
        if not note.get("examples"):
            rep.error(f"{path.name}: needs at least one example")
        elif not any(x.get("sourceStory") for x in note["examples"]):
            rep.warn(f"{path.name}: no example is sourced from a story "
                     f"(add sourceStory/sentence to keep notes anchored in real content)")
        mistakes = note.get("commonMistakes", [])
        if not mistakes:
            rep.error(f"{path.name}: needs at least one commonMistakes entry "
                      f"(a Qissa grammar note without mistakes is incomplete)")
        for i, m in enumerate(mistakes):
            for field in ("wrong", "right", "why"):
                if not m.get(field):
                    rep.error(f"{path.name}: commonMistakes[{i}] missing '{field}'")
    return ids


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("package", type=Path, help="story package directory")
    ap.add_argument("--grammar-dir", type=Path, default=None,
                    help="global grammar registry (default: content/grammar next to the package tree)")
    args = ap.parse_args()

    pkg: Path = args.package
    grammar_dir = args.grammar_dir
    if grammar_dir is None:
        # Global registry lives at content/grammar; packages at content/<collection>/<story>.
        candidates = [pkg.parent.parent / "grammar", pkg.parent / "grammar"]
        grammar_dir = next((c for c in candidates if c.is_dir()), candidates[0])
    rep = Report()
    stats = {"tokens": 0, "irab_tokens": 0, "used_lex": set(), "used_grammar": set()}

    print(f"Validating package: {pkg}")
    if not pkg.is_dir():
        print(f"  E  {pkg}: not a directory")
        return 1

    grammar_ids = check_grammar_notes(grammar_dir, rep)
    manifest = check_manifest(pkg, rep)
    glossary_doc = load_json(pkg / "glossary.json", rep) or {}
    glossary = glossary_doc.get("entries", {})
    if not glossary:
        rep.error("glossary.json: no entries")
    for lex, entry in glossary.items():
        if not entry.get("lemma"):
            rep.error(f"glossary.json:{lex}: missing lemma")
        if not entry.get("gloss", {}).get("en"):
            rep.error(f"glossary.json:{lex}: missing English gloss")
        lvl = entry.get("level")
        if not isinstance(lvl, int) or not 0 <= lvl <= 6:
            rep.error(f"glossary.json:{lex}: level must be integer 0-6, got {lvl!r}")

    if manifest:
        for ch in manifest.get("chapters", []):
            chapter_file = pkg / "chapters" / f"{ch.get('n')}.json"
            if chapter_file.exists():
                check_chapter(chapter_file, glossary, grammar_ids, rep, stats)

    check_morphology(pkg, glossary, rep)

    for unused in sorted(set(glossary) - stats["used_lex"]):
        rep.warn(f"glossary.json: entry '{unused}' never referenced by any chapter")
    if stats["tokens"]:
        coverage = 100 * stats["irab_tokens"] / stats["tokens"]
        if coverage < 100:
            rep.warn(f"i'rab coverage {coverage:.0f}% "
                     f"({stats['irab_tokens']}/{stats['tokens']} tokens)")
    print(f"  tokens: {stats['tokens']}, i'rab: {stats['irab_tokens']}, "
          f"glossary used: {len(stats['used_lex'])}/{len(glossary)}, "
          f"grammar notes referenced: {len(stats['used_grammar'])}/{len(grammar_ids)}\n")
    return rep.dump()


if __name__ == "__main__":
    sys.exit(main())
