#!/usr/bin/env python3
"""hand174.py — (wave 174) two drafted readings the new text's lexicon brought to light.

  «الْمَقَامَاتُ» 2:s37       … فَلَا أَضْرِبُ بِهَا وَجْهَهُ وَأَصْبِرُ حَتَّى يَتُوبَ
      «أَضْرِبُ» is the speaker's muḍāriʿ of ضَرَبَ («I do not strike his face with them»): the fatḥa on the hamza is
      the first person's prefix, and a Form IV muḍāriʿ would wear a ḍamma (أُضْرِبُ). The drafted key was `adraba`
      (أَضْرَبَ, «to turn away from»); the stored line already said «فِعْلٌ مُضَارِعٌ مَرْفُوعٌ … تَقْدِيرُهُ أَنَا» and
      stays. The entry `adraba` had no other token in this package, so it leaves its glossary and morphology
      (al-Kāfiya keeps its own).

  «الْأُصُولُ الْمُنِيفَةُ» 22:s9  فَمِنْ هَاهُنَا قُلْنَا إِنَّ إِيمَانَنَا مِثْلُ إِيمَانِ الْمَلَائِكَةِ …
      «هَاهُنَا» is the tanbīh's hāʾ on «هُنَا», a demonstrative of place, built, in the place of jarr by «مِنْ».
      The drafted line split it «هَاهُ + نَا» and called it a khabar annexed to «our».

The written vowels are left exactly as shipped. Writes into each package's fixes.json (so a regeneration keeps the
fix) and, with --apply, into the shipped chapters.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SAMPLES = HERE.parent.parent / "content" / "samples"

KEYFIX = ("al-maqamat-birgivi", "maqamat", "2:s37:23", "أَضْرِبُ", "adraba", "daraba")
HAHUNA = {"irab": {"ar": "الْهَاءُ لِلتَّنْبِيهِ، وَ«هُنَا» اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِمِنْ.",
                   "en": "The ha calls attention; «هُنَا» is a demonstrative of place, built on sukun, in the place of jarr by «مِنْ»: «from here».",
                   "tr": "Hâ tenbih içindir; «هُنَا» mekân için ism-i işâret, sükûn üzere mebnî; «مِنْ» ile mahallen mecrûr: «buradan»."},
          "tags": ["al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab", "huruf-jarr"]}
LINEFIX = ("al-usul-al-munifa", "usul", "22:s9:1", "هَاهُنَا", HAHUNA)


def used_keys(pkg):
    used = set()
    for cp in sorted((SAMPLES / pkg / "chapters").glob("*.json")):
        for s in json.load(open(cp, encoding="utf-8"))["sentences"]:
            for tk in s["tokens"]:
                used.add(tk.get("lex")); used.update(g.get("lex") for g in tk.get("segments", []))
                if isinstance(tk.get("phrase"), dict): used.add(tk["phrase"].get("lex"))
    return used


def main():
    apply = "--apply" in sys.argv
    # 1 — the key
    pkg, folder, where, word, old, new = KEYFIX
    fp = HERE / folder / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
    f[where] = {**(f.get(where) or {}), "key": new}
    json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(pkg, len(f), "fixes in fixes.json")
    if apply:
        ch, sid, i = where.split(":"); p = SAMPLES / pkg / "chapters" / f"{ch}.json"; d = json.load(open(p, encoding="utf-8"))
        t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][int(i)]
        assert t["surface"]["full"] == word, t["surface"]["full"]
        assert t["lex"] in (old, new), t["lex"]
        print(f"{where} {word}: {t['lex']} -> {new}"); t["lex"] = new
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        used = used_keys(pkg); assert new in used
        if old not in used:   # the entry no token reaches any more leaves the package
            for name, holder_key in (("glossary.json", "entries"), ("morphology.json", "verbs")):
                q = SAMPLES / pkg / name; g = json.load(open(q, encoding="utf-8"))
                if old in g.get(holder_key, {}):
                    g[holder_key].pop(old); json.dump(g, open(q, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print("  removed", old, "from", name)
    # 2 — the line
    pkg, folder, where, word, v = LINEFIX
    fp = HERE / folder / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
    f[where] = {**(f.get(where) or {}), "irab": dict(v["irab"]), "tags": list(v["tags"])}
    json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(pkg, len(f), "fixes in fixes.json")
    if apply:
        ch, sid, i = where.split(":"); p = SAMPLES / pkg / "chapters" / f"{ch}.json"; d = json.load(open(p, encoding="utf-8"))
        t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][int(i)]
        assert t["surface"]["full"] == word, t["surface"]["full"]
        print(f"{where} {word}\n   - {t['irab']['ar']}\n   + {v['irab']['ar']}")
        t["irab"] = dict(v["irab"]); t["grammar"] = list(v["tags"]); t.pop("segments", None)
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        used = used_keys(pkg)
        q = SAMPLES / pkg / "glossary.json"; g = json.load(open(q, encoding="utf-8"))
        dead = [k for k in g["entries"] if k not in used]
        if dead: print("  NOTE entries no token reaches now:", dead)


if __name__ == "__main__":
    main()
