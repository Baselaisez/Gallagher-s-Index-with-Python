"""Author content/samples/mathal-sabaqa-al-sayf-al-adhal — «سَبَقَ السَّيْفُ الْعَذَلَ», the proverbs' shelf (v348-A), Level 4.

RECEIVED TEXT. Abū ʿUbayd's own tale of Ḍabba ibn Udd, as al-Bakrī's «فصل المقال» carries it (Shamela 1025, p. 79 = printed 1:67, bāb 1):
the entry «الحديث ذو شجون» and the three sayings of Ḍabba that became proverbs — «أسعد أم سعيد», «إن الحديث ذو شجون», «سبق السيف العذل».
The exact passage: research/sources/mathal-sabaqa-al-sayf-al-adhal-src.txt. The heading sentence is the entry's proverb; then the tale,
whole and in order, from «يحدث بهذا المثل» to «فذهبت كلمته الثالثة مثلاً أيضاً».
CORRECTIONS (e-text → now), each against the WITNESS research/sources/mathal-sabaqa-al-sayf-al-adhal-witness.txt (Abū ʿUbayd, Kitāb
al-amthāl, ed. Qaṭāmish, Shamela 135 pp. 29–30 = printed 61–62): «لوم يرجع» → «وَلَمْ يَرْجِعْ»; «مثقلاً» → «مَثَلًا»; «رني» → «أَرِنِي».
VOWELLING is ours throughout. «يُحَدِّثُ» is read active, its hidden doer the narrator Abū ʿUbayd draws on (his own book: «وكان المفضل
بن محمد يحدث بهذا المثل»); the passive «يُحَدَّثُ» is possible on the Faṣl's words alone — for the hoca.
Run: python3 tools/authoring/author_mathal_sabaqa_al_sayf_al_adhal.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-sabaqa-al-sayf-al-adhal"
DB = ("ضَبَّةَ", "Ḍabba", "Dabbe")
HR = ("الْحَارِثِ", "al-Ḥārith", "Hâris")
RAWI = ("الرَّاوِي", "the narrator", "râvî")
DIPT_DABBA = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", " — a man's name with the feminine ending, barred from tanwin", " — lafzî müennes alem, gayr-i munsarif")
def DABBA(role, punct=None, pre=None):
    if role == "fail": return FAIL("ضَبَّةُ", "dabba-name", "propn", ["mamnu-min-sarf"], *DIPT_DABBA, punct=punct)
    if role == "ism_inna": return tok("ضَبَّةَ", "dabba-name", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + DIPT_DABBA[0] + ".", "The noun of إِنَّ, in nasb" + DIPT_DABBA[1] + ".", "İnne'nin ismi, mansûb" + DIPT_DABBA[2] + ".", punct=punct)
    if role == "ismk": return ISMK("ضَبَّةُ", "dabba-name", "propn", ["mamnu-min-sarf"], *DIPT_DABBA, punct=punct)
def MATHALAN(punct="."):
    return HAL("مَثَلًا", "mathal", punct=punct, note_ar=" — أَيْ: سَارَتْ مَثَلًا", note_en=" — i.e. it went round as a proverb", note_tr=" — yani darb-ı mesel olarak yayıldı")
def DHAHABAT():
    return MADI("فَذَهَبَتْ", "dhahaba", fem=True, **W(FAIL_BAAD))
def KALIMATUHU(): return ENC_NOUN("كَلِمَتُهُ", "kalima", "هُ", "fail", note_ar=" — وَالْهَاءُ لِضَبَّةَ", note_en=" — «his» is Ḍabba's", note_tr=" — zamir Dabbe'ye döner")
def AYDAN(punct="."):
    return tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: آضَ، مَنْصُوبٌ بِالْفَتْحَةِ.",
        "An absolute object of an omitted verb («it returned» — آضَ), in nasb: «likewise».", "Mahzûf bir fiilin (آضَ «döndü») mef'ûl-i mutlakı, mansûb: «yine, keza».", punct=punct)
def NAAT_ORD(full, lex, punct=None):
    return NAAT(full, lex, "raf", note_ar=" — نَعْتٌ لِـ«كَلِمَتُهُ»", note_en=" — it describes «his saying»: the ordinal", note_tr=" — «sözü»nün na'tı; sıra sayısı", punct=punct)
def SHAHR_HARAM():
    return [FI(), MAJR("الشَّهْرِ", "shahr"), NAAT("الْحَرَامِ", "haram", "jarr", note_ar=" — وَالشَّهْرُ الْحَرَامُ: مَا حُرِّمَ فِيهِ الْقِتَالُ", note_en=" — the sacred month, in which fighting was forbidden", note_tr=" — haram ay: savaşın yasak olduğu ay")]

TITLES = [{"ar": "سَبَقَ السَّيْفُ الْعَذَلَ", "en": "The Sword Came before the Blame", "tr": "Kılıç Kınamadan Önce Davrandı"}]

S1 = []
S1.append({"id": "s1", "translation": {"en": "Talk has its branches.", "tr": "Söz sözü açar (sözün dalları vardır)."},
 "tokens": [MUBTADA("الْحَدِيثُ", "hadith", note_ar=" — وَهٰذَا الْمَثَلُ الَّذِي أَوْرَدَهُ أَبُو عُبَيْدٍ فِي هٰذَا الْبَابِ", note_en=" — this is the proverb Abū ʿUbayd gives in this chapter", note_tr=" — Ebû Ubeyd'in bu bâbda zikrettiği atasözü budur"),
  tok("ذُو", "dhu", "noun", ["mubtada-khabar", "five-nouns", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The predicate (khabar), in raf' by the waw — one of the five nouns; annexed.", "Haber, esmâ-i hamseden olduğu için vâv ile merfû; muzâf."),
  MUDAF_ILAYH("شُجُونٍ", "shujun", extra=["jam-taksir"], note_ar=" — جَمْعُ شَجْنٍ: الشُّعْبَةُ وَالطَّرِيقُ فِي الْوَادِي، أَيْ: يَتَشَعَّبُ وَيَجُرُّ بَعْضُهُ بَعْضًا", note_en=" — plural of شَجْن, a branch, a by-way in a valley: talk branches out and one part draws on another", note_tr=" — şecn'in çoğulu: vadideki kol, yan yol; söz dallanır, biri ötekini çeker", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "He tells this proverb of Ḍabba ibn Udd;", "tr": "Bu atasözünü Dabbe b. Üd hakkında anlatır;"},
 "tokens": [MUDARI("يُحَدِّثُ", "haddatha", ["form-ii-verbs"], note_ar=" — يَعُودُ عَلَى الرَّاوِي الَّذِي يَنْقُلُ عَنْهُ أَبُو عُبَيْدٍ، وَهُوَ فِي كِتَابِهِ الْمُفَضَّلُ بْنُ مُحَمَّدٍ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", note_en=" — the narrator Abū ʿUbayd draws on (in his own book, al-Mufaḍḍal ibn Muḥammad); the clause opens afresh", note_tr=" — Ebû Ubeyd'in naklettiği râvî (kendi kitabında el-Mufaddal b. Muhammed); cümle isti'nâfiyyedir"),
  tok("بِهٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُحَدِّثُ».",
      "The ba is a jarr letter; هٰذَا is a demonstrative built on sukun in the seat of jarr — the phrase hangs on «tells».", "Bâ cer harfi; hâzâ işaret ismi, sükûn üzere mebnî, mahallen mecrûr — câr-mecrûr «anlatır»a müteallik.", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
  BADAL("الْمَثَلِ", "mathal", "jarr"),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُحَدِّثُ»", "; the phrase hangs on «tells»", "; câr-mecrûr «anlatır»a müteallik", gloss_tr="«hakkında»"),
  MAJR("ضَبَّةَ", "dabba-name", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_DABBA[0], note_en=" — by a fatha standing in for the kasra" + DIPT_DABBA[1], note_tr=" — kesre yerine fetha ile" + DIPT_DABBA[2]),
  BN("jarr", ("ضَبَّةَ", "Ḍabba", "Dabbe")), NM("أُدٍّ", "udd", MUNSARIF, punct="؛")]})
S1.append({"id": "s3", "translation": {"en": "he said: The beginning of it was that he had two sons; one of them was called Saʿd and the other Saʿīd.", "tr": "dedi ki: Bunun başlangıcı şuydu: Onun iki oğlu vardı; birine Sa'd, ötekine Saîd denirdi."},
 "tokens": [SAYQ("قَالَ", RAWI),
  ISTI(KANA("وَكَانَ")), ISMK("بَدْءُ", "bad-beginning", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ISHARA("ذٰلِكَ", "dhalika", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr"),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "mawadi-fath-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنَّ وَاسْمِهَا وَخَبَرِهَا فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
      "أَنَّ «that», a particle of emphasis that puts its noun in nasb; the attached «he» (Ḍabba) is its noun — and أَنَّ with its noun and predicate makes a masdar that fills the seat of nasb as the predicate of كَانَ.",
      "Enne te'kîd ve nasb harfi; bitişik «o» zamiri (Dabbe) ismi, mahallen mansûb — enne, ismi ve haberiyle kurduğu müevvel masdar kâne'nin haberi olarak mahallen mansûb.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  NOTE(KANA("كَانَ"), " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû"),
  NOTE(LAHU("لَهُ", "pron-3ms", " («onun»)"), "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ", "; the phrase hangs on the omitted, fronted predicate of كَانَ", "; câr-mecrûr kâne'nin öne alınmış mahzûf haberine müteallik"),
  tok("ابْنَانِ", "ibn", "noun", ["kana-wa-akhawatuha", "al-muthanna"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ.", "The noun of كَانَ, placed after its predicate, in raf' by the alif — a dual; the nun stands for the tanwin of the singular.", "Kâne'nin (haberinden sonraya bırakılmış) ismi, tesniye olduğu için elif ile merfû; nûn, müfreddeki tenvinin yerine.", punct="؛"),
  tok("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ — وَأَصْلُهُ يُقْوَلُ، نُقِلَتْ فَتْحَةُ الْوَاوِ إِلَى الْقَافِ ثُمَّ قُلِبَتْ أَلِفًا.",
      "Present verb in the passive, in raf' — «it is said»; from يُقْوَلُ: the waw's fatha moves to the qaf and the waw turns to alif.", "Meçhul muzâri, merfû — «denir»; aslı يُقْوَلُ: vâvın fethası kâfa nakledilir, vâv elife döner."),
  tok("لِأَحَدِهِمَا", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَأَحَدِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُقَالُ».",
      "The lam is a jarr letter; «one» is in jarr and annexed to «the two of them» — the phrase hangs on «is said».", "Lâm cer harfi; «biri» mecrûr, «ikisi» zamirine muzâf — câr-mecrûr «denir»e müteallik.", segments=[seg("لِ", "li", "prep"), seg("أَحَدِ", "ahad", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  NAIB("سَعْدٌ", "sad-name", note_ar=" — عَلَمٌ مُنْصَرِفٌ؛ وَهُوَ اللَّفْظُ الْمَقُولُ", note_en=" — a fully declined name; it is the word that is said", note_tr=" — munsarif alem; söylenen lafızdır"),
  tok("وَالْآخَرُ", "akhar", "noun", ["mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْآخَرُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «يُقَالُ».",
      "The waw conjoins; «the other» is a mubtada in raf' — the clause is conjoined to «is said».", "«ve» + «öteki» mübtedâ, merfû — cümle «denir» cümlesine ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("الْآخَرُ", "akhar", "noun")]),
  KHABAR("سَعِيدٌ", "said-name", note_ar=" — عَلَمٌ مُنْصَرِفٌ", note_en=" — a fully declined name", note_tr=" — munsarif alem", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "The two went out in search of camels of theirs; Saʿd came back and Saʿīd did not come back.", "tr": "İkisi kendilerine ait develeri aramaya çıktı; Sa'd döndü, Saîd dönmedi."},
 "tokens": [tok("فَخَرَجَا", "kharaja", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "fail", "al-muthanna"], "الْفَاءُ عَاطِفَةٌ، وَخَرَجَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "The fa conjoins; past verb built on fatha, and the alif of the two is its doer, in the seat of raf'.", "«bunun üzerine» + fetha üzere mebnî mâzî; tesniye elifi fâildir, mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("خَرَجَ", "kharaja", "verb"), seg("ا", "pron-3d", "pron")]),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«خَرَجَا»", "; the phrase hangs on «went out»", "; câr-mecrûr «çıktılar»a müteallik"),
  MAJR("طَلَبِ", "talab", extra=["masdar"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("إِبِلٍ", "ibil"),
  tok("لَهُمَا", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "naat-sifa"], "اللَّامُ حَرْفُ جَرٍّ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«إِبِلٍ».",
      "The lam is a jarr letter; «the two of them» fills the seat of jarr — the phrase hangs on an omitted adjective of «camels».", "Lâm cer harfi; «ikisi» zamiri mahallen mecrûr — câr-mecrûr «develer»in mahzûf na'tına müteallik.", punct="؛", segments=[seg("لَ", "li", "prep"), seg("هُمَا", "pron-3d", "pron")]),
  MADI("فَرَجَعَ", "rajaa", **W(FAIL_BAAD)), FAIL("سَعْدٌ", "sad-name", "propn"),
  tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates, puts the verb in jazm and turns it to the past.", "«ve» + lem: nefy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  JAZM_V("يَرْجِعْ", "rajaa"), FAIL("سَعِيدٌ", "said-name", "propn", punct=".")]})
S1.append({"id": "s5", "translation": {"en": "So whenever Ḍabba saw a figure coming towards him, he would say: «Is it Saʿd or Saʿīd?»", "tr": "Dabbe ne zaman karşıdan gelen bir karaltı görse: «Sa'd mı, Saîd mi?» derdi."},
 "tokens": [ISTI(NOTE(KANA("فَكَانَ"), " — وَخَبَرُهَا جُمْلَةُ «كُلَّمَا» بِشَرْطِهَا وَجَوَابِهَا", "; its predicate is the كُلَّمَا clause with its two halves", "; haberi, iki yarısıyla «küllemâ» cümlesidir")), DABBA("ismk"),
  tok("كُلَّمَا", "kullama", "part", ["maful-fih"], "كُلَّ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«قَالَ» الْآتِي، مُضَافٌ، وَمَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ.",
      "كُلَّ is an adverb of time in nasb, hanging on the «said» that follows, annexed; مَا makes a masdar of time: «every time that».", "Küll zaman zarfı, mansûb; gelecek «dedi»ye müteallik, muzâf; mâ masdariyye-zarfiyye: «her ne zaman ki»."),
  MADI_ALIF("رَأَى", "raa", hidden=True, **W(HID(*DB), (" — وَالْجُمْلَةُ صِلَةُ «مَا» الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا", "; the clause is the ṣila of the masdar-making مَا, with no seat", "; cümle masdariyye mâ'nın sılası, mahalli yoktur"))),
  MAFUL("شَخْصًا", "shakhs"), NAAT("مُقْبِلًا", "muqbil", "nasb", extra=["ism-fail"], note_ar=" — اسْمُ فَاعِلٍ مِنْ أَقْبَلَ", note_en=" — the active participle of أَقْبَلَ «to come towards»", note_tr=" — أَقْبَلَ'in ism-i fâili: «yönelip gelen»"),
  NOTE(QALA("قَالَ", hidden=True, punct=":"), " — وَالْجُمْلَةُ جَوَابُ «كُلَّمَا»، وَهِيَ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause answers كُلَّمَا and fills the seat of nasb as the predicate of كَانَ", "; cümle küllemâ'nın cevabı; kâne'nin haberi olarak mahallen mansûb"),
  tok("أَسَعْدٌ", "sad-name", "propn", ["al-istifham", "mubtada-khabar", "hadhf-wa-taqdir"], "الْهَمْزَةُ حَرْفُ اسْتِفْهَامٍ، وَسَعْدٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: أَهٰذَا سَعْدٌ؟ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
      "The hamza asks a question; «Saʿd» is the predicate of an omitted mubtada («is this Saʿd?»), in raf' — the clause is what is said, in the seat of nasb.", "Hemze istifham harfi; «Sa'd» mahzûf mübtedânın haberi («bu Sa'd mı?»), merfû — cümle mekūlü'l-kavl, mahallen mansûb.", segments=[seg("أَ", "hamza-istifham", "part"), seg("سَعْدٌ", "sad-name", "propn")]),
  tok("أَمْ", "am", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ مُعَادِلٌ لِلْهَمْزَةِ (أَمِ الْمُتَّصِلَةُ)، يُطْلَبُ بِهِ التَّعْيِينُ.", "The joined أَمْ «or», which balances the hamza and asks which of the two it is.", "Hemzeye denk muttasıl em «yoksa»: ikisinden hangisi olduğunu sorar."),
  ATF("سَعِيدٌ", "said-name", "propn", punct="؟")]})
S1.append({"id": "s6", "translation": {"en": "And that saying of his went round as a proverb.", "tr": "Onun bu sözü darb-ı mesel oldu."},
 "tokens": [ISTI(DHAHABAT()), KALIMATUHU(), ISHARA("هٰذِهِ", "hadhihi", "رَفْعٍ بَدَلٌ مِنْ «كَلِمَتُهُ»", "raf' as a badal of «his saying»", "merfû — «sözü»nden bedel", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre", extra=["badal"]), MATHALAN()]})
S1.append({"id": "s7", "translation": {"en": "He said: Then Ḍabba — while he was travelling, and al-Ḥārith ibn Kaʿb with him, in the sacred month — the two came upon a place.", "tr": "Dedi ki: Sonra Dabbe — haram ayda, yanında Hâris b. Ka'b ile yol alırken — ikisi bir yere vardılar."},
 "tokens": [SAYQ("قَالَ", RAWI), THUMMA(),
  tok("إِنَّ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَكُسِرَتْ هَمْزَتُهَا لِوُقُوعِهَا فِي أَوَّلِ الْكَلَامِ الْمَحْكِيِّ.", "A particle of emphasis that puts its noun in nasb and raises its predicate — its hamza takes kasra at the head of the reported speech.", "Te'kîd ve nasb harfi: ismini nasb, haberini ref eder — nakledilen sözün başında olduğu için hemzesi meksûrdur."),
  DABBA("ism_inna"),
  tok("بَيْنَمَا", "baynama", "noun", ["maful-fih"], "بَيْنَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«أَتَيَا»، وَمَا زَائِدَةٌ كَفَّتْهُ عَنِ الْإِضَافَةِ إِلَى الْمُفْرَدِ.", "بَيْنَ is an adverb of time in nasb, hanging on «came»; the extra مَا keeps it from being annexed to a single noun: «while».", "Beyne zaman zarfı, mansûb; «vardılar»a müteallik; zâid mâ onu müfrede izâfetten alıkoyar: «…iken»."),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، يَعُودُ عَلَى ضَبَّةَ.", "A detached pronoun built on fatha, in the seat of raf' as the mubtada (Ḍabba).", "Munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû (Dabbe)."),
  MUDARI("يَسِيرُ", "sara-travel", ["hollow-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «هُوَ»، وَالْجُمْلَةُ الِاسْمِيَّةُ مُضَافٌ إِلَيْهَا «بَيْنَ»", note_en=" — the clause is the predicate of «he», and the nominal clause is what بَيْنَ is annexed to", note_tr=" — cümle «hüve»nin haberi; isim cümlesi beyne'nin muzâfun ileyhidir"),
  tok("وَمَعَهُ", "maa", "noun", ["maful-fih", "al-hal-jumla-wa-rabituha", "al-bariz-al-muttasil"], "الْوَاوُ حَالِيَّةٌ، وَمَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The waw is the waw of state; مَعَ «with» is an adverb of place in nasb, hanging on an omitted fronted predicate, annexed to «him».", "Vâv hâliyye; mea mekân zarfı, mansûb; öne alınmış mahzûf habere müteallik, «o» zamirine muzâf.", segments=[seg("وَ", "wa", "conj"), seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("الْحَارِثُ", "harith-alam", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «يَسِيرُ».", "The mubtada, placed after its predicate, in raf' — the clause is a hal of the doer of «travels», in the seat of nasb.", "Muahhar mübtedâ, merfû — cümle «yol alır»ın fâilinden hâl, mahallen mansûb."),
  BN("raf", ("الْحَارِثُ", "al-Ḥārith", "Hâris")), NM("كَعْبٍ", "kab-name", MUNSARIF, punct="،"),
  *[NOTE(SHAHR_HARAM()[0], " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَسِيرُ»", "; the phrase hangs on «travels»", "; câr-mecrûr «yol alır»a müteallik"), SHAHR_HARAM()[1], NOTE(SHAHR_HARAM()[2], "", "", "")],
  tok("إِذْ", "idh", "part", ["maful-fih"], "حَرْفُ مُفَاجَأَةٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "The إِذْ of surprise, built on sukun, with no seat — the clause after it fills the seat of raf' as the predicate of إِنَّ.", "Müfâcee (ansızınlık) iz'i, sükûn üzere mebnî, mahalli yoktur — sonraki cümle inne'nin haberi olarak mahallen merfû."),
  tok("أَتَيَا", "ata", "verb", ["thulathi-mujarrad-babs", "naqis-verbs", "al-bariz-al-muttasil", "fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَعَادَتِ الْيَاءُ الَّتِي قُلِبَتْ أَلِفًا فِي «أَتَى».",
      "Past verb built on fatha; the alif of the two is its doer, in the seat of raf' — the ya that was an alif in أَتَى comes back.", "Fetha üzere mebnî mâzî; tesniye elifi fâil, mahallen merfû — «etâ»da elife dönen yâ geri gelir.", segments=[seg("أَتَيَ", "ata", "verb"), seg("ا", "pron-3d", "pron")]),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَتَيَا»", "; the phrase hangs on «came»", "; câr-mecrûr «vardılar»a müteallik"), MAJR("مَكَانٍ", "makan", punct=".")]})
S1.append({"id": "s8", "translation": {"en": "Al-Ḥārith said to Ḍabba: «Do you see this spot? I met a young man here, of such-and-such a look,", "tr": "Hâris Dabbe'ye dedi ki: «Şu yeri görüyor musun? Ben burada şöyle şöyle görünüşlü bir delikanlıya rastladım,"},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), FAIL("الْحَارِثُ", "harith-alam", "propn"),
  tok("لِضَبَّةَ", "li", "prep", ["huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَضَبَّةَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ" + DIPT_DABBA[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ».",
      "The lam is a jarr letter; Ḍabba is in jarr by a fatha standing in for the kasra" + DIPT_DABBA[1] + " — the phrase hangs on «said».", "Lâm cer harfi; Dabbe kesre yerine fetha ile mecrûr" + DIPT_DABBA[2] + " — câr-mecrûr «dedi»ye müteallik.", punct=":", segments=[seg("لِ", "li", "prep"), seg("ضَبَّةَ", "dabba-name", "propn")]),
  tok("أَتَرَى", "raa", "verb", ["al-istifham", "mudari-marfu", "naqis-verbs"], "الْهَمْزَةُ حَرْفُ اسْتِفْهَامٍ، وَتَرَى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
      "The hamza asks; «see» is a present verb in raf' by a damma estimated on the alif; its doer «you» must stay hidden — the clause is what is said, in the seat of nasb.", "Hemze istifham; terâ, elif üzerinde takdîrî damme ile merfû muzâri; fâil vücûben gizli «sen» — cümle mekūlü'l-kavl, mahallen mansûb.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَرَى", "raa", "verb")]),
  ISHARA("هٰذَا", "hadha", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb"), BADAL("الْمَوْضِعَ", "mawdi", "nasb", punct="؟"),
  tok("فَإِنِّي", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "ya-al-mutakallim"], "الْفَاءُ تَعْلِيلِيَّةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا، وَحُذِفَتْ إِحْدَى النُّونَاتِ تَخْفِيفًا.",
      "The fa gives the reason; إِنَّ is the particle of emphasis, and the ya «I» is its noun in the seat of nasb (one of the nuns is dropped for lightness).", "Fâ ta'lîl içindir; inne te'kîd ve nasb harfi, mütekellim yâ'sı ismi, mahallen mansûb (nûnlardan biri tahfîf için düşmüştür).", segments=[seg("فَ", "fa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  MADI_T("لَقِيتُ", "laqiya", who="ana", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", note_en="; the clause fills the seat of raf' as the predicate of إِنَّ", note_tr="; cümle inne'nin haberi olarak mahallen merfû"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («orada»)", note_ar=" — وَالْهَاءُ لِلْمَوْضِعِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«لَقِيتُ»", note_en=" — «it» is the spot; the phrase hangs on «I met»", note_tr=" — zamir «yer»e döner; câr-mecrûr «rastladım»a müteallik"),
  MAFUL("فَتًى", "fata-youth", extra=["ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the fatha is estimated on the alif, which drops before the tanwin: a maqṣūr noun", note_tr=" — fetha, tenvin karşısında düşen elif üzerinde takdîrîdir: maksûr isim"),
  PREP("مِنْ", "min", " — بَيَانِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ", " — it explains the kind; the phrase hangs on an omitted, fronted predicate", "; beyân içindir; câr-mecrûr öne alınmış mahzûf habere müteallik", gloss_tr="«-den»"),
  ENC_NOUN("هَيْئَتِهِ", "haya-shape", "هِ", "majr", note_ar=" — وَالْهَاءُ لِلْفَتَى", note_en=" — «his» is the young man's", note_tr=" — zamir delikanlıya döner"),
  tok("كَذَا", "kadha", "part", ["mubtada-khabar", "al-kinayat-wal-zuruf-al-mabniyya"], "كِنَايَةٌ مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«فَتًى».",
      "A word of allusion («such-and-such»), built on sukun, in the seat of raf' as the mubtada placed last — the clause qualifies «a young man», in the seat of nasb.", "Kinâye (\"şöyle şöyle\"), sükûn üzere mebnî, muahhar mübtedâ olarak mahallen merfû — cümle «delikanlı»nın na'tı, mahallen mansûb."),
  tok("وَكَذَا", "kadha", "part", ["atf-nasaq", "al-kinayat-wal-zuruf-al-mabniyya"], WA_AR + "كَذَا كِنَايَةٌ مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مَعْطُوفَةٌ عَلَى الْأُولَى.", "The waw conjoins; the second «such» is built on sukun, in the seat of raf', conjoined to the first.", "«ve» + ikinci «kezâ», sükûn üzere mebnî, birinciye ma'tûf, mahallen merfû.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("كَذَا", "kadha", "part")])]})
S1.append({"id": "s9", "translation": {"en": "and I killed him and took this sword from him.»", "tr": "onu öldürdüm ve bu kılıcı ondan aldım.»"},
 "tokens": [MADI_T("فَقَتَلْتُهُ", "qatala", who="ana", enc="هُ", note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «لَقِيتُ»", note_en="; the clause is conjoined to «I met»", note_tr="; cümle «rastladım»a ma'tûf"),
  MADI_T("وَأَخَذْتُ", "akhadha", who="ana"), JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَخَذْتُ»", note_en=" — the phrase hangs on «I took»", note_tr=" — câr-mecrûr «aldım»a müteallik"),
  ISHARA("هٰذَا", "hadha", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb"), BADAL("السَّيْفَ", "sayf", "nasb", punct=".")]})
S1.append({"id": "s10", "translation": {"en": "And lo — it was the description of Saʿīd.", "tr": "Bir de ne görsün — bu, Saîd'in eşkâliydi."},
 "tokens": [tok("فَإِذَا", "idha", "part", ["maful-fih"], "الْفَاءُ عَاطِفَةٌ، وَإِذَا حَرْفُ مُفَاجَأَةٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "The fa conjoins; إِذَا here is the particle of surprise («and lo»), with no seat.", "«bunun üzerine» + müfâcee izâ'sı («bir de ne görsün»), i'râbdan mahalli yoktur.", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  tok("هِيَ", "hiya", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، يَعُودُ عَلَى الْهَيْئَةِ الْمَوْصُوفَةِ.", "A detached pronoun built on fatha, in the seat of raf' as the mubtada — «it», the look just described.", "Munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû — anlatılan görünüşe döner."),
  KHABAR("صِفَةُ", "sifa", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), NM("سَعِيدٍ", "said-name", MUNSARIF, punct=".")]})
S1.append({"id": "s11", "translation": {"en": "Ḍabba said to him: «Show me the sword, that I may look at it.»", "tr": "Dabbe ona: «Kılıcı bana göster de bir bakayım» dedi."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), LAHU("لَهُ", "pron-3ms", " («ona»)"), DABBA("fail", punct=":"),
  tok("أَرِنِي", "ara", "verb", ["imperative-amr", "form-iv-verbs", "naqis-verbs", "mafulayn", "ya-al-mutakallim", "al-fail-al-mudmar-al-mustatir-wujuban"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "Imperative of أَرَى «to show», built on the dropping of the weak letter; its doer «you» must stay hidden; the nun guards the verb, and the ya «me» is its first object, in the seat of nasb — the clause is what is said.", "Erâ «göstermek» fiilinin emri, illet harfinin hazfi üzere mebnî; fâil vücûben gizli «sen»; nûn vikâye, yâ birinci mef'ûl, mahallen mansûb — cümle mekūlü'l-kavl.", segments=[seg("أَرِ", "ara", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  MAFUL("السَّيْفَ", "sayf", extra=["mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي", note_en=" — the second object", note_tr=" — ikinci mef'ûl"),
  tok("أَنْظُرْ", "nazara", "verb", ["jawab-al-talab", "nawasib-wa-jawazim-al-mudari"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الْأَمْرِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.",
      "Present verb in jazm as the answer to the command, its sign the sukun; the doer «I» must stay hidden.", "Emrin cevabı olarak meczûm muzâri, alâmeti sükûn; fâil vücûben gizli «ben»."),
  ILAYHI(punct=".")]})
S1.append({"id": "s12", "translation": {"en": "He handed it to him, and Ḍabba knew it.", "tr": "Hâris kılıcı ona uzattı; Dabbe de onu tanıdı."},
 "tokens": [ISTI(ENC_MADI("فَنَاوَلَهُ", "nawala-amr", "هُ", ["form-iii-verbs"], hidden=True, note_ar=HID(*HR)[0] + " — وَالْهَاءُ لِضَبَّةَ، وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ: السَّيْفَ", note_en=" (al-Ḥārith) — «him» is Ḍabba; the second object, the sword, is left unsaid", note_tr=" (Hâris) — zamir Dabbe'ye döner; ikinci mef'ûl (kılıç) mahzûf")),
  ENC_MADI("فَعَرَفَهُ", "arafa", "هُ", note_ar=" — وَالْهَاءُ لِلسَّيْفِ، وَالْفَاعِلُ بَعْدَهُ", note_en=" — «it» is the sword; its doer follows", note_tr=" — zamir kılıca döner; fâili ondan sonra gelir"),
  DABBA("fail", punct=".")]})
S1.append({"id": "s13", "translation": {"en": "He said: And at that he said, «Talk has its branches»; and his second saying went round as a proverb as well.", "tr": "Dedi ki: İşte o anda «Söz sözü açar» dedi; onun bu ikinci sözü de darb-ı mesel oldu."},
 "tokens": [SAYQ("قَالَ", RAWI),
  tok("فَعِنْدَهَا", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "الْفَاءُ زَائِدَةٌ لِتَزْيِينِ اللَّفْظِ، وَعِنْدَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«قَالَ»، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يَعُودُ عَلَى تِلْكَ الْحَالِ.",
      "The fa is extra, for the flow of the words; عِنْدَ «at» is an adverb of time in nasb hanging on «said», annexed to «it» — that moment.", "Fâ lafzı süsleyen zâid harf; inde zaman zarfı, mansûb, «dedi»ye müteallik, «o» zamirine muzâf — o âna döner.", segments=[seg("فَ", "fa", "conj"), seg("عِنْدَ", "inda", "noun"), seg("هَا", "pron-3fs", "pron")]),
  NOTE(QALA("قَالَ", hidden=True, punct=":"), HID(*DB)[0], HID(*DB)[1], HID(*DB)[2]),
  tok("إِنَّ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَكُسِرَتْ هَمْزَتُهَا بَعْدَ الْقَوْلِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.", "The particle of emphasis — its hamza takes kasra after a verb of saying; the clause is what is said, in the seat of nasb.", "Te'kîd ve nasb harfi — kavilden sonra hemzesi meksûr; cümle mekūlü'l-kavl, mahallen mansûb."),
  tok("الْحَدِيثَ", "hadith", "noun", ["inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of إِنَّ, in nasb.", "İnne'nin ismi, mansûb."),
  tok("ذُو", "dhu", "noun", ["inna-wa-akhawatuha", "five-nouns", "idafa-definiteness"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The predicate of إِنَّ, in raf' by the waw — one of the five nouns; annexed.", "İnne'nin haberi, esmâ-i hamseden olduğu için vâv ile merfû; muzâf."),
  MUDAF_ILAYH("شُجُونٍ", "shujun", extra=["jam-taksir"], punct="،"),
  DHAHABAT(), KALIMATUHU(), NAAT_ORD("الثَّانِيَةُ", "thani"), MATHALAN(None), AYDAN()]})
S1.append({"id": "s14", "translation": {"en": "Then he struck al-Ḥārith with it until he had killed him.", "tr": "Sonra kılıçla Hâris'e vurdu, nihayet onu öldürdü."},
 "tokens": [THUMMA(), MADI("ضَرَبَ", "daraba", hidden=True, **W(HID(*DB))),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)", note_ar=" — وَالْهَاءُ لِلسَّيْفِ، وَالْبَاءُ لِلِاسْتِعَانَةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ضَرَبَ»", note_en=" — «it» is the sword; the ba of the instrument; the phrase hangs on «struck»", note_tr=" — zamir kılıca döner; bâ alet içindir; câr-mecrûr «vurdu»ya müteallik"),
  MAFUL("الْحَارِثَ", "harith-alam", "propn"),
  tok("حَتَّى", "hatta", "part", ["ila-hatta-fi-wal-ba-fil-kafiya"], "حَرْفُ ابْتِدَاءٍ وَغَايَةٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ — وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا.", "حَتَّى here opens a new clause and marks the end point («until»), with no seat — the clause after it has no seat.", "Hattâ burada ibtidâ ve gâye harfi, mahalli yoktur — sonraki cümle isti'nâfiyye, mahalli yoktur."),
  ENC_MADI("قَتَلَهُ", "qatala", "هُ", hidden=True, note_ar=" — وَالْهَاءُ لِلْحَارِثِ", note_en=" — «him» is al-Ḥārith", note_tr=" — zamir Hâris'e döner", punct=".")]})
S1.append({"id": "s15", "translation": {"en": "He said: The people blamed him for that and said: «Do you kill in the sacred month?»", "tr": "Dedi ki: İnsanlar bu yüzden onu kınadılar ve: «Haram ayda mı adam öldürürsün?» dediler."},
 "tokens": [SAYQ("قَالَ", RAWI),
  tok("فَلَامَهُ", "lama", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "maful-bihi"], "الْفَاءُ زَائِدَةٌ، وَلَامَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — يَعُودُ عَلَى ضَبَّةَ، وَالْفَاعِلُ بَعْدَهُ.",
      "The fa is extra; لَامَ «blamed» is a past verb built on fatha, and «him» (Ḍabba) is its object in the seat of nasb; its doer follows.", "Fâ zâid; lâme «kınadı» fetha üzere mebnî mâzî, «onu» (Dabbe) mef'ûlün bih, mahallen mansûb; fâili ondan sonra gelir.", segments=[seg("فَ", "fa", "conj"), seg("لَامَ", "lama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  FAIL("النَّاسُ", "nas"), NOTE(ALA(), " — لِلتَّعْلِيلِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«لَامَهُ»", " — of the cause («for»); the phrase hangs on «blamed him»", "; sebep bildirir; câr-mecrûr «kınadı»ya müteallik"),
  ISHARA("ذٰلِكَ", "dhalika", "جَرٍّ", "jarr", "mecrûr"),
  VERB_WAW("وَقَالُوا", "qala", ["hollow-verbs", "maful-bihi"], punct=":"),
  tok("أَتَقْتُلُ", "qatala", "verb", ["al-istifham", "mudari-marfu", "khuruj-al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتَقْتُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
      "The hamza asks in reproach; «kill» is a present verb in raf', its doer «you» hidden — the clause is what is said, in the seat of nasb.", "Hemze inkârî istifham; taktulu merfû muzâri, fâil vücûben gizli «sen» — cümle mekūlü'l-kavl, mahallen mansûb.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَقْتُلُ", "qatala", "verb")]),
  NOTE(SHAHR_HARAM()[0], " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَقْتُلُ»", "; the phrase hangs on «kill»", "; câr-mecrûr «öldürürsün»e müteallik"), SHAHR_HARAM()[1], NAAT("الْحَرَامِ", "haram", "jarr", punct="؟")]})
S1.append({"id": "s16", "translation": {"en": "He said: «The sword came before the blame»; and his third saying went round as a proverb as well.", "tr": "O da: «Kılıç kınamadan önce davrandı» dedi; onun bu üçüncü sözü de darb-ı mesel oldu."},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True, punct=":")),
  NOTE(MADI("سَبَقَ", "sabaqa", **W(FAIL_BAAD)), " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekūlü'l-kavl, mahallen mansûb"),
  FAIL("السَّيْفُ", "sayf"),
  MAFUL("الْعَذَلَ", "adhl", note_ar=" — وَالْعَذَلُ: اللَّوْمُ", note_en=" — blame, reproach", note_tr=" — kınama", punct="،"),
  DHAHABAT(), KALIMATUHU(), NAAT_ORD("الثَّالِثَةُ", "thalith"), MATHALAN(None), AYDAN()]})

NEW_GLOSS = {
 "dabba-name": NP("ضَبَّة", "Ḍabba ibn Udd — a forefather of the Arabs of Muḍar; a man's name with the feminine ending, so a diptote", "Dabbe b. Üd — Mudar Araplarının atalarından; tâ-i te'nîsli erkek ismi, gayr-i munsarif"),
 "udd": NP("أُدّ", "Udd — the father of Ḍabba, of the line of Muḍar; a fully declined name", "Üd — Dabbe'nin babası, Mudar soyundan; munsarif isim"),
 "kab-name": NP("كَعْب", "Kaʿb — a man's name, fully declined; here al-Ḥārith ibn Kaʿb", "Ka'b — erkek ismi, munsarif; burada Hâris b. Ka'b"),
 "shujun": NN("شُجُون", "ش ج ن", "branches, by-ways (pl. of شَجْن: a branch of a valley, a winding way) — الْحَدِيثُ ذُو شُجُونٍ «talk has its branches: one thing leads to another»", "kollar, yan yollar (şecn'in çoğulu: vadinin kolu, dolambaçlı yol) — الْحَدِيثُ ذُو شُجُونٍ «söz sözü açar»"),
}
GLOSS_HERE = {
 "adhl": ("blame, reproach — سَبَقَ السَّيْفُ الْعَذَلَ «the sword came before the blame» (the proverb reads الْعَذَل with fatha on the dhāl)", "kınama, ayıplama — سَبَقَ السَّيْفُ الْعَذَلَ «kılıç kınamadan önce davrandı» (atasözünde zâl fethalıdır)"),
 "harith-alam": ("al-Ḥārith — a man's name; here al-Ḥārith ibn Kaʿb, who killed Ḍabba's son", "Hâris — erkek ismi; burada Dabbe'nin oğlunu öldüren Hâris b. Ka'b"),
 "sad-name": ("Saʿd — a man's name; here Saʿd, the son of Ḍabba who came back", "Sa'd — erkek ismi; burada Dabbe'nin dönen oğlu Sa'd"),
 "said-name": ("Saʿīd — a man's name; here Saʿīd, the son of Ḍabba who did not come back", "Saîd — erkek ismi; burada Dabbe'nin dönmeyen oğlu Saîd"),
}
LEMMA_HERE = {"adhl": "عَذَل"}

FOR_HOCA = [
 ("«يُحَدِّثُ»: active (the narrator, al-Mufaḍḍal in Abū ʿUbayd's own book) or passive «يُحَدَّثُ» on the Faṣl's words alone", "«يُحَدِّثُ»: malûm (râvî; Ebû Ubeyd'in kendi kitabında el-Mufaddal) mı, yoksa yalnız Fasl'ın lafzına göre meçhul «يُحَدَّثُ» mü"),
 ("«الْعَذَلَ» with fatha on the dhāl (the proverb as it is known); Abū ʿUbayd's following remark «ويقال إنما هو العذل، وإنما جاز في الشعر للضرورة» is ambiguous unvowelled", "«الْعَذَلَ» zâl fethalı (bilinen şekliyle); Ebû Ubeyd'in arkasından gelen «ويقال إنما هو العذل…» sözü harekesiz hâliyle müphemdir"),
 ("«كَلِمَتُهُ هٰذِهِ»: the demonstrative read as a badal (a naʿt is also said)", "«كَلِمَتُهُ هٰذِهِ»: işaret ismi bedel okundu (na't da denir)"),
 ("«فَعِنْدَهَا»: the fa read as extra (zāʾida) after «قَالَ:»", "«فَعِنْدَهَا»: «قَالَ:»dan sonraki fâ zâide okundu"),
 ("«مَثَلًا» in «فَذَهَبَتْ كَلِمَتُهُ … مَثَلًا»: read as a ḥāl", "«فَذَهَبَتْ كَلِمَتُهُ … مَثَلًا»daki «مَثَلًا» hâl okundu"),
]

MANIFEST = manifest(SLUG, level=4, title=TITLES[0],
    subtitle={"ar": "حِكَايَةُ ضَبَّةَ بْنِ أُدٍّ وَأَمْثَالِهِ الثَّلَاثَةِ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "The tale of Ḍabba ibn Udd and his three sayings that became proverbs — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Dabbe b. Üd'ün hikâyesi ve darb-ı mesel olan üç sözü — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="p. 79 (printed 1:67), bāb 1", pages_ar="ص ٧٩ (الْمَطْبُوعُ ١: ٦٧)، الْبَابُ الْأَوَّلُ",
    span_en="Abū ʿUbayd's entry «الحديث ذو شجون»: the proverb as the heading, then the whole tale he tells of Ḍabba ibn Udd, from «يحدث بهذا المثل» to «فذهبت كلمته الثالثة مثلاً أيضاً»",
    span_tr="Ebû Ubeyd'in «الحديث ذو شجون» maddesi: başlıkta atasözü, ardından Dabbe b. Üd hakkında anlattığı hikâyenin tamamı («يحدث بهذا المثل»den «فذهبت كلمته الثالثة مثلاً أيضاً»ya)",
    span_ar="مَادَّةُ أَبِي عُبَيْدٍ «الْحَدِيثُ ذُو شُجُونٍ»: الْمَثَلُ عُنْوَانًا، ثُمَّ الْحِكَايَةُ كُلُّهَا مِنْ «يُحَدِّثُ بِهٰذَا الْمَثَلِ» إِلَى «فَذَهَبَتْ كَلِمَتُهُ الثَّالِثَةُ مَثَلًا أَيْضًا»",
    corrections=[("لوم يرجع", "وَلَمْ يَرْجِعْ"), ("مثقلاً", "مَثَلًا"), ("رني", "أَرِنِي")],
    witness_ar="«كِتَابُ الْأَمْثَالِ» لِأَبِي عُبَيْدٍ نَفْسِهِ (تَحْقِيقُ قَطَامِش، الشَّامِلَةُ ١٣٥، ص ٦١–٦٢)",
    witness_en="Abū ʿUbayd's own Kitāb al-amthāl (ed. ʿAbd al-Majīd Qaṭāmish, Dār al-Maʾmūn 1980; Shamela 135, printed pp. 61–62)",
    witness_tr="Ebû Ubeyd'in kendi Kitâbü'l-emsâl'i (thk. Abdülmecîd Katâmiş, Dâru'l-Me'mûn 1980; Şâmile 135, s. 61–62)",
    hoca=FOR_HOCA, madrib=None)
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, LEMMA_HERE)
