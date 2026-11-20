# -*- coding: utf-8 -*-
"""Author chapter 4 of talkhis-al-miftah — خِلَافُ مُقْتَضَى الظَّاهِر.

Chapter 3 stated the rule in three sentences. This chapter is the exception,
and the exception is where ʿilm al-maʿani actually lives: a speaker may treat a
hearer as the man he is NOT, and the sentence is then built for the man he has
been made into. A listener who never asked is answered as though he had; a man
who is not denying is argued with; a denier is spoken to gently because the
evidence in front of him ought to have been enough.

Each of the three has a TRIGGER, and the matn names it — a preceding word that
raised the question, a visible sign of denial, a proof already in his hands.
Without the trigger the departure is not eloquence but error, which is why the
three إِذَا clauses are the load-bearing half of every sentence here.

ATTRIBUTION: the received matn of the Talkhis. The supplied Ottoman commentary
(research/sources/talkhis-al-miftah-balagha.txt, lines ~480-515) carries all
three cases as Turkish prose with their Arabic evidence vowelled: al-Muʾminun
23:27 for the first, the verse of Ḥajl for the second, al-Baqara 2:2 for the
third, and the negative triad مَا زَيْدٌ قَائِمًا / مَا زَيْدٌ بِقَائِمٍ / وَاللهِ مَا
زَيْدٌ بِقَائِمٍ for s4. Nothing here is composed.

Grammar this chapter is chosen to teach:
  • خَالِي الذِّهْنِ as a MARFUʿ naib al-fail — the same phrase chapter 3 showed
    in jarr. A manqus estimates its damma AND its kasra and writes only its
    fatha, so the reader now has two of the three in real text.
  • مَنْزِلَةَ — the second object surviving a passive, for the third package
    in a row, and here on a verb nobody would call doubly transitive at sight.
  • مَا إِنْ تَأَمَّلَهُ ارْتَدَعَ — a sila that is a whole CONDITIONAL sentence.
  • مَنْفِيّ — the ism mafʿul of a NAQIS: مَنْفُوي with the waw turned ya and
    merged. The i'lal engine derives it from nothing.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/talkhis-al-miftah"
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

TITLE4 = {"ar": "خِلَافُ مُقْتَضَى الظَّاهِر",
          "en": "Speaking Against What the Surface Calls For",
          "tr": "Muktezâ-yı Zâhirin Hilâfı"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "A mind empty of the ruling is put in the place of one who asks, when something has come earlier in the speech that points to the report.",
 "tr": "Zihni hükümden hâlî olan kimse, kelâmda daha önce habere işaret eden bir şey geçmişse, soran kimsenin yerine konur."},
 "tokens": [
  tok("وَقَدْ","qad","part",["qad-harf"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«قَدْ» مَعَ الْمُضَارِعِ لِلتَّقْلِيلِ — وَهِيَ الْحَرْفُ نَفْسُهُ الَّذِي خُتِمَ بِهِ الْبَابُ الثَّالِثُ، فَالْبَابُ يَبْتَدِئُ مِنْ حَيْثُ وَقَفَ الَّذِي قَبْلَهُ.",
      "A resuming waw, and «qad» with a mudari means «sometimes» — the very letter chapter 3 closed on, so this chapter opens exactly where that one stopped. What was announced there as a possibility is now taken apart into its three cases.",
      "İsti'nâf vâvı; ve muzâri ile «قَدْ» taklîl ifade eder — üçüncü bâbın kendisiyle kapandığı harfin ta kendisi; öyleyse bu bâb, bir öncekinin durduğu yerden başlar. Orada bir ihtimâl olarak duyurulan şey, burada üç hâline ayrılıyor.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يُنَزَّلُ","nazzala","verb",["khilaf-muqtada-al-zahir","naib-al-fail","mafulayn","form-ii-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ — مِنْ «نَزَّلَ» عَلَى التَّفْعِيلِ، وَهُوَ يَتَعَدَّى إِلَى مَفْعُولَيْنِ.",
      "A mudari built for the unnamed doer, in raf' with the damma written — from نَزَّلَ on تَفْعِيل, and it reaches TWO objects. Nobody would call «to put down» doubly transitive at sight; the second object arrives two words later and its fatha is the proof. The doer is unnamed because the rule holds for any speaker at all.",
      "Meçhûl sîgasında, zâhir damme ile merfû muzâri — TEF'ÎL vezninde «نَزَّلَ»den; ve İKİ mef'ûle geçer. «İndirmek»e bakıp iki mef'ûllü diyecek kimse yoktur; ikinci mef'ûl iki kelime sonra gelir ve fethası delîldir. Fâil anılmaz, çünkü kâide her mütekellim için geçerlidir."),
  tok("خَالِي","khali","noun",["naib-al-fail","ism-maqsur-manqus","idafa-lafziyya","idafa-definiteness"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ ضَمَّةٌ مُقَدَّرَةٌ عَلَى الْيَاءِ لِلثِّقَلِ، وَهُوَ مُضَافٌ — وَهُوَ اللَّفْظُ نَفْسُهُ الَّذِي وَرَدَ فِي الْبَابِ الثَّالِثِ مَجْرُورًا.",
      "The naib al-fa'il in raf' with a damma ESTIMATED on the ya for heaviness, and a mudaf — and it is the very phrase chapter 3 showed in JARR with an estimated kasra. A manqus estimates both its damma and its kasra and writes only its fatha, so the reader now has two of the three states in real text, on one phrase, one chapter apart.",
      "Sıklet sebebiyle yâ üzerinde MUKADDER damme ile merfû nâib-i fâil ve muzâf — ve üçüncü bâbın MECRÛR olarak gösterdiği ibarenin ta kendisi. Menkūs, hem dammesini hem kesrasını mukadder kılar, yalnız fethasını yazar; öyleyse okuyucu artık üç hâlin ikisini gerçek metinde, tek ibare üzerinde, bir bâb arayla görmüştür."),
  tok("الذِّهْنِ","dhihn","noun",["idafa-definiteness","idafa-lafziyya"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فَاعِلُ «خَالِي» مَعْنًى، وَالْإِضَافَةُ لَفْظِيَّةٌ فَلَا تُفِيدُ تَعْرِيفًا.",
      "The mudaf ilayh in jarr — the fa'il of «empty» in meaning, and the annexation is lafziyya, so nothing is made definite. That matters here: a definite naib al-fa'il would name one particular man, and the matn is stating a rule about a kind.",
      "Mecrûr muzâfun ileyh — mânen «خَالِي»nin fâilidir; ve izâfet lafziyyedir, hiçbir şeyi marife yapmaz. Bu burada mühimdir: marife bir nâib-i fâil belirli bir kişiyi anardı; metin ise bir cinse dair kâide koyuyor."),
  tok("مَنْزِلَةَ","manzila","noun",["khilaf-muqtada-al-zahir","mafulayn","maful-bihi","idafa-definiteness"],
      "الْمَفْعُولُ الثَّانِي لِـ«يُنَزَّلُ» مَنْصُوبٌ بِالْفَتْحَةِ وَهُوَ مُضَافٌ — بَقِيَ عَلَى نَصْبِهِ لِأَنَّ الْأَوَّلَ أَخَذَ مَقَامَ الْفَاعِلِ.",
      "The SECOND object of «is put», in nasb by the fatha and a mudaf — it kept its nasb because the first object had already taken the doer's seat. Third package in a row for this rule, and here it is doing real work: without the fatha the phrase would read as a place, and the sentence would be about furniture.",
      "«يُنَزَّلُ»nin İKİNCİ mef'ûlü, fetha ile mansub ve muzâf — nasbını korumuştur, zira fâil makāmını birinci mef'ûl almıştır. Bu kâide için üst üste üçüncü paket; ve burada gerçek bir iş görür: fetha olmasaydı ibare bir mekân gibi okunur ve cümle eşyadan bahseder olurdu."),
  tok("السَّائِلِ","sail","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «سَأَلَ»، وَهُوَ الْمُتَرَدِّدُ الطَّالِبُ فِي الْبَابِ الثَّالِثِ.",
      "The mudaf ilayh in jarr — the ism fa'il of سَأَلَ, and «the one who asks» is chapter 3's hesitating-and-seeking hearer under a shorter name. The matn is compressing a two-condition description into one word, which it can do only because the previous chapter did the work.",
      "Mecrûr muzâfun ileyh — «سَأَلَ»nin ism-i fâili; ve «soran», üçüncü bâbın tereddüd edip taleb eden muhâtabının kısa adıdır. Metin, iki şartlı bir tarifi tek kelimeye sıkıştırır; bunu ancak bir önceki bâb işi gördüğü için yapabilir."),
  tok("إِذَا","idha","part",["idha-shartiyya"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، خَافِضٌ لِشَرْطِهِ مُتَعَلِّقٌ بِجَوَابِهِ — وَلَا يَجْزِمُ.",
      "A zarf of future time carrying the sense of a condition — and it does NOT put its verbs in jazm, which is the whole difference between it and إِنْ two sentences back in chapter 3. The clause it opens is the TRIGGER, and everything this chapter permits depends on it: without the trigger the departure from the surface is not eloquence, it is a mistake.",
      "Şart mânâsı taşıyan, gelecek zaman zarfı — ve fiillerini CEZMETMEZ; üçüncü bâbdaki «إِنْ» ile arasındaki bütün fark budur. Açtığı cümle TETİKLEYİCİdir ve bu bâbın izin verdiği her şey ona bağlıdır: tetikleyici yoksa zâhirden ayrılmak belâgat değil hatâdır."),
  tok("تَقَدَّمَ","taqaddama","verb",["idha-shartiyya","fail","form-v-verbs"],
      "فِعْلٌ مَاضٍ فِعْلُ الشَّرْطِ لِـ«إِذَا» — عَلَى تَفَعَّلَ مِنْ «ق د م»، وَبِنَاءُ التَّفَعُّلِ هُنَا لِلْمُطَاوَعَةِ.",
      "A mazi, the condition's verb after «idha» — on تَفَعَّلَ from ق د م. What has «gone before» is the point: the trigger has to be already on the page when the report arrives, because a hearer cannot be made into an asker retroactively.",
      "«إِذَا»nın şart fiili olan mâzî — «ق د م»den TEFA''UL vezninde. «Önce geçmiş olmak» esastır: tetikleyici, haber geldiğinde sayfada zaten bulunmalıdır; zira bir muhâtab geriye dönük olarak soran hâline getirilemez."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«تَقَدَّمَ».",
      "A jarr letter attaching to «has gone before».",
      "«تَقَدَّمَ»ye taalluk eden cer harfi."),
  tok("الْكَلَامِ","kalam","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي» — وَالْقَيْدُ مُهِمٌّ: الْإِشَارَةُ تَكُونُ فِي الْكَلَامِ نَفْسِهِ، لَا فِي حَالِ الْمُخَاطَبِ.",
      "Majrur by «fi» — and the restriction matters: the pointer is IN THE SPEECH, not in the hearer's circumstances. The second and third cases will locate their triggers elsewhere, and the three prepositions are how the matn keeps them apart.",
      "«فِي» ile mecrûr — ve kayıt mühimdir: işaret, muhâtabın hâlinde değil KELÂMIN İÇİNDEdir. İkinci ve üçüncü hâller tetikleyicilerini başka yerde bulacaktır; metin üçünü birbirinden bu üç harf-i cerle ayırır."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","fail","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلُ «تَقَدَّمَ».",
      "A relative noun, fixed in form, in the position of RAF' as the fa'il of «has gone before» — indefinite in force («something that…»), which is what lets the rule cover every kind of pointer at once.",
      "Mebnî ism-i mevsûl; «تَقَدَّمَ»nin fâili olarak mahallen MERFÛdur — kuvvet îtibârıyla nekredir («işaret eden bir şey»), ve kâidenin her nevi işareti birden kapsamasını sağlayan budur."),
  tok("يُشِيرُ","ashaara","verb",["jumla-sifa","hollow-verbs","form-iv-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ عَائِدٌ عَلَى «مَا» — أَجْوَفُ وَاوِيٌّ مِنْ «أَشَارَ» عَلَى الْإِفْعَالِ: أَصْلُهُ «يُشْوِرُ»، نُقِلَتْ حَرَكَةُ الْوَاوِ إِلَى السَّاكِنِ قَبْلَهَا ثُمَّ قُلِبَتْ يَاءً لِسُكُونِهَا بَعْدَ كَسْرَةٍ.",
      "A mudari in raf' with a hidden «it» going back to the «ma» — a hollow waw verb of Form IV. Its origin is يُشْوِرُ: the waw's kasra moved back onto the silent letter before it, and the waw itself, now quiescent after a kasra, turned into a ya. Two i'lal steps in one letter, and the clause is the sila with no position in i'rab.",
      "Merfû muzâri; fâili «مَا»ya râci müstetir zamirdir — «أَشَارَ»dan, if'âl vezninde ecvef-i vâvî. Aslı «يُشْوِرُ»dur: vâvın kesrası öncesindeki sâkine nakledilmiş, sonra kesradan sonra sâkin kalan vâv yâya kalbolmuştur. Tek harfte iki i'lâl adımı; ve cümle, i'râbdan mahalli olmayan sıladır."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يُشِيرُ» — وَ«أَشَارَ» يَتَعَدَّى بِإِلَى.",
      "A jarr letter attaching to «points» — أَشَارَ reaches what it points at through an ila, and the paradigm's own preposition is part of knowing the verb.",
      "«يُشِيرُ»a taalluk eden cer harfi — «أَشَارَ» işaret ettiği şeye «إِلَى» ile ulaşır; fiilin kendi harf-i cerri, o fiili bilmenin bir parçasıdır."),
  tok("الْخَبَرِ","khabar","noun",["huruf-jarr","khabar-insha"],
      "مَجْرُورٌ بِـ«إِلَى» — وَالْمِثَالُ الْمَشْهُورُ قَوْلُهُ تَعَالَى: وَلَا تُخَاطِبْنِي فِي الَّذِينَ ظَلَمُوا إِنَّهُمْ مُغْرَقُونَ؛ فَالنَّهْيُ عَنِ الْمُخَاطَبَةِ أَشَارَ إِلَى الْحُكْمِ، فَنُزِّلَ نُوحٌ مَنْزِلَةَ السَّائِلِ وَأُكِّدَ الْخَبَرُ.",
      "Majrur by «ila» — and the famous instance is «and do not address Me concerning those who did wrong: THEY ARE TO BE DROWNED» (al-Muʾminun 23:27). The prohibition itself pointed at the ruling, so Noah — who had asked nothing — was put in the asker's place and the report came emphasised. The surface called for هُمْ مُغْرَقُونَ; the situation called for إِنَّهُمْ.",
      "«إِلَى» ile mecrûr — ve meşhur misâl şu âyettir: «Zulmedenler hakkında bana hitâb etme; ONLAR MUHAKKAK BOĞULACAKLARDIR» (Mü'minûn 23:27). Hitâbdan nehyin kendisi hükme işaret etmiştir; böylece hiçbir şey sormamış olan Nûh aleyhisselâm soranın yerine konmuş ve haber te'kîdli gelmiştir. Muktezâ-yı zâhir «هُمْ مُغْرَقُونَ» idi; muktezâ-yı hâl «إِنَّهُمْ» oldu.",
      punct="."),
 ],
 "jumal": [J("إِذَا تَقَدَّمَ فِي الْكَلَامِ مَا يُشِيرُ إِلَى الْخَبَرِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "A verbal clause, in the position of jarr as what «idha» is annexed to.",
   "«إِذَا»nın kendisine izâfe edilmesiyle mahallen mecrûr fiil cümlesi."),
  J("يُشِيرُ إِلَى الْخَبَرِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "And one who is not denying is put in the place of a denier, when something of the marks of denial has appeared on him.",
 "tr": "İnkâr etmeyen kimse, üzerinde inkâr alâmetlerinden bir şey belirdiğinde, münkirin yerine konur."},
 "tokens": [
  tok("وَيُنَزَّلُ","nazzala","verb",["khilaf-muqtada-al-zahir","naib-al-fail","mafulayn","form-ii-verbs","mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَالْفِعْلُ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالتَّرْكِيبُ نَفْسُهُ ثَلَاثَ مَرَّاتٍ، لِيَقَعَ الْفَرْقُ فِي الْمُنَزَّلِ وَالْمُنَزَّلِ عَلَيْهِ وَحْدَهُمَا.",
      "A joining waw and the same passive verb — the identical frame three times over, so that the difference falls only on WHO is put in WHOSE place. A matn that repeats a construction word for word is telling you to read the substitutions and nothing else.",
      "Atıf vâvı ve aynı meçhûl fiil — üç defa aynı terkîb; böylece fark, yalnız KİMİN KİMİN yerine konduğunda kalır. Bir terkîbi kelimesi kelimesine tekrar eden metin, size yalnız değişenleri okumanızı söylüyordur.",
      segments=[seg("وَ","wa","conj"), seg("يُنَزَّلُ","nazzala","verb")]),
  tok("غَيْرُ","ghayr","noun",["naib-al-fail","idafa-definiteness"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَ«غَيْرُ» مُضَافٌ بِمَعْنَاهُ، لَا يَتِمُّ إِلَّا بِمَا بَعْدَهُ.",
      "The naib al-fa'il in raf' and a mudaf — and «ghayr» is mudaf by its very meaning: it says nothing until the word after it arrives. That is the same fact the Manar's relative-ma rule leans on, and here it is doing the ordinary work of building a phrase.",
      "Merfû nâib-i fâil ve muzâf — ve «غَيْر» mânâsı gereği muzâftır; kendisinden sonraki kelime gelmeden hiçbir şey söylemez. Menâr'ın ism-i mevsûl kâidesinin dayandığı hakikatin aynısı; burada sıradan bir terkîb kurma işini görüyor."),
  tok("الْمُنْكِرِ","munkir","noun",["idafa-definiteness","ism-fail","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «أَنْكَرَ»، وَهُوَ الْمَذْكُورُ فِي الْبَابِ الثَّالِثِ.",
      "The mudaf ilayh in jarr — the ism fa'il of أَنْكَرَ, chapter 3's third hearer. «Not-the-denier» is everyone but him: both the empty-minded man and the hesitating one, gathered by a single negating noun.",
      "Mecrûr muzâfun ileyh — «أَنْكَرَ»nin ism-i fâili; üçüncü bâbın üçüncü muhâtabı. «Münkir olmayan», ondan başka herkestir: hem zihni hâlî olan hem tereddüd eden, tek bir nefiy ismiyle toplanmış."),
  tok("مَنْزِلَةَ","manzila","noun",["khilaf-muqtada-al-zahir","mafulayn","maful-bihi","idafa-definiteness"],
      "الْمَفْعُولُ الثَّانِي مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "The second object, in nasb and a mudaf.",
      "İkinci mef'ûl, mansub ve muzâf."),
  tok("الْمُنْكِرِ","munkir","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَقَدْ تَكَرَّرَتِ الْكَلِمَةُ فِي سَطْرٍ وَاحِدٍ: مَنْفِيَّةً أَوَّلًا وَمُثْبَتَةً ثَانِيًا، وَبَيْنَهُمَا الْحُكْمُ كُلُّهُ.",
      "The mudaf ilayh in jarr — and the word stands TWICE in one line: once negated and once affirmed, with the whole ruling between them. «Not-a-denier is put in a denier's place» is a sentence that cannot be paraphrased shorter, and the repetition is not clumsiness.",
      "Mecrûr muzâfun ileyh — ve kelime tek satırda İKİ defa geçer: önce nefyedilmiş, sonra ispat edilmiş; ikisinin arasında hükmün tamamı vardır. «Münkir olmayan, münkirin yerine konur» cümlesi daha kısa söylenemez ve tekrar bir acemilik değildir."),
  tok("إِذَا","idha","part",["idha-shartiyya"],
      "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ — وَهُوَ التَّرْخِيصُ نَفْسُهُ: لَا تَنْزِيلَ بِغَيْرِ سَبَبٍ.",
      "The same conditional zarf — and the same licence: no substitution without a cause. Three sentences, three إِذَا clauses, and the matn will not state a single one of these permissions bare.",
      "Aynı şart mânâlı zarf — ve aynı ruhsat: sebepsiz tenzîl yoktur. Üç cümle, üç «إِذَا»; ve metin bu izinlerin hiçbirini çıplak bırakmaz."),
  tok("ظَهَرَ","zahara","verb",["idha-shartiyya","fail"],
      "فِعْلٌ مَاضٍ فِعْلُ الشَّرْطِ — وَالظُّهُورُ لَا الْوُجُودُ: يَكْفِي أَنْ يَبْدُوَ عَلَيْهِ، وَلَا يُشْتَرَطُ أَنْ يَكُونَ مُنْكِرًا فِي نَفْسِهِ.",
      "A mazi, the condition's verb — and the verb is APPEARING, not being. It is enough that something should show on him; he is not required to be a denier in himself. The whole discipline turns on what the speaker may reasonably read off the situation, and this verb says so.",
      "Şartın fiili olan mâzî — ve fiil, olmak değil GÖRÜNMEKtir. Üzerinde bir şeyin belirmesi yeter; kendisinde gerçekten münkir olması şart değildir. Bütün ilim, mütekellimin hâlden makul olarak okuyabileceği şey üzerinde döner ve bu fiil bunu söyler."),
  tok("عَلَيْهِ","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ظَهَرَ»، وَقَدْ قُدِّمَ عَلَى الْفَاعِلِ — وَالتَّقْدِيمُ لِلِاهْتِمَامِ.",
      "A jarr-majrur attaching to «appeared», and PUT BEFORE the fa'il — the fronting is for attention: on HIM, not somewhere in the air. The trigger of the first case was in the speech; this one is on the man.",
      "«ظَهَرَ»ye taalluk eden câr-mecrûr; fâilin ÖNÜNE geçmiştir — takdîm ihtimâm içindir: havada bir yerde değil, ONUN ÜZERİNDE. Birinci hâlin tetikleyicisi kelâmdaydı; bunun ki adamın üzerindedir.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هِ","pron-3ms","pron")]),
  tok("شَيْءٌ","shay","noun",["fail"],
      "فَاعِلُ «ظَهَرَ» مَرْفُوعٌ مُنَوَّنٌ — وَتَنْكِيرُهُ لِلتَّقْلِيلِ: أَدْنَى شَيْءٍ يَكْفِي.",
      "The fa'il of «appeared», in raf' with its tanwin — and the indefinite is for SMALLNESS here: the least thing is enough. Compare chapter 3's «one emphasiser» and chapter 16 of the Manar's «any excuse whatsoever» — the same tanwin doing a third job, and only the context says which.",
      "Tenvinli merfû fâil — ve buradaki nekre AZLIK içindir: en ufak şey yeter. Üçüncü bâbdaki «bir te'kîd» ile Menâr'ın on altıncı bâbındaki «herhangi bir özür» ile karşılaştırın: aynı tenvin üçüncü bir işi görüyor ve hangisi olduğunu yalnız siyâk söyler."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلتَّبْعِيضِ أَوْ لِلْبَيَانِ، مُتَعَلِّقٌ بِمَحْذُوفٍ صِفَةٍ لِـ«شَيْءٌ».",
      "A jarr letter of partition or of specification, attaching to an unsaid word describing «something» — «something OF the marks». A jarr phrase describing an indefinite is that indefinite's na't in position, and nothing is written to carry it.",
      "Teb'îz yahut beyân için cer harfi; «شَيْءٌ»un sıfatı olan mahzûfa taalluk eder — «alâmetlerDEN bir şey». Nekreyi niteleyen câr-mecrûr, mahallen o nekrenin na'tıdır ve onu taşıyacak hiçbir şey yazılmamıştır."),
  tok("أَمَارَاتِ","amara","noun",["idafa-definiteness","jam-muannath-salim"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ لِـ«أَمَارَةٍ»، وَهِيَ الْعَلَامَةُ.",
      "Majrur by the kasra and a mudaf — a sound feminine plural of أَمَارَة, a SIGN. The word is chosen against عَلَامَة: an amara is what lets you infer, not what states. The speaker is reading evidence, not being told.",
      "Kesra ile mecrûr ve muzâf — «أَمَارَة»in cem'-i müennes sâlimi; alâmet demektir. Kelime «عَلَامَة»e karşı seçilmiştir: emâre, çıkarım yaptıran şeydir, bildiren şey değil. Mütekellim delil okuyor, kendisine haber verilmiyor."),
  tok("الْإِنْكَارِ","inkar","noun",["idafa-definiteness","masdar","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْمِثَالُ الْمَشْهُورُ بَيْتُ الْحَجْلِ: جَاءَ شَقِيقٌ عَارِضًا رُمْحَهُ، إِنَّ بَنِي عَمِّكَ فِيهِمْ رِمَاحٌ؛ فَحَمْلُهُ الرُّمْحَ عَارِضًا أَمَارَةٌ، فَأُكِّدَ الْخَبَرُ وَلَمْ يَكُنْ مُنْكِرًا.",
      "The mudaf ilayh in jarr — and the famous instance is the verse of Ḥajl: «Shaqiq came holding his spear sideways — YOUR uncle's sons have spears among them too». Carrying the spear crosswise, as though the other side had none, was the mark; so the report was emphasised although the man had denied nothing aloud. The surface called for بَنُو عَمِّكَ; the situation called for إِنَّ.",
      "Mecrûr muzâfun ileyh — ve meşhur misâl Hacl'in beytidir: «Şakîk mızrağını yan tutarak geldi — SENİN amcanın oğullarında da mızraklar vardır». Mızrağı, karşı tarafta yokmuş gibi çapraz taşıması emâredir; bu yüzden adam ağzıyla hiçbir şeyi inkâr etmemişken haber te'kîdli gelmiştir. Muktezâ-yı zâhir «بَنُو عَمِّكَ» idi; muktezâ-yı hâl «إِنَّ» oldu.",
      punct="."),
 ],
 "jumal": [J("إِذَا ظَهَرَ عَلَيْهِ شَيْءٌ مِنْ أَمَارَاتِ الْإِنْكَارِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "A verbal clause, in the position of jarr as what «idha» is annexed to.",
   "«إِذَا»nın kendisine izâfe edilmesiyle mahallen mecrûr fiil cümlesi.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "And a denier is put in the place of one who is not denying, when he has with him something which, if he considered it, he would desist.",
 "tr": "Münkir olan kimse, yanında — düşündüğü takdirde inkârından döneceği — bir şey bulunduğunda, münkir olmayanın yerine konur."},
 "tokens": [
  tok("وَيُنَزَّلُ","nazzala","verb",["khilaf-muqtada-al-zahir","naib-al-fail","mafulayn","form-ii-verbs","mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَالْفِعْلُ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَهَذَا التَّنْزِيلُ عَكْسُ الَّذِي قَبْلَهُ.",
      "A joining waw and the same passive verb — and this substitution runs the OTHER way. The first two took a weaker hearer and treated him as stronger; this one takes the strongest and treats him as though he had no objection at all.",
      "Atıf vâvı ve aynı meçhûl fiil — ve bu tenzîl, öncekinin TERSİ yöndedir. İlk ikisi daha zayıf bir muhâtabı daha güçlü sayıyordu; bu ise en güçlüsünü alıp hiç itirazı yokmuş gibi muâmele ediyor.",
      segments=[seg("وَ","wa","conj"), seg("يُنَزَّلُ","nazzala","verb")]),
  tok("الْمُنْكِرُ","munkir","noun",["naib-al-fail","ism-fail","form-iv-verbs"],
      "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — وَقَدْ كَانَ مُضَافًا إِلَيْهِ مَجْرُورًا مَرَّتَيْنِ فِي الْجُمْلَةِ السَّابِقَةِ، فَصَارَ هُنَا نَائِبَ الْفَاعِلِ مَرْفُوعًا.",
      "The naib al-fa'il in raf' — and this word was a mudaf ilayh in jarr TWICE in the sentence before. Same word, three appearances, two cases, in two consecutive lines: the matn moves a term through its i'rab as it goes, which is the cheapest teaching there is.",
      "Merfû nâib-i fâil — ve bu kelime bir önceki cümlede İKİ defa mecrûr muzâfun ileyhti. Aynı kelime, üç geçiş, iki hâl, iki ardışık satırda: metin, ilerledikçe bir terimi i'râbından geçirir; bu, öğretmenin en ucuz yoludur."),
  tok("مَنْزِلَةَ","manzila","noun",["khilaf-muqtada-al-zahir","mafulayn","maful-bihi","idafa-definiteness"],
      "الْمَفْعُولُ الثَّانِي مَنْصُوبٌ وَهُوَ مُضَافٌ — ثَالِثُ مَرَّةٍ فِي ثَلَاثِ جُمَلٍ، وَفَتْحَتُهُ ثَابِتَةٌ فِي الثَّلَاثِ.",
      "The second object, in nasb and a mudaf — the third time in three sentences, and its fatha stands in all three. A rule seen once is a fact; seen three times in one frame it is a habit the reader can carry to a text nobody has annotated.",
      "İkinci mef'ûl, mansub ve muzâf — üç cümlede üçüncü defa; ve fethası üçünde de durur. Bir kere görülen kâide bir bilgidir; tek kalıpta üç kere görülen, okuyucunun hiç şerh edilmemiş bir metne taşıyabileceği bir alışkanlıktır."),
  tok("غَيْرِ","ghayr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — وَ«غَيْرُ» فِي هَذَا الْبَابِ مَرَّتَانِ: مَرْفُوعَةً نَائِبَ فَاعِلٍ وَمَجْرُورَةً مُضَافًا إِلَيْهِ.",
      "The mudaf ilayh in jarr and itself a mudaf — «ghayr» stands twice in this chapter, once in raf' as a deputy subject and once in jarr as a mudaf ilayh. A word that is annexed by its very meaning still takes whatever case its own position gives it.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — «غَيْر» bu bâbda iki defa geçer: bir kere merfû nâib-i fâil, bir kere mecrûr muzâfun ileyh. Mânâsı gereği muzâf olan bir kelime, yine de kendi mevkiinin verdiği hâli alır."),
  tok("الْمُنْكِرِ","munkir","noun",["idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ تَمَّتِ الْأَحْوَالُ الثَّلَاثَةُ.",
      "The mudaf ilayh in jarr — and with it the three cases are complete.",
      "Mecrûr muzâfun ileyh — ve onunla üç hâl tamamlanır."),
  tok("إِذَا","idha","part",["idha-shartiyya"],
      "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ — وَالثَّالِثُ فِي ثَلَاثِ جُمَلٍ.",
      "The same conditional zarf, the third in three sentences.",
      "Aynı şart mânâlı zarf; üç cümlede üçüncüsü."),
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","idha-shartiyya","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ — وَخَبَرُهُ مُقَدَّمٌ وَاسْمُهُ مُؤَخَّرٌ، وَذَلِكَ لِأَنَّ الِاسْمَ مَوْصُولٌ طَالَتْ صِلَتُهُ.",
      "An incomplete mazi, the condition's verb — with its khabar FIRST and its ism LAST, because the ism is a relative whose sila runs on for four more words. Arabic front-loads the short half; a heavy subject waits.",
      "Şartın fiili olan nâkıs mâzî — haberi ÖNDE, ismi SONDA; zira ismi, sılası dört kelime daha süren bir mevsûldür. Arapça kısa yarıyı öne alır; ağır olan özne bekler."),
  tok("مَعَهُ","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَهُوَ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ» مُقَدَّمٌ.",
      "A zarf in nasb and a mudaf, the ha annexed to it — standing in the POSITION OF NASB as the FRONTED khabar of «kana». And note the third trigger's location: the first was in the speech, the second on the man, this one WITH him. Three prepositions, three places a speaker may look.",
      "Mansub zarf ve muzâf; hâ muzâfun ileyhtir — «كَانَ»nin MUKADDEM haberi olarak mahallen MANSUBdur. Ve üçüncü tetikleyicinin yerine dikkat: birincisi kelâmda, ikincisi adamın üzerinde, bu ise YANINDA. Üç harf, mütekellimin bakabileceği üç yer.",
      segments=[seg("مَعَ","maa","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","kana-wa-akhawatuha","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ «كَانَ» مُؤَخَّرٌ.",
      "A relative noun, fixed in form, in the position of RAF' as the DELAYED ism of «kana» — «there is with him THAT WHICH…». Everything after it is its sila, and the sila is a whole conditional sentence, which is the hardest structure in the chapter.",
      "Mebnî ism-i mevsûl; «كَانَ»nin MUAHHAR ismi olarak mahallen MERFÛdur — «yanında ŞU ŞEY vardır ki…». Ondan sonraki her şey sılasıdır ve sıla, bütün bir şart cümlesidir; bâbın en zor yapısı budur."),
  tok("إِنْ","in-shartiyya","part",["in-shartiyya"],
      "حَرْفُ شَرْطٍ جَازِمٌ — وَجُمْلَةُ الشَّرْطِ وَجَوَابُهُ كِلْتَاهُمَا دَاخِلَتَانِ فِي صِلَةِ «مَا».",
      "A conditional LETTER that governs jazm — and the condition together with its answer is INSIDE the sila of «ma». A relative clause containing a full conditional sentence is the sort of nesting a reader has to hold two levels of at once, and it is exactly what the matn needed: the thing he has is not simply a proof, it is a proof-if-examined.",
      "Cezmeden şart HARFİ — ve şart cümlesi ile cevâbı, ikisi birden «مَا»nın SILASININ İÇİNDEdir. Tam bir şart cümlesi barındıran bir sıla, okuyucunun iki seviyeyi birden tutmasını ister; ve metnin ihtiyacı tam da buydu: adamın yanındaki şey sadece bir delil değil, DÜŞÜNÜLDÜĞÜ TAKDİRDE delildir."),
  tok("تَأَمَّلَهُ","taammala","verb",["in-shartiyya","form-v-verbs","maful-bihi"],
      "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ عَائِدٌ عَلَى «مَا» — وَهُوَ الْعَائِدُ. عَلَى تَفَعَّلَ مِنْ «أ م ل»، وَبِنَاءُ التَّفَعُّلِ لِلتَّكَلُّفِ: النَّظَرُ مَرَّةً بَعْدَ مَرَّةٍ.",
      "A mazi in the POSITION of jazm as the condition's verb, and the ha is an attached pronoun in the position of nasb as its maf'ul bihi, returning to the «ma» — that pronoun is the ʿaid. On تَفَعَّلَ from أ م ل, and Form V here carries EFFORT: looking again and again. Not «if he sees it» but «if he works at it», which is why the man may still be denying in good faith.",
      "Şartın fiili olarak MAHALLEN MECZÛM mâzî; hâ ise «مَا»ya râci, mef'ûlün bih olarak mahallen mansub muttasıl zamirdir — ÂİD odur. «أ م ل»den TEFA''UL vezninde; ve tefe''ul burada TEKELLÜF ifade eder: tekrar tekrar bakmak. «Görürse» değil «üzerinde çalışırsa»; adamın hâlâ iyi niyetle inkâr ediyor olabilmesinin sebebi budur.",
      segments=[seg("تَأَمَّلَ","taammala","verb"), seg("هُ","pron-3ms","pron")]),
  tok("ارْتَدَعَ","irtadaa","verb",["in-shartiyya","form-viii-verbs"],
      "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَفَاعِلُهُ مُسْتَتِرٌ — عَلَى اِفْتَعَلَ مِنْ «ر د ع»، وَلَمْ تُبْدَلْ تَاؤُهُ لِأَنَّ الرَّاءَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ. وَجُمْلَةُ الشَّرْطِ كُلُّهَا صِلَةٌ لَا مَحَلَّ لَهَا.",
      "A mazi in the position of jazm as the ANSWER to the condition, its fa'il hidden — on اِفْتَعَلَ from ر د ع, and its ta is unchanged because the ra is not one of the letters that colour it. The whole conditional sentence is the sila and has no position in i'rab, while its two halves each have one: three levels of clause on one line.",
      "Şartın CEVÂBI olarak mahallen meczûm mâzî; fâili müstetirdir — «ر د ع»den İFTİÂL vezninde; tâsı değişmemiştir, zira râ ibdâl harflerinden değildir. Şart cümlesinin tamamı sıladır ve mahalli yoktur; iki yarısının ise her birinin mahalli vardır: tek satırda üç seviye cümle.",
      punct="."),
 ],
 "jumal": [J("إِنْ تَأَمَّلَهُ ارْتَدَعَ",
   "جُمْلَةٌ شَرْطِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A conditional sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan şart cümlesi — mahalsizdir."),
  J("كَانَ مَعَهُ مَا إِنْ تَأَمَّلَهُ ارْتَدَعَ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "A verbal clause, in the position of jarr as what «idha» is annexed to.",
   "«إِذَا»nın kendisine izâfe edilmesiyle mahallen mecrûr fiil cümlesi.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "And the considerations of negated speech are like the considerations of affirmed speech.",
 "tr": "Menfî kelâmın itibarları, müsbet kelâmın itibarları gibidir."},
 "tokens": [
  tok("وَاعْتِبَارَاتُ","itibar","noun",["mubtada-khabar","jam-muannath-salim","idafa-definiteness","form-viii-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«اعْتِبَارَاتُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ لِمَصْدَرِ «اِعْتَبَرَ» عَلَى الِافْتِعَالِ.",
      "A resuming waw, and «the considerations of» is the mubtada in raf' and a mudaf — a sound feminine plural of the Form VIII masdar of اِعْتَبَرَ. A masdar pluralised names the SEVERAL WAYS a thing may be regarded, which is exactly what this sentence claims transfers.",
      "İsti'nâf vâvı; «اعْتِبَارَاتُ» merfû mübtedâ ve muzâftır — «اِعْتَبَرَ»nin iftiâl masdarının cem'-i müennes sâlimi. Cemilenmiş bir masdar, bir şeyin İTİBAR EDİLEBİLECEĞİ ÇEŞİTLİ VECİHLERİ adlandırır; bu cümlenin intikal ettiğini iddia ettiği şey de tam budur.",
      segments=[seg("وَ","wa","conj"), seg("اعْتِبَارَاتُ","itibar","noun")]),
  tok("الْكَلَامِ","kalam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyh."),
  tok("الْمَنْفِيِّ","manfi","noun",["naat-sifa","ism-maful","naqis-verbs"],
      "نَعْتٌ لِـ«الْكَلَامِ» مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ «نَفَى» النَّاقِصِ: أَصْلُهُ «مَنْفُويٌ»، اجْتَمَعَتِ الْوَاوُ وَالْيَاءُ وَسَبَقَتْ إِحْدَاهُمَا بِالسُّكُونِ فَقُلِبَتِ الْوَاوُ يَاءً وَأُدْغِمَتْ، ثُمَّ كُسِرَتِ الْفَاءُ لِتَصِحَّ الْيَاءُ.",
      "A na't of «speech», in jarr — the ism maf'ul of the DEFECTIVE verb نَفَى. Its origin is مَنْفُويٌ: waw and ya met with the first quiescent, so the waw turned ya and the two merged, and then the letter before them took a kasra so the ya could stand. Three i'lal steps, and the app's own engine derives every one of them from the bare pattern — the same chain that produces مَرْمِيّ.",
      "«الْكَلَام»in na'tı, mecrûr — NÂKIS «نَفَى»nin ism-i mef'ûlü. Aslı «مَنْفُويٌ»dur: vâv ile yâ birleşmiş, biri sâkin olduğu için vâv yâya kalbolup idgâm edilmiş, sonra yâ sahîh kalsın diye öncesi kesralanmıştır. Üç i'lâl adımı; ve uygulamanın kendi motoru bunların hepsini çıplak vezinden türetir — «مَرْمِيّ»i üreten zincirin aynısı."),
  tok("كَاعْتِبَارَاتِ","itibar","noun",["huruf-jarr","tashbih","idafa-definiteness"],
      "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ«اعْتِبَارَاتِ» مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "The kaf is a jarr letter of LIKENING, and «the considerations of» is majrur by the kasra and a mudaf — the whole phrase standing in the position of raf' as the khabar. Two identical plurals in one sentence, one in raf' and one in jarr, and the kaf between them: the sentence is its own demonstration of what a comparison looks like.",
      "Kâf, TEŞBÎH için cer harfidir; «اعْتِبَارَاتِ» kesra ile mecrûr ve muzâftır — ve câr-mecrûrun tamamı, haber olarak mahallen merfûdur. Tek cümlede aynı cemi iki defa, biri ref'de biri cerde, aralarında kâf: cümle, bir teşbîhin nasıl göründüğünün kendi gösterimidir.",
      segments=[seg("كَـ","ka","prep"), seg("اعْتِبَارَاتِ","itibar","noun")]),
  tok("الْمُثْبَتِ","muthbat","noun",["idafa-definiteness","ism-maful","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ «أَثْبَتَ» عَلَى مُفْعَلٍ، وَجَذْرُهُ «ث ب ت» الَّذِي بُنِيَتْ عَلَيْهِ دَلَالَةُ الْبَابِ السَّابِعِ فِي الْمَنَارِ. وَالْمَعْنَى: مَا زَيْدٌ قَائِمًا لِخَالِي الذِّهْنِ، وَمَا زَيْدٌ بِقَائِمٍ لِلْمُتَرَدِّدِ، وَوَاللهِ مَا زَيْدٌ بِقَائِمٍ لِلْمُنْكِرِ.",
      "The mudaf ilayh in jarr — the ism maf'ul of أَثْبَتَ on مُفْعَل, from the root ث ب ت that carried Mukhtasar al-Manar's definition of dalala. And the claim is worked out exactly as the affirmative was: مَا زَيْدٌ قَائِمًا for the empty mind, مَا زَيْدٌ بِقَائِمٍ for the hesitant, وَاللهِ مَا زَيْدٌ بِقَائِمٍ for the denier. The zaid ba is the negative sentence's own emphasiser, and it does the work إِنَّ did in the affirmative.",
      "Mecrûr muzâfun ileyh — «أَثْبَتَ»nin MUF'AL vezninde ism-i mef'ûlü; Muhtasaru'l-Menâr'ın delâlet tarifini taşıyan «ث ب ت» kökünden. Ve iddia, müsbette olduğu gibi işletilir: zihni hâlî olana «مَا زَيْدٌ قَائِمًا», tereddüd edene «مَا زَيْدٌ بِقَائِمٍ», münkire «وَاللهِ مَا زَيْدٌ بِقَائِمٍ». Zâid bâ, menfî cümlenin kendi te'kîd aracıdır ve müsbette «إِنَّ»nin gördüğü işi görür.",
      punct="."),
 ],
 "jumal": [J("وَاعْتِبَارَاتُ الْكَلَامِ الْمَنْفِيِّ كَاعْتِبَارَاتِ الْمُثْبَتِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A resumed nominal sentence, with no position in i'rab.",
   "İsti'nâfî isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "Then predication is of two kinds: an intellectual truth, and an intellectual figure.",
 "tr": "Sonra isnâd iki kısımdır: hakîkat-i akliyye ve mecâz-ı aklî."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَبِهِ يُنْتَقَلُ مِنْ أَحْوَالِ الْمُخَاطَبِ إِلَى نَفْسِ الْإِسْنَادِ.",
      "A letter of atf giving sequence with an interval — and with it the book turns from the states of the HEARER to the predication ITSELF. Four chapters have been about who is being spoken to; from here the question is what a sentence claims and whether the claim is literal.",
      "Terâhî ile tertîb için atıf harfi — ve onunla kitap, MUHÂTABIN hâllerinden İSNÂDIN kendisine geçer. Dört bâb kime söylendiği üzerineydi; buradan itibaren mesele, cümlenin ne iddia ettiği ve bu iddianın hakîkî olup olmadığıdır."),
  tok("الْإِسْنَادُ","isnad","noun",["mubtada-khabar","masdar","form-iv-verbs"],
      "مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «أَسْنَدَ» عَلَى إِفْعَالٍ، وَهُوَ نِسْبَةُ أَحَدِ الطَّرَفَيْنِ إِلَى الْآخَرِ.",
      "The mubtada in raf' — the Form IV masdar of أَسْنَدَ, «to lean one thing on another», and that is exactly what a sentence does: it leans a predicate against a subject. The term names the ACT of predicating, not either of the two things predicated.",
      "Merfû mübtedâ — «أَسْنَدَ»nin İF'ÂL vezninde masdarı: bir şeyi bir şeye dayamak; ve bir cümlenin yaptığı tam olarak budur — müsnedi müsnedün ileyhe dayar. Terim, dayanan iki şeyi değil, DAYAMA fiilini adlandırır."),
  tok("ضَرْبَانِ","darb","noun",["mubtada-khabar","al-muthanna"],
      "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى — وَهُوَ التَّرْكِيبُ نَفْسُهُ الَّذِي خُتِمَ بِهِ الْبَابُ الْأَوَّلُ: التَّعْقِيدُ ضَرْبَانِ.",
      "The khabar in raf', its sign the ALIF because it is a dual — and it is the very construction chapter 1 closed on: «obscurity is of two kinds». The book divides in twos and says so the same way each time, which is what makes a matn memorable rather than merely short.",
      "Merfû haber; ref' alâmeti, tesniye olduğu için ELİFtir — ve birinci bâbın kendisiyle kapandığı terkîbin ta kendisi: «التَّعْقِيدُ ضَرْبَانِ». Kitap ikişer ikişer taksîm eder ve her defasında aynı şekilde söyler; bir metni yalnız kısa değil EZBERLENEBİLİR yapan şey budur.",
      punct="："),
  tok("حَقِيقَةٌ","haqiqa","noun",["badal"],
      "بَدَلٌ مِنْ «ضَرْبَانِ» مَرْفُوعٌ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — وَالْحَقِيقَةُ الْعَقْلِيَّةُ إِسْنَادُ الْفِعْلِ إِلَى مَا هُوَ لَهُ عِنْدَ الْمُتَكَلِّمِ.",
      "A badal of «two kinds», in raf', or the khabar of an unspoken mubtada — and an intellectual TRUTH is attributing the act to the one it really belongs to, in the speaker's own belief. The word stood in Mukhtasar al-Manar for the literal sense of a WORD; here it is the literal sense of an ATTRIBUTION, which is a different question about the same sentence.",
      "«ضَرْبَانِ»den merfû bedel, yahut mahzûf bir mübtedânın haberi — ve hakîkat-i akliyye, fiili, mütekellimin kendi inancında ona gerçekten âit olana isnâd etmektir. Kelime Muhtasaru'l-Menâr'da bir KELİMENİN hakîkî mânâsı için duruyordu; burada bir İSNÂDIN hakîkîliğidir — aynı cümle hakkında başka bir soru."),
  tok("عَقْلِيَّةٌ","aqli","noun",["naat-sifa"],
      "نَعْتٌ لِـ«حَقِيقَةٌ» مَرْفُوعٌ — اسْمٌ مَنْسُوبٌ إِلَى الْعَقْلِ، وَالتَّاءُ لِلتَّأْنِيثِ مُطَابَقَةً لِمَنْعُوتِهَا.",
      "A na't of «truth», in raf' — a nisba noun on عَقْل with the ta of the feminine, agreeing with what it describes. It is called INTELLECTUAL because the judgement is made by the mind about the attribution, not by the ear about the word.",
      "«حَقِيقَةٌ»un na'tı, merfû — «عَقْل»a nisbet edilmiş isim; tâ, men'ûtuna mutâbakat için müennesliktir. AKLÎ denmesinin sebebi, hükmün kelime hakkında kulakla değil, isnâd hakkında akılla verilmesidir."),
  tok("وَمَجَازٌ","majaz","noun",["atf-nasaq","anwa-al-majaz"],
      "مَعْطُوفٌ مَرْفُوعٌ — وَالْمَجَازُ الْعَقْلِيُّ إِسْنَادُ الْفِعْلِ إِلَى غَيْرِ مَا هُوَ لَهُ لِعَلَاقَةٍ مَعَ قَرِينَةٍ، كَقَوْلِهِمْ: أَنْبَتَ الرَّبِيعُ الْبَقْلَ — وَكُلُّ كَلِمَةٍ فِيهِ حَقِيقَةٌ، وَإِنَّمَا نُقِلَتِ النِّسْبَةُ.",
      "Joined, in raf' — an intellectual FIGURE is attributing the act to something other than its true owner, for a relation and with a signal: «the spring made the herbage grow». Every single word there is literal; what has moved is the ATTRIBUTION. That is what makes this a different kind of majaz from the one the reader already knows, and the app's own note on it has been waiting for a story to anchor it.",
      "Ma'tûf, merfû — mecâz-ı aklî, fiili, bir alâka ve karîne ile hakîkî sahibinden başkasına isnâd etmektir: «bahar bitkiyi bitirdi». Oradaki her kelime hakîkîdir; yer değiştiren şey İSNÂDdır. Bunu okuyucunun bildiği mecâzdan başka bir nevi yapan şey budur; ve uygulamanın bu mevzudaki notu, kendisini bağlayacak bir hikâye beklemekteydi.",
      segments=[seg("وَ","wa","conj"), seg("مَجَازٌ","majaz","noun")]),
  tok("عَقْلِيٌّ","aqli","noun",["naat-sifa"],
      "نَعْتٌ لِـ«مَجَازٌ» مَرْفُوعٌ — بِلَا تَاءٍ، مُطَابَقَةً لِمَنْعُوتِهِ الْمُذَكَّرِ؛ وَالنِّسْبَتَانِ فِي سَطْرٍ وَاحِدٍ تُرِيَانِ الْمُطَابَقَةَ فِي التَّذْكِيرِ وَالتَّأْنِيثِ.",
      "A na't of «figure», in raf' — WITHOUT the ta, agreeing with its masculine head. The two nisbas stand four words apart, one feminine and one masculine, and between them they show the whole of adjectival agreement without a word of explanation. The chapter ends by opening the next one.",
      "«مَجَازٌ»un na'tı, merfû — tâsız; müzekker men'ûtuna mutâbakat içindir. İki nisbet, dört kelime arayla, biri müennes biri müzekker; ikisi birden sıfat mutâbakatının tamamını tek kelime izah etmeden gösterir. Bâb, bir sonrakini açarak biter.",
      punct="."),
 ],
 "jumal": [J("ثُمَّ الْإِسْنَادُ ضَرْبَانِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

GLOSS_ADD = {
 "idha":     g("إِذَا", None, "part", "when, if (a conditional zarf; it does NOT govern jazm)", "-dığı zaman, eğer (şart zarfı; cezmetmez)", 2),
 "nazzala":  g("نَزَّلَ", "ن ز ل", "verb", "to put down, to place (someone) in a position", "indirmek; (birini) bir yere koymak", 4, form="II"),
 "manzila":  g("مَنْزِلَة", "ن ز ل", "noun", "place, standing, station", "menzile, mertebe", 3),
 "sail":     g("سَائِل", "س أ ل", "noun", "one who asks (ism fa'il)", "soran, sâil (ism-i fâil)", 2),
 "taqaddama": g("تَقَدَّمَ", "ق د م", "verb", "to go before, to precede", "önce geçmek, takaddüm etmek", 3, form="V"),
 "ashaara":  g("أَشَارَ", "ش و ر", "verb", "to point to, to indicate (with إِلَى)", "işaret etmek (إِلَى ile)", 3, form="IV"),
 "amara":    g("أَمَارَة", "أ م ر", "noun", "a mark one infers from, a token", "emâre; çıkarım yaptıran alâmet", 4, plural="أَمَارَات"),
 "taammala": g("تَأَمَّلَ", "أ م ل", "verb", "to consider closely, to ponder", "teemmül etmek, iyice düşünmek", 4, form="V"),
 "irtadaa":  g("اِرْتَدَعَ", "ر د ع", "verb", "to desist, to be checked", "vazgeçmek, geri durmak", 4, form="VIII"),
 "shay":     g("شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "zahara":   g("ظَهَرَ", "ظ ه ر", "verb", "to appear, to become visible", "zâhir olmak, görünmek", 2, form="I"),
 "itibar":   g("اعْتِبَار", "ع ب ر", "noun", "a way of regarding a thing (masdar, Form VIII)", "itibar; bir şeye bakış vechi (masdar, iftiâl)", 4, plural="اعْتِبَارَات"),
 "manfi":    g("مَنْفِيّ", "ن ف ي", "noun", "negated (ism maf'ul of a naqis)", "menfî; nefyedilmiş (nâkıstan ism-i mef'ûl)", 4),
 "muthbat":  g("مُثْبَت", "ث ب ت", "noun", "affirmed (ism maf'ul, Form IV)", "müsbet; ispat edilmiş (ism-i mef'ûl, if'âl)", 4),
 "isnad":    g("إِسْنَاد", "س ن د", "noun", "predication — leaning one term on another (masdar, Form IV)", "isnâd; bir tarafı ötekine dayama (masdar, if'âl)", 5),
 "aqli":     g("عَقْلِيّ", "ع ق ل", "noun", "intellectual, of the mind (nisba)", "aklî (nisbet)", 3),
 "ka":       g("كَـ", None, "prep", "like, as (the kaf of likening)", "gibi (teşbîh kâfı)", 1),
 "ghayr":    g("غَيْر", "غ ي ر", "noun", "other than; not (a noun that is mudaf by its meaning)", "gayr; başkası (mânâsı gereği muzâf isim)", 2),
 "haqiqa":   g("حَقِيقَة", "ح ق ق", "noun", "truth; the literal sense", "hakîkat; hakîkî mânâ", 3),
 "majaz":    g("مَجَاز", "ج و ز", "noun", "a figure; a transferred sense", "mecâz", 3),
 "thumma":   g("ثُمَّ", None, "conj", "then (sequence with an interval)", "sonra (terâhî ile tertîb)", 1),
}

def build_morph():
    out = {}
    # COPIED after a lemma-identity assert — a lex key is global.
    for pkg, lex in [("wasiyyat-abi-hanifa-samti", "taqaddama"),
                     ("aqaid-ahl-al-sunna", "zahara")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))
        assert g_["entries"][lex]["lemma"] == GLOSS_ADD[lex]["lemma"], lex
        out[lex] = m["verbs"][lex]
    # نَزَّلَ — Form II sound, with the majhul the chapter uses three times.
    out["nazzala"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "نَزَّل", "نَزِّل", "نَزِّل",
                                 "تَنْزِيل", "مُنَزِّل", maful="مُنَزَّل",
                                 pmz="نُزِّلَ", pmd="يُنَزَّلُ",
                                 note="مَجْهُولُ الْمُضَارِعِ: ضَمُّ الْأَوَّلِ وَفَتْحُ مَا قَبْلَ الْآخِرِ — يُنَزَّلُ.")
    # أَشَارَ — Form IV of an AJWAF wawi. أَصْلُهُ يُشْوِرُ: naql then qalb.
    # NOTE the key: `ashara` already belongs to عَاشَرَ in another package, and a
    # lex key is GLOBAL. Doubling the alif follows the جَازَ/جَزَى precedent.
    out["ashaara"] = _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ وَاوِيٌّ", _sg.W4, "ُ",
                                        "أَشَار", "أَشَر", "شِير", "شِر", "أَشِير", "أَشِر",
                                        "إِشَارَة", "مُشِير", maful="مُشَار",
                                        pmz="أُشِيرَ", pmd="يُشَارُ",
                                        note="أَجْوَفُ وَاوِيٌّ مِنَ الْإِفْعَالِ: يُشْوِرُ ← نُقِلَتِ الْكَسْرَةُ ثُمَّ قُلِبَتِ الْوَاوُ يَاءً.")
    # تَأَمَّلَ — Form V; its first radical is a HAMZA, so the reader's own
    # conjugator refuses the root and the audit skips it. That refusal is
    # doctrine, not a gap: seat orthography is not derivable.
    out["taammala"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَأَمَّل", "تَأَمَّل", "تَأَمَّل",
                                  "تَأَمُّل", "مُتَأَمِّل", maful="مُتَأَمَّل")
    # اِرْتَدَعَ — Form VIII sound; the ta is unchanged because ر is not one of
    # the letters that colour it.
    out["irtadaa"] = _sg.derived(_sg.B8, _sg.W8, "َ", "اِرْتَدَع", "رْتَدِع", "اِرْتَدِع",
                                 "اِرْتِدَاع", "مُرْتَدِع",
                                 note="لَمْ تُبْدَلْ تَاءُ الِافْتِعَالِ لِأَنَّ الرَّاءَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/4.json").write_text(
    json.dumps({"chapter": 4, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 4 for c in man["chapters"]):
    man["chapters"].append({"n": 4, "title": TITLE4})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.4.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch4:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
