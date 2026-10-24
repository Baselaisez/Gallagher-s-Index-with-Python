# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 45: THE NŪN OF EMPHASIS — light (quiescent) and heavy (fatḥa, kasra after the dual alif and the feminine plural);
rarely on a negation (مَا يَقُومَنَّ زَيْدٌ), obligatory in the affirmative answer of an oath (لَأَفْعَلَنَّ), frequent in the condition
strengthened by مَا (إِمَّا تَفْعَلَنَّ); the vowel before it (ḍamma with the plural wāw, kasra with the addressed woman's yāʾ, fatḥa
elsewhere); the light nūn barred from the dual and the feminine plural (two quiescents) except by Yūnus; with an apparent pronoun the
nūn behaves as a separate word (the wāw/yāʾ dropped unless a fatḥa precedes, else vowelled), without one as part of the word —
hence تَرَيَنَّ، تَرَوُنَّ، تَرَيِنَّ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~353-356 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch45.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "nun-al-tawkid-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "نُونُ التَّأْكِيدِ", "en": "The nūn of emphasis — heavy and light, the vowel before it, and how it meets the pronouns", "tr": "Te'kid nûnu — şeddeli ve hafif, öncesindeki hareke ve zamirlerle buluşması"}
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
NT = "nun-tawkid"
def DRB(full, stem, nun, ar, en, tr, punct=None, nun_lex="nun-tawkid-seg"):
    return cited(full, "daraba", "verb", [NT, K], ar, en, tr, punct=punct, segments=[seg(stem, "daraba", "verb"), seg(nun, nun_lex, "part")])
