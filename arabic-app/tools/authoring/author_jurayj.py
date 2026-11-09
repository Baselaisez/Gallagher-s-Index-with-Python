"""Author content/samples/jurayj-al-abid — «جُرَيْجٌ الْعَابِدُ», the twenty-fifth ORIGINAL story and the fifth at Level 3 (wave 123).

ORIGINAL graded Arabic: Jurayj, a worshipper with a hermitage, does not answer his mother's call three days running while he
prays; she prays that he not die before he is tried among people; a woman of the town bears a shepherd's child and says it is
Jurayj's; the people tear down his hermitage and beat him; he prays, strokes the infant's head and asks «who is your
father?», and the infant speaks from the cradle: «so-and-so the shepherd»; the people offer to rebuild the hermitage of gold
and he asks for clay, as it was. The narrative is preserved in the ḥadīth collections (al-Bukhārī, Muslim) and is RETOLD
FREELY here in a graded reader's wording: no sentence is the text of a ḥadīth and none may be cited as one; no āya is quoted.
Four chapters, nineteen sentences. Written on the authoring kit (story_kit.py); two entries are new — the name جُرَيْج and the
noun صَوْمَعَة; every verb's paradigm is the shelf's. Regenerate with:
python3 tools/authoring/author_jurayj.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "jurayj-al-abid"
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
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
HAL_FULL = (" — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the nominal clause fills the seat of nasb as a hal", "; isim cümlesi hâl olarak mahallen mansûb")
NAAT_CL_RAF = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ", "; the clause fills the seat of raf' as the adjective of the indefinite noun before it", "; cümle, önceki nekre ismin na'tı olarak mahallen merfû")
NAAT_CL_NASB = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ", "; the clause fills the seat of nasb as the adjective of the indefinite noun before it", "; cümle, önceki nekre ismin na'tı olarak mahallen mansûb")
DIM = (" — عَلَمٌ عَلَى وَزْنِ التَّصْغِيرِ فُعَيْلٍ، مُنْصَرِفٌ", " — a proper name on the diminutive pattern فُعَيْل, fully declined", " — tasgîr vezni fuʿayl üzere bir alem, munsarif")

# ---- the name and the hermitage in their seats -------------------------------------------------------------------------
JURAYJ_F = lambda punct=None: FAIL("جُرَيْجٌ", "jurayj", "propn", note_ar=DIM[0], note_en=DIM[1], note_tr=DIM[2], punct=punct)
JURAYJ_ISMK = lambda punct=None: ISMK("جُرَيْجٌ", "jurayj", "propn", note_ar=DIM[0], note_en=DIM[1], note_tr=DIM[2], punct=punct)
JURAYJ_KH = lambda punct=None: KHABAR("جُرَيْجٌ", "jurayj", note_ar=DIM[0], note_en=DIM[1], note_tr=DIM[2], punct=punct)
JURAYJ_MAF = lambda punct=None: MAFUL("جُرَيْجًا", "jurayj", "propn", note_ar=DIM[0], note_en=DIM[1], note_tr=DIM[2], punct=punct)
JURAYJ_J = lambda punct=None: MAJR("جُرَيْجٍ", "jurayj", "propn", note_ar=DIM[0], note_en=DIM[1], note_tr=DIM[2], punct=punct)
JURAYJ_ISM_ANNA = lambda punct=None: tok("جُرَيْجًا", "jurayj", "propn", ["inna-wa-akhawatuha", "inna-am-anna"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + DIM[0] + ".", "The noun of أَنَّ, in nasb" + DIM[1] + ".", "Enne'nin ismi, mansûb" + DIM[2] + ".", punct=punct)
JURAYJ_MUNADA = lambda punct=None: tok("جُرَيْجُ", "jurayj", "propn", ["vocative-munada", "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"],
    "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The called name — a single proper noun built on damma in the seat of nasb.", "Münâdâ — müfred alem, damme üzere mebnî, mahallen mansûb.", punct=punct)
SAWMAA_ISMK = lambda punct=None: ISMK("صَوْمَعَةٌ", "sawmaa", muakhkhar=True, punct=punct)
SAWMAA_J = lambda punct=None: MAJR("الصَّوْمَعَةِ", "sawmaa", punct=punct)
GHULAMU_MUNADA = lambda punct=None: tok("غُلَامُ", "ghulam", "noun", ["vocative-munada", "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"],
    "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The called noun — an indefinite made definite by the call, built on damma in the seat of nasb.", "Münâdâ — nekre-i maksûde, damme üzere mebnî, mahallen mansûb.", punct=punct)
RABBI = lambda punct=None: tok("رَبِّ", "rabb", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness", "hadhf-wa-taqdir"],
    "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَحُذِفَتِ الْيَاءُ وَبَقِيَتِ الْكَسْرَةُ دَلِيلًا عَلَيْهَا.",
    "The called noun «my Lord», annexed to the speaker's ya and in nasb by an estimated fatha; the ya itself is dropped and its kasra stays as its trace.",
    "Münâdâ «Rabbim» — mütekellim yâ'sına muzâf, takdîrî fetha ile mansûb; yâ hazfedilmiş, kesresi ona delil olarak kalmıştır.", punct=punct)
ALLAHUMMA = lambda punct=None: tok("اللّٰهُمَّ", "allahumma", "propn", ["vocative-munada", "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"],
    "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَالْمِيمُ الْمُشَدَّدَةُ عِوَضٌ عَنْ يَاءِ النِّدَاءِ الْمَحْذُوفَةِ.",
    "The called name «O God», built on damma in the seat of nasb; the doubled mim stands in for the dropped vocative يَا.", "Münâdâ, alem, damme üzere mebnî, mahallen mansûb; şeddeli mîm, hazfedilen nidâ yâ'sından bedeldir.", punct=punct)
WA_HUWA_HAL = lambda: tok("وَهُوَ", "huwa", "pron", ["al-hal-jumla-wa-rabituha", "mubtada-khabar", "al-mabni-wal-mudmar"],
    "الْوَاوُ حَالِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw opens a hal clause; «he» is a detached pronoun built on fatha, the mubtada in the seat of raf'.", "Hâl vâvı; «o» munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")])

# ---- the verbs whose shape the kit does not hold ------------------------------------------------------------------------
NADATHU = lambda full="فَنَادَتْهُ", punct=None, shart=False: tok(full, "nada", "verb", ["naqis-verbs", "form-iii-verbs", "al-bariz-al-muttasil", "maful-bihi"] + (["al-majzum-wal-shart-wal-jaza"] if shart else []),
    (FA_AR if full.startswith("فَ") else "") + "نَادَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ" + ("، فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ" if shart else "") + "، وَالتَّاءُ لِلتَّأْنِيثِ" + ("" if shart else "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ") + "، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    ("The fa conjoins; " if full.startswith("فَ") else "") + "«she called him» — a past naqis verb built on a fatha estimated on the alif that dropped before the ta" + (", in the seat of jazm as the verb of the condition" if shart else "") + "; the ta marks the feminine" + ("" if shart else " and the doer «she» is hidden") + "; the attached «him» is its object.",
    ("Fâ atıf; " if full.startswith("فَ") else "") + "«ona seslendi» — tâ'dan önce düşen elif üzerinde takdîrî fetha ile mebnî nâkıs mâzî" + ("; şart fiili olarak mahallen meczûm" if shart else "") + "; tâ te'nîs içindir" + ("" if shart else "; fâil gizli «o»") + "; bitişik «onu» mef'ûlün bih.",
    punct=punct, segments=[s for s in [(seg("فَ", "fa", "conj") if full.startswith("فَ") else None), seg("نَادَتْ", "nada", "verb"), seg("هُ", "pron-3ms", "pron")] if s])
YUJIBHA = lambda punct=None: tok("يُجِبْهَا", "ajaba", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ يُجِيبْ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "Present verb in jazm after لَمْ, its sign the sukun; the hollow verb's middle letter drops where two quiescents meet (يُجِيبْ → يُجِبْ); the doer «he» is hidden and the attached «her» is its object.",
    "Lem ile meczûm muzâri, alâmeti sükûn; ecvef fiilin aynı iki sâkin karşılaşınca düşer (yücîb → yücib); fâil gizli «o», bitişik «onu/ona» mef'ûlün bih.",
    punct=punct, segments=[seg("يُجِبْ", "ajaba", "verb"), seg("هَا", "pron-3fs", "pron")])
TUMITHU = lambda punct=None: tok("تُمِتْهُ", "amata", "verb", ["nawasib-wa-jawazim-al-mudari", "la-nahiya", "form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ تُمِيتْ)، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "«Do not let him die» — a present verb in jazm after the prohibiting لَا, its sign the sukun; the hollow middle letter drops (تُمِيتْ → تُمِتْ); the doer «You» must stay hidden and the attached «him» is its object.",
    "«Onu öldürme» — nehiy lâ'sı ile meczûm muzâri, alâmeti sükûn; ecvef fiilin aynı düşer (tümît → tümit); fâil «Sen» vücûben müstetir, bitişik «onu» mef'ûlün bih.",
    punct=punct, segments=[seg("تُمِتْ", "amata", "verb"), seg("هُ", "pron-3ms", "pron")])
HATTA = lambda: tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
    "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْفِعْلُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «until»: a particle of jarr marking the end-point; the verb after it is put in nasb by an أَنْ that must stay hidden, and the clause they build is in jarr after حَتَّى.", "Hattâ «-e kadar»: gâye ve cer harfi; sonraki fiil vücûben gizli en ile mansûb, kurdukları müevvel masdar hattâ ile mecrûr.")
YUFTANA = lambda: tok("يُفْتَنَ", "fatana", "verb", ["nawasib-wa-jawazim-al-mudari", "naib-al-fail", "al-majhul-fil-kafiya"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "«he is put to trial» — a present passive in nasb by the hidden أَنْ after حَتَّى, its sign the fatha; the deputy doer «he» is hidden.", "«fitneye düşürülür» — hattâ'dan sonra gizli en ile mansûb meçhul muzâri, alâmeti fetha; nâib-i fâil gizli «o».")
YADU = lambda punct=None: tok("يَدْعُ", "daa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْوَاوِ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "Present verb in jazm after لَمْ — its sign is the DROPPED weak letter (يَدْعُو → يَدْعُ); the doer «he» is hidden.", "Lem ile meczûm muzâri — alâmeti illet harfinin (vâv) hazfidir (yed'û → yed'u); fâil gizli «o».", punct=punct)
AIDUHA = lambda punct=None: tok("أَعِيدُوهَا", "aada", "verb", ["imperative-amr", "form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi", "afal-khamsa"],
    "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَوَاوُ الْجَمَاعَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "«Put it back» — an imperative built on the dropped nun, since its present is one of the five verbs; the waw of the group is the doer and the attached «it» the object.", "«Onu geri koyun» — muzârii ef'âl-i hamseden olduğu için nûnun hazfi üzere mebnî emir; cemâat vâvı fâil, bitişik «onu» mef'ûlün bih.",
    punct=punct, segments=[seg("أَعِيدُو", "aada", "verb"), seg("هَا", "pron-3fs", "pron")])
BANAWHA = lambda punct=None: tok("فَبَنَوْهَا", "bana", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
    FA_AR + "بَنَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَوَاوُ الْجَمَاعَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "The fa conjoins; «they built it» — a past naqis verb built on a damma estimated on the alif that dropped before the waw of the group (بَنَى + وا → بَنَوْا); the waw is the doer and the attached «it» the object.",
    "Fâ atıf; «onu yaptılar» — cemâat vâvından önce düşen elif üzerinde takdîrî damme ile mebnî nâkıs mâzî (benâ + vâv → benev); vâv fâil, bitişik «onu» mef'ûlün bih.",
    punct=punct, segments=[seg("فَ", "fa", "conj"), seg("بَنَوْ", "bana", "verb"), seg("هَا", "pron-3fs", "pron")])
KANAT_HID = lambda punct=None: tok("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "hadhf-wa-taqdir"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَخَبَرُهَا مَحْذُوفٌ تَقْدِيرُهُ: مِنْ طِينٍ.",
    "كَانَ with the feminine ta; its noun «she/it» is hidden and its predicate is left unsaid («as it was [of clay]»).", "Kâne, te'nîs tâ'sı ile; ismi gizli «o», haberi hazfedilmiştir («[çamurdan] olduğu gibi»).", punct=punct)
KAMA = lambda: tok("كَمَا", "kama", "part", ["huruf-jarr", "masdar", "tashbih"],
    "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَمَا مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْكَافِ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ: إِعَادَةً كَكَوْنِهَا.",
    "The kaf of likeness is a jarr letter and مَا builds a masdar after it; the clause they form is in jarr («as it was»).", "Teşbih kâfı cer harfi, mâ masdariyye; kurdukları müevvel masdar kâf ile mecrûr («olduğu gibi»).",
    segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")])
AYDAN = lambda punct=None: tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq", "hadhf-wa-taqdir"],
    "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: آضَ أَيْضًا — أَيْ رَجَعَ رُجُوعًا، وَالْمَعْنَى: كَذٰلِكَ.", "«also» — the absolute object of a dropped verb (آضَ «he returned»), frozen into an adverb meaning «likewise».", "«de/dahi» — hazfedilmiş bir fiilin (âde «döndü») mef'ûl-i mutlakı, «aynı şekilde» anlamında kalıplaşmıştır.", punct=punct)
THANI_J = lambda: tok("الثَّانِي", "thani", "noun", ["naat-sifa", "ism-maqsur-manqus", "asma-al-adad-fil-kafiya"],
    "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ، وَهُوَ عَدَدٌ تَرْتِيبِيٌّ عَلَى فَاعِلٍ.",
    "«the second» — an adjective in jarr by a kasra estimated on the ya (a manqus noun); the ordinal on the pattern فَاعِل.", "«ikinci» — yâ üzerinde takdîrî kesre ile mecrûr na't (ism-i menkûs); fâil vezninde sıra sayısı.")
ABU_ISMK = lambda: tok("أَبُو", "ab", "noun", ["kana-wa-akhawatuha", "five-nouns", "idafa-definiteness"],
    "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The noun of كَانَ, in raf' by the WAW — one of the five nouns — and annexed.", "Kâne'nin ismi, esmâ-i hamseden olduğu için vâv ile merfû; muzâf.")
ABUKA = lambda punct=None: tok("أَبُوكَ", "ab", "noun", ["mubtada-khabar", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"],
    "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "«your father» — the predicate, in raf' by the waw as one of the five nouns, annexed to the attached «your».", "«baban» — haber, esmâ-i hamseden olduğu için vâv ile merfû; bitişik kâf muzâfun ileyh.", punct=punct, segments=[seg("أَبُو", "ab", "noun"), seg("كَ", "pron-2ms", "pron")])
ABI = lambda: tok("أَبِي", "ab", "noun", ["mubtada-khabar", "five-nouns", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"],
    "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — فَالْأَسْمَاءُ الْخَمْسَةُ إِذَا أُضِيفَتْ إِلَى الْيَاءِ أُعْرِبَتْ بِحَرَكَاتٍ مُقَدَّرَةٍ لَا بِالْحُرُوفِ — مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "«my father» — the mubtada, in raf' by a damma estimated before the speaker's ya: annexed to that ya, the five nouns decline by estimated vowels, not by letters; the ya is the second term of the idafa.",
    "«babam» — mübtedâ, mütekellim yâ'sından önce takdîrî damme ile merfû: esmâ-i hamse bu yâ'ya muzâf olunca harflerle değil takdîrî harekelerle i'râb edilir; yâ muzâfun ileyh.", segments=[seg("أَبِ", "ab", "noun"), seg("ي", "pron-1s", "pron")])
AL_RAI = lambda punct=None: tok("الرَّاعِي", "rai", "noun", ["naat-sifa", "ism-maqsur-manqus", "ism-fail"],
    "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ تَثْبُتُ يَاؤُهُ مَعَ الْأَلِفِ وَاللَّامِ.", "«the shepherd» — an adjective in raf' by a kasra… no: by a damma estimated on the ya; a manqus noun whose ya stays once it carries the article.", "«çoban» — yâ üzerinde takdîrî damme ile merfû na't; ism-i menkûs, harf-i tarif alınca yâ'sı sabit kalır.", punct=punct)
RAIYAN_KHK = lambda: KHK("رَاعِيًا", "rai", extra=["ism-maqsur-manqus", "ism-fail"], note_ar=" — اسْمٌ مَنْقُوصٌ تَظْهَرُ فَتْحَتُهُ لِخِفَّتِهَا", note_en=" — a manqus noun whose fatha SHOWS, being light", note_tr=" — ism-i menkûs, fethası hafif olduğu için zâhirdir")
UMMI_MUB = lambda: tok("أُمِّي", "umm", "noun", ["mubtada-khabar", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil", "hadhf-wa-taqdir"],
    "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْخَبَرُ مَحْذُوفٌ تَقْدِيرُهُ: أُمِّي تُنَادِينِي.",
    "«my mother» — the mubtada, in raf' by a damma estimated before the speaker's ya, annexed to it; the predicate is left unsaid («my mother [is calling me]»).", "«annem» — mütekellim yâ'sından önce takdîrî damme ile merfû mübtedâ, ona muzâf; haber hazfedilmiştir («annem [beni çağırıyor]»).",
    segments=[seg("أُمّ", "umm", "noun"), seg("ي", "pron-1s", "pron")])
WA_SALATI = lambda punct=None: tok("وَصَلَاتِي", "salat", "noun", ["atf-nasaq", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil", "hadhf-wa-taqdir"],
    WA_AR + "صَلَاةُ مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَخَبَرُهُ مَحْذُوفٌ تَقْدِيرُهُ: وَصَلَاتِي أَقْطَعُهَا؟ فَأَيَّهُمَا أُقَدِّمُ؟",
    "The waw conjoins «my prayer», in raf' by an estimated damma and annexed to the speaker's ya; its predicate too is unsaid («and my prayer — [do I break it?]»): the worshipper weighs the two.",
    "Vâv atıf; «namazım» — takdîrî damme ile merfû, mütekellim yâ'sına muzâf; haberi hazfedilmiştir («ya namazım — [onu keseyim mi?]»): âbid ikisini tartar.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("صَلَاتِ", "salat", "noun"), seg("ي", "pron-1s", "pron")])
MA_IST = lambda: tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar", "al-mabni-wal-mudmar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the interrogative noun built on sukun, the mubtada in the seat of raf'.", "«ne» — sükûn üzere mebnî istifhâm ismi, mübtedâ olarak mahallen merfû.")
LAKUM_KH = lambda punct=None: tok("لَكُمْ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ: مَا لَكُمْ؟ أَيْ: مَا شَأْنُكُمْ؟",
    "The lam is a jarr letter and the attached «you» fills the seat of jarr; the phrase is the predicate — «what is [the matter] with you?»", "Lâm cer harfi, bitişik «siz» mahallen mecrûr; câr-mecrûr haberdir — «size ne oluyor?»", punct=punct, segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")])
MAN_IST = lambda: tok("مَنْ", "man", "pron", ["al-istifham", "mubtada-khabar", "al-mabni-wal-mudmar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the interrogative noun built on sukun, the mubtada in the seat of raf'.", "«kim» — sükûn üzere mebnî istifhâm ismi, mübtedâ olarak mahallen merfû.")
MAN_SHART_ANNA = lambda: tok("مَنْ", "man", "pron", ["al-majzum-wal-shart-wal-jaza", "inna-wa-akhawatuha", "al-mabni-wal-mudmar"],
    "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ، وَجُمْلَتَا الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ رَفْعٍ خَبَرُهَا.",
    "«whoever» — the conditional noun that governs jazm, built on sukun in the seat of nasb as the noun of أَنَّ; the condition and its answer together are its predicate.", "«her kim» — cezmeden şart ismi, sükûn üzere mebnî, enne'nin ismi olarak mahallen mansûb; şart ve cevap cümleleri birlikte haberidir.")
AYNA = lambda: tok("أَيْنَ", "ayna", "pron", ["al-istifham", "maful-fih", "mubtada-khabar", "al-mabni-wal-mudmar"],
    "اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ، وَهُوَ خَبَرٌ مُقَدَّمٌ.", "«where» — the interrogative of place, built on fatha in the seat of nasb as an adverb; it is the FRONTED predicate.", "«nerede» — mekân istifhâmı, fetha üzere mebnî, zarf olarak mahallen mansûb; öne alınmış haberdir.")
ANNA = lambda role=("", "", ""), full="أَنَّ": tok(full, "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"] + (["atf-nasaq"] if full.startswith("وَ") else []),
    (WA_AR if full.startswith("وَ") else "") + "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".",
    ("The waw conjoins; " if full.startswith("وَ") else "") + "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".",
    ("Vâv atıf; " if full.startswith("وَ") else "") + "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".",
    segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part")] if full.startswith("وَ") else None)
ISM_ANNA = lambda full, lex, pos="noun", note=("", "", ""), punct=None: tok(full, lex, pos, ["inna-wa-akhawatuha", "inna-am-anna"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + note[0] + ".", "The noun of أَنَّ, in nasb" + note[1] + ".", "Enne'nin ismi, mansûb" + note[2] + ".", punct=punct)
KH_ANNA_N = lambda full, lex, extra=None, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha", "inna-am-anna"] + (extra or []), "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of أَنَّ, in raf'.", "Enne'nin haberi, merfû.", punct=punct)
ISM_INNA = lambda full, lex, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of إِنَّ, in nasb.", "İnne'nin ismi, mansûb.", punct=punct)
IBNUKA_KH = lambda punct=None: tok("ابْنُكَ", "ibn", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"],
    "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«your son» — the predicate of إِنَّ, in raf' and annexed to the attached «your».", "«senin oğlun» — inne'nin haberi, merfû; bitişik kâf muzâfun ileyh.", punct=punct, segments=[seg("ابْنُ", "ibn", "noun"), seg("كَ", "pron-2ms", "pron")])
FA_ALAYHI = lambda: tok("فَعَلَيْهِ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "al-majzum-wal-shart-wal-jaza", "mubtada-khabar"],
    "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَعَلَى حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
    "The fa ties the answer of the condition to it; عَلَى is a jarr letter and the attached «him» fills the seat of jarr; the phrase is the FRONTED predicate («upon him [is] …»), and the clause is the answer, in the seat of jazm.",
    "Fâ, şartın cevabını bağlar; alâ cer harfi, bitişik «o» mahallen mecrûr; câr-mecrûr öne alınmış haberdir («ona düşer…»), cümle şartın cevabı olarak mahallen meczûm.",
    segments=[seg("فَ", "fa", "conj"), seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")])
WA_IBADATIHI = lambda punct=None: tok("وَعِبَادَتِهِ", "ibada", "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "عِبَادَةِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The waw conjoins «his worship», in jarr like the word before it and annexed to the attached «his».", "Vâv atıf; «ibadeti» — öncekine uyarak mecrûr, bitişik zamire muzâf.",
    punct=punct, segments=[seg("وَ", "wa", "conj"), seg("عِبَادَتِ", "ibada", "noun"), seg("هِ", "pron-3ms", "pron")])
LA_JAWAB = lambda punct=None: tok("لَا", "la", "part", ["la-nafiya"], "حَرْفُ جَوَابٍ يَنْفِي مَا قَبْلَهُ، لَا عَمَلَ لَهُ.", "«No» — the answer particle that denies what was proposed; it governs nothing.", "«Hayır» — kendinden önce söyleneni reddeden cevap harfi; amel etmez.", punct=punct)
PREP_KH = lambda full, lex, punct=None: PREP(full, lex, " — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ", "; the jarr phrase is the predicate", "; câr-mecrûr haberdir", punct=punct, gloss_tr={"min": "«-den»", "fi": "«-de»"}[lex])
PREP_KH_HAL = lambda: PREP("فِي", "fi", " — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the jarr phrase is the predicate, and the nominal clause is a hal in the seat of nasb", "; câr-mecrûr haber, isim cümlesi hâl olarak mahallen mansûb", gloss_tr="«-de»")
QARIBAN = lambda: tok("قَرِيبًا", "qarib", "noun", ["hal", "maful-fih", "sifa-mushabbaha"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (أَوْ ظَرْفُ مَكَانٍ) — يُبَيِّنُ هَيْئَةَ الرَّعْيِ: قَرِيبًا مِنَ الصَّوْمَعَةِ.", "«near» — a hal in nasb (or an adverb of place): how the grazing went, «close to the hermitage».", "«yakınında» — mansûb hâl (ya da mekân zarfı): otlatmanın hâli, «savmaaya yakın».")

TITLES = [{"ar": "جُرَيْجٌ وَأُمُّهُ", "en": "Jurayj and his mother", "tr": "Cüreyc ve annesi"},
          {"ar": "الْفِتْنَةُ", "en": "The trial", "tr": "Fitne"},
          {"ar": "الْغُلَامُ يَتَكَلَّمُ", "en": "The infant speaks", "tr": "Bebek konuşuyor"},
          {"ar": "صَوْمَعَةٌ مِنْ طِينٍ", "en": "A hermitage of clay", "tr": "Çamurdan bir savmaa"}]

# ---- Chapter 1 — جُرَيْجٌ وَأُمُّهُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "In a town there was a worshipper named Jurayj, and he had a hermitage in which he worshipped God.", "tr": "Bir kasabada Cüreyc adında âbid bir adam vardı; onun, içinde Allah'a ibadet ettiği bir savmaası vardı."},
 "tokens": [KANA("كَانَ"), PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"), MAJR("قَرْيَةٍ", "qarya"), ISMK("رَجُلٌ", "rajul", muakhkhar=True), NAAT("عَابِدٌ", "abid", "raf", ["ism-fail"]),
  ENC_NOUN("اسْمُهُ", "ism", "هُ", "mubtada", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِرَجُلٍ", note_en="; the clause is a second adjective of «a man», in the seat of raf'", note_tr="; cümle «adam»ın ikinci na'tı, mahallen merfû"), JURAYJ_KH(punct="،"),
  KANA("وَكَانَتْ", fem=True), LAHU("لَهُ", "pron-3ms", " («onun»)"), SAWMAA_ISMK(), MUDARI("يَعْبُدُ", "abada", note_ar=NAAT_CL_RAF[0] + " لِصَوْمَعَةٍ", note_en=NAAT_CL_RAF[1], note_tr=NAAT_CL_RAF[2]), ALLAH_MAF(), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "One day his mother came to him while he was praying, and called him: «Jurayj!»", "tr": "Bir gün annesi, o namaz kılarken yanına geldi ve ona seslendi: «Cüreyc!»"},
 "tokens": [ENC_MADI("فَجَاءَتْهُ", "jaa", "هُ", ["hollow-verbs"], fem=True), ENC_NOUN("أُمُّهُ", "umm", "هُ", "fail"), ZARF("يَوْمًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False), WA_HUWA_HAL(),
  MUDARI("يُصَلِّي", "salla", ["form-ii-verbs"], naqis="ي", note_ar=KH_CL[0] + HAL_FULL[0], note_en=KH_CL[1] + HAL_FULL[1], note_tr=KH_CL[2] + HAL_FULL[2], punct="،"), NADATHU(punct=":"), YA(), JURAYJ_MUNADA(punct="!")]})
S1.append({"id": "s3", "translation": {"en": "He said to himself: «My Lord — my mother, and my prayer!» Then he stayed at his prayer and did not answer her.", "tr": "Kendi kendine dedi: «Rabbim — annem mi, namazım mı!» Sonra namazında kaldı ve ona cevap vermedi."},
 "tokens": [QALA_F("فَقَالَ", hidden=True), FI(), ENC_NOUN("نَفْسِهِ", "nafs", "هِ", "majr", punct=":"), YA(), RABBI(punct="،"), UMMI_MUB(), WA_SALATI(punct="!"),
  MADI("فَبَقِيَ", "baqiya", ["naqis-verbs"], hidden=True), FI(), ENC_NOUN("صَلَاتِهِ", "salat", "هِ", "majr"), LAM_JAZM("وَلَمْ"), YUJIBHA(punct=".")]})
S1.append({"id": "s4", "translation": {"en": "Then she came to him on the second day and called him, and he did not answer her; then she came to him on the third day, and he did not answer her either.", "tr": "Sonra ikinci gün yanına gelip ona seslendi, o cevap vermedi; üçüncü gün yine geldi, yine cevap vermedi."},
 "tokens": [THUMMA(), ENC_MADI("جَاءَتْهُ", "jaa", "هُ", ["hollow-verbs"], fem=True, hidden=True), FI(), MAJR("الْيَوْمِ", "yawm"), THANI_J(), NADATHU(punct="،"), LAM_JAZM("فَلَمْ"), YUJIBHA(punct="،"),
  THUMMA(), ENC_MADI("جَاءَتْهُ", "jaa", "هُ", ["hollow-verbs"], fem=True, hidden=True), FI(), MAJR("الْيَوْمِ", "yawm"), NAAT("الثَّالِثِ", "thalith", "jarr", ["asma-al-adad-fil-kafiya"]), LAM_JAZM("فَلَمْ"), YUJIBHA(), AYDAN(punct=".")]})
S1.append({"id": "s5", "translation": {"en": "So his mother grew angry and said: «O God, do not let him die until he is put to trial among the people.»", "tr": "Annesi kızdı ve dedi: «Allah'ım, insanlar arasında fitneye düşmeden onu öldürme.»"},
 "tokens": [MADI("فَغَضِبَتْ", "ghadiba", fem=True), ENC_NOUN("أُمُّهُ", "umm", "هُ", "fail"), QALAT("وَقَالَتْ", punct=":"), ALLAHUMMA(punct="،"), LA_NAHIYA(), TUMITHU(), HATTA(), YUFTANA(), ZARF("بَيْنَ", "bayna"), MUDAF_ILAYH("النَّاسِ", "nas", punct=".")]})

# ---- Chapter 2 — الْفِتْنَةُ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "There was a woman in the town; she bore a boy, and the boy's father was a shepherd who grazed the sheep near the hermitage.", "tr": "Kasabada bir kadın vardı; bir oğlan doğurdu. Oğlanın babası, koyunları savmaanın yakınında otlatan bir çobandı."},
 "tokens": [KANA("وَكَانَتْ", fem=True), PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"), MAJR("الْقَرْيَةِ", "qarya"), ISMK("امْرَأَةٌ", "imraa", muakhkhar=True, punct="،"), MADI("فَوَلَدَتْ", "walada", ["mithal-verbs"], fem=True, hidden=True), MAFUL("غُلَامًا", "ghulam", punct="،"),
  KANA("وَكَانَ"), ABU_ISMK(), MUDAF_ILAYH("الْغُلَامِ", "ghulam"), RAIYAN_KHK(), MUDARI("يَرْعَى", "raa-graze", ["naqis-verbs"], naqis="ا", note_ar=NAAT_CL_NASB[0] + " لِرَاعِيًا", note_en=NAAT_CL_NASB[1], note_tr=NAAT_CL_NASB[2]), MAFUL("الْغَنَمَ", "ghanam"), QARIBAN(), MINA(), SAWMAA_J(punct=".")]})
S2.append({"id": "s2", "translation": {"en": "The woman said to the people: «This boy is from Jurayj the worshipper!»", "tr": "Kadın insanlara dedi: «Bu oğlan âbid Cüreyc'tendir!»"},
 "tokens": [MADI("فَقَالَتِ", "qala", ["hollow-verbs", "maful-bihi"], fem=True, kasra=True, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), FAIL("الْمَرْأَةُ", "imraa"), LI_AL("لِلنَّاسِ", "nas", "النَّاسِ", punct=":"),
  ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ"), BADAL("الْغُلَامُ", "ghulam", "raf", note_ar=" — بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", note_en=" — the substitute that names what the demonstrative points at", note_tr=" — işaret isminden bedel"),
  PREP_KH("مِنْ", "min"), JURAYJ_J(), NAAT("الْعَابِدِ", "abid", "jarr", ["ism-fail"], punct="!")]})
S2.append({"id": "s3", "translation": {"en": "The people grew angry and came to the hermitage; they tore it down and beat Jurayj.", "tr": "İnsanlar öfkelendi ve savmaaya geldiler; onu yıktılar ve Cüreyc'i dövdüler."},
 "tokens": [MADI("فَغَضِبَ", "ghadiba"), FAIL("النَّاسُ", "nas"), VERB_WAW("وَجَاءُوا", "jaa", ["hollow-verbs"]), ILA(), SAWMAA_J(punct="،"), VERB_WAW_ENC("فَهَدَمُوهَا", "hadama", "هَا"), VERB_WAW("وَضَرَبُوا", "daraba"), JURAYJ_MAF(punct=".")]})
S2.append({"id": "s4", "translation": {"en": "He said to them: «What is the matter with you?» They said: «This woman says the boy is your son!»", "tr": "Onlara dedi: «Size ne oluyor?» Dediler: «Bu kadın, oğlanın senin oğlun olduğunu söylüyor!»"},
 "tokens": [QALA_F("فَقَالَ", hidden=True), LAHU("لَهُمْ", "pron-3mp", " («onlara»)", punct=":"), MA_IST(), LAKUM_KH(punct="؟"), VERB_WAW("قَالُوا", "qala", ["hollow-verbs", "maful-bihi"], punct=":"),
  ISHARA("هٰذِهِ", "hadhihi", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"), BADAL("الْمَرْأَةُ", "imraa", "raf", note_ar=" — بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", note_en=" — the substitute of the demonstrative", note_tr=" — işaret isminden bedel"),
  MUDARI("تَقُولُ", "qala", ["hollow-verbs", "maful-bihi"], who="هِيَ", note_ar=KH_CL[0] + MAQUL[0], note_en=KH_CL[1] + MAQUL[1], note_tr=KH_CL[2] + MAQUL[2], punct=":"), INNA(), ISM_INNA("الْغُلَامَ", "ghulam"), IBNUKA_KH(punct="!")]})
S2.append({"id": "s5", "translation": {"en": "Jurayj said: «Where is the boy?» So they brought him.", "tr": "Cüreyc dedi: «Oğlan nerede?» Onu getirdiler."},
 "tokens": [QALA_F("فَقَالَ"), JURAYJ_F(punct=":"), AYNA(), MUBTADA("الْغُلَامُ", "ghulam", note_ar=" مُؤَخَّرٌ", note_en=" (placed after its predicate)", note_tr=" (haberinden sonra)", punct="؟"), VERB_WAW("فَجَاءُوا", "jaa", ["hollow-verbs"]),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onu»)", punct=".", note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ: جَاءُوا بِهِ أَيْ أَحْضَرُوهُ", note_en=" — this ba makes the verb transitive: «they came with him» is «they brought him»", note_tr=" — bu bâ ta'diye içindir: «onunla geldiler» = «onu getirdiler»")]})
S2.append({"id": "s6", "translation": {"en": "Jurayj was patient: he neither grew angry nor prayed against them.", "tr": "Cüreyc sabırlıydı: ne öfkelendi ne de onlara beddua etti."},
 "tokens": [KANA("وَكَانَ"), JURAYJ_ISMK(), KHK("صَابِرًا", "sabir", extra=["ism-fail"], punct="،"), LAM_JAZM("فَلَمْ"), JAZM_V("يَغْضَبْ", "ghadiba", hidden="هُوَ"), LAM_JAZM("وَلَمْ"), YADU(), ALAYHIM(punct=".")]})

# ---- Chapter 3 — الْغُلَامُ يَتَكَلَّمُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "Jurayj stood up, prayed and called on his Lord; then he came to the boy.", "tr": "Cüreyc kalktı, namaz kıldı ve Rabbine dua etti; sonra oğlanın yanına geldi."},
 "tokens": [MADI("فَقَامَ", "qama", ["hollow-verbs"]), JURAYJ_F(), MADI_ALIF("فَصَلَّى", "salla", ["form-ii-verbs"], hidden=True), MADI_ALIF("وَدَعَا", "daa", hidden=True), ENC_NOUN("رَبَّهُ", "rabb", "هُ", "maful", punct="،"), THUMMA(), MADI_ALIF("أَتَى", "ata", hidden=True), MAFUL("الْغُلَامَ", "ghulam", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "He stroked his head and said: «Boy, who is your father?»", "tr": "Başını okşadı ve dedi: «Ey çocuk, baban kim?»"},
 "tokens": [MADI("فَمَسَحَ", "masaha", hidden=True), ENC_NOUN("رَأْسَهُ", "ras", "هُ", "maful"), QALA("وَقَالَ", hidden=True, punct=":"), YA(), GHULAMU_MUNADA(punct="،"), MAN_IST(), ABUKA(punct="؟")]})
S3.append({"id": "s3", "translation": {"en": "The boy spoke while he was in the cradle, and said: «My father is so-and-so, the shepherd.»", "tr": "Çocuk beşikteyken konuştu ve dedi: «Babam falanca çobandır.»"},
 "tokens": [MADI("فَتَكَلَّمَ", "takallama", ["form-v-verbs"]), FAIL("الْغُلَامُ", "ghulam"), WA_HUWA_HAL(), PREP_KH_HAL(), MAJR("الْمَهْدِ", "mahd-cradle", punct="،"), QALA("وَقَالَ", hidden=True, punct=":"), ABI(), KHABAR("فُلَانٌ", "fulan"), AL_RAI(punct=".")]})
S3.append({"id": "s4", "translation": {"en": "The people marvelled, and they knew that Jurayj was innocent and that the woman had not told the truth.", "tr": "İnsanlar şaşırdı ve Cüreyc'in suçsuz olduğunu, kadının doğru söylemediğini anladılar."},
 "tokens": [MADI("فَعَجِبَ", "ajiba"), FAIL("النَّاسُ", "nas", punct="،"), VERB_WAW("وَعَرَفُوا", "arafa", ["mafulayn"]),
  ANNA((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَرَفَ", "; the clause it builds stands for both objects of «they knew»", "; kurduğu müevvel masdar arafe'nin iki mef'ûlünün yerini tutar")), JURAYJ_ISM_ANNA(), KH_ANNA_N("بَرِيءٌ", "bari", ["sifa-mushabbaha"]),
  ANNA(full="وَأَنَّ"), ISM_ANNA("الْمَرْأَةَ", "imraa"), LAM_JAZM(), JAZM_V("تَصْدُقْ", "sadaqa-verb", hidden="هِيَ", note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2], punct=".")]})

# ---- Chapter 4 — صَوْمَعَةٌ مِنْ طِينٍ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "They said to him: «We will build your hermitage for you of gold.»", "tr": "Ona dediler: «Savmaanı sana altından yapalım.»"},
 "tokens": [VERB_WAW("فَقَالُوا", "qala", ["hollow-verbs", "maful-bihi"]), LAHU("لَهُ", "pron-3ms", " («ona»)", punct=":"), MUDARI("نَبْنِي", "bana", ["naqis-verbs"], who="نَحْنُ", naqis="ي", wujub=True), LAHU("لَكَ", "pron-2ms", " («sana»)"), ENC_NOUN("صَوْمَعَتَكَ", "sawmaa", "كَ", "maful"), MIN(), MAJR("ذَهَبٍ", "dhahab", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He said: «No — put it back of clay, as it was.»", "tr": "Dedi: «Hayır — onu çamurdan, olduğu gibi yeniden yapın.»"},
 "tokens": [QALA_F("قَالَ", punct=":", hidden=True), LA_JAWAB(punct="،"), AIDUHA(), MIN(), MAJR("طِينٍ", "tin"), KAMA(), KANAT_HID(punct=".")]})
S4.append({"id": "s3", "translation": {"en": "So they built it of clay as it was, and Jurayj went back to his hermitage and his worship.", "tr": "Onu çamurdan, olduğu gibi yaptılar; Cüreyc savmaasına ve ibadetine döndü."},
 "tokens": [BANAWHA(), MIN(), MAJR("طِينٍ", "tin"), KAMA(), KANAT_HID(punct="،"), MADI("وَرَجَعَ", "rajaa"), JURAYJ_F(), ILA(), ENC_NOUN("صَوْمَعَتِهِ", "sawmaa", "هِ", "majr"), WA_IBADATIHI(punct=".")]})
S4.append({"id": "s4", "translation": {"en": "And the people learned that God answers a mother's prayer, and that whoever is called by his mother must answer her.", "tr": "İnsanlar öğrendi ki Allah annenin duasını kabul eder; annesi kendisine seslenen kimsenin ona cevap vermesi gerekir."},
 "tokens": [MADI("وَعَلِمَ", "alima", ["mafulayn"]), FAIL("النَّاسُ", "nas"), ANNA((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَلِمَ", "; the clause it builds stands for both objects of «they learned»", "; kurduğu müevvel masdar alime'nin iki mef'ûlünün yerini tutar")),
  ISM_ANNA("اللهَ", "allah", "propn", LAFZ), MUDARI("يَسْتَجِيبُ", "istajaba", ["form-x-verbs", "hollow-verbs"], note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]), MAFUL("دُعَاءَ", "dua", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْأُمِّ", "umm", punct="،"),
  ANNA(full="وَأَنَّ"), MAN_SHART_ANNA(), NADATHU("نَادَتْهُ", shart=True), ENC_NOUN("أُمُّهُ", "umm", "هُ", "fail"), FA_ALAYHI(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ مُؤَخَّرٌ", "; the clause it builds is the mubtada, placed after its predicate", "; kurduğu müevvel masdar sonraya bırakılmış mübtedâdır"), MANSUB_AN("يُجِيبَهَا", "ajaba", ["form-iv-verbs", "hollow-verbs"], enc="هَا", punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf; two entries are new -------------------------------------
PREF = ["qisas-al-nabiyyin-4", "al-kafiya", "al-amana-wa-al-khashaba", "ashab-al-ghar", "tawbat-al-qatil", "al-abras-wa-al-aqra-wa-al-ama", "luqman-wa-ibnuh", "adam-wa-iblis",
        "dhu-al-qarnayn-wa-al-sadd", "wasiyyat-abi-yusuf-l5", "izhar-al-asrar", "al-asad-wa-al-arnab", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
PREF = [p for p in PREF if _pkg_dir(p).joinpath("glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
FORCE = {"ma-masdariyya": "al-kafiya", "sadaqa-verb": "al-kafiya"}
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

NEW_GLOSS = {
 "jurayj": {"lemma": "جُرَيْج", "root": "ج ر ج", "pos": "propn", "gloss": {"en": "Jurayj — a worshipper of the Children of Israel (a name on the diminutive pattern فُعَيْل)", "tr": "Cüreyc — İsrailoğulları'ndan bir âbid (tasgîr vezni fuʿayl üzere bir isim)"}, "level": 3},
 "sawmaa": {"lemma": "صَوْمَعَة", "root": "ص م ع", "pos": "noun", "plural": "صَوَامِع", "gloss": {"en": "a hermit's cell, a hermitage (a monk's tower of worship)", "tr": "savmaa, inziva kulesi (râhibin ibadet yeri)"}, "level": 3},
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

LEVEL_NAME = json.loads((ROOT / "content/samples/qisas-al-nabiyyin-4/manifest.json").read_text(encoding="utf-8")).get("levelName", "Intermediate")
MANIFEST = {
 "id": "jurayj-al-abid",
 "storyGroup": "jurayj-al-abid",
 "title": {"ar": "جُرَيْجٌ الْعَابِدُ", "en": "Jurayj the Worshipper", "tr": "Âbid Cüreyc"},
 "subtitle": {"ar": "عَابِدٌ لَمْ يُجِبْ أُمَّهُ وَهُوَ يُصَلِّي فَدَعَتْ عَلَيْهِ، ثُمَّ تَكَلَّمَ غُلَامٌ فِي الْمَهْدِ فَبَرَّأَهُ — قِصَّةٌ لِلْمُسْتَوَى الثَّالِثِ",
              "en": "A worshipper does not answer his mother while he prays and she prays against him; then an infant speaks from the cradle and clears him — a story for the third level",
              "tr": "Namaz kılarken annesine cevap vermeyen âbid ve annesinin bedduası; sonra beşikteki bir bebek konuşup onu aklar — üçüncü seviye için bir hikâye"},
 "level": 3,
 "levelName": LEVEL_NAME,
 "version": "0.1.0",
 "published": "2026-11-09",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّالِثُ) لِخَبَرِ جُرَيْجٍ الْعَابِدِ الْمَرْوِيِّ فِي الصَّحِيحَيْنِ، بِأُسْلُوبِ كِتَابِ الْقِرَاءَةِ الْمُتَدَرِّجِ. لَيْسَ فِيهَا نَصُّ حَدِيثٍ وَلَا آيَةٌ، وَلَا يَصِحُّ أَنْ تُنْسَبَ جُمْلَةٌ مِنْهَا إِلَى حَدِيثٍ.",
  "en": "ORIGINAL Level-3 graded Arabic: the narrative of Jurayj the worshipper, preserved in the Sahihs of al-Bukhari and Muslim, RETOLD FREELY in the wording of a graded reader. No sentence is the text of a hadith, no verse is quoted, and none may be cited as such.",
  "tr": "ÖZGÜN 3. seviye kolaylaştırılmış Arapça: Buhârî ve Müslim'in Sahîh'lerinde nakledilen âbid Cüreyc kıssası, kolaylaştırılmış okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir hadisin metni değildir, hiçbir âyet aktarılmamıştır; hiçbiri hadis diye nakledilemez.",
  "reviewStatus": "pending-scholarly-review",
 },
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
