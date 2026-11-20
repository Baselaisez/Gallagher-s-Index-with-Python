#!/usr/bin/env python3
"""hand183.py — (wave 183) four authored corrections in «الْأُصُولُ الْمُنِيفَةُ» that the doer audit brought to light
(a verb line promising a hidden doer while a later word claimed to be its doer: the later word was the one mislabelled).
Writes them into fixes.json (so a regeneration keeps them) and, with --apply, into the shipped package.

  2:s3    وَلَأَنْ يَتَفَقَّهَ الرَّجُلُ كَيْفَ يَعْبُدُ رَبَّهُ خَيْرٌ لَهُ مِنْ أَنْ يَجْمَعَ الْعِلْمَ الْكَثِيرَ
          — the lām is the lām of ibtidāʾ and «أَنْ» the maṣdar-maker that puts يَتَفَقَّهَ in naṣb (the line read «لِأَنَّ»);
            the clause it makes is the mubtadaʾ and «خَيْرٌ» its KHABAR (the line called it the doer of يَعْبُدُ, whose doer
            is the hidden pronoun returning to «الرَّجُلُ»); «كَيْفَ» is the interrogative noun in the seat of a ḥāl
  29:s1   فِي زَمَانٍ مِقْدَارُهُ …  — «مِقْدَارُهُ» opens the clause that describes «زَمَانٍ»: a mubtadaʾ, not the doer of
          «وَيَبْعَثُهُمْ» (whose doer is the hidden pronoun returning to the Name)

The written vowels are left exactly as shipped; only the lines that name them change.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "al-usul-al-munifa"
FIX = {
 "2:s3:0": {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لَامُ الِابْتِدَاءِ، وَ«أَنْ» حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ يَتَفَقَّهَ» فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
                     "en": "The waw conjoins; the lam of ibtida' (emphasis); «أَنْ» — the masdar-maker that governs nasb: the clause it makes («that a man gain understanding») stands in the place of raf' as the mubtada.",
                     "tr": "«ve» + ibtidâ (te'kîd) lâmı + «أَنْ» — masdariyye, nasbeder: kurduğu te'villi masdar («kişinin fıkıh öğrenmesi») ref mahallinde mübtedâdır."},
            "pos": "part", "key": "an-masdariyya", "tags": ["an-masdariyya", "mubtada-khabar"],
            "segments": [{"form": "وَ", "lex": "wa", "pos": "conj"}, {"form": "لَأَنْ", "lex": "an-masdariyya", "pos": "part"}]},
 "2:s3:3": {"irab": {"ar": "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.",
                     "en": "An interrogative noun, built on the fatha, in the place of nasb as a hal («in what manner»).",
                     "tr": "İstifham ismi, fetha üzere mebnî; nasb mahallinde hâl («ne şekilde»)."},
            "pos": "noun", "tags": ["al-istifham"]},
 "2:s3:6": {"irab": {"ar": "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ — وَالْمُبْتَدَأُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ يَتَفَقَّهَ».",
                     "en": "The khabar, in raf'; the sign is the damma — its mubtada is the masdar clause «أَنْ يَتَفَقَّهَ».",
                     "tr": "Haber, merfû; alâmeti damme ile — mübtedâsı «أَنْ يَتَفَقَّهَ» te'villi masdarıdır."},
            "pos": "noun", "tags": ["mubtada-khabar"]},
 "29:s1:13": {"irab": {"ar": "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِـ«زَمَانٍ».",
                       "en": "The mubtada, in raf'; the sign is the damma; annexed, the pronoun «his/its» is the mudaf ilayh — the clause it opens describes «زَمَانٍ».",
                       "tr": "Mübtedâ, merfû; alâmeti damme ile; muzâf, zamir «onun» muzâfun ileyh — açtığı cümle «زَمَانٍ» kelimesinin sıfatıdır."},
              "pos": "noun", "tags": ["mubtada-khabar", "idafa-definiteness"]},
}


def main():
    fp = HERE / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
    f.update(FIX)
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