def NUNT(full="نُونُ", tags=("mubtada-khabar", "idafa-definiteness"), ar="مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", en="«the nūn of».", tr="«... nûnu»."):
    return [W(full, "nun-letter", "noun", list(tags) + [NT], ar, en, tr), W("التَّأْكِيدِ", "takid", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«emphasis».", "«te'kid».")]
def ALIF_TATHNIYA(tags=("idafa-definiteness",), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ."):
    return [W("أَلِفِ", "alif-letter", "noun", list(tags), ar, "«the alif of».", "«elifi»."), W("التَّثْنِيَةِ", "tathniya", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dual».", "«tesniye»."), atf_wa("وَجَمْعِ", "jam", "noun", [AT, "idafa-definiteness"], "جَمْعِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the plural of».", "«ve ... cemi».", "جَمْعِ"), W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müennes».")]
def TATHNIYA_JAM(first_tags, first_ar, punct=None):
    return [W("التَّثْنِيَةِ", "tathniya", "noun", list(first_tags) + ["al-muthanna"], first_ar, "«the dual».", "«tesniye»."), atf_wa("وَجَمْعِ", "jam", "noun", [AT, "idafa-definiteness"], "جَمْعِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the plural of».", "«ve ... cemi».", "جَمْعِ"), W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müennes».", punct=punct)]

S.append({"id": "s1", "translation": {
 "en": "The nūn of emphasis is of two kinds, light and heavy. The light one is quiescent; the heavy one takes a fatḥa except with the alif of the dual and the feminine plural — as اِضْرِبَنَّ، اِضْرِبُنَّ، اِضْرِبِنَّ — and a kasra with the alif of the dual and the feminine plural, as اِضْرِبَانِّ، اِضْرِبْنَانِّ." + C_EN,
 "tr": "Te'kid nûnu, hafif ve şeddeli olmak üzere iki kısımdır. Hafif nûn sâkindir; şeddeli nûn tesniye elifi ve cemi müennes dışında fethalıdır — اِضْرِبَنَّ، اِضْرِبُنَّ، اِضْرِبِنَّ gibi — tesniye elifi ve cemi müennesle kesrelidir — اِضْرِبَانِّ، اِضْرِبْنَانِّ gibi." + C_TR},
 "tokens": [
  *NUNT(),
  W("قِسْمَانِ", "qism", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«is of two kinds».", "«iki kısımdır».", punct=":"),
  W("مُخَفَّفَةٌ", "mukhaffafa", "noun", ["badal", "ism-maful", "form-ii-verbs"], "بَدَلٌ مَرْفُوعٌ.", "«light».", "«hafif»."),
  atf_wa("وَمُشَدَّدَةٌ", "mushaddada", "noun", [AT, "ism-maful", "form-ii-verbs"], "مُشَدَّدَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and heavy».", "«ve şeddeli».", "مُشَدَّدَةٌ", punct="."),
  W("فَالْمُخَفَّفَةُ", "mukhaffafa", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمُخَفَّفَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the light one».", "«hafif nûn».", segments=[seg("فَ", "fa", "conj"), seg("الْمُخَفَّفَةُ", "mukhaffafa", "noun")]),
  W("سَاكِنَةٌ", "sakin", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«is quiescent».", "«sâkindir».", punct="،"),
  atf_wa("وَالْمُشَدَّدَةُ", "mushaddada", "noun", ["mubtada-khabar"], "الْمُشَدَّدَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the heavy one».", "«şeddeli nûn».", "الْمُشَدَّدَةُ"),
  W("مَفْتُوحَةٌ", "maftuh", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«takes a fatḥa».", "«fethalıdır»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("غَيْرِ", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«other than».", "«dışında»."),
  *ALIF_TATHNIYA(),
  nahwu(),
  DRB("اِضْرِبَنَّ", "اِضْرِبَ", "نَّ", "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«strike! (emphatic)».", "«mutlaka vur!».", punct="،"),
  DRB("اِضْرِبُنَّ", "اِضْرِبُ", "نَّ", "فِعْلُ أَمْرٍ لِلْجَمَاعَةِ، حُذِفَتْ وَاوُ الْجَمْعِ لِالْتِقَاءِ السَّاكِنَيْنِ وَبَقِيَتِ الضَّمَّةُ دَلِيلًا عَلَيْهَا.", "«strike! (you men)».", "«mutlaka vurun!».", punct="،"),
  DRB("اِضْرِبِنَّ", "اِضْرِبِ", "نَّ", "فِعْلُ أَمْرٍ لِلْمُخَاطَبَةِ، حُذِفَتْ يَاءُ الْمُخَاطَبَةِ وَبَقِيَتِ الْكَسْرَةُ دَلِيلًا عَلَيْهَا.", "«strike! (you woman)».", "«mutlaka vur! (kadın)».", punct="،"),
  atf_wa("وَمَكْسُورَةٌ", "maksur", "noun", [AT, "ism-maful"], "مَكْسُورَةٌ مَعْطُوفٌ عَلَى مَفْتُوحَةٌ.", "«and takes a kasra».", "«ve kesrelidir».", "مَكْسُورَةٌ"),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  *ALIF_TATHNIYA(),
  nahwu(),
  DRB("اِضْرِبَانِّ", "اِضْرِبَا", "نِّ", "فِعْلُ أَمْرٍ لِلْمُثَنَّى، وَالْأَلِفُ فَاعِلٌ، وَالنُّونُ الثَّقِيلَةُ مَكْسُورَةٌ بَعْدَ الْأَلِفِ.", "«strike! (you two)».", "«mutlaka vurun! (ikiniz)».", punct="،"),
  DRB("اِضْرِبْنَانِّ", "اِضْرِبْنَا", "نِّ", "فِعْلُ أَمْرٍ لِلنِّسْوَةِ، وَنُونُ النِّسْوَةِ فَاعِلٌ، وَزِيدَتْ أَلِفٌ فَاصِلَةٌ بَيْنَ النُّونَيْنِ، وَالثَّقِيلَةُ مَكْسُورَةٌ.", "«strike! (you women)».", "«mutlaka vurun! (kadınlar)».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And the nūn of emphasis rarely enters on a negation though it carries no sense of request — as مَا يَقُومَنَّ زَيْدٌ; it is obligatory in the affirmative answer of an oath — as وَاللهِ لَأَفْعَلَنَّ الْفَرَائِضَ; and it is frequent in the condition strengthened with مَا — as إِمَّا تَفْعَلَنَّ." + C_EN,
 "tr": "Te'kid nûnu, talep mânâsı olmadığı hâlde nefyin üzerine az olarak da girer — مَا يَقُومَنَّ زَيْدٌ gibi; kasemin müsbet cevabında lâzımdır — وَاللهِ لَأَفْعَلَنَّ الْفَرَائِضَ gibi; مَا ile te'kid edilmiş şartta çoktur — إِمَّا تَفْعَلَنَّ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتَدْخُلُ", "dakhala", "verb", ["fail"], "تَدْخُلُ فِعْلٌ مُضَارِعٌ.", "«and enters».", "«ve girer».", "تَدْخُلُ"),
  *NUNT(tags=("fail", "idafa-definiteness"), ar="فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ."),
  W("قَلِيلًا", "qalil", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«rarely».", "«az olarak»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("النَّفْيِ", "nafy", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a negation».", "«nefyin»."),
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "الْوَاوُ حَالِيَّةٌ، وَإِنْ وَصْلِيَّةٌ.", "«though».", "«... -sa da».", "إِنْ"),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَكُنْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ.", "«there is».", "«olmasa da»."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr", "kana-wa-akhawatuha", "taqdim-al-musnad"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرُ يَكُنْ مُقَدَّمٌ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("مَعْنَى", "mana", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "اسْمُ يَكُنْ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«a sense of».", "«mânâsı»."),
  W("الطَّلَبِ", "talab", "noun", ["idafa-definiteness", "insha-wa-tamanni"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«request».", "«talep».", punct="،"),
  nahwu(),
  cited("مَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  cited("يَقُومَنَّ", "qama", "verb", [NT, "fail", "hollow-verbs", K], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ — عَلَى قِلَّةٍ بَعْدَ النَّفْيِ.", "«does stand (emphatic)».", "«asla kalk-».", segments=[seg("يَقُومَ", "qama", "verb"), seg("نَّ", "nun-tawkid-seg", "part")]),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="؛"),
  atf_wa("وَتَلْزَمُ", "lazima", "verb", ["fail"], "تَلْزَمُ فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and is obligatory».", "«ve lâzımdır».", "تَلْزَمُ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("جَوَابِ", "jawab", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the answer of».", "«cevabında»."),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness", "huruf-al-qasam-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«an oath».", "«kasemin»."),
  W("الْمُثْبَتِ", "muthbat", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«affirmative».", "«müsbet».", punct="،"),
  nahwu(),
  cited("وَاللهِ", "allah", "propn", ["huruf-al-qasam-fil-kafiya", "huruf-jarr"], "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by Allah».", "«vallahi».", segments=[seg("وَ", "waw-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  cited("لَأَفْعَلَنَّ", "faala", "verb", [NT, "huruf-al-qasam-fil-kafiya", "fail", K], "اللَّامُ لِجَوَابِ الْقَسَمِ، وَأَفْعَلَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I will surely do».", "«mutlaka yapacağım».", segments=[seg("لَ", "lam-qasam", "part"), seg("أَفْعَلَ", "faala", "verb"), seg("نَّ", "nun-tawkid-seg", "part")]),
  cited("الْفَرَائِضَ", "farida", "noun", ["maful-bihi", "jam-taksir", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«the obligatory duties».", "«farzları».", punct="؛"),
  atf_wa("وَتَكْثُرُ", "kathura", "verb", ["fail"], "تَكْثُرُ فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and is frequent».", "«ve çoktur».", "تَكْثُرُ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-ta»."),
  W("الشَّرْطِ", "shart", "noun", ["huruf-jarr", "al-majzum-wal-shart-wal-jaza"], "مَجْرُورٌ.", "«the condition».", "«şartta»."),
  W("الْمُؤَكَّدِ", "muakkad", "noun", ["naat-sifa", "ism-maful", "form-ii-verbs"], "صِفَةٌ مَجْرُورَةٌ.", "«strengthened».", "«te'kid edilmiş»."),
  bi_("بِمَا", "ma-zaida", "part", ["majaz-ziyada-nuqsan", "anwa-ma"], "مَا فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ: الزَّائِدَةُ.", "«with mā».", "«mâ ile».", "مَا", punct="،"),
  nahwu(),
  cited("إِمَّا", "in-shartiyya", "part", ["in-shartiyya", "majaz-ziyada-nuqsan", K], "إِنْ الشَّرْطِيَّةُ وَمَا الزَّائِدَةُ، أُدْغِمَتِ النُّونُ فِي الْمِيمِ.", "«if ever».", "«eğer bir»."),
  cited("تَفْعَلَنَّ", "faala", "verb", [NT, "in-shartiyya", "fail", K], "فِعْلُ الشَّرْطِ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ فِي مَحَلِّ جَزْمٍ.", "«you do».", "«yaparsan».", punct=".", segments=[seg("تَفْعَلَ", "faala", "verb"), seg("نَّ", "nun-tawkid-seg", "part")]),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And what precedes the heavy and the light nūn takes a ḍamma with the wāw of the masculine plural — as اِضْرِبُنْ، اِضْرِبُنَّ — a kasra with the yāʾ of the addressed woman — as اِضْرِبِنْ، اِضْرِبِنَّ — and a fatḥa in the rest — as اِضْرِبَنْ، اِضْرِبَنَّ." + C_EN,
 "tr": "Şeddeli ve hafif nûnun öncesi cemi müzekker vâvıyla mazmumdur — اِضْرِبُنْ، اِضْرِبُنَّ gibi; müfred müennes muhataba yâ'sıyla meksurdur — اِضْرِبِنْ، اِضْرِبِنَّ gibi; diğerlerinde meftuhtur — اِضْرِبَنْ، اِضْرِبَنَّ gibi." + C_TR},
 "tokens": [
  atf_wa("وَمَا", "ma-mawsula", "pron", ["mubtada-khabar", "ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«and what».", "«ve ... olan».", "مَا"),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةٌ.", "«precedes».", "«öncesi»."),
  W("النُّونِ", "nun-letter", "noun", ["idafa-definiteness", NT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the nūn».", "«nûnun»."),
  W("الْمُشَدَّدَةِ", "mushaddada", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«heavy».", "«şeddeli»."),
  atf_wa("وَالْمُخَفَّفَةِ", "mukhaffafa", "noun", [AT], "الْمُخَفَّفَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and light».", "«ve hafif».", "الْمُخَفَّفَةِ"),
  W("مَضْمُومٌ", "madmum", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«takes a ḍamma».", "«mazmumdur»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("وَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the wāw of».", "«vâvıyla»."),
  W("جَمْعِ", "jam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cemi»."),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine».", "«müzekker».", punct="،"),
  nahwu(),
  DRB("اِضْرِبُنْ", "اِضْرِبُ", "نْ", "فِعْلُ أَمْرٍ لِلْجَمَاعَةِ مَعَ النُّونِ الْخَفِيفَةِ — ضُمَّ مَا قَبْلَهَا.", "«strike! (you men)».", "«vurun!».", punct="،", nun_lex="nun-tawkid-khafifa"),
  DRB("اِضْرِبُنَّ", "اِضْرِبُ", "نَّ", "فِعْلُ أَمْرٍ لِلْجَمَاعَةِ مَعَ النُّونِ الثَّقِيلَةِ.", "«strike! (you men)».", "«mutlaka vurun!».", punct="؛"),
  atf_wa("وَمَكْسُورٌ", "maksur", "noun", [AT, "ism-maful"], "مَكْسُورٌ مَعْطُوفٌ عَلَى مَضْمُومٌ.", "«and takes a kasra».", "«ve meksurdur».", "مَكْسُورٌ"),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("يَاءِ", "ya-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the yāʾ of».", "«yâ'sıyla»."),
  W("الْمُفْرَدَةِ", "mufrad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the single».", "«müfred»."),
  W("الْمُخَاطَبَةِ", "mukhataba-fem", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«addressed woman».", "«muhataba».", punct="،"),
  nahwu(),
  DRB("اِضْرِبِنْ", "اِضْرِبِ", "نْ", "فِعْلُ أَمْرٍ لِلْمُخَاطَبَةِ مَعَ النُّونِ الْخَفِيفَةِ — كُسِرَ مَا قَبْلَهَا.", "«strike! (you woman)».", "«vur! (kadın)».", punct="،", nun_lex="nun-tawkid-khafifa"),
  DRB("اِضْرِبِنَّ", "اِضْرِبِ", "نَّ", "فِعْلُ أَمْرٍ لِلْمُخَاطَبَةِ مَعَ النُّونِ الثَّقِيلَةِ.", "«strike! (you woman)».", "«mutlaka vur! (kadın)».", punct="؛"),
  atf_wa("وَمَفْتُوحٌ", "maftuh", "noun", [AT, "ism-maful"], "مَفْتُوحٌ مَعْطُوفٌ.", "«and takes a fatḥa».", "«ve meftuhtur».", "مَفْتُوحٌ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("غَيْرِهِمَا", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«the rest».", "«diğerlerinde».", punct="،", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3d()]),
  nahwu(),
  DRB("اِضْرِبَنْ", "اِضْرِبَ", "نْ", "فِعْلُ أَمْرٍ لِلْوَاحِدِ مَعَ النُّونِ الْخَفِيفَةِ — فُتِحَ مَا قَبْلَهَا.", "«strike!».", "«vur!».", punct="،", nun_lex="nun-tawkid-khafifa"),
  DRB("اِضْرِبَنَّ", "اِضْرِبَ", "نَّ", "فِعْلُ أَمْرٍ لِلْوَاحِدِ مَعَ النُّونِ الثَّقِيلَةِ.", "«strike! (emphatic)».", "«mutlaka vur!».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the light nūn does not enter on the dual or the feminine plural, because a meeting of two quiescents would follow; so one does not say اِضْرِبَانْ nor اِضْرِبْنَانْ — except according to Yūnus." + C_EN,
 "tr": "Hafif nûn, iki sâkinin bir araya gelmesi lâzım geleceğinden tesniyeye ve cemi müennese girmez; اِضْرِبَانْ ve اِضْرِبْنَانْ denmez — ancak Yûnus'a göre girer." + C_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... -mez».", "لَا"),
  W("تَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ.", "«does enter».", "«girmez»."),
  W("الْمُخَفَّفَةُ", "mukhaffafa", "noun", ["fail", NT], "فَاعِلٌ مَرْفُوعٌ.", "«the light one».", "«hafif nûn»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  *TATHNIYA_JAM(("huruf-jarr",), "مَجْرُورٌ."),
  li_("لِلُزُومِ", "luzum", "noun", ["idafa-definiteness", "lam-taleel"], "لُزُومِ مَجْرُورٌ، وَهُوَ مُضَافٌ — اللَّامُ لِلتَّعْلِيلِ.", "«because would follow».", "«... lâzım geleceğinden».", "لُزُومِ"),
  W("اجْتِمَاعِ", "ijtimaa", "noun", ["idafa-definiteness", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«a meeting of».", "«bir araya gelmesi»."),
  W("السَّاكِنَيْنِ", "sakin", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two quiescents».", "«iki sâkinin».", punct="،"),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«bu yüzden ... -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is said».", "«denmez».", punct=":"),
  DRB("اِضْرِبَانْ", "اِضْرِبَا", "نْ", "مَرْفُوضٌ — تَلْتَقِي الْأَلِفُ السَّاكِنَةُ وَالنُّونُ السَّاكِنَةُ.", "«(not said)».", "«(denmez)».", nun_lex="nun-tawkid-khafifa"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya", AT], "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ مَعَ الْعَطْفِ.", "«nor».", "«ne de».", "لَا"),
  DRB("اِضْرِبْنَانْ", "اِضْرِبْنَا", "نْ", "مَرْفُوضٌ — لِالْتِقَاءِ السَّاكِنَيْنِ.", "«(not said)».", "«(denmez)».", punct="—", nun_lex="nun-tawkid-khafifa"),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«ancak»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "istithna"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — الْمُسْتَثْنَى.", "«according to».", "«... -a göre»."),
  W("يُونُسَ", "yunus", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — غَيْرُ مُنْصَرِفٍ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.", "«Yūnus».", "«Yûnus'a».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And the heavy and the light nūn, outside the dual and the feminine plural, with an apparent pronoun — the yāʾ of the addressed woman or the wāw of the plural — are like a separate word: the wāw and the yāʾ are dropped if what precedes them is not on a fatḥa, and the wāw is vowelled with a ḍamma and the yāʾ with a kasra if it is." + C_EN,
 "tr": "Şeddeli ve hafif nûn, tesniye ve cemi müennes dışında, bâriz zamirle — muhataba yâ'sı ve cemi vâvıyla — beraber munfasıl kelime gibidir: vâv ve yâ'nın öncesi meftuh değilse hazfedilir, meftuh ise vâv damme ile, yâ kesre ile harekelenir." + C_TR},
 "tokens": [
  atf_wa("وَالنُّونُ", "nun-letter", "noun", ["mubtada-khabar", NT], "النُّونُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the nūn».", "«ve nûn».", "النُّونُ"),
  W("الْمُشَدَّدَةُ", "mushaddada", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«heavy».", "«şeddeli»."),
  atf_wa("وَالْمُخَفَّفَةُ", "mukhaffafa", "noun", [AT], "الْمُخَفَّفَةُ مَعْطُوفٌ.", "«and light».", "«ve hafif».", "الْمُخَفَّفَةُ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«outside».", "«... dışında»."),
  W("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«(other than)».", "«(gayrı)»."),
  *TATHNIYA_JAM(("idafa-definiteness",), "مُضَافٌ إِلَيْهِ مَجْرُورٌ."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile beraber»."),
  W("الضَّمِيرِ", "damir", "noun", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the pronoun».", "«zamirle»."),
  W("الْبَارِزِ", "bariz", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«apparent».", "«bâriz».", punct="—"),
  W("يَاءِ", "ya-letter", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ مِنَ الضَّمِيرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the yāʾ of».", "«yâ'sı»."),
  W("الْمُخَاطَبَةِ", "mukhataba-fem", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the addressed woman».", "«muhataba»."),
  atf_wa("وَوَاوِ", "waw-letter", "noun", [AT, "idafa-definiteness"], "وَاوِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the wāw of».", "«ve vâvı».", "وَاوِ"),
  W("الْجَمْعِ", "jam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the plural».", "«cemi».", punct="—"),
  ka_("كَالْكَلِمَةِ", "kalima", "noun", ["mubtada-khabar"], "الْكَلِمَةِ مَجْرُورٌ — خَبَرُ النُّونُ.", "«are like a word».", "«kelime gibidir».", "الْكَلِمَةِ", segs=[seg("كَ", "ka", "prep"), seg("الْكَلِمَةِ", "kalima", "noun")]),
  W("الْمُنْفَصِلَةِ", "munfasil", "noun", ["naat-sifa", "ism-fail", "form-vii-verbs"], "صِفَةٌ مَجْرُورَةٌ.", "«separate».", "«munfasıl».", punct=":"),
  W("فَتُحْذَفُ", "hadhafa", "verb", ["naib-al-fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتُحْذَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«so are dropped».", "«hazfedilir».", segments=[seg("فَ", "fa", "conj"), seg("تُحْذَفُ", "hadhafa", "verb")]),
  W("الْوَاوُ", "waw-letter", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the wāw».", "«vâv»."),
  atf_wa("وَالْيَاءُ", "ya-letter", "noun", [AT], "الْيَاءُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the yāʾ».", "«ve yâ».", "الْيَاءُ"),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-se»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«değil-»."),
  W("يَكُنْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ.", "«is».", "«-se»."),
  W("مَا", "ma-mawsula", "pron", ["kana-wa-akhawatuha", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُنْ.", "«what».", "«... olan»."),
  W("قَبْلَهُمَا", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُمَا مُضَافٌ إِلَيْهِ — صِلَةٌ.", "«precedes them».", "«öncesi».", segments=[seg("قَبْلَ", "qabla", "noun"), pr3d()]),
  W("مَفْتُوحًا", "maftuh", "noun", ["kana-wa-akhawatuha", "ism-maful"], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«on a fatḥa».", "«meftuh».", punct="،"),
  atf_wa("وَتُحَرَّكُ", "harraka", "verb", ["naib-al-fail", "form-ii-verbs"], "تُحَرَّكُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is vowelled».", "«ve harekelenir».", "تُحَرَّكُ"),
  W("الْوَاوُ", "waw-letter", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the wāw».", "«vâv»."),
  bi_("بِالضَّمَّةِ", "damma", "noun", [], "الضَّمَّةِ مَجْرُورٌ.", "«with a ḍamma».", "«damme ile».", "الضَّمَّةِ", segs=[seg("بِ", "bi", "prep"), seg("الضَّمَّةِ", "damma", "noun")]),
  atf_wa("وَالْيَاءُ", "ya-letter", "noun", [AT], "الْيَاءُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the yāʾ».", "«yâ».", "الْيَاءُ"),
  bi_("بِالْكَسْرَةِ", "kasra", "noun", [], "الْكَسْرَةِ مَجْرُورٌ.", "«with a kasra».", "«kesre ile».", "الْكَسْرَةِ", segs=[seg("بِ", "bi", "prep"), seg("الْكَسْرَةِ", "kasra", "noun")]),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«-se»."),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is».", "«ise»."),
  W("مَفْتُوحًا", "maftuh", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«on a fatḥa».", "«meftuh».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And if it is not with an apparent pronoun, it is like an attached word, and what precedes it is vowelled with a fatḥa, as with the alif of the dual." + C_EN,
 "tr": "Bâriz zamirle beraber olmazsa muttasıl kelime gibidir; tesniye elifiyle olduğu gibi öncesi fetha ile harekelenir." + C_TR},
 "tokens": [
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "إِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve ... -sa».", "إِنْ"),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("تَكُنْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«it is».", "«olmazsa»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفٌ مَنْصُوبٌ — خَبَرُ تَكُنْ، وَهُوَ مُضَافٌ.", "«with».", "«... ile beraber»."),
  W("ضَمِيرٍ", "damir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a pronoun».", "«zamir»."),
  W("بَارِزٍ", "bariz", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«apparent».", "«bâriz»."),
  W("فَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَهِيَ مُبْتَدَأٌ.", "«it is».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هِيَ", "hiya", "pron")]),
  ka_("كَالْكَلِمَةِ", "kalima", "noun", ["mubtada-khabar"], "الْكَلِمَةِ مَجْرُورٌ — خَبَرٌ.", "«like a word».", "«kelime gibidir».", "الْكَلِمَةِ", segs=[seg("كَ", "ka", "prep"), seg("الْكَلِمَةِ", "kalima", "noun")]),
  W("الْمُتَّصِلَةِ", "muttasil", "noun", ["naat-sifa", "ism-fail", "form-viii-verbs"], "صِفَةٌ مَجْرُورَةٌ.", "«attached».", "«muttasıl».", punct="،"),
  W("فَيُحَرَّكُ", "harraka", "verb", ["naib-al-fail", "form-ii-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيُحَرَّكُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is vowelled».", "«harekelenir».", segments=[seg("فَ", "fa", "conj"), seg("يُحَرَّكُ", "harraka", "verb")]),
  W("مَا", "ma-mawsula", "pron", ["naib-al-fail", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«what».", "«... olan»."),
  W("قَبْلَهَا", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةٌ.", "«precedes it».", "«öncesi».", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  bi_("بِالْفَتْحَةِ", "fatha", "noun", [], "الْفَتْحَةِ مَجْرُورٌ.", "«with a fatḥa».", "«fetha ile».", "الْفَتْحَةِ", segs=[seg("بِ", "bi", "prep"), seg("الْفَتْحَةِ", "fatha", "noun")]),
  ka_("كَمَا", "ma-masdariyya", "part", ["anwa-ma"], "مَا مَصْدَرِيَّةٌ.", "«as».", "«... olduğu gibi».", "مَا", segs=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  W("أَلِفِ", "alif-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the alif of».", "«elifi»."),
  W("التَّثْنِيَةِ", "tathniya", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the dual».", "«tesniye».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "For this reason one says for هَلْ تَرَى: هَلْ تَرَيَنَّ; for هَلْ تَرَوْنَ: هَلْ تَرَوُنَّ; and for هَلْ تَرَيْنَ: هَلْ تَرَيِنَّ." + C_EN,
 "tr": "Bu sebeple هَلْ تَرَى için هَلْ تَرَيَنَّ, هَلْ تَرَوْنَ için هَلْ تَرَوُنَّ, هَلْ تَرَيْنَ için هَلْ تَرَيِنَّ denir." + C_TR},
 "tokens": [
  W("فَلِذَلِكَ", "dhalika", "pron", ["huruf-jarr", "asma-al-ishara-wal-mawsulat"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لِلتَّعْلِيلِ، وَذَلِكَ فِي مَحَلِّ جَرٍّ.", "«for this reason».", "«bu sebeple».", segments=[seg("فَ", "fa", "conj"), seg("لِ", "lam-taleel", "part"), seg("ذَلِكَ", "dhalika", "pron")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«one says».", "«denir»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«... için»."),
  cited("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do».", "«... mi»."),
  cited("تَرَى", "raa", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — لَا ضَمِيرَ بَارِزًا.", "«you see».", "«görüyorsun».", punct=":"),
  cited("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do».", "«... mi»."),
  cited("تَرَيَنَّ", "raa", "verb", [NT, "fail", "naqis-verbs", K], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ — رُدَّتِ الْأَلِفُ يَاءً وَفُتِحَتْ قَبْلَ النُّونِ كَمَا مَعَ أَلِفِ التَّثْنِيَةِ.", "«you surely see».", "«mutlaka görürsün».", punct="،", segments=[seg("تَرَيَ", "raa", "verb"), seg("نَّ", "nun-tawkid-seg", "part")]),
  atf_wa("وَفِي", "fi", "prep", [AT, "huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and for».", "«ve ... için».", "فِي"),
  cited("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do».", "«... mi»."),
  cited("تَرَوْنَ", "raa", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَا قَبْلَهَا مَفْتُوحٌ.", "«you (all) see».", "«görüyorsunuz».", punct=":"),
  cited("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do».", "«... mi»."),
  cited("تَرَوُنَّ", "raa", "verb", [NT, "fail", "naqis-verbs", K], "حُذِفَتْ نُونُ الرَّفْعِ، وَبَقِيَتْ وَاوُ الْجَمْعِ مَضْمُومَةً لِأَنَّ مَا قَبْلَهَا مَفْتُوحٌ، وَالنُّونُ الثَّقِيلَةُ بَعْدَهَا.", "«you (all) surely see».", "«mutlaka görürsünüz».", punct="،"),
  atf_wa("وَفِي", "fi", "prep", [AT, "huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and for».", "«ve ... için».", "فِي"),
  cited("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do».", "«... mi»."),
  cited("تَرَيْنَ", "raa", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ — مَا قَبْلَهَا مَفْتُوحٌ.", "«you (woman) see».", "«görüyorsun (kadın)».", punct=":"),
  cited("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do».", "«... mi»."),
  cited("تَرَيِنَّ", "raa", "verb", [NT, "fail", "naqis-verbs", K], "حُذِفَتْ نُونُ الرَّفْعِ، وَبَقِيَتْ يَاءُ الْمُخَاطَبَةِ مَكْسُورَةً لِأَنَّ مَا قَبْلَهَا مَفْتُوحٌ، وَالنُّونُ الثَّقِيلَةُ بَعْدَهَا.", "«you (woman) surely see».", "«mutlaka görürsün (kadın)».", punct="."),
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
 "mushaddada": need("mushaddada", "مُشَدَّدَة", "ش د د", "noun", "doubled, heavy — said of the nūn of emphasis written with a shadda", "şeddeli, ağır — şedde ile yazılan te'kid nûnu için", 4),
 "nun-tawkid-khafifa": need("nun-tawkid-khafifa", "نْ (نُونُ التَّوْكِيدِ الْخَفِيفَةُ)", "ن", "part", "the light nūn of emphasis — a quiescent nūn on the end of a verb", "hafif te'kid nûnu — fiil sonunda sâkin bir nûn", 4),
 "farida": need("farida", "فَرِيضَة", "ف ر ض", "noun", "an obligatory duty, an ordinance (pl. فَرَائِض)", "farz, farîza (ç. فَرَائِض)", 2),
 "muakkad": need("muakkad", "مُؤَكَّد", "أ ك د", "noun", "emphasised, strengthened (ism mafʿūl of أَكَّدَ)", "te'kid edilmiş, pekiştirilmiş (ekkede'nin ism-i mefʿûlü)", 4),
 "harraka": need("harraka", "حَرَّكَ", "ح ر ك", "verb", "to vowel (a letter), to give it a ḥaraka (Form II)", "(bir harfi) harekelemek (tefʿîl)", 3),
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
put_morph(mo, "harraka", _nfc(_sg.derived(_sg.B2, _sg.W2, "ُ", "حَرَّك", "حَرِّك", "حَرِّك", "تَحْرِيك", "مُحَرِّك", "مُحَرَّك", "حُرِّكَ", "يُحَرَّكُ", "حَرَّكَ الْحَرْفَ: جَعَلَ عَلَيْهِ حَرَكَةً — بَابُ التَّفْعِيلِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "نُونُ التَّأْكِيدِ فِي الْكَافِيَةِ", "en": "The nūn of emphasis in the Kafiya: the light and the heavy nūn, where each may go, the vowel before it, and the rule for the pronouns it meets", "tr": "Kâfiye'de te'kid nûnu: hafif ve şeddeli nûn, her birinin gidebildiği yer, öncesindeki hareke ve karşılaştığı zamirler kuralı"},
 "level": 5, "group": "sarf",
 "classicalSources": ["الكافية لابن الحاجب — نون التأكيد مخففة ومشددة؛ تدخل قليلا على النفي، وتلزم في جواب القسم المثبت، وتكثر في الشرط المؤكد بما؛ ما قبلها مضموم مع الواو ومكسور مع الياء ومفتوح في غيرهما؛ الخفيفة لا تدخل على التثنية وجمع المؤنث", "ضياء صونغور اوغلى — دفتر الكافية: اضربن اضربن اضربن اضربان اضربنان؛ يونس؛ كالكلمة المنفصلة والمتصلة؛ هل ترين هل ترون هل ترين"],
 "question": {
  "en": ["How many nūns of emphasis are there, and how do they sound? Two: the LIGHT one is a quiescent nūn (اِضْرِبَنْ); the HEAVY one is doubled, on a fatḥa (اِضْرِبَنَّ), and on a kasra after the dual's alif and the feminine plural (اِضْرِبَانِّ، اِضْرِبْنَانِّ). The sarf lab prints both rows for every verb.",
         "Where may the nūn go? Mainly on request — command, prohibition, question, wish. The notebook's three refinements: rarely on a plain negation (مَا يَقُومَنَّ زَيْدٌ); OBLIGATORILY in the affirmative answer of an oath (وَاللهِ لَأَفْعَلَنَّ); and frequently in a condition strengthened by مَا (إِمَّا تَفْعَلَنَّ).",
         "What vowel stands before the nūn? It copies the pronoun it replaced: ḍamma for the plural wāw (اِضْرِبُنَّ), kasra for the woman's yāʾ (اِضْرِبِنَّ), fatḥa everywhere else (اِضْرِبَنَّ). The analyzer reads the person of an emphatic verb off that vowel, since the pronoun letter itself is gone.",
         "Why can the light nūn not join a dual or a feminine plural? اِضْرِبَانْ would set a quiescent alif against a quiescent nūn — two quiescents meeting — so the heavy nūn is used there and takes a kasra. Yūnus allowed it; the Kafiya does not.",
         "What is the «separate word / attached word» rule? With an apparent pronoun (the wāw, the yāʾ) the nūn counts as a separate word, so the pronoun is dropped unless a fatḥa precedes it — then it stays, vowelled (تَرَوُنَّ، تَرَيِنَّ). With no apparent pronoun the nūn is part of the word, and the letter before it simply takes a fatḥa (تَرَيَنَّ, the alif returned to its yāʾ).",
         "Why does the sarf engine refuse to generate the emphatic rows for a weak verb from a template? Because تَرَى → تَرَيَنَّ needs the i'lāl chain run backwards (the alif is a turned yāʾ); the engine derives it from the rules rather than pasting نَّ on the surface."],
  "tr": ["Kaç te'kid nûnu vardır ve nasıl okunur? İki: HAFİF olan sâkin bir nûndur (اِضْرِبَنْ); ŞEDDELİ olan çifttir, fethalıdır (اِضْرِبَنَّ), tesniye elifi ve cemi müennesten sonra kesrelidir (اِضْرِبَانِّ، اِضْرِبْنَانِّ). Sarf atölyesi her fiil için iki satırı da basar.",
         "Nûn nereye gidebilir? Başlıca talebe — emir, nehiy, soru, temenni. Defterin üç inceliği: düz nefye nadiren (مَا يَقُومَنَّ زَيْدٌ); kasemin müsbet cevabında VÂCİP olarak (وَاللهِ لَأَفْعَلَنَّ); مَا ile pekiştirilmiş şartta çokça (إِمَّا تَفْعَلَنَّ).",
         "Nûndan önce hangi hareke durur? Yerini aldığı zamiri kopyalar: cemi vâvı için damme (اِضْرِبُنَّ), kadının yâ'sı için kesre (اِضْرِبِنَّ), başka her yerde fetha (اِضْرِبَنَّ). Analizör te'kidli fiilin şahsını o harekeden okur, çünkü zamir harfinin kendisi gitmiştir.",
         "Hafif nûn niçin tesniyeye ya da cemi müennese eklenemez? اِضْرِبَانْ sâkin elifi sâkin nûnun karşısına koyardı — iki sâkinin buluşması — bu yüzden orada şeddeli nûn kullanılır ve kesre alır. Yûnus izin verdi; Kâfiye vermez.",
         "«Munfasıl kelime / muttasıl kelime» kuralı nedir? Bâriz zamirle (vâv, yâ) nûn ayrı bir kelime sayılır; bu yüzden zamir, önünde fetha yoksa düşer — varsa harekelenerek kalır (تَرَوُنَّ، تَرَيِنَّ). Bâriz zamir yoksa nûn kelimenin parçasıdır ve öncesindeki harf yalnızca fetha alır (تَرَيَنَّ, elif yâ'sına döner).",
         "Sarf motoru illetli fiilin te'kid satırlarını niçin şablondan üretmeyi reddeder? Çünkü تَرَى → تَرَيَنَّ i'lâl zincirinin tersten yürütülmesini ister (elif, dönmüş bir yâ'dır); motor نَّ'yi yüzeye yapıştırmak yerine onu kurallardan türetir."]},
 "plain": {
  "en": "Arabic can bolt a «really!» nūn onto a verb: a light one (just n) or a heavy one (nn). It goes on commands and wishes, must go on a sworn promise, and the vowel just before it tells you who is being spoken to. When the verb already ends in a «you all» or «you, woman» letter, that letter either drops or gets a vowel.",
  "tr": "Arapça bir fiile «gerçekten!» nûnu takabilir: hafif (sadece n) ya da ağır (nn). Emir ve temennilere gelir, yeminli söze gelmek zorundadır ve hemen öncesindeki hareke kime söylendiğini anlatır. Fiil zaten «siz» ya da «sen, kadın» harfiyle bitiyorsa o harf ya düşer ya da hareke alır."},
 "explanation": {
  "en": "The Kafiya's bāb on the nūn of emphasis in the notebook's order: the two kinds and their vowels, the three places outside plain request (negation rarely, the oath's affirmative answer obligatorily, the مَا-strengthened condition frequently), the vowel before the nūn as a copy of the pronoun it displaced, the light nūn's exclusion from the dual and the feminine plural with Yūnus' dissent, and the rule that decides what happens to the wāw and the yāʾ — the nūn as a separate word when a pronoun shows, as part of the word when none does — closed by the three هَلْ تَرَى forms that the rule predicts. Every form in the chapter is a verb-paradigm cell the sarf engine can derive, and the chapter is also the specification of the emphatic rows the lab prints.",
  "tr": "Kâfiye'nin te'kid nûnu bâbı defterin sırasıyla: iki kısım ve harekeleri, düz talep dışındaki üç yer (nefye nadiren, kasemin müsbet cevabına vâcip olarak, مَا ile pekiştirilmiş şarta çokça), nûndan önceki hareke yerini aldığı zamirin kopyası olarak, hafif nûnun Yûnus'un muhalefetiyle tesniye ve cemi müennesten dışlanması ve vâv ile yâ'ya ne olacağını belirleyen kural — zamir görününce nûn ayrı kelime, görünmeyince kelimenin parçası — kuralın öngördüğü üç هَلْ تَرَى şekliyle kapanır. Bâbdaki her şekil sarf motorunun türetebildiği bir çekim hücresidir ve bâb aynı zamanda atölyenin bastığı te'kid satırlarının şartnamesidir."},
 "examples": [
  {"ar": "اِضْرِبَنَّ — اِضْرِبُنَّ — اِضْرِبِنَّ — اِضْرِبَانِّ — اِضْرِبْنَانِّ", "en": "The heavy nūn across the persons.", "tr": "Şahıslar boyunca şeddeli nûn.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "وَاللهِ لَأَفْعَلَنَّ الْفَرَائِضَ", "en": "Obligatory in the oath's affirmative answer.", "tr": "Kasemin müsbet cevabında vâcip.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "اِضْرِبُنْ — اِضْرِبِنْ — اِضْرِبَنْ", "en": "The vowel before the light nūn.", "tr": "Hafif nûndan önceki hareke.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "لَا يُقَالُ اِضْرِبَانْ وَلَا اِضْرِبْنَانْ إِلَّا عِنْدَ يُونُسَ", "en": "The light nūn barred from the dual and the feminine plural.", "tr": "Hafif nûn tesniye ve cemi müennesten menedilir.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "هَلْ تَرَيَنَّ — هَلْ تَرَوُنَّ — هَلْ تَرَيِنَّ", "en": "The separate-word rule applied to a weak verb.", "tr": "Munfasıl kelime kuralı illetli fiile uygulanmış.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«اِضْرِبُونَّ»",
   "right": "«اِضْرِبُنَّ — vâv düşer, dammesi kalır»",
   "why": {"en": "Before the nūn the plural wāw drops unless a fatḥa precedes it.", "tr": "Nûndan önce cemi vâvı, önünde fetha yoksa düşer."}},
  {"wrong": "«اِضْرِبَانْ»",
   "right": "«اِضْرِبَانِّ — tesniyede yalnız şeddeli nûn, kesre ile»",
   "why": {"en": "The light nūn would meet the quiescent alif.", "tr": "Hafif nûn sâkin elifle buluşurdu."}},
  {"wrong": "«وَاللهِ لَأَفْعَلُ الْفَرَائِضَ»",
   "right": "«وَاللهِ لَأَفْعَلَنَّ الْفَرَائِضَ — kasemin müsbet cevabında nûn lâzımdır»",
   "why": {"en": "An affirmative oath-answer in the present takes the lām and the nūn together.", "tr": "Muzâride müsbet kasem cevabı lâm ile nûnu birlikte alır."}}],
 "relatedNotes": ["nun-tawkid", "huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "al-muthanna", "al-mabni-wal-mudmar"]}

ADD_EN = (" Chapter 45 (notebook lines ~353-356): the nūn of emphasis — light and heavy with their vowels, the three places outside request, the vowel before the nūn, the light nūn barred from the dual and the feminine plural (Yūnus dissenting), and the separate-word / attached-word rule with the three hal tarā forms — the notebook's exposition, kept as commentary (s1-s7).")
ADD_TR = (" Kırk beşinci bâb (defter satırları ~353-356): te'kid nûnu — harekeleriyle hafif ve şeddeli, talep dışındaki üç yer, nûndan önceki hareke, tesniye ve cemi müennesten menedilen hafif nûn (Yûnus muhalif) ve üç hel terâ şekliyle munfasıl/muttasıl kelime kuralı — defterin açıklaması, şerh olarak (s1-s7).")
write_out(45, S, TITLE, ADD_EN, ADD_TR, "353-356", GLOSS_ADD, notes=(NOTE,),
          related=(("nun-tawkid", [K]), ("huruf-al-qasam-fil-kafiya", [K])))
report(45, S, GLOSS_ADD, (NOTE,))
