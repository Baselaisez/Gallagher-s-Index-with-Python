# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 7: THE KINAYAT AND THE BUILT ADVERBS. كَمْ and كَذَا for number, كَيْتَ and ذَيْتَ for speech; كَمْ as a vague number
with the head of the sentence, interrogative (its tamyiz singular in nasb) and predicative (singular or plural in jarr, مِنْ may enter);
its three mahalls as the notebook works them (commentary); كَأَيِّنْ; then the built adverbs: إِذَا for the future with the condition
(and for surprise), إِذْ for the past annexed to both kinds of clause, أَيْنَ and أَنَّى for place, مَتَى for time, أَيَّانَ for the great
and the future, كَيْفَ for the state, مُذْ and مُنْذُ for the start or the whole of a span.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~195-202 of the transcription.

  VERBATIM from the notebook's Arabic: every example (the notebook's own and the ayas it cites: al-A'raf 7:4 without its opening waw as the
  notebook cites it, Al 'Imran 3:146, al-Anfal 8:26, al-An'am 6:74, Al 'Imran 3:37, al-Dhariyat 51:12).
  RESTORED (the notebook carries the ruling only in Turkish; the received matn of the Kafiya is written and marked): s1, s3, s4, s5, s6, s10, s11, s12, s13, s14, s15, s16.
  COMMENTARY (the notebook's question and answer on كَمْ's mahall): s7, s8, s9 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch7.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-kinayat-wal-zuruf-al-mabniyya"
K3 = "al-mabni-wal-mudmar"
KN = "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf"
TITLE = {"ar": "الْكِنَايَاتُ وَالظُّرُوفُ الْمَبْنِيَّةُ", "en": "The kināyāt and the built adverbs", "tr": "Kinâyeler ve mebnî zarflar"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
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
def fi_mahall(kase, k_ar, k_en, k_tr, first=True, punct=None):
    return [W("وَفِي" if not first else "فِي", "fi", "prep", ["huruf-jarr"] + (["atf-nasaq"] if not first else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if not first else "") + "فِي حَرْفُ جَرٍّ.", ("«and in» " if not first else "«in»"), ("«ve -de»" if not first else "«-de»"), segments=([seg("وَ", "wa", "conj")] if not first else []) + [seg("فِي", "fi", "prep")]),
            W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallinde»."),
            W(k_ar, kase, "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", k_en, k_tr, punct=punct)]
def kam(full="كَمْ", tags=(), ar="كَمْ اسْمٌ مَبْنِيٌّ عَلَى السُّكُونِ.", en="«how many» — كَمْ.", tr="«kaç / nice» — kem.", punct=None, segments=None, wa=False):
    if wa: return cited_wa("وَكَمْ", "kam", "pron", list(tags), ar, en, tr, "كَمْ", punct=punct)
    return cited(full, "kam", "pron", list(tags), ar, en, tr, punct=punct, segments=segments)

# ----------- s1 (RESTORED): the kinayat
S.append({"id": "s1", "translation": {
 "en": "The kināyāt: كَمْ and كَذَا for number, كَيْتَ and ذَيْتَ for speech." + R_EN,
 "tr": "Kinâyeler: sayı için كَمْ ve كَذَا, söz için كَيْتَ ve ذَيْتَ." + R_TR},
 "tokens": [
  W("الْكِنَايَاتُ", "kinaya", "noun", ["mubtada-khabar", "jam-muannath-salim", KN], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — أَلْفَاظٌ يُعَبَّرُ بِهَا عَنْ مُعَيَّنٍ لِغَرَضٍ.", "«the kināyāt» — words that stand in for a definite thing on purpose.", "«kinâyeler» — bir garaz için muayyen bir şeyin yerini tutan lafızlar.", punct=":"),
  cited("كَمْ", "kam", "pron", ["mubtada-khabar", KN], "فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«how many» — the khabar.", "«kaç / nice» — haber."),
  cited_wa("وَكَذَا", "kadha", "pron", [KN], "كَذَا مَعْطُوفٌ.", "«and so-many».", "«ve şu kadar».", "كَذَا"),
  li_("لِلْعَدَدِ", "adad", "noun", [], "الْعَدَدِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for number».", "«sayı için».", "الْعَدَدِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْعَدَدِ", "adad", "noun")]),
  cited_wa("وَكَيْتَ", "kayta", "pron", [KN], "كَيْتَ مَعْطُوفٌ — مَبْنِيٌّ عَلَى الْفَتْحِ.", "«and such-and-such».", "«ve şöyle».", "كَيْتَ"),
  cited_wa("وَذَيْتَ", "dhayta", "pron", [KN], "ذَيْتَ مَعْطُوفٌ.", "«and so-and-so».", "«ve böyle».", "ذَيْتَ"),
  li_("لِلْحَدِيثِ", "hadith", "noun", [], "الْحَدِيثِ مَجْرُورٌ بِالْكَسْرَةِ — أَيْ: لِلْكَلَامِ الْمَحْكِيِّ.", "«for speech» — for reported talk.", "«söz için» — nakledilen söz için.", "الْحَدِيثِ", punct=".", segs=[seg("لِ", "li", "prep"), seg("الْحَدِيثِ", "hadith", "noun")]),
 ]})

