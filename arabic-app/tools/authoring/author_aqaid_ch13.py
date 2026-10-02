# -*- coding: utf-8 -*-
"""Author chapter 13 of aqaid-ahl-al-sunna — angels, books, and the mi'raj.

Continues the matn from chapter 12: the angels are Allah's servants who act
by His command and are described with neither maleness nor femaleness; Allah
has books He sent down upon His prophets, in which He made plain His command
and His prohibition, His promise and His threat; and the ascension of the
Messenger, awake and in his own person, is true.

Verbatim contiguous span, re-vowelled against the received text.
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
def g(lemma, root, pos, en, tr, level, plural=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
S = []

TITLE13 = {"ar": "الْمَلَائِكَةُ وَالْكُتُبُ وَالْمِعْرَاجُ",
           "en": "The Angels, the Books, and the Ascension",
           "tr": "Melekler, Kitaplar ve Mi'râc"}

S.append({"id": "s1", "translation": {
 "en": "And the angels are the servants of Allah the Exalted, the ones who act by His command.",
 "tr": "Melekler, Allah Teâlâ'nın emriyle iş gören kullarıdır."},
 "tokens": [
  tok("وَالْمَلَائِكَةُ","malak","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْمَلَائِكَةُ» مُبْتَدَأٌ مَرْفُوعٌ — جَمْعُ «مَلَكٍ» عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.",
      "Isti'naf waw; «the angels» is the mubtada in raf' — the plural of مَلَك on a diptote plural shape.",
      "İstinâf vâvı; «الْمَلَائِكَةُ» merfû mübtedâ — «مَلَك»in müntehe'l-cumû' vezninde cem'i.",
      segments=[seg("وَ","wa","conj"), seg("الْمَلَائِكَةُ","malak","noun")]),
  tok("عِبَادُ","abd","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ «عَبْدٍ».",
      "The khabar in raf', and a mudaf — the plural of عَبْد.",
      "Merfû haber ve muzâf — «عَبْد»in cem'i."),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "A past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır."),
  tok("الْعَامِلُونَ","amil","noun",["naat-sifa","jam-mudhakkar-salim","ism-fail"],
      "نَعْتٌ لِـ«عِبَادُ» مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ — جَمْعُ مُذَكَّرٍ سَالِمٌ، اسْمُ فَاعِلٍ مِنْ «عَمِلَ».",
      "A na't of «servants», in raf' by the WAW — a sound masculine plural, the ism fa'il of عَمِلَ.",
      "«عِبَادُ»nun na'tı, VÂV ile merfû — cem'-i müzekker-i sâlim, «عَمِلَ»nin ism-i fâili."),
  tok("بِأَمْرِهِ","amr","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«أَمْرِ» مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ مُتَعَلِّقٌ بِـ«الْعَامِلُونَ».",
      "The ba is a jarr letter; «command» is in jarr and a mudaf, the ha its mudaf ilayh — and the phrase attaches to «the ones who act».",
      "Bâ cer harfi; «أَمْرِ» mecrur ve muzâf, hâ muzâfun ileyh — câr-mecrûr «الْعَامِلُونَ»e taalluk eder.",
      segments=[seg("بِ","bi","prep"), seg("أَمْرِ","amr","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
 ],
 "jumal": [J("وَالْمَلَائِكَةُ عِبَادُ اللهِ تَعَالَى الْعَامِلُونَ بِأَمْرِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "They are not described with maleness, nor with femaleness.",
 "tr": "Onlar ne erkeklikle ne dişilikle vasıflanırlar."},
 "tokens": [
  tok("لَا","la-nafiya","part",["ma-la-mushabbaha"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "A plain negator with no government.",
      "Amel etmeyen nefiy harfi."),
  tok("يُوصَفُونَ","wasafa","verb",["naib-al-fail","afal-khamsa","mithal-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَوَاوُ الْجَمَاعَةِ نَائِبُ فَاعِلٍ — مِنَ الْمِثَالِ الْوَاوِيِّ «وَصَفَ»، وَثَبَتَتْ وَاوُهُ فِي الْمَجْهُولِ.",
      "A mudari built for the unknown, in raf' by the RETAINED nun; the waw of the group is its deputy fa'il — from the waw-initial وَصَفَ, and its waw STAYS in the passive.",
      "Nûnun sübûtuyla merfû meçhul muzâri; vâv-ı cemâat nâibü'l-fâildir — misâl-i vâvî «وَصَفَ»den, meçhulde vâvı sâbit kalır."),
  tok("بِذُكُورَةٍ","dhukura","noun",["huruf-jarr"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«ذُكُورَةٍ» مَجْرُورٌ — نَكِرَةٌ فِي سِيَاقِ النَّفْيِ فَتَعُمُّ.",
      "The ba is a jarr letter; «maleness» is in jarr — an indefinite under a negation, so it covers every kind of it.",
      "Bâ cer harfi; «ذُكُورَةٍ» mecrur — nefiy siyâkında nekiredir, umûm ifade eder.",
      segments=[seg("بِ","bi","prep"), seg("ذُكُورَةٍ","dhukura","noun")]),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
      "Joining waw; the لا re-affirms the negation.",
      "Atıf vâvı; «لَا» nefyi pekiştirir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("أُنُوثَةٍ","unutha","noun",["huruf-jarr","atf-nasaq"],
      "مَعْطُوفٌ عَلَى «ذُكُورَةٍ» مَجْرُورٌ.",
      "Joined to «maleness», in jarr.",
      "«ذُكُورَةٍ»e ma'tûf, mecrurdur.", punct="."),
 ],
 "jumal": [J("لَا يُوصَفُونَ بِذُكُورَةٍ وَلَا أُنُوثَةٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ، أَوِ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا.",
   "A verbal clause: either a second na't in the position of raf', or a fresh sentence with no place at all.",
   "Fiil cümlesi: ya mahallen merfû ikinci na't, ya da mahalsiz istinâf.")]})

S.append({"id": "s3", "translation": {
 "en": "And Allah has books which He sent down upon His prophets.",
 "tr": "Allah'ın, peygamberlerine indirdiği kitapları vardır."},
 "tokens": [
  tok("وَلِلَّهِ","allah","noun",["huruf-jarr","mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "Isti'naf waw; the lam is a jarr letter and the Name is in jarr — the phrase is a FRONTED khabar.",
      "İstinâf vâvı; lâm cer harfi, lafza-i celâl mecrur — câr-mecrûr öne geçmiş haberdir.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","prep"), seg("لَّهِ","allah","noun")]),
  tok("كُتُبٌ","kitab","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — نَكِرَتُهُ سَائِغَةٌ لِتَقَدُّمِ الْخَبَرِ.",
      "The delayed mubtada in raf' — indefinite, which is licensed because the khabar came first.",
      "Sonraya bırakılmış merfû mübtedâ — haber öne geçtiği için nekireliği câizdir."),
  tok("أَنْزَلَهَا","anzala","verb",["form-iv-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى اللهِ، وَ«هَا» مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«كُتُبٌ».",
      "A past verb, its fa'il hidden and returning to Allah, «ha» its object — and the clause is a na't of «books», in the position of raf'.",
      "Mâzî fiil; fâili Allah'a dönen müstetir zamir, «هَا» mef'ûlün bih — cümle «كُتُبٌ»un na'tı olarak mahallen merfûdur.",
      segments=[seg("أَنْزَلَ","anzala","verb"), seg("هَا","pron-3fs","pron")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("أَنْبِيَائِهِ","nabi","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَظَهَرَتِ الْكَسْرَةُ لِلْإِضَافَةِ مَعَ كَوْنِهِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.",
      "In jarr by the kasra and a mudaf, the ha its mudaf ilayh — and the kasra SHOWS, because idafa restores it to a diptote plural.",
      "Kesra ile mecrur ve muzâf, hâ muzâfun ileyh — müntehe'l-cumû' vezninde olduğu hâlde izâfet sebebiyle kesra zâhirdir.",
      segments=[seg("أَنْبِيَائِ","nabi","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
 ],
 "jumal": [J("وَلِلَّهِ كُتُبٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ قُدِّمَ خَبَرُهَا — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause with a fronted khabar — i'rabless.",
   "Haberi öne geçmiş istinâfî isim cümlesi — mahalsizdir."),
  J("أَنْزَلَهَا عَلَى أَنْبِيَائِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«كُتُبٌ».",
   "A verbal clause in the position of raf' as a na't of «books».",
   "«كُتُبٌ»un na'tı olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s4", "translation": {
 "en": "And in them He made plain His command and His prohibition, His promise and His threat.",
 "tr": "Onlarda emrini, nehyini, va'dini ve vaîdini beyan etti."},
 "tokens": [
  tok("وَبَيَّنَ","bayyana","verb",["form-ii-verbs","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«بَيَّنَ» فِعْلٌ مَاضٍ مِنْ بَابِ التَّفْعِيلِ، وَالْفَاعِلُ مُسْتَتِرٌ.",
      "Joining waw; «made plain» is a Form II past verb, its fa'il hidden.",
      "Atıf vâvı; «بَيَّنَ» tef'îl bâbından mâzî, fâili müstetirdir.",
      segments=[seg("وَ","wa","conj"), seg("بَيَّنَ","bayyana","verb")]),
  tok("فِيهَا","fi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«بَيَّنَ»، وَ«هَا» يَعُودُ عَلَى الْكُتُبِ.",
      "A jarr phrase attaching to «made plain»; the «ha» returns to the books.",
      "«بَيَّنَ»ye taalluk eden câr-mecrûr; «هَا» kitaplara döner.",
      segments=[seg("فِي","fi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("أَمْرَهُ","amr","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "The direct object in nasb and a mudaf; the ha is its mudaf ilayh.",
      "Mansub mef'ûlün bih ve muzâf; hâ muzâfun ileyhtir.",
      segments=[seg("أَمْرَ","amr","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَنَهْيَهُ","nahy","noun",["maful-bihi","atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «أَمْرَهُ» مَنْصُوبٌ — مَصْدَرُ «نَهَى».",
      "Joined to «His command», in nasb — the masdar of نَهَى.",
      "«أَمْرَهُ»ye ma'tûf, mansub — «نَهَى»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("نَهْيَ","nahy","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَوَعْدَهُ","wad","noun",["maful-bihi","atf-nasaq","idafa-definiteness","mithal-verbs"],
      "مَعْطُوفٌ مَنْصُوبٌ — مَصْدَرُ «وَعَدَ» مِنَ الْمِثَالِ الْوَاوِيِّ.",
      "Joined, in nasb — the masdar of وَعَدَ, a waw-initial verb.",
      "Ma'tûf, mansub — misâl-i vâvî «وَعَدَ»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("وَعْدَ","wad","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَوَعِيدَهُ","waid","noun",["maful-bihi","atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَنْصُوبٌ — وَالْوَعِيدُ مَا كَانَ فِي الشَّرِّ، وَالْوَعْدُ مَا كَانَ فِي الْخَيْرِ.",
      "Joined, in nasb — a «threat» is a promise of evil, where a «promise» is of good.",
      "Ma'tûf, mansub — vaîd şer, va'd ise hayır hakkındadır.",
      segments=[seg("وَ","wa","conj"), seg("وَعِيدَ","waid","noun"), seg("هُ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("وَبَيَّنَ فِيهَا أَمْرَهُ وَنَهْيَهُ وَوَعْدَهُ وَوَعِيدَهُ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ عَلَى «أَنْزَلَهَا» فِي مَحَلِّ رَفْعٍ.",
   "A verbal clause joined to «He sent them down», in the position of raf'.",
   "«أَنْزَلَهَا»ya ma'tûf fiil cümlesi — mahallen merfûdur.")]})

S.append({"id": "s5", "translation": {
 "en": "And the ascension of the Messenger of Allah — upon him be prayer and peace — while awake and in his own person, to the heaven, then to whatever of the heights Allah the Exalted willed, is true.",
 "tr": "Allah Resûlü'nün — aleyhi's-salâtü ve's-selâm — uyanık hâlde ve bizzat bedeniyle semâya, sonra Allah Teâlâ'nın dilediği yüce makamlara mi'râcı haktır."},
 "tokens": [
  tok("وَالْمِعْرَاجُ","miraj","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْمِعْرَاجُ» مُبْتَدَأٌ مَرْفُوعٌ — عَلَى وَزْنِ مِفْعَالٍ.",
      "Isti'naf waw; «the ascension» is the mubtada in raf' — on the wazn مِفْعَال.",
      "İstinâf vâvı; «الْمِعْرَاجُ» merfû mübtedâ — mif'âl vezninde.",
      segments=[seg("وَ","wa","conj"), seg("الْمِعْرَاجُ","miraj","noun")]),
  tok("لِرَسُولِ","rasul","noun",["huruf-jarr","idafa-definiteness"],
      "اللَّامُ حَرْفُ جَرٍّ، وَ«رَسُولِ» مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "The lam is a jarr letter; «Messenger» is in jarr and a mudaf.",
      "Lâm cer harfi; «رَسُولِ» mecrur ve muzâftır.",
      segments=[seg("لِ","li","prep"), seg("رَسُولِ","rasul","noun")]),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("عَلَيْهِ","ala","prep",["huruf-jarr","jumla-mutarida"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ.",
      "A jarr phrase as a fronted khabar; the whole is a parenthetic prayer.",
      "Öne geçmiş haber olan câr-mecrûr; cümle mu'teriza duâdır.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هِ","pron-3ms","pron")]),
  tok("الصَّلَاةُ","salat","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "The delayed mubtada in raf'.", "Sonraya bırakılmış merfû mübtedâ."),
  tok("وَالسَّلَامُ","salam","noun",["atf-nasaq","mubtada-khabar"],
      "مَعْطُوفٌ عَلَى «الصَّلَاةُ» مَرْفُوعٌ.",
      "Joined to «prayer», in raf'.",
      "«الصَّلَاةُ»ya ma'tûf, merfûdur.",
      segments=[seg("وَ","wa","conj"), seg("السَّلَامُ","salam","noun")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ حَالٌ.",
      "A jarr letter; the phrase stands as a hal.",
      "Cer harfi; câr-mecrûr hâldir."),
  tok("الْيَقَظَةِ","yaqaza","noun",["huruf-jarr","hal"],
      "مَجْرُورٌ بِالْكَسْرَةِ — أَيْ غَيْرَ نَائِمٍ، وَهُوَ رَدٌّ عَلَى مَنْ قَالَ إِنَّهُ مَنَامٌ.",
      "In jarr by the kasra — that is, NOT asleep; the word is placed here to answer those who said it was a dream.",
      "Kesra ile mecrur — yani uykuda değil; bunu rüya sayanlara reddiyedir."),
  tok("بِشَخْصِهِ","shakhs","noun",["huruf-jarr","hal","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«شَخْصِ» مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ بِبَدَنِهِ لَا بِالرُّوحِ وَحْدَهَا.",
      "The ba is a jarr letter; «person» is in jarr and a mudaf, the ha its mudaf ilayh — that is, in his BODY, not in spirit alone.",
      "Bâ cer harfi; «شَخْصِ» mecrur ve muzâf, hâ muzâfun ileyh — yani bedeniyle, yalnız ruhla değil.",
      segments=[seg("بِ","bi","prep"), seg("شَخْصِ","shakhs","noun"), seg("هِ","pron-3ms","pron")]),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ.",
      "A jarr letter of end-point.",
      "Gayenin sonunu bildiren cer harfi."),
  tok("السَّمَاءِ","sama","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ.", "In jarr by the kasra.", "Kesra ile mecrurdur."),
  tok("ثُمَّ","thumma","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.",
      "A joining letter: in order, and with an interval between.",
      "Tertîb ve terâhî bildiren atıf harfi."),
  tok("إِلَى","ila","prep",["huruf-jarr","atf-nasaq"],
      "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ قَبْلَهُ.",
      "Joined to the preceding jarr phrase.",
      "Öncesindeki câr-mecrûra ma'tûftur."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِـ«إِلَى».",
      "A relative noun, fixed, in the position of jarr after «ila».",
      "İsm-i mevsûl — mebnî, «إِلَى» ile mahallen mecrûr."),
  tok("شَاءَ","shaa","verb",["hollow-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A past verb; the clause is the sila — i'rabless.",
      "Mâzî fiil; cümle sıladır, mahalsizdir."),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name, the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "A past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْبَيَانِ.", "A jarr letter of explication.", "Beyan için cer harfi."),
  tok("الْعُلَى","ula","noun",["huruf-jarr","ism-maqsur-manqus"],
      "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مَقْصُورٌ، جَمْعُ «الْعُلْيَا».",
      "In jarr by a kasra ESTIMATED on its alif — a maqsur noun, the plural of الْعُلْيَا.",
      "Elifi üzerinde takdîrî kesra ile mecrur — maksûr; «الْعُلْيَا»nın cem'i."),
  tok("حَقٌّ","haqq","noun",["mubtada-khabar"],
      "خَبَرُ «الْمِعْرَاجُ» مَرْفُوعٌ — وَتَأَخَّرَ عَنْ كُلِّ هَذِهِ الْقُيُودِ لِيَقَعَ الْحُكْمُ عَلَيْهَا مَجْمُوعَةً.",
      "The khabar of «the ascension», in raf' — held back behind every one of those qualifiers so that the verdict falls on all of them TOGETHER.",
      "«الْمِعْرَاجُ»un merfû haberi — hüküm hepsinin birden üzerine düşsün diye bütün kayıtlardan sonraya bırakılmıştır.", punct="."),
 ],
 "jumal": [J("وَالْمِعْرَاجُ ... حَقٌّ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir."),
  J("عَلَيْهِ الصَّلَاةُ وَالسَّلَامُ",
   "جُمْلَةٌ اسْمِيَّةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ — لَا مَحَلَّ لَهَا.",
   "A parenthetic nominal clause of prayer — i'rabless.",
   "Mu'teriza duâ cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "malak":   g("مَلَك", "م ل ك", "noun", "angel", "melek", 1, "مَلَائِكَة"),
 "amil":    g("عَامِل", "ع م ل", "noun", "one who acts, works", "amel eden; işleyen", 2),
 "wasafa":  g("وَصَفَ", "و ص ف", "verb", "to describe", "vasfetmek; nitelemek", 2),
 "dhukura": g("ذُكُورَة", "ذ ك ر", "noun", "maleness", "erkeklik", 4),
 "unutha":  g("أُنُوثَة", "أ ن ث", "noun", "femaleness", "dişilik", 4),
 "anzala":  g("أَنْزَلَ", "ن ز ل", "verb", "to send down", "indirmek", 2),
 "bayyana": g("بَيَّنَ", "ب ي ن", "verb", "to make plain", "beyan etmek; açıklamak", 2),
 "nahy":    g("نَهْي", "ن ه ي", "noun", "prohibition (masdar)", "nehiy; yasaklama (masdar)", 3),
 "wad":     g("وَعْد", "و ع د", "noun", "promise (masdar)", "va'd; söz verme (masdar)", 2),
 "waid":    g("وَعِيد", "و ع د", "noun", "threat — a promise of evil", "vaîd — şer va'di", 4),
 "miraj":   g("مِعْرَاج", "ع ر ج", "noun", "ascension (on the wazn mif'al)", "mi'râc (mif'âl vezninde)", 3),
 "salat":   g("صَلَاة", "ص ل و", "noun", "prayer, blessing", "salât; namaz", 1),
 "yaqaza":  g("يَقَظَة", "ي ق ظ", "noun", "wakefulness", "uyanıklık", 4),
 "shakhs":  g("شَخْص", "ش خ ص", "noun", "person, bodily self", "şahıs; beden", 2),
 "sama":    g("سَمَاء", "س م و", "noun", "heaven, sky", "semâ; gök", 1),
 "haqq":    g("حَقّ", "ح ق ق", "noun", "truth, true", "hak; gerçek", 1),
 "thumma":  g("ثُمَّ", None, "part", "then (in order, after an interval)", "sonra (tertîb ve terâhî)", 1),
 "ula":     g("الْعُلَى", "ع ل و", "noun", "the heights (pl. of al-ulya)", "yüce makamlar (el-ulyâ'nın cem'i)", 4),
 "pron-3fs": g("هَا", None, "pron", "her, it (fem., attached)", "onu/onun (dişil, muttasıl)", 1),
}

def build_morph():
    samti = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json").read_text(encoding="utf-8"))["verbs"]
    out = {"anzala": samti["anzala"]}
    # وَصَفَ — the waw-initial mithal of bab ضَرَبَ. Its waw drops in the ACTIVE
    # mudari (يَصِفُ) and stays in the passive (يُوصَفُ), which is precisely the
    # rule IlalEngine's hadhf-waw-mithal encodes: the drop needs a kasra after.
    out["wasafa"] = _sg.sound1("daraba", "وَصَف", "صِف", "صِف", "وَصْف", "وَاصِف",
                               "مَوْصُوف", "وُصِفَ", "يُوصَفُ",
                               cls="مِثَالٌ وَاوِيٌّ",
                               note="مِثَالٌ وَاوِيٌّ: تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ الْمَعْلُومِ — يَصِفُ، وَتَثْبُتُ فِي الْمَجْهُولِ — يُوصَفُ.")
    out["bayyana"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "بَيَّن", "بَيِّن", "بَيِّن",
                                 "تَبْيِين", "مُبَيِّن", "مُبَيَّن")
    # The third radical is a NUN, so it meets the nun of the feminine-plural
    # suffix. sarf_gen writes the two apart (بَيَّنْنَ) while the in-app engine
    # assimilates them (بَيَّنَّ), and the paradigm-audit gate compares the two.
    # The assimilated spelling is the standard one, so the stored cells follow
    # the engine. NOTE: `amina` in chapter 12 came out of sound1() and keeps
    # the un-assimilated أَمِنْنَ, which the engine also accepts — so the two
    # generators disagree about this one boundary for Form I vs Form II. That
    # inconsistency is real and is logged in research/COVERAGE.md; do not
    # "harmonise" it by editing stored data until the engine is settled.
    for i, v in ((5, "بَيَّنَّ"), (13, "بَيَّنَّا")):
        out["bayyana"]["mazi"][i] = v
    for i, v in ((5, "يُبَيِّنَّ"), (11, "تُبَيِّنَّ")):
        out["bayyana"]["mudari"][i] = v
    out["bayyana"]["amr"][5] = "بَيِّنَّ"
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/13.json").write_text(json.dumps({"chapter": 13, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 13 for c in man["chapters"]):
    man["chapters"].append({"n": 13, "title": TITLE13})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.11.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch13:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
