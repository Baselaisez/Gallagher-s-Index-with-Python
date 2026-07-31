# -*- coding: utf-8 -*-
"""Author content/samples/kitab-al-waqf — the Waqf story.

ORIGINAL graded Arabic, composed editorially from the user's uploaded
Turkish sohbet on waqf property (research/sources/vakif-mali-turkce.txt).
The classical definition follows the Hanafi books (Hidaya register) and
the closing maxim — شَرْطُ الْوَاقِفِ كَنَصِّ الشَّارِعِ — is the
madrasah's received qaida; everything is marked pending-scholarly-review.
Verb paradigms ride the same audited engines as the rest of the corpus.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PKG = ROOT / "content/samples/kitab-al-waqf"
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
 "en": "Waqf is confining the thing itself to the ownership of Allah the Exalted, and directing its benefit to His servants.",
 "tr": "Vakıf, aynın kendisini Allah Teâlâ'nın mülkü üzere hapsetmek ve menfaatini O'nun kullarına yöneltmektir."},
 "tokens": [
  tok("الْوَقْفُ","waqf","noun",["mubtada-khabar","masdar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ وَقَفَ.",
      "The mubtada in raf' — the masdar of «to confine».",
      "Merfû mübteda — وَقَفَ'nin masdarıdır."),
  tok("حَبْسُ","habs","noun",["mubtada-khabar","masdar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — تَعْرِيفُ الْحَنَفِيَّةِ.",
      "The khabar in raf', mudaf — the Hanafi definition.",
      "Merfû haber; muzâf — Hanefîlerin tarifidir."),
  tok("الْعَيْنِ","ayn-waqf","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.","Mudaf ilayh in jarr.","Mecrur muzâfun ileyhtir."),
  tok("عَلَى","ala","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("مِلْكِ","milk","noun",["huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ.","In jarr, mudaf.","Mecrur isim; muzâftır."),
  tok("اللَّهِ","allah","propn",["idafa-definiteness"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The name of majesty, mudaf ilayh in jarr.",
      "Lafza-i celâl; mecrur muzâfun ileyhtir."),
  tok("تَعَالَى","taala","verb",["fail","naqis-verbs"],
      "مَاضٍ لِلتَّعْظِيمِ وَالْفَاعِلُ مُسْتَتِرٌ.",
      "A past verb of exaltation, agent hidden.",
      "Ta'zîm için mâzî; fâili gizlidir.", punct="•"),
  tok("وَصَرْفُ","sarf-direct","noun",["atf-nasaq","masdar","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «حَبْسُ» مَرْفُوعٌ مُضَافٌ.",
      "Joined to «confining», in raf', mudaf.",
      "«حبس»e matuf; merfû ve muzâftır."),
  tok("مَنْفَعَتِهَا","manfaa-waqf","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَ«هَا» مُضَافٌ إِلَيْهِ ثَانٍ.",
      "Mudaf ilayh in jarr, «its» a second mudaf ilayh.",
      "Mecrur muzâfun ileyh; «ها» ikinci muzâfun ileyhtir."),
  tok("إِلَى","ila-waqf","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("عِبَادِهِ","ibad","noun",["huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ — جَمْعُ «عَبْد» — وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr — the plural of «servant» — the ha its mudaf ilayh.",
      "Mecrur isim — «عبد»in cem'i — hâ, muzâfun ileyhtir.", punct="."),
 ],
 "jumal": [
  J("الْوَقْفُ حَبْسُ الْعَيْنِ…",
    "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ — لَا مَحَلَّ لَهَا.",
    "An opening nominal clause — i'rabless.",
    "İbtidâiyye isim cümlesi — mahalsizdir."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "So when a man endows his land, it leaves his ownership and its sale is no longer permitted.",
 "tr": "Bir kimse arazisini vakfedince, arazi onun mülkünden çıkar ve artık satışı câiz olmaz."},
 "tokens": [
  tok("فَإِذَا","idha","part",["idha-shartiyya"],
      "الْفَاءُ لِلتَّفْرِيعِ وَ«إِذَا» ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "The fa branches; «idha» a conditional adverbial.",
      "Tefrî' fâsı; «إذا» şart mânalı zarftır."),
  tok("وَقَفَ","waqafa","verb",["idha-shartiyya","fail","mithal-verbs"],
      "فِعْلُ الشَّرْطِ — مِثَالٌ وَاوِيٌّ.",
      "The condition verb — a waw-initial verb.",
      "Şart fiili — misâl-i vâvîdir."),
  tok("الرَّجُلُ","rajul","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.","The fa'il in raf'.","Merfû fâildir."),
  tok("أَرْضَهُ","ard","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "The object in nasb, the ha its mudaf ilayh.",
      "Mensub mef'ûlün bih; hâ, muzâfun ileyhtir."),
  tok("خَرَجَتْ","kharaja","verb",["idha-shartiyya","fail"],
      "جَوَابُ «إِذَا» — مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ وَالْفَاعِلُ مُسْتَتِرٌ.",
      "Idha's answer — past, the ta marking the feminine, agent hidden.",
      "«إذا»nın cevabı — mâzî; tâ, te'nis içindir; fâili gizlidir."),
  tok("عَنْ","an-prep","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("مِلْكِهِ","milk","noun",["huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr, the ha its mudaf ilayh.",
      "Mecrur isim; hâ, muzâfun ileyhtir.", punct="•"),
  tok("فَلَا","la-nafiya","part",[],
      "الْفَاءُ عَاطِفَةٌ وَ«لَا» نَافِيَةٌ.",
      "The fa joins; «la» negates.",
      "Atıf fâsı; «لا» nâfiyedir."),
  tok("يَجُوزُ","jawaza","verb",["fail","hollow-verbs","mudari-marfu"],
      "مُضَارِعٌ مَرْفُوعٌ.","A mudari' in raf'.","Merfû muzâridir."),
  tok("بَيْعُهَا","bay-waqf","noun",["fail","idafa-definiteness","masdar"],
      "فَاعِلٌ مَرْفُوعٌ وَ«هَا» مُضَافٌ إِلَيْهِ.",
      "The fa'il in raf', «its» the mudaf ilayh.",
      "Merfû fâil; «ها» muzâfun ileyhtir.", punct="."),
 ],
 "jumal": [
  J("فَإِذَا وَقَفَ… خَرَجَتْ…",
    "جُمْلَةُ شَرْطٍ غَيْرِ جَازِمٍ وَجَوَابُهَا.",
    "A non-jazm conditional and its answer.",
    "Cezmetmeyen şart cümlesi ve cevabıdır."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And whoever uses the waqf against what it was endowed for has wronged — nay, it is theft.",
 "tr": "Kim vakfı, vakfedildiği amacın dışında kullanırsa zulmetmiştir — hattâ bu, hırsızlıktır."},
 "tokens": [
  tok("وَمَنِ","man-shart","pron",["in-shartiyya"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ وَ«مَنْ» شَرْطِيَّةٌ مُبْتَدَأٌ.",
      "The waw resumes; conditional «whoever», a mubtada.",
      "İsti'nâf vâvı; şart «من»i, mübtedadır."),
  tok("اسْتَعْمَلَ","istamala","verb",["in-shartiyya","fail","form-x-verbs"],
      "فِعْلُ الشَّرْطِ — مَاضِي الِاسْتِفْعَالِ فِي مَحَلِّ جَزْمٍ.",
      "The condition verb — the Form X past in jazm position.",
      "Şart fiili — istif'âlin mâzîsi; mahallen meczumdur."),
  tok("الْوَقْفَ","waqf","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.","The object in nasb.","Mensub mef'ûlün bihtir."),
  tok("فِي","fi","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.","A jarr particle.","Cer harfidir."),
  tok("غَيْرِ","ghayr","noun",["huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ.","In jarr, mudaf.","Mecrur isim; muzâftır."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","idafa-definiteness"],
      "«مَا» مَوْصُولَةٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.",
      "Relative «ma», mudaf ilayh in jarr position.",
      "İsm-i mevsûl «ما»; mahallen mecrur muzâfun ileyhtir."),
  tok("وُقِفَ","waqafa","verb",["naib-al-fail","ism-mawsul","mithal-verbs"],
      "مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةُ «مَا».",
      "A passive past, its deputy fa'il hidden — the clause ma's sila.",
      "Meçhul mâzî; nâib-i fâili gizli — cümle, «ما»nın sılasıdır."),
  tok("لَهُ","lahu-waqf","part",["huruf-jarr"],
      "اللَّامُ جَارَّةٌ وَالْهَاءُ مَجْرُورٌ.",
      "The lam governs the ha.",
      "Lâm cer harfi; hâ mecrurdur."),
  tok("فَقَدْ","qad","part",["qad-harf","in-shartiyya"],
      "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ وَ«قَدْ» لِلتَّحْقِيقِ.",
      "The fa binds the answer; «qad» for certainty.",
      "Cevabı bağlayan fâ; «قد» tahkik içindir."),
  tok("ظَلَمَ","zalama","verb",["in-shartiyya","fail"],
      "مَاضٍ وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.",
      "A past verb, agent hidden — the clause the condition's answer, in jazm position.",
      "Mâzî; fâili gizli — cümle, şartın cevabı olarak mahallen meczumdur.", punct="•"),
  tok("بَلْ","bal","part",["huruf-tanbih"],
      "«بَلْ» لِلْإِضْرَابِ الِانْتِقَالِيِّ.",
      "«Bal» — turning to the stronger word.",
      "«بل» — daha ağırına geçiş (ıdrâb) içindir."),
  tok("هُوَ","huwa-waqf","pron",["mubtada-khabar"],
      "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.",
      "A mubtada in raf' position.",
      "Mahallen merfû mübtedadır."),
  tok("سَرِقَةٌ","sariqa","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.","The khabar in raf'.","Merfû haberdir.", punct="."),
 ],
 "jumal": [
  J("وَمَنِ اسْتَعْمَلَ… فَقَدْ ظَلَمَ",
    "جُمْلَةُ شَرْطٍ — وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُ «مَنْ».",
    "A conditional — condition and answer together the khabar of «whoever».",
    "Şart cümlesi — şart ve cevap birlikte «من»in haberidir."),
  J("بَلْ هُوَ سَرِقَةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ بَعْدَ «بَلْ» — لَا مَحَلَّ لَهَا.",
    "A nominal clause after «bal» — i'rabless.",
    "«بل»den sonra isim cümlesi — mahalsizdir."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "Its seller is in sin, and its buyer is in sin: the wrong does not become lawful by passing from hand to hand.",
 "tr": "Onu satan günahtadır, alan da günahtadır: haksızlık elden ele geçmekle helâl olmaz."},
 "tokens": [
  tok("وَبَائِعُهُ","bai","noun",["mubtada-khabar","ism-fail","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ وَ«بَائِعُ» مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "The waw joins; «its seller» a mubtada in raf' — a participle — the ha its mudaf ilayh.",
      "Atıf vâvı; «بائع» merfû mübteda — ism-i fâil — hâ, muzâfun ileyhtir."),
  tok("آثِمٌ","athim","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ أَثِمَ.",
      "The khabar in raf' — the participle of «to sin».",
      "Merfû haber — أَثِمَ'nin ism-i fâilidir."),
  tok("وَمُشْتَرِيهِ","mushtari","noun",["atf-nasaq","mubtada-khabar","ism-fail","ism-maqsur-manqus","idafa-definiteness"],
      "مَعْطُوفٌ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — اسْمُ فَاعِلِ الِافْتِعَالِ، مَنْقُوصٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joined; «its buyer» a mubtada in raf' by an assumed damma — the Form VIII participle, manqus — the ha its mudaf ilayh.",
      "Matuf; «مشتري» takdîrî zamme ile merfû mübteda — iftiâlin ism-i fâili, menkus — hâ, muzâfun ileyhtir."),
  tok("آثِمٌ","athim","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.","The khabar in raf'.","Merfû haberdir.", punct="•"),
  tok("فَالظُّلْمُ","zulm","noun",["mubtada-khabar","masdar"],
      "الْفَاءُ لِلتَّعْلِيلِ وَ«الظُّلْمُ» مُبْتَدَأٌ.",
      "The fa gives the reason; «wrong» a mubtada.",
      "Ta'lîl fâsı; «الظلم» mübtedadır."),
  tok("لَا","la-nafiya","part",[],
      "«لَا» نَافِيَةٌ.","The negating «la».","Nefiy «لا»sıdır."),
  tok("يَحِلُّ","halla-lawful","verb",["fail","doubled-verbs","mudari-marfu"],
      "مُضَارِعٌ مَرْفُوعٌ — مُضَاعَفٌ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.",
      "A mudari' in raf' — geminate — the clause the mubtada's khabar.",
      "Merfû muzâri — muzâaf — cümle, mübtedanın haberidir."),
  tok("بِتَدَاوُلِ","tadawul","noun",["huruf-jarr","masdar","form-vi-verbs","idafa-definiteness"],
      "الْبَاءُ سَبَبِيَّةٌ وَ«تَدَاوُلِ» مَجْرُورٌ مُضَافٌ — مَصْدَرُ التَّفَاعُلِ.",
      "The ba of cause; «passing around» in jarr, mudaf — the Form VI masdar.",
      "Sebep bildiren بِ; «تداول» mecrur ve muzâf — tefâulün masdarıdır."),
  tok("الْأَيْدِي","yad-waqf","noun",["idafa-definiteness","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — جَمْعُ «يَد»، مَنْقُوصٌ.",
      "Mudaf ilayh in jarr by an assumed kasra — the plural of «hand», manqus.",
      "Takdîrî kesreyle mecrur muzâfun ileyh — «يد»in cem'i, menkustur.", punct="."),
 ],
 "jumal": [
  J("وَبَائِعُهُ آثِمٌ وَمُشْتَرِيهِ آثِمٌ",
    "جُمْلَتَانِ اسْمِيَّتَانِ مُتَعَاطِفَتَانِ.",
    "Two nominal clauses, joined.",
    "Birbirine matuf iki isim cümlesidir."),
  J("فَالظُّلْمُ لَا يَحِلُّ…",
    "جُمْلَةٌ اسْمِيَّةٌ لِلتَّعْلِيلِ؛ خَبَرُهَا جُمْلَةُ «لَا يَحِلُّ».",
    "A nominal clause giving the reason; its khabar the la-yahillu clause.",
    "Ta'lîl için isim cümlesi; haberi «لا يحلّ» cümlesidir."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "So preserve the waqf, and honor its founder's stipulation — for the founder's stipulation is like the Lawgiver's text.",
 "tr": "Öyleyse vakfı koru ve vakfedenin şartına hürmet et — çünkü vakfedenin şartı, Şâri'in nassı gibidir."},
 "tokens": [
  tok("فَاحْفَظِ","hafiza","verb",["imperative-amr","fail"],
      "الْفَاءُ لِلتَّفْرِيعِ وَ«احْفَظْ» أَمْرٌ مَبْنِيٌّ عَلَى السُّكُونِ — كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْفَاعِلُ أَنْتَ.",
      "The fa branches; «preserve!» an imperative on sukun — kasra where two sukuns meet — its agent «you».",
      "Tefrî' fâsı; «احفظ» sükûn üzere mebnî emir — iki sâkin buluşunca kesre almıştır — fâili «sen»dir."),
  tok("الْوَقْفَ","waqf","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.","The object in nasb.","Mensub mef'ûlün bihtir."),
  tok("وَاحْتَرِمْ","ihtarama","verb",["atf-nasaq","imperative-amr","fail","form-viii-verbs"],
      "مَعْطُوفٌ — أَمْرُ الِافْتِعَالِ وَالْفَاعِلُ أَنْتَ.",
      "Joined — the Form VIII imperative, its agent «you».",
      "Matuf — iftiâlin emri; fâili «sen»dir."),
  tok("شَرْطَ","shart-waqf","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ.",
      "The object in nasb, mudaf.",
      "Mensub mef'ûlün bih; muzâftır."),
  tok("الْوَاقِفِ","waqif","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ.",
      "Mudaf ilayh in jarr — an active participle.",
      "Mecrur muzâfun ileyh — ism-i fâildir.", punct="•"),
  tok("فَإِنَّ","inna-waqf","part",["inna-wa-akhawatuha"],
      "الْفَاءُ لِلتَّعْلِيلِ وَ«إِنَّ» تَنْصِبُ الِاسْمَ وَتَرْفَعُ الْخَبَرَ.",
      "The fa gives the reason; «inna» — nasb on its noun, raf' on its khabar.",
      "Ta'lîl fâsı; «إنّ» ismini nasb, haberini raf eder."),
  tok("شَرْطَ","shart-waqf","noun",["inna-wa-akhawatuha","idafa-definiteness"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ مُضَافٌ.",
      "Inna's noun in nasb, mudaf.",
      "«إنّ»nin ismi; mensub ve muzâftır."),
  tok("الْوَاقِفِ","waqif","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.","Mudaf ilayh in jarr.","Mecrur muzâfun ileyhtir."),
  tok("كَنَصِّ","nass","noun",["huruf-jarr","tashbih","idafa-definiteness","inna-wa-akhawatuha"],
      "الْكَافُ لِلتَّشْبِيهِ — وَالْجَارُّ خَبَرُ «إِنَّ» — وَ«نَصِّ» مَجْرُورٌ مُضَافٌ.",
      "The kaf of likening — the phrase inna's khabar — «the text» in jarr, mudaf.",
      "Teşbih kâfı — câr, «إنّ»nin haberidir — «نصّ» mecrur ve muzâftır."),
  tok("الشَّارِعِ","shari","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الشَّارِعُ: صَاحِبُ الشَّرْعِ.",
      "Mudaf ilayh in jarr — the Lawgiver.",
      "Mecrur muzâfun ileyh — Şâri': şeriatın sahibidir.", punct="."),
 ],
 "jumal": [
  J("فَاحْفَظِ الْوَقْفَ وَاحْتَرِمْ…",
    "جُمْلَتَا أَمْرٍ مُتَعَاطِفَتَانِ — لَا مَحَلَّ لَهُمَا.",
    "Two joined imperative clauses — i'rabless.",
    "Birbirine matuf iki emir cümlesi — mahalsizdir."),
  J("فَإِنَّ شَرْطَ الْوَاقِفِ كَنَصِّ الشَّارِعِ",
    "جُمْلَةُ «إِنَّ» لِلتَّعْلِيلِ — الْقَاعِدَةُ الْمَشْهُورَةُ.",
    "The inna-clause of reason — the famous qaida.",
    "Ta'lîl için «إنّ» cümlesi — meşhur kaidedir."),
 ]})

TITLE1 = {"ar": "الْوَقْفُ وَحُرْمَتُهُ",
          "en": "Waqf and Its Inviolability",
          "tr": "Vakıf ve Dokunulmazlığı"}

GLOSS = {
 "waqf": {"lemma": "وَقْف", "root": "و ق ف", "pos": "noun", "plural": "أَوْقَاف",
   "gloss": {"en": "waqf — endowment", "tr": "vakıf"}, "level": 3},
 "habs": {"lemma": "حَبْس", "root": "ح ب س", "pos": "noun",
   "gloss": {"en": "confining (masdar)", "tr": "hapsetme, alıkoyma (masdar)"}, "level": 4},
 "ayn-waqf": {"lemma": "عَيْن", "root": "ع ي ن", "pos": "noun", "plural": "أَعْيَان",
   "gloss": {"en": "the thing itself (fiqh)", "tr": "ayn — şeyin kendisi (fıkıh)"}, "level": 4},
 "ala": {"lemma": "عَلَى", "pos": "prep",
   "gloss": {"en": "upon", "tr": "üzerine"}, "level": 1},
 "milk": {"lemma": "مِلْك", "root": "م ل ك", "pos": "noun", "plural": "أَمْلَاك",
   "gloss": {"en": "ownership", "tr": "mülk"}, "level": 2},
 "allah": {"lemma": "اللَّه", "pos": "propn",
   "gloss": {"en": "Allah", "tr": "Allah"}, "level": 0},
 "taala": {"lemma": "تَعَالَى", "root": "ع ل و", "pos": "verb", "form": "VI",
   "gloss": {"en": "He is exalted", "tr": "yücedir, teâlâ"}, "level": 2},
 "sarf-direct": {"lemma": "صَرْف", "root": "ص ر ف", "pos": "noun",
   "gloss": {"en": "directing, disbursing (masdar)", "tr": "sarf etme, yöneltme (masdar)"}, "level": 3},
 "manfaa-waqf": {"lemma": "مَنْفَعَة", "root": "ن ف ع", "pos": "noun", "plural": "مَنَافِع",
   "gloss": {"en": "benefit, use", "tr": "menfaat"}, "level": 3},
 "ila-waqf": {"lemma": "إِلَى", "pos": "prep",
   "gloss": {"en": "to, toward", "tr": "-e doğru"}, "level": 1},
 "ibad": {"lemma": "عِبَاد", "root": "ع ب د", "pos": "noun",
   "gloss": {"en": "servants (of Allah)", "tr": "kullar"}, "level": 2},
 "idha": {"lemma": "إِذَا", "pos": "part",
   "gloss": {"en": "when, whenever", "tr": "-diği zaman, -ince"}, "level": 2},
 "waqafa": {"lemma": "وَقَفَ", "root": "و ق ف", "pos": "verb", "form": "I",
   "gloss": {"en": "to endow as waqf; to stop", "tr": "vakfetmek; durmak"}, "level": 3},
 "rajul": {"lemma": "رَجُل", "root": "ر ج ل", "pos": "noun", "plural": "رِجَال",
   "gloss": {"en": "man", "tr": "adam, kişi"}, "level": 1},
 "ard": {"lemma": "أَرْض", "root": "أ ر ض", "pos": "noun", "plural": "أَرَاضٍ",
   "gloss": {"en": "land, earth", "tr": "arazi, yer"}, "level": 1},
 "kharaja": {"lemma": "خَرَجَ", "root": "خ ر ج", "pos": "verb", "form": "I",
   "gloss": {"en": "to leave, go out", "tr": "çıkmak"}, "level": 1},
 "an-prep": {"lemma": "عَنْ", "pos": "prep",
   "gloss": {"en": "from, away from", "tr": "-den"}, "level": 1},
 "la-nafiya": {"lemma": "لَا", "pos": "part",
   "gloss": {"en": "not", "tr": "değil, -mez"}, "level": 1},
 "jawaza": {"lemma": "جَازَ", "root": "ج و ز", "pos": "verb", "form": "I",
   "gloss": {"en": "to be permitted", "tr": "câiz olmak"}, "level": 2},
 "bay-waqf": {"lemma": "بَيْع", "root": "ب ي ع", "pos": "noun", "plural": "بُيُوع",
   "gloss": {"en": "sale (masdar)", "tr": "satış, bey' (masdar)"}, "level": 2},
 "man-shart": {"lemma": "مَنْ (الشَّرْطِيَّة)", "pos": "pron",
   "gloss": {"en": "whoever (conditional)", "tr": "her kim (şart)"}, "level": 2},
 "istamala": {"lemma": "اِسْتَعْمَلَ", "root": "ع م ل", "pos": "verb", "form": "X",
   "gloss": {"en": "to use", "tr": "kullanmak"}, "level": 3},
 "fi": {"lemma": "فِي", "pos": "prep",
   "gloss": {"en": "in", "tr": "içinde, -de"}, "level": 1},
 "ghayr": {"lemma": "غَيْر", "root": "غ ي ر", "pos": "noun",
   "gloss": {"en": "other than", "tr": "gayrı, başkası"}, "level": 2},
 "ma-mawsula": {"lemma": "مَا (الْمَوْصُولَة)", "pos": "pron",
   "gloss": {"en": "that which (relative)", "tr": "şey ki (ism-i mevsûl)"}, "level": 3},
 "lahu-waqf": {"lemma": "لَهُ", "pos": "part",
   "gloss": {"en": "for it", "tr": "onun için"}, "level": 1},
 "qad": {"lemma": "قَدْ", "pos": "part",
   "gloss": {"en": "indeed (with the past)", "tr": "gerçekten (mâzî ile)"}, "level": 2},
 "zalama": {"lemma": "ظَلَمَ", "root": "ظ ل م", "pos": "verb", "form": "I",
   "gloss": {"en": "to wrong", "tr": "zulmetmek"}, "level": 2},
 "bal": {"lemma": "بَلْ", "pos": "part",
   "gloss": {"en": "nay, rather", "tr": "hattâ, bilakis"}, "level": 3},
 "huwa-waqf": {"lemma": "هُوَ", "pos": "pron",
   "gloss": {"en": "he, it", "tr": "o"}, "level": 1},
 "sariqa": {"lemma": "سَرِقَة", "root": "س ر ق", "pos": "noun",
   "gloss": {"en": "theft", "tr": "hırsızlık"}, "level": 3},
 "bai": {"lemma": "بَائِع", "root": "ب ي ع", "pos": "noun",
   "gloss": {"en": "seller (ism fa'il)", "tr": "satıcı, bâyi' (ism-i fâil)"}, "level": 3},
 "athim": {"lemma": "آثِم", "root": "أ ث م", "pos": "noun",
   "gloss": {"en": "sinning, in sin (ism fa'il)", "tr": "günahkâr (ism-i fâil)"}, "level": 4},
 "mushtari": {"lemma": "مُشْتَرٍ (الْمُشْتَرِي)", "root": "ش ر ي", "pos": "noun",
   "gloss": {"en": "buyer (Form VIII ism fa'il)", "tr": "alıcı, müşteri (iftiâl ism-i fâili)"}, "level": 3},
 "zulm": {"lemma": "ظُلْم", "root": "ظ ل م", "pos": "noun",
   "gloss": {"en": "wrong, injustice", "tr": "zulüm"}, "level": 2},
 "halla-lawful": {"lemma": "حَلَّ", "root": "ح ل ل", "pos": "verb", "form": "I",
   "gloss": {"en": "to become lawful", "tr": "helâl olmak"}, "level": 3},
 "tadawul": {"lemma": "تَدَاوُل", "root": "د و ل", "pos": "noun",
   "gloss": {"en": "passing from hand to hand (Form VI masdar)", "tr": "tedâvül, elden ele geçme (tefâul masdarı)"}, "level": 5},
 "yad-waqf": {"lemma": "يَد", "root": "ي د ي", "pos": "noun", "plural": "أَيْدٍ",
   "gloss": {"en": "hand", "tr": "el"}, "level": 1},
 "hafiza": {"lemma": "حَفِظَ", "root": "ح ف ظ", "pos": "verb", "form": "I",
   "gloss": {"en": "to preserve, guard", "tr": "korumak, hıfzetmek"}, "level": 2},
 "ihtarama": {"lemma": "اِحْتَرَمَ", "root": "ح ر م", "pos": "verb", "form": "VIII",
   "gloss": {"en": "to honor, respect", "tr": "hürmet etmek"}, "level": 3},
 "shart-waqf": {"lemma": "شَرْط", "root": "ش ر ط", "pos": "noun", "plural": "شُرُوط",
   "gloss": {"en": "stipulation", "tr": "şart"}, "level": 2},
 "waqif": {"lemma": "وَاقِف", "root": "و ق ف", "pos": "noun",
   "gloss": {"en": "the founder of the waqf (ism fa'il)", "tr": "vâkıf — vakfeden (ism-i fâil)"}, "level": 4},
 "inna-waqf": {"lemma": "إِنَّ", "pos": "part",
   "gloss": {"en": "indeed (governs its clause)", "tr": "muhakkak (cümlesine amel eder)"}, "level": 1},
 "nass": {"lemma": "نَصّ", "root": "ن ص ص", "pos": "noun", "plural": "نُصُوص",
   "gloss": {"en": "text (of the Law)", "tr": "nas — şer'î metin"}, "level": 4},
 "shari": {"lemma": "شَارِع", "root": "ش ر ع", "pos": "noun",
   "gloss": {"en": "the Lawgiver (ism fa'il)", "tr": "Şâri' — şeriat koyan (ism-i fâil)"}, "level": 5},
}

MANIFEST = {
 "id": "kitab-al-waqf",
 "storyGroup": "kitab-al-waqf",
 "title": {"ar": "كِتَابُ الْوَقْفِ",
           "en": "The Book of Waqf",
           "tr": "Vakıf Bahsi"},
 "subtitle": {"ar": "الْوَقْفُ: تَعْرِيفُهُ وَحُرْمَتُهُ، بِعَرَبِيَّةٍ مُيَسَّرَةٍ",
              "en": "The endowment — its definition and inviolability, in graded original Arabic",
              "tr": "Vakıf — tarifi ve dokunulmazlığı, kolaylaştırılmış Arapçayla"},
 "level": 4,
 "levelName": "Upper Intermediate",
 "version": "0.1.0",
 "published": "2026-07-31",
 "access": "premium",
 "chapters": [{"n": 1, "title": TITLE1}],
 "siblings": [],
 "attribution": {
  "ar": "عَرَبِيَّةٌ أَصْلِيَّةٌ مُيَسَّرَةٌ صِيغَتْ تَحْرِيرِيًّا مِنْ سُؤَالٍ وَجَوَابٍ تُرْكِيٍّ عَنِ الْوَقْفِ رَفَعَهُ صَاحِبُ الْمَشْرُوعِ.",
  "en": ("ORIGINAL graded Arabic, composed editorially from the project owner's uploaded Turkish "
         "question-and-answer on waqf property (research/sources/vakif-mali-turkce.txt). The Hanafi "
         "definition of waqf and the maxim شَرْطُ الْوَاقِفِ كَنَصِّ الشَّارِعِ are the madrasah's "
         "received doctrine, supplied editorially in the Hidaya register; no sentence here may be "
         "cited as a classical text. Chapter 1 covers the definition and inviolability; further "
         "chapters follow release by release."),
  "tr": ("ÖZGÜN kolaylaştırılmış Arapça; proje sahibinin yüklediği Türkçe vakıf sohbetinden "
         "(research/sources/vakif-mali-turkce.txt) editoryal olarak telif edilmiştir. Vakfın Hanefî "
         "tarifi ve «vâkıfın şartı Şâri'in nassı gibidir» kaidesi medresenin gelen doktrini olup "
         "Hidâye üslûbunda editoryal olarak verilmiştir; buradaki hiçbir cümle klasik metin diye "
         "iktibas edilemez. 1. bölüm tarif ve dokunulmazlığı kapsar; sonraki bölümler sürüm sürüm "
         "gelecektir."),
  "reviewStatus": "pending-scholarly-review"
 }
}

# paradigms: copied where the corpus already owns the verb, engine-built
# for the newcomers. istamala lives in the Samti package; jawaza and
# taala in the Sulh package (jawaza engine-built there, taala copied).
def copy_verbs():
    out = {}
    for lex, src in (("istamala", "wasiyyat-abi-hanifa-samti"),
                     ("jawaza", "kitab-al-sulh"),
                     ("taala", "kitab-al-sulh")):
        verbs = json.loads((ROOT / "content/samples" / src / "morphology.json")
                           .read_text(encoding="utf-8"))["verbs"]
        out[lex] = verbs[lex]
    return out

MORPH = {"verbs": copy_verbs()}
# وَقَفَ — mithal waw of bab daraba: the waw drops in the mudari (يَقِفُ).
MORPH["verbs"]["waqafa"] = _sg.sound1(
    "daraba", "وَقَف", "قِف", "قِف", "وَقْف", "وَاقِف",
    "مَوْقُوف", "وُقِفَ", "يُوقَفُ",
    note="مِثَالٌ وَاوِيٌّ: تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ — وَقَفَ يَقِفُ.")
MORPH["verbs"]["kharaja"] = _sg.sound1(
    "nasara", "خَرَج", "خْرُج", "اُخْرُج", "خُرُوج", "خَارِج")
MORPH["verbs"]["zalama"] = _sg.sound1(
    "daraba", "ظَلَم", "ظْلِم", "اِظْلِم", "ظُلْم", "ظَالِم",
    "مَظْلُوم", "ظُلِمَ", "يُظْلَمُ")
MORPH["verbs"]["hafiza"] = _sg.sound1(
    "samia", "حَفِظ", "حْفَظ", "اِحْفَظ", "حِفْظ", "حَافِظ",
    "مَحْفُوظ", "حُفِظَ", "يُحْفَظُ")
MORPH["verbs"]["ihtarama"] = _sg.derived(
    _sg.B8, _sg.W8, "َ", "اِحْتَرَم", "حْتَرِم", "اِحْتَرِم",
    "اِحْتِرَام", "مُحْتَرِم", "مُحْتَرَم", "اُحْتُرِمَ", "يُحْتَرَمُ")
# حَلَّ يَحِلُّ — geminate of bab daraba, assembled cell by cell like the
# corpus's other doubled verbs (contracted stem before vowels, broken
# before consonants), with idgham applied by the shared helper.
MORPH["verbs"]["halla-lawful"] = _sg.idgham(_sg.entry(
    _sg.BABS["daraba"][0] + " — مُضَاعَفٌ", _sg.BABS["daraba"][1], "حِلّ", "حَالّ",
    _sg.mazi14("حَلّ", "حَلَل"), _sg.mudari14("َ", "حِلّ", "حْلِل"),
    ["حِلَّ", "حِلَّا", "حِلُّوا", "حِلِّي", "حِلَّا", "اِحْلِلْنَ"],
    "يَحِلَّ", "يَحِلَّ", "تَحِلَّ",
    note="مُضَاعَفٌ مِنْ بَابِ ضَرَبَ: الْجَزْمُ بِالْفَتْحِ، وَيَجُوزُ الْفَكُّ — لَمْ يَحِلَّ / لَمْ يَحْلِلْ."))

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
