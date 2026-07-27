#!/usr/bin/env python3
"""Regenerate the embedded data block in prototype/reader.html from content packages.

The prototype is a renderer; the content packages are the source of truth. This script
reads one or more story packages plus the global grammar registry, transforms them into
the JS constants the app shell expects (a STORIES array + shared GRAMMAR), and splices
them between the __DATA_START__ / __DATA_END__ markers.

Usage:
    python3 tools/build_prototype.py                       # discover all packages
    python3 tools/build_prototype.py --package <dir> --html <file>   # standalone build
    python3 tools/build_prototype.py --packages <dir> <dir> ...

Run tools/validate_content.py on each package first — this script refuses obviously
broken input but does not repeat full validation.
"""
import argparse
import json
from pathlib import Path

START = "// __DATA_START__"
END = "// __DATA_END__"

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS = [ROOT / "content/samples", ROOT / "content/user-uploads"]
IRAB_TR = ROOT / "content/i18n/irab-tr.json"


def load_irab_tr():
    """Turkish translation memory for i'rab notes, keyed by the English string.

    Chapters author i'rab as {ar, en}; the Turkish comes from this shared file so
    a phrase repeated across stories is translated once. Missing keys simply fall
    back to English in the reader — run tools/check_irab_tr.py to find them.
    """
    if not IRAB_TR.is_file():
        return {}
    return json.loads(IRAB_TR.read_text(encoding="utf-8")).get("entries", {})


def bilingual(value):
    """Normalize plain strings and {en, tr} objects to {en, tr}."""
    if isinstance(value, dict):
        return {"en": value.get("en", ""), "tr": value.get("tr", value.get("en", ""))}
    return {"en": value or "", "tr": value or ""}


def discover():
    pkgs = []
    for coll in COLLECTIONS:
        if coll.is_dir():
            pkgs += sorted(d for d in coll.iterdir() if (d / "manifest.json").is_file())
    return pkgs


def build_story(pkg: Path, irab_tr=None):
    irab_tr = irab_tr or {}
    manifest = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
    glossary = json.loads((pkg / "glossary.json").read_text(encoding="utf-8"))["entries"]

    morph = {}
    mpath = pkg / "morphology.json"
    if mpath.exists():
        for lex, m in json.loads(mpath.read_text(encoding="utf-8"))["verbs"].items():
            entry = {"bab": m["bab"], "wazn": m["wazn"], "masdar": m["masdar"],
                     "fail": m["ismFail"], "mazi": m["mazi"], "mudari": m["mudari"],
                     "amr": m["amr"]}
            if m.get("ismMaful"):
                entry["maful"] = m["ismMaful"]
            # Governed mudari' forms feed the Emsile-i Muhtelife table. They are
            # stored, not derived: for hollow/defective verbs the jussive is not a
            # vowel swap (يَقُولُ -> لَمْ يَقُلْ, يَرْمِي -> لَمْ يَرْمِ).
            for key in ("mansub", "majzum", "majzum2",
                        "majhulMazi", "majhulMudari"):
                if m.get(key):
                    entry[key] = m[key]
            if m.get("note"):
                entry["note"] = m["note"]
            morph[lex] = entry

    chapters = []
    for ch in manifest["chapters"]:
        data = json.loads((pkg / "chapters" / f"{ch['n']}.json").read_text(encoding="utf-8"))
        sentences = []
        for sen in data["sentences"]:
            tokens = []
            for tok in sen["tokens"]:
                # pos travels with the token: the reader needs to know whether a
                # word is a nominal before it can quiz its role in the sentence.
                t = {"s": tok["surface"], "lex": tok["lex"]}
                if tok.get("pos"):
                    t["pos"] = tok["pos"]
                for key in ("grammar", "punctAfter", "quoteBefore", "quoteAfter",
                            "irab", "phrase"):
                    if tok.get(key):
                        t[key] = tok[key]
                if t.get("irab") and t["irab"].get("en") and not t["irab"].get("tr"):
                    tr = irab_tr.get(t["irab"]["en"])
                    if tr:
                        t["irab"] = dict(t["irab"], tr=tr)
                if tok.get("segments"):
                    t["segments"] = [{"form": s["form"], "lex": s["lex"]}
                                     for s in tok["segments"]]
                tokens.append(t)
            sentence = {"id": sen["id"], "translation": sen["translation"],
                        "tokens": tokens}
            if sen.get("audio"):
                sentence["audio"] = sen["audio"]  # [startMs, endMs] — forward-prep for real narration
            sentences.append(sentence)
        chapters.append({"n": ch["n"], "title": ch["title"], "sentences": sentences})

    return {
        "id": manifest["id"],
        "group": manifest.get("storyGroup", manifest["id"]),
        "title": manifest["title"],
        "subtitle": manifest.get("subtitle", {}),
        "level": manifest.get("level", 1),
        "levelName": manifest.get("levelName", ""),
        "access": manifest.get("access", "free"),
        "review": manifest.get("attribution", {}).get("reviewStatus", ""),
        "glossary": glossary,
        "morph": morph,
        "chapters": chapters,
    }


