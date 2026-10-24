# -*- coding: utf-8 -*-
"""Author chapter 8 of talkhis-al-miftah — تَعْرِيفُ الْمُسْنَدِ إِلَيْهِ بِالْمَوْصُولِ وَالْإِشَارَةِ.

Chapter 7 asked WHETHER to say the subject. This one asks HOW: a definite
musnad ilayh can be made definite six ways, and the choice is never neutral.
The Talkhis works two of them right through — the relative and the
demonstrative — and the reasons it gives are the least mechanical thing in the
whole fann, because several of them are about the HEARER rather than the
sentence.

The relative is chosen when the ṣila is the only thing the hearer knows about
the man; when the proper name would be ugly to say (الَّذِي يَخْرُجُ مِنَ الْإِنْسَانِ
rather than the word for it); for sheer magnification, where naming the thing
would make it smaller (فَغَشِيَهُمْ مِنَ الْيَمِّ مَا غَشِيَهُمْ — «there covered them
what covered them», and no noun could have carried it); and to point at what
KIND of report is coming, so that إِنَّ الَّذِينَ يَسْتَكْبِرُونَ already announces a
punishment before the punishment is named.

The demonstrative is chosen to separate its referent completely, to lean on a
hearer who has not been following, to place a thing near or middle or far —
and then, because near and far are also high and low, to despise by pointing
close and to honour by pointing far. أَهَذَا الَّذِي يَذْكُرُ آلِهَتَكُمْ against
ذَلِكَ الْكِتَابُ: one letter of distance apart, and the whole attitude reversed.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~712-790, which carries
all of it in vowelled Arabic — the two prose examples, Yusuf 12:23, Taha 20:78,
al-A'raf 7:92, al-Anbiya 21:36, al-Baqara 2:2, and the هَذَا زَيْدٌ / ذَاكَ زَيْدٌ /
ذَلِكَ زَيْدٌ triple. Paired phrases are juxtaposed with a full stop between
them, as in chapters 5 to 7; nothing is composed.

Grammar this chapter is chosen to teach:
  • FOUR RELATIVES with four different shapes of ṣila — a verbal clause, a
    NOMINAL clause (الَّتِي هُوَ فِي بَيْتِهَا), a kana clause, and a clause whose
    verb is the same verb again (مَا غَشِيَهُمْ). The ʿaid is visible in every one
    of them, and the note on the mawsul finally has the full set.
  • الْخَاسِرِينَ against chapter 7's الْمُفْلِحُونَ — the same sound masculine
    plural, one in NASB by the ya and one in RAF' by the waw, one chapter apart,
    and both of them khabars with a damir fasl in front.
  • أَمْسِ — mabni on the KASRA, which almost nothing else in the language is.
  • هَذَا / ذَاكَ / ذَلِكَ — near, middle and far, three sentences that differ by
    one word and say three different things about where a man is standing.
  • آلِهَتَكُمْ — the madda: a hamza carrying a fatha followed by an alif of
    prolongation, written as one letter, and the app's harakat auditor has to
    know that آ is not an unvowelled alif.
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

TITLE8 = {"ar": "تَعْرِيفُ الْمُسْنَدِ إِلَيْهِ بِالْمَوْصُولِ وَالْإِشَارَةِ",
          "en": "Making the Subject Definite: by the Relative, and by Pointing",
          "tr": "Müsnedün İleyhin Ma'rife Kılınması: Mevsûl ve İşaretle"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "The one who was with us yesterday is a learned man. — What comes out of a human being breaks the ablution.",
 "tr": "Dün bizimle beraber olan, âlim bir adamdır. — İnsandan çıkan şey abdesti bozar."},
 "tokens": [
  tok("الَّذِي","alladhi","pron",["ism-mawsul","mubtada-khabar","tarif-al-musnad-ilayh"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَعُرِّفَ بِهِ الْمُسْنَدُ إِلَيْهِ لِأَنَّ الْمُخَاطَبَ لَا يَعْرِفُ مِنْ حَالِهِ إِلَّا الصِّلَةَ.",
      "A relative noun, mabni on the sukun, in the position of raf' as the mubtada — and the subject was made definite THIS way because the ṣila is the only thing the hearer knows about him. He was not there when the man was named; he was there yesterday. A proper name would have identified nobody.",
      "İsm-i mevsûl; sükûn üzere mebnî, mahallen merfû mübtedâdır — ve müsnedün ileyh BU yolla ma'rife kılınmıştır, zira muhâtabın onun hâlinden bildiği tek şey sıladır. Adam adlandırılırken orada değildi; dün oradaydı. Bir alem hiç kimseyi tanıtmazdı."),
  tok("كَانَ","kana","verb",["kana-wa-akhawatuha","jumla-sifa"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» يَعُودُ عَلَى الْمَوْصُولِ — وَهُوَ الْعَائِدُ. وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "An incomplete mazi; its ism is a pronoun CONCEALED as «he», pointing back at the relative — and that concealed pronoun is the ʿAID, without which the ṣila would not be a ṣila. The clause has no position in i'rab. A ṣila built on kana is the third shape this chapter shows.",
      "Nâkıs mâzî; ismi, mevsûle râci müstetir «هُوَ» zamiridir — ve o gizli zamir ÂİDdir; onsuz sıla, sıla olmazdı. Cümlenin i'râbdan mahalli yoktur. Kâne üzerine kurulmuş sıla, bu bâbın gösterdiği üçüncü şekildir."),
  tok("مَعَنَا","maa","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ — وَهُوَ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ».",
      "A zarf of place in nasb and a mudaf, with «na» annexed to it — standing in the position of nasb as the khabar of «kana». مَعَ is a NOUN, not a letter: this app peels مَعَنَا into two the way it peels مَعَهُ, and the pronoun is a mudaf ilayh rather than a majrur.",
      "Mansub mekân zarfı ve muzâf; «نَا» muzâfun ileyhtir — ve «كَانَ»nin haberi olarak mahallen mansubdur. «مَعَ» harf değil İSİMdir: uygulama «مَعَنَا»yı da «مَعَهُ» gibi ikiye ayırır ve zamir mecrûr değil, muzâfun ileyh olur.",
      segments=[seg("مَعَ","maa","noun"), seg("نَا","pron-1p","pron")]),
  tok("أَمْسِ","ams","noun",["maful-fih"],
      "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«كَانَ».",
      "A zarf of TIME, mabni ON THE KASRA, standing in the position of nasb and attaching to «was». Almost nothing else in the language is built on a kasra — the imperative on a sukun, أَيْنَ and كَيْفَ on a fatha, and أَمْسِ alone on a kasra, when it means the particular yesterday just past.",
      "ZAMAN zarfı; KESRA üzere mebnî, mahallen mansub ve «كَانَ»ye taalluk eder. Dilde kesra üzere mebnî olan başka hemen hiçbir şey yoktur — emir sükûn üzere, «أَيْنَ» ile «كَيْفَ» fetha üzere; «أَمْسِ» ise, geçen muayyen dünü kastettiğinde, tek başına kesra üzere mebnîdir."),
  tok("رَجُلٌ","rajul","noun",["mubtada-khabar"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ — نَكِرَةٌ، وَالْخَبَرُ يَجُوزُ تَنْكِيرُهُ وَإِنْ كَانَ الْمُبْتَدَأُ مَعْرِفَةً.",
      "The khabar of the mubtada, in raf' — and it is INDEFINITE, which a khabar may be even when the mubtada is definite. The rule that an indefinite may not open a sentence says nothing about where it may finish one.",
      "Merfû haber — ve NEKREdir; mübtedâ marife olsa da haberin nekre olması câizdir. Nekrenin cümleye başlayamayacağı kāidesi, cümleyi nerede bitirebileceği hakkında hiçbir şey söylemez."),
  tok("عَالِمٌ","alim","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«رَجُلٌ» مَرْفُوعٌ — اسْمُ فَاعِلٍ عَلَى فَاعِلٍ.",
      "A na't of «a man», in raf' — an ism fa'il on فَاعِل. The whole predicate is two indefinite words, and the subject is a five-word relative clause: the sentence is heavy at the front on purpose, because the identification is the news.",
      "«رَجُلٌ»un merfû na'tı — FÂİL vezninde ism-i fâil. Yüklemin tamamı iki nekre kelime, öznesi ise beş kelimelik bir mevsûl terkîbi: cümle bilerek öne ağırdır, zira haber olan şey TANITMAdır.",
      punct="."),
  tok("الَّذِي","alladhi","pron",["ism-mawsul","mubtada-khabar","tarif-al-musnad-ilayh"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَعُرِّفَ بِهِ الْمُسْنَدُ إِلَيْهِ اسْتِقْبَاحًا لِلتَّصْرِيحِ بِاسْمِهِ.",
      "A relative in the position of raf' as the mubtada — and here the subject was made definite this way because SAYING ITS NAME WOULD BE UGLY. The fiqh books need to state the thing that breaks ablution and decline to write the word; the relative gives them a definite subject and a clean page at once. It is the plainest possible demonstration that a choice of definiteness is a choice of manners.",
      "Mahallen merfû mübtedâ olan ism-i mevsûl — ve müsnedün ileyh burada, İSMİNİ AÇIKÇA SÖYLEMEK ÇİRKİN olduğu için bu yolla ma'rife kılınmıştır. Fıkıh kitapları abdesti bozan şeyi söylemek zorundadır ve o kelimeyi yazmaktan kaçınır; mevsûl onlara aynı anda hem marife bir özne hem temiz bir sayfa verir. Ma'rifelik tercihinin bir edeb tercihi olduğunun en sade ispatı budur."),
  tok("يَخْرُجُ","kharaja","verb",["mudari-marfu","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» عَائِدٌ عَلَى الْمَوْصُولِ — وَالْجُمْلَةُ صِلَةٌ لَا مَحَلَّ لَهَا.",
      "A mudari' in raf', its fa'il concealed as «he» and pointing back at the relative — the ʿaid again, and again invisible. The clause is the ṣila and has no position in i'rab.",
      "Merfû muzâri fiil; fâili müstetir «هُوَ»dur ve mevsûle râcidir — yine ÂİD, yine görünmez. Cümle sıladır, i'râbdan mahalli yoktur."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ، فُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter of origin, its nun opened with a fatha for the meeting of two quiescents.",
      "İbtidâ-i gāye için cer harfi; nûnu, iki sâkinin buluşması sebebiyle fetha almıştır."),
  tok("الْإِنْسَانِ","insan","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«مِنْ» — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَخْرُجُ»، لَغْوٌ.",
      "Majrur by «min» — the phrase attaching to «comes out», so it is laghw.",
      "«مِنْ» ile mecrûr — câr-mecrûr «يَخْرُجُ»a taalluk eder, lağvdır."),
  tok("نَاقِضٌ","naqid","noun",["mubtada-khabar","ism-fail"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ — اسْمُ فَاعِلٍ عَامِلٌ عَمَلَ فِعْلِهِ.",
      "The khabar in raf' — an ism fa'il, and one that GOVERNS: the jarr phrase after it is its own complement, not the sentence's. A participle doing a verb's work is what makes the four-word predicate possible.",
      "Merfû haber — ism-i fâil; ve AMEL EDEN bir ism-i fâil: ardındaki câr-mecrûr cümlenin değil, onun kendi mütemmimidir. Fiilin işini gören bir vasıf, dört kelimelik yüklemi mümkün kılan şeydir."),
  tok("لِلْوُضُوءِ","wudu","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "اللَّامُ حَرْفُ جَرٍّ وَ«الْوُضُوءِ» مَجْرُورٌ، وَأَلِفُ «أَلْ» مَحْذُوفَةٌ خَطًّا — مُتَعَلِّقٌ بِـ«نَاقِضٌ»، لَغْوٌ.",
      "The lam is a jarr letter and «the ablution» is majrur, the article's alif dropped in writing — attaching to «breaking», laghw. Both halves of this sentence hang their jarr phrase on a participle rather than a verb; there is no verb in the predicate at all.",
      "Lâm cer harfi, «الْوُضُوءِ» mecrûr; «أَلْ»in elifi yazıda düşmüştür — «نَاقِضٌ»a taalluk eder, lağvdır. Bu cümlenin iki yarısı da câr-mecrûrunu fiile değil vasfa asar; yüklemde hiç fiil yoktur.",
      segments=[seg("لِ","li","prep"), seg("الْوُضُوءِ","wudu","noun")],
      punct="."),
 ],
 "jumal": [J("كَانَ مَعَنَا أَمْسِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("يَخْرُجُ مِنَ الْإِنْسَانِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "And she in whose house he was sought to lure him from himself.",
 "tr": "Evinde bulunduğu kadın, onun nefsinden murâd almak istedi."},
 "tokens": [
  tok("وَرَاوَدَتْهُ","rawada","verb",["fail","maful-bihi","form-iii-verbs"],
      "الْوَاوُ حَسَبَ مَا قَبْلَهَا، وَ«رَاوَدَتْ» فِعْلٌ مَاضٍ عَلَى فَاعَلَ وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.",
      "The waw as its context takes it, and «sought to lure» is a mazi of Form III with the ta of the feminine, the ha its object in the position of nasb. Form III names an act done TOWARDS someone, which is why the verb needs an «an» after it as well: she sought to draw him away FROM himself.",
      "Vâv öncesine göredir; «رَاوَدَتْ» FÂALE vezninde mâzîdir, tâ müennesliktir; hâ ise mahallen mansub mef'ûlün bihtir. MUFÂALE bâbı, birine YÖNELİK yapılan işi adlandırır; fiilin ardından ayrıca bir «عَنْ» istemesinin sebebi de budur: onu nefsinden UZAKLAŞTIRMAK istedi.",
      segments=[seg("وَ","wa","conj"), seg("رَاوَدَتْهُ","rawada","verb")]),
  tok("الَّتِي","allati","pron",["ism-mawsul","fail","tarif-al-musnad-ilayh"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَعُرِّفَ بِهِ الْمُسْنَدُ إِلَيْهِ زِيَادَةً فِي التَّقْرِيرِ.",
      "A relative, mabni, in the position of raf' as the FA'IL — and the subject was made definite this way for EXTRA REINFORCEMENT. The verse is about Yusuf's innocence, and «she in whose house he was» states the whole difficulty of his position in five words: he was in her house, she had the power, and the naming of neither party would have said any of it.",
      "İsm-i mevsûl; mahallen merfû FÂİLdir — ve müsnedün ileyh, ZİYÂDE TAKRÎR için bu yolla ma'rife kılınmıştır. Âyet Yûsuf aleyhisselâmın temizliği hakkındadır; ve «evinde bulunduğu kadın» ifadesi, onun içinde bulunduğu bütün zorluğu beş kelimede söyler: onun evindeydi, kuvvet ondaydı; iki tarafın adının anılması bunların hiçbirini söylemezdi."),
  tok("هُوَ","huwa","pron",["mubtada-khabar","jumla-sifa"],
      "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ صِلَةُ الْمَوْصُولِ.",
      "A detached pronoun in the position of raf' as the mubtada — and the ṣila here is a NOMINAL sentence, which is the second of the four shapes this chapter shows. A ṣila may be a verbal clause, a nominal one, a shibh jumla or a kana clause; the one thing it may never be is a single word.",
      "Munfasıl zamir, mahallen merfû mübtedâ — ve buradaki sıla İSİM cümlesidir; bu bâbın gösterdiği dört şekilden ikincisi. Sıla; fiil cümlesi, isim cümlesi, şibh-i cümle yahut kâne cümlesi olabilir; olamayacağı tek şey tek bir kelimedir."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "A jarr letter of containment.",
      "Zarfiyyet için cer harfi."),
  tok("بَيْتِهَا","bayt","noun",["huruf-jarr","idafa-definiteness","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ وَ«هَا» مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ، فَهُوَ ظَرْفٌ مُسْتَقَرٌّ. وَ«هَا» هِيَ الْعَائِدُ.",
      "Majrur by «fi», a mudaf with «ha» annexed to it — and the phrase attaches to an omitted khabar, so it is MUSTAQARR. And the «ha» is the ʿAID: it is the pronoun that carries the relative back into its own clause, and here it is written rather than concealed, which makes this the clearest ʿaid in the library.",
      "«فِي» ile mecrûr, muzâf; «هَا» muzâfun ileyhtir — ve terkîb mahzûf bir habere taalluk eder, öyleyse MÜSTAKARdır. «هَا» ise ÂİDdir: mevsûlü kendi cümlesine geri taşıyan zamirdir ve burada gizli değil YAZILIdır; kütüphanedeki en berrak âid budur.",
      segments=[seg("بَيْتِ","bayt","noun"), seg("هَا","pron-3fs","pron")]),
  tok("عَنْ","an","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ — مُتَعَلِّقٌ بِـ«رَاوَدَتْ».",
      "A jarr letter of MOVING AWAY FROM — attaching to «sought to lure». The letter is doing real work: رَاوَدَهُ means to coax him, and رَاوَدَهُ عَنْ نَفْسِهِ means to coax him AWAY from himself. Remove the letter and the sentence loses its whole subject matter.",
      "MÜCÂVEZE için cer harfi — «رَاوَدَتْ»a taalluk eder. Harf gerçek bir iş görüyor: «رَاوَدَهُ» onu ikna etmeye çalışmak, «رَاوَدَهُ عَنْ نَفْسِهِ» ise onu nefsinden UZAKLAŞTIRMAYA çalışmak demektir. Harfi kaldırın, cümle bütün mevzuunu kaybeder."),
  tok("نَفْسِهِ","nafs","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَنْ» وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Majrur by «an», a mudaf with the ha annexed to it. Three pronouns in this verse point at two different people and never once collide, because Arabic marks gender on every one of them.",
      "«عَنْ» ile mecrûr, muzâf; hâ muzâfun ileyhtir. Bu âyetteki üç zamir iki ayrı kişiye işaret eder ve bir kere bile çakışmaz; zira Arapça hepsinde cinsiyeti işaretler.",
      punct="."),
 ],
 "jumal": [J("هُوَ فِي بَيْتِهَا",
   "جُمْلَةٌ اسْمِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan isim cümlesi — mahalsizdir.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "So there covered them, of the sea, what covered them. — Those who called Shu'ayb a liar, they were the losers.",
 "tr": "Denizden onları örten örttü. — Şuayb'ı yalanlayanlar, işte hüsrana uğrayanlar onlardır."},
 "tokens": [
  tok("فَغَشِيَهُمْ","ghashiya","verb",["fail","maful-bihi","naqis-verbs"],
      "الْفَاءُ عَاطِفَةٌ، وَ«غَشِيَ» فِعْلٌ مَاضٍ نَاقِصٌ مِنْ بَابِ سَمِعَ، وَ«هُمْ» مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.",
      "A joining fa, and «covered» is a DEFECTIVE mazi of the bab samia — its ya keeps a kasra in the third person and drops only in the plural (غَشُوا) — with «them» as its object in the position of nasb.",
      "Atıf fâsı; «غَشِيَ» semia bâbından NÂKIS mâzîdir — yâsı üçüncü şahısta kesrasını korur, yalnız cemide düşer (غَشُوا) — ve «هُمْ» mahallen mansub mef'ûlün bihtir.",
      segments=[seg("فَ","fa","conj"), seg("غَشِيَهُمْ","ghashiya","verb")]),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلتَّبْعِيضِ أَوْ لِبَيَانِ الْجِنْسِ.",
      "A jarr letter — here of PARTITION or of naming the kind: «of the sea», some of it, a part whose size is left unsaid. The letter is chosen to keep the quantity out of the sentence, which is the same work the relative does two words later.",
      "Cer harfi — burada TEB'ÎZ yahut cinsi beyân içindir: «denizden», bir kısmı; miktarı söylenmemiş bir parça. Harf, mikdarı cümlenin dışında tutmak için seçilmiştir; iki kelime sonraki mevsûlün gördüğü işin aynısı."),
  tok("الْيَمِّ","yamm","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«مِنْ» — مُتَعَلِّقٌ بِـ«غَشِيَ»، لَغْوٌ.",
      "Majrur by «min» — attaching to «covered», laghw.",
      "«مِنْ» ile mecrûr — «غَشِيَ»ye taalluk eder, lağvdır."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","fail","tarif-al-musnad-ilayh","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَعُرِّفَ بِهِ الْمُسْنَدُ إِلَيْهِ لِلتَّفْخِيمِ.",
      "A relative, mabni, in the position of raf' as the FA'IL — and the subject was made definite this way for TAFKHIM, sheer magnification. Any noun would have been smaller than the thing: say «the water» and you have measured it. «What covered them» refuses to say, and the refusal is the whole of the effect. Note also where it stands: a verb three words back, a jarr phrase between, and the fa'il seat empty — which is exactly the shape chapter 4 taught the engine to read.",
      "Mahallen merfû FÂİL olan ism-i mevsûl — ve müsnedün ileyh TEFHÎM için, yani büyütmek için bu yolla ma'rife kılınmıştır. Hangi isim gelseydi şeyden küçük olurdu: «su» deyin, onu ölçmüş olursunuz. «Onları örten» söylemeyi reddeder ve tesirin tamamı bu reddediştir. Durduğu yere de dikkat: üç kelime geride bir fiil, arada bir câr-mecrûr ve boş bir fâil yeri — dördüncü bâbın motora okumayı öğrettiği şeklin ta kendisi."),
  tok("غَشِيَهُمْ","ghashiya","verb",["fail","maful-bihi","naqis-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ وَ«هُمْ» مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا، وَفَاعِلُهُ مُسْتَتِرٌ هُوَ الْعَائِدُ.",
      "The same mazi again with the same object — and the clause is the ṣila, its concealed fa'il the ʿaid. The verse repeats the verb rather than complete it, and that is the figure: the ṣila of the relative is the very predicate the relative is the subject of, so the sentence closes on itself and says nothing more than that it happened.",
      "Aynı mâzî, aynı mef'ûlle yeniden — ve cümle sıladır, müstetir fâili âiddir. Âyet fiili tamamlamaz, TEKRAR eder; sanat da budur: mevsûlün sılası, mevsûlün öznesi olduğu yüklemin ta kendisidir; cümle kendi üzerine kapanır ve olduğundan başka bir şey söylemez.",
      punct="."),
  tok("الَّذِينَ","alladhina","pron",["ism-mawsul","mubtada-khabar","tarif-al-musnad-ilayh"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَعُرِّفَ بِهِ الْمُسْنَدُ إِلَيْهِ لِلْإِيمَاءِ إِلَى وَجْهِ بِنَاءِ الْخَبَرِ.",
      "A plural relative, mabni on the fatha, in the position of raf' as the mubtada — and the subject was made definite this way to POINT AT THE KIND OF REPORT COMING. Naming them by what they did announces that the khabar will be a recompense for doing it, before the khabar has arrived. A reader who hears «those who called him a liar» already knows the sentence will not end well.",
      "Cemi ism-i mevsûl; fetha üzere mebnî, mahallen merfû mübtedâdır — ve müsnedün ileyh, GELECEK HABERİN CİNSİNE İMÂ için bu yolla ma'rife kılınmıştır. Onları yaptıkları işle adlandırmak, haber gelmeden önce onun bir CEZÂ olacağını duyurur. «Onu yalanlayanlar» diye işiten okuyucu, cümlenin iyi bitmeyeceğini şimdiden bilir."),
  tok("كَذَّبُوا","kadhdhaba","verb",["fail","maful-bihi","form-ii-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ عَلَى فَعَّلَ، وَوَاوُ الْجَمَاعَةِ فَاعِلٌ فِي مَحَلِّ رَفْعٍ وَهِيَ الْعَائِدُ — وَالْجُمْلَةُ صِلَةٌ.",
      "A mazi of Form II, and the WAW OF THE GROUP is its fa'il, in the position of raf' — and that waw is the ʿaid, written and visible. Form II here is تَكْذِيب, «to call a liar»: the doubled letter turns a state into a verdict passed on someone.",
      "TEF'ÎL vezninde mâzî; CEMÂAT VÂVI mahallen merfû fâildir ve âid odur — yazılı ve görünür. Buradaki tef'îl «tekzîb»dir, «yalancı saymak»: şeddeli harf, bir hâli, birisi hakkında verilmiş bir hükme çevirir."),
  tok("شُعَيْبًا","shuayb","propn",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَهُوَ عَلَمٌ عَلَى وَزْنِ فُعَيْلٍ، وَهُوَ مُنْصَرِفٌ فَنُوِّنَ.",
      "The object in nasb — a proper name on the DIMINUTIVE scale فُعَيْل, and it takes a tanwin, so it is not barred from it. A name may be barred for foreignness or for a feminine ending; a diminutive shape bars nothing, and the tanwin on the page is the proof.",
      "Mansub mef'ûlün bih — TASGÎR vezni olan FU'AYL üzerinde bir alem; ve tenvîn alır, öyleyse gayr-i munsarif değildir. Bir isim, a'cemîlik yahut müenneslik sebebiyle men edilebilir; tasgîr vezni hiçbir şeyi men etmez ve sayfadaki tenvîn bunun delîlidir."),
  tok("كَانُوا","kana","verb",["kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَوَاوُ الْجَمَاعَةِ اسْمُهُ فِي مَحَلِّ رَفْعٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "An incomplete mazi, the waw of the group its ISM in the position of raf' — and the whole clause is the khabar of the mubtada, in the position of raf'. Two waws of the group in one sentence, one a fa'il and one the ism of kana: the same letter, two different offices, decided by the verb in front of it.",
      "Nâkıs mâzî; cemâat vâvı mahallen merfû İSMİdir — ve cümlenin tamamı, mübtedânın haberi olarak mahallen merfûdur. Tek cümlede iki cemâat vâvı: biri fâil, öteki kânenin ismi; aynı harf, iki ayrı vazife, kararı önündeki fiil veriyor."),
  tok("هُمُ","hum","pron",["damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — يُفِيدُ الْحَصْرَ، وَضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A pronoun of SEPARATION, with no position in i'rab: it announces that what follows is the khabar and not an adjective, and it carries restriction — «they and nobody else». Chapter 7 had the same pronoun in the same office, inside a nominal sentence; here it stands inside kana.",
      "FASIL zamiri; i'râbdan mahalli yoktur — ardındakinin sıfat değil haber olduğunu bildirir ve hasr ifade eder: «başkası değil, onlar». Yedinci bâbda aynı zamir aynı vazifedeydi, fakat isim cümlesi içinde; burada kânenin içinde duruyor."),
  tok("الْخَاسِرِينَ","khasir","noun",["kana-wa-akhawatuha","jam-mudhakkar-salim","ism-fail"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "The khabar of «kana», in NASB, its sign the YA because it is a sound masculine plural. Set it beside chapter 7's الْمُفْلِحُونَ — the same class of plural, the same office of khabar, the same damir fasl in front of it — and one takes a waw because a mubtada raised it while the other takes a ya because kana put it in nasb. Two chapters apart, and the pair says everything about how this plural declines.",
      "MANSUB «كَانَ» haberi; nasb alâmeti, cem'-i müzekker-i sâlim olduğu için YÂdır. Yedinci bâbdaki «الْمُفْلِحُونَ» ile yan yana koyun — aynı cemi sınıfı, aynı haber vazifesi, önünde aynı fasıl zamiri — biri vâv alır, çünkü onu bir mübtedâ ref' etmiştir; öteki yâ alır, çünkü onu kâne nasb etmiştir. İki bâb arayla duran bu çift, bu ceminin nasıl i'râb aldığı hakkında her şeyi söyler.",
      punct="."),
 ],
 "jumal": [J("غَشِيَهُمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("كَانُوا هُمُ الْخَاسِرِينَ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
   "A verbal sentence in the position of raf' as the khabar of the mubtada.",
   "Mübtedânın haberi olarak mahallen merfû fiil cümlesi.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "«Is THIS the one who speaks of your gods?» — THAT is the Book, in which there is no doubt.",
 "tr": "«İlâhlarınızı diline dolayan BU mu?» — İŞTE O kitap; onda hiçbir şüphe yoktur."},
 "tokens": [
  tok("أَهَذَا","hadha","pron",["asma-al-ishara","mubtada-khabar","tarif-al-musnad-ilayh"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَ«هَذَا» اسْمُ إِشَارَةٍ لِلْقَرِيبِ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْإِشَارَةُ إِلَى الْقَرِيبِ هُنَا لِلتَّحْقِيرِ.",
      "The hamza is of DENYING interrogation, and «this» is the demonstrative for what is NEAR, mabni, in the position of raf' as the mubtada — and pointing near is here for CONTEMPT. Distance in Arabic is also rank: the man is standing right there, and saying so is the insult.",
      "Hemze İNKÂRÎ istifham içindir; «هَذَا» ise YAKIN için ism-i işaret, mahallen merfû mübtedâdır — ve yakına işaret burada TAHKÎR içindir. Arapçada mesafe aynı zamanda mertebedir: adam tam oradadır ve bunu söylemek hakaretin kendisidir.",
      segments=[seg("أَ","hamza-istifham","part"), seg("هَذَا","hadha","pron")]),
  tok("الَّذِي","alladhi","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "A relative in the position of raf' as the KHABAR. The demonstrative and the relative stand in one sentence here, each doing its own work: the first points, the second describes, and neither could do the other's job.",
      "Mahallen merfû HABER olan ism-i mevsûl. İşaret ismi ile mevsûl bu cümlede yan yana durur, her biri kendi işini görür: birincisi işaret eder, ikincisi vasfeder; hiçbiri ötekinin işini göremez."),
  tok("يَذْكُرُ","dhakara","verb",["mudari-marfu","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَفَاعِلُهُ مُسْتَتِرٌ عَائِدٌ عَلَى الْمَوْصُولِ — وَالْجُمْلَةُ صِلَةٌ. وَ«ذَكَرَ» هُنَا بِمَعْنَى الْعَيْبِ.",
      "A mudari' in raf', its fa'il concealed and pointing back at the relative; the clause is the ṣila. And «mentions» here means to mention with BLAME — the verb's neutral sense is not what the speakers heard, and nothing in the grammar says so. That is a matter for the lexicon and the situation, not for the i'rab.",
      "Merfû muzâri; fâili müstetirdir ve mevsûle râcidir; cümle sıladır. Ve buradaki «ذَكَرَ» AYIPLAYARAK anmak mânâsındadır — fiilin tarafsız mânâsı, söyleyenlerin işittiği şey değildir; ve gramerde bunu söyleyen hiçbir şey yoktur. Bu, i'râbın değil, sözlüğün ve makāmın işidir."),
  tok("آلِهَتَكُمْ","ilah","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ وَ«كُمْ» مُضَافٌ إِلَيْهِ — جَمْعُ تَكْسِيرٍ لِـ«إِلَه»، وَالْمَدَّةُ هَمْزَةٌ مَفْتُوحَةٌ بَعْدَهَا أَلِفٌ.",
      "The object in nasb, a mudaf with «kum» annexed to it — a broken plural of إِلَه. And the MADDA at the front is two letters written as one: a hamza carrying a fatha, then an alif of prolongation. آ is not an unvowelled alif, which is exactly what the app's harakat auditor has to know before it can pass a word like this.",
      "Mansub mef'ûlün bih, muzâf; «كُمْ» muzâfun ileyhtir — «إِلَه»in cem'-i teksîri. Baştaki MEDDE ise tek yazılan iki harftir: fethalı bir hemze, ardından bir med elifi. «آ» harekesiz bir elif değildir; uygulamanın hareke denetçisinin böyle bir kelimeyi geçirebilmek için önce bilmesi gereken şey de budur.",
      punct="."),
  tok("ذَلِكَ","dhalika","pron",["asma-al-ishara","mubtada-khabar","tarif-al-musnad-ilayh"],
      "اسْمُ إِشَارَةٍ لِلْبَعِيدِ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَاللَّامُ لِلْبُعْدِ وَالْكَافُ لِلْخِطَابِ. وَالْإِشَارَةُ إِلَى الْبَعِيدِ هُنَا لِلتَّعْظِيمِ.",
      "The demonstrative for what is FAR, mabni, in the position of raf' as the mubtada — its lam is the lam of DISTANCE and its kaf is the kaf of ADDRESS, neither of them part of the word's own letters. And pointing far is here for HONOUR. Set it against أَهَذَا four words back: one letter of distance apart, and the whole attitude reversed.",
      "UZAK için ism-i işaret; mahallen merfû mübtedâdır — lâmı UZAKLIK lâmı, kâfı HİTÂB kâfıdır; ikisi de kelimenin kendi harflerinden değildir. Ve uzağa işaret burada TA'ZÎM içindir. Dört kelime önceki «أَهَذَا» ile karşılaştırın: bir mesafe harfi fark, ve bütün tavır tersine dönmüş."),
  tok("الْكِتَابُ","kitab","noun",["mubtada-khabar"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ — وَقِيلَ: بَدَلٌ أَوْ نَعْتٌ، وَالْخَبَرُ الْجُمْلَةُ بَعْدَهُ.",
      "The khabar of the mubtada, in raf' — though it is also read as a badal or a na't, with the clause after it as the khabar. Both readings are in the books; the surface does not settle it, and this app's rule is to name what is undecidable rather than choose quietly.",
      "Merfû haber — bununla birlikte bedel yahut na't olduğu, haberin ise sonraki cümle olduğu da söylenmiştir. İki okuyuş da kitaplarda vardır; yüzey meseleyi bitirmez ve bu uygulamanın kāidesi, karara bağlanamayanı sessizce seçmek değil ADLANDIRMAKtır."),
  tok("لَا","la-nafiya-lil-jins","part",["la-nafiya-lil-jins"],
      "لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ «إِنَّ».",
      "The «la» that denies the WHOLE GENUS, and it governs as «inna» does: its noun in nasb, built on the fatha, and its khabar in raf'. It does not say «there is no doubt here» but «doubt of any kind is ruled out», which is a stronger claim and a different word.",
      "CİNSİNİ nefyeden «لَا»; «إِنَّ» gibi amel eder: ismini nasb — fetha üzere mebnî kılar — haberini ref' eder. «Burada şüphe yok» demez, «hiçbir cinsten şüphe söz konusu değil» der; bu daha kuvvetli bir iddia ve başka bir kelimedir."),
  tok("رَيْبَ","rayb","noun",["la-nafiya-lil-jins"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — نَكِرَةٌ مُفْرَدَةٌ، فَبُنِيَتْ.",
      "The ism of «la», MABNI on the fatha, in the position of nasb — and it is built rather than declined because it is a bare indefinite standing straight after the la. Add a word between them, or annex it, and it would take a written fatha as a manṣūb noun instead.",
      "«لَا»nın ismi; fetha üzere MEBNÎ, mahallen mansubdur — ve i'râb almayıp mebnî olmasının sebebi, «لَا»dan hemen sonra gelen müfred bir nekre olmasıdır. Araya bir kelime girse yahut muzâf olsa, mansub bir isim olarak yazılı fetha alırdı."),
  tok("فِيهِ","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "«فِي» حَرْفُ جَرٍّ وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «لَا»، فَهُوَ ظَرْفٌ مُسْتَقَرٌّ.",
      "«fi» is a jarr letter and the ha is in the position of jarr — and the phrase attaches to the OMITTED khabar of «la», which makes it MUSTAQARR. Three words of Arabic, and one of them is not written at all.",
      "«فِي» cer harfi, hâ mahallen mecrûrdur — ve terkîb, «لَا»nın MAHZÛF haberine taalluk eder; öyleyse MÜSTAKARdır. Üç kelimelik Arapça, ve biri hiç yazılmamış.",
      segments=[seg("فِي","fi","prep"), seg("هِ","pron-3ms","pron")],
      punct="."),
 ],
 "jumal": [J("يَذْكُرُ آلِهَتَكُمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir."),
  J("لَا رَيْبَ فِيهِ",
   "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ.",
   "A nominal sentence, in the position of raf' as a second khabar, or in the position of nasb as a hal.",
   "İkinci haber olarak mahallen merfû, yahut hâl olarak mahallen mansub isim cümlesi.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "This is Zayd. That (middling) is Zayd. That (far) is Zayd. — Those are my fathers.",
 "tr": "Bu Zeyd'dir. Şu Zeyd'dir. O Zeyd'dir. — İşte onlar benim babalarımdır."},
 "tokens": [
  tok("هَذَا","hadha","pron",["asma-al-ishara","mubtada-khabar"],
      "اسْمُ إِشَارَةٍ لِلْقَرِيبِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "The demonstrative for what is NEAR, mabni on the sukun, in the position of raf' as the mubtada. Bare: no lam, no kaf.",
      "YAKIN için ism-i işaret; sükûn üzere mebnî, mahallen merfû mübtedâdır. Çıplak: ne lâm var ne kâf."),
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "The khabar in raf'.",
      "Merfû haber.",
      punct="."),
  tok("ذَاكَ","dhaka","pron",["asma-al-ishara","mubtada-khabar"],
      "اسْمُ إِشَارَةٍ لِلْمُتَوَسِّطِ — «ذَا» وَالْكَافُ لِلْخِطَابِ، بِلَا لَامٍ.",
      "The demonstrative for the MIDDLE distance — «dha» with the kaf of address and NO lam. The three sentences here differ by one word and by nothing else, and they say three different things about where a man is standing.",
      "ORTA mesafe için ism-i işaret — «ذَا» ve hitâb kâfı; LÂM yok. Buradaki üç cümle tek bir kelimede ve başka hiçbir şeyde farklıdır; ve bir adamın nerede durduğu hakkında üç ayrı şey söylerler."),
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "The khabar in raf'.",
      "Merfû haber.",
      punct="."),
  tok("ذَلِكَ","dhalika","pron",["asma-al-ishara","mubtada-khabar"],
      "اسْمُ إِشَارَةٍ لِلْبَعِيدِ — «ذَا» وَاللَّامُ لِلْبُعْدِ وَالْكَافُ لِلْخِطَابِ.",
      "The demonstrative for what is FAR — «dha», the lam of distance, and the kaf of address. Three letters of grammar bolted onto one demonstrative, and the middle one is the whole difference between this and the word before it.",
      "UZAK için ism-i işaret — «ذَا», uzaklık lâmı ve hitâb kâfı. Tek bir işaret ismine takılmış üç gramer harfi; ve ortadaki, bununla bir önceki kelime arasındaki bütün farktır."),
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ — وَالْخَبَرُ لَمْ يَتَغَيَّرْ فِي الثَّلَاثِ، وَإِنَّمَا تَغَيَّرَ الْمُسْنَدُ إِلَيْهِ.",
      "The khabar in raf' — and the khabar has not changed in any of the three. Only the musnad ilayh moved, which is the seventh chapter's thesis proved again with a different device.",
      "Merfû haber — ve haber üç cümlenin hiçbirinde değişmedi. Yalnız müsnedün ileyh yer değiştirdi; yedinci bâbın tezi, başka bir vasıtayla yeniden ispat edilmiş oluyor.",
      punct="."),
  tok("أُولَئِكَ","ulaika","pron",["asma-al-ishara","mubtada-khabar","tarif-al-musnad-ilayh"],
      "اسْمُ إِشَارَةٍ لِلْجَمْعِ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْإِشَارَةُ هُنَا لِلتَّعْرِيضِ بِغَبَاوَةِ السَّامِعِ.",
      "The PLURAL demonstrative, mabni, in the position of raf' as the mubtada — and the pointing is here a jab at the hearer's slowness: «THESE, the ones I have just listed, are my fathers — now bring me their like». Chapter 7 met this same word in the Baqara verse, where it was said for clarity; here the identical word is said to make a man feel small.",
      "CEMİ ism-i işaret; mahallen merfû mübtedâdır — ve işaret burada muhâtabın ağır anlayışına bir ta'rîzdir: «İŞTE ŞUNLAR, saydıklarım, benim babalarımdır; haydi bir benzerlerini getir». Yedinci bâb aynı kelimeyle Bakara âyetinde karşılaşmıştı, orada îzâh için söylenmişti; burada tıpatıp aynı kelime, bir adama küçüklüğünü hissettirmek için söyleniyor."),
  tok("آبَائِي","ab","noun",["mubtada-khabar","ya-al-mutakallim","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ وَالْيَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ تَكْسِيرٍ لِـ«أَب».",
      "The khabar in raf' by a damma ESTIMATED on the letter before the speaker's ya, a mudaf with the ya annexed — a broken plural of أَب. Note what the plural does to the five nouns: أَب declines by a WAW in the singular (أَبُوهُ) and by an ordinary damma once it is broken, because the five-noun rule is about those five words in the singular and nothing else.",
      "Merfû haber; ref' alâmeti, mütekellim yâsından önceki harfte MUKADDER dammedir; muzâftır, yâ muzâfun ileyhtir — «أَب»in cem'-i teksîri. Cemi'nin esmâ-i hamseye ne yaptığına dikkat: «أَب» müfredken VÂV ile i'râb alır («أَبُوهُ»), kırıldıktan sonra sıradan damme ile; zira esmâ-i hamse kāidesi o beş kelimenin yalnız müfredi hakkındadır.",
      punct="."),
 ],
 "jumal": [J("هَذَا زَيْدٌ",
   "جُمْلَةٌ اسْمِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, with no position in i'rab.",
   "İsim cümlesi; i'râbdan mahalli yoktur."),
  J("أُولَئِكَ آبَائِي",
   "جُمْلَةٌ اسْمِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, with no position in i'rab.",
   "İsim cümlesi; i'râbdan mahalli yoktur.")]})

GLOSS_ADD = {
 "ams":       g("أَمْسِ", None, "noun", "yesterday (a zarf, mabni on the kasra)", "dün (kesra üzere mebnî zarf)", 3),
 "wudu":      g("وُضُوء", "و ض أ", "noun", "the ritual ablution", "abdest", 3),
 "rawada":    g("رَاوَدَ", "ر و د", "verb", "to try to coax or lure (with عَنْ: away from)", "murâd almak istemek, ikna etmeye çalışmak (عَنْ ile)", 5, form="III"),
 "ghashiya":  g("غَشِيَ", "غ ش ي", "verb", "to cover, to overwhelm", "örtmek, kaplamak", 4, form="I"),
 "yamm":      g("يَمّ", "ي م م", "noun", "the sea", "deniz, yemm", 4),
 "kadhdhaba": g("كَذَّبَ", "ك ذ ب", "verb", "to call a liar, to deny the truth of", "yalanlamak, tekzîb etmek", 3, form="II"),
 "shuayb":    g("شُعَيْب", None, "propn", "Shu'ayb (the prophet)", "Şuayb (aleyhisselâm)", 3),
 "khasir":    g("خَاسِر", "خ س ر", "noun", "one who loses, a loser (ism fa'il)", "hüsrana uğrayan (ism-i fâil)", 3),
 "dhakara":   g("ذَكَرَ", "ذ ك ر", "verb", "to mention; (here) to speak of with blame", "anmak; (burada) ayıplayarak anmak", 2, form="I"),
 "rayb":      g("رَيْب", "ر ي ب", "noun", "doubt", "şüphe, reyb", 3),
 "hamza-istifham": g("أَ (هَمْزَةُ الِاسْتِفْهَام)", None, "part", "the interrogative hamza", "istifham hemzesi", 2),
 "an":        g("عَنْ", None, "prep", "from, away from (of moving away)", "-den (mücâveze)", 1),
 # COPIED from other packages, lemma-identical — a lex key is global.
 "alladhi":   g("الَّذِي", None, "pron", "the one who, which (masc. sg. relative)", "o ki (müfred müzekker ism-i mevsûl)", 2),
 "alladhina": g("الَّذِينَ", None, "pron", "those who (masc. pl. relative)", "onlar ki (cemi müzekker ism-i mevsûl)", 2),
 "kana":      g("كَانَ", "ك و ن", "verb", "to be (an incomplete verb)", "olmak, idi (nâkıs fiil)", 1, form="I"),
 "maa":       g("مَعَ", None, "noun", "with (a zarf — a noun, not a letter)", "ile, beraber (zarf — harf değil, isim)", 1),
 "rajul":     g("رَجُل", "ر ج ل", "noun", "man", "adam, er", 1, plural="رِجَال"),
 "alim":      g("عَالِم", "ع ل م", "noun", "learned, a scholar (ism fa'il)", "âlim (ism-i fâil)", 2, plural="عُلَمَاء"),
 "kharaja":   g("خَرَجَ", "خ ر ج", "verb", "to go out, to come out", "çıkmak", 1, form="I"),
 "insan":     g("إِنْسَان", "أ ن س", "noun", "a human being", "insan", 1, plural="نَاس"),
 "naqid":     g("نَاقِض", "ن ق ض", "noun", "one that breaks or undoes (ism fa'il)", "bozan, nakzeden (ism-i fâil)", 4),
 "bayt":      g("بَيْت", "ب ي ت", "noun", "house", "ev", 1, plural="بُيُوت"),
 "hadha":     g("هٰذَا", None, "pron", "this (near, masc. sg.)", "bu (yakın, müfred müzekker)", 1),
 "dhalika":   g("ذٰلِكَ", None, "pron", "that (far, masc. sg.)", "o (uzak, müfred müzekker)", 1),
 "dhaka":     g("ذَاكَ", None, "pron", "that (middle distance, masc. sg.)", "şu (orta mesafe, müfred müzekker)", 2),
 "kitab":     g("كِتَاب", "ك ت ب", "noun", "book, writing", "kitap", 1, plural="كُتُب"),
 "zayd":      g("زَيْد", None, "propn", "Zayd (a man's name)", "Zeyd (bir erkek adı)", 1),
 "ab":        g("أَب", "أ ب و", "noun", "father", "baba", 1, plural="آبَاء"),
 "ilah":      g("إِلَه", "أ ل ه", "noun", "a god, a deity", "ilah, tanrı", 2, plural="آلِهَة"),
 "pron-1p":   g("نَا", None, "pron", "we, us (attached)", "biz (muttasıl)", 1),
 "la-nafiya-lil-jins": g("لَا (النَّافِيَةُ لِلْجِنْس)", None, "part", "no ... at all (denies the whole genus)", "hiçbir ... yoktur (cinsini nefyeden lâ)", 4),
}

def build_morph():
    out = {}
    for pkg, lex in [("wasiyyat-abi-yusuf-l5", "kana"),
                     ("wasiyyat-abi-hanifa-samti", "kharaja")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    # رَاوَدَ — Form III sound.
    out["rawada"] = _sg.derived(_sg.B3, _sg.W3, "ُ", "رَاوَد", "رَاوِد", "رَاوِد",
                                "مُرَاوَدَة", "مُرَاوِد", maful="مُرَاوَد",
                                pmz="رُووِدَ", pmd="يُرَاوَدُ")
    # كَذَّبَ — Form II sound.
    out["kadhdhaba"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "كَذَّب", "كَذِّب", "كَذِّب",
                                   "تَكْذِيب", "مُكَذِّب", maful="مُكَذَّب",
                                   pmz="كُذِّبَ", pmd="يُكَذَّبُ")
    # ذَكَرَ — Form I sound, bab nasara.
    out["dhakara"] = _sg.sound1("nasara", "ذَكَر", "ذْكُر", "اُذْكُر", "ذِكْر", "ذَاكِر",
                                "مَذْكُور", "ذُكِرَ", "يُذْكَرُ")
    # غَشِيَ — Form I NAQIS YA'I of bab samia, and that bab needs the kasra mazi:
    # غَشِيَ / غَشِيَتْ but غَشُوا, exactly as رَضِيَ and بَقِيَ. `naqis1` builds the
    # rama-type mazi only, so this one is spelled out through `entry`.
    out["ghashiya"] = _sg.entry("مِنْ بَابِ سَمِعَ يَسْمَعُ — نَاقِصٌ يَائِيٌّ", "فَعِلَ يَفْعَلُ",
                                "غَشْي", "غَاشٍ (الْغَاشِي)",
                                _sg.mazi_naqis_kasra("غَشِ", "غَشُوا"),
                                _sg.mudari_naqis("َ", "غْش", "a"),
                                _sg.amr_naqis("اِغْش", "a"),
                                "يَغْشَى", "يَغْشَ", "تَغْشَ",
                                "مَغْشِيّ", "غُشِيَ", "يُغْشَى",
                                "نَاقِصٌ كَرَضِيَ: تَبْقَى الْيَاءُ مَكْسُورَةً فِي الْغَائِبِ — غَشِيَ، وَجَمْعُهُ غَشُوا.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/8.json").write_text(
    json.dumps({"chapter": 8, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 8 for c in man["chapters"]):
    man["chapters"].append({"n": 8, "title": TITLE8})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.8.0"
ADD_EN = (" Chapter 8 continues from the same file (lines ~712-790), which carries every one of its "
          "examples vowelled: the two prose sentences, Yusuf 12:23, Taha 20:78, al-A'raf 7:92, "
          "al-Anbiya 21:36, al-Baqara 2:2 and the هَذَا/ذَاكَ/ذَلِكَ triple with Farazdaq's line.")
ADD_TR = (" Sekizinci bâb aynı dosyadan (satır ~712-790) devam eder; o satırlar bâbın bütün "
          "misallerini harekeli olarak taşır: iki nesir cümlesi, Yûsuf 12:23, Tâhâ 20:78, A'râf 7:92, "
          "Enbiyâ 21:36, Bakara 2:2 ve Ferezdak'ın mısraıyla birlikte هَذَا/ذَاكَ/ذَلِكَ üçlüsü.")
if "21:36" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch8:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
