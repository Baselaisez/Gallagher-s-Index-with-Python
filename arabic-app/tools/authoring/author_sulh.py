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
 "version": "0.1.0",
 "published": "2026-07-31",
 "access": "premium",
 "chapters": [{"n": 1, "title": TITLE1}],
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
                     ("taala", "wasiyyat-abi-hanifa-samti")):
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

ALL = S

(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "chapters/1.json").write_text(json.dumps({"chapter": 1, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")

used = {t["lex"] for s in ALL for t in s["tokens"]}
dead = set(GLOSS) - used
missing = used - set(GLOSS)
print("tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS),
      "jumal:", sum(len(s.get("jumal", [])) for s in ALL),
      "dead:", sorted(dead), "missing:", sorted(missing))
