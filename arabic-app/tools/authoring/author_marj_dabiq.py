"""Author content/samples/marj-dabiq — «مَرْجُ دَابِقَ», an ORIGINAL historical story at Level 5 (Advanced).

ORIGINAL graded Arabic, kept to the well-attested core of the years 922–923 AH / 1516–1517 CE as Ibn Iyās tells it in
Badāʾiʿ al-zuhūr fī waqāʾiʿ al-duhūr, with Ibn Ṭūlūn's Mufākahat al-khillān fī ḥawādith al-zamān for Syria: the Mamluks
rule Egypt and al-Shām; their sultan is the old al-Ghawrī, and the Ottomans of the lands of Rūm have a sultan named Selim;
discord falls between the two sultans; al-Ghawrī marches out of Egypt with his army and comes down at Aleppo, and Selim
marches against him; the two hosts meet at Marj Dābiq near Aleppo in 922; the Ottomans have many cannons; al-Ghawrī's army
is routed and he dies on the field; Selim enters Aleppo, then Damascus, and all al-Shām comes under his obedience, so that
only Egypt is left to the Mamluks; the emirs in Cairo raise the emir Ṭūmān Bāy to the rule; Selim marches on Egypt, the
sultan of Egypt waits for him at al-Raydāniyya near Cairo, fights, and is routed; Selim enters Cairo at the beginning of
923; the sultan of Egypt fights on for a while until he is taken captive, and then he is killed (one neutral line); the
state of the Mamluks ends and their lands pass into the hands of the Ottomans. It is RETOLD FREELY — no sentence is a
quotation from either chronicle, no āya or ḥadīth is quoted, no words are put in a historical person's mouth. Left out on
purpose: the transfer of the caliphate, every number of troops and dead, the manner of al-Ghawrī's death and the fate of
his body, the defection of emirs on the field, the date of the month of either battle, and every detail of Ṭūmān Bāy's
capture and death beyond the bare line that he was killed.

NAMES (only the five the brief certifies; every other person is «the sultan of Egypt», «the emirs»).
 سَلِيمٌ — an Arabic name (فَعِيل, the adjective «sound»), masculine with no second cause: fully declined, with tanwin.
 الْغَوْرِيُّ — a nisba title with the article: fully declined.
 مَرْجُ دَابِقَ — a place-name built as an idafa (carries the phrase key marj-dabiq, as the shelf's عَيْنُ جَالُوتَ does):
   مَرْج «meadow» (pl. مُرُوج, as in al-Masʿūdī's مُرُوجُ الذَّهَبِ) takes the case of its seat; دَابِق is a DIPTOTE, with no
   tanwin (مَرْجِ دَابِقَ) — the hoca's ruling of 2026-11-19; the first draft had declined it with tanwin.
 الرَّيْدَانِيَّةُ — a place-name with the article: fully declined.
 طُومَانَ بَايُ — a foreign compound name, analysed by the shelf's own doctrine of the blended compound (content/grammar,
   after the Kāfiya: «the first part built on fatḥa when it ends in a sound letter, the second declined as a diptote»):
   the first token طُومَانَ is built on fatḥa with no seat, the second بَايُ carries the case (ʿalamiyya + tarkīb mazjī +
   ʿujma). It stands only in raf'. Confirmed by the hoca, 2026-11-19.

Five chapters, twenty-eight sentences. The Level-5 constructions: the mafʿūl muṭlaq (قِتَالًا شَدِيدًا twice — once as the
deputy of اقْتِتَال — هَزِيمَةً شَدِيدَةً after a passive verb, خَوْفًا شَدِيدًا); the mafʿūl lahu (طَلَبًا لِسُلْطَانِهَا); tamyīz after
an elative (أَكْبَرَ مِنْ سَلِيمٍ سِنًّا); the istithnāʾ mufarragh (فَلَمْ يَبْقَ لِلْمَمَالِيكِ إِلَّا مِصْرُ); ṣifa and relative clauses
with their resumptive pronoun (يُقَالُ لَهُ twice, اسْمُهُ سَلِيمٌ, الْبِلَادُ الَّتِي مَلَكُوهَا); لَمَّا three times; حَتَّى + the
subjunctive (حَتَّى يَمْنَعَهُ) and حَتَّى opening a clause; لَامُ التَّعْلِيلِ + the subjunctive (لِيَدْفَعَ); wāw al-ḥāl (وَهُوَ شَيْخٌ
كَبِيرٌ), a ḥāl clause with no link (يَنْظُرُ) and a single ḥāl (أَسِيرًا); the fronted predicate of كَانَ (عَلَيْهِمْ، لِلْعُثْمَانِيِّينَ،
مَعَ الْعُثْمَانِيِّينَ); صَارَ, ظَلَّ and لَكِنَّ; كَمَا with مَا al-maṣdariyya; the passive past and present; the dual; numbers in a
date (اثْنَتَيْنِ وَعِشْرِينَ وَتِسْعِمِائَةٍ، ثَلَاثٍ وَعِشْرِينَ وَتِسْعِمِائَةٍ).

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf and every verb's paradigm
is the shelf's own (no new verb); the new entries are only those in NEW_GLOSS (the names, مَرْج, and the place-name phrase).
Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_marj_dabiq.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "marj-dabiq"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"هُمُ": "pron-3mp", "هِمْ": "pron-3mp", "هُمْ": "pron-3mp", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"هُمُ": "هُمْ", "هِمْ": "هُمْ", "هُمْ": "هُمْ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})

N = lambda s: unicodedata.normalize("NFC", s)
def PH(t, lex, span=2):
    """the name-phrase sits on the FIRST token of its span (CLAUDE.md «Idioms/phrases»): both words keep their own iʿrāb"""
    t["phrase"] = {"lex": lex, "span": span}
    return t
def W(*triples):
    """join note triples into the kit's note_ar / note_en / note_tr keywords"""
    out = ["", "", ""]
    for m in triples:
        out = [a + b for a, b in zip(out, m)]
    return dict(note_ar=out[0], note_en=out[1], note_tr=out[2])

MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
NAIB_BAAD = ("، وَنَائِبُ الْفَاعِلِ بَعْدَهُ", "; its deputy doer follows", "; nâib-i fâili ondan sonra gelir")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
KH_KANA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
HALCL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause is a hal, in the seat of nasb", "; cümle hâl olarak mahallen mansûb")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
KH_MUQ_J = (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate of كَانَ", "; câr-mecrûr kâne'nin öne alınmış haberine müteallik")
SALIM_W = ("بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", " — by the waw, a sound masculine plural", " — cem-i müzekker sâlim olduğu için vâv ile")
DIPT_TOWN = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town or a land), barred from tanwin", " — müennes özel isim (şehir ya da ülke), gayr-i munsarif")
NO_TANWIN = "بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ"
MAMALIK_NOTE = (" — جَمْعُ مَمْلُوكٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَظَهَرَتْ عَلَيْهِ الْكَسْرَةُ لِدُخُولِ أَلْ", " — the plural of «mamlūk» on the pattern of the farthest plurals (a diptote), here in jarr by the kasra because it carries the article", " — memlûk'ün cem'i, muntehe'l-cumû' vezninde (gayr-i munsarif); elif-lâm aldığı için kesre ile mecrûr")

# ---- the names --------------------------------------------------------------------------------------------------
SALIM_NOTE = (" — عَلَمٌ عَرَبِيٌّ مُذَكَّرٌ لَيْسَ فِيهِ إِلَّا الْعَلَمِيَّةُ، فَهُوَ مَصْرُوفٌ", " — an Arabic masculine name with no second cause besides being a name, so it is fully declined (with tanwin)", " — alemiyetten başka sebebi olmayan Arapça müzekker isim; bu yüzden munsarif (tenvinli)")
def SALIM(role, punct=None):
    """سَلِيمٌ — the sultan of the Ottomans: an Arabic name on فَعِيل, fully declined"""
    if role == "fail": return FAIL("سَلِيمٌ", "salim-sultan", "propn", **W(SALIM_NOTE), punct=punct)
    if role == "majr": return MAJR("سَلِيمٍ", "salim-sultan", "propn", **W(SALIM_NOTE), punct=punct)
    if role == "khabar_sifa":
        return tok("سَلِيمٌ", "salim-sultan", "propn", ["mubtada-khabar", "jumla-sifa"],
            "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ" + SALIM_NOTE[0] + " — وَالْجُمْلَةُ الِاسْمِيَّةُ «اسْمُهُ سَلِيمٌ» فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«سُلْطَانٌ».",
            "The predicate (khabar), in raf'" + SALIM_NOTE[1] + " — the nominal clause «his name is Selim» is a second na't of «a sultan», in the seat of raf'.",
            "Haber, merfû" + SALIM_NOTE[2] + " — «adı Selim» isim cümlesi «sultan»ın ikinci na'tı, mahallen merfû.", punct=punct)
    raise ValueError(role)
NISBA = (" — لَقَبٌ عَلَى صِيغَةِ النِّسْبَةِ دَخَلَتْهُ أَلْ", " — a title in the form of a nisba, carrying the article", " — elif-lâm almış nisbet sîgasında bir lakap")
def GHAWRI(role, punct=None):
    """الْغَوْرِيُّ — the sultan of Egypt: a nisba title with the article, fully declined"""
    if role == "fail": return FAIL("الْغَوْرِيُّ", "ghawri", "propn", ["ism-mansub"], **W(NISBA), punct=punct)
    if role == "mi": return MUDAF_ILAYH("الْغَوْرِيِّ", "ghawri", "propn", ["ism-mansub"], **W(NISBA), punct=punct)
    if role == "naib":
        return tok("الْغَوْرِيُّ", "ghawri", "propn", ["naib-al-fail", "ism-mansub"],
            "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ الِاسْمُ الْمَقُولُ نَفْسُهُ؛" + NISBA[0][2:] + ".",
            "The deputy doer of «is called», in raf' — the very name that is said;" + NISBA[1][2:] + ".",
            "«Denir»in nâib-i fâili, merfû — söylenen ismin kendisi;" + NISBA[2][2:] + ".", punct=punct)
    raise ValueError(role)
