#!/usr/bin/env python3
"""hand169.py — (wave 169) four authored corrections in «الْأُصُولُ الْمُنِيفَةُ» that the مَا rules brought to light.
Writes them into fixes.json (so a regeneration keeps them) and, with --apply, into the shipped package.

  30:s3   فَمَا تَنْفَعُهُمْ شَفَاعَةُ الشَّافِعِينَ      — the negating مَا before its verb and its stated doer, not a relative
  31:s11  أَوَلَيْسَ الْقَائِلُ مَا أَحَدٌ مِنَ النَّاسِ أَحَبُّ   — لَيْسَ is the frozen māḍī of kāna's sisters (the line called it a manṣūb
          muḍāriʿ); الْقَائِلُ is ITS noun; and the مَا opens the quoted «no one … is dearer», the negation that governs
          nothing here (the book's own translation reads it so)

The written vowels are left exactly as shipped; only the lines that name them change.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "al-usul-al-munifa"
FIX = {
 "30:s3:60": {"irab": {"ar": "الْفَاءُ عَاطِفَةٌ، وَ«مَا» نَافِيَةٌ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.",
                       "en": "The fa conjoins; «not» — the negation before a verb.",
                       "tr": "«bunun üzerine» + «değil / -madı» — fiilden önce nefiy mâsı."},
              "pos": "part", "key": "ma-nafiya", "tags": [],
              "segments": [{"form": "فَ", "lex": "fa", "pos": "conj"}, {"form": "مَا", "lex": "ma-nafiya", "pos": "part"}]},
 "31:s11:20": {"irab": {"ar": "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ.",
                        "en": "The hamza asks, the waw conjoins; a past verb — one of kāna's sisters: it raises its noun and puts its predicate in naṣb.",
                        "tr": "Soru hemzesi + «ve» + mâzî fiil — kâne'nin kardeşlerinden: ismini ref, haberini nasb eder."},
               "pos": "verb", "tags": ["kana-wa-akhawatuha"]},
 "31:s11:21": {"irab": {"ar": "اسْمُ لَيْسَ مَرْفُوعٌ بِالضَّمَّةِ.",
                        "en": "The noun of laysa, in raf'; the sign is the damma.",
                        "tr": "Leyse'nin ismi, merfû; alâmeti damme ile."},
               "pos": "noun", "tags": ["kana-wa-akhawatuha"]},
 "31:s11:22": {"irab": {"ar": "«مَا» نَافِيَةٌ لَا عَمَلَ لَهَا، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.",
                        "en": "«not» — the negation; it governs nothing here: a mubtadaʾ and its khabar follow.",
                        "tr": "«değil» — nefiy mâsı; burada amel etmez: ardından mübtedâ ve haberi gelir."},
               "pos": "part", "key": "ma-nafiya", "tags": []},
}


def main():
    fp = HERE / "fixes.json"; f = json.load(open(fp, encoding="utf-8")); f.update(FIX)
    json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(len(f), "fixes in fixes.json")
    if "--apply" not in sys.argv: return
    by = {}
    for k, v in FIX.items(): ch, sid, i = k.split(":"); by.setdefault(ch, []).append((sid, int(i), v))
    for ch, rows in by.items():
        p = PKG / "chapters" / f"{ch}.json"; d = json.load(open(p, encoding="utf-8"))
        for sid, i, v in rows:
            t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][i]
            print(f"{ch}:{sid}:{i} {t['surface']['full']}\n   - {t['irab']['ar']}\n   + {v['irab']['ar']}")
            t["irab"] = dict(v["irab"])
            if "tags" in v: t["grammar"] = list(v["tags"])
            if "pos" in v: t["pos"] = v["pos"]
            if "key" in v: t["lex"] = v["key"]
            if "segments" in v: t["segments"] = [dict(x) for x in v["segments"]]
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
