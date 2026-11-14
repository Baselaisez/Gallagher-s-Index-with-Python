#!/usr/bin/env python3
"""hand189.py — (wave 189) «الْعَيْن» in Taṣrīf al-ʿIzzī is the SECOND RADICAL, not the jurist's «specified thing».

The engine keyed every «الْعَيْنُ / عَيْنُهُ» of the ṣarf text to `ayn-thing`, the only noun عَيْن it found first on the
shelf — a fiqh entry («specified thing, corporeal object»). Thirty-five tokens of the matn showed a learner that gloss
on the letter that stands where the ع of «فَعَلَ» stands. Marāḥ al-Arwāḥ, part seven, uses the word both ways in one
chapter (the ʿayn of the verb; «عَيْن» the many-meaninged noun), which is how it was noticed.

Adds the entry `ayn-letter` (lemma عَيْن — the letter, and the second radical) beside `fa-letter` / `lam-letter`, records
it in lemmas.txt so a regeneration keeps it, and — with --apply — re-keys the shipped tokens and their segments and
drops `ayn-thing` from this package's glossary once nothing uses it. Lines and vowels are untouched.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "tasrif-al-izzi"
OLD, NEW = "ayn-thing", "ayn-letter"
ENTRY = {"lemma": "عَيْن", "root": "ع ي ن", "pos": "noun",
         "gloss": {"en": "the letter ʿayn (ع) — in ṣarf, the SECOND radical: the letter of a word that stands where the ع of «فَعَلَ» stands",
                   "tr": "ayn harfi (ع) — sarfta kelimenin İKİNCİ asıl harfi: «فَعَلَ»deki ع'ın yerinde duran harf"},
         "level": 4}
LINE = NEW + " | عَيْن | noun | ع ي ن | " + ENTRY["gloss"]["en"] + " | " + ENTRY["gloss"]["tr"] + " | العين عين\n"


def main():
    lp = HERE / "lemmas.txt"; s = open(lp, encoding="utf-8").read()
    if not any(l.startswith(NEW + " |") for l in s.split("\n")):
        open(lp, "w", encoding="utf-8").write(s + ("" if s.endswith("\n") else "\n") + "# --- (wave 189) the ʿayn of the scale, beside fa-letter and lam-letter\n" + LINE)
        print("lemmas.txt: ayn-letter recorded")
    if "--apply" not in sys.argv: return
    gp = PKG / "glossary.json"; raw = open(gp, encoding="utf-8").read(); g = json.loads(raw); e = g.get("entries", g)
    e[NEW] = ENTRY
    n = 0
    for p in sorted((PKG / "chapters").glob("*.json")):
        r = open(p, encoding="utf-8").read(); d = json.loads(r); hit = 0
        for sen in d["sentences"]:
            for t in sen["tokens"]:
                if t.get("lex") == OLD: t["lex"] = NEW; hit += 1
                for sg in t.get("segments", []):
                    if sg.get("lex") == OLD: sg["lex"] = NEW
        if hit:
            open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if r.endswith("\n") else "")); n += hit
    still = any(t.get("lex") == OLD or any(sg.get("lex") == OLD for sg in t.get("segments", []))
                for p in (PKG / "chapters").glob("*.json") for sen in json.load(open(p, encoding="utf-8"))["sentences"] for t in sen["tokens"])
    if not still: e.pop(OLD, None)
    open(gp, "w", encoding="utf-8").write(json.dumps(g, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""))
    print(n, "tokens re-keyed;", OLD, "kept" if still else "dropped from this glossary")


main()
