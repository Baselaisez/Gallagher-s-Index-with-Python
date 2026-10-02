# -*- coding: utf-8 -*-
"""Author chapter 12 of mukhtasar-al-manar — ABROGATION.

Chapter 5 named النَّسْخ once, in passing, to define the muhkam as the wording
that cannot take it. Seven chapters later the matn comes back and says what
abrogation IS — and the Hanafi definition is a careful one, chosen against a
rival: نسخ is the SHOWING that a ruling's term has run out, not the LIFTING of
a ruling that was going to last.

ATTRIBUTION: like chapters 2–11, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • بَيَانُ انْتِهَاءِ مُدَّةِ الْحُكْمِ الشَّرْعِيِّ — an idafa chain FIVE members long
    with a na't hanging off the last, the longest in the package.
  • يَجْرِي — a NAQIS verb in raf': the damma cannot sit on the ya, so it is
    UNDERSTOOD. The manqus noun's rule, on a verb.
  • لِأَنَّهُ — the lam of reason over إِنَّ's sister, with the pronoun clinging to
    it as its ISM in the position of nasb. It stands three times here.
  • لَا يَحْتَمِلُ — chapter 5's own verb returning to close its own loop: the
    muhkam was defined as what does not admit abrogation, and here abrogation
    is said not to reach the muhkam. The two sentences are one fact.
  • نَسْخُ الْكِتَابِ بِالْكِتَابِ — a masdar governing, twice over, in a chiasmus.
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

TITLE12 = {"ar": "النَّسْخ", "en": "Abrogation", "tr": "Nesih"}

# لِأَنَّ + a clinging pronoun stands three times in this chapter, so its i'rab
# is written once and used where the matn repeats it.
LIANNA = ("اللَّامُ لِلتَّعْلِيلِ، وَ«أَنَّ» حَرْفٌ مِنْ أَخَوَاتِ «إِنَّ» يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.",
 "The LAM gives the reason, «anna» is one of inna's sisters — it puts its noun into NASB and its khabar into raf' — and the HA clinging to it is that noun, in the POSITION of nasb. One written word, three things in i'rab.",
 "LÂM ta'lîl içindir; «أَنَّ» inne'nin kardeşlerinden bir harftir — ismini nasb, haberini ref eder — ve ona bitişen HÂ o ismidir, mahallen mansubdur. Yazıda tek kelime, i'râbda üç şey.")

S.append({"id": "s1", "translation": {
 "en": "Then abrogation, with us, is the showing that the term of a legal ruling has run out — not the lifting of it.",
 "tr": "Nesih, bize göre şer'î hükmün müddetinin bittiğinin beyânıdır; onun kaldırılması değil."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.",
      "A letter of atf giving sequence with an interval.",
      "Terâhî ile tertîb için atıf harfi."),
  tok("النَّسْخُ","naskh","noun",["mubtada-khabar","masdar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَقَدْ ذُكِرَ فِي بَابِ الْمُحْكَمِ مَفْعُولًا بِهِ («لَا يَحْتَمِلُ النَّسْخَ»)، وَعَادَ الْآنَ مُبْتَدَأً لِيُحَدَّ.",
      "The mubtada in raf' — and it stood in chapter 5 as a maf'ul bihi, in «does not admit ABROGATION». Seven chapters later it comes back as a mubtada to be defined. A term is used where it is needed and defined where it must be.",
      "Merfû mübtedâ — beşinci bâbda «لَا يَحْتَمِلُ النَّسْخَ» içinde mef'ûlün bih olarak geçmişti; yedi bâb sonra tarif edilmek üzere mübtedâ olarak döner. Istılah, gerektiği yerde kullanılır, gerektiğinde tarif edilir."),
  tok("بَيَانُ","bayan","noun",["mubtada-khabar","masdar","idafa-definiteness","form-ii-verbs"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَاخْتِيَارُ «بَيَان» هُوَ الْمَذْهَبُ كُلُّهُ: النَّسْخُ إِظْهَارٌ لِانْتِهَاءِ الْمُدَّةِ، لَا إِبْطَالٌ لِحُكْمٍ كَانَ سَيَدُومُ.",
      "The khabar in raf' and a mudaf — and the choice of the word BAYAN is the whole position. Abrogation is a SHOWING that a term has run out, not an undoing of a ruling that was going to last. God knew the term from the beginning; the abrogating text tells us where it ended. Choose «raf'» instead and you have said the ruling changed, which is a different doctrine.",
      "Merfû haber ve muzâf — «BEYÂN» kelimesinin seçilmesi mezhebin kendisidir. Nesih, müddetin bittiğinin GÖSTERİLMESİdir; devam edecek bir hükmün iptali değil. Müddeti Allah ezelde biliyordu; nâsih nass bize nerede bittiğini bildirir. Yerine «ref'» dersen, hükmün değiştiğini söylemiş olursun ki bu başka bir görüştür."),
  tok("انْتِهَاءِ","intiha","noun",["idafa-definiteness","masdar","form-viii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «اِنْتَهَى» عَلَى افْتِعَالٍ، وَهُوَ نَاقِصٌ فَجَاءَ مَصْدَرُهُ مَمْدُودًا.",
      "The mudaf ilayh in jarr and itself a mudaf — the masdar of اِنْتَهَى on اِفْتِعَال. The verb is NAQIS, and a naqis اِفْتِعَال makes its masdar mamdud: اِنْتِهَاء، اِقْتِضَاء، اِدِّعَاء. The hamza at the end is the weak lam turned into one, so the noun keeps its tanwin — chapter 6's rule, on a fourth root.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — «اِنْتَهَى»nin İFTİÂL vezninde masdarı. Fiil NÂKIStır ve nâkıs iftiâlin masdarı memdûd gelir: اِنْتِهَاء، اِقْتِضَاء، اِدِّعَاء. Sondaki hemze illetli lâmdan dönüşmedir, dolayısıyla isim tenvînini korur — altıncı bâbın kaidesi, dördüncü bir kökte."),
  tok("مُدَّةِ","mudda","noun",["idafa-definiteness","doubled-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — الْحَلْقَةُ الثَّالِثَةُ.",
      "The mudaf ilayh in jarr and itself a mudaf — the third link.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — üçüncü halka."),
  tok("الْحُكْمِ","hukm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ تَمَّتِ السِّلْسِلَةُ أَرْبَعَ حَلَقَاتٍ: بَيَانُ ← انْتِهَاءِ ← مُدَّةِ ← الْحُكْمِ، وَكُلُّ وَاحِدَةٍ فِي الْوَسَطِ مُضَافٌ وَمُضَافٌ إِلَيْهِ مَعًا. وَهَذِهِ أَطْوَلُ إِضَافَةٍ فِي الْكِتَابِ.",
      "The mudaf ilayh in jarr — and with it the chain closes at FOUR links: بَيَانُ ← انْتِهَاءِ ← مُدَّةِ ← الْحُكْمِ, every middle member a mudaf and a mudaf ilayh at once, and only the last not itself a mudaf. It is the longest idafa in the book, and it is not ornament: each link narrows the one before it, and dropping any of them would change the definition.",
      "Mecrûr muzâfun ileyh — zincir onunla DÖRT halkada kapanır: بَيَانُ ← انْتِهَاءِ ← مُدَّةِ ← الْحُكْمِ; ortadaki her üye aynı anda hem muzâf hem muzâfun ileyhtir, yalnız sonuncusu muzâf değildir. Kitaptaki en uzun izâfettir ve süs değildir: her halka öncekini daraltır; birini düşürsen tarif değişir."),
  tok("الشَّرْعِيِّ","shari","noun",["naat-sifa"],
      "نَعْتٌ لِـ«الْحُكْمِ» مَجْرُورٌ — اسْمٌ مَنْسُوبٌ، وَقَدْ مَرَّ نَكِرَةً فِي بَابِ الْإِجْمَاعِ («حُكْمٍ شَرْعِيٍّ») وَهَا هُوَ مَعْرِفَةً.",
      "A na't of «the ruling», in jarr — a nisba noun. It stood INDEFINITE in the chapter on consensus, حُكْمٍ شَرْعِيٍّ, and here it is definite. The na't follows its noun in definiteness as in everything else, and the two occurrences show the rule from both sides.",
      "«الْحُكْمِ»in na'tı, mecrûr — mensûb isim. İcmâ bâbında NEKRE geçmişti («حُكْمٍ شَرْعِيٍّ»), burada marifedir. Na't, mevsûfuna marifelik-nekrelikte de tâbi olur; iki geçiş kaideyi iki yönden gösterir."),
  tok("عِنْدَنَا","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ — وَهِيَ الْمَرَّةُ الثَّالِثَةُ فِي الْكِتَابِ، وَفِي كُلِّ مَرَّةٍ تَسْبِقُ خِلَافًا مَعْلُومًا.",
      "An adverb in nasb and a mudaf — the third time in the book, and each time it stands just where a known disagreement begins. When this matn says «with us» it is not padding: it is a footnote in two words.",
      "Mansub zarf ve muzâf — kitapta üçüncü defadır ve her defasında bilinen bir ihtilâfın hemen önünde durur. Bu metin «bize göre» dediğinde bu dolgu değildir: iki kelimelik bir dipnottur.",
      segments=[seg("عِنْدَ","inda","noun"), seg("نَا","pron-1p","pron")]),
  tok("لَا","la-nafiya","part",["atf-nasaq"],
      "«لَا» عَاطِفَةٌ نَافِيَةٌ — تَنْفِي عَنِ الثَّانِي مَا أُثْبِتَ لِلْأَوَّلِ.",
      "«La» joining and denying: it takes back from the second what was granted to the first. The matn does not merely state its own view; it names the other and refuses it in the same breath.",
      "Nefyeden âtıfa «لَا» — birinciye verileni ikinciden alır. Metin yalnız kendi görüşünü söylemez; ötekini adıyla anıp aynı nefeste reddeder."),
  tok("رَفْعُهُ","raf","noun",["atf-nasaq","masdar","idafa-definiteness"],
      "مَعْطُوفٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ «رَفَعَ»، وَهُوَ الْقَوْلُ الْمُقَابِلُ: أَنَّ النَّسْخَ إِبْطَالُ حُكْمٍ ثَابِتٍ.",
      "Joined, in raf' and a mudaf, with the HA as its mudaf ilayh — the masdar of رَفَعَ, and the rival position named: that abrogation LIFTS a ruling which was standing. Note that رَفْع is also the name of the very case this word is in; the science borrowed the word from the grammar, or the grammar from it.",
      "Ma'tûf, merfû ve muzâf; HÂ muzâfun ileyhtir — «رَفَعَ»in masdarı ve reddedilen görüşün adı: neshin, sâbit bir hükmü kaldırması. Dikkat: «رَفْع» aynı zamanda bu kelimenin içinde bulunduğu i'râb hâlinin de adıdır; ilim kelimeyi gramerden yahut gramer ondan almıştır.",
      punct=".", segments=[seg("رَفْعُ","raf","noun"), seg("هُ","pron-3ms","pron")]),
 ],
 "jumal": [J("النَّسْخُ بَيَانُ انْتِهَاءِ مُدَّةِ الْحُكْمِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And it does not run except in the Prophet's lifetime, because it comes only by revelation.",
 "tr": "Nesih, ancak Peygamber'in hayatında cereyan eder; zira o, vahiyle olur."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq","mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا — وَهِيَ شَرْطُ الِاسْتِثْنَاءِ الْمُفَرَّغِ الْآتِي.",
      "A joining waw, and «la» simply denying — and the condition for the emptied exception coming next.",
      "Atıf vâvı ve amel etmeyen nefy «لَا»sı — gelecek müferrağ istisnânın şartıdır.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَجْرِي","jara","verb",["mudari-marfu","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — وَهُوَ نَاقِصٌ يَائِيٌّ مِنْ «ج ر ي». وَهَذَا هُوَ حُكْمُ الْمَنْقُوصِ نَفْسُهُ، عَلَى فِعْلٍ لَا عَلَى اسْمٍ: الضَّمَّةُ وَالْكَسْرَةُ ثَقِيلَتَانِ عَلَى الْيَاءِ، وَالْفَتْحَةُ خَفِيفَةٌ فَتَظْهَرُ.",
      "A mudari in raf' by a damma ESTIMATED on the ya, which is too heavy to carry it — a naqis yai from ج ر ي. This is the manqus noun's own rule appearing on a VERB: the damma and the kasra are heavy on a ya and are only understood, while the fatha is light and is written. Put this verb after لَنْ and the fatha shows at once: لَنْ يَجْرِيَ.",
      "Yâ üzerinde sıkletten dolayı TAKDÎRÎ damme ile merfû muzâri — «ج ر ي»den nâkıs-ı yâî. Bu, menkūs ismin kaidesinin FİİL üzerinde görünmesidir: damme ile kesra yâya ağır gelir ve takdîr edilir, fetha hafiftir ve yazılır. Bu fiili «لَنْ»den sonra koy, fetha derhal görünsün: لَنْ يَجْرِيَ."),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ — وَهُوَ الْخَامِسُ فِي الْكِتَابِ.",
      "The particle of exception, the exception MUFARRAGH — the fifth in the book. Five negations, five إِلَّا, and not one mustathna minhu named.",
      "İstisnâ edatı; istisnâ MÜFERRAĞdır — kitapta beşincisidir. Beş nefy, beş «إِلَّا» ve hiçbirinde zikredilmiş bir müstesnâ minh yok."),
  tok("فِي","fi","prep",["huruf-jarr","istithna-mufarragh"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يَجْرِي» — وَالْجَارُّ وَالْمَجْرُورُ هُوَ الْمُسْتَثْنَى الْمُفَرَّغُ.",
      "A jarr letter attaching to «runs» — and the phrase after it is the emptied exception itself.",
      "«يَجْرِي»ye taalluk eden cer harfi — sonrasındaki câr-mecrûr müferrağ müstesnânın kendisidir."),
  tok("حَيَاةِ","hayat","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — وَكُتِبَتْ أَلِفُهُ يَاءً («حَيَاة») عَلَى الرَّسْمِ الْمُصْحَفِيِّ الْمَشْهُورِ، وَنُطْقُهَا أَلِفٌ.",
      "In jarr after «fi» and a mudaf. Its alif is written as a YA in the codex spelling — حَيَاة — and pronounced as an alif all the same. Spelling and sound part company here, and only the tradition of the written text explains why.",
      "«فِي» ile mecrûr ve muzâf. Elifi, meşhur mushaf resminde YÂ ile yazılır — «حَيَاة» — ve yine elif olarak okunur. Burada imlâ ile telaffuz ayrılır; sebebini yalnız yazı geleneği açıklar."),
  tok("النَّبِيِّ","nabi","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَقَدْ مَرَّ فِي بَابِ السُّنَّةِ مَجْرُورًا بِـ«عَنْ»، وَهَا هُوَ مُضَافًا إِلَيْهِ.",
      "The mudaf ilayh in jarr — it stood in jarr after «an» in the chapter on the Sunna, and here it is a mudaf ilayh. Same case, two roads to it.",
      "Mecrûr muzâfun ileyh — sünnet bâbında «عَنْ» ile mecrûr geçmişti, burada muzâfun ileyhtir. Aynı i'râb, ona giden iki ayrı yol.", punct="،"),
  tok("لِأَنَّهُ","anna","part",["inna-wa-akhawatuha","lam-taleel"], *LIANNA,
      segments=[seg("لِ","li","prep"), seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("بِالْوَحْيِ","wahy","noun",["huruf-jarr","inna-wa-akhawatuha"],
      "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ» — وَالْخَبَرُ شِبْهُ جُمْلَةٍ، وَالتَّقْدِيرُ «كَائِنٌ بِالْوَحْيِ».",
      "A jarr-majrur standing in the POSITION of raf' as «anna»'s khabar. A khabar may be a shibh jumla, and then the raf' is not on any letter: an omitted «is» carries it, and the phrase stands where that word would have been.",
      "«أَنَّ»nin haberi olarak mahallen merfû câr-mecrûr. Haber şibh-i cümle olabilir; o zaman ref' hiçbir harfin üzerinde değildir: mahzûf bir «kâin» onu taşır ve ibare o kelimenin yerinde durur.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("الْوَحْيِ","wahy","noun")]),
 ],
 "jumal": [J("لَا يَجْرِي إِلَّا فِي حَيَاةِ النَّبِيِّ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir."),
  J("أَنَّهُ بِالْوَحْيِ",
   "الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» وَمَا بَعْدَهَا فِي مَحَلِّ جَرٍّ بِاللَّامِ.",
   "The masdar muawwal from «anna» and what follows it, in the position of jarr after the lam.",
   "«أَنَّ» ve sonrasından çıkan masdar-ı müevvel, lâm ile mahallen mecrûrdur.")]})

S.append({"id": "s3", "translation": {
 "en": "And it does not enter reports, because a report does not admit of alteration.",
 "tr": "Nesih haberlere girmez; zira haber değiştirilmeye ihtimâl vermez."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq","mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "A joining waw, and «la» simply denying.",
      "Atıf vâvı ve amel etmeyen nefy «لَا»sı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَدْخُلُ","dakhala","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «النَّسْخِ» — وَقَابِلْهُ بِـ«يَجْرِي» فِي الْجُمْلَةِ السَّابِقَةِ: ضَمَّةٌ ظَاهِرَةٌ هُنَا وَمُقَدَّرَةٌ هُنَاكَ، وَالْفَرْقُ آخِرُ الْحَرْفِ لَا شَيْءَ سِوَاهُ.",
      "A mudari in raf' by a damma that is WRITTEN, its fa'il a hidden pronoun going back to «abrogation». Set it beside يَجْرِي in the sentence before: the same case, the same governor, and one damma written while the other is only understood. The difference is the last letter and nothing else.",
      "ZÂHİR damme ile merfû muzâri; fâili «النَّسْخِ»e râci müstetir zamîrdir. Bir önceki cümledeki «يَجْرِي» ile yan yana koy: aynı i'râb, aynı âmil; biri yazılı, öteki takdîrî. Fark, son harften ibarettir."),
  tok("الْأَخْبَارَ","akhbar","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ «خَبَرٍ»، وَ«دَخَلَ» يَتَعَدَّى بِنَفْسِهِ هُنَا.",
      "The maf'ul bihi in nasb — the plural of «khabar», and دَخَلَ takes its object directly here, without a preposition.",
      "Mansub mef'ûlün bih — «خَبَر»in cemidir; «دَخَلَ» burada harf-i cersiz, doğrudan mef'ûl alır."),
  tok("لِأَنَّ","anna","part",["inna-wa-akhawatuha","lam-taleel"],
      "اللَّامُ لِلتَّعْلِيلِ، وَ«أَنَّ» حَرْفٌ نَاسِخٌ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَاسْمُهَا هُنَا ظَاهِرٌ لَا ضَمِيرٌ، بِخِلَافِ «لِأَنَّهُ» قَبْلُ.",
      "The LAM of reason and «anna», the abrogating letter that puts its noun into nasb and its khabar into raf' — and here its noun is a WORD standing on the page, not a pronoun clinging to it as in لِأَنَّهُ before. The same particle, twice, with its noun shown two ways.",
      "Ta'lîl LÂMı ve «أَنَّ» — ismini nasb, haberini ref eden nâsih harf. Burada ismi, önceki «لِأَنَّهُ»deki gibi bitişen bir zamîr değil, sayfada duran bir KELİMEdir. Aynı harf, iki defa; ismi iki ayrı şekilde.",
      segments=[seg("لِ","li","prep"), seg("أَنَّ","anna","part")]),
  tok("الْخَبَرَ","khabar","noun",["inna-wa-akhawatuha"],
      "اسْمُ «أَنَّ» مَنْصُوبٌ بِالْفَتْحَةِ.",
      "«Anna»'s noun, in nasb by the fatha — and the nasb is WRITTEN here, which is what makes this the clearer of the two occurrences to learn from.",
      "«أَنَّ»nin mansub ismi, fetha ile — ve nasb burada YAZILIdır; iki geçişten öğrenmeye daha elverişli olanı budur."),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "«La» simply denying.", "Amel etmeyen nefy «لَا»sı."),
  tok("يَحْتَمِلُ","ihtamala","verb",["mudari-marfu","form-viii-verbs","inna-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ» — وَهُوَ الْفِعْلُ الَّذِي حُدَّ بِهِ الْمُحْكَمُ فِي الْبَابِ الْخَامِسِ.",
      "A mudari in raf', and the clause stands in the POSITION of raf' as «anna»'s khabar. It is the very verb that defined the muhkam in chapter 5 — «what does not admit abrogation» — and here it defines why a report cannot be abrogated. One verb, two chapters, and the same idea of what a wording will and will not BEAR.",
      "Merfû muzâri; cümle «أَنَّ»nin haberi olarak mahallen merfûdur. Beşinci bâbda muhkemi tarif eden fiilin aynısıdır — «nesih ihtimâli taşımayan» — ve burada haberin neden neshedilemeyeceğini tarif eder. Tek fiil, iki bâb ve lafzın neyi KALDIRIP kaldıramayacağına dair aynı fikir."),
  tok("التَّبْدِيلَ","tabdil","noun",["maful-bihi","masdar","form-ii-verbs"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَصْدَرُ «بَدَّلَ» عَلَى تَفْعِيلٍ، وَالْمَعْنَى: الْخَبَرُ إِمَّا صِدْقٌ أَوْ كَذِبٌ، فَلَوْ نُسِخَ لَانْقَلَبَ أَحَدُهُمَا إِلَى الْآخَرِ.",
      "The maf'ul bihi in nasb — the masdar of بَدَّلَ on تَفْعِيل. The reasoning behind the word: a report is either true or false, and to abrogate one would be to turn a truth into a falsehood. Rulings have terms; facts do not.",
      "Mansub mef'ûlün bih — «بَدَّلَ»in TEF'ÎL vezninde masdarı. Kelimenin arkasındaki muhâkeme şudur: haber ya doğrudur ya yalan; neshedilseydi biri ötekine dönerdi. Hükümlerin müddeti olur, haberlerin olmaz.",
      punct="."),
 ],
 "jumal": [J("لَا يَدْخُلُ الْأَخْبَارَ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir."),
  J("لَا يَحْتَمِلُ التَّبْدِيلَ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».",
   "A verbal clause in the position of raf', «anna»'s khabar.",
   "«أَنَّ»nin haberi olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s4", "translation": {
 "en": "And it does not enter the firm, because the firm does not admit of abrogation.",
 "tr": "Muhkeme de girmez; zira muhkem nesih ihtimâli taşımaz."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq","mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ.",
      "A joining waw, and «la» denying.",
      "Atıf vâvı ve nefy «لَا»sı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَدْخُلُ","dakhala","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ.",
      "A mudari in raf', its fa'il a hidden pronoun.",
      "Merfû muzâri, fâili müstetirdir."),
  tok("الْمُحْكَمَ","muhkam","noun",["maful-bihi","ism-maful","form-iv-verbs"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَهُوَ الْقِسْمُ الرَّابِعُ مِنْ مَرَاتِبِ الْوُضُوحِ، عَادَ الْآنَ مَفْعُولًا بَعْدَ أَنْ كَانَ مُبْتَدَأً.",
      "The maf'ul bihi in nasb — the fourth rung of the clarity ladder, come back as an object after standing as a mubtada in chapter 5. The matn keeps its own vocabulary and moves each word through the offices as the argument needs.",
      "Mansub mef'ûlün bih — vuzûh merdiveninin dördüncü basamağı; beşinci bâbda mübtedâ iken şimdi mef'ûl olarak döner. Metin kendi kelime dağarını korur ve her kelimeyi, delil neyi gerektiriyorsa o vazifeye taşır."),
  tok("لِأَنَّهُ","anna","part",["inna-wa-akhawatuha","lam-taleel"], *LIANNA,
      segments=[seg("لِ","li","prep"), seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "«La» simply denying.", "Amel etmeyen nefy «لَا»sı."),
  tok("يَحْتَمِلُ","ihtamala","verb",["mudari-marfu","form-viii-verbs","inna-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ «أَنَّ» فِي مَحَلِّ رَفْعٍ.",
      "A mudari in raf', the clause standing as «anna»'s khabar in the position of raf'.",
      "Merfû muzâri; cümle «أَنَّ»nin haberi olarak mahallen merfûdur."),
  tok("النَّسْخَ","naskh","noun",["maful-bihi","masdar"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَهَذِهِ الْجُمْلَةُ بِحُرُوفِهَا هِيَ حَدُّ الْمُحْكَمِ فِي الْبَابِ الْخَامِسِ: «بِحَيْثُ لَا يَحْتَمِلُ النَّسْخَ». فَالتَّعْلِيلُ هُنَا لَيْسَ بُرْهَانًا جَدِيدًا بَلْ إِحَالَةٌ عَلَى التَّعْرِيفِ، وَهَذَا أَقْوَى مَا يَكُونُ: الْمُحْكَمُ لَا يُنْسَخُ لِأَنَّهُ لَوْ نُسِخَ لَمَا كَانَ مُحْكَمًا.",
      "The maf'ul bihi in nasb — and this clause, word for word, IS the definition of the muhkam in chapter 5: «so that it does not admit abrogation». So the reason given here is not a new argument at all but a pointer back to the definition, and that is the strongest kind there is: the muhkam is not abrogated because a thing that could be abrogated would not have been a muhkam.",
      "Mansub mef'ûlün bih — ve bu cümle, harfi harfine, beşinci bâbdaki muhkemin tarifidir: «بِحَيْثُ لَا يَحْتَمِلُ النَّسْخَ». Öyleyse buradaki ta'lîl yeni bir delil değil, tarife bir havâledir; ve bu, olabilecek en kuvvetli delildir: muhkem neshedilmez, zira neshedilebilecek olan zaten muhkem olmazdı.",
      punct="."),
 ],
 "jumal": [J("لَا يَدْخُلُ الْمُحْكَمَ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the abrogation of the Book by the Book is permitted, and of the Sunna by the Sunna.",
 "tr": "Kitâb'ın Kitâb'la, Sünnet'in Sünnet'le neshi câizdir."},
 "tokens": [
  tok("وَيَجُوزُ","jaaza","verb",["atf-nasaq","mudari-marfu","hollow-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«يَجُوزُ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ وَاوِيٌّ مِنْ «ج و ز»، بَقِيَتْ عَيْنُهُ وَاوًا فِي الْمُضَارِعِ لِانْضِمَامِ مَا قَبْلَهَا.",
      "A joining waw, and «yajuzu» a mudari in raf' — an AJWAF WAWI from ج و ز whose middle radical stays a waw in the mudari, because the letter before it carries a damma. Compare يَسْتَقِيمُ in chapter 7, where a kasra turned the same kind of waw into a ya: the vowel before the weak letter decides what it becomes.",
      "Atıf vâvı ve «يَجُوزُ» merfû muzâri — «ج و ز»den ECVEF-İ VÂVÎ; muzâride ayn harfi vâv olarak kalır, zira öncesi ötrelidir. Yedinci bâbdaki «يَسْتَقِيمُ» ile karşılaştır: orada bir kesra aynı cinsten vâvı yâya çevirmişti. İlletli harften önceki hareke, onun ne olacağına karar verir.",
      segments=[seg("وَ","wa","conj"), seg("يَجُوزُ","jaaza","verb")]),
  tok("نَسْخُ","naskh","noun",["fail","masdar","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ عَمَلَ فِعْلِهِ: أُضِيفَ إِلَى مَفْعُولِهِ ثُمَّ تَعَلَّقَ بِهِ الْجَارُّ. وَهُوَ الْمُبْتَدَأُ فِي أَوَّلِ الْبَابِ، فَاعِلًا فِي آخِرِهِ.",
      "The fa'il in raf' and a mudaf — a masdar GOVERNING as its verb would: added to its object and then taking a jarr for what the verb takes. And it is the very word that stood as the mubtada at the head of this chapter, now standing as a fa'il at its close.",
      "Merfû fâil ve muzâf — fiili gibi AMEL EDEN masdar: mef'ûlüne izâfe edilmiş, sonra câr ona taalluk etmiştir. Bâbın başında mübtedâ olan kelimenin kendisi, sonunda fâil olarak durur."),
  tok("الْكِتَابِ","kitab","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ فِي اللَّفْظِ، مَفْعُولُ الْمَصْدَرِ فِي الْمَعْنَى.",
      "The mudaf ilayh in jarr by its form, the masdar's OBJECT in meaning — the thing abrogated.",
      "Lafzan mecrûr muzâfun ileyh, ma'nen masdarın mef'ûlü — neshedilen şey."),
  tok("بِالْكِتَابِ","kitab","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«نَسْخُ» — وَالْبَاءُ لِلِاسْتِعَانَةِ: بِهِ يَقَعُ النَّسْخُ. وَالْكَلِمَةُ نَفْسُهَا مَرَّتَيْنِ فِي مَوْقِعَيْنِ: مَجْرُورَةٌ بِالْإِضَافَةِ ثُمَّ مَجْرُورَةٌ بِالْحَرْفِ.",
      "A jarr-majrur attaching to «the abrogation», the BA being of instrument: the thing BY which it happens. The same word twice in one line and in two offices — once in jarr by an idafa and once in jarr by a letter. Same ending, two entirely different reasons for it, and that is the whole of what i'rab teaches.",
      "«نَسْخُ»a taalluk eden câr-mecrûr; BÂ istiâne içindir: neshin KENDİSİYLE gerçekleştiği şey. Aynı kelime bir satırda iki defa, iki ayrı vazifede — biri izâfetle mecrûr, öteki harfle. Aynı son, tamamen ayrı iki sebep; i'râbın öğrettiği şeyin tamamı budur.",
      segments=[seg("بِ","bi","prep"), seg("الْكِتَابِ","kitab","noun")]),
  tok("وَالسُّنَّةِ","sunna","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الْكِتَابِ» الْمُضَافِ إِلَيْهِ، مَجْرُورٌ.",
      "Joined to «the Book» as a mudaf ilayh, in jarr — the second term of the pair.",
      "Muzâfun ileyh olan «الْكِتَابِ»a ma'tûf, mecrûr — çiftin ikinci tarafı.",
      segments=[seg("وَ","wa","conj"), seg("السُّنَّةِ","sunna","noun")]),
  tok("بِالسُّنَّةِ","sunna","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مَعْطُوفٌ — وَالتَّرْكِيبُ مُقَابَلَةٌ: كِتَابٌ بِكِتَابٍ وَسُنَّةٌ بِسُنَّةٍ، وَتَرْتِيبُ الْأَلْفَاظِ يَحْمِلُ الْحُكْمَ وَحْدَهُ. وَبِهِ خُتِمَ الْبَابُ عَلَى الْأَصْلَيْنِ اللَّذَيْنِ فُتِحَ بِهِمَا الْكِتَابُ.",
      "A joined jarr-majrur — and the whole construction is a MUQABALA, a matched pair: Book by Book, Sunna by Sunna. The arrangement carries the ruling without a word of explanation, which is what balagha means by the figure. And the chapter closes on the two sources the book opened with, eleven chapters back.",
      "Ma'tûf câr-mecrûr — ve bütün terkîb bir MUKĀBELEdir: Kitâb Kitâbla, Sünnet Sünnetle. Diziliş, tek kelime izah olmadan hükmü taşır; belâgatin bu sanattan kastettiği budur. Bâb, kitabın on bir bâb önce açıldığı iki asıl üzerinde kapanır.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("السُّنَّةِ","sunna","noun")]),
 ],
 "jumal": [J("يَجُوزُ نَسْخُ الْكِتَابِ بِالْكِتَابِ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "intiha":  g("اِنْتِهَاء", "ن ه ي", "noun", "coming to an end (masdar, Form VIII)", "intihâ; sona erme (masdar)", 4),
 "mudda":   g("مُدَّة", "م د د", "noun", "a term, a stretch of time", "müddet", 2, plural="مُدَد"),
 "raf":     g("رَفْع", "ر ف ع", "noun", "lifting, removing (masdar) — also the name of the raf' case", "ref'; kaldırma (masdar)", 3),
 "jara":    g("جَرَى", "ج ر ي", "verb", "to run, to take effect", "cereyan etmek, geçerli olmak", 3),
 "hayat":   g("حَيَاة", "ح ي ي", "noun", "life, a lifetime", "hayat", 1),
 "anna":    g("أَنَّ", None, "part", "that (inna's sister: nasb on its noun, raf' on its khabar)", "ki (inne'nin kardeşi)", 3),
 "wahy":    g("وَحْي", "و ح ي", "noun", "revelation", "vahiy", 2),
 "akhbar":  g("أَخْبَار", "خ ب ر", "noun", "reports, statements of fact (plural of خَبَر)", "haberler", 2),
 "khabar":  g("خَبَر", "خ ب ر", "noun", "a report; a statement that is true or false", "haber", 2, plural="أَخْبَار"),
 "tabdil":  g("تَبْدِيل", "ب د ل", "noun", "alteration, exchanging one thing for another (masdar, Form II)", "tebdîl; değiştirme (masdar)", 4),
 "jaaza":   g("جَازَ", "ج و ز", "verb", "to be permitted, to be allowed", "câiz olmak", 3),
}

def build_morph():
    out = {}
    # Both copied after a lemma-identity check: the library already carries
    # them and they agree.
    for lex, src in (("jara", "wasiyyat-abi-hanifa-samti"), ("jaaza", "aqaid-ahl-al-sunna"),
                     ("dakhala", "aqaid-ahl-al-sunna")):
        s = json.loads((ROOT / "content/samples" / src / "morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / "content/samples" / src / "glossary.json").read_text(encoding="utf-8"))
        if lex in GLOSS_ADD:
            assert g_["entries"][lex]["lemma"] == GLOSS_ADD[lex]["lemma"], \
                f"{lex}: {src} has {g_['entries'][lex]['lemma']}, we say {GLOSS_ADD[lex]['lemma']}"
        out[lex] = s["verbs"][lex]
    return out

# دَخَلَ is copied but its glossary entry has to match the source too.
GLOSS_ADD["dakhala"] = g("دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1)

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/12.json").write_text(
    json.dumps({"chapter": 12, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 12 for c in man["chapters"]):
    man["chapters"].append({"n": 12, "title": TITLE12})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.12.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch12:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
