# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 27: the intellect as a cause of knowledge — the self-evident and the inferred.
Source: matn line 27 (وأما العقل فهو سبب للعلم أيضا … فهو اكتسابي).  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch27.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْعَقْلُ سَبَبٌ لِلْعِلْمِ", "en": "The Intellect as a Cause of Knowledge", "tr": "İlmin Sebebi Olarak Akıl"}
S = []
def FAHUWA(of, en, tr, kind="fa-khabar"):
    pre = {"fa-khabar": "الْفَاءُ دَاخِلَةٌ فِي خَبَرِ الْمُبْتَدَإِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ", "fa-jawab": "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»"}[kind]
    tags = ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada" if kind == "fa-khabar" else "amma-tafsiliyya", "al-marifa-al-mudmarat-wal-alam"]
    return W("فَهُوَ", "pron-3ms-munfasil", "pron", tags, pre + "، وَ«هُوَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ ثَانٍ، وَالْجُمْلَةُ خَبَرُ «" + of + "».", en, tr, segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "pron-3ms-munfasil", "pron")])
S.append({"id": "s1", "translation": {
 "en": "As for the intellect, it too is a cause of knowledge.",
 "tr": "Akla gelince: o da ilmin bir sebebidir."},
 "tokens": [
  W("وَأَمَّا", "amma", "part", ["amma-tafsiliyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«أَمَّا» حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ مَبْنِيٌّ لَا مَحَلَّ لَهُ.", "«as for» — ammā detaches a topic and demands a fāʾ in its answer.", "«… -e gelince» — emmâ bir konuyu ayırır ve cevabında fâ ister.", segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")]),
  MUB("الْعَقْلُ", "aql", "«the intellect» — the third of the three causes of knowledge.", "«akıl» — ilmin üç sebebinin üçüncüsü."),
  FAHUWA("الْعَقْلُ", "«it» — the fāʾ answers ammā; هُوَ opens the sentence that is the khabar.", "«o» — fâ emmâ'ya cevaptır; هُوَ haber olan cümleyi açar.", kind="fa-jawab"),
  KHA("سَبَبٌ", "sabab", "«a cause».", "«bir sebep».", of="هُوَ"),
  FUSED("لِلْعِلْمِ", "لِ", "ilm", "«of knowledge».", "«ilmin».", "«سَبَبٌ»", inner="الْعِلْمِ"),
  W("أَيْضًا", "aydan", "adv", ["maful-mutlaq", "hadhf-wa-taqdir"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ، أَيْ: آضَ أَيْضًا — مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«too, also» — the masdar of آضَ «to return», an absolute object of its dropped verb.", "«de, dahi» — آضَ «dönmek»in masdarı; hazfedilmiş fiilinin mef'ûl-i mutlakı.", punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And what is established by it self-evidently is necessary — like the knowledge that the whole of a thing is greater than its part.",
 "tr": "Onunla bedîhî olarak sabit olan zarûrîdir — bir şeyin bütününün parçasından büyük olduğunu bilmek gibi."},
 "tokens": [
  W("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "al-fa-fi-khabar-al-mubtada", "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَدَخَلَتِ الْفَاءُ فِي خَبَرِهِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ.", "«and what» — a relative as mubtada; because it carries the sense of a condition, its khabar takes a fāʾ.", "«ve her ne ki» — mübteda olan ism-i mevsûl; şart mânâsı taşıdığı için haberine fâ girer.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  MAZI("ثَبَتَ", "thabata", "«is established» — the ṣila of مَا.", "«sabit olur» — مَا'nın sılası.", HIDDEN_HUWA + " — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا", tags=["ism-mawsul", "fail"]),
  PRON_J("مِنْهُ", "مِنْ", "«of it» — of the intellect.", "«ondan» — akıldan.", "«ثَبَتَ»"),
  FUSED("بِالْبَدِيهَةِ", "بِ", "badiha", "«self-evidently» — by immediate apprehension, with no reasoning.", "«bedâheten» — istidlâlsiz, ilk bakışta.", "«ثَبَتَ»", inner="الْبَدِيهَةِ"),
  FAHUWA("مَا", "«it» — the fāʾ enters the khabar of مَا.", "«o» — fâ, مَا'nın haberine girer."),
  KHA("ضَرُورِيٌّ", "daruri", "«necessary».", "«zarûrîdir».", of="هُوَ", punct="،"),
  FUSED("كَالْعِلْمِ", "كَ", "ilm", "«like the knowledge» — hanging on a dropped khabar: «and that is like …».", "«bilmek gibi» — hazfedilmiş bir habere bağlı: «o da … gibidir».", "مَحْذُوفٍ، أَيْ: وَذَلِكَ كَائِنٌ كَالْعِلْمِ", inner="الْعِلْمِ", meaning=" لِلتَّشْبِيهِ", tags=["hadhf-wa-taqdir"]),
  W("بِأَنَّ", "anna", "part", ["huruf-jarr", "inna-wa-akhawatuha", "mawadi-fath-anna", "an-masdariyya"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«أَنَّ» حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْبَاءِ مُتَعَلِّقٌ بِـ«الْعِلْمِ».", "«that» — anna with its clause makes a masdar in jarr after the bāʾ: «the knowledge of the-whole's-being-greater».", "«… olduğunu» — enne ve cümlesi, bâ'dan sonra mecrûr bir masdar olur: «bütünün büyük olduğunu bilmek».", segments=[seg("بِ", "bi", "prep"), seg("أَنَّ", "anna", "part")]),
  W("كُلَّ", "kull", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ «أَنَّ» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَهُوَ مُضَافٌ.", "«the whole of».", "«bütünü»."),
  MUDI("الشَّيْءِ", "shay", "«the thing».", "«şeyin»."),
  W("أَعْظَمُ", "azam", "noun", ["inna-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ «أَنَّ» مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ، وَهُوَ اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«is greater» — an elative, barred from tanwīn, as anna's khabar.", "«daha büyüktür» — enne'nin haberi olan, tenvinden men edilmiş ism-i tafdîl."),
  PREP("مِنْ", "min", "«than».", "«-den»."),
  ENC("جُزْئِهِ", "juz", "«its part».", "«parçasından».", "اسْمٌ مَجْرُورٌ بِـ«مِنْ» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", att="«أَعْظَمُ»", punct=".")]})
S.append({"id": "s3", "translation": {
 "en": "And what is established by it through reasoning is acquired.",
 "tr": "Onunla istidlâl yoluyla sabit olan ise iktisâbîdir."},
 "tokens": [
  W("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "al-fa-fi-khabar-al-mubtada", "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and what».", "«ve her ne ki».", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  MAZI("ثَبَتَ", "thabata", "«is established».", "«sabit olur».", HIDDEN_HUWA + " — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ", tags=["ism-mawsul", "fail"]),
  PRON_J("مِنْهُ", "مِنْ", "«of it».", "«ondan».", "«ثَبَتَ»"),
  FUSED("بِالِاسْتِدْلَالِ", "بِ", "istidlal", "«through reasoning» — the masdar of Form X: seeking the proof (دَلِيل).", "«istidlâl ile» — istif'âl masdarı: delil aramak.", "«ثَبَتَ»", inner="الِاسْتِدْلَالِ", tags=["masdar", "form-x-verbs"]),
  FAHUWA("مَا", "«it».", "«o»."),
  KHA("اكْتِسَابِيٌّ", "iktisabi", "«acquired» — the nisba of اكْتِسَاب, the masdar of Form VIII.", "«iktisâbîdir» — iftiâl masdarı اكْتِسَاب'a nispet.", of="هُوَ", punct=".", tags=["ism-mansub"])]})

CAND = {
 "badiha": need("badiha", "بَدِيهَة", "ب د ه", "noun", "self-evidence, immediate apprehension — a truth known at first sight", "bedâhet, ilk bakışta biliş — delilsiz bilinen hakikat", 4),
 "istidlal": need("istidlal", "اسْتِدْلَال", "د ل ل", "noun", "reasoning, inference — seeking the proof (masdar of Form X)", "istidlâl, delil getirme (istif'âl masdarı)", 4),
 "iktisabi": need("iktisabi", "اكْتِسَابِيّ", "ك س ب", "noun", "acquired (of knowledge: reached by reasoning)", "iktisâbî (ilim için: istidlâlle kazanılan)", 4),
}
ADD_EN = " Chapter 27 (matn line 27): the intellect as the third cause of knowledge; the self-evident is necessary, the inferred is acquired."
ADD_TR = " Yirmi yedinci bâb (matn satırı 27): ilmin üçüncü sebebi olarak akıl; bedîhî olan zarûrî, istidlâlî olan iktisâbîdir."
finish(27, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 27 (matn line 27)")
