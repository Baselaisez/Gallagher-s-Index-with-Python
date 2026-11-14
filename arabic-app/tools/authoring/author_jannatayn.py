"""Author content/samples/sahib-al-jannatayn — «صَاحِبُ الْجَنَّتَيْنِ», the twenty-sixth ORIGINAL story and the sixth at Level 3 (wave 124).

ORIGINAL graded Arabic: the parable of the man with two gardens (Sūrat al-Kahf) RETOLD FREELY in a graded reader's wording —
the rich owner of two vineyards boasts to his poor believing companion, denies that his garden could ever perish or that the
Hour is near, is counselled to thank God, laughs it off; fire from the sky destroys both gardens in a night, and he wakes to
dry earth and regret. No āya is quoted and no sentence is Qurʾānic wording; the Qurʾān's own phrases were deliberately
avoided and paraphrased. Four chapters, seventeen sentences; the DUAL is the grammar thread (رَجُلَانِ، جَنَّتَانِ، الْجَنَّتَيْنِ،
جَنَّتَيْهِ، كَانَتَا، صَارَتَا، تُعْطِيَانِ، حَوْلَهُمَا). One entry is new — عِنَب. Regenerate with:
python3 tools/authoring/author_jannatayn.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "sahib-al-jannatayn"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *
from story_kit import _pre
import sarf_gen as _sg

PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمَا": "pron-3d", "هِمَا": "pron-3d"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "هُمْ": "هُمْ", "هِمْ": "هِمْ", "هُمَا": "هُمَا", "هِمَا": "هُمَا"})

MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_F = lambda full="فَقَالَ", punct=None, hidden=False: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, punct=punct, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
LAFZ = (" — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl")
MUDAF_NOTE = ("، مُضَافٌ", ", annexed", ", muzâf")
KH_KANA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
HAL_FULL = (" — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the nominal clause fills the seat of nasb as a hal", "; isim cümlesi hâl olarak mahallen mansûb")
NAAT_CL_NASB = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ", "; the clause fills the seat of nasb as the adjective of the indefinite noun before it", "; cümle, önceki nekre ismin na'tı olarak mahallen mansûb")
DUAL_RAF = "بِالْأَلِفِ لِأَنَّهُ مُثَنًّى"; DUAL_JN = "بِالْيَاءِ لِأَنَّهُ مُثَنًّى"
DUAL_N = (" — عَلَامَةُ الْمُثَنَّى", " — the dual's sign", " — tesniye alâmeti")

WA_HUWA_HAL = lambda: tok("وَهُوَ", "huwa", "pron", ["al-hal-jumla-wa-rabituha", "mubtada-khabar", "al-mabni-wal-mudmar"],
    "الْوَاوُ حَالِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw opens a hal clause; «he» is a detached pronoun built on fatha, the mubtada in the seat of raf'.", "Hâl vâvı; «o» munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")])
WA_HUWA_ATF = lambda: tok("وَهُوَ", "huwa", "pron", ["atf-nasaq", "mubtada-khabar", "al-mabni-wal-mudmar"],
    WA_AR + "هُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins a second clause; «He» is a detached pronoun built on fatha, the mubtada in the seat of raf'.", "Vâv atıf; «O» munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")])
ANA = lambda: tok("أَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — a detached pronoun built on sukun, the mubtada in the seat of raf'.", "«ben» — sükûn üzere mebnî munfasıl zamir, mübtedâ olarak mahallen merfû.")
AMMA = lambda full="أَمَّا": tok(full, "amma", "part", ["al-majzum-wal-shart-wal-jaza", "al-fa-fi-jawab-al-shart"] + (["atf-nasaq"] if full.startswith("وَ") else []),
    (WA_AR if full.startswith("وَ") else "") + "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ، وَجَوَابُهَا مَقْرُونٌ بِالْفَاءِ.", ("The waw conjoins; " if full.startswith("وَ") else "") + "أَمَّا «as for» — a particle of condition, detailing and emphasis; its answer carries the fa.", ("Vâv atıf; " if full.startswith("وَ") else "") + "Emmâ — şart, tafsîl ve te'kîd harfi; cevabı fâ ile gelir.",
    segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")] if full.startswith("وَ") else None)
FA_JAWAB_AMMA_MUDARI = lambda full, lex, extra=None, who="أَنَا", punct=None: tok(full, lex, "verb", ["al-fa-fi-jawab-al-shart", "mudari-marfu", "al-fail-al-mudmar-al-mustatir-wujuban"] + (extra or []),
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: " + who + " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
    "The fa opens the answer of أَمَّا; the present verb is in raf', its doer «" + who + "» hidden of necessity; the clause is the predicate of the mubtada.", "Fâ, emmâ'nın cevabına gelmiştir; merfû muzâri, fâil «" + who + "» vücûben müstetir; cümle mübtedânın haberi.",
    punct=punct, segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])
FA_KANA_AMMA = lambda: tok("فَكَانَ", "kana", "verb", ["al-fa-fi-jawab-al-shart", "kana-wa-akhawatuha", "hollow-verbs"],
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
    "The fa opens the answer of أَمَّا; كَانَ's noun «he» is hidden; the clause is the predicate of the mubtada.", "Fâ, emmâ'nın cevabına gelmiştir; kâne'nin ismi gizli «o»; cümle mübtedânın haberi.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")])
KANATA = lambda: tok("فَكَانَتَا", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
    FA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهَا.", "The fa conjoins; كَانَ with the feminine ta and the ALIF OF THE TWO as its noun, in the seat of raf' («the two of them were»).", "Fâ atıf; kâne, te'nîs tâ'sı ve ismi olan tesniye elifi ile («ikisi … idi»).",
    segments=[seg("فَ", "fa", "conj"), seg("كَانَتْ", "kana", "verb"), seg("ا", "pron-3d", "pron")])
SARATA = lambda: tok("صَارَتَا", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
    "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهَا.", "صَارَ «became» with the feminine ta and the alif of the two as its noun («the two had become»).", "Sâra «oldu», te'nîs tâ'sı ve ismi olan tesniye elifi ile («ikisi … olmuştu»).",
    segments=[seg("صَارَتْ", "sara", "verb"), seg("ا", "pron-3d", "pron")])
TUTIYANI = lambda: tok("تُعْطِيَانِ", "aata", "verb", ["afal-khamsa", "kana-wa-akhawatuha", "form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "fail"],
    "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + KH_KANA_CL[0] + ".",
    "«the two give» — one of the five verbs, in raf' by the fixed nun; the alif of the two is its doer" + KH_KANA_CL[1] + ".", "«ikisi verir» — ef'âl-i hamseden, nûnun sübûtu ile merfû; tesniye elifi fâil" + KH_KANA_CL[2] + ".",
    segments=[seg("تُعْطِيَا", "aata", "verb"), seg("نِ", "nun-rafa", "part")] if False else None)
HAWLAHUMA = lambda: tok("حَوْلَهُمَا", "hawla", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِاسْمِ كَانَ.",
    "«around the two of them» — an adverb of place annexed to the dual pronoun; the FRONTED predicate, and the clause is a second adjective of كَانَ's noun.", "«ikisinin çevresinde» — tesniye zamirine muzâf mekân zarfı; öne alınmış haber, cümle kâne'nin isminin ikinci na'tı.",
    segments=[seg("حَوْلَ", "hawla", "noun"), seg("هُمَا", "pron-3d", "pron")])
WA_BAYNAHUMA = lambda: tok("وَبَيْنَهُمَا", "bayna", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar"],
    WA_AR + "بَيْنَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرٌ مُقَدَّمٌ.", "The waw conjoins; «between the two» — an adverb annexed to the dual pronoun, the fronted predicate.", "Vâv atıf; «ikisinin arasında» — tesniye zamirine muzâf zarf, öne alınmış haber.",
    segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")])
INDAHU = lambda: tok("عِنْدَهُ", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«with Him» — an adverb of place annexed to the pronoun.", "«O'nun katında» — zamire muzâf mekân zarfı.", segments=[seg("عِنْدَ", "inda", "noun"), seg("هُ", "pron-3ms", "pron")])
LAN = lambda full="لَنْ": tok(full, "lan", "part", ["nawasib-wa-jawazim-al-mudari"] + (["atf-nasaq"] if full.startswith("وَ") else []), (WA_AR if full.startswith("وَ") else "") + "لَنْ حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", ("The waw conjoins; " if full.startswith("وَ") else "") + "لَنْ denies the future and puts the verb in nasb.", ("Vâv atıf; " if full.startswith("وَ") else "") + "Len — nefiy, nasb ve istikbâl harfi.",
    segments=[seg("وَ", "wa", "conj"), seg("لَنْ", "lan", "part")] if full.startswith("وَ") else None)
ABADAN = lambda punct=None: tok("أَبَدًا", "abadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ لِلْمُسْتَقْبَلِ مَنْصُوبٌ بِالْفَتْحَةِ — يُلَازِمُ النَّفْيَ.", "«ever» — an adverb of future time in nasb; it keeps to negated clauses («never»).", "«asla» — gelecek zaman zarfı, mansûb; nefiy ile kullanılır.", punct=punct)
ANNA = lambda role=("", "", ""): tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".", "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".", "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
ISM_ANNA = lambda full, lex, pos="noun", note=("", "", ""), punct=None: tok(full, lex, pos, ["inna-wa-akhawatuha", "inna-am-anna"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + note[0] + ".", "The noun of أَنَّ, in nasb" + note[1] + ".", "Enne'nin ismi, mansûb" + note[2] + ".", punct=punct)
KH_ANNA_N = lambda full, lex, extra=None, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha", "inna-am-anna"] + (extra or []), "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of أَنَّ, in raf'.", "Enne'nin haberi, merfû.", punct=punct)
FASAAJIDU = lambda: tok("فَسَأَجِدُ", "wajada", "verb", ["al-fa-fi-jawab-al-shart", "al-majzum-wal-shart-wal-jaza", "mudari-marfu", "mithal-verbs", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَالسِّينُ حَرْفُ اسْتِقْبَالٍ، وَأَجِدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
    "The fa ties the answer of the condition; the sin marks the future; «I will find» is a present verb in raf' with «I» hidden of necessity; the clause is the answer, in the seat of jazm.", "Fâ şartın cevabını bağlar; sîn istikbâl içindir; «bulacağım» merfû muzâri, fâil «ben» vücûben müstetir; cümle şartın cevabı olarak mahallen meczûm.",
    segments=[seg("فَ", "fa", "conj"), seg("سَ", "sa", "part"), seg("أَجِدُ", "wajada", "verb")])
ATAKFURU = lambda: tok("أَتَكْفُرُ", "kafara", "verb", ["al-istifham", "mudari-marfu", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتَكْفُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "The hamza asks a question that rebukes («do you disbelieve?»); the present verb is in raf' with «you» hidden of necessity.", "İnkârî istifhâm hemzesi; merfû muzâri, fâil «sen» vücûben müstetir.",
    segments=[seg("أَ", "hamza-istifham", "part"), seg("تَكْفُرُ", "kafara", "verb")])
ALLADHI_NAAT_J = lambda: tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa", "mahall-al-majrur"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِرَبِّكَ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.", "A relative pronoun built on sukun in the seat of jarr as the adjective of «your Lord»; the clause after it is its clause.", "İsm-i mevsûl, sükûn üzere mebnî, «Rabbin»in na'tı olarak mahallen mecrûr; sonraki cümle sılasıdır.")
HINA = lambda: tok("حِينَ", "hina", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when» — an adverb of time in nasb, annexed to the clause that follows.", "«-dığı zaman» — mansûb zaman zarfı, sonraki cümleye muzâf.")
TASHKURI = lambda: tok("تَشْكُرِ", "shakara", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "Present verb in jazm after لَمْ, its sign the sukun — voweled with kasra before the following ال; the doer «you» is hidden of necessity.", "Lem ile meczûm muzâri, alâmeti sükûn — iki sâkin karşılaştığı için kesre ile harekelendi; fâil «sen» vücûben müstetir.")
TAQUL = lambda punct=None: tok("تَقُلْ", "qala", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "hollow-verbs", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ تَقُولْ)، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ" + MAQUL[0] + ".",
    "Present verb in jazm after لَمْ; the hollow middle letter drops (تَقُولْ → تَقُلْ); the doer «you» is hidden of necessity" + MAQUL[1] + ".", "Lem ile meczûm muzâri; ecvef fiilin aynı düşer (tekûl → tekul); fâil «sen» vücûben müstetir" + MAQUL[2] + ".", punct=punct)
ATANI = lambda punct=None: tok("أَعْطَانِي", "aata", "verb", ["naqis-verbs", "form-iv-verbs", "ya-al-mutakallim", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + SILA[0] + ".",
    "«He gave me» — a past naqis verb built on a fatha estimated on the alif; the doer «He» is hidden; the nun guards the verb and the speaker's ya is its object" + SILA[1] + ".", "«bana verdi» — elif üzerinde takdîrî fetha ile mebnî nâkıs mâzî; fâil gizli «O»; nûn vikâye, mütekellim yâ'sı mef'ûlün bih" + SILA[2] + ".",
    punct=punct, segments=[seg("أَعْطَا", "aata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
YUTIYANI = lambda: tok("يُعْطِيَنِي", "aata", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs", "form-iv-verbs", "mafulayn", "ya-al-mutakallim", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
    "«that He give me» — a present verb in nasb by أَنْ, its fatha SHOWING on the ya; the doer «He» is hidden; the nun guards the verb and the speaker's ya is the FIRST object.", "«bana vermesi» — en ile mansûb muzâri, fethası yâ üzerinde zâhir; fâil gizli «O»; nûn vikâye, mütekellim yâ'sı birinci mef'ûl.",
    segments=[seg("يُعْطِيَ", "aata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
WA_AN = lambda: tok("وَأَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari", "atf-nasaq"], WA_AR + "أَنْ حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ، وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْأَوَّلِ.", "The waw conjoins a second أَنْ-clause to the first.", "Vâv atıf; ikinci en-cümlesi birinciye atfedilir.", segments=[seg("وَ", "wa", "conj"), seg("أَنْ", "an-masdariyya", "part")])
LAKINNA = lambda: tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"], WA_AR + "لٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "The waw conjoins; لٰكِنَّ «but» is the sister of إِنَّ that corrects what went before: its noun in nasb, its predicate in raf'.", "Vâv atıf; lâkinne — inne'nin kardeşlerinden istidrâk harfi: ismini nasb, haberini ref eder.",
    segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")])
ISM_LAKINNA_ALLAH = lambda: tok("اللهَ", "allah", "propn", ["inna-wa-akhawatuha"], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + LAFZ[0] + ".", "The noun of لٰكِنَّ, in nasb" + LAFZ[1] + ".", "Lâkinne'nin ismi, mansûb" + LAFZ[2] + ".")
KH_LAKINNA = lambda full, lex, extra=None: tok(full, lex, "noun", ["inna-wa-akhawatuha"] + (extra or []), "خَبَرُ لٰكِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of لٰكِنَّ, in raf'.", "Lâkinne'nin haberi, merfû.")
LAYTANI = lambda: tok("لَيْتَنِي", "layta", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya", "ya-al-mutakallim", "al-bariz-al-muttasil"],
    "لَيْتَ حَرْفُ تَمَنٍّ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "لَيْتَ «would that» is the sister of إِنَّ that wishes; the nun guards it and the speaker's ya is its noun, in the seat of nasb.", "Leyte — inne'nin kardeşlerinden temennî harfi; nûn vikâye, mütekellim yâ'sı ismi, mahallen mansûb.",
    segments=[seg("لَيْتَ", "layta", "part"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
WA_QAD_HAL = lambda: tok("وَقَدْ", "qad", "part", ["al-hal-jumla-wa-rabituha", "qad-harf"], "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ حَالٌ.", "The waw opens a hal clause and قَدْ affirms the past verb — «[finding them] already turned…».", "Hâl vâvı; kad tahkîk harfi — sonraki cümle hâl olarak mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")])
LAYSA_NAAT = lambda: tok("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مِنْ أَخَوَاتِ كَانَ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِأَرْضٍ.", "لَيْسَ «there is not» — the frozen sister of كَانَ; the clause is a second adjective of «earth».", "Leyse — kâne'nin câmid kardeşi; cümle «toprak»ın ikinci na'tı.")
JANNATAYHI = lambda: tok("جَنَّتَيْهِ", "janna", "noun", ["maful-bihi", "idafa-definiteness", "al-bariz-al-muttasil"],
    "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَكُسِرَتْ لِمُنَاسَبَةِ الْيَاءِ.",
    "«his two gardens» — the object, in nasb by the YA as a dual, its nun dropped for the annexation; the attached «his» is the second term, its damma turned to kasra after the ya.", "«iki bahçesini» — mef'ûlün bih, tesniye olduğu için yâ ile mansûb, nûnu izâfet için düşmüş; bitişik «onun» muzâfun ileyh, yâ'dan sonra kesre ile.",
    segments=[seg("جَنَّتَيْ", "janna", "noun"), seg("هِ", "pron-3ms", "pron")])
MAN_MAWSUL_MI = lambda: tok("مَنْ", "man", "pron", ["ism-mawsul", "idafa-definiteness", "mahall-al-majrur"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.", "«whoever» — the relative noun built on sukun, the second term of the idafa in the seat of jarr; the clause after it is its clause.", "«kimse» — sükûn üzere mebnî ism-i mevsûl, muzâfun ileyh olarak mahallen mecrûr; sonraki cümle sılasıdır.")
LILLADHINA = lambda: tok("لِلَّذِينَ", "alladhina", "pron", ["huruf-jarr", "ism-mawsul", "mahall-al-majrur", "mubtada-khabar"],
    "اللَّامُ حَرْفُ جَرٍّ، وَالَّذِينَ اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.", "The lam is a jarr letter; «those who» is the plural relative built on fatha in the seat of jarr; the phrase is the predicate and the clause after it is the relative's clause.", "Lâm cer harfi; «o kimseler» — fetha üzere mebnî cemi ism-i mevsûl, mahallen mecrûr; câr-mecrûr haber, sonraki cümle sıla.",
    segments=[seg("لِ", "li", "prep"), seg("الَّذِينَ", "alladhina", "pron")])
FA_HADHIHI = lambda: tok("فَهٰذِهِ", "hadhihi", "pron", ["asma-al-ishara", "mubtada-khabar"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The fa opens the moral; «this» is a demonstrative built on kasra, the mubtada in the seat of raf'.", "Fâ isti'nâf içindir; «işte bu» kesre üzere mebnî işaret ismi, mübtedâ olarak mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("هٰذِهِ", "hadhihi", "pron")])
WAL_AQIBA = lambda: tok("وَالْعَاقِبَةُ", "aqiba", "noun", ["mubtada-khabar"], WA_AR + "الْعَاقِبَةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; «the outcome» is the mubtada, in raf'.", "Vâv atıf; «âkıbet» mübtedâ, merfû.", segments=[seg("وَ", "wa", "conj"), seg("الْعَاقِبَةُ", "aqiba", "noun")])
YANFAHU = lambda punct=None: tok("يَنْفَعْهُ", "nafaa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.", "Present verb in jazm after لَمْ; the attached «him» is its object and its doer follows.", "Lem ile meczûm muzâri; bitişik «ona» mef'ûlün bih, fâili sonra gelir.", punct=punct, segments=[seg("يَنْفَعْ", "nafaa", "verb"), seg("هُ", "pron-3ms", "pron")])
QAWMUHU_ATF = lambda punct=None: tok("قَوْمُهُ", "qawm", "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"], "مَعْطُوفٌ عَلَى الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "Conjoined to the doer, in raf' and annexed to «his».", "Fâile ma'tûf, merfû, «onun»a muzâf.", punct=punct, segments=[seg("قَوْمُ", "qawm", "noun"), seg("هُ", "pron-3ms", "pron")])
WA_QAWMI = lambda: tok("وَقَوْمِي", "qawm", "noun", ["mubtada-khabar", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"], WA_AR + "قَوْمُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The waw conjoins a second clause; «my people» is its mubtada, in raf' by a damma estimated before the speaker's ya.", "Vâv atıf; «kavmim» mübtedâ, mütekellim yâ'sından önce takdîrî damme ile merfû.", segments=[seg("وَ", "wa", "conj"), seg("قَوْمِ", "qawm", "noun"), seg("ي", "pron-1s", "pron")])
NASIYA = lambda: MADI("وَنَسِيَ", "nasiya", ["naqis-verbs"], hidden=True, note_ar=" — نَاقِصٌ يَائِيٌّ تَظْهَرُ فَتْحَتُهُ عَلَى الْيَاءِ" + SILA[0], note_en=" — a naqis verb in ya whose fatha shows" + SILA[1], note_tr=" — yâ'lı nâkıs fiil, fethası zâhir" + SILA[2])

TITLES = [{"ar": "الْجَنَّتَانِ", "en": "The two gardens", "tr": "İki bahçe"},
          {"ar": "الْفَخْرُ", "en": "The boast", "tr": "Övünme"},
          {"ar": "النَّصِيحَةُ", "en": "The counsel", "tr": "Nasihat"},
          {"ar": "الْهَلَاكُ", "en": "The ruin", "tr": "Helâk"}]

S1 = []
S1.append({"id": "s1", "translation": {"en": "In a town there were two men: one of them was rich and the other poor.", "tr": "Bir kasabada iki adam vardı: biri zengin, diğeri fakirdi."},
 "tokens": [KANA("كَانَ"), PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"), MAJR("قَرْيَةٍ", "qarya"), ISMK("رَجُلَانِ", "rajul", muakhkhar=True, sign=DUAL_RAF, punct=":"),
  ENC_NOUN("أَحَدُهُمَا", "ahad", "هُمَا", "mubtada"), KHABAR("غَنِيٌّ", "ghani"), ATF("وَالْآخَرُ", "akhar", "noun", "raf", note_ar=" — مُبْتَدَأٌ ثَانٍ مَعْطُوفٌ عَلَى الْأَوَّلِ", note_en=" — a second mubtada conjoined to the first", note_tr=" — birinciye atfedilen ikinci mübtedâ"), KHABAR("فَقِيرٌ", "faqir", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "The rich man had two gardens of grapes, with many palm trees around them, and between them sown fields and a river.", "tr": "Zenginin üzümden iki bahçesi vardı; çevrelerinde birçok hurma ağacı, aralarında ekin ve bir ırmak."},
 "tokens": [KANA("وَكَانَ"), LI_AL("لِلْغَنِيِّ", "ghani", "الْغَنِيِّ", note_ar=KH_MUQ[0], note_en=KH_MUQ[1], note_tr=KH_MUQ[2]), ISMK("جَنَّتَانِ", "janna", muakhkhar=True, sign=DUAL_RAF),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِاسْمِ كَانَ", "; the jarr phrase is the adjective of كَانَ's noun", "; câr-mecrûr kâne'nin isminin na'tı", gloss_tr="«-den»"), MAJR("عِنَبٍ", "inab", punct="،"),
  HAWLAHUMA(), MUBTADA("نَخَلَاتٌ", "nakhla", note_ar=" مُؤَخَّرٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ", note_en=" (placed after its predicate) — a sound feminine plural", note_tr=" (haberinden sonra) — cem-i müennes sâlim"), NAAT("كَثِيرَةٌ", "kathir", "raf", punct="،"),
  WA_BAYNAHUMA(), MUBTADA("زَرْعٌ", "zar", note_ar=" مُؤَخَّرٌ", note_en=" (placed after its predicate)", note_tr=" (haberinden sonra)"), ATF("وَنَهَرٌ", "nahr", "noun", "raf", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "The water ran between the two gardens, and so the two of them gave much fruit.", "tr": "Su iki bahçenin arasından akıyordu; böylece ikisi de bol meyve veriyordu."},
 "tokens": [KANA("وَكَانَ"), ISMK("الْمَاءُ", "ma-water"), MUDARI("يَجْرِي", "jara", ["naqis-verbs"], naqis="ي", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]), ZARF("بَيْنَ", "bayna"), MUDAF_ILAYH("الْجَنَّتَيْنِ", "janna", sign=DUAL_JN, punct="،"),
  KANATA(), TUTIYANI(), MAFUL("ثَمَرًا", "thamar"), NAAT("كَثِيرًا", "kathir", "nasb", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "The poor man was a believer who worshipped God and thanked Him; as for the rich man, he used to boast of his wealth.", "tr": "Fakir, Allah'a ibadet eden ve O'na şükreden bir mümindi; zengine gelince, malıyla övünürdü."},
 "tokens": [KANA("وَكَانَ"), ISMK("الْفَقِيرُ", "faqir"), KHK("مُؤْمِنًا", "mumin", extra=["ism-fail"]), MUDARI("يَعْبُدُ", "abada", note_ar=NAAT_CL_NASB[0] + " لِمُؤْمِنًا", note_en=NAAT_CL_NASB[1], note_tr=NAAT_CL_NASB[2]), ALLAH_MAF(), MUDARI("وَيَشْكُرُهُ", "shakara", enc="هُ", punct="،"),
  AMMA("وَأَمَّا"), MUBTADA("الْغَنِيُّ", "ghani"), FA_KANA_AMMA(), MUDARI("يَفْخَرُ", "fakhara", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]), BI_NOUN("بِمَالِهِ", "mal", "مَالِهِ", enc="هِ", punct=".")]})

S2 = []
S2.append({"id": "s1", "translation": {"en": "The rich man entered his garden with his poor companion and said to him: «My wealth is more than your wealth, and my people are stronger than your people.»", "tr": "Zengin, fakir arkadaşıyla bahçesine girdi ve ona dedi: «Malım senin malından çok, kavmim senin kavminden güçlü.»"},
 "tokens": [MADI("وَدَخَلَ", "dakhala"), FAIL("الْغَنِيُّ", "ghani"), ENC_NOUN("جَنَّتَهُ", "janna", "هُ", "maful"), MAA(), ENC_NOUN("صَاحِبِهِ", "sahib", "هِ", "mudaf"), NAAT("الْفَقِيرِ", "faqir", "jarr", punct="،"), QALA("وَقَالَ", hidden=True), LAHU("لَهُ", "pron-3ms", " («ona»)", punct=":"),
  YA_MUTAKALLIM_N("مَالِي", "mal", "مَال", "مُبْتَدَأٌ مَرْفُوعٌ", "The mubtada, in raf'", "Mübtedâ, merfû"), KHABAR("أَكْثَرُ", "akthar", ["ism-tafdil", "mamnu-min-sarf"], note_ar=" — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=" — an elative, barred from tanwin", note_tr=" — gayr-i munsarif ism-i tafdîl"), MIN(), ENC_NOUN("مَالِكَ", "mal", "كَ", "majr", punct="،"),
  WA_QAWMI(), KHABAR("أَقْوَى", "aqwa", ["ism-tafdil", "ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — اسْمُ تَفْضِيلٍ مَقْصُورٌ", note_en=" — an elative ending in alif", note_tr=" — maksûr ism-i tafdîl"), MIN(), ENC_NOUN("قَوْمِكَ", "qawm", "كَ", "majr", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "Then he looked at his garden and said: «This garden will never perish, and my wealth will never go.»", "tr": "Sonra bahçesine baktı ve dedi: «Bu bahçe asla yok olmayacak, malım da asla gitmeyecek.»"},
 "tokens": [THUMMA(), MADI("نَظَرَ", "nazara", hidden=True), ILA(), ENC_NOUN("جَنَّتِهِ", "janna", "هِ", "majr"), QALA("وَقَالَ", hidden=True, punct=":"), LAN(), MANSUB_AN("تَهْلِكَ", "halaka", by="لَنْ", hidden=False),
  ISHARA("هٰذِهِ", "hadhihi", "رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"), BADAL("الْجَنَّةُ", "janna", "raf", note_ar=" — بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", note_en=" — the substitute of the demonstrative", note_tr=" — işaret isminden bedel"), ABADAN(punct="،"),
  LAN("وَلَنْ"), MANSUB_AN("يَذْهَبَ", "dhahaba", by="لَنْ", hidden=False), YA_MUTAKALLIM_N("مَالِي", "mal", "مَال", "فَاعِلٌ مَرْفُوعٌ", "The doer, in raf'", "Fâil, merfû", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "«And I do not think the Day of Rising is near; and if I return to my Lord, I will find with Him something better than this garden.»", "tr": "«Kıyamet gününün yakın olduğunu da sanmıyorum; Rabbime dönsem bile O'nun katında bu bahçeden daha hayırlısını bulurum.»"},
 "tokens": [WA_LA_NAFIYA(), MUDARI("أَظُنُّ", "zanna", ["mafulayn"], who="أَنَا", wujub=True), ANNA((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ ظَنَّ", "; the clause it builds stands for both objects of «I think»", "; kurduğu müevvel masdar zanne'nin iki mef'ûlünün yerini tutar")),
  ISM_ANNA("يَوْمَ", "yawm", note=MUDAF_NOTE), MUDAF_ILAYH("الْقِيَامَةِ", "qiyama"), KH_ANNA_N("قَرِيبٌ", "qarib", ["sifa-mushabbaha"], punct="،"),
  IN_SHART("وَإِنْ"), MADI_T("رَجَعْتُ", "rajaa", who="ana", shart=True), ILA(), YA_MUTAKALLIM_N("رَبِّي", "rabb", "رَبّ", "مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr"), FASAAJIDU(), INDAHU(),
  MAFUL("خَيْرًا", "khayr", extra=["ism-tafdil"], note_ar=" — اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ", note_en=" — an elative whose hamza is dropped", note_tr=" — hemzesi düşmüş ism-i tafdîl"), MIN(),
  ISHARA("هٰذِهِ", "hadhihi", "جَرٍّ", "jarr after the letter", "mecrûr", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"), BADAL("الْجَنَّةِ", "janna", "jarr", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "His companion said to him: «Do you deny your Lord who created you and gave you this wealth?»", "tr": "Arkadaşı ona dedi: «Seni yaratan ve sana bu malı veren Rabbini inkâr mı ediyorsun?»"},
 "tokens": [QALA_F("فَقَالَ"), LAHU("لَهُ", "pron-3ms", " («ona»)"), ENC_NOUN("صَاحِبُهُ", "sahib", "هُ", "fail", punct=":"), ATAKFURU(), BI_NOUN("بِرَبِّكَ", "rabb", "رَبِّكَ", enc="كَ"), ALLADHI_NAAT_J(),
  ENC_MADI("خَلَقَكَ", "khalaqa", "كَ", hidden=True, note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]), ENC_MADI("وَرَزَقَكَ", "razaqa", "كَ", ["mafulayn"], hidden=True, note_ar=" أَوَّلُ", note_en=" — the first of two", note_tr=" — iki mef'ûlün birincisi"),
  ISHARA("هٰذَا", "hadha", "نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ", "nasb as the second object", "mansûb — ikinci mef'ûl", extra=["mafulayn"]), BADAL("الْمَالَ", "mal", "nasb", punct="؟")]})
S2.append({"id": "s5", "translation": {"en": "«As for me, I worship God alone and thank Him for everything.»", "tr": "«Bana gelince, yalnız Allah'a ibadet eder ve her şey için O'na şükrederim.»"},
 "tokens": [AMMA(), ANA(), FA_JAWAB_AMMA_MUDARI("فَأَعْبُدُ", "abada"), ALLAH_MAF(), WAHDAHU(punct="،"), MUDARI("وَأَشْكُرُهُ", "shakara", who="أَنَا", enc="هُ", wujub=True), ALA(), MAJR("كُلِّ", "kull", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("شَيْءٍ", "shay", punct=".")]})

S3 = []
S3.append({"id": "s1", "translation": {"en": "And he said to him: «Why did you not thank God when you entered your garden, and did not say: the wealth is God's wealth, and He is the one who gave me?»", "tr": "Ve ona dedi: «Bahçene girdiğinde neden Allah'a şükretmedin ve: 'Mal Allah'ın malıdır, bana veren O'dur' demedin?»"},
 "tokens": [QALA("وَقَالَ", hidden=True), LAHU("لَهُ", "pron-3ms", " («ona»)", punct=":"), LIMADHA(), LAM_JAZM(), TASHKURI(), ALLAH_MAF(), HINA(), MADI_T("دَخَلْتَ", "dakhala", who="anta", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the clause is the second term of the idafa, in the seat of jarr", note_tr="; cümle muzâfun ileyh olarak mahallen mecrûr"), ENC_NOUN("جَنَّتَكَ", "janna", "كَ", "maful", punct="،"),
  LAM_JAZM("وَلَمْ"), TAQUL(punct=":"), MUBTADA("الْمَالُ", "mal"), KHABAR("مَالُ", "mal", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), ALLAH_MI(punct="،"), WA_HUWA_ATF(), ALLADHI(), ATANI(punct="؟")]})
S3.append({"id": "s2", "translation": {"en": "«I am poor today, but God is able to give me something better than your garden, and to destroy your garden in a single night.»", "tr": "«Bugün fakirim; ama Allah bana senin bahçenden hayırlısını vermeye de, bahçeni bir gecede yok etmeye de kâdirdir.»"},
 "tokens": [ANA(), KHABAR("فَقِيرٌ", "faqir"), ZARF("الْيَوْمَ", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False, punct="،"), LAKINNA(), ISM_LAKINNA_ALLAH(), KH_LAKINNA("قَادِرٌ", "qadir", ["ism-fail"]), ALA(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِعَلَى", "; the clause it builds is in jarr after عَلَى", "; kurduğu müevvel masdar alâ ile mecrûr"), YUTIYANI(), MAFUL("خَيْرًا", "khayr", extra=["mafulayn", "ism-tafdil"], note_ar=" ثَانٍ", note_en=" — the second of two", note_tr=" — iki mef'ûlün ikincisi"), MIN(), ENC_NOUN("جَنَّتِكَ", "janna", "كَ", "majr", punct="،"),
  WA_AN(), MANSUB_AN("يُهْلِكَ", "ahlaka", ["form-iv-verbs"]), ENC_NOUN("جَنَّتَكَ", "janna", "كَ", "maful"), FI(), MAJR("لَيْلَةٍ", "layla"), NAAT("وَاحِدَةٍ", "wahid", "jarr", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "But the rich man did not listen to his companion's counsel, and went off laughing.", "tr": "Zengin, arkadaşının nasihatini dinlemedi ve gülerek gitti."},
 "tokens": [LAM_JAZM("فَلَمْ"), JAZM_V("يَسْمَعِ", "samia", note_ar="، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — voweled with kasra before the following ال", note_tr=" — iki sâkin karşılaştığı için kesre ile harekelendi"), FAIL("الْغَنِيُّ", "ghani"), MAFUL("نَصِيحَةَ", "nasiha", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), ENC_NOUN("صَاحِبِهِ", "sahib", "هِ", "mudaf", punct="،"),
  MADI("وَذَهَبَ", "dhahaba", hidden=True), WA_HUWA_HAL(), MUDARI("يَضْحَكُ", "dahika", note_ar=KH_CL[0] + HAL_FULL[0], note_en=KH_CL[1] + HAL_FULL[1], note_tr=KH_CL[2] + HAL_FULL[2], punct=".")]})

S4 = []
S4.append({"id": "s1", "translation": {"en": "Then in the night God sent fire from the sky upon the two gardens, and it destroyed everything in them.", "tr": "Gece Allah gökten iki bahçenin üzerine bir ateş gönderdi; içlerindeki her şeyi yok etti."},
 "tokens": [MADI("فَأَرْسَلَ", "arsala", ["form-iv-verbs"]), ALLAH_F(), FI(), MAJR("اللَّيْلِ", "layl"), MAFUL("نَارًا", "nar"), MINA(), MAJR("السَّمَاءِ", "sama"), ALA(), MAJR("الْجَنَّتَيْنِ", "janna", sign=DUAL_JN, punct="،"),
  MADI("فَأَهْلَكَتْ", "ahlaka", ["form-iv-verbs"], fem=True, hidden=True), MAFUL("كُلَّ", "kull", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("شَيْءٍ", "shay"), JARR_PRON("فِيهِمَا", "fi", "فِي", "هِمَا", " («ikisinde»)", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "In the morning the rich man saw his two gardens turned into dry earth, with no fruit in it and no water.", "tr": "Sabah olunca zengin, iki bahçesini kurumuş bir toprağa dönmüş buldu: ne meyve kalmıştı ne su."},
 "tokens": [tok("فَأَصْبَحَ", "asbaha", "verb", ["form-iv-verbs"], FA_AR + "أَصْبَحَ هُنَا فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى دَخَلَ فِي الصَّبَاحِ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "The fa conjoins; here أَصْبَحَ is a FULL verb, «he entered the morning», built on fatha — not the sister of كَانَ.", "Fâ atıf; burada asbaha tam fiildir, «sabaha girdi» — kâne'nin kardeşi değil.", segments=[seg("فَ", "fa", "conj"), seg("أَصْبَحَ", "asbaha", "verb")]),
  FAIL("الْغَنِيُّ", "ghani"), MADI_ALIF("فَرَأَى", "raa", hidden=True), JANNATAYHI(), WA_QAD_HAL(), SARATA(), KHK("أَرْضًا", "ard", note_ar=" — أَيْ خَبَرُ صَارَ", note_en=" — that is, of صَارَ", note_tr=" — yani sâra'nın haberi"), NAAT("يَابِسَةً", "yabis", "nasb", ["ism-fail"], punct="،"),
  LAYSA_NAAT(), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ مُقَدَّمٌ", note_en="; the jarr phrase is the FRONTED predicate of لَيْسَ", note_tr="; câr-mecrûr leyse'nin öne alınmış haberi"), ISMK("ثَمَرٌ", "thamar", muakhkhar=True, note_ar=" — اسْمُ لَيْسَ", note_en=" — that is, of لَيْسَ", note_tr=" — yani leyse'nin ismi"), WA_LA_NAFIYA(), ATF("مَاءٌ", "ma-water", "noun", "raf", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "He regretted bitterly and said: «Would that I had thanked my Lord and not boasted of my wealth!»", "tr": "Derin bir pişmanlık duydu ve dedi: «Keşke Rabbime şükretseydim de malımla övünmeseydim!»"},
 "tokens": [MADI("فَنَدِمَ", "nadima", hidden=True), tok("نَدَمًا", "nadam", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ فِعْلِهِ.", "The absolute object, in nasb — the verb's own masdar.", "Mef'ûl-i mutlak, mansûb — fiilin kendi masdarı."), NAAT("شَدِيدًا", "shadid", "nasb", punct="،"),
  QALA("وَقَالَ", hidden=True, punct=":"), LAYTANI(), MADI_T("شَكَرْتُ", "shakara", who="ana", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَيْتَ", note_en="; the clause fills the seat of raf' as the predicate of لَيْتَ", note_tr="; cümle leyte'nin haberi olarak mahallen merfû"),
  YA_MUTAKALLIM_N("رَبِّي", "rabb", "رَبّ", "مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb"), LAM_JAZM("وَلَمْ"), JAZM_V("أَفْخَرْ", "fakhara", hidden="أَنَا"), BI_NOUN("بِمَالِي", "mal", "مَالِي", enc="ي", punct="!")]})
S4.append({"id": "s4", "translation": {"en": "He found no one to help him, and neither his wealth nor his people availed him.", "tr": "Ona yardım edecek kimse bulamadı; ne malı ne kavmi ona fayda verdi."},
 "tokens": [LAM_JAZM("وَلَمْ"), JAZM_V("يَجِدْ", "wajada", ["mithal-verbs"], hidden="هُوَ"), MAFUL("أَحَدًا", "ahad"), MUDARI("يَنْصُرُهُ", "nasara", enc="هُ", note_ar=NAAT_CL_NASB[0] + " لِأَحَدًا", note_en=NAAT_CL_NASB[1], note_tr=NAAT_CL_NASB[2], punct="،"),
  LAM_JAZM("وَلَمْ"), YANFAHU(), ENC_NOUN("مَالُهُ", "mal", "هُ", "fail"), WA_LA_NAFIYA(), QAWMUHU_ATF(punct=".")]})
S4.append({"id": "s5", "translation": {"en": "Such is the end of whoever boasts of his wealth and forgets his Lord; and the good end belongs to those who give thanks.", "tr": "İşte malıyla övünüp Rabbini unutanın sonu budur; güzel âkıbet ise şükredenlerindir."},
 "tokens": [FA_HADHIHI(), KHABAR("عَاقِبَةُ", "aqiba", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MAN_MAWSUL_MI(), MADI("فَخَرَ", "fakhara", hidden=True, note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]), BI_NOUN("بِمَالِهِ", "mal", "مَالِهِ", enc="هِ"), NASIYA(), ENC_NOUN("رَبَّهُ", "rabb", "هُ", "maful", punct="،"),
  WAL_AQIBA(), NAAT("الْحَسَنَةُ", "hasan-adj", "raf"), LILLADHINA(), MUDARI5("يَشْكُرُونَ", "shakara", note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2], punct=".")]})

CHAPS = [S1, S2, S3, S4]
PREF = ["qisas-al-nabiyyin-4", "al-kafiya", "al-amana-wa-al-khashaba", "ashab-al-ghar", "tawbat-al-qatil", "al-abras-wa-al-aqra-wa-al-ama", "luqman-wa-ibnuh", "adam-wa-iblis", "hud-wa-aad", "ayyub-wa-al-sabr", "qarun-wa-kunuzuh",
        "dhu-al-qarnayn-wa-al-sadd", "wasiyyat-abi-yusuf-l5", "izhar-al-asrar", "al-asad-wa-al-arnab", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
PREF = [p for p in PREF if _pkg_dir(p).joinpath("glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
FORCE = {"sa": "adam-wa-iblis"}
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF if (_pkg_dir(p) / "morphology.json").exists()}
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    for p in PREF:
        if k in _M.get(p, {}): return _M[p][k]
    return None
NEW_GLOSS = {"inab": {"lemma": "عِنَب", "root": "ع ن ب", "pos": "noun", "gloss": {"en": "grapes (a collective; the unit noun is عِنَبَة)", "tr": "üzüm (cins ismi; tekili عِنَبَة)"}, "level": 3}}
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
LEVEL_NAME = json.loads((ROOT / "content/samples/qisas-al-nabiyyin-4/manifest.json").read_text(encoding="utf-8")).get("levelName", "Intermediate")
MANIFEST = {
 "id": "sahib-al-jannatayn", "storyGroup": "sahib-al-jannatayn",
 "title": {"ar": "صَاحِبُ الْجَنَّتَيْنِ", "en": "The Man with Two Gardens", "tr": "İki Bahçe Sahibi"},
 "subtitle": {"ar": "غَنِيٌّ فَخَرَ بِجَنَّتَيْهِ عَلَى صَاحِبِهِ الْفَقِيرِ وَنَسِيَ رَبَّهُ، فَهَلَكَتَا فِي لَيْلَةٍ — قِصَّةٌ لِلْمُسْتَوَى الثَّالِثِ",
              "en": "A rich man boasts of his two gardens to his poor companion and forgets his Lord; both perish in a night — a story for the third level",
              "tr": "İki bahçesiyle fakir arkadaşına karşı övünen ve Rabbini unutan zengin; iki bahçe bir gecede yok olur — üçüncü seviye için bir hikâye"},
 "level": 3, "levelName": LEVEL_NAME, "version": "0.1.0", "published": "2026-11-09", "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّالِثُ) لِمَثَلِ صَاحِبِ الْجَنَّتَيْنِ الَّذِي ضَرَبَهُ الْقُرْآنُ فِي سُورَةِ الْكَهْفِ، بِأُسْلُوبِ كِتَابِ الْقِرَاءَةِ الْمُتَدَرِّجِ وَبِغَيْرِ أَلْفَاظِ الْآيَاتِ. لَيْسَ فِيهَا نَصُّ آيَةٍ، وَلَا يَصِحُّ أَنْ تُنْسَبَ جُمْلَةٌ مِنْهَا إِلَى الْقُرْآنِ.",
  "en": "ORIGINAL Level-3 graded Arabic: the parable of the man with two gardens from Surat al-Kahf, RETOLD FREELY in the wording of a graded reader and deliberately NOT in the Qur'an's own words. No verse is quoted and no sentence may be cited as Qur'anic text.",
  "tr": "ÖZGÜN 3. seviye kolaylaştırılmış Arapça: Kehf sûresindeki iki bahçe sahibi meseli, kolaylaştırılmış okuyucu üslûbuyla ve bilerek âyet lafızları KULLANILMADAN serbestçe yeniden anlatılmıştır. Hiçbir âyet aktarılmamıştır; hiçbir cümle Kur'an metni diye nakledilemez.",
  "reviewStatus": "pending-scholarly-review"},
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
