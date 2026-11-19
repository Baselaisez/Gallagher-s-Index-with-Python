"""Author content/samples/muallaqat-antara — «مُعَلَّقَةُ عَنْتَرَةَ بْنِ شَدَّادٍ», a RECEIVED text at Level 6 (Master).

Twelve chapters. Chapter 1 is the poet's khabar, VERBATIM from Ibn Qutayba, «الشعر والشعراء» (Dār al-Ḥadīth, Cairo 1423,
1/244–245, § 419, whole; shamela.ws/book/23785/237–238). Chapters 2–12 are the WHOLE Muʿallaqa — all 75 verses of
al-Zawzanī's recension, in his order and count («شرح المعلقات السبع», shamela.ws/book/11253/268–288): PLAN (in the tail)
cuts verses 1–75 into eleven chapters of 6–8 verses, none left out and no run skipped. A verse is ONE sentence; the last
token of its first hemistich carries punctAfter "•". The metre is al-kāmil; the rawī is a mīm with kasra, the rhyme unbound.

The iʿrāb of every verse token was checked against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب المعلقات العشر
الطوال» (shamela.ws/book/151017/674–803) and is written in the shelf's own wording; where he gives two readings the first
is given and the second mentioned. The meanings and the glosses of the rare words are al-Zawzanī's. The balāgha is named on
the token that carries it, after the syntax, in the categories of al-Qazwīnī's Talkhīṣ, on one of two bases the line states:
a commentator names or describes the figure, or — «عَلَى حَدِّ التَّلْخِيصِ» — it meets the Talkhīṣ's own definition.
The verbatim source pages live in research/sources/muallaqat-antara-src.txt.

THE POEM IS AUTHORED IN STAGES. Each verse is filed by its number — V(n, en, tr, first, second) fills VERSE[n] — and the
writer at the foot publishes only the chapters whose verses are ALL authored, contiguously from verse 1. The manifest
attribution is BUILT from what is published. DIV lists every departure from the edition's print with its witness; FLAGS
the editorial vowels left for the scholar.

Regenerate with:  QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_antara.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-antara"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import tok, seg      # the shared token builder (NFC-normalises every Arabic string)
import sarf_gen as _sg

N = lambda s: unicodedata.normalize("NFC", s)

# =====================================================================================================================
# The line-builder. An iʿrāb line is a chain of fragments; a fragment is (ar, en, tr) and carries the grammar notes it
# teaches. J() joins the chain, closes it with a full stop and capitalises the English and the Turkish.
# =====================================================================================================================
class Fr(tuple):
    def __new__(cls, ar, en, tr, *g):
        o = tuple.__new__(cls, (ar, en, tr)); o.g = list(g); return o
def _cap(s, tr=False):
    if not s: return s
    if tr and s[0] == "i": return "İ" + s[1:]
    if tr and s[0] == "ı": return "I" + s[1:]
    return s[0].upper() + s[1:]
def J(*parts):
    parts = [p for p in parts if p]
    ar = "".join(p[0] for p in parts); en = "".join(p[1] for p in parts); tr = "".join(p[2] for p in parts)
    for x in (ar, en, tr): assert not x.rstrip().endswith((".", "،", ";")), x
    g = [x for p in parts for x in getattr(p, "g", [])]
    return Fr(N(ar) + ".", _cap(en) + ".", _cap(tr, True) + ".", *dict.fromkeys(g))
def W(full, lex, pos, *parts, g=None, p=None, s=None):
    """one token: surface, key, part of speech, the fragments of its line; g = more grammar notes, p = the mark after it,
    s = the clitic chain as (form, key, pos) triples"""
    line = J(*parts)
    return tok(full, lex, pos, list(dict.fromkeys(line.g + (g or []))), line[0], line[1], line[2], punct=p,
               segments=[seg(*x) for x in s] if s else None)
def n(full, lex, *parts, **k): return W(full, lex, "noun", *parts, **k)
def v(full, lex, *parts, **k): return W(full, lex, "verb", *parts, **k)
def pn(full, lex, *parts, **k): return W(full, lex, "propn", *parts, **k)
def pt(full, lex, *parts, **k): return W(full, lex, "part", *parts, **k)
def pp(full, lex, *parts, **k): return W(full, lex, "prep", *parts, **k)
def pro(full, lex, *parts, **k): return W(full, lex, "pron", *parts, **k)

# ---- the clitics, as (form, key, pos) ----
WA, FA = ("وَ", "wa", "conj"), ("فَ", "fa", "conj")
BI, LI, KA = ("بِ", "bi", "prep"), ("لِ", "li", "prep"), ("كَ", "ka", "prep")
_PK = {"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp", "كَ": "pron-2ms", "كِ": "pron-2fs",
       "نِي": "pron-1s", "ي": "pron-1s", "يَ": "pron-1s", "نَا": "pron-1p", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هُنَّ": "pron-3fp", "هِنَّ": "pron-3fp",
       "كُمْ": "pron-2mp", "كُمُ": "pron-2mp"}
def P(form): return (form, _PK[form], "pron")
_PRN = {"هُ": ("الْهَاءُ", "the هُ", "«hû»"), "هِ": ("الْهَاءُ", "the هِ", "«hî»"), "هَا": ("هَا", "هَا", "هَا"), "ي": ("الْيَاءُ", "the ya", "yâ"), "يَ": ("الْيَاءُ", "the ya", "yâ"),
        "كَ": ("الْكَافُ", "the kaf", "kâf"), "كِ": ("الْكَافُ", "the kaf", "kâf"), "هُمَا": ("هُمَا", "هُمَا", "هُمَا"), "هِمَا": ("هِمَا", "هِمَا", "هِمَا"), "نَا": ("نَا", "نَا", "نَا"),
        "هُمْ": ("هُمْ", "هُمْ", "هُمْ"), "هِمْ": ("هِمْ", "هِمْ", "هِمْ"), "هُمُ": ("هُمْ", "هُمْ", "هُمْ"), "هُنَّ": ("هُنَّ", "هُنَّ", "هُنَّ"), "هِنَّ": ("هِنَّ", "هِنَّ", "هِنَّ"),
        "كُمْ": ("كُمْ", "كُمْ", "كُمْ"), "كُمُ": ("كُمْ", "كُمْ", "كُمْ"), "نِي": ("الْيَاءُ", "the ya", "yâ")}

# ---- case and its sign ----
SGN = {
 "r": ("مَرْفُوعٌ بِالضَّمَّةِ", "in raf' by the damma", "damme ile merfû"),
 "n": ("مَنْصُوبٌ بِالْفَتْحَةِ", "in nasb by the fatha", "fetha ile mansûb"),
 "j": ("مَجْرُورٌ بِالْكَسْرَةِ", "in jarr by the kasra", "kesre ile mecrûr"),
 "jf": ("مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", "in jarr by the fatha in place of the kasra, being a diptote", "gayr-i munsarif olduğu için kesre yerine fetha ile mecrûr"),
 "rA": ("مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "in raf' by a damma estimated on the alif", "elif üzerinde takdîrî damme ile merfû"),
 "nA": ("مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "in nasb by a fatha estimated on the alif", "elif üzerinde takdîrî fetha ile mansûb"),
 "jA": ("مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "in jarr by a kasra estimated on the alif", "elif üzerinde takdîrî kesre ile mecrûr"),
 "rY": ("مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "in raf' by a damma estimated on the ya", "yâ üzerinde takdîrî damme ile merfû"),
 "jY": ("مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "in jarr by a kasra estimated on the ya", "yâ üzerinde takdîrî kesre ile mecrûr"),
 "rM": ("مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ", "in raf' by a damma estimated before the speaker's ya, whose kasra holds the place", "mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû"),
 "nM": ("مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ", "in nasb by a fatha estimated before the speaker's ya, whose kasra holds the place", "mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb"),
 "jM": ("مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ", "in jarr by a kasra estimated before the speaker's ya, whose own kasra holds the place", "mütekellim yâsından önceki harf üzerinde takdîrî kesre ile mecrûr"),
 "rD": ("مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى", "in raf' by the alif, being a dual", "tesniye olduğu için elif ile merfû"),
 "nD": ("مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى", "in nasb by the ya, being a dual", "tesniye olduğu için yâ ile mansûb"),
 "jD": ("مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى", "in jarr by the ya, being a dual", "tesniye olduğu için yâ ile mecrûr"),
 "rW": ("مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", "in raf' by the waw, being a sound masculine plural", "cem-i müzekker sâlim olduğu için vâv ile merfû"),
 "nP": ("مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", "in nasb by the ya, being a sound masculine plural", "cem-i müzekker sâlim olduğu için yâ ile mansûb"),
 "jP": ("مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", "in jarr by the ya, being a sound masculine plural", "cem-i müzekker sâlim olduğu için yâ ile mecrûr"),
 "nK": ("مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ", "in nasb by the kasra in place of the fatha, being a sound feminine plural", "cem-i müennes sâlim olduğu için fetha yerine kesre ile mansûb"),
 "r5": ("مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "in raf' by the waw, being one of the five nouns", "esmâ-i hamseden olduğu için vâv ile merfû"),
 "n5": ("مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "in nasb by the alif, being one of the five nouns", "esmâ-i hamseden olduğu için elif ile mansûb"),
 "j5": ("مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "in jarr by the ya, being one of the five nouns", "esmâ-i hamseden olduğu için yâ ile mecrûr"),
}
_SG_TAGS = {"jf": ["mamnu-min-sarf"], "rA": ["ism-maqsur-manqus"], "nA": ["ism-maqsur-manqus"], "jA": ["ism-maqsur-manqus"], "rY": ["ism-maqsur-manqus"], "jY": ["ism-maqsur-manqus"],
            "rM": ["ya-al-mutakallim"], "nM": ["ya-al-mutakallim"], "jM": ["ya-al-mutakallim"], "rD": ["al-muthanna"], "nD": ["al-muthanna"], "jD": ["al-muthanna"],
            "rW": ["jam-mudhakkar-salim"], "nP": ["jam-mudhakkar-salim"], "jP": ["jam-mudhakkar-salim"], "nK": ["jam-muannath-salim"], "r5": ["five-nouns"], "n5": ["five-nouns"], "j5": ["five-nouns"]}
def RO(ar, en, tr, s, *tags):
    """a role and its case: «فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ»"""
    a, e, t = SGN[s]
    return Fr(ar + " " + a, en + ", " + e, tr + ", " + t, *(list(tags) + _SG_TAGS.get(s, [])))
def FL(s="r"): return RO("فَاعِلٌ", "the doer (fa'il)", "fâil", s, "fail")
def NF(s="r"): return RO("نَائِبُ فَاعِلٍ", "the deputy doer", "nâib-i fâil", s, "naib-al-fail")
def MF(s="n"): return RO("مَفْعُولٌ بِهِ", "the direct object", "mef'ûlün bih", s, "maful-bihi")
def MF1(s="n"): return RO("مَفْعُولٌ بِهِ أَوَّلُ", "the first object", "birinci mef'ûlün bih", s, "maful-bihi", "mafulayn")
def MF2(s="n"): return RO("مَفْعُولٌ بِهِ ثَانٍ", "the second object", "ikinci mef'ûlün bih", s, "maful-bihi", "mafulayn")
def MI(s="j"): return RO("مُضَافٌ إِلَيْهِ", "the second term of the idafa", "muzâfun ileyh", s, "idafa-definiteness")
def MJ(s="j"):
    a, e, t = SGN[s]
    return Fr("اسْمٌ " + a, "a noun " + e + " after the jarr letter", "cer harfinden sonra " + t + " isim", "huruf-jarr", *_SG_TAGS.get(s, []))
def MB(s="r"): return RO("مُبْتَدَأٌ", "the mubtada", "mübtedâ", s, "mubtada-khabar")
def KH(s="r"): return RO("خَبَرٌ", "the khabar (predicate)", "haber", s, "mubtada-khabar")
def HL(s="n"): return RO("حَالٌ", "a hal (circumstantial accusative)", "hâl", s, "hal")
def TZ(s="n"): return RO("تَمْيِيزٌ", "a tamyiz (specifier)", "temyîz", s, "tamyiz", "al-tamyiz-wa-ahkamuh")
def MM(s="n"): return RO("مَفْعُولٌ مُطْلَقٌ", "an absolute object (maf'ul mutlaq)", "mef'ûl-i mutlak", s, "maful-mutlaq")
def ML(s="n"): return RO("مَفْعُولٌ لِأَجْلِهِ", "an object of cause (maf'ul li-ajlih)", "mef'ûlün lieclih", s, "maful-lah")
def ZZ(s="n"): return RO("ظَرْفُ زَمَانٍ", "an adverb of time", "zaman zarfı", s, "maful-fih")
def ZM(s="n"): return RO("ظَرْفُ مَكَانٍ", "an adverb of place", "mekân zarfı", s, "maful-fih")
def NAT(of, s="j", nth=""):
    a, e, t = SGN[s]
    return Fr("نَعْتٌ %sلِـ«%s» %s" % (nth and nth + " ", of, a), "a%s adjective (na't) of «%s», %s" % ({"": "n", "ثَانٍ": " second", "ثَالِثٌ": " third", "آخَرُ": " further"}[nth], of, e),
              "«%s» kelimesinin %sna'tı, %s" % (of, {"": "", "ثَانٍ": "ikinci ", "ثَالِثٌ": "üçüncü ", "آخَرُ": "bir başka "}[nth], t), "naat-sifa", *_SG_TAGS.get(s, []))
def ATF(of, s="j"):
    a, e, t = SGN[s]
    return Fr("مَعْطُوفٌ عَلَى «%s» %s" % (of, a), "conjoined to «%s», %s" % (of, e), "«%s» kelimesine ma'tûf, %s" % (of, t), "atf-nasaq", *_SG_TAGS.get(s, []))
def BDL(of, s="j"):
    a, e, t = SGN[s]
    return Fr("بَدَلٌ مِنْ «%s» %s" % (of, a), "a badal (substitute) of «%s», %s" % (of, e), "«%s» kelimesinden bedel, %s" % (of, t), "badal", *_SG_TAGS.get(s, []))
MDF = Fr("، مُضَافٌ", ", annexed", ", muzâf", "idafa-definiteness")
def IDF(pr):
    """…, annexed, and the attached pronoun is its second term"""
    a, e, t = _PRN[pr]
    return Fr("، مُضَافٌ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" % a, ", annexed; %s is its second term, in the seat of jarr" % e, ", muzâf; %s muzâfun ileyh, mahallen mecrûr" % t,
              "idafa-definiteness", "al-bariz-al-muttasil")

# ---- the verb ----
MADI = Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "a past verb built on fatha", "fetha üzere mebnî mâzî")
MADI_F = Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "a past verb built on fatha; the ta marks the feminine", "fetha üzere mebnî mâzî; tâ te'nîs içindir")
MADI_A = Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "a past verb built on a fatha estimated on the alif", "elif üzerinde takdîrî fetha ile mebnî mâzî", "naqis-verbs")
MAJH = Fr(" مَبْنِيٌّ لِلْمَجْهُولِ", " in the passive", " (meçhul)", "al-majhul-fil-kafiya")
def TU(who):
    """the past verb with the doer's ta: ana | anta | anti"""
    a, e, t = {"ana": ("تَاءُ الْمُتَكَلِّمِ", "I", "ben"), "anta": ("تَاءُ الْمُخَاطَبِ", "you", "sen"), "anti": ("تَاءُ الْمُخَاطَبَةِ", "you, a woman", "sen (müennes)")}[who]
    return Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" % a,
              "a past verb built on sukun because the doer's ta is attached; the ta («%s») is the doer, in the seat of raf'" % e,
              "fâil tâsı bitiştiği için sükûn üzere mebnî mâzî; tâ («%s») fâildir, mahallen merfû" % t, "al-bariz-al-muttasil", "fail")
def TU_M(who):
    """the PASSIVE past verb with the ta as deputy doer"""
    a, e, t = {"ana": ("تَاءُ الْمُتَكَلِّمِ", "I", "ben"), "anta": ("تَاءُ الْمُخَاطَبِ", "you", "sen"), "anti": ("تَاءُ الْمُخَاطَبَةِ", "you, a woman", "sen (müennes)")}[who]
    return Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِالتَّاءِ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ" % a,
              "a past verb in the passive, built on sukun because the ta is attached; the ta («%s») is the deputy doer, in the seat of raf'" % e,
              "meçhul mâzî, tâ bitiştiği için sükûn üzere mebnî; tâ («%s») nâib-i fâildir, mahallen merfû" % t, "al-bariz-al-muttasil", "naib-al-fail", "al-majhul-fil-kafiya")
