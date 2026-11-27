# -*- coding: utf-8 -*-
"""Author chapter 2 of mukhtasar-al-manar — the four sources, and the first two named.

Chapter 1 gave the three opening definitions (usul al-fiqh, asl, fiqh). The matn
then turns from defining its terms to naming its SOURCES, and takes them up one
at a time with أَمَّا … فَ.

ATTRIBUTION, and it matters: the package's chapter 1 was transcribed from a
printed page the project owner supplied. NO transcription was supplied for what
follows it, so this chapter is set from the RECEIVED matn — the wording every
edition of the Hanafi usul tradition carries at this point — and that is
recorded in the manifest attribution rather than passed off as the owner's
page. The package is already `pending-scholarly-review`; this chapter is the
part of it most in need of that review.

Grammar this chapter is chosen to teach:
  • أَمَّا … فَ — three jobs in one letter (condition, detailing, emphasis) and
    the one hard rule: the answer MUST carry the fa, and the fa may never touch
    أَمَّا. A new registry note, `amma-tafsiliyya`, is written alongside it.
  • دَفَّتَيِ الْمُصْحَفِ — a DUAL as mudaf, so its nun falls exactly where a
    tanwin would: the Idafa engine's rule 2 on the page.
  • نَقْلًا مُتَوَاتِرًا — a maf'ul mutlaq, the masdar that confirms the verbal
    force of the participle before it.
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

TITLE2 = {"ar": "الْأَدِلَّةُ الْأَرْبَعَة", "en": "The Four Sources", "tr": "Dört Delil"}

S.append({"id": "s1", "translation": {
 "en": "Then the sources are four: the Book, the Sunna, consensus and analogy.",
 "tr": "Deliller dörttür: Kitâb, Sünnet, icmâ ve kıyâs."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ مَعَ التَّرَاخِي — انْتَقَلَ بِهِ مِنَ التَّعْرِيفَاتِ إِلَى الْمَقْصُودِ.",
      "A letter of atf giving sequence with an interval — with it the matn steps from defining its terms to its real subject.",
      "Terâhî ile tertîb bildiren atıf harfi — metin onunla tariflerden asıl maksada geçer."),
  tok("الْأَدِلَّةُ","adilla","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ «دَلِيلٍ» عَلَى أَفْعِلَةٍ.",
      "The mubtada in raf' by the damma — the plural of «dalil» on أَفْعِلَة.",
      "Damme ile merfû mübtedâ — «دَلِيل»in EF'İLE vezninde cemidir."),
  tok("أَرْبَعَةٌ","arbaa","noun",["mubtada-khabar","tamyiz"],
      "خَبَرٌ مَرْفُوعٌ — وَلَحِقَتْهُ التَّاءُ لِأَنَّ مَعْدُودَهُ مُذَكَّرٌ، وَالْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُخَالِفُ مَعْدُودَهُ.",
      "The khabar in raf' — and it wears the TA because what it counts is masculine: from three to ten the number takes the OPPOSITE gender to the thing counted.",
      "Merfû haber — ma'dûdu müzekker olduğu için TÂ almıştır: üçten ona kadar sayı, ma'dûduna ZIT cinste gelir.", punct="："),
  tok("الْكِتَابُ","kitab","noun",["badal","mubtada-khabar"],
      "بَدَلٌ مِنْ «أَرْبَعَةٌ» مَرْفُوعٌ — بَدَلُ تَفْصِيلٍ يُفَصِّلُ الْمُجْمَلَ قَبْلَهُ.",
      "A badal of «four», in raf' — a badal of DETAIL, which unpacks the summary before it.",
      "«أَرْبَعَةٌ»den merfû bedel — öncesindeki icmâli açan TAFSÎL bedelidir."),
  tok("وَالسُّنَّةُ","sunna","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ.", "Joined, in raf'.", "Ma'tûf, merfû.",
      segments=[seg("وَ","wa","conj"), seg("السُّنَّةُ","sunna","noun")]),
  tok("وَالْإِجْمَاعُ","ijma","noun",["atf-nasaq","masdar","form-iv-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ «أَجْمَعَ» عَلَى إِفْعَالٍ.",
      "Joined, in raf' — the masdar of أَجْمَعَ on إِفْعَال.",
      "Ma'tûf, merfû — «أَجْمَعَ»nin İF'ÂL vezninde masdarı.",
      segments=[seg("وَ","wa","conj"), seg("الْإِجْمَاعُ","ijma","noun")]),
  tok("وَالْقِيَاسُ","qiyas","noun",["atf-nasaq","masdar","form-iii-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ «قَايَسَ»، وَبِهِ تَمَّ الْعَدُّ أَرْبَعَةً.",
      "Joined, in raf' — the masdar of قَايَسَ, and with it the count of four is complete.",
      "Ma'tûf, merfû — «قَايَسَ»nin masdarı; dörtlü sayım bununla tamamlanır.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("الْقِيَاسُ","qiyas","noun")]),
 ],
 "jumal": [J("الْأَدِلَّةُ أَرْبَعَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "As for the Book, it is the Qur'an transmitted to us between the two covers of the codex by a mass transmission.",
 "tr": "Kitâb'a gelince, o bize mushafın iki kapağı arasında mütevâtir bir nakille nakledilen Kur'ân'dır."},
 "tokens": [
  tok("أَمَّا","amma","part",["amma-tafsiliyya"],
      "حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ، نَابَ عَنْ «مَهْمَا يَكُنْ مِنْ شَيْءٍ» — وَلِذَلِكَ لَزِمَتِ الْفَاءُ فِي جَوَابِهِ.",
      "A letter of CONDITION, of DETAILING and of EMPHASIS at once, standing in for «whatever may be of the matter» — which is why its answer must carry the FA.",
      "Aynı anda ŞART, TAFSÎL ve TE'KÎD harfi; «مَهْمَا يَكُنْ مِنْ شَيْءٍ»in yerini tutar — cevabında FÂ'nın zorunlu olmasının sebebi budur."),
  tok("الْكِتَابُ","kitab","noun",["mubtada-khabar","amma-tafsiliyya"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَلَا بُدَّ مِنْ فَاصِلٍ بَيْنَ «أَمَّا» وَفَائِهَا، وَهَذَا الْمُبْتَدَأُ هُوَ الْفَاصِلُ.",
      "The mubtada in raf' — something must stand between «amma» and its fa, and this mubtada is that something: the very word being singled out.",
      "Merfû mübtedâ — «أَمَّا» ile fâsı arasına mutlaka bir fâsıl girmelidir; işte ayrılıp öne çıkarılan bu mübtedâ o fâsıldır."),
  tok("فَهُوَ","huwa","pron",["amma-tafsiliyya","mubtada-khabar"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ«هُوَ» ضَمِيرُ فَصْلٍ أَوْ مُبْتَدَأٌ ثَانٍ، وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.",
      "The FA is the one that falls in «amma»'s answer, and «huwa» is either a separating pronoun or a second mubtada; the clause is the khabar of the first.",
      "FÂ, «أَمَّا»nın cevabına düşen fâdır; «هُوَ» ise fasıl zamîri yahut ikinci mübtedâdır, cümle de birincinin haberidir.",
      segments=[seg("فَ","fa","conj"), seg("هُوَ","huwa","pron")]),
  tok("الْقُرْآنُ","quran","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The khabar, in raf' by the damma.", "Damme ile merfû haber."),
  tok("الْمَنْقُولُ","manqul","noun",["naat-sifa","ism-maful"],
      "نَعْتٌ لِـ«الْقُرْآنُ» مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «نَقَلَ»، وَهُوَ يَعْمَلُ عَمَلَ فِعْلِهِ فَيَتَعَلَّقُ بِهِ مَا بَعْدَهُ.",
      "A na't of «the Qur'an», in raf' — the ism maf'ul of نَقَلَ, and it GOVERNS like its verb, so what follows attaches to it.",
      "«الْقُرْآنُ»un na'tı, merfû — «نَقَلَ»nin ism-i mef'ûlü; fiili gibi amel eder, bu yüzden sonrası ona taalluk eder."),
  tok("إِلَيْنَا","ilayna","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«الْمَنْقُولُ».",
      "A jarr-majrur attaching to «transmitted».",
      "«الْمَنْقُولُ»a taalluk eden câr-mecrûr.",
      segments=[seg("إِلَى","ila","prep"), seg("نَا","pron-1p","pron")]),
  tok("بَيْنَ","bayna","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«الْمَنْقُولُ».",
      "A place-adverb in nasb and a mudaf, attaching to «transmitted».",
      "Mansub mekân zarfı ve muzâf; «الْمَنْقُولُ»a taalluk eder."),
  tok("دَفَّتَيِ","daffa","noun",["al-muthanna","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ — وَكُسِرَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "The mudaf ilayh, in jarr by the YA because it is a DUAL — and its NUN has fallen for the idafa, exactly where a tanwin would have fallen. The ya then takes a kasra because two sukuns met.",
      "Mecrûr muzâfun ileyh; TESNİYE olduğu için YÂ ile mecrûrdur ve NÛNu izâfet sebebiyle düşmüştür — tenvînin düşeceği yerde. İki sâkin yan yana geldiği için yâ kesra almıştır."),
  tok("الْمُصْحَفِ","mushaf","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ آلَةٍ عَلَى مُفْعَلٍ فِي الْأَصْلِ: مَا يُصْحَفُ فِيهِ.",
      "The mudaf ilayh in jarr — in origin a tool-noun on مُفْعَل: the thing the pages are gathered in.",
      "Mecrûr muzâfun ileyh — aslında MUF'AL vezninde ism-i âlettir: sahifelerin toplandığı şey."),
  tok("نَقْلًا","naql","noun",["maful-mutlaq","masdar"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرٌ مُؤَكِّدٌ لِعَامِلِهِ «الْمَنْقُولُ»، وَبِهِ ثَبَتَ أَنَّ اسْمَ الْمَفْعُولِ عَامِلٌ حَقًّا.",
      "A MAF'UL MUTLAQ in nasb — the masdar that confirms its own governor «transmitted». Its presence is the proof that the participle really does govern.",
      "Mansub MEF'ÛL-Ü MUTLAK — âmili olan «الْمَنْقُولُ»u te'kîd eden masdardır. Varlığı, ism-i mef'ûlün gerçekten amel ettiğinin delilidir."),
  tok("مُتَوَاتِرًا","mutawatir","noun",["naat-sifa","ism-fail","form-vi-verbs"],
      "نَعْتٌ لِـ«نَقْلًا» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «تَوَاتَرَ» عَلَى مُتَفَاعِلٍ، وَهُوَ النَّقْلُ الَّذِي يَسْتَحِيلُ تَوَاطُؤُ نَقَلَتِهِ عَلَى الْكَذِبِ.",
      "A na't of «a transmission», in nasb — the ism fa'il of تَوَاتَرَ on مُتَفَاعِل: the transmission whose transmitters could not possibly have agreed on a lie.",
      "«نَقْلًا»ın na'tı, mansub — «تَوَاتَرَ»nin MÜTEFÂİL vezninde ism-i fâili: nakledenlerinin yalan üzerinde birleşmesi imkânsız olan nakil.",
      punct="."),
 ],
 "jumal": [J("أَمَّا الْكِتَابُ فَهُوَ الْقُرْآنُ",
   "جُمْلَةٌ اسْمِيَّةٌ وَقَعَتْ جَوَابًا لِـ«أَمَّا» — لَا مَحَلَّ لَهَا.",
   "A nominal clause standing as «amma»'s answer — i'rabless.",
   "«أَمَّا»nın cevabı olarak düşen isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And as for the Sunna, it is what issued from the Prophet by way of word, deed or tacit approval.",
 "tr": "Sünnet'e gelince, o Peygamber'den söz, fiil yahut takrîr olarak sâdır olandır."},
 "tokens": [
  tok("وَأَمَّا","amma","part",["atf-nasaq","amma-tafsiliyya"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَمَّا» تَفْصِيلِيَّةٌ — وَبِهَا يُسَاقُ الْبَنْدُ الثَّانِي مِنَ التَّعْدَادِ.",
      "A joining waw and the detailing «amma» — with it the enumeration is carried on to its second item.",
      "Atıf vâvı ve tafsîl «emmâ»sı — sayımın ikinci maddesi bununla getirilir.",
      segments=[seg("وَ","wa","conj"), seg("أَمَّا","amma","part")]),
  tok("السُّنَّةُ","sunna","noun",["mubtada-khabar","amma-tafsiliyya"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ الْفَاصِلُ بَيْنَ «أَمَّا» وَفَائِهَا.",
      "The mubtada in raf', and the thing standing between «amma» and its fa.",
      "Merfû mübtedâ; «أَمَّا» ile fâsı arasındaki fâsıldır."),
  tok("فَمَا","ma-mawsula","pron",["amma-tafsiliyya","ism-mawsul"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "The fa of «amma»'s answer, and «ma» is a RELATIVE noun — fixed in form, in the position of raf' as the khabar.",
      "«أَمَّا»nın cevabındaki fâ; «مَا» ise mebnî ism-i mevsûldür, haber olarak mahallen merfûdur.",
      segments=[seg("فَ","fa","conj"), seg("مَا","ma-mawsula","pron")]),
  tok("صَدَرَ","sadara","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، لَا مَحَلَّ لَهَا.",
      "A past verb with a hidden «he» for its fa'il — and the clause is the SILA of the relative, which never has a position in i'rab.",
      "Mâzî fiil, fâili müstetir «هُوَ» — cümle ism-i mevsûlün SILAsıdır ve sılanın i'râbda mahalli olmaz."),
  tok("عَنِ","an-prep","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ، مُتَعَلِّقٌ بِـ«صَدَرَ» — وَكُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter of going-out-from, attaching to «issued» — its nun takes a kasra because two sukuns met.",
      "Mücâveze için cer harfi; «صَدَرَ»ye taalluk eder — iki sâkin karşılaştığı için nûnu kesra almıştır."),
  tok("النَّبِيِّ","nabi","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَنْ» بِالْكَسْرَةِ — فَعِيلٌ بِمَعْنَى مَفْعُولٍ عَلَى قَوْلٍ: الْمُنَبَّأُ.",
      "In jarr after «an» by the kasra — فَعِيل in the sense of مَفْعُول on one reading: the one informed.",
      "«عَنْ» ile kesra üzere mecrûr — bir görüşe göre mef'ûl mânâsında FAÎLdir: kendisine haber verilen."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْبَيَانِ، وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنَ الضَّمِيرِ فِي «صَدَرَ».",
      "A jarr letter of EXPLAINING what a thing consists of; the phrase is a hal from the pronoun inside «issued».",
      "Beyâniyye cer harfi; câr-mecrûr, «صَدَرَ»deki zamîrden hâldir."),
  tok("قَوْلٍ","qawl","noun",["huruf-jarr","masdar"],
      "مَجْرُورٌ بِـ«مِنْ» — مَصْدَرُ «قَالَ».",
      "In jarr after «min» — the masdar of قَالَ.",
      "«مِنْ» ile mecrûr — «قَالَ»nin masdarı."),
  tok("أَوْ","aw","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّنْوِيعِ لَا لِلشَّكِّ — يَعُدُّ الْأَنْوَاعَ وَلَا يَتَرَدَّدُ بَيْنَهَا.",
      "A letter of atf giving KINDS, not doubt: it lists the sorts of thing, it does not waver between them.",
      "Şüphe için değil TENVΑ için atıf harfi: nevileri sayar, aralarında tereddüt etmez."),
  tok("فِعْلٍ","fil","noun",["atf-nasaq","masdar"],
      "مَعْطُوفٌ عَلَى «قَوْلٍ» مَجْرُورٌ.",
      "Joined to «word», in jarr.", "«قَوْلٍ»e ma'tûf, mecrûr."),
  tok("أَوْ","aw","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّنْوِيعِ.", "Another atf of kinds.", "Yine tenvî için atıf harfi."),
  tok("تَقْرِيرٍ","taqrir","noun",["atf-nasaq","masdar","form-ii-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ «قَرَّرَ» عَلَى تَفْعِيلٍ، وَهُوَ سُكُوتُهُ عَنِ الْفِعْلِ يُفْعَلُ بِحَضْرَتِهِ.",
      "Joined, in jarr — the masdar of قَرَّرَ on تَفْعِيل: his saying nothing about an act done in his presence, which is itself a ruling.",
      "Ma'tûf, mecrûr — «قَرَّرَ»nin TEF'ÎL vezninde masdarı: huzurunda yapılan bir fiile susmasıdır ki bu da bir hükümdür.",
      punct="."),
 ],
 "jumal": [J("وَأَمَّا السُّنَّةُ فَمَا صَدَرَ عَنِ النَّبِيِّ",
   "جُمْلَةٌ اسْمِيَّةٌ وَقَعَتْ جَوَابًا لِـ«أَمَّا» — لَا مَحَلَّ لَهَا.",
   "A nominal clause standing as «amma»'s answer — i'rabless.",
   "«أَمَّا»nın cevabı olarak düşen isim cümlesi — mahalsizdir."),
  J("صَدَرَ عَنِ النَّبِيِّ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "thumma":     g("ثُمَّ", None, "conj", "then (with an interval)", "sonra (araya zaman girerek)", 1),
 "arbaa":      g("أَرْبَعَة", "ر ب ع", "noun", "four", "dört", 1),
 "kitab":      g("كِتَاب", "ك ت ب", "noun", "the Book, scripture", "Kitâb", 1, plural="كُتُب"),
 "sunna":      g("سُنَّة", "س ن ن", "noun", "the Sunna, the trodden way", "sünnet", 2, plural="سُنَن"),
 "ijma":       g("إِجْمَاع", "ج م ع", "noun", "consensus (masdar, Form IV)", "icmâ (masdar)", 4),
 "qiyas":      g("قِيَاس", "ق ي س", "noun", "analogy (masdar, Form III)", "kıyâs (masdar)", 4),
 "amma":       g("أَمَّا", None, "part", "as for … (detailing; its answer takes فَ)", "…e gelince (tafsîl; cevabı فَ alır)", 4),
 "fa":         g("فَ", None, "conj", "so, then (joining letter)", "ve, öyleyse (atıf harfi)", 1),
 "quran":      g("قُرْآن", "ق ر أ", "noun", "the Qur'an", "Kur'ân", 1),
 "manqul":     g("مَنْقُول", "ن ق ل", "noun", "transmitted (ism maf'ul)", "menkūl; nakledilen", 3),
 "ilayna":     g("إِلَيْنَا", None, "prep", "to us", "bize", 1),
 "ila":        g("إِلَى", None, "prep", "to, toward (jarr letter)", "-e, -a (cer harfi)", 1),
 "bayna":      g("بَيْنَ", "ب ي ن", "noun", "between (adverb of place)", "arasında (mekân zarfı)", 1),
 "daffa":      g("دَفَّة", "د ف ف", "noun", "a cover, one board of a binding", "kapak; cildin bir kanadı", 5, plural="دَفَّتَانِ"),
 "mushaf":     g("مُصْحَف", "ص ح ف", "noun", "the codex, the bound Qur'an", "mushaf", 2),
 "naql":       g("نَقْل", "ن ق ل", "noun", "transmission (masdar)", "nakil (masdar)", 3),
 "mutawatir":  g("مُتَوَاتِر", "و ت ر", "noun", "mass-transmitted (ism fa'il, Form VI)", "mütevâtir", 5),
 "sadara":     g("صَدَرَ", "ص د ر", "verb", "to issue, come forth", "sâdır olmak", 3),
 "an-prep":    g("عَنْ", None, "prep", "from, away from (jarr letter)", "-den (cer harfi)", 1),
 "nabi":       g("نَبِيّ", "ن ب أ", "noun", "prophet", "nebî, peygamber", 1, plural="أَنْبِيَاء"),
 "min":        g("مِنْ", None, "prep", "from; consisting of (jarr letter)", "-den; …olarak (cer harfi)", 1),
 "qawl":       g("قَوْل", "ق و ل", "noun", "a word, a saying (masdar)", "söz (masdar)", 1),
 "aw":         g("أَوْ", None, "conj", "or (here: listing kinds)", "yahut (burada: nevi sayar)", 1),
 "fil":        g("فِعْل", "ف ع ل", "noun", "a deed, an act (masdar)", "fiil, iş (masdar)", 1),
 "taqrir":     g("تَقْرِير", "ق ر ر", "noun", "tacit approval — his silence at an act (masdar, Form II)", "takrîr — bir fiile susarak onay (masdar)", 5),
 "pron-1p":    g("نَا", None, "pron", "us, our", "biz, -imiz", 1),
}

def build_morph():
    out = {}
    # صَدَرَ — sound, bab nasara. Its masdar صُدُور is the one the usul books use.
    out["sadara"] = _sg.sound1("nasara", "صَدَر", "صْدُر", "اُصْدُر", "صُدُور", "صَادِر",
                               note="مِنْ بَابِ نَصَرَ — وَمَصْدَرُهُ صُدُورٌ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/2.json").write_text(
    json.dumps({"chapter": 2, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 2 for c in man["chapters"]):
    man["chapters"].append({"n": 2, "title": TITLE2})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.2.0"
man["title"] = {"ar": "مُخْتَصَرُ الْمَنَار: التَّعْرِيفَاتُ وَالْأَدِلَّة",
                "en": "Mukhtasar al-Manar: The Definitions and the Sources",
                "tr": "Muhtasaru'l-Menâr: Tarifler ve Deliller"}
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة الأربعة وبيان الكتاب والسنة",
                   "en": "The opening definitions, then the four sources with the Book and the Sunna set out",
                   "tr": "Açılış tarifleri, sonra dört delil ile Kitâb ve Sünnet'in beyânı"}
# The note is written in EACH language — an English sentence parked in the `tr`
# field is not a bilingual app, and attribution is the one field a reader is
# most entitled to read in their own language.
NOTE = {
 "en": ("Chapter 2 onward is set from the RECEIVED matn of the Hanafi usul tradition, "
        "not from the owner's supplied page — no transcription was supplied beyond page 1. "
        "It is the part of this package most in need of the scholarly review already pending."),
 "tr": ("İkinci bölümden itibaren metin, proje sahibinin verdiği sayfadan değil, Hanefî usûl "
        "geleneğinin MEŞHÛR matnından alınmıştır — birinci sayfanın ötesi için herhangi bir "
        "transkripsiyon verilmemiştir. Bu paketin, hâlihazırda beklemekte olan ilmî tashîhe "
        "en çok muhtaç olan kısmı burasıdır."),
 "ar": ("وَمَا بَعْدَ الْبَابِ الْأَوَّلِ مَأْخُوذٌ مِنَ الْمَتْنِ الْمُتَدَاوَلِ عِنْدَ الْحَنَفِيَّةِ، "
        "لَا مِنَ الصَّحِيفَةِ الْمُسَلَّمَةِ؛ إِذْ لَمْ يُسَلَّمْ مِنْهَا إِلَّا الْأُولَى، "
        "وَهُوَ أَحْوَجُ مَا فِي هَذَا الْكِتَابِ إِلَى الْمُرَاجَعَةِ الْعِلْمِيَّةِ الْمُنْتَظَرَةِ."),
}
BASE_TR = ("Proje sahibinin verdiği Muhtasaru'l-Menâr ders notlarından (1. sayfa) alınan tarifler; "
           "eser, Kāsım b. Kutlubuğa el-Hanefî'nin usûl-i fıkha dâir muhtasarıdır. Matbû sayfadan "
           "istinsah edilmiştir; oradaki şerh Osmanlı Türkçesiyledir. Neşirden önce matbû bir "
           "nüsha ile karşılaştırılmalıdır.")
for lang in ("en", "tr", "ar"):
    cur = man["attribution"].get(lang, "").strip()
    # repair: an earlier pass appended the English note to the empty tr field
    for other in NOTE.values():
        if lang != "tr" or other == NOTE["tr"]:
            continue
        cur = cur.replace(other, "").strip()
    if lang == "tr" and not cur:
        cur = BASE_TR
    if NOTE[lang] not in cur:
        cur = (cur + " " + NOTE[lang]).strip()
    man["attribution"][lang] = cur
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch2:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
