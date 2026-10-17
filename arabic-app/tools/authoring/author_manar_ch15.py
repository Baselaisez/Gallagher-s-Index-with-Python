# -*- coding: utf-8 -*-
"""Author chapter 15 of mukhtasar-al-manar — WHERE ANALOGY DOES NOT RUN,
and the pair it produces: ʿAZIMA and RUKHSA.

Chapter 14 built qiyas up — four pillars and a condition on the last of them.
This chapter does the opposite and is the more useful half: it says where the
instrument may NOT be used at all. A method that is never fenced is not a
method, and the matn fences this one in a single line before it goes on to
name the two faces every ruling wears.

ATTRIBUTION: like chapters 2–14, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn:
s1 is the standard four-item bar, s3 is al-Nasafi's own definition of the
ʿazima, s4 the received definition of the rukhsa, and s5 the qaʿida in the
wording the commentaries carry.

Grammar this chapter is chosen to teach:
  • الْمُقَدَّرَاتِ as the ism of أَنَّ — a sound feminine plural in NASB, and its
    sign is a KASRA. The one place where the case and the mark disagree by
    rule and not by accident.
  • تُدْرَكُ — the majhul of Form IV in the FEMININE, which the package stores
    only in the masculine. The engine has to BUILD it, and can.
  • لَا يُقَاسُ — the majhul of a HOLLOW verb, where the letter changes as well
    as the vowels (يَقِيسُ → يُقَاسُ). The rule that built تُدْرَكُ refuses this
    one on purpose, and the paradigm stores it. The boundary is the lesson.
  • فَغَيْرُهُ — الْفَاءُ الدَّاخِلَةُ عَلَى خَبَرِ الْمُبْتَدَإِ, admitted because the
    mubtada is a mawsul carrying the sense of a condition. A new note.
  • لِمَا لَزِمَ — the ʿaid of a sila that is a MUSTATIR pronoun: nothing on the
    page points back at the ma, and the relative is still sound.
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
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
S = []

TITLE15 = {"ar": "الْعَزِيمَةُ وَالرُّخْصَةُ وَمَا لَا قِيَاسَ فِيهِ",
           "en": "Strict Rule, Dispensation, and Where Analogy Does Not Run",
           "tr": "Azîmet, Ruhsat ve Kıyâsın Girmediği Yerler"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "And analogy does not run in the fixed punishments, the expiations, the divinely fixed amounts, or the dispensations.",
 "tr": "Kıyâs; hadlerde, keffâretlerde, mukadderâtta ve ruhsatlarda cârî olmaz."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["mudari-marfu"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا — فَالْفِعْلُ بَعْدَهَا مَرْفُوعٌ، بِخِلَافِ «لَمْ» فِي الْبَابِ الرَّابِعَ عَشَرَ فَإِنَّهَا تَجْزِمُ.",
      "A resuming waw, and «la» simply denying — it governs nothing, so the verb after it stays in RAF'. Set this beside لَمْ يَرِدْ one chapter back: both are negations, one leaves the verb alone and the other cuts its ending off. The particle, not the negation, is what governs.",
      "İsti'nâf vâvı ve amel etmeyen nefy «لَا»sı — ardındaki fiil MERFÛ kalır. Bir önceki bâbdaki «لَمْ يَرِدْ» ile yan yana koyun: ikisi de nefiydir; biri fiile dokunmaz, öteki sonunu keser. Âmil olan nefiy değil, harfin kendisidir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَجْرِي","jara","verb",["mudari-marfu","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ ضَمَّةٌ مُقَدَّرَةٌ عَلَى الْيَاءِ مَنَعَ مِنْ ظُهُورِهَا الثِّقَلُ — نَاقِصٌ يَائِيٌّ مِنْ «ج ر ي».",
      "A mudari in raf', and its damma is ESTIMATED on the ya because the ya is too heavy to carry it. The very verb chapter 12 used to show this rule appearing on a verb rather than a noun — and there it was the abrogation that «runs», here the analogy that does not.",
      "Merfû muzâri fiil; ref' alâmeti, sıklet sebebiyle yâ üzerinde MUKADDER dammedir — «ج ر ي»den nâkıs yâî. On ikinci bâbın bu kâideyi isimde değil FİİLde gösterdiği fiilin aynısı: orada cârî olan nesihti, burada cârî OLMAYAN kıyastır."),
  tok("الْقِيَاسُ","qiyas","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ — وَظُهُورُهَا هُنَا بَعْدَ تَقْدِيرِهَا فِي الْفِعْلِ يُرِي الْفَرْقَ فِي سَطْرٍ وَاحِدٍ.",
      "The fa'il in raf' with the damma WRITTEN — and having just seen the same damma estimated on the verb before it, the reader gets both states of one vowel inside a single line.",
      "Zâhir damme ile merfû fâil — ve hemen önceki fiilde aynı dammenin mukadder olduğunu gördükten sonra okuyucu tek satırda o harekenin her iki hâlini de görmüş olur."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يَجْرِي» — وَالظَّرْفِيَّةُ هُنَا مَعْنَوِيَّةٌ لَا مَكَانِيَّةٌ.",
      "A jarr letter attaching to «runs» — and the containment it names is a conceptual one, not a place. Four abstract categories are being spoken of as though they were rooms analogy may not enter.",
      "«يَجْرِي»ye taalluk eden cer harfi — buradaki zarfiyyet mekânî değil ma'nevîdir. Dört soyut kategori, kıyâsın giremeyeceği odalar gibi anlatılıyor."),
  tok("الْحُدُودِ","hadd","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تَكْسِيرٍ لِـ«حَدٍّ»، وَهُوَ الْعُقُوبَةُ الْمُقَدَّرَةُ شَرْعًا.",
      "Majrur by the kasra — a broken plural of حَدّ, the punishment whose measure the Law itself fixed. A doubled root: the two dals of ح د د meet in the singular and are separated by the plural's own vowel.",
      "Kesra ile mecrûr — «حَدّ»in cem'-i teksîri; şer'an mikdârı belirlenmiş cezâ. Muzaaf bir kök: ح د د'nin iki dâlı müfredde birleşir, cemide cem'in kendi harekesiyle ayrılır."),
  tok("وَالْكَفَّارَاتِ","kaffara","noun",["atf-nasaq","jam-muannath-salim"],
      "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، وَجَرُّهُ بِالْكَسْرَةِ كَجَرِّ الْمُفْرَدِ، فَلَا يُشْكِلُ.",
      "Joined and majrur by the kasra — a sound feminine plural, whose jarr looks exactly like a singular's and so raises no question. Remember the shape: in the very next sentence the same plural will be MANSUB and will still wear a kasra, and that is the one that surprises people.",
      "Ma'tûf, kesra ile mecrûr — cem'-i müennes sâlim; cerri müfredin cerri gibidir, bu yüzden bir müşkil doğurmaz. Şekli aklınızda tutun: bir sonraki cümlede aynı cemi MANSUB olacak ve yine kesra taşıyacak; şaşırtan odur.",
      segments=[seg("وَ","wa","conj"), seg("الْكَفَّارَاتِ","kaffara","noun")]),
  tok("وَالْمُقَدَّرَاتِ","muqaddarat","noun",["atf-nasaq","jam-muannath-salim","ism-maful"],
      "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ «مُقَدَّرَةٍ»، وَهِيَ اسْمُ مَفْعُولٍ مِنْ «قَدَّرَ» عَلَى مُفَعَّلٍ: مَا قَدَّرَهُ الشَّارِعُ بِعَدَدٍ أَوْ كَيْلٍ.",
      "Joined and majrur — the plural of مُقَدَّرَة, the ism maf'ul of Form II on مُفَعَّل: what the Lawgiver has himself fixed by number or measure — the eighty lashes, the forty days, the nisab. A quantity is not reasoned to; it is received.",
      "Ma'tûf, mecrûr — «مُقَدَّرَة»in cemi; «قَدَّرَ»den MÜFEA'AL vezninde ism-i mef'ûl: Şâri'in sayı yahut ölçüyle bizzat takdîr ettiği şey — seksen değnek, kırk gün, nisab. Mikdar akılla bulunmaz, nakille alınır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُقَدَّرَاتِ","muqaddarat","noun")]),
  tok("وَالرُّخَصِ","rukhsa","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — جَمْعُ «رُخْصَةٍ»، وَسَتُعَرَّفُ فِي هَذَا الْبَابِ نَفْسِهِ: يُذْكَرُ الِاسْمُ فِي الْقَائِمَةِ ثُمَّ يُحَدُّ بَعْدَ سَطْرَيْنِ.",
      "Joined and majrur — the plural of رُخْصَة, and the matn will define the word inside this same chapter. Naming a term in a list and defining it two lines later is the book's habit: it was done to قِيَاس in chapter 3 and to مُتَوَاتِر in chapter 2.",
      "Ma'tûf, mecrûr — «رُخْصَة»in cemi; ve metin bu kelimeyi aynı bâbın içinde tarif edecek. Bir terimi listede anıp iki satır sonra tarif etmek kitabın âdetidir: üçüncü bâbda «kıyâs»a, ikinci bâbda «mütevâtir»e aynısı yapılmıştı.",
      segments=[seg("وَ","wa","conj"), seg("الرُّخَصِ","rukhsa","noun")], punct="."),
 ],
 "jumal": [J("وَلَا يَجْرِي الْقِيَاسُ فِي الْحُدُودِ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed verbal sentence, with no position in i'rab.",
   "İsti'nâfî fiil cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "…because the fixed amounts are not grasped by opinion.",
 "tr": "…zira mukadderât re'y ile idrâk edilmez."},
 "tokens": [
  tok("لِأَنَّ","anna","part",["inna-wa-akhawatuha","lam-taleel"],
      "اللَّامُ لِلتَّعْلِيلِ وَ«أَنَّ» مِنْ أَخَوَاتِ «إِنَّ» تَنْصِبُ الِاسْمَ وَتَرْفَعُ الْخَبَرَ — وَفُتِحَتِ الْهَمْزَةُ لِأَنَّهَا مَعَ مَعْمُولَيْهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِاللَّامِ.",
      "The lam of causation with «anna» of inna's family, which puts its noun in nasb and its khabar in raf'. The hamza takes a FATHA precisely because the whole clause construes as a masdar governed by the lam — «because of the not-being-grasped of…». The kasra/fatha rule chapter 12 stated is applied here rather than restated.",
      "Ta'lîl lâmı ile inne'nin kardeşlerinden «أَنَّ»: ismini nasb, haberini raf eder. Hemze FETHALIdır; çünkü ma'mûlleriyle birlikte lâmın cerrettiği bir masdar te'vîlindedir. On ikinci bâbın kesra/fetha kâidesi burada tekrar edilmez, uygulanır.",
      segments=[seg("لِ","li","prep"), seg("أَنَّ","anna","part")]),
  tok("الْمُقَدَّرَاتِ","muqaddarat","noun",["inna-wa-akhawatuha","jam-muannath-salim"],
      "اسْمُ «أَنَّ» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْكَسْرَةُ نِيَابَةً عَنِ الْفَتْحَةِ — لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ، وَهَذَا الْجَمْعُ يُنْصَبُ بِالْكَسْرَةِ.",
      "The ism of «anna», in NASB — and its mark is a KASRA standing in for the fatha, because the sound feminine plural takes its nasb by a kasra. This is the one place in nahw where the case and the mark disagree by RULE: the word is mansub and looks majrur, and the identical word looked exactly the same one sentence ago while genuinely being majrur. Nothing on the surface separates them; only the governor does.",
      "«أَنَّ»nin ismi, MANSUB — alâmeti, fetha yerine geçen KESRAdır; zira cem'-i müennes sâlimdir ve bu cemi kesra ile nasbolunur. Nahivde hâl ile alâmetin KÂİDE gereği ayrıştığı yer burasıdır: kelime mansubdur, mecrûr görünür; bir cümle önce aynı kelime tıpatıp böyle görünüyordu ve gerçekten mecrûrdu. Yüzeyde ikisini ayıran hiçbir şey yok, yalnız âmil ayırır."),
  tok("لَا","la-nafiya","part",["mudari-marfu","anwa-al-khabar"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا، وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».",
      "A bare negation, and the clause after it stands in the POSITION OF RAF' as the khabar of «anna» — a clause serving as a khabar, which the package has now shown for inna's family as well as for a plain mubtada.",
      "Amel etmeyen nefiy; sonrasındaki cümle «أَنَّ»nin haberi olarak MAHALLEN MERFÛdur — haber olan bir cümle; paket bunu artık sade mübtedâda olduğu gibi inne ailesinde de göstermiştir."),
  tok("تُدْرَكُ","adraka","verb",["naib-al-fail","form-iv-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هِيَ» يَعُودُ عَلَى الْمُقَدَّرَاتِ — وَقَاعِدَتُهُ: ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ.",
      "A mudari built for the UNNAMED DOER, in raf', its naib al-fa'il a hidden «she» going back to the fixed amounts. The rule that made it is two words long: raise the first letter to a damma and open the one before the last to a fatha — يُدْرِكُ becomes يُدْرَكُ, and with the feminine prefix تُدْرَكُ. The doer is dropped not because it is unknown but because naming it would add nothing: it is anyone who reasons.",
      "MEÇHÛL sîgasında merfû muzâri; nâib-i fâili, mukadderâta râci' müstetir «هِيَ»dir. Kâidesi iki kelimedir: evvelini zammeli, âhirinden öncekini fethalı yap — «يُدْرِكُ» «يُدْرَكُ» olur, müennes önekiyle «تُدْرَكُ». Fâil meçhûl olduğu için değil, söylenmesi bir şey katmadığı için düşürülmüştür: o, akıl yürüten herkestir."),
  tok("بِالرَّأْيِ","ray","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«تُدْرَكُ» — وَالْبَاءُ لِلِاسْتِعَانَةِ، وَ«الرَّأْيُ» هُنَا هُوَ الْقِيَاسُ نَفْسُهُ بِاسْمِهِ الْآخَرِ.",
      "A jarr-majrur attaching to «grasped», the ba naming the INSTRUMENT — and «opinion» here is analogy itself under its other name. The sentence therefore reads: analogy is barred from measures because measures are not reached by analogy. It is not circular; it is a statement about what kind of thing a quantity is.",
      "«تُدْرَكُ»a taalluk eden câr-mecrûr; bâ istiâne içindir ve buradaki «re'y», kıyâsın öteki adıdır. O hâlde cümle şunu söyler: mikdarlarda kıyâs yürümez, çünkü mikdarlar kıyâsla elde edilmez. Bu bir devir değil, mikdârın ne tür bir şey olduğuna dair bir hükümdür.",
      segments=[seg("بِ","bi","prep"), seg("الرَّأْيِ","ray","noun")], punct="."),
 ],
 "jumal": [J("لَا تُدْرَكُ بِالرَّأْيِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».",
   "A verbal clause in the position of raf', the khabar of «anna».",
   "«أَنَّ»nin haberi olarak mahallen merfû fiil cümlesi.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "And the ʿazima is a name for what binds the servants by God — exalted is He — making it obligatory.",
 "tr": "Azîmet, Allah Teâlâ'nın îcâbıyla kullara lâzım olan şeyin adıdır."},
 "tokens": [
  tok("وَالْعَزِيمَةُ","azima","noun",["mubtada-khabar","atf-nasaq"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْعَزِيمَةُ» مُبْتَدَأٌ مَرْفُوعٌ — عَلَى وَزْنِ فَعِيلَةٍ، وَأَصْلُهَا الْقَصْدُ الْمُؤَكَّدُ.",
      "A resuming waw, and «the ʿazima» is the mubtada in raf' — on فَعِيلَة, from a root meaning a resolve that has been made firm. The word is the ordinary rule: what was laid down without an excuse in view.",
      "İsti'nâf vâvı; «الْعَزِيمَة» merfû mübtedâdır — فَعِيلَة vezninde; aslı, pekiştirilmiş kasıddır. Kelime, asıl hükmü ifade eder: bir özür göz önünde tutulmaksızın konulan.",
      segments=[seg("وَ","wa","conj"), seg("الْعَزِيمَةُ","azima","noun")]),
  tok("اسْمٌ","ism","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَقَوْلُهُ «اسْمٌ لِـ» أَدَقُّ مِنْ «هِيَ»: الْمُعَرَّفُ لَفْظٌ، وَالْمُعَرَّفُ بِهِ مَعْنًى، وَالْحَدُّ يَصِلُ بَيْنَهُمَا.",
      "The khabar in raf' with its tanwin — and «a NAME for…» is more exact than «is»: what is being defined is a WORD, what defines it is a meaning, and the definition joins the two. The matn could have written «the ʿazima is what binds» and chose not to. Compare chapter 1, where الْفِقْهُ مَعْرِفَةُ… defines the discipline directly and needs no such bridge.",
      "Tenvînli merfû haber — ve «...nin ADIdır» demek, «...dir» demekten daha dakîktir: tarif edilen bir LAFIZ, tarif eden bir MÂNÂdır ve had ikisini birleştirir. Metin «azîmet, lâzım olandır» diyebilirdi, demedi. Birinci bâbdaki «الْفِقْهُ مَعْرِفَةُ...» ile karşılaştırın: orada ilmin kendisi tarif edilir ve böyle bir köprüye ihtiyaç duyulmaz."),
  tok("لِمَا","ma-mawsula","pron",["ism-mawsul","huruf-jarr","anwa-ma"],
      "اللَّامُ حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«اسْمٌ»، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — كَلِمَةٌ وَاحِدَةٌ فِي الْخَطِّ وَكَلِمَتَانِ فِي الْإِعْرَابِ.",
      "The lam is a jarr letter hanging on «a name», and «ma» is a relative noun, fixed in form, in the position of JARR after it — one word in writing and two in i'rab. The jarr letter also settles the class outright: a harf is never majrur, so whatever else this ma might have been, here it is an ism.",
      "Lâm, «اسْمٌ»a taalluk eden cer harfidir; «مَا» ise mebnî ism-i mevsûl olarak mahallen MECRÛRdur — yazıda tek kelime, i'râbda iki. Cer harfi sınıfı da kesin olarak tayin eder: harf mecrûr olmaz; öyleyse bu mâ, başka ne olabilirse olsun, burada isimdir.",
      segments=[seg("لِ","li","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("لَزِمَ","lazima","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ مِنْ بَابِ سَمِعَ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» يَعُودُ عَلَى «مَا» — وَهُوَ الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ لَا مَحَلَّ لَهَا.",
      "A mazi built on the fatha, from the bab of سَمِعَ, its fa'il a hidden «he» going back to the «ma» — and THAT hidden pronoun is the ʿaid. A relative must have a pronoun returning to it, and here nothing on the page returns: the returning pronoun is concealed inside the verb. A sila is sound with an unwritten ʿaid and unsound with none at all.",
      "Sem'ia bâbından, fetha üzere mebnî mâzî; fâili, «مَا»ya râci' müstetir «هُوَ»dur — ÂİD odur ve cümle sıladır, mahalli yoktur. Mevsûlün kendisine dönen bir zamiri bulunmalıdır; burada sayfada dönen hiçbir şey yoktur: dönen zamir fiilin içinde gizlidir. Sıla, yazılmamış bir âidle sahîh, hiç âidsiz ise fâsiddir."),
  tok("الْعِبَادَ","ibad","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ «عَبْدٍ»، وَاللَّازِمُ يَلْزَمُ الْمُكَلَّفَ فَيَتَعَدَّى إِلَيْهِ.",
      "The maf'ul bihi in nasb by the fatha — the plural of عَبْد. What binds, binds SOMEONE, and the verb reaches its object directly. Note who is named: not the believers and not the jurists, but the servants, which is every responsible person without exception.",
      "Fetha ile mansub mef'ûlün bih — «عَبْد»in cemi. Lâzım olan şey BİRİNE lâzım olur ve fiil mef'ûlüne doğrudan geçer. Kimin anıldığına dikkat edin: mü'minler yahut fakîhler değil, KULLAR — yani istisnâsız her mükellef."),
  tok("بِإِيجَابِ","ijab","noun",["huruf-jarr","masdar","form-iv-verbs","mithal-verbs","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«لَزِمَ»، وَ«إِيجَابِ» مُضَافٌ — مَصْدَرُ «أَوْجَبَ» عَلَى إِفْعَالٍ مِنْ مِثَالٍ وَاوِيٍّ: أَصْلُهُ «إِوْجَاب»، فَسَكَنَتِ الْوَاوُ بَعْدَ كَسْرَةٍ فَقُلِبَتْ يَاءً.",
      "A jarr-majrur attaching to «binds», and «the making obligatory of» is a mudaf — the Form IV masdar of أَوْجَبَ from a waw-initial root. Its origin is إِوْجَاب: a silent waw after a kasra cannot stand, so it turns into a ya. Chapter 4 used the verb أَنْ يُوجِبَ where the same waw became a MADD after a damma; here it becomes a YA after a kasra. One weak letter, two fates, decided entirely by the vowel in front of it.",
      "«لَزِمَ»ye taalluk eden câr-mecrûr; «إِيجَابِ» muzâftır — misâl-i vâvîden if'âl vezninde «أَوْجَبَ»nin masdarı. Aslı «إِوْجَاب»dır; kesradan sonra sâkin vâv duramaz, yâya kalbolur. Dördüncü bâbdaki «أَنْ يُوجِبَ»de aynı vâv, dammeden sonra MED harfi olmuştu; burada kesradan sonra YÂ oluyor. Tek illetli harf, iki âkıbet; belirleyen, yalnız önündeki harekedir.",
      segments=[seg("بِ","bi","prep"), seg("إِيجَابِ","ijab","noun")]),
  tok("اللَّهِ","allah","propn",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْإِضَافَةُ هُنَا إِلَى الْفَاعِلِ: الْمُوجِبُ هُوَ اللهُ.",
      "The mudaf ilayh in jarr — and the idafa is to the DOER: the one who makes it obligatory is God. A masdar may be annexed to whoever does it or to whatever it is done to, and here only the first reading stands, because an obligation has no other author.",
      "Mecrûr muzâfun ileyh — ve izâfet burada FÂİLEdir: îcâb eden Allah'tır. Masdar, yapana da yapılana da izâfe edilebilir; burada yalnız birincisi durur, çünkü îcâbın başka bir sahibi yoktur."),
  tok("تَعَالَى","taala","verb",["form-vi-verbs","naqis-verbs","jumla-mutarida"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَفَاعِلُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
      "A mazi built on a fatha ESTIMATED on the alif, which cannot bear one, with a hidden «He» for its fa'il — and the whole clause is an interjected invocation with no position in i'rab at all. It sits between the mudaf ilayh and what follows without disturbing either: an i'rab-less clause is exactly what may be dropped in anywhere.",
      "Elif üzerinde taazzür sebebiyle MUKADDER fetha ile mebnî mâzî; fâili müstetirdir — ve cümle, i'râbdan mahalli olmayan mu'terize duâ cümlesidir. Muzâfun ileyh ile sonrası arasına, ikisini de bozmadan girer: mahalsiz cümle, tam da her yere sokulabilen cümledir.", punct="."),
 ],
 "jumal": [J("لَزِمَ الْعِبَادَ بِإِيجَابِ اللَّهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("تَعَالَى",
   "جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "An interjected invocation, with no position in i'rab.",
   "Mu'terize duâ cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "And the rukhsa is what was legislated for an excuse, while the evidence that forbids it still stands.",
 "tr": "Ruhsat ise, haram kılan delil bâkî iken bir özür sebebiyle meşrû kılınan şeydir."},
 "tokens": [
  tok("وَالرُّخْصَةُ","rukhsa","noun",["mubtada-khabar","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الرُّخْصَةُ» مُبْتَدَأٌ مَرْفُوعٌ — وَهِيَ فِي اللُّغَةِ التَّيْسِيرُ، وَقَدْ ذُكِرَتْ فِي الْقَائِمَةِ فِي أَوَّلِ الْبَابِ.",
      "A joining waw, and «the rukhsa» is the mubtada in raf' — in the language it is an easing, and it was the fourth item in the list that opened this chapter. The definition now arrives.",
      "Atıf vâvı; «الرُّخْصَة» merfû mübtedâdır — lügatte kolaylaştırmadır ve bâbı açan listenin dördüncü kalemiydi. Tarifi şimdi geliyor.",
      segments=[seg("وَ","wa","conj"), seg("الرُّخْصَةُ","rukhsa","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَهَذَا هُوَ قَالَبُ الْحُدُودِ فِي هَذَا الْكِتَابِ كُلِّهِ: مُبْتَدَأٌ مَعْرِفَةٌ ثُمَّ «مَا» ثُمَّ فِعْلٌ.",
      "A relative noun, fixed on sukun, in the position of RAF' as the khabar — and this is the definitional frame the whole book is written in: a definite mubtada, then «ma», then a verb. Chapter 1 opened with it, chapter 14 used it four times, and it is the reason a bare negation must never be the first reading of a «ma» in this position.",
      "Sükûn üzere mebnî ism-i mevsûl; haber olarak mahallen MERFÛdur — ve bu, kitabın tamamının yazıldığı tarif kalıbıdır: marife mübtedâ, sonra «مَا», sonra fiil. Birinci bâb onunla açıldı, on dördüncü bâb onu dört kere kullandı; bu konumdaki bir «mâ»nın ilk okuyuşunun asla sade nefiy olmaması bundandır."),
  tok("شُرِعَ","sharaa","verb",["naib-al-fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» عَائِدٌ عَلَى «مَا» — وَقَاعِدَتُهُ: ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ.",
      "A mazi built for the unnamed doer, its naib al-fa'il a hidden «he» going back to the «ma» — and the rule is the mate of the one in sentence 2: raise the first letter and put a KASRA before the last. شَرَعَ becomes شُرِعَ. The doer is left unnamed here for the opposite reason to sentence 2's: there it was anyone, here it is the Lawgiver, and naming Him would make a definition read like a report.",
      "Meçhûl sîgasında mebnî mâzî; nâib-i fâili «مَا»ya râci' müstetir «هُوَ»dur — kâidesi, ikinci cümledekinin eşidir: evvelini zammeli, âhirinden öncekini KESRALI yap. «شَرَعَ», «شُرِعَ» olur. Fâil burada, ikinci cümlenin tam aksi bir sebeple gizlenmiştir: orada herkesti, burada Şâri'dir ve O'nu anmak, tarifi habere çevirirdi."),
  tok("لِعُذْرٍ","udhr","noun",["huruf-jarr","maful-lah"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«شُرِعَ»، وَاللَّامُ لِلتَّعْلِيلِ — وَتَنْكِيرُ «عُذْرٍ» مَقْصُودٌ: أَيُّ عُذْرٍ مُعْتَبَرٍ كَانَ.",
      "A jarr-majrur attaching to «was legislated», the lam naming the REASON — and «an excuse» is left indefinite on purpose: any excuse the Law counts. Had it been definite the definition would have named one case instead of a class.",
      "«شُرِعَ»a taalluk eden câr-mecrûr; lâm ta'lîl içindir — ve «عُذْرٍ»in nekre bırakılması kasıtlıdır: şer'an mu'teber HERHANGİ bir özür. Marife olsaydı tarif, bir sınıf yerine tek bir hâdiseyi anmış olurdu.",
      segments=[seg("لِ","li","prep"), seg("عُذْرٍ","udhr","noun")]),
  tok("مَعَ","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«شُرِعَ» — وَالْمُصَاحَبَةُ هُنَا زَمَانِيَّةٌ: الْحُكْمَانِ قَائِمَانِ مَعًا.",
      "A zarf in nasb and a mudaf, attaching to «was legislated» — and the accompaniment it names is in TIME: the two rulings stand together. This one word carries the whole difference between a dispensation and an abrogation, and chapter 12 is what it is answering.",
      "Zarfiyyet üzere mansub zarf ve muzâf; «شُرِعَ»a taalluk eder — ve ifade ettiği beraberlik ZAMÂNÎdir: iki hüküm birlikte durmaktadır. Bu tek kelime, ruhsat ile nesih arasındaki bütün farkı taşır ve cevap verdiği yer on ikinci bâbdır."),
  tok("قِيَامِ","qiyam","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «قَامَ» بِمَعْنَى الثَّبَاتِ وَالْبَقَاءِ، لَا الْقِيَامِ عَلَى الْقَدَمَيْنِ.",
      "The mudaf ilayh in jarr, itself a mudaf — the masdar of قَامَ in the sense of STANDING FIRM, not standing on one's feet. A chain of three: «with — the standing of — the evidence».",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — «قَامَ»nin, ayakta durmak değil SEBÂT ve bekā mânâsındaki masdarı. Üçlü bir zincir: «ile — durması — delîlin»."),
  tok("الدَّلِيلِ","dalil","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الْمُضَافُ إِلَيْهِ الثَّانِي فِي السِّلْسِلَةِ، وَكُلُّ حَلْقَةٍ تُضَيِّقُ مَا قَبْلَهَا.",
      "The second mudaf ilayh of the chain, in jarr — and each link narrows the one before it, exactly as the four-link idafa of chapter 12 did.",
      "Zincirin ikinci muzâfun ileyhi, mecrûr — ve her halka kendinden öncekini daraltır; tıpkı on ikinci bâbdaki dört halkalı izâfet gibi."),
  tok("الْمُحَرِّمِ","muharrim","noun",["naat-sifa","ism-fail","form-ii-verbs"],
      "نَعْتٌ لِـ«الدَّلِيلِ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «حَرَّمَ» عَلَى مُفَعِّلٍ، وَبِهِ تَمَّ الْحَدُّ: الدَّلِيلُ الْمُحَرِّمُ لَمْ يُرْفَعْ، وَإِنَّمَا رُخِّصَ فِي خِلَافِهِ لِعُذْرٍ.",
      "A na't of «the evidence», in jarr — the ism fa'il of Form II on مُفَعِّل, and with it the definition closes. The prohibiting evidence has NOT been lifted; leave has merely been granted to act otherwise while an excuse lasts. Set this against chapter 12: abrogation ends the first ruling, a dispensation leaves it standing and steps around it. One participle carries that whole distinction.",
      "«الدَّلِيلِ»in na'tı, mecrûr — «حَرَّمَ»den MÜFA'İL vezninde ism-i fâil; had onunla tamamlanır. Haram kılan delil KALDIRILMAMIŞTIR; yalnızca özür devam ettiği müddetçe hilâfına izin verilmiştir. Bunu on ikinci bâbla karşılaştırın: nesih ilk hükmü bitirir, ruhsat onu ayakta bırakır ve yanından dolaşır. Bu ayrımın tamamını tek bir ism-i fâil taşır.",
      punct="."),
 ],
 "jumal": [J("شُرِعَ لِعُذْرٍ مَعَ قِيَامِ الدَّلِيلِ الْمُحَرِّمِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "And whatever is established contrary to analogy — nothing else is measured against it.",
 "tr": "Kıyâsa muhâlif olarak sâbit olan şeye ise başkası kıyas edilmez."},
 "tokens": [
  tok("وَمَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar","anwa-ma"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَفِيهِ مَعْنَى الشَّرْطِ، وَلِذَلِكَ دَخَلَتِ الْفَاءُ عَلَى خَبَرِهِ.",
      "A resuming waw, and «ma» a relative noun, fixed in form, in the position of RAF' as the MUBTADA — and it carries the sense of a condition, which is why a fa may enter its khabar. Everywhere else in this book the ma has been a khabar; here for the first time it is the subject, and the difference is visible only from what follows it.",
      "İsti'nâf vâvı; «مَا» mebnî ism-i mevsûl, MÜBTEDÂ olarak mahallen MERFÛdur — ve şart mânâsı taşır; haberine fâ girmesinin sebebi budur. Bu kitapta «mâ» her yerde haber olmuştu; burada ilk defa mübtedâdır ve fark, yalnız kendisinden SONRA gelenden anlaşılır.",
      segments=[seg("وَ","wa","conj"), seg("مَا","ma-mawsula","pron")]),
  tok("ثَبَتَ","thabata","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» عَائِدٌ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ لَا مَحَلَّ لَهَا.",
      "A mazi on the fatha, its fa'il a hidden «he» returning to the «ma» — the sila again, and the ʿaid concealed again. The same verb stood in chapter 7 as the definition of dalala; there it took its evidence by a ba, here it takes its manner by an ʿala.",
      "Fetha üzere mebnî mâzî; fâili «مَا»ya râci' müstetir «هُوَ»dur — cümle sıladır, mahalli yoktur. Aynı fiil yedinci bâbda delâletin tarifinde durmuştu; orada delilini bâ ile alıyordu, burada keyfiyetini alâ ile alır."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«ثَبَتَ» — وَهِيَ هُنَا لِلْمُخَالَفَةِ لَا لِلِاسْتِعْلَاءِ.",
      "A jarr letter attaching to «is established» — and here it names DIVERGENCE, not the elevation it usually names. «Established upon a contrariety» is Arabic's way of saying: established, and against the rule.",
      "«ثَبَتَ»ye taalluk eden cer harfi — burada isti'lâ değil MUHÂLEFET ifade eder. «Bir muhalefet üzere sâbit olmak», Arapçanın «sâbittir, fakat kâideye aykırıdır» deme biçimidir."),
  tok("خِلَافِ","khilaf","noun",["idafa-definiteness","masdar"],
      "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ — مَصْدَرُ «خَالَفَ» عَلَى فِعَالٍ مِنْ «خ ل ف»، وَهُوَ الْجَذْرُ الَّذِي جَاءَ مِنْهُ «اِخْتِلَافُ الْأَحْوَالِ» فِي آخِرِ الْبَابِ الرَّابِعَ عَشَرَ.",
      "Majrur by «ala» and a mudaf — the Form III masdar of خَالَفَ on فِعَال, from خ ل ف: the root that closed chapter 14 in اخْتِلَافِ الْأَحْوَالِ. There it was a cause that must not vary; here it is a ruling that varies from the rule and is kept anyway.",
      "«عَلَى» ile mecrûr ve muzâf — «خ ل ف»den فِعَال vezninde «خَالَفَ»nin masdarı; on dördüncü bâbı kapatan «اخْتِلَافِ الْأَحْوَالِ»in kökünün aynısı. Orada değişmemesi gereken bir illetti, burada kâideden ayrılan ve buna rağmen korunan bir hüküm."),
  tok("الْقِيَاسِ","qiyas","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهَذَا الِاسْمُ ثَالِثُ مَرَّةٍ فِي الْبَابِ: فَاعِلًا مَرْفُوعًا، ثُمَّ فِي التَّرْكِيبِ، ثُمَّ مُضَافًا إِلَيْهِ.",
      "The mudaf ilayh in jarr — the third appearance of this noun in the chapter: first as a fa'il in raf', then in the title's own phrase, and now as a mudaf ilayh. Same word, three offices, one chapter.",
      "Mecrûr muzâfun ileyh — bu ismin bâbdaki üçüncü geçişi: önce merfû fâil, sonra bâb başlığının terkîbinde, şimdi muzâfun ileyh. Aynı kelime, üç vazife, tek bâb."),
  tok("فَغَيْرُهُ","ghayr","noun",["fa-khabar-mubtada","mubtada-khabar","idafa-definiteness"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الْمُبْتَدَإِ الْمُتَضَمِّنِ مَعْنَى الشَّرْطِ، وَ«غَيْرُ» مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "The FA is the linking fa of the khabar, admitted because the mubtada carries the sense of a condition — «whatever is established… THEN what is other than it…». It is not the fa of joining and not the fa of consequence; it is the one letter that shows a relative was doing a conditional's work. «Ghayr» is a second mubtada in raf' and a mudaf, the ha its mudaf ilayh.",
      "FÂ, şart mânâsı taşıyan mübtedânın haberine bağlayan râbıta fâsıdır — «her ne sâbit olursa... İŞTE ondan başkası...». Ne atıf fâsıdır ne de tefrî' fâsı; bir ism-i mevsûlün şart vazifesi gördüğünü gösteren tek harftir. «غَيْرُ» merfû ikinci mübtedâ ve muzâftır, hâ ise muzâfun ileyhtir.",
      segments=[seg("فَ","fa","conj"), seg("غَيْرُ","ghayr","noun"), seg("هُ","pron-3ms","pron")]),
  tok("عَلَيْهِ","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُقَاسُ»، وَقَدْ قُدِّمَ عَلَى عَامِلِهِ — وَالتَّقْدِيمُ يُفِيدُ الْقَصْرَ: عَلَيْهِ بِالذَّاتِ لَا يُقَاسُ.",
      "A jarr-majrur attaching to «is measured», and PUT BEFORE its governor — and that fronting narrows the sense: it is against THIS that nothing may be measured. The same حَرْفٌ عَلَى stood two words back meaning divergence; here it means what it usually means, the thing measured against. One letter, two senses, one sentence.",
      "«يُقَاسُ»a taalluk eden câr-mecrûr; âmilinin ÖNÜNE geçmiştir — ve bu takdîm kasr ifade eder: kıyas edilmeyen, bilhassa ONA kıyastır. Aynı «عَلَى» iki kelime önce muhalefet mânâsındaydı; burada mutâd mânâsındadır: kendisine kıyas edilen taraf. Tek harf, iki mânâ, tek cümle."),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُ «غَيْرُهُ»، وَجُمْلَةُ «غَيْرُهُ … لَا يُقَاسُ» فِي مَحَلِّ رَفْعٍ خَبَرُ «مَا».",
      "A bare negation — and the clause after it stands in the position of raf' as the khabar of «ghayruhu», while the whole of «ghayruhu … la yuqasu» stands in the position of raf' as the khabar of «ma». Two clauses nested, each holding the other's place: this is the shape the fa was announcing.",
      "Amel etmeyen nefiy — sonrasındaki cümle «غَيْرُهُ»nün haberi olarak mahallen merfû; «غَيْرُهُ ... لَا يُقَاسُ»un tamamı ise «مَا»nın haberi olarak mahallen merfûdur. İç içe iki cümle, her biri ötekinin yerini tutar: fânın haber verdiği yapı budur."),
  tok("يُقَاسُ","qasa","verb",["naib-al-fail","hollow-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» عَائِدٌ عَلَى «غَيْرُهُ» — وَهُوَ أَجْوَفُ يَائِيٌّ: «يَقِيسُ» فِي الْبِنَاءِ لِلْمَجْهُولِ تَنْقَلِبُ يَاؤُهُ أَلِفًا فَيَصِيرُ «يُقَاسُ».",
      "A mudari for the unnamed doer, in raf', its naib al-fa'il a hidden «he» going back to «what is other than it» — and the root is HOLLOW with a ya. Here the passive does more than move vowels: يَقِيسُ becomes يُقَاسُ, and the middle radical changes its very LETTER. That is why this form has to be memorised where تُدْرَكُ in sentence 2 could be built from the rule. The two verbs are put in one chapter for exactly this contrast.",
      "Meçhûl sîgasında merfû muzâri; nâib-i fâili «غَيْرُهُ»ne râci' müstetir «هُوَ»dur — kök ecvef-i yâîdir. Burada meçhûl, harekeleri değiştirmekle kalmaz: «يَقِيسُ», «يُقَاسُ» olur ve ayn harfi bizzat DEĞİŞİR. İkinci cümledeki «تُدْرَكُ» kâideden kurulabilirken bu sîganın ezberlenmesi gerekmesinin sebebi budur. İki fiil, tam da bu mukabele için tek bâbda toplanmıştır.",
      punct="."),
 ],
 "jumal": [J("ثَبَتَ عَلَى خِلَافِ الْقِيَاسِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("فَغَيْرُهُ عَلَيْهِ لَا يُقَاسُ",
   "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَا»، وَاقْتَرَنَتْ بِالْفَاءِ لِتَضَمُّنِ الْمُبْتَدَإِ مَعْنَى الشَّرْطِ.",
   "A nominal clause in the position of raf' as the khabar of «ma», joined by the FA because the mubtada carries the sense of a condition.",
   "«مَا»nın haberi olarak mahallen merfû isim cümlesi; mübtedâ şart mânâsı taşıdığı için FÂ ile bağlanmıştır.")]})

GLOSS_ADD = {
 "allah":      {"lemma": "اللَّه", "pos": "propn", "gloss": {"en": "Allah", "tr": "Allah"}, "level": 0},
 "hadd":       g("حَدّ", "ح د د", "noun", "hadd — a punishment the Law itself fixed; a limit", "had — şer'î ceza; sınır", 4, plural="حُدُود"),
 "kaffara":    g("كَفَّارَة", "ك ف ر", "noun", "expiation (lit. that which covers a sin)", "keffâret (günahı örten şey)", 5, plural="كَفَّارَات"),
 "muqaddarat": g("مُقَدَّرَات", "ق د ر", "noun", "the fixed amounts — what the Lawgiver settled by number or measure", "mukadderât — Şâri'in sayı yahut ölçüyle takdîr ettikleri", 5),
 "rukhsa":     g("رُخْصَة", "ر خ ص", "noun", "a dispensation — leave to act otherwise while an excuse lasts", "ruhsat — özür sürdükçe hilâfına izin", 4, plural="رُخَص"),
 "azima":      g("عَزِيمَة", "ع ز م", "noun", "the strict rule — what was laid down with no excuse in view", "azîmet — özür göz önünde tutulmaksızın konulan asıl hüküm", 4),
 "ism":        g("اسْم", "س م و", "noun", "name", "isim, ad", 1, plural="أَسْمَاء"),
 "lazima":     g("لَزِمَ", "ل ز م", "verb", "to be binding upon, to cleave to", "lâzım olmak, gerekmek", 3),
 "ibad":       g("عِبَاد", "ع ب د", "noun", "servants (plural of abd)", "kullar (abdin cem'i)", 2),
 "ijab":       g("إِيجَاب", "و ج ب", "noun", "making obligatory (Form IV masdar of وَجَبَ)", "îcâb; vâcib kılma (وَجَبَ'nin if'âl masdarı)", 3),
 "taala":      g("تَعَالَى", "ع ل و", "verb", "to be exalted (said of Allah)", "yüce olmak (Allah hakkında)", 2, form="VI"),
 "sharaa":     g("شَرَعَ", "ش ر ع", "verb", "to legislate, to lay down as law", "meşrû kılmak, şeriat koymak", 3),
 "udhr":       g("عُذْر", "ع ذ ر", "noun", "excuse", "özür, mazeret", 3, plural="أَعْذَار"),
 "maa":        g("مَعَ", None, "noun", "with, together with", "ile; beraber", 1),
 "qiyam":      g("قِيَام", "ق و م", "noun", "subsistence, standing firm", "kıyam, sebat, ayakta durma", 4),
 "muharrim":   g("مُحَرِّم", "ح ر م", "noun", "forbidding (ism fa'il, Form II)", "haram kılan (ism-i fâil, tef'îl)", 4),
 "khilaf":     g("خِلَاف", "خ ل ف", "noun", "disagreement; contrary", "muhalefet, hilâf", 3),
 "qasa":       g("قَاسَ", "ق ي س", "verb", "to measure one case against another", "kıyas etmek", 3),
}

def build_morph():
    out = {}
    # تَعَالَى — Form VI naqis. Copied from kitab-al-waqf after a lemma check;
    # four packages already carry this paradigm and none of them disagree.
    s = json.loads((ROOT / "content/samples/kitab-al-waqf/morphology.json").read_text(encoding="utf-8"))
    g_ = json.loads((ROOT / "content/samples/kitab-al-waqf/glossary.json").read_text(encoding="utf-8"))
    assert g_["entries"]["taala"]["lemma"] == GLOSS_ADD["taala"]["lemma"]
    out["taala"] = s["verbs"]["taala"]
    # لَزِمَ — sound, bab سَمِعَ. No majhul is stored: the verb is used here in
    # the active and a passive nobody wrote would be a guess wearing a fact's
    # clothes.
    out["lazima"] = _sg.sound1("samia", "لَزِم", "لْزَم", "اِلْزَم", "لُزُوم", "لَازِم",
                               maful="مَلْزُوم")
    # شَرَعَ — sound, bab فَتَحَ. Its MAJHUL is the sentence's own lesson and is
    # stored: ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ.
    out["sharaa"] = _sg.sound1("fataha", "شَرَع", "شْرَع", "اِشْرَع", "شَرْع", "شَارِع",
                               maful="مَشْرُوع", pmz="شُرِعَ", pmd="يُشْرَعُ",
                               note="مَجْهُولُ الْمَاضِي: ضَمُّ الْأَوَّلِ وَكَسْرُ مَا قَبْلَ الْآخِرِ — شُرِعَ.")
    # قَاسَ — أَجْوَفُ يَائِيٌّ from bab ضَرَبَ. The stems go in WITHOUT their sukun.
    # Its majhul is stored and NOT derivable: in a hollow verb the passive
    # changes the middle LETTER as well as the vowels — يَقِيسُ becomes يُقَاسُ —
    # and no vowel rule reaches that. This is the boundary the reader's own
    # majhul builder refuses to cross, and it is refused on purpose.
    out["qasa"] = _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "قَاس", "قِس", "قِيس", "قِس",
                              "قِيس", "قِس", "قِيَاس", "قَائِس",
                              maful="مَقِيس", pmz="قِيسَ", pmd="يُقَاسُ",
                              note="أَجْوَفُ يَائِيٌّ: قِيلَ وَبِيعَ وَقِيسَ عَلَى قِيَاسٍ وَاحِدٍ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/15.json").write_text(
    json.dumps({"chapter": 15, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 15 for c in man["chapters"]):
    man["chapters"].append({"n": 15, "title": TITLE15})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.15.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch15:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