MAZJ = ("عَلَمٌ أَعْجَمِيٌّ مُرَكَّبٌ تَرْكِيبَ مَزْجٍ", "a foreign proper name built as a blended compound (tarkīb mazjī)", "mezcî terkiple kurulmuş yabancı özel isim")
def TUMANBAY(role, punct=None):
    """طُومَانَ بَايُ — the last Mamluk sultan: the shelf's doctrine of the blended compound (first part built on fatḥa, the
    second carries the case as a diptote); it stands only in raf'. Both tokens carry the key; the phrase sits on the first."""
    seat = {"badal": ("بَدَلٌ مِنَ «الْأَمِيرُ» مَرْفُوعٌ", "a badal of «the emir», in raf'", "«emîr»den bedel, merfû"),
            "naib": ("نَائِبُ فَاعِلٍ مَرْفُوعٌ", "the deputy doer of «was killed», in raf'", "«öldürüldü»nün nâib-i fâili, merfû")}[role]
    g = {"badal": ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"], "naib": ["naib-al-fail"]}[role]
    first = tok("طُومَانَ", "tumanbay", "propn", g + ["mamnu-min-sarf"],
        "صَدْرُ «طُومَانَ بَايُ»، وَهُوَ " + MAZJ[0] + ": صَدْرُهُ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ، وَالْإِعْرَابُ عَلَى عَجُزِهِ — وَالْعَلَمُ كُلُّهُ " + seat[0].split(" مَرْفُوعٌ")[0] + ".",
        "The first part of «Ṭūmān Bāy», " + MAZJ[1] + ": the first part is built on fatha and has no seat; the case falls on the second part — the whole name is " + seat[1].split(", in raf'")[0] + ".",
        "«Tûmân Bây»ın ilk parçası; " + MAZJ[2] + ": ilk parça fetha üzere mebnîdir, mahalli yoktur; i'râb ikinci parçadadır — ismin tamamı " + seat[2].split(", merfû")[0] + ".")
    second = tok("بَايُ", "tumanbay", "propn", g + ["mamnu-min-sarf"],
        "عَجُزُ «طُومَانَ بَايُ»، وَعَلَيْهِ إِعْرَابُ الْعَلَمِ كُلِّهِ: " + seat[0] + " بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّرْكِيبِ الْمَزْجِيِّ، وَهُوَ أَعْجَمِيٌّ.",
        "The second part of «Ṭūmān Bāy», which carries the case of the whole name: " + seat[1] + " by the damma with no tanwin — a diptote, being a proper name and a blended compound (and foreign).",
        "«Tûmân Bây»ın ikinci parçası; ismin tamamının i'râbı onun üzerindedir: " + seat[2] + ", tenvinsiz damme ile — alemiyet ve mezcî terkip sebebiyle gayr-i munsarif (ayrıca yabancı).", punct=punct)
    return [PH(first, "tumanbay"), second]

MISR_J = lambda punct=None, role="majr": (MAJR if role == "majr" else MUDAF_ILAYH)("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, **W(DIPT_TOWN), punct=punct)
HALAB_J = lambda punct=None: MAJR("حَلَبَ", "halab", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, **W(DIPT_TOWN), punct=punct)
UTHMANIYYUN_F = lambda punct=None: FAIL("الْعُثْمَانِيُّونَ", "uthmani", extra=["jam-mudhakkar-salim", "ism-mansub"], sign=SALIM_W[0], note_en=SALIM_W[1], note_tr=SALIM_W[2], punct=punct)
R_MI = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", "idafa-definiteness")
R_MAF = ("مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", "maful-bihi")
R_MAJR = ("مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", "huruf-jarr")
UTHMANIYYIN = lambda role, punct=None: SALIM_J("الْعُثْمَانِيِّينَ", "uthmani", role, extra=["ism-mansub"], punct=punct)

# ---- particles and frames the kit does not hold (most copied from the sister stories, author_ayn_jalut.py and
#      author_fath_al_qustantiniyya.py) ----------------------------------------------------------------------------
def TILKA(seat_ar, seat_en, seat_tr, punct=None):
    return tok("تِلْكَ", "tilka", "pron", ["asma-al-ishara"],
        "اسْمُ إِشَارَةٍ لِلْمُؤَنَّثِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "The feminine demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "Müennes işaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
DH_MI = ("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh")
def YUQALU(of_ar, of_en, of_tr, seat_ar, seat_en, seat_tr):
    """يُقَالُ لَهُ X: «who is called X» — a passive present whose clause qualifies the noun before it"""
    return tok("يُقَالُ", "qala", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "hollow-verbs", "jumla-sifa"],
        "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ " + seat_ar + " نَعْتٌ لِـ«" + of_ar + "».",
        "A present verb in the passive, in raf'; its deputy doer follows — the clause qualifies «" + of_en + "», in the seat of " + seat_en + ".",
        "Meçhul muzâri, merfû; nâib-i fâili sonra gelir — cümle «" + of_tr + "»ın na'tı, mahallen " + seat_tr + ".")
def LAHU_AID(of_ar, of_en, of_tr):
    return JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)", extra=["jumla-sifa"],
        note_ar=" — وَالْهَاءُ الْعَائِدُ الَّذِي يَرْبِطُ جُمْلَةَ النَّعْتِ بِـ«" + of_ar + "»",
        note_en="; «him/it» is the returning pronoun that ties the na't clause to «" + of_en + "»",
        note_tr="; «hû», na't cümlesini «" + of_tr + "»a bağlayan âid zamirdir")
JAMAN_F = lambda: tok("الْجَمْعَانِ", "jam", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ.",
    "The doer, in raf' by the alif — a dual («the two hosts»); its nun stands in for the tanwin of the singular.", "Fâil, tesniye olduğu için elif ile merfû («iki ordu»); nûn, müfred ismin tenvini yerinedir.")
QITAL_NAIB = lambda: tok("قِتَالًا", "qital", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
    "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «قَاتَلَ»، وَهُوَ يُلَاقِي «اقْتَتَلُوا» فِي مَادَّتِهِ وَمَعْنَاهُ فَنَابَ عَنْ مَصْدَرِهِ «اقْتِتَالًا»، وَبِنَعْتِهِ يُبَيِّنُ النَّوْعَ.",
    "Standing in for the absolute object, in nasb — the masdar of قَاتَلَ: it shares the root and the meaning of «fought one another» and takes the place of that verb's own masdar (اقْتِتَال); with its adjective it tells the KIND of fighting.",
    "Mef'ûlün mutlakın nâibi, mansûb — kâtele'nin masdarı: «birbirleriyle savaştılar» fiiliyle kökte ve anlamda buluştuğu için onun masdarının (iktitâl) yerini tuttu; sıfatıyla savaşın türünü bildirir.")
def MUTLAQ_X(full, lex, verb_ar, verb_en, verb_tr, punct=None, note=("", "", "")):
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «" + verb_ar + "»، يُؤَكِّدُ فِعْلَهُ، وَبِنَعْتِهِ يُبَيِّنُ نَوْعَهُ" + note[0] + ".",
        "The absolute object (maf'ul mutlaq), in nasb — the masdar of «" + verb_en + "»: it strengthens its verb, and with its adjective it tells the KIND" + note[1] + ".",
        "Mef'ûlün mutlak, mansûb — «" + verb_tr + "» fiilinin masdarı: fiilini pekiştirir, sıfatıyla da türünü bildirir" + note[2] + ".", punct=punct)
def MAFUL_LAHU(full, lex, punct=None, note_ar="", note_en="", note_tr=""):
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah", "masdar"],
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ" + note_ar + ".",
        "The maf'ul li-ajlih (object of cause), in nasb — a masdar giving the reason for the act, sharing its time and its doer" + note_en + ".",
        "Mef'ûlün lieclih, mansûb — fiilin sebebini bildiren masdar; fiille zamanda ve fâilde ortak" + note_tr + ".", punct=punct)
def MAA_KH(punct=None):
    """مَعَ before its noun, the whole the fronted predicate of كَانَ"""
    return tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"],
        "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ كَانَ مُقَدَّمٌ.",
        "An adverb «with», in nasb and annexed — the adverb phrase is the FRONTED predicate of كَانَ.",
        "«ile, yanında» — mekân zarfı, mansûb, muzâf — zarf, kâne'nin öne alınmış mahzûf haberine müteallik.", punct=punct)
def TISUMIA(punct=None):
    return tok("وَتِسْعِمِائَةٍ", "tisumia", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
        "الْوَاوُ عَاطِفَةٌ، وَ«تِسْعِ» مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ«مِائَةٍ» مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَجَاءَ «تِسْع» بِغَيْرِ تَاءٍ لِأَنَّ الْمِائَةَ مُؤَنَّثَةٌ، وَيُكْتَبُ الْجُزْآنِ كَلِمَةً وَاحِدَةً.",
        "The waw conjoins; «nine» is conjoined, in jarr and annexed, and «hundred» is its second term, in jarr — nine has no ta because «hundred» is feminine, and the two parts are written as one word.",
        "Vâv atıf; «dokuz» ma'tûf, mecrûr, muzâf; «yüz» muzâfun ileyh, mecrûr — «yüz» müennes olduğu için tis' tâsızdır; iki parça bitişik yazılır.",
        punct=punct, segments=[seg("وَ", "wa", "conj"), seg("تِسْعِمِائَةٍ", "tisumia", "noun")])
