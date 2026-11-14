# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 29: the negations — what the Originator is not. Source: matn line 31 (ولا مصور … ولا يجري عليه زمان);
the names before it and لَيْسَ بِعَرَضٍ وَلَا جِسْمٍ وَلَا جَوْهَرٍ are chapter 5, whose list s1 of this chapter continues (the matn's own
list, the two epithets الشَّائِي الْمُرِيدُ at its head left to the sharḥ).  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch29.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "مَا يُنْفَى عَنِ اللهِ تَعَالَى", "en": "What Is Denied of God", "tr": "Allah'tan Nefyedilenler"}
S = []
def NEG(full, lex, en, tr, tags=(), punct=None, extra=""):
    return W(full, lex, "noun", ["atf-nasaq"] + list(tags), "مَعْطُوفٌ عَلَى «عَرَضٍ» فِي قَوْلِهِ: لَيْسَ بِعَرَضٍ (الْبَابُ الْخَامِسُ) تَابِعٌ لَهُ فِي الْجَرِّ، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + extra + ".", en, tr, punct=punct)
S.append({"id": "s1", "translation": {
 "en": "— nor is He formed, nor bounded, nor numbered, nor made of portions, nor of parts, nor finite.",
 "tr": "— ne sûret verilmiştir, ne sınırlıdır, ne sayılıdır, ne parçalardan ne cüzlerden mürekkeptir, ne de sonludur."},
 "tokens": [
  WALA("«nor» — the list continues chapter 5's لَيْسَ بِعَرَضٍ وَلَا جِسْمٍ وَلَا جَوْهَرٍ.", "«ne de» — liste, beşinci bâbın لَيْسَ بِعَرَضٍ وَلَا جِسْمٍ وَلَا جَوْهَرٍ'ini sürdürür."),
  NEG("مُصَوَّرٍ", "musawwar", "«formed» — given a form; the ism mafʿūl of Form II.", "«sûret verilmiş» — tef'îl ism-i mef'ûlü.", tags=["ism-maful", "form-ii-verbs"], punct="،"),
  WALA(), NEG("مَحْدُودٍ", "mahdud", "«bounded».", "«sınırlı».", tags=["ism-maful"], punct="،"),
  WALA(), NEG("مَعْدُودٍ", "madud", "«numbered».", "«sayılı».", tags=["ism-maful"], punct="،"),
  WALA(), NEG("مُتَبَعِّضٍ", "mutabaid", "«made of portions» — the ism fāʿil of Form V from بَعْض.", "«parçalardan mürekkep» — بَعْض'ten tefe'ul ism-i fâili.", tags=["ism-fail", "form-v-verbs"], punct="،"),
  WALA(), NEG("مُتَجَزِّئٍ", "mutajazzi", "«made of parts» — from جُزْء; the hamza sits on the yāʾ-seat after a kasra.", "«cüzlerden mürekkep» — جُزْء'den; hemze kesreden sonra yâ kürsüsünde oturur.", tags=["ism-fail", "form-v-verbs"], punct="،"),
  WALA(), NEG("مُتَنَاهٍ", "mutanahi", "«finite» — an indefinite manqūṣ: the yāʾ falls and the tanwīn stands in for it; the kasra is estimated.", "«sonlu» — nekre mankûs: yâ düşer, tenvin onun yerine durur; kesre takdirîdir.", tags=["ism-fail", "form-vi-verbs", "ism-maqsur-manqus"], punct=".", extra=" الْمُقَدَّرَةُ عَلَى الْيَاءِ الْمَحْذُوفَةِ")]})
S.append({"id": "s2", "translation": {
 "en": "And He is not described by quiddity nor by quality.",
 "tr": "O, ne mâhiyetle ne de keyfiyetle vasfedilir."},
 "tokens": [
  W("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«and not».", "«ve … -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُوصَفُ", "wasafa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.", "«is described» — a passive with its hidden deputy doer.", "«vasfedilir» — gizli nâib-i fâilli meçhul."),
  FUSED("بِالْمَاهِيَّةِ", "بِ", "mahiyya", "«by quiddity» — the «what-is-it-ness» (مَا هِيَ) of a thing.", "«mâhiyetle» — bir şeyin «o nedir»liği (مَا هِيَ).", "«يُوصَفُ»", inner="الْمَاهِيَّةِ"),
  WALA(),
  W("بِالْكَيْفِيَّةِ", "kayfiyya", "noun", ["huruf-jarr", "atf-nasaq", "mahall-al-majrur"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«الْكَيْفِيَّةِ» مَجْرُورٌ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى «بِالْمَاهِيَّةِ».", "«by quality» — the «how-ness» (كَيْفَ).", "«keyfiyetle» — «nasıl»lık (كَيْفَ).", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الْكَيْفِيَّةِ", "kayfiyya", "noun")])]})
