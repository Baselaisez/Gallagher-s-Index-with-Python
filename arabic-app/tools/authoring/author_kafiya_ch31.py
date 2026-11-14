# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 31: THE JARR LETTERS (III) — the lām for appropriation, for cause, in the sense of عَنْ with the verb of saying,
redundant (27:72), and for the wāw of the oath of wonder; رُبَّ for paucity, at the head of speech, on a described indefinite, later used
for abundance, its disputed mutaʿallaq (al-Birgivī against the majority), its vague pronoun with a tamyīz (Basrans vs Kufans), and the
مَا that stops its government (15:2); the wāw that stands for رُبَّ (the verse of the empty town).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~333-334 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch31.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-lam-wa-rubba-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الْجَرِّ: اللَّامُ وَرُبَّ وَوَاوُهَا", "en": "The jarr letters — the lām, rubba and the wāw of rubba", "tr": "Cer harfleri — lâm, rubbe ve rubbe vâvı"}
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
def FOR(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return li_(full, lex, "noun", ["mubtada-khabar", K] + list(tags), inner + " مَجْرُورٌ — خَبَرٌ.", en, tr, inner, punct=punct, segs=segs)
def FORW(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return W(full, lex, "noun", ["atf-nasaq", HJ, K] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَ" + inner + " مَجْرُورٌ — مَعْطُوفٌ عَلَى الْخَبَرِ.", en, tr, punct=punct, segments=(segs if segs else [seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg(inner, lex, "noun")]))
def RUBBA(ar="حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ لِلتَّقْلِيلِ.", punct=None, segs=None, full="رُبَّ"): return cited(full, "rubba", "prep", [K, HJ], ar, "«many a / how few».", "«nice / ne az».", punct=punct, segments=segs)
def RUBBAH(full, prn, en, tr, side="الْبَصْرِيِّينَ"): return cited(full, "rubba", "prep", [K, HJ, "tamyiz"], "رُبَّ حَرْفُ جَرٍّ، وَالضَّمِيرُ مَجْرُورٌ مُبْهَمٌ يُفَسِّرُهُ التَّمْيِيزُ — عِنْدَ " + side + ".", en, tr, segments=[seg("رُبَّ", "rubba", "prep"), prn])
def TAM(full, lex, en, tr, punct=None, tags=()): return cited(full, lex, "noun", [K, "tamyiz"] + list(tags), "تَمْيِيزٌ مَنْصُوبٌ لِلضَّمِيرِ الْمُبْهَمِ.", en, tr, punct=punct)

S.append({"id": "s1", "translation": {
 "en": "And the lām is for appropriation, as الْمَالُ لِزَيْدٍ; for cause, as ضَرَبْتُ لِلتَّأْدِيبِ; and in the sense of عَنْ with the verb of saying, as قُلْتُ لِزَيْدٍ." + C_EN,
 "tr": "Lâm ihtisas içindir, الْمَالُ لِزَيْدٍ gibi; ta'lil içindir, ضَرَبْتُ لِلتَّأْدِيبِ gibi; ve kavl maddesiyle birlikte عَنْ mânâsındadır, قُلْتُ لِزَيْدٍ gibi." + C_TR},
 "tokens": [
  atf_wa("وَاللَّامُ", "lam-letter", "noun", ["mubtada-khabar", K, HJ], "اللَّامُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the lām».", "«ve lâm».", "اللَّامُ"),
  FOR("لِلِاخْتِصَاصِ", "ikhtisas", "«is for appropriation».", "«ihtisas içindir».", "الِاخْتِصَاصِ", segs=[seg("لِ", "li", "prep"), seg("لِاخْتِصَاصِ", "ikhtisas", "noun")], punct="،"),
  nahwu(),
  cited("الْمَالُ", "mal", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the property».", "«mal»."),
  li_("لِزَيْدٍ", "zayd", "propn", [K, "khabar-al-mubtada-wa-ahkamuh"], "زَيْدٍ مَجْرُورٌ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ؛ اللَّامُ لِلِاخْتِصَاصِ.", "«belongs to Zayd».", "«Zeyd'indir».", "زَيْدٍ", punct="؛"),
  FORW("وَلِلتَّعْلِيلِ", "talil", "«and for cause».", "«ve ta'lil içindir».", "التَّعْلِيلِ", segs=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لتَّعْلِيلِ", "talil", "noun")], punct="،", tags=["lam-taleel"]),
  nahwu(),
  cited("ضَرَبْتُ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck».", "«dövdüm».", segments=[seg("ضَرَبْ", "daraba", "verb"), prT()]),
  li_("لِلتَّأْدِيبِ", "tadib", "noun", [K, "lam-taleel", "maful-lah"], "التَّأْدِيبِ مَجْرُورٌ — لَامُ التَّعْلِيلِ.", "«for discipline».", "«edeplendirmek için».", "التَّأْدِيبِ", segs=[seg("لِ", "lam-taleel", "part"), seg("لتَّأْدِيبِ", "tadib", "noun")], punct="؛"),
  atf_wa("وَبِمَعْنَى", "mana", "noun", ["atf-nasaq", "idafa-definiteness", K], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ مُضَافٌ — مَعْطُوفٌ عَلَى الْخَبَرِ.", "«and in the sense of».", "«ve ... mânâsındadır».", "مَعْنَى", extra_segs=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  cited("عَنْ", "an-jarr", "prep", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«ʿan».", "«an»."),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile birlikte»."),
  W("الْقَوْلِ", "qawl", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb of saying».", "«kavl maddesi».", punct="،"),
  nahwu(),
  cited("قُلْتُ", "qala", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I spoke».", "«söz ettim».", segments=[seg("قُلْ", "qala", "verb"), prT()]),
  li_("لِزَيْدٍ", "zayd", "propn", [K], "زَيْدٍ مَجْرُورٌ — اللَّامُ بِمَعْنَى عَنْ: قُلْتُ عَنْهُ.", "«about Zayd».", "«Zeyd hakkında».", "زَيْدٍ", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And redundant, as رَدِفَ لَكُمْ; and in the sense of the wāw in the oath of wonder, as لِلَّهِ لَا يُؤَخَّرُ الْأَجَلُ." + C_EN,
 "tr": "Ve zâid olur, رَدِفَ لَكُمْ gibi; taaccüb için olan kasemde vâv mânâsında olur, لِلَّهِ لَا يُؤَخَّرُ الْأَجَلُ gibi." + C_TR},
 "tokens": [
  atf_wa("وَزَائِدَةً", "zaid", "noun", ["hal", K], "زَائِدَةً حَالٌ مِنَ اللَّامِ: وَتَكُونُ زَائِدَةً.", "«and redundant».", "«ve zâid olur».", "زَائِدَةً", punct="،"),
  nahwu(),
  cited("رَدِفَ", "radifa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«has drawn near».", "«yaklaştı»."),
  cited("لَكُمْ", "li", "prep", [K, "maful-bihi"], "اللَّامُ زَائِدَةٌ، وَكُمْ مَفْعُولٌ بِهِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — رَدِفَكُمْ.", "«to you».", "«size».", punct="؛", segments=[seg("لَ", "li", "prep"), pr2mp()]),
  atf_wa("وَبِمَعْنَى", "mana", "noun", ["atf-nasaq", "idafa-definiteness", K], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ مُضَافٌ.", "«and in the sense of».", "«ve ... mânâsında olur».", "مَعْنَى", extra_segs=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness", "anwa-al-waw"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wāw».", "«vâv»."),
  W("فِي", "fi", "prep", [HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْقَسَمِ", "qasam", "noun", [HJ, "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the oath of».", "«kasemde»."),
  W("لِلتَّعَجُّبِ", "taajjub", "noun", ["lam-taleel", "fil-al-taajjub-fil-kafiya"], "اللَّامُ لِلتَّعْلِيلِ، وَالتَّعَجُّبِ مَجْرُورٌ.", "«wonder».", "«taaccüb için olan».", punct="،", segments=[seg("لِ", "lam-taleel", "part"), seg("لتَّعَجُّبِ", "taajjub", "noun")]),
  nahwu(),
  cited("لِلَّهِ", "allah", "propn", [K, HJ], "اللَّامُ لِلْقَسَمِ بِمَعْنَى الْوَاوِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — الْمُقْسَمُ بِهِ.", "«by God!».", "«Allah'a yemin olsun».", segments=[seg("لِ", "li", "prep"), seg("لَّهِ", "allah", "propn")]),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ — جَوَابُ الْقَسَمِ.", "«not».", "«-mez»."),
  cited("يُؤَخَّرُ", "akhkhara", "verb", ["naib-al-fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is delayed».", "«ertelenmez»."),
  cited("الْأَجَلُ", "ajal", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the appointed term».", "«ecel».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And رُبَّ is for paucity; it has the head of speech; and on the soundest view it is confined to a described indefinite. Its original setting is paucity, but it was later used for abundance." + C_EN,
 "tr": "رُبَّ taklil içindir; sadr-ı kelâm onundur; en sahih görüşe göre mevsûf bir nekreye mahsustur. Asıl vaz'ı taklildir, fakat sonradan teksir için kullanılmıştır." + C_TR},
 "tokens": [
  cited_wa("وَرُبَّ", "rubba", "prep", ["mubtada-khabar", K, HJ], "رُبَّ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and rubba».", "«ve rubbe».", "رُبَّ"),
  FOR("لِلتَّقْلِيلِ", "taqlil", "«is for paucity».", "«taklil içindir».", "التَّقْلِيلِ", segs=[seg("لِ", "li", "prep"), seg("لتَّقْلِيلِ", "taqlil", "noun")], punct="؛"),
  atf_wa("وَلَهَا", "li", "prep", [HJ, "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and it has».", "«ve ... onundur».", "لَهَا", extra_segs=[seg("لَ", "li", "prep"), pr3fs()]),
  W("صَدْرُ", "sadr", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«sadr-ı»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«speech».", "«kelâm».", punct="؛"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on».", "«göre»."),
  W("الْأَصَحِّ", "asahh", "noun", [HJ, "ism-tafdil"], "مَجْرُورٌ.", "«the soundest view».", "«en sahih görüşe»."),
  W("مُخْتَصَّةٌ", "mukhtass", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is confined».", "«mahsustur»."),
  bi_("بِنَكِرَةٍ", "nakira", "noun", ["al-marifa-wal-nakira-fil-kafiya"], "نَكِرَةٍ مَجْرُورٌ.", "«to an indefinite».", "«bir nekreye».", "نَكِرَةٍ"),
  W("مَوْصُوفَةٍ", "mawsuf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«described».", "«mevsûf».", punct="."),
  atf_wa("وَأَصْلُهَا", "asl", "noun", ["mubtada-khabar", "idafa-definiteness"], "أَصْلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its original setting».", "«asıl vaz'ı».", "أَصْلُ", extra_segs=[seg("أَصْلُ", "asl", "noun"), pr3fs()]),
  W("التَّقْلِيلُ", "taqlil", "noun", ["mubtada-khabar", K], "خَبَرٌ مَرْفُوعٌ.", "«is paucity».", "«taklildir».", punct="،"),
  W("ثُمَّ", "thumma", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«but later».", "«fakat sonradan»."),
  W("اسْتُعْمِلَتْ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it was used».", "«kullanılmıştır».", segments=[seg("اسْتُعْمِلَ", "istamala", "verb"), seg("تْ", "ta-tanith", "part")]),
  li_("لِلتَّكْثِيرِ", "takthir", "noun", [K, "lam-taleel"], "التَّكْثِيرِ مَجْرُورٌ.", "«for abundance».", "«teksir için».", "التَّكْثِيرِ", segs=[seg("لِ", "li", "prep"), seg("لتَّكْثِيرِ", "takthir", "noun")], punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And on what it hangs on there are two views: for al-Birgivī it has nothing to hang on; for most, what it hangs on is a dropped past verb — as رُبَّ رَجُلٍ كَرِيمٍ, that is, لَقِيتُهُ." + C_EN,
 "tr": "Müteallakında iki görüş vardır: Birgivî'ye göre müteallakı yoktur; çoğunluğa göre müteallakı mahzûf bir mâzî fiildir — رُبَّ رَجُلٍ كَرِيمٍ gibi, yani لَقِيتُهُ." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", [HJ, "khabar-al-mubtada-wa-ahkamuh"], "فِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and on».", "«ve ... -da».", "فِي"),
  W("مُتَعَلَّقِهَا", "mutaallaq", "noun", [HJ, "idafa-definiteness", "ism-maful"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«what it hangs on».", "«müteallakında».", segments=[seg("مُتَعَلَّقِ", "mutaallaq", "noun"), pr3fs()]),
  W("قَوْلَانِ", "qawl", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«there are two views».", "«iki görüş vardır».", punct=":"),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ مُقَدَّمٌ لِلَا.", "«for».", "«... göre»."),
  W("الْبِرْكِوِيِّ", "birgivi", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Birgivī».", "«Birgivî'ye»."),
  W("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"], "نَافِيَةٌ لِلْجِنْسِ.", "«no».", "«yoktur»."),
  W("مُتَعَلَّقَ", "mutaallaq", "noun", ["la-nafiya-lil-jins", "ism-maful"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«thing to hang on».", "«müteallakı»."),
  W("لَهَا", "li", "prep", [HJ, "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَا.", "«has it».", "«onun».", punct="؛", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْأَكْثَرِ", "akthar", "noun", ["idafa-definiteness", "ism-tafdil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«most».", "«çoğunluğa»."),
  W("مُتَعَلَّقُهَا", "mutaallaq", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«what it hangs on».", "«müteallakı».", segments=[seg("مُتَعَلَّقُ", "mutaallaq", "noun"), pr3fs()]),
  W("فِعْلٌ", "fil", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a verb».", "«bir ... fiildir»."),
  W("مَاضٍ", "madi", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ.", "«past».", "«mâzî»."),
  W("مَحْذُوفٌ", "mahdhuf", "noun", ["naat-sifa", "hadhf-wa-taqdir"], "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ.", "«dropped».", "«mahzûf».", punct="،"),
  nahwu(),
  RUBBA(),
  cited("رَجُلٍ", "rajul", "noun", [K, HJ, "maful-bihi"], "مَجْرُورٌ لَفْظًا بِرُبَّ، مَنْصُوبٌ مَحَلًّا مَفْعُولٌ بِهِ لِلْفِعْلِ الْمَحْذُوفِ.", "«a man».", "«adam»."),
  cited("كَرِيمٍ", "karim", "noun", ["naat-sifa", "sifa-mushabbaha"], "صِفَةٌ مَجْرُورَةٌ — النَّكِرَةُ مَوْصُوفَةٌ.", "«noble».", "«değerli».", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("لَقِيتُهُ", "laqiya", "verb", ["fail", "maful-bihi", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ مَحْذُوفٌ مُقَدَّرٌ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — مُتَعَلَّقُ رُبَّ.", "«I met him».", "«ona rastladım».", punct=".", segments=[seg("لَقِي", "laqiya", "verb"), prT(), pr3ms()]),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And it sometimes enters on a vague pronoun distinguished by a manṣūb indefinite: for the Basrans the pronoun is always masculine singular — رُبَّهُ رَجُلًا, رُبَّهُ رِجَالًا, رُبَّهُ امْرَأَةً — and for the Kufans it matches the tamyīz — رُبَّهُمَا رَجُلَيْنِ, رُبَّهُمْ رِجَالًا, رُبَّهَا امْرَأَةً." + C_EN,
 "tr": "Bazen mansûb bir nekre ile temyiz edilmiş mübhem bir zamir üzerine girer: Basralılara göre zamir daima müfred müzekkerdir — رُبَّهُ رَجُلًا, رُبَّهُ رِجَالًا, رُبَّهُ امْرَأَةً — Kûfelilere göre temyize mutâbık olur — رُبَّهُمَا رَجُلَيْنِ, رُبَّهُمْ رِجَالًا, رُبَّهَا امْرَأَةً." + C_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("تَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«it enters».", "«girer»."),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("ضَمِيرٍ", "damir", "noun", [HJ, "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«a pronoun».", "«bir zamir»."),
  W("مُبْهَمٍ", "mubham", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«vague».", "«mübhem»."),
  W("مُمَيَّزٍ", "mumayyaz", "noun", ["naat-sifa", "ism-maful", "tamyiz"], "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ.", "«distinguished».", "«temyiz edilmiş»."),
  bi_("بِنَكِرَةٍ", "nakira", "noun", ["tamyiz"], "نَكِرَةٍ مَجْرُورٌ.", "«by an indefinite».", "«bir nekre ile».", "نَكِرَةٍ"),
  W("مَنْصُوبَةٍ", "mansub", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«manṣūb».", "«mansûb».", punct=":"),
  W("فَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-fa-fi-khabar-al-mubtada", "khabar-al-mubtada-wa-ahkamuh"], "الْفَاءُ لِلتَّفْرِيعِ، وَعِنْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«for».", "«... göre».", segments=[seg("فَ", "fa", "conj"), seg("عِنْدَ", "inda", "noun")]),
  W("الْبَصْرِيِّينَ", "basri", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Basrans».", "«Basralılara»."),
  W("الضَّمِيرُ", "damir", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the pronoun».", "«zamir»."),
  W("مُفْرَدٌ", "mufrad", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is singular».", "«müfred»."),
  W("مُذَكَّرٌ", "mudhakkar", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«masculine».", "«müzekkerdir»."),
  W("أَبَدًا", "abadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«always».", "«daima».", punct="،"),
  nahwu(),
  RUBBAH("رُبَّهُ", pr3ms(), "«many a one, as a man».", "«nice kimse, adam olarak»."),
  TAM("رَجُلًا", "rajul", "«as a man».", "«adam olarak».", punct="،"),
  RUBBAH("رُبَّهُ", pr3ms(), "«many a one, as men».", "«nice kimse, adamlar olarak»."),
  TAM("رِجَالًا", "rijal", "«as men».", "«adamlar olarak».", punct="،", tags=["jam-taksir"]),
  RUBBAH("رُبَّهُ", pr3ms(), "«many a one, as a woman».", "«nice kimse, kadın olarak»."),
  TAM("امْرَأَةً", "imraa", "«as a woman».", "«kadın olarak».", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْكُوفِيِّينَ", "kufi", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Kufans».", "«Kûfelilere»."),
  W("يُطَابِقُ", "tabaqa", "verb", ["fail", "form-iii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الضَّمِيرُ.", "«it matches».", "«mutâbık olur»."),
  W("التَّمْيِيزَ", "tamyiz-noun", "noun", ["maful-bihi", "tamyiz"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the tamyīz».", "«temyize».", punct="،"),
  nahwu(),
  RUBBAH("رُبَّهُمَا", pr3d(), "«many a pair, as two men».", "«nice ikisi, iki adam olarak».", side="الْكُوفِيِّينَ"),
  TAM("رَجُلَيْنِ", "rajul", "«as two men».", "«iki adam olarak».", punct="،", tags=["al-muthanna"]),
  RUBBAH("رُبَّهُمْ", pr3mp(), "«many a group, as men».", "«nice onlar, adamlar olarak».", side="الْكُوفِيِّينَ"),
  TAM("رِجَالًا", "rijal", "«as men».", "«adamlar olarak».", punct="،", tags=["jam-taksir"]),
  RUBBAH("رُبَّهَا", pr3fs(), "«many a she, as a woman».", "«nice o, kadın olarak».", side="الْكُوفِيِّينَ"),
  TAM("امْرَأَةً", "imraa", "«as a woman».", "«kadın olarak».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And the مَا that stops it governing attaches to it, and then it enters on a sentence — as رُبَمَا يَوَدُّ الَّذِينَ كَفَرُوا لَوْ كَانُوا مُسْلِمِينَ." + C_EN,
 "tr": "Amelden alıkoyan مَا ona bitişir ve o zaman cümle üzerine girer — رُبَمَا يَوَدُّ الَّذِينَ كَفَرُوا لَوْ كَانُوا مُسْلِمِينَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتَلْحَقُهَا", "lahiqa", "verb", ["fail", "maful-bihi"], "تَلْحَقُ فِعْلٌ مُضَارِعٌ، وَهَا مَفْعُولٌ بِهِ.", "«and attaches to it».", "«ve ona bitişir».", "تَلْحَقُ", extra_segs=[seg("تَلْحَقُ", "lahiqa", "verb"), pr3fs()]),
  cited("مَا", "ma-kaffa", "part", ["fail", "anwa-ma"], "فَاعِلٌ — الْحَرْفُ مَحْكِيٌّ.", "«the mā».", "«mâ»."),
  W("الْكَافَّةُ", "ma-kaffa-adj", "noun", ["naat-sifa", "ism-fail", "anwa-ma"], "صِفَةٌ مَرْفُوعَةٌ — الْمَانِعَةُ مِنَ الْعَمَلِ.", "«that stops it governing».", "«kâffe».", punct="،"),
  W("فَتَدْخُلُ", "dakhala", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَدْخُلُ فِعْلٌ مُضَارِعٌ.", "«and then it enters».", "«o zaman girer».", segments=[seg("فَ", "fa", "conj"), seg("تَدْخُلُ", "dakhala", "verb")]),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الْجُمْلَةِ", "jumla", "noun", [HJ], "مَجْرُورٌ.", "«a sentence».", "«cümle».", punct="،"),
  nahwu(),
  cited("رُبَمَا", "rubba", "prep", [K, HJ, "anwa-ma"], "رُبَّ مُخَفَّفَةٌ مَكْفُوفَةٌ بِمَا عَنِ الْعَمَلِ.", "«perhaps / often».", "«nice kere».", segments=[seg("رُبَ", "rubba", "prep"), seg("مَا", "ma-kaffa", "part")]),
  cited("يَوَدُّ", "wadda", "verb", ["fail", "doubled-verbs", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«will wish».", "«arzu ederler»."),
  cited("الَّذِينَ", "alladhina", "pron", ["fail", "ism-mawsul"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«those who».", "«... olanlar»."),
  cited("كَفَرُوا", "kafara", "verb", ["ism-mawsul", "fail"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَالْجُمْلَةُ صِلَةٌ.", "«disbelieved».", "«inkâr edenler».", segments=[seg("كَفَرُ", "kafara", "verb"), seg("وا", "pron-3mp", "pron")]),
  cited("لَوْ", "law", "part", ["an-masdariyya"], "مَصْدَرِيَّةٌ — وَالْمَصْدَرُ مَفْعُولُ يَوَدُّ.", "«that».", "«-mayı»."),
  cited("كَانُوا", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهَا.", "«they had been».", "«olmuş olmayı».", segments=[seg("كَانُ", "kana", "verb"), seg("وا", "pron-3mp", "pron")]),
  cited("مُسْلِمِينَ", "muslim", "noun", ["kana-wa-akhawatuha", "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ كَانُوا مَنْصُوبٌ بِالْيَاءِ.", "«Muslims».", "«müslüman».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And the wāw in the sense of رُبَّ enters on a described indefinite — as وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ إِلَّا الْيَعَافِيرُ وَإِلَّا الْعِيسُ: بَلْدَةٍ is put in jarr by the wāw that means رُبَّ." + C_EN,
 "tr": "رُبَّ mânâsındaki vâv mevsûf bir nekre üzerine girer — وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ إِلَّا الْيَعَافِيرُ وَإِلَّا الْعِيسُ gibi: بَلْدَةٍ, رُبَّ mânâsındaki vâv ile cer olmuştur." + C_TR},
 "tokens": [
  atf_wa("وَالْوَاوُ", "waw-letter", "noun", ["mubtada-khabar", K, HJ, "anwa-al-waw"], "الْوَاوُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the wāw».", "«ve vâv».", "الْوَاوُ"),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — صِفَةٌ لِلْوَاوِ.", "«in the sense of».", "«mânâsındaki».", "مَعْنَى"),
  cited("رُبَّ", "rubba", "prep", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«rubba».", "«rubbe»."),
  W("تَدْخُلُ", "dakhala", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«enters».", "«girer»."),
  W("عَلَى", "ala", "prep", [HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("نَكِرَةٍ", "nakira", "noun", [HJ], "مَجْرُورٌ.", "«an indefinite».", "«bir nekre»."),
  W("مَوْصُوفَةٍ", "mawsuf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«described».", "«mevsûf».", punct="،"),
  nahwu(),
  cited("وَبَلْدَةٍ", "balda", "noun", [K, HJ, "anwa-al-waw"], "الْوَاوُ وَاوُ رُبَّ، وَبَلْدَةٍ مَجْرُورٌ بِهَا.", "«many a town».", "«nice belde».", segments=[seg("وَ", "waw-letter", "noun"), seg("بَلْدَةٍ", "balda", "noun")]),
  cited("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "naat-sifa"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ — الْجُمْلَةُ صِفَةُ بَلْدَةٍ.", "«there is not».", "«yoktur»."),
  cited("بِهَا", "bi", "prep", [HJ, "kana-wa-akhawatuha"], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَيْسَ مُقَدَّمٌ.", "«in it».", "«onda».", segments=[seg("بِ", "bi", "prep"), pr3fs()]),
  cited("أَنِيسٌ", "anis", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ.", "«any companion».", "«hiçbir can»."),
  cited("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«-den başka»."),
  cited("الْيَعَافِيرُ", "yaafir", "noun", ["istithna", "jam-taksir", "mamnu-min-sarf"], "بَدَلٌ مِنْ أَنِيسٌ مَرْفُوعٌ — جَمْعُ يَعْفُورٍ.", "«the wild asses».", "«yaban eşekleri»."),
  cited_wa("وَإِلَّا", "illa", "part", ["istithna"], "إِلَّا مُكَرَّرَةٌ لِلتَّوْكِيدِ.", "«and except».", "«ve ... -den başka».", "إِلَّا"),
  cited("الْعِيسُ", "is-camels", "noun", ["istithna"], "مَعْطُوفٌ عَلَى الْيَعَافِيرُ مَرْفُوعٌ.", "«the white camels».", "«beyaz develer».", punct=":"),
  W("فَبَلْدَةٍ", "balda", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَبَلْدَةٍ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so baldatin».", "«o hâlde beldetin».", segments=[seg("فَ", "fa", "conj"), seg("بَلْدَةٍ", "balda", "noun")]),
  W("مَجْرُورٌ", "majrur", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is put in jarr».", "«cer olmuştur»."),
  bi_("بِالْوَاوِ", "waw-letter", "noun", ["anwa-al-waw"], "الْوَاوِ مَجْرُورٌ.", "«by the wāw».", "«vâv ile».", "الْوَاوِ"),
  W("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ صِفَةٌ.", "«that».", "«... olan»."),
  bi_("بِمَعْنَى", "mana", "noun", ["ism-mawsul", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ مُضَافٌ — الْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«means».", "«mânâsında».", "مَعْنَى"),
  cited("رُبَّ", "rubba", "prep", ["idafa-definiteness", HJ], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«rubba».", "«rubbe».", punct="."),
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
 "radifa": need("radifa", "رَدِفَ", "ر د ف", "verb", "to come close behind, to follow at the back (27:72)", "ardından yaklaşmak, peşinden gelmek (27:72)", 4),
 "wadda": need("wadda", "وَدَّ", "و د د", "verb", "to wish, to love (doubled, first radical wāw: وَدِدْتُ، يَوَدُّ)", "arzu etmek, sevmek (muzâaf ve misâl: وَدِدْتُ، يَوَدُّ)", 3),
 "ma-kaffa-adj": need("ma-kaffa-adj", "كَافَّة", "ك ف ف", "noun", "the مَا that «stops» a governor from governing — مَا الْكَافَّة", "âmili amelden alıkoyan mâ — mâ-i kâffe", 4),
 "birgivi": need("birgivi", "الْبِرْكِوِيّ", "ب ر ك", "propn", "Al-Birgivī (Birgivî Mehmed Efendi, d. 981/1573) — author of the ʿAwāmil and the Iẓhār", "Birgivî Mehmed Efendi (ö. 981/1573) — Avâmil ve İzhâr'ın müellifi", 5),
 "basri": need("basri", "بَصْرِيّ", "ب ص ر", "noun", "Basran — of the Basra school of grammar; plural الْبَصْرِيُّونَ", "Basralı — Basra nahiv mektebinden; cem'i الْبَصْرِيُّونَ", 4),
 "balda": need("balda", "بَلْدَة", "ب ل د", "noun", "a town, a tract of land", "belde, yer", 3),
 "anis": need("anis", "أَنِيس", "أ ن س", "noun", "a companion, one who keeps one company", "enîs, can yoldaşı", 4),
 "yaafir": need("yaafir", "يَعْفُور", "ع ف ر", "noun", "a wild ass (or a gazelle fawn); plural يَعَافِير", "yaban eşeği (ya da ceylan yavrusu); cem'i يَعَافِير", 5),
 "is-camels": need("is-camels", "عِيس", "ع ي س", "noun", "white camels tinged with red (a collective)", "kızıla çalan beyaz develer (cins ismi)", 5),
 "lahiqa": need("lahiqa", "لَحِقَ", "ل ح ق", "verb", "to catch up with, to attach to", "yetişmek, bitişmek", 3),
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
put_morph(mo, "radifa", _nfc(_sg.sound1("samia", "رَدِف", "رْدَف", "اِرْدَف", "رَدَف", "رَادِف", "مَرْدُوف", "رُدِفَ", "يُرْدَفُ", "رَدِفَهُ وَرَدِفَ لَهُ: تَبِعَهُ وَجَاءَ خَلْفَهُ — بَابُ سَمِعَ.")))
put_morph(mo, "lahiqa", _nfc(_sg.sound1("samia", "لَحِق", "لْحَق", "اِلْحَق", "لُحُوق", "لَاحِق", "مَلْحُوق", "لُحِقَ", "يُلْحَقُ", "لَحِقَهُ وَلَحِقَ بِهِ: أَدْرَكَهُ وَاتَّصَلَ بِهِ — بَابُ سَمِعَ.")))
put_morph(mo, "wadda", _nfc(_sg.entry("مِنْ بَابِ فَعِلَ يَفْعَلُ — مُضَاعَفٌ مِثَالٌ (سَمَاعِيٌّ)", "فَعِلَ يَفْعَلُ", "وُدّ", "وَادّ", _sg.mazi14("وَدّ", "وَدِد"), _sg.mudari14("َ", "وَدّ", "وْدَد"), ["وَدَّ", "وَدَّا", "وَدُّوا", "وَدِّي", "وَدَّا", "اِيدَدْنَ"], "يَوَدَّ", "يَوَدَّ", "تَوَدَّ", "مَوْدُود", "وُدَّ", "يُوَدُّ", "وَدَّ الشَّيْءَ: أَحَبَّهُ وَتَمَنَّاهُ — مُضَاعَفٌ أَوَّلُهُ وَاوٌ: وَدِدْتُ، يَوَدُّ، وَالْجَزْمُ بِالْفَتْحِ — لَمْ يَوَدَّ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch31 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "اللَّامُ وَرُبَّ وَوَاوُهَا فِي الْكَافِيَةِ", "en": "The lām and rubba in the Kafiya: appropriation, cause, «about», redundancy and the oath; rubba's paucity, its head position, its described indefinite, its disputed governor, its vague pronoun, its mā, and the wāw that stands for it", "tr": "Kâfiye'de lâm ve rubbe: ihtisas, ta'lil, «hakkında», zâidlik ve kasem; rubbe'nin taklili, sadr-ı kelâm, mevsûf nekresi, ihtilâflı müteallakı, mübhem zamiri, mâ'sı ve yerine geçen vâv"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — اللام للاختصاص والتعليل؛ رب للتقليل ولها صدر الكلام، مختصة بنكرة موصوفة؛ والواو بمعنى رب", "ضياء صونغور اوغلى — دفتر الكافية: اللام بمعنى عن مع القول، زائدة، وبمعنى واو القسم؛ رب أصلها التقليل ثم التكثير؛ متعلقها عند البركوي والأكثر؛ ربه رجلا بين البصريين والكوفيين؛ ما الكافة؛ وبلدة ليس بها أنيس"],
 "question": {
  "en": ["What does the lām do? Four things beside cause: it assigns (الْمَالُ لِزَيْدٍ — the property is Zayd's), it gives the reason (ضَرَبْتُ لِلتَّأْدِيبِ), with a verb of saying it means «about» (قُلْتُ لِزَيْدٍ = عَنْهُ), it can be redundant (رَدِفَ لَكُمْ = رَدِفَكُمْ), and in the oath of wonder it does the wāw's work (لِلَّهِ لَا يُؤَخَّرُ الْأَجَلُ).",
         "What is رُبَّ? A letter of paucity — «how few a…» — that must open its clause and may govern only an indefinite that carries a description. Set down for «few», it came to be used for «many», which is why translators waver between «rarely» and «often».",
         "What does رُبَّ hang on? Al-Birgivī says nothing — it is a letter that governs and stops there. Most say a dropped past verb: رُبَّ رَجُلٍ كَرِيمٍ is complete only as رُبَّ رَجُلٍ كَرِيمٍ لَقِيتُهُ. The TaalluqEngine follows the majority and supplies the verb.",
         "What is رُبَّهُ رَجُلًا? Rubba on a vague pronoun that a manṣūb indefinite explains. The schools divide on the pronoun: the Basrans keep it هُ whatever follows (رُبَّهُ رِجَالًا، رُبَّهُ امْرَأَةً); the Kufans make it agree (رُبَّهُمْ رِجَالًا، رُبَّهَا امْرَأَةً). Both tables are stored.",
         "What happens with رُبَمَا? The مَا is kāffa: it stops رُبَّ governing and lets it enter on a whole sentence — رُبَمَا يَوَدُّ الَّذِينَ كَفَرُوا. The MaEngine reads this face from the fused spelling.",
         "And the wāw of rubba? A wāw at the head of a verse that puts an indefinite in jarr with nothing before it — وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ — is رُبَّ in disguise; the WawEngine's rubba face fires on exactly that signal: an opening wāw followed by a majrūr indefinite."],
  "tr": ["Lâm ne yapar? Ta'lilin yanında dört şey: tahsis eder (الْمَالُ لِزَيْدٍ — mal Zeyd'indir), sebebi verir (ضَرَبْتُ لِلتَّأْدِيبِ), kavl fiiliyle «hakkında» demektir (قُلْتُ لِزَيْدٍ = عَنْهُ), zâid olabilir (رَدِفَ لَكُمْ = رَدِفَكُمْ) ve taaccüb kaseminde vâvın işini görür (لِلَّهِ لَا يُؤَخَّرُ الْأَجَلُ).",
         "رُبَّ nedir? Cümlesini açması gereken ve yalnız vasıf taşıyan bir nekreyi yönetebilen taklil harfi — «ne az…». «Az» için konulmuş, «çok» için kullanılır olmuştur; mütercimlerin «nadiren» ile «sık sık» arasında gidip gelmesi bundandır.",
         "رُبَّ neye asılır? Birgivî hiçbir şeye der — yöneten ve orada duran bir harftir. Çoğunluk mahzûf bir mâzî fiile der: رُبَّ رَجُلٍ كَرِيمٍ ancak رُبَّ رَجُلٍ كَرِيمٍ لَقِيتُهُ olarak tamdır. TaalluqEngine çoğunluğu izler ve fiili takdir eder.",
         "رُبَّهُ رَجُلًا nedir? Mansûb bir nekrenin açıkladığı mübhem bir zamir üzerinde rubbe. Mektepler zamirde ayrılır: Basralılar ardından ne gelirse gelsin هُ tutar (رُبَّهُ رِجَالًا، رُبَّهُ امْرَأَةً); Kûfeliler uydurur (رُبَّهُمْ رِجَالًا، رُبَّهَا امْرَأَةً). İki tablo da saklanır.",
         "رُبَمَا'da ne olur? مَا kâffedir: رُبَّ'nin amelini durdurur ve bütün bir cümle üzerine girmesine izin verir — رُبَمَا يَوَدُّ الَّذِينَ كَفَرُوا. MaEngine bu yüzü bitişik yazımdan okur.",
         "Ya rubbe vâvı? Beytin başında, önünde hiçbir şey olmadan bir nekreyi cer eden vâv — وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ — kılık değiştirmiş رُبَّ'dir; WawEngine'in rubbe yüzü tam bu işaretle ateşlenir: açılış vâvı ve ardından mecrûr bir nekre."]},
 "plain": {
  "en": "The lām says «belongs to», «in order to», and with «said» it means «about»; sometimes it adds nothing, and in an oath it can stand for «by». Rubba means «many a…» or «how few a…» and must open the sentence; add mā to it and it governs nothing. A verse may drop rubba and keep only a wāw that does its work.",
  "tr": "Lâm «-indir», «için» der, «dedi» ile «hakkında» demektir; bazen hiçbir şey katmaz, kasemde «yemin olsun» yerine geçer. Rubbe «nice…» ya da «ne az…» demektir ve cümleyi açmalıdır; ona mâ ekle, hiçbir şeyi yönetmez. Bir beyit rubbe'yi düşürüp yalnız onun işini gören vâvı tutabilir."},
 "explanation": {
  "en": "The lām's list is the notebook's: the Kafiya's two senses, appropriation and cause, then three the gloss adds — «about» after a verb of saying, redundancy in the aya رَدِفَ لَكُمْ (where the object is majrūr in letter and manṣūb in place, the same double iʿrāb as the redundant bāʾ of the previous chapter), and the lām of the oath of wonder, which the notebook equates with the wāw. رُبَّ is given with its four fixed facts — paucity, head position, a described indefinite, the later shift to abundance — and then three disputes, each with its holders named: whether it hangs on anything (al-Birgivī against the majority and the dropped لَقِيتُهُ), what pronoun it takes in رُبَّهُ رَجُلًا (the Basrans' invariable هُ against the Kufans' agreement, both paradigms spelled out), and the مَا that disarms it. The wāw of rubba closes the chapter with the famous verse of the empty town, parsed so that the wāw itself governs the jarr. The chapter is the third of the jarr-letter series, and the oath letters, whose answer it has already touched, follow in the next.",
  "tr": "Lâm'ın listesi defterindir: Kâfiye'nin iki mânâsı, ihtisas ve ta'lil; sonra şerhin eklediği üç — kavl fiilinden sonra «hakkında», رَدِفَ لَكُمْ âyetinde zâidlik (mef'ûl lafzen mecrûr, mahallen mansûb; önceki bâbın zâid bâ'sıyla aynı çifte i'rab) ve defterin vâvla bir tuttuğu taaccüb kasemi lâmı. رُبَّ dört sabit olgusuyla verilir — taklil, sadr-ı kelâm, mevsûf nekre, sonradan teksire kayış — ardından her biri sahipleriyle üç ihtilâf: bir şeye asılıp asılmadığı (Birgivî çoğunluğa ve mahzûf لَقِيتُهُ'ye karşı), رُبَّهُ رَجُلًا'da hangi zamiri aldığı (Basralıların değişmez هُ'si Kûfelilerin mutâbakatına karşı, iki tablo da yazılır) ve onu silahsızlandıran مَا. Rubbe vâvı bâbı boş belde beytiyle kapar; beyit vâvın kendisi ceri yönetecek şekilde çözümlenir. Bâb cer harfleri dizisinin üçüncüsüdür; cevabına zaten dokunduğu kasem harfleri sonrakinde gelir."},
 "examples": [
  {"ar": "الْمَالُ لِزَيْدٍ — ضَرَبْتُ لِلتَّأْدِيبِ — قُلْتُ لِزَيْدٍ", "en": "The lām's three senses.", "tr": "Lâm'ın üç mânâsı.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "رَدِفَ لَكُمْ — لِلَّهِ لَا يُؤَخَّرُ الْأَجَلُ", "en": "Redundant, and in the oath of wonder.", "tr": "Zâid ve taaccüb kaseminde.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "رُبَّ رَجُلٍ كَرِيمٍ — أَيْ لَقِيتُهُ", "en": "Rubba and its dropped governor.", "tr": "Rubbe ve mahzûf müteallakı.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "رُبَّهُ رَجُلًا — رُبَّهُمْ رِجَالًا", "en": "The vague pronoun: Basra and Kufa.", "tr": "Mübhem zamir: Basra ve Kûfe.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "رُبَمَا يَوَدُّ الَّذِينَ كَفَرُوا لَوْ كَانُوا مُسْلِمِينَ", "en": "Rubba disarmed by mā.", "tr": "Mâ ile silahsızlanan rubbe.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ", "en": "The wāw of rubba.", "tr": "Rubbe vâvı.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«لَقِيتُ رُبَّ رَجُلٍ»",
   "right": "«رُبَّ رَجُلٍ كَرِيمٍ لَقِيتُهُ — rubbe'nin sadr-ı kelâm hakkı vardır»",
   "why": {"en": "Rubba must open its clause; nothing may precede it.", "tr": "Rubbe cümlesini açmalıdır; önüne hiçbir şey geçemez."}},
  {"wrong": "«رُبَّ الرَّجُلِ»",
   "right": "«رُبَّ رَجُلٍ كَرِيمٍ — rubbe mevsûf bir nekreye mahsustur»",
   "why": {"en": "On the soundest view rubba takes no definite noun.", "tr": "En sahih görüşe göre rubbe marife almaz."}},
  {"wrong": "«رُبَمَا رَجُلٍ»",
   "right": "«رُبَمَا يَوَدُّ… — mâ-i kâffe rubbe'yi amelden alıkoyar, cümle üzerine girer»",
   "why": {"en": "Once mā attaches, rubba governs nothing and takes a sentence.", "tr": "Mâ bitişince rubbe hiçbir şeyi yönetmez ve cümle alır."}},
  {"wrong": "«قُلْتُ لِزَيْدٍ — Zeyd'e dedim (her zaman)»",
   "right": "«kavl ile lâm عَنْ mânâsına da gelir: Zeyd hakkında konuştum»",
   "why": {"en": "The notebook records the «about» sense of the lām after the verb of saying.", "tr": "Defter kavl fiilinden sonra lâm'ın «hakkında» mânâsını kaydeder."}}],
 "relatedNotes": ["ila-hatta-fi-wal-ba-fil-kafiya", "huruf-jarr", "lam-taleel", "anwa-ma", "anwa-al-waw", "tamyiz"]}

ADD_EN = (" Chapter 31 (notebook lines ~333-334): the lām's senses (27:72), rubba's rules and disputes (al-Birgivī; Basra and Kufa on رُبَّهُ), the kāffa mā (15:2) and the wāw of rubba (the verse وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ) — the notebook's exposition, kept as commentary (s1-s7). Qurʾānic text as the source prints it.")
ADD_TR = (" Otuz birinci bâb (defter satırları ~333-334): lâm'ın mânâları (27:72), rubbe'nin kuralları ve ihtilâfları (Birgivî; رُبَّهُ'da Basra ve Kûfe), mâ-i kâffe (15:2) ve rubbe vâvı (وَبَلْدَةٍ لَيْسَ بِهَا أَنِيسٌ beyti) — defterin açıklaması, şerh olarak (s1-s7). Kur'ân metni kaynağın bastığı gibi.")
write_out(31, S, TITLE, ADD_EN, ADD_TR, "333-334", GLOSS_ADD, notes=(NOTE,),
          related=(("ila-hatta-fi-wal-ba-fil-kafiya", [K]), ("anwa-al-waw", [K])))
report(31, S, GLOSS_ADD, (NOTE,))