def build_grammar(grammar_dir: Path):
    notes = {}
    for path in sorted(grammar_dir.glob("*.json")):
        g = json.loads(path.read_text(encoding="utf-8"))
        note = {"title": g["title"], "level": g.get("level"),
                "group": g.get("group", "nahw"),
                "explanation": bilingual(g.get("explanation"))}
        if g.get("amil"):
            note["amil"] = g["amil"]
        if g.get("mamul"):
            note["mamul"] = g["mamul"]
        if g.get("classicalSources"):
            note["sources"] = g["classicalSources"]
        note["examples"] = [{"ar": x["ar"], "en": x.get("en", ""),
                             "src": x.get("sourceStory")}
                            for x in g.get("examples", [])]
        note["mistakes"] = [{"wrong": m["wrong"], "right": m["right"],
                             "why": bilingual(m.get("why"))}
                            for m in g.get("commonMistakes", [])]
        notes[g["id"]] = note
    return notes


def js(name, value):
    return f"const {name} = {json.dumps(value, ensure_ascii=False, separators=(',', ':'))};"


def build_catalog(pkgs):
    """Build a catalog.json index from discovered packages.

    Returns a catalog dict with packages sorted by level then id (stable/diff-friendly).
    Each package entry includes: id, title, level, levelName, version, access,
    storyGroup, reviewStatus, chapters (count), rotationWindow (null).
    """
    catalog_packages = []
    for pkg in pkgs:
        manifest = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
        entry = {
            "id": manifest["id"],
            "title": manifest["title"],
            "level": manifest.get("level", 1),
            "levelName": manifest.get("levelName", ""),
            "version": manifest.get("version", ""),
            "access": manifest.get("access", "free"),
            "storyGroup": manifest.get("storyGroup", manifest["id"]),
            "reviewStatus": manifest.get("attribution", {}).get("reviewStatus", ""),
            "chapters": len(manifest.get("chapters", [])),
            "rotationWindow": None,
        }
        catalog_packages.append(entry)

    # Sort by level then id for deterministic output
    catalog_packages.sort(key=lambda p: (p["level"], p["id"]))

    return {
        "catalogVersion": "0.1",
        "generatedFrom": "tools/build_prototype.py",
        "packages": catalog_packages,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--package", type=Path, default=None,
                    help="build a standalone reader for a single package")
    ap.add_argument("--packages", type=Path, nargs="*", default=None)
    ap.add_argument("--grammar-dir", type=Path, default=ROOT / "content/grammar")
    ap.add_argument("--html", type=Path, default=ROOT / "prototype/reader.html")
    args = ap.parse_args()

    # Track whether we're doing a full discovery (for catalog write guard)
    is_full_discovery = False
    if args.package:
        pkgs = [args.package]
    elif args.packages:
        pkgs = args.packages
    else:
        pkgs = discover()
        is_full_discovery = True
    if not pkgs:
        raise SystemExit("no packages found")

    irab_tr = load_irab_tr()
    stories = [build_story(p, irab_tr) for p in pkgs]
    grammar = build_grammar(args.grammar_dir)
    block = "\n".join([
        START,
        "// Generated by tools/build_prototype.py — DO NOT EDIT BY HAND.",
        f"// Packages: {', '.join(p.name for p in pkgs)}",
        js("STORIES", stories),
        js("GRAMMAR", grammar),
        js("REF_GROUPS", [
            {"id": "sarf", "ar": "الصَّرْف", "en": "Morphology — after Emsile & Bina"},
            {"id": "nahw", "ar": "النَّحْو", "en": "Syntax — after al-Kafiya & Qatr al-Nada"},
            {"id": "awamil", "ar": "الْعَوَامِل", "en": "Governors — after Birgivi's Awamil"},
        ]),
        END,
    ])

    html = args.html.read_text(encoding="utf-8")
    i, j = html.find(START), html.find(END)
    if i == -1 or j == -1:
        raise SystemExit(f"markers {START} / {END} not found in {args.html}")
    args.html.write_text(html[:i] + block + html[j + len(END):], encoding="utf-8")
    n_tokens = sum(len(s["tokens"]) for st in stories
                   for c in st["chapters"] for s in c["sentences"])
    print(f"Rebuilt {args.html}: {len(stories)} stories, {n_tokens} tokens, "
          f"{len(grammar)} grammar notes")

    # Build and write catalog only on full discovery, not on --package single builds
    if is_full_discovery:
        catalog = build_catalog(pkgs)
        catalog_path = ROOT / "content/catalog.json"
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"Wrote catalog.json: {len(catalog['packages'])} packages")


if __name__ == "__main__":
    main()
