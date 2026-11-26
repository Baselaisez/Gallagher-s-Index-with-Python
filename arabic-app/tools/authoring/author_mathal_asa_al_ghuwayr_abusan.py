"""Author content/samples/mathal-asa-al-ghuwayr-abusan — «عَسَى الْغُوَيْرُ أَبْؤُسًا», the proverbs' shelf (v348-A), Level 5.

RECEIVED TEXT: Abū ʿUbayd's proverb (bāb of suspicion) and Ibn al-Kalbī's report of al-Zabbāʾ and Qaṣīr's caravan, from al-Bakrī's
commentary, «فصل المقال» (Shamela 1025, p. 436 = printed 1:424). The exact passage: research/sources/mathal-asa-al-ghuwayr-abusan-src.txt.
The tale from «وقال ابن الكلبي: الغوير» to «حين أخذ على غير الطريق»; the chapter closes with the sentence in which the book says where the
proverb is said — al-Aṣmaʿī's «فصار مثلاً لكل شيء يخاف أن يأتي منه شر», which in the book stands before Ibn al-Kalbī's report.
CORRECTION (one): «الزبى» → «الزَّبَّاءُ», against the edition's own apparatus (note 2 on p. 436: manuscript ص reads «الزباء», and the
editor: «فتغييره أولى»). Every vowel is ours. «عسى» here governs like كَانَ, as al-Bakrī himself says right after («وتشبه عسى بكان …
وعلى هذا أتى المثل»).
Run: python3 tools/authoring/author_mathal_asa_al_ghuwayr_abusan.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-asa-al-ghuwayr-abusan"
ZB = ("الزَّبَّاءِ", "al-Zabbāʾ", "Zebbâ")
QS = ("قَصِيرٍ", "Qaṣīr", "Kasîr")
def GHUWAYR(role, punct=None, note=("", "", "")):
    dim = (" — تَصْغِيرُ «الْغَارِ»", " — the diminutive of الْغَار «the cave»", " — «gār» (mağara) kelimesinin tasgîri")
    if role == "ism_asa": return tok("الْغُوَيْرُ", "ghuwayr", "propn", ["afal-al-muqaraba"], "اسْمُ عَسَى مَرْفُوعٌ بِالضَّمَّةِ" + dim[0] + note[0] + ".", "The noun of عَسَى, in raf'" + dim[1] + note[1] + ".", "Asâ'nın ismi, merfû" + dim[2] + note[2] + ".", punct=punct)
    if role == "mub": return MUBTADA("الْغُوَيْرُ", "ghuwayr", "propn", note_ar=dim[0], note_en=dim[1], note_tr=dim[2], punct=punct)
    if role == "majr": return MAJR("الْغُوَيْرِ", "ghuwayr", "propn", punct=punct)
def ASA_HEAD(full="عَسَى", note=("", "", "")):
    return tok(full, "asa-hope", "verb", ["afal-al-muqaraba", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مِنْ أَفْعَالِ الرَّجَاءِ، مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، يَعْمَلُ هُنَا عَمَلَ كَانَ: يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + note[0] + ".",
        "A defective, frozen past verb of hope, built on a fatha estimated on the alif; here it governs like كَانَ — it raises its noun and puts its predicate in nasb" + note[1] + ".",
        "Recâ bildiren nâkıs, câmid mâzî; elif üzerinde takdîrî fetha ile mebnî; burada kâne gibi amel eder: ismini ref, haberini nasb eder" + note[2] + ".")
def ABUSAN(punct=None):
    return tok("أَبْؤُسًا", "bus", "noun", ["afal-al-muqaraba", "jam-taksir"], "خَبَرُ عَسَى مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ بُؤْسٍ، أَيْ: شُرُورًا.", "The predicate of عَسَى, in nasb — the plural of بُؤْس «misery»: «evils».", "Asâ'nın haberi, mansûb — bü's'ün (sıkıntı) çoğulu: «belâlar».", punct=punct)

TITLES = [{"ar": "عَسَى الْغُوَيْرُ أَبْؤُسًا", "en": "The Little Cave May Bring Evils", "tr": "Belki de Mağaracıktan Belâlar Gelir"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "The little cave may well bring evils.", "tr": "Belki de bu mağaracıktan belâlar çıkar."},
 "tokens": [ASA_HEAD(note=HEAD_CL), GHUWAYR("ism_asa"), ABUSAN(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "Ibn al-Kalbī said: al-Ghuwayr is a well-known water of the tribe of Kalb, in the region of al-Samāwa.", "tr": "İbnü'l-Kelbî dedi ki: Guveyr, Kelb kabilesine ait bilinen bir sudur; Semâve tarafındadır."},
 "tokens": [QALA("وَقَالَ", punct=None), FAIL("ابْنُ", "ibn", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), NM("الْكَلْبِيِّ", "kalbi", (" — هِشَامُ بْنُ مُحَمَّدٍ النَّسَّابَةُ", " — Hishām ibn Muḥammad, the genealogist", " — neseb âlimi Hişâm b. Muhammed"), punct=":"),
  NOTE(GHUWAYR("mub"), " — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", "; the sentence is what is said", "; cümle mekūlü'l-kavl"),
  KHABAR("مَاءٌ", "ma-water", punct=None),
  tok("لِكَلْبٍ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ لِلْمِلْكِ، وَكَلْبٍ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ قَبِيلَةٍ مُنْصَرِفٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَاءٌ».",
      "The lam of ownership, a jarr letter; Kalb, the tribe's name, is in jarr and fully declined — the phrase hangs on an omitted adjective of «water».", "Lâm mülk içindir (cer harfi); Kelb (kabile adı, munsarif) mecrûr — câr-mecrûr «su»nun mahzûf na'tına müteallik.", segments=[seg("لِ", "li", "prep"), seg("كَلْبٍ", "kalb-tribe", "propn")]),
  NAAT("مَعْرُوفٌ", "maruf", note_ar=" — نَعْتٌ ثَانٍ لِـ«مَاءٌ»، اسْمُ مَفْعُولٍ مِنْ عَرَفَ", note_en=" — a second adjective of «water»: the passive participle of عَرَفَ, «well known»", note_tr=" — «su»nun ikinci na'tı; arafe'nin ism-i mef'ûlü: «bilinen»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — يَعُودُ عَلَى الْغُوَيْرِ.", "The waw conjoins; «it» (al-Ghuwayr) is a detached pronoun, the mubtada, in the seat of raf'.", "«ve» + «o» (Guveyr) munfasıl zamir, mübtedâ, mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  BI_NOUN("بِنَاحِيَةِ", "nahiya", "نَاحِيَةِ", note_ar="، مُضَافٌ — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ", note_en="; annexed — the ba means «in»; the phrase hangs on an omitted predicate", note_tr="; muzâf — bâ «fî» anlamında; câr-mecrûr mahzûf habere müteallik"),
  NM("السَّمَاوَةِ", "samawa", (" — بَادِيَةٌ بَيْنَ الْكُوفَةِ وَالشَّامِ", " — the steppe between Kufa and Syria", " — Kûfe ile Şam arasındaki çöl"), punct=".")]})
S1.append({"id": "s3", "translation": {"en": "This proverb was spoken by none other than al-Zabbāʾ.", "tr": "Bu atasözünü söyleyen, Zebbâ'dan başkası değildir."},
 "tokens": [tok("وَهٰذَا", "hadha", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; هٰذَا «this» is a demonstrative built on sukun, in the seat of raf' as the mubtada.", "«ve» + hâzâ işaret ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هٰذَا", "hadha", "pron")]),
  BADAL("الْمَثَلُ", "mathal", "raf"),
  tok("إِنَّمَا", "innama", "part", ["innama-kaffa", "qasr"], "إِنَّ حَرْفُ تَوْكِيدٍ مَكْفُوفٌ، وَمَا كَافَّةٌ — أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا.", "إِنَّ held back from governing by the مَا that stops it — a particle of restriction («none but»), governing nothing.", "Mâ-i kâffe ile amelden alıkonmuş inne — hasr edatı («ancak»), amel etmez."),
  MADI("تَكَلَّمَتْ", "takallama", ["form-v-verbs"], fem=True, note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ", note_en="; its doer follows — the clause is the predicate of «this», in the seat of raf'", note_tr="; fâili sonra gelir — cümle mübtedânın haberi, mahallen merfû"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onu»)", note_ar=" — وَالْهَاءُ لِلْمَثَلِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَكَلَّمَتْ»", note_en=" — «it» is the proverb; the phrase hangs on «spoke»", note_tr=" — zamir atasözüne döner; câr-mecrûr «söyledi»ye müteallik"),
  FAIL("الزَّبَّاءُ", "zabba", "propn", ["mamnu-min-sarf"], note_ar=" — مَمْنُوعَةٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ مَلِكَةُ الْجَزِيرَةِ وَتَدْمُرَ", note_en=" — a diptote for its long feminine alif; the queen of the Jazīra and Palmyra", note_tr=" — memdûde te'nîs elifi yüzünden gayr-i munsarif; Cezîre ve Tedmür kraliçesi", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "That was because, when she sent Qaṣīr al-Lakhmī with the caravan to carry back to her on it some of the cloth and the fine wares of Iraq —", "tr": "Şöyle ki: Kasîr el-Lahmî'yi, kendisi için kervanla Irak'ın kumaşlarından ve güzel eşyalarından yüklesin diye gönderdiğinde —"},
 "tokens": [tok("وَذٰلِكَ", "dhalika", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.", "The waw resumes; the demonstrative ذَا is the mubtada in the seat of raf'; the lam marks distance and the kaf is the particle of address.", "Vâv isti'nâf; zâ işaret ismi mübtedâ, mahallen merfû; lâm uzaklık, kâf hitap harfi.", segments=[seg("وَ", "wa", "conj"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("أَنَّهَا", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "mawadi-fath-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا (الزَّبَّاءُ) — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.", "أَنَّ «that»; «she» (al-Zabbāʾ) is its noun in the seat of nasb — the masdar it makes is the predicate of «that was», in the seat of raf'.", "Enne; «o» (Zebbâ) ismi, mahallen mansûb — kurduğu müevvel masdar mübtedânın haberi, mahallen merfû.", segments=[seg("أَنَّ", "anna", "part"), seg("هَا", "pron-3fs", "pron")]),
  NOTE(LAMMA2("لَمَّا"), " — وَالْجُمْلَةُ مِنْ «لَمَّا» وَشَرْطِهَا وَجَوَابِهَا فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the لَمَّا clause with its answer fills the seat of raf' as the predicate of أَنَّ", "; lemmâ cümlesi cevabıyla birlikte enne'nin haberi, mahallen merfû"),
  MADI("وَجَّهَتْ", "wajjaha", ["form-ii-verbs"], fem=True, hidden=True, **W(LAMMA_SHART)),
  MAFUL("قَصِيرًا", "qasir-lakhmi", "propn", note_ar=" — عَلَمٌ مُنْصَرِفٌ", note_en=" — a fully declined name", note_tr=" — munsarif alem"),
  NAAT("اللَّخْمِيَّ", "lakhmi", "nasb", extra=["ism-mansub"], note_ar=" — نِسْبَةٌ إِلَى لَخْمٍ", note_en=" — a nisba to the tribe of Lakhm", note_tr=" — Lahm kabilesine nisbet"),
  BI_NOUN("بِالْعِيرِ", "ir-caravan", "الْعِيرِ", note_ar=" — لِلْمُصَاحَبَةِ؛ وَالْعِيرُ: الْإِبِلُ تَحْمِلُ الْمِيرَةَ، مُؤَنَّثَةٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَجَّهَتْ»", note_en=" — the ba of company; الْعِير is a caravan of laden camels (feminine); the phrase hangs on «sent»", note_tr=" — bâ musâhabe; îr: yük taşıyan deve kervanı (müennes); câr-mecrûr «gönderdi»ye müteallik", punct="،"),
  MANSUB_AN("لِيَحْمِلَ", "hamala", by="أَنْ مُضْمَرَةٍ بَعْدَ لَامِ التَّعْلِيلِ", note_ar=" — وَاللَّامُ حَرْفُ جَرٍّ، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِهَا مُتَعَلِّقٌ بِـ«وَجَّهَتْ»؛ وَالْفَاعِلُ قَصِيرٌ", note_en=" — the lam is a jarr letter of purpose, the masdar so made hangs on «sent»; the doer is Qaṣīr", note_tr=" — lâm ta'lîl için cer harfi, müevvel masdar «gönderdi»ye müteallik; fâil Kasîr"),
  NOTE(LAHU("لَهَا", "pron-3fs", " («onun için»)"), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَحْمِلَ»", "; the phrase hangs on «carry»", "; câr-mecrûr «yüklesin»e müteallik"),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («onun üzerine»)", note_ar=" — وَالْهَاءُ لِلْعِيرِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَحْمِلَ»", note_en=" — «it» is the caravan; the phrase hangs on «carry»", note_tr=" — zamir kervana döner; câr-mecrûr «yüklesin»e müteallik"),
  PREP("مِنْ", "min", " — تَبْعِيضِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَحْمِلَ» عَلَى الْمَعْنَى", " — partitive («some of»); the phrase stands for the object of «carry»", "; teb'îz içindir; câr-mecrûr mânâca «yüklesin»in mef'ûlü yerindedir", gloss_tr="«-den»"),
  MAJR("بَزِّ", "bazz", note_ar=MUDAF[0] + " — وَالْبَزُّ: الثِّيَابُ وَمَتَاعُ الْبَيْتِ", note_en=MUDAF[1] + " — بَزّ: cloth, fabrics", note_tr=MUDAF[2] + " — bezz: kumaş, giyecek"),
  MUDAF_ILAYH("الْعِرَاقِ", "iraq", "propn"),
  tok("وَأَلْطَافِهِ", "lutf", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَأَلْطَافِ مَعْطُوفٌ عَلَى «بَزِّ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ لُطْفٍ: الطُّرَفُ وَالْهَدَايَا.",
      "The waw conjoins; «fine wares» is conjoined to «cloth», in jarr, annexed to «its» (Iraq's) — the plural of لُطْف: dainties, gifts.", "«ve» + eltâf, «bezz»e ma'tûf, mecrûr, «onun» (Irak'ın) zamirine muzâf — lutf'un çoğulu: nâdide şeyler, hediyeler.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("أَلْطَافِ", "lutf", "noun"), seg("هِ", "pron-3ms", "pron")])]})
S1.append({"id": "s5", "translation": {"en": "and he was seeking to avenge on her the blood of Jadhīma al-Abrash —", "tr": "o ise Cezîme el-Ebraş'ın kanını ondan almak peşindeydi —"},
 "tokens": [tok("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (قَصِيرٌ) — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw of state; كَانَ is the defective past verb, its noun the hidden «he» (Qaṣīr) — the clause is a hal, in the seat of nasb.", "Vâv hâliyye; kâne nâkıs mâzî, ismi gizli «o» (Kasîr) — cümle hâl, mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("كَانَ", "kana", "verb")]),
  MUDARI("يَطْلُبُهَا", "talaba", enc="هَا", note_ar=" — وَالْهَاءُ لِلزَّبَّاءِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", note_en=" — «her» is al-Zabbāʾ; the clause is the predicate of كَانَ", note_tr=" — zamir Zebbâ'ya döner; cümle kâne'nin haberi"),
  BI_NOUN("بِذَحْلِ", "lb-dhahl", "ذَحْلِ", note_ar="، مُضَافٌ — وَالْبَاءُ لِلسَّبَبِيَّةِ؛ وَالذَّحْلُ: الثَّأْرُ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَطْلُبُ»", note_en="; annexed — the ba of cause; ذَحْل is a blood-feud; the phrase hangs on «seek»", note_tr="; muzâf — bâ sebebiyye; zahl: kan dâvası; câr-mecrûr «peşindeydi»ye müteallik"),
  NM("جَذِيمَةَ", "jadhima", (DIPT_ALAM_F[0] + " — وَهُوَ جَذِيمَةُ الْأَبْرَشُ مَلِكُ الْحِيرَةِ الَّذِي قَتَلَتْهُ الزَّبَّاءُ", " — by a fatha standing in for the kasra" + DIPT_ALAM_F[1] + "; Jadhīma al-Abrash, king of al-Ḥīra, whom al-Zabbāʾ killed", " — kesre yerine fetha ile" + DIPT_ALAM_F[2] + "; Zebbâ'nın öldürdüğü Hîre kralı Cezîme el-Ebraş"), sign=FATHA_JARR, extra=["mamnu-min-sarf"]),
  NAAT("الْأَبْرَشِ", "abrash", "jarr", note_ar=" — لَقَبُهُ، وَالْأَبْرَشُ: الْأَبْرَصُ؛ وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ «الْ» عَلَيْهِ", note_en=" — his byname, «the speckled» (the leper); in jarr by the kasra because it carries the article", note_tr=" — lakabı: «alacalı» (abras); «el» aldığı için kesre ile mecrûr", punct="،")]})
S1.append({"id": "s6", "translation": {"en": "so he made the loads into chests, and put in every one of them a man with his weapons;", "tr": "bunun üzerine yükleri sandık yaptı ve her birinin içine silâhlı bir adam koydu;"},
 "tokens": [tok("فَجَعَلَ", "jaala", "verb", ["thulathi-mujarrad-babs", "mafulayn"], "الْفَاءُ زَائِدَةٌ فِي جَوَابِ لَمَّا، وَجَعَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ بِمَعْنَى صَيَّرَ، يَنْصِبُ مَفْعُولَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (قَصِيرٌ) — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا.",
      "The fa is extra, opening the answer of لَمَّا; جَعَلَ «made into» (like صَيَّرَ) takes two objects; its doer the hidden «he» (Qaṣīr) — the clause answers لَمَّا and has no seat.", "Fâ lemmâ'nın cevabında zâiddir; ceale «yaptı» (sayyera gibi) iki mef'ûl alır; fâil gizli «o» (Kasîr) — cümle lemmâ'nın cevabı, mahalli yoktur.", segments=[seg("فَ", "fa", "conj"), seg("جَعَلَ", "jaala", "verb")]),
  MAFUL("الْأَحْمَالَ", "himl", extra=["mafulayn", "jam-taksir"], note_ar=" — وَهُوَ الْمَفْعُولُ الْأَوَّلُ، جَمْعُ حِمْلٍ", note_en=" — the first object, the plural of حِمْل «a load»", note_tr=" — birinci mef'ûl; himl'in çoğulu"),
  MAFUL("صَنَادِيقَ", "sunduq", extra=["mafulayn", "jam-taksir", "mamnu-min-sarf"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي، جَمْعُ صُنْدُوقٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، فَلَمْ يُنَوَّنْ", note_en=" — the second object, the plural of صُنْدُوق on the «ultimate plural» pattern, so without tanwin", note_tr=" — ikinci mef'ûl; sundûk'un çoğulu, müntehe'l-cumû' vezninde, tenvinsiz", punct="،"),
  MADI("وَجَعَلَ", "jaala", hidden=True, note_ar=" — بِمَعْنَى وَضَعَ، يَنْصِبُ مَفْعُولًا وَاحِدًا", note_en=" — here «put», taking one object", note_tr=" — burada «koydu», tek mef'ûl alır"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَعَلَ»", "; the phrase hangs on «put»", "; câr-mecrûr «koydu»ya müteallik"),
  MAJR("كُلِّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("وَاحِدٍ", "wahid"),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («onlardan»)", note_ar=" — وَالْهَاءُ لِلصَّنَادِيقِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«وَاحِدٍ»", note_en=" — «them» are the chests; the phrase hangs on an omitted adjective of «one»", note_tr=" — zamir sandıklara döner; câr-mecrûr «bir»in mahzûf na'tına müteallik"),
  MAFUL("رَجُلًا", "rajul"),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "مَعَ «with», an adverb of place in nasb hanging on an omitted, fronted predicate, annexed to «him».", "Mea mekân zarfı, mansûb; öne alınmış mahzûf habere müteallik, «o» zamirine muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("السِّلَاحُ", "silah", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«رَجُلًا».", "The mubtada placed after its predicate, in raf' — the clause qualifies «a man», in the seat of nasb.", "Muahhar mübtedâ, merfû — cümle «adam»ın na'tı, mahallen mansûb.", punct="؛")]})
S1.append({"id": "s7", "translation": {"en": "then he turned aside with them from the plain road and took the way by al-Ghuwayr.", "tr": "sonra onlarla apaçık yoldan saptı ve Guveyr üzerinden yol aldı."},
 "tokens": [THUMMA(), MADI("تَنَكَّبَ", "tanakkaba", ["form-v-verbs"], hidden=True, note_ar=" — وَتَنَكَّبَ الطَّرِيقَ: عَدَلَ عَنْهُ", note_en=" — تَنَكَّبَ الطَّرِيقَ: to turn aside from a road", note_tr=" — tenekkebe't-tarîk: yoldan sapmak"),
  JARR_PRON("بِهِمُ", "bi", "بِ", "هِمُ", " («onlarla»)", note_ar=" — لِلْمُصَاحَبَةِ، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَنَكَّبَ»", note_en=" — the ba of company; the mim takes damma where two sukuns meet; the phrase hangs on «turned aside»", note_tr=" — bâ musâhabe; iki sâkin karşılaştığı için mîm dammelendi; câr-mecrûr «saptı»ya müteallik"),
  MAFUL("الطَّرِيقَ", "tariq"), NAAT("الْمَنْهَجَ", "manhaj", "nasb", note_ar=" — أَيِ: الْبَيِّنَ الْوَاضِحَ", note_en=" — i.e. the plain, open road", note_tr=" — yani apaçık, belli olan", punct="،"),
  MADI("وَأَخَذَ", "akhadha", ["mahmuz-verbs"], hidden=True, note_ar=" — وَأَخَذَ عَلَى الطَّرِيقِ: سَلَكَهُ", note_en=" — أَخَذَ عَلَى: to take a way by", note_tr=" — ehaze alâ: bir yoldan gitmek"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَخَذَ»", "; the phrase hangs on «took»", "; câr-mecrûr «aldı»ya müteallik"), GHUWAYR("majr", punct="،")]})
S1.append({"id": "s8", "translation": {"en": "She asked for news of him, and was told of that;", "tr": "Zebbâ onun haberini sordu; kendisine bu bildirildi;"},
 "tokens": [ISTI(MADI("فَسَأَلَتْ", "saala", ["mahmuz-verbs"], fem=True, hidden=True, **W(HID(*ZB)))),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَأَلَتْ»", "; the phrase hangs on «asked»", "; câr-mecrûr «sordu»ya müteallik", gloss_tr="«hakkında»"),
  ENC_NOUN("خَبَرِهِ", "khabar", "هِ", "majr", note_ar=" — وَالْهَاءُ لِقَصِيرٍ", note_en=" — «his» is Qaṣīr's", note_tr=" — zamir Kasîr'e döner", punct="،"),
  tok("فَأُخْبِرَتْ", "akhbara", "verb", ["naib-al-fail", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأُخْبِرَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ (الزَّبَّاءُ).",
      "The fa conjoins; «was told» is a past verb in the passive, built on fatha; the ta marks the feminine, and the deputy doer is the hidden «she» (al-Zabbāʾ).", "«bunun üzerine» + meçhul mâzî «haber verildi», fetha üzere mebnî; tâ te'nîs, nâib-i fâil gizli «o» (Zebbâ).", segments=[seg("فَ", "fa", "conj"), seg("أُخْبِرَتْ", "akhbara", "verb")]),
  tok("بِذٰلِكَ", "dhalika", "pron", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أُخْبِرَتْ».",
      "The ba is a jarr letter; the demonstrative ذَا fills the seat of jarr (the lam marks distance, the kaf is the particle of address) — the phrase hangs on «was told».", "Bâ cer harfi; zâ işaret ismi mahallen mecrûr (lâm uzaklık, kâf hitap) — câr-mecrûr «bildirildi»ye müteallik.", punct="؛", segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")])]})
S1.append({"id": "s9", "translation": {"en": "and she said: «The little cave may well bring evils» —", "tr": "o da: «Belki de bu mağaracıktan belâlar çıkar» dedi —"},
 "tokens": [ISTI(QALAT("فَقَالَتْ", punct=":")), ASA_HEAD(note=MAQUL), GHUWAYR("ism_asa"), ABUSAN(punct="،")]})
S1.append({"id": "s10", "translation": {"en": "she means: it may be that that road brings something bad;", "tr": "demek istiyor ki: belki o yol bir kötülük getirir;"},
 "tokens": [MUDARI("تَقُولُ", "qala", ["hollow-verbs"], who="هِيَ", note_ar=" — أَيْ: تُرِيدُ؛ وَالْجُمْلَةُ تَفْسِيرِيَّةٌ لَا مَحَلَّ لَهَا", note_en=" — i.e. she means; the clause explains and has no seat", note_tr=" — yani kastediyor; cümle tefsîriyye, mahalli yoktur", punct=":"),
  tok("عَسَى", "asa-hope", "verb", ["afal-al-muqaraba"], "فِعْلٌ مَاضٍ جَامِدٌ تَامٌّ هُنَا، مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ يَأْتِيَ»؛ وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "A frozen past verb, here complete (tāmm), built on a fatha estimated on the alif — its doer is the masdar made by «أَنْ يَأْتِيَ»; the clause is what is said.", "Câmid mâzî, burada tâm; elif üzerinde takdîrî fetha ile mebnî — fâili «en ye'tiye»den müevvel masdardır; cümle mekūlü'l-kavl."),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ فَاعِلُ عَسَى", "; the masdar it makes is the doer of عَسَى, in the seat of raf'", "; kurduğu müevvel masdar asâ'nın fâili, mahallen merfû"),
  MANSUB_AN("يَأْتِيَ", "ata", hidden=False, note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha shows on the ya, being light", note_tr=" — fetha hafif olduğu için yâ üzerinde görünür"),
  ISHARA("ذٰلِكَ", "dhalika", "رَفْعٍ فَاعِلٌ", "raf' as the doer", "fâil — merfû"), BADAL("الطَّرِيقُ", "tariq", "raf"),
  BI_NOUN("بِسُوءٍ", "su", "سُوءٍ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَأْتِيَ»", note_en=" — the phrase hangs on «bring»", note_tr=" — câr-mecrûr «getirir»e müteallik", punct="؛")]})
S1.append({"id": "s11", "translation": {"en": "and she found his conduct strange when he took a way other than the road.", "tr": "ve o, yol dışından gidince onun durumunu yadırgadı."},
 "tokens": [MADI("وَاسْتَنْكَرَتْ", "istankara", ["form-x-verbs"], fem=True, hidden=True, note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «فَقَالَتْ»", note_en=" — the clause is conjoined to «she said»", note_tr=" — cümle «dedi»ye ma'tûf"),
  ENC_NOUN("شَأْنَهُ", "shan", "هُ", "maful", note_ar=" — وَالْهَاءُ لِقَصِيرٍ", note_en=" — «his» is Qaṣīr's", note_tr=" — zamir Kasîr'e döner"),
  ZARF("حِينَ", "hin", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«اسْتَنْكَرَتْ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", note_en="; it hangs on «found strange» and is annexed to the clause after it", note_tr="; «yadırgadı»ya müteallik, sonraki cümleye muzâf"),
  MADI("أَخَذَ", "akhadha", ["mahmuz-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «حِينَ» إِلَيْهَا", note_en=" — the clause is in the seat of jarr, annexed to «when»", note_tr=" — cümle «hîne»ye muzâfun ileyh, mahallen mecrûr"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَخَذَ»", "; the phrase hangs on «took»", "; câr-mecrûr «aldı»ya müteallik"),
  MAJR("غَيْرِ", "ghayr", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الطَّرِيقِ", "tariq", punct=".")]})
S1.append({"id": "s12", "translation": {"en": "(Where it is said — al-Aṣmaʿī) So it became a proverb for anything from which evil is feared to come.", "tr": "(Nerede söylenir — Asmaî) Böylece, kendisinden kötülük gelmesinden korkulan her şey için darb-ı mesel oldu."},
 "tokens": [tok("فَصَارَ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ فِي سِيَاقِ كَلَامِ الْأَصْمَعِيِّ، وَصَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (هٰذَا الْقَوْلُ).",
      "The fa conjoins (in al-Aṣmaʿī's own account); صَارَ «became», a sister of كَانَ, its noun the hidden «it» (this saying).", "Fâ Asmaî'nin kendi sözü içinde atıf içindir; sâra «oldu», kâne'nin kardeşi; ismi gizli «o» (bu söz).", segments=[seg("فَ", "fa", "conj"), seg("صَارَ", "sara", "verb")]),
  KHK("مَثَلًا", "mathal", note_ar=" — خَبَرُ صَارَ", note_en=" — the predicate of صَارَ", note_tr=" — sâra'nın haberi"),
  tok("لِكُلِّ", "li", "prep", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَثَلًا».", "The lam is a jarr letter; «every» is in jarr and annexed — the phrase hangs on an omitted adjective of «a proverb».", "Lâm cer harfi; «her» mecrûr, muzâf — câr-mecrûr «mesel»in mahzûf na'tına müteallik.", segments=[seg("لِ", "li", "prep"), seg("كُلِّ", "kull", "noun")]),
  MUDAF_ILAYH("شَيْءٍ", "shay"),
  tok("يُخَافُ", "khafa", "verb", ["naib-al-fail", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ — وَنَائِبُ فَاعِلِهِ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ يَأْتِيَ»، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«شَيْءٍ».",
      "Present verb in the passive, in raf' — its deputy doer is the masdar made by «أَنْ يَأْتِيَ»; the clause qualifies «thing», in the seat of jarr.", "Meçhul muzâri, merfû — nâib-i fâili «en ye'tiye»den müevvel masdar; cümle «şey»in na'tı, mahallen mecrûr."),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ", "; the masdar it makes is the deputy doer, in the seat of raf'", "; kurduğu müevvel masdar nâib-i fâil, mahallen merfû"),
  MANSUB_AN("يَأْتِيَ", "ata", hidden=False),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", note_ar=" — وَالْهَاءُ لِلشَّيْءِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَأْتِيَ»", note_en=" — «it» is the thing; the phrase hangs on «come»", note_tr=" — zamir «şey»e döner; câr-mecrûr «gelmesi»ne müteallik"),
  FAIL("شَرٌّ", "sharr", punct=".")]})

NEW_GLOSS = {
 "ghuwayr": NP("الْغُوَيْر", "al-Ghuwayr (the little cave) — a water of the tribe of Kalb in al-Samāwa; in the proverb عَسَى الْغُوَيْرُ أَبْؤُسًا, said where evil is feared to come from a thing", "el-Guveyr (mağaracık) — Semâve'de Kelb kabilesine ait bir su; عَسَى الْغُوَيْرُ أَبْؤُسًا atasözünde: bir şeyden kötülük gelmesinden korkulduğunda söylenir", level=5),
 "kalb-tribe": NP("كَلْب", "Kalb — an Arab tribe of Quḍāʿa, in the Syrian steppe (elsewhere كَلْب is a dog)", "Kelb — Kudâa'dan, Şam çölünde bir Arap kabilesi (başka yerde «köpek»)", level=5),
 "kalbi": NP("الْكَلْبِيّ", "al-Kalbī — the nisba to Kalb; ابْنُ الْكَلْبِيِّ is Hishām ibn Muḥammad al-Kalbī (d. 204 AH), the genealogist and reporter", "el-Kelbî — Kelb'e nisbet; İbnü'l-Kelbî: neseb âlimi ve râvî Hişâm b. Muhammed el-Kelbî (ö. 204)", level=5),
 "samawa": NP("السَّمَاوَة", "al-Samāwa — the waterless steppe between Kufa and Syria", "es-Semâve — Kûfe ile Şam arasındaki susuz çöl", level=5),
 "zabba": NP("الزَّبَّاء", "al-Zabbāʾ — the queen of the Jazīra and Palmyra in the Arab tales, who killed Jadhīma al-Abrash; a diptote", "ez-Zebbâ — Arap rivâyetlerinde Cezîre ve Tedmür kraliçesi, Cezîme el-Ebraş'ı öldürdü; gayr-i munsarif", level=5),
 "qasir-lakhmi": NP("قَصِير", "Qaṣīr — Qaṣīr ibn Saʿd al-Lakhmī, Jadhīma's man, who avenged him on al-Zabbāʾ (as a common noun قَصِير is «short»)", "Kasîr — Cezîme'nin adamı Kasîr b. Sa'd el-Lahmî; onun öcünü Zebbâ'dan aldı (cins isim olarak «kısa»)", level=5),
 "lakhmi": NN("لَخْمِيّ", "ل خ م", "of Lakhm — the nisba to the tribe of Lakhm", "Lahmî — Lahm kabilesine nisbet", level=5),
 "ir-caravan": NN("عِير", "ع ي ر", "a caravan — camels carrying provisions and wares (feminine)", "kervan — erzak ve mal taşıyan develer (müennes)", level=5),
 "bazz": NN("بَزّ", "ب ز ز", "cloth, fabrics; garments and household stuff", "kumaş, bez; giyecek ve ev eşyası", level=5),
 "jadhima": NP("جَذِيمَة", "Jadhīma al-Abrash — the king of al-Ḥīra in the Arab tales, killed by al-Zabbāʾ; a diptote", "Cezîme el-Ebraş — Arap rivâyetlerinde Hîre kralı, Zebbâ tarafından öldürüldü; gayr-i munsarif", level=5),
 "abrash": NN("أَبْرَش", "ب ر ش", "speckled, spotted (of skin) — the byname of Jadhīma; a diptote as an adjective (أَفْعَل)", "alacalı, benekli (cilt) — Cezîme'nin lakabı; sıfat olarak gayr-i munsarif (ef'al)", level=5),
 "tanakkaba": NV("تَنَكَّبَ", "ن ك ب", "V", "to turn aside from, to avoid (a road) (Form V)", "(bir yoldan) sapmak, kaçınmak (tefa''ul bâbı)", level=5),
 "manhaj": NN("مَنْهَج", "ن ه ج", "a plain, open road; (as here) plain, clear", "apaçık yol; (burada) belli, açık", level=5),
 "wajjaha": NV("وَجَّهَ", "و ج ه", "II", "to send (someone) off, to dispatch (Form II)", "(birini) göndermek, yola çıkarmak (tef'îl bâbı)", level=5),
}
GLOSS_HERE = {
 "bus": ("misery, hardship; pl. أَبْؤُس — evils (عَسَى الْغُوَيْرُ أَبْؤُسًا)", "sıkıntı, darlık; çoğ. أَبْؤُس — belâlar"),
 "lutf": ("kindness, gentleness; pl. أَلْطَاف — dainties, choice gifts", "lütuf, incelik; çoğ. أَلْطَاف — nâdide şeyler, hediyeler"),
 "himl": ("a load (that is carried); pl. أَحْمَال", "yük; çoğ. أَحْمَال"),
 "sunduq": ("a box, a chest; pl. صَنَادِيق (a diptote)", "sandık; çoğ. صَنَادِيق (gayr-i munsarif)"),
}
V = {"wajjaha": SG.derived(SG.B2, SG.W2, "ُ", "وَجَّه", "وَجِّه", "وَجِّه", "تَوْجِيه", "مُوَجِّه", "مُوَجَّه", "وُجِّهَ", "يُوَجَّهُ"),
     "tanakkaba": SG.derived(SG.B5, SG.W5, "َ", "تَنَكَّب", "تَنَكَّب", "تَنَكَّب", "تَنَكُّب", "مُتَنَكِّب", "مُتَنَكَّب", "تُنُكِّبَ", "يُتَنَكَّبُ")}
FOR_HOCA = [
 ("the answer of «لَمَّا وَجَّهَتْ»: read as «فَجَعَلَ» with an extra fa (Qaṣīr made the loads into chests when she sent him); «فَسَأَلَتْ» is also possible", "«لَمَّا وَجَّهَتْ»nin cevabı: zâid fâ ile «فَجَعَلَ» okundu; «فَسَأَلَتْ» de mümkün"),
 ("«مِنْ بَزِّ الْعِرَاقِ»: the partitive phrase read as standing for the object of «يَحْمِلَ»", "«مِنْ بَزِّ الْعِرَاقِ»: teb'îz ifadesi «يَحْمِلَ»nin mef'ûlü yerinde okundu"),
 ("«الْمَنْهَجَ» read as an adjective of «الطَّرِيقَ» (the editor glosses it «البين الواضح»)", "«الْمَنْهَجَ», «الطَّرِيقَ»nin na'tı okundu (muhakkik: «البين الواضح»)"),
 ("the closing sentence is al-Aṣmaʿī's (another origin of the proverb), taken as the book's statement of where it is said", "son cümle Asmaî'ye aittir (atasözünün başka bir menşei); kitabın kullanım yeri beyânı olarak alındı"),
]
MANIFEST = manifest(SLUG, level=5, title=TITLES[0],
    subtitle={"ar": "الزَّبَّاءُ وَصَنَادِيقُ قَصِيرٍ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Al-Zabbāʾ and Qaṣīr's chests — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Zebbâ ve Kasîr'in sandıkları — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="p. 436 (printed 1:424), bāb 14", pages_ar="ص ٤٣٦ (الْمَطْبُوعُ ١: ٤٢٤)، الْبَابُ الرَّابِعَ عَشَرَ",
    span_en="Abū ʿUbayd's proverb as the heading; Ibn al-Kalbī's report in al-Bakrī's commentary, whole — from «وقال ابن الكلبي: الغوير» to «حين أخذ على غير الطريق» (al-Bakrī's grammatical remark after it is not taken); and, closing the chapter, al-Aṣmaʿī's sentence that tells where the proverb is said, which in the book stands just before Ibn al-Kalbī's report",
    span_tr="Başlıkta Ebû Ubeyd'in atasözü; Bekrî'nin şerhindeki İbnü'l-Kelbî rivâyeti tamamen — «وقال ابن الكلبي: الغوير»den «حين أخذ على غير الطريق»ye (ardındaki nahiv notu alınmadı); bölümün sonunda, kitapta bu rivâyetten hemen önce gelen ve atasözünün yerini söyleyen Asmaî cümlesi",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ رِوَايَةُ ابْنِ الْكَلْبِيِّ كُلُّهَا مِنْ «وَقَالَ ابْنُ الْكَلْبِيِّ: الْغُوَيْرُ» إِلَى «حِينَ أَخَذَ عَلَى غَيْرِ الطَّرِيقِ»، ثُمَّ جُمْلَةُ الْأَصْمَعِيِّ فِي مَضْرِبِهِ، وَهِيَ فِي الْكِتَابِ قَبْلَ الرِّوَايَةِ",
    corrections=[("الزبى", "الزَّبَّاءُ")],
    witness_ar="جِهَازُ التَّحْقِيقِ نَفْسُهُ: حَاشِيَةُ الْمُحَقِّقِ (٢) فِي ص ٤٣٦، وَفِيهَا أَنَّ النُّسْخَةَ ص تَقْرَأُ «الزباء» وَأَنَّ «تَغْيِيرَهُ أَوْلَى»",
    witness_en="the edition's own apparatus — the editor's note 2 on p. 436: manuscript ص reads «الزباء», «فتغييره أولى»",
    witness_tr="neşrin kendi aparatı — muhakkikin s. 436'daki 2. notu: ص nüshası «الزباء» okur, «فتغييره أولى»",
    hoca=FOR_HOCA, madrib=("فَصَارَ مَثَلًا لِكُلِّ شَيْءٍ يُخَافُ أَنْ يَأْتِيَ مِنْهُ شَرٌّ — الْأَصْمَعِيُّ", "al-Aṣmaʿī: «a proverb for anything from which evil is feared to come»", "Asmaî: «kendisinden kötülük gelmesinden korkulan her şey için»"))
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
