# -*- coding: utf-8 -*-
"""Author chapter 13 of mukhtasar-al-manar — the SUNNA divided by transmission.

Chapter 2 defined the Sunna and moved on. Eleven chapters later the matn comes
back and divides it by how it reached us — mutawatir, mashhur, ahad — and then,
in one compressed closing sentence, says what each of the three obliges. The
chapter pays off مُتَوَاتِرًا, which stood in chapter 2 as a bare adjective on a
transmission, and now names a whole class.

ATTRIBUTION: like chapters 2–12, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • لَا يُتَصَوَّرُ — the MAJHUL of Form V, the third passive class the package
    has shown (Form X in ch10, Form I throughout, and this).
  • تَوَاطُؤُهُمْ — a Form VI masdar whose hamza rides a WAW for the damma on it,
    the same seat rule اقْتِضَاؤُهُ taught in chapter 7, and with a plural pronoun.
  • الثَّانِي — a MANQUS made definite, in jarr: the ya stands and the kasra is
    understood. Chapter 4 showed the same noun indefinite as قَاضٍ.
  • أَوِ الِاثْنَانِ — a hamzat al-wasl after a sukun, so the waw of أَوْ takes a
    kasra it does not own.
  • The closing sentence runs its verb ONCE and lets two more clauses borrow
    it. Ellipsis is not an abbreviation here; it is what makes the three
    rulings read as one graded scale.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/mukhtasar-al-manar"
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

TITLE13 = {"ar": "أَقْسَامُ السُّنَّة", "en": "The Sunna by Its Transmission",
           "tr": "Sünnetin Kısımları"}

S.append({"id": "s1", "translation": {
 "en": "Then the Sunna is of three kinds: mass-transmitted, well-known and single-chain.",
 "tr": "Sünnet üç kısımdır: mütevâtir, meşhur ve âhâd."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَالتَّرَاخِي هُنَا فِي الْكِتَابِ نَفْسِهِ: عُرِّفَتِ السُّنَّةُ فِي الْبَابِ الثَّانِي وَقُسِّمَتْ هُنَا.",
      "A letter of atf giving sequence with an interval — and the interval here is in the book itself: the Sunna was defined in chapter 2 and is divided only now, eleven chapters later. A matn defines a term where it must and works it where it can.",
      "Terâhî ile tertîb için atıf harfi — ve buradaki terâhî kitabın kendisindedir: sünnet ikinci bâbda tarif edilmiş, on bir bâb sonra burada taksîm edilmiştir. Metin, ıstılahı gerektiği yerde tarif eder, imkân bulduğu yerde işler."),
  tok("السُّنَّةُ","sunna","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ الْأَصْلُ الثَّانِي مِنَ الْأَرْبَعَةِ، وَلَمْ يُقَسَّمْ غَيْرُهُ مِنَ الْأُصُولِ.",
      "The mubtada in raf' — the second of the four sources, and the only one of them this matn divides. The Book needed no division by transmission: it came one way.",
      "Merfû mübtedâ — dört asıldan ikincisidir ve bu metnin taksîm ettiği tek asıldır. Kitâbın nakil cihetinden taksîme ihtiyacı yoktu: tek yolla gelmiştir."),
  tok("ثَلَاثَةُ","thalatha","noun",["mubtada-khabar","idafa-definiteness","tamyiz"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَالْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى مَعْدُودِهِ، وَلَحِقَتْهُ التَّاءُ لِأَنَّ مَعْدُودَهُ مُذَكَّرٌ.",
      "The khabar in raf' and a MUDAF — from three to ten the number is joined to what it counts by an idafa, and it wears the TA because what it counts is masculine. The very rule أَرْبَعَةُ أَقْسَامٍ carried in chapter 4, on a different numeral and the same counted noun.",
      "Merfû haber ve MUZÂF — üçten ona kadar sayı ma'dûduna izâfetle bağlanır ve ma'dûdu müzekker olduğu için TÂ alır. Dördüncü bâbdaki «أَرْبَعَةُ أَقْسَامٍ»in aynı kaidesi; sayı başka, ma'dûd aynı."),
  tok("أَقْسَامٍ","aqsam","noun",["idafa-definiteness","tamyiz"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الْمُمَيِّزُ فِي الْمَعْنَى.",
      "The mudaf ilayh in jarr — and the distinguisher in meaning.",
      "Mecrûr muzâfun ileyh — mânâ cihetinden mümeyyizdir.", punct="："),
  tok("مُتَوَاتِرٌ","mutawatir","noun",["badal","ism-fail","form-vi-verbs"],
      "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «تَوَاتَرَ» عَلَى مُتَفَاعِلٍ. وَقَدْ مَرَّ فِي الْبَابِ الثَّانِي مَنْصُوبًا نَعْتًا («نَقْلًا مُتَوَاتِرًا»)، وَهَا هُوَ مَرْفُوعًا بَدَلًا وَاسْمًا لِقِسْمٍ بِرَأْسِهِ.",
      "A badal of detail, in raf' — the ism fa'il of تَوَاتَرَ on مُتَفَاعِل. It stood in chapter 2 in NASB as a na't, in نَقْلًا مُتَوَاتِرًا, describing one transmission. Here it stands in RAF' as a badal and names a whole class. A word climbs from adjective to technical term as a science builds itself, and this is that climb caught in one book.",
      "Merfû tafsîl bedeli — «تَوَاتَرَ»nin MÜTEFÂİL vezninde ism-i fâili. İkinci bâbda «نَقْلًا مُتَوَاتِرًا» içinde MANSUB bir na't olarak geçmişti; burada MERFÛ bir bedeldir ve başlı başına bir kısmın adıdır. Bir ilim kurulurken kelime sıfattan ıstılaha yükselir; bu yükseliş tek bir kitapta yakalanmıştır."),
  tok("وَمَشْهُورٌ","mashhur","noun",["atf-nasaq","ism-maful"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «شَهَرَ» عَلَى مَفْعُولٍ.",
      "Joined, in raf' — the ism maf'ul of شَهَرَ on مَفْعُول: the report that was MADE well known.",
      "Ma'tûf, merfû — «شَهَرَ»in MEF'ÛL vezninde ism-i mef'ûlü: meşhur KILINMIŞ haber.",
      segments=[seg("وَ","wa","conj"), seg("مَشْهُورٌ","mashhur","noun")]),
  tok("وَآحَادٌ","aahad","noun",["atf-nasaq","mamnu-min-sarf"],
      "مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ «أَحَدٍ» عَلَى أَفْعَالٍ، وَالْمَدَّةُ فِي أَوَّلِهِ هَمْزَتَانِ: هَمْزَةُ الْوَصْلِ الْأَصْلِيَّةُ وَهَمْزَةُ الْجَمْعِ، الْتَقَتَا فَكُتِبَتَا مَدًّا.",
      "Joined, in raf' — the plural of أَحَد on أَفْعَال. The MADDA at its head is two hamzas run together: the pattern's own and the root's, meeting and written as one long stroke. آ is never a letter of its own; it is always two things at once.",
      "Ma'tûf, merfû — «أَحَد»in EF'ÂL vezninde cemi. Başındaki MEDDE iki hemzedir: veznin hemzesi ile kökün hemzesi karşılaşıp tek bir uzun çizgi olarak yazılmıştır. «آ» hiçbir zaman müstakil bir harf değildir; daima aynı anda iki şeydir.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("آحَادٌ","aahad","noun")]),
 ],
 "jumal": [J("السُّنَّةُ ثَلَاثَةُ أَقْسَامٍ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the mass-transmitted is what a body of people related, whose colluding upon a lie cannot be conceived.",
 "tr": "Mütevâtir, yalan üzerinde birleşmeleri tasavvur edilemeyen bir topluluğun rivâyet ettiğidir."},
 "tokens": [
  tok("فَالْمُتَوَاتِرُ","mutawatir","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْمُتَوَاتِرُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the mass-transmitted» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الْمُتَوَاتِرُ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْمُتَوَاتِرُ","mutawatir","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("رَوَاهُ","rawa","verb",["fail","maful-bihi","jumla-sifa","naqis-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ وَاوِيٌّ مِنْ «ر و ي»، وَالْهَاءُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ وَهِيَ الْعَائِدُ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ. وَالْأَلِفُ فِي «رَوَى» مُنْقَلِبَةٌ عَنْ يَاءٍ، وَتَظْهَرُ الْيَاءُ فِي «رَوَيْتُ».",
      "A past verb, a NAQIS from ر و ي, with the HA as its maf'ul bihi in the position of nasb — and that HA is the pronoun tying the sila to its relative. Note where the tie is: in the earlier definitions it hung on a jarr letter (مِنْهُ، بِهِ), and here it is the object itself. The alif of رَوَى is a ya in disguise, and رَوَيْتُ shows it.",
      "«ر و ي»den NÂKIS mâzî fiil; HÂ mahallen mansub mef'ûlün bihtir ve sılayı mevsûlüne bağlayan âiddir — cümle sıladır. Râbıtanın yerine dikkat: önceki tariflerde bir cer harfine asılıydı (مِنْهُ، بِهِ), burada mef'ûlün kendisidir. «رَوَى»nin elifi gizlenmiş bir yâdır; «رَوَيْتُ» onu gösterir.",
      segments=[seg("رَوَى","rawa","verb"), seg("هُ","pron-3ms","pron")]),
  tok("قَوْمٌ","qawm","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ مُنَوَّنٌ — وَجَاءَ نَكِرَةً لِأَنَّ الْمُرَادَ أَيُّ جَمَاعَةٍ بَلَغَتْ هَذَا الْحَدَّ، لَا قَوْمٌ بِعَيْنِهِمْ، وَلِذَلِكَ لَمْ يُذْكَرْ لَهُمْ عَدَدٌ.",
      "The fa'il in raf' with its tanwin, and INDEFINITE on purpose: any body of people that reaches this bar, not one named group — which is also why no NUMBER is given for them. The definition is by a property, not by a count, and that is the school's position.",
      "Tenvînli merfû fâil ve kasten NEKRE: bu ölçüye ulaşan herhangi bir topluluk; muayyen bir kavim değil. Onlara bir SAYI verilmemesinin sebebi de budur. Tarif sayıyla değil vasıfladır ve mezhebin görüşü budur."),
  tok("لَا","la-nafiya","part",["mudari-marfu","jumla-sifa"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا، وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«قَوْمٌ» — لِأَنَّ الْمَنْعُوتَ نَكِرَةٌ.",
      "«La» simply denying, and the clause after it stands in the position of raf' as a NA'T of «a body of people» — because what it describes is INDEFINITE. Had قَوْم carried ال, the very same clause would have been a hal instead. The tanwin decides.",
      "Amel etmeyen nefy «لَا»sı; sonrasındaki cümle «قَوْمٌ»un na'tı olarak mahallen merfûdur — zira men'ût NEKREdir. «قَوْم» «أَلْ» taşısaydı aynı cümle hâl olurdu. Kararı tenvîn verir."),
  tok("يُتَصَوَّرُ","tasawwara","verb",["naib-al-fail","form-v-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — مِنْ «تَصَوَّرَ» عَلَى تَفَعَّلَ، وَمَجْهُولُ الْمُضَارِعِ: ضَمُّ الْأَوَّلِ وَفَتْحُ مَا قَبْلَ الْآخِرِ. وَاسْمُ الْفَاعِلِ مِنْهُ «مُتَصَوِّر» بِالْكَسْرِ وَالْمَفْعُولُ «مُتَصَوَّر» بِالْفَتْحِ.",
      "A mudari built for the unnamed doer, in raf' — from تَصَوَّرَ on تَفَعَّلَ, and the present passive is made as always: a damma on the first letter, a fatha before the last. Note what separates this bab's two participles: مُتَصَوِّر with a kasra is the one who conceives, مُتَصَوَّر with a fatha the thing conceived. One vowel, and the app's own conjugator had them confused until this package's مُتَشَابِه caught it out.",
      "Meçhûl sîgasında merfû muzâri — «تَفَعَّلَ» vezninde «تَصَوَّرَ»den; muzârinin meçhûlü her zamanki gibidir: başı ötreli, son harften öncesi fethalı. Bu bâbın iki ism-i fâil/mef'ûlünü ayıran şeye dikkat: kesralı «مُتَصَوِّر» tasavvur eden, fethalı «مُتَصَوَّر» tasavvur edilendir. Tek hareke — ve uygulamanın kendi sarf motoru, bu paketteki «مُتَشَابِه» yakalayana kadar ikisini karıştırıyordu."),
  tok("تَوَاطُؤُهُمْ","tawatu","noun",["naib-al-fail","masdar","form-vi-verbs","idafa-definiteness"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَ«هُمْ» مُضَافٌ إِلَيْهِ — مَصْدَرُ «تَوَاطَأَ» عَلَى تَفَاعُلٍ، وَبَابُ التَّفَاعُلِ لِلْمُشَارَكَةِ وَهُوَ الْمُرَادُ هُنَا بِعَيْنِهِ. وَكُتِبَتِ الْهَمْزَةُ عَلَى الْوَاوِ لِلضَّمَّةِ، كَمَا فِي «اقْتِضَاؤُهُ».",
      "The naib al-fa'il in raf' and a mudaf, with «hum» as its mudaf ilayh — the masdar of تَوَاطَأَ on تَفَاعُل. Form VI is the form of MUTUALITY and that is exactly what is meant: not that each lied, but that they agreed together to. Its hamza rides a WAW because the vowel on it is a damma, the same seat rule اقْتِضَاؤُهُ carried in chapter 7.",
      "Merfû nâib-i fâil ve muzâf; «هُمْ» muzâfun ileyhtir — «تَوَاطَأَ»nin TEFÂUL vezninde masdarı. Tefâul bâbı MÜŞÂREKET içindir ve burada kastedilen tam olarak odur: her birinin yalan söylemesi değil, birlikte sözleşmeleri. Hemzesi damme sebebiyle VÂV üzerindedir — yedinci bâbdaki «اقْتِضَاؤُهُ»nün aynı kürsü kaidesi.",
      segments=[seg("تَوَاطُؤُ","tawatu","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«تَوَاطُؤُ» — وَالْمَصْدَرُ يَعْمَلُ عَمَلَ فِعْلِهِ فَيَتَعَلَّقُ بِهِ الْجَارُّ.",
      "A jarr letter attaching to «their colluding» — a masdar governs like its verb, so the phrase hangs on it.",
      "«تَوَاطُؤُ»a taalluk eden cer harfi — masdar fiili gibi amel eder, câr ona asılır."),
  tok("الْكَذِبِ","kadhib","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» — وَبِهِ تَمَّ الْحَدُّ: لَيْسَ الْمُرَادُ أَنَّهُمْ لَا يَكْذِبُونَ، بَلْ أَنَّ اتِّفَاقَهُمْ جَمِيعًا عَلَى كَذِبٍ وَاحِدٍ لَا يُتَصَوَّرُ.",
      "In jarr after «ala» — and with it the definition closes. What is denied is not that any of them could lie, but that ALL of them could agree on ONE lie. The strength of a mutawatir report lies in the impossibility of the agreement, not in the honesty of the men.",
      "«عَلَى» ile mecrûr — tarif onunla tamamlanır. Nefyedilen, içlerinden birinin yalan söyleyebileceği değil, HEPSİNİN TEK bir yalan üzerinde birleşebileceğidir. Mütevâtirin kuvveti, râvilerin doğruluğunda değil, bu birleşmenin imkânsızlığındadır.",
      punct="."),
 ],
 "jumal": [J("مَا رَوَاهُ قَوْمٌ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("لَا يُتَصَوَّرُ تَوَاطُؤُهُمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«قَوْمٌ».",
   "A verbal clause in the position of raf', a na't of «a body of people».",
   "«قَوْمٌ»un na'tı olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s3", "translation": {
 "en": "And the well-known is what was single-chain at its root, then became widely known in the second generation.",
 "tr": "Meşhur, aslında âhâd iken ikinci asırda şöhret bulandır."},
 "tokens": [
  tok("وَالْمَشْهُورُ","mashhur","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمَشْهُورُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the well-known» is the mubtada in raf'.",
      "Atıf vâvı; «الْمَشْهُورُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمَشْهُورُ","mashhur","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","hollow-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ.",
      "A past verb of the incomplete kind, its ISM a hidden pronoun going back to «that which»; the clause is the sila. كَانَ takes an ism in raf' and a khabar in nasb — it does not do the work of an ordinary verb, which is why the books call it naqis, «incomplete»: it gives a time and nothing else.",
      "Nâkıs mâzî fiil; İSMİ «مَا»ya râci müstetir zamîrdir, cümle sıladır. «كَانَ» ismini ref, haberini nasb eder — sıradan bir fiilin işini görmez; kitapların ona «nâkıs» demesinin sebebi budur: yalnız bir zaman bildirir, başka bir şey değil."),
  tok("آحَادًا","aahad","noun",["kana-wa-akhawatuha"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ — وَهُوَ الْقِسْمُ الثَّالِثُ، ذُكِرَ هُنَا قَبْلَ حَدِّهِ لِأَنَّ الْمَشْهُورَ لَا يُفْهَمُ إِلَّا بِهِ.",
      "«Kana»'s khabar, in nasb — and it is the THIRD kind, named here before its own definition arrives, because the well-known cannot be described without it. A matn may reach forward when the argument needs it.",
      "«كَانَ»nin mansub haberi — ÜÇÜNCÜ kısımdır ve kendi tarifinden önce burada anılmıştır; zira meşhur onsuz anlatılamaz. Metin, delil gerektirdiğinde ileriye uzanabilir."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ.",
      "A jarr letter hanging on an omitted word standing as a hal.",
      "Mahzûf bir hâle taalluk eden cer harfi."),
  tok("الْأَصْلِ","asl","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي» — وَ«الْأَصْلُ» هُنَا الطَّبَقَةُ الْأُولَى مِنَ الْإِسْنَادِ: طَبَقَةُ الصَّحَابَةِ.",
      "In jarr after «fi» — and «the root» here means the FIRST layer of the chain, the Companions' generation. The word opened the book meaning a foundation; here it means the earliest link of a transmission.",
      "«فِي» ile mecrûr — buradaki «الْأَصْل», isnâdın İLK tabakasıdır: sahâbe tabakası. Kelime kitabı «temel» mânâsında açmıştı; burada nakil zincirinin en eski halkası demektir."),
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَهُوَ هُنَا فِي مَوْضِعِهِ تَمَامًا: بَيْنَ الطَّبَقَتَيْنِ جِيلٌ كَامِلٌ.",
      "A letter of atf giving sequence WITH AN INTERVAL — and it is exactly the right letter here, because a whole generation stands between the two layers. Had the matn written فَ instead, it would have said the fame followed at once, which is a different claim.",
      "Terâhî ile tertîb için atıf harfi — ve burada tam yerindedir: iki tabaka arasında bir nesil vardır. Metin «فَ» yazsaydı şöhretin hemen ardından geldiğini söylemiş olurdu ki bu başka bir iddiadır."),
  tok("اشْتَهَرَ","ishtahara","verb",["fail","form-viii-verbs"],
      "فِعْلٌ مَاضٍ عَلَى «اِفْتَعَلَ» مِنْ «ش ه ر»، وَفَاعِلُهُ مُسْتَتِرٌ — وَالشِّينُ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ فَسَلِمَتْ تَاءُ الْوَزْنِ، كَمَا فِي «اسْتَتَرَ» فِي الْبَابِ الْعَاشِرِ.",
      "A past verb on اِفْتَعَلَ from ش ه ر, its fa'il hidden — and the shin is not among the letters that force the ibdal, so the pattern's ta stands unchanged, exactly as in اسْتَتَرَ in chapter 10. Set the two beside اِزْدَادَ and اِطَّلَعَ and the whole table is on the page.",
      "«ش ه ر»den «اِفْتَعَلَ» vezninde mâzî fiil, fâili müstetir — şîn ibdâl harflerinden değildir, bu yüzden veznin tâsı olduğu gibi kalmıştır; onuncu bâbdaki «اسْتَتَرَ» gibi. İkisini «اِزْدَادَ» ve «اِطَّلَعَ» ile yan yana koy, cetvelin tamamı sayfada olsun."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«اشْتَهَرَ».",
      "A jarr letter attaching to «became known».",
      "«اشْتَهَرَ»ye taalluk eden cer harfi."),
  tok("الْقَرْنِ","qarn","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».", "In jarr after «fi».", "«فِي» ile mecrûr."),
  tok("الثَّانِي","thani","noun",["naat-sifa","ism-maqsur-manqus"],
      "نَعْتٌ لِـ«الْقَرْنِ» مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ مُعَرَّفٌ بِـ«أَلْ»، فَبَقِيَتْ يَاؤُهُ. وَقَابِلْهُ بِـ«قَاضٍ» النَّكِرَةِ فِي بَابِ الْأَقْسَامِ: هُنَاكَ سَقَطَتِ الْيَاءُ وَعَوَّضَ عَنْهَا التَّنْوِينُ، وَهُنَا وَقَفَتْ.",
      "A na't of «the generation», in jarr by a kasra ESTIMATED on the ya, which is too heavy to carry it — a MANQUS made definite by ال, so its ya stands. Set it against the indefinite قَاضٍ of chapter 4: there the ya dropped and a tanwin took its place; here it holds. Same noun class, two states, and the article decides which face it shows.",
      "«الْقَرْنِ»in na'tı; yâ üzerinde sıkletten dolayı TAKDÎRÎ kesra ile mecrûrdur — «أَلْ» ile marife olmuş MENKŪS isimdir, bu yüzden yâsı durur. Dördüncü bâbdaki nekre «قَاضٍ» ile karşılaştır: orada yâ düşmüş, yerini tenvîn almıştı; burada yerinde kalmıştır. Aynı isim sınıfı, iki hâl; hangi yüzünü göstereceğine harf-i tarif karar verir.",
      punct="."),
 ],
 "jumal": [J("كَانَ آحَادًا فِي الْأَصْلِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("ثُمَّ اشْتَهَرَ فِي الْقَرْنِ الثَّانِي",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ عَلَى الصِّلَةِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause joined to the sila — i'rabless.",
   "Sılaya ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And the single-chain is what one man related, or two.",
 "tr": "Âhâd, bir kişinin yahut iki kişinin rivâyet ettiğidir."},
 "tokens": [
  tok("وَالْآحَادُ","aahad","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْآحَادُ» مُبْتَدَأٌ مَرْفُوعٌ — وَاجْتَمَعَ فِيهِ أَلِفُ الْوَصْلِ وَالْمَدَّةُ، فَصَارَ أَوَّلُهُ ثَلَاثَ هَمَزَاتٍ فِي الْأَصْلِ.",
      "A joining waw; «the single-chain» is the mubtada in raf'. Now the article's own alif has joined the madda, so what stands at the head of this word is, in origin, three hamzas in a row reduced to one written stroke and one alif. Arabic never says three; it writes what it says.",
      "Atıf vâvı; «الْآحَادُ» merfû mübtedâdır. Harf-i tarifin elifi meddeye eklenmiştir; kelimenin başında aslen üç hemze vardır ve bunlar tek bir çizgi ile bir elife indirilmiştir. Arapça üçünü birden söylemez; söylediğini yazar.",
      segments=[seg("وَ","wa","conj"), seg("الْآحَادُ","aahad","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("رَوَاهُ","rawa","verb",["fail","maful-bihi","jumla-sifa","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ عَائِدٌ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ. وَهُوَ عَيْنُ فِعْلِ حَدِّ الْمُتَوَاتِرِ، وَالْفَرْقُ كُلُّهُ فِي الْفَاعِلِ.",
      "A past verb, the HA its maf'ul bihi going back to «that which»; the clause is the sila. It is the SAME verb that defined the mutawatir, and the entire difference between the two classes sits in the fa'il: there an unnumbered قَوْم, here الْوَاحِدُ. The definitions are one sentence apart in wording and a whole science apart in consequence.",
      "Mâzî fiil; HÂ «مَا»ya râci mef'ûlün bihtir, cümle sıladır. Mütevâtiri tarif eden fiilin AYNISIdır ve iki sınıf arasındaki bütün fark FÂİLdedir: orada sayısı verilmemiş bir «قَوْم», burada «الْوَاحِدُ». Tarifler lafızda tek kelime, neticede bir ilim kadar uzaktır.",
      segments=[seg("رَوَى","rawa","verb"), seg("هُ","pron-3ms","pron")]),
  tok("الْوَاحِدُ","wahid","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — وَجَاءَ مَعْرِفَةً بِخِلَافِ «قَوْمٌ» النَّكِرَةِ، لِأَنَّ الْمُرَادَ الْجِنْسُ الْمَعْهُودُ: الرَّاوِي الْفَرْدُ.",
      "The fa'il in raf' — and DEFINITE, unlike the indefinite قَوْم of the first definition, because what is meant is the known kind: the single transmitter as a type. Two fa'ils in two parallel sentences, one definite and one not, and each is right for what it names.",
      "Merfû fâil — ilk tarifteki nekre «قَوْمٌ»un aksine MARİFEdir; zira kastedilen bilinen cinstir: tek râvi tipi. İki paralel cümlede iki fâil, biri marife biri nekre, ve her biri adlandırdığı şey için doğrudur."),
  tok("أَوِ","aw","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ — وَكُسِرَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ: سَكَنَتِ الْوَاوُ وَبَعْدَهَا هَمْزَةُ وَصْلٍ سَاكِنَةٌ، فَحُرِّكَتْ بِالْكَسْرِ.",
      "A letter of atf — and its WAW takes a kasra it does not own. The waw of أَوْ is silent, and the wasl hamza after it is silent too; two sukuns will not stand, so the first is broken with a kasra. The same law that turned دَفَّتَيْ into دَفَّتَيِ in chapter 2, here on a particle.",
      "Atıf harfi — ve VÂVı kendisine ait olmayan bir kesra alır. «أَوْ»in vâvı sâkindir, ardındaki vasıl hemzesi de sâkindir; iki sâkin yan yana durmaz, birincisi kesra ile harekelenir. İkinci bâbda «دَفَّتَيْ»i «دَفَّتَيِ» yapan kanunun aynısı, burada bir harf üzerinde."),
  tok("الِاثْنَانِ","ithnan","noun",["atf-nasaq","al-muthanna"],
      "مَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَنُونُهُ ثَابِتَةٌ لِأَنَّهُ غَيْرُ مُضَافٍ — وَأَلِفُهُ أَلِفُ وَصْلٍ، وَهُوَ مِنَ الْأَسْمَاءِ الْقَلِيلَةِ الَّتِي تَبْدَأُ بِهَا. وَبِهَذَا الْعَدَدِ يَنْتَهِي الْقِسْمُ: مَا زَادَ عَلَى اثْنَيْنِ وَلَمْ يَبْلُغْ حَدَّ الشُّهْرَةِ فَهُوَ آحَادٌ أَيْضًا.",
      "Joined, in raf' by the ALIF because it is a DUAL, its nun standing because nothing is added to it — and its alif is a WASL alif, one of the very few NOUNS that begin with one. The count stops at two here not because three would be different in kind, but because the definition is by the absence of a property, not by a number.",
      "ELİF ile merfû ma'tûf, zira TESNİYEdir; muzâf olmadığı için nûnu durur — ve elifi VASIL elifidir; bununla başlayan pek az İSİMden biridir. Sayının ikide durması, üçün başka bir cins olmasından değildir: tarif bir sayıyla değil, bir vasfın yokluğuyla yapılır.",
      punct="."),
 ],
 "jumal": [J("مَا رَوَاهُ الْوَاحِدُ أَوِ الِاثْنَانِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the mass-transmitted obliges the knowledge of certainty, the well-known the knowledge of settled confidence, and the single-chain, action.",
 "tr": "Mütevâtir yakîn ilmini, meşhur tuma'nînet ilmini, âhâd ise ameli îcâb ettirir."},
 "tokens": [
  tok("وَالْمُتَوَاتِرُ","mutawatir","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُتَوَاتِرُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the mass-transmitted» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُتَوَاتِرُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَوَاتِرُ","mutawatir","noun")]),
  tok("يُوجِبُ","awjaba","verb",["mudari-marfu","form-iv-verbs","mithal-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ فِي مَحَلِّ رَفْعٍ — وَهُوَ الْفِعْلُ الَّذِي بُنِيَ عَلَيْهِ حُكْمُ الْأَمْرِ وَحُكْمُ الْعَامِّ، وَهَا هُوَ يَحْمِلُ حُكْمَ الْأَقْسَامِ الثَّلَاثَةِ. رَابِعُ خَانَةٍ مِنْ صَرْفِهِ فِي هَذَا الْكِتَابِ.",
      "A mudari in raf', the clause standing as the khabar in the position of raf' — and it is the verb on which the ruling of the command was built in chapter 8 and the ruling of the general in chapter 11. Here it carries the ruling of all three kinds at once. Four chapters have now shown four cells of this one paradigm.",
      "Merfû muzâri; cümle mahallen merfû haberdir — sekizinci bâbda emrin hükmü, on birincide âmmın hükmü bu fiil üzerine kurulmuştu; burada üç kısmın hükmünü birden taşır. Dört bâb, bu tek çekimin dört hânesini göstermiş oldu."),
  tok("عِلْمَ","ilm","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "The maf'ul bihi in nasb, and a mudaf.",
      "Mansub mef'ûlün bih ve muzâf."),
  tok("الْيَقِينِ","yaqin","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْيَقِينُ أَعْلَى دَرَجَاتِ الْعِلْمِ، لَا يُخَالِطُهُ شَكٌّ.",
      "The mudaf ilayh in jarr — and yaqin is the highest degree of knowledge, with no doubt mixed into it. The scale of this sentence runs downward from here.",
      "Mecrûr muzâfun ileyh — yakîn, ilmin en yüksek derecesidir; içine şüphe karışmaz. Bu cümlenin ölçeği buradan aşağı iner.", punct="،"),
  tok("وَالْمَشْهُورُ","mashhur","noun",["atf-nasaq","mubtada-khabar"],
      "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ — وَخَبَرُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ الْأَوَّلُ.",
      "A second mubtada in raf' — and its khabar is OMITTED, the first sentence having supplied it. From here to the end of the line the verb is never written again and is understood twice.",
      "İkinci merfû mübtedâ — haberi MAHZÛFtur; birinci cümle onu göstermiştir. Buradan satır sonuna kadar fiil bir daha yazılmaz ve iki defa takdîr edilir.",
      segments=[seg("وَ","wa","conj"), seg("الْمَشْهُورُ","mashhur","noun")]),
  tok("عِلْمَ","ilm","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ «يُوجِبُ» — وَنَصْبُهُ هُوَ الدَّلِيلُ عَلَى الْحَذْفِ: لَوْلَا عَامِلٌ مُقَدَّرٌ لَمَا انْتَصَبَ.",
      "The maf'ul bihi in nasb — of an OMITTED verb, understood as «obliges». And its NASB is the proof that something was omitted: an accusative needs a governor, and there is none written. The i'rab of a word can testify to a word that is not there.",
      "MAHZÛF bir fiilin mansub mef'ûlün bihi; takdîri «يُوجِبُ»dur. Ve NASBı, hazfin delilidir: mansub bir isim âmil ister, yazılı âmil ise yoktur. Bir kelimenin i'râbı, orada bulunmayan bir kelimeye şehâdet edebilir."),
  tok("الطُّمَأْنِينَةِ","tumanina","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهِيَ دُونَ الْيَقِينِ: سُكُونُ النَّفْسِ مَعَ بَقَاءِ احْتِمَالٍ ضَعِيفٍ.",
      "The mudaf ilayh in jarr — and it stands below certainty: the settling of the soul while a faint possibility of the contrary remains. The word itself is unusually long for Arabic, and its shape is that of a quadriliteral's masdar.",
      "Mecrûr muzâfun ileyh — yakînin altındadır: zayıf bir ihtimâl kalmakla birlikte nefsin sükûn bulması. Kelimenin kendisi Arapça için alışılmadık uzunluktadır ve şekli rubâî bir masdarınkidir.", punct="،"),
  tok("وَالْآحَادُ","aahad","noun",["atf-nasaq","mubtada-khabar"],
      "مُبْتَدَأٌ ثَالِثٌ مَرْفُوعٌ — وَخَبَرُهُ مَحْذُوفٌ كَذَلِكَ.",
      "A third mubtada in raf' — its khabar omitted in the same way.",
      "Üçüncü merfû mübtedâ — haberi yine mahzûftur.",
      segments=[seg("وَ","wa","conj"), seg("الْآحَادُ","aahad","noun")]),
  tok("الْعَمَلَ","amal","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ — وَلَاحِظْ مَا لَمْ يُقَلْ: لَمْ يُذْكَرْ لِلْآحَادِ عِلْمٌ أَصْلًا، بَلِ الْعَمَلُ وَحْدَهُ. فَالسُّلَّمُ يَنْزِلُ مِنْ عِلْمِ الْيَقِينِ إِلَى عِلْمِ الطُّمَأْنِينَةِ ثُمَّ يَخْرُجُ مِنْ بَابِ الْعِلْمِ كُلِّهِ إِلَى الْعَمَلِ — وَكُلُّ ذَلِكَ بِحَذْفٍ وَمُقَابَلَةٍ، بِلَا كَلِمَةٍ زَائِدَةٍ وَاحِدَةٍ.",
      "The maf'ul bihi in nasb of an omitted verb — and notice what is NOT said. For the single-chain report no knowledge is named at all: only action. The scale descends from the knowledge of certainty to the knowledge of confidence and then steps out of the category of knowledge altogether into deed. Three rulings, one written verb, and not a single wasted word. This is what the balagha books mean when they say that ellipsis can say more than statement.",
      "Mahzûf bir fiilin mansub mef'ûlün bihi — ve SÖYLENMEYENE dikkat et. Âhâd için hiçbir ilim zikredilmemiştir; yalnız amel. Ölçek, yakîn ilminden tuma'nînet ilmine iner, sonra ilim kategorisinden büsbütün çıkıp amele geçer. Üç hüküm, tek yazılı fiil ve fazladan tek kelime yok. Belâgat kitaplarının «hazif, sarâhatten çok söyler» derken kastettiği budur.",
      punct="."),
 ],
 "jumal": [J("الْمُتَوَاتِرُ يُوجِبُ عِلْمَ الْيَقِينِ",
   "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause whose khabar is a verbal clause — i'rabless.",
   "Haberi fiil cümlesi olan isim cümlesi — mahalsizdir."),
  J("وَالْمَشْهُورُ عِلْمَ الطُّمَأْنِينَةِ",
   "جُمْلَةٌ مَعْطُوفَةٌ حُذِفَ عَامِلُهَا لِدَلَالَةِ الْأَوَّلِ عَلَيْهِ.",
   "A joined clause whose governor is omitted, the first having pointed to it.",
   "Âmili, birincinin delâletiyle hazfedilmiş ma'tûf cümle.")]})

GLOSS_ADD = {
 "mashhur":  g("مَشْهُور", "ش ه ر", "noun", "the WELL-KNOWN — single-chain at root, famous by the second generation", "meşhur — aslı âhâd, ikinci asırda şöhret bulan", 4),
 "aahad":    g("آحَاد", "أ ح د", "noun", "SINGLE-CHAIN reports (plural of أَحَد)", "âhâd — tek râvili haberler", 4),
 "rawa":     g("رَوَى", "ر و ي", "verb", "to relate, to transmit (a report)", "rivâyet etmek", 3),
 "ishtahara": g("اِشْتَهَرَ", "ش ه ر", "verb", "to become widely known", "şöhret bulmak, meşhur olmak", 4),
 "qawm":     g("قَوْم", "ق و م", "noun", "a people, a group", "kavim, topluluk", 2),
 "kadhib":   g("كَذِب", "ك ذ ب", "noun", "falsehood, lying", "yalan", 2),
 "thalatha": g("ثَلَاثَة", "ث ل ث", "noun", "three", "üç", 1),
 "tawatu":   g("تَوَاطُؤ", "و ط أ", "noun", "collusion, agreeing together (masdar, Form VI)", "tevâtu'; birlikte sözleşme (masdar)", 5),
 "tasawwara": g("تَصَوَّرَ", "ص و ر", "verb", "to conceive, form a notion of", "tasavvur etmek", 4),
 "qarn":     g("قَرْن", "ق ر ن", "noun", "an age, a generation", "asır, karn", 3, plural="قُرُون"),
 "thani":    g("ثَانِي", "ث ن ي", "noun", "second (ordinal; a manqus noun)", "ikinci (menkūs isim)", 2),
 "ithnan":   g("اِثْنَانِ", "ث ن ي", "noun", "two", "iki", 1),
 "yaqin":    g("يَقِين", "ي ق ن", "noun", "certainty — knowledge with no doubt in it", "yakîn; şüphesiz bilgi", 4),
 "tumanina": g("طُمَأْنِينَة", "ط م أ ن", "noun", "settled confidence — below certainty (masdar)", "tuma'nînet; yakînin altındaki sükûn", 5),
 "pron-3mp": g("هُمْ", None, "pron", "them, their (masc. plural, attached)", "onlar, -leri (cemi müzekker)", 1),
}

def build_morph():
    out = {}
    # تَصَوَّرَ — COPIED, and it is the witness in this chapter's own i'rab: its
    # stored participles (مُتَصَوِّر / مُتَصَوَّر) are the pair the conjugator was
    # getting wrong until v113.
    s = json.loads((ROOT / "content/samples/aqaid-ahl-al-sunna/morphology.json").read_text(encoding="utf-8"))
    out["tasawwara"] = s["verbs"]["tasawwara"]
    # رَوَى — NAQIS. The lam is a ya (ر و ي) and the mazi ends in an alif that
    # is that ya in disguise; the ـتُ persons bring it back.
    out["rawa"] = _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "رَوَ", "رْو", "i", "اِرْوِ",
                             "رِوَايَة", "رَاوٍ (الرَّاوِي)",
                             maful="مَرْوِيّ", pmz="رُوِيَ", pmd="يُرْوَى",
                             note="نَاقِصٌ يَائِيٌّ: لَمْ يَرْوِ.")
    # اِشْتَهَرَ — Form VIII, sound. The shin forces no ibdal.
    out["ishtahara"] = _sg.derived("بَابُ الِافْتِعَالِ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ",
                                   "اِشْتَهَر", "شْتَهِر", "اِشْتَهِر", "اِشْتِهَار", "مُشْتَهِر",
                                   note="لَمْ تُبْدَلْ تَاءُ الِافْتِعَالِ لِأَنَّ الشِّينَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/13.json").write_text(
    json.dumps({"chapter": 13, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 13 for c in man["chapters"]):
    man["chapters"].append({"n": 13, "title": TITLE13})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.13.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch13:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
