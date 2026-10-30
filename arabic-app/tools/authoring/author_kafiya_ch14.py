# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 14: THE BROKEN PLURAL. Defined in the notebook's own Arabic; the plural of paucity (three to ten) on four patterns
with the notebook's examples; the plural of multitude (above ten) with the notebook's twenty-two examples, each with its singular; the
end-of-plurals pattern (فَعَالِل، فَعَالِيل); and the notebook's note that Ibn al-Hajib counts the sound plurals among the plurals of paucity.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~229-255 of the transcription.

  VERBATIM from the notebook's Arabic: s1 (the definition) and every pattern and example.
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s2, s3, s4.
  COMMENTARY (the notebook's lists and explanations): s5, s6, s7, s8 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch14.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "jam-al-taksir-fil-kafiya"
JK = "jam-taksir"
TITLE = {"ar": "جَمْعُ التَّكْسِيرِ", "en": "The broken plural", "tr": "Cem-i teksîr"}
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
def pair(pl_full, pl_lex, sg_full, en, tr, first=False, punct=None):
    """«X plural of Y» pairs: the plural cited, then جَمْعُ + singular"""
    p = (cited(pl_full, pl_lex, "noun", [JK], "فِي مَحَلِّ رَفْعٍ خَبَرٌ.", en, tr) if first
         else cited_wa("وَ" + pl_full, pl_lex, "noun", [JK], pl_full + " مَعْطُوفٌ.", "«and» " + en, "«ve» " + tr, pl_full))
    return [p, W("جَمْعُ", "jam", "noun", ["hal", "idafa-definiteness"], "حَالٌ أَوْ بَدَلٌ، وَهُوَ مُضَافٌ.", "— the plural of", "— cem'i:", segments=None),
            cited(sg_full, pl_lex, "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْمُفْرَدُ.", "its singular.", "müfredi.", punct=punct)]

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The broken plural: that in which the build of its singular has changed — as in رِجَالٌ and أَفْرَاسٌ.",
 "tr": "Cem-i teksîr: müfredinin binâsı (sîgası) değişmiş olandır — رِجَالٌ ve أَفْرَاسٌ gibi."},
 "tokens": [
  W("جَمْعُ", "jam", "noun", ["mubtada-khabar", "idafa-definiteness", JK], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the plural of» — the mubtada.", "«cem-i» — mübtedâ."),
  W("التَّكْسِيرِ", "taksir", "noun", ["idafa-definiteness", JK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«breaking».", "«teksîr».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«that» — the khabar.", "«... olan» — haber."),
  W("تَغَيَّرَ", "taghayyara", "verb", ["ism-mawsul", "fail", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«has changed».", "«değişmiş»."),
  W("بِنَاءُ", "bina", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — أَيْ: صِيغَتُهُ.", "«the build of» — the doer: its shape.", "«binâsı» — fâil: sîgası."),
  W("وَاحِدِهِ", "wahid", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«its singular» — the hāʾ the ʿāʾid.", "«müfredinin» — hâ âid.", punct="،", segments=[seg("وَاحِدِ", "wahid", "noun"), pr3msi()]),
  nahwu(),
  cited("رِجَالٌ", "rajul", "noun", ["idafa-definiteness", JK], "فِي مَحَلِّ جَرٍّ — جَمْعُ رَجُلٍ.", "«men» — the plural of رَجُل.", "«adamlar» — racül'ün cem'i."),
  cited_wa("وَأَفْرَاسٌ", "faras", "noun", [JK], "أَفْرَاسٌ مَعْطُوفٌ — جَمْعُ فَرَسٍ.", "«and horses» — the plural of فَرَس.", "«ve atlar» — feres'in cem'i.", "أَفْرَاسٌ", punct="."),
 ]})

# ----------- s2 (RESTORED): the plural of paucity
S.append({"id": "s2", "translation": {
 "en": "And the plural of paucity is what is said of three to ten, and it has four patterns: أَفْعُلٌ، أَفْعَالٌ، أَفْعِلَةٌ and فِعْلَةٌ." + R_EN,
 "tr": "Cem-i kıllet üçten ona kadar olan fertlere ıtlak olunandır ve dört vezni vardır: أَفْعُلٌ، أَفْعَالٌ، أَفْعِلَةٌ ve فِعْلَةٌ." + R_TR},
 "tokens": [
  atf_wa("وَجَمْعُ", "jam", "noun", ["mubtada-khabar", "idafa-definiteness", JK], "جَمْعُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the plural of» — the mubtada.", "«ve cem-i» — mübtedâ.", "جَمْعُ"),
  W("الْقِلَّةِ", "qilla", "noun", ["idafa-definiteness", JK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«paucity».", "«kıllet»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("يُطْلَقُ", "atlaqa", "verb", ["ism-mawsul", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«is said».", "«ıtlak olunan»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-e»."),
  W("الثَّلَاثَةِ", "thalatha", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«three».", "«üç»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e kadar»."),
  W("الْعَشَرَةِ", "ashara", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«ten».", "«on».", punct="،"),
  atf_wa("وَلَهُ", "li", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ؛ خَبَرٌ مُقَدَّمٌ.", "«and it has».", "«ve onun ... vardır».", "لَ", extra_segs=[seg("لَ", "li", "prep"), pr3ms()]),
  W("أَرْبَعَةُ", "arbaa", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«four».", "«dört»."),
  W("أَوْزَانٍ", "wazn", "noun", ["idafa-definiteness", "tamyiz", JK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعٌ مَجْرُورٌ بَعْدَ الْأَرْبَعَةِ.", "«patterns» — a plural in jarr after four.", "«vezin» — dörtten sonra cemi mecrûr.", punct=":"),
  cited("أَفْعُلٌ", "afulun-wazn", "noun", ["badal", JK], "بَدَلٌ مِنْ أَرْبَعَةُ — كَأَفْلُسٍ.", "«afʿul» — as أَفْلُس from فُلْس.", "«ef'ul» — fülsün cem'i eflüs gibi."),
  cited_wa("وَأَفْعَالٌ", "afal-pl-wazn", "noun", [JK], "أَفْعَالٌ مَعْطُوفٌ — كَأَفْرَاسٍ.", "«and afʿāl» — as أَفْرَاس from فَرَس.", "«ve ef'âl» — feres'in cem'i efrâs gibi.", "أَفْعَالٌ"),
  cited_wa("وَأَفْعِلَةٌ", "afila-wazn", "noun", [JK], "أَفْعِلَةٌ مَعْطُوفٌ — كَأَرْغِفَةٍ.", "«and afʿila» — as أَرْغِفَة from رَغِيف.", "«ve ef'ile» — rağîf'in cem'i erğife gibi.", "أَفْعِلَةٌ"),
  cited_wa("وَفِعْلَةٌ", "fila-wazn", "noun", [JK], "فِعْلَةٌ مَعْطُوفٌ — كَغِلْمَةٍ.", "«and fiʿla» — as غِلْمَة from غُلَام.", "«ve fi'le» — gulâm'ın cem'i gılme gibi.", "فِعْلَةٌ", punct="."),
 ]})

# ----------- s3 (RESTORED): the plural of multitude
S.append({"id": "s3", "translation": {
 "en": "And what is other than these is a plural of multitude, said of what is above ten." + R_EN,
 "tr": "Bunların dışındakiler cem-i kesrettir; ondan yukarı olan fertlere ıtlak olunur." + R_TR},
 "tokens": [
  atf_wa("وَمَا", "ma-mawsula", "pron", ["mubtada-khabar", "ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and what» — the mubtada.", "«ve ... olan» — mübtedâ.", "مَا"),
  W("سِوَاهَا", "siwa", "noun", ["ism-mawsul", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is other than these».", "«bunların dışında olan».", segments=[seg("سِوَا", "siwa", "noun"), pr3fs()]),
  W("جَمْعُ", "jam", "noun", ["mubtada-khabar", "idafa-definiteness", JK], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is a plural of» — the khabar.", "«cem-i ... -dir» — haber."),
  W("كَثْرَةٍ", "kathra", "noun", ["idafa-definiteness", JK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«multitude».", "«kesret».", punct="،"),
  W("يُطْلَقُ", "atlaqa", "verb", ["naib-al-fail", "naat-sifa"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِفَةٌ.", "«said».", "«ıtlak olunur»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-e»."),
  W("مَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what».", "«... olan»."),
  W("فَوْقَ", "fawqa", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةُ مَا.", "«is above».", "«yukarı»."),
  W("الْعَشَرَةِ", "ashara", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ten».", "«ondan».", punct="."),
 ]})

# ----------- s4 (RESTORED): the end-of-plurals pattern
S.append({"id": "s4", "translation": {
 "en": "And of it is the pattern of the utmost of plurals, فَعَالِلُ and فَعَالِيلُ — as in عَوَامِلُ, the plural of عَامِل, and مَصَابِيحُ, the plural of مِصْبَاح." + R_EN,
 "tr": "Ondan biri de müntehe'l-cumû' sîgasıdır, فَعَالِلُ ve فَعَالِيلُ — عَامِل'in cem'i عَوَامِلُ ve مِصْبَاح'ın cem'i مَصَابِيحُ gibi." + R_TR},
 "tokens": [
  atf_wa("وَمِنْهُ", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ؛ خَبَرٌ مُقَدَّمٌ.", "«and of it is».", "«ve ondan biri».", "مِنْ", extra_segs=[seg("مِنْ", "min", "prep"), pr3ms()]),
  W("صِيغَةُ", "sigha", "noun", ["mubtada-khabar", "idafa-definiteness", JK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the pattern of».", "«sîgası»."),
  W("مُنْتَهَى", "muntaha", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the utmost of».", "«müntehâ»."),
  W("الْجُمُوعِ", "jumu", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ جَمْعٍ.", "«plurals».", "«cumû'».", punct="،"),
  cited("فَعَالِلُ", "faalil-wazn", "noun", ["badal", JK, "mamnu-min-sarf"], "بَدَلٌ مِنْ صِيغَةُ مَرْفُوعٌ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«faʿālil».", "«fe'âlil»."),
  cited_wa("وَفَعَالِيلُ", "faalil-wazn", "noun", [JK, "mamnu-min-sarf"], "فَعَالِيلُ مَعْطُوفٌ.", "«and faʿālīl».", "«ve fe'âlîl».", "فَعَالِيلُ", punct="،"),
  nahwu(),
  cited("عَوَامِلُ", "amil", "noun", ["idafa-definiteness", JK, "mamnu-min-sarf"], "فِي مَحَلِّ جَرٍّ — جَمْعُ عَامِلٍ، أُعِلَّتْ أَلِفُهُ وَاوًا.", "«governors» — the plural of عَامِل.", "«âmiller» — âmil'in cem'i."),
  W("جَمْعُ", "jam", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ، وَهُوَ مُضَافٌ.", "— the plural of", "— cem'i:"),
  cited("عَامِلٍ", "amil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "عَامِل.", "âmil.", punct="،"),
  cited_wa("وَمَصَابِيحُ", "misbah", "noun", [JK, "mamnu-min-sarf"], "مَصَابِيحُ مَعْطُوفٌ — جَمْعُ مِصْبَاحٍ.", "«and lamps» — the plural of مِصْبَاح.", "«ve kandiller» — misbâh'ın cem'i.", "مَصَابِيحُ"),
  W("جَمْعُ", "jam", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ، وَهُوَ مُضَافٌ.", "— the plural of", "— cem'i:"),
  cited("مِصْبَاحٍ", "misbah", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "مِصْبَاح.", "misbâh.", punct="."),
 ]})

# ----------- s5 (COMMENTARY): the notebook's list, first third
S.append({"id": "s5", "translation": {
 "en": "And its examples: حُمْرٌ the plural of أَحْمَر, غُفْرَانٌ of غَفِير, غِلْمَانٌ of غُلَام, جَرْحَى of جَرِيح, فِرَقٌ of فِرْقَة, صُوَّامٌ of صَائِم, أَوْلِيَاءُ of وَلِيّ." + C_EN,
 "tr": "Örnekleri: أَحْمَر'in cem'i حُمْرٌ, غَفِير'in غُفْرَانٌ, غُلَام'ın غِلْمَانٌ, جَرِيح'in جَرْحَى, فِرْقَة'nin فِرَقٌ, صَائِم'in صُوَّامٌ, وَلِيّ'nin أَوْلِيَاءُ." + C_TR},
 "tokens": [
  atf_wa("وَأَمْثِلَتُهُ", "mithal", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "أَمْثِلَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its examples» — the mubtada.", "«ve örnekleri» — mübtedâ.", "أَمْثِلَتُ", extra_segs=[seg("أَمْثِلَتُ", "mithal", "noun"), pr3ms()], punct=":"),
  *pair("حُمْرٌ", "ahmar", "أَحْمَرَ", "«red ones»", "«kırmızılar»", first=True, punct="،"),
  *pair("غُفْرَانٌ", "ghafir", "غَفِيرٍ", "«many»", "«çok kişiler»", punct="،"),
  *pair("غِلْمَانٌ", "ghulam", "غُلَامٍ", "«boys»", "«oğlanlar»", punct="،"),
  *pair("جَرْحَى", "jarih", "جَرِيحٍ", "«wounded ones»", "«yaralılar»", punct="،"),
  *pair("فِرَقٌ", "furqa", "فِرْقَةٍ", "«groups»", "«fırkalar»", punct="،"),
  *pair("صُوَّامٌ", "saim", "صَائِمٍ", "«fasters»", "«oruçlular»", punct="،"),
  *pair("أَوْلِيَاءُ", "wali", "وَلِيٍّ", "«friends of God»", "«velîler»", punct="."),
 ]})

# ----------- s6 (COMMENTARY): second third
S.append({"id": "s6", "translation": {
 "en": "And حُيَّضٌ the plural of حَائِض, رِجَالٌ of رَجُل, غُرَفٌ of غُرْفَة, نَصَرَةٌ of نَاصِر, قُضَاةٌ of قَاضِيَة, قِرَطَةٌ of قُرْط, يَتَامَى of يَتِيم, عَبِيدٌ of عَبْد." + C_EN,
 "tr": "Ve حَائِض'in cem'i حُيَّضٌ, رَجُل'ün رِجَالٌ, غُرْفَة'nin غُرَفٌ, نَاصِر'in نَصَرَةٌ, قَاضِيَة'nin قُضَاةٌ, قُرْط'un قِرَطَةٌ, يَتِيم'in يَتَامَى, عَبْد'in عَبِيدٌ." + C_TR},
 "tokens": [
  *pair("حُيَّضٌ", "haid", "حَائِضٍ", "«menstruating women»", "«hayızlılar»", punct="،"),
  *pair("رِجَالٌ", "rajul", "رَجُلٍ", "«men»", "«adamlar»", punct="،"),
  *pair("غُرَفٌ", "ghurfa", "غُرْفَةٍ", "«rooms»", "«odalar»", punct="،"),
  *pair("نَصَرَةٌ", "nasir-helper", "نَاصِرٍ", "«helpers»", "«yardımcılar»", punct="،"),
  *pair("قُضَاةٌ", "qadiya", "قَاضِيَةٍ", "«judges»", "«kadılar»", punct="،"),
  *pair("قِرَطَةٌ", "qurt", "قُرْطٍ", "«earrings»", "«küpeler»", punct="،"),
  *pair("يَتَامَى", "yatim", "يَتِيمٍ", "«orphans»", "«yetimler»", punct="،"),
  *pair("عَبِيدٌ", "abd", "عَبْدٍ", "«slaves»", "«kullar»", punct="."),
 ]})
S[5]["tokens"][0] = cited("وَحُيَّضٌ", "haid", "noun", [JK, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَحُيَّضٌ مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "«and menstruating women»", "«ve hayızlılar»", segments=[seg("وَ", "wa", "conj"), seg("حُيَّضٌ", "haid", "noun")])

# ----------- s7 (COMMENTARY): last third
S.append({"id": "s7", "translation": {
 "en": "And وُجُوهٌ the plural of وَجْه, ظُرَفَاءُ of ظَرِيف, أُسَارَى of أَسِير, ظِرْبَى of ظِرْبَان, أُسْدٌ of أَسَد, and مَشْيُوخَاءُ of شَيْخ." + C_EN,
 "tr": "Ve وَجْه'in cem'i وُجُوهٌ, ظَرِيف'in ظُرَفَاءُ, أَسِير'in أُسَارَى, ظِرْبَان'ın ظِرْبَى, أَسَد'in أُسْدٌ, شَيْخ'in مَشْيُوخَاءُ." + C_TR},
 "tokens": [
  *pair("وُجُوهٌ", "wajh", "وَجْهٍ", "«faces»", "«yüzler»", punct="،"),
  *pair("ظُرَفَاءُ", "zarif", "ظَرِيفٍ", "«witty ones»", "«zarifler»", punct="،"),
  *pair("أُسَارَى", "asir", "أَسِيرٍ", "«captives»", "«esirler»", punct="،"),
  *pair("ظِرْبَى", "zirban", "ظِرْبَانٍ", "«polecats»", "«kokarcalar»", punct="،"),
  *pair("أُسْدٌ", "asad", "أَسَدٍ", "«lions»", "«aslanlar»", punct="،"),
  *pair("مَشْيُوخَاءُ", "shaykh", "شَيْخٍ", "«elders»", "«şeyhler»", punct="."),
 ]})
S[6]["tokens"][0] = cited("وَوُجُوهٌ", "wajh", "noun", [JK, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَوُجُوهٌ مَعْطُوفٌ.", "«and faces»", "«ve yüzler»", segments=[seg("وَ", "wa", "conj"), seg("وُجُوهٌ", "wajh", "noun")])

# ----------- s8 (COMMENTARY): the sound plurals and paucity
S.append({"id": "s8", "translation": {
 "en": "And Ibn al-Ḥājib counted the two sound plurals among the plurals of paucity, while some scholars hold them to be plurals absolutely, bound neither to paucity nor to multitude." + C_EN,
 "tr": "İbnü'l-Hâcib iki sâlim cemiyi cem-i kıllet'ten saymıştır; bazı âlimlere göre ise onlar kıllet ve kesretle kayıtlanmaksızın mutlak cemidir." + C_TR},
 "tokens": [
  atf_wa("وَعَدَّ", "adda-count", "verb", ["fail", "doubled-verbs"], "عَدَّ فِعْلٌ مَاضٍ.", "«and counted».", "«ve saydı».", "عَدَّ"),
  W("ابْنُ", "ibn", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«Ibn».", "«İbn»."),
  W("الْحَاجِبِ", "hajib", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مُصَنِّفُ الْكَافِيَةِ.", "«al-Ḥājib» — the Kafiya's author.", "«el-Hâcib» — Kâfiye'nin müellifi."),
  W("الْجَمْعَيْنِ", "jam", "noun", ["maful-bihi", "al-muthanna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«the two plurals».", "«iki cemiyi»."),
  W("السَّالِمَيْنِ", "salim", "noun", ["naat-sifa", "al-muthanna"], "صِفَةٌ مَنْصُوبَةٌ بِالْيَاءِ.", "«sound».", "«sâlim»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«among».", "«-den»."),
  W("جُمُوعِ", "jumu", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the plurals of».", "«cemileri»."),
  W("الْقِلَّةِ", "qilla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«paucity».", "«kıllet».", punct="،"),
  atf_wa("وَبَعْضُ", "bad", "noun", ["mubtada-khabar", "idafa-definiteness"], "بَعْضُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«while some of».", "«bazı».", "بَعْضُ"),
  W("الْعُلَمَاءِ", "alim-scholar", "noun", ["idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِأَجْلِ ال.", "«the scholars».", "«âlimler»."),
  W("يَجْعَلُهُمَا", "jaala", "verb", ["mubtada-khabar", "mafulayn"], "فِعْلٌ مُضَارِعٌ، وَهُمَا مَفْعُولٌ أَوَّلُ، وَالْجُمْلَةُ خَبَرٌ.", "«hold them to be».", "«onları ... sayar».", segments=[seg("يَجْعَلُ", "jaala", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  W("جَمْعًا", "jam", "noun", ["mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a plural».", "«cemi»."),
  W("مُطْلَقًا", "mutlaqan", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«absolutely».", "«mutlak».", punct="،"),
  W("غَيْرَ", "ghayr", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«not».", "«-maksızın»."),
  W("مُقَيَّدٍ", "muqayyad", "noun", ["idafa-definiteness", "ism-maful", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«bound».", "«kayıtlı»."),
  W("بِالْقِلَّةِ", "qilla", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْقِلَّةِ مَجْرُورٌ.", "«to paucity».", "«kılletle».", segments=[seg("بِ", "bi", "prep"), seg("الْقِلَّةِ", "qilla", "noun")]),
  atf_wa("وَالْكَثْرَةِ", "kathra", "noun", [], "الْكَثْرَةِ مَعْطُوفٌ مَجْرُورٌ.", "«nor multitude».", "«ve kesretle».", "الْكَثْرَةِ", punct="."),
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
 "afulun-wazn": need("afulun-wazn", "أَفْعُل", None, "noun", "the pattern أَفْعُلٌ — a plural of paucity (فُلْس → أَفْلُس)", "ef'ul vezni — cem-i kıllet (füls → eflüs)", 4),
 "afal-pl-wazn": need("afal-pl-wazn", "أَفْعَال", None, "noun", "the pattern أَفْعَالٌ — a plural of paucity (فَرَس → أَفْرَاس)", "ef'âl vezni — cem-i kıllet (feres → efrâs)", 3),
 "afila-wazn": need("afila-wazn", "أَفْعِلَة", None, "noun", "the pattern أَفْعِلَةٌ — a plural of paucity (رَغِيف → أَرْغِفَة)", "ef'ile vezni — cem-i kıllet (rağîf → erğife)", 4),
 "fila-wazn": need("fila-wazn", "فِعْلَة", None, "noun", "the pattern فِعْلَةٌ — a plural of paucity (غُلَام → غِلْمَة)", "fi'le vezni — cem-i kıllet (gulâm → gılme)", 4),
 "faalil-wazn": need("faalil-wazn", "فَعَالِل", None, "noun", "the pattern فَعَالِلُ (and فَعَالِيلُ) — the utmost of plurals, a diptote (عَوَامِل، مَصَابِيح)", "fe'âlil vezni (ve fe'âlîl) — müntehe'l-cumû', gayr-i munsarif (avâmil, mesâbîh)", 4),
 "ghafir": need("ghafir", "غَفِير", "غ ف ر", "noun", "many, a throng (الْجَمُّ الْغَفِيرُ); plural غُفْرَان", "kalabalık, çok (el-cemmü'l-gafîr); cem'i gufrân", 5),
 "qadiya": need("qadiya", "قَاضِيَة", "ق ض ي", "noun", "a female judge; the notebook gives قُضَاة as its plural", "kadın kadı; defter cem'ini kudât verir", 5),
 "qurt": need("qurt", "قُرْط", "ق ر ط", "noun", "an earring; plural قِرَطَة", "küpe; cem'i kırata", 4),
 "asir": need("asir", "أَسِير", "أ س ر", "noun", "a captive; plural أُسَارَى", "esir; cem'i üsârâ", 2),
 "zirban": need("zirban", "ظِرْبَان", "ظ ر ب", "noun", "a polecat; plural ظِرْبَى", "kokarca; cem'i zırbâ", 6),
 "hajib": need("hajib", "الْحَاجِب", "ح ج ب", "propn", "Ibn al-Ḥājib (d. 646/1249), the author of the Kāfiya and the Shāfiya", "İbnü'l-Hâcib (ö. 646/1249), Kâfiye ve Şâfiye'nin müellifi", 4),
 "muqayyad": need("muqayyad", "مُقَيَّد", "ق ي د", "noun", "bound, restricted (ism maf'ul of Form II قَيَّدَ)", "mukayyed, kayıtlı (kayyede'nin ism-i mef'ûlü)", 4),
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
print("kafiya ch14 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "جَمْعُ التَّكْسِيرِ فِي الْكَافِيَةِ", "en": "The broken plural in the Kafiya: paucity (four patterns) against multitude, the utmost-of-plurals pattern, and the notebook's twenty-two examples", "tr": "Kâfiye'de cem-i teksîr: kıllet (dört vezin) ile kesret, müntehe'l-cumû' sîgası ve defterin yirmi iki örneği"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — جمع التكسير: ما تغير بناء واحده؛ جمع القلة أفعل وأفعال وأفعلة وفعلة؛ وما سواها جمع كثرة؛ صيغة منتهى الجموع", "ضياء صونغور اوغلى — دفتر الكافية: التعريف بلفظه، أربعة أوزان القلة بأمثلتها، اثنان وعشرون مثالا للكثرة بمفرداتها، عد ابن الحاجب الجمعين السالمين من القلة"],
 "question": {
  "en": ["What is a BROKEN plural? One whose singular's build has changed — by adding, dropping or re-vowelling — as رِجَال from رَجُل and أَفْرَاس from فَرَس; the sound plurals leave the singular whole and only add an ending.",
         "Which plurals say «a few»? The plural of PAUCITY, for three to ten, on four patterns: أَفْعُل (أَفْلُس), أَفْعَال (أَفْرَاس), أَفْعِلَة (أَرْغِفَة), فِعْلَة (غِلْمَة). Every other broken pattern is a plural of MULTITUDE, for more than ten.",
         "What is the utmost of plurals? فَعَالِل and فَعَالِيل (عَوَامِل، مَصَابِيح) — a plural that cannot itself be pluralised again, and a diptote for that very reason.",
         "How does the notebook teach the multitude patterns? Not by their names but by twenty-two pairs, each plural beside its singular: حُمْر / أَحْمَر، غِلْمَان / غُلَام، جَرْحَى / جَرِيح، فِرَق / فِرْقَة، صُوَّام / صَائِم، أَوْلِيَاء / وَلِيّ، حُيَّض / حَائِض، رِجَال / رَجُل، غُرَف / غُرْفَة، نَصَرَة / نَاصِر، قُضَاة / قَاضِيَة، قِرَطَة / قُرْط، يَتَامَى / يَتِيم، عَبِيد / عَبْد، وُجُوه / وَجْه، ظُرَفَاء / ظَرِيف، أُسَارَى / أَسِير، ظِرْبَى / ظِرْبَان، أُسْد / أَسَد، مَشْيُوخَاء / شَيْخ.",
         "Are the sound plurals plurals of paucity? Ibn al-Ḥājib counts them so; the notebook records the other view, that -ūna and -āt are plurals absolutely, bound to neither number.",
         "What does the engine do? The IsmTagger reads a broken plural back to its wazn (رِجَال → فِعَال) and the glossary stores the plural a human checked; the AlamaEngine knows the utmost-of-plurals pattern as a diptote and reads its tanwīn on a manqūṣ (مَعَانٍ) as the tanwīn of compensation."],
  "tr": ["MÜKESSER cemi nedir? Müfredinin binâsı değişmiş olan — ekleyerek, atarak ya da harekesini değiştirerek — رَجُل'den رِجَال, فَرَس'ten أَفْرَاس gibi; sâlim cemiler müfredi bütün bırakıp yalnız ek getirir.",
         "Hangi cemiler «birkaç» der? Üçten ona KILLET cemi, dört vezinde: أَفْعُل (أَفْلُس), أَفْعَال (أَفْرَاس), أَفْعِلَة (أَرْغِفَة), فِعْلَة (غِلْمَة). Diğer her mükesser vezin KESRET cemidir, ondan fazlası için.",
         "Müntehe'l-cumû' nedir? فَعَالِل ve فَعَالِيل (عَوَامِل، مَصَابِيح) — tekrar cemi'lenemeyen cemi; tam bu yüzden gayr-i munsarif.",
         "Defter kesret vezinlerini nasıl öğretir? Adlarıyla değil, her cemi müfredinin yanında yirmi iki çiftle: حُمْر / أَحْمَر، غِلْمَان / غُلَام، جَرْحَى / جَرِيح، فِرَق / فِرْقَة، صُوَّام / صَائِم، أَوْلِيَاء / وَلِيّ، حُيَّض / حَائِض، رِجَال / رَجُل، غُرَف / غُرْفَة، نَصَرَة / نَاصِر، قُضَاة / قَاضِيَة، قِرَطَة / قُرْط، يَتَامَى / يَتِيم، عَبِيد / عَبْد، وُجُوه / وَجْه، ظُرَفَاء / ظَرِيف، أُسَارَى / أَسِير، ظِرْبَى / ظِرْبَان، أُسْد / أَسَد، مَشْيُوخَاء / شَيْخ.",
         "Sâlim cemiler kıllet cemisi midir? İbnü'l-Hâcib öyle sayar; defter öteki görüşü de kaydeder: -ûne ve -ât mutlak cemidir, iki sayıya da bağlı değildir.",
         "Motor ne yapar? IsmTagger mükesser cemiyi veznine geri okur (رِجَال → فِعَال), sözlük bir insanın denetlediği cemiyi saklar; AlamaEngine müntehe'l-cumû' sîgasını gayr-i munsarif bilir ve mankûs üzerindeki tenvinini (مَعَانٍ) ivaz tenvini olarak okur."]},
 "plain": {
  "en": "A broken plural reshapes the word itself (رَجُل → رِجَال). Four shapes mean «three to ten» (أَفْعُل، أَفْعَال، أَفْعِلَة، فِعْلَة); all the other shapes mean «many». The heaviest shape, فَعَالِل/فَعَالِيل, is the end of the line — it cannot be pluralised again and takes no tanwīn.",
  "tr": "Mükesser cemi kelimenin kendisini yeniden biçimlendirir (رَجُل → رِجَال). Dört biçim «üçten ona» demektir (أَفْعُل، أَفْعَال، أَفْعِلَة، فِعْلَة); diğer bütün biçimler «çok» demektir. En ağır biçim, فَعَالِل/فَعَالِيل, yolun sonudur — tekrar cemi'lenemez ve tenvin almaz."},
 "explanation": {
  "en": "Where the sound plurals add an ending and leave the word alone, the broken plural reaches inside the word: the Kafiya's definition says only that the singular's build has changed, and the notebook's one-line examples show the three ways it can — رِجَال adds a letter, كُتُب drops one, أُسْد re-vowels. The chapter then draws the one line Arabic draws through its plurals that European grammars do not: some shapes mean a few and some mean many. Four patterns are reserved for three to ten — the two with the hamza of أَفْعُل and أَفْعَال, the أَفْعِلَة of the long-vowelled singulars, and فِعْلَة — and everything else is multitude. The notebook does not recite the twenty-two multitude patterns by name; it hands the student twenty-two words with their singulars, which is the way the patterns are actually learned, and the chapter keeps them as the notebook gives them. Two notes close it. The utmost of plurals, فَعَالِل and فَعَالِيل, is the ceiling: a form already so heavy that it cannot be pluralised again, and that heaviness is why it is barred from the tanwīn — the AlamaEngine's row for مَعَانٍ is this rule met on a manqūṣ. And Ibn al-Ḥājib's own placing of the sound plurals among the plurals of paucity is recorded with the dissent, since a learner who meets مُسْلِمُونَ for a thousand men needs to know that the ending was never a count.",
  "tr": "Sâlim cemiler ek getirip kelimeyi rahat bırakırken mükesser cemi kelimenin içine girer: Kâfiye'nin tarifi yalnız müfredin binâsının değiştiğini söyler, defterin tek satırlık örnekleri bunun üç yolunu gösterir — رِجَال harf ekler, كُتُب atar, أُسْد harekeyi değiştirir. Bâb sonra Arapçanın cemileri arasına Avrupa gramerlerinin çizmediği tek çizgiyi çeker: bazı biçimler az, bazıları çok demektir. Dört vezin üçten ona ayrılmıştır — أَفْعُل ve أَفْعَال'in hemzelileri, uzun ünlülü müfredlerin أَفْعِلَة'si ve فِعْلَة — gerisi kesrettir. Defter yirmi iki kesret veznini adıyla saymaz; öğrenciye müfredleriyle yirmi iki kelime verir ki vezinler gerçekte böyle öğrenilir ve bâb onları defterin verdiği gibi tutar. İki not kapatır. Müntehe'l-cumû', فَعَالِل ve فَعَالِيل, tavandır: tekrar cemi'lenemeyecek kadar ağır bir biçim; bu ağırlık tenvinden men edilmesinin sebebidir — AlamaEngine'in مَعَانٍ satırı bu kuralın mankûsla karşılaşmasıdır. İbnü'l-Hâcib'in sâlim cemileri kıllet cemilerine koyması muhâlif görüşle birlikte kaydedilir; çünkü bin adam için مُسْلِمُونَ ile karşılaşan öğrenci, ekin hiçbir zaman bir sayı olmadığını bilmelidir."},
 "examples": [
  {"ar": "جَمْعُ التَّكْسِيرِ: مَا تَغَيَّرَ بِنَاءُ وَاحِدِهِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "أَفْعُلٌ، أَفْعَالٌ، أَفْعِلَةٌ، فِعْلَةٌ", "en": "The four patterns of paucity.", "tr": "Dört kıllet vezni.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "عَوَامِلُ جَمْعُ عَامِلٍ، وَمَصَابِيحُ جَمْعُ مِصْبَاحٍ", "en": "The utmost of plurals.", "tr": "Müntehe'l-cumû'.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "حُمْرٌ جَمْعُ أَحْمَرَ … أَوْلِيَاءُ جَمْعُ وَلِيٍّ", "en": "The notebook's examples, first group.", "tr": "Defterin örnekleri, birinci grup.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "وُجُوهٌ جَمْعُ وَجْهٍ … مَشْيُوخَاءُ جَمْعُ شَيْخٍ", "en": "The notebook's examples, last group.", "tr": "Defterin örnekleri, son grup.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "عَدَّ ابْنُ الْحَاجِبِ الْجَمْعَيْنِ السَّالِمَيْنِ مِنْ جُمُوعِ الْقِلَّةِ", "en": "The sound plurals and paucity.", "tr": "Sâlim cemiler ve kıllet.", "sourceStory": "al-kafiya", "sentence": "s8"}],
 "commonMistakes": [
  {"wrong": "«رِجَالٌ üçten ona kadar adam demektir»",
   "right": "«رِجَالٌ (فِعَال) kesret cemidir; kıllet için أَرْجُلٌ yoktur, kıllet vezinleri dörttür»",
   "why": {"en": "Only the four named patterns carry the sense of paucity; فِعَال is a pattern of multitude.", "tr": "Yalnız dört adlı vezin kıllet manası taşır; فِعَال kesret veznidir."}},
  {"wrong": "«مَصَابِيحٌ — tenvinli»",
   "right": "«مَصَابِيحُ — müntehe'l-cumû' sîgası gayr-i munsariftir»",
   "why": {"en": "The utmost-of-plurals pattern is barred from the tanwīn by the heaviness of its form alone.", "tr": "Müntehe'l-cumû' sîgası yalnız biçiminin ağırlığıyla tenvinden men edilmiştir."}},
  {"wrong": "«مَعَانٍ tenvinlidir, demek ki munsariftir»",
   "right": "«مَعَانٍ müntehe'l-cumû'dür; tenvini ivaz tenvinidir, düşen yânın karşılığı — nasbda مَعَانِيَ»",
   "why": {"en": "A manqūṣ on this pattern drops its yāʾ in rafʿ and jarr and takes a tanwīn of compensation, not of declension.", "tr": "Bu vezindeki mankûs ref' ve cerde yâsını düşürür ve i'râb değil ivaz tenvini alır."}},
  {"wrong": "«مُسْلِمُونَ on kişiden az Müslüman demektir»",
   "right": "«مُسْلِمُونَ her sayıyı karşılar; İbnü'l-Hâcib'in onu kıllet'ten sayması bir taksimdir, bir sınır değil»",
   "why": {"en": "The notebook records both views; usage uses the sound plural for any number.", "tr": "Defter iki görüşü de kaydeder; kullanım sâlim cemiyi her sayı için kullanır."}}],
 "relatedNotes": [JK, "jam-mudhakkar-salim", "jam-muannath-salim", "mamnu-min-sarf", "ism-maqsur-manqus", "al-jam-al-salim-fil-kafiya"]}

ADD_EN = (" Chapter 14 (notebook lines ~229-255): the broken plural defined in the notebook's own Arabic (s1) with every pattern and example it lists; the plural of paucity, "
          "the plural of multitude and the utmost-of-plurals pattern restored from the received matn and marked (s2-s4); the notebook's twenty-two examples with their singulars "
          "(s5-s7) and its note on Ibn al-Hajib's placing of the sound plurals (s8) as commentary.")
ADD_TR = (" On dördüncü bâb (defter satırları ~229-255): cem-i teksîr defterin kendi Arapçasıyla tarif edilir (s1), saydığı her vezin ve örnekle; cem-i kıllet, cem-i kesret ve "
          "müntehe'l-cumû' sîgası alınan metinden geri yazılmış ve işaretlenmiştir (s2-s4); defterin müfredleriyle yirmi iki örneği (s5-s7) ve İbnü'l-Hâcib'in sâlim cemileri "
          "yerleştirişi hakkındaki notu (s8) şerh olarak.")
write_out(14, S, TITLE, ADD_EN, ADD_TR, "229-255", GLOSS_ADD, notes=(NOTE,),
          related=((JK, [K]), ("mamnu-min-sarf", [K]), ("al-jam-al-salim-fil-kafiya", [K])))
report(14, S, GLOSS_ADD, (NOTE,))
