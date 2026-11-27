#!/usr/bin/env python3
"""hand185.py — (wave 185) the twenty-seven bare «اسْمٌ.» lines of «الْأُصُولُ الْمُنِيفَةُ» given their iʿrāb.

The engine had named each of these words a noun and stopped. Each was read in its sentence:

  the modality «بِلَا كَيْفٍ» (six)     majrūr after the bāʾ across the negating لَا — and keyed to the NOUN كَيْف, not the question كَيْفَ
  the question كَيْفَ (four)            the fronted khabar of يَكُونُ / أَصْبَحَ, or the ḥāl of the doer of نُقَاتِلُ
  إِذْ (four)                           the built ẓarf of past time, annexed to its clause (with the sense of cause in 22:s11)
  يَوْمَئِذٍ (two)                       the ẓarf يَوْمَ annexed to إِذْ, whose tanwīn stands for the dropped clause
  joined after «وَلَا»                  5:s7 وَلَا حَرْفٍ · 15:s4 وَلَا كَبِيرَةً · 32:s6 وَلَا حَدٌّ وَلَا قِصَاصٌ
  the rest                              2:s25 اثْنَتَيْنِ · 14:s30 / 14:s34 الْعَمَى · 22:s12 الْمَؤُونَاتِ · 24:s14 أَوَكَانُوا · 24:s15 الْأُخْرَى ·
                                        29:s1 خَمْسِينَ (the āya's wording kept; keyed to خَمْسُونَ, not خَمْس)

Writes them into fixes.json (so a regeneration keeps them) and, with --apply, into the shipped package.
The written vowels are left exactly as shipped; only the lines that name them change.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent.parent.parent / "content" / "samples" / "al-usul-al-munifa"


def row(bare, ar, en, tr, **kw): return dict({"bare": bare, "irab": {"ar": ar, "en": en, "tr": tr}}, **kw)


KAYF = lambda: row("كيف", "مَجْرُورٌ بِالْبَاءِ فِي «بِلَا» بِالْكَسْرَةِ — وَ«لَا» مُعْتَرِضَةٌ بَيْنَ الْجَارِّ وَالْمَجْرُورِ بِمَعْنَى «غَيْر».",
                   "In jarr by the bāʾ of «بِلَا»; the sign is the kasra — «لَا» stands between the preposition and its noun with the sense of «غَيْر» (without).",
                   "«بِلَا»daki bâ ile mecrûr; alâmeti kesre ile — «لَا», câr ile mecrûr arasına «غَيْر» mânâsıyla girmiştir.", key="kayf", pos="noun")
IDH = lambda extra_ar="", extra_en="", extra_tr="": row("إذ", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ" + extra_ar + ".",
                   "An adverb of past time («when»), built on sukun, in the place of nasb; annexed to the clause after it" + extra_en + ".",
                   "Geçmiş zaman zarfı («-diği zaman»), sükûn üzere mebnî, mahallen mansûb; kendisinden sonraki cümleye muzâftır" + extra_tr + ".", pos="noun")
YAWM = lambda: row("يومئذ", "«يَوْمَ» ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ«إِذٍ» ظَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْجُمْلَةِ الْمَحْذُوفَةِ.",
                   "«يَوْمَ» is an adverb of time, in nasb; the sign is the fatha; annexed — and «إِذٍ» is a built adverb in the place of jarr as the mudaf ilayh; its tanwin stands for the clause left out.",
                   "«يَوْمَ» zaman zarfı, mansûb; alâmeti fetha ile; muzâf — «إِذٍ» mebnî zarf, mahallen mecrûr muzâfun ileyh; tenvini hazfedilen cümlenin yerine gelmiştir.", pos="noun")
AMA = lambda: row("العمى", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The object (maf'ul bih), in nasb; the sign is a fatha estimated on the alif.", "Mef'ûlün bih, mansûb; alâmeti elif üzerinde takdîrî fetha ile.", pos="noun")
def KAYFA(seat_ar, seat_en, seat_tr):
    return row("كيف", "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ " + seat_ar + ".", "An interrogative noun («how»), built on fatha, " + seat_en + ".", "İstifham ismi («nasıl»), feth üzere mebnî, " + seat_tr + ".", pos="noun")
def ATF(bare, case_ar, case_en, case_tr, on):
    return row(bare, "مَعْطُوفٌ عَلَى «" + on + "» " + case_ar + ".", "Joined to «" + on + "», " + case_en + ".", "«" + on + "» üzerine ma'tûf, " + case_tr + ".", pos="noun")


FIX = {
 "2:s25:19": row("اثنتين", "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى — أَيْ: بَالِغِينَ هٰذَا الْعَدَدَ — أَوْ نَائِبٌ عَنِ الْمَصْدَرِ.",
                 "A hal, in nasb; the sign is the yāʾ — it follows the dual: «split, reaching this number» — or it stands in for the masdar.",
                 "Hâl, mansûb; alâmeti yâ ile — tesniyeye mülhaktır: «bu sayıya ulaşarak ayrıldılar» — yahut masdardan nâibdir.", pos="noun"),
 "3:s1:31": IDH(),
 "5:s3:29": KAYFA("فِي مَحَلِّ نَصْبٍ خَبَرُ «يَكُونُ» مُقَدَّمٌ، وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ — أَوْ حَالٌ إِنْ جُعِلَتْ «يَكُونُ» تَامَّةً", "in the place of nasb as the fronted khabar of «يَكُونُ», whose noun is a hidden pronoun — or a hal, if «يَكُونُ» is taken as complete", "mahallen mansûb, «يَكُونُ»nün öne geçmiş haberi; ismi gizli zamirdir — «يَكُونُ» tam sayılırsa hâldir"),
 "5:s3:41": KAYFA("فِي مَحَلِّ نَصْبٍ خَبَرُ «يَكُونُ» مُقَدَّمٌ، وَاسْمُهَا «فَنَاؤُهُ»", "in the place of nasb as the fronted khabar of «يَكُونُ», whose noun is «فَنَاؤُهُ»", "mahallen mansûb, «يَكُونُ»nün öne geçmiş haberi; ismi «فَنَاؤُهُ»dur"),
 "5:s7:25": ATF("حرف", "مَجْرُورٌ بِالْكَسْرَةِ", "in jarr; the sign is the kasra", "mecrûr; alâmeti kesre ile", "آلَةٍ"),
 "8:s1:10": KAYF(), "8:s1:24": KAYF(), "8:s3:53": KAYF(), "9:s3:24": KAYF(), "9:s3:29": KAYF(), "9:s3:45": KAYF(),
 "14:s30:31": AMA(), "14:s34:6": AMA(),
 "15:s4:33": ATF("كبيرة", "مَنْصُوبٌ بِالْفَتْحَةِ", "in nasb; the sign is the fatha", "mansûb; alâmeti fetha ile", "صَغِيرَةً"),
 "20:s2:27": KAYFA("فِي مَحَلِّ نَصْبٍ خَبَرُ «أَصْبَحَ» مُقَدَّمٌ، وَالتَّاءُ بَعْدَهُ اسْمُهَا", "in the place of nasb as the fronted khabar of «أَصْبَحَ», whose noun is the tāʾ after it", "mahallen mansûb, «أَصْبَحَ»nin öne geçmiş haberi; ismi ondan sonraki tâdır"),
 "20:s6:16": YAWM(),
 "22:s11:33": IDH("، وَفِيهِ مَعْنَى التَّعْلِيلِ", "; it carries the sense of cause («since»)", "; ta'lîl mânâsı taşır («çünkü»)"),
 "22:s12:24": row("المؤونات", "مَفْعُولٌ بِهِ لِلْمَصْدَرِ «تَحَمُّل» مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
                  "The object of the masdar «تَحَمُّل», in nasb; the sign is the kasra in place of the fatha — a sound feminine plural.",
                  "«تَحَمُّل» masdarının mef'ûlü, mansûb; alâmeti fetha yerine kesre ile — cem'-i müennes sâlim.", pos="noun"),
 "23:s6:52": IDH(),
 "24:s11:37": IDH(),
 "24:s14:30": row("أوكانوا", "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْوَاوُ عَاطِفَةٌ، وَ«كَانُوا» فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.",
                  "The hamza asks; the waw conjoins; «كَانُوا» is an incomplete past verb, built on damma for the waw of the group, and that waw is its noun.",
                  "Hemze istifham içindir; vâv atıf harfidir; «كَانُوا» nâkıs mâzî fiil, cemaat vâvına bitiştiği için damm üzere mebnî; o vâv ismidir.", pos="verb", tags=["kana-wa-akhawatuha"]),
 "24:s15:61": row("الأخرى", "خَبَرُ الْمُبْتَدَإِ «مَا» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The khabar of the mubtada «مَا», in raf'; the sign is a damma estimated on the alif.", "«مَا» mübtedâsının haberi, merfû; alâmeti elif üzerinde takdîrî damme ile.", pos="noun"),
 "25:s19:35": YAWM(),
 "29:s1:14": row("خمسين", "مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، عَلَى حِكَايَةِ لَفْظِ الْآيَةِ حَيْثُ هُوَ خَبَرُ «كَانَ» — كَذَا فِي الْأَصْلِ، وَالْقِيَاسُ هُنَا الرَّفْعُ لِأَنَّهُ خَبَرُ «مِقْدَارُهُ».",
                 "In nasb; the sign is the yāʾ — it follows the sound masculine plural; the āya's wording is kept, where it is the khabar of «كَانَ» — so the source has it; by rule it would be in raf' here, as the khabar of «مِقْدَارُهُ».",
                 "Mansûb; alâmeti yâ ile — cem'-i müzekker sâlime mülhaktır; «كَانَ»nin haberi olduğu âyetin lafzı aynen korunmuştur — asılda böyledir; kıyâsen burada «مِقْدَارُهُ»nun haberi olarak merfû olurdu.", key="khamsun", pos="noun"),
 "32:s5:19": KAYFA("فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «نُقَاتِلُ»", "in the place of nasb as a hal of the doer of «نُقَاتِلُ»", "mahallen mansûb, «نُقَاتِلُ»nün fâilinden hâl"),
 "32:s6:80": row("حد", "مَعْطُوفٌ عَلَى مَحَلِّ «لَا غَرَامَةَ» مَرْفُوعٌ بِالضَّمَّةِ — وَمَحَلُّ «لَا» مَعَ اسْمِهَا الرَّفْعُ بِالِابْتِدَاءِ.",
                 "Joined to the PLACE of «لَا غَرَامَةَ», in raf'; the sign is the damma — «لَا» with its noun stands in the place of a mubtada.",
                 "«لَا غَرَامَةَ»nin MAHALLİNE ma'tûf, merfû; alâmeti damme ile — «لَا» ismiyle birlikte mübtedâ mahallindedir.", pos="noun"),
 "32:s6:82": ATF("قصاص", "مَرْفُوعٌ بِالضَّمَّةِ", "in raf'; the sign is the damma", "merfû; alâmeti damme ile", "حَدٌّ"),
}


def main():
    fp = HERE / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
    for k, v in FIX.items(): f[k] = dict(f.get(k, {}), **{x: y for x, y in v.items() if x != "bare"})
    json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(len(f), "fixes in fixes.json")
    if "--apply" not in sys.argv: return
    by = {}
    for k, v in FIX.items(): ch, sid, i = k.split(":"); by.setdefault(ch, []).append((sid, int(i), v))
    n = 0
    for ch, rows in by.items():
        p = PKG / "chapters" / f"{ch}.json"; d = json.load(open(p, encoding="utf-8"))
        for sid, i, v in rows:
            t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][i]
            assert t["surface"]["bare"] == v["bare"], (ch, sid, i, t["surface"]["bare"], v["bare"])
            assert t["irab"]["ar"].strip() in ("اسْمٌ.", v["irab"]["ar"]), (ch, sid, i, t["irab"]["ar"])
            t["irab"] = dict(v["irab"]); n += 1
            if "tags" in v: t["grammar"] = list(v["tags"])
            if "pos" in v: t["pos"] = v["pos"]
            if "key" in v: t["lex"] = v["key"]
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(n, "lines written")


if __name__ == "__main__":
    main()
