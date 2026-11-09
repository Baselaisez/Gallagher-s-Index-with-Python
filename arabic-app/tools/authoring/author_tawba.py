"""Author content/samples/tawbat-al-qatil — «تَوْبَةُ الْقَاتِلِ», the twenty-third ORIGINAL story and the third at Level 3 (wave 116).

ORIGINAL graded Arabic: a man who has killed ninety-nine people asks whether repentance is open to him; a monk says no and
becomes the hundredth; a learned man says yes and sends him to a land of worshippers; he dies on the road, the angels of mercy
and of punishment disagree over him, and an angel in human form judges by which land lies nearer. The narrative is preserved in
the ḥadīth collections (al-Bukhārī and Muslim) and is RETOLD FREELY here in a graded reader's wording: no sentence is the text
of a ḥadīth and none may be cited as one. Four chapters, twenty-three sentences. Written on the authoring kit (story_kit.py);
five entries are new (رَاهِب، حَكَم، شِبْر، نِصْف، تَائِب), none of them verbs.  Regenerate with:
python3 tools/authoring/author_tawba.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "tawbat-al-qatil"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
if not (ROOT / "tools/authoring/story_kit.py").exists(): sys.path.insert(0, "/tmp/claude-0/-home-user-Gallagher-s-Index-with-Python/612c64cf-e6b9-547d-9c53-f32b7b6377b6/scratchpad/w113")   # the kit before it lands (wave 113)
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

# ============ «تَوْبَةُ الْقَاتِلِ» — the twenty-third ORIGINAL story, the third at Level 3 (wave 116) ============
PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "هِمَا": "pron-3d", "هُمَا": "pron-3d", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هَا": "pron-3fs"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "هِمَا": "هُمَا", "هُمَا": "هُمَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هَا": "هَا"})

TAFDIL_DIPT = ("، وَهُوَ اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ",
               " — an elative on أَفْعَل, barred from tanwin as an adjective on the verb's pattern", " — ef'al vezninde ism-i tafdîl; vasfiyet ve fiil vezni sebebiyle gayr-i munsarif")
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_F = lambda full="فَقَالَ": MADI(full, "qala", ["hollow-verbs", "maful-bihi"], note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
ALLAHU_F = lambda punct=None: ALLAH_F(punct=punct)

# --- the compound number ninety-nine and its tamyīz --------------------------------------------------------------
TISA_MAF = lambda: tok("تِسْعَةً", "tisa", "noun", ["maful-bihi", "asma-al-adad-fil-kafiya"],
    "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمَعْطُوفِ، وَهُوَ مُذَكَّرٌ لِأَنَّ مَعْدُودَهُ (نَفْس) مُؤَنَّثٌ.",
    "The direct object, in nasb — the units of a conjoined number; it is masculine in form because its counted noun نَفْس is feminine (three to nine take the opposite gender).",
    "Mef'ûlün bih, mansûb — atıflı sayının birler basamağı; ma'dûdu (nefs) müennes olduğu için müzekker gelir (üçten dokuza sayılar ma'dûduna zıt gelir).")
TISA_KH_INNA = lambda: tok("تِسْعَةً", "tisa", "noun", ["maful-bihi", "asma-al-adad-fil-kafiya"],
    "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمَعْطُوفِ، مُذَكَّرٌ لِأَنَّ مَعْدُودَهُ مُؤَنَّثٌ.",
    "The direct object of «I killed», in nasb — the units of a conjoined number, masculine because the counted noun is feminine.",
    "«Öldürdüm»ün mef'ûlü, mansûb — atıflı sayının birler basamağı; ma'dûdu müennes olduğu için müzekker.")
TISIN_ATF = lambda: tok("وَتِسْعِينَ", "tisun", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"],
    WA_AR + "تِسْعِينَ مَعْطُوفٌ عَلَى تِسْعَةٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — عَقْدٌ مِنَ الْعُقُودِ لَا يَتَغَيَّرُ بِالتَّذْكِيرِ وَالتَّأْنِيثِ.",
    "The waw conjoins; «ninety» is conjoined to «nine», in nasb by the ya because the tens are declined like the sound masculine plural; a ten does not change for gender.",
    "Vâv atıf; «doksan», «dokuz»a ma'tûf, yâ ile mansûb — onluklar cem-i müzekker sâlime mülhaktır ve cinse göre değişmez.", segments=[seg("وَ", "wa", "conj"), seg("تِسْعِينَ", "tisun", "noun")])
NAFS_TAMYIZ = lambda punct=None: tok("نَفْسًا", "nafs", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"],
    "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — تَمْيِيزُ الْعَدَدِ مِنْ أَحَدَ عَشَرَ إِلَى تِسْعَةٍ وَتِسْعِينَ مُفْرَدٌ مَنْصُوبٌ.",
    "The tamyiz (specifier), in nasb — from eleven to ninety-nine the counted noun is a singular in nasb.",
    "Temyîz, mansûb — on birden doksan dokuza kadar ma'dûd müfred ve mansûb gelir.", punct=punct)

# --- the question words and the particles of answer --------------------------------------------------------------
MAN_ISTIFHAM = lambda full="مَنْ", pre="": tok(full, "man", "pron", ["al-istifham", "mubtada-khabar", "al-mabni-wal-mudmar"],
    pre + "مَنْ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
    ("The waw opens a new clause; " if pre else "") + "«Who?» is an interrogative noun built on sukun, the mubtada in the seat of raf'.",
    ("Vâv isti'nâf içindir; " if pre else "") + "«kim?» — sükûn üzere mebnî istifhâm ismi, mübtedâ olarak mahallen merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("مَنْ", "man", "pron")] if pre else None)
HAL_Q = lambda full="هَلْ": tok(full, "hal-istifham", "part", ["al-istifham"],
    (FA_AR if full.startswith("فَ") else "") + "هَلْ حَرْفُ اسْتِفْهَامٍ لِطَلَبِ التَّصْدِيقِ.",
    ("The fa conjoins; " if full.startswith("فَ") else "") + "هَلْ asks a yes-or-no question.", ("Fâ atıf; " if full.startswith("فَ") else "") + "hel — tasdik isteyen istifhâm harfi.",
    segments=[seg("فَ", "fa", "conj"), seg("هَلْ", "hal-istifham", "part")] if full.startswith("فَ") else None)
NAAM = lambda punct=None: tok("نَعَمْ", "naam", "part", [], "حَرْفُ جَوَابٍ لِتَقْرِيرِ مَا قَبْلَهُ.", "The answer particle «yes», affirming what was asked.", "Cevap harfi «evet»; sorulanı tasdik eder.", punct=punct)
LA_JAWAB = lambda punct=None: tok("لَا", "la", "part", [], "حَرْفُ جَوَابٍ لِنَفْيِ مَا سُئِلَ عَنْهُ.", "The answer particle «no», denying what was asked.", "Cevap harfi «hayır»; sorulanı nefyeder.", punct=punct)

# --- the kind-denying لَا, the extra مِنْ, the lam of possession ------------------------------------------------------
LA_JINS = lambda: tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"],
    "لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ إِنَّ: تَنْصِبُ الِاسْمَ وَتَرْفَعُ الْخَبَرَ.",
    "The kind-denying لَا «no … at all», which works like إِنَّ: its noun in nasb, its predicate in raf'.", "Cinsini nefyeden lâ; inne gibi amel eder: ismini nasb, haberini ref eder.")
TAWBA_ISM_LA = lambda: tok("تَوْبَةَ", "tawba", "noun", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"],
    "اسْمُ لَا النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — نَكِرَةٌ مُفْرَدَةٌ.",
    "The noun of the kind-denying لَا, built on fatha in the seat of nasb — a single indefinite noun.", "Cinsini nefyeden lâ'nın ismi, fetha üzere mebnî, mahallen mansûb — müfred nekre.")
LAKA_KH_LA = lambda punct=None: tok("لَكَ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "la-nafiya-lil-jins"],
    "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَا.",
    "The lam is a jarr letter and the attached «you» fills the seat of jarr; the jarr phrase is the predicate of لَا.", "Lâm cer harfi, bitişik kâf mahallen mecrûr — câr-mecrûr lâ'nın haberidir.",
    punct=punct, segments=[seg("لَ", "li", "prep"), seg("كَ", "pron-2ms", "pron")])
LI_KH_MUQ = lambda: tok("لِي", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim", "mubtada-khabar"],
    "اللَّامُ حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
    "The lam is a jarr letter and the speaker's ya fills the seat of jarr; the jarr phrase is the FRONTED predicate.", "Lâm cer harfi, mütekellim yâ'sı mahallen mecrûr — câr-mecrûr öne alınmış haberdir.",
    segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")])
MIN_ZAIDA = lambda: tok("مِنْ", "min", "prep", ["huruf-jarr", "huruf-al-ziyada-fil-kafiya"],
    "حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ الْعُمُومِ، يَدْخُلُ عَلَى النَّكِرَةِ بَعْدَ الِاسْتِفْهَامِ.",
    "An EXTRA jarr letter: after a question it enters on the indefinite noun to stress «any at all» — it governs the form, not the meaning.", "Zâid cer harfi: istifhâmdan sonra nekre üzerine gelir, umumu te'kîd eder — lafzı cerreder, mânâyı değil.")
TAWBA_MUB_ZAIDA = lambda punct=None: tok("تَوْبَةٍ", "tawba", "noun", ["mubtada-khabar", "huruf-al-ziyada-fil-kafiya", "mahall-al-majrur"],
    "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا بِمِنَ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا — «هَلْ لِي تَوْبَةٌ».",
    "The mubtada, placed after its predicate: in jarr in form after the extra مِنْ, in raf' by seat — «is there any repentance for me?».", "Mübtedâ (haberinden sonra): zâid min ile lafzen mecrûr, mahallen merfû — «benim için tövbe var mı?».", punct=punct)

# --- إِنَّ and لٰكِنَّ with a noun as their ism; the fronted khabar inside إِنَّ ---------------------------------------
FA_INNA = lambda: tok("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], FA_AR + "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
    "The fa conjoins (and gives the reason); إِنَّ is the verb-like particle: its noun in nasb, its predicate in raf'.", "Fâ atıf (sebep bildirir); inne te'kîd ve nasb harfi: ismini nasb, haberini ref eder.",
    segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")])
ISM_INNA_N = lambda full, lex, extra=None, punct=None, note=("", "", ""): tok(full, lex, "noun", ["inna-wa-akhawatuha"] + (extra or []),
    "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + note[0] + ".", "The noun of إِنَّ, in nasb" + note[1] + ".", "İnne'nin ismi, mansûb" + note[2] + ".", punct=punct)
FIHA_KH_INNA = lambda: tok("فِيهَا", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "inna-wa-akhawatuha"],
    "حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ مُقَدَّمٌ.",
    "A jarr letter with the attached «it» in the seat of jarr; the jarr phrase is the FRONTED predicate of إِنَّ (its noun, indefinite, comes after).", "Cer harfi, bitişik hâ mahallen mecrûr — câr-mecrûr inne'nin öne alınmış haberidir (nekre ismi sonra gelir).",
    segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])
WA_LAKINNA = lambda: tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"],
    WA_AR + "لٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
    "The waw conjoins; لٰكِنَّ «but» is the corrective sister of إِنَّ: its noun in nasb, its predicate in raf'.", "Vâv atıf; lâkinne — inne'nin istidrâk bildiren kardeşi: ismini nasb, haberini ref eder.",
    segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")])
ARDAKA_ISM_LAKINNA = lambda: tok("أَرْضَكَ", "ard", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"],
    "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The noun of لٰكِنَّ, in nasb; annexed, and the attached «your» is the second term of the idafa in the seat of jarr.", "Lâkinne'nin ismi, mansûb; muzâf, bitişik kâf muzâfun ileyh — mahallen mecrûr.",
    segments=[seg("أَرْضَ", "ard", "noun"), seg("كَ", "pron-2ms", "pron")])
ARD_KH_LAKINNA = lambda: tok("أَرْضُ", "ard", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"],
    "خَبَرُ لٰكِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The predicate of لٰكِنَّ, in raf' and annexed.", "Lâkinne'nin haberi, merfû, muzâf.")
BAB_ISM_INNA = lambda: ISM_INNA_N("بَابَ", "bab", ["idafa-definiteness"], note=("، مُضَافٌ", " and annexed", ", muzâf"))

# --- verbs the kit does not shape -------------------------------------------------------------------------------
YUGHLAQU = lambda: tok("يُغْلَقُ", "aghlaqa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "form-iv-verbs", "inna-wa-akhawatuha"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ — ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ — وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْبَابِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.",
    "A present verb in the passive, in raf' — its first letter takes damma and the letter before the last a fatha; the deputy doer «it» (the door) is hidden, and the clause fills the seat of raf' as the predicate of إِنَّ.",
    "Meçhul muzâri, merfû — evveli mazmûm, âhirinden önceki harf meftûh; nâib-i fâil gizli «o» (kapı); cümle inne'nin haberi olarak mahallen merfû.")
QILA = lambda: tok("وَقِيلَ", "qala", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "hollow-verbs"],
    WA_AR + "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — أَصْلُهُ قُوِلَ، نُقِلَتْ كَسْرَةُ الْوَاوِ إِلَى الْقَافِ فَقُلِبَتِ الْوَاوُ يَاءً — وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ.",
    "The waw conjoins; «it was said» is a hollow verb in the passive, built on fatha: from قُوِلَ the kasra moved to the qaf and the waw became ya; the quoted clause after it stands as its deputy doer.",
    "Vâv atıf; «denildi» — meçhul ecvef mâzî: aslı kuvile, vâvın kesresi kâfa nakledilince vâv yâ'ya döndü; hikâye edilen cümle nâib-i fâildir.",
    punct=":", segments=[seg("وَ", "wa", "conj"), seg("قِيلَ", "qala", "verb")])
KANA_SHART = lambda: tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza", "hollow-verbs"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "كَانَ as the verb of the condition, built on fatha in the seat of jazm; its noun is the hidden «he».", "Şart fiili olarak kâne, fetha üzere mebnî, mahallen meczûm; ismi gizli «o».")
FA_HUWA_JAWAB = lambda: tok("فَهُوَ", "huwa", "pron", ["al-fa-fi-jawab-al-shart", "mubtada-khabar", "al-mabni-wal-mudmar", "al-majzum-wal-shart-wal-jaza"],
    "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ لِأَنَّهُ جُمْلَةٌ اسْمِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
    "The fa binds the condition's answer, which is a nominal clause; «he» is a detached pronoun built on fatha, the mubtada in the seat of raf'.", "Fâ, isim cümlesi olan şartın cevabını bağlar; «o» munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû.",
    segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")])
AYYATIHIMA = lambda: tok("أَيَّتِهِمَا", "ayy", "pron", ["huruf-jarr", "al-majzum-wal-shart-wal-jaza", "idafa-definiteness", "al-bariz-al-muttasil", "al-muthanna"],
    "اسْمُ شَرْطٍ جَازِمٌ مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ (أَيَّةُ مُؤَنَّثُ أَيٍّ، وَهُوَ الْمُعْرَبُ مِنْ أَسْمَاءِ الشَّرْطِ)، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِأَقْرَبَ.",
    "A conditional noun that governs jazm, itself in jarr after إِلَى by the kasra (أَيَّة is the feminine of أَيّ, the one conditional noun that declines); annexed, with the dual «the two of them» as the second term in the seat of jarr — the phrase attaches to «nearer».",
    "Cezmeden şart ismi, ilâ ile kesre üzere mecrûr (eyye, eyy'in müennesi — i'râb alan tek şart ismi); muzâf, tesniye zamiri «o ikisi» muzâfun ileyh, mahallen mecrûr — câr-mecrûr «daha yakın»a müteallik.",
    segments=[seg("أَيَّةِ", "ayy", "pron"), seg("هِمَا", "pron-3d", "pron")])
FA_ILA = lambda: tok("فَإِلَى", "ila", "prep", ["huruf-jarr"], FA_AR + "إِلَى حَرْفُ جَرٍّ.", "The fa conjoins; إِلَى is a jarr letter.", "Fâ atıf; ilâ cer harfi.", segments=[seg("فَ", "fa", "conj"), seg("إِلَى", "ila", "prep")])
ARDAYN = lambda punct=None: tok("الْأَرْضَيْنِ", "ard", "noun", ["huruf-jarr", "al-muthanna", "al-muthanna-fil-kafiya"],
    "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ.",
    "In jarr by the ya because it is a dual; the nun stands in for the tanwin of the singular.", "Tesniye olduğu için yâ ile mecrûr; nûn, müfredin tenvîninden bedeldir.", punct=punct)
AQRAB_KHK = lambda: tok("أَقْرَبَ", "aqrab", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"],
    "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ" + TAFDIL_DIPT[0] + ".", "The predicate of كَانَ, in nasb" + TAFDIL_DIPT[1] + ".", "Kâne'nin haberi, mansûb" + TAFDIL_DIPT[2] + ".")
AQRAB_MAF2 = lambda: tok("أَقْرَبَ", "aqrab", "noun", ["maful-bihi", "mafulayn", "ism-tafdil", "mamnu-min-sarf"],
    "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ" + TAFDIL_DIPT[0] + ".", "The second object of «they found», in nasb" + TAFDIL_DIPT[1] + ".", "«Buldular»ın ikinci mef'ûlü, mansûb" + TAFDIL_DIPT[2] + ".")
HAKAM_MAF2 = lambda punct=None: tok("حَكَمًا", "hakam", "noun", ["maful-bihi", "mafulayn"],
    "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — جَعَلَ هُنَا بِمَعْنَى صَيَّرَ، تَنْصِبُ مَفْعُولَيْنِ.",
    "The second object, in nasb — جَعَلَ here means «to make into» and takes two objects.", "İkinci mef'ûlün bih, mansûb — ce'ale burada «kılmak» anlamında iki mef'ûl alır.", punct=punct)
ALLATI_NAAT = lambda: tok("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"],
    "اسْمٌ مَوْصُولٌ لِلْمُفْرَدَةِ الْمُؤَنَّثَةِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلْأَرْضِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
    "The feminine relative pronoun, built on sukun in the seat of jarr as the adjective of «the land»; the clause after it is its clause.", "Müennes ism-i mevsûl, sükûn üzere mebnî, «arz»ın na'tı olarak mahallen mecrûr; sonraki cümle sılasıdır.")
MA_MAJR = lambda: tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"],
    "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِعَلَى، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ — وَالْعَائِدُ مَحْذُوفٌ: مَا فَعَلَهُ.",
    "A relative pronoun built on sukun in the seat of jarr after عَلَى; the clause after it is its clause, and the returning pronoun is omitted («what he did [it]»).", "İsm-i mevsûl, sükûn üzere mebnî, alâ ile mahallen mecrûr; sonraki cümle sılası, âid zamir hazfedilmiş («yaptığı [şey]»).")
KADHA_MI = lambda: tok("كَذَا", "kadha", "noun", ["al-kinayat-wal-zuruf-al-mabniyya", "idafa-definiteness"],
    "كِنَايَةٌ عَنِ اسْمِ الْبَلَدِ مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A stand-in for the town's name («such-and-such»), built on sukun in the seat of jarr as the second term of the idafa.", "Belde adının yerini tutan kinâye («falanca»), sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr.")
WA_KADHA = lambda punct=None: tok("وَكَذَا", "kadha", "noun", ["atf-nasaq", "al-kinayat-wal-zuruf-al-mabniyya"],
    WA_AR + "كَذَا كِنَايَةٌ مَعْطُوفَةٌ مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "The waw conjoins a second «such-and-such», built on sukun in the seat of jarr.", "Vâv atıf; ikinci «falanca», sükûn üzere mebnî, mahallen mecrûr.",
    punct=punct, segments=[seg("وَ", "wa", "conj"), seg("كَذَا", "kadha", "noun")])
QAWMAN_ISM_INNA = lambda: ISM_INNA_N("قَوْمًا", "qawm", note=(" مُؤَخَّرٌ — نَكِرَةٌ سَوَّغَ الِابْتِدَاءَ بِهَا تَقَدُّمُ الْخَبَرِ", ", placed after its predicate — an indefinite noun the fronted predicate allows", " (haberinden sonra) — öne alınan haber nekre olmasına cevaz verir"))
SALIHIN_NAAT = lambda: tok("صَالِحِينَ", "salih", "noun", ["naat-sifa", "jam-mudhakkar-salim", "ism-fail"],
    "نَعْتٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "An adjective agreeing with «a people», in nasb by the ya as a sound masculine plural.", "Na't, cem-i müzekker sâlim olduğu için yâ ile mansûb.")
MAAHUM = lambda punct=None: tok("مَعَهُمْ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb and annexed to the attached «them».", "Mekân zarfı «ile», mansûb, muzâf; bitişik «onlar» muzâfun ileyh.",
    punct=punct, segments=[seg("مَعَ", "maa", "noun"), seg("هُمْ", "pron-3mp", "pron")])
BAYNAHUM = lambda: tok("بَيْنَهُمْ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "An adverb of place «between», in nasb and annexed to the attached «them».", "Mekân zarfı «arasında», mansûb, muzâf; bitişik «onlar» muzâfun ileyh.",
    segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمْ", "pron-3mp", "pron")])
KULLAHA = lambda punct=None: tok("كُلَّهَا", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
    "تَوْكِيدٌ مَعْنَوِيٌّ لِذُنُوبِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A tawkid of meaning for «his sins», in nasb like them and annexed to the attached pronoun that refers back to them.", "«Günahları»nın mânevî te'kîdi, onun gibi mansûb; muzâf, bitişik zamir muzâfun ileyh.",
    punct=punct, segments=[seg("كُلَّ", "kull", "noun"), seg("هَا", "pron-3fs", "pron")])
MARRATAN = lambda: tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"],
    "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلْعَدَدِ مَنْصُوبٌ بِالْفَتْحَةِ.", "An absolute object that counts the act («one more time»), in nasb.", "Sayı bildiren mef'ûlün mutlak, mansûb.")
UKHRA_NAAT = lambda punct=None: tok("أُخْرَى", "ukhra", "noun", ["naat-sifa", "ism-maqsur-manqus", "mamnu-min-sarf"],
    "نَعْتٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مُؤَنَّثُ آخَرَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ.",
    "An adjective of «a time», in nasb by a fatha estimated on the alif — the feminine of آخَر, barred from tanwin by its feminine alif.", "«Kez»in na'tı, elif üzerindeki takdîrî fetha ile mansûb — âhar'ın müennesi, te'nîs elifi sebebiyle gayr-i munsarif.", punct=punct)
ALAM_KH = lambda: tok("أَعْلَمُ", "alam-elative", "noun", ["mubtada-khabar", "ism-tafdil", "idafa-definiteness"],
    "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ أُضِيفَ إِلَى مَعْرِفَةٍ فَجَازَ إِفْرَادُهُ.",
    "The predicate, in raf' and annexed — an elative on أَفْعَل annexed to a definite noun («the most learned of the people of the earth»).", "Haber, merfû, muzâf — ef'al vezninde ism-i tafdîl, marifeye muzâf («yeryüzü halkının en bilgini»).")
ALAM_NAAT_RAF = lambda: tok("أَعْلَمُ", "alam-elative", "noun", ["naat-sifa", "ism-tafdil", "mamnu-min-sarf"],
    "نَعْتٌ لِأَحَدٍ مَرْفُوعٌ بِالضَّمَّةِ" + TAFDIL_DIPT[0] + "، وَ«مِنْ» بَعْدَهُ لِلتَّفْضِيلِ.", "An adjective of «anyone», in raf'" + TAFDIL_DIPT[1] + "; the مِنْ after it is the «than» of comparison.", "«Biri»nin na'tı, merfû" + TAFDIL_DIPT[2] + "; sonraki min tafdîl içindir.")
FI_KH_MUQ_MUB = lambda: PREP("فِي", "fi", "، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate", "; câr-mecrûr öne alınmış haberdir", gloss_tr="«-de»")
NAAT_CL_RAJUL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِرَجُلٍ", "; the clause qualifies «a man» — in the seat of raf' as its na't", "; cümle «adam»ın na'tı olarak mahallen merfû")
NAAT_CL_QAWM = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِقَوْمٍ", "; the clause is a second adjective of «a people», in the seat of nasb", "; cümle «kavim»in ikinci na'tı, mahallen mansûb")
MUDAF_ILAYH_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ لِإِذَا", "; the clause fills the seat of jarr, annexed to إِذَا", "; cümle izâ'ya muzâfun ileyh olarak mahallen mecrûr")
JAWAB_IDHA = (" — وَالْجُمْلَةُ جَوَابُ إِذَا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of إِذَا and has no seat of its own", "; cümle izâ'nın cevabıdır, i'râbdan mahalli yoktur")
MASDAR_NAZ = (" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَنْصُوبٌ بِنَزْعِ الْخَافِضِ: أَمَرَهَا بِالِاقْتِرَابِ", "; the clause it builds stands as an object after the dropped preposition («commanded it to draw near»)", "; kurduğu müevvel masdar, hâfızın nez'iyle mansûb («yaklaşmasını emretti»)")
MASDAR_NAZ2 = (" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَنْصُوبٌ بِنَزْعِ الْخَافِضِ: أَمَرَهَا بِالتَّبَاعُدِ", "; the clause it builds stands as an object after the dropped preposition («commanded it to move away»)", "; kurduğu müevvel masdar, hâfızın nez'iyle mansûb («uzaklaşmasını emretti»)")
MUDAF_NOTE = ("، مُضَافٌ", ", annexed", ", muzâf")

TITLES = [{"ar": "الرَّجُلُ وَالرَّاهِبُ", "en": "The man and the monk", "tr": "Adam ve rahip"},
          {"ar": "الْعَالِمُ وَالطَّرِيقُ", "en": "The learned man and the road", "tr": "Âlim ve yol"},
          {"ar": "الْمَلَائِكَةُ تَخْتَلِفُ", "en": "The angels disagree", "tr": "Melekler ihtilâfa düşer"},
          {"ar": "الْأَرْضُ تَقْتَرِبُ", "en": "The land draws near", "tr": "Yer yaklaşır"}]

# ---- Chapter 1 — الرَّجُلُ وَالرَّاهِبُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "In a town there was a man who had killed ninety-nine people.", "tr": "Bir beldede doksan dokuz kişi öldürmüş bir adam vardı."},
 "tokens": [KANA("كَانَ"), FI((KH_MUQ[0], KH_MUQ[1], KH_MUQ[2])), MAJR("قَرْيَةٍ", "qarya"), ISMK("رَجُلٌ", "rajul", muakhkhar=True),
  MADI("قَتَلَ", "qatala", hidden=True, note_ar=NAAT_CL_RAJUL[0], note_en=NAAT_CL_RAJUL[1], note_tr=NAAT_CL_RAJUL[2]), TISA_MAF(), TISIN_ATF(), NAFS_TAMYIZ(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "Then he regretted what he had done, and he wished to repent to God.", "tr": "Sonra yaptığına pişman oldu ve Allah'a tövbe etmek istedi."},
 "tokens": [THUMMA(), MADI("نَدِمَ", "nadima", hidden=True), ALA(), MA_MAJR(), MADI("فَعَلَ", "faala", hidden=True, punct="،", note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]),
  MADI("وَأَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True), AN_MAFUL(), MANSUB_AN("يَتُوبَ", "taba-repent", ["hollow-verbs"]), ILA(), ALLAH_J(punct=".")]})
S1.append({"id": "s3", "translation": {"en": "So he asked the people: «Who is the most learned of the people of the earth?» — and they pointed him to a monk.", "tr": "İnsanlara sordu: «Yeryüzü halkının en bilgini kimdir?» Onu bir rahibe yönlendirdiler."},
 "tokens": [MADI("فَسَأَلَ", "saala", hidden=True), MAFUL("النَّاسَ", "nas", punct=":"), MAN_ISTIFHAM(), ALAM_KH(), MUDAF_ILAYH("أَهْلِ", "ahl", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]),
  MUDAF_ILAYH("الْأَرْضِ", "ard", punct="؟"), VERB_WAW_ENC("فَدَلُّوهُ", "dalla", "هُ", ["doubled-verbs"]), ALA(), MAJR("رَاهِبٍ", "rahib", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "He came to him and said to him: «I have killed ninety-nine people; is there any repentance for me?»", "tr": "Ona gelip dedi ki: «Ben doksan dokuz kişi öldürdüm; benim için tövbe var mı?»"},
 "tokens": [ENC_MADI("فَأَتَاهُ", "ata", "هُ", alif=True, hidden=True), QALA("وَقَالَ", hidden=True), LAHU("لَهُ", "pron-3ms", "«ona»", punct=":"), INNA_ENC("إِنِّي", "ي", " («ben»)"),
  MADI_T("قَتَلْتُ", "qatala", who="ana", note_ar=KH_INNA[0], note_en=KH_INNA[1], note_tr=KH_INNA[2]), TISA_KH_INNA(), TISIN_ATF(), NAFS_TAMYIZ(punct="،"),
  HAL_Q("فَهَلْ"), LI_KH_MUQ(), MIN_ZAIDA(), TAWBA_MUB_ZAIDA(punct="؟")]})
S1.append({"id": "s5", "translation": {"en": "The monk said: «No — there is no repentance for you at all.»", "tr": "Rahip dedi: «Hayır, senin için hiçbir tövbe yoktur.»"},
 "tokens": [QALA_F("فَقَالَ"), FAIL("الرَّاهِبُ", "rahib", punct=":"), LA_JAWAB(punct="،"), LA_JINS(), TAWBA_ISM_LA(), LAKA_KH_LA(punct=".")]})
S1.append({"id": "s6", "translation": {"en": "The man grew angry and killed him, and so with him he completed a hundred.", "tr": "Adam öfkelendi ve onu da öldürdü; böylece onunla yüzü tamamladı."},
 "tokens": [MADI("فَغَضِبَ", "ghadiba"), FAIL("الرَّجُلُ", "rajul"), ENC_MADI("وَقَتَلَهُ", "qatala", "هُ", hidden=True, punct="،"), MADI("فَأَكْمَلَ", "akmala", ["form-iv-verbs"], hidden=True), BIHI(),
  MAFUL("مِائَةً", "mia", extra=["asma-al-adad-fil-kafiya"], punct=".", note_ar=" — وَتَمْيِيزُهَا مَحْذُوفٌ: مِائَةَ نَفْسٍ", note_en=" — its specifier is left out («a hundred [souls]»)", note_tr=" — temyîzi hazfedilmiş («yüz [kişi]»)")]})

# ---- Chapter 2 — الْعَالِمُ وَالطَّرِيقُ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "Then he asked once more: «Is there anyone on earth more learned than this one?»", "tr": "Sonra bir kez daha sordu: «Yeryüzünde bundan daha bilgin biri var mı?»"},
 "tokens": [THUMMA(), MADI("سَأَلَ", "saala", hidden=True), MARRATAN(), UKHRA_NAAT(punct=":"), HAL_Q(), FI_KH_MUQ_MUB(), MAJR("الْأَرْضِ", "ard"),
  MUBTADA("أَحَدٌ", "ahad", note_ar=" مُؤَخَّرٌ", note_en=" (placed after its predicate)", note_tr=" (haberinden sonra)"), ALAM_NAAT_RAF(),
  MIN((" — مِنْ هُنَا لِلتَّفْضِيلِ", "; this مِنْ is the «than» after the elative", "; bu min, ism-i tafdîlden sonraki tafdîl min'idir")), ISHARA("هٰذَا", "hadha", "جَرٍّ", "jarr", "mecrûr", punct="؟")]})
S2.append({"id": "s2", "translation": {"en": "They pointed him to a learned man; he went to him and told him his story.", "tr": "Onu bilgin bir adama yönlendirdiler; ona gitti ve kıssasını anlattı."},
 "tokens": [VERB_WAW_ENC("فَدَلُّوهُ", "dalla", "هُ", ["doubled-verbs"]), ALA(), MAJR("رَجُلٍ", "rajul"), NAAT("عَالِمٍ", "alim-scholar", "jarr", ["ism-fail"], punct="،"),
  MADI("فَذَهَبَ", "dhahaba", hidden=True), ILAYHI(), MADI("وَقَصَّ", "qassa", ["doubled-verbs"], hidden=True), ALAYHI(), ENC_NOUN("قِصَّتَهُ", "qissa", "هُ", "maful", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "The learned man said: «Yes — and who could keep you from repentance?»", "tr": "Âlim dedi: «Evet; seni tövbeden kim alıkoyabilir ki?»"},
 "tokens": [QALA_F("فَقَالَ"), FAIL("الْعَالِمُ", "alim-scholar", extra=["ism-fail"], punct=":"), NAAM(punct="،"), MAN_ISTIFHAM("وَمَنْ", pre=WA_ISTINAF[0]),
  MUDARI("يَمْنَعُكَ", "manaa", enc="كَ", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ، وَالِاسْتِفْهَامُ إِنْكَارِيٌّ: لَا يَمْنَعُكَ أَحَدٌ", note_en="; the clause is the predicate in the seat of raf', and the question denies («no one can»)", note_tr="; cümle haber olarak mahallen merfû; istifhâm inkârîdir («kimse alıkoyamaz»)"),
  MINA(), MAJR("التَّوْبَةِ", "tawba", punct="؟")]})
S2.append({"id": "s4", "translation": {"en": "«The door of repentance is never shut.»", "tr": "«Tövbe kapısı asla kapanmaz.»"},
 "tokens": [INNA(), BAB_ISM_INNA(), MUDAF_ILAYH("التَّوْبَةِ", "tawba"), LA_NAFIYA(), YUGHLAQU(),
  ZARF("أَبَدًا", "abadan", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False, punct=".", note_ar=" — لِاسْتِغْرَاقِ الْمُسْتَقْبَلِ الْمَنْفِيِّ", note_en=" — it sweeps the whole of the denied future", note_tr=" — nefyedilen geleceğin tümünü kapsar")]})
S2.append({"id": "s5", "translation": {"en": "«But your land is a land of evil, so leave it for such-and-such a town.»", "tr": "«Fakat senin yurdun bir kötülük yurdudur; oradan çık, falanca beldeye git.»"},
 "tokens": [WA_LAKINNA(), ARDAKA_ISM_LAKINNA(), ARD_KH_LAKINNA(), MUDAF_ILAYH("سُوءٍ", "su", punct="،"), AMR("فَاخْرُجْ", "kharaja"), JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («oradan»)"), ILA(),
  MAJR("قَرْيَةِ", "qarya", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), KADHA_MI(), WA_KADHA(punct=".")]})
S2.append({"id": "s6", "translation": {"en": "«For in it there are righteous people who worship God; worship Him with them, and do not return to your land.»", "tr": "«Çünkü orada Allah'a ibadet eden sâlih bir kavim var; onlarla birlikte O'na ibadet et ve yurduna dönme.»"},
 "tokens": [FA_INNA(), FIHA_KH_INNA(), QAWMAN_ISM_INNA(), SALIHIN_NAAT(), MUDARI5("يَعْبُدُونَ", "abada", role_ar=NAAT_CL_QAWM[0], role_en=NAAT_CL_QAWM[1], role_tr=NAAT_CL_QAWM[2]), ALLAH_MAF(punct="،"),
  AMR("فَاعْبُدْهُ", "abada", enc="هُ"), MAAHUM(punct="،"), WA_LA_NAHIYA(), JAZM_V("تَرْجِعْ", "rajaa", by="لَا النَّاهِيَةِ", by_en="the prohibitive لَا", by_tr="nehiy lâ'sı", hidden="أَنْتَ"), ILA(), ENC_NOUN("أَرْضِكَ", "ard", "كَ", "majr", punct=".")]})

# ---- Chapter 3 — الْمَلَائِكَةُ تَخْتَلِفُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "The man set out repentant and travelled along the road, until, when he had reached its midpoint, death came to him.", "tr": "Adam tövbekâr olarak yola çıktı; yolda ilerledi, nihayet yarısına vardığında ölüm ona geldi."},
 "tokens": [MADI("فَخَرَجَ", "kharaja"), FAIL("الرَّجُلُ", "rajul"), HAL("تَائِبًا", "taib", ["ism-fail"], punct="،"), MADI("وَسَارَ", "sara-travel", ["hollow-verbs"], hidden=True), FI(), MAJR("الطَّرِيقِ", "tariq", punct="،"),
  HATTA_IBT(), IDHA("إِذَا"), MADI("بَلَغَ", "balagha", hidden=True, note_ar=MUDAF_ILAYH_CL[0], note_en=MUDAF_ILAYH_CL[1], note_tr=MUDAF_ILAYH_CL[2]), ENC_NOUN("نِصْفَهُ", "nisf", "هُ", "maful"),
  ENC_MADI("أَتَاهُ", "ata", "هُ", alif=True, note_ar=JAWAB_IDHA[0], note_en=JAWAB_IDHA[1], note_tr=JAWAB_IDHA[2]), FAIL("الْمَوْتُ", "mawt", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "He died while he was seeking God's mercy.", "tr": "Allah'ın rahmetini dilerken öldü."},
 "tokens": [MADI("فَمَاتَ", "mata-die", ["hollow-verbs"], hidden=True), WA_HUWA_HAL(), MUDARI("يَطْلُبُ", "talaba", note_ar=KH_CL[0] + "، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", note_en=KH_CL[1] + "; the whole nominal clause is a hal in the seat of nasb", note_tr=KH_CL[2] + "; isim cümlesi hâl olarak mahallen mansûb"),
  MAFUL("رَحْمَةَ", "rahma", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), ALLAH_MI(punct=".")]})
S3.append({"id": "s3", "translation": {"en": "The angels of mercy and the angels of punishment disagreed over him.", "tr": "Rahmet melekleri ile azap melekleri onun hakkında ihtilâfa düştüler."},
 "tokens": [MADI("فَاخْتَلَفَتْ", "ikhtalafa", ["form-viii-verbs"], fem=True), JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onun hakkında»)"),
  FAIL("مَلَائِكَةُ", "malak", extra=["jam-taksir"], note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الرَّحْمَةِ", "rahma"),
  ATF("وَمَلَائِكَةُ", "malak", "noun", "raf", ["jam-taksir", "idafa-definiteness"], note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْعَذَابِ", "adhab", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "The angels of mercy said: «He came repentant, having turned to God with his heart.»", "tr": "Rahmet melekleri dedi: «Tövbekâr olarak geldi; kalbiyle Allah'a yönelmişti.»"},
 "tokens": [MADI("قَالَتْ", "qala", ["hollow-verbs", "maful-bihi"], fem=True, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), FAIL("مَلَائِكَةُ", "malak", extra=["jam-taksir"], note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]),
  MUDAF_ILAYH("الرَّحْمَةِ", "rahma", punct=":"), MADI("جَاءَ", "jaa", ["hollow-verbs"], hidden=True), HAL("تَائِبًا", "taib", ["ism-fail"], punct="،"), WA_QAD(),
  MADI("أَقْبَلَ", "aqbala", ["form-iv-verbs"], hidden=True, note_ar=HAL_CL[0], note_en=HAL_CL[1], note_tr=HAL_CL[2]), BI_NOUN("بِقَلْبِهِ", "qalb", "قَلْبِهِ", enc="هِ"), ILA(), ALLAH_J(punct=".")]})
S3.append({"id": "s5", "translation": {"en": "And the angels of punishment said: «He never did any good at all.»", "tr": "Azap melekleri de dedi: «O hiçbir zaman bir hayır işlemedi.»"},
 "tokens": [MADI("وَقَالَتْ", "qala", ["hollow-verbs", "maful-bihi"], fem=True, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), FAIL("مَلَائِكَةُ", "malak", extra=["jam-taksir"], note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]),
  MUDAF_ILAYH("الْعَذَابِ", "adhab", punct=":"), INNA_ENC("إِنَّهُ", "هُ", " («o»)"), LAM_JAZM(), JAZM_V("يَعْمَلْ", "amila", hidden="هُوَ", note_ar=KH_INNA[0], note_en=KH_INNA[1], note_tr=KH_INNA[2]),
  MAFUL("خَيْرًا", "khayr"), QATTU(punct=".")]})
S3.append({"id": "s6", "translation": {"en": "So God sent them an angel in the form of a human being, and they made him an arbiter between them.", "tr": "Bunun üzerine Allah onlara insan sûretinde bir melek gönderdi; onu aralarında hakem yaptılar."},
 "tokens": [MADI("فَأَرْسَلَ", "arsala", ["form-iv-verbs"]), ALLAHU_F(), ILAYHIM(), MAFUL("مَلَكًا", "malak"), FI(), MAJR("صُورَةِ", "sura", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("إِنْسَانٍ", "insan", punct="،"),
  VERB_WAW_ENC("فَجَعَلُوهُ", "jaala", "هُ", ["mafulayn"], note_ar=" أَوَّلُ", note_en=" — the FIRST of two", note_tr=" — iki mef'ûlün birincisi"), BAYNAHUM(), HAKAM_MAF2(punct=".")]})

# ---- Chapter 4 — الْأَرْضُ تَقْتَرِبُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "The angel said: «Look at the two lands: to whichever of them he was nearer, he belongs to its people.»", "tr": "Melek dedi: «İki yere bakın: hangisine daha yakınsa, o oranın halkındandır.»"},
 "tokens": [QALA_F("فَقَالَ"), FAIL("الْمَلَكُ", "malak", punct=":"), AMR5("انْظُرُوا", "nazara"), ILA(), ARDAYN(punct="،"), FA_ILA(), AYYATIHIMA(), KANA_SHART(), AQRAB_KHK(), FA_HUWA_JAWAB(), MIN(),
  ENC_NOUN("أَهْلِهَا", "ahl", "هَا", "majr", punct=".", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", note_en="; the jarr phrase is the predicate, and the nominal clause fills the seat of jazm as the condition's answer", note_tr="; câr-mecrûr haber; isim cümlesi şartın cevabı olarak mahallen meczûm")]})
S4.append({"id": "s2", "translation": {"en": "They looked, and they found him nearer to the land he had wanted by a single span.", "tr": "Baktılar ve onu, istediği yere bir karış daha yakın buldular."},
 "tokens": [VERB_WAW("فَنَظَرُوا", "nazara", punct="،"), VERB_WAW_ENC("فَوَجَدُوهُ", "wajada", "هُ", ["mafulayn", "mithal-verbs"], note_ar=" أَوَّلُ — وَوَجَدَ هُنَا مِنْ أَفْعَالِ الْقُلُوبِ تَنْصِبُ مَفْعُولَيْنِ", note_en=" — the FIRST of two: «to find» here is a verb of the heart", note_tr=" — iki mef'ûlün birincisi: «bulmak» burada ef'âl-i kulûbdandır"),
  AQRAB_MAF2(), ILA(), MAJR("الْأَرْضِ", "ard"), ALLATI_NAAT(), ENC_MADI("أَرَادَهَا", "arada", "هَا", ["form-iv-verbs", "hollow-verbs"], hidden=True, note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]),
  BI_NOUN("بِشِبْرٍ", "shibr", "شِبْرٍ", note_ar=" — وَالْبَاءُ لِلْمُلَابَسَةِ: بِمِقْدَارِ شِبْرٍ", note_en=" — the ba measures the difference («by a span»)", note_tr=" — bâ miktar bildirir («bir karış kadar»)"), NAAT("وَاحِدٍ", "wahid", "jarr", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "And it is said that God commanded the righteous land to draw near, and commanded the land of evil to move away.", "tr": "Denilir ki Allah sâlih yere yaklaşmasını, kötülük yurduna da uzaklaşmasını emretti."},
 "tokens": [QILA(), INNA(), ALLAH_ISMI(), MADI("أَمَرَ", "amara-command", hidden=True, note_ar=KH_INNA[0], note_en=KH_INNA[1], note_tr=KH_INNA[2]), MAFUL("الْأَرْضَ", "ard"),
  NAAT("الصَّالِحَةَ", "salih", "nasb", ["ism-fail"], note_ar=" — مُؤَنَّثُ صَالِحٍ", note_en=" — the feminine of «righteous»", note_tr=" — sâlih'in müennesi"), AN(*MASDAR_NAZ),
  MANSUB_AN("تَقْتَرِبَ", "iqtaraba", ["form-viii-verbs"], who="هِيَ", punct="،"), MADI("وَأَمَرَ", "amara-command", hidden=True), MAFUL("أَرْضَ", "ard", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]),
  MUDAF_ILAYH("السُّوءِ", "su"), AN(*MASDAR_NAZ2), MANSUB_AN("تَتَبَاعَدَ", "tabaaada", ["form-vi-verbs"], who="هِيَ", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "So the angels of mercy took him, and God forgave him all his sins.", "tr": "Rahmet melekleri onu aldı ve Allah onun bütün günahlarını bağışladı."},
 "tokens": [ENC_MADI("فَأَخَذَتْهُ", "akhadha", "هُ", fem=True), FAIL("مَلَائِكَةُ", "malak", extra=["jam-taksir"], note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الرَّحْمَةِ", "rahma", punct="،"),
  MADI("وَغَفَرَ", "ghafara"), ALLAHU_F(), LAHU("لَهُ", "pron-3ms", "«ona»"), ENC_NOUN("ذُنُوبَهُ", "dhanb", "هُ", "maful", ["jam-taksir"]), KULLAHA(punct=".")]})
S4.append({"id": "s5", "translation": {"en": "Whoever repents to God with a sincere repentance, God accepts his repentance — even if his sins were like the mountains.", "tr": "Kim Allah'a samimi bir tövbeyle tövbe ederse, günahları dağlar gibi olsa bile Allah tövbesini kabul eder."},
 "tokens": [MAN_SHART("فَمَنْ"), SHART_V("تَابَ", "taba-repent", ["hollow-verbs"]), ILA(), ALLAH_J(), MUTLAQ("تَوْبَةً", "tawba"), NAAT("صَادِقَةً", "sadiq", "nasb", ["ism-fail"]),
  JAWAB_V("قَبِلَ", "qabila"), ALLAHU_F(), ENC_NOUN("تَوْبَتَهُ", "tawba", "هُ", "maful", punct="،"), WA_LAW(), KANA("كَانَتْ", fem=True), ENC_NOUN("ذُنُوبُهُ", "dhanb", "هُ", "ismk", ["jam-taksir"]),
  KHK("مِثْلَ", "mithl", extra=["idafa-definiteness"], note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْجِبَالِ", "jabal", extra=["jam-taksir"], punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf; five entries are new ------------------------------
PREF = ["qisas-al-nabiyyin-4", "al-kafiya", "adam-wa-iblis", "dhu-al-qarnayn-wa-al-sadd", "wasiyyat-abi-yusuf-l5", "izhar-al-asrar", "al-asad-wa-al-arnab",
        "luqman-wa-ibnuh", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "al-abras-wa-al-aqra-wa-al-ama", "ashab-al-ghar"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
# sadiq is صَادِق «truthful» on most of the shelf and صَدِيق «friend» in two texts — the story means the first, so it is pinned
FORCE = {"sadiq": "qisas-al-nabiyyin-4", "marra-once": "al-kafiya", "ikhtalafa": "qisas-al-nabiyyin-4", "ma-mawsula": "al-asad-wa-al-arnab", "la": "al-kafiya", "naam": "al-kafiya"}
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF}
def find_gloss(k):
    if FORCE.get(k) and k in _G[FORCE[k]]: return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    if FORCE.get(k) and k in _M[FORCE[k]]: return _M[FORCE[k]][k]
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

NEW_GLOSS = {
 "rahib": {"lemma": "رَاهِب", "root": "ر ه ب", "pos": "noun", "plural": "رُهْبَان", "gloss": {"en": "a monk (a Christian ascetic; pl. رُهْبَان)", "tr": "rahip, keşiş (ç. رُهْبَان)"}, "level": 3},
 "hakam": {"lemma": "حَكَم", "root": "ح ك م", "pos": "noun", "plural": "حُكَّام", "gloss": {"en": "an arbiter — a judge the two sides choose", "tr": "hakem — iki tarafın seçtiği yargıcı"}, "level": 3},
 "shibr": {"lemma": "شِبْر", "root": "ش ب ر", "pos": "noun", "plural": "أَشْبَار", "gloss": {"en": "a span — the width of a spread hand", "tr": "karış"}, "level": 3},
 "nisf": {"lemma": "نِصْف", "root": "ن ص ف", "pos": "noun", "plural": "أَنْصَاف", "gloss": {"en": "half", "tr": "yarı, yarım"}, "level": 3},
 "taib": {"lemma": "تَائِب", "root": "ت و ب", "pos": "noun", "plural": "تَائِبُونَ", "gloss": {"en": "repentant, one who repents (the active participle of تَابَ)", "tr": "tövbe eden, tâib (tâbe'nin ism-i fâili)"}, "level": 3},
}
NEW_VERBS = {}
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
    v = NEW_VERBS.get(k) or find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

LEVEL_NAME = json.loads((ROOT / "content/samples/qisas-al-nabiyyin-4/manifest.json").read_text(encoding="utf-8")).get("levelName", "Intermediate")
MANIFEST = {
 "id": "tawbat-al-qatil",
 "storyGroup": "tawbat-al-qatil",
 "title": {"ar": "تَوْبَةُ الْقَاتِلِ", "en": "The Killer's Repentance", "tr": "Katilin Tövbesi"},
 "subtitle": {"ar": "رَجُلٌ قَتَلَ مِائَةَ نَفْسٍ ثُمَّ طَلَبَ التَّوْبَةَ: الرَّاهِبُ، وَالْعَالِمُ، وَالْمَلَائِكَةُ تَخْتَلِفُ، وَالْأَرْضُ تَقْتَرِبُ — قِصَّةٌ لِلْمُسْتَوَى الثَّالِثِ",
              "en": "A man who killed a hundred people and then sought repentance: the monk, the learned man, the angels in dispute, and the land that drew near — a story for the third level",
              "tr": "Yüz kişi öldürüp sonra tövbe arayan bir adam: rahip, âlim, ihtilâfa düşen melekler ve yaklaşan yer — üçüncü seviye için bir hikâye"},
 "level": 3,
 "levelName": LEVEL_NAME,
 "version": "0.1.0",
 "published": "2026-11-08",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّالِثُ) لِخَبَرِ الرَّجُلِ الَّذِي قَتَلَ تِسْعَةً وَتِسْعِينَ نَفْسًا ثُمَّ تَابَ، الْمَرْوِيِّ فِي كُتُبِ الْحَدِيثِ (الْبُخَارِيُّ وَمُسْلِمٌ). النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ هِيَ نَصُّ حَدِيثٍ، فَلَا يُنْسَبُ شَيْءٌ مِنْهُ إِلَى الْحَدِيثِ.",
  "en": "ORIGINAL Level-3 graded Arabic: the narrative of the man who killed ninety-nine people and then repented, preserved in the hadith collections (al-Bukhari, Muslim), RETOLD FREELY in the wording of a graded reader. No sentence is the text of a hadith and none may be cited as one.",
  "tr": "ÖZGÜN 3. seviye kolaylaştırılmış Arapça: hadis kitaplarında (Buhârî, Müslim) nakledilen, doksan dokuz kişi öldürüp sonra tövbe eden adamın kıssası, kolaylaştırılmış okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir hadisin metni değildir ve hiçbiri hadis olarak nakledilemez.",
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
