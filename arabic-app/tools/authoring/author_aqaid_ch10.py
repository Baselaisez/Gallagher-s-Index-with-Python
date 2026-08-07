# -*- coding: utf-8 -*-
"""Author chapter 10 of aqaid-ahl-al-sunna — saying «I am a believer».

Continues the matn: once affirmation and profession are found in the servant
he may say «I am truly a believer» without the exception; the happy may turn
wretched and the wretched happy, but the CHANGE falls on happiness and
wretchedness, not on Allah's making-happy and making-wretched, for those are
His attributes and no change touches Him or them. Verbatim contiguous spans
re-vowelled against the received text; each sentence stops at a matn period
and no clause is skipped from the middle.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
sys.path.insert(0, str(ROOT / "tools/authoring"))
import sarf_gen as _sg
DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)
def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
S = []

S.append({"id": "s1", "translation": {
 "en": "And when affirmation and profession are found in the servant, it is sound for him to say: I am truly a believer.",
 "tr": "Kulda tasdik ve ikrar bulunduğunda, «ben gerçekten mü'minim» demesi sahih olur."},
 "tokens": [
  tok("وَإِذَا","idha","part",["idha-shartiyya"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«إِذَا» ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "Isti'naf waw; إِذَا is a time-adverb carrying conditional force.",
      "İstinâf vâvı; «إِذَا» şart manası taşıyan zaman zarfıdır.",
      segments=[seg("وَ","wa","conj"), seg("إِذَا","idha","part")]),
  tok("وُجِدَ","wajada","verb",["naib-al-fail","mithal-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — مِنَ الْمِثَالِ الْوَاوِيِّ «وَجَدَ».",
      "A passive past verb — from the waw-initial وَجَدَ.",
      "Meçhul mâzî fiil — misâl-i vâvî «وَجَدَ»dendir."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("الْعَبْدِ","abd","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ».",
      "In jarr after مِنْ.",
      "«مِنْ» ile mecrurdur."),
  tok("التَّصْدِيقُ","tasdiq","noun",["naib-al-fail","form-ii-verbs","masdar"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.",
      "The deputy of the fa'il, in raf'.",
      "Merfû nâibü'l-fâildir."),
  tok("وَالْإِقْرَارُ","iqrar","noun",["atf-nasaq","masdar"],
      "مَعْطُوفٌ عَلَى نَائِبِ الْفَاعِلِ مَرْفُوعٌ.",
      "Joined to the deputy, in raf'.",
      "Nâibü'l-fâile ma'tûf, merfûdur.",
      segments=[seg("وَ","wa","conj"), seg("الْإِقْرَارُ","iqrar","noun")]),
  tok("صَحَّ","sahha","verb",["doubled-verbs","thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ مُضَاعَفٌ، وَهُوَ جَوَابُ «إِذَا».",
      "A geminate past verb — the answer of إِذَا.",
      "Muzâaf mâzî fiil — «إِذَا»nın cevabıdır."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«صَحَّ».",
      "Preposition-phrase attached to صَحَّ.",
      "«صَحَّ»ye mütealliḳ câr-mecrûr.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — سَاكِنُ النُّونِ، فَهُوَ غَيْرُ «أَنَّ» الْمُشَدَّدَةِ.",
      "The masdar-making particle, governing nasb — its nun is SAKIN, so it is not the doubled أَنَّ.",
      "Nasbeden masdariyye harfi — nûnu SÂKİNDİR, şeddeli «أَنَّ» değildir."),
  tok("يَقُولَ","qala","verb",["an-masdariyya","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ»، وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ «صَحَّ».",
      "A mudari in nasb after أَنْ; the construed masdar is the fa'il of صَحَّ.",
      "«أَنْ» ile mansub muzâri; müevvel masdar «صَحَّ»nin fâilidir.", punct=":"),
  tok("أَنَا","pron-1s-munfasil","pron",["mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "A detached pronoun, mabni, standing as the mubtada in raf' position.",
      "Munfasıl mebnî zamir — mübteda olarak mahallen merfûdur."),
  tok("مُؤْمِنٌ","mumin","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ.",
      "The khabar, in raf'.",
      "Merfû haberdir."),
  tok("حَقًّا","haqq","noun",["maful-mutlaq"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ — أَيْ أَحُقُّ ذَلِكَ حَقًّا.",
      "An absolute object in nasb for an ELIDED verb — «I affirm it truly».",
      "Mahzuf bir fiil için mensub mef'ûl-i mutlak — «bunu gerçekten hak bilirim» takdirinde.", punct="."),
 ],
 "jumal": [
  J("وَإِذَا وُجِدَ مِنَ الْعَبْدِ التَّصْدِيقُ وَالْإِقْرَارُ",
    "جُمْلَةُ الشَّرْطِ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا».",
    "The condition clause, in jarr position by إِذَا's idafa.",
    "Şart cümlesi — «إِذَا»nın izâfetiyle mahallen mecrurdur."),
  J("أَنَا مُؤْمِنٌ حَقًّا",
    "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "A nominal clause in nasb position — the quoted speech.",
    "Makûlü'l-kavl olarak mahallen mensub isim cümlesi.")]})

S.append({"id": "s2", "translation": {
 "en": "And it is not fitting that he say: I am a believer, if Allah wills.",
 "tr": "«İnşâallah mü'minim» demesi ise uygun değildir."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ.",
      "Joining waw; the لا negates.",
      "Atıf vâvı; «لَا» nefiy içindir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَنْبَغِي","inbagha","verb",["mudari-marfu","form-vii-verbs","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — مِنَ «انْبَغَى».",
      "A mudari in raf' by a damma ESTIMATED on the ya as too heavy — from انْبَغَى (Form VII).",
      "Yâ üzerinde ağırlık sebebiyle takdîrî damme ile merfû muzâri — «انْبَغَى» (infiâl) fiilindendir."),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.",
      "The masdar-making particle, governing nasb.",
      "Nasbeden masdariyye harfidir."),
  tok("يَقُولَ","qala","verb",["an-masdariyya","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ «يَنْبَغِي».",
      "A mudari in nasb; the construed masdar is the fa'il of يَنْبَغِي.",
      "Mansub muzâri; müevvel masdar «يَنْبَغِي»nin fâilidir.", punct=":"),
  tok("أَنَا","pron-1s-munfasil","pron",["mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "A detached pronoun, the mubtada in raf' position.",
      "Munfasıl zamir — mübteda olarak mahallen merfûdur."),
  tok("مُؤْمِنٌ","mumin","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ.",
      "The khabar, in raf'.",
      "Merfû haberdir."),
  tok("إِنْ","in-shartiyya","part",["in-shartiyya"],
      "حَرْفُ شَرْطٍ جَازِمٌ.",
      "The conditional particle, governing jazm.",
      "Câzim şart harfidir."),
  tok("شَاءَ","shaa","verb",["in-shartiyya","hollow-verbs"],
      "فِعْلُ الشَّرْطِ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.",
      "The condition verb, a past in jazm position; its answer is ELIDED, shown by what precedes.",
      "Şart fiili — mâzî, mahallen meczum; cevabı mahzuftur, öncesi ona delâlet eder."),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name — the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir.", punct="."),
 ],
 "jumal": [
  J("وَلَا يَنْبَغِي أَنْ يَقُولَ",
    "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined verbal clause — i'rabless.",
    "Ma'tûf fiil cümlesi — mahalsizdir."),
  J("إِنْ شَاءَ اللهُ",
    "جُمْلَةُ شَرْطٍ جَوَابُهَا مَحْذُوفٌ — لَا مَحَلَّ لَهَا.",
    "A conditional clause whose answer is elided — i'rabless.",
    "Cevabı mahzuf şart cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the happy one may become wretched, and the wretched one may become happy.",
 "tr": "Said olan şakî olabilir, şakî olan da said olabilir."},
 "tokens": [
  tok("وَالسَّعِيدُ","said","noun",["mubtada-khabar","sifa-mushabbaha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«السَّعِيدُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "Isti'naf waw; السَّعِيد is the mubtada in raf'.",
      "İstinâf vâvı; «السَّعِيدُ» merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("السَّعِيدُ","said","noun")]),
  tok("قَدْ","qad","part",["qad-harf"],
      "حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ — «رُبَّمَا»، لَا تَحْقِيقٌ.",
      "With a mudari, qad marks INFREQUENCY — «may sometimes», not certainty.",
      "Muzâri ile kad TAKLÎL bildirir — «bazen olur», tahkik değil."),
  tok("يَشْقَى","shaqiya","verb",["mudari-marfu","naqis-verbs","ism-maqsur-manqus"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْجُمْلَةُ خَبَرٌ.",
      "A mudari in raf' by a damma ESTIMATED on the alif — it cannot bear one; the clause is the khabar.",
      "Elif üzerinde takdîrî damme ile merfû muzâri (teazzür); cümle haberdir.", punct="،"),
  tok("وَالشَّقِيُّ","shaqi","noun",["mubtada-khabar","atf-nasaq"],
      "مَعْطُوفٌ — مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.",
      "Joined — a second mubtada, in raf'.",
      "Ma'tûf — ikinci merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("الشَّقِيُّ","shaqi","noun")]),
  tok("قَدْ","qad","part",["qad-harf"],
      "حَرْفُ تَقْلِيلٍ.",
      "The particle of infrequency.",
      "Taklîl harfidir."),
  tok("يَسْعَدُ","saida","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ.",
      "A mudari in raf'; the clause is the khabar.",
      "Merfû muzâri; cümle haberdir.", punct="."),
 ],
 "jumal": [
  J("وَالسَّعِيدُ قَدْ يَشْقَى",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause — i'rabless.",
    "Müste'nefe isim cümlesi — mahalsizdir."),
  J("قَدْ يَشْقَى",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
    "A verbal clause standing as the khabar, in raf' position.",
    "Haber olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s4", "translation": {
 "en": "And no change comes upon Allah the Exalted, nor upon His attributes.",
 "tr": "Allah Teâlâ üzerine de sıfatları üzerine de değişme yoktur."},
 "tokens": [
  tok("وَلَا","la-nafiya-lil-jins","part",["la-nafiya-lil-jins"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَا» نَافِيَةٌ لِلْجِنْسِ.",
      "Isti'naf waw; the لا denies the whole genus.",
      "İstinâf vâvı; «لَا» cinsini nefyeden lâdır.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya-lil-jins","part")]),
  tok("تَغَيُّرَ","taghayyur","noun",["la-nafiya-lil-jins","form-v-verbs","masdar"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — مَصْدَرُ «تَغَيَّرَ».",
      "The ism of لا, built on fatha, in nasb position — the masdar of تَغَيَّرَ (Form V).",
      "«لَا»nın ismi — fetha üzere mebnî, mahallen mensub; «تَغَيَّرَ» (tefa''ul) masdarıdır."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ «لَا».",
      "A jarr letter; the phrase is the khabar of لا.",
      "Cer harfi; câr-mecrûr «لَا»nın haberidir."),
  tok("اللهِ","allah","noun",["huruf-jarr"],
      "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.",
      "The majestic name, in jarr.",
      "Lafza-i celâl — mecrurdur."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır."),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
      "Joining waw; the لا re-affirms the negation.",
      "Atıf vâvı; «لَا» nefyi pekiştirir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("عَلَى","ala","prep",["huruf-jarr","atf-nasaq"],
      "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ قَبْلَهُ.",
      "Joined to the preceding preposition-phrase.",
      "Öncesindeki câr-mecrûra ma'tûftur."),
  tok("صِفَاتِهِ","sifa","noun",["huruf-jarr","idafa-definiteness","jam-muannath-salim"],
      "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr by the kasra — a sound feminine plural, itself a mudaf; the ha is its mudaf ilayh.",
      "Kesra ile mecrur — cem'-i müennes-i sâlim ve muzâf; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("صِفَاتِ","sifa","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("وَلَا تَغَيُّرَ عَلَى اللهِ تَعَالَى وَلَا عَلَى صِفَاتِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ مَنْفِيَّةٌ بِلَا النَّافِيَةِ لِلْجِنْسِ — لَا مَحَلَّ لَهَا.",
   "A resumed nominal clause negated by the genus-denying la — i'rabless.",
   "Cinsini nefyeden lâ ile menfî müste'nefe isim cümlesi — mahalsizdir.")]})

TITLE10 = {"ar": "قَوْلُ الْعَبْدِ «أَنَا مُؤْمِنٌ» وَالسَّعَادَةُ وَالشَّقَاوَةُ",
           "en": "Saying «I am a Believer»; Happiness and Wretchedness",
           "tr": "«Ben Mü'minim» Demek; Saâdet ve Şekāvet"}

def g(lemma, root, pos, en, tr, lvl):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": lvl}
    if root: e["root"] = root
    return e
GLOSS_ADD = {
 "wajada": g("وَجَدَ","و ج د","verb","to find; (passive) to be found","bulmak; (meçhul) bulunmak",2),
 "sahha": g("صَحَّ","ص ح ح","verb","to be sound, valid","sahih olmak; geçerli olmak",3),
 "an-masdariyya": g("أَنْ","","part","that (masdar-maker, governs nasb)","-mesi (masdariyye, nasbeder)",3),
 "pron-1s-munfasil": g("أَنَا","","pron","I (detached)","ben (munfasıl)",1),
 "inbagha": g("انْبَغَى","ب غ ي","verb","to be fitting, proper","yaraşmak; uygun olmak",4),
 "shaa": g("شَاءَ","ش ي أ","verb","to will","dilemek",2),
 "said": g("سَعِيد","س ع د","noun","happy, blessed","said; mutlu",3),
 "shaqi": g("شَقِيّ","ش ق و","noun","wretched","şakî; bedbaht",3),
 "shaqiya": g("شَقِيَ","ش ق و","verb","to be wretched","şakî olmak",3),
 "saida": g("سَعِدَ","س ع د","verb","to be happy, blessed","said olmak",3),
 "taghayyur": g("تَغَيُّر","غ ي ر","noun","change (masdar, Form V)","değişme; tagayyür (masdar)",4),
 "idha": g("إِذَا","","part","when (a time-adverb carrying conditional force)","-dığı zaman (şart manalı zaman zarfı)",2),
 "in-shartiyya": g("إِنْ","","part","if (conditional, governs jazm)","eğer (câzim şart harfi)",2),
}

def build_morph():
    kaf = json.loads((ROOT / "content/samples/kitab-al-kaffarat/morphology.json").read_text(encoding="utf-8"))["verbs"]
    out = {"wajada": kaf["wajada"]}
    out["sahha"] = _sg.idgham(_sg.entry(
        _sg.BABS["daraba"][0] + " — مُضَاعَفٌ", _sg.BABS["daraba"][1], "صِحَّة", "صَاحّ",
        _sg.mazi14("صَحّ", "صَحَح"), _sg.mudari14("َ", "صِحّ", "صْحِح"),
        ["صِحَّ", "صِحَّا", "صِحُّوا", "صِحِّي", "صِحَّا", "اِصْحِحْنَ"],
        "يَصِحَّ", "يَصِحَّ", "تَصِحَّ",
        note="مُضَاعَفٌ مِنْ بَابِ ضَرَبَ: الْجَزْمُ بِالْفَتْحِ، وَيَجُوزُ الْفَكُّ."))
    out["shaqiya"] = _sg.entry("مِنْ بَابِ سَمِعَ يَسْمَعُ — نَاقِصٌ وَاوِيٌّ", "فَعِلَ يَفْعَلُ",
                               "شَقَاوَة", "شَقِيّ",
                               _sg.mazi_naqis_kasra("شَقِ", "شَقُوا"),
                               _sg.mudari_naqis("َ", "شْق", "a"), _sg.amr_naqis("اِشْق", "a"),
                               "يَشْقَى", "يَشْقَ", "تَشْقَ", None, None, None,
                               "نَاقِصٌ كَرَضِيَ: تَسْقُطُ الْيَاءُ مَعَ ضَمَائِرِ الرَّفْعِ — شَقِيتَ، وَجَمْعُهُ شَقُوا.")
    # انْبَغَى — infial of the naqis ب غ ي; it has no imperative in use, and
    # the corpus's jamid flag is for verbs with no tasrif at all, so it is
    # built in full and only its amr row is the one the books do not recite.
    out["inbagha"] = _sg.derived_naqis(_sg.B7 + " — نَاقِصٌ", _sg.W7, "َ",
                                       "اِنْبَغَ", "نْبَغ", "i", "اِنْبَغ",
                                       "اِنْبِغَاء", "مُنْبَغٍ", None, None, None,
                                       "نَاقِصٌ مِنَ الِانْفِعَالِ: يَنْبَغِي — تُقَدَّرُ الضَّمَّةُ عَلَى يَائِهِ.")
    out["saida"] = _sg.sound1("samia", "سَعِد", "سْعَد", "اِسْعَد", "سَعَادَة", "سَعِيد")
    out["shaa"] = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json")
                             .read_text(encoding="utf-8"))["verbs"]["shaa"]
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/10.json").write_text(json.dumps({"chapter": 10, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 10 for c in man["chapters"]):
    man["chapters"].append({"n": 10, "title": TITLE10})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.8.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch10:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