S.append({"id": "s3", "translation": {
 "en": "And He does not settle in a place, nor does time run upon Him.",
 "tr": "Bir mekânda yerleşmez ve üzerinde zaman geçmez."},
 "tokens": [
  W("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«and not».", "«ve … -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  MUDA("يَتَمَكَّنُ", "tamakkana", "«settles» — Form V: to take a place (مَكَان) and be fixed in it.", "«yerleşir» — tefe'ul bâbı: bir mekân (مَكَان) tutup orada sabitlenmek.", HIDDEN_HUWA, tags=["form-v-verbs"]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("مَكَانٍ", "makan", "«a place».", "«bir mekân».", "فِي", "«يَتَمَكَّنُ»", punct="،"),
  W("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«nor».", "«ve … -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  MUDA("يَجْرِي", "jara", "«runs» — a defective verb; the ḍamma is estimated on the yāʾ.", "«geçer, cereyan eder» — nâkıs fiil; damme yâ üzerinde takdirîdir.", "وَالْفَاعِلُ «زَمَانٌ»", tags=["naqis-verbs", "fail"], sign="الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  PRON_J("عَلَيْهِ", "عَلَيْ", "«upon Him» — the alif maqṣūra of عَلَى turns to yāʾ before the pronoun.", "«O'nun üzerinde» — عَلَى'nın elif-i maksûresi zamirden önce yâ olur.", "«يَجْرِي»"),
  W("زَمَانٌ", "zaman", "noun", ["fail", "al-fail-al-muzhar-wa-tanith-amilih"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«time» — the doer, held back behind the jarr phrase.", "«zaman» — câr-mecrûrun ardına bırakılmış fâil.", punct=".")]})

CAND = {
 "musawwar": need("musawwar", "مُصَوَّر", "ص و ر", "noun", "formed, given a form (ism mafʿūl of Form II)", "sûret verilmiş (tef'îl ism-i mef'ûlü)", 4),
 "mahiyya": need("mahiyya", "مَاهِيَّة", "م ا ه", "noun", "quiddity, essence — the answer to «what is it?»", "mâhiyet — «o nedir?» sorusunun cevabı", 5),
 "mutabaid": need("mutabaid", "مُتَبَعِّض", "ب ع ض", "noun", "made of portions, divisible into portions (ism fāʿil of Form V)", "parçalardan mürekkep, parçalanır (tefe'ul ism-i fâili)", 5),
 "mutajazzi": need("mutajazzi", "مُتَجَزِّئ", "ج ز أ", "noun", "made of parts, divisible (ism fāʿil of Form V)", "cüzlerden mürekkep, bölünür (tefe'ul ism-i fâili)", 5),
 "mutanahi": need("mutanahi", "مُتَنَاهٍ", "ن ه ي", "noun", "finite, having an end (ism fāʿil of Form VI)", "sonlu, nihayeti olan (tefâul ism-i fâili)", 5),
 "tamakkana": need("tamakkana", "تَمَكَّنَ", "م ك ن", "verb", "to settle, to be established in a place", "yerleşmek, bir yerde karar kılmak", 4),
}
MORPH = {"tamakkana": sarf.derived(sarf.B5, W5, "َ", "تَمَكَّن", "تَمَكَّن", "تَمَكَّن", "تَمَكُّن", "مُتَمَكِّن", None, None, None,
                                   "تَمَكَّنَ مِنَ الْمَكَانِ يَتَمَكَّنُ تَمَكُّنًا: اسْتَقَرَّ فِيهِ — مِنْ بَابِ التَّفَعُّلِ، لَازِمٌ")}
ADD_EN = (" Chapter 29 (matn line 31): the negations — not formed, bounded, numbered, of portions, of parts or finite; not described by"
          " quiddity or quality; in no place, under no time. The list continues chapter 5's لَيْسَ بِعَرَضٍ وَلَا جِسْمٍ وَلَا جَوْهَرٍ; the two"
          " epithets الشَّائِي الْمُرِيدُ closing the names are not authored.")
ADD_TR = (" Yirmi dokuzuncu bâb (matn satırı 31): nefiyler — sûretli, sınırlı, sayılı, parçalı, cüzlü ve sonlu değildir; mâhiyet ve keyfiyetle"
          " vasfedilmez; mekânda değildir, üzerinde zaman geçmez. Liste beşinci bâbın لَيْسَ بِعَرَضٍ وَلَا جِسْمٍ وَلَا جَوْهَرٍ'ini sürdürür; isimleri"
          " kapatan الشَّائِي الْمُرِيدُ sıfatları yazılmamıştır.")
finish(29, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 29 (matn line 31)", morph=MORPH)
