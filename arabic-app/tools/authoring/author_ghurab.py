"""Author content/samples/al-ghurab-wa-al-thalab — «الْغُرَابُ وَالثَّعْلَبُ», the twenty-eighth ORIGINAL story, the eighth at Level 1 (wave 126).

ORIGINAL graded Arabic: the fable of the crow and the fox (Aesop; La Fontaine) retold for beginners — a crow finds a piece of
cheese, a hungry fox flatters it into speaking, the cheese falls, and the crow learns not to trust a liar's praise. Twelve
sentences in four chapters; two entries new to the lexicon (ثَعْلَب، جُبْن). Regenerate with: python3 tools/authoring/author_ghurab.py
"""
import json, os, pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "al-ghurab-wa-al-thalab"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *
from story_kit import _pre
import sarf_gen as _sg

PRON.update({"كَ": "pron-2ms", "ي": "pron-1s", "نِي": "pron-1s"}); PRON_AR.update({"كَ": "الْكَافُ", "ي": "الْيَاءُ", "نِي": "الْيَاءُ"})
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_F = lambda full="فَقَالَ", punct=None, hidden=False: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, punct=punct, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
MUDAF_NOTE = ("، مُضَافٌ", ", annexed", ", muzâf")
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
HAL_FULL = (" — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the nominal clause fills the seat of nasb as a hal", "; isim cümlesi hâl olarak mahallen mansûb")
ANNA = lambda role=("", "", ""): tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".", "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".", "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
ISM_ANNA = lambda full, lex, punct=None, enc=None: tok(full, lex, "noun", ["inna-wa-akhawatuha", "inna-am-anna"] + (["idafa-definiteness", "al-bariz-al-muttasil"] if enc else []),
    "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + ("، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" if enc else "") + ".", "The noun of أَنَّ, in nasb" + ("; annexed to the attached pronoun" if enc else "") + ".", "Enne'nin ismi, mansûb" + ("; bitişik zamire muzâf" if enc else "") + ".",
    punct=punct, segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")] if enc else None)
KH_ANNA_N = lambda full, lex, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha", "inna-am-anna"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of أَنَّ, in raf'.", "Enne'nin haberi, merfû.", punct=punct)
WAL_JUBN_HAL = lambda: tok("وَالْجُبْنُ", "jubn", "noun", ["al-hal-jumla-wa-rabituha", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَالْجُبْنُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ" + HAL_FULL[0] + ".", "The waw opens a hal clause; «the cheese» is its mubtada, in raf'" + HAL_FULL[1] + ".", "Hâl vâvı; «peynir» mübtedâ, merfû" + HAL_FULL[2] + ".", segments=[seg("وَ", "wa", "conj"), seg("الْجُبْنُ", "jubn", "noun")])
GHURABU_MUNADA = lambda punct=None: tok("غُرَابُ", "ghurab", "noun", ["vocative-munada"], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The called noun — an indefinite made definite by the call, built on damma in the seat of nasb.", "Münâdâ — nekre-i maksûde, damme üzere mebnî, mahallen mansûb.", punct=punct)
JIDDAN = lambda punct=None: tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: جَدَّ جِدًّا، وَالْمَعْنَى: كَثِيرًا.", "«very» — the absolute object of a dropped verb, frozen into an adverb of degree.", "«çok» — hazfedilmiş bir fiilin mef'ûl-i mutlakı, derece zarfı olarak kalıplaşmıştır.", punct=punct)
WA_ANA = lambda: tok("وَأَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], WA_AR + "أَنَا ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; «I» is a detached pronoun built on sukun, the mubtada in the seat of raf'.", "Vâv atıf; «ben» sükûn üzere mebnî munfasıl zamir, mübtedâ olarak mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("أَنَا", "ana", "pron")])
LAN = lambda: tok("لَنْ", "lan", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "لَنْ denies the future and puts the verb in nasb.", "Len — nefiy, nasb ve istikbâl harfi.")
MAN_SHART = lambda: tok("مَنْ", "man", "pron", ["al-majzum-wal-shart-wal-jaza", "mubtada-khabar", "al-mabni-wal-mudmar"], "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُهُ.", "«whoever» — the conditional noun built on sukun, the mubtada in the seat of raf'; the condition and its answer are its predicate.", "«her kim» — sükûn üzere mebnî şart ismi, mübtedâ olarak mahallen merfû; şart ve cevap cümleleri haberi.")
MADAHAKA = lambda: tok("مَدَحَكَ", "madaha", "verb", ["al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«praises you» — a past verb in the seat of jazm as the verb of the condition; the doer «he» is hidden and the attached «you» is its object.", "«seni överse» — şart fiili olarak mahallen meczûm mâzî; fâil gizli «o», bitişik «seni» mef'ûlün bih.", segments=[seg("مَدَحَ", "madaha", "verb"), seg("كَ", "pron-2ms", "pron")])
FA_HUWA = lambda: tok("فَهُوَ", "huwa", "pron", ["al-fa-fi-jawab-al-shart", "al-majzum-wal-shart-wal-jaza", "mubtada-khabar", "al-mabni-wal-mudmar"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "The fa ties the answer of the condition; «he» is a detached pronoun, the mubtada; the clause is the answer, in the seat of jazm.", "Fâ şartın cevabını bağlar; «o» munfasıl zamir, mübtedâ; cümle şartın cevabı olarak mahallen meczûm.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")])
FAL_DARS = lambda punct=None: tok("فَالدَّرْسُ", "dars", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَالدَّرْسُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَخَبَرُهُ الْجُمْلَةُ بَعْدَهُ.", "The fa opens the moral; «the lesson» is the mubtada, in raf', and the sentence after it is its predicate.", "Fâ isti'nâf içindir; «ders» mübtedâ, merfû; sonraki cümle haberidir.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg("الدَّرْسُ", "dars", "noun")])

TITLES = [{"ar": "الْغُرَابُ وَالْجُبْنُ", "en": "The crow and the cheese", "tr": "Karga ve peynir"},
          {"ar": "حِيلَةُ الثَّعْلَبِ", "en": "The fox's trick", "tr": "Tilkinin hilesi"},
          {"ar": "الصَّوْتُ", "en": "The voice", "tr": "Ses"},
          {"ar": "الدَّرْسُ", "en": "The lesson", "tr": "Ders"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "A crow found a piece of cheese; it took it and went to a tree.", "tr": "Bir karga bir parça peynir buldu; onu aldı ve bir ağaca gitti."},
 "tokens": [MADI("وَجَدَ", "wajada", ["mithal-verbs"]), FAIL("غُرَابٌ", "ghurab"), MAFUL("قِطْعَةَ", "qita", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("جُبْنٍ", "jubn", punct="،"), ENC_MADI("فَأَخَذَهَا", "akhadha", "هَا", hidden=True), MADI("وَذَهَبَ", "dhahaba", hidden=True), ILA(), MAJR("شَجَرَةٍ", "shajara", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "The crow stood on top of the tree with the cheese in its mouth.", "tr": "Karga, peynir ağzında, ağacın tepesinde durdu."},
 "tokens": [MADI("وَقَفَ", "waqafa", ["mithal-verbs"]), FAIL("الْغُرَابُ", "ghurab"), ZARF("فَوْقَ", "fawqa"), MUDAF_ILAYH("الشَّجَرَةِ", "shajara"), WAL_JUBN_HAL(), PREP("فِي", "fi", " — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ", "; the jarr phrase is the predicate", "; câr-mecrûr haberdir", gloss_tr="«-de»"), ENC_NOUN("فَمِهِ", "fam", "هِ", "majr", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "Under the tree there was a hungry fox.", "tr": "Ağacın altında aç bir tilki vardı."},
 "tokens": [KANA("وَكَانَ"), ZARF("تَحْتَ", "tahta", note_ar=KH_MUQ[0].replace("الْجَارُّ وَالْمَجْرُورُ", "الظَّرْفُ"), note_en="; the adverb phrase is the FRONTED predicate of كَانَ", note_tr="; zarf, kâne'nin öne alınmış haberi"), MUDAF_ILAYH("الشَّجَرَةِ", "shajara"), ISMK("ثَعْلَبٌ", "thalab", muakhkhar=True), NAAT("جَائِعٌ", "jai", "raf", ["ism-fail"], punct=".")]})
S2 = []
S2.append({"id": "s1", "translation": {"en": "The fox saw the cheese and wanted to take it by a trick.", "tr": "Tilki peyniri gördü ve onu bir hileyle almak istedi."},
 "tokens": [MADI_ALIF("رَأَى", "raa"), FAIL("الثَّعْلَبُ", "thalab"), MAFUL("الْجُبْنَ", "jubn", punct="،"), MADI("فَأَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True), AN_MAFUL(), MANSUB_AN("يَأْخُذَهُ", "akhadha", enc="هُ"), BI_NOUN("بِحِيلَةٍ", "hila", "حِيلَةٍ", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "He said to the crow: «O crow, your colour is very beautiful!»", "tr": "Kargaya dedi: «Ey karga, rengin çok güzel!»"},
 "tokens": [QALA_F("فَقَالَ", hidden=True), LI_AL("لِلْغُرَابِ", "ghurab", "الْغُرَابِ", punct=":"), YA(), GHURABU_MUNADA(punct="،"), ENC_NOUN("لَوْنُكَ", "lawn", "كَ", "mubtada"), KHABAR("جَمِيلٌ", "jamil"), JIDDAN(punct="!")]})
S2.append({"id": "s3", "translation": {"en": "«And I know that your voice is beautiful too.»", "tr": "«Sesinin de güzel olduğunu biliyorum.»"},
 "tokens": [WA_ANA(), MUDARI("أَعْرِفُ", "arafa", ["mafulayn"], who="أَنَا", wujub=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en="; the clause is the predicate of «I»", note_tr="; cümle «ben»in haberi"), ANNA((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ أَعْرِفُ", "; the clause it builds stands for both objects of «I know»", "; kurduğu müevvel masdar a'rifu'nun iki mef'ûlünün yerini tutar")),
  ISM_ANNA("صَوْتَكَ", "sawt", enc="كَ"), KH_ANNA_N("جَمِيلٌ", "jamil"), tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ، وَالْمَعْنَى: كَذٰلِكَ.", "«too» — the absolute object of a dropped verb, frozen into an adverb.", "«de» — hazfedilmiş bir fiilin mef'ûl-i mutlakı, zarf gibi kalıplaşmıştır.", punct=".")]})
S3 = []
S3.append({"id": "s1", "translation": {"en": "The crow was glad at the fox's words and wanted to speak.", "tr": "Karga tilkinin sözlerine sevindi ve konuşmak istedi."},
 "tokens": [MADI("فَرِحَ", "fariha"), FAIL("الْغُرَابُ", "ghurab"), BI_NOUN("بِكَلَامِ", "kalam", "كَلَامِ", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الثَّعْلَبِ", "thalab", punct="،"), MADI("وَأَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True), AN_MAFUL(), MANSUB_AN("يَتَكَلَّمَ", "takallama", ["form-v-verbs"], punct=".")]})
S3.append({"id": "s2", "translation": {"en": "It opened its mouth, and the cheese fell to the ground.", "tr": "Ağzını açtı ve peynir yere düştü."},
 "tokens": [MADI("فَفَتَحَ", "fataha", hidden=True), ENC_NOUN("فَمَهُ", "fam", "هُ", "maful", punct="،"), MADI("فَسَقَطَ", "saqata"), FAIL("الْجُبْنُ", "jubn"), ALA(), MAJR("الْأَرْضِ", "ard", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "The fox took the cheese and ate it, then laughed and went away.", "tr": "Tilki peyniri aldı ve yedi; sonra güldü ve gitti."},
 "tokens": [MADI("فَأَخَذَ", "akhadha"), FAIL("الثَّعْلَبُ", "thalab"), MAFUL("الْجُبْنَ", "jubn"), ENC_MADI("وَأَكَلَهُ", "akala", "هُ", hidden=True, punct="،"), THUMMA(), MADI("ضَحِكَ", "dahika", hidden=True), MADI("وَذَهَبَ", "dhahaba", hidden=True, punct=".")]})
S4 = []
S4.append({"id": "s1", "translation": {"en": "The crow was sad, and it knew that the fox had lied to it.", "tr": "Karga üzüldü ve tilkinin ona yalan söylediğini anladı."},
 "tokens": [MADI("حَزِنَ", "hazina"), FAIL("الْغُرَابُ", "ghurab", punct="،"), MADI("وَعَرَفَ", "arafa", ["mafulayn"], hidden=True), ANNA((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَرَفَ", "; the clause it builds stands for both objects of «it knew»", "; kurduğu müevvel masdar arafe'nin iki mef'ûlünün yerini tutar")), ISM_ANNA("الثَّعْلَبَ", "thalab"), MADI("كَذَبَ", "kadhaba", hidden=True, note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]), ALAYHI(punct=".")]})
S4.append({"id": "s2", "translation": {"en": "It said to itself: «I will never listen to a liar's words again.»", "tr": "Kendi kendine dedi: «Bir daha asla yalancının sözünü dinlemeyeceğim.»"},
 "tokens": [QALA("وَقَالَ", hidden=True), FI(), ENC_NOUN("نَفْسِهِ", "nafs", "هِ", "majr", punct=":"), LAN(), MANSUB_AN("أَسْمَعَ", "samia", by="لَنْ", who="أَنَا", wujub=True), MAFUL("كَلَامَ", "kalam", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْكَاذِبِ", "kadhib-liar", extra=["ism-fail"]),
  tok("مَرَّةً", "marra-once", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (أَوْ مَفْعُولٌ مُطْلَقٌ).", "«a time» — an adverb of time in nasb (or an absolute object).", "«bir kez» — mansûb zaman zarfı (ya da mef'ûl-i mutlak)."), NAAT("أُخْرَى", "ukhra", "nasb", ["ism-maqsur-manqus", "mamnu-min-sarf"], note_ar=" — بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", note_en=" — its fatha estimated on the alif", note_tr=" — fethası elif üzerinde takdîrî", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "The lesson: whoever praises you with lies wants something from you.", "tr": "Ders: seni yalanla öven, senden bir şey istiyordur."},
 "tokens": [FAL_DARS(punct=":"), MAN_SHART(), MADAHAKA(), BI_NOUN("بِالْكَذِبِ", "kadhib", "الْكَذِبِ"), FA_HUWA(), MUDARI("يُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en="; the clause is the predicate of «he»", note_tr="; cümle «o»nun haberi"), MAFUL("شَيْئًا", "shay"), MINKA(punct=".") if "MINKA" in dir() else JARR_PRON("مِنْكَ", "min", "مِنْ", "كَ", " («senden»)", punct=".")]})
CHAPS = [S1, S2, S3, S4]
PREF = ["qisas-al-nabiyyin-1", "al-kafiya", "al-asad-wa-al-arnab", "juha-wa-al-himar", "luqman-wa-ibnuh", "al-amana-wa-al-khashaba", "ashab-al-ghar", "adam-wa-iblis", "musa-wa-firawn", "izhar-al-asrar", "talkhis-al-miftah", "aqaid-ahl-al-sunna"]
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
PREF = [p for p in PREF if _pkg_dir(p).joinpath("glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF if (_pkg_dir(p) / "morphology.json").exists()}
def find_gloss(k):
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    for p in PREF:
        if k in _M.get(p, {}): return _M[p][k]
    return None
NEW_GLOSS = {
 "thalab": {"lemma": "ثَعْلَب", "root": "ث ع ل ب", "pos": "noun", "plural": "ثَعَالِب", "gloss": {"en": "a fox", "tr": "tilki"}, "level": 1},
 "jubn": {"lemma": "جُبْن", "root": "ج ب ن", "pos": "noun", "gloss": {"en": "cheese", "tr": "peynir"}, "level": 1},
}
used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k)
    if e is None: missing.append(k)
    else: GLOSS[k] = e
assert not missing, missing
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par
LEVEL_NAME = json.loads((ROOT / "content/samples/musa-wa-firawn/manifest.json").read_text(encoding="utf-8")).get("levelName", "Beginner")
MANIFEST = {
 "id": "al-ghurab-wa-al-thalab", "storyGroup": "al-ghurab-wa-al-thalab",
 "title": {"ar": "الْغُرَابُ وَالثَّعْلَبُ", "en": "The Crow and the Fox", "tr": "Karga ile Tilki"},
 "subtitle": {"ar": "غُرَابٌ وَجَدَ جُبْنًا، وَثَعْلَبٌ أَخَذَهُ بِالْمَدْحِ الْكَاذِبِ — حِكَايَةٌ لِلْمُسْتَوَى الْأَوَّلِ", "en": "A crow finds cheese and a fox takes it with false praise — a fable for the first level", "tr": "Peynir bulan karga ve onu yalancı övgüyle alan tilki — birinci seviye için bir fabl"},
 "level": 1, "levelName": LEVEL_NAME, "version": "0.1.0", "published": "2026-11-09", "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِحِكَايَةِ الْغُرَابِ وَالثَّعْلَبِ الْمَشْهُورَةِ (إِيسُوب؛ لَافُونْتِين)، بِأُسْلُوبِ كِتَابِ الْقِرَاءَةِ الْمُتَدَرِّجِ. لَيْسَ فِيهَا نَصٌّ مَنْقُولٌ.",
  "en": "ORIGINAL Level-1 graded Arabic: the well-known fable of the crow and the fox (Aesop; La Fontaine) retold for beginners in the wording of a graded reader. No text is quoted from any source.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: meşhur karga ile tilki fablı (Ezop; La Fontaine), kolaylaştırılmış okuyucu üslûbuyla yeni başlayanlar için yeniden anlatılmıştır. Hiçbir kaynaktan metin aktarılmamıştır.",
  "reviewStatus": "pending-scholarly-review"},
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
