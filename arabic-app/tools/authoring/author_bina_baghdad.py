"""Author content/samples/bina-baghdad — «بِنَاءُ بَغْدَادَ», an ORIGINAL historical story at Level 5 (Advanced).

ORIGINAL graded Arabic: the ʿAbbāsid caliph Abū Jaʿfar al-Manṣūr wants a new capital for his state and goes out himself to
look for a site; on the Tigris there is a small village called Baghdad; he stops there, spends a night, and resolves to
build. He chooses the place for its river (ships come up the Tigris from the sea; the Euphrates is near, with canals between
the two rivers), its roads (they meet there from Syria, Kufa, Basra and Khurāsān) and its trade. He sends envoys to gather
workers and men of every craft; in the year 145 of the Hijra he begins the building and lays the first brick with his own
hand. The city is made round, with two walls and a moat, four gates named after the lands their roads lead to (the Kufa,
Basra, Khurāsān and Syria Gates), and the palace with its green dome and the congregational mosque at the centre; he names it
Madīnat al-Salām. Within a few years people, markets and scholars fill it, and it becomes a seat of learning: al-Ṭabarī
writes his History there, and al-Khaṭīb al-Baghdādī gathers its reports in Tārīkh Baghdād. Only the well-attested core is
told (al-Ṭabarī, Taʾrīkh al-rusul wa-l-mulūk, under the years 145–146; al-Khaṭīb al-Baghdādī, Taʾrīkh Baghdād, the opening
topographical part). The numbers of workers and the costs (the reports differ) and the astrologers' part are left out; no
āya or ḥadīth is quoted, and no sentence is a quotation of a source — al-Manṣūr's reasons are told in the narrator's words,
never as his recorded speech.

Five chapters, twenty-eight sentences, in a Level-5 register: mafʿūl muṭlaq (بِنَاءً قَوِيًّا), mafʿūl lahu (رَغْبَةً), tamyīz
(عِلْمًا after an elative; the counted noun after أَرْبَعَة and the year-number), istithnāʾ mufarragh (مَا مَضَى إِلَّا سَنَوَاتٌ,
with the verb left masculine across إِلَّا), relative and naʿt clauses with a resumptive pronoun (الَّذِي يَخْرُجُ إِلَيْهِ طَرِيقُهُ،
مَوْضِعًا يَبْنِيهَا فِيهِ، أَنْهَارٌ تَجْرِي فِيهَا السُّفُنُ، قُبَّةٌ يَرَاهَا النَّاسُ، كِتَابٍ سَمَّاهُ), لَمَّا, حَتَّى + subjunctive (حَتَّى يَجْمَعُوا)
beside the ibtidāʾ حَتَّى, the wāw of ḥāl (وَالْمَنْصُورُ يَنْظُرُ، وَمَعَهُمْ كُتُبُهُمْ), a jumla ḥāl (يَطْلُبُ), kāna and its sisters
(كَانَ with a fronted predicate, صَارَ, and بَاتَ used as a COMPLETE verb), أَنَّ in «وَذٰلِكَ أَنَّ», the passive (تُسَمَّى، سُمِّيَ),
إِذَا with its answer, جَعَلَ and سَمَّى with two objects, the dual (سُورَيْنِ، النَّهْرَيْنِ) and diptotes in every seat.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf (the majority reading of a
key wins; a key whose majority gloss belongs to another context is pinned to a package with a plain gloss). No new verb is
minted: every verb's paradigm is copied from a package that already owns it. New entries are listed in NEW_GLOSS. Regenerate:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_bina_baghdad.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "bina-baghdad"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"نَا": "pron-1p", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمَا": "pron-3d"})
PRON_AR.update({"نَا": "نَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُمَا": "هُمَا"})
N = lambda s: unicodedata.normalize("NFC", s)

# ---- the clause seats and short notes this story needs (ar, en, tr) ---------------------------------------------------
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
DOER_AFTER = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
DIPT_BAGHDAD = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town), barred from tanwin", " — müennes özel isim (şehir adı), gayr-i munsarif")
DIPT_DIJLA = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a river), barred from tanwin", " — müennes özel isim (nehir adı), gayr-i munsarif")
DIPT_KHURASAN = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", " — a proper name ending in the added alif and nun, barred from tanwin", " — sonunda zâid elif ve nûn bulunan özel isim, gayr-i munsarif")
LAQAB = (" — لَقَبُ الْخَلِيفَةِ الْعَبَّاسِيِّ أَبِي جَعْفَرٍ", " — the title of the ʿAbbāsid caliph Abū Jaʿfar", " — Abbâsî halifesi Ebû Ca'fer'in lakabı")
def NAAT_OF(seat, of_ar, of_en, of_tr, second=False):
    """the clause is the na't of a named indefinite noun"""
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return (" — وَالْجُمْلَةُ فِي مَحَلِّ " + s[0] + " نَعْتٌ " + ("ثَانٍ " if second else "") + "لِـ«" + of_ar + "»",
            "; the clause qualifies «" + of_en + "» — " + ("a second na't, " if second else "") + "in the seat of " + s[1],
            "; cümle «" + of_tr + "» için " + ("ikinci " if second else "") + "na't, mahallen " + s[2])
def PH(t, lex, span=2):
    """the name-phrase sits on the FIRST token of its span (CLAUDE.md «Idioms/phrases»): both words keep their own iʿrāb"""
    t["phrase"] = {"lex": lex, "span": span}
    return t
def J(*parts):
    """join note triples"""
    return tuple("".join(p[i] for p in parts) for i in range(3))

# ---- names ---------------------------------------------------------------------------------------------------------------
MANSUR_F = lambda punct=None: FAIL("الْمَنْصُورُ", "mansur-caliph", "propn", note_ar=LAQAB[0], note_en=LAQAB[1], note_tr=LAQAB[2], punct=punct)
BAGHDAD_MI = lambda punct=None, note=("", "", ""): MUDAF_ILAYH("بَغْدَادَ", "baghdad", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_BAGHDAD[0] + note[0], note_en=DIPT_BAGHDAD[1] + note[1], note_tr=DIPT_BAGHDAD[2] + note[2], punct=punct)
DIJLA_J = lambda punct=None: MAJR("دِجْلَةَ", "dijla", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_DIJLA[0], note_en=DIPT_DIJLA[1], note_tr=DIPT_DIJLA[2], punct=punct)
DIJLA_MI = lambda punct=None: MUDAF_ILAYH("دِجْلَةَ", "dijla", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_DIJLA[0], note_en=DIPT_DIJLA[1], note_tr=DIPT_DIJLA[2], punct=punct)

# ---- particles and short words ------------------------------------------------------------------------------------------
def ANNA_T(role=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".",
        "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
HATTA = lambda: tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
    "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «so that» is a particle of purpose and jarr: the present verb after it is in nasb by an أَنْ that must stay hidden, and the masdar they build is in jarr by حَتَّى.",
    "Hattâ «-sın diye» — gâye ve cer harfi: sonraki muzâri vücûben gizli en ile mansûb; kurdukları müevvel masdar hattâ ile mecrûr.")
def WA_PREP(full, lex, head, note=("", "", "")):
    """وَمِنَ، وَمِنْ، وَفِي: a conjunction (or the waw that opens a sentence) fused to a jarr letter"""
    istinaf = note == "istinaf"
    if istinaf: note = ("", "", "")
    kasr = head == "مِنَ"
    return tok(full, lex, "prep", ["huruf-jarr"] + ([] if istinaf else ["atf-nasaq"]),
        ("الْوَاوُ لِلِاسْتِئْنَافِ، وَ" if istinaf else WA_AR) + head + " حَرْفُ جَرٍّ" + ("، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ" if kasr else "") + note[0] + ".",
        ("The waw opens a new sentence; " if istinaf else "The waw conjoins; ") + head + " is a jarr letter" + (", voweled with fatha before the following ال" if kasr else "") + note[1] + ".",
        ("Vâv isti'nâf içindir; " if istinaf else "«ve» + ") + "cer harfi" + ("; iki sâkin karşılaştığı için fetha ile harekelendi" if kasr else "") + note[2] + ".",
        segments=[seg("وَ", "wa", "conj"), seg(head, lex, "prep")])
def HADHA_MUB():
    return ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ", extra=["mubtada-khabar"])
def LAHU(pron_tr, punct=None, note=("", "", "")):
    return tok("لَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
        "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ" + note[0] + ".",
        "The lam is a jarr letter; the attached «him» is built on damma and fills the seat of jarr" + note[1] + ".",
        "Lâm cer harfi; bitişik «o» zamiri damme üzere mebnî, mahallen mecrûr" + pron_tr + note[2] + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")])
def LAHA(note=("", "", ""), punct=None):
    return tok("لَهَا", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
        "اللَّامُ حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ" + note[0] + ".",
        "The lam is a jarr letter; the attached «it» (fem.) is built on sukun and fills the seat of jarr" + note[1] + ".",
        "Lâm cer harfi; bitişik «o» (müennes) zamiri sükûn üzere mebnî, mahallen mecrûr" + note[2] + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg("هَا", "pron-3fs", "pron")])
