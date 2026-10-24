# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 10: THE NUMBER NOUNS. The number noun defined (the notebook's Arabic), the twelve roots, the gender of three to ten,
the compounds eleven to nineteen, the decades shared by both genders, the hundreds and thousands, the joining of the units to the
decades and of everything to the hundreds, the tamyiz rules, and the ordinals from the second to the tenth.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~213-215 of the transcription.

  VERBATIM from the notebook's Arabic: s1 (the definition) and every number form and example it lists.
  RESTORED (the rulings stand in Turkish; the received matn of the Kafiya is written and marked): s2-s9.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch10.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "asma-al-adad-fil-kafiya"
TM = "al-tamyiz-wa-ahkamuh"
MR = "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"
TITLE = {"ar": "أَسْمَاءُ الْعَدَدِ", "en": "The number nouns", "tr": "Sayı isimleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def nums(items, first_ar="فِي مَحَلِّ جَرٍّ.", last_punct=None):
    """a cited list: first bare, the rest joined by waw; items = (full, lex, en, tr)"""
    out = []
    for i, (full, lex, en, tr) in enumerate(items):
        p = last_punct if i == len(items) - 1 else None
        if i == 0: out.append(cited(full, lex, "noun", [K], first_ar, en, tr, punct=p))
        else: out.append(cited_wa("وَ" + full, lex, "noun", [K], full + " مَعْطُوفٌ.", "«and» " + en, "«ve» " + tr, full, punct=p))
    return out

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The number nouns: what is coined for the quantity of the units of things.",
 "tr": "Sayı isimleri: eşyanın fertlerinin miktarı için konulmuş olanlardır."},
 "tokens": [
  W("أَسْمَاءُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the nouns of» — the mubtada.", "«isimleri» — mübtedâ."),
  W("الْعَدَدِ", "adad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«number».", "«sayı».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.", "«is coined».", "«konulmuş»."),
  li_("لِكَمِّيَّةِ", "kammiyya", "noun", ["idafa-definiteness"], "كَمِّيَّةِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«for the quantity of».", "«miktarı için».", "كَمِّيَّةِ"),
  W("آحَادِ", "aahad", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ — جَمْعُ أَحَدٍ.", "«the units of».", "«fertlerinin»."),
  W("الْأَشْيَاءِ", "shay", "noun", ["idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِأَجْلِ ال.", "«things».", "«eşyanın».", punct="."),
 ]})

