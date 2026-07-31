# -*- coding: utf-8 -*-
"""Author content/samples/kitab-al-sulh — the Sulh story, chapter by chapter.

ORIGINAL graded Arabic, composed editorially from the user's uploaded
Turkish fiqh reference (research/sources/sulh-fiqh-turkce.txt). The
Qur'anic clause {وَالصُّلْحُ خَيْرٌ} (al-Nisa 4:128) and the hadith wording
«الصُّلْحُ جَائِزٌ بَيْنَ الْمُسْلِمِينَ…» (Tirmidhi, Ahkam 17) are received
text; everything else is simple original composition in the Hidaya
register, marked pending-scholarly-review. Verb paradigms ride the same
audited engines as the rest of the corpus.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PKG = ROOT / "content/samples/kitab-al-sulh"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import sarf_gen as _sg

import re
DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)

def tok(full, lex, pos, grammar, ar, en, tr, punct=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)},
         "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if punct: t["punctAfter"] = punct
    return t

J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}

S = []

S.append({"id": "s1", "translation": {
 "en": "Sulh is a contract that lifts the dispute between two contending parties.",
 "tr": "Sulh, iki çekişen taraf arasındaki nizâı kaldıran bir akittir."},
 "tokens": [
  tok("الصُّلْحُ","sulh","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — الصُّلْحُ لُغَةً: قَطْعُ النِّزَاعِ.",
      "Mubtada in raf' — «sulh», in the tongue: cutting off dispute.",
      "Merfû mübteda — «sulh» lugatte: nizâı kesmektir."),
  tok("عَقْدٌ","aqd","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ عَقَدَ.",
      "The khabar in raf' — the masdar of «to bind».",
      "Merfû haber — عَقَدَ'nin masdarıdır."),
  tok("يَرْفَعُ","rafaa","verb",["mudari-marfu","jumla-sifa"],
      "مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِفَةٌ لِـ«عَقْدٌ» فِي مَحَلِّ رَفْعٍ.",
      "A mudari' in raf' — the clause describes «a contract», in raf's position.",
      "Merfû muzâri — cümle «عقد»in sıfatıdır; mahallen merfûdur."),
  tok("النِّزَاعَ","niza","noun",["maful-bihi","masdar"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَصْدَرُ الْمُفَاعَلَةِ مِنْ نَازَعَ.",
      "The object in nasb — the Form III masdar of «to contend».",
      "Mensub mef'ûlün bih — نَازَعَ'nin müfâale masdarıdır."),
  tok("بَيْنَ","bayna","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "A place-adverbial in nasb, mudaf.",
      "Mensub mekân zarfı; muzâftır."),
  tok("الْمُتَخَاصِمَيْنِ","mutakhasim","noun",["idafa-definiteness","ism-fail","form-vi-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنَّى اسْمِ فَاعِلِ التَّفَاعُلِ.",
      "Mudaf ilayh, jarr by the ya — the dual of the Form VI participle.",
      "Yâ ile mecrur muzâfun ileyh — tefâulün ism-i fâilinin tesniyesidir.", punct="."),
 ],
 "jumal": [
  J("الصُّلْحُ عَقْدٌ…",
    "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا؛ وَجُمْلَةُ «يَرْفَعُ» صِفَةٌ.",
    "An opening nominal sentence — i'rabless; the «lifts» clause is its sifa.",
    "İbtidâî isim cümlesi — mahalsiz; «يرفع» cümlesi sıfattır."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "Allah Most High has said: “And sulh is best” (al-Nisa 4:128).",
 "tr": "Allah Teâlâ buyurdu: «Sulh daha hayırlıdır» (en-Nisâ 4/128)."},
 "tokens": [
  tok("قَالَ","qala","verb",["hollow-verbs"],
      "فِعْلٌ مَاضٍ — أَجْوَفُ.",
      "A past verb — hollow.",
      "Mâzî fiil — ecveftir."),
  tok("اللهُ","allah","propn",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The Name of Majesty, fa'il in raf'.",
      "Lafza-i celâl; merfû fâildir."),
  tok("تَعَالَى","taala","verb",["naqis-verbs","form-vi-verbs"],
      "فِعْلٌ مَاضٍ، وَجُمْلَتُهُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "A past verb whose clause interposes in reverence.",
      "Mâzî fiil; cümlesi tazim için muterizedir.", punct=":"),
  tok("وَالصُّلْحُ","sulh","noun",["mubtada-khabar"],
      "الْوَاوُ عَلَى مَا قَبْلَهَا فِي الْآيَةِ، وَ«الصُّلْحُ» مُبْتَدَأٌ مَرْفُوعٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "The waw follows what precedes it in the aya; «al-sulh» a mubtada in raf' — the clause is the quoted speech.",
      "Vav, âyette öncesine bağlıdır; «الصلح» merfû mübteda — cümle makûlü'l-kavldir."),
  tok("خَيْرٌ","khayr","noun",["mubtada-khabar","ism-tafdil"],
      "خَبَرٌ مَرْفُوعٌ — «خَيْر» بِقُوَّةِ أَفْعَلِ التَّفْضِيلِ.",
      "The khabar in raf' — «khayr» with the comparative's force.",
      "Merfû haber — «خير» ism-i tafdîl kuvvetindedir.", punct="."),
 ],
 "jumal": [
  J("وَالصُّلْحُ خَيْرٌ",
    "جُمْلَةٌ اسْمِيَّةٌ — مَقُولُ الْقَوْلِ فِي مَحَلِّ نَصْبٍ.",
    "A nominal sentence — the quoted speech, in nasb's position.",
    "İsim cümlesi — makûlü'l-kavl olarak mahallen mensubdur."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And the Prophet, peace be upon him, said: “Sulh is permissible between the Muslims.”",
 "tr": "Peygamber (aleyhisselâm) buyurdu: «Müslümanlar arasında sulh câizdir.»"},
 "tokens": [
  tok("وَقَالَ","qala","verb",["atf-nasaq","hollow-verbs"],
      "الْوَاوُ عَاطِفَةٌ، «قَالَ» مَاضٍ.",
      "The waw joins; «said» a past verb.",
      "Vav atıftır; «قال» mâzîdir."),
  tok("النَّبِيُّ","nabi","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.","Fa'il in raf'.","Merfû fâildir."),
  tok("عَلَيْهِ","alayhi","part",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ — خَبَرٌ مُقَدَّمٌ لِلدُّعَاءِ.",
      "A jarr-phrase — the fronted khabar of the blessing.",
      "Câr-mecrûr — duanın mukaddem haberidir."),
  tok("السَّلَامُ","salam","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَالْجُمْلَةُ مُعْتَرِضَةٌ دُعَائِيَّةٌ.",
      "The delayed mubtada in raf' — a parenthetical blessing.",
      "Muahhar mübteda; merfû — muterize dua cümlesidir.", punct=":"),
  tok("الصُّلْحُ","sulh","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "Mubtada in raf' — the clause is the quoted speech.",
      "Merfû mübteda — cümle makûlü'l-kavldir."),
  tok("جَائِزٌ","jaiz","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ جَازَ.",
      "The khabar in raf' — the participle of «to be allowed».",
      "Merfû haber — جَازَ'nin ism-i fâilidir."),
  tok("بَيْنَ","bayna","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "An adverbial in nasb, mudaf.",
      "Mensub zarf; muzâftır."),
  tok("الْمُسْلِمِينَ","muslim","noun",["idafa-definiteness","jam-mudhakkar-salim","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "Mudaf ilayh, jarr by the ya — a sound masculine plural.",
      "Yâ ile mecrur muzâfun ileyh — cem-i müzekker-i sâlimdir.", punct="."),
 ],
 "jumal": [
  J("الصُّلْحُ جَائِزٌ بَيْنَ الْمُسْلِمِينَ",
    "جُمْلَةٌ اسْمِيَّةٌ — مَقُولُ الْقَوْلِ فِي مَحَلِّ نَصْبٍ.",
    "A nominal sentence — the quoted speech, in nasb's position.",
    "İsim cümlesi — makûlü'l-kavl olarak mahallen mensubdur."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "— “except a sulh that forbids a lawful thing or permits a forbidden one.”",
 "tr": "— «Helâli haram kılan yahut haramı helâl kılan bir sulh müstesnâ.»"},
 "tokens": [
  tok("إِلَّا","illa","part",["istithna"],
      "حَرْفُ اسْتِثْنَاءٍ.",
      "The particle of exception.",
      "İstisnâ harfidir."),
  tok("صُلْحًا","sulh","noun",["istithna"],
      "مُسْتَثْنًى مَنْصُوبٌ.",
      "The excepted, in nasb.",
      "Müstesnâ; mensubdur."),
  tok("حَرَّمَ","harrama","verb",["form-ii-verbs","jumla-sifa"],
      "مَاضٍ مِنَ التَّفْعِيلِ — وَالْجُمْلَةُ صِفَةٌ لِـ«صُلْحًا».",
      "A Form II past — the clause describes «a sulh».",
      "Tef'îl bâbından mâzî — cümle «صلحًا»ın sıfatıdır."),
  tok("حَلَالًا","halal","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "The object in nasb.",
      "Mensub mef'ûlün bihtir."),
  tok("أَوْ","aw","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ.","A joining particle.","Atıf harfidir."),
  tok("أَحَلَّ","ahalla","verb",["atf-nasaq","form-iv-verbs"],
      "مَعْطُوفٌ — مَاضٍ مِنَ الْإِفْعَالِ، مُضَاعَفٌ.",
      "Joined on — a Form IV past, geminate.",
      "Matuf — if'âl bâbından mâzî; muzâaftır."),
  tok("حَرَامًا","haram","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "The object in nasb.",
      "Mensub mef'ûlün bihtir.", punct="."),
 ],
 "jumal": [
  J("إِلَّا صُلْحًا حَرَّمَ حَلَالًا…",
    "اسْتِثْنَاءٌ مُتَّصِلٌ مِنْ عُمُومِ الصُّلْحِ الْجَائِزِ؛ وَجُمْلَةُ «حَرَّمَ» صِفَةٌ فِي مَحَلِّ نَصْبٍ.",
    "A connected exception from the general permission; the «forbids» clause its sifa, in nasb's position.",
    "Câiz sulhun umumundan muttasıl istisnâ; «حرّم» cümlesi sıfat olarak mahallen mensubdur."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "So sulh is commended, and the judge urges the disputants toward it.",
 "tr": "Şu halde sulh menduptur; hâkim, hasımları ona teşvik eder."},
 "tokens": [
  tok("فَالصُّلْحُ","sulh","noun",["mubtada-khabar"],
      "الْفَاءُ لِلتَّفْرِيعِ وَ«الصُّلْحُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "The fa draws the consequence; «al-sulh» a mubtada in raf'.",
      "Fâ tefrî' içindir; «الصلح» merfû mübtedadır."),
  tok("مَنْدُوبٌ","mandub","noun",["mubtada-khabar","ism-maful"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ: الْمَطْلُوبُ فِعْلُهُ طَلَبًا غَيْرَ جَازِمٍ.",
      "The khabar in raf' — a passive participle: what the Law asks for without binding.",
      "Merfû haber — ism-i mef'ûl: kesin olmayan taleple istenendir.", punct="،"),
  tok("وَالْقَاضِي","qadi","noun",["atf-nasaq","mubtada-khabar","ism-maqsur-manqus","ism-fail"],
      "الْوَاوُ عَاطِفَةٌ، «الْقَاضِي» مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.",
      "The waw joins; «the judge» a mubtada by an assumed damma — a manqus noun.",
      "Vav atıftır; «القاضي» takdîrî damme ile merfû mübteda — menkûstur."),
  tok("يُرَغِّبُ","raggaba","verb",["mudari-marfu","form-ii-verbs"],
      "مُضَارِعٌ مَرْفُوعٌ مِنَ التَّفْعِيلِ — وَالْجُمْلَةُ خَبَرٌ.",
      "A Form II mudari' in raf' — the clause is the khabar.",
      "Tef'îl bâbından merfû muzâri — cümle haberdir."),
  tok("فِيهِ","fi","part",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ.","A jarr-phrase.","Câr ve mecrûrdur."),
  tok("الْخُصُومَ","khasm","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ «خَصْم».",
      "The object in nasb — the plural of «disputant».",
      "Mensub mef'ûlün bih — «خصم»in cem'idir.", punct="."),
 ],
 "jumal": [
  J("وَالْقَاضِي يُرَغِّبُ فِيهِ الْخُصُومَ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ — فِي مَحَلِّ رَفْعٍ.",
    "A nominal sentence whose khabar is a verbal clause — in raf's position.",
    "Haberi fiil cümlesi olan isim cümlesi — mahallen merfûdur."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And it is of three kinds: sulh upon acknowledgment, sulh upon denial, and sulh upon silence.",
 "tr": "Sulh üç nevidir: ikrar üzerine sulh, inkâr üzerine sulh ve sükût üzerine sulh."},
 "tokens": [
  tok("وَهُوَ","huwa","pron",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، «هُوَ» مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.",
      "The waw begins afresh; «it» a mubtada in raf's position.",
      "Vav isti'nâfiyedir; «هو» mahallen merfû mübtedadır."),
  tok("ثَلَاثَةُ","thalatha","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَاءَ بِالتَّاءِ لِأَنَّ الْمَعْدُودَ «نَوْع» مُذَكَّرٌ: قَاعِدَةُ الْعَدَدِ.",
      "The khabar in raf', mudaf — it keeps the TA because the counted «kind» is masculine: the number rule.",
      "Merfû haber; muzâf — ma'dûd olan «نوع» müzekker olduğundan TÂ'lıdır: aded kaidesi."),
  tok("أَنْوَاعٍ","naw","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعٌ بَعْدَ الثَّلَاثَةِ.",
      "Mudaf ilayh in jarr — a plural, as 3–10 demand.",
      "Mecrur muzâfun ileyh — 3–10'dan sonra cemidir.", punct=":"),
  tok("صُلْحٌ","sulh","noun",["badal"],
      "بَدَلٌ مُفَصَّلٌ مِنْ «ثَلَاثَةُ» مَرْفُوعٌ.",
      "A detailing badal of «three», in raf'.",
      "«ثلاثة»den tafsil bedeli; merfûdur."),
  tok("عَنْ","an-prep","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("إِقْرَارٍ","iqrar","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ — مَصْدَرُ الْإِفْعَالِ.",
      "In jarr — the Form IV masdar.",
      "Mecrur — if'âl masdarıdır.", punct="،"),
  tok("وَصُلْحٌ","sulh","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ.","Joined, in raf'.","Matuf; merfûdur."),
  tok("عَنْ","an-prep","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("إِنْكَارٍ","inkar","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ — مَصْدَرُ الْإِفْعَالِ.",
      "In jarr — the Form IV masdar.",
      "Mecrur — if'âl masdarıdır.", punct="،"),
  tok("وَصُلْحٌ","sulh","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ.","Joined, in raf'.","Matuf; merfûdur."),
  tok("عَنْ","an-prep","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("سُكُوتٍ","sukut","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ — مَصْدَرُ سَكَتَ.",
      "In jarr — the masdar of «to be silent».",
      "Mecrur — سَكَتَ'nin masdarıdır.", punct="."),
 ],
 "jumal": [
  J("وَهُوَ ثَلَاثَةُ أَنْوَاعٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا؛ وَفِيهَا قَاعِدَةُ الْعَدَدِ ٣–١٠.",
    "A fresh nominal sentence — i'rabless; the 3–10 number rule lives in it.",
    "İsti'nâf isim cümlesi — mahalsiz; içinde 3–10 aded kaidesi vardır."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And its pillar is the offer and the acceptance.",
 "tr": "Rüknü, icap ve kabuldür."},
 "tokens": [
  tok("وَرُكْنُهُ","rukn","noun",["mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، «رُكْنُ» مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ إِلَى الْهَاءِ.",
      "The waw joins; «pillar» a mubtada in raf', mudaf to the «its».",
      "Vav atıftır; «ركن» merfû mübteda; هُ zamirine muzâftır."),
  tok("الْإِيجَابُ","ijab","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ الْإِفْعَالِ.",
      "The khabar in raf' — the Form IV masdar.",
      "Merfû haber — if'âl masdarıdır."),
  tok("وَالْقَبُولُ","qabul","noun",["atf-nasaq","masdar"],
      "مَعْطُوفٌ مَرْفُوعٌ.",
      "Joined, in raf'.",
      "Matuf; merfûdur.", punct="."),
 ],
 "jumal": [
  J("وَرُكْنُهُ الْإِيجَابُ وَالْقَبُولُ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal sentence — i'rabless.",
    "Matuf isim cümlesi — mahalli yoktur."),
 ]})

TITLE1 = {"ar": "تَعْرِيفُ الصُّلْحِ وَمَشْرُوعِيَّتُهُ",
          "en": "The Definition of Sulh, and Its Legitimacy",
          "tr": "Sulhun Tarifi ve Meşrûiyeti"}

# ---------------------------------------------------------------- chapter 2
S2 = []

S2.append({"id": "s8", "translation": {
 "en": "Sulh upon acknowledgment, when it falls on property, is like a sale.",
 "tr": "İkrar üzerine sulh, bir mal üzerine vâki olursa satım (bey') gibidir."},
 "tokens": [
  tok("فَالصُّلْحُ","sulh","noun",["mubtada-khabar"],
      "الْفَاءُ لِلتَّفْصِيلِ وَ«الصُّلْحُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "The fa opens the detail; «al-sulh» a mubtada in raf'.",
      "Fâ tafsil içindir; «الصلح» merfû mübtedadır."),
  tok("عَنْ","an-prep","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("إِقْرَارٍ","iqrar","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ.","In jarr.","Mecrurdur."),
  tok("إِذَا","idha","part",["idha-shartiyya","maful-fih"],
      "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "The adverbial carrying a condition.",
      "Şart manası taşıyan zarftır."),
  tok("وَقَعَ","waqaa","verb",["idha-shartiyya","mithal-verbs"],
      "فِعْلُ الشَّرْطِ — مِثَالٌ وَاوِيٌّ، وَفَاعِلُهُ مُسْتَتِرٌ.",
      "The condition verb — an assimilated (waw) verb, its fa'il concealed.",
      "Şart fiili — misâl-i vâvî; fâili gizlidir."),
  tok("عَلَى","ala","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("مَالٍ","mal","noun",["huruf-jarr"],
      "مَجْرُورٌ.","In jarr.","Mecrurdur."),
  tok("فَهُوَ","huwa","pron",["mubtada-khabar"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ وَ«هُوَ» مُبْتَدَأٌ.",
      "The fa ties the answer; «it» a mubtada.",
      "Fâ, cevabı bağlar; «هو» mübtedadır."),
  tok("كَالْبَيْعِ","bay","noun",["huruf-jarr","tashbih","mubtada-khabar"],
      "الْكَافُ لِلتَّشْبِيهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "The kaf of likeness — the phrase is the khabar.",
      "Teşbih kâfı — câr-mecrûr haberdir.", punct="."),
 ],
 "jumal": [
  J("إِذَا وَقَعَ عَلَى مَالٍ فَهُوَ كَالْبَيْعِ",
    "جُمْلَةُ شَرْطٍ ظَرْفِيَّةٌ، جَوَابُهَا بِالْفَاءِ — وَالْجُمْلَتَانِ خَبَرٌ عَنِ الصُّلْحِ.",
    "A when-condition whose answer rides the fa — together the khabar of «sulh».",
    "Zarf yollu şart; cevabı fâ iledir — ikisi birlikte «sulh»un haberidir."),
 ]})

S2.append({"id": "s9", "translation": {
 "en": "And when it falls on a usufruct, it is like a hire.",
 "tr": "Bir menfaat üzerine vâki olursa kira (icâre) gibidir."},
 "tokens": [
  tok("وَإِذَا","idha","part",["atf-nasaq","idha-shartiyya"],
      "الْوَاوُ عَاطِفَةٌ وَ«إِذَا» ظَرْفُ شَرْطٍ.",
      "The waw joins; «when» the conditional adverbial.",
      "Vav atıftır; «إذا» şart zarfıdır."),
  tok("وَقَعَ","waqaa","verb",["idha-shartiyya","mithal-verbs"],
      "فِعْلُ الشَّرْطِ.","The condition verb.","Şart fiilidir."),
  tok("عَلَى","ala","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("مَنْفَعَةٍ","manfaa","noun",["huruf-jarr"],
      "مَجْرُورٌ — مَصْدَرٌ مِيمِيٌّ مِنَ النَّفْعِ.",
      "In jarr — a mimic masdar of «benefit».",
      "Mecrur — نفع'den mîmî masdardır."),
  tok("فَهُوَ","huwa","pron",["mubtada-khabar"],
      "الْفَاءُ رَابِطَةٌ وَ«هُوَ» مُبْتَدَأٌ.",
      "The fa ties; «it» a mubtada.",
      "Fâ bağlayıcıdır; «هو» mübtedadır."),
  tok("كَالْإِجَارَةِ","ijara","noun",["huruf-jarr","tashbih","mubtada-khabar"],
      "الْكَافُ لِلتَّشْبِيهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "The kaf of likeness — the phrase is the khabar.",
      "Teşbih kâfı — câr-mecrûr haberdir.", punct="."),
 ],
 "jumal": [
  J("وَإِذَا وَقَعَ عَلَى مَنْفَعَةٍ فَهُوَ كَالْإِجَارَةِ",
    "جُمْلَةُ شَرْطٍ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined conditional sentence — i'rabless.",
    "Matuf şart cümlesi — mahalli yoktur."),
 ]})

S2.append({"id": "s10", "translation": {
 "en": "And sulh upon denial is permissible — to cut the litigation short.",
 "tr": "İnkâr üzerine sulh câizdir — husumeti kesmek için."},
 "tokens": [
  tok("وَالصُّلْحُ","sulh","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ وَ«الصُّلْحُ» مُبْتَدَأٌ.",
      "The waw joins; «al-sulh» a mubtada.",
      "Vav atıftır; «الصلح» mübtedadır."),
  tok("عَنْ","an-prep","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("إِنْكَارٍ","inkar","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ.","In jarr.","Mecrurdur."),
  tok("جَائِزٌ","jaiz","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ.","The khabar in raf'.","Merfû haberdir."),
  tok("لِقَطْعِ","qat","noun",["huruf-jarr","lam-taleel","masdar","idafa-definiteness"],
      "اللَّامُ لِلتَّعْلِيلِ وَ«قَطْعِ» مَجْرُورٌ مُضَافٌ.",
      "The lam of purpose; «cutting» in jarr, mudaf.",
      "Ta'lîl lâmı; «قطع» mecrur ve muzâftır."),
  tok("الْخُصُومَةِ","khusuma","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrur muzâfun ileyhtir.", punct="."),
 ],
 "jumal": [
  J("وَالصُّلْحُ عَنْ إِنْكَارٍ جَائِزٌ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal sentence — i'rabless.",
    "Matuf isim cümlesi — mahalli yoktur."),
 ]})

S2.append({"id": "s11", "translation": {
 "en": "And no sulh is valid over what is not lawful property — like wine.",
 "tr": "Mütekavvim mal olmayan şey üzerine sulh câiz olmaz — şarap gibi."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ وَ«لَا» نَافِيَةٌ.",
      "The waw joins; «la» negates.",
      "Vav atıftır; «لا» nâfiyedir."),
  tok("يَجُوزُ","jawaza","verb",["mudari-marfu","hollow-verbs"],
      "مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ.",
      "A mudari' in raf' — hollow.",
      "Merfû muzâri — ecveftir."),
  tok("الصُّلْحُ","sulh","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.","Fa'il in raf'.","Merfû fâildir."),
  tok("عَلَى","ala","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","huruf-jarr"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.",
      "A relative noun in jarr's position.",
      "İsm-i mevsûl; mahallen mecrurdur."),
  tok("لَيْسَ","laysa","verb",["kana-wa-akhawatuha","ism-mawsul"],
      "«لَيْسَ» وَاسْمُهَا مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةُ «مَا».",
      "«Laysa» with its concealed noun — the clause is ma's sila.",
      "«ليس»; ismi gizlidir — cümle «ما»nın sılasıdır."),
  tok("بِمَالٍ","mal","noun",["kana-wa-akhawatuha","tawkid","huruf-jarr"],
      "الْبَاءُ زَائِدَةٌ فِي خَبَرِ «لَيْسَ»، وَ«مَالٍ» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.",
      "An EXTRA ba on laysa's khabar; «property» jarr in form, nasb in place.",
      "«ليس»nin haberinde ZÂİD بِ; «مال» lafzan mecrur, mahallen mensubdur."),
  tok("مُتَقَوِّمٍ","mutaqawwim","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلِ التَّفَعُّلِ: مَا يُبَاحُ الِانْتِفَاعُ بِهِ شَرْعًا.",
      "A na't in jarr — the Form V participle: property the Law lets one use.",
      "Mecrur na't — tefe''ulün ism-i fâili: şer'an intifaı mübah maldır."),
  tok("كَالْخَمْرِ","khamr","noun",["huruf-jarr","tashbih"],
      "الْكَافُ لِلتَّمْثِيلِ.",
      "The kaf of exemplifying.",
      "Temsil kâfıdır.", punct="."),
 ],
 "jumal": [
  J("لَيْسَ بِمَالٍ مُتَقَوِّمٍ",
    "جُمْلَةُ الصِّلَةِ — لَا مَحَلَّ لَهَا؛ وَالْبَاءُ الزَّائِدَةُ تُؤَكِّدُ النَّفْيَ.",
    "The sila clause — i'rabless; the extra ba presses the negation.",
    "Sıla cümlesi — mahalsiz; zâid بِ nefyi pekiştirir."),
 ]})

S2.append({"id": "s12", "translation": {
 "en": "And whoever settles for part of his debt has dropped the rest.",
 "tr": "Kim alacağının bir kısmı üzerine sulh yaparsa, kalanını düşürmüş olur."},
 "tokens": [
  tok("وَمَنْ","man-shart","pron",["in-shartiyya","mubtada-khabar"],
      "اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "A jazm-working conditional noun, mubtada in raf's position.",
      "Cezm eden şart ismi; mahallen merfû mübtedadır."),
  tok("صَالَحَ","salaha","verb",["in-shartiyya","form-iii-verbs"],
      "فِعْلُ الشَّرْطِ — مَاضٍ فِي مَحَلِّ جَزْمٍ، مِنَ الْمُفَاعَلَةِ.",
      "The condition verb — a past in jazm's position, Form III.",
      "Şart fiili — mahallen meczum mâzî; müfâale bâbındandır."),
  tok("عَلَى","ala","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("بَعْضِ","baad","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ.","In jarr, mudaf.","Mecrur; muzâftır."),
  tok("دَيْنِهِ","dayn","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ إِلَى الْهَاءِ.",
      "Mudaf ilayh in jarr, itself mudaf to «his».",
      "Mecrur muzâfun ileyh; هُ'ya muzâftır."),
  tok("فَقَدْ","qad","part",["in-shartiyya","tawkid"],
      "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ وَ«قَدْ» لِلتَّحْقِيقِ.",
      "The fa ties the answer; «qad» affirms.",
      "Fâ cevabı bağlar; «قد» tahkik içindir."),
  tok("أَسْقَطَ","asqata","verb",["in-shartiyya","form-iv-verbs"],
      "جَوَابُ الشَّرْطِ — مَاضٍ فِي مَحَلِّ جَزْمٍ، مِنَ الْإِفْعَالِ.",
      "The answer — a past in jazm's position, Form IV.",
      "Şartın cevabı — mahallen meczum mâzî; if'âl bâbındandır."),
  tok("الْبَاقِيَ","baqi","noun",["maful-bihi","ism-maqsur-manqus","ism-fail"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ ظَاهِرَةٍ — مَنْقُوصٌ تَظْهَرُ فَتْحَتُهُ.",
      "The object in nasb — a manqus whose fatha shows plainly.",
      "Mensub mef'ûlün bih — menkûstur; fethası açıkça görünür.", punct="."),
 ],
 "jumal": [
  J("وَمَنْ صَالَحَ… فَقَدْ أَسْقَطَ…",
    "جُمْلَةُ شَرْطٍ: فِعْلُهَا وَجَوَابُهَا مَاضِيَانِ فِي مَحَلِّ جَزْمٍ — وَالْمَجْمُوعُ خَبَرُ «مَنْ».",
    "A conditional whose verb and answer are both pasts in jazm's position — together the khabar of «whoever».",
    "Şart cümlesi: fiili ve cevabı mahallen meczum iki mâzîdir — bütünü «من»in haberidir."),
 ]})

TITLE2 = {"ar": "أَنْوَاعُ الصُّلْحِ وَأَحْكَامُهَا",
          "en": "The Kinds of Sulh, and Their Rulings",
          "tr": "Sulhun Nevileri ve Hükümleri"}

GLOSS = {
 "sulh": {"lemma": "صُلْح", "root": "ص ل ح", "pos": "noun",
   "gloss": {"en": "sulh — amicable settlement", "tr": "sulh, barış"}, "level": 2},
 "aqd": {"lemma": "عَقْد", "root": "ع ق د", "pos": "noun", "plural": "عُقُود",
   "gloss": {"en": "contract", "tr": "akit"}, "level": 2},
 "rafaa": {"lemma": "رَفَعَ", "root": "ر ف ع", "pos": "verb", "form": "I",
   "gloss": {"en": "to lift, remove", "tr": "kaldırmak"}, "level": 2},
 "niza": {"lemma": "نِزَاع", "root": "ن ز ع", "pos": "noun",
   "gloss": {"en": "dispute (Form III masdar)", "tr": "nizâ, çekişme"}, "level": 3},
 "bayna": {"lemma": "بَيْنَ", "root": "ب ي ن", "pos": "noun",
   "gloss": {"en": "between (adverbial)", "tr": "arasında (zarf)"}, "level": 1},
 "mutakhasim": {"lemma": "مُتَخَاصِم", "root": "خ ص م", "pos": "noun",
   "gloss": {"en": "contending party (Form VI participle)", "tr": "çekişen taraf (tefâul ism-i fâili)"}, "level": 4},
 "qala": {"lemma": "قَالَ", "root": "ق و ل", "pos": "verb", "form": "I",
   "gloss": {"en": "to say", "tr": "demek, söylemek"}, "level": 1},
 "allah": {"lemma": "اللَّه", "pos": "propn", "gloss": {"en": "Allah", "tr": "Allah"}, "level": 0},
 "taala": {"lemma": "تَعَالَى", "root": "ع ل و", "pos": "verb", "form": "VI",
   "gloss": {"en": "to be exalted (said of Allah)", "tr": "yüce olmak (Allah hakkında)"}, "level": 2},
 "khayr": {"lemma": "خَيْر", "root": "خ ي ر", "pos": "noun",
   "gloss": {"en": "good; best", "tr": "hayır; daha hayırlı"}, "level": 1},
 "nabi": {"lemma": "نَبِيّ", "root": "ن ب أ", "pos": "noun", "plural": "أَنْبِيَاء",
   "gloss": {"en": "prophet", "tr": "nebî, peygamber"}, "level": 1},
 "alayhi": {"lemma": "عَلَيْهِ", "pos": "part",
   "gloss": {"en": "upon him", "tr": "onun üzerine"}, "level": 1},
 "salam": {"lemma": "سَلَام", "root": "س ل م", "pos": "noun",
   "gloss": {"en": "peace", "tr": "selâm"}, "level": 1},
 "jaiz": {"lemma": "جَائِز", "root": "ج و ز", "pos": "noun",
   "gloss": {"en": "permissible (ism fa'il of جَازَ)", "tr": "câiz"}, "level": 2},
 "muslim": {"lemma": "مُسْلِم", "root": "س ل م", "pos": "noun", "plural": "مُسْلِمُون",
   "gloss": {"en": "Muslim (Form IV participle)", "tr": "Müslüman"}, "level": 1},
 "illa": {"lemma": "إِلَّا", "pos": "part",
   "gloss": {"en": "except", "tr": "ancak, müstesnâ"}, "level": 1},
 "harrama": {"lemma": "حَرَّمَ", "root": "ح ر م", "pos": "verb", "form": "II",
   "gloss": {"en": "to forbid", "tr": "haram kılmak"}, "level": 2},
 "halal": {"lemma": "حَلَال", "root": "ح ل ل", "pos": "noun",
   "gloss": {"en": "the lawful", "tr": "helâl"}, "level": 1},
 "ahalla": {"lemma": "أَحَلَّ", "root": "ح ل ل", "pos": "verb", "form": "IV",
   "gloss": {"en": "to make lawful", "tr": "helâl kılmak"}, "level": 3},
 "haram": {"lemma": "حَرَام", "root": "ح ر م", "pos": "noun",
   "gloss": {"en": "the forbidden", "tr": "haram"}, "level": 1},
 "mandub": {"lemma": "مَنْدُوب", "root": "ن د ب", "pos": "noun",
   "gloss": {"en": "commended (ism maf'ul)", "tr": "mendup"}, "level": 3},
 "qadi": {"lemma": "قَاضٍ (الْقَاضِي)", "root": "ق ض ي", "pos": "noun", "plural": "قُضَاة",
   "gloss": {"en": "judge (a manqus ism fa'il)", "tr": "kadı, hâkim (menkûs ism-i fâil)"}, "level": 2},
 "raggaba": {"lemma": "رَغَّبَ", "root": "ر غ ب", "pos": "verb", "form": "II",
   "gloss": {"en": "to urge, make desirous (with في)", "tr": "teşvik etmek (في ile)"}, "level": 3},
 "fi": {"lemma": "فِي", "pos": "part", "gloss": {"en": "in", "tr": "içinde, -de"}, "level": 1},
 "khasm": {"lemma": "خَصْم", "root": "خ ص م", "pos": "noun", "plural": "خُصُوم",
   "gloss": {"en": "disputant, adversary", "tr": "hasım"}, "level": 3},
 "huwa": {"lemma": "هُوَ", "pos": "pron", "gloss": {"en": "he, it", "tr": "o"}, "level": 1},
 "thalatha": {"lemma": "ثَلَاثَة", "root": "ث ل ث", "pos": "noun",
   "gloss": {"en": "three (keeps its ta before a masculine noun)", "tr": "üç (müzekker ma'dûd önünde tâ'lı)"}, "level": 1},
 "naw": {"lemma": "نَوْع", "root": "ن و ع", "pos": "noun", "plural": "أَنْوَاع",
   "gloss": {"en": "kind, sort", "tr": "nevi, tür"}, "level": 2},
 "aw": {"lemma": "أَوْ", "pos": "part",
   "gloss": {"en": "or", "tr": "veya, yahut"}, "level": 1},
 "an-prep": {"lemma": "عَنْ", "pos": "part",
   "gloss": {"en": "from, upon (here: based on)", "tr": "-den; (burada) üzerine"}, "level": 1},
 "iqrar": {"lemma": "إِقْرَار", "root": "ق ر ر", "pos": "noun",
   "gloss": {"en": "acknowledgment (Form IV masdar)", "tr": "ikrar (if'âl masdarı)"}, "level": 3},
 "inkar": {"lemma": "إِنْكَار", "root": "ن ك ر", "pos": "noun",
   "gloss": {"en": "denial (Form IV masdar)", "tr": "inkâr (if'âl masdarı)"}, "level": 3},
 "sukut": {"lemma": "سُكُوت", "root": "س ك ت", "pos": "noun",
   "gloss": {"en": "silence", "tr": "sükût"}, "level": 3},
 "rukn": {"lemma": "رُكْن", "root": "ر ك ن", "pos": "noun", "plural": "أَرْكَان",
   "gloss": {"en": "pillar, essential element", "tr": "rükün"}, "level": 2},
 "ijab": {"lemma": "إِيجَاب", "root": "و ج ب", "pos": "noun",
   "gloss": {"en": "the offer (Form IV masdar of وَجَبَ)", "tr": "icap (وَجَبَ'nin if'âl masdarı)"}, "level": 3},
 "qabul": {"lemma": "قَبُول", "root": "ق ب ل", "pos": "noun",
   "gloss": {"en": "the acceptance", "tr": "kabul"}, "level": 2},
 "idha": {"lemma": "إِذَا", "pos": "part",
   "gloss": {"en": "when, whenever", "tr": "-dığı zaman"}, "level": 1},
 "ala": {"lemma": "عَلَى", "pos": "part",
   "gloss": {"en": "on, over", "tr": "üzerine, üzerinde"}, "level": 1},
 "la-nafiya": {"lemma": "لَا", "pos": "part",
   "gloss": {"en": "no; not", "tr": "hayır; değil"}, "level": 1},
 "laysa": {"lemma": "لَيْسَ", "root": "ل ي س", "pos": "verb", "form": "I",
   "gloss": {"en": "is not (conjugates in the past only)", "tr": "değildir (yalnız mâzîde çekilir)"}, "level": 2},
 "waqaa": {"lemma": "وَقَعَ", "root": "و ق ع", "pos": "verb", "form": "I",
   "gloss": {"en": "to fall, occur", "tr": "vâki olmak, düşmek"}, "level": 2},
 "mal": {"lemma": "مَال", "root": "م و ل", "pos": "noun", "plural": "أَمْوَال",
   "gloss": {"en": "property, wealth", "tr": "mal"}, "level": 1},
 "bay": {"lemma": "بَيْع", "root": "ب ي ع", "pos": "noun", "plural": "بُيُوع",
   "gloss": {"en": "sale", "tr": "satım, bey'"}, "level": 2},
 "manfaa": {"lemma": "مَنْفَعَة", "root": "ن ف ع", "pos": "noun", "plural": "مَنَافِع",
   "gloss": {"en": "usufruct, benefit", "tr": "menfaat"}, "level": 3},
 "ijara": {"lemma": "إِجَارَة", "root": "أ ج ر", "pos": "noun",
   "gloss": {"en": "hire, lease", "tr": "icâre, kira"}, "level": 3},
 "jawaza": {"lemma": "جَازَ", "root": "ج و ز", "pos": "verb", "form": "I",
   "gloss": {"en": "to be permissible", "tr": "câiz olmak"}, "level": 2},
 "ma-mawsula": {"lemma": "مَا (الْمَوْصُولَة)", "pos": "pron",
   "gloss": {"en": "that which (relative)", "tr": "şey ki (ism-i mevsûl)"}, "level": 3},
 "mutaqawwim": {"lemma": "مُتَقَوِّم", "root": "ق و م", "pos": "noun",
   "gloss": {"en": "lawful to use — of property (Form V participle)", "tr": "mütekavvim (intifaı mübah mal)"}, "level": 5},
 "khamr": {"lemma": "خَمْر", "root": "خ م ر", "pos": "noun",
   "gloss": {"en": "wine", "tr": "şarap, hamr"}, "level": 3},
 "qat": {"lemma": "قَطْع", "root": "ق ط ع", "pos": "noun",
   "gloss": {"en": "cutting off", "tr": "kesme, kat'"}, "level": 2},
 "khusuma": {"lemma": "خُصُومَة", "root": "خ ص م", "pos": "noun",
   "gloss": {"en": "litigation, quarrel", "tr": "husumet, dava"}, "level": 4},
 "man-shart": {"lemma": "مَنْ (الشَّرْطِيَّة)", "pos": "pron",
   "gloss": {"en": "whoever (conditional)", "tr": "her kim (şart)"}, "level": 2},
 "salaha": {"lemma": "صَالَحَ", "root": "ص ل ح", "pos": "verb", "form": "III",
   "gloss": {"en": "to make settlement with", "tr": "sulh yapmak, uzlaşmak"}, "level": 3},
 "baad": {"lemma": "بَعْض", "root": "ب ع ض", "pos": "noun",
   "gloss": {"en": "part, some", "tr": "bazı, kısım"}, "level": 2},
 "dayn": {"lemma": "دَيْن", "root": "د ي ن", "pos": "noun", "plural": "دُيُون",
   "gloss": {"en": "debt", "tr": "borç, deyn"}, "level": 3},
 "qad": {"lemma": "قَدْ", "pos": "part",
   "gloss": {"en": "indeed (with the past: completion)", "tr": "gerçekten (mâzî ile: tahkik)"}, "level": 2},
 "asqata": {"lemma": "أَسْقَطَ", "root": "س ق ط", "pos": "verb", "form": "IV",
   "gloss": {"en": "to drop, waive", "tr": "düşürmek, ıskat etmek"}, "level": 3},
 "baqi": {"lemma": "بَاقٍ (الْبَاقِي)", "root": "ب ق ي", "pos": "noun",
   "gloss": {"en": "the remainder (ism fa'il of بَقِيَ)", "tr": "bâkî, kalan"}, "level": 3},
}

MANIFEST = {
 "id": "kitab-al-sulh",
 "storyGroup": "kitab-al-sulh",
 "title": {"ar": "كِتَابُ الصُّلْحِ",
           "en": "The Book of Sulh",
           "tr": "Sulh Bahsi"},
 "subtitle": {"ar": "الصُّلْحُ: تَعْرِيفُهُ وَأَنْوَاعُهُ وَأَحْكَامُهُ، بِعَرَبِيَّةٍ مُيَسَّرَةٍ",
              "en": "Settlement in fiqh — definition, kinds and rulings, in graded original Arabic",
              "tr": "Fıkıhta sulh — tarifi, nevileri ve hükümleri, kolaylaştırılmış Arapçayla"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.2.0",
 "published": "2026-07-31",
 "access": "premium",
 "chapters": [{"n": 1, "title": TITLE1}, {"n": 2, "title": TITLE2}],
 "siblings": [],
 "attribution": {
  "ar": "عَرَبِيَّةٌ أَصْلِيَّةٌ مُيَسَّرَةٌ صِيغَتْ تَحْرِيرِيًّا مِنْ مَرْجِعٍ فِقْهِيٍّ تُرْكِيٍّ رَفَعَهُ صَاحِبُ الْمَشْرُوعِ.",
  "en": ("ORIGINAL graded Arabic, composed editorially from the project owner's uploaded Turkish fiqh "
         "reference on sulh (research/sources/sulh-fiqh-turkce.txt; Hanafi-centered, with classical "
         "citations). The Qur'anic clause (al-Nisa 4:128) and the hadith wording (Tirmidhi, Ahkam 17) "
         "are received text quoted as transmitted; all other Arabic is editorial composition in the "
         "Hidaya register and must not be cited as a classical text. Chapter 1 covers the definition, "
         "evidences, kinds and pillar; further chapters follow release by release."),
  "tr": ("ÖZGÜN kolaylaştırılmış Arapça; proje sahibinin yüklediği Türkçe sulh maddesinden "
         "(research/sources/sulh-fiqh-turkce.txt) editoryal olarak telif edilmiştir. Âyet iktibası "
         "(en-Nisâ 4/128) ve hadis lafzı (Tirmizî, Ahkâm 17) nakledilen metindir; diğer bütün Arapça, "
         "Hidâye üslûbunda editoryal telif olup klasik metin diye iktibas edilemez. 1. bölüm tarif, "
         "deliller, neviler ve rüknü kapsar; sonraki bölümler sürüm sürüm gelecektir."),
  "reviewStatus": "pending-scholarly-review"
 }
}

def copy_verbs():
    out = {}
    for lex, src in (("qala", "aqaid-ahl-al-sunna"),
                     ("taala", "wasiyyat-abi-hanifa-samti"),
                     ("laysa", "wasiyyat-abi-hanifa-samti")):
        verbs = json.loads((ROOT / "content/samples" / src / "morphology.json")
                           .read_text(encoding="utf-8"))["verbs"]
        out[lex] = verbs[lex]
    return out

MORPH = {"verbs": copy_verbs()}
MORPH["verbs"]["rafaa"] = _sg.sound1(
    "fataha", "رَفَع", "رْفَع", "اِرْفَع", "رَفْع", "رَافِع",
    "مَرْفُوع", "رُفِعَ", "يُرْفَعُ")
MORPH["verbs"]["harrama"] = _sg.derived(
    _sg.B2, _sg.W2, "ُ", "حَرَّم", "حَرِّم", "حَرِّم", "تَحْرِيم",
    "مُحَرِّم", "مُحَرَّم", "حُرِّمَ", "يُحَرَّمُ")
MORPH["verbs"]["raggaba"] = _sg.derived(
    _sg.B2, _sg.W2, "ُ", "رَغَّب", "رَغِّب", "رَغِّب", "تَرْغِيب",
    "مُرَغِّب", "مُرَغَّب", "رُغِّبَ", "يُرَغَّبُ")
# أَحَلَّ — Form IV geminate, assembled like the corpus's اِسْتَعَدَّ:
# contracted stem before vowels, broken stem before consonants.
MORPH["verbs"]["ahalla"] = _sg.entry(
    "بَابُ الْإِفْعَالِ: أَفْعَلَ يُفْعِلُ — مُضَاعَفٌ", _sg.W4,
    "إِحْلَال", "مُحِلّ",
    _sg.mazi14("أَحَلّ", "أَحْلَل"),
    _sg.mudari14("ُ", "حِلّ", "حْلِل"),
    ["أَحِلَّ", "أَحِلَّا", "أَحِلُّوا", "أَحِلِّي", "أَحِلَّا", "أَحْلِلْنَ"],
    "يُحِلَّ", "يُحِلَّ", "تُحِلَّ",
    "مُحَلّ", "أُحِلَّ", "يُحَلُّ",
    "مُضَاعَفٌ مِنَ الْإِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُحِلَّ، وَيَجُوزُ لَمْ يُحْلِلْ.")
# chapter 2's verbs: وَقَعَ rides the mithal shapes (waw drops in the mudari),
# جَازَ the hollow engine, صَالَحَ and أَسْقَطَ the derived engines.
MORPH["verbs"]["waqaa"] = _sg.sound1(
    "fataha", "وَقَع", "قَع", "قَع", "وُقُوع", "وَاقِع",
    note="مِثَالٌ وَاوِيٌّ: تَسْقُطُ الْوَاوُ فِي الْمُضَارِعِ وَالْأَمْرِ — يَقَعُ، قَعْ.")
MORPH["verbs"]["jawaza"] = _sg.hollow1(
    "nasara", "أَجْوَفُ وَاوِيٌّ", "جَاز", "جُز", "جُوز", "جُز",
    "جُوز", "جُز", "جَوَاز", "جَائِز",
    note=_sg.HOLLOW_NOTE.format(ex="جُزْتَ"))
MORPH["verbs"]["salaha"] = _sg.derived(
    _sg.B3, _sg.W3, "ُ", "صَالَح", "صَالِح", "صَالِح", "مُصَالَحَة",
    "مُصَالِح", "مُصَالَح", "صُولِحَ", "يُصَالَحُ")
MORPH["verbs"]["asqata"] = _sg.derived(
    _sg.B4, _sg.W4, "ُ", "أَسْقَط", "سْقِط", "أَسْقِط", "إِسْقَاط",
    "مُسْقِط", "مُسْقَط", "أُسْقِطَ", "يُسْقَطُ")

ALL = S + S2

(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "chapters/1.json").write_text(json.dumps({"chapter": 1, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "chapters/2.json").write_text(json.dumps({"chapter": 2, "sentences": S2}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")

used = {t["lex"] for s in ALL for t in s["tokens"]}
dead = set(GLOSS) - used
missing = used - set(GLOSS)
print("tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS),
      "jumal:", sum(len(s.get("jumal", [])) for s in ALL),
      "dead:", sorted(dead), "missing:", sorted(missing))
