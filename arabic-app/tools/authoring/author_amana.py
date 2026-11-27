"""Author content/samples/al-amana-wa-al-khashaba — «الْأَمَانَةُ وَالْخَشَبَةُ», the twenty-fourth ORIGINAL story and the fourth at Level 3 (wave 117).

ORIGINAL graded Arabic: a man borrows a thousand dinars with God alone as witness and guarantor, cannot find a ship when the
term falls due, hollows a log, seals the coins and a letter inside it and commits it to the sea; the lender finds the log on
the shore as firewood, and the borrower arrives later with a second thousand. The narrative is preserved in the ḥadīth
collections (al-Bukhārī) and is RETOLD FREELY here in a graded reader's wording: no sentence is the text of a ḥadīth and none
may be cited as one; no āya is quoted. Four chapters, twenty sentences. Written on the authoring kit (story_kit.py); six
entries are new — the nouns كَفِيل، خَشَبَة and the verbs أَقْرَضَ (IV), أَشْهَدَ (IV), نَقَرَ (I, bāb naṣara), اسْتَوْدَعَ (X), each with a
generated paradigm.  Regenerate with:
python3 tools/authoring/author_amana.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "al-amana-wa-al-khashaba"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
if not (ROOT / "tools/authoring/story_kit.py").exists(): sys.path.insert(0, "/tmp/claude-0/-home-user-Gallagher-s-Index-with-Python/612c64cf-e6b9-547d-9c53-f32b7b6377b6/scratchpad/w113")   # the kit before it lands (wave 113)
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

# ============ «الْأَمَانَةُ وَالْخَشَبَةُ» — the twenty-fourth ORIGINAL story, the fourth at Level 3 (wave 117) ============
PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "هِمَا": "pron-3d", "هُمَا": "pron-3d", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "هِمَا": "هُمَا", "هُمَا": "هُمَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})

MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_F = lambda full="فَقَالَ", punct=None, hidden=False: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, punct=punct, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
MUDAF_NOTE = ("، مُضَافٌ", ", annexed", ", muzâf")
LAFZ = (" — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl")
ALLAH_MUB = lambda: MUBTADA("اللهُ", "allah", "propn", note_ar=LAFZ[0], note_en=LAFZ[1], note_tr=LAFZ[2])
ALLAH_ISMK = lambda: ISMK("اللهُ", "allah", "propn", note_ar=LAFZ[0], note_en=LAFZ[1], note_tr=LAFZ[2])
KH_KANA_J = ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ", "; the jarr phrase is the predicate of كَانَ", "; câr-mecrûr kâne'nin haberidir")
SIFA_J = ("، وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِرَجُلٍ", "; the jarr phrase qualifies «a man»", "; câr-mecrûr «adam»ın sıfatıdır")
KH_MUQ_J = ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate", "; câr-mecrûr öne alınmış haberdir")
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
KH_LAALLA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَعَلَّ", "; the clause fills the seat of raf' as the predicate of لَعَلَّ", "; cümle lealle'nin haberi olarak mahallen merfû")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
JAWAB_QASAM = (" — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا", "; the clause is the answer of the oath and has no seat of its own", "; cümle kasemin cevabıdır, i'râbdan mahalli yoktur")
NAAT_CL_SAFINA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِسَفِينَةٍ", "; the clause qualifies «a ship» — in the seat of nasb as its na't", "; cümle «gemi»nin na'tı olarak mahallen mansûb")
HAL_FULL = (" — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the nominal clause fills the seat of nasb as a hal", "; isim cümlesi hâl olarak mahallen mansûb")

# --- the number أَلْف and its singular tamyīz in jarr --------------------------------------------------------------
ALF_MAF2 = lambda note=("", "", ""): tok("أَلْفَ", "alf", "noun", ["maful-bihi", "mafulayn", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
    "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالْمِائَةُ وَالْأَلْفُ يُضَافَانِ إِلَى مُفْرَدٍ مَجْرُورٍ" + note[0] + ".",
    "The second object, in nasb and annexed — a hundred and a thousand annex a SINGULAR in jarr" + note[1] + ".", "İkinci mef'ûlün bih, mansûb, muzâf — yüz ve bin, mecrûr bir müfrede muzâf olur" + note[2] + ".")
ALF_MAF = lambda: tok("أَلْفَ", "alf", "noun", ["maful-bihi", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
    "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — يُضَافُ إِلَى مُفْرَدٍ مَجْرُورٍ.", "The direct object, in nasb and annexed — a thousand annexes a singular in jarr.", "Mef'ûlün bih, mansûb, muzâf — bin, mecrûr bir müfrede muzâf olur.")
ALF_MUB = lambda: tok("أَلْفُ", "alf", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
    "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — يُضَافُ إِلَى مُفْرَدٍ مَجْرُورٍ.", "The mubtada, placed after its predicate, in raf' and annexed to a singular in jarr.", "Mübtedâ (haberinden sonra), merfû, muzâf — mecrûr bir müfrede muzâf.")
DINAR_MI = lambda punct=None: tok("دِينَارٍ", "dinar", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya", "tamyiz"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — تَمْيِيزُ الْأَلْفِ مُفْرَدٌ مَجْرُورٌ بِالْإِضَافَةِ.", "The second term of the idafa, in jarr — the specifier of «a thousand», a singular in jarr by the annexation.", "Muzâfun ileyh, mecrûr — «bin»in temyîzi, izâfetle mecrûr müfred.", punct=punct)
ALALF_MAF2 = lambda: tok("الْأَلْفَ", "alf", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَعْطَى يَنْصِبُ مَفْعُولَيْنِ.", "The second object of «he gave», in nasb — أَعْطَى takes two objects.", "«Verdi»nin ikinci mef'ûlü, mansûb — a'tâ iki mef'ûl alır.")

# --- the imperative of أَتَى with the guarding nūn, and the answer of the request in jazm --------------------------------
ITINI = lambda full="ائْتِنِي", punct=None: tok(full, "ata", "verb", ["imperative-amr", "naqis-verbs", "ya-al-mutakallim", "al-bariz-al-muttasil", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    (FA_AR if full.startswith("فَ") else "") + "فِعْلُ أَمْرٍ مِنْ أَتَى مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ (أَصْلُهُ ائْتِيْ)، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — ائْتِ بِكَذَا: جِئْ بِهِ.",
    ("The fa conjoins; " if full.startswith("فَ") else "") + "the imperative of أَتَى «come», built on the dropped weak letter; the doer «you» must stay hidden; the nun guards the verb and the speaker's ya is its object — «bring me».",
    ("Fâ atıf; " if full.startswith("فَ") else "") + "etâ'nın emri, illet harfinin hazfi üzere mebnî; fâil «sen» vücûben müstetir; nûn vikâye, mütekellim yâ'sı mef'ûlün bih — «bana getir».",
    punct=punct, segments=[s for s in [(seg("فَ", "fa", "conj") if full.startswith("فَ") else None), seg("ائْتِ", "ata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")] if s])
USHHIDHUM = lambda: tok("أُشْهِدْهُمْ", "ashhada", "verb", ["jawab-al-talab", "nawasib-wa-jawazim-al-mudari", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ لِأَنَّهُ جَوَابُ الطَّلَبِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَهُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — إِنْ تَأْتِنِي بِهِمْ أُشْهِدْهُمْ.",
    "A present verb in jazm as the ANSWER OF THE REQUEST («bring me witnesses [and] I will make them witness»), its sign the sukun; the doer «I» must stay hidden and the attached «them» is its object.",
    "Talebin cevabı olarak meczûm muzâri («bana şâhitler getir, onları şâhit tutayım»), alâmeti sükûn; fâil «ben» vücûben müstetir; bitişik «onlar» mef'ûlün bih.",
    segments=[seg("أُشْهِدْ", "ashhada", "verb"), seg("هُمْ", "pron-3mp", "pron")])
SHUHADA_J = lambda: BI_NOUN("بِشُهَدَاءَ", "shahid-witness", "شُهَدَاءَ", extra=["mamnu-min-sarf", "jam-taksir"], sign="بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ",
    note_ar=" — جَمْعُ شَهِيدٍ عَلَى فُعَلَاءَ", note_en=" — the plural of «witness» on فُعَلَاء, a diptote by its lengthened feminine alif, so the fatha stands for the kasra", note_tr=" — şehîd'in fuʿalâ' veznindeki cem'i; memdûd te'nîs elifi sebebiyle gayr-i munsarif, fetha kesrenin yerini tutar")

# --- the speaker's yāʾ on a ẓarf, and the khabar built on it -----------------------------------------------------------
BAYNI = lambda: tok("بَيْنِي", "bayna", "noun", ["maful-fih", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِشَهِيدٍ.",
    "An adverb of place «between», in nasb by a fatha estimated before the speaker's ya; annexed, the ya its second term — it attaches to «witness».", "Mekân zarfı «arasında», mütekellim yâ'sından önce takdîrî fetha ile mansûb; muzâf, yâ muzâfun ileyh — «şâhid»e müteallik.",
    segments=[seg("بَيْنِ", "bayna", "noun"), seg("ي", "pron-1s", "pron")])
WA_BAYNAKA = lambda punct=None: tok("وَبَيْنَكَ", "bayna", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "بَيْنَ ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — بَيْنَ تُكَرَّرُ مَعَ الضَّمِيرِ.",
    "The waw conjoins a second «between», in nasb and annexed to «you» — بَيْنَ is repeated before a pronoun.", "Vâv atıf; ikinci «arasında», mansûb, muzâf; kâf muzâfun ileyh — beyne zamirle tekrarlanır.",
    punct=punct, segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun"), seg("كَ", "pron-2ms", "pron")])
KAFILI = lambda punct=None: YA_MUTAKALLIM_N("كَفِيلِي", "kafil", "كَفِيل", "خَبَرٌ مَرْفُوعٌ", "The predicate, in raf'", "Haber, merfû", extra=["mubtada-khabar", "sifa-mushabbaha"], punct=punct)
SHAHID_KH = lambda: KHABAR("شَهِيدٌ", "shahid-witness", ["sifa-mushabbaha"], note_ar=" — صِيغَةُ مُبَالَغَةٍ عَلَى فَعِيلٍ بِمَعْنَى شَاهِدٍ", note_en=" — an intensive on فَعِيل with the sense of «one who witnesses»", note_tr=" — feʿîl vezninde mübâlağa sîgası, «şâhid» anlamında")

# --- the lām of purpose on a weak verb, with and without an enclitic -------------------------------------------------------
LIYUADDIYA = lambda: tok("لِيُؤَدِّيَ", "adda", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "form-ii-verbs", "naqis-verbs"],
    "اللَّامُ لِلتَّعْلِيلِ، وَيُؤَدِّيَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ جَوَازًا بَعْدَ لَامِ التَّعْلِيلِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ لِخِفَّتِهَا، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "The lam of purpose; «that he might render» is a present verb put in nasb by an أَنْ understood after the lam — its fatha SHOWS on the ya, which bears it lightly; the doer «he» is hidden.",
    "Ta'lîl lâmı; «ödemesi için» — lâmdan sonra gizli en ile mansûb muzâri; fetha hafif olduğu için yâ üzerinde zâhirdir; fâil gizli «o».",
    segments=[seg("لِ", "lam-taleel", "part"), seg("يُؤَدِّيَ", "adda", "verb")])
LIATIYAKA = lambda: tok("لِآتِيَكَ", "ata", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "اللَّامُ لِلتَّعْلِيلِ، وَآتِيَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — آتِيكَ بِهِ: أَجِيئُكَ بِهِ.",
    "The lam of purpose; «that I might come to you» is a present verb in nasb by a hidden أَنْ, its fatha showing on the ya; the doer «I» must stay hidden and the attached «you» is its object.",
    "Ta'lîl lâmı; «sana gelmem için» — gizli en ile mansûb muzâri, fethası yâ üzerinde zâhir; fâil «ben» vücûben müstetir; bitişik kâf mef'ûlün bih.",
    segments=[seg("لِ", "lam-taleel", "part"), seg("آتِيَ", "ata", "verb"), seg("كَ", "pron-2ms", "pron")])

# --- the oath, the question on لَمْ, the compound tense --------------------------------------------------------------------
WALLAHI = lambda: tok("وَاللهِ", "wa-qasam", "part", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "huruf-jarr"],
    "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِهَا — وَجَوَابُ الْقَسَمِ الْجُمْلَةُ بَعْدَهُ الْمُصَدَّرَةُ بِاللَّامِ وَقَدْ.",
    "The waw of oath and jarr, the Name of Majesty in jarr after it; the answer of the oath is the clause that follows, opened by the lam and قَدْ.", "Kasem ve cer vâvı, lafza-i celâl onunla mecrûr; kasemin cevabı, lâm ve kad ile başlayan sonraki cümledir.",
    segments=[seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")])
LAQAD = lambda: tok("لَقَدْ", "qad", "part", ["qad-harf", "al-qasam-wal-shart-fil-kafiya"],
    "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The lam opens the answer of the oath; قَدْ affirms the past verb.", "Lâm kasemin cevabına gelmiştir; kad tahkîk harfidir.")
FA_MA_NAFIYA = lambda: tok("فَمَا", "ma-nafiya", "part", ["la-nafiya"], FA_AR + "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; مَا negates and governs nothing.", "Fâ atıf; mâ nefiy harfi, amel etmez.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")])
ALAM = lambda: tok("أَلَمْ", "lam-jazima", "part", ["al-istifham", "nawasib-wa-jawazim-al-mudari", "lam-jazim"],
    "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The hamza asks a question that expects assent («did I not…?»); لَمْ negates, governs jazm and turns the tense to the past.", "Takrîrî istifhâm hemzesi; lem — nefiy, cezm ve kalb harfi.",
    segments=[seg("أَ", "a-istifham", "part"), seg("لَمْ", "lam-jazima", "part")])
UKHBIRKA = lambda: tok("أُخْبِرْكَ", "akhbara", "verb", ["nawasib-wa-jawazim-al-mudari", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "Present verb in jazm after لَمْ, its sign the sukun; the doer «I» must stay hidden and the attached «you» is its object.", "Lem ile meczûm muzâri, alâmeti sükûn; fâil «ben» vücûben müstetir; bitişik kâf mef'ûlün bih.",
    segments=[seg("أُخْبِرْ", "akhbara", "verb"), seg("كَ", "pron-2ms", "pron")])
ANNI = lambda role=("", "", ""): tok("أَنِّي", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna", "al-bariz-al-muttasil", "ya-al-mutakallim"],
    "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا" + role[0] + ".",
    "أَنَّ «that» is the verb-like particle that builds a masdar; the speaker's ya is its noun in the seat of nasb" + role[1] + ".", "Enne — te'kîd, nasb ve masdar harfi; mütekellim yâ'sı ismi, mahallen mansûb" + role[2] + ".",
    segments=[seg("أَنَّ", "anna", "part"), seg("ي", "pron-1s", "pron")])
KUNTA_K = lambda: tok("كُنْتَ", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ (حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ)، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.",
    "كَانَ built on sukun before the ta of the doer (its middle letter dropped where two quiescents met); the ta «you» is its noun, in the seat of raf'.", "Kâne, fâil tâ'sı bitiştiği için sükûn üzere mebnî (iki sâkin karşılaşınca aynı düştü); tâ «sen» ismi, mahallen merfû.")
ILAYYA = lambda punct=None: tok("إِلَيَّ", "ila", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"],
    "حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَقُلِبَتْ أَلِفُ إِلَى يَاءً وَأُدْغِمَتْ فِي يَاءِ الْمُتَكَلِّمِ.",
    "A jarr letter; the speaker's ya fills the seat of jarr — the alif of إِلَى turns to ya and merges with the pronoun's ya.", "Cer harfi; mütekellim yâ'sı mahallen mecrûr — ilâ'nın elifi yâ'ya dönüp zamirin yâ'sına idgâm edildi.", punct=punct, segments=[seg("إِلَى", "ila", "prep"), seg("يَ", "pron-1s", "pron")])

# --- لَعَلَّ, إِذَا of surprise with the extra bāʾ, the vocative اللّٰهُمَّ ---------------------------------------------------
LAALLA = lambda: tok("لَعَلَّ", "laalla", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"],
    "حَرْفُ تَرَجٍّ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "لَعَلَّ «perhaps» is the sister of إِنَّ that hopes: its noun in nasb, its predicate in raf'.", "Lealle — inne'nin kardeşlerinden terecci harfi: ismini nasb, haberini ref eder.")
SAFINA_ISM_LAALLA = lambda: tok("سَفِينَةً", "safina", "noun", ["inna-wa-akhawatuha"], "اسْمُ لَعَلَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of لَعَلَّ, in nasb.", "Lealle'nin ismi, mansûb.")
FA_IDHA_FUJA = lambda: tok("فَإِذَا", "idha", "part", ["huruf-al-shart-fil-kafiya", "al-kinayat-wal-zuruf-al-mabniyya"],
    FA_AR + "إِذَا لِلْمُفَاجَأَةِ، حَرْفٌ عِنْدَ قَوْمٍ وَظَرْفُ مَكَانٍ عِنْدَ آخَرِينَ، وَلَا تَدْخُلُ إِلَّا عَلَى الْجُمْلَةِ الِاسْمِيَّةِ.",
    "The fa conjoins; this إِذَا is the إِذَا OF SURPRISE («and there was…»): a particle for some, an adverb of place for others, and it opens only a nominal clause.", "Fâ atıf; bu izâ, müfâcee izâ'sıdır («bir de ne görsün»): kimine göre harf, kimine göre mekân zarfı; yalnız isim cümlesine girer.",
    segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")])
BIL_KHASHABA_MUB = lambda: tok("بِالْخَشَبَةِ", "khashaba", "noun", ["huruf-jarr", "huruf-al-ziyada-fil-kafiya", "mubtada-khabar", "hadhf-wa-taqdir", "mahall-al-majrur"],
    "الْبَاءُ زَائِدَةٌ، وَالْخَشَبَةُ مُبْتَدَأٌ مَجْرُورٌ لَفْظًا بِالْبَاءِ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا، وَخَبَرُهُ مَحْذُوفٌ تَقْدِيرُهُ: حَاضِرَةٌ أَمَامَهُ.",
    "The ba is EXTRA: «the log» is the mubtada, in jarr in form after the extra ba and in raf' by seat; its predicate is omitted («[was there] before him»).", "Bâ zâiddir: «odun» mübtedâ, zâid bâ ile lafzen mecrûr, mahallen merfû; haberi hazfedilmiş («önünde [duruyordu]»).",
    segments=[seg("بِ", "bi", "prep"), seg("الْخَشَبَةِ", "khashaba", "noun")])
ALLATI_NAAT_KH = lambda: tok("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa", "mahall-al-majrur"],
    "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ نَعْتٌ لِلْخَشَبَةِ، فِي مَحَلِّ جَرٍّ عَلَى اللَّفْظِ أَوْ رَفْعٍ عَلَى الْمَحَلِّ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
    "The feminine relative, built on sukun, the adjective of «the log» — in the seat of jarr by its form or of raf' by its seat; the clause after it is its clause.", "Müennes ism-i mevsûl, sükûn üzere mebnî, «odun»un na'tı — lafza göre mahallen mecrûr, mahalle göre merfû; sonraki cümle sılasıdır.")
ALLAHUMMA = lambda punct=None: tok("اللّٰهُمَّ", "allahumma", "propn", ["vocative-munada", "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"],
    "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَالْمِيمُ الْمُشَدَّدَةُ عِوَضٌ عَنْ يَاءِ النِّدَاءِ الْمَحْذُوفَةِ.",
    "The called name «O God», built on damma in the seat of nasb; the doubled mim stands in for the dropped vocative يَا.", "Münâdâ, alem, damme üzere mebnî, mahallen mansûb; şeddeli mîm, hazfedilen nidâ yâ'sından bedeldir.", punct=punct)
WA_MAAHU_KH = lambda: tok("وَمَعَهُ", "maa", "noun", ["al-hal-jumla-wa-rabituha", "maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar"],
    "الْوَاوُ حَالِيَّةٌ، وَمَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens a hal clause; «with him» is an adverb of place annexed to the pronoun — the FRONTED predicate, and the clause is a hal in the seat of nasb.", "Hâl vâvı; «yanında» mansûb mekân zarfı, zamire muzâf — öne alınmış haber; cümle hâl olarak mahallen mansûb.",
    segments=[seg("وَ", "wa", "conj"), seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")])
ALLADHI_NAAT_RAF = lambda: tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"],
    "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلرَّجُلِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.", "A relative pronoun built on sukun in the seat of raf' as the adjective of «the man»; the clause after it is its clause.", "İsm-i mevsûl, sükûn üzere mebnî, «adam»ın na'tı olarak mahallen merfû; sonraki cümle sılasıdır.")
MA_MAF = lambda: tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
    "A relative pronoun built on sukun, the object in the seat of nasb; the clause after it is its clause.", "İsm-i mevsûl, sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb; sonraki cümle sılasıdır.")
SAALANI = lambda: tok("وَسَأَلَنِي", "saala", "verb", ["al-bariz-al-muttasil", "maful-bihi", "mafulayn", "ya-al-mutakallim"],
    WA_AR + "سَأَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
    "The waw conjoins; past verb built on fatha, the doer «he» hidden; the nun guards it and the speaker's ya is its FIRST object.", "Vâv atıf; fetha üzere mebnî mâzî, fâil gizli «o»; nûn vikâye, mütekellim yâ'sı birinci mef'ûlün bih.",
    segments=[seg("وَ", "wa", "conj"), seg("سَأَلَ", "saala", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
KAFILAN_MAF2 = lambda punct=None: tok("كَفِيلًا", "kafil", "noun", ["maful-bihi", "mafulayn", "sifa-mushabbaha"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — سَأَلَ يَنْصِبُ مَفْعُولَيْنِ.", "The second object, in nasb — «to ask someone for something» takes two objects.", "İkinci mef'ûlün bih, mansûb — se'ele iki mef'ûl alır.", punct=punct)
HADHIHI_MAF2 = lambda: ISHARA("هٰذِهِ", "hadhihi", "نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ", "nasb as the second object", "mansûb — ikinci mef'ûl", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre", extra=["mafulayn"])
HADHIHI_MI = lambda punct=None: ISHARA("هٰذِهِ", "hadhihi", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre", extra=["idafa-definiteness"], punct=punct)
FA_KANAT = lambda: tok("فَكَانَتِ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    FA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    "The fa conjoins; كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb; the ta marks the feminine and is voweled with kasra before the following ال.",
    "Fâ atıf; nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.", segments=[seg("فَ", "fa", "conj"), seg("كَانَتِ", "kana", "verb")])
KHAYR_KHK_MUDAF = lambda full="خَيْرَ": tok(full, "khayr", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"] + (["atf-nasaq"] if full.startswith("وَ") else []),
    (WA_AR if full.startswith("وَ") else "") + ("خَيْرَ مَعْطُوفٌ عَلَى خَبَرِ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ" if full.startswith("وَ") else "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ") + "، مُضَافٌ — خَيْرٌ اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ (أَصْلُهُ أَخْيَرُ).",
    ("The waw conjoins; a second predicate of كَانَ, in nasb" if full.startswith("وَ") else "The predicate of كَانَ, in nasb") + " and annexed — خَيْر is an elative whose hamza is dropped (from أَخْيَر).",
    ("Vâv atıf; kâne'nin ikinci haberi, mansûb" if full.startswith("وَ") else "Kâne'nin haberi, mansûb") + ", muzâf — hayr, hemzesi düşmüş ism-i tafdîldir (aslı ahyer).",
    segments=[seg("وَ", "wa", "conj"), seg("خَيْرَ", "khayr", "noun")] if full.startswith("وَ") else None)
BANI_J = lambda: tok("بَنِي", "banu", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "idafa-definiteness"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ" + SIFA_J[0] + ".",
    "In jarr by the ya — a plural attached to the sound masculine plural in its declension, its nun dropped for the annexation; annexed" + SIFA_J[1] + ".", "Yâ ile mecrûr — cem-i müzekker sâlime mülhak, nûnu izâfet için düşmüş; muzâf" + SIFA_J[2] + ".")

TITLES = [{"ar": "الْقَرْضُ", "en": "The loan", "tr": "Borç"},
          {"ar": "الْبَحْرُ", "en": "The sea", "tr": "Deniz"},
          {"ar": "الْخَشَبَةُ تَصِلُ", "en": "The log arrives", "tr": "Odun kıyıya varır"},
          {"ar": "الْأَمَانَةُ", "en": "The trust", "tr": "Emanet"}]

# ---- Chapter 1 — الْقَرْضُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "A man of the Children of Israel was in need of money, so he asked another man to lend him a thousand dinars.", "tr": "İsrailoğulları'ndan bir adam paraya muhtaçtı; başka bir adamdan kendisine bin dinar borç vermesini istedi."},
 "tokens": [KANA("كَانَ"), ISMK("رَجُلٌ", "rajul"), MIN(), BANI_J(), ISRAIL_MI(), PREP("فِي", "fi", *KH_KANA_J, gloss_tr="«-de»"), MAJR("حَاجَةٍ", "haja"), ILA(), MAJR("الْمَالِ", "mal", punct="،"),
  MADI("فَسَأَلَ", "saala", ["mafulayn"], hidden=True), MAFUL("رَجُلًا", "rajul", note_ar=" أَوَّلُ", note_en=" — the first of two", note_tr=" — iki mef'ûlün birincisi"), AKHAR_NAAT("آخَرَ", "nasb"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ ثَانٍ لِسَأَلَ", "; the clause it builds is the second object of «asked»", "; kurduğu müevvel masdar se'ele'nin ikinci mef'ûlüdür"),
  MANSUB_AN("يُقْرِضَهُ", "aqrada", ["form-iv-verbs", "mafulayn"], enc="هُ", note_ar=" أَوَّلُ", note_en=" — the first of two", note_tr=" — iki mef'ûlün birincisi"), ALF_MAF2(), DINAR_MI(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "He said to him: «Bring me witnesses, and I will have them witness against you.»", "tr": "Ona dedi: «Bana şâhitler getir, onları senin aleyhine şâhit tutayım.»"},
 "tokens": [QALA_F("فَقَالَ", hidden=True), LAHU("لَهُ", "pron-3ms", "«ona»", punct=":"), ITINI(), SHUHADA_J(), USHHIDHUM(), JARR_PRON("عَلَيْكَ", "ala", "عَلَيْ", "كَ", " («senin aleyhine»)", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "He said: «God is witness between me and you.»", "tr": "Dedi: «Benimle senin aranda Allah şâhittir.»"},
 "tokens": [QALA_F("فَقَالَ", punct=":", hidden=True), ALLAH_MUB(), SHAHID_KH(), BAYNI(), WA_BAYNAKA(punct=".")]})
S1.append({"id": "s4", "translation": {"en": "He said: «Then bring me a guarantor.» He said: «God is my guarantor.»", "tr": "Dedi: «Öyleyse bana bir kefil getir.» Dedi: «Kefilim Allah'tır.»"},
 "tokens": [QALA_F("قَالَ", punct=":", hidden=True), ITINI("فَأْتِنِي"), BI_NOUN("بِكَفِيلٍ", "kafil", "كَفِيلٍ", punct="."), QALA_F("قَالَ", punct=":", hidden=True), ALLAH_MUB(), KAFILI(punct=".")]})
S1.append({"id": "s5", "translation": {"en": "He said: «You have spoken the truth» — and he gave him the thousand until an appointed term.", "tr": "Dedi: «Doğru söyledin» ve ona bin dinarı belli bir vadeye kadar verdi."},
 "tokens": [QALA_F("قَالَ", punct=":", hidden=True), MADI_T("صَدَقْتَ", "sadaqa-be-true", who="anta", punct="،"), ENC_MADI("فَأَعْطَاهُ", "aata", "هُ", ["form-iv-verbs", "mafulayn"], alif=True, hidden=True, note_ar=" أَوَّلُ", note_en=" — the first of two", note_tr=" — iki mef'ûlün birincisi"),
  ALALF_MAF2(), ILA(), MAJR("أَجَلٍ", "ajal"), NAAT("مَعْلُومٍ", "malum", "jarr", ["ism-maful"], punct=".")]})

# ---- Chapter 2 — الْبَحْرُ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "The man went out to sea for his trade; when he had finished his business he looked for a ship to return in, so as to pay the debt at its term.", "tr": "Adam ticareti için denize açıldı; işini bitirince, borcu vadesinde ödemek üzere dönebileceği bir gemi aradı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja"), FAIL("الرَّجُلُ", "rajul"), FI(), MAJR("الْبَحْرِ", "bahr"), LI_ENC("لِتِجَارَتِهِ", "tijara", "تِجَارَتِ", "هِ", punct="،"), LAMMA2("فَلَمَّا"),
  MADI_ALIF("قَضَى", "qada-verb", hidden=True, note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), ENC_NOUN("حَاجَتَهُ", "haja", "هُ", "maful"),
  MADI("طَلَبَ", "talaba", hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]), MAFUL("سَفِينَةً", "safina"),
  MUDARI("يَرْجِعُ", "rajaa", note_ar=NAAT_CL_SAFINA[0], note_en=NAAT_CL_SAFINA[1], note_tr=NAAT_CL_SAFINA[2]), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onunla»)", punct="،"),
  LIYUADDIYA(), MAFUL("الدَّيْنَ", "dayn"), FI(), ENC_NOUN("أَجَلِهِ", "ajal", "هِ", "majr", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "He found no ship; so he took a log and hollowed it out, and put inside it a thousand dinars and a letter to his companion.", "tr": "Gemi bulamadı; bir odun aldı, içini oydu ve içine bin dinar ile arkadaşına bir mektup koydu."},
 "tokens": [LAM_JAZM("فَلَمْ"), JAZM_V("يَجِدْ", "wajada", ["mithal-verbs"], hidden="هُوَ", note_ar=" — وَحُذِفَتْ وَاوُ وَجَدَ فِي مُضَارِعِهِ لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ", note_en=" — the waw of وَجَدَ drops in the present, caught between a ya and a kasra", note_tr=" — vecede'nin vâvı muzâride yâ ile kesre arasında kaldığı için düşer"),
  MAFUL("سَفِينَةً", "safina", punct="،"), MADI("فَأَخَذَ", "akhadha", hidden=True), MAFUL("خَشَبَةً", "khashaba"), ENC_MADI("فَنَقَرَهَا", "naqara", "هَا", hidden=True, punct="،"),
  MADI("وَجَعَلَ", "jaala", hidden=True), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içine»)"), ALF_MAF(), DINAR_MI(), ATF("وَكِتَابًا", "kitab", "noun", "nasb", note_ar=" — كِتَابٌ هُنَا: رِسَالَةٌ", note_en=" — a letter", note_tr=" — burada kitâb: mektup"),
  ILA(), ENC_NOUN("صَاحِبِهِ", "sahib", "هِ", "majr", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "Then he brought it to the sea and said: «O God, You know that I took a thousand dinars from so-and-so.»", "tr": "Sonra onu denize getirdi ve dedi: «Allah'ım, biliyorsun ki ben falancadan bin dinar aldım.»"},
 "tokens": [THUMMA(), MADI_ALIF("أَتَى", "ata", hidden=True), JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onu»)", note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ: أَتَى بِهَا أَيْ جَاءَ بِهَا", note_en=" — this ba makes the verb transitive («brought it»)", note_tr=" — bu bâ ta'diye içindir («onu getirdi»)"),
  ILA(), MAJR("الْبَحْرِ", "bahr"), QALA("وَقَالَ", hidden=True, punct=":"), ALLAHUMMA(punct="،"), INNA_ENC("إِنَّكَ", "كَ", " («sen»)"),
  MUDARI("تَعْلَمُ", "alima", ["mafulayn"], who="أَنْتَ", note_ar=KH_INNA[0], note_en=KH_INNA[1], note_tr=KH_INNA[2]),
  ANNI((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ تَعْلَمُ", "; the clause it builds stands for both objects of «you know»", "; kurduğu müevvel masdar ta'lemu'nun iki mef'ûlünün yerini tutar")),
  MADI_T("أَخَذْتُ", "akhadha", who="ana", note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]), MIN(), MAJR("فُلَانٍ", "fulan"), ALF_MAF(), DINAR_MI(punct=".")]})
S2.append({"id": "s4", "translation": {"en": "«He asked me for a guarantor, and I said: God is my guarantor — and he was content with You.»", "tr": "«Benden kefil istedi; ben de dedim ki: Kefilim Allah'tır — o da Sana râzı oldu.»"},
 "tokens": [SAALANI(), KAFILAN_MAF2(punct="،"), MADI_T("فَقُلْتُ", "qala", who="ana", extra=["hollow-verbs", "maful-bihi"], punct=":", note_ar="، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ" + MAQUL[0], note_en=" (its middle letter dropped where two quiescents met)" + MAQUL[1], note_tr=" (iki sâkin karşılaşınca aynı düştü)" + MAQUL[2]),
  ALLAH_MUB(), KAFILI(punct="،"), MADI("فَرَضِيَ", "radiya", ["naqis-verbs"], hidden=True), JARR_PRON("بِكَ", "bi", "بِ", "كَ", " («sana»)", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "«I sought a ship and found none; and I entrust this log to You.»", "tr": "«Gemi aradım, bulamadım; bu odunu Sana emanet ediyorum.»"},
 "tokens": [INNA_ENC("وَإِنِّي", "ي", " («ben»)"), MADI_T("طَلَبْتُ", "talaba", who="ana", note_ar=KH_INNA[0], note_en=KH_INNA[1], note_tr=KH_INNA[2]), MAFUL("سَفِينَةً", "safina"), LAM_JAZM("فَلَمْ"),
  JAZM_V("أَجِدْ", "wajada", ["mithal-verbs"], hidden="أَنَا", punct="،", note_ar=" — وَالْمَفْعُولُ مَحْذُوفٌ: فَلَمْ أَجِدْهَا", note_en=" — its object is omitted («I found none»)", note_tr=" — mef'ûlü hazfedilmiş («bulamadım»)"),
  INNA_ENC("وَإِنِّي", "ي", " («ben»)"), MUDARI("أَسْتَوْدِعُكَ", "istawdaa", ["form-x-verbs", "mafulayn", "mithal-verbs"], who="أَنَا", enc="كَ", wujub=True, note_ar=" أَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", note_en=" — the first of two; the clause is the predicate of إِنَّ", note_tr=" — iki mef'ûlün birincisi; cümle inne'nin haberi"),
  HADHIHI_MAF2(), BADAL("الْخَشَبَةَ", "khashaba", "nasb", punct=".")]})
S2.append({"id": "s6", "translation": {"en": "Then he threw it into the sea, and went back while still seeking a ship to his town.", "tr": "Sonra onu denize attı ve memleketine gidecek bir gemi arayarak geri döndü."},
 "tokens": [THUMMA(), MADI_ALIF("رَمَى", "rama", hidden=True), JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onu»)"), FI(), MAJR("الْبَحْرِ", "bahr", punct="،"), MADI("وَرَجَعَ", "rajaa", hidden=True), WA_HUWA_HAL(),
  MUDARI("يَطْلُبُ", "talaba", note_ar=KH_CL[0] + HAL_FULL[0], note_en=KH_CL[1] + HAL_FULL[1], note_tr=KH_CL[2] + HAL_FULL[2]), MAFUL("سَفِينَةً", "safina"), ILA(), ENC_NOUN("بَلَدِهِ", "balad", "هِ", "majr", punct=".")]})

# ---- Chapter 3 — الْخَشَبَةُ تَصِلُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "The owner of the money went out to the shore, looking: perhaps a ship had come with his money.", "tr": "Paranın sahibi kıyıya çıkıp bakıyordu: belki bir gemi parasıyla gelmiştir diye."},
 "tokens": [MADI("وَخَرَجَ", "kharaja"), FAIL("صَاحِبُ", "sahib", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْمَالِ", "mal"), ILA(), MAJR("السَّاحِلِ", "sahil"),
  MUDARI("يَنْظُرُ", "nazara", note_ar=HAL_CL[0], note_en=HAL_CL[1], note_tr=HAL_CL[2], punct=":"), LAALLA(), SAFINA_ISM_LAALLA(), QAD(),
  MADI("جَاءَتْ", "jaa", ["hollow-verbs"], fem=True, hidden=True, note_ar=KH_LAALLA[0], note_en=KH_LAALLA[1], note_tr=KH_LAALLA[2]), BI_NOUN("بِمَالِهِ", "mal", "مَالِهِ", enc="هِ", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "And there was the log with the money inside it; he took it home to his family as firewood.", "tr": "Bir de ne görsün: içinde para olan odun! Onu ailesine odun diye aldı."},
 "tokens": [FA_IDHA_FUJA(), BIL_KHASHABA_MUB(), ALLATI_NAAT_KH(), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içinde»)", note_ar=KH_MUQ_J[0], note_en=KH_MUQ_J[1], note_tr=KH_MUQ_J[2]),
  MUBTADA("الْمَالُ", "mal", note_ar=" مُؤَخَّرٌ" + SILA[0], note_en=" (placed after its predicate)" + SILA[1], note_tr=" (haberinden sonra)" + SILA[2], punct="،"), ENC_MADI("فَأَخَذَهَا", "akhadha", "هَا", hidden=True), LI_ENC("لِأَهْلِهِ", "ahl", "أَهْلِ", "هِ"),
  HAL("حَطَبًا", "hatab", punct=".", note_ar=" — جَامِدٌ مُؤَوَّلٌ بِالْمُشْتَقِّ: مُتَّخَذَةً حَطَبًا", note_en=" — a plain noun read as a derived one («taken as firewood»)", note_tr=" — câmid isim, müştak ile te'vîl edilir («odun olarak»)")]})
S3.append({"id": "s3", "translation": {"en": "When he broke it open, he found the money and the letter inside it.", "tr": "Onu kırınca içinde parayı ve mektubu buldu."},
 "tokens": [LAMMA2("فَلَمَّا"), ENC_MADI("كَسَرَهَا", "kasara", "هَا", hidden=True, note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]),
  MADI("وَجَدَ", "wajada", ["mithal-verbs"], hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içinde»)"), MAFUL("الْمَالَ", "mal"), ATF("وَالْكِتَابَ", "kitab", "noun", "nasb", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "Then the man who had taken the loan arrived, and with him another thousand dinars.", "tr": "Sonra borcu alan adam geldi; yanında bir bin dinar daha vardı."},
 "tokens": [THUMMA(), MADI("قَدِمَ", "qadima"), FAIL("الرَّجُلُ", "rajul"), ALLADHI_NAAT_RAF(), MADI("أَخَذَ", "akhadha", hidden=True, note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]), MAFUL("الدَّيْنَ", "dayn", punct="،"),
  WA_MAAHU_KH(), ALF_MUB(), DINAR_MI(), AKHAR_NAAT("آخَرُ", "raf", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "He said: «By God, I kept seeking a ship to bring you your money, and I found none before this one.»", "tr": "Dedi: «Vallahi, sana paranı getirmek için gemi aradım durdum; bundan önce hiçbir gemi bulamadım.»"},
 "tokens": [QALA_F("فَقَالَ", punct=":", hidden=True), WALLAHI(), LAQAD(), MADI_T("طَلَبْتُ", "talaba", who="ana", note_ar=JAWAB_QASAM[0], note_en=JAWAB_QASAM[1], note_tr=JAWAB_QASAM[2]), MAFUL("سَفِينَةً", "safina"),
  LIATIYAKA(), BI_NOUN("بِمَالِكَ", "mal", "مَالِكَ", enc="كَ", punct="،"), FA_MA_NAFIYA(), MADI_T("وَجَدْتُ", "wajada", who="ana", extra=["mithal-verbs"]), MAFUL("سَفِينَةً", "safina"),
  ZARF("قَبْلَ", "qabla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), HADHIHI_MI(punct=".")]})

# ---- Chapter 4 — الْأَمَانَةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "The owner of the money said: «Had you sent me anything?»", "tr": "Paranın sahibi dedi: «Bana bir şey göndermiş miydin?»"},
 "tokens": [QALA_F("فَقَالَ"), FAIL("صَاحِبُ", "sahib", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْمَالِ", "mal", punct=":"),
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "هَلْ حَرْفُ اسْتِفْهَامٍ لِطَلَبِ التَّصْدِيقِ.", "هَلْ asks a yes-or-no question.", "Hel — tasdik isteyen istifhâm harfi."),
  KUNTA_K(), MADI_T("أَرْسَلْتَ", "arsala", who="anta", extra=["form-iv-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ كَانَ مَعَ الْمَاضِي تُفِيدُ الْمَاضِيَ الْبَعِيدَ", note_en="; the clause is the predicate of كَانَ — كَانَ before a past verb gives the pluperfect («had you sent»)", note_tr="; cümle kâne'nin haberi — kâne mâzîden önce uzak geçmişi bildirir («göndermiş miydin»)"),
  ILAYYA(), BI_NOUN("بِشَيْءٍ", "shay", "شَيْءٍ", punct="؟")]})
S4.append({"id": "s2", "translation": {"en": "He said: «Did I not tell you that I found no ship before this one?»", "tr": "Dedi: «Bundan önce gemi bulamadığımı sana söylemedim mi?»"},
 "tokens": [QALA_F("قَالَ", punct=":", hidden=True), ALAM(), UKHBIRKA(), ANNI((" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَنْصُوبٌ بِنَزْعِ الْخَافِضِ: أُخْبِرْكَ بِأَنِّي", "; the clause it builds stands after the dropped preposition («tell you [of] my finding none»)", "; kurduğu müevvel masdar hâfızın nez'iyle mansûb («bulamadığımı sana haber vermek»)")),
  LAM_JAZM(), JAZM_V("أَجِدْ", "wajada", ["mithal-verbs"], hidden="أَنَا", note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]), MAFUL("سَفِينَةً", "safina"),
  ZARF("قَبْلَ", "qabla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), HADHIHI_MI(punct="؟")]})
S4.append({"id": "s3", "translation": {"en": "He said: «God has delivered on your behalf what you sent in the log; so take your money and go back with it.»", "tr": "Dedi: «Odunun içinde gönderdiğini Allah senin adına ödedi; paranı al ve onunla dön.»"},
 "tokens": [QALA_F("قَالَ", punct=":", hidden=True), INNA(), ALLAH_ISMI(), QAD(), MADI_ALIF("أَدَّى", "adda", ["form-ii-verbs"], hidden=True, note_ar=KH_INNA[0], note_en=KH_INNA[1], note_tr=KH_INNA[2]),
  JARR_PRON("عَنْكَ", "an", "عَنْ", "كَ", " («senin adına»)"), MA_MAF(), MADI_T("بَعَثْتَ", "baatha", who="anta", note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]), BIHI(), FI(), MAJR("الْخَشَبَةِ", "khashaba", punct="،"),
  AMR("فَخُذْ", "akhadha", note_ar=" — وَحُذِفَتْ هَمْزَةُ أَخَذَ فِي أَمْرِهِ", note_en=" — the hamza of أَخَذَ is dropped in its imperative", note_tr=" — ehaze'nin hemzesi emrinde düşer"), ENC_NOUN("مَالَكَ", "mal", "كَ", "maful"),
  AMR("وَارْجِعْ", "rajaa"), BIHI(punct=".")]})
S4.append({"id": "s4", "translation": {"en": "So the trust was good for them both, and God was the best guarantor and the best witness.", "tr": "Böylece emanet ikisi için de hayırlı oldu; Allah en hayırlı kefil ve en hayırlı şâhit idi."},
 "tokens": [FA_KANAT(), ISMK("الْأَمَانَةُ", "amana-trust"), KHK("خَيْرًا", "khayr", extra=["ism-tafdil"], note_ar=" — اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ", note_en=" — an elative whose hamza is dropped", note_tr=" — hemzesi düşmüş ism-i tafdîl"), LAHU("لَهُمَا", "pron-3d", "«o ikisi için»", punct="،"),
  KANA("وَكَانَ"), ALLAH_ISMK(), KHAYR_KHK_MUDAF("خَيْرَ"), MUDAF_ILAYH("كَفِيلٍ", "kafil", extra=["sifa-mushabbaha"]), KHAYR_KHK_MUDAF("وَخَيْرَ"), MUDAF_ILAYH("شَهِيدٍ", "shahid-witness", extra=["sifa-mushabbaha"], punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf; six entries are new ---------------------------------
PREF = ["qisas-al-nabiyyin-4", "al-kafiya", "adam-wa-iblis", "dhu-al-qarnayn-wa-al-sadd", "wasiyyat-abi-yusuf-l5", "izhar-al-asrar", "al-asad-wa-al-arnab",
        "luqman-wa-ibnuh", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
FORCE = {"ma-mawsula": "al-asad-wa-al-arnab", "lam-taleel": "al-kafiya", "nun-wiqaya": "al-asad-wa-al-arnab", "shahid-witness": "al-kafiya", "qada-verb": "aqaid-ahl-al-sunna", "sadaqa-be-true": "al-kafiya"}
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
 "kafil": {"lemma": "كَفِيل", "root": "ك ف ل", "pos": "noun", "plural": "كُفَلَاء", "gloss": {"en": "a guarantor, a surety (ṣifa mushabbaha on فَعِيل)", "tr": "kefil (feʿîl vezninde sıfat-ı müşebbehe)"}, "level": 3},
 "khashaba": {"lemma": "خَشَبَة", "root": "خ ش ب", "pos": "noun", "plural": "خَشَبَات", "gloss": {"en": "a piece of wood, a log (the unit noun of خَشَب)", "tr": "bir parça odun, kütük (haşeb'in ism-i vahdeti)"}, "level": 3},
 "aqrada": {"lemma": "أَقْرَضَ", "root": "ق ر ض", "pos": "verb", "gloss": {"en": "to lend (Form IV; two objects: أَقْرَضَهُ مَالًا)", "tr": "borç vermek (if'âl; iki mef'ûl alır)"}, "level": 3},
 "ashhada": {"lemma": "أَشْهَدَ", "root": "ش ه د", "pos": "verb", "gloss": {"en": "to call to witness, to have someone witness (Form IV)", "tr": "şâhit tutmak (if'âl)"}, "level": 3},
 "naqara": {"lemma": "نَقَرَ", "root": "ن ق ر", "pos": "verb", "gloss": {"en": "to hollow out, to bore into (bāb naṣara)", "tr": "oymak, delmek (nasara bâbı)"}, "level": 3},
 "istawdaa": {"lemma": "اِسْتَوْدَعَ", "root": "و د ع", "pos": "verb", "gloss": {"en": "to entrust something to someone's keeping (Form X; two objects)", "tr": "emanet etmek, emanet bırakmak (istif'âl; iki mef'ûl alır)"}, "level": 3},
}
NEW_VERBS = {
 "aqrada": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْرَض", "قْرِض", "أَقْرِض", "إِقْرَاض", "مُقْرِض", "مُقْرَض", "أُقْرِضَ", "يُقْرَضُ", "أَقْرَضَهُ الْمَالَ يُقْرِضُهُ إِقْرَاضًا: أَعْطَاهُ إِيَّاهُ قَرْضًا يَرُدُّ مِثْلَهُ."),
 "ashhada": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَشْهَد", "شْهِد", "أَشْهِد", "إِشْهَاد", "مُشْهِد", "مُشْهَد", "أُشْهِدَ", "يُشْهَدُ", "أَشْهَدَهُ عَلَى الْأَمْرِ يُشْهِدُهُ إِشْهَادًا: جَعَلَهُ شَاهِدًا عَلَيْهِ."),
 "naqara": _sg.sound1("nasara", "نَقَر", "نْقُر", "اُنْقُر", "نَقْر", "نَاقِر", maful="مَنْقُور", pmz="نُقِرَ", pmd="يُنْقَرُ", note="نَقَرَ الْخَشَبَةَ يَنْقُرُهَا نَقْرًا مِنْ بَابِ نَصَرَ: حَفَرَهَا وَجَوَّفَهَا."),
 "istawdaa": _sg.derived(_sg.B10, "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ", "اِسْتَوْدَع", "سْتَوْدِع", "اِسْتَوْدِع", "اِسْتِيدَاع", "مُسْتَوْدِع", maful="مُسْتَوْدَع", pmz="اُسْتُودِعَ", pmd="يُسْتَوْدَعُ",
                          note="اسْتَوْدَعَهُ الشَّيْءَ يَسْتَوْدِعُهُ اسْتِيدَاعًا: جَعَلَهُ عِنْدَهُ وَدِيعَةً يَحْفَظُهَا؛ مِثَالٌ وَاوِيٌّ، وَوَاوُهُ تَثْبُتُ لِسُكُونِهَا بَعْدَ فَتْحَةِ التَّاءِ."),
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
    v = NEW_VERBS.get(k) or find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

LEVEL_NAME = json.loads((ROOT / "content/samples/qisas-al-nabiyyin-4/manifest.json").read_text(encoding="utf-8")).get("levelName", "Intermediate")
MANIFEST = {
 "id": "al-amana-wa-al-khashaba",
 "storyGroup": "al-amana-wa-al-khashaba",
 "title": {"ar": "الْأَمَانَةُ وَالْخَشَبَةُ", "en": "The Trust and the Log", "tr": "Emanet ve Odun"},
 "subtitle": {"ar": "رَجُلٌ اسْتَقْرَضَ أَلْفَ دِينَارٍ وَاللهُ شَهِيدُهُ وَكَفِيلُهُ، فَلَمَّا لَمْ يَجِدْ سَفِينَةً بَعَثَ بِالْمَالِ فِي خَشَبَةٍ — قِصَّةٌ لِلْمُسْتَوَى الثَّالِثِ",
              "en": "A man borrows a thousand dinars with God as his witness and guarantor; finding no ship, he sends the money in a log — a story for the third level",
              "tr": "Allah'ı şâhit ve kefil tutarak bin dinar borç alan adam; gemi bulamayınca parayı bir odunun içinde gönderir — üçüncü seviye için bir hikâye"},
 "level": 3,
 "levelName": LEVEL_NAME,
 "version": "0.1.0",
 "published": "2026-11-08",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّالِثُ) لِخَبَرِ الرَّجُلِ الَّذِي اسْتَقْرَضَ أَلْفَ دِينَارٍ وَبَعَثَ بِهَا فِي خَشَبَةٍ، الْمَرْوِيِّ فِي صَحِيحِ الْبُخَارِيِّ. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ هِيَ نَصُّ حَدِيثٍ وَلَا آيَةٌ، فَلَا يُنْسَبُ شَيْءٌ مِنْهُ إِلَى الْحَدِيثِ.",
  "en": "ORIGINAL Level-3 graded Arabic: the narrative of the man who borrowed a thousand dinars and sent them back in a log, preserved in Sahih al-Bukhari, RETOLD FREELY in the wording of a graded reader. No sentence is the text of a hadith, no verse is quoted, and none may be cited as such.",
  "tr": "ÖZGÜN 3. seviye kolaylaştırılmış Arapça: Sahîh-i Buhârî'de nakledilen, bin dinar borç alıp onu bir odunun içinde geri gönderen adamın kıssası, kolaylaştırılmış okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir hadisin metni değildir, hiçbir âyet aktarılmamıştır; hiçbiri hadis olarak nakledilemez.",
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