# ----------- s2 (RESTORED): the twelve roots
S.append({"id": "s2", "translation": {
 "en": "And its roots are twelve words: from one to ten, and a hundred and a thousand." + R_EN,
 "tr": "Asılları on iki kelimedir: birden ona kadar, yüz ve bin." + R_TR},
 "tokens": [
  atf_wa("وَأُصُولُهَا", "asl", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "أُصُولُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its roots» — the mubtada.", "«ve asılları» — mübtedâ.", "أُصُولُ", extra_segs=[seg("أُصُولُ", "asl", "noun"), pr3fs()]),
  W("اثْنَتَا", "ithnan", "noun", ["mubtada-khabar", MR, "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — الْجُزْءُ الْأَوَّلُ مُعْرَبٌ إِعْرَابَ الْمُثَنَّى.", "«twelve (f.)» — the khabar; the first part declines like a dual.", "«on iki» — haber; birinci cüz' tesniye gibi mu'reb."),
  W("عَشْرَةَ", "ashara", "noun", [MR], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî."),
  W("كَلِمَةً", "kalima", "noun", ["tamyiz", TM], "تَمْيِيزٌ مَنْصُوبٌ مُفْرَدٌ — مُمَيِّزُ الْأَحَدَ عَشَرَ إِلَى التِّسْعَةِ وَالتِّسْعِينَ.", "«words» — the singular tamyīz of eleven to ninety-nine.", "«kelime» — on birden doksan dokuza müfred temyîz.", punct=":"),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("وَاحِدٍ", "wahid", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«one».", "«bir»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e kadar»."),
  cited("عَشَرَةٍ", "ashara", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«ten».", "«on».", punct="،"),
  cited_wa("وَمِائَةٍ", "mia", "noun", [], "مِائَةٍ مَعْطُوفٌ.", "«and a hundred».", "«ve yüz».", "مِائَةٍ"),
  cited_wa("وَأَلْفٍ", "alf", "noun", [], "أَلْفٍ مَعْطُوفٌ.", "«and a thousand».", "«ve bin».", "أَلْفٍ", punct="."),
 ]})

# ----------- s3 (RESTORED): one and two
S.append({"id": "s3", "translation": {
 "en": "So one and two: وَاحِدٌ and وَاحِدَةٌ، اثْنَانِ and اثْنَتَانِ, agreeing with the counted noun — and they are not followed by a tamyīz, for رَجُلٌ and رَجُلَانِ say it already." + R_EN,
 "tr": "Bir ve iki: وَاحِدٌ ve وَاحِدَةٌ، اثْنَانِ ve اثْنَتَانِ, ma'dûda uyar — ve onlara temyîz getirilmez; çünkü رَجُلٌ ve رَجُلَانِ bunu zaten söyler." + R_TR},
 "tokens": [
  W("فَالْوَاحِدُ", "wahid", "noun", ["mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْوَاحِدُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so one» — the mubtada.", "«bir» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الْوَاحِدُ", "wahid", "noun")]),
  atf_wa("وَالِاثْنَانِ", "ithnan", "noun", ["al-muthanna"], "الِاثْنَانِ مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ.", "«and two».", "«ve iki».", "الِاثْنَانِ", punct=":"),
  cited("وَاحِدٌ", "wahid", "noun", ["mubtada-khabar"], "خَبَرٌ — لِلْمُذَكَّرِ.", "«wāḥid» — for the masculine.", "«vâhid» — müzekker için."),
  cited_wa("وَوَاحِدَةٌ", "wahid", "noun", ["al-muannath-wa-alamatuh"], "وَاحِدَةٌ مَعْطُوفٌ — لِلْمُؤَنَّثِ.", "«and wāḥida» — for the feminine.", "«ve vâhide» — müennes için.", "وَاحِدَةٌ", punct="،"),
  cited_wa("وَاثْنَانِ", "ithnan", "noun", ["al-muthanna"], "اثْنَانِ مَعْطُوفٌ.", "«and ithnāni».", "«ve isnâni».", "اثْنَانِ"),
  cited_wa("وَاثْنَتَانِ", "ithnan", "noun", ["al-muthanna", "al-muannath-wa-alamatuh"], "اثْنَتَانِ مَعْطُوفٌ — لِلْمُؤَنَّثِ.", "«and ithnatāni».", "«ve isnetâni».", "اثْنَتَانِ", punct="،"),
  W("مُطَابِقَانِ", "mutabiq", "noun", ["hal", "al-muthanna", "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ؟ — بَلْ خَبَرٌ ثَانٍ مَرْفُوعٌ بِالْأَلِفِ: يُطَابِقَانِ الْمَعْدُودَ.", "«agreeing» — a second khabar: they agree with the counted noun.", "«uyar» — ikinci haber: ma'dûda uyarlar."),
  li_("لِلْمَعْدُودِ", "madud", "noun", ["ism-maful"], "الْمَعْدُودِ مَجْرُورٌ.", "«with the counted noun».", "«ma'dûda».", "الْمَعْدُودِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمَعْدُودِ", "madud", "noun")]),
  atf_wa("وَلَا", "la", "part", ["la-nafiya"], "لَا حَرْفُ نَفْيٍ.", "«and not».", "«ve -mez».", "لَا"),
  W("يُمَيَّزَانِ", "mayyaza", "verb", ["naib-al-fail", "afal-khamsa", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ.", "«are they given a tamyīz».", "«temyîz getirilmez».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  cited("رَجُلًا", "rajul", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ — الْمِثَالُ.", "«a man» — the ism of أَنَّ.", "«racül» — enne'nin ismi."),
  cited_wa("وَرَجُلَيْنِ", "rajul", "noun", ["al-muthanna"], "رَجُلَيْنِ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ.", "«and two men».", "«ve racüleyn».", "رَجُلَيْنِ"),
  W("يُفِيدَانِ", "afada", "verb", ["inna-wa-akhawatuha", "fail", "afal-khamsa", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«convey» — the khabar of أَنَّ.", "«ifade eder» — enne'nin haberi."),
  W("الْمَعْنَى", "mana", "noun", ["maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«the meaning».", "«manayı».", punct="."),
 ]})

# ----------- s4 (RESTORED): three to ten
S.append({"id": "s4", "translation": {
 "en": "And from three to ten: with the tāʾ for the masculine — ثَلَاثَةٌ … عَشَرَةٌ — and without it for the feminine — ثَلَاثٌ … عَشْرٌ." + R_EN,
 "tr": "Üçten ona kadar: müzekker için tâ ile — ثَلَاثَةٌ … عَشَرَةٌ — müennes için tâsız — ثَلَاثٌ … عَشْرٌ." + R_TR},
 "tokens": [
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ.", "«and from».", "«ve -den».", "مِنْ"),
  cited("ثَلَاثَةٍ", "thalatha", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«three».", "«üç»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e kadar»."),
  cited("عَشَرَةٍ", "ashara", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«ten».", "«on».", punct=":"),
  W("بِالتَّاءِ", "ta-letter", "noun", ["huruf-jarr", "al-muannath-wa-alamatuh"], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّاءِ مَجْرُورٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ بِالتَّاءِ.", "«with the tāʾ» — the khabar of an understood «it is».", "«tâ ile» — takdir edilen «o»nun haberi.", segments=[seg("بِ", "bi", "prep"), seg("التَّاءِ", "ta-letter", "noun")]),
  li_("لِلْمُذَكَّرِ", "mudhakkar", "noun", [], "الْمُذَكَّرِ مَجْرُورٌ — عَكْسُ الْقِيَاسِ.", "«for the masculine» — against the ordinary rule.", "«müzekker için» — kıyâsın tersine.", "الْمُذَكَّرِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمُذَكَّرِ", "mudhakkar", "noun")]),
  *nums([("ثَلَاثَةٌ", "thalatha", "three", "üç"), ("أَرْبَعَةٌ", "arbaa", "four", "dört"), ("خَمْسَةٌ", "khamsa", "five", "beş"), ("سِتَّةٌ", "sitta", "six", "altı"), ("سَبْعَةٌ", "saba-seven", "seven", "yedi"), ("ثَمَانِيَةٌ", "thamaniya", "eight", "sekiz"), ("تِسْعَةٌ", "tisa", "nine", "dokuz"), ("عَشَرَةٌ", "ashara", "ten", "on")], first_ar="بَدَلٌ مِنْ بِالتَّاءِ أَوْ خَبَرٌ آخَرُ.", last_punct="،"),
  atf_wa("وَبِدُونِهَا", "duna", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَدُونِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and without it».", "«ve onsuz».", "دُونِ", extra_segs=[seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun"), pr3fs()]),
  li_("لِلْمُؤَنَّثِ", "muannath", "noun", [], "الْمُؤَنَّثِ مَجْرُورٌ.", "«for the feminine».", "«müennes için».", "الْمُؤَنَّثِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمُؤَنَّثِ", "muannath", "noun")]),
  *nums([("ثَلَاثٌ", "thalath", "three (f.)", "üç"), ("أَرْبَعٌ", "arba", "four (f.)", "dört"), ("خَمْسٌ", "khams", "five (f.)", "beş"), ("سِتٌّ", "sitt", "six (f.)", "altı"), ("سَبْعٌ", "sab-seven", "seven (f.)", "yedi"), ("ثَمَانٍ", "thamani", "eight (f.)", "sekiz"), ("تِسْعٌ", "tis", "nine (f.)", "dokuz"), ("عَشْرٌ", "ashr", "ten (f.)", "on")], first_ar="فِي مَحَلِّ جَرٍّ.", last_punct="."),
 ]})

# ----------- s5 (RESTORED): eleven to nineteen
S.append({"id": "s5", "translation": {
 "en": "And from eleven to nineteen the two parts are compounded and built on the fatḥ: أَحَدَ عَشَرَ، اثْنَا عَشَرَ، ثَلَاثَةَ عَشَرَ … for the masculine, and إِحْدَى عَشْرَةَ، اثْنَتَا عَشْرَةَ، ثَلَاثَ عَشْرَةَ … for the feminine." + R_EN,
 "tr": "On birden on dokuza kadar iki cüz' birleşir ve feth üzere mebnî olur: müzekkerde أَحَدَ عَشَرَ، اثْنَا عَشَرَ، ثَلَاثَةَ عَشَرَ …, müennesde إِحْدَى عَشْرَةَ، اثْنَتَا عَشْرَةَ، ثَلَاثَ عَشْرَةَ …" + R_TR},
 "tokens": [
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ.", "«and from».", "«ve -den».", "مِنْ"),
  cited("أَحَدَ", "ahad", "noun", [MR], "فِي مَحَلِّ جَرٍّ — الْجُزْءُ الْأَوَّلُ.", "«eleven».", "«on bir»."),
  W("عَشَرَ", "ashar", "noun", [MR], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part.", "— ikinci cüz'."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e kadar»."),
  cited("تِسْعَةَ", "tisa", "noun", [MR], "فِي مَحَلِّ جَرٍّ.", "«nineteen».", "«on dokuz»."),
  W("عَشَرَ", "ashar", "noun", [MR], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part.", "— ikinci cüz'."),
  W("يُرَكَّبُ", "rakkaba", "verb", ["naib-al-fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«are compounded».", "«birleştirilir»."),
  W("الْجُزْءَانِ", "juz", "noun", ["naib-al-fail", "al-muthanna"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالْأَلِفِ.", "«the two parts».", "«iki cüz'»."),
  atf_wa("وَيُبْنَيَانِ", "bana", "verb", ["naib-al-fail", "afal-khamsa", "naqis-verbs"], "يُبْنَيَانِ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ.", "«and are built».", "«ve mebnî kılınır».", "يُبْنَيَانِ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْفَتْحِ", "fath", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the fatḥ».", "«feth».", punct=":"),
  cited("أَحَدَ", "ahad", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«eleven».", "«on bir»."),
  W("عَشَرَ", "ashar", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî.", punct="،"),
  cited("اثْنَا", "ithnan", "noun", [MR, "al-muthanna"], "مُعْرَبٌ بِالْأَلِفِ — الْمُسْتَثْنَى.", "«twelve» — the exception, declining.", "«on iki» — istisnâ, mu'reb."),
  W("عَشَرَ", "ashar", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî.", punct="،"),
  cited("ثَلَاثَةَ", "thalatha", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«thirteen».", "«on üç»."),
  W("عَشَرَ", "ashar", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«up to».", "«-e kadar»."),
  cited("تِسْعَةَ", "tisa", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«nineteen».", "«on dokuz»."),
  W("عَشَرَ", "ashar", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî."),
  li_("لِلْمُذَكَّرِ", "mudhakkar", "noun", [], "الْمُذَكَّرِ مَجْرُورٌ.", "«for the masculine».", "«müzekker için».", "الْمُذَكَّرِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمُذَكَّرِ", "mudhakkar", "noun")]),
  cited_wa("وَإِحْدَى", "ihda", "noun", [MR], "إِحْدَى مَعْطُوفٌ — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ.", "«and eleven (f.)».", "«ve on bir (müennes)».", "إِحْدَى"),
  W("عَشْرَةَ", "ashara", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî.", punct="،"),
  cited("اثْنَتَا", "ithnan", "noun", [MR, "al-muthanna"], "مُعْرَبٌ بِالْأَلِفِ.", "«twelve (f.)».", "«on iki (müennes)»."),
  W("عَشْرَةَ", "ashara", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî.", punct="،"),
  cited("ثَلَاثَ", "thalath", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«thirteen (f.)».", "«on üç (müennes)»."),
  W("عَشْرَةَ", "ashara", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«up to».", "«-e kadar»."),
  cited("تِسْعَ", "tis", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "«nineteen (f.)».", "«on dokuz (müennes)»."),
  W("عَشْرَةَ", "ashara", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî."),
  li_("لِلْمُؤَنَّثِ", "muannath", "noun", [], "الْمُؤَنَّثِ مَجْرُورٌ.", "«for the feminine».", "«müennes için».", "الْمُؤَنَّثِ", punct=".", segs=[seg("لِ", "li", "prep"), seg("الْمُؤَنَّثِ", "muannath", "noun")]),
 ]})

# ----------- s6 (RESTORED): decades, hundreds, thousands, the joining
S.append({"id": "s6", "translation": {
 "en": "And عِشْرُونَ up to تِسْعُونَ are alike for both genders, and so are مِائَةٌ and أَلْفٌ; the units are joined to the decades — أَحَدٌ وَعِشْرُونَ، إِحْدَى وَعِشْرُونَ — and what exceeds a hundred or a thousand is joined to it — مِائَةٌ وَوَاحِدٌ." + R_EN,
 "tr": "عِشْرُونَ'den تِسْعُونَ'ye kadar iki cins için birdir; مِائَةٌ ve أَلْفٌ de öyle; birler onluklara atfedilir — أَحَدٌ وَعِشْرُونَ، إِحْدَى وَعِشْرُونَ — yüzü ya da bini aşan ona atfedilir — مِائَةٌ وَوَاحِدٌ." + R_TR},
 "tokens": [
  cited_wa("وَعِشْرُونَ", "ishrun", "noun", ["mubtada-khabar", "jam-mudhakkar-salim"], "عِشْرُونَ مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ.", "«and twenty» — the mubtada.", "«ve yirmi» — mübtedâ.", "عِشْرُونَ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«up to».", "«-e kadar»."),
  cited("تِسْعِينَ", "tisun", "noun", ["huruf-jarr", "jam-mudhakkar-salim"], "فِي مَحَلِّ جَرٍّ — مَجْرُورٌ بِالْيَاءِ.", "«ninety».", "«doksan»."),
  W("سَوَاءٌ", "sawa", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — أَيْ: مُسْتَوِيَةٌ.", "«are alike» — the khabar.", "«birdir» — haber."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-de»."),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the masculine».", "«müzekkerde»."),
  atf_wa("وَالْمُؤَنَّثِ", "muannath", "noun", [], "الْمُؤَنَّثِ مَعْطُوفٌ.", "«and the feminine».", "«ve müennesde».", "الْمُؤَنَّثِ", punct="،"),
  atf_wa("وَكَذٰلِكَ", "dhalika", "pron", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh", "asma-al-ishara"], "الْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ فِي مَحَلِّ جَرٍّ؛ خَبَرٌ مُقَدَّمٌ.", "«and likewise».", "«ve böyledir».", "ذٰلِكَ", extra_segs=[seg("كَ", "ka", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  cited("مِائَةٌ", "mia", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ.", "«a hundred».", "«yüz»."),
  cited_wa("وَأَلْفٌ", "alf", "noun", [], "أَلْفٌ مَعْطُوفٌ.", "«and a thousand».", "«ve bin».", "أَلْفٌ", punct="؛"),
  atf_wa("وَتُعْطَفُ", "atafa", "verb", ["naib-al-fail"], "تُعْطَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and are joined».", "«ve atfedilir».", "تُعْطَفُ"),
  W("الْآحَادُ", "aahad", "noun", ["naib-al-fail", "jam-taksir"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«the units».", "«birler»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْعُقُودِ", "aqd", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِالْكَسْرَةِ — الْعِشْرُونَ وَأَخَوَاتُهَا.", "«the decades» — twenty and its sisters.", "«onluklara» — yirmi ve kardeşleri.", punct="،"),
  nahwu(),
  cited("أَحَدٌ", "ahad", "noun", [], "فِي مَحَلِّ جَرٍّ — الْمَعْطُوفُ عَلَيْهِ.", "«one».", "«bir»."),
  cited_wa("وَعِشْرُونَ", "ishrun", "noun", ["jam-mudhakkar-salim"], "عِشْرُونَ مَعْطُوفٌ.", "«and twenty» — twenty-one.", "«ve yirmi» — yirmi bir.", "عِشْرُونَ", punct="،"),
  cited("إِحْدَى", "ihda", "noun", ["al-muannath-wa-alamatuh"], "فِي مَحَلِّ جَرٍّ — لِلْمُؤَنَّثِ.", "«one (f.)».", "«bir (müennes)»."),
  cited_wa("وَعِشْرُونَ", "ishrun", "noun", ["jam-mudhakkar-salim"], "عِشْرُونَ مَعْطُوفٌ.", "«and twenty».", "«ve yirmi».", "عِشْرُونَ", punct="،"),
  atf_wa("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "naib-al-fail", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى الْآحَادُ فِي مَحَلِّ رَفْعٍ.", "«and what».", "«ve ... olan».", "مَا"),
  W("زَادَ", "zada", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«exceeds».", "«aşan»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«-i»."),
  cited("مِائَةٍ", "mia", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«a hundred».", "«yüzü»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("أَلْفٍ", "alf", "noun", ["atf-nasaq"], "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«a thousand».", "«bini»."),
  W("يُعْطَفُ", "atafa", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«is joined».", "«atfedilir»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to it».", "«ona».", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  nahwu(),
  cited("مِائَةٌ", "mia", "noun", [], "فِي مَحَلِّ جَرٍّ.", "«a hundred».", "«yüz»."),
  cited_wa("وَوَاحِدٌ", "wahid", "noun", [], "وَاحِدٌ مَعْطُوفٌ — مِائَةٌ وَوَاحِدٌ.", "«and one» — a hundred and one.", "«ve bir» — yüz bir.", "وَاحِدٌ", punct="."),
 ]})

# ----------- s7 (RESTORED): the tamyiz
S.append({"id": "s7", "translation": {
 "en": "And the tamyīz of three to ten is a plural in jarr, of eleven to ninety-nine a singular in naṣb, and of a hundred and a thousand a singular in jarr." + R_EN,
 "tr": "Üçten ona kadarın temyîzi cemi mecrûr, on birden doksan dokuza kadarınki müfred mansûb, yüz ile bininki müfred mecrûrdur." + R_TR},
 "tokens": [
  atf_wa("وَمُمَيِّزُ", "mumayyiz", "noun", ["mubtada-khabar", "idafa-definiteness", TM], "مُمَيِّزُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the tamyīz of» — the mubtada.", "«ve temyîzi» — mübtedâ.", "مُمَيِّزُ"),
  cited("ثَلَاثَةٍ", "thalatha", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«three».", "«üçün»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e kadar»."),
  cited("عَشَرَةٍ", "ashara", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«ten».", "«onun»."),
  W("مَجْمُوعٌ", "majmu", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«a plural» — the khabar.", "«cemi» — haber."),
  W("مَجْرُورٌ", "majrur", "noun", ["naat-sifa", "ism-maful", TM], "صِفَةٌ مَرْفُوعَةٌ — ثَلَاثَةُ رِجَالٍ.", "«in jarr» — ثَلَاثَةُ رِجَالٍ.", "«mecrûr» — selâsetü ricâlin.", punct="،"),
  atf_wa("وَمُمَيِّزُ", "mumayyiz", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُمَيِّزُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«and the tamyīz of».", "«ve temyîzi».", "مُمَيِّزُ"),
  cited("أَحَدَ", "ahad", "noun", ["idafa-definiteness", MR], "فِي مَحَلِّ جَرٍّ.", "«eleven».", "«on birin»."),
  W("عَشَرَ", "ashar", "noun", [MR], "مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part, built.", "— ikinci cüz', mebnî."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e kadar»."),
  cited("تِسْعَةٍ", "tisa", "noun", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ.", "«nine».", "«dokuz»."),
  cited_wa("وَتِسْعِينَ", "tisun", "noun", ["jam-mudhakkar-salim"], "تِسْعِينَ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ.", "«and ninety».", "«ve doksanın».", "تِسْعِينَ"),
  W("مُفْرَدٌ", "mufrad", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a singular».", "«müfred»."),
  W("مَنْصُوبٌ", "mansub", "noun", ["naat-sifa", TM], "صِفَةٌ مَرْفُوعَةٌ — أَحَدَ عَشَرَ رَجُلًا.", "«in naṣb» — أَحَدَ عَشَرَ رَجُلًا.", "«mansûb» — ehade aşera racülen.", punct="،"),
  atf_wa("وَمُمَيِّزُ", "mumayyiz", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُمَيِّزُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«and the tamyīz of».", "«ve temyîzi».", "مُمَيِّزُ"),
  cited("مِائَةٍ", "mia", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ.", "«a hundred».", "«yüzün»."),
  cited_wa("وَأَلْفٍ", "alf", "noun", [], "أَلْفٍ مَعْطُوفٌ.", "«and a thousand».", "«ve binin».", "أَلْفٍ"),
  W("مُفْرَدٌ", "mufrad", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a singular».", "«müfred»."),
  W("مَجْرُورٌ", "majrur", "noun", ["naat-sifa", TM], "صِفَةٌ مَرْفُوعَةٌ — مِائَةُ رَجُلٍ.", "«in jarr» — مِائَةُ رَجُلٍ.", "«mecrûr» — mietü racülin.", punct="."),
 ]})

# ----------- s8 (RESTORED): the ordinals
S.append({"id": "s8", "translation": {
 "en": "And from the singular is derived, for making the number: ثَانٍ، ثَالِثٌ، رَابِعٌ، خَامِسٌ، سَادِسٌ، سَابِعٌ، ثَامِنٌ، تَاسِعٌ، عَاشِرٌ for the masculine, and with the tāʾ for the feminine — not below two nor above ten." + R_EN,
 "tr": "Sayıyı yapan manasında müfredden şunlar türetilir: müzekkerde ثَانٍ، ثَالِثٌ، رَابِعٌ، خَامِسٌ، سَادِسٌ، سَابِعٌ، ثَامِنٌ، تَاسِعٌ، عَاشِرٌ, müennesde tâ ile — ikinin altında ve onun üstünde değil." + R_TR},
 "tokens": [
  atf_wa("وَيُشْتَقُّ", "ishtaqqa", "verb", ["naib-al-fail", "form-viii-verbs", "doubled-verbs"], "يُشْتَقُّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is derived».", "«ve türetilir».", "يُشْتَقُّ"),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الْمُفْرَدِ", "mufrad", "noun", ["huruf-jarr"], "مَجْرُورٌ — ثَلَاثَةٌ وَأَخَوَاتُهَا.", "«the singular» — three and its sisters.", "«müfredden» — üç ve kardeşleri."),
  li_("لِلتَّصْيِيرِ", "tasyir", "noun", ["lam-taleel", "masdar", "form-ii-verbs"], "التَّصْيِيرِ مَجْرُورٌ — جَعْلُ النَّاقِصِ تَامًّا.", "«for the making» — making the lesser number the greater.", "«tasyîr için» — eksik sayıyı tam yapma.", "التَّصْيِيرِ", punct=":"),
  *nums([("ثَانٍ", "thani", "second", "ikinci"), ("ثَالِثٌ", "thalith", "third", "üçüncü"), ("رَابِعٌ", "rabi-fourth", "fourth", "dördüncü"), ("خَامِسٌ", "khamis", "fifth", "beşinci"), ("سَادِسٌ", "sadis", "sixth", "altıncı"), ("سَابِعٌ", "sabi", "seventh", "yedinci"), ("ثَامِنٌ", "thamin-eighth", "eighth", "sekizinci"), ("تَاسِعٌ", "tasi", "ninth", "dokuzuncu"), ("عَاشِرٌ", "ashir-tenth", "tenth", "onuncu")], first_ar="نَائِبُ فَاعِلِ يُشْتَقُّ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", last_punct=None),
  li_("لِلْمُذَكَّرِ", "mudhakkar", "noun", [], "الْمُذَكَّرِ مَجْرُورٌ.", "«for the masculine».", "«müzekker için».", "الْمُذَكَّرِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمُذَكَّرِ", "mudhakkar", "noun")]),
  atf_wa("وَبِالتَّاءِ", "ta-letter", "noun", ["huruf-jarr", "al-muannath-wa-alamatuh"], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّاءِ مَجْرُورٌ.", "«and with the tāʾ».", "«ve tâ ile».", "التَّاءِ", extra_segs=[seg("بِ", "bi", "prep"), seg("التَّاءِ", "ta-letter", "noun")]),
  li_("لِلْمُؤَنَّثِ", "muannath", "noun", [], "الْمُؤَنَّثِ مَجْرُورٌ.", "«for the feminine».", "«müennes için».", "الْمُؤَنَّثِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمُؤَنَّثِ", "muannath", "noun")]),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«... değil»."),
  W("دُونَ", "duna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«below».", "«altında»."),
  cited("اثْنَيْنِ", "ithnan", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two».", "«ikinin»."),
  atf_wa("وَلَا", "la", "part", ["la-nafiya"], "لَا حَرْفُ نَفْيٍ.", "«nor».", "«ve ... değil».", "لَا"),
  W("فَوْقَ", "fawqa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«above».", "«üstünde»."),
  cited("عَشَرَةٍ", "ashara", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ten».", "«onun».", punct="."),
 ]})

def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "kammiyya": need("kammiyya", "كَمِّيَّة", None, "noun", "quantity, how-many-ness (the abstract noun of كَمْ)", "kemmiyet, nicelik (kem'in masdar-ı ca'lîsi)", 5),
 "madud": need("madud", "مَعْدُود", "ع د د", "noun", "the counted noun (ism maf'ul of عَدَّ)", "ma'dûd, sayılan isim (adde'nin ism-i mef'ûlü)", 3),
 "mayyaza": need("mayyaza", "مَيَّزَ", "م ي ز", "verb", "to distinguish, to give a tamyīz (Form II)", "ayırmak, temyîz vermek (tef'îl)", 4),
 "afada": need("afada", "أَفَادَ", "ف ي د", "verb", "to convey, to give (a meaning), to benefit (Form IV; hollow)", "ifade etmek, (mana) vermek, fayda vermek (if'âl; ecvef)", 3),
 "rakkaba": need("rakkaba", "رَكَّبَ", "ر ك ب", "verb", "to compound, to put together (Form II)", "terkip etmek, birleştirmek (tef'îl)", 4),
 "sawa": need("sawa", "سَوَاء", "س و ي", "noun", "alike, equal", "eşit, bir", 3),
 "aqd": need("aqd", "عَقْد", "ع ق د", "noun", "a decade (twenty, thirty… — الْعُقُود); a knot, a contract", "onluk (yirmi, otuz… — ukûd); düğüm, akit", 4, plural="عُقُود"),
 "khams": need("khams", "خَمْس", "خ م س", "noun", "five (feminine form)", "beş (müennes şekli)", 2),
 "thamani": need("thamani", "ثَمَانٍ", "ث م ن", "noun", "eight (feminine form; a manqūṣ: ثَمَانِي)", "sekiz (müennes şekli; mankûs: semânî)", 3),
 "ishtaqqa": need("ishtaqqa", "اشْتَقَّ", "ش ق ق", "verb", "to derive (Form VIII; doubled)", "türetmek (iftiâl; muzâaf)", 4),
 "tasyir": need("tasyir", "تَصْيِير", "ص ي ر", "noun", "making (one thing into another) — the sense in which ثَالِثٌ «makes two three» (masdar of Form II صَيَّرَ)", "tasyîr, bir şeyi başka bir şey kılma — سَالِثٌ'ün «ikiyi üç yapması» (sayyere'nin masdarı)", 5),
}
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
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "mayyaza", _sg.derived(_sg.B2, _sg.W2, "ُ", "مَيَّز", "مَيِّز", "مَيِّز", "تَمْيِيز", "مُمَيِّز", "مُمَيَّز", "مُيِّزَ", "يُمَيَّزُ", "مَيَّزَ الشَّيْءَ يُمَيِّزُهُ: فَصَلَهُ عَنْ غَيْرِهِ — مِنَ الْبَابِ الثَّانِي."))
put_morph(mo, "rakkaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "رَكَّب", "رَكِّب", "رَكِّب", "تَرْكِيب", "مُرَكِّب", "مُرَكَّب", "رُكِّبَ", "يُرَكَّبُ", "رَكَّبَ الشَّيْءَ يُرَكِّبُهُ: ضَمَّ بَعْضَهُ إِلَى بَعْضٍ — مِنَ الْبَابِ الثَّانِي."))
put_morph(mo, "afada", _sg.derived_hollow(_sg.B4, _sg.W4, "ِ", "أَفَاد", "أَفَدْ", "فِيد", "فِد", "أَفِيد", "أَفِد", "إِفَادَة", "مُفِيد", "مُفَاد", "أُفِيدَ", "يُفَادُ", "أَفَادَ يُفِيدُ إِفَادَةً: أَعْطَى الْفَائِدَةَ — أَجْوَفُ يَائِيٌّ مِنْ بَابِ الْإِفْعَالِ."))
put_morph(mo, "ishtaqqa", find_morph("ishtaqqa"))   # an identity copy: the key is owned elsewhere
report(10, S, GLOSS_ADD, (NOTE,))