def ZARF_ENC(full, lex, enc, kind="مَكَانٍ", kind_en="place", kind_tr="mekân", note=("", "", ""), punct=None):
    """حَوْلَهَا، عِنْدَهُ: an adverb annexed to its pronoun"""
    return tok(full, lex, "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
        "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note[0] + ".",
        "An adverb of " + kind_en + ", in nasb and annexed to the attached pronoun, which fills the seat of jarr" + note[1] + ".",
        kind_tr + " zarfı, mansûb; bitişik zamire muzâf, zamir mahallen mecrûr" + note[2] + ".",
        punct=punct, segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def ATF_ENC(full, lex, enc, case="jarr", extra=None, note=("", "", ""), punct=None):
    """وَطُرُقِهِ، وَتِجَارَتِهِ: a conjoined noun annexed to its pronoun"""
    sign = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    stem = full[2:]
    return tok(full, lex, "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        WA_AR + "مَعْطُوفٌ " + sign + "، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note[0] + ".",
        "The waw conjoins; the noun takes the case of the word it is joined to, and is annexed to the attached pronoun (in the seat of jarr)" + note[1] + ".",
        "«ve» + ma'tûf, öncekinin i'râbını alır; bitişik zamire muzâf, zamir mahallen mecrûr" + note[2] + ".",
        punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def MUD_DF(full, lex, extra=None, naqis=False, note=("", "", ""), punct=None):
    """يَخْرُجُ طَرِيقُهُ، تَجْرِي فِيهَا السُّفُنُ: a present verb in raf' whose doer follows"""
    sign = ("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " (the damma is estimated on the ya)", " (damme yâ üzerinde takdîrî)") if naqis else ("بِالضَّمَّةِ", "", "")
    return tok(full, lex, "verb", ["mudari-marfu"] + (["naqis-verbs"] if naqis else []) + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign[0] + "، وَالْفَاعِلُ بَعْدَهُ" + note[0] + ".",
        "Present verb in raf'" + sign[1] + "; its doer follows" + note[1] + ".",
        "Merfû muzâri" + sign[2] + "; fâili ondan sonra gelir" + note[2] + ".", punct=punct)
def MUTLAQ_NAW(full, lex, verb_ar, verb_en, verb_tr, how=("بِوَصْفِهِ", "by the adjective after it", "sıfatıyla"), extra=None, punct=None):
    """بِنَاءً قَوِيًّا: the absolute object that names the KIND of the act"""
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"] + (extra or []),
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «" + verb_ar + "» مُبَيِّنٌ لِلنَّوْعِ " + how[0] + ".",
        "The absolute object (maf'ul mutlaq), in nasb — the masdar of «" + verb_en + "», naming the KIND of the act " + how[1] + ".",
        "Mef'ûlün mutlak, mansûb — «" + verb_tr + "» fiilinin masdarı; " + how[2] + " fiilin nev'ini beyan eder.", punct=punct)
def MAFUL_LAHU(full, lex, punct=None, note=("", "", "")):
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"],
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ" + note[0] + ".",
        "The maf'ul li-ajlih (object of cause), in nasb — a masdar of the heart giving the reason for the act, sharing its time and its doer" + note[1] + ".",
        "Mef'ûlün lieclih, mansûb — fiilin sebebini bildiren kalbî masdar; fiille zamanda ve fâilde ortak" + note[2] + ".", punct=punct)
def TAMYIZ_T(full, lex, what_ar, what_en, what_tr, punct=None):
    return tok(full, lex, "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"],
        "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ " + what_ar + ".", "A specifier (tamyiz), in nasb — it names " + what_en + ".", "Temyîz, mansûb — " + what_tr + " beyan eder.", punct=punct)
TAFDIL_TAMYIZ = ("جِهَةَ التَّفْضِيلِ", "the respect in which the comparison holds", "üstünlüğün hangi yönden olduğunu")
def MAF2(full, lex, extra=None, punct=None, note=("", "", "")):
    """the second object of a verb of two objects"""
    return tok(full, lex, "noun", ["maful-bihi", "mafulayn"] + (extra or []), "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ" + note[0] + ".",
        "The second object, in nasb" + note[1] + ".", "İkinci mef'ûlün bih, mansûb" + note[2] + ".", punct=punct)

TITLES = [{"ar": "الْخَلِيفَةُ يَطْلُبُ مَوْضِعًا", "en": "The caliph looks for a site", "tr": "Halife bir yer arıyor"},
          {"ar": "النَّهْرُ وَالطُّرُقُ", "en": "The river and the roads", "tr": "Nehir ve yollar"},
          {"ar": "الْعُمَّالُ وَالْبِنَاءُ", "en": "The workers and the building", "tr": "İşçiler ve inşa"},
          {"ar": "الْمَدِينَةُ الْمُسْتَدِيرَةُ", "en": "The round city", "tr": "Yuvarlak şehir"},
          {"ar": "دَارُ الْعِلْمِ", "en": "A home of learning", "tr": "İlim yurdu"}]

# =================================== Chapter 1 — الْخَلِيفَةُ يَطْلُبُ مَوْضِعًا ===================================
S1 = []
S1.append({"id": "s1", "translation": {"en": "This is a report that the historians relate about the building of Baghdad; we tell it here in our own words.",
                                      "tr": "Bu, tarihçilerin Bağdat'ın kuruluşu hakkında rivayet ettiği bir haberdir; biz onu burada kendi sözlerimizle anlatıyoruz."},
 "tokens": [HADHA_MUB(), KHABAR("خَبَرٌ", "khabar"),
  tok("يَرْوِيهِ", "rawa", "verb", ["mudari-marfu", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "jumla-sifa"],
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ — وَالْهَاءُ عَائِدٌ عَلَى «خَبَرٌ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لَهُ.",
    "Present verb in raf' (the damma is estimated on the ya); the attached pronoun is its object, placed before the doer, which follows — the pronoun returns to «a report», and the clause is its na't, in the seat of raf'.",
    "Merfû muzâri (damme yâ üzerinde takdîrî); bitişik zamir fâilden önce gelmiş mef'ûlün bih, mahallen mansûb; fâili ondan sonra gelir — zamir «haber»e döner; cümle onun na'tı, mahallen merfû.",
    segments=[seg("يَرْوِي", "rawa", "verb"), seg("هِ", "pron-3ms", "pron")]),
  FAIL("أَهْلُ", "ahl", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("التَّارِيخِ", "tarikh"),
  PREP("عَنْ", "an", gloss_tr="«hakkında»"),
  MAJR("بِنَاءِ", "bina", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَرْوِي»", note_en=", annexed — the jarr phrase attaches to «relate»", note_tr=", muzâf — câr-mecrûr «rivayet eder»e müteallik"),
  BAGHDAD_MI(punct="،"),
  MUDARI("نَحْكِيهِ", "haka", ["jumla-sifa"], who="نَحْنُ", enc="هِ", naqis="ي", wujub=True,
    note_ar=NAAT_OF("raf", "خَبَرٌ", "a report", "haber", True)[0], note_en=NAAT_OF("raf", "خَبَرٌ", "a report", "haber", True)[1], note_tr=NAAT_OF("raf", "خَبَرٌ", "a report", "haber", True)[2]),
  HUNA(), BI_NOUN("بِأَلْفَاظِنَا", "lafz", "أَلْفَاظِنَا", enc="نَا", extra=["jam-taksir"], note_ar=" — جَمْعُ لَفْظٍ", note_en=" — «our words», the plural of لَفْظ", note_tr=" — lafz'ın cem'i, «sözlerimiz»", punct=".")]})

S1.append({"id": "s2", "translation": {"en": "Al-Manṣūr was the caliph of the Muslims, and he wanted to build a new capital for his state.",
                                      "tr": "Mansûr, Müslümanların halifesiydi; devleti için yeni bir başkent kurmak istiyordu."},
 "tokens": [KANA("كَانَ"), ISMK("الْمَنْصُورُ", "mansur-caliph", "propn", note_ar=LAQAB[0], note_en=LAQAB[1], note_tr=LAQAB[2]),
  KHK("خَلِيفَةَ", "khalifa", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الْمُسْلِمِينَ", "muslim", extra=["jam-mudhakkar-salim"], sign="بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the ya, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için yâ ile", punct="،"),
  KANA_HID("وَكَانَ"),
  MUDARI_KH("يُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"]),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يُرِيدُ»", "; the clause it builds is the object of «wanted», in the seat of nasb", "; kurduğu müevvel masdar «istiyordu»nun mef'ûlü, mahallen mansûb"),
  MANSUB_AN("يَبْنِيَ", "bana", ["naqis-verbs"], note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha shows on the ya, being light", note_tr=" — fetha hafif olduğu için yâ üzerinde görünür"),
  LI_ENC("لِدَوْلَتِهِ", "dawla", "دَوْلَتِ", "هِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَبْنِيَ»", note_en=" — the jarr phrase attaches to «build»", note_tr=" — câr-mecrûr «kurmak»a müteallik"),
  MAFUL("عَاصِمَةً", "asima"), NAAT("جَدِيدَةً", "jadid", "nasb", punct=".")]})

S1.append({"id": "s3", "translation": {"en": "So he went out, looking for a site on which to build it.",
                                      "tr": "Bunun üzerine, onu üzerine kuracağı bir yer arayarak yola çıktı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja", hidden=True), HAL_CL_MUDARI("يَطْلُبُ", "talaba"), MAFUL("مَوْضِعًا", "mawdi"),
  MUDARI("يَبْنِيهَا", "bana", ["jumla-sifa"], enc="هَا", naqis="ي",
    note_ar=" — وَهَا عَائِدَةٌ عَلَى الْعَاصِمَةِ" + NAAT_OF("nasb", "مَوْضِعًا", "a site", "yer")[0],
    note_en=" — «it» returns to the capital" + NAAT_OF("nasb", "مَوْضِعًا", "a site", "yer")[1],
    note_tr=" — «onu» zamiri başkente döner" + NAAT_OF("nasb", "مَوْضِعًا", "a site", "yer")[2]),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)", punct=".",
    note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَبْنِي»، وَالْهَاءُ عَائِدٌ عَلَى «مَوْضِعًا» يَرْبِطُ الصِّفَةَ بِالْمَوْصُوفِ",
    note_en="; the jarr phrase attaches to «build», and the pronoun returns to «a site» — the bond that ties the qualifying clause to its noun",
    note_tr="; câr-mecrûr «kurar»a müteallik; zamir «yer»e döner — sıfat cümlesini mevsûfuna bağlayan âid budur")]})

