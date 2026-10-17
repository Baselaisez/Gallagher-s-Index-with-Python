#!/usr/bin/env python3
"""Analyze raw classical Arabic text into a Qissa content package using Claude.

This is the "upload your own text" ability: give it 2-3 pages of fiqh, hadith,
history, or any classical Arabic material, and it produces the same package the
editorial pipeline produces for embedded stories — three tashkeel layers, clitic
segmentation, bilingual (EN/TR) glossary and translations, trilingual i'rab per
word, and links into the SAME global grammar registry the embedded stories use
(so tapping إنّ in an uploaded fiqh text opens the exact same note as in the
wasiyya). Grammar topics the registry doesn't cover yet are returned as
suggestions instead of invented links.

Usage:
    python3 tools/analyze_text.py mytext.txt --title-en "On Intentions" \
        --title-ar "باب النية" [--out content/user-uploads/on-intentions] \
        [--build-reader] [--model claude-opus-4-8]

Credentials: resolved the standard way (ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN /
`ant auth login` profile). For offline testing of the packaging pipeline, pass
--mock <analysis.json> with a pre-baked model response.

The output is machine-generated: the manifest is stamped
reviewStatus="auto-generated-unreviewed" and the validator will warn until a
human review upgrades it. Audio for uploaded texts uses on-device TTS in the
reader (no audio timestamps are produced here).
"""
import argparse
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = TOOLS_DIR.parent
sys.path.insert(0, str(TOOLS_DIR))
from validate_content import strip_diacritics  # noqa: E402

BILINGUAL = {"type": "object", "additionalProperties": False,
             "required": ["en", "tr"],
             "properties": {"en": {"type": "string"}, "tr": {"type": "string"}}}

ANALYSIS_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["levelEstimate", "sentences", "glossary", "suggestedNotes"],
    "properties": {
        "levelEstimate": {"type": "integer"},
        "sentences": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["id", "translation", "tokens"],
            "properties": {
                "id": {"type": "string"},
                "translation": BILINGUAL,
                "tokens": {"type": "array", "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["surface", "lex", "pos", "grammar", "punctAfter",
                                 "quoteBefore", "quoteAfter", "segments", "irab"],
                    "properties": {
                        "surface": {"type": "object", "additionalProperties": False,
                                    "required": ["full", "smart", "bare"],
                                    "properties": {"full": {"type": "string"},
                                                   "smart": {"type": "string"},
                                                   "bare": {"type": "string"}}},
                        "lex": {"type": "string"},
                        "pos": {"type": "string"},
                        "grammar": {"type": "array", "items": {"type": "string"}},
                        "punctAfter": {"type": ["string", "null"]},
                        "quoteBefore": {"type": ["string", "null"]},
                        "quoteAfter": {"type": ["string", "null"]},
                        "segments": {"type": ["array", "null"], "items": {
                            "type": "object", "additionalProperties": False,
                            "required": ["form", "lex"],
                            "properties": {"form": {"type": "string"},
                                           "lex": {"type": "string"}}}},
                        "irab": {"type": "object", "additionalProperties": False,
                                 "required": ["ar", "en", "tr"],
                                 "properties": {"ar": {"type": "string"},
                                                "en": {"type": "string"},
                                                "tr": {"type": "string"}}},
                    }}},
            }}},
        "glossary": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["lex", "lemma", "root", "pos", "form", "plural", "gloss", "level"],
            "properties": {
                "lex": {"type": "string"}, "lemma": {"type": "string"},
                "root": {"type": ["string", "null"]}, "pos": {"type": "string"},
                "form": {"type": ["string", "null"]}, "plural": {"type": ["string", "null"]},
                "gloss": BILINGUAL, "level": {"type": "integer"},
            }}},
        "suggestedNotes": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["titleAr", "titleEn", "reason"],
            "properties": {"titleAr": {"type": "string"}, "titleEn": {"type": "string"},
                           "reason": {"type": "string"}}}},
    },
}

