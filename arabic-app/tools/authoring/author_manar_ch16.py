# -*- coding: utf-8 -*-
"""Author chapter 16 of mukhtasar-al-manar — IJTIHAD AND TAQLID, and the book
closes its own ring.

Fifteen chapters have been about the SOURCES and the WORDING: what the Law is
made of and how its words behave. This one is about the reader of them. It
defines the effort, states its conditions, forbids the man who has not met them
from speaking, defines what the rest of us do instead, and ends by assigning
every person to one of the two. That last sentence is the only place in the
book that addresses a PERSON rather than a text, which is why it comes last.

The conditions in s2 are chapter 2's four sources, word for word, in the same
order — there in RAF' as the things the Law is known BY, here in JARR as the
things the mujtahid must know. A matn that ends where it began has finished.

ATTRIBUTION: like chapters 2–15, set from the RECEIVED matn of the Hanafi usul
tradition. s1 is the standard definition of ijtihad carried by al-Nasafi and
the commentaries; s4 is the received definition of taqlid; s5 is the qaida in
its usual wording.

Grammar this chapter is chosen to teach:
  • بَذْلُ الْفَقِيهِ وُسْعَهُ — إِعْمَالُ الْمَصْدَر, a masdar governing exactly like
    its verb: the majrur after it is its FA'IL and the mansub after that is its
    MAF'UL BIH. A new note.
  • أَنْ يُفْتِيَ — a NAQIS verb in nasb, and the fatha is WRITTEN. Chapter 15's
    يَجْرِي had its damma estimated on the same letter for the same reason it is
    written here: the fatha is light and the ya can carry it.
  • فَعَلَيْهِ التَّقْلِيدُ — the jawab of a REAL condition, where the fa is
    OBLIGATORY because the answer is a nominal sentence. Set against chapter
    15's فَغَيْرُهُ, where a relative merely BORROWED the conditional sense.
  • بِمَا لَا يَعْلَمُ — a sila whose vacancy is in the MAF'UL seat, not the
    fa'il's. The v117 rule reads the fa'il's; this sentence is deliberately the
    case it does not reach, and the bank is where that shows.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/mukhtasar-al-manar"
sys.path.insert(0, str(ROOT / "tools/authoring"))
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
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
S = []

TITLE16 = {"ar": "الِاجْتِهَادُ وَالتَّقْلِيد",
           "en": "Ijtihad and Taqlid",
           "tr": "İctihâd ve Taklîd"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "And ijtihad is the jurist's expending of his utmost capacity in seeking the ruling of the Law.",
 "tr": "İctihâd, fakîhin şer'î hükmü aramakta bütün gücünü sarf etmesidir."},
 "tokens": [
  tok("وَالِاجْتِهَادُ","ijtihad","noun",["mubtada-khabar","masdar","form-viii-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الِاجْتِهَادُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «اِجْتَهَدَ» عَلَى اِفْتِعَالٍ مِنْ «ج ه د»، وَقَدْ ذُكِرَ فِي الْبَابِ الثَّالِثِ عَشَرَ اسْمًا وَلَمْ يُحَدَّ.",
      "A resuming waw, and «ijtihad» is the mubtada in raf' — the Form VIII masdar of اِجْتَهَدَ from ج ه د, the root of effort. The word stood in chapter 13 as a bare term; only here is it defined. Fifteen chapters have been about the TEXTS; this one is about the man reading them, and it is the last thing the book has to say.",
      "İsti'nâf vâvı; «الِاجْتِهَاد» merfû mübtedâdır — «ج ه د»den iftiâl vezninde «اِجْتَهَدَ»nin masdarı; cehd kökünden. Kelime on üçüncü bâbda çıplak bir terim olarak geçmiş, tarif edilmemişti. On beş bâb METİNLER üzerineydi; bu bâb onları okuyan insan üzerinedir ve kitabın söyleyecek son sözüdür."),
  tok("بَذْلُ","badhl","noun",["mubtada-khabar","masdar","imal-al-masdar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ عَمَلَ فِعْلِهِ: أُضِيفَ إِلَى فَاعِلِهِ وَنَصَبَ مَفْعُولَهُ.",
      "The khabar in raf' and a mudaf — and it is a masdar WORKING like its own verb. Watch the next two words: the majrur after it is not merely annexed to it, it is its FA'IL, and the word after that is its MAF'UL BIH in nasb. «بَذَلَ الْفَقِيهُ وُسْعَهُ» has been folded into a noun without losing a single one of its parts.",
      "Merfû haber ve muzâf — ve kendi fiilinin amelini yapan bir MASDARdır. Sonraki iki kelimeye bakın: ardındaki mecrûr sadece ona muzâfun ileyh değil, FÂİLidir; ondan sonraki de mansub MEF'ÛLÜN BİHidir. «بَذَلَ الْفَقِيهُ وُسْعَهُ» cümlesi, hiçbir parçasını kaybetmeden bir isme katlanmıştır."),
  tok("الْفَقِيهِ","faqih","noun",["idafa-definiteness","imal-al-masdar","fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ لَفْظًا، وَهُوَ فَاعِلُ الْمَصْدَرِ مَعْنًى — «مَنْ يَبْذُلُ» هُوَ الْفَقِيهُ.",
      "The mudaf ilayh in jarr by its FORM, and the masdar's fa'il in MEANING — the one doing the expending is the jurist. Two i'rabs on one word, and neither cancels the other: this is the same double reading the phrase layer gives بَيْنَ يَدَيْهِ, but here it is the government that doubles rather than the sense.",
      "LAFZAN mecrûr muzâfun ileyh, MÂNEN masdarın fâili — sarf edenin kendisi fakîhtir. Tek kelimede iki i'râb ve hiçbiri ötekini iptal etmez: «بَيْنَ يَدَيْهِ»e ibare katmanının verdiği çift okuyuşun aynısı; şu farkla ki burada ikilenen mânâ değil AMELdir."),
  tok("وُسْعَهُ","wus","noun",["maful-bihi","imal-al-masdar","idafa-definiteness"],
      "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ بِالْفَتْحَةِ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَنَصْبُهُ هُوَ الدَّلِيلُ عَلَى أَنَّ «بَذْلَ» عَمِلَ.",
      "The masdar's maf'ul bihi, in nasb by the fatha, itself a mudaf with the ha annexed to it — and THIS FATHA IS THE PROOF that «badhl» governed at all. Had the masdar merely been a noun, a second annexation would have followed: بَذْلُ الْفَقِيهِ وُسْعِهِ. The kasra would have been possible Arabic and a different sentence; the fatha is what makes this one a definition of an ACT.",
      "Masdarın fetha ile mansub mef'ûlün bihi; kendisi de muzâftır, hâ muzâfun ileyhtir — VE BU FETHA, «بَذْل»ün amel ettiğinin DELİLİdir. Masdar sadece bir isim olsaydı ikinci bir izâfet gelirdi: بَذْلُ الْفَقِيهِ وُسْعِهِ. Kesra da Arapça olurdu ve başka bir cümle olurdu; bu cümleyi bir FİİLİN tarifi yapan şey fethadır.",
      segments=[seg("وُسْعَ","wus","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«بَذْلُ» — وَتَعَلُّقُ الْجَارِّ بِمَصْدَرٍ دَلِيلٌ آخَرُ عَلَى عَمَلِهِ.",
      "A jarr letter attaching to «badhl» — and a jarr phrase hanging on a masdar is one more sign that the masdar is doing a verb's work. Nothing hangs in the air, and what this one hangs on is a noun with a verb's meaning.",
      "«بَذْل»e taalluk eden cer harfi — ve bir câr-mecrûrun masdara taalluk etmesi, onun amel ettiğinin bir başka delilidir. Hiçbir şey boşlukta durmaz; bunun asıldığı yer de fiil mânâsı taşıyan bir isimdir."),
  tok("طَلَبِ","talab","noun",["idafa-definiteness","masdar"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — مَصْدَرٌ ثَانٍ فِي الْجُمْلَةِ، وَقَدْ أُضِيفَ إِلَى مَفْعُولِهِ لَا إِلَى فَاعِلِهِ.",
      "Majrur by «fi» and itself a mudaf — a SECOND masdar in one sentence, and this one is annexed to its OBJECT rather than to its doer: what is sought is the ruling. Two masdars, two different annexations, side by side — which is exactly how the grammar books teach the distinction.",
      "«فِي» ile mecrûr ve muzâf — tek cümlede İKİNCİ masdar; ve bu, fâiline değil MEF'ÛLÜNE izâfe edilmiştir: aranan şey hükümdür. İki masdar, iki farklı izâfet, yan yana — nahiv kitaplarının bu farkı öğrettiği kalıbın ta kendisi."),
  tok("الْحُكْمِ","hukm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ مَفْعُولُ «طَلَبِ» مَعْنًى، فَالْمَطْلُوبُ هُوَ الْحُكْمُ.",
      "The mudaf ilayh in jarr — and the object of «seeking» in meaning: what is sought is the ruling. The word that opened the book's first sentence and has stood in every chapter since is the object of the last effort described in it.",
      "Mecrûr muzâfun ileyh — ve mânen «طَلَب»in mef'ûlü: aranan, hükümdür. Kitabın ilk cümlesini açan ve o günden beri her bâbda duran kelime, kitapta anlatılan son gayretin mef'ûlüdür."),
  tok("الشَّرْعِيِّ","shari","noun",["naat-sifa"],
      "نَعْتٌ لِـ«الْحُكْمِ» مَجْرُورٌ — اسْمٌ مَنْسُوبٌ إِلَى «الشَّرْعِ»، وَقَدْ وُصِفَ بِهِ الْحُكْمُ فِي أَوَّلِ الْكِتَابِ أَيْضًا.",
      "A na't of «the ruling», in jarr — a nisba noun built on الشَّرْع, and the very adjective chapter 1 attached to the same head word in its opening line. The book's last definition wears the same two words as its first.",
      "«الْحُكْم»in na'tı, mecrûr — «الشَّرْع»e nisbet edilmiş isim; birinci bâbın açılış satırında da aynı kelimeyi niteleyen sıfatın kendisi. Kitabın son tarifi, ilk tarifiyle aynı iki kelimeyi taşır.",
      punct="."),
 ],
 "jumal": [J("الِاجْتِهَادُ بَذْلُ الْفَقِيهِ وُسْعَهُ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed nominal sentence, with no position in i'rab.",
   "İsti'nâfî isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "And his condition is knowledge of the Book, the Sunna, consensus and analogy.",
 "tr": "Şartı; Kitâb'ı, Sünnet'i, icmâ'ı ve kıyâsı bilmektir."},
 "tokens": [
  tok("وَشَرْطُهُ","shart","noun",["mubtada-khabar","idafa-definiteness","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«شَرْطُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ عَائِدٌ عَلَى الْمُجْتَهِدِ لَا عَلَى الِاجْتِهَادِ.",
      "A joining waw; «his condition» is the mubtada in raf' and a mudaf, the ha its mudaf ilayh — and the ha goes back to the MAN, not to the act. Chapter 14 used the same word for the ʿilla's condition and it referred to a thing; here it refers to a person, and the difference is the whole subject of this chapter.",
      "Atıf vâvı; «شَرْطُ» merfû mübtedâ ve muzâftır, hâ muzâfun ileyhtir — ve hâ, fiile değil ADAMA râcidir. On dördüncü bâb aynı kelimeyi illetin şartı için kullanmıştı ve bir şeye dönüyordu; burada bir kişiye dönüyor ve bu fark, bu bâbın bütün mevzuudur.",
      segments=[seg("وَ","wa","conj"), seg("شَرْطُ","shart","noun"), seg("هُ","pron-3ms","pron")]),
  tok("الْعِلْمُ","ilm","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرٌ، وَقَدْ عُدِّيَ بِالْبَاءِ لَا بِنَفْسِهِ، فَلَمْ يَنْصِبْ شَيْئًا.",
      "The khabar in raf' — a masdar again, but this one reaches its object through a BA rather than directly, so it puts nothing in nasb. Set it beside «بَذْلُ … وُسْعَهُ» one sentence back: a masdar governs exactly as its verb does, and عَلِمَ بِـ takes a jarr letter where بَذَلَ takes a bare object. The masdar inherits the verb's habits, not a general licence.",
      "Merfû haber — yine bir masdar; fakat bu, mef'ûlüne kendisiyle değil BÂ ile ulaşır, dolayısıyla hiçbir şeyi nasb etmez. Bir önceki cümledeki «بَذْلُ ... وُسْعَهُ» ile yan yana koyun: masdar, fiilinin amelini aynen yapar; «عَلِمَ بِـ» cer harfi ister, «بَذَلَ» ise mef'ûlü doğrudan alır. Masdar, fiilin âdetini miras alır; umumî bir ruhsat değil."),
  tok("بِالْكِتَابِ","kitab","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«الْعِلْمُ» — وَهُوَ أَوَّلُ الْأَدِلَّةِ الْأَرْبَعَةِ، وَقَدْ عُدَّتْ فِي الْبَابِ الثَّانِي مَرْفُوعَةً.",
      "A jarr-majrur attaching to «knowledge» — the first of the four sources, which chapter 2 listed in RAF' as the things the Law is known BY. Here the same four stand in JARR as the things the mujtahid must know. Same list, same order, opposite end of the book, and the case has turned over.",
      "«الْعِلْمُ»a taalluk eden câr-mecrûr — dört delîlin birincisi; ikinci bâb bunları, Şerîatin kendileriyle BİLİNDİĞİ şeyler olarak MERFÛ saymıştı. Burada aynı dördü, müctehidin bilmesi gereken şeyler olarak MECRÛR durur. Aynı liste, aynı sıra, kitabın öteki ucu — ve i'râb ters dönmüş.",
      segments=[seg("بِ","bi","prep"), seg("الْكِتَابِ","kitab","noun")]),
  tok("وَالسُّنَّةِ","sunna","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — وَقَدْ قُسِمَتْ بِاعْتِبَارِ النَّقْلِ فِي الْبَابِ الثَّالِثَ عَشَرَ.",
      "Joined, in jarr — divided by its transmission in chapter 13. The list is not a summary: every one of these four has had a chapter or more of its own, and naming them here is naming those chapters.",
      "Ma'tûf, mecrûr — on üçüncü bâbda nakil itibarıyla taksîm edilmişti. Liste bir özet değildir: bu dördün her biri kendi bâbına yahut bâblarına sahiptir ve burada onları anmak, o bâbları anmaktır.",
      segments=[seg("وَ","wa","conj"), seg("السُّنَّةِ","sunna","noun")]),
  tok("وَالْإِجْمَاعِ","ijma","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — وَقَدْ عُرِّفَ فِي الْبَابِ الثَّالِثِ.",
      "Joined, in jarr — defined in chapter 3.",
      "Ma'tûf, mecrûr — üçüncü bâbda tarif edilmişti.",
      segments=[seg("وَ","wa","conj"), seg("الْإِجْمَاعِ","ijma","noun")]),
  tok("وَالْقِيَاسِ","qiyas","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — وَقَدْ فُصِّلَ فِي الْبَابَيْنِ الرَّابِعَ عَشَرَ وَالْخَامِسَ عَشَرَ: أَرْكَانُهُ ثُمَّ حُدُودُهُ.",
      "Joined, in jarr — taken apart in chapters 14 and 15: its pillars, then its limits. The four sources are named twice in this book and nowhere else, once at the start and once at the end, and everything between them is the detail of one of the four.",
      "Ma'tûf, mecrûr — on dördüncü ve on beşinci bâblarda tafsîl edilmişti: önce rükünleri, sonra sınırları. Dört delil bu kitapta yalnız iki defa anılır — başta bir kez, sonda bir kez — ve aradaki her şey bu dördünden birinin tafsîlidir.",
      segments=[seg("وَ","wa","conj"), seg("الْقِيَاسِ","qiyas","noun")], punct="."),
 ],
 "jumal": [J("وَشَرْطُهُ الْعِلْمُ بِالْكِتَابِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "And it is not permitted for him to give a ruling on what he does not know.",
 "tr": "Bilmediği bir şey hakkında fetvâ vermesi ona câiz değildir."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "A joining waw and a bare negation — the same pairing that opened chapter 15, and again the verb after it keeps its raf'.",
      "Atıf vâvı ve amel etmeyen nefy «لَا»sı — on beşinci bâbı açan ikilinin aynısı; ardındaki fiil yine ref'ini korur.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَجُوزُ","jaaza","verb",["mudari-marfu","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ — أَجْوَفُ وَاوِيٌّ مِنْ «ج و ز»، وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ الْآتِي.",
      "A mudari in raf' with the damma written — a hollow verb of ج و ز, and its FA'IL is the masdar-clause that follows. The doer of «is permitted» has not appeared yet and is not a noun at all: it is «his giving a ruling».",
      "Zâhir damme ile merfû muzâri — «ج و ز»den ecvef-i vâvî; ve FÂİLİ, arkadan gelen masdar-ı müevveldir. «Câizdir»in fâili henüz gelmemiştir ve zaten bir isim de değildir: «fetvâ vermesi»dir."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَجُوزُ» — وَالْهَاءُ عَائِدَةٌ عَلَى الْمُجْتَهِدِ الْمَذْكُورِ ضِمْنًا فِي «شَرْطُهُ».",
      "A jarr-majrur attaching to «is permitted», the ha going back to the mujtahid — who has never been named in this chapter by a noun of his own. He is carried entirely by pronouns: «his condition», «for him», «he does not know». The book describes the man without ever naming him.",
      "«يَجُوزُ»a taalluk eden câr-mecrûr; hâ, müctehide râcidir — ki bu bâbda kendi ismiyle bir kere bile anılmamıştır. Tamamen zamirlerle taşınır: «şartı», «ona», «bilmediği». Kitap adamı, adını hiç anmadan tarif eder.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("أَنْ","an-nasiba","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِمَّا بَعْدَهُ فِي مَحَلِّ رَفْعٍ فَاعِلُ «يَجُوزُ».",
      "A masdar-making letter putting the mudari into nasb, and the masdar it forms with what follows stands in the position of RAF' as the fa'il of «is permitted». Chapter 14 used this particle to make a khabar and chapter 4 to make one too; this is the first time in the book it makes a FA'IL.",
      "Masdariyye ve nâsıbe harfi; kendisiyle sonrasından çıkan masdar-ı müevvel, «يَجُوزُ»un fâili olarak MAHALLEN MERFÛdur. On dördüncü bâb bu harfle haber yapmıştı, dördüncü bâb da öyle; kitapta ilk defa burada FÂİL yapıyor."),
  tok("يُفْتِيَ","afta","verb",["an-masdariyya","naqis-verbs","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ — نَاقِصٌ يَائِيٌّ مِنْ «ف ت و» عَلَى أَفْعَلَ.",
      "A mudari in nasb after «an», and its fatha is WRITTEN on the ya. Compare يَجْرِي in chapter 15, whose damma on the same letter had to be estimated: the damma is heavy and a ya will not carry it, the fatha is light and a ya carries it easily. One letter, two cases, and the difference between a written sign and an estimated one is nothing but the weight of the vowel.",
      "«أَنْ» ile mansub muzâri; nasb alâmeti, yâ üzerinde ZÂHİR fethadır — «ف ت و»den أَفْعَلَ vezninde nâkıs-ı yâî. On beşinci bâbdaki «يَجْرِي» ile karşılaştırın: aynı harfteki dammesi MUKADDERdi. Damme ağırdır, yâ onu taşımaz; fetha hafiftir, yâ onu kolayca taşır. Tek harf, iki hâl; zâhir alâmet ile mukadder alâmet arasındaki bütün fark, harekenin ağırlığıdır."),
  tok("بِمَا","ma-mawsula","pron",["ism-mawsul","huruf-jarr","anwa-ma"],
      "الْبَاءُ حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يُفْتِيَ»، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ «لَا يَعْلَمُهُ».",
      "The ba is a jarr letter hanging on «give a ruling», and «ma» is a relative noun in the position of jarr — and its ʿaid is DROPPED: the sense is «what he does not know IT». Chapter 15's ma had a concealed doer for its ʿaid; this one has a dropped OBJECT, which is the commoner case and the harder one to see, because a transitive verb standing with no object at all is the only sign that anything is missing.",
      "Bâ, «يُفْتِيَ»ye taalluk eden cer harfidir; «مَا» ise mahallen mecrûr ism-i mevsûldür — ve ÂİDİ HAZFEDİLMİŞTİR: takdîri «لَا يَعْلَمُهُ»dur. On beşinci bâbın mâsında âid gizli bir fâildi; bunda ise düşmüş bir MEF'ÛLdür — ki daha yaygın, fakat görülmesi daha zor olanıdır: müteaddî bir fiilin hiç mef'ûlsüz durması, bir şeyin eksik olduğuna dair tek işarettir.",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا، وَالْجُمْلَةُ بَعْدَهَا صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A bare negation, and the clause after it is the sila of the relative, with no position in i'rab.",
      "Amel etmeyen nefiy; sonrasındaki cümle ism-i mevsûlün sılasıdır ve mahalli yoktur."),
  tok("يَعْلَمُ","alima","verb",["mudari-marfu","fail"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَمَفْعُولُهُ مَحْذُوفٌ، وَهُوَ الْعَائِدُ.",
      "A mudari in raf' with a hidden «he» for its fa'il — and its OBJECT is dropped, and that dropped object is the ʿaid. عَلِمَ is transitive; a transitive verb that names nothing is a verb whose object is somewhere else, and here it is the ma at the head of the clause. The whole sentence turns on a word that is not written.",
      "Merfû muzâri; fâili müstetir «هُوَ»dur — ve MEF'ÛLÜ hazfedilmiştir; işte âid odur. «عَلِمَ» müteaddîdir; hiçbir şey anmayan müteaddî bir fiil, mef'ûlü başka yerde olan fiildir — ve burası, cümlenin başındaki «مَا»dır. Bütün cümle, yazılmamış bir kelimenin üzerinde döner.",
      punct="."),
 ],
 "jumal": [J("أَنْ يُفْتِيَ بِمَا لَا يَعْلَمُ",
   "الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ فَاعِلُ «يَجُوزُ».",
   "The masdar muawwal, in the position of raf' as the fa'il of «is permitted».",
   "Masdar-ı müevvel, «يَجُوزُ»un fâili olarak mahallen merfûdur."),
  J("لَا يَعْلَمُ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "And taqlid is acting on another's word with no proof.",
 "tr": "Taklîd, bir delîl olmaksızın başkasının sözüyle amel etmektir."},
 "tokens": [
  tok("وَالتَّقْلِيدُ","taqlid","noun",["mubtada-khabar","masdar","form-ii-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«التَّقْلِيدُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «قَلَّدَ» عَلَى تَفْعِيلٍ، وَأَصْلُهُ جَعْلُ الْقِلَادَةِ فِي الْعُنُقِ.",
      "A resuming waw, and «taqlid» is the mubtada in raf' — the Form II masdar of قَلَّدَ on تَفْعِيل. Its root sense is putting a NECKLACE on a neck: the follower hangs the responsibility for the ruling round the neck of the one he follows. The word is not a slur and not a compliment; it is a description of where the liability sits.",
      "İsti'nâf vâvı; «التَّقْلِيد» merfû mübtedâdır — «قَلَّدَ»nin TEF'ÎL vezninde masdarı. Kök mânâsı boyna GERDANLIK takmaktır: mukallid, hükmün mesuliyetini tâbi olduğu kişinin boynuna asar. Kelime ne bir zemdir ne bir medih; mesuliyetin nerede durduğunun tarifidir.",
      segments=[seg("وَ","wa","conj"), seg("التَّقْلِيدُ","taqlid","noun")]),
  tok("الْعَمَلُ","amal","noun",["mubtada-khabar","masdar"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرٌ ثَالِثٌ يَقَعُ خَبَرًا فِي هَذَا الْبَابِ، وَقَدْ عُدِّيَ بِالْبَاءِ.",
      "The khabar in raf' — the third masdar in this chapter to stand as a khabar, and like «knowledge» it reaches its object through a ba. Every definition in this chapter defines an ACT by naming the act: ijtihad is an expending, its condition is a knowing, taqlid is an acting. A discipline about texts ends by describing what people DO.",
      "Merfû haber — bu bâbda haber olan üçüncü masdar; ve «الْعِلْم» gibi mef'ûlüne bâ ile ulaşır. Bu bâbdaki her tarif, bir FİİLİ, fiilin kendisini anarak tarif eder: ictihâd bir sarf etmedir, şartı bir bilmedir, taklîd bir amel etmedir. Metinler üzerine bir ilim, insanların NE YAPTIĞINI tarif ederek biter."),
  tok("بِقَوْلِ","qawl","noun",["huruf-jarr","idafa-definiteness","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«الْعَمَلُ»، وَ«قَوْلِ» مُضَافٌ.",
      "A jarr-majrur attaching to «acting», and «the word of» is a mudaf. What is acted upon is not evidence but SPEECH — and that single choice of noun is the whole definition.",
      "«الْعَمَلُ»a taalluk eden câr-mecrûr; «قَوْلِ» muzâftır. Kendisiyle amel edilen şey delil değil SÖZdür — ve bu tek kelime seçimi, tarifin tamamıdır.",
      segments=[seg("بِ","bi","prep"), seg("قَوْلِ","qawl","noun")]),
  tok("الْغَيْرِ","ghayr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — «الْغَيْرُ» بِأَلْ، وَهُوَ قَلِيلٌ فِي كَلَامِ الْفُصَحَاءِ وَجَائِزٌ عِنْدَ أَهْلِ الِاصْطِلَاحِ.",
      "The mudaf ilayh in jarr — «al-ghayr» with the article, which the purest usage avoids and the technical writers permit. The matn is speaking as a jurist here, not as a poet, and the terminology wins.",
      "Mecrûr muzâfun ileyh — harf-i tarifli «الْغَيْر»; fasîhlerin kelâmında azdır, ıstılah ehlince câizdir. Metin burada şâir gibi değil fakîh gibi konuşur ve ıstılah galip gelir."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«الْعَمَلُ» — وَهِيَ هُنَا لِلْمُجَاوَزَةِ بِمَعْنَى الْخُلُوِّ.",
      "A jarr letter attaching to «acting» — and here it names being APART from a thing, which is how «min ghayri» comes to mean «without». The two words are read together and neither carries the sense alone.",
      "«الْعَمَلُ»a taalluk eden cer harfi — burada mücâveze, yani hulüv (bir şeyden hâlî olma) mânâsındadır. «مِنْ غَيْرِ» ikisi birlikte okunur; ikisinden hiçbiri mânâyı tek başına taşımaz."),
  tok("غَيْرِ","ghayr","noun",["idafa-definiteness"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ — وَ«غَيْرُ» فِي هَذِهِ الْجُمْلَةِ مَرَّتَانِ: مُضَافًا إِلَيْهِ ثُمَّ مُضَافًا، وَالثَّانِيَةُ لَا أَلَ فِيهَا.",
      "Majrur by «min» and itself a mudaf — and «ghayr» stands TWICE in this one sentence, first as a mudaf ilayh with the article and then as a mudaf without it. A word that is mudaf by its very nature cannot also wear ال when it is annexed, and the sentence shows both states four words apart.",
      "«مِنْ» ile mecrûr ve muzâf — ve «غَيْر» bu tek cümlede İKİ defa geçer: önce harf-i tarifli muzâfun ileyh, sonra tarifsiz muzâf. Mânâsı gereği muzâf olan bir kelime, izâfe edildiğinde ال taşıyamaz; cümle her iki hâli dört kelime arayla gösterir."),
  tok("حُجَّةٍ","hujja","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُنَوَّنٌ — وَتَنْكِيرُهُ فِي سِيَاقِ النَّفْيِ يُفِيدُ الْعُمُومَ: مِنْ غَيْرِ حُجَّةٍ مَا.",
      "The mudaf ilayh in jarr with its tanwin — and an indefinite inside a negative frame is GENERAL: without any proof whatsoever. Had it been definite the definition would have excluded one proof and admitted the rest. This is the same reason chapter 15 left «an excuse» indefinite, and it is worth learning as a habit: in a definition, the tanwin is doing work.",
      "Tenvînli mecrûr muzâfun ileyh — ve nefiy siyâkında nekre UMÛM ifade eder: hiçbir delil olmaksızın. Marife olsaydı tarif, bir delîli dışarıda bırakıp ötekileri kabul etmiş olurdu. On beşinci bâbın «عُذْرٍ»i nekre bırakmasının sebebi de aynıdır; bunu bir alışkanlık olarak öğrenmeye değer: tarifte tenvîn iş görür.",
      punct="."),
 ],
 "jumal": [J("وَالتَّقْلِيدُ الْعَمَلُ بِقَوْلِ الْغَيْرِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed nominal sentence, with no position in i'rab.",
   "İsti'nâfî isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "So whoever has not reached the rank of ijtihad — upon him is taqlid.",
 "tr": "Kim ictihâd derecesine ulaşmamışsa, ona düşen taklîddir."},
 "tokens": [
  tok("فَمَنْ","man-shartiyya","pron",["in-shartiyya","mubtada-khabar"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَ«مَنْ» اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "The fa draws a consequence from everything before it, and «man» is a CONDITIONAL NOUN that puts two verbs into jazm — mabni on sukun, in the position of raf' as the mubtada. It is one of the fifteen jawazim and it is an ISM, not a harf: the book's last sentence is governed by a noun.",
      "Fâ tefrî' içindir; «مَنْ» ise iki fiili cezmeden ŞART İSMİdir — sükûn üzere mebnî, mübtedâ olarak mahallen merfû. On beş câzimden biridir ve HARF değil İSİMdir: kitabın son cümlesini bir isim idare eder.",
      segments=[seg("فَ","fa","conj"), seg("مَنْ","man-shartiyya","pron")]),
  tok("لَمْ","lam-jazim","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَالْجَزْمُ هُنَا مِنْ «لَمْ» لَا مِنْ «مَنْ»، وَ«مَنْ» عَمَلُهَا فِي مَحَلِّ الْجُمْلَةِ.",
      "A letter of negation, jazm and TIME-REVERSAL — it turns a present form into a past sense. And note whose jazm the verb actually wears: «lam» is standing right there, so the sign belongs to it, while «man» governs the CLAUSE's position. Two governors, one verb, and no contradiction — this is the distinction Qawa'id al-I'rab makes between a word's i'rab and a clause's mahall.",
      "Nefiy, cezm ve KALB harfi — muzâri sîgayı mâzî mânâsına çevirir. Ve fiilin cezmi kimden: «لَمْ» hemen orada durduğu için alâmet onundur; «مَنْ» ise CÜMLENİN mahalline amel eder. İki âmil, tek fiil ve hiçbir tezat yok — Kavâidü'l-İ'râbın, kelimenin i'râbı ile cümlenin mahalli arasında yaptığı ayrım budur."),
  tok("يَبْلُغْ","balagha","verb",["lam-jazim"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَهُوَ فِعْلُ الشَّرْطِ.",
      "A mudari in jazm by «lam», its sign the sukun, with a hidden «he» for its fa'il — and it is the CONDITION's verb. A sound root, so the jazm shows as a plain sukun and nothing is lost. Set it against chapter 14's لَمْ يَرِدْ, where the same jazm fell on a mithal and the waw stayed gone: the sign is the same, the damage differs entirely with the root.",
      "«لَمْ» ile meczûm muzâri; cezm alâmeti sükûndur, fâili müstetir «هُوَ»dur — ve ŞARTIN fiilidir. Kök sahîhtir, bu yüzden cezm sade bir sükûn olarak görünür ve hiçbir şey kaybolmaz. On dördüncü bâbdaki «لَمْ يَرِدْ» ile karşılaştırın: orada aynı cezm bir misâle düşmüş ve vâv düşük kalmıştı. Alâmet aynıdır; zarar, köke göre tamamen değişir."),
  tok("رُتْبَةَ","rutba","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ وَهُوَ مُضَافٌ.",
      "The maf'ul bihi in nasb by the fatha, and a mudaf — «the RANK of ijtihad», not ijtihad itself. A man may perform an act of ijtihad and not hold the rank; the noun the matn chose is the one that makes the distinction.",
      "Fetha ile mansub mef'ûlün bih ve muzâf — «ictihâdın DERECESİ», ictihâdın kendisi değil. Bir kimse bir ictihâd fiilini işleyip derecesine sahip olmayabilir; metnin seçtiği isim, bu ayrımı yapan isimdir."),
  tok("الِاجْتِهَادِ","ijtihad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الِاسْمُ الَّذِي فُتِحَ بِهِ الْبَابُ، وَبِهِ يُخْتَمُ الشَّرْطُ.",
      "The mudaf ilayh in jarr — the word this chapter opened with, standing here inside its own condition. The chapter is a ring, as the book is.",
      "Mecrûr muzâfun ileyh — bâbın kendisiyle açıldığı isim; burada kendi şartının içinde durur. Bâb bir halkadır; kitap gibi."),
  tok("فَعَلَيْهِ","ala","prep",["fa-khabar-mubtada","huruf-jarr","mubtada-khabar"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ وَجَبَ اقْتِرَانُهَا لِأَنَّ الْجَوَابَ جُمْلَةٌ اسْمِيَّةٌ، وَ«عَلَيْهِ» جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.",
      "The FA links the answer to its condition, and here it is OBLIGATORY, because the answer is a nominal sentence — a nominal jawab can never stand bare. Set this against chapter 15's فَغَيْرُهُ: there a relative merely BORROWED the sense of a condition and the fa was permitted; here the condition is real and the fa is required. Same letter, one licensed and one compulsory, and the difference is what «man» is. «Alayhi» is a jarr-majrur standing as a FRONTED khabar.",
      "FÂ, cevâbı şarta bağlar ve burada VÂCİBdir; zira cevap bir isim cümlesidir — isim cümlesinden cevap asla fâsız duramaz. On beşinci bâbdaki «فَغَيْرُهُ» ile karşılaştırın: orada bir ism-i mevsûl şart mânâsını ÖDÜNÇ almıştı ve fâ câizdi; burada şart hakikidir ve fâ vâcibtir. Aynı harf; biri ruhsat, öteki mecburiyet — ve farkı yapan «مَنْ»dir. «عَلَيْهِ» ise MUKADDEM haber olan câr-mecrûrdur.",
      segments=[seg("فَ","fa","conj"), seg("عَلَيْ","ala","prep"), seg("هِ","pron-3ms","pron")]),
  tok("التَّقْلِيدُ","taqlid","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ. وَبِهَذِهِ الْكَلِمَةِ يُخْتَمُ الْكِتَابُ: بَدَأَ بِتَعْرِيفِ الْعِلْمِ وَانْتَهَى بِمَا يَلْزَمُ مَنْ لَمْ يَبْلُغْهُ.",
      "The DELAYED mubtada, in raf' — and the nominal sentence as a whole stands in the POSITION OF JAZM as the answer to the condition. A nominal clause cannot show jazm on any letter, so it is jazm in place only, which is precisely why the fa had to be there: without it nothing would mark the clause as an answer at all. And with this word the book closes. It opened by defining a science and it ends by naming what is owed by everyone who has not reached it — which is nearly everyone, and the matn says so without a word of apology.",
      "MUAHHAR mübtedâ, merfû — ve isim cümlesinin tamamı, şartın cevâbı olarak MAHALLEN MECZÛMdur. İsim cümlesi hiçbir harfinde cezm gösteremez; bu yüzden cezmi yalnız mahallendir — ve fânın orada bulunmasının zarûreti tam da budur: onsuz cümleyi cevap diye işaretleyecek hiçbir şey kalmazdı. Ve kitap bu kelimeyle kapanır. Bir ilmin tarifiyle açılmış, o ilme ulaşamayanın üzerine düşenle bitmiştir — ki bu, neredeyse herkestir; metin bunu bir kelime özür dilemeden söyler.",
      punct="."),
 ],
 "jumal": [J("لَمْ يَبْلُغْ رُتْبَةَ الِاجْتِهَادِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.",
   "A verbal clause in the position of jazm, the verb of the condition.",
   "Şartın fiili olarak mahallen meczûm fiil cümlesi."),
  J("فَعَلَيْهِ التَّقْلِيدُ",
   "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَاقْتِرَانُهَا بِالْفَاءِ وَاجِبٌ لِأَنَّهَا اسْمِيَّةٌ.",
   "A nominal sentence in the position of jazm as the answer to the condition — and the fa is OBLIGATORY on it, because it is nominal.",
   "Şartın cevâbı olarak mahallen meczûm isim cümlesi; isim cümlesi olduğu için fâ ile bağlanması VÂCİBdir.")]})

GLOSS_ADD = {
 "badhl":   g("بَذْل", "ب ذ ل", "noun", "expending, spending freely (masdar)", "bezl; sarf etme (masdar)", 4),
 "faqih":   g("فَقِيه", "ف ق ه", "noun", "jurist", "fakih", 3, plural="فُقَهَاء"),
 "wus":     g("وُسْع", "و س ع", "noun", "capacity, what one can bear", "vüs'; güç yetirilen", 4),
 "taqlid":  g("تَقْلِيد", "ق ل د", "noun", "taqlid — acting on another's word without proof (masdar, Form II)", "taklîd — delilsiz olarak başkasının sözüyle amel (masdar, tef'îl)", 4),
 "hujja":   g("حُجَّة", "ح ج ج", "noun", "proof, argument", "hüccet, delil", 3, plural="حُجَج"),
 "rutba":   g("رُتْبَة", "ر ت ب", "noun", "rank, degree", "rütbe, derece", 3, plural="رُتَب"),
 "afta":    g("أَفْتَى", "ف ت و", "verb", "to give the fatwa", "fetva vermek", 4, form="IV"),
 "alima":   g("عَلِمَ", "ع ل م", "verb", "to know", "bilmek", 1, form="I"),
 "balagha": g("بَلَغَ", "ب ل غ", "verb", "to reach", "ulaşmak, varmak", 2, form="I"),
 "man-shartiyya": g("مَنْ (الشَّرْطِيَّة)", None, "pron", "whoever (conditional)", "her kim (şart)", 3),
}

def build_morph():
    """Three paradigms, all COPIED after a lemma-identity assert. Nothing here
    is generated: every one of these verbs is already carried, hand-checked, by
    another package, and a lex key is global — two spellings of one verb in two
    packages is the collision this project has been bitten by before."""
    out = {}
    for pkg, lex in [("kitab-al-waqf", "afta"),
                     ("aqaid-ahl-al-sunna", "alima"),
                     ("wasiyyat-abi-hanifa-samti", "balagha")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))
        assert g_["entries"][lex]["lemma"] == GLOSS_ADD[lex]["lemma"], lex
        out[lex] = m["verbs"][lex]
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/16.json").write_text(
    json.dumps({"chapter": 16, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 16 for c in man["chapters"]):
    man["chapters"].append({"n": 16, "title": TITLE16})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.16.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch16:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