ISHRIN = lambda: ATF("وَعِشْرِينَ", "ishrun", "noun", "jarr", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
    note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr")
HATTA_KAY = lambda: tok("حَتَّى", "hatta", "part", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari", "ila-hatta-fi-wal-ba-fil-kafiya"],
    "حَرْفُ جَرٍّ بِمَعْنَى «كَيْ» لِلتَّعْلِيلِ، وَالْفِعْلُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى here means «so that» (purpose): a jarr letter after which an unspoken أَنْ must put the verb in nasb; the masdar so built is in jarr by حَتَّى.",
    "Hattâ burada «-sin diye» (ta'lîl) anlamında cer harfi; sonraki fiil vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr.")
QABLU = lambda punct=None: tok("قَبْلُ", "qablu", "noun", ["maful-fih", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "huruf-jarr"],
    "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ — قُطِعَ عَنِ الْإِضَافَةِ لَفْظًا وَنُوِيَ مَعْنَاهَا (أَيْ: مِنْ قَبْلِ ذٰلِكَ).",
    "An adverb of time built on damma, in the seat of jarr after مِنْ — cut off from its annexation in wording while its sense is kept («before that»).",
    "Zaman zarfı, damme üzere mebnî, min ile mahallen mecrûr — lafzen izâfetten kesilmiş, mânâsı niyet edilmiştir («ondan önce»).", punct=punct)

# ============================================ the text ============================================
TITLES = [{"ar": "سُلْطَانَانِ", "en": "Two Sultans", "tr": "İki Sultan"},
          {"ar": "يَوْمُ مَرْجِ دَابِقَ", "en": "The Day of Marj Dābiq", "tr": "Mercidâbık Günü"},
          {"ar": "الشَّامُ فِي يَدِ سَلِيمٍ", "en": "Al-Shām in Selim's Hand", "tr": "Şam Diyarı Selim'in Elinde"},
          {"ar": "يَوْمُ الرَّيْدَانِيَّةِ", "en": "The Day of al-Raydāniyya", "tr": "Ridâniye Günü"},
          {"ar": "نِهَايَةُ الدَّوْلَةِ", "en": "The End of a State", "tr": "Bir Devletin Sonu"}]

# ---- Chapter 1 — سُلْطَانَانِ ----
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "The Mamluks were the kings of Egypt and al-Shām (Syria) for a long time.",
  "tr": "Memlükler uzun zaman Mısır'ın ve Şam diyarının hükümdarlarıydı."},
 "tokens": [KANA("كَانَ"),
  ISMK("الْمَمَالِيكُ", "mamluk", extra=["jam-taksir"], note_ar=" — جَمْعُ مَمْلُوكٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ", note_en=" — the plural of «mamlūk», on the pattern of the farthest plurals", note_tr=" — memlûk'ün muntehe'l-cumû' vezninde cem'i"),
  KHK("مُلُوكَ", "malik-king", extra=["jam-taksir", "idafa-definiteness"], **W(MUDAF, (" — جَمْعُ مَلِكٍ", " — the plural of «king»", " — melik'in cem'i"))),
  MISR_J(role="mi"),
  ATF("وَالشَّامِ", "sham", "propn", "jarr"),
  ZARF("زَمَنًا", "zaman-period", mudaf=False, **ZAMAN),
  NAAT("طَوِيلًا", "tawil-long", "nasb", punct=".")]})
S1.append({"id": "s2", "translation": {
  "en": "Over them in those days was a sultan who was called al-Ghawrī.",
  "tr": "O günlerde başlarında, kendisine Gavrî denen bir sultan vardı."},
 "tokens": [KANA("وَكَانَ"),
  JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onların başında»)", extra=["kana-wa-akhawatuha"], **W(KH_MUQ_J)),
  FI(),
  TILKA("جَرٍّ بِفِي", "jarr after فِي", "mecrûr (fî ile)"),
  BADAL("الْأَيَّامِ", "yawm", "jarr", extra=["jam-taksir"], note_ar=" — جَمْعُ يَوْمٍ", note_en=" — the plural of «day»", note_tr=" — yevm'in cem'i"),
  ISMK("سُلْطَانٌ", "sultan", muakhkhar=True),
  YUQALU("سُلْطَانٌ", "a sultan", "sultan", "رَفْعٍ", "raf'", "merfû"),
  LAHU_AID("سُلْطَانٌ", "a sultan", "sultan"),
  GHAWRI("naib", punct=".")]})
S1.append({"id": "s3", "translation": {
  "en": "And the Ottomans, in the lands of Rūm (Anatolia), had another sultan, whose name was Selim.",
  "tr": "Osmanlıların da Rum diyarında, adı Selim olan başka bir sultanı vardı."},
 "tokens": [KANA("وَكَانَ"),
  tok("لِلْعُثْمَانِيِّينَ", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim", "ism-mansub", "kana-wa-akhawatuha"],
      "اللَّامُ حَرْفُ جَرٍّ لِلْمِلْكِ، وَالْعُثْمَانِيِّينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ" + KH_MUQ_J[0] + ".",
      "The lam is a jarr letter of possession («the Ottomans had»); «the Ottomans» after it is in jarr by the ya, a sound masculine plural" + KH_MUQ_J[1] + ".",
      "Lâm mülk bildiren cer harfi; «Osmanlılar» cem-i müzekker sâlim olduğu için yâ ile mecrûr" + KH_MUQ_J[2] + ".",
      segments=[seg("لِ", "li", "prep"), seg("الْعُثْمَانِيِّينَ", "uthmani", "noun")]),
  FI(),
  MAJR("بِلَادِ", "bilad", **W(MUDAF)),
  MUDAF_ILAYH("الرُّومِ", "rum", "propn", note_ar=" — وَبِلَادُ الرُّومِ هُنَا: الْأَنَاضُولُ", note_en=" — «the lands of Rūm» here are Anatolia", note_tr=" — Rum diyarı burada Anadolu'dur"),
  ISMK("سُلْطَانٌ", "sultan", muakhkhar=True),
  AKHAR_NAAT("آخَرُ", "raf"),
  ENC_NOUN("اسْمُهُ", "ism", "هُ", "mubtada", extra=["jumla-sifa"], note_ar=" — وَالْهَاءُ الْعَائِدُ الَّذِي يَرْبِطُ جُمْلَةَ النَّعْتِ بِـ«سُلْطَانٌ»", note_en="; «his» is the returning pronoun that ties the na't clause to «a sultan»", note_tr="; «hû», na't cümlesini «sultan»a bağlayan âid zamirdir"),
  SALIM("khabar_sifa", punct=".")]})