SYSTEM_PROMPT = """You are the analysis engine of Qissa, an Arabic graded-reader app built on the
madrasah grammar tradition (Emsile, Bina, Birgivi's Awamil, al-Kafiya, Qatr al-Nada).
You receive raw classical Arabic text and produce the app's content-package analysis.

Rules — every one of these is checked by an automated validator:
1. Preserve the text exactly. Every word of the input appears as a token, in order.
   You may ADD tashkeel but never change letters or word order. Split into sentences
   at natural boundaries; ids are s1, s2, ... in order.
2. Three surface layers per token: "full" = complete tashkeel; "smart" = only the
   harakat needed to disambiguate; "bare" = no diacritics at all. HARD CONSTRAINT:
   stripping all diacritics (U+064B-U+0652, U+0670) from "full" and from "smart"
   must yield exactly "bare".
3. Move punctuation out of surfaces: sentence punctuation goes in punctAfter;
   quote marks in quoteBefore/quoteAfter. Surfaces contain only the word.
4. Segment clitics in "segments" (وَ، فَ، بِ، لِ، كَ، سَ، ال is NOT split, attached
   pronouns are): each segment has its vocalized form and its own lex id.
5. lex ids are short lowercase latin slugs (e.g. "qala", "niyya", "pron-3ms").
   Reuse the same lex for every occurrence of the same lexeme, including the
   common ids: wa, fa, bi, li, ila, min, an, inna, ma, la, allah, pron-3ms,
   pron-2ms, pron-1s.
6. Every token gets "irab": full classical parsing in Arabic (with harakat) plus
   a learner-facing English and Turkish rendering.
7. "grammar" per token may ONLY contain ids from the registry provided in the user
   message. If a token exhibits a grammar topic that is not in the registry, leave
   it out of "grammar" and add the topic once to "suggestedNotes" instead.
8. Glossary: one entry per lex (content words AND function words/pronouns used in
   segments), lemma vocalized, root as spaced letters (e.g. "ق و ل") or null,
   verb form as Roman numeral or null, gloss in English and Turkish,
   level 0 (proper nouns) to 6 (rare/classical).
9. levelEstimate: overall difficulty of this text on the app's 1-6 scale.
Return only the JSON object."""


def registry(grammar_dir: Path):
    notes = []
    for path in sorted(grammar_dir.glob("*.json")):
        g = json.loads(path.read_text(encoding="utf-8"))
        notes.append({"id": g["id"], "ar": g["title"]["ar"], "en": g["title"]["en"]})
    return notes


