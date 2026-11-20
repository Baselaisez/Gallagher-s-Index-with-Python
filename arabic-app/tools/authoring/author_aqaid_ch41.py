# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 41: the Companions are mentioned only with good; witness for the ten; wiping over the khuffs; date-nabīdh.
Source: matn lines 77-79.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch41.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الصَّحَابَةُ وَالْعَشَرَةُ، وَالْمَسْحُ وَالنَّبِيذُ", "en": "The Companions and the Ten; the Khuffs and Nabīdh", "tr": "Sahâbe ve Aşere; Mesh ve Nebîz"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And one refrains from mentioning the Companions except with good.",
 "tr": "Sahâbeyi anmaktan — hayırla olmadıkça — kaçınılır."},
 "tokens": [
  W("وَيُكَفُّ", "kaffa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "doubled-verbs", "mudari-marfu"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«يُكَفُّ» فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «عَنْ ذِكْرِ».", "«one refrains» — an impersonal passive: its deputy doer is the jarr phrase.", "«kaçınılır» — gayr-i şahsî meçhul: nâib-i fâili câr-mecrûrdur.", segments=[seg("وَ", "wa", "conj"), seg("يُكَفُّ", "kaffa", "verb")]),
  PREP("عَنْ", "an", "«from».", "«-den»."),
  MAJ("ذِكْرِ", "dhikr", "«mentioning».", "«anmak».", "عَنْ", None, mudaf=True, extra="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ", tags=["naib-al-fail", "masdar"]),
  MUDI("الصَّحَابَةِ", "sahaba", "«the Companions» — a collective: those who met the Prophet believing and died believing.", "«sahâbe» — topluluk ismi: Peygamber'i mü'min olarak görüp mü'min olarak ölenler."),
  W("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ مَبْنِيَّةٌ لَا مَحَلَّ لَهَا.", "«except» — an exception with no stated whole: «with any manner … except with good».", "«ancak» — müstesnâ minhi zikredilmemiş istisnâ: «her şekilde … ancak hayırla»."),
  FUSED("بِخَيْرٍ", "بِ", "khayr", "«with good» — the jarr phrase takes the case its position demands, as an emptied exception does.", "«hayırla» — müferrağ istisnâda olduğu gibi câr-mecrûr, mevkiinin gerektirdiği hükmü alır.", "«ذِكْرِ»", inner="خَيْرٍ", punct=".", tags=["istithna-mufarragh"])]})
