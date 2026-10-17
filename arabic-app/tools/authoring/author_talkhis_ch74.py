# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 74: the ILMAM / SALKH (the meaning alone taken) in its three grades, and the HIDDEN taking — the two meanings
resembling each other, the meaning moved to another place, the second's meaning wider, the qalb (the contrary meaning), the addition that
betters — with the closing rule: all of this only where the second is KNOWN to have taken from the first; otherwise «so-and-so said it, and
so-and-so had said it before him». Source lines ~4661-4700 (sahifa 161-164).

  RESTORED (the source carries the rulings only in Turkish): s1, s2, s5, s8, s11, s14, s17, s20, s23, s27, s28 — the received matn, marked.
  The bayts are the source's own printed Arabic: Abu Tammam / al-Mutanabbi (s3-s4), al-Buhturi / al-Mutanabbi (s6-s7), the Bedouin / Ashjaʿ
  (s9-s10), Jarir / al-Mutanabbi (s12-s13), al-Buhturi / al-Mutanabbi (s15-s16), Jarir / Abu Nuwas (s18-s19), Abu l-Shis / al-Mutanabbi
  (s21-s22), al-Afwah / Abu Tammam (s24-s26).

  python3 tools/authoring/author_talkhis_ch74.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

K = "sariqat-ghayr-zahira"
A = "ilm-al-arud"
QF = "al-qafiya"
TITLE = {"ar": "الْإِلْمَامُ وَالْأَخْذُ غَيْرُ الظَّاهِرِ", "en": "The ilmam and the hidden taking", "tr": "İlmâm ve zâhir olmayan alma"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the source gives this ruling only in Turkish; this is the received matn of the Talkhis.)"
R_TR = " (Geri yazım: kaynak bu hükmü yalnız Türkçe verir; bu, Telhîs'in alınan metnidir.)"

