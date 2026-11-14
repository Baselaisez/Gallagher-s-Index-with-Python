# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 33: THE JARR LETTERS (V) — عَنْ for passing-over in its three shapes; عَلَى for being above; both become nouns after
مِنْ; the kāf for likeness, redundant (42:11), «like» after عَنْ in Dhū l-Rumma's half-line, on explicit nouns only (al-Mubarrad);
مُذْ and مُنْذُ for the beginning of past time and containment in the present; حَاشَا، خَلَا، عَدَا for exception — letters when the
noun is majrūr, verbs when it is manṣūb.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~334-336 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch33.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "an-ala-al-kaf-mudh-wa-huruf-al-istithna-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الْجَرِّ: عَنْ وَعَلَى وَالْكَافُ وَمُذْ وَمُنْذُ وَحُرُوفُ الِاسْتِثْنَاءِ", "en": "The jarr letters — ʿan, ʿalā, the kāf, mudh and mundhu, and the exception letters", "tr": "Cer harfleri — an, alâ, kâf, müz ve münzü ve istisnâ harfleri"}
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
def LET(full, lex, en, tr, wa=True, punct=None, pos="prep"):
    if wa: return cited_wa("وَ" + full, lex, pos, ["mubtada-khabar", K, HJ], full + " لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, full, punct=punct)
    return cited(full, lex, pos, ["mubtada-khabar", K, HJ], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, punct=punct)
def FOR(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return li_(full, lex, "noun", ["mubtada-khabar", K] + list(tags), inner + " مَجْرُورٌ — خَبَرٌ.", en, tr, inner, punct=punct, segs=segs)
def QAWM(): return cited("الْقَوْمُ", "qawm", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the people».", "«kavim».")
def JAANI(): return cited("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()])
def EXC_J(full, lex, en, tr): return cited(full, lex, "prep", [K, HJ, "istithna"], "حَرْفُ جَرٍّ لِلِاسْتِثْنَاءِ — لِأَنَّ مَا بَعْدَهُ مَجْرُورٌ.", en, tr)
def EXC_V(full, lex, en, tr): return cited(full, lex, "verb", [K, "istithna"], "فِعْلٌ مَاضٍ جَامِدٌ لِلِاسْتِثْنَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ — لِأَنَّ مَا بَعْدَهُ مَنْصُوبٌ.", en, tr)
def ZJ(punct=None): return cited("زَيْدٍ", "zayd", "propn", [HJ, "istithna"], "مَجْرُورٌ — الْمُسْتَثْنَى.", "«Zayd».", "«Zeyd».", punct=punct)
def ZN(punct=None): return cited("زَيْدًا", "zayd", "propn", ["maful-bihi", "istithna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُسْتَثْنَى.", "«Zayd».", "«Zeyd».", punct=punct)

S.append({"id": "s1", "translation": {
 "en": "عَنْ is for passing-over — a thing's passing beyond another and drawing away from it — and it comes in three shapes: a thing parting from one thing and reaching another, as رَمَيْتُ السَّهْمَ عَنِ الْقَوْسِ إِلَى الصَّيْدِ." + C_EN,
 "tr": "عَنْ mücâveze içindir — bir şeyin başka bir şeyi geçmesi ve ondan uzaklaşması — ve üç şekilde olur: bir şeyin bir şeyden ayrılıp başka bir şeye ulaşmasıyla, رَمَيْتُ السَّهْمَ عَنِ الْقَوْسِ إِلَى الصَّيْدِ gibi." + C_TR},
 "tokens": [
  LET("عَنْ", "an-jarr", "«ʿan».", "«an».", wa=False),
  FOR("لِلْمُجَاوَزَةِ", "mujawaza", "«is for passing-over».", "«mücâveze içindir».", "الْمُجَاوَزَةِ", segs=[seg("لِ", "li", "prep"), seg("لْمُجَاوَزَةِ", "mujawaza", "noun")], punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  W("تَجَاوُزِ", "tajawaza", "noun", ["idafa-definiteness", "form-vi-verbs"], "بَدَلٌ مِنَ الْمُجَاوَزَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ — مَصْدَرُ تَجَاوَزَ.", "«a thing's passing beyond».", "«bir şeyin ... geçmesi»."),
  W("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyin»."),
  W("شَيْئًا", "shay", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", "«another».", "«başka bir şeyi»."),
  atf_wa("وَبُعْدِهِ", "bud-distance", "noun", ["atf-nasaq", "idafa-definiteness"], "بُعْدِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and drawing away».", "«ve uzaklaşması».", "بُعْدِ", extra_segs=[seg("بُعْدِ", "bud-distance", "noun"), pr3msi()]),
  W("عَنْهُ", "an-jarr", "prep", [HJ], "عَنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«from it».", "«ondan».", punct="،", segments=[seg("عَنْ", "an-jarr", "prep"), pr3ms()]),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("عَلَى", "ala", "prep", [HJ, "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«comes in».", "«... üzeredir»."),
  W("ثَلَاثَةِ", "thalatha", "noun", [HJ, "idafa-definiteness", "asma-al-adad-fil-kafiya"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«three».", "«üç»."),
  W("أَوْجُهٍ", "wajh", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ وَجْهٍ.", "«shapes».", "«şekil».", punct=":"),
  bi_("بِانْفِصَالِ", "infisal", "noun", ["idafa-definiteness", "form-vii-verbs"], "انْفِصَالِ مَجْرُورٌ، وَهُوَ مُضَافٌ — بَدَلٌ.", "«a thing parting».", "«ayrılmasıyla».", "انْفِصَالِ"),
  W("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyin»."),
  W("عَنْ", "an-jarr", "prep", [HJ, K], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("شَيْءٍ", "shay", "noun", [HJ], "مَجْرُورٌ.", "«one thing».", "«bir şey»."),
  atf_wa("وَوُصُولِهِ", "wusul", "noun", ["atf-nasaq", "idafa-definiteness"], "وُصُولِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and reaching».", "«ve ulaşmasıyla».", "وُصُولِ", extra_segs=[seg("وُصُولِ", "wusul", "noun"), pr3msi()]),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«-».", "«-e»."),
  W("شَيْءٍ", "shay", "noun", [HJ], "مَجْرُورٌ.", "«another».", "«başka bir şeye»."),
  W("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "صِفَةٌ مَجْرُورَةٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«other».", "«başka».", punct="،"),
  nahwu(),
  cited("رَمَيْتُ", "rama", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I shot».", "«attım».", segments=[seg("رَمَيْ", "rama", "verb"), prT()]),
  cited("السَّهْمَ", "sahm", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the arrow».", "«oku»."),
  cited("عَنِ", "an-jarr", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  cited("الْقَوْسِ", "qaws", "noun", [HJ], "مَجْرُورٌ — الْمُفَارَقُ.", "«the bow».", "«yaydan»."),
  cited("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ لِلِانْتِهَاءِ.", "«toward».", "«-e»."),
  cited("الصَّيْدِ", "sayd", "noun", [HJ], "مَجْرُورٌ — الْمَوْصُولُ إِلَيْهِ.", "«the game».", "«ava».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "Or by reaching the third thing only, as أَخَذْتُ عَنْهُ الْعِلْمَ; or by parting from the second only, as أَدَّيْتُ عَنْهُ الدَّيْنَ." + C_EN,
 "tr": "Ya da yalnız üçüncü şeye ulaşmakla, أَخَذْتُ عَنْهُ الْعِلْمَ gibi; ya da yalnız ikinci şeyden ayrılmakla, أَدَّيْتُ عَنْهُ الدَّيْنَ gibi." + C_TR},
 "tokens": [
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  bi_("بِالْوُصُولِ", "wusul", "noun", ["atf-nasaq"], "الْوُصُولِ مَجْرُورٌ — مَعْطُوفٌ عَلَى بِانْفِصَالِ.", "«by reaching».", "«ulaşmakla».", "الْوُصُولِ"),
  W("إِلَى", "ila", "prep", [HJ], "حَرْفُ جَرٍّ.", "«-».", "«-e»."),
  W("الثَّالِثِ", "thalith", "noun", [HJ], "مَجْرُورٌ.", "«the third».", "«üçüncü şeye»."),
  W("فَقَطْ", "faqat", "adv", ["hal"], "الْفَاءُ زَائِدَةٌ، وَقَطْ اسْمٌ بِمَعْنَى حَسْبُ.", "«only».", "«yalnız».", punct="،"),
  nahwu(),
  cited("أَخَذْتُ", "akhadha", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I took».", "«aldım».", segments=[seg("أَخَذْ", "akhadha", "verb"), prT()]),
  cited("عَنْهُ", "an-jarr", "prep", [K, HJ], "عَنْ حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ، وَالْهَاءُ مَجْرُورٌ — الْعِلْمُ وَصَلَ إِلَيَّ وَلَمْ يُفَارِقْهُ.", "«from him».", "«ondan».", segments=[seg("عَنْ", "an-jarr", "prep"), pr3ms()]),
  cited("الْعِلْمَ", "ilm", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«knowledge».", "«ilim».", punct="؛"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  bi_("بِالِانْفِصَالِ", "infisal", "noun", ["atf-nasaq"], "الِانْفِصَالِ مَجْرُورٌ — مَعْطُوفٌ.", "«by parting».", "«ayrılmakla».", "الِانْفِصَالِ"),
  W("عَنِ", "an-jarr", "prep", [HJ], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  W("الثَّانِي", "thani", "noun", [HJ, "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second».", "«ikinci şeyden»."),
  W("فَقَطْ", "faqat", "adv", ["hal"], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ.", "«only».", "«yalnız».", punct="،"),
  nahwu(),
  cited("أَدَّيْتُ", "adda", "verb", ["fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I paid».", "«ödedim».", segments=[seg("أَدَّيْ", "adda", "verb"), prT()]),
  cited("عَنْهُ", "an-jarr", "prep", [K, HJ], "عَنْ حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ، وَالْهَاءُ مَجْرُورٌ — الدَّيْنُ فَارَقَهُ وَلَمْ يَصِلْ إِلَيَّ.", "«on his behalf».", "«onun yerine».", segments=[seg("عَنْ", "an-jarr", "prep"), pr3ms()]),
  cited("الدَّيْنَ", "dayn", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the debt».", "«borcu».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And عَلَى is for being-above, as الْقَلَمُ عَلَى الْمَكْتَبِ; and when عَنْ and عَلَى come after مِنْ they are nouns — عَنْ in the sense of جَانِب, as مِنْ عَنْ يَمِينِي, that is, مِنْ جَانِبِ يَمِينِي; and عَلَى in the sense of فَوْق, as مِنْ عَلَيْهِ, that is, مِنْ فَوْقِهِ." + C_EN,
 "tr": "عَلَى isti'lâ içindir, الْقَلَمُ عَلَى الْمَكْتَبِ gibi; عَنْ ve عَلَى, مِنْ'den sonra geldiklerinde isim olurlar — عَنْ, جَانِب mânâsında, مِنْ عَنْ يَمِينِي gibi, yani مِنْ جَانِبِ يَمِينِي; عَلَى, فَوْق mânâsında, مِنْ عَلَيْهِ gibi, yani مِنْ فَوْقِهِ." + C_TR},
 "tokens": [
  LET("عَلَى", "ala", "«and ʿalā».", "«ve alâ»."),
  FOR("لِلِاسْتِعْلَاءِ", "istila", "«is for being-above».", "«isti'lâ içindir».", "الِاسْتِعْلَاءِ", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِعْلَاءِ", "istila", "noun")], punct="،"),
  nahwu(),
  cited("الْقَلَمُ", "qalam", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the pen».", "«kalem»."),
  cited("عَلَى", "ala", "prep", [K, HJ, "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ لِلِاسْتِعْلَاءِ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is on».", "«üzerindedir»."),
  cited("الْمَكْتَبِ", "maktab", "noun", [HJ], "مَجْرُورٌ.", "«the desk».", "«yazı masasının».", punct="؛"),
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -diklerinde».", "إِذَا"),
  W("جَاءَتْ", "jaa", "verb", ["idha-shartiyya", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — فِعْلُ الشَّرْطِ.", "«come».", "«geldiklerinde».", segments=[seg("جَاءَ", "jaa", "verb"), seg("تْ", "ta-tanith", "part")]),
  cited("عَنْ", "an-jarr", "prep", ["fail", K], "فِي مَحَلِّ رَفْعٍ فَاعِلٌ — اللَّفْظُ مَحْكِيٌّ.", "«ʿan».", "«an»."),
  cited_wa("وَعَلَى", "ala", "prep", ["fail", K], "عَلَى مَعْطُوفٌ — اللَّفْظُ مَحْكِيٌّ.", "«and ʿalā».", "«ve alâ».", "عَلَى"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonra»."),
  cited("مِنْ", "min", "prep", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«min».", "«min»."),
  W("فَهُمَا", "pron-dual", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart", "al-muthanna"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَهُمَا مُبْتَدَأٌ.", "«they are».", "«ikisi».", segments=[seg("فَ", "fa", "conj"), seg("هُمَا", "pron-dual", "pron")]),
  W("اسْمَانِ", "ism", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«nouns».", "«isim olurlar».", punct="—"),
  cited("عَنْ", "an-jarr", "noun", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«ʿan».", "«an»."),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("جَانِبٍ", "janib", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«side».", "«cânib».", punct="،"),
  nahwu(),
  cited("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.", "«from».", "«-den»."),
  cited("عَنْ", "an-jarr", "noun", [K, HJ, "idafa-definiteness"], "اسْمٌ بِمَعْنَى جَانِبٍ مَجْرُورٌ بِمِنْ، وَهُوَ مُضَافٌ.", "«the side of».", "«tarafından»."),
  cited("يَمِينِي", "yamin", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my right».", "«sağımın».", punct="،", segments=[seg("يَمِينِ", "yamin", "noun"), seg("ي", "pron-1s", "pron")]),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("جَانِبِ", "janib", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the side of».", "«tarafından»."),
  cited("يَمِينِي", "yamin", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my right».", "«sağımın».", punct="؛", segments=[seg("يَمِينِ", "yamin", "noun"), seg("ي", "pron-1s", "pron")]),
  cited_wa("وَعَلَى", "ala", "noun", ["mubtada-khabar", K], "عَلَى لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and ʿalā».", "«ve alâ».", "عَلَى"),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("فَوْقٍ", "fawqa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«above».", "«fevk».", punct="،"),
  nahwu(),
  cited("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.", "«from».", "«-den»."),
  cited("عَلَيْهِ", "ala", "noun", [K, HJ, "idafa-definiteness"], "اسْمٌ بِمَعْنَى فَوْقٍ مَجْرُورٌ بِمِنْ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«above him».", "«üstünden».", punct="،", segments=[seg("عَلَيْ", "ala", "noun"), pr3msi()]),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("فَوْقِهِ", "fawqa", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«above him».", "«üstünden».", punct=".", segments=[seg("فَوْقِ", "fawqa", "noun"), pr3msi()]),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the kāf is for likeness, as زَيْدٌ كَالْأَسَدِ; and redundant, as لَيْسَ كَمِثْلِهِ شَيْءٌ; and when it comes after عَنْ it is in the sense of مِثْل, as يَضْحَكْنَ عَنْ كَالْبَرَدِ الْمُنْهَمِّ; and it is confined to the explicit noun, though al-Mubarrad allowed it on a pronoun." + C_EN,
 "tr": "Kâf teşbih içindir, زَيْدٌ كَالْأَسَدِ gibi; zâid olur, لَيْسَ كَمِثْلِهِ شَيْءٌ gibi; عَنْ'den sonra gelirse مِثْل mânâsındadır, يَضْحَكْنَ عَنْ كَالْبَرَدِ الْمُنْهَمِّ gibi; zâhir isme mahsustur, fakat Müberred zamir üzerine girmesine cevaz verdi." + C_TR},
 "tokens": [
  atf_wa("وَالْكَافُ", "kaf-letter", "noun", ["mubtada-khabar", K, HJ], "الْكَافُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the kāf».", "«ve kâf».", "الْكَافُ"),
  FOR("لِلتَّشْبِيهِ", "tashbih", "«is for likeness».", "«teşbih içindir».", "التَّشْبِيهِ", segs=[seg("لِ", "li", "prep"), seg("لتَّشْبِيهِ", "tashbih", "noun")], punct="،", tags=["tashbih"]),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — الْمُشَبَّهُ.", "«Zayd».", "«Zeyd»."),
  ka_("كَالْأَسَدِ", "asad", "noun", [K, "tashbih", "khabar-al-mubtada-wa-ahkamuh"], "الْأَسَدِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ؛ الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is like the lion».", "«aslan gibidir».", "الْأَسَدِ", punct="؛"),
  atf_wa("وَزَائِدَةً", "zaid", "noun", ["hal", K], "زَائِدَةً حَالٌ.", "«and redundant».", "«ve zâid olur».", "زَائِدَةً", punct="،"),
  nahwu(),
  cited("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«there is not».", "«yoktur»."),
  ka_("كَمِثْلِهِ", "mithl", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness"], "الْكَافُ زَائِدَةٌ، وَمِثْلِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ لَيْسَ مُقَدَّمٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«like Him».", "«O'nun benzeri».", "مِثْلِ", segs=[seg("كَ", "ka", "part"), seg("مِثْلِ", "mithl", "noun"), pr3msi()]),
  cited("شَيْءٌ", "shay", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ.", "«anything».", "«hiçbir şey».", punct="؛"),
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -se».", "إِذَا"),
  W("جَاءَتْ", "jaa", "verb", ["idha-shartiyya", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«it comes».", "«gelirse».", segments=[seg("جَاءَ", "jaa", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonra»."),
  cited("عَنْ", "an-jarr", "prep", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«ʿan».", "«an»."),
  W("فَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَهِيَ مُبْتَدَأٌ.", "«it is».", "«o»."),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«in the sense of».", "«mânâsındadır».", "مَعْنَى"),
  cited("مِثْلٍ", "mithl", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«mithl».", "«misl».", punct="،"),
  nahwu(),
  cited("يَضْحَكْنَ", "dahika", "verb", ["fail", "al-mabni-wal-mudmar"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ فَاعِلٌ.", "«they (the women) laugh».", "«gülüyorlar».", segments=[seg("يَضْحَكْ", "dahika", "verb"), seg("نَ", "nun-niswa", "pron")]),
  cited("عَنْ", "an-jarr", "prep", [K, HJ], "حَرْفُ جَرٍّ — يَكْشِفْنَ عَنْ ثَغْرٍ.", "«baring».", "«... dişlerinden»."),
  ka_("كَالْبَرَدِ", "barad", "noun", [K, HJ, "tashbih"], "الْكَافُ اسْمٌ بِمَعْنَى مِثْلٍ مَجْرُورٌ بِعَنْ، وَهُوَ مُضَافٌ؛ الْبَرَدِ مُضَافٌ إِلَيْهِ.", "«the like of hail».", "«dolu gibi».", "الْبَرَدِ", segs=[seg("كَ", "ka", "noun"), seg("الْبَرَدِ", "barad", "noun")]),
  cited("الْمُنْهَمِّ", "munhamm", "noun", ["naat-sifa", "ism-fail", "form-vii-verbs", "doubled-verbs"], "صِفَةٌ مَجْرُورَةٌ — اسْمُ فَاعِلٍ مِنِ انْهَمَّ: ذَابَ وَسَالَ.", "«melting».", "«erimiş».", punct="؛"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("مُخْتَصَّةٌ", "mukhtass", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is confined».", "«mahsustur»."),
  bi_("بِالِاسْمِ", "ism", "noun", [], "الِاسْمِ مَجْرُورٌ.", "«to the noun».", "«isme».", "الِاسْمِ"),
  W("الظَّاهِرِ", "zahir", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«explicit».", "«zâhir».", punct="،"),
  atf_wa("وَجَوَّزَ", "jawwaza", "verb", ["fail", "form-ii-verbs"], "جَوَّزَ فِعْلٌ مَاضٍ.", "«though … allowed».", "«fakat ... cevaz verdi».", "جَوَّزَ"),
  W("الْمُبَرِّدُ", "mubarrad", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Mubarrad».", "«Müberred»."),
  W("دُخُولَهَا", "dukhul", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its entering».", "«girmesine».", segments=[seg("دُخُولَ", "dukhul", "noun"), pr3fs()]),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الضَّمِيرِ", "damir", "noun", [HJ, "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«a pronoun».", "«zamir».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And مُذْ and مُنْذُ are for the beginning in past time and for containment in present time: in مَا رَأَيْتُهُ مُذْ شَهْرِنَا, مُذْ is for beginning with a muḍāf supplied — مُذْ دُخُولِ شَهْرِنَا, «since our month came in» — and it is also for containment, «within our month»; and in مَا رَأَيْتُهُ مُنْذُ يَوْمِنَا, مُنْذُ is for containment." + C_EN,
 "tr": "مُذْ ve مُنْذُ, mâzî zamanda ibtidâ, hâl zamanında zarfiyet içindir: مَا رَأَيْتُهُ مُذْ شَهْرِنَا'da مُذْ, muzâf takdiriyle ibtidâ içindir — مُذْ دُخُولِ شَهْرِنَا, «ayımız gireli» — ve zarfiyet için de olur, «bu ay içinde»; مَا رَأَيْتُهُ مُنْذُ يَوْمِنَا'da مُنْذُ zarfiyet içindir." + C_TR},
 "tokens": [
  LET("مُذْ", "mudh", "«and mudh».", "«ve müz»."),
  cited_wa("وَمُنْذُ", "mundhu", "prep", ["mubtada-khabar", K, HJ], "مُنْذُ مَعْطُوفٌ — اللَّفْظُ مَحْكِيٌّ.", "«and mundhu».", "«ve münzü».", "مُنْذُ"),
  FOR("لِلِابْتِدَاءِ", "ibtida-start", "«are for the beginning».", "«ibtidâ içindir».", "الِابْتِدَاءِ", segs=[seg("لِ", "li", "prep"), seg("لِابْتِدَاءِ", "ibtida-start", "noun")]),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الزَّمَانِ", "zaman", "noun", [HJ], "مَجْرُورٌ.", "«time».", "«zamanda»."),
  W("الْمَاضِي", "madi", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«past».", "«mâzî»."),
  atf_wa("وَلِلظَّرْفِيَّةِ", "zarfiyya", "noun", ["atf-nasaq", K], "اللَّامُ حَرْفُ جَرٍّ، وَالظَّرْفِيَّةِ مَجْرُورٌ — مَعْطُوفٌ عَلَى الْخَبَرِ.", "«and for containment».", "«ve zarfiyet içindir».", "الظَّرْفِيَّةِ", extra_segs=[seg("لِ", "li", "prep"), seg("لظَّرْفِيَّةِ", "zarfiyya", "noun")]),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الزَّمَانِ", "zaman", "noun", [HJ], "مَجْرُورٌ.", "«time».", "«zamanında»."),
  W("الْحَاضِرِ", "hadir", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«present».", "«hâl».", punct=":"),
  W("فَفِي", "fi", "prep", [HJ, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«in».", "«-da».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  cited("مَا", "ma-nafiya", "part", [HJ, "anwa-ma", "la-nafiya"], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — مَا نَافِيَةٌ.", "«not».", "«-medim»."),
  cited("رَأَيْتُهُ", "raa", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«have I seen him».", "«onu görmedim».", segments=[seg("رَأَيْ", "raa", "verb"), prT(), pr3ms()]),
  cited("مُذْ", "mudh", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«since».", "«-den beri»."),
  cited("شَهْرِنَا", "shahr", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our month».", "«ayımız».", punct="،", segments=[seg("شَهْرِ", "shahr", "noun"), seg("نَا", "pron-1p", "pron")]),
  cited("مُذْ", "mudh", "prep", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«mudh».", "«müz»."),
  li_("لِلِابْتِدَاءِ", "ibtida-start", "noun", ["mubtada-khabar", K], "الِابْتِدَاءِ مَجْرُورٌ — خَبَرٌ.", "«is for beginning».", "«ibtidâ içindir».", "الِابْتِدَاءِ", segs=[seg("لِ", "li", "prep"), seg("لِابْتِدَاءِ", "ibtida-start", "noun")]),
  bi_("بِتَقْدِيرِ", "taqdir", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"], "تَقْدِيرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«with … supplied».", "«... takdiriyle».", "تَقْدِيرِ"),
  W("مُضَافٍ", "mudaf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a muḍāf».", "«bir muzâf».", punct="—"),
  cited("مُذْ", "mudh", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«since».", "«-den beri»."),
  cited("دُخُولِ", "dukhul", "noun", [HJ, "idafa-definiteness", "hadhf-wa-taqdir"], "مَجْرُورٌ، وَهُوَ مُضَافٌ — الْمُضَافُ الْمُقَدَّرُ.", "«the coming in of».", "«girmesinden»."),
  cited("شَهْرِنَا", "shahr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our month».", "«ayımızın».", punct="،", segments=[seg("شَهْرِ", "shahr", "noun"), seg("نَا", "pron-1p", "pron")]),
  atf_wa("وَلِلظَّرْفِيَّةِ", "zarfiyya", "noun", ["atf-nasaq", K], "اللَّامُ حَرْفُ جَرٍّ، وَالظَّرْفِيَّةِ مَجْرُورٌ — مَعْطُوفٌ.", "«and also for containment».", "«ve zarfiyet için de».", "الظَّرْفِيَّةِ", extra_segs=[seg("لِ", "li", "prep"), seg("لظَّرْفِيَّةِ", "zarfiyya", "noun")]),
  W("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ.", "«too».", "«de».", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ — التَّقْدِيرُ.", "«within».", "«içinde»."),
  cited("شَهْرِنَا", "shahr", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our month».", "«ayımız».", punct="؛", segments=[seg("شَهْرِ", "shahr", "noun"), seg("نَا", "pron-1p", "pron")]),
  atf_wa("وَفِي", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -da».", "فِي"),
  cited("مَا", "ma-nafiya", "part", [HJ, "anwa-ma"], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — مَا نَافِيَةٌ.", "«not».", "«-medim»."),
  cited("رَأَيْتُهُ", "raa", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«have I seen him».", "«onu görmedim».", segments=[seg("رَأَيْ", "raa", "verb"), prT(), pr3ms()]),
  cited("مُنْذُ", "mundhu", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«during».", "«-de»."),
  cited("يَوْمِنَا", "yawm", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our day».", "«günümüz».", punct="،", segments=[seg("يَوْمِ", "yawm", "noun"), seg("نَا", "pron-1p", "pron")]),
  cited("مُنْذُ", "mundhu", "prep", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«mundhu».", "«münzü»."),
  li_("لِلظَّرْفِيَّةِ", "zarfiyya", "noun", ["mubtada-khabar", K], "الظَّرْفِيَّةِ مَجْرُورٌ — خَبَرٌ.", "«is for containment».", "«zarfiyet içindir».", "الظَّرْفِيَّةِ", segs=[seg("لِ", "li", "prep"), seg("لظَّرْفِيَّةِ", "zarfiyya", "noun")], punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And حَاشَا, خَلَا and عَدَا are for exception — they except what follows them from what precedes; and they are jarr letters if we read the noun after them in jarr, and verbs if we read it in naṣb." + C_EN,
 "tr": "حَاشَا, خَلَا ve عَدَا istisnâ içindir — kendilerinden sonra geleni öncekilerden istisnâ ederler; ardlarındaki ismi cer okursak cer harfi, nasb okursak fiil olurlar." + C_TR},
 "tokens": [
  LET("حَاشَا", "hasha", "«and ḥāshā».", "«ve hâşâ».", pos="part"),
  cited_wa("وَخَلَا", "khala-except", "part", ["mubtada-khabar", K, HJ], "خَلَا مَعْطُوفٌ — اللَّفْظُ مَحْكِيٌّ.", "«khalā».", "«halâ».", "خَلَا"),
  cited_wa("وَعَدَا", "ada-except", "part", ["mubtada-khabar", K, HJ], "عَدَا مَعْطُوفٌ — اللَّفْظُ مَحْكِيٌّ.", "«and ʿadā».", "«ve adâ».", "عَدَا"),
  FOR("لِلِاسْتِثْنَاءِ", "istithna", "«are for exception».", "«istisnâ içindir».", "الِاسْتِثْنَاءِ", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِثْنَاءِ", "istithna", "noun")], punct="،", tags=["istithna"]),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  W("تُخْرِجُ", "akhraja", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they except».", "«çıkarırlar»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what».", "«... -i»."),
  W("بَعْدَهَا", "bada", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — صِلَةٌ.", "«follows them».", "«kendilerinden sonra geleni».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("مِمَّا", "ma-mawsula", "pron", [HJ, "ism-mawsul", "anwa-ma"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«from what».", "«... -den».", segments=[seg("مِنْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("قَبْلَهَا", "qabla", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — صِلَةٌ.", "«precedes».", "«öncekilerden».", punct="؛", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and they».", "«ve onlar».", "هِيَ"),
  W("حُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«are letters of».", "«harfidir»."),
  W("جَرٍّ", "jarr", "noun", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer»."),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-sak»."),
  W("قَرَأْنَا", "qaraa", "verb", ["in-shartiyya", "fail"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَنَا فَاعِلٌ.", "«we read».", "«okursak».", segments=[seg("قَرَأْ", "qaraa", "verb"), seg("نَا", "pron-1p", "pron")]),
  W("الِاسْمَ", "ism", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the noun».", "«ismi»."),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«after them».", "«ardlarındaki».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  bi_("بِالْجَرِّ", "jarr", "noun", [HJ], "الْجَرِّ مَجْرُورٌ.", "«in jarr».", "«cer ile».", "الْجَرِّ", punct="،"),
  atf_wa("وَأَفْعَالٌ", "fil", "noun", ["mubtada-khabar", "jam-taksir"], "أَفْعَالٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ.", "«and verbs».", "«ve fiildir».", "أَفْعَالٌ"),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-sak»."),
  W("قَرَأْنَاهُ", "qaraa", "verb", ["in-shartiyya", "fail", "maful-bihi"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«we read it».", "«onu okursak».", segments=[seg("قَرَأْ", "qaraa", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  bi_("بِالنَّصْبِ", "nasb", "noun", [], "النَّصْبِ مَجْرُورٌ.", "«in naṣb».", "«nasb ile».", "النَّصْبِ", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "As جَاءَنِي الْقَوْمُ حَاشَا زَيْدٍ, خَلَا زَيْدٍ, عَدَا زَيْدٍ; and جَاءَنِي الْقَوْمُ حَاشَا زَيْدًا, خَلَا زَيْدًا, عَدَا زَيْدًا." + C_EN,
 "tr": "جَاءَنِي الْقَوْمُ حَاشَا زَيْدٍ, خَلَا زَيْدٍ, عَدَا زَيْدٍ gibi; ve جَاءَنِي الْقَوْمُ حَاشَا زَيْدًا, خَلَا زَيْدًا, عَدَا زَيْدًا gibi." + C_TR},
 "tokens": [
  nahwu(),
  JAANI(), QAWM(),
  EXC_J("حَاشَا", "hasha", "«except».", "«hariç»."), ZJ(punct="،"),
  EXC_J("خَلَا", "khala-except", "«except».", "«hariç»."), ZJ(punct="،"),
  EXC_J("عَدَا", "ada-except", "«except».", "«hariç»."), ZJ(punct="؛"),
  cited_wa("وَجَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and came to me».", "«ve bana geldi».", "جَاءَنِي", extra_segs=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  QAWM(),
  EXC_V("حَاشَا", "hasha", "«except».", "«hariç»."), ZN(punct="،"),
  EXC_V("خَلَا", "khala-except", "«except».", "«hariç»."), ZN(punct="،"),
  EXC_V("عَدَا", "ada-except", "«except».", "«hariç»."), ZN(punct="."),
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
 "sayd": need("sayd", "صَيْد", "ص ي د", "noun", "game, quarry (what is hunted)", "av (avlanan şey)", 3),
 "maktab": need("maktab", "مَكْتَب", "ك ت ب", "noun", "a writing-desk (ism makān of كَتَبَ)", "yazı masası (ketebe'nin ism-i mekânı)", 2),
 "munhamm": need("munhamm", "مُنْهَمّ", "ه م م", "noun", "melting, running (of hail) — the Form VII ism fāʿil of انْهَمَّ", "eriyen, akan (dolu için) — inhemme'nin ism-i fâili", 5),
 "tajawaza": need("tajawaza", "تَجَاوُز", "ج و ز", "noun", "passing beyond — the maṣdar of تَجَاوَزَ", "aşma, geçme — tecâveze'nin masdarı", 4),
 "infisal": need("infisal", "انْفِصَال", "ف ص ل", "noun", "separation, parting — the maṣdar of انْفَصَلَ", "ayrılma — infesale'nin masdarı", 4),
 "wusul": need("wusul", "وُصُول", "و ص ل", "noun", "arrival, reaching — the maṣdar of وَصَلَ", "ulaşma, varma — vasale'nin masdarı", 3),
 "nun-niswa": need("nun-niswa", "نَ (نُونُ النِّسْوَةِ)", "ن", "pron", "the nūn of the women — the feminine-plural subject pronoun that builds the verb on sukūn", "nisve nûnu — fiili sükûn üzere mebnî kılan müennes cemi fâil zamiri", 4),
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
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch33 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "عَنْ وَعَلَى وَالْكَافُ وَمُذْ وَمُنْذُ وَحُرُوفُ الِاسْتِثْنَاءِ فِي الْكَافِيَةِ", "en": "ʿan, ʿalā, the kāf, mudh/mundhu and the exception letters in the Kafiya: passing-over in three shapes, being-above, the two that turn into nouns after min, the kāf's three uses, time since and time within, and letters that become verbs", "tr": "Kâfiye'de an, alâ, kâf, müz/münzü ve istisnâ harfleri: üç şekliyle mücâveze, isti'lâ, min'den sonra isme dönen ikisi, kâfın üç kullanımı, -den beri ve içinde, fiile dönen harfler"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — عن للمجاوزة؛ على للاستعلاء؛ وهما اسمان بعد من؛ الكاف للتشبيه وزائدة وبمعنى مثل؛ مذ ومنذ؛ حاشا وخلا وعدا للاستثناء", "ضياء صونغور اوغلى — دفتر الكافية: أوجه المجاوزة الثلاثة؛ القلم على المكتب؛ من عن يميني ومن عليه؛ ليس كمثله شيء؛ يضحكن عن كالبرد المنهم؛ المبرد؛ ما رأيته مذ شهرنا ومنذ يومنا؛ حاشا زيد وحاشا زيدا"],
 "question": {
  "en": ["What is ʿan? The letter of passing beyond — something leaves one point and the letter marks it. The notebook finds three shapes and gives each its sentence: leave-and-reach (the arrow from the bow to the game), reach-only (knowledge taken from a teacher — it reaches you and does not leave him), leave-only (a debt paid on someone's behalf — it leaves him and reaches no one).",
         "And ʿalā? Being above: the pen on the desk. Then the surprise both letters share — after min they stop being letters: مِنْ عَنْ يَمِينِي means «from the side of my right» and مِنْ عَلَيْهِ «from above him». A letter cannot be governed by min; a noun can.",
         "What does the kāf do? Likeness (زَيْدٌ كَالْأَسَدِ); nothing at all in لَيْسَ كَمِثْلِهِ شَيْءٌ, where it is redundant so that the verse does not say God has a like; and «the like of» as a noun after ʿan in Dhū l-Rumma's يَضْحَكْنَ عَنْ كَالْبَرَدِ. It takes an explicit noun only — al-Mubarrad, once more, allows the pronoun.",
         "How do mudh and mundhu differ? They do not, in sense: both mark the start of a past span or the inside of a present one. مَا رَأَيْتُهُ مُذْ شَهْرِنَا is «since our month began» (a muḍāf supplied) or «within this month»; مَا رَأَيْتُهُ مُنْذُ يَوْمِنَا is «within today». What is understood is a muḍāf, and the HadhfEngine names it.",
         "Why are ḥāshā, khalā and ʿadā in two chapters? Because they are two words each: with the noun in jarr they are letters of exception, with it in naṣb they are verbs whose hidden doer is «it». The reader decides by the last vowel, and the SignEngine reads that vowel and names the class.",
         "What does the engine do? The PARTICLES table holds all five with their restrictions; the analyzer reclassifies ʿan and ʿalā as nouns when min precedes; the kāf's redundant face is read from لَيْسَ; and the exception trio is classed letter or verb from the ending of the next word."],
  "tr": ["An nedir? Aşma harfi — bir şey bir noktadan ayrılır ve harf bunu işaretler. Defter üç şekil bulur ve her birine cümlesini verir: ayrıl-ve-ulaş (yaydan ava ok), yalnız ulaş (hocadan alınan ilim — sana ulaşır, ondan ayrılmaz), yalnız ayrıl (birinin yerine ödenen borç — ondan ayrılır, kimseye ulaşmaz).",
         "Ya alâ? Üstte olma: masanın üstündeki kalem. Sonra iki harfin paylaştığı sürpriz — min'den sonra harf olmaktan çıkarlar: مِنْ عَنْ يَمِينِي «sağ tarafımdan», مِنْ عَلَيْهِ «üstünden» demektir. Bir harf min'in ma'mûlü olamaz; bir isim olabilir.",
         "Kâf ne yapar? Teşbih (زَيْدٌ كَالْأَسَدِ); لَيْسَ كَمِثْلِهِ شَيْءٌ'de hiçbir şey — âyet Allah'ın benzeri var demesin diye zâiddir; ve Zü'r-Rumme'nin يَضْحَكْنَ عَنْ كَالْبَرَدِ'inde an'dan sonra isim olarak «benzeri». Yalnız zâhir isim alır — Müberred, yine, zamire izin verir.",
         "Müz ile münzü nasıl ayrılır? Mânâda ayrılmaz: ikisi de geçmiş bir sürenin başını ya da şimdiki bir sürenin içini işaretler. مَا رَأَيْتُهُ مُذْ شَهْرِنَا «ayımız başlayalı» (muzâf takdir edilir) ya da «bu ay içinde»; مَا رَأَيْتُهُ مُنْذُ يَوْمِنَا «bugün içinde». Takdir edilen bir muzâftır ve HadhfEngine onu adlandırır.",
         "Hâşâ, halâ ve adâ neden iki bâbda? Çünkü her biri iki kelimedir: isim cerdeyse istisnâ harfi, nasbdaysa gizli fâili «o» olan fiil. Okuyucu son harekeyle karar verir; SignEngine o harekeyi okur ve sınıfı adlandırır.",
         "Motor ne yapar? PARTICLES tablosu beşini kayıtlarıyla tutar; analizör min öncelediğinde an ve alâ'yı isim olarak yeniden sınıflar; kâfın zâid yüzü لَيْسَ'den okunur; istisnâ üçlüsü sonraki kelimenin sonundan harf ya da fiil sayılır."]},
 "plain": {
  "en": "ʿAn means «away from», ʿalā «on», and after «from» both become nouns. The kāf means «like», says nothing in «there is nothing like Him», and after ʿan means «the like of». Mudh and mundhu say «since» or «within». Ḥāshā, khalā and ʿadā mean «except» and are letters or verbs by the vowel that follows.",
  "tr": "An «-den uzağa», alâ «üstünde» demektir; «-den»den sonra ikisi de isim olur. Kâf «gibi» demektir, «O'nun benzeri yoktur»da hiçbir şey söylemez, an'dan sonra «benzeri» demektir. Müz ve münzü «-den beri» ya da «içinde» der. Hâşâ, halâ ve adâ «hariç» demektir; ardındaki harekeye göre harf ya da fiildir."},
 "explanation": {
  "en": "The last five letters of the Kafiya's list, in the notebook's order. ʿAn is defined by passing-over and then analysed into three shapes by whether the thing leaves its source, reaches its goal, or both — a small piece of semantics the notebook makes mechanical with three sentences. ʿAlā is given in one line, and the rule that follows it is the chapter's most useful: after min, ʿan and ʿalā are nouns, because a letter cannot be governed. The kāf has its three uses, and the notebook keeps the Qurʾānic case honest: the kāf in لَيْسَ كَمِثْلِهِ شَيْءٌ is redundant, so the verse denies a like, not a like of a like. Mudh and mundhu are explained by what is understood: a beginning needs a muḍāf (دُخُولِ شَهْرِنَا), containment does not. The exception trio closes the chapter with the Kafiya's own criterion: jarr after them makes them letters, naṣb makes them verbs — the same word read two ways by one vowel, and both readings are stored side by side in the last sentence.",
  "tr": "Kâfiye listesinin son beş harfi, defterin sırasıyla. An mücâveze ile tarif edilir, sonra şeyin kaynağından ayrılıp ayrılmadığına, hedefine ulaşıp ulaşmadığına ya da ikisine göre üç şekle ayrılır — defterin üç cümleyle mekanik kıldığı küçük bir anlam parçası. Alâ tek satırda verilir ve ardından gelen kural bâbın en faydalısıdır: min'den sonra an ve alâ isimdir, çünkü bir harf yönetilemez. Kâfın üç kullanımı vardır ve defter Kur'ânî örneği dürüst tutar: لَيْسَ كَمِثْلِهِ شَيْءٌ'deki kâf zâiddir, dolayısıyla âyet benzeri reddeder, benzerin benzerini değil. Müz ve münzü takdir edilenle açıklanır: ibtidâ bir muzâf ister (دُخُولِ شَهْرِنَا), zarfiyet istemez. İstisnâ üçlüsü bâbı Kâfiye'nin kendi ölçütüyle kapar: ardlarında cer onları harf, nasb fiil yapar — tek harekeyle iki türlü okunan aynı kelime; son cümlede iki okuyuş yan yana saklanır."},
 "examples": [
  {"ar": "رَمَيْتُ السَّهْمَ عَنِ الْقَوْسِ إِلَى الصَّيْدِ", "en": "ʿan: leave and reach.", "tr": "An: ayrıl ve ulaş.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "أَخَذْتُ عَنْهُ الْعِلْمَ — أَدَّيْتُ عَنْهُ الدَّيْنَ", "en": "ʿan: reach only, leave only.", "tr": "An: yalnız ulaş, yalnız ayrıl.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "مِنْ عَنْ يَمِينِي — مِنْ عَلَيْهِ", "en": "ʿan and ʿalā as nouns after min.", "tr": "Min'den sonra isim olarak an ve alâ.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "لَيْسَ كَمِثْلِهِ شَيْءٌ — يَضْحَكْنَ عَنْ كَالْبَرَدِ الْمُنْهَمِّ", "en": "The redundant kāf and the kāf as a noun.", "tr": "Zâid kâf ve isim olarak kâf.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "مَا رَأَيْتُهُ مُذْ شَهْرِنَا — مُنْذُ يَوْمِنَا", "en": "Since and within.", "tr": "-den beri ve içinde.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "جَاءَنِي الْقَوْمُ حَاشَا زَيْدٍ — حَاشَا زَيْدًا", "en": "Letter with jarr, verb with naṣb.", "tr": "Cerle harf, nasbla fiil.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«مِنْ عَنْ يَمِينِي — iki cer harfi üst üste»",
   "right": "«عَنْ burada جَانِب mânâsında isimdir ve min ile mecrûrdur»",
   "why": {"en": "A letter cannot be governed; after min the word is a noun.", "tr": "Harf yönetilemez; min'den sonra kelime isimdir."}},
  {"wrong": "«لَيْسَ كَمِثْلِهِ شَيْءٌ — O'nun benzerinin benzeri yoktur»",
   "right": "«kâf zâiddir: O'nun benzeri yoktur»",
   "why": {"en": "The redundant kāf adds no second likeness.", "tr": "Zâid kâf ikinci bir benzerlik katmaz."}},
  {"wrong": "«مَا رَأَيْتُهُ مُذْ شَهْرِنَا — ayımızdan beri (muzâfsız)»",
   "right": "«مُذْ دُخُولِ شَهْرِنَا — ibtidâ için bir muzâf takdir edilir»",
   "why": {"en": "A span cannot begin at a month; it begins at the month's coming in.", "tr": "Bir süre ayda başlamaz; ayın girmesinde başlar."}},
  {"wrong": "«حَاشَا زَيْدًا — cer harfi»",
   "right": "«nasb ile حَاشَا fiildir; cer ile حَاشَا زَيْدٍ harftir»",
   "why": {"en": "The vowel after the word decides its class.", "tr": "Kelimeden sonraki hareke sınıfını belirler."}}],
 "relatedNotes": ["huruf-al-qasam-fil-kafiya", "huruf-jarr", "huruf-jarr-nawadir", "istithna", "tashbih"]}

ADD_EN = (" Chapter 33 (notebook lines ~334-336): ʿan's three shapes, ʿalā, the two as nouns after min, the kāf (42:11; Dhū l-Rumma's half-line), mudh/mundhu, and ḥāshā/khalā/ʿadā as letters or verbs — the notebook's exposition, kept as commentary (s1-s7). Qurʾānic text as the source prints it.")
ADD_TR = (" Otuz üçüncü bâb (defter satırları ~334-336): an'ın üç şekli, alâ, min'den sonra isim olarak ikisi, kâf (42:11; Zü'r-Rumme'nin mısraı), müz/münzü ve harf ya da fiil olarak hâşâ/halâ/adâ — defterin açıklaması, şerh olarak (s1-s7). Kur'ân metni kaynağın bastığı gibi.")
write_out(33, S, TITLE, ADD_EN, ADD_TR, "334-336", GLOSS_ADD, notes=(NOTE,),
          related=(("huruf-al-qasam-fil-kafiya", [K]), ("istithna", [K])))
report(33, S, GLOSS_ADD, (NOTE,))
