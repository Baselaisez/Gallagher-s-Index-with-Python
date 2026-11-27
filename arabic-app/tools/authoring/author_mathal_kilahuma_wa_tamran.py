"""Author content/samples/mathal-kilahuma-wa-tamran — «كِلَاهُمَا وَتَمْرًا», the proverbs' shelf (v348-A), Level 4.

RECEIVED TEXT: Abū ʿUbayd's own anecdote of the caliph and al-Bakrī's report of ʿAmr ibn Ḥumrān al-Jaʿdī, «فصل المقال» (Shamela 1025,
p. 122 = printed 1:110). The exact passage: research/sources/mathal-kilahuma-wa-tamran-src.txt. Two spans, each whole: Abū ʿUbayd's
«جاءنا عن بعض الخلفاء … فلم يوله شيئاً», then al-Bakrī's «أول من قال هذا عمرو بن حمران الجعدي … فقال له عمرو "كلاهما وتمراً"» (the
editor's bracketed supplement after it and the second report are not taken). «الجعدي» is the editor's own correction in the print
(his note 1: «في س ط ص: الجعفري. والتصحيح عن الفاخر والميداني»), kept as printed.
CORRECTION (one): «أطمعني» → «أَطْعِمْنِي», against al-Maydānī's Majmaʿ al-amthāl (research/sources/mathal-kilahuma-wa-tamran-witness.txt:
«أطعمنى من هذا الزبد»). Every vowel is ours. The iʿrāb of the proverb follows the book's own supplement and al-Maydānī: «كِلَاهُمَا» raised
(«لك كلاهما»), «تَمْرًا» in nasb by an implied «وأزيدك».
Run: python3 tools/authoring/author_mathal_kilahuma_wa_tamran.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-kilahuma-wa-tamran"
def KILAHUMA(note=("", "", "")):
    return tok("كِلَاهُمَا", "kila", "noun", ["mubtada-khabar", "al-muthanna", "idafa-definiteness", "al-bariz-al-muttasil", "hadhf-wa-taqdir"],
        "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى مُضَافٌ إِلَى الضَّمِيرِ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْخَبَرُ مَحْذُوفٌ تَقْدِيرُهُ: لَكَ" + note[0] + ".",
        "The mubtada, in raf' by the alif — attached to the dual when annexed to a pronoun; «the two of them» is its second term; the predicate is left out: «(both are yours)»" + note[1] + ".",
        "Mübtedâ; zamire muzâf olduğunda tesniyeye mülhak olduğu için elif ile merfû; «hümâ» muzâfun ileyh; haber mahzûf: «(ikisi de senin)»" + note[2] + ".",
        segments=[seg("كِلَا", "kila", "noun"), seg("هُمَا", "pron-3d", "pron")])
def WA_TAMRAN(punct=None, quoted=False):
    q = "، وَجُمْلَةُ «كِلَاهُمَا وَتَمْرًا» فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ" if quoted else ""
    return tok("وَتَمْرًا", "tamr", "noun", ["maful-bihi", "hadhf-wa-taqdir", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَتَمْرًا مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: وَأَزِيدُكَ تَمْرًا — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا" + q + ".",
        "The waw conjoins; «dates» is the object, in nasb, of an omitted verb: «and (I will add you) dates» — the clause is conjoined to the one before.", "«ve» + «hurma», mahzûf bir fiilin mef'ûlü, mansûb: «(sana) hurma da (katarım)» — cümle öncekine ma'tûf.",
        punct=punct, segments=[seg("وَ", "wa", "conj"), seg("تَمْرًا", "tamr", "noun")])

TITLES = [{"ar": "كِلَاهُمَا وَتَمْرًا", "en": "Both of Them, and Dates Besides", "tr": "İkisi de, Üstüne Hurma"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "Both of them — and dates besides.", "tr": "İkisi de — üstüne de hurma."},
 "tokens": [KILAHUMA(HEAD_CL), WA_TAMRAN(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "It has reached us of one of the caliphs that he offered a man a choice of two things, and the man said: «Both of them, and dates besides.»", "tr": "Halifelerden birinin, bir adama iki şıktan birini seçmesini teklif ettiği bize ulaştı; adam da: «İkisi de, üstüne hurma» dedi."},
 "tokens": [ENC_MADI("جَاءَنَا", "jaa", "نَا", ["hollow-verbs", "mahmuz-verbs"], note_ar=" — وَالْفَاعِلُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّهُ عَرَضَ»: جَاءَنَا عَرْضُهُ", note_en=" — its doer is the masdar made by «that he offered»: «his offering reached us»", note_tr=" — fâili «ennehû arada»dan müevvel masdardır: «onun teklifi bize ulaştı»"),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَاءَنَا»", "; the phrase hangs on «reached us»", "; câr-mecrûr «ulaştı»ya müteallik", gloss_tr="«hakkında»"),
  MAJR("بَعْضِ", "bad", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الْخُلَفَاءِ", "khalifa", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ خَلِيفَةٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ، وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ «الْ»", note_en=" — the plural of خَلِيفَة, a diptote (the long feminine alif), in jarr by the kasra because it carries the article", note_tr=" — halîfe'nin çoğulu; memdûde elif yüzünden gayr-i munsarif, «el» aldığı için kesre ile mecrûr"),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "mawadi-fath-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ فَاعِلُ «جَاءَ».", "أَنَّ «that»; «he» (the caliph) is its noun in the seat of nasb — the masdar it makes is the doer of «reached», in the seat of raf'.", "Enne; «o» (halife) ismi, mahallen mansûb — müevvel masdar «ulaştı»nın fâili, mahallen merfû.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  MADI("عَرَضَ", "arada-present", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", note_en=" — the clause is the predicate of أَنَّ", note_tr=" — cümle enne'nin haberi"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَرَضَ»", "; the phrase hangs on «offered»", "; câr-mecrûr «teklif etti»ye müteallik"),
  MAJR("رَجُلٍ", "rajul"),
  MAFUL("خَلَّتَيْنِ", "khalla", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", note_ar=" — وَالْخَلَّةُ هُنَا: الْخَصْلَةُ يُخَيَّرُ فِيهَا", note_en=" — by the ya, a dual: two things to choose between", note_tr=" — tesniye olduğu için yâ ile: seçilecek iki şık", punct="،"),
  ISTI(QALA("فَقَالَ", hidden=True, punct=":")), NOTE(KILAHUMA(), " — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", "; the sentence is what is said", "; cümle mekūlü'l-kavl"), WA_TAMRAN(punct="،", quoted=True)]})
S1.append({"id": "s3", "translation": {"en": "He grew angry with him and said: «Do you jest in my presence?», and gave him charge of nothing.", "tr": "Halife ona kızdı ve: «Benim huzurumda şaka mı yapıyorsun?» dedi; ona hiçbir iş vermedi."},
 "tokens": [ISTI(MADI("فَغَضِبَ", "ghadiba", hidden=True, note_ar=" — يَعُودُ عَلَى الْخَلِيفَةِ", note_en=" (the caliph)", note_tr=" (halife)")),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («ona»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«غَضِبَ»", note_en=" — the phrase hangs on «grew angry»", note_tr=" — câr-mecrûr «kızdı»ya müteallik", punct="،"),
  QALA("وَقَالَ", hidden=True, punct=":"),
  tok("أَعِنْدِي", "inda", "noun", ["al-istifham", "maful-fih", "ya-al-mutakallim"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَعِنْدَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ مُتَعَلِّقٌ بِـ«تَمْزَحُ»، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "The hamza asks in reproach; عِنْدَ «in the presence of» is an adverb of place in nasb (the fatha estimated before the ya), hanging on «jest», annexed to «me» — the clause is what is said.", "Hemze inkârî istifham; inde mekân zarfı, yâ'dan önce takdîrî fetha ile mansûb, «şaka yaparsın»a müteallik, «ben» zamirine muzâf — cümle mekūlü'l-kavl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  MUDARI("تَمْزَحُ", "mazaha-jest", who="أَنْتَ", wujub=True, punct="؟"),
  tok("فَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], FA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The fa conjoins; لَمْ negates, puts the verb in jazm and turns it to the past.", "«bunun üzerine» + lem: nefy, cezm ve kalb harfi.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يُوَلِّهِ", "walla-amr", "verb", ["nawasib-wa-jawazim-al-mudari", "form-ii-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (الْخَلِيفَةُ)، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
      "Present verb in jazm by لَمْ, its sign the dropped weak letter (the ya); its doer the hidden «he» (the caliph), and «him» its first object.", "Lem ile meczûm muzâri, alâmeti illet harfinin (yâ) hazfi; fâil gizli «o» (halife), zamir birinci mef'ûl.", segments=[seg("يُوَلِّ", "walla-amr", "verb"), seg("هِ", "pron-3ms", "pron")]),
  MAFUL("شَيْئًا", "shay", extra=["mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي", note_en=" — the second object", note_tr=" — ikinci mef'ûl", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "The first to say this was ʿAmr ibn Ḥumrān al-Jaʿdī.", "tr": "Bunu ilk söyleyen Amr b. Humrân el-Ca'dî'dir."},
 "tokens": [MUBTADA("أَوَّلُ", "awwal", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The relative «the one who», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «men», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, **W(SILA_)),
  ISHARA("هٰذَا", "hadha", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb"),
  KHABAR("عَمْرُو", "amr-name", note_ar=NO_TANWIN[0] + " — وَالْوَاوُ تُكْتَبُ فَرْقًا بَيْنَهُ وَبَيْنَ «عُمَرَ»", note_en=NO_TANWIN[1] + " — the waw is written to tell it from «ʿUmar»", note_tr=NO_TANWIN[2] + " — vâv, «Ömer»den ayırmak için yazılır"),
  BN("raf", ("عَمْرُو", "ʿAmr", "Amr")),
  NM("حُمْرَانَ", "humran", (" — بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ: عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", " — by a fatha standing in for the kasra: a name barred from tanwin for the added alif and nun", " — kesre yerine fetha ile: alemiyet ve elif-nûn ziyadesi sebebiyle gayr-i munsarif"), sign=FATHA_JARR, extra=["mamnu-min-sarf"]),
  NAAT("الْجَعْدِيُّ", "jadi", "raf", extra=["ism-mansub"], note_ar=" — نَعْتٌ لِـ«عَمْرُو»، نِسْبَةٌ إِلَى جَعْدَةَ", note_en=" — an adjective of «ʿAmr»: a nisba to (the tribe of) Jaʿda", note_tr=" — «Amr»ın na'tı; Ca'de'ye nisbet", punct=".")]})
S1.append({"id": "s5", "translation": {"en": "He was out among his family's camels, tending them, when a man passed by him whom hunger and thirst had worn out — and before ʿAmr lay butter, a round loaf and dates.", "tr": "Ailesinin develeri arasında onları güdüyordu; açlığın ve susuzluğun bitap düşürdüğü bir adam yanından geçti; Amr'ın önünde de tereyağı, yuvarlak bir ekmek ve hurma vardı."},
 "tokens": [ISTI(KANA("وَكَانَ")),
  NOTE(FI(), " — وَاسْمُ كَانَ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (عَمْرٌو)؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", "; the noun of كَانَ is the hidden «he» (ʿAmr); the phrase hangs on the omitted predicate of كَانَ", "; kâne'nin ismi gizli «o» (Amr); câr-mecrûr kâne'nin mahzûf haberine müteallik"),
  MAJR("إِبِلٍ", "ibil"),
  tok("لِأَهْلِهِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَأَهْلِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«إِبِلٍ».", "The lam is a jarr letter; «family» is in jarr, annexed to «his» — the phrase hangs on an omitted adjective of «camels».", "Lâm cer harfi; «aile» mecrûr, «onun» zamirine muzâf — câr-mecrûr «develer»in mahzûf na'tına müteallik.", segments=[seg("لِ", "li", "prep"), seg("أَهْلِ", "ahl", "noun"), seg("هِ", "pron-3ms", "pron")]),
  MUDARI("يَرْعَاهَا", "raa-graze", naqis="ا", enc="هَا", note_ar=" — وَالْهَاءُ لِلْإِبِلِ؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِـ«إِبِلٍ»", note_en=" — «them» are the camels; the clause is a second adjective of «camels»", note_tr=" — zamir develere döner; cümle «develer»in ikinci na'tı", punct="،"),
  ISTI(MADI("فَمَرَّ", "marra", ["doubled-verbs"], **W(FAIL_BAAD))),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («yanından»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَرَّ»", note_en=" — the phrase hangs on «passed»", note_tr=" — câr-mecrûr «geçti»ye müteallik"),
  FAIL("رَجُلٌ", "rajul"), QAD(),
  ENC_MADI("جَهَدَهُ", "jahada-tf", "هُ", note_ar=" — أَيْ: أَجْهَدَهُ وَأَتْعَبَهُ، وَالْفَاعِلُ بَعْدَهُ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«رَجُلٌ»", note_en=" — i.e. it wore him out; its doer follows; the clause qualifies «a man»", note_tr=" — yani onu bitap düşürdü; fâili sonra gelir; cümle «adam»ın na'tı"),
  FAIL("الْجُوعُ", "ju"), ATF("وَالْعَطَشُ", "atash", punct="،"),
  tok("وَبَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَبَيْنَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، مُضَافٌ.", "The waw of state; بَيْنَ «between» is an adverb of place in nasb, hanging on an omitted, fronted predicate; annexed.", "Vâv hâliyye; beyne mekân zarfı, mansûb, öne alınmış mahzûf habere müteallik; muzâf.", segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun")]),
  MUDAF_ILAYH("يَدَيْ", "yad", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", note_ar=MUDAF[0], note_en=" — by the ya, a dual, its nun dropped for the annexation; annexed", note_tr=" — tesniye olduğu için yâ ile, izâfet için nûnu düşmüş; muzâf"),
  NM("عَمْرٍو", "amr-name", MUNSARIF),
  tok("زُبْدٌ", "zubd", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "The mubtada, placed after its predicate, in raf' — the clause is a hal, in the seat of nasb.", "Muahhar mübtedâ, merfû — cümle hâl, mahallen mansûb."),
  ATF("وَقُرْصٌ", "qurs"), ATF("وَتَمْرٌ", "tamr", punct="،")]})
S1.append({"id": "s6", "translation": {"en": "The man said to him: «Feed me from your butter or from your loaf.»", "tr": "Adam ona: «Tereyağından ya da ekmeğinden bana yedir» dedi."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), LAHU("لَهُ", "pron-3ms", " («ona»)"), FAIL("الرَّجُلُ", "rajul", punct=":"),
  AMR("أَطْعِمْنِي", "atama", ["form-iv-verbs"], enc="نِي", wiqaya=True, note_ar=" — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", note_en=" — the clause is what is said", note_tr=" — cümle mekūlü'l-kavl"),
  PREP("مِنْ", "min", " — تَبْعِيضِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَطْعِمْ»", " — partitive («some of»); the phrase hangs on «feed»", "; teb'îz; câr-mecrûr «yedir»e müteallik", gloss_tr="«-den»"),
  ENC_NOUN("زُبْدِكَ", "zubd", "كَ", "majr"),
  tok("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ مَبْنِيٌّ عَلَى السُّكُونِ.", "أَوْ «or», the conjunction of choice, built on sukun.", "Ev «veya», tahyîr için atıf harfi, sükûn üzere mebnî."),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «مِنْ زُبْدِكَ»", "; the phrase is conjoined to «from your butter»", "; câr-mecrûr «tereyağından»a ma'tûf", gloss_tr="«-den»"),
  ENC_NOUN("قُرْصِكَ", "qurs", "كَ", "majr", punct=".")]})
S1.append({"id": "s7", "translation": {"en": "And ʿAmr said to him: «Both of them — and dates besides.»", "tr": "Amr da ona: «İkisi de, üstüne de hurma» dedi."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), LAHU("لَهُ", "pron-3ms", " («ona»)"),
  FAIL("عَمْرٌو", "amr-name", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2], punct=":"),
  NOTE(KILAHUMA(), " — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", "; the sentence is what is said", "; cümle mekūlü'l-kavl"), WA_TAMRAN(punct=".", quoted=True)]})

NEW_GLOSS = {
 "mazaha-jest": NV("مَزَحَ", "م ز ح", "I", "to jest, to joke — مَزَحَ يَمْزَحُ", "şaka yapmak — mezaha yemzahu"),
 "humran": NP("حُمْرَان", "Ḥumrān — a man's name, a diptote (the added alif and nun); here ʿAmr ibn Ḥumrān al-Jaʿdī", "Humrân — erkek ismi, gayr-i munsarif (elif-nûn ziyadesi); burada Amr b. Humrân el-Ca'dî"),
 "jadi": NN("جَعْدِيّ", "ج ع د", "of Jaʿda — the nisba to the tribe of Jaʿda (of ʿĀmir ibn Ṣaʿṣaʿa)", "Ca'dî — Ca'de kabilesine (Âmir b. Sa'saa'dan) nisbet"),
 "zubd": NN("زُبْد", "ز ب د", "butter, fresh butter", "tereyağı"),
 "qurs": NN("قُرْص", "ق ر ص", "a round flat loaf of bread", "yuvarlak yassı ekmek, pide"),
}
GLOSS_HERE = {
 "khalla": ("a trait, a quality; (here) one of two things offered to choose between", "haslet, nitelik; (burada) seçilmek üzere sunulan iki şıktan biri"),
 "jahada-tf": ("to strive, to exert oneself; جَهَدَهُ: (of hunger, toil) to wear a man out", "çabalamak; جَهَدَهُ: (açlık, yorgunluk) birini bitap düşürmek"),
 "walla-amr": ("to turn (a thing) towards; وَلَّاهُ الْأَمْرَ: to put a man in charge of an affair (Form II)", "(bir şeyi) bir yöne çevirmek; وَلَّاهُ الْأَمْرَ: birini bir işin başına getirmek (tef'îl bâbı)"),
}
V = {"mazaha-jest": SG.sound1("fataha", "مَزَح", "مْزَح", "اِمْزَح", "مَزْح", "مَازِح", None, None, None, "لَازِمٌ: مَزَحَ يَمْزَحُ مَزْحًا.")}
FOR_HOCA = [
 ("the iʿrāb of «كِلَاهُمَا وَتَمْرًا»: «كِلَاهُمَا» a mubtada whose predicate is left out («لك»), «تَمْرًا» the object of an implied «وأزيدك» (al-Maydānī; the book's own supplement gives also «كليهما» on an implied verb)", "«كِلَاهُمَا وَتَمْرًا»nın i'râbı: «كِلَاهُمَا» haberi mahzûf mübtedâ («لك»), «تَمْرًا» takdîrî «وأزيدك»in mef'ûlü (Meydânî; kitabın kendi ilâvesi takdîrî fiille «كليهما»yı da verir)"),
 ("«فَلَمْ يُوَلِّهِ شَيْئًا»: Form II يُوَلِّي «to put in charge» (two objects)", "«فَلَمْ يُوَلِّهِ شَيْئًا»: tef'îl bâbından «iş başına getirmek» (iki mef'ûl)"),
 ("«جَهَدَهُ الْجُوعُ» on Form I (جَهَدَ), not «أَجْهَدَهُ»", "«جَهَدَهُ الْجُوعُ» sülâsî (جَهَدَ) okundu, «أَجْهَدَهُ» değil"),
]
MANIFEST = manifest(SLUG, level=4, title=TITLES[0],
    subtitle={"ar": "عَمْرُو بْنُ حُمْرَانَ وَالرَّجُلُ الْجَائِعُ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "ʿAmr ibn Ḥumrān and the hungry man — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Amr b. Humrân ve aç adam — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="p. 122 (printed 1:110), bāb 2", pages_ar="ص ١٢٢ (الْمَطْبُوعُ ١: ١١٠)، الْبَابُ الثَّانِي",
    span_en="the proverb as the heading; Abū ʿUbayd's anecdote of the caliph, whole («جاءنا عن بعض الخلفاء … فلم يوله شيئاً»); al-Bakrī's report of ʿAmr ibn Ḥumrān, whole («أول من قال هذا … فقال له عمرو كلاهما وتمراً») — the editor's bracketed supplement after it and the second report are not taken",
    span_tr="başlıkta atasözü; Ebû Ubeyd'in halife fıkrası tamamen; Bekrî'nin Amr b. Humrân rivâyeti tamamen — ardındaki muhakkik ilâvesi ve ikinci rivâyet alınmadı",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ خَبَرُ أَبِي عُبَيْدٍ عَنْ بَعْضِ الْخُلَفَاءِ كُلُّهُ، ثُمَّ خَبَرُ عَمْرِو بْنِ حُمْرَانَ عِنْدَ الْبَكْرِيِّ كُلُّهُ",
    corrections=[("أطمعني", "أَطْعِمْنِي")],
    witness_ar="«مَجْمَعُ الْأَمْثَالِ» لِلْمَيْدَانِيِّ (الشَّامِلَةُ ١٢٩٢٩، ٢: ١٥١)", witness_en="al-Maydānī's Majmaʿ al-amthāl (Shamela 12929, 2:151, § 3079: «أطعمنى من هذا الزبد»)", witness_tr="Meydânî, Mecmau'l-emsâl (Şâmile 12929, 2:151, § 3079: «أطعمنى من هذا الزبد»)",
    extra_en="«الجعدي» is the editor's own correction in the print (his note: the manuscripts read «الجعفري»), kept as printed. ", extra_tr="«الجعدي» baskıda muhakkikin kendi tashihidir (nüshalar «الجعفري» okur); baskıdaki gibi bırakıldı. ", extra_ar="وَ«الْجَعْدِيُّ» تَصْحِيحُ الْمُحَقِّقِ فِي الْمَطْبُوعِ، أُبْقِيَ كَمَا هُوَ. ",
    hoca=FOR_HOCA)
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