def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)
def fi(tag, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def wa_qawl(name_toks, tag=None):
    return [tok("وَقَوْلِ", "qawl", "noun", [tag or K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve … sözü».",
                segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun")])] + name_toks
def ka_qawl(name_toks, tag=None):
    return [tok("كَقَوْلِ", "qawl", "noun", [tag or K, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، مُضَافٌ.", "«as the saying of».", "«… sözü gibi».",
                segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun")])] + name_toks
def abu_tammam(): return [tok("أَبِي", "abu-tammam", "propn", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
                          tok("تَمَّامٍ", "abu-tammam", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Tammam».", "«Temmâm».", punct=":")]
def abu_tayyib(): return [tok("أَبِي", "abu-tayyib", "propn", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
                          tok("الطَّيِّبِ", "abu-tayyib", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«l-Tayyib».", "«et-Tayyib».", punct=":")]
def name1(full, lex, en, tr): return [tok(full, lex, "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", en, tr, punct=":")]
def SR(kind2, with_, grade=None, sub="zahir"):
    d = {"kind": "sariqa", "sub": sub, "kind2": kind2, "with": with_}
    if grade: d["grade"] = grade
    return d

# ----------- s1 — the ilmam (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "And if the meaning alone is taken, it is called ILMAM (touching) and SALKH (flaying) — and it too is of three kinds." + R_EN,
 "tr": "Yalnız mana alınırsa buna İLMÂM (dokunma) ve SELH (yüzme) denir — o da üç kısımdır." + R_TR},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("أُخِذَ", "akhadha", "verb", [K, "in-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is taken».", "«alınırsa»."),
  tok("الْمَعْنَى", "mana", "noun", [K, "naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the meaning».", "«mana»."),
  tok("وَحْدَهُ", "wahda", "noun", [K, "hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«alone» — the hal.", "«tek başına» — hâl.", segments=[seg("وَحْدَ", "wahda", "noun"), pr3ms()]),
  tok("سُمِّيَ", "samma", "verb", [K, "in-shartiyya", "naib-al-fail", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — جَوَابُ الشَّرْطِ.", "«it is called» — the jawab.", "«… denir» — cevap."),
  tok("إِلْمَامًا", "ilmam", "noun", [K, "mafulayn", "masdar", "form-iv-verbs", "doubled-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ أَلَمَّ بِهِ: نَزَلَ بِهِ وَمَسَّهُ.", "«ilmam — a touching» — the masdar of Form IV, doubled.", "«ilmâm — dokunma» — if'âl masdarı, muzâaf."),
  tok("وَسَلْخًا", "salkh", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَسَلْخًا مَعْطُوفٌ مَنْصُوبٌ — السَّلْخُ: نَزْعُ الْجِلْدِ.", "«and salkh — a flaying».", "«ve selh — deriyi yüzme».", segments=[seg("وَ", "wa", "conj"), seg("سَلْخًا", "salkh", "noun")], punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it».", "«o da».", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("ثَلَاثَةُ", "thalatha", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — الْعَدَدُ ثَلَاثَةٌ يُؤَنَّثُ مَعَ الْمَعْدُودِ الْمُذَكَّرِ.", "«three» — the khabar; the number takes the ta with a masculine counted noun.", "«üç» — haber; sayı müzekker ma'dûdla tâ alır."),
  tok("أَقْسَامٍ", "qism", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِسْمٍ.", "«kinds».", "«kısım»."),
  tok("كَذَلِكَ", "kadhalika", "part", [K, "hal"], "الْكَافُ لِلتَّشْبِيهِ وَذَلِكَ اسْمُ إِشَارَةٍ — كَالْإِغَارَةِ: فِي مَحَلِّ نَصْبٍ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ.", "«likewise» — as the ighara.", "«öylece» — iğâre gibi."),
 ]})

# ----------- s2 — the first grade (RESTORED) + Abu Tammam
S.append({"id": "s2", "translation": {
 "en": "The first: that the second be more eloquent, and so be praised — as the saying of Abu Tammam:" + R_EN,
 "tr": "Birincisi: ikincisinin daha beliğ olup memdûh olması — Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first».", "«birincisi»."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-sıdır» — cümle haber."),
  tok("يَكُونَ", "kana", "verb", [K, "an-masdariyya", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be».", "«olması»."),
  tok("الثَّانِي", "thani", "noun", [K, "kana-wa-akhawatuha", "ism-maqsur-manqus"], "اسْمُ يَكُونَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second».", "«ikincisi»."),
  tok("أَبْلَغَ", "ablagh", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ يَكُونَ مَنْصُوبٌ — اسْمُ تَفْضِيلٍ.", "«more eloquent».", "«daha beliğ»."),
  tok("فَيُمْدَحَ", "madaha", "verb", [K, "atf-nasaq", "naib-al-fail"], "الْفَاءُ عَاطِفَةٌ، وَيُمْدَحَ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ — مَعْطُوفٌ عَلَى يَكُونَ.", "«and so be praised» — joined to «be».", "«ve memdûh olması» — yekûne'ye ma'tûf.",
      segments=[seg("فَ", "fa", "conj"), seg("يُمْدَحَ", "madaha", "verb")], punct="،"),
 ] + ka_qawl(abu_tammam())})
S.append({"id": "s3", "translation": {
 "en": "«It is a favour: if it hastens, good; and if it delays, * then in some places the delay is more useful» (Abu Tammam — ṭawīl).",
 "tr": "«O bir ihsandır: acele gelirse hayırdır; gecikirse * bazı yerlerde gecikme daha faydalıdır» (Ebû Temmâm — tavîl)."},
 "tokens": [
  tok("هُوَ", "huwa", "pron", [K, A, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«it».", "«o»."),
  tok("الصُّنْعُ", "sun", "noun", [K, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ — الصُّنْعُ: الْإِحْسَانُ.", "«a favour» — the khabar.", "«ihsandır» — haber."),
  tok("إِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-se»."),
  tok("يَعْجَلْ", "ajila", "verb", [K, "in-shartiyya"], "مُضَارِعٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ: عَجِلَ يَعْجَلُ.", "«it hastens» — the shart verb.", "«acele gelirse» — şart fiili."),
  tok("فَخَيْرٌ", "khayr", "noun", [K, "in-shartiyya", "hadhf-wa-taqdir"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَخَيْرٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: فَهُوَ خَيْرٌ.", "«good» — the jawab.", "«hayırdır» — cevap.", segments=[seg("فَ", "fa", "conj"), seg("خَيْرٌ", "khayr", "noun")]),
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("يَرِثْ", "ratha-delay", "verb", [K, "in-shartiyya", "hollow-verbs"], "مُضَارِعٌ مَجْزُومٌ — رَاثَ يَرِيثُ: أَبْطَأَ، حُذِفَتْ يَاؤُهُ لِلْجَزْمِ.", "«it delays» — رَاثَ, hollow; the ya fell for the jazm.", "«gecikirse» — râse, ecvef; cezm için yâ düştü.", punct="*"),
  tok("فَلِلرَّيْثِ", "rayth", "noun", [K, "in-shartiyya", "huruf-jarr", "masdar"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَاللَّامُ حَرْفُ جَرٍّ، وَالرَّيْثِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«for the delay» — the fronted khabar.", "«gecikme için» — öne alınmış haber.",
      segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("الرَّيْثِ", "rayth", "noun")]),
  fi(K),
  tok("بَعْضِ", "bad", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«some».", "«bazı»."),
  tok("الْمَوَاضِعِ", "mawdi", "noun", [K, "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ مَوْضِعٍ.", "«places».", "«yerlerde»."),
  tok("أَنْفَعُ", "anfa", "noun", [K, QF, "mubtada-khabar", "ism-tafdil"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ. الرَّوِيُّ الْعَيْنُ.", "«more useful» — the delayed mubtada; rhyme: rawi ʿayn.", "«daha faydalı» — sona bırakılmış mübtedâ; kafiye: revî ayn."),
 ]})
S.append({"id": "s4", "translation": {
 "en": "And the saying of Abu l-Tayyib: «And of the good is the slowness of your gift to me: * the swiftest of clouds on their way are the rainless ones» — the meaning alone, and better: an ilmam that is praised.",
 "tr": "Ve Ebü't-Tayyib'in: «Bağışının bana gecikmesi de hayırdandır: * bulutların yolda en hızlısı yağmursuz olanıdır» sözü — yalnız mana, ve daha iyi: memdûh bir ilmâm."},
 "tokens": wa_qawl(abu_tayyib()) + [
  tok("وَمِنَ", "min", "prep", [K, A, "huruf-jarr"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنَ حَرْفُ جَرٍّ.", "«and of».", "«ve … -den».", segments=[seg("وَ", "wa", "conj"), seg("مِنَ", "min", "prep")]),
  tok("الْخَيْرِ", "khayr", "noun", [K, "huruf-jarr", "mubtada-khabar"], "مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«the good» — the fronted khabar.", "«hayır» — öne alınmış haber."),
  tok("بُطْءُ", "but", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the slowness».", "«gecikmesi»."),
  tok("سَيْبِكَ", "sayb", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — السَّيْبُ: الْعَطَاءُ.", "«of your gift».", "«bağışının».", segments=[seg("سَيْبِ", "sayb", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("عَنِّي", "an", "prep", [K, "huruf-jarr", "ya-al-mutakallim"], "عَنْ حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ — أُدْغِمَتِ النُّونُ فِي نُونِ الْوِقَايَةِ.", "«from me» — the nun of عن merged into the nun of wiqaya.", "«benden» — an'ın nûnu vikâye nûnuna idgam.", segments=[seg("عَنْ", "an", "prep"), seg("نِي", "pron-1s", "pron")], punct="*"),
  tok("أَسْرَعُ", "asra", "noun", [K, "mubtada-khabar", "idafa-definiteness", "ism-tafdil"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«the swiftest».", "«en hızlısı»."),
  tok("السُّحْبِ", "sahab", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ سَحَابٍ.", "«of clouds».", "«bulutların»."),
  fi(K),
  tok("الْمَسِيرِ", "masir", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ — مَصْدَرٌ مِيمِيٌّ.", "«on the way».", "«yolda»."),
  tok("الْجَهَامُ", "jaham", "noun", [K, QF, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الْجَهَامُ: السَّحَابُ الَّذِي لَا مَاءَ فِيهِ. الرَّوِيُّ الْمِيمُ.", "«the rainless cloud» — the khabar; rhyme: rawi mim.", "«yağmursuz bulut» — haber; kafiye: revî mîm."),
 ]})
S[-1]["badi"] = [SR("ilmam", "s3", "mamduh")]

# ----------- s5 — the second grade (RESTORED) + al-Buhturi
S.append({"id": "s5", "translation": {
 "en": "The second: that it be below it, and so be blamed — as the saying of al-Buhturi:" + R_EN,
 "tr": "İkincisi: ondan aşağı olup mezmûm olması — Buhturî'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second».", "«ikincisi».", segments=[seg("وَ", "wa", "conj"), seg("الثَّانِي", "thani", "noun")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-sıdır»."),
  tok("يَكُونَ", "kana", "verb", [K, "an-masdariyya", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it be».", "«olması»."),
  tok("دُونَهُ", "duna", "noun", [K, "maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفٌ مَنْصُوبٌ — خَبَرُ يَكُونَ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«below it».", "«ondan aşağı».", segments=[seg("دُونَ", "duna", "noun"), pr3ms()]),
  tok("فَيُذَمَّ", "dhamma", "verb", [K, "atf-nasaq", "naib-al-fail", "doubled-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيُذَمَّ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ — مُضَاعَفٌ.", "«and so be blamed».", "«ve mezmûm olması».",
      segments=[seg("فَ", "fa", "conj"), seg("يُذَمَّ", "dhamma", "verb")], punct="،"),
 ] + ka_qawl(name1("الْبُحْتُرِيِّ", "buhturi", "«al-Buhturi».", "«Buhturî»."))})
S.append({"id": "s6", "translation": {
 "en": "«And when his polished speech gleams in the assembly, * you would take his tongue for one of his keen swords» (al-Buhturi — kāmil; the word الْمَصْقُولُ straddles the two hemistichs: a mudawwar bayt).",
 "tr": "«Mecliste cilâlı sözü parladığında * dilini keskin kılıçlarından sanırsın» (Buhturî — kâmil; الْمَصْقُولُ kelimesi iki mısraya yayılır: müdevver beyit)."},
 "tokens": [
  tok("وَإِذَا", "idha", "noun", [K, A, "idha-shartiyya", "maful-fih"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve … -diğinde».", segments=[seg("وَ", "wa", "conj"), seg("إِذَا", "idha", "noun")]),
  tok("تَأَلَّقَ", "taallaqa", "verb", [K, "idha-shartiyya", "form-v-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ: تَأَلَّقَ: لَمَعَ.", "«gleams» — Form V: to flash.", "«parladığında» — tefa'ul: parlamak."),
  fi(K),
  tok("النَّدِيِّ", "nadi", "noun", [K, "huruf-jarr"], "مَجْرُورٌ — النَّدِيُّ: مَجْلِسُ الْقَوْمِ.", "«the assembly».", "«mecliste»."),
  tok("كَلَامُهُ", "kalam", "noun", [K, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his speech» — the doer.", "«sözü» — fâil.", segments=[seg("كَلَامُ", "kalam", "noun"), pr3ms()], punct="*"),
  tok("الْمَصْقُولُ", "masqul", "noun", [K, "naat-sifa", "ism-maful"], "نَعْتٌ لِكَلَامُهُ مَرْفُوعٌ — اسْمُ مَفْعُولٍ: الْمَجْلُوُّ. يَقَعُ فِي أَوَّلِ الْعَجُزِ وَالْبَيْتُ مُدَوَّرٌ.", "«polished» — the na't; it opens the second hemistich, the bayt being mudawwar.", "«cilâlı» — sıfat; acüzün başında, beyit müdevver."),
  tok("خِلْتَ", "khala", "verb", [K, "zanna-wa-akhawatuha", "mafulayn", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — مِنْ أَخَوَاتِ ظَنَّ، يَنْصِبُ مَفْعُولَيْنِ: خَالَ يَخَالُ.", "«you would take … for» — a sister of ظَنَّ, two objects.", "«sanırsın» — zanne'nin kız kardeşi, iki mef'ûl."),
  tok("لِسَانَهُ", "lisan", "noun", [K, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his tongue» — the first object.", "«dilini» — ilk mef'ûl.", segments=[seg("لِسَانَ", "lisan", "noun"), pr3ms()]),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr", "mafulayn"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَوْضِعِ الْمَفْعُولِ الثَّانِي.", "«one of» — the jarr phrase stands as the second object.", "«-den biri» — câr-mecrûr ikinci mef'ûl yerinde."),
  tok("عَضْبِهِ", "adb", "noun", [K, QF, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَضْبُ: السَّيْفُ الْقَاطِعُ. الرَّوِيُّ الْبَاءُ.", "«his keen sword» — rhyme: rawi ba, the ha its wasl.", "«keskin kılıcı» — kafiye: revî bâ, hâ vasl.", segments=[seg("عَضْبِ", "adb", "noun"), pr3msi()]),
 ]})
S.append({"id": "s7", "translation": {
 "en": "And the saying of Abu l-Tayyib: «As if their tongues in speech had been set * upon their spears in the thrust as spearheads» — the meaning alone, and below it: an ilmam that is blamed.",
 "tr": "Ve Ebü't-Tayyib'in: «Sanki dilleri konuşmada * mızraklarının ucuna sançmada temren yapılmış» sözü — yalnız mana, ve ondan aşağı: mezmûm bir ilmâm."},
 "tokens": wa_qawl(abu_tayyib()) + [
  tok("كَأَنَّ", "kaanna", "part", [K, A, "inna-wa-akhawatuha"], "حَرْفُ تَشْبِيهٍ وَنَصْبٍ.", "«as if».", "«sanki»."),
  tok("أَلْسُنَهُمْ", "lisan", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], "اسْمُ كَأَنَّ مَنْصُوبٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ لِسَانٍ.", "«their tongues» — kaʾanna's ism.", "«dilleri» — keenne'nin ismi.", segments=[seg("أَلْسُنَ", "lisan", "noun"), pr3mp()]),
  fi(K),
  tok("النُّطْقِ", "nutq", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ.", "«speech».", "«konuşmada»."),
  tok("قَدْ", "qad", "part", [K, "qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«had».", "«-mış»."),
  tok("جُعِلَتْ", "jaala", "verb", [K, "inna-wa-akhawatuha", "naib-al-fail", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ كَأَنَّ.", "«had been set» — kaʾanna's khabar.", "«yapılmış» — keenne'nin haberi.", punct="*"),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  tok("رِمَاحِهِمْ", "rumh", "noun", [K, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ رُمْحٍ.", "«their spears».", "«mızraklarının».", segments=[seg("رِمَاحِ", "rumh", "noun"), pr3mp()]),
  fi(K),
  tok("الطَّعْنِ", "tan", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ.", "«the thrust».", "«sançmada»."),
  tok("خُرْصَانَا", "khurs", "noun", [K, QF, "mafulayn", "jam-taksir"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — جَمْعُ خُرْصٍ: سِنَانُ الرُّمْحِ؛ أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ.", "«as spearheads» — the second object; the alif of itlaq.", "«temren olarak» — ikinci mef'ûl; ıtlak elifi."),
 ]})
S[-1]["badi"] = [SR("ilmam", "s6", "madhmum")]

# ----------- s8 — the third grade (RESTORED) + the Bedouin
S.append({"id": "s8", "translation": {
 "en": "The third: that it be its equal, and so be far from blame while the merit stays the first's — as the saying of the Bedouin:" + R_EN,
 "tr": "Üçüncüsü: onun dengi olup zemden uzak kalması, fazilet birincinin olmak üzere — Bedevî'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ.", "«the third».", "«üçüncüsü».", segments=[seg("وَ", "wa", "conj"), seg("الثَّالِثُ", "thalith", "noun")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ.", "«that».", "«-sıdır»."),
  tok("يَكُونَ", "kana", "verb", [K, "an-masdariyya", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«it be».", "«olması»."),
  tok("مِثْلَهُ", "mithl", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ يَكُونَ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its equal».", "«dengi».", segments=[seg("مِثْلَ", "mithl", "noun"), pr3ms()]),
  tok("فَيَبْعُدَ", "baada", "verb", [K, "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَيَبْعُدَ مُضَارِعٌ مَنْصُوبٌ — بَعُدَ يَبْعُدُ.", "«and so be far».", "«ve uzak olması».", segments=[seg("فَ", "fa", "conj"), seg("يَبْعُدَ", "baada", "verb")]),
  tok("عَنِ", "an", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — كُسِرَتِ النُّونُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  tok("الذَّمِّ", "dhamm", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«blame».", "«zemden»."),
  tok("وَيَكُونَ", "kana", "verb", [K, "atf-nasaq", "kana-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَيَكُونَ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«and be».", "«ve olması».", segments=[seg("وَ", "wa", "conj"), seg("يَكُونَ", "kana", "verb")]),
  tok("الْفَضْلُ", "fadl", "noun", [K, "kana-wa-akhawatuha"], "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the merit».", "«fazilet»."),
  tok("لِلْأَوَّلِ", "awwal", "noun", [K, "huruf-jarr", "kana-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَوَّلِ مَجْرُورٌ — خَبَرُ يَكُونَ.", "«the first's».", "«birincinin».", segments=[seg("لِ", "li", "prep"), seg("الْأَوَّلِ", "awwal", "noun")], punct="،"),
 ] + ka_qawl(name1("الْأَعْرَابِيِّ", "arabi-bedouin", "«the Bedouin».", "«Bedevî»."))})
S.append({"id": "s9", "translation": {
 "en": "«He was not the richest of the young men in wealth, * but he was the most open-handed of them» (the Bedouin — wāfir).",
 "tr": "«Gençlerin malca en zengini değildi, * fakat kolu en açık olanıydı» (Bedevî — vâfir)."},
 "tokens": [
  tok("وَلَمْ", "lam", "part", [K, A, "lam-jazim"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ.", "«and … not».", "«ve … değil».", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam", "part")]),
  tok("يَكُ", "kana", "verb", [K, "lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ — حُذِفَتْ نُونُهُ تَخْفِيفًا: يَكُنْ، وَاسْمُهُ مُسْتَتِرٌ.", "«he was» — لَمْ يَكُ with its nun lightened away.", "«idi» — nûnu hafifletilerek düşmüş lem yekü."),
  tok("أَكْثَرَ", "akthar", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"], "خَبَرُ يَكُ مَنْصُوبٌ، مُضَافٌ.", "«the richest».", "«en çok»."),
  tok("الْفِتْيَانِ", "fatan", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ فَتًى.", "«of the young men».", "«gençlerin»."),
  tok("مَالًا", "mal", "noun", [K, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in wealth» — the tamyiz.", "«malca» — temyîz.", punct="*"),
  tok("وَلَكِنْ", "lakin", "part", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا يَعْمَلُ.", "«but» — the light lakin governs nothing.", "«fakat» — hafif lâkin amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لَكِنْ", "lakin", "part")]),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«he was».", "«idi»."),
  tok("أَرْحَبَهُمْ", "arhab", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ، وَهُمْ مُضَافٌ إِلَيْهِ — اسْمُ تَفْضِيلٍ مِنْ رَحُبَ.", "«the most open of them».", "«onların en genişi».", segments=[seg("أَرْحَبَ", "arhab", "noun"), pr3mp()]),
  tok("ذِرَاعَا", "dhira", "noun", [K, QF, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ: رَحْبُ الذِّرَاعِ كِنَايَةٌ عَنِ الْجُودِ.", "«in arm» — the tamyiz; «wide of arm» is a kinaya for generosity.", "«kolca» — temyîz; «kolu geniş» cömertlikten kinâye."),
 ]})
S.append({"id": "s10", "translation": {
 "en": "And the saying of Ashjaʿ: «He is not the widest of them in wealth, * but his kindness is the widest» — the meaning alone, and its equal: no blame, the merit the first's.",
 "tr": "Ve Eşca'ın: «Zenginlikte onların en genişi değildir, * fakat iyiliği en geniştir» sözü — yalnız mana, ve dengi: zem yok, fazilet birincinin."},
 "tokens": wa_qawl(name1("أَشْجَعَ", "ashja", "«Ashjaʿ» — Ashjaʿ al-Sulami.", "«Eşca'» — Eşca' es-Sülemî.")) + [
  tok("وَلَيْسَ", "laysa", "verb", [K, A, "kana-wa-akhawatuha"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَيْسَ فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«he is not».", "«değildir».", segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  tok("بِأَوْسَعِهِمْ", "awsa-wider", "noun", [K, "huruf-jarr", "kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"], "الْبَاءُ زَائِدَةٌ، وَأَوْسَعِ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا، وَهُمْ مُضَافٌ إِلَيْهِ.", "«the widest of them» — laysa's khabar under the extra ba.", "«onların en genişi» — zâid bâ altında leyse'nin haberi.",
      segments=[seg("بِ", "bi", "prep"), seg("أَوْسَعِ", "awsa-wider", "noun"), pr3mp()]),
  fi(K),
  tok("الْغِنَى", "ghina", "noun", [K, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«wealth».", "«zenginlikte».", punct="*"),
  tok("وَلَكِنَّ", "lakinna", "part", [K, "inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَلَكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ.", "«but».", "«fakat».", segments=[seg("وَ", "wa", "conj"), seg("لَكِنَّ", "lakinna", "part")]),
  tok("مَعْرُوفَهُ", "maruf", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness", "ism-maful"], "اسْمُ لَكِنَّ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْمَعْرُوفُ: الْإِحْسَانُ.", "«his kindness» — lakinna's ism.", "«iyiliği» — lâkinnenin ismi.", segments=[seg("مَعْرُوفَ", "maruf", "noun"), pr3ms()]),
  tok("أَوْسَعُ", "awsa-wider", "noun", [K, QF, "inna-wa-akhawatuha", "ism-tafdil"], "خَبَرُ لَكِنَّ مَرْفُوعٌ. الرَّوِيُّ الْعَيْنُ.", "«the widest» — lakinna's khabar; rhyme: rawi ʿayn.", "«en geniştir» — lâkinnenin haberi; kafiye: revî ayn."),
 ]})
S[-1]["badi"] = [SR("ilmam", "s9", "mithl")]

# ----------- s11 — the hidden taking: the two meanings resemble (RESTORED) + Jarir
S.append({"id": "s11", "translation": {
 "en": "And the taking that is NOT plain: among it, that the two meanings resemble each other — as the saying of Jarir:" + R_EN,
 "tr": "ZÂHİR OLMAYAN alma: iki mananın birbirine benzemesi bundandır — Cerîr'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَغَيْرُ", "ghayr", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَغَيْرُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and other than».", "«ve … olmayan».", segments=[seg("وَ", "wa", "conj"), seg("غَيْرُ", "ghayr", "noun")]),
  tok("الظَّاهِرِ", "zahir", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the plain».", "«zâhir»."),
  tok("مِنْهُ", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«among it».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرُ غَيْرُ.", "«that» — the khabar.", "«-sidir» — haber."),
  tok("يَتَشَابَهَ", "tashabaha", "verb", [K, "an-masdariyya", "form-vi-verbs"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ — تَشَابَهَ: أَشْبَهَ أَحَدُهُمَا الْآخَرَ.", "«resemble each other» — Form VI.", "«benzeşmesi» — tefâul."),
  tok("الْمَعْنَيَانِ", "mana", "noun", [K, "fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنَّى مَعْنًى، رُدَّتْ أَلِفُهُ يَاءً.", "«the two meanings» — the dual of a maqsur, its alif turned ya.", "«iki mana» — maksûrun tesniyesi, elifi yâ olmuş.", punct="،"),
 ] + ka_qawl(name1("جَرِيرٍ", "jarir", "«Jarir» — Jarir b. ʿAtiyya.", "«Cerîr» — Cerîr b. Atıyye."))})
S.append({"id": "s12", "translation": {
 "en": "«So let not their beards keep you from a need — * alike are the one with the turban and the one with the veil» (Jarir — wāfir).",
 "tr": "«Sakalları seni bir ihtiyaçtan alıkoymasın — * sarıklı ile başörtülü birdir» (Cerîr — vâfir)."},
 "tokens": [
  tok("فَلَا", "la-nahiya", "part", [K, A, "la-nahiya"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«so let … not» — the prohibiting la.", "«… -masın» — nehiy lâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nahiya", "part")]),
  tok("يَمْنَعْكَ", "manaa", "verb", [K, "la-nahiya", "mafulayn"], "مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«keep you» — jussive; the kaf its object.", "«seni alıkoymasın» — meczûm; kâf mef'ûl.", segments=[seg("يَمْنَعْ", "manaa", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("أَرَبٍ", "arab", "noun", [K, "huruf-jarr"], "مَجْرُورٌ — الْأَرَبُ: الْحَاجَةُ.", "«a need».", "«bir ihtiyaçtan»."),
  tok("لِحَاهُمْ", "lihya", "noun", [K, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ لِحْيَةٍ.", "«their beards» — the doer.", "«sakalları» — fâil.", segments=[seg("لِحَا", "lihya", "noun"), pr3mp()], punct="*"),
  tok("سَوَاءٌ", "sawa", "noun", [K, "mubtada-khabar"], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«alike» — the fronted khabar.", "«birdir» — öne alınmış haber."),
  tok("ذُو", "dhu", "noun", [K, "mubtada-khabar", "five-nouns", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ.", "«the one with» — the delayed mubtada, a five-noun.", "«… sahibi» — sona bırakılmış mübtedâ, esmâ-i hamse."),
  tok("الْعِمَامَةِ", "imama", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the turban».", "«sarık»."),
  tok("وَالْخِمَارِ", "khimar", "noun", [K, QF, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْخِمَارِ مَعْطُوفٌ مَجْرُورٌ: وَذُو الْخِمَارِ. الرَّوِيُّ الرَّاءُ، وَالرِّدْفُ الْأَلِفُ.", "«and (the one with) the veil» — the rhyme: rawi ra, alif ridf.", "«ve başörtü(lü)» — kafiye: revî râ, elif ridf.", segments=[seg("وَ", "wa", "conj"), seg("الْخِمَارِ", "khimar", "noun")]),
 ]})
S.append({"id": "s13", "translation": {
 "en": "And the saying of Abu l-Tayyib: «And whoever of them has a spear in his hand * is like whoever of them has dye in his hand» — the two meanings resemble each other: a hidden taking.",
 "tr": "Ve Ebü't-Tayyib'in: «Onlardan elinde mızrak olan, * onlardan elinde kına olan gibidir» sözü — iki mana benzeşir: hafî alma."},
 "tokens": wa_qawl(abu_tayyib()) + [
  tok("وَمَنْ", "man", "noun", [K, A, "ism-mawsul", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمَنْ اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«and whoever» — the relative, the mubtada.", "«ve kim» — mevsûl, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("مَنْ", "man", "noun")]),
  fi(K),
  tok("كَفِّهِ", "kaff", "noun", [K, "huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«in his hand» — the fronted khabar inside the sila.", "«elinde» — sıla içinde öne alınmış haber.", segments=[seg("كَفِّ", "kaff", "noun"), pr3msi()]),
  tok("مِنْهُمْ", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهُمْ مَجْرُورٌ.", "«of them».", "«onlardan».", segments=[seg("مِنْ", "min", "prep"), pr3mp()]),
  tok("قَنَاةٌ", "qana", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a spear».", "«bir mızrak».", punct="*"),
  tok("كَمَنْ", "man", "noun", [K, "huruf-jarr", "ism-mawsul", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ مَنِ الْأُولَى.", "«is like whoever» — the khabar of the first «whoever».", "«kim … gibidir» — ilk men'in haberi.", segments=[seg("كَ", "ka", "prep"), seg("مَنْ", "man", "noun")]),
  fi(K),
  tok("كَفِّهِ", "kaff", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in his hand».", "«elinde».", segments=[seg("كَفِّ", "kaff", "noun"), pr3msi()]),
  tok("مِنْهُمْ", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهُمْ مَجْرُورٌ.", "«of them».", "«onlardan».", segments=[seg("مِنْ", "min", "prep"), pr3mp()]),
  tok("خِضَابُ", "khidab", "noun", [K, QF, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — الْخِضَابُ: مَا يُخْضَبُ بِهِ؛ نُوِّنَ فِي الْأَصْلِ وَأُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الْبَاءُ.", "«dye» — rhyme: rawi ba, the tanwin dropped.", "«kına» — kafiye: revî bâ, tenvin bırakılmış."),
 ]})
S[-1]["badi"] = [SR("tashabuh", "s12", None, "ghayr-zahir")]

# ----------- s14 — the meaning moved to another place (RESTORED) + al-Buhturi
S.append({"id": "s14", "translation": {
 "en": "And among it: that the meaning be MOVED to another place — as the saying of al-Buhturi:" + R_EN,
 "tr": "Mananın başka bir yere NAKLEDİLMESİ de bundandır — Buhturî'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and among it» — the fronted khabar.", "«ve ondandır» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that» — the masdar is the delayed mubtada.", "«-si» — masdar sona bırakılmış mübtedâ."),
  tok("يُنْقَلَ", "naqala", "verb", [K, "an-masdariyya", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be moved».", "«nakledilmesi»."),
  tok("الْمَعْنَى", "mana", "noun", [K, "naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the meaning».", "«mana»."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("مَحَلٍّ", "mahall", "noun", [K, "huruf-jarr", "naat-sifa"], "مَجْرُورٌ.", "«a place».", "«bir yere»."),
  tok("آخَرَ", "akhar", "noun", [K, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى وَزْنِ أَفْعَلَ.", "«another» — the diptote takes fatha for kasra.", "«başka» — gayr-i munsarif, kesre yerine fetha.", punct="،"),
 ] + ka_qawl(name1("الْبُحْتُرِيِّ", "buhturi", "«al-Buhturi».", "«Buhturî»."))})
S.append({"id": "s15", "translation": {
 "en": "«They were stripped, and the blood shone upon them * reddening — as if they had not been stripped» (al-Buhturi — kāmil).",
 "tr": "«Soyuldular, ve kan üzerlerinde parladı * kızarmış olarak — sanki soyulmamışlar gibi» (Buhturî — kâmil)."},
 "tokens": [
  tok("سُلِبُوا", "salaba", "verb", [K, A, "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ.", "«they were stripped» — the waw its naʾib.", "«soyuldular» — vâv nâib-i fâil."),
  tok("وَأَشْرَقَتِ", "ashraqa", "verb", [K, "atf-nasaq", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَشْرَقَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and shone» — the ta takes kasra before the article.", "«ve parladı» — tâ iki sâkin yüzünden kesre.", segments=[seg("وَ", "wa", "conj"), seg("أَشْرَقَتِ", "ashraqa", "verb")]),
  tok("الدِّمَاءُ", "dam", "noun", [K, "fail", "jam-taksir", "ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ دَمٍ، مَمْدُودٌ.", "«the blood» — plural of دَم.", "«kanlar» — dem'in cem'i."),
  tok("عَلَيْهِمْ", "ala", "prep", [K, "huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَهُمْ مَجْرُورٌ — تُشْبَعُ مِيمُهُ فِي الْوَزْنِ: عَلَيْهِمُ.", "«upon them» — the metre reads the mim with a damma.", "«üzerlerine» — vezinde mîm ötreli okunur.", segments=[seg("عَلَيْ", "ala", "prep"), pr3mp()], punct="*"),
  tok("مُحْمَرَّةً", "muhmarr", "noun", [K, "hal", "ism-fail"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلِ احْمَرَّ (الْبَابُ التَّاسِعُ)، مُؤَنَّثٌ.", "«reddening» — the hal; ism faʿil of Form IX.", "«kızarmış olarak» — hâl; ihmarra'nın ism-i fâili."),
  tok("فَكَأَنَّهُمْ", "kaanna", "part", [K, "inna-wa-akhawatuha"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَكَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَهُمْ اسْمُهَا.", "«so that as if they».", "«sanki onlar».", segments=[seg("فَ", "fa", "conj"), seg("كَأَنَّ", "kaanna", "part"), pr3mp()]),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-me-»."),
  tok("يُسْلَبُوا", "salaba", "verb", [K, QF, "lam-jazim", "naib-al-fail", "inna-wa-akhawatuha"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — خَبَرُ كَأَنَّ. الرَّوِيُّ الْبَاءُ، وَالْوَاوُ وَصْلٌ.", "«had been stripped» — kaʾanna's khabar; rhyme: rawi ba, the waw its wasl.", "«soyulmuşlar» — keennenin haberi; kafiye: revî bâ, vâv vasl."),
 ]})
S.append({"id": "s16", "translation": {
 "en": "And the saying of Abu l-Tayyib: «The blood has dried on it while it is drawn * from its sheath — and so it is as though sheathed» — the meaning moved from the slain to the sword: hidden.",
 "tr": "Ve Ebü't-Tayyib'in: «Kan üzerinde kurudu, o kınından * sıyrılmışken — sanki kınındadır» sözü — mana öldürülenlerden kılıca nakledilmiş: hafî."},
 "tokens": wa_qawl(abu_tayyib()) + [
  tok("يَبِسَ", "yabisa", "verb", [K, A, "fail"], "فِعْلٌ مَاضٍ — يَبِسَ يَيْبَسُ.", "«has dried».", "«kurudu»."),
  tok("النَّجِيعُ", "naji", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ — النَّجِيعُ: دَمُ الْجَوْفِ.", "«the blood» — the dark blood of the body.", "«kan» — iç kanı."),
  tok("عَلَيْهِ", "ala", "prep", [K, "huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«on it».", "«üzerinde».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("وَهُوَ", "huwa", "pron", [K, "hal", "mubtada-khabar"], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ — وَالْجُمْلَةُ حَالٌ؛ تُسَكَّنُ هَاؤُهُ فِي الْوَزْنِ: وَهْوَ.", "«while it» — the waw of hal; the metre reads وَهْوَ.", "«o … iken» — hâl vâvı; vezin vehve okur.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("مُجَرَّدٌ", "mujarrad", "noun", [K, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ جَرَّدَ.", "«drawn, bared».", "«sıyrılmış».", punct="*"),
  tok("عَنْ", "an", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("غِمْدِهِ", "ghimd", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its sheath».", "«kınından».", segments=[seg("غِمْدِ", "ghimd", "noun"), pr3msi()], punct="،"),
  tok("فَكَأَنَّمَا", "kaanna", "part", [K, "innama-kaffa"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَكَأَنَّ كُفَّتْ بِمَا عَنِ الْعَمَلِ.", "«and so as though» — ma stops kaʾanna's governing.", "«sanki» — mâ keennenin amelini keser.", segments=[seg("فَ", "fa", "conj"), seg("كَأَنَّ", "kaanna", "part"), seg("مَا", "ma-kaffa", "part")]),
  tok("هُوَ", "huwa", "pron", [K, "mubtada-khabar"], "مُبْتَدَأٌ.", "«it».", "«o»."),
  tok("مُغْمَدُ", "mughmad", "noun", [K, QF, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ أَغْمَدَ؛ أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الدَّالُ.", "«sheathed» — rhyme: rawi dal, released.", "«kınında» — kafiye: revî dâl, ıtlâk."),
 ]})
S[-1]["badi"] = [SR("naql", "s15", None, "ghayr-zahir")]

# ----------- s17 — the second's meaning wider (RESTORED) + Jarir
S.append({"id": "s17", "translation": {
 "en": "And among it: that the meaning of the second be WIDER — as the saying of Jarir:" + R_EN,
 "tr": "İkincinin manasının DAHA KAPSAMLI olması da bundandır — Cerîr'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and among it».", "«ve ondandır».", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that».", "«-sı»."),
  tok("يَكُونَ", "kana", "verb", [K, "an-masdariyya", "kana-wa-akhawatuha"], "مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be».", "«olması»."),
  tok("مَعْنَى", "mana", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "اسْمُ يَكُونَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the meaning of».", "«manası»."),
  tok("الثَّانِي", "thani", "noun", [K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second».", "«ikincinin»."),
  tok("أَشْمَلَ", "ashmal", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ يَكُونَ مَنْصُوبٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«wider» — the elative, a diptote.", "«daha kapsamlı» — ism-i tafdîl, gayr-i munsarif.", punct="،"),
 ] + ka_qawl(name1("جَرِيرٍ", "jarir", "«Jarir».", "«Cerîr»."))})
S.append({"id": "s18", "translation": {
 "en": "«When the Banu Tamim are angry at you, * you find all mankind angry» (Jarir — wāfir).",
 "tr": "«Temîm oğulları sana kızdığında, * bütün insanları kızgın bulursun» (Cerîr — vâfir)."},
 "tokens": [
  tok("إِذَا", "idha", "part", [K, A, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  tok("غَضِبَتْ", "ghadiba", "verb", [K, "idha-shartiyya", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — غَضِبَ يَغْضَبُ.", "«are angry».", "«kızdı»."),
  tok("عَلَيْكَ", "ala", "prep", [K, "huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْكَافُ مَجْرُورٌ.", "«at you».", "«sana».", segments=[seg("عَلَيْ", "ala", "prep"), seg("كَ", "pron-2ms", "pron")]),
  tok("بَنُو", "banu", "noun", [K, "fail", "jam-mudhakkar-salim", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، مُضَافٌ، حُذِفَتْ نُونُهُ.", "«the sons of» — the doer, raised by the waw.", "«oğulları» — fâil, vâv ile merfû.", segments=None),
  tok("تَمِيمٍ", "tamim", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — قَبِيلَةُ جَرِيرٍ.", "«Tamim» — Jarir's tribe.", "«Temîm» — Cerîr'in kabilesi.", punct="*"),
  tok("وَجَدْتَ", "wajada", "verb", [K, "idha-shartiyya", "mafulayn", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جَوَابُ إِذَا؛ يَنْصِبُ مَفْعُولَيْنِ.", "«you find» — the jawab; two objects.", "«bulursun» — cevap; iki mef'ûl.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("النَّاسَ", "nas", "noun", [K, "mafulayn"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ.", "«mankind» — the first object.", "«insanları» — birinci mef'ûl."),
  tok("كُلَّهُمْ", "kull", "noun", [K, "tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَعْنَوِيٌّ مَنْصُوبٌ، وَهُمْ مُضَافٌ إِلَيْهِ — تُشْبَعُ مِيمُهُ فِي الْوَزْنِ.", "«all of them» — the tawkid; the metre reads the mim with a damma.", "«hepsini» — te'kîd; vezinde mîm ötreli.", segments=[seg("كُلَّ", "kull", "noun"), pr3mp()]),
  tok("غِضَابَا", "ghadban", "noun", [K, QF, "mafulayn", "jam-taksir"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — جَمْعُ غَضْبَانَ؛ أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ. الرَّوِيُّ الْبَاءُ.", "«angry» — the second object; rhyme: rawi ba.", "«kızgın» — ikinci mef'ûl; kafiye: revî bâ."),
 ]})
S.append({"id": "s19", "translation": {
 "en": "And the saying of Abu Nuwas: «It is not, from God, a thing to be denied * that He gather the world in one man» — the second is wider than the first, and finer: hidden.",
 "tr": "Ve Ebû Nüvâs'ın: «Allah'tan uzak görülecek şey değildir * âlemi bir kişide toplaması» sözü — ikinci birinciden daha kapsamlı ve daha güzel: hafî."},
 "tokens": wa_qawl([tok("أَبِي", "ab", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
                    tok("نُوَاسٍ", "nuwas", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو نُوَاسٍ الْحَسَنُ بْنُ هَانِئٍ.", "«Nuwas».", "«Nüvâs».", punct=":")]) + [
  tok("وَلَيْسَ", "laysa", "verb", [K, A, "kana-wa-akhawatuha"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَيْسَ فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«it is not».", "«değildir».", segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — فُتِحَتْ نُونُهُ قَبْلَ لَامِ التَّعْرِيفِ.", "«from».", "«-den»."),
  tok("اللهِ", "allah", "propn", [K, "huruf-jarr"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God».", "«Allah'tan»."),
  tok("بِمُسْتَنْكَرٍ", "mustankar", "noun", [K, "huruf-jarr", "kana-wa-akhawatuha", "ism-maful", "form-x-verbs"], "الْبَاءُ زَائِدَةٌ، وَمُسْتَنْكَرٍ خَبَرُ لَيْسَ مُقَدَّمٌ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — اسْمُ مَفْعُولِ اسْتَنْكَرَ.", "«a thing denied» — laysa's fronted khabar under the extra ba; ism mafʿul of Form X.", "«uzak görülen» — zâid bâ altında leysenin öne alınmış haberi.", segments=[seg("بِ", "bi", "prep"), seg("مُسْتَنْكَرٍ", "mustankar", "noun")], punct="*"),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "kana-wa-akhawatuha"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ اسْمُ لَيْسَ مُؤَخَّرٌ.", "«that» — the masdar is laysa's delayed ism.", "«-ması» — masdar leysenin sona bırakılmış ismi."),
  tok("يَجْمَعَ", "jamaa", "verb", [K, "an-masdariyya"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«He gather».", "«toplaması»."),
  tok("الْعَالَمَ", "alam-world", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْعَالَمُ: الْخَلْقُ كُلُّهُ.", "«the world».", "«âlemi»."),
  fi(K),
  tok("وَاحِدٍ", "wahid", "noun", [K, QF, "huruf-jarr"], "مَجْرُورٌ. الرَّوِيُّ الدَّالُ، وَقَبْلَهُ حَاءٌ مَكْسُورَةٌ.", "«one man» — rhyme: rawi dal.", "«bir kişide» — kafiye: revî dâl."),
 ]})
S[-1]["badi"] = [SR("ashmal", "s18", None, "ghayr-zahir")]

# ----------- s20 — the qalb: the contrary meaning (RESTORED) + Abu l-Shis
S.append({"id": "s20", "translation": {
 "en": "And among it the QALB — that the meaning of the second be the contrary of the meaning of the first — as the saying of Abu l-Shis:" + R_EN,
 "tr": "KALB de bundandır — ikincinin manasının birincinin manasının zıddı olması — Ebü'ş-Şîs'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and among it».", "«ve ondandır».", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("الْقَلْبُ", "qalb", "noun", [K, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — الْقَلْبُ هُنَا: عَكْسُ الْمَعْنَى.", "«the qalb» — here: turning the meaning over.", "«kalb» — burada: mananın tersine çevrilmesi.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it is».", "«o da».", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-sıdır»."),
  tok("يَكُونَ", "kana", "verb", [K, "an-masdariyya", "kana-wa-akhawatuha"], "مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«be».", "«olması»."),
  tok("مَعْنَى", "mana", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "اسْمُ يَكُونَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the meaning of».", "«manası»."),
  tok("الثَّانِي", "thani", "noun", [K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second».", "«ikincinin»."),
  tok("نَقِيضَ", "naqid-contrary", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ يَكُونَ مَنْصُوبٌ، مُضَافٌ — النَّقِيضُ: الْمُخَالِفُ الَّذِي لَا يَجْتَمِعُ مَعَهُ.", "«the contrary of».", "«zıddı»."),
  tok("مَعْنَى", "mana", "noun", [K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the meaning of».", "«manasının»."),
  tok("الْأَوَّلِ", "awwal", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the first».", "«birincinin».", punct="،"),
 ] + ka_qawl([tok("أَبِي", "ab", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
              tok("الشِّيصِ", "shis", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الشِّيصِ الْخُزَاعِيُّ، ابْنُ عَمِّ دِعْبِلٍ.", "«l-Shis» — Abu l-Shis al-Khuzaʿi, Diʿbil's cousin.", "«ş-Şîs» — Ebü'ş-Şîs el-Huzâî, Di'bil'in amcaoğlu.", punct=":")])})
S.append({"id": "s21", "translation": {
 "en": "«I find the blame, in loving you, delicious — * for love of your mention: so let the blamers blame me» (Abu l-Shis — kāmil).",
 "tr": "«Sana olan aşkımda kınanmayı lezzetli bulurum — * anılmanı sevdiğimden: kınayanlar beni kınasın» (Ebü'ş-Şîs — kâmil)."},
 "tokens": [
  tok("أَجِدُ", "wajada", "verb", [K, A, "mafulayn", "mithal-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — حُذِفَتْ وَاوُهُ لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ؛ يَنْصِبُ مَفْعُولَيْنِ.", "«I find» — the mithal verb drops its waw; two objects.", "«bulurum» — misâl fiil vâvını düşürür; iki mef'ûl."),
  tok("الْمَلَامَةَ", "malama", "noun", [K, "mafulayn"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ.", "«the blame» — the first object.", "«kınanmayı» — birinci mef'ûl."),
  fi(K),
  tok("هَوَاكَ", "hawa-passion", "noun", [K, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْكَافُ مُضَافٌ إِلَيْهِ — الْهَوَى: الْعِشْقُ.", "«loving you» — a maqsur.", "«sana aşkımda» — maksûr.", segments=[seg("هَوَا", "hawa-passion", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَذِيذَةً", "ladhidh", "noun", [K, "mafulayn", "sifa-mushabbaha"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ.", "«delicious» — the second object.", "«lezzetli» — ikinci mef'ûl.", punct="*"),
  tok("حُبًّا", "hubb", "noun", [K, "maful-lah", "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ.", "«for love» — the object of cause.", "«sevgiden» — mef'ûlün leh."),
  tok("لِذِكْرِكِ", "dhikr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَذِكْرِ مَجْرُورٌ، وَالْكَافُ الْمَكْسُورَةُ مُضَافٌ إِلَيْهِ — لِلْمُخَاطَبَةِ.", "«of your mention» — the kasra marks a woman addressed.", "«anılmanı» — kesreli kâf: muhâtaba.", segments=[seg("لِ", "li", "prep"), seg("ذِكْرِ", "dhikr", "noun"), seg("كِ", "pron-2fs", "pron")]),
  tok("فَلْيَلُمْنِي", "lama", "verb", [K, "lam-amr", "hollow-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَاللَّامُ لَامُ الْأَمْرِ سَاكِنَةٌ بَعْدَ الْفَاءِ، وَيَلُمْ مُضَارِعٌ مَجْزُومٌ — حُذِفَ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ: لَامَ يَلُومُ — وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ.", "«so let … blame me» — the lam of command jussive on the hollow verb, its waw dropped.", "«beni kınasın» — emir lâmı ile meczûm ecvef fiil, vâvı düşmüş.", segments=[seg("فَ", "fa", "conj"), seg("لْ", "lam-amr", "part"), seg("يَلُمْ", "lama", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("اللُّوَّمُ", "luwwam", "noun", [K, QF, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ لَائِمٍ عَلَى فُعَّلٍ. الرَّوِيُّ الْمِيمُ.", "«the blamers» — plural of لَائِم on فُعَّل; rhyme: rawi mim.", "«kınayanlar» — lâim'in fu''al vezninde cem'i; kafiye: revî mîm."),
 ]})
S.append({"id": "s22", "translation": {
 "en": "And the saying of Abu l-Tayyib: «Do I love him and love blame on his account? * Blame on his account is one of his enemies» — the contrary of the first: the qalb, hidden.",
 "tr": "Ve Ebü't-Tayyib'in: «Onu sever de onun için kınanmayı sever miyim? * Onun için kınanma düşmanlarındandır» sözü — birincinin zıddı: kalb, hafî."},
 "tokens": wa_qawl(abu_tayyib()) + [
  tok("أَأُحِبُّهُ", "ahabba", "verb", [K, A, "al-istifham", "doubled-verbs", "form-iv-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَأُحِبُّ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ.", "«do I love him?» — the denying question.", "«onu sever miyim?» — inkârî istifhâm.", segments=[seg("أَ", "hamza-istifham", "part"), seg("أُحِبُّ", "ahabba", "verb"), pr3ms()]),
  tok("وَأُحِبُّ", "ahabba", "verb", [K, "atf-nasaq", "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُحِبُّ مُضَارِعٌ مَرْفُوعٌ.", "«and love».", "«ve severim».", segments=[seg("وَ", "wa", "conj"), seg("أُحِبُّ", "ahabba", "verb")]),
  tok("فِيهِ", "fi", "prep", [K, "huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — أَيْ فِي حُبِّهِ.", "«on his account».", "«onun için».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("مَلَامَةً", "malama", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«blame».", "«kınanmayı».", punct="*"),
  tok("إِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«şüphesiz»."),
  tok("الْمَلَامَةَ", "malama", "noun", [K, "inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«the blame» — inna's ism.", "«kınanma» — innenin ismi."),
  tok("فِيهِ", "fi", "prep", [K, "huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«on his account».", "«onun için».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«of» — the khabar.", "«-den» — haber."),
  tok("أَعْدَائِهِ", "aduww", "noun", [K, QF, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ عَدُوٍّ. الرَّوِيُّ الْهَمْزَةُ، وَالْأَلِفُ رِدْفٌ، وَالْهَاءُ وَصْلٌ.", "«his enemies» — rhyme: rawi hamza, alif ridf, the ha its wasl.", "«düşmanlarından» — kafiye: revî hemze, elif ridf, hâ vasl.", segments=[seg("أَعْدَائِ", "aduww", "noun"), pr3msi()]),
 ]})
S[-1]["badi"] = [SR("qalb", "s21", None, "ghayr-zahir")]

# ----------- s23 — part taken and bettered by an addition (RESTORED) + al-Afwah
S.append({"id": "s23", "translation": {
 "en": "And among it: that part of the meaning be taken, and there be added to it what betters it — as the saying of al-Afwah:" + R_EN,
 "tr": "Mananın bir kısmının alınıp ona onu güzelleştiren bir ekin katılması da bundandır — Efveh'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and among it».", "«ve ondandır».", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that».", "«-sı»."),
  tok("يُؤْخَذَ", "akhadha", "verb", [K, "an-masdariyya", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be taken».", "«alınması»."),
  tok("بَعْضُ", "bad", "noun", [K, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«part of».", "«bir kısmı»."),
  tok("الْمَعْنَى", "mana", "noun", [K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the meaning».", "«mananın»."),
  tok("وَيُضَافَ", "adafa", "verb", [K, "atf-nasaq", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُضَافَ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ — أَضَافَ يُضِيفُ.", "«and be added».", "«ve katılması».", segments=[seg("وَ", "wa", "conj"), seg("يُضَافَ", "adafa", "verb")]),
  tok("إِلَيْهِ", "ila", "prep", [K, "huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to it».", "«ona».", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ.", "«what».", "«… şey»."),
  tok("يُحَسِّنُهُ", "hassana", "verb", [K, "ism-mawsul", "form-ii-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ — صِلَةٌ.", "«betters it» — the sila.", "«onu güzelleştiren» — sıla.", segments=[seg("يُحَسِّنُ", "hassana", "verb"), pr3ms()], punct="،"),
 ] + ka_qawl(name1("الْأَفْوَهِ", "afwah", "«al-Afwah» — al-Afwah al-Awdi, the pre-Islamic poet.", "«Efveh» — câhiliye şairi Efveh el-Evdî."))})
S.append({"id": "s24", "translation": {
 "en": "«And you see the birds on our tracks, * an eye's seeing — confident that they will be fed» (al-Afwah — ramal).",
 "tr": "«Kuşları izlerimiz üzerinde görürsün, * göz görüşüyle — doyurulacaklarına güvenerek» (Efveh — remel)."},
 "tokens": [
  tok("وَتَرَى", "raa", "verb", [K, A, "naqis-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتَرَى مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and you see».", "«ve görürsün».", segments=[seg("وَ", "wa", "conj"), seg("تَرَى", "raa", "verb")]),
  tok("الطَّيْرَ", "tayr", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْمُ جِنْسٍ.", "«the birds».", "«kuşları»."),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerinde»."),
  tok("آثَارِنَا", "athar", "noun", [K, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ أَثَرٍ.", "«our tracks».", "«izlerimiz».", segments=[seg("آثَارِ", "athar", "noun"), seg("نَا", "pron-1p", "pron")], punct="*"),
  tok("رَأْيَ", "ray", "noun", [K, "maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ، مُضَافٌ — أَيْ رُؤْيَةً بِالْعَيْنِ.", "«an eye's seeing» — the maful mutlaq.", "«göz görüşü» — mef'ûl-i mutlak."),
  tok("عَيْنٍ", "ayn", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of an eye».", "«gözün»."),
  tok("ثِقَةً", "thiqa", "noun", [K, "maful-lah", "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ — مَصْدَرُ وَثِقَ.", "«confident» — the object of cause.", "«güvenerek» — mef'ûlün leh."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "hadhf-wa-taqdir"], "أَنْ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ — أَيْ ثِقَةً بِأَنَّهَا سَتُمَارُ.", "«that» — the lightened anna, its ism concealed.", "«-ına» — hafifletilmiş enne, ismi mahzûf."),
  tok("سَتُمَارُ", "mara", "verb", [K, QF, "naib-al-fail", "hollow-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَتُمَارُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — مَارَ يَمِيرُ: جَلَبَ الْمِيرَةَ. الرَّوِيُّ الرَّاءُ، وَالْأَلِفُ رِدْفٌ.", "«they will be fed» — the passive of a hollow verb; rhyme: rawi ra, alif ridf.", "«doyurulacaklar» — ecvef fiilin meçhûlü; kafiye: revî râ, elif ridf.", segments=[seg("سَ", "sa", "part"), seg("تُمَارُ", "mara", "verb")]),
 ]})
S.append({"id": "s25", "translation": {
 "en": "And the two sayings of Abu Tammam: «The eagles of his banners were shaded, in the forenoon, * by eagles of birds drinking their fill of the blood» (ṭawīl) —",
 "tr": "Ve Ebû Temmâm'ın şu iki sözü: «Sancaklarının kartalları kuşluk vakti * kana kanan kuş kartallarıyla gölgelendi» (tavîl) —"},
 "tokens": wa_qawl(abu_tammam()) + [
  tok("وَقَدْ", "qad", "part", [K, A, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ لِلتَّحْقِيقِ.", "«and indeed».", "«ve gerçekten».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("ظُلِّلَتْ", "zallala", "verb", [K, "naib-al-fail", "form-ii-verbs", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ — ظَلَّلَ: جَعَلَ عَلَيْهِ ظِلًّا.", "«were shaded» — Form II passive.", "«gölgelendi» — tef'îl meçhûlü."),
  tok("عِقْبَانُ", "uqab", "noun", [K, "naib-al-fail", "idafa-definiteness", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ — جَمْعُ عُقَابٍ؛ الْعِقْبَانُ هُنَا: صُوَرُ الْعُقْبَانِ عَلَى الرَّايَاتِ.", "«the eagles» — the eagle-figures on the banners.", "«kartallar» — sancaklardaki kartal resimleri."),
  tok("أَعْلَامِهِ", "alam", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ عَلَمٍ: الرَّايَةُ.", "«of his banners».", "«sancaklarının».", segments=[seg("أَعْلَامِ", "alam", "noun"), pr3msi()]),
  tok("ضُحًى", "duha", "noun", [K, "maful-fih", "ism-maqsur-manqus"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«in the forenoon».", "«kuşlukta».", punct="*"),
  tok("بِعِقْبَانِ", "uqab", "noun", [K, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَعِقْبَانِ مَجْرُورٌ، مُضَافٌ.", "«by eagles of».", "«kartallarıyla».", segments=[seg("بِ", "bi", "prep"), seg("عِقْبَانِ", "uqab", "noun")]),
  tok("طَيْرٍ", "tayr", "noun", [K, "idafa-definiteness", "naat-sifa"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«birds».", "«kuş»."),
  fi(K),
  tok("الدِّمَاءِ", "dam", "noun", [K, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ.", "«the blood».", "«kana»."),
  tok("نَوَاهِلِ", "nahil", "noun", [K, QF, "naat-sifa", "jam-taksir", "mamnu-min-sarf"], "نَعْتٌ لِطَيْرٍ مَجْرُورٌ — جَمْعُ نَاهِلٍ عَلَى فَوَاعِلَ، مَمْنُوعٌ مِنَ الصَّرْفِ صُرِفَ بِالْكَسْرِ لِلْقَافِيَةِ. الرَّوِيُّ اللَّامُ.", "«drinking their fill» — a diptote given kasra for the rhyme; rawi lam.", "«kana kanan» — kafiye için kesre almış gayr-i munsarif; revî lâm."),
 ]})
S[-1]["badi"] = [SR("ziyada", "s24", "mamduh", "ghayr-zahir")]
S.append({"id": "s26", "translation": {
 "en": "«They stayed with the standards until it was as though * they were of the army — except that they did not fight» — part of al-Afwah's meaning taken, and the addition betters it: hidden.",
 "tr": "«Sancaklarla kaldılar, öyle ki sanki * ordudandılar — ancak savaşmadılar» — Efveh'in manasının bir kısmı alınmış, ek onu güzelleştirir: hafî."},
 "tokens": [
  tok("أَقَامَتْ", "aqama", "verb", [K, A, "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — أَيِ الْعِقْبَانُ.", "«they stayed» — the eagles.", "«kaldılar» — kartallar."),
  tok("مَعَ", "maa", "noun", [K, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«ile»."),
  tok("الرَّايَاتِ", "raya", "noun", [K, "idafa-definiteness", "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ رَايَةٍ.", "«the standards».", "«sancaklarla»."),
  tok("حَتَّى", "hatta", "part", [K, "huruf-jarr"], "حَرْفُ ابْتِدَاءٍ — تَدْخُلُ عَلَى الْجُمْلَةِ.", "«until» — the hatta of a new clause.", "«öyle ki» — ibtidâ hattâsı."),
  tok("كَأَنَّهَا", "kaanna", "part", [K, "inna-wa-akhawatuha"], "كَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«as though they».", "«sanki onlar».", segments=[seg("كَأَنَّ", "kaanna", "part"), seg("هَا", "pron-3fs", "pron")], punct="*"),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَأَنَّ.", "«of» — the khabar.", "«-den» — haber."),
  tok("الْجَيْشِ", "jaysh", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the army».", "«ordu»."),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ — اسْتِثْنَاءٌ مُنْقَطِعٌ بِمَعْنَى لَكِنْ.", "«except» — a detached exception: «but».", "«ancak» — munkatı' istisnâ: «fakat»."),
  tok("أَنَّهَا", "anna", "part", [K, "inna-am-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا — وَالْمَصْدَرُ مُسْتَثْنًى.", "«that they».", "«onlar».", segments=[seg("أَنَّ", "anna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-ma-»."),
  tok("تُقَاتِلِ", "qatala-iii", "verb", [K, QF, "lam-jazim", "form-iii-verbs", "inna-am-anna"], "مُضَارِعٌ مَجْزُومٌ بِلَمْ، كُسِرَ لِلْقَافِيَةِ — خَبَرُ أَنَّ؛ قَاتَلَ يُقَاتِلُ. الرَّوِيُّ اللَّامُ.", "«did fight» — jussive, given kasra for the rhyme; rawi lam.", "«savaşmadılar» — meczûm, kafiye için kesre; revî lâm."),
 ]})

# ----------- s27 — most of it accepted; the more hidden, the nearer to acceptance (RESTORED)
S.append({"id": "s27", "translation": {
 "en": "And this and its likes — most of it is accepted; and among it is what fine handling brings out from the rank of following into the domain of invention. And the more hidden it is, the nearer to acceptance." + R_EN,
 "tr": "Bu ve benzerleri — çoğu makbuldür; güzel tasarrufun tâbi olma sınıfından ibdâ' alanına çıkardığı da bundandır. Ne kadar gizli olursa kabule o kadar yakındır." + R_TR},
 "tokens": [
  tok("وَهَذَا", "hadha", "pron", [K, "asma-al-ishara", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهَذَا اسْمُ إِشَارَةٍ مُبْتَدَأٌ.", "«and this».", "«ve bu».", segments=[seg("وَ", "wa", "conj"), seg("هَذَا", "hadha", "pron")]),
  tok("وَأَمْثَالُهُ", "mithl", "noun", [K, "atf-nasaq", "idafa-definiteness", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَأَمْثَالُ مَعْطُوفٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ مِثْلٍ.", "«and its likes».", "«ve benzerleri».", segments=[seg("وَ", "wa", "conj"), seg("أَمْثَالُ", "mithl", "noun"), pr3ms()]),
  tok("أَكْثَرُهُ", "akthar", "noun", [K, "mubtada-khabar", "idafa-definiteness", "ism-tafdil"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«most of it» — the second mubtada.", "«çoğu» — ikinci mübtedâ."),
  tok("مَقْبُولٌ", "maqbul", "noun", [K, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ هَذَا.", "«accepted».", "«makbuldür».", punct="،"),
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and among it».", "«ve ondandır».", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«… şey»."),
  tok("يُخْرِجُهُ", "akhraja", "verb", [K, "ism-mawsul", "form-iv-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ — صِلَةٌ.", "«brings out» — the sila.", "«çıkarır» — sıla.", segments=[seg("يُخْرِجُ", "akhraja", "verb"), pr3ms()]),
  tok("حُسْنُ", "husn", "noun", [K, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the fineness of».", "«güzelliği»."),
  tok("التَّصَرُّفِ", "tasarruf", "noun", [K, "idafa-definiteness", "masdar", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَصَرَّفَ.", "«handling».", "«tasarrufun»."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("قَبِيلِ", "qabil", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — الْقَبِيلُ: الصِّنْفُ.", "«the rank of».", "«sınıfından»."),
  tok("الِاتِّبَاعِ", "ittiba", "noun", [K, "idafa-definiteness", "masdar", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اتَّبَعَ.", "«following».", "«tâbi olmanın»."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«into».", "«-e»."),
  tok("حَيِّزِ", "hayyiz", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — الْحَيِّزُ: الْمَكَانُ وَالنَّاحِيَةُ.", "«the domain of».", "«alanına»."),
  tok("الِابْتِدَاعِ", "ibtida", "noun", [K, "idafa-definiteness", "masdar", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ ابْتَدَعَ.", "«invention».", "«ibdâ'ın».", punct="."),
  tok("وَكُلَّمَا", "kullama", "part", [K, "maful-fih"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَكُلَّمَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and whenever» — the conditional adverb.", "«ve ne zaman» — şart manalı zarf.", segments=[seg("وَ", "wa", "conj"), seg("كُلَّمَا", "kullama", "part")]),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is».", "«olursa»."),
  tok("أَشَدَّ", "ashadd", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ — اسْمُ تَفْضِيلٍ يَتَوَصَّلُ بِهِ إِلَى التَّفْضِيلِ بِالتَّمْيِيزِ.", "«more intense» — the helper elative.", "«daha şiddetli» — yardımcı ism-i tafdîl."),
  tok("خَفَاءً", "khafa-hiddenness", "noun", [K, "tamyiz", "masdar"], "تَمْيِيزٌ مَنْصُوبٌ — مَصْدَرُ خَفِيَ.", "«in hiddenness» — the tamyiz.", "«gizlilikte» — temyîz."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ — جَوَابُ كُلَّمَا.", "«it is» — the jawab.", "«olur» — cevap."),
  tok("أَقْرَبَ", "aqrab", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«nearer».", "«daha yakın»."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْقَبُولِ", "qabul", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ — مَصْدَرُ قَبِلَ.", "«acceptance».", "«kabule».", punct="."),
 ]})

# ----------- s28 — the closing rule: only where the taking is known (RESTORED)
S.append({"id": "s28", "translation": {
 "en": "And all of this is when it is KNOWN that the second took from the first; otherwise it is said: «so-and-so said such, and so-and-so had preceded him to it»." + R_EN,
 "tr": "Bütün bunlar ikincinin birinciden aldığı BİLİNDİĞİNDEDİR; yoksa şöyle denir: «falan şöyle dedi, ve falan onda ondan önce davranmıştı»." + R_TR},
 "tokens": [
  tok("وَهَذَا", "hadha", "pron", [K, "asma-al-ishara", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهَذَا مُبْتَدَأٌ.", "«and this».", "«ve bu».", segments=[seg("وَ", "wa", "conj"), seg("هَذَا", "hadha", "pron")]),
  tok("كُلُّهُ", "kull", "noun", [K, "tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«all of it» — the tawkid.", "«hepsi» — te'kîd."),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", "mubtada-khabar"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ — وَالظَّرْفُ خَبَرٌ.", "«when» — the khabar.", "«-dığında» — haber."),
  tok("عُلِمَ", "alima", "verb", [K, "idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it is known».", "«bilinirse»."),
  tok("أَنَّ", "anna", "part", [K, "inna-am-anna", "naib-al-fail"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ نَائِبُ فَاعِلٍ.", "«that» — the masdar is the naʾib.", "«-ğı» — masdar nâib-i fâil."),
  tok("الثَّانِيَ", "thani", "noun", [K, "inna-am-anna", "ism-maqsur-manqus"], "اسْمُ أَنَّ مَنْصُوبٌ — تَظْهَرُ الْفَتْحَةُ عَلَى الْمَنْقُوصِ.", "«the second» — the manqus shows its fatha.", "«ikinci» — mankûs fethasını gösterir."),
  tok("أَخَذَ", "akhadha", "verb", [K, "inna-am-anna"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — خَبَرُ أَنَّ.", "«took» — anna's khabar.", "«aldı» — ennenin haberi."),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْأَوَّلِ", "awwal", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the first».", "«birinciden».", punct="،"),
  tok("وَإِلَّا", "illa", "part", [K, "in-shartiyya", "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ شَرْطِيَّةٌ أُدْغِمَتْ فِي لَا النَّافِيَةِ — أَيْ وَإِنْ لَمْ يُعْلَمْ.", "«otherwise» — in + la, the verb concealed.", "«yoksa» — in + lâ, fiil mahzûf.", segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  tok("فَيُقَالُ", "qala", "verb", [K, "in-shartiyya", "naib-al-fail", "hollow-verbs"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَيُقَالُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — قَالَ يُقَالُ.", "«then it is said».", "«o zaman denir».", segments=[seg("فَ", "fa", "conj"), seg("يُقَالُ", "qala", "verb")], punct=":"),
  tok("قَالَ", "qala", "verb", [K, "fail"], "فِعْلٌ مَاضٍ — مَقُولُ الْقَوْلِ نَائِبُ فَاعِلِ يُقَالُ.", "«said» — the quoted clause is the naʾib.", "«dedi» — mekûl nâib-i fâil."),
  tok("فُلَانٌ", "fulan", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ — كِنَايَةٌ عَنِ الْعَلَمِ.", "«so-and-so».", "«falan»."),
  tok("كَذَا", "kadha", "part", [K, "maful-bihi"], "كِنَايَةٌ عَنِ الْمَقُولِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«such».", "«şöyle».", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, "qad-harf", "hal"], "الْوَاوُ لِلْحَالِ، وَقَدْ لِلتَّحْقِيقِ.", "«while indeed».", "«ve gerçekten».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("سَبَقَهُ", "sabaqa", "verb", [K, "hal", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ حَالٌ.", "«had preceded him».", "«ondan önce davranmıştı».", segments=[seg("سَبَقَ", "sabaqa", "verb"), pr3ms()]),
  tok("إِلَيْهِ", "ila", "prep", [K, "huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to it».", "«ona».", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("فُلَانٌ", "fulan", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ.", "«so-and-so».", "«falan».", punct="."),
 ]})

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 # part 1
 "ilmam": need("ilmam", "إِلْمَام", "ل م م", "noun", "ilmam — a touching, an alighting (masdar of Form IV أَلَمَّ بِهِ); of poetry: taking the meaning alone", "ilmâm — dokunma, uğrama (if'âl masdarı, elemme bihi); şiirde: yalnız manayı alma", 6),
 "salkh": need("salkh", "سَلْخ", "س ل خ", "noun", "salkh — flaying, stripping the skin (masdar of سَلَخَ); of poetry: the meaning taken bare of its words", "selh — deriyi yüzme (selaha masdarı); şiirde: mananın lafzından soyulup alınması", 6),
 "kadhalika": need("kadhalika", "كَذَلِكَ", None, "part", "likewise, so too (ka + dhalika)", "öylece, o da öyle (ke + zâlike)", 2),
 "madaha": need("madaha", "مَدَحَ", "م د ح", "verb", "to praise (مَدَحَ يَمْدَحُ)", "övmek, methetmek (medeha yemdehu)", 3),
 "sun": need("sun", "صُنْع", "ص ن ع", "noun", "a doing, a kindness done (masdar of صَنَعَ)", "yapış, iyilik (sane'a masdarı)", 5),
 "ajila": need("ajila", "عَجِلَ", "ع ج ل", "verb", "to hasten, to come quickly (عَجِلَ يَعْجَلُ)", "acele etmek, çabuk gelmek (acile ya'celu)", 4),
 "ratha-delay": need("ratha-delay", "رَاثَ", "ر ي ث", "verb", "to be slow, to tarry (hollow; رَاثَ يَرِيثُ) — the contrary of haste", "yavaş olmak, gecikmek (ecvef; râse yerîsu) — acelenin zıddı", 6),
 "rayth": need("rayth", "رَيْث", "ر ي ث", "noun", "slowness, delay (masdar of رَاثَ يَرِيثُ) — the contrary of haste", "yavaşlık, gecikme (râse yerîsu masdarı) — acelenin zıddı", 6),
 "mawdi": need("mawdi", "مَوْضِع", "و ض ع", "noun", "a place, a position (ism makan of وَضَعَ; pl. مَوَاضِع)", "yer, mevzi (vada'a'nın ism-i mekânı; ç. مَوَاضِع)", 3, plural="مَوَاضِع"),
 "anfa": need("anfa", "أَنْفَع", "ن ف ع", "noun", "more useful (the elative of نَافِع)", "daha faydalı (nâfi'in ism-i tafdîli)", 4),
 "but": need("but", "بُطْء", "ب ط أ", "noun", "slowness (masdar of بَطُؤَ)", "yavaşlık (batu'e masdarı)", 5),
 "sayb": need("sayb", "سَيْب", "س ي ب", "noun", "a gift, a flowing bounty", "bağış, akan ihsan", 6),
 "asra": need("asra", "أَسْرَع", "س ر ع", "noun", "faster (the elative of سَرِيع)", "daha hızlı (serî'in ism-i tafdîli)", 3),
 "masir": need("masir", "مَسِير", "س ي ر", "noun", "a journey, a moving along (masdar mimi of سَارَ)", "yürüyüş, gidiş (sâre'nin mimli masdarı)", 4),
 "jaham": need("jaham", "جَهَام", "ج ه م", "noun", "the jaham — a cloud that has emptied its rain", "cehâm — yağmurunu boşaltmış bulut", 6),
 "taallaqa": need("taallaqa", "تَأَلَّقَ", "أ ل ق", "verb", "to flash, to shine (Form V; تَأَلَّقَ يَتَأَلَّقُ)", "parlamak, ışıldamak (tefa''ul; teellaka yeteellaku)", 5),
 "masqul": need("masqul", "مَصْقُول", "ص ق ل", "noun", "polished (ism maf'ul of صَقَلَ)", "cilâlı (sakale'nin ism-i mef'ûlü)", 5),
 "adb": need("adb", "عَضْب", "ع ض ب", "noun", "a sharp sword (a sifa on فَعْل used as a name of the sword)", "keskin kılıç (fa'l vezninde sıfat, kılıcın adı)", 6),
 "rumh": need("rumh", "رُمْح", "ر م ح", "noun", "a spear (pl. رِمَاح)", "mızrak (ç. رِمَاح)", 3, plural="رِمَاح"),
 "tan": need("tan", "طَعْن", "ط ع ن", "noun", "thrusting, stabbing (masdar of طَعَنَ)", "mızrak saplama (ta'ane masdarı)", 4),
 "khurs": need("khurs", "خُرْص", "خ ر ص", "noun", "a spearhead (pl. خُرْصَان)", "mızrak ucu (ç. خُرْصَان)", 6, plural="خُرْصَان"),
 "arabi-bedouin": need("arabi-bedouin", "أَعْرَابِيّ", "ع ر ب", "noun", "a Bedouin, a desert Arab (the nisba of أَعْرَاب)", "bedevî, çöl Arabı (a'râb'ın nisbesi)", 4),
 "dhira": need("dhira", "ذِرَاع", "ذ ر ع", "noun", "the forearm, the arm (fem.; pl. أَذْرُع) — «wide of arm»: generous", "kol, zirâ (müennes; ç. أَذْرُع) — «kolu geniş»: cömert", 3, plural="أَذْرُع"),
 "arhab": need("arhab", "أَرْحَب", "ر ح ب", "noun", "wider, roomier (the elative of رَحْب)", "daha geniş (rahb'ın ism-i tafdîli)", 4),
 "ashja": need("ashja", "أَشْجَع", None, "propn", "Ashjaʿ — Ashjaʿ al-Sulami, the ʿAbbasid panegyrist (d. c. 195 AH)", "Eşca' — Abbâsî methiye şairi Eşca' es-Sülemî (ö. yak. 195)", 6),
 "awsa-wider": need("awsa-wider", "أَوْسَع", "و س ع", "noun", "wider, more abundant (the elative of وَاسِع)", "daha geniş, daha bol (vâsi'in ism-i tafdîli)", 3),
 "maruf": need("maruf", "مَعْرُوف", "ع ر ف", "noun", "a kindness, a good deed (ism maf'ul of عَرَفَ: the known good)", "iyilik, ihsan (arafe'nin ism-i mef'ûlü: bilinen iyi)", 3),
 "jarir": need("jarir", "جَرِير", None, "propn", "Jarir — Jarir b. ʿAtiyya al-Tamimi, the Umayyad poet (d. 110 AH)", "Cerîr — Emevî şairi Cerîr b. Atıyye et-Temîmî (ö. 110)", 5),
 "lihya": need("lihya", "لِحْيَة", "ل ح ي", "noun", "a beard (pl. لِحًى)", "sakal (ç. لِحًى)", 3, plural="لِحًى"),
 "khimar": need("khimar", "خِمَار", "خ م ر", "noun", "a woman's head-veil (pl. خُمُر)", "başörtüsü (ç. خُمُر)", 4, plural="خُمُر"),
 "khidab": need("khidab", "خِضَاب", "خ ض ب", "noun", "dye, henna for the hands", "kına, el boyası", 5),
 "dhamma": need("dhamma", "ذَمَّ", "ذ م م", "verb", "to blame (doubled; ذَمَّ يَذُمُّ)", "kınamak, zemmetmek (muzâaf; zemme yezummu)", 3),
 "baada": need("baada", "بَعُدَ", "ب ع د", "verb", "to be far (بَعُدَ يَبْعُدُ)", "uzak olmak (be'ude yeb'udu)", 3),
 # part 2
 "naqala": need("naqala", "نَقَلَ", "ن ق ل", "verb", "to move, to transfer (نَقَلَ يَنْقُلُ)", "nakletmek, taşımak (nekale yenkulu)", 3),
 "dam": need("dam", "دَم", "د م ي", "noun", "blood (pl. دِمَاء)", "kan (ç. دِمَاء)", 2, plural="دِمَاء"),
 "muhmarr": need("muhmarr", "مُحْمَرّ", "ح م ر", "noun", "reddening, turned red (ism fa'il of Form IX احْمَرَّ)", "kızarmış, kızıllaşan (if'ilâl ism-i fâili)", 5),
 "yabisa": need("yabisa", "يَبِسَ", "ي ب س", "verb", "to dry (يَبِسَ يَيْبَسُ)", "kurumak (yebise yeybesu)", 4),
 "naji": need("naji", "نَجِيع", "ن ج ع", "noun", "the dark blood from within the body", "koyu iç kanı", 6),
 "mujarrad": need("mujarrad", "مُجَرَّد", "ج ر د", "noun", "bared, drawn; stripped of (ism maf'ul of Form II جَرَّدَ)", "sıyrılmış, çıplak; …-den soyulmuş (tef'îl ism-i mef'ûlü)", 5),
 "ghimd": need("ghimd", "غِمْد", "غ م د", "noun", "a scabbard, a sheath (pl. أَغْمَاد)", "kın (ç. أَغْمَاد)", 5, plural="أَغْمَاد"),
 "mughmad": need("mughmad", "مُغْمَد", "غ م د", "noun", "sheathed (ism maf'ul of Form IV أَغْمَدَ)", "kınına sokulmuş (if'âl ism-i mef'ûlü)", 5),
 "ashmal": need("ashmal", "أَشْمَل", "ش م ل", "noun", "more comprehensive, wider (the elative of شَامِل)", "daha kapsamlı, daha şümullü (şâmil'in ism-i tafdîli)", 5),
 "ghadiba": need("ghadiba", "غَضِبَ", "غ ض ب", "verb", "to be angry (غَضِبَ عَلَيْهِ يَغْضَبُ)", "kızmak, öfkelenmek (gadibe aleyhi yagdabu)", 3),
 "tamim": need("tamim", "تَمِيم", None, "propn", "Tamim — the great tribe of Najd, Jarir's own", "Temîm — Necd'in büyük kabilesi, Cerîr'in kabilesi", 5),
 "alam-world": need("alam-world", "عَالَم", "ع ل م", "noun", "the world, all creation (pl. عَالَمُونَ / عَوَالِم)", "âlem, bütün yaratılmışlar (ç. عَالَمُونَ / عَوَالِم)", 2, plural="عَوَالِم"),
 "mustankar": need("mustankar", "مُسْتَنْكَر", "ن ك ر", "noun", "a thing held strange, denied (ism maf'ul of Form X اسْتَنْكَرَ)", "yadırganan, uzak görülen (istif'âl ism-i mef'ûlü)", 5),
 "naqid-contrary": need("naqid-contrary", "نَقِيض", "ن ق ض", "noun", "the contrary, the contradictory (فَعِيل): what cannot hold together with a thing", "nakîz, zıt (fa'îl): bir şeyle bir arada olamayan", 5),
 "shis": need("shis", "الشِّيص", None, "propn", "al-Shis — in Abu l-Shis al-Khuzaʿi, the ʿAbbasid poet (d. c. 196 AH)", "Şîs — Ebü'ş-Şîs el-Huzâî adında, Abbâsî şairi (ö. yak. 196)", 6),
 "malama": need("malama", "مَلَامَة", "ل و م", "noun", "blame, reproach (a masdar of لَامَ)", "kınama, melâmet (lâme'nin masdarı)", 4),
 "hawa-passion": need("hawa-passion", "هَوًى", "ه و ي", "noun", "passion, love; the desire of the soul (maqsur; pl. أَهْوَاء)", "hevâ, aşk; nefsin arzusu (maksûr; ç. أَهْوَاء)", 3, plural="أَهْوَاء"),
 "ladhidh": need("ladhidh", "لَذِيذ", "ل ذ ذ", "noun", "delicious, delightful (a sifa mushabbaha on فَعِيل)", "lezzetli, tatlı (fa'îl vezninde sıfat-ı müşebbehe)", 3),
 "lama": need("lama", "لَامَ", "ل و م", "verb", "to blame (hollow; لَامَ يَلُومُ)", "kınamak (ecvef; lâme yelûmu)", 3),
 "luwwam": need("luwwam", "لُوَّم", "ل و م", "noun", "the blamers (plural of لَائِم on فُعَّل)", "kınayanlar (lâim'in fu''al vezninde cem'i)", 6),
 "afwah": need("afwah", "الْأَفْوَه", None, "propn", "al-Afwah — al-Afwah al-Awdi, the pre-Islamic poet and chief of Awd", "Efveh — câhiliye şairi ve Evd reisi Efveh el-Evdî", 6),
 "athar": need("athar", "أَثَر", "أ ث ر", "noun", "a track, a trace (pl. آثَار)", "iz, eser (ç. آثَار)", 2, plural="آثَار"),
 "mara": need("mara", "مَارَ", "م ي ر", "verb", "to bring provisions to (hollow; مَارَ يَمِيرُ; passive: to be provisioned, fed)", "azık getirmek (ecvef; mâre yemîru; meçhûlü: azıklanmak, doyurulmak)", 6),
 "zallala": need("zallala", "ظَلَّلَ", "ظ ل ل", "verb", "to shade, to cast shade over (Form II; ظَلَّلَ يُظَلِّلُ)", "gölgelemek (tef'îl; zallele yuzallilu)", 5),
 "uqab": need("uqab", "عُقَاب", "ع ق ب", "noun", "an eagle (fem.; pl. عِقْبَان)", "kartal (müennes; ç. عِقْبَان)", 4, plural="عِقْبَان"),
 "nahil": need("nahil", "نَاهِل", "ن ه ل", "noun", "drinking one's fill (ism fa'il of نَهِلَ; pl. نَوَاهِل / نِهَال)", "kana kana içen (nehile'nin ism-i fâili; ç. نَوَاهِل)", 6, plural="نَوَاهِل"),
 "raya": need("raya", "رَايَة", "ر أ ي", "noun", "a standard, a flag (pl. رَايَات)", "sancak, bayrak (ç. رَايَات)", 3, plural="رَايَات"),
 "jaysh": need("jaysh", "جَيْش", "ج ي ش", "noun", "an army (pl. جُيُوش)", "ordu (ç. جُيُوش)", 2, plural="جُيُوش"),
 "qatala-iii": need("qatala-iii", "قَاتَلَ", "ق ت ل", "verb", "to fight (Form III; قَاتَلَ يُقَاتِلُ)", "savaşmak (mufâale; kâtele yukâtilu)", 3),
 "qabil": need("qabil", "قَبِيل", "ق ب ل", "noun", "a kind, a class — مِنْ قَبِيلِ: of the sort of", "sınıf, tür — min kabîli: … türünden", 4),
 "hayyiz": need("hayyiz", "حَيِّز", "ح و ز", "noun", "a domain, a space (فَيْعِل of حَازَ)", "alan, saha (hâze'nin fey'il vezni)", 5),
 "ashadd": need("ashadd", "أَشَدّ", "ش د د", "noun", "more intense, stronger (the elative of شَدِيد) — the helper elative before a tamyiz", "daha şiddetli, daha güçlü (şedîd'in ism-i tafdîli) — temyîz önünde yardımcı ism-i tafdîl", 3),
 "khafa-hiddenness": need("khafa-hiddenness", "خَفَاء", "خ ف ي", "noun", "hiddenness (masdar of خَفِيَ)", "gizlilik, hafâ (hafiye masdarı)", 4),
 "aqrab": need("aqrab", "أَقْرَب", "ق ر ب", "noun", "nearer (the elative of قَرِيب)", "daha yakın (karîb'in ism-i tafdîli)", 3),
 "qabul": need("qabul", "قَبُول", "ق ب ل", "noun", "acceptance (masdar of قَبِلَ)", "kabul (kabile masdarı)", 3),
 "sabaqa": need("sabaqa", "سَبَقَ", "س ب ق", "verb", "to precede, to get there first (سَبَقَ يَسْبِقُ; سَبَقَهُ إِلَيْهِ)", "önce gelmek, önce davranmak (sebeka yesbiku; sebekahu ileyhi)", 3),
 "hassana": need("hassana", "حَسَّنَ", "ح س ن", "verb", "to make fine, to better (Form II; حَسَّنَ يُحَسِّنُ)", "güzelleştirmek (tef'îl; hassene yuhassinu)", 3),
}
# every lex key the chapter uses is either minted above or owned by a package
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

# ---------------------------------------------------------------- paradigms
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "madaha", _sg.sound1("fataha", "مَدَح", "مْدَح", "اِمْدَح", "مَدْح", "مَادِح", "مَمْدُوح", "مُدِحَ", "يُمْدَحُ", "مَدَحَ يَمْدَحُ — مِنْ بَابِ فَتَحَ؛ مَجْهُولُهُ يُمْدَحُ."))
put_morph(mo, "dhamma", gem("nasara", "ذَمّ", "ذَمَم", "ذُمّ", "ذْمُم", ["ذُمَّ", "ذُمَّا", "ذُمُّوا", "ذُمِّي", "ذُمَّا", "اُذْمُمْنَ"], "ذَمّ", "ذَامّ", "مَذْمُوم", "ذُمَّ", "يُذَمُّ",
                                "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: ذَمَّ يَذُمُّ — مَجْهُولُهُ يُذَمُّ."))
put_morph(mo, "ajila", _sg.sound1("samia", "عَجِل", "عْجَل", "اِعْجَل", "عَجَل", "عَاجِل", None, None, None, "عَجِلَ يَعْجَلُ — مِنْ بَابِ سَمِعَ."))
put_morph(mo, "baada", _sg.sound1("karuma", "بَعُد", "بْعُد", "اُبْعُد", "بُعْد", "بَعِيد", None, None, None, "بَعُدَ يَبْعُدُ — مِنْ بَابِ حَسُنَ؛ صِفَتُهُ بَعِيدٌ."))
put_morph(mo, "taallaqa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَأَلَّق", "تَأَلَّق", "تَأَلَّق", "تَأَلُّق", "مُتَأَلِّق", None, None, None, "تَأَلَّقَ يَتَأَلَّقُ: لَمَعَ — لَازِمٌ."))
put_morph(mo, "naqala", _sg.sound1("nasara", "نَقَل", "نْقُل", "اُنْقُل", "نَقْل", "نَاقِل", "مَنْقُول", "نُقِلَ", "يُنْقَلُ", "نَقَلَ يَنْقُلُ — مِنْ بَابِ نَصَرَ؛ مَجْهُولُهُ يُنْقَلُ."))
put_morph(mo, "yabisa", _sg.sound1("samia", "يَبِس", "يْبَس", "اِيبَس", "يُبْس", "يَابِس", None, None, None, "يَبِسَ يَيْبَسُ — مِثَالٌ يَائِيٌّ مِنْ بَابِ سَمِعَ؛ تَثْبُتُ يَاؤُهُ فِي الْمُضَارِعِ.", cls="مِثَالٌ يَائِيٌّ"))
put_morph(mo, "ghadiba", _sg.sound1("samia", "غَضِب", "غْضَب", "اِغْضَب", "غَضَب", "غَاضِب / غَضْبَان", "مَغْضُوب (عَلَيْهِ)", "غُضِبَ", "يُغْضَبُ", "غَضِبَ يَغْضَبُ — مِنْ بَابِ سَمِعَ؛ يَتَعَدَّى بِعَلَى."))
put_morph(mo, "lama", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "لَام", "لُم", "لُوم", "لُم", "لُوم", "لُم", "لَوْم / مَلَامَة", "لَائِم", "مَلُوم", "لِيمَ", "يُلَامُ", "لَامَ يَلُومُ — أَجْوَفٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ؛ مَجْزُومُهُ يَلُمْ."))
put_morph(mo, "ratha-delay", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "رَاث", "رِث", "رِيث", "رِث", "رِيث", "رِث", "رَيْث", "رَائِث", None, None, None, "رَاثَ يَرِيثُ: أَبْطَأَ — أَجْوَفٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ مَجْزُومُهُ يَرِثْ."))
put_morph(mo, "mara", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "مَار", "مِر", "مِير", "مِر", "مِير", "مِر", "مَيْر", "مَائِر", "مَمِير", "مِيرَ", "يُمَارُ", "مَارَ يَمِيرُ: جَلَبَ الْمِيرَةَ — أَجْوَفٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ مَجْهُولُهُ يُمَارُ."))
put_morph(mo, "zallala", _sg.derived(_sg.B2, _sg.W2, "ُ", "ظَلَّل", "ظَلِّل", "ظَلِّل", "تَظْلِيل", "مُظَلِّل", "مُظَلَّل", "ظُلِّلَ", "يُظَلَّلُ", "ظَلَّلَ يُظَلِّلُ — مَجْهُولُهُ ظُلِّلَ."))
put_morph(mo, "hassana", _sg.idgham(_sg.derived(_sg.B2, _sg.W2, "ُ", "حَسَّن", "حَسِّن", "حَسِّن", "تَحْسِين", "مُحَسِّن", "مُحَسَّن", "حُسِّنَ", "يُحَسَّنُ", "حَسَّنَ يُحَسِّنُ.")))
put_morph(mo, "qatala-iii", _sg.derived(_sg.B3, _sg.W3, "ُ", "قَاتَل", "قَاتِل", "قَاتِل", "مُقَاتَلَة / قِتَال", "مُقَاتِل", "مُقَاتَل", "قُوتِلَ", "يُقَاتَلُ", "قَاتَلَ يُقَاتِلُ — مَجْزُومُهُ يُقَاتِلْ."))
put_morph(mo, "sabaqa", _sg.sound1("daraba", "سَبَق", "سْبِق", "اِسْبِق", "سَبْق", "سَابِق", "مَسْبُوق", "سُبِقَ", "يُسْبَقُ", "سَبَقَ يَسْبِقُ — مِنْ بَابِ ضَرَبَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE = {
 "id": "sariqat-ghayr-zahira",
 "title": {"ar": "الْإِلْمَامُ وَالْأَخْذُ غَيْرُ الظَّاهِرِ — تَشَابُهٌ وَنَقْلٌ وَشُمُولٌ وَقَلْبٌ وَزِيَادَةٌ", "en": "The ilmam and the hidden taking — resemblance, moving, widening, qalb, addition", "tr": "İlmâm ve zâhir olmayan alma — benzeşme, nakil, şümul, kalb, ziyade"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الخاتمة: وإن أخذ المعنى وحده سمي إلماما وسلخا؛ وغير الظاهر منه أن يتشابه المعنيان … وكلما كان أشد خفاء كان أقرب إلى القبول"],
 "question": {
  "en": ["What is the ILMAM? The meaning alone taken, with none of the words — also called salkh, a flaying (s1). Like the ighara it has three grades: the second better and praised (Abu Tammam's «if it hastens, good; if it tarries, in some places the delay is more useful» taken up by al-Mutanabbi's «the fastest cloud is the one with no rain», s2-s4); the second worse and blamed (al-Buhturi's polished speech like a sword, al-Mutanabbi's tongues as spearheads, s5-s7); equal, no blame, the merit the first's (the Bedouin's «widest of arm», Ashjaʿ's «his kindness is the widest», s8-s10).",
         "What is the HIDDEN taking? Five doors (s11-s26): the two meanings merely RESEMBLE (Jarir's «the turbaned and the veiled are alike», al-Mutanabbi's «spear or dye in the hand»); the meaning MOVED to another place (al-Buhturi's stripped slain reddened by blood, al-Mutanabbi's drawn sword that the dried blood sheathes); the second's meaning WIDER (Jarir's «all mankind angry» widened by Abu Nuwas to «the world in one man»); the QALB, the contrary (Abu l-Shis loves the blame, al-Mutanabbi counts it an enemy); PART taken and BETTERED by an addition (al-Afwah's birds following the army, Abu Tammam's eagles that «stayed with the standards … except that they did not fight»).",
         "What does the book rule? Most of the hidden kind is accepted; fine handling can lift it out of following into invention; and the more hidden the taking, the nearer it is to acceptance (s27). And all of this only where it is KNOWN that the second took from the first — otherwise one says only: so-and-so said it, and so-and-so had said it before him (s28).",
         "What does the engine read? The `sariqa` frame sits on the taker's bayt with `with` naming the source; for the hidden kind the engine cannot see the meaning, so it counts the shared roots (few, as the words differ), prints them, and reports the authored kind2 as the book's naming — tashabuh, naql, ashmal, qalb, ziyada — while the plain kind's naskh/ighara/ilmam it computes itself. The ʿarūḍ card scans each bayt and names its metre and rhyme letter."],
  "tr": ["İLMÂM nedir? Lafzın hiçbiri olmaksızın yalnız mananın alınması — selh, yüzme de denir (s1). İğâre gibi üç derecesi vardır: ikinci daha iyi ve memdûh (Ebû Temmâm'ın «acele olursa hayır; gecikirse bazı yerlerde gecikme daha faydalı» sözünü Mütenebbî'nin «bulutların en hızlısı yağmursuz olanı» ile alması, s2-s4); ikinci daha kötü ve mezmûm (Buhturî'nin kılıç gibi cilâlı sözü, Mütenebbî'nin mızrak ucu gibi dilleri, s5-s7); dengi, zem yok, fazilet birincinin (Bedevî'nin «kolu en geniş»i, Eşca'ın «iyiliği en geniş»i, s8-s10).",
         "ZÂHİR OLMAYAN alma nedir? Beş kapı (s11-s26): iki mananın yalnızca BENZEŞMESİ (Cerîr'in «sarıklı ile başörtülü birdir»i, Mütenebbî'nin «elde mızrak yahut kına»sı); mananın başka yere NAKLİ (Buhturî'nin kanla kızaran soyulmuş ölüleri, Mütenebbî'nin kuruyan kanın kınına soktuğu sıyrılmış kılıcı); ikincinin manasının DAHA KAPSAMLI olması (Cerîr'in «bütün insanlar kızgın»ını Ebû Nüvâs'ın «âlem bir kişide»ye genişletmesi); KALB, zıt mana (Ebü'ş-Şîs kınanmayı sever, Mütenebbî onu düşman sayar); BİR KISMIN alınıp bir ekle GÜZELLEŞTİRİLMESİ (Efveh'in orduyu izleyen kuşları, Ebû Temmâm'ın «sancaklarla kalan … ancak savaşmayan» kartalları).",
         "Kitap ne hükmeder? Hafî türün çoğu makbuldür; güzel tasarruf onu tâbi olmaktan ibdâ'a çıkarabilir; alma ne kadar gizliyse kabule o kadar yakındır (s27). Ve bütün bunlar ancak ikincinin birinciden aldığı BİLİNDİĞİNDE — yoksa yalnız şöyle denir: falan söyledi, falan da ondan önce söylemişti (s28).",
         "Motor neyi okur? `sariqa` çerçevesi alanın beytinde durur, `with` kaynağı adlandırır; hafî türde motor manayı göremez, bu yüzden ortak kökleri sayar (lafız farklı olduğundan az), onları basar ve yazarın kind2'sini kitabın adlandırması olarak bildirir — teşâbüh, nakl, eşmel, kalb, ziyâde — zâhir türün nesh/iğâre/ilmâmını ise kendisi hesaplar. Arûz kartı her beyti taktî' eder, bahrini ve revî harfini adlandırır."]},
 "plain": {
  "en": "Taking only another poet's idea has the same three grades as the raid. Hidden taking — resembling, moving, widening, reversing or adding to the idea — is mostly accepted, and the better hidden, the more accepted; but call it taking only when you know it was.",
  "tr": "Başka şairin yalnız fikrini almak, yağmanın üç derecesine tâbidir. Gizli alma — fikri benzetme, taşıma, genişletme, tersine çevirme yahut ona ekleme — çoğunlukla makbuldür, ne kadar gizliyse o kadar makbul; ama alma olduğunu bilmeden alma deme."},
 "explanation": {
  "en": "وَإِنْ أُخِذَ الْمَعْنَى وَحْدَهُ سُمِّيَ إِلْمَامًا وَسَلْخًا. The plain taking ends with the ilmam: the words all gone, the meaning kept, graded like the ighara by the second poet's success. Then the book turns to what is NOT plain — the takings a reader would not notice without being told: the two meanings resemble each other; the meaning is moved from the slain to the sword; the second poet widens what the first said of one tribe to the whole world; the second says the contrary of the first; the second takes a part and adds what betters it. The rulings are RESTORED from the received matn and marked; the bayts are the source's printed Arabic. In the reader the sariqa frame prints both bayts with the shared roots lit, the kind2 chip and, where the book gives one, the grade; the ʿarūḍ card beneath scans the bayt and names its metre (kāmil, wāfir, sarīʿ, ramal, ṭawīl) and its rawī.",
  "tr": "وَإِنْ أُخِذَ الْمَعْنَى وَحْدَهُ سُمِّيَ إِلْمَامًا وَسَلْخًا. Zâhir alma ilmâm ile biter: lafız tamamen gitmiş, mana kalmış, iğâre gibi ikinci şairin başarısına göre derecelendirilir. Sonra kitap zâhir OLMAYANA döner — söylenmeden okuyanın fark etmeyeceği almalar: iki mana benzeşir; mana öldürülenlerden kılıca taşınır; ikinci şair birincinin bir kabile için dediğini bütün âleme genişletir; ikinci birincinin zıddını söyler; ikinci bir kısmını alıp onu güzelleştireni ekler. Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; beyitler kaynağın basılı Arapçasıdır. Okuyucuda sariqa çerçevesi iki beyti ortak kökleri yanmış olarak basar, kind2 çipini ve kitap verdiyse dereceyi gösterir; altındaki arûz kartı beyti taktî' eder, bahrini (kâmil, vâfir, serî', remel, tavîl) ve revîsini adlandırır."},
 "examples": [
  {"ar": "وَمِنَ الْخَيْرِ بُطْءُ سَيْبِكَ عَنِّي * أَسْرَعُ السُّحْبِ فِي الْمَسِيرِ الْجَهَامُ", "en": "al-Mutanabbi from Abu Tammam — an ilmam that is praised.", "tr": "Mütenebbî, Ebû Temmâm'dan — memdûh bir ilmâm.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "يَبِسَ النَّجِيعُ عَلَيْهِ وَهُوَ مُجَرَّدٌ * عَنْ غِمْدِهِ فَكَأَنَّمَا هُوَ مُغْمَدُ", "en": "al-Mutanabbi from al-Buhturi — the meaning moved from the slain to the sword.", "tr": "Mütenebbî, Buhturî'den — mana ölülerden kılıca taşınmış.", "sourceStory": "talkhis-al-miftah", "sentence": "s16"},
  {"ar": "وَلَيْسَ مِنَ اللهِ بِمُسْتَنْكَرٍ * أَنْ يَجْمَعَ الْعَالَمَ فِي وَاحِدٍ", "en": "Abu Nuwas from Jarir — the second's meaning wider and finer.", "tr": "Ebû Nüvâs, Cerîr'den — ikincinin manası daha kapsamlı ve daha güzel.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"},
  {"ar": "أَأُحِبُّهُ وَأُحِبُّ فِيهِ مَلَامَةً * إِنَّ الْمَلَامَةَ فِيهِ مِنْ أَعْدَائِهِ", "en": "al-Mutanabbi from Abu l-Shis — the qalb: the contrary meaning.", "tr": "Mütenebbî, Ebü'ş-Şîs'ten — kalb: zıt mana.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"},
  {"ar": "أَقَامَتْ مَعَ الرَّايَاتِ حَتَّى كَأَنَّهَا * مِنَ الْجَيْشِ إِلَّا أَنَّهَا لَمْ تُقَاتِلِ", "en": "Abu Tammam from al-Afwah — part taken, and the addition betters it.", "tr": "Ebû Temmâm, Efveh'ten — bir kısmı alınmış, ek onu güzelleştirir.", "sourceStory": "talkhis-al-miftah", "sentence": "s26"}],
 "commonMistakes": [
  {"wrong": "«İki beyit aynı şeyi söylüyor: ikincisi çalmış»",
   "right": "«وَهَذَا كُلُّهُ إِذَا عُلِمَ أَنَّ الثَّانِيَ أَخَذَ مِنَ الْأَوَّلِ — bilinmiyorsa yalnız: falan dedi, falan ondan önce demişti»",
   "why": {"en": "The book's last fence: a taking is a matter of knowledge, not of resemblance. Without it there is only precedence to record.", "tr": "Kitabın son çiti: alma bir bilgi meselesidir, benzerlik meselesi değil. Bilgi yoksa yalnız öncelik kaydedilir."}},
  {"wrong": "«Gizli alma daha kötüdür, çünkü saklanmıştır»",
   "right": "«وَكُلَّمَا كَانَ أَشَدَّ خَفَاءً كَانَ أَقْرَبَ إِلَى الْقَبُولِ — ne kadar gizliyse kabule o kadar yakındır»",
   "why": {"en": "In the badiʿ hiddenness is a merit: the second poet has worked the meaning into something of his own.", "tr": "Bedî'de gizlilik bir meziyettir: ikinci şair manayı kendine ait bir şeye dönüştürmüştür."}}],
 "relatedNotes": ["sariqat-shiriyya", "ilm-al-arud", "al-qafiya"]}

ADD_EN = (" Chapter 74 (lines ~4661-4700, sahifa 161-164): the ilmam in its three grades (s1-s10; Abu Tammam and al-Mutanabbi, al-Buhturi and "
          "al-Mutanabbi, the Bedouin and Ashjaʿ) and the hidden taking (s11-s26; Jarir and al-Mutanabbi; al-Buhturi and al-Mutanabbi; Jarir and "
          "Abu Nuwas; Abu l-Shis and al-Mutanabbi; al-Afwah and Abu Tammam), with the closing rules (s27-s28). The rulings are RESTORED from the "
          "received matn and marked; the bayts are the source's printed Arabic. The `sariqa` frames carry sub `ghayr-zahir` and the book's kind2.")
ADD_TR = (" Yetmiş dördüncü bâb (satır ~4661-4700, sahife 161-164): üç derecesiyle ilmâm (s1-s10; Ebû Temmâm ve Mütenebbî, Buhturî ve Mütenebbî, "
          "Bedevî ve Eşca') ve zâhir olmayan alma (s11-s26; Cerîr ve Mütenebbî; Buhturî ve Mütenebbî; Cerîr ve Ebû Nüvâs; Ebü'ş-Şîs ve Mütenebbî; "
          "Efveh ve Ebû Temmâm), kapanış kurallarıyla (s27-s28). Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; beyitler kaynağın "
          "basılı Arapçasıdır. `sariqa` çerçeveleri `ghayr-zahir` alt türünü ve kitabın kind2'sini taşır.")
write_out(74, S, TITLE, ADD_EN, ADD_TR, "4661-4700", GLOSS_ADD, notes=(NOTE,),
          related=(("sariqat-shiriyya", ["sariqat-ghayr-zahira"]), ("ilm-al-badi", ["sariqat-ghayr-zahira"]), ("ilm-al-arud", ["sariqat-ghayr-zahira"])))
report(74, S, GLOSS_ADD, (NOTE,))
