# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 32: THE OATH LETTERS — the wāw (verb dropped, no request, explicit noun only), the tāʾ (like the wāw, on the
name of God only), the bāʾ (the most general: with or without the verb, in statement and request, on noun and pronoun); the three
answers of the oath (the lām, إِنَّ, a negation); and the answer dropped when the oath follows or interrupts the sentence that shows it.
Source: the Ottoman notebook (Ziya Sungur-oglu), line ~334 of the transcription.

  COMMENTARY (the notebook): s1-s5 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch32.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "huruf-al-qasam-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الْقَسَمِ وَجَوَابُهُ", "en": "The oath letters and the answer of the oath", "tr": "Kasem harfleri ve kasemin cevabı"}
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
QS = "qasam-waw"
def ALLAH_Q(full, lexp, en, tr, ar, punct=None):
    return cited(full, "allah", "propn", [K, HJ], ar, en, tr, punct=punct, segments=[seg(full[0] + ("َ" if full[1] == "َ" else "ِ"), lexp, "prep"), seg(full[2:], "allah", "propn")])
def LAF(punct=None, tags=()): return cited("لَأَفْعَلَنَّ", "faala", "verb", [K, "nun-tawkid", "nun-tawkid"] + list(tags), "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَأَفْعَلَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ.", "«I will surely do».", "«elbette yapacağım».", punct=punct, segments=[seg("لَ", "lam-qasam", "part"), seg("أَفْعَلَ", "faala", "verb"), seg("نَّ", "nun-tawkid-seg", "part")])

