"""Author content/samples/al-bukhari-fi-baghdad — «الْبُخَارِيُّ فِي بَغْدَادَ», an ORIGINAL story at Level 5 (Advanced).

ORIGINAL graded Arabic: the scholars of Baghdad test Imam al-Bukhārī's memory. They take a hundred ḥadīths, mix up their
chains and texts, and share them among ten men, ten each; in a crowded gathering each man puts his ḥadīths to him, and to every
one he answers that he does not know it; then he turns back to the first man and gives every text its right chain, in order,
then to the second, until the hundred are restored — and the people acknowledge his precedence. The report is told by
al-Khaṭīb al-Baghdādī (Tārīkh Baghdād, in the notice on al-Bukhārī) and by Ibn Ḥajar (Hady al-Sārī, the introduction to Fatḥ
al-Bārī), who remarks that the wonder is less the correcting than the memorising of the wrong order from one hearing. It is
RETOLD FREELY here: no ḥadīth text is quoted (the hundred stay unnamed), no āya is quoted, and no sentence is a quotation of a
source; the one phrase kept as the reports give it is al-Bukhārī's short reply «لَا أَعْرِفُهُ» («I do not know it»).
Ibn Ḥajar's remark is given in reported speech, as a paraphrase.

Four chapters, twenty-eight sentences, in a Level-5 register: mafʿūl muṭlaq (شَهَادَةً لَا شَكَّ فِيهَا، and مَرَّةً as its deputy of
number), mafʿūl lahu (تَعَجُّبًا), tamyīz (حِفْظًا after an elative; the counted noun after مِائَة and عَشَرَة), istithnāʾ mufarragh
(لَمْ يَقُلْ … إِلَّا، لَمْ يَسْمَعْهُ إِلَّا مَرَّةً), the numbers with their counted nouns (مِائَةَ حَدِيثٍ، عَشَرَةِ رِجَالٍ، عَشَرَةُ أَحَادِيثَ),
relative and na't clauses with a resumptive pronoun (خَبَرٌ يَرْوِيهِ، إِسْنَادًا لَيْسَ لَهُ، شَهَادَةً لَا شَكَّ فِيهَا), لَمَّا, حَتَّى + subjunctive
(حَتَّى يَعْرِفُوا) beside the ibtidāʾ حَتَّى, the wāw of ḥāl, أَمَّا … فَ, ظَنَّ with two objects, kāna and its sisters (كَانَ، صَارَ، لَيْسَ
with the extra bāʾ, مَا زَالَ), أَنَّ and لٰكِنَّ, and لَا of the genus.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf (the majority reading of a key
wins; a few keys whose majority gloss belongs to another context are pinned to a package with a plain gloss); four entries are
new — the names الْبُخَارِيّ and بَغْدَاد, إِسْنَاد in its ḥadīth sense (pl. أَسَانِيد; the shelf's `isnad` is the grammarians'
«predication»), the noun شَرْح (pl. شُرُوح) — and the name-phrase ابْنُ حَجَرٍ. No new verb is minted: every verb's paradigm is
copied from a package that already owns it. Regenerate with:
python3 tools/authoring/author_al_bukhari_fi_baghdad.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "al-bukhari-fi-baghdad"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "هُمْ": "هُمْ", "هِمْ": "هُمْ"})
N = lambda s: unicodedata.normalize("NFC", s)

# ---- the clause seats and short notes this story needs (ar, en, tr) ---------------------------------------------------
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
MAQUL_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekûlü'l-kavl olarak mahallen mansûb")
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
KH_ZALA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ", "; the clause is the predicate of زَالَ, in the seat of nasb", "; cümle zâle'nin haberi olarak mahallen mansûb")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
DIPT_BAGHDAD = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town), barred from tanwin", " — müennes özel isim (şehir adı), gayr-i munsarif")
MUNTAHA = (" — جَمْعُ حَدِيثٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ", " — the plural of حَدِيث, on the farthest-plural pattern", " — hadîs'in müntehe'l-cumû' vezninde cem'i")
def NAAT_OF(seat, of_ar, of_en, of_tr, second=False):
    """the clause is the na't of a named indefinite noun"""
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return (" — وَالْجُمْلَةُ فِي مَحَلِّ " + s[0] + " نَعْتٌ " + ("ثَانٍ " if second else "") + "لِـ«" + of_ar + "»",
            "; the clause qualifies «" + of_en + "» — " + ("a second na't, " if second else "") + "in the seat of " + s[1],
            "; cümle «" + of_tr + "» için " + ("ikinci " if second else "") + "na't, mahallen " + s[2])
def JAR_NAAT(seat, of_ar, of_en, of_tr):
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return ("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ " + s[0] + " نَعْتٌ لِـ«" + of_ar + "»",
            "; the jarr phrase qualifies «" + of_en + "», in the seat of " + s[1],
            "; câr-mecrûr «" + of_tr + "» için na't, mahallen " + s[2])
def NOTE(t, ar="", en="", tr=""):
    """append a remark to a kit line, before its closing full stop"""
    for k, v in (("ar", ar), ("en", en), ("tr", tr)):
        if v:
            s = t["irab"][k]
            t["irab"][k] = N((s[:-1] if s.endswith(".") else s) + v + ".")
    return t
def PH(t, lex, span=2):
    """the name-phrase sits on the FIRST token of its span (CLAUDE.md «Idioms/phrases»): both words keep their own iʿrāb"""
    t["phrase"] = {"lex": lex, "span": span}
    return t

# ---- names ---------------------------------------------------------------------------------------------------------------
NISBA = (" — نِسْبَةٌ إِلَى بُخَارَى صَارَتْ عَلَمًا عَلَى الْإِمَامِ", " — a nisba to Bukhārā that became the Imam's name", " — Buhârâ'ya nispet olup İmam'ın adı olmuştur")
BUKHARI_F = lambda punct=None: FAIL("الْبُخَارِيُّ", "bukhari", "propn", note_ar=NISBA[0], note_en=NISBA[1], note_tr=NISBA[2], punct=punct)
BAGHDAD_J = lambda punct=None: MAJR("بَغْدَادَ", "baghdad", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_BAGHDAD[0], note_en=DIPT_BAGHDAD[1], note_tr=DIPT_BAGHDAD[2], punct=punct)

# ---- particles and short words ------------------------------------------------------------------------------------------
AN_PREP = lambda punct=None: PREP("عَنْ", "an", gloss_tr="«-den, hakkında»", punct=punct)
def ANNA_T(role=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".",
        "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
HATTA = lambda: tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
    "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «so that, until» is a particle of limit and jarr: the present verb after it is in nasb by an أَنْ that must stay hidden, and the masdar they build is in jarr by حَتَّى.",
    "Hattâ — gâye ve cer harfi: sonraki muzâri vücûben gizli en ile mansûb; kurdukları müevvel masdar hattâ ile mecrûr.")
WA_ISTINAF_T = lambda full, lex, rest_ar, rest_en, rest_tr, grammar, pos="noun", punct=None: tok(full, lex, pos, grammar,
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَ" + rest_ar, "The waw opens a new sentence; " + rest_en, "Vâv isti'nâf içindir; " + rest_tr, punct=punct,
    segments=[seg("وَ", "wa", "conj"), seg(full[2:], lex, pos)])
def ZALA(hidden=False):
    return tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + ("، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else "") + " — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ.",
        "زَالَ is a defective past verb, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb" + ("; its noun is the hidden pronoun «he»" if hidden else "") + " — after a negation it means «never ceased».",
        "Zâle: kâne'nin kardeşlerinden, fetha üzere mebnî nâkıs mâzî; ismini ref, haberini nasb eder" + ("; ismi gizli zamir «o»" if hidden else "") + " — nefiyle birlikte devamlılık bildirir.")
WA_MA = lambda: WA_ISTINAF_T("وَمَا", "ma-nafiya", "مَا حَرْفُ نَفْيٍ.", "مَا negates the verb after it.", "mâ nefiy harfi.", ["la-nafiya"], pos="part")
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
HADHA = lambda seat_ar, seat_en, seat_tr, extra=None, punct=None: ISHARA("هٰذَا", "hadha", seat_ar, seat_en, seat_tr, extra=extra, punct=punct)
def LAYSA_T(note=("", "", ""), extra=None):
    return tok("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha"] + (extra or []),
        "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + note[0] + ".",
        "لَيْسَ «is not» is the frozen defective verb, built on fatha: it raises its noun and puts its predicate in nasb; its noun is the hidden pronoun «it»" + note[1] + ".",
        "Leyse: fetha üzere mebnî câmid nâkıs mâzî; ismini ref, haberini nasb eder; ismi gizli zamir «o»" + note[2] + ".")
def KULL_TAWKID(full, case, enc, of_ar, of_en, of_tr, punct=None):
    """كُلِّهَا، كُلَّهَا: a tawkid of meaning, annexed to the pronoun that returns to what it strengthens"""
    sign = {"nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "in nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "in jarr", "mecrûr")}[case]
    return tok(full, "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
        "تَوْكِيدٌ مَعْنَوِيٌّ لِـ«" + of_ar + "» " + sign[0] + "، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        "A tawkid of meaning «all of them», strengthening «" + of_en + "» and " + sign[1] + " like it; annexed to the pronoun, which fills the seat of jarr.",
        "Ma'nevî te'kîd «hepsi», «" + of_tr + "»yi pekiştirir ve onun gibi " + sign[2] + "; zamire muzâf, zamir mahallen mecrûr.", punct=punct,
        segments=[seg(full[:-len(enc)], "kull", "noun"), seg(enc, PRON[enc], "pron")])
