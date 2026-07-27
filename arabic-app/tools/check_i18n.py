#!/usr/bin/env python3
"""Fail when any user-visible string exists in English but not in Turkish.

The app is bilingual by contract, and the gaps that got through were never the
prose — explanations and common mistakes were translated from the start. They
were the small things: a note's title, a worked example's one-line explanation,
a level name. Those are exactly what a checker is for.

Usage:  python3 tools/check_i18n.py          # exit 1 if anything is missing
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Level names live in manifests as plain English and are translated in the
# reader by lookup; every value used must be in that table.
KNOWN_LEVEL_NAMES = {
    "Newbie", "Elementary", "Intermediate", "Upper Intermediate",
    "Advanced", "Master", "Mastery",
}


def bilingual_ok(v):
    return isinstance(v, dict) and v.get("en") and v.get("tr")


def main():
    missing = []

    for f in sorted((ROOT / "content/grammar").glob("*.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        nid = g["id"]
        if not g["title"].get("tr"):
            missing.append(f"grammar/{nid}: title has no tr")
        if not bilingual_ok(g.get("explanation")):
            missing.append(f"grammar/{nid}: explanation not bilingual")
        for i, x in enumerate(g.get("examples", [])):
            if x.get("en") and not x.get("tr"):
                missing.append(f"grammar/{nid}: examples[{i}] has en but no tr")
        for i, m in enumerate(g.get("commonMistakes", [])):
            if not bilingual_ok(m.get("why")):
                missing.append(f"grammar/{nid}: commonMistakes[{i}].why not bilingual")

    for f in sorted(ROOT.glob("content/*/*/manifest.json")):
        m = json.loads(f.read_text(encoding="utf-8"))
        pkg = f.parent.name
        for field in ("title", "subtitle"):
            v = m.get(field)
            if v and not v.get("tr"):
                missing.append(f"{pkg}/manifest: {field} has no tr")
        for ch in m.get("chapters", []):
            if not ch.get("title", {}).get("tr"):
                missing.append(f"{pkg}/manifest: chapter {ch.get('n')} title has no tr")
        ln = m.get("levelName")
        if ln and ln not in KNOWN_LEVEL_NAMES:
            missing.append(f"{pkg}/manifest: levelName {ln!r} has no entry in the reader's LEVEL_TR")

    for f in sorted(ROOT.glob("content/*/*/glossary.json")):
        pkg = f.parent.name
        for lex, e in json.loads(f.read_text(encoding="utf-8"))["entries"].items():
            if not bilingual_ok(e.get("gloss")):
                missing.append(f"{pkg}/glossary: {lex} gloss not bilingual")
            for extra in ("literal", "note"):
                if e.get(extra) and not bilingual_ok(e[extra]):
                    missing.append(f"{pkg}/glossary: {lex} {extra} not bilingual")

    # i'rab Turkish may come from the shared translation memory instead of the
    # token, so apply the same merge the builder does before judging.
    tm_path = ROOT / "content/i18n/irab-tr.json"
    tm = (json.loads(tm_path.read_text(encoding="utf-8")).get("entries", {})
          if tm_path.is_file() else {})

    for f in sorted(ROOT.glob("content/*/*/chapters/*.json")):
        pkg = f.parents[1].name
        d = json.loads(f.read_text(encoding="utf-8"))
        for sen in d["sentences"]:
            where = f"{pkg}/{d['chapter']}:{sen['id']}"
            if not bilingual_ok(sen.get("translation")):
                missing.append(f"{where}: translation not bilingual")
            for i, t in enumerate(sen["tokens"]):
                ir = t.get("irab")
                if ir and ir.get("en") and not (ir.get("tr") or tm.get(ir["en"])):
                    missing.append(f"{where}[{i}]: i'rab «{ir['en'][:48]}» has no tr "
                                   f"and no entry in content/i18n/irab-tr.json")

    if missing:
        for m in missing:
            print(f"  MISSING  {m}")
        print(f"\n{len(missing)} untranslated string(s)")
        return 1
    print("every user-visible string has Turkish")
    return 0


if __name__ == "__main__":
    sys.exit(main())