S.append({"id": "s2", "translation": {
 "en": "And we bear witness for the Ten who were given glad tidings, whom the Prophet — upon him be blessing and peace — gave glad tidings.",
 "tr": "Peygamber'in — ona salât ve selâm olsun — müjdelediği, müjdelenmiş On'a (cennetle) şehâdet ederiz."},
 "tokens": [
  MUDA("وَنَشْهَدُ", "shahida", "«and we bear witness» — that they are of Paradise.", "«ve şehâdet ederiz» — cennetlik olduklarına.", HIDDEN_NAHNU, wa="isti"),
  FUSED("لِلْعَشَرَةِ", "لِ", "ashara", "«for the Ten» — with the tāʾ, as the counted are men.", "«On için» — ma'dûd erkek olduğundan tâ'lı.", "«نَشْهَدُ»", inner="الْعَشَرَةِ", extra=" — أَيْ: بِالْجَنَّةِ", tags=["asma-al-adad-fil-kafiya"]),
  NAT("الْمُبَشَّرَةِ", "mubashshara", "«given glad tidings» — the ism mafʿūl of Form II.", "«müjdelenmiş» — tef'îl ism-i mef'ûlü.", "الْعَشَرَةِ", "jarr", tags=["ism-maful", "form-ii-verbs"]),
  W("الَّذِينَ", "alladhina", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ صِفَةٌ ثَانِيَةٌ لِـ«الْعَشَرَةِ».", "«whom» — the plural relative, a second adjective of the Ten.", "«ki onları» — çoğul ism-i mevsûl; On'un ikinci sıfatı."),
  W("بَشَّرَهُمُ", "bashshara", "verb", ["form-ii-verbs", "ism-mawsul", "al-bariz-al-muttasil"], "فِعْلٌ مَاضٍ، وَ«هُمْ» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ «النَّبِيُّ» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«gave them glad tidings» — the object pronoun comes before the doer; its mīm takes a ḍamma before the article.", "«onları müjdeledi» — mef'ûl zamiri fâilden önce gelir; mîmi elif-lâm önünde damme alır.", segments=[seg("بَشَّرَ", "bashshara", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  FAIL("النَّبِيُّ", "nabi", "«the Prophet».", "«Peygamber»."),
  *SALAWAT(),
  ]})
S[-1]["tokens"][-1]["punctAfter"] = "."
S.append({"id": "s3", "translation": {
 "en": "And we hold wiping over the khuffs (to be lawful) on a journey and at home.",
 "tr": "Seferde ve hazarda mestler üzerine meshi (câiz) görürüz."},
 "tokens": [
  MUDA("وَنَرَى", "raa", "«and we hold» — رَأَى here is of opinion: we judge it lawful.", "«ve görürüz» — رَأَى burada görüş fiilidir: câiz sayarız.", HIDDEN_NAHNU, wa="isti", tags=["naqis-verbs", "al-mutaaddi-wa-afal-al-qulub"], sign="الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"),
  MAFUL("الْمَسْحَ", "mash", "«wiping» — the masdar; in place of washing the feet.", "«meshi» — masdar; ayakları yıkamanın yerine.", "نَرَى", tags=["masdar"]),
  PREP("عَلَى", "ala", "«over».", "«üzerine»."),
  W("الْخُفَّيْنِ", "khuff", "noun", ["al-muthanna", "mahall-al-majrur", "huruf-jarr"], "اسْمٌ مَجْرُورٌ بِـ«عَلَى» وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«الْمَسْحَ».", "«the two khuffs» — a dual in jarr by its yāʾ.", "«iki mest» — yâ ile mecrûr tesniye."),
  PREP("فِي", "fi", "«on».", "«-de»."),
  MAJ("السَّفَرِ", "safar", "«a journey».", "«sefer».", "فِي", "«الْمَسْحَ»"),
  ATF("وَالْحَضَرِ", "hadar-home", "«and at home» — residence, the opposite of travel.", "«ve hazar» — ikamet; seferin karşıtı.", "السَّفَرِ", "jarr", punct=".")]})
S.append({"id": "s4", "translation": {"en": "And we do not forbid the nabīdh of dates.", "tr": "Hurma nebîzini haram saymayız."},
 "tokens": [
  W("وَلَا", "la-nafiya", "part", ["la-nafiya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«and not».", "«ve … -mayız».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  MUDA("نُحَرِّمُ", "harrama", "«we forbid» — Form II: to declare forbidden.", "«haram sayarız» — tef'îl bâbı: haram kılmak.", HIDDEN_NAHNU, tags=["form-ii-verbs"]),
  MAFUL("نَبِيذَ", "nabidh", "«the nabīdh of» — water in which dates were steeped, before it ferments to intoxication.", "«nebîzi» — hurmanın suda bekletilmesiyle yapılan, sarhoş edecek kadar fermente olmamış içecek.", "نُحَرِّمُ", mudaf=True),
  MUDI("التَّمْرِ", "tamr", "«dates».", "«hurma».", punct=".")]})

CAND = {
 "sahaba": need("sahaba", "صَحَابَة", "ص ح ب", "noun", "the Companions of the Prophet (a collective)", "sahâbe (topluluk ismi)", 3),
 "mubashshara": need("mubashshara", "مُبَشَّرَة", "ب ش ر", "noun", "given glad tidings (ism mafʿūl of Form II, feminine)", "müjdelenmiş (tef'îl ism-i mef'ûlü, müennes)", 4),
 "mash": need("mash", "مَسْح", "م س ح", "noun", "wiping (with a wet hand) — the masdar of مَسَحَ", "mesh, ıslak elle sıvazlama (مَسَحَ'nin masdarı)", 3),
 "khuff": need("khuff", "خُفّ", "خ ف ف", "noun", "a khuff — a leather sock that may be wiped instead of washing the foot", "mest — ayak yıkamak yerine üzerine mesh edilebilen deri çorap", 3, plural="خِفَاف"),
 "hadar-home": need("hadar-home", "حَضَر", "ح ض ر", "noun", "residence at home — the opposite of travel", "hazar, ikamet — seferin karşıtı", 4),
 "nabidh": need("nabidh", "نَبِيذ", "ن ب ذ", "noun", "nabīdh — a drink of steeped dates or raisins", "nebîz — hurma ya da kuru üzümün suda bekletilmesiyle yapılan içecek", 4),
}
ADD_EN = (" Chapter 41 (matn lines 77-79): the Companions mentioned only with good, witness for the Ten, wiping over the khuffs on a journey and"
          " at home, and date-nabīdh not forbidden; the supplied text reads وَيُكَفُّ (some prints وَنَكُفُّ).")
ADD_TR = (" Kırk birinci bâb (matn satırları 77-79): sahâbe ancak hayırla anılır, aşereye şehâdet, seferde ve hazarda mestler üzerine mesh,"
          " hurma nebîzi haram değildir; nüsha وَيُكَفُّ okur (bazı baskılarda وَنَكُفُّ).")
finish(41, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 41 (matn lines 77-79)")
