# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 30: THE JARR LETTERS (II) — إِلَى for the end-point in place and time, rarely «with» (4:2); حَتَّى like إِلَى
(97:5), often «with», on explicit nouns only (al-Mubarrad allows the pronoun); فِي for containment; the bāʾ for attachment, aid,
accompaniment, exchange, transitivity (and the «ṣayyara» sense it adds), containment, and its redundancy — by rule in the khabar of
لَيْسَ and مَا and after هَلْ, by hearing in a mubtada (بِحَسْبِكَ), a doer (كَفَى بِاللهِ شَهِيدًا) and an object (أَلْقَى بِيَدِهِ).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~332-333 of the transcription.

  COMMENTARY (the notebook): s1-s6 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch30.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "ila-hatta-fi-wal-ba-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الْجَرِّ: إِلَى وَحَتَّى وَفِي وَالْبَاءُ", "en": "The jarr letters — ilā, ḥattā, fī and the bāʾ", "tr": "Cer harfleri — ilâ, hattâ, fî ve bâ"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
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
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "part"), seg(inner, lex, pos)]))
def jw(full): return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full

HJ = "huruf-jarr"
def LET(full, lex, en, tr, ar="لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", wa=False, punct=None):
    if wa: return cited_wa("وَ" + full, lex, "prep", ["mubtada-khabar", K, HJ], full + " لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, full, punct=punct)
    return cited(full, lex, "prep", ["mubtada-khabar", K, HJ], ar, en, tr, punct=punct)
def FOR(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return li_(full, lex, "noun", ["mubtada-khabar", K] + list(tags), inner + " مَجْرُورٌ — خَبَرٌ.", en, tr, inner, punct=punct, segs=segs)
def FORW(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return W(full, lex, "noun", ["atf-nasaq", HJ, K] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَ" + inner + " مَجْرُورٌ — مَعْطُوفٌ عَلَى الْخَبَرِ.", en, tr, punct=punct, segments=(segs if segs else [seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg(inner, lex, "noun")]))
def PT(): return prT()

S.append({"id": "s1", "translation": {
 "en": "إِلَى is for the end-point — in place, as خَرَجْتُ إِلَى السُّوقِ, or in time, as أَتِمُّوا الصِّيَامَ إِلَى اللَّيْلِ; and rarely in the sense of مَعَ, as لَا تَأْكُلُوا أَمْوَالَهُمْ إِلَى أَمْوَالِكُمْ, that is, مَعَ أَمْوَالِكُمْ." + C_EN,
 "tr": "إِلَى intihâ içindir — خَرَجْتُ إِلَى السُّوقِ gibi mekânda ya da أَتِمُّوا الصِّيَامَ إِلَى اللَّيْلِ gibi zamanda; az olarak مَعَ mânâsındadır, لَا تَأْكُلُوا أَمْوَالَهُمْ إِلَى أَمْوَالِكُمْ gibi, yani مَعَ أَمْوَالِكُمْ." + C_TR},
 "tokens": [
  LET("إِلَى", "ila", "«ilā».", "«ilâ»."),
  FOR("لِلِانْتِهَاءِ", "intiha", "is for the end-point».", "«intihâ içindir».", "الِانْتِهَاءِ", segs=[seg("لِ", "li", "prep"), seg("لِانْتِهَاءِ", "intiha", "noun")], punct="،"),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمَكَانِ", "makan", "noun", [HJ], "مَجْرُورٌ.", "«place».", "«mekânda»."),
  ka_("كَخَرَجْتُ", "kharaja", "verb", [HJ, "fail"], "خَرَجْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«as «I went out»».", "««çıktım» gibi».", "خَرَجْ", segs=[seg("كَ", "ka", "part"), seg("خَرَجْ", "kharaja", "verb"), PT()]),
  cited("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِانْتِهَاءِ.", "«to».", "«-e»."),
  cited("السُّوقِ", "suq", "noun", [HJ], "مَجْرُورٌ — مُنْتَهَى الْخُرُوجِ.", "«the market».", "«çarşıya».", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الزَّمَانِ", "zaman", "noun", [HJ], "مَجْرُورٌ.", "«time».", "«zamanda»."),
  ka_("كَأَتِمُّوا", "atamma", "verb", [HJ, "fail", "doubled-verbs", "form-iv-verbs"], "أَتِمُّوا فِعْلُ أَمْرٍ، وَالْوَاوُ فَاعِلٌ — الْآيَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«as «complete»».", "««tamamlayın» gibi».", "أَتِمُّ", segs=[seg("كَ", "ka", "part"), seg("أَتِمُّ", "atamma", "verb"), seg("وا", "pron-2mp", "pron")]),
  cited("الصِّيَامَ", "siyam", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the fast».", "«orucu»."),
  cited("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِانْتِهَاءِ.", "«until».", "«-e kadar»."),
  cited("اللَّيْلِ", "layl", "noun", [HJ], "مَجْرُورٌ — مُنْتَهَى الصِّيَامِ.", "«night».", "«geceye».", punct="؛"),
  atf_wa("وَقَلِيلًا", "qalil", "noun", ["maful-mutlaq"], "قَلِيلًا نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ: تَكُونُ كَوْنًا قَلِيلًا.", "«and rarely».", "«ve az olarak».", "قَلِيلًا"),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness", K], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in the sense of».", "«mânâsındadır».", "مَعْنَى"),
  cited("مَعَ", "maa", "adv", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«maʿa».", "«mea».", punct="،"),
  nahwu(),
  cited("لَا", "la-nahiya", "part", ["la-nahiya", "nawasib-wa-jawazim-al-mudari"], "نَاهِيَةٌ جَازِمَةٌ.", "«do not».", "«-mayın»."),
  cited("تَأْكُلُوا", "akala", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«eat».", "«yemeyin».", segments=[seg("تَأْكُلُ", "akala", "verb"), seg("وا", "pron-2mp", "pron")]),
  cited("أَمْوَالَهُمْ", "mal", "noun", ["maful-bihi", "idafa-definiteness", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ مَالٍ.", "«their wealth».", "«onların mallarını».", segments=[seg("أَمْوَالَ", "mal", "noun"), pr3mp()]),
  cited("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ بِمَعْنَى مَعَ.", "«along with».", "«-e katarak»."),
  cited("أَمْوَالِكُمْ", "mal", "noun", [HJ, "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your wealth».", "«kendi mallarınız».", punct="،", segments=[seg("أَمْوَالِ", "mal", "noun"), pr2mp()]),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — التَّقْدِيرُ.", "«with».", "«ile birlikte»."),
  cited("أَمْوَالِكُمْ", "mal", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your wealth».", "«mallarınız».", punct=".", segments=[seg("أَمْوَالِ", "mal", "noun"), pr2mp()]),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And حَتَّى is like إِلَى for the end-point, as سَلَامٌ هِيَ حَتَّى مَطْلَعِ الْفَجْرِ; it is often in the sense of مَعَ; and it is confined to the explicit noun, though al-Mubarrad allowed it to enter on a pronoun." + C_EN,
 "tr": "حَتَّى intihâda إِلَى gibidir, سَلَامٌ هِيَ حَتَّى مَطْلَعِ الْفَجْرِ gibi; çoğu kere مَعَ mânâsındadır; zâhir isme mahsustur, fakat Müberred zamir üzerine girmesine cevaz verdi." + C_TR},
 "tokens": [
  LET("حَتَّى", "hatta", "«and ḥattā».", "«ve hattâ».", wa=True),
  ka_("كَإِلَى", "ila", "prep", ["mubtada-khabar", K, HJ], "إِلَى فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«is like ilā».", "«ilâ gibidir».", "إِلَى"),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«for».", "«-de»."),
  W("الِانْتِهَاءِ", "intiha", "noun", [HJ, K], "مَجْرُورٌ.", "«the end-point».", "«intihâda».", punct="،"),
  nahwu(),
  cited("سَلَامٌ", "salam", "noun", ["mubtada-khabar"], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«peace».", "«selâmettir»."),
  cited("هِيَ", "pron-3fs-munfasil", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "مُبْتَدَأٌ مُؤَخَّرٌ.", "«it is».", "«o»."),
  cited("حَتَّى", "hatta", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِانْتِهَاءِ.", "«until».", "«-e kadar»."),
  cited("مَطْلَعِ", "matla", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the rising of».", "«doğuşuna»."),
  cited("الْفَجْرِ", "fajr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«dawn».", "«fecrin».", punct="؛"),
  atf_wa("وَكَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "كَثِيرًا نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«and often».", "«ve çoğu kere».", "كَثِيرًا"),
  W("تَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ.", "«it is».", "«olur»."),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness", "kana-wa-akhawatuha"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ تَكُونُ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("مَعَ", "maa", "adv", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«maʿa».", "«mea».", punct="؛"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("مُخْتَصَّةٌ", "mukhtass", "noun", ["mubtada-khabar", "ism-maful", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«is confined».", "«mahsustur»."),
  bi_("بِالِاسْمِ", "ism", "noun", [], "الِاسْمِ مَجْرُورٌ.", "«to the noun».", "«isme».", "الِاسْمِ"),
  W("الظَّاهِرِ", "zahir", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«explicit».", "«zâhir».", punct="،"),
  atf_wa("وَجَوَّزَ", "jawwaza", "verb", ["fail", "form-ii-verbs"], "جَوَّزَ فِعْلٌ مَاضٍ.", "«though … allowed».", "«fakat ... cevaz verdi».", "جَوَّزَ"),
  W("الْمُبَرِّدُ", "mubarrad", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Mubarrad».", "«Müberred»."),
  W("دُخُولَهَا", "dukhul", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its entering».", "«girmesine».", segments=[seg("دُخُولَ", "dukhul", "noun"), pr3fs()]),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الضَّمِيرِ", "damir", "noun", [HJ, "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«a pronoun».", "«zamir».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And فِي is for containment, as الْمَاءُ فِي الْكُوزِ: the jug is a container for the water in reality." + C_EN,
 "tr": "فِي zarfiyet içindir, الْمَاءُ فِي الْكُوزِ gibi: bardak, suya hakikaten zarftır." + C_TR},
 "tokens": [
  LET("فِي", "fi", "«and fī».", "«ve fî».", wa=True),
  FOR("لِلظَّرْفِيَّةِ", "zarfiyya", "«is for containment».", "«zarfiyet içindir».", "الظَّرْفِيَّةِ", segs=[seg("لِ", "li", "prep"), seg("لظَّرْفِيَّةِ", "zarfiyya", "noun")], punct="،"),
  nahwu(),
  cited("الْمَاءُ", "ma-water", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the water».", "«su»."),
  cited("فِي", "fi", "prep", [K, HJ, "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is in».", "«-dadır»."),
  cited("الْكُوزِ", "kuz", "noun", [HJ], "مَجْرُورٌ.", "«the jug».", "«bardak».", punct=":"),
  W("فَالْكُوزُ", "kuz", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْكُوزُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the jug».", "«bardak».", segments=[seg("فَ", "fa", "conj"), seg("الْكُوزُ", "kuz", "noun")]),
  W("ظَرْفٌ", "zarf", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a container».", "«zarftır»."),
  li_("لِلْمَاءِ", "ma-water", "noun", [], "الْمَاءِ مَجْرُورٌ.", "«for the water».", "«suya».", "الْمَاءِ", segs=[seg("لِ", "li", "prep"), seg("لْمَاءِ", "ma-water", "noun")]),
  W("حَقِيقَةً", "haqiqa", "noun", ["hal", "haqiqa-majaz"], "حَالٌ مَنْصُوبٌ — لَا مَجَازًا.", "«in reality».", "«hakikaten».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the bāʾ is for attachment, as مَرَرْتُ بِزَيْدٍ; for aid, as كَتَبْتُ بِالْقَلَمِ; for accompaniment, as اشْتَرَيْتُ الْفَرَسَ بِسَرْجِهِ; and for exchange, as بِعْتُ هَذَا بِذَاكَ." + C_EN,
 "tr": "Bâ ilsâk içindir, مَرَرْتُ بِزَيْدٍ gibi; istiâne içindir, كَتَبْتُ بِالْقَلَمِ gibi; musâhabe içindir, اشْتَرَيْتُ الْفَرَسَ بِسَرْجِهِ gibi; ve mukâbele içindir, بِعْتُ هَذَا بِذَاكَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَالْبَاءُ", "ba-harf", "noun", ["mubtada-khabar", K, HJ], "الْبَاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the bāʾ».", "«ve bâ».", "الْبَاءُ"),
  FOR("لِلْإِلْصَاقِ", "ilsaq", "«is for attachment».", "«ilsâk içindir».", "الْإِلْصَاقِ", segs=[seg("لِ", "li", "prep"), seg("لْإِلْصَاقِ", "ilsaq", "noun")], punct="،"),
  nahwu(),
  cited("مَرَرْتُ", "marra", "verb", ["fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I passed».", "«uğradım».", segments=[seg("مَرَرْ", "marra", "verb"), PT()]),
  bi_("بِزَيْدٍ", "zayd", "propn", [K], "زَيْدٍ مَجْرُورٌ — أَلْصَقَتِ الْبَاءُ الْمُرُورَ بِزَيْدٍ.", "«by Zayd».", "«Zeyd'e».", "زَيْدٍ", punct="؛"),
  FORW("وَلِلِاسْتِعَانَةِ", "istiana", "«and for aid».", "«ve istiâne içindir».", "الِاسْتِعَانَةِ", segs=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لِاسْتِعَانَةِ", "istiana", "noun")], punct="،"),
  nahwu(),
  cited("كَتَبْتُ", "kataba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I wrote».", "«yazdım».", segments=[seg("كَتَبْ", "kataba", "verb"), PT()]),
  bi_("بِالْقَلَمِ", "qalam", "noun", [K], "الْقَلَمِ مَجْرُورٌ — الْآلَةُ الْمُسْتَعَانُ بِهَا.", "«with the pen».", "«kalemle».", "الْقَلَمِ", punct="؛"),
  FORW("وَلِلْمُصَاحَبَةِ", "musahaba", "«and for accompaniment».", "«ve musâhabe içindir».", "الْمُصَاحَبَةِ", segs=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لْمُصَاحَبَةِ", "musahaba", "noun")], punct="،"),
  nahwu(),
  cited("اشْتَرَيْتُ", "ishtara", "verb", ["fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I bought».", "«satın aldım».", segments=[seg("اشْتَرَيْ", "ishtara", "verb"), PT()]),
  cited("الْفَرَسَ", "faras", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the horse».", "«atı»."),
  bi_("بِسَرْجِهِ", "sarj", "noun", [K, "idafa-definiteness"], "سَرْجِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْبَاءُ بِمَعْنَى مَعَ.", "«with its saddle».", "«eyeriyle birlikte».", "سَرْجِ", segs=[seg("بِ", "bi", "prep"), seg("سَرْجِ", "sarj", "noun"), pr3msi()], punct="؛"),
  FORW("وَلِلْمُقَابَلَةِ", "muqabala", "«and for exchange».", "«ve mukâbele içindir».", "الْمُقَابَلَةِ", segs=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لْمُقَابَلَةِ", "muqabala", "noun")], punct="،"),
  nahwu(),
  cited("بِعْتُ", "baa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I sold».", "«sattım».", segments=[seg("بِعْ", "baa", "verb"), PT()]),
  cited("هَذَا", "hadha", "pron", ["maful-bihi", "asma-al-ishara-wal-mawsulat"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this».", "«bunu»."),
  bi_("بِذَاكَ", "dhaka", "pron", [K, "asma-al-ishara-wal-mawsulat"], "ذَاكَ فِي مَحَلِّ جَرٍّ — الْعِوَضُ.", "«for that».", "«şunun karşılığında».", "ذَاكَ", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And for transitivity, as ذَهَبْتُ بِزَيْدٍ, that is, صَيَّرْتُهُ ذَاهِبًا; when an intransitive verb is made transitive by the bāʾ it carries the sense of صَيَّرَ, and not with any other letter — so ذَهَبْتُ إِلَى زَيْدٍ means ذَهَبْتُ نَحْوَهُ; and for containment, as جَلَسْتُ بِالْمَسْجِدِ." + C_EN,
 "tr": "Ta'diye içindir, ذَهَبْتُ بِزَيْدٍ gibi, yani صَيَّرْتُهُ ذَاهِبًا; lâzım fiil bâ ile müteaddî olduğunda صَيَّرَ mânâsını taşır, başka harfle taşımaz — ذَهَبْتُ إِلَى زَيْدٍ, ذَهَبْتُ نَحْوَهُ demektir; ve zarfiyet içindir, جَلَسْتُ بِالْمَسْجِدِ gibi." + C_TR},
 "tokens": [
  FORW("وَلِلتَّعْدِيَةِ", "tadiya", "«and for transitivity».", "«ve ta'diye içindir».", "التَّعْدِيَةِ", segs=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لتَّعْدِيَةِ", "tadiya", "noun")], punct="،"),
  nahwu(),
  cited("ذَهَبْتُ", "dhahaba", "verb", ["fail"], "فِعْلٌ مَاضٍ لَازِمٌ، وَالتَّاءُ فَاعِلٌ.", "«I took away».", "«götürdüm».", segments=[seg("ذَهَبْ", "dhahaba", "verb"), PT()]),
  bi_("بِزَيْدٍ", "zayd", "propn", [K, "al-lazim-wal-mutaaddi"], "زَيْدٍ مَجْرُورٌ — الْبَاءُ عَدَّتِ الْفِعْلَ اللَّازِمَ.", "«Zayd».", "«Zeyd'i».", "زَيْدٍ", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("صَيَّرْتُهُ", "sayyara", "verb", ["fail", "mafulayn", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«I made him».", "«onu ... kıldım».", segments=[seg("صَيَّرْ", "sayyara", "verb"), PT(), pr3ms()]),
  cited("ذَاهِبًا", "dhahib", "noun", ["mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«go».", "«gider».", punct="؛"),
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -diğinde».", "إِذَا"),
  W("تَعَدَّى", "taadda", "verb", ["idha-shartiyya", "fail", "form-v-verbs", "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«is made transitive».", "«müteaddî olduğunda»."),
  W("اللَّازِمُ", "lazim", "noun", ["fail", "al-lazim-wal-mutaaddi"], "فَاعِلٌ مَرْفُوعٌ.", "«the intransitive».", "«lâzım fiil»."),
  bi_("بِالْبَاءِ", "ba-harf", "noun", [K], "الْبَاءِ مَجْرُورٌ.", "«by the bāʾ».", "«bâ ile».", "الْبَاءِ"),
  W("أَفَادَ", "afada", "verb", ["fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ — جَوَابُ الشَّرْطِ.", "«it carries».", "«taşır»."),
  W("مَعْنَى", "mana", "noun", ["maful-bihi", "idafa-definiteness", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the sense of».", "«mânâsını»."),
  cited("صَيَّرَ", "sayyara", "verb", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«ṣayyara».", "«sayyere».", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... -maz».", "لَا"),
  W("يُفِيدُهُ", "afada", "verb", ["fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«carries it».", "«taşımaz».", segments=[seg("يُفِيدُ", "afada", "verb"), pr3ms()]),
  bi_("بِغَيْرِهَا", "ghayr", "noun", ["idafa-definiteness"], "غَيْرِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«with any other».", "«başka harfle».", "غَيْرِ", segs=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun"), pr3fs()], punct="،"),
  cited("فَذَهَبْتُ", "dhahaba", "verb", ["fail", "mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَذَهَبْتُ مَحْكِيٌّ مُبْتَدَأٌ.", "«so «I went»».", "«o hâlde «gittim»».", segments=[seg("فَ", "fa", "conj"), seg("ذَهَبْ", "dhahaba", "verb"), PT()]),
  cited("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِانْتِهَاءِ.", "«to».", "«-e»."),
  cited("زَيْدٍ", "zayd", "propn", [HJ], "مَجْرُورٌ.", "«Zayd».", "«Zeyd'e»."),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«means».", "«... demektir».", "مَعْنَى"),
  cited("ذَهَبْتُ", "dhahaba", "verb", ["idafa-definiteness", "fail"], "مُضَافٌ إِلَيْهِ — الْجُمْلَةُ مَحْكِيَّةٌ.", "«I went».", "«gittim».", segments=[seg("ذَهَبْ", "dhahaba", "verb"), PT()]),
  cited("نَحْوَهُ", "nahwa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«toward him».", "«ona doğru».", punct="؛", segments=[seg("نَحْوَ", "nahwa", "adv"), pr3ms()]),
  FORW("وَلِلظَّرْفِيَّةِ", "zarfiyya", "«and for containment».", "«ve zarfiyet içindir».", "الظَّرْفِيَّةِ", segs=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لظَّرْفِيَّةِ", "zarfiyya", "noun")], punct="،"),
  nahwu(),
  cited("جَلَسْتُ", "jalasa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I sat».", "«oturdum».", segments=[seg("جَلَسْ", "jalasa", "verb"), PT()]),
  bi_("بِالْمَسْجِدِ", "masjid", "noun", [K], "الْمَسْجِدِ مَجْرُورٌ — الْبَاءُ بِمَعْنَى فِي.", "«in the mosque».", "«mescitte».", "الْمَسْجِدِ", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And it is redundant by rule in the khabar of لَيْسَ and of the negating مَا, and in the question with هَلْ — as هَلْ زَيْدٌ بِقَائِمٍ; and by hearing elsewhere: in a mubtada, as بِحَسْبِكَ زَيْدٌ; in a doer, as كَفَى بِاللهِ شَهِيدًا; and in an object, as أَلْقَى بِيَدِهِ." + C_EN,
 "tr": "لَيْسَ ve nâfiye مَا'nın haberinde ve هَلْ ile istifhamda kıyasen zâid olur — هَلْ زَيْدٌ بِقَائِمٍ gibi; bunların dışında semâen zâid olur: mübtedâda, بِحَسْبِكَ زَيْدٌ gibi; fâilde, كَفَى بِاللهِ شَهِيدًا gibi; ve mef'ûlde, أَلْقَى بِيَدِهِ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتُزَادُ", "zada", "verb", ["naib-al-fail", "hollow-verbs"], "تُزَادُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«and it is redundant».", "«ve zâid olur».", "تُزَادُ"),
  W("قِيَاسًا", "qiyas", "noun", ["hal"], "حَالٌ مَنْصُوبٌ، أَوْ مَفْعُولٌ مُطْلَقٌ.", "«by rule».", "«kıyasen»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("خَبَرِ", "khabar", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the khabar of».", "«haberinde»."),
  cited("لَيْسَ", "laysa", "verb", ["idafa-definiteness", "kana-wa-akhawatuha"], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«laysa».", "«leyse»."),
  cited_wa("وَمَا", "ma-nafiya", "part", ["idafa-definiteness", "anwa-ma", "ma-la-laysa-wa-la-al-jins"], "مَا مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and mā».", "«ve mâ».", "مَا"),
  W("النَّافِيَةِ", "nafi", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«the negating».", "«nâfiye»."),
  atf_wa("وَفِي", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -da».", "فِي"),
  W("الِاسْتِفْهَامِ", "istifham", "noun", [HJ, "adawat-al-tasawwur"], "مَجْرُورٌ.", "«the question».", "«istifhamda»."),
  bi_("بِهَلْ", "hal-istifham", "part", ["adawat-al-tasawwur"], "هَلْ فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«with hal».", "«hel ile».", "هَلْ", punct="،"),
  nahwu(),
  cited("هَلْ", "hal-istifham", "part", ["adawat-al-tasawwur"], "حَرْفُ اسْتِفْهَامٍ.", "«is».", "«-mı»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  bi_("بِقَائِمٍ", "qaim", "noun", [K, "mubtada-khabar"], "قَائِمٍ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا خَبَرٌ — الْبَاءُ زَائِدَةٌ قِيَاسًا.", "«standing».", "«ayakta».", "قَائِمٍ", punct="؛"),
  atf_wa("وَسَمَاعًا", "samaa", "noun", ["hal"], "سَمَاعًا حَالٌ مَعْطُوفٌ عَلَى قِيَاسًا.", "«and by hearing».", "«ve semâen».", "سَمَاعًا"),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("غَيْرِهَا", "ghayr", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«elsewhere».", "«bunların dışında».", punct=":", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الْمُبْتَدَإِ", "mubtada", "noun", [HJ, "mubtada-khabar"], "مَجْرُورٌ.", "«a mubtada».", "«mübtedâda».", punct="،"),
  nahwu(),
  cited("بِحَسْبِكَ", "hasb-enough", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "الْبَاءُ زَائِدَةٌ سَمَاعًا، وَحَسْبِ مُبْتَدَأٌ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«enough for you».", "«sana yeter».", segments=[seg("بِ", "bi", "prep"), seg("حَسْبِ", "hasb-enough", "noun"), pr2ms()]),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is Zayd».", "«Zeyd».", punct="،"),
  atf_wa("وَفِي", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ.", "«in».", "«... -de».", "فِي"),
  W("الْفَاعِلِ", "fail-doer", "noun", [HJ, "fail"], "مَجْرُورٌ.", "«a doer».", "«fâilde».", punct="،"),
  nahwu(),
  cited("كَفَى", "kafa", "verb", ["fail", "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ.", "«suffices».", "«yeter»."),
  cited("بِاللهِ", "allah", "propn", [K, "fail"], "الْبَاءُ زَائِدَةٌ، وَلَفْظُ الْجَلَالَةِ فَاعِلٌ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا.", "«God».", "«Allah».", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  cited("شَهِيدًا", "shahid-witness", "noun", ["tamyiz", "hal"], "تَمْيِيزٌ أَوْ حَالٌ مَنْصُوبٌ.", "«as witness».", "«şahit olarak».", punct="،"),
  atf_wa("وَفِي", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("الْمَفْعُولِ", "maful-noun", "noun", [HJ, "maful-bihi"], "مَجْرُورٌ.", "«an object».", "«mef'ûlde».", punct="،"),
  nahwu(),
  cited("أَلْقَى", "alqa", "verb", ["fail", "form-iv-verbs", "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«he threw».", "«attı»."),
  cited("بِيَدِهِ", "yad", "noun", [K, "maful-bihi", "idafa-definiteness"], "الْبَاءُ زَائِدَةٌ، وَيَدِ مَفْعُولٌ بِهِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his hand».", "«elini».", punct=".", segments=[seg("بِ", "bi", "prep"), seg("يَدِ", "yad", "noun"), pr3msi()]),
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
 "atamma": need("atamma", "أَتَمَّ", "ت م م", "verb", "to complete, to bring to its end (Form IV, doubled)", "tamamlamak, sonuna erdirmek (if'âl, muzâaf)", 3),
 "zarfiyya": need("zarfiyya", "ظَرْفِيَّة", "ظ ر ف", "noun", "containment — the sense of fī, a place or time holding what is in it", "zarfiyet — fî'nin mânâsı; içindekini tutan yer ya da zaman", 4),
 "sarj": need("sarj", "سَرْج", "س ر ج", "noun", "a saddle", "eyer", 3),
 "kuz": need("kuz", "كُوز", "ك و ز", "noun", "a jug, a mug", "bardak, testi", 3),
 "mubarrad": need("mubarrad", "الْمُبَرِّد", "ب ر د", "propn", "Al-Mubarrad (d. 285/898) — the Basran grammarian, author of al-Muqtaḍab", "Müberred (ö. 285/898) — Basralı nahivci, el-Muktadab'ın müellifi", 5),
 "fajr": need("fajr", "فَجْر", "ف ج ر", "noun", "dawn, daybreak", "fecir, tan", 2),
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
put_morph(mo, "atamma", _nfc(_sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "إِتْمَام", "مُتِمّ", _sg.mazi14("أَتَمّ", "أَتْمَم"), _sg.mudari14("ُ", "تِمّ", "تْمِم"), ["أَتِمَّ", "أَتِمَّا", "أَتِمُّوا", "أَتِمِّي", "أَتِمَّا", "أَتْمِمْنَ"], "يُتِمَّ", "يُتِمَّ", "تُتِمَّ", "مُتَمّ", "أُتِمَّ", "يُتَمُّ", "أَتَمَّ الشَّيْءَ: أَكْمَلَهُ وَبَلَغَ بِهِ تَمَامَهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُتِمَّ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch30 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "إِلَى وَحَتَّى وَفِي وَالْبَاءُ فِي الْكَافِيَةِ", "en": "Ilā, ḥattā, fī and the bāʾ in the Kafiya: the end-point and its rare «with», ḥattā's restriction, containment, and the bāʾ's seven senses with its two kinds of redundancy", "tr": "Kâfiye'de ilâ, hattâ, fî ve bâ: intihâ ve nadir «ile»si, hattâ'nın kaydı, zarfiyet ve bâ'nın iki tür zâidliğiyle yedi mânâsı"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — حروف الجر: إلى للانتهاء، حتى كإلى، في للظرفية، الباء للإلصاق والاستعانة والمصاحبة والمقابلة والتعدية والظرفية والزيادة", "ضياء صونغور اوغلى — دفتر الكافية: إلى في المكان والزمان وبمعنى مع؛ حتى والمبرد؛ الماء في الكوز؛ معاني الباء وأمثلتها؛ زيادتها قياسا في خبر ليس وما وبعد هل، وسماعا في المبتدأ والفاعل والمفعول"],
 "question": {
  "en": ["What does إِلَى do? It names the END of what the verb reaches — a place (خَرَجْتُ إِلَى السُّوقِ) or a time (أَتِمُّوا الصِّيَامَ إِلَى اللَّيْلِ). It is the mirror of مِنْ, which is why the madrasah's test for مِنْ was «can إِلَى stand opposite it?». Rarely it means «together with» (4:2), and the notebook marks that as the exception it is.",
         "How does حَتَّى differ? In sense it is إِلَى (97:5), and more often than إِلَى it means «including, along with». In use it is narrower: it takes only an explicit noun — حَتَّاهُ is not said — except for al-Mubarrad, who lets it govern a pronoun.",
         "And فِي? Containment, in reality (الْمَاءُ فِي الْكُوزِ) — the metaphorical uses come later; the notebook's point is that the jug really holds the water, which is why the Jarr lab calls this the literal ẓarfiyya.",
         "What are the bāʾ's senses? Attachment (مَرَرْتُ بِزَيْدٍ — the passing touches Zayd), aid (كَتَبْتُ بِالْقَلَمِ — the instrument), accompaniment (بِسَرْجِهِ — «with»), exchange (بِعْتُ هَذَا بِذَاكَ — the price), transitivity (ذَهَبْتُ بِزَيْدٍ — «I made Zayd go»), and containment (جَلَسْتُ بِالْمَسْجِدِ — «in»).",
         "Why does the bāʾ of transitivity matter? Because it alone adds the sense of ṣayyara: ذَهَبْتُ بِزَيْدٍ makes Zayd go, while ذَهَبْتُ إِلَى زَيْدٍ only goes toward him. The letter changes who moves — a fact the analyzer's lāzim/mutaʿaddī reading has to respect.",
         "When is the bāʾ redundant? By RULE in three places — the khabar of لَيْسَ, the khabar of the negating مَا, and the question with هَلْ (هَلْ زَيْدٌ بِقَائِمٍ); by HEARING elsewhere, in cases the books list and the learner memorises: a mubtada (بِحَسْبِكَ زَيْدٌ), a doer (كَفَى بِاللهِ شَهِيدًا), an object (أَلْقَى بِيَدِهِ). A redundant letter governs the word's form but not its place: قَائِمٍ is majrūr in letter and khabar in position."],
  "tr": ["إِلَى ne yapar? Fiilin ulaştığının SONUNU adlandırır — bir yer (خَرَجْتُ إِلَى السُّوقِ) ya da bir zaman (أَتِمُّوا الصِّيَامَ إِلَى اللَّيْلِ). مِنْ'in aynasıdır; medresenin مِنْ testinin «karşısına إِلَى konabilir mi?» olması bundandır. Nadiren «ile birlikte» demektir (4:2) ve defter bunu olduğu gibi istisna olarak işaretler.",
         "حَتَّى nasıl farklıdır? Mânâda إِلَى'dır (97:5) ve إِلَى'dan daha sık «dahil, beraber» demektir. Kullanımda daha dardır: yalnız zâhir isim alır — حَتَّاهُ denmez — zamiri yönetmesine izin veren Müberred hariç.",
         "Ya فِي? Zarfiyet, hakikaten (الْمَاءُ فِي الْكُوزِ) — mecazî kullanımlar sonra gelir; defterin vurgusu bardağın suyu gerçekten tutmasıdır; Cer laboratuvarının buna hakikî zarfiyet demesi bundandır.",
         "Bâ'nın mânâları nelerdir? İlsâk (مَرَرْتُ بِزَيْدٍ — uğrama Zeyd'e değer), istiâne (كَتَبْتُ بِالْقَلَمِ — alet), musâhabe (بِسَرْجِهِ — «ile»), mukâbele (بِعْتُ هَذَا بِذَاكَ — bedel), ta'diye (ذَهَبْتُ بِزَيْدٍ — «Zeyd'i gider kıldım») ve zarfiyet (جَلَسْتُ بِالْمَسْجِدِ — «-de»).",
         "Ta'diye bâ'sı neden önemlidir? Çünkü sayyere mânâsını yalnız o katar: ذَهَبْتُ بِزَيْدٍ Zeyd'i gider kılar, ذَهَبْتُ إِلَى زَيْدٍ yalnız ona doğru gider. Harf kimin hareket ettiğini değiştirir — analizörün lâzım/müteaddî okuyuşunun saymak zorunda olduğu bir olgu.",
         "Bâ ne zaman zâiddir? KIYASEN üç yerde — لَيْسَ'nin haberi, nâfiye مَا'nın haberi ve هَلْ ile istifham (هَلْ زَيْدٌ بِقَائِمٍ); SEMÂEN başka yerlerde, kitapların listeleyip talebenin ezberlediği hâllerde: mübtedâ (بِحَسْبِكَ زَيْدٌ), fâil (كَفَى بِاللهِ شَهِيدًا), mef'ûl (أَلْقَى بِيَدِهِ). Zâid harf kelimenin şeklini yönetir, yerini değil: قَائِمٍ lafzen mecrûr, mahallen haberdir."]},
 "plain": {
  "en": "Ilā says where or when something ends, ḥattā does the same with a hint of «including», and fī says «inside». The bāʾ is the busiest letter: «by», «with», «for», «in», and the one that makes «I went» into «I took him». Sometimes the bāʾ adds no meaning at all, and the books say exactly where that is allowed.",
  "tr": "İlâ bir şeyin nerede ya da ne zaman bittiğini söyler, hattâ aynı şeyi «dahil» imasıyla yapar, fî «içinde» der. Bâ en meşgul harftir: «ile», «birlikte», «karşılığında», «-de» ve «gittim»i «götürdüm» yapan harf. Bazen bâ hiç mânâ katmaz ve kitaplar bunun tam nerede câiz olduğunu söyler."},
 "explanation": {
  "en": "Four letters, in the notebook's order and with its examples. إِلَى is defined by the end-point in place and in time, and the one departure, the sense of مَعَ in the verse on the orphans' property, is marked as rare. حَتَّى shares the end-point sense and adds two facts a learner needs at once: it leans toward «including», and it refuses a pronoun — the dissent of al-Mubarrad is recorded with his name, as every dissent in this book is. فِي is the literal container, and the notebook's one-line gloss insists on ḥaqīqatan: the jug really holds the water. The bāʾ takes the rest of the chapter, and the notebook's list is the classical seven with the Kafiya's own examples; the gloss on transitivity is the chapter's sharpest point — only the bāʾ makes the intransitive verb a causative, and ذَهَبْتُ إِلَى زَيْدٍ against ذَهَبْتُ بِزَيْدٍ shows the difference in a word. Redundancy is divided as the madrasah divides it, into what is by rule (the three places after a negation or a question) and what is by hearing (the mubtada, the doer, the object), each with its Qurʾānic or proverbial case. Every redundant bāʾ in the chapter is parsed with its double iʿrāb — majrūr in letter, its true office in position — which is the TaalluqEngine's and the SignEngine's shared rule for a zāʾid letter.",
  "tr": "Dört harf, defterin sırası ve örnekleriyle. إِلَى yerde ve zamanda intihâ ile tarif edilir; tek sapma, yetimlerin malı âyetindeki مَعَ mânâsı, nadir diye işaretlenir. حَتَّى intihâ mânâsını paylaşır ve talebenin hemen ihtiyaç duyduğu iki olgu ekler: «dahil»e meyleder ve zamiri reddeder — Müberred'in muhalefeti, bu kitaptaki her muhalefet gibi, adıyla kaydedilir. فِي hakikî zarftır ve defterin tek satırlık şerhi hakîkaten'de ısrar eder: bardak suyu gerçekten tutar. Bâ bâbın geri kalanını alır; defterin listesi Kâfiye'nin kendi örnekleriyle klasik yedidir; ta'diye şerhi bâbın en keskin noktasıdır — lâzım fiili yalnız bâ ettirgen yapar ve ذَهَبْتُ بِزَيْدٍ karşısında ذَهَبْتُ إِلَى زَيْدٍ farkı tek kelimede gösterir. Zâidlik medresenin böldüğü gibi bölünür: kıyasen olan (nefy ya da istifhamdan sonraki üç yer) ve semâen olan (mübtedâ, fâil, mef'ûl), her biri Kur'ânî ya da darb-ı mesel örneğiyle. Bâbdaki her zâid bâ çifte i'rabıyla çözümlenir — lafzen mecrûr, mahallen gerçek görevi — ki bu TaalluqEngine ile SignEngine'in zâid harf için ortak kuralıdır."},
 "examples": [
  {"ar": "أَتِمُّوا الصِّيَامَ إِلَى اللَّيْلِ", "en": "ilā for the end in time.", "tr": "Zamanda intihâ için ilâ.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "سَلَامٌ هِيَ حَتَّى مَطْلَعِ الْفَجْرِ", "en": "ḥattā like ilā.", "tr": "İlâ gibi hattâ.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "الْمَاءُ فِي الْكُوزِ", "en": "fī, the literal container.", "tr": "Hakikî zarf fî.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "اشْتَرَيْتُ الْفَرَسَ بِسَرْجِهِ — بِعْتُ هَذَا بِذَاكَ", "en": "Accompaniment and exchange.", "tr": "Musâhabe ve mukâbele.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "ذَهَبْتُ بِزَيْدٍ — ذَهَبْتُ إِلَى زَيْدٍ", "en": "The bāʾ of transitivity against ilā.", "tr": "Ta'diye bâ'sı ilâ'ya karşı.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "كَفَى بِاللهِ شَهِيدًا — أَلْقَى بِيَدِهِ", "en": "The redundant bāʾ by hearing.", "tr": "Semâen zâid bâ.", "sourceStory": "al-kafiya", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«ذَهَبْتُ إِلَى زَيْدٍ — Zeyd'i götürdüm»",
   "right": "«ذَهَبْتُ بِزَيْدٍ — Zeyd'i götürdüm; ذَهَبْتُ إِلَى زَيْدٍ — Zeyd'e gittim»",
   "why": {"en": "Only the bāʾ adds the sense of ṣayyara to an intransitive verb.", "tr": "Lâzım fiile sayyere mânâsını yalnız bâ katar."}},
  {"wrong": "«حَتَّاهُ»",
   "right": "«حَتَّى زَيْدٍ — hattâ zâhir isme mahsustur (Müberred hariç)»",
   "why": {"en": "The majority bar ḥattā from a pronoun; the notebook names the one dissent.", "tr": "Çoğunluk hattâ'yı zamirden men eder; defter tek muhalifi adlandırır."}},
  {"wrong": "«هَلْ زَيْدٌ بِقَائِمٍ — قَائِمٍ mecrûrdur, haber değildir»",
   "right": "«lafzen mecrûr, mahallen merfû haber — bâ kıyasen zâiddir»",
   "why": {"en": "A redundant letter changes the form, not the office.", "tr": "Zâid harf şekli değiştirir, görevi değil."}},
  {"wrong": "«لَا تَأْكُلُوا أَمْوَالَهُمْ إِلَى أَمْوَالِكُمْ — mallarınıza kadar»",
   "right": "«مَعَ أَمْوَالِكُمْ — mallarınızla birlikte; ilâ burada mea mânâsındadır»",
   "why": {"en": "The notebook records the rare sense and its one Qurʾānic case.", "tr": "Defter nadir mânâyı ve tek Kur'ânî örneğini kaydeder."}}],
 "relatedNotes": ["al-harf-wa-huruf-al-jarr-fil-kafiya", "huruf-jarr", "al-lazim-wal-mutaaddi", "ma-la-laysa-wa-la-al-jins", "haqiqa-majaz"]}

ADD_EN = (" Chapter 30 (notebook lines ~332-333): ilā (4:2), ḥattā (97:5) and al-Mubarrad, fī, and the bāʾ's senses with its redundancy by rule and by hearing (4:79; 5:30-type أَلْقَى بِيَدِهِ) — the notebook's exposition, kept as commentary (s1-s6). Qurʾānic text as the source prints it.")
ADD_TR = (" Otuzuncu bâb (defter satırları ~332-333): ilâ (4:2), hattâ (97:5) ve Müberred, fî ve bâ'nın kıyasen ve semâen zâidliğiyle mânâları (4:79; أَلْقَى بِيَدِهِ) — defterin açıklaması, şerh olarak (s1-s6). Kur'ân metni kaynağın bastığı gibi.")
write_out(30, S, TITLE, ADD_EN, ADD_TR, "332-333", GLOSS_ADD, notes=(NOTE,),
          related=(("al-harf-wa-huruf-al-jarr-fil-kafiya", [K]), ("huruf-jarr", [K])))
report(30, S, GLOSS_ADD, (NOTE,))
