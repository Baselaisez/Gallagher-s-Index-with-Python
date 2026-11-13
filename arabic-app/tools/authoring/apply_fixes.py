#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_fixes.py — the author's corrected iʿrāb lines, written into a shipped engine-authored package AND into its fixes file.

    python3 tools/authoring/apply_fixes.py <package-id> <authoring-dir> <notes.json> [--dry]

notes.json   {"<ch>:<sId>:<i>": {"w": "<the token as written — checked>", "irab": {"ar", "en", "tr"},
                                  "grammar"?: [note ids], "pos"?: …, "lex"?: <lex key>}}

The packages made by pkg_from_engine.py are not regenerated wholesale when one line is wrong (a later engine reads other
words differently): the token is corrected in place, and the same row is merged into tools/authoring/<dir>/fixes.json
(`irab`, `tags`, `pos`, `key`) so that a future regeneration writes the corrected line again. Every row names the word it
corrects; a row whose word is not the token at that address stops the run.
"""
import json, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = lambda s: unicodedata.normalize("NFC", s or "")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    pkg_id, adir, notes_path = args
    pkg = ROOT / "content/samples" / pkg_id
    fixes_path = ROOT / "tools/authoring" / adir / "fixes.json"
    notes = json.load(open(notes_path, encoding="utf-8"))
    fixes = json.load(open(fixes_path, encoding="utf-8"))
    gids = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
    glossary = json.load(open(pkg / "glossary.json", encoding="utf-8"))["entries"]
    chapters = {}
    changed = 0
    for key, row in sorted(notes.items(), key=lambda kv: [int(kv[0].split(":")[0]), kv[0]]):
        ch, sid, i = key.split(":"); i = int(i)
        if ch not in chapters:
            chapters[ch] = json.load(open(pkg / "chapters" / f"{ch}.json", encoding="utf-8"))
        sen = next((s for s in chapters[ch]["sentences"] if s["id"] == sid), None)
        if sen is None or i >= len(sen["tokens"]):
            raise SystemExit(f"{key}: no such token")
        tok = sen["tokens"][i]
        if N(tok["surface"]["full"]) != N(row["w"]):
            raise SystemExit(f"{key}: the token is «{tok['surface']['full']}», the row corrects «{row['w']}»")
        for lang in ("ar", "en", "tr"):
            if not row["irab"].get(lang):
                raise SystemExit(f"{key}: the line has no «{lang}»")
        for g in row.get("grammar", []):
            if g not in gids:
                raise SystemExit(f"{key}: unknown grammar note «{g}»")
        if "lex" in row and row["lex"] not in glossary:
            raise SystemExit(f"{key}: the package's glossary has no «{row['lex']}»")
        before = json.dumps(tok, ensure_ascii=False, sort_keys=True)
        tok["irab"] = {lang: row["irab"][lang] for lang in ("ar", "en", "tr")}
        if "grammar" in row: tok["grammar"] = list(row["grammar"])
        if "pos" in row: tok["pos"] = row["pos"]
        if "lex" in row:
            for seg in tok.get("segments", []):   # the host segment carries the word's key: it follows the correction
                if seg.get("lex") == tok.get("lex") and tok.get("lex") != row["lex"]:
                    seg["lex"] = row["lex"]
                    if "pos" in row and "pos" in seg: seg["pos"] = row["pos"]
            tok["lex"] = row["lex"]
        if json.dumps(tok, ensure_ascii=False, sort_keys=True) != before: changed += 1
        fx = dict(fixes.get(key, {}))
        fx["irab"] = dict(tok["irab"])
        if "grammar" in row: fx["tags"] = list(row["grammar"])
        if "pos" in row: fx["pos"] = "verb" if row["pos"] == "verb" else ("noun" if row["pos"] in ("noun", "propn", "adj") else fx.get("pos", row["pos"]))
        if "lex" in row: fx["key"] = row["lex"]
        fixes[key] = fx
    print(f"{pkg_id}: {len(notes)} rows, {changed} tokens changed" + (" (dry run — nothing written)" if dry else ""))
    if dry: return
    for ch, data in chapters.items():
        (pkg / "chapters" / f"{ch}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    fixes_path.write_text(json.dumps(fixes, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