S1.append({"id": "s4", "translation": {
  "en": "Then discord fell between the two sultans, and al-Ghawrī went out of Egypt with his army, though he was an old man.",
  "tr": "Sonra iki sultanın arasına anlaşmazlık düştü; Gavrî de yaşlı bir adam olduğu hâlde ordusuyla Mısır'dan çıktı."},
 "tokens": [THUMMA(),
  MADI("وَقَعَ", "waqaa", ["mithal-verbs"], **W(FAIL_BAAD)),
  FAIL("الْخِلَافُ", "khilaf"),
  ZARF("بَيْنَ", "bayna"),
  MUDAF_ILAYH("السُّلْطَانَيْنِ", "sultan", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", note_ar="، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الْمُفْرَدِ", note_en=" — by the ya, being a dual; its nun stands in for the tanwin of the singular", note_tr=" — tesniye olduğu için yâ ile; nûn, müfredin tenvini yerinedir", punct="،"),
  MADI("فَخَرَجَ", "kharaja", **W(FAIL_BAAD)),
  GHAWRI("fail"),
  MIN(), MISR_J(),
  BI_NOUN("بِجَيْشِهِ", "jaysh", "جَيْشِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of company, «with»", note_tr=" — bâ musâhabe içindir, «ile»"),
  WA_HUWA_HAL(),
  KHABAR("شَيْخٌ", "shaykh"),
  NAAT("كَبِيرٌ", "kabir", "raf", punct=".")]})
S1.append({"id": "s5", "translation": {
  "en": "He was older than Selim in years.",
  "tr": "O, yaşça Selim'den büyüktü."},
 "tokens": [KANA_HID("وَكَانَ", note=("، يَعُودُ عَلَى الْغَوْرِيِّ", " (al-Ghawrī)", " (Gavrî)")),
  KHK("أَكْبَرَ", "akbar", extra=["ism-tafdil", "mamnu-min-sarf"], sign="بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ",
      note_ar=" — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", note_en=" with no tanwin — an elative, a diptote as an adjective on the verb's pattern", note_tr=", tenvinsiz — vasfiyet ve fiil vezni sebebiyle gayr-i munsarif ism-i tafdîl"),
  MIN(role=(" لِلْمُفَاضَلَةِ", " of comparison («than»)", " (mufâdale)")),
  SALIM("majr"),
  TAMYIZ("سِنًّا", "sinn", punct=".")]})
S1.append({"id": "s6", "translation": {
  "en": "He marched until he came down at Aleppo, and Selim marched against him with his armies.",
  "tr": "Yürüdü ve sonunda Halep'e kondu; Selim de ordularıyla onun üzerine yürüdü."},
 "tokens": [MADI("فَسَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  HATTA_IBT(),
  MADI("نَزَلَ", "nazala", hidden=True),
  BI_NOUN("بِحَلَبَ", "halab", "حَلَبَ", pos="propn", extra=["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_TOWN[0] + " — وَالْبَاءُ بِمَعْنَى فِي", note_en=DIPT_TOWN[1] + "; the ba here means «at»", note_tr=DIPT_TOWN[2] + "; bâ burada «-de» anlamındadır", punct="،"),
  MADI("وَسَارَ", "sara-travel", ["hollow-verbs"], **W(FAIL_BAAD)),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («onun üzerine»)"),
  SALIM("fail"),
  BI_NOUN("بِجُيُوشِهِ", "jaysh", "جُيُوشِهِ", enc="هِ", extra=["jam-taksir"], note_ar=" — جَمْعُ جَيْشٍ، وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the plural of «army»; the ba of company («with»)", note_tr=" — ceyş'in cem'i; bâ musâhabe içindir («ile»)", punct=".")]})

# ---- Chapter 2 — يَوْمُ مَرْجِ دَابِقَ ----
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "The two hosts met at a place near Aleppo which is called Marj Dābiq, «the Meadow of Dābiq».",
  "tr": "İki ordu Halep yakınında, kendisine Mercidâbık («Dâbık Çayırı») denen bir yerde karşılaştı."},
 "tokens": [MADI_ALIF("وَالْتَقَى", "iltaqa", ["form-viii-verbs"], **W(FAIL_BAAD)),
  JAMAN_F(),
  FI(), MAJR("مَوْضِعٍ", "mawdi"),
  NAAT("قَرِيبٍ", "qarib", "jarr"),
  MIN(), HALAB_J(),
  YUQALU("مَوْضِعٍ", "a place", "yer", "جَرٍّ", "jarr", "mecrûr"),
  LAHU_AID("مَوْضِعٍ", "a place", "yer"),
  PH(tok("مَرْجُ", "marj", "noun", ["naib-al-fail", "idafa-definiteness"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَهُوَ الِاسْمُ الْمَقُولُ نَفْسُهُ، وَ«مَرْجُ دَابِقَ» اسْمُ مَوْضِعٍ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ.",
      "The deputy doer of «is called», in raf' and annexed — the very name that is said; «Marj Dābiq» is a place-name built as an idafa.",
      "«Denir»in nâib-i fâili, merfû, muzâf — söylenen ismin kendisi; «Mercidâbık» izâfetle kurulmuş bir yer adıdır."), "marj-dabiq"),
  MUDAF_ILAYH("دَابِقَ", "dabiq", "propn", extra=["mamnu-min-sarf"], sign="بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ", note_ar=" — اسْمُ مَوْضِعٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ، فَلَا يُنَوَّنُ", note_en="; its sign is the fatha standing for the kasra — a place-name barred from tanwin (a proper name, feminine as a place)", note_tr="; alâmeti kesreden nâib fethadır — yer adı olarak gayr-i munsarif (alemiyet ve te'nîs), tenvin almaz", punct=".")]})
S2.append({"id": "s2", "translation": {
  "en": "That was in the year nine hundred and twenty-two.",
  "tr": "Bu, dokuz yüz yirmi iki yılında oldu."},
 "tokens": [KANA("وَكَانَ"),
  DHALIKA("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi", extra=["kana-wa-akhawatuha"]),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", "; the jarr phrase hangs on the omitted predicate of كَانَ", " — câr-mecrûr kâne'nin mahzûf haberine müteallik")),
  MAJR("سَنَةِ", "sana", **W(MUDAF)),
  MUDAF_ILAYH("اثْنَتَيْنِ", "ithnatan", extra=["asma-al-adad-fil-kafiya", "al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى",
      note_ar=" — وَجَاءَ مُؤَنَّثًا لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ: الْوَاحِدُ وَالِاثْنَانِ يُوَافِقَانِ الْمَعْدُودَ",
      note_en=" — by the ya, declined like a dual; it is feminine because the thing counted, «year», is feminine: one and two agree with what they count",
      note_tr=" — müsenâya mülhak olduğu için yâ ile; ma'dûd «sene» müennes olduğu için müennes geldi: bir ve iki ma'dûduna uyar"),
  ISHRIN(), TISUMIA(punct=".")]})
S2.append({"id": "s3", "translation": {
  "en": "They fought one another fiercely, and the Ottomans had many cannons with them.",
  "tr": "Şiddetle çarpıştılar; Osmanlıların yanında da birçok top vardı."},
 "tokens": [VERB_WAW("فَاقْتَتَلُوا", "iqtatala", ["form-viii-verbs"]), QITAL_NAIB(), NAAT("شَدِيدًا", "shadid", "nasb", punct="،"),
  KANA("وَكَانَتْ", fem=True),
  MAA_KH(),
  UTHMANIYYIN(R_MI),
  ISMK("مَدَافِعُ", "midfa", extra=["mamnu-min-sarf", "jam-taksir"], muakhkhar=True,
       note_ar=" بِلَا تَنْوِينٍ — جَمْعُ مِدْفَعٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَنَّهُ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ (مَفَاعِل)؛ وَأُنِّثَ الْفِعْلُ لِأَنَّهُ جَمْعُ تَكْسِيرٍ", note_en=" without tanwin — the plural of «cannon», a diptote on the furthest-plural pattern مَفَاعِل; the verb is feminine because it is a broken plural", note_tr=" tenvinsiz — midfa'ın cemi; müntehe'l-cumû' sîgasında (mefâil) olduğu için gayr-i munsarif; kırık çoğul olduğu için fiil müennes geldi"),
  NAAT("كَثِيرَةٌ", "kathir", "raf", note_ar=" — جَمْعُ مَا لَا يَعْقِلُ يُوصَفُ بِالْمُفْرَدِ الْمُؤَنَّثِ", note_en=" — a plural of things is described by a feminine singular", note_tr=" — akılsız varlıkların cemi müfred müennesle vasıflanır", punct=".")]})
S2.append({"id": "s4", "translation": {
  "en": "Then al-Ghawrī's army was routed — a heavy rout.",
  "tr": "Sonra Gavrî'nin ordusu ağır bir yenilgiye uğratıldı."},
 "tokens": [THUMMA(),
  MAJHUL("هُزِمَ", "hazama", ["thulathi-mujarrad-babs"], **W(NAIB_BAAD)),
  NAIB("جَيْشُ", "jaysh", **W(MUDAF)),
  GHAWRI("mi"),
  MUTLAQ_X("هَزِيمَةً", "hazima", "هَزَمَ", "to rout", "bozguna uğratmak", note=(" — وَيَنْصِبُهُ الْفِعْلُ الْمَبْنِيُّ لِلْمَجْهُولِ كَمَا يَنْصِبُهُ الْمَبْنِيُّ لِلْمَعْلُومِ", "; a passive verb governs its masdar just as the active does", "; meçhul fiil de ma'lûm gibi masdarını nasb eder")),
  NAAT("شَدِيدَةً", "shadid", "nasb", punct=".")]})
S2.append({"id": "s5", "translation": {
  "en": "And al-Ghawrī died on the field of battle, and he never went back to Egypt.",
  "tr": "Gavrî savaş yerinde öldü ve Mısır'a bir daha dönmedi."},
 "tokens": [MADI("وَمَاتَ", "mata-die", ["hollow-verbs"], **W(FAIL_BAAD)),
  GHAWRI("fail"),
  FI(), MAJR("مَوْضِعِ", "mawdi", **W(MUDAF)), MUDAF_ILAYH("الْقِتَالِ", "qital", extra=["masdar"], punct="،"),
  WA_LAM(),
  JAZM_V("يَرْجِعْ", "rajaa", ["lam-jazim"], hidden="هُوَ"),
  ILA(), MISR_J(punct=".")]})
S2.append({"id": "s6", "translation": {
  "en": "When the fighting was over, Selim entered Aleppo.",
  "tr": "Savaş bitince Selim Halep'e girdi."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI_ALIF("انْتَهَى", "intaha", ["form-viii-verbs"], **W(FAIL_BAAD, LAMMA_CL)),
  FAIL("الْقِتَالُ", "qital", extra=["masdar"], punct="،"),
  MADI("دَخَلَ", "dakhala", **W(FAIL_BAAD, JAWAB_LAMMA)),
  SALIM("fail"),
  MAFUL("حَلَبَ", "halab", "propn", ["mamnu-min-sarf"], sign=NO_TANWIN,
        note_ar=DIPT_TOWN[0] + " — وَقِيلَ: مَنْصُوبٌ عَلَى التَّوَسُّعِ بِنَزْعِ الْخَافِضِ (دَخَلَ فِي حَلَبَ)",
        note_en=DIPT_TOWN[1] + " (some read it as in nasb by the dropping of the jarr letter: «entered into Aleppo»)",
        note_tr=DIPT_TOWN[2] + " (bir görüşe göre cer harfinin hazfiyle mansûbdur: «Halep'in içine girdi»)", punct=".")]})

# ---- Chapter 3 — الشَّامُ فِي يَدِ سَلِيمٍ ----
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "Then he marched to Damascus and entered it, and stayed there a while, looking into the affairs of its people.",
  "tr": "Sonra Dımaşk'a yürüdü ve oraya girdi; halkının işlerine bakarak bir süre orada kaldı."},
 "tokens": [THUMMA(),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  ILA(), MAJR("دِمَشْقَ", "dimashq", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, **W(DIPT_TOWN)),
  ENC_MADI("فَدَخَلَهَا", "dakhala", "هَا", ["thulathi-mujarrad-babs"], hidden=True, punct="،"),
  MADI("وَأَقَامَ", "aqama", ["form-iv-verbs", "hollow-verbs"], hidden=True),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)", note_ar=" — وَالْبَاءُ بِمَعْنَى فِي", note_en="; the ba here means «in»", note_tr="; bâ burada «-de» anlamındadır"),
  ZARF("مُدَّةً", "mudda", mudaf=False, **ZAMAN),
  MUDARI("يَنْظُرُ", "nazara", ["thulathi-mujarrad-babs", "hal", "al-hal-jumla-wa-rabituha"], **W(HALCL)),
  FI(), MAJR("أُمُورِ", "amr", extra=["jam-taksir"], **W(MUDAF, (" — جَمْعُ أَمْرٍ", " — the plural of «affair»", " — emr'in cem'i"))),
  ENC_NOUN("أَهْلِهَا", "ahl", "هَا", "mudaf", note_ar=" — وَالضَّمِيرُ لِدِمَشْقَ", note_en=" — «its» is Damascus", note_tr=" — zamir Dımaşk'a döner", punct=".")]})
