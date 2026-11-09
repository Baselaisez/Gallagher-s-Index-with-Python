"""Author content/samples/al-rahma-bil-hayawan — «الرَّحْمَةُ بِالْحَيَوَانِ», the twenty-seventh ORIGINAL story, the fifteenth at Level 2 (wave 125).

ORIGINAL graded Arabic: two ḥadīth narratives on mercy to animals RETOLD FREELY — the thirsty traveller who climbs back down a
well to water a dog from his leather sock and is forgiven, and the woman who shuts a cat in until it starves and is punished.
No sentence is the text of a ḥadīth (the ḥadīths' own clauses were paraphrased), no āya is quoted, and none may be cited as such.
Four chapters, sixteen sentences. Two entries are new — the nouns هِرَّة and عَطَش. Regenerate with:
python3 tools/authoring/author_rahma.py
"""
import json, os, pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "al-rahma-bil-hayawan"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *
from story_kit import _pre
import sarf_gen as _sg

PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "هُمْ": "هُمْ", "هِمْ": "هِمْ"})
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_F = lambda full="فَقَالَ", punct=None, hidden=False: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, punct=punct, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
LAFZ = (" — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl")
MUDAF_NOTE = ("، مُضَافٌ", ", annexed", ", muzâf")
KH_KANA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
NAAT_CL_RAF = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ", "; the clause fills the seat of raf' as the adjective of the indefinite noun before it", "; cümle, önceki nekre ismin na'tı olarak mahallen merfû")
NAAT_CL_NASB = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ", "; the clause fills the seat of nasb as the adjective of the indefinite noun before it", "; cümle, önceki nekre ismin na'tı olarak mahallen mansûb")
JAWAB_SHART = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "; the clause fills the seat of jazm as the answer of the condition", "; cümle şartın cevabı olarak mahallen meczûm")

