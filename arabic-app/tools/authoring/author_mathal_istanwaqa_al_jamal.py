"""Author content/samples/mathal-istanwaqa-al-jamal — «قَدِ اسْتَنْوَقَ الْجَمَلُ», the proverbs' shelf (v348-A), Level 5.

RECEIVED TEXT: Abū ʿUbayd's proverb with his report of Ṭarafa at a king's court, and al-Bakrī's naming of the poet and the king, «فصل
المقال» (Shamela 1025, pp. 202–203 = printed 1:190–191). The exact passage: research/sources/mathal-istanwaqa-al-jamal-src.txt. Abū ʿUbayd's
«وكان بعض العلماء يخبر … فقال طرفة عندها: استنوق الجمل», then al-Bakrī's «هذا الشاعر الذي لم يذكر اسمه … إلا للإناث خاصة», each whole,
with the verse he quotes in its place (one sentence, the hemistich marked «•»); al-Kumayt's verse and al-Bakrī's discussion of it are not
taken. The chapter closes with Abū ʿUbayd's own words on where the proverb is said («وهو الرجل يكون في حديث ثم يخلط ذلك بغيره وينتقل
إليه»), which in the book stand right after the proverb. CORRECTION (one): «الملتمس» → «الْمُتَلَمِّسُ», against the editor's note 1 on p. 203 («وهو في شعر المتلمس أيضاً») and the book's own spelling elsewhere.
Orthography only: the e-text's «ناقه» is «نَاقَةٍ». Every vowel is ours.
Run: python3 tools/authoring/author_mathal_istanwaqa_al_jamal.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-istanwaqa-al-jamal"
def ISTANWAQA(note=("", "", ""), qad=False):
    full = "اسْتَنْوَقَ"
    return tok(full, "istanwaqa", "verb", ["form-x-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — وَصَحَّتْ وَاوُهُ عَلَى الْأَصْلِ فَلَمْ تُقْلَبْ أَلِفًا (اسْتَنْوَقَ لَا اسْتَنَاقَ)، وَالْفَاعِلُ بَعْدَهُ" + note[0] + ".",
        "Past verb built on fatha — its waw stays sound and is not turned to alif (اسْتَنْوَقَ, not اسْتَنَاقَ); its doer follows" + note[1] + ".",
        "Fetha üzere mebnî mâzî — vâvı aslı üzere sahih kalır, elife dönmez (اسْتَنْوَقَ, اسْتَنَاقَ değil); fâili sonra gelir" + note[2] + ".")
def TARAFA_F(punct=None):
    return FAIL("طَرَفَةُ", "tarafa-tf", "propn", ["mamnu-min-sarf"], "، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", " — a man's name with the feminine ending, barred from tanwin", " — lafzî müennes alem, gayr-i munsarif", punct=punct)

TITLES = [{"ar": "قَدِ اسْتَنْوَقَ الْجَمَلُ", "en": "The He-Camel Has Turned She-Camel", "tr": "Erkek Deve Dişi Deveye Döndü"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "The he-camel has turned into a she-camel.", "tr": "Erkek deve dişi deveye dönüştü."},
 "tokens": [tok("قَدِ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "قَدْ affirms the past verb after it; it takes kasra where two sukuns meet.", "Kad tahkîk harfi; iki sâkin karşılaştığı için kesre ile harekelendi."),
  ISTANWAQA(HEAD_CL), FAIL("الْجَمَلُ", "jamal-camel", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "One of the learned used to report that this proverb is Ṭarafa ibn al-ʿAbd's.", "tr": "Âlimlerden biri bu atasözünün Tarafe b. el-Abd'e ait olduğunu haber verirdi."},
 "tokens": [ISTI(KANA("وَكَانَ")), ISMK("بَعْضُ", "bad", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الْعُلَمَاءِ", "alim-scholar", extra=["jam-taksir"]),
  MUDARI("يُخْبِرُ", "akhbara", ["form-iv-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", note_en=" — the clause is the predicate of كَانَ", note_tr=" — cümle kâne'nin haberi"),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِنْ مَعْمُولَيْهِ مَفْعُولُ «يُخْبِرُ».", "أَنَّ «that» — with its noun and predicate it makes a masdar, the object of «report».", "Enne — ismi ve haberiyle kurduğu müevvel masdar «haber verir»in mef'ûlü."),
  ISHARA("هٰذَا", "hadha", "نَصْبٍ اسْمُ أَنَّ", "nasb as the noun of أَنَّ", "enne'nin ismi — mansûb"), BADAL("الْمَثَلَ", "mathal", "nasb"),
  tok("لِطَرَفَةَ", "li", "prep", ["huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ لِلنِّسْبَةِ، وَطَرَفَةَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ أَنَّ.",
      "The lam of belonging, a jarr letter; Ṭarafa is in jarr by a fatha standing in for the kasra (a name with the feminine ending) — the phrase hangs on the omitted predicate of أَنَّ.", "Lâm aidiyet için cer harfi; Tarafe kesre yerine fetha ile mecrûr (lafzî müennes alem) — câr-mecrûr enne'nin mahzûf haberine müteallik.", segments=[seg("لِ", "li", "prep"), seg("طَرَفَةَ", "tarafa-tf", "propn")]),
  BN("jarr", ("طَرَفَةَ", "Ṭarafa", "Tarafe")), NM("الْعَبْدِ", "abd", (" — وَالْعَبْدُ اسْمُ أَبِيهِ", " — al-ʿAbd is his father's name", " — el-Abd babasının adıdır"), punct="،")]})
S1.append({"id": "s3", "translation": {"en": "There was at the court of a certain king a poet who was reciting to him a poem describing a he-camel, then turned it to the description of a she-camel;", "tr": "Krallardan birinin yanında, ona bir erkek deveyi tasvir eden bir şiir okuyan bir şair vardı; sonra şiiri dişi devenin vasfına çevirdi;"},
 "tokens": [ISTI(KANA("وَكَانَ")),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ، مُضَافٌ.", "An adverb of place in nasb, hanging on the omitted, fronted predicate of كَانَ; annexed.", "Mekân zarfı, mansûb; kâne'nin öne alınmış mahzûf haberine müteallik; muzâf."),
  MUDAF_ILAYH("بَعْضِ", "bad", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْمُلُوكِ", "malik-king", extra=["jam-taksir"]),
  ISMK("شَاعِرٌ", "shair", muakhkhar=True),
  MUDARI("يُنْشِدُهُ", "anshada", ["form-iv-verbs"], enc="هُ", note_ar=" — وَالْهَاءُ لِلْمَلِكِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«شَاعِرٌ»", note_en=" — «him» is the king; the clause qualifies «a poet»", note_tr=" — zamir krala döner; cümle «şair»in na'tı"),
  MAFUL("شِعْرًا", "shir", extra=["mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي", note_en=" — the second object", note_tr=" — ikinci mef'ûl"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«شِعْرًا»", "; the phrase hangs on an omitted adjective of «a poem»", "; câr-mecrûr «şiir»in mahzûf na'tına müteallik"),
  MAJR("وَصْفِ", "wasf", extra=["masdar"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("جَمَلٍ", "jamal-camel", punct="،"),
  THUMMA(), ENC_MADI("حَوَّلَهُ", "hawwala", "هُ", ["form-ii-verbs"], hidden=True, note_ar=" — وَالْهَاءُ لِلشِّعْرِ", note_en=" — «it» is the poem", note_tr=" — zamir şiire döner"),
  NOTE(ILA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حَوَّلَ»", "; the phrase hangs on «turned»", "; câr-mecrûr «çevirdi»ye müteallik"),
  MAJR("نَعْتِ", "nat-descr", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("نَاقَةٍ", "naqa", punct="،")]})
S1.append({"id": "s4", "translation": {"en": "and Ṭarafa said at that: «The he-camel has turned she-camel.»", "tr": "bunun üzerine Tarafe: «Erkek deve dişi deveye döndü» dedi."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), TARAFA_F(),
  tok("عِنْدَهَا", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«قَالَ»، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يَعُودُ عَلَى تِلْكَ الْحَالِ.", "An adverb of time in nasb hanging on «said», annexed to «it» — that moment.", "Zaman zarfı, mansûb, «dedi»ye müteallik; «o» zamirine muzâf — o âna döner.", punct=":", segments=[seg("عِنْدَ", "inda", "noun"), seg("هَا", "pron-3fs", "pron")]),
  ISTANWAQA(MAQUL), FAIL("الْجَمَلُ", "jamal-camel", punct=".")]})
S1.append({"id": "s5", "translation": {"en": "This poet whose name he does not give is al-Musayyab ibn ʿAlas; and it is said he is al-Mutalammis.", "tr": "Adını vermediği bu şair el-Müseyyeb b. Alas'tır; el-Mütelemmis olduğu da söylenir."},
 "tokens": [ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "mübtedâ — merfû"), BADAL("الشَّاعِرُ", "shair", "raf"),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«الشَّاعِرُ».", "A relative built on sukun, in the seat of raf' as an adjective of «the poet».", "İsm-i mevsûl, sükûn üzere mebnî, «şair»in na'tı olarak mahallen merfû."),
  LAM_JAZM(),
  JAZM_V("يَذْكُرِ", "dhakara", hidden="هُوَ", note_ar=" — وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْفَاعِلُ أَبُو عُبَيْدٍ؛ وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ", note_en=" — it takes kasra where two sukuns meet; the doer is Abū ʿUbayd; the clause is the ṣila", note_tr=" — iki sâkin karşılaştığı için kesrelendi; fâil Ebû Ubeyd; cümle sıla"),
  ENC_NOUN("اسْمَهُ", "ism-name", "هُ", "maful", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ", note_en=" — «his» is the returning pronoun", note_tr=" — zamir âiddir"),
  tok("هُوَ", "huwa", "pron", ["damir-fasl", "mubtada-khabar"], "ضَمِيرُ فَصْلٍ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "A pronoun of separation (ḍamīr al-faṣl), built on fatha, with no seat: it marks what follows as the predicate.", "Fasıl zamiri, fetha üzere mebnî, i'râbdan mahalli yoktur: sonrakinin haber olduğunu belirtir."),
  KHABAR("الْمُسَيَّبُ", "musayyab", note_ar=" — عَلَمٌ مُعَرَّفٌ بِالْ", note_en=" — a name with the article", note_tr=" — «el» ile marife alem"),
  BN("raf", ("الْمُسَيَّبُ", "al-Musayyab", "el-Müseyyeb")), NM("عَلَسٍ", "alas", MUNSARIF, punct="،"),
  tok("وَقِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَقُولَةُ بَعْدَهُ (عِنْدَ مَنْ يُجِيزُهُ).", "The waw conjoins; «it is said» is a past verb in the passive, built on fatha — its deputy doer is the sentence said after it (for those who allow it).", "«ve» + kîle meçhul mâzî, fetha üzere mebnî — nâib-i fâili ondan sonra söylenen cümledir (caiz görenlere göre).", punct=":", segments=[seg("وَ", "wa", "conj"), seg("قِيلَ", "qala", "verb")]),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun built on fatha, in the seat of raf' as the mubtada.", "Munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû."),
  KHABAR("الْمُتَلَمِّسُ", "mutalammis", note_ar=" — لَقَبُ الشَّاعِرِ جَرِيرِ بْنِ عَبْدِ الْمَسِيحِ الضُّبَعِيِّ", note_en=" — the byname of the poet Jarīr ibn ʿAbd al-Masīḥ al-Ḍubaʿī", note_tr=" — şair Cerîr b. Abdülmesîh ed-Dubaî'nin lakabı", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "He recited his poem in which he says:", "tr": "İçinde şöyle dediği şiirini okudu:"},
 "tokens": [MADI("أَنْشَدَ", "anshada", ["form-iv-verbs"], hidden=True, note_ar=" — يَعُودُ عَلَى الشَّاعِرِ", note_en=" (the poet)", note_tr=" (şair)"),
  ENC_NOUN("شِعْرَهُ", "shir", "هُ", "maful"),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«شِعْرَهُ».", "A relative built on sukun, in the seat of nasb as an adjective of «his poem».", "İsm-i mevsûl, sükûn üzere mebnî, «şiirini»nin na'tı olarak mahallen mansûb."),
  MUDARI("يَقُولُ", "qala", ["hollow-verbs"], note_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ", note_en=" — the clause is the ṣila", note_tr=" — cümle sıla"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَقُولُ»", note_en=" — «it» is the returning pronoun; the phrase hangs on «says»", note_tr=" — zamir âid; câr-mecrûr «der»e müteallik", punct=":")]})
S1.append({"id": "s7", "translation": {"en": "«I put away care when it comes upon me / on a swift camel, the ṣayʿariyya brand upon it, sturdy.»", "tr": "«Tasa geldiğinde onu unuturum / boynunda sayʿariyye damgası olan, sağlam, hızlı bir deveyle.»"},
 "tokens": [tok("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا فِي الْقَصِيدَةِ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَهِيَ مَعَ الْمُضَارِعِ هُنَا لِلتَّكْثِيرِ.", "The waw continues what comes before it in the poem; قَدْ with the present here means «often».", "Vâv kasidedeki öncesine bağlıdır; kad burada muzâri ile çokluk bildirir.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  MUDARI("أَتَنَاسَى", "tanasa", ["form-vi-verbs", "naqis-verbs"], who="أَنَا", naqis="ا", wujub=True, note_ar=" — وَتَنَاسَى الشَّيْءَ: أَرَى نَفْسَهُ أَنَّهُ نَسِيَهُ", note_en=" — تَنَاسَى: to make oneself forget a thing", note_tr=" — tenâsâ: bir şeyi unutmuş gibi yapmak"),
  MAFUL("الْهَمَّ", "hamm"),
  ZARF("عِنْدَ", "inda", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«أَتَنَاسَى»", note_en="; it hangs on «I put away»", note_tr="; «unuturum»a müteallik"),
  ENC_NOUN("احْتِضَارِهِ", "ihtidar-tf", "هِ", "mudaf", extra=["masdar"], note_ar=" — أَيْ: حُضُورِهِ؛ وَالْهَاءُ لِلْهَمِّ", note_en=" — i.e. its coming; «its» is care's", note_tr=" — yani gelmesi; zamir tasaya döner", punct="•"),
  tok("بِنَاجٍ", "bi", "prep", ["huruf-jarr", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ لِلِاسْتِعَانَةِ، وَنَاجٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمٌ مَنْقُوصٌ نَكِرَةٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَتَنَاسَى».",
      "The ba of the means, a jarr letter; «a swift one» is in jarr by a kasra estimated on the dropped ya — an indefinite manqūṣ noun; the phrase hangs on «I put away».", "Bâ isti'âne için cer harfi; nâcin, düşen yâ üzerinde takdîrî kesre ile mecrûr — nekre mankûs isim; câr-mecrûr «unuturum»a müteallik.", segments=[seg("بِ", "bi", "prep"), seg("نَاجٍ", "najin", "noun")]),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («üzerinde»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ", note_en=" — the phrase hangs on an omitted, fronted predicate", note_tr=" — câr-mecrûr öne alınmış mahzûf habere müteallik"),
  tok("الصَّيْعَرِيَّةُ", "sayariyya", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«نَاجٍ».", "The mubtada, placed after its predicate, in raf' — the clause qualifies «a swift one», in the seat of jarr.", "Muahhar mübtedâ, merfû — cümle «nâcin»in na'tı, mahallen mecrûr."),
  NAAT("مُكْدَمِ", "mukdam-ant", "jarr", note_ar=" — نَعْتٌ ثَانٍ لِـ«نَاجٍ»، أَيْ: صُلْبٍ غَلِيظٍ؛ وَهُوَ مَوْضِعُ الْقَافِيَةِ", note_en=" — a second adjective of «a swift one»: sturdy, solid; it is the rhyme word", note_tr=" — «nâcin»in ikinci na'tı: sağlam, kalın; kafiye kelimesidir", punct=".")]})
S1.append({"id": "s8", "translation": {"en": "That was at the court of ʿAmr ibn Hind.", "tr": "Bu, Amr b. Hind'in huzurunda olmuştu."},
 "tokens": [tok("وَذٰلِكَ", "dhalika", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.", "The waw resumes; the demonstrative ذَا is the mubtada in the seat of raf'; the lam marks distance and the kaf is the particle of address.", "Vâv isti'nâf; zâ işaret ismi mübtedâ, mahallen merfû; lâm uzaklık, kâf hitap.", segments=[seg("وَ", "wa", "conj"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ، مُضَافٌ.", "An adverb of place in nasb, hanging on an omitted predicate; annexed.", "Mekân zarfı, mansûb, mahzûf habere müteallik; muzâf."),
  MUDAF_ILAYH("عَمْرِو", "amr-name", "propn", note_ar=NO_TANWIN[0], note_en=NO_TANWIN[1], note_tr=NO_TANWIN[2]),
  BN("jarr", ("عَمْرِو", "ʿAmr", "Amr")), NM("هِنْدٍ", "hind", (" — عَلَمٌ مُؤَنَّثٌ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ، يَجُوزُ صَرْفُهُ وَمَنْعُهُ", " — a three-letter feminine name with a quiet middle letter: it may be declined or not", " — ortası sâkin üç harfli müennes alem; munsarif de gayr-i munsarif de olabilir"), punct=".")]})
S1.append({"id": "s9", "translation": {"en": "And Ṭarafa said «The he-camel has turned she-camel», because the ṣayʿariyya is a brand found only on females.", "tr": "Tarafe de «Erkek deve dişi deveye döndü» dedi; çünkü sayʿariyye yalnız dişilere vurulan bir damgadır."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), TARAFA_F(punct=":"),
  ISTANWAQA(MAQUL), FAIL("الْجَمَلُ", "jamal-camel", punct="،"),
  tok("لِأَنَّ", "anna", "part", ["lam-taleel", "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ مُتَعَلِّقٌ بِـ«قَالَ».", "The lam of cause, a jarr letter, and أَنَّ «that» — the masdar they make is in jarr by the lam, hanging on «said».", "Ta'lîl lâmı (cer harfi) ve enne — kurulan müevvel masdar lâm ile mecrûr, «dedi»ye müteallik.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part")]),
  tok("الصَّيْعَرِيَّةَ", "sayariyya", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, in nasb.", "Enne'nin ismi, mansûb."),
  tok("سِمَةٌ", "sima", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of أَنَّ, in raf'.", "Enne'nin haberi, merfû."),
  LA_NAFIYA(),
  tok("تَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«سِمَةٌ».", "A defective present verb in raf', its noun the hidden «it» (feminine) — the clause qualifies «a brand».", "Nâkıs muzâri, merfû; ismi gizli «o» — cümle «damga»nın na'tı, mahallen merfû."),
  ILLA(),
  tok("لِلْإِنَاثِ", "li", "prep", ["huruf-jarr", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَالْإِنَاثِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ أُنْثَى؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «تَكُونُ».", "The lam is a jarr letter; «females» (plural of أُنْثَى) is in jarr — the phrase hangs on the omitted predicate of «is».", "Lâm cer harfi; «dişiler» (ünsâ'nın çoğulu) mecrûr — câr-mecrûr «tekûnu»nun mahzûf haberine müteallik.", segments=[seg("لِ", "li", "prep"), seg("الْإِنَاثِ", "inath", "noun")]),
  HAL("خَاصَّةً", "khassa", note_ar=" — أَيْ: خَاصَّةً بِهِنَّ", note_en=" — i.e. belonging to them alone", note_tr=" — yani yalnız onlara özgü olarak", punct=".")]})
S1.append({"id": "s10", "translation": {"en": "(Where it is said) It is the man who is on one subject, then mixes it up with another and passes over to that.", "tr": "(Nerede söylenir) Bir konuda konuşurken onu başka bir şeyle karıştırıp ona geçen adam için söylenir."},
 "tokens": [tok("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — يَعُودُ عَلَى مَضْرِبِ الْمَثَلِ؛ وَبِهٰذَا فَسَّرَهُ أَبُو عُبَيْدٍ.", "The waw resumes; «it» (where the proverb applies) is a detached pronoun, the mubtada — Abū ʿUbayd's own gloss.", "Vâv isti'nâf; «o» (atasözünün söylendiği yer) munfasıl zamir, mübtedâ — Ebû Ubeyd'in kendi açıklaması.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  KHABAR("الرَّجُلُ", "rajul"),
  MUDARI_KH("يَكُونُ", "kana", ["hollow-verbs"], note_ar=" — بَلْ هُوَ فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «الرَّجُلُ»", note_en=" — rather a defective present verb, its noun the hidden «he»; the clause is a hal of «the man»", note_tr=" — daha doğrusu nâkıs muzâri, ismi gizli «o»; cümle «adam»dan hâl"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «يَكُونُ»", "; the phrase hangs on the omitted predicate of «is»", "; câr-mecrûr «yekûnu»nun mahzûf haberine müteallik"),
  MAJR("حَدِيثٍ", "hadith"),
  THUMMA(), MUDARI("يَخْلِطُ", "khalata", note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «يَكُونُ»", note_en=" — the clause is conjoined to «is»", note_tr=" — cümle «yekûnu»ya ma'tûf"),
  ISHARA("ذٰلِكَ", "dhalika", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb"),
  tok("بِغَيْرِهِ", "bi", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَخْلِطُ».", "The ba is a jarr letter; «another» is in jarr, annexed to «it» — the phrase hangs on «mixes».", "Bâ cer harfi; «başka» mecrûr, «o» zamirine muzâf — câr-mecrûr «karıştırır»a müteallik.", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun"), seg("هِ", "pron-3ms", "pron")]),
  MUDARI("وَيَنْتَقِلُ", "intaqala", ["form-viii-verbs"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «يَخْلِطُ»", note_en=" — the clause is conjoined to «mixes»", note_tr=" — cümle «karıştırır»a ma'tûf"),
  ILAYHI(punct=".")]})

NEW_GLOSS = {
 "istanwaqa": NV("اِسْتَنْوَقَ", "ن و ق", "X", "(of a he-camel) to become like a she-camel — قَدِ اسْتَنْوَقَ الْجَمَلُ, said of one who mixes one subject with another; its waw stays sound (Form X)", "(erkek deve) dişi deveye benzemek — قَدِ اسْتَنْوَقَ الْجَمَلُ, bir konuyu başkasıyla karıştıran için söylenir; vâvı sahih kalır (istif'âl bâbı)", level=5),
 "alas": NP("عَلَس", "ʿAlas — a man's name, fully declined; al-Musayyab ibn ʿAlas, the pre-Islamic poet of Ḍubayʿa", "Alas — erkek ismi, munsarif; câhiliye şairi el-Müseyyeb b. Alas", level=5),
 "mutalammis": NP("الْمُتَلَمِّس", "al-Mutalammis — the byname of the pre-Islamic poet Jarīr ibn ʿAbd al-Masīḥ, Ṭarafa's uncle", "el-Mütelemmis — câhiliye şairi Cerîr b. Abdülmesîh'in lakabı, Tarafe'nin dayısı", level=5),
 "tanasa": NV("تَنَاسَى", "ن س ي", "VI", "to put out of one's mind, to make oneself forget (Form VI, defective)", "unutmuş gibi yapmak, zihninden atmak (tefâul bâbı, nâkıs)", level=5),
 "najin": NN("نَاجٍ", "ن ج و", "swift (of a camel) — the active participle of نَجَا, a manqūṣ noun", "hızlı (deve) — necâ'nın ism-i fâili, mankûs isim", level=5),
 "sayariyya": NN("صَيْعَرِيَّة", "ص ع ر", "the ṣayʿariyya — a brand set on the neck of she-camels only", "sayʿariyye — yalnız dişi develerin boynuna vurulan damga", level=5),
 "sima": NN("سِمَة", "و س م", "a brand, a mark (masdar-noun of وَسَمَ)", "damga, işaret (vesema'dan)", level=5),
}
GLOSS_HERE = {
 "musayyab": ("al-Musayyab — a man's name; here al-Musayyab ibn ʿAlas, the poet (elsewhere Saʿīd ibn al-Musayyab, the Medinan jurist)", "el-Müseyyeb — erkek ismi; burada şair el-Müseyyeb b. Alas (başka yerde Medineli fakih Saîd b. el-Müseyyeb)"),
 "mukdam-ant": ("sturdy, solid (of a camel); bitten by other stallions (al-Zawzanī on ʿAntara)", "sağlam, kalın (deve); başka aygırlarca ısırılmış (Antere'de Zevzenî)"),
 "khassa": ("the elite; خَاصَّةً (adverbial): exclusively, alone", "seçkinler; خَاصَّةً (zarf gibi): yalnızca, özellikle"),
 "hind": ("Hind — a woman's name: here the mother of ʿAmr ibn Hind, king of al-Ḥīra, who is named after her", "Hind — kadın ismi: burada Hîre kralı Amr b. Hind'in annesi; kral onun adıyla anılır"),
}
V = {"istanwaqa": SG.derived(SG.B10, SG.W10, "َ", "اِسْتَنْوَق", "سْتَنْوِق", "اِسْتَنْوِق", "اِسْتِنْوَاق", "مُسْتَنْوِق", None, None, None, "أَجْوَفُ وَاوِيٌّ صَحَّتْ عَيْنُهُ شُذُوذًا (اسْتَنْوَقَ)؛ لَازِمٌ."),
     "tanasa": SG.derived_naqis(SG.B6 + " — نَاقِصٌ", SG.W6, "َ", "تَنَاسَ", "تَنَاس", "a", "تَنَاس", "تَنَاسٍ (التَّنَاسِي)", "مُتَنَاسٍ", "مُتَنَاسًى", "تُنُوسِيَ", "يُتَنَاسَى", "نَاقِصٌ يَائِيٌّ مِنَ التَّفَاعُلِ: تَنَاسَى يَتَنَاسَى.")}
V["istanwaqa"]["samai"] = True   # HEARD, not built: the sound waw of اسْتَنْوَقَ is the sarf books' own example of shudhūdh (the rule gives اسْتَنَاقَ) — v333's stored-heard rule
FOR_HOCA = [
 ("the verse «وَقَدْ أَتَنَاسَى الْهَمَّ عِنْدَ احْتِضَارِهِ • بِنَاجٍ عَلَيْهِ الصَّيْعَرِيَّةُ مُكْدَمِ»: «مُكْدَمِ» (sturdy) and the reading of «احْتِضَارِهِ»", "«وَقَدْ أَتَنَاسَى الْهَمَّ …» beyti: «مُكْدَمِ» (sağlam) ve «احْتِضَارِهِ» okunuşu"),
 ("«هِنْدٍ» declined (it may also be left undeclined)", "«هِنْدٍ» munsarif okundu (gayr-i munsarif de olabilir)"),
 ("«وَقِيلَ: هُوَ الْمُتَلَمِّسُ»: the deputy doer of «قِيلَ» taken as the sentence said", "«وَقِيلَ: هُوَ الْمُتَلَمِّسُ»: «قِيلَ»nin nâib-i fâili söylenen cümle sayıldı"),
 ("«خَاصَّةً» read as a ḥāl (a maṣdar of the kind of عَافِيَة is also said)", "«خَاصَّةً» hâl okundu (âfiye vezninde masdar olarak mef'ûl-i mutlak da denir)"),
 ("the closing gloss «وَهُوَ الرَّجُلُ يَكُونُ فِي حَدِيثٍ …» is Abū ʿUbayd's, placed after the tale as the proverb's use", "sondaki «وَهُوَ الرَّجُلُ يَكُونُ فِي حَدِيثٍ …» açıklaması Ebû Ubeyd'indir; kullanım yeri olarak hikâyenin sonuna alındı"),
]
MANIFEST = manifest(SLUG, level=5, title=TITLES[0],
    subtitle={"ar": "طَرَفَةُ وَالشَّاعِرُ الَّذِي وَصَفَ الْجَمَلَ بِسِمَةِ النَّاقَةِ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Ṭarafa and the poet who gave a he-camel the she-camel's brand — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Tarafe ve erkek deveye dişi devenin damgasını vuran şair — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="pp. 202–203 (printed 1:190–191), bāb 3", pages_ar="ص ٢٠٢–٢٠٣ (الْمَطْبُوعُ ١: ١٩٠–١٩١)، الْبَابُ الثَّالِثُ",
    span_en="the proverb as the heading; Abū ʿUbayd's report «وكان بعض العلماء يخبر … فقال طرفة عندها استنوق الجمل», whole; al-Bakrī's «هذا الشاعر الذي لم يذكر اسمه … إلا للإناث خاصة», whole, with the verse he quotes (al-Kumayt's verse and its discussion are not taken); and, closing the chapter, Abū ʿUbayd's gloss of where the proverb is said, which in the book follows the proverb",
    span_tr="başlıkta atasözü; Ebû Ubeyd'in «وكان بعض العلماء يخبر … فقال طرفة عندها استنوق الجمل» rivâyeti tamamen; Bekrî'nin «هذا الشاعر الذي لم يذكر اسمه … إلا للإناث خاصة» sözü, naklettiği beyitle birlikte tamamen (Kümeyt'in beyti ve tartışması alınmadı); bölümün sonunda Ebû Ubeyd'in, kitapta atasözünden hemen sonra gelen kullanım açıklaması",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ خَبَرُ أَبِي عُبَيْدٍ عَنْ طَرَفَةَ، ثُمَّ كَلَامُ الْبَكْرِيِّ فِي اسْمِ الشَّاعِرِ مَعَ الْبَيْتِ، ثُمَّ تَفْسِيرُ أَبِي عُبَيْدٍ لِمَضْرِبِ الْمَثَلِ، وَهُوَ فِي الْكِتَابِ بَعْدَ الْمَثَلِ",
    extra_en="Orthography only: the e-text's «ناقه» is «نَاقَةٍ». The verse is one sentence, its first hemistich closed by «•». ", extra_tr="Yalnız imlâ: elektronik metindeki «ناقه», «نَاقَةٍ»dir. Beyit tek cümledir; ilk mısraı «•» ile kapanır. ", extra_ar="وَ«ناقه» فِي النَّصِّ الْإِلِكْتُرُونِيِّ هِيَ «نَاقَةٍ». ",
    corrections=[("وقيل هو الملتمس", "وَقِيلَ: هُوَ الْمُتَلَمِّسُ")],
    witness_ar="حَاشِيَةُ الْمُحَقِّقِ (١) فِي ص ٢٠٣: «وَهُوَ فِي شِعْرِ الْمُتَلَمِّسِ أَيْضًا»، وَالْكِتَابُ نَفْسُهُ يَكْتُبُ «الْمُتَلَمِّس» فِي سَبْعَةِ مَوَاضِعَ",
    witness_en="the editor's note 1 on p. 203 («وهو في شعر المتلمس أيضاً»), and the book's own spelling «المتلمس» in seven other places",
    witness_tr="muhakkikin s. 203'teki 1. notu («وهو في شعر المتلمس أيضاً») ve kitabın yedi başka yerdeki «المتلمس» yazımı",
    hoca=FOR_HOCA, madrib=("وَهُوَ الرَّجُلُ يَكُونُ فِي حَدِيثٍ ثُمَّ يَخْلِطُ ذٰلِكَ بِغَيْرِهِ وَيَنْتَقِلُ إِلَيْهِ", "the man who mixes one subject with another", "bir konuyu başkasıyla karıştıran adam"))
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
