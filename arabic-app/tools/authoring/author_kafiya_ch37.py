# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 37: THE COORDINATION LETTERS (I) — the ten; the first four for absolute joining; the wāw without order, the fāʾ
with order and no delay, ثُمَّ with order and delay, حَتَّى with order and delay and a part of its whole (مَاتَ النَّاسُ حَتَّى
الْأَنْبِيَاءُ); the two differences between حَتَّى and ثُمَّ — the part condition, and the delay real in ثُمَّ but only in the mind in
حَتَّى (قَدِمَ الْحُجَّاجُ حَتَّى الْمُشَاةُ).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~341-342 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch37.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "huruf-al-atf-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الْعَطْفِ: الْوَاوُ وَالْفَاءُ وَثُمَّ وَحَتَّى", "en": "The coordination letters — the wāw, the fāʾ, thumma and ḥattā", "tr": "Atıf harfleri — vâv, fâ, sümme ve hattâ"}
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

AT = "atf-nasaq"
def LET(full, lex, en, tr, wa=True, punct=None, pos="conj"):
    if wa: return cited_wa("وَ" + full, lex, pos, ["mubtada-khabar", K, AT], full + " لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, full, punct=punct)
    return cited(full, lex, pos, ["mubtada-khabar", K, AT], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, punct=punct)
def LN(full, lex, en, tr, inner, punct=None, extra=None):
    return cited_wa("وَ" + full, lex, "noun", [K, AT], full + " مَعْطُوفٌ مَرْفُوعٌ — اسْمُ الْحَرْفِ.", en, tr, inner, punct=punct, extra_segs=extra)
def FOR(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return li_(full, lex, "noun", ["mubtada-khabar", K] + list(tags), inner + " مَجْرُورٌ — خَبَرٌ.", en, tr, inner, punct=punct, segs=segs)
def JAANI(): return cited("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()])
def ZAYD_F(): return cited("زَيْدٌ", "zayd", "propn", ["fail", AT], "فَاعِلٌ مَرْفُوعٌ — الْمَعْطُوفُ عَلَيْهِ.", "«Zayd».", "«Zeyd».")
def AMR_M(letter_ar, en, tr, punct="."): return cited("عَمْرٌو", "amr-name", "propn", [K, AT], "مَعْطُوفٌ عَلَى زَيْدٌ مَرْفُوعٌ — " + letter_ar, en, tr, punct=punct)

S.append({"id": "s1", "translation": {
 "en": "The letters of coordination: the wāw, the fāʾ, ثُمَّ, حَتَّى, أَوْ, إِمَّا, أَمْ, لَا, بَلْ and لَكِنْ; and the first four are for absolute joining." + C_EN,
 "tr": "Atıf harfleri: vâv, fâ, ثُمَّ, حَتَّى, أَوْ, إِمَّا, أَمْ, لَا, بَلْ ve لَكِنْ'dir; ilk dördü mutlak cem' içindir." + C_TR},
 "tokens": [
  W("حُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harfleri»."),
  W("الْعَطْفِ", "atf", "noun", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«coordination».", "«atıf».", punct=":"),
  cited("الْوَاوُ", "waw-letter", "noun", ["mubtada-khabar", K, AT, "anwa-al-waw"], "خَبَرٌ — اسْمُ الْحَرْفِ.", "«the wāw».", "«vâv»."),
  LN("الْفَاءُ", "fa-letter", "«the fāʾ».", "«fâ».", "الْفَاءُ"),
  cited_wa("وَثُمَّ", "thumma", "conj", [K, AT], "ثُمَّ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«thumma».", "«sümme».", "ثُمَّ"),
  cited_wa("وَحَتَّى", "hatta", "conj", [K, AT], "حَتَّى مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«ḥattā».", "«hattâ».", "حَتَّى"),
  cited_wa("وَأَوْ", "aw", "conj", [K, AT], "أَوْ مَعْطُوفٌ.", "«aw».", "«ev».", "أَوْ"),
  cited_wa("وَإِمَّا", "imma", "part", [K, AT], "إِمَّا مَعْطُوفٌ.", "«immā».", "«immâ».", "إِمَّا"),
  cited_wa("وَأَمْ", "am", "part", [K, AT], "أَمْ مَعْطُوفٌ.", "«am».", "«em».", "أَمْ"),
  cited_wa("وَلَا", "la-nafiya", "part", [K, AT], "لَا مَعْطُوفٌ — لَا الْعَاطِفَةُ.", "«lā».", "«lâ».", "لَا"),
  cited_wa("وَبَلْ", "bal", "conj", [K, AT], "بَلْ مَعْطُوفٌ.", "«bal».", "«bel».", "بَلْ"),
  cited_wa("وَلَكِنْ", "lakin", "part", [K, AT], "لَكِنْ مَعْطُوفٌ.", "«and lākin».", "«ve lâkin».", "لَكِنْ", punct="؛"),
  atf_wa("وَالْأَرْبَعَةُ", "arbaa", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "الْأَرْبَعَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the four».", "«ve dördü».", "الْأَرْبَعَةُ"),
  W("الْأُولَى", "awwal", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ — مُؤَنَّثُ الْأَوَّلِ.", "«first».", "«ilk»."),
  li_("لِلْجَمْعِ", "jam", "noun", ["mubtada-khabar", K], "الْجَمْعِ مَجْرُورٌ — خَبَرٌ.", "«are for joining».", "«cem' içindir».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("لْجَمْعِ", "jam", "noun")]),
  W("الْمُطْلَقِ", "mutlaq", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«absolute».", "«mutlak».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "The wāw is for absolute joining without order: جَاءَنِي زَيْدٌ وَعَمْرٌو tells that Zayd and ʿAmr came, but not that one came before the other, nor that they came together." + C_EN,
 "tr": "Vâv, tertip olmaksızın mutlak cem' içindir: جَاءَنِي زَيْدٌ وَعَمْرٌو, Zeyd ile Amr'ın geldiğini bildirir; fakat birinin önce, ötekinin sonra geldiğini ya da beraber geldiklerini bildirmez." + C_TR},
 "tokens": [
  cited("الْوَاوُ", "waw-letter", "noun", ["mubtada-khabar", K, AT, "anwa-al-waw"], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«the wāw».", "«vâv»."),
  FOR("لِلْجَمْعِ", "jam", "«is for joining».", "«cem' içindir».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("لْجَمْعِ", "jam", "noun")]),
  W("الْمُطْلَقِ", "mutlaq", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«absolute».", "«mutlak»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا — بِلَا بِمَعْنَى مِنْ غَيْرِ.", "«without».", "«-sız».", "لَا"),
  W("تَرْتِيبٍ", "tartib", "noun", ["huruf-jarr", K], "مَجْرُورٌ.", "«order».", "«tertip».", punct=":"),
  W("فَقَوْلُكَ", "qawl", "noun", ["mubtada-khabar", "idafa-definiteness", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَقَوْلُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your saying».", "«... sözün».", segments=[seg("فَ", "fa", "conj"), seg("قَوْلُ", "qawl", "noun"), pr2ms()]),
  JAANI(), ZAYD_F(),
  cited_wa("وَعَمْرٌو", "amr-name", "propn", [K, AT], "الْوَاوُ عَاطِفَةٌ لِلْجَمْعِ الْمُطْلَقِ، وَعَمْرٌو مَعْطُوفٌ مَرْفُوعٌ.", "«and ʿAmr».", "«ve Amr».", "عَمْرٌو"),
  W("يُفِيدُ", "afada", "verb", ["mubtada-khabar", "fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«tells».", "«bildirir»."),
  W("مَجِيئَهُمَا", "maji", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«that they both came».", "«ikisinin geldiğini».", punct="،", segments=[seg("مَجِيئَ", "maji", "noun"), pr3d()]),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«but not».", "«fakat ... -mez».", "لَا"),
  W("يُفِيدُ", "afada", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«does it tell».", "«bildirmez»."),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ مَفْعُولٌ بِهِ.", "«that».", "«-ini»."),
  W("أَحَدَهُمَا", "ahad", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them».", "«birinin».", segments=[seg("أَحَدَ", "ahad", "noun"), pr3d()]),
  W("جَاءَ", "jaa", "verb", ["inna-wa-akhawatuha", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«came».", "«geldiğini»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«önce»."),
  W("الْآخَرِ", "akhar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the other».", "«ötekinden»."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«nor».", "«ne de».", "لَا"),
  W("أَنَّهُمَا", "anna", "part", ["inna-wa-akhawatuha"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهُمَا اسْمُهَا.", "«that they».", "«ikisinin».", segments=[seg("أَنَّ", "anna", "part"), pr3d()]),
  W("جَاءَا", "jaa", "verb", ["inna-wa-akhawatuha", "fail", "al-muthanna", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْأَلِفُ فَاعِلٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«came».", "«geldiklerini».", segments=[seg("جَاءَ", "jaa", "verb"), seg("ا", "pron-3d", "pron")]),
  W("مَعًا", "maa", "adv", ["hal"], "حَالٌ مَنْصُوبٌ.", "«together».", "«beraber».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And the fāʾ is for joining with order and without delay — as جَاءَنِي زَيْدٌ فَعَمْرٌو, «Zayd came to me and ʿAmr right after»." + C_EN,
 "tr": "Fâ, tertip ile ve mühletsiz cem' içindir — جَاءَنِي زَيْدٌ فَعَمْرٌو gibi, «bana Zeyd, hemen ardından Amr geldi»." + C_TR},
 "tokens": [
  atf_wa("وَالْفَاءُ", "fa-letter", "noun", ["mubtada-khabar", K, AT], "الْفَاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fāʾ».", "«ve fâ».", "الْفَاءُ"),
  FOR("لِلْجَمْعِ", "jam", "«is for joining».", "«cem' içindir».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("لْجَمْعِ", "jam", "noun")]),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("التَّرْتِيبِ", "tartib", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«order».", "«tertip»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا — بِلَا بِمَعْنَى مِنْ غَيْرِ.", "«and without».", "«ve ... -siz».", "لَا"),
  W("مُهْلَةٍ", "muhla", "noun", ["huruf-jarr", K], "مَجْرُورٌ.", "«delay».", "«mühlet».", punct="،"),
  nahwu(),
  JAANI(), ZAYD_F(),
  cited("فَعَمْرٌو", "amr-name", "propn", [K, AT], "الْفَاءُ عَاطِفَةٌ لِلتَّرْتِيبِ وَالتَّعْقِيبِ، وَعَمْرٌو مَعْطُوفٌ مَرْفُوعٌ.", "«then ʿAmr».", "«hemen ardından Amr».", segments=[seg("فَ", "fa", "conj"), seg("عَمْرٌو", "amr-name", "propn")], punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  W("جَاءَ", "jaa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«came».", "«geldi»."),
  W("عَمْرٌو", "amr-name", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«ʿAmr».", "«Amr»."),
  W("عَقِيبَ", "aqib", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«right after».", "«hemen ardından»."),
  W("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'in».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And ثُمَّ is for joining with order and with delay — as جَاءَنِي زَيْدٌ ثُمَّ عَمْرٌو, «Zayd came to me, and ʿAmr after a while»." + C_EN,
 "tr": "ثُمَّ, tertip ve mühletle birlikte cem' içindir — جَاءَنِي زَيْدٌ ثُمَّ عَمْرٌو gibi, «bana Zeyd, bir süre sonra Amr geldi»." + C_TR},
 "tokens": [
  LET("ثُمَّ", "thumma", "«and thumma».", "«ve sümme»."),
  FOR("لِلْجَمْعِ", "jam", "«is for joining».", "«cem' içindir».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("لْجَمْعِ", "jam", "noun")]),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("التَّرْتِيبِ", "tartib", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«order».", "«tertip»."),
  atf_wa("وَالْمُهْلَةِ", "muhla", "noun", [AT, K], "الْمُهْلَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and delay».", "«ve mühlet».", "الْمُهْلَةِ", punct="،"),
  nahwu(),
  JAANI(), ZAYD_F(),
  cited("ثُمَّ", "thumma", "conj", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "«then».", "«sonra»."),
  AMR_M("بِثُمَّ.", "«ʿAmr».", "«Amr».", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  W("جَاءَ", "jaa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«came».", "«geldi»."),
  W("عَمْرٌو", "amr-name", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«ʿAmr».", "«Amr»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... sonra»."),
  W("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'den»."),
  bi_("بِمُهْلَةٍ", "muhla", "noun", [K], "مُهْلَةٍ مَجْرُورٌ.", "«with a delay».", "«bir süre».", "مُهْلَةٍ", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And حَتَّى is for joining with order and delay — as مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ; its delay is less than that of ثُمَّ, and its coordinate is a part of what it is joined to, the strongest or the weakest part, to signify strength or weakness." + C_EN,
 "tr": "حَتَّى, tertip ve mühletle birlikte cem' içindir — مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ gibi; mühleti ثُمَّ'ninkinden azdır ve ma'tûfu, kuvvet ya da zaaf ifade etmek için ma'tûfun aleyhin en kuvvetli ya da en zayıf cüz'üdür." + C_TR},
 "tokens": [
  LET("حَتَّى", "hatta", "«and ḥattā».", "«ve hattâ»."),
  FOR("لِلْجَمْعِ", "jam", "«is for joining».", "«cem' içindir».", "الْجَمْعِ", segs=[seg("لِ", "li", "prep"), seg("لْجَمْعِ", "jam", "noun")]),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("التَّرْتِيبِ", "tartib", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«order».", "«tertip»."),
  atf_wa("وَالْمُهْلَةِ", "muhla", "noun", [AT, K], "الْمُهْلَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and delay».", "«ve mühlet».", "الْمُهْلَةِ", punct="،"),
  nahwu(),
  cited("مَاتَ", "mata-die", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«died».", "«öldü»."),
  cited("النَّاسُ", "nas", "noun", ["fail", AT], "فَاعِلٌ مَرْفُوعٌ — الْمَعْطُوفُ عَلَيْهِ.", "«mankind».", "«insanlar»."),
  cited("حَتَّى", "hatta", "conj", [K, AT], "حَرْفُ عَطْفٍ — الْمَعْطُوفُ جُزْءٌ مِنَ الْمَعْطُوفِ عَلَيْهِ.", "«even».", "«hatta»."),
  cited("الْأَنْبِيَاءُ", "nabi", "noun", [K, AT, "jam-taksir"], "مَعْطُوفٌ عَلَى النَّاسُ مَرْفُوعٌ — جَمْعُ نَبِيٍّ، أَقْوَى الْأَجْزَاءِ.", "«the prophets».", "«peygamberler».", punct="؛"),
  atf_wa("وَمُهْلَتُهَا", "muhla", "noun", ["mubtada-khabar", "idafa-definiteness", K], "مُهْلَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its delay».", "«mühleti».", "مُهْلَتُ", extra_segs=[seg("مُهْلَتُ", "muhla", "noun"), pr3fs()]),
  W("أَقَلُّ", "aqall", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«is less».", "«daha azdır»."),
  W("مِنْ", "min", "prep", ["huruf-jarr", "ism-tafdil"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  W("مُهْلَةِ", "muhla", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the delay of».", "«mühletinden»."),
  cited("ثُمَّ", "thumma", "conj", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«thumma».", "«sümme'nin».", punct="،"),
  atf_wa("وَمَعْطُوفُهَا", "matuf", "noun", ["mubtada-khabar", "idafa-definiteness", AT], "مَعْطُوفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its coordinate».", "«ve ma'tûfu».", "مَعْطُوفُ", extra_segs=[seg("مَعْطُوفُ", "matuf", "noun"), pr3fs()]),
  W("جُزْءٌ", "juz", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a part».", "«bir cüz'üdür»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-in»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«what it is joined».", "«ma'tûfun»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to».", "«aleyhin».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  W("أَقْوَاهُ", "aqwa", "noun", ["badal", "idafa-definiteness", "ism-tafdil", "ism-maqsur-manqus"], "بَدَلٌ مِنْ جُزْءٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the strongest».", "«en kuvvetlisi».", segments=[seg("أَقْوَا", "aqwa", "noun"), pr3ms()]),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("أَضْعَفُهُ", "adaf", "noun", [AT, "idafa-definiteness", "ism-tafdil"], "مَعْطُوفٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the weakest».", "«en zayıfı».", segments=[seg("أَضْعَفُ", "adaf", "noun"), pr3ms()]),
  li_("لِإِفَادَةِ", "ifada", "noun", ["idafa-definiteness", "lam-taleel"], "إِفَادَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to signify».", "«ifade etmek için».", "إِفَادَةِ"),
  W("الْقُوَّةِ", "quwwa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«strength».", "«kuvvet»."),
  W("أَوِ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«ya da»."),
  W("الضَّعْفِ", "daf", "noun", [AT], "مَعْطُوفٌ مَجْرُورٌ.", "«weakness».", "«zaaf».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And between حَتَّى and ثُمَّ there are two differences: in حَتَّى it is a condition that the coordinate be a part of what it is joined to, and in ثُمَّ it is not." + C_EN,
 "tr": "حَتَّى ile ثُمَّ arasında iki fark vardır: حَتَّى'da ma'tûfun ma'tûfun aleyhten bir cüz olması şarttır; ثُمَّ'de şart değildir." + C_TR},
 "tokens": [
  atf_wa("وَبَيْنَ", "bayna", "adv", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "بَيْنَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«and between».", "«ve ... arasında».", "بَيْنَ"),
  cited("حَتَّى", "hatta", "conj", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«ḥattā».", "«hattâ»."),
  cited_wa("وَثُمَّ", "thumma", "conj", [AT], "ثُمَّ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and thumma».", "«ile sümme».", "ثُمَّ"),
  W("فَرْقَانِ", "farq", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«there are two differences».", "«iki fark vardır».", punct=":"),
  W("فِي", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«in».", "«-da»."),
  cited("حَتَّى", "hatta", "conj", ["huruf-jarr", AT], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«ḥattā».", "«hattâ»."),
  W("يُشْتَرَطُ", "ishtarata", "verb", ["naib-al-fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it is a condition».", "«şarttır»."),
  W("كَوْنُ", "kawn", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«that … be».", "«olması»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَصْدَرِ.", "«the coordinate».", "«ma'tûfun»."),
  W("جُزْءًا", "juz", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَوْنُ مَنْصُوبٌ.", "«a part».", "«bir cüz»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-ten»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«what it is joined».", "«ma'tûfun»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to».", "«aleyhten».", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  cited("ثُمَّ", "thumma", "conj", ["huruf-jarr", AT], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«thumma».", "«sümme»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«değildir»."),
  W("يُشْتَرَطُ", "ishtarata", "verb", ["naib-al-fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«is it a condition».", "«şart».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And in ثُمَّ the delay is in outward fact — in جَاءَنِي زَيْدٌ ثُمَّ عَمْرٌو, ʿAmr's coming is really after Zayd's — while in حَتَّى it is only in the mind: when we say مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ, the prophets' death is after mankind's in the mind, not in fact; and in قَدِمَ الْحُجَّاجُ حَتَّى الْمُشَاةُ the arrival of those on foot may in fact be the reverse." + C_EN,
 "tr": "ثُمَّ'de mühlet dış dünya itibariyledir — جَاءَنِي زَيْدٌ ثُمَّ عَمْرٌو'da Amr'ın gelişi hakikaten Zeyd'den sonradır — حَتَّى'da ise yalnız zihin itibariyledir: مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ dediğimizde peygamberlerin ölümü zihnen insanlardan sonradır, hakikatte değil; قَدِمَ الْحُجَّاجُ حَتَّى الْمُشَاةُ'da yayaların gelişi hakikatte tersi de olabilir." + C_TR},
 "tokens": [
  atf_wa("وَالْمُهْلَةُ", "muhla", "noun", ["mubtada-khabar", K], "الْمُهْلَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the delay».", "«ve mühlet».", "الْمُهْلَةُ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("ثُمَّ", "thumma", "conj", ["huruf-jarr", AT], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«thumma».", "«sümme»."),
  W("فِي", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ.", "«is in».", "«... itibariyledir»."),
  W("الْخَارِجِ", "kharij", "noun", ["huruf-jarr", "ism-fail"], "مَجْرُورٌ — الْوَاقِعُ.", "«outward fact».", "«dış dünya».", punct="—"),
  W("فَفِي", "fi", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«in».", "«-da».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  cited("جَاءَنِي", "jaa", "verb", ["huruf-jarr", "fail", "maful-bihi", "hollow-verbs"], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  ZAYD_F(),
  cited("ثُمَّ", "thumma", "conj", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then».", "«sonra»."),
  AMR_M("بِثُمَّ.", "«ʿAmr».", "«Amr».", punct="،"),
  W("مَجِيءُ", "maji", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the coming of».", "«gelişi»."),
  W("عَمْرٍو", "amr-name", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ʿAmr».", "«Amr'ın»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ.", "«is after».", "«... sonradır»."),
  W("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'den»."),
  W("حَقِيقَةً", "haqiqa", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«really».", "«hakikaten».", punct="—"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«while in».", "«... -da ise».", "فِي"),
  cited("حَتَّى", "hatta", "conj", ["huruf-jarr", AT], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«ḥattā».", "«hattâ»."),
  W("فِي", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: الْمُهْلَةُ.", "«it is in».", "«... itibariyledir»."),
  W("الذِّهْنِ", "dhihn", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the mind».", "«zihin»."),
  W("فَقَطْ", "faqat", "adv", ["hal"], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ.", "«only».", "«yalnız».", punct=":"),
  W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğimizde».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  W("قُلْنَا", "qala", "verb", ["idha-shartiyya", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ — فِعْلُ الشَّرْطِ.", "«we say».", "«dediğimizde».", segments=[seg("قُلْ", "qala", "verb"), seg("نَا", "pron-1p", "pron")]),
  cited("مَاتَ", "mata-die", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«died».", "«öldü»."),
  cited("النَّاسُ", "nas", "noun", ["fail", AT], "فَاعِلٌ مَرْفُوعٌ.", "«mankind».", "«insanlar»."),
  cited("حَتَّى", "hatta", "conj", [K, AT], "حَرْفُ عَطْفٍ.", "«even».", "«hatta»."),
  cited("الْأَنْبِيَاءُ", "nabi", "noun", [AT, "jam-taksir"], "مَعْطُوفٌ مَرْفُوعٌ.", "«the prophets».", "«peygamberler».", punct="،"),
  W("فَمَوْتُ", "mawt", "noun", ["mubtada-khabar", "idafa-definiteness", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَمَوْتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the death of».", "«ölümü».", segments=[seg("فَ", "fa", "conj"), seg("مَوْتُ", "mawt", "noun")]),
  W("الْأَنْبِيَاءِ", "nabi", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the prophets».", "«peygamberlerin»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ.", "«is after».", "«... sonradır»."),
  W("مَوْتِ", "mawt", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the death of».", "«ölümünden»."),
  W("النَّاسِ", "nas", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«mankind».", "«insanların»."),
  W("ذِهْنًا", "dhihn", "noun", ["hal"], "حَالٌ مَنْصُوبٌ: كَائِنًا فِي الذِّهْنِ.", "«in the mind».", "«zihnen»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", AT], "عَاطِفَةٌ لِلنَّفْيِ.", "«not».", "«... değil»."),
  W("حَقِيقَةً", "haqiqa", "noun", [AT, "hal"], "مَعْطُوفٌ مَنْصُوبٌ.", "«in fact».", "«hakikatte».", punct="؛"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -da».", "فِي"),
  cited("قَدِمَ", "qadima", "verb", ["huruf-jarr", "fail"], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — قَدِمَ فِعْلٌ مَاضٍ.", "«arrived».", "«geldi»."),
  cited("الْحُجَّاجُ", "hajj-pilgrim", "noun", ["fail", AT, "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ حَاجٍّ.", "«the pilgrims».", "«hacılar»."),
  cited("حَتَّى", "hatta", "conj", [K, AT], "حَرْفُ عَطْفٍ.", "«even».", "«hatta»."),
  cited("الْمُشَاةُ", "mashi", "noun", [AT, "jam-taksir"], "مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ مَاشٍ، أَضْعَفُ الْأَجْزَاءِ.", "«those on foot».", "«yayalar».", punct="،"),
  W("قَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«may».", "«-ebilir»."),
  W("يَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«be».", "«olabilir»."),
  W("قُدُومُ", "qudum", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَكُونُ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the arrival of».", "«gelişi»."),
  W("الْمُشَاةِ", "mashi", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«those on foot».", "«yayaların»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-te»."),
  W("الْحَقِيقَةِ", "haqiqa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«fact».", "«hakikatte»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "kana-wa-akhawatuha"], "حَرْفُ جَرٍّ — خَبَرُ يَكُونُ.", "«-».", "«-»."),
  W("الْعَكْسِ", "aks", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the reverse».", "«tersi».", punct="."),
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
 "muhla": need("muhla", "مُهْلَة", "م ه ل", "noun", "a delay, an interval — what ثُمَّ adds to order and the fāʾ lacks", "mühlet, ara — sümme'nin tertibe eklediği, fâ'da olmayan", 4),
 "aqib": need("aqib", "عَقِيب", "ع ق ب", "noun", "immediately after (a ẓarf: عَقِيبَ)", "hemen ardından (zarf: عَقِيبَ)", 4),
 "aqwa": need("aqwa", "أَقْوَى", "ق و ي", "noun", "strongest, stronger — the elative of قَوِيّ", "en kuvvetli, daha kuvvetli — kaviyy'in ism-i tafdîli", 3),
 "adaf": need("adaf", "أَضْعَف", "ض ع ف", "noun", "weakest, weaker — the elative of ضَعِيف", "en zayıf, daha zayıf — zaîf'in ism-i tafdîli", 3),
 "aqall": need("aqall", "أَقَلّ", "ق ل ل", "noun", "less, least — the elative of قَلِيل", "daha az, en az — kalîl'in ism-i tafdîli", 2),
 "ishtarata": need("ishtarata", "اِشْتَرَطَ", "ش ر ط", "verb", "to stipulate, to make a condition (Form VIII)", "şart koşmak (iftiâl)", 3),
 "hajj-pilgrim": need("hajj-pilgrim", "حَاجّ", "ح ج ج", "noun", "a pilgrim; plural حُجَّاج", "hacı; cem'i حُجَّاج", 2),
 "qudum": need("qudum", "قُدُوم", "ق د م", "noun", "arrival, coming — the maṣdar of قَدِمَ", "geliş, varış — kadime'nin masdarı", 3),
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
put_morph(mo, "ishtarata", _nfc(_sg.derived(_sg.B8, _sg.W8, "َ", "شْتَرَط", "شْتَرِط", "اِشْتَرِط", "اِشْتِرَاط", "مُشْتَرِط", "مُشْتَرَط", "اُشْتُرِطَ", "يُشْتَرَطُ", "اِشْتَرَطَ الشَّيْءَ: جَعَلَهُ شَرْطًا — بَابُ الِافْتِعَالِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch37 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "حُرُوفُ الْعَطْفِ فِي الْكَافِيَةِ: الْوَاوُ وَالْفَاءُ وَثُمَّ وَحَتَّى", "en": "The coordination letters in the Kafiya: the ten, and the four of absolute joining — the wāw without order, the fāʾ with order and no delay, thumma with delay in fact, ḥattā with a part of its whole and delay only in the mind", "tr": "Kâfiye'de atıf harfleri: on harf ve mutlak cem'in dördü — tertipsiz vâv, tertipli ve mühletsiz fâ, hakikî mühletli sümme, bütününün bir cüz'ü ve yalnız zihnî mühletle hattâ"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — حروف العطف: الواو والفاء وثم وحتى وأو وإما وأم ولا وبل ولكن؛ والأربعة الأولى للجمع المطلق", "ضياء صونغور اوغلى — دفتر الكافية: الواو بلا ترتيب؛ الفاء للترتيب بلا مهلة؛ ثم للترتيب مع المهلة؛ حتى ومعطوفها جزء؛ الفرقان بين حتى وثم؛ مات الناس حتى الأنبياء؛ قدم الحجاج حتى المشاة"],
 "question": {
  "en": ["How many coordination letters are there? Ten, and they divide by what they say about the two things joined. The first four say both are in: the wāw, the fāʾ, thumma, ḥattā. The next three leave it open which one: aw, immā, am. The last three settle on one of the two: lā, bal, lākin.",
         "What does the wāw add? Nothing but «and». جَاءَنِي زَيْدٌ وَعَمْرٌو says both came — not who came first, not whether together. The WawEngine's atf face is exactly this: joining, with no order read into it.",
         "What do the fāʾ and thumma add? Order — and they differ in the gap. The fāʾ joins with order and no delay (ʿAmr right after Zayd); thumma with order and a delay (ʿAmr after a while). The gap is real: it happened in that order.",
         "What is special about ḥattā as a coordinator? Two things. Its coordinate must be a PART of what it is joined to — and the strongest or weakest part, to make a point: مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ (even the prophets, the strongest), قَدِمَ الْحُجَّاجُ حَتَّى الْمُشَاةُ (even those on foot, the weakest). And its «delay» is only in the mind: the prophets did not really die after everyone else.",
         "How is ḥattā the coordinator told from ḥattā the jarr letter? By the case that follows: الْأَنْبِيَاءُ in rafʿ is joined to النَّاسُ; a majrūr after ḥattā is the end-point of chapter 30. The analyzer reads the ending and names the face.",
         "What does the engine do? The PARTICLES table holds the ten with their senses; the AmilEngine pairs each coordinate with what it is joined to, so the coordinate takes its partner's case; and the TartibEngine's order ledger records whether a letter implies sequence."],
  "tr": ["Kaç atıf harfi vardır? On; ve bağlanan iki şey hakkında söyledikleriyle bölünürler. İlk dördü ikisinin de dahil olduğunu söyler: vâv, fâ, sümme, hattâ. Sonraki üçü hangisi olduğunu açık bırakır: ev, immâ, em. Son üçü ikisinden birinde karar kılar: lâ, bel, lâkin.",
         "Vâv ne ekler? «Ve»den başka hiçbir şey. جَاءَنِي زَيْدٌ وَعَمْرٌو ikisinin de geldiğini söyler — kimin önce geldiğini değil, beraber olup olmadığını değil. WawEngine'in atıf yüzü tam budur: içine sıra okunmayan bağlama.",
         "Fâ ve sümme ne ekler? Tertip — ve aralıkta ayrılırlar. Fâ tertiple ve mühletsiz bağlar (Amr Zeyd'in hemen ardından); sümme tertiple ve mühletle (Amr bir süre sonra). Aralık gerçektir: o sırayla olmuştur.",
         "Atıf harfi olarak hattâ'da özel olan ne? İki şey. Ma'tûfu bağlandığının bir CÜZ'Ü olmalıdır — ve bir noktayı vurgulamak için en kuvvetli ya da en zayıf cüz: مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ (peygamberler bile, en kuvvetli), قَدِمَ الْحُجَّاجُ حَتَّى الْمُشَاةُ (yayalar bile, en zayıf). Ve «mühleti» yalnız zihindedir: peygamberler gerçekten herkesten sonra ölmedi.",
         "Atıf hattâ'sı cer hattâ'sından nasıl ayrılır? Ardından gelen harekeyle: ref'teki الْأَنْبِيَاءُ, النَّاسُ'a bağlıdır; hattâ'dan sonraki mecrûr otuzuncu bâbın intihâsıdır. Analizör sonu okur ve yüzü adlandırır.",
         "Motor ne yapar? PARTICLES tablosu onunu mânâlarıyla tutar; AmilEngine her ma'tûfu bağlandığıyla eşler, böylece ma'tûf eşinin i'rabını alır; TartibEngine'in sıra defteri bir harfin sıra ima edip etmediğini kaydeder."]},
 "plain": {
  "en": "Ten little words join one thing to another. The first four — «and», «and then», «then later», «even» — say both things are included; they differ only in whether one came after the other and how long after. «Even» has a twist: what follows it must be part of what came before, and the «after» is only in your head.",
  "tr": "On küçük kelime bir şeyi ötekine bağlar. İlk dördü — «ve», «hemen sonra», «sonra», «hatta» — ikisinin de dahil olduğunu söyler; yalnız sırada ve aradaki sürede ayrılırlar. «Hatta»nın bir inceliği vardır: ardından gelen öncekinin parçası olmalıdır ve «sonra» yalnız kafandadır."},
 "explanation": {
  "en": "The Kafiya lists the ten and makes the first division — the four for absolute joining — and the notebook glosses each of the four by the two parameters the tradition uses, order and delay. The wāw has neither, and the notebook says so negatively, in the way that matters for reading: nothing about who came first or whether together may be inferred from it. The fāʾ has order without delay, thumma has both. Ḥattā is the interesting one, and the notebook gives it the two rules that make it a different letter from the jarr ḥattā of chapter 30: the coordinate is a part of the whole — the extreme part, to make a point of strength or weakness — and the delay is mental, not real, which the two stock examples show from both ends (the prophets' death, the pilgrims on foot). The two differences from thumma are then stated as a catechism. The next chapter takes the six remaining letters.",
  "tr": "Kâfiye onunu sayar ve ilk bölümü — mutlak cem'in dördü — yapar; defter dördün her birini geleneğin kullandığı iki ölçütle, tertip ve mühletle şerh eder. Vâvda ikisi de yoktur ve defter bunu okuma için önemli olan olumsuz biçimde söyler: kimin önce geldiği ya da beraber olup olmadıkları ondan çıkarılamaz. Fâ'da mühletsiz tertip, sümme'de ikisi de vardır. İlginç olan hattâ'dır ve defter ona onu otuzuncu bâbın cer hattâ'sından farklı bir harf kılan iki kuralı verir: ma'tûf bütünün bir cüz'üdür — kuvvet ya da zaaf vurgusu için uç cüz — ve mühlet gerçek değil zihnîdir; iki alışılmış örnek bunu iki uçtan gösterir (peygamberlerin ölümü, yaya hacılar). Sümme'den iki fark sonra sual-cevap olarak verilir. Sonraki bâb kalan altı harfi alır."},
 "examples": [
  {"ar": "الْوَاوُ وَالْفَاءُ وَثُمَّ وَحَتَّى وَأَوْ وَإِمَّا وَأَمْ وَلَا وَبَلْ وَلَكِنْ", "en": "The ten.", "tr": "On harf.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "جَاءَنِي زَيْدٌ وَعَمْرٌو", "en": "The wāw: both, in no order.", "tr": "Vâv: ikisi, sırasız.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "جَاءَنِي زَيْدٌ فَعَمْرٌو — جَاءَنِي زَيْدٌ ثُمَّ عَمْرٌو", "en": "The fāʾ and thumma: order, without and with delay.", "tr": "Fâ ve sümme: tertip, mühletsiz ve mühletli.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ", "en": "Ḥattā: the strongest part.", "tr": "Hattâ: en kuvvetli cüz.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "قَدِمَ الْحُجَّاجُ حَتَّى الْمُشَاةُ", "en": "Ḥattā: the weakest part, the delay only in the mind.", "tr": "Hattâ: en zayıf cüz, mühlet yalnız zihinde.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«جَاءَنِي زَيْدٌ وَعَمْرٌو — önce Zeyd, sonra Amr geldi»",
   "right": "«ikisi de geldi; vâv sıra bildirmez»",
   "why": {"en": "Only the fāʾ and thumma carry order.", "tr": "Sırayı yalnız fâ ve sümme taşır."}},
  {"wrong": "«مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءِ»",
   "right": "«مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ — atıf hattâ'sından sonra ma'tûf, ma'tûfun aleyhin i'rabını alır»",
   "why": {"en": "A majrūr after ḥattā makes it the jarr letter, not the coordinator.", "tr": "Hattâ'dan sonra mecrûr onu atıf değil cer harfi yapar."}},
  {"wrong": "«جَاءَنِي زَيْدٌ حَتَّى عَمْرٌو»",
   "right": "«جَاءَنِي الْقَوْمُ حَتَّى زَيْدٌ — hattâ'nın ma'tûfu bir cüz olmalıdır»",
   "why": {"en": "ʿAmr is not a part of Zayd; the part condition fails.", "tr": "Amr Zeyd'in cüz'ü değildir; cüz şartı sağlanmaz."}},
  {"wrong": "«مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ — peygamberler herkesten sonra öldü»",
   "right": "«hattâ'nın mühleti yalnız zihnîdir; hakikatte bir sıra yoktur»",
   "why": {"en": "The second difference from thumma: the delay is in the mind.", "tr": "Sümme'den ikinci fark: mühlet zihindedir."}}],
 "relatedNotes": ["atf-nasaq", "anwa-al-waw", "ila-hatta-fi-wal-ba-fil-kafiya", "al-tawabi-note", "tartib-note"]}
NOTE["relatedNotes"] = ["atf-nasaq", "anwa-al-waw", "ila-hatta-fi-wal-ba-fil-kafiya", "al-fa-fi-jawab-al-shart"]

ADD_EN = (" Chapter 37 (notebook lines ~341-342): the ten coordination letters and the four of absolute joining — the wāw, the fāʾ, thumma and ḥattā with their stock examples and the two ḥattā/thumma differences — the notebook's exposition, kept as commentary (s1-s7).")
ADD_TR = (" Otuz yedinci bâb (defter satırları ~341-342): on atıf harfi ve mutlak cem'in dördü — vâv, fâ, sümme ve hattâ alışılmış örnekleriyle ve iki hattâ/sümme farkı — defterin açıklaması, şerh olarak (s1-s7).")
write_out(37, S, TITLE, ADD_EN, ADD_TR, "341-342", GLOSS_ADD, notes=(NOTE,),
          related=(("atf-nasaq", [K]), ("anwa-al-waw", [K])))
report(37, S, GLOSS_ADD, (NOTE,))