FA_IDHA_FUJA = lambda: tok("فَإِذَا", "idha", "part", ["huruf-al-shart-fil-kafiya", "al-kinayat-wal-zuruf-al-mabniyya"],
    FA_AR + "إِذَا لِلْمُفَاجَأَةِ، حَرْفٌ عِنْدَ قَوْمٍ وَظَرْفُ مَكَانٍ عِنْدَ آخَرِينَ، وَلَا تَدْخُلُ إِلَّا عَلَى الْجُمْلَةِ الِاسْمِيَّةِ.",
    "The fa conjoins; this إِذَا is the إِذَا OF SURPRISE («and there was…»): a particle for some, an adverb of place for others, and it opens only a nominal clause.", "Fâ atıf; bu izâ, müfâcee izâ'sıdır («bir de ne görsün»): kimine göre harf, kimine göre mekân zarfı; yalnız isim cümlesine girer.",
    segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")])
ATSHANU_KH = lambda: tok("عَطْشَانُ", "atshan", "noun", ["mubtada-khabar", "mamnu-min-sarf", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — صِفَةٌ عَلَى فَعْلَانَ مَمْنُوعَةٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ.", "«thirsty» — the predicate, in raf'; an adjective on فَعْلَان, barred from tanwin by its added alif and nun.", "«susamış» — haber, merfû; fa'lân vezninde sıfat, elif-nûn ziyadesiyle gayr-i munsarif.")
MITHLI = lambda punct=None: YA_MUTAKALLIM_N("مِثْلِي", "mithl", "مِثْل", "نَعْتٌ (أَوْ حَالٌ) مَرْفُوعٌ", "An adjective of the predicate (or a hal), in raf'", "Haberin na'tı (ya da hâl), merfû", punct=punct)
MAAN_TAMYIZ = lambda punct=None: tok("مَاءً", "ma-water", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ مَا مُلِئَ بِهِ الْخُفُّ.", "A tamyiz in nasb — it names what the sock was filled with.", "Temyiz, mansûb — mestin ne ile dolduğunu belirtir.", punct=punct)
MARRATAN_THANIYA = lambda: [tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ الْعَدَدَ.", "An absolute object in nasb — it counts the action («a second time»).", "Mef'ûl-i mutlak, mansûb — sayıyı bildirir («ikinci kez»)."),
                              NAAT("ثَانِيَةً", "thani", "nasb", ["asma-al-adad-fil-kafiya"], punct="،")]
TUTIMHA = lambda: tok("تُطْعِمْهَا", "atama", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "Present verb in jazm after لَمْ; the doer «she» is hidden and the attached «it» is its object.", "Lem ile meczûm muzâri; fâil gizli «o», bitişik «onu» mef'ûlün bih.",
    segments=[seg("تُطْعِمْ", "atama", "verb"), seg("هَا", "pron-3fs", "pron")])
TASQIHA = lambda punct=None: tok("تَسْقِهَا", "saqa-water", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "Present verb in jazm after لَمْ — its sign the DROPPED weak letter (تَسْقِي → تَسْقِ); the doer «she» is hidden and «it» is the object.", "Lem ile meczûm muzâri — alâmeti illet harfinin (yâ) hazfi (teskî → teski); fâil gizli «o», bitişik «onu» mef'ûlün bih.",
    punct=punct, segments=[seg("تَسْقِ", "saqa-water", "verb"), seg("هَا", "pron-3fs", "pron")])
TATRUKHA = lambda: tok("تَتْرُكْهَا", "taraka", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "Present verb in jazm after لَمْ; the doer «she» is hidden and «it» is the object.", "Lem ile meczûm muzâri; fâil gizli «o», bitişik «onu» mef'ûlün bih.",
    segments=[seg("تَتْرُكْ", "taraka", "verb"), seg("هَا", "pron-3fs", "pron")])
LITATLUBA = lambda: tok("لِتَطْلُبَ", "talaba", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari"], "اللَّامُ لِلتَّعْلِيلِ، وَتَطْلُبَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.", "The lam of purpose; «that it might seek» is in nasb by a hidden أَنْ; the doer «it/she» is hidden.", "Ta'lîl lâmı; «araması için» gizli en ile mansûb; fâil gizli «o».", segments=[seg("لِ", "lam-taleel", "part"), seg("تَطْلُبَ", "talaba", "verb")])
BISABABI = lambda: tok("بِسَبَبِ", "sabab", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَسَبَبِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "The ba of cause; «because of» is in jarr after it and annexed.", "Sebebiyet bâ'sı; «sebebiyle» mecrûr, muzâf.", segments=[seg("بِ", "bi", "prep"), seg("سَبَبِ", "sabab", "noun")])
WALAW = lambda: tok("وَلَوْ", "law", "part", ["huruf-al-shart-fil-kafiya"], "الْوَاوُ حَالِيَّةٌ، وَلَوْ وَصْلِيَّةٌ لِلتَّعْمِيمِ — أَيْ: حَتَّى لَوْ كَانَ، وَجَوَابُهَا مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "The waw opens a hal and this لَوْ is the «even if» of generalisation; its answer is left unsaid, shown by what precedes.", "Hâl vâvı; bu lev, ta'mîm için «velev» — «olsa bile»; cevabı önceki cümlenin delâletiyle hazfedilmiştir.", segments=[seg("وَ", "wa", "conj"), seg("لَوْ", "law", "part")])
MAN_SHART = lambda full="فَمَنْ": tok(full, "man", "pron", ["al-majzum-wal-shart-wal-jaza", "mubtada-khabar", "al-mabni-wal-mudmar"], (FA_AR if full.startswith("فَ") else WA_AR) + "مَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُهُ.",
    ("The fa conjoins; " if full.startswith("فَ") else "The waw conjoins; ") + "«whoever» — the conditional noun built on sukun, the mubtada in the seat of raf'; the condition and its answer are its predicate.", ("Fâ atıf; " if full.startswith("فَ") else "Vâv atıf; ") + "«her kim» — sükûn üzere mebnî şart ismi, mübtedâ olarak mahallen merfû; şart ve cevap cümleleri haberi.",
    segments=[seg(full[:2], "fa" if full.startswith("فَ") else "wa", "conj"), seg("مَنْ", "man", "pron")])
SHART_V = lambda full, lex, extra=None: tok(full, lex, "verb", ["al-majzum-wal-shart-wal-jaza"] + (extra or []), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "A past verb built on fatha, in the seat of jazm as the verb of the condition; the doer «he» is hidden.", "Fetha üzere mebnî mâzî, şart fiili olarak mahallen meczûm; fâil gizli «o».")
RAHIMAHU_JAWAB = lambda: tok("رَحِمَهُ", "rahima", "verb", ["al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.", "A past verb in the seat of jazm as the answer of the condition; the attached «him» is its object and its doer follows.", "Şartın cevabı olarak mahallen meczûm mâzî; bitişik «ona» mef'ûlün bih, fâili sonra gelir.", segments=[seg("رَحِمَ", "rahima", "verb"), seg("هُ", "pron-3ms", "pron")])
YARHAMHU = lambda: tok("يَرْحَمْهُ", "rahima", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ" + JAWAB_SHART[0] + ".", "Present verb in jazm after لَمْ; «him» is its object and its doer follows" + JAWAB_SHART[1] + ".", "Lem ile meczûm muzâri; «ona» mef'ûlün bih, fâili sonra gelir" + JAWAB_SHART[2] + ".", segments=[seg("يَرْحَمْ", "rahima", "verb"), seg("هُ", "pron-3ms", "pron")])
GHUFIRA = lambda: tok("غُفِرَ", "ghafara", "verb", ["naib-al-fail", "al-majhul-fil-kafiya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ (لَهُ) — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِرَجُلٌ.", "«was forgiven» — a passive past; its deputy doer is the jarr phrase after it («for him»); the clause is the adjective of «a man».", "«bağışlandı» — meçhul mâzî; nâib-i fâili sonraki câr-mecrûrdur («ona»); cümle «adam»ın na'tı.")
UDHDHIBAT = lambda: tok("عُذِّبَتْ", "adhdhaba", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِامْرَأَةٌ.", "«was punished» — a passive past with the feminine ta; the deputy doer «she» is hidden; the clause is the adjective of «a woman».", "«cezalandırıldı» — te'nîs tâ'lı meçhul mâzî; nâib-i fâil gizli «o»; cümle «kadın»ın na'tı.")
HAKADHA = lambda: tok("هٰكَذَا", "hakadha", "pron", ["asma-al-ishara", "maful-mutlaq"], "الْهَاءُ لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ — وَالْمَجْمُوعُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ: تَعْلِيمًا هٰكَذَا.", "«thus»: the ha of alerting, the kaf of likeness and the demonstrative; together the adjective of a dropped masdar («taught [a teaching] like this»).", "«işte böyle»: tenbih hâ'sı, teşbih kâfı ve işaret ismi; birlikte hazfedilmiş bir masdarın na'tı.")
ANNA = lambda role=("", "", ""): tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".", "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".", "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
ISM_ANNA_MUAKHKHAR = lambda full, lex, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha", "inna-am-anna"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, placed after its predicate, in nasb.", "Enne'nin ismi, haberinden sonraya bırakılmış, mansûb.", punct=punct)

TITLES = [{"ar": "الرَّجُلُ وَالْكَلْبُ", "en": "The man and the dog", "tr": "Adam ve köpek"},
          {"ar": "الْخُفُّ وَالْمَاءُ", "en": "The sock and the water", "tr": "Mest ve su"},
          {"ar": "الْمَرْأَةُ وَالْهِرَّةُ", "en": "The woman and the cat", "tr": "Kadın ve kedi"},
          {"ar": "الْعَاقِبَةُ", "en": "The outcome", "tr": "Âkıbet"}]

S1 = []
S1.append({"id": "s1", "translation": {"en": "A man was walking along a long road on a hot day, and he grew very thirsty.", "tr": "Bir adam sıcak bir günde uzun bir yolda yürüyordu; çok susadı."},
 "tokens": [KANA("كَانَ"), ISMK("رَجُلٌ", "rajul"), MUDARI("يَمْشِي", "masha", ["naqis-verbs"], naqis="ي", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]), FI(), MAJR("طَرِيقٍ", "tariq"), NAAT("طَوِيلٍ", "tawil-long", "jarr", ["sifa-mushabbaha"]), FI(), MAJR("يَوْمٍ", "yawm"), NAAT("حَارٍّ", "harr-hot", "jarr", ["ism-fail"], punct="،"),
  MADI("فَعَطِشَ", "atisha", hidden=True), tok("عَطَشًا", "atash", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ فِعْلِهِ.", "The absolute object, in nasb — the verb's own masdar.", "Mef'ûl-i mutlak, mansûb — fiilin kendi masdarı."), NAAT("شَدِيدًا", "shadid", "nasb", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "He found a well, went down into it and drank, then came out.", "tr": "Bir kuyu buldu, içine indi ve su içti, sonra çıktı."},
 "tokens": [MADI("فَوَجَدَ", "wajada", ["mithal-verbs"], hidden=True), MAFUL("بِئْرًا", "bir", punct="،"), MADI("فَنَزَلَ", "nazala", hidden=True), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içine»)"), MADI("وَشَرِبَ", "shariba", hidden=True, punct="،"), THUMMA(), MADI("خَرَجَ", "kharaja", hidden=True, punct=".")]})
S1.append({"id": "s3", "translation": {"en": "And there was a dog by the well, licking the dust from thirst.", "tr": "Bir de ne görsün: kuyunun yanında susuzluktan toprağı yalayan bir köpek."},
 "tokens": [FA_IDHA_FUJA(), MUBTADA("كَلْبٌ", "kalb"), INDA(), MUDAF_ILAYH("الْبِئْرِ", "bir", note_ar=" — وَالظَّرْفُ خَبَرٌ", note_en="; the adverb phrase is the predicate", note_tr="; zarf haberdir"), MUDARI("يَأْكُلُ", "akala", note_ar=NAAT_CL_RAF[0] + " لِكَلْبٌ", note_en=NAAT_CL_RAF[1], note_tr=NAAT_CL_RAF[2]), MAFUL("التُّرَابَ", "turab"), MINA(), MAJR("الْعَطَشِ", "atash", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "The man said to himself: «This dog is thirsty like me.»", "tr": "Adam kendi kendine dedi: «Bu köpek de benim gibi susamış.»"},
 "tokens": [QALA_F("فَقَالَ"), FAIL("الرَّجُلُ", "rajul"), FI(), ENC_NOUN("نَفْسِهِ", "nafs", "هِ", "majr", punct=":"), ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ"), BADAL("الْكَلْبُ", "kalb", "raf"), ATSHANU_KH(), MITHLI(punct=".")]})

S2 = []
S2.append({"id": "s1", "translation": {"en": "So he went down the well a second time, filled his leather sock with water, then held it in his mouth and climbed up.", "tr": "Kuyuya ikinci kez indi, mestini suyla doldurdu, sonra onu ağzıyla tuttu ve yukarı çıktı."},
 "tokens": [MADI("فَنَزَلَ", "nazala", hidden=True), MAFUL("الْبِئْرَ", "bir", note_ar=" — نَزَلَ هُنَا مُتَعَدٍّ بِنَفْسِهِ", note_en=" — here «went down» takes its object directly", note_tr=" — burada nezele doğrudan mef'ûl alır")] + MARRATAN_THANIYA() +
  [MADI("وَمَلَأَ", "malaa", hidden=True), ENC_NOUN("خُفَّهُ", "khuff", "هُ", "maful"), MAAN_TAMYIZ(punct="،"), THUMMA(), ENC_MADI("أَمْسَكَهُ", "amsaka", "هُ", ["form-iv-verbs"], hidden=True), BI_NOUN("بِفَمِهِ", "fam", "فَمِهِ", enc="هِ"), MADI("وَصَعِدَ", "saada-climb", hidden=True, punct=".")]})
S2.append({"id": "s2", "translation": {"en": "He gave the dog to drink until it had drunk its fill; and God was pleased with him and forgave him his sins.", "tr": "Köpeği kanıncaya kadar suladı; Allah ondan razı oldu ve günahlarını bağışladı."},
 "tokens": [MADI_ALIF("فَسَقَى", "saqa-water", hidden=True), MAFUL("الْكَلْبَ", "kalb"), tok("حَتَّى", "hatta", "part", ["huruf-jarr"], "حَرْفُ غَايَةٍ وَابْتِدَاءٍ، وَالْجُمْلَةُ بَعْدَهُ لَا مَحَلَّ لَهَا.", "حَتَّى «until» before a past verb opens a new clause marking the end-point.", "Hattâ «-e kadar» — mâzî fiilden önce gâye bildiren ibtidâ harfi."), MADI("شَرِبَ", "shariba", hidden=True, punct="،"),
  MADI("فَرَضِيَ", "radiya", ["naqis-verbs"]), ALLAH_F(), JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)"), MADI("وَغَفَرَ", "ghafara", hidden=True), LAHU("لَهُ", "pron-3ms", " («ona»)"), ENC_NOUN("ذُنُوبَهُ", "dhanb", "هُ", "maful", extra=["jam-taksir"], punct=".")]})
S2.append({"id": "s3", "translation": {"en": "And the people learned that in mercy to every living creature there is a reward with God.", "tr": "İnsanlar öğrendi ki her canlıya merhamette Allah katında bir ecir vardır."},
 "tokens": [MADI("وَعَلِمَ", "alima", ["mafulayn"]), FAIL("النَّاسُ", "nas"), ANNA((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَلِمَ", "; the clause it builds stands for both objects of «they learned»", "; kurduğu müevvel masdar alime'nin iki mef'ûlünün yerini tutar")),
  PREP("فِي", "fi", " — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate of أَنَّ", "; câr-mecrûr enne'nin öne alınmış haberi", gloss_tr="«-de»"), MAJR("الرَّحْمَةِ", "rahma"), BI_NOUN("بِكُلِّ", "kull", "كُلِّ", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("حَيَوَانٍ", "hayawan"),
  ISM_ANNA_MUAKHKHAR("أَجْرًا", "ajr"), INDA(), ALLAH_MI(punct=".")]})

S3 = []
S3.append({"id": "s1", "translation": {"en": "In a town there was a woman who had a small cat.", "tr": "Bir kasabada küçük bir kedisi olan bir kadın vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True), PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"), MAJR("قَرْيَةٍ", "qarya"), ISMK("امْرَأَةٌ", "imraa", muakhkhar=True), LAHU("لَهَا", "pron-3fs", " («onun»)", grammar=["mubtada-khabar"]), MUBTADA("هِرَّةٌ", "hirra", note_ar=" مُؤَخَّرٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِامْرَأَةٌ", note_en=" (placed after its predicate) — the clause is the adjective of «a woman»", note_tr=" (haberinden sonra) — cümle «kadın»ın na'tı"), NAAT("صَغِيرَةٌ", "saghir", "raf", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "She shut it in the house, and neither fed it nor gave it water.", "tr": "Onu evde hapsetti; ne yedirdi ne de su verdi."},
 "tokens": [ENC_MADI("فَحَبَسَتْهَا", "habasa", "هَا", fem=True, hidden=True), FI(), MAJR("الْبَيْتِ", "bayt", punct="،"), LAM_JAZM("وَلَمْ"), TUTIMHA(), LAM_JAZM("وَلَمْ"), TASQIHA(punct=".")]})
S3.append({"id": "s3", "translation": {"en": "Nor did she let it go out to seek its food.", "tr": "Yiyeceğini araması için dışarı çıkmasına da izin vermedi."},
 "tokens": [LAM_JAZM("وَلَمْ"), TATRUKHA(), MUDARI("تَخْرُجُ", "kharaja", who="هِيَ", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ (أَوْ مَفْعُولٌ ثَانٍ لِتَرَكَ)", note_en="; the clause is a hal in the seat of nasb (or the second object of «let»)", note_tr="; cümle hâl olarak mahallen mansûb (ya da terake'nin ikinci mef'ûlü)"), LITATLUBA(), ENC_NOUN("طَعَامَهَا", "taam", "هَا", "maful", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "So the cat died of hunger.", "tr": "Kedi açlıktan öldü."},
 "tokens": [MADI("فَمَاتَتِ", "mata-die", ["hollow-verbs"], fem=True, kasra=True), FAIL("الْهِرَّةُ", "hirra"), MINA(), MAJR("الْجُوعِ", "ju", punct=".")]})

S4 = []
S4.append({"id": "s1", "translation": {"en": "God was angry with the woman, and her punishment was severe — because of a weak cat.", "tr": "Allah kadına gazap etti; zayıf bir kedi yüzünden cezası şiddetli oldu."},
 "tokens": [MADI("فَغَضِبَ", "ghadiba"), ALLAH_F(), ALA(), MAJR("الْمَرْأَةِ", "imraa", punct="،"), KANA("وَكَانَ"), ENC_NOUN("عِقَابُهَا", "iqab", "هَا", "ismk"), KHK("شَدِيدًا", "shadid"), BISABABI(), MUDAF_ILAYH("هِرَّةٍ", "hirra"), NAAT("ضَعِيفَةٍ", "daif", "jarr", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "Mercy to the weak is good, and wronging them is evil — even if it is a small animal.", "tr": "Zayıfa merhamet hayırdır, ona zulüm ise şerdir — küçük bir hayvan olsa bile."},
 "tokens": [tok("فَالرَّحْمَةُ", "rahma", "noun", ["mubtada-khabar"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَالرَّحْمَةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The fa opens the moral; «mercy» is the mubtada, in raf'.", "Fâ isti'nâf içindir; «merhamet» mübtedâ, merfû.", segments=[seg("فَ", "fa", "conj"), seg("الرَّحْمَةُ", "rahma", "noun")]),
  BI_NOUN("بِالضَّعِيفِ", "daif", "الضَّعِيفِ"), KHABAR("خَيْرٌ", "khayr", punct="،"), tok("وَالظُّلْمُ", "zulm", "noun", ["atf-nasaq", "mubtada-khabar"], WA_AR + "الظُّلْمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins a second clause; «wrong» is its mubtada, in raf'.", "Vâv atıf; «zulüm» ikinci cümlenin mübtedâsı, merfû.", segments=[seg("وَ", "wa", "conj"), seg("الظُّلْمُ", "zulm", "noun")]),
  LAHU("لَهُ", "pron-3ms", " («ona»)"), KHABAR("شَرٌّ", "sharr", punct="،"), WALAW(), KANA("كَانَ"), KHK("حَيَوَانًا", "hayawan", note_ar="، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", note_en="; the noun of كَانَ «it» is hidden", note_tr="; kâne'nin ismi gizli «o»"), NAAT("صَغِيرًا", "saghir", "nasb", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "Whoever shows mercy, God shows him mercy; and whoever does wrong, God does not show him mercy.", "tr": "Kim merhamet ederse Allah ona merhamet eder; kim zulmederse Allah ona merhamet etmez."},
 "tokens": [MAN_SHART("فَمَنْ"), SHART_V("رَحِمَ", "rahima"), RAHIMAHU_JAWAB(), ALLAH_F(punct="،"), MAN_SHART("وَمَنْ"), SHART_V("ظَلَمَ", "zalama"), LAM_JAZM(), YARHAMHU(), ALLAH_F(punct=".")]})
S4.append({"id": "s4", "translation": {"en": "Thus the Prophet taught people mercy to animals: a man was forgiven because of a dog, and a woman was punished because of a cat.", "tr": "Peygamber insanlara hayvanlara merhameti işte böyle öğretti: bir adam bir köpek yüzünden bağışlandı, bir kadın bir kedi yüzünden cezalandırıldı."},
 "tokens": [HAKADHA(), MADI("عَلَّمَ", "allama", ["form-ii-verbs", "mafulayn"]), FAIL("النَّبِيُّ", "nabi"), MAFUL("النَّاسَ", "nas", note_ar=" أَوَّلُ", note_en=" — the first of two", note_tr=" — iki mef'ûlün birincisi"), MAFUL("الرَّحْمَةَ", "rahma", note_ar=" ثَانٍ", note_en=" — the second of two", note_tr=" — iki mef'ûlün ikincisi"), BI_NOUN("بِالْحَيَوَانِ", "hayawan", "الْحَيَوَانِ", punct=":"),
  MUBTADA("رَجُلٌ", "rajul", note_ar=" — وَسَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ وَصْفُهَا", note_en=" — an indefinite mubtada, allowed by the adjective clause after it", note_tr=" — nekre mübtedâ, sıfat cümlesi ile câiz"), GHUFIRA(), LAHU("لَهُ", "pron-3ms", " («ona»)"), BISABABI(), MUDAF_ILAYH("كَلْبٍ", "kalb", punct="،"),
  tok("وَامْرَأَةٌ", "imraa", "noun", ["atf-nasaq", "mubtada-khabar"], WA_AR + "امْرَأَةٌ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَصْفُهَا سَوَّغَ الِابْتِدَاءَ بِهَا.", "The waw conjoins; «a woman» is the mubtada of a second clause, in raf'.", "Vâv atıf; «bir kadın» ikinci cümlenin mübtedâsı, merfû.", segments=[seg("وَ", "wa", "conj"), seg("امْرَأَةٌ", "imraa", "noun")]), UDHDHIBAT(), BISABABI(), MUDAF_ILAYH("هِرَّةٍ", "hirra", punct=".")]})

CHAPS = [S1, S2, S3, S4]
PREF = ["qisas-al-nabiyyin-4", "al-kafiya", "al-amana-wa-al-khashaba", "ashab-al-ghar", "tawbat-al-qatil", "al-abras-wa-al-aqra-wa-al-ama", "luqman-wa-ibnuh", "adam-wa-iblis", "hud-wa-aad", "ayyub-wa-al-sabr",
        "dhu-al-qarnayn-wa-al-sadd", "wasiyyat-abi-yusuf-l5", "izhar-al-asrar", "al-asad-wa-al-arnab", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
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
 "hirra": {"lemma": "هِرَّة", "root": "ه ر ر", "pos": "noun", "plural": "هِرَر", "gloss": {"en": "a cat (feminine; the masculine is هِرّ)", "tr": "kedi (müennes; müzekkeri هِرّ)"}, "level": 2},
 "atash": {"lemma": "عَطَش", "root": "ع ط ش", "pos": "noun", "gloss": {"en": "thirst (the masdar of عَطِشَ)", "tr": "susuzluk (عَطِشَ fiilinin masdarı)"}, "level": 2},
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
LEVEL_NAME = json.loads((ROOT / "content/samples/luqman-wa-ibnuh/manifest.json").read_text(encoding="utf-8")).get("levelName", "Elementary")
MANIFEST = {
 "id": "al-rahma-bil-hayawan", "storyGroup": "al-rahma-bil-hayawan",
 "title": {"ar": "الرَّحْمَةُ بِالْحَيَوَانِ", "en": "Mercy to Animals", "tr": "Hayvanlara Merhamet"},
 "subtitle": {"ar": "رَجُلٌ سَقَى كَلْبًا فَغُفِرَ لَهُ، وَامْرَأَةٌ حَبَسَتْ هِرَّةً فَعُوقِبَتْ — قِصَّتَانِ لِلْمُسْتَوَى الثَّانِي",
              "en": "A man waters a dog and is forgiven; a woman shuts a cat in and is punished — two stories for the second level",
              "tr": "Bir köpeği sulayan adam bağışlanır; bir kediyi hapseden kadın cezalandırılır — ikinci seviye için iki hikâye"},
 "level": 2, "levelName": LEVEL_NAME, "version": "0.1.0", "published": "2026-11-09", "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّانِي) لِخَبَرَيْنِ مَرْوِيَّيْنِ فِي الصَّحِيحَيْنِ: الرَّجُلِ الَّذِي سَقَى الْكَلْبَ، وَالْمَرْأَةِ الَّتِي حَبَسَتِ الْهِرَّةَ، بِأُسْلُوبِ كِتَابِ الْقِرَاءَةِ الْمُتَدَرِّجِ. لَيْسَ فِيهَا نَصُّ حَدِيثٍ وَلَا آيَةٌ، وَلَا يَصِحُّ أَنْ تُنْسَبَ جُمْلَةٌ مِنْهَا إِلَى حَدِيثٍ.",
  "en": "ORIGINAL Level-2 graded Arabic: two narratives preserved in the Sahihs of al-Bukhari and Muslim — the man who watered the dog and the woman who shut in the cat — RETOLD FREELY in the wording of a graded reader. No sentence is the text of a hadith, no verse is quoted, and none may be cited as such.",
  "tr": "ÖZGÜN 2. seviye kolaylaştırılmış Arapça: Buhârî ve Müslim'in Sahîh'lerinde nakledilen iki kıssa — köpeği sulayan adam ve kediyi hapseden kadın — kolaylaştırılmış okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir hadisin metni değildir, hiçbir âyet aktarılmamıştır; hiçbiri hadis diye nakledilemez.",
  "reviewStatus": "pending-scholarly-review"},
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
