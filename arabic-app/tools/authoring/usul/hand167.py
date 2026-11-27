#!/usr/bin/env python3
"""hand167.py — (wave 167) five authored corrections in «الْأُصُولُ الْمُنِيفَةُ» that no line-level rule reaches.
Writes them into fixes.json (so a regeneration keeps them) and, with --apply, into the shipped package.

  6:s5   وَلَمْ يَكُنْ مِنْ إِرَادَتِهِ تَعَالَى ذَبْحُهُ   — ذَبْحُهُ is the postponed noun of يَكُنْ, not a doer; يَكُنْ hides no noun
  7:s3   وَكَلَامُهُ تَعَالَى مَقْرُوءٌ مَحْفُوظٌ          — a new clause: mubtadaʾ, khabar, second khabar (not «اسْمُ كَانَ … فَاعِلٌ … نَعْتٌ»)
  31:s2  كَمَا يُرَى الْكَوْكَبُ الدُّرِّيُّ               — الْكَوْكَبُ is the deputy doer of the passive يُرَى
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "al-usul-al-munifa"
MD = "، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ"
FIX = {
 "6:s5:14": {"irab": {"ar": "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَجْزُومٌ بِـ«لَمْ»، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهَا «ذَبْحُهُ» الْمُؤَخَّرُ.",
                      "en": "A present verb, one of kāna's sisters, in jazm after «lam» — its sign is the sukūn; its noun is the postponed «dhabḥuhu».",
                      "tr": "Kâne'nin kardeşlerinden muzâri fiil, «lem» ile meczûm — alâmeti sükûn; ismi sonra gelen «zebhuhû»dur."}, "pos": "verb"},
 "6:s5:18": {"irab": {"ar": "اسْمُ «يَكُنْ» مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ" + MD + "، وَخَبَرُهَا الْجَارُّ وَالْمَجْرُورُ الْمُتَقَدِّمُ «مِنْ إِرَادَتِهِ».",
                      "en": "The postponed noun of «yakun», in rafʿ by the ḍamma; annexed, the pronoun is its muḍāf ilayh; the predicate is the fronted phrase «min irādatihi».",
                      "tr": "«yekün»ün muahhar ismi, damme ile merfû; muzâf, zamir muzâfun ileyh; haberi öne geçmiş câr-mecrûr «min irâdetihî»dir."}, "pos": "noun", "tags": ["kana-wa-akhawatuha", "idafa-definiteness"]},
 "7:s3:15": {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ" + MD + ".",
                      "en": "The wāw conjoins; the mubtadaʾ, in rafʿ by the ḍamma; annexed, the pronoun is its muḍāf ilayh.",
                      "tr": "Vâv atıf harfi; mübtedâ, damme ile merfû; muzâf, zamir muzâfun ileyh."}, "pos": "noun", "tags": ["mubtada-khabar", "idafa-definiteness"]},
 "7:s3:17": {"irab": {"ar": "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "en": "The khabar (predicate), in raf'; the sign is the damma.", "tr": "Haber, merfû; alâmeti damme ile."}, "pos": "noun", "tags": ["mubtada-khabar"]},
 "7:s3:18": {"irab": {"ar": "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ.", "en": "A second khabar, in raf'; the sign is the damma.", "tr": "İkinci haber, merfû; alâmeti damme ile."}, "pos": "noun", "tags": ["mubtada-khabar"]},
 "31:s2:33": {"irab": {"ar": "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ.",
                       "en": "A present verb in the passive, in raf'; the sign is a damma implied on the alif.",
                       "tr": "Meçhul muzâri fiil, merfû; alâmeti elif üzerinde takdîrî damme."}, "pos": "verb"},
 "31:s2:34": {"irab": {"ar": "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "en": "The deputy doer (na'ib al-fa'il), in raf'; the sign is the damma.", "tr": "Nâib-i fâil, merfû; alâmeti damme ile."}, "pos": "noun", "tags": ["naib-al-fail"]},
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
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
