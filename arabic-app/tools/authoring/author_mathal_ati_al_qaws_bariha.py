"""Author content/samples/mathal-ati-al-qaws-bariha — «أَعْطِ الْقَوْسَ بَارِيَهَا», the proverbs' shelf (v348-A), Level 5.

RECEIVED TEXT: Abū ʿUbayd's proverb and al-Bakrī's tale of al-Ḥuṭayʾa at the table of Saʿīd ibn al-ʿĀṣ, «فصل المقال» (Shamela 1025,
pp. 310–311 = printed 1:298–299). The exact passage: research/sources/mathal-ati-al-qaws-bariha-src.txt. The heading is the proverb; the
tale is al-Bakrī's whole, from «أول من نطق بهذا المثل الحطيئة» to «ووصله وحباه» (the verse after it is not taken); the chapter ends with
Abū ʿUbayd's own words on where the proverb is said («أي استعن على عملك بأهل المعرفة والحذق»), moved from before the tale to its close
as the brief asks — the only change of place, named in the attribution. No correction: «سم٧ع» is «سمع» with a stray digit of the e-text
(orthography). Every vowel is ours.
Run: python3 tools/authoring/author_mathal_ati_al_qaws_bariha.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-ati-al-qaws-bariha"
HT = ("الْحُطَيْئَةِ", "al-Ḥuṭayʾa", "Hutay'e")
SD = ("سَعِيدِ بْنِ الْعَاصِ", "Saʿīd ibn al-ʿĀṣ", "Saîd b. el-Âs")
HJ = ("الْحَاجِبِ", "the chamberlain", "hâcib")
NS = ("النَّاسِ", "the people", "insanlar")

TITLES = [{"ar": "أَعْطِ الْقَوْسَ بَارِيَهَا", "en": "Give the Bow to the One Who Shapes It", "tr": "Yayı Yontana Ver"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "Give the bow to the one who shapes it.", "tr": "Yayı, yontan ustasına ver."},
 "tokens": [tok("أَعْطِ", "aata", "verb", ["imperative-amr", "form-iv-verbs", "naqis-verbs", "mafulayn", "al-fail-al-mudmar-al-mustatir-wujuban"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَجُمْلَةُ الْمَثَلِ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
      "Imperative of أَعْطَى «to give», built on the dropping of the weak letter (the ya); its doer «you» must stay hidden — the proverb is an opening sentence with no seat.",
      "A'tâ «vermek» fiilinin emri, illet harfinin (yâ) hazfi üzere mebnî; fâil vücûben gizli «sen» — atasözü ibtidâiyye cümle, mahalli yoktur."),
  MAFUL("الْقَوْسَ", "qaws", extra=["mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الْأَوَّلُ", note_en=" — the first object", note_tr=" — birinci mef'ûl"),
  tok("بَارِيَهَا", "bari-qaws", "noun", ["maful-bihi", "mafulayn", "ism-maqsur-manqus", "ism-fail", "idafa-definiteness", "al-bariz-al-muttasil"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ لِخِفَّتِهَا — اسْمٌ مَنْقُوصٌ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The second object, in nasb by the fatha, which shows on the ya because it is light — a manqūṣ noun (the one who pares the bow), annexed to «it».",
      "İkinci mef'ûl, hafif olduğu için yâ üzerinde görünen fetha ile mansûb — mankûs isim (yayı yontan), «o» zamirine muzâf.", punct=".",
      segments=[seg("بَارِيَ", "bari-qaws", "noun"), seg("هَا", "pron-3fs", "pron")])]})
S1.append({"id": "s2", "translation": {"en": "The first to speak this proverb was al-Ḥuṭayʾa.", "tr": "Bu atasözünü ilk söyleyen Hutay'e'dir."},
 "tokens": [MUBTADA("أَوَّلُ", "awwal", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The relative «the one who», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «men», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  MADI("نَطَقَ", "nataqa", hidden=True, **W(SILA_)),
  tok("بِهٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَطَقَ».", "The ba is a jarr letter; هٰذَا is a demonstrative in the seat of jarr — the phrase hangs on «spoke».", "Bâ cer harfi; hâzâ işaret ismi, mahallen mecrûr — câr-mecrûr «söyledi»ye müteallik.", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
  BADAL("الْمَثَلِ", "mathal", "jarr"),
  KHABAR("الْحُطَيْئَةُ", "hutaya", ["mubtada-khabar"], punct=".", note_ar=" — لَقَبُ الشَّاعِرِ جَرْوَلِ بْنِ أَوْسٍ", note_en=" — the byname of the poet Jarwal ibn Aws", note_tr=" — şair Cervel b. Evs'in lakabı")]})
S1.append({"id": "s3", "translation": {"en": "That was because he came in to Saʿīd ibn al-ʿĀṣ while he was giving the people their midday meal, and he ate a coarse eating.", "tr": "Şöyle ki: Saîd b. el-Âs halka öğle yemeği verirken Hutay'e yanına girdi ve kaba saba yedi."},
 "tokens": [tok("وَذٰلِكَ", "dhalika", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.", "The waw resumes; the demonstrative ذَا is the mubtada, in the seat of raf'; the lam marks distance and the kaf is the particle of address.", "Vâv isti'nâf içindir; zâ işaret ismi mübtedâ, mahallen merfû; lâm uzaklık, kâf hitap harfi.", segments=[seg("وَ", "wa", "conj"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "mawadi-fath-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا (الْحُطَيْئَةُ) — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِمَّا بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "أَنَّ «that», the particle of emphasis; the attached «he» (al-Ḥuṭayʾa) is its noun in the seat of nasb — أَنَّ with what follows makes a masdar in the seat of raf' as the predicate.", "Enne te'kîd ve nasb harfi; «o» zamiri (Hutay'e) ismi, mahallen mansûb — sonrasıyla kurduğu müevvel masdar mübtedânın haberi, mahallen merfû.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  MADI("دَخَلَ", "dakhala", hidden=True, **W((" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi, mahallen merfû"))),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«دَخَلَ»", "; the phrase hangs on «came in»", "; câr-mecrûr «girdi»ye müteallik"),
  MAJR("سَعِيدِ", "said-name", "propn", note_ar=NO_TANWIN[0], note_en=NO_TANWIN[1], note_tr=NO_TANWIN[2]),
  BN("jarr", ("سَعِيدِ", "Saʿīd", "Saîd")),
  NM("الْعَاصِ", "al-as", sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ تَخْفِيفًا", note=(" — وَأَصْلُهُ: الْعَاصِي، اسْمٌ مَنْقُوصٌ حُذِفَتْ يَاؤُهُ فِي الْعَلَمِ", " — by a kasra estimated on the ya, which the name drops (al-ʿĀṣī → al-ʿĀṣ): a manqūṣ noun", " — isimde düşen yâ üzerinde takdîrî kesre ile; aslı «el-Âsî», mankûs isim")),
  tok("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — يَعُودُ عَلَى سَعِيدٍ.", "The waw of state; «he» (Saʿīd) is a detached pronoun built on fatha, in the seat of raf' as the mubtada.", "Vâv hâliyye; «o» (Saîd) munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  MUDARI("يُغَدِّي", "ghadda", ["form-ii-verbs"], naqis="ي", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «هُوَ»، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", note_en=" — the clause is the predicate of «he», and the nominal clause is a hal, in the seat of nasb", note_tr=" — cümle «hüve»nin haberi; isim cümlesi hâl, mahallen mansûb"),
  MAFUL("النَّاسَ", "nas", punct="،"),
  MADI("فَأَكَلَ", "akala", hidden=True, **W(HID(*HT))),
  tok("أَكْلًا", "akl", "noun", ["maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مُبَيِّنٌ لِلنَّوْعِ بِنَعْتِهِ.", "An absolute object (maf'ūl muṭlaq) in nasb — its adjective tells the kind of eating.", "Mef'ûl-i mutlak, mansûb — na'tı yeme şeklini bildirir."),
  NAAT("جَافِيًا", "jafin", "nasb", extra=["ism-maqsur-manqus", "ism-fail"], punct=".", note_ar=" — بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ؛ اسْمٌ مَنْقُوصٌ، أَيْ: غَلِيظًا خَشِنًا", note_en=" — the fatha shows on the ya of this manqūṣ noun: coarse, rough", note_tr=" — mankûs isimde fetha yâ üzerinde görünür: kaba, hoyrat")]})
S1.append({"id": "s4", "translation": {"en": "When the people had finished their food and gone out, he stayed where he was;", "tr": "İnsanlar yemeklerini bitirip çıkınca o yerinde kaldı;"},
 "tokens": [ISTI(LAMMA2("فَلَمَّا")), MADI("فَرَغَ", "faragha", **W(FAIL_BAAD, LAMMA_SHART)), FAIL("النَّاسُ", "nas"),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«فَرَغَ»", "; the phrase hangs on «finished»", "; câr-mecrûr «bitirdi»ye müteallik", gloss_tr="«-den»"),
  ENC_NOUN("طَعَامِهِمْ", "taam", "هِمْ", "majr"),
  WAW_PL("وَخَرَجُوا", "kharaja", note=ATF_CL),
  MADI("أَقَامَ", "aqama", ["hollow-verbs", "form-iv-verbs"], hidden=True, **W(HID(*HT), JAWAB_LAMMA)),
  tok("مَكَانَهُ", "makan", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«أَقَامَ»، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "An adverb of place in nasb, hanging on «stayed», annexed to «his».", "Mekân zarfı, mansûb, «kaldı»ya müteallik; «onun» zamirine muzâf.", punct="؛", segments=[seg("مَكَانَ", "makan", "noun"), seg("هُ", "pron-3ms", "pron")])]})
S1.append({"id": "s5", "translation": {"en": "so the chamberlain came to him to put him out.", "tr": "bunun üzerine hâcib onu çıkarmak için yanına geldi."},
 "tokens": [ISTI(ENC_MADI("فَأَتَاهُ", "ata", "هُ", alif=True, note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْهَاءُ لِلْحُطَيْئَةِ", note_en="; its doer follows — «him» is al-Ḥuṭayʾa", note_tr="; fâili ondan sonra gelir — zamir Hutay'e'ye döner")),
  FAIL("الْحَاجِبُ", "hajib"),
  tok("لِيُخْرِجَهُ", "akhraja", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi"], "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَيُخْرِجَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ مُتَعَلِّقٌ بِـ«أَتَاهُ».",
      "The lam of purpose, a jarr letter; «put out» is a present verb in nasb by an أَنْ hidden after the lam, its doer the hidden «he», and «him» its object — the masdar so made is in jarr by the lam and hangs on «came to him».",
      "Lâm ta'lîl lâmı (cer harfi); yuhrice, lâmdan sonra gizli «en» ile mansûb muzâri, fâil gizli «o», zamir mef'ûlün bih — kurulan müevvel masdar lâm ile mecrûr, «geldi»ye müteallik.", punct=".",
      segments=[seg("لِ", "li", "prep"), seg("يُخْرِجَ", "akhraja", "verb"), seg("هُ", "pron-3ms", "pron")])]})
S1.append({"id": "s6", "translation": {"en": "But he refused and said: «Do you think them too good to sit with me?", "tr": "O ise direndi ve dedi ki: «Onları benimle oturmaktan üstün mü tutuyorsun?"},
 "tokens": [ISTI(MADI("فَامْتَنَعَ", "imtanaa", ["form-viii-verbs"], hidden=True, **W(HID(*HT)))),
  QALA("وَقَالَ", hidden=True, punct=":"),
  tok("أَتَرْغَبُ", "raghiba", "verb", ["al-istifham", "mudari-marfu", "khuruj-al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتَرْغَبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
      "The hamza asks in reproach; «you hold» is a present verb in raf', its doer «you» hidden — the clause is what is said, in the seat of nasb.", "Hemze inkârî istifham; targabu merfû muzâri, fâil vücûben gizli «sen» — cümle mekūlü'l-kavl, mahallen mansûb.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَرْغَبُ", "raghiba", "verb")]),
  JARR_PRON("بِهِمْ", "bi", "بِ", "هِمْ", " («onları»)", note_ar=" — وَرَغِبَ بِهِ عَنْهُ: رَفَعَهُ عَنْهُ وَضَنَّ بِهِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَرْغَبُ»", note_en=" — رَغِبَ بِهِ عَنْ: to hold a man too good for a thing; the phrase hangs on «hold»", note_tr=" — رَغِبَ بِهِ عَنْ: birini bir şeyden üstün tutmak; câr-mecrûr fiile müteallik"),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَرْغَبُ»", "; the phrase hangs on «hold»", "; câr-mecrûr «tutuyorsun»a müteallik", gloss_tr="«-den»"),
  NOTE(YA_MUTAKALLIM_N("مُجَالَسَتِي", "mujalasa", "مُجَالَسَتِ", "مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", extra=["masdar", "huruf-jarr"], punct="؟"), "", "", "")]})
S1.append({"id": "s7", "translation": {"en": "It is I who hold myself too good for them!»", "tr": "Asıl ben kendimi onlardan üstün tutarım!»"},
 "tokens": [tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "ya-al-mutakallim"], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ مِنْ مَقُولِ الْقَوْلِ.", "إِنَّ, the particle of emphasis; the ya «I» is its noun in the seat of nasb — the clause goes on with what is said.", "İnne te'kîd ve nasb harfi; yâ ismi, mahallen mansûb — cümle söylenen sözün devamıdır.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  NOTE(YA_MUTAKALLIM_N("بِنَفْسِي", "nafs", "نَفْسِ", "مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", prep=("بِ", "bi", "الْبَاءُ حَرْفُ جَرٍّ", "The ba is a jarr letter", "Bâ cer harfi")), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَرْغَبُ»", " — the phrase hangs on «I hold»", " — câr-mecrûr «tutarım»a müteallik"),
  JARR_PRON("عَنْهُمْ", "an", "عَنْ", "هُمْ", " («onlardan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَرْغَبُ»", note_en=" — the phrase hangs on «I hold»", note_tr=" — câr-mecrûr «tutarım»a müteallik"),
  tok("لَأَرْغَبُ", "raghiba", "verb", ["mudari-marfu", "inna-wa-akhawatuha"], "اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَأَرْغَبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.",
      "The lam of emphasis moved to the predicate; «I hold» is a present verb in raf', its doer «I» hidden — the clause fills the seat of raf' as the predicate of إِنَّ.", "Müzahlaka lâmı (te'kîd); ergabu merfû muzâri, fâil vücûben gizli «ben» — cümle inne'nin haberi, mahallen merfû.", punct=".", segments=[seg("لَ", "lam-ibtida", "part"), seg("أَرْغَبُ", "raghiba", "verb")])]})
S1.append({"id": "s8", "translation": {"en": "When Saʿīd heard that from him — and he did not know him — he said: «Leave him.»", "tr": "Saîd bunu ondan işitince — onu tanımıyordu — «Bırak onu» dedi."},
 "tokens": [ISTI(LAMMA2("فَلَمَّا")), MADI("سَمِعَ", "samia", **W(FAIL_BAAD, LAMMA_SHART)), FAIL("سَعِيدٌ", "said-name", "propn"),
  ISHARA("ذٰلِكَ", "dhalika", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَمِعَ»", note_en=" — the phrase hangs on «heard»", note_tr=" — câr-mecrûr «işitti»ye müteallik"),
  tok("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — يَعُودُ عَلَى سَعِيدٍ.", "The waw of state; «he» (Saʿīd) is the mubtada, a detached pronoun in the seat of raf'.", "Vâv hâliyye; «o» (Saîd) mübtedâ, munfasıl zamir, mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  LA_NAFIYA(),
  MUDARI("يَعْرِفُهُ", "arafa", enc="هُ", note_ar=" — وَالْهَاءُ لِلْحُطَيْئَةِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «هُوَ»، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", note_en=" — «him» is al-Ḥuṭayʾa; the clause is the predicate of «he», and the nominal clause is a hal", note_tr=" — zamir Hutay'e'ye döner; cümle «hüve»nin haberi, isim cümlesi hâl", punct="،"),
  MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=":", **W(JAWAB_LAMMA)),
  AMR("دَعْهُ", "wadaa-let", enc="هُ", note_ar=" — مِنْ وَدَعَ بِمَعْنَى تَرَكَ؛ وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", note_en=" — from وَدَعَ «to let be»; the clause is what is said", note_tr=" — «bırakmak» anlamındaki vede'den; cümle mekūlü'l-kavl", punct=".")]})
S1.append({"id": "s9", "translation": {"en": "And they fell to talking about poetry and the poets.", "tr": "Derken şiir ve şairler üzerine müzakereye daldılar."},
 "tokens": [ISTI(WAW_PL("وَتَذَاكَرُوا", "tadhakara", ["form-vi-verbs"])), MAFUL("الشِّعْرَ", "shir"), ATF("وَالشُّعَرَاءَ", "shair", case="nasb", extra=["jam-taksir"], note_ar=" — جَمْعُ شَاعِرٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", note_en=" — the plural of شَاعِر, a diptote for its long feminine alif", note_tr=" — şâir'in çoğulu; memdûde te'nîs elifi yüzünden gayr-i munsarif", punct=".")]})
S1.append({"id": "s10", "translation": {"en": "Then he said to them: «You have hit upon good poetry;", "tr": "Bunun üzerine onlara dedi ki: «Şiirin iyisini buldunuz;"},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True)), LAHU("لَهُمْ", "pron-3mp", " («onlara»)", punct=":"),
  TUM("أَصَبْتُمْ", "asaba", ["form-iv-verbs", "hollow-verbs"], note=MAQUL), MAFUL("جَيِّدَ", "jayyid", note_ar=MUDAF[0] + " — مِنْ إِضَافَةِ الصِّفَةِ إِلَى الْمَوْصُوفِ", note_en=MUDAF[1] + " — the quality annexed to what it qualifies", note_tr=MUDAF[2] + " — sıfatın mevsûfa izâfeti"),
  MUDAF_ILAYH("الشِّعْرِ", "shir", punct="،")]})
S1.append({"id": "s11", "translation": {"en": "and had you given the bow to the one who shapes it, you would have come upon what you are after.»", "tr": "ama yayı yontan ustasına verseydiniz, aradığınızı bulurdunuz.»"},
 "tokens": [tok("وَلَوْ", "law", "part", ["huruf-al-shart-fil-kafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ يَدُلُّ عَلَى امْتِنَاعِ الْجَوَابِ لِامْتِنَاعِ الشَّرْطِ.", "The waw conjoins; لَوْ «had …», a conditional particle that does not put the verb in jazm: the answer did not happen because the condition did not.", "«ve» + lev: cezmetmeyen şart harfi; şart olmadığı için cevabın da olmadığını bildirir.", segments=[seg("وَ", "wa", "conj"), seg("لَوْ", "law", "part")]),
  TUM("أَعْطَيْتُمُ", "aata", ["form-iv-verbs", "naqis-verbs", "mafulayn"], note=(" — وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ فِعْلُ الشَّرْطِ لَا مَحَلَّ لَهَا", "; the mim takes damma where two sukuns meet; the clause is the condition and has no seat", "; iki sâkin karşılaştığı için mîm dammelenir; cümle şart cümlesi, mahalli yoktur"), pre=("", "", "")),
  MAFUL("الْقَوْسَ", "qaws", extra=["mafulayn"]),
  tok("بَارِيَهَا", "bari-qaws", "noun", ["maful-bihi", "mafulayn", "ism-maqsur-manqus", "idafa-definiteness", "al-bariz-al-muttasil"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The second object, in nasb by the fatha showing on the ya; annexed to «it».", "İkinci mef'ûl, yâ üzerinde görünen fetha ile mansûb; «o» zamirine muzâf.", segments=[seg("بَارِيَ", "bari-qaws", "noun"), seg("هَا", "pron-3fs", "pron")]),
  TUM("لَوَقَعْتُمْ", "waqaa", ["mithal-verbs"], note=(" — وَالْجُمْلَةُ جَوَابُ لَوْ لَا مَحَلَّ لَهَا", "; the clause is the answer of لَوْ and has no seat", "; cümle lev'in cevabı, mahalli yoktur"), pre=("اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَ", "The lam opens the answer of لَوْ; ", "Lâm lev'in cevabındadır; "), lam=True),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَقَعْتُمْ»", "; the phrase hangs on «come upon»", "; câr-mecrûr «buldunuz»a müteallik"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "The relative «what», built on sukun, in the seat of jarr.", "İsm-i mevsûl «mâ», sükûn üzere mebnî, mahallen mecrûr."),
  tok("تُرِيدُونَ", "arada", "verb", ["afal-khamsa", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا، وَالْعَائِدُ مَحْذُوفٌ: تُرِيدُونَهُ.",
      "Present verb in raf' by the kept nun — one of the five verbs; the waw is its doer — the clause is the ṣila, its returning pronoun left out («what you want [it]»).", "Ef'âl-i hamseden, nûnun sübûtuyla merfû muzâri; vâv fâil — cümle sıla, âid zamir mahzûf.", punct=".", segments=[seg("تُرِيدُ", "arada", "verb"), seg("ونَ", "pron-2mp", "pron")])]})
S1.append({"id": "s12", "translation": {"en": "Saʿīd took notice of him and asked his lineage, and he gave it,", "tr": "Saîd ona dikkat kesildi, soyunu sordu; o da soyunu söyledi."},
 "tokens": [ISTI(MADI("فَانْتَبَهَ", "intabaha", ["form-viii-verbs"], **W(FAIL_BAAD))), LAHU("لَهُ", "pron-3ms", " («ona»)"), FAIL("سَعِيدٌ", "said-name", "propn", punct="،"),
  ENC_MADI("وَنَسَبَهُ", "nasaba-attribute", "هُ", hidden=True, note_ar=" — أَيْ: سَأَلَهُ عَنْ نَسَبِهِ", note_en=" — i.e. he asked him his lineage", note_tr=" — yani soyunu sordu"),
  MADI("فَانْتَسَبَ", "intasaba-nasab", ["form-viii-verbs"], hidden=True, **W(HID(*HT))), LAHU("لَهُ", "pron-3ms", " («ona»)", punct="،")]})
S1.append({"id": "s13", "translation": {"en": "and he said: «God keep you, Abū Mulayka!", "tr": "ve dedi ki: «Allah ömür versin, ey Ebû Müleyke!"},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True, punct=":")),
  ENC_MADI("حَيَّاكَ", "hayya", "كَ", ["form-ii-verbs", "naqis-verbs"], alif=True, note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ خَبَرِيَّةٌ لَفْظًا دُعَائِيَّةٌ مَعْنًى، فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", note_en="; its doer follows — a statement in form, a prayer in meaning; the clause is what is said", note_tr="; fâili ondan sonra — lafzen haber, mânen dua"),
  ALLAH_F(), YA(),
  tok("أَبَا", "ab", "noun", ["vocative-munada", "five-nouns", "idafa-definiteness"], "مُنَادًى مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "A vocative in nasb by the alif — one of the five nouns; annexed.", "Münâdâ, esmâ-i hamseden olduğu için elif ile mansûb; muzâf."),
  NM("مُلَيْكَةَ", "mulayka", sign=FATHA_JARR, extra=["mamnu-min-sarf"], note=(DIPT_ALAM_F[0] + " — وَأَبُو مُلَيْكَةَ كُنْيَةُ الْحُطَيْئَةِ", " — by a fatha standing in for the kasra" + DIPT_ALAM_F[1] + "; Abū Mulayka is al-Ḥuṭayʾa's kunya", " — kesre yerine fetha ile" + DIPT_ALAM_F[2] + "; Ebû Müleyke Hutay'e'nin künyesidir"), punct="!")]})
S1.append({"id": "s14", "translation": {"en": "Why did you not let us know who you were, rather than lead us into ignorance of you, so that we neglect your due and stint you your share?»", "tr": "Kim olduğunu bize bildirseydin ya; bizi senden habersiz bırakmasaydın da hakkını zayi edip payını eksik vermeseydik!»"},
 "tokens": [tok("أَلَا", "ala-tahdid", "part", ["al-tahdid-wa-qad-wal-istifham-fil-kafiya"], "حَرْفُ تَحْضِيضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَهُوَ مَعَ الْمَاضِي لِلتَّوْبِيخِ وَاللَّوْمِ عَلَى مَا فَاتَ، لَا مَحَلَّ لَهُ.", "أَلَا, the particle of urging; with a past verb it reproaches what was left undone («why did you not…»), with no seat.", "Elâ tahdîd harfi; mâzî ile geçmişte yapılmayan şey için kınar («…seydin ya»), mahalli yoktur."),
  tok("أَعْلَمْتَنَا", "aalama", "verb", ["form-iv-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "Past verb built on sukun because the ta of the doer is attached; the ta «you» is its doer, and نَا «us» its object in the seat of nasb — the clause is what is said.", "Fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, «nâ» mef'ûlün bih, mahallen mansûb — cümle mekūlü'l-kavl.",
      segments=[seg("أَعْلَمْ", "aalama", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نَا", "pron-1p", "pron")]),
  BI_NOUN("بِمَكَانِكَ", "makan", "مَكَانِكَ", enc="كَ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَعْلَمْتَنَا»؛ وَمَكَانُ الرَّجُلِ: مَنْزِلَتُهُ وَحُضُورُهُ", note_en=" — the phrase hangs on «let us know»; a man's makān is his standing and his presence", note_tr=" — câr-mecrûr «bildirseydin»e müteallik; mekân: kişinin yeri ve mevkii", punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates, puts the verb in jazm and turns it to the past.", "«ve» + lem: nefy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("تَحْمِلْنَا", "hamala", "verb", ["nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «أَعْلَمْتَنَا».",
      "Present verb in jazm by لَمْ, its sign the sukun; its doer «you» hidden, and نَا «us» its object — the clause is conjoined to «let us know».", "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli «sen», «nâ» mef'ûlün bih — cümle «bildirseydin»e ma'tûf.", segments=[seg("تَحْمِلْ", "hamala", "verb"), seg("نَا", "pron-1p", "pron")]),
  NOTE(ALA(), " — وَحَمَلَهُ عَلَى الْأَمْرِ: أَوْقَعَهُ فِيهِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَحْمِلْنَا»", "; حَمَلَهُ عَلَى: to lead a man into a thing; the phrase hangs on «lead us»", "; حَمَلَهُ عَلَى: birini bir şeye sevk etmek; câr-mecrûr fiile müteallik"),
  MAJR("الْجَهْلِ", "jahl", extra=["masdar"]),
  JARR_PRON("بِكَ", "bi", "بِ", "كَ", " («seni»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْجَهْلِ»", note_en=" — the phrase hangs on the masdar «ignorance»", note_tr=" — câr-mecrûr «cehl» masdarına müteallik"),
  tok("فَنُضَيِّعَ", "dayyaa", "verb", ["nawasib-wa-jawazim-al-mudari", "form-ii-verbs"], "الْفَاءُ فَاءُ السَّبَبِيَّةِ، وَنُضَيِّعَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ فَاءِ السَّبَبِيَّةِ فِي جَوَابِ النَّفْيِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ.",
      "The fa of consequence; «we neglect» is a present verb in nasb by an أَنْ that must stay hidden after the fa of consequence answering a negation, its sign the fatha; its doer «we» hidden.", "Sebebiyye fâsı; nudayyia, nefyin cevabında sebebiyye fâsından sonra vücûben gizli «en» ile mansûb muzâri, alâmeti fetha; fâil gizli «biz».", segments=[seg("فَ", "fa", "conj"), seg("نُضَيِّعَ", "dayyaa", "verb")]),
  ENC_NOUN("حَقَّكَ", "haqq", "كَ", "maful"),
  tok("وَنَبْخَسَكَ", "bakhasa", "verb", ["nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], "الْوَاوُ عَاطِفَةٌ، وَنَبْخَسَ فِعْلٌ مُضَارِعٌ مَعْطُوفٌ عَلَى «نُضَيِّعَ» مَنْصُوبٌ بِالْفَتْحَةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
      "The waw conjoins; «we stint» is conjoined to «we neglect» and in nasb by the fatha; its doer «we» hidden, and «you» its first object.", "«ve» + nebhase, «nudayyia»ya ma'tûf, fetha ile mansûb; fâil gizli «biz», kâf birinci mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("نَبْخَسَ", "bakhasa", "verb"), seg("كَ", "pron-2ms", "pron")]),
  ENC_NOUN("قِسْطَكَ", "qist", "كَ", "maful", note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي؛ وَالْقِسْطُ: الْحِصَّةُ وَالنَّصِيبُ", note_en=" — the second object; قِسْط here is a share, one's portion", note_tr=" — ikinci mef'ûl; kıst: pay, hisse", punct=".")]})
S1.append({"id": "s15", "translation": {"en": "And he brought him near, gave him a seat close by, asked him to recite, and gave him gifts and favours.", "tr": "Onu yanına yaklaştırdı, meclisini yakın tuttu, ondan şiir okumasını istedi, ona ihsanda bulunup bağışlar verdi."},
 "tokens": [ISTI(ENC_MADI("وَأَدْنَاهُ", "adna-verb", "هُ", ["form-iv-verbs"], alif=True, hidden=True, note_ar=HID(*SD)[0] + "، وَالْهَاءُ لِلْحُطَيْئَةِ", note_en=" (Saʿīd) — «him» is al-Ḥuṭayʾa", note_tr=" (Saîd) — zamir Hutay'e'ye döner")),
  MADI("وَقَرَّبَ", "qarraba", ["form-ii-verbs"], hidden=True), ENC_NOUN("مَجْلِسَهُ", "majlis", "هُ", "maful"),
  ENC_MADI("وَاسْتَنْشَدَهُ", "istanshada", "هُ", ["form-x-verbs"], hidden=True, note_ar=" — أَيْ: طَلَبَ أَنْ يُنْشِدَهُ شِعْرَهُ", note_en=" — he asked him to recite his poetry", note_tr=" — şiirini okumasını istedi"),
  ENC_MADI("وَوَصَلَهُ", "wasala", "هُ", ["mithal-verbs"], hidden=True, note_ar=" — وَوَصَلَهُ: أَعْطَاهُ صِلَةً", note_en=" — وَصَلَهُ here: he gave him a gift (a ṣila)", note_tr=" — burada: ona hediye (sıla) verdi"),
  ENC_MADI("وَحَبَاهُ", "lb-haba", "هُ", ["naqis-verbs"], alif=True, hidden=True, note_ar=" — وَحَبَاهُ: أَعْطَاهُ بِلَا جَزَاءٍ", note_en=" — حَبَاهُ: he bestowed on him freely", note_tr=" — habâhu: karşılıksız bağışladı", punct=".")]})
S1.append({"id": "s16", "translation": {"en": "(Where it is said) That is: in your work, seek the help of those with knowledge and skill.", "tr": "(Nerede söylenir) Yani: işinde bilgi ve ustalık sahiplerinden yardım iste."},
 "tokens": [tok("أَيِ", "ay", "part", [], "حَرْفُ تَفْسِيرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، لَا مَحَلَّ لَهُ — وَبِهِ فَسَّرَ أَبُو عُبَيْدٍ مَضْرِبَ الْمَثَلِ.", "أَيْ «that is», the particle of explanation, built on sukun and given kasra where two sukuns meet; it has no seat — with it Abū ʿUbayd tells where the proverb is said.", "Ey tefsir harfi, sükûn üzere mebnî; iki sâkin karşılaştığı için kesreyle harekelenmiştir, mahalli yoktur — Ebû Ubeyd atasözünün yerini bununla açıklar."),
  AMR("اسْتَعِنْ", "istaana", ["form-x-verbs", "hollow-verbs"], note_ar=" — وَأَصْلُهُ اسْتَعْوِنْ، نُقِلَتْ كَسْرَةُ الْوَاوِ إِلَى الْعَيْنِ ثُمَّ حُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ تَفْسِيرِيَّةٌ لَا مَحَلَّ لَهَا", note_en=" — from اسْتَعْوِنْ: the waw's kasra moves to the ʿayn and the waw drops where two sukuns meet; the clause explains and has no seat", note_tr=" — aslı اسْتَعْوِنْ: vâvın kesresi ayne nakledilir, iki sâkin karşılaşınca vâv düşer; cümle tefsîriyye, mahalli yoktur"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اسْتَعِنْ»", "; the phrase hangs on «seek help»", "; câr-mecrûr «yardım iste»ye müteallik"),
  ENC_NOUN("عَمَلِكَ", "amal-work", "كَ", "majr", extra=["masdar"]),
  BI_NOUN("بِأَهْلِ", "ahl", "أَهْلِ", note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اسْتَعِنْ»", note_en="; annexed — the phrase hangs on «seek help»", note_tr="; muzâf — câr-mecrûr «yardım iste»ye müteallik"),
  MUDAF_ILAYH("الْمَعْرِفَةِ", "marifa", extra=["masdar"]),
  ATF("وَالْحِذْقِ", "hidhq", case="jarr", extra=["masdar"], punct=".")]})

NEW_GLOSS = {
 "bari-qaws": NN("بَارِي", "ب ر ي", "one who pares, who shapes (a bow, an arrow, a pen) — the active participle of بَرَى (a manqūṣ noun); أَعْطِ الْقَوْسَ بَارِيَهَا «give the bow to its maker»", "yontan, biçim veren (yay, ok, kalem) — بَرَى'nın ism-i fâili (mankûs); أَعْطِ الْقَوْسَ بَارِيَهَا «yayı yontanına ver»", level=5),
 "al-as": NP("الْعَاص", "al-ʿĀṣ — a man's name (al-ʿĀṣī, a manqūṣ noun whose ya the name drops); here Saʿīd ibn al-ʿĀṣ (d. 59 AH), the Umayyad governor of Kufa and Medina", "el-Âs — erkek ismi (aslı el-Âsî, yâ'sı isimde düşen mankûs); burada Saîd b. el-Âs (ö. 59), Kûfe ve Medine'nin Emevî valisi", level=5),
 "mulayka": NP("مُلَيْكَة", "Mulayka — a woman's name, a diptote; أَبُو مُلَيْكَةَ is the kunya of the poet al-Ḥuṭayʾa", "Müleyke — kadın ismi, gayr-i munsarif; أَبُو مُلَيْكَةَ şair Hutay'e'nin künyesidir", level=5),
 "ghadda": NV("غَدَّى", "غ د و", "II", "to give (someone) the midday meal, to feed at noon (Form II, defective)", "(birine) öğle yemeği yedirmek (tef'îl bâbı, nâkıs)", level=5),
 "jafin": NN("جَافٍ", "ج ف و", "coarse, rough, uncouth (an active participle of جَفَا, a manqūṣ noun: جَافِيًا in nasb)", "kaba, hoyrat, görgüsüz (cefâ'nın ism-i fâili, mankûs isim; nasbda جَافِيًا)", level=5),
 "mujalasa": NN("مُجَالَسَة", "ج ل س", "sitting together, keeping company (masdar of جَالَسَ, Form III)", "birlikte oturma, sohbet arkadaşlığı (câlese'nin masdarı)", level=5),
 "tadhakara": NV("تَذَاكَرَ", "ذ ك ر", "VI", "to talk over together, to discuss among themselves (Form VI)", "aralarında müzakere etmek, birlikte konuşmak (tefâul bâbı)", level=5),
 "intabaha": NV("اِنْتَبَهَ", "ن ب ه", "VIII", "to take notice, to become alert (لَهُ: to a man) (Form VIII)", "dikkat kesilmek, uyanmak (لَهُ: birine) (iftiâl bâbı)", level=5),
 "intasaba-nasab": NV("اِنْتَسَبَ", "ن س ب", "VIII", "to state one's lineage, to trace oneself to (Form VIII)", "soyunu söylemek, kendini bir soya nispet etmek (iftiâl bâbı)", level=5),
 "ala-tahdid": {"lemma": "أَلَا", "pos": "part", "gloss": {"en": "why not…? — the particle of urging; with a past verb a reproach for what was left undone", "tr": "…sene ya! — tahdîd harfi; mâzî ile yapılmayan şey için kınama"}, "level": 5},
 "adna-verb": NV("أَدْنَى", "د ن و", "IV", "to bring near, to draw (someone) close (Form IV, defective)", "yaklaştırmak, yanına almak (if'âl bâbı, nâkıs)", level=5),
 "istanshada": NV("اِسْتَنْشَدَ", "ن ش د", "X", "to ask (someone) to recite poetry (Form X)", "(birinden) şiir okumasını istemek (istif'âl bâbı)", level=5),
 "hidhq": NN("حِذْق", "ح ذ ق", "skill, mastery, expertness (masdar of حَذَقَ)", "ustalık, maharet (hazaka'nın masdarı)", level=5),
}
GLOSS_HERE = {
 "said-name": ("Saʿīd — a man's name; here Saʿīd ibn al-ʿĀṣ, the Umayyad governor", "Saîd — erkek ismi; burada Emevî valisi Saîd b. el-Âs"),
 "hutaya": ("al-Ḥuṭayʾa — the byname of Jarwal ibn Aws (d. c. 45 AH), the poet of satire, kunya Abū Mulayka", "Hutay'e — hiciv şairi Cervel b. Evs'in (ö. 45 civ.) lakabı; künyesi Ebû Müleyke"),
 "nasaba-attribute": ("to ascribe, to attribute; نَسَبَهُ: to ask a man his lineage", "nispet etmek; نَسَبَهُ: birine soyunu sormak"),
}
V = {}
V["ghadda"] = SG.derived_naqis(SG.B2 + " — نَاقِصٌ", SG.W2, "ُ", "غَدَّ", "غَدّ", "i", "غَدّ", "تَغْدِيَة", "مُغَدٍّ", "مُغَدًّى", "غُدِّيَ", "يُغَدَّى", "نَاقِصٌ وَاوِيٌّ مِنَ التَّفْعِيلِ: غَدَّاهُ يُغَدِّيهِ — أَطْعَمَهُ الْغَدَاءَ.")
V["tadhakara"] = SG.derived(SG.B6, SG.W6, "َ", "تَذَاكَر", "تَذَاكَر", "تَذَاكَر", "تَذَاكُر", "مُتَذَاكِر", "مُتَذَاكَر", "تُذُوكِرَ", "يُتَذَاكَرُ")
V["intabaha"] = SG.derived(SG.B8, SG.W8, "َ", "اِنْتَبَه", "نْتَبِه", "اِنْتَبِه", "اِنْتِبَاه", "مُنْتَبِه", None, None, None, "لَازِمٌ: انْتَبَهَ لَهُ — تَنَبَّهَ إِلَيْهِ.")
V["intasaba-nasab"] = SG.derived(SG.B8, SG.W8, "َ", "اِنْتَسَب", "نْتَسِب", "اِنْتَسِب", "اِنْتِسَاب", "مُنْتَسِب", None, None, None, "لَازِمٌ: انْتَسَبَ إِلَى أَبِيهِ — اعْتَزَى.")
V["adna-verb"] = SG.derived_naqis(SG.B4 + " — نَاقِصٌ", SG.W4, "ُ", "أَدْنَ", "دْن", "i", "أَدْن", "إِدْنَاء", "مُدْنٍ", "مُدْنًى", "أُدْنِيَ", "يُدْنَى", "نَاقِصٌ وَاوِيٌّ مِنَ الْإِفْعَالِ: أَدْنَاهُ يُدْنِيهِ — قَرَّبَهُ.")
V["istanshada"] = SG.derived(SG.B10, SG.W10, "َ", "اِسْتَنْشَد", "سْتَنْشِد", "اِسْتَنْشِد", "اِسْتِنْشَاد", "مُسْتَنْشِد", "مُسْتَنْشَد", "اُسْتُنْشِدَ", "يُسْتَنْشَدُ")

FOR_HOCA = [
 ("«الْعَاصِ»: the kasra on the ṣād, the name's ya dropped (al-ʿĀṣī)", "«الْعَاصِ»: sâd kesreli, ismin yâ'sı düşmüş (el-Âsî)"),
 ("«فَنُضَيِّعَ … وَنَبْخَسَكَ»: read in nasb after the fa of consequence answering «وَلَمْ تَحْمِلْنَا»; raf' «فَنُضَيِّعُ» (resumption) is possible", "«فَنُضَيِّعَ … وَنَبْخَسَكَ»: «وَلَمْ تَحْمِلْنَا»nın cevabında sebebiyye fâsından sonra mansûb okundu; isti'nâf ile merfû «فَنُضَيِّعُ» de mümkün"),
 ("«أَلَا أَعْلَمْتَنَا»: أَلَا read as the particle of urging/reproach (هَلَّا)", "«أَلَا أَعْلَمْتَنَا»: elâ tahdîd/tevbîh harfi (hellâ) okundu"),
 ("«أَتَرْغَبُ بِهِمْ عَنْ مُجَالَسَتِي»: addressed to the chamberlain (the second person), as the e-text gives no vowel", "«أَتَرْغَبُ بِهِمْ عَنْ مُجَالَسَتِي»: hâcibe hitap (ikinci şahıs) okundu"),
 ("the closing «أَيِ اسْتَعِنْ …» is Abū ʿUbayd's explanation, placed after the tale as the proverb's use", "sondaki «أَيِ اسْتَعِنْ …» Ebû Ubeyd'in açıklamasıdır; atasözünün kullanım yeri olarak hikâyenin sonuna alındı"),
]
MANIFEST = manifest(SLUG, level=5, title=TITLES[0],
    subtitle={"ar": "الْحُطَيْئَةُ عَلَى مَائِدَةِ سَعِيدِ بْنِ الْعَاصِ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Al-Ḥuṭayʾa at the table of Saʿīd ibn al-ʿĀṣ — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Hutay'e, Saîd b. el-Âs'ın sofrasında — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="pp. 310–311 (printed 1:298–299), bāb 9", pages_ar="ص ٣١٠–٣١١ (الْمَطْبُوعُ ١: ٢٩٨–٢٩٩)، الْبَابُ التَّاسِعُ",
    span_en="Abū ʿUbayd's proverb as the heading; al-Bakrī's tale whole, from «أول من نطق بهذا المثل الحطيئة» to «ووصله وحباه» (the verse after it not taken); and, closing the chapter, Abū ʿUbayd's own words on the proverb's use («أي استعن على عملك بأهل المعرفة والحذق»), which in the book stand before the tale",
    span_tr="Başlıkta Ebû Ubeyd'in atasözü; Bekrî'nin hikâyesinin tamamı («أول من نطق بهذا المثل الحطيئة»den «ووصله وحباه»ya; ardından gelen beyit alınmadı); bölümün sonunda Ebû Ubeyd'in, kitapta hikâyeden önce gelen kullanım açıklaması («أي استعن على عملك بأهل المعرفة والحذق»)",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ خَبَرُ الْبَكْرِيِّ كُلُّهُ مِنْ «أَوَّلُ مَنْ نَطَقَ بِهٰذَا الْمَثَلِ الْحُطَيْئَةُ» إِلَى «وَوَصَلَهُ وَحَبَاهُ»، ثُمَّ تَفْسِيرُ أَبِي عُبَيْدٍ لِمَضْرِبِهِ، وَهُوَ فِي الْكِتَابِ قَبْلَ الْخَبَرِ",
    extra_en="Orthography only: «سم٧ع» in the e-text is «سَمِعَ» with a stray digit. ", extra_tr="Yalnız imlâ: elektronik metindeki «سم٧ع», araya karışmış bir rakamla «سَمِعَ»dir. ", extra_ar="وَ«سم٧ع» فِي النَّصِّ الْإِلِكْتُرُونِيِّ هِيَ «سَمِعَ» دَخَلَهَا رَقْمٌ. ",
    hoca=FOR_HOCA, madrib=("أَيِ اسْتَعِنْ عَلَى عَمَلِكَ بِأَهْلِ الْمَعْرِفَةِ وَالْحِذْقِ", "«seek the help of those with knowledge and skill»", "«bilgi ve ustalık sahiplerinden yardım iste»"))
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
