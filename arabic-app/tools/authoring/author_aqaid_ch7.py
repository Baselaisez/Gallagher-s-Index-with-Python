# -*- coding: utf-8 -*-
"""Author chapter 7 of aqaid-ahl-al-sunna — khalq al-af'al and istita'a.

Continues the matn where chapter 6 stopped: Allah as creator of every deed
of His servants, the servants' own chosen acts for which they are rewarded
and punished, and the power that comes WITH the act. Verbatim contiguous
spans re-vowelled against the received text; pending-scholarly-review.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2] if '__file__' in dir() else pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
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
 "en": "And Allah the Exalted is the creator of all the deeds of His servants — of unbelief and faith, obedience and disobedience.",
 "tr": "Allah Teâlâ, kullarının bütün fiillerinin yaratıcısıdır — küfrün ve imanın, taatin ve isyanın."},
 "tokens": [
  tok("وَاللهُ","allah","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.",
      "Isti'naf waw; the majestic name is the mubtada in raf'.",
      "İstinâf vâvı; lafza-i celâl merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("اللهُ","allah","noun")]),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'teriza cümlesidir."),
  tok("خَالِقٌ","khaliq","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «خَلَقَ» عَامِلٌ عَمَلَ فِعْلِهِ.",
      "Khabar in raf' — the ism fa'il of خَلَقَ, governing as its verb would.",
      "Merfû haber — «خَلَقَ» fiilinin ism-i fâili; fiilinin amelini yapar."),
  tok("لِأَفْعَالِ","li","prep",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«خَالِقٌ»، وَ«أَفْعَالِ» مُضَافٌ.",
      "Preposition-phrase attached to خَالِق; أَفْعَال is a mudaf.",
      "«خَالِقٌ»a mütealliḳ câr-mecrûr; «أَفْعَالِ» muzâftır.",
      segments=[seg("لِ","li","prep"), seg("أَفْعَالِ","afal","noun")]),
  tok("الْعِبَادِ","ibad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «عَبْد».",
      "Mudaf ilayh in jarr — the plural of عَبْد.",
      "Mecrûr muzâfun ileyh — «عَبْد» kelimesinin cem'idir."),
  tok("كُلِّهَا","kull","noun",["tawkid","idafa-definiteness"],
      "تَوْكِيدٌ مَعْنَوِيٌّ لِـ«أَفْعَالِ» مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A ma'nawi tawkid of أَفْعَال, in jarr; the ha is its mudaf ilayh.",
      "«أَفْعَالِ»in mecrûr ma'nevî te'kidi; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("كُلِّ","kull","noun"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْبَيَانِ.",
      "The jarr letter of explanation — «namely».",
      "Beyân bildiren cer harfi — «yani»."),
  tok("الْكُفْرِ","kufr","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ» بَيَانًا لِلْأَفْعَالِ.",
      "In jarr after مِنْ, explaining what those deeds are.",
      "«مِنْ» ile mecrur; fiillerin ne olduğunu beyân eder."),
  tok("وَالْإِيمَانِ","iman","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ.",
      "Joined to it, in jarr.",
      "Ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("الْإِيمَانِ","iman","noun")]),
  tok("وَالطَّاعَةِ","taa","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ.",
      "Joined to it, in jarr.",
      "Ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("الطَّاعَةِ","taa","noun")]),
  tok("وَالْعِصْيَانِ","isyan","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ.",
      "Joined to it, in jarr.",
      "Ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("الْعِصْيَانِ","isyan","noun")], punct="."),
 ],
 "jumal": [J("وَاللهُ تَعَالَى خَالِقٌ لِأَفْعَالِ الْعِبَادِ كُلِّهَا",
   "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
   "A resumed nominal clause — i'rabless.",
   "Müste'nefe isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And they are all by His will, His volition, His judgement, His decree and His measuring-out.",
 "tr": "Bunların hepsi O'nun irâdesi, meşîeti, hükmü, kazâsı ve takdiriyledir."},
 "tokens": [
  tok("وَهِيَ","pron-3fs-munfasil","pron",["mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«هِيَ» مُبْتَدَأٌ.",
      "Joining waw; هِيَ is the mubtada.",
      "Atıf vâvı; «هِيَ» mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","pron-3fs-munfasil","pron")]),
  tok("كُلُّهَا","kull","noun",["tawkid","idafa-definiteness"],
      "تَوْكِيدٌ مَعْنَوِيٌّ لِلْمُبْتَدَإِ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A ma'nawi tawkid of the mubtada, in raf'; the ha is its mudaf ilayh.",
      "Mübtedanın merfû ma'nevî te'kidi; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("كُلُّ","kull","noun"), seg("هَا","pron-3fs","pron")]),
  tok("بِإِرَادَتِهِ","bi","prep",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A preposition-phrase standing as the khabar, in raf' position; the ha is the mudaf ilayh.",
      "Haber olarak mahallen merfû câr-mecrûr; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("بِ","bi","prep"), seg("إِرَادَتِ","irada","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَمَشِيئَتِهِ","mashia","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joined in jarr; the ha is its mudaf ilayh.",
      "Ma'tûf ve mecrur; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("مَشِيئَتِ","mashia","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَحُكْمِهِ","hukm","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joined in jarr; the ha is its mudaf ilayh.",
      "Ma'tûf ve mecrur; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("حُكْمِ","hukm","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَقَضَائِهِ","qada","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joined in jarr; the ha is its mudaf ilayh.",
      "Ma'tûf ve mecrur; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("قَضَائِ","qada","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَتَقْدِيرِهِ","taqdir","noun",["atf-nasaq","idafa-definiteness","form-ii-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ «قَدَّرَ»، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joined in jarr — the masdar of قَدَّرَ (Form II); the ha is its mudaf ilayh.",
      "Ma'tûf ve mecrur — «قَدَّرَ» (tef'îl) masdarı; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("تَقْدِيرِ","taqdir","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("وَهِيَ كُلُّهَا بِإِرَادَتِهِ وَمَشِيئَتِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined nominal clause — i'rabless.",
   "Ma'tûf isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the servants have chosen acts, for which they are rewarded and for which they are punished.",
 "tr": "Kulların ihtiyârî fiilleri vardır; onlarla sevap kazanır, onlardan dolayı cezalandırılırlar."},
 "tokens": [
  tok("وَلِلْعِبَادِ","li","prep",["huruf-jarr","mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "Isti'naf waw; the preposition-phrase is a fronted khabar.",
      "İstinâf vâvı; câr-mecrûr haber-i mukaddemdir.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","prep"), seg("الْعِبَادِ","ibad","noun")]),
  tok("أَفْعَالٌ","afal","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.",
      "The delayed mubtada, in raf'.",
      "Sonraya bırakılmış merfû mübtedadır."),
  tok("اخْتِيَارِيَّةٌ","ikhtiyari","noun",["naat-sifa","form-viii-verbs"],
      "نَعْتٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى «الِاخْتِيَار»، مَصْدَرِ «اخْتَارَ».",
      "A na't in raf' — the nisba of الِاخْتِيَار, the masdar of اخْتَارَ (Form VIII).",
      "Merfû na't — «اخْتَارَ» (iftiâl) masdarı «الِاخْتِيَار»a nisbettir."),
  tok("يُثَابُونَ","athaba","verb",["naib-al-fail","mudari-marfu","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ نَائِبُ الْفَاعِلِ، وَالْجُمْلَةُ نَعْتٌ ثَانٍ.",
      "A passive mudari in raf' by its retained nun; the waw is the deputy fa'il, and the clause is a second na't.",
      "Nûnun sübûtuyla merfû meçhul muzâri; vâv nâibü'l-fâildir, cümle ikinci na'ttır.",
      segments=[seg("يُثَابُ","athaba","verb"), seg("ونَ","pron-3mp","pron")]),
  tok("بِهَا","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُثَابُونَ».",
      "Preposition-phrase attached to يُثَابُونَ.",
      "«يُثَابُونَ»e mütealliḳ câr-mecrûr.",
      segments=[seg("بِ","bi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("وَيُعَاقَبُونَ","aqaba","verb",["atf-nasaq","naib-al-fail","form-iii-verbs"],
      "مَعْطُوفٌ عَلَى «يُثَابُونَ» — مُضَارِعٌ مَجْهُولٌ مِنْ «عَاقَبَ».",
      "Joined to يُثَابُونَ — a passive mudari of عَاقَبَ (Form III).",
      "«يُثَابُونَ»e ma'tûf — «عَاقَبَ» (mufâale) fiilinin meçhul muzârisi.",
      segments=[seg("وَ","wa","conj"), seg("يُعَاقَبُ","aqaba","verb"), seg("ونَ","pron-3mp","pron")]),
  tok("عَلَيْهَا","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُعَاقَبُونَ».",
      "Preposition-phrase attached to يُعَاقَبُونَ.",
      "«يُعَاقَبُونَ»e mütealliḳ câr-mecrûr.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هَا","pron-3fs","pron")], punct="."),
 ],
 "jumal": [
  J("وَلِلْعِبَادِ أَفْعَالٌ اخْتِيَارِيَّةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ مِنْ خَبَرٍ مُقَدَّمٍ وَمُبْتَدَإٍ مُؤَخَّرٍ — لَا مَحَلَّ لَهَا.",
    "A nominal clause of fronted khabar and delayed mubtada — i'rabless.",
    "Haber-i mukaddem ve mübteda-i muahhardan kurulu isim cümlesi — mahalsizdir."),
  J("يُثَابُونَ بِهَا",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«أَفْعَالٌ».",
    "A verbal clause in raf' position, a na't of أَفْعَال.",
    "«أَفْعَالٌ»un na'tı olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s4", "translation": {
 "en": "And the power is with the act, and the servant is not charged with what is not within his capacity.",
 "tr": "İstitâat fiille beraberdir; kul, gücünün yetmediği şeyle mükellef tutulmaz."},
 "tokens": [
  tok("وَالِاسْتِطَاعَةُ","istitaa","noun",["mubtada-khabar","form-x-verbs","masdar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الِاسْتِطَاعَةُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «اسْتَطَاعَ».",
      "Isti'naf waw; الِاسْتِطَاعَة is the mubtada in raf' — the masdar of اسْتَطَاعَ (Form X).",
      "İstinâf vâvı; «الِاسْتِطَاعَةُ» merfû mübteda — «اسْتَطَاعَ» (istif'âl) masdarıdır.",
      segments=[seg("وَ","wa","conj"), seg("الِاسْتِطَاعَةُ","istitaa","noun")]),
  tok("مَعَ","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ، وَهُوَ مُضَافٌ.",
      "An adverbial zarf in nasb standing as the khabar, in raf' position; a mudaf.",
      "Haber olarak mahallen merfû mensub zarf; muzâftır."),
  tok("الْفِعْلِ","fil","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir.", punct="."),
 ],
 "jumal": [
  J("وَالِاسْتِطَاعَةُ مَعَ الْفِعْلِ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause — i'rabless.",
    "Müste'nefe isim cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the servant is not charged with what is not within his capacity.",
 "tr": "Kul, gücünün yetmediği şeyle mükellef tutulmaz."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",[],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ — وَقَعَتْ بَعْدَ تَمَامِ الْكَلَامِ، وَ«لَا» نَافِيَةٌ.",
      "An isti'naf waw — it comes after a completed sentence, not joining to it; the لا negates.",
      "İstinâf vâvı — tam bir cümleden sonra gelmiştir, atıf için değildir; «لَا» nefiy içindir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُكَلَّفُ","kallafa","verb",["naib-al-fail","mudari-marfu","form-ii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.",
      "A passive mudari in raf'.",
      "Merfû meçhul muzâri fiildir."),
  tok("الْعَبْدُ","abd","noun",["naib-al-fail"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.",
      "The deputy fa'il, in raf'.",
      "Merfû nâibü'l-fâildir."),
  tok("بِمَا","bi","prep",["huruf-jarr","ism-mawsul"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» مَوْصُولَةٌ مَجْرُورَةٌ بِهَا.",
      "The ba is a jarr letter and «ma» is the relative, in jarr after it.",
      "Bâ cer harfi, «mâ» mevsûledir ve onunla mecrurdur.",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("لَيْسَ","laysa","verb",["kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "A defective past verb with a hidden ism; the clause is the sila of the relative.",
      "Nâkıs mâzî fiil, ismi gizli zamir; cümle mevsûlün sılasıdır."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("وُسْعِهِ","wus","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ «لَيْسَ».",
      "In jarr and a mudaf; the phrase stands as laysa's khabar, in nasb position.",
      "Mecrur ve muzâf; câr-mecrûr, «leyse»nin haberi olarak mahallen mensubdur.",
      segments=[seg("وُسْعِ","wus","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [
  J("وَلَا يُكَلَّفُ الْعَبْدُ بِمَا لَيْسَ فِي وُسْعِهِ",
    "جُمْلَةٌ فِعْلِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed verbal clause — i'rabless.",
    "Müste'nefe fiil cümlesi — mahalsizdir."),
  J("لَيْسَ فِي وُسْعِهِ",
    "جُمْلَةٌ صِلَةٌ لِـ«مَا» — لَا مَحَلَّ لَهَا.",
    "The sila clause of «ma» — i'rabless.",
    "«Mâ»nın sıla cümlesi — mahalsizdir.")]})

TITLE7 = {"ar": "خَلْقُ الْأَفْعَالِ وَالِاسْتِطَاعَةُ",
          "en": "The Creation of Deeds and Human Power",
          "tr": "Halk-ı Ef'âl ve İstitâat"}

def g(lemma, root, pos, en, tr, lvl):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": lvl}
    if root: e["root"] = root
    return e
GLOSS_ADD = {
 "khaliq": g("خَالِق","خ ل ق","noun","creator (ism fa'il)","yaratıcı; hâlik (ism-i fâil)",3),
 "afal": g("أَفْعَال","ف ع ل","noun","deeds, acts (plural of fi'l)","fiiller (fi'lin cem'i)",2),
 "ibad": g("عِبَاد","ع ب د","noun","servants (plural of abd)","kullar (abdin cem'i)",2),
 "abd": g("عَبْد","ع ب د","noun","servant, slave","kul; abd",1),
 "kufr": g("كُفْر","ك ف ر","noun","unbelief","küfür",3),
 "iman": g("إِيمَان","أ م ن","noun","faith","îman",1),
 "taa": g("طَاعَة","ط و ع","noun","obedience","tâat; itaat",2),
 "isyan": g("عِصْيَان","ع ص ي","noun","disobedience","isyan",3),
 "irada": g("إِرَادَة","ر و د","noun","will","irâde",3),
 "mashia": g("مَشِيئَة","ش ي أ","noun","volition","meşîet; dileme",4),
 "hukm": g("حُكْم","ح ك م","noun","judgement, ruling","hüküm",2),
 "qada": g("قَضَاء","ق ض ي","noun","decree","kazâ",3),
 "taqdir": g("تَقْدِير","ق د ر","noun","measuring-out, predestining (masdar)","takdir (masdar)",4),
 "ikhtiyari": g("اخْتِيَارِيّ","خ ي ر","noun","chosen, voluntary (nisba)","ihtiyârî (nisbe)",4),
 "athaba": g("أَثَابَ","ث و ب","verb","to reward","sevap vermek; mükâfatlandırmak",4),
 "aqaba": g("عَاقَبَ","ع ق ب","verb","to punish","cezalandırmak",3),
 "istitaa": g("اسْتِطَاعَة","ط و ع","noun","power, capacity (masdar)","istitâat; güç (masdar)",4),
 "maa": g("مَعَ",None,"noun","with, together with","ile; beraber",1),
 "kull": g("كُلّ","ك ل ل","noun","all, every; the whole of it","hep; bütün; tamamı",1),
 "fil": g("فِعْل","ف ع ل","noun","act, deed; verb","fiil",1),
 "kallafa": g("كَلَّفَ","ك ل ف","verb","to charge with, oblige","mükellef tutmak",3),
 "wus": g("وُسْع","و س ع","noun","capacity, what one can bear","vüs'; güç yetirilen",4),
 "pron-3fs-munfasil": g("هِيَ",None,"pron","she / it (detached)","o (müennes, munfasıl)",1),
 "pron-3mp": g("ـونَ",None,"pron","they (attached)","onlar (bitişik)",1),
 "pron-3fs": g("ـهَا",None,"pron","her / its (attached)","onun (müennes, bitişik)",1),
}

def build_morph():
    src = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json").read_text(encoding="utf-8"))["verbs"]
    out = {"kallafa": src["kallafa"]}
    # Form III wears DAMMA on its mudari' prefix — يُعَاقِبُ, not يِعَاقِبُ.
    out["aqaba"] = _sg.derived(_sg.B3, _sg.W3, "ُ", "عَاقَب", "عَاقِب", "عَاقِب",
                               "مُعَاقَبَة", "مُعَاقِب", "مُعَاقَب", "عُوقِبَ", "يُعَاقَبُ")
    # أَثَابَ — hollow waw of the if'al road, on the أَغَاثَ pattern
    out["athaba"] = _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ", _sg.W4, "ُ",
                                       "أَثَاب", "أَثَب", "ثِيب", "ثِب", "أَثِيب", "أَثِب",
                                       "إِثَابَة", "مُثِيب", "مُثَاب", "أُثِيبَ", "يُثَابُ",
                                       "أَجْوَفُ مِنَ الْإِفْعَالِ: يُثِيبُ ← لَمْ يُثِبْ.")
    return out

DIVERGENCE = (
 " In 7:s2 the app reads «وَقَضَائِهِ» where the supplied transcription has "
 "«وقضيته»: the received formula of the matn pairs قَضَاء with قَدَر, and the "
 "source's reading looks like a transcription slip. The received wording is "
 "used and the divergence recorded here.")
DIVERGENCE_TR = (
 " 7:s2'de uygulama «وَقَضَائِهِ» okur; verilen transkripsiyonda «وقضيته» "
 "geçmektedir. Metnin mütedâvel rivayeti قَضَاء ile قَدَر'i birlikte anar; "
 "kaynaktaki okuyuş istinsah hatası görünmektedir. Mütedâvel lafız esas "
 "alınmış, fark burada kaydedilmiştir.")

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
for lang, txt in (("en", DIVERGENCE), ("tr", DIVERGENCE_TR)):
    a = man["attribution"].get(lang, "")
    if "7:s2" not in a:
        man["attribution"][lang] = a + txt
(PKG / "chapters/7.json").write_text(json.dumps({"chapter": 7, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 7 for c in man["chapters"]):
    man["chapters"].append({"n": 7, "title": TITLE7})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.5.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch7:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
