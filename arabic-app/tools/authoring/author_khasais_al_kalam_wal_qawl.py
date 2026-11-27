"""Author content/samples/khasais-al-kalam-wal-qawl — «الْكَلَامُ وَالْقَوْلُ», the shelf «مِنْ كُتُبِ الْعَرَبِيَّةِ» (v352-K), Level 5.

RECEIVED TEXT: Ibn Jinnī, al-Khaṣāʾiṣ (ed. al-Najjār; Shamela 9986), vol. 1 p. 18 (Shamela p. 17), the bāb «هذا باب القول على الفصل بين
الكلام والقول»: the part where the difference itself is stated — from «أما الكلام فكل لفظ مستقل بنفسه» to «هذا أصله.», whole. Before it the
bāb runs through the six orders of the roots ق و ل and ك ل م (pp. 1:5–18); after it, «ثم يتسع فيه …» (the wider uses of قول, pp. 1:18–33).
The exact passage: research/sources/khasais-al-kalam-wal-qawl-src.txt. No correction; KEPT AS PRINTED: «يسميه النحويين» (the e-text's
yāʾ where the doer wants «النحويون»; no second witness of the line was found), its final vowel left unwritten and the slip named in its
iʿrāb line. Every vowel is ours.
Run: python3 tools/authoring/author_khasais_al_kalam_wal_qawl.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from khasais_common import *

SLUG = "khasais-al-kalam-wal-qawl"
J = lambda s: "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + s
MH = (" — وَهُوَ مِثَالٌ مَحْكِيٌّ", " — a quoted example", " — hikâye edilen bir misal")
def SOUND(full, lex, ar, en, tr, p="،", wa=True):
    """a cited sound-word / noun-verb in the list after «نَحْوُ»: conjoined and quoted (maḥkī) — a built word, so no case is claimed for it (v330)"""
    t = X(full, lex, "noun", ["asma-al-afal-wal-aswat-wal-murakkabat", "hikayat-al-hal"] + (["atf-nasaq"] if wa else []),
          (WA_AR if wa else "") + ar + " — لَفْظٌ مَحْكِيٌّ فِي قَائِمَةِ الْأَمْثِلَةِ.",
          ("The waw conjoins; " if wa else "") + en + " — a word quoted in the list of examples.", ("«ve» + " if wa else "") + tr + " — misaller listesinde hikâye edilmiş bir lafız.", p=p, pre=("wa",) if wa else ())
    return t
def NAHW_(full="نَحْوُ", p=":"):
    return tok(full, "nahwa", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: ذٰلِكَ، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.",
               "The predicate of an omitted mubtada («that is»), in raf', annexed — what follows is its second term: «such as».", "Mahzûf mübtedânın («bu») haberi, merfû, muzâf — sonrası muzâfun ileyh: «gibi».", punct=p)

TITLES = [{"ar": "الْكَلَامُ وَالْقَوْلُ", "en": "Kalām and Qawl: Speech and Utterance", "tr": "Kelâm ve Kavl"}]
S1 = [
 SEN(1, "As for kalām (speech), it is every utterance that stands by itself and conveys its meaning.", "Kelâma gelince, o, kendi başına müstakil, mânasını ifade eden her lafızdır.",
 [tok("أَمَّا", "amma-tafsil", "part", ["amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "أَمَّا «as for», the particle of condition and detailing.", "«Emmâ» şart ve tafsîl harfi."),
  MUBTADA("الْكَلَامُ", "kalam"),
  X("فَكُلُّ", "kull", "noun", ["fa-khabar-mubtada", "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَكُلُّ خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fa falls in the answer of أَمَّا; «every» is the predicate, in raf', annexed.", "Fâ «emmâ»nın cevabındadır; «kullu» haber, merfû, muzâf.", pre=("fa",)),
  MUDAF_ILAYH("لَفْظٍ", "lafz"),
  NAAT("مُسْتَقِلٍّ", "mustaqill", "jarr", extra=["ism-fail"]),
  X("بِنَفْسِهِ", "bi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَفْسِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + J("بِـ«مُسْتَقِلٍّ»") + ".",
      "The ba is a jarr letter; «itself» is in jarr, annexed to «it» — the phrase hangs on «standing».", "Bâ cer harfi; «nefs» mecrûr, muzâf, zamir muzâfun ileyh — câr-mecrûr «müstakil»e müteallik.", p="،", pre=("bi",), enc="هِ", s="nafs", spos="noun"),
  NAAT("مُفِيدٍ", "mufid", "jarr", extra=["ism-fail"], note_ar=" — نَعْتٌ ثَانٍ لِـ«لَفْظٍ»", note_en=" — a second adjective of «utterance»", note_tr=" — «lafz»ın ikinci na'tı"),
  X("لِمَعْنَاهُ", "li", "prep", ["huruf-jarr", "ism-maqsur-manqus", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ" + J("بِـ«مُفِيدٍ»") + ".",
      "The lam is a jarr letter; «meaning» is in jarr by a kasra estimated on the alif, annexed to «its» — the phrase hangs on «conveying».", "Lâm cer harfi; «ma'nâ» elif üzerinde takdîrî kesre ile mecrûr, muzâf; zamir muzâfun ileyh — câr-mecrûr «müfîd»e müteallik.", p=".", pre=("li",), enc="هُ", s="mana", spos="noun")]),
 SEN(2, "It is what the grammarians call sentences (jumal), such as: «Zayd is your brother», «Muḥammad stood», «Saʿīd was struck», «In the house is your father», and ṣah, mah, ruwayda, and ḥāʾ and ʿāʾ among the sounds, and ḥassi, labbi, uffi and awwah.",
     "Nahivcilerin cümleler (cümel) dediği budur: «Zeyd kardeşindir», «Muhammed kalktı», «Saîd dövüldü», «Babası evdedir» gibi; ve sah, meh, ruveyde; seslerden hâ ve â; hassi, lebbi, uffi ve evveh.",
 [tok("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — يَعُودُ عَلَى الْكَلَامِ.", "The waw resumes; «it» (kalām) is the mubtada, in the seat of raf'.", "Vâv isti'nâf; «hüve» (kelâma döner) mübtedâ, mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "A relative noun built on sukun, in the seat of raf' as the predicate.", "İsm-i mevsûl, sükûn üzere mebnî, haber olarak mahallen merfû."),
  tok("يُسَمِّيهِ", "samma", "verb", ["form-ii-verbs", "naqis-verbs", "mafulayn", "al-bariz-al-muttasil"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ، وَهِيَ الْعَائِدُ؛ وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A present verb in raf' by a damma estimated on the ya (too heavy to show); «it» is its first object and the pronoun that returns; its doer follows — the clause is the ṣila.", "Muzâri, yâ üzerinde sıklet sebebiyle takdîrî damme ile merfû; «hu» birinci mef'ûl ve âid zamir; fâili sonra gelir — cümle sıladır.", segments=[seg("يُسَمِّي", "samma", "verb"), seg("هِ", "pron-3ms", "pron")]),
  tok("النَّحْوِيِّين", "nahwi", "noun", ["fail", "jam-mudhakkar-salim"], "فَاعِلٌ؛ كَذَا فِي النَّصِّ الْإِلِكْتُرُونِيِّ بِالْيَاءِ، وَحَقُّ الْفَاعِلِ الرَّفْعُ بِالْوَاوِ: «النَّحْوِيُّونَ» — فَأُبْقِيَ رَسْمُهُ كَمَا وَرَدَ وَلَمْ تُكْتَبْ حَرَكَةُ آخِرِهِ، وَهُوَ مَذْكُورٌ لِلْعَالِمِ الْمُرَاجِعِ.",
      "The doer. The e-text writes it with ya; as doer it should be in raf' with waw («al-naḥwiyyūna») — the letters are kept as received, the last vowel left unwritten, and the point is left for the scholar.", "Fâil; elektronik metinde yâ iledir, fâil olarak vâv ile merfû olması gerekir («en-nahviyyûne») — harfler geldiği gibi bırakıldı, son harekesi yazılmadı; hocaya bırakıldı."),
  tok("الْجُمَلَ", "jumla", "noun", ["mafulayn", "jam-taksir"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ جُمْلَةٍ.", "The second object, in nasb — the plural of جُمْلَة «sentence».", "İkinci mef'ûl, mansûb — «cümle»nin çoğulu.", punct="،"),
  NAHW_(),
  tok("زَيْدٌ", "zayd", "propn", ["mubtada-khabar", "hikayat-al-hal"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ مِثَالٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The mubtada, in raf' — the whole sentence is a quoted example, in the seat of jarr as the second term after «such as».", "Mübtedâ, merfû — cümle hikâye edilen misaldir, muzâfun ileyh olarak mahallen mecrûr."),
  X("أَخُوكَ", "akh", "noun", ["mubtada-khabar", "five-nouns", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The predicate, in raf' by the waw (one of the five nouns), annexed to «your».", "Haber, beş isimden olduğu için vâv ile merfû, muzâf; «ke» muzâfun ileyh.", p="،", enc="كَ"),
  X("وَقَامَ", "qama", "verb", ["hollow-verbs", "hikayat-al-hal"], WA_AR + "قَامَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مِثَالٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "The waw conjoins; «stood» is a past verb built on fatha — a quoted example, conjoined to the one before.", "«ve» + «kâme» fetha üzere mebnî mâzî — öncekine ma'tûf hikâye edilmiş misal.", pre=("wa",)),
  FAIL("مُحَمَّدٌ", "muhammad", "propn", punct="،"),
  X("وَضُرِبَ", "daraba", "verb", ["naib-al-fail", "hikayat-al-hal"], WA_AR + "ضُرِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — مِثَالٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "The waw conjoins; «was struck» is a passive past verb built on fatha — a quoted example, conjoined.", "«ve» + «duribe» meçhul mâzî — öncekine ma'tûf hikâye edilmiş misal.", pre=("wa",)),
  NAIB("سَعِيدٌ", "said-name", punct="،"),
  X("وَفِي", "fi", "prep", ["huruf-jarr", "hikayat-al-hal"], WA_AR + "فِي حَرْفُ جَرٍّ — مِثَالٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "The waw conjoins; فِي is a jarr letter — a quoted example, conjoined.", "«ve» + «fî» cer harfi — öncekine ma'tûf misal.", pre=("wa",)),
  MAJR("الدَّارِ", "dar", note_ar=J("بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ"), note_en=" — the phrase hangs on an omitted predicate placed first", note_tr=" — câr-mecrûr öne alınmış mahzûf habere müteallik"),
  X("أَبُوكَ", "ab", "noun", ["mubtada-khabar", "five-nouns", "al-bariz-al-muttasil"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "The mubtada placed after its predicate, in raf' by the waw (one of the five nouns), annexed to «your».", "Muahhar mübtedâ, beş isimden olduğu için vâv ile merfû, muzâf; «ke» muzâfun ileyh.", p="،", enc="كَ"),
  SOUND("وَصَهْ", "sah", "صَهْ اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى «اسْكُتْ» مَبْنِيٌّ عَلَى السُّكُونِ", "ṣah «hush!» is a noun-verb of command built on sukun", "«sah» (sus!) sükûn üzere mebnî emir ism-i fiili"),
  SOUND("وَمَهْ", "mah", "مَهْ اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى «اكْفُفْ» مَبْنِيٌّ عَلَى السُّكُونِ", "mah «stop!» is a noun-verb of command built on sukun", "«meh» (dur!) sükûn üzere mebnî emir ism-i fiili"),
  SOUND("وَرُوَيْدَ", "ruwayd", "رُوَيْدَ اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى «أَمْهِلْ» مَبْنِيٌّ عَلَى الْفَتْحِ", "ruwayda «go gently!» is a noun-verb of command built on fatha", "«ruveyde» (yavaş ol!) fetha üzere mebnî emir ism-i fiili"),
  SOUND("وَحَاء", "haa-sound", "حَاء اسْمُ صَوْتٍ يُزْجَرُ بِهِ الْإِبِلُ، مَبْنِيٌّ — وَلَمْ تُكْتَبْ حَرَكَةُ آخِرِهِ", "ḥāʾ is a sound-word with which camels are driven, built (indeclinable) — its last vowel is left unwritten", "«hâ» develeri sürmek için kullanılan ses ismi, mebnî — son harekesi yazılmadı", p=None),
  SOUND("وَعَاء", "aa-sound", "عَاء اسْمُ صَوْتٍ يُدْعَى بِهِ الضَّأْنُ، مَبْنِيٌّ — وَلَمْ تُكْتَبْ حَرَكَةُ آخِرِهِ", "ʿāʾ is a sound-word with which sheep are called, built (indeclinable) — its last vowel is left unwritten", "«â» koyunları çağırmak için kullanılan ses ismi, mebnî — son harekesi yazılmadı", p=None),
  PREP("فِي", "fi", gloss_tr="«-de»"),
  MAJR("الْأَصْوَاتِ", "sawt", extra=["jam-taksir"], note_ar=J("بِمَحْذُوفٍ حَالٍ مِنْ «حَاء» وَ«عَاء»، أَيْ: كَائِنَيْنِ فِي الْأَصْوَاتِ"), note_en=" — the phrase hangs on an omitted hal of ḥāʾ and ʿāʾ («being among the sounds»)", note_tr=" — câr-mecrûr «hâ» ve «â»dan mahzûf hâle müteallik", punct="،"),
  SOUND("وَحَسِّ", "hassi", "حَسِّ اسْمُ صَوْتٍ يَقُولُهُ الْمُتَوَجِّعُ، مَبْنِيٌّ عَلَى الْكَسْرِ", "ḥassi, the cry of one in pain, is a sound-word built on kasra", "«hassi» acı duyanın söylediği ses ismi, kesre üzere mebnî"),
  SOUND("وَلَبِّ", "labbi", "لَبِّ بِمَعْنَى «لَبَّيْكَ» فِي لُغَةِ بَعْضِ الْعَرَبِ، مَبْنِيٌّ عَلَى الْكَسْرِ كَأَمْسِ وَغَاقِ", "labbi, «at your service» in the speech of some Arabs, built on kasra like أَمْسِ and غَاقِ", "«lebbi», bazı Araplarda «lebbeyk» anlamında, «emsi» ve «gâki» gibi kesre üzere mebnî"),
  SOUND("وَأُفِّ", "uff", "أُفِّ اسْمُ فِعْلٍ مُضَارِعٍ بِمَعْنَى «أَتَضَجَّرُ» مَبْنِيٌّ عَلَى الْكَسْرِ", "uffi «fie!» is a noun-verb meaning «I am vexed», built on kasra", "«uffi» (öf!) «bıktım» anlamında muzâri ism-i fiili, kesre üzere mebnî"),
  SOUND("وَأَوَّهْ", "awwah", "أَوَّهْ اسْمُ فِعْلٍ مُضَارِعٍ بِمَعْنَى «أَتَوَجَّعُ» مَبْنِيٌّ عَلَى السُّكُونِ", "awwah «alas!» is a noun-verb meaning «I am in pain», built on sukun", "«evveh» (ah!) «acı duyuyorum» anlamında muzâri ism-i fiili, sükûn üzere mebnî", p=".")]),
 SEN(3, "So every utterance that stands by itself, and from which the fruit of its meaning is gathered, is kalām.", "Kendi başına müstakil olan ve mânasının meyvesi kendisinden devşirilen her lafız kelâmdır.",
 [X("فَكُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fa resumes; «every» is the mubtada, in raf', annexed.", "Fâ isti'nâf; «kullu» mübtedâ, merfû, muzâf.", pre=("fa",)),
  MUDAF_ILAYH("لَفْظٍ", "lafz"),
  tok("اسْتَقَلَّ", "istaqalla", "verb", ["form-x-verbs", "doubled-verbs", "jumla-sifa"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«لَفْظٍ».", "A past verb built on fatha; its doer is the hidden «it» — the clause qualifies «utterance», in the seat of jarr.", "Fetha üzere mebnî mâzî; fâili gizli «hüve» — cümle «lafz»ın na'tı, mahallen mecrûr."),
  X("بِنَفْسِهِ", "bi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَفْسِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ" + J("بِـ«اسْتَقَلَّ»") + ".", "The ba is a jarr letter with «itself» — the phrase hangs on «stands».", "Bâ cer harfi, «nefsi» — câr-mecrûr «istakalle»ye müteallik.", p="،", pre=("bi",), enc="هِ", s="nafs", spos="noun"),
  X("وَجُنِيَتْ", "jana-v-hr", "verb", ["naib-al-fail", "naqis-verbs", "atf-nasaq"], WA_AR + "جُنِيَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ بَعْدَهُ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «اسْتَقَلَّ».",
      "The waw conjoins; «was gathered» is a passive past verb built on fatha, the ta marking the feminine; its deputy doer follows — the clause is conjoined to «stands».", "«ve» + «cüniyet» meçhul mâzî, tâ te'nîs; nâib-i fâili sonra — cümle «istakalle»ye ma'tûf.", pre=("wa",)),
  X("مِنْهُ", "min", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى اللَّفْظِ" + J("بِـ«جُنِيَتْ»") + ".", "A jarr letter with «it» (the utterance) — the phrase hangs on «was gathered».", "Cer harfi, zamir (lafza döner) — câr-mecrûr «cüniyet»e müteallik.", enc="هُ"),
  NAIB("ثَمَرَةُ", "thamara", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  X("مَعْنَاهُ", "mana", "noun", ["idafa-definiteness", "ism-maqsur-manqus", "al-bariz-al-muttasil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The second term of the idafa, in jarr by a kasra estimated on the alif, annexed to «its».", "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr, muzâf; zamir muzâfun ileyh.", p="،", enc="هُ"),
  tok("فَهُوَ", "huwa", "pron", ["fa-khabar-mubtada", "mubtada-khabar"], "الْفَاءُ رَابِطَةٌ لِلْخَبَرِ لِشَبَهِ الْمُبْتَدَإِ بِالشَّرْطِ فِي الْعُمُومِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ ثَانٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «كُلُّ».",
      "The fa ties the predicate on, since a general mubtada resembles a condition; «it» is a second mubtada — the clause is the predicate of «every», in the seat of raf'.", "Fâ, umumîlikte şarta benzeyen mübtedânın haberine râbıtadır; «hüve» ikinci mübtedâ — cümle «kullu»nun haberi, mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  KHABAR("كَلَامٌ", "kalam", punct=".")]),
 SEN(4, "As for qawl (utterance), its root sense is that it is every utterance the tongue moves lightly with, whether complete or incomplete.", "Kavle gelince, onun aslı, dilin onunla kıpırdadığı her lafız olmasıdır; tam olsun eksik olsun.",
 [X("وَأَمَّا", "amma-tafsil", "part", ["amma-tafsiliyya"], WA_AR + "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "The waw conjoins; أَمَّا «as for» is the particle of condition and detailing.", "«ve» + «emmâ» şart ve tafsîl harfi.", pre=("wa",)),
  MUBTADA("الْقَوْلُ", "qawl"),
  X("فَأَصْلُهُ", "asl", "noun", ["fa-khabar-mubtada", "mubtada-khabar", "al-bariz-al-muttasil"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَأَصْلُ مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ خَبَرُ «الْقَوْلُ».",
      "The fa falls in the answer of أَمَّا; «its root» is a second mubtada, in raf', annexed to «its» — the clause is the predicate of «qawl».", "Fâ «emmâ»nın cevabında; «asl» ikinci mübtedâ, merfû, muzâf — cümle «el-kavl»in haberi.", pre=("fa",), enc="هُ"),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna", "al-bariz-al-muttasil"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا يَعُودُ عَلَى الْقَوْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَصْلُهُ».",
      "أَنَّ with «it» (qawl) as its noun — the masdar it makes is the predicate of «its root», in the seat of raf'.", "«Enne», «hu» (kavle döner) ismi — te'vîlî masdar «asluhu»nun haberi, mahallen merfû.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("كُلُّ", "kull", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The predicate of أَنَّ, in raf', annexed.", "Enne'nin haberi, merfû, muzâf."),
  MUDAF_ILAYH("لَفْظٍ", "lafz"),
  tok("مَذِلَ", "madhila", "verb", ["thulathi-mujarrad-babs", "jumla-sifa"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«لَفْظٍ»؛ وَمَذِلَ بِالشَّيْءِ: قَلِقَ بِهِ وَلَمْ يَسْتَقِرَّ.",
      "A past verb built on fatha; its doer follows — the clause qualifies «utterance», in the seat of jarr. مَذِلَ بِهِ: to be restless with a thing, to move lightly with it.", "Fetha üzere mebnî mâzî; fâili sonra — cümle «lafz»ın na'tı, mahallen mecrûr. «Mezile bihî»: onunla kıpırdadı, duramadı."),
  X("بِهِ", "bi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى اللَّفْظِ، وَهُوَ الْعَائِدُ" + J("بِـ«مَذِلَ»") + ".", "The ba is a jarr letter with «it» (the utterance), the pronoun that returns — the phrase hangs on «moves».", "Bâ cer harfi, zamir (lafza döner, âid) — câr-mecrûr «mezile»ye müteallik.", enc="هِ"),
  FAIL("اللِّسَانُ", "lisan", punct="،"),
  tok("تَامًّا", "tamm", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of كَانَ placed first, in nasb.", "Kâne'nin öne alınmış haberi, mansûb."),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "hal"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى اللَّفْظِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "The defective past verb; its noun is the hidden «it» (the utterance) — the clause is a hal, in the seat of nasb.", "Nâkıs mâzî; ismi gizli «hüve» (lafız) — cümle hâl, mahallen mansûb."),
  tok("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّسْوِيَةِ مَبْنِيٌّ عَلَى السُّكُونِ.", "أَوْ «or», conjoining two equal choices.", "«Ev» (veya) atıf harfi."),
  tok("نَاقِصًا", "naqis", "noun", ["atf-nasaq", "ism-fail"], "مَعْطُوفٌ عَلَى «تَامًّا» مَنْصُوبٌ بِالْفَتْحَةِ.", "Conjoined to «complete», in nasb.", "«Tâmmen»e ma'tûf, mansûb.", punct=".")]),
 SEN(5, "The complete is what conveys a meaning — I mean the sentence and whatever has its sense, such as ṣahin and īhin.", "Tam olan, ifade eden (müfîd) lafızdır; yani cümle ve onun mânasında olan, «sahin» ve «îhin» gibi.",
 [X("فَالتَّامُّ", "tamm", "noun", ["mubtada-khabar", "ism-fail"], "الْفَاءُ لِلتَّفْصِيلِ، وَالتَّامُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The fa details; «the complete» is the mubtada, in raf'.", "Fâ tafsîl içindir; «et-tâmm» mübtedâ, merfû.", pre=("fa",)),
  tok("هُوَ", "huwa", "pron", ["damir-fasl"], "ضَمِيرُ فَصْلٍ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "A pronoun of separation (ḍamīr al-faṣl), with no seat: it marks what follows as the predicate.", "Fasıl zamiri, i'râbdan mahalli yoktur: sonrasının haber olduğunu belirtir."),
  KHABAR("الْمُفِيدُ", "mufid", extra=["ism-fail"], punct="،"),
  tok("أَعْنِي", "ana-mean", "verb", ["naqis-verbs", "jumla-mutarida"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّفْسِيرِ لَا مَحَلَّ لَهَا.",
      "A present verb in raf' by a damma estimated on the ya; its doer is the hidden «I» — the clause is put in to explain, with no seat.", "Muzâri, yâ üzerinde takdîrî damme ile merfû; fâili vücûben gizli «ene» — cümle açıklama için araya girmiştir, mahalli yoktur."),
  MAFUL("الْجُمْلَةَ", "jumla"),
  tok("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى «الْجُمْلَةَ».", "The waw conjoins; «what» is a relative built on sukun, in the seat of nasb, conjoined to «the sentence».", "Vâv atıf; «mâ» ism-i mevsûl, mahallen mansûb, «el-cümle»ye ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "The defective past verb; its noun is the hidden «it» (the «what») — the clause is the ṣila.", "Nâkıs mâzî; ismi gizli «hüve» («mâ») — cümle sıladır."),
  PREP("فِي", "fi", gloss_tr="«-de»"),
  X("مَعْنَاهَا", "mana", "noun", ["huruf-jarr", "ism-maqsur-manqus", "al-bariz-al-muttasil"], "مَجْرُورٌ بِـ«فِي» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْجُمْلَةِ" + J("بِمَحْذُوفٍ خَبَرِ «كَانَ»") + ".",
      "In jarr after فِي by a kasra estimated on the alif, annexed to «its» (the sentence's) — the phrase hangs on the omitted predicate of كَانَ.", "«fî» ile elif üzerinde takdîrî kesre ile mecrûr, muzâf; zamir (cümleye döner) — câr-mecrûr «kâne»nin mahzûf haberine müteallik.", p="،", enc="هَا"),
  PREP("مِنْ", "min", "، بَيَانِيَّةٌ", " that explains", gloss_tr="«-den»", role_tr=" (beyân)"),
  MAJR("نَحْوِ", "nahwa", note_ar="، مُضَافٌ" + J("بِمَحْذُوفٍ حَالٍ مِنْ «مَا»"), note_en=", annexed — the phrase hangs on an omitted hal of «what»: «such as»", note_tr=", muzâf — câr-mecrûr «mâ»dan mahzûf hâle müteallik", punct=":"),
  SOUND("صَهٍ", "sah", "صَهٍ اسْمُ فِعْلِ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِلتَّنْوِينِ، وَتَنْوِينُهُ لِلتَّنْكِيرِ (اسْكُتْ سُكُوتًا مَا)", "ṣahin, with the tanwin of indefiniteness («hush — any hushing»), a noun-verb of command", "«sahin» tenkîr tenvini ile emir ism-i fiili («herhangi bir susuş sus»)", wa=False),
  SOUND("وَإِيهٍ", "iha", "إِيهٍ اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى «زِدْنِي حَدِيثًا» مَبْنِيٌّ عَلَى الْكَسْرِ، وَتَنْوِينُهُ لِلتَّنْكِيرِ", "īhin «go on (with any talk)!», a noun-verb of command with the tanwin of indefiniteness", "«îhin» («herhangi bir sözü sürdür!») tenkîr tenvinli emir ism-i fiili", p=".")]),
 SEN(6, "The incomplete is what is the opposite of that, such as «Zayd», «Muḥammad», «inna», and «kāna your brother» — when it is the kāna of time, not the kāna of event.", "Eksik olan ise bunun zıddı olandır: «Zeyd», «Muhammed», «inne» ve «kâne ahûke» gibi — kâne zaman bildiren (nâkıs) olup olay bildiren (tâm) olmadığında.",
 [ATF("وَالنَّاقِصُ", "naqis", note_ar=" — وَهُوَ مُبْتَدَأٌ", note_en=" — it is a mubtada", note_tr=" — mübtedâdır"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "A relative «what», in the seat of raf' as the predicate.", "İsm-i mevsûl «mâ», haber olarak mahallen merfû."),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "The defective past verb; its noun is the hidden «it» — the clause is the ṣila.", "Nâkıs mâzî; ismi gizli «hüve» — cümle sıladır."),
  X("بِضِدِّ", "bi", "prep", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَضِدِّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ" + J("بِمَحْذُوفٍ خَبَرِ «كَانَ»") + ".", "The ba is a jarr letter; «opposite» is in jarr, annexed — the phrase hangs on the omitted predicate of كَانَ.", "Bâ cer harfi; «zıdd» mecrûr, muzâf — câr-mecrûr «kâne»nin mahzûf haberine müteallik.", pre=("bi",), s="didd", spos="noun"),
  ISHARA("ذٰلِكَ", "dhalika", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr", punct="،"),
  NAHW_(),
  MUDAF_ILAYH("زَيْدٍ", "zayd", "propn", punct="،"),
  ATF("وَمُحَمَّدٍ", "muhammad", "propn", case="jarr", punct="،"),
  X("وَإِنَّ", "inna", "part", ["inna-wa-akhawatuha", "hikayat-al-hal", "atf-nasaq"], WA_AR + "إِنَّ لَفْظٌ مَحْكِيٌّ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ مَعْطُوفٌ عَلَى «زَيْدٍ».", "The waw conjoins; «inna» is a quoted word, built on fatha, in the seat of jarr, conjoined to «Zayd».", "«ve» + «inne» hikâye edilmiş lafız, fetha üzere mebnî, mahallen mecrûr, «Zeyd»e ma'tûf.", p="،", pre=("wa",)),
  X("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "hikayat-al-hal"], WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ — وَالْقَوْلُ «كَانَ أَخُوكَ» مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مَعْطُوفٌ؛ وَهُوَ نَاقِصٌ لِأَنَّ خَبَرَهُ لَمْ يُذْكَرْ.",
      "The waw conjoins; كَانَ is the defective past verb — «kāna your brother» is quoted, in the seat of jarr, conjoined; it is incomplete because its predicate is not given.", "«ve» + «kâne» nâkıs mâzî — «kâne ahûke» hikâye edilmiş, mahallen mecrûr, ma'tûf; haberi zikredilmediği için eksik bir sözdür.", pre=("wa",)),
  X("أَخُوكَ", "akh", "noun", ["kana-wa-akhawatuha", "five-nouns", "al-bariz-al-muttasil"], "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "The noun of كَانَ, in raf' by the waw (one of the five nouns), annexed to «your».", "Kâne'nin ismi, beş isimden olduğu için vâv ile merfû, muzâf; «ke» muzâfun ileyh.", p="،", enc="كَ"),
  tok("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ خَافِضٌ لِشَرْطِهِ، مَبْنِيٌّ عَلَى السُّكُونِ — وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "إِذَا «when», a ẓarf of time with the force of a condition; its answer is omitted, shown by what came before.", "«İzâ» şart anlamlı zaman zarfı; cevabı mahzûf, öncesi ona delâlet eder."),
  tok("كَانَتِ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى «كَانَ» (الْكَلِمَةِ) — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
      "The defective past verb; the ta marks the feminine (kasra before the sukun); its noun is the hidden «she» — the word kāna — and the clause is in the seat of jarr, annexed to إِذَا.", "Nâkıs mâzî; tâ te'nîs (kesre aldı); ismi gizli «hiye» (kâne kelimesi) — cümle «izâ»ya muzâfun ileyh olarak mahallen mecrûr."),
  KHK("الزَّمَانِيَّةَ", "zamaniyya", extra=["ism-mansub"]),
  tok("لَا", "la", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ وَنَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "لَا «not», conjoining and negating.", "«Lâ» atıf ve nefy harfi."),
  ATF("الْحَدَثِيَّةَ", "hadathiyya", case="nasb", extra=["ism-mansub"], punct=".")]),
 SEN(7, "So every kalām is qawl, but not every qawl is kalām.", "Öyleyse her kelâm kavldir, fakat her kavl kelâm değildir.",
 [X("فَكُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fa resumes; «every» is the mubtada, in raf', annexed.", "Fâ isti'nâf; «kullu» mübtedâ, merfû, muzâf.", pre=("fa",)),
  MUDAF_ILAYH("كَلَامٍ", "kalam"), KHABAR("قَوْلٌ", "qawl", punct="،"),
  X("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "atf-nasaq"], WA_AR + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ.", "The waw conjoins; لَيْسَ «is not» is the rigid defective verb.", "«ve» + «leyse» câmid nâkıs fiil.", pre=("wa",)),
  tok("كُلُّ", "kull", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ لَيْسَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of لَيْسَ, in raf', annexed.", "Leyse'nin ismi, merfû, muzâf."),
  MUDAF_ILAYH("قَوْلٍ", "qawl"),
  tok("كَلَامًا", "kalam", "noun", ["kana-wa-akhawatuha"], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of لَيْسَ, in nasb.", "Leyse'nin haberi, mansûb.", punct=".")]),
 SEN(8, "This is its root sense.", "Bunun aslı budur.",
 [ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "mübtedâ — merfû"),
  X("أَصْلُهُ", "asl", "noun", ["mubtada-khabar", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْقَوْلِ.", "The predicate, in raf', annexed to «its» (qawl).", "Haber, merfû, muzâf; zamir (kavle döner) muzâfun ileyh.", p=".", enc="هُ")]),
]

NEW_GLOSS = {
 "nahwi": NN("نَحْوِيّ", "ن ح و", "a grammarian (pl. النَّحْوِيُّونَ)", "nahivci (çoğ. en-nahviyyûn)", level=6),
 "thamara": NN("ثَمَرَة", "ث م ر", "a fruit; the yield of a thing", "meyve; bir şeyin semeresi", level=5),
 "madhila": NV("مَذِلَ", "م ذ ل", "I", "to be restless with, to move lightly with (مَذِلَ بِهِ اللِّسَانُ: the tongue moved with it)", "kıpırdamak, duramamak (dil onunla kıpırdadı)", level=6),
 "haa-sound": NN("حَاء", "ح و ء", "ḥāʾ — a sound-word with which camels are driven", "hâ — develeri sürmek için çıkarılan ses", level=6),
 "aa-sound": NN("عَاء", "ع و ء", "ʿāʾ — a sound-word with which sheep are called", "â — koyunları çağırmak için çıkarılan ses", level=6),
 "hassi": NN("حَسِّ", "ح س س", "ḥassi — the cry of one who feels a sudden pain", "hassi — ani bir acı duyanın sesi", level=6),
 "labbi": NN("لَبِّ", "ل ب ب", "labbi — «at your service» (= لَبَّيْكَ) in the speech of some Arabs", "lebbi — bazı Araplarda «lebbeyk» (buyur)", level=6),
 "uff": NN("أُفّ", "أ ف ف", "uff — «fie!», a word of vexation (a noun-verb)", "öf! — bıkkınlık sözü (ism-i fiil)", level=5),
 "awwah": NN("أَوَّهْ", "أ و ه", "awwah — «alas!», a word of pain (a noun-verb)", "evveh — ah!, acı sözü (ism-i fiil)", level=6),
 "iha": NN("إِيهِ", "أ ي ه", "īhi — «go on!» (with talk); إِيهٍ with tanwin: go on with any talk", "îhi — «devam et!» (söze); tenvinle: herhangi bir söze devam et", level=6),
 "zamaniyya": NN("زَمَانِيَّة", "ز م ن", "of time — said of كَانَ when it is defective (it gives the time of its predicate)", "zamanî — nâkıs kâne için (haberinin zamanını bildirir)", level=6),
 "hadathiyya": NN("حَدَثِيَّة", "ح د ث", "of event — said of كَانَ when it is complete (it means «happened»)", "hadesî — tâm kâne için («oldu, meydana geldi»)", level=6),
}
GLOSS_HERE = {
 "jana-v-hr": ("to pluck, to gather (fruit); to commit (a crime) — جَنَى يَجْنِي", "(meyve) devşirmek; (suç) işlemek — cenâ yecnî"),
 "nahwa": ("such as, like (the noun نَحْو, annexed to the example)", "gibi (örneğe muzâf «nahv» ismi)"),
}
V = {"madhila": SG.sound1("samia", "مَذِل", "مْذَل", "اِمْذَل", "مَذَل", "مَاذِل")}
FOR_HOCA = [
 ("«يُسَمِّيهِ النَّحْوِيِّين» — KEPT AS PRINTED: the e-text has the yāʾ where the doer wants «النَّحْوِيُّونَ»; no second witness of the line was found, so the letters stand and the last vowel is left unwritten", "«يُسَمِّيهِ النَّحْوِيِّين» — BASKIDAKİ GİBİ: fâilin «en-nahviyyûne» olması gerekirken elektronik metinde yâ var; ikinci bir şâhit bulunamadı, harfler korundu, son hareke yazılmadı"),
 ("the sound-words «حَاء» and «عَاء»: their final vowel left unwritten", "«حَاء» ve «عَاء» ses isimleri: son harekeleri yazılmadı"),
 ("«حَسِّ، لَبِّ، أُفِّ، أَوَّهْ»: the vowelling of these sound-words follows the lexicon's common form (each has others)", "«حَسِّ، لَبِّ، أُفِّ، أَوَّهْ»: bu ses isimleri sözlüğün yaygın şekliyle harekelendi (başka şekilleri de var)"),
 ("«مَذِلَ بِهِ اللِّسَانُ»: مَذِلَ (Lisān; مَذَلَ is also given)", "«مَذِلَ بِهِ اللِّسَانُ»: mezile (Lisân; mezele de vardır)"),
 ("«وَضُرِبَ سَعِيدٌ» read in the passive (a complete sentence, as the list requires)", "«وَضُرِبَ سَعِيدٌ» meçhul okundu (listenin gerektirdiği tam cümle)"),
]
MANIFEST = manifest(SLUG, level=5, title=TITLES[0],
    subtitle={"ar": "الْفَرْقُ بَيْنَ الْكَلَامِ وَالْقَوْلِ — مِنْ «الْخَصَائِصِ» لِابْنِ جِنِّي، نَصٌّ مَنْقُولٌ بِلَفْظِهِ", "en": "The difference between kalām and qawl — from Ibn Jinnī's al-Khaṣāʾiṣ, the received text, word for word", "tr": "Kelâm ile kavl arasındaki fark — İbn Cinnî'nin el-Hasâis'inden, lafzıyla"},
    bab_ar="هٰذَا بَابُ الْقَوْلِ عَلَى الْفَصْلِ بَيْنَ الْكَلَامِ وَالْقَوْلِ", bab_en="On the distinction between kalām and qawl", bab_tr="Kelâm ile kavl arasındaki fark üzerine", vol=1, pages="18", shamela="17",
    span_en="the part where the difference itself is stated, from «أما الكلام فكل لفظ مستقل بنفسه» to «هذا أصله.», whole",
    span_tr="farkın bizzat anlatıldığı kısım, «أما الكلام فكل لفظ مستقل بنفسه»dan «هذا أصله.» sözüne kadar, tamamen",
    span_ar="مِنْ «أَمَّا الْكَلَامُ فَكُلُّ لَفْظٍ مُسْتَقِلٍّ بِنَفْسِهِ» إِلَى «هٰذَا أَصْلُهُ»",
    left_en="what comes before (pp. 1:5–18: the six orders of the roots ق و ل and ك ل م and what each means) and after («ثم يتسع فيه …», the wider uses of qawl, pp. 1:18–33)",
    left_tr="öncesi (s. 1:5–18: ق و ل ve ك ل م köklerinin altı dizilişi ve anlamları) ve sonrası («ثم يتسع فيه …», kavlin geniş kullanımları, s. 1:18–33)",
    left_ar="مَا قَبْلَهُ مِنْ تَقَالِيبِ «ق و ل» وَ«ك ل م» وَمَا بَعْدَهُ مِنَ اتِّسَاعِهِمْ فِي «الْقَوْلِ»",
    extra_en="KEPT AS PRINTED: «يسميه النحويين» (the doer written with yāʾ; its last vowel left unwritten, the slip named in its iʿrāb line). ",
    extra_tr="BASKIDAKİ GİBİ BIRAKILAN: «يسميه النحويين» (fâil yâ ile yazılmış; son harekesi yazılmadı, hata i'râb satırında belirtildi). ",
    extra_ar="وَأُبْقِيَ كَمَا وَرَدَ: «يسميه النحويين» بِالْيَاءِ، وَنُبِّهَ عَلَيْهِ فِي إِعْرَابِهِ. ",
    hoca=FOR_HOCA)
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
