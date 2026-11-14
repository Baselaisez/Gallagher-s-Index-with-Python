# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 19: THE ISM TAFDIL. Defined in the notebook's own Arabic; أَفْعَلُ / فُعْلَى; خَيْر and شَرّ; the condition (a bare
triliteral that is no colour or defect) and the أَشَدُّ workaround; for the doer by rule and sometimes for the object; the three uses (annexed,
with مِنْ, with the lām) and the ban on joining two; the bare use only with a clue (اللهُ أَكْبَرُ); the two senses of the annexed form (the
described noun as one of the group, or absolute excess with the annexation as clarification — يُوسُفُ أَحْسَنُ إِخْوَتِهِ); agreement — free in the
first sense, obligatory in the second and with the lām, barred with مِنْ; and the five conditions under which it raises a written noun — the
مَسْأَلَةُ الْكُحْلِ with the notebook's reasons.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~273-282 of the transcription.

  VERBATIM: s1, s12 (the Kuḥl sentence as the notebook prints it). RESTORED (received matn, marked): s2, s4, s5, s7, s9, s10, s11.
  COMMENTARY (the notebook): s3, s6, s8, s13.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch19.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "ism-al-tafdil-fil-kafiya"
IT = "ism-tafdil"
TITLE = {"ar": "اِسْمُ التَّفْضِيلِ", "en": "The ism tafḍīl", "tr": "İsm-i tafdîl"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
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
def AW(): return W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya».")
def ZAYD(): return cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».")
def AFDAL(ar, en, tr, punct=None, full="أَفْضَلُ"): return cited(full, "afdal", "noun", ["mubtada-khabar", IT, "mamnu-min-sarf"], ar, en, tr, punct=punct)
def ANNAS(punct=None): return cited("النَّاسِ", "nas", "noun", ["idafa-definiteness", IT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of people».", "«insanların».", punct=punct)

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The ism tafḍīl: what is derived from a verb for one described by an excess over another.",
 "tr": "İsm-i tafdîl: başkası üzerine ziyadelikle vasıflanan zât için fiilden türetilen isimdir."},
 "tokens": [
  W("اسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", IT], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("التَّفْضِيلِ", "tafdil", "noun", ["idafa-definiteness", IT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«preference».", "«tafdîl».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("اشْتُقَّ", "ishtaqqa", "verb", ["ism-mawsul", "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.", "«is derived».", "«türetilen»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("فِعْلٍ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«fiil»."),
  li_("لِمَوْصُوفٍ", "mawsuf", "noun", [], "مَوْصُوفٍ مَجْرُورٌ.", "«for one described».", "«vasıflanan için».", "مَوْصُوفٍ"),
  bi_("بِزِيَادَةٍ", "ziyada", "noun", [IT], "زِيَادَةٍ مَجْرُورٌ — مُتَعَلِّقٌ بِمَوْصُوفٍ.", "«by an excess».", "«ziyadelikle».", "زِيَادَةٍ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«üzerine»."),
  W("غَيْرِهِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another».", "«başkası».", punct=".", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
 ]})

# ----------- s2 (RESTORED): the shape
S.append({"id": "s2", "translation": {
 "en": "And its shape is أَفْعَلُ for the masculine and فُعْلَى for the feminine." + R_EN,
 "tr": "Sîgası müzekker için أَفْعَلُ, müennes için فُعْلَى'dır." + R_TR},
 "tokens": [
  atf_wa("وَصِيغَتُهُ", "sigha", "noun", ["mubtada-khabar", "idafa-definiteness"], "صِيغَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its shape».", "«ve sîgası».", "صِيغَتُ", extra_segs=[seg("صِيغَتُ", "sigha", "noun"), pr3ms()]),
  cited("أَفْعَلُ", "afal-wazn", "noun", ["mubtada-khabar", IT, "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — الْوَزْنُ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«afʿal» — a diptote.", "«ef'al» — gayr-i munsarif."),
  li_("لِلْمُذَكَّرِ", "mudhakkar", "noun", [], "الْمُذَكَّرِ مَجْرُورٌ.", "«for the masculine».", "«müzekker için».", "الْمُذَكَّرِ", segs=[seg("لِ", "li", "prep"), seg("لْمُذَكَّرِ", "mudhakkar", "noun")]),
  cited_wa("وَفُعْلَى", "fula-wazn", "noun", ["mubtada-khabar", IT, "ism-maqsur-manqus"], "فُعْلَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَخَبَرُهُ لِلْمُؤَنَّثِ.", "«and fuʿlā».", "«ve fu'lâ».", "فُعْلَى"),
  li_("لِلْمُؤَنَّثِ", "muannath", "noun", ["mubtada-khabar", "al-muannath-wa-alamatuh"], "الْمُؤَنَّثِ مَجْرُورٌ — خَبَرٌ.", "«for the feminine».", "«müennes için».", "الْمُؤَنَّثِ", punct=".", segs=[seg("لِ", "li", "prep"), seg("لْمُؤَنَّثِ", "muannath", "noun")]),
 ]})

# ----------- s3 (COMMENTARY): خَيْر and شَرّ
S.append({"id": "s3", "translation": {
 "en": "And خَيْرٌ and شَرٌّ, used with مِنْ, are two ism tafḍīl, their origin being أَخْيَرُ and أَشَرُّ." + C_EN,
 "tr": "مِنْ ile kullanılan خَيْرٌ ve شَرٌّ aslında أَخْيَرُ ve أَشَرُّ olmakla iki ism-i tafdîldir." + C_TR},
 "tokens": [
  cited_wa("وَخَيْرٌ", "khayr", "noun", ["mubtada-khabar", IT], "خَيْرٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and khayr».", "«ve hayr».", "خَيْرٌ"),
  cited_wa("وَشَرٌّ", "sharr", "noun", ["mubtada-khabar", IT], "شَرٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and sharr».", "«ve şerr».", "شَرٌّ"),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — حَالٌ.", "«with».", "«... ile»."),
  cited("مِنْ", "min", "prep", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«min».", "«min»."),
  W("اسْمَا", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«are two nouns of».", "«iki ism-i»."),
  W("تَفْضِيلٍ", "tafdil", "noun", ["idafa-definiteness", IT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«preference».", "«tafdîldir».", punct="،"),
  W("أَصْلُهُمَا", "asl", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their origin».", "«asılları».", segments=[seg("أَصْلُ", "asl", "noun"), pr3d()]),
  cited("أَخْيَرُ", "akhyar-tafdil", "noun", ["mubtada-khabar", IT, "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — حُذِفَتْ هَمْزَتُهُ.", "«akhyar» — the hamza dropped.", "«ahyer» — hemzesi düşmüş."),
  cited_wa("وَأَشَرُّ", "asharr", "noun", [IT, "mamnu-min-sarf"], "أَشَرُّ مَعْطُوفٌ.", "«and asharr».", "«ve eşerr».", "أَشَرُّ", punct="."),
 ]})

# ----------- s4 (RESTORED): the condition
S.append({"id": "s4", "translation": {
 "en": "And its condition is that it be built from a bare triliteral that is neither a colour nor a defect — as in زَيْدٌ أَفْضَلُ النَّاسِ — so it is not built from the like of أَحْمَرَ and أَعْوَرَ." + R_EN,
 "tr": "Şartı, renk ve kusur olmayan sülâsî mücerredden binâ edilmesidir — زَيْدٌ أَفْضَلُ النَّاسِ gibi — bu yüzden أَحْمَرَ ve أَعْوَرَ gibilerden binâ edilmez." + R_TR},
 "tokens": [
  atf_wa("وَشَرْطُهُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness"], "شَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its condition».", "«ve şartı».", "شَرْطُ", extra_segs=[seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that».", "«-mesidir»."),
  W("يُبْنَى", "bana", "verb", ["naib-al-fail", "nawasib-wa-jawazim-al-mudari", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«it be built».", "«binâ edilmesi»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("ثُلَاثِيٍّ", "thulathi", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a triliteral».", "«sülâsî»."),
  W("مُجَرَّدٍ", "mujarrad", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«bare».", "«mücerred»."),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "naat-sifa"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ — وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ.", "«that is not».", "«olmayan»."),
  bi_("بِلَوْنٍ", "lawn", "noun", ["kana-wa-akhawatuha", IT], "لَوْنٍ مَجْرُورٌ لَفْظًا بِالْبَاءِ الزَّائِدَةِ — خَبَرُ لَيْسَ.", "«a colour».", "«renk».", "لَوْنٍ"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor».", "«ve ... değil».", "لَا"),
  W("عَيْبٍ", "ayb", "noun", ["atf-nasaq", IT], "مَعْطُوفٌ عَلَى لَوْنٍ مَجْرُورٌ.", "«a defect».", "«kusur».", punct="،"),
  nahwu(),
  ZAYD(),
  AFDAL("خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مِنْ فَضَلَ، ثُلَاثِيٌّ مُجَرَّدٌ.", "«the most excellent of» — from فَضَلَ.", "«en faziletlisi» — fadale'den."),
  ANNAS(punct="؛"),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«bu yüzden -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُبْنَى", "bana", "verb", ["naib-al-fail", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«is it built».", "«binâ edilir»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("نَحْوِ", "nahw", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the like of».", "«gibilerden»."),
  cited("أَحْمَرَ", "ahmar", "noun", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — لَوْنٌ.", "«red» — a colour.", "«kırmızı» — renk."),
  cited_wa("وَأَعْوَرَ", "awar", "noun", ["mamnu-min-sarf"], "أَعْوَرَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ — عَيْبٌ.", "«and one-eyed» — a defect.", "«ve tek gözlü» — kusur.", "أَعْوَرَ", punct="."),
 ]})

# ----------- s5 (RESTORED): أَشَدُّ
S.append({"id": "s5", "translation": {
 "en": "And if it is meant from other than the triliteral, or from a colour or a defect, one says هُوَ أَشَدُّ مِنْهُ اسْتِخْرَاجًا, and أَشَدُّ مِنْهُ بَيَاضًا, and أَشَدُّ مِنْهُ عَمًى." + R_EN,
 "tr": "Sülâsîden başkasından veya renk ve kusurdan kastedilirse هُوَ أَشَدُّ مِنْهُ اسْتِخْرَاجًا, أَشَدُّ مِنْهُ بَيَاضًا ve أَشَدُّ مِنْهُ عَمًى denir." + R_TR},
 "tokens": [
  W("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("قُصِدَ", "qasada", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it is meant».", "«kastedilirse»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«other than».", "«başkasından»."),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the triliteral».", "«sülâsînin»."),
  AW(),
  W("مِنَ", "min", "prep", ["atf-nasaq", "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("اللَّوْنِ", "lawn", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a colour».", "«renk»."),
  atf_wa("وَالْعَيْبِ", "ayb", "noun", [], "الْعَيْبِ مَعْطُوفٌ مَجْرُورٌ.", "«or a defect».", "«ve kusur».", "الْعَيْبِ"),
  W("قِيلَ", "qala", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — جَوَابُ الشَّرْطِ.", "«one says».", "«denir».", punct=":"),
  cited("هُوَ", "huwa", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«he».", "«o»."),
  cited("أَشَدُّ", "ashadd", "noun", ["mubtada-khabar", IT, "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ يَحْمِلُ الْمَعْنَى.", "«is stronger» — the carrier.", "«daha şiddetlidir» — taşıyıcı."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr", IT], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْمُفَضَّلُ عَلَيْهِ.", "«than him».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  cited("اسْتِخْرَاجًا", "istikhraj", "noun", ["tamyiz", "form-x-verbs"], "تَمْيِيزٌ مَنْصُوبٌ — مَصْدَرُ غَيْرِ الثُّلَاثِيِّ.", "«in extracting» — the tamyīz.", "«istihrac bakımından» — temyiz.", punct="،"),
  cited_wa("وَأَشَدُّ", "ashadd", "noun", [IT, "mamnu-min-sarf"], "أَشَدُّ مَعْطُوفٌ.", "«and stronger».", "«ve daha şiddetli».", "أَشَدُّ"),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«than him».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  cited("بَيَاضًا", "bayad", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — مَصْدَرُ اللَّوْنِ.", "«in whiteness».", "«beyazlık bakımından».", punct="،"),
  cited_wa("وَأَشَدُّ", "ashadd", "noun", [IT, "mamnu-min-sarf"], "أَشَدُّ مَعْطُوفٌ.", "«and stronger».", "«ve daha şiddetli».", "أَشَدُّ"),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«than him».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  cited("عَمًى", "ama-blindness", "noun", ["tamyiz", "ism-maqsur-manqus"], "تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — مَصْدَرُ الْعَيْبِ.", "«in blindness».", "«körlük bakımından».", punct="."),
 ]})

# ----------- s6 (COMMENTARY): for the doer, sometimes the object
S.append({"id": "s6", "translation": {
 "en": "And by rule it is for the doer — as أَفْضَلُ, أَعْلَمُ, أَعْقَلُ — and it has come for the object: أَعْذَرُ, أَلْوَمُ, أَشْغَلُ, أَشْهَرُ, أَعْرَفُ." + C_EN,
 "tr": "Kıyâsı fâil içindir — أَفْضَلُ، أَعْلَمُ، أَعْقَلُ gibi — mef'ûl için de gelmiştir: أَعْذَرُ، أَلْوَمُ، أَشْغَلُ، أَشْهَرُ، أَعْرَفُ." + C_TR},
 "tokens": [
  atf_wa("وَقِيَاسُهُ", "qiyas", "noun", ["mubtada-khabar", "idafa-definiteness"], "قِيَاسُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and by rule it».", "«ve kıyâsı».", "قِيَاسُ", extra_segs=[seg("قِيَاسُ", "qiyas", "noun"), pr3ms()]),
  li_("لِلْفَاعِلِ", "fail-doer", "noun", ["mubtada-khabar"], "الْفَاعِلِ مَجْرُورٌ — خَبَرٌ.", "«is for the doer».", "«fâil içindir».", "الْفَاعِلِ", segs=[seg("لِ", "li", "prep"), seg("لْفَاعِلِ", "fail-doer", "noun")]),
  nahwu(),
  AFDAL("فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«more excellent».", "«daha faziletli»."),
  cited_wa("وَأَعْلَمُ", "alam-tafdil", "noun", [IT, "mamnu-min-sarf"], "أَعْلَمُ مَعْطُوفٌ.", "«more knowing».", "«daha bilgili».", "أَعْلَمُ"),
  cited_wa("وَأَعْقَلُ", "aqal", "noun", [IT, "mamnu-min-sarf"], "أَعْقَلُ مَعْطُوفٌ.", "«more intelligent».", "«daha akıllı».", "أَعْقَلُ", punct="،"),
  atf_wa("وَجَاءَ", "jaa", "verb", ["fail"], "جَاءَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it has come».", "«ve gelmiştir».", "جَاءَ"),
  li_("لِلْمَفْعُولِ", "maful-noun", "noun", [], "الْمَفْعُولِ مَجْرُورٌ.", "«for the object».", "«mef'ûl için».", "الْمَفْعُولِ", segs=[seg("لِ", "li", "prep"), seg("لْمَفْعُولِ", "maful-noun", "noun")]),
  nahwu(),
  cited("أَعْذَرُ", "adhar", "noun", ["idafa-definiteness", IT, "mamnu-min-sarf"], "فِي مَحَلِّ جَرٍّ — بِمَعْنَى أَكْثَرُ مَعْذُورِيَّةً.", "«more excused».", "«daha mazur»."),
  cited_wa("وَأَلْوَمُ", "alwam", "noun", [IT, "mamnu-min-sarf"], "أَلْوَمُ مَعْطُوفٌ — أَكْثَرُ مَلُومِيَّةً.", "«more blamed».", "«daha kınanmış».", "أَلْوَمُ"),
  cited_wa("وَأَشْغَلُ", "ashghal", "noun", [IT, "mamnu-min-sarf"], "أَشْغَلُ مَعْطُوفٌ — أَكْثَرُ مَشْغُولِيَّةً.", "«more occupied».", "«daha meşgul».", "أَشْغَلُ"),
  cited_wa("وَأَشْهَرُ", "ashhar", "noun", [IT, "mamnu-min-sarf"], "أَشْهَرُ مَعْطُوفٌ — أَكْثَرُ شُهْرَةً.", "«more famous».", "«daha meşhur».", "أَشْهَرُ"),
  cited_wa("وَأَعْرَفُ", "arafu", "noun", [IT, "mamnu-min-sarf"], "أَعْرَفُ مَعْطُوفٌ — أَكْثَرُ مَعْرُوفِيَّةً.", "«better known».", "«daha ma'rûf».", "أَعْرَفُ", punct="."),
 ]})

# ----------- s7 (RESTORED): the three uses
S.append({"id": "s7", "translation": {
 "en": "And it is used in one of three ways: annexed, as زَيْدٌ أَفْضَلُ النَّاسِ; with مِنْ, as زَيْدٌ أَفْضَلُ مِنْ بَكْرٍ; and with the lām, as زَيْدٌ الْأَفْضَلُ — and two of them are not joined." + R_EN,
 "tr": "Üç şeyden biriyle kullanılır: muzâf olarak, زَيْدٌ أَفْضَلُ النَّاسِ gibi; مِنْ ile, زَيْدٌ أَفْضَلُ مِنْ بَكْرٍ gibi; lâm ile, زَيْدٌ الْأَفْضَلُ gibi — ikisi birleştirilmez." + R_TR},
 "tokens": [
  atf_wa("وَيُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "يُسْتَعْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is used».", "«ve kullanılır».", "يُسْتَعْمَلُ"),
  bi_("بِأَحَدِ", "ahad", "noun", ["idafa-definiteness"], "أَحَدِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in one of».", "«... -den biriyle».", "أَحَدِ"),
  W("ثَلَاثَةٍ", "thalatha", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«three».", "«üç».", punct=":"),
  W("مُضَافًا", "mudaf", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ.", "«annexed».", "«muzâf olarak»."),
  nahwu(),
  ZAYD(),
  AFDAL("خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the most excellent of».", "«en faziletlisi»."),
  ANNAS(punct="،"),
  atf_wa("وَبِمِنْ", "min", "prep", ["hal", "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَمِنْ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — مَعْطُوفٌ عَلَى مُضَافًا.", "«and with min».", "«ve min ile».", "مِنْ", extra_segs=[seg("بِ", "bi", "prep"), seg("مِنْ", "min", "prep")]),
  nahwu(),
  ZAYD(),
  AFDAL("خَبَرٌ مَرْفُوعٌ.", "«more excellent».", "«daha faziletlidir»."),
  cited("مِنْ", "min", "prep", ["huruf-jarr", IT], "حَرْفُ جَرٍّ — لِلْمُفَضَّلِ عَلَيْهِ.", "«than».", "«-den»."),
  cited("بَكْرٍ", "bakr", "propn", ["huruf-jarr", IT], "مَجْرُورٌ — الْمُفَضَّلُ عَلَيْهِ.", "«Bakr».", "«Bekir».", punct="،"),
  atf_wa("وَبِاللَّامِ", "lam-letter", "noun", ["hal", "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّامِ مَجْرُورٌ — مَعْطُوفٌ.", "«and with the lām».", "«ve lâm ile».", "اللَّامِ", extra_segs=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  nahwu(),
  ZAYD(),
  AFDAL("خَبَرٌ مَرْفُوعٌ — مُعَرَّفٌ بِاللَّامِ.", "«the most excellent».", "«en faziletli».", punct="؛", full="الْأَفْضَلُ"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -mez».", "لَا"),
  W("يُجْمَعُ", "jamaa", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«are joined».", "«birleştirilir»."),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arası»."),
  W("اثْنَيْنِ", "ithnan", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two».", "«ikisinin»."),
  W("مِنْهَا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ.", "«of them».", "«onlardan».", punct=".", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
 ]})

# ----------- s8 (COMMENTARY): the bare use
S.append({"id": "s8", "translation": {
 "en": "And it is not used without them except with a clue — as اللهُ أَكْبَرُ, that is, greater than everything." + C_EN,
 "tr": "Bunlarsız ancak karîne ile kullanılır — اللهُ أَكْبَرُ gibi, yani her şeyden büyük." + C_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -mez».", "لَا"),
  W("يُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is it used».", "«kullanılır»."),
  bi_("بِدُونِهَا", "duna", "noun", ["idafa-definiteness"], "دُونِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«without them».", "«bunlarsız».", "دُونِ", segs=[seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun"), pr3fs()]),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except».", "«ancak»."),
  bi_("بِقَرِينَةٍ", "qarina", "noun", [], "قَرِينَةٍ مَجْرُورٌ.", "«with a clue».", "«karîne ile».", "قَرِينَةٍ", punct="،"),
  nahwu(),
  cited("اللهُ", "allah", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«God».", "«Allah»."),
  cited("أَكْبَرُ", "akbar", "noun", ["mubtada-khabar", IT, "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ بِلَا مِنْ وَلَا إِضَافَةٍ وَلَا لَامٍ.", "«is greatest» — bare.", "«en büyüktür» — çıplak.", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["al-mabni-wal-mudmar"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».", punct=":"),
  cited("أَكْبَرُ", "akbar", "noun", ["mubtada-khabar", IT, "mamnu-min-sarf"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«greater».", "«daha büyük»."),
  W("مِنْ", "min", "prep", ["huruf-jarr", IT], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  W("كُلِّ", "kull", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«every».", "«her»."),
  W("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«thing».", "«şey».", punct="."),
 ]})

# ----------- s9 (RESTORED): the two senses of the annexed form
S.append({"id": "s9", "translation": {
 "en": "And the annexed form has two senses: the excess of the described noun over the muḍāf ilayh, on condition that it be a part of it — as زَيْدٌ أَفْضَلُ النَّاسِ, so يُوسُفُ أَحْسَنُ إِخْوَتِهِ is not said in this sense; and excess absolutely, the annexation being for clarification, so يُوسُفُ أَحْسَنُ إِخْوَتِهِ is permitted." + R_EN,
 "tr": "Muzâf olanın iki mânâsı vardır: mevsûfun muzâfun ileyh üzerine ziyadeliği, ondan bir parça olması şartıyla — زَيْدٌ أَفْضَلُ النَّاسِ gibi; bu mânâda يُوسُفُ أَحْسَنُ إِخْوَتِهِ denmez; ve mutlak ziyadelik, izâfet îzâh için olmak üzere; böylece يُوسُفُ أَحْسَنُ إِخْوَتِهِ câizdir." + R_TR},
 "tokens": [
  atf_wa("وَالْمُضَافُ", "mudaf", "noun", ["mubtada-khabar"], "الْمُضَافُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the annexed form».", "«ve muzâf olan».", "الْمُضَافُ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ.", "«has».", "«... üzeredir»."),
  W("مَعْنَيَيْنِ", "mana", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ.", "«two senses».", "«iki mânâ».", punct=":"),
  W("زِيَادَةُ", "ziyada", "noun", ["mubtada-khabar", "idafa-definiteness", IT], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ، وَخَبَرُهُ مَحْذُوفٌ: أَحَدُهُمَا.", "«the excess of».", "«ziyadeliği»."),
  W("الْمَوْصُوفِ", "mawsuf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the described noun».", "«mevsûfun»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«üzerine»."),
  W("الْمُضَافِ", "mudaf", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the muḍāf».", "«muzâfun»."),
  W("إِلَيْهِ", "ilayhi", "part", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — تَمَامُ الْمُصْطَلَحِ.", "«ilayh».", "«ileyh»."),
  bi_("بِشَرْطِ", "shart", "noun", ["idafa-definiteness"], "شَرْطِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«on condition».", "«şartıyla».", "شَرْطِ"),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that».", "«-ması»."),
  W("يَكُونَ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — الْمَوْصُوفُ.", "«it be».", "«olması»."),
  W("بَعْضًا", "bad", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«a part».", "«bir parça»."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«of it».", "«ondan».", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  nahwu(),
  ZAYD(),
  AFDAL("خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — زَيْدٌ بَعْضُ النَّاسِ.", "«the most excellent of» — Zayd is one of the people.", "«en faziletlisi» — Zeyd insanlardan biridir."),
  ANNAS(punct="،"),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«bu yüzden -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is it said».", "«denir»."),
  cited("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Yūsuf».", "«Yûsuf»."),
  cited("أَحْسَنُ", "ahsan", "noun", ["mubtada-khabar", "idafa-definiteness", IT, "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the most beautiful of».", "«en güzeli»."),
  cited("إِخْوَتِهِ", "akh", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — يُوسُفُ لَيْسَ بَعْضًا مِنْ إِخْوَتِهِ.", "«his brothers» — Yūsuf is not one of them.", "«kardeşlerinin» — Yûsuf onlardan biri değildir.", segments=[seg("إِخْوَتِ", "akh", "noun"), pr3msi()]),
  bi_("بِهٰذَا", "hadha", "pron", ["asma-al-ishara-wal-mawsulat"], "هٰذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«in this».", "«bu».", "هٰذَا"),
  W("الْمَعْنَى", "mana", "noun", ["badal", "ism-maqsur-manqus"], "بَدَلٌ مِنْ هٰذَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«sense».", "«mânâda».", punct="؛"),
  atf_wa("وَالزِّيَادَةُ", "ziyada", "noun", ["mubtada-khabar", IT], "الزِّيَادَةُ مُبْتَدَأٌ مَرْفُوعٌ، وَخَبَرُهُ مَحْذُوفٌ: الثَّانِي.", "«and excess».", "«ve ziyadelik».", "الزِّيَادَةُ"),
  W("مُطْلَقًا", "mutlaqan", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«absolutely».", "«mutlak olarak».", punct="،"),
  atf_wa("وَالْإِضَافَةُ", "idafa", "noun", ["mubtada-khabar"], "الْإِضَافَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the annexation».", "«ve izâfet».", "الْإِضَافَةُ"),
  li_("لِلْإِيضَاحِ", "idah", "noun", ["mubtada-khabar"], "الْإِيضَاحِ مَجْرُورٌ — خَبَرٌ.", "«is for clarification».", "«îzâh içindir».", "الْإِيضَاحِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لْإِيضَاحِ", "idah", "noun")]),
  W("فَيَجُوزُ", "jaaza", "verb", ["fail", "al-fa-fi-khabar-al-mubtada", "hollow-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ، وَفَاعِلُهُ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«so … is permitted».", "«böylece câizdir».", segments=[seg("فَ", "fa", "conj"), seg("يَجُوزُ", "jaaza", "verb")]),
  cited("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Yūsuf».", "«Yûsuf»."),
  cited("أَحْسَنُ", "ahsan", "noun", ["mubtada-khabar", "idafa-definiteness", IT, "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the most beautiful» — absolutely.", "«en güzeli» — mutlak."),
  cited("إِخْوَتِهِ", "akh", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْإِضَافَةُ لِلْإِيضَاحِ.", "«his brothers» — the annexation clarifies.", "«kardeşlerinin» — izâfet îzâh eder.", punct=".", segments=[seg("إِخْوَتِ", "akh", "noun"), pr3msi()]),
 ]})

# ----------- s10 (RESTORED): agreement
S.append({"id": "s10", "translation": {
 "en": "And in the first its singularity and its agreement with the described noun are both permitted — as الزَّيْدَانِ أَفْضَلُ النَّاسِ and أَفْضَلَا النَّاسِ, هِنْدٌ أَفْضَلُ النَّاسِ and فُضْلَى النِّسَاءِ; in the second and with the lām agreement is obligatory; and with مِنْ the singular masculine is obligatory — as هِنْدٌ أَفْضَلُ مِنْ عَمْرٍو." + R_EN,
 "tr": "Birincide müfred kalması da mevsûfa mutâbakatı da câizdir — الزَّيْدَانِ أَفْضَلُ النَّاسِ ve أَفْضَلَا النَّاسِ, هِنْدٌ أَفْضَلُ النَّاسِ ve فُضْلَى النِّسَاءِ gibi; ikincide ve lâm ile mutâbakat lâzımdır; مِنْ ile müfred müzekker lâzımdır — هِنْدٌ أَفْضَلُ مِنْ عَمْرٍو gibi." + R_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("الْأَوَّلِ", "awwal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the first».", "«birinci»."),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«are permitted».", "«câizdir»."),
  W("إِفْرَادُهُ", "ifrad", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its singularity».", "«müfred kalması».", segments=[seg("إِفْرَادُ", "ifrad", "noun"), pr3ms()]),
  atf_wa("وَمُطَابَقَتُهُ", "mutabaqa", "noun", ["fail", "idafa-definiteness"], "مُطَابَقَتُ مَعْطُوفٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its agreement».", "«ve mutâbakatı».", "مُطَابَقَتُ", extra_segs=[seg("مُطَابَقَتُ", "mutabaqa", "noun"), pr3ms()]),
  li_("لِلْمَوْصُوفِ", "mawsuf", "noun", [], "الْمَوْصُوفِ مَجْرُورٌ.", "«with the described noun».", "«mevsûfa».", "الْمَوْصُوفِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لْمَوْصُوفِ", "mawsuf", "noun")]),
  nahwu(),
  cited("الزَّيْدَانِ", "zayd", "propn", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ.", "«the two Zayds».", "«iki Zeyd»."),
  AFDAL("خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مُفْرَدٌ لِمُثَنًّى.", "«the most excellent of» — singular for a dual.", "«en faziletlisi» — tesniye için müfred."),
  ANNAS(),
  cited_wa("وَأَفْضَلَا", "afdal", "noun", ["mubtada-khabar", "al-muthanna", IT], "أَفْضَلَا مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ — مُطَابِقٌ.", "«and the two most excellent of» — agreeing.", "«ve en faziletli ikisi» — mutâbık.", "أَفْضَلَا"),
  ANNAS(punct="،"),
  cited_wa("وَهِنْدٌ", "hind", "propn", ["mubtada-khabar"], "هِنْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and Hind».", "«ve Hind».", "هِنْدٌ"),
  AFDAL("خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مُذَكَّرٌ لِمُؤَنَّثٍ.", "«the most excellent of» — masculine for a feminine.", "«en faziletlisi» — müennes için müzekker."),
  ANNAS(),
  cited_wa("وَفُضْلَى", "fudla", "noun", ["mubtada-khabar", IT, "ism-maqsur-manqus"], "فُضْلَى مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ — مُطَابِقٌ.", "«and the most excellent (f.) of» — agreeing.", "«ve en faziletlisi (müennes)» — mutâbık.", "فُضْلَى"),
  cited("النِّسَاءِ", "nisa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«women».", "«kadınların».", punct="؛"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("الثَّانِي", "thani", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second».", "«ikinci»."),
  atf_wa("وَمَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "مَعَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and with».", "«ve ... ile».", "مَعَ"),
  W("اللَّامِ", "lam-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the lām».", "«lâm»."),
  W("تَلْزَمُ", "lazima", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is obligatory».", "«lâzımdır»."),
  W("الْمُطَابَقَةُ", "mutabaqa", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«agreement».", "«mutâbakat».", punct="؛"),
  atf_wa("وَمَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "مَعَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and with».", "«ve ... ile».", "مَعَ"),
  cited("مِنْ", "min", "prep", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«min».", "«min»."),
  W("يَلْزَمُ", "lazima", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is obligatory».", "«lâzımdır»."),
  W("الْإِفْرَادُ", "ifrad", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the singular».", "«müfred»."),
  atf_wa("وَالتَّذْكِيرُ", "tadhkir", "noun", [], "التَّذْكِيرُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the masculine».", "«ve müzekker».", "التَّذْكِيرُ", punct="،"),
  nahwu(),
  cited("هِنْدٌ", "hind", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Hind».", "«Hind»."),
  AFDAL("خَبَرٌ مَرْفُوعٌ — مُفْرَدٌ مُذَكَّرٌ لِمُؤَنَّثٍ.", "«more excellent» — masculine singular.", "«daha faziletlidir» — müfred müzekker."),
  cited("مِنْ", "min", "prep", ["huruf-jarr", IT], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  cited("عَمْرٍو", "amr-name", "propn", ["huruf-jarr", IT], "مَجْرُورٌ — الْمُفَضَّلُ عَلَيْهِ.", "«ʿAmr».", "«Amr».", punct="."),
 ]})

# ----------- s11 (RESTORED + the notebook's five): government
S.append({"id": "s11", "translation": {
 "en": "And it is a weak governor, so it raises a written noun only under five conditions: that it be a ṣifa of a thing in wording and of that thing's effect in sense; that this effect be the preferred one in respect of the first and the one preferred over in respect of another; and that the speech be negated." + R_EN,
 "tr": "Zayıf bir âmildir; bu yüzden zâhir ismi ancak beş şartla ref' eder: lafızda bir şeyin, mânâda o şeyin müsebbebinin sıfatı olması; o müsebbebin birinciye nisbetle mufaddal, başkasına nisbetle mufaddalun aleyh olması; ve kelâmın menfî olması." + R_TR},
 "tokens": [
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هُوَ"),
  W("عَامِلٌ", "amil", "noun", ["mubtada-khabar", IT], "خَبَرٌ مَرْفُوعٌ.", "«a governor».", "«bir âmildir»."),
  W("ضَعِيفٌ", "daif", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«weak».", "«zayıf».", punct="،"),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«bu yüzden -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يَرْفَعُ", "rafaa", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«does it raise».", "«ref' eder»."),
  W("الِاسْمَ", "ism", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a noun».", "«ismi»."),
  W("الظَّاهِرَ", "zahir", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«written».", "«zâhir»."),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ حَصْرٍ.", "«only».", "«ancak»."),
  bi_("بِخَمْسَةِ", "khamsa", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya"], "خَمْسَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«under five».", "«beş».", "خَمْسَةِ"),
  W("شُرُوطٍ", "shart", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«conditions».", "«şartla».", punct=":"),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَوَّلُهَا.", "«that».", "«-ması»."),
  W("يَكُونَ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«it be».", "«olması»."),
  W("صِفَةً", "sifa", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«a ṣifa».", "«sıfat»."),
  li_("لِشَيْءٍ", "shay", "noun", [], "شَيْءٍ مَجْرُورٌ.", "«of a thing».", "«bir şeyin».", "شَيْءٍ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("اللَّفْظِ", "lafz", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«wording».", "«lafız»."),
  atf_wa("وَلِمُسَبَّبِهِ", "musabbab", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَمُسَبَّبِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and of its effect».", "«ve müsebbebinin».", "لِ", extra_segs=[seg("لِ", "li", "prep"), seg("مُسَبَّبِ", "musabbab", "noun"), pr3msi()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الْمَعْنَى", "mana", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«sense».", "«mânâ».", punct="،"),
  atf_wa("وَأَنْ", "an-masdariyya", "part", ["an-masdariyya"], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«and that».", "«ve -ması».", "أَنْ"),
  W("يَكُونَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«be».", "«olması»."),
  W("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara-wal-mawsulat", "kana-wa-akhawatuha"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُونَ.", "«that».", "«o»."),
  W("الْمُسَبَّبُ", "musabbab", "noun", ["badal"], "بَدَلٌ مَرْفُوعٌ.", "«effect».", "«müsebbeb»."),
  W("مُفَضَّلًا", "mufaddal", "noun", ["kana-wa-akhawatuha", IT], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«the preferred».", "«mufaddal»."),
  bi_("بِاعْتِبَارِ", "itibar", "noun", ["idafa-definiteness"], "اعْتِبَارِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in respect of».", "«... nisbetle».", "اعْتِبَارِ"),
  W("الْأَوَّلِ", "awwal", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the first».", "«birinciye»."),
  atf_wa("وَمُفَضَّلًا", "mufaddal", "noun", [IT], "مُفَضَّلًا مَعْطُوفٌ مَنْصُوبٌ.", "«and the one preferred».", "«ve mufaddal».", "مُفَضَّلًا"),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — تَمَامُ الْمُصْطَلَحِ.", "«over».", "«aleyh».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  bi_("بِالنِّسْبَةِ", "nisba", "noun", [], "النِّسْبَةِ مَجْرُورٌ.", "«in relation».", "«nisbetle».", "النِّسْبَةِ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("غَيْرِهِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another».", "«başkasına».", punct="،", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  atf_wa("وَأَنْ", "an-masdariyya", "part", ["an-masdariyya"], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«and that».", "«ve -ması».", "أَنْ"),
  W("يَكُونَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«be».", "«olması»."),
  W("الْكَلَامُ", "kalam", "noun", ["kana-wa-akhawatuha"], "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the speech».", "«kelâmın»."),
  W("مَنْفِيًّا", "manfi", "noun", ["kana-wa-akhawatuha", "ism-maful"], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«negated».", "«menfî».", punct="."),
 ]})

# ----------- s12 (VERBATIM): the Kuḥl sentence
S.append({"id": "s12", "translation": {
 "en": "As in: I have seen no man in whose eye the kohl is more beautiful than it is in Zayd's eye — so الْكُحْلُ is the doer of أَحْسَنَ.",
 "tr": "Meselâ: Gözündeki sürme Zeyd'in gözündeki sürmeden daha güzel olan hiçbir adam görmedim — öyleyse الْكُحْلُ, أَحْسَنَ'nin fâilidir."},
 "tokens": [
  nahwu(),
  cited("مَا", "ma-nafiya", "part", ["ma-la-laysa-wa-la-al-jins", IT], "نَافِيَةٌ — الشَّرْطُ الْخَامِسُ.", "«not» — the fifth condition.", "«-medim» — beşinci şart."),
  cited("رَأَيْتُ", "raa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I have seen».", "«görmedim».", segments=[seg("رَأَيْ", "raa", "verb"), prT()]),
  cited("رَجُلًا", "rajul", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمَوْصُوفُ فِي اللَّفْظِ.", "«a man» — described in wording.", "«bir adam» — lafızda mevsûf."),
  cited("أَحْسَنَ", "ahsan", "noun", ["naat-sifa", IT, "mamnu-min-sarf"], "صِفَةٌ لِرَجُلًا مَنْصُوبَةٌ — اسْمُ تَفْضِيلٍ بِمَعْنَى حَسُنَ، عَامِلٌ.", "«more beautiful» — the governing elative.", "«daha güzel» — amel eden ism-i tafdîl."),
  cited("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("عَيْنِهِ", "ayn-eye", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — يَعُودُ إِلَى رَجُلٍ.", "«his eye».", "«gözünde».", segments=[seg("عَيْنِ", "ayn-eye", "noun"), pr3msi()]),
  cited("الْكُحْلُ", "kuhl", "noun", ["fail", IT], "فَاعِلٌ لِأَحْسَنَ مَرْفُوعٌ — الْمُسَبَّبُ، الْمَوْصُوفُ فِي الْمَعْنَى.", "«the kohl» — the elative's doer.", "«sürme» — ism-i tafdîlin fâili."),
  cited("مِنْهُ", "min", "prep", ["huruf-jarr", IT], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — يَعُودُ إِلَى الْكُحْلِ.", "«than it».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  cited("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("عَيْنِ", "ayn-eye", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the eye of».", "«gözünde»."),
  cited("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'in».", punct="،"),
  W("فَالْكُحْلُ", "kuhl", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْكُحْلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the kohl».", "«öyleyse sürme».", segments=[seg("فَ", "fa", "conj"), seg("الْكُحْلُ", "kuhl", "noun")]),
  W("فَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the doer of».", "«fâilidir»."),
  cited("أَحْسَنَ", "ahsan", "noun", ["idafa-definiteness", IT], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«aḥsana».", "«ahsene'nin».", punct="."),
 ]})

# ----------- s13 (COMMENTARY): why the negation, and why not a mubtada
S.append({"id": "s13", "translation": {
 "en": "And the negation was required because the particle of negation negates the excess, so that أَحْسَنَ comes to mean حَسُنَ; and were الْكُحْلُ raised as a delayed mubtada, a foreign word would stand between أَحْسَنَ and its governed مِنْهُ." + C_EN,
 "tr": "Nefy şart kılındı, çünkü nefy edatı ziyadeliği nefy eder; böylece أَحْسَنَ, حَسُنَ mânâsına gelir. الْكُحْلُ muahhar mübtedâ olarak ref' edilseydi, أَحْسَنَ ile ma'mûlü مِنْهُ arasına ecnebî bir kelime girmiş olurdu." + C_TR},
 "tokens": [
  atf_wa("وَاشْتُرِطَ", "ishtarata", "verb", ["naib-al-fail", "form-viii-verbs"], "اشْتُرِطَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … was required».", "«ve şart kılındı».", "اشْتُرِطَ"),
  W("النَّفْيُ", "nafy", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the negation».", "«nefy»."),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("أَدَاةَ", "adat", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the particle of».", "«edatı»."),
  W("النَّفْيِ", "nafy", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«negation».", "«nefy»."),
  W("تَنْفِي", "nafa", "verb", ["inna-wa-akhawatuha", "fail", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«negates».", "«nefy eder»."),
  W("الزِّيَادَةَ", "ziyada", "noun", ["maful-bihi", IT], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the excess».", "«ziyadeliği».", punct="،"),
  W("فَيَصِيرُ", "sara", "verb", ["kana-wa-akhawatuha", "al-fa-fi-khabar-al-mubtada", "hollow-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَصِيرُ فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«so … comes to be».", "«böylece ... olur».", segments=[seg("فَ", "fa", "conj"), seg("يَصِيرُ", "sara", "verb")]),
  cited("أَحْسَنَ", "ahsan", "noun", ["kana-wa-akhawatuha", IT], "فِي مَحَلِّ رَفْعٍ اسْمُ يَصِيرُ.", "«aḥsana».", "«ahsene»."),
  bi_("بِمَعْنَى", "mana", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ يَصِيرُ.", "«in the sense of».", "«mânâsına».", "مَعْنَى"),
  cited("حَسُنَ", "hasuna", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«ḥasuna» — «was beautiful».", "«hasune» — «güzel oldu».", punct="؛"),
  atf_wa("وَلَوْ", "law", "part", ["al-majzum-wal-shart-wal-jaza"], "لَوْ حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«and were».", "«ve ... -seydi».", "لَوْ"),
  W("رُفِعَ", "rafaa", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«raised».", "«ref' edilseydi»."),
  cited("الْكُحْلُ", "kuhl", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the kohl».", "«sürme»."),
  W("مُبْتَدَأً", "mubtada", "noun", ["hal", "mubtada-khabar"], "حَالٌ مَنْصُوبٌ.", "«as a mubtada».", "«mübtedâ olarak»."),
  W("مُؤَخَّرًا", "muakhkhar", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَنْصُوبَةٌ.", "«delayed».", "«muahhar».", punct="،"),
  W("لَفُصِلَ", "fasala", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَفُصِلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«there would stand … between».", "«... arasına girmiş olurdu».", segments=[seg("لَ", "lam-jawab", "part"), seg("فُصِلَ", "fasala", "verb")]),
  bi_("بِأَجْنَبِيٍّ", "ajnabi", "noun", [], "أَجْنَبِيٍّ مَجْرُورٌ — مَعْمُولُ الْعَامِلِ الْمَعْنَوِيِّ.", "«a foreign word».", "«ecnebî bir kelime».", "أَجْنَبِيٍّ"),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasına»."),
  cited("أَحْسَنَ", "ahsan", "noun", ["idafa-definiteness", IT], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«aḥsana».", "«ahsene»."),
  atf_wa("وَمَعْمُولِهِ", "mamul", "noun", ["idafa-definiteness"], "مَعْمُولِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its governed word».", "«ve ma'mûlü».", "مَعْمُولِ", extra_segs=[seg("مَعْمُولِ", "mamul", "noun"), pr3msi()]),
  cited("مِنْهُ", "min", "prep", ["badal"], "بَدَلٌ مِنْ مَعْمُولِهِ — الْجَارُّ وَالْمَجْرُورُ الْمَحْكِيُّ.", "«minhu».", "«minhü».", punct=".", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
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
 "afal-wazn": need("afal-wazn", "أَفْعَل", None, "noun", "the pattern أَفْعَلُ — the ism tafḍīl (and the colour/defect adjective), a diptote", "ef'al vezni — ism-i tafdîl (ve renk/kusur sıfatı), gayr-i munsarif", 3),
 "fula-wazn": need("fula-wazn", "فُعْلَى", None, "noun", "the pattern فُعْلَى — the feminine of the ism tafḍīl (كُبْرَى، فُضْلَى)", "fu'lâ vezni — ism-i tafdîlin müennesi (kübrâ, fudlâ)", 3),
 "akhyar-tafdil": need("akhyar-tafdil", "أَخْيَر", "خ ي ر", "noun", "better — the full form behind خَيْر the elative", "daha hayırlı — ism-i tafdîl olan hayr'ın tam biçimi", 4),
 "asharr": need("asharr", "أَشَرّ", "ش ر ر", "noun", "worse — the full form behind شَرّ the elative", "daha kötü — ism-i tafdîl olan şerr'in tam biçimi", 4),
 "bayad": need("bayad", "بَيَاض", "ب ي ض", "noun", "whiteness — the maṣdar of a colour", "beyazlık — bir rengin masdarı", 3),
 "ama-blindness": need("ama-blindness", "عَمًى", "ع م ي", "noun", "blindness — the maṣdar of a defect, a maqṣūr", "körlük — bir kusurun masdarı, maksûr", 3),
 "adhar": need("adhar", "أَعْذَر", "ع ذ ر", "noun", "more excused — an elative in the sense of the object", "daha mazur — mef'ûl mânâsında ism-i tafdîl", 5),
 "alwam": need("alwam", "أَلْوَم", "ل و م", "noun", "more blamed — an elative in the sense of the object", "daha kınanmış — mef'ûl mânâsında ism-i tafdîl", 5),
 "ashghal": need("ashghal", "أَشْغَل", "ش غ ل", "noun", "more occupied — an elative in the sense of the object", "daha meşgul — mef'ûl mânâsında ism-i tafdîl", 5),
 "fudla": need("fudla", "فُضْلَى", "ف ض ل", "noun", "the most excellent (feminine) — the فُعْلَى of أَفْضَل", "en faziletli (müennes) — efdal'in fu'lâsı", 4),
 "muakhkhar": need("muakhkhar", "مُؤَخَّر", "أ خ ر", "noun", "delayed, placed later (of a mubtada or khabar)", "muahhar, sonraya bırakılmış (mübtedâ veya haber için)", 4),
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
print("kafiya ch19 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "اسْمُ التَّفْضِيلِ فِي الْكَافِيَةِ", "en": "The ism tafḍīl in the Kafiya: definition, shape, the colour-and-defect bar with the أَشَدُّ workaround, the three uses, the two senses of annexation and their agreement, and the five conditions of مَسْأَلَةُ الْكُحْلِ", "tr": "Kâfiye'de ism-i tafdîl: tarif, sîga, renk-kusur yasağı ve أَشَدُّ çözümü, üç kullanım, izâfetin iki mânâsı ve uyumları, ve Kuhl meselesinin beş şartı"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — اسم التفضيل: ما اشتق من فعل لموصوف بزيادة على غيره؛ أفعل وفعلى؛ شرطه؛ يستعمل بمن أو مضافا أو باللام؛ المضاف على معنيين؛ ولا يرفع الظاهر إلا في مسألة الكحل", "ضياء صونغور اوغلى — دفتر الكافية: خير وشر؛ أشد منه استخراجا وبياضا وعمى؛ أفضل وأعلم وأعقل للفاعل، أعذر وألوم وأشغل وأشهر وأعرف للمفعول؛ الله أكبر بالقرينة؛ يوسف أحسن إخوته؛ الشروط الخمسة ومثال الكحل وتعليل النفي والأجنبي"],
 "question": {
  "en": ["What is an ISM TAFḌĪL? A noun derived from a verb for the one described as having MORE of the quality than another: أَفْضَلُ, «more excellent». Its shape is أَفْعَلُ, a diptote, and فُعْلَى for the feminine; خَيْر and شَرّ with مِنْ are elatives that have shed their hamza.",
         "From which verbs may it be built? Only from a bare triliteral that names neither a colour nor a defect — because أَحْمَر and أَعْوَر already occupy the أَفْعَل shape as plain adjectives. Everything else borrows a carrier: أَشَدُّ مِنْهُ اسْتِخْرَاجًا (an augmented verb), أَشَدُّ مِنْهُ بَيَاضًا (a colour), أَشَدُّ مِنْهُ عَمًى (a defect) — the maṣdar follows as a tamyīz.",
         "Whom does it describe? By rule the doer (أَفْضَل، أَعْلَم، أَعْقَل); by hearing sometimes the object — أَعْذَر «more excused», أَشْهَر «more famous», أَعْرَف «better known».",
         "How is it USED? In one of three ways, never two at once: annexed (أَفْضَلُ النَّاسِ), with مِنْ (أَفْضَلُ مِنْ بَكْرٍ), or with the article (الْأَفْضَلُ). Bare, only when the context supplies the comparison — اللهُ أَكْبَرُ.",
         "What are the two senses of أَفْضَلُ النَّاسِ? Either Zayd exceeds the group he belongs to — then he must be ONE of them, which is why يُوسُفُ أَحْسَنُ إِخْوَتِهِ fails in this sense (Yūsuf is not one of his own brothers); or the excess is absolute and the annexation merely says whom we are talking about — then the same sentence is fine.",
         "Does it agree? In the first annexed sense you may leave it singular masculine or make it agree (الزَّيْدَانِ أَفْضَلُ النَّاسِ / أَفْضَلَا النَّاسِ, هِنْدٌ أَفْضَلُ النَّاسِ / فُضْلَى النِّسَاءِ); in the second sense and with the article it must agree; with مِنْ it is always singular masculine (هِنْدٌ أَفْضَلُ مِنْ عَمْرٍو).",
         "When does it GOVERN a written noun? Only in the مَسْأَلَةُ الْكُحْلِ: مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ. Five conditions meet there — the elative describes the man in wording and the kohl in sense, the kohl is preferred in his eye and preferred-over in Zayd's, and the sentence is negated, which drains the comparison out of أَحْسَنَ and leaves it meaning حَسُنَ, a verb that can take a doer. Reading الْكُحْلُ as a mubtada instead would plant a foreign word between أَحْسَنَ and its مِنْهُ."],
  "tr": ["İSM-İ TAFDÎL nedir? Bir vasfı başkasından DAHA ÇOK taşıyan diye nitelenen için fiilden türetilen isim: أَفْضَلُ, «daha faziletli». Sîgası gayr-i munsarif أَفْعَلُ, müennesi فُعْلَى; مِنْ ile خَيْر ve شَرّ hemzesini atmış ism-i tafdîllerdir.",
         "Hangi fiillerden binâ edilir? Yalnız renk ya da kusur bildirmeyen sülâsî mücerredden — çünkü أَحْمَر ve أَعْوَر, أَفْعَل biçimini düz sıfat olarak zaten doldurur. Gerisi bir taşıyıcı ödünç alır: أَشَدُّ مِنْهُ اسْتِخْرَاجًا (mezîd fiil), أَشَدُّ مِنْهُ بَيَاضًا (renk), أَشَدُّ مِنْهُ عَمًى (kusur) — masdar temyiz olarak izler.",
         "Kimi niteler? Kıyâsen fâili (أَفْضَل، أَعْلَم، أَعْقَل); semâan bazen mef'ûlü — أَعْذَر «daha mazur», أَشْهَر «daha meşhur», أَعْرَف «daha ma'rûf».",
         "Nasıl KULLANILIR? Üç yoldan biriyle, asla ikisiyle birden: muzâf (أَفْضَلُ النَّاسِ), مِنْ ile (أَفْضَلُ مِنْ بَكْرٍ) ya da lâm ile (الْأَفْضَلُ). Çıplak, yalnız bağlam karşılaştırmayı verdiğinde — اللهُ أَكْبَرُ.",
         "أَفْضَلُ النَّاسِ'in iki mânâsı nedir? Ya Zeyd ait olduğu topluluğu aşar — o zaman onlardan BİRİ olmalıdır; bu mânâda يُوسُفُ أَحْسَنُ إِخْوَتِهِ'nin bozuk olmasının sebebi budur (Yûsuf kendi kardeşlerinden biri değildir); ya da ziyadelik mutlaktır ve izâfet yalnız kimden söz ettiğimizi söyler — o zaman aynı cümle doğrudur.",
         "Uyar mı? Birinci muzâf mânâda müfred müzekker bırakabilir ya da uydurabilirsiniz (الزَّيْدَانِ أَفْضَلُ النَّاسِ / أَفْضَلَا النَّاسِ, هِنْدٌ أَفْضَلُ النَّاسِ / فُضْلَى النِّسَاءِ); ikinci mânâda ve lâm ile uymak zorundadır; مِنْ ile her zaman müfred müzekkerdir (هِنْدٌ أَفْضَلُ مِنْ عَمْرٍو).",
         "Zâhir ismi ne zaman YÖNETİR? Yalnız Kuhl meselesinde: مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ. Orada beş şart buluşur — ism-i tafdîl lafızda adamı, mânâda sürmeyi niteler; sürme onun gözünde mufaddal, Zeyd'inkinde mufaddalun aleyhtir; cümle menfîdir ki bu أَحْسَنَ'den karşılaştırmayı boşaltıp onu fâil alabilen bir fiil olan حَسُنَ mânâsında bırakır. الْكُحْلُ'ü mübtedâ okumak ise أَحْسَنَ ile مِنْهُ'sünün arasına ecnebî bir kelime sokardı."]},
 "plain": {
  "en": "An ism tafḍīl is the «more/most» form (أَفْضَل «more excellent», فُضْلَى for women). It is built only from simple verbs that are not colours or defects, used either annexed, with مِنْ, or with the article, and it almost never takes a subject of its own — except in one famous sentence about kohl.",
  "tr": "İsm-i tafdîl «daha/en» biçimidir (أَفْضَل «daha faziletli», kadınlar için فُضْلَى). Yalnız renk ya da kusur olmayan basit fiillerden kurulur; ya muzâf, ya مِنْ ile, ya da lâm ile kullanılır ve kendi öznesini hemen hiç almaz — sürme hakkındaki ünlü tek cümle dışında."},
 "explanation": {
  "en": "The elative is defined by its one job — to say that its subject has more of a quality than someone else — and everything in the chapter follows from how little grammar that job needs. Its shape is fixed, a diptote أَفْعَلُ with فُعْلَى beside it, and its source is restricted to the bare triliteral because the colours and defects have already taken the shape for their plain adjectives; where the shape is unavailable the language carries the comparison on أَشَدُّ and hands the quality to a tamyīz. It is used in exactly three frames, which cannot be stacked, and the chapter's finest point is the two readings of the annexed frame: a man can be the most excellent OF the people only if he is one of them, which is why the Qurʾānic brothers of Yūsuf cannot be his comparison class in that sense — but Arabic also uses the annexation merely to point, and in that absolute sense the same words stand. Agreement follows the sense: optional in the first, obligatory in the second and under the article, forbidden with مِنْ. Its government closes the chapter and the notebook spends its longest passage on it. The elative is too weak a governor to raise a written doer except in one configuration, the Kuḥl sentence, where five conditions coincide; the notebook's explanation of the last of them is the lesson — a negation strips the comparison out of the elative and leaves it meaning the plain verb, and only then can it take a doer, while the alternative reading would break the bond between the elative and its مِنْهُ with a word that belongs to neither.",
  "tr": "İsm-i tafdîl tek işiyle tarif edilir — öznesinin bir vasfı başkasından daha çok taşıdığını söylemek — ve bâbdaki her şey bu işin ne kadar az nahiv gerektirdiğinden çıkar. Sîgası sabittir, yanında فُعْلَى ile gayr-i munsarif bir أَفْعَلُ; kaynağı sülâsî mücerredle sınırlıdır, çünkü renkler ve kusurlar biçimi düz sıfatları için zaten almıştır; biçim müsait olmadığında dil karşılaştırmayı أَشَدُّ üzerinde taşır ve vasfı bir temyize verir. Tam üç çerçevede kullanılır, bunlar üst üste konamaz ve bâbın en ince noktası muzâf çerçevenin iki okunuşudur: bir adam insanların en faziletlisi ancak onlardan biriyse olabilir; Kur'ân'daki Yûsuf'un kardeşlerinin o mânâda onun karşılaştırma sınıfı olamamasının sebebi budur — ama Arapça izâfeti yalnız işaret etmek için de kullanır ve o mutlak mânâda aynı kelimeler ayakta kalır. Uyum mânâyı izler: birincide ihtiyârî, ikincide ve lâm altında vâcib, مِنْ ile yasak. Ameli bâbı kapatır ve defter en uzun pasajını ona ayırır. İsm-i tafdîl beş şartın birleştiği tek dizilim olan Kuhl cümlesi dışında zâhir bir fâili ref' edemeyecek kadar zayıf bir âmildir; defterin sonuncu şarta dair açıklaması dersin kendisidir — nefy karşılaştırmayı ism-i tafdîlden soyup onu düz fiil mânâsında bırakır ve ancak o zaman fâil alabilir; öteki okuma ise ism-i tafdîl ile مِنْهُ'sü arasındaki bağı ikisine de ait olmayan bir kelimeyle koparırdı."},
 "examples": [
  {"ar": "اسْمُ التَّفْضِيلِ: مَا اشْتُقَّ مِنْ فِعْلٍ لِمَوْصُوفٍ بِزِيَادَةٍ عَلَى غَيْرِهِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "هُوَ أَشَدُّ مِنْهُ اسْتِخْرَاجًا، وَأَشَدُّ مِنْهُ بَيَاضًا، وَأَشَدُّ مِنْهُ عَمًى", "en": "The carrier for what cannot take the shape.", "tr": "Biçimi alamayan için taşıyıcı.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "زَيْدٌ أَفْضَلُ النَّاسِ، زَيْدٌ أَفْضَلُ مِنْ بَكْرٍ، زَيْدٌ الْأَفْضَلُ", "en": "The three uses.", "tr": "Üç kullanım.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "يُوسُفُ أَحْسَنُ إِخْوَتِهِ", "en": "Barred in the first sense, permitted in the second.", "tr": "Birinci mânâda yasak, ikincide câiz.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "هِنْدٌ أَفْضَلُ النَّاسِ وَفُضْلَى النِّسَاءِ — هِنْدٌ أَفْضَلُ مِنْ عَمْرٍو", "en": "Agreement optional, then forbidden.", "tr": "Uyum ihtiyârî, sonra yasak.", "sourceStory": "al-kafiya", "sentence": "s10"},
  {"ar": "مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ", "en": "The kohl sentence: the elative raising a doer.", "tr": "Kuhl cümlesi: fâil ref' eden ism-i tafdîl.", "sourceStory": "al-kafiya", "sentence": "s12"}],
 "commonMistakes": [
  {"wrong": "«زَيْدٌ أَحْمَرُ مِنْ عَمْرٍو — daha kırmızı»",
   "right": "«زَيْدٌ أَشَدُّ حُمْرَةً مِنْ عَمْرٍو — renkten ism-i tafdîl kurulmaz»",
   "why": {"en": "أَحْمَر is the plain adjective; the comparison rides on أَشَدُّ with the maṣdar as tamyīz.", "tr": "أَحْمَر düz sıfattır; karşılaştırma masdar temyiz olarak أَشَدُّ üzerinde taşınır."}},
  {"wrong": "«زَيْدٌ الْأَفْضَلُ مِنْ عَمْرٍو»",
   "right": "«زَيْدٌ أَفْضَلُ مِنْ عَمْرٍو veya زَيْدٌ الْأَفْضَلُ — lâm ile مِنْ birleşmez»",
   "why": {"en": "The three uses exclude one another.", "tr": "Üç kullanım birbirini dışlar."}},
  {"wrong": "«هِنْدٌ فُضْلَى مِنْ عَمْرٍو»",
   "right": "«هِنْدٌ أَفْضَلُ مِنْ عَمْرٍو — مِنْ ile ism-i tafdîl hep müfred müzekkerdir»",
   "why": {"en": "With مِنْ the elative never agrees; it behaves like a verb's fixed form.", "tr": "مِنْ ile ism-i tafdîl asla uymaz; fiilin sabit biçimi gibi davranır."}},
  {"wrong": "«يُوسُفُ أَحْسَنُ إِخْوَتِهِ — Yûsuf kardeşlerinden biri olarak en güzeli»",
   "right": "«mutlak mânâda: Yûsuf en güzeldir, izâfet yalnız îzâh içindir»",
   "why": {"en": "In the first sense the described noun must be a member of the muḍāf ilayh; Yūsuf is not one of his own brothers.", "tr": "Birinci mânâda mevsûf muzâfun ileyhin üyesi olmalıdır; Yûsuf kendi kardeşlerinden biri değildir."}}],
 "relatedNotes": [IT, "mamnu-min-sarf", "tamyiz", "al-sifa-al-mushabbaha-fil-kafiya", "amal-ism-al-tafdil-wal-masdar", "idafa-definiteness"]}

ADD_EN = (" Chapter 19 (notebook lines ~273-282): the ism tafḍīl defined in the notebook's own Arabic (s1) and the Kuḥl sentence as it prints it (s12); the shape, the condition, the أَشَدُّ workaround, the three uses, the two senses of annexation, the agreement rules "
          "and the five conditions of government restored from the received matn and marked (s2, s4-s5, s7, s9-s11); خَيْر and شَرّ, the elatives for the object, اللهُ أَكْبَرُ and the notebook's reasons for the negation and the foreign word as commentary (s3, s6, s8, s13).")
ADD_TR = (" On dokuzuncu bâb (defter satırları ~273-282): ism-i tafdîl defterin kendi Arapçasıyla tarif edilir (s1) ve Kuhl cümlesi bastığı gibi verilir (s12); sîga, şart, أَشَدُّ çözümü, üç kullanım, izâfetin iki mânâsı, uyum kuralları ve amelin beş şartı alınan metinden "
          "geri yazılmış ve işaretlenmiştir (s2, s4-s5, s7, s9-s11); خَيْر ve شَرّ, mef'ûl mânâsındaki ism-i tafdîller, اللهُ أَكْبَرُ ve defterin nefy ile ecnebî kelimeye dair gerekçeleri şerh olarak (s3, s6, s8, s13).")
write_out(19, S, TITLE, ADD_EN, ADD_TR, "273-282", GLOSS_ADD, notes=(NOTE,),
          related=((IT, [K]), ("amal-ism-al-tafdil-wal-masdar", [K]), ("mamnu-min-sarf", [K])))
report(19, S, GLOSS_ADD, (NOTE,))