S3.append({"id": "s2", "translation": {
  "en": "And the lands of al-Shām, all of them, came under his obedience.",
  "tr": "Şam diyarının tamamı onun itaatine girdi."},
 "tokens": [MADI("وَدَخَلَتْ", "dakhala", fem=True, **W(FAIL_BAAD)),
  FAIL("بِلَادُ", "bilad", **W(MUDAF, (" — وَهُوَ جَمْعُ تَكْسِيرٍ، فَجَازَ تَأْنِيثُ فِعْلِهِ", " — a broken plural, so its verb may take the feminine", " — kırık çoğul; bu yüzden fiilinin müennes gelmesi caizdir"))),
  MUDAF_ILAYH("الشَّامِ", "sham", "propn"),
  tok("كُلُّهَا", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
      "تَوْكِيدٌ مَعْنَوِيٌّ لِـ«بِلَادُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يَعُودُ عَلَى الْبِلَادِ.",
      "A tawkid of meaning «all of them», strengthening «the lands», in raf' like them; annexed to the attached pronoun (the lands), which fills the seat of jarr.",
      "«Bilâd»ın ma'nevî te'kîdi «hepsi», onun gibi merfû; bitişik zamire (diyarlar) muzâf, zamir mahallen mecrûr.",
      segments=[seg("كُلُّ", "kull", "noun"), seg("هَا", "pron-3fs", "pron")]),
  FI(), ENC_NOUN("طَاعَتِهِ", "taa", "هِ", "majr", note_ar=" — وَالضَّمِيرُ لِسَلِيمٍ", note_en=" — «his» is Selim", note_tr=" — zamir Selim'e döner", punct=".")]})
S3.append({"id": "s3", "translation": {
  "en": "So nothing was left to the Mamluks but Egypt.",
  "tr": "Böylece Memlüklere Mısır'dan başka bir şey kalmadı."},
 "tokens": [LAM_JAZM("فَلَمْ"),
  tok("يَبْقَ", "baqiya", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (يَبْقَى ← لَمْ يَبْقَ)، وَالْفَاعِلُ بَعْدَ إِلَّا.",
      "Present verb in jazm after لَمْ, its sign the dropped weak letter (يَبْقَى → لَمْ يَبْقَ); its doer comes after إِلَّا.",
      "Lem ile meczûm muzâri; alâmeti illet harfinin hazfi (yebkâ → lem yebka); fâili illâ'dan sonra gelir."),
  LI_AL("لِلْمَمَالِيكِ", "mamluk", "الْمَمَالِيكِ", extra=["jam-taksir"], note_ar=MAMALIK_NOTE[0] + "؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَبْقَ»", note_en=MAMALIK_NOTE[1] + "; the phrase hangs on «was left»", note_tr=MAMALIK_NOTE[2] + "; câr-mecrûr «kaldı»ya müteallik"),
  ILLA(),
  FAIL("مِصْرُ", "misr", "propn", ["mamnu-min-sarf", "istithna-mufarragh"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ",
       note_ar=DIPT_TOWN[0] + " — وَالِاسْتِثْنَاءُ مُفَرَّغٌ، فَهُوَ فَاعِلُ «يَبْقَ»", note_en=", with no tanwin" + DIPT_TOWN[1] + " — the exception is emptied, so it is the doer of «was left»", note_tr=", tenvinsiz" + DIPT_TOWN[2] + " — istisnâ müferrağdır, «kaldı»nın fâilidir", punct=".")]})
S3.append({"id": "s4", "translation": {
  "en": "When the news of al-Ghawrī's death reached the people of Egypt, they feared the Ottomans with a great fear.",
  "tr": "Gavrî'nin ölüm haberi Mısır halkına ulaşınca Osmanlılardan şiddetle korktular."},
 "tokens": [LAMMA2("وَلَمَّا"),
  MADI("بَلَغَ", "balagha", **W(FAIL_BAAD, LAMMA_CL)),
  MAFUL("أَهْلَ", "ahl", **W(MUDAF, (" — قُدِّمَ عَلَى الْفَاعِلِ", " — placed before the doer", " — fâilden önce getirilmiştir"))),
  MISR_J(role="mi"),
  FAIL("خَبَرُ", "khabar-news", **W(MUDAF)),
  MUDAF_ILAYH("مَوْتِ", "mawt", **W(MUDAF)),
  GHAWRI("mi", punct="،"),
  VERB_WAW("خَافُوا", "khafa", ["hollow-verbs"], **W(JAWAB_LAMMA)),
  MINA(), UTHMANIYYIN(R_MAJR),
  MUTLAQ_X("خَوْفًا", "khawf", "خَافَ", "to fear", "korkmak"),
  NAAT("شَدِيدًا", "shadid", "nasb", punct=".")]})
S3.append({"id": "s5", "translation": {
  "en": "The emirs gathered in Cairo, and after al-Ghawrī the emir Ṭūmān Bāy took up the rule.",
  "tr": "Emîrler Kahire'de toplandı; Gavrî'den sonra işi emîr Tûmân Bây üstlendi."},
 "tokens": [MADI("وَاجْتَمَعَ", "ijtamaa", ["form-viii-verbs"], **W(FAIL_BAAD)),
  FAIL("الْأُمَرَاءُ", "amir", extra=["jam-taksir"], note_ar=" — جَمْعُ أَمِيرٍ عَلَى فُعَلَاءَ", note_en=" — the plural of «emir», on the pattern فُعَلَاء", note_tr=" — emîr'in fu'alâ vezninde cem'i"),
  FI(), MAJR("الْقَاهِرَةِ", "qahira", "propn", punct="،"),
  MADI("فَقَامَ", "qama", ["hollow-verbs"], **W(FAIL_BAAD)),
  BI_NOUN("بِالْأَمْرِ", "amr", "الْأَمْرِ", note_ar=" — وَقَامَ بِالْأَمْرِ: تَوَلَّاهُ وَنَهَضَ بِهِ", note_en=" — «to rise WITH the matter» is to take it up, to take charge of the rule", note_tr=" — «işle kalktı»: onu üstlendi, yönetimi eline aldı"),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  GHAWRI("mi"),
  FAIL("الْأَمِيرُ", "amir"),
  *TUMANBAY("badal", punct=".")]})
S3.append({"id": "s6", "translation": {
  "en": "So he became sultan over Egypt, and he gathered the troops to drive the Ottomans back from it.",
  "tr": "Böylece Mısır'a sultan oldu ve Osmanlıları oradan geri püskürtmek için askerleri topladı."},
 "tokens": [tok("فَصَارَ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
      FA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى طُومَانَ بَايَ.",
      "The fa carries the story on; صَارَ «became» is one of كَانَ's sisters, built on fatha; its noun is the hidden «he» (Ṭūmān Bāy).",
      "«bunun üzerine» + sâra «oldu»: kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; ismi gizli zamir «o» (Tûmân Bây).",
      segments=[seg("فَ", "fa", "conj"), seg("صَارَ", "sara", "verb")]),
  tok("سُلْطَانًا", "sultan", "noun", ["kana-wa-akhawatuha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of صَارَ, in nasb.", "Sâra'nın haberi, mansûb."),
  ALA(), MISR_J(punct="،"),
  MADI("وَجَمَعَ", "jamaa-gather", hidden=True),
  MAFUL("الْجُنُودَ", "jund", extra=["jam-taksir"], note_ar=" — جَمْعُ جُنْدٍ", note_en=" — the plural of «troop»", note_tr=" — cünd'ün cem'i"),
  tok("لِيَدْفَعَ", "dafaa", "verb", ["nawasib-wa-jawazim-al-mudari", "an-masdariyya", "huruf-jarr"],
      "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَيَدْفَعَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ جَوَازًا بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَمَعَ».",
      "The lam of purpose is a jarr letter; the present verb after it is in nasb by an أَنْ that may stay hidden after the lam, its sign the fatha; the doer «he» is hidden — the masdar they build is in jarr by the lam, and the phrase hangs on «gathered».",
      "Lâm ta'lîl lâmı, cer harfi; sonraki muzâri lâmdan sonra cevâzen gizli en ile mansûb, alâmeti fetha; fâil gizli zamir «o» — müevvel masdar lâm ile mecrûr, câr-mecrûr «topladı»ya müteallik.",
      segments=[seg("لِ", "li", "prep"), seg("يَدْفَعَ", "dafaa", "verb")]),
  UTHMANIYYIN(R_MAF),
  JARR_PRON("عَنْهَا", "an", "عَنْ", "هَا", " («ondan»)", note_ar=" — وَالضَّمِيرُ لِمِصْرَ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَدْفَعَ»", note_en="; «it» is Egypt, and the phrase hangs on «drive back»", note_tr="; zamir Mısır'a döner, câr-mecrûr «def etmek»e müteallik", punct=".")]})

# ---- Chapter 4 — يَوْمُ الرَّيْدَانِيَّةِ ----
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "Then Selim marched with his armies on Egypt, in pursuit of its sultan, until he drew near Cairo.",
  "tr": "Sonra Selim, sultanının peşine düşerek ordularıyla Mısır'a yürüdü; sonunda Kahire'ye yaklaştı."},
 "tokens": [THUMMA(),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"], **W(FAIL_BAAD)),
  SALIM("fail"),
  BI_NOUN("بِجُيُوشِهِ", "jaysh", "جُيُوشِهِ", enc="هِ", extra=["jam-taksir"], note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of company («with»)", note_tr=" — bâ musâhabe içindir («ile»)"),
  ILA(), MISR_J(),
  MAFUL_LAHU("طَلَبًا", "talab"),
  LI_ENC("لِسُلْطَانِهَا", "sultan", "سُلْطَانِ", "هَا", note_ar=" — وَاللَّامُ تُقَوِّي عَمَلَ الْمَصْدَرِ فِي مَفْعُولِهِ، وَالضَّمِيرُ لِمِصْرَ", note_en="; the lam strengthens the masdar's hold on its object, and «its» is Egypt", note_tr="; lâm masdarın mef'ûlündeki amelini kuvvetlendirir; zamir Mısır'a döner", punct="،"),
  HATTA_IBT(),
  MADI("قَرُبَ", "qaruba", hidden=True),
  MINA(), MAJR("الْقَاهِرَةِ", "qahira", "propn", punct=".")]})
