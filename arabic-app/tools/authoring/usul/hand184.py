#!/usr/bin/env python3
"""hand184.py — (wave 184) seventeen «مَا» lines of «الْأُصُولُ الْمُنِيفَةُ» corrected after the seat audit.

The engine-authored lines had named the face of «مَا» by the word next to it (مَا لَمْ → «ظَرْفِيَّة», وَمَا + verb →
«نَافِيَة») where the SEAT says otherwise. Each line below was read in its sentence:

  the relative in a governed seat    2:s2 وَمَا يَتَعَلَّقُ · 6:s11 مَا لَمْ يَقْضِ · 14:s20 (twice) إِنَّكُمْ وَمَا تَعْبُدُونَ ·
                                     15:s6 وَمَا آتَاكُمُ الرَّسُولُ · 18:s10 وَمَا أُنْزِلَ إِلَى إِبْرَاهِيمَ · 19:s13 يَقُولُونَ مَا سَمِعُوا ·
                                     22:s10 عَايَنُوا … مَا لَمْ نُعَايِنْ · 25:s1 مَا كَانَ مِنَ السَّيِّئَاتِ · 25:s17 مَا لَمْ يَذْكُرْهُ ·
                                     26:s4 وَالثَّالِثَةُ مَا كَانَ مِنْ عَمَلٍ
  the question                       20:s8 وَمَا لَهُمْ لَا يَقُولُونَ
  the negation                       14:s18 مَا مِنْ نَبِيٍّ … إِلَّا · 14:s20 مَا أَنْتُمْ عَلَيْهِ بِفَاتِنِينَ · 25:s4 وَمَا أَسْتَطِيعُ أَنْ أُمْضِيَ
  the masdar-making letter           14:s35 مَا خَلَا الطَّاعَةَ · 24:s17 مَا دَامُوا

Writes them into fixes.json (so a regeneration keeps them) and, with --apply, into the shipped package.
The written vowels are left exactly as shipped; only the lines that name them change.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "al-usul-al-munifa"

W_AR, W_EN, W_TR = "الْوَاوُ عَاطِفَةٌ، وَ", "The waw conjoins; ", "«ve» + "


def maw(seat_ar, seat_en, seat_tr, sila, aid_ar, aid_en, aid_tr, waw=False):
    ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if waw else "") + f"اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ {seat_ar}، وَصِلَتُهُ جُمْلَةُ «{sila}»، {aid_ar}."
    en = (W_EN + "a" if waw else "A") + f" relative pronoun — built (mabni), {seat_en}; its clause is «{sila}»; {aid_en}."
    tr = (W_TR if waw else "") + f"İsm-i mevsûl — mebnî, {seat_tr}; sılası «{sila}» cümlesidir; {aid_tr}."
    d = {"irab": {"ar": ar, "en": en, "tr": tr}, "pos": "pron", "key": "ma-mawsula", "tags": ["ism-mawsul"]}
    if waw: d["segments"] = [{"form": "وَ", "lex": "wa", "pos": "conj"}, {"form": "مَا", "lex": "ma-mawsula", "pos": "part"}]
    return d


AID_DROP = lambda x: (f"وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ «{x}»", f"the returning pronoun is dropped («{x}»)", f"âid zamiri hazfedilmiştir («{x}»)")
AID_KANA = ("وَالْعَائِدُ اسْمُ «كَانَ» الْمُسْتَتِرُ", "the returning pronoun is the hidden noun of «كَانَ»", "âid, «كَانَ»nin gizli ismidir")
AID_IN = ("وَالْعَائِدُ الضَّمِيرُ فِيهَا", "the returning pronoun stands inside it", "âid zamiri içindedir")

FIX = {
 "2:s2:7": maw("فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى مَا قَبْلَهُ", "joined to what precedes, in the place of nasb", "öncesine ma'tûf, nasb mahallinde", "يَتَعَلَّقُ مِنْهَا بِالِاعْتِقَادِيَّاتِ", *AID_IN, waw=True),
 "6:s11:12": maw("فِي مَحَلِّ رَفْعٍ فَاعِلُ «يَجْرِيَ»", "in the place of raf' as the doer of «يَجْرِيَ»", "ref mahallinde «يَجْرِيَ» fiilinin fâili", "لَمْ يَقْضِ", *AID_DROP("لَمْ يَقْضِهِ")),
 "14:s18:17": {"irab": {"ar": "«مَا» نَافِيَةٌ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ — وَ«مِنْ» بَعْدَهَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ، وَالنَّفْيُ مَعَ «إِلَّا» قَصْرٌ.",
                        "en": "«not» — the negation; the مِنْ after it is the extra one that strengthens the denial, and the denial with «إِلَّا» confines: «there is no prophet … but he warned».",
                        "tr": "«değil» — nefiy mâsı; ardındaki مِنْ nefyi pekiştiren zâid harftir, nefiy ise «إِلَّا» ile kasr bildirir: «hiçbir peygamber yoktur ki … uyarmamış olsun»."},
               "pos": "part", "key": "ma-nafiya", "tags": []},
 "14:s20:28": maw("فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى اسْمِ «إِنَّ»", "in the place of nasb, joined to the noun of «إِنَّ»", "nasb mahallinde, «إِنَّ»nin ismine ma'tûf", "تَعْبُدُونَ", *AID_DROP("تَعْبُدُونَهُ"), waw=True),
 "14:s20:41": maw("فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى اسْمِ «إِنَّ»", "in the place of nasb, joined to the noun of «إِنَّ»", "nasb mahallinde, «إِنَّ»nin ismine ma'tûf", "تَعْبُدُونَ", *AID_DROP("تَعْبُدُونَهُ"), waw=True),
 "14:s20:43": {"irab": {"ar": "«مَا» نَافِيَةٌ تَعْمَلُ عَمَلَ «لَيْسَ» (الْحِجَازِيَّةُ)، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ — وَالْبَاءُ فِي خَبَرِهَا «بِفَاتِنِينَ» زَائِدَةٌ.",
                        "en": "«not» — the negation that governs like «لَيْسَ» (the Hijazi ma); the bāʾ on its predicate «بِفَاتِنِينَ» is the extra one.",
                        "tr": "«değil» — «لَيْسَ» gibi amel eden nefiy mâsı (Hicâziyye); haberi «بِفَاتِنِينَ»deki bâ zâidedir."},
               "pos": "part", "key": "ma-hijaziyya", "tags": ["ma-la-mushabbaha"]},
 "14:s35:17": {"irab": {"ar": "«مَا» مَصْدَرِيَّةٌ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ — «مَا خَلَا»: وَ«خَلَا» بَعْدَهَا فِعْلٌ لِلِاسْتِثْنَاءِ يَنْصِبُ مَا بَعْدَهُ.",
                        "en": "The masdar-making ma, a letter — «مَا خَلَا»: after it «خَلَا» is a verb of exception and puts what follows in nasb («except obedience and disobedience»).",
                        "tr": "Masdariyye mâ, harf — «مَا خَلَا»: ardındaki «خَلَا» istisnâ fiilidir ve sonrasını nasbeder («tâat ve mâsiyet hâriç»)."},
               "pos": "part", "key": "ma-masdariyya", "tags": []},
 "15:s6:25": maw("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ (وَيَجُوزُ أَنْ تَكُونَ شَرْطِيَّةً)", "in the place of raf' as a mubtada (it may also be read as the conditional ma)", "ref mahallinde mübtedâ (şartiyye de okunabilir)", "آتَاكُمُ الرَّسُولُ", "وَالْعَائِدُ مَحْذُوفٌ، وَخَبَرُهُ جُمْلَةُ «فَخُذُوهُ»", "the returning pronoun is dropped, and its khabar is the clause «فَخُذُوهُ»", "âid zamiri hazfedilmiştir; haberi «فَخُذُوهُ» cümlesidir", waw=True),
 "18:s10:7": maw("فِي مَحَلِّ جَرٍّ مَعْطُوفٌ عَلَى لَفْظِ الْجَلَالَةِ", "in the place of jarr, joined to the Name", "cer mahallinde, lafza-i celâle ma'tûf", "أُنْزِلَ إِلَى إِبْرَاهِيمَ …", *AID_IN, waw=True),
 "19:s13:17": maw("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَقُولُونَ»", "in the place of nasb as the object of «يَقُولُونَ»", "nasb mahallinde «يَقُولُونَ»nin mef'ûlü", "سَمِعُوا", *AID_DROP("سَمِعُوهُ")),
 "20:s8:36": {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَ«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ «لَهُمْ» (مَا لَهُمْ = أَيُّ شَيْءٍ لَهُمْ).",
                       "en": "The waw conjoins; «مَا» is an interrogative noun, built, in the place of raf' as the mubtada; its khabar is «لَهُمْ» («what is it with them that …?»).",
                       "tr": "«ve» + «مَا» istifham ismi, mebnî, ref mahallinde mübtedâ; haberi «لَهُمْ»dür («onlara ne oluyor ki …?»)."},
              "pos": "pron", "key": "ma-istifham", "tags": ["al-istifham"],
              "segments": [{"form": "وَ", "lex": "wa", "pos": "conj"}, {"form": "مَا", "lex": "ma-istifham", "pos": "pron"}]},
 "22:s10:32": maw("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«عَايَنُوا»", "in the place of nasb as the object of «عَايَنُوا»", "nasb mahallinde «عَايَنُوا»nun mef'ûlü", "لَمْ نُعَايِنْ", *AID_DROP("لَمْ نُعَايِنْهُ")),
 "24:s17:25": {"irab": {"ar": "«مَا» مَصْدَرِيَّةٌ ظَرْفِيَّةٌ (مَا دَامُوا = مُدَّةَ دَوَامِهِمْ)، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.",
                        "en": "«as long as» — the masdar-making ma of time before «دَامَ», a letter.",
                        "tr": "«… olduğu müddetçe» — «دَامَ»den önce zarfiyye masdariyye mâ, harf."},
               "pos": "part", "key": "ma-masdariyya", "tags": []},
 "25:s1:32": maw("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "in the place of raf' as a mubtada", "ref mahallinde mübtedâ", "كَانَ مِنَ السَّيِّئَاتِ …", *AID_KANA),
 "25:s4:41": {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَ«مَا» نَافِيَةٌ، حَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ.",
                       "en": "The waw conjoins; «not» — the negation before a verb.",
                       "tr": "«ve» + «değil / -madı» — fiilden önce nefiy mâsı."},
              "pos": "part", "key": "ma-nafiya", "tags": [],
              "segments": [{"form": "وَ", "lex": "wa", "pos": "conj"}, {"form": "مَا", "lex": "ma-nafiya", "pos": "part"}]},
 "25:s17:21": maw("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«ذَكَرَ»", "in the place of nasb as the object of «ذَكَرَ»", "nasb mahallinde «ذَكَرَ»nin mef'ûlü", "لَمْ يَذْكُرْهُ", "وَالْعَائِدُ الْهَاءُ فِي «يَذْكُرْهُ»", "the returning pronoun is the hāʾ of «يَذْكُرْهُ»", "âid, «يَذْكُرْهُ»daki hâ zamiridir"),
 "26:s4:83": maw("فِي مَحَلِّ رَفْعٍ خَبَرُ «الثَّالِثَةُ»", "in the place of raf' as the khabar of «الثَّالِثَةُ»", "ref mahallinde «الثَّالِثَةُ»nün haberi", "كَانَ مِنْ عَمَلٍ …", *AID_KANA),
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
            assert t["surface"]["bare"] in ("ما", "وما", "فما"), (ch, sid, i, t["surface"]["full"])
            print(f"{ch}:{sid}:{i} {t['surface']['full']}\n   - {t['irab']['ar']}\n   + {v['irab']['ar']}")
            t["irab"] = dict(v["irab"])
            if "tags" in v: t["grammar"] = list(v["tags"])
            if "pos" in v: t["pos"] = v["pos"]
            if "key" in v: t["lex"] = v["key"]
            if "segments" in v: t["segments"] = [dict(x) for x in v["segments"]]
            elif "segments" in t and t["surface"]["bare"] == "ما": t.pop("segments")
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