S1.append({"id": "s4", "translation": {"en": "On the river Tigris there was a small village called Baghdad.",
                                      "tr": "Dicle nehrinin kıyısında Bağdat denen küçük bir köy vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True), ALA(),
  MAJR("نَهْرِ", "nahr", extra=["idafa-definiteness"], note_ar="، مُضَافٌ" + KH_MUQ[0], note_en=", annexed" + KH_MUQ[1], note_tr=", muzâf" + KH_MUQ[2]),
  DIJLA_MI(),
  ISMK("قَرْيَةٌ", "qarya", muakhkhar=True, note_ar=" — وَجَازَ أَنْ يَكُونَ نَكِرَةً لِتَقَدُّمِ الْخَبَرِ شِبْهِ الْجُمْلَةِ", note_en="; it may be indefinite because the jarr-phrase predicate comes first", note_tr="; câr-mecrûr haber öne geçtiği için nekire olabilir"),
  NAAT("صَغِيرَةٌ", "saghir", "raf"),
  tok("تُسَمَّى", "samma", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs", "naqis-verbs", "mafulayn", "jumla-sifa"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «قَرْيَةٌ»، وَهُوَ الْعَائِدُ الرَّابِطُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«قَرْيَةٌ».",
    "Present verb in the passive, in raf' by a damma estimated on the alif; its deputy doer is the hidden «it» (the village), the resumptive pronoun — the clause is a second na't of «a village», in the seat of raf'.",
    "Meçhul muzâri, elif üzerinde takdîrî damme ile merfû; nâib-i fâil «köy»e dönen gizli zamir «o» — bağlayıcı âid zamirdir; cümle «köy»ün ikinci na'tı, mahallen merfû."),
  tok("بَغْدَادَ", "baghdad", "propn", ["maful-bihi", "mafulayn", "mamnu-min-sarf"],
    "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ بِلَا تَنْوِينٍ" + DIPT_BAGHDAD[0] + " — سَمَّى يَنْصِبُ مَفْعُولَيْنِ، فَلَمَّا بُنِيَ لِلْمَجْهُولِ نَابَ الْأَوَّلُ عَنِ الْفَاعِلِ وَبَقِيَ الثَّانِي مَنْصُوبًا.",
    "The second object, in nasb (fatha without tanwin)" + DIPT_BAGHDAD[1] + " — سَمَّى takes two objects; in the passive the first becomes the deputy doer and the second stays in nasb.",
    "İkinci mef'ûlün bih, tenvinsiz fetha ile mansûb" + DIPT_BAGHDAD[2] + " — sammâ iki mef'ûl alır; meçhul olunca birincisi nâib-i fâil olur, ikincisi mansûb kalır.", punct=".")]})