def chunk_text(text: str, max_words: int):
    """Split on blank lines, then group paragraphs into ~max_words chapters."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, current, count = [], [], 0
    for p in paras:
        words = len(p.split())
        if current and count + words > max_words:
            chunks.append("\n\n".join(current))
            current, count = [], 0
        current.append(p)
        count += words
    if current:
        chunks.append("\n\n".join(current))
    return chunks or [text.strip()]


def analyze_chunk(client, model: str, chunk: str, notes, known_lex):
    prompt = (
        "## Grammar registry (the ONLY valid ids for token \"grammar\")\n"
        + "\n".join(f"- {n['id']}: {n['ar']} — {n['en']}" for n in notes)
        + ("\n\n## lex ids already defined for this text (reuse them)\n"
           + ", ".join(sorted(known_lex)) if known_lex else "")
        + "\n\n## Text to analyze\n" + chunk
    )
    with client.messages.stream(
        model=model,
        max_tokens=64000,
        system=[{"type": "text", "text": SYSTEM_PROMPT,
                 "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": prompt}],
        output_config={"format": {"type": "json_schema", "schema": ANALYSIS_SCHEMA}},
    ) as stream:
        message = stream.get_final_message()
    if message.stop_reason == "refusal":
        raise SystemExit("The model declined to process this text (stop_reason=refusal).")
    if message.stop_reason == "max_tokens":
        raise SystemExit("Analysis truncated (max_tokens) — split the input into smaller files.")
    text = next(b.text for b in message.content if b.type == "text")
    return json.loads(text)


def fix_layers(tok):
    """Enforce the tashkeel-layer law even if the model slipped."""
    s = tok["surface"]
    s["full"] = unicodedata.normalize("NFC", s["full"])
    bare = strip_diacritics(s["full"])
    if strip_diacritics(s.get("bare", "")) != bare or s.get("bare") != bare:
        s["bare"] = bare
    if strip_diacritics(s.get("smart", "")) != bare:
        s["smart"] = s["full"]


def to_chapter(analysis, n, valid_ids, dropped):
    sentences = []
    for sen in analysis["sentences"]:
        tokens = []
        for tok in sen["tokens"]:
            fix_layers(tok)
            t = {"surface": tok["surface"], "lex": tok["lex"], "pos": tok["pos"]}
            grammar = [g for g in tok.get("grammar") or [] if g in valid_ids]
            dropped.update(set(tok.get("grammar") or []) - valid_ids)
            if grammar:
                t["grammar"] = grammar
            for key in ("punctAfter", "quoteBefore", "quoteAfter"):
                if tok.get(key):
                    t[key] = tok[key]
            if tok.get("segments"):
                t["segments"] = tok["segments"]
            t["irab"] = tok["irab"]
            tokens.append(t)
        sentences.append({"id": sen["id"], "translation": sen["translation"], "tokens": tokens})
    return {"chapter": n, "sentences": sentences}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path, help="UTF-8 .txt file of Arabic text")
    ap.add_argument("--title-en", required=True)
    ap.add_argument("--title-ar", required=True)
    ap.add_argument("--title-tr", default=None)
    ap.add_argument("--out", type=Path, default=None,
                    help="output package dir (default content/user-uploads/<slug>)")
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--grammar-dir", type=Path, default=ROOT / "content/grammar")
    ap.add_argument("--max-chunk-words", type=int, default=400)
    ap.add_argument("--mock", type=Path, default=None,
                    help="JSON file with a pre-baked analysis (offline pipeline test)")
    ap.add_argument("--build-reader", action="store_true",
                    help="also emit a standalone reader.html for this package")
    args = ap.parse_args()

    slug = re.sub(r"[^a-z0-9]+", "-", args.title_en.lower()).strip("-")
    out = args.out or ROOT / "content/user-uploads" / slug
    notes = registry(args.grammar_dir)
    valid_ids = {n["id"] for n in notes}
    text = args.input.read_text(encoding="utf-8")
    chunks = chunk_text(text, args.max_chunk_words)
    print(f"{len(chunks)} chapter(s) to analyze; grammar registry: {len(valid_ids)} notes")

    analyses = []
    if args.mock:
        mock = json.loads(args.mock.read_text(encoding="utf-8"))
        analyses = mock if isinstance(mock, list) else [mock]
        print("mock mode: using pre-baked analysis")
    else:
        import anthropic
        client = anthropic.Anthropic()  # ANTHROPIC_API_KEY / AUTH_TOKEN / ant profile
        known_lex = set()
        for i, chunk in enumerate(chunks, 1):
            print(f"analyzing chapter {i}/{len(chunks)} ({len(chunk.split())} words)…")
            analysis = analyze_chunk(client, args.model, chunk, notes, known_lex)
            known_lex.update(e["lex"] for e in analysis["glossary"])
            analyses.append(analysis)

    # ---- assemble the package ----
    out.mkdir(parents=True, exist_ok=True)
    (out / "chapters").mkdir(exist_ok=True)
    glossary, dropped, suggested = {}, set(), []
    chapters_meta = []
    for n, analysis in enumerate(analyses, 1):
        chapter = to_chapter(analysis, n, valid_ids, dropped)
        (out / "chapters" / f"{n}.json").write_text(
            json.dumps(chapter, ensure_ascii=False, indent=2), encoding="utf-8")
        chapters_meta.append({"n": n, "title": {"ar": f"الفصل {n}", "en": f"Part {n}"}})
        for entry in analysis["glossary"]:
            e = {k: v for k, v in entry.items() if v is not None and k != "lex"}
            glossary.setdefault(entry["lex"], e)
        suggested.extend(analysis.get("suggestedNotes", []))

    level = max(a.get("levelEstimate", 3) for a in analyses)
    manifest = {
        "id": slug,
        "storyGroup": slug,
        "title": {"ar": args.title_ar, "en": args.title_en,
                  **({"tr": args.title_tr} if args.title_tr else {})},
        "level": min(max(level, 1), 6),
        "levelName": ["Newbie", "Elementary", "Intermediate", "Upper-Intermediate",
                      "Advanced", "Master"][min(max(level, 1), 6) - 1],
        "version": "0.1.0",
        # An upload enters the library the day it is analyzed — that is exactly
        # what the library's "New" shelf means.
        "published": date.today().isoformat(),
        "access": "user-upload",
        "chapters": chapters_meta,
        "attribution": {
            "en": "User-uploaded text, analyzed automatically by the Qissa analyzer "
                  "(LLM). Vocalization, i'rab, and glosses are machine-generated and "
                  "may contain errors.",
            "reviewStatus": "auto-generated-unreviewed",
        },
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                       encoding="utf-8")
    (out / "glossary.json").write_text(
        json.dumps({"entries": glossary}, ensure_ascii=False, indent=2), encoding="utf-8")
    if suggested or dropped:
        (out / "suggested-notes.json").write_text(json.dumps({
            "suggestedNotes": suggested,
            "droppedGrammarIds": sorted(dropped),
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- validate ----
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "validate_content.py"), str(out),
         "--grammar-dir", str(args.grammar_dir)])
    if result.returncode != 0:
        print("\npackage written but FAILED validation — inspect before use:", out)
        sys.exit(1)

    # ---- optional standalone reader ----
    if args.build_reader:
        import shutil
        reader = out / "reader.html"
        shutil.copy(ROOT / "prototype/reader.html", reader)
        subprocess.run(
            [sys.executable, str(TOOLS_DIR / "build_prototype.py"),
             "--package", str(out), "--grammar-dir", str(args.grammar_dir),
             "--html", str(reader)], check=True)
        print("standalone reader:", reader)

    print("\npackage ready:", out)
    if suggested:
        print(f"{len(suggested)} new grammar topic(s) suggested — see suggested-notes.json")


if __name__ == "__main__":
    main()