# ----------- s2 (the notebook's examples)
S.append({"id": "s2", "translation": {
 "en": "As in «I have so-many dirhams», and «So-and-so said such-and-such, and so-and-so said so-and-so».",
 "tr": "«Bende şu kadar dirhem var» ve «Falan şöyle şöyle dedi, falan böyle böyle dedi» gibi."},
 "tokens": [
  nahwu(),
  W("عِنْدِي", "inda", "noun", ["idafa-definiteness", "maful-fih", "khabar-al-mubtada-wa-ahkamuh"], "لَفْظٌ مَحْكِيٌّ؛ وَفِي الْمِثَالِ ظَرْفٌ خَبَرٌ مُقَدَّمٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«I have» — the fronted khabar.", "«bende var» — öne alınmış haber.", segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  cited("كَذَا", "kadha", "pron", ["mubtada-khabar", KN], "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ — كِنَايَةٌ عَنْ عَدَدٍ.", "«so-many» — the mubtada, a stand-in for a number.", "«şu kadar» — mübtedâ, bir sayının kinâyesi."),
  W("دِرْهَمًا", "dirham", "noun", ["tamyiz", KN], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«dirhams» — the tamyīz.", "«dirhem» — temyîz.", punct="،"),
  atf_wa("وَقَالَ", "qala", "verb", ["fail", "hollow-verbs"], "قَالَ فِعْلٌ مَاضٍ.", "«and said».", "«ve dedi».", "قَالَ"),
  W("فُلَانٌ", "fulan", "noun", ["fail", KN], "فَاعِلٌ مَرْفُوعٌ — كِنَايَةٌ عَنْ عَلَمٍ.", "«so-and-so» — the doer, a stand-in for a name.", "«falan» — fâil, bir ismin kinâyesi."),
  cited("كَيْتَ", "kayta", "pron", ["maful-bihi", KN], "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — كِنَايَةٌ عَنِ الْحَدِيثِ.", "«such-and-such» — the object, a stand-in for the words said.", "«şöyle» — mef'ûl, sözün kinâyesi."),
  cited("كَيْتَ", "kayta", "pron", ["tawkid", KN], "تَوْكِيدٌ لَفْظِيٌّ.", "«such-and-such» — repeated for emphasis.", "«şöyle» — lafzî te'kîd.", punct="،"),
  atf_wa("وَقَالَ", "qala", "verb", ["fail", "hollow-verbs"], "قَالَ فِعْلٌ مَاضٍ.", "«and said».", "«ve dedi».", "قَالَ"),
  W("فُلَانٌ", "fulan", "noun", ["fail", KN], "فَاعِلٌ مَرْفُوعٌ.", "«so-and-so».", "«falan»."),
  cited("ذَيْتَ", "dhayta", "pron", ["maful-bihi", KN], "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«so-and-so» — the object.", "«böyle» — mef'ûl."),
  cited("ذَيْتَ", "dhayta", "pron", ["tawkid", KN], "تَوْكِيدٌ لَفْظِيٌّ.", "«so-and-so» — repeated.", "«böyle» — tekrar.", punct="."),
 ]})

# ----------- s3 (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "So كَمْ is a noun for a vague number, and it has the head of the sentence." + R_EN,
 "tr": "كَمْ, mübhem bir sayının ismidir ve sadr-ı kelâm ona âittir." + R_TR},
 "tokens": [
  W("فَكَمْ", "kam", "pron", ["mubtada-khabar", KN], "الْفَاءُ لِلتَّفْصِيلِ، وَكَمْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«so كَمْ» — the mubtada.", "«kem ise» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("كَمْ", "kam", "pron")]),
  W("اسْمٌ", "ism", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«is a noun» — the khabar.", "«bir isimdir» — haber."),
  li_("لِعَدَدٍ", "adad", "noun", ["naat-sifa"], "عَدَدٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«for a number».", "«bir sayı için».", "عَدَدٍ"),
  W("مُبْهَمٍ", "mubham", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ لِعَدَدٍ مَجْرُورَةٌ.", "«vague» — its naʿt.", "«mübhem» — sıfatı.", punct="،"),
  atf_wa("وَلَهَا", "li", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and to it belongs» — the fronted khabar.", "«ve ona âittir» — öne alınmış haber.", "لَ", extra_segs=[seg("لَ", "li", "prep"), pr3fs()]),
  W("صَدْرُ", "sadr", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the head of» — the delayed mubtada: كَمْ opens its sentence.", "«sadrı» — mübtedâ: kem cümlesinin başında durur."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«kelâmın».", punct="."),
 ]})

# ----------- s4 (RESTORED + examples)
S.append({"id": "s4", "translation": {
 "en": "And it is interrogative, so its tamyīz is singular in naṣb — as in «how many men are with you?» and «how many dirhams is your wealth?»" + R_EN,
 "tr": "İstifhâmiyye olur, temyîzi müfred mansûbdur — «yanında kaç adam var?» ve «malın kaç dirhem?» gibi." + R_TR},
 "tokens": [
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هِيَ"),
  W("اسْتِفْهَامِيَّةٌ", "istifhamiyya", "noun", ["mubtada-khabar", "ism-mansub"], "خَبَرٌ مَرْفُوعٌ.", "«interrogative» — the khabar.", "«istifhâmiyye» — haber."),
  W("فَيَكُونُ", "kana", "verb", ["kana-wa-akhawatuha"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«so is».", "«öyleyse olur».", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  W("مُمَيِّزُهَا", "mumayyiz", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "tamyiz"], "اسْمُ يَكُونُ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its tamyīz» — the ism of kāna.", "«temyîzi» — kâne'nin ismi.", segments=[seg("مُمَيِّزُ", "mumayyiz", "noun"), pr3fs()]),
  W("مُفْرَدًا", "mufrad", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«singular» — the khabar.", "«müfred» — haber."),
  W("مَنْصُوبًا", "mansub", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ لِمُفْرَدًا مَنْصُوبَةٌ.", "«in naṣb».", "«mansûb».", punct="،"),
  nahwu(),
  kam(tags=["mubtada-khabar", KN], ar="فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — اسْتِفْهَامِيَّةٌ.", en="«how many» — the mubtada.", tr="«kaç» — mübtedâ."),
  W("رَجُلًا", "rajul", "noun", ["tamyiz", KN], "تَمْيِيزُ كَمْ مَنْصُوبٌ بِالْفَتْحَةِ — مُفْرَدٌ.", "«men» — the tamyīz, singular in naṣb.", "«adam» — temyîz, müfred mansûb."),
  W("عِنْدَكَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "mubtada-khabar"], "ظَرْفٌ مَنْصُوبٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«with you» — the khabar.", "«yanında» — haber.", punct="؟", segments=[seg("عِنْدَ", "inda", "noun"), pr2ms()]),
  kam(wa=True, tags=["mubtada-khabar", KN], ar="كَمْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", en="«and how many».", tr="«ve kaç»."),
  W("دِرْهَمًا", "dirham", "noun", ["tamyiz", KN], "تَمْيِيزٌ مَنْصُوبٌ.", "«dirhams» — the tamyīz.", "«dirhem» — temyîz."),
  W("مَالُكَ", "mal", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«is your wealth» — the khabar.", "«malın» — haber.", punct="؟", segments=[seg("مَالُ", "mal", "noun"), pr2ms()]),
 ]})

# ----------- s5 (RESTORED + examples)
S.append({"id": "s5", "translation": {
 "en": "And predicative, so its tamyīz is singular or plural in jarr — as in «many a man is with you» and «many men are with you»." + R_EN,
 "tr": "Haberiyye olur, temyîzi müfred ya da cemi mecrûrdur — «yanında nice adam var» ve «yanında nice adamlar var» gibi." + R_TR},
 "tokens": [
  atf_wa("وَخَبَرِيَّةٌ", "khabariyya", "noun", ["mubtada-khabar", "ism-mansub"], "خَبَرِيَّةٌ مَعْطُوفٌ عَلَى اسْتِفْهَامِيَّةٌ مَرْفُوعٌ.", "«and predicative».", "«ve haberiyye».", "خَبَرِيَّةٌ"),
  W("فَيَكُونُ", "kana", "verb", ["kana-wa-akhawatuha"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«so is».", "«öyleyse olur».", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  W("مُمَيِّزُهَا", "mumayyiz", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَكُونُ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its tamyīz».", "«temyîzi».", segments=[seg("مُمَيِّزُ", "mumayyiz", "noun"), pr3fs()]),
  W("مُفْرَدًا", "mufrad", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«singular».", "«müfred»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَجْمُوعًا", "majmu", "noun", ["atf-nasaq", "ism-maful"], "مَعْطُوفٌ مَنْصُوبٌ.", "«plural».", "«cemi»."),
  W("مَجْرُورًا", "majrur", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَنْصُوبَةٌ.", "«in jarr».", "«mecrûr».", punct="،"),
  nahwu(),
  kam(tags=["mubtada-khabar", KN], ar="فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — خَبَرِيَّةٌ بِمَعْنَى كَثِيرٍ.", en="«many a» — the mubtada, predicative.", tr="«nice» — mübtedâ, haberiyye."),
  W("رَجُلٍ", "rajul", "noun", ["tamyiz", KN, "idafa-definiteness"], "تَمْيِيزُ كَمْ مَجْرُورٌ بِالْكَسْرَةِ — مُفْرَدٌ؛ كَأَنَّهُ مُضَافٌ إِلَيْهِ.", "«man» — the tamyīz, singular in jarr as if annexed.", "«adam» — temyîz, müfred mecrûr; muzâfun ileyh gibi."),
  W("عِنْدَكَ", "inda", "noun", ["maful-fih", "mubtada-khabar"], "ظَرْفٌ خَبَرٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«with you».", "«yanında».", punct="،", segments=[seg("عِنْدَ", "inda", "noun"), pr2ms()]),
  kam(wa=True, tags=["mubtada-khabar", KN], ar="كَمْ مُبْتَدَأٌ.", en="«and many».", tr="«ve nice»."),
  W("رِجَالٍ", "rajul", "noun", ["tamyiz", KN, "jam-taksir"], "تَمْيِيزٌ مَجْرُورٌ — مَجْمُوعٌ.", "«men» — the tamyīz, plural in jarr.", "«adamlar» — temyîz, cemi mecrûr."),
  W("عِنْدَكَ", "inda", "noun", ["maful-fih", "mubtada-khabar"], "ظَرْفٌ خَبَرٌ.", "«with you».", "«yanında».", punct=".", segments=[seg("عِنْدَ", "inda", "noun"), pr2ms()]),
 ]})

# ----------- s6 (RESTORED + the aya as the notebook cites it)
S.append({"id": "s6", "translation": {
 "en": "And مِنْ may enter its tamyīz, as in «how many a town We have destroyed»." + R_EN,
 "tr": "Temyîzine مِنْ girebilir: «nice beldeyi helâk ettik» gibi." + R_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«and may».", "«ve bazen».", "قَدْ"),
  W("يَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«enter».", "«girer»."),
  W("مُمَيِّزَهَا", "mumayyiz", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its tamyīz» — the object.", "«temyîzine» — mef'ûl.", segments=[seg("مُمَيِّزَ", "mumayyiz", "noun"), pr3fs()]),
  cited("مِنْ", "min", "prep", ["fail", "huruf-jarr"], "فِي مَحَلِّ رَفْعٍ فَاعِلٌ — لَفْظُ مِنْ.", "«مِنْ» — the doer: the word itself.", "«min» — fâil: kelimenin kendisi.", punct="،"),
  nahwu(),
  kam(tags=["mubtada-khabar", KN, "al-iqtibas-wal-tadmin"], ar="فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — خَبَرِيَّةٌ (الْأَعْرَاف ٤، كَمَا أَوْرَدَهُ الدَّفْتَرُ دُونَ الْوَاوِ).", en="«how many a» — the mubtada (al-Aʿrāf 7:4, cited without its opening wāw as the notebook has it).", tr="«nice» — mübtedâ (A'râf 7:4; defterin naklettiği gibi baştaki vâvsız)."),
  W("مِنْ", "min", "prep", ["huruf-jarr", KN], "حَرْفُ جَرٍّ زَائِدٌ دَاخِلٌ عَلَى الْمُمَيِّزِ.", "«of» — the extra مِنْ before the tamyīz.", "«-den» — temyîzin önündeki zâid min."),
  W("قَرْيَةٍ", "qarya", "noun", ["huruf-jarr", "tamyiz", KN], "مَجْرُورٌ لَفْظًا بِمِنْ، تَمْيِيزُ كَمْ.", "«a town» — the tamyīz in jarr by مِنْ.", "«belde» — min ile mecrûr temyîz."),
  W("أَهْلَكْنَاهَا", "ahlaka", "verb", ["mubtada-khabar", "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ، وَالْجُمْلَةُ خَبَرُ كَمْ.", "«We destroyed it» — the khabar clause.", "«onu helâk ettik» — haber cümlesi.", punct=".", segments=[seg("أَهْلَكْ", "ahlaka", "verb"), pr1p(), pr3fs()]),
 ]})
for _t in S[5]["tokens"]:
    if _t["surface"]["full"] == "أَهْلَكْنَاهَا": _t["quoteAfter"] = "﴾"
S[5]["tokens"][5]["quoteBefore"] = "﴿"

# ----------- s7 (COMMENTARY): mahall nasb
S.append({"id": "s7", "translation": {
 "en": "And it stands in the place of naṣb when a verb after it governs it — as in «how many men did you beat?», «how many blows did you strike?», «how many days did you beat?»." + C_EN,
 "tr": "Sonrasındaki fiil onda amel ederse mahallen mansûbdur — «kaç adam dövdün?», «kaç vuruş vurdun?», «kaç gün dövdün?» gibi." + C_TR},
 "tokens": [
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  *fi_mahall("nasb", "نَصْبٍ", "«naṣb» — the khabar.", "«nasb» — haber."),
  W("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ince»."),
  W("عَمِلَ", "amila", "verb", ["idha-shartiyya", "fail"], "فِعْلٌ مَاضٍ.", "«governs».", "«amel ederse»."),
  W("فِيهَا", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  W("فِعْلٌ", "fil", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a verb» — the doer.", "«bir fiil» — fâil."),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ondan sonraki».", punct="،", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  nahwu(),
  kam(tags=["maful-bihi", KN], ar="فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِضَرَبْتَ.", en="«how many» — the object of «you beat».", tr="«kaç» — darabte'nin mef'ûlü."),
  W("رَجُلًا", "rajul", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«men».", "«adam»."),
  W("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you beat».", "«dövdün».", punct="؟", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
  kam(wa=True, tags=["maful-mutlaq", KN], ar="كَمْ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ مُطْلَقٌ.", en="«and how many» — the absolute object.", tr="«ve kaç» — mef'ûl-i mutlak."),
  W("ضَرْبَةً", "darba", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«blows».", "«vuruş»."),
  W("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you strike».", "«vurdun».", punct="؟", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
  kam(wa=True, tags=["maful-fih", KN], ar="كَمْ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ فِيهِ.", en="«and how many» — the adverbial object.", tr="«ve kaç» — mef'ûlün fîh."),
  W("يَوْمًا", "yawm", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«days».", "«gün»."),
  W("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you beat».", "«dövdün».", punct="؟", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
 ]})

# ----------- s8 (COMMENTARY): mahall jarr
S.append({"id": "s8", "translation": {
 "en": "And in the place of jarr when a jarr letter or a muḍāf precedes it — as in «for how many dirhams did you buy?» and «the servant of how many men did you beat?»." + C_EN,
 "tr": "Önünde bir cer harfi ya da bir muzâf varsa mahallen mecrûrdur — «kaç dirheme satın aldın?» ve «kaç adamın kölesini dövdün?» gibi." + C_TR},
 "tokens": [
  *fi_mahall("jarr", "جَرٍّ", "«jarr».", "«cer».", first=False),
  W("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ince»."),
  W("تَقَدَّمَهَا", "taqaddama", "verb", ["idha-shartiyya", "maful-bihi", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ.", "«precedes it».", "«ondan önce gelirse».", segments=[seg("تَقَدَّمَ", "taqaddama", "verb"), pr3fs()]),
  W("حَرْفُ", "harf", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«a letter of».", "«harfi»."),
  W("جَرٍّ", "jarr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُضَافٌ", "mudaf", "noun", ["atf-nasaq", "ism-maful"], "مَعْطُوفٌ مَرْفُوعٌ.", "«a muḍāf».", "«bir muzâf».", punct="،"),
  nahwu(),
  W("بِكَمْ", "kam", "pron", ["huruf-jarr", KN], "الْبَاءُ حَرْفُ جَرٍّ، وَكَمْ فِي مَحَلِّ جَرٍّ.", "«for how many» — كَمْ in the place of jarr by the bāʾ.", "«kaça» — bâ ile mahallen mecrûr kem.", segments=[seg("بِ", "bi", "prep"), seg("كَمْ", "kam", "pron")]),
  W("دِرْهَمًا", "dirham", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«dirhams».", "«dirhem»."),
  W("اشْتَرَيْتَ", "ishtara", "verb", ["fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you buy».", "«satın aldın».", punct="؟", segments=[seg("اشْتَرَيْ", "ishtara", "verb"), prTa()]),
  atf_wa("وَغُلَامَ", "ghulam", "noun", ["maful-bihi", "idafa-definiteness"], "غُلَامَ مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and the servant of» — the fronted object, a muḍāf.", "«ve kölesini» — öne alınmış mef'ûl, muzâf.", "غُلَامَ"),
  kam(tags=["idafa-definiteness", KN], ar="فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", en="«how many» — in the place of jarr as muḍāf ilayh.", tr="«kaç» — muzâfun ileyh olarak mahallen mecrûr."),
  W("رَجُلًا", "rajul", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«men».", "«adamın»."),
  W("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you beat».", "«dövdün».", punct="؟", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
 ]})

# ----------- s9 (COMMENTARY): mahall raf
S.append({"id": "s9", "translation": {
 "en": "And in the place of rafʿ when nothing requires its naṣb or its jarr: a mubtada if it is not a ẓarf and a khabar if it is — as in «how many men is your brother?» and «how many days is your journey?»." + C_EN,
 "tr": "Nasbını ya da cerrini gerektiren bir şey yoksa mahallen merfûdur: zarf değilse mübtedâ, zarfsa haber — «kardeşin kaç adam?» ve «yolculuğun kaç gün?» gibi." + C_TR},
 "tokens": [
  *fi_mahall("raf", "رَفْعٍ", "«rafʿ».", "«ref'».", first=False),
  W("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ince»."),
  W("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-mazsa»."),
  W("يَكُنْ", "kana", "verb", ["lam-jazim", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — تَامَّةٌ هُنَا بِمَعْنَى يُوجَدُ.", "«there is» — kāna complete here: «exists».", "«bulunmazsa» — burada tam kâne: «bulunur»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلُ يَكُنْ.", "«what» — the doer.", "«... bir şey» — fâil."),
  W("يُوجِبُ", "awjaba", "verb", ["ism-mawsul", "fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«requires» — the ṣila.", "«gerektiren» — sıla."),
  W("نَصْبَهَا", "nasb", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its naṣb».", "«nasbını».", segments=[seg("نَصْبَ", "nasb", "noun"), pr3fs()]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("جَرَّهَا", "jarr", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its jarr».", "«cerrini».", punct=":", segments=[seg("جَرَّ", "jarr", "noun"), pr3fs()]),
  W("مُبْتَدَأً", "mubtada", "noun", ["hal"], "حَالٌ مَنْصُوبٌ — أَيْ: تَكُونُ مُبْتَدَأً.", "«a mubtada» — the ḥāl.", "«mübtedâ olarak» — hâl."),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  W("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«... değilse»."),
  W("تَكُنْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ، فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is» — the condition's verb.", "«... ise» — şart fiili."),
  W("ظَرْفًا", "zarf", "noun", ["kana-wa-akhawatuha"], "خَبَرُ تَكُنْ مَنْصُوبٌ.", "«a ẓarf».", "«zarf»."),
  atf_wa("وَخَبَرًا", "khabar", "noun", ["hal"], "خَبَرًا مَعْطُوفٌ عَلَى مُبْتَدَأً مَنْصُوبٌ.", "«and a khabar».", "«ve haber olarak».", "خَبَرًا"),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  W("كَانَتْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«it is».", "«... ise»."),
  W("ظَرْفًا", "zarf", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَتْ مَنْصُوبٌ.", "«a ẓarf».", "«zarf».", punct="،"),
  nahwu(),
  kam(tags=["mubtada-khabar", KN], ar="فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — مُمَيِّزُهَا غَيْرُ ظَرْفٍ.", en="«how many» — the mubtada: its tamyīz is no ẓarf.", tr="«kaç» — mübtedâ: temyîzi zarf değil."),
  W("رَجُلًا", "rajul", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«men».", "«adam»."),
  W("أَخُوكَ", "akh", "noun", ["mubtada-khabar", "idafa-definiteness", "five-nouns"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«is your brother» — the khabar, rafʿ by the wāw.", "«kardeşin» — haber, vâv ile merfû.", punct="؟", segments=[seg("أَخُو", "akh", "noun"), pr2ms()]),
  kam(wa=True, tags=["mubtada-khabar", KN], ar="كَمْ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ — مُمَيِّزُهَا ظَرْفٌ.", en="«and how many» — the fronted khabar: its tamyīz is a ẓarf.", tr="«ve kaç» — öne alınmış haber: temyîzi zarf."),
  W("يَوْمًا", "yawm", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«days».", "«gün»."),
  W("سَفَرُكَ", "safar", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«is your journey» — the delayed mubtada.", "«yolculuğun» — mübtedâ.", punct="؟", segments=[seg("سَفَرُ", "safar", "noun"), pr2ms()]),
 ]})

# ----------- s10 (RESTORED + aya)
S.append({"id": "s10", "translation": {
 "en": "And كَأَيِّنْ has the meaning of the predicative كَمْ, and مِنْ usually accompanies it — as in «how many a prophet»." + R_EN,
 "tr": "كَأَيِّنْ haberiyye كَمْ manasındadır ve ona çoğunlukla مِنْ eşlik eder — «nice peygamber» gibi." + R_TR},
 "tokens": [
  cited_wa("وَكَأَيِّنْ", "kaayyin", "pron", ["mubtada-khabar", KN], "كَأَيِّنْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى السُّكُونِ.", "«and كَأَيِّنْ» — the mubtada.", "«ve keeyyin» — mübtedâ.", "كَأَيِّنْ"),
  W("بِمَعْنَى", "mana", "noun", ["huruf-jarr", "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in the meaning of» — the khabar.", "«manasındadır» — haber.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  cited("كَمْ", "kam", "pron", ["idafa-definiteness", KN], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«كَمْ».", "«kem»."),
  W("الْخَبَرِيَّةِ", "khabariyya", "noun", ["naat-sifa"], "صِفَةٌ لِكَمْ مَجْرُورَةٌ.", "«the predicative».", "«haberiyye».", punct="،"),
  atf_wa("وَيَلْزَمُهَا", "lazima", "verb", ["maful-bihi"], "يَلْزَمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَهَا مَفْعُولٌ بِهِ.", "«and accompanies it».", "«ve ona eşlik eder».", "يَلْزَمُ", extra_segs=[seg("يَلْزَمُ", "lazima", "verb"), pr3fs()]),
  cited("مِنْ", "min", "prep", ["fail"], "فِي مَحَلِّ رَفْعٍ فَاعِلٌ — لَفْظُ مِنْ.", "«مِنْ» — the doer.", "«min» — fâil."),
  W("غَالِبًا", "ghalib", "noun", ["hal", "ism-fail"], "حَالٌ مَنْصُوبٌ.", "«usually».", "«çoğunlukla».", punct="،"),
  nahwu(),
  W("وَكَأَيِّنْ", "kaayyin", "pron", ["mubtada-khabar", KN, "al-iqtibas-wal-tadmin"], "الْوَاوُ عَاطِفَةٌ، وَكَأَيِّنْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ (آل عِمْرَان ١٤٦).", "«and how many a» — the mubtada (Āl ʿImrān 3:146).", "«ve nice» — mübtedâ (Âl-i İmrân 3:146).", segments=[seg("وَ", "wa", "conj"), seg("كَأَيِّنْ", "kaayyin", "pron")]),
  W("مِنْ", "min", "prep", ["huruf-jarr", KN], "حَرْفُ جَرٍّ زَائِدٌ.", "«of» — the extra مِنْ.", "«-den» — zâid min."),
  W("نَبِيٍّ", "nabi", "noun", ["huruf-jarr", "tamyiz", KN], "مَجْرُورٌ لَفْظًا، تَمْيِيزُ كَأَيِّنْ.", "«a prophet» — the tamyīz.", "«peygamber» — temyîz.", punct="."),
 ]})
for _t in S[9]["tokens"]:
    if _t["surface"]["full"] == "نَبِيٍّ": _t["quoteAfter"] = "﴾"
S[9]["tokens"][8]["quoteBefore"] = "﴿"

# ----------- s11 (RESTORED): idha
S.append({"id": "s11", "translation": {
 "en": "The built adverbs: إِذَا for the future, and the meaning of a condition is usually in it, so the verb is preferred after it — as in «when the sun is risen, the day is present»." + R_EN,
 "tr": "Mebnî zarflar: إِذَا gelecek zaman içindir ve çoğunlukla şart manası taşır; bu yüzden sonrasında fiil tercih edilir — «güneş doğmuş olunca gündüz mevcuttur» gibi." + R_TR},
 "tokens": [
  W("الظُّرُوفُ", "zarf", "noun", ["mubtada-khabar", "jam-taksir", KN], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the adverbs» — the mubtada.", "«zarflar» — mübtedâ."),
  W("الْمَبْنِيَّةُ", "mabni", "noun", ["naat-sifa", K3], "صِفَةٌ مَرْفُوعَةٌ.", "«built».", "«mebnî».", punct=":"),
  cited("إِذَا", "idha", "part", ["mubtada-khabar", KN], "فِي مَحَلِّ رَفْعٍ خَبَرٌ — أَيْ: مِنْهَا إِذَا.", "«إِذَا» — the khabar: among them is إِذَا.", "«izâ» — haber: onlardan biri izâ."),
  li_("لِلْمُسْتَقْبَلِ", "mustaqbal", "noun", ["ism-maful"], "الْمُسْتَقْبَلِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for the future».", "«gelecek zaman için».", "الْمُسْتَقْبَلِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمُسْتَقْبَلِ", "mustaqbal", "noun")]),
  atf_wa("وَفِيهَا", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "فِي حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and in it is» — the fronted khabar.", "«ve onda vardır» — öne alınmış haber.", "فِي", extra_segs=[seg("فِي", "fi", "prep"), pr3fs()]),
  W("مَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the meaning of» — the delayed mubtada.", "«manası» — mübtedâ."),
  W("الشَّرْطِ", "shart", "noun", ["idafa-definiteness", "idha-shartiyya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a condition».", "«şart»."),
  W("غَالِبًا", "ghalib", "noun", ["hal", "ism-fail"], "حَالٌ مَنْصُوبٌ.", "«usually».", "«çoğunlukla».", punct="،"),
  W("فَلِذٰلِكَ", "dhalika", "pron", ["huruf-jarr", "lam-taleel", "asma-al-ishara"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لِلتَّعْلِيلِ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«so for that reason».", "«bu yüzden».", segments=[seg("فَ", "fa", "conj"), seg("لِ", "lam-taleel", "part"), seg("ذٰلِكَ", "dhalika", "pron")]),
  W("اخْتِيرَ", "ikhtara", "verb", ["naib-al-fail", "form-viii-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أُعِلَّ: اُخْتُيِرَ ← اخْتِيرَ.", "«is preferred» — the passive of a hollow Form VIII.", "«tercih edilir» — ecvef iftiâl'in meçhulü."),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ondan sonra».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("الْفِعْلُ", "fil", "noun", ["naib-al-fail"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«the verb» — the deputy doer.", "«fiil» — nâib-i fâil.", punct="،"),
  nahwu(),
  W("إِذَا", "idha", "part", ["idha-shartiyya", KN], "ظَرْفٌ لِمَا يُسْتَقْبَلُ، مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ.", "«when» — the future adverb with the condition in it.", "«-ince» — şart manalı gelecek zarfı."),
  W("كَانَتِ", "kana", "verb", ["idha-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«is» — kāna, the verb chosen after إِذَا.", "«olunca» — izâ'dan sonra seçilen fiil."),
  W("الشَّمْسُ", "shams", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَتْ مَرْفُوعٌ.", "«the sun» — its ism.", "«güneş» — ismi."),
  W("طَالِعَةً", "tali", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ كَانَتْ مَنْصُوبٌ.", "«risen» — its khabar.", "«doğmuş» — haberi."),
  W("فَالنَّهَارُ", "nahar", "noun", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَالنَّهَارُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the day» — the fāʾ of the answer; the mubtada.", "«gündüz» — cevabın fâ'sı; mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("النَّهَارُ", "nahar", "noun")]),
  W("مَوْجُودٌ", "mawjud", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ، وَالْجُمْلَةُ جَوَابُ إِذَا.", "«is present» — the khabar; the clause is the answer.", "«mevcuttur» — haber; cümle izâ'nın cevabı.", punct="."),
 ]})

# ----------- s12 (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "And it may be for surprise, and then the mubtada must follow it — as in «I went out, and there was the lion!»." + R_EN,
 "tr": "Müfâcee için de olur; o zaman sonrasında mübtedâ gelmesi gerekir — «çıktım, bir de ne göreyim, arslan!» gibi." + R_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ حَرْفُ تَقْلِيلٍ.", "«and may».", "«ve bazen».", "قَدْ"),
  W("تَكُونُ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is».", "«olur»."),
  li_("لِلْمُفَاجَأَةِ", "mufajaa", "noun", ["kana-wa-akhawatuha", "masdar"], "الْمُفَاجَأَةِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ تَكُونُ.", "«for surprise» — the khabar.", "«müfâcee için» — haber.", "الْمُفَاجَأَةِ", segs=[seg("لِ", "li", "prep"), seg("الْمُفَاجَأَةِ", "mufajaa", "noun")]),
  W("فَيَلْزَمُهَا", "lazima", "verb", ["maful-bihi"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَلْزَمُ فِعْلٌ مُضَارِعٌ، وَهَا مَفْعُولٌ بِهِ.", "«so it must follow it».", "«o zaman ona lâzım olur».", segments=[seg("فَ", "fa", "conj"), seg("يَلْزَمُ", "lazima", "verb"), pr3fs()]),
  W("الْمُبْتَدَأُ", "mubtada", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the mubtada» — the doer.", "«mübtedâ» — fâil.", punct="،"),
  nahwu(),
  W("خَرَجْتُ", "kharaja", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I went out».", "«çıktım».", segments=[seg("خَرَجْ", "kharaja", "verb"), prT()]),
  W("فَإِذَا", "idha-fujaiyya", "part", [KN, "idha-shartiyya"], "الْفَاءُ عَاطِفَةٌ، وَإِذَا لِلْمُفَاجَأَةِ — ظَرْفُ مَكَانٍ عِنْدَ قَوْمٍ، حَرْفٌ عِنْدَ آخَرِينَ.", "«and there!» — the إِذَا of surprise.", "«bir de ne göreyim» — müfâcee izâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha-fujaiyya", "part")]),
  W("السَّبُعُ", "sabu", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَخَبَرُهُ مَحْذُوفٌ تَقْدِيرُهُ حَاضِرٌ.", "«the lion» — the mubtada; its khabar «present» understood.", "«arslan» — mübtedâ; haberi «hâzır» takdirinde.", punct="!"),
 ]})

# ----------- s13 (RESTORED): idh
S.append({"id": "s13", "translation": {
 "en": "And إِذْ for the past, and it is annexed to both kinds of clause — as in «when you were few» and «when Ibrāhīm said to his father»." + R_EN,
 "tr": "إِذْ geçmiş zaman içindir ve her iki cümleye muzâf olur — «hani siz azdınız» ve «hani İbrâhîm babasına demişti» gibi." + R_TR},
 "tokens": [
  cited_wa("وَإِذْ", "idh", "part", ["mubtada-khabar", KN], "إِذْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى السُّكُونِ.", "«and إِذْ» — the mubtada.", "«ve iz» — mübtedâ.", "إِذْ"),
  li_("لِلْمَاضِي", "madi", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "الْمَاضِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the past» — the khabar.", "«geçmiş zaman için» — haber.", "الْمَاضِي", punct="،", segs=[seg("لِ", "li", "prep"), seg("الْمَاضِي", "madi", "noun")]),
  atf_wa("وَتُضَافُ", "adafa", "verb", ["naib-al-fail", "form-iv-verbs"], "تُضَافُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is annexed».", "«ve muzâf olur».", "تُضَافُ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْجُمْلَتَيْنِ", "jumla", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — الِاسْمِيَّةِ وَالْفِعْلِيَّةِ.", "«the two clauses» — nominal and verbal.", "«iki cümleye» — isim ve fiil cümlesi.", punct="،"),
  nahwu(),
  W("إِذْ", "idh", "part", [KN, "maful-fih", "al-iqtibas-wal-tadmin"], "ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ عَلَى السُّكُونِ، مُضَافٌ إِلَى الْجُمْلَةِ (الْأَنْفَال ٢٦).", "«when» — annexed to a nominal clause (al-Anfāl 8:26).", "«hani» — isim cümlesine muzâf (Enfâl 8:26)."),
  W("أَنْتُمْ", "antum", "pron", ["mubtada-khabar", "idafa-definiteness"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«you» — the mubtada of the annexed clause.", "«siz» — muzâf cümlenin mübtedâsı."),
  W("قَلِيلٌ", "qalil", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«few» — the khabar.", "«azdınız» — haber."),
  W("وَإِذْ", "idh", "part", [KN, "maful-fih", "al-iqtibas-wal-tadmin"], "الْوَاوُ عَاطِفَةٌ، وَإِذْ ظَرْفٌ مُضَافٌ إِلَى الْجُمْلَةِ الْفِعْلِيَّةِ (الْأَنْعَام ٧٤).", "«and when» — annexed to a verbal clause (al-Anʿām 6:74).", "«ve hani» — fiil cümlesine muzâf (En'âm 6:74).", segments=[seg("وَ", "wa", "conj"), seg("إِذْ", "idh", "part")]),
  W("قَالَ", "qala", "verb", ["fail", "idafa-definiteness", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«said».", "«demişti»."),
  W("إِبْرَاهِيمُ", "ibrahim", "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the doer.", "«İbrâhîm» — fâil."),
  li_("لِأَبِيهِ", "ab", "noun", ["five-nouns", "idafa-definiteness"], "أَبِي مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his father» — jarr by the yāʾ.", "«babasına» — yâ ile mecrûr.", "أَبِي", punct=".", segs=[seg("لِ", "li", "prep"), seg("أَبِي", "ab", "noun"), pr3msi()]),
 ]})
for _t in S[12]["tokens"]:
    if _t["surface"]["full"] == "قَلِيلٌ": _t["quoteAfter"] = "﴾"
    if _t["surface"]["full"] == "لِأَبِيهِ": _t["quoteAfter"] = "﴾"
S[12]["tokens"][6]["quoteBefore"] = "﴿"; S[12]["tokens"][9]["quoteBefore"] = "﴿"

# ----------- s14 (RESTORED): ayna, anna
S.append({"id": "s14", "translation": {
 "en": "And أَيْنَ and أَنَّى for place, as a question and as a condition — as in «where is Zayd?», «whence is this yours?» and «wherever you are, I am»." + R_EN,
 "tr": "أَيْنَ ve أَنَّى mekân içindir, istifhâm ve şart olarak — «Zeyd nerede?», «bu sana nereden?» ve «sen nerede olursan ben de orada olurum» gibi." + R_TR},
 "tokens": [
  cited_wa("وَأَيْنَ", "ayna", "pron", ["mubtada-khabar", KN], "أَيْنَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى الْفَتْحِ.", "«and أَيْنَ» — the mubtada.", "«ve eyne» — mübtedâ.", "أَيْنَ"),
  cited_wa("وَأَنَّى", "anna-istifham", "pron", [KN], "أَنَّى مَعْطُوفٌ.", "«and أَنَّى».", "«ve ennâ».", "أَنَّى"),
  li_("لِلْمَكَانِ", "makan", "noun", ["mubtada-khabar"], "الْمَكَانِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for place» — the khabar.", "«mekân için» — haber.", "الْمَكَانِ", segs=[seg("لِ", "li", "prep"), seg("الْمَكَانِ", "makan", "noun")]),
  W("اسْتِفْهَامًا", "istifham", "noun", ["hal", "masdar", "al-istifham"], "حَالٌ مَنْصُوبٌ — أَيْ: مُسْتَفْهَمًا بِهِمَا.", "«as a question» — the ḥāl.", "«istifhâm olarak» — hâl."),
  atf_wa("وَشَرْطًا", "shart", "noun", ["hal"], "شَرْطًا مَعْطُوفٌ مَنْصُوبٌ.", "«and as a condition».", "«ve şart olarak».", "شَرْطًا", punct="،"),
  nahwu(),
  W("أَيْنَ", "ayna", "pron", [KN, "maful-fih", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفُ مَكَانٍ لِلِاسْتِفْهَامِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ خَبَرٌ مُقَدَّمٌ.", "«where» — the fronted khabar.", "«nerede» — öne alınmış haber."),
  W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«is Zayd».", "«Zeyd».", punct="؟"),
  atf_wa("وَأَنَّى", "anna-istifham", "pron", [KN, "maful-fih", "khabar-al-mubtada-wa-ahkamuh", "al-iqtibas-wal-tadmin"], "أَنَّى ظَرْفٌ لِلِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ خَبَرٌ مُقَدَّمٌ (آل عِمْرَان ٣٧).", "«and whence» — the fronted khabar (Āl ʿImrān 3:37).", "«ve nereden» — öne alınmış haber (Âl-i İmrân 3:37).", "أَنَّى"),
  W("لَكِ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ مَجْرُورٌ — لِلْمُخَاطَبَةِ.", "«to you (f.)».", "«sana (kadın)».", segments=[seg("لَ", "li", "prep"), seg("كِ", "pron-2fs", "pron")]),
  W("هٰذَا", "hadha", "pron", ["mubtada-khabar", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«this» — the delayed mubtada.", "«bu» — mübtedâ.", punct="؟"),
  atf_wa("وَأَيْنَ", "ayna", "pron", [KN, "in-shartiyya", "maful-fih"], "أَيْنَ اسْمُ شَرْطٍ جَازِمٌ، ظَرْفُ مَكَانٍ فِي مَحَلِّ نَصْبٍ.", "«and wherever» — the conditional adverb.", "«ve nerede» — şart zarfı.", "أَيْنَ"),
  W("تَكُنْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، فِعْلُ الشَّرْطِ — تَامَّةٌ.", "«you are» — the condition's verb, jazm.", "«olursan» — şart fiili, meczûm."),
  W("أَكُنْ", "kana", "verb", ["al-majzum-wal-shart-wal-jaza", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، جَوَابُ الشَّرْطِ.", "«I am» — the answer, jazm.", "«ben de olurum» — cevap, meczûm.", punct="."),
 ]})
for _t in S[13]["tokens"]:
    if _t["surface"]["full"] == "هٰذَا": _t["quoteAfter"] = "﴾"
S[13]["tokens"][8]["quoteBefore"] = "﴿"

# ----------- s15 (RESTORED): mata, ayyana
S.append({"id": "s15", "translation": {
 "en": "And مَتَى for time, as a question and as a condition — «when did you come?», «whenever you go out, I go out»; and أَيَّانَ for the question about great matters and the future — «when is the Day of Judgement?»." + R_EN,
 "tr": "مَتَى zaman içindir, istifhâm ve şart olarak — «ne zaman geldin?», «ne zaman çıkarsan ben de çıkarım»; أَيَّانَ büyük işler ve gelecek hakkında istifhâm içindir — «din günü ne zaman?»." + R_TR},
 "tokens": [
  cited_wa("وَمَتَى", "mata", "pron", ["mubtada-khabar", KN], "مَتَى مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and مَتَى» — the mubtada.", "«ve metâ» — mübtedâ.", "مَتَى"),
  li_("لِلزَّمَانِ", "zaman", "noun", ["mubtada-khabar"], "الزَّمَانِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for time» — the khabar.", "«zaman için» — haber.", "الزَّمَانِ", segs=[seg("لِ", "li", "prep"), seg("الزَّمَانِ", "zaman", "noun")]),
  W("اسْتِفْهَامًا", "istifham", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«as a question».", "«istifhâm olarak»."),
  atf_wa("وَشَرْطًا", "shart", "noun", ["hal"], "شَرْطًا مَعْطُوفٌ.", "«and as a condition».", "«ve şart olarak».", "شَرْطًا", punct="،"),
  nahwu(),
  W("مَتَى", "mata", "pron", [KN, "maful-fih"], "ظَرْفُ زَمَانٍ لِلِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ.", "«when».", "«ne zaman»."),
  W("جِئْتَ", "jaa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you come».", "«geldin».", punct="؟", segments=[seg("جِئْ", "jaa", "verb"), prTa()]),
  atf_wa("وَمَتَى", "mata", "pron", [KN, "in-shartiyya", "maful-fih"], "مَتَى اسْمُ شَرْطٍ جَازِمٌ، ظَرْفُ زَمَانٍ.", "«and whenever» — the conditional adverb.", "«ve ne zaman» — şart zarfı.", "مَتَى"),
  W("تَخْرُجْ", "kharaja", "verb", ["in-shartiyya", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، فِعْلُ الشَّرْطِ.", "«you go out».", "«çıkarsan»."),
  W("أَخْرُجْ", "kharaja", "verb", ["al-majzum-wal-shart-wal-jaza"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، جَوَابُ الشَّرْطِ.", "«I go out».", "«ben de çıkarım».", punct="؛"),
  cited_wa("وَأَيَّانَ", "ayyana", "pron", ["mubtada-khabar", KN], "أَيَّانَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and أَيَّانَ» — the mubtada.", "«ve eyyâne» — mübtedâ.", "أَيَّانَ"),
  li_("لِلِاسْتِفْهَامِ", "istifham", "noun", ["mubtada-khabar"], "الِاسْتِفْهَامِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the question» — the khabar.", "«istifhâm için» — haber.", "الِاسْتِفْهَامِ", segs=[seg("لِ", "li", "prep"), seg("الِاسْتِفْهَامِ", "istifham", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«hakkında»."),
  W("الْأُمُورِ", "amr", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ أَمْرٍ.", "«matters».", "«işler»."),
  W("الْعِظَامِ", "azim", "noun", ["naat-sifa", "jam-taksir"], "صِفَةٌ مَجْرُورَةٌ — جَمْعُ عَظِيمٍ.", "«great».", "«büyük»."),
  atf_wa("وَالْمُسْتَقْبَلِ", "mustaqbal", "noun", ["huruf-jarr"], "الْمُسْتَقْبَلِ مَعْطُوفٌ مَجْرُورٌ.", "«and the future».", "«ve gelecek».", "الْمُسْتَقْبَلِ", punct="،"),
  nahwu(),
  W("أَيَّانَ", "ayyana", "pron", [KN, "maful-fih", "khabar-al-mubtada-wa-ahkamuh", "al-iqtibas-wal-tadmin"], "ظَرْفُ زَمَانٍ لِلِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ خَبَرٌ مُقَدَّمٌ (الذَّارِيَات ١٢).", "«when» — the fronted khabar (al-Dhāriyāt 51:12).", "«ne zaman» — öne alınmış haber (Zâriyât 51:12)."),
  W("يَوْمُ", "yawm", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the Day of».", "«günü»."),
  W("الدِّينِ", "din", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Judgement».", "«din».", punct="؟"),
 ]})
for _t in S[14]["tokens"]:
    if _t["surface"]["full"] == "الدِّينِ": _t["quoteAfter"] = "﴾"
S[14]["tokens"][17]["quoteBefore"] = "﴿"

# ----------- s16 (RESTORED): kayfa, mudh, mundhu
S.append({"id": "s16", "translation": {
 "en": "And كَيْفَ for the state as a question — «how are you?»; and مُذْ and مُنْذُ either for the start of a span, so a definite singular follows them, or for the whole of it, so a span reckoned by number follows — «I have not seen him since Friday», «I have not seen him for two days»." + R_EN,
 "tr": "كَيْفَ istifhâm olarak hâl içindir — «nasılsın?»; مُذْ ve مُنْذُ ya sürenin başı içindir, o zaman onları ma'rife bir müfred izler, ya da sürenin tamamı içindir, o zaman sayıyla ölçülen bir zaman izler — «onu cumadan beri görmedim», «onu iki gündür görmedim»." + R_TR},
 "tokens": [
  cited_wa("وَكَيْفَ", "kayfa", "pron", ["mubtada-khabar", KN], "كَيْفَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and كَيْفَ» — the mubtada.", "«ve keyfe» — mübtedâ.", "كَيْفَ"),
  li_("لِلْحَالِ", "hal-state", "noun", ["mubtada-khabar"], "الْحَالِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the state» — the khabar.", "«hâl için» — haber.", "الْحَالِ", segs=[seg("لِ", "li", "prep"), seg("الْحَالِ", "hal-state", "noun")]),
  W("اسْتِفْهَامًا", "istifham", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«as a question».", "«istifhâm olarak».", punct="،"),
  nahwu(),
  W("كَيْفَ", "kayfa", "pron", [KN, "khabar-al-mubtada-wa-ahkamuh"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«how» — the fronted khabar.", "«nasıl» — öne alınmış haber."),
  W("أَنْتَ", "anta", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«are you» — the delayed mubtada.", "«sen» — mübtedâ.", punct="؟"),
  cited_wa("وَمُذْ", "mudh", "part", ["mubtada-khabar", KN], "مُذْ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and مُذْ» — the mubtada.", "«ve müz» — mübtedâ.", "مُذْ"),
  cited_wa("وَمُنْذُ", "mundhu", "part", [KN], "مُنْذُ مَعْطُوفٌ.", "«and مُنْذُ».", "«ve münzü».", "مُنْذُ"),
  W("إِمَّا", "imma", "part", ["atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  li_("لِأَوَّلِ", "awwal", "noun", ["mubtada-khabar", "idafa-definiteness"], "أَوَّلِ مَجْرُورٌ، وَهُوَ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the start of» — the khabar.", "«başı için» — haber.", "أَوَّلِ", segs=[seg("لِ", "li", "prep"), seg("أَوَّلِ", "awwal", "noun")]),
  W("الْمُدَّةِ", "mudda", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the span».", "«sürenin»."),
  W("فَيَلِيهِمَا", "waliya", "verb", ["maful-bihi", "naqis-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَلِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُمَا مَفْعُولٌ بِهِ.", "«so follows them».", "«o zaman onları izler».", segments=[seg("فَ", "fa", "conj"), seg("يَلِي", "waliya", "verb"), pr3d()]),
  W("مُفْرَدٌ", "mufrad", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a singular» — the doer.", "«bir müfred» — fâil."),
  W("مَعْرِفَةٌ", "marifa", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«definite».", "«ma'rife».", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  li_("لِجَمِيعِهَا", "jami", "noun", ["atf-nasaq", "idafa-definiteness"], "جَمِيعِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — مَعْطُوفٌ عَلَى لِأَوَّلِ.", "«for the whole of it».", "«tamamı için».", "جَمِيعِ", segs=[seg("لِ", "li", "prep"), seg("جَمِيعِ", "jami", "noun"), pr3fs()]),
  W("فَيَلِيهِمَا", "waliya", "verb", ["maful-bihi", "naqis-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَلِي فِعْلٌ مُضَارِعٌ، وَهُمَا مَفْعُولٌ بِهِ.", "«so follows them».", "«o zaman onları izler».", segments=[seg("فَ", "fa", "conj"), seg("يَلِي", "waliya", "verb"), pr3d()]),
  W("زَمَانٌ", "zaman", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a span».", "«bir zaman»."),
  W("مُقَدَّرٌ", "muqaddar", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«reckoned».", "«ölçülen»."),
  W("بِالْعَدَدِ", "adad", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْعَدَدِ مَجْرُورٌ.", "«by number».", "«sayıyla».", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْعَدَدِ", "adad", "noun")]),
  nahwu(),
  W("مَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not».", "«-medim»."),
  W("رَأَيْتُهُ", "raa", "verb", ["fail", "maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I saw him».", "«onu gördüm».", segments=[seg("رَأَيْ", "raa", "verb"), prT(), pr3ms()]),
  W("مُذْ", "mudh", "part", [KN, "mubtada-khabar"], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — اسْمٌ هُنَا، وَمَا بَعْدَهُ خَبَرُهُ؛ وَعِنْدَ الزَّجَّاجِ خَبَرٌ مُقَدَّمٌ.", "«since» — a noun here, the mubtada; al-Zajjāj reads it as the fronted khabar.", "«... beri» — burada isim, mübtedâ; Zeccâc'a göre öne alınmış haber."),
  W("يَوْمُ", "yawm", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — أَيْ: أَوَّلُ الْمُدَّةِ يَوْمُ الْجُمُعَةِ.", "«the day of» — the khabar: the start of the span is Friday.", "«günü» — haber: sürenin başı cuma günü."),
  W("الْجُمُعَةِ", "jumua", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Friday».", "«cuma».", punct="،"),
  atf_wa("وَمَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "مَا حَرْفُ نَفْيٍ.", "«and not».", "«ve -medim».", "مَا"),
  W("رَأَيْتُهُ", "raa", "verb", ["fail", "maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I saw him».", "«onu gördüm».", segments=[seg("رَأَيْ", "raa", "verb"), prT(), pr3ms()]),
  W("مُنْذُ", "mundhu", "part", [KN, "mubtada-khabar"], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — بِمَعْنَى جَمِيعِ الْمُدَّةِ.", "«for» — the whole span.", "«-dir» — sürenin tamamı."),
  W("يَوْمَانِ", "yawm", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two days» — the khabar, rafʿ by the alif.", "«iki gün» — haber, elif ile merfû.", punct="."),
 ]})

# ---------------------------------------------------------------- NFC
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
 "kaayyin": need("kaayyin", "كَأَيِّنْ", None, "pron", "how many a… (= the predicative كَمْ; usually with مِنْ: كَأَيِّنْ مِنْ نَبِيٍّ)", "nice… (= haberiyye kem; çoğunlukla min ile: keeyyin min nebiyyin)", 5),
 "mufajaa": need("mufajaa", "مُفَاجَأَة", "ف ج أ", "noun", "surprise, sudden encounter (masdar of Form III فَاجَأَ) — إِذَا الْمُفَاجَأَةِ: «and there was…!»", "müfâcee, ansızın karşılaşma (fâcee'nin masdarı) — izâ-i müfâcee: «bir de ne göreyim…!»", 4),
 "waliya": need("waliya", "وَلِيَ", "و ل ي", "verb", "to follow directly, to come next after (وَلِيَ يَلِي)", "hemen ardından gelmek, izlemek (veliye yelî)", 4),
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
put_morph(mo, "waliya", find_morph("waliya"))   # an identity copy: the key is owned elsewhere
report(7, S, GLOSS_ADD, (NOTE,))