S.append({"id": "s1", "translation": {
 "en": "And the wāw of the oath is used only with its verb dropped; it is for other than a request; and it is confined to the explicit noun — so one does not say أَقْسَمْتُ وَاللهِ, nor وَاللهِ أَخْبِرْنِي in asking, nor وَكَ." + C_EN,
 "tr": "Kasem vâvı ancak fiilinin hazfiyle kullanılır; sualin gayrı içindir; ve zâhir isme mahsustur — أَقْسَمْتُ وَاللهِ denmez, sualde وَاللهِ أَخْبِرْنِي denmez, وَكَ denmez." + C_TR},
 "tokens": [
  atf_wa("وَوَاوُ", "waw-letter", "noun", ["mubtada-khabar", "idafa-definiteness", K, HJ], "وَاوُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the wāw of».", "«ve ... vâvı».", "وَاوُ"),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasem»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "qasr"], "نَافِيَةٌ — النَّفْيُ وَالِاسْتِثْنَاءُ لِلْقَصْرِ.", "«only».", "«ancak»."),
  W("تُسْتَعْمَلُ", "istamala", "verb", ["mubtada-khabar", "naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ خَبَرٌ.", "«is used».", "«kullanılır»."),
  W("إِلَّا", "illa", "part", ["istithna", "qasr"], "أَدَاةُ حَصْرٍ.", "«but».", "«-le»."),
  bi_("بِحَذْفِ", "hadhf", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"], "حَذْفِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«with the dropping of».", "«hazfiyle».", "حَذْفِ"),
  W("فِعْلِهَا", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its verb».", "«fiilinin».", punct="؛", segments=[seg("فِعْلِ", "fil", "noun"), pr3fs()]),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  li_("لِغَيْرِ", "ghayr", "noun", ["mubtada-khabar", "idafa-definiteness"], "غَيْرِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is for other than».", "«... gayrı içindir».", "غَيْرِ"),
  W("السُّؤَالِ", "sual", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الطَّلَبُ.", "«a request».", "«sualin».", punct="؛"),
  atf_wa("وَمُخْتَصَّةٌ", "mukhtass", "noun", ["mubtada-khabar", "ism-maful"], "مُخْتَصَّةٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ.", "«and confined».", "«ve ... mahsustur».", "مُخْتَصَّةٌ"),
  bi_("بِالِاسْمِ", "ism", "noun", [], "الِاسْمِ مَجْرُورٌ.", "«to the noun».", "«isme».", "الِاسْمِ"),
  W("الظَّاهِرِ", "zahir", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«explicit».", "«zâhir».", punct="،"),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«o hâlde ... -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْمَقُولُ.", "«does one say».", "«denmez»."),
  cited("أَقْسَمْتُ", "aqsama", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْمَمْنُوعُ ذِكْرُهُ مَعَ الْوَاوِ.", "«I swear».", "«yemin ettim».", segments=[seg("أَقْسَمْ", "aqsama", "verb"), prT()]),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«nor».", "«ne de».", "لَا"),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ."),
  cited("أَخْبِرْنِي", "akhbara", "verb", ["fail", "maful-bihi", "form-iv-verbs"], "فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«tell me».", "«bana haber ver».", segments=[seg("أَخْبِرْ", "akhbara", "verb"), pr1s()]),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("السُّؤَالِ", "sual", "noun", [HJ], "مَجْرُورٌ.", "«asking».", "«sualde».", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«nor».", "«ne de».", "لَا"),
  cited("وَكَ", "waw-qasam", "prep", [K, HJ, "al-mabni-wal-mudmar"], "الْوَاوُ لِلْقَسَمِ، وَالْكَافُ ضَمِيرٌ مَجْرُورٌ — مَمْنُوعٌ.", "«by you».", "«sana yemin olsun».", punct=".", segments=[seg("وَ", "waw-qasam", "prep"), pr2ms()]),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And the tāʾ of the oath is like its wāw, and it is confined to the name of God — as تَاللهِ." + C_EN,
 "tr": "Kasem tâsı kasem vâvı gibidir ve Allah lafzına mahsustur — تَاللهِ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتَاءُ", "ta-letter", "noun", ["mubtada-khabar", "idafa-definiteness", K, HJ], "تَاءُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the tāʾ of».", "«ve ... tâsı».", "تَاءُ"),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasem»."),
  ka_("كَوَاوِهِ", "waw-letter", "noun", ["mubtada-khabar", "idafa-definiteness"], "وَاوِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«is like its wāw».", "«vâvı gibidir».", "وَاوِ", segs=[seg("كَ", "ka", "part"), seg("وَاوِ", "waw-letter", "noun"), pr3msi()], punct="،"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("مُخْتَصَّةٌ", "mukhtass", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is confined».", "«mahsustur»."),
  bi_("بِاسْمِ", "ism", "noun", ["idafa-definiteness"], "اسْمِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to the name of».", "«... lafzına».", "اسْمِ"),
  W("اللهِ", "allah", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God».", "«Allah».", punct="،"),
  nahwu(),
  ALLAH_Q("تَاللهِ", "ta-qasam", "«by God».", "«tallahi».", "التَّاءُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And the bāʾ of the oath is more general than them all: it is used with the verb, as أُقْسِمُ بِاللهِ, and without it, as بِاللهِ; in a statement, as بِاللهِ لَأَفْعَلَنَّ كَذَا, and in a request, as بِاللهِ اجْلِسْ; on the explicit noun, as بِاللهِ لَأَفْعَلَنَّ, and on the pronoun, as بِكَ لَأَفْعَلَنَّ." + C_EN,
 "tr": "Kasem bâsı hepsinden umumîdir: fiille kullanılır, أُقْسِمُ بِاللهِ gibi, fiilsiz de, بِاللهِ gibi; haberde, بِاللهِ لَأَفْعَلَنَّ كَذَا gibi, sualde de, بِاللهِ اجْلِسْ gibi; zâhir isimde, بِاللهِ لَأَفْعَلَنَّ gibi, zamirde de, بِكَ لَأَفْعَلَنَّ gibi." + C_TR},
 "tokens": [
  atf_wa("وَبَاءُ", "ba-harf", "noun", ["mubtada-khabar", "idafa-definiteness", K, HJ], "بَاءُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the bāʾ of».", "«ve ... bâsı».", "بَاءُ"),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasem»."),
  W("أَعَمُّ", "aamm", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«is more general».", "«daha umumîdir»."),
  W("مِنْهَا", "min", "prep", [HJ, "ism-tafdil"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — الْمُفَضَّلُ عَلَيْهِ.", "«than them».", "«onlardan».", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  W("كُلِّهَا", "kull", "noun", ["tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَعْنَوِيٌّ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«all».", "«hepsinden».", punct=":", segments=[seg("كُلِّ", "kull", "noun"), pr3fs()]),
  W("تُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it is used».", "«kullanılır»."),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb».", "«fiil».", punct="،"),
  nahwu(),
  cited("أُقْسِمُ", "aqsama", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I swear».", "«yemin ederim»."),
  ALLAH_Q("بِاللهِ", "ba-qasam", "«by God».", "«Allah'a».", "الْبَاءُ لِلْقَسَمِ مَعَ ذِكْرِ الْفِعْلِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", punct="،"),
  atf_wa("وَبِدُونِهِ", "dun", "noun", ["idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَدُونِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and without it».", "«ve onsuz».", "دُونِ", extra_segs=[seg("بِ", "bi", "prep"), seg("دُونِ", "dun", "noun"), pr3msi()], punct="،"),
  nahwu(),
  ALLAH_Q("بِاللهِ", "ba-qasam", "«by God».", "«billâhi».", "الْبَاءُ لِلْقَسَمِ وَالْفِعْلُ مَحْذُوفٌ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", punct="؛"),
  atf_wa("وَفِي", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("الْخَبَرِ", "khabar", "noun", [HJ, "khabar-insha"], "مَجْرُورٌ — ضِدُّ الطَّلَبِ.", "«a statement».", "«haberde».", punct="،"),
  nahwu(),
  ALLAH_Q("بِاللهِ", "ba-qasam", "«by God».", "«billâhi».", "الْبَاءُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ."),
  LAF(),
  cited("كَذَا", "kadha", "pron", ["maful-bihi"], "كِنَايَةٌ عَنِ الْفِعْلِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«such-and-such».", "«şöyle».", punct="،"),
  atf_wa("وَفِي", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("السُّؤَالِ", "sual", "noun", [HJ], "مَجْرُورٌ.", "«a request».", "«sualde».", punct="،"),
  nahwu(),
  ALLAH_Q("بِاللهِ", "ba-qasam", "«by God».", "«Allah aşkına».", "الْبَاءُ لِلْقَسَمِ فِي الطَّلَبِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ."),
  cited("اجْلِسْ", "jalasa", "verb", ["fail"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«sit».", "«otur».", punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", [HJ], "عَلَى حَرْفُ جَرٍّ.", "«and on».", "«ve ... -de».", "عَلَى"),
  W("الِاسْمِ", "ism", "noun", [HJ], "مَجْرُورٌ.", "«the noun».", "«isimde»."),
  W("الظَّاهِرِ", "zahir", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«explicit».", "«zâhir».", punct="،"),
  nahwu(),
  ALLAH_Q("بِاللهِ", "ba-qasam", "«by God».", "«billâhi».", "الْبَاءُ لِلْقَسَمِ عَلَى الِاسْمِ الظَّاهِرِ."),
  LAF(punct="،"),
  atf_wa("وَعَلَى", "ala", "prep", [HJ], "عَلَى حَرْفُ جَرٍّ.", "«and on».", "«ve ... -de».", "عَلَى"),
  W("الضَّمِيرِ", "damir", "noun", [HJ, "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«the pronoun».", "«zamirde».", punct="،"),
  nahwu(),
  cited("بِكَ", "ba-qasam", "prep", [K, HJ, "al-mabni-wal-mudmar"], "الْبَاءُ لِلْقَسَمِ، وَالْكَافُ ضَمِيرٌ مَجْرُورٌ — جَائِزٌ مَعَ الْبَاءِ دُونَ الْوَاوِ.", "«by you».", "«sana yemin olsun».", segments=[seg("بِ", "ba-qasam", "prep"), pr2ms()]),
  LAF(punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the oath is answered by one of three: by the lām — as وَاللهِ لَزَيْدٌ قَائِمٌ and وَاللهِ لَأَفْعَلَنَّ كَذَا; by إِنَّ — as وَاللهِ إِنَّ زَيْدًا لَقَائِمٌ; and by a negation with مَا or لَا — as وَاللهِ مَا زَيْدٌ بِقَائِمٍ and وَاللهِ لَا يَقُومُ زَيْدٌ." + C_EN,
 "tr": "Kasem üç şeyden biriyle cevaplanır: lâm ile — وَاللهِ لَزَيْدٌ قَائِمٌ ve وَاللهِ لَأَفْعَلَنَّ كَذَا gibi; إِنَّ ile — وَاللهِ إِنَّ زَيْدًا لَقَائِمٌ gibi; مَا ve لَا gibi nefy ile — وَاللهِ مَا زَيْدٌ بِقَائِمٍ ve وَاللهِ لَا يَقُومُ زَيْدٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَيُجَابُ", "ajaba", "verb", ["naib-al-fail", "form-iv-verbs", "hollow-verbs"], "يُجَابُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is answered».", "«ve cevaplanır».", "يُجَابُ"),
  W("الْقَسَمُ", "qasam", "noun", ["naib-al-fail", K], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the oath».", "«kasem»."),
  bi_("بِأَحَدِ", "ahad", "noun", ["idafa-definiteness"], "أَحَدِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by one of».", "«... -den biriyle».", "أَحَدِ"),
  W("ثَلَاثَةٍ", "thalatha", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«three».", "«üç şey».", punct=":"),
  bi_("بِاللَّامِ", "lam-letter", "noun", [K, "nun-tawkid"], "اللَّامِ مَجْرُورٌ — بَدَلٌ مِنْ بِأَحَدِ.", "«by the lām».", "«lâm ile».", "اللَّامِ", punct="،"),
  nahwu(),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ."),
  cited("لَزَيْدٌ", "zayd", "propn", ["mubtada-khabar", K, "nun-tawkid"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd is indeed».", "«Zeyd elbette».", segments=[seg("لَ", "lam-qasam", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«standing».", "«ayaktadır»."),
  cited_wa("وَوَاللهِ", "allah", "propn", [K, HJ], "الْوَاوُ الْأُولَى عَاطِفَةٌ، وَالثَّانِيَةُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«and by God».", "«ve vallahi».", "وَاللهِ", extra_segs=[seg("وَ", "waw-qasam", "prep"), seg("اللهِ", "allah", "propn")]),
  LAF(),
  cited("كَذَا", "kadha", "pron", ["maful-bihi"], "كِنَايَةٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«such-and-such».", "«şöyle».", punct="؛"),
  atf_wa("وَبِإِنَّ", "inna", "part", ["inna-wa-akhawatuha", K], "الْبَاءُ حَرْفُ جَرٍّ، وَإِنَّ فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«and by inna».", "«ve inne ile».", "إِنَّ", extra_segs=[seg("بِ", "bi", "prep"), seg("إِنَّ", "inna", "part")], punct="،"),
  nahwu(),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ."),
  cited("إِنَّ", "inna", "part", ["inna-wa-akhawatuha", K], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — جَوَابُ الْقَسَمِ.", "«indeed».", "«muhakkak»."),
  cited("زَيْدًا", "zayd", "propn", ["inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«Zayd».", "«Zeyd»."),
  cited("لَقَائِمٌ", "qaim", "noun", ["inna-wa-akhawatuha", "inna-wa-akhawatuha"], "اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَقَائِمٌ خَبَرُ إِنَّ مَرْفُوعٌ.", "«is surely standing».", "«elbette ayaktadır».", punct="؛", segments=[seg("لَ", "lam-ibtida", "part"), seg("قَائِمٌ", "qaim", "noun")]),
  atf_wa("وَبِالنَّفْيِ", "nafy", "noun", [K], "الْبَاءُ حَرْفُ جَرٍّ، وَالنَّفْيِ مَجْرُورٌ.", "«and by a negation».", "«ve nefy ile».", "النَّفْيِ", extra_segs=[seg("بِ", "bi", "prep"), seg("النَّفْيِ", "nafy", "noun")]),
  bi_("بِمَا", "ma-nafiya", "part", ["anwa-ma", "la-nafiya"], "مَا فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«with mā».", "«mâ ile».", "مَا"),
  cited_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا مَعْطُوفَةٌ — الْحَرْفُ مَحْكِيٌّ.", "«or lā».", "«ve lâ».", "لَا", punct="،"),
  nahwu(),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ."),
  cited("مَا", "ma-nafiya", "part", ["anwa-ma", "ma-la-laysa-wa-la-al-jins"], "نَافِيَةٌ — جَوَابُ الْقَسَمِ.", "«not».", "«değildir»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  bi_("بِقَائِمٍ", "qaim", "noun", ["mubtada-khabar"], "قَائِمٍ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا خَبَرٌ — الْبَاءُ زَائِدَةٌ.", "«standing».", "«ayakta».", "قَائِمٍ"),
  cited_wa("وَوَاللهِ", "allah", "propn", [K, HJ], "الْوَاوُ الْأُولَى عَاطِفَةٌ، وَالثَّانِيَةُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«and by God».", "«ve vallahi».", "وَاللهِ", extra_segs=[seg("وَ", "waw-qasam", "prep"), seg("اللهِ", "allah", "propn")]),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ — جَوَابُ الْقَسَمِ.", "«not».", "«-maz»."),
  cited("يَقُومُ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«will stand».", "«kalkmaz»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And when a sentence that shows the answer precedes the oath — as زَيْدٌ قَائِمٌ وَاللهِ — or the oath falls between its parts — as زَيْدٌ وَاللهِ قَائِمٌ — the answer of the oath is dropped." + C_EN,
 "tr": "Kasemin cevabına delâlet eden cümle kasemden önce geldiğinde — زَيْدٌ قَائِمٌ وَاللهِ gibi — ya da kasem o cümlenin cüzleri arasında olduğunda — زَيْدٌ وَاللهِ قَائِمٌ gibi — kasemin cevabı hazfedilir." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -diğinde».", "إِذَا"),
  W("تَقَدَّمَتِ", "taqaddama", "verb", ["idha-shartiyya", "fail", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — فِعْلُ الشَّرْطِ.", "«precedes».", "«önce geldiğinde».", segments=[seg("تَقَدَّمَ", "taqaddama", "verb"), seg("تِ", "ta-tanith", "part")]),
  W("الْجُمْلَةُ", "jumla", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the sentence».", "«cümle»."),
  W("الدَّالَّةُ", "dalla", "noun", ["naat-sifa", "ism-fail", "doubled-verbs"], "صِفَةٌ مَرْفُوعَةٌ — اسْمُ فَاعِلٍ مِنْ دَلَّ.", "«that shows».", "«delâlet eden»."),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«-».", "«-e»."),
  W("جَوَابِ", "jawab", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the answer of».", "«cevabına»."),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasemin»."),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«-».", "«-den»."),
  W("الْقَسَمِ", "qasam", "noun", [HJ, K], "مَجْرُورٌ.", "«the oath».", "«kasemden».", punct="،"),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الْجُمْلَةُ دَالَّةٌ عَلَى الْجَوَابِ.", "«is standing».", "«ayaktadır»."),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — وَالْجَوَابُ مَحْذُوفٌ.", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("تَوَسَّطَ", "tawassata", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى تَقَدَّمَتْ.", "«falls between».", "«ortasında olduğunda»."),
  W("الْقَسَمُ", "qasam", "noun", ["fail", K], "فَاعِلٌ مَرْفُوعٌ.", "«the oath».", "«kasem»."),
  W("بَيْنَ", "bayna", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasında»."),
  W("جُزْأَيْهَا", "juz", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، وَهَا مُضَافٌ إِلَيْهِ.", "«its parts».", "«cüzleri».", punct="،", segments=[seg("جُزْأَيْ", "juz", "noun"), pr3fs()]),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  ALLAH_Q("وَاللهِ", "waw-qasam", "«by God».", "«vallahi».", "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — الْقَسَمُ مُعْتَرِضٌ."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is standing».", "«ayaktadır».", punct="،"),
  W("حُذِفَ", "hadhafa", "verb", ["naib-al-fail", "hadhf-wa-taqdir", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ.", "«is dropped».", "«hazfedilir»."),
  W("جَوَابُ", "jawab", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the answer of».", "«cevabı»."),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasemin».", punct="."),
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
 "waw-qasam": need("waw-qasam", "وَ (الْقَسَم)", "و", "prep", "the wāw of the oath — a jarr letter on an explicit noun with the verb of swearing dropped: وَاللهِ", "kasem vâvı — fiili mahzûf, zâhir isme giren cer harfi: وَاللهِ", 4),
 "ba-qasam": need("ba-qasam", "بِ (الْقَسَم)", "ب", "prep", "the bāʾ of the oath — the most general oath letter: with or without the verb, on noun or pronoun", "kasem bâsı — en umumî kasem harfi: fiilli ya da fiilsiz, isimde ya da zamirde", 4),
 "nun-tawkid-seg": need("nun-tawkid-seg", "نَّ (نُونُ التَّوْكِيدِ)", "ن", "part", "the heavy nūn of emphasis on the verb of an oath's answer", "kasem cevabındaki fiilin şeddeli te'kid nûnu", 4),
 "dun": need("dun", "دُون", "د و ن", "noun", "without, short of; below (a ẓarf, always annexed)", "-sız, -den aşağı (daima muzâf bir zarf)", 3),
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
print("kafiya ch32 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "حُرُوفُ الْقَسَمِ وَجَوَابُهُ فِي الْكَافِيَةِ", "en": "The oath letters in the Kafiya: the wāw's three restrictions, the tāʾ on the name of God, the bāʾ's generality, the three answers, and when the answer is dropped", "tr": "Kâfiye'de kasem harfleri: vâvın üç kaydı, Allah lafzındaki tâ, bâ'nın umumîliği, üç cevap ve cevabın düştüğü yer"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — واو القسم لا تستعمل إلا بحذف الفعل، ولغير السؤال، ومختصة بالاسم الظاهر؛ والتاء كالواو مختصة باسم الله؛ والباء أعم", "ضياء صونغور اوغلى — دفتر الكافية: جواب القسم باللام وإن والنفي؛ حذف الجواب إذا تقدمت الجملة الدالة عليه أو توسط القسم"],
 "question": {
  "en": ["What does the wāw of the oath refuse? Three things: a stated verb (أَقْسَمْتُ وَاللهِ is not said — the wāw already means «I swear»), a request (وَاللهِ أَخْبِرْنِي is not said), and a pronoun (وَكَ is not said). Each refusal is a test the analyzer can run on the surface.",
         "And the tāʾ? Everything the wāw refuses, plus one more: it takes no noun but the name of God — تَاللهِ and nothing else.",
         "Why is the bāʾ «more general»? Because it passes every test the other two fail: أُقْسِمُ بِاللهِ with the verb, بِاللهِ without it, بِاللهِ لَأَفْعَلَنَّ in a statement, بِاللهِ اجْلِسْ in a request, and بِكَ لَأَفْعَلَنَّ on a pronoun. The three letters are one meaning at three widths.",
         "How is an oath answered? By one of three heads: the lām (لَزَيْدٌ قَائِمٌ, لَأَفْعَلَنَّ — with the emphatic nūn on a verb), إِنَّ (إِنَّ زَيْدًا لَقَائِمٌ), or a negation (مَا زَيْدٌ بِقَائِمٍ, لَا يَقُومُ زَيْدٌ). The kernel's oath detector looks for exactly these three after a majrūr name of God.",
         "When is the answer missing? When the sentence that would be the answer already stands before the oath (زَيْدٌ قَائِمٌ وَاللهِ) or has the oath lodged inside it (زَيْدٌ وَاللهِ قَائِمٌ). The answer is then said to be dropped, because the earlier sentence shows it — the HadhfEngine's rule for the jawāb al-qasam.",
         "What does the engine do? The oath letters are registered in the PARTICLES table with their restrictions; the HadhfEngine audits the dropped jawāb; and the SignEngine reads لَأَفْعَلَنَّ as built on the fatḥa because of the nūn, not as manṣūb."],
  "tr": ["Kasem vâvı neyi reddeder? Üç şeyi: açık bir fiili (أَقْسَمْتُ وَاللهِ denmez — vâv zaten «yemin ederim» demektir), bir isteği (وَاللهِ أَخْبِرْنِي denmez) ve bir zamiri (وَكَ denmez). Her ret, analizörün yüzeyde çalıştırabileceği bir testtir.",
         "Ya tâ? Vâvın reddettiği her şey, artı bir tane daha: Allah lafzından başka isim almaz — تَاللهِ, başka hiçbir şey.",
         "Bâ neden «daha umumî»dir? Çünkü ötekilerin kaldığı her testten geçer: fiille أُقْسِمُ بِاللهِ, fiilsiz بِاللهِ, haberde بِاللهِ لَأَفْعَلَنَّ, sualde بِاللهِ اجْلِسْ ve zamirde بِكَ لَأَفْعَلَنَّ. Üç harf, üç genişlikte tek mânâdır.",
         "Kasem nasıl cevaplanır? Üç baştan biriyle: lâm (لَزَيْدٌ قَائِمٌ, لَأَفْعَلَنَّ — fiilde te'kid nûnuyla), إِنَّ (إِنَّ زَيْدًا لَقَائِمٌ) ya da nefy (مَا زَيْدٌ بِقَائِمٍ, لَا يَقُومُ زَيْدٌ). Çekirdeğin kasem dedektörü mecrûr Allah lafzından sonra tam bu üçünü arar.",
         "Cevap ne zaman yoktur? Cevap olacak cümle zaten kasemden önce durduğunda (زَيْدٌ قَائِمٌ وَاللهِ) ya da kasem onun içine yerleştiğinde (زَيْدٌ وَاللهِ قَائِمٌ). O zaman cevap hazfedilmiş sayılır, çünkü önceki cümle onu gösterir — HadhfEngine'in cevâb-ı kasem kuralı.",
         "Motor ne yapar? Kasem harfleri kayıtlarıyla PARTICLES tablosuna kayıtlıdır; HadhfEngine mahzûf cevabı denetler; SignEngine لَأَفْعَلَنَّ'yi mansûb değil nûn sebebiyle fetha üzere mebnî okur."]},
 "plain": {
  "en": "Arabic swears with three letters: wa-llāhi, ta-llāhi, bi-llāhi. The wāw needs no «I swear», cannot ask for anything and takes no pronoun; the tāʾ works only on God's name; the bāʾ does everything. An oath is answered by «surely», by inna, or by «not»; the answer is left out when the sentence around it says it.",
  "tr": "Arapça üç harfle yemin eder: vallahi, tallahi, billâhi. Vâv «yemin ederim» istemez, bir şey isteyemez ve zamir almaz; tâ yalnız Allah lafzında işler; bâ her şeyi yapar. Kasem «elbette» ile, inne ile ya da «değil» ile cevaplanır ve çevresindeki cümle onu zaten söylüyorsa cevap bırakılabilir."},
 "explanation": {
  "en": "The three oath letters are presented as the notebook presents them: by what each may and may not do. The wāw's three bars — no stated verb, no request, no pronoun — are each given with the sentence that is not said, which is the madrasah's way of teaching a prohibition. The tāʾ inherits them and adds the restriction to the name of God. The bāʾ is defined as the widest of the three, and the notebook proves it by walking the bāʾ through every door the wāw cannot open: the stated verb, the request, the pronoun. The answer of the oath is then given in the three heads with their paired examples, and the chapter closes with the rule of the dropped answer, which is really a rule about order: an answer-sentence that stands before the oath, or that the oath interrupts, is not repeated. Two notes for the parser: لَأَفْعَلَنَّ is a muḍāriʿ built on the fatḥa because of the heavy nūn, not a manṣūb; and in مَا زَيْدٌ بِقَائِمٍ the bāʾ is the redundant bāʾ of the previous chapters, so قَائِمٍ is majrūr in letter and khabar in place.",
  "tr": "Üç kasem harfi defterin sunduğu gibi sunulur: her birinin yapabildiği ve yapamadığıyla. Vâvın üç yasağı — açık fiil yok, istek yok, zamir yok — her biri söylenmeyen cümleyle verilir; medresenin yasak öğretme yolu budur. Tâ bunları devralır ve Allah lafzı kaydını ekler. Bâ üçün en genişi olarak tarif edilir ve defter bunu bâ'yı vâvın açamadığı her kapıdan geçirerek kanıtlar: açık fiil, istek, zamir. Sonra kasemin cevabı çift örnekli üç başla verilir ve bâb, aslında bir sıra kuralı olan mahzûf cevap kuralıyla kapanır: kasemden önce duran ya da kasemin böldüğü cevap cümlesi tekrarlanmaz. Çözümleyici için iki not: لَأَفْعَلَنَّ şeddeli nûn sebebiyle fetha üzere mebnî bir muzâridir, mansûb değil; مَا زَيْدٌ بِقَائِمٍ'deki bâ önceki bâbların zâid bâ'sıdır, dolayısıyla قَائِمٍ lafzen mecrûr, mahallen haberdir."},
 "examples": [
  {"ar": "أَقْسَمْتُ وَاللهِ — وَاللهِ أَخْبِرْنِي — وَكَ", "en": "The three things the wāw refuses.", "tr": "Vâvın reddettiği üç şey.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "تَاللهِ", "en": "The tāʾ on the name of God.", "tr": "Allah lafzında tâ.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "أُقْسِمُ بِاللهِ — بِاللهِ اجْلِسْ — بِكَ لَأَفْعَلَنَّ", "en": "The bāʾ passes every door.", "tr": "Bâ her kapıdan geçer.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "وَاللهِ لَزَيْدٌ قَائِمٌ — وَاللهِ إِنَّ زَيْدًا لَقَائِمٌ — وَاللهِ مَا زَيْدٌ بِقَائِمٍ", "en": "The three answers.", "tr": "Üç cevap.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "زَيْدٌ قَائِمٌ وَاللهِ — زَيْدٌ وَاللهِ قَائِمٌ", "en": "The answer dropped.", "tr": "Mahzûf cevap.", "sourceStory": "al-kafiya", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«أَقْسَمْتُ وَاللهِ»",
   "right": "«أُقْسِمُ بِاللهِ — fiil açıkça gelince kasem harfi bâ'dır»",
   "why": {"en": "The wāw is used only with the verb dropped.", "tr": "Vâv ancak fiilin hazfiyle kullanılır."}},
  {"wrong": "«تَرَبِّي»",
   "right": "«تَاللهِ — tâ yalnız Allah lafzına girer; وَرَبِّي، بِرَبِّي»",
   "why": {"en": "The tāʾ is confined to the name of God.", "tr": "Tâ Allah lafzına mahsustur."}},
  {"wrong": "«وَاللهِ لَأَفْعَلَنَّ — mansûb muzâri»",
   "right": "«te'kid nûnu sebebiyle fetha üzere mebnî muzâri»",
   "why": {"en": "The heavy nūn builds the verb; nothing governs it in naṣb.", "tr": "Şeddeli nûn fiili mebnî kılar; onu nasb eden bir şey yoktur."}},
  {"wrong": "«زَيْدٌ وَاللهِ قَائِمٌ — cevap قَائِمٌ'dur»",
   "right": "«cevap mahzûftur; قَائِمٌ, زَيْدٌ'ün haberidir»",
   "why": {"en": "An oath lodged inside a sentence takes no separate answer.", "tr": "Cümle içine yerleşen kasem ayrı cevap almaz."}}],
 "relatedNotes": ["al-lam-wa-rubba-fil-kafiya", "huruf-jarr", "nun-tawkid", "inna-wa-akhawatuha", "hadhf-wa-taqdir", "qasr"]}

ADD_EN = (" Chapter 32 (notebook line ~334): the wāw, tāʾ and bāʾ of the oath with their restrictions, the three answers of the oath, and the dropped answer — the notebook's exposition, kept as commentary (s1-s5).")
ADD_TR = (" Otuz ikinci bâb (defter satırı ~334): kasemin vâvı, tâsı ve bâsı kayıtlarıyla, kasemin üç cevabı ve mahzûf cevap — defterin açıklaması, şerh olarak (s1-s5).")
write_out(32, S, TITLE, ADD_EN, ADD_TR, "334", GLOSS_ADD, notes=(NOTE,),
          related=(("al-lam-wa-rubba-fil-kafiya", [K]), ("nun-tawkid", [K])))
report(32, S, GLOSS_ADD, (NOTE,))