def MUDR(est=None):
    return {None: Fr("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ", "a present verb in raf' by the damma", "damme ile merfû muzâri", "mudari-marfu"),
            "y": Fr("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "a present verb in raf' by a damma estimated on the ya", "yâ üzerinde takdîrî damme ile merfû muzâri", "mudari-marfu", "naqis-verbs"),
            "w": Fr("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ", "a present verb in raf' by a damma estimated on the waw", "vâv üzerinde takdîrî damme ile merfû muzâri", "mudari-marfu", "naqis-verbs"),
            "a": Fr("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "a present verb in raf' by a damma estimated on the alif", "elif üzerinde takdîrî damme ile merfû muzâri", "mudari-marfu", "naqis-verbs")}[est]
MUDR5 = Fr("فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a present verb, one of the five verbs, in raf' by the kept nun; the waw is its doer, in the seat of raf'",
           "ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâildir, mahallen merfû", "afal-khamsa", "mudari-marfu", "al-bariz-al-muttasil")
NISWA = Fr("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a present verb built on sukun because the nun of the women is attached; that nun is the doer, in the seat of raf'",
           "nûn-ı nisve bitiştiği için sükûn üzere mebnî muzâri; nûn fâildir, mahallen merfû", "al-bariz-al-muttasil", "fail")
_WHO = {"أَنَا": ("I", "ben"), "أَنْتَ": ("you", "sen"), "أَنْتِ": ("you", "sen"), "هُوَ": ("he / it", "o"), "هِيَ": ("she / it", "o"), "نَحْنُ": ("we", "biz")}
def HID(who, ref=None, naib=False):
    """the hidden doer (or deputy doer); ref = (ar, en, tr) of what it returns to"""
    e, t = _WHO[who]
    wj = who in ("أَنَا", "أَنْتَ", "نَحْنُ")
    role = ("نَائِبُ الْفَاعِلِ", "its deputy doer", "nâib-i fâili") if naib else ("الْفَاعِلُ", "its doer", "fâili")
    ar = "، وَ%s ضَمِيرٌ مُسْتَتِرٌ %sتَقْدِيرُهُ: %s" % (role[0], "وُجُوبًا " if wj else "", who)
    en = "; %s is the hidden «%s»" % (role[1], e); tr = "; %s %sgizli zamir «%s»" % (role[2], "vücûben " if wj else "", t)
    if ref: ar += " يَعُودُ عَلَى " + ref[0]; en += " — " + ref[1]; tr += " — " + ref[2]
    return Fr(ar, en, tr, *(["al-fail-al-mudmar-al-mustatir-wujuban"] if wj else []))
def OBJ(pr, role=("مَفْعُولٌ بِهِ", "its object", "mef'ûlün bih")):
    a, e, t = _PRN[pr]
    return Fr("، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ %s" % (a, role[0]), "; %s is %s, in the seat of nasb" % (e, role[1]), "; %s %s, mahallen mansûb" % (t, role[2]), "al-bariz-al-muttasil", "maful-bihi")
FAIL_BAD = Fr("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")

# ---- the conjunction fused to the word ----
def PRE(kind, word):
    a, e, t = {"wa": ("الْوَاوُ عَاطِفَةٌ، وَ", "the waw conjoins; ", "vâv atıf harfi; "), "fa": ("الْفَاءُ عَاطِفَةٌ، وَ", "the fa conjoins; ", "fâ atıf harfi; "),
               "wa-ist": ("الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "the waw opens a new sentence; ", "vâv isti'nâfiyye; "), "fa-ist": ("الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ", "the fa opens a new sentence; ", "fâ isti'nâfiyye; "),
               "wa-hal": ("الْوَاوُ حَالِيَّةٌ، وَ", "the waw is the waw of the hal; ", "vâv hâliyye; "),
               "fa-jaza": ("الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَ", "the fa ties the answer to its condition; ", "fâ şartın cevabını bağlar; "),
               "wa-rubba": ("الْوَاوُ وَاوُ رُبَّ، وَ", "the waw is the waw of رُبَّ («many a …»); ", "vâv, «رُبَّ» vâvıdır («nice …»); ")}[kind]
    return Fr(a + word + " ", e + word + " is ", t + word + " ", *({"wa": ["atf-nasaq"], "fa": ["atf-nasaq"], "wa-hal": ["al-hal-jumla-wa-rabituha", "anwa-al-waw"], "wa-ist": ["anwa-al-waw"],
                                                               "fa-jaza": ["al-fa-fi-jawab-al-shart"], "wa-rubba": ["al-lam-wa-rubba-fil-kafiya", "anwa-al-waw"]}.get(kind, [])))
_HARF = {"بِ": ("الْبَاءُ", "the ba", "bâ"), "لِ": ("اللَّامُ", "the lam", "lâm"), "كَ": ("الْكَافُ", "the kaf", "kâf")}
def JN(h, word, s="j", sense=None):
    """a jarr letter written onto its noun: «الْبَاءُ حَرْفُ جَرٍّ، وَالْجِوَاءِ اسْمٌ مَجْرُورٌ بِالْكَسْرَةِ»; sense = (ar, en, tr) of the letter's meaning"""
    a, e, t = _HARF[h]; sa, se, st = SGN[s]
    k = (" وَتَشْبِيهٍ", " of likening", " (teşbîh bildirir)") if h == "كَ" else ("", "", "")
    m = (" " + sense[0], " " + sense[1], " " + sense[2]) if sense else ("", "", "")
    return Fr("%s حَرْفُ جَرٍّ%s%s، وَ«%s» اسْمٌ %s" % (a, k[0], m[0], word, sa), "%s is a jarr letter%s%s; «%s» is %s" % (e, k[1], m[1], word, se), "%s cer harfi%s%s; «%s» %s" % (t, k[2], m[2], word, st),
              "huruf-jarr", *_SG_TAGS.get(s, []))
FI_SENSE = ("بِمَعْنَى «فِي»", "meaning «in»", "«-de» anlamında")
def JP(prep, pr, name=None):
    """a jarr letter fused to its pronoun: «فِي حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ»"""
    a, e, t = _PRN[pr]; nm = name or (prep, prep, prep)
    return Fr("%s حَرْفُ جَرٍّ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ" % (nm[0], a), "%s is a jarr letter and %s is in the seat of jarr" % (nm[1], e), "%s cer harfi, %s mahallen mecrûr" % (nm[2], t), "huruf-jarr", "al-bariz-al-muttasil")
HJ = Fr("حَرْفُ جَرٍّ", "a jarr letter", "cer harfi", "huruf-jarr")
def TA(word):
    """the jarr phrase hangs on «word»"""
    return Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«%s»" % word, "; the jarr phrase hangs on «%s»" % word, "; câr-mecrûr «%s» kelimesine müteallik" % word)
def TAM(kind, word=None, nth=""):
    """… hangs on an omitted na't / hal / khabar"""
    k = {"naat": ("نَعْتٍ %sلِـ" % (nth and nth + " "), "an omitted %sna't of " % ({"": "", "ثَانٍ": "second ", "ثَالِثٍ": "third "}[nth]), "mahzûf %sna'tına" % ({"": "", "ثَانٍ": "ikinci ", "ثَالِثٍ": "üçüncü "}[nth])),
         "hal": ("حَالٍ مِنْ ", "an omitted hal of ", "mahzûf hâline"), "khabar": ("خَبَرٍ", "the omitted khabar", "mahzûf habere"),
         "khabar-m": ("خَبَرٍ مُقَدَّمٍ", "the omitted, fronted khabar", "öne alınmış mahzûf habere")}[kind]
    if word is None: return Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ " + k[0], "; the jarr phrase hangs on " + k[1], "; câr-mecrûr " + k[2] + " müteallik")
    return Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ %s«%s»" % (k[0], word), "; the jarr phrase hangs on %s«%s»" % (k[1], word), "; câr-mecrûr «%s» kelimesinin %s müteallik" % (word, k[2]))
def ZT(word):
    """the adverb hangs on «word»"""
    return Fr("، مُتَعَلِّقٌ بِـ«%s»" % word, ", hanging on «%s»" % word, "; «%s» kelimesine müteallik" % word)

# ---- a clause and its seat ----
_MH = {"r": ("فِي مَحَلِّ رَفْعٍ ", ", in the seat of raf'", ", mahallen merfû"), "n": ("فِي مَحَلِّ نَصْبٍ ", ", in the seat of nasb", ", mahallen mansûb"), "j": ("فِي مَحَلِّ جَرٍّ ", ", in the seat of jarr", ", mahallen mecrûr"),
       "z": ("فِي مَحَلِّ جَزْمٍ ", ", in the seat of jazm", ", mahallen meczûm")}
def CL(m, ar, en, tr, *tags):
    """«وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ» — m = r | n | j | z, or 0 for a clause with no seat"""
    if m == 0: return Fr(" — وَالْجُمْلَةُ %s لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ" % ar, "; the clause %s and has no seat of its own" % en, "; cümle %s, i'râbdan mahalli yoktur" % tr, *tags)
    a, e, t = _MH[m]
    return Fr(" — وَالْجُمْلَةُ %s%s" % (a, ar), "; the clause is %s%s" % (en, e), "; cümle %s%s" % (tr, t), *tags)
CL_KH = CL("r", "خَبَرُ الْمُبْتَدَأِ", "the khabar of the mubtada", "mübtedânın haberi", "anwa-al-khabar")
CL_SILA = CL(0, "صِلَةُ الْمَوْصُولِ", "is the relative's sila", "sıla cümlesidir")
CL_IST = CL(0, "اسْتِئْنَافِيَّةٌ", "opens a new sentence", "isti'nâfiyyedir")
CL_JAWAB = CL(0, "جَوَابُ الشَّرْطِ غَيْرِ الْجَازِمِ", "answers a condition that does not put in jazm", "câzim olmayan şartın cevabıdır")
def CL_NAAT(of, m="j"): return CL(m, "نَعْتٌ لِـ«%s»" % of, "a na't of «%s»" % of, "«%s» kelimesinin na'tı" % of, "jumla-sifa")
def CL_HAL(of): return CL("n", "حَالٌ مِنْ «%s»" % of, "a hal of «%s»" % of, "«%s» kelimesinden hâl" % of, "al-hal-jumla-wa-rabituha")
def CL_MI(of): return CL("j", "بِإِضَافَةِ «%s» إِلَيْهَا" % of, "annexed to «%s»" % of, "«%s» kelimesinin muzâfun ileyhi" % of)

# ---- notes ----
def Dn(ar, en, tr, *tags): return Fr(" — " + ar, " — " + en, " — " + tr, *tags)            # a note after the dash
def Sn(ar, en, tr, *tags): return Fr(". " + ar, ". " + _cap(en), ". " + _cap(tr, True), *tags)   # a new sentence in the line: the balāgha
def HD(ar, en, tr, *tags):
    """a figure no commentator names, that meets the Talkhīṣ's own definition — the line says so"""
    return Fr(". وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — " + ar, ". By the Talkhīṣ's definition, " + en, ". Telhîs'in tarifine göre " + tr, *tags)
# the rhyme: the rawī is a mīm with kasra and the qāfiya is muṭlaqa
QT = Fr("، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ وَأُشْبِعَتْ كَسْرَةُ الرَّوِيِّ", "; at the rhyme its tanwin is dropped and the kasra of the rawī is lengthened", "; kâfiyede tenvini düşer, revînin kesresi uzatılır", "al-qafiya")
QA = Fr("، وَأُشْبِعَتْ كَسْرَةُ الرَّوِيِّ لِلْإِطْلَاقِ", "; the kasra of the rawī is lengthened, the rhyme being unbound", "; kâfiye mutlak olduğu için revînin kesresi uzatılır", "al-qafiya")
RAWI_J = ("السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِلرَّوِيِّ — وَهِيَ حَرَكَةُ الْقَافِيَةِ الْمُطْلَقَةِ، تُشْبَعُ فِي الْإِنْشَادِ", "the sukun — which gives way to the kasra of the rhyme (the ḥarakat al-rawī: the qāfiya is unbound, and the kasra is lengthened in recitation)",
          "sükûn — yerini revî harekesi olan kesreye bırakmıştır (kâfiye mutlaktır; kesre inşâdda uzatılır)")

VERSE = {}                   # al-Zawzanī's verse number -> its sentence (ids are given when the chapters are cut)
S1 = []                      # the khabar's sentences, in order
def K(en, tr, tokens):
    """one sentence of the khabar"""
    S1.append({"id": "s%d" % (len(S1) + 1), "translation": {"en": en, "tr": tr}, "tokens": tokens})
def V(num, en, tr, first, second):
    """one verse = one sentence: «•» closes the first hemistich, a full stop the verse"""
    assert num not in VERSE, num
    first[-1]["punctAfter"] = "•"
    second[-1].setdefault("punctAfter", ".")
    VERSE[num] = {"translation": {"en": en, "tr": tr}, "tokens": first + second}

# =====================================================================================================================
# Chapter 1 — خَبَرُ عَنْتَرَةَ (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/244–245, § 419 — verbatim, contiguous, whole)
# =====================================================================================================================
KANA = Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ", "the defective past verb, built on fatha: it raises its noun and puts its predicate in nasb", "fetha üzere mebnî nâkıs mâzî: ismini ref, haberini nasb eder", "kana-wa-akhawatuha", "hollow-verbs")
ANTARA_DIPT = Dn("عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", "a proper name with the feminine ta, barred from tanwin", "lafzî te'nîsli özel isim, gayr-i munsarif", "mamnu-min-sarf")
LA_NAF = Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi", "la-nafiya")
MA_NAF = Fr("مَا حَرْفُ نَفْيٍ", "مَا is a particle of negation", "مَا nefy harfi")
INNA_ = Fr("حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ", "the particle of emphasis that puts its noun in nasb and raises its predicate", "te'kîd ve nasb harfi: ismini nasb, haberini ref eder", "inna-wa-akhawatuha")
ISM_INNA = RO("اسْمُ إِنَّ", "the noun of إِنَّ", "إِنَّ'nin ismi", "n", "inna-wa-akhawatuha")
LAM_MUZ = Fr("اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَ", "the lam is the displaced lam of emphasis; ", "lâm, te'kîd bildiren lâm-ı müzahlakadır; ")
CL_KH_INNA = CL("r", "خَبَرُ إِنَّ", "the predicate of إِنَّ", "إِنَّ'nin haberi", "inna-wa-akhawatuha")
QATTU = Fr("ظَرْفُ زَمَانٍ لِاسْتِغْرَاقِ الْمَاضِي مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ", "an adverb of time that sweeps the whole past («ever»), built on damma, in the seat of nasb", "geçmişin tamamını kuşatan zaman zarfı («hiç»), damme üzere mebnî, mahallen mansûb", "maful-fih", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya")
WA_LA = lambda: pt("وَلَا", "la-nafiya", Fr("الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ", "the waw conjoins; لَا is added to strengthen the negation", "vâv atıf harfi; لَا nefyi pekiştirmek için zâiddir", "atf-nasaq", "huruf-al-ziyada-fil-kafiya"), s=[WA, ("لَا", "la-nafiya", "part")])
def FA_MA(): return pt("فَمَا", "ma-nafiya", PRE("fa", "مَا"), Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi"), s=[FA, ("مَا", "ma-nafiya", "part")])
def HADARTA(): return v("حَضَرْتَ", "hadara", TU("anta"), g=["thulathi-mujarrad-babs"])
def ANTA_TAWKID(): return pro("أَنْتَ", "anta", Fr("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلتَّاءِ فِي «حَضَرْتَ»، وَهُوَ الَّذِي سَوَّغَ الْعَطْفَ عَلَى ضَمِيرِ الرَّفْعِ الْمُتَّصِلِ",
    "a detached pronoun built on fatha, in the seat of raf': it repeats the ta of «حَضَرْتَ» for emphasis, and so lets a noun be conjoined to that attached pronoun", "fetha üzere mebnî munfasıl zamir, mahallen merfû: «حَضَرْتَ»deki tâ'nın te'kîdidir; bitişik ref zamirine atfı mümkün kılan da odur", "tawkid", "al-tawkid-al-lafzi-wal-manawi", "al-atf-bil-huruf-wa-ahkamuh"))
def ABUKA(p=None): return n("أَبُوكَ", "ab", Fr("مَعْطُوفٌ عَلَى التَّاءِ فِي «حَضَرْتَ» مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "conjoined to the ta of «حَضَرْتَ», in raf' by the waw, being one of the five nouns", "«حَضَرْتَ»deki tâ'ya ma'tûf, esmâ-i hamseden olduğu için vâv ile merfû", "atf-nasaq", "five-nouns"), IDF("كَ"), p=p, s=[("أَبُو", "ab", "noun"), P("كَ")])
def JADDUKA(p=None): return n("جَدُّكَ", "jadd", ATF("أَبُوكَ", "r"), IDF("كَ"), p=p, s=[("جَدُّ", "jadd", "noun"), P("كَ")])
def WA_INNA(): return pt("وَإِنَّ", "inna", PRE("wa", "إِنَّ"), INNA_, Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جَوَابِ الْقَسَمِ", "the clause is conjoined to the answer of the oath", "cümle kasemin cevabına ma'tûftur"), s=[WA, ("إِنَّ", "inna", "part")])
def NAS(role, p=None): return n({"n": "النَّاسَ", "j": "النَّاسِ"}[role], "nas", ISM_INNA if role == "n" else MI(), p=p)
def BIMA(): return pro("بِمَا", "ma-mawsula", Fr("الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ", "the ba is a jarr letter; مَا is a relative noun built on sukun, in the seat of jarr", "bâ cer harfi; مَا sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr", "huruf-jarr", "ism-mawsul"), s=[BI, ("مَا", "ma-mawsula", "pron")])
def MALAKAT(): return v("مَلَكَتْ", "malaka", MADI_F, FAIL_BAD, CL_SILA, Dn("وَالْعَائِدُ مَحْذُوفٌ، أَيْ: مَلَكَتْهُ", "the pronoun that returns to مَا is dropped: «what [it] owned»", "mevsûle dönen zamir hazfedilmiştir: «sahip olduğu [şey]»", "hadhf-al-maful"), g=["thulathi-mujarrad-babs"])

K("ʿAntara was among the hardiest men of his time and the most open-handed of them with whatever his hand owned.",
  "Antere, zamanındaki insanların en çetinlerinden ve elinin sahip olduğu şeyde en cömertlerindendi.", [
 v("وَكَانَ", "kana", PRE("wa-ist", "كَانَ"), KANA, s=[WA, ("كَانَ", "kana", "verb")]),
 pn("عَنْتَرَةُ", "antara", RO("اسْمُ كَانَ", "the noun of كَانَ", "كَانَ'nin ismi", "r", "kana-wa-akhawatuha"), ANTARA_DIPT),
 pp("مِنْ", "min", HJ, Dn("لِلتَّبْعِيضِ", "of «some of»", "teb'îz bildirir")),
 n("أَشَدِّ", "ashadd", MJ(), MDF, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ؛ وَأَشَدُّ اسْمُ تَفْضِيلٍ", "the jarr phrase hangs on the omitted predicate of كَانَ; أَشَدّ is an elative", "câr-mecrûr كَانَ'nin mahzûf haberine müteallik; أَشَدّ ism-i tafdîldir", "kana-wa-akhawatuha", "ism-tafdil")),
 n("أَهْلِ", "ahl", MI(), MDF),
 n("زَمَانِهِ", "zaman", MI(), IDF("هِ"), s=[("زَمَانِ", "zaman", "noun"), P("هِ")]),
 n("وَأَجْوَدِهِمْ", "ajwad-ant", PRE("wa", "أَجْوَدِ"), ATF("أَشَدِّ"), IDF("هِمْ"), Dn("اسْمُ تَفْضِيلٍ مِنَ الْجُودِ", "an elative of «generosity»", "«cömertlik»ten ism-i tafdîl", "ism-tafdil"), s=[WA, ("أَجْوَدِ", "ajwad-ant", "noun"), P("هِمْ")]),
 BIMA(), MALAKAT(),
 n("يَدُهُ", "yad", FL(), IDF("هُ"), Dn("وَالْجَارُّ وَالْمَجْرُورُ «بِمَا» مُتَعَلِّقَانِ بِـ«أَجْوَدِ»", "the phrase «بِمَا» hangs on «أَجْوَدِ»", "«بِمَا» câr-mecrûru «أَجْوَدِ» kelimesine müteallik"), p=".", s=[("يَدُ", "yad", "noun"), P("هُ")]),
])
K("He used to say no more poetry than two verses or three, until a man of the Banū ʿAbs traded insults with him,",
  "Şiirden yalnızca iki üç beyit söylerdi; nihayet Abs oğullarından bir adam onunla sövüştü,", [
 v("وَكَانَ", "kana", PRE("wa", "كَانَ"), KANA, Dn("وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى عَنْتَرَةَ", "its noun is the hidden «he» — ʿAntara", "ismi Antere'ye dönen gizli zamir «o»"), s=[WA, ("كَانَ", "kana", "verb")]),
 pt("لَا", "la-nafiya", LA_NAF),
 v("يَقُولُ", "qala", MUDR(), HID("هُوَ"), CL("n", "خَبَرُ كَانَ", "the predicate of كَانَ", "كَانَ'nin haberi", "kana-wa-akhawatuha"), g=["hollow-verbs"]),
 pp("مِنَ", "min", HJ, Dn("وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ", "voweled with fatha before the following ال", "iki sâkin karşılaştığı için fetha ile harekelendi")),
 n("الشِّعْرِ", "shir", MJ(), TAM("hal", "الْبَيْتَيْنِ"), Dn("كَانَ نَعْتًا لَهُ فَلَمَّا تَقَدَّمَ عَلَيْهِ صَارَ حَالًا", "it would have been its na't, but placed before it it becomes a hal", "onun na'tı iken öne geçince hâl olmuştur")),
 pt("إِلَّا", "illa", Fr("أَدَاةُ حَصْرٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ", "the particle of restriction; the exception is «emptied» (mufarragh)", "hasr edatı; istisnâ müferrağdır", "istithna-mufarragh", "istithna"),
    HD("قَصْرٌ بِالنَّفْيِ وَالِاسْتِثْنَاءِ: قَصَرَ قَوْلَهُ الشِّعْرَ عَلَى الْبَيْتَيْنِ وَالثَّلَاثَةِ", "this is a restriction (qaṣr) by negation and exception: his verse-making is confined to two verses or three", "bu, nefy ve istisnâ ile yapılmış bir kasrdır: şiir söylemesi iki üç beyte hasredilmiştir", "qasr", "turuq-al-qasr")),
 n("الْبَيْتَيْنِ", "bayt", MF("nD")),
 n("وَالثَّلَاثَةَ", "thalatha", PRE("wa", "الثَّلَاثَةَ"), ATF("الْبَيْتَيْنِ", "n"), Dn("وَالْوَاوُ بِمَعْنَى «أَوْ»", "the waw has the sense of «or»", "vâv «veya» anlamındadır"), p="،", s=[WA, ("الثَّلَاثَةَ", "thalatha", "noun")]),
 pt("حَتَّى", "hatta", Fr("حَرْفُ غَايَةٍ وَابْتِدَاءٍ، وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ", "a particle of limit that opens a new clause", "gâye ve ibtidâ harfi; sonraki cümle müste'nefedir", "ila-hatta-fi-wal-ba-fil-kafiya")),
 v("سَابَّهُ", "saabba-ant", MADI, OBJ("هُ", ("مَفْعُولٌ بِهِ مُقَدَّمٌ", "its object, placed before the doer", "öne geçmiş mef'ûlün bih")), Dn("مِنَ الْمُفَاعَلَةِ: شَاتَمَهُ", "Form III: «traded insults with him»", "müfâale bâbından: «onunla sövüştü»", "form-iii-verbs", "doubled-verbs"), s=[("سَابَّ", "saabba-ant", "verb"), P("هُ")]),
 n("رَجُلٌ", "rajul", FL()),
 pp("مِنْ", "min", HJ),
 n("بَنِي", "ibn", Fr("اسْمٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", "a noun in jarr by the ya — it is declined like the sound masculine plural — its nun dropped for the idafa; annexed", "cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr isim; nûnu izâfetten dolayı düşmüştür; muzâf", "huruf-jarr", "jam-mudhakkar-salim", "idafa-definiteness"), TAM("naat", "رَجُلٌ")),
 pn("عَبْسٍ", "abs", MI(), p="،"),
])
K("and he spoke of his blackness and the blackness of his mother and his brothers, and taunted him with that, and with his not composing poetry.",
  "onun siyahlığını, annesinin ve kardeşlerinin siyahlığını andı; onu bununla ve şiir söylememesiyle ayıpladı.", [
 v("فَذَكَرَ", "dhakara", PRE("fa", "ذَكَرَ"), MADI, HID("هُوَ", ("الرَّجُلِ", "the man", "o adam")), s=[FA, ("ذَكَرَ", "dhakara", "verb")], g=["thulathi-mujarrad-babs"]),
 n("سَوَادَهُ", "sawad", MF(), IDF("هُ"), s=[("سَوَادَ", "sawad", "noun"), P("هُ")]),
 n("وَسَوَادَ", "sawad", PRE("wa", "سَوَادَ"), ATF("سَوَادَهُ", "n"), MDF, s=[WA, ("سَوَادَ", "sawad", "noun")]),
 n("أُمِّهِ", "umm", MI(), IDF("هِ"), s=[("أُمِّ", "umm", "noun"), P("هِ")]),
 n("وَإِخْوَتِهِ", "akh", PRE("wa", "إِخْوَتِ"), ATF("أُمِّ"), IDF("هِ"), Dn("جَمْعُ أَخٍ", "the plural of أَخ", "أَخ'ın cem'i", "jam-taksir"), p="،", s=[WA, ("إِخْوَتِ", "akh", "noun"), P("هِ")]),
 v("وَعَيَّرَهُ", "ayyara", PRE("wa", "عَيَّرَ"), MADI, HID("هُوَ"), OBJ("هُ"), s=[WA, ("عَيَّرَ", "ayyara", "verb"), P("هُ")], g=["form-ii-verbs"]),
 pro("بِذٰلِكَ", "dhalika", Fr("الْبَاءُ حَرْفُ جَرٍّ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ لِلْبُعْدِ وَالْكَافُ لِلْخِطَابِ", "the ba is a jarr letter; ذَا is a demonstrative built on sukun, in the seat of jarr; the lam marks distance and the kaf address", "bâ cer harfi; ذَا sükûn üzere mebnî ism-i işâret, mahallen mecrûr; lâm uzaklık, kâf hitap içindir", "huruf-jarr", "asma-al-ishara"), TA("عَيَّرَ"), p="،", s=[BI, ("ذٰلِكَ", "dhalika", "pron")]),
 pt("وَبِأَنَّهُ", "anna", Fr("الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنَّ وَمَعْمُولَيْهَا فِي مَحَلِّ جَرٍّ بِالْبَاءِ، مَعْطُوفٌ عَلَى «بِذٰلِكَ»",
    "the waw conjoins and the ba is a jarr letter; أَنَّ puts its noun in nasb, and the attached هُ is that noun — the masdar the clause makes is in the seat of jarr by the ba, conjoined to «بِذٰلِكَ»", "vâv atıf harfi, bâ cer harfi; أَنَّ te'kîd ve nasb harfi, bitişik «hû» ismidir, mahallen mansûb — أَنَّ ile iki ma'mûlünün müevvel masdarı bâ ile mahallen mecrûr, «بِذٰلِكَ»ye ma'tûf", "atf-nasaq", "huruf-jarr", "inna-wa-akhawatuha", "mawadi-fath-anna", "al-bariz-al-muttasil"), s=[WA, BI, ("أَنَّ", "anna", "part"), P("هُ")]),
 pt("لَا", "la-nafiya", LA_NAF),
 v("يَقُولُ", "qala", MUDR(), HID("هُوَ"), CL("r", "خَبَرُ أَنَّ", "the predicate of أَنَّ", "أَنَّ'nin haberi", "inna-wa-akhawatuha"), g=["hollow-verbs"]),
 n("الشِّعْرَ", "shir", MF(), p="،"),
])
K("So ʿAntara said to him: «By God, people help one another with a meal, and you have never attended where people give that help — not you, nor your father, nor your grandfather;",
  "Bunun üzerine Antere ona dedi ki: «Vallahi insanlar yemek vererek birbirlerine yardım eder; ne sen, ne baban, ne de deden insanların bu yardımlaşma yerinde hiç bulunmadınız;", [
 v("فَقَالَ", "qala", PRE("fa", "قَالَ"), MADI, FAIL_BAD, Dn("وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "what is said is its object", "söylenen söz mef'ûlün bihtir", "maful-bihi"), s=[FA, ("قَالَ", "qala", "verb")], g=["hollow-verbs"]),
 pp("لَهُ", "li", JP("اللَّامُ", "هُ", ("اللَّامُ", "the lam", "lâm")), TA("قَالَ"), s=[("لَ", "li", "prep"), P("هُ")]),
 pn("عَنْتَرَةُ", "antara", FL(), ANTARA_DIPT, p=":"),
 pn("وَاللهِ", "allah", Fr("الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُقْسِمُ", "the waw is the particle of the oath, a jarr letter; the Name of Majesty is what is sworn by, in jarr by the kasra — the phrase hangs on an omitted verb, «I swear»", "vâv kasem ve cer harfi; lafza-i celâl kendisiyle yemin edilendir, kesre ile mecrûr — câr-mecrûr «yemin ederim» takdirindeki mahzûf fiile müteallik", "huruf-al-qasam-fil-kafiya", "huruf-jarr", "hadhf-wa-taqdir"), s=[("وَ", "wa-qasam", "part"), ("اللهِ", "allah", "propn")]),
 pt("إِنَّ", "inna", INNA_, Dn("كُسِرَتْ هَمْزَتُهَا لِوُقُوعِهَا فِي جَوَابِ الْقَسَمِ", "its hamza takes kasra because it opens the answer of the oath", "kasemin cevabında bulunduğu için hemzesi kesrelidir", "mawadi-kasr-inna")),
 NAS("n"),
 v("لَيَتَرَافَدُونَ", "tarafada-ant", LAM_MUZ, Fr("«يَتَرَافَدُونَ» فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "«يَتَرَافَدُونَ» is one of the five verbs, in raf' by the kept nun; the waw is its doer, in the seat of raf'", "«يَتَرَافَدُونَ» ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâildir, mahallen merfû", "afal-khamsa", "mudari-marfu", "al-bariz-al-muttasil", "form-vi-verbs"), CL_KH_INNA,
    Dn("تَرَافَدُوا: تَعَاوَنُوا، وَالرِّفْدُ: الْعَطَاءُ وَالصِّلَةُ (حَاشِيَةُ الْمُحَقِّقِ)", "تَرَافَدُوا: they helped one another; الرِّفْد is a gift, a bounty (the editor's note)", "تَرَافَدُوا: yardımlaştılar; الرِّفْد: bağış, ihsan (muhakkikin notu)"), s=[("لَ", "lam-ibtida", "part"), ("يَتَرَافَدُونَ", "tarafada-ant", "verb")]),
 n("بِالطُّعْمَةِ", "tuma-ant", JN("بِ", "الطُّعْمَةِ"), TA("يَتَرَافَدُونَ"), Dn("الطُّعْمَةُ بِضَمِّ الطَّاءِ: الْمَأْكَلَةُ وَالدَّعْوَةُ إِلَى الطَّعَامِ (حَاشِيَةُ الْمُحَقِّقِ)", "الطُّعْمَة, with damma on the ta: a meal given, a call to eat (the editor's note)", "الطُّعْمَة, tâ'nın dammesiyle: verilen yemek, yemeğe davet (muhakkikin notu)"), p="،", s=[BI, ("الطُّعْمَةِ", "tuma-ant", "noun")]),
 FA_MA(), HADARTA(),
 n("مَرْفِدَ", "marfid-ant", MF(), MDF, Dn("اسْمُ مَكَانٍ مِنْ رَفَدَ يَرْفِدُ: مَوْضِعُ التَّرَافُدِ", "a noun of place from رَفَدَ يَرْفِدُ: the place where such help is given", "رَفَدَ يَرْفِدُ fiilinden ism-i mekân: yardımlaşılan yer")),
 NAS("j"),
 ANTA_TAWKID(), WA_LA(), ABUKA(), WA_LA(), JADDUKA(),
 n("قَطُّ", "qattu", QATTU, ZT("حَضَرْتَ"), p="،"),
])
K("and people are called out in the raids and are known by the marks they wear, and we have never seen you among raiding horsemen in the front ranks of the men;",
  "insanlar baskınlarda çağrılır ve takındıkları nişanlarla tanınırlar; biz seni baskın yapan atlılar içinde, insanların ön saflarında hiç görmedik;", [
 WA_INNA(), NAS("n"),
 v("لَيُدْعَوْنَ", "daa", LAM_MUZ, Fr("«يُدْعَوْنَ» فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ", "«يُدْعَوْنَ» is a passive present verb, one of the five verbs, in raf' by the kept nun; the waw is its deputy doer, in the seat of raf'", "«يُدْعَوْنَ» ef'âl-i hamseden meçhul muzâri, nûnun sübûtuyla merfû; vâv nâib-i fâildir, mahallen merfû", "afal-khamsa", "mudari-marfu", "naib-al-fail", "al-majhul-fil-kafiya", "naqis-verbs"), CL_KH_INNA, s=[("لَ", "lam-ibtida", "part"), ("يُدْعَوْنَ", "daa", "verb")]),
 pp("فِي", "fi", HJ),
 n("الْغَارَاتِ", "ghara-ant", MJ(), TA("يُدْعَوْنَ"), Dn("جَمْعُ غَارَةٍ", "the plural of غَارَة", "غَارَة'nin cem'i", "jam-muannath-salim")),
 v("فَيُعْرَفُونَ", "arafa", PRE("fa", "يُعْرَفُونَ"), Fr("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ", "a passive present verb, one of the five verbs, in raf' by the kept nun; the waw is its deputy doer, in the seat of raf'", "ef'âl-i hamseden meçhul muzâri, nûnun sübûtuyla merfû; vâv nâib-i fâildir, mahallen merfû", "afal-khamsa", "mudari-marfu", "naib-al-fail", "al-majhul-fil-kafiya"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «يُدْعَوْنَ»", "the clause is conjoined to «يُدْعَوْنَ»", "cümle «يُدْعَوْنَ» kelimesine ma'tûftur"), s=[FA, ("يُعْرَفُونَ", "arafa", "verb")]),
 n("بِتَسْوِيمِهِمْ", "taswim-ant", JN("بِ", "تَسْوِيمِ"), IDF("هِمْ"), TA("يُعْرَفُونَ"), Dn("التَّسْوِيمُ: أَنْ يُعْلِمَ الْفَارِسُ نَفْسَهُ بِعَلَامَةٍ يُعْرَفُ بِهَا فِي الْحَرْبِ", "التَّسْوِيم: a horseman's marking himself with a sign by which he is known in battle", "التَّسْوِيم: süvarinin savaşta tanınacağı bir nişan takınması", "masdar"), p="،", s=[BI, ("تَسْوِيمِ", "taswim-ant", "noun"), P("هِمْ")]),
 FA_MA(),
 v("رَأَيْنَاكَ", "raa", Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا» الْفَاعِلِينَ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a past verb built on sukun because the نَا of the doers is attached; نَا is the doer, in the seat of raf'", "fâil «nâ»sı bitiştiği için sükûn üzere mebnî mâzî; نَا fâildir, mahallen merfû", "al-bariz-al-muttasil", "fail", "naqis-verbs"), OBJ("كَ"), s=[("رَأَيْ", "raa", "verb"), P("نَا"), P("كَ")]),
 pp("فِي", "fi", HJ),
 n("خَيْلٍ", "khayl", MJ(), TAM("hal", "الْكَافِ فِي «رَأَيْنَاكَ»"), Dn("وَالْخَيْلُ هُنَا: الْفُرْسَانُ", "«the horses» here are the horsemen", "«atlar» burada süvarilerdir")),
 n("مُغِيرَةٍ", "mughir-ant", NAT("خَيْلٍ"), Dn("اسْمُ فَاعِلٍ مِنْ أَغَارَ", "the active participle of أَغَارَ «to raid»", "أَغَارَ («baskın yapmak») fiilinden ism-i fâil", "ism-fail")),
 pp("فِي", "fi", HJ),
 n("أَوَائِلِ", "awail", MJ(), MDF, TAM("hal", "الْكَافِ"), Dn("جَمْعُ أَوَّلَ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ", "the plural of أَوَّل, a «farthest plural» (a diptote), yet in jarr by the kasra because it is annexed", "أَوَّل'in muntehe'l-cumû' vezninde cem'i (gayr-i munsarif); muzâf olduğu için kesre ile mecrûr", "jam-taksir", "mamnu-min-sarf")),
 NAS("j"),
 n("قَطُّ", "qattu", QATTU, ZT("رَأَيْنَاكَ"), p="،"),
])
K("and disputes do arise among us, and neither you nor your father nor your grandfather has ever attended the settling of a case; you are nothing but a truffle that sprang up in a soft hollow.",
  "aramızda karışık davalar olur; ne sen, ne baban, ne de deden bir davanın hükme bağlandığı yerde bulundunuz; sen ancak yumuşak bir düzlükte bitmiş bir mantarsın.", [
 WA_INNA(),
 n("اللَّبْسَ", "labs", ISM_INNA, Dn("اللَّبْسُ: اخْتِلَاطُ الْأَمْرِ وَاشْتِبَاهُهُ", "اللَّبْس: a matter's being tangled and unclear", "اللَّبْس: işin karışması, içinden çıkılmaz hâle gelmesi")),
 v("لَيَكُونُ", "kana", LAM_MUZ, Fr("«يَكُونُ» فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى اللَّبْسِ", "«يَكُونُ» is a defective present verb in raf' by the damma; its noun is the hidden «it» — the dispute", "«يَكُونُ» damme ile merfû nâkıs muzâri; ismi اللَّبْس'e dönen gizli zamir «o»", "kana-wa-akhawatuha", "mudari-marfu", "hollow-verbs"), CL_KH_INNA,
    Dn("وَيَجُوزُ أَنْ تَكُونَ تَامَّةً بِمَعْنَى يَقَعُ", "it may also be the complete كَانَ, «occurs»", "«vuku bulur» anlamında tâm fiil olması da câizdir", "al-fil-al-tamm-wal-naqis"), s=[("لَ", "lam-ibtida", "part"), ("يَكُونُ", "kana", "verb")]),
 n("بَيْنَنَا", "bayna", ZM(), IDF("نَا"), Dn("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «يَكُونُ»", "it hangs on the omitted predicate of «يَكُونُ»", "«يَكُونُ» fiilinin mahzûf haberine müteallik"), p="،", s=[("بَيْنَ", "bayna", "noun"), P("نَا")]),
 FA_MA(), HADARTA(), ANTA_TAWKID(), WA_LA(), ABUKA(), WA_LA(), JADDUKA(),
 n("خُطَّةَ", "khutta-ant", MF(), MDF, Dn("الْخُطَّةُ: الْأَمْرُ وَالْقِصَّةُ", "الْخُطَّة: an affair, a case", "الْخُطَّة: iş, dava")),
 n("فَيْصَلٍ", "faysal-ant", MI(), Dn("الْفَيْصَلُ: الْقَضَاءُ الَّذِي يَفْصِلُ بَيْنَ الْحَقِّ وَالْبَاطِلِ (حَاشِيَةُ الْمُحَقِّقِ عَنِ «اللِّسَانِ»)", "الْفَيْصَل: the judgement that parts right from wrong (the editor's note, from the Lisān)", "الْفَيْصَل: hak ile bâtılı ayıran hüküm (muhakkikin Lisân'dan notu)"), p="،"),
 pt("وَإِنَّمَا", "innama", PRE("wa", "إِنَّمَا"), Fr("كَافَّةٌ وَمَكْفُوفَةٌ، أَدَاةُ حَصْرٍ", "إِنَّ held back by مَا, a particle of restriction", "kâffe ve mekfûfe, hasr edatı", "innama-kaffa"),
    HD("قَصْرٌ بِـ«إِنَّمَا»: قَصَرَ الْمُخَاطَبَ عَلَى صِفَةِ الْفَقْعِ", "this is a restriction (qaṣr) by إِنَّمَا: the man addressed is confined to being a truffle", "bu, «إِنَّمَا» ile yapılmış bir kasrdır: muhatap «mantar» olma sıfatına hasredilmiştir", "qasr", "turuq-al-qasr"), s=[WA, ("إِنَّمَا", "innama", "part")]),
 pro("أَنْتَ", "anta", Fr("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "a detached pronoun built on fatha, the mubtada, in the seat of raf'", "fetha üzere mebnî munfasıl zamir, mübtedâ, mahallen merfû", "mubtada-khabar")),
 n("فَقْعٌ", "faq-ant", KH(), Dn("الْفَقْعُ بِالْفَتْحِ وَالْكَسْرِ: الرِّخْوُ مِنَ الْكَمْأَةِ وَهُوَ أَرْدَؤُهَا (حَاشِيَةُ الْمُحَقِّقِ)", "الْفَقْع, with fatha or kasra: the soft white truffle, the poorest kind (the editor's note)", "الْفَقْع, fetha veya kesre ile: yumuşak beyaz yer mantarı, mantarların en kötüsü (muhakkikin notu)"),
    HD("تَشْبِيهٌ حُذِفَتْ أَدَاتُهُ وَوَجْهُهُ: الْمُشَبَّهُ الْمُخَاطَبُ، وَالْمُشَبَّهُ بِهِ الْفَقْعُ النَّابِتُ بِالْقَرْقَرِ، وَالْوَجْهُ الذِّلَّةُ؛ وَفِي الْمَثَلِ: «أَذَلُّ مِنْ فَقْعٍ بِقَرْقَرٍ» لِأَنَّ الدَّوَابَّ تَطَؤُهُ بِأَرْجُلِهَا وَلَا أَصْلَ لَهُ (حَاشِيَةُ الْمُحَقِّقِ)",
       "this is a tashbih with neither particle nor point of likeness stated: the man addressed is likened to a truffle sprung up in a soft hollow, the point being lowliness — the proverb runs «lowlier than a truffle in a hollow», for the beasts tread it underfoot and it has no root (the editor's note)",
       "bu, edatı ve vechi hazfedilmiş bir teşbîhtir: müşebbeh muhatap, müşebbehün bih düzlükte biten mantar, vech-i şebeh zillettir; darbımeselde «düzlükteki mantardan daha zelil» denir, çünkü hayvanlar onu ayaklarıyla çiğner ve kökü yoktur (muhakkikin notu)", "tashbih", "aqsam-al-tashbih")),
 v("نَبَتَ", "nabata", MADI, HID("هُوَ", ("الْفَقْعِ", "the truffle", "mantar")), CL_NAAT("فَقْعٌ", "r"), g=["thulathi-mujarrad-babs"]),
 n("بِقَرْقَرٍ", "qarqar-ant", JN("بِ", "قَرْقَرٍ", sense=FI_SENSE), TA("نَبَتَ"), Dn("الْقَرْقَرُ: الْأَرْضُ الْمُطْمَئِنَّةُ اللَّيِّنَةُ (حَاشِيَةُ الْمُحَقِّقِ)", "الْقَرْقَر: low, soft, level ground (the editor's note)", "الْقَرْقَر: alçak, yumuşak düz arazi (muhakkikin notu)"), p="،", s=[BI, ("قَرْقَرٍ", "qarqar-ant", "noun")]),
])
ANA_HID = HID("أَنَا")
def ATF_V(full, lex, stem, est=None, g=None, note=None):
    """وَأَعِفُّ: a present verb conjoined to «أَحْتَضِرُ», its doer the hidden «I»"""
    return v(full, lex, PRE("wa", stem), MUDR(est), ANA_HID, Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «أَحْتَضِرُ»", "the clause is conjoined to «أَحْتَضِرُ»", "cümle «أَحْتَضِرُ» cümlesine ma'tûftur"), note, s=[WA, (stem, lex, "verb")], g=g)
K("As for me, I am there when the fighting is hard, I hand over the spoil in full, I hold back from begging, I give freely of what my hand owns, and I settle the sharp-cut case. As for poetry — you shall know.»",
  "Bana gelince: ben savaşın kızıştığı yerde hazır bulunurum, ganimeti eksiksiz veririm, dilenmekten uzak dururum, elimin sahip olduğu şeyi cömertçe veririm, keskin davayı hükme bağlarım. Şiire gelince — onu da göreceksin.»", [
 pt("وَإِنِّي", "inna", PRE("wa", "إِنَّ"), INNA_, Fr("، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the attached ya is its noun, in the seat of nasb", "; bitişik yâ ismidir, mahallen mansûb", "al-bariz-al-muttasil", "ya-al-mutakallim"), s=[WA, ("إِنِّ", "inna", "part"), P("ي")]),
 v("لَأَحْتَضِرُ", "ihtadara-ant", LAM_MUZ, Fr("«أَحْتَضِرُ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ", "«أَحْتَضِرُ» is a present verb in raf' by the damma", "«أَحْتَضِرُ» damme ile merfû muzâri", "mudari-marfu", "form-viii-verbs"), ANA_HID, CL_KH_INNA, Dn("احْتَضَرَ الشَّيْءَ: حَضَرَهُ وَشَهِدَهُ", "احْتَضَرَ a thing: was present at it", "احْتَضَرَ: bir şeyde hazır bulundu"), s=[("لَ", "lam-ibtida", "part"), ("أَحْتَضِرُ", "ihtadara-ant", "verb")]),
 n("الْبَأْسَ", "bas", MF(), Dn("الْبَأْسُ: الشِّدَّةُ فِي الْحَرْبِ", "الْبَأْس: the stress of battle", "الْبَأْس: savaşın şiddeti"), p="،"),
 ATF_V("وَأُوفِي", "awfa", "أُوفِي", est="y", g=["form-iv-verbs"], note=Dn("أَوْفَى الشَّيْءَ: أَعْطَاهُ وَافِيًا تَامًّا", "أَوْفَى a thing: gave it whole and in full", "أَوْفَى: bir şeyi tam ve eksiksiz verdi")),
 n("الْمَغْنَمَ", "maghnam", MF(), p="،"),
 ATF_V("وَأَعِفُّ", "affa-ant", "أَعِفُّ", g=["doubled-verbs"]),
 pp("عَنِ", "an", HJ, Dn("وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "voweled with kasra before the following ال", "iki sâkin karşılaştığı için kesre ile harekelendi")),
 n("الْمَسْأَلَةِ", "masala", MJ(), TA("أَعِفُّ"), Dn("الْمَسْأَلَةُ هُنَا: سُؤَالُ النَّاسِ أَمْوَالَهُمْ", "الْمَسْأَلَة here: asking people for what they have", "الْمَسْأَلَة burada: insanlardan mal istemek"), p="،"),
 ATF_V("وَأَجُودُ", "jada", "أَجُودُ", g=["hollow-verbs"]),
 BIMA(), MALAKAT(),
 n("يَدِي", "yad", FL("rM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), Dn("وَالْجَارُّ وَالْمَجْرُورُ «بِمَا» مُتَعَلِّقَانِ بِـ«أَجُودُ»", "the phrase «بِمَا» hangs on «أَجُودُ»", "«بِمَا» câr-mecrûru «أَجُودُ» kelimesine müteallik"), p="،", s=[("يَدِ", "yad", "noun"), P("ي")]),
 ATF_V("وَأَفْصِلُ", "fasala", "أَفْصِلُ", g=["thulathi-mujarrad-babs"]),
 n("الْخُطَّةَ", "khutta-ant", MF()),
 n("الصَّمْعَاءَ", "samaa-ant", NAT("الْخُطَّةَ", "n"), Dn("الصَّمْعَاءُ: الْمَاضِيَةُ (حَاشِيَةُ الْمُحَقِّقِ)", "الصَّمْعَاء: the keen one, that cuts straight through (the editor's note)", "الصَّمْعَاء: keskin, kestirip atan (muhakkikin notu)"), p="،"),
 pt("وَأَمَّا", "amma", PRE("wa", "أَمَّا"), Fr("حَرْفُ شَرْطٍ وَتَفْصِيلٍ", "the particle of condition and detailing, «as for …»", "şart ve tafsîl harfi", "amma-tafsiliyya", "amma-fil-kafiya"), s=[WA, ("أَمَّا", "amma", "part")]),
 n("الشِّعْرُ", "shir", MB()),
 v("فَسَتَعْلَمُ", "alima", Fr("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَالسِّينُ حَرْفُ اسْتِقْبَالٍ، وَ«تَعْلَمُ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ", "the fa stands in the answer of أَمَّا; the sin is the particle of the future; «تَعْلَمُ» is a present verb in raf' by the damma", "fâ «أَمَّا»nın cevabındadır; sîn istikbâl harfi; «تَعْلَمُ» damme ile merfû muzâri", "al-fa-fi-jawab-al-shart", "mudari-marfu"), HID("أَنْتَ"), CL_KH,
    Dn("وَالْمَفْعُولُ مَحْذُوفٌ، أَيْ: فَسَتَعْلَمُهُ — وَعْدٌ فِي مَعْنَى الْوَعِيدِ", "its object is dropped, «you shall know it» — a promise that is a threat", "mef'ûlü hazfedilmiştir: «onu bileceksin» — tehdit mânâsında bir vaad", "hadhf-al-maful"), p=".", s=[FA, ("سَ", "sa-istiqbal", "part"), ("تَعْلَمُ", "alima", "verb")]),
])
K("And the first thing he composed was an ode — «Have the poets left any place unpatched?» — which is the finest of his poetry; they used to call it «the Gilded».",
  "İlk söylediği şey bir kaside oldu: «Şairler yamanacak bir yer bıraktı mı?» — bu, onun şiirinin en güzelidir; ona «el-Müzhebe» (Yaldızlı) derlerdi.", [
 v("فَكَانَ", "kana", PRE("fa", "كَانَ"), KANA, s=[FA, ("كَانَ", "kana", "verb")]),
 n("أَوَّلُ", "awwal", RO("اسْمُ كَانَ", "the noun of كَانَ", "كَانَ'nin ismi", "r", "kana-wa-akhawatuha"), MDF),
 pro("مَا", "ma-mawsula", Fr("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "a relative noun built on sukun, the second term of the idafa, in the seat of jarr", "sükûn üzere mebnî ism-i mevsûl, muzâfun ileyh, mahallen mecrûr", "ism-mawsul", "idafa-definiteness")),
 v("قَالَ", "qala", MADI, HID("هُوَ"), CL_SILA, Dn("وَالْعَائِدُ مَحْذُوفٌ، أَيْ: قَالَهُ", "the returning pronoun is dropped: «what he said»", "âid zamir hazfedilmiştir: «söylediği»", "hadhf-al-maful"), g=["hollow-verbs"]),
 n("قَصِيدَةً", "qasida", RO("خَبَرُ كَانَ", "the predicate of كَانَ", "كَانَ'nin haberi", "n", "kana-wa-akhawatuha"), p=":"),
 pt("هَلْ", "hal-istifham", Fr("حَرْفُ اسْتِفْهَامٍ — وَالشَّطْرُ مَحْكِيٌّ، وَهُوَ صَدْرُ الْمُعَلَّقَةِ يُعَرِّفُ الْقَصِيدَةَ بِهِ (بَدَلٌ مِنْ «قَصِيدَةً»)، وَإِعْرَابُ كَلِمَاتِهِ عَلَى مَا هِيَ عَلَيْهِ فِي الْبَيْتِ", "the particle of question — the hemistich is quoted: it is the opening of the Muʿallaqa, and names the ode (a badal of «قَصِيدَةً»); its words are parsed as they stand in the verse", "istifhâm harfi — mısra hikâye edilmiştir: muallakanın ilk mısraıdır ve kasideyi tanıtır («قَصِيدَةً»den bedel); kelimeleri beyitteki hâlleriyle i'râb edilir", "al-istifham", "badal")),
 v("غَادَرَ", "ghadara-ant", MADI, FAIL_BAD, g=["form-iii-verbs"]),
 n("الشُّعَرَاءُ", "shair", FL(), Dn("جَمْعُ شَاعِرٍ عَلَى فُعَلَاءَ", "the plural of «poet», on the pattern فُعَلَاء", "شَاعِر'in fu'alâ vezninde cem'i", "jam-taksir")),
 pp("مِنْ", "min", Fr("حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ الْمَفْهُومِ مِنَ الِاسْتِفْهَامِ", "an added jarr letter: it strengthens the denial the question carries", "zâid cer harfi: istifhâmdan anlaşılan nefyi pekiştirir", "huruf-jarr", "huruf-al-ziyada-fil-kafiya")),
 n("مُتَرَدَّمِ", "mutaraddam-ant", Fr("مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "the direct object, in nasb by a fatha that the vowel of the added jarr letter keeps from showing", "mef'ûlün bih; zâid cer harfinin harekesi yüzünden zâhir olmayan takdîrî fetha ile mansûb", "maful-bihi"), QT, p="،"),
 pro("وَهِيَ", "hiya", PRE("wa-ist", "هِيَ"), Fr("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "a detached pronoun built on fatha, the mubtada, in the seat of raf'", "fetha üzere mebnî munfasıl zamir, mübtedâ, mahallen merfû", "mubtada-khabar"), s=[WA, ("هِيَ", "hiya", "pron")]),
 n("أَجْوَدُ", "ajwad-ant", KH(), MDF, Dn("اسْمُ تَفْضِيلٍ مِنَ الْجَوْدَةِ", "an elative of «goodness»: «the finest»", "«iyilik, kalite»den ism-i tafdîl: «en güzeli»", "ism-tafdil")),
 n("شِعْرِهِ", "shir", MI(), IDF("هِ"), p="،", s=[("شِعْرِ", "shir", "noun"), P("هِ")]),
 v("وَكَانُوا", "kana", PRE("wa", "كَانُوا"), Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ", "the defective past verb, built on damma because the waw of the group is attached; that waw is the noun of كَانَ, in the seat of raf'", "cemâat vâvı bitiştiği için damme üzere mebnî nâkıs mâzî; vâv كَانَ'nin ismidir, mahallen merfû", "kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"), s=[WA, ("كَانُو", "kana", "verb"), ("ا", "pron-3mp", "pron")]),
 v("يُسَمُّونَهَا", "samma", MUDR5, OBJ("هَا", ("مَفْعُولٌ بِهِ أَوَّلُ", "its first object", "birinci mef'ûlün bih")), CL("n", "خَبَرُ كَانَ", "the predicate of كَانَ", "كَانَ'nin haberi", "kana-wa-akhawatuha"), s=[("يُسَمُّونَ", "samma", "verb"), P("هَا")], g=["form-ii-verbs", "naqis-verbs", "mafulayn"]),
 n("الْمُذْهَبَةَ", "mudhhaba-ant", MF2(), Dn("اسْمُ مَفْعُولٍ مِنْ أَذْهَبَ الشَّيْءَ: طَلَاهُ بِالذَّهَبِ (حَاشِيَةُ الْمُحَقِّقِ)", "the passive participle of أَذْهَبَ «to gild»: «the gilded one» (the editor's note)", "أَذْهَبَ («altınla kaplamak») fiilinden ism-i mef'ûl: «yaldızlı» (muhakkikin notu)", "ism-maful"), p="."),
])

# =====================================================================================================================
# Chapter 2 — دَارُ عَبْلَةَ بِالْجِوَاءِ (al-Zawzanī vv. 1–8)
# =====================================================================================================================
ZAW, DUR = "(الزَّوْزَنِيُّ)", "(الدُّرَّةُ)"
ABLA_DIPT = Dn("عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ", "a woman's name, barred from tanwin", "müennes özel isim, gayr-i munsarif", "mamnu-min-sarf")
MUNADA_M = Fr("مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ", "the one called, annexed and so in nasb by the fatha", "muzâf münâdâ, fetha ile mansûb", "vocative-munada", "idafa-definiteness")
AMR_Y = Fr("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "an imperative built on the dropping of the nun — its present is one of the five verbs — and the ya of the woman addressed is its doer, in the seat of raf'",
           "nûnun hazfi üzere mebnî emir — muzârii ef'âl-i hamsedendir — muhâtaba yâsı fâildir, mahallen merfû", "imperative-amr", "afal-khamsa", "al-bariz-al-muttasil")
ZAID_MIN = Fr("حَرْفُ جَرٍّ زَائِدٌ", "an added jarr letter", "zâid cer harfi", "huruf-jarr", "huruf-al-ziyada-fil-kafiya")
LAYSA_ = Fr("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مِنْ أَخَوَاتِ كَانَ", "the frozen defective verb «is not», a sister of كَانَ", "كَانَ'nin kardeşlerinden câmid nâkıs fiil («değildir»)", "kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins")
def BI_ZAID(word, rhyme=QT):
    """بِمَزْعَمِ: the added ba on the predicate of لَيْسَ"""
    return Fr("الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَ«%s» خَبَرُ لَيْسَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ" % word,
              "the ba is an added jarr letter that strengthens the negation; «%s» is the predicate of لَيْسَ, in nasb by a fatha that the vowel of the added letter keeps from showing" % word,
              "bâ nefyi pekiştiren zâid cer harfi; «%s» لَيْسَ'nin haberi, zâid cer harfinin harekesi yüzünden zâhir olmayan takdîrî fetha ile mansûb" % word, "huruf-jarr", "huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha")

# ---- v. 1 ----
V(1, "Have the poets left any place in need of a patch? — Or rather: did you know the abode again, after doubting?",
  "Şairler yamanacak bir yer bıraktı mı? — Yoksa (bırak bunu:) tereddütten sonra yurdu tanıdın mı?",
 [pt("هَلْ", "hal-istifham", Fr("حَرْفُ اسْتِفْهَامٍ", "the particle of question", "istifhâm harfi", "al-istifham"),
     Sn("وَالِاسْتِفْهَامُ يَتَضَمَّنُ مَعْنَى الْإِنْكَارِ، أَيْ: لَمْ يَتْرُكِ الشُّعَرَاءُ شَيْئًا يُصَاغُ فِيهِ شِعْرٌ إِلَّا وَقَدْ صَاغُوهُ فِيهِ " + ZAW + ". وَالْقَصِيدَةُ مِنَ الْبَحْرِ الْكَامِلِ",
        "the question carries a denial: the poets have left nothing that verse can be made of but they have made it (al-Zawzanī). The ode is in the metre al-kāmil",
        "istifhâm inkâr mânâsı taşır: şairler, hakkında şiir söylenebilecek hiçbir şey bırakmamış, hepsini söylemişlerdir (Zevzenî). Kaside kâmil bahrindendir", "khuruj-al-istifham", "ilm-al-arud")),
  v("غَادَرَ", "ghadara-ant", MADI, FAIL_BAD, g=["form-iii-verbs"]),
  n("الشُّعَرَاءُ", "shair", FL(), Dn("جَمْعُ شَاعِرٍ عَلَى فُعَلَاءَ", "the plural of «poet», on the pattern فُعَلَاء", "شَاعِر'in fu'alâ vezninde cem'i", "jam-taksir")),
  pp("مِنْ", "min", ZAID_MIN, Dn("زِيدَ لِتَوْكِيدِ النَّفْيِ الَّذِي فِي الِاسْتِفْهَامِ", "added to strengthen the denial in the question", "istifhâmdaki nefyi pekiştirmek için eklenmiştir")),
  n("مُتَرَدَّمِ", "mutaraddam-ant", Fr("مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "the direct object, in nasb by a fatha that the vowel of the added jarr letter keeps from showing", "mef'ûlün bih; zâid cer harfinin harekesi yüzünden zâhir olmayan takdîrî fetha ile mansûb", "maful-bihi"), QT,
     Dn("الْمُتَرَدَّمُ: الْمَوْضِعُ الَّذِي يُسْتَرْقَعُ وَيُسْتَصْلَحُ لِمَا اعْتَرَاهُ مِنَ الْوَهْنِ " + ZAW + "؛ وَالْبَيْتُ مُصَرَّعٌ: عَرُوضُهُ عَلَى رَوِيِّ ضَرْبِهِ", "الْمُتَرَدَّم: a place to be patched and put right where it has worn thin (al-Zawzanī); the verse is muṣarraʿ — its first hemistich ends on the rhyme too", "الْمُتَرَدَّم: yıprandığı için yamanıp onarılacak yer (Zevzenî); beyit musarra'dır: ilk mısraı da kâfiyelidir"),
     Sn("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: شَبَّهَ مَا يُقَالُ فِيهِ الشِّعْرُ مِنَ الْمَعَانِي بِالْمَوْضِعِ الَّذِي يُرْقَعُ، وَحَذَفَ الْمُشَبَّهَ؛ قَالَ الدُّرَّةُ: «وَإِنَّمَا هٰذَا مَثَلٌ، يَقُولُ: هَلْ تَرَكُوا مَقَالًا لِقَائِلٍ»",
        "here is an istiʿāra taṣrīḥiyya: the themes verse is made of are likened to a place that is patched, and the thing likened is left unsaid; al-Durra: «this is only a figure — he means: have they left anyone anything to say?»",
        "burada istiâre-i tasrîhiyye vardır: hakkında şiir söylenen mânâlar yamanan yere benzetilmiş, müşebbeh hazfedilmiştir; Dürre: «Bu ancak bir temsildir; ‹söyleyecek birine söz bıraktılar mı?› demektir»", "istiara", "aqsam-al-istiara"))],
 [pt("أَمْ", "am", Fr("حَرْفُ عَطْفٍ", "a conjunction", "atıf harfi", "atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya"), Dn("وَهِيَ الْمُنْقَطِعَةُ بِمَعْنَى «بَلْ» مَعَ هَمْزَةِ الِاسْتِفْهَامِ: أَضْرَبَ عَنِ الْكَلَامِ الْأَوَّلِ وَأَخَذَ فِي فَنٍّ آخَرَ " + ZAW, "the «cut-off» أَمْ, meaning «rather …?»: he turns from his first words and takes up another matter (al-Zawzanī)", "munkatı'a olan أَمْ: «بَلْ» ve istifhâm hemzesi anlamındadır; şair ilk sözünden dönüp başka bir konuya geçmiştir (Zevzenî)")),
  pt("هَلْ", "hal-istifham", Fr("حَرْفُ اسْتِفْهَامٍ", "the particle of question", "istifhâm harfi", "al-istifham"), Dn("وَيَجُوزُ أَنْ تَكُونَ بِمَعْنَى «قَدْ» " + ZAW, "it may also mean «قَدْ» (al-Zawzanī)", "«قَدْ» anlamında olması da câizdir (Zevzenî)")),
  v("عَرَفْتَ", "arafa", TU("anta"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا لَا مَحَلَّ لَهَا", "the clause is conjoined to the one before and has no seat", "cümle öncekine ma'tûftur, i'râbdan mahalli yoktur"),
     Sn("وَفِيهِ تَجْرِيدٌ: جَرَّدَ مِنْ نَفْسِهِ شَخْصًا وَخَاطَبَهُ " + DUR + "؛ قَالَ الزَّوْزَنِيُّ: «فَقَالَ مُخَاطِبًا لِنَفْسِهِ»", "here is a tajrīd: he draws a second person out of himself and speaks to him (al-Durra); al-Zawzanī: «he says it addressing himself»", "burada tecrîd vardır: kendi nefsinden bir şahıs çıkarıp ona hitap etmiştir (Dürre); Zevzenî: «kendi nefsine hitap ederek söyler»", "tajrid"), g=["thulathi-mujarrad-babs"]),
  n("الدَّارَ", "dar", MF()),
  n("بَعْدَ", "bada", ZZ(), MDF, ZT("عَرَفْتَ")),
  n("تَوَهُّمِ", "tawahhum", MI(), QT, Dn("أَيْ: بَعْدَ شَكِّكَ فِيهَا " + ZAW, "that is, after your doubt about it (al-Zawzanī)", "yani: onun hakkındaki şüphenden sonra (Zevzenî)", "masdar"))])

# ---- v. 2 ----
V(2, "O abode of ʿAbla at al-Jiwāʾ, speak! A good morning to you, abode of ʿAbla, and may you be safe.",
  "Ey Able'nin Civâ'daki yurdu, konuş! Sabahın hayrolsun ey Able'nin yurdu, selâmette ol.",
 [pt("يَا", "ya-nida", Fr("حَرْفُ نِدَاءٍ", "the vocative particle", "nidâ harfi", "vocative-munada")),
  n("دَارَ", "dar", MUNADA_M),
  pn("عَبْلَةَ", "abla-ant", MI("jf"), Dn("عَبْلَةُ: اسْمُ عَشِيقَتِهِ " + ZAW, "ʿAbla is the name of the woman he loves (al-Zawzanī)", "Able: sevdiği kadının adı (Zevzenî)")),
  n("بِالْجِوَاءِ", "jiwa", JN("بِ", "الْجِوَاءِ", sense=FI_SENSE), TAM("naat", "دَارَ عَبْلَةَ"), Dn("أَوْ بِمَحْذُوفٍ حَالٍ مِنْهُ " + DUR + "؛ وَالْجِوَاءُ جَمْعُ جَوٍّ وَهُوَ الْوَادِي، وَهُوَ فِي الْبَيْتِ مَوْضِعٌ بِعَيْنِهِ " + ZAW, "or on an omitted hal of it (al-Durra); الْجِوَاء is the plural of جَوّ, a valley — in the verse a particular place (al-Zawzanī)", "yahut ondan mahzûf bir hâle (Dürre); الْجِوَاء, «vadi» anlamındaki جَوّ'in cem'idir; beyitte belirli bir yerin adıdır (Zevzenî)"), s=[BI, ("الْجِوَاءِ", "jiwa", "noun")]),
  v("تَكَلَّمِي", "takallama", AMR_Y, Dn("أَيْ: أَخْبِرِينِي عَنْ أَهْلِكِ مَا فَعَلُوا " + ZAW, "that is: tell me what has become of your people (al-Zawzanī)", "yani: halkının ne yaptığını bana haber ver (Zevzenî)"), g=["form-v-verbs"])],
 [v("وَعِمِي", "waama-ant", PRE("wa", "عِمِي"), AMR_Y, Dn("مِنْ وَعَمَ يَعِمُ بِمَعْنَى نَعِمَ يَنْعَمُ", "from وَعَمَ يَعِمُ, the same as نَعِمَ يَنْعَمُ «to live in ease»", "وَعَمَ يَعِمُ fiilinden; نَعِمَ يَنْعَمُ («refah içinde olmak») ile aynı anlamda", "mithal-verbs"),
     Sn("وَالْأَمْرُ خَرَجَ إِلَى الدُّعَاءِ وَالتَّحِيَّةِ: أَضْرَبَ عَنِ اسْتِخْبَارِهَا إِلَى تَحِيَّتِهَا فَقَالَ: طَابَ عَيْشُكِ فِي صَبَاحِكِ وَسَلِمْتِ " + ZAW, "the imperative has passed to prayer and greeting: he turns from asking it for news to greeting it — «may your life be sweet this morning, and may you be safe» (al-Zawzanī)", "emir, dua ve selâmlama mânâsına çıkmıştır: ondan haber sormaktan onu selâmlamaya dönmüş, «sabahında hayatın hoş olsun, selâmette ol» demiştir (Zevzenî)", "al-amr-wa-wujuhuh"), s=[WA, ("عِمِي", "waama-ant", "verb")]),
  n("صَبَاحًا", "sabah", ZZ(), ZT("عِمِي"), Dn("وَيَجُوزُ أَنْ يَكُونَ تَمْيِيزًا مُحَوَّلًا عَنِ الْفَاعِلِ " + DUR, "it may also be a tamyiz turned from the doer (al-Durra)", "fâilden çevrilmiş temyîz olması da câizdir (Dürre)")),
  n("دَارَ", "dar", MUNADA_M, Dn("حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ", "its vocative particle is dropped", "nidâ harfi hazfedilmiştir", "hadhf-wa-taqdir")),
  pn("عَبْلَةَ", "abla-ant", MI("jf")),
  v("وَاسْلَمِي", "salima-safe", PRE("wa", "اسْلَمِي"), AMR_Y, Dn("وَهُوَ دُعَاءٌ لَهَا بِالسَّلَامَةِ", "a prayer that it be kept safe", "onun selâmeti için duadır", "al-amr-wa-wujuhuh"), g=["thulathi-mujarrad-babs", "al-qafiya"], s=[WA, ("اسْلَمِي", "salima-safe", "verb")])])

# ---- v. 3 ----
V(3, "I halted my she-camel in it — and she was like a castle — to do what a lingerer needs to do.",
  "Orada, bir köşk gibi (iri) olan devemi durdurdum; oyalanan kimsenin ihtiyacını gidermek için.",
 [v("فَوَقَفْتُ", "waqafa", PRE("fa-ist", "وَقَفْتُ"), TU("ana"), Dn("وَنَصَبَ الْمَفْعُولَ لِأَنَّهُ بِمَعْنَى حَبَسْتُ " + DUR, "it takes an object because it means «I held back» (al-Durra)", "«alıkoydum» anlamında olduğu için mef'ûl almıştır (Dürre)", "al-lazim-wal-mutaaddi"), s=[FA, ("وَقَفْتُ", "waqafa", "verb")], g=["mithal-verbs"]),
  pp("فِيهَا", "fi", JP("فِي", "هَا"), TA("وَقَفْتُ"), s=[("فِي", "fi", "prep"), P("هَا")]),
  n("نَاقَتِي", "naqa", MF("nM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), s=[("نَاقَتِ", "naqa", "noun"), P("ي")]),
  pt("وَكَأَنَّهَا", "kaanna", PRE("wa-hal", "كَأَنَّ"), Fr("حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "the particle of likening that puts its noun in nasb; the attached هَا is that noun", "teşbîh ve nasb harfi; bitişik هَا ismidir, mahallen mansûb", "inna-wa-akhawatuha", "al-bariz-al-muttasil"), CL_HAL("نَاقَتِي"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ النَّاقَةُ، وَالْمُشَبَّهُ بِهِ الْفَدَنُ وَهُوَ الْقَصْرُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الْعِظَمُ وَضِخَمُ الْجِرْمِ " + ZAW,
        "here is a tashbih mursal mujmal: the thing likened is the she-camel; the thing it is likened to, a castle; the tool is كَأَنَّ; the point of likeness is left unsaid — greatness and bulk of body (al-Zawzanī)",
        "burada mürsel mücmel bir teşbîh vardır: müşebbeh deve; müşebbehün bih köşk; edat «كَأَنَّ»; vech-i şebeh hazfedilmiştir — büyüklük ve gövde iriliği (Zevzenî)", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"), s=[WA, ("كَأَنَّ", "kaanna", "part"), P("هَا")])],
 [n("فَدَنٌ", "fadan-ant", RO("خَبَرُ كَأَنَّ", "the predicate of كَأَنَّ", "كَأَنَّ'nin haberi", "r", "inna-wa-akhawatuha"), Dn("الْفَدَنُ: الْقَصْرُ، وَالْجَمْعُ الْأَفْدَانُ " + ZAW + "؛ وَهُوَ الْمُشَبَّهُ بِهِ", "الْفَدَن: a castle, pl. أَفْدَان (al-Zawzanī); it is the thing she is likened to", "الْفَدَن: köşk, ç. أَفْدَان (Zevzenî); müşebbehün bihtir", "tashbih")),
  v("لِأَقْضِيَ", "qada-verb", Fr("اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَ«أَقْضِيَ» فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "the lam is the lam of purpose, a jarr letter; «أَقْضِيَ» is a present verb put in nasb by an أَنْ hidden after it, its sign the fatha", "lâm ta'lîl lâmıdır, cer harfi; «أَقْضِيَ» lâmdan sonra gizli أَنْ ile mansûb muzâri, alâmeti fetha", "lam-taleel", "nawasib-wa-jawazim-al-mudari", "naqis-verbs"), HID("أَنَا"),
     Dn("وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِاللَّامِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَقَفْتُ»", "the masdar the clause makes is in the seat of jarr by the lam, and the phrase hangs on «وَقَفْتُ»", "müevvel masdar lâm ile mahallen mecrûr; câr-mecrûr «وَقَفْتُ» kelimesine müteallik", "an-masdariyya"), s=[LI, ("أَقْضِيَ", "qada-verb", "verb")]),
  n("حَاجَةَ", "haja", MF(), MDF),
  n("الْمُتَلَوِّمِ", "mutalawwim-ant", MI(), QA, Dn("الْمُتَلَوِّمُ: الْمُتَمَكِّثُ، يَعْنِي نَفْسَهُ: أَقْضِي حَاجَةَ الْمُتَمَكِّثِ بِجَزَعِي مِنْ فِرَاقِهَا وَبُكَائِي عَلَى أَيَّامِ وِصَالِهَا " + ZAW, "الْمُتَلَوِّم: one who lingers — he means himself: to do the lingerer's need, grieving at her going and weeping for the days he had with her (al-Zawzanī)", "الْمُتَلَوِّم: oyalanan, bekleyen — kendisini kasteder: ayrılığına üzülüp vuslat günlerine ağlayarak oyalanan kimsenin ihtiyacını gidermek (Zevzenî)", "ism-fail"))])

# ---- v. 4 ----
V(4, "ʿAbla stays at al-Jiwāʾ, and our people at al-Ḥazn, then al-Ṣammān, then al-Mutathallam.",
  "Able Civâ'da konaklar; bizimkiler ise Hazn'da, sonra Sammân'da, sonra Mütesellem'de.",
 [v("وَتَحُلُّ", "halla-settle", PRE("wa", "تَحُلُّ"), MUDR(), FAIL_BAD, Dn("وَيَجُوزُ أَنْ تَكُونَ الْوَاوُ اسْتِئْنَافِيَّةً " + DUR, "the waw may also open a new sentence (al-Durra)", "vâvın isti'nâfiyye olması da câizdir (Dürre)"), s=[WA, ("تَحُلُّ", "halla-settle", "verb")], g=["doubled-verbs"]),
  pn("عَبْلَةُ", "abla-ant", FL(), ABLA_DIPT),
  n("بِالْجِوَاءِ", "jiwa", JN("بِ", "الْجِوَاءِ", sense=FI_SENSE), TA("تَحُلُّ"), s=[BI, ("الْجِوَاءِ", "jiwa", "noun")]),
  n("وَأَهْلُنَا", "ahl", PRE("wa", "أَهْلُ"), ATF("عَبْلَةُ", "r"), IDF("نَا"), Dn("عَلَى تَقْدِيرِ فِعْلٍ، أَيْ: وَيَحُلُّ أَهْلُنَا " + DUR + "؛ وَظَاهِرُ تَفْسِيرِ الزَّوْزَنِيِّ أَنَّهُ مُبْتَدَأٌ خَبَرُهُ «بِالْحَزْنِ»: وَأَهْلُنَا نَازِلُونَ بِهٰذِهِ الْمَوَاضِعِ", "with a verb understood, «and our people stay …» (al-Durra); al-Zawzanī's gloss reads it as a mubtada whose khabar is «بِالْحَزْنِ»: «and our people are settled in these places»", "bir fiil takdiriyle: «bizimkiler de konaklar» (Dürre); Zevzenî'nin açıklamasına göre ise mübtedâdır, haberi «بِالْحَزْنِ»dir: «bizimkiler bu yerlerde konaklamıştır»", "hadhf-wa-taqdir"), s=[WA, ("أَهْلُ", "ahl", "noun"), P("نَا")])],
 [n("بِالْحَزْنِ", "hazn", JN("بِ", "الْحَزْنِ", sense=FI_SENSE), Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَحْذُوفِ؛ وَالْحَزْنُ مَوْضِعٌ", "the phrase hangs on the understood verb; al-Ḥazn is a place", "câr-mecrûr mahzûf fiile müteallik; Hazn bir yer adıdır"), s=[BI, ("الْحَزْنِ", "hazn", "noun")]),
  pn("فَالصَّمَّانِ", "samman-ant", PRE("fa", "الصَّمَّانِ"), ATF("الْحَزْنِ"), Dn("اسْمُ مَوْضِعٍ؛ وَالْفَاءُ تُفِيدُ التَّعْقِيبَ: يَنْتَقِلُونَ مِنْ مَوْضِعٍ إِلَى آخَرَ " + DUR, "a place-name; the fa marks succession — they move on from one place to the next (al-Durra)", "yer adı; fâ ta'kîb bildirir: bir yerden ötekine göçerler (Dürre)"), s=[FA, ("الصَّمَّانِ", "samman-ant", "propn")]),
  pn("فَالْمُتَثَلَّمِ", "mutathallam", PRE("fa", "الْمُتَثَلَّمِ"), ATF("الْحَزْنِ"), QA, Dn("اسْمُ مَوْضِعٍ", "a place-name", "yer adı"), s=[FA, ("الْمُتَثَلَّمِ", "mutathallam", "propn")])])

# ---- v. 5 ----
V(5, "May you be greeted, of all traces — one long forsaken, left empty and desolate since Umm al-Haytham went.",
  "Selâm sana, ey (bütün izler içinden) yurt izi! Üzerinden çok zaman geçmiş, Ümmü'l-Heysem'den sonra boşalıp ıssız kalmış iz.",
 [v("حُيِّيتَ", "hayya", TU_M("anta"), CL_IST,
     Sn("وَالْجُمْلَةُ خَبَرِيَّةٌ لَفْظًا إِنْشَائِيَّةٌ مَعْنًى: الْمُرَادُ مِنْهَا الدُّعَاءُ " + DUR, "the sentence is a report in form and a request in meaning: what is meant is a prayer (al-Durra)", "cümle lafzen haber, mânen inşâdır: maksat duadır (Dürre)", "khabar-fi-mana-al-insha"), g=["form-ii-verbs", "naqis-verbs"]),
  pp("مِنْ", "min", ZAID_MIN, Dn("كَذَا أَعْرَبَهُ الدُّرَّةُ؛ وَفَسَّرَهُ الزَّوْزَنِيُّ: حُيِّيتَ مِنْ جُمْلَةِ الْأَطْلَالِ، أَيْ خُصِّصْتَ بِالتَّحِيَّةِ مِنْ بَيْنِهَا", "so al-Durra parses it; al-Zawzanī glosses: «may you be greeted from among all traces» — singled out for the greeting", "Dürre böyle i'râb eder; Zevzenî ise «izler arasından selâmlanasın» diye açıklar: selâm, onların içinden sana tahsis edilmiştir")),
  n("طَلَلٍ", "talal", Fr("تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "a tamyiz, in nasb by a fatha that the vowel of the added jarr letter keeps from showing", "temyîz; zâid cer harfinin harekesi yüzünden zâhir olmayan takdîrî fetha ile mansûb", "tamyiz", "al-tamyiz-wa-ahkamuh")),
  v("تَقَادَمَ", "taqadama-ant", MADI, FAIL_BAD, CL_NAAT("طَلَلٍ"), g=["form-vi-verbs"]),
  n("عَهْدُهُ", "ahd", FL(), IDF("هُ"), Dn("أَيْ: قَدُمَ عَهْدُهُ بِأَهْلِهِ " + ZAW, "that is, it is long since its people were in it (al-Zawzanī)", "yani: halkıyla olan devri eskimiştir (Zevzenî)"), s=[("عَهْدُ", "ahd", "noun"), P("هُ")])],
 [v("أَقْوَى", "aqwa-empty-ant", MADI_A, HID("هُوَ", ("«طَلَلٍ»", "the trace", "yurt izi")), CL_NAAT("طَلَلٍ"), Dn("نَعْتٌ ثَانٍ، وَتَصْلُحُ لِلْحَالِيَّةِ " + DUR, "a second na't; it may also be a hal (al-Durra)", "ikinci na'ttır; hâl olması da mümkündür (Dürre)"), g=["form-iv-verbs"]),
  v("وَأَقْفَرَ", "aqfara-ant", PRE("wa", "أَقْفَرَ"), MADI, HID("هُوَ"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «أَقْوَى»", "the clause is conjoined to «أَقْوَى»", "cümle «أَقْوَى» cümlesine ma'tûftur"),
     Sn("وَالْإِقْوَاءُ وَالْإِقْفَارُ: الْخَلَاءُ، جَمَعَ بَيْنَهُمَا لِضَرْبٍ مِنَ التَّأْكِيدِ " + ZAW + " — فَهُوَ إِطْنَابٌ بِعَطْفِ اللَّفْظِ عَلَى مُرَادِفِهِ", "الْإِقْوَاء and الْإِقْفَار both mean being empty; he joins the two for a kind of emphasis (al-Zawzanī) — an iṭnāb, a word conjoined to its synonym", "الْإِقْوَاء ve الْإِقْفَار ikisi de «boşalmak»tır; bir tür te'kîd için ikisini bir araya getirmiştir (Zevzenî) — lafzın müterâdifine atfıyla yapılan bir itnâbdır", "ijaz-itnab-musawat", "asbab-al-itnab"), s=[WA, ("أَقْفَرَ", "aqfara-ant", "verb")], g=["form-iv-verbs"]),
  n("بَعْدَ", "bada", ZZ(), MDF, Dn("مُتَعَلِّقٌ بِأَحَدِ الْفِعْلَيْنِ قَبْلَهُ عَلَى التَّنَازُعِ " + DUR, "it hangs on one of the two verbs before it, which contend for it (al-Durra)", "tenâzu' yoluyla önceki iki fiilden birine müteallik (Dürre)", "tanazu")),
  n("أُمِّ", "umm", MI(), MDF),
  pn("الْهَيْثَمِ", "haytham-ant", MI(), QA, Dn("أُمُّ الْهَيْثَمِ: كُنْيَةُ عَبْلَةَ " + ZAW, "Umm al-Haytham is ʿAbla's kunya (al-Zawzanī)", "Ümmü'l-Heysem: Able'nin künyesi (Zevzenî)"))])

# ---- v. 6 ----
V(6, "She has settled in the land of those who roar, and so it has become hard for me to seek you, daughter of Makhram.",
  "O, kükreyenlerin (düşmanların) toprağına kondu; artık seni aramak bana güç oldu, ey Mahrem'in kızı.",
 [v("حَلَّتْ", "halla-settle", MADI_F, HID("هِيَ", ("عَبْلَةَ", "ʿAbla", "Able")), CL_IST, g=["doubled-verbs"]),
  n("بِأَرْضِ", "ard", JN("بِ", "أَرْضِ", sense=FI_SENSE), MDF, TA("حَلَّتْ"), s=[BI, ("أَرْضِ", "ard", "noun")]),
  n("الزَّائِرِينَ", "zair-roar-ant", MI("jP"), Dn("اسْمُ فَاعِلٍ مِنْ زَأَرَ الْأَسَدُ؛ وَالزَّائِرُونَ: الْأَعْدَاءُ " + ZAW, "the active participle of زَأَرَ «(the lion) roared»; «the roarers» are the enemies (al-Zawzanī)", "زَأَرَ («aslan kükredi») fiilinden ism-i fâil; «kükreyenler»: düşmanlar (Zevzenî)", "ism-fail"),
     Sn("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شَبَّهَ تَوَعُّدَهُمْ وَتَهَدُّدَهُمْ بِزَئِيرِ الْأَسَدِ " + ZAW + "، ثُمَّ اشْتُقَّ مِنَ الزَّئِيرِ «الزَّائِرُونَ»", "here is an istiʿāra taṣrīḥiyya tabaʿiyya: their threats and menaces are likened to a lion's roar (al-Zawzanī), and «the roarers» is derived from that roar", "burada istiâre-i tasrîhiyye-i tebeiyye vardır: tehdit ve gözdağları aslanın kükremesine benzetilmiş (Zevzenî), sonra «kükreme»den «kükreyenler» türetilmiştir", "istiara", "aqsam-al-istiara", "istiara-tabaiyya")),
  v("فَأَصْبَحَتْ", "asbaha", PRE("fa", "أَصْبَحَتْ"), Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى عَبْلَةَ", "a defective past verb built on fatha; the ta marks the feminine; its noun is the hidden «she» — ʿAbla", "fetha üzere mebnî nâkıs mâzî; tâ te'nîs içindir; ismi Able'ye dönen gizli zamir «o»", "kana-wa-akhawatuha", "form-iv-verbs"), s=[FA, ("أَصْبَحَتْ", "asbaha", "verb")])],
 [n("عَسِرًا", "asir-ant", RO("خَبَرُ «أَصْبَحَتْ»", "the predicate of «أَصْبَحَتْ»", "«أَصْبَحَتْ» fiilinin haberi", "n", "kana-wa-akhawatuha"), Dn("صِفَةٌ مُشَبَّهَةٌ رَفَعَتْ مَا بَعْدَهَا؛ وَجَوَّزَ التِّبْرِيزِيُّ رَفْعَهُ خَبَرًا مُقَدَّمًا وَ«طِلَابُكِ» مُبْتَدَأً مُؤَخَّرًا وَالْجُمْلَةُ خَبَرُ «أَصْبَحَتْ» " + DUR, "a sifa mushabbaha that raises what follows; al-Tibrīzī also allows it in raf', a fronted khabar with «طِلَابُكِ» its mubtada, the clause being the predicate of «أَصْبَحَتْ» (al-Durra)", "kendinden sonrakini ref eden sıfat-ı müşebbehe; Tebrîzî, öne alınmış haber olarak merfû okunmasını, «طِلَابُكِ»nin de sonraya bırakılmış mübtedâ, cümlenin «أَصْبَحَتْ»nin haberi olmasını câiz görür (Dürre)", "sifa-mushabbaha")),
  pp("عَلَيَّ", "ala", JP("عَلَى", "يَ"), TA("عَسِرًا"), s=[("عَلَيْ", "ala", "prep"), P("يَ")]),
  n("طِلَابُكِ", "tilab-ant", RO("فَاعِلٌ لِلصِّفَةِ الْمُشَبَّهَةِ «عَسِرًا»", "the doer of the sifa mushabbaha «عَسِرًا»", "«عَسِرًا» sıfat-ı müşebbehesinin fâili", "r", "fail"), IDF("كِ"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", "the masdar annexed to its object", "masdarın mef'ûlüne izâfeti", "masdar", "imal-al-masdar"),
     Sn("وَفِيهِ الْتِفَاتٌ مِنَ الْغَيْبَةِ فِي «حَلَّتْ» إِلَى الْخِطَابِ " + DUR + "؛ قَالَ الزَّوْزَنِيُّ: «وَأَضْرَبَ عَنِ الْخَبَرِ فِي الظَّاهِرِ إِلَى الْخِطَابِ، وَهُوَ شَائِعٌ فِي الْكَلَامِ»", "here is an iltifāt, from the third person of «حَلَّتْ» to the second (al-Durra); al-Zawzanī: «he turns from report, outwardly, to address — and that is common in speech»", "burada «حَلَّتْ»deki gaybetten hitaba iltifât vardır (Dürre); Zevzenî: «görünüşte haberden hitaba dönmüştür; bu, kelâmda yaygındır»", "iltifat"), s=[("طِلَابُ", "tilab-ant", "noun"), P("كِ")]),
  n("ابْنَةَ", "ibna-ant", MUNADA_M, Dn("حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ", "its vocative particle is dropped", "nidâ harfi hazfedilmiştir", "hadhf-wa-taqdir")),
  pn("مَخْرَمِ", "makhram-ant", MI(), QT, Dn("مَخْرَمٌ: اسْمُ رَجُلٍ مِنْ آبَائِهَا", "Makhram: a man's name, one of her forefathers", "Mahrem: onun atalarından bir adamın adı"))])

# ---- v. 7 ----
V(7, "I was made to love her by chance, while I kill her people — a hope, by your father's life, that is no place for hope.",
  "Kavmini öldürüp dururken ona tesadüfen gönül verdim; babanın hayatına yemin olsun ki bu, umulacak yeri olmayan bir umuttur.",
 [v("عُلِّقْتُهَا", "allaqa", TU_M("ana"), Dn("وَهُوَ الْمَفْعُولُ الْأَوَّلُ فِي الْأَصْلِ", "it was the first object", "aslında birinci mef'ûldür"), OBJ("هَا", ("مَفْعُولٌ بِهِ ثَانٍ", "the second object", "ikinci mef'ûlün bih")), CL_IST,
     Dn("التَّعْلِيقُ: التَّفْعِيلُ مِنَ الْعَلَقِ وَالْعَلَاقَةِ وَهُمَا الْعِشْقُ وَالْهَوَى " + ZAW, "التَّعْلِيق is Form II of الْعَلَق / الْعَلَاقَة, love and passion (al-Zawzanī)", "التَّعْلِيق: «aşk ve sevda» demek olan الْعَلَق / الْعَلَاقَة'tan tef'îl (Zevzenî)"),
     HD("الْتِفَاتٌ مِنَ الْخِطَابِ فِي «طِلَابُكِ» إِلَى الْغَيْبَةِ، وَالْمَعْنِيُّ وَاحِدٌ", "there is an iltifāt, from the second person of «طِلَابُكِ» back to the third — the one meant is the same", "«طِلَابُكِ»deki hitaptan gaybete iltifât vardır; kastedilen aynıdır", "iltifat"), s=[("عُلِّقْتُ", "allaqa", "verb"), P("هَا")], g=["form-ii-verbs", "mafulayn"]),
  n("عَرَضًا", "arad", MM(), Dn("عَلَى حَدِّ «قَعَدْتُ جُلُوسًا»، وَقِيلَ: تَمْيِيزٌ " + DUR + "؛ أَيْ: فَجْأَةً مِنْ غَيْرِ قَصْدٍ لَهُ " + ZAW, "after the manner of «قَعَدْتُ جُلُوسًا»; it is also read as a tamyiz (al-Durra); that is, suddenly, unsought (al-Zawzanī)", "«قَعَدْتُ جُلُوسًا» kabilinden; temyîz olduğu da söylenmiştir (Dürre); yani: ansızın, kasıtsız (Zevzenî)")),
  v("وَأَقْتُلُ", "qatala", PRE("wa-hal", "أَقْتُلُ"), MUDR(), HID("أَنَا"), CL_HAL("التَّاءِ فِي «عُلِّقْتُهَا»"),
     Dn("وَقِيلَ: هُوَ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ، أَيْ: وَأَنَا أَقْتُلُ، وَالْجُمْلَةُ الِاسْمِيَّةُ حَالٌ — وَهٰذَا لَا ضَرُورَةَ فِيهِ، لِأَنَّ الْمُضَارِعَ الْمُثْبَتَ لَا يَقْتَرِنُ بِوَاوِ الْحَالِ " + DUR, "it is also read as the khabar of an omitted mubtada, «while I kill», the nominal clause being the hal — and that reading needs no poetic licence, since a plain affirmative present does not take the waw of the hal (al-Durra)", "mahzûf mübtedânın haberi olduğu da söylenmiştir: «ben öldürürken»; isim cümlesi hâl olur — bu vecihte zarûret yoktur, çünkü müsbet muzâri hâl vâvı almaz (Dürre)", "hadhf-wa-taqdir"), s=[WA, ("أَقْتُلُ", "qatala", "verb")], g=["thulathi-mujarrad-babs"]),
  n("قَوْمَهَا", "qawm", MF(), IDF("هَا"), s=[("قَوْمَ", "qawm", "noun"), P("هَا")])],
 [n("زَعْمًا", "zam-ant", RO("مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ", "an absolute object of an omitted verb", "mahzûf bir fiilin mef'ûl-i mutlakı", "n", "maful-mutlaq", "hadhf-wa-taqdir"), Dn("وَالتَّقْدِيرُ: أَزْعُمُ زَعْمًا " + ZAW + "؛ وَالزَّعْمُ: الطَّمَعُ", "the full wording is «I hope a hope» (al-Zawzanī); الزَّعْم is hoping, coveting", "takdiri: «bir umut umuyorum» (Zevzenî); الزَّعْم: umma, tamah", "masdar")),
  n("لَعَمْرُ", "amr-qasam", Fr("اللَّامُ لَامُ الِابْتِدَاءِ، وَ«عَمْرُ» مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي", "the lam is the lam of beginning; «عَمْرُ» is a mubtada, in raf' by the damma, annexed; its khabar must be left out — «is my oath»", "lâm ibtidâ lâmıdır; «عَمْرُ» mübtedâ, damme ile merfû, muzâf; haberi vücûben mahzûftur, takdiri: «yeminimdir»", "mubtada-khabar", "idafa-definiteness", "huruf-al-qasam-fil-kafiya", "hadhf-wa-taqdir"),
     Dn("الْعَمْرُ وَالْعُمْرُ: الْحَيَاةُ وَالْبَقَاءُ، وَلَا يُسْتَعْمَلُ فِي الْقَسَمِ إِلَّا بِفَتْحِ الْعَيْنِ " + ZAW, "الْعَمْر and الْعُمْر: life, lasting; in an oath only the form with fatha is used (al-Zawzanī)", "الْعَمْر ve الْعُمْر: hayat, bekâ; kasemde yalnızca ayn'ın fethasıyla kullanılır (Zevzenî)"),
     Sn("وَالْجُمْلَةُ مُعْتَرِضَةٌ بَيْنَ الْمَوْصُوفِ «زَعْمًا» وَصِفَتِهِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ " + DUR + " — وَهُوَ الِاعْتِرَاضُ، وَنُكْتَتُهُ التَّوْكِيدُ بِالْقَسَمِ", "the clause stands as a parenthesis between «زَعْمًا» and its adjective and has no seat (al-Durra) — an iʿtirāḍ, whose point is the emphasis of an oath", "cümle, mevsûf «زَعْمًا» ile sıfatı arasında mu'tarızadır, i'râbdan mahalli yoktur (Dürre) — bu i'tirâzdır; nüktesi kasemle te'kîddir", "itirad", "jumla-mutarida"), s=[("لَ", "lam-ibtida", "part"), ("عَمْرُ", "amr-qasam", "noun")]),
  n("أَبِيكَ", "ab", MI("j5"), IDF("كَ"), s=[("أَبِي", "ab", "noun"), P("كَ")]),
  v("لَيْسَ", "laysa", LAYSA_, Fr("، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الزَّعْمِ", "; its noun is the hidden «it» — the hope", "; ismi الزَّعْم'e dönen gizli zamir «o»"), CL_NAAT("زَعْمًا", "n")),
  n("بِمَزْعَمِ", "mazam-ant", BI_ZAID("مَزْعَمِ"), QT, Dn("الْمَزْعَمُ: الْمَطْمَعُ، أَيْ: أَطْمَعُ فِي حُبِّكِ طَمَعًا لَا مَوْضِعَ لَهُ " + ZAW, "الْمَزْعَم: a thing to be hoped for — «I hope for your love with a hope that has no ground» (al-Zawzanī)", "الْمَزْعَم: umulacak şey — «sevgin için, yeri olmayan bir umut besliyorum» (Zevzenî)"), s=[BI, ("مَزْعَمِ", "mazam-ant", "noun")])])

# ---- v. 8 ----
V(8, "And truly you have come to hold in me — think nothing else — the place of one loved and honoured.",
  "And olsun ki sen bende — başka türlü sanma — sevilen ve ağırlanan kimsenin yerine kondun.",
 [pt("وَلَقَدْ", "qad", Fr("الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ وَالْمُقْسَمُ بِهِ مَحْذُوفٌ تَقْدِيرُهُ: وَاللهِ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ", "the waw is the particle of the oath, with what is sworn by left out — «by God»; the lam stands in the answer of the oath; قَدْ is a particle of certainty", "vâv kasem ve cer harfi, kendisiyle yemin edilen mahzûftur: «vallahi»; lâm kasemin cevabındadır; قَدْ tahkîk harfi", "huruf-al-qasam-fil-kafiya", "qad-harf", "hadhf-wa-taqdir"), s=[("وَ", "wa-qasam", "part"), ("لَ", "lam-qasam", "part"), ("قَدْ", "qad", "part")]),
  v("نَزَلْتِ", "nazala", TU("anti"), CL(0, "جَوَابُ الْقَسَمِ", "answers the oath", "kasemin cevabıdır"),
     HD("الْتِفَاتٌ مِنَ الْغَيْبَةِ فِي «عُلِّقْتُهَا» إِلَى الْخِطَابِ", "there is an iltifāt, from the third person of «عُلِّقْتُهَا» to the second", "«عُلِّقْتُهَا»daki gaybetten hitaba iltifât vardır", "iltifat"), g=["thulathi-mujarrad-babs"]),
  pt("فَلَا", "la-nahiya", Fr("الْفَاءُ حَرْفُ تَفْرِيعٍ، وَلَا نَاهِيَةٌ جَازِمَةٌ", "the fa branches the clause from the oath; لَا is the prohibiting particle, which puts in jazm", "fâ tefrî' harfi; لَا nehiy harfi, cezmeder", "la-nahiya", "al-nahy-wa-wujuhuh"), s=[FA, ("لَا", "la-nahiya", "part")]),
  v("تَظُنِّي", "zanna", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a present verb in jazm by the prohibiting لَا, its sign the dropping of the nun — one of the five verbs — and the ya of the woman addressed is its doer, in the seat of raf'", "nehiy لَا'sı ile meczûm muzâri, alâmeti nûnun hazfi — ef'âl-i hamsedendir — muhâtaba yâsı fâildir, mahallen merfû", "afal-khamsa", "nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "doubled-verbs"),
     Sn("وَجُمْلَةُ «فَلَا تَظُنِّي غَيْرَهُ» مُعْتَرِضَةٌ بَيْنَ «نَزَلْتِ» وَمُتَعَلِّقِهِ " + DUR + " — وَهُوَ الِاعْتِرَاضُ، وَنُكْتَتُهُ تَوْكِيدُ الْخَبَرِ: فَتَيَقَّنِي هٰذَا وَاعْلَمِيهِ قَطْعًا " + ZAW, "the clause «think nothing else» is a parenthesis between «نَزَلْتِ» and what hangs on it (al-Durra) — an iʿtirāḍ, whose point is to make the statement sure: «be certain of this, know it for a fact» (al-Zawzanī)", "«فَلَا تَظُنِّي غَيْرَهُ» cümlesi «نَزَلْتِ» ile müteallakı arasında mu'tarızadır (Dürre) — bu i'tirâzdır; nüktesi haberi pekiştirmektir: «buna kesin inan, bunu kat'î olarak bil» (Zevzenî)", "itirad", "jumla-mutarida")),
  n("غَيْرَهُ", "ghayr", MF1(), IDF("هُ"), Dn("وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ تَقْدِيرُهُ: وَاقِعًا " + DUR, "the second object is left out — «[to be] the case» (al-Durra)", "ikinci mef'ûl hazfedilmiştir, takdiri: «vâki» (Dürre)", "hadhf-al-maful"), s=[("غَيْرَ", "ghayr", "noun"), P("هُ")])],
 [pp("مِنِّي", "min", Fr("مِنْ حَرْفُ جَرٍّ، وَالنُّونُ الثَّانِيَةُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ", "مِنْ is a jarr letter, the second nun guards it, and the ya is in the seat of jarr", "مِنْ cer harfi, ikinci nûn vikâye içindir, yâ mahallen mecrûr", "huruf-jarr", "ya-al-mutakallim"), TA("نَزَلْتِ"), s=[("مِنِّ", "min", "prep"), P("ي")]),
  n("بِمَنْزِلَةِ", "manzila", JN("بِ", "مَنْزِلَةِ", sense=FI_SENSE), MDF, TA("نَزَلْتِ"), Dn("وَقِيلَ: بِمَحْذُوفٍ صِفَةٍ لِمَصْدَرٍ مَحْذُوفٍ، أَيْ: نُزُولًا مُشَابِهًا مَنْزِلَةَ الْمُحَبِّ " + DUR, "it is also hung on the omitted adjective of an omitted masdar — «a coming-down like the place of the loved one» (al-Durra)", "mahzûf bir masdarın mahzûf sıfatına müteallik olduğu da söylenmiştir: «sevilenin yerine benzer bir konuşla» (Dürre)"), s=[BI, ("مَنْزِلَةِ", "manzila", "noun")]),
  n("الْمُحَبِّ", "muhabb-ant", MI(), Dn("اسْمُ مَفْعُولٍ مِنْ أَحَبَّ عَلَى الْقِيَاسِ، وَالْأَكْثَرُ فِي كَلَامِهِمْ «مَحْبُوبٌ»؛ أَيْ: مَنْزِلَةَ مَنْ يُحَبُّ وَيُكْرَمُ " + ZAW, "the regular passive participle of أَحَبَّ — the Arabs more often say مَحْبُوب; that is, «the place of one who is loved and honoured» (al-Zawzanī)", "أَحَبَّ fiilinden kıyâsî ism-i mef'ûl — Arap sözünde daha çok «مَحْبُوب» kullanılır; yani: «sevilen ve ağırlanan kimsenin yeri» (Zevzenî)", "ism-maful")),
  n("الْمُكْرَمِ", "mukram", NAT("الْمُحَبِّ"), QA, Dn("اسْمُ مَفْعُولٍ مِنْ أَكْرَمَ", "the passive participle of أَكْرَمَ", "أَكْرَمَ fiilinden ism-i mef'ûl", "ism-maful"))])

# ==== VERSES ABOVE THIS LINE (in poem order) ====
# =====================================================================================================================
# The registers: new lexicon entries, new paradigms, fitted glosses, departures from the print, vowels for the scholar,
# and the figures of sound (claimed by the Talkhīṣ's own definition).
# A NEW key ends in «-ant» (the poet's own name apart) so that it cannot meet a key of another package being written
# beside this one; a key without the suffix is the shelf's, reused because the lemma is the same.
# =====================================================================================================================
def G(lemma, pos, en, tr, level=6, root=None, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
_sg1, _dv = _sg.sound1, _sg.derived
NEW_GLOSS, NEW_VERBS, TAILOR, DIV, FLAGS, BADI_HADD = {}, {}, {}, [], [], []

# ---- the khabar ----
NEW_GLOSS.update({
 "antara": G("عَنْتَرَة", "propn", "ʿAntara ibn Shaddād of ʿAbs — the pre-Islamic poet and horseman; a diptote (a name with the feminine ta); shortened to عَنْتَرَ when called", "Antere b. Şeddâd el-Absî — Câhiliye şairi ve süvarisi; gayr-i munsarif (lafzî te'nîsli alem); nidâda عَنْتَرَ diye kısaltılır"),
 "ajwad-ant": G("أَجْوَد", "noun", "most generous (elative of جُود); best, finest (elative of جَوْدَة)", "en cömert (جُود'dan ism-i tafdîl); en iyi, en güzel (جَوْدَة'den ism-i tafdîl)", 5, "ج و د"),
 "saabba-ant": G("سَابَّ", "verb", "to trade insults with, to revile one another (Form III, doubled; سَابَّ يُسَابُّ)", "karşılıklı sövüşmek, atışmak (müfâale, muzaaf; سَابَّ يُسَابُّ)", 6, "س ب ب", form="III"),
 "tarafada-ant": G("تَرَافَدَ", "verb", "to help one another, to give to one another (Form VI; from الرِّفْد «a gift»)", "yardımlaşmak, birbirine bağışta bulunmak (tefâul; الرِّفْد «bağış»tan)", 6, "ر ف د", form="VI"),
 "tuma-ant": G("طُعْمَة", "noun", "a meal given, an invitation to eat; a means of living", "verilen yemek, yemeğe davet; geçimlik", 6, "ط ع م"),
 "marfid-ant": G("مَرْفِد", "noun", "the place or occasion where help and gifts are given (noun of place from رَفَدَ يَرْفِدُ)", "yardım ve bağışın yapıldığı yer, yardımlaşma meclisi (رَفَدَ يَرْفِدُ'den ism-i mekân)", 6, "ر ف د"),
 "ghara-ant": G("غَارَة", "noun", "a raid, a mounted attack (pl. غَارَات)", "baskın, akın (ç. غَارَات)", 5, "غ و ر", "غَارَات"),
 "taswim-ant": G("تَسْوِيم", "noun", "marking oneself (or one's horse) with a sign to be known in battle (masdar of Form II سَوَّمَ)", "savaşta tanınmak için kendine (veya atına) nişan koymak (سَوَّمَ'nin masdarı)", 6, "س و م"),
 "mughir-ant": G("مُغِير", "noun", "raiding, a raider (ism fa'il of أَغَارَ)", "baskın yapan, akıncı (أَغَارَ'den ism-i fâil)", 5, "غ و ر"),
 "khutta-ant": G("خُطَّة", "noun", "an affair, a case, a matter to be decided (pl. خُطَط)", "iş, mesele, hükme bağlanacak dava (ç. خُطَط)", 6, "خ ط ط", "خُطَط"),
 "faysal-ant": G("فَيْصَل", "noun", "the decisive judgement that parts right from wrong; a judge who gives it", "hak ile bâtılı ayıran kesin hüküm; bu hükmü veren hakem", 6, "ف ص ل"),
 "faq-ant": G("فَقْع", "noun", "a soft white truffle, the poorest kind — a byword for lowliness (also فِقْع)", "yumuşak beyaz yer mantarı, mantarın en kötüsü — zillet için darbımesel (فِقْع da denir)", 6, "ف ق ع"),
 "qarqar-ant": G("قَرْقَر", "noun", "low, soft, level ground", "alçak, yumuşak düz arazi", 6, "ق ر ر"),
 "ihtadara-ant": G("اِحْتَضَرَ", "verb", "to be present at, to attend (Form VIII)", "bir yerde hazır bulunmak (iftiâl)", 6, "ح ض ر", form="VIII"),
 "affa-ant": G("عَفَّ", "verb", "to abstain, to hold back from what is unbecoming (doubled; عَفَّ يَعِفُّ; with عَنْ)", "iffetli davranmak, yakışmayan şeyden el çekmek (muzaaf; عَفَّ يَعِفُّ; عَنْ ile)", 5, "ع ف ف", form="I"),
 "samaa-ant": G("صَمْعَاء", "noun", "keen, cutting straight through (fem. of أَصْمَع; a diptote)", "keskin, kestirip atan (أَصْمَع'ın müennesi; gayr-i munsarif)", 6, "ص م ع"),
 "ghadara-ant": G("غَادَرَ", "verb", "to leave, to leave behind (Form III)", "bırakmak, geride bırakmak (müfâale)", 5, "غ د ر", form="III"),
 "mutaraddam-ant": G("مُتَرَدَّم", "noun", "a place to be patched or mended (noun of place from تَرَدَّمَ) — al-Zawzanī; or a tune to be hummed over", "yamanacak, onarılacak yer (تَرَدَّمَ'den ism-i mekân) — Zevzenî; yahut terennüm edilecek nağme", 6, "ر د م"),
 "mudhhaba-ant": G("مُذْهَبَة", "noun", "gilded (fem. ism maf'ul of أَذْهَبَ) — «the Gilded», a name for a Muʿallaqa", "yaldızlı (أَذْهَبَ'den müennes ism-i mef'ûl) — «el-Müzhebe», muallaka için kullanılan ad", 6, "ذ ه ب"),
})
NEW_VERBS.update({
 "saabba-ant": _sg.entry(_sg.B3 + " — مُضَاعَفٌ", _sg.W3, "مُسَابَّة / سِبَاب", "مُسَابّ", _sg.mazi14("سَابّ", "سَابَب"), _sg.mudari14("ُ", "سَابّ", "سَابِب"),
     ["سَابَّ", "سَابَّا", "سَابُّوا", "سَابِّي", "سَابَّا", "سَابِبْنَ"], "يُسَابَّ", "يُسَابَّ", "تُسَابَّ", note="مُضَاعَفٌ مِنَ الْمُفَاعَلَةِ: يُدْغَمُ الْمِثْلَانِ — سَابَّ يُسَابُّ، وَيُفَكُّ مَعَ ضَمِيرِ الرَّفْعِ الْمُتَحَرِّكِ: سَابَبْتُ."),
 "tarafada-ant": _dv(_sg.B6, _sg.W6, "َ", "تَرَافَد", "تَرَافَد", "تَرَافَد", "تَرَافُد", "مُتَرَافِد"),
 "ihtadara-ant": _dv(_sg.B8, _sg.W8, "َ", "اِحْتَضَر", "حْتَضِر", "اِحْتَضِر", "اِحْتِضَار", "مُحْتَضِر", "مُحْتَضَر", "اُحْتُضِرَ", "يُحْتَضَرُ"),
 "affa-ant": _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "عِفَّة / عَفَاف", "عَفّ / عَفِيف", _sg.mazi14("عَفّ", "عَفَف"), _sg.mudari14("َ", "عِفّ", "عْفِف"),
     ["عِفَّ", "عِفَّا", "عِفُّوا", "عِفِّي", "عِفَّا", "اِعْفِفْنَ"], "يَعِفَّ", "يَعِفَّ", "تَعِفَّ", note="لَازِمٌ، وَالْوَصْفُ مِنْهُ عَفٌّ وَعَفِيفٌ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ (لَمْ يَعِفَّ)، وَيَجُوزُ الْفَكُّ: لَمْ يَعْفِفْ."),
 "ghadara-ant": _dv(_sg.B3, _sg.W3, "ُ", "غَادَر", "غَادِر", "غَادِر", "مُغَادَرَة", "مُغَادِر", "مُغَادَر", "غُودِرَ", "يُغَادَرُ"),
})
TAILOR.update({
 "bas": ("might, stress of battle; harm, distress", "güç, savaşın şiddeti; zarar, sıkıntı"),
 "awfa": ("to give in full, to hand over complete; to keep (a covenant) in full (Form IV)", "tam ve eksiksiz vermek; (ahdi) tam yerine getirmek (if'âl)"),
 "labs": ("confusion, a tangled and doubtful matter", "karışıklık, içinden çıkılmaz iş"),
 "fasala": ("to part, to separate; to decide, to settle (a case)", "ayırmak; (davayı) hükme bağlamak"),
 "masala": ("a question, an issue; asking, begging", "soru, mesele; isteme, dilenme"),
 "khayl": ("horses (a collective); horsemen", "atlar (ism-i cem'); süvariler"),
 "dhakara": ("to mention, to speak of", "anmak, söz etmek"),
 "hadara": ("to be present at, to attend", "hazır bulunmak, katılmak"),
 "daa": ("to call, to call out; to pray", "çağırmak, seslenmek; dua etmek"),
})
FLAGS += [
 (0, "«مَرْفِدَ النَّاسِ» وَ«لَيُدْعَوْنَ» وَ«وَأُوفِي» وَ«أَوَّلُ مَا قَالَ قَصِيدَةً» فِي الْخَبَرِ", "«مَرْفِدَ النَّاسِ», «لَيُدْعَوْنَ», «وَأُوفِي» and «أَوَّلُ مَا قَالَ قَصِيدَةً» in the khabar", "haberdeki «مَرْفِدَ النَّاسِ», «لَيُدْعَوْنَ», «وَأُوفِي» ve «أَوَّلُ مَا قَالَ قَصِيدَةً»"),
]

# ---- vv. 1–8 ----
NEW_GLOSS.update({
 "abla-ant": G("عَبْلَة", "propn", "ʿAbla — the woman ʿAntara loves, his cousin; a diptote (a woman's name)", "Able — Antere'nin sevdiği kadın, amcasının kızı; gayr-i munsarif (müennes alem)"),
 "waama-ant": G("وَعَمَ", "verb", "to be in ease and comfort — heard in the greeting عِمْ صَبَاحًا «a good morning to you» (وَعَمَ يَعِمُ, the same as نَعِمَ)", "refah ve rahat içinde olmak — عِمْ صَبَاحًا «sabahın hayrolsun» selâmında kullanılır (وَعَمَ يَعِمُ; نَعِمَ ile aynı)", 6, "و ع م", form="I"),
 "fadan-ant": G("فَدَن", "noun", "a castle, a lofty building (pl. أَفْدَان)", "köşk, yüksek yapı (ç. أَفْدَان)", 6, "ف د ن", "أَفْدَان"),
 "mutalawwim-ant": G("مُتَلَوِّم", "noun", "one who lingers, who waits about (ism fa'il of Form V تَلَوَّمَ)", "oyalanan, bekleyip duran (تَلَوَّمَ'den ism-i fâil)", 6, "ل و م"),
 "samman-ant": G("الصَّمَّان", "propn", "al-Ṣammān — a tract of hard high ground in the land of Tamīm, named in the opening of the ode", "es-Sammân — Temîm yurdunda sert ve yüksek bir arazi; kasidenin başında anılır"),
 "taqadama-ant": G("تَقَادَمَ", "verb", "to grow old, to lie far back in time (Form VI)", "eskimek, üzerinden çok zaman geçmek (tefâul)", 5, "ق د م", form="VI"),
 "aqwa-empty-ant": G("أَقْوَى", "verb", "to become empty of its people, to lie waste (Form IV; أَقْوَى يُقْوِي)", "halkından boşalmak, ıssız kalmak (if'âl; أَقْوَى يُقْوِي)", 6, "ق و ي", form="IV"),
 "aqfara-ant": G("أَقْفَرَ", "verb", "to become desolate, a waste with no one in it (Form IV)", "ıssızlaşmak, kimsesiz çöl hâline gelmek (if'âl)", 6, "ق ف ر", form="IV"),
 "haytham-ant": G("الْهَيْثَم", "propn", "al-Haytham — in Umm al-Haytham, ʿAbla's kunya", "Heysem — Able'nin künyesi «Ümmü'l-Heysem»de"),
 "zair-roar-ant": G("زَائِر", "noun", "roaring, a roarer (ism fa'il of زَأَرَ, of a lion) — الزَّائِرُونَ: the enemies who threaten", "kükreyen (زَأَرَ'den ism-i fâil; aslan için) — الزَّائِرُونَ: tehdit savuran düşmanlar", 6, "ز أ ر"),
 "asir-ant": G("عَسِر", "noun", "hard, difficult (a sifa mushabbaha of عَسِرَ)", "güç, zor (عَسِرَ'den sıfat-ı müşebbehe)", 5, "ع س ر"),
 "tilab-ant": G("طِلَاب", "noun", "seeking, going after (a masdar of طَالَبَ / طَلَبَ)", "arama, peşine düşme (طَالَبَ / طَلَبَ'nin masdarı)", 6, "ط ل ب"),
 "ibna-ant": G("اِبْنَة", "noun", "a daughter (the feminine of اِبْن)", "kız evlât (اِبْن'in müennesi)", 4, "ب ن و"),
 "makhram-ant": G("مَخْرَم", "propn", "Makhram — a man's name; ʿAbla is called «daughter of Makhram»", "Mahrem — bir adam adı; Able «Mahrem'in kızı» diye anılır"),
 "zam-ant": G("زَعْم", "noun", "hoping for, coveting (al-Zawzanī: الطَّمَع); a claim", "umma, tamah (Zevzenî: الطَّمَع); iddia", 6, "ز ع م"),
 "mazam-ant": G("مَزْعَم", "noun", "a thing to be hoped for, a ground for hope (al-Zawzanī: الْمَطْمَع)", "umulacak şey, umut yeri (Zevzenî: الْمَطْمَع)", 6, "ز ع م"),
 "muhabb-ant": G("مُحَبّ", "noun", "loved, beloved — the regular ism maf'ul of أَحَبَّ, rarer in use than مَحْبُوب", "sevilen — أَحَبَّ'den kıyâsî ism-i mef'ûl; kullanımda مَحْبُوب'dan nadirdir", 6, "ح ب ب"),
})
NEW_VERBS.update({
 "waama-ant": _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مِثَالٌ وَاوِيٌّ", "فَعَلَ يَفْعِلُ", "وَعْم", "وَاعِم", _sg.mazi14("وَعَم"), _sg.mudari14("َ", "عِم"), _sg.amr_attach("عِم"),
     "يَعِمَ", "يَعِمْ", "تَعِمْ", note="مِثَالٌ وَاوِيٌّ: تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ وَالْأَمْرِ — يَعِمُ، عِمْ؛ وَلَا يَكَادُ يُسْتَعْمَلُ إِلَّا فِي التَّحِيَّةِ: عِمْ صَبَاحًا، عِمِي صَبَاحًا."),
 "taqadama-ant": _dv(_sg.B6, _sg.W6, "َ", "تَقَادَم", "تَقَادَم", "تَقَادَم", "تَقَادُم", "مُتَقَادِم"),
 "aqwa-empty-ant": _sg.derived_naqis(_sg.B4 + " — لَفِيفٌ مَقْرُونٌ", _sg.W4, "ُ", "أَقْوَ", "قْو", "i", "أَقْو", "إِقْوَاء", "مُقْوٍ", note="لَفِيفٌ مَقْرُونٌ مِنَ الْإِفْعَالِ: أَقْوَى يُقْوِي — لَمْ يُقْوِ، بِحَذْفِ الْيَاءِ."),
 "aqfara-ant": _dv(_sg.B4, _sg.W4, "ُ", "أَقْفَر", "قْفِر", "أَقْفِر", "إِقْفَار", "مُقْفِر"),
})
TAILOR.update({
 "jiwa": ("valleys, wide low grounds (pl. of جَوّ) — in this ode al-Jiwāʾ is a particular place", "vadiler, geniş alçak araziler (جَوّ'in cem'i) — bu kasidede Civâ belirli bir yerin adıdır"),
 "hazn": ("hard, rugged ground (pl. حُزُون) — in this ode al-Ḥazn is a place", "sert, engebeli arazi (ç. حُزُون) — bu kasidede Hazn bir yer adıdır"),
 "mutathallam": ("al-Mutathallam — a place named in the openings of Zuhayr's ode and of ʿAntara's", "Mütesellem — Züheyr'in ve Antere'nin kasidelerinin başında anılan bir yer"),
 "allaqa": ("to hang a thing on something; passive عُلِّقَ فُلَانَةَ: he was made to love her (Form II)", "bir şeyi bir yere asmak; meçhulü عُلِّقَ فُلَانَةَ: ona gönül verdi (tef'îl)"),
 "arad": ("what comes by chance, unsought — عَرَضًا: by chance; (in kalām) an accident, what subsists in another", "tesadüfen gelen, kastedilmeyen şey — عَرَضًا: tesadüfen; (kelâmda) araz"),
 "qada-verb": ("to carry out, to fulfil (a need); to decree; to judge", "yerine getirmek, (ihtiyacı) gidermek; hükmetmek"),
 "halla-settle": ("to alight, to settle in a place (حَلَّ يَحُلُّ)", "konmak, bir yere yerleşmek (حَلَّ يَحُلُّ)"),
 "hayya": ("to greet, to wish long life to (Form II, naqis)", "selâmlamak, hayat dilemek (tef'îl, nâkıs)"),
 "tawahhum": ("doubt, conjecture; fancying (masdar of Form V تَوَهَّمَ)", "şüphe, tahmin; vehmetme (تَوَهَّمَ'nin masdarı)"),
 "waqafa": ("to stop, to stand; to bring to a halt", "durmak; durdurmak"),
})
DIV += [
 (4, "الْبَيْتُ ٤ «فَالصَّمَانِ» ← «فَالصَّمَّانِ» بِتَشْدِيدِ الْمِيمِ، وَالشَّاهِدُ الْوَزْنُ وَاسْمُ الْمَوْضِعِ", "v. 4 «فَالصَّمَانِ» → «فَالصَّمَّانِ», with shadda on the mīm — witness: the metre, and the place's name", "4. beyit «فَالصَّمَانِ» → «فَالصَّمَّانِ», mîm'in şeddesiyle — şâhit: vezin ve yerin adı"),
 (6, "الْبَيْتُ ٦ «طِلَابُكَ» ← «طِلَابُكِ» بِكَسْرِ الْكَافِ، وَالشَّاهِدُ النِّدَاءُ بَعْدَهُ «ابْنَةَ مَخْرَمِ» وَشَرْحُ الزَّوْزَنِيِّ وَإِعْرَابُ الدُّرَّةِ", "v. 6 «طِلَابُكَ» → «طِلَابُكِ», with kasra on the kāf — witness: the vocative after it, «daughter of Makhram», al-Zawzanī's commentary and al-Durra's iʿrāb", "6. beyit «طِلَابُكَ» → «طِلَابُكِ», kâf'ın kesresiyle — şâhit: ardındaki nidâ «ابْنَةَ مَخْرَمِ», Zevzenî'nin şerhi ve Dürre'nin i'râbı"),
 (8, "الْبَيْتُ ٨ «بِمَنْزِلَةَ الْمُحِبِّ» ← «بِمَنْزِلَةِ الْمُحَبِّ» بِجَرِّ التَّاءِ وَفَتْحِ الْحَاءِ اسْمَ مَفْعُولٍ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ (مَنْزِلَةَ مَنْ يُحَبُّ وَيُكْرَمُ) وَإِعْرَابُ الدُّرَّةِ", "v. 8 «بِمَنْزِلَةَ الْمُحِبِّ» → «بِمَنْزِلَةِ الْمُحَبِّ», the tāʾ in jarr and the ḥāʾ with fatha, a passive participle — witness: al-Zawzanī's own gloss («the place of one who is loved and honoured») and al-Durra's iʿrāb", "8. beyit «بِمَنْزِلَةَ الْمُحِبِّ» → «بِمَنْزِلَةِ الْمُحَبِّ», tâ'nın cerri ve hâ'nın fethasıyla, ism-i mef'ûl olarak — şâhit: Zevzenî'nin kendi şerhi («sevilen ve ağırlanan kimsenin yeri») ve Dürre'nin i'râbı"),
]
FLAGS += [
 (6, "رَاءُ «مَخْرَمِ» (ب ٦)", "the rāʾ of «مَخْرَمِ» (v. 6)", "«مَخْرَمِ»in râ'sı (b. 6)"),
]
BADI_HADD += [
 (7, "زَعْمًا", "زَعْمًا", "بِمَزْعَمِ", "مَزْعَمِ", "isht", True),
 (8, "نَزَلْتِ", "نَزَلْتِ", "بِمَنْزِلَةِ", "مَنْزِلَةِ", "isht", False),
]

# >>> NEW REGISTERS ABOVE THIS LINE <<<
# =====================================================================================================================
# THE FIGURES OF SOUND — neither commentator names one (they comment on meaning and iʿrāb, not on badīʿ). Each is claimed
# by the Talkhīṣ's own DEFINITION, and its line says so («عَلَى حَدِّ التَّلْخِيصِ»):
#   mulḥaq bil-jinās  — «وَيُلْحَقُ بِالْجِنَاسِ شَيْئَانِ: أَحَدُهُمَا أَنْ يَجْمَعَ اللَّفْظَيْنِ الِاشْتِقَاقُ» (shelf Talkhīṣ ch. 69, s17)
#   radd al-ʿajuz     — «وَفِي النَّظْمِ أَنْ يَكُونَ أَحَدُهُمَا فِي آخِرِ الْبَيْتِ وَالْآخَرُ فِي صَدْرِ الْمِصْرَاعِ الْأَوَّلِ أَوْ حَشْوِهِ أَوْ آخِرِهِ أَوْ صَدْرِ
#                        الثَّانِي», the pair being «الْمُكَرَّرَيْنِ أَوِ الْمُتَجَانِسَيْنِ أَوِ الْمُلْحَقَيْنِ بِهِمَا» (ch. 70, s6 and s1)
# The SEAT of a radd is not typed in: it is computed from the two tokens' places and the hemistich mark, and the table
# is asserted against it both ways — no radd is claimed off its seats, and none that sits on a seat is passed over.
# BADI_HADD rows: (verse, first word's token, how it is shown, second word's token, how it is shown, kind, radd?)
#   kind: "isht" = joined by derivation; "takrar" = the same word repeated (it counts only as a radd al-ʿajuz)
# =====================================================================================================================
_SEAT = {"sadr1": ("صَدْرِ الْمِصْرَاعِ الْأَوَّلِ", "at the head of the first hemistich", "ilk mısraın başında"),
         "hashw1": ("حَشْوِ الْمِصْرَاعِ الْأَوَّلِ", "inside the first hemistich", "ilk mısraın içinde"),
         "akhir1": ("آخِرِ الْمِصْرَاعِ الْأَوَّلِ", "at the end of the first hemistich", "ilk mısraın sonunda"),
         "sadr2": ("صَدْرِ الْمِصْرَاعِ الثَّانِي", "at the head of the second hemistich", "ikinci mısraın başında")}
def _tok_at(num, surface, nth=0):
    toks = VERSE[num]["tokens"]; f = N(surface)
    hit = [i for i, t in enumerate(toks) if t["surface"]["full"] == f]
    assert len(hit) > nth, (num, surface, hit)
    return hit[nth]
def _radd_seat(num, ia, ib):
    """the Talkhīṣ's four seats for the partner of the verse-final word; None if the pair is off them"""
    toks = VERSE[num]["tokens"]; hem = [i for i, t in enumerate(toks) if t.get("punctAfter") == "•"]
    assert len(hem) == 1, num
    h = hem[0]
    if ib != len(toks) - 1: return None
    return "sadr1" if ia == 0 else "hashw1" if ia < h else "akhir1" if ia == h else "sadr2" if ia == h + 1 else None
def _add(t, ar, en, tr, tags):
    i = t["irab"]
    assert all(i[k].endswith(".") for k in ("ar", "en", "tr")), i
    i["ar"] += N(ar) + "."; i["en"] += en + "."; i["tr"] += tr + "."
    t["grammar"] = t.get("grammar", []) + [g for g in tags if g not in t.get("grammar", [])]
_second = {}
for _row in BADI_HADD:
    _n, _a, _ad, _b, _bd, _kind, _radd = _row[:7]
    if _n not in VERSE: continue
    _ia, _ib = _tok_at(_n, _a), _tok_at(_n, _b, 1 if _a == _b else 0)
    assert _ia < _ib, (_n, _a, _b)
    _seat = _radd_seat(_n, _ia, _ib)
    assert (_seat is not None) == _radd, ("radd al-ʿajuz: the table and the seats disagree", _n, _a, _b, _seat)
    if _kind == "isht":
        _ar = " وَبَيْنَهُ وَبَيْنَ «" + _bd + "» — عَلَى حَدِّ التَّلْخِيصِ — مُلْحَقٌ بِالْجِنَاسِ: يَجْمَعُ اللَّفْظَيْنِ الِاشْتِقَاقُ"
        _en = " By the Talkhīṣ's definition it is «attached to the jinas» with " + _bd + ": derivation joins the two words"
        _tr = " Telhîs'in tarifine göre «" + _bd + "» ile arasında cinâsa mülhak olan iştikâk vardır: iki lafzı iştikâk birleştirir"
        _tags = ["mulhaq-bil-jinas"]
        if _radd:
            _s = _SEAT[_seat]
            _ar += "؛ وَهُمَا — عَلَى حَدِّهِ — مِنْ رَدِّ الْعَجُزِ عَلَى الصَّدْرِ: أَحَدُهُمَا فِي " + _s[0] + " وَالْآخَرُ فِي آخِرِ الْبَيْتِ"
            _en += "; and by its definition the two make a radd al-'ajuz 'ala al-sadr: one stands " + _s[1] + ", the other at the end of the verse"
            _tr += "; yine onun tarifine göre ikisi reddü'l-acüz ale's-sadr oluşturur: biri " + _s[2] + ", diğeri beytin sonundadır"
            _tags = _tags + ["radd-al-ajuz"]
    else:
        assert _kind == "takrar" and _radd, _row
        _s = _SEAT[_seat]
        _ar = " وَبَيْنَهُ وَبَيْنَ «" + _bd + "» فِي آخِرِ الْبَيْتِ — عَلَى حَدِّ التَّلْخِيصِ — رَدُّ الْعَجُزِ عَلَى الصَّدْرِ: اللَّفْظَانِ مُكَرَّرَانِ، أَحَدُهُمَا فِي " + _s[0] + " وَالْآخَرُ فِي آخِرِ الْبَيْتِ"
        _en = " By the Talkhīṣ's definition it makes with the " + _bd + " that ends the verse a radd al-'ajuz 'ala al-sadr: the word is repeated, once " + _s[1] + " and once at the end of the verse"
        _tr = " Telhîs'in tarifine göre beytin sonundaki «" + _bd + "» ile arasında reddü'l-acüz ale's-sadr vardır: lafız tekrar edilmiştir; biri " + _s[2] + ", diğeri beytin sonundadır"
        _tags = ["radd-al-ajuz"]
    _add(VERSE[_n]["tokens"][_ia], _ar, _en, _tr, _tags)
    _second.setdefault((_n, _ib), []).append((_ad, _tags))
for (_n, _ib), _L in _second.items():
    _As = [a for a, _ in _L]; _tags = [g for _, tg in _L for g in tg]
    _add(VERSE[_n]["tokens"][_ib],
         " وَهُوَ — عَلَى حَدِّ التَّلْخِيصِ — الطَّرَفُ الثَّانِي لِمَا ذُكِرَ عِنْدَ " + " وَ".join("«" + a + "»" for a in _As) + " مِنَ الْبَدِيعِ اللَّفْظِيِّ",
         " By the Talkhīṣ's definition it is the second term of the figure of sound noted at " + " and ".join(_As),
         " Telhîs'in tarifine göre, " + " ve ".join("«" + a + "»" for a in _As) + (" kelimesinde" if len(_As) == 1 else " kelimelerinde") + " anılan lafzî bedîin ikinci ucudur", _tags)

# =====================================================================================================================
# The package: chapters, lexicon, paradigms, manifest
# =====================================================================================================================
AR_DIG = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
def ar_num(x): return str(x).translate(AR_DIG)
TOTAL = 75   # the poem's verses in al-Zawzanī's count
PLAN = [  # (first verse, last verse, the chapter's theme) — every verse of the poem, in al-Zawzanī's order, none skipped
 (1, 8, ("دَارُ عَبْلَةَ بِالْجِوَاءِ", "ʿAbla's dwelling at al-Jiwāʾ", "Civâ'da Able'nin yurdu")),
 (9, 15, ("الرَّحِيلُ، وَثَغْرُ عَبْلَةَ", "The departure, and ʿAbla's mouth", "Göç ve Able'nin ağzı")),
 (16, 21, ("الرَّوْضَةُ وَذُبَابُهَا، وَسَرْجُ الْفَارِسِ", "The meadow and its fly; the horseman's saddle", "Çayır ve sineği; süvarinin eyeri")),
 (22, 27, ("النَّاقَةُ وَالظَّلِيمُ", "The she-camel and the ostrich", "Dişi deve ve erkek devekuşu")),
 (28, 33, ("النَّاقَةُ: سَيْرُهَا وَعَرَقُهَا", "The she-camel: her pace and her sweat", "Dişi deve: yürüyüşü ve teri")),
 (34, 40, ("أَخْلَاقُ الْفَارِسِ، وَالْخَمْرُ", "The horseman's character, and the wine", "Süvarinin ahlâkı ve şarap")),
 (41, 46, ("هَلَّا سَأَلْتِ الْخَيْلَ", "«Why did you not ask the horsemen?»", "«Süvarilere sorsaydın ya!»")),
 (47, 52, ("الْمُدَجَّجُ، وَحَامِي الْحَقِيقَةِ", "The man in full armour, and the defender of his own", "Tepeden tırnağa silahlı adam ve hakikatini koruyan yiğit")),
 (53, 60, ("مَصْرَعُ الْبَطَلِ، وَالشَّاةُ", "The champion's fall, and the «ewe»", "Kahramanın düşüşü ve «koyun»")),
 (61, 68, ("وَصَاةُ الْعَمِّ، وَالْأَدْهَمُ فِي الْحَوْمَةِ", "The uncle's charge, and the black horse in the thick of the fight", "Amcanın vasiyeti ve savaşın ortasında yağız at")),
 (69, 75, ("شَكْوَى الْفَرَسِ، وَابْنَا ضَمْضَمٍ", "The horse's complaint, and the two sons of Ḍamḍam", "Atın şikâyeti ve Damdam'ın iki oğlu")),
]
assert [a for a, b, t in PLAN] == [1] + [b + 1 for a, b, t in PLAN[:-1]] and PLAN[-1][1] == TOTAL and all(6 <= b - a + 1 <= 8 for a, b, t in PLAN)
# only what is finished is published: the chapters whose verses are all authored, contiguously from verse 1
DONE = 0
while DONE + 1 in VERSE: DONE += 1
READY = [(a, b, t) for a, b, t in PLAN if b <= DONE]
DONE_TO = READY[-1][1] if READY else 0
CHAPS = [S1] + [[{"id": "s%d" % (i + 1), **VERSE[num]} for i, num in enumerate(range(a, b + 1))] for a, b, t in READY]
VNUMS = [(a, b) for a, b, t in READY]
TITLES = [{"ar": "خَبَرُ عَنْتَرَةَ", "en": "ʿAntara's Story", "tr": "Antere'nin Haberi"}] + [{"ar": t[0], "en": t[1], "tr": t[2]} for a, b, t in READY]
ALL_AUTHORED = [S1] + [[VERSE[num]] for num in sorted(VERSE)]
WHOLE = DONE_TO == TOTAL
for S in ALL_AUTHORED:
    for s in S:
        hem = [t for t in s["tokens"] if t.get("punctAfter") == "•"]
        assert len(hem) == (0 if S is S1 else 1), s["translation"]["en"]
        for t in s["tokens"]:
            t["grammar"] = list(dict.fromkeys(t.get("grammar", [])))
            if not t["grammar"]: del t["grammar"]
_GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
_bad = sorted({g for S in ALL_AUTHORED for s in S for t in s["tokens"] for g in t.get("grammar", []) if g not in _GR})
assert not _bad, _bad
# a segment never opens with a bare vowel mark
import re as _re
for S in ALL_AUTHORED:
    for s in S:
        for t in s["tokens"]:
            for sg2 in t.get("segments", []):
                sg2["form"] = _re.sub("^[ً-ْ]+", "", sg2["form"])

# ---- the lexicon: every shelf key by lemma identity; the entries in NEW_GLOSS are new ---------------------------------
PREF = ["muallaqat-zuhayr", "muallaqat-imri-al-qays", "talkhis-al-miftah", "al-kafiya", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "izhar-al-asrar", "marah-al-arwah",
        "tasrif-al-izzi", "sibawayh-fi-al-basra", "ayn-jalut", "bina-baghdad", "wasiyyat-abi-yusuf-l5", "shudhur-al-dhahab"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
# where the shelf holds one key in several senses, take the entry this text uses
FORCE = {}
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k, lemma):
    for p in PREF:
        if k in _M[p] and _G[p].get(k, {}).get("lemma") == lemma: return _M[p][k]
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None
# a key is a global claim: a NEW key must not name anything else on the shelf, nor in a sibling's staged package
_STAGED = {}
for d in OUT_ROOT.iterdir() if OUT_ROOT.exists() else []:
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
_lid = lambda x: "".join(c for c in unicodedata.normalize("NFD", x or "") if not unicodedata.combining(c))
for k, e in NEW_GLOSS.items():
    # a sister package (on the shelf or staged) may hold the key with the SAME word — then the script still re-runs
    hit = [p for p in PREF if k in _G[p] and _lid(_G[p][k].get("lemma")) != _lid(e["lemma"])]
    assert not hit, ("a NEW key names another word on the shelf", k, hit)
    assert k == "antara" or k.endswith("-ant"), ("a NEW key carries the suffix", k)
    for p, g in _STAGED.items():
        if k in g: assert _lid(g[k].get("lemma")) == _lid(e["lemma"]), ("staged clash", k, p, g[k].get("lemma"))
assert set(NEW_VERBS) == {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}, set(NEW_VERBS) ^ {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}

def _keys(chs):
    out = set()
    for S in chs:
        for s in S:
            for t in s["tokens"]:
                out.add(t["lex"])
                for sg2 in t.get("segments", []): out.add(sg2["lex"])
                if t.get("phrase"): out.add(t["phrase"]["lex"])
    return out
used_all, used = _keys(ALL_AUTHORED), _keys(CHAPS)
missing = sorted(k for k in used_all if not (NEW_GLOSS.get(k) or find_gloss(k)))
assert not missing, ("keys with no entry", missing)
unused_new = sorted(set(NEW_GLOSS) - used_all)
assert not unused_new, ("NEW entries no token uses", unused_new)
assert not sorted(set(TAILOR) - used_all), ("TAILOR rows no token uses", sorted(set(TAILOR) - used_all))
assert not [k for k in TAILOR if k in NEW_GLOSS], "TAILOR is for shelf keys"
GLOSS = {}
for k in sorted(used):
    e = json.loads(json.dumps(NEW_GLOSS.get(k) or find_gloss(k)))
    if k in TAILOR: e["gloss"] = {"en": TAILOR[k][0], "tr": TAILOR[k][1]}
    GLOSS[k] = e
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    vb = NEW_VERBS.get(k) or find_verb(k, e["lemma"])
    if vb: MORPH["verbs"][k] = vb
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, ("verbs with no paradigm", no_par)

# ---- the attribution, BUILT from what is published -------------------------------------------------------------------
_div = sorted(d for d in DIV if d[0] <= DONE_TO)
_flg = sorted(f for f in FLAGS if f[0] <= DONE_TO)
_ch_ar = "؛ ".join("الْفَصْلُ %s: %s–%s" % (ar_num(i + 2), ar_num(a), ar_num(b)) for i, (a, b) in enumerate(VNUMS))
_ch_en = "; ".join("chapter %d: vv. %d–%d" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_ch_tr = "; ".join("%d. bölüm: %d–%d. beyitler" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
if WHOLE:
    _scope = ("وَالْفُصُولُ بَعْدَهُ مُعَلَّقَتُهُ كَامِلَةً — خَمْسَةٌ وَسَبْعُونَ بَيْتًا لَمْ يُتْرَكْ مِنْهَا بَيْتٌ وَلَمْ يُقَدَّمْ وَلَمْ يُؤَخَّرْ",
              "The chapters after it are his Muʿallaqa WHOLE — seventy-five verses, none left out and none moved",
              "Sonraki bölümler onun muallakasının TAMAMIDIR — yetmiş beş beyit; hiçbiri atlanmamış, hiçbirinin yeri değiştirilmemiştir")
    _rest = ("", "", "")
else:
    _scope = ("وَالْفُصُولُ بَعْدَهُ الْأَبْيَاتُ %s–%s مِنْ مُعَلَّقَتِهِ مُتَتَالِيَةً لَمْ يُتْرَكْ مِنْ بَيْنِهَا بَيْتٌ" % (ar_num(1), ar_num(DONE_TO)),
              "The chapters after it are vv. 1–%d of his Muʿallaqa, consecutive, with no verse dropped from among them" % DONE_TO,
              "Sonraki bölümler onun muallakasının 1–%d. beyitleridir; ardışıktır, aralarından beyit atlanmamıştır" % DONE_TO)
    _rest = (" وَالْقَصِيدَةُ فِي رِوَايَتِهِ خَمْسَةٌ وَسَبْعُونَ بَيْتًا، وَبَقِيَّتُهَا (%s–%s) تُلْحَقُ عَلَى هٰذَا النَّسَقِ." % (ar_num(DONE_TO + 1), ar_num(TOTAL)),
             " In his recension the ode has seventy-five verses; the rest (vv. %d–%d) is to follow in the same manner." % (DONE_TO + 1, TOTAL),
             " Onun rivayetinde kaside yetmiş beş beyittir; kalanı (%d–%d. beyitler) aynı usulle eklenecektir." % (DONE_TO + 1, TOTAL))
_div_ar = "؛ ".join("(%s) " % ar_num(i + 1) + d[1] for i, d in enumerate(_div))
_div_en = "; ".join("(%d) " % (i + 1) + d[2] for i, d in enumerate(_div))
_div_tr = "; ".join("(%d) " % (i + 1) + d[3] for i, d in enumerate(_div))
ATTR_AR = ("نَصٌّ مَنْقُولٌ بِلَفْظِهِ. الْفَصْلُ الْأَوَّلُ خَبَرُ عَنْتَرَةَ بْنِ شَدَّادٍ الْعَبْسِيِّ مِنْ «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةِ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ٢٣٧٨٥)، ج ١ ص ٢٤٤–٢٤٥، الْفِقْرَةُ ٤١٩ بِتَمَامِهَا: قِطْعَةٌ مُتَّصِلَةٌ وَاحِدَةٌ لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ، وَتُرِكَ رَقْمُ الْفِقْرَةِ وَأَرْقَامُ حَوَاشِي الْمُحَقِّقِ وَقَوْسَاهُ حَوْلَ «يَدِي»؛ وَمَا قَبْلَهَا مِنَ التَّرْجَمَةِ (نَسَبُهُ، وَخَبَرُ ادِّعَاءِ أَبِيهِ إِيَّاهُ، وَأَغْرِبَةُ الْعَرَبِ) وَمَا بَعْدَهَا (حَرْبُ دَاحِسٍ، وَمَوْتُهُ) لَمْ يُؤْخَذْ. "
    + _scope[0] + " — وَهِيَ مِنَ الْبَحْرِ الْكَامِلِ، وَرَوِيُّهَا مِيمٌ مَكْسُورَةٌ وَقَافِيَتُهَا مُطْلَقَةٌ — بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) وَتَرْتِيبِهِ وَعَدِّهِ فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةِ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م (الْكِتَابُ ١١٢٥٣)، ص ٢٤٥–٢٦٥. " + _ch_ar + ". وَالْبَيْتُ جُمْلَةٌ وَاحِدَةٌ، وَعَلَامَةُ «•» آخِرُ صَدْرِهِ." + _rest[0] + " "
    "الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ عَلَى حَالِهِ بِإِمْلَاءِ هٰذَا الرَّفِّ، وَمَا تَرَكَتْهُ عَارِيًا — وَهُوَ حَرَكَاتُ خَبَرِ ابْنِ قُتَيْبَةَ كُلُّهَا سِوَى الشَّدَّاتِ، وَكَثِيرٌ مِنْ حُرُوفِ الْأَبْيَاتِ — ضَبَطَهُ الْمُحَرِّرُ بِمَا يُوجِبُهُ الْوَزْنُ وَالشَّرْحُ. "
    + ("وَخُولِفَ الْمَطْبُوعُ فِي هٰذِهِ الْمَوَاضِعِ، وَكُلُّهَا سَهْوُ طِبَاعَةٍ يَشْهَدُ عَلَيْهِ شَاهِدٌ: " + _div_ar + ". " if _div else "")
    + ("وَمِمَّا ضَبَطَهُ الْمُحَرِّرُ وَلَمْ يَقْطَعْ بِهِ وَزْنٌ وَلَا شَرْحٌ: " + "، وَ".join(f[1] for f in _flg) + ". " if _flg else "")
    + "إِعْرَابُ كُلِّ كَلِمَةٍ بِعِبَارَةِ هٰذَا الرَّفِّ، وَقَدْ رُوجِعَ إِعْرَابُ الْأَبْيَاتِ عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ: إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهَ الدُّرَّة (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م؛ الْكِتَابُ ١٥١٠١٧، ج ٢ ص ١٣٥–٢٦٤) — وَهُوَ يَرْوِي الْقَصِيدَةَ بِعَدٍّ آخَرَ وَيَزِيدُ أَبْيَاتًا لَيْسَتْ عِنْدَ الزَّوْزَنِيِّ — وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ: مَا نَصَّ عَلَيْهِ أَوْ وَصَفَهُ الزَّوْزَنِيُّ أَوِ الدُّرَّةُ ذُكِرَ مَنْسُوبًا إِلَيْهِ، وَمَا كَانَ بِحَدِّ التَّلْخِيصِ وَحْدَهُ — وَلَمْ يُسَمِّهِ الشَّارِحَانِ — قِيلَ فِيهِ: «عَلَى حَدِّ التَّلْخِيصِ»؛ وَلَمْ يُوجَدْ فِي مَتْنِ التَّلْخِيصِ اسْتِشْهَادٌ بِبَيْتٍ مِنْ هٰذِهِ الْقَصِيدَةِ. وَالتَّرْجَمَةُ مَعْنَى الْبَيْتِ عَلَى شَرْحِ الزَّوْزَنِيِّ، لَا شِعْرٌ. وَتَقْسِيمُ الْفُصُولِ وَعَنَاوِينُهَا وَعَلَامَاتُ التَّرْقِيمِ مِنَ الْمُحَرِّرِ، وَالنَّصُّ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.")
ATTR_EN = ("The RECEIVED text, word for word. Chapter 1 is the khabar of ʿAntara ibn Shaddād al-ʿAbsī from Ibn Qutayba (d. 276 AH), al-Shiʿr wa-l-shuʿarāʾ, in the edition al-Maktaba al-Shāmila names «Dār al-Ḥadīth, Cairo, 1423 AH» (book 23785), vol. 1 pp. 244–245, § 419 in full: one contiguous span with nothing cut from inside it; only the paragraph number, the editor's footnote marks and his brackets round «يَدِي» are left out. The rest of the entry — before it his lineage, how his father came to acknowledge him, and «the ravens of the Arabs»; after it the war of Dāḥis and his death — is not taken. "
    + _scope[1] + " — in the metre al-kāmil, rhyming on a mīm with kasra, the rhyme unbound — in the recension, order and verse-count of al-Zawzanī (d. 486 AH), Sharḥ al-Muʿallaqāt al-sabʿ, the edition Shamela names «Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423 AH / 2002 CE» (book 11253), pp. 245–265: " + _ch_en + ". Each verse is one sentence, and «•» marks the end of its first hemistich." + _rest[1] + " "
    "The vowelling has two layers. What the edition vowels is kept, in this shelf's spelling; what it leaves bare — every short vowel of Ibn Qutayba's khabar (the edition prints only its shaddas) and many letters of the verses — is supplied editorially, as the metre and the commentary require. "
    + ("The edition's print is departed from in these places, each a slip of the press with a witness against it: " + _div_en + ". " if _div else "")
    + ("Editorial vowels that neither metre nor commentary settles: " + ", ".join(f[2] for f in _flg) + ". " if _flg else "")
    + "Every token's iʿrāb is written in this shelf's own wording; that of the verses was checked against Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409 AH / 1989 CE; book 151017, vol. 2 pp. 135–264), who counts the ode differently and has verses al-Zawzanī does not; where he offers two readings the first is given and the second mentioned. The figures of balāgha are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ: one that al-Zawzanī or al-Durra names or describes is given with his name; one that rests on the Talkhīṣ's definition alone, which neither commentator names, says so in its line («by the Talkhīṣ's definition»). No verse of this ode was found cited in the matn of the Talkhīṣ. The translations give each verse's plain meaning after al-Zawzanī; they are not verse. The division into chapters, their titles and the punctuation are editorial. Pending scholarly review.")
ATTR_TR = ("Metin LAFZIYLA aktarılmıştır. 1. bölüm, Antere b. Şeddâd el-Absî'nin haberidir: İbn Kuteybe (ö. 276 h.), eş-Şi'r ve'ş-şuarâ, el-Mektebetü'ş-Şâmile'nin «Dâru'l-Hadîs, Kahire, 1423 h.» diye andığı baskı (kitap 23785), c. 1 s. 244–245, § 419'un tamamı: içinden hiçbir şey çıkarılmamış tek ve kesintisiz bir parça; yalnızca paragraf numarası, muhakkikin dipnot işaretleri ve «يَدِي» kelimesinin etrafındaki parantezi alınmamıştır. Tercemenin geri kalanı — öncesinde nesebi, babasının onu oğul olarak tanıması ve «Arapların kargaları»; sonrasında Dâhis savaşı ve ölümü — alınmamıştır. "
    + _scope[2] + " — kaside kâmil bahrindendir, revîsi kesreli mîm, kâfiyesi mutlaktır — Zevzenî'nin (ö. 486 h.) Şerhu'l-Muallakâti's-seb'indeki rivayeti, sırası ve beyit sayımıyla; Şâmile'nin «Dâru İhyâi't-Türâsi'l-Arabî, 1423 h. / 2002 m.» diye andığı baskı (kitap 11253), s. 245–265: " + _ch_tr + ". Her beyit tek cümledir; «•» ilk mısraın sonunu gösterir." + _rest[2] + " "
    "Harekeleme iki katmandır: baskının harekelediği yerler bu rafın imlâsıyla korunmuş; harekesiz bıraktığı yerler — İbn Kuteybe haberinin bütün kısa harekeleri (baskı yalnızca şeddeleri basar) ve beyitlerdeki pek çok harf — vezin ve şerhin gerektirdiği şekilde editörce harekelenmiştir. "
    + ("Baskıdan şu yerlerde ayrılınmıştır; hepsi, aleyhine şâhit bulunan dizgi sehvidir: " + _div_tr + ". " if _div else "")
    + ("Vezin ve şerhin kesinleştirmediği editoryal harekeler: " + ", ".join(f[3] for f in _flg) + ". " if _flg else "")
    + "Her kelimenin i'râbı bu rafın kendi ifadesiyle yazılmış; beyitlerin i'râbı Muhammed Ali Tâhâ ed-Dürre'nin Fethu'l-Kebîri'l-Müteâl: İ'râbü'l-Muallakâti'l-aşri't-tıvâl'i (Mektebetü's-Sevâdî, Cidde, 2. baskı, 1409 h. / 1989 m.; kitap 151017, c. 2 s. 135–264) ile karşılaştırılmıştır; o, kasideyi başka bir sayımla rivayet eder ve Zevzenî'de bulunmayan beyitler ekler; iki vecih verdiği yerde birincisi esas alınmış, ikincisi belirtilmiştir. Belâgat nükteleri Kazvînî'nin Telhîsu'l-Miftâh'ındaki bâblara göre adlandırılmıştır: Zevzenî'nin yahut Dürre'nin adını andığı veya tarif ettiği nükte ona nisbet edilerek verilmiş; yalnızca Telhîs'in tarifine dayanan ve iki şârihin de adlandırmadığı nükte, satırında «Telhîs'in tarifine göre» kaydıyla belirtilmiştir. Telhîs metninde bu kasideden şâhit getirilen bir beyte rastlanmamıştır. Çeviriler beytin Zevzenî'ye göre düz mânâsını verir; şiir değildir. Bölümlere ayırma, bölüm başlıkları ve noktalama editoryaldir. Metin ilmî incelemeyi beklemektedir.")
MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ عَنْتَرَةَ بْنِ شَدَّادٍ", "en": "The Muʿallaqa of ʿAntara ibn Shaddād", "tr": "Antere b. Şeddâd'ın Muallakası"},
 "subtitle": {"ar": ("الْمُعَلَّقَةُ كَامِلَةً" if WHOLE else "الْمُعَلَّقَةُ") + " بِرِوَايَةِ الزَّوْزَنِيِّ، مَعَ خَبَرِ الشَّاعِرِ عَنِ ابْنِ قُتَيْبَةَ — بَيْتًا بَيْتًا بِالْإِعْرَابِ وَالْبَلَاغَةِ",
              "en": ("The whole ode" if WHOLE else "The ode") + " in al-Zawzanī's recension, with the poet's story from Ibn Qutayba — verse by verse, with full iʿrāb and balāgha",
              "tr": "Zevzenî rivayetiyle muallaka" + ("nın tamamı" if WHOLE else "") + " ve İbn Kuteybe'den şairin haberi — beyit beyit, tam i'râb ve belâgatıyla"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": [],
 "attribution": {"ar": ATTR_AR, "en": ATTR_EN, "tr": ATTR_TR, "reviewStatus": "pending-scholarly-review"},
}
import shutil as _sh
if (PKG / "chapters").exists(): _sh.rmtree(PKG / "chapters")
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("chapters:", len(CHAPS), "| verses in package: 1-%d" % DONE_TO, "| verses authored:", len(VERSE), "of", TOTAL, "| waiting:", [x for x in sorted(VERSE) if x > DONE_TO],
      "| sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