S1.append({"id": "s5", "translation": {"en": "When he reached it, he stopped there and spent a night in it.",
                                      "tr": "Oraya varınca orada konakladı ve bir gece orada kaldı."},
 "tokens": [LAMMA2("فَلَمَّا"),
  ENC_MADI("بَلَغَهَا", "balagha", "هَا", hidden=True, note_ar="، وَهَا عَائِدَةٌ عَلَى الْقَرْيَةِ" + LAMMA_CL[0], note_en="; «it» returns to the village" + LAMMA_CL[1], note_tr="; zamir köye döner" + LAMMA_CL[2]),
  MADI("نَزَلَ", "nazala", hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)", punct="،", note_ar="، وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«نَزَلَ»", note_en="; the ba here means «at», and the phrase attaches to «stopped»", note_tr="; bâ burada «-de» anlamında; câr-mecrûr «konakladı»ya müteallik"),
  MADI("وَبَاتَ", "bata", ["hollow-verbs", "al-fil-al-tamm-wal-naqis"], hidden=True,
    note_ar=" — وَبَاتَ هُنَا فِعْلٌ تَامٌّ بِمَعْنَى «أَقَامَ اللَّيْلَ»، يَكْتَفِي بِفَاعِلِهِ وَلَا يَطْلُبُ خَبَرًا",
    note_en=" — بَاتَ is a COMPLETE verb here, «to pass the night»: it is content with its doer and asks for no predicate",
    note_tr=" — bâte burada tam fiildir, «geceyi geçirmek» anlamında: fâiliyle yetinir, haber istemez"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («orada»)"),
  ZARF("لَيْلَةً", "layla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False, punct=".")]})

S1.append({"id": "s6", "translation": {"en": "The place pleased him, and he resolved to build his city there.",
                                      "tr": "Yer onun hoşuna gitti; şehrini orada kurmaya karar verdi."},
 "tokens": [ENC_MADI("فَأَعْجَبَهُ", "ajaba-please", "هُ", ["form-iv-verbs"], note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  FAIL("الْمَوْضِعُ", "mawdi", punct="،"),
  MADI("وَعَزَمَ", "azama", hidden=True), ALA(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِعَلَى، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«عَزَمَ»", "; the masdar it builds is in jarr after عَلَى, and the phrase attaches to «resolved»", "; kurduğu müevvel masdar alâ ile mecrûr; câr-mecrûr «karar verdi»ye müteallik"),
  MANSUB_AN("يَبْنِيَ", "bana", ["naqis-verbs"], note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha shows on the ya, being light", note_tr=" — fetha hafif olduğu için yâ üzerinde görünür"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («orada»)"),
  ENC_NOUN("مَدِينَتَهُ", "madina", "هُ", "maful", punct=".")]})

# ======================================== Chapter 2 — النَّهْرُ وَالطُّرُقُ ========================================
S2 = []
S2.append({"id": "s1", "translation": {"en": "Al-Manṣūr chose it out of desire for its river, its roads and its trade.",
                                      "tr": "Mansûr orayı nehrine, yollarına ve ticaretine duyduğu istekten dolayı seçti."},
 "tokens": [ENC_MADI("وَاخْتَارَهُ", "ikhtara", "هُ", ["form-viii-verbs", "hollow-verbs"],
    note_ar="، وَالْهَاءُ عَائِدٌ عَلَى الْمَوْضِعِ" + DOER_AFTER[0], note_en="; «it» returns to the site" + DOER_AFTER[1], note_tr="; zamir yere döner" + DOER_AFTER[2]),
  MANSUR_F(), MAFUL_LAHU("رَغْبَةً", "raghba"), FI(),
  ENC_NOUN("نَهْرِهِ", "nahr", "هِ", "majr", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«رَغْبَةً»", note_en=" — the jarr phrase attaches to «desire»", note_tr=" — câr-mecrûr «istek»e müteallik"),
  ATF_ENC("وَطُرُقِهِ", "tariq", "هِ", extra=["jam-taksir"], note=(" — جَمْعُ طَرِيقٍ", " — the plural of طَرِيق", " — tarîk'in cem'i")),
  ATF_ENC("وَتِجَارَتِهِ", "tijara", "هِ", punct=".")]})

S2.append({"id": "s2", "translation": {"en": "That is because ships would come to it on the Tigris, from the sea and from distant lands.",
                                      "tr": "Çünkü gemiler Dicle üzerinden, denizden ve uzak ülkelerden oraya gelirdi."},
 "tokens": [tok("وَذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "mubtada-khabar"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
    "The waw opens a new sentence; ذٰلِكَ «that» is a demonstrative built on sukun, in the seat of raf' as the mubtada; the lam marks distance and the kaf is a particle of address.",
    "Vâv isti'nâf içindir; zâlike işaret ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû; lâm uzaklık için, kâf hitap harfidir.",
    segments=[seg("وَ", "wa", "conj"), seg("ذٰلِكَ", "dhalika", "pron")]),
  ANNA_T((" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; أَنَّ and what follows stand for a masdar, the predicate of «that», in the seat of raf'", "; enne ve sonrası masdar te'vîlinde olup mübtedânın haberi, mahallen merfû")),
  tok("السُّفُنَ", "safina", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ سَفِينَةٍ.", "The noun of أَنَّ, in nasb — the plural of سَفِينَة.", "Enne'nin ismi, mansûb — sefîne'nin cem'i."),
  MUDARI("تَأْتِيهِ", "ata", enc="هِ", naqis="ي", who="هِيَ",
    note_ar=" — وَالْهَاءُ عَائِدٌ عَلَى الْمَوْضِعِ" + KH_ANNA[0], note_en=" — «it» returns to the site" + KH_ANNA[1], note_tr=" — zamir yere döner" + KH_ANNA[2]),
  FI(), DIJLA_J(), MINA(), MAJR("الْبَحْرِ", "bahr"),
  WA_PREP("وَمِنَ", "min", "مِنَ"), MAJR("الْبِلَادِ", "bilad"), NAAT("الْبَعِيدَةِ", "baid", "jarr", punct=".")]})

S2.append({"id": "s3", "translation": {"en": "The Euphrates was near it, and between the two rivers there were small canals on which ships sailed.",
                                      "tr": "Fırat da oraya yakındı; iki nehrin arasında, üzerlerinde gemilerin yüzdüğü küçük kanallar vardı."},
 "tokens": [KANA("وَكَانَ"), ISMK("الْفُرَاتُ", "furat", "propn"), KHK("قَرِيبًا", "qarib"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ona»)", punct="،", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«قَرِيبًا»", note_en="; the jarr phrase attaches to «near»", note_tr="; câr-mecrûr «yakın»a müteallik"),
  tok("وَبَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"],
    "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ.",
    "The waw conjoins; بَيْنَ «between» is an adverb of place, in nasb and annexed — it hangs on an omitted predicate, placed first.",
    "«ve» + beyne «arasında»: mekân zarfı, mansûb, muzâf — öne alınmış mahzûf habere müteallik.",
    segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun")]),
  MUDAF_ILAYH("النَّهْرَيْنِ", "nahr", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", note_ar=" — يَعْنِي دِجْلَةَ وَالْفُرَاتَ", note_en=" — by the ya, a dual: the Tigris and the Euphrates", note_tr=" — tesniye olduğu için yâ ile: Dicle ve Fırat"),
  MUBTADA("أَنْهَارٌ", "nahr", extra=["jam-taksir"], note_ar="، وَهُوَ مُؤَخَّرٌ — جَمْعُ نَهْرٍ، وَجَازَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ شِبْهِ الْجُمْلَةِ",
    note_en=", placed after its predicate — the plural of نَهْر; an indefinite mubtada is allowed because the adverbial predicate comes first", note_tr=", haberinden sonraya bırakılmış — nehr'in cem'i; zarf haber öne geçtiği için nekire mübtedâ caizdir"),
  NAAT("صَغِيرَةٌ", "saghir", "raf", note_ar=" — وَجَاءَ مُفْرَدًا مُؤَنَّثًا لِأَنَّ جَمْعَ مَا لَا يَعْقِلُ يُوصَفُ بِالْمُفْرَدَةِ الْمُؤَنَّثَةِ",
    note_en=" — singular feminine, because a plural of things without reason takes a feminine singular adjective", note_tr=" — akılsız varlıkların cem'i müfred müennesle vasıflandığı için müfred müennes geldi"),
  MUD_DF("تَجْرِي", "jara", ["jumla-sifa"], naqis=True, note=NAAT_OF("raf", "أَنْهَارٌ", "canals", "kanallar", True)),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onlarda»)", note_ar="، وَهَا عَائِدٌ عَلَى «أَنْهَارٌ» يَرْبِطُ الصِّفَةَ بِالْمَوْصُوفِ", note_en="; «them» returns to «canals» — the bond that ties the clause to its noun", note_tr="; zamir «kanallar»a döner — sıfat cümlesini mevsûfuna bağlar"),
  FAIL("السُّفُنُ", "safina", extra=["jam-taksir"], punct=".")]})

S2.append({"id": "s4", "translation": {"en": "And the roads from Syria, Kufa, Basra and Khurāsān met at it.",
                                      "tr": "Şam'dan, Kûfe'den, Basra'dan ve Horasan'dan gelen yollar da orada birleşirdi."},
 "tokens": [KANAT_K("وَكَانَتِ"), ISMK("الطُّرُقُ", "tariq", extra=["jam-taksir"], note_ar=" — جَمْعُ طَرِيقٍ", note_en=" — the plural of طَرِيق", note_tr=" — tarîk'in cem'i"),
  MUDARI("تَلْتَقِي", "iltaqa", ["form-viii-verbs", "kana-wa-akhawatuha"], naqis="ي", who="هِيَ", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  ZARF_ENC("عِنْدَهُ", "inda", "هُ", note=("، مُتَعَلِّقٌ بِـ«تَلْتَقِي»", "; it attaches to «met»", "; «birleşirdi»ye müteallik")),
  MINA(), MAJR("الشَّامِ", "sham", "propn", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنَ «الطُّرُقُ»، أَيْ: آتِيَةً مِنَ الشَّامِ",
    note_en=" — the jarr phrase hangs on an omitted hal of «the roads»: «coming from Syria»", note_tr=" — câr-mecrûr «yollar»dan mahzûf bir hâle müteallik: «Şam'dan gelerek»"),
  ATF("وَالْكُوفَةِ", "kufa", "propn", "jarr"), ATF("وَالْبَصْرَةِ", "basra", "propn", "jarr"),
  ATF("وَخُرَاسَانَ", "khurasan", "propn", "jarr", extra=["mamnu-min-sarf"], sign="مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ", note_ar=DIPT_KHURASAN[0], note_en=DIPT_KHURASAN[1], note_tr=DIPT_KHURASAN[2], punct=".")]})

S2.append({"id": "s5", "translation": {"en": "And whenever a river and a road come together in a place, trade grows plentiful there.",
                                      "tr": "Bir yerde nehir ile yol bir araya gelince, orada ticaret çoğalır."},
 "tokens": [IDHA("وَإِذَا"),
  MADI("اجْتَمَعَ", "ijtamaa", ["form-viii-verbs", "idha-shartiyya"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا، وَهِيَ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ بَعْدَهُ",
    note_en=" — the clause is in the seat of jarr, annexed to إِذَا: it is the condition; its doer follows", note_tr=" — cümle izâ'ya muzâfun ileyh olarak mahallen mecrûr, şart cümlesidir; fâili ondan sonra gelir"),
  FAIL("النَّهْرُ", "nahr"), ATF("وَالطَّرِيقُ", "tariq", "noun", "raf"), FI(), MAJR("مَوْضِعٍ", "mawdi", punct="،"),
  MADI("كَثُرَتْ", "kathura", ["idha-shartiyya"], fem=True, note_ar=" — وَالْجُمْلَةُ جَوَابُ شَرْطٍ غَيْرِ جَازِمٍ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ، وَالْفَاعِلُ بَعْدَهُ",
    note_en=" — the clause is the answer of a condition that does not govern jazm, with no seat of its own; its doer follows", note_tr=" — cümle câzim olmayan şartın cevabıdır, i'râbdan mahalli yoktur; fâili ondan sonra gelir"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («orada»)", note_ar="، وَالْهَاءُ عَائِدٌ عَلَى «مَوْضِعٍ»", note_en="; the pronoun returns to «a place»", note_tr="; zamir «bir yer»e döner"),
  FAIL("التِّجَارَةُ", "tijara", punct=".")]})

# ======================================== Chapter 3 — الْعُمَّالُ وَالْبِنَاءُ ========================================
S3 = []
S3.append({"id": "s1", "translation": {"en": "Then he sent his envoys to the lands, so that they would gather for him workers and men of craft.",
                                      "tr": "Sonra elçilerini ülkelere gönderdi; ta ki onun için işçileri ve zanaat ehlini toplasınlar."},
 "tokens": [THUMMA(), MADI("بَعَثَ", "baatha", hidden=True),
  ENC_NOUN("رُسُلَهُ", "rasul-msg", "هُ", "maful", extra=["jam-taksir"], note_ar=" — جَمْعُ رَسُولٍ", note_en=" — the plural of رَسُول", note_tr=" — resûl'ün cem'i"),
  ILA(), MAJR("الْبِلَادِ", "bilad"),
  HATTA(), FIVE_NASB("يَجْمَعُوا", "jamaa-gather", by="أَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى", by_en="an أَنْ hidden of necessity after حَتَّى", by_tr="hattâ'dan sonra vücûben gizli en"),
  LAHU(" («onun için»)"),
  MAFUL("الْعُمَّالَ", "amil-worker", extra=["jam-taksir"], note_ar=" — جَمْعُ عَامِلٍ", note_en=" — the plural of عَامِل", note_tr=" — âmil'in cem'i"),
  ATF("وَأَهْلَ", "ahl", "noun", "nasb", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الصَّنْعَةِ", "sana-craft", punct=".")]})

S3.append({"id": "s2", "translation": {"en": "So workers came to him from Syria, Kufa and Basra, and from many other lands.",
                                      "tr": "Bunun üzerine Şam'dan, Kûfe'den ve Basra'dan ve daha birçok ülkeden ona işçiler geldi."},
 "tokens": [ENC_MADI("فَجَاءَهُ", "jaa", "هُ", ["hollow-verbs"], note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  FAIL("الْعُمَّالُ", "amil-worker", extra=["jam-taksir"]), MINA(), MAJR("الشَّامِ", "sham", "propn"),
  ATF("وَالْكُوفَةِ", "kufa", "propn", "jarr"), ATF("وَالْبَصْرَةِ", "basra", "propn", "jarr", punct="،"),
  WA_PREP("وَمِنْ", "min", "مِنْ"), MAJR("بِلَادٍ", "bilad"),
  tok("أُخْرَى", "ukhra", "noun", ["naat-sifa", "ism-maqsur-manqus", "mamnu-min-sarf"],
    "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مُؤَنَّثُ آخَرَ.",
    "An adjective agreeing with «lands», in jarr by a kasra estimated on the alif — the feminine of آخَر «other».",
    "Na't, «ülkeler»e uyar; elif üzerinde takdîrî kesre ile mecrûr — âhar'ın müennesi."),
  NAAT("كَثِيرَةٍ", "kathir", "jarr", note_ar=" — نَعْتٌ ثَانٍ", note_en=" — a second na't", note_tr=" — ikinci na't", punct=".")]})

S3.append({"id": "s3", "translation": {"en": "Among them were men of every craft, and men who knew the art of building.",
                                      "tr": "Aralarında her zanaatın ehli ve inşaatı bilen kimseler vardı."},
 "tokens": [KANA("وَكَانَ"),
  JARR_PRON("فِيهِمْ", "fi", "فِي", "هِمْ", " («onların arasında»)", extra=["kana-wa-akhawatuha"], note_ar=KH_MUQ[0], note_en=KH_MUQ[1], note_tr=KH_MUQ[2]),
  ISMK("أَهْلُ", "ahl", extra=["idafa-definiteness"], muakhkhar=True, note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("كُلِّ", "kull", note_ar=MUDAF[0], note_en=", itself annexed", note_tr=", kendisi de muzâf"),
  MUDAF_ILAYH("صَنْعَةٍ", "sana-craft", punct="،"),
  ATF("وَأَهْلُ", "ahl", "noun", "raf", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الْعِلْمِ", "ilm"),
  BI_NOUN("بِالْبِنَاءِ", "bina", "الْبِنَاءِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«الْعِلْمِ»", note_en=" — the jarr phrase attaches to «knowledge»", note_tr=" — câr-mecrûr «ilim»e müteallik", punct=".")]})

S3.append({"id": "s4", "translation": {"en": "In the year one hundred and forty-five of the Hijra, al-Manṣūr began building the city.",
                                      "tr": "Hicretin yüz kırk beşinci yılında Mansûr şehrin inşasına başladı."},
 "tokens": [WA_PREP("وَفِي", "fi", "فِي", "istinaf"),
  MAJR("سَنَةِ", "sana", extra=["idafa-definiteness"], note_ar="، مُضَافٌ إِلَى الْعَدَدِ بَعْدَهُ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«بَدَأَ»", note_en=", annexed to the number after it — the phrase attaches to «began»", note_tr=", sonraki sayıya muzâf — câr-mecrûr «başladı»ya müteallik"),
  MUDAF_ILAYH("خَمْسٍ", "khams", extra=["asma-al-adad-fil-kafiya"], note_ar=" — وَجَاءَ بِلَا تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ: الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُخَالِفُ الْمَعْدُودَ",
    note_en=" — without the ta, because the thing counted, «year», is feminine: the numbers three to ten take the opposite gender", note_tr=" — ma'dûd «sene» müennes olduğu için tâsız geldi: üçten ona kadar sayılar ma'dûda muhalefet eder"),
  ATF("وَأَرْبَعِينَ", "arbaun", "noun", "jarr", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
    note_en=" — in jarr by the ya, as it declines like a sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  ATF("وَمِائَةٍ", "mia", "noun", "jarr", extra=["asma-al-adad-fil-kafiya"]),
  LI_AL("لِلْهِجْرَةِ", "hijra", "الْهِجْرَةِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنْ «سَنَةِ»، أَيْ: مَحْسُوبَةً مِنَ الْهِجْرَةِ",
    note_en=" — the phrase hangs on an omitted hal: the year as counted from the Hijra, «AH»", note_tr=" — câr-mecrûr mahzûf bir hâle müteallik: hicretten sayılan yıl, «hicrî»"),
  MADI("بَدَأَ", "badaa", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]), MANSUR_F(),
  MAFUL("بِنَاءَ", "bina", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْمَدِينَةِ", "madina", punct=".")]})

S3.append({"id": "s5", "translation": {"en": "With his own hand he laid the first brick in it.",
                                      "tr": "İçine ilk kerpici kendi eliyle koydu."},
 "tokens": [MADI("وَوَضَعَ", "wadaa", ["mithal-verbs"], hidden=True),
  BI_NOUN("بِيَدِهِ", "yad", "يَدِهِ", enc="هِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«وَضَعَ»", note_en=" — the jarr phrase attaches to «laid»", note_tr=" — câr-mecrûr «koydu»ya müteallik"),
  MAFUL("أَوَّلَ", "awwal", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("لَبِنَةٍ", "labina"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", punct=".", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«وَضَعَ»، وَهَا عَائِدَةٌ عَلَى الْمَدِينَةِ",
    note_en="; the jarr phrase attaches to «laid», and «it» returns to the city", note_tr="; câr-mecrûr «koydu»ya müteallik; zamir şehre döner")]})

S3.append({"id": "s6", "translation": {"en": "They built it with a strong building, while al-Manṣūr looked on at their work.",
                                      "tr": "Onu sağlam bir yapıyla inşa ettiler; Mansûr da onların işine bakıyordu."},
 "tokens": [tok("فَبَنَوْهَا", "bana", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
    FA_AR + "بَنَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَوَاوُ الْجَمَاعَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "The fa conjoins; «they built it» — a past naqis verb built on a damma estimated on the alif that dropped before the waw of the group (بَنَى + وا → بَنَوْا); the waw is the doer and the attached «it» the object.",
    "Fâ atıf; «onu inşa ettiler» — cemâat vâvından önce düşen elif üzerinde takdîrî damme ile mebnî nâkıs mâzî (benâ + vâv → benev); vâv fâil, bitişik «onu» mef'ûlün bih.",
    segments=[seg("فَ", "fa", "conj"), seg("بَنَوْ", "bana", "verb"), seg("هَا", "pron-3fs", "pron")]),
  MUTLAQ_NAW("بِنَاءً", "bina", "بَنَى", "built", "inşa ettiler"), NAAT("قَوِيًّا", "qawi", "nasb", punct="،"),
  tok("وَالْمَنْصُورُ", "mansur-caliph", "propn", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"],
    "الْوَاوُ حَالِيَّةٌ، وَالْمَنْصُورُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens a hal clause; «al-Manṣūr» is the mubtada, in raf' — the nominal clause is a hal, in the seat of nasb.",
    "Hâl vâvı; «Mansûr» mübtedâ, merfû — isim cümlesi hâl olarak mahallen mansûb.",
    segments=[seg("وَ", "wa", "conj"), seg("الْمَنْصُورُ", "mansur-caliph", "propn")]),
  MUDARI("يَنْظُرُ", "nazara", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]), ILA(),
  ENC_NOUN("عَمَلِهِمْ", "amal-work", "هِمْ", "majr", punct=".")]})

# ======================================== Chapter 4 — الْمَدِينَةُ الْمُسْتَدِيرَةُ ========================================
S4 = []
S4.append({"id": "s1", "translation": {"en": "He made it round, built two walls around it, and dug a moat around them both.",
                                      "tr": "Onu yuvarlak yaptı, etrafına iki sur yaptırdı ve ikisinin çevresine bir hendek kazdırdı."},
 "tokens": [ENC_MADI("وَجَعَلَهَا", "jaala", "هَا", ["mafulayn"], hidden=True,
    note_ar=" أَوَّلُ — وَجَعَلَ هُنَا بِمَعْنَى صَيَّرَ، فَنَصَبَ مَفْعُولَيْنِ", note_en=" — the first of two: جَعَلَ here means «made into», so it takes two objects", note_tr=" — birincisi: ce'ale burada «kıldı» anlamında olduğu için iki mef'ûl alır"),
  MAF2("مُسْتَدِيرَةً", "mustadir", extra=["ism-fail"], punct="،", note=(" — اسْمُ فَاعِلٍ مِنِ اسْتَدَارَ", " — the active participle of اسْتَدَارَ «to be round»", " — istedâra'nın ism-i fâili")),
  MADI_ALIF("وَبَنَى", "bana", hidden=True),
  ZARF_ENC("حَوْلَهَا", "hawl", "هَا", note=("، مُتَعَلِّقٌ بِـ«بَنَى»", "; it attaches to «built»", "; «yaptı»ya müteallik")),
  MAFUL("سُورَيْنِ", "sur-wall", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", note_en=" — by the ya, a dual", note_tr=" — tesniye olduğu için yâ ile", punct="،"),
  MADI("وَحَفَرَ", "hafara", hidden=True),
  ZARF_ENC("حَوْلَهُمَا", "hawl", "هُمَا", note=("، وَهُمَا عَائِدٌ عَلَى السُّورَيْنِ", "; «them both» returns to the two walls", "; zamir iki sura döner")),
  MAFUL("خَنْدَقًا", "khandaq", punct=".")]})

S4.append({"id": "s2", "translation": {"en": "He gave it four gates: the Kufa Gate, the Basra Gate, the Khurāsān Gate and the Syria Gate.",
                                      "tr": "Ona dört kapı yaptı: Kûfe Kapısı, Basra Kapısı, Horasan Kapısı ve Şam Kapısı."},
 "tokens": [MADI("وَجَعَلَ", "jaala", hidden=True),
  LAHA(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«جَعَلَ»", "; the jarr phrase attaches to «made»", "; câr-mecrûr «yaptı»ya müteallik")),
  MAFUL("أَرْبَعَةَ", "arbaa", extra=["asma-al-adad-fil-kafiya", "idafa-definiteness"], note_ar="، مُضَافٌ — وَجَاءَ الْعَدَدُ بِالتَّاءِ لِأَنَّ مُفْرَدَ الْمَعْدُودِ (بَابٌ) مُذَكَّرٌ",
    note_en=", annexed — the number takes the ta because the singular of the counted noun (بَاب) is masculine", note_tr=", muzâf — sayılanın müfredi (bâb) müzekker olduğu için sayı tâ ile gelmiştir"),
  MUDAF_ILAYH("أَبْوَابٍ", "bab", extra=["jam-taksir", "asma-al-adad-fil-kafiya"], punct=":",
    note_ar=" — تَمْيِيزُ الْعَدَدِ: جَمْعٌ مَجْرُورٌ بِالْإِضَافَةِ، وَهُوَ جَمْعُ بَابٍ", note_en=" — the counted noun after 3–10: a plural in jarr by the idafa (the plural of بَاب)", note_tr=" — sayının temyîzi: izâfetle mecrûr cem' (bâb'ın cem'i)"),
  tok("بَابَ", "bab", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "idafa-definiteness"],
    "بَدَلٌ مِنْ «أَرْبَعَةَ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — بَدَلُ تَفْصِيلٍ يُفَصِّلُ الْعَدَدَ الْمُجْمَلَ.",
    "A badal of «four», in nasb and annexed — a badal of detail that spells out the number given in sum.",
    "«dört»ten bedel, mansûb, muzâf — mücmel sayıyı tafsil eden bedel."),
  MUDAF_ILAYH("الْكُوفَةِ", "kufa", "propn", punct="،"),
  ATF("وَبَابَ", "bab", "noun", "nasb", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْبَصْرَةِ", "basra", "propn", punct="،"),
  ATF("وَبَابَ", "bab", "noun", "nasb", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("خُرَاسَانَ", "khurasan", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_KHURASAN[0], note_en=DIPT_KHURASAN[1], note_tr=DIPT_KHURASAN[2], punct="،"),
  ATF("وَبَابَ", "bab", "noun", "nasb", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الشَّامِ", "sham", "propn", punct=".")]})

S4.append({"id": "s3", "translation": {"en": "Each gate was named after the land to which its road leads out.",
                                      "tr": "Her kapıya, yolunun çıktığı ülkenin adı verildi."},
 "tokens": [tok("وَسُمِّيَ", "samma", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs", "naqis-verbs"],
    WA_AR + "سُمِّيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — وَسَمَّى يَتَعَدَّى إِلَى الِاسْمِ هُنَا بِالْبَاءِ.",
    "The waw conjoins; «was named» is a past verb in the passive, built on fatha — سَمَّى reaches the name here through the ba.",
    "«ve» + meçhul mâzî, fetha üzere mebnî — sammâ burada isme bâ ile geçer.",
    segments=[seg("وَ", "wa", "conj"), seg("سُمِّيَ", "samma", "verb")]),
  NAIB("كُلُّ", "kull", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("بَابٍ", "bab"),
  BI_NOUN("بِاسْمِ", "ism-name", "اسْمِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«سُمِّيَ»", note_en="; it is annexed, and the jarr phrase attaches to «was named»", note_tr="; muzâf — câr-mecrûr «adlandırıldı»ya müteallik"),
  MUDAF_ILAYH("الْبَلَدِ", "balad"),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«الْبَلَدِ».",
    "A relative pronoun «which», built on sukun, in the seat of jarr as a na't of «the land».", "İsm-i mevsûl «ki o», sükûn üzere mebnî, «ülke»nin na'tı olarak mahallen mecrûr."),
  MUD_DF("يَخْرُجُ", "kharaja", ["ism-mawsul"], note=SILA),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)", note_ar="، وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en="; the pronoun is the one that returns to the relative (the ʿāʾid)", note_tr="; zamir mevsûle dönen âiddir"),
  ENC_NOUN("طَرِيقُهُ", "tariq", "هُ", "fail", punct=".", note_ar=" — وَالْهَاءُ عَائِدَةٌ عَلَى «بَابٍ»", note_en=" — «its» returns to «gate»", note_tr=" — zamir «kapı»ya döner")]})

S4.append({"id": "s4", "translation": {"en": "In its centre he built his palace and the congregational mosque.",
                                      "tr": "Ortasına sarayını ve ulu camiyi yaptırdı."},
 "tokens": [MADI_ALIF("وَبَنَى", "bana", hidden=True), FI(), ENC_NOUN("وَسَطِهَا", "wasat", "هَا", "majr"),
  ENC_NOUN("قَصْرَهُ", "qasr-palace", "هُ", "maful"), ATF("وَالْمَسْجِدَ", "masjid", "noun", "nasb"),
  NAAT("الْجَامِعَ", "jami-mosque", "nasb", ["ism-fail"], note_ar=" — اسْمُ فَاعِلٍ مِنْ جَمَعَ: الْمَسْجِدُ الَّذِي تُصَلَّى فِيهِ الْجُمُعَةُ", note_en=" — the active participle of جَمَعَ: the mosque where the Friday prayer is held", note_tr=" — cemea'nın ism-i fâili: cuma namazı kılınan mescid", punct=".")]})

S4.append({"id": "s5", "translation": {"en": "Above the palace was a green dome that people could see from afar.",
                                      "tr": "Sarayın üstünde, insanların uzaktan gördüğü yeşil bir kubbe vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  ZARF("فَوْقَ", "fawqa", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ مُقَدَّمٌ", note_en="; it hangs on the omitted, FRONTED predicate of كَانَ", note_tr="; kâne'nin öne alınmış mahzûf haberine müteallik"),
  MUDAF_ILAYH("الْقَصْرِ", "qasr-palace"),
  ISMK("قُبَّةٌ", "qubba", muakhkhar=True),
  tok("خَضْرَاءُ", "khadra-green", "noun", ["naat-sifa", "mamnu-min-sarf"],
    "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ، مُؤَنَّثُ أَخْضَرَ.",
    "An adjective agreeing with «a dome», in raf' by a damma without tanwin — barred from tanwin by its long feminine ending; the feminine of أَخْضَر.",
    "Na't, merfû; tenvinsiz damme — memdûde te'nîs elifi sebebiyle gayr-i munsarif; ahdar'ın müennesi."),
  tok("يَرَاهَا", "raa", "verb", ["mudari-marfu", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "jumla-sifa"],
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَهُوَ الْعَائِدُ عَلَى «قُبَّةٌ»، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«قُبَّةٌ».",
    "Present verb in raf' by a damma estimated on the alif; «it» is its object, placed before the doer, which follows, and it is the pronoun that returns to «a dome» — the clause is a second na't of «a dome», in the seat of raf'.",
    "Merfû muzâri, elif üzerinde takdîrî damme ile; «onu» zamiri fâilden önce gelmiş mef'ûlün bih ve «kubbe»ye dönen âiddir; fâili ondan sonra gelir — cümle «kubbe»nin ikinci na'tı, mahallen merfû.",
    segments=[seg("يَرَا", "raa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  FAIL("النَّاسُ", "nas"), MIN(),
  MAJR("بَعِيدٍ", "baid", note_ar=" — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: مِنْ مَكَانٍ بَعِيدٍ", note_en=" — an adjective whose noun is omitted: «from a distant place»", note_tr=" — mevsûfu hazfedilmiş sıfat: «uzak bir yerden»", punct=".")]})

S4.append({"id": "s6", "translation": {"en": "And he named it Madīnat al-Salām, the City of Peace.",
                                      "tr": "Ve ona Medînetü's-Selâm, yani Barış Şehri adını verdi."},
 "tokens": [ENC_MADI("وَسَمَّاهَا", "samma", "هَا", ["form-ii-verbs", "mafulayn"], alif=True, hidden=True,
    note_ar=" أَوَّلُ، وَسَمَّى يَنْصِبُ مَفْعُولَيْنِ", note_en=" — the first of two: سَمَّى takes two objects", note_tr=" — birincisi: sammâ iki mef'ûl alır"),
  PH(MAF2("مَدِينَةَ", "madina", extra=["idafa-definiteness"], note=MUDAF), "madinat-al-salam"),
  MUDAF_ILAYH("السَّلَامِ", "salam", punct=".")]})

# ============================================ Chapter 5 — دَارُ الْعِلْمِ ============================================
S5 = []
S5.append({"id": "s1", "translation": {"en": "Only a few years passed before people and markets multiplied in it.",
                                      "tr": "Aradan birkaç yıl geçmişti ki orada insanlar ve çarşılar çoğaldı."},
 "tokens": [tok("فَمَا", "ma-nafiya", "part", ["la-nafiya"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَمَا حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ مَعَ الْفِعْلِ.",
    "The fa opens a new sentence; مَا negates the verb after it and governs nothing.", "Fâ isti'nâf içindir; mâ nefiy harfi, fiil önünde amel etmez.",
    segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  MADI_ALIF("مَضَى", "mada", note_ar=" — وَلَمْ تَلْحَقْهُ تَاءُ التَّأْنِيثِ وَفَاعِلُهُ مُؤَنَّثٌ لِأَنَّ «إِلَّا» فَصَلَتْ بَيْنَهُمَا، وَالتَّذْكِيرُ مَعَ هٰذَا الْفَصْلِ هُوَ الْمُخْتَارُ",
    note_en=" — no feminine ta although its doer is feminine, because إِلَّا stands between them: with that separation the masculine is the preferred usage",
    note_tr=" — fâili müennes olduğu hâlde te'nîs tâsı almadı, çünkü aralarına «illâ» girdi; bu ayrılıkla müzekker kullanım tercih edilir"),
  ILLA(),
  FAIL("سَنَوَاتٌ", "sana", extra=["jam-muannath-salim"], note_ar=" — وَهُوَ الْمُسْتَثْنَى الْمُفَرَّغُ، جَمْعُ سَنَةٍ جَمْعَ مُؤَنَّثٍ سَالِمًا", note_en=" — the emptied exception itself; the sound feminine plural of سَنَة", note_tr=" — müferrağ müstesnânın kendisi; sene'nin cem-i müennes sâlimi"),
  NAAT("قَلِيلَةٌ", "qalil", "raf"),
  HATTA_IBT(), MADI("كَثُرَ", "kathura", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («orada»)"), FAIL("النَّاسُ", "nas"),
  ATF("وَالْأَسْوَاقُ", "suq", "noun", "raf", extra=["jam-taksir"], note_ar=" — جَمْعُ سُوقٍ", note_en=" — the plural of سُوق", note_tr=" — sûk'un cem'i", punct=".")]})

S5.append({"id": "s2", "translation": {"en": "Scholars travelled to it from every land, bringing their books with them.",
                                      "tr": "Her ülkeden âlimler, kitapları yanlarında, oraya göç etti."},
 "tokens": [MADI("وَرَحَلَ", "rahala", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  JARR_PRON("إِلَيْهَا", "ila", "إِلَيْ", "هَا", " («oraya»)"),
  FAIL("الْعُلَمَاءُ", "alim-scholar", extra=["jam-taksir"], note_ar=" — جَمْعُ عَالِمٍ", note_en=" — the plural of عَالِم", note_tr=" — âlim'in cem'i"),
  MIN(), MAJR("كُلِّ", "kull", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("بَلَدٍ", "balad", punct="،"),
  tok("وَمَعَهُمْ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "al-hal-jumla-wa-rabituha"],
    "الْوَاوُ حَالِيَّةٌ، وَمَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ.",
    "The waw opens a hal clause; مَعَ «with» is an adverb of place in nasb, annexed to «them» (in the seat of jarr) — it hangs on an omitted predicate, placed first.",
    "Hâl vâvı; mea' «ile» mekân zarfı, mansûb; «onlar» zamirine muzâf, zamir mahallen mecrûr — öne alınmış mahzûf habere müteallik.",
    segments=[seg("وَ", "wa", "conj"), seg("مَعَ", "maa", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  ENC_NOUN("كُتُبُهُمْ", "kitab", "هُمْ", "mubtada", extra=["jam-taksir", "al-hal-jumla-wa-rabituha"], punct=".",
    note_ar=" — وَالْمُبْتَدَأُ مُؤَخَّرٌ، وَهُوَ جَمْعُ كِتَابٍ؛ وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الْعُلَمَاءُ»",
    note_en=" — placed after its predicate; the plural of كِتَاب. The nominal clause is a hal of «the scholars», in the seat of nasb",
    note_tr=" — haberinden sonraya bırakılmış; kitâb'ın cem'i. İsim cümlesi «âlimler»den hâl, mahallen mansûb")]})

S5.append({"id": "s3", "translation": {"en": "So it became one of the greatest cities in the world for learning.",
                                      "tr": "Böylece ilim bakımından dünyanın en büyük şehirlerinden biri oldu."},
 "tokens": [tok("فَصَارَتْ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    FA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى بَغْدَادَ.",
    "The fa conjoins; صَارَ «became» is a defective past verb, a sister of كَانَ, built on fatha; the ta marks the feminine, and its noun is the hidden «it», returning to Baghdad.",
    "Fâ atıf; sâra «oldu»: kâne'nin kardeşlerinden, fetha üzere mebnî nâkıs mâzî; tâ te'nîs içindir; ismi Bağdat'a dönen gizli zamir «o».",
    segments=[seg("فَ", "fa", "conj"), seg("صَارَتْ", "sara", "verb")]),
  MIN(),
  MAJR("أَعْظَمِ", "azam", extra=["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ جُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ",
    note_en=", annexed — an elative, which takes the kasra because it is annexed; the jarr phrase is the predicate of صَارَ, in the seat of nasb",
    note_tr=", muzâf — ism-i tafdîl, muzâf olduğu için kesre ile mecrûr; câr-mecrûr sâra'nın haberi, mahallen mansûb"),
  MUDAF_ILAYH("مُدُنِ", "madina", extra=["jam-taksir"], note_ar="، مُضَافٌ — جَمْعُ مَدِينَةٍ", note_en=", itself annexed — the plural of مَدِينَة", note_tr=", kendisi de muzâf — medîne'nin cem'i"),
  MUDAF_ILAYH("الدُّنْيَا", "dunya", extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_en=" — the kasra is estimated on the alif", note_tr=" — kesre elif üzerinde takdîrî"),
  TAMYIZ_T("عِلْمًا", "ilm", *TAFDIL_TAMYIZ, punct=".")]})

S5.append({"id": "s4", "translation": {"en": "In it al-Ṭabarī wrote his great History.",
                                      "tr": "Taberî büyük Tarih'ini orada yazdı."},
 "tokens": [MADI("وَكَتَبَ", "kataba", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («orada»)"),
  FAIL("الطَّبَرِيُّ", "tabari", "propn", note_ar=" — نِسْبَةٌ إِلَى طَبَرِسْتَانَ صَارَتْ عَلَمًا عَلَيْهِ", note_en=" — a nisba to Ṭabaristān that became his name", note_tr=" — Taberistan'a nispet olup onun adı olmuştur"),
  ENC_NOUN("تَارِيخَهُ", "tarikh", "هُ", "maful"), NAAT("الْكَبِيرَ", "kabir", "nasb", punct=".")]})

S5.append({"id": "s5", "translation": {"en": "And al-Khaṭīb al-Baghdādī gathered its reports, and the reports of its scholars, in a book that he named «The History of Baghdad».",
                                      "tr": "Hatîb el-Bağdâdî de onun haberlerini ve âlimlerinin haberlerini, «Bağdat Tarihi» adını verdiği bir kitapta topladı."},
 "tokens": [MADI("وَجَمَعَ", "jamaa-gather", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  PH(FAIL("الْخَطِيبُ", "khatib-preacher", note_ar=" — لَقَبُ أَبِي بَكْرٍ أَحْمَدَ بْنِ عَلِيٍّ", note_en=" — the title of Abū Bakr Aḥmad ibn ʿAlī", note_tr=" — Ebû Bekir Ahmed b. Ali'nin lakabı"), "al-khatib-al-baghdadi"),
  NAAT("الْبَغْدَادِيُّ", "baghdadi", "raf", ["ism-mansub"], note_ar=" — اسْمٌ مَنْسُوبٌ إِلَى بَغْدَادَ", note_en=" — a nisba adjective, «of Baghdad»", note_tr=" — Bağdat'a nisbet edilmiş isim"),
  ENC_NOUN("أَخْبَارَهَا", "khabar", "هَا", "maful", extra=["jam-taksir"], note_ar=" — جَمْعُ خَبَرٍ", note_en=" — the plural of خَبَر", note_tr=" — haber'in cem'i"),
  ATF("وَأَخْبَارَ", "khabar", "noun", "nasb", extra=["idafa-definiteness", "jam-taksir"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ENC_NOUN("عُلَمَائِهَا", "alim-scholar", "هَا", "mudaf", extra=["jam-taksir"], note_ar="، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ وَإِنْ كَانَ عَلَى وَزْنِ فُعَلَاءَ",
    note_en=" — a diptote pattern (فُعَلَاء), but annexed, so it takes the kasra", note_tr=" — fu'alâ' vezninde gayr-i munsarif iken muzâf olduğu için kesre ile"),
  FI(), MAJR("كِتَابٍ", "kitab"),
  ENC_MADI("سَمَّاهُ", "samma", "هُ", ["form-ii-verbs", "mafulayn", "jumla-sifa"], alif=True, hidden=True,
    note_ar=" أَوَّلُ، وَهُوَ الْعَائِدُ عَلَى «كِتَابٍ»" + NAAT_OF("jarr", "كِتَابٍ", "a book", "kitap")[0],
    note_en=" — the first of two, and the pronoun that returns to «a book»" + NAAT_OF("jarr", "كِتَابٍ", "a book", "kitap")[1],
    note_tr=" — birincisi; «kitap»a dönen âid zamir" + NAAT_OF("jarr", "كِتَابٍ", "a book", "kitap")[2]),
  MAF2("تَارِيخَ", "tarikh", extra=["idafa-definiteness"], note=("، مُضَافٌ — وَهُوَ اسْمُ الْكِتَابِ", ", annexed — the book's title", ", muzâf — kitabın adı")),
  BAGHDAD_MI(punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-viii-verbs", "form-x-verbs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            g = t.get("grammar", [])
            if DERIVED & set(g): g = [x for x in g if x != "thulathi-mujarrad-babs"]
            t["grammar"] = list(dict.fromkeys(g))

# ---- the lexicon: every key by lemma identity from the shelf (the majority reading of a key wins) -------------------------
PKGS = sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
_M = {p: (json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
          if (ROOT / "content/samples" / p / "morphology.json").exists() else {}) for p in PKGS}
DIA_ = re.compile("[ً-ٰ]")
def _lemma_id(e): return DIA_.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))
# keys whose first majority holder carries a gloss written for another context — pinned to a package whose gloss is plain
FORCE = {"kitab": "jumal-al-tadrib", "inda": "talkhis-al-miftah"}
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
 "mansur-caliph": {"lemma": "الْمَنْصُور", "pos": "propn", "gloss": {"en": "al-Manṣūr — Abū Jaʿfar ʿAbd Allāh al-Manṣūr (d. 158 / 775), the second ʿAbbāsid caliph and the founder of Baghdad; the title means «the one granted victory»", "tr": "Mansûr — Ebû Ca'fer Abdullah el-Mansûr (ö. 158 / 775), ikinci Abbâsî halifesi ve Bağdat'ın kurucusu; lakap «zafer verilmiş» demektir"}, "level": 5},
 "dijla": {"lemma": "دِجْلَة", "pos": "propn", "gloss": {"en": "the Tigris (a diptote: a feminine proper name)", "tr": "Dicle nehri (gayr-i munsarif: müennes özel isim)"}, "level": 5},
 "khurasan": {"lemma": "خُرَاسَان", "pos": "propn", "gloss": {"en": "Khurāsān — the great eastern province of the caliphate (a diptote)", "tr": "Horasan — hilâfetin büyük doğu eyaleti (gayr-i munsarif)"}, "level": 5},
 "labina": {"lemma": "لَبِنَة", "root": "ل ب ن", "pos": "noun", "gloss": {"en": "a brick of sun-dried clay", "tr": "kerpiç (güneşte kurutulmuş tuğla)"}, "level": 5},
 "khandaq": {"lemma": "خَنْدَق", "root": "خ ن د ق", "pos": "noun", "plural": "خَنَادِق", "gloss": {"en": "a moat, a trench (pl. خَنَادِق)", "tr": "hendek (çoğ. hanâdik)"}, "level": 5},
 "qasr-palace": {"lemma": "قَصْر", "root": "ق ص ر", "pos": "noun", "plural": "قُصُور", "gloss": {"en": "a palace, a castle (pl. قُصُور)", "tr": "saray, köşk (çoğ. kusûr)"}, "level": 4},
 "jami-mosque": {"lemma": "جَامِع", "root": "ج م ع", "pos": "noun", "plural": "جَوَامِع", "gloss": {"en": "gathering (the active participle of جَمَعَ); الْمَسْجِدُ الْجَامِعُ: the congregational mosque, where the Friday prayer is held (pl. جَوَامِع)", "tr": "toplayan (cemea'nın ism-i fâili); el-mescidü'l-câmi': cuma namazı kılınan ulu cami (çoğ. cevâmi')"}, "level": 5},
 "tabari": {"lemma": "الطَّبَرِيّ", "pos": "propn", "gloss": {"en": "al-Ṭabarī — Muḥammad ibn Jarīr al-Ṭabarī (d. 310 / 923), the historian and Qurʾān commentator who lived in Baghdad; a nisba to Ṭabaristān", "tr": "Taberî — Muhammed b. Cerîr et-Taberî (ö. 310 / 923), Bağdat'ta yaşamış tarihçi ve müfessir; Taberistan'a nispet"}, "level": 5},
 "baghdadi": {"lemma": "بَغْدَادِيّ", "pos": "noun", "gloss": {"en": "of Baghdad, a Baghdadi (the nisba of بَغْدَاد)", "tr": "Bağdatlı (بَغْدَاد'a nisbe)"}, "level": 5},
 "madinat-al-salam": PHRASE("مَدِينَةُ السَّلَامِ", 5, "Madīnat al-Salām, «the City of Peace» — the name al-Manṣūr gave his round city, Baghdad",
    "Medînetü's-Selâm, «Barış Şehri» — Mansûr'un yuvarlak şehrine, Bağdat'a verdiği ad",
    "literally «the city of peace»", "lafzen «barış şehri»",
    "An idafa: مَدِينَة carries the case of its seat (here the second object of سَمَّى), and السَّلَام is always in jarr.",
    "Bir izâfettir: مَدِينَة yerinin i'râbını taşır (burada sammâ'nın ikinci mef'ûlü), السَّلَام daima mecrûrdur."),
 "al-khatib-al-baghdadi": PHRASE("الْخَطِيبُ الْبَغْدَادِيُّ", 5, "al-Khaṭīb al-Baghdādī — Abū Bakr Aḥmad ibn ʿAlī (d. 463 / 1071), the ḥadīth scholar who wrote Tārīkh Baghdād",
    "Hatîb el-Bağdâdî — Ebû Bekir Ahmed b. Ali (ö. 463 / 1071), Târîhu Bağdâd'ı yazan hadis âlimi",
    "literally «the preacher of Baghdad»", "lafzen «Bağdatlı hatip»",
    "A title and a nisba: الْخَطِيب «the preacher» is his laqab and carries the case of its seat; الْبَغْدَادِيّ «of Baghdad» follows it as an adjective in the same case.",
    "Bir lakap ve bir nisbe: الْخَطِيب «hatip» onun lakabıdır ve yerinin i'râbını taşır; الْبَغْدَادِيّ «Bağdatlı» ona sıfat olarak aynı i'râbla uyar."),
}
# a key is a global claim: a NEW key must not already be on the shelf — nor in a sibling story staged in the same wave — with
# another lemma (the same lemma under the same key is one word, and then the entry must match)
STAGED = pathlib.Path(os.environ.get("QISSA_STAGED_ROOT", str(OUT_ROOT)))
_STG = {}
if STAGED.exists() and STAGED.resolve() != (ROOT / "content/samples").resolve():
    for d in STAGED.iterdir():
        if d.name != SLUG and (d / "glossary.json").exists():
            _STG[d.name + "*"] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
for k in NEW_GLOSS:
    for p, gl in list(_G.items()) + list(_STG.items()):
        if k in gl and _lemma_id(gl[k]) != _lemma_id(NEW_GLOSS[k]):
            raise SystemExit(f"new key {k!r} already exists in {p} with another lemma")
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
 "title": {"ar": "بِنَاءُ بَغْدَادَ", "en": "The Building of Baghdad", "tr": "Bağdat'ın Kuruluşu"},
 "subtitle": {"ar": "الْخَلِيفَةُ الْمَنْصُورُ يَخْتَارُ مَوْضِعًا عَلَى دِجْلَةَ وَيَبْنِي مَدِينَةَ السَّلَامِ الْمُسْتَدِيرَةَ — قِصَّةٌ لِلْمُسْتَوَى الْخَامِسِ",
              "en": "The caliph al-Manṣūr chooses a site on the Tigris and builds the round City of Peace — a story for the fifth level",
              "tr": "Halife Mansûr Dicle kıyısında bir yer seçer ve yuvarlak Barış Şehri'ni kurar — beşinci seviye için bir hikâye"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "قِصَّةٌ تَارِيخِيَّةٌ أَصْلِيَّةٌ (الْمُسْتَوَى الْخَامِسُ) تَرْوِي بِنَاءَ الْخَلِيفَةِ أَبِي جَعْفَرٍ الْمَنْصُورِ مَدِينَةَ بَغْدَادَ سَنَةَ ١٤٥ هـ، أُلِّفَتْ عَلَى مَا اتَّفَقَ عَلَيْهِ الطَّبَرِيُّ فِي «تَارِيخِ الرُّسُلِ وَالْمُلُوكِ» وَالْخَطِيبُ الْبَغْدَادِيُّ فِي «تَارِيخِ بَغْدَادَ». لَيْسَتْ فِيهَا جُمْلَةٌ هِيَ نَصُّ مَصْدَرٍ، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا يُنْسَبُ فِيهَا إِلَى الْمَنْصُورِ كَلَامٌ عَلَى أَنَّهُ لَفْظُهُ؛ وَتُرِكَتْ أَعْدَادُ الْعُمَّالِ وَالنَّفَقَاتِ لِاخْتِلَافِ الرِّوَايَاتِ، وَتُرِكَ خَبَرُ الْمُنَجِّمِينَ. كُلُّ إِعْرَابٍ فِيهَا اجْتِهَادُ الْمُؤَلِّفِ، وَهِيَ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "ORIGINAL Level-5 graded Arabic: a historical narrative of how the ʿAbbāsid caliph Abū Jaʿfar al-Manṣūr chose a site on the Tigris and built Baghdad, the round city he named Madīnat al-Salām, from 145 AH — composed for this reader from the well-attested core of the event as al-Ṭabarī tells it in his Taʾrīkh al-rusul wa-l-mulūk (under the years 145–146) and al-Khaṭīb al-Baghdādī in the opening part of his Taʾrīkh Baghdād. No sentence is a quotation from any source; no verse or ḥadīth is quoted; al-Manṣūr's reasons for the site are told in the narrator's words and nothing is put in his mouth as his recorded speech. The numbers of workers and the costs (the reports differ) and the astrologers' part of the story are left out. Every iʿrāb line is the author's own analysis, pending scholarly review.",
  "tr": "ÖZGÜN 5. seviye kolaylaştırılmış Arapça: Abbâsî halifesi Ebû Ca'fer el-Mansûr'un 145 / 762 yılından itibaren Dicle kıyısında bir yer seçip Medînetü's-Selâm adını verdiği yuvarlak şehir Bağdat'ı kuruşunun tarihî anlatısı — Taberî'nin Târîhu'r-rusül ve'l-mülûk'ünde (145–146 yılları altında) ve Hatîb el-Bağdâdî'nin Târîhu Bağdâd'ının giriş kısmında anlatılan sağlam çekirdeğe dayanılarak bu okuyucu için yazılmıştır. Hiçbir cümle herhangi bir kaynaktan alıntı değildir; âyet ya da hadis aktarılmamıştır; Mansûr'un yeri seçme sebepleri anlatıcının kendi sözleriyle verilmiş, ona lafzen söylenmiş bir söz isnat edilmemiştir. İşçi sayıları ve harcamalar (rivayetler farklıdır) ile müneccimlere dair kısım dışarıda bırakılmıştır. Her i'râb satırı yazarın kendi tahlilidir ve ilmî incelemeyi beklemektedir.",
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
