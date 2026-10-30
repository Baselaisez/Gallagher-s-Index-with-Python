# -*- coding: utf-8 -*-
"""Author chapter 8 of aqaid-ahl-al-sunna — the sam'iyyat.

Continues the matn where chapter 7 stopped: the punishment of the grave,
the questioning of Munkar and Nakir, and the roll of eight realities each
declared حَقٌّ — then the DUAL, which the corpus had barely taught until
now: مَخْلُوقَتَانِ مَوْجُودَتَانِ بَاقِيَتَانِ لَا تَفْنَيَانِ. Chapter 1 opened
this story with the hawd hadith; here the matn names الْحَوْضُ حَقٌّ, so the
book closes a ring it opened.

Verbatim contiguous spans re-vowelled against the received text: each
sentence stops at a matn period, and no clause is skipped from the middle.
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
 "en": "And the punishment of the grave is for the unbelievers and for some of the disobedient among the believers.",
 "tr": "Kabir azabı kâfirler için ve mü'minlerin âsi olanlarından bir kısmı içindir."},
 "tokens": [
  tok("وَعَذَابُ","adhab","noun",["mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«عَذَابُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "Isti'naf waw; عَذَاب is the mubtada in raf', itself a mudaf.",
      "İstinâf vâvı; «عَذَابُ» merfû mübteda ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("عَذَابُ","adhab","noun")]),
  tok("الْقَبْرِ","qabr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir."),
  tok("لِلْكَافِرِينَ","li","prep",["huruf-jarr","jam-mudhakkar-salim","ism-fail"],
      "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ — مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "A preposition-phrase standing as the khabar, in raf' position — in jarr by the ya, being a sound masculine plural.",
      "Haber olarak mahallen merfû câr-mecrûr — cem'-i müzekker-i sâlim olduğu için yâ ile mecrurdur.",
      segments=[seg("لِ","li","prep"), seg("الْكَافِرِينَ","kafir","noun")]),
  tok("وَلِبَعْضِ","li","prep",["atf-nasaq","huruf-jarr","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ، وَ«بَعْضِ» مُضَافٌ.",
      "Joined to the preceding phrase; بَعْض is a mudaf.",
      "Önceki câr-mecrûra ma'tûf; «بَعْضِ» muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","prep"), seg("بَعْضِ","bad","noun")]),
  tok("عُصَاةِ","usat","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — جَمْعُ «عَاصٍ».",
      "Mudaf ilayh in jarr, itself a mudaf — the plural of عَاصٍ.",
      "Mecrûr muzâfun ileyh ve muzâf — «عَاصٍ» kelimesinin cem'idir."),
  tok("الْمُؤْمِنِينَ","mumin","noun",["idafa-definiteness","jam-mudhakkar-salim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "Mudaf ilayh in jarr by the ya — a sound masculine plural.",
      "Yâ ile mecrûr muzâfun ileyh — cem'-i müzekker-i sâlim.", punct="،"),
 ],
 "jumal": [J("وَعَذَابُ الْقَبْرِ لِلْكَافِرِينَ",
   "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
   "A resumed nominal clause — i'rabless.",
   "Müste'nefe isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And the bliss of the people of obedience in the grave is by what Allah the Exalted knows and wills.",
 "tr": "Taat ehlinin kabirde nimetlendirilmesi, Allah Teâlâ'nın bildiği ve dilediği şekildedir."},
 "tokens": [
  tok("وَتَنْعِيمُ","taniim","noun",["mubtada-khabar","idafa-definiteness","form-ii-verbs","masdar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«تَنْعِيمُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «نَعَّمَ».",
      "Joining waw; تَنْعِيم is the mubtada in raf', a mudaf — the masdar of نَعَّمَ (Form II).",
      "Atıf vâvı; «تَنْعِيمُ» merfû mübteda ve muzâf — «نَعَّمَ» (tef'îl) masdarıdır.",
      segments=[seg("وَ","wa","conj"), seg("تَنْعِيمُ","taniim","noun")]),
  tok("أَهْلِ","ahl","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "Mudaf ilayh in jarr, itself a mudaf.",
      "Mecrûr muzâfun ileyh ve muzâftır."),
  tok("الطَّاعَةِ","taa","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "The jarr letter of containment.",
      "Zarfiyyet bildiren cer harfidir."),
  tok("الْقَبْرِ","qabr","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي»، وَالْجَارُّ مُتَعَلِّقٌ بِـ«تَنْعِيمُ».",
      "In jarr after فِي; the phrase attaches to تَنْعِيم.",
      "«فِي» ile mecrur; câr-mecrûr «تَنْعِيمُ»e mütealliḳtır."),
  tok("بِمَا","bi","prep",["huruf-jarr","ism-mawsul","anwa-ma"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» مَوْصُولَةٌ مَجْرُورَةٌ بِهَا، وَالْجَارُّ خَبَرٌ.",
      "The ba is a jarr letter and «ma» is the relative in jarr after it; the phrase is the khabar.",
      "Bâ cer harfi, «mâ» mevsûledir ve onunla mecrurdur; câr-mecrûr haberdir.",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("يَعْلَمُهُ","alima","verb",["mudari-marfu","maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "A mudari in raf'; the ha is its object, and the clause is the sila of the relative.",
      "Merfû muzâri; hâ zamiri mef'ûlün bihtir, cümle mevsûlün sılasıdır.",
      segments=[seg("يَعْلَمُ","alima","verb"), seg("هُ","pron-3ms","pron")]),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name — the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır."),
  tok("وَيُرِيدُهُ","arada","verb",["atf-nasaq","form-iv-verbs","hollow-verbs"],
      "مَعْطُوفٌ عَلَى «يَعْلَمُهُ» — مُضَارِعٌ مِنْ «أَرَادَ»، أَجْوَفُ مِنَ الْإِفْعَالِ.",
      "Joined to يَعْلَمُهُ — the mudari of أَرَادَ, a hollow Form IV.",
      "«يَعْلَمُهُ»e ma'tûf — «أَرَادَ» fiilinin muzârisi; if'âlden ecveftir.",
      segments=[seg("وَ","wa","conj"), seg("يُرِيدُ","arada","verb"), seg("هُ","pron-3ms","pron")], punct="،"),
 ],
 "jumal": [
  J("وَتَنْعِيمُ أَهْلِ الطَّاعَةِ فِي الْقَبْرِ بِمَا يَعْلَمُهُ اللهُ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal clause — i'rabless.",
    "Ma'tûf isim cümlesi — mahalsizdir."),
  J("يَعْلَمُهُ اللهُ تَعَالَى",
    "جُمْلَةٌ فِعْلِيَّةٌ صِلَةٌ لِـ«مَا» — لَا مَحَلَّ لَهَا.",
    "A verbal clause, the sila of «ma» — i'rabless.",
    "«Mâ»nın sıla cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the questioning of Munkar and Nakir is established by the transmitted proofs.",
 "tr": "Münker ve Nekîr'in sorgusu, semî' delillerle sabittir."},
 "tokens": [
  tok("وَسُؤَالُ","sual","noun",["mubtada-khabar","idafa-definiteness","masdar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«سُؤَالُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "Joining waw; سُؤَال is the mubtada in raf', itself a mudaf.",
      "Atıf vâvı; «سُؤَالُ» merfû mübteda ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("سُؤَالُ","sual","noun")]),
  tok("مُنْكَرٍ","munkar","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ لِمَلَكٍ.",
      "Mudaf ilayh in jarr — the name of an angel.",
      "Mecrûr muzâfun ileyh — bir meleğin ismidir."),
  tok("وَنَكِيرٍ","nakir","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ.",
      "Joined to it, in jarr.",
      "Ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("نَكِيرٍ","nakir","noun")]),
  tok("ثَابِتٌ","thabit","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «ثَبَتَ».",
      "The khabar in raf' — the ism fa'il of ثَبَتَ.",
      "Merfû haber — «ثَبَتَ» fiilinin ism-i fâilidir."),
  tok("بِالدَّلَائِلِ","bi","prep",["huruf-jarr","mamnu-min-sarf"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ثَابِتٌ» — «الدَّلَائِل» صِيغَةُ مُنْتَهَى الْجُمُوعِ، وَجُرَّتْ بِالْكَسْرَةِ لِدُخُولِ «أَلْ».",
      "Preposition-phrase attached to ثَابِت — الدَّلَائِل is a diptote, yet takes the kasra because ال has entered it.",
      "«ثَابِتٌ»a mütealliḳ câr-mecrûr — «الدَّلَائِل» gayr-i munsariftir; «el» girdiği için kesra ile mecrurdur.",
      segments=[seg("بِ","bi","prep"), seg("الدَّلَائِلِ","dalil","noun")]),
  tok("السَّمْعِيَّةِ","samiyya","noun",["naat-sifa"],
      "نَعْتٌ مَجْرُورٌ — نِسْبَةٌ إِلَى «السَّمْع».",
      "A na't in jarr — the nisba of السَّمْع, «what is heard» (revelation).",
      "Mecrûr na't — «السَّمْع»e nisbettir: naklî.", punct="."),
 ],
 "jumal": [J("وَسُؤَالُ مُنْكَرٍ وَنَكِيرٍ ثَابِتٌ بِالدَّلَائِلِ السَّمْعِيَّةِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined nominal clause — i'rabless.",
   "Ma'tûf isim cümlesi — mahalsizdir.")]})

# the roll of eight: one mubtada + khabar pattern, eight times over
ROLL = [("وَالْبَعْثُ","bath","الْبَعْثُ"), ("وَالْوَزْنُ","wazn","الْوَزْنُ"),
        ("وَالْكِتَابُ","kitab","الْكِتَابُ"), ("وَالسُّؤَالُ","sual","السُّؤَالُ"),
        ("وَالْحَوْضُ","hawd","الْحَوْضُ"), ("وَالصِّرَاطُ","sirat","الصِّرَاطُ"),
        ("وَالْجَنَّةُ","janna","الْجَنَّةُ"), ("وَالنَّارُ","nar","النَّارُ")]
roll_tokens = []
for i, (full, lex, barepart) in enumerate(ROLL):
    roll_tokens.append(tok(full, lex, "noun", ["mubtada-khabar"],
        "مُبْتَدَأٌ مَرْفُوعٌ.", "A mubtada in raf'.", "Merfû mübtedadır.",
        segments=[seg("وَ","wa","conj"), seg(barepart, lex, "noun")]))
    roll_tokens.append(tok("حَقٌّ", "haqq", "noun", ["mubtada-khabar"],
        "خَبَرٌ مَرْفُوعٌ.", "Its khabar, in raf'.", "Merfû haberidir.",
        punct="." if i == len(ROLL) - 1 else "،"))

S.append({"id": "s4", "translation": {
 "en": "The resurrection is true, the weighing is true, the book is true, the questioning is true, the basin is true, the bridge is true, the garden is true and the fire is true.",
 "tr": "Ba's haktır, tartı haktır, kitap haktır, sual haktır, havz haktır, sırat haktır, cennet haktır, cehennem haktır."},
 "tokens": roll_tokens,
 "jumal": [J("وَالْبَعْثُ حَقٌّ، وَالْوَزْنُ حَقٌّ…",
   "ثَمَانِي جُمَلٍ اسْمِيَّةٍ مُتَعَاطِفَةٍ — لَا مَحَلَّ لَهَا.",
   "Eight joined nominal clauses — all i'rabless.",
   "Birbirine atfedilmiş sekiz isim cümlesi — hepsi mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And they two are created, existent and abiding: they do not perish, nor do their people perish.",
 "tr": "O ikisi yaratılmış, mevcut ve bâkîdir; ne kendileri fânî olur ne de ehli."},
 "tokens": [
  tok("وَهُمَا","pron-dual","pron",["mubtada-khabar","al-muthanna"],
      "الْوَاوُ عَاطِفَةٌ، وَ«هُمَا» ضَمِيرُ تَثْنِيَةٍ مُبْتَدَأٌ.",
      "Joining waw; هُمَا is the DUAL pronoun, the mubtada.",
      "Atıf vâvı; «هُمَا» tesniye zamiri, mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("هُمَا","pron-dual","pron")]),
  tok("مَخْلُوقَتَانِ","makhluq","noun",["mubtada-khabar","ism-maful","al-muthanna"],
      "خَبَرٌ أَوَّلُ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى — اسْمُ مَفْعُولٍ.",
      "First khabar in raf', its sign the ALIF because it is a DUAL — an ism maf'ul.",
      "Birinci merfû haber; tesniye olduğu için ref alâmeti ELİFTİR — ism-i mef'ûldür."),
  tok("مَوْجُودَتَانِ","mawjud","noun",["mubtada-khabar","ism-maful","al-muthanna"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.",
      "Second khabar in raf' by the alif — a dual.",
      "İkinci merfû haber, elif ile — tesniyedir."),
  tok("بَاقِيَتَانِ","baqi","noun",["mubtada-khabar","ism-fail","naqis-verbs","al-muthanna"],
      "خَبَرٌ ثَالِثٌ مَرْفُوعٌ بِالْأَلِفِ — اسْمُ فَاعِلٍ مِنَ النَّاقِصِ «بَقِيَ».",
      "Third khabar in raf' by the alif — the ism fa'il of the defective بَقِيَ.",
      "Üçüncü merfû haber, elif ile — nâkıs «بَقِيَ» fiilinin ism-i fâilidir.", punct="،"),
  tok("لَا","la-nafiya","part",[],
      "«لَا» نَافِيَةٌ غَيْرُ عَامِلَةٍ.",
      "The negating la — it governs nothing.",
      "Amel etmeyen nefiy lâsıdır."),
  tok("تَفْنَيَانِ","faniya","verb",["mudari-marfu","afal-khamsa","naqis-verbs","al-muthanna"],
      "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ.",
      "A mudari of the five verbs, in raf' by its retained NUN; the dual alif is its fa'il.",
      "Ef'âl-i hamseden muzâri; nûnun sübûtuyla merfûdur, tesniye elifi fâildir."),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ.",
      "Joining waw; the لا negates.",
      "Atıf vâvı; «لَا» nefiy içindir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَفْنَى","faniya","verb",["mudari-marfu","naqis-verbs","ism-maqsur-manqus"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.",
      "A mudari in raf' by a damma ESTIMATED on the alif — the letter cannot carry it.",
      "Elif üzerinde takdîrî damme ile merfû muzâri — elif harekeyi taşıyamaz (teazzür)."),
  tok("أَهْلُهُمَا","ahl","noun",["fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَ«هُمَا» مُضَافٌ إِلَيْهِ.",
      "The fa'il in raf', a mudaf; هُمَا is its mudaf ilayh.",
      "Merfû fâil ve muzâf; «هُمَا» muzâfun ileyhtir.",
      segments=[seg("أَهْلُ","ahl","noun"), seg("هُمَا","pron-dual","pron")], punct="."),
 ],
 "jumal": [
  J("وَهُمَا مَخْلُوقَتَانِ مَوْجُودَتَانِ بَاقِيَتَانِ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ وَأَخْبَارُهَا مُتَعَدِّدَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal clause with multiple khabars — i'rabless.",
    "Haberi müteaddit ma'tûf isim cümlesi — mahalsizdir."),
  J("لَا تَفْنَيَانِ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ رَابِعٌ.",
    "A verbal clause standing as a fourth khabar, in raf' position.",
    "Dördüncü haber olarak mahallen merfû fiil cümlesi.")]})

TITLE8 = {"ar": "السَّمْعِيَّاتُ", "en": "What Revelation Alone Reports", "tr": "Sem'iyyât"}

def g(lemma, root, pos, en, tr, lvl):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": lvl}
    if root: e["root"] = root
    return e
GLOSS_ADD = {
 "adhab": g("عَذَاب","ع ذ ب","noun","punishment","azap",3),
 "qabr": g("قَبْر","ق ب ر","noun","grave","kabir",2),
 "kafir": g("كَافِر","ك ف ر","noun","unbeliever (ism fa'il)","kâfir (ism-i fâil)",2),
 "bad": g("بَعْض","ب ع ض","noun","some, a part of","bâzı; bir kısmı",1),
 "mumin": g("مُؤْمِن","أ م ن","noun","believer (ism fa'il of Form IV)","mü'min (if'âlin ism-i fâili)",1),
 "usat": g("عُصَاة","ع ص ي","noun","the disobedient (plural of asin)","âsiler (âsînin cem'i)",4),
 "taniim": g("تَنْعِيم","ن ع م","noun","bestowing bliss (masdar)","nimetlendirme (masdar)",4),
 "sual": g("سُؤَال","س أ ل","noun","questioning (masdar)","sual; sorgu (masdar)",2),
 "munkar": g("مُنْكَر","ن ك ر","noun","Munkar (an angel of the grave)","Münker (kabir meleği)",4),
 "nakir": g("نَكِير","ن ك ر","noun","Nakir (an angel of the grave)","Nekîr (kabir meleği)",4),
 "dalil": g("دَلَائِل","د ل ل","noun","proofs (plural of dalil)","deliller (delîlin cem'i)",3),
 "samiyya": g("سَمْعِيّ","س م ع","noun","transmitted, revelation-based (nisba)","semî'; naklî (nisbe)",4),
 "bath": g("بَعْث","ب ع ث","noun","resurrection","ba's; diriliş",3),
 "wazn": g("وَزْن","و ز ن","noun","weighing (of deeds)","tartı; vezn",3),
 "kitab": g("كِتَاب","ك ت ب","noun","book, the record of deeds","kitap; amel defteri",1),
 "sirat": g("صِرَاط","ص ر ط","noun","the bridge; the path","sırat; yol",2),
 "nar": g("نَار","ن و ر","noun","fire","ateş; nâr",1),
 "mawjud": g("مَوْجُود","و ج د","noun","existent (ism maf'ul)","mevcut (ism-i mef'ûl)",3),
 "baqi": g("بَاقٍ","ب ق ي","noun","abiding, remaining (ism fa'il)","bâkî; kalıcı (ism-i fâil)",3),
 "arada": g("أَرَادَ","ر و د","verb","to will, to want","dilemek; istemek",2),
 "faniya": g("فَنِيَ","ف ن ي","verb","to perish","fânî olmak; yok olmak",3),
 "pron-dual": g("هُمَا",None,"pron","they two (dual)","o ikisi (tesniye)",2),
}

def build_morph():
    hanifa = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa/morphology.json").read_text(encoding="utf-8"))["verbs"]
    amali = json.loads((ROOT / "content/samples/bad-al-amali/morphology.json").read_text(encoding="utf-8"))["verbs"]
    return {"arada": hanifa["arada"], "faniya": amali["faniya"]}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/8.json").write_text(json.dumps({"chapter": 8, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 8 for c in man["chapters"]):
    man["chapters"].append({"n": 8, "title": TITLE8})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.6.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch8:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