S4.append({"id": "s2", "translation": {
  "en": "The sultan of Egypt had camped with his army at al-Raydāniyya, so that he might keep him from entering Cairo.",
  "tr": "Mısır sultanı da onu Kahire'ye girmekten alıkoymak için ordusuyla Ridâniye'de konaklamıştı."},
 "tokens": [KANA("وَكَانَ"),
  ISMK("سُلْطَانُ", "sultan", **W(MUDAF)),
  MISR_J(role="mi"),
  QAD(),
  MADI("نَزَلَ", "nazala", hidden=True, **W(KH_KANA)),
  BI_NOUN("بِجَيْشِهِ", "jaysh", "جَيْشِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of company, «with»", note_tr=" — bâ musâhabe içindir, «ile»"),
  FI(), MAJR("الرَّيْدَانِيَّةِ", "raydaniyya", "propn", note_ar=" — اسْمُ مَوْضِعٍ قُرْبَ الْقَاهِرَةِ دَخَلَتْهُ أَلْ", note_en=" — a place-name near Cairo, carrying the article", note_tr=" — Kahire yakınında, elif-lâm almış bir yer adı", punct="،"),
  HATTA_KAY(),
  tok("يَمْنَعَهُ", "manaa", "verb", ["nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى سُلْطَانِ مِصْرَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَهِيَ لِسَلِيمٍ.",
      "Present verb in nasb by an أَنْ hidden of necessity after حَتَّى, its sign the fatha; the doer «he» (the sultan of Egypt) is hidden, and the attached «him» (Selim) is its object, in the seat of nasb.",
      "Hattâ'dan sonra vücûben gizli en ile mansûb muzâri, alâmeti fetha; fâil gizli zamir «o» (Mısır sultanı); bitişik «onu» (Selim'i) mef'ûlün bih, mahallen mansûb.",
      segments=[seg("يَمْنَعَ", "manaa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  MIN(), MAJR("دُخُولِ", "dukhul", extra=["masdar"], **W(MUDAF, (" — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ", " — a masdar annexed to its object", " — mef'ûlüne muzâf masdar"))),
  MUDAF_ILAYH("الْقَاهِرَةِ", "qahira", "propn", punct=".")]})
S4.append({"id": "s3", "translation": {
  "en": "When the Ottomans reached him, he fought them fiercely.",
  "tr": "Osmanlılar ona ulaşınca onlarla şiddetle çarpıştı."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI("وَصَلَ", "wasala", ["mithal-verbs"], **W(FAIL_BAAD, LAMMA_CL)),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)"),
  UTHMANIYYUN_F(punct="،"),
  ENC_MADI("قَاتَلَهُمْ", "qatala-fight", "هُمْ", ["form-iii-verbs"], hidden=True, **W(JAWAB_LAMMA)),
  MUTLAQ_X("قِتَالًا", "qital", "قَاتَلَ", "to fight", "çarpışmak"),
  NAAT("شَدِيدًا", "shadid", "nasb", punct=".")]})
S4.append({"id": "s4", "translation": {
  "en": "But his army was routed, just as al-Ghawrī's army had been routed before.",
  "tr": "Fakat onun ordusu da, daha önce Gavrî'nin ordusu bozguna uğratıldığı gibi bozguna uğratıldı."},
 "tokens": [tok("وَلَكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha"],
      WA_AR + "لَكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "The waw conjoins; لَكِنَّ «but» is the verb-like particle of correction: it puts its noun in nasb and raises its predicate.",
      "«ve» + lâkinne «fakat»: istidrâk bildiren, fiile benzeyen harf; ismini nasb, haberini ref eder.",
      segments=[seg("وَ", "wa", "conj"), seg("لَكِنَّ", "lakinna", "part")]),
  tok("جَيْشَهُ", "jaysh", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"],
      "اسْمُ لَكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The noun of لَكِنَّ, in nasb; annexed to the attached «his», which fills the seat of jarr.",
      "Lâkinne'nin ismi, mansûb; bitişik zamire muzâf, zamir mahallen mecrûr.",
      segments=[seg("جَيْشَ", "jaysh", "noun"), seg("هُ", "pron-3ms", "pron")]),
  MAJHUL("هُزِمَ", "hazama", ["thulathi-mujarrad-babs"], note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى الْجَيْشِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَكِنَّ",
      note_en="; its deputy doer is the hidden «it» (the army) — the clause is the predicate of لَكِنَّ, in the seat of raf'", note_tr="; nâib-i fâil orduya dönen gizli zamir «o» — cümle lâkinne'nin haberi, mahallen merfû"),
  KAMA(),
  MAJHUL("هُزِمَ", "hazama", ["thulathi-mujarrad-babs"], note_ar=NAIB_BAAD[0] + " — وَالْجُمْلَةُ صِلَةُ مَا الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ",
      note_en=NAIB_BAAD[1] + " — the clause is the ṣila of the masdar-making مَا and has no seat of its own", note_tr=NAIB_BAAD[2] + " — cümle masdariyye mâ'nın sılasıdır, i'râbdan mahalli yoktur"),
  NAIB("جَيْشُ", "jaysh", **W(MUDAF)),
  GHAWRI("mi"),
  MIN(), QABLU(punct=".")]})
S4.append({"id": "s5", "translation": {
  "en": "And Selim entered Cairo at the beginning of the year nine hundred and twenty-three.",
  "tr": "Selim de dokuz yüz yirmi üç yılının başında Kahire'ye girdi."},
 "tokens": [MADI("وَدَخَلَ", "dakhala", **W(FAIL_BAAD)),
  SALIM("fail"),
  MAFUL("الْقَاهِرَةَ", "qahira", "propn", note_ar=" — وَقِيلَ: مَنْصُوبٌ عَلَى التَّوَسُّعِ بِنَزْعِ الْخَافِضِ", note_en=" (some read it as in nasb by the dropping of the jarr letter)", note_tr=" (bir görüşe göre cer harfinin hazfiyle mansûbdur)"),
  FI(), MAJR("أَوَّلِ", "awwal", **W(MUDAF)),
  MUDAF_ILAYH("سَنَةِ", "sana", **W(MUDAF)),
  MUDAF_ILAYH("ثَلَاثٍ", "thalath", extra=["asma-al-adad-fil-kafiya"],
      note_ar=" — وَحُذِفَتْ مِنْهُ التَّاءُ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ: الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى تِسْعَةٍ يُخَالِفُ مَعْدُودَهُ",
      note_en=" — without the ta, because the thing counted, «year», is feminine: three to nine take the opposite gender of what they count",
      note_tr=" — ma'dûd «sene» müennes olduğu için tâsız: üçten dokuza kadar sayılar ma'dûduna cinsçe zıt olur"),
  ISHRIN(), TISUMIA(punct=".")]})

# ---- Chapter 5 — نِهَايَةُ الدَّوْلَةِ ----
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "The sultan of Egypt kept on fighting the Ottomans for a while after that, until he was taken captive.",
  "tr": "Mısır sultanı bundan sonra bir süre Osmanlılarla çarpışmayı sürdürdü; sonunda esir alındı."},
 "tokens": [tok("وَظَلَّ", "zalla-remain", "verb", ["kana-wa-akhawatuha", "doubled-verbs"],
      WA_AR + "ظَلَّ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَيُفِيدُ هُنَا الِاسْتِمْرَارَ.",
      "The waw conjoins; ظَلَّ «kept on» is one of كَانَ's sisters, built on fatha: it raises its noun and puts its predicate in nasb — here it tells that the act went on.",
      "«ve» + zalle «sürdürdü»: kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; ismini ref, haberini nasb eder — burada devamı bildirir.",
      segments=[seg("وَ", "wa", "conj"), seg("ظَلَّ", "zalla-remain", "verb")]),
  tok("سُلْطَانُ", "sultan", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ ظَلَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of ظَلَّ, in raf', annexed.", "Zalle'nin ismi, merfû, muzâf."),
  MISR_J(role="mi"),
  MUDARI("يُقَاتِلُ", "qatala-fight", ["form-iii-verbs", "kana-wa-akhawatuha"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ ظَلَّ", note_en=" — the clause is the predicate of ظَلَّ, in the seat of nasb", note_tr=" — cümle zalle'nin haberi, mahallen mansûb"),
  UTHMANIYYIN(R_MAF),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  DHALIKA(*DH_MI),
  ZARF("مُدَّةً", "mudda", mudaf=False, **ZAMAN, punct="،"),
  HATTA_IBT(),
  MAJHUL("أُخِذَ", "akhadha", ["thulathi-mujarrad-babs"], note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", note_en="; its deputy doer is the hidden «he»", note_tr="; nâib-i fâil gizli zamir «o»"),
  HAL("أَسِيرًا", "asir", note_ar="، وَصَاحِبُهُ نَائِبُ الْفَاعِلِ الْمُسْتَتِرُ", note_en=" — its owner is the hidden deputy doer «he»", note_tr=" — sahibi gizli nâib-i fâildir", punct=".")]})
S5.append({"id": "s2", "translation": {
  "en": "Then Ṭūmān Bāy was killed.",
  "tr": "Sonra Tûmân Bây öldürüldü."},
 "tokens": [THUMMA(),
  MAJHUL("قُتِلَ", "qatala", ["thulathi-mujarrad-babs"], **W(NAIB_BAAD)),
  *TUMANBAY("naib", punct=".")]})
S5.append({"id": "s3", "translation": {
  "en": "And with that the state of the Mamluks came to an end.",
  "tr": "Böylece Memlük devleti sona erdi."},
 "tokens": [tok("وَبِذٰلِكَ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
      WA_AR + "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«انْتَهَتْ».",
      "The waw conjoins; the ba is a jarr letter of cause («with that»), and the demonstrative after it is built on sukun in the seat of jarr — its lam marks distance and its kaf is a particle of address; the phrase hangs on «came to an end».",
      "«ve» + sebebiyet bâ'sı cer harfi; işaret ismi sükûn üzere mebnî, mahallen mecrûr — lâm uzaklık için, kâf hitap harfidir; câr-mecrûr «sona erdi»ye müteallik.",
      segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("انْتَهَتْ", "intaha", "verb", ["form-viii-verbs", "naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ (انْتَهَى ← انْتَهَتْ)، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ بَعْدَهُ.",
      "Past verb built on a fatha estimated on the alif, which dropped where two quiescents met (انْتَهَى → انْتَهَتْ); the ta marks the feminine, and its doer follows.",
      "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî (intehâ → intehet); tâ te'nîs içindir; fâili ondan sonra gelir."),
  FAIL("دَوْلَةُ", "dawla", **W(MUDAF)),
  MUDAF_ILAYH("الْمَمَالِيكِ", "mamluk", extra=["jam-taksir"], **W(MAMALIK_NOTE), punct=".")]})
S5.append({"id": "s4", "translation": {
  "en": "And the lands which they had held for a long time passed into the hands of the Ottomans.",
  "tr": "Uzun zaman ellerinde tuttukları diyarlar da Osmanlıların eline geçti."},
 "tokens": [tok("وَصَارَتِ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
      WA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "The waw conjoins; صَارَ «became, passed» is one of كَانَ's sisters, built on fatha: it raises its noun and puts its predicate in nasb; the ta marks the feminine and is voweled with kasra before the following ال.",
      "«ve» + sâra: kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; ismini ref, haberini nasb eder; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.",
      segments=[seg("وَ", "wa", "conj"), seg("صَارَتِ", "sara", "verb")]),
  tok("الْبِلَادُ", "bilad", "noun", ["kana-wa-akhawatuha", "jam-taksir"], "اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ، فَأُنِّثَ فِعْلُهُ.",
      "The noun of صَارَ, in raf' — a broken plural, so its verb is feminine.", "Sâra'nın ismi, merfû — kırık çoğul; bu yüzden fiili müennes geldi."),
  tok("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«الْبِلَادُ».",
      "A relative pronoun «which», built on sukun, in the seat of raf' as a na't of «the lands».", "İsm-i mevsûl «ki o», sükûn üzere mebnî, «diyarlar»ın na'tı olarak mahallen merfû."),
  VERB_WAW_ENC("مَلَكُوهَا", "malaka", "هَا", ["thulathi-mujarrad-babs"], note_ar=" — وَالْوَاوُ لِلْمَمَالِيكِ، وَهَا الْعَائِدُ عَلَى «الَّتِي»" + SILA_[0], note_en=" — the waw is the Mamluks, and «them» is the pronoun that returns to «which»" + SILA_[1], note_tr=" — vâv Memlüklerdir; «hâ», «ki o»ya dönen âid zamirdir" + SILA_[2]),
  ZARF("زَمَنًا", "zaman-period", mudaf=False, **ZAMAN),
  NAAT("طَوِيلًا", "tawil-long", "nasb"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ صَارَ", "; the jarr phrase hangs on the omitted predicate of صَارَ", " — câr-mecrûr sâra'nın mahzûf haberine müteallik")),
  MAJR("أَيْدِي", "yad", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", note_ar="، مُضَافٌ — جَمْعُ يَدٍ، اسْمٌ مَنْقُوصٌ", note_en=" — by a kasra estimated on the ya (too heavy to voice); annexed — the plural of «hand», a manqūṣ", note_tr=" — yâ üzerinde takdîrî kesre ile (ağırlık sebebiyle); muzâf — yed'in cem'i, mankûs isim"),
  UTHMANIYYIN(R_MI, punct=".")]})
S5.append({"id": "s5", "translation": {
  "en": "Selim stayed in Egypt some months, then he went back to his own lands.",
  "tr": "Selim birkaç ay Mısır'da kaldı, sonra kendi diyarına döndü."},
 "tokens": [MADI("وَأَقَامَ", "aqama", ["form-iv-verbs", "hollow-verbs"], **W(FAIL_BAAD)),
  SALIM("fail"),
  BI_NOUN("بِمِصْرَ", "misr", "مِصْرَ", pos="propn", extra=["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_TOWN[0] + " — وَالْبَاءُ بِمَعْنَى فِي", note_en=DIPT_TOWN[1] + "; the ba here means «in»", note_tr=DIPT_TOWN[2] + "; bâ burada «-de» anlamındadır"),
  ZARF("أَشْهُرًا", "shahr", mudaf=False, extra=["jam-taksir"], **ZAMAN, note_ar=" — جَمْعُ قِلَّةٍ لِشَهْرٍ", note_en=" — a plural of paucity of «month»", note_tr=" — şehrin cem-i kıllesi", punct="،"),
  THUMMA(),
  MADI("رَجَعَ", "rajaa", hidden=True),
  ILA(), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr", punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            if DERIVED & set(t.get("grammar", [])) and "thulathi-mujarrad-babs" in t["grammar"]:
                t["grammar"].remove("thulathi-mujarrad-babs")
            t["grammar"] = list(dict.fromkeys(t.get("grammar", [])))
            if not t["grammar"]: del t["grammar"]

# the grammar anchors must all resolve in the registry
_GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
_bad = sorted({g for S in CHAPS for s in S for t in s["tokens"] for g in t.get("grammar", []) if g not in _GR})
assert not _bad, _bad

# ---- the lexicon: every key by lemma identity from the shelf; the entries below are new -----------------------------------
PREF = ["ayn-jalut", "fath-al-qustantiniyya", "alb-arslan-wa-malazgird", "salah-al-din-wa-al-quds", "ibn-khaldun-wa-timur",
        "bina-baghdad", "al-kafiya", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "wasiyyat-abi-yusuf-l5", "talkhis-al-miftah"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
# where the shelf holds one key in several packages, take the entry whose sense this story uses
FORCE = {"kabir": "sibawayh-fi-al-basra", "mudda": "qisas-al-nabiyyin-4", "kull": "qisas-al-nabiyyin-4", "lakinna": "qisas-al-nabiyyin-4",
         "kama": "sibawayh-fi-al-basra", "dafaa": "qisas-al-nabiyyin-4", "an": "sibawayh-fi-al-basra", "hatta": "wasiyyat-abi-hanifa-samti", "hazima": "qisas-al-nabiyyin-4", "akbar": "qisas-al-nabiyyin-4", "sinn": "qisas-al-nabiyyin-4"}
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    if FORCE.get(k) and k in _M.get(FORCE[k], {}): return _M[FORCE[k]][k]
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

def PHRASE(lemma, lvl, g_en, g_tr, l_en, l_tr, n_en, n_tr):
    return {"lemma": lemma, "pos": "phrase", "level": lvl, "gloss": {"en": g_en, "tr": g_tr}, "literal": {"en": l_en, "tr": l_tr}, "note": {"en": n_en, "tr": n_tr}}

NEW_GLOSS = {
 "ghawri": {"lemma": "الْغَوْرِيّ", "pos": "propn", "gloss": {
    "en": "al-Ghawrī — al-Ashraf Qānṣūh al-Ghawrī, Mamluk sultan of Egypt and Syria (r. 906–922 / 1501–1516), who died at Marj Dābiq; a nisba title with the article, fully declined",
    "tr": "Gavrî — el-Eşref Kansu Gavrî, Mısır ve Şam'ın Memlük sultanı (s. 906–922 / 1501–1516), Mercidâbık'ta öldü; elif-lâmlı nisbet lakabı, munsarif"}, "level": 5},
 "salim-sultan": {"lemma": "سَلِيم", "pos": "propn", "gloss": {
    "en": "Selim — Sultan Selim I of the Ottomans (r. 918–926 / 1512–1520), who took Syria and Egypt; an Arabic name on فَعِيل, fully declined (سَلِيمٌ)",
    "tr": "Selim — Osmanlı Sultanı I. Selim (Yavuz; s. 918–926 / 1512–1520), Şam'ı ve Mısır'ı aldı; fa'îl vezninde Arapça isim, munsarif (سَلِيمٌ)"}, "level": 5},
 "tumanbay": {"lemma": "طُومَان بَاي", "pos": "propn", "gloss": {
    "en": "Ṭūmān Bāy — al-Ashraf Ṭūmān Bāy, the last Mamluk sultan of Egypt (r. 922–923 / 1516–1517); a foreign compound name: the first part is built on fatha (طُومَانَ), the second carries the case as a diptote (بَايُ)",
    "tr": "Tûmân Bây — el-Eşref Tûmân Bây, Mısır'ın son Memlük sultanı (s. 922–923 / 1516–1517); yabancı mürekkep isim: ilk parça fetha üzere mebnî (طُومَانَ), ikinci parça gayr-i munsarif olarak i'râbı taşır (بَايُ)"}, "level": 5},
 "marj": {"lemma": "مَرْج", "root": "م ر ج", "pos": "noun", "plural": "مُرُوج", "gloss": {
    "en": "a meadow, open grassland where beasts graze (pl. مُرُوج)", "tr": "çayır, hayvanların otladığı açık otlak (ç. مُرُوج)"}, "level": 5},
 "dabiq": {"lemma": "دَابِق", "pos": "propn", "gloss": {
    "en": "Dābiq — a village north of Aleppo, beside the meadow called Marj Dābiq; a diptote, with no tanwin (دَابِقَ in jarr)",
    "tr": "Dâbık — Halep'in kuzeyinde, Mercidâbık denen çayırın yanındaki köy; gayr-i munsariftir, tenvin almaz (cerde دَابِقَ)"}, "level": 5},
 "marj-dabiq": PHRASE("مَرْجُ دَابِقَ", 5, "Marj Dābiq — the meadow by the village of Dābiq, north of Aleppo, where the Ottomans broke the Mamluk army in 922 / 1516 and the sultan al-Ghawrī died",
    "Mercidâbık — Halep'in kuzeyinde, Dâbık köyünün yanındaki çayır; Osmanlılar 922 / 1516'da Memlük ordusunu burada bozdu ve Sultan Gavrî burada öldü",
    "literally «the Meadow of Dābiq»", "lafzen «Dâbık Çayırı»",
    "A place-name built as an idafa: مَرْج «meadow» takes the case of its seat (مَرْجُ in raf', مَرْجِ in jarr), and دَابِق stays its second term, in jarr by the fatha, for it is a diptote: مَرْجُ دَابِقَ، يَوْمُ مَرْجِ دَابِقَ.",
    "İzâfetle kurulmuş bir yer adı: مَرْج «çayır» bulunduğu yerin i'râbını alır (refte مَرْجُ, cerde مَرْجِ); دَابِق ise muzâfun ileyh olarak mecrûr kalır; gayr-i munsarif olduğu için cer alâmeti fethadır: مَرْجُ دَابِقَ، يَوْمُ مَرْجِ دَابِقَ."),
 "raydaniyya": {"lemma": "الرَّيْدَانِيَّة", "pos": "propn", "gloss": {
    "en": "al-Raydāniyya — a place just outside Cairo to the north-east, where the Ottomans routed the last Mamluk army at the end of 922 / January 1517",
    "tr": "Ridâniye — Kahire'nin hemen kuzeydoğusunda bir yer; Osmanlılar son Memlük ordusunu 922 sonunda / Ocak 1517'de burada bozguna uğrattı"}, "level": 5},
}
# a key is a global claim: a NEW key must not already name something else on the shelf (nor in a sibling's staged package)
_STAGED = {}
for d in OUT_ROOT.iterdir() if OUT_ROOT.exists() else []:
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
for k, e in NEW_GLOSS.items():
    hit = [p for p in PREF if k in _G[p]]
    assert not hit, (k, hit)
    for p, g in _STAGED.items():
        if k in g:
            assert g[k].get("lemma") == e["lemma"], ("staged clash", k, p, g[k].get("lemma"))

used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
            if t.get("phrase"): used.add(t["phrase"]["lex"])
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k)
    if e is None: missing.append(k)
    else: GLOSS[k] = json.loads(json.dumps(e))
assert not missing, missing
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "مَرْجُ دَابِقَ", "en": "Marj Dābiq", "tr": "Mercidâbık"},
 "subtitle": {"ar": "سُلْطَانَانِ يَلْتَقِيَانِ قُرْبَ حَلَبَ، وَدَوْلَةٌ تَنْتَهِي، وَمِصْرُ وَالشَّامُ تَصِيرَانِ إِلَى الْعُثْمَانِيِّينَ — قِصَّةٌ لِلْمُسْتَوَى الْخَامِسِ",
              "en": "Two sultans meet near Aleppo, a state comes to its end, and Egypt and al-Shām pass to the Ottomans — a story for the fifth level",
              "tr": "Halep yakınında karşılaşan iki sultan, sona eren bir devlet ve Osmanlılara geçen Mısır ile Şam — beşinci seviye için bir hikâye"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى الْخَامِسُ) لِخَبَرِ وَقْعَةِ مَرْجِ دَابِقَ سَنَةَ ٩٢٢ هـ / ١٥١٦ م، وَمَوْتِ السُّلْطَانِ الْغَوْرِيِّ فِيهَا، وَدُخُولِ السُّلْطَانِ سَلِيمٍ الشَّامَ ثُمَّ مِصْرَ بَعْدَ وَقْعَةِ الرَّيْدَانِيَّةِ، وَدُخُولِهِ الْقَاهِرَةَ أَوَّلَ سَنَةِ ٩٢٣ هـ / ١٥١٧ م، وَانْتِهَاءِ دَوْلَةِ الْمَمَالِيكِ، عَلَى مَا يَرْوِيهِ ابْنُ إِيَاسٍ فِي «بَدَائِعِ الزُّهُورِ فِي وَقَائِعِ الدُّهُورِ»، وَابْنُ طُولُونَ فِي «مُفَاكَهَةِ الْخِلَّانِ فِي حَوَادِثِ الزَّمَانِ» لِأَخْبَارِ الشَّامِ. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ تِلْكَ الْكُتُبِ، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا قَوْلٌ يُنْسَبُ إِلَى أَحَدٍ. وَتُرِكَ خَبَرُ انْتِقَالِ الْخِلَافَةِ، وَأَعْدَادُ الْجُيُوشِ وَالْقَتْلَى، وَصِفَةُ مَوْتِ الْغَوْرِيِّ، وَتَفْصِيلُ أَسْرِ طُومَانَ بَايَ وَقَتْلِهِ؛ وَاكْتُفِيَ بِأَنَّهُ قُتِلَ. وَكُلُّ إِعْرَابٍ فِيهَا اجْتِهَادُ الْمُؤَلِّفِ، وَهِيَ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "ORIGINAL Level-5 graded Arabic: the battle of Marj Dābiq in 922 AH / 1516 CE, where the Mamluk sultan al-Ghawrī died on the field, the Ottoman sultan Selim's taking of Syria, his victory over Ṭūmān Bāy at al-Raydāniyya and his entry into Cairo at the beginning of 923 AH / 1517 CE, and the end of the Mamluk state — RETOLD FREELY along the well-attested core of the classical accounts: Ibn Iyās, Badāʾiʿ al-zuhūr fī waqāʾiʿ al-duhūr, and, for Syria, Ibn Ṭūlūn, Mufākahat al-khillān fī ḥawādith al-zamān. No sentence is a quotation from these works; no āya or ḥadīth is quoted; no words are put in a historical person's mouth. Left out on purpose: the transfer of the caliphate, the sizes of the armies and the numbers of the slain, the manner of al-Ghawrī's death, and the details of Ṭūmān Bāy's capture and death — one neutral line says only that he was killed. Every iʿrāb line is the author's own analysis, pending scholarly review.",
  "tr": "ÖZGÜN 5. seviye Arapça: 922 h. / 1516 m. yılındaki Mercidâbık savaşı ve Memlük sultanı Gavrî'nin savaş meydanında ölümü, Osmanlı sultanı Selim'in Şam'ı alışı, Ridâniye'de Tûmân Bây'ı yenişi ve 923 h. / 1517 m. yılı başında Kahire'ye girişi ile Memlük devletinin sonu; klasik kaynakların — İbn İyâs, Bedâi'u'z-zühûr fî vekâi'i'd-dühûr ve Şam için İbn Tûlûn, Müfâkehetü'l-hillân fî havâdisi'z-zamân — üzerinde birleştiği sağlam çekirdeğe bağlı kalınarak SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bu eserlerden alıntı değildir; hiçbir âyet veya hadis aktarılmamıştır; hiçbir tarihî şahsın ağzına söz konmamıştır. Bilerek dışarıda bırakılanlar: hilâfetin intikali, ordu büyüklükleri ve ölü sayıları, Gavrî'nin ölüm şekli ve Tûmân Bây'ın esir alınıp öldürülmesinin ayrıntıları — yalnızca öldürüldüğünü söyleyen tarafsız bir cümle vardır. Her i'râb satırı yazarın kendi tahlilidir ve ilmî incelemeyi beklemektedir.",
  "reviewStatus": "pending-scholarly-review",
 },
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]),
      "new:", sorted(k for k in GLOSS if k in NEW_GLOSS), "->", PKG)