def LI_N(full, lex, stem, note=("", "", ""), extra=None, punct=None):
    """لِكُلِّ، لِأَحَدٍ: the lam of jarr on an indefinite or annexed noun"""
    return tok(full, "li", "prep", ["huruf-jarr"] + (extra or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَ" + stem + " مَجْرُورٌ بِالْكَسْرَةِ" + note[0] + ".", "The lam is a jarr letter; the noun after it is in jarr" + note[1] + ".", "Lâm cer harfi; sonraki isim mecrûr" + note[2] + ".",
        punct=punct, segments=[seg("لِ", "li", "prep"), seg(stem, lex, "noun")])
def LAHU(pron_tr, punct=None, note=("", "", "")):
    """لَهُ: the lam of jarr (voweled with fatha before a pronoun) and the attached «him»"""
    return tok("لَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
        "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ" + note[0] + ".",
        "The lam is a jarr letter; the attached «him» is built on damma and fills the seat of jarr" + note[1] + ".",
        "Lâm cer harfi; bitişik «o» zamiri damme üzere mebnî, mahallen mecrûr" + pron_tr + note[2] + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")])
def ZARF_BADA(note=("", "", "")):
    return tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ" + note[0] + ".",
        "An adverb of time «after», in nasb and annexed" + note[1] + ".", "Zaman zarfı «sonra», mansûb, muzâf" + note[2] + ".")
MANQUS = ("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ")
MANQUS_NOTE = (" — اسْمٌ مَنْقُوصٌ", " — a manqūṣ noun: the vowel is estimated on the ya", " — mankûs isim: hareke yâ üzerinde takdîrî")

# ---- the verb and noun shapes the kit does not carry ---------------------------------------------------------------------
def MUD_ENC_DF(full, lex, enc, extra=None, punct=None, note=("", "", ""), naqis=False):
    """يَرْوِيهِ أَهْلُ الْعِلْمِ: a present verb in raf' with its object pronoun, the doer following"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    sign = ("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " (the damma is estimated on the ya)", " (damme yâ üzerinde takdîrî)") if naqis else ("بِالضَّمَّةِ", "", "")
    return tok(full, lex, "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi"] + (["naqis-verbs"] if naqis else []) + (extra or []),
        ar0 + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign[0] + "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ" + note[0] + ".",
        en0 + "present verb in raf'" + sign[1] + "; the attached pronoun is its object, placed before the doer, which follows" + note[1] + ".",
        tr0 + "merfû muzâri" + sign[2] + "; bitişik zamir fâilden önce gelmiş mef'ûlün bih, mahallen mansûb; fâili ondan sonra gelir" + note[2] + ".",
        punct=punct, segments=[s for s in [sg, seg(stem[:-len(enc)], lex, "verb"), seg(enc, PRON[enc], "pron")] if s])
def FIVE_NASB_ENC(full, lex, enc, extra=None, punct=None, note=("", "", "")):
    """يَمْتَحِنُوهُ: one of the five verbs in nasb by أَنْ (the nun dropped), with an attached object"""
    stem = full[:-len(enc)]
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil", "maful-bihi"] + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note[0] + ".",
        "Present verb in nasb by أَنْ, its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf', and the attached pronoun its object, in the seat of nasb" + note[1] + ".",
        "En ile mansûb muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû; bitişik zamir mef'ûlün bih, mahallen mansûb" + note[2] + ".",
        punct=punct, segments=[seg(stem[:-1], lex, "verb"), seg("و", "pron-3mp", "pron"), seg(enc, PRON[enc], "pron")])
def MAF2(full, lex, extra=None, punct=None, note=("", "", "")):
    """the second object of a verb of two objects"""
    return tok(full, lex, "noun", ["maful-bihi", "mafulayn"] + (extra or []), "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ" + note[0] + ".",
        "The second object, in nasb" + note[1] + ".", "İkinci mef'ûlün bih, mansûb" + note[2] + ".", punct=punct)
def MUTLAQ_NAW(full, lex, verb_ar, verb_en, verb_tr, how=("بِوَصْفِهِ", "by the adjective after it", "sıfatıyla"), extra=None, punct=None, note=("", "", "")):
    """شَهَادَةً لَا شَكَّ فِيهَا: the absolute object that names the KIND of the act"""
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"] + (extra or []),
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «" + verb_ar + "» مُبَيِّنٌ لِلنَّوْعِ " + how[0] + note[0] + ".",
        "The absolute object (maf'ul mutlaq), in nasb — the masdar of «" + verb_en + "», naming the KIND of the act " + how[1] + note[1] + ".",
        "Mef'ûlün mutlak, mansûb — «" + verb_tr + "» fiilinin masdarı; " + how[2] + " fiilin nev'ini beyan eder" + note[2] + ".", punct=punct)
def MAFUL_LAHU(full, lex, punct=None):
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"],
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ.",
        "The maf'ul li-ajlih (object of cause), in nasb — a masdar of the heart giving the reason for the act, sharing its time and its doer.",
        "Mef'ûlün lieclih, mansûb — fiilin sebebini bildiren kalbî masdar; fiille zamanda ve fâilde ortak.", punct=punct)
def TAMYIZ_T(full, lex, what_ar, what_en, what_tr, punct=None):
    return tok(full, lex, "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"],
        "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ " + what_ar + ".", "A specifier (tamyiz), in nasb — it names " + what_en + ".", "Temyîz, mansûb — " + what_tr + " beyan eder.", punct=punct)
TAFDIL_TAMYIZ = ("جِهَةَ التَّفْضِيلِ", "the respect in which the comparison holds", "üstünlüğün hangi yönden olduğunu")
def FA_AMMA(full):
    """فَأَمَّا / وَأَمَّا: the particle of detailing"""
    pre = full[:2]
    return tok(full, "amma", "part", ["amma-tafsiliyya"],
        ("الْفَاءُ لِلِاسْتِئْنَافِ" if pre == "فَ" else "الْوَاوُ عَاطِفَةٌ") + "، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
        ("The fa opens a new sentence" if pre == "فَ" else "The waw conjoins") + "; أَمَّا «as for» is the particle of condition, detailing and emphasis, built on sukun, with no seat — its answer must take the fa.",
        ("Fâ isti'nâf içindir" if pre == "فَ" else "Vâv atıf harfidir") + "; emmâ «…-e gelince»: şart, tafsîl ve te'kîd harfi, sükûn üzere mebnî, mahalli yoktur — cevabı fâ ile bağlanır.",
        segments=[seg(pre, "fa" if pre == "فَ" else "wa", "conj"), seg("أَمَّا", "amma", "part")])
FA_AMMA_AR = "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَ"
FA_AMMA_EN = "The fa answers أَمَّا; "
FA_AMMA_TR = "Fâ emmâ'nın cevabına gelmiştir; "
KH_AMMA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the clause is the predicate of the mubtada, in the seat of raf'", "; cümle mübtedânın haberi, mahallen merfû")

TITLES = [{"ar": "الْإِمَامُ وَعُلَمَاءُ بَغْدَادَ", "en": "The Imam and the scholars of Baghdad", "tr": "İmam ve Bağdat âlimleri"},
          {"ar": "الْمَجْلِسُ", "en": "The gathering", "tr": "Meclis"},
          {"ar": "الْجَوَابُ", "en": "The answer", "tr": "Cevap"},
          {"ar": "بَعْدَ الْمَجْلِسِ", "en": "After the gathering", "tr": "Meclisten sonra"}]

# ======================================== Chapter 1 — الْإِمَامُ وَعُلَمَاءُ بَغْدَادَ ========================================
S1 = []
S1.append({"id": "s1", "translation": {"en": "This is a report that the scholars relate about Imam al-Bukhārī; we tell it here in our own words.",
                                      "tr": "Bu, âlimlerin İmam Buhârî hakkında rivayet ettiği bir haberdir; biz onu burada kendi sözlerimizle anlatıyoruz."},
 "tokens": [HADHA("رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ", extra=["mubtada-khabar"]), KHABAR("خَبَرٌ", "khabar"),
  MUD_ENC_DF("يَرْوِيهِ", "rawa", "هِ", ["jumla-sifa"], naqis=True,
    note=(" — وَالْهَاءُ عَائِدٌ عَلَى «خَبَرٌ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لَهُ", "; the pronoun returns to «a report», and the clause is its na't, in the seat of raf'", "; zamir «haber»e döner; cümle onun na'tı, mahallen merfû")),
  FAIL("أَهْلُ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْعِلْمِ", "ilm"),
  AN_KASRA(), MAJR("الْإِمَامِ", "imam"),
  tok("الْبُخَارِيِّ", "bukhari", "propn", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"],
    "بَدَلٌ مِنَ «الْإِمَامِ» مَجْرُورٌ بِالْكَسْرَةِ" + NISBA[0] + ".", "A badal of «the Imam», in jarr" + NISBA[1] + ".", "«İmam»dan bedel, mecrûr" + NISBA[2] + ".", punct="،"),
  MUDARI("نَحْكِيهِ", "haka", ["naqis-verbs", "jumla-sifa"], who="نَحْنُ", enc="هِ", naqis="ي", wujub=True,
    note_ar=NAAT_OF("raf", "خَبَرٌ", "a report", "haber", True)[0], note_en=NAAT_OF("raf", "خَبَرٌ", "a report", "haber", True)[1], note_tr=NAAT_OF("raf", "خَبَرٌ", "a report", "haber", True)[2]),
  HUNA(), BI_NOUN("بِأَلْفَاظِنَا", "lafz", "أَلْفَاظِنَا", enc="نَا", extra=["jam-taksir"], note_ar=" — جَمْعُ لَفْظٍ", note_en=" — «our words», the plural of لَفْظ", note_tr=" — lafz'ın cem'i, «sözlerimiz»", punct=".")]})

S1.append({"id": "s2", "translation": {"en": "Al-Bukhārī was the strongest of the people of his time in memory for ḥadīth, and people knew him in every land.",
                                      "tr": "Buhârî, zamanının insanları içinde hadis ezberi bakımından en güçlüsüydü; insanlar onu her beldede tanırdı."},
 "tokens": [KANA("كَانَ"), ISMK("الْبُخَارِيُّ", "bukhari", "propn", note_ar=NISBA[0], note_en=NISBA[1], note_tr=NISBA[2]),
  KHK("أَقْوَى", "aqwa", extra=["ism-tafdil", "idafa-definiteness"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ",
    note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ", note_en=" — the fatha is estimated on the alif; an elative «strongest», annexed", note_tr=" — fetha elif üzerinde takdîrî; ism-i tafdîl «en güçlü», muzâf"),
  MUDAF_ILAYH("أَهْلِ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf"),
  TAMYIZ_T("حِفْظًا", "hifz", *TAFDIL_TAMYIZ),
  LI_AL("لِلْحَدِيثِ", "hadith", "الْحَدِيثِ", punct="،", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«حِفْظًا»", note_en=" — the jarr phrase attaches to «memory»", note_tr=" — câr-mecrûr «ezber»e müteallik"),
  tok("وَقَدْ", "qad", "part", ["atf-nasaq"], WA_AR + "قَدْ حَرْفُ تَحْقِيقٍ.", "The waw conjoins a second sentence; قَدْ affirms the past verb after it.", "«ve» + kad tahkîk harfi.",
    segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  ENC_MADI("عَرَفَهُ", "arafa", "هُ", note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili ondan sonra gelir"), FAIL("النَّاسُ", "nas"),
  FI(), MAJR("كُلِّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("بَلَدٍ", "balad", punct=".")]})

S1.append({"id": "s3", "translation": {"en": "When he arrived in Baghdad, its scholars heard of him.", "tr": "Bağdat'a vardığında oranın âlimleri onu duydular."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("وَصَلَ", "wasala", ["mithal-verbs"], hidden=True, note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]),
  ILA(), BAGHDAD_J(punct="،"),
  MADI("سَمِعَ", "samia", note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]), BIHI(),
  ENC_NOUN("عُلَمَاؤُهَا", "alim-scholar", "هَا", "fail", extra=["jam-taksir"], punct=".",
    note_ar=" — جَمْعُ عَالِمٍ عَلَى فُعَلَاءَ، وَالْهَاءُ عَائِدٌ عَلَى بَغْدَادَ", note_en=" — the plural of عَالِم on فُعَلَاء; the pronoun «its» returns to Baghdad", note_tr=" — âlim'in fuʿalâ' veznindeki cem'i; zamir Bağdat'a döner")]})

S1.append({"id": "s4", "translation": {"en": "So they met and agreed to test his memory, so that they might know his worth.",
                                      "tr": "Bunun üzerine toplanıp onun ezberini sınamakta birleştiler; ta ki değerini bilsinler."},
 "tokens": [VERB_WAW("فَاجْتَمَعُوا", "ijtamaa", ["form-viii-verbs"]), ALA(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِعَلَى، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«اجْتَمَعُوا»", "; the masdar it builds is in jarr after عَلَى, and the phrase attaches to «they met (agreeing)»", "; kurduğu müevvel masdar alâ ile mecrûr; câr-mecrûr «toplandılar»a müteallik"),
  FIVE_NASB("يَمْتَحِنُوا", "imtahana", ["form-viii-verbs"]), ENC_NOUN("حِفْظَهُ", "hifz", "هُ", "maful", punct="،"),
  HATTA(), FIVE_NASB("يَعْرِفُوا", "arafa", by="أَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى", by_en="an أَنْ hidden of necessity after حَتَّى", by_tr="hattâ'dan sonra vücûben gizli en"),
  ENC_NOUN("قَدْرَهُ", "qadr", "هُ", "maful", punct=".")]})

S1.append({"id": "s5", "translation": {"en": "They took a hundred ḥadīths and mixed up their chains with their texts.",
                                      "tr": "Yüz hadis aldılar ve onların isnadlarını metinleriyle birbirine karıştırdılar."},
 "tokens": [VERB_WAW("فَأَخَذُوا", "akhadha"),
  MAFUL("مِائَةَ", "mia", extra=["asma-al-adad-fil-kafiya", "idafa-definiteness"],
    note_ar="، مُضَافٌ — وَالْمِائَةُ تُضَافُ إِلَى مُفْرَدٍ مَجْرُورٍ", note_en=", annexed — مِائَة is annexed to a singular noun in jarr", note_tr=", muzâf — mi'e, mecrûr bir müfrede muzâf olur"),
  MUDAF_ILAYH("حَدِيثٍ", "hadith", extra=["asma-al-adad-fil-kafiya"], punct="،",
    note_ar=" — وَهُوَ تَمْيِيزُ الْعَدَدِ: مُفْرَدٌ مَجْرُورٌ بِالْإِضَافَةِ", note_en=" — the counted noun (the tamyiz of the number): a singular, in jarr by the idafa", note_tr=" — sayının temyîzi: izâfetle mecrûr müfred"),
  VERB_WAW("فَخَلَطُوا", "khalata"),
  ENC_NOUN("أَسَانِيدَهَا", "isnad-chain", "هَا", "maful", extra=["jam-taksir", "mamnu-min-sarf"],
    note_ar=" — جَمْعُ إِسْنَادٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَالْهَاءُ عَائِدٌ عَلَى الْأَحَادِيثِ", note_en=" — the plural of إِسْنَاد on the farthest-plural pattern; «their» returns to the ḥadīths", note_tr=" — isnâd'ın müntehe'l-cumû' vezninde cem'i; zamir hadislere döner"),
  BI_NOUN("بِمُتُونِهَا", "matn", "مُتُونِهَا", enc="هَا", extra=["jam-taksir"], punct=".",
    note_ar=" — جَمْعُ مَتْنٍ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«خَلَطُوا»", note_en=" — the plural of مَتْن; the jarr phrase attaches to «mixed»", note_tr=" — metn'in cem'i; câr-mecrûr «karıştırdılar»a müteallik")]})

S1.append({"id": "s6", "translation": {"en": "They gave every text a chain that was not its own.", "tr": "Her metne, kendisine ait olmayan bir isnad verdiler."},
 "tokens": [VERB_WAW("فَأَعْطَوْا", "aata", ["form-iv-verbs", "mafulayn"], alif=True,
    note_ar=" — وَهُوَ يَنْصِبُ مَفْعُولَيْنِ", note_en="; the verb takes two objects", note_tr="; fiil iki mef'ûl alır"),
  MAFUL("كُلَّ", "kull", extra=["idafa-definiteness", "mafulayn"], note_ar="، مُضَافٌ — وَهُوَ الْمَفْعُولُ الْأَوَّلُ", note_en=", annexed — the first object", note_tr=", muzâf — birinci mef'ûl"),
  MUDAF_ILAYH("مَتْنٍ", "matn"),
  MAF2("إِسْنَادًا", "isnad-chain"),
  LAYSA_T((" يَعُودُ عَلَى «إِسْنَادًا» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«إِسْنَادًا»", ", returning to «a chain» — the clause qualifies «a chain», in the seat of nasb", ", «isnad»a döner — cümle «isnad»ın na'tı, mahallen mansûb"), extra=["jumla-sifa"]),
  LAHU(" («onun»)", punct=".", note=("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ لَيْسَ، وَالْهَاءُ عَائِدٌ عَلَى «مَتْنٍ»", "; the jarr phrase is the predicate of لَيْسَ, in the seat of nasb, and the pronoun returns to «text»", "; câr-mecrûr leyse'nin haberi, mahallen mansûb; zamir «metin»e döner"))]})

S1.append({"id": "s7", "translation": {"en": "Then they divided them among ten men, so that each man of them had ten ḥadīths.",
                                      "tr": "Sonra onları on adam arasında paylaştırdılar; her birine on hadis düştü."},
 "tokens": [THUMMA(), VERB_WAW_ENC("قَسَمُوهَا", "qasama", "هَا"), ALA(),
  MAJR("عَشَرَةِ", "ashara", extra=["asma-al-adad-fil-kafiya", "idafa-definiteness"],
    note_ar="، مُضَافٌ — وَجَاءَ الْعَدَدُ بِالتَّاءِ لِأَنَّ مُفْرَدَ الْمَعْدُودِ (رَجُلٌ) مُذَكَّرٌ", note_en=", annexed — the number takes the ta because the singular of the counted noun (رَجُل) is masculine", note_tr=", muzâf — sayılanın müfredi (racul) müzekker olduğu için sayı tâ ile gelmiştir"),
  MUDAF_ILAYH("رِجَالٍ", "rajul", extra=["jam-taksir", "asma-al-adad-fil-kafiya"], punct="،",
    note_ar=" — تَمْيِيزُ الْعَدَدِ: جَمْعٌ مَجْرُورٌ بِالْإِضَافَةِ، وَهُوَ جَمْعُ رَجُلٍ", note_en=" — the counted noun after 3–10: a plural in jarr by the idafa (the plural of رَجُل)", note_tr=" — sayının temyîzi: izâfetle mecrûr cem' (racul'ün cem'i)"),
  KANA("فَكَانَ"),
  LI_N("لِكُلِّ", "kull", "كُلِّ", ("، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ", ", annexed; the jarr phrase is the FRONTED predicate of كَانَ", ", muzâf; câr-mecrûr kâne'nin öne alınmış haberi"), extra=["kana-wa-akhawatuha", "idafa-definiteness"]),
  MUDAF_ILAYH("رَجُلٍ", "rajul"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", note_ar=JAR_NAAT("jarr", "رَجُلٍ", "man", "adam")[0], note_en=JAR_NAAT("jarr", "رَجُلٍ", "man", "adam")[1], note_tr=JAR_NAAT("jarr", "رَجُلٍ", "man", "adam")[2]),
  ISMK("عَشَرَةُ", "ashara", extra=["asma-al-adad-fil-kafiya", "idafa-definiteness"], muakhkhar=True,
    note_ar="، مُضَافٌ — وَجَاءَ بِالتَّاءِ لِأَنَّ مُفْرَدَ الْمَعْدُودِ (حَدِيثٌ) مُذَكَّرٌ", note_en=", annexed — it takes the ta because the singular of the counted noun (حَدِيث) is masculine", note_tr=", muzâf — sayılanın müfredi (hadîs) müzekker olduğu için tâ ile gelmiştir"),
  MUDAF_ILAYH("أَحَادِيثَ", "hadith", extra=["jam-taksir", "mamnu-min-sarf", "asma-al-adad-fil-kafiya"], sign=FATHA_JARR, punct=".",
    note_ar=" — تَمْيِيزُ الْعَدَدِ، جَمْعُ حَدِيثٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، فَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ",
    note_en=" — the counted noun; the plural of حَدِيث on the farthest-plural pattern, a diptote, so the fatha stands for the kasra",
    note_tr=" — sayının temyîzi; hadîs'in müntehe'l-cumû' vezninde cem'i, gayr-i munsarif olduğu için kesre yerine fetha ile")]})

# =================================================== Chapter 2 — الْمَجْلِسُ ===================================================
S2 = []
S2.append({"id": "s1", "translation": {"en": "They set a day for the gathering, and a great crowd of people attended it.",
                                      "tr": "Meclis için bir gün belirlediler; ona büyük bir kalabalık katıldı."},
 "tokens": [VERB_WAW("وَجَعَلُوا", "jaala"),
  LI_AL("لِلْمَجْلِسِ", "majlis", "الْمَجْلِسِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«جَعَلُوا»", note_en=" — the jarr phrase attaches to «they set»", note_tr=" — câr-mecrûr «belirlediler»e müteallik"),
  MAFUL("يَوْمًا", "yawm", punct="،"),
  ENC_MADI("فَحَضَرَهُ", "hadara", "هُ", note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili ondan sonra gelir"),
  FAIL("جَمْعٌ", "jam"), NAAT("عَظِيمٌ", "azim", "raf", ["sifa-mushabbaha"]), MINA(),
  MAJR("النَّاسِ", "nas", punct=".", note_ar=JAR_NAAT("raf", "جَمْعٌ", "crowd", "kalabalık")[0], note_en=JAR_NAAT("raf", "جَمْعٌ", "crowd", "kalabalık")[1], note_tr=JAR_NAAT("raf", "جَمْعٌ", "crowd", "kalabalık")[2])]})

S2.append({"id": "s2", "translation": {"en": "When the people had sat down, one of the ten men stood up and asked him about one of his ḥadīths.",
                                      "tr": "İnsanlar oturunca on kişiden biri kalktı ve ona hadislerinden birini sordu."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("جَلَسَ", "jalasa", note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), FAIL("النَّاسُ", "nas", punct="،"),
  MADI("قَامَ", "qama", ["hollow-verbs"], note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]), FAIL("رَجُلٌ", "rajul"), MINA(),
  MAJR("الْعَشَرَةِ", "ashara", extra=["asma-al-adad-fil-kafiya"], punct="،", note_ar=JAR_NAAT("raf", "رَجُلٌ", "a man", "adam")[0], note_en=JAR_NAAT("raf", "رَجُلٌ", "a man", "adam")[1], note_tr=JAR_NAAT("raf", "رَجُلٌ", "a man", "adam")[2]),
  ENC_MADI("فَسَأَلَهُ", "saala", "هُ", hidden=True), AN_PREP(), MAJR("حَدِيثٍ", "hadith"), MIN(),
  ENC_NOUN("أَحَادِيثِهِ", "hadith", "هِ", "majr", extra=["jam-taksir", "mamnu-min-sarf"], punct=".",
    note_ar=" — وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ، وَهُوَ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ؛ وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«حَدِيثٍ»",
    note_en=" — a diptote plural, but annexed, so it takes the kasra; the jarr phrase qualifies «a ḥadīth», in the seat of jarr",
    note_tr=" — gayr-i munsarif cem' iken muzâf olduğu için kesre ile mecrûr; câr-mecrûr «hadis»in na'tı, mahallen mecrûr")]})

S2.append({"id": "s3", "translation": {"en": "Al-Bukhārī said: «I do not know it.»", "tr": "Buhârî dedi: «Onu bilmiyorum.»"},
 "tokens": [MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), BUKHARI_F(punct=":"),
  LA_NAFIYA(), MUDARI("أَعْرِفُهُ", "arafa", who="أَنَا", enc="هُ", wujub=True, punct=".", note_ar=MAQUL_CL[0], note_en=MAQUL_CL[1], note_tr=MAQUL_CL[2])]})

S2.append({"id": "s4", "translation": {"en": "The man kept asking him about one ḥadīth after another, while al-Bukhārī gave him the same answer, until he had finished all his ḥadīths.",
                                      "tr": "Adam ona hadis ardına hadis sormaya devam etti, Buhârî de ona aynı cevabı veriyordu; sonunda adam bütün hadislerini bitirdi."},
 "tokens": [WA_MA(), ZALA(), tok("الرَّجُلُ", "rajul", "noun", ["kana-wa-akhawatuha"], "اسْمُ زَالَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of زَالَ, in raf'.", "Zâle'nin ismi, merfû."),
  MUDARI("يَسْأَلُهُ", "saala", enc="هُ", note_ar=KH_ZALA[0], note_en=KH_ZALA[1], note_tr=KH_ZALA[2]),
  AN_PREP(), MAJR("حَدِيثٍ", "hadith"),
  ZARF_BADA((" — مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٍ لِـ«حَدِيثٍ»", "; it hangs on an omitted na't of «a ḥadīth»", "; «hadis»in mahzûf na'tına müteallik")),
  MUDAF_ILAYH("حَدِيثٍ", "hadith", punct="،"),
  tok("وَالْبُخَارِيُّ", "bukhari", "propn", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"],
    "الْوَاوُ حَالِيَّةٌ، وَالْبُخَارِيُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens a hal clause; «al-Bukhārī» is the mubtada, in raf' — the nominal clause is a hal, in the seat of nasb.",
    "Hâl vâvı; «Buhârî» mübtedâ, merfû — isim cümlesi hâl olarak mahallen mansûb.",
    segments=[seg("وَ", "wa", "conj"), seg("الْبُخَارِيُّ", "bukhari", "propn")]),
  MUDARI("يُجِيبُهُ", "ajaba", ["form-iv-verbs", "hollow-verbs"], enc="هُ", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]),
  BI_NOUN("بِمِثْلِ", "mithl", "مِثْلِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en="; it is annexed", note_tr="; muzâf"),
  DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", punct="،", extra=["idafa-definiteness"]),
  HATTA_IBT(), MADI("فَرَغَ", "faragha", hidden=True), MIN(),
  ENC_NOUN("أَحَادِيثِهِ", "hadith", "هِ", "majr", extra=["jam-taksir", "mamnu-min-sarf"],
    note_ar=" — وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ", note_en=" — a diptote plural, but annexed, so it takes the kasra", note_tr=" — gayr-i munsarif cem' iken muzâf olduğu için kesre ile"),
  KULL_TAWKID("كُلِّهَا", "jarr", "هَا", "أَحَادِيثِهِ", "his ḥadīths", "hadisleri", punct=".")]})

S2.append({"id": "s5", "translation": {"en": "Then the second stood up, then the third, until all ten had finished.", "tr": "Sonra ikincisi kalktı, sonra üçüncüsü; nihayet onların hepsi bitirdi."},
 "tokens": [THUMMA(), MADI("قَامَ", "qama", ["hollow-verbs"]),
  FAIL("الثَّانِي", "thani", extra=["ism-maqsur-manqus"], sign=MANQUS[0], note_ar=MANQUS_NOTE[0], note_en=MANQUS_NOTE[1], note_tr=MANQUS_NOTE[2], punct="،"),
  THUMMA(), tok("الثَّالِثُ", "thalith", "noun", ["atf-nasaq"], "مَعْطُوفٌ عَلَى «الثَّانِي» بِثُمَّ مَرْفُوعٌ بِالضَّمَّةِ.", "Conjoined to «the second» by ثُمَّ, in raf' like it.", "Sümme ile «ikinci»ye ma'tûf, merfû.", punct="،"),
  HATTA_IBT(), MADI("فَرَغَ", "faragha"), FAIL("الْعَشَرَةُ", "ashara", extra=["asma-al-adad-fil-kafiya"]), KULLUHUM(punct=".")]})

S2.append({"id": "s6", "translation": {"en": "And to none of them did he say anything but «I do not know it».", "tr": "Onlardan hiçbirine «Onu bilmiyorum»dan başka bir şey söylemedi."},
 "tokens": [WA_LAM(), JAZM_V("يَقُلْ", "qala", ["hollow-verbs", "maful-bihi"], hidden="هُوَ",
    note_ar=" — وَحُذِفَتْ عَيْنُهُ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — its middle letter (the waw) dropped where two quiescents met", note_tr=" — iki sâkin karşılaşınca aynü'l-fiili (vâv) düştü"),
  LI_N("لِأَحَدٍ", "ahad", "أَحَدٍ", (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَقُلْ»", "; the jarr phrase attaches to «say»", "; câr-mecrûr «söyledi»ye müteallik")),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", note_ar=JAR_NAAT("jarr", "أَحَدٍ", "one", "biri")[0], note_en=JAR_NAAT("jarr", "أَحَدٍ", "one", "biri")[1], note_tr=JAR_NAAT("jarr", "أَحَدٍ", "one", "biri")[2]),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"],
    "أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ لِأَنَّ الْكَلَامَ مَنْفِيٌّ وَلَمْ يُذْكَرِ الْمُسْتَثْنَى مِنْهُ، فَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ لِـ«يَقُلْ».",
    "إِلَّا «but, except» governs nothing here: the exception is «emptied» (mufarragh) — the sentence is negated and what is excepted from is not named, so the words after it are the object of «say», in the seat of nasb.",
    "İllâ burada amel etmez: istisnâ müferrağdır — cümle menfî ve müstesnâ minh zikredilmemiştir; sonraki cümle «söyledi»nin mekûlü olarak mahallen mansûb.", punct=":"),
  LA_NAFIYA(), MUDARI("أَعْرِفُهُ", "arafa", who="أَنَا", enc="هُ", wujub=True, punct=".")]})

S2.append({"id": "s7", "translation": {"en": "As for the men of understanding, they knew what he was doing; as for the others, they thought him weak of memory.",
                                      "tr": "Anlayış sahipleri onun ne yaptığını anladılar; diğerleri ise onu ezberi zayıf sandılar."},
 "tokens": [FA_AMMA("فَأَمَّا"), MUBTADA("أَهْلُ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْفَهْمِ", "fahm"),
  tok("فَعَرَفُوا", "arafa", "verb", ["amma-tafsiliyya", "al-bariz-al-muttasil", "fail"],
    FA_AMMA_AR + "عَرَفُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + KH_AMMA[0] + ".",
    FA_AMMA_EN + "«they knew» is a past verb built on damma before the waw of the group; that waw is the doer, in the seat of raf'" + KH_AMMA[1] + ".",
    FA_AMMA_TR + "«bildiler», cemâat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâil, mahallen merfû" + KH_AMMA[2] + ".",
    segments=[seg("فَ", "fa", "conj"), seg("عَرَفُو", "arafa", "verb"), seg("ا", "pron-3mp", "pron")]),
  MAWSUL_MAF("مَا", "ma-mawsula", built="السُّكُونِ", built_en="sukun", built_tr="sükûn"),
  MUDARI("يَصْنَعُ", "sanaa", punct="،", note_ar=SILA[0] + "، وَالْعَائِدُ مَحْذُوفٌ: مَا يَصْنَعُهُ", note_en=SILA[1] + "; the pronoun returning to مَا is dropped («what he was doing [it]»)", note_tr=SILA[2] + "; mevsûle dönen zamir hazfedilmiştir"),
  FA_AMMA("وَأَمَّا"), ENC_NOUN("غَيْرُهُمْ", "ghayr", "هُمْ", "mubtada"),
  tok("فَظَنُّوهُ", "zanna", "verb", ["amma-tafsiliyya", "zanna-wa-akhawatuha", "mafulayn", "doubled-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
    FA_AMMA_AR + "ظَنُّوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ" + KH_AMMA[0] + ".",
    FA_AMMA_EN + "«they thought» is a past verb built on damma before the waw of the group; the waw is the doer, and the attached «him» is the FIRST object of ظَنَّ, in the seat of nasb" + KH_AMMA[1] + ".",
    FA_AMMA_TR + "«sandılar», cemâat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâil; bitişik «onu» zannetmek fiilinin birinci mef'ûlü, mahallen mansûb" + KH_AMMA[2] + ".",
    segments=[seg("فَ", "fa", "conj"), seg("ظَنُّ", "zanna", "verb"), seg("و", "pron-3mp", "pron"), seg("هُ", "pron-3ms", "pron")]),
  tok("ضَعِيفَ", "daif", "noun", ["maful-bihi", "mafulayn", "zanna-wa-akhawatuha", "sifa-mushabbaha", "idafa-definiteness"],
    "مَفْعُولٌ بِهِ ثَانٍ لِـ«ظَنَّ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — صِفَةٌ مُشَبَّهَةٌ أُضِيفَتْ إِلَى مَا هُوَ فَاعِلُهَا فِي الْمَعْنَى.",
    "The SECOND object of ظَنَّ, in nasb and annexed — a ṣifa mushabbaha annexed to what is its doer in meaning («weak of memory» = «his memory is weak»).",
    "Zannetmek fiilinin ikinci mef'ûlü, mansûb, muzâf — mânâca fâili olan kelimeye muzâf sıfat-ı müşebbehe («ezberi zayıf»)."),
  MUDAF_ILAYH("الْحِفْظِ", "hifz", punct=".")]})

# =================================================== Chapter 3 — الْجَوَابُ ===================================================
S3 = []
S3.append({"id": "s1", "translation": {"en": "When al-Bukhārī knew that they had finished, he turned to the first man.",
                                      "tr": "Buhârî onların bitirdiğini anlayınca birinci adama döndü."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("عَلِمَ", "alima", ["zanna-wa-akhawatuha"], note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), BUKHARI_F(),
  tok("أَنَّهُمْ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna", "mawadi-fath-anna", "al-bariz-al-muttasil"],
    "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ «عَلِمَ».",
    "أَنَّ «that» builds a masdar; the attached «they» is its noun in the seat of nasb — the clause it builds stands for both objects of «knew».",
    "Enne masdar kurar; bitişik «onlar» ismi, mahallen mansûb — kurduğu müevvel masdar «bildi»nin iki mef'ûlünün yerini tutar.",
    segments=[seg("أَنَّ", "anna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  QAD(), VERB_WAW("فَرَغُوا", "faragha", punct="،", note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]),
  MADI("الْتَفَتَ", "iltafata", ["form-viii-verbs"], hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  ILA(), MAJR("الرَّجُلِ", "rajul"), NAAT("الْأَوَّلِ", "awwal", "jarr", punct=".")]})

S3.append({"id": "s2", "translation": {"en": "He related to him his first ḥadīth just as the man had asked him about it, then related it with its correct chain.",
                                      "tr": "Ona birinci hadisini, adamın kendisine sorduğu şekliyle rivayet etti; sonra onu sahih isnadıyla rivayet etti."},
 "tokens": [MADI_ALIF("فَرَوَى", "rawa", hidden=True), LAHU(" («ona»)"),
  ENC_NOUN("حَدِيثَهُ", "hadith", "هُ", "maful"), NAAT("الْأَوَّلَ", "awwal", "nasb"),
  KAMA(), ENC_MADI("سَأَلَهُ", "saala", "هُ", hidden=True,
    note_ar=" — وَالْفَاعِلُ يَعُودُ عَلَى الرَّجُلِ، وَالْهَاءُ عَلَى الْبُخَارِيِّ؛ وَالْجُمْلَةُ صِلَةُ مَا الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا",
    note_en="; the hidden doer is the man and «him» is al-Bukhārī; the clause is the ṣila of the masdar-making مَا and has no seat",
    note_tr="; gizli fâil adam, zamir Buhârî'dir; cümle masdariyye mâ'nın sılası, mahalli yoktur"),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan, onu»)", punct="،"),
  THUMMA(), ENC_MADI("رَوَاهُ", "rawa", "هُ", hidden=True, alif=True),
  BI_NOUN("بِإِسْنَادِهِ", "isnad-chain", "إِسْنَادِهِ", enc="هِ"), NAAT("الصَّحِيحِ", "sahih", "jarr", ["sifa-mushabbaha"], punct=".")]})

S3.append({"id": "s3", "translation": {"en": "Then he did the same with the second ḥadīth and the third, until he had finished them all.",
                                      "tr": "Sonra ikinci ve üçüncü hadisle de aynısını yaptı; nihayet hepsini bitirdi."},
 "tokens": [THUMMA(), MADI("فَعَلَ", "faala", hidden=True), DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", extra=["maful-bihi"]),
  BI_NOUN("بِالْحَدِيثِ", "hadith", "الْحَدِيثِ"),
  tok("الثَّانِي", "thani", "noun", ["naat-sifa", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ " + MANQUS[1] + MANQUS_NOTE[0] + ".", "An adjective agreeing with its noun, in jarr" + MANQUS_NOTE[1] + ".", "Na't, mevsûfuna uyar; mecrûr" + MANQUS_NOTE[2] + "."),
  tok("وَالثَّالِثِ", "thalith", "noun", ["atf-nasaq"], WA_AR + "الثَّالِثِ مَعْطُوفٌ عَلَى «الثَّانِي» مَجْرُورٌ بِالْكَسْرَةِ.", "The waw conjoins; «the third» is conjoined to «the second», in jarr.", "Vâv atıf; «üçüncü», «ikinci»ye ma'tûf, mecrûr.",
    punct="،", segments=[seg("وَ", "wa", "conj"), seg("الثَّالِثِ", "thalith", "noun")]),
  HATTA_IBT(), MADI("فَرَغَ", "faragha", hidden=True), JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)"),
  KULL_TAWKID("كُلِّهَا", "jarr", "هَا", "هَا", "them", "onlar", punct=".")]})

S3.append({"id": "s4", "translation": {"en": "He returned every text to its correct chain, without erring in any of them.",
                                      "tr": "Her metni sahih isnadına iade etti; bunların hiçbirinde hata etmiyordu."},
 "tokens": [MADI("فَرَدَّ", "radda", ["doubled-verbs"], hidden=True),
  MAFUL("كُلَّ", "kull", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("مَتْنٍ", "matn"),
  ILA(), ENC_NOUN("إِسْنَادِهِ", "isnad-chain", "هِ", "majr", note_ar=" — وَالْهَاءُ عَائِدٌ عَلَى «مَتْنٍ»", note_en=" — «its» returns to «text»", note_tr=" — zamir «metin»e döner"),
  NAAT("الصَّحِيحِ", "sahih", "jarr", ["sifa-mushabbaha"], punct="،"),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"), LA_NAFIYA(),
  MUDARI("يُخْطِئُ", "akhtaa", ["form-iv-verbs"], note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]),
  FI(), MAJR("شَيْءٍ", "shay"),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («onlardan»)", punct=".", note_ar=JAR_NAAT("jarr", "شَيْءٍ", "anything", "bir şey")[0], note_en=JAR_NAAT("jarr", "شَيْءٍ", "anything", "bir şey")[1], note_tr=JAR_NAAT("jarr", "شَيْءٍ", "anything", "bir şey")[2])]})

S3.append({"id": "s5", "translation": {"en": "Then he turned to the second man and did with him as he had done with the first.",
                                      "tr": "Sonra ikinci adama döndü ve ona da birinciye yaptığının aynısını yaptı."},
 "tokens": [THUMMA(), MADI("الْتَفَتَ", "iltafata", ["form-viii-verbs"], hidden=True), ILA(),
  MAJR("الثَّانِي", "thani", extra=["ism-maqsur-manqus"], sign=MANQUS[1], note_ar=MANQUS_NOTE[0], note_en=MANQUS_NOTE[1], note_tr=MANQUS_NOTE[2], punct="،"),
  MADI("فَصَنَعَ", "sanaa", hidden=True), BIHI(),
  MAFUL("مِثْلَ", "mithl", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A relative noun «what», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  MADI("صَنَعَ", "sanaa", hidden=True, note_ar=SILA[0] + "، وَالْعَائِدُ مَحْذُوفٌ: صَنَعَهُ", note_en=SILA[1] + "; the pronoun returning to مَا is dropped («did [it]»)", note_tr=SILA[2] + "; mevsûle dönen zamir hazfedilmiştir"),
  BI_NOUN("بِالْأَوَّلِ", "awwal", "الْأَوَّلِ", punct=".")]})

S3.append({"id": "s6", "translation": {"en": "He kept doing this with one man after another, until he had returned all hundred to their right form.",
                                      "tr": "Bunu adam ardına adam yapmaya devam etti; sonunda yüz hadisin hepsini doğru şekline döndürdü."},
 "tokens": [WA_MA(), ZALA(hidden=True), MUDARI("يَفْعَلُ", "faala", note_ar=KH_ZALA[0], note_en=KH_ZALA[1], note_tr=KH_ZALA[2]),
  DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", extra=["maful-bihi"]),
  BI_NOUN("بِرَجُلٍ", "rajul", "رَجُلٍ"),
  ZARF_BADA((" — مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٍ لِـ«رَجُلٍ»", "; it hangs on an omitted na't of «a man»", "; «adam»ın mahzûf na'tına müteallik")),
  MUDAF_ILAYH("رَجُلٍ", "rajul", punct="،"),
  HATTA_IBT(), MADI("رَدَّ", "radda", ["doubled-verbs"], hidden=True), MAFUL("الْمِائَةَ", "mia", extra=["asma-al-adad-fil-kafiya"]),
  KULL_TAWKID("كُلَّهَا", "nasb", "هَا", "الْمِائَةَ", "the hundred", "yüz"), ILA(),
  ENC_NOUN("صَوَابِهَا", "sawab", "هَا", "majr", punct=".")]})

S3.append({"id": "s7", "translation": {"en": "The people of the gathering fell silent in wonder at his memory.", "tr": "Meclistekiler onun ezberine hayretle sustular."},
 "tokens": [MADI("فَسَكَتَ", "sakata"), FAIL("أَهْلُ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْمَجْلِسِ", "majlis"),
  MAFUL_LAHU("تَعَجُّبًا", "taajjub"), MIN(),
  ENC_NOUN("حِفْظِهِ", "hifz", "هِ", "majr", punct=".", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«تَعَجُّبًا»", note_en=" — the jarr phrase attaches to «in wonder»", note_tr=" — câr-mecrûr «hayretle»ye müteallik")]})

# ================================================ Chapter 4 — بَعْدَ الْمَجْلِسِ ================================================
S4 = []
S4.append({"id": "s1", "translation": {"en": "Then the people acknowledged his merit, and bore witness to his memory with a testimony in which there is no doubt.",
                                      "tr": "Sonra insanlar onun faziletini kabul ettiler ve ezberine, hiç şüphe bulunmayan bir şahitlikle şahitlik ettiler."},
 "tokens": [THUMMA(), MADI("عَرَفَ", "arafa"), FAIL("النَّاسُ", "nas"), LAHU(" («onun için»)"),
  ENC_NOUN("فَضْلَهُ", "fadl", "هُ", "maful", punct="،"),
  VERB_WAW("وَشَهِدُوا", "shahida"), LAHU(" («onun lehine»)"), BI_NOUN("بِالْحِفْظِ", "hifz", "الْحِفْظِ"),
  MUTLAQ_NAW("شَهَادَةً", "shahada", "شَهِدَ", "bore witness", "şahitlik ettiler", how=("بِالْجُمْلَةِ الَّتِي بَعْدَهُ", "by the clause that qualifies it", "kendisinden sonraki cümleyle")),
  tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "jumla-sifa"],
    "لَا نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«شَهَادَةً».",
    "لَا that denies the whole genus («no … at all»), working like إِنَّ — the clause qualifies «a testimony», in the seat of nasb.",
    "Cinsini nefyeden lâ, inne gibi amel eder — cümle «şahitlik»in na'tı, mahallen mansûb."),
  tok("شَكَّ", "shakk", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.",
    "The noun of لَا, built on fatha (no tanwin), in the seat of nasb.", "Lâ'nın ismi, fetha üzere mebnî (tenvinsiz), mahallen mansûb."),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", punct=".",
    note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ لَا، وَالْهَاءُ عَائِدٌ عَلَى «شَهَادَةً»",
    note_en="; the jarr phrase hangs on the omitted predicate of لَا, and the pronoun returns to «a testimony»",
    note_tr="; câr-mecrûr lâ'nın mahzûf haberine müteallik; zamir «şahitlik»e döner")]})

S4.append({"id": "s2", "translation": {"en": "They had wanted to test him, and the test became a witness in his favour.",
                                      "tr": "Onu sınamak istemişlerdi; sınav ise onun lehine bir şahit oldu."},
 "tokens": [KANU("وَكَانُوا"), QAD(),
  VERB_WAW("أَرَادُوا", "arada", ["form-iv-verbs", "hollow-verbs"], note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«أَرَادُوا»", "; the clause it builds is the object of «wanted»", "; kurduğu müevvel masdar «istediler»in mef'ûlü"),
  FIVE_NASB_ENC("يَمْتَحِنُوهُ", "imtahana", "هُ", ["form-viii-verbs"], punct="،"),
  SARA("فَصَارَ"), tok("الِامْتِحَانُ", "imtihan", "noun", ["kana-wa-akhawatuha"], "اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of صَارَ, in raf'.", "Sâra'nın ismi, merfû."),
  tok("شَاهِدًا", "shahid", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ مِنْ شَهِدَ.", "The predicate of صَارَ, in nasb — the active participle of «to bear witness».", "Sâra'nın haberi, mansûb — şehide'nin ism-i fâili."),
  LAHU(" («onun lehine»)", punct=".")]})

S4.append({"id": "s3", "translation": {"en": "Ibn Ḥajar related this report at the beginning of his commentary on al-Bukhārī's book.",
                                      "tr": "İbn Hacer bu haberi, Buhârî'nin kitabına yazdığı şerhin başında rivayet etti."},
 "tokens": [MADI_ALIF("وَرَوَى", "rawa", note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili ondan sonra gelir"),
  PH(FAIL("ابْنُ", "ibn", note_ar=MUDAF[0] + " — وَ«ابْنُ حَجَرٍ» اسْمٌ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ اشْتُهِرَ بِهِ الْإِمَامُ الْعَسْقَلَانِيُّ", note_en=MUDAF[1] + " — «Ibn Ḥajar» is a name built as an idafa, by which al-ʿAsqalānī is known", note_tr=MUDAF[2] + " — «İbn Hacer» izâfet terkibiyle kurulmuş, el-Askalânî'nin meşhur olduğu addır"), "ibn-hajar"),
  MUDAF_ILAYH("حَجَرٍ", "hajar"),
  HADHA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", extra=["maful-bihi"]), BADAL("الْخَبَرَ", "khabar", "nasb"),
  FI(), MAJR("أَوَّلِ", "awwal", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), ENC_NOUN("شَرْحِهِ", "sharh", "هِ", "mudaf"),
  ALA(), MAJR("كِتَابِ", "kitab", note_ar=MUDAF[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«شَرْحِهِ»", note_en=MUDAF[1] + "; the jarr phrase attaches to «his commentary»", note_tr=MUDAF[2] + "; câr-mecrûr «şerhi»ne müteallik"),
  MUDAF_ILAYH("الْبُخَارِيِّ", "bukhari", "propn", punct=".")]})

S4.append({"id": "s4", "translation": {"en": "He explained that setting the error right was no wonder in a man like him in memory.",
                                      "tr": "Hatayı doğruya döndürmenin, ezberde onun gibi bir adam için şaşılacak bir şey olmadığını açıkladı."},
 "tokens": [MADI("وَبَيَّنَ", "bayyana", ["form-ii-verbs"], hidden=True),
  ANNA_T((" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«بَيَّنَ»", "; the clause it builds is the object of «explained»", "; kurduğu müevvel masdar «açıkladı»nın mef'ûlü")),
  tok("رَدَّ", "radd", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مَصْدَرُ رَدَّ.", "The noun of أَنَّ, in nasb and annexed — the masdar of «to return».", "Enne'nin ismi, mansûb, muzâf — redde'nin masdarı."),
  MUDAF_ILAYH("الْخَطَأِ", "khata", note_ar=" — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", note_en=" — the masdar is annexed to its object", note_tr=" — masdarın mef'ûlüne izâfeti"),
  ILA(), MAJR("الصَّوَابِ", "sawab"),
  LAYSA_T((" يَعُودُ عَلَى «رَدَّ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", ", returning to «setting» — the clause is the predicate of أَنَّ, in the seat of raf'", ", «döndürme»ye döner — cümle enne'nin haberi, mahallen merfû")),
  tok("بِعَجِيبٍ", "ajib", "noun", ["huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha", "sifa-mushabbaha"],
    "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَعَجِيبٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.",
    "The ba is an extra jarr letter that strengthens the negation; «a wonder» is the predicate of لَيْسَ — in jarr on the page, in nasb in its seat.",
    "Bâ, nefyi pekiştiren zâid cer harfi; «şaşılacak» leyse'nin haberi — lafzan mecrûr, mahallen mansûb.",
    segments=[seg("بِ", "bi", "prep"), seg("عَجِيبٍ", "ajib", "noun")]),
  MIN(), MAJR("رَجُلٍ", "rajul", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«عَجِيبٍ»", note_en=" — the jarr phrase attaches to «a wonder»", note_tr=" — câr-mecrûr «şaşılacak»a müteallik"),
  tok("مِثْلِهِ", "mithl", "noun", ["naat-sifa", "idafa-definiteness", "al-bariz-al-muttasil"],
    "نَعْتٌ لِـ«رَجُلٍ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَ«مِثْل» لَا يَتَعَرَّفُ بِالْإِضَافَةِ، فَصَحَّ أَنْ يَكُونَ نَعْتًا لِنَكِرَةٍ.",
    "A na't of «a man», in jarr and annexed to the pronoun in the seat of jarr — مِثْل does not become definite by annexation, so it can qualify an indefinite noun.",
    "«adam»ın na'tı, mecrûr; zamire muzâf, zamir mahallen mecrûr — misl izâfetle marife olmaz, bu yüzden nekirenin na'tı olabilir.",
    segments=[seg("مِثْلِ", "mithl", "noun"), seg("هِ", "pron-3ms", "pron")]),
  FI(), MAJR("الْحِفْظِ", "hifz", punct=".")]})

S4.append({"id": "s5", "translation": {"en": "But the wonder, in his view, is that he memorised the error in its order, though he had heard it only once.",
                                      "tr": "Ona göre asıl şaşılacak olan, hatayı sırasıyla ezberlemiş olmasıdır; üstelik onu yalnızca bir kez duymuştu."},
 "tokens": [tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"],
    WA_AR + "لٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
    "The waw conjoins; لٰكِنَّ «but» is the verb-like particle of correction: its noun in nasb, its predicate in raf'.",
    "«ve» + lâkinne: istidrâk harfi, fiile benzer; ismini nasb, haberini ref eder.",
    segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")]),
  tok("الْعَجِيبَ", "ajib", "noun", ["inna-wa-akhawatuha", "sifa-mushabbaha"], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of لٰكِنَّ, in nasb.", "Lâkinne'nin ismi, mansûb."),
  tok("عِنْدَهُ", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ هُنَا بِمَعْنَى «فِي رَأْيِهِ»، مُتَعَلِّقٌ بِـ«الْعَجِيبَ».",
    "An adverb «with him», in nasb and annexed to the pronoun in the seat of jarr — here «in his view»; it attaches to «the wonder».",
    "Zarf «onun yanında», mansûb; zamire muzâf, zamir mahallen mecrûr — burada «ona göre» anlamında; «şaşılacak»a müteallik.",
    segments=[seg("عِنْدَ", "inda", "noun"), seg("هُ", "pron-3ms", "pron")]),
  ANNAHU((" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ", "; the masdar it builds is the predicate of لٰكِنَّ, in the seat of raf'", "; kurduğu müevvel masdar lâkinne'nin haberi, mahallen merfû")),
  MADI("حَفِظَ", "hafiza", hidden=True, note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]), MAFUL("الْخَطَأَ", "khata"),
  ALA(), ENC_NOUN("تَرْتِيبِهِ", "tartib", "هِ", "majr", punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-hal-jumla-wa-rabituha"],
    "الْوَاوُ حَالِيَّةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَالْجُمْلَةُ بَعْدَهُمَا فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens a hal clause; لَمْ negates, governs jazm and turns the present to the past — the clause is a hal, in the seat of nasb.",
    "Hâl vâvı; lem: nefy, cezm ve kalb harfi — sonraki cümle hâl olarak mahallen mansûb.",
    segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يَسْمَعْهُ", "samia", "verb", ["nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "Present verb in jazm by لَمْ, its sign the sukun; the doer is a hidden pronoun «he», and the attached pronoun is its object, in the seat of nasb.",
    "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli zamir «o»; bitişik zamir mef'ûlün bih, mahallen mansûb.",
    segments=[seg("يَسْمَعْ", "samia", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"],
    "أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ لِأَنَّ الْكَلَامَ مَنْفِيٌّ، فَمَا بَعْدَهَا يَأْخُذُ إِعْرَابَهُ مِنْ مَوْقِعِهِ.",
    "إِلَّا «only, except» governs nothing here: the exception is «emptied» (mufarragh) because the sentence is negated — what follows takes the case its own position demands.",
    "İllâ burada amel etmez: cümle menfî olduğu için istisnâ müferrağdır — sonrası i'râbını kendi mevkiinden alır."),
  tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"],
    "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — مُبَيِّنٌ لِلْعَدَدِ، أَيْ: سَمَاعًا وَاحِدًا.",
    "Stands in for the absolute object, in nasb — it states the NUMBER of the act («once» = a single hearing).",
    "Mef'ûlün mutlakın nâibi, mansûb — fiilin sayısını bildirir («bir kez» = tek bir duyuş)."),
  NAAT("وَاحِدَةً", "wahid", "nasb", punct=".")]})

S4.append({"id": "s6", "translation": {"en": "In this report there is proof of the strength of memory that God gave him.",
                                      "tr": "Bu haberde, Allah'ın ona verdiği ezber gücüne bir delil vardır."},
 "tokens": [tok("وَفِي", "fi", "prep", ["huruf-jarr"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفِي حَرْفُ جَرٍّ.", "The waw opens a new sentence; فِي «in» is a jarr letter.", "Vâv isti'nâf içindir; fî «-de» — cer harfi.",
    segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")]),
  ISHARA("هٰذَا", "hadha", "جَرٍّ", "jarr", "mecrûr"),
  BADAL("الْخَبَرِ", "khabar", "jarr", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", note_en="; the jarr phrase is the FRONTED predicate", note_tr="; câr-mecrûr öne alınmış haberdir"),
  MUBTADA("دَلِيلٌ", "dalil-proof", note_ar=" — مُؤَخَّرٌ، وَجَازَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ شِبْهِ الْجُمْلَةِ",
    note_en=" — placed after its predicate; an indefinite mubtada is allowed because the jarr-phrase predicate comes first", note_tr=" — haberinden sonraya bırakılmış; câr-mecrûr haber öne geçtiği için nekire mübtedâ caizdir"),
  ALA(), tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِعَلَى.",
    "A relative noun «what», built on sukun, in the seat of jarr after عَلَى.", "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî, alâ ile mahallen mecrûr."),
  ENC_MADI("أَعْطَاهُ", "aata", "هُ", ["form-iv-verbs", "mafulayn"], alif=True,
    note_ar="، وَالْفَاعِلُ بَعْدَهُ" + SILA[0] + "، وَالْعَائِدُ مَحْذُوفٌ: أَعْطَاهُ إِيَّاهُ",
    note_en="; its doer follows" + SILA[1] + "; the pronoun returning to مَا, the second object, is dropped («gave him [it]»)",
    note_tr="; fâili ondan sonra gelir" + SILA[2] + "; mevsûle dönen ikinci mef'ûl hazfedilmiştir"),
  ALLAH_F(), MIN((" بَيَانِيٌّ يُبَيِّنُ «مَا»، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ", " that explains «what» (min of explanation); the jarr phrase is a hal of it, in the seat of nasb", " — beyâniyye: «mâ»yı açıklar; câr-mecrûr ondan hâl, mahallen mansûb")),
  MAJR("قُوَّةِ", "quwwa", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الْحِفْظِ", "hifz", punct=".")]})

S4.append({"id": "s7", "translation": {"en": "And the scholars have never ceased to relate this report, down to this day.", "tr": "Âlimler bu haberi bugüne kadar rivayet etmeye devam etmektedir."},
 "tokens": [WA_MA(), ZALA(),
  tok("أَهْلُ", "ahl", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ زَالَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of زَالَ, in raf', annexed.", "Zâle'nin ismi, merfû; muzâf."),
  MUDAF_ILAYH("الْعِلْمِ", "ilm"),
  MUDARI5("يَرْوُونَ", "rawa", extra=["naqis-verbs", "kana-wa-akhawatuha"], note_ar=" — وَحُذِفَتْ لَامُهُ (الْيَاءُ) لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ",
    note_en=" — its last radical, the ya, dropped where two quiescents met; the clause is the predicate of زَالَ, in the seat of nasb", note_tr=" — lâm'ı (yâ) iki sâkin karşılaşınca düştü; cümle zâle'nin haberi, mahallen mansûb"),
  HADHA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", extra=["maful-bihi"]), BADAL("الْخَبَرَ", "khabar", "nasb"), ILA(), MAJR("الْيَوْمِ", "yawm", punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf (the majority reading of a key wins) -------------------------
PKGS = sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
_M = {p: (json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
          if (ROOT / "content/samples" / p / "morphology.json").exists() else {}) for p in PKGS}
DIA_ = re.compile("[ً-ٰ]")
def _lemma_id(e): return DIA_.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))
# keys whose first majority holder carries a gloss written for another context — pinned to a package whose gloss is plain
FORCE = {"rajul": "jumal-al-tadrib", "hafiza": "jumal-al-tadrib", "kitab": "jumal-al-tadrib", "qama": "jumal-al-tadrib", "azim": "jumal-al-tadrib",
         "inda": "talkhis-al-miftah", "radd": "kitab-al-waqf", "majlis": "wasiyyat-abi-hanifa-samti", "ajaba": "wasiyyat-abi-yusuf-l5"}
def find_entry(k):
    """(gloss entry, owning package) — the reading of the key that most packages hold; ties go to the alphabetical first"""
    holders = [(p, _G[p][k]) for p in PKGS if k in _G[p]]
    if not holders: return None, None
    votes = collections.Counter(_lemma_id(e) for p, e in holders)
    best = votes.most_common(1)[0][0]
    group = [(p, e) for p, e in holders if _lemma_id(e) == best]
    if k in FORCE:
        pinned = [(p, e) for p, e in group if p == FORCE[k]]
        assert pinned, ("FORCE package does not hold the majority reading", k, FORCE[k])
        group = pinned + [g for g in group if g[0] != FORCE[k]]
    if group[0][1].get("pos") == "verb":
        for p, e in group:
            if k in _M[p]: return e, p
    return group[0][1], group[0][0]

def PHRASE(lemma, lvl, g_en, g_tr, l_en, l_tr, n_en, n_tr):
    return {"lemma": lemma, "pos": "phrase", "level": lvl, "gloss": {"en": g_en, "tr": g_tr}, "literal": {"en": l_en, "tr": l_tr}, "note": {"en": n_en, "tr": n_tr}}
NEW_GLOSS = {
 "bukhari": {"lemma": "الْبُخَارِيّ", "pos": "propn", "gloss": {"en": "al-Bukhārī — Imam Muḥammad ibn Ismāʿīl al-Bukhārī (d. 256 / 870), compiler of the Ṣaḥīḥ; a nisba to Bukhārā", "tr": "Buhârî — İmam Muhammed b. İsmâil el-Buhârî (ö. 256 / 870), Sahîh'in müellifi; Buhârâ'ya nispet"}, "level": 5},
 "baghdad": {"lemma": "بَغْدَاد", "pos": "propn", "gloss": {"en": "Baghdad — the ʿAbbāsid capital on the Tigris (a diptote: a feminine proper name)", "tr": "Bağdat — Dicle kıyısındaki Abbâsî başkenti (gayr-i munsarif: müennes özel isim)"}, "level": 4},
 "isnad-chain": {"lemma": "إِسْنَاد", "root": "س ن د", "pos": "noun", "plural": "أَسَانِيد", "gloss": {"en": "the chain of transmitters of a ḥadīth, its isnād (pl. أَسَانِيد)", "tr": "bir hadisin râvi zinciri, isnad (çoğ. esânîd)"}, "level": 5},
 "sharh": {"lemma": "شَرْح", "root": "ش ر ح", "pos": "noun", "plural": "شُرُوح", "gloss": {"en": "a commentary, an explanation (masdar of شَرَحَ; pl. شُرُوح)", "tr": "şerh, açıklama (şeraha'nın masdarı; çoğ. şürûh)"}, "level": 5},
 "ibn-hajar": PHRASE("ابْنُ حَجَرٍ", 5, "Ibn Ḥajar al-ʿAsqalānī (d. 852 / 1449), the great commentator on al-Bukhārī's Ṣaḥīḥ (Fatḥ al-Bārī, whose introduction is Hady al-Sārī)",
    "İbn Hacer el-Askalânî (ö. 852 / 1449), Buhârî'nin Sahîh'inin büyük şârihi (Fethu'l-Bârî; mukaddimesi Hedyü's-Sârî)",
    "literally «the son of a stone»", "lafzen «taşın oğlu»",
    "A name built as an idafa: ابْنُ carries the case of its seat, and حَجَرٍ is always in jarr — a three-letter masculine name, so it keeps its tanwin.",
    "İzâfetle kurulmuş bir addır: ابْنُ yerinin i'râbını taşır, حَجَرٍ daima mecrûrdur — üç harfli müzekker isim olduğu için tenvinini korur."),
}
for k in NEW_GLOSS:
    hit = [p for p in PKGS if k in _G[p]]
    assert not hit, ("a key is a global claim — already taken", k, hit)
used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
            if t.get("phrase"): used.add(t["phrase"]["lex"])
GLOSS, ORIGIN, missing = {}, {}, []
for k in sorted(used):
    if k in NEW_GLOSS:
        GLOSS[k] = NEW_GLOSS[k]; continue
    e, p = find_entry(k)
    if e is None: missing.append(k)
    else: GLOSS[k], ORIGIN[k] = e, p
assert not missing, missing
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    if k in ORIGIN and k in _M[ORIGIN[k]]: MORPH["verbs"][k] = _M[ORIGIN[k]][k]
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "الْبُخَارِيُّ فِي بَغْدَادَ", "en": "al-Bukhārī in Baghdad", "tr": "Buhârî Bağdat'ta"},
 "subtitle": {"ar": "عُلَمَاءُ بَغْدَادَ يَمْتَحِنُونَ حِفْظَ الْإِمَامِ بِمِائَةِ حَدِيثٍ مَقْلُوبَةِ الْأَسَانِيدِ — قِصَّةٌ لِلْمُسْتَوَى الْخَامِسِ",
              "en": "The scholars of Baghdad test the Imam's memory with a hundred ḥadīths whose chains they have turned about — a story for the fifth level",
              "tr": "Bağdat âlimleri, isnadlarını karıştırdıkları yüz hadisle İmamın ezberini sınar — beşinci seviye için bir hikâye"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى الْخَامِسُ) لِخَبَرِ امْتِحَانِ عُلَمَاءِ بَغْدَادَ حِفْظَ الْإِمَامِ الْبُخَارِيِّ بِمِائَةِ حَدِيثٍ قَلَبُوا أَسَانِيدَهَا وَمُتُونَهَا، كَمَا يَرْوِيهِ الْخَطِيبُ الْبَغْدَادِيُّ فِي «تَارِيخِ بَغْدَادَ»، وَابْنُ حَجَرٍ فِي «هَدْيِ السَّارِي». النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ هِيَ نَصُّ مَصْدَرٍ، وَلَا آيَةٌ، وَلَا نَصُّ حَدِيثٍ — فَالْأَحَادِيثُ الْمِائَةُ لَا تُسَمَّى؛ وَلَمْ يُتْرَكْ عَلَى لَفْظِ الْخَبَرِ إِلَّا جَوَابُ الْإِمَامِ الْقَصِيرُ «لَا أَعْرِفُهُ»، وَكَلَامُ ابْنِ حَجَرٍ مَحْكِيٌّ بِالْمَعْنَى.",
  "en": "ORIGINAL Level-5 graded Arabic: the report of how the scholars of Baghdad tested Imam al-Bukhārī's memory with a hundred ḥadīths whose chains and texts they had turned about, shared among ten men — told by al-Khaṭīb al-Baghdādī in Tārīkh Baghdād (in his notice on al-Bukhārī) and by Ibn Ḥajar in Hady al-Sārī, the introduction to Fatḥ al-Bārī — RETOLD FREELY as a retelling. No sentence is a quotation of a source; no verse is quoted and no ḥadīth text is quoted: the hundred ḥadīths stay unnamed. The one phrase kept as the reports give it is al-Bukhārī's two-word reply «lā aʿrifuhu» («I do not know it»); Ibn Ḥajar's remark that the wonder lies in his memorising the wrong order from a single hearing is given in reported speech, as a paraphrase. Only the well-attested core is told; the details of the setting (who the ten were, the exact wording of the onlookers' remarks) are left out.",
  "tr": "ÖZGÜN 5. seviye Arapça: Bağdat âlimlerinin, isnadlarını ve metinlerini birbirine karıştırıp on kişiye paylaştırdıkları yüz hadisle İmam Buhârî'nin ezberini sınamaları haberi — Hatîb el-Bağdâdî'nin Târîhu Bağdâd'ında (Buhârî maddesinde) ve İbn Hacer'in Fethu'l-Bârî mukaddimesi Hedyü's-Sârî'de anlatılır — SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir kaynaktan alıntı değildir; hiçbir âyet ve hiçbir hadis metni aktarılmamıştır: yüz hadisin hiçbiri anılmaz. Haberdeki lafzıyla korunan tek ifade, Buhârî'nin iki kelimelik cevabı «lâ a'rifuhû» («onu bilmiyorum»)dur; İbn Hacer'in, asıl şaşılacak şeyin hatalı sırayı tek dinleyişte ezberlemesi olduğu yolundaki sözü dolaylı anlatımla, mânâ olarak verilmiştir. Yalnız sağlam çekirdek anlatılmıştır; ortamın ayrıntıları (on kişinin kimler olduğu, seyircilerin sözlerinin lafzı) çıkarılmıştır.",
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
