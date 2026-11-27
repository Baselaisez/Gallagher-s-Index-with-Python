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

# =====================================================================================================================
# Chapter 3 — الرَّحِيلُ، وَثَغْرُ عَبْلَةَ (al-Zawzanī vv. 9–15)
# =====================================================================================================================
def ILT(ar, en, tr):
    """an iltifāt the words themselves show (the Talkhīṣ's definition: a meaning put in one of the three persons after another)"""
    return HD("الْتِفَاتٌ " + ar, "there is an iltifāt, " + en, tr + " iltifât vardır", "iltifat")
KAANNA_ = Fr("حَرْفُ تَشْبِيهٍ وَنَصْبٍ", "the particle of likening that puts its noun in nasb", "teşbîh ve nasb harfi", "inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya")
def ISM_K(s="n"): return RO("اسْمُ كَأَنَّ", "the noun of كَأَنَّ", "كَأَنَّ'nin ismi", s, "inna-wa-akhawatuha")
def KH_K(s="r"): return RO("خَبَرُ كَأَنَّ", "the predicate of كَأَنَّ", "كَأَنَّ'nin haberi", s, "inna-wa-akhawatuha")
CL_KH_K = CL("r", "خَبَرُ كَأَنَّ", "the predicate of كَأَنَّ", "كَأَنَّ'nin haberi", "inna-wa-akhawatuha")

# ---- v. 9 ----
V(9, "How can she be visited, when her people have taken their spring quarters at ʿUnayzatān and ours are at al-Ghaylam?",
  "Ziyaret nasıl mümkün olsun? Onun ailesi baharı geçirmek üzere Uneyzeteyn'e konmuş, bizimkiler ise Gaylem'de.",
 [n("كَيْفَ", "kayfa", Fr("اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ", "an interrogative noun built on fatha, the fronted khabar, in the seat of raf'", "fetha üzere mebnî istifhâm ismi, öne alınmış haber, mahallen merfû", "al-istifham", "mubtada-khabar", "taqdim-al-musnad"),
     Sn("وَالِاسْتِفْهَامُ إِنْكَارِيٌّ أَوْ تَعَجُّبِيٌّ " + DUR + "، أَيْ: كَيْفَ يُمْكِنُنِي أَنْ أَزُورَهَا وَبَيْنَ الْمَوْضِعَيْنِ مَسَافَةٌ بَعِيدَةٌ وَمَشَقَّةٌ مَدِيدَةٌ " + ZAW, "the question is one of denial, or of wonder (al-Durra): how could I visit her, with so far a road and so long a hardship between the two places? (al-Zawzanī)", "istifhâm inkârî yahut taaccübîdir (Dürre): iki yer arasında uzak bir mesafe ve uzun bir meşakkat varken onu nasıl ziyaret edebilirim? (Zevzenî)", "khuruj-al-istifham")),
  n("الْمَزَارُ", "mazar-ant", MB(), Dn("مُبْتَدَأٌ مُؤَخَّرٌ؛ وَالْمَزَارُ فِي الْبَيْتِ مَصْدَرٌ كَالزِّيَارَةِ " + ZAW, "placed after its khabar; الْمَزَار in the verse is a masdar, like الزِّيَارَة (al-Zawzanī)", "haberinden sonraya bırakılmıştır; الْمَزَار beyitte الزِّيَارَة gibi masdardır (Zevzenî)", "masdar")),
  pt("وَقَدْ", "qad", PRE("wa-hal", "قَدْ"), Fr("حَرْفُ تَحْقِيقٍ", "a particle of certainty", "tahkîk harfi", "qad-harf"), s=[WA, ("قَدْ", "qad", "part")]),
  v("تَرَبَّعَ", "tarabbaa-ant", MADI, FAIL_BAD, CL_HAL("الْمَزَارُ"), Dn("التَّرَبُّعُ: الْإِقَامَةُ زَمَنَ الرَّبِيعِ " + ZAW, "التَّرَبُّع: staying somewhere through the spring (al-Zawzanī)", "التَّرَبُّع: bahar mevsiminde bir yerde konaklamak (Zevzenî)"), g=["form-v-verbs"]),
  n("أَهْلُهَا", "ahl", FL(), IDF("هَا"), ILT("مِنَ الْخِطَابِ فِي «نَزَلْتِ» إِلَى الْغَيْبَةِ", "from the second person of «نَزَلْتِ» to the third", "«نَزَلْتِ»deki hitaptan gaybete"), s=[("أَهْلُ", "ahl", "noun"), P("هَا")])],
 [pn("بِعُنَيْزَتَيْنِ", "unayzatan-ant", JN("بِ", "عُنَيْزَتَيْنِ", "jD", sense=FI_SENSE), TA("تَرَبَّعَ"), Dn("مَوْضِعَانِ", "two places", "iki yer adı"), s=[BI, ("عُنَيْزَتَيْنِ", "unayzatan-ant", "propn")]),
  n("وَأَهْلُنَا", "ahl", PRE("wa", "أَهْلُ"), RO("فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ دَلَّ عَلَيْهِ مَا قَبْلَهُ تَقْدِيرُهُ: حَلَّ", "the doer of an omitted verb that what goes before points to — «have settled»", "öncesinin delâlet ettiği mahzûf fiilin («kondu») fâili", "r", "fail", "hadhf-wa-taqdir"), IDF("نَا"),
     Dn("وَلَكَ أَنْ تَجْعَلَ الْوَاوَ حَالِيَّةً وَ«أَهْلُنَا» مُبْتَدَأً خَبَرُهُ «بِالْغَيْلَمِ» " + DUR, "or the waw is the waw of the hal and «أَهْلُنَا» a mubtada whose khabar is «بِالْغَيْلَمِ» (al-Durra)", "yahut vâv hâliyye, «أَهْلُنَا» mübtedâ, «بِالْغَيْلَمِ» de haberidir (Dürre)"), s=[WA, ("أَهْلُ", "ahl", "noun"), P("نَا")]),
  pn("بِالْغَيْلَمِ", "ghaylam-ant", JN("بِ", "الْغَيْلَمِ", sense=FI_SENSE), QA, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَحْذُوفِ؛ وَالْغَيْلَمُ مَوْضِعٌ", "the phrase hangs on the omitted verb; al-Ghaylam is a place", "câr-mecrûr mahzûf fiile müteallik; Gaylem bir yer adıdır"), s=[BI, ("الْغَيْلَمِ", "ghaylam-ant", "propn")])])

# ---- v. 10 ----
V(10, "If you had resolved to part — no wonder: your camels were bridled on a dark night.",
  "Ayrılığa karar vermişsen (şaşılmaz); çünkü develerinize karanlık bir gecede yular vurulmuştu.",
 [pt("إِنْ", "in-shartiyya", Fr("حَرْفُ شَرْطٍ جَازِمٌ", "the conditional particle that puts in jazm", "cezmeden şart harfi", "in-shartiyya", "al-majzum-wal-shart-wal-jaza")),
  v("كُنْتِ", "kana", Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَتَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ", "the defective past verb, built on sukun, in the seat of jazm as the verb of the condition; the ta of the woman addressed is the noun of كَانَ, in the seat of raf'", "sükûn üzere mebnî nâkıs mâzî, şart fiili olarak mahallen meczûm; muhâtaba tâsı كَانَ'nin ismidir, mahallen merfû", "kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil", "al-majzum-wal-shart-wal-jaza"),
     ILT("مِنَ الْغَيْبَةِ فِي «أَهْلُهَا» إِلَى الْخِطَابِ", "from the third person of «أَهْلُهَا» to the second", "«أَهْلُهَا»daki gaybetten hitaba")),
  v("أَزْمَعْتِ", "azmaa", TU("anti"), CL("n", "خَبَرُ كَانَ", "the predicate of كَانَ", "كَانَ'nin haberi", "kana-wa-akhawatuha"), Dn("الْإِزْمَاعُ: تَوْطِينُ النَّفْسِ عَلَى الشَّيْءِ " + ZAW, "الْإِزْمَاع: setting one's mind firmly on a thing (al-Zawzanī)", "الْإِزْمَاع: bir şeye kesin karar vermek (Zevzenî)"), g=["form-iv-verbs"]),
  n("الْفِرَاقَ", "firaq", Fr("اسْمٌ مَنْصُوبٌ عَلَى نَزْعِ الْخَافِضِ بِالْفَتْحَةِ، وَالتَّقْدِيرُ: عَلَى الْفِرَاقِ", "a noun in nasb by the fatha because its jarr letter is dropped — «[on] parting»", "cer harfi hazfedildiği için fetha ile mansûb isim; takdiri: «ayrılığa»", "hadhf-al-jarr"), Dn("كَذَا أَعْرَبَهُ الدُّرَّةُ", "so al-Durra parses it", "Dürre böyle i'râb eder")),
  pt("فَإِنَّمَا", "innama", Fr("الْفَاءُ حَرْفٌ دَالٌّ عَلَى التَّعْلِيلِ، وَإِنَّمَا كَافَّةٌ وَمَكْفُوفَةٌ", "the fa gives the reason; إِنَّمَا is إِنَّ held back by مَا", "fâ ta'lîl bildirir; إِنَّمَا kâffe ve mekfûfedir", "innama-kaffa"),
     Sn("وَجَوَابُ الشَّرْطِ مَحْذُوفٌ تَقْدِيرُهُ: فَلَا عَجَبَ " + DUR + " — وَهُوَ إِيجَازٌ بِالْحَذْفِ؛ وَمَعْنَاهُ عِنْدَ الزَّوْزَنِيِّ: فَإِنِّي قَدْ شَعَرْتُ بِهِ بِزَمِّكُمْ إِبِلَكُمْ لَيْلًا", "the answer of the condition is left out — «then it is no wonder» (al-Durra) — a brevity by omission; al-Zawzanī gives the sense: «for I knew of it by your bridling your camels at night»", "şartın cevabı hazfedilmiştir, takdiri: «şaşılmaz» (Dürre) — bu, hazifle îcâzdır; Zevzenî'ye göre mânâ: «çünkü develerinize geceleyin yular vurmanızdan bunu sezmiştim»", "ijaz-al-hadhf", "hadhf-wa-taqdir"), s=[FA, ("إِنَّمَا", "innama", "part")])],
 [v("زُمَّتْ", "zamma-ant", Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "a past verb in the passive, built on fatha; the ta marks the feminine", "meçhul mâzî, fetha üzere mebnî; tâ te'nîs içindir", "al-majhul-fil-kafiya", "doubled-verbs"), Dn("زَمَّ الْبَعِيرَ: جَعَلَ لَهُ زِمَامًا اسْتِعْدَادًا لِلسَّفَرِ (حَاشِيَةُ الطَّبْعَةِ)", "زَمَّ الْبَعِيرَ: he put the nose-rein on the camel, making ready to travel (the edition's note)", "زَمَّ الْبَعِيرَ: yolculuğa hazırlanmak için deveye yular vurdu (baskının notu)")),
  n("رِكَابُكُمُ", "rikab-ant", NF(), IDF("كُمُ"), Dn("وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ وَأُشْبِعَتْ لِإِقَامَةِ الْوَزْنِ " + DUR + "؛ وَالرِّكَابُ: الْإِبِلُ، لَا وَاحِدَ لَهَا مِنْ لَفْظِهَا " + ZAW, "the mim is given a damma, and lengthened, to keep the metre (al-Durra); الرِّكَاب: riding-camels — it has no singular of its own form (al-Zawzanī)", "mîm vezin için damme ile harekelenip uzatılmıştır (Dürre); الرِّكَاب: binek develeri; kendi lafzından tekili yoktur (Zevzenî)"), s=[("رِكَابُ", "rikab-ant", "noun"), P("كُمُ")]),
  n("بِلَيْلٍ", "layl", JN("بِ", "لَيْلٍ", sense=FI_SENSE), TA("زُمَّتْ"),
     HD("كِنَايَةٌ عَنْ أَنَّ الرَّحِيلَ أَمْرٌ بُيِّتَ: أُرِيدَ بِزَمِّ الرِّكَابِ لَيْلًا لَازِمُهُ؛ قَالَ الدُّرَّةُ: «فَإِنَّ هٰذَا الْأَمْرَ قَدْ دَبَّرْتُمُوهُ بِلَيْلٍ»", "this is a kināya for a departure settled beforehand: the bridling of the camels by night is said and what goes with it is meant; al-Durra: «this is a thing you planned by night»", "bu, göçün önceden kararlaştırılmış bir iş olduğundan kinâyedir: develere geceleyin yular vurulması söylenmiş, bunun lâzımı kastedilmiştir; Dürre: «bu işi siz gece vakti kurmuşsunuz»", "kinaya"), s=[BI, ("لَيْلٍ", "layl", "noun")]),
  n("مُظْلِمِ", "muzlim", NAT("لَيْلٍ"), QT)])

# ---- v. 11 ----
V(11, "Nothing alarmed me but her people's pack-camels, in the midst of the dwellings, cropping the seeds of the khimkhim.",
  "Beni ancak, ailesinin yük develerinin yurtların ortasında hımhım tohumu yemesi ürküttü.",
 [pt("مَا", "ma-nafiya", Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi")),
  v("رَاعَنِي", "raa-alarm-ant", MADI, Fr("، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "; the nun guards the verb's ending, and the ya is its object, in the seat of nasb", "; nûn vikâye içindir, yâ mef'ûlün bih, mahallen mansûb", "al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim"), CL_IST, Dn("رَاعَهُ رَوْعًا: أَفْزَعَهُ " + ZAW, "رَاعَهُ: it frightened him (al-Zawzanī)", "رَاعَهُ: onu korkuttu (Zevzenî)"), s=[("رَاعَ", "raa-alarm-ant", "verb"), ("نِ", "nun-wiqaya", "part"), P("ي")], g=["hollow-verbs"]),
  pt("إِلَّا", "illa", Fr("أَدَاةُ حَصْرٍ", "the particle of restriction", "hasr edatı", "istithna-mufarragh", "istithna"),
     HD("قَصْرٌ بِالنَّفْيِ وَالِاسْتِثْنَاءِ: قَصَرَ الرَّوْعَ عَلَى حَمُولَةِ أَهْلِهَا", "this is a restriction (qaṣr) by negation and exception: the alarm is confined to her people's pack-camels", "bu, nefy ve istisnâ ile yapılmış bir kasrdır: korku, ailesinin yük develerine hasredilmiştir", "qasr", "turuq-al-qasr")),
  n("حَمُولَةُ", "hamula-ant", FL(), MDF, Dn("الْحَمُولَةُ: الْإِبِلُ الَّتِي تُطِيقُ أَنْ يُحْمَلَ عَلَيْهَا " + ZAW, "الْحَمُولَة: the camels strong enough to carry loads (al-Zawzanī)", "الْحَمُولَة: yük taşımaya gücü yeten develer (Zevzenî)"),
     Sn("وَفِي الْبَيْتِ كِنَايَةٌ عَنْ قُرْبِ الرَّحِيلِ: مَا أَنْذَرَنِي بِارْتِحَالِهَا إِلَّا انْقِضَاءُ مُدَّةِ الِانْتِجَاعِ وَالْكَلَإِ، فَإِذَا انْقَضَتْ عَلِمْتُ أَنَّهَا تَرْتَحِلُ " + ZAW, "the verse is a kināya for a departure close at hand: what warned me of her going was only that the season of pasture had run out — when it had, I knew she would move on (al-Zawzanī)", "beyitte göçün yaklaştığından kinâye vardır: gideceğini bana ancak otlak mevsiminin bitmesi haber verdi; bitince göçeceğini anladım (Zevzenî)", "kinaya")),
  n("أَهْلِهَا", "ahl", MI(), IDF("هَا"), ILT("مِنَ الْخِطَابِ فِي «رِكَابُكُمُ» إِلَى الْغَيْبَةِ", "from the second person of «رِكَابُكُمُ» to the third", "«رِكَابُكُمُ»daki hitaptan gaybete"), s=[("أَهْلِ", "ahl", "noun"), P("هَا")])],
 [n("وَسْطَ", "wast", ZM(), MDF, ZT("تَسَفُّ"), Dn("وَسْطَ بِتَسْكِينِ السِّينِ لَا يَكُونُ إِلَّا ظَرْفًا، وَالْوَسَطُ بِفَتْحِهَا اسْمٌ لِمَا بَيْنَ طَرَفَيِ الشَّيْءِ " + ZAW, "وَسْط, with a quiescent sin, is only ever an adverb; الْوَسَط, with fatha, is a noun for what lies between a thing's two ends (al-Zawzanī)", "sîn'in sükûnuyla وَسْط yalnızca zarf olur; fethasıyla الْوَسَط ise bir şeyin iki ucu arasındaki yerin adıdır (Zevzenî)")),
  n("الدِّيَارِ", "dar", MI(), Dn("جَمْعُ دَارٍ", "the plural of دَار", "دَار'ın cem'i", "jam-taksir")),
  v("تَسَفُّ", "saffa-ant", MUDR(), HID("هِيَ", ("الْحَمُولَةِ", "the pack-camels", "yük develeri")), CL_HAL("حَمُولَةُ"), g=["doubled-verbs"]),
  n("حَبَّ", "habb-grain", MF(), MDF),
  n("الْخِمْخِمِ", "khimkhim-ant", MI(), QA, Dn("الْخِمْخِمُ: نَبْتٌ تُعْلَفُهُ الْإِبِلُ " + ZAW, "الْخِمْخِم: a plant camels are fed on (al-Zawzanī)", "الْخِمْخِم: develere yedirilen bir bitki (Zevzenî)"))])

# ---- v. 12 ----
V(12, "Among them are forty-two milch-camels, black as the inner wing-feathers of the black raven.",
  "İçlerinde, kapkara kuzgunun iç kanat tüyleri gibi siyah kırk iki sağmal deve vardır.",
 [pp("فِيهَا", "fi", JP("فِي", "هَا"), TAM("khabar-m"), Dn("وَالضَّمِيرُ لِلْحَمُولَةِ", "the pronoun is the pack-camels", "zamir yük develerine döner", "taqdim-al-musnad"), s=[("فِي", "fi", "prep"), P("هَا")]),
  n("اثْنَتَانِ", "ithnatan", Fr("مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى", "the mubtada, placed after its khabar, in raf' by the alif — it is declined like the dual", "sonraya bırakılmış mübtedâ; tesniyeye mülhak olduğu için elif ile merfû", "mubtada-khabar", "al-muthanna", "asma-al-adad-fil-kafiya"),
     Sn("وَفِي الْبَيْتِ كِنَايَةٌ عَنْ غِنَى أَهْلِهَا: «فَفِيهِ إِيمَاءٌ بِأَنَّ أَهْلَ الْحَبِيبَةِ ذَوُو غِنًى وَيَسَارٍ» " + DUR + "؛ وَقَالَ الزَّوْزَنِيُّ: ذَكَرَ سَوَادَهَا لِأَنَّهَا أَنْفَسُ الْإِبِلِ وَأَعَزُّهَا عِنْدَهُمْ، وَصَفَ رَهْطَ عَشِيقَتِهِ بِالْغِنَى وَالتَّمَوُّلِ", "the verse is a kināya for her people's wealth: «it hints that the beloved's people are rich and at ease» (al-Durra); al-Zawzanī: he names their blackness because black camels were the choicest and most prized — he is describing his beloved's kin as wealthy", "beyitte ailesinin zenginliğinden kinâye vardır: «sevgilinin ailesinin zengin ve varlıklı olduğuna îmâ vardır» (Dürre); Zevzenî: siyahlıklarını anmıştır, çünkü siyah develer onların yanında en değerli ve en makbul develerdir; sevgilisinin kavmini zenginlikle vasfetmiştir", "kinaya", "tarid-talwih-ramz")),
  n("وَأَرْبَعُونَ", "arbaun", PRE("wa", "أَرْبَعُونَ"), Fr("مَعْطُوفٌ عَلَى «اثْنَتَانِ» مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", "conjoined to «اثْنَتَانِ», in raf' by the waw — it is declined like the sound masculine plural", "«اثْنَتَانِ» kelimesine ma'tûf; cem-i müzekker sâlime mülhak olduğu için vâv ile merfû", "atf-nasaq", "jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"), s=[WA, ("أَرْبَعُونَ", "arbaun", "noun")]),
  n("حَلُوبَةً", "haluba", Fr("تَمْيِيزُ الْعَدَدِ مَنْصُوبٌ بِالْفَتْحَةِ", "the tamyiz (specifier) of the number, in nasb by the fatha", "sayının temyîzi, fetha ile mansûb", "tamyiz", "al-tamyiz-wa-ahkamuh"), Dn("الْحَلُوبَةُ جَمْعُ الْحَلُوبِ عِنْدَ الْبَصْرِيِّينَ، وَقَالَ غَيْرُهُمْ: هِيَ بِمَعْنَى مَحْلُوبَةٍ " + ZAW, "الْحَلُوبَة is the plural of الْحَلُوب for the Basrans; others say it means «one that is milked» (al-Zawzanī)", "الْحَلُوبَة, Basralılara göre الْحَلُوب'un cem'idir; başkalarına göre «sağılan» anlamındadır (Zevzenî)"))],
 [n("سُودًا", "aswad", NAT("حَلُوبَةً", "n"), Dn("جَمْعُ سَوْدَاءَ — وَهُوَ أَوَّلُ ثَلَاثَةِ أَوْجُهٍ ذَكَرَهَا ابْنُ هِشَامٍ، وَالثَّانِي أَنَّهُ حَالٌ مِنَ الْعَدَدِ، وَالثَّالِثُ أَنَّهُ حَالٌ مِنْ «حَلُوبَةً» مَعَ كَوْنِهَا نَكِرَةً؛ وَيُرْوَى «سُودٌ» بِالرَّفْعِ نَعْتًا لِلْعَدَدِ " + DUR, "the plural of سَوْدَاء — the first of three readings Ibn Hishām gives; the second makes it a hal of the number, the third a hal of «حَلُوبَةً» though that is indefinite; it is also transmitted as «سُودٌ», in raf', a na't of the number (al-Durra)", "سَوْدَاء'nın cem'i — İbn Hişâm'ın zikrettiği üç vechin ilkidir; ikincisi sayıdan hâl, üçüncüsü nekre olmasına rağmen «حَلُوبَةً»den hâl olmasıdır; sayının na'tı olarak merfû «سُودٌ» diye de rivayet edilir (Dürre)", "jam-taksir", "hal")),
  n("كَخَافِيَةِ", "khafiya-ant", JN("كَ", "خَافِيَةِ"), MDF, TAM("naat", "حَلُوبَةً", "ثَالِثٍ"), Dn("أَوْ حَالٍ مِنْهُ " + DUR + "؛ وَالْخَوَافِي مِنَ الْجَنَاحِ: أَرْبَعٌ مِنْ رِيشِهِ " + ZAW, "or on a hal of it (al-Durra); الْخَوَافِي of a wing are four of its feathers (al-Zawzanī)", "yahut ondan bir hâle (Dürre); kanadın الْخَوَافِي'si, tüylerinden dördüdür (Zevzenî)"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ: الْمُشَبَّهُ النُّوقُ الْحَلُوبَةُ، وَالْمُشَبَّهُ بِهِ خَوَافِي الْغُرَابِ الْأَسْوَدِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ السَّوَادُ وَقَدْ ذُكِرَ فِي «سُودًا» " + ZAW, "here is a tashbih mursal mufaṣṣal: the milch-camels are likened to the inner feathers of the black raven; the tool is the kaf; the point of likeness — blackness — is stated in «سُودًا» (al-Zawzanī)", "burada mürsel mufassal bir teşbîh vardır: müşebbeh sağmal develer; müşebbehün bih kara kuzgunun iç kanat tüyleri; edat kâf; vech-i şebeh siyahlıktır ve «سُودًا» kelimesinde zikredilmiştir (Zevzenî)", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih", "wajh-al-shabah"), s=[KA, ("خَافِيَةِ", "khafiya-ant", "noun")]),
  n("الْغُرَابِ", "ghurab", MI()),
  n("الْأَسْحَمِ", "asham-ant", NAT("الْغُرَابِ"), QA, Dn("الْأَسْحَمُ: الْأَسْوَدُ " + ZAW, "الْأَسْحَم: black (al-Zawzanī)", "الْأَسْحَم: siyah (Zevzenî)"))])

# ---- v. 13 ----
V(13, "— when she takes you captive with a mouth of keen-edged teeth, white, sweet where it is kissed and pleasant to taste.",
  "(O korku,) seni, keskin kenarlı dişleri olan, bembeyaz, öpüldüğü yeri tatlı, tadı hoş bir ağızla esir aldığı zamandı.",
 [n("إِذْ", "idh", Fr("ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«رَاعَنِي»", "an adverb for past time, built on sukun, in the seat of nasb; it hangs on «رَاعَنِي»", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «رَاعَنِي» kelimesine müteallik", "maful-fih", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"), Dn("أَوْ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ " + DUR + "؛ أَيْ: إِنَّمَا كَانَ فَزَعُكَ مِنِ ارْتِحَالِهَا حِينَ تَسْتَبِيكَ " + ZAW, "or on an omitted «remember» (al-Durra); that is: your alarm at her going was when she was taking you captive (al-Zawzanī)", "yahut «hatırla» takdirindeki mahzûf fiile (Dürre); yani: onun göçünden korkun, seni esir aldığı zamandı (Zevzenî)")),
  v("تَسْتَبِيكَ", "istaba-ant", MUDR("y"), HID("هِيَ", ("عَبْلَةَ", "ʿAbla", "Able")), OBJ("كَ"), CL_MI("إِذْ"), Dn("الِاسْتِبَاءُ وَالسَّبْيُ وَاحِدٌ " + ZAW, "الِاسْتِبَاء and السَّبْي are one: taking captive (al-Zawzanī)", "الِاسْتِبَاء ile السَّبْي birdir: esir almak (Zevzenî)"),
     HD("تَجْرِيدٌ وَالْتِفَاتٌ: انْتَقَلَ مِنَ التَّكَلُّمِ فِي «رَاعَنِي» إِلَى خِطَابِ نَفْسِهِ", "there is a tajrīd and an iltifāt: he passes from the first person of «رَاعَنِي» to addressing himself", "tecrîd ve iltifât vardır: «رَاعَنِي»deki tekellümden kendi nefsine hitaba geçmiştir", "tajrid", "iltifat"), s=[("تَسْتَبِي", "istaba-ant", "verb"), P("كَ")], g=["form-viii-verbs"]),
  n("بِذِي", "dhu", JN("بِ", "ذِي", "j5"), MDF, TA("تَسْتَبِي"),
     Sn("وَفِيهِ إِيجَازٌ بِحَذْفِ الْمَوْصُوفِ: أَيْ بِثَغْرٍ ذِي غُرُوبٍ " + ZAW, "here is brevity by dropping the thing described: «with [a mouth] of keen edges» (al-Zawzanī)", "burada mevsûfun hazfiyle îcâz vardır: «keskin kenarlı [bir ağızla]» (Zevzenî)", "ijaz-al-hadhf"), s=[BI, ("ذِي", "dhu", "noun")]),
  n("غُرُوبٍ", "gharb-ant", MI(), Dn("جَمْعُ غَرْبٍ، وَغَرْبُ كُلِّ شَيْءٍ: حَدُّهُ؛ أَرَادَ بِالْغُرُوبِ الْأُشُرَ الَّتِي تَكُونُ فِي أَسْنَانِ الشَّوَابِّ " + ZAW, "the plural of غَرْب, the edge of a thing; he means the fine serrations on the teeth of the young (al-Zawzanī)", "غَرْب'in cem'i; bir şeyin غَرْب'i onun keskin kenarıdır; gençlerin dişlerindeki ince tırtılları kastetmiştir (Zevzenî)", "jam-taksir")),
  n("وَاضِحٍ", "wadih", NAT("ذِي غُرُوبٍ", nth="ثَانٍ"), Dn("أَيْ لِلثَّغْرِ الْمَحْذُوفِ؛ وَالْوُضُوحُ: الْبَيَاضُ " + ZAW, "that is, of the omitted «mouth»; الْوُضُوح is whiteness (al-Zawzanī)", "yani mahzûf «ağız»ın; الْوُضُوح: beyazlık (Zevzenî)"))],
 [n("عَذْبٍ", "adhb", NAT("ذِي غُرُوبٍ", nth="ثَالِثٌ"), Dn("صِفَةٌ مُشَبَّهَةٌ رَفَعَتْ مَا بَعْدَهَا؛ وَيُرْوَى بِالرَّفْعِ خَبَرًا مُقَدَّمًا وَ«مُقَبَّلُهُ» مُبْتَدَأً مُؤَخَّرًا " + DUR, "a sifa mushabbaha that raises what follows; it is also transmitted in raf', a fronted khabar with «مُقَبَّلُهُ» its mubtada (al-Durra)", "kendinden sonrakini ref eden sıfat-ı müşebbehe; öne alınmış haber olarak merfû, «مُقَبَّلُهُ» de sonraya bırakılmış mübtedâ diye de rivayet edilir (Dürre)", "sifa-mushabbaha")),
  n("مُقَبَّلُهُ", "muqabbal-ant", RO("فَاعِلٌ لِلصِّفَةِ الْمُشَبَّهَةِ «عَذْبٍ»", "the doer of the sifa mushabbaha «عَذْبٍ»", "«عَذْبٍ» sıfat-ı müşebbehesinin fâili", "r", "fail"), IDF("هُ"), Dn("الْمُقَبَّلُ: مَوْضِعُ التَّقْبِيلِ " + ZAW, "الْمُقَبَّل: the place that is kissed (al-Zawzanī)", "الْمُقَبَّل: öpülen yer (Zevzenî)"), s=[("مُقَبَّلُ", "muqabbal-ant", "noun"), P("هُ")]),
  n("لَذِيذِ", "ladhidh", NAT("ذِي غُرُوبٍ", nth="آخَرُ"), MDF, Dn("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا", "the sifa mushabbaha annexed to its doer", "sıfat-ı müşebbehenin fâiline izâfeti", "idafa-lafziyya", "sifa-mushabbaha")),
  n("الْمَطْعَمِ", "matam-ant", MI(), QA, Dn("الْمَطْعَمُ: الطَّعْمُ " + ZAW, "الْمَطْعَم: the taste (al-Zawzanī)", "الْمَطْعَم: tat (Zevzenî)"))])

# ---- v. 14 ----
V(14, "It is as if a perfumer's musk-pod, in the breath of a fair woman, ran ahead of her teeth to you from her mouth.",
  "Sanki bir attarın misk kesesi, güzel bir kadının nefesinde, ağzından sana doğru dişlerinden önce ulaşmış gibidir.",
 [pt("وَكَأَنَّ", "kaanna", PRE("wa-ist", "كَأَنَّ"), KAANNA_, s=[WA, ("كَأَنَّ", "kaanna", "part")]),
  n("فَارَةَ", "fara-ant", ISM_K(), MDF, Dn("فَارَةُ الْمِسْكِ: وِعَاؤُهُ؛ سُمِّيَتْ فَارَةً لِأَنَّ الرَّوَائِحَ الطَّيِّبَةَ تَفُورُ مِنْهَا " + ZAW, "the «fāra» of musk is its pod; so called because the sweet scents rise (تَفُورُ) from it (al-Zawzanī)", "miskin «fâre»si onun kesesidir; güzel kokular ondan fışkırdığı (تَفُورُ) için bu adı almıştır (Zevzenî)"),
     Sn("وَفِيهِ تَشْبِيهٌ: شَبَّهَ طِيبَ نَكْهَتِهَا بِطِيبِ رِيحِ الْمِسْكِ " + ZAW + "، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الطِّيبُ، فَهُوَ مُرْسَلٌ مُجْمَلٌ", "here is a tashbih: the sweetness of her breath is likened to the sweetness of the scent of musk (al-Zawzanī); the tool is كَأَنَّ, and the point of likeness — sweetness — is left unsaid: a tashbih mursal mujmal", "burada teşbîh vardır: nefesinin güzel kokusu misk kokusunun güzelliğine benzetilmiştir (Zevzenî); edat «كَأَنَّ»; vech-i şebeh olan güzel koku hazfedilmiştir: mürsel mücmel teşbîhtir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih")),
  n("تَاجِرٍ", "tajir", MI(), Dn("أَرَادَ بِالتَّاجِرِ: الْعَطَّارَ " + ZAW, "by «the merchant» he means the perfumer (al-Zawzanī)", "«tâcir» ile attarı kastetmiştir (Zevzenî)")),
  n("بِقَسِيمَةٍ", "qasima-ant", JN("بِ", "قَسِيمَةٍ", sense=FI_SENSE), TAM("naat", "فَارَةَ تَاجِرٍ"), Dn("الْقَسَامَةُ: الْحُسْنُ وَالصَّبَاحَةُ، وَالنَّعْتُ قَسِيمٌ؛ أَيْ: بِنَكْهَةِ امْرَأَةٍ حَسْنَاءَ " + ZAW, "الْقَسَامَة is beauty and fairness, and the adjective is قَسِيم; that is, «in the breath of a fair woman» (al-Zawzanī)", "الْقَسَامَة: güzellik ve alımlılık; sıfatı قَسِيم'dir; yani: «güzel bir kadının nefesinde» (Zevzenî)"), s=[BI, ("قَسِيمَةٍ", "qasima-ant", "noun")])],
 [v("سَبَقَتْ", "sabaqa", MADI_F, HID("هِيَ", ("«فَارَةَ تَاجِرٍ»", "the musk-pod", "misk kesesi")), CL_KH_K, g=["thulathi-mujarrad-babs"]),
  n("عَوَارِضَهَا", "arida-ant", MF(), IDF("هَا"), Dn("جَمْعُ عَارِضَةٍ؛ وَالْعَوَارِضُ مِنَ الْأَسْنَانِ مَعْرُوفَةٌ " + ZAW + "؛ أَيْ: تَسْبِقُ نَكْهَتُهَا الطَّيِّبَةُ عَوَارِضَهَا إِذَا رُمْتَ تَقْبِيلَهَا", "the plural of عَارِضَة; the ʿawāriḍ among the teeth are well known (al-Zawzanī); that is, her sweet breath reaches you before her teeth do", "عَارِضَة'nin cem'i; dişlerden «avârız» bilinmektedir (Zevzenî); yani: güzel nefesi sana dişlerinden önce ulaşır", "jam-taksir", "mamnu-min-sarf"), s=[("عَوَارِضَ", "arida-ant", "noun"), P("هَا")]),
  pp("إِلَيْكَ", "ila", JP("إِلَى", "كَ"), TA("سَبَقَتْ"), s=[("إِلَيْ", "ila", "prep"), P("كَ")]),
  pp("مِنَ", "min", HJ, Dn("وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ", "voweled with fatha before the following ال", "iki sâkin karşılaştığı için fetha ile harekelendi")),
  n("الْفَمِ", "fam", MJ(), TA("سَبَقَتْ"), QA)])

# ---- v. 15 ----
V(15, "Or a meadow never yet grazed, whose growth a rain has tended that brings little dung with it, and that is no trodden, well-known place.",
  "Yahut henüz otlanmamış bir çayır (gibidir); bitkisini, beraberinde gübre az olan bir yağmur beslemiş; orası ayak basılan, bilinen bir yer de değildir.",
 [pt("أَوْ", "aw", Fr("حَرْفُ عَطْفٍ", "a conjunction", "atıf harfi", "atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya")),
  n("رَوْضَةً", "rawda", ATF("فَارَةَ", "n"), Dn("فِي الْبَيْتِ قَبْلَهُ", "in the verse before", "önceki beyitteki"),
     HD("تَشْبِيهُ الْجَمْعِ، لِتَعَدُّدِ الْمُشَبَّهِ بِهِ: طِيبُ نَكْهَتِهَا كَطِيبِ رِيحِ فَارَةِ الْمِسْكِ أَوْ كَطِيبِ رِيحِ رَوْضَةٍ نَاضِرَةٍ لَمْ تُرْعَ " + ZAW, "this is a «tashbīh al-jamʿ», the thing likened-to being more than one: the sweetness of her breath is like that of a musk-pod, or like that of a fresh meadow never grazed (al-Zawzanī)", "bu, müşebbehün bih birden fazla olduğu için «teşbîhü'l-cem'»dir: nefesinin güzel kokusu misk kesesinin kokusu gibi, yahut hiç otlanmamış taze bir çayırın kokusu gibidir (Zevzenî)", "tashbih", "aqsam-al-tashbih")),
  n("أُنُفًا", "unuf-ant", NAT("رَوْضَةً", "n"), Dn("رَوْضَةٌ أُنُفٌ: لَمْ تُرْعَ بَعْدُ " + ZAW, "a meadow that is أُنُف: not yet grazed (al-Zawzanī)", "أُنُف çayır: henüz otlanmamış (Zevzenî)")),
  v("تَضَمَّنَ", "tadammana", MADI, FAIL_BAD, CL("r", "خَبَرُ «كَأَنَّ» فِي التَّقْدِيرِ", "the predicate of the كَأَنَّ understood", "takdir edilen «كَأَنَّ»nin haberi"), Dn("وَقَالَ ابْنُ الْأَنْبَارِيِّ: كَلَامٌ مُسْتَأْنَفٌ " + DUR, "Ibn al-Anbārī takes it as a new sentence (al-Durra)", "İbnü'l-Enbârî ise müste'nef cümle sayar (Dürre)"), g=["form-v-verbs"]),
  n("نَبْتَهَا", "nabt", RO("مَفْعُولٌ بِهِ مُقَدَّمٌ", "the direct object, placed before the doer", "öne geçmiş mef'ûlün bih", "n", "maful-bihi"), IDF("هَا"), s=[("نَبْتَ", "nabt", "noun"), P("هَا")])],
 [n("غَيْثٌ", "ghayth", RO("فَاعِلٌ مُؤَخَّرٌ", "the doer, placed after the object", "sonraya bırakılmış fâil", "r", "fail")),
  n("قَلِيلُ", "qalil", NAT("غَيْثٌ", "r"), MDF, Dn("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا", "the sifa mushabbaha annexed to its doer", "sıfat-ı müşebbehenin fâiline izâfeti", "idafa-lafziyya", "sifa-mushabbaha")),
  n("الدِّمْنِ", "dimna", MI(), Dn("الدِّمَنُ وَالدِّمْنُ: جَمْعُ دِمْنَةٍ وَهِيَ السِّرْجِينُ " + ZAW, "الدِّمَن / الدِّمْن: the plural of دِمْنَة, dung (al-Zawzanī)", "الدِّمَن / الدِّمْن: «gübre» anlamındaki دِمْنَة'nin cem'i (Zevzenî)", "jam-taksir")),
  v("لَيْسَ", "laysa", LAYSA_, Fr("، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «غَيْثٌ»", "; its noun is the hidden «it» — the rain", "; ismi «غَيْثٌ» kelimesine dönen gizli zamir «o»"), CL_HAL("نَبْتَهَا"), Dn("أَوْ نَعْتٌ ثَانٍ لِـ«غَيْثٌ» " + DUR + "؛ وَفَسَّرَهُ الزَّوْزَنِيُّ: وَلَيْسَتِ الرَّوْضَةُ بِمَعْلَمٍ تَطَؤُهُ الدَّوَابُّ وَالنَّاسُ", "or a second na't of «غَيْثٌ» (al-Durra); al-Zawzanī glosses: the meadow is no known place that beasts and men tread", "yahut «غَيْثٌ»ün ikinci na'tı (Dürre); Zevzenî: «çayır, hayvanların ve insanların çiğnediği bilinen bir yer değildir» diye açıklar")),
  n("بِمَعْلَمِ", "malam-ant", BI_ZAID("مَعْلَمِ"), QT, Dn("الْمَعْلَمُ: الْمَوْضِعُ الْمَعْرُوفُ الَّذِي يُقْصَدُ", "الْمَعْلَم: a known place that people make for", "الْمَعْلَم: bilinen, varılıp gidilen yer"), s=[BI, ("مَعْلَمِ", "malam-ant", "noun")])])

# =====================================================================================================================
# Chapter 4 — الرَّوْضَةُ وَذُبَابُهَا، وَسَرْجُ الْفَارِسِ (al-Zawzanī vv. 16–21)
# =====================================================================================================================
def FAS(word):
    """the fa that joins and gives the cause (al-Durra: «حرف عطف وسبب»)"""
    return Fr("الْفَاءُ عَاطِفَةٌ سَبَبِيَّةٌ، وَ" + word + " ", "the fa conjoins and marks a consequence; " + word + " is ", "fâ atıf ve sebep bildirir; " + word + " ", "atf-nasaq")
def JZM_R(word="لَمْ"):
    """a jussive at the rhyme: its sukun gives way to the rawī's kasra"""
    return Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«%s» وَعَلَامَةُ جَزْمِهِ %s" % (word, RAWI_J[0]), "a present verb in jazm by «%s», its sign %s" % (word, RAWI_J[1]), "«%s» ile meczûm muzâri, alâmeti %s" % (word, RAWI_J[2]),
              "nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-qafiya")
LAM_J = Fr("حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ", "the particle that negates, puts in jazm and turns the present to the past", "nefy, cezm ve kalb harfi", "lam-jazim", "nawasib-wa-jawazim-al-mudari")
def SIFA_MD(nth, s="j"):
    """al-Durra's «صفة … للموصوف المحذوف»: the word stands as a na't of a noun left unsaid (the horse, the man)"""
    a, e, t = SGN[s]
    o = {"": ("", "", ""), "ثَانٍ": ("ثَانٍ ", "second ", "ikinci "), "ثَالِثٌ": ("ثَالِثٌ ", "third ", "üçüncü ")}[nth]
    return Fr("نَعْتٌ %sلِمَوْصُوفٍ مَحْذُوفٍ %s" % (o[0], a), "a %sna't of a noun left unsaid, %s" % (o[1], e), "mahzûf bir mevsûfun %sna'tı, %s" % (o[2], t), "naat-sifa", "hadhf-wa-taqdir", *_SG_TAGS.get(s, []))
def NAQ_SUB(who, ref=None):
    """the noun of a كَانَ-sister hidden in it"""
    wj = who in ("أَنَا", "أَنْتَ", "نَحْنُ"); e, t = _WHO[who]
    ar = "، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ %sتَقْدِيرُهُ: %s" % ("وُجُوبًا " if wj else "", who); en = "; its noun is the hidden «%s»" % e; tr = "; ismi %sgizli zamir «%s»" % ("vücûben " if wj else "", t)
    if ref: ar += " يَعُودُ عَلَى " + ref[0]; en += " — " + ref[1]; tr += " — " + ref[2]
    return Fr(ar, en, tr, "kana-wa-akhawatuha")

# ---- v. 16 ----
V(16, "Every first-raining cloud, pure (of cold and wind), poured its bounty upon it, and they left every hollow like a dirham.",
  "Her ilk yağmurlu, (soğuk ve rüzgârdan) arı bulut onun üzerine bol bol yağdı; her çukuru bir dirhem gibi bıraktılar.",
 [v("جَادَتْ", "jada", MADI_F, FAIL_BAD, CL_IST, Dn("أَيْ: أَمْطَرَتْ مَطَرًا جَوْدًا " + DUR, "that is, it rained a heavy, soaking rain (al-Durra)", "yani: bol, her şeyi doyuran bir yağmur yağdırdı (Dürre)"), g=["hollow-verbs"]),
  pp("عَلَيْهِ", "ala", JP("عَلَى", "هِ"), TA("جَادَتْ"), Dn("وَالْهَاءُ تَعُودُ عَلَى النَّبْتِ الْمَذْكُورِ فِي الْبَيْتِ قَبْلَهُ " + DUR, "the pronoun returns to the growth named in the verse before (al-Durra)", "zamir önceki beyitte anılan bitkiye döner (Dürre)"), s=[("عَلَيْ", "ala", "prep"), P("هِ")]),
  n("كُلُّ", "kull", FL(), MDF),
  n("بِكْرٍ", "bikr", MI(), Dn("الْبِكْرُ مِنَ السَّحَابِ: السَّابِقُ مَطَرُهُ، وَالْجَمْعُ الْأَبْكَارُ " + ZAW, "الْبِكْر among clouds: the one whose rain comes first, pl. أَبْكَار (al-Zawzanī)", "bulutlardan الْبِكْر: yağmuru önce gelen, ç. أَبْكَار (Zevzenî)")),
  n("حُرَّةٍ", "hurr", NAT("بِكْرٍ"), Dn("الْحُرَّةُ: الْخَالِصَةُ مِنَ الْبَرَدِ وَالرِّيحِ " + ZAW + "؛ وَيُرْوَى: «جَادَتْ عَلَيْهِ كُلُّ عَيْنٍ ثَرَّةٍ»", "الْحُرَّة: (a cloud) free of hail and wind (al-Zawzanī); another version reads «every copious rain of days»", "الْحُرَّة: doludan ve rüzgârdan arınmış (bulut) (Zevzenî); «her bol, günlerce süren yağmur» diye de rivayet edilir"))],
 [v("فَتَرَكْنَ", "taraka", FAS("تَرَكْنَ"), Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ يَعُودُ عَلَى السَّحَائِبِ الْمَفْهُومَةِ مِنْ «كُلُّ بِكْرٍ»",
       "a past verb built on sukun because the nun of the women is attached; the nun is its doer, in the seat of raf' — the clouds that «every first cloud» means", "nûn-ı nisve bitiştiği için sükûn üzere mebnî mâzî; nûn fâildir, mahallen merfû — «her ilk bulut»tan anlaşılan bulutlara döner", "al-bariz-al-muttasil", "fail"),
     Dn("وَهُوَ هُنَا بِمَعْنَى «صَيَّرَ» فَنَصَبَ مَفْعُولَيْنِ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «جَادَتْ» لَا مَحَلَّ لَهَا " + DUR, "here it means «made», so it takes two objects; the clause is conjoined to «جَادَتْ» and has no seat (al-Durra)", "burada «kıldı» anlamındadır, iki mef'ûl alır; cümle «جَادَتْ»e ma'tûftur, mahalli yoktur (Dürre)", "mafulayn"), s=[FA, ("تَرَكْنَ", "taraka", "verb")]),
  n("كُلَّ", "kull", MF1(), MDF),
  n("قَرَارَةٍ", "qarara", MI(), Dn("الْقَرَارَةُ: الْحُفْرَةُ " + ZAW, "الْقَرَارَة: a hollow in the ground (al-Zawzanī)", "الْقَرَارَة: çukur (Zevzenî)")),
  n("كَالدِّرْهَمِ", "dirham", JN("كَ", "الدِّرْهَمِ"), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ مَفْعُولٍ بِهِ ثَانٍ لِـ«تَرَكْنَ»", "; the jarr phrase hangs on the omitted second object of «تَرَكْنَ»", "; câr-mecrûr «تَرَكْنَ»in mahzûf ikinci mef'ûlüne müteallik", "mafulayn"), QA,
     Dn("وَإِنْ جَعَلْتَ الْكَافَ اسْمًا بِمَعْنَى «مِثْلَ» فَهِيَ الْمَفْعُولُ الثَّانِي " + DUR, "if the kaf is taken as a noun meaning «like», it is itself the second object (al-Durra)", "kâf «مِثْلَ» anlamında isim sayılırsa ikinci mef'ûlün kendisidir (Dürre)"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: الْمُشَبَّهُ كُلُّ قَرَارَةٍ، وَالْمُشَبَّهُ بِهِ الدِّرْهَمُ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ اسْتِدَارَتُهَا بِالْمَاءِ وَبَيَاضُ مَائِهَا وَصَفَاؤُهُ " + ZAW + "، لَمْ يُذْكَرْ فِي الْبَيْتِ فَهُوَ مُجْمَلٌ",
        "here is a tashbih mursal: the thing likened is every hollow; the thing it is likened to, the dirham; the tool, the kaf; the point of likeness — their roundness when full of water and the whiteness and clearness of the water (al-Zawzanī) — is not said in the verse, so the likening is mujmal",
        "burada mürsel teşbîh vardır: müşebbeh her çukur; müşebbehün bih dirhem; edat kâf; vech-i şebeh — suyla dolunca yuvarlaklığı, suyunun beyazlığı ve duruluğu (Zevzenî) — beyitte söylenmediği için mücmeldir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[KA, ("الدِّرْهَمِ", "dirham", "noun")])])

# ---- v. 17 ----
V(17, "Pouring and streaming; and every evening the water runs over it, never cut off.",
  "Döke döke, aka aka; her akşam su üzerinde akar, hiç kesilmez.",
 [n("سَحًّا", "sahh-ant", RO("مَفْعُولٌ مُطْلَقٌ عَامِلُهُ مِنْ غَيْرِ لَفْظِهِ، وَهُوَ «جَادَتْ» فِي الْبَيْتِ قَبْلَهُ", "an absolute object whose governor is of another wording — «جَادَتْ» in the verse before", "lafzı başka olan âmili önceki beyitteki «جَادَتْ» olan mef'ûl-i mutlak", "n", "maful-mutlaq"),
     Dn("أَوْ عَامِلُهُ مَحْذُوفٌ تَقْدِيرُهُ: تَسُحُّ سَحًّا " + DUR + "؛ وَالسَّحُّ: الصَّبُّ وَالِانْصِبَابُ جَمِيعًا " + ZAW, "or its governor is omitted — «it pours a pouring» (al-Durra); السَّحّ: pouring, and pouring down, both (al-Zawzanī)", "yahut âmili mahzûftur: «döker, dökmekle» (Dürre); السَّحّ: hem dökmek hem dökülmek (Zevzenî)", "masdar")),
  n("وَتَسْكَابًا", "taskab-ant", PRE("wa", "تَسْكَابًا"), ATF("سَحًّا", "n"), Dn("فَهُوَ مَفْعُولٌ مُطْلَقٌ أَيْضًا؛ وَالتَّسْكَابُ: السَّكْبُ " + ZAW, "so it too is an absolute object; التَّسْكَاب: pouring (al-Zawzanī)", "o da mef'ûl-i mutlaktır; التَّسْكَاب: dökmek (Zevzenî)", "masdar"), s=[WA, ("تَسْكَابًا", "taskab-ant", "noun")]),
  n("فَكُلَّ", "kull", PRE("fa", "كُلَّ"), ZZ(), MDF, ZT("يَجْرِي"), Dn("أَخَذَ الظَّرْفِيَّةَ مِنَ الْمُضَافِ إِلَيْهِ " + DUR, "it takes its adverbial force from the word it is annexed to (al-Durra)", "zarflığını muzâfun ileyhten almıştır (Dürre)"), s=[FA, ("كُلَّ", "kull", "noun")])  ,
  n("عَشِيَّةٍ", "ashiyya", MI())],
 [v("يَجْرِي", "jara", MUDR("y"), FAIL_BAD, CL(0, "مَعْطُوفَةٌ عَلَى جُمْلَةِ «جَادَتْ»", "is conjoined to the clause of «جَادَتْ»", "«جَادَتْ» cümlesine ma'tûftur")),
  pp("عَلَيْهَا", "ala", JP("عَلَى", "هَا"), TA("يَجْرِي"), s=[("عَلَيْ", "ala", "prep"), P("هَا")]),
  n("الْمَاءُ", "ma-water", FL()),
  pt("لَمْ", "lam-jazim", LAM_J),
  v("يَتَصَرَّمِ", "tasarrama-ant", JZM_R(), HID("هُوَ", ("الْمَاءِ", "the water", "suya")), CL_HAL("الْمَاءُ"),
     Dn("وَقَالَ الدُّرَّةُ: مَجْزُومٌ بِسُكُونٍ مُقَدَّرٍ مَنَعَ مِنْ ظُهُورِهِ الْكَسْرُ الْعَارِضُ لِضَرُورَةِ الشِّعْرِ؛ وَالتَّصَرُّمُ: الِانْقِطَاعُ " + ZAW, "al-Durra puts it: in jazm by a sukun estimated, kept from showing by the kasra the verse brings in; التَّصَرُّم: being cut off (al-Zawzanī)", "Dürre: şiir zarureti olarak gelen kesrenin görünmesine engel olduğu takdîrî sükûnla meczûmdur; التَّصَرُّم: kesilmek (Zevzenî)"), g=["form-v-verbs"])])

# ---- v. 18 ----
V(18, "The flies have it to themselves and do not leave it, humming like the drinker who sings to himself.",
  "Sinekler orayı yalnız kendilerine ayırmıştır; ayrılmazlar, kendi kendine terennüm eden içici gibi vızıldarlar.",
 [v("وَخَلَا", "khala", PRE("wa", "خَلَا"), MADI_A, FAIL_BAD, CL(0, "مَعْطُوفَةٌ عَلَى جُمْلَةِ «جَادَتْ»", "is conjoined to the clause of «جَادَتْ»", "«جَادَتْ» cümlesine ma'tûftur"),
     Dn("أَوْ مُسْتَأْنَفَةٌ " + DUR, "or it opens a new sentence (al-Durra)", "yahut isti'nâfiyyedir (Dürre)"), s=[WA, ("خَلَا", "khala", "verb")]),
  n("الذُّبَابُ", "dhubab", FL(), Dn("وَالْمُرَادُ بِهِ الْجَمْعُ " + DUR, "the many flies are meant (al-Durra)", "çokluk kastedilmiştir (Dürre)")),
  pp("بِهَا", "bi", JP("بِ", "هَا", ("الْبَاءُ", "the ba", "bâ")), TA("خَلَا"), s=[BI, P("هَا")]),
  v("فَلَيْسَ", "laysa", FAS("لَيْسَ"), LAYSA_, NAQ_SUB("هُوَ", ("الذُّبَابِ", "the flies", "sineklere")), CL(0, "مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "is conjoined to the one before", "öncekine ma'tûftur"), s=[FA, ("لَيْسَ", "laysa", "verb")]),
  n("بِبَارِحٍ", "barih-ant", BI_ZAID("بَارِحٍ"), Dn("وَهُوَ اسْمُ فَاعِلٍ مِنْ «بَرِحَ» النَّاقِصَةِ يَعْمَلُ عَمَلَهَا: اسْمُهُ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى الذُّبَابِ وَخَبَرُهُ «غَرِدًا» " + DUR + "؛ وَالْبَرَاحُ: الزَّوَالُ " + ZAW,
       "it is the active participle of the defective بَرِحَ and works as it does: its noun is a hidden pronoun (the flies), its predicate «غَرِدًا» (al-Durra); الْبَرَاح: going away (al-Zawzanī)", "nâkıs «بَرِحَ»in ism-i fâilidir ve onun amelini yapar: ismi sineklere dönen gizli zamir, haberi «غَرِدًا»dır (Dürre); الْبَرَاح: ayrılıp gitmek (Zevzenî)", "ism-fail"), s=[BI, ("بَارِحٍ", "barih-ant", "noun")])],
 [n("غَرِدًا", "gharid-ant", RO("خَبَرُ «بَارِحٍ»", "the predicate of «بَارِحٍ»", "«بَارِحٍ»in haberi", "n", "kana-wa-akhawatuha"), Dn("وَقَالَ التِّبْرِيزِيُّ: حَالٌ مِنَ الذُّبَابِ، وَالْأَوَّلُ أَصَحُّ " + DUR + "؛ وَالتَّغْرِيدُ: التَّصْوِيتُ، وَالنَّعْتُ غَرِدٌ " + ZAW,
       "al-Tibrīzī makes it a hal of the flies — the first is sounder (al-Durra); التَّغْرِيد: making a sound; the adjective is غَرِد (al-Zawzanī)", "Tebrîzî onu sineklerden hâl sayar; birincisi daha sahihtir (Dürre); التَّغْرِيد: ses çıkarmak, sıfatı غَرِد (Zevzenî)")),
  n("كَفِعْلِ", "fil", JN("كَ", "فِعْلِ"), MDF, Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، التَّقْدِيرُ: يَفْعَلُ فِعْلًا مِثْلَ فِعْلِ الشَّارِبِ", "; the jarr phrase hangs on the omitted na't of an omitted absolute object — «it does a doing like the drinker's»", "; câr-mecrûr mahzûf bir mef'ûl-i mutlakın mahzûf na'tına müteallik: «içicinin yaptığı gibi bir yapış yapar»", "maful-mutlaq", "hadhf-wa-taqdir"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شَبَّهَ أَصْوَاتَ الذُّبَابِ بِالْغِنَاءِ — يُصَوِّتْنَ تَصْوِيتَ شَارِبِ الْخَمْرِ حِينَ رَجَّعَ صَوْتَهُ بِالْغِنَاءِ " + ZAW + "؛ فَالْمُشَبَّهُ صَوْتُ الذُّبَابِ، وَالْمُشَبَّهُ بِهِ تَرَنُّمُ الشَّارِبِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ تَرْجِيعُ الصَّوْتِ وَلَمْ يُذْكَرْ",
        "here is a tashbih mursal mujmal: he likens the flies' sounds to singing — they make the sound of a wine-drinker turning his voice over in song (al-Zawzanī); the thing likened is the flies' sound, the thing it is likened to the drinker's singing, the tool the kaf, and the point of likeness — the voice turned over and over — is not said",
        "burada mürsel mücmel teşbîh vardır: sineklerin seslerini şarkıya benzetmiştir — şarap içenin şarkıyla sesini döndürüp tekrarladığı gibi ses çıkarırlar (Zevzenî); müşebbeh sineklerin sesi, müşebbehün bih içicinin terennümü, edat kâf, vech-i şebeh — sesin döndürülüp tekrarlanması — söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[KA, ("فِعْلِ", "fil", "noun")]),
  n("الشَّارِبِ", "sharib", MI(), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ " + DUR + "؛ أَرَادَ شَارِبَ الْخَمْرِ", "the masdar is annexed to its doer (al-Durra); he means the drinker of wine", "masdar fâiline izâfe edilmiştir (Dürre); şarap içeni kastetmiştir", "masdar")),
  n("الْمُتَرَنِّمِ", "mutarannim-ant", SIFA_MD("ثَانٍ"), QA, Dn("التَّقْدِيرُ: الرَّجُلِ الشَّارِبِ الْمُتَرَنِّمِ، وَ«الشَّارِبِ» نَعْتُهُ الْأَوَّلُ " + DUR + "؛ وَالتَّرَنُّمُ: تَرْدِيدُ الصَّوْتِ بِضَرْبٍ مِنَ التَّلْحِينِ " + ZAW,
       "understand «the man, the drinker, the singer», «الشَّارِبِ» being its first na't (al-Durra); التَّرَنُّم: turning the voice over with a kind of melody (al-Zawzanī)", "takdîr: «içici, terennüm eden adam»; «الشَّارِبِ» onun birinci na'tıdır (Dürre); التَّرَنُّم: sesi bir tür nağmeyle tekrarlamak (Zevzenî)", "ism-fail"))])

# ---- v. 19 ----
V(19, "Humming, he rubs one forearm against the other, like the striking of a man with a maimed hand who bends over the fire-sticks.",
  "Vızıldayarak bir kolunu öbür koluna sürter — eli kesik bir adamın, çakmak çubuklarının üzerine eğilip ateş çıkarması gibi.",
 [n("هَزِجًا", "hazij-ant", RO("خَبَرٌ ثَانٍ لِـ«بَارِحٍ» فِي الْبَيْتِ قَبْلَهُ", "a second predicate of «بَارِحٍ» in the verse before", "önceki beyitteki «بَارِحٍ»in ikinci haberi", "n", "kana-wa-akhawatuha"),
     Dn("بِكَسْرِ الزَّايِ؛ وَيُرْوَى بِفَتْحِهَا مَصْدَرًا مَفْعُولًا مُطْلَقًا لِفِعْلٍ مَحْذُوفٍ، وَالْأَوَّلُ أَجْوَدُ " + DUR + "؛ هَزِجًا: مُصَوِّتًا " + ZAW, "with kasra on the zay; it is also read with fatha, a masdar, the absolute object of an omitted verb — the first is better (al-Durra); هَزِجًا: making a sound (al-Zawzanī)", "zây'ın kesresiyle; fethasıyla, mahzûf bir fiilin mef'ûl-i mutlakı olan masdar olarak da rivayet edilir, birincisi daha iyidir (Dürre); هَزِجًا: ses çıkararak (Zevzenî)")),
  v("يَحُكُّ", "hakka-ant", MUDR(), HID("هُوَ", ("الذُّبَابِ", "the fly", "sineğe")), CL_HAL("الذُّبَابُ"), Dn("أَوْ خَبَرٌ ثَالِثٌ لِـ«بَارِحٍ» " + DUR, "or a third predicate of «بَارِحٍ» (al-Durra)", "yahut «بَارِحٍ»in üçüncü haberi (Dürre)"), g=["doubled-verbs"]),
  n("ذِرَاعَهُ", "dhira", MF(), IDF("هُ"), s=[("ذِرَاعَ", "dhira", "noun"), P("هُ")]),
  n("بِذِرَاعِهِ", "dhira", JN("بِ", "ذِرَاعِ"), IDF("هِ"), TA("يَحُكُّ"), s=[BI, ("ذِرَاعِ", "dhira", "noun"), P("هِ")])],
 [n("قَدْحَ", "qadh", RO("مَفْعُولٌ مُطْلَقٌ", "an absolute object", "mef'ûl-i mutlak", "n", "maful-mutlaq"), MDF, Dn("نَابَ عَنِ الْمَصْدَرِ الْمَحْذُوفِ وَصِفَتِهِ، وَالْأَصْلُ: يَحُكُّ ذِرَاعَهُ حَكًّا مِثْلَ قَدْحِ الْمُكِبِّ " + DUR, "it stands for the omitted masdar and its na't: «he rubs his forearm a rubbing like the striking of …» (al-Durra)", "mahzûf masdarın ve sıfatının yerini tutar: «kolunu … çakması gibi bir sürtüşle sürter» (Dürre)", "hadhf-wa-taqdir"),
     Sn("وَفِيهِ تَشْبِيهٌ: شَبَّهَ حَكَّ الذُّبَابِ إِحْدَى ذِرَاعَيْهِ بِالْأُخْرَى بِقَدْحِ رَجُلٍ نَاقِصِ الْيَدِ النَّارَ مِنَ الزَّنْدَيْنِ " + ZAW + "؛ وَالْأَدَاةُ مَحْذُوفَةٌ نَابَ عَنْهَا الْمَصْدَرُ",
        "here is a tashbih: he likens the fly's rubbing of one forearm against the other to a maimed-handed man striking fire from the two fire-sticks (al-Zawzanī); the tool is dropped and the masdar stands in for it",
        "burada teşbîh vardır: sineğin bir kolunu ötekine sürtmesini, eli kesik bir adamın iki çakmak çubuğundan ateş çıkarmasına benzetmiştir (Zevzenî); edat hazfedilmiş, yerini masdar tutmuştur", "tashbih", "arkan-al-tashbih"),
     HD("هُوَ تَشْبِيهٌ مُؤَكَّدٌ — مَا حُذِفَتْ أَدَاتُهُ — وَتَمْثِيلٌ: وَجْهُ الشَّبَهِ هَيْئَةٌ مُنْتَزَعَةٌ مِنْ مُتَعَدِّدٍ، عُضْوٌ يُحَكُّ بِعُضْوٍ حَكًّا مُتَتَابِعًا مَعَ انْكِبَابٍ",
        "it is a tashbih mu'akkad — one whose tool is dropped — and a tamthil: the point of likeness is a figure drawn from several things, a limb rubbed on a limb again and again by one bent over",
        "bu, edatı hazfedilen müekked teşbîh ve temsîldir: vech-i şebeh birden çok şeyden alınmış bir heyettir — eğilmiş birinin bir uzvu öbür uzva art arda sürtmesi", "aqsam-al-tashbih")),
  n("الْمُكِبِّ", "mukibb-ant", MI(), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ الْمُكِبُّ: الْمُقْبِلُ عَلَى الشَّيْءِ " + ZAW, "the masdar is annexed to its doer, and the word is a na't of a noun left unsaid (al-Durra); الْمُكِبّ: one bent over a thing, intent on it (al-Zawzanī)", "masdar fâiline izâfe edilmiştir; kelime mahzûf bir mevsûfun sıfatıdır (Dürre); الْمُكِبّ: bir şeyin üzerine eğilen (Zevzenî)", "ism-fail", "masdar")),
  pp("عَلَى", "ala", HJ),
  n("الزِّنَادِ", "zinad-ant", MJ(), TA("الْمُكِبِّ"), Dn("الزِّنَادُ: مَا تُقْدَحُ بِهِ النَّارُ، جَمْعُ زَنْدٍ", "الزِّنَاد: the sticks fire is struck from, pl. of زَنْد", "الزِّنَاد: ateş çakılan çubuklar, زَنْد'ın cem'i", "jam-taksir")),
  n("الْأَجْذَمِ", "ajdham-ant", SIFA_MD("ثَانٍ"), QA, Dn("وَقِيلَ: نَعْتٌ لِـ«الزِّنَادِ» " + DUR + "؛ الْأَجْذَمُ: النَّاقِصُ الْيَدِ " + ZAW, "it is also said to be a na't of «الزِّنَادِ» (al-Durra); الْأَجْذَم: one whose hand is maimed (al-Zawzanī)", "«الزِّنَادِ»in na'tı olduğu da söylenmiştir (Dürre); الْأَجْذَم: eli eksik (Zevzenî)"))])

# ---- v. 20 ----
V(20, "She passes her evenings and her mornings on the back of a soft cushion, and I pass my nights on the back of a black, bridled horse.",
  "O, akşamlarını ve sabahlarını yumuşak bir minderin sırtında geçirir; ben ise gecelerimi gemli, yağız bir atın sırtında geçiririm.",
 [v("تُمْسِي", "amsa", Fr("فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "a defective present verb, a sister of كَانَ, in raf' by a damma estimated on the ya", "كَانَ'nin kardeşlerinden nâkıs muzâri, yâ üzerinde takdîrî damme ile merfû", "kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs"),
     NAQ_SUB("هِيَ", ("عَبْلَةَ", "ʿAbla", "Able'ye")), CL_IST,
     HD("بَيْنَهُ وَبَيْنَ «تُصْبِحُ» طِبَاقٌ: الْجَمْعُ بَيْنَ مَعْنَيَيْنِ مُتَقَابِلَيْنِ، الْمَسَاءِ وَالصَّبَاحِ", "it makes a tibaq with «تُصْبِحُ»: two opposed meanings, evening and morning, brought together", "«تُصْبِحُ» ile arasında tıbâk vardır: iki karşıt mânâ, akşam ve sabah bir araya getirilmiştir", "tibaq"), g=["form-iv-verbs"]),
  v("وَتُصْبِحُ", "asbaha", PRE("wa", "تُصْبِحُ"), Fr("فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ", "a defective present verb in raf' by the damma", "damme ile merfû nâkıs muzâri", "kana-wa-akhawatuha", "mudari-marfu"), NAQ_SUB("هِيَ"),
     HD("هُوَ الطَّرَفُ الثَّانِي مِنْ طِبَاقِ «تُمْسِي»", "it is the second term of the tibaq with «تُمْسِي»", "«تُمْسِي» ile kurulan tıbâkın ikinci ucudur", "tibaq"), g=["form-iv-verbs"], s=[WA, ("تُصْبِحُ", "asbaha", "verb")]),
  n("فَوْقَ", "fawqa", ZM(), MDF, Dn("وَقَدْ تَنَازَعَهُ الْفِعْلَانِ النَّاقِصَانِ: هُوَ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ لِأَحَدِهِمَا، وَخَبَرُ الْآخَرِ مَحْذُوفٌ — وَالثَّانِي أَوْلَى عِنْدَ الْبَصْرِيِّينَ، وَالْأَوَّلُ عِنْدَ الْكُوفِيِّينَ " + DUR,
       "the two defective verbs contend for it: it hangs on the omitted predicate of one of them, and the other's predicate is omitted — the Basrans prefer the second, the Kufans the first (al-Durra)", "iki nâkıs fiil onun üzerinde tenâzu' eder: birinin mahzûf haberine müteallik olur, ötekinin haberi mahzûftur — Basralılara göre ikincisi, Kûfelilere göre birincisi evlâdır (Dürre)", "tanazu")),
  n("ظَهْرِ", "zahr", MI(), MDF),
  n("حَشِيَّةٍ", "hashiyya-ant", MI(), Dn("الْحَشِيَّةُ مِنَ الثِّيَابِ: مَا حُشِيَ بِقُطْنٍ أَوْ صُوفٍ أَوْ غَيْرِهِمَا، وَالْجَمْعُ الْحَشَايَا " + ZAW, "الْحَشِيَّة: a cloth stuffed with cotton, wool or the like, pl. حَشَايَا (al-Zawzanī)", "الْحَشِيَّة: pamuk, yün vb. ile doldurulmuş kumaş, ç. حَشَايَا (Zevzenî)"),
     Sn("وَكَوْنُهَا فَوْقَ حَشِيَّةٍ كِنَايَةٌ عَنْ تَنَعُّمِهَا، وَبَيْتُوتَتُهُ فَوْقَ فَرَسٍ كِنَايَةٌ عَنْ مُقَاسَاتِهِ الشَّدَائِدَ: «يَقُولُ: هِيَ تَتَنَعَّمُ وَأَنَا أُقَاسِي شَدَائِدَ الْأَسْفَارِ وَالْحُرُوبِ» " + ZAW,
        "her being on a cushion is a kinaya for her life of ease, and his nights on a horse a kinaya for the hardships he bears: «he means: she lives in comfort, and I endure the hardships of journeys and wars» (al-Zawzanī)",
        "onun minder üzerinde olması bolluk içinde yaşamasından, onun at üzerinde gecelemesi çektiği zorluklardan kinâyedir: «Demek ister ki: o nimet içinde yaşar, ben ise yolculukların ve savaşların zorluklarına katlanırım» (Zevzenî)", "kinaya"))],
 [v("وَأَبِيتُ", "bata", PRE("wa", "أَبِيتُ"), Fr("فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَرْفُوعٌ بِالضَّمَّةِ", "a defective present verb, a sister of كَانَ, in raf' by the damma", "كَانَ'nin kardeşlerinden nâkıs muzâri, damme ile merfû", "kana-wa-akhawatuha", "mudari-marfu"), NAQ_SUB("أَنَا"),
     CL(0, "مَعْطُوفَةٌ عَلَى جُمْلَةِ «تُمْسِي»", "is conjoined to the clause of «تُمْسِي»", "«تُمْسِي» cümlesine ma'tûftur"), Sn("وَهُوَ مَوْضِعُ الْكِنَايَةِ الثَّانِيَةِ الْمَذْكُورَةِ عِنْدَ «حَشِيَّةٍ»", "this is where the second kinaya, noted at «حَشِيَّةٍ», lies", "«حَشِيَّةٍ»de anılan ikinci kinâyenin yeri burasıdır", "kinaya"),
     g=["hollow-verbs"], s=[WA, ("أَبِيتُ", "bata", "verb")]),
  n("فَوْقَ", "fawqa", ZM(), MDF, Fr("، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «أَبِيتُ»", ", hanging on the omitted predicate of «أَبِيتُ»", "; «أَبِيتُ»ün mahzûf haberine müteallik")),
  n("سَرَاةِ", "sarat-ant", MI(), MDF, Dn("السَّرَاةُ: أَعْلَى الظَّهْرِ " + ZAW, "السَّرَاة: the top of the back (al-Zawzanī)", "السَّرَاة: sırtın en üstü (Zevzenî)")),
  n("أَدْهَمَ", "adham-ant", MI("jf"), Dn("مُنِعَ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — التَّقْدِيرُ: فَرَسٍ أَدْهَمَ " + DUR + "؛ وَالْأَدْهَمُ: الْأَسْوَدُ",
       "barred from tanwin as an adjective on the pattern أَفْعَل, and a na't of a noun left unsaid — «a black horse» (al-Durra); الْأَدْهَم: black", "sıfat olduğu ve أَفْعَل vezninde bulunduğu için gayr-i munsarif; mahzûf bir mevsûfun sıfatıdır — «yağız bir at» (Dürre); الْأَدْهَم: siyah", "hadhf-wa-taqdir")),
  n("مُلْجَمِ", "muljam", SIFA_MD("ثَانٍ"), QT, Dn("اسْمُ مَفْعُولٍ مِنْ «أَلْجَمَ»: عَلَيْهِ لِجَامُهُ؛ وَطُبِعَ فِي النَّشْرَةِ «مُلجِمِ» بِكَسْرِ الْجِيمِ", "the passive participle of أَلْجَمَ: with its bridle on; the edition prints «مُلجِمِ», with kasra on the jim", "«أَلْجَمَ»den ism-i mef'ûl: gemi takılı; neşirde cîm'in kesresiyle «مُلجِمِ» basılmıştır", "ism-maful"))])

# ---- v. 21 ----
V(21, "And my cushion is a saddle on a horse thick of limb, full in the flanks where the rider's heel strikes, stout where the girth goes.",
  "Benim minderim ise, kalın bacaklı, mahmuz vurulan böğürleri dolgun, kolan yeri besili bir atın üstündeki eyerdir.",
 [n("وَحَشِيَّتِي", "hashiyya-ant", PRE("wa-ist", "حَشِيَّةُ"), MB("rM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"),
     Sn("وَهُوَ كِنَايَةٌ عَنْ مُلَازَمَتِهِ رُكُوبَ الْخَيْلِ: «يُرِيدُ أَنَّهُ يَسْتَوْطِئُ سَرْجَ الْفَرَسِ كَمَا يَسْتَوْطِئُ غَيْرُهُ الْحَشِيَّةَ، وَيُلَازِمُ رُكُوبَ الْخَيْلِ لُزُومَ غَيْرِهِ الْجُلُوسَ عَلَى الْحَشِيَّةِ» " + ZAW,
        "it is a kinaya for his never leaving the horse's back: «he means that he finds the saddle as soft as another finds a cushion, and keeps to riding as another keeps to sitting on a cushion» (al-Zawzanī)",
        "atın sırtından hiç ayrılmamasından kinâyedir: «Başkası minderi nasıl yumuşak bulursa o da eyeri öyle yumuşak bulur; başkası minderde oturmaya nasıl devam ederse o da ata binmeye öyle devam eder demek ister» (Zevzenî)", "kinaya"),
     s=[WA, ("حَشِيَّتِ", "hashiyya-ant", "noun"), P("ي")]),
  n("سَرْجٌ", "sarj", KH(), CL(0, "الِاسْمِيَّةُ مُسْتَأْنَفَةٌ", "(the nominal one) opens a new sentence", "(isim cümlesi) isti'nâfiyyedir")),
  pp("عَلَى", "ala", HJ),
  n("عَبْلِ", "abl-ant", MJ(), MDF, TAM("naat", "سَرْجٌ"), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — فَرَسٍ — مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا " + DUR + "؛ الْعَبْلُ: الْغَلِيظُ " + ZAW,
       "it is a na't of a noun left unsaid — a horse — the sifa mushabbaha annexed to its own doer (al-Durra); الْعَبْل: thick (al-Zawzanī)", "mahzûf bir mevsûfun — atın — sıfatıdır; sıfat-ı müşebbehe fâiline izâfe edilmiştir (Dürre); الْعَبْل: kalın (Zevzenî)", "sifa-mushabbaha", "hadhf-wa-taqdir")),
  n("الشَّوَى", "shawan-ant", MI("jA"), Dn("الشَّوَى: الْأَطْرَافُ وَالْقَوَائِمُ " + ZAW, "الشَّوَى: the extremities, the legs (al-Zawzanī)", "الشَّوَى: uzuvlar, bacaklar (Zevzenî)"))],
 [n("نَهْدٍ", "nahd-ant", SIFA_MD("ثَانٍ"), Dn("النَّهْدُ: الضَّخْمُ الْمُشْرِفُ " + ZAW, "النَّهْد: big and tall (al-Zawzanī)", "النَّهْد: iri ve yüksek (Zevzenî)", "sifa-mushabbaha")),
  n("مَرَاكِلُهُ", "markal-ant", RO("فَاعِلٌ لِلصِّفَةِ الْمُشَبَّهَةِ «نَهْدٍ»", "the doer of the sifa mushabbaha «نَهْدٍ»", "«نَهْدٍ» sıfat-ı müşebbehesinin fâili", "r", "fail", "sifa-mushabbaha"), IDF("هُ"),
     Dn("جَمْعُ مَرْكَلٍ، وَهُوَ مَوْضِعُ الرَّكْلِ، وَالرَّكْلُ: الضَّرْبُ بِالرِّجْلِ " + ZAW, "the plural of مَرْكَل, the place where the heel strikes — الرَّكْل is striking with the foot (al-Zawzanī)", "مَرْكَل'in cem'i: tekmenin (mahmuzun) vurulduğu yer; الرَّكْل: ayakla vurmak (Zevzenî)", "jam-taksir"), s=[("مَرَاكِلُ", "markal-ant", "noun"), P("هُ")]),
  n("نَبِيلِ", "nabil-ant", SIFA_MD("ثَالِثٌ"), MDF, Dn("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا " + DUR + "؛ النَّبِيلُ: السَّمِينُ " + ZAW, "the sifa mushabbaha annexed to its own doer (al-Durra); النَّبِيل: fat, stout (al-Zawzanī)", "sıfat-ı müşebbehe fâiline izâfe edilmiştir (Dürre); النَّبِيل: besili, semiz (Zevzenî)", "sifa-mushabbaha")),
  n("الْمَحْزِمِ", "mahzim-ant", MI(), QA, Dn("الْمَحْزِمُ: مَوْضِعُ الْحِزَامِ مِنْ جَسَدِ الدَّابَّةِ " + ZAW, "الْمَحْزِم: the place of the girth on the beast's body (al-Zawzanī)", "الْمَحْزِم: hayvanın gövdesinde kolanın yeri (Zevzenî)"))])

# =====================================================================================================================
# Chapter 5 — النَّاقَةُ وَالظَّلِيمُ (al-Zawzanī vv. 22–27)
# =====================================================================================================================
LAM_PRN = ("اللَّامُ", "the lam", "lâm")
OSTRICH = ("الظَّلِيمِ", "the ostrich", "devekuşuna")
CAMEL = ("النَّاقَةِ", "the she-camel", "dişi deveye")

# ---- v. 22 ----
V(22, "Will a Shadanī she-camel bring me to her dwelling — one cursed with an udder robbed of its milk and cut off?",
  "Beni onun yurduna Şedenî bir dişi deve ulaştırır mı — sütten mahrum, kesik bir memeyle lanetlenmiş bir deve?",
 [pt("هَلْ", "hal-istifham", Fr("حَرْفُ اسْتِفْهَامٍ", "the particle of question", "istifhâm harfi", "al-istifham"),
     Sn("وَالِاسْتِفْهَامُ هُنَا مُفِيدٌ لِلتَّمَنِّي " + DUR, "the question here carries a wish (al-Durra)", "istifhâm burada temennî ifade eder (Dürre)", "khuruj-al-istifham", "insha-wa-tamanni")),
  v("تُبْلِغَنِّي", "ablagha", Fr("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ",
       "a present verb built on fatha because the heavy nun of emphasis is attached; the ya is its first object, in the seat of nasb", "ağır te'kîd nûnu bitiştiği için fetha üzere mebnî muzâri; yâ birinci mef'ûldür, mahallen mansûb", "nun-tawkid", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"),
     FAIL_BAD, CL_IST, Dn("أَوْ هِيَ النُّونُ الْخَفِيفَةُ أُدْغِمَتْ فِيهَا نُونُ الْوِقَايَةِ " + DUR, "or it is the light nun, with the nun of protection merged into it (al-Durra)", "yahut hafif nûndur, vikâye nûnu ona idgâm edilmiştir (Dürre)"),
     g=["form-iv-verbs"], s=[("تُبْلِغَنِّ", "ablagha", "verb"), P("ي")]),
  n("دَارَهَا", "dar", MF2(), IDF("هَا"), s=[("دَارَ", "dar", "noun"), P("هَا")]),
  n("شَدَنِيَّةٌ", "shadaniyya-ant", FL(), Dn("وَهُوَ فِي الْأَصْلِ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — نَاقَةٌ — " + DUR + "؛ شَدَنٌ: أَرْضٌ أَوْ قَبِيلَةٌ تُنْسَبُ الْإِبِلُ إِلَيْهَا " + ZAW,
       "it is in origin a na't of a noun left unsaid — a she-camel (al-Durra); Shadan is a land or a tribe camels are named after (al-Zawzanī)", "aslında mahzûf bir mevsûfun — dişi devenin — sıfatıdır (Dürre); Şeden, develerin nispet edildiği bir yer ya da kabiledir (Zevzenî)", "hadhf-wa-taqdir"))],
 [v("لُعِنَتْ", "laana", Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "a past verb in the passive, built on fatha; the ta marks the feminine", "fetha üzere mebnî meçhul mâzî; tâ te'nîs içindir", "al-majhul-fil-kafiya"),
     HID("هِيَ", CAMEL, naib=True), CL("r", "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ", "a second na't of the noun left unsaid", "mahzûf mevsûfun ikinci na'tı", "jumla-sifa"),
     Sn("وَفِيهِ كِنَايَةٌ عَنْ قُوَّتِهَا: دُعِيَ عَلَيْهَا بِأَنْ تُحْرَمَ اللَّبَنَ «أَيْ لِبُعْدِ عَهْدِهَا بِاللِّقَاحِ … وَإِنَّمَا شَرَطَ هٰذَا لِتَكُونَ أَقْوَى وَأَسْمَنَ وَأَصْبَرَ عَلَى مُعَانَاةِ شَدَائِدِ الْأَسْفَارِ، لِأَنَّ كَثْرَةَ الْحَمْلِ وَالْوِلَادَةِ تُكْسِبُهَا ضَعْفًا وَهُزَالًا» " + ZAW,
        "here is a kinaya for her strength: she is cursed to be robbed of milk — «that is, it is long since she conceived … he makes this a condition so that she be stronger, fatter and more patient of the hardships of travel, for much bearing and foaling makes a camel weak and lean» (al-Zawzanī)",
        "burada gücünden kinâye vardır: sütten mahrum kalmakla lanetlenmiştir — «yani gebe kalmasının üzerinden uzun zaman geçmiştir … bunu şart koşar ki daha güçlü, daha semiz ve yolculuk zorluklarına daha dayanıklı olsun; çok gebelik ve doğum deveyi zayıf düşürür» (Zevzenî)", "kinaya")),
  n("بِمَحْرُومِ", "mahrum", JN("بِ", "مَحْرُومِ"), MDF, TA("لُعِنَتْ"), s=[BI, ("مَحْرُومِ", "mahrum", "noun")]),
  n("الشَّرَابِ", "sharab", MI(), Dn("أَرَادَ بِالشَّرَابِ اللَّبَنَ " + ZAW, "by «drink» he means milk (al-Zawzanī)", "«içecek» ile sütü kastetmiştir (Zevzenî)")),
  n("مُصَرَّمِ", "musarram-ant", NAT("مَحْرُومِ الشَّرَابِ"), QT, Dn("التَّصْرِيمُ: الْقَطْعُ " + ZAW, "التَّصْرِيم: cutting off (al-Zawzanī)", "التَّصْرِيم: kesmek (Zevzenî)", "ism-maful"))])

# ---- v. 23 ----
V(23, "Swinging her tail after the night journey, swaggering, she breaks the hillocks with the tread of a crushing hoof.",
  "Gece yolculuğunun ardından kuyruğunu sallayan, salına salına yürüyen (bir deve); ezen bir tabanın basışıyla tepecikleri kırar.",
 [n("خَطَّارَةٌ", "khattara-ant", NAT("شَدَنِيَّةٌ", "r", "آخَرُ"), Dn("وَيَجُوزُ أَنْ يَكُونَ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ عَلَى الْقَطْعِ " + DUR + "؛ صِيغَةُ مُبَالَغَةٍ مِنْ «خَطَرَ الْبَعِيرُ بِذَنَبِهِ» إِذَا شَالَ بِهِ " + ZAW,
       "it may also be the khabar of an omitted mubtada, cut off from what goes before (al-Durra); a form of intensity from «the camel swung its tail», when it raises it (al-Zawzanī)", "kat' yoluyla mahzûf bir mübtedânın haberi de olabilir (Dürre); «deve kuyruğunu kaldırıp salladı» sözünden mübalağa sîgası (Zevzenî)", "sighat-mubalagha")),
  n("غِبَّ", "ghibb-ant", ZZ(), MDF, ZT("خَطَّارَةٌ"), Dn("غِبُّ كُلِّ شَيْءٍ: بَعْدَهُ " + DUR, "the غِبّ of anything is what comes after it (al-Durra)", "her şeyin غِبّ'ı ondan sonrasıdır (Dürre)")),
  n("السُّرَى", "sura-ant", MI("jA"), Dn("السُّرَى: سَيْرُ اللَّيْلِ — «بَعْدَمَا سَارَتِ اللَّيْلَ كُلَّهُ» " + ZAW, "السُّرَى: travelling by night — «after she has travelled the whole night» (al-Zawzanī)", "السُّرَى: gece yürüyüşü — «bütün gece yürüdükten sonra» (Zevzenî)")),
  n("زَيَّافَةٌ", "zayyafa-ant", NAT("شَدَنِيَّةٌ", "r", "آخَرُ"), Dn("وَيَجُوزُ فِيهِ مَا جَازَ فِي «خَطَّارَةٌ» " + DUR + "؛ وَالزَّيَفُ: التَّبَخْتُرُ " + ZAW, "the same two readings as «خَطَّارَةٌ» (al-Durra); الزَّيَف: swaggering (al-Zawzanī)", "«خَطَّارَةٌ»de câiz olan burada da câizdir (Dürre); الزَّيَف: salınarak yürümek (Zevzenî)", "sighat-mubalagha"))],
 [v("تَطِسُ", "watasa-ant", MUDR(), HID("هِيَ", CAMEL), CL_IST, Dn("بِالْإِعْرَاضِ عَمَّا قَبْلَهَا، أَوْ فِي مَحَلِّ رَفْعٍ نَعْتٌ آخَرُ لِلنَّاقَةِ " + DUR + "؛ الْوَطْسُ: الْكَسْرُ " + ZAW, "taken apart from what goes before; or a further na't of the she-camel, in the seat of raf' (al-Durra); الْوَطْس: breaking (al-Zawzanī)", "öncesinden ayrı tutulursa; yahut deveye bir başka na't olarak mahallen merfû (Dürre); الْوَطْس: kırmak (Zevzenî)"), g=["mithal-verbs"]),
  n("الْإِكَامَ", "akama-ant", MF(), Dn("جَمْعُ أَكَمَةٍ: التَّلُّ الصَّغِيرُ", "the plural of أَكَمَة, a hillock", "أَكَمَة'nin cem'i: tepecik", "jam-taksir")),
  n("بِوَخْذِ", "wakhdh-ant", JN("بِ", "وَخْذِ"), MDF, TA("تَطِسُ"), Dn("كَذَا طُبِعَ بِالذَّالِ؛ وَفِي الشَّرْحِ: «وَيُرْوَى: بِذَاتِ خُفٍّ … وَيُرْوَى: بِوَخْدِ خُفٍّ، الْوَخْدُ وَالْوَخَدَانُ: السَّيْرُ السَّرِيعُ» " + ZAW + "، وَعِنْدَ الدُّرَّةِ «بِوَخْدِ»",
       "so printed, with dhal; the commentary adds: «it is also related ‹with a foot that has a hoof› … and ‹with the swift pace of a hoof›; الْوَخْد is a swift pace» (al-Zawzanī); al-Durra reads بِوَخْدِ", "zâl ile böyle basılmıştır; şerhte: «‹tabanlı bir ayakla› … ve ‹tabanın hızlı yürüyüşüyle› diye de rivayet edilir; الْوَخْد hızlı yürüyüştür» (Zevzenî); Dürre «بِوَخْدِ» okur"), s=[BI, ("وَخْذِ", "wakhdh-ant", "noun")]),
  n("خُفٍّ", "khuff", MI()),
  n("مِيثَمِ", "maytham-ant", NAT("خُفٍّ"), QT, Dn("الْمِيثَمُ لِلْمُبَالَغَةِ، كَأَنَّهُ آلَةُ الْوَثْمِ، وَالْوَثْمُ: الْكَسْرُ " + ZAW, "مِيثَم is for intensity — as if the hoof were the very tool of crushing; الْوَثْم is breaking (al-Zawzanī)", "مِيثَم mübalağa içindir — taban sanki ezme aletidir; الْوَثْم: kırmak (Zevzenî)", "sighat-mubalagha"))])

# ---- v. 24 ----
V(24, "It is as if, at evening, she breaks the hillocks with one whose toe-pads are close together, earless — an ostrich.",
  "Sanki akşamleyin tepecikleri, parmak tabanları birbirine yakın, kulaksız biriyle — bir erkek devekuşuyla — kırıyor.",
 [pt("وَكَأَنَّمَا", "ka-annama", PRE("wa-ist", "كَأَنَّمَا"), Fr("حَرْفُ تَشْبِيهٍ كَفَّتْهُ «مَا» الْكَافَّةُ عَنِ الْعَمَلِ", "the particle of likening, kept from governing by the restraining مَا", "kâffe «mâ» ile amelden alıkonmuş teşbîh harfi", "innama-kaffa", "inna-wa-akhawatuha"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: «شَبَّهَهَا فِي سُرْعَةِ سَيْرِهَا بَعْدَ سُرَى لَيْلَةٍ وَوَصْلِ سَيْرِ يَوْمٍ بِهِ بِسُرْعَةِ سَيْرِ الظَّلِيمِ» " + ZAW + "؛ فَالْمُشَبَّهُ النَّاقَةُ، وَالْمُشَبَّهُ بِهِ الظَّلِيمُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ السُّرْعَةُ وَلَمْ يُذْكَرْ",
        "here is a tashbih mursal: «he likens her, in the speed of her going after a night's journey joined to a day's, to the speed of the ostrich» (al-Zawzanī); the thing likened is the she-camel, the thing it is likened to the ostrich, the tool كَأَنَّ, and the point of likeness — speed — is not said",
        "burada mürsel teşbîh vardır: «bir gecelik yürüyüşe bir günlük yürüyüş eklendikten sonraki hızında onu erkek devekuşunun hızına benzetmiştir» (Zevzenî); müşebbeh dişi deve, müşebbehün bih devekuşu, edat «كَأَنَّ», vech-i şebeh — hız — söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     HD("كِنَايَةٌ عَنْ مَوْصُوفٍ: ذَكَرَ الظَّلِيمَ بِصِفَاتٍ تَجْتَمِعُ لَهُ — «قَرِيبِ بَيْنِ الْمَنْسَمَيْنِ مُصَلَّمِ» — وَلَمْ يُسَمِّهِ؛ وَالْمَطْلُوبُ بِهَا غَيْرُ صِفَةٍ وَلَا نِسْبَةٍ",
        "a kinaya for a thing described: he names the ostrich only by attributes that meet in it — «close-toed, earless» — and never by its name; what is sought by it is neither an attribute nor an attribution",
        "mevsûftan kinâye vardır: devekuşunu adını anmadan, onda bir araya gelen sıfatlarla — «parmak tabanları yakın, kulaksız» — anmıştır; bununla istenen ne bir sıfat ne bir nisbettir", "kinaya", "aqsam-al-kinaya"),
     s=[WA, ("كَأَنَّمَا", "ka-annama", "part")]),
  v("تَطِسُ", "watasa-ant", MUDR(), HID("هِيَ", CAMEL), CL_IST, g=["mithal-verbs"]),
  n("الْإِكَامَ", "akama-ant", MF()),
  n("عَشِيَّةً", "ashiyya", ZZ(), ZT("تَطِسُ"), Dn("أَيْ: عَشِيَّةً بَعْدَ سُرَى اللَّيْلِ وَسَيْرِ النَّهَارِ " + ZAW, "that is, at evening, after the night's journey and the day's march (al-Zawzanī)", "yani: gece yürüyüşünden ve gündüz yolculuğundan sonra akşamleyin (Zevzenî)"))],
 [n("بِقَرِيبِ", "qarib", JN("بِ", "قَرِيبِ"), MDF, TA("تَطِسُ"), Dn("وَ«قَرِيبِ» صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: ظَلِيمٍ " + DUR, "«قَرِيبِ» is a na't of a noun left unsaid — an ostrich (al-Durra)", "«قَرِيبِ», mahzûf bir mevsûfun — devekuşunun — sıfatıdır (Dürre)", "hadhf-wa-taqdir"), s=[BI, ("قَرِيبِ", "qarib", "noun")]),
  n("بَيْنِ", "bayna", MI(), MDF, Dn("قَالَ الدُّرَّةُ: «قَرِيبٌ مُضَافٌ وَبَيْنُ مُضَافٌ إِلَيْهِ»؛ وَطُبِعَ فِي النَّشْرَةِ بِفَتْحِ النُّونِ", "al-Durra: «قَرِيب is annexed and بَيْن is its second term»; the edition prints it with fatha on the nun", "Dürre: «قَرِيب muzâf, بَيْن muzâfun ileyhtir»; neşirde nûn'un fethasıyla basılmıştır")),
  n("الْمَنْسَمَيْنِ", "mansim", MI("jD"), Dn("الْمَنْسِمُ: طَرَفُ خُفِّ الْبَعِيرِ وَالنَّعَامِ؛ كَذَا طُبِعَ بِفَتْحِ السِّينِ", "الْمَنْسِم: the tip of the foot of a camel or an ostrich; so printed, with fatha on the sin", "الْمَنْسِم: devenin ve devekuşunun ayak ucu; sîn'in fethasıyla böyle basılmıştır")),
  n("مُصَلَّمِ", "musallam-ant", SIFA_MD("ثَانٍ"), QT, Dn("وَالصِّفَةُ الْأُولَى «قَرِيبِ» " + DUR + "؛ «الْمُصَلَّمُ مِنْ أَوْصَافِ الظَّلِيمِ لِأَنَّهُ لَا أُذُنَ لَهُ، وَالصَّلْمُ: الِاسْتِئْصَالُ، كَأَنَّ أُذُنَهُ اسْتُؤْصِلَتْ» " + ZAW,
       "the first na't is «قَرِيبِ» (al-Durra); «الْمُصَلَّم is said of the ostrich, which has no ears — الصَّلْم is cutting off at the root, as if its ears had been cut away» (al-Zawzanī)", "birinci sıfat «قَرِيبِ»tir (Dürre); «الْمُصَلَّم devekuşunun sıfatlarındandır, çünkü kulağı yoktur; الصَّلْم kökünden kesmektir, sanki kulağı kökünden kesilmiştir» (Zevzenî)", "ism-maful"))])

# ---- v. 25 ----
V(25, "To him the young ostriches gather, as Yemeni herds gather to a mute, outlandish herdsman.",
  "Devekuşu yavruları ona sığınır; tıpkı Yemen develerinin, dili dönmeyen yabancı bir çobana sığındığı gibi.",
 [v("تَأْوِي", "awa-shelter", MUDR("y"), FAIL_BAD, CL_IST, g=["naqis-verbs"]),
  pp("لَهُ", "li", JP("لَ", "هُ", LAM_PRN), TA("تَأْوِي"), Dn("وَحَقُّهُ أَنْ يُوصَلَ بِـ«إِلَى»: أَوَيْتُ إِلَيْهِ، «وَإِنَّمَا وَصَلَهَا بِاللَّامِ لِأَنَّهُ أَرَادَ: تَأْوِي إِلَيْهِ قُلُصٌ لَهُ» " + ZAW, "the verb is properly joined with إِلَى; «he joins it with the lam because he means: young ostriches of his own gather to him» (al-Zawzanī)", "fiil aslında «إِلَى» ile kullanılır; «lâm ile kullanmıştır, çünkü ‹kendisine ait yavrular ona sığınır› demek ister» (Zevzenî)"), s=[("لَ", "li", "prep"), P("هُ")]),
  n("قُلُصُ", "qalus-ant", FL(), MDF, Dn("«الْقَلُوصُ مِنَ الْإِبِلِ وَالنَّعَامِ بِمَنْزِلَةِ الْجَارِيَةِ مِنَ النَّاسِ، وَالْجَمْعُ قُلُصٌ وَقَلَائِصُ» " + ZAW, "«the قَلُوص among camels and ostriches is as the young girl among people; pl. قُلُص and قَلَائِص» (al-Zawzanī)", "«deve ve devekuşlarında قَلُوص, insanlardaki genç kız gibidir; ç. قُلُص ve قَلَائِص» (Zevzenî)", "jam-taksir")),
  n("النَّعَامِ", "naam-ant", MI()),
  pt("كَمَا", "kama", Fr("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«مَا» حَرْفٌ مَصْدَرِيٌّ", "the kaf is a jarr letter of likening, and مَا is the particle that makes a masdar", "kâf teşbîh bildiren cer harfi, «mâ» masdar harfi", "huruf-jarr"),
     Dn("وَ«مَا» وَ«أَوَتْ» فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ: «تَأْوِي لَهُ إِيوَاءً كَإِيوَاءِ حِزَقٍ» " + DUR, "مَا with «أَوَتْ» makes a masdar in jarr by the kaf, and the phrase hangs on the omitted na't of an omitted absolute object: «they gather to him a gathering like the gathering of herds» (al-Durra)", "«mâ» ile «أَوَتْ» kâf ile mecrûr bir masdar te'vîlindedir; câr-mecrûr mahzûf bir mef'ûl-i mutlakın mahzûf na'tına müteallik: «sürülerin sığınışı gibi bir sığınışla ona sığınırlar» (Dürre)", "an-masdariyya", "maful-mutlaq"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: الْمُشَبَّهُ أُوِيُّ صِغَارِ النَّعَامِ إِلَى الظَّلِيمِ، وَالْمُشَبَّهُ بِهِ أُوِيُّ الْإِبِلِ الْيَمَانِيَةِ إِلَى رَاعِيهَا، وَالْأَدَاةُ الْكَافُ؛ قَالَ الزَّوْزَنِيُّ: «شَبَّهَ الظَّلِيمَ فِي سَوَادِهِ بِهٰذَا الرَّاعِي الْحَبَشِيِّ، وَقُلُصَ النَّعَامِ بِإِبِلٍ يَمَانِيَةٍ … وَوَصَفَهُ بِالْعِيِّ وَالْعُجْمَةِ لِأَنَّ الظَّلِيمَ لَا نُطْقَ لَهُ»",
        "here is a tashbih mursal: the thing likened is the young ostriches gathering to the ostrich; the thing it is likened to, Yemeni camels gathering to their herdsman; the tool, the kaf. Al-Zawzanī: «he likens the ostrich in its blackness to this Abyssinian herdsman, and the young ostriches to Yemeni camels … and calls him mute and outlandish because the ostrich has no speech»",
        "burada mürsel teşbîh vardır: müşebbeh devekuşu yavrularının erkek devekuşuna sığınması; müşebbehün bih Yemen develerinin çobanlarına sığınması; edat kâf. Zevzenî: «Erkek devekuşunu siyahlığında bu Habeşli çobana, yavruları Yemen develerine benzetmiştir … onu dili dönmez ve yabancı diye nitelemiştir, çünkü devekuşunun konuşması yoktur»", "tashbih", "arkan-al-tashbih"),
     s=[KA, ("مَا", "ma-masdariyya", "part")])],
 [v("أَوَتْ", "awa-shelter", Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ", "a past verb built on a fatha estimated on the alif, dropped where two quiescents met; the ta marks the feminine", "iki sâkin buluştuğu için düşen elif üzerinde takdîrî fetha ile mebnî mâzî; tâ te'nîs içindir", "naqis-verbs"), FAIL_BAD),
  n("حِزَقٌ", "hizqa-ant", FL(), Dn("«الْحِزَقُ: الْجَمَاعَاتُ، وَالْوَاحِدَةُ حِزْقَةٌ» " + ZAW, "«الْحِزَق: groups, herds; sing. حِزْقَة» (al-Zawzanī)", "«الْحِزَق: topluluklar, sürüler; tekili حِزْقَة» (Zevzenî)", "jam-taksir")),
  n("يَمَانِيَةٌ", "yamanin", NAT("حِزَقٌ", "r"), Dn("أَيْ: إِبِلٌ يَمَانِيَةٌ، «لِأَنَّ السَّوَادَ فِي إِبِلِ الْيَمَانِيِّينَ أَكْثَرُ» " + ZAW, "that is, Yemeni camels — «for blackness is commoner among the camels of the Yemenis» (al-Zawzanī)", "yani Yemen develeri — «çünkü siyahlık Yemenlilerin develerinde daha çoktur» (Zevzenî)")),
  n("لِأَعْجَمَ", "ajam", JN("لِ", "أَعْجَمَ", "jf"), TA("أَوَتْ"), Dn("مُنِعَ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ «أَرَادَ بِالْأَعْجَمِ الْحَبَشِيَّ» " + ZAW, "a diptote, an adjective on أَفْعَل, and a na't of a noun left unsaid (al-Durra); «by the outlandish one he means an Abyssinian» (al-Zawzanī)", "sıfat ve أَفْعَل vezni sebebiyle gayr-i munsarif; mahzûf bir mevsûfun sıfatı (Dürre); «أَعْجَم ile Habeşliyi kastetmiştir» (Zevzenî)", "mamnu-min-sarf", "hadhf-wa-taqdir"), s=[LI, ("أَعْجَمَ", "ajam", "noun")]),
  n("طِمْطِمِ", "timtim-ant", SIFA_MD("ثَانٍ"), QT, Dn("«الطِّمْطِمُ: الْعَيِيُّ الَّذِي لَا يُفْصِحُ» " + ZAW, "«الطِّمْطِم: the tongue-tied man who cannot speak plainly» (al-Zawzanī)", "«الطِّمْطِم: açık konuşamayan, dili tutuk kimse» (Zevzenî)"))])

# ---- v. 26 ----
V(26, "They follow the top of his head, and he is like a women's litter on a raised frame, set up as a tent for them.",
  "Onun başının tepesini izlerler; o ise, onlar için çadır gibi kurulmuş, yüksek bir sedir üzerindeki kadın hevdecine benzer.",
 [v("يَتْبَعْنَ", "tabia-follow", NISWA, CL_IST, Sn("وَهُوَ كِنَايَةٌ عَنْ مُلَازَمَتِهِ: «أَيْ جَعَلَتْهُ نُصْبَ أَعْيُنِهَا لَا تَنْحَرِفُ عَنْهُ» " + ZAW, "it is a kinaya for keeping close to him: «that is, they keep him before their eyes and never turn aside from him» (al-Zawzanī)", "ondan ayrılmamaktan kinâyedir: «yani onu gözlerinin önünde tutar, ondan sapmazlar» (Zevzenî)", "kinaya"), g=["thulathi-mujarrad-babs"]),
  n("قُلَّةَ", "qulla-ant", MF(), MDF, Dn("قُلَّةُ الرَّأْسِ: أَعْلَاهُ " + ZAW, "the قُلَّة of the head is its top (al-Zawzanī)", "başın قُلَّة'si tepesidir (Zevzenî)")),
  n("رَأْسِهِ", "ras", MI(), IDF("هِ"), s=[("رَأْسِ", "ras", "noun"), P("هِ")]),
  pt("وَكَأَنَّهُ", "kaanna", PRE("wa-hal", "كَأَنَّ"), KAANNA_, Fr("، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the attached هُ is its noun, in the seat of nasb", "; bitişik هُ ismidir, mahallen mansûb", "al-bariz-al-muttasil"),
     CL("n", "حَالٌ مِنَ الْهَاءِ فِي «رَأْسِهِ»", "a hal of the pronoun in «رَأْسِهِ»", "«رَأْسِهِ»deki zamirden hâl", "al-hal-jumla-wa-rabituha"), Dn("وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ " + DUR, "the links are the waw and the pronoun (al-Durra)", "râbıt vâv ve zamirdir (Dürre)"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: «شَبَّهَ خَلْقَهُ بِمَرْكَبٍ مِنْ مَرَاكِبِ النِّسَاءِ جُعِلَ كَالْخَيْمَةِ فَوْقَ مَكَانٍ مُرْتَفِعٍ» " + ZAW + "؛ فَالْمُشَبَّهُ الظَّلِيمُ، وَالْمُشَبَّهُ بِهِ الْحِدْجُ عَلَى النَّعْشِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ لَمْ يُذْكَرْ",
        "here is a tashbih mursal mujmal: «he likens its build to a women's litter made like a tent on a raised place» (al-Zawzanī); the thing likened is the ostrich, the thing it is likened to the litter on its frame, the tool كَأَنَّ, and the point of likeness is not said",
        "burada mürsel mücmel teşbîh vardır: «yaratılışını, yüksek bir yerin üstünde çadır gibi kurulmuş kadın binitlerinden birine benzetmiştir» (Zevzenî); müşebbeh devekuşu, müşebbehün bih sedir üzerindeki hevdec, edat «كَأَنَّ», vech-i şebeh söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[WA, ("كَأَنَّ", "kaanna", "part"), P("هُ")])],
 [n("حِدْجٌ", "hidj-ant", KH_K(), Dn("«الْحِدْجُ: مَرْكَبٌ مِنْ مَرَاكِبِ النِّسَاءِ» " + ZAW + "؛ وَعِنْدَ الدُّرَّةِ «حَرَجٌ»", "«الْحِدْج: one of the litters women ride in» (al-Zawzanī); al-Durra reads حَرَج", "«الْحِدْج: kadın binitlerinden biri» (Zevzenî); Dürre «حَرَجٌ» okur")),
  pp("عَلَى", "ala", HJ),
  n("نَعْشٍ", "nash-ant", MJ(), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُخَيَّمِ» بَعْدَهُمَا", "; the jarr phrase hangs on «مُخَيَّمِ» after it", "; câr-mecrûr sonraki «مُخَيَّمِ»e müteallik"), Dn("«النَّعْشُ: الشَّيْءُ الْمَرْفُوعُ، وَالنَّعْشُ بِمَعْنَى الْمَنْعُوشِ» " + ZAW, "«النَّعْش: a thing raised up — النَّعْش in the sense of what is raised» (al-Zawzanī)", "«النَّعْش: yükseltilmiş şey; mef'ûl anlamında» (Zevzenî)")),
  pp("لَهُنَّ", "li", JP("لَ", "هُنَّ", LAM_PRN), TA("مُخَيَّمِ"), s=[("لَ", "li", "prep"), P("هُنَّ")]),
  n("مُخَيَّمِ", "mukhayyam-ant", NAT("نَعْشٍ"), Fr("، وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ", "; its deputy doer is a pronoun hidden in it", "; nâib-i fâili onda gizli zamirdir", "naib-al-fail"), QT, Dn("«الْمُخَيَّمُ: الْمَجْعُولُ خَيْمَةً» " + ZAW, "«الْمُخَيَّم: made into a tent» (al-Zawzanī)", "«الْمُخَيَّم: çadır yapılmış» (Zevzenî)", "ism-maful"))])

# ---- v. 27 ----
V(27, "Small of head, he tends his eggs at Dhū al-ʿUshayra, like the slave in a long fur, with no ears.",
  "Küçük başlı; Zü'l-Uşeyre'de yumurtalarını gözetir — uzun kürk giymiş, kulaksız köle gibi.",
 [n("صَعْلٍ", "sal-ant", Fr("نَعْتٌ آخَرُ لِلظَّلِيمِ الْمَحْذُوفِ الْمَوْصُوفِ بِـ«قَرِيبِ» وَ«مُصَلَّمِ» فِي الْبَيْتِ الرَّابِعِ وَالْعِشْرِينَ مَجْرُورٌ بِالْكَسْرَةِ", "a further na't of the unnamed ostrich described by «قَرِيبِ» and «مُصَلَّمِ» in verse 24, in jarr by the kasra", "24. beyitte «قَرِيبِ» ve «مُصَلَّمِ» ile nitelenen mahzûf devekuşunun bir başka na'tı, kesre ile mecrûr", "naat-sifa", "hadhf-wa-taqdir"),
     Dn("وَيَجُوزُ رَفْعُهُ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ — هُوَ صَعْلٌ — عَلَى الْقَطْعِ " + DUR + "؛ «الصَّعْلُ وَالْأَصْعَلُ: الصَّغِيرُ الرَّأْسِ» " + ZAW, "it may also be read in raf', the khabar of an omitted «he is», cut off from what goes before (al-Durra); «الصَّعْل and الْأَصْعَل: small of head» (al-Zawzanī)", "kat' yoluyla mahzûf «o»nun haberi olarak merfû okunması da câizdir (Dürre); «الصَّعْل ve الْأَصْعَل: küçük başlı» (Zevzenî)", "sifa-mushabbaha")),
  v("يَعُودُ", "ada-visit", MUDR(), HID("هُوَ", OSTRICH), CL("j", "نَعْتٌ آخَرُ لِلظَّلِيمِ", "a further na't of the ostrich", "devekuşunun bir başka na'tı", "jumla-sifa"), Dn("«يَعُودُ: يَتَعَهَّدُ» " + ZAW, "«يَعُودُ: he tends, looks after» (al-Zawzanī)", "«يَعُودُ: gözetir, bakar» (Zevzenî)"), g=["hollow-verbs"]),
  n("بِذِي", "dhu", JN("بِ", "ذِي", "j5", sense=FI_SENSE), MDF, TA("يَعُودُ"), s=[BI, ("ذِي", "dhu", "noun")]),
  pn("الْعُشَيْرَةِ", "ushayra-ant", MI(), Dn("«ذُو الْعُشَيْرَةِ: مَوْضِعٌ» " + ZAW, "«Dhū al-ʿUshayra: a place» (al-Zawzanī)", "«Zü'l-Uşeyre: bir yer» (Zevzenî)")),
  n("بَيْضَهُ", "bayd-ant", MF(), IDF("هُ"), s=[("بَيْضَ", "bayd-ant", "noun"), P("هُ")])],
 [n("كَالْعَبْدِ", "abd", JN("كَ", "الْعَبْدِ"), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ آخَرَ لِلظَّلِيمِ", "; the jarr phrase hangs on an omitted further na't of the ostrich", "; câr-mecrûr devekuşunun mahzûf bir başka na'tına müteallik"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: «شَبَّهَ الظَّلِيمَ بِعَبْدٍ لَبِسَ فَرْوًا طَوِيلًا وَلَا أُذُنَ لَهُ لِأَنَّهُ لَا أُذُنَ لِلنَّعَامِ، وَشَرَطَ الْفَرْوَ الطَّوِيلَ لِيُشْبِهَ جَنَاحَيْهِ، وَشَرَطَ الْعَبْدَ لِسَوَادِ الظَّلِيمِ» " + ZAW + "؛ وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ لَمْ يُذْكَرْ فِي الْبَيْتِ",
        "here is a tashbih mursal: «he likens the ostrich to a slave wearing a long fur and without ears, for ostriches have no ears; he makes the fur long to be like its wings, and makes him a slave for the ostrich's blackness» (al-Zawzanī); the tool is the kaf, and the point of likeness is not said in the verse",
        "burada mürsel teşbîh vardır: «devekuşunu, uzun kürk giymiş ve kulağı olmayan bir köleye benzetmiştir, çünkü devekuşlarının kulağı yoktur; kürkün uzun olmasını kanatlarına benzesin diye, köle olmasını devekuşunun siyahlığı için şart koşmuştur» (Zevzenî); edat kâf, vech-i şebeh beyitte söylenmemiştir", "tashbih", "arkan-al-tashbih"),
     s=[KA, ("الْعَبْدِ", "abd", "noun")]),
  n("ذِي", "dhu", NAT("الْعَبْدِ", "j5"), MDF),
  n("الْفَرْوِ", "farw-ant", MI()),
  n("الطَّوِيلِ", "tawil-long", NAT("الْفَرْوِ"), Dn("كَمَا فِي شَرْحِ الزَّوْزَنِيِّ: «لَبِسَ فَرْوًا طَوِيلًا»؛ وَجَعَلَهُ الدُّرَّةُ وَ«الْأَصْلَمِ» صِفَتَيْنِ لِـ«الْعَبْدِ»", "as in al-Zawzanī's gloss, «wearing a long fur»; al-Durra makes it and «الْأَصْلَمِ» two na'ts of «الْعَبْدِ»", "Zevzenî'nin şerhindeki gibi: «uzun bir kürk giymiş»; Dürre onu ve «الْأَصْلَمِ»i «الْعَبْدِ»in iki sıfatı sayar")),
  n("الْأَصْلَمِ", "aslam-ant", NAT("الْعَبْدِ"), QA, Dn("«الْأَصْلَمُ: الَّذِي لَا أُذُنَ لَهُ» " + ZAW, "«الْأَصْلَم: one who has no ears» (al-Zawzanī)", "«الْأَصْلَم: kulağı olmayan» (Zevzenî)"))])

# =====================================================================================================================
# Chapter 6 — النَّاقَةُ: سَيْرُهَا وَعَرَقُهَا (al-Zawzanī vv. 28–33)
# =====================================================================================================================

# ---- v. 28 ----
V(28, "She drank of the water of the two Duḥruḍs, and then turned aside, shying away from the pools of the Daylam.",
  "Duhrudeyn'in suyundan içti; sonra yana meyleden, Deylem'in havuzlarından ürken bir deve oldu.",
 [v("شَرِبَتْ", "shariba", MADI_F, HID("هِيَ", CAMEL), CL_IST, g=["thulathi-mujarrad-babs"]),
  n("بِمَاءِ", "ma-water", JN("بِ", "مَاءِ", sense=("بِمَعْنَى «مِنْ»", "meaning «from»", "«-den» anlamında")), MDF, TA("شَرِبَتْ"),
     Dn("وَهٰذَا مَذْهَبُ الْكُوفِيِّينَ؛ وَالْبَاءُ عِنْدَ الْبَصْرِيِّينَ زَائِدَةٌ وَ«مَاءِ» مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا حَرَكَةُ حَرْفِ الْجَرِّ الزَّائِدِ " + DUR + "، وَبِهِمَا قَالَ الزَّوْزَنِيُّ",
        "this is the Kufans' view; for the Basrans the ba is added and «مَاءِ» is the object, in nasb by a fatha that the added letter's vowel keeps from showing (al-Durra); al-Zawzanī gives both", "bu Kûfelilerin görüşüdür; Basralılara göre bâ zâiddir, «مَاءِ» mef'ûlün bihtir ve zâid harfin harekesi yüzünden görünmeyen takdîrî fetha ile mansûbdur (Dürre); Zevzenî ikisini de anar", "huruf-al-ziyada-fil-kafiya"),
     s=[BI, ("مَاءِ", "ma-water", "noun")]),
  pn("الدُّحْرُضَيْنِ", "duhrudan-ant", MI("jD"), Dn("مَوْضِعٌ، بِلَفْظِ الْمُثَنَّى: «شَرِبَتْ هٰذِهِ النَّاقَةُ مِنْ مِيَاهِ هٰذَا الْمَوْضِعِ» " + ZAW, "a place, named in the dual: «the she-camel drank of the waters of this place» (al-Zawzanī)", "tesniye lafzıyla bir yer adı: «bu deve bu yerin sularından içti» (Zevzenî)")),
  v("فَأَصْبَحَتْ", "asbaha", PRE("fa", "أَصْبَحَتْ"), Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "a defective past verb built on fatha; the ta marks the feminine", "fetha üzere mebnî nâkıs mâzî; tâ te'nîs içindir", "kana-wa-akhawatuha"), NAQ_SUB("هِيَ", CAMEL),
     CL(0, "مَعْطُوفَةٌ عَلَى «شَرِبَتْ»", "is conjoined to «شَرِبَتْ»", "«شَرِبَتْ»e ma'tûftur"), g=["form-iv-verbs"], s=[FA, ("أَصْبَحَتْ", "asbaha", "verb")])],
 [n("زَوْرَاءَ", "azwar-ant", RO("خَبَرُ «أَصْبَحَ»", "the predicate of «أَصْبَحَ»", "«أَصْبَحَ»in haberi", "n", "kana-wa-akhawatuha"), Dn("وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ «الزَّوَرُ: الْمَيْلُ … وَالنَّعْتُ أَزْوَرُ، وَالْأُنْثَى زَوْرَاءُ» " + ZAW,
       "it takes no tanwin, for the long feminine alif; «الزَّوَر is leaning aside … the adjective is أَزْوَر, fem. زَوْرَاء» (al-Zawzanī)", "memdûde te'nîs elifi sebebiyle gayr-i munsariftir; «الزَّوَر: meyletmek … sıfatı أَزْوَر, müennesi زَوْرَاء» (Zevzenî)", "mamnu-min-sarf")),
  v("تَنْفِرُ", "nafara", MUDR(), HID("هِيَ", CAMEL), CL("n", "خَبَرٌ ثَانٍ لِـ«أَصْبَحَ»", "a second predicate of «أَصْبَحَ»", "«أَصْبَحَ»in ikinci haberi", "kana-wa-akhawatuha")),
  pp("عَنْ", "an", HJ),
  n("حِيَاضِ", "hawd", MJ(), MDF, TA("تَنْفِرُ"), Dn("جَمْعُ حَوْضٍ", "the plural of حَوْض", "حَوْض'un cem'i", "jam-taksir")),
  pn("الدَّيْلَمِ", "daylam-ant", MI(), QA, Dn("«مِيَاهُ الدَّيْلَمِ: مِيَاهٌ مَعْرُوفَةٌ، وَقِيلَ: الْعَرَبُ تُسَمِّي الْأَعْدَاءَ دَيْلَمًا لِأَنَّ الدَّيْلَمَ صِنْفٌ مِنْ أَعْدَائِهَا» " + ZAW, "«the waters of the Daylam are known waters; it is also said that the Arabs call enemies ‹Daylam›, the Daylam being one kind of their enemies» (al-Zawzanī)", "«Deylem suları bilinen sulardır; Arapların düşmanlara ‹Deylem› dediği de söylenir, çünkü Deylem onların düşmanlarından bir sınıftır» (Zevzenî)"))])

# ---- v. 29 ----
V(29, "It is as if she holds her right flank away from a big-headed yowler of the supper-time,",
  "Sanki sağ böğrünü, akşam yemeği vakti miyavlayan iri ve çirkin başlı bir (kedi)den uzak tutuyor:",
 [pt("وَكَأَنَّمَا", "ka-annama", PRE("wa-ist", "كَأَنَّمَا"), Fr("حَرْفُ تَشْبِيهٍ كَفَّتْهُ «مَا» الْكَافَّةُ عَنِ الْعَمَلِ", "the particle of likening, kept from governing by the restraining مَا", "kâffe «mâ» ile amelden alıkonmuş teşbîh harfi", "innama-kaffa", "inna-wa-akhawatuha"),
     Sn("وَفِيهِ تَشْبِيهٌ: «يَصِفُ هٰذِهِ النَّاقَةَ بِالنَّشَاطِ فِي السَّيْرِ وَأَنَّهَا لَا تَسْتَقِيمُ فِي سَيْرِهَا نَشَاطًا وَمَرَحًا، فَكَأَنَّهَا تُنَحِّي جَانِبَهَا الْأَيْمَنَ خَوْفَ خَدْشِ سِنَّوْرٍ إِيَّاهُ» " + ZAW + "؛ وَالْأَدَاةُ «كَأَنَّ»",
        "here is a tashbih: «he describes the she-camel as lively in her going, never keeping straight for liveliness and high spirits — as if she held her right flank away for fear a cat should scratch it» (al-Zawzanī); the tool is كَأَنَّ",
        "burada teşbîh vardır: «deveyi yürüyüşündeki canlılıkla niteler; neşe ve coşkudan dolayı yürüyüşünde dosdoğru gitmez, sanki bir kedinin tırmalamasından korkarak sağ yanını uzak tutuyormuş gibidir» (Zevzenî); edat «كَأَنَّ»", "tashbih", "arkan-al-tashbih"),
     s=[WA, ("كَأَنَّمَا", "ka-annama", "part")]),
  v("تَنْأَى", "naa", MUDR("a"), HID("هِيَ", CAMEL), CL_IST, Dn("وَيُرْوَى «يَنْأَى» بِالْيَاءِ فَيَكُونُ «هِرٌّ» فِي الْبَيْتِ بَعْدَهُ فَاعِلَهُ " + DUR, "it is also related «يَنْأَى», with ya, and then «هِرٌّ» in the next verse is its doer (al-Durra)", "«يَنْأَى» diye yâ ile de rivayet edilir; o zaman sonraki beyitteki «هِرٌّ» onun fâilidir (Dürre)")),
  n("بِجَانِبِ", "janib", JN("بِ", "جَانِبِ"), MDF, TA("تَنْأَى"), Dn("وَالْبَاءُ لِلتَّعْدِيَةِ " + ZAW, "the ba makes the verb transitive (al-Zawzanī)", "bâ fiili geçişli kılar (Zevzenî)"), s=[BI, ("جَانِبِ", "janib", "noun")]),
  n("دَفِّهَا", "daff-ant", MI(), IDF("هَا"), Dn("مِنْ إِضَافَةِ الْمُرَادِفِ إِلَى مُرَادِفِهِ " + DUR + "؛ «الدَّفُّ: الْجَنْبُ» " + ZAW, "a word annexed to its synonym (al-Durra); «الدَّفّ is the flank» (al-Zawzanī)", "bir kelime eş anlamlısına izâfe edilmiştir (Dürre); «الدَّفّ: böğür» (Zevzenî)"), s=[("دَفِّ", "daff-ant", "noun"), P("هَا")])],
 [n("الْوَحْشِيِّ", "wahshi-ant", NAT("دَفِّهَا"), Dn("«الْجَانِبُ الْوَحْشِيُّ: الْيَمِينُ، وَسُمِّيَ وَحْشِيًّا لِأَنَّهُ لَا يُرْكَبُ مِنْ ذٰلِكَ الْجَانِبِ وَلَا يُنْزَلُ» " + ZAW + "؛ وَالْبَيْتُ مُدَوَّرٌ: «الْ» آخِرُ الصَّدْرِ وَ«وَحْشِيِّ» أَوَّلُ الْعَجُزِ",
       "«the ‹wild› side is the right, called so because one neither mounts nor dismounts on that side» (al-Zawzanī); the verse runs on: «الْ» ends the first hemistich and «وَحْشِيِّ» opens the second", "«‹vahşî› taraf sağ taraftır; o taraftan ne binilir ne inilir diye böyle adlandırılmıştır» (Zevzenî); beyit müdevverdir: «الْ» ilk mısraın sonu, «وَحْشِيِّ» ikincinin başıdır", "ilm-al-arud")),
  pp("مِنْ", "min", HJ),
  n("هَزِجِ", "hazij-ant", MJ(), MDF, TA("تَنْأَى"), Dn("عَلَى حَذْفِ مُضَافٍ: مِنْ خَوْفِ هَزِجِ الْعَشِيِّ؛ وَإِنْ عَلَّقْتَهُ بِمَحْذُوفٍ حَالٍ — تَنْأَى خَوْفًا مِنْ هَزِجٍ — فَالْمَعْنَى لَا يَأْبَاهُ " + DUR + "؛ «الْهَزِجُ: الصَّوْتُ … وَالنَّعْتُ هَزِجٌ» " + ZAW,
       "with a word left out: «for fear of the yowler»; it may also hang on an omitted hal — «drawing away in fear of …» (al-Durra); «هَزِج is sound … the adjective is هَزِج» (al-Zawzanī)", "bir muzâf hazfedilmiştir: «yowler'ın korkusundan»; mahzûf bir hâle bağlanması da anlama aykırı değildir (Dürre); «الْهَزِج: ses … sıfatı هَزِج» (Zevzenî)", "hadhf-wa-taqdir"),
     Sn("وَفِيهِ حَذْفُ الْمُضَافِ: «أَيْ مِنْ خَوْفِ هَزِجِ الْعَشِيِّ، فَحَذَفَ الْمُضَافَ» " + ZAW + "؛ وَ«هَزِجُ الْعَشِيِّ» كِنَايَةٌ عَنِ الْهِرِّ: «جَعَلَهُ هَزِجَ الْعَشِيِّ لِأَنَّهُمْ إِذَا تَعَشَّوْا فَإِنَّهُ يَصِيحُ عَلَى هٰذَا الطَّعَامِ لِيُطْعَمَ» " + ZAW,
        "here a word is dropped: «that is, for fear of the yowler of the supper-time — he dropped the annexed word» (al-Zawzanī); and «the yowler of the supper-time» is a kinaya for the cat: «he calls it so because when they sup it cries over the food to be fed» (al-Zawzanī)",
        "burada muzâf hazfedilmiştir: «yani akşam yemeği vakti miyavlayanın korkusundan; muzâfı hazfetmiştir» (Zevzenî); «akşam yemeğinin miyavlayanı» kediden kinâyedir: «onu böyle adlandırmıştır, çünkü onlar akşam yemeği yerken o, kendisine yedirilsin diye yemeğin başında bağırır» (Zevzenî)", "ijaz-al-hadhf", "kinaya", "aqsam-al-kinaya")),
  n("الْعَشِيِّ", "ashiyy", MI()),
  n("مُؤَوَّمِ", "muawwam-ant", NAT("هَزِجِ الْعَشِيِّ"), QT, Dn("«الْمُؤَوَّمُ: الْقَبِيحُ الرَّأْسِ الْعَظِيمُهُ» " + ZAW + "؛ وَفَتْحُ الْهَمْزَةِ مِنَ الْوَزْنِ", "«الْمُؤَوَّم: with a big, ugly head» (al-Zawzanī); the fatha on the hamza is settled by the metre", "«الْمُؤَوَّم: başı iri ve çirkin» (Zevzenî); hemzenin fethası vezinle sabittir", "ism-maful"))])

# ---- v. 30 ----
V(30, "— a cat led alongside her: whenever she turned on it in anger, it met her with both paws and with its mouth.",
  "— yanına bağlanıp yedilmiş bir kedi; dişi deve ne zaman öfkeyle ona dönse, kedi onu iki eliyle ve ağzıyla karşılardı.",
 [n("هِرٍّ", "hirr-ant", BDL("هَزِجِ الْعَشِيِّ"), Dn("«هِرٌّ: بَدَلٌ مِنْ هَزِجِ الْعَشِيِّ» " + ZAW + "؛ وَعَلَى رِوَايَةِ «يَنْأَى» هُوَ فَاعِلٌ مَرْفُوعٌ " + DUR, "«هِرّ is a badal of ‹the yowler of the supper-time›» (al-Zawzanī); on the version «يَنْأَى» it is the doer, in raf' (al-Durra)", "«هِرّ, ‹akşamın miyavlayanı›ndan bedeldir» (Zevzenî); «يَنْأَى» rivayetine göre fâildir, merfûdur (Dürre)")),
  n("جَنِيبٍ", "janib-ant", NAT("هِرٍّ"), Dn("«جَنِيبٌ: أَيْ مَجْنُوبٌ إِلَيْهَا، أَيْ مَقُودٌ» " + ZAW, "«جَنِيب: led at her side, that is, led along» (al-Zawzanī)", "«جَنِيب: yanına bağlanmış, yani yedilen» (Zevzenî)")),
  pt("كُلَّمَا", "kullama", Fr("«كُلَّ» ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِجَوَابِهِ «اتَّقَاهَا»، مُضَافٌ، وَ«مَا» حَرْفٌ مَصْدَرِيٌّ ظَرْفِيٌّ", "«كُلَّ» is an adverb of time in nasb by the fatha, hanging on its answer «اتَّقَاهَا», annexed; مَا is the particle that makes a masdar of time", "«كُلَّ» fetha ile mansûb zaman zarfı, cevabı «اتَّقَاهَا»ya müteallik, muzâf; «mâ» zaman bildiren masdar harfi", "maful-fih", "an-masdariyya"),
     Dn("وَ«مَا» وَالْفِعْلُ بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِإِضَافَةِ «كُلَّ» إِلَيْهِ: كُلَّ وَقْتِ عُطُوفِهَا " + DUR, "مَا and the verb after it make a masdar in jarr, «كُلَّ» being annexed to it: «every time of her turning» (al-Durra)", "«mâ» ve ardındaki fiil, «كُلَّ»nin kendisine izâfesiyle mecrûr bir masdar te'vîlindedir: «her dönüş vaktinde» (Dürre)"), s=[("كُلَّ", "kull", "noun"), ("مَا", "ma-masdariyya", "part")]),
  v("عَطَفَتْ", "atafa", MADI_F, HID("هِيَ", CAMEL), CL(0, "صِلَةُ «مَا» الْمَصْدَرِيَّةِ", "is the sila of the masdar-making مَا", "masdar bildiren «mâ»nın sılasıdır")),
  pp("لَهُ", "li", JP("لَ", "هُ", LAM_PRN), TA("عَطَفَتْ"), s=[("لَ", "li", "prep"), P("هُ")])],
 [n("غَضْبَى", "ghadban", HL("nA"), Dn("مِنْ فَاعِلِ «عَطَفَتْ»؛ وَهُوَ مُؤَنَّثُ غَضْبَانَ", "of the doer of «عَطَفَتْ»; the feminine of غَضْبَان", "«عَطَفَتْ»in fâilinden; غَضْبَان'ın müennesi")),
  v("اتَّقَاهَا", "ittaqa", MADI_A, OBJ("هَا"), HID("هُوَ", ("الْهِرِّ", "the cat", "kediye")), CL(0, "جَوَابُ «كُلَّمَا»", "is the answer of «كُلَّمَا»", "«كُلَّمَا»nın cevabıdır"),
     Dn("وَ«كُلَّمَا» وَمَا دَخَلَتْ عَلَيْهِ نَعْتٌ ثَانٍ لِـ«هِرٍّ» " + DUR + "؛ «اتَّقَاهَا: أَيِ اسْتَقْبَلَهَا» " + ZAW, "«كُلَّمَا» with what it governs is a second na't of «هِرٍّ» (al-Durra); «اتَّقَاهَا: it met her» (al-Zawzanī)", "«كُلَّمَا» ve girdiği cümle «هِرٍّ»ın ikinci na'tıdır (Dürre); «اتَّقَاهَا: onu karşıladı» (Zevzenî)"),
     g=["form-viii-verbs"], s=[("اتَّقَى", "ittaqa", "verb"), P("هَا")]),
  n("بِالْيَدَيْنِ", "yad", JN("بِ", "الْيَدَيْنِ", "jD"), TA("اتَّقَاهَا"), s=[BI, ("الْيَدَيْنِ", "yad", "noun")]),
  n("وَبِالْفَمِ", "fam", Fr("الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَ«الْفَمِ» اسْمٌ مَجْرُورٌ بِالْكَسْرَةِ، وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «بِالْيَدَيْنِ»", "the waw conjoins; the ba is a jarr letter and «الْفَمِ» a noun in jarr by the kasra; the phrase is conjoined to «بِالْيَدَيْنِ»", "vâv atıf; bâ cer harfi, «الْفَمِ» kesre ile mecrûr isim; câr-mecrûr «بِالْيَدَيْنِ»e ma'tûf", "atf-nasaq", "huruf-jarr"), QA,
     Dn("«يَقُولُ: كُلَّمَا أَمَالَتْ رَأْسَهَا إِلَيْهِ زَادَهَا خَدْشًا وَعَضًّا» " + ZAW, "«whenever she bent her head towards it, it gave her more scratching and biting» (al-Zawzanī)", "«başını ona ne zaman eğse, onu daha çok tırmalar ve ısırırdı» (Zevzenî)"), s=[WA, BI, ("الْفَمِ", "fam", "noun")])])

# ---- v. 31 ----
V(31, "She knelt down by the side of al-Ridāʿ, and it was as if she knelt on crushed reeds that crackle.",
  "Ridâ' tarafında çöktü; sanki ses veren, kırılmış kamışların üzerine çökmüştü.",
 [v("بَرَكَتْ", "baraka-ant", MADI_F, HID("هِيَ", CAMEL), CL_IST),
  pp("عَلَى", "ala", HJ),
  n("جَنْبِ", "janb-ant", MJ(), MDF, TA("بَرَكَتْ"), Dn("وَعِنْدَ الدُّرَّةِ: «عَلَى مَاءِ الرِّدَاعِ»", "al-Durra reads «by the water of al-Ridāʿ»", "Dürre «عَلَى مَاءِ الرِّدَاعِ» okur")),
  pn("الرِّدَاعِ", "rida-ant", MI(), Dn("«رِدَاعٌ: مَوْضِعٌ» " + ZAW, "«Ridāʿ: a place» (al-Zawzanī)", "«Ridâ': bir yer» (Zevzenî)")),
  pt("كَأَنَّمَا", "ka-annama", Fr("حَرْفُ تَشْبِيهٍ كَفَّتْهُ «مَا» الْكَافَّةُ عَنِ الْعَمَلِ", "the particle of likening, kept from governing by the restraining مَا", "kâffe «mâ» ile amelden alıkonmuş teşbîh harfi", "innama-kaffa", "inna-wa-akhawatuha"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: «شَبَّهَ أَنِينَهَا مِنْ كَلَالِهَا بِصَوْتِ الْقَصَبِ الْمُكَسَّرِ عِنْدَ بُرُوكِهَا عَلَيْهِ، وَقِيلَ: بَلْ شَبَّهَ صَوْتَ تَكَسُّرِ الطِّينِ الْيَابِسِ الَّذِي نَضَبَ عَنْهُ الْمَاءُ بِصَوْتِ تَكَسُّرِ الْقَصَبِ» " + ZAW + "؛ وَالْأَدَاةُ «كَأَنَّ»",
        "here is a tashbih mursal: «he likens her groaning from weariness to the sound of crushed reeds as she kneels on them; or, it is said, the sound of dry mud cracking where the water has gone from it to the sound of reeds breaking» (al-Zawzanī); the tool is كَأَنَّ",
        "burada mürsel teşbîh vardır: «yorgunluktan inlemesini, üzerine çöktüğünde kırılan kamışın sesine benzetmiştir; yahut suyu çekilmiş kuru çamurun kırılma sesini kamış kırılma sesine benzetmiştir» (Zevzenî); edat «كَأَنَّ»", "tashbih", "arkan-al-tashbih"))],
 [v("بَرَكَتْ", "baraka-ant", MADI_F, HID("هِيَ", CAMEL), CL("n", "حَالٌ مِنْ فَاعِلِ «بَرَكَتْ» الْأَوَّلِ", "a hal of the doer of the first «بَرَكَتْ»", "ilk «بَرَكَتْ»in fâilinden hâl", "al-hal-jumla-wa-rabituha"), Dn("وَالرَّابِطُ الضَّمِيرُ " + DUR, "the link is the pronoun (al-Durra)", "râbıt zamirdir (Dürre)")),
  pp("عَلَى", "ala", HJ),
  n("قَصَبٍ", "qasab-ant", MJ(), TA("بَرَكَتْ")),
  n("أَجَشَّ", "ajashsh-ant", NAT("قَصَبٍ", "jf"), Dn("مُنِعَ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ " + DUR + "؛ «أَجَشُّ: لَهُ صَوْتٌ» " + ZAW, "barred from tanwin as an adjective on أَفْعَل (al-Durra); «أَجَشّ: that has a sound» (al-Zawzanī)", "sıfat ve أَفْعَل vezni sebebiyle gayr-i munsarif (Dürre); «أَجَشّ: sesi olan» (Zevzenî)")),
  n("مُهَضَّمِ", "muhaddam-ant", NAT("قَصَبٍ", "j", "ثَانٍ"), Fr("، وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ", "; its deputy doer is a pronoun hidden in it", "; nâib-i fâili onda gizli zamirdir", "naib-al-fail"), QT, Dn("«مُهَضَّمٌ: أَيْ مُكَسَّرٌ» " + ZAW, "«مُهَضَّم: broken» (al-Zawzanī)", "«مُهَضَّم: kırılmış» (Zevzenî)", "ism-maful"))])

# ---- v. 32 ----
V(32, "It is as if thick syrup or pitch, boiled until it thickened, had been set in a cauldron whose sides the firewood was kindled about;",
  "Sanki koyulaşana dek kaynatılmış bir pekmez ya da katran, yanlarında odunların tutuşturulduğu bir kazandaymış —",
 [pt("وَكَأَنَّ", "kaanna", PRE("wa-ist", "كَأَنَّ"), KAANNA_,
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: «شَبَّهَ الْعَرَقَ السَّائِلَ مِنْ رَأْسِهَا وَعُنُقِهَا بِرُبٍّ أَوْ قَطِرَانٍ جُعِلَ فِي قُمْقُمٍ أُوقِدَتْ عَلَيْهِ النَّارُ فَهُوَ يَتَرَشَّحُ بِهِ عِنْدَ الْغَلَيَانِ، وَعَرَقُ الْإِبِلِ أَسْوَدُ لِذٰلِكَ شَبَّهَهُ بِهِمَا» " + ZAW + "؛ فَالْمُشَبَّهُ الْعَرَقُ، وَالْمُشَبَّهُ بِهِ الرُّبُّ أَوِ الْكُحَيْلُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ السَّوَادُ وَالتَّرَشُّحُ وَلَمْ يُذْكَرْ",
        "here is a tashbih mursal: «he likens the sweat running from her head and neck to syrup or pitch put in a cauldron with a fire lit under it, oozing as it boils; camels' sweat is black, which is why he likens it to these two» (al-Zawzanī); the thing likened is the sweat, the thing it is likened to the syrup or the pitch, the tool كَأَنَّ, and the point of likeness — blackness and oozing — is not said",
        "burada mürsel teşbîh vardır: «başından ve boynundan akan teri, altında ateş yakılmış bir kazana konmuş, kaynarken sızan pekmeze ya da katrana benzetmiştir; develerin teri siyahtır, bu yüzden onu bu ikisine benzetmiştir» (Zevzenî); müşebbeh ter, müşebbehün bih pekmez ya da katran, edat «كَأَنَّ», vech-i şebeh — siyahlık ve sızma — söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[WA, ("كَأَنَّ", "kaanna", "part")]),
  n("رُبًّا", "rubb-ant", ISM_K(), Dn("«الرُّبُّ: الطِّلَاءُ» " + ZAW, "«الرُّبّ: thick boiled juice» (al-Zawzanī)", "«الرُّبّ: koyu kaynatılmış usare, pekmez» (Zevzenî)")),
  pt("أَوْ", "aw", Fr("حَرْفُ عَطْفٍ", "a conjunction", "atıf harfi", "atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya")),
  n("كُحَيْلًا", "kuhayl-ant", ATF("رُبًّا", "n"), Dn("«الْكُحَيْلُ: الْقَطِرَانُ» " + ZAW, "«الْكُحَيْل: pitch, tar» (al-Zawzanī)", "«الْكُحَيْل: katran» (Zevzenî)")),
  n("مُعْقَدًا", "muqad-ant", NAT("كُحَيْلًا", "n"), Dn("«عَقَدْتُ الدَّوَاءَ: أَغْلَيْتُهُ حَتَّى خَثُرَ» " + ZAW, "«I thickened the medicine: I boiled it until it grew thick» (al-Zawzanī)", "«ilacı koyulaştırdım: koyulaşana dek kaynattım» (Zevzenî)", "ism-maful"))],
 [v("حَشَّ", "hashsha-ant", MADI, FAIL_BAD, CL("r", "خَبَرُ «كَأَنَّ»", "the predicate of «كَأَنَّ»", "«كَأَنَّ»nin haberi", "inna-wa-akhawatuha"), Dn("أَوْ نَعْتٌ ثَانٍ لِـ«كُحَيْلًا» إِذَا جُعِلَتْ جُمْلَةُ «يَنْبَاعُ» بَعْدَهُ الْخَبَرَ " + DUR + "؛ «حَشَّ النَّارَ يَحُشُّهَا حَشًّا: أَوْقَدَهَا» " + ZAW,
       "or a second na't of «كُحَيْلًا» if the clause «يَنْبَاعُ» after it is taken as the predicate (al-Durra); «حَشَّ النَّارَ يَحُشُّهَا: to kindle a fire» (al-Zawzanī)", "yahut sonraki «يَنْبَاعُ» cümlesi haber sayılırsa «كُحَيْلًا»nın ikinci na'tı (Dürre); «حَشَّ النَّارَ يَحُشُّهَا: ateşi tutuşturmak» (Zevzenî)"), g=["doubled-verbs"]),
  n("الْوَقُودُ", "waqud-ant", FL(), Dn("«الْوَقُودُ: الْحَطَبُ، وَالْوُقُودُ بِضَمِّ الْوَاوِ: الْإِيقَادُ» " + ZAW, "«الْوَقُود: firewood; الْوُقُود with damma: kindling» (al-Zawzanī)", "«الْوَقُود: odun; vâv'ın dammesiyle الْوُقُود: tutuşturma» (Zevzenî)")),
  pp("بِهِ", "bi", JP("بِ", "هِ", ("الْبَاءُ", "the ba", "bâ")), TA("حَشَّ"), Dn("وَقَالَ ابْنُ الْأَنْبَارِيِّ: مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ " + DUR, "Ibn al-Anbārī: they hang on an omitted hal (al-Durra)", "İbnü'l-Enbârî: mahzûf bir hâle müteallik (Dürre)"), s=[BI, P("هِ")]),
  n("جَوَانِبَ", "janib", MF(), MDF, Dn("وَقَالَ التِّبْرِيزِيُّ: يَجُوزُ أَنْ يَكُونَ «حَشَّ» بِمَعْنَى احْتَشَّ وَ«جَوَانِبَ» ظَرْفًا " + DUR, "al-Tibrīzī: حَشَّ may mean احْتَشَّ, and «جَوَانِبَ» then is an adverb (al-Durra)", "Tebrîzî: «حَشَّ» احْتَشَّ anlamında, «جَوَانِبَ» de zarf olabilir (Dürre)", "jam-taksir")),
  n("قُمْقُمِ", "qumqum-ant", MI(), QT, Sn("وَ«شَبَّهَ رَأْسَهَا بِالْقُمْقُمِ فِي الصَّلَابَةِ» " + ZAW, "and «he likens her head to the cauldron for hardness» (al-Zawzanī)", "ve «başını sertlikte kazana benzetmiştir» (Zevzenî)", "tashbih"),
     HD("هُوَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: ذَكَرَ الْمُشَبَّهَ بِهِ «قُمْقُمِ» وَطَوَى الْمُشَبَّهَ — رَأْسَهَا — وَالْجَامِعُ الصَّلَابَةُ", "it is an isti'ara tasrihiyya: he names the thing likened to, «قُمْقُمِ», and folds away the thing likened — her head; what joins them is hardness", "bu bir istiâre-i tasrîhiyyedir: müşebbehün bih «قُمْقُمِ» anılmış, müşebbeh — başı — dürülmüştür; câmi' sertliktir", "istiara", "aqsam-al-istiara"))])

# ---- v. 33 ----
V(33, "— it oozes from behind the ear of an easily angered, strongly built, swaggering she-camel, like the prized stallion bitten by the others.",
  "— öfkesi çabuk, sağlam yapılı, salınarak yürüyen bir devenin kulak arkasından sızar; (öteki aygırlarca) ısırılmış değerli bir aygır gibi.",
 [v("يَنْبَاعُ", "nabaa", MUDR(), HID("هُوَ", ("الرُّبِّ أَوِ الْكُحَيْلِ", "the syrup or the pitch", "pekmeze ya da katrana")), CL("r", "خَبَرُ «كَأَنَّ» فِي الْبَيْتِ قَبْلَهُ", "the predicate of «كَأَنَّ» in the verse before", "önceki beyitteki «كَأَنَّ»nin haberi", "inna-wa-akhawatuha"),
     Dn("«أَرَادَ يَنْبَعُ فَأَشْبَعَ الْفَتْحَةَ لِإِقَامَةِ الْوَزْنِ فَتَوَلَّدَتْ مِنْ إِشْبَاعِهَا أَلِفٌ … وَمِنْهُمْ مَنْ جَعَلَهُ يَنْفَعِلُ مِنَ الْبَوْعِ وَهُوَ طَيُّ الْمَسَافَةِ» " + ZAW + "؛ وَهُوَ ضَرُورَةُ شِعْرٍ",
        "«he means يَنْبَعُ: he lengthened the fatha to keep the metre, and an alif was born of the lengthening … some make it يَنْفَعِل from الْبَوْع, covering ground» (al-Zawzanī); a poet's licence", "«يَنْبَعُ demek istemiş, vezni korumak için fethayı uzatmış, uzatmadan bir elif doğmuştur … kimi de onu الْبَوْع'dan (mesafe katetmek) يَنْفَعِل sayar» (Zevzenî); şiir zaruretidir", "ilm-al-arud")),
  pp("مِنْ", "min", HJ),
  n("ذِفْرَى", "dhifra-ant", MJ("jA"), MDF, TA("يَنْبَاعُ"), Dn("«الذِّفْرَى: مَا خَلْفَ الْأُذُنِ» " + ZAW, "«الذِّفْرَى: the place behind the ear» (al-Zawzanī)", "«الذِّفْرَى: kulak arkası» (Zevzenî)")),
  n("غَضُوبٍ", "ghadub-ant", MI(), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — نَاقَةٍ — " + DUR, "it is a na't of a noun left unsaid — a she-camel (al-Durra)", "mahzûf bir mevsûfun — devenin — sıfatıdır (Dürre)", "sighat-mubalagha", "hadhf-wa-taqdir")),
  n("جَسْرَةٍ", "jasra-ant", SIFA_MD("ثَانٍ"), Dn("«الْجَسْرَةُ: النَّاقَةُ الْمُوثَقَةُ الْخَلْقِ» " + ZAW, "«الْجَسْرَة: a she-camel strongly built» (al-Zawzanī)", "«الْجَسْرَة: sağlam yapılı dişi deve» (Zevzenî)"))],
 [n("زَيَّافَةٍ", "zayyafa-ant", SIFA_MD("ثَالِثٌ"), Dn("«الزَّيْفُ: التَّبَخْتُرُ» " + ZAW, "«الزَّيْف: swaggering» (al-Zawzanī)", "«الزَّيْف: salınmak» (Zevzenî)", "sighat-mubalagha")),
  n("مِثْلَ", "mithl", RO("حَالٌ مِنَ الْمَوْصُوفِ الْمَحْذُوفِ بَعْدَ وَصْفِهِ", "a hal of the unnamed she-camel, once described", "nitelendikten sonra mahzûf mevsûftan hâl", "n", "hal"), MDF, Dn("وَأَوَّلُ وَجْهَيِ الدُّرَّةِ أَنَّهُ صِفَةٌ رَابِعَةٌ، وَذٰلِكَ عَلَى جَرِّهِ، وَالنَّشْرَةُ تَنْصِبُهُ", "al-Durra's first view makes it a fourth na't — that is with jarr; the edition has it in nasb", "Dürre'nin ilk görüşü onu dördüncü sıfat sayar — bu cerle olur; neşir ise onu nasb ile verir"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: «شَبَّهَهَا بِالْفَحْلِ فِي تَبَخْتُرِهَا وَوَثَاقَةِ خَلْقِهَا وَضِخَمِهَا» " + ZAW + "؛ وَالْأَدَاةُ «مِثْلَ»، وَوَجْهُ الشَّبَهِ لَمْ يُذْكَرْ فِي الْبَيْتِ",
        "here is a tashbih mursal mujmal: «he likens her to the stallion in her swagger, her strong build and her bulk» (al-Zawzanī); the tool is مِثْل, and the point of likeness is not said in the verse",
        "burada mürsel mücmel teşbîh vardır: «onu salınışında, yapısının sağlamlığında ve iriliğinde aygıra benzetmiştir» (Zevzenî); edat «مِثْلَ», vech-i şebeh beyitte söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih")),
  n("الْفَنِيقِ", "faniq", MI(), Dn("«الْفَنِيقُ: الْفَحْلُ مِنَ الْإِبِلِ» " + ZAW, "«الْفَنِيق: the stallion among camels» (al-Zawzanī)", "«الْفَنِيق: develerin aygırı» (Zevzenî)")),
  n("الْمُكْدَمِ", "mukdam-ant", NAT("الْفَنِيقِ"), QA, Dn("أَيْ: «قَدْ كَدَمَتْهُ الْفُحُولُ» " + ZAW, "that is, «the other stallions have bitten him» (al-Zawzanī)", "yani «öteki aygırlar onu ısırmıştır» (Zevzenî)", "ism-maful"))])

# =====================================================================================================================
# Chapter 7 — أَخْلَاقُ الْفَارِسِ، وَالْخَمْرُ (al-Zawzanī vv. 34–40)
# =====================================================================================================================
def INNANI(fa):
    """فَإِنَّنِي: the fa, then إِنَّ with the nun of protection and the speaker's ya as its noun"""
    a, e, t = {"jaza": ("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ", "the fa falls in the answer of the condition", "fâ şartın cevabına girmiştir"),
               "idha": ("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «إِذَا»", "the fa falls in the answer of «إِذَا»", "fâ «إِذَا»nın cevabına girmiştir"),
               "talil": ("الْفَاءُ حَرْفُ تَعْلِيلٍ", "the fa gives the reason", "fâ ta'lîl harfidir")}[fa]
    return Fr(a + "، وَ«إِنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا",
              e + "; إِنَّ is the particle of emphasis that puts its noun in nasb; the nun protects; the ya is its noun, in the seat of nasb",
              t + "; «إِنَّ» te'kîd ve nasb harfi, nûn vikâye içindir, yâ ismidir, mahallen mansûb", "inna-wa-akhawatuha", "al-bariz-al-muttasil",
              *({"jaza": ["al-fa-fi-jawab-al-shart"], "idha": ["al-fa-fi-jawab-al-shart"], "talil": []}[fa]))
S_INNANI = [FA, ("إِنَّ", "inna", "part"), ("نِ", "nun-wiqaya", "part"), P("ي")]
def KH_INNA(s="r", nth=""):
    o = {"": ("", "", ""), "ثَانٍ": (" ثَانٍ", " second", " ikinci")}[nth]
    return RO("خَبَرُ إِنَّ" + o[0], "the" + o[1] + " predicate of إِنَّ", "إِنَّ'nin" + o[2] + " haberi", s, "inna-wa-akhawatuha")
IDHA_Z = Fr("ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ", "an adverb of future time that puts its condition in jarr and is governed by its answer; built on sukun, in the seat of nasb",
            "şartını cer eden, cevabıyla mansûb olan gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb", "idha-shartiyya", "maful-fih")
ABLA2 = ("عَبْلَةَ", "ʿAbla", "Able")

# ---- v. 34 ----
V(34, "If you let your veil down before me, I am skilled at taking the horseman in his coat of mail.",
  "Benden yüzünü peçeyle örtüyorsan (bil ki) ben, zırhını giymiş süvariyi yakalamakta usta biriyim.",
 [pt("إِنْ", "in-shartiyya", Fr("حَرْفُ شَرْطٍ جَازِمٌ", "the conditional particle that puts in jazm", "cezmeden şart harfi", "in-shartiyya", "al-majzum-wal-shart-wal-jaza"),
     ILT("مِنَ الْغَيْبَةِ إِلَى الْخِطَابِ: تَحَدَّثَ عَنْهَا فِي «تُمْسِي وَتُصْبِحُ» ثُمَّ خَاطَبَهَا — «يَقُولُ مُخَاطِبًا عَشِيقَتَهُ» (الزَّوْزَنِيُّ)", "from the third person to the second: he spoke of her in «she passes her evenings and her mornings», and now addresses her — «he says, addressing the woman he loves» (al-Zawzanī)", "«akşamlarını ve sabahlarını geçirir» derken ondan söz edip şimdi ona hitap ettiği için (Zevzenî: «sevdiğine hitap ederek der ki») gaybetten hitaba")),
  v("تُغْدِفِي", "aghdafa-ant", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ",
       "a present verb in jazm, the verb of the condition, its sign the dropping of the nun — it is one of the five verbs; the ya is its doer, in the seat of raf'", "şart fiili olarak meczûm muzâri, ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; yâ fâildir, mahallen merfû", "afal-khamsa", "al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil"),
     CL(0, "ابْتِدَائِيَّةٌ", "is an opening clause", "ibtidâiyyedir"), Dn("«الْإِغْدَافُ: الْإِرْخَاءُ» " + ZAW, "«الْإِغْدَاف: letting down» (al-Zawzanī)", "«الْإِغْدَاف: salıvermek, indirmek» (Zevzenî)"), g=["form-iv-verbs"]),
  n("دُونِي", "dun", ZM("nM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), ZT("تُغْدِفِي"), s=[("دُونِ", "dun", "noun"), P("ي")]),
  n("الْقِنَاعَ", "qina-ant", MF(), Sn("وَإِغْدَافُ الْقِنَاعِ كِنَايَةٌ عَنِ الِاسْتِتَارِ وَالْإِعْرَاضِ: «أَيْ تَسْتَتِرِي عَنِّي» " + ZAW, "letting down the veil is a kinaya for hiding from him and turning away: «that is, if you hide yourself from me» (al-Zawzanī)", "peçeyi indirmek ondan gizlenmekten ve yüz çevirmekten kinâyedir: «yani benden gizlenirsen» (Zevzenî)", "kinaya")),
  pt("فَإِنَّنِي", "inna", INNANI("jaza"), CL("z", "جَوَابُ الشَّرْطِ", "the answer of the condition", "şartın cevabı", "al-fa-fi-jawab-al-shart"), s=S_INNANI)],
 [n("طَبٌّ", "tabb-ant", KH_INNA(), Dn("«طَبٌّ: حَاذِقٌ عَالِمٌ» " + ZAW, "«طَبّ: skilled, knowing» (al-Zawzanī)", "«طَبّ: usta, bilgili» (Zevzenî)", "sifa-mushabbaha")),
  n("بِأَخْذِ", "akhdh", JN("بِ", "أَخْذِ"), MDF, TA("طَبٌّ"), s=[BI, ("أَخْذِ", "akhdh", "noun")]),
  n("الْفَارِسِ", "faris-ant", MI(), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ وَفَاعِلُهُ مَحْذُوفٌ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR, "the masdar is annexed to its object and its doer is left out; and the word is a na't of a noun left unsaid (al-Durra)", "masdar mef'ûlüne izâfe edilmiş, fâili hazfedilmiştir; kelime mahzûf bir mevsûfun sıfatıdır (Dürre)", "masdar")),
  n("الْمُسْتَلْئِمِ", "mustalim", SIFA_MD("ثَانٍ"), QA, Dn("«اسْتَلْأَمَ: لَبِسَ اللَّأْمَةَ»، وَهِيَ الدِّرْعُ " + ZAW + "؛ يَقُولُ: «لَا يَنْبَغِي لَكِ أَنْ تَزْهَدِي فِيَّ مَعَ نَجْدَتِي وَبَأْسِي»", "«اسْتَلْأَمَ: he put on the لَأْمَة», a coat of mail (al-Zawzanī); he means: «you should not think little of me, with my courage and my might»", "«اسْتَلْأَمَ: لَأْمَة giydi», yani zırh (Zevzenî); demek ister ki: «yiğitliğim ve gücümle benden yüz çevirmen yakışmaz»", "ism-fail"))])

# ---- v. 35 ----
V(35, "Praise me for what you know of me, for I am easy to deal with, so long as I am not wronged.",
  "Benim hakkımda bildiklerinle beni öv; çünkü haksızlığa uğramadıkça huyum yumuşak, geçimim kolaydır.",
 [v("أَثْنِي", "athna-ant", AMR_Y, Dn("وَالْجُمْلَةُ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا " + DUR, "the clause opens the speech and has no seat (al-Durra)", "cümle ibtidâiyyedir, mahalli yoktur (Dürre)"), g=["form-iv-verbs", "naqis-verbs"]),
  pp("عَلَيَّ", "ala", JP("عَلَى", "ي"), TA("أَثْنِي")),
  pp("بِمَا", "ma-mawsula", Fr("الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ", "the ba is a jarr letter, and مَا a relative noun built on sukun, in the seat of jarr", "bâ cer harfi; «mâ» sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr", "huruf-jarr", "ism-mawsul"), TA("أَثْنِي"), s=[BI, ("مَا", "ma-mawsula", "pron")]),
  v("عَلِمْتِ", "alima", TU("anti"), CL_SILA, Dn("وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: عَلِمْتِهِ " + DUR + "؛ أَيْ: «مِنْ مَحَامِدِي وَمَنَاقِبِي» " + ZAW, "the pronoun returning to the relative is left out — «what you know of it» (al-Durra); that is, «of my praiseworthy deeds and virtues» (al-Zawzanī)", "mevsûle dönen zamir hazfedilmiştir: «bildiğin şey» (Dürre); yani «övülecek hasletlerimden ve meziyetlerimden» (Zevzenî)"), g=["thulathi-mujarrad-babs"]),
  pt("فَإِنَّنِي", "inna", INNANI("talil"), CL(0, "تَعْلِيلٌ لِلْأَمْرِ", "gives the reason for the command", "emrin gerekçesidir"), s=S_INNANI)],
 [n("سَمْحٌ", "samh-ant", KH_INNA(), Dn("وَعِنْدَ الدُّرَّةِ «سَهْلٌ»", "al-Durra reads سَهْلٌ", "Dürre «سَهْلٌ» okur", "sifa-mushabbaha")),
  n("مُخَالَقَتِي", "mukhalaqa-ant", RO("فَاعِلٌ لِلصِّفَةِ الْمُشَبَّهَةِ «سَمْحٌ»", "the doer of the sifa mushabbaha «سَمْحٌ»", "«سَمْحٌ» sıfat-ı müşebbehesinin fâili", "rM", "fail", "sifa-mushabbaha"),
     Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), Dn("«الْمُخَالَقَةُ: مُفَاعَلَةٌ مِنَ الْخُلُقِ» " + ZAW, "«الْمُخَالَقَة: dealing with others in character — the mufā'ala of الْخُلُق» (al-Zawzanī)", "«الْمُخَالَقَة: الْخُلُق'tan müfâale, ahlâkla muamele» (Zevzenî)", "masdar"),
     s=[("مُخَالَقَتِ", "mukhalaqa-ant", "noun"), P("ي")]),
  pt("إِذَا", "idha", Fr("ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«سَمْحٌ»", "an adverb of time built on sukun, in the seat of nasb, hanging on «سَمْحٌ»", "sükûn üzere mebnî zaman zarfı, mahallen mansûb, «سَمْحٌ»a müteallik", "maful-fih"),
     Dn("وَإِنْ جَعَلْتَهَا شَرْطِيَّةً فَجَوَابُهَا مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ " + DUR, "if it is taken as conditional, its answer is left out, pointed to by what goes before (al-Durra)", "şartiyye sayılırsa cevabı hazfedilmiştir, öncesi ona delâlet eder (Dürre)")),
  pt("لَمْ", "lam-jazim", LAM_J),
  v("أُظْلَمِ", "zalama", JZM_R(), MAJH, Fr("، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا", "; its deputy doer is the hidden «I»", "; nâib-i fâili vücûben gizli zamir «ben»", "naib-al-fail"),
     CL_MI("إِذَا"), Dn("أَيْ: «إِذَا لَمْ يُهْضَمْ حَقِّي وَلَمْ يُبْخَسْ حَظِّي» " + ZAW, "that is, «so long as my right is not trodden on nor my share cut short» (al-Zawzanī)", "yani «hakkım çiğnenmedikçe ve payım eksiltilmedikçe» (Zevzenî)"), g=["thulathi-mujarrad-babs"])])

# ---- v. 36 ----
V(36, "But when I am wronged, the wrong done me is grim, bitter in its taste like the taste of colocynth.",
  "Ama haksızlığa uğradığımda, bana yapılan haksızlık (karşılığı) çetin olur; tadı ebucehil karpuzunun tadı gibi acıdır.",
 [pt("وَإِذَا", "idha", PRE("wa-ist", "إِذَا"), IDHA_Z, s=[WA, ("إِذَا", "idha", "part")]),
  v("ظُلِمْتُ", "zalama", TU_M("ana"), CL_MI("إِذَا"),
     HD("بَيْنَهُ وَبَيْنَ «لَمْ أُظْلَمِ» فِي الْبَيْتِ قَبْلَهُ طِبَاقُ السَّلْبِ: فِعْلَا مَصْدَرٍ وَاحِدٍ، أَحَدُهُمَا مُثْبَتٌ وَالْآخَرُ مَنْفِيٌّ", "it makes a tibaq al-salb with «لَمْ أُظْلَمِ» in the verse before: two verbs of one masdar, one affirmed and the other denied", "önceki beyitteki «لَمْ أُظْلَمِ» ile tıbâk-ı selb oluşturur: aynı masdardan iki fiil, biri müspet öteki menfî", "tibaq")),
  pt("فَإِنَّ", "inna", Fr("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «إِذَا»، وَ«إِنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ", "the fa falls in the answer of «إِذَا»; إِنَّ is the particle of emphasis that puts its noun in nasb", "fâ «إِذَا»nın cevabına girmiştir; «إِنَّ» te'kîd ve nasb harfi", "al-fa-fi-jawab-al-shart", "inna-wa-akhawatuha"),
     CL(0, "جَوَابُ «إِذَا»", "is the answer of «إِذَا»", "«إِذَا»nın cevabıdır"), s=[FA, ("إِنَّ", "inna", "part")]),
  n("ظُلْمِي", "zulm", RO("اسْمُ إِنَّ", "the noun of إِنَّ", "إِنَّ'nin ismi", "nM", "inna-wa-akhawatuha"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"),
     Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ وَفَاعِلُهُ مَحْذُوفٌ " + DUR, "the masdar is annexed to its object, and its doer is left out (al-Durra)", "masdar mef'ûlüne izâfe edilmiş, fâili hazfedilmiştir (Dürre)", "masdar"), s=[("ظُلْمِ", "zulm", "noun"), P("ي")]),
  n("بَاسِلٌ", "basil-ant", KH_INNA(), Dn("«بَاسِلٌ: كَرِيهٌ، وَرَجُلٌ بَاسِلٌ: شُجَاعٌ» " + ZAW, "«بَاسِل: hateful, grim; a بَاسِل man is a brave one» (al-Zawzanī)", "«بَاسِل: çirkin, çetin; بَاسِل adam: yiğit» (Zevzenî)"))],
 [n("مُرٌّ", "murr-ant", KH_INNA("r", "ثَانٍ")),
  n("مَذَاقَتُهُ", "madhaqa-ant", MB(), IDF("هُ"), Dn("وَالْجُمْلَةُ مُفَسِّرَةٌ لِـ«مُرٌّ»، أَوْ خَبَرٌ ثَالِثٌ لِـ«إِنَّ»؛ وَيَجُوزُ أَنْ يَكُونَ «مَذَاقَتُهُ» فَاعِلًا لِـ«مُرٌّ» " + DUR, "the clause explains «مُرٌّ», or is a third predicate of إِنَّ; «مَذَاقَتُهُ» may also be the doer of «مُرٌّ» (al-Durra)", "cümle «مُرٌّ»u açıklar, yahut إِنَّ'nin üçüncü haberidir; «مَذَاقَتُهُ»nun «مُرٌّ»un fâili olması da câizdir (Dürre)"), s=[("مَذَاقَةُ", "madhaqa-ant", "noun"), P("هُ")]),
  n("كَطَعْمِ", "tam-taste", JN("كَ", "طَعْمِ"), MDF, TAM("khabar", "مَذَاقَتُهُ"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ: الْمُشَبَّهُ مَذَاقَةُ ظُلْمِهِ، وَالْمُشَبَّهُ بِهِ طَعْمُ الْعَلْقَمِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ الْمَرَارَةُ وَقَدْ ذُكِرَتْ «مُرٌّ»؛ قَالَ الزَّوْزَنِيُّ: «أَيْ مَنْ ظَلَمَنِي عَاقَبْتُهُ عِقَابًا بَالِغًا يَكْرَهُهُ كَمَا يَكْرَهُ طَعْمَ الْعَلْقَمِ مَنْ ذَاقَهُ»",
        "here is a tashbih mursal mufassal: the thing likened is the taste of the wrong done him; the thing it is likened to, the taste of colocynth; the tool, the kaf; and the point of likeness — bitterness — is said: «مُرٌّ». Al-Zawzanī: «that is, whoever wrongs me I punish with a punishment he hates as one who tastes colocynth hates its taste»",
        "burada mürsel mufassal teşbîh vardır: müşebbeh ona yapılan haksızlığın tadı; müşebbehün bih ebucehil karpuzunun tadı; edat kâf; vech-i şebeh — acılık — «مُرٌّ» diye söylenmiştir. Zevzenî: «yani bana haksızlık edeni, ebucehil karpuzunu tadanın onun tadından hoşlanmadığı gibi hoşlanmayacağı ağır bir cezayla cezalandırırım»", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[KA, ("طَعْمِ", "tam-taste", "noun")]),
  n("الْعَلْقَمِ", "alqam-ant", MI(), QA, Dn("الْعَلْقَمُ: الْحَنْظَلُ", "الْعَلْقَم: colocynth, the bitter gourd", "الْعَلْقَم: ebucehil karpuzu, acı kabak"))])

# ---- v. 37 ----
V(37, "And I have drunk of the wine after the midday heats had settled, paying with the bright, stamped (coin).",
  "Andolsun, öğle sıcakları durulduktan sonra parlatılmış, damgalı (dinar) karşılığında şaraptan içtim.",
 [pt("وَلَقَدْ", "qad", Fr("الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ وَالْمُقْسَمُ بِهِ مَحْذُوفٌ تَقْدِيرُهُ: وَاللهِ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَ«قَدْ» حَرْفُ تَحْقِيقٍ",
       "the waw is the waw of the oath, a jarr letter, with the thing sworn by left out — «by God»; the lam falls in the answer of the oath; قَدْ is a particle of certainty", "vâv kasem ve cer harfidir, kendisiyle yemin edilen hazfedilmiştir: «Allah'a andolsun»; lâm kasemin cevabına girmiştir; «قَدْ» tahkîk harfi", "huruf-al-qasam-fil-kafiya", "qad-harf", "hadhf-wa-taqdir"),
     s=[("وَ", "wa-qasam", "prep"), ("لَ", "lam-qasam", "part"), ("قَدْ", "qad", "part")]),
  v("شَرِبْتُ", "shariba", TU("ana"), CL(0, "جَوَابُ الْقَسَمِ", "is the answer of the oath", "kasemin cevabıdır"),
     Sn("وَهُوَ كِنَايَةٌ عَنِ الْجُودِ: «يُرِيدُ أَنَّهُ اشْتَرَى الْخَمْرَ فَشَرِبَهَا، وَالْعَرَبُ تَفْتَخِرُ بِشُرْبِ الْخَمْرِ وَالْقِمَارِ لِأَنَّهَا مِنْ دَلَائِلِ الْجُودِ عِنْدَهَا» " + ZAW, "it is a kinaya for generosity: «he means he bought the wine and drank it; the Arabs boasted of drinking wine and of gaming, for with them these were signs of open-handedness» (al-Zawzanī)", "cömertlikten kinâyedir: «şarabı satın alıp içtiğini kasteder; Araplar şarap içmekle ve kumarla övünürlerdi, çünkü bunlar onlarca cömertliğin delillerindendir» (Zevzenî)", "kinaya"), g=["thulathi-mujarrad-babs"]),
  pp("مِنَ", "min", HJ),
  n("الْمُدَامَةِ", "mudama", MJ(), TA("شَرِبْتُ"), Dn("«الْمُدَامُ وَالْمُدَامَةُ: الْخَمْرُ، سُمِّيَتْ بِهَا لِأَنَّهَا أُدِيمَتْ فِي دَنِّهَا» " + ZAW, "«الْمُدَام and الْمُدَامَة: wine, so called because it was kept long in its jar» (al-Zawzanī)", "«الْمُدَام ve الْمُدَامَة: şarap; küpünde uzun süre bekletildiği için böyle adlandırılmıştır» (Zevzenî)")),
  n("بَعْدَمَا", "bada", Fr("«بَعْدَ» ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«شَرِبْتُ»، مُضَافٌ، وَ«مَا» حَرْفٌ مَصْدَرِيٌّ", "«بَعْدَ» is an adverb of time in nasb by the fatha, hanging on «شَرِبْتُ», annexed; مَا is the particle that makes a masdar", "«بَعْدَ» fetha ile mansûb zaman zarfı, «شَرِبْتُ»e müteallik, muzâf; «mâ» masdar harfi", "maful-fih", "an-masdariyya"),
     s=[("بَعْدَ", "bada", "noun"), ("مَا", "ma-masdariyya", "part")])],
 [v("رَكَدَ", "rakada-ant", MADI, FAIL_BAD, CL(0, "صِلَةُ «مَا» الْمَصْدَرِيَّةِ", "is the sila of the masdar-making مَا", "masdar bildiren «mâ»nın sılasıdır"), Dn("وَ«مَا» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِإِضَافَةِ «بَعْدَ» إِلَيْهِ " + DUR + "؛ «رَكَدَ: سَكَنَ» " + ZAW,
       "مَا with the verb makes a masdar in jarr, «بَعْدَ» being annexed to it (al-Durra); «رَكَدَ: it settled, grew still» (al-Zawzanī)", "«mâ» ile fiil, «بَعْدَ»nin izâfesiyle mecrûr bir masdar te'vîlindedir (Dürre); «رَكَدَ: durgunlaştı» (Zevzenî)")),
  n("الْهَوَاجِرُ", "hajira-ant", FL(), Dn("«جَمْعُ الْهَاجِرَةِ، وَهِيَ أَشَدُّ الْأَوْقَاتِ حَرًّا» " + ZAW, "«the plural of الْهَاجِرَة, the hottest time of day» (al-Zawzanī)", "«الْهَاجِرَة'nin cem'i: günün en sıcak vakti» (Zevzenî)", "jam-taksir")),
  n("بِالْمَشُوفِ", "mashuf-ant", JN("بِ", "الْمَشُوفِ"), TA("شَرِبْتُ"), Dn("وَ«الْمَشُوفِ» صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ «الْمَشُوفُ: الْمَجْلُوُّ … بِالْمَشُوفِ: أَيْ بِالدِّينَارِ، فَحَذَفَ الْمَوْصُوفَ، وَمِنْهُمْ مَنْ جَعَلَهُ مِنْ صِفَةِ الْقَدَحِ» " + ZAW,
       "«الْمَشُوفِ» is a na't of a noun left unsaid (al-Durra); «الْمَشُوف: polished … ‹with the polished one›: with the dinar — he dropped the noun it describes; some make it describe the cup» (al-Zawzanī)", "«الْمَشُوفِ» mahzûf bir mevsûfun sıfatıdır (Dürre); «الْمَشُوف: cilalanmış … yani dinarla; mevsûfu hazfetmiştir; kimi onu kadehin sıfatı sayar» (Zevzenî)", "hadhf-wa-taqdir"),
     Sn("وَفِيهِ حَذْفُ الْمَوْصُوفِ: «أَيْ بِالدِّينَارِ، فَحَذَفَ الْمَوْصُوفَ» " + ZAW, "here the noun described is dropped: «that is, with the dinar — he dropped the noun described» (al-Zawzanī)", "burada mevsûf hazfedilmiştir: «yani dinarla; mevsûfu hazfetmiştir» (Zevzenî)", "ijaz-al-hadhf"),
     s=[BI, ("الْمَشُوفِ", "mashuf-ant", "noun")]),
  n("الْمُعْلَمِ", "mulam-ant", SIFA_MD("ثَانٍ"), QA, Dn("«الْمُعْلَمُ: الَّذِي فِيهِ عَلَامَاتٌ» — أَيِ الْمَنْقُوشُ", "«الْمُعْلَم: that bears marks» — stamped", "«الْمُعْلَم: üzerinde işaretler bulunan» — yani damgalı", "ism-maful"))])

# ---- v. 38 ----
V(38, "— from a yellow glass with lines on it, paired with a shining (jug) in the left hand, its mouth stopped with a cloth.",
  "— üzerinde çizgiler bulunan sarı bir kadehten; sol elde, ağzı bezle tıkalı parlak (bir ibrikle) yan yana konmuş.",
 [n("بِزُجَاجَةٍ", "zujaja", JN("بِ", "زُجَاجَةٍ", sense=("بِمَعْنَى «مِنْ»", "meaning «from»", "«-den» anlamında")), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«شَرِبْتُ» فِي الْبَيْتِ قَبْلَهُ", "; the jarr phrase hangs on «شَرِبْتُ» in the verse before", "; câr-mecrûr önceki beyitteki «شَرِبْتُ»e müteallik"), s=[BI, ("زُجَاجَةٍ", "zujaja", "noun")]),
  n("صَفْرَاءَ", "asfar", NAT("زُجَاجَةٍ", "jf"), Dn("مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ وَقِيلَ: حَالٌ مِنَ «الْمُدَامَةِ»، وَالْأَوَّلُ أَجْوَدُ " + DUR, "a diptote for the long feminine alif; it is also said to be a hal of «الْمُدَامَةِ», but the first is better (al-Durra)", "memdûde te'nîs elifi sebebiyle gayr-i munsarif; «الْمُدَامَةِ»den hâl olduğu da söylenmiştir, birincisi daha iyidir (Dürre)")),
  n("ذَاتِ", "dhat", NAT("زُجَاجَةٍ", "j", "ثَانٍ"), MDF),
  n("أَسِرَّةٍ", "sirar-ant", MI(), Dn("«الْأَسِرَّةُ: جَمْعُ السِّرِّ وَالسِّرَرِ، وَهُمَا الْخَطُّ مِنْ خُطُوطِ الْيَدِ وَالْجَبْهَةِ وَغَيْرِهِمَا» " + ZAW, "«الْأَسِرَّة: the plural of السِّرّ and السِّرَر, a line among the lines of the hand, the brow and the like» (al-Zawzanī)", "«الْأَسِرَّة: السِّرّ ve السِّرَر'in cem'i; el, alın vb.'deki çizgilerden biri» (Zevzenî)", "jam-taksir"))],
 [v("قُرِنَتْ", "qarana", Fr("فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "a past verb in the passive, built on fatha; the ta marks the feminine", "fetha üzere mebnî meçhul mâzî; tâ te'nîs içindir", "al-majhul-fil-kafiya"),
     HID("هِيَ", ("الزُّجَاجَةِ", "the glass", "kadehe"), naib=True), CL("j", "نَعْتٌ لِـ«زُجَاجَةٍ»", "a na't of «زُجَاجَةٍ»", "«زُجَاجَةٍ»in na'tı", "jumla-sifa"), Dn("أَوْ حَالٌ مِنْهَا بَعْدَ وَصْفِهَا " + DUR, "or a hal of it, once described (al-Durra)", "yahut nitelendikten sonra ondan hâl (Dürre)")),
  n("بِأَزْهَرَ", "azhar-ant", JN("بِ", "أَزْهَرَ", "jf"), TA("قُرِنَتْ"), Dn("مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ «بِأَزْهَرَ: أَيْ بِإِبْرِيقٍ أَزْهَرَ» " + ZAW,
       "a diptote, an adjective on أَفْعَل, and a na't of a noun left unsaid (al-Durra); «‹with a shining one›: with a shining jug» (al-Zawzanī)", "sıfat ve أَفْعَل vezni sebebiyle gayr-i munsarif; mahzûf bir mevsûfun sıfatı (Dürre); «parlak biriyle, yani parlak bir ibrikle» (Zevzenî)", "hadhf-wa-taqdir"),
     Sn("وَفِيهِ حَذْفُ الْمَوْصُوفِ: «أَيْ بِإِبْرِيقٍ أَزْهَرَ» " + ZAW, "here the noun described is dropped: «that is, with a shining jug» (al-Zawzanī)", "burada mevsûf hazfedilmiştir: «yani parlak bir ibrikle» (Zevzenî)", "ijaz-al-hadhf"), s=[BI, ("أَزْهَرَ", "azhar-ant", "noun")]),
  pp("فِي", "fi", HJ),
  n("الشِّمَالِ", "shimal", MJ(), TA("قُرِنَتْ"), Dn("وَإِنْ عَلَّقْتَهُمَا بِـ«مُفَدَّمِ» فَالشِّمَالُ بِمَعْنَى الْجِهَةِ " + DUR, "if the phrase is hung on «مُفَدَّمِ», الشِّمَال means the direction (al-Durra)", "câr-mecrûr «مُفَدَّمِ»e bağlanırsa الشِّمَال yön anlamındadır (Dürre)")),
  n("مُفَدَّمِ", "mufaddam-ant", SIFA_MD("ثَانٍ"), QT, Dn("«مُفَدَّمٌ: مَسْدُودُ الرَّأْسِ بِالْفِدَامِ» " + ZAW + "، وَالْفِدَامُ مَا يُوضَعُ عَلَى الْفَمِ سِدَادًا لَهُ", "«مُفَدَّم: with its head stopped by a فِدَام» (al-Zawzanī), a cloth put over the mouth to close it", "«مُفَدَّم: başı فِدَام ile tıkanmış» (Zevzenî); فِدَام, ağzı kapatmak için üzerine konan bezdir", "ism-maful"))])

# ---- v. 39 ----
V(39, "And when I drink, I am a spender of my wealth, while my honour is whole and unwounded.",
  "İçtiğimde malımı tüketirim; namusum ise tam ve yarasız kalır.",
 [pt("فَإِذَا", "idha", PRE("fa-ist", "إِذَا"), IDHA_Z, s=[FA, ("إِذَا", "idha", "part")]),
  v("شَرِبْتُ", "shariba", TU("ana"), CL_MI("إِذَا"), Dn("وَالْمَفْعُولُ مَحْذُوفٌ " + DUR, "the object is left out (al-Durra)", "mef'ûl hazfedilmiştir (Dürre)"), g=["thulathi-mujarrad-babs"]),
  pt("فَإِنَّنِي", "inna", INNANI("idha"), CL(0, "جَوَابُ «إِذَا»", "is the answer of «إِذَا»", "«إِذَا»nın cevabıdır"), s=S_INNANI),
  n("مُسْتَهْلِكٌ", "mustahlik-ant", KH_INNA(), Fr("، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ فِيهِ وُجُوبًا تَقْدِيرُهُ: أَنَا", "; its doer is the hidden «I»", "; fâili vücûben gizli zamir «ben»"), Dn("اسْمُ فَاعِلٍ يَعْمَلُ عَمَلَ فِعْلِهِ", "an active participle working as its verb does", "fiilinin amelini yapan ism-i fâil", "ism-fail"),
     HD("بَيْنَهُ وَبَيْنَ «وَافِرٌ» طِبَاقٌ: إِهْلَاكُ الْمَالِ وَوُفُورُ الْعِرْضِ مَعْنَيَانِ مُتَقَابِلَانِ فِي الْجُمْلَةِ — «فَأَكُونُ تَامَّ الْعِرْضِ مُهْلِكَ الْمَالِ» (الزَّوْزَنِيُّ)", "it makes a tibaq with «وَافِرٌ»: wasting the wealth and the honour kept whole are meanings opposed in the main — «so I am whole in honour, a waster of wealth» (al-Zawzanī)", "«وَافِرٌ» ile tıbâk oluşturur: malı tüketmek ve namusun tam kalması genel olarak karşıt iki mânâdır — «namusu tam, malı tüketen olurum» (Zevzenî)", "tibaq"))],
 [n("مَالِي", "mal", RO("مَفْعُولٌ بِهِ لِـ«مُسْتَهْلِكٌ»", "the object of «مُسْتَهْلِكٌ»", "«مُسْتَهْلِكٌ»un mef'ûlü", "nM", "maful-bihi"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), s=[("مَالِ", "mal", "noun"), P("ي")]),
  n("وَعِرْضِي", "ird", PRE("wa-hal", "عِرْضُ"), MB("rM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), s=[WA, ("عِرْضِ", "ird", "noun"), P("ي")]),
  n("وَافِرٌ", "wafir-ant", KH(), CL("n", "حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «مُسْتَهْلِكٌ»", "a hal of the pronoun hidden in «مُسْتَهْلِكٌ»", "«مُسْتَهْلِكٌ»daki gizli zamirden hâl", "al-hal-jumla-wa-rabituha"), Dn("أَوْ مِنْ يَاءِ «مَالِي»، وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ " + DUR, "or of the ya of «مَالِي»; the links are the waw and the pronoun (al-Durra)", "yahut «مَالِي»deki yâdan; râbıt vâv ve zamirdir (Dürre)")),
  pt("لَمْ", "lam-jazim", LAM_J),
  v("يُكْلَمِ", "kalama-ant", JZM_R(), MAJH, HID("هُوَ", ("«عِرْضِي»", "my honour", "namusuma"), naib=True), CL(0, "مُفَسِّرَةٌ لِـ«وَافِرٌ»", "explains «وَافِرٌ»", "«وَافِرٌ»u açıklar"), Dn("أَوْ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ " + DUR + "؛ أَيْ: «لَا يَكْلِمُ عِرْضِي عَيْبُ عَائِبٍ» " + ZAW, "or a second khabar, in the seat of raf' (al-Durra); that is, «no faultfinder's fault wounds my honour» (al-Zawzanī)", "yahut ikinci haber olarak mahallen merfû (Dürre); yani «hiçbir ayıplayanın ayıbı namusumu yaralamaz» (Zevzenî)"),
     HD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شَبَّهَ الْعِرْضَ بِجِسْمٍ يُجْرَحُ وَطَوَى الْمُشَبَّهَ بِهِ، وَأَثْبَتَ لِلْعِرْضِ الْكَلْمَ وَهُوَ مِنْ لَوَازِمِ الْجِسْمِ", "an isti'ara makniyya: honour is likened to a body that can be wounded, the body is folded away, and «wounding», which belongs to bodies, is given to honour", "istiâre-i mekniyye: namus yaralanabilen bir bedene benzetilmiş, beden dürülmüş, bedenin lâzımı olan «yaralanma» namusa verilmiştir", "istiara-makniyya", "aqsam-al-istiara"),
     g=["thulathi-mujarrad-babs"])])

# ---- v. 40 ----
V(40, "And when I am sober I do not fall short in giving; and my nature and my generosity are as you know them.",
  "Ayıldığımda da cömertlikte kusur etmem; huylarım ve cömertliğim bildiğin gibidir.",
 [pt("وَإِذَا", "idha", PRE("wa", "إِذَا"), IDHA_Z, Dn("«وَهٰذَانِ الْبَيْتَانِ قَدْ حَكَمَ الرُّوَاةُ بِتَقَدُّمِهِمَا فِي بَابِهِمَا» " + ZAW, "«the transmitters have judged these two verses the first of their kind» (al-Zawzanī)", "«râviler bu iki beytin kendi türlerinde önde olduğuna hükmetmiştir» (Zevzenî)"), s=[WA, ("إِذَا", "idha", "part")]),
  v("صَحَوْتُ", "saha", TU("ana"), CL_MI("إِذَا"), Dn("أَيْ: «إِذَا صَحَوْتُ مِنْ سُكْرِي … يُفَارِقُنِي السُّكْرُ وَلَا يُفَارِقُنِي الْجُودُ» " + ZAW, "that is, «when I wake from my drunkenness … drunkenness leaves me and generosity does not» (al-Zawzanī)", "yani «sarhoşluğumdan ayıldığımda … sarhoşluk benden ayrılır, cömertlik ayrılmaz» (Zevzenî)"), g=["naqis-verbs"]),
  pt("فَمَا", "ma-nafiya", Fr("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «إِذَا»، وَ«مَا» حَرْفُ نَفْيٍ", "the fa falls in the answer of «إِذَا»; مَا is a particle of negation", "fâ «إِذَا»nın cevabına girmiştir; «mâ» nefy harfi", "al-fa-fi-jawab-al-shart"), s=[FA, ("مَا", "ma-nafiya", "part")]),
  v("أُقَصِّرُ", "qassara", MUDR(), HID("أَنَا"), CL(0, "جَوَابُ «إِذَا»", "is the answer of «إِذَا»", "«إِذَا»nın cevabıdır"), g=["form-ii-verbs"]),
  pp("عَنْ", "an", HJ),
  n("نَدًى", "nada-ant", MJ("jA"), TA("أُقَصِّرُ"), Dn("وَالْأَلِفُ مَحْذُوفَةٌ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْمَكْتُوبَةُ دَلِيلٌ عَلَيْهَا " + DUR + "؛ النَّدَى: الْجُودُ", "the alif is dropped where two quiescents meet, and the written one points to it (al-Durra); النَّدَى: generosity", "elif iki sâkin buluştuğu için düşmüştür, yazılan elif ona delildir (Dürre); النَّدَى: cömertlik"))],
 [pt("وَكَمَا", "kama", Fr("الْوَاوُ عَاطِفَةٌ، وَالْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«مَا» حَرْفٌ مَصْدَرِيٌّ", "the waw conjoins; the kaf is a jarr letter of likening, and مَا makes a masdar", "vâv atıf; kâf teşbîh bildiren cer harfi, «mâ» masdar harfi", "atf-nasaq", "huruf-jarr", "an-masdariyya"),
     Fr("، وَ«مَا» وَالْفِعْلُ بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ", "; مَا with the verb after it makes a masdar in jarr by the kaf, and the phrase hangs on an omitted, fronted khabar", "; «mâ» ve ardındaki fiil kâf ile mecrûr masdar te'vîlindedir; câr-mecrûr öne alınmış mahzûf habere müteallik", "taqdim-al-musnad"),
     s=[WA, KA, ("مَا", "ma-masdariyya", "part")]),
  v("عَلِمْتِ", "alima", TU("anti"), CL(0, "صِلَةُ «مَا» الْمَصْدَرِيَّةِ", "is the sila of the masdar-making مَا", "masdar bildiren «mâ»nın sılasıdır"), Dn("وَالْمَفْعُولُ مَحْذُوفٌ تَقْدِيرُهُ: عَلِمْتِهَا " + DUR, "the object is left out — «as you know them» (al-Durra)", "mef'ûl hazfedilmiştir: «onları bildiğin gibi» (Dürre)"), g=["thulathi-mujarrad-babs"]),
  n("شَمَائِلِي", "shimal", RO("مُبْتَدَأٌ مُؤَخَّرٌ", "the mubtada, placed after its khabar", "sonraya bırakılmış mübtedâ", "rM", "mubtada-khabar"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"),
     Dn("جَمْعُ شِمَالٍ: الْخُلُقُ وَالطَّبْعُ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the plural of شِمَال, character, nature; the clause is conjoined to the one before", "شِمَال'in cem'i: huy, tabiat; cümle öncekine ma'tûftur", "jam-taksir"), s=[("شَمَائِلِ", "shimal", "noun"), P("ي")]),
  n("وَتَكَرُّمِي", "takarrum-ant", PRE("wa", "تَكَرُّمُ"), ATF("شَمَائِلِي", "rM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"),
     Dn("وَالْمِيمُ رَوِيُّ الْقَافِيَةِ وَيَاءُ الْمُتَكَلِّمِ بَعْدَهَا وَصْلٌ", "the mim is the rawī and the speaker's ya after it is the rhyme's extension (waṣl)", "mîm kâfiyenin revîsi, ardındaki mütekellim yâsı vasıldır", "al-qafiya", "masdar"), s=[WA, ("تَكَرُّمِ", "takarrum-ant", "noun"), P("ي")])])

# =====================================================================================================================
# Chapter 8 — هَلَّا سَأَلْتِ الْخَيْلَ (al-Zawzanī vv. 41–46)
# =====================================================================================================================
def SIFA_X(word="", s="j"):
    """a further na't (beyond the third) of a noun left unsaid"""
    a, e, t = SGN[s]
    return Fr("نَعْتٌ آخَرُ لِلْمَوْصُوفِ الْمَحْذُوفِ %s" % a, "a further na't of the noun left unsaid, %s" % e, "mahzûf mevsûfun bir başka na'tı, %s" % t, "naat-sifa", "hadhf-wa-taqdir", *_SG_TAGS.get(s, []))
HORSE = ("الْفَرَسِ", "the horse", "ata")

# ---- v. 41 ----
V(41, "Many a husband of a fair woman have I left thrown to the ground, his shoulder-muscle whistling like the split lip of a hare-lipped man,",
  "Nice güzel bir kadının kocasını yere serili bıraktım; omuz kası, yarık dudaklı birinin ağız kenarı gibi ıslık çalıyordu.",
 [n("وَحَلِيلِ", "halil-ant", PRE("wa-rubba", "حَلِيلِ"), Fr("مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ «رُبَّ» الْمُقَدَّرَةِ بَعْدَ الْوَاوِ",
       "the mubtada, in raf' by an estimated damma that the vowel of the near-added jarr letter رُبَّ, understood after the waw, keeps from showing", "mübtedâ; vâvdan sonra takdir edilen, zâide benzer «رُبَّ» cer harfinin harekesi yüzünden görünmeyen takdîrî damme ile merfû", "mubtada-khabar", "huruf-jarr"), MDF,
     Dn("وَخَبَرُهُ مَحْذُوفٌ تَقْدِيرُهُ: مَوْجُودٌ، أَوْ جُمْلَةُ «سَبَقَتْ يَدَايَ» فِي الْبَيْتِ بَعْدَهُ؛ وَيَجُوزُ أَنْ يَكُونَ مَفْعُولًا بِهِ مُقَدَّمًا لِـ«تَرَكْتُ» " + DUR + "؛ «الْحَلِيلُ — بِالْمُهْمَلَةِ —: الزَّوْجُ» " + ZAW,
        "its khabar is left out — «there is» — or it is the clause «سَبَقَتْ يَدَايَ» in the next verse; it may also be the fronted object of «تَرَكْتُ» (al-Durra); «الْحَلِيل, with the undotted ḥāʾ: the husband» (al-Zawzanī)", "haberi hazfedilmiştir: «vardır»; yahut sonraki beyitteki «سَبَقَتْ يَدَايَ» cümlesidir; «تَرَكْتُ»ün öne alınmış mef'ûlü olması da câizdir (Dürre); «الْحَلِيل — noktasız hâ ile —: koca» (Zevzenî)"),
     s=[WA, ("حَلِيلِ", "halil-ant", "noun")]),
  n("غَانِيَةٍ", "ghaniya-ant", MI(), Dn("«الْغَانِيَةُ: ذَاتُ الزَّوْجِ … وَقِيلَ: بَلِ الْبَارِعَةُ الْجَمَالِ الْمُسْتَغْنِيَةُ بِكَمَالِ جَمَالِهَا عَنِ التَّزَيُّنِ» " + ZAW, "«الْغَانِيَة: a married woman … or, it is said, a woman so beautiful that she needs no adornment» (al-Zawzanī)", "«الْغَانِيَة: kocalı kadın … yahut güzelliğinin kemâli ile süslenmeye ihtiyaç duymayan kadın» (Zevzenî)")),
  v("تَرَكْتُ", "taraka", TU("ana"), CL("j", "نَعْتٌ لِـ«حَلِيلِ غَانِيَةٍ»", "a na't of «حَلِيلِ غَانِيَةٍ»", "«حَلِيلِ غَانِيَةٍ»in na'tı", "jumla-sifa"), Dn("وَمَفْعُولُهُ الْأَوَّلُ مَحْذُوفٌ تَقْدِيرُهُ: تَرَكْتُهُ " + DUR, "its first object is left out — «I left him» (al-Durra)", "birinci mef'ûlü hazfedilmiştir: «onu bıraktım» (Dürre)", "mafulayn")),
  n("مُجَدَّلًا", "mujaddal-ant", MF2(), Dn("«جَدَّلْتُهُ: أَلْقَيْتُهُ عَلَى الْجَدَالَةِ، وَهِيَ الْأَرْضُ» " + ZAW, "«I threw him on the جَدَالَة, the ground» (al-Zawzanī)", "«onu جَدَالَة'ya, yani yere serdim» (Zevzenî)", "ism-maful"))],
 [v("تَمْكُو", "maka-ant", MUDR("w"), FAIL_BAD, CL("n", "مَفْعُولٌ ثَانٍ آخَرُ لِـ«تَرَكْتُ»", "a further second object of «تَرَكْتُ»", "«تَرَكْتُ»ün bir başka ikinci mef'ûlü", "mafulayn"), Dn("وَقِيلَ: حَالٌ، وَالْأَوَّلُ أَوْلَى " + DUR + "؛ «الْمُكَاءُ: الصَّفِيرُ» " + ZAW, "or a hal, the first being better (al-Durra); «الْمُكَاء: whistling» (al-Zawzanī)", "yahut hâl; birincisi evlâdır (Dürre); «الْمُكَاء: ıslık» (Zevzenî)"), g=["naqis-verbs"]),
  n("فَرِيصَتُهُ", "farisa-ant", FL(), IDF("هُ"), Dn("الْفَرِيصَةُ: لَحْمَةٌ بَيْنَ الْجَنْبِ وَالْكَتِفِ تَرْتَعِدُ عِنْدَ الْفَزَعِ", "الْفَرِيصَة: the flesh between flank and shoulder that quivers in fear", "الْفَرِيصَة: korkuda titreyen, böğürle omuz arasındaki et"), s=[("فَرِيصَةُ", "farisa-ant", "noun"), P("هُ")]),
  n("كَشِدْقِ", "shidq", JN("كَ", "شِدْقِ"), MDF, Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مَحْذُوفٍ", "; the jarr phrase hangs on the omitted na't of an omitted object", "; câr-mecrûr mahzûf bir mef'ûlün mahzûf sıfatına müteallik", "hadhf-wa-taqdir"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: «قَالَ أَكْثَرُهُمْ: شَبَّهَ سَعَةَ الطَّعْنِ بِسَعَةِ شِدْقِ الْأَعْلَمِ، وَقَالَ بَعْضُهُمْ: بَلْ شَبَّهَ صَوْتَ انْصِبَابِ الدَّمِ بِصَوْتِ خُرُوجِ النَّفَسِ مِنْ شِدْقِ الْأَعْلَمِ» " + ZAW + "؛ وَالْأَدَاةُ الْكَافُ",
        "here is a tashbih mursal: «most say he likens the width of the wound to the width of the split lip of a hare-lipped man; some say he likens the sound of the gushing blood to the sound of breath escaping from a hare-lipped man's lip» (al-Zawzanī); the tool is the kaf",
        "burada mürsel teşbîh vardır: «çoğu, yaranın genişliğini yarık dudaklının ağız kenarının genişliğine benzettiğini; bazıları da dökülen kanın sesini yarık dudaklının ağzından çıkan nefesin sesine benzettiğini söyler» (Zevzenî); edat kâf", "tashbih", "arkan-al-tashbih"),
     s=[KA, ("شِدْقِ", "shidq", "noun")]),
  n("الْأَعْلَمِ", "alam-harelip-ant", MI(), QA, Dn("«الْعَلَمُ: الشَّقُّ فِي الشَّفَةِ الْعُلْيَا» " + ZAW + "، وَالْأَعْلَمُ: الْمَشْقُوقُ الشَّفَةِ الْعُلْيَا", "«الْعَلَم is the split in the upper lip» (al-Zawzanī); الْأَعْلَم: one whose upper lip is split", "«الْعَلَم: üst dudaktaki yarık» (Zevzenî); الْأَعْلَم: üst dudağı yarık"))])

# ---- v. 42 ----
V(42, "My hands were quicker to him with a swift thrust and the spray of a piercing wound the colour of dragon's blood.",
  "Ellerim, hızlı bir mızrak darbesiyle ve rengi ejder kanı gibi olan, delip geçen bir yaranın serpintisiyle ona önce davrandı.",
 [v("سَبَقَتْ", "sabaqa", MADI_F, FAIL_BAD, CL("r", "خَبَرُ «حَلِيلِ» فِي الْبَيْتِ قَبْلَهُ", "the khabar of «حَلِيلِ» in the verse before", "önceki beyitteki «حَلِيلِ»in haberi", "anwa-al-khabar"), Dn("أَوْ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا إِنْ لَمْ يُجْعَلْ «حَلِيلِ» مُبْتَدَأً " + DUR, "or it opens a new sentence and has no seat, if «حَلِيلِ» is not taken as a mubtada (al-Durra)", "yahut «حَلِيلِ» mübtedâ sayılmazsa isti'nâfiyyedir, mahalli yoktur (Dürre)"), g=["thulathi-mujarrad-babs"]),
  n("يَدَايَ", "yad", FL("rD"), Fr("، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the nun is dropped for the annexation, and the ya is its second term, in the seat of jarr", "; izâfe sebebiyle nûn düşmüştür; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), s=[("يَدَا", "yad", "noun"), P("يَ")]),
  pp("لَهُ", "li", JP("لَ", "هُ", LAM_PRN), TA("سَبَقَتْ"), s=[("لَ", "li", "prep"), P("هُ")]),
  n("بِعَاجِلِ", "ajil-hadir", JN("بِ", "عَاجِلِ"), MDF, TA("سَبَقَتْ"), Dn("مِنْ إِضَافَةِ الصِّفَةِ إِلَى الْمَوْصُوفِ: بِطَعْنَةٍ عَاجِلَةٍ " + DUR, "the adjective annexed to the noun it describes — «with a swift thrust» (al-Durra)", "sıfat mevsûfuna izâfe edilmiştir: «hızlı bir darbeyle» (Dürre)"), s=[BI, ("عَاجِلِ", "ajil-hadir", "noun")]),
  n("طَعْنَةٍ", "tana-ant", MI())],
 [n("وَرَشَاشِ", "rashash-ant", PRE("wa", "رَشَاشِ"), ATF("عَاجِلِ"), MDF, s=[WA, ("رَشَاشِ", "rashash-ant", "noun")]),
  n("نَافِذَةٍ", "nafidha-ant", MI(), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — طَعْنَةٍ نَافِذَةٍ — " + DUR, "a na't of a noun left unsaid — a piercing thrust (al-Durra)", "mahzûf bir mevsûfun sıfatı — delip geçen bir darbe (Dürre)", "hadhf-wa-taqdir")),
  n("كَلَوْنِ", "lawn", JN("كَ", "لَوْنِ"), MDF, TAM("naat", "رَشَاشِ"), Dn("أَوْ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ: لَوْنُهُ كَلَوْنِ الْعَنْدَمِ " + DUR, "or on the omitted khabar of an omitted mubtada — «its colour is like …» (al-Durra)", "yahut mahzûf bir mübtedânın mahzûf haberine: «rengi … gibidir» (Dürre)"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: «طَعَنْتُهُ طَعْنَةً فِي عَجَلَةٍ تَرُشُّ دَمًا مِنْ طَعْنَةٍ نَافِذَةٍ تَحْكِي لَوْنَ الْعَنْدَمِ» " + ZAW + "؛ فَالْمُشَبَّهُ الرَّشَاشُ، وَالْمُشَبَّهُ بِهِ الْعَنْدَمُ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ اللَّوْنُ وَقَدْ ذُكِرَ فَهُوَ مُفَصَّلٌ",
        "here is a tashbih mursal: «I thrust at him with a swift thrust, spraying blood from a piercing wound that copies the colour of dragon's blood» (al-Zawzanī); the thing likened is the spray, the thing it is likened to the ʿandam, the tool the kaf, and the point of likeness — the colour — is said, so it is mufassal",
        "burada mürsel teşbîh vardır: «ona hızlı bir darbe vurdum; delip geçen yaradan, ejder kanının rengini andıran kan serpiyordu» (Zevzenî); müşebbeh serpinti, müşebbehün bih ʿandem, edat kâf; vech-i şebeh — renk — söylendiği için mufassaldır", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[KA, ("لَوْنِ", "lawn", "noun")]),
  n("الْعَنْدَمِ", "andam-ant", MI(), QA, Dn("«الْعَنْدَمُ: دَمُ الْأَخَوَيْنِ، وَقِيلَ: بَلْ هُوَ الْبَقَّمُ، وَقِيلَ: شَقَائِقُ النُّعْمَانِ» " + ZAW, "«الْعَنْدَم: dragon's blood (the red resin); or brazil-wood; or the red anemone» (al-Zawzanī)", "«الْعَنْدَم: ejder kanı (kırmızı reçine); yahut bakkam ağacı; yahut gelincik» (Zevzenî)"))])

# ---- v. 43 ----
V(43, "Why did you not ask the horsemen, daughter of Mālik, if you did not know what you had not learned?",
  "Ey Mâlik'in kızı, bilmediğin şeyi bilmiyorsan süvarilere sorsaydın ya!",
 [pt("هَلَّا", "halla", Fr("حَرْفُ تَحْضِيضٍ", "a particle urging (or reproaching)", "tahdîd harfi", "insha-wa-tamanni")),
  v("سَأَلْتِ", "saala", TU("anti"), CL_IST, g=["thulathi-mujarrad-babs"]),
  n("الْخَيْلَ", "khayl", MF(), Sn("وَفِيهِ مَجَازٌ مُرْسَلٌ: أَرَادَ بِالْخَيْلِ فُرْسَانَهَا — «هَلْ سَأَلْتِ الْفُرْسَانَ عَنْ حَالِي» " + ZAW, "here is a majaz mursal: by «the horses» he means their riders — «did you ask the horsemen about me?» (al-Zawzanī)", "burada mecâz-ı mürsel vardır: «atlar» ile binicilerini kastetmiştir — «süvarilere benim hâlimi sordun mu?» (Zevzenî)", "majaz-mursal"),
     HD("عَلَاقَتُهُ الْمَحَلِّيَّةُ: سَمَّى الرَّاكِبِينَ بِاسْمِ مَحَلِّهِمْ", "its tie is the place: the riders are called by the name of what they sit on", "alâkası mahalliyyedir: biniciler bulundukları yerin adıyla anılmıştır", "anwa-al-majaz")),
  n("يَابْنَةَ", "ibna-ant", Fr("«يَا» حَرْفُ نِدَاءٍ، وَ«ابْنَةَ» مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَسَقَطَتْ هَمْزَةُ وَصْلِهِ فِي الْخَطِّ", "يَا is the vocative particle; «ابْنَةَ» is the one called, annexed, in nasb by the fatha — its hamzat al-wasl drops in the writing", "«يَا» nidâ harfi; «ابْنَةَ» muzâf münâdâ, fetha ile mansûb; vasl hemzesi yazıda düşmüştür", "vocative-munada", "idafa-definiteness"),
     CL(0, "النِّدَائِيَّةُ مُعْتَرِضَةٌ", "(the call) stands between and", "(nidâ cümlesi) araya girmiştir"), s=[("يَا", "ya-nida", "part"), ("بْنَةَ", "ibna-ant", "noun")]),
  pn("مَالِكٍ", "malik-name", MI(), Dn("وَهُوَ أَبُو عَبْلَةَ", "he is ʿAbla's father", "Able'nin babasıdır"))],
 [pt("إِنْ", "in-shartiyya", Fr("حَرْفُ شَرْطٍ جَازِمٌ", "the conditional particle that puts in jazm", "cezmeden şart harfi", "in-shartiyya", "al-majzum-wal-shart-wal-jaza"), Dn("وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ تَقْدِيرُهُ: فَاسْأَلِي " + DUR, "its answer is left out, pointed to by what goes before — «then ask» (al-Durra)", "cevabı hazfedilmiştir, öncesi ona delâlet eder: «o hâlde sor» (Dürre)", "ijaz-al-hadhf")),
  v("كُنْتِ", "kana", Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَتَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ", "the defective past verb, built on sukun, in the seat of jazm as the verb of the condition; the ta of the woman addressed is the noun of كَانَ, in the seat of raf'", "sükûn üzere mebnî nâkıs mâzî, şart fiili olarak mahallen meczûm; muhâtaba tâsı كَانَ'nin ismidir, mahallen merfû", "kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil", "al-majzum-wal-shart-wal-jaza")),
  n("جَاهِلَةً", "jahil", RO("خَبَرُ كَانَ", "the predicate of كَانَ", "كَانَ'nin haberi", "n", "kana-wa-akhawatuha")),
  pp("بِمَا", "ma-mawsula", Fr("الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ", "the ba is a jarr letter, and مَا a relative noun built on sukun, in the seat of jarr", "bâ cer harfi; «mâ» sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr", "huruf-jarr", "ism-mawsul"), TA("جَاهِلَةً"),
     Dn("وَإِنْ جَعَلْتَ الْبَاءَ بِمَعْنَى «عَنْ» تَعَلَّقَتْ بِـ«سَأَلْتِ» وَكَانَتِ الشَّرْطِيَّةُ مُعْتَرِضَةً " + DUR, "if the ba is taken to mean «about», it hangs on «سَأَلْتِ» and the conditional clause stands between (al-Durra)", "bâ «عَنْ» anlamında alınırsa «سَأَلْتِ»e müteallik olur ve şart cümlesi araya girmiş olur (Dürre)"), s=[BI, ("مَا", "ma-mawsula", "pron")]),
  pt("لَمْ", "lam-jazim", LAM_J),
  v("تَعْلَمِي", "alima", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a present verb in jazm by لَمْ, its sign the dropping of the nun — it is one of the five verbs; the ya of the woman addressed is its doer, in the seat of raf'", "«lem» ile meczûm muzâri, ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; muhâtaba yâsı fâildir, mahallen merfû", "afal-khamsa", "lam-jazim", "al-bariz-al-muttasil"),
     CL_SILA, Dn("وَالْعَائِدُ مَحْذُوفٌ: بِمَا لَمْ تَعْلَمِيهِ " + DUR + "؛ وَالْمِيمُ رَوِيُّ الْقَافِيَةِ وَالْيَاءُ بَعْدَهَا وَصْلٌ", "the returning pronoun is left out — «what you have not learned» (al-Durra); the mim is the rawī and the ya after it the waṣl", "dönen zamir hazfedilmiştir: «bilmediğin şey» (Dürre); mîm revî, ardındaki yâ vasıldır", "al-qafiya"), g=["thulathi-mujarrad-babs"])])

# ---- v. 44 ----
V(44, "— when I never left the saddle of a swimming, full-bodied horse, wounded, whom the armed champions took turns at striking;",
  "— ben, zırhlı yiğitlerin sırayla vurduğu, yaralı, iri, yüzer gibi koşan bir atın eyerinden hiç ayrılmazken;",
 [n("إِذْ", "idh", Fr("ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«سَأَلْتِ» فِي الْبَيْتِ قَبْلَهُ", "an adverb of past time, built on sukun, in the seat of nasb, hanging on «سَأَلْتِ» in the verse before", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb, önceki beyitteki «سَأَلْتِ»e müteallik", "maful-fih")),
  pt("لَا", "la-nafiya", Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi")),
  v("أَزَالُ", "zala-ant", Fr("فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَرْفُوعٌ بِالضَّمَّةِ", "a defective present verb, a sister of كَانَ, in raf' by the damma", "كَانَ'nin kardeşlerinden nâkıs muzâri, damme ile merfû", "kana-wa-akhawatuha", "mudari-marfu"), NAQ_SUB("أَنَا"), CL_MI("إِذْ"), g=["hollow-verbs"]),
  pp("عَلَى", "ala", HJ),
  n("رِحَالَةِ", "rihala-ant", MJ(), MDF, TAM("khabar", "أَزَالُ"), Dn("الرِّحَالَةُ: السَّرْجُ؛ «يَقُولُ: هَلَّا سَأَلْتِ الْفُرْسَانَ عَنْ حَالِي إِذْ لَمْ أَزَلْ عَلَى سَرْجِ فَرَسٍ سَابِحٍ» " + ZAW, "الرِّحَالَة: a saddle; «why did you not ask the horsemen about me, when I never left the saddle of a swimming horse?» (al-Zawzanī)", "الرِّحَالَة: eyer; «hiç ayrılmadığım hâlde, yüzer gibi koşan bir atın eyerinden, süvarilere hâlimi sorsaydın ya» (Zevzenî)")),
  n("سَابِحٍ", "sabih-ant", MI(), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — فَرَسٍ — " + DUR, "a na't of a noun left unsaid — a horse (al-Durra)", "mahzûf bir mevsûfun — atın — sıfatıdır (Dürre)", "ism-fail", "hadhf-wa-taqdir"),
     HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي «سَابِحٍ»: شُبِّهَ عَدْوُ الْفَرَسِ وَمَدُّهُ يَدَيْهِ بِالسِّبَاحَةِ، ثُمَّ اشْتُقَّ مِنْهَا اسْمُ الْفَاعِلِ", "an isti'ara taba'iyya in «سَابِحٍ»: the horse's running, stretching out its forelegs, is likened to swimming, and the active participle is derived from it", "«سَابِحٍ»de istiâre-i tebeiyye: atın ön ayaklarını uzatarak koşması yüzmeye benzetilmiş, sonra ondan ism-i fâil türetilmiştir", "istiara-tabaiyya", "aqsam-al-istiara"))],
 [n("نَهْدٍ", "nahd-ant", SIFA_MD("ثَانٍ"), Dn("«وَنَهْدٌ مِنْ صِفَةِ السَّابِحِ، وَهُوَ الضَّخْمُ» " + ZAW, "«نَهْد describes the swimmer: big» (al-Zawzanī)", "«نَهْد yüzücünün sıfatıdır: iri» (Zevzenî)")),
  v("تَعَاوَرُهُ", "taawara-ant", MUDR(), OBJ("هُ"), FAIL_BAD, CL("j", "نَعْتٌ ثَالِثٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "a third na't of the noun left unsaid", "mahzûf mevsûfun üçüncü na'tı", "jumla-sifa"), Dn("أَوْ حَالٌ مِنْهُ بَعْدَ وَصْفِهِ " + DUR + "؛ وَأَصْلُهُ تَتَعَاوَرُهُ فَحُذِفَتْ إِحْدَى التَّاءَيْنِ؛ «التَّعَاوُرُ: التَّدَاوُلُ، يُقَالُ: تَعَاوَرُوهُ ضَرْبًا: جَعَلُوا يَضْرِبُونَهُ عَلَى جِهَةِ التَّنَاوُبِ» " + ZAW,
       "or a hal of it, once described (al-Durra); it is تَتَعَاوَرُهُ with one ta dropped; «التَّعَاوُر is passing round: ‹they took turns at him with blows› — they struck him by turns» (al-Zawzanī)", "yahut nitelendikten sonra ondan hâl (Dürre); aslı تَتَعَاوَرُهُ'dur, iki tâdan biri hazfedilmiştir; «التَّعَاوُر: sırayla yapmak — ‹ona sırayla vurdular›» (Zevzenî)"), g=["form-vi-verbs"], s=[("تَعَاوَرُ", "taawara-ant", "verb"), P("هُ")]),
  n("الْكُمَاةُ", "kamiyy-ant", FL("rA"), Dn("جَمْعُ كَمِيٍّ: الشُّجَاعُ الْمُتَكَمِّي فِي سِلَاحِهِ", "the plural of كَمِيّ, the brave man hidden in his armour", "كَمِيّ'nin cem'i: silahına bürünmüş yiğit", "jam-taksir")),
  n("مُكَلَّمِ", "mukallam-ant", SIFA_X(), QT, Dn("«الْكَلْمُ: الْجَرْحُ، وَالتَّكْلِيمُ: التَّجْرِيحُ» " + ZAW + "؛ أَيْ «جَرَحَهُ كُلٌّ مِنْهُمْ»", "«الْكَلْم is a wound; التَّكْلِيم is wounding again and again» (al-Zawzanī) — «each of them wounded it»", "«الْكَلْم: yara; التَّكْلِيم: tekrar tekrar yaralamak» (Zevzenî) — «her biri onu yaraladı»", "ism-maful"))])

# ---- v. 45 ----
V(45, "At one turn he is stripped out for the spear-thrusting, and at another he draws back to a host of strong bows, vast in number.",
  "Kimi zaman mızrak dövüşü için (saftan) çıkarılır, kimi zaman da sağlam yaylı, kalabalık bir orduya sığınır.",
 [n("طَوْرًا", "tawr", ZZ(), ZT("يُجَرَّدُ"), Dn("«الطَّوْرُ: التَّارَةُ وَالْمَرَّةُ، وَالْجَمْعُ الْأَطْوَارُ» " + ZAW, "«الطَّوْر: a turn, a time; pl. أَطْوَار» (al-Zawzanī)", "«الطَّوْر: kere, defa; ç. أَطْوَار» (Zevzenî)")),
  v("يُجَرَّدُ", "jarrada-ant", MUDR(), MAJH, HID("هُوَ", HORSE, naib=True), CL_IST,
     HD("بَيْنَهُ وَبَيْنَ «يَأْوِي» طِبَاقٌ: إِفْرَادُهُ مِنَ الصَّفِّ لِلطِّعَانِ وَأُوِيُّهُ إِلَى الْجَمَاعَةِ مَعْنَيَانِ مُتَقَابِلَانِ فِي الْجُمْلَةِ", "it makes a tibaq with «يَأْوِي»: being singled out of the ranks for the fight and drawing back to the host are meanings opposed in the main", "«يَأْوِي» ile tıbâk oluşturur: dövüş için saftan ayrılmak ve topluluğa sığınmak genel olarak karşıt iki mânâdır", "tibaq"), g=["form-ii-verbs"]),
  n("لِلطِّعَانِ", "tian-ant", JN("لِ", "الطِّعَانِ"), TA("يُجَرَّدُ"), Dn("«يَقُولُ: مَرَّةً أُجَرِّدُهُ مِنْ صَفِّ الْأَوْلِيَاءِ لِطَعْنِ الْأَعْدَاءِ وَضَرْبِهِمْ» " + ZAW, "«at one time I strip him out of the line of friends to thrust at the enemy and strike them» (al-Zawzanī)", "«bir kere onu dostların safından düşmanlara mızrak saplamak ve vurmak için çıkarırım» (Zevzenî)", "masdar"), s=[LI, ("الطِّعَانِ", "tian-ant", "noun")]),
  n("وَتَارَةً", "tara-time", PRE("wa", "تَارَةً"), ZZ(), ZT("يَأْوِي"), s=[WA, ("تَارَةً", "tara-time", "noun")])],
 [v("يَأْوِي", "awa-shelter", MUDR("y"), HID("هُوَ", HORSE), CL(0, "مَعْطُوفَةٌ عَلَى «يُجَرَّدُ»", "is conjoined to «يُجَرَّدُ»", "«يُجَرَّدُ»a ma'tûftur"), HD("وَهُوَ الطَّرَفُ الثَّانِي مِنْ طِبَاقِ «يُجَرَّدُ»", "it is the second term of the tibaq with «يُجَرَّدُ»", "«يُجَرَّدُ» ile kurulan tıbâkın ikinci ucudur", "tibaq"), g=["naqis-verbs"]),
  pp("إِلَى", "ila", HJ),
  n("حَصِدِ", "hasid-ant", MJ(), MDF, TA("يَأْوِي"), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، مِنْ إِضَافَةِ الْوَصْفِ إِلَى فَاعِلِهِ " + DUR + "؛ «حَصِدَ الشَّيْءُ حَصَدًا إِذَا اسْتَحْكَمَ» " + ZAW, "a na't of a noun left unsaid, the adjective annexed to its own doer (al-Durra); «حَصِدَ: a thing grew firm» (al-Zawzanī)", "mahzûf bir mevsûfun sıfatı, vasıf fâiline izâfe edilmiştir (Dürre); «حَصِدَ: bir şey sağlamlaştı» (Zevzenî)", "hadhf-wa-taqdir"),
     Sn("وَهُوَ كِنَايَةٌ عَنِ الرُّمَاةِ: «أَرَادَ أَنَّهُمْ رُمَاةٌ مَعَ كَثْرَةِ عَدَدِهِمْ» " + ZAW, "it is a kinaya for archers: «he means they are archers, and many» (al-Zawzanī)", "okçulardan kinâyedir: «onların çok sayıda okçu olduğunu kasteder» (Zevzenî)", "kinaya")),
  n("الْقِسِيِّ", "qaws", MI(), Dn("جَمْعُ قَوْسٍ", "the plural of قَوْس, a bow", "قَوْس'un cem'i", "jam-taksir")),
  n("عَرَمْرَمِ", "aramram-ant", SIFA_MD("ثَانٍ"), QT, Dn("«الْعَرَمْرَمُ: الْكَثِيرُ» " + ZAW, "«الْعَرَمْرَم: numerous» (al-Zawzanī)", "«الْعَرَمْرَم: çok, kalabalık» (Zevzenî)"))])

# ---- v. 46 ----
V(46, "Whoever was present at the battle will tell you that I plunge into the fray and hold back at the sharing of the spoil.",
  "Savaşta bulunan herkes sana haber verir ki ben savaşın içine dalarım ve ganimet paylaşılırken iffetli davranırım.",
 [v("يُخْبِرْكِ", "akhbara", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، لِأَنَّهُ جَوَابُ الطَّلَبِ فِي «هَلَّا سَأَلْتِ»، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ",
       "a present verb in jazm by the sukun, being the answer to the request in «why did you not ask»; the kaf is its first object, in the seat of nasb", "sükûn ile meczûm muzâri, «sorsaydın ya» talebinin cevabıdır; kâf birinci mef'ûldür, mahallen mansûb", "jawazim-al-mudari-wal-amr-fil-kafiya", "al-bariz-al-muttasil", "maful-bihi"),
     FAIL_BAD, CL(0, "جَوَابُ الطَّلَبِ", "is the answer to a request", "talebin cevabıdır"), Dn("«يُخْبِرْكِ: مَجْزُومٌ لِأَنَّهُ جَوَابُ هَلَّا سَأَلْتِ» " + ZAW, "«يُخْبِرْكِ is in jazm as the answer of ‹why did you not ask›» (al-Zawzanī)", "«يُخْبِرْكِ, ‹sorsaydın ya›nın cevabı olduğu için meczûmdur» (Zevzenî)"), g=["form-iv-verbs"], s=[("يُخْبِرْ", "akhbara", "verb"), P("كِ")]),
  n("مَنْ", "man", Fr("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a relative noun built on sukun, the doer, in the seat of raf'", "sükûn üzere mebnî ism-i mevsûl, fâil, mahallen merfû", "ism-mawsul", "fail")),
  v("شَهِدَ", "shahida", MADI, HID("هُوَ", ("«مَنْ»", "«مَنْ»", "«مَنْ»e")), CL_SILA, g=["thulathi-mujarrad-babs"]),
  n("الْوَقِيعَةَ", "waqia-ant", MF(), Dn("«الْوَقْعَةُ وَالْوَقِيعَةُ: اسْمَانِ مِنْ أَسْمَاءِ الْحُرُوبِ» " + ZAW, "«الْوَقْعَة and الْوَقِيعَة are names for battle» (al-Zawzanī)", "«الْوَقْعَة ve الْوَقِيعَة savaşın adlarındandır» (Zevzenî)")),
  pt("أَنَّنِي", "anna", Fr("حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "the particle of emphasis that puts its noun in nasb; the nun protects; the ya is its noun, in the seat of nasb", "te'kîd ve nasb harfi; nûn vikâye içindir; yâ ismidir, mahallen mansûb", "inna-wa-akhawatuha", "al-bariz-al-muttasil"),
     Dn("وَ«أَنَّ» وَاسْمُهَا وَخَبَرُهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «يُخْبِرْ» الثَّانِي وَالثَّالِثِ " + DUR, "أَنَّ with its noun and predicate makes a masdar that stands for the second and third objects of «يُخْبِرْ» (al-Durra)", "«أَنَّ», ismi ve haberiyle, «يُخْبِرْ»ün ikinci ve üçüncü mef'ûllerinin yerini tutan masdar te'vîlindedir (Dürre)", "an-masdariyya"), s=[("أَنَّ", "anna", "part"), ("نِ", "nun-wiqaya", "part"), P("ي")])],
 [v("أَغْشَى", "ghashiya", MUDR("a"), HID("أَنَا"), CL("r", "خَبَرُ «أَنَّ»", "the predicate of أَنَّ", "«أَنَّ»nin haberi", "inna-wa-akhawatuha"),
     HD("بَيْنَهُ وَبَيْنَ «أَعِفُّ» طِبَاقٌ: الْإِقْدَامُ عَلَى الشَّيْءِ وَالْكَفُّ عَنْهُ مَعْنَيَانِ مُتَقَابِلَانِ فِي الْجُمْلَةِ", "it makes a tibaq with «أَعِفُّ»: going in at a thing and holding back from it are meanings opposed in the main", "«أَعِفُّ» ile tıbâk oluşturur: bir şeye atılmak ve ondan geri durmak genel olarak karşıt iki mânâdır", "tibaq"), g=["thulathi-mujarrad-babs"]),
  n("الْوَغَى", "wagha", MF("nA"), Sn("«الْوَغَى: أَصْوَاتُ أَهْلِ الْحَرْبِ، ثُمَّ اسْتُعِيرَ لِلْحَرْبِ» " + ZAW + "، فَهُوَ مَجَازٌ نُقِلَ مِنْ صَوْتِ الْحَرْبِ إِلَيْهَا", "«الْوَغَى is the cries of men at war, then borrowed for war itself» (al-Zawzanī): a majaz carried over from the sound of battle to battle", "«الْوَغَى savaşanların sesleridir, sonra savaşın kendisi için istiare edilmiştir» (Zevzenî): savaşın sesinden savaşa nakledilmiş bir mecâz", "haqiqa-majaz")),
  v("وَأَعِفُّ", "affa-ant", PRE("wa", "أَعِفُّ"), MUDR(), HID("أَنَا"), CL("r", "مَعْطُوفَةٌ عَلَى «أَغْشَى»", "conjoined to «أَغْشَى»", "«أَغْشَى»ya ma'tûf"),
     HD("وَهُوَ الطَّرَفُ الثَّانِي مِنْ طِبَاقِ «أَغْشَى»", "it is the second term of the tibaq with «أَغْشَى»", "«أَغْشَى» ile kurulan tıbâkın ikinci ucudur", "tibaq"),
     Sn("وَالْعِفَّةُ عِنْدَ الْمَغْنَمِ كِنَايَةٌ عَنْ كَرَمِهِ وَعُلُوِّ هِمَّتِهِ: «يُخْبِرْكِ مَنْ حَضَرَ الْحَرْبَ بِأَنِّي كَرِيمٌ عَالِي الْهِمَّةِ، آتِي فِي الْحُرُوبِ وَأَعِفُّ عَنِ اغْتِنَامِ الْأَمْوَالِ» " + ZAW, "holding back at the spoil is a kinaya for his nobility and high aim: «whoever was at the battle will tell you that I am noble and high-minded, coming on in war and holding back from taking the goods» (al-Zawzanī)", "ganimette iffetli davranmak, cömertliğinden ve himmetinin yüceliğinden kinâyedir: «savaşta bulunan sana haber verir ki ben cömert ve yüksek himmetliyim; savaşa gelir, malları ganimet almaktan geri dururum» (Zevzenî)", "kinaya"),
     g=["doubled-verbs"], s=[WA, ("أَعِفُّ", "affa-ant", "verb")]),
  n("عِنْدَ", "inda", ZM(), MDF, ZT("أَعِفُّ")),
  n("الْمَغْنَمِ", "maghnam", MI(), QA, Dn("«الْمَغْنَمُ وَالْغُنْمُ وَالْغَنِيمَةُ وَاحِدٌ» " + ZAW, "«الْمَغْنَم, الْغُنْم and الْغَنِيمَة are one: spoil» (al-Zawzanī)", "«الْمَغْنَم, الْغُنْم ve الْغَنِيمَة birdir: ganimet» (Zevzenî)"))])

# =====================================================================================================================
# Chapter 9 — الْمُدَجَّجُ، وَحَامِي الْحَقِيقَةِ (al-Zawzanī vv. 47–52)
# =====================================================================================================================
RUBBA_MB = Fr("مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ «رُبَّ» الْمُقَدَّرَةِ بَعْدَ الْوَاوِ",
              "the mubtada, in raf' by an estimated damma that the vowel of the near-added jarr letter رُبَّ, understood after the waw, keeps from showing", "mübtedâ; vâvdan sonra takdir edilen, zâide benzer «رُبَّ» cer harfinin harekesi yüzünden görünmeyen takdîrî damme ile merfû", "mubtada-khabar", "huruf-jarr")
MAN_D = ("الْمَوْصُوفِ الْمَحْذُوفِ", "the man left unsaid", "mahzûf mevsûfa")

# ---- v. 47 ----
V(47, "And many a man in full armour, whose combat the champions shunned, neither hasty to flee nor one to yield,",
  "Nice tepeden tırnağa silahlı adam ki yiğitler onunla vuruşmaktan çekinirdi; ne kaçmaya koşan biriydi ne de teslim olan,",
 [n("وَمُدَجَّجٍ", "mudajjaj-ant", PRE("wa-rubba", "مُدَجَّجٍ"), RUBBA_MB, Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، وَخَبَرُهُ فِي الْبَيْتِ التَّالِي " + DUR + "؛ «الْمُدَجَّجُ وَالْمُدَجِّجُ: التَّامُّ السِّلَاحِ» " + ZAW,
       "it is a na't of a noun left unsaid, and its khabar is in the next verse (al-Durra); «الْمُدَجَّج, or الْمُدَجِّج: one fully armed» (al-Zawzanī)", "mahzûf bir mevsûfun sıfatıdır, haberi sonraki beyittedir (Dürre); «الْمُدَجَّج yahut الْمُدَجِّج: silahı tam olan» (Zevzenî)", "ism-maful", "hadhf-wa-taqdir"), s=[WA, ("مُدَجَّجٍ", "mudajjaj-ant", "noun")]),
  v("كَرِهَ", "kariha", MADI, FAIL_BAD, CL("j", "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ", "a second na't of the noun left unsaid", "mahzûf mevsûfun ikinci na'tı", "jumla-sifa"),
     Sn("وَهُوَ كِنَايَةٌ عَنْ شِدَّةِ بَأْسِهِ: «كَانَتِ الْأَبْطَالُ تَكْرَهُ نِزَالَهُ وَقِتَالَهُ لِفَرْطِ بَأْسِهِ وَصِدْقِ مِرَاسِهِ» " + ZAW, "it is a kinaya for his great might: «the champions hated to meet him in combat for his excessive might and his true hardihood» (al-Zawzanī)", "gücünün şiddetinden kinâyedir: «kahramanlar, aşırı gücü ve sağlam savaşçılığı yüzünden onunla vuruşmaktan hoşlanmazdı» (Zevzenî)", "kinaya"), g=["thulathi-mujarrad-babs"]),
  n("الْكُمَاةُ", "kamiyy-ant", FL("rA")),
  n("نِزَالَهُ", "nizal-ant", MF(), IDF("هُ"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ وَفَاعِلُهُ مَحْذُوفٌ " + DUR, "the masdar annexed to its object, its doer left out (al-Durra)", "masdar mef'ûlüne izâfe edilmiş, fâili hazfedilmiştir (Dürre)", "masdar"), s=[("نِزَالَ", "nizal-ant", "noun"), P("هُ")])],
 [pt("لَا", "la-nafiya", Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi")),
  n("مُمْعِنٍ", "mumin-ant", SIFA_MD("ثَالِثٌ"), Dn("«الْإِمْعَانُ: الْإِسْرَاعُ فِي الشَّيْءِ وَالْغُلُوُّ فِيهِ» " + ZAW, "«الْإِمْعَان: hastening in a thing and going far in it» (al-Zawzanī)", "«الْإِمْعَان: bir işte acele etmek ve aşırı gitmek» (Zevzenî)", "ism-fail")),
  n("هَرَبًا", "harab", RO("مَفْعُولٌ مُطْلَقٌ مِنْ مَعْنَى عَامِلِهِ", "an absolute object in the sense of its governor", "âmilinin anlamından mef'ûl-i mutlak", "n", "maful-mutlaq"), Dn("قَالَهُ التِّبْرِيزِيُّ، لِأَنَّ «لَا مُمْعِنٍ» بِمَعْنَى لَا هَارِبٍ؛ وَرَأَى الدُّرَّةُ أَنَّهُ مَنْصُوبٌ بِنَزْعِ الْخَافِضِ " + DUR, "so al-Tibrīzī, since «not hastening» means «not fleeing»; al-Durra holds it is in nasb for a dropped jarr letter (al-Durra)", "Tebrîzî böyle der, çünkü «لَا مُمْعِنٍ», «kaçmayan» anlamındadır; Dürre ise cer harfinin düşmesiyle mansûb olduğunu düşünür (Dürre)", "masdar")),
  pt("وَلَا", "la", Fr("الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ", "the waw conjoins; لَا is added to strengthen the negation", "vâv atıf; «lâ» nefyi pekiştirmek için zâiddir", "atf-nasaq", "huruf-al-ziyada-fil-kafiya"), s=[WA, ("لَا", "la", "part")]),
  n("مُسْتَسْلِمِ", "mustaslim-ant", ATF("مُمْعِنٍ"), QT, Dn("وَفَاعِلُهُمَا ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى الْمَوْصُوفِ الْمَحْذُوفِ " + DUR + "؛ «الِاسْتِسْلَامُ: الِانْقِيَادُ وَالِاسْتِكَانَةُ» " + ZAW, "the doer of both is a hidden pronoun returning to the man left unsaid (al-Durra); «الِاسْتِسْلَام: yielding, submitting» (al-Zawzanī)", "ikisinin fâili mahzûf mevsûfa dönen gizli zamirdir (Dürre); «الِاسْتِسْلَام: boyun eğmek, teslim olmak» (Zevzenî)", "ism-fail"))])

# ---- v. 48 ----
V(48, "— my hand was generous to him with a swift thrust from a straightened spear, hard of joint, true.",
  "— elim ona, boğumları sert, düzeltilmiş, doğrultulmuş bir mızrakla hızlı bir darbe ikram etti.",
 [v("جَادَتْ", "jada", MADI_F, FAIL_BAD, CL("r", "خَبَرُ «مُدَجَّجٍ» فِي الْبَيْتِ قَبْلَهُ", "the khabar of «مُدَجَّجٍ» in the verse before", "önceki beyitteki «مُدَجَّجٍ»in haberi", "anwa-al-khabar"), Dn("«وَالْبَيْتُ جَوَابُ رُبَّ الْمُضْمَرِ بَعْدَ الْوَاوِ فِي: وَمُدَجَّجٍ» " + ZAW, "«the verse answers the رُبَّ understood after the waw in ‹and many a man in full armour›» (al-Zawzanī)", "«beyit, ‹ve nice silahlı› sözündeki vâvdan sonra gizli رُبَّ'nin cevabıdır» (Zevzenî)"),
     HD("اسْتِعَارَةٌ تَهَكُّمِيَّةٌ: اسْتَعْمَلَ «الْجُودَ» — وَهُوَ الْعَطَاءُ — فِي ضِدِّهِ، الطَّعْنَةِ الْقَاتِلَةِ، لِلتَّهَكُّمِ", "an isti'ara of mockery: he uses «generosity» — giving — for its opposite, the deadly thrust, in mockery", "istiâre-i tehekkümiyye: «cömertlik» (vermek) kelimesini, alay için zıddı olan öldürücü darbe hakkında kullanmıştır", "istiara", "aqsam-al-istiara"), g=["hollow-verbs"]),
  pp("لَهُ", "li", JP("لَ", "هُ", LAM_PRN), TA("جَادَتْ"), s=[("لَ", "li", "prep"), P("هُ")]),
  n("كَفِّي", "kaff-hand", FL("rM"), Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), Dn("وَعِنْدَ الدُّرَّةِ «يَدَايَ»", "al-Durra reads «يَدَايَ», my two hands", "Dürre «يَدَايَ» okur"), s=[("كَفِّ", "kaff-hand", "noun"), P("ي")]),
  n("بِعَاجِلِ", "ajil-hadir", JN("بِ", "عَاجِلِ"), MDF, TA("جَادَتْ"), Dn("«قَدَّمَ الصِّفَةَ عَلَى الْمَوْصُوفِ ثُمَّ أَضَافَهَا إِلَيْهِ، تَقْدِيرُهُ: بِطَعْنَةٍ عَاجِلَةٍ» " + ZAW, "«he put the adjective before its noun and annexed it to it — that is, ‹with a swift thrust›» (al-Zawzanī)", "«sıfatı mevsûftan önce getirip ona izâfe etmiştir; takdiri: hızlı bir darbeyle» (Zevzenî)"), s=[BI, ("عَاجِلِ", "ajil-hadir", "noun")]),
  n("طَعْنَةٍ", "tana-ant", MI())],
 [n("بِمُثَقَّفٍ", "muthaqqaf-ant", JN("بِ", "مُثَقَّفٍ"), TAM("naat", "طَعْنَةٍ"), Dn("وَقِيلَ: بِـ«عَاجِلِ»، وَالْأَوَّلُ أَقْوَى؛ وَ«مُثَقَّفٍ» صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR, "some hang it on «عَاجِلِ», the first being stronger; «مُثَقَّفٍ» is a na't of a noun left unsaid (al-Durra)", "kimi onu «عَاجِلِ»e bağlar, birincisi daha güçlüdür; «مُثَقَّفٍ» mahzûf bir mevsûfun sıfatıdır (Dürre)", "ism-maful", "hadhf-wa-taqdir"),
     HD("كِنَايَةٌ عَنْ مَوْصُوفٍ: ذَكَرَ الرُّمْحَ بِصِفَاتٍ تَجْتَمِعُ لَهُ — مُثَقَّفٍ صَدْقِ الْكُعُوبِ مُقَوَّمٍ — وَلَمْ يُسَمِّهِ، كَمَا فَسَّرَهُ الزَّوْزَنِيُّ: «بِرُمْحٍ مُقَوَّمٍ صُلْبِ الْكُعُوبِ»", "a kinaya for a thing described: he names the spear only by attributes that meet in it — straightened, hard of joint, true — as al-Zawzanī spells it out: «with a straightened spear, hard of joint»", "mevsûftan kinâye: mızrağı adını anmadan onda birleşen sıfatlarla — düzeltilmiş, boğumları sert, doğrultulmuş — anmıştır; Zevzenî'nin açıkladığı gibi: «boğumları sert, doğrultulmuş bir mızrakla»", "kinaya", "aqsam-al-kinaya"),
     s=[BI, ("مُثَقَّفٍ", "muthaqqaf-ant", "noun")]),
  n("صَدْقِ", "sadq-ant", SIFA_MD("ثَانٍ"), MDF, Dn("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا " + DUR + "؛ «الصَّدْقُ: الصُّلْبُ» " + ZAW, "the sifa mushabbaha annexed to its own doer (al-Durra); «الصَّدْق: hard» (al-Zawzanī)", "sıfat-ı müşebbehe fâiline izâfe edilmiştir (Dürre); «الصَّدْق: sert» (Zevzenî)", "sifa-mushabbaha")),
  n("الْكُعُوبِ", "kab-ant", MI(), Dn("جَمْعُ كَعْبٍ: عُقْدَةُ الْقَنَاةِ", "the plural of كَعْب, a knot of the spear-shaft", "كَعْب'ın cem'i: mızrak sapının boğumu", "jam-taksir")),
  n("مُقَوَّمِ", "muqawwam-ant", SIFA_MD("ثَالِثٌ"), QT, Dn("اسْمُ مَفْعُولٍ مِنْ قَوَّمَ: مُعَدَّلٌ", "the passive participle of قَوَّمَ: set straight", "قَوَّمَ'den ism-i mef'ûl: doğrultulmuş", "ism-maful"))])

# ---- v. 49 ----
V(49, "And I ran him through, clothes and all, with the hard spear — the noble man is not forbidden to the spears.",
  "Sert mızrakla elbiselerini (bedenine) diktim; soylu kişi mızraklara haram değildir.",
 [v("فَشَكَكْتُ", "shakka", PRE("fa", "شَكَكْتُ"), TU("ana"), CL(0, "مَعْطُوفَةٌ عَلَى «جَادَتْ» فِي الْبَيْتِ قَبْلَهُ", "is conjoined to «جَادَتْ» in the verse before", "önceki beyitteki «جَادَتْ»e ma'tûftur"), Dn("فَهِيَ فِي مَحَلِّ رَفْعٍ مِثْلُهَا " + DUR + "؛ «الشَّكُّ: الِانْتِظَامُ، وَالْفِعْلُ شَكَّ يَشُكُّ» " + ZAW, "so it is in the seat of raf' like it (al-Durra); «الشَّكّ is stringing through; the verb شَكَّ يَشُكُّ» (al-Zawzanī)", "dolayısıyla o da onun gibi mahallen merfûdur (Dürre); «الشَّكّ: dizmek, geçirmek; fiili شَكَّ يَشُكُّ» (Zevzenî)"),
     g=["doubled-verbs"], s=[FA, ("شَكَكْتُ", "shakka", "verb")]),
  n("بِالرُّمْحِ", "rumh", JN("بِ", "الرُّمْحِ"), TA("شَكَكْتُ"), s=[BI, ("الرُّمْحِ", "rumh", "noun")]),
  n("الْأَصَمِّ", "asamm", NAT("الرُّمْحِ"), Dn("«الْأَصَمُّ: الصُّلْبُ» " + ZAW, "«الْأَصَمّ: hard» (al-Zawzanī)", "«الْأَصَمّ: sert» (Zevzenî)")),
  n("ثِيَابَهُ", "thawb", MF(), IDF("هُ"), Sn("وَهُوَ كِنَايَةٌ عَنْ إِنْفَاذِ الرُّمْحِ فِيهِ: «أَيْ طَعَنْتُهُ طَعْنَةً أَنْفَذَتِ الرُّمْحَ فِي جِسْمِهِ وَثِيَابِهِ كُلِّهَا» " + ZAW, "it is a kinaya for driving the spear right through him: «that is, I thrust him through so that the spear passed through his body and all his clothes» (al-Zawzanī)", "mızrağı onun içinden geçirmekten kinâyedir: «yani ona öyle bir darbe vurdum ki mızrak bedeninden ve bütün elbiselerinden geçti» (Zevzenî)", "kinaya"),
     s=[("ثِيَابَ", "thawb", "noun"), P("هُ")])],
 [v("لَيْسَ", "laysa", LAYSA_, CL_IST),
  n("الْكَرِيمُ", "karim", RO("اسْمُ لَيْسَ", "the noun of لَيْسَ", "لَيْسَ'nin ismi", "r", "kana-wa-akhawatuha")),
  pp("عَلَى", "ala", HJ),
  n("الْقَنَا", "qana", MJ("jA"), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُحَرَّمِ» بَعْدَهُمَا", "; the jarr phrase hangs on «مُحَرَّمِ» after it", "; câr-mecrûr sonraki «مُحَرَّمِ»e müteallik"), Dn("جَمْعُ قَنَاةٍ: الرُّمْحُ", "the plural of قَنَاة, a spear", "قَنَاة'nın cem'i: mızrak", "jam-taksir")),
  n("بِمُحَرَّمِ", "muharram-ant", BI_ZAID("مُحَرَّمِ"), QT, Dn("«يُرِيدُ أَنَّ الرِّمَاحَ مُولَعَةٌ بِالْكِرَامِ لِحِرْصِهِمْ عَلَى الْإِقْدَامِ، وَقِيلَ: بَلْ مَعْنَاهُ أَنَّ كَرَمَهُ لَا يُخَلِّصُهُ مِنَ الْقَتْلِ الْمُقَدَّرِ لَهُ» " + ZAW, "«he means the spears are fond of the noble, for their eagerness to press forward; or, it is said, his nobility does not save him from the death decreed for him» (al-Zawzanī)", "«mızrakların, ileri atılma hırsları yüzünden soylulara düşkün olduğunu kasteder; yahut soyluluğunun onu takdir edilmiş ölümden kurtarmadığını» (Zevzenî)", "ism-maful"),
     s=[BI, ("مُحَرَّمِ", "muharram-ant", "noun")])])

# ---- v. 50 ----
V(50, "Then I left him a slaughter-beast for the beasts of prey, which reach for him and bite at his fine fingertips and his wrist.",
  "Sonra onu yırtıcı hayvanlara kesimlik bir hayvan gibi bıraktım; ona uzanır, güzel parmak uçlarını ve bileğini ısırırlar.",
 [v("فَتَرَكْتُهُ", "taraka", PRE("fa", "تَرَكْتُ"), TU("ana"), OBJ("هُ", ("مَفْعُولٌ بِهِ أَوَّلُ", "its first object", "birinci mef'ûl")), CL(0, "مَعْطُوفَةٌ عَلَى «جَادَتْ»", "is conjoined to «جَادَتْ»", "«جَادَتْ»e ma'tûftur"), s=[FA, ("تَرَكْتُ", "taraka", "verb"), P("هُ")]),
  n("جَزَرَ", "jazara-ant", MF2(), MDF, Dn("«الْجَزَرُ: جَمْعُ جَزَرَةٍ، وَهِيَ الشَّاةُ الَّتِي أُعِدَّتْ لِلذَّبْحِ» " + ZAW, "«الْجَزَر: the plural of جَزَرَة, a sheep set aside for slaughter» (al-Zawzanī)", "«الْجَزَر: جَزَرَة'nin cem'i, kesilmek için ayrılmış koyun» (Zevzenî)"),
     Sn("وَفِيهِ تَشْبِيهٌ بَلِيغٌ: «فَصَيَّرْتُهُ طُعْمَةً لِلسِّبَاعِ كَمَا يَكُونُ الْجَزَرُ طُعْمَةً لِلنَّاسِ» " + ZAW + "؛ الْمُشَبَّهُ الْقَتِيلُ، وَالْمُشَبَّهُ بِهِ الْجَزَرُ، وَحُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ",
        "here is a tashbih baligh: «I made him a meal for the beasts of prey, as slaughter-sheep are a meal for men» (al-Zawzanī); the thing likened is the slain man, the thing it is likened to the slaughter-sheep, and both the tool and the point of likeness are dropped",
        "burada belîğ teşbîh vardır: «onu, kesimlik koyunların insanlara yem olduğu gibi yırtıcılara yem kıldım» (Zevzenî); müşebbeh öldürülen, müşebbehün bih kesimlik koyun; edat ve vech-i şebeh hazfedilmiştir", "tashbih", "aqsam-al-tashbih")),
  n("السِّبَاعِ", "sabu", MI(), Dn("جَمْعُ سَبُعٍ", "the plural of سَبُع", "سَبُع'ün cem'i", "jam-taksir")),
  v("يَنُشْنَهُ", "nasha-ant", NISWA, OBJ("هُ"), CL("n", "حَالٌ مِنَ «السِّبَاعِ»", "a hal of «السِّبَاعِ»", "«السِّبَاعِ»dan hâl", "al-hal-jumla-wa-rabituha"), Dn("إِنْ كَانَتْ «أَلْ» لِلتَّعْرِيفِ، أَوْ فِي مَحَلِّ جَرٍّ نَعْتٌ إِنْ كَانَتْ لِلْجِنْسِ " + DUR + "؛ «النَّوْشُ: التَّنَاوُلُ، وَالْفِعْلُ نَاشَ يَنُوشُ» " + ZAW,
       "if the article defines; or a na't, in the seat of jarr, if it names the kind (al-Durra); «النَّوْش is reaching for a thing; the verb نَاشَ يَنُوشُ» (al-Zawzanī)", "«أَلْ» tarif içinse; cins içinse mahallen mecrûr na'ttır (Dürre); «النَّوْش: uzanıp almak; fiili نَاشَ يَنُوشُ» (Zevzenî)"), g=["hollow-verbs"], s=[("يَنُشْنَ", "nasha-ant", "verb"), P("هُ")])],
 [v("يَقْضِمْنَ", "qadima-ant", NISWA, CL(0, "بَدَلٌ مِنْ جُمْلَةِ «يَنُشْنَهُ»", "is a badal of the clause «يَنُشْنَهُ»", "«يَنُشْنَهُ» cümlesinden bedeldir", "badal"), Dn("كَذَا أَعْرَبَهُ الدُّرَّةُ عَلَى رِوَايَةِ «يَقْضِمْنَ»؛ «الْقَضْمُ: الْأَكْلُ بِمُقَدَّمِ الْأَسْنَانِ» " + ZAW, "so al-Durra parses it, on the version «يَقْضِمْنَ»; «الْقَضْم is eating with the front teeth» (al-Zawzanī)", "Dürre «يَقْضِمْنَ» rivayetine göre böyle i'râb eder; «الْقَضْم: ön dişlerle yemek» (Zevzenî)")),
  n("حُسْنَ", "husn", MF(), MDF, Dn("أَيْ: «بَنَانَهُ الْحَسَنَ وَمِعْصَمَهُ الْحَسَنَ» " + ZAW, "that is, «his fine fingertips and his fine wrist» (al-Zawzanī)", "yani «güzel parmak uçlarını ve güzel bileğini» (Zevzenî)")),
  n("بَنَانِهِ", "banan", MI(), IDF("هِ"), s=[("بَنَانِ", "banan", "noun"), P("هِ")]),
  n("وَالْمِعْصَمِ", "misam", PRE("wa", "الْمِعْصَمِ"), ATF("بَنَانِهِ"), QA, s=[WA, ("الْمِعْصَمِ", "misam", "noun")])])

# ---- v. 51 ----
V(51, "And many a joined coat of ample mail have I rent open at its gaps with the sword, off a defender of what was his to guard, a man who marked himself in battle —",
  "Nice geniş zırhın halkalarını, savunması gereken şeyleri koruyan, savaşta kendini işaretle tanıtan bir yiğidin üzerinden kılıçla yırttım —",
 [n("وَمِشَكِّ", "mishakk-ant", PRE("wa-rubba", "مِشَكِّ"), RUBBA_MB, MDF, Dn("«الْمِشَكُّ: الدِّرْعُ الَّتِي قَدْ شُكَّ بَعْضُهَا إِلَى بَعْضٍ، وَقِيلَ: مَسَامِيرُهَا … وَقِيلَ: الرَّجُلُ التَّامُّ السِّلَاحِ» " + ZAW, "«الْمِشَكّ: a coat of mail whose rings are joined one to another; or its rivets …; or a man fully armed» (al-Zawzanī)", "«الْمِشَكّ: halkaları birbirine geçirilmiş zırh; yahut perçinleri …; yahut silahı tam adam» (Zevzenî)"), s=[WA, ("مِشَكِّ", "mishakk-ant", "noun")]),
  n("سَابِغَةٍ", "sabigha", MI(), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ — دِرْعٍ — " + DUR + "؛ وَالسَّابِغَةُ: الدِّرْعُ الْوَاسِعَةُ", "a na't of a noun left unsaid — a coat of mail (al-Durra); السَّابِغَة: a wide, ample coat of mail", "mahzûf bir mevsûfun — zırhın — sıfatıdır (Dürre); السَّابِغَة: geniş zırh", "hadhf-wa-taqdir")),
  v("هَتَكْتُ", "hataka-ant", TU("ana"), CL("r", "خَبَرُ «مِشَكِّ»", "the khabar of «مِشَكِّ»", "«مِشَكِّ»in haberi", "anwa-al-khabar"), Dn("أَوْ فِي مَحَلِّ جَرٍّ نَعْتٌ وَالْخَبَرُ مَحْذُوفٌ " + DUR, "or a na't, in the seat of jarr, with the khabar left out (al-Durra)", "yahut mahallen mecrûr na't, haber hazfedilmiş (Dürre)"),
     Sn("وَهُوَ كِنَايَةٌ عَنْ عِظَمِ بَأْسِهِ: «يُرِيدُ أَنَّهُ هَتَكَ مِثْلَ هٰذِهِ الدِّرْعِ عَنْ مِثْلِ هٰذَا الشُّجَاعِ، فَكَيْفَ الظَّنُّ بِغَيْرِهِ» " + ZAW, "it is a kinaya for his great might: «he means he tore such a coat of mail off such a brave man — what then of any other?» (al-Zawzanī)", "gücünün büyüklüğünden kinâyedir: «böyle bir yiğidin üzerinden böyle bir zırhı yırttığını kasteder; başkası hakkında ne düşünülür?» (Zevzenî)", "kinaya")),
  n("فُرُوجَهَا", "farj-gap", MF(), IDF("هَا"), Dn("جَمْعُ فَرْجٍ؛ «شَقَقْتُ أَوْسَاطَهَا» " + ZAW, "the plural of فَرْج; «I split its middles» (al-Zawzanī)", "فَرْج'in cem'i; «ortalarını yardım» (Zevzenî)", "jam-taksir"), s=[("فُرُوجَ", "farj-gap", "noun"), P("هَا")])],
 [n("بِالسَّيْفِ", "sayf", JN("بِ", "السَّيْفِ"), TA("هَتَكْتُ"), s=[BI, ("السَّيْفِ", "sayf", "noun")]),
  pp("عَنْ", "an", HJ),
  n("حَامِي", "hamin-ant", MJ("jY"), MDF, TA("هَتَكْتُ"), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ " + DUR, "a na't of a noun left unsaid, the active participle annexed to its object (al-Durra)", "mahzûf bir mevsûfun sıfatı; ism-i fâil mef'ûlüne izâfe edilmiştir (Dürre)", "ism-fail", "hadhf-wa-taqdir")),
  n("الْحَقِيقَةِ", "haqiqa", MI(), Dn("«الْحَقِيقَةُ: مَا يَحِقُّ عَلَيْكَ حِفْظُهُ، أَيْ يَجِبُ» " + ZAW, "«الْحَقِيقَة: what you are bound to guard» (al-Zawzanī)", "«الْحَقِيقَة: korunması sana vâcip olan şey» (Zevzenî)")),
  n("مُعْلِمِ", "mulim-ant", SIFA_MD("ثَانٍ"), QT, Dn("«الْمُعْلِمُ — بِكَسْرِ اللَّامِ —: الَّذِي أَعْلَمَ نَفْسَهُ، أَيْ شَهَرَهَا بِعَلَامَةٍ يُعْرَفُ بِهَا فِي الْحُرُوبِ … وَالْمُعْلَمُ — بِفَتْحِ اللَّامِ —: الَّذِي يُشَارُ إِلَيْهِ» " + ZAW, "«الْمُعْلِم, with kasra on the lam: one who marks himself with a sign to be known by in war …; الْمُعْلَم, with fatha: one pointed out (as the hero of the troop)» (al-Zawzanī)", "«الْمُعْلِم — lâm'ın kesresiyle —: savaşta tanınmak için kendini bir işaretle belirleyen …; الْمُعْلَم — fethasıyla —: kendisine işaret edilen» (Zevzenî)", "ism-fail"))])

# ---- v. 52 ----
V(52, "quick of hand at the gaming-arrows when winter comes, a tearer-down of the wine-sellers' banners, blamed (for his giving).",
  "kış gelince kumar oklarında eli çabuk, şarapçıların bayraklarını indirten, (cömertliği yüzünden) çokça kınanan biri.",
 [n("رَبِذٍ", "rabidh-ant", SIFA_X(), Dn("لِلْمَوْصُوفِ الْمَحْذُوفِ فِي الْبَيْتِ قَبْلَهُ " + DUR + "؛ «الرَّبِذُ: السَّرِيعُ» " + ZAW + "؛ «وَالْبَيْتُ كُلُّهُ مِنْ صِفَةِ حَامِي الْحَقِيقَةِ»", "of the man left unsaid in the verse before (al-Durra); «الرَّبِذ: quick» (al-Zawzanī); «the whole verse describes the defender of what was his to guard»", "önceki beyitteki mahzûf mevsûfun (Dürre); «الرَّبِذ: çabuk» (Zevzenî); «beytin tamamı ‹hakikatini koruyan›ın sıfatıdır»", "sifa-mushabbaha")),
  n("يَدَاهُ", "yad", RO("فَاعِلٌ لِلصِّفَةِ الْمُشَبَّهَةِ «رَبِذٍ»", "the doer of the sifa mushabbaha «رَبِذٍ»", "«رَبِذٍ» sıfat-ı müşebbehesinin fâili", "rD", "fail", "sifa-mushabbaha"), Fr("، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the nun is dropped for the annexation, and the هُ is its second term, in the seat of jarr", "; izâfe sebebiyle nûn düşmüştür; hâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness"), s=[("يَدَا", "yad", "noun"), P("هُ")]),
  n("بِالْقِدَاحِ", "qidh-ant", JN("بِ", "الْقِدَاحِ"), TA("رَبِذٍ"), Dn("جَمْعُ قِدْحٍ: سَهْمُ الْمَيْسِرِ؛ «سَرِيعِ الْيَدِ خَفِيفِهَا فِي إِجَالَةِ الْقِدَاحِ فِي الْمَيْسِرِ» " + ZAW, "the plural of قِدْح, an arrow of the game of maysir; «quick and light of hand at turning the arrows in the maysir» (al-Zawzanī)", "قِدْح'in cem'i: meysir kumarının oku; «meysirde okları çevirmekte eli çabuk ve hafif» (Zevzenî)", "jam-taksir"), s=[BI, ("الْقِدَاحِ", "qidh-ant", "noun")]),
  pt("إِذَا", "idha", Fr("ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«رَبِذٍ»", "an adverb of time built on sukun, in the seat of nasb, hanging on «رَبِذٍ»", "sükûn üzere mebnî zaman zarfı, mahallen mansûb, «رَبِذٍ»e müteallik", "maful-fih")),
  v("شَتَا", "shata-ant", MADI_A, HID("هُوَ", MAN_D), CL_MI("إِذَا"), Dn("«شَتَا: دَخَلَ فِي الشِّتَاءِ … وَخَصَّ الشِّتَاءَ لِأَنَّهُمْ يُكْثِرُونَ الْمَيْسِرَ فِيهِ لِتَفَرُّغِهِمْ» " + ZAW, "«شَتَا: he entered winter … he names winter because they played maysir most then, having leisure» (al-Zawzanī)", "«شَتَا: kışa girdi … kışı anmıştır, çünkü boş vakitleri olduğundan meysiri en çok o mevsimde oynarlardı» (Zevzenî)"))],
 [n("هَتَّاكِ", "hattak-ant", SIFA_X(), MDF, Dn("وَهُوَ صِيغَةُ مُبَالَغَةٍ لِاسْمِ الْفَاعِلِ، مِنْ إِضَافَتِهِ إِلَى مَفْعُولِهِ " + DUR, "an intensive form of the active participle, annexed to its object (al-Durra)", "ism-i fâilin mübalağa sîgası, mef'ûlüne izâfe edilmiştir (Dürre)", "sighat-mubalagha"),
     Sn("وَهُوَ كِنَايَةٌ عَنْ سَعَةِ جُودِهِ: «أَيْ كَانَ يَشْتَرِي جَمِيعَ مَا عِنْدَهُمْ مِنَ الْخَمْرِ حَتَّى يَقْلَعُوا رَايَاتِهِمْ لِنَفَادِ خَمْرِهِمْ» " + ZAW, "it is a kinaya for the breadth of his giving: «that is, he used to buy up all the wine they had, until they pulled down their banners, their wine gone» (al-Zawzanī)", "cömertliğinin genişliğinden kinâyedir: «yani onların bütün şaraplarını satın alırdı; şarapları tükendiği için bayraklarını sökerlerdi» (Zevzenî)", "kinaya")),
  n("غَايَاتِ", "ghaya", MI(), MDF, Dn("«الْغَايَةُ: رَايَةٌ يَنْصِبُهَا الْخَمَّارُ لِيُعْرَفَ مَكَانُهُ بِهَا» " + ZAW, "«الْغَايَة: a banner the wine-seller sets up so that his place is known by it» (al-Zawzanī)", "«الْغَايَة: şarapçının yeri bilinsin diye diktiği bayrak» (Zevzenî)", "jam-muannath-salim")),
  n("التِّجَارِ", "tajir", MI(), Dn("«أَرَادَ بِالتِّجَارِ الْخَمَّارِينَ» " + ZAW + "؛ جَمْعُ تَاجِرٍ", "«by the traders he means the wine-sellers» (al-Zawzanī); the plural of تَاجِر", "«tüccarlarla şarapçıları kastetmiştir» (Zevzenî); تَاجِر'in cem'i", "jam-taksir")),
  n("مُلَوَّمِ", "mulawwam-ant", SIFA_X(), Fr("، وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ", "; its deputy doer is a pronoun hidden in it", "; nâib-i fâili onda gizli zamirdir", "naib-al-fail"), QT, Dn("وَهُوَ مُبَالَغَةُ اسْمِ الْمَفْعُولِ " + DUR + "؛ «الْمُلَوَّمُ: الَّذِي لِيمَ مَرَّةً بَعْدَ أُخْرَى … مَلُومٌ عَلَى إِمْعَانِهِ فِي الْجُودِ وَإِسْرَافِهِ فِي الْبَذْلِ» " + ZAW, "an intensive passive participle (al-Durra); «الْمُلَوَّم: blamed time after time … for going far in generosity and lavishing his gifts» (al-Zawzanī)", "ism-i mef'ûlün mübalağasıdır (Dürre); «الْمُلَوَّم: defalarca kınanan … cömertlikte aşırı gidip bağışta israf ettiği için» (Zevzenî)", "ism-maful"))])

# =====================================================================================================================
# Chapter 10 — مَصْرَعُ الْبَطَلِ، وَالشَّاةُ (al-Zawzanī vv. 53–60)
# =====================================================================================================================
IDF_Y = Fr("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed; the ya is its second term, in the seat of jarr", ", muzâf; yâ muzâfun ileyh, mahallen mecrûr", "idafa-definiteness")
SHAT = ("«شَاةَ قَنَصٍ»", "the «ewe of the hunt»", "«av koyunu»na")

# ---- v. 53 ----
V(53, "When he saw that I had dismounted, making for him, he bared his back teeth — and not in a smile.",
  "Onu öldürmek için (atımdan) indiğimi görünce azı dişlerini gösterdi — ama gülümsemek için değil.",
 [pt("لَمَّا", "lamma", Fr("حَرْفُ وُجُودٍ لِوُجُودٍ", "the particle «when this was, that was»", "vücûd li-vücûd harfi"), Dn("وَيَرَى ابْنُ السَّرَّاجِ وَالْفَارِسِيُّ وَابْنُ جِنِّيٍّ وَجَمَاعَةٌ أَنَّهَا ظَرْفٌ بِمَعْنَى «حِينَ»، وَهُوَ الْمَشْهُورُ بَيْنَ الْمُعْرِبِينَ " + DUR, "Ibn al-Sarrāj, al-Fārisī, Ibn Jinnī and others hold it is an adverb meaning «at the time when» — the view most parsers follow (al-Durra)", "İbnü's-Serrâc, Fârisî, İbn Cinnî ve bir grup onu «حِينَ» anlamında zarf sayar; i'râbcılar arasında meşhur olan budur (Dürre)", "maful-fih")),
  v("رَآنِي", "raa", MADI_A, Fr("، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "; the nun protects, and the ya is its object, in the seat of nasb", "; nûn vikâye içindir, yâ mef'ûldür, mahallen mansûb", "al-bariz-al-muttasil", "maful-bihi"), HID("هُوَ", MAN_D), CL(0, "ابْتِدَائِيَّةٌ", "is an opening clause", "ibtidâiyyedir"),
     g=["hollow-verbs"], s=[("رَآ", "raa", "verb"), ("نِ", "nun-wiqaya", "part"), P("ي")]),
  pt("قَدْ", "qad", Fr("حَرْفُ تَحْقِيقٍ", "a particle of certainty", "tahkîk harfi", "qad-harf")),
  v("نَزَلْتُ", "nazala", TU("ana"), CL("n", "حَالٌ مِنْ يَاءِ «رَآنِي»", "a hal of the ya of «رَآنِي»", "«رَآنِي»deki yâdan hâl", "al-hal-jumla-wa-rabituha"), Dn("وَ«رَأَى» بَصَرِيَّةٌ " + DUR, "«رَأَى» is of the eye (al-Durra)", "«رَأَى» gözle görmektir (Dürre)"), g=["thulathi-mujarrad-babs"]),
  v("أُرِيدُهُ", "arada", MUDR(), HID("أَنَا"), OBJ("هُ"), CL("n", "حَالٌ مِنْ تَاءِ «نَزَلْتُ»", "a hal of the ta of «نَزَلْتُ»", "«نَزَلْتُ»teki tâdan hâl", "al-hal-jumla-wa-rabituha"), Dn("فَتَدَاخَلَتِ الْحَالَانِ " + DUR, "so the two hals are nested (al-Durra)", "böylece iki hâl iç içe girmiştir (Dürre)"), g=["form-iv-verbs", "hollow-verbs"], s=[("أُرِيدُ", "arada", "verb"), P("هُ")])],
 [v("أَبْدَى", "abda", MADI_A, HID("هُوَ", MAN_D), CL(0, "جَوَابُ «لَمَّا»", "is the answer of «لَمَّا»", "«لَمَّا»nın cevabıdır"), g=["form-iv-verbs"]),
  n("نَوَاجِذَهُ", "najidh-ant", MF(), IDF("هُ"), Dn("جَمْعُ نَاجِذٍ، وَهُوَ آخِرُ الْأَضْرَاسِ " + DUR, "the plural of نَاجِذ, the hindmost molar (al-Durra)", "نَاجِذ'in cem'i: en arkadaki azı dişi (Dürre)", "jam-taksir"),
     Sn("وَإِبْدَاءُ النَّوَاجِذِ لِغَيْرِ تَبَسُّمٍ كِنَايَةٌ عَنِ الْفَزَعِ: «كَشَرَ عَنْ أَسْنَانِهِ غَيْرَ مُتَبَسِّمٍ، أَيْ لِفَرْطِ كُلُوحِهِ مِنْ كَرَاهِيَةِ الْمَوْتِ قَلَصَتْ شَفَتَاهُ عَنْ أَسْنَانِهِ» " + ZAW, "baring the back teeth, not in a smile, is a kinaya for terror: «he showed his teeth, not smiling — from the excess of his grimace, hating death, his lips drew back from his teeth» (al-Zawzanī)", "gülümsemeden azı dişlerini göstermek korkudan kinâyedir: «gülümsemeden dişlerini gösterdi; yani ölümden duyduğu tiksintiyle yüzünü öyle buruşturdu ki dudakları dişlerinden çekildi» (Zevzenî)", "kinaya"),
     s=[("نَوَاجِذَ", "najidh-ant", "noun"), P("هُ")]),
  n("لِغَيْرِ", "ghayr", JN("لِ", "غَيْرِ"), MDF, TA("أَبْدَى"), HD("تَكْمِيلٌ: لَمَّا أَوْهَمَ «أَبْدَى نَوَاجِذَهُ» الضَّحِكَ جَاءَ بِـ«لِغَيْرِ تَبَسُّمِ» فَدَفَعَهُ", "a takmil: since «he bared his back teeth» might suggest laughter, he adds «and not in a smile» to ward it off", "tekmîl: «azı dişlerini gösterdi» gülmeyi vehmettirebileceği için «gülümsemek için değil» diyerek bunu def etmiştir", "takmil-wa-tatmim"), s=[LI, ("غَيْرِ", "ghayr", "noun")]),
  n("تَبَسُّمِ", "tabassum", MI(), QT, Dn("وَيُرْوَى: «لِغَيْرِ تَكَلُّمِ» " + ZAW, "it is also related «and not to speak» (al-Zawzanī)", "«konuşmak için değil» diye de rivayet edilir (Zevzenî)", "masdar"))])

# ---- v. 54 ----
V(54, "I saw him the length of the day as if his fingertips and his head had been dyed with ʿiẓlim.",
  "Gün boyu onu, parmak uçları ve başı sanki çivitotuyla boyanmış gibi gördüm.",
 [n("عَهْدِي", "ahd", MB("rM"), IDF_Y, Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ " + DUR + "؛ «الْعَهْدُ: اللِّقَاءُ، يُقَالُ: عَهِدْتُهُ أَعْهَدُهُ عَهْدًا إِذَا لَقِيتُهُ» " + ZAW, "the masdar annexed to its doer (al-Durra); «الْعَهْد is meeting: ‹I came on him›» (al-Zawzanī)", "masdar fâiline izâfe edilmiştir (Dürre); «الْعَهْد: karşılaşmak; ‹ona rastladım› denir» (Zevzenî)", "masdar"), s=[("عَهْدِ", "ahd", "noun"), P("ي")]),
  pp("بِهِ", "bi", JP("بِ", "هِ", ("الْبَاءُ", "the ba", "bâ")), TAM("khabar"), Dn("قَالَهُ التِّبْرِيزِيُّ وَابْنُ الْأَنْبَارِيِّ؛ وَرَأَى الدُّرَّةُ أَنَّهُمَا مُتَعَلِّقَانِ بِالْمَصْدَرِ وَالْخَبَرُ مَحْذُوفٌ سَدَّتِ الْحَالُ مَسَدَّهُ " + DUR, "so al-Tibrīzī and Ibn al-Anbārī; al-Durra holds it hangs on the masdar, the khabar being left out and the hal standing in its place (al-Durra)", "Tebrîzî ve İbnü'l-Enbârî böyle der; Dürre ise onun masdara müteallik olduğunu, haberin hazfedilip yerini hâlin tuttuğunu düşünür (Dürre)"), s=[BI, P("هِ")]),
  n("مَدَّ", "madd", ZZ(), MDF, Dn("وَهُوَ عِنْدَ التِّبْرِيزِيِّ بَدَلٌ مِنَ الِاسْتِقْرَارِ، وَعَلَّقَهُ الدُّرَّةُ بِالْمَصْدَرِ " + DUR + "؛ «مَدُّ النَّهَارِ: طُولُهُ» " + ZAW, "for al-Tibrīzī it stands for the «being» the khabar implies; al-Durra hangs it on the masdar (al-Durra); «مَدّ النَّهَار: the length of the day» (al-Zawzanī)", "Tebrîzî'ye göre haberdeki istikrardan bedeldir; Dürre onu masdara bağlar (Dürre); «مَدُّ النَّهَارِ: günün uzunluğu» (Zevzenî)")),
  n("النَّهَارِ", "nahar", MI()),
  pt("كَأَنَّمَا", "ka-annama", Fr("حَرْفُ تَشْبِيهٍ كَفَّتْهُ «مَا» الْكَافَّةُ عَنِ الْعَمَلِ", "the particle of likening, kept from governing by the restraining مَا", "kâffe «mâ» ile amelden alıkonmuş teşbîh harfi", "innama-kaffa", "inna-wa-akhawatuha"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: «رَأَيْتُهُ طُولَ النَّهَارِ وَامْتِدَادَهُ بَعْدَ قَتْلِي إِيَّاهُ وَجَفَافِ الدَّمِ عَلَيْهِ كَأَنَّ بَنَانَهُ وَرَأْسَهُ مَخْضُوبَانِ بِهٰذَا النَّبْتِ» " + ZAW + "؛ فَالْمُشَبَّهُ بَنَانُهُ وَرَأْسُهُ وَقَدْ جَفَّ عَلَيْهِمَا الدَّمُ، وَالْمُشَبَّهُ بِهِ الْمَخْضُوبُ بِالْعِظْلِمِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ اللَّوْنُ وَلَمْ يُذْكَرْ",
        "here is a tashbih mursal mujmal: «I saw him the length of the day, after I had killed him and the blood had dried on him, as if his fingertips and head were dyed with this plant» (al-Zawzanī); the thing likened is his fingers and head with the blood dried on them, the thing it is likened to what is dyed with ʿiẓlim, the tool كَأَنَّ, and the point of likeness — the colour — is not said",
        "burada mürsel mücmel teşbîh vardır: «onu öldürüp kan üzerinde kuruduktan sonra gün boyu, parmak uçları ve başı bu bitkiyle boyanmış gibi gördüm» (Zevzenî); müşebbeh, üzerinde kan kurumuş parmakları ve başı; müşebbehün bih çivitotuyla boyanmış olan; edat «كَأَنَّ»; vech-i şebeh — renk — söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"))],
 [v("خُضِبَ", "khadaba-ant", MADI, MAJH, CL("n", "حَالٌ مِنَ الْهَاءِ فِي «بِهِ»", "a hal of the pronoun in «بِهِ»", "«بِهِ»deki zamirden hâl", "al-hal-jumla-wa-rabituha"), Dn("وَالْعَامِلُ فِيهَا الْمَصْدَرُ، وَهِيَ سَادَّةٌ مَسَدَّ الْخَبَرِ " + DUR, "its governor is the masdar, and it stands in place of the khabar (al-Durra)", "âmili masdardır ve haberin yerini tutar (Dürre)")),
  n("الْبَنَانُ", "banan", NF()),
  n("وَرَأْسُهُ", "ras", PRE("wa", "رَأْسُ"), ATF("الْبَنَانُ", "r"), IDF("هُ"), s=[WA, ("رَأْسُ", "ras", "noun"), P("هُ")]),
  n("بِالْعِظْلَمِ", "izlim-ant", JN("بِ", "الْعِظْلَمِ"), TA("خُضِبَ"), QA, Dn("«الْعِظْلِمُ: نَبْتٌ يُخْتَضَبُ بِهِ» " + ZAW + "؛ وَطُبِعَ بِفَتْحِ اللَّامِ", "«الْعِظْلِم: a plant used for dyeing» (al-Zawzanī); the edition prints the lam with fatha", "«الْعِظْلِم: boyamada kullanılan bir bitki» (Zevzenî); neşirde lâm fethayla basılmıştır"), s=[BI, ("الْعِظْلَمِ", "izlim-ant", "noun")])])

# ---- v. 55 ----
V(55, "I thrust at him with the spear, then fell upon him with an Indian blade, of pure steel, swift to cut.",
  "Ona mızrakla vurdum, sonra demiri saf, keskin bir Hint kılıcıyla üzerine çıktım.",
 [v("فَطَعَنْتُهُ", "taana", PRE("fa", "طَعَنْتُ"), TU("ana"), OBJ("هُ"), CL(0, "مَعْطُوفَةٌ أَوْ مُسْتَأْنَفَةٌ", "is conjoined, or opens a new sentence", "ma'tûf yahut isti'nâfiyyedir"), Dn("عَلَى الْوَجْهَيْنِ فِي الْفَاءِ " + DUR, "on the two readings of the fa (al-Durra)", "fâ'daki iki vecihe göre (Dürre)"), g=["thulathi-mujarrad-babs"], s=[FA, ("طَعَنْتُ", "taana", "verb"), P("هُ")]),
  n("بِالرُّمْحِ", "rumh", JN("بِ", "الرُّمْحِ"), TA("طَعَنْتُ"), s=[BI, ("الرُّمْحِ", "rumh", "noun")]),
  pt("ثُمَّ", "thumma", Fr("حَرْفُ عَطْفٍ", "a conjunction («then»)", "atıf harfi («sonra»)", "atf-nasaq")),
  v("عَلَوْتُهُ", "ala-rise", TU("ana"), OBJ("هُ"), CL(0, "مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "is conjoined to the one before", "öncekine ma'tûftur"), g=["naqis-verbs"], s=[("عَلَوْتُ", "ala-rise", "verb"), P("هُ")])],
 [n("بِمُهَنَّدٍ", "muhannad-ant", JN("بِ", "مُهَنَّدٍ"), TA("عَلَوْتُ"), Dn("وَ«مُهَنَّدٍ» صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ أَيْ: «مَعَ سَيْفٍ مُهَنَّدٍ صَافِي الْحَدِيدِ سَرِيعِ الْقَطْعِ» " + ZAW, "«مُهَنَّدٍ» is a na't of a noun left unsaid (al-Durra) — «with an Indian sword, of pure steel, swift to cut» (al-Zawzanī)", "«مُهَنَّدٍ» mahzûf bir mevsûfun sıfatıdır (Dürre) — «demiri saf, çabuk kesen bir Hint kılıcıyla» (Zevzenî)", "hadhf-wa-taqdir"),
     HD("كِنَايَةٌ عَنْ مَوْصُوفٍ: ذَكَرَ السَّيْفَ بِصِفَاتٍ تَجْتَمِعُ لَهُ — مُهَنَّدٍ صَافِي الْحَدِيدَةِ مِخْذَمٍ — وَلَمْ يُسَمِّهِ", "a kinaya for a thing described: he names the sword only by attributes that meet in it — Indian, of pure steel, keen — and never by its name", "mevsûftan kinâye: kılıcı adını anmadan onda birleşen sıfatlarla — Hint işi, demiri saf, keskin — anmıştır", "kinaya", "aqsam-al-kinaya"), s=[BI, ("مُهَنَّدٍ", "muhannad-ant", "noun")]),
  n("صَافِي", "safin-ant", SIFA_MD("ثَانٍ", "jY"), MDF, Dn("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا " + DUR, "the adjective annexed to its own doer (al-Durra)", "sıfat fâiline izâfe edilmiştir (Dürre)", "sifa-mushabbaha")),
  n("الْحَدِيدَةِ", "hadida-ant", MI()),
  n("مِخْذَمِ", "mikhdham", SIFA_MD("ثَالِثٌ"), QT, Dn("«الْمِخْذَمُ: السَّرِيعُ الْقَطْعِ» " + ZAW, "«الْمِخْذَم: swift to cut» (al-Zawzanī)", "«الْمِخْذَم: çabuk kesen» (Zevzenî)"))])

# ---- v. 56 ----
V(56, "A hero, as if his clothes were hung on a great tree, shod with sandals of tanned hide, no twin.",
  "Bir yiğit; elbiseleri sanki ulu bir ağaca giydirilmiş; tabaklanmış deriden nalınlar giydirilir; ikiz değil.",
 [n("بَطَلٍ", "batal-ant", SIFA_X(), Dn("لِلْمَوْصُوفِ الْمَحْذُوفِ بِـ«حَامِي الْحَقِيقَةِ» فِي الْبَيْتِ ٥١؛ وَيُرْوَى بِالرَّفْعِ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ " + DUR + "؛ «يَقُولُ: وَهُوَ بَطَلٌ مَدِيدُ الْقَدِّ» " + ZAW,
       "of the unnamed man described as «defender of what was his to guard» in v. 51; it is also related in raf', the khabar of an omitted «he is» (al-Durra); «he says: and he is a tall-statured hero» (al-Zawzanī)", "51. beyitte «hakikatini koruyan» diye nitelenen mahzûf mevsûfun; mahzûf «o»nun haberi olarak merfû da rivayet edilir (Dürre); «Demek ister ki: o uzun boylu bir yiğittir» (Zevzenî)")),
  pt("كَأَنَّ", "kaanna", KAANNA_, CL("j", "نَعْتٌ لِـ«بَطَلٍ»", "a na't of «بَطَلٍ»", "«بَطَلٍ»in na'tı", "jumla-sifa"), Dn("أَوْ حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِيهِ " + DUR, "or a hal of the pronoun hidden in it (al-Durra)", "yahut ondaki gizli zamirden hâl (Dürre)"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: «كَأَنَّ ثِيَابَهُ أُلْبِسَتْ شَجَرَةً عَظِيمَةً مِنْ طُولِ قَامَتِهِ وَاسْتِوَاءِ خَلْقِهِ» " + ZAW + "؛ فَالْمُشَبَّهُ الْبَطَلُ فِي ثِيَابِهِ، وَالْمُشَبَّهُ بِهِ السَّرْحَةُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ طُولُ الْقَامَةِ وَلَمْ يُذْكَرْ",
        "here is a tashbih mursal mujmal: «as if his clothes were put on a great tree, for his tall stature and the evenness of his build» (al-Zawzanī); the thing likened is the hero in his clothes, the thing it is likened to the great tree, the tool كَأَنَّ, and the point of likeness — height — is not said",
        "burada mürsel mücmel teşbîh vardır: «boyunun uzunluğundan ve yapısının düzgünlüğünden elbiseleri sanki ulu bir ağaca giydirilmiştir» (Zevzenî); müşebbeh elbiseleri içindeki yiğit, müşebbehün bih ulu ağaç, edat «كَأَنَّ», vech-i şebeh — boy uzunluğu — söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih")),
  n("ثِيَابَهُ", "thawb", ISM_K(), IDF("هُ"), s=[("ثِيَابَ", "thawb", "noun"), P("هُ")]),
  pp("فِي", "fi", HJ),
  n("سَرْحَةٍ", "sarha-ant", MJ(), TAM("khabar", "كَأَنَّ"), Dn("«السَّرْحَةُ: الشَّجَرَةُ الْعَظِيمَةُ» " + ZAW, "«السَّرْحَة: a great tree» (al-Zawzanī)", "«السَّرْحَة: ulu ağaç» (Zevzenî)"))],
 [v("يُحْذَى", "hadha-ant", MUDR("a"), MAJH, HID("هُوَ", ("الْبَطَلِ", "the hero", "yiğide"), naib=True), Fr("، وَهُوَ الْمَفْعُولُ الْأَوَّلُ", ", which is the first object", ", birinci mef'ûldür", "mafulayn"), CL("j", "نَعْتٌ ثَانٍ لِـ«بَطَلٍ»", "a second na't of «بَطَلٍ»", "«بَطَلٍ»in ikinci na'tı", "jumla-sifa"),
     Dn("«يُحْذَى: أَيْ تُجْعَلُ حِذَاءً لَهُ، وَالْحِذَاءُ: النَّعْلُ» " + ZAW, "«يُحْذَى: they are made his footwear; الْحِذَاء is a sandal» (al-Zawzanī)", "«يُحْذَى: ona ayakkabı yapılır; الْحِذَاء: nalın» (Zevzenî)"), g=["naqis-verbs"]),
  n("نِعَالَ", "nal", MF2(), MDF, Dn("جَمْعُ نَعْلٍ", "the plural of نَعْل", "نَعْل'in cem'i", "jam-taksir")),
  n("السِّبْتِ", "sibt-ant", MI(), Dn("«جُلُودُ الْبَقَرِ الْمَدْبُوغَةُ بِالْقَرَظِ … أَيْ تَسْتَوْعِبُ رِجْلَاهُ السِّبْتَ» " + ZAW, "«ox-hides tanned with qaraẓ … that is, his feet fill the whole hide» (al-Zawzanī)", "«karaz ile tabaklanmış sığır derileri … yani ayakları derinin tamamını doldurur» (Zevzenî)")),
  v("لَيْسَ", "laysa", LAYSA_, NAQ_SUB("هُوَ", ("الْبَطَلِ", "the hero", "yiğide")), CL("j", "نَعْتٌ ثَالِثٌ لِـ«بَطَلٍ»", "a third na't of «بَطَلٍ»", "«بَطَلٍ»in üçüncü na'tı", "jumla-sifa")),
  n("بِتَوْأَمِ", "tawam-ant", BI_ZAID("تَوْأَمِ"), QT, Sn("وَهُوَ كِنَايَةٌ عَنْ قُوَّتِهِ: «بَالَغَ فِي وَصْفِهِ بِالشِّدَّةِ وَالْقُوَّةِ بِامْتِدَادِ قَامَتِهِ وَعِظَمِ أَعْضَائِهِ وَتَمَامِ غِذَائِهِ عِنْدَ إِرْضَاعِهِ، إِذْ كَانَ فَذًّا غَيْرَ تَوْأَمٍ» " + ZAW, "it is a kinaya for his strength: «he goes far in describing his hardness and might — his tall stature, his great limbs, his full nourishment at the breast, for he was born alone, no twin» (al-Zawzanī)", "gücünden kinâyedir: «onun sağlamlığını ve gücünü, boyunun uzunluğu, uzuvlarının iriliği ve emzirilirken gıdasının tamlığıyla — ikiz değil tek doğduğu için — anlatmakta mübalağa etmiştir» (Zevzenî)", "kinaya"),
     s=[BI, ("تَوْأَمِ", "tawam-ant", "noun")])])

# ---- v. 57 ----
V(57, "O the ewe of a hunt, for one to whom she is lawful! To me she is forbidden — would she were not forbidden!",
  "Ey kendisine helâl olan kimse için ne av koyunu! Bana ise haram oldu — keşke haram olmasaydı!",
 [pt("يَا", "ya-nida", Fr("حَرْفُ نِدَاءٍ وَتَعَجُّبٍ", "the particle of calling and of wonder", "nidâ ve taaccüb harfi", "vocative-munada"),
     Sn("وَالنِّدَاءُ خَرَجَ إِلَى التَّعَجُّبِ " + DUR + "؛ «يَا هٰؤُلَاءِ اشْهَدُوا شَاةَ قَنَصٍ … فَتَعَجَّبُوا مِنْ حُسْنِهَا وَجَمَالِهَا» " + ZAW, "the call has passed into wonder (al-Durra); «O people, witness a ewe of the hunt … and marvel at her beauty» (al-Zawzanī)", "nidâ taaccübe çıkmıştır (Dürre); «Ey insanlar, bir av koyununa şahit olun … güzelliğine hayret edin» (Zevzenî)", "khabar-insha")),
  n("شَاةَ", "shat", Fr("مُنَادًى مُتَعَجَّبٌ مِنْهُ مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ", "the one called in wonder, annexed, in nasb by the fatha", "kendisine hayret edilen muzâf münâdâ, fetha ile mansûb", "vocative-munada", "idafa-definiteness"), Dn("وَيَجُوزُ أَنْ يَكُونَ الْمُنَادَى مَحْذُوفًا — يَا هٰؤُلَاءِ — وَ«شَاةَ» مَفْعُولًا بِهِ لِفِعْلٍ مَحْذُوفٍ: اشْهَدُوا " + DUR, "or the one called is left out — «O people» — and «شَاةَ» is the object of an omitted «witness» (al-Durra)", "yahut münâdâ hazfedilmiştir — «ey insanlar» — ve «شَاةَ» mahzûf «şahit olun» fiilinin mef'ûlüdür (Dürre)"),
     Sn("«الشَّاةُ: كِنَايَةٌ عَنِ الْمَرْأَةِ» " + ZAW, "«the ewe is a kinaya for the woman» (al-Zawzanī)", "«koyun, kadından kinâyedir» (Zevzenî)", "kinaya")),
  pt("مَا", "ma-zaida", Fr("حَرْفٌ زَائِدٌ مُقْحَمٌ بَيْنَ الْمُتَضَايِفَيْنِ", "an added word set between the two terms of the idafa", "muzâf ile muzâfun ileyh arasına giren zâid harf", "huruf-al-ziyada-fil-kafiya"), Dn("«مَا: صِلَةٌ زَائِدَةٌ» " + ZAW + "؛ وَجَوَّزَ ابْنُ الْأَنْبَارِيِّ أَنْ تَكُونَ نَكِرَةً مَوْصُوفَةً فِي مَحَلِّ جَرٍّ وَ«قَنَصٍ» صِفَتُهَا " + DUR, "«مَا is an added connective» (al-Zawzanī); Ibn al-Anbārī allows it to be an indefinite noun, in the seat of jarr, with «قَنَصٍ» describing it (al-Durra)", "«mâ, zâid bir sıladır» (Zevzenî); İbnü'l-Enbârî onun mahallen mecrûr nekre-i mevsûfe, «قَنَصٍ»in de sıfatı olmasını câiz görür (Dürre)")),
  n("قَنَصٍ", "qanas-ant", MI(), Dn("الْقَنَصُ: الصَّيْدُ", "الْقَنَص: the hunt, game", "الْقَنَص: av")),
  n("لِمَنْ", "man", Fr("اللَّامُ حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ", "the lam is a jarr letter, and مَنْ a relative noun built on sukun, in the seat of jarr", "lâm cer harfi; «men» sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr", "huruf-jarr", "ism-mawsul"), TA("قَنَصٍ"), s=[LI, ("مَنْ", "man", "pron")]),
  v("حَلَّتْ", "halla-lawful", MADI_F, HID("هِيَ", SHAT), CL_SILA, HD("بَيْنَهُ وَبَيْنَ «حَرُمَتْ» طِبَاقٌ: الْحِلُّ وَالْحُرْمَةُ مَعْنَيَانِ مُتَضَادَّانِ", "it makes a tibaq with «حَرُمَتْ»: lawful and forbidden are contraries", "«حَرُمَتْ» ile tıbâk oluşturur: helâl ve haram iki zıt mânâdır", "tibaq"), g=["doubled-verbs"]),
  pp("لَهُ", "li", JP("لَ", "هُ", LAM_PRN), TA("حَلَّتْ"), s=[("لَ", "li", "prep"), P("هُ")])],
 [v("حَرُمَتْ", "haruma-ant", MADI_F, HID("هِيَ", SHAT), CL("n", "حَالٌ مِنْ فَاعِلِ «حَلَّتْ» عَلَى تَقْدِيرِ «قَدْ»", "a hal of the doer of «حَلَّتْ», with قَدْ understood", "«قَدْ» takdiriyle «حَلَّتْ»in fâilinden hâl", "al-hal-jumla-wa-rabituha"),
     HD("وَهُوَ الطَّرَفُ الثَّانِي مِنْ طِبَاقِ «حَلَّتْ»، وَبَيْنَهُ وَبَيْنَ «لَمْ تَحْرُمِ» طِبَاقُ السَّلْبِ", "it is the second term of the tibaq with «حَلَّتْ», and with «لَمْ تَحْرُمِ» it makes a tibaq al-salb", "«حَلَّتْ» ile kurulan tıbâkın ikinci ucudur; «لَمْ تَحْرُمِ» ile de tıbâk-ı selb oluşturur", "tibaq"), g=["thulathi-mujarrad-babs"]),
  pp("عَلَيَّ", "ala", JP("عَلَى", "ي"), TA("حَرُمَتْ")),
  pt("وَلَيْتَهَا", "layta", PRE("wa-ist", "لَيْتَ"), Fr("حَرْفُ تَمَنٍّ وَنَصْبٍ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "the particle of wishing that puts its noun in nasb; the attached هَا is that noun", "temennî ve nasb harfi; bitişik هَا ismidir, mahallen mansûb", "inna-wa-akhawatuha", "al-bariz-al-muttasil"),
     Dn("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ اسْتِئْنَافًا بَيَانِيًّا، وَلَا تُعْطَفُ عَلَى الْحَالِ لِأَنَّهَا إِنْشَائِيَّةٌ " + DUR, "the clause opens a new, explanatory sentence; it is not conjoined to the hal, being an utterance of wish (al-Durra)", "cümle beyânî isti'nâfiyyedir; inşâî olduğu için hâle atfedilmez (Dürre)"),
     Sn("وَهُوَ إِنْشَاءُ تَمَنٍّ: «أَيْ لَيْتَ أَبِي لَمْ يَتَزَوَّجْهَا حَتَّى كَانَ يَحِلُّ لِي تَزَوُّجُهَا، وَقِيلَ: أَرَادَ أَنَّهَا حَرُمَتْ عَلَيْهِ بِاشْتِبَاكِ الْحَرْبِ بَيْنَ قَبِيلَتَيْهِمَا ثُمَّ تَمَنَّى بَقَاءَ الصُّلْحِ» " + ZAW,
        "it is an utterance of wishing: «that is, would that my father had not married her, so that she were lawful for me to marry; or, it is said, she was forbidden him by the war between their two tribes, and he wishes the peace had lasted» (al-Zawzanī)",
        "temennî inşâsıdır: «yani keşke babam onunla evlenmeseydi de onunla evlenmem bana helâl olsaydı; yahut iki kabile arasındaki savaş yüzünden ona haram olduğunu kasteder ve barışın sürmesini temenni eder» (Zevzenî)", "insha-wa-tamanni"),
     s=[WA, ("لَيْتَ", "layta", "part"), P("هَا")]),
  pt("لَمْ", "lam-jazim", LAM_J),
  v("تَحْرُمِ", "haruma-ant", JZM_R(), HID("هِيَ", SHAT), CL("r", "خَبَرُ «لَيْتَ»", "the predicate of «لَيْتَ»", "«لَيْتَ»in haberi", "inna-wa-akhawatuha"), g=["thulathi-mujarrad-babs"])])

# ---- v. 58 ----
V(58, "So I sent my maid and said to her: «Go, and spy out news of her for me, and find out.»",
  "Bunun üzerine cariyemi gönderdim ve ona dedim: «Git, onun haberlerini benim için gizlice araştır ve öğren.»",
 [v("فَبَعَثْتُ", "baatha", PRE("fa-ist", "بَعَثْتُ"), TU("ana"), CL_IST, g=["thulathi-mujarrad-babs"], s=[FA, ("بَعَثْتُ", "baatha", "verb")]),
  n("جَارِيَتِي", "jariya", MF("nM"), IDF_Y, Dn("«يَقُولُ: فَبَعَثْتُ جَارِيَتِي لِتَتَعَرَّفَ أَحْوَالَهَا لِي» " + ZAW, "«he says: so I sent my maid to learn how she fared, for me» (al-Zawzanī)", "«Demek ister ki: onun hâllerini benim için öğrensin diye cariyemi gönderdim» (Zevzenî)"), s=[("جَارِيَتِ", "jariya", "noun"), P("ي")]),
  v("فَقُلْتُ", "qala", PRE("fa", "قُلْتُ"), TU("ana"), CL(0, "مَعْطُوفَةٌ عَلَى «بَعَثْتُ»", "is conjoined to «بَعَثْتُ»", "«بَعَثْتُ»e ma'tûftur"), g=["hollow-verbs"], s=[FA, ("قُلْتُ", "qala", "verb")]),
  pp("لَهَا", "li", JP("لَ", "هَا", LAM_PRN), TA("قُلْتُ"), s=[("لَ", "li", "prep"), P("هَا")]),
  v("اذْهَبِي", "dhahaba", AMR_Y, CL("n", "مَقُولُ الْقَوْلِ", "what is said", "mekûlü'l-kavl"), g=["thulathi-mujarrad-babs"])],
 [v("فَتَجَسَّسِي", "tajassasa-ant", PRE("fa", "تَجَسَّسِي"), AMR_Y, CL("n", "مَعْطُوفَةٌ عَلَى «اذْهَبِي» فَهِيَ مِنْ مَقُولِ الْقَوْلِ", "conjoined to «اذْهَبِي», so it too is part of what is said", "«اذْهَبِي»ye ma'tûftur, o da mekûlü'l-kavldendir"), g=["form-v-verbs"], s=[FA, ("تَجَسَّسِي", "tajassasa-ant", "verb")]),
  n("أَخْبَارَهَا", "akhbar", MF(), IDF("هَا"), s=[("أَخْبَارَ", "akhbar", "noun"), P("هَا")]),
  pp("لِي", "li", JP("لِ", "ي", LAM_PRN), TA("تَجَسَّسِي")),
  v("وَاعْلَمِي", "alima", PRE("wa", "اعْلَمِي"), AMR_Y, CL("n", "مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا مِنْ مَقُولِ الْقَوْلِ", "conjoined to what is said before it", "önceki mekûlü'l-kavle ma'tûftur"), Dn("وَمَفْعُولَاهُ مَحْذُوفَانِ لِدَلَالَةِ الْكَلَامِ عَلَيْهِمَا " + DUR + "؛ وَالْيَاءُ بَعْدَ الْمِيمِ — رَوِيِّ الْقَافِيَةِ — يَاءُ الْمُخَاطَبَةِ", "its two objects are left out, the speech pointing to them (al-Durra); the ya after the mim — the rawī — is the ya of the woman addressed", "iki mef'ûlü, söz onlara delâlet ettiği için hazfedilmiştir (Dürre); revî olan mîm'den sonraki yâ muhâtaba yâsıdır", "al-qafiya"), g=["thulathi-mujarrad-babs"], s=[WA, ("اعْلَمِي", "alima", "verb")])])

# ---- v. 59 ----
V(59, "She said: «I saw the enemies off their guard, and the ewe is open to one who would shoot.»",
  "(Cariye) dedi ki: «Düşmanları gafil gördüm; koyun, nişan alacak kişiye açıktır.»",
 [v("قَالَتْ", "qala", MADI_F, HID("هِيَ", ("الْجَارِيَةِ", "the maid", "cariyeye")), CL_IST, g=["hollow-verbs"], p=":"),
  v("رَأَيْتُ", "raa", TU("ana"), CL("n", "مَقُولُ الْقَوْلِ", "what is said", "mekûlü'l-kavl"), g=["naqis-verbs"]),
  pp("مِنَ", "min", HJ),
  n("الْأَعَادِي", "aadin", MJ("jY"), TA("رَأَيْتُ"), Dn("أَوْ بِمَحْذُوفٍ حَالٍ مِنْ «غِرَّةً» كَانَ نَعْتًا لَهَا فَلَمَّا قُدِّمَ صَارَ حَالًا " + DUR, "or on an omitted hal of «غِرَّةً» — a na't of it that, put before it, became a hal (al-Durra)", "yahut «غِرَّةً»den mahzûf bir hâle; ona na't iken öne alınınca hâl olmuştur (Dürre)", "jam-taksir")),
  n("غِرَّةً", "ghirra-ant", MF(), Dn("«الْغِرَّةُ: الْغَفْلَةُ» " + ZAW, "«الْغِرَّة: heedlessness» (al-Zawzanī)", "«الْغِرَّة: gaflet» (Zevzenî)"))],
 [n("وَالشَّاةُ", "shat", PRE("wa-hal", "الشَّاةُ"), MB(), Sn("وَهِيَ الْكِنَايَةُ عَنِ الْمَرْأَةِ الَّتِي ذَكَرَهَا الزَّوْزَنِيُّ فِي الْبَيْتِ ٥٧", "it is the kinaya for the woman al-Zawzanī names at v. 57", "Zevzenî'nin 57. beyitte andığı kadından kinâyedir", "kinaya"), s=[WA, ("الشَّاةُ", "shat", "noun")]),
  n("مُمْكِنَةٌ", "mumkin", KH(), CL("n", "حَالٌ مِنْ تَاءِ «رَأَيْتُ»", "a hal of the ta of «رَأَيْتُ»", "«رَأَيْتُ»teki tâdan hâl", "al-hal-jumla-wa-rabituha"), Dn("وَالرَّابِطُ الْوَاوُ فَقَطْ؛ وَإِنْ عَطَفْتَهَا عَلَى «رَأَيْتُ» كَانَتْ مِنْ مَقُولِ الْقَوْلِ " + DUR, "the link is the waw alone; if conjoined to «رَأَيْتُ» it is part of what is said (al-Durra)", "râbıt yalnız vâvdır; «رَأَيْتُ»e atfedilirse mekûlü'l-kavlden olur (Dürre)", "ism-fail")),
  n("لِمَنْ", "man", Fr("اللَّامُ حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ", "the lam is a jarr letter, and مَنْ a relative noun built on sukun, in the seat of jarr", "lâm cer harfi; «men» sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr", "huruf-jarr", "ism-mawsul"), TA("مُمْكِنَةٌ"), s=[LI, ("مَنْ", "man", "pron")]),
  pro("هُوَ", "pron-3ms-munfasil", Fr("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "a detached pronoun built on fatha, the mubtada, in the seat of raf'", "fetha üzere mebnî munfasıl zamir, mübtedâ, mahallen merfû", "mubtada-khabar")),
  n("مُرْتَمِ", "murtamin-ant", Fr("خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", "the khabar, in raf' by a damma estimated on the ya dropped where two quiescents met", "haber; iki sâkin buluştuğu için düşen yâ üzerinde takdîrî damme ile merfû", "mubtada-khabar", "ism-maqsur-manqus"), CL_SILA, Dn("وَهُوَ مَنْقُوصٌ حُذِفَتْ يَاؤُهُ، وَأُشْبِعَتْ كَسْرَةُ الرَّوِيِّ فَوَلَّدَتْ يَاءَ الْإِطْلَاقِ " + DUR + "؛ «يُرِيدُ أَنَّ زِيَارَتَهَا مُمْكِنٌ لِطَالِبِهَا لِغَفْلَةِ الرُّقَبَاءِ» " + ZAW, "a manqus whose ya is dropped; the kasra of the rawī is lengthened and gives the ya of the unbound rhyme (al-Durra); «he means that visiting her is open to whoever seeks it, the watchers being off their guard» (al-Zawzanī)", "yâsı düşmüş menkûs; revînin kesresi uzatılıp ıtlâk yâsını doğurmuştur (Dürre); «onu ziyaretin, gözcülerin gafleti yüzünden isteyene mümkün olduğunu kasteder» (Zevzenî)", "ism-fail", "al-qafiya"),
     HD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: اسْتَعَارَ رَمْيَ الصَّيْدِ لِطَلَبِ زِيَارَتِهَا، وَاشْتَقَّ مِنْهُ «مُرْتَمٍ»", "an isti'ara tasrihiyya taba'iyya: shooting at game is borrowed for seeking to visit her, and «مُرْتَمٍ» is derived from it", "istiâre-i tasrîhiyye-i tebeiyye: avı nişan almak onu ziyaret etmeyi istemek için istiare edilmiş ve ondan «مُرْتَمٍ» türetilmiştir", "istiara-tabaiyya", "aqsam-al-istiara"))])

# ---- v. 60 ----
V(60, "It was as if she turned with the neck of a young fawn, a gazelle-kid, pure, white of lip and nose.",
  "Sanki (bize bakarken) dudağı ve burnu beyaz, halis, ceylan yavrularından bir yavrunun boynuyla dönüyordu.",
 [pt("وَكَأَنَّمَا", "ka-annama", PRE("wa-ist", "كَأَنَّمَا"), Fr("حَرْفُ تَشْبِيهٍ كَفَّتْهُ «مَا» الْكَافَّةُ عَنِ الْعَمَلِ", "the particle of likening, kept from governing by the restraining مَا", "kâffe «mâ» ile amelden alıkonmuş teşbîh harfi", "innama-kaffa", "inna-wa-akhawatuha"),
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: «كَأَنَّ الْتِفَاتَهَا إِلَيْنَا فِي نَظَرِهَا الْتِفَاتُ وَلَدِ ظَبْيَةٍ هٰذِهِ صِفَتُهُ فِي نَظَرِهِ» " + ZAW + "؛ وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ لَمْ يُذْكَرْ",
        "here is a tashbih mursal mujmal: «as if her turning to us as she looked were the turning of a gazelle's young, so described, as it looks» (al-Zawzanī); the tool is كَأَنَّ, and the point of likeness is not said",
        "burada mürsel mücmel teşbîh vardır: «bize bakarken dönüşü, böyle nitelenen bir ceylan yavrusunun bakarken dönüşü gibidir» (Zevzenî); edat «كَأَنَّ», vech-i şebeh söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[WA, ("كَأَنَّمَا", "ka-annama", "part")]),
  v("الْتَفَتَتْ", "iltafata", MADI_F, FAIL_BAD, CL_IST, Dn("وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى الْمُتَحَدَّثِ عَنْهَا " + DUR, "the doer is a hidden pronoun returning to the woman spoken of (al-Durra)", "fâil, sözü edilen kadına dönen gizli zamirdir (Dürre)"), g=["form-viii-verbs"]),
  n("بِجِيدِ", "jid", JN("بِ", "جِيدِ"), MDF, TA("الْتَفَتَتْ"), s=[BI, ("جِيدِ", "jid", "noun")]),
  n("جَدَايَةٍ", "jadaya-ant", MI(), Dn("«الْجِدَايَةُ وَالْجَدَايَةُ: وَلَدُ الظَّبْيَةِ، وَالْجَمْعُ الْجَدَايَا» " + ZAW, "«الْجِدَايَة or الْجَدَايَة: a gazelle's young; pl. جَدَايَا» (al-Zawzanī)", "«الْجِدَايَة ve الْجَدَايَة: ceylan yavrusu; ç. جَدَايَا» (Zevzenî)"))],
 [n("رَشَأٍ", "rasha-ant", NAT("جَدَايَةٍ"), Dn("أَوْ بَدَلٌ مِنْهُ، وَهُوَ أَوْلَى عِنْدَهُ " + DUR + "؛ «الرَّشَأُ: الَّذِي قَوِيَ مِنْ أَوْلَادِ الظِّبَاءِ» " + ZAW, "or a badal of it, which he prefers (al-Durra); «الرَّشَأ: a gazelle's young grown strong» (al-Zawzanī)", "yahut ondan bedel; Dürre bunu evlâ görür (Dürre); «الرَّشَأ: ceylan yavrularından güçlenmiş olan» (Zevzenî)")),
  pp("مِنَ", "min", HJ),
  n("الْغِزْلَانِ", "ghazal", MJ(), TA("رَشَأٍ"), Dn("بِاعْتِبَارِ مَعْنَاهُ " + DUR + "؛ جَمْعُ غَزَالٍ " + ZAW, "by its sense (al-Durra); the plural of غَزَال (al-Zawzanī)", "anlamı itibarıyla (Dürre); غَزَال'in cem'i (Zevzenî)", "jam-taksir")),
  n("حُرٍّ", "hurr", NAT("جَدَايَةٍ", "j", "ثَانٍ"), Dn("«الْحُرُّ مِنْ كُلِّ شَيْءٍ: خَالِصُهُ وَجَيِّدُهُ» " + ZAW, "«the حُرّ of anything is its pure and best» (al-Zawzanī)", "«her şeyin حُرّ'ı halisi ve iyisidir» (Zevzenî)")),
  n("أَرْثَمِ", "artham-ant", NAT("جَدَايَةٍ", "j", "ثَالِثٌ"), QT, Dn("وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَصُرِفَ لِضَرُورَةِ الشِّعْرِ " + DUR + "؛ «الْأَرْثَمُ: الَّذِي فِي شَفَتِهِ الْعُلْيَا وَأَنْفِهِ بَيَاضٌ» " + ZAW,
       "by rule it takes no tanwin, an adjective on أَفْعَل; it is declined in full by poetic licence (al-Durra); «الْأَرْثَم: with white on the upper lip and nose» (al-Zawzanī)", "sıfat ve أَفْعَل vezni sebebiyle gayr-i munsarif olması gerekirken şiir zarureti için munsarif kılınmıştır (Dürre); «الْأَرْثَم: üst dudağında ve burnunda beyazlık olan» (Zevzenî)", "mamnu-min-sarf"))])

# =====================================================================================================================
# Chapter 11 — وَصَاةُ الْعَمِّ، وَالْأَدْهَمُ فِي الْحَوْمَةِ (al-Zawzanī vv. 61–68)
# =====================================================================================================================
STEED = ("الْأَدْهَمِ", "the black horse", "yağız ata")

# ---- v. 61 ----
V(61, "I am told that ʿAmr is not thankful for my kindness — and ingratitude sours the soul of the one who gives.",
  "Bana haber verildi ki Amr iyiliğime şükretmiyormuş; nankörlük ise iyilik edenin içini bulandırır.",
 [v("نُبِّئْتُ", "nabbaa", TU_M("ana"), Fr("، وَهِيَ الْمَفْعُولُ الْأَوَّلُ أُقِيمَ مُقَامَ الْفَاعِلِ", ", which is the first object, set in the doer's place", "; bu, fâilin yerine konmuş birinci mef'ûldür", "maful-bihi"), CL_IST,
     Dn("«وَهٰذِهِ مِنْ سَبْعَةِ أَفْعَالٍ تَتَعَدَّى إِلَى ثَلَاثَةِ مَفَاعِيلَ: أُعْلِمْتُ وَأُرِيتُ وَأُنْبِئْتُ وَنُبِّئْتُ وَأُخْبِرْتُ وَخُبِّرْتُ وَحُدِّثْتُ … لِتَضَمُّنِهَا مَعْنَى أَعْلَمْتُ» " + ZAW, "«this is one of seven verbs that take three objects: أُعْلِمْتُ, أُرِيتُ, أُنْبِئْتُ, نُبِّئْتُ, أُخْبِرْتُ, خُبِّرْتُ, حُدِّثْتُ … because they hold the sense of ‹to make known›» (al-Zawzanī)", "«bu, üç mef'ûl alan yedi fiilden biridir: أُعْلِمْتُ, أُرِيتُ, أُنْبِئْتُ, نُبِّئْتُ, أُخْبِرْتُ, خُبِّرْتُ, حُدِّثْتُ … ‹bildirmek› anlamını içerdikleri için» (Zevzenî)"), g=["form-ii-verbs"]),
  pn("عَمْرًا", "amr-name", MF2(), Dn("«وَعَمْرًا هُوَ الْمَفْعُولُ الثَّانِي» " + ZAW, "«and ʿAmr is the second object» (al-Zawzanī)", "«Amr ikinci mef'ûldür» (Zevzenî)")),
  n("غَيْرَ", "ghayr", RO("مَفْعُولٌ بِهِ ثَالِثٌ", "the third object", "üçüncü mef'ûlün bih", "n", "maful-bihi"), MDF),
  n("شَاكِرِ", "shakir", MI(), MDF, Dn("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ " + DUR, "the active participle annexed to its object (al-Durra)", "ism-i fâil mef'ûlüne izâfe edilmiştir (Dürre)", "ism-fail")),
  n("نِعْمَتِي", "nima", MI("jM"), IDF_Y, s=[("نِعْمَتِ", "nima", "noun"), P("ي")])],
 [n("وَالْكُفْرُ", "kufr", PRE("wa-hal", "الْكُفْرُ"), MB(), s=[WA, ("الْكُفْرُ", "kufr", "noun")]),
  n("مَخْبَثَةٌ", "makhbatha-ant", KH(), CL("n", "حَالٌ مِنْ تَاءِ «نُبِّئْتُ»", "a hal of the ta of «نُبِّئْتُ»", "«نُبِّئْتُ»teki tâdan hâl", "al-hal-jumla-wa-rabituha"), Dn("أَوْ مِنْ «عَمْرًا»، وَالرَّابِطُ الْوَاوُ " + DUR + "؛ «وَكُفْرَانُ النِّعْمَةِ يُنَفِّرُ نَفْسَ الْمُنْعِمِ عَنِ الْإِنْعَامِ» " + ZAW, "or of «عَمْرًا»; the link is the waw (al-Durra); «ingratitude for a kindness turns the giver's soul away from giving» (al-Zawzanī)", "yahut «عَمْرًا»dan; râbıt vâvdır (Dürre); «nimete nankörlük, iyilik edenin nefsini iyilikten soğutur» (Zevzenî)")),
  n("لِنَفْسِ", "nafs", JN("لِ", "نَفْسِ"), MDF, TA("مَخْبَثَةٌ"), s=[LI, ("نَفْسِ", "nafs", "noun")]),
  n("الْمُنْعِمِ", "munim-ant", MI(), QA, Dn("اسْمُ فَاعِلٍ مِنْ أَنْعَمَ", "the active participle of أَنْعَمَ", "أَنْعَمَ'in ism-i fâili", "ism-fail"))])

# ---- v. 62 ----
V(62, "And I have kept my uncle's charge, in the forenoon, when the lips draw back from the white of the teeth,",
  "Andolsun, amcamın kuşluk vaktindeki vasiyetini korudum; dudakların dişlerin beyazlığından çekildiği an —",
 [pt("وَلَقَدْ", "qad", Fr("الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ وَالْمُقْسَمُ بِهِ مَحْذُوفٌ تَقْدِيرُهُ: وَاللهِ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَ«قَدْ» حَرْفُ تَحْقِيقٍ",
       "the waw is the waw of the oath, a jarr letter, with the thing sworn by left out — «by God»; the lam falls in the answer of the oath; قَدْ is a particle of certainty", "vâv kasem ve cer harfidir, kendisiyle yemin edilen hazfedilmiştir: «Allah'a andolsun»; lâm kasemin cevabına girmiştir; «قَدْ» tahkîk harfi", "huruf-al-qasam-fil-kafiya", "qad-harf", "hadhf-wa-taqdir"),
     s=[("وَ", "wa-qasam", "prep"), ("لَ", "lam-qasam", "part"), ("قَدْ", "qad", "part")]),
  v("حَفِظْتُ", "hafiza", TU("ana"), CL(0, "جَوَابُ الْقَسَمِ", "is the answer of the oath", "kasemin cevabıdır"), g=["thulathi-mujarrad-babs"]),
  n("وَصَاةَ", "wasat-ant", MF(), MDF, Dn("اسْمُ مَصْدَرٍ مُضَافٌ إِلَى فَاعِلِهِ " + DUR + "؛ «الْوَصَاةُ وَالْوَصِيَّةُ شَيْءٌ وَاحِدٌ» " + ZAW, "a quasi-masdar annexed to its doer (al-Durra); «الْوَصَاة and الْوَصِيَّة are one thing: a charge» (al-Zawzanī)", "fâiline izâfe edilmiş ism-i masdar (Dürre); «الْوَصَاة ile الْوَصِيَّة aynı şeydir» (Zevzenî)", "masdar")),
  n("عَمِّي", "amm-uncle", MI("jM"), IDF_Y, s=[("عَمِّ", "amm-uncle", "noun"), P("ي")]),
  n("بِالضُّحَى", "duha", JN("بِ", "الضُّحَى", "jA", sense=FI_SENSE), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَصَاةَ»", "; the jarr phrase hangs on «وَصَاةَ»", "; câr-mecrûr «وَصَاةَ»ye müteallik"), s=[BI, ("الضُّحَى", "duha", "noun")])],
 [n("إِذْ", "idh", Fr("ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«وَصَاةَ»", "an adverb of past time, built on sukun, in the seat of nasb, hanging on «وَصَاةَ»", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb, «وَصَاةَ»ye müteallik", "maful-fih"), Dn("وَقِيلَ: بَدَلٌ مِنْ «بِالضُّحَى» " + DUR, "it is also said to be a badal of «بِالضُّحَى» (al-Durra)", "«بِالضُّحَى»dan bedel olduğu da söylenmiştir (Dürre)")),
  v("تَقْلِصُ", "qalasa-ant", MUDR(), FAIL_BAD, CL_MI("إِذْ"), Sn("وَهُوَ كِنَايَةٌ عَنْ أَشَدِّ أَحْوَالِ الْحَرْبِ: «وَهِيَ حَالَةُ تَقَلُّصِ الشِّفَاهِ عَنِ الْأَسْنَانِ مِنْ شِدَّةِ كُلُوحِ الْأَبْطَالِ وَالْكُمَاةِ فَرَقًا مِنَ الْقَتْلِ» " + ZAW, "it is a kinaya for the fiercest moment of battle: «the state in which the lips shrink back from the teeth for the heroes' grimacing in dread of death» (al-Zawzanī)", "savaşın en şiddetli hâlinden kinâyedir: «kahramanların ölüm korkusuyla yüzlerini buruşturmalarından dudakların dişlerden çekildiği hâl» (Zevzenî)", "kinaya")),
  n("الشَّفَتَانِ", "shafa-lip", FL("rD")),
  pp("عَنْ", "an", HJ),
  n("وَضَحِ", "wadah-ant", MJ(), MDF, TA("تَقْلِصُ"), Dn("«وَضَحُ الْفَمِ: الْأَسْنَانُ» " + ZAW, "«the وَضَح of the mouth: the teeth» (al-Zawzanī)", "«ağzın وَضَح'ı: dişler» (Zevzenî)")),
  n("الْفَمِ", "fam", MI(), QA)])

# ---- v. 63 ----
V(63, "in the thick of the battle, whose plunging floods the heroes do not complain of but with an inarticulate roar.",
  "— savaşın ortasında; kahramanlar onun boğucu şiddetlerinden anlaşılmaz bir uğultudan başka bir şeyle şikâyet etmez.",
 [pp("فِي", "fi", HJ),
  n("حَوْمَةِ", "hawma-ant", MJ(), MDF, TA("حَفِظْتُ"), Dn("أَوْ بِـ«تَقْلِصُ» " + DUR + "؛ «حَوْمَةُ الْحَرْبِ: مُعْظَمُهَا، وَهِيَ حَيْثُ تَحُومُ الْحَرْبُ أَيْ تَدُورُ» " + ZAW, "or on «تَقْلِصُ» (al-Durra); «the حَوْمَة of battle is its thick, where the battle circles» (al-Zawzanī)", "yahut «تَقْلِصُ»e (Dürre); «savaşın حَوْمَة'sı: en yoğun yeri, savaşın döndüğü yer» (Zevzenî)")),
  n("الْحَرْبِ", "harb", MI(), Dn("وَعِنْدَ الدُّرَّةِ «حَوْمَةِ الْمَوْتِ»", "al-Durra reads «the thick of death»", "Dürre «حَوْمَةِ الْمَوْتِ» okur")),
  pro("الَّتِي", "allati", Fr("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«حَوْمَةِ الْحَرْبِ»", "a relative noun built on sukun, in the seat of jarr, a na't of «حَوْمَةِ الْحَرْبِ»", "sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr, «حَوْمَةِ الْحَرْبِ»in na'tı", "ism-mawsul", "naat-sifa")),
  pt("لَا", "la-nafiya", Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi")),
  v("تَشْتَكِي", "ishtaka-ant", MUDR("y"), FAIL_BAD, CL_SILA, g=["form-viii-verbs", "naqis-verbs"])],
 [n("غَمَرَاتِهَا", "ghamra-ant", MF("nK"), IDF("هَا"), Dn("«غَمَرَاتُ الْحَرْبِ: شَدَائِدُهَا الَّتِي تَغْمُرُ أَصْحَابَهَا، أَيْ تَغْلِبُ قُلُوبَهُمْ وَعُقُولَهُمْ» " + ZAW, "«the غَمَرَات of battle: its hardships that flood over those in it, overwhelming their hearts and minds» (al-Zawzanī)", "«savaşın غَمَرَات'ı: içindekileri boğan, kalplerine ve akıllarına galip gelen şiddetleri» (Zevzenî)"), s=[("غَمَرَاتِ", "ghamra-ant", "noun"), P("هَا")]),
  n("الْأَبْطَالُ", "batal-ant", FL(), Dn("جَمْعُ بَطَلٍ", "the plural of بَطَل", "بَطَل'in cem'i", "jam-taksir")),
  n("غَيْرَ", "ghayr", RO("مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ الْمُنْقَطِعِ", "in nasb as an exception of another kind (munqaṭiʿ)", "munkatı' istisna üzere mansûb", "n", "istithna-mufarragh"), MDF, Dn("وَقَالَ ابْنُ الْأَنْبَارِيِّ: نُصِبَ عَلَى الْمَصْدَرِ، كَأَنَّهُ جَعَلَ التَّغَمْغُمَ مِنَ الشَّكْوَى " + DUR, "Ibn al-Anbārī: it is in nasb as an absolute object, as though the roar were a kind of complaint (al-Durra)", "İbnü'l-Enbârî: mef'ûl-i mutlak olarak mansûbdur, sanki uğultuyu şikâyetin bir türü saymıştır (Dürre)")),
  n("تَغَمْغُمِ", "taghamghum-ant", MI(), QT, Dn("«التَّغَمْغُمُ: صِيَاحٌ وَلَجَبٌ لَا يُفْهَمُ مِنْهُ شَيْءٌ» " + ZAW, "«التَّغَمْغُم: shouting and din from which nothing can be made out» (al-Zawzanī)", "«التَّغَمْغُم: hiçbir şey anlaşılmayan bağırış ve gürültü» (Zevzenî)", "masdar"))])

# ---- v. 64 ----
V(64, "when they shielded themselves with me against the spear-heads, I did not shrink from them — only my place to press forward grew too narrow.",
  "— onlar beni mızrak uçlarına karşı siper ettiklerinde onlardan korkup geri çekilmedim; fakat ilerleyecek yerim daraldı.",
 [n("إِذْ", "idh", Fr("ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«أَخِمْ»", "an adverb of past time, built on sukun, in the seat of nasb, hanging on «أَخِمْ»", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb, «أَخِمْ»e müteallik", "maful-fih")),
  v("يَتَّقُونَ", "ittaqa", MUDR5, CL_MI("إِذْ"), Dn("«الِاتِّقَاءُ: الْحَجْرُ بَيْنَ الشَّيْئَيْنِ … اتَّقَيْتُ الْعَدُوَّ بِتُرْسِي: جَعَلْتُ التُّرْسَ حَاجِزًا بَيْنِي وَبَيْنَ الْعَدُوِّ» " + ZAW, "«الِاتِّقَاء is putting a barrier between two things … ‹I shielded myself from the enemy with my shield›» (al-Zawzanī)", "«الِاتِّقَاء: iki şey arasına engel koymak … ‹düşmana karşı kalkanımı siper ettim›» (Zevzenî)"),
     Sn("وَهُوَ كِنَايَةٌ عَنْ تَقْدِيمِهِ فِي الْحَرْبِ: «أَيْ قَدَّمُونِي وَجَعَلُونِي فِي نُحُورِ أَعْدَائِهِمْ» " + ZAW, "it is a kinaya for his being put in front: «that is, they put me forward and set me at the throats of their enemies» (al-Zawzanī)", "savaşta öne sürülmesinden kinâyedir: «yani beni öne sürüp düşmanlarının göğüslerine karşı koydular» (Zevzenî)", "kinaya"), g=["form-viii-verbs"]),
  pp("بِيَ", "bi", JP("بِ", "يَ", ("الْبَاءُ", "the ba", "bâ")), TA("يَتَّقُونَ"), s=[BI, P("يَ")]),
  n("الْأَسِنَّةَ", "sinan", MF(), Dn("جَمْعُ سِنَانٍ", "the plural of سِنَان, a spear-head", "سِنَان'ın cem'i: mızrak ucu", "jam-taksir")),
  pt("لَمْ", "lam-jazim", LAM_J),
  v("أَخِمْ", "khama-ant", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "a present verb in jazm by لَمْ, its sign the sukun; its middle letter is dropped where two quiescents meet", "«lem» ile meczûm muzâri, alâmeti sükûn; iki sâkin buluştuğu için ayn'ı düşmüştür", "lam-jazim", "nawasib-wa-jawazim-al-mudari"), HID("أَنَا"), CL_IST,
     Dn("وَإِنْ جُعِلَتْ «إِذْ» بَدَلًا مِنْ «إِذْ» فِي الْبَيْتِ ٦٢ فَالْجُمْلَةُ حَالٌ مِنْ يَاءِ «بِيَ» " + DUR + "؛ «الْخَيْمُ: الْجُبْنُ» " + ZAW, "if «إِذْ» is taken as a badal of «إِذْ» in v. 62, the clause is a hal of the ya of «بِيَ» (al-Durra); «الْخَيْم: cowardice» (al-Zawzanī)", "«إِذْ», 62. beyitteki «إِذْ»den bedel sayılırsa cümle «بِيَ»deki yâdan hâl olur (Dürre); «الْخَيْم: korkaklık» (Zevzenî)"), g=["hollow-verbs"])],
 [pp("عَنْهَا", "an", JP("عَنْ", "هَا"), TA("أَخِمْ"), s=[("عَنْ", "an", "prep"), P("هَا")]),
  pt("وَلٰكِنِّي", "lakinna", PRE("wa", "لٰكِنَّ"), Fr("حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "the particle of correction that puts its noun in nasb; the ya is its noun, in the seat of nasb", "istidrâk ve nasb harfi; yâ ismidir, mahallen mansûb", "inna-wa-akhawatuha", "al-bariz-al-muttasil"),
     Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «لَمْ أَخِمْ» " + DUR, "the clause is conjoined to «لَمْ أَخِمْ» (al-Durra)", "cümle «لَمْ أَخِمْ»e ma'tûftur (Dürre)"), s=[WA, ("لٰكِنَّ", "lakinna", "part"), P("ي")]),
  v("تَضَايَقَ", "tadayaqa-ant", MADI, FAIL_BAD, CL("r", "خَبَرُ «لٰكِنَّ»", "the predicate of «لٰكِنَّ»", "«لٰكِنَّ»nin haberi", "inna-wa-akhawatuha"), g=["form-vi-verbs"]),
  n("مُقْدَمِي", "muqdam-ant", FL("rM"), IDF_Y, Dn("«الْمُقْدَمُ: مَوْضِعُ الْإِقْدَامِ» " + ZAW + "؛ وَالْمِيمُ رَوِيُّ الْقَافِيَةِ وَيَاءُ الْمُتَكَلِّمِ بَعْدَهَا وَصْلٌ", "«الْمُقْدَم: the place of pressing forward» (al-Zawzanī); the mim is the rawī and the speaker's ya after it the waṣl", "«الْمُقْدَم: ileri atılma yeri» (Zevzenî); mîm revî, ardındaki mütekellim yâsı vasıldır", "al-qafiya"), s=[("مُقْدَمِ", "muqdam-ant", "noun"), P("ي")])])

# ---- v. 65 ----
V(65, "When I saw the enemy's host advance, urging one another on, I wheeled round upon them, and none could blame me.",
  "Düşman topluluğunun, birbirini savaşa kışkırtarak ilerlediğini görünce, kınanmayacak biri olarak onlara döndüm.",
 [pt("لَمَّا", "lamma", Fr("حَرْفُ وُجُودٍ لِوُجُودٍ", "the particle «when this was, that was»", "vücûd li-vücûd harfi"), Dn("أَوْ ظَرْفٌ بِمَعْنَى «حِينَ»، كَمَا فِي الْبَيْتِ ٥٣ " + DUR, "or an adverb meaning «at the time when», as at v. 53 (al-Durra)", "yahut «حِينَ» anlamında zarf; 53. beyitteki gibi (Dürre)")),
  v("رَأَيْتُ", "raa", TU("ana"), CL(0, "ابْتِدَائِيَّةٌ", "is an opening clause", "ibtidâiyyedir"), g=["naqis-verbs"]),
  n("الْقَوْمَ", "qawm", MF()),
  v("أَقْبَلَ", "aqbala", MADI, FAIL_BAD, CL("n", "مَفْعُولٌ بِهِ ثَانٍ لِـ«رَأَيْتُ» إِنْ كَانَتْ عِلْمِيَّةً", "the second object of «رَأَيْتُ» if it is of knowing", "«رَأَيْتُ» bilmek anlamındaysa ikinci mef'ûlü", "mafulayn"), Dn("أَوْ حَالٌ مِنَ «الْقَوْمَ» إِنْ كَانَتْ بَصَرِيَّةً، بِتَقْدِيرِ «قَدْ» " + DUR, "or a hal of «الْقَوْمَ» if it is of the eye, with قَدْ understood (al-Durra)", "«رَأَيْتُ» gözle görmekse «قَدْ» takdiriyle «الْقَوْمَ»den hâl (Dürre)"), g=["form-iv-verbs"]),
  n("جَمْعُهُمْ", "jam", FL(), IDF("هُمْ"), s=[("جَمْعُ", "jam", "noun"), P("هُمْ")])],
 [v("يَتَذَامَرُونَ", "tadhamara-ant", MUDR5, CL("n", "مَفْعُولٌ ثَانٍ آخَرُ أَوْ حَالٌ أُخْرَى", "a further second object, or a further hal", "bir başka ikinci mef'ûl yahut bir başka hâl", "mafulayn"), Dn("«التَّذَامُرُ: تَفَاعُلٌ مِنَ الذَّمْرِ، وَهُوَ الْحَضُّ عَلَى الْقِتَالِ» " + ZAW, "«التَّذَامُر is the tafā'ul of الذَّمْر, urging to fight» (al-Zawzanī)", "«التَّذَامُر: الذَّمْر'den tefâul; savaşa teşvik etmek» (Zevzenî)"), g=["form-vi-verbs"]),
  v("كَرَرْتُ", "karra-ant", TU("ana"), CL(0, "جَوَابُ «لَمَّا»", "is the answer of «لَمَّا»", "«لَمَّا»nın cevabıdır"), Dn("أَيْ: «عَطَفْتُ عَلَيْهِمْ لِقِتَالِهِمْ» " + ZAW, "that is, «I turned on them to fight them» (al-Zawzanī)", "yani «savaşmak için onlara döndüm» (Zevzenî)"), g=["doubled-verbs"]),
  n("غَيْرَ", "ghayr", HL(), MDF, Dn("مِنْ تَاءِ «كَرَرْتُ» " + DUR, "of the ta of «كَرَرْتُ» (al-Durra)", "«كَرَرْتُ»teki tâdan (Dürre)")),
  n("مُذَمَّمِ", "mudhammam-ant", MI(), QT, Dn("أَيْ: «مَحْمُودُ الْقِتَالِ غَيْرُ مَذْمُومِهِ» " + ZAW, "that is, «praised in the fight, not blamed in it» (al-Zawzanī)", "yani «savaşta övülen, kınanmayan» (Zevzenî)", "ism-maful"))])

# ---- v. 66 ----
V(66, "They called «ʿAntar!» — while the spears were like well-ropes in the breast of the black horse.",
  "«Antere!» diye çağırıyorlardı; mızraklar ise yağız atın göğsünde kuyu ipleri gibiydi.",
 [v("يَدْعُونَ", "daa", MUDR5, CL_IST, g=["naqis-verbs"]),
  pn("عَنْتَرَ", "antara", Fr("مُنَادًى مُرَخَّمٌ حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ، مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى التَّاءِ الْمَحْذُوفَةِ عَلَى لُغَةِ مَنْ يَنْتَظِرُ الْحَرْفَ الْأَخِيرَ، فِي مَحَلِّ نَصْبٍ", "the one called, shortened (tarkhim), its vocative particle dropped; built on a damma estimated on the dropped ta — the usage of those who «wait for» the last letter — in the seat of nasb", "terhîm edilmiş münâdâ, nidâ harfi hazfedilmiş; son harfi «bekleyenlerin» lügatine göre düşen tâ üzerinde takdîrî damme ile mebnî, mahallen mansûb", "vocative-munada", "hadhf-wa-taqdir"),
     Dn("وَيُرْوَى بِالضَّمِّ عَلَى لُغَةِ مَنْ لَا يَنْتَظِرُ، وَيَجُوزُ فِي الْفَتْحِ أَنْ يَكُونَ مَفْعُولًا بِهِ لِـ«يَدْعُونَ»؛ وَالنِّدَائِيَّةُ مَقُولٌ لِقَوْلٍ يُفَسِّرُهُ «يَدْعُونَ» " + DUR, "it is also related with damma, by the usage of those who do not wait; with fatha it may also be the object of «يَدْعُونَ»; the call is the words of a saying that «يَدْعُونَ» implies (al-Durra)", "beklemeyenlerin lügatine göre damme ile de rivayet edilir; fethalı okunuşta «يَدْعُونَ»ün mef'ûlü de olabilir; nidâ cümlesi, «يَدْعُونَ»ün açıkladığı bir sözün mekûlüdür (Dürre)")),
  n("وَالرِّمَاحُ", "rumh", PRE("wa-hal", "الرِّمَاحُ"), MB(), Dn("جَمْعُ رُمْحٍ؛ وَالْجُمْلَةُ حَالٌ مِنْ فَاعِلِ «يَدْعُونَ»، وَالرَّابِطُ الْوَاوُ " + DUR, "the plural of رُمْح; the clause is a hal of the doer of «يَدْعُونَ», the link being the waw (al-Durra)", "رُمْح'un cem'i; cümle «يَدْعُونَ»ün fâilinden hâldir, râbıt vâvdır (Dürre)", "jam-taksir"), s=[WA, ("الرِّمَاحُ", "rumh", "noun")]),
  pt("كَأَنَّهَا", "kaanna", KAANNA_, Fr("، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the attached هَا is its noun, in the seat of nasb", "; bitişik هَا ismidir, mahallen mansûb", "al-bariz-al-muttasil"), CL_KH,
     Sn("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: «شَبَّهَهَا فِي طُولِهَا بِالْحِبَالِ الَّتِي يُسْتَقَى بِهَا مِنَ الْآبَارِ» " + ZAW + "؛ فَالْمُشَبَّهُ الرِّمَاحُ، وَالْمُشَبَّهُ بِهِ أَشْطَانُ الْبِئْرِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ الطُّولُ وَلَمْ يُذْكَرْ",
        "here is a tashbih mursal mujmal: «he likens them, for their length, to the ropes water is drawn from wells with» (al-Zawzanī); the thing likened is the spears, the thing it is likened to the well-ropes, the tool كَأَنَّ, and the point of likeness — length — is not said",
        "burada mürsel mücmel teşbîh vardır: «onları uzunluklarında kuyulardan su çekilen iplere benzetmiştir» (Zevzenî); müşebbeh mızraklar, müşebbehün bih kuyu ipleri, edat «كَأَنَّ», vech-i şebeh — uzunluk — söylenmemiştir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"),
     s=[("كَأَنَّ", "kaanna", "part"), P("هَا")])],
 [n("أَشْطَانُ", "shatan-ant", KH_K(), MDF, Dn("«الشَّطَنُ: الْحَبْلُ الَّذِي يُسْتَقَى بِهِ، وَالْجَمْعُ الْأَشْطَانُ» " + ZAW, "«الشَّطَن: the rope water is drawn with; pl. أَشْطَان» (al-Zawzanī)", "«الشَّطَن: su çekilen ip; ç. أَشْطَان» (Zevzenî)", "jam-taksir")),
  n("بِئْرٍ", "bir", MI()),
  pp("فِي", "fi", HJ),
  n("لَبَانِ", "laban-ant", MJ(), MDF, Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ ثَانٍ لِلْمُبْتَدَإِ «الرِّمَاحُ»", "; the jarr phrase hangs on an omitted second khabar of «الرِّمَاحُ»", "; câr-mecrûr «الرِّمَاحُ» mübtedâsının mahzûf ikinci haberine müteallik"), Dn("«اللَّبَانُ: الصَّدْرُ» " + ZAW, "«اللَّبَان: the breast» (al-Zawzanī)", "«اللَّبَان: göğüs» (Zevzenî)")),
  n("الْأَدْهَمِ", "adham-ant", MI(), QA, Dn("أَرَادَ فَرَسَهُ " + DUR, "he means his own horse (al-Durra)", "kendi atını kastetmiştir (Dürre)"))])

# ---- v. 67 ----
V(67, "I kept charging them with the hollow of his throat and his breast, until he was clothed in blood.",
  "Onun gerdan çukuru ve göğsüyle düşmanlara saldırmayı sürdürdüm; sonunda kana büründü.",
 [pt("مَا", "ma-nafiya", Fr("حَرْفُ نَفْيٍ", "a particle of negation", "nefy harfi")),
  v("زِلْتُ", "zala-ant", Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ «زَالَ»", "a defective past verb built on sukun because the ta is attached; the ta is the noun of زَالَ, in the seat of raf'", "tâ bitiştiği için sükûn üzere mebnî nâkıs mâzî; tâ «زَالَ»in ismidir, mahallen merfû", "kana-wa-akhawatuha", "al-bariz-al-muttasil"), CL_IST, g=["hollow-verbs"]),
  v("أَرْمِيهِمْ", "rama", MUDR("y"), HID("أَنَا"), OBJ("هِمْ"), CL("n", "خَبَرُ «زَالَ»", "the predicate of زَالَ", "«زَالَ»in haberi", "kana-wa-akhawatuha"), Dn("أَيْ: «لَمْ أَزَلْ أَرْمِي الْأَعْدَاءَ بِنَحْرِ فَرَسِي» " + ZAW, "that is, «I never stopped charging the enemy with my horse's throat» (al-Zawzanī)", "yani «düşmanlara atımın gerdanıyla saldırmayı bırakmadım» (Zevzenî)"), g=["naqis-verbs"], s=[("أَرْمِي", "rama", "verb"), P("هِمْ")]),
  n("بِثُغْرَةِ", "thughra-ant", JN("بِ", "ثُغْرَةِ"), MDF, TA("أَرْمِي"), Dn("«الثُّغْرَةُ: الْوَقْبَةُ فِي أَعْلَى النَّحْرِ» " + ZAW + "؛ وَعِنْدَ الدُّرَّةِ «بِغُرَّةِ وَجْهِهِ»", "«الثُّغْرَة: the hollow at the top of the throat» (al-Zawzanī); al-Durra reads «with the blaze of his face»", "«الثُّغْرَة: gerdanın üstündeki çukur» (Zevzenî); Dürre «بِغُرَّةِ وَجْهِهِ» okur"), s=[BI, ("ثُغْرَةِ", "thughra-ant", "noun")]),
  n("نَحْرِهِ", "nahr-chest", MI(), IDF("هِ"), s=[("نَحْرِ", "nahr-chest", "noun"), P("هِ")])],
 [n("وَلَبَانِهِ", "laban-ant", PRE("wa", "لَبَانِ"), ATF("ثُغْرَةِ"), IDF("هِ"), s=[WA, ("لَبَانِ", "laban-ant", "noun"), P("هِ")]),
  pt("حَتَّى", "hatta", Fr("حَرْفُ غَايَةٍ وَجَرٍّ بِمَعْنَى «إِلَى»، بَعْدَهُ «أَنْ» مُضْمَرَةٌ", "a particle of limit and jarr meaning «until», with an أَنْ hidden after it", "«-e kadar» anlamında gâye ve cer harfi, ardında gizli «أَنْ» vardır", "huruf-jarr", "an-masdariyya")),
  v("تَسَرْبَلَ", "tasarbala-ant", MADI, HID("هُوَ", STEED), Dn("وَ«أَنْ» الْمُضْمَرَةُ وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِـ«حَتَّى»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَرْمِيهِمْ» " + DUR, "the hidden أَنْ with the verb makes a masdar in jarr by حَتَّى, and the phrase hangs on «أَرْمِيهِمْ» (al-Durra)", "gizli «أَنْ» ile fiil, «حَتَّى» ile mecrûr masdar te'vîlindedir; câr-mecrûr «أَرْمِيهِمْ»e müteallik (Dürre)"),
     Sn("«وَصَارَ لَهُ بِمَنْزِلَةِ السِّرْبَالِ، أَيْ عَمَّ جَسَدَهُ عُمُومَ السِّرْبَالِ جَسَدَ لَابِسِهِ» " + ZAW, "«the blood became as a shirt to him — it covered his body as a shirt covers the body of the one who wears it» (al-Zawzanī)", "«kan onun için gömlek yerine geçti; gömleğin giyenin bedenini kapladığı gibi onun bedenini kapladı» (Zevzenî)", "tashbih"),
     HD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شَبَّهَ إِحَاطَةَ الدَّمِ بِجَسَدِهِ بِلُبْسِ السِّرْبَالِ، وَاشْتَقَّ مِنْهُ «تَسَرْبَلَ»", "an isti'ara tasrihiyya taba'iyya: he likens the blood's covering his body to putting on a shirt, and derives «تَسَرْبَلَ» from it", "istiâre-i tasrîhiyye-i tebeiyye: kanın bedenini kuşatmasını gömlek giymeye benzetmiş ve ondan «تَسَرْبَلَ» fiilini türetmiştir", "istiara-tabaiyya", "aqsam-al-istiara")),
  n("بِالدَّمِ", "dam", JN("بِ", "الدَّمِ"), TA("تَسَرْبَلَ"), QA, s=[BI, ("الدَّمِ", "dam", "noun")])])

# ---- v. 68 ----
V(68, "He swerved from the falling of the spears upon his breast, and complained to me with a tear and a whinny.",
  "Mızrakların göğsüne inişinden yana kaydı; gözyaşıyla ve hafif bir kişnemeyle bana yakındı.",
 [v("فَازْوَرَّ", "azwarra-ant", PRE("fa", "ازْوَرَّ"), MADI, HID("هُوَ", STEED), CL(0, "مَعْطُوفَةٌ عَلَى «تَسَرْبَلَ»", "is conjoined to «تَسَرْبَلَ»", "«تَسَرْبَلَ»e ma'tûftur"), Dn("وَيُرْوَى بِالْوَاوِ " + DUR + "؛ «الِازْوِرَارُ: الْمَيْلُ» " + ZAW, "it is also related with waw (al-Durra); «الِازْوِرَار: swerving aside» (al-Zawzanī)", "vâv ile de rivayet edilir (Dürre); «الِازْوِرَار: meyletmek» (Zevzenî)"), s=[FA, ("ازْوَرَّ", "azwarra-ant", "verb")]),
  pp("مِنْ", "min", HJ),
  n("وَقْعِ", "waq-ant", MJ(), MDF, TA("ازْوَرَّ"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ " + DUR, "the masdar annexed to its doer (al-Durra)", "masdar fâiline izâfe edilmiştir (Dürre)", "masdar")),
  n("الْقَنَا", "qana", MI("jA")),
  n("بِلَبَانِهِ", "laban-ant", JN("بِ", "لَبَانِ"), IDF("هِ"), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْمَصْدَرِ «وَقْعِ»", "; the jarr phrase hangs on the masdar «وَقْعِ»", "; câr-mecrûr «وَقْعِ» masdarına müteallik"), s=[BI, ("لَبَانِ", "laban-ant", "noun"), P("هِ")])],
 [v("وَشَكَا", "shaka", PRE("wa", "شَكَا"), MADI_A, HID("هُوَ", STEED), CL(0, "مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "is conjoined to the one before", "öncekine ma'tûftur"),
     Sn("أَيْ: «نَظَرَ إِلَيَّ وَحَمْحَمَ لِأَرِقَّ لَهُ» " + ZAW, "that is, «he looked at me and whinnied, that I might feel for him» (al-Zawzanī)", "yani «bana baktı ve kişnedi ki ona acıyayım» (Zevzenî)"),
     HD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شَبَّهَ نَظَرَ الْفَرَسِ وَحَمْحَمَتَهُ بِالشَّكْوَى، وَاشْتَقَّ مِنْهَا «شَكَا»", "an isti'ara tasrihiyya taba'iyya: the horse's look and whinny are likened to complaining, and «شَكَا» is derived from it", "istiâre-i tasrîhiyye-i tebeiyye: atın bakışı ve kişnemesi şikâyete benzetilmiş, ondan «شَكَا» türetilmiştir", "istiara-tabaiyya", "aqsam-al-istiara"), g=["naqis-verbs"], s=[WA, ("شَكَا", "shaka", "verb")]),
  pp("إِلَيَّ", "ila", JP("إِلَى", "ي"), TA("شَكَا")),
  n("بِعَبْرَةٍ", "abra", JN("بِ", "عَبْرَةٍ"), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «شَكَا»", "; the jarr phrase hangs on an omitted hal of the doer of «شَكَا»", "; câr-mecrûr «شَكَا»nın fâilinden mahzûf bir hâle müteallik"), Dn("التَّقْدِيرُ: شَكَا بَاكِيًا بِعَبْرَةٍ " + DUR, "understand: «he complained, weeping a tear» (al-Durra)", "takdir: «gözyaşı dökerek yakındı» (Dürre)"), s=[BI, ("عَبْرَةٍ", "abra", "noun")]),
  n("وَتَحَمْحُمِ", "tahamhum-ant", PRE("wa", "تَحَمْحُمِ"), ATF("عَبْرَةٍ"), QT, Dn("«التَّحَمْحُمُ: مِنْ صَهِيلِ الْفَرَسِ مَا كَانَ فِيهِ شِبْهُ الْحَنِينِ لِيَرِقَّ صَاحِبُهُ لَهُ» " + ZAW, "«التَّحَمْحُم: the kind of neigh in a horse that has a plaintive yearning in it, so that its master may feel for it» (al-Zawzanī)", "«التَّحَمْحُم: atın kişnemesinden, sahibi ona acısın diye içinde inilti benzeri bulunan» (Zevzenî)", "masdar"), s=[WA, ("تَحَمْحُمِ", "tahamhum-ant", "noun")])])

# =====================================================================================================================
# Chapter 12 — شَكْوَى الْفَرَسِ، وَابْنَا ضَمْضَمٍ (al-Zawzanī vv. 69–75)
# =====================================================================================================================
QASAM_LQ = Fr("الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ وَالْمُقْسَمُ بِهِ مَحْذُوفٌ تَقْدِيرُهُ: وَاللهِ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَ«قَدْ» حَرْفُ تَحْقِيقٍ",
              "the waw is the waw of the oath, a jarr letter, with the thing sworn by left out — «by God»; the lam falls in the answer of the oath; قَدْ is a particle of certainty", "vâv kasem ve cer harfidir, kendisiyle yemin edilen hazfedilmiştir: «Allah'a andolsun»; lâm kasemin cevabına girmiştir; «قَدْ» tahkîk harfi", "huruf-al-qasam-fil-kafiya", "qad-harf", "hadhf-wa-taqdir")
S_WLQ = [("وَ", "wa-qasam", "prep"), ("لَ", "lam-qasam", "part"), ("قَدْ", "qad", "part")]
SONS = ("ابْنَيْ ضَمْضَمٍ", "the two sons of Ḍamḍam", "Damdam'ın iki oğluna")

# ---- v. 69 ----
V(69, "Had he known what talk is, he would have complained; and had he known speech, he would have spoken to me.",
  "Konuşmanın ne olduğunu bilseydi şikâyet ederdi; söz bilseydi benimle konuşurdu.",
 [pt("لَوْ", "law", Fr("حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ: لِمَا كَانَ سَيَقَعُ لِوُقُوعِ غَيْرِهِ", "the particle of the unreal condition: of what would have happened had something else happened", "imtinâ' li-imtinâ' harfi: başka bir şey olsaydı olacak olan şey için", "huruf-al-shart-fil-kafiya")),
  v("كَانَ", "kana", Fr("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، فِعْلُ شَرْطِ «لَوْ»", "the defective past verb built on fatha, the verb of the condition of لَوْ", "fetha üzere mebnî nâkıs mâzî, «لَوْ»nun şart fiili", "kana-wa-akhawatuha"), NAQ_SUB("هُوَ", STEED), CL(0, "ابْتِدَائِيَّةٌ", "is an opening clause", "ibtidâiyyedir"), g=["hollow-verbs"]),
  v("يَدْرِي", "dara", MUDR("y"), HID("هُوَ", STEED), CL("n", "خَبَرُ «كَانَ»", "the predicate of كَانَ", "«كَانَ»nin haberi", "kana-wa-akhawatuha"), Dn("وَهُوَ مُعَلَّقٌ عَنِ الْعَمَلِ لَفْظًا بِـ«مَا» الِاسْتِفْهَامِيَّةِ بَعْدَهُ " + DUR, "it is held back from governing in wording by the interrogative مَا after it (al-Durra)", "ardındaki istifhâm «mâ»sı sebebiyle lafzen amelden alıkonmuştur (Dürre)"), g=["naqis-verbs"]),
  pro("مَا", "ma-istifham", Fr("اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "an interrogative noun built on sukun, the mubtada, in the seat of raf'", "sükûn üzere mebnî istifhâm ismi, mübtedâ, mahallen merfû", "al-istifham", "mubtada-khabar")),
  n("الْمُحَاوَرَةُ", "muhawara-ant", KH(), Dn("وَالْجُمْلَةُ الِاسْمِيَّةُ سَدَّتْ مَسَدَّ مَفْعُولَيْ «يَدْرِي» " + DUR + "؛ أَيْ: «لَوْ كَانَ يَعْلَمُ الْخِطَابَ» " + ZAW, "the nominal clause stands for the two objects of «يَدْرِي» (al-Durra); that is, «had he known address» (al-Zawzanī)", "isim cümlesi «يَدْرِي»nin iki mef'ûlünün yerini tutar (Dürre); yani «hitabı bilseydi» (Zevzenî)", "masdar")),
  v("اشْتَكَى", "ishtaka-ant", MADI_A, HID("هُوَ", STEED), CL(0, "جَوَابُ «لَوْ»", "is the answer of لَوْ", "«لَوْ»nun cevabıdır"), g=["form-viii-verbs"])],
 [v("وَلَكَانَ", "kana", Fr("الْوَاوُ عَاطِفَةٌ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ «لَوْ» تَقْدِيرًا، وَ«كَانَ» فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "the waw conjoins; the lam falls in the answer of لَوْ, as understood; كَانَ is a defective past verb built on fatha", "vâv atıf; lâm takdiren «لَوْ»nun cevabına girmiştir; «كَانَ» fetha üzere mebnî nâkıs mâzî", "atf-nasaq", "kana-wa-akhawatuha"),
     NAQ_SUB("هُوَ", STEED), CL(0, "مَعْطُوفَةٌ عَلَى «اشْتَكَى»", "is conjoined to «اشْتَكَى»", "«اشْتَكَى»ya ma'tûftur"), g=["hollow-verbs"], s=[WA, ("لَ", "lam-jawab", "part"), ("كَانَ", "kana", "verb")]),
  pt("لَوْ", "law", Fr("حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ", "the particle of the unreal condition", "imtinâ' li-imtinâ' harfi", "huruf-al-shart-fil-kafiya"), Dn("وَ«لَوْ» وَمَا دَخَلَتْ عَلَيْهِ مُعْتَرِضٌ بَيْنَ «كَانَ» وَخَبَرِهَا، وَجَوَابُهَا مَحْذُوفٌ " + DUR, "لَوْ with what it governs stands between كَانَ and its predicate, and its answer is left out (al-Durra)", "«لَوْ» ve girdiği cümle «كَانَ» ile haberi arasına girmiştir; cevabı hazfedilmiştir (Dürre)")),
  v("عَلِمَ", "alima", MADI, HID("هُوَ", STEED), CL(0, "شَرْطُ «لَوْ»", "is the condition of لَوْ", "«لَوْ»nun şartıdır"), g=["thulathi-mujarrad-babs"]),
  n("الْكَلَامَ", "kalam", MF()),
  n("مُكَلِّمِي", "mukallim-ant", RO("خَبَرُ «كَانَ»", "the predicate of كَانَ", "«كَانَ»nin haberi", "nM", "kana-wa-akhawatuha"), IDF_Y, Dn("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ " + DUR + "؛ «يُرِيدُ أَنَّهُ لَوْ قَدَرَ عَلَى الْكَلَامِ لَشَكَا إِلَيَّ مِمَّا أَصَابَهُ مِنَ الْجِرَاحِ» " + ZAW + "؛ وَالْيَاءُ بَعْدَ الْمِيمِ — رَوِيِّ الْقَافِيَةِ — وَصْلٌ",
       "the active participle annexed to its object (al-Durra); «he means that, could he speak, he would have complained to me of the wounds that struck him» (al-Zawzanī); the ya after the mim, the rawī, is the waṣl", "ism-i fâil mef'ûlüne izâfe edilmiştir (Dürre); «konuşabilseydi başına gelen yaralardan bana yakınırdı demek ister» (Zevzenî); revî olan mîm'den sonraki yâ vasıldır", "ism-fail", "al-qafiya"), s=[("مُكَلِّمِ", "mukallim-ant", "noun"), P("ي")])])

# ---- v. 70 ----
V(70, "And what healed my soul and took its sickness away was the horsemen's cry: «Woe to you, ʿAntar — forward!»",
  "Andolsun, ruhumu iyileştiren ve hastalığını gideren, süvarilerin «Vay sana Antere, ileri!» sözü oldu.",
 [pt("وَلَقَدْ", "qad", QASAM_LQ, s=S_WLQ),
  v("شَفَى", "shafa", MADI_A, Fr("، وَفَاعِلُهُ ضَمِيرٌ يَعُودُ عَلَى «قِيلُ» عِنْدَ الْبَصْرِيِّينَ", "; its doer is a pronoun returning to «قِيلُ», as the Basrans have it", "; Basralılara göre fâili «قِيلُ»e dönen zamirdir", "tanazu"), CL(0, "جَوَابُ الْقَسَمِ", "is the answer of the oath", "kasemin cevabıdır"),
     HD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شَبَّهَ النَّفْسَ الْمَهْمُومَةَ بِالْجِسْمِ الْعَلِيلِ، وَطَوَى الْمُشَبَّهَ بِهِ، وَأَثْبَتَ لَهَا الشِّفَاءَ وَالسُّقْمَ مِنْ لَوَازِمِهِ", "an isti'ara makniyya: the troubled soul is likened to a sick body, the body is folded away, and healing and sickness, which belong to it, are given to the soul", "istiâre-i mekniyye: kederli nefis hasta bir bedene benzetilmiş, beden dürülmüş, onun lâzımı olan şifa ve hastalık nefse verilmiştir", "istiara-makniyya", "aqsam-al-istiara"), g=["naqis-verbs"]),
  n("نَفْسِي", "nafs", MF("nM"), IDF_Y, s=[("نَفْسِ", "nafs", "noun"), P("ي")]),
  v("وَأَذْهَبَ", "adhhaba-ant", PRE("wa", "أَذْهَبَ"), MADI, FAIL_BAD, CL(0, "مَعْطُوفَةٌ عَلَى جَوَابِ الْقَسَمِ", "is conjoined to the answer of the oath", "kasemin cevabına ma'tûftur"), Dn("وَعِنْدَ الدُّرَّةِ «وَأَبْرَأَ»", "al-Durra reads «and cured»", "Dürre «وَأَبْرَأَ» okur"), g=["form-iv-verbs"], s=[WA, ("أَذْهَبَ", "adhhaba-ant", "verb")]),
  n("سُقْمَهَا", "suqm-ant", MF(), IDF("هَا"), s=[("سُقْمَ", "suqm-ant", "noun"), P("هَا")])],
 [n("قِيلُ", "qil", FL(), MDF, Dn("لِـ«أَذْهَبَ» عِنْدَ الْبَصْرِيِّينَ لِقُرْبِهِ — تَنَازَعَهُ الْفِعْلَانِ — وَيَخْتَارُ الْكُوفِيُّونَ الْعَكْسَ " + DUR + "؛ وَهُوَ مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "of «أَذْهَبَ», as the Basrans have it, being nearer — the two verbs contend for it; the Kufans prefer the reverse (al-Durra); the masdar is annexed to its doer", "Basralılara göre yakınlığı sebebiyle «أَذْهَبَ»in fâilidir — iki fiil onun üzerinde tenâzu' eder; Kûfeliler tersini seçer (Dürre); masdar fâiline izâfe edilmiştir", "tanazu", "masdar"),
     Sn("وَهُوَ كِنَايَةٌ عَنْ تَعْوِيلِهِمْ عَلَيْهِ: «يُرِيدُ أَنَّ تَعْوِيلَ أَصْحَابِهِ عَلَيْهِ وَالْتِجَاءَهُمْ إِلَيْهِ شَفَى نَفْسَهُ وَنَفَى غَمَّهُ» " + ZAW, "it is a kinaya for their reliance on him: «he means that his companions' leaning on him and taking refuge in him healed his soul and drove his grief away» (al-Zawzanī)", "ona güvenmelerinden kinâyedir: «arkadaşlarının ona dayanması ve ona sığınmalarının ruhunu iyileştirdiğini ve kederini giderdiğini kasteder» (Zevzenî)", "kinaya")),
  n("الْفَوَارِسِ", "faris-ant", MI(), Dn("جَمْعُ فَارِسٍ", "the plural of فَارِس", "فَارِس'in cem'i", "jam-taksir")),
  n("وَيْكَ", "wayk-ant", Fr("اسْمُ فِعْلٍ مُضَارِعٍ بِمَعْنَى «نَعْجَبُ» مَبْنِيٌّ عَلَى السُّكُونِ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ، وَالْكَافُ حَرْفُ خِطَابٍ لَا مَحَلَّ لَهُ", "a verbal noun with the sense of a present verb, «we wonder», built on sukun; its doer is the hidden «we»; the kaf is a letter of address with no seat", "«hayret ederiz» anlamında muzâri ism-i fiil, sükûn üzere mebnî; fâili vücûben gizli «biz»; kâf mahalli olmayan hitap harfidir", "al-fail-al-mudmar-al-mustatir-wujuban"),
     Dn("وَهُوَ عِنْدَ الزَّوْزَنِيِّ «وَيْلَكَ»: «قَوْلُ الْفَوَارِسِ لِي: وَيْلَكَ يَا عَنْتَرَةُ أَقْدِمْ»", "al-Zawzanī renders it «woe to you»: «the horsemen's saying to me: woe to you, ʿAntara, forward!»", "Zevzenî onu «وَيْلَكَ» diye açıklar: «süvarilerin bana: vay sana ey Antere, ileri! demesi»"), s=[("وَيْ", "wayk-ant", "noun"), ("كَ", "pron-2ms", "pron")]),
  pn("عَنْتَرَ", "antara", Fr("مُنَادًى مُرَخَّمٌ حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ، مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى التَّاءِ الْمَحْذُوفَةِ عَلَى لُغَةِ مَنْ يَنْتَظِرُ الْحَرْفَ الْأَخِيرَ، فِي مَحَلِّ نَصْبٍ", "the one called, shortened (tarkhim), its vocative particle dropped; built on a damma estimated on the dropped ta — the usage of those who «wait for» the last letter — in the seat of nasb", "terhîm edilmiş münâdâ, nidâ harfi hazfedilmiş; son harfi bekleyenlerin lügatine göre düşen tâ üzerinde takdîrî damme ile mebnî, mahallen mansûb", "vocative-munada", "hadhf-wa-taqdir"),
     Dn("وَالنِّدَائِيَّةُ مَقُولٌ لِلْمَصْدَرِ «قِيلُ» " + DUR, "the call is what the masdar «قِيلُ» says (al-Durra)", "nidâ cümlesi «قِيلُ» masdarının mekûlüdür (Dürre)")),
  v("أَقْدِمِ", "aqdama", Fr("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى " + RAWI_J[0], "an imperative built on " + RAWI_J[1], "mebnî emir; binâ alâmeti " + RAWI_J[2], "imperative-amr", "al-qafiya"), HID("أَنْتَ"), Dn("وَالْجُمْلَةُ مَقُولُ الْقَوْلِ أَيْضًا " + DUR + "؛ أَيْ: «أَقْدِمْ نَحْوَ الْعَدُوِّ وَاحْمِلْ عَلَيْهِ» " + ZAW, "the clause too is what is said (al-Durra); that is, «go forward at the enemy and charge him» (al-Zawzanī)", "cümle de mekûlü'l-kavldir (Dürre); yani «düşmana doğru ilerle ve ona saldır» (Zevzenî)"), g=["form-iv-verbs"])])

# ---- v. 71 ----
V(71, "And the horses were plunging through the soft ground, scowling, tall mares and short-haired, tall stallions among them.",
  "Atlar yumuşak, ayak batan arazide suratları asık dalıp gidiyordu; aralarında uzun boylu kısraklar ve kısa tüylü, uzun boylu aygırlar vardı.",
 [n("وَالْخَيْلُ", "khayl", PRE("wa-ist", "الْخَيْلُ"), MB(), s=[WA, ("الْخَيْلُ", "khayl", "noun")]),
  v("تَقْتَحِمُ", "iqtahama-ant", MUDR(), HID("هِيَ", ("الْخَيْلِ", "the horses", "atlara")), CL_KH, g=["form-viii-verbs"]),
  n("الْخَبَارَ", "khabar-soft-ant", MF(), Dn("«الْخَبَارُ: الْأَرْضُ اللَّيِّنَةُ» " + ZAW + "، الَّتِي تَسُوخُ فِيهَا الْقَوَائِمُ", "«الْخَبَار: soft ground» (al-Zawzanī), in which the legs sink", "«الْخَبَار: yumuşak arazi» (Zevzenî), ayakların battığı")),
  n("عَوَابِسًا", "abis-ant", HL(), Dn("مِنَ «الْخَيْلُ»؛ وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ، وَصُرِفَ لِضَرُورَةِ الشِّعْرِ " + DUR + "؛ «وَقَدْ عَبَسَتْ وُجُوهُهَا لِمَا نَالَهَا مِنَ الْإِعْيَاءِ» " + ZAW,
       "of «الْخَيْلُ»; by rule a «farthest plural» takes no tanwin, and it is declined in full here by poetic licence (al-Durra); «their faces scowled for the weariness that came on them» (al-Zawzanī)", "«الْخَيْلُ»den hâl; muntehe'l-cumû' vezninde olduğu için gayr-i munsarif olması gerekirken şiir zarureti için tenvinlenmiştir (Dürre); «yorgunluktan yüzleri asılmıştı» (Zevzenî)", "mamnu-min-sarf", "jam-taksir"))],
 [pp("مِنْ", "min", HJ),
  n("بَيْنِ", "bayna", MJ(), MDF, Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «تَقْتَحِمُ»", "; the jarr phrase hangs on an omitted hal of the doer of «تَقْتَحِمُ»", "; câr-mecrûr «تَقْتَحِمُ»ün fâilinden mahzûf bir hâle müteallik"), Dn("وَ«مِنْ» لِلتَّفْسِيرِ وَالْبَيَانِ " + DUR + "؛ أَيْ: «كُلُّهَا طَوِيلَةٌ» " + ZAW, "مِنْ explains (al-Durra); that is, «all of them are tall» (al-Zawzanī)", "«مِنْ» açıklama içindir (Dürre); yani «hepsi uzun boyludur» (Zevzenî)")),
  n("شَيْظَمَةٍ", "shayzam", MI(), Dn("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ الشَّيْظَمُ: «الطَّوِيلُ مِنَ الْخَيْلِ» " + ZAW, "a na't of a noun left unsaid (al-Durra); شَيْظَم: «tall, of horses» (al-Zawzanī)", "mahzûf bir mevsûfun sıfatıdır (Dürre); شَيْظَم: «atlardan uzun boylu olan» (Zevzenî)", "hadhf-wa-taqdir")),
  n("وَأَجْرَدَ", "ajrad-ant", PRE("wa", "أَجْرَدَ"), ATF("شَيْظَمَةٍ", "jf"), Dn("مُنِعَ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ " + DUR + "؛ وَالْأَجْرَدُ: الْقَصِيرُ الشَّعْرِ مِنَ الْخَيْلِ", "a diptote, an adjective on أَفْعَل, and a na't of a noun left unsaid (al-Durra); الْأَجْرَد: a short-haired horse", "sıfat ve أَفْعَل vezni sebebiyle gayr-i munsarif; mahzûf bir mevsûfun sıfatı (Dürre); الْأَجْرَد: kısa tüylü at", "hadhf-wa-taqdir"), s=[WA, ("أَجْرَدَ", "ajrad-ant", "noun")]),
  n("شَيْظَمِ", "shayzam", SIFA_MD("ثَانٍ"), QT)])

# ---- v. 72 ----
V(72, "My riding-camels are tractable wherever I will; my mind backs me, and I drive it on with a firm resolve.",
  "Binek develerim nereye istersem uysaldır; aklım bana yardımcıdır ve onu sağlam bir kararla ileri sürerim.",
 [n("ذُلُلٌ", "dhalul", RO("خَبَرٌ مُقَدَّمٌ", "the fronted khabar", "öne alınmış haber", "r", "mubtada-khabar", "taqdim-al-musnad"), Dn("جَمْعُ ذَلُولٍ؛ وَيُجِيزُ الْكُوفِيُّ أَنْ يَكُونَ مُبْتَدَأً وَ«رِكَابِي» فَاعِلًا بِهِ سَدَّ مَسَدَّ الْخَبَرِ " + DUR + "؛ «ذُلُلٌ: جَمْعُ ذَلُولٍ مِنَ الذُّلِّ، وَهُوَ ضِدُّ الصُّعُوبَةِ» " + ZAW,
       "the plural of ذَلُول; a Kufan may make it the mubtada with «رِكَابِي» its doer standing for the khabar (al-Durra); «ذُلُل: the plural of ذَلُول, from الذُّلّ, the opposite of hardness» (al-Zawzanī)", "ذَلُول'ün cem'i; Kûfeli onu mübtedâ, «رِكَابِي»yi de haberin yerini tutan fâili sayabilir (Dürre); «ذُلُل: ذَلُول'ün cem'i; الذُّلّ'den, zorluğun zıddı» (Zevzenî)", "jam-taksir")),
  n("رِكَابِي", "rikab-ant", RO("مُبْتَدَأٌ مُؤَخَّرٌ", "the mubtada, placed after its khabar", "sonraya bırakılmış mübtedâ", "rM", "mubtada-khabar"), IDF_Y, s=[("رِكَابِ", "rikab-ant", "noun"), P("ي")]),
  n("حَيْثُ", "haythu", Fr("ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«ذُلُلٌ»", "an adverb of place built on damma, in the seat of nasb, hanging on «ذُلُلٌ»", "damme üzere mebnî mekân zarfı, mahallen mansûb, «ذُلُلٌ»e müteallik", "maful-fih")),
  v("شِئْتُ", "shaa", TU("ana"), CL_MI("حَيْثُ"), g=["hollow-verbs"]),
  n("مُشَايِعِي", "mushayi-ant", RO("خَبَرٌ مُقَدَّمٌ", "the fronted khabar", "öne alınmış haber", "rM", "mubtada-khabar"), IDF_Y, Dn("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ " + DUR + "؛ «الْمُشَايَعَةُ: الْمُعَاوَنَةُ، أُخِذَتْ مِنَ الشِّيَاعِ وَهُوَ دَقَائِقُ الْحَطَبِ لِمُعَاوَنَتِهِ النَّارَ عَلَى الْإِيقَادِ فِي الْحَطَبِ الْجَزْلِ» " + ZAW,
       "the active participle annexed to its object (al-Durra); «الْمُشَايَعَة is helping, taken from الشِّيَاع, kindling, for it helps the fire to catch in the thick wood» (al-Zawzanī)", "ism-i fâil mef'ûlüne izâfe edilmiştir (Dürre); «الْمُشَايَعَة: yardım etmek; ince çırpı anlamındaki الشِّيَاع'dan alınmıştır, çünkü kalın odunda ateşin tutuşmasına yardım eder» (Zevzenî)", "ism-fail"), s=[("مُشَايِعِ", "mushayi-ant", "noun"), P("ي")])],
 [n("لُبِّي", "lubb", RO("مُبْتَدَأٌ مُؤَخَّرٌ", "the mubtada, placed after its khabar", "sonraya bırakılmış mübtedâ", "rM", "mubtada-khabar"), IDF_Y, Dn("أَيْ: «يُعَاوِنُنِي عَلَى أَفْعَالِي عَقْلِي» " + ZAW + "؛ وَعِنْدَ الدُّرَّةِ «قَلْبِي»", "that is, «my mind helps me in what I do» (al-Zawzanī); al-Durra reads «قَلْبِي», my heart", "yani «aklım işlerimde bana yardım eder» (Zevzenî); Dürre «قَلْبِي» okur"), s=[("لُبِّ", "lubb", "noun"), P("ي")]),
  v("وَأَحْفِزُهُ", "hafaza-ant", PRE("wa-ist", "أَحْفِزُ"), MUDR(), HID("أَنَا"), OBJ("هُ"), CL_IST, Dn("أَوْ مَعْطُوفَةٌ عَلَى الِاسْمِيَّةِ بِتَقْدِيرِ: وَأَنَا أَحْفِزُهُ " + DUR + "؛ «الْحَفْزُ: الدَّفْعُ» " + ZAW, "or conjoined to the nominal clause, understood as «and I drive it» (al-Durra); «الْحَفْز: pushing on» (al-Zawzanī)", "yahut «ve ben onu sürerim» takdiriyle isim cümlesine ma'tûf (Dürre); «الْحَفْز: itmek» (Zevzenî)"), g=["thulathi-mujarrad-babs"], s=[WA, ("أَحْفِزُ", "hafaza-ant", "verb"), P("هُ")]),
  n("بِأَمْرٍ", "amr", JN("بِ", "أَمْرٍ"), TA("أَحْفِزُ"), s=[BI, ("أَمْرٍ", "amr", "noun")]),
  n("مُبْرَمِ", "mubram", NAT("أَمْرٍ"), QT, Dn("«الْإِبْرَامُ: الْإِحْكَامُ» " + ZAW, "«الْإِبْرَام: making firm» (al-Zawzanī)", "«الْإِبْرَام: sağlamlaştırmak» (Zevzenî)", "ism-maful"))])

# ---- v. 73 ----
V(73, "And I feared I should die before war's turn of fortune had come round upon the two sons of Ḍamḍam,",
  "Andolsun, Damdam'ın iki oğlunun başına savaşın felaketi dönmeden ölmekten korktum —",
 [pt("وَلَقَدْ", "qad", QASAM_LQ, s=S_WLQ),
  v("خَشِيتُ", "khashiya", TU("ana"), CL(0, "جَوَابُ الْقَسَمِ", "is the answer of the oath", "kasemin cevabıdır"), g=["naqis-verbs"]),
  pt("بِأَنْ", "an-masdariyya", Fr("الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ«أَنْ» حَرْفُ مَصْدَرٍ وَنَصْبٍ", "the ba is an added jarr letter; أَنْ is the particle that makes a masdar and puts the verb in nasb", "bâ zâid cer harfi; «أَنْ» masdar ve nasb harfi", "huruf-al-ziyada-fil-kafiya", "an-masdariyya"),
     Dn("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ لَفْظًا مَنْصُوبٍ مَحَلًّا مَفْعُولٌ بِهِ لِـ«خَشِيتُ»؛ وَقِيلَ: الْبَاءُ أَصْلِيَّةٌ، وَالْمَعْنَى يَأْبَاهُ " + DUR, "أَنْ with the verb makes a masdar, in jarr in wording and in nasb in its seat, the object of «خَشِيتُ»; some take the ba as a true jarr letter, which the sense refuses (al-Durra)", "«أَنْ» ile fiil lafzen mecrûr, mahallen mansûb bir masdar te'vîlindedir, «خَشِيتُ»ün mef'ûlüdür; bâ'yı aslî sayanlar da vardır, ama anlam bunu kabul etmez (Dürre)"), s=[BI, ("أَنْ", "an-masdariyya", "part")]),
  v("أَمُوتَ", "mata-die", Fr("فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "a present verb in nasb by أَنْ, its sign the fatha", "«أَنْ» ile mansûb muzâri, alâmeti fetha", "nawasib-wa-jawazim-al-mudari"), HID("أَنَا"), g=["hollow-verbs"]),
  pt("وَلَمْ", "lam-jazim", PRE("wa-hal", "لَمْ"), LAM_J, s=[WA, ("لَمْ", "lam-jazim", "part")]),
  v("تَدُرْ", "dara-turn", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "a present verb in jazm by لَمْ, its sign the sukun; its middle letter is dropped where two quiescents meet", "«lem» ile meczûm muzâri, alâmeti sükûn; iki sâkin buluştuğu için ayn'ı düşmüştür", "lam-jazim", "nawasib-wa-jawazim-al-mudari"), FAIL_BAD,
     CL("n", "حَالٌ مِنْ فَاعِلِ «أَمُوتَ»", "a hal of the doer of «أَمُوتَ»", "«أَمُوتَ»un fâilinden hâl", "al-hal-jumla-wa-rabituha"), Dn("وَالرَّابِطُ الْوَاوُ؛ وَعِنْدَ الدُّرَّةِ «وَلَمْ تَكُنْ»", "the link is the waw; al-Durra reads «and there was not»", "râbıt vâvdır; Dürre «وَلَمْ تَكُنْ» okur"), g=["hollow-verbs"])],
 [n("لِلْحَرْبِ", "harb", JN("لِ", "الْحَرْبِ"), Fr("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«دَائِرَةٌ» بَعْدَهُمَا", "; the jarr phrase hangs on «دَائِرَةٌ» after it", "; câr-mecrûr sonraki «دَائِرَةٌ»ye müteallik"), Dn("وَقِيلَ: بِمَحْذُوفٍ حَالٍ مِنْهَا كَانَ نَعْتًا فَلَمَّا قُدِّمَ صَارَ حَالًا " + DUR, "or on an omitted hal of it — a na't that, put first, became a hal (al-Durra)", "yahut ondan mahzûf bir hâle; na't iken öne alınınca hâl olmuştur (Dürre)"), s=[LI, ("الْحَرْبِ", "harb", "noun")]),
  n("دَائِرَةٌ", "daira-ant", FL(), Dn("«الدَّائِرَةُ: اسْمٌ لِلْحَادِثَةِ، سُمِّيَتْ بِهَا لِأَنَّهَا تَدُورُ مِنْ خَيْرٍ إِلَى شَرٍّ وَمِنْ شَرٍّ إِلَى خَيْرٍ، ثُمَّ اسْتُعْمِلَتْ فِي الْمَكْرُوهَةِ دُونَ الْمَحْبُوبَةِ» " + ZAW, "«الدَّائِرَة is a name for a turn of fortune, so called because it turns from good to ill and from ill to good; then it was used for the hateful one only» (al-Zawzanī)", "«الدَّائِرَة: başa gelen olayın adıdır; iyiden kötüye, kötüden iyiye döndüğü için böyle adlandırılmış, sonra yalnız hoşa gitmeyen için kullanılmıştır» (Zevzenî)", "ism-fail")),
  pp("عَلَى", "ala", HJ),
  n("ابْنَيْ", "ibn", MJ("jD"), Fr("، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ", "; the nun is dropped for the annexation", "; izâfe sebebiyle nûn düşmüştür", "idafa-definiteness"), TA("تَدُرْ")),
  pn("ضَمْضَمِ", "damdam", MI(), QT, Dn("«وَهُمَا حُصَيْنٌ وَهَرِمٌ ابْنَا ضَمْضَمٍ» " + ZAW, "«they are Ḥuṣayn and Harim, the two sons of Ḍamḍam» (al-Zawzanī)", "«onlar Damdam'ın iki oğlu Husayn ve Herim'dir» (Zevzenî)"))])

# ---- v. 74 ----
V(74, "the two who revile my honour, though I have not reviled them, and who vow — when I am not before them — to shed my blood.",
  "— ben onlara sövmediğim hâlde namusuma söven, ben karşılarında değilken kanımı dökmeyi adayan iki kişi.",
 [n("الشَّاتِمَيْ", "shatim-ant", NAT("ابْنَيْ ضَمْضَمٍ", "jD"), Fr("، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ", "; the nun is dropped for the annexation", "; izâfe sebebiyle nûn düşmüştür", "idafa-definiteness"),
     Dn("وَيَجُوزُ نَصْبُهُ عَلَى الذَّمِّ بِفِعْلٍ مَحْذُوفٍ، وَرَفْعُهُ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ " + DUR, "it may also be in nasb, as blame, by an omitted verb, or in raf' as the khabar of an omitted mubtada (al-Durra)", "mahzûf bir fiille zem üzere mansûb, yahut mahzûf bir mübtedânın haberi olarak merfû da olabilir (Dürre)", "ism-fail")),
  n("عِرْضِي", "ird", MI("jM"), IDF_Y, Dn("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ " + DUR, "the active participle annexed to its object (al-Durra)", "ism-i fâil mef'ûlüne izâfe edilmiştir (Dürre)"), s=[("عِرْضِ", "ird", "noun"), P("ي")]),
  pt("وَلَمْ", "lam-jazim", PRE("wa-hal", "لَمْ"), LAM_J, s=[WA, ("لَمْ", "lam-jazim", "part")]),
  v("أَشْتِمْهُمَا", "shatama", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "a present verb in jazm by لَمْ, its sign the sukun", "«lem» ile meczûm muzâri, alâmeti sükûn", "lam-jazim", "nawasib-wa-jawazim-al-mudari"), HID("أَنَا"), OBJ("هُمَا"),
     CL("n", "حَالٌ مِنْ يَاءِ «عِرْضِي»", "a hal of the ya of «عِرْضِي»", "«عِرْضِي»deki yâdan hâl", "al-hal-jumla-wa-rabituha"),
     HD("بَيْنَهُ وَبَيْنَ «الشَّاتِمَيْ» طِبَاقُ السَّلْبِ: الشَّتْمُ مُثْبَتٌ لَهُمَا وَمَنْفِيٌّ عَنْهُ", "it makes a tibaq al-salb with «الشَّاتِمَيْ»: reviling is affirmed of them and denied of him", "«الشَّاتِمَيْ» ile tıbâk-ı selb oluşturur: sövmek onlar için müspet, onun için menfîdir", "tibaq"), g=["thulathi-mujarrad-babs"], s=[("أَشْتِمْ", "shatama", "verb"), P("هُمَا")])],
 [n("وَالنَّاذِرَيْنِ", "nadhir-ant", PRE("wa", "النَّاذِرَيْنِ"), ATF("الشَّاتِمَيْ", "jD"), Dn("عَلَى جَمِيعِ الْوُجُوهِ فِيهِ " + DUR, "on all the readings it allows (al-Durra)", "onda câiz olan bütün vecihlere göre (Dürre)", "ism-fail"), s=[WA, ("النَّاذِرَيْنِ", "nadhir-ant", "noun")]),
  pt("إِذَا", "idha", Fr("ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«النَّاذِرَيْنِ»", "an adverb of time built on sukun, in the seat of nasb, hanging on «النَّاذِرَيْنِ»", "sükûn üzere mebnî zaman zarfı, mahallen mansûb, «النَّاذِرَيْنِ»e müteallik", "maful-fih"),
     Sn("وَفِيهِ تَعْرِيضٌ بِجُبْنِهِمَا: «يُرِيدُ أَنَّهُمَا يَتَوَعَّدَانِهِ حَالَ غَيْبَتِهِ، فَأَمَّا فِي حَالِ الْحُضُورِ فَلَا يَتَجَاسَرَانِ عَلَيْهِ» " + ZAW, "here is a hint (ta'rid) at their cowardice: «he means they threaten him when he is away; when he is there they dare not» (al-Zawzanī)", "burada korkaklıklarına ta'rîz vardır: «o yokken onu tehdit ederler, o varken ise ona cesaret edemezler demek ister» (Zevzenî)", "kinaya")),
  pt("لَمَ", "lam-jazim", Fr("حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ، وَحَرَكَتُهُ فَتْحَةُ الْهَمْزَةِ بَعْدَهُ نُقِلَتْ إِلَيْهِ", "the particle that negates, puts in jazm and turns to the past; its vowel is the fatha of the hamza after it, moved onto it", "nefy, cezm ve kalb harfi; harekesi, ardındaki hemzenin kendisine nakledilen fethasıdır", "lam-jazim", "nawasib-wa-jawazim-al-mudari")),
  v("الْقَهُمَا", "laqiya", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ، وَأَصْلُهُ «أَلْقَهُمَا» نُقِلَتْ فَتْحَةُ هَمْزَتِهِ إِلَى الْمِيمِ قَبْلَهُ وَحُذِفَتْ", "a present verb in jazm by لَمْ, its sign the dropping of the weak letter; it is «أَلْقَهُمَا», the fatha of its hamza moved onto the mim before it and the hamza dropped", "«lem» ile meczûm muzâri, alâmeti illet harfinin hazfi; aslı «أَلْقَهُمَا»dır, hemzesinin fethası önceki mîm'e nakledilip hemze hazfedilmiştir", "naqis-verbs"),
     HID("أَنَا"), OBJ("هُمَا"), CL_MI("إِذَا"), Dn("وَعِنْدَ الدُّرَّةِ «لَمْ أَلْقَهُمَا»، وَيُرْوَى «لَقِيتُهُمَا»", "al-Durra writes «لَمْ أَلْقَهُمَا»; it is also related «لَقِيتُهُمَا»", "Dürre «لَمْ أَلْقَهُمَا» yazar; «لَقِيتُهُمَا» diye de rivayet edilir"), s=[("الْقَ", "laqiya", "verb"), P("هُمَا")]),
  n("دَمِي", "dam", RO("مَفْعُولٌ بِهِ لِـ«النَّاذِرَيْنِ»", "the object of «النَّاذِرَيْنِ»", "«النَّاذِرَيْنِ»in mef'ûlü", "nM", "maful-bihi"), IDF_Y, Dn("وَالْيَاءُ بَعْدَ الْمِيمِ — رَوِيِّ الْقَافِيَةِ — وَصْلٌ", "the ya after the mim, the rawī, is the waṣl", "revî olan mîm'den sonraki yâ vasıldır", "al-qafiya"), s=[("دَمِ", "dam", "noun"), P("ي")])])

# ---- v. 75 ----
V(75, "If they do it — well, I left their father a slaughter-beast for the beasts of prey and for every aged vulture.",
  "Bunu yaparlarsa (şaşılmaz); andolsun, ben onların babasını yırtıcılara ve her yaşlı akbabaya kesimlik bir hayvan gibi bıraktım.",
 [pt("إِنْ", "in-shartiyya", Fr("حَرْفُ شَرْطٍ جَازِمٌ", "the conditional particle that puts in jazm", "cezmeden şart harfi", "in-shartiyya", "al-majzum-wal-shart-wal-jaza")),
  v("يَفْعَلَا", "faala", Fr("فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "a present verb in jazm, the verb of the condition, its sign the dropping of the nun — it is one of the five verbs; the alif of the two is its doer, in the seat of raf'", "şart fiili olarak meczûm muzâri, ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; tesniye elifi fâildir, mahallen merfû", "afal-khamsa", "al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil"),
     CL(0, "ابْتِدَائِيَّةٌ", "is an opening clause", "ibtidâiyyedir"), Dn("أَيْ: «إِنْ يَشْتُمَانِي لَمْ أَسْتَغْرِبْ مِنْهُمَا ذٰلِكَ» " + ZAW, "that is, «if they revile me, I do not wonder at it from them» (al-Zawzanī)", "yani «bana söverlerse bunu onlardan garip karşılamam» (Zevzenî)"), g=["thulathi-mujarrad-babs"]),
  pt("فَلَقَدْ", "qad", Fr("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مَحْذُوفٍ، وَ«قَدْ» حَرْفُ تَحْقِيقٍ", "the fa falls in the answer of the condition; the lam falls in the answer of an omitted oath; قَدْ is a particle of certainty", "fâ şartın cevabına girmiştir; lâm mahzûf bir kasemin cevabına girmiştir; «قَدْ» tahkîk harfi", "al-fa-fi-jawab-al-shart", "qad-harf", "hadhf-wa-taqdir"), s=[FA, ("لَ", "lam-qasam", "part"), ("قَدْ", "qad", "part")]),
  v("تَرَكْتُ", "taraka", TU("ana"), CL(0, "جَوَابُ الْقَسَمِ", "is the answer of the oath", "kasemin cevabıdır"), Dn("وَالْقَسَمُ وَجَوَابُهُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ؛ وَإِنْ قُدِّرَ الْجَوَابُ مَحْذُوفًا — فَلَا أَلُومُهُمَا — فَالْقَسَمِيَّةُ تَعْلِيلٌ " + DUR, "the oath with its answer is in the seat of jazm, the answer of the condition; or, if the answer is taken as left out — «I do not blame them» — the oath clause gives the reason (al-Durra)", "kasem ve cevabı şartın cevabı olarak mahallen meczûmdur; cevap mahzûf sayılırsa — «onları kınamam» — kasem cümlesi ta'lîldir (Dürre)", "mafulayn")),
  n("أَبَاهُمَا", "ab", MF1("n5"), IDF("هُمَا"), s=[("أَبَا", "ab", "noun"), P("هُمَا")])],
 [n("جَزَرَ", "jazara-ant", MF2(), MDF, Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ " + DUR, "the masdar annexed to its doer (al-Durra)", "masdar fâiline izâfe edilmiştir (Dürre)"),
     Sn("وَفِيهِ التَّشْبِيهُ الْبَلِيغُ الَّذِي فِي الْبَيْتِ ٥٠: «قَتَلْتُ أَبَاهُمَا وَصَيَّرْتُهُ جَزَرَ السِّبَاعِ» " + ZAW, "here is the tashbih baligh of v. 50: «I killed their father and made him a slaughter-beast for the beasts of prey» (al-Zawzanī)", "burada 50. beyitteki belîğ teşbîh vardır: «babalarını öldürdüm ve onu yırtıcılara kesimlik hayvan kıldım» (Zevzenî)", "tashbih", "aqsam-al-tashbih")),
  n("السِّبَاعِ", "sabu", MI()),
  n("وَكُلِّ", "kull", PRE("wa", "كُلِّ"), ATF("السِّبَاعِ"), MDF, s=[WA, ("كُلِّ", "kull", "noun")]),
  n("نَسْرٍ", "nasr-bird-ant", MI()),
  n("قَشْعَمِ", "qasham", NAT("نَسْرٍ"), QT, Dn("أَيْ: «كُلِّ نَسْرٍ مُسِنٍّ» " + ZAW, "that is, «every aged vulture» (al-Zawzanī)", "yani «her yaşlı akbaba» (Zevzenî)"))])

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

# ---- vv. 9–15 ----
def _dbl(bab, f, l, masdar, fail, maful=None, pmz=None, pmd=None):
    """a doubled Form-I verb: bab "nasara" (يَفْعُلُ) or "samia" (يَفْعَلُ)"""
    b, w = _sg.BABS[bab]; mv = "ُ" if bab == "nasara" else "َ" if bab == "samia" else "ِ"
    fk = {"nasara": "َ", "samia": "ِ", "daraba": "َ"}[bab]
    amr = [f + mv + l + "َّ", f + mv + l + "َّا", f + mv + l + "ُّوا", f + mv + l + "ِّي", f + mv + l + "َّا", "ا" + ("ُ" if bab == "nasara" else "ِ") + f + "ْ" + l + mv + l + "ْنَ"]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(f + "َ" + l + "ّ", f + "َ" + l + fk + l), _sg.mudari14("َ", f + mv + l + "ّ", f + "ْ" + l + mv + l),
                     amr, "يَ" + f + mv + l + "َّ", "يَ" + f + mv + l + "َّ", "تَ" + f + mv + l + "َّ", maful, pmz, pmd,
                     note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَ" + f + mv + l + "َّ، وَيَجُوزُ الْفَكُّ: لَمْ يَ" + f + "ْ" + l + mv + l + "ْ.")
NEW_GLOSS.update({
 "mazar-ant": G("مَزَار", "noun", "visiting, a visit (a mīmī masdar, like زِيَارَة — al-Zawzanī); a place one visits", "ziyaret (mîmî masdar, زِيَارَة gibi — Zevzenî); ziyaret edilen yer", 6, "ز و ر"),
 "tarabbaa-ant": G("تَرَبَّعَ", "verb", "to spend the spring at a place (Form V; التَّرَبُّع: staying through the spring — al-Zawzanī)", "bir yerde baharı geçirmek (tefe''ul; التَّرَبُّع: bahar mevsimi boyunca konaklamak — Zevzenî)", 6, "ر ب ع", form="V"),
 "unayzatan-ant": G("عُنَيْزَتَان", "propn", "ʿUnayzatān — two places, named in the dual", "Uneyzeteyn — tesniye ile anılan iki yer", 6),
 "ghaylam-ant": G("الْغَيْلَم", "propn", "al-Ghaylam — a place", "Gaylem — bir yer adı", 6),
 "zamma-ant": G("زَمَّ", "verb", "to put the nose-rein (زِمَام) on a camel, made ready for travel (زَمَّ يَزُمُّ)", "deveye yular (زِمَام) takmak, yolculuğa hazırlamak (زَمَّ يَزُمُّ)", 6, "ز م م"),
 "rikab-ant": G("رِكَاب", "noun", "riding camels — a plural with no singular of its own form; al-Farrāʾ: its singular is رَكُوب (al-Zawzanī)", "binek develeri — kendi lafzından müfredi olmayan cem'; Ferrâ'ya göre müfredi رَكُوب (Zevzenî)", 6, "ر ك ب"),
 "raa-alarm-ant": G("رَاعَ", "verb", "to alarm, to frighten (رَاعَهُ رَوْعًا: أَفْزَعَهُ — al-Zawzanī)", "korkutmak, ürkütmek (رَاعَهُ رَوْعًا: أَفْزَعَهُ — Zevzenî)", 6, "ر و ع"),
 "hamula-ant": G("حَمُولَة", "noun", "pack-camels — the camels strong enough to be loaded (al-Zawzanī)", "yük develeri — üzerine yük vurulabilen develer (Zevzenî)", 6, "ح م ل"),
 "saffa-ant": G("سَفَّ", "verb", "to take a dry thing (seed, powder) into the mouth, to crop (سَفَّ يَسَفُّ)", "kuru bir şeyi (tane, toz) ağza atmak, otlamak (سَفَّ يَسَفُّ)", 6, "س ف ف"),
 "khimkhim-ant": G("خِمْخِم", "noun", "khimkhim — a plant whose seed camels are fed (al-Zawzanī)", "himhim — tanesi develere yem olarak verilen bir bitki (Zevzenî)", 6, "خ م خ م"),
 "khafiya-ant": G("خَافِيَة", "noun", "one of the hidden inner feathers of a wing, four in each wing (pl. خَوَافٍ — al-Zawzanī)", "kanadın içte kalan gizli tüylerinden biri, her kanatta dört tane (ç. خَوَافٍ — Zevzenî)", 6, "خ ف ي", "خَوَافٍ"),
 "asham-ant": G("أَسْحَم", "noun", "black (الْأَسْحَمُ: الْأَسْوَدُ — al-Zawzanī)", "siyah (الْأَسْحَمُ: الْأَسْوَدُ — Zevzenî)", 6, "س ح م"),
 "istaba-ant": G("اسْتَبَى", "verb", "to take captive, to captivate (Form VIII of س ب ي; الِاسْتِبَاء and السَّبْي are one — al-Zawzanī)", "esir almak, gönlünü tutsak etmek (س ب ي kökünden ifti'âl; الِاسْتِبَاء ile السَّبْي birdir — Zevzenî)", 6, "س ب ي", form="VIII"),
 "gharb-ant": G("غَرْب", "noun", "the edge, the sharpness of a thing (pl. غُرُوب); ذُو غُرُوبٍ: a mouth of keen-edged teeth (al-Zawzanī)", "bir şeyin keskin kenarı (ç. غُرُوب); ذُو غُرُوبٍ: keskin dişli ağız (Zevzenî)", 6, "غ ر ب", "غُرُوب"),
 "muqabbal-ant": G("مُقَبَّل", "noun", "the place one kisses (noun of place on the passive participle's pattern — al-Zawzanī)", "öpülen yer (ism-i mef'ûl vezninde ism-i mekân — Zevzenî)", 6, "ق ب ل"),
 "matam-ant": G("مَطْعَم", "noun", "taste (here = الطَّعْم — al-Zawzanī); food", "tat (burada الطَّعْم — Zevzenî); yiyecek", 6, "ط ع م"),
 "fara-ant": G("فَارَة", "noun", "a musk-pod (فَارَةُ الْمِسْكِ), lightened from فَائِرَة: sweet smells «well up» from it (al-Zawzanī)", "misk kesesi (فَارَةُ الْمِسْكِ); فَائِرَة'den hafifletilmiş: güzel kokular ondan «kaynar» (Zevzenî)", 6, "ف و ر"),
 "qasima-ant": G("قَسِيمَة", "noun", "a fair, comely woman (from الْقَسَامَة: beauty — al-Zawzanī)", "güzel yüzlü kadın (الْقَسَامَة «güzellik»ten — Zevzenî)", 6, "ق س م"),
 "arida-ant": G("عَارِضَة", "noun", "one of the side teeth; pl. عَوَارِض, the teeth at the sides of the mouth", "yan dişlerden biri; ç. عَوَارِض, ağzın yanlarındaki dişler", 6, "ع ر ض", "عَوَارِض"),
 "unuf-ant": G("أُنُف", "noun", "untouched, fresh — رَوْضَةٌ أُنُفٌ: a meadow not yet grazed (al-Zawzanī)", "dokunulmamış, taze — رَوْضَةٌ أُنُفٌ: henüz otlanmamış çayır (Zevzenî)", 6, "أ ن ف"),
 "malam-ant": G("مَعْلَم", "noun", "a known place, a landmark that people make for and tread", "bilinen yer, insanların gidip çiğnediği işaretli mekân", 6, "ع ل م"),
})
NEW_VERBS.update({
 "tarabbaa-ant": _dv(_sg.B5, _sg.W5, "َ", "تَرَبَّع", "تَرَبَّع", "تَرَبَّع", "تَرَبُّع", "مُتَرَبِّع"),
 "zamma-ant": _dbl("nasara", "ز", "م", "زَمّ", "زَامّ", "مَزْمُوم", "زُمَّ", "يُزَمُّ"),
 "raa-alarm-ant": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "رَاع", "رُع", "رُوع", "رُع", "رُوع", "رُع", "رَوْع", "رَائِع", "مَرُوع", "رِيعَ", "يُرَاعُ", _sg.HOLLOW_NOTE.format(ex="رُعْتَ")),
 "saffa-ant": _dbl("samia", "س", "ف", "سَفّ", "سَافّ", "مَسْفُوف", "سُفَّ", "يُسَفُّ"),
 "istaba-ant": _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِسْتَبَ", "سْتَب", "i", "اِسْتَب", "اِسْتِبَاء", "مُسْتَبٍ (الْمُسْتَبِي)"),
})
DIV += [
 (10, "الْبَيْتُ ١٠ «رِكَابُكُمْ» ← «رِكَابُكُمُ» بِضَمِّ الْمِيمِ وَإِشْبَاعِهَا، وَالشَّاهِدُ الْوَزْنُ (لَا يَسْتَقِيمُ الْكَامِلُ بِسُكُونِهَا) وَإِعْرَابُ الدُّرَّةِ: «حُرِّكَتْ بِالضَّمِّ لِضَرُورَةِ الشِّعْرِ فَتَوَلَّدَتْ وَاوُ الْإِشْبَاعِ»", "v. 10 «رِكَابُكُمْ» → «رِكَابُكُمُ», the mīm with damma, lengthened — witness: the metre (al-kāmil does not scan with the sukūn) and al-Durra's iʿrāb («moved with damma for the poet's need, so that a lengthening waw was born»)", "10. beyit «رِكَابُكُمْ» → «رِكَابُكُمُ», mîm'in dammesi ve uzatılmasıyla — şâhit: vezin (kâmil sükûnla yürümez) ve Dürre'nin i'râbı («şiir zarureti için damme ile harekelendi, böylece işbâ vâvı doğdu»)"),
]

# ---- vv. 16–21 ----
NEW_GLOSS.update({
 "sahh-ant": G("سَحّ", "noun", "pouring, pouring down (masdar of سَحَّ يَسُحُّ; «السَّحُّ: الصَّبُّ وَالِانْصِبَابُ جَمِيعًا» — al-Zawzanī)", "dökmek, dökülmek (سَحَّ يَسُحُّ'nin masdarı; Zevzenî: «hem dökmek hem dökülmek»)", 6, "س ح ح"),
 "taskab-ant": G("تَسْكَاب", "noun", "pouring, streaming (a masdar on تَفْعَال, = السَّكْب — al-Zawzanī)", "dökmek, akıtmak (تَفْعَال vezninde masdar, السَّكْب ile aynı — Zevzenî)", 6, "س ك ب"),
 "tasarrama-ant": G("تَصَرَّمَ", "verb", "to be cut off, to come to an end (Form V; التَّصَرُّم: الِانْقِطَاع — al-Zawzanī)", "kesilmek, sona ermek (tefe''ul; التَّصَرُّم: kesilme — Zevzenî)", 6, "ص ر م", form="V"),
 "barih-ant": G("بَارِح", "noun", "leaving, going away — the active participle of the defective بَرِحَ; لَيْسَ بِبَارِحٍ: it does not cease", "ayrılan, giden — nâkıs بَرِحَ'in ism-i fâili; لَيْسَ بِبَارِحٍ: durmaksızın …", 6, "ب ر ح"),
 "gharid-ant": G("غَرِد", "noun", "making a sound, trilling, humming (adjective of غَرَّدَ — al-Zawzanī)", "ses çıkaran, şakıyan, vızıldayan (غَرَّدَ'nin sıfatı — Zevzenî)", 6, "غ ر د"),
 "mutarannim-ant": G("مُتَرَنِّم", "noun", "singing to oneself, turning the voice over in melody (active participle of تَرَنَّمَ)", "kendi kendine terennüm eden, sesini nağmeyle döndüren (تَرَنَّمَ'nin ism-i fâili)", 6, "ر ن م"),
 "hazij-ant": G("هَزِج", "noun", "making a sound, humming (هَزِجًا: مُصَوِّتًا — al-Zawzanī)", "ses çıkaran, vızıldayan (هَزِجًا: مُصَوِّتًا — Zevzenî)", 6, "ه ز ج"),
 "hakka-ant": G("حَكَّ", "verb", "to rub, to scratch (حَكَّ يَحُكُّ)", "sürtmek, kaşımak (حَكَّ يَحُكُّ)", 5, "ح ك ك"),
 "mukibb-ant": G("مُكِبّ", "noun", "bent over a thing, intent upon it (active participle of أَكَبَّ; «الْمُكِبُّ: الْمُقْبِلُ عَلَى الشَّيْءِ» — al-Zawzanī)", "bir şeyin üzerine eğilen, ona yönelen (أَكَبَّ'nin ism-i fâili — Zevzenî)", 6, "ك ب ب"),
 "zinad-ant": G("زِنَاد", "noun", "fire-sticks, the steel and flint fire is struck from (pl. of زَنْد)", "çakmak çubukları, ateş çakılan çakmak (زَنْد'ın cem'i)", 6, "ز ن د"),
 "ajdham-ant": G("أَجْذَم", "noun", "with a maimed or cut hand («الْأَجْذَمُ: النَّاقِصُ الْيَدِ» — al-Zawzanī)", "eli kesik, eli eksik (Zevzenî)", 6, "ج ذ م"),
 "hashiyya-ant": G("حَشِيَّة", "noun", "a stuffed cushion, a mattress (pl. حَشَايَا — al-Zawzanī)", "doldurulmuş minder, döşek (ç. حَشَايَا — Zevzenî)", 6, "ح ش و", "حَشَايَا"),
 "sarat-ant": G("سَرَاة", "noun", "the top of the back; the best part of a thing («السَّرَاةُ: أَعْلَى الظَّهْرِ» — al-Zawzanī)", "sırtın en üstü; bir şeyin en iyisi (Zevzenî)", 6, "س ر و"),
 "adham-ant": G("أَدْهَم", "noun", "black (of a horse), a black horse; a diptote (an adjective on أَفْعَل)", "yağız, siyah (at); gayr-i munsarif (أَفْعَل vezninde sıfat)", 6, "د ه م"),
 "abl-ant": G("عَبْل", "noun", "thick, stout («الْعَبْلُ: الْغَلِيظُ» — al-Zawzanī); عَبْلُ الشَّوَى: thick of limb", "kalın, iri (Zevzenî); عَبْلُ الشَّوَى: kalın bacaklı", 6, "ع ب ل"),
 "shawan-ant": G("شَوًى", "noun", "the extremities, the legs of a beast («الشَّوَى: الْأَطْرَافُ وَالْقَوَائِمُ» — al-Zawzanī)", "uzuvlar, hayvanın bacakları (Zevzenî)", 6, "ش و ي"),
 "nahd-ant": G("نَهْد", "noun", "big and tall, full («النَّهْدُ: الضَّخْمُ الْمُشْرِفُ» — al-Zawzanī)", "iri ve yüksek, dolgun (Zevzenî)", 6, "ن ه د"),
 "markal-ant": G("مَرْكَل", "noun", "the place where the rider's heel strikes the horse's flank (pl. مَرَاكِل — al-Zawzanī)", "binicinin topuğunun atın böğrüne vurduğu yer (ç. مَرَاكِل — Zevzenî)", 6, "ر ك ل", "مَرَاكِل"),
 "nabil-ant": G("نَبِيل", "noun", "stout, fat (al-Zawzanī: borrowed for good and for evil); noble", "besili, semiz (Zevzenî: iyilik ve kötülük için de istiare edilir); soylu", 6, "ن ب ل"),
 "mahzim-ant": G("مَحْزِم", "noun", "the place of the girth on a beast's body (al-Zawzanī)", "hayvanın gövdesinde kolanın yeri (Zevzenî)", 6, "ح ز م"),
})
NEW_VERBS.update({
 "tasarrama-ant": _dv(_sg.B5, _sg.W5, "َ", "تَصَرَّم", "تَصَرَّم", "تَصَرَّم", "تَصَرُّم", "مُتَصَرِّم"),
 "hakka-ant": _dbl("nasara", "ح", "ك", "حَكّ", "حَاكّ", "مَحْكُوك", "حُكَّ", "يُحَكُّ"),
})
TAILOR.update({
 "jada": ("to give freely; (of rain) to fall abundantly — جَادَتْ عَلَيْهِ: it rained heavily upon it", "cömertçe vermek; (yağmur) bol yağmak — جَادَتْ عَلَيْهِ: üzerine bol yağdı"),
 "bikr": ("the first of its kind; (of a cloud) the one whose rain comes first (al-Zawzanī)", "türünün ilki; (bulut için) yağmuru önce gelen (Zevzenî)"),
 "hurr": ("free; pure, the best of a thing — of a cloud: free of hail and wind (al-Zawzanī)", "hür; bir şeyin halisi, en iyisi — bulut için: doludan ve rüzgârdan arınmış (Zevzenî)"),
 "qarara": ("a resting place; a hollow in the ground where water gathers (al-Zawzanī: الْحُفْرَة)", "karar yeri; suyun toplandığı çukur (Zevzenî: الْحُفْرَة)"),
 "qadh": ("striking fire (from fire-sticks); (of speech) disparaging", "(çakmaktan) ateş çakma; (sözde) yerme, kusur bulma"),
 "khala": ("to be empty; خَلَا بِهِ: to have a place to oneself", "boş olmak; خَلَا بِهِ: bir yerde yalnız kalmak, orayı kendine ayırmak"),
})
DIV += [
 (20, "الْبَيْتُ ٢٠ «مُلجِمِ» ← «مُلْجَمِ» بِفَتْحِ الْجِيمِ اسْمَ مَفْعُولٍ، وَالشَّاهِدُ الْمَعْنَى عِنْدَ الشَّارِحَيْنِ: فَرَسٌ عَلَيْهِ لِجَامُهُ («فَوْقَ ظَهْرِ فَرَسٍ أَدْهَمَ مُلْجَمٍ» — الزَّوْزَنِيُّ وَالدُّرَّةُ)، وَالْكَلِمَةُ عِنْدَهُمَا غَيْرُ مَشْكُولَةٍ", "v. 20 «مُلجِمِ» → «مُلْجَمِ», fatha on the jīm, a passive participle — witness: the sense both commentators give, a horse with its bridle on («on the back of a black, bridled horse» — al-Zawzanī and al-Durra); neither vowels the word", "20. beyit «مُلجِمِ» → «مُلْجَمِ», cîm'in fethasıyla ism-i mef'ûl — şâhit: iki şârihin verdiği mânâ, gemi takılı at («gemli yağız bir atın sırtında» — Zevzenî ve Dürre); ikisi de kelimeyi harekelememiştir"),
]
FLAGS += [
 (20, "جِيمُ «مُلْجَمِ» (ب ٢٠): طُبِعَتْ مَكْسُورَةً، وَالْفَتْحُ مِنَ الْمَعْنَى لَا مِنْ نُسْخَةٍ مَشْكُولَةٍ", "the jīm of «مُلْجَمِ» (v. 20): printed with kasra; the fatha comes from the sense, not from a vowelled witness", "«مُلْجَمِ»in cîm'i (b. 20): kesreyle basılmış; fetha bir harekeli nüshadan değil mânâdan alınmıştır"),
]

# ---- vv. 22–27 ----
NEW_GLOSS.update({
 "shadaniyya-ant": G("شَدَنِيَّة", "noun", "a she-camel of Shadan — «a land or a tribe camels are named after» (al-Zawzanī)", "Şeden devesi — «develerin nispet edildiği bir yer ya da kabile» (Zevzenî)", 6, "ش د ن"),
 "musarram-ant": G("مُصَرَّم", "noun", "cut off (passive participle of صَرَّمَ; التَّصْرِيم: cutting — al-Zawzanī); of an udder: dried up", "kesilmiş (صَرَّمَ'in ism-i mef'ûlü; التَّصْرِيم: kesmek — Zevzenî); meme için: kurumuş", 6, "ص ر م"),
 "khattara-ant": G("خَطَّارَة", "noun", "(a she-camel) that swings and raises her tail as she goes — an intensive form from خَطَرَ بِذَنَبِهِ", "yürürken kuyruğunu kaldırıp sallayan (deve) — خَطَرَ بِذَنَبِهِ'den mübalağa sîgası", 6, "خ ط ر"),
 "ghibb-ant": G("غِبّ", "noun", "the after of a thing; غِبَّ: after (adverbial)", "bir şeyin ardı; غِبَّ: -den sonra (zarf olarak)", 6, "غ ب ب"),
 "sura-ant": G("سُرًى", "noun", "travelling by night, the night journey", "gece yürüyüşü, gece yolculuğu", 6, "س ر ي"),
 "zayyafa-ant": G("زَيَّافَة", "noun", "(a she-camel) that swaggers as she goes — intensive form; الزَّيَف: التَّبَخْتُر (al-Zawzanī)", "salınarak yürüyen (deve) — mübalağa sîgası; الزَّيَف: salınmak (Zevzenî)", 6, "ز ي ف"),
 "watasa-ant": G("وَطَسَ", "verb", "to break, to crush with the foot (وَطَسَ يَطِسُ; الْوَطْسُ وَالْوَثْمُ: الْكَسْرُ — al-Zawzanī)", "kırmak, ayakla ezmek (وَطَسَ يَطِسُ; Zevzenî: الْوَطْسُ وَالْوَثْمُ: kırmak)", 6, "و ط س"),
 "akama-ant": G("أَكَمَة", "noun", "a hillock, a mound (pl. إِكَام)", "tepecik, tümsek (ç. إِكَام)", 6, "أ ك م", "إِكَام"),
 "wakhdh-ant": G("وَخْذ", "noun", "so printed in the edition of al-Zawzanī (v. 23), sense not glossed there; al-Durra reads وَخْد, «a swift pace» — left for the scholar", "Zevzenî neşrinde böyle basılmıştır (b. 23), orada anlamı açıklanmaz; Dürre وَخْد «hızlı yürüyüş» okur — âlimin incelemesine bırakılmıştır", 6),
 "maytham-ant": G("مِيثَم", "noun", "crushing hard — an intensive form, «as if it were the very tool of crushing (الْوَثْم)» (al-Zawzanī)", "çok ezen — mübalağa sîgası, «sanki ezmenin (الْوَثْم) aletiymiş gibi» (Zevzenî)", 6, "و ث م"),
 "musallam-ant": G("مُصَلَّم", "noun", "with the ears cut away — said of the ostrich, which has no ears (الصَّلْم: الِاسْتِئْصَال — al-Zawzanī)", "kulakları kökünden kesik — kulağı olmayan devekuşu için söylenir (Zevzenî)", 6, "ص ل م"),
 "qalus-ant": G("قَلُوص", "noun", "a young she-camel or young ostrich — «as the young girl among people» (pl. قُلُص, قَلَائِص — al-Zawzanī)", "genç dişi deve ya da genç devekuşu — «insanlardaki genç kız gibi» (ç. قُلُص, قَلَائِص — Zevzenî)", 6, "ق ل ص", "قُلُص"),
 "hizqa-ant": G("حِزْقَة", "noun", "a group, a herd (pl. حِزَق — al-Zawzanī)", "topluluk, sürü (ç. حِزَق — Zevzenî)", 6, "ح ز ق", "حِزَق"),
 "timtim-ant": G("طِمْطِم", "noun", "one who cannot speak plainly, tongue-tied (al-Zawzanī)", "açık konuşamayan, dili tutuk (Zevzenî)", 6, "ط م ط م"),
 "qulla-ant": G("قُلَّة", "noun", "the top of a thing; قُلَّةُ الرَّأْسِ: the top of the head (al-Zawzanī)", "bir şeyin tepesi; قُلَّةُ الرَّأْسِ: başın tepesi (Zevzenî)", 6, "ق ل ل"),
 "nash-ant": G("نَعْش", "noun", "a raised thing, a frame (al-Zawzanī: in the sense of مَنْعُوش); a bier", "yükseltilmiş şey, sedir (Zevzenî: مَنْعُوش anlamında); tabut", 6, "ن ع ش"),
 "mukhayyam-ant": G("مُخَيَّم", "noun", "made into a tent (passive participle of خَيَّمَ — al-Zawzanī)", "çadır yapılmış (خَيَّمَ'nin ism-i mef'ûlü — Zevzenî)", 6, "خ ي م"),
 "sal-ant": G("صَعْل", "noun", "small of head (= أَصْعَل — al-Zawzanī)", "küçük başlı (= أَصْعَل — Zevzenî)", 6, "ص ع ل"),
 "ushayra-ant": G("الْعُشَيْرَة", "propn", "in ذُو الْعُشَيْرَة, a place (al-Zawzanī)", "ذُو الْعُشَيْرَة adında, bir yer (Zevzenî)", 6),
 "bayd-ant": G("بَيْض", "noun", "eggs (collective; one: بَيْضَة)", "yumurtalar (cins ismi; tekili بَيْضَة)", 5, "ب ي ض"),
 "hidj-ant": G("حِدْج", "noun", "a women's camel-litter («مَرْكَبٌ مِنْ مَرَاكِبِ النِّسَاءِ» — al-Zawzanī; pl. حُدُوج)", "kadın hevdeci («kadın binitlerinden biri» — Zevzenî; ç. حُدُوج)", 6, "ح د ج"),
 "naam-ant": G("نَعَام", "noun", "ostriches (collective; one: نَعَامَة)", "devekuşları (cins ismi; tekili نَعَامَة)", 5, "ن ع م"),
 "farw-ant": G("فَرْو", "noun", "a fur, a garment of fur", "kürk", 6, "ف ر و"),
 "aslam-ant": G("أَصْلَم", "noun", "with no ears, the ears cut away (al-Zawzanī)", "kulaksız, kulakları kesik (Zevzenî)", 6, "ص ل م"),
})
NEW_VERBS.update({
 "watasa-ant": _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مِثَالٌ وَاوِيٌّ", "فَعَلَ يَفْعِلُ", "وَطْس", "وَاطِس", _sg.mazi14("وَطَس"), _sg.mudari14("َ", "طِس"), _sg.amr_attach("طِس"),
     "يَطِسَ", "يَطِسْ", "تَطِسْ", "مَوْطُوس", "وُطِسَ", "يُوطَسُ", note="مِثَالٌ وَاوِيٌّ مِنْ بَابِ ضَرَبَ: تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ وَالْأَمْرِ — يَطِسُ، طِسْ؛ وَالْبَابُ مِنَ الْبَيْتِ نَفْسِهِ: «تَطِسُ» بِكَسْرِ الطَّاءِ."),
})
TAILOR.update({
 "khuff": ("the foot of a camel or an ostrich, its pad; a leather sock", "devenin ya da devekuşunun tabanı; mest"),
 "ada-visit": ("to visit (the sick); to tend, to look after (يَعُودُ: يَتَعَهَّدُ — al-Zawzanī)", "(hastayı) ziyaret etmek; gözetmek, bakmak (يَعُودُ: يَتَعَهَّدُ — Zevzenî)"),
})
DIV += [
 (24, "الْبَيْتُ ٢٤ «بَيْنَ» ← «بَيْنِ» بِالْجَرِّ، وَالشَّاهِدُ إِعْرَابُ الدُّرَّةِ: «قَرِيبٌ مُضَافٌ وَبَيْنُ مُضَافٌ إِلَيْهِ»، وَ«قَرِيبِ» قَبْلَهُ بِلَا تَنْوِينٍ لَا يَكُونُ إِلَّا مُضَافًا", "v. 24 «بَيْنَ» → «بَيْنِ», in jarr — witness: al-Durra's iʿrāb («قَرِيب is annexed and بَيْن is its second term»), and «قَرِيبِ» before it, without tanwin, can only be annexed", "24. beyit «بَيْنَ» → «بَيْنِ», cerle — şâhit: Dürre'nin i'râbı («قَرِيب muzâf, بَيْن muzâfun ileyh») ve tenvinsiz «قَرِيبِ» ancak muzâf olabilir"),
]
FLAGS += [
 (23, "«بِوَخْذِ» (ب ٢٣): طُبِعَ بِالذَّالِ وَالشَّرْحُ يَذْكُرُ «بِوَخْدِ» رِوَايَةً أُخْرَى، وَالدُّرَّةُ يَقْرَأُ «بِوَخْدِ»؛ أُبْقِيَ مَا طُبِعَ، وَسُكُونُ الْخَاءِ مِنَ الْوَزْنِ", "«بِوَخْذِ» (v. 23): printed with dhāl, while the commentary gives «بِوَخْدِ» as another version and al-Durra reads «بِوَخْدِ»; the print is kept, and the sukūn on the khāʾ comes from the metre", "«بِوَخْذِ» (b. 23): zâl ile basılmış; şerh «بِوَخْدِ»i başka bir rivayet olarak anar, Dürre «بِوَخْدِ» okur; basılan korunmuştur, hâ'nın sükûnu vezindendir"),
 (24, "نُونُ «بَيْنِ» (ب ٢٤): طُبِعَتْ مَفْتُوحَةً، وَالْجَرُّ مِنْ إِعْرَابِ الدُّرَّةِ", "the nūn of «بَيْنِ» (v. 24): printed with fatha; the jarr comes from al-Durra's iʿrāb", "«بَيْنِ»in nûn'u (b. 24): fethalı basılmış; cer Dürre'nin i'râbındandır"),
 (24, "سِينُ «الْمَنْسَمَيْنِ» (ب ٢٤): كَذَا طُبِعَتْ بِالْفَتْحِ، وَالْمَعْرُوفُ «مَنْسِم» بِالْكَسْرِ؛ أُبْقِيَ مَا طُبِعَ", "the sīn of «الْمَنْسَمَيْنِ» (v. 24): so printed, with fatha, where the word is known as «مَنْسِم» with kasra; the print is kept", "«الْمَنْسَمَيْنِ»in sîn'i (b. 24): fethayla böyle basılmış, bilinen ise kesreli «مَنْسِم»dir; basılan korunmuştur"),
]

# ---- vv. 28–33 ----
NEW_GLOSS.update({
 "duhrudan-ant": G("الدُّحْرُضَان", "propn", "al-Duḥruḍān — a place with waters, named in the dual", "Duhrudeyn — suları olan, tesniye ile anılan bir yer", 6),
 "azwar-ant": G("أَزْوَر", "noun", "leaning aside, turning away (fem. زَوْرَاء, pl. زُور; الزَّوَر: الْمَيْل — al-Zawzanī)", "yana meyleden, yüz çeviren (müe. زَوْرَاء, ç. زُور; الزَّوَر: meyil — Zevzenî)", 6, "ز و ر"),
 "daylam-ant": G("الدَّيْلَم", "propn", "the Daylam — a people of the Persian highlands; «the waters of the Daylam» are known waters, or the Arabs call any enemy «Daylam» (al-Zawzanī)", "Deylem — İran dağlık bölgesinin bir kavmi; «Deylem suları» bilinen sulardır, yahut Araplar her düşmana «Deylem» der (Zevzenî)", 6),
 "daff-ant": G("دَفّ", "noun", "the side, the flank («الدَّفُّ: الْجَنْبُ» — al-Zawzanī)", "yan, böğür (Zevzenî)", 6, "د ف ف"),
 "wahshi-ant": G("وَحْشِيّ", "noun", "wild; الْجَانِبُ الْوَحْشِيُّ: the right side of a beast, where one neither mounts nor dismounts (al-Zawzanī)", "yabanî; الْجَانِبُ الْوَحْشِيُّ: hayvanın, ne binilen ne inilen sağ tarafı (Zevzenî)", 6, "و ح ش"),
 "muawwam-ant": G("مُؤَوَّم", "noun", "with a big, ugly head (al-Zawzanī)", "başı iri ve çirkin (Zevzenî)", 6, "أ و م"),
 "hirr-ant": G("هِرّ", "noun", "a cat, a tom-cat", "kedi, erkek kedi", 5, "ه ر ر"),
 "janib-ant": G("جَنِيب", "noun", "led at the side, led along (= مَجْنُوب، مَقُود — al-Zawzanī)", "yana bağlanıp yedilen (= مَجْنُوب، مَقُود — Zevzenî)", 6, "ج ن ب"),
 "baraka-ant": G("بَرَكَ", "verb", "(of a camel) to kneel down (بَرَكَ يَبْرُكُ بُرُوكًا)", "(deve) çökmek (بَرَكَ يَبْرُكُ بُرُوكًا)", 5, "ب ر ك"),
 "janb-ant": G("جَنْب", "noun", "side, flank; عَلَى جَنْبِ: by the side of", "yan, böğür; عَلَى جَنْبِ: -in yanında", 5, "ج ن ب"),
 "rida-ant": G("الرِّدَاع", "propn", "al-Ridāʿ — a place (al-Zawzanī)", "Ridâ' — bir yer (Zevzenî)", 6),
 "qasab-ant": G("قَصَب", "noun", "reeds, canes (collective)", "kamış (cins ismi)", 5, "ق ص ب"),
 "ajashsh-ant": G("أَجَشّ", "noun", "harsh-sounding, with a hoarse sound («لَهُ صَوْتٌ» — al-Zawzanī); a diptote", "kaba sesli, boğuk ses veren («sesi olan» — Zevzenî); gayr-i munsarif", 6, "ج ش ش"),
 "muhaddam-ant": G("مُهَضَّم", "noun", "broken, crushed («مُكَسَّر» — al-Zawzanī)", "kırılmış, ezilmiş («مُكَسَّر» — Zevzenî)", 6, "ه ض م"),
 "rubb-ant": G("رُبّ", "noun", "thick boiled juice, syrup («الرُّبُّ: الطِّلَاءُ» — al-Zawzanī)", "koyu kaynatılmış usare, pekmez (Zevzenî)", 6, "ر ب ب"),
 "kuhayl-ant": G("كُحَيْل", "noun", "pitch, tar («الْكُحَيْلُ: الْقَطِرَانُ» — al-Zawzanī)", "katran (Zevzenî)", 6, "ك ح ل"),
 "muqad-ant": G("مُعْقَد", "noun", "boiled until thick (passive participle of أَعْقَدَ; «عَقَدْتُ الدَّوَاءَ: أَغْلَيْتُهُ حَتَّى خَثُرَ» — al-Zawzanī)", "koyulaşana dek kaynatılmış (أَعْقَدَ'nin ism-i mef'ûlü — Zevzenî)", 6, "ع ق د"),
 "hashsha-ant": G("حَشَّ", "verb", "to kindle (a fire), to stoke it (حَشَّ يَحُشُّ — al-Zawzanī)", "(ateşi) tutuşturmak, harlatmak (حَشَّ يَحُشُّ — Zevzenî)", 6, "ح ش ش"),
 "waqud-ant": G("وَقُود", "noun", "firewood; (وُقُود, with damma) kindling (al-Zawzanī)", "odun, yakacak; (dammeli وُقُود) tutuşturma (Zevzenî)", 5, "و ق د"),
 "qumqum-ant": G("قُمْقُم", "noun", "a cauldron, a copper pot", "kazan, bakır kap", 6, "ق م ق م"),
 "dhifra-ant": G("ذِفْرَى", "noun", "the bone behind the ear (of a camel), where the sweat breaks out (al-Zawzanī)", "(devede) kulak arkasındaki kemik, terin çıktığı yer (Zevzenî)", 6, "ذ ف ر"),
 "ghadub-ant": G("غَضُوب", "noun", "quick to anger (intensive form of غَضِبَ)", "çabuk öfkelenen (غَضِبَ'den mübalağa sîgası)", 6, "غ ض ب"),
 "jasra-ant": G("جَسْرَة", "noun", "(a she-camel) strongly built («الْمُوثَقَةُ الْخَلْقِ» — al-Zawzanī)", "sağlam yapılı (dişi deve) (Zevzenî)", 6, "ج س ر"),
 "mukdam-ant": G("مُكْدَم", "noun", "bitten (by other stallions) — «قَدْ كَدَمَتْهُ الْفُحُولُ» (al-Zawzanī)", "(öteki aygırlarca) ısırılmış (Zevzenî)", 6, "ك د م"),
})
NEW_VERBS.update({
 "baraka-ant": _sg1("nasara", "بَرَك", "بْرُك", "اُبْرُك", "بُرُوك", "بَارِك"),
 "hashsha-ant": _dbl("nasara", "ح", "ش", "حَشّ", "حَاشّ", "مَحْشُوش", "حُشَّ", "يُحَشُّ"),
})
TAILOR.update({
 "hawd": ("a basin, a watering pool (pl. حِيَاض)", "havuz, sulak (ç. حِيَاض)"),
 "atafa": ("to incline, to turn (towards or upon); (with عَلَى) to feel compassion", "eğilmek, (bir şeye) dönmek; (عَلَى ile) şefkat göstermek"),
 "ittaqa": ("to guard oneself against, to fear; to meet, to face (اتَّقَاهَا: اسْتَقْبَلَهَا — al-Zawzanī)", "sakınmak, korunmak; karşılamak (اتَّقَاهَا: اسْتَقْبَلَهَا — Zevzenî)"),
 "nabaa": ("to gush, to ooze, to spring forth; يَنْبَاعُ is يَنْبَعُ with its fatha lengthened for the metre (al-Zawzanī)", "fışkırmak, sızmak; يَنْبَاعُ, vezin için fethası uzatılmış يَنْبَعُ'dur (Zevzenî)"),
 "bayna": ("between (adverb of place); as a noun, the space between", "arasında (mekân zarfı); isim olarak: ara"),
})
DIV += [
 (29, "الْبَيْتُ ٢٩ مُدَوَّرٌ: قَسَمَتِ النَّشْرَةُ «الْوَحْشِيِّ» بَيْنَ الْمِصْرَاعَيْنِ (الـ … وَحْشِيّ)، وَعَلَامَةُ الْمِصْرَاعِ هُنَا بَعْدَ «دَفِّهَا» لِأَنَّ الْكَلِمَةَ لَا تُقْسَمُ", "v. 29 runs on (mudawwar): the edition divides «الْوَحْشِيِّ» between the hemistichs (الـ … وَحْشِيّ); here the hemistich mark stands after «دَفِّهَا», since a word is not split", "29. beyit müdevverdir: neşir «الْوَحْشِيِّ» kelimesini iki mısra arasında böler (الـ … وَحْشِيّ); burada mısra işareti «دَفِّهَا»dan sonradır, çünkü kelime bölünmez"),
 (30, "الْبَيْتُ ٣٠ «باليَديَنِ» ← «بِالْيَدَيْنِ»: طُبِعَتِ الْفَتْحَةُ عَلَى الْيَاءِ الثَّانِيَةِ، وَالشَّاهِدُ الْوَزْنُ وَإِعْرَابُ الدُّرَّةِ (مُثَنًّى مَجْرُورٌ بِالْيَاءِ)", "v. 30 «باليَديَنِ» → «بِالْيَدَيْنِ»: the fatha was printed on the second yāʾ — witness: the metre and al-Durra's iʿrāb (a dual in jarr by the yāʾ)", "30. beyit «باليَديَنِ» → «بِالْيَدَيْنِ»: fetha ikinci yâ üzerine basılmış — şâhit: vezin ve Dürre'nin i'râbı (yâ ile mecrûr tesniye)"),
]

# ---- vv. 34–40 ----
NEW_GLOSS.update({
 "aghdafa-ant": G("أَغْدَفَ", "verb", "to let down (a veil), to let fall (Form IV; الْإِغْدَاف: الْإِرْخَاء — al-Zawzanī)", "(peçeyi) indirmek, salıvermek (if'âl; الْإِغْدَاف: الْإِرْخَاء — Zevzenî)", 6, "غ د ف", form="IV"),
 "qina-ant": G("قِنَاع", "noun", "a veil, a woman's head-covering", "peçe, kadın baş örtüsü", 5, "ق ن ع"),
 "tabb-ant": G("طَبّ", "noun", "skilled, expert («طَبٌّ: حَاذِقٌ عَالِمٌ» — al-Zawzanī)", "usta, mahir («حَاذِقٌ عَالِمٌ» — Zevzenî)", 6, "ط ب ب"),
 "faris-ant": G("فَارِس", "noun", "a horseman, a rider (pl. فُرْسَان)", "süvari, atlı (ç. فُرْسَان)", 4, "ف ر س", "فُرْسَان"),
 "athna-ant": G("أَثْنَى", "verb", "to praise (أَثْنَى عَلَيْهِ; Form IV, naqis)", "övmek (أَثْنَى عَلَيْهِ; if'âl, nâkıs)", 5, "ث ن ي", form="IV"),
 "samh-ant": G("سَمْح", "noun", "easy, generous, gracious; سَمْحُ الْمُخَالَقَةِ: easy to deal with", "kolay, cömert, yumuşak; سَمْحُ الْمُخَالَقَةِ: geçimi kolay", 6, "س م ح"),
 "mukhalaqa-ant": G("مُخَالَقَة", "noun", "dealing with people in character (mufā'ala of الْخُلُق — al-Zawzanī)", "insanlarla ahlâkla muamele (الْخُلُق'tan müfâale — Zevzenî)", 6, "خ ل ق"),
 "basil-ant": G("بَاسِل", "noun", "grim, hateful; (of a man) brave (al-Zawzanī)", "çetin, çirkin; (adam için) yiğit (Zevzenî)", 6, "ب س ل"),
 "murr-ant": G("مُرّ", "noun", "bitter", "acı", 5, "م ر ر"),
 "madhaqa-ant": G("مَذَاقَة", "noun", "taste, the tasting of a thing", "tat, tadım", 6, "ذ و ق"),
 "alqam-ant": G("عَلْقَم", "noun", "colocynth, the bitter gourd — anything very bitter", "ebucehil karpuzu, acı kabak — çok acı olan her şey", 6, "ع ل ق م"),
 "rakada-ant": G("رَكَدَ", "verb", "to settle, to grow still («رَكَدَ: سَكَنَ» — al-Zawzanī; رَكَدَ يَرْكُدُ)", "durulmak, durgunlaşmak («سَكَنَ» — Zevzenî; رَكَدَ يَرْكُدُ)", 6, "ر ك د"),
 "hajira-ant": G("هَاجِرَة", "noun", "the midday heat, the hottest time of the day (pl. هَوَاجِر — al-Zawzanī)", "öğle sıcağı, günün en sıcak vakti (ç. هَوَاجِر — Zevzenî)", 6, "ه ج ر", "هَوَاجِر"),
 "mashuf-ant": G("مَشُوف", "noun", "polished, made to shine (al-Zawzanī: the polished dinar)", "cilalanmış, parlatılmış (Zevzenî: parlatılmış dinar)", 6, "ش و ف"),
 "mulam-ant": G("مُعْلَم", "noun", "marked, bearing marks; (of a coin) stamped", "işaretli, üzerinde alâmetler bulunan; (para için) damgalı", 6, "ع ل م"),
 "sirar-ant": G("سِرَر", "noun", "a line, a crease of the hand or brow (also سِرّ; pl. أَسِرَّة, أَسَارِير — al-Zawzanī)", "çizgi, el ya da alın kırışığı (سِرّ da denir; ç. أَسِرَّة, أَسَارِير — Zevzenî)", 6, "س ر ر", "أَسِرَّة"),
 "azhar-ant": G("أَزْهَر", "noun", "bright, shining white; a diptote (an adjective on أَفْعَل)", "parlak, ak; gayr-i munsarif (أَفْعَل vezninde sıfat)", 6, "ز ه ر"),
 "mufaddam-ant": G("مُفَدَّم", "noun", "with its mouth stopped by a cloth (فِدَام) (al-Zawzanī)", "ağzı bir bezle (فِدَام) tıkanmış (Zevzenî)", 6, "ف د م"),
 "mustahlik-ant": G("مُسْتَهْلِك", "noun", "one who uses up, spends to the last (active participle of اسْتَهْلَكَ)", "tüketen, son kuruşuna dek harcayan (اسْتَهْلَكَ'in ism-i fâili)", 6, "ه ل ك"),
 "wafir-ant": G("وَافِر", "noun", "abundant, whole, untouched", "bol, tam, eksiksiz", 5, "و ف ر"),
 "kalama-ant": G("كَلَمَ", "verb", "to wound (كَلَمَهُ يَكْلِمُهُ كَلْمًا)", "yaralamak (كَلَمَهُ يَكْلِمُهُ كَلْمًا)", 6, "ك ل م"),
 "nada-ant": G("نَدًى", "noun", "dew, moisture; open-handedness, generosity", "çiy, nem; cömertlik", 6, "ن د ي"),
 "takarrum-ant": G("تَكَرُّم", "noun", "generosity, acting nobly (masdar of تَكَرَّمَ)", "cömertlik, kerem gösterme (تَكَرَّمَ'nin masdarı)", 6, "ك ر م"),
})
NEW_VERBS.update({
 "aghdafa-ant": _dv(_sg.B4, _sg.W4, "ُ", "أَغْدَف", "غْدِف", "أَغْدِف", "إِغْدَاف", "مُغْدِف", "مُغْدَف", "أُغْدِفَ", "يُغْدَفُ"),
 "athna-ant": _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ يَائِيٌّ", _sg.W4, "ُ", "أَثْنَ", "ثْن", "i", "أَثْن", "إِثْنَاء", "مُثْنٍ", note="نَاقِصٌ مِنَ الْإِفْعَالِ: أَثْنَى يُثْنِي — لَمْ يُثْنِ، وَالْأَمْرُ: أَثْنِ، أَثْنِي."),
 "rakada-ant": _sg1("nasara", "رَكَد", "رْكُد", "اُرْكُد", "رُكُود", "رَاكِد"),
 "kalama-ant": _sg1("daraba", "كَلَم", "كْلِم", "اِكْلِم", "كَلْم", "كَالِم", "مَكْلُوم", "كُلِمَ", "يُكْلَمُ"),
})
TAILOR.update({
 "dhat": ("possessor of (the feminine of ذُو); essence, self", "sahibi (ذُو'nun müennesi); öz, zat"),
 "shimal": ("left, the left hand; (pl. شَمَائِل) nature, character", "sol, sol el; (ç. شَمَائِل) huy, tabiat"),
})
DIV += [
 (38, "الْبَيْتُ ٣٨ «مَفَدَّمِ» ← «مُفَدَّمِ» بِضَمِّ الْمِيمِ اسْمَ مَفْعُولٍ مِنْ فَدَّمَ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ «مَسْدُودُ الرَّأْسِ بِالْفِدَامِ»، وَلَيْسَ فِي الْعَرَبِيَّةِ «مَفَعَّلٌ»", "v. 38 «مَفَدَّمِ» → «مُفَدَّمِ», damma on the mīm, the passive participle of فَدَّمَ — witness: al-Zawzanī's gloss «its head stopped with the فِدَام»; Arabic has no pattern مَفَعَّل", "38. beyit «مَفَدَّمِ» → «مُفَدَّمِ», mîm'in dammesiyle, فَدَّمَ'den ism-i mef'ûl — şâhit: Zevzenî'nin şerhi «başı فِدَام ile tıkanmış»; Arapçada مَفَعَّل vezni yoktur"),
 (39, "الْبَيْتُ ٣٩ «وَعْرِضِي» ← «وَعِرْضِي»، وَالشَّاهِدُ الْوَزْنُ وَإِعْرَابُ الدُّرَّةِ (عِرْضِي مُبْتَدَأٌ)", "v. 39 «وَعْرِضِي» → «وَعِرْضِي» (the sukūn printed on the wrong letter) — witness: the metre and al-Durra's iʿrāb («عِرْضِي» a mubtadaʾ)", "39. beyit «وَعْرِضِي» → «وَعِرْضِي» (sükûn yanlış harfe basılmış) — şâhit: vezin ve Dürre'nin i'râbı («عِرْضِي» mübtedâ)"),
]
FLAGS += [
 (38, "مِيمُ «مُفَدَّمِ» (ب ٣٨): طُبِعَتْ مَفْتُوحَةً، وَالضَّمُّ مِنَ الصِّيغَةِ وَالشَّرْحِ لَا مِنْ نُسْخَةٍ مَشْكُولَةٍ", "the mīm of «مُفَدَّمِ» (v. 38): printed with fatha; the damma comes from the pattern and the gloss, not from a vowelled witness", "«مُفَدَّمِ»in mîm'i (b. 38): fethayla basılmış; damme bir harekeli nüshadan değil, vezin kalıbından ve şerhten alınmıştır"),
]
BADI_HADD += [
 (36, "ظُلِمْتُ", "ظُلِمْتُ", "ظُلْمِي", "ظُلْمِي", "isht", False),
]

# ---- vv. 41–46 ----
NEW_GLOSS.update({
 "halil-ant": G("حَلِيل", "noun", "husband (fem. حَلِيلَة, wife) — «they share one dwelling and one bed», or «each is lawful to the other» (al-Zawzanī)", "koca (müe. حَلِيلَة, eş) — «aynı evi ve yatağı paylaşırlar» yahut «her biri ötekine helâldir» (Zevzenî)", 6, "ح ل ل"),
 "ghaniya-ant": G("غَانِيَة", "noun", "a married woman; a woman so beautiful she needs no adornment (pl. غَوَانٍ — al-Zawzanī)", "kocalı kadın; süse ihtiyaç duymayacak kadar güzel kadın (ç. غَوَانٍ — Zevzenî)", 6, "غ ن ي"),
 "mujaddal-ant": G("مُجَدَّل", "noun", "thrown down on the ground (الْجَدَالَة: the ground — al-Zawzanī)", "yere serilmiş (الْجَدَالَة: yer — Zevzenî)", 6, "ج د ل"),
 "maka-ant": G("مَكَا", "verb", "to whistle (مَكَا يَمْكُو مُكَاءً; الْمُكَاء: الصَّفِير — al-Zawzanī)", "ıslık çalmak (مَكَا يَمْكُو مُكَاءً — Zevzenî)", 6, "م ك و"),
 "farisa-ant": G("فَرِيصَة", "noun", "the flesh between flank and shoulder that quivers in fear", "korkuda titreyen, böğürle omuz arasındaki et", 6, "ف ر ص"),
 "alam-harelip-ant": G("أَعْلَم", "noun", "with a split upper lip, hare-lipped (الْعَلَم: the split in the upper lip — al-Zawzanī)", "üst dudağı yarık (الْعَلَم: üst dudaktaki yarık — Zevzenî)", 6, "ع ل م"),
 "tana-ant": G("طَعْنَة", "noun", "a thrust, a stab (with a spear)", "(mızrakla) darbe, saplama", 5, "ط ع ن"),
 "rashash-ant": G("رَشَاش", "noun", "spray, what is sprinkled (of blood)", "serpinti, saçıntı (kan)", 6, "ر ش ش"),
 "nafidha-ant": G("نَافِذَة", "noun", "piercing right through (a thrust that passes through)", "delip geçen (darbe)", 5, "ن ف ذ"),
 "andam-ant": G("عَنْدَم", "noun", "dragon's blood (a red resin); or brazil-wood, or the red anemone (al-Zawzanī)", "ejder kanı (kırmızı reçine); yahut bakkam ağacı ya da gelincik (Zevzenî)", 6),
 "ibna-ant": G("ابْنَة", "noun", "daughter (= بِنْت)", "kız evlat (= بِنْت)", 4, "ب ن ي"),
 "zala-ant": G("زَالَ", "verb", "with a negation, a sister of كَانَ: لَا يَزَالُ, مَا زَالَ — never ceases to be, is still (زَالَ يَزَالُ)", "olumsuzlukla كَانَ'nin kardeşi: لَا يَزَالُ, مَا زَالَ — hâlâ …, … olmaktan geri durmaz (زَالَ يَزَالُ)", 5, "ز ي ل"),
 "rihala-ant": G("رِحَالَة", "noun", "a saddle (of leather, without wood)", "eyer (ahşapsız, deriden)", 6, "ر ح ل"),
 "sabih-ant": G("سَابِح", "noun", "swimming; (of a horse) running as though swimming, stretching out its forelegs", "yüzen; (at) ön ayaklarını uzatarak yüzer gibi koşan", 6, "س ب ح"),
 "taawara-ant": G("تَعَاوَرَ", "verb", "to take turns at a thing (Form VI; التَّعَاوُر: التَّدَاوُل — al-Zawzanī)", "bir şeyi sırayla yapmak (tefâul; Zevzenî: التَّعَاوُر: التَّدَاوُل)", 6, "ع و ر", form="VI"),
 "kamiyy-ant": G("كَمِيّ", "noun", "a champion hidden in his armour (pl. كُمَاة)", "zırhına bürünmüş yiğit (ç. كُمَاة)", 6, "ك م ي", "كُمَاة"),
 "mukallam-ant": G("مُكَلَّم", "noun", "wounded again and again (التَّكْلِيم: التَّجْرِيح — al-Zawzanī)", "tekrar tekrar yaralanmış (Zevzenî)", 6, "ك ل م"),
 "jarrada-ant": G("جَرَّدَ", "verb", "to strip, to bare; to single out, to send out alone (Form II)", "soymak, çıplak bırakmak; ayırıp yalnız göndermek (tef'îl)", 5, "ج ر د", form="II"),
 "tian-ant": G("طِعَان", "noun", "spear-thrusting, fighting with spears (masdar of طَاعَنَ)", "mızraklaşma, mızrakla dövüş (طَاعَنَ'nin masdarı)", 6, "ط ع ن"),
 "hasid-ant": G("حَصِد", "noun", "firm, tightly made (حَصِدَ الشَّيْءُ: اسْتَحْكَمَ — al-Zawzanī)", "sağlam, sıkı yapılmış (Zevzenî)", 6, "ح ص د"),
 "aramram-ant": G("عَرَمْرَم", "noun", "numerous, vast (of an army — al-Zawzanī)", "çok kalabalık (ordu — Zevzenî)", 6, "ع ر م"),
 "waqia-ant": G("وَقِيعَة", "noun", "a battle, an encounter (= وَقْعَة; pl. وَقَائِع — al-Zawzanī)", "savaş, çarpışma (= وَقْعَة; ç. وَقَائِع — Zevzenî)", 6, "و ق ع"),
})
NEW_VERBS.update({
 "maka-ant": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "مَكَ", "مْك", "u", "اُمْك", "مُكَاء", "مَاكٍ", None, None, None, "مَكَا يَمْكُو مُكَاءً: صَفَرَ."),
 "zala-ant": _sg.hollow1("samia", "أَجْوَفُ يَائِيٌّ", "زَال", "زِل", "زَال", "زَل", "زَال", "زَل", "زَيْل", "زَائِل", None, None, None, "النَّاقِصَةُ مِنْ أَخَوَاتِ كَانَ لَا تَعْمَلُ إِلَّا بَعْدَ نَفْيٍ أَوْ شِبْهِهِ: مَا زَالَ، لَا يَزَالُ؛ وَلَا يُسْتَعْمَلُ مِنْهَا أَمْرٌ وَلَا مَصْدَرٌ، وَالْجَدْوَلُ عَلَى قِيَاسِ الْبَابِ."),
 "taawara-ant": _dv(_sg.B6, _sg.W6, "َ", "تَعَاوَر", "تَعَاوَر", "تَعَاوَر", "تَعَاوُر", "مُتَعَاوِر"),
 "jarrada-ant": _dv(_sg.B2, _sg.W2, "ُ", "جَرَّد", "جَرِّد", "جَرِّد", "تَجْرِيد", "مُجَرِّد", "مُجَرَّد", "جُرِّدَ", "يُجَرَّدُ"),
})
TAILOR.update({
 "malik-name": ("Mālik — a man's name; in this ode, ʿAbla's father", "Mâlik — erkek adı; bu kasidede Able'nin babası"),
 "khayl": ("horses (a collective); by majaz, horsemen", "atlar (cins ismi); mecâzen süvariler"),
})

# ---- vv. 47–52 ----
NEW_GLOSS.update({
 "mudajjaj-ant": G("مُدَجَّج", "noun", "fully armed (also مُدَجِّج — al-Zawzanī)", "tepeden tırnağa silahlı (مُدَجِّج de denir — Zevzenî)", 6, "د ج ج"),
 "nizal-ant": G("نِزَال", "noun", "single combat, meeting a foe on foot (masdar of نَازَلَ)", "teke tek vuruşma, düşmanla yaya karşılaşma (نَازَلَ'nin masdarı)", 6, "ن ز ل"),
 "mumin-ant": G("مُمْعِن", "noun", "going far in a thing, hastening in it (الْإِمْعَان — al-Zawzanī)", "bir işte ileri giden, acele eden (Zevzenî)", 6, "م ع ن"),
 "mustaslim-ant": G("مُسْتَسْلِم", "noun", "yielding, submitting (الِاسْتِسْلَام: الِانْقِيَاد — al-Zawzanī)", "teslim olan, boyun eğen (Zevzenî)", 6, "س ل م"),
 "muthaqqaf-ant": G("مُثَقَّف", "noun", "straightened (of a spear-shaft, set right with the ثِقَاف); a spear", "düzeltilmiş (mızrak sapı); mızrak", 6, "ث ق ف"),
 "sadq-ant": G("صَدْق", "noun", "hard, firm («الصَّدْقُ: الصُّلْبُ» — al-Zawzanī); صَدْقُ الْكُعُوبِ: hard of joint", "sert, sağlam (Zevzenî); صَدْقُ الْكُعُوبِ: boğumları sert", 6, "ص د ق"),
 "kab-ant": G("كَعْب", "noun", "a knot, a joint of a spear-shaft (pl. كُعُوب); the ankle-bone", "mızrak sapının boğumu (ç. كُعُوب); topuk kemiği", 6, "ك ع ب", "كُعُوب"),
 "muqawwam-ant": G("مُقَوَّم", "noun", "set straight, made true (passive participle of قَوَّمَ)", "doğrultulmuş (قَوَّمَ'nin ism-i mef'ûlü)", 6, "ق و م"),
 "muharram-ant": G("مُحَرَّم", "noun", "forbidden, made inviolable", "haram kılınmış, dokunulmaz", 5, "ح ر م"),
 "jazara-ant": G("جَزَرَة", "noun", "a sheep set aside for slaughter (pl. جَزَر — al-Zawzanī)", "kesilmek için ayrılmış koyun (ç. جَزَر — Zevzenî)", 6, "ج ز ر", "جَزَر"),
 "nasha-ant": G("نَاشَ", "verb", "to reach for, to take hold of (نَاشَ يَنُوشُ نَوْشًا — al-Zawzanī)", "uzanıp almak, yakalamak (نَاشَ يَنُوشُ — Zevzenî)", 6, "ن و ش"),
 "qadima-ant": G("قَضَمَ", "verb", "to bite, to eat with the front teeth (الْقَضْم — al-Zawzanī)", "ısırmak, ön dişlerle yemek (Zevzenî)", 6, "ق ض م"),
 "mishakk-ant": G("مِشَكّ", "noun", "a coat of mail whose rings are joined; its rivets; or a man fully armed (al-Zawzanī)", "halkaları birbirine geçirilmiş zırh; perçinleri; yahut silahı tam adam (Zevzenî)", 6, "ش ك ك"),
 "hataka-ant": G("هَتَكَ", "verb", "to rend, to tear open (هَتَكَ يَهْتِكُ)", "yırtmak, yarıp açmak (هَتَكَ يَهْتِكُ)", 6, "ه ت ك"),
 "hamin-ant": G("حَامٍ", "noun", "a defender, one who guards (active participle of حَمَى; الْحَامِي with the article)", "koruyan, savunan (حَمَى'nin ism-i fâili; harf-i tarifle الْحَامِي)", 5, "ح م ي"),
 "mulim-ant": G("مُعْلِم", "noun", "one who marks himself with a sign in battle (with kasra; with fatha, مُعْلَم: one pointed out — al-Zawzanī)", "savaşta kendini bir işaretle belirleyen (kesreyle; fethayla مُعْلَم: kendisine işaret edilen — Zevzenî)", 6, "ع ل م"),
 "rabidh-ant": G("رَبِذ", "noun", "quick, light of hand («الرَّبِذُ: السَّرِيعُ» — al-Zawzanī)", "çabuk, eli hafif (Zevzenî)", 6, "ر ب ذ"),
 "qidh-ant": G("قِدْح", "noun", "an arrow of the game of maysir (pl. قِدَاح)", "meysir kumarının oku (ç. قِدَاح)", 6, "ق د ح", "قِدَاح"),
 "shata-ant": G("شَتَا", "verb", "to enter winter, to pass the winter (شَتَا يَشْتُو شَتْوًا — al-Zawzanī)", "kışa girmek, kışı geçirmek (شَتَا يَشْتُو — Zevzenî)", 6, "ش ت و"),
 "hattak-ant": G("هَتَّاك", "noun", "one who often tears down (an intensive form of هَاتِك)", "çokça yırtan, indiren (هَاتِك'in mübalağa sîgası)", 6, "ه ت ك"),
 "mulawwam-ant": G("مُلَوَّم", "noun", "blamed time after time (al-Zawzanī)", "defalarca kınanan (Zevzenî)", 6, "ل و م"),
})
NEW_VERBS.update({
 "nasha-ant": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "نَاش", "نُش", "نُوش", "نُش", "نُوش", "نُش", "نَوْش", "نَائِش", None, None, None, _sg.HOLLOW_NOTE.format(ex="نُشْتَ")),
 "qadima-ant": _sg1("daraba", "قَضَم", "قْضِم", "اِقْضِم", "قَضْم", "قَاضِم", "مَقْضُوم", "قُضِمَ", "يُقْضَمُ"),
 "hataka-ant": _sg1("daraba", "هَتَك", "هْتِك", "اِهْتِك", "هَتْك", "هَاتِك", "مَهْتُوك", "هُتِكَ", "يُهْتَكُ"),
 "shata-ant": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "شَتَ", "شْت", "u", "اُشْت", "شَتْو", "شَاتٍ", None, None, None, "شَتَا يَشْتُو: دَخَلَ فِي الشِّتَاءِ."),
})
TAILOR.update({
 "shakka": ("to string through, to pierce (الشَّكّ: الِانْتِظَام — al-Zawzanī); to doubt", "dizmek, delip geçirmek (الشَّكّ: الِانْتِظَام — Zevzenî); şüphe etmek"),
 "haqiqa": ("what one is bound to guard and defend (al-Zawzanī); (balāgha) the literal use of a word", "korunması ve savunulması gereken şey (Zevzenî); (belâgat) hakikat"),
 "ghaya": ("the utmost end; a banner a wine-seller sets up as his sign (al-Zawzanī)", "en son uç; şarapçının işaret olarak diktiği bayrak (Zevzenî)"),
 "tajir": ("merchant, trader; (in this ode) a wine-seller (al-Zawzanī)", "tüccar; (bu kasidede) şarapçı (Zevzenî)"),
})
FLAGS += [
 (50, "ضَادُ «يَقْضِمْنَ» (ب ٥٠): طُبِعَتْ مَكْسُورَةً فَأُخِذَ الْبَابُ (قَضَمَ يَقْضِمُ) مِنْهَا؛ وَالْمَعْرُوفُ فِي الْمَعَاجِمِ «قَضِمَ يَقْضَمُ» — يَنْظُرُ فِيهِ الْعَالِمُ", "the ḍād of «يَقْضِمْنَ» (v. 50): printed with kasra, and the bāb (قَضَمَ يَقْضِمُ) is taken from it; the lexicons commonly give قَضِمَ يَقْضَمُ — for the scholar", "«يَقْضِمْنَ»in dâd'ı (b. 50): kesreyle basılmış, bâb (قَضَمَ يَقْضِمُ) ondan alınmıştır; sözlüklerde yaygın olan قَضِمَ يَقْضَمُ'dur — âlimin incelemesine"),
]

# ---- vv. 53–60 ----
NEW_GLOSS.update({
 "najidh-ant": G("نَاجِذ", "noun", "a back tooth, the hindmost molar (pl. نَوَاجِذ)", "azı dişi, en arkadaki azı (ç. نَوَاجِذ)", 6, "ن ج ذ", "نَوَاجِذ"),
 "khadaba-ant": G("خَضَبَ", "verb", "to dye, to stain (خَضَبَ يَخْضِبُ)", "boyamak, kınalamak (خَضَبَ يَخْضِبُ)", 6, "خ ض ب"),
 "izlim-ant": G("عِظْلِم", "noun", "ʿiẓlim — a plant used for dyeing (al-Zawzanī); in this edition printed عِظْلَم", "ızlim — boyamada kullanılan bir bitki (Zevzenî); bu neşirde عِظْلَم basılmıştır", 6, "ع ظ ل م"),
 "muhannad-ant": G("مُهَنَّد", "noun", "an Indian blade, a sword of Indian steel", "Hint kılıcı, Hint çeliğinden kılıç", 6, "ه ن د"),
 "safin-ant": G("صَافٍ", "noun", "pure, clear (active participle of صَفَا; الصَّافِي with the article)", "saf, duru (صَفَا'nın ism-i fâili; harf-i tarifle الصَّافِي)", 5, "ص ف و"),
 "hadida-ant": G("حَدِيدَة", "noun", "a piece of iron; the steel of a blade", "demir parçası; kılıcın çeliği", 5, "ح د د"),
 "batal-ant": G("بَطَل", "noun", "a hero, a champion (pl. أَبْطَال)", "kahraman, yiğit (ç. أَبْطَال)", 5, "ب ط ل", "أَبْطَال"),
 "sarha-ant": G("سَرْحَة", "noun", "a great tree («السَّرْحَةُ: الشَّجَرَةُ الْعَظِيمَةُ» — al-Zawzanī)", "ulu ağaç (Zevzenî)", 6, "س ر ح"),
 "hadha-ant": G("حَذَا", "verb", "to shoe; حُذِيَ نَعْلًا: to be given sandals to wear (حَذَا يَحْذُو; passive يُحْذَى)", "ayakkabı giydirmek; حُذِيَ نَعْلًا: kendisine nalın giydirilmek (حَذَا يَحْذُو; meçhulü يُحْذَى)", 6, "ح ذ و"),
 "sibt-ant": G("سِبْت", "noun", "ox-hide tanned with qaraẓ, used for fine sandals (al-Zawzanī)", "karaz ile tabaklanmış sığır derisi, ince nalınlar yapılır (Zevzenî)", 6, "س ب ت"),
 "tawam-ant": G("تَوْأَم", "noun", "a twin", "ikiz", 5, "و أ م"),
 "qanas-ant": G("قَنَص", "noun", "the hunt; game", "av", 6, "ق ن ص"),
 "haruma-ant": G("حَرُمَ", "verb", "to be forbidden, unlawful (حَرُمَ يَحْرُمُ)", "haram olmak (حَرُمَ يَحْرُمُ)", 5, "ح ر م"),
 "tajassasa-ant": G("تَجَسَّسَ", "verb", "to spy out, to search out news secretly (Form V)", "gizlice araştırmak, haber toplamak (tefe''ul)", 6, "ج س س", form="V"),
 "ghirra-ant": G("غِرَّة", "noun", "heedlessness, being off one's guard («الْغِرَّةُ: الْغَفْلَةُ» — al-Zawzanī)", "gaflet, tedbirsizlik (Zevzenî)", 6, "غ ر ر"),
 "murtamin-ant": G("مُرْتَمٍ", "noun", "one who shoots, a hunter (active participle of ارْتَمَى)", "nişan alan, atan (ارْتَمَى'nin ism-i fâili)", 6, "ر م ي"),
 "jadaya-ant": G("جَدَايَة", "noun", "a gazelle's young (also جِدَايَة; pl. جَدَايَا — al-Zawzanī)", "ceylan yavrusu (جِدَايَة da denir; ç. جَدَايَا — Zevzenî)", 6, "ج د ي"),
 "rasha-ant": G("رَشَأ", "noun", "a young gazelle grown strong (al-Zawzanī)", "güçlenmiş ceylan yavrusu (Zevzenî)", 6, "ر ش أ"),
 "artham-ant": G("أَرْثَم", "noun", "with white on the upper lip and nose (al-Zawzanī); a diptote", "üst dudağında ve burnunda beyazlık olan (Zevzenî); gayr-i munsarif", 6, "ر ث م"),
})
NEW_VERBS.update({
 "khadaba-ant": _sg1("daraba", "خَضَب", "خْضِب", "اِخْضِب", "خَضْب", "خَاضِب", "مَخْضُوب", "خُضِبَ", "يُخْضَبُ"),
 "hadha-ant": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "حَذَ", "حْذ", "u", "اُحْذ", "حَذْو", "حَاذٍ", "مَحْذُوّ", "حُذِيَ", "يُحْذَى"),
 "haruma-ant": _sg1("karuma", "حَرُم", "حْرُم", "اُحْرُم", "حُرْمَة", "حَرَام"),
 "tajassasa-ant": _dv(_sg.B5, _sg.W5, "َ", "تَجَسَّس", "تَجَسَّس", "تَجَسَّس", "تَجَسُّس", "مُتَجَسِّس"),
})
TAILOR.update({
 "madd": ("extent, length — مَدَّ النَّهَارِ: the whole length of the day; (in reading) lengthening", "uzunluk — مَدَّ النَّهَارِ: gün boyunca; (kıraatte) med"),
 "jariya": ("a slave-girl, a maid; a ship (that runs on the water)", "cariye, hizmetçi kız; (suda akan) gemi"),
 "ahd": ("meeting, coming upon (عَهِدْتُهُ: لَقِيتُهُ — al-Zawzanī); a time; a covenant", "karşılaşma (Zevzenî: عَهِدْتُهُ: لَقِيتُهُ); zaman; ahit"),
 "ala-rise": ("to rise above; عَلَاهُ بِالسَّيْفِ: to fall upon him with the sword", "yükselmek; عَلَاهُ بِالسَّيْفِ: kılıçla üzerine çıkmak"),
 "shat": ("a sheep, a ewe; (in this ode) a kinaya for the woman (al-Zawzanī)", "koyun; (bu kasidede) kadından kinâye (Zevzenî)"),
})
DIV += [
 (53, "الْبَيْتُ ٥٣ «أَبْدَي» ← «أَبْدَى»: كُتِبَتِ الْأَلِفُ الْمَقْصُورَةُ يَاءً مَنْقُوطَةً، فَكُتِبَتْ عَلَى رَسْمِ الرَّفِّ", "v. 53 «أَبْدَي» → «أَبْدَى»: the alif maqṣūra was written as a dotted yāʾ; it is written in the shelf's spelling", "53. beyit «أَبْدَي» → «أَبْدَى»: elif-i maksûre noktalı yâ olarak yazılmış; rafın imlâsıyla yazılmıştır"),
 (56, "الْبَيْتُ ٥٦ «السَّبْتِ» ← «السِّبْتِ» بِكَسْرِ السِّينِ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ مَشْكُولًا فِي الصَّفْحَةِ: «تَسْتَوْعِبُ رِجْلَاهُ السِّبتَ»، وَتَفْسِيرُهُ بِالْجُلُودِ الْمَدْبُوغَةِ", "v. 56 «السَّبْتِ» → «السِّبْتِ», kasra on the sīn — witness: al-Zawzanī's own commentary, vowelled on the same page («his feet fill the السِّبت») and his gloss «tanned hides»", "56. beyit «السَّبْتِ» → «السِّبْتِ», sîn'in kesresiyle — şâhit: aynı sayfada harekeli olarak Zevzenî'nin kendi şerhi («ayakları السِّبت'i doldurur») ve «tabaklanmış deriler» açıklaması"),
]
FLAGS += [
 (54, "لَامُ «الْعِظْلَمِ» (ب ٥٤): طُبِعَتْ مَفْتُوحَةً وَالْمَعْرُوفُ «عِظْلِم» بِالْكَسْرِ؛ أُبْقِيَ مَا طُبِعَ", "the lām of «الْعِظْلَمِ» (v. 54): printed with fatha, where the word is known as «عِظْلِم» with kasra; the print is kept", "«الْعِظْلَمِ»in lâm'ı (b. 54): fethayla basılmış, bilinen ise kesreli «عِظْلِم»dir; basılan korunmuştur"),
]
BADI_HADD += [
 (57, "حَرُمَتْ", "حَرُمَتْ", "تَحْرُمِ", "تَحْرُمِ", "isht", True),
]

# ---- vv. 61–68 ----
NEW_GLOSS.update({
 "makhbatha-ant": G("مَخْبَثَة", "noun", "what makes (the soul) foul, sours it — «ingratitude turns the giver's soul away from giving» (al-Zawzanī)", "(nefsi) bulandıran, soğutan şey (Zevzenî)", 6, "خ ب ث"),
 "munim-ant": G("مُنْعِم", "noun", "one who bestows kindness, a benefactor (active participle of أَنْعَمَ)", "iyilik eden, nimet veren (أَنْعَمَ'in ism-i fâili)", 5, "ن ع م"),
 "wasat-ant": G("وَصَاة", "noun", "a charge, a last counsel (a quasi-masdar; = الْوَصِيَّة — al-Zawzanī)", "vasiyet, öğüt (ism-i masdar; = الْوَصِيَّة — Zevzenî)", 6, "و ص ي"),
 "qalasa-ant": G("قَلَصَ", "verb", "to shrink, to draw back (الْقُلُوص: التَّشَنُّج وَالْقِصَر — al-Zawzanī; قَلَصَ يَقْلِصُ)", "büzülmek, çekilmek (Zevzenî; قَلَصَ يَقْلِصُ)", 6, "ق ل ص"),
 "wadah-ant": G("وَضَح", "noun", "whiteness, brightness; وَضَحُ الْفَمِ: the teeth (al-Zawzanī)", "beyazlık, parlaklık; وَضَحُ الْفَمِ: dişler (Zevzenî)", 6, "و ض ح"),
 "hawma-ant": G("حَوْمَة", "noun", "the thick, the main mass (of battle), where it circles (al-Zawzanī)", "(savaşın) en yoğun yeri, döndüğü yer (Zevzenî)", 6, "ح و م"),
 "ishtaka-ant": G("اشْتَكَى", "verb", "to complain of (Form VIII, naqis)", "şikâyet etmek (ifti'âl, nâkıs)", 5, "ش ك و", form="VIII"),
 "ghamra-ant": G("غَمْرَة", "noun", "a flood; (pl. غَمَرَات) the overwhelming hardships of battle (al-Zawzanī)", "taşkın; (ç. غَمَرَات) savaşın boğucu şiddetleri (Zevzenî)", 6, "غ م ر", "غَمَرَات"),
 "taghamghum-ant": G("تَغَمْغُم", "noun", "an inarticulate roar, a din from which nothing can be made out (al-Zawzanī)", "anlaşılmaz uğultu, gürültü (Zevzenî)", 6, "غ م م"),
 "khama-ant": G("خَامَ", "verb", "to shrink back in cowardice («الْخَيْمُ: الْجُبْنُ» — al-Zawzanī; خَامَ يَخِيمُ)", "korkup geri çekilmek (Zevzenî; خَامَ يَخِيمُ)", 6, "خ ي م"),
 "tadayaqa-ant": G("تَضَايَقَ", "verb", "to grow narrow, to be cramped (Form VI)", "daralmak, sıkışmak (tefâul)", 6, "ض ي ق", form="VI"),
 "muqdam-ant": G("مُقْدَم", "noun", "the place of pressing forward (noun of place of أَقْدَمَ — al-Zawzanī)", "ileri atılma yeri (أَقْدَمَ'den ism-i mekân — Zevzenî)", 6, "ق د م"),
 "tadhamara-ant": G("تَذَامَرَ", "verb", "to urge one another on to fight (Form VI of الذَّمْر — al-Zawzanī)", "birbirini savaşa kışkırtmak (الذَّمْر'den tefâul — Zevzenî)", 6, "ذ م ر", form="VI"),
 "karra-ant": G("كَرَّ", "verb", "to wheel round and charge again (كَرَّ يَكُرُّ)", "dönüp yeniden saldırmak (كَرَّ يَكُرُّ)", 6, "ك ر ر"),
 "mudhammam-ant": G("مُذَمَّم", "noun", "much blamed (غَيْرُ مُذَمَّمٍ: «praised in the fight, not blamed» — al-Zawzanī)", "çok kınanan (غَيْرُ مُذَمَّمٍ: «savaşta övülen, kınanmayan» — Zevzenî)", 6, "ذ م م"),
 "shatan-ant": G("شَطَن", "noun", "a well-rope (pl. أَشْطَان — al-Zawzanī)", "kuyu ipi (ç. أَشْطَان — Zevzenî)", 6, "ش ط ن", "أَشْطَان"),
 "laban-ant": G("لَبَان", "noun", "the breast, the chest (of a horse) («اللَّبَانُ: الصَّدْرُ» — al-Zawzanī)", "(atın) göğsü (Zevzenî)", 6, "ل ب ن"),
 "thughra-ant": G("ثُغْرَة", "noun", "the hollow at the top of the throat (pl. ثُغَر — al-Zawzanī)", "gerdanın üstündeki çukur (ç. ثُغَر — Zevzenî)", 6, "ث غ ر"),
 "tasarbala-ant": G("تَسَرْبَلَ", "verb", "to put on a shirt (سِرْبَال); to be clothed, covered (quadriliteral, تَفَعْلَلَ)", "gömlek (سِرْبَال) giymek; bürünmek (rubâî, tefa'lül)", 6, "س ر ب ل"),
 "azwarra-ant": G("ازْوَرَّ", "verb", "to swerve, to lean aside (Form IX; الِازْوِرَار: الْمَيْل — al-Zawzanī)", "yana kaymak, meyletmek (if'ilâl; Zevzenî: الِازْوِرَار: meyil)", 6, "ز و ر", form="IX"),
 "waq-ant": G("وَقْع", "noun", "falling, the fall of a blow (masdar of وَقَعَ)", "düşme, darbenin inişi (وَقَعَ'nin masdarı)", 5, "و ق ع"),
 "tahamhum-ant": G("تَحَمْحُم", "noun", "a low, plaintive whinny (al-Zawzanī)", "inilti benzeri hafif kişneme (Zevzenî)", 6, "ح م ح م"),
})
NEW_VERBS.update({
 "qalasa-ant": _sg1("daraba", "قَلَص", "قْلِص", "اِقْلِص", "قُلُوص", "قَالِص"),
 "ishtaka-ant": _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِشْتَكَ", "شْتَك", "i", "اِشْتَك", "اِشْتِكَاء", "مُشْتَكٍ (الْمُشْتَكِي)"),
 "khama-ant": _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "خَام", "خِم", "خِيم", "خِم", "خِيم", "خِم", "خَيْم", "خَائِم", None, None, None, _sg.HOLLOW_NOTE.format(ex="لَمْ أَخِمْ")),
 "tadayaqa-ant": _dv(_sg.B6, _sg.W6, "َ", "تَضَايَق", "تَضَايَق", "تَضَايَق", "تَضَايُق", "مُتَضَايِق"),
 "tadhamara-ant": _dv(_sg.B6, _sg.W6, "َ", "تَذَامَر", "تَذَامَر", "تَذَامَر", "تَذَامُر", "مُتَذَامِر"),
 "karra-ant": _dbl("nasara", "ك", "ر", "كَرّ", "كَارّ"),
 "tasarbala-ant": _sg.derived("بَابُ التَّفَعْلُلِ (مَزِيدُ الرُّبَاعِيِّ): تَفَعْلَلَ يَتَفَعْلَلُ", "تَفَعْلَلَ يَتَفَعْلَلُ", "َ", "تَسَرْبَل", "تَسَرْبَل", "تَسَرْبَل", "تَسَرْبُل", "مُتَسَرْبِل"),
 "azwarra-ant": _sg.nfc({"bab": "الْبَابُ التَّاسِعُ اِفْعَلَّ — مُضَاعَفٌ", "wazn": "اِفْعَلَّ يَفْعَلُّ", "masdar": "اِزْوِرَار", "ismFail": "مُزْوَرّ",
  "mazi": ["اِزْوَرَّ", "اِزْوَرَّا", "اِزْوَرُّوا", "اِزْوَرَّتْ", "اِزْوَرَّتَا", "اِزْوَرَرْنَ", "اِزْوَرَرْتَ", "اِزْوَرَرْتُمَا", "اِزْوَرَرْتُمْ", "اِزْوَرَرْتِ", "اِزْوَرَرْتُمَا", "اِزْوَرَرْتُنَّ", "اِزْوَرَرْتُ", "اِزْوَرَرْنَا"],
  "mudari": ["يَزْوَرُّ", "يَزْوَرَّانِ", "يَزْوَرُّونَ", "تَزْوَرُّ", "تَزْوَرَّانِ", "يَزْوَرِرْنَ", "تَزْوَرُّ", "تَزْوَرَّانِ", "تَزْوَرُّونَ", "تَزْوَرِّينَ", "تَزْوَرَّانِ", "تَزْوَرِرْنَ", "أَزْوَرُّ", "نَزْوَرُّ"],
  "amr": ["اِزْوَرَّ", "اِزْوَرَّا", "اِزْوَرُّوا", "اِزْوَرِّي", "اِزْوَرَّا", "اِزْوَرِرْنَ"], "mansub": "يَزْوَرَّ", "majzum": "يَزْوَرَّ", "majzum2": "تَزْوَرَّ",
  "note": "اِزْوَرَّ يَزْوَرُّ اِزْوِرَارًا: مَالَ — مِنَ الْبَابِ التَّاسِعِ لِلْأَلْوَانِ وَالْعُيُوبِ، لَازِمٌ."}),
})
TAILOR.update({
 "jam": ("gathering; a host, a gathered company (masdar of جَمَعَ); the plural", "toplama; toplanmış topluluk, ordu (جَمَعَ'nin masdarı); cem'"),
 "rama": ("to throw, to shoot; رَمَاهُمْ بِـ: to charge them with (al-Zawzanī: «أَرْمِي الْأَعْدَاءَ بِنَحْرِ فَرَسِي»)", "atmak; رَمَاهُمْ بِـ: onlara … ile saldırmak (Zevzenî)"),
})
DIV += [
 (62, "الْبَيْتُ ٦٢ «عَنِ وَضَحِ» ← «عَنْ وَضَحِ» بِسُكُونِ النُّونِ، وَالشَّاهِدُ الْوَزْنُ (لَا يَسْتَقِيمُ الْكَامِلُ بِالْكَسْرِ)", "v. 62 «عَنِ وَضَحِ» → «عَنْ وَضَحِ», the nūn quiescent — witness: the metre (al-kāmil does not scan with the kasra)", "62. beyit «عَنِ وَضَحِ» → «عَنْ وَضَحِ», nûn sâkin — şâhit: vezin (kâmil kesreyle yürümez)"),
 (63, "الْبَيْتُ ٦٣ «الْحَرِبِ» ← «الْحَرْبِ» بِسُكُونِ الرَّاءِ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ لِلْكَلِمَةِ نَفْسِهَا: «حَوْمَةُ الْحَرْبِ: مُعْظَمُهَا، وَهِيَ حَيْثُ تَحُومُ الْحَرْبُ أَيْ تَدُورُ»", "v. 63 «الْحَرِبِ» → «الْحَرْبِ», the rāʾ quiescent — witness: al-Zawzanī's gloss of this very word («the thick of the battle, where the battle circles»)", "63. beyit «الْحَرِبِ» → «الْحَرْبِ», râ sâkin — şâhit: Zevzenî'nin bu kelimeyi açıklaması («savaşın ortası, savaşın döndüğü yer»)"),
 (65, "الْبَيْتُ ٦٥ «جَمْعَهُمْ» ← «جَمْعُهُمْ» بِالرَّفْعِ فَاعِلًا لِـ«أَقْبَلَ»، وَالشَّاهِدُ إِعْرَابُ الدُّرَّةِ («جَمْعُهُمْ: فَاعِلٌ») وَشَرْحُ الزَّوْزَنِيِّ «لَمَّا رَأَيْتُ جَمْعَ الْأَعْدَاءِ قَدْ أَقْبَلُوا»", "v. 65 «جَمْعَهُمْ» → «جَمْعُهُمْ», in raf' as the doer of «أَقْبَلَ» — witness: al-Durra's iʿrāb («جمعهم: the doer») and al-Zawzanī's paraphrase «when I saw the enemy's host advance»", "65. beyit «جَمْعَهُمْ» → «جَمْعُهُمْ», «أَقْبَلَ»in fâili olarak merfû — şâhit: Dürre'nin i'râbı («جمعهم: fâil») ve Zevzenî'nin şerhi «düşman topluluğunun ilerlediğini görünce»"),
]
FLAGS += [
 (63, "رَاءُ «الْحَرْبِ» (ب ٦٣): طُبِعَتْ مَكْسُورَةً، وَالْوَزْنُ يَحْتَمِلُ الْوَجْهَيْنِ؛ السُّكُونُ مِنْ شَرْحِ الْكَلِمَةِ", "the rāʾ of «الْحَرْبِ» (v. 63): printed with kasra, and the metre allows both; the sukūn comes from the gloss of the word", "«الْحَرْبِ»in râ'sı (b. 63): kesreyle basılmış, vezin ikisine de elverir; sükûn kelimenin şerhinden alınmıştır"),
]

# ---- vv. 69–75 ----
NEW_GLOSS.update({
 "muhawara-ant": G("مُحَاوَرَة", "noun", "talking together, conversation (mufā'ala; = الْخِطَاب — al-Zawzanī)", "karşılıklı konuşma (müfâale; = الْخِطَاب — Zevzenî)", 6, "ح و ر"),
 "mukallim-ant": G("مُكَلِّم", "noun", "one who speaks to another (active participle of كَلَّمَ)", "biriyle konuşan (كَلَّمَ'nin ism-i fâili)", 5, "ك ل م"),
 "adhhaba-ant": G("أَذْهَبَ", "verb", "to take away, to remove (Form IV)", "gidermek, alıp götürmek (if'âl)", 5, "ذ ه ب", form="IV"),
 "suqm-ant": G("سُقْم", "noun", "sickness (also سَقَم)", "hastalık (سَقَم da denir)", 5, "س ق م"),
 "wayk-ant": G("وَيْك", "noun", "an exclamation: «woe to you!», «look!» — a verbal noun of wonder; al-Zawzanī renders it وَيْلَكَ", "ünlem: «vay sana!», «bak!» — hayret bildiren ism-i fiil; Zevzenî onu وَيْلَكَ diye açıklar", 6),
 "iqtahama-ant": G("اقْتَحَمَ", "verb", "to plunge into, to rush headlong into (Form VIII)", "dalmak, kendini atmak (ifti'âl)", 6, "ق ح م", form="VIII"),
 "khabar-soft-ant": G("خَبَار", "noun", "soft ground in which the legs sink («الْخَبَارُ: الْأَرْضُ اللَّيِّنَةُ» — al-Zawzanī)", "ayakların battığı yumuşak arazi (Zevzenî)", 6, "خ ب ر"),
 "abis-ant": G("عَابِس", "noun", "scowling, frowning (pl. عَوَابِس)", "suratı asık, çehresi buruşuk (ç. عَوَابِس)", 6, "ع ب س", "عَوَابِس"),
 "ajrad-ant": G("أَجْرَد", "noun", "(of a horse) short-haired, smooth-coated — a mark of breeding; a diptote", "(at) kısa tüylü — soyluluk alâmeti; gayr-i munsarif", 6, "ج ر د"),
 "mushayi-ant": G("مُشَايِع", "noun", "one who backs and helps (الْمُشَايَعَة: الْمُعَاوَنَة — al-Zawzanī)", "destekleyen, yardım eden (Zevzenî)", 6, "ش ي ع"),
 "hafaza-ant": G("حَفَزَ", "verb", "to push on, to urge forward («الْحَفْزُ: الدَّفْعُ» — al-Zawzanī; حَفَزَ يَحْفِزُ)", "ileri itmek, sürmek (Zevzenî; حَفَزَ يَحْفِزُ)", 6, "ح ف ز"),
 "daira-ant": G("دَائِرَة", "noun", "a turn of fortune, a calamity (al-Zawzanī: it turns from good to ill; then used of the hateful only)", "felek dönüşü, felaket (Zevzenî: iyiden kötüye döner; sonra yalnız hoşa gitmeyen için)", 6, "د و ر"),
 "shatim-ant": G("شَاتِم", "noun", "one who reviles (active participle of شَتَمَ)", "söven (شَتَمَ'nin ism-i fâili)", 5, "ش ت م"),
 "nadhir-ant": G("نَاذِر", "noun", "one who vows (active participle of نَذَرَ)", "adak adayan (نَذَرَ'nin ism-i fâili)", 5, "ن ذ ر"),
 "nasr-bird-ant": G("نَسْر", "noun", "a vulture (pl. نُسُور)", "akbaba (ç. نُسُور)", 5, "ن س ر"),
})
NEW_VERBS.update({
 "adhhaba-ant": _dv(_sg.B4, _sg.W4, "ُ", "أَذْهَب", "ذْهِب", "أَذْهِب", "إِذْهَاب", "مُذْهِب", "مُذْهَب", "أُذْهِبَ", "يُذْهَبُ"),
 "iqtahama-ant": _dv(_sg.B8, _sg.W8, "َ", "اِقْتَحَم", "قْتَحِم", "اِقْتَحِم", "اِقْتِحَام", "مُقْتَحِم"),
 "hafaza-ant": _sg1("daraba", "حَفَز", "حْفِز", "اِحْفِز", "حَفْز", "حَافِز", "مَحْفُوز", "حُفِزَ", "يُحْفَزُ"),
})
TAILOR.update({
 "dara-turn": ("to turn, to revolve; (of fortune) to come round upon (دَارَ يَدُورُ)", "dönmek; (felek) birinin başına dönmek (دَارَ يَدُورُ)"),
 "lubb": ("the core; the mind, the understanding (pl. أَلْبَاب)", "öz; akıl, anlayış (ç. أَلْبَاب)"),
})
DIV += [
 (72, "الْبَيْتُ ٧٢ «لُبْتِي» ← «لُبِّي»، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ «وَيُعَاوِنُنِي عَلَى أَفْعَالِي عَقْلِي» — وَاللُّبُّ الْعَقْلُ — وَلَيْسَ «لُبْتِي» بِكَلِمَةٍ؛ وَالدُّرَّةُ يَقْرَأُ «قَلْبِي»", "v. 72 «لُبْتِي» → «لُبِّي» — witness: al-Zawzanī's gloss «my mind helps me in what I do» (اللُّبّ is the mind); «لُبْتِي» is no word; al-Durra reads «قَلْبِي»", "72. beyit «لُبْتِي» → «لُبِّي» — şâhit: Zevzenî'nin «aklım işlerimde bana yardım eder» şerhi (اللُّبّ akıldır); «لُبْتِي» bir kelime değildir; Dürre «قَلْبِي» okur"),
 (73, "الْبَيْتُ ٧٣ «بَأَنْ» ← «بِأَنْ» بِكَسْرِ الْبَاءِ، وَالشَّاهِدُ إِعْرَابُ الدُّرَّةِ (الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ)؛ وَ«تَدُر» ← «تَدُرْ» بِالسُّكُونِ، وَالشَّاهِدُ الْوَزْنُ وَالْجَزْمُ بِـ«لَمْ»", "v. 73 «بَأَنْ» → «بِأَنْ», kasra on the bāʾ — witness: al-Durra's iʿrāb (an added jarr letter); and «تَدُر» → «تَدُرْ» with sukūn — witness: the metre and the jazm by لَمْ", "73. beyit «بَأَنْ» → «بِأَنْ», bâ'nın kesresiyle — şâhit: Dürre'nin i'râbı (zâid cer harfi); «تَدُر» → «تَدُرْ», sükûnla — şâhit: vezin ve «لَمْ» ile cezm"),
]
FLAGS += [
 (74, "«لَمَ الْقَهُمَا» (ب ٧٤): أُبْقِيَ رَسْمُ النَّشْرَةِ وَوُجِّهَ بِنَقْلِ فَتْحَةِ هَمْزَةِ «أَلْقَهُمَا» إِلَى مِيمِ «لَمْ» — وَالْوَزْنُ يُوَافِقُهُ؛ وَالدُّرَّةُ يَكْتُبُ «لَمْ أَلْقَهُمَا»", "«لَمَ الْقَهُمَا» (v. 74): the edition's spelling is kept and read as the fatha of the hamza of «أَلْقَهُمَا» moved onto the mīm of لَمْ — the metre agrees; al-Durra writes «لَمْ أَلْقَهُمَا»", "«لَمَ الْقَهُمَا» (b. 74): neşrin imlâsı korunmuş, «أَلْقَهُمَا»nın hemzesinin fethası «لَمْ»in mîm'ine nakledilmiş olarak okunmuştur — vezin buna uyar; Dürre «لَمْ أَلْقَهُمَا» yazar"),
]
BADI_HADD += [
 (69, "الْكَلَامَ", "الْكَلَامَ", "مُكَلِّمِي", "مُكَلِّمِي", "isht", False),
 (71, "شَيْظَمَةٍ", "شَيْظَمَةٍ", "شَيْظَمِ", "شَيْظَمِ", "isht", False),
 (73, "تَدُرْ", "تَدُرْ", "دَائِرَةٌ", "دَائِرَةٌ", "isht", False),
 (74, "الشَّاتِمَيْ", "الشَّاتِمَيْ", "أَشْتِمْهُمَا", "أَشْتِمْهُمَا", "isht", False),
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
    + ("وَخُولِفَ الْمَطْبُوعُ فِي هٰذِهِ الْمَوَاضِعِ — سَهْوُ طِبَاعَةٍ يَشْهَدُ عَلَيْهِ شَاهِدٌ، أَوْ رَسْمٌ أَوْ تَقْسِيمٌ لِلْبَيْتِ ذُكِرَ وَجْهُهُ: " + _div_ar + ". " if _div else "")
    + ("وَمِمَّا ضَبَطَهُ الْمُحَرِّرُ وَلَمْ يَقْطَعْ بِهِ وَزْنٌ وَلَا شَرْحٌ: " + "، وَ".join(f[1] for f in _flg) + ". " if _flg else "")
    + "إِعْرَابُ كُلِّ كَلِمَةٍ بِعِبَارَةِ هٰذَا الرَّفِّ، وَقَدْ رُوجِعَ إِعْرَابُ الْأَبْيَاتِ عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ: إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهَ الدُّرَّة (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م؛ الْكِتَابُ ١٥١٠١٧، ج ٢ ص ١٣٥–٢٦٤) — وَهُوَ يَرْوِي الْقَصِيدَةَ بِعَدٍّ آخَرَ وَيَزِيدُ أَبْيَاتًا لَيْسَتْ عِنْدَ الزَّوْزَنِيِّ — وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ: مَا نَصَّ عَلَيْهِ أَوْ وَصَفَهُ الزَّوْزَنِيُّ أَوِ الدُّرَّةُ ذُكِرَ مَنْسُوبًا إِلَيْهِ، وَمَا كَانَ بِحَدِّ التَّلْخِيصِ وَحْدَهُ — وَلَمْ يُسَمِّهِ الشَّارِحَانِ — قِيلَ فِيهِ: «عَلَى حَدِّ التَّلْخِيصِ»؛ وَلَمْ يُوجَدْ فِي مَتْنِ التَّلْخِيصِ اسْتِشْهَادٌ بِبَيْتٍ مِنْ هٰذِهِ الْقَصِيدَةِ. وَالتَّرْجَمَةُ مَعْنَى الْبَيْتِ عَلَى شَرْحِ الزَّوْزَنِيِّ، لَا شِعْرٌ. وَتَقْسِيمُ الْفُصُولِ وَعَنَاوِينُهَا وَعَلَامَاتُ التَّرْقِيمِ مِنَ الْمُحَرِّرِ، وَالنَّصُّ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.")
ATTR_EN = ("The RECEIVED text, word for word. Chapter 1 is the khabar of ʿAntara ibn Shaddād al-ʿAbsī from Ibn Qutayba (d. 276 AH), al-Shiʿr wa-l-shuʿarāʾ, in the edition al-Maktaba al-Shāmila names «Dār al-Ḥadīth, Cairo, 1423 AH» (book 23785), vol. 1 pp. 244–245, § 419 in full: one contiguous span with nothing cut from inside it; only the paragraph number, the editor's footnote marks and his brackets round «يَدِي» are left out. The rest of the entry — before it his lineage, how his father came to acknowledge him, and «the ravens of the Arabs»; after it the war of Dāḥis and his death — is not taken. "
    + _scope[1] + " — in the metre al-kāmil, rhyming on a mīm with kasra, the rhyme unbound — in the recension, order and verse-count of al-Zawzanī (d. 486 AH), Sharḥ al-Muʿallaqāt al-sabʿ, the edition Shamela names «Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423 AH / 2002 CE» (book 11253), pp. 245–265: " + _ch_en + ". Each verse is one sentence, and «•» marks the end of its first hemistich." + _rest[1] + " "
    "The vowelling has two layers. What the edition vowels is kept, in this shelf's spelling; what it leaves bare — every short vowel of Ibn Qutayba's khabar (the edition prints only its shaddas) and many letters of the verses — is supplied editorially, as the metre and the commentary require. "
    + ("The edition's print is departed from in these places — a slip of the press with a witness against it, or a spelling or a division of the verse whose reason is given: " + _div_en + ". " if _div else "")
    + ("Editorial vowels that neither metre nor commentary settles: " + ", ".join(f[2] for f in _flg) + ". " if _flg else "")
    + "Every token's iʿrāb is written in this shelf's own wording; that of the verses was checked against Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409 AH / 1989 CE; book 151017, vol. 2 pp. 135–264), who counts the ode differently and has verses al-Zawzanī does not; where he offers two readings the first is given and the second mentioned. The figures of balāgha are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ: one that al-Zawzanī or al-Durra names or describes is given with his name; one that rests on the Talkhīṣ's definition alone, which neither commentator names, says so in its line («by the Talkhīṣ's definition»). No verse of this ode was found cited in the matn of the Talkhīṣ. The translations give each verse's plain meaning after al-Zawzanī; they are not verse. The division into chapters, their titles and the punctuation are editorial. Pending scholarly review.")
ATTR_TR = ("Metin LAFZIYLA aktarılmıştır. 1. bölüm, Antere b. Şeddâd el-Absî'nin haberidir: İbn Kuteybe (ö. 276 h.), eş-Şi'r ve'ş-şuarâ, el-Mektebetü'ş-Şâmile'nin «Dâru'l-Hadîs, Kahire, 1423 h.» diye andığı baskı (kitap 23785), c. 1 s. 244–245, § 419'un tamamı: içinden hiçbir şey çıkarılmamış tek ve kesintisiz bir parça; yalnızca paragraf numarası, muhakkikin dipnot işaretleri ve «يَدِي» kelimesinin etrafındaki parantezi alınmamıştır. Tercemenin geri kalanı — öncesinde nesebi, babasının onu oğul olarak tanıması ve «Arapların kargaları»; sonrasında Dâhis savaşı ve ölümü — alınmamıştır. "
    + _scope[2] + " — kaside kâmil bahrindendir, revîsi kesreli mîm, kâfiyesi mutlaktır — Zevzenî'nin (ö. 486 h.) Şerhu'l-Muallakâti's-seb'indeki rivayeti, sırası ve beyit sayımıyla; Şâmile'nin «Dâru İhyâi't-Türâsi'l-Arabî, 1423 h. / 2002 m.» diye andığı baskı (kitap 11253), s. 245–265: " + _ch_tr + ". Her beyit tek cümledir; «•» ilk mısraın sonunu gösterir." + _rest[2] + " "
    "Harekeleme iki katmandır: baskının harekelediği yerler bu rafın imlâsıyla korunmuş; harekesiz bıraktığı yerler — İbn Kuteybe haberinin bütün kısa harekeleri (baskı yalnızca şeddeleri basar) ve beyitlerdeki pek çok harf — vezin ve şerhin gerektirdiği şekilde editörce harekelenmiştir. "
    + ("Baskıdan şu yerlerde ayrılınmıştır — aleyhine şâhit bulunan dizgi sehvi, ya da gerekçesi belirtilen bir imlâ veya beyit bölümü: " + _div_tr + ". " if _div else "")
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
