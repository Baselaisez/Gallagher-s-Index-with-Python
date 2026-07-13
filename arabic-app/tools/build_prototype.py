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


def build_story(pkg: Path):
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
                t = {"s": tok["surface"], "lex": tok["lex"]}
                for key in ("grammar", "punctAfter", "quoteBefore", "quoteAfter", "irab"):
                    if tok.get(key):
                        t[key] = tok[key]
                if tok.get("segments"):
                    t["segments"] = [{"form": s["form"], "lex": s["lex"]}
                                     for s in tok["segments"]]
                tokens.append(t)
            sentences.append({"id": sen["id"], "translation": sen["translation"],
                              "tokens": tokens})
        chapters.append({"n": ch["n"], "title": ch["title"], "sentences": sentences})

    return {
        "id": manifest["id"],
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


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--package", type=Path, default=None,
                    help="build a standalone reader for a single package")
    ap.add_argument("--packages", type=Path, nargs="*", default=None)
    ap.add_argument("--grammar-dir", type=Path, default=ROOT / "content/grammar")
    ap.add_argument("--html", type=Path, default=ROOT / "prototype/reader.html")
    args = ap.parse_args()

    if args.package:
        pkgs = [args.package]
    elif args.packages:
        pkgs = args.packages
    else:
        pkgs = discover()
    if not pkgs:
        raise SystemExit("no packages found")

    stories = [build_story(p) for p in pkgs]
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


if __name__ == "__main__":
    main()
