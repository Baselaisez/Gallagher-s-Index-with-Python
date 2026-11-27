# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 32: takwīn is God's bringing-into-being of the world not in eternity but at the time of each thing's
existence; and will is an eternal attribute. Source: matn line 33 (وهو تكوينه تعالى للعالم … قائمة بذاته); وَالتَّكْوِينُ صِفَةٌ لِلهِ تَعَالَى
أَزَلِيَّةٌ and وَهُوَ غَيْرُ الْمُكَوَّنِ عِنْدَنَا are chapter 6.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch32.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "التَّكْوِينُ وَالْإِرَادَةُ", "en": "Bringing-into-Being, and Will", "tr": "Tekvîn ve İrade"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And it is His — the Exalted — bringing-into-being of the world and of every part of its parts, not in eternity but at the time of its existence, according to His knowledge and His will.",
 "tr": "O, Allah Teâlâ'nın âlemi ve âlemin her bir cüzünü — ezelde değil, varlığının vaktinde, ilmine ve iradesine göre — var etmesidir."},
 "tokens": [
  HUWA("وَهُوَ", "«and it» — takwīn, defined in chapter 6 as an eternal attribute.", "«ve o» — altıncı bâbda ezelî sıfat olarak tarif edilen tekvîn.", wa="atf"),
  ENC("تَكْوِينُهُ", "takwin", "«His bringing-into-being» — a masdar annexed to its doer; it governs لِلْعَالَمِ as its verb would.", "«O'nun var etmesi» — fâiline muzâf masdar; fiili gibi لِلْعَالَمِ'e amel eder.", "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ", pr="هُ", tags=["mubtada-khabar", "masdar", "imal-al-masdar"]),
  TAALA(),
  FUSED("لِلْعَالَمِ", "لِ", "alam", "«of the world» — the masdar's object through the lām.", "«âlemi» — masdarın lâm ile mef'ûlü.", "«تَكْوِينُهُ»", inner="الْعَالَمِ", tags=["imal-al-masdar"]),
  FUSED("وَلِكُلِّ", "لِ", "kull", "«and of every».", "«ve her … -ini».", "«تَكْوِينُهُ»", wa="atf", mudaf=True, inner="كُلِّ"),
  MUDI("جُزْءٍ", "juz", "«part».", "«cüz»."),
  PREP("مِنْ", "min", "«of».", "«-den»."),
  ENC("أَجْزَائِهِ", "juz", "«its parts» — the phrase describes جُزْءٍ.", "«cüzlerinden» — câr-mecrûr جُزْءٍ'in sıfatıdır.", "اسْمٌ مَجْرُورٌ بِـ«مِنْ» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", att="مَحْذُوفٍ صِفَةٌ لِـ«جُزْءٍ»", tags=["jam-taksir", "jumla-sifa"]),
  LA("«not».", "«değil»."),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("الْأَزَلِ", "azal", "«eternity» — the beginningless past; the bringing-into-being is eternal as an attribute, its effect is not.", "«ezel» — başlangıçsız geçmiş; var etme sıfat olarak ezelîdir, eseri değil.", "فِي", "«تَكْوِينُهُ»", punct="،"),
  W("بَلْ", "bal", "part", ["atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya"], "حَرْفُ إِضْرَابٍ وَعَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "«but rather» — bal sets the negated aside and affirms what follows.", "«bilakis» — bel, nefyedileni bırakır, ardındakini ispat eder."),
  FUSED("لِوَقْتِ", "لِ", "waqt", "«at the time of» — the lām of time; joined to the negated فِي الْأَزَلِ.", "«vaktinde» — vakit lâmı; nefyedilen فِي الْأَزَلِ'e atıf.", "«تَكْوِينُهُ»", mudaf=True, inner="وَقْتِ", tags=["atf-nasaq"]),
  ENC("وُجُودِهِ", "wujud", "«its existence».", "«varlığının».", "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ"),
  PREP("عَلَى", "ala", "«according to».", "«göre»."),
  MAJ("حَسَبِ", "hasab", "«the measure of» — عَلَى حَسَبِ: according to.", "«… -e göre» — عَلَى حَسَبِ: göre.", "عَلَى", "مَحْذُوفٍ حَالٌ مِنْ «تَكْوِينُهُ»", mudaf=True, tags=["hal"]),
  ENC("عِلْمِهِ", "ilm", "«His knowledge».", "«ilmine».", "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ"),
  ENC("وَإِرَادَتِهِ", "irada", "«and His will» — the tāʾ marbūṭa opens to tāʾ before the pronoun.", "«ve iradesine» — tâ-i merbûta zamirden önce açık tâ olur.", "مَعْطُوفٌ عَلَى «عِلْمِهِ» تَابِعٌ لَهُ فِي الْجَرِّ", pr="هِ", wa="atf", tags=["atf-nasaq"], punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And will is an eternal attribute of God the Exalted, subsisting in His Essence.",
 "tr": "İrade, Allah Teâlâ'nın zâtıyla kâim ezelî bir sıfatıdır."},
 "tokens": [
  MUB("وَالْإِرَادَةُ", "irada", "«and will».", "«ve irade».", wa="isti"),
  KHA("صِفَةٌ", "sifa", "«an attribute».", "«bir sıfat».", of="الْإِرَادَةُ"),
  FUSED("لِلهِ", "لِ", "allah", "«of God» — the lām of the article is swallowed into the Name: لِ + اللّٰه.", "«Allah'ın» — elif-lâmın lâmı İsm-i Celâl'e katılır: لِ + اللّٰه.", "مَحْذُوفٍ صِفَةٌ لِـ«صِفَةٌ»", inner="اللهِ", pos="propn", tags=["anwa-al-lam-al-tarif"]),
  TAALA(),
  NAT("أَزَلِيَّةٌ", "azali", "«eternal».", "«ezelî».", "صِفَةٌ", "raf", tags=["ism-mansub"]),
  NAT("قَائِمَةٌ", "qaim", "«subsisting» — a second adjective.", "«kâim» — ikinci sıfat.", "صِفَةٌ", "raf", tags=["ism-fail"], extra=" (صِفَةٌ ثَانِيَةٌ)"),
  ENC("بِذَاتِهِ", "dhat", "«in His Essence».", "«zâtıyla».", "«ذَاتِ» مَجْرُورٌ بِالْبَاءِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", letter="بِ", att="«قَائِمَةٌ»", punct=".")]})

CAND = {
 "azal": need("azal", "أَزَل", "أ ز ل", "noun", "eternity without beginning", "ezel, başlangıçsızlık", 4),
}
ADD_EN = (" Chapter 32 (matn line 33): takwīn as God's bringing-into-being of the world and of each of its parts at the time of its existence,"
          " not in eternity, and will as an eternal attribute subsisting in His Essence; the sentences on takwīn before it are chapter 6.")
ADD_TR = (" Otuz ikinci bâb (matn satırı 33): tekvîn, Allah'ın âlemi ve her cüzünü ezelde değil varlığı vaktinde var etmesidir; irade, zâtıyla"
          " kâim ezelî bir sıfattır; öncesindeki tekvîn cümleleri altıncı bâbdır.")
finish(32, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 32 (matn line 33)")
