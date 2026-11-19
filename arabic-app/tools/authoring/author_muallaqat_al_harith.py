"""Author content/samples/muallaqat-al-harith — «مُعَلَّقَةُ الْحَارِثِ بْنِ حِلِّزَةَ», a RECEIVED text at Level 6 (Master).

Chapter 1 is the poet's khabar, VERBATIM from Ibn Qutayba, «الشعر والشعراء» (Dār al-Ḥadīth, Cairo 1423, 1/193, § 319;
shamela.ws/book/23785/186): one contiguous span, the whole of § 319. The chapters after it are the Muʿallaqa in al-Zawzanī's
text, order and count («شرح المعلقات السبع», shamela.ws/book/11253/290–307, pp. 269–286): 82 verses, cut by PLAN below.
A verse is ONE sentence; the last token of its first hemistich carries punctAfter "•". The iʿrāb of every token was checked
against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال» (shamela.ws/book/151017/448–546 — he gives the ode in another order
and count, 86 verses) and is written in the shelf's own wording; the balāgha is named on the token that carries it, after the
syntax. A figure a commentator names or describes is written plainly with his name; one that rests on the Talkhīṣ's
definition alone says «عَلَى حَدِّ التَّلْخِيصِ».

Sources on disk: research/sources/muallaqat-al-harith-src.txt (Ibn Qutayba + al-Zawzanī), -durra.txt.

THIS FILE IS ASSEMBLED from parts kept in the author's work folder (head / chapter blocks / lexicon / tail); it is the
single source of the package. RESUMABLE: verses are filed by number through VV(); the chapters are cut from PLAN as far
as the verses reach, and the attribution says how far the package goes.
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_al_harith.py
"""
import json, os, pathlib, sys, unicodedata, re

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-al-harith"
PKG = OUT_ROOT / SLUG

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import tok, seg, WA_AR, FA_AR, WA_ISTINAF
import sarf_gen as _sg

NO = ("", "", "")
NFC = lambda x: unicodedata.normalize("NFC", x)
def cap(s): return s[:1].upper() + s[1:]
def N3(*t):
    """join note triples"""
    return tuple("".join(x) for x in zip(*t)) if t else NO
def T(full, lex, pos, g, ar, en, tr, p=None, segs=None):
    return tok(full, lex, pos, list(g), ar, en, tr, punct=p, segments=segs)
def SG(*triples): return [seg(f, l, q) for f, l, q in triples]
def PH(t, lex, span=2):
    t["phrase"] = {"lex": lex, "span": span}
    return t

PRON = {"هَا": "pron-3fs", "هُ": "pron-3ms", "هِ": "pron-3ms", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp", "هُنَّ": "pron-3fp", "هِنَّ": "pron-3fp",
        "هُمَا": "pron-3d", "هِمَا": "pron-3d", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كِ": "pron-2fs", "كُمْ": "pron-2mp", "نَا": "pron-1p"}
PRON_AR = {"هَا": "هَا", "هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُمُ": "هُمْ", "هُنَّ": "هُنَّ", "هِنَّ": "هُنَّ", "هُمَا": "هُمَا", "هِمَا": "هُمَا",
           "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كِ": "الْكَافُ", "كُمْ": "كُمْ", "نَا": "نَا"}
CONJ = {"w": ("wa", WA_AR, "The waw conjoins; ", "«ve» + "), "f": ("fa", FA_AR, "The fa conjoins; ", "«fe» + "),
        "wi": ("wa",) + WA_ISTINAF, "fi": ("fa", "الْفَاءُ لِلِاسْتِئْنَافِ، وَ", "The fa opens a new clause; ", "Fâ isti'nâf içindir; "),
        "wh": ("wa", "الْوَاوُ حَالِيَّةٌ، وَ", "The waw opens a hal clause; ", "Vâv hâliyyedir; "),
        "fs": ("fa", "الْفَاءُ لِلسَّبَبِيَّةِ، وَ", "The fa of cause; ", "Fâ sebebiyyedir; "),
        "fj": ("fa", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَ", "The fa that opens the answer of the condition; ", "Fâ şartın cevabının başındadır; "),
        "wr": ("wa-rubba", "الْوَاوُ وَاوُ «رُبَّ»، وَ", "The waw of رُبَّ («many a …»); ", "Vâv «rubbe» vâvıdır; ")}
JARR = {"bi": ("bi", "الْبَاءُ حَرْفُ جَرٍّ، وَ", "The ba is a jarr letter; ", "Bâ cer harfi; "),
        "ka": ("ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ", "The kaf is the jarr letter of likening; ", "Kâf teşbîh ve cer harfi; "),
        "li": ("li", "اللَّامُ حَرْفُ جَرٍّ، وَ", "The lam is a jarr letter; ", "Lâm cer harfi; ")}
SIGN = {"raf": "بِالضَّمَّةِ", "nasb": "بِالْفَتْحَةِ", "jarr": "بِالْكَسْرَةِ"}
ROLE = {
 "fail": ("فَاعِلٌ مَرْفُوعٌ", "the doer (fa'il), in raf'", "fâil, merfû", "raf", ["fail"]),
 "naib": ("نَائِبُ فَاعِلٍ مَرْفُوعٌ", "the deputy doer (na'ib al-fa'il), in raf'", "nâib-i fâil, merfû", "raf", ["naib-al-fail"]),
 "maf": ("مَفْعُولٌ بِهِ مَنْصُوبٌ", "the direct object, in nasb", "mef'ûlün bih, mansûb", "nasb", ["maful-bihi"]),
 "maf1": ("مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ", "the first object, in nasb", "birinci mef'ûlün bih, mansûb", "nasb", ["maful-bihi", "mafulayn"]),
 "maf2": ("مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ", "the second object, in nasb", "ikinci mef'ûlün bih, mansûb", "nasb", ["maful-bihi", "mafulayn"]),
 "mub": ("مُبْتَدَأٌ مَرْفُوعٌ", "the mubtada, in raf'", "mübtedâ, merfû", "raf", ["mubtada-khabar"]),
 "khb": ("خَبَرُ الْمُبْتَدَأِ مَرْفُوعٌ", "the khabar of the mubtada, in raf'", "mübtedânın haberi, merfû", "raf", ["mubtada-khabar"]),
 "mdf": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "the second term of the idafa, in jarr", "muzâfun ileyh, mecrûr", "jarr", ["idafa-definiteness"]),
 "majr": ("مَجْرُورٌ", "in jarr after the letter", "cer harfiyle mecrûr", "jarr", ["huruf-jarr"]),
 "hal": ("حَالٌ مَنْصُوبٌ", "a hal, in nasb", "hâl, mansûb", "nasb", ["hal"]),
 "zarfz": ("ظَرْفُ زَمَانٍ مَنْصُوبٌ", "an adverb of time, in nasb", "zaman zarfı, mansûb", "nasb", ["maful-fih"]),
 "zarfm": ("ظَرْفُ مَكَانٍ مَنْصُوبٌ", "an adverb of place, in nasb", "mekân zarfı, mansûb", "nasb", ["maful-fih"]),
 "ismk": ("اسْمُ كَانَ مَرْفُوعٌ", "the noun of كَانَ, in raf'", "kâne'nin ismi, merfû", "raf", ["kana-wa-akhawatuha"]),
 "khbk": ("خَبَرُ كَانَ مَنْصُوبٌ", "the predicate of كَانَ, in nasb", "kâne'nin haberi, mansûb", "nasb", ["kana-wa-akhawatuha"]),
 "ismi": ("اسْمُ إِنَّ مَنْصُوبٌ", "the noun of إِنَّ, in nasb", "inne'nin ismi, mansûb", "nasb", ["inna-wa-akhawatuha"]),
 "khbi": ("خَبَرُ إِنَّ مَرْفُوعٌ", "the predicate of إِنَّ, in raf'", "inne'nin haberi, merfû", "raf", ["inna-wa-akhawatuha"]),
 "isma": ("اسْمُ أَنَّ مَنْصُوبٌ", "the noun of أَنَّ, in nasb", "enne'nin ismi, mansûb", "nasb", ["inna-wa-akhawatuha"]),
 "khba": ("خَبَرُ أَنَّ مَرْفُوعٌ", "the predicate of أَنَّ, in raf'", "enne'nin haberi, merfû", "raf", ["inna-wa-akhawatuha"]),
 "ismka": ("اسْمُ كَأَنَّ مَنْصُوبٌ", "the noun of كَأَنَّ, in nasb", "keenne'nin ismi, mansûb", "nasb", ["inna-wa-akhawatuha"]),
 "khbka": ("خَبَرُ كَأَنَّ مَرْفُوعٌ", "the predicate of كَأَنَّ, in raf'", "keenne'nin haberi, merfû", "raf", ["inna-wa-akhawatuha"]),
 "tamyiz": ("تَمْيِيزٌ مَنْصُوبٌ", "a tamyiz (specifier), in nasb", "temyîz, mansûb", "nasb", ["tamyiz"]),
 "mutlaq": ("مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ", "a maf'ul mutlaq (absolute object), in nasb", "mef'ûl-i mutlak, mansûb", "nasb", ["maful-mutlaq"]),
 "lah": ("مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ", "a maf'ul li-ajlih (object of cause), in nasb", "mef'ûlün leh, mansûb", "nasb", ["maful-lah"]),
 "munada": ("مُنَادًى مَنْصُوبٌ", "a vocative, in nasb", "münâdâ, mansûb", "nasb", ["vocative-munada"]),
}
for _c, _a, _e, _t in (("r", "مَرْفُوعٌ", "raf'", "merfû", ), ("n", "مَنْصُوبٌ", "nasb", "mansûb"), ("j", "مَجْرُورٌ", "jarr", "mecrûr")):
    _k = {"r": "raf", "n": "nasb", "j": "jarr"}[_c]
    ROLE["naat" + _c] = ("نَعْتٌ " + _a, "an adjective (na't), in " + _e + " like its noun", "na't (sıfat), mevsûfu gibi " + _t, _k, ["naat-sifa"])
    ROLE["atf" + _c] = ("مَعْطُوفٌ " + _a, "conjoined to the word before it, in " + _e, "ma'tûf, " + _t, _k, ["atf-nasaq"])
    ROLE["bdl" + _c] = ("بَدَلٌ " + _a, "a badal (substitute), in " + _e + " like the word it stands for", "bedel, mübdelün minh gibi " + _t, _k, ["badal"])
    ROLE["twk" + _c] = ("تَوْكِيدٌ مَعْنَوِيٌّ " + _a, "an emphasis (tawkid) of meaning, in " + _e + " like the word it strengthens", "ma'nevî te'kîd, müekked gibi " + _t, _k, ["tawkid"])
MUD = ("، مُضَافٌ", ", annexed", ", muzâf")
ENC3 = ("، مُضَافٌ، وَ%s ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; annexed, and the attached pronoun is the second term of the idafa, in the seat of jarr", "; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr")
# ---- signs that are not the plain vowel: (ar, en, tr) ----
S_JMS = ("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", " — by the ya, a sound masculine plural", " — cem-i müzekker sâlim olduğu için yâ ile")
S_JMSR = ("بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", " — by the waw, a sound masculine plural", " — cem-i müzekker sâlim olduğu için vâv ile")
S_MUTH = ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", " — by the ya, a dual", " — tesniye olduğu için yâ ile")
S_MUTHM = ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, a dual whose nun drops in the idafa", " — tesniye olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür")
S_JFS = ("بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ", " — by the kasra that stands for the fatha, a sound feminine plural", " — cem-i müennes sâlim olduğu için fetha yerine kesre ile")
S_DIPT = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", " — by the fatha that stands for the kasra, a diptote", " — gayr-i munsarif olduğu için kesre yerine fetha ile")
S_ALIF = lambda v, e, t: ("بِ" + v + " مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", " — by a " + e + " estimated on the alif", " — elif üzerinde takdîrî " + t + " ile")
S_AR, S_AN, S_AJ = S_ALIF("ضَمَّةٍ", "damma", "damme"), S_ALIF("فَتْحَةٍ", "fatha", "fetha"), S_ALIF("كَسْرَةٍ", "kasra", "kesre")
S_YA5 = ("بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", " — by the ya, one of the five nouns", " — esmâ-i hamseden olduğu için yâ ile")
S_ALIF5 = ("بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", " — by the alif, one of the five nouns", " — esmâ-i hamseden olduğu için elif ile")
# the rhyme: the rawī is a hamza with ḍamma after an alif (the ridf); the ḍamma is drawn out in recitation (the waṣl, a wāw)
QAF = (" — وَهُوَ قَافِيَةُ الْبَيْتِ: ضَمَّتُهُ ضَمَّةُ إِعْرَابِهِ، وَهِيَ حَرَكَةُ الرَّوِيِّ", " — it is the rhyme-word: its damma is its own iʿrāb, and it is the vowel of the rawī", " — kâfiye kelimesidir: dammesi kendi i'râbıdır, aynı zamanda revînin harekesidir")
QAF_N = (QAF[0] + "، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ وَأُشْبِعَتْ ضَمَّةُ الرَّوِيِّ", QAF[1] + "; at the rhyme its tanwin is dropped and the damma of the rawī is lengthened", QAF[2] + "; kâfiyede tenvini düşmüş, revînin dammesi uzatılmıştır")
def QAF_X(ar, en, tr):
    """a rhyme-word whose case is not raf': the ḍamma is the rawī's vowel over another case"""
    return (" — وَهُوَ قَافِيَةُ الْبَيْتِ: " + ar, " — it is the rhyme-word: " + en, " — kâfiye kelimesidir: " + tr)
def R(role, full, lex, enc=None, n=NO, g=(), pos="noun", mud=False, sign=None, c=None, j=None, p=None, of=None):
    """a noun in a named seat: c = a conjunction written on it, j = a jarr letter written on it (bi / ka / li),
    enc = its attached pronoun, mud = annexed to the next word, sign = (ar, en, tr) when not the default,
    of = (ar, en, tr) of the word it belongs to («نَعْتٌ لِـ…»، «مَعْطُوفٌ عَلَى …»)"""
    full = NFC(full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs.append(seg(stem[:2], "wa" if k == "wa-rubba" else k, "conj")); stem = stem[2:]
    r = ROLE[role]; head = r[0]; hen, htr = r[1], r[2]
    if of:
        w = head.split(" ")
        if role.startswith("atf"): head = w[0] + " عَلَى «" + of[0] + "» " + " ".join(w[1:]); hen += " — joined to «" + of[1] + "»"; htr += " — «" + of[2] + "»"
        else: head = " ".join(w[:-1]) + " لِـ«" + of[0] + "» " + w[-1]; hen += " — of «" + of[1] + "»"; htr += " — «" + of[2] + "»"
    if j:
        k, a, e, t = JARR[j]; segs.append(seg(stem[:2], k, "prep")); stem = stem[2:]
        ar0 += a; en0 += e; tr0 += t
        if role == "majr": head = "«" + (stem[:-len(enc)] if enc else stem) + "» مَجْرُورٌ"
    core = stem[:-len(enc)] if enc else stem
    sg = sign or (SIGN[r[3]], "", "")
    a = ar0 + head + " " + sg[0]; e = en0 + hen + sg[1]; t = tr0 + htr + sg[2]
    if enc: a += ENC3[0] % PRON_AR[enc]; e += ENC3[1]; t += ENC3[2]
    elif mud: a += MUD[0]; e += MUD[1]; t += MUD[2]
    segs.append(seg(core, lex, pos))
    if enc: segs.append(seg(enc, PRON[enc], "pron"))
    tags = list(r[4]) + (["idafa-definiteness", "al-bariz-al-muttasil"] if enc else ["idafa-definiteness"] if mud else []) + (["huruf-jarr"] if j else []) + list(g)
    return tok(full, lex, pos, tags, a + n[0] + ".", cap(e + n[1] + "."), cap(t + n[2] + "."), punct=p, segments=segs if len(segs) > 1 else None)

_M = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى "
_FA = "ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ"
_FAN = "ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ"
_D = "فِعْلٌ مُضَارِعٌ "
VK = {
 "m": (_M + "الْفَتْحِ", "past verb built on fatha", "fetha üzere mebnî mâzî"),
 "ma": (_M + "فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "past verb built on a fatha estimated on the alif", "elif üzerindeki takdîrî fetha ile mebnî mâzî"),
 "mt": (_M + "الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "past verb built on fatha (the ta marks the feminine)", "fetha üzere mebnî mâzî (tâ te'nîs içindir)"),
 "mtq": (_M + "فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ", "past verb built on a fatha estimated on the alif that dropped before the feminine ta", "te'nîs tâ'sından önce düşen elif üzerinde takdîrî fetha ile mebnî mâzî"),
 "mtk": (_M + "الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "past verb built on fatha (the feminine ta takes kasra where two quiescents meet)", "fetha üzere mebnî mâzî (te'nîs tâ'sı iki sâkin karşılaştığı için kesrelidir)"),
 "mn": (_M + "السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ " + _FA, "past verb built on sukun because the nun of the women is attached; that nun is the doer, in the seat of raf'", "nûn-ı nisve bitiştiği için sükûn üzere mebnî mâzî; nûn fâildir, mahallen merfû"),
 "mw": (_M + "الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ " + _FA, "past verb built on damma because the waw of the group is attached; that waw is the doer, in the seat of raf'", "cemâat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâildir, mahallen merfû"),
 "mwa": (_M + "ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَوَاوُ الْجَمَاعَةِ " + _FA, "past verb built on a damma estimated on the alif that dropped before the waw of the group; that waw is the doer, in the seat of raf'", "cemâat vâvından önce düşen elif üzerinde takdîrî damme ile mebnî mâzî; vâv fâildir, mahallen merfû"),
 "mtu": (_M + "السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ " + _FA, "past verb built on sukun because the ta of the doer is attached; that ta («I») is the doer, in the seat of raf'", "fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ («ben») fâildir, mahallen merfû"),
 "mta": (_M + "السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ " + _FA, "past verb built on sukun because the ta of the doer is attached; that ta («you», masc.) is the doer, in the seat of raf'", "fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ («sen») fâildir, mahallen merfû"),
 "mti": (_M + "السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ " + _FA, "past verb built on sukun because the ta of the doer is attached; that ta («you», fem.) is the doer, in the seat of raf'", "fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ («sen», müennes) fâildir, mahallen merfû"),
 "mtum": (_M + "السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَ«تُمْ» " + _FA, "past verb built on sukun because the subject pronoun is attached; تُمْ («you», pl.) is the doer, in the seat of raf'", "ref zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» («siz») fâildir, mahallen merfû"),
 "mna": (_M + "السُّكُونِ لِاتِّصَالِهِ بِـ«نَا» الْفَاعِلِينَ، وَنَا " + _FA, "past verb built on sukun because نَا of the doers is attached; نَا («we») is the doer, in the seat of raf'", "fâil «nâ»sı bitiştiği için sükûn üzere mebnî mâzî; «nâ» («biz») fâildir, mahallen merfû"),
 "d": (_D + "مَرْفُوعٌ بِالضَّمَّةِ", "present verb in raf'", "merfû muzâri"),
 "da": (_D + "مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "present verb in raf' by a damma estimated on the alif", "elif üzerinde takdîrî damme ile merfû muzâri"),
 "dy": (_D + "مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "present verb in raf' by a damma estimated on the ya", "yâ üzerinde takdîrî damme ile merfû muzâri"),
 "dw": (_D + "مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ", "present verb in raf' by a damma estimated on the waw", "vâv üzerinde takdîrî damme ile merfû muzâri"),
 "d5": (_D + "مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَوَاوُ الْجَمَاعَةِ " + _FA, "present verb, one of the five verbs, in raf' by the kept nun; the waw of the group is the doer, in the seat of raf'", "ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; cemâat vâvı fâildir, mahallen merfû"),
 "d5y": (_D + "مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ " + _FA, "present verb, one of the five verbs, in raf' by the kept nun; the ya of the woman addressed is the doer, in the seat of raf'", "ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; muhâtaba yâ'sı fâildir, mahallen merfû"),
 "dn": (_D + "مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ " + _FA, "present verb built on sukun because the nun of the women is attached; that nun is the doer, in the seat of raf'", "nûn-ı nisve bitiştiği için sükûn üzere mebnî muzâri; nûn fâildir, mahallen merfû"),
 "a": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ", "imperative built on sukun", "sükûn üzere mebnî emir"),
 "a5y": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ " + _FA, "imperative built on the dropping of the nun; the ya of the woman addressed is the doer, in the seat of raf'", "nûnun hazfi üzere mebnî emir; muhâtaba yâ'sı fâildir, mahallen merfû"),
}
def JZ(why_ar, why_en, why_tr, sign="sukun"):
    """a muḍāriʿ in jazm: JZ("بِلَمْ", "by لَمْ", "lem ile") …"""
    s = {"sukun": ("السُّكُونُ", "the sukun", "sükûn"),
         "nun": ("حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ", "the dropping of the nun, for it is one of the five verbs", "ef'âl-i hamseden olduğu için nûnun hazfi"),
         "ya": ("حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْكَسْرَةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا", "the dropping of the weak letter (the ya), the kasra before it left as its trace", "illet harfinin (yâ'nın) hazfi; önceki kesre ona delildir"),
         "waw": ("حَذْفُ حَرْفِ الْعِلَّةِ (الْوَاوِ)، وَالضَّمَّةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا", "the dropping of the weak letter (the waw), the damma before it left as its trace", "illet harfinin (vâv'ın) hazfi; önceki damme ona delildir"),
         "alif": ("حَذْفُ حَرْفِ الْعِلَّةِ (الْأَلِفِ)، وَالْفَتْحَةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا", "the dropping of the weak letter (the alif), the fatha before it left as its trace", "illet harfinin (elifin) hazfi; önceki fetha ona delildir"),
         "fatha": ("السُّكُونُ، وَحُرِّكَ بِالْفَتْحِ لِلتَّخَلُّصِ مِنَ الْتِقَاءِ السَّاكِنَيْنِ فِي الْمُضَاعَفِ", "the sukun — voweled with fatha to keep two quiescents apart in the doubled verb", "sükûn — muzâafta iki sâkinin karşılaşmaması için fetha ile harekelenmiştir"),
         "kasr": ("السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "the sukun — voweled with kasra where two quiescents meet", "sükûn — iki sâkin karşılaştığı için kesre ile harekelenmiştir")}[sign]
    return (_D + "مَجْزُومٌ " + why_ar + " وَعَلَامَةُ جَزْمِهِ " + s[0], "present verb in jazm " + why_en + ", its sign " + s[1], why_tr + " meczûm muzâri, alâmeti " + s[2])
def NS(why_ar, why_en, why_tr, sign="fatha"):
    """a muḍāriʿ in nasb: NS("بِأَنْ", "by أَنْ", "en ile") …"""
    s = {"fatha": ("الْفَتْحَةُ", "the fatha", "fetha"),
         "nun": ("حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ", "the dropping of the nun, for it is one of the five verbs", "ef'âl-i hamseden olduğu için nûnun hazfi"),
         "alif": ("فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "a fatha estimated on the alif", "elif üzerinde takdîrî fetha")}[sign]
    return (_D + "مَنْصُوبٌ " + why_ar + " وَعَلَامَةُ نَصْبِهِ " + s[0], "present verb in nasb " + why_en + ", its sign " + s[1], why_tr + " mansûb muzâri, alâmeti " + s[2])
def DZ(ar, en, tr):
    """a hidden doer: DZ("هِيَ يَعُودُ عَلَى الْخَمْرِ", "«she» — the wine", "şaraba dönen gizli «o»")"""
    return (ar, en, tr)
NAHNU = DZ("نَحْنُ", "«we»", "gizli zamir «biz»")
ANA = DZ("أَنَا", "«I»", "gizli zamir «ben»")
ANTA = DZ("أَنْتَ", "«you»", "gizli zamir «sen»")
def HUWA(ar=None, en=None, tr=None): return DZ("هُوَ" + (" يَعُودُ عَلَى " + ar if ar else ""), "«he»" + (" — " + en if en else ""), (tr + " dönen " if tr else "") + "gizli zamir «o»")
def HIYA(ar=None, en=None, tr=None): return DZ("هِيَ" + (" يَعُودُ عَلَى " + ar if ar else ""), "«she»" + (" — " + en if en else ""), (tr + " dönen " if tr else "") + "gizli zamir «o»")
def V(kind, full, lex, n=NO, g=(), enc=None, c=None, pas=False, doer=None, p=None, encrole="maf"):
    """a verb: kind = a key of VK, or a ready triple from JZ() / NS(); enc = an attached object pronoun; doer = a hidden doer;
    pas = passive (the hidden / attached subject is then the deputy doer)"""
    full = NFC(full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    a, e, t = VK[kind] if isinstance(kind, str) else kind
    if pas:
        a = a.replace("فِعْلٌ مَاضٍ", "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ،", 1).replace("فِعْلٌ مُضَارِعٌ", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ،", 1).replace(_FA, _FAN)
        e = "passive " + e.replace("is the doer", "is the deputy doer"); t = "meçhul " + t.replace("fâildir", "nâib-i fâildir")
    if doer:
        a += ("، وَنَائِبُ الْفَاعِلِ" if pas else "، وَالْفَاعِلُ") + " مُسْتَتِرٌ تَقْدِيرُهُ: " + doer[0]
        e += ("; its deputy doer is the hidden " if pas else "; the doer is the hidden ") + doer[1]
        t += ("; nâib-i fâil " if pas else "; fâil ") + doer[2]
    core = stem[:-len(enc)] if enc else stem
    if enc:
        if encrole == "maf":
            a += "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ"
            e += "; the attached pronoun is the object, in the seat of nasb"; t += "; bitişik zamir mef'ûlün bih, mahallen mansûb"
        else:
            a += "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ"
            e += "; the attached pronoun is the first object, in the seat of nasb"; t += "; bitişik zamir birinci mef'ûlün bih, mahallen mansûb"
    segs.append(seg(core, lex, "verb"))
    if enc: segs.append(seg(enc, PRON[enc], "pron"))
    ks = kind if isinstance(kind, str) else ""
    tags = (["mudari-marfu"] if ks[:1] == "d" and ks != "dn" else []) + (["naib-al-fail"] if pas else []) + (["maful-bihi", "al-bariz-al-muttasil"] if enc else []) \
        + (["al-bariz-al-muttasil", "fail"] if ks in ("mn", "mw", "mwa", "mtu", "mta", "mti", "mtum", "mna", "d5", "d5y", "dn", "a5y") and not pas else []) \
        + (["afal-khamsa"] if ks in ("d5", "d5y") else []) + (["imperative-amr"] if ks[:1] == "a" else []) + list(g)
    return tok(full, lex, "verb", tags, ar0 + a + n[0] + ".", cap(en0 + e + n[1] + "."), cap(tr0 + t + n[2] + "."), punct=p, segments=segs if len(segs) > 1 else None)
def PR(full, lex, n=NO, g=(), p=None, c=None):
    """a jarr letter standing alone"""
    full = NFC(full); ar0 = en0 = tr0 = ""; segs = None
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs = [seg(full[:2], k, "conj"), seg(full[2:], lex, "prep")]
    return T(full, lex, "prep", ["huruf-jarr"] + list(g), ar0 + "حَرْفُ جَرٍّ" + n[0] + ".", cap(en0 + "a jarr letter" + n[1] + "."), cap(tr0 + "cer harfi" + n[2] + "."), p=p, segs=segs)
def JP(full, lex, enc, n=NO, g=(), p=None, c=None):
    """a jarr letter with its attached pronoun: بِهَا، مِنْهَا، عَلَيْهِ"""
    full = NFC(full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    segs += [seg(stem[:-len(enc)], lex, "prep"), seg(enc, PRON[enc], "pron")]
    return tok(full, lex, "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + list(g),
        ar0 + "حَرْفُ جَرٍّ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِهِ" + n[0] + ".",
        cap(en0 + "a jarr letter; the attached pronoun is in the seat of jarr after it" + n[1] + "."),
        cap(tr0 + "cer harfi; bitişik zamir onunla mahallen mecrûr" + n[2] + "."), punct=p, segments=segs)
def PT(full, lex, ar, en, tr, g=(), p=None, c=None, pos="part", segs=None):
    """a particle with its own line; c = a conjunction written on it"""
    full = NFC(full); ar0 = en0 = tr0 = ""
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs = segs or [seg(full[:2], k, "conj"), seg(full[2:], lex, pos)]
    return T(full, lex, pos, list(g), ar0 + ar + ".", cap(en0 + en + "."), cap(tr0 + tr + "."), p=p, segs=segs)
def MT(ar, en, tr):
    """«وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ…» — tr carries its own case ending"""
    return (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«" + ar + "»", "; the phrase hangs on «" + en + "»", "; câr-mecrûr «" + tr + " müteallik")
def MTH(ar, en, tr):
    """a jarr phrase hanging on an omitted word: MTH("خَبَرٍ مُقَدَّمٍ", "the omitted, fronted khabar", "öne alınmış mahzûf habere")"""
    return (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ " + ar, "; the phrase hangs on " + en, "; câr-mecrûr " + tr + " müteallik")
def MZ(ar, en, tr):
    """a ẓarf hanging on its governor"""
    return (" — مُتَعَلِّقٌ بِـ«" + ar + "»", " — it hangs on «" + en + "»", " — «" + tr + " müteallik")
def ZW(ar, en, tr):
    """a gloss or a reading that is al-Zawzanī's"""
    return (" — " + ar + " (الزَّوْزَنِيُّ)", " — " + en + " (al-Zawzanī)", " — " + tr + " (Zevzenî)")
def DR(ar, en, tr):
    """a reading that is al-Durra's"""
    return (" — " + ar + " (الدُّرَّةُ)", " — " + en + " (al-Durra)", " — " + tr + " (Dürre)")
def NT(ar, en, tr): return (" — " + ar, " — " + en, " — " + tr)
def HADD(ar, en, tr):
    """a figure that rests on the Talkhīṣ's definition alone"""
    return (" — وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — " + ar, " — by the Talkhīṣ's definition, " + en, " — Telhîs'in tarifine göre " + tr)
# ---- the seat of a clause ----
_SEAT = {
 "nr": ("فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«%s»", "a na't of «%s», in the seat of raf'", "«%s» na'tı, mahallen merfû"),
 "nn": ("فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«%s»", "a na't of «%s», in the seat of nasb", "«%s» na'tı, mahallen mansûb"),
 "nj": ("فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«%s»", "a na't of «%s», in the seat of jarr", "«%s» na'tı, mahallen mecrûr"),
 "hal": ("فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «%s»", "a hal of «%s», in the seat of nasb", "«%s» hâl, mahallen mansûb"),
 "khb": ("فِي مَحَلِّ رَفْعٍ خَبَرُ «%s»", "the khabar of «%s», in the seat of raf'", "«%s» haberi, mahallen merfû"),
 "khbn": ("فِي مَحَلِّ نَصْبٍ خَبَرُ «%s»", "the predicate of «%s», in the seat of nasb", "«%s» haberi, mahallen mansûb"),
 "mdf": ("فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «%s» إِلَيْهَا", "in the seat of jarr, «%s» being annexed to it", "«%s» kendisine muzâf olduğu için mahallen mecrûr"),
 "maqul": ("فِي مَحَلِّ نَصْبٍ مَقُولُ «%s»", "what «%s» says, in the seat of nasb", "«%s» mekûlü, mahallen mansûb"),
 "atf": ("مَعْطُوفَةٌ عَلَى جُمْلَةِ «%s»", "joined to the clause «%s»", "«%s» cümlesine ma'tûf"),
 "maf": ("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«%s»", "the object of «%s», in the seat of nasb", "«%s» mef'ûlü, mahallen mansûb"),
}
def CL(kind, ar=None, en=None, tr=None):
    """the seat of the clause this verb heads: CL("nr", "قَوْمٍ", "a people", "kavm»in") — tr carries its case ending inside the quotes"""
    if kind == "sila": return (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — the clause is the relative's ṣila and has no seat of its own", " — cümle sıla cümlesidir, i'râbdan mahalli yoktur")
    if kind == "ist": return (" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — a fresh sentence, with no seat of its own", " — cümle müste'nefedir, i'râbdan mahalli yoktur")
    if kind == "ibt": return (" — وَالْجُمْلَةُ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — the sentence opens the speech and has no seat of its own", " — cümle ibtidâiyyedir, i'râbdan mahalli yoktur")
    if kind == "jawab": return (" — وَالْجُمْلَةُ جَوَابُ شَرْطٍ غَيْرِ جَازِمٍ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — the clause is the answer of a condition that does not put in jazm, and has no seat of its own", " — cümle gayr-i câzim şartın cevabıdır, i'râbdan mahalli yoktur")
    if kind == "itirad": return (" — وَالْجُمْلَةُ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — a parenthetical clause, with no seat of its own", " — cümle mu'tarızadır, i'râbdan mahalli yoktur")
    s = _SEAT[kind]
    tr_ = s[2].replace("«%s»", "«" + tr) if tr else s[2]
    return (" — وَالْجُمْلَةُ " + (s[0] % ar), " — the clause is " + (s[1] % en), " — cümle " + tr_)
def KAANNA(full, n=NO, enc=None, g=(), c=None):
    """كَأَنَّ alone, or with its noun attached"""
    full = NFC(full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a0, e0, t0 = CONJ[c]; ar0, en0, tr0 = a0, e0, t0; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    a = "كَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ"; e = "كَأَنَّ is the particle of likening, one of إِنَّ's sisters: it puts its noun in nasb"; t = "keenne: teşbîh ve nasb harfi, inne'nin kardeşlerinden"
    if enc:
        a += "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا"; e += "; the attached pronoun is its noun, in the seat of nasb"; t += "; bitişik zamir ismidir, mahallen mansûb"
        segs += [seg(stem[:-len(enc)], "kaanna", "part"), seg(enc, PRON[enc], "pron")]
    return T(full, "kaanna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"] + (["al-bariz-al-muttasil"] if enc else []) + list(g), ar0 + a + n[0] + ".", cap(en0 + e + n[1] + "."), cap(tr0 + t + n[2] + "."),
             segs=segs if len(segs) > 1 else None)
def INNA(full, which="inna", n=NO, enc=None, g=(), c=None, j=None):
    """إِنَّ / أَنَّ alone or with its noun attached; j="bi" for بِأَنَّا"""
    full = NFC(full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a0, e0, t0 = CONJ[c]; ar0, en0, tr0 = a0, e0, t0; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    if j:
        k, a0, e0, t0 = JARR[j]; ar0 += a0; en0 += e0; tr0 += t0; segs.append(seg(stem[:2], k, "prep")); stem = stem[2:]
    nm = {"inna": ("إِنَّ", "إِنَّ", "inne"), "anna": ("أَنَّ", "أَنَّ", "enne")}[which]
    a = nm[0] + " حَرْفُ تَوْكِيدٍ وَنَصْبٍ"; e = nm[1] + " is the particle of emphasis that puts its noun in nasb"; t = nm[2] + ": te'kîd ve nasb harfi"
    if enc:
        a += "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا"; e += "; the attached pronoun is its noun, in the seat of nasb"; t += "; bitişik zamir ismidir, mahallen mansûb"
        core = "إِنَّ" if which == "inna" else "أَنَّ"
        segs += [seg(core, which, "part"), seg(enc, PRON[enc], "pron")]
    return T(full, which, "part", ["inna-wa-akhawatuha"] + (["al-bariz-al-muttasil"] if enc else []) + (["huruf-jarr"] if j else []) + list(g), ar0 + a + n[0] + ".", cap(en0 + e + n[1] + "."), cap(tr0 + t + n[2] + "."),
             segs=segs if len(segs) > 1 else None)
IDHA_L = ("ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ، خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ", "an adverb of time to come that carries a condition — annexed to its condition clause and held in nasb by its answer — built on sukun, in the seat of nasb", "gelecek zaman için şart mânâsı taşıyan zarf: şartına muzâf, cevabıyla mansûb; sükûn üzere mebnî, mahallen mansûb")
def IDHA(full="إِذَا", n=NO, g=(), c=None, plain=False):
    """إِذَا: conditional (default) or plain adverb (plain=True: «ظَرْفُ زَمَانٍ … مُتَعَلِّقٌ بِـ…» given in n)"""
    if plain:
        return PT(full, "idha", "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ" + n[0], "an adverb of time built on sukun, in the seat of nasb, annexed to the clause after it" + n[1], "sükûn üzere mebnî zaman zarfı, mahallen mansûb; kendisinden sonraki cümleye muzâf" + n[2], g=["maful-fih", "idha-shartiyya"] + list(g), c=c, pos="noun")
    return PT(full, "idha", IDHA_L[0] + n[0], IDHA_L[1] + n[1], IDHA_L[2] + n[2], g=["idha-shartiyya", "maful-fih"] + list(g), c=c, pos="noun")
MA_Z = lambda: PT("مَا", "ma-zaida", "حَرْفٌ زَائِدٌ بَعْدَ «إِذَا» لِلتَّوْكِيدِ، لَا عَمَلَ لَهُ", "an extra particle after إِذَا, for emphasis; it governs nothing", "«izâ»dan sonra te'kîd için gelen zâid harf; ameli yoktur", g=["anwa-ma", "huruf-al-ziyada-fil-kafiya"])
def QAD(full="قَدْ", c=None, kasr=False, n=NO):
    return PT(full, "qad", "قَدْ حَرْفُ تَحْقِيقٍ" + ("، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ" if kasr else "") + n[0], "قَدْ is the particle of assurance" + (", voweled with kasra where two quiescents meet" if kasr else "") + n[1], "kad: tahkîk harfi" + (" — iki sâkin karşılaştığı için kesre ile harekelenmiştir" if kasr else "") + n[2], g=["qad-harf"], c=c)
def LA_N(full="لَا", c=None, n=NO):
    return PT(full, "la-nafiya", "لَا حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ" + n[0], "لَا is a particle of negation; it governs nothing" + n[1], "lâ: nefy harfi, ameli yoktur" + n[2], g=["la-nafiya"], c=c)
def LAM(full="لَمْ", c=None, n=NO):
    return PT(full, "lam", "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ" + n[0], "لَمْ is the particle of negation and jazm that turns the present to the past" + n[1], "lem: nefy, cezm ve kalb harfi" + n[2], g=["lam-jazim", "nawasib-wa-jawazim-al-mudari"], c=c)
def AN(full="أَنْ", n=NO, c=None, g=()):
    return PT(full, "an-masdariyya", "أَنْ حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ" + n[0], "أَنْ is the masdar-making particle that puts the present verb in nasb" + n[1], "en: masdar ve nasb harfi" + n[2], g=["an-masdariyya", "nawasib-wa-jawazim-al-mudari"] + list(g), c=c)
def HATTA(n=NO):
    return PT("حَتَّى", "hatta", "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْفِعْلُ بَعْدَهُ مَنْصُوبٌ بِـ«أَنْ» مُضْمَرَةً وُجُوبًا" + n[0], "a jarr letter of «until»; the verb after it is in nasb by an أَنْ that must stay hidden" + n[1], "gâye bildiren cer harfi; sonraki fiil vücûben gizli «en» ile mansûbdur" + n[2], g=["huruf-jarr", "ila-hatta-fi-wal-ba-fil-kafiya", "an-masdariyya"], pos="prep")
def NAHNU_M(full="وَنَحْنُ", c="w", n=NO, g=()):
    return PT(full, "nahnu", "نَحْنُ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ" + n[0], "نَحْنُ «we» is a detached pronoun built on damma, in the seat of raf' as mubtada" + n[1], "nahnü «biz»: damme üzere mebnî munfasıl zamir, mübtedâ olarak mahallen merfû" + n[2], g=["mubtada-khabar", "al-mabni-wal-mudmar"] + list(g), c=c, pos="pron")
TB = ["tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"]

CH = {}
VERSES = {}
def VV(n, en, tr, first, second):
    """one verse = one sentence: «•» closes the first hemistich, a full stop the verse"""
    first, second = [t for t in first if t], [t for t in second if t]
    first[-1]["punctAfter"] = "•"
    second[-1].setdefault("punctAfter", ".")
    assert n not in VERSES, n
    VERSES[n] = {"id": "v%d" % n, "translation": {"en": en, "tr": tr}, "tokens": first + second}
# =====================================================================================================================
# Chapter 1 — خَبَرُ الْحَارِثِ بْنِ حِلِّزَةَ (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/193, § 319 whole — verbatim, contiguous)
# =====================================================================================================================
HARITH = DZ("هُوَ يَعُودُ عَلَى الْحَارِثِ", "«he» — al-Ḥārith", "Hâris'e dönen gizli «o»")
AMR_H = DZ("هُوَ يَعُودُ عَلَى عَمْرِو بْنِ هِنْدٍ", "«he» — ʿAmr ibn Hind", "Amr b. Hind'e dönen gizli «o»")
IBN = lambda role, full, n=NO: R(role, full, "ibn", mud=True, n=n)
def NAME(role, full, lex, sign=None, n=NO, p=None, g=(), mud=False, c=None, j=None):
    return R(role, full, lex, pos="propn", sign=sign, n=n, p=p, g=g, mud=mud, c=c, j=j)
S_DIPT_T = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ", " — by the fatha that stands for the kasra: a diptote, being a proper name on the pattern of a verb", " — özel isim ve fiil vezninde olduğu için gayr-i munsarif: kesre yerine fetha ile")
S_BANI = ("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür")
HUWA_MUB = lambda full="هُوَ", c=None, n=NO, p=None: PT(full, "huwa", "هُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ" + n[0], "هُوَ «he» is a detached pronoun built on fatha, in the seat of raf' as mubtada" + n[1], "hüve «o»: fetha üzere mebnî munfasıl zamir, mübtedâ olarak mahallen merfû" + n[2], g=["mubtada-khabar", "al-mabni-wal-mudmar"], c=c, pos="pron", p=p)
QASIDA = HIYA("الْقَصِيدَةِ", "the ode", "kasideye")

def V1(intro):
    """verse 1 of the ode — quoted by Ibn Qutayba in the khabar (intro=False) and the poem's opening (intro=True)"""
    m = ((" — وَالْقَصِيدَةُ مِنَ الْبَحْرِ الْخَفِيفِ، وَرَوِيُّهَا هَمْزَةٌ مَضْمُومَةٌ قَبْلَهَا أَلِفٌ رِدْفًا", " — the ode is in the metre al-khafīf; its rhyme-letter is a hamza with damma, with an alif before it as ridf", " — kaside hafîf bahrindendir; revîsi dammeli hemze, öncesinde ridf olarak elif") if intro else NO)
    return ([V("mt", "آذَنَتْنَا", "adhana", enc="نَا", g=["form-iv-verbs"] + (["ilm-al-arud", "al-qafiya"] if intro else []), n=N3(CL("ibt") if intro else NT("وَالْبَيْتُ كُلُّهُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«الْقَائِلُ»", "the whole verse is the object of «the one who said», in the seat of nasb", "beytin tamamı «söyleyen»in mef'ûlü, mahallen mansûb"), m, ZW("الْإِيذَانُ: الْإِعْلَامُ", "إِيذَان is giving notice", "«îzân»: bildirmek"))),
             R("majr", "بِبَيْنِهَا", "bayn-parting", j="bi", enc="هَا", n=N3(MT("آذَنَتْ", "gave notice", "bildirdi»ye"), DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti"), ZW("الْبَيْنُ: الْفِرَاقُ؛ أَيْ بِعَزْمِهَا عَلَى فِرَاقِنَا", "بَيْن is parting: that is, her resolve to leave us", "«beyn»: ayrılık; yani bizden ayrılmaya azmetmesi"))),
             NAME("fail", "أَسْمَاءُ", "asma-hr", g=["mamnu-min-sarf"], n=NT("وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", "it takes no tanwin: a diptote, a woman's name", "tenvin almaz: kadın adı olduğu için gayr-i munsarif"))],
            [PT("رُبَّ", "rubba", "حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ لَا يَتَعَلَّقُ بِشَيْءٍ", "a jarr letter that resembles the extra ones; it hangs on nothing", "zâide benzeyen cer harfi; hiçbir şeye müteallik olmaz", g=["al-lam-wa-rubba-fil-kafiya", "huruf-jarr"]),
             T("ثَاوٍ", "thawi-hr", "noun", ["mubtada-khabar", "ism-maqsur-manqus", "ism-fail", "hadhf-wa-taqdir"],
               "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ، وَهُوَ مَجْرُورٌ لَفْظًا بِـ«رُبَّ»؛ اسْمٌ مَنْقُوصٌ حُذِفَتْ يَاؤُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ (رُبَّ رَجُلٍ ثَاوٍ) — الثَّاوِي: الْمُقِيمُ (الزَّوْزَنِيُّ).",
               "The mubtada, in raf' by an estimated damma that the jarr of رُبَّ keeps from showing — in jarr in its letters after رُبَّ; a manqus noun whose ya dropped where two quiescents met; it is the adjective of an omitted noun («many a man staying») — ثَاوٍ is one who stays (al-Zawzanī).",
               "Mübtedâ: zâide benzeyen cer harfinin harekesi mahalli işgal ettiği için takdîrî damme ile merfû, lafzen «rubbe» ile mecrûr; iki sâkin karşılaştığı için yâsı düşen menkûs isim; mahzûf bir mevsûfun sıfatıdır («nice ikamet eden adam») — «sâvî»: ikamet eden (Zevzenî)."),
             V("d", "يُمَلُّ", "malla-hr", pas=True, g=["doubled-verbs"], n=NT("وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ، وَخَبَرُ الْمُبْتَدَأِ الْمَجْرُورِ بِـ«رُبَّ» مَحْذُوفٌ تَقْدِيرُهُ: مَوْجُودٌ (الدُّرَّةُ)", "the clause is a second adjective of the omitted noun; the khabar of the mubtada that رُبَّ put in jarr is omitted — «there is» (al-Durra)", "cümle mahzûf mevsûfun ikinci sıfatıdır; «rubbe» ile mecrûr mübtedânın haberi mahzûftur: «vardır» (Dürre)")),
             JP("مِنْهُ", "min", "هُ", n=MT("يُمَلُّ", "is wearied", "usanılır»a")),
             R("naib", "الثَّوَاءُ", "thawa-hr", n=N3(QAF, ZW("الثَّوَاءُ وَالثُّوِيُّ: الْإِقَامَةُ؛ وَالتَّقْدِيرُ: رُبَّ ثَاوٍ يُمَلُّ مِنْ ثَوَائِهِ — يُرِيدُ أَنَّ أَسْمَاءَ وَإِنْ طَالَتْ إِقَامَتُهَا لَمْ يَمْلُلْهَا", "ثَوَاء and ثُوِيّ are staying; the sense is «many a one who stays is wearied of for his staying» — he means that, however long Asmāʾ stayed, he never wearied of her", "«sevâ» ve «süviyy»: ikamet; takdir: «nice ikamet eden, ikametinden usanılır» — Esmâ ne kadar uzun kalsa da ondan usanmadığını kastediyor")))])

S1 = []
S1.append({"id": "s1", "translation": {
  "en": "He is of the Banū Yashkur, of Bakr ibn Wāʾil.",
  "tr": "O, Benî Yeşkür'dendir; Bekir b. Vâil'den."},
 "tokens": [HUWA_MUB(n=NT("يَعُودُ عَلَى الْحَارِثِ", "it refers to al-Ḥārith", "Hâris'e döner")),
  PR("مِنْ", "min", n=MTH("خَبَرِ الْمُبْتَدَأِ", "the omitted khabar of the mubtada", "mübtedânın mahzûf haberine")),
  R("majr", "بَنِي", "banu", mud=True, sign=S_BANI, g=["jam-mudhakkar-salim"]),
  NAME("mdf", "يَشْكُرَ", "yashkur", sign=S_DIPT_T, g=["mamnu-min-sarf"], p="،"),
  PR("مِنْ", "min", n=MTH("خَبَرٍ ثَانٍ لِلْمُبْتَدَأِ", "an omitted second khabar of the mubtada", "mübtedânın mahzûf ikinci haberine")),
  NAME("majr", "بَكْرِ", "bakr", mud=True),
  IBN("naatj", "بْنِ"),
  NAME("mdf", "وَائِلٍ", "wail-hr", p=".")]})
S1.append({"id": "s2", "translation": {
  "en": "He was a leper, and it is he who said:",
  "tr": "Alacalı (abras) idi; şunu söyleyen odur:"},
 "tokens": [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], WA_ISTINAF[0] + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْحَارِثِ.",
    WA_ISTINAF[1] + "كَانَ is a defective past verb built on fatha; its noun is the hidden «he» — al-Ḥārith.", WA_ISTINAF[2] + "kâne: fetha üzere mebnî nâkıs mâzî; ismi Hâris'e dönen gizli «o»dur.", segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  R("khbk", "أَبْرَصَ", "abras", g=["mamnu-min-sarf"], n=NT("وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", "it takes no tanwin: a diptote, an adjective on the pattern of a verb", "tenvin almaz: sıfat ve fiil vezninde olduğu için gayr-i munsarif"), p="،"),
  HUWA_MUB("وَهُوَ", c="wi"),
  R("khb", "الْقَائِلُ", "qail", g=["ism-fail"], n=NT("وَهُوَ اسْمُ فَاعِلٍ يَعْمَلُ عَمَلَ فِعْلِهِ، وَالْبَيْتُ بَعْدَهُ مَقُولُهُ", "an active participle working like its verb; the verse after it is what he said", "fiili gibi amel eden ism-i fâil; ondan sonraki beyit onun mekûlüdür"), p=":")]})
_v1a, _v1b = V1(False)
_v1a[-1]["punctAfter"] = "•"; _v1b[-1]["punctAfter"] = "."
S1.append({"id": "s3", "translation": {
  "en": "«Asmāʾ has told us she is leaving — many a one who stays is wearied of for staying.»",
  "tr": "«Esmâ bize ayrılacağını bildirdi — nice kalan vardır ki kalışından usanılır.»"},
 "tokens": _v1a + _v1b})
S1.append({"id": "s4", "translation": {
  "en": "It is said that he improvised it before ʿAmr ibn Hind, extempore, over a matter between Bakr and Taghlib after the peace;",
  "tr": "Denir ki onu, sulhtan sonra Bekir ile Tağlib arasında olan bir mesele hakkında, Amr b. Hind'in huzurunda irticâlen (hazırlıksız) söylemiştir;"},
 "tokens": [V("d", "وَيُقَالُ", "qala", c="wi", pas=True, g=["hollow-verbs"], n=NT("وَنَائِبُ فَاعِلِهِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ", "its deputy doer is the clause reported after it", "nâib-i fâili ondan sonraki hikâye edilen cümledir")),
  INNA("إِنَّهُ", enc="هُ", g=["mawadi-kasr-inna"], n=NT("وَكُسِرَتْ هَمْزَتُهَا لِأَنَّهَا مَحْكِيَّةٌ بِالْقَوْلِ، وَالْهَاءُ لِلْحَارِثِ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِـ«يُقَالُ»", "its hamza takes kasra because it is reported after «it is said»; the ha is al-Ḥārith; the clause is the deputy doer of «it is said», in the seat of raf'", "hemzesi kavlden sonra hikâye edildiği için kesrelidir; hâ Hâris'tir; cümle «denir»in nâib-i fâili, mahallen merfû")),
  V("m", "ارْتَجَلَهَا", "irtajala-hr", enc="هَا", doer=HARITH, g=["form-viii-verbs"], n=N3(CL("khb", "إِنَّ", "إِنَّ", "inne"), NT("وَالْهَاءُ لِلْقَصِيدَةِ", "the ha is the ode", "hâ kasideye döner"))),
  R("zarfm", "بَيْنَ", "bayna", mud=True, n=MZ("ارْتَجَلَ", "improvised", "irticâl etti»ye")),
  R("mdf", "يَدَيْ", "yad", mud=True, sign=S_MUTHM, g=["al-muthanna"]),
  NAME("mdf", "عَمْرِو", "amr-name", mud=True),
  IBN("naatj", "بْنِ"),
  NAME("mdf", "هِنْدٍ", "hind", n=NT("وَصُرِفَ لِأَنَّهُ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ، وَيَجُوزُ فِيهِ الْمَنْعُ", "given tanwin, being a three-letter name with a quiescent middle; it may also be left a diptote", "orta harfi sâkin üç harfli isim olduğu için munsarif kılınmıştır; gayr-i munsarif yapmak da caizdir")),
  R("mutlaq", "ارْتِجَالًا", "irtijal", g=["masdar"], n=NT("مُؤَكِّدٌ لِعَامِلِهِ", "it strengthens its verb", "âmilini te'kîd eder"), p="،"),
  PR("فِي", "fi", n=MT("ارْتَجَلَ", "improvised", "irticâl etti»ye")),
  R("majr", "شَيْءٍ", "shay"),
  T("كَانَ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «وَقَعَ» مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «شَيْءٍ»، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«شَيْءٍ».",
    "A complete past verb meaning «happened», built on fatha; its doer is the hidden «it» — the matter; the clause is a na't of «a matter», in the seat of jarr.", "«Vuku buldu» anlamında tam mâzî, fetha üzere mebnî; fâili «şey»e dönen gizli «o»; cümle «şey»in na'tı, mahallen mecrûr."),
  R("zarfm", "بَيْنَ", "bayna", mud=True, n=MZ("كَانَ", "happened", "oldu»ya")),
  NAME("mdf", "بَكْرٍ", "bakr"),
  NAME("atfj", "وَتَغْلِبَ", "taghlib-amr", c="w", sign=S_DIPT_T, g=["mamnu-min-sarf"]),
  R("zarfz", "بَعْدَ", "bada", mud=True, n=MZ("كَانَ", "happened", "oldu»ya")),
  R("mdf", "الصُّلْحِ", "sulh", p="،")]})
S1.append({"id": "s5", "translation": {
  "en": "and he would recite it to him from behind the curtain, for the leprosy he had;",
  "tr": "ve üzerindeki alacalık (baras) yüzünden ona perdenin arkasından okurdu;"},
 "tokens": [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْحَارِثِ.",
    "The waw conjoins; كَانَ is a defective past verb built on fatha; its noun is the hidden «he» — al-Ḥārith.", "«ve» + kâne: fetha üzere mebnî nâkıs mâzî; ismi Hâris'e dönen gizli «o»dur.", segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  V("d", "يُنْشِدُهُ", "anshada", enc="هُ", doer=HARITH, g=["form-iv-verbs"], n=N3(CL("khbn", "كَانَ", "كَانَ", "kâne"), NT("وَالْهَاءُ لِعَمْرِو بْنِ هِنْدٍ، وَالْمَفْعُولُ الثَّانِي — الْقَصِيدَةُ — مَفْهُومٌ", "the ha is ʿAmr ibn Hind, and the second object — the ode — is understood", "hâ Amr b. Hind'e döner; ikinci mef'ûl — kaside — anlaşılmaktadır"))),
  PR("مِنْ", "min", n=MT("يُنْشِدُ", "recites", "okur»a")),
  R("majr", "وَرَاءِ", "wara", mud=True),
  R("mdf", "السِّجْفِ", "sijf-hr", p="،"),
  R("majr", "لِلْبَرَصِ", "baras-hr", j="li", n=N3(MT("يُنْشِدُ", "recites", "okur»a"), NT("وَاللَّامُ لِلتَّعْلِيلِ", "the lam gives the reason", "lâm ta'lîl içindir"))),
  PT("الَّذِي", "alladhi", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«الْبَرَصِ»", "a relative noun built on sukun, in the seat of jarr as a na't of «the leprosy»", "sükûn üzere mebnî ism-i mevsûl, «baras»ın na'tı olarak mahallen mecrûr", g=["ism-mawsul", "naat-sifa"], pos="pron"),
  T("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «الَّذِي» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A defective past verb built on fatha; its noun is the hidden «it», which refers back to «which» — the clause is the relative's ṣila and has no seat of its own.", "Fetha üzere mebnî nâkıs mâzî; ismi «ellezî»ye dönen gizli «o» — cümle sıla cümlesidir, i'râbdan mahalli yoktur."),
  JP("بِهِ", "bi", "هُ", n=MTH("خَبَرِ «كَانَ»", "the omitted predicate of كَانَ", "«kâne»nin mahzûf haberine"), p="،")]})
S1.append({"id": "s6", "translation": {
  "en": "and he ordered the curtain between them lifted, admiring the ode;",
  "tr": "(Amr) kaside hoşuna gittiği için aralarındaki perdenin kaldırılmasını emretti;"},
 "tokens": [V("m", "فَأَمَرَ", "amara-command", c="f", doer=AMR_H),
  R("majr", "بِرَفْعِ", "raf", j="bi", mud=True, n=MT("أَمَرَ", "ordered", "emretti»ye")),
  R("mdf", "السِّجْفِ", "sijf-hr", n=NT("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", "a masdar annexed to its object", "masdarın mef'ûlüne izâfeti")),
  R("zarfm", "بَيْنَهُ", "bayna", enc="هُ", n=MZ("رَفْعِ", "lifting", "kaldırma»ya")),
  R("atfn", "وَبَيْنَهُ", "bayna", c="w", enc="هُ", of=("بَيْنَهُ", "between him", "beynehû"), n=NT("وَالْهَاءُ الْأُولَى لِعَمْرٍو وَالثَّانِيَةُ لِلْحَارِثِ", "the first ha is ʿAmr, the second al-Ḥārith", "birinci hâ Amr'a, ikincisi Hâris'e döner"), p="،"),
  R("lah", "اسْتِحْسَانًا", "istihsan-hr", g=["masdar"]),
  JP("لَهَا", "li", "هَا", n=N3(MT("اسْتِحْسَانًا", "admiring", "beğenme»ye"), NT("وَالْهَاءُ لِلْقَصِيدَةِ", "the ha is the ode", "hâ kasideye döner")), p="،")]})
S1.append({"id": "s7", "translation": {
  "en": "al-Ḥārith was leaning on a short spear, and it drove into his body without his feeling it.",
  "tr": "Hâris kısa bir mızrağa dayanıyordu; mızrak, o farkına varmadan bedenine saplandı."},
 "tokens": [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ.",
    "The waw conjoins; كَانَ is a defective past verb built on fatha.", "«ve» + kâne: fetha üzere mebnî nâkıs mâzî.", segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  NAME("ismk", "الْحَارِثُ", "harith-alam"),
  R("khbk", "مُتَوَكِّئًا", "mutawakki-hr", g=["ism-fail"]),
  PR("عَلَى", "ala", n=MT("مُتَوَكِّئًا", "leaning", "dayanan»a")),
  R("majr", "عَنَزَةٍ", "anaza-hr", p="،"),
  V("mt", "فَارْتَزَّتْ", "irtazza-hr", c="f", doer=HIYA("الْعَنَزَةِ", "the short spear", "kısa mızrağa"), g=["form-viii-verbs", "doubled-verbs"]),
  PR("فِي", "fi", n=MT("ارْتَزَّتْ", "drove in", "saplandı»ya")),
  R("majr", "جَسَدِهِ", "jasad", enc="هُ"),
  HUWA_MUB("وَهُوَ", c="wh"),
  LA_N(),
  V("d", "يَشْعُرُ", "shaara", doer=HARITH, n=NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «هُوَ»، وَجُمْلَةُ «وَهُوَ لَا يَشْعُرُ» فِي مَحَلِّ نَصْبٍ حَالٌ", "the clause is the khabar of «he», in the seat of raf'; «while he did not feel it» is a hal, in the seat of nasb", "cümle «o»nun haberi, mahallen merfû; «o farkına varmazken» cümlesi hâldir, mahallen mansûb"), p=".")]})
CH[1] = S1
# =====================================================================================================================
# The poem — vv. 1–8 — آذَنَتْنَا بِبَيْنِهَا أَسْمَاءُ
# =====================================================================================================================
S_DIPT_M = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", " — by the fatha that stands for the kasra: a diptote, for its feminine alif mamduda", " — memdûde te'nîs elifi sebebiyle gayr-i munsarif: kesre yerine fetha ile")
S_DIPT_Q = ("بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ نِيَابَةً عَنِ الْكَسْرَةِ، لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَقْصُورَةِ", " — by a fatha estimated on the alif standing for the kasra: a diptote, for its feminine alif maqsura", " — maksûre te'nîs elifi sebebiyle gayr-i munsarif: elif üzerinde kesre yerine takdîrî fetha ile")
S_MUTHA = ("بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", " — by the alif, a dual; the nun stands for the tanwin of the singular", " — tesniye olduğu için elif ile; nûn müfreddeki tenvinin karşılığıdır")
S_MUTHY = ("بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", " — by the ya, a dual; the nun stands for the tanwin of the singular", " — tesniye olduğu için yâ ile; nûn müfreddeki tenvinin karşılığıdır")
FA_PLACE = NT("وَالْفَاءُ هُنَا لِلْعَطْفِ مِنْ غَيْرِ أَنْ تُفِيدَ تَرْتِيبًا وَلَا تَعْقِيبًا (الدُّرَّةُ)", "here the fa joins without implying order or succession (al-Durra)", "fâ burada tertip ve takîb bildirmeden atfeder (Dürre)")
PLACE = lambda role, full, lex, n=NO, c="f", sign=None, mud=False, g=(), of=None: R(role, full, lex, pos="propn", c=c, n=n, sign=sign, mud=mud, g=g, of=of)
VV(1, "Asmāʾ has told us she is leaving — many a one who stays is wearied of for his staying,",
  "Esmâ bize ayrılacağını bildirdi — nice kalan vardır ki kalışından usanılır;", *V1(True))
VV(2, "after we had met at Burqat Shammāʾ — and the nearest of her dwellings is al-Khalṣāʾ —",
  "Burkatü Şemmâ'da buluşmamızın ardından — onun yurtlarının en yakını da Halsâ'dır —",
 [R("zarfz", "بَعْدَ", "bada", mud=True, n=N3(MZ("آذَنَتْنَا", "gave us notice", "bize bildirdi»ye"), NT("فِي الْبَيْتِ الْأَوَّلِ", "in the first verse", "ilk beyitte"))),
  R("mdf", "عَهْدٍ", "ahd", n=ZW("الْعَهْدُ: اللِّقَاءُ", "عَهْد here is meeting", "«ahd»: buluşma")),
  JP("لَهَا", "li", "هَا", n=MT("عَهْدٍ", "meeting", "buluşma»ya")),
  R("majr", "بِبُرْقَةِ", "burqa-tf", j="bi", mud=True, n=MT("عَهْدٍ", "meeting", "buluşma»ya"))],
 [PLACE("mdf", "شَمَّاءَ", "shamma-hr", c=None, sign=S_DIPT_M, g=["mamnu-min-sarf"], n=DR("هَضْبَةٌ مَعْرُوفَةٌ", "a well-known hill", "bilinen bir tepe")),
  R("mub", "فَأَدْنَى", "adna-hr", c="fi", mud=True, sign=S_AR, g=["ism-tafdil", "ism-maqsur-manqus"]),
  R("mdf", "دِيَارِهَا", "dar", enc="هَا", g=["jam-taksir"]),
  PLACE("khb", "الْخَلْصَاءُ", "khalsa-hr", c=None, n=N3(QAF, NT("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause is a fresh sentence with no seat of its own", "cümle müste'nefedir, i'râbdan mahalli yoktur"), ZW("أَيْ وَخَلْصَاءَ الَّتِي هِيَ أَقْرَبُ دِيَارِهَا إِلَيْنَا", "that is, al-Khalṣāʾ, the nearest of her dwellings to us", "yani yurtlarının bize en yakını olan Halsâ")))])
VV(3, "then al-Muḥayyāh, then al-Ṣifāḥ, then the heights of Fitāq, then ʿĀdhib, then al-Wafāʾ,",
  "sonra Muhayyâ, sonra Sifâh, sonra Fitâk'ın dorukları, sonra Âzib, sonra Vefâ;",
 [PLACE("atfr", "فَالْمُحَيَّاةُ", "muhayya-hr", of=("الْخَلْصَاءُ", "al-Khalṣāʾ", "el-Halsâ"), n=N3(FA_PLACE, DR("أَرْضٌ", "a tract of land", "bir arazi"))),
  PLACE("atfr", "فَالصِّفَاحُ", "sifah-hr", n=DR("هِضَابٌ مُجْتَمِعَةٌ، وَاحِدُهَا صَفْحَةٌ", "hills lying together; singular صَفْحَة", "bir arada duran tepeler; tekili «safha»"))],
 [R("atfr", "فَأَعْنَاقُ", "unuq", c="f", mud=True, g=["jam-taksir", "istiara", "aqsam-al-istiara"], n=N3(NT("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: أَعَالِي الْجَبَلِ أَعْنَاقٌ؛ وَصَفَهَا الدُّرَّةُ: «أَرَادَ بِأَعْنَاقِهِ أَعَالِيَهُ»، وَتَسْمِيَتُهَا عَلَى حَدِّ التَّلْخِيصِ", "an istiʿāra taṣrīḥiyya: the mountain's heights are called necks — al-Durra describes it («by its necks he means its heights»); the name is by the Talkhīṣ's definition", "istiâre-i tasrîhiyye: dağın doruklarına «boyunlar» denmiştir — Dürre tarif eder («boyunlarıyla doruklarını kastetti»); adlandırma Telhîs'in tarifine göredir"),
     DR("وَيُرْوَى «فَأَعْلَى ذِي فِتَاقٍ»", "it is also related «then the top of Dhū Fitāq»", "«fe-a'lâ zî Fitâk» diye de rivayet edilir"))),
  PLACE("mdf", "فِتَاقٍ", "fitaq-hr", c=None, n=DR("جَبَلٌ", "a mountain", "bir dağ")),
  PLACE("atfr", "فَعَاذِبٌ", "adhib-hr", n=DR("وَادٍ", "a valley", "bir vadi")),
  PLACE("atfr", "فَالْوَفَاءُ", "wafa-place-hr", n=N3(QAF, DR("أَرْضٌ", "a tract of land", "bir arazi")))])
VV(4, "then Riyāḍ al-Qaṭā, then the valleys of al-Shurbub, then al-Shuʿbatān, then al-Ablāʾ.",
  "sonra Riyâdu'l-Katâ, sonra Şurbub vadileri, sonra Şu'betân, sonra Eblâ.",
 [R("atfr", "فَرِيَاضُ", "rawda", c="f", mud=True, g=["jam-taksir"], n=DR("أَرْضٌ بِعَيْنِهَا يَسْتَنْقِعُ فِيهَا الْمَاءُ فَتُعْشِبُ وَتَأْلَفُهَا الطَّيْرُ", "a particular tract where water stands, so that it grows green and the birds keep to it", "suyun birikip yeşerdiği ve kuşların alıştığı belli bir arazi")),
  R("mdf", "الْقَطَا", "qata-hr", sign=S_AJ, g=["ism-maqsur-manqus"]),
  R("atfr", "فَأَوْدِيَةُ", "wadi-valley", c="f", mud=True, g=["jam-taksir"], n=DR("قَالَ الْأَصْمَعِيُّ: إِنَّمَا أَرَادَ وَادِيَ الشُّرْبُبِ فَاضْطَرَّهُ الشِّعْرُ إِلَى الْجَمْعِ", "al-Aṣmaʿī said: he meant the valley of al-Shurbub, and the verse forced him into the plural", "Asmaî dedi ki: Şurbub vadisini kastetti, şiir onu cemʿe zorladı"))],
 [PLACE("mdf", "الشُّرْبُبِ", "shurbub-hr", c=None, n=DR("اسْمُ جَبَلٍ، بِفَتْحِ الْبَاءِ الْأُولَى وَضَمِّهَا", "the name of a mountain, with fatha or damma on the first ba", "bir dağ adı; ilk bâ fethalı ve dammeli okunur")),
  PLACE("atfr", "فَالشُّعْبَتَانِ", "shubatan-hr", sign=S_MUTHA, g=["al-muthanna"], n=DR("أَكَمَةٌ لَهَا قَرْنَانِ نَاتِئَانِ", "a hillock with two jutting horns", "iki çıkıntılı boynuzu olan bir tepecik")),
  PLACE("atfr", "فَالْأَبْلَاءُ", "abla-hr", n=N3(QAF, DR("اسْمُ بِئْرٍ", "the name of a well", "bir kuyu adı")))])
VV(5, "I do not see there the one I knew in them, so today I weep, out of my wits — and what can weeping give back?",
  "Oralarda tanıdığım kimseyi göremiyorum; bu yüzden bugün aklım başımdan gitmiş ağlıyorum — ağlamak neyi geri getirir ki?",
 [LA_N(),
  V("da", "أَرَى", "raa", doer=ANA, g=["naqis-verbs"], n=CL("ist")),
  PT("مَنْ", "man", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "a relative noun built on sukun, in the seat of nasb as the object", "sükûn üzere mebnî ism-i mevsûl, mef'ûlün bih olarak mahallen mansûb", g=["ism-mawsul", "maful-bihi"], pos="pron"),
  V("mtu", "عَهِدْتُ", "ahida-hr", n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ، أَيْ: عَهِدْتُهُ", "the pronoun referring back is left out: «whom I knew»", "dönen zamir mahzûftur: «tanıdığım»"))),
  JP("فِيهَا", "fi", "هَا", n=MT("عَهِدْتُ", "I knew", "tanıdım»a")),
  V("dy", "فَأَبْكِي", "baka", c="f", doer=ANA, g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: أَنَا، وَالْجُمْلَةُ الِاسْمِيَّةُ مَعْطُوفَةٌ عَلَى «لَا أَرَى»؛ وَلِذٰلِكَ رُفِعَ الْفِعْلُ بَعْدَ الْفَاءِ وَالنَّفْيِ", "the clause is the khabar of an omitted mubtada, «I», and that nominal clause is joined to «I do not see»; that is why the verb after the fa and the negation is in raf'", "cümle mahzûf «ben» mübtedâsının haberi olarak mahallen merfû; isim cümlesi «görmüyorum»a ma'tûftur; bu yüzden fâ ve nefyden sonraki fiil merfûdur"))],
 [R("zarfz", "الْيَوْمَ", "yawm", n=MZ("أَبْكِي", "I weep", "ağlıyorum»a")),
  R("tamyiz", "دَلْهًا", "dalh-hr", n=N3(DR("وَقِيلَ: مَفْعُولٌ مُطْلَقٌ", "some make it an absolute object", "mef'ûl-i mutlak olduğu da söylenmiştir"), ZW("فَأَنَا أَبْكِي الْيَوْمَ ذَاهِبَ الْعَقْلِ؛ الدَّلْهُ: ذَهَابُ الْعَقْلِ", "«so today I weep, my wits gone»; دَلْه is the loss of one's wits", "«bugün aklım gitmiş ağlıyorum»; «delh»: aklın gitmesi"))),
  PT("وَمَا", "ma-istifham", "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَأَجَازَ الدُّرَّةُ أَنْ يَكُونَ مَفْعُولًا بِهِ مُقَدَّمًا لِـ«يُحِيرُ»، وَقَالَ: الِاسْتِئْنَافُ أَقْوَى مِنَ الْعَطْفِ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى النَّفْيِ: قَالَ الزَّوْزَنِيُّ: «وَهٰذَا اسْتِفْهَامٌ يَتَضَمَّنُ الْجُحُودَ، أَيْ لَا يَرُدُّ الْبُكَاءُ عَلَى صَاحِبِهِ فَائِتًا»",
     "a question noun built on sukun, in the seat of raf' as mubtada — al-Durra allows it to be the fronted object of «gives back», and holds a fresh start stronger than conjoining — the question has left asking for denial: al-Zawzanī: «this is a question that holds a denial: weeping gives back nothing lost to the one who weeps»",
     "sükûn üzere mebnî istifhâm ismi, mübtedâ olarak mahallen merfû — Dürre «geri getirir»in öne alınmış mef'ûlü olmasını da caiz görür ve isti'nâfı atıftan kuvvetli sayar — burada istifhâm nefy anlamına çıkmıştır: Zevzenî: «bu inkâr içeren bir sorudur: ağlamak, sahibine kaybettiğini geri getirmez»",
     c="w", g=["al-istifham", "khuruj-al-istifham", "mubtada-khabar"], pos="pron"),
  V("d", "يُحِيرُ", "ahara-hr", g=["form-iv-verbs", "hollow-verbs"], n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَا»، وَالرَّابِطُ مَحْذُوفٌ: يُحِيرُهُ", "the clause is the khabar of «what», in the seat of raf'; the link is left out: «gives it back»", "cümle «mâ»nın haberi, mahallen merfû; bağlayıcı zamir mahzûftur: «onu geri getirir»"),
     ZW("الْإِحَارَةُ: الرَّدُّ، مِنْ: حَارَ الشَّيْءُ يَحُورُ حَوْرًا إِذَا رَجَعَ", "إِحَارَة is giving back, from حَارَ يَحُورُ «to return»", "«ihâre»: geri vermek; «hâra yehûru»: döndü'den"), DR("وَرِوَايَتُهُ «وَمَا يَرُدُّ»، وَذَكَرَ «يُحِيرُ» رِوَايَةً", "his text reads «يَرُدُّ», with «يُحِيرُ» as a variant", "onun rivayeti «yeruddu»dur; «yuhîru»yu rivayet olarak anar"))),
  R("fail", "الْبُكَاءُ", "buka", n=QAF)])
VV(6, "Before your eyes Hind lit the fire at last, the high ground lifting it up to you.",
  "Hind ateşi en son, senin gözlerinin önünde yaktı; yüksek yer onu sana doğru kaldırıp işaret ediyordu.",
 [R("majr", "وَبِعَيْنَيْكَ", "ayn-eye", c="wi", j="bi", enc="كَ", sign=("بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, a dual whose nun drops in the idafa", " — tesniye olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["al-muthanna", "tajrid", "taqdim-al-musnad"],
    n=N3(MT("أَوْقَدَتْ", "lit", "yaktı»ya"), NT("وَتَقَدَّمَ عَلَى فِعْلِهِ", "it stands before its verb", "fiilinden önce gelmiştir"),
     DR("وَفِيهِ تَجْرِيدٌ: الْكَافُ لِلْخِطَابِ وَالْمُرَادُ نَفْسُهُ، جَرَّدَ مِنْ نَفْسِهِ شَخْصًا وَخَاطَبَهُ — وَكَذٰلِكَ الزَّوْزَنِيُّ: «يُخَاطِبُ نَفْسَهُ»", "a tajrīd: the kaf is address, and he means himself — he drew another person out of himself and spoke to him; so also al-Zawzanī: «he addresses himself»", "tecrîd: kâf hitaptır ve kendini kastediyor — kendinden bir şahıs soyutlayıp ona hitap etti; Zevzenî de: «kendine hitap ediyor»"))),
  V("mt", "أَوْقَدَتْ", "awqada", g=["form-iv-verbs", "mithal-verbs"], n=CL("ist")),
  NAME("fail", "هِنْدٌ", "hind", n=NT("وَصُرِفَ لِأَنَّهُ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ", "given tanwin, being a three-letter name with a quiescent middle", "orta harfi sâkin üç harfli isim olduğu için munsarif kılınmıştır"))],
 [R("maf", "النَّارَ", "nar"),
  R("zarfz", "أَخِيرًا", "akhir-last", n=N3(MZ("أَوْقَدَتْ", "lit", "yaktı»ya"), DR("أَيْ عِنْدَ آخِرِ عَهْدِهِ بِهَا، وَيُرْوَى «أَصِيلًا»", "that is, at the last of his time with her; also related «at evening»", "yani onunla son buluşmasında; «asîlen» diye de rivayet edilir"))),
  V("dy", "تُلْوِي", "alwa", g=["form-iv-verbs", "naqis-verbs"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «النَّارَ»، وَالرَّابِطُ الضَّمِيرُ فِي «بِهَا»", "the clause is a hal of «the fire», in the seat of nasb; the link is the pronoun in «with it»", "cümle «ateş»ten hâl, mahallen mansûb; bağlayıcı «bihâ»daki zamirdir"), ZW("أَلْوَى بِالشَّيْءِ: أَشَارَ بِهِ", "أَلْوَى بِالشَّيْءِ is to signal with a thing", "«elvâ bi'ş-şey'»: onunla işaret etti"))),
  JP("بِهَا", "bi", "هَا", n=MT("تُلْوِي", "lifts", "kaldırır»a")),
  R("fail", "الْعَلْيَاءُ", "alya", g=["majaz-aqli"], n=N3(QAF, ZW("الْعَلْيَاءُ: الْبُقْعَةُ الْعَالِيَةُ؛ وَكَأَنَّ الْبُقْعَةَ الْعَالِيَةَ الَّتِي أَوْقَدَتْهَا عَلَيْهَا كَانَتْ تُشِيرُ إِلَيْكَ بِهَا", "العَلْيَاء is the high ground: as though the height on which she lit it were beckoning you with it", "«aleyâ»: yüksek yer; sanki ateşi üzerinde yaktığı yüksek yer onunla sana işaret ediyordu"),
     HADD("مَجَازٌ عَقْلِيٌّ: أُسْنِدَ الْإِلْوَاءُ إِلَى الْمَكَانِ الَّذِي وَقَعَ فِيهِ، وَإِنَّمَا تُرْفَعُ النَّارُ عَلَيْهِ — وَصَفَهُ الزَّوْزَنِيُّ بِـ«كَأَنَّ»", "a majāz ʿaqlī: the beckoning is assigned to the place where it happens, though the fire is only raised upon it — al-Zawzanī describes it with «as though»", "mecâz-ı aklî: işaret etme, gerçekleştiği yere isnad edilmiştir; oysa ateş yalnızca onun üzerinde yükselir — Zevzenî bunu «sanki» ile tarif eder")))])
VV(7, "I gazed at her fire from far off at Khazāzā — how far from you is the warming at it!",
  "Hazâzâ'da onun ateşine uzaktan baktım — ona ısınmak senden ne kadar uzak!",
 [V("mtu", "فَتَنَوَّرْتُ", "tanawwara-hr", c="f", g=["form-v-verbs"], n=N3(DR("وَيَجُوزُ أَنْ تَكُونَ الْفَاءُ لِلِاسْتِئْنَافِ", "the fa may also open a fresh sentence", "fâ isti'nâf için de olabilir"), ZW("التَّنَوُّرُ: النَّظَرُ إِلَى النَّارِ", "تَنَوُّر is looking at a fire", "«tenevvür»: ateşe bakmak"))),
  R("maf", "نَارَهَا", "nar", enc="هَا"),
  PR("مِنْ", "min", n=MT("تَنَوَّرْتُ", "I gazed", "baktım»a")),
  R("majr", "بَعِيدٍ", "baid")],
 [NAME("majr", "بِخَزَازَى", "khazaza-amr", j="bi", sign=S_DIPT_Q, g=["mamnu-min-sarf", "ism-maqsur-manqus"], n=N3(MT("تَنَوَّرْتُ", "I gazed", "baktım»a"), DR("وَيَجُوزُ تَعَلُّقُهُمَا بِمَحْذُوفٍ حَالٍ مِنْ «نَارَهَا»؛ وَرِوَايَتُهُ «بِخَزَازٍ»، وَيُرْوَى «خَزَازَى»", "the phrase may also hang on an omitted hal of «her fire»; his text reads «بِخَزَازٍ», with «خَزَازَى» as a variant", "câr-mecrûr «ateşi»nden mahzûf bir hâle de müteallik olabilir; onun rivayeti «bi-Hazâzin», «Hazâzâ» diye de rivayet edilir"))),
  PT("هَيْهَاتَ", "hayhat", "اسْمُ فِعْلٍ مَاضٍ بِمَعْنَى «بَعُدَ» مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ هَيْهَاتَ: بَعُدَ الْأَمْرُ جِدًّا (الزَّوْزَنِيُّ)", "a verbal noun of the past meaning «it is far», built on fatha, with no seat — a fresh sentence; هَيْهَاتَ: the thing is very far (al-Zawzanī)", "«uzaktır» anlamında mâzî ism-i fiil, fetha üzere mebnî, mahalli yok — cümle müste'nefedir; «heyhâte»: iş çok uzaklaştı (Zevzenî)", g=["ism-fil", "asma-al-afal-wal-aswat-wal-murakkabat"], pos="noun"),
  JP("مِنْكَ", "min", "كَ", g=["tajrid"], n=N3(MT("هَيْهَاتَ", "far is", "uzaktır»a"), DR("وَهُوَ يُخَاطِبُ نَفْسَهُ، كَالتَّجْرِيدِ فِي الْبَيْتِ قَبْلَهُ", "he speaks to himself, the tajrīd of the verse before", "kendine hitap eder; önceki beyitteki tecrîd gibi"))),
  R("fail", "الصِّلَاءُ", "sila-hr", n=N3(NT("فَاعِلُ «هَيْهَاتَ»", "the doer of «far is»", "«heyhâte»nin fâili"), QAF, ZW("الصِّلَاءُ: مَصْدَرُ صَلِيَ بِالنَّارِ إِذَا احْتَرَقَ بِهَا أَوْ نَالَهُ حَرُّهَا", "صِلَاء is the masdar of صَلِيَ بِالنَّارِ, to be burnt by a fire or reached by its heat", "«sılâ»: ateşle yanmak ya da sıcaklığına ulaşmak anlamındaki «saliye»nin masdarı")))])
VV(8, "She lit it between al-ʿAqīq and Shakhṣān with a stick of wood, and it shone as the light shines.",
  "Onu Akîk ile Şahsân arasında bir odunla yaktı; ışık nasıl parlarsa öyle parladı.",
 [V("mt", "أَوْقَدَتْهَا", "awqada", enc="هَا", doer=HIYA("هِنْدٍ", "Hind", "Hind'e"), g=["form-iv-verbs", "mithal-verbs"], n=DR("وَالْجُمْلَةُ بَدَلٌ مِنْ جُمْلَةِ «أَوْقَدَتْ هِنْدٌ النَّارَ» لَا مَحَلَّ لَهَا مِثْلُهَا", "the clause is a badal of «Hind lit the fire» and, like it, has no seat", "cümle «Hind ateşi yaktı» cümlesinden bedeldir; o da mahalsizdir")),
  R("zarfm", "بَيْنَ", "bayna", mud=True, n=MZ("أَوْقَدَتْ", "lit", "yaktı»ya")),
  PLACE("mdf", "الْعَقِيقِ", "aqiq-hr", c=None, n=DR("وَادٍ بِظَاهِرِ الْمَدِينَةِ", "a valley outside Medina", "Medine'nin dışında bir vadi"))],
 [PLACE("atfj", "فَشَخْصَيْنِ", "shakhsan-hr", sign=S_MUTHY, g=["al-muthanna"], n=DR("أَكَمَةٌ لَهَا شُعْبَتَانِ، عَلَى صِيغَةِ الْمُثَنَّى", "a hillock with two prongs, in the form of a dual", "iki çatallı bir tepecik; tesniye kalıbında")),
  R("majr", "بِعُودٍ", "ud", j="bi", n=MT("أَوْقَدَتْ", "lit", "yaktı»ya")),
  PT("كَمَا", "ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «مَا» وَ«يَلُوحُ» مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ مَعَ فِعْلِهِ: فَلَاحَتْ لَوْحًا كَلَوْحِ الضِّيَاءِ (الدُّرَّةُ) — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ لَوْحُ النَّارِ، وَالْمُشَبَّهُ بِهِ لَوْحُ الضِّيَاءِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ — الْإِشْرَاقُ يُرَى مِنْ بَعِيدٍ — غَيْرُ مَذْكُورٍ؛ وَهُوَ قَوْلُ الزَّوْزَنِيِّ: «فَلَاحَتْ كَمَا يَلُوحُ الضِّيَاءُ»",
     "the kaf is the jarr letter of likening and «mā» makes a masdar: «mā» with «shines» is a masdar in jarr after the kaf, and the phrase hangs on the omitted adjective of an absolute object dropped with its verb — «and it shone with a shining like the light's» (al-Durra) — a tashbih mursal mujmal: the fire's shining is likened to the shining of light; the particle is the kaf; the point of likeness — a brightness seen from afar — is not stated; it is al-Zawzanī's «and it shone as the light shines»",
     "kâf teşbîh ve cer harfi, «mâ» masdariyyedir: «mâ» ile «parlar» kâf ile mecrûr bir masdardır; câr-mecrûr fiiliyle birlikte hazfedilmiş bir mef'ûl-i mutlakın mahzûf sıfatına müteallik: «ışığın parlaması gibi bir parlamayla parladı» (Dürre) — teşbîh-i mürsel mücmel: ateşin parlaması ışığın parlamasına benzetilmiştir; edat kâf; vech-i şebeh — uzaktan görünen parlaklık — zikredilmemiştir; Zevzenî: «ışık nasıl parlarsa öyle parladı»",
     pos="prep", g=TB + ["huruf-jarr", "maful-mutlaq"], segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part"))),
  V("d", "يَلُوحُ", "laha-verb", g=["hollow-verbs"]),
  R("fail", "الضِّيَاءُ", "diya-hr", n=N3(QAF, DR("قِيلَ: ضِيَاءُ الْفَجْرِ، وَقِيلَ: ضِيَاءُ النَّارِ", "said to be the light of dawn, or of a fire", "fecrin ya da bir ateşin ışığı olduğu söylenmiştir")))])
# =====================================================================================================================
# The poem — vv. 9–14 — الزَّفُوفُ
# =====================================================================================================================
S_DIPT_MR = ("بِالضَّمَّةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", " — by the damma, without tanwin: a diptote, for its feminine alif mamduda", " — damme ile, tenvinsiz: memdûde te'nîs elifi sebebiyle gayr-i munsarif")
HIQLA = HIYA("الْهِقْلَةِ", "the ostrich", "deve kuşuna")
VV(9, "But I seek help against care — when speed sweeps off even the one who stays —",
  "Ama ben kedere karşı yardım dilerim — sürat, yerinde oturanı bile alıp götürdüğünde —",
 [T("غَيْرَ", "ghayr", "noun", ["istithna", "idafa-definiteness", "husn-al-ibtida-wal-takhallus-wal-intiha"],
    "مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ الْمُنْقَطِعِ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، مُضَافٌ — وَقِيلَ: مَنْصُوبٌ عَلَى الْحَالِ (الدُّرَّةُ)؛ وَمَعْنَاهُ: لٰكِنِّي (الزَّوْزَنِيُّ) — وَفِيهِ التَّخَلُّصُ: قَالَ الزَّوْزَنِيُّ: «انْتَقَلَ مِنَ النَّسِيبِ إِلَى ذِكْرِ حَالِهِ فِي طَلَبِ الْمَجْدِ»، وَتَسْمِيَتُهُ عَلَى حَدِّ التَّلْخِيصِ.",
    "In nasb as a cut-off exception, its sign the fatha, annexed — others: in nasb as a hal (al-Durra); it means «but I» (al-Zawzanī) — here is the takhalluṣ, the passage to the purpose: al-Zawzanī: «he moves from the love-prelude to his own state in seeking glory»; the name is by the Talkhīṣ's definition.",
    "Munkatı istisna olarak mansûb, alâmeti fetha, muzâf — hâl olarak mansûb olduğu da söylenmiştir (Dürre); anlamı «lâkin ben»dir (Zevzenî) — burada tahallus (maksada geçiş) vardır: Zevzenî: «nesîbden şeref arayışındaki hâlini anmaya geçti»; adlandırma Telhîs'in tarifine göredir."),
  T("أَنِّي", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "ya-al-mutakallim"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» وَاسْمِهَا وَخَبَرِهَا فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «غَيْرَ» إِلَيْهِ.",
    "أَنَّ is the particle of emphasis that puts its noun in nasb; the ya is its noun, in the seat of nasb — أَنَّ with its noun and predicate makes a masdar, in the seat of jarr, «other than» being annexed to it.",
    "Enne: te'kîd ve nasb harfi; yâ ismidir, mahallen mansûb — «enne», ismi ve haberi «gayr»ın kendisine muzâf olmasıyla mahallen mecrûr bir masdar olur.", segs=SG(("أَنِّ", "anna", "part"), ("ي", "pron-1s", "pron"))),
  QAD(),
  V("d", "أَسْتَعِينُ", "istaana", doer=ANA, g=["form-x-verbs", "hollow-verbs"], n=CL("khb", "أَنَّ", "أَنَّ", "enne")),
  PR("عَلَى", "ala", n=MT("أَسْتَعِينُ", "I seek help", "yardım dilerim»e")),
  R("majr", "الْهَمِّ", "hamm")],
 [IDHA(plain=True, n=N3(MZ("أَسْتَعِينُ", "I seek help", "yardım dilerim»e"), DR("وَإِنْ جُعِلَتْ شَرْطِيَّةً فَجَوَابُهَا مَحْذُوفٌ: إِذَا خَفَّ … فَأَنَا أَسْتَعِينُ، وَهِيَ وَمَدْخُولُهَا مُعْتَرِضَةٌ", "if it is taken as conditional, its answer is left out — «when … then I seek help» — and it with its clause is a parenthesis", "şartiyye sayılırsa cevabı mahzûftur: «… olduğunda yardım dilerim»; o ve girdiği cümle mu'tarızadır"))),
  V("m", "خَفَّ", "lb-khaffa", g=["doubled-verbs", "kinaya"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"),
     NT("وَفِيهِ كِنَايَةٌ عَنْ عِظَمِ الْخَطْبِ: قَالَ الزَّوْزَنِيُّ: «إِذَا أَسْرَعَ الْمُقِيمُ فِي السَّيْرِ لِعِظَمِ الْخَطْبِ وَفَظَاعَةِ الْخَوْفِ»", "a kināya for the gravity of the crisis: al-Zawzanī: «when even the one who stays hurries off, for the greatness of the matter and the horror of the fear»", "işin büyüklüğünden kinaye: Zevzenî: «işin büyüklüğü ve korkunun dehşetinden yerinde oturan bile yola koyulduğunda»"))),
  R("majr", "بِالثَّوِيِّ", "thawiyy-hr", j="bi", n=N3(MT("خَفَّ", "swept off", "hafifletti»ye"), ZW("الثَّوِيُّ وَالثَّاوِي: الْمُقِيمُ، وَالْبَاءُ لِلتَّعْدِيَةِ", "ثَوِيّ and ثَاوٍ are one who stays; the ba makes the verb transitive", "«sevîy» ve «sâvî»: ikamet eden; bâ ta'diye içindir"))),
  R("fail", "النَّجَاءُ", "naja-speed-tf", n=N3(QAF, ZW("النَّجَاءُ: الْإِسْرَاعُ فِي السَّيْرِ", "نَجَاء is speed in going", "«necâ»: yürüyüşte hızlanmak")))])
VV(10, "with a swift-paced she-camel, as though she were an ostrich, mother of young ostriches of the waste, tall and stooping,",
  "seğirten bir deveyle; sanki o, çöl yavrularının anası, uzun boylu, eğik bir dişi deve kuşudur;",
 [R("majr", "بِزَفُوفٍ", "zafuf-hr", j="bi", g=["sighat-mubalagha", "hadhf-wa-taqdir", "istiara", "istiara-tabaiyya"], n=N3(MT("أَسْتَعِينُ", "I seek help", "yardım dilerim»e"), DR("وَ«زَفُوفٌ» صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: بِنَاقَةٍ زَفُوفٍ", "«swift-paced» is the adjective of an omitted noun: «with a she-camel swift-paced»", "«zefûf» mahzûf bir mevsûfun sıfatıdır: «seğirten bir deveyle»"),
     NT("وَفِيهِ اسْتِعَارَةٌ: قَالَ الزَّوْزَنِيُّ: «الزَّفِيفُ: إِسْرَاعُ النَّعَامَةِ فِي سَيْرِهَا، ثُمَّ يُسْتَعَارُ لِسَيْرِ غَيْرِهَا… وَالزَّفُوفُ مُبَالَغَةٌ»؛ وَهِيَ — عَلَى حَدِّ التَّلْخِيصِ — تَبَعِيَّةٌ لِأَنَّهَا فِي صِفَةٍ مُشْتَقَّةٍ", "an istiʿāra: al-Zawzanī: «زَفِيف is the ostrich's speed in going, then it is borrowed for the going of others … and زَفُوف is the intensive»; by the Talkhīṣ's definition it is tabaʿiyya, being in a derived adjective", "istiâre: Zevzenî: «zefîf, deve kuşunun hızlı yürüyüşüdür, sonra başkalarının yürüyüşü için istiâre edilir… zefûf mübalağadır»; Telhîs'in tarifine göre türemiş bir sıfatta olduğu için tebeiyyedir"))),
  KAANNA("كَأَنَّهَا", enc="هَا", g=TB, n=N3(DR("وَجُمْلَةُ «كَأَنَّهَا …» صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "the clause «as though she …» is a second adjective of the omitted noun", "«sanki o…» cümlesi mahzûf mevsûfun ikinci sıfatıdır"),
     NT("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ النَّاقَةُ، وَالْمُشَبَّهُ بِهِ الْهِقْلَةُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الْإِسْرَاعُ — ذَكَرَهُ الزَّوْزَنِيُّ: «كَأَنَّهَا فِي إِسْرَاعِهَا فِي السَّيْرِ نَعَامَةٌ»", "a tashbih mursal mujmal: the she-camel is likened to the ostrich; the particle is كَأَنَّ; the point of likeness — speed — is al-Zawzanī's: «as though, in her speed, she were an ostrich»", "teşbîh-i mürsel mücmel: müşebbeh deve, müşebbehün bih dişi deve kuşu, edat «keenne»; vech-i şebeh — hız — Zevzenî'dedir: «hızında sanki bir deve kuşu»"))),
  R("khbka", "هِقْلَةٌ", "hiqla-hr", n=ZW("الْهِقْلَةُ: النَّعَامَةُ، وَالظَّلِيمُ هِقْلٌ", "هِقْلَة is the female ostrich; the male is هِقْل", "«hıkle»: dişi deve kuşu; erkeği «hıkl»"))],
 [R("naatr", "أُمُّ", "umm", mud=True, of=("هِقْلَةٌ", "ostrich", "hıkle")),
  R("mdf", "رِئَالٍ", "ral-hr", g=["jam-taksir"], n=ZW("الرَّأْلُ: وَلَدُ النَّعَامَةِ، وَالْجَمْعُ رِئَالٌ", "رَأْل is the ostrich's young; the plural is رِئَال", "«ra'l»: deve kuşu yavrusu; çoğulu «riâl»")),
  R("naatj", "دَوِّيَّةٍ", "dawwiyy-hr", g=["ism-mansub"], of=("رِئَالٍ", "young ostriches", "riâl"), n=N3(DR("وَعِنْدَ الدُّرَّةِ «دَوِّيَّةٌ» صِفَةٌ ثَانِيَةٌ لِـ«هِقْلَةٌ»", "al-Durra makes «of the waste» a second adjective of «ostrich» (in raf')", "Dürre'de «devviyye», «hıkle»nin ikinci sıfatıdır (merfû)"), ZW("الدَّوِّيَّةُ: مَنْسُوبَةٌ إِلَى الدَّوِّ، وَهِيَ الْمَفَازَةُ", "دَوِّيَّة is «of the dawww», the waterless waste", "«devviyye»: «devv»e, yani susuz çöle mensup"))),
  R("naatr", "سَقْفَاءُ", "saqfa-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("هِقْلَةٌ", "ostrich", "hıkle"), n=N3(QAF, ZW("السَّقَفُ: طُولٌ مَعَ انْحِنَاءٍ، وَالنَّعْتُ أَسْقَفُ", "سَقَف is height with a stoop; the adjective is أَسْقَف", "«sakaf»: eğiklikle beraber uzunluk; sıfatı «eskaf»")))])
VV(11, "She has caught a faint sound, and the hunters have frightened her, late in the day, with evening drawing near.",
  "Gizli bir ses sezmiş, avcılar da onu ikindi vakti ürkütmüştür; akşam da yaklaşmıştır.",
 [V("mt", "آنَسَتْ", "anasa", doer=HIQLA, g=["form-iv-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «هِقْلَةٌ» بَعْدَ وَصْفِهَا، وَالْعَامِلُ «كَأَنَّ» لِمَا فِيهَا مِنْ مَعْنَى الْفِعْلِ؛ وَتَجُوزُ الْوَصْفِيَّةُ وَالِاسْتِئْنَافُ", "the clause is a hal of «ostrich» after its description, in the seat of nasb, governed by كَأَنَّ for the verbal sense in it; an adjective or a fresh start is also allowed", "cümle, sıfatlarından sonra «hıkle»den hâl olarak mahallen mansûbdur; âmili, fiil mânâsı taşıdığı için «keenne»dir; sıfat ve isti'nâf da caizdir")),
  R("maf", "نَبْأَةً", "nabaa-hr", n=ZW("النَّبْأَةُ: الصَّوْتُ الْخَفِيُّ يَسْمَعُهُ الْإِنْسَانُ أَوْ يَتَخَيَّلُهُ", "نَبْأَة is a faint sound that one hears or imagines", "«neb'e»: insanın duyduğu ya da duyar gibi olduğu gizli ses")),
  V("m", "وَأَفْزَعَهَا", "afzaa", c="w", enc="هَا", g=["form-iv-verbs"], n=N3(CL("atf", "آنَسَتْ", "she caught", "sezdi"), ZW("الْإِفْزَاعُ: الْإِخَافَةُ", "إِفْزَاع is frightening", "«ifzâ»: korkutmak")))],
 [R("fail", "الْقُنَّاصُ", "qanis", g=["jam-taksir"], n=ZW("الْقُنَّاصُ: جَمْعُ قَانِصٍ، وَهُوَ الصَّائِدُ", "قُنَّاص is the plural of قَانِص, a hunter", "«kunnâs»: «kânıs»ın, yani avcının çoğulu")),
  R("zarfz", "عَصْرًا", "asr", n=N3(MZ("أَفْزَعَ", "frightened", "ürküttü»ye"), ZW("الْعَصْرُ: الْعَشِيُّ", "عَصْر here is the late afternoon", "«asr»: ikindi vakti"))),
  QAD("وَقَدْ", c="wh"),
  V("ma", "دَنَا", "dana", g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الْقُنَّاصُ» أَوْ مِنَ الضَّمِيرِ فِي «أَفْزَعَهَا»، وَالرَّابِطُ الْوَاوُ", "the clause is a hal of «the hunters» or of the object pronoun in «frightened her», in the seat of nasb; the waw is the link", "cümle «avcılar»dan ya da «onu ürküttü»deki zamirden hâl, mahallen mansûb; bağlayıcı vâvdır")),
  R("fail", "الْإِمْسَاءُ", "imsa-hr", g=["masdar"], n=N3(QAF, ZW("لَمَّا شَبَّهَ نَاقَتَهُ بِالنَّعَامَةِ بَالَغَ فِي وَصْفِ النَّعَامَةِ بِالْإِسْرَاعِ: تَئُوبُ إِلَى أَوْلَادِهَا مَعَ إِحْسَاسِهَا بِالصَّيَّادِينَ وَقُرْبِ الْمَسَاءِ، فَهٰذِهِ الْأَسْبَابُ تَزِيدُهَا إِسْرَاعًا", "having likened his camel to the ostrich, he heightens the ostrich's speed: she heads back to her young, sensing the hunters and the coming evening — causes that add to her haste", "devesini deve kuşuna benzetince, deve kuşunun hızını vurgular: avcıları sezerek ve akşamın yaklaşmasıyla yavrularına döner; bu sebepler hızını artırır")))])
VV(12, "Behind her you see, from the fall and strike of her feet, a fine dust, as though it were dust stirred up.",
  "Ayaklarını kaldırıp yere vurmasından ardında ince bir toz görürsün; sanki savrulan bir tozdur.",
 [V("da", "فَتَرَى", "raa", c="fi", doer=ANTA, g=["naqis-verbs"], n=N3(CL("ist"), ZW("فَتَرَى أَنْتَ أَيُّهَا الْمُخَاطَبُ", "«you see» — you, whoever is addressed", "«görürsün» — sen, ey muhatap"))),
  R("zarfm", "خَلْفَهَا", "khalf", enc="هَا", n=N3(MZ("تَرَى", "you see", "görürsün»e"), ZW("خَلْفَ هٰذِهِ النَّاقَةِ", "behind this she-camel", "bu devenin ardında"))),
  PR("مِنَ", "min", n=MT("تَرَى", "you see", "görürsün»e")),
  R("majr", "الرَّجْعِ", "lb-raj", n=ZW("مِنْ رَجْعِهَا قَوَائِمَهَا وَضَرْبِهَا الْأَرْضَ بِهَا", "from her bringing back her legs and striking the ground with them", "ayaklarını geri çekip onlarla yere vurmasından"))],
 [R("atfj", "وَالْوَقْعِ", "waq-ant", c="w", of=("الرَّجْعِ", "the fall", "er-rec'"), g=["masdar"]),
  R("maf", "مَنِينًا", "manin-hr", n=ZW("الْمَنِينُ: الْغُبَارُ الرَّقِيقُ؛ وَجَعْلُهُ رَقِيقًا إِشَارَةٌ إِلَى غَايَةِ إِسْرَاعِهَا", "مَنِين is fine dust; making it fine points to the height of her speed", "«menîn»: ince toz; onu ince kılması, hızının son derecesine işarettir")),
  KAANNA("كَأَنَّهُ", enc="هُ", g=TB, n=N3(CL("nn", "مَنِينًا", "fine dust", "menînen»"),
     NT("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْغُبَارُ الرَّقِيقُ، وَالْمُشَبَّهُ بِهِ الْإِهْبَاءُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الرِّقَّةُ وَالِانْبِثَاثُ — مِنْ قَوْلِ الزَّوْزَنِيِّ: «غُبَارًا رَقِيقًا كَأَنَّهُ هَبَاءٌ مُنْبَثٌّ»", "a tashbih mursal mujmal: the fine dust is likened to dust stirred up; the particle is كَأَنَّ; the point of likeness — fineness and scattering — is from al-Zawzanī: «a fine dust, as though it were scattered motes»", "teşbîh-i mürsel mücmel: müşebbeh ince toz, müşebbehün bih savrulan toz, edat «keenne»; vech-i şebeh — incelik ve dağılma — Zevzenî'nin sözündendir: «sanki dağılmış zerreler»"))),
  R("khbka", "إِهْبَاءُ", "ihba-hr", g=["masdar"], n=N3(QAF_N, ZW("الْأَهْبَاءُ: جَمْعُ هَبَاءٍ، وَالْإِهْبَاءُ: إِثَارَتُهُ", "أَهْبَاء is the plural of هَبَاء, and إِهْبَاء is raising it", "«ehbâ» «hebâ»nın çoğuludur, «ihbâ» ise onu kaldırmaktır")))])
VV(13, "and sole-pieces, with more sole-pieces behind them, dropped, which the desert has worn away.",
  "ve ardında başka taban parçaları bulunan, düşmüş taban parçaları görürsün; çöl onları tüketmiştir.",
 [R("atfn", "وَطِرَاقًا", "tiraq-hr", c="w", of=("مَنِينًا", "fine dust", "menînen"), n=ZW("الطِّرَاقُ: يُرِيدُ بِهَا أَطْبَاقَ نَعْلِهَا", "by طِرَاق he means the layers of her sole", "«tırâk» ile tabanının katmanlarını kastediyor")),
  PR("مِنْ", "min", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "خَلْفِهِنَّ", "khalf", enc="هِنَّ"),
  R("mub", "طِرَاقٌ", "tiraq-hr", n=NT("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«طِرَاقًا»", "placed after its khabar; the nominal clause is a na't of «sole-pieces», in the seat of nasb", "sona bırakılmıştır; isim cümlesi «tırâken»in na'tı, mahallen mansûb"))],
 [R("naatr", "سَاقِطَاتٌ", "saqit-hr", g=["jam-muannath-salim", "ism-fail"], of=("طِرَاقٌ", "sole-pieces", "tırâk")),
  V("mtq", "أَلْوَتْ", "alwa", g=["form-iv-verbs", "naqis-verbs", "majaz-aqli"], n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«طِرَاقٌ»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ", "the clause is a second na't of «sole-pieces», in the seat of raf', or a hal of it, in the seat of nasb", "cümle «tırâk»ın ikinci na'tı olarak mahallen merfû, ya da ondan hâl olarak mahallen mansûb"),
     DR("وَرِوَايَتُهُ «تُلْوِي»", "his text reads «تُلْوِي»", "onun rivayeti «tulvî»dir"), ZW("أَلْوَى بِالشَّيْءِ: أَفْنَاهُ وَأَبْطَلَهُ", "أَلْوَى بِالشَّيْءِ is to wear a thing away, to destroy it", "«elvâ bi'ş-şey'»: onu tüketti, yok etti"))),
  JP("بِهَا", "bi", "هَا", n=MT("أَلْوَتْ", "wore away", "tüketti»ye")),
  R("fail", "الصَّحْرَاءُ", "sahra", n=N3(QAF, ZW("قَدْ قَطَعَهَا وَأَبْطَلَهَا قَطْعُ الصَّحْرَاءِ وَوَطْؤُهَا", "the crossing and treading of the desert cut them off and wore them away", "çölü kat edip çiğnemek onları koparıp tüketmiştir"),
     HADD("مَجَازٌ عَقْلِيٌّ: أُسْنِدَ الْإِفْنَاءُ إِلَى الصَّحْرَاءِ، وَهِيَ مَكَانُهُ، وَإِنَّمَا أَفْنَاهَا قَطْعُهَا وَوَطْؤُهَا كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "a majāz ʿaqlī: the wearing away is assigned to the desert, its place, though it was the crossing and treading of it that wore them, as al-Zawzanī explains", "mecâz-ı aklî: tüketme, onun mekânı olan çöle isnad edilmiştir; oysa onları tüketen, Zevzenî'nin açıkladığı gibi, çölü kat etmek ve çiğnemektir")))])
VV(14, "On her I make sport of the midday heats, when every man of care is a blind tethered camel.",
  "Her dertli kişinin, kabre bağlanmış kör bir deve gibi şaşkın kaldığı vakit, ben onunla öğle sıcaklarında eğlenirim.",
 [V("da", "أَتَلَهَّى", "talahha-hr", doer=ANA, g=["form-v-verbs", "naqis-verbs"], n=N3(CL("ist"), ZW("أَتَلَعَّبُ بِهَا فِي أَشَدِّ مَا يَكُونُ مِنَ الْحَرِّ", "I play with her in the fiercest of the heat", "sıcağın en şiddetlisinde onunla oynarım"))),
  JP("بِهَا", "bi", "هَا", n=MT("أَتَلَهَّى", "I make sport", "eğlenirim»e")),
  T("الْهَوَاجِرَ", "hajira-ant", "noun", ["hadhf-al-jarr", "jam-taksir"], "مَنْصُوبٌ عَلَى نَزْعِ الْخَافِضِ (أَيْ: فِي الْهَوَاجِرِ)، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ (الدُّرَّةُ).",
    "In nasb by the dropping of the jarr letter («in the midday heats»), its sign the fatha (al-Durra).", "Cer harfinin düşmesiyle («öğle sıcaklarında») mansûb, alâmeti fetha (Dürre)."),
  PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«أَتَلَهَّى»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb of past time built on sukun, in the seat of nasb, hanging on «I make sport» and annexed to the clause after it", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «eğlenirim»e müteallik, sonraki cümleye muzâf", g=["maful-fih"], pos="noun"),
  R("mub", "كُلُّ", "kull", mud=True)],
 [R("mdf", "ابْنِ", "ibn", mud=True),
  R("mdf", "هَمٍّ", "hamm"),
  R("khb", "بَلِيَّةٌ", "lb-baliyya", g=TB, n=N3(NT("وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذْ» إِلَيْهَا", "the nominal clause is in the seat of jarr, إِذْ being annexed to it", "isim cümlesi, «iz» kendisine muzâf olduğu için mahallen mecrûr"),
     HADD("تَشْبِيهٌ بَلِيغٌ: الْمُشَبَّهُ ابْنُ الْهَمِّ، وَالْمُشَبَّهُ بِهِ الْبَلِيَّةُ الْعَمْيَاءُ، حُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ، وَوَجْهُهُ التَّحَيُّرُ كَمَا شَرَحَهُ الزَّوْزَنِيُّ: «إِذَا تَحَيَّرَ صَاحِبُ كُلِّ هَمٍّ تَحَيُّرَ النَّاقَةِ الْبَلِيَّةِ الْعَمْيَاءِ»", "a tashbih baligh: the man of care is likened to the blind tethered camel, with particle and point left out; the point is bewilderment, as al-Zawzanī explains: «when every man of care is bewildered as the blind tethered camel is bewildered»", "teşbîh-i belîğ: müşebbeh dertli kişi, müşebbehün bih kör «beliyye» deve; edat ve vech-i şebeh hazfedilmiştir; vech şaşkınlıktır, Zevzenî'nin açıkladığı gibi: «her dertli, kör beliyye devenin şaşırdığı gibi şaşırdığında»"))),
  R("naatr", "عَمْيَاءُ", "ama-blind", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("بَلِيَّةٌ", "tethered camel", "beliyye"), n=QAF)])
# =====================================================================================================================
# The poem — vv. 15–21 — الْأَرَاقِمُ
# =====================================================================================================================
VV(15, "There has come to us, of the events and the tidings, a grave matter that troubles us and grieves us:",
  "Olaylardan ve haberlerden bize, bizi uğraştıran ve üzen büyük bir iş geldi:",
 [V("ma", "وَأَتَانَا", "ata", c="wi", enc="نَا", g=["naqis-verbs"], n=N3(CL("ist"), DR("وَرِوَايَتُهُ: «وَأَتَانَا عَنِ الْأَرَاقِمِ أَنْبَاءٌ وَخَطْبٌ»", "his text reads «there came to us, of the Arāqim, tidings and a grave matter»", "onun rivayeti: «Erâkım'dan bize haberler ve büyük bir iş geldi»"))),
  PR("مِنَ", "min", n=MT("أَتَى", "came", "geldi»ye")),
  R("majr", "الْحَوَادِثِ", "haditha-hr", g=["jam-taksir"])],
 [R("atfj", "وَالْأَنْبَاءِ", "naba-tidings", c="w", g=["jam-taksir"], of=("الْحَوَادِثِ", "the events", "el-havâdis")),
  R("fail", "خَطْبٌ", "khatb-amr", n=NT("مُؤَخَّرٌ عَنِ الْجَارِّ وَالْمَجْرُورِ", "placed after the jarr phrase", "câr-mecrûrdan sonraya bırakılmıştır")),
  V("da", "نُعْنَى", "ana-mean", pas=True, doer=NAHNU, g=["naqis-verbs"], n=N3(CL("nr", "خَطْبٌ", "a grave matter", "hatbun»"), ZW("عُنِيَ الرَّجُلُ بِالشَّيْءِ يُعْنَى بِهِ فَهُوَ مَعْنِيٌّ بِهِ", "عُنِيَ بِالشَّيْءِ يُعْنَى: a man is concerned with a thing, troubled by it", "«unîye bi'ş-şey'» yu'nâ: kişi bir şeyle meşgul oldu, onunla uğraştı"))),
  JP("بِهِ", "bi", "هُ", n=MT("نُعْنَى", "troubles us", "uğraştırılırız»a")),
  V("d", "وَنُسَاءُ", "saa-bad", c="w", pas=True, doer=NAHNU, g=["hollow-verbs"], n=N3(CL("atf", "نُعْنَى", "we are troubled", "uğraştırılırız"), QAF, ZW("سُؤْتُ الرَّجُلَ: أَحْزَنْتُهُ", "سُؤْتُ الرَّجُلَ: I grieved the man", "«su'tu'r-racüle»: adamı üzdüm")))])
VV(16, "our brothers, the Arāqim, go beyond all bounds against us, insistent in their talk;",
  "kardeşlerimiz Erâkım bize karşı sözlerinde ısrarla haddi aşıyorlar;",
 [INNA("إِنَّ", n=N3(NT("وَالْجُمْلَةُ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ — تَفْسِيرٌ لِلْخَطْبِ: «ثُمَّ فَسَّرَ ذٰلِكَ الْخَطْبَ» (الزَّوْزَنِيُّ)", "the sentence opens afresh and has no seat — it explains the grave matter: «then he explains that matter» (al-Zawzanī)", "cümle ibtidâiyyedir, mahalli yoktur — «büyük iş»i açıklar: «sonra o işi açıkladı» (Zevzenî)"), DR("وَيُرْوَى بِفَتْحِ الْهَمْزَةِ، فَيَكُونُ الْمَصْدَرُ الْمُؤَوَّلُ بَدَلًا مِنَ «الْخَطْبِ»", "it is also related with fatha on the hamza, and the masdar it makes is then a badal of «the grave matter»", "hemzenin fethasıyla da rivayet edilir; o zaman te'vil edilen masdar «büyük iş»ten bedel olur"))),
  R("ismi", "إِخْوَانَنَا", "akh", enc="نَا", g=["jam-taksir"]),
  R("bdln", "الْأَرَاقِمَ", "arqam-hr", pos="propn", g=["jam-taksir"], of=("إِخْوَانَنَا", "our brothers", "ihvânenâ"), n=ZW("الْأَرَاقِمُ: بُطُونٌ مِنْ تَغْلِبَ، سُمُّوا بِهَا لِأَنَّ امْرَأَةً شَبَّهَتْ عُيُونَ آبَائِهِمْ بِعُيُونِ الْأَرَاقِمِ", "the Arāqim are clans of Taghlib, so called because a woman likened their fathers' eyes to the eyes of vipers", "Erâkım, Tağlib'in boylarıdır; bir kadın atalarının gözlerini erkek yılanların gözlerine benzettiği için bu adı almışlardır"))],
 [V("d5", "يَغْلُونَ", "ghala", g=["naqis-verbs", "afal-khamsa"], n=N3(CL("khb", "إِنَّ", "إِنَّ", "inne"), ZW("الْغُلُوُّ: مُجَاوَزَةُ الْحَدِّ", "غُلُوّ is going beyond the bound", "«gulüvv»: haddi aşmak"))),
  JP("عَلَيْنَا", "ala", "نَا", n=MT("يَغْلُونَ", "go beyond bounds", "haddi aşarlar»a")),
  PR("فِي", "fi", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "قِيلِهِمْ", "qil", enc="هِمْ", n=DR("وَرِوَايَتُهُ «قَوْلِهِمْ»، مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "his text reads «قَوْلِهِمْ»; a masdar annexed to its doer", "onun rivayeti «kavlihim»dir; masdarın fâiline izâfeti")),
  R("mub", "إِحْفَاءُ", "ihfa-hr", g=["masdar"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «يَغْلُونَ»، أَوْ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ لِـ«إِنَّ» (الدُّرَّةُ)", "placed after its khabar; the nominal clause is a hal of the doer of «go beyond», in the seat of nasb, or a second predicate of إِنَّ, in the seat of raf' (al-Durra)", "sona bırakılmıştır; isim cümlesi «haddi aşarlar»ın fâilinden hâl olarak mahallen mansûb, ya da «inne»nin ikinci haberi olarak mahallen merfû (Dürre)"), QAF_N, ZW("الْإِحْفَاءُ: الْإِلْحَاحُ", "إِحْفَاء is insistence", "«ihfâ»: ısrar")))])
VV(17, "they mix the innocent among us with the guilty, and being clear of guilt does not help the clear.",
  "aramızdaki suçsuzu suçluyla karıştırıyorlar; suçsuza suçsuzluğu fayda vermiyor.",
 [V("d5", "يَخْلِطُونَ", "khalata", g=["afal-khamsa"], n=DR("وَالْجُمْلَةُ حَالٌ أَوْ خَبَرٌ ثَانٍ كَالْجُمْلَةِ قَبْلَهَا، وَيُمْكِنُ الِاسْتِئْنَافُ", "the clause is a hal or a second predicate like the one before; a fresh start is also possible", "cümle öncekisi gibi hâl ya da ikinci haberdir; isti'nâf da mümkündür")),
  R("maf", "الْبَرِيءَ", "bari", g=["sifa-mushabbaha"]),
  JP("مِنَّا", "min", "نَا", n=MT("الْبَرِيءَ", "the innocent", "suçsuz»a")),
  R("majr", "بِذِي", "dhu", j="bi", mud=True, sign=S_YA5, g=["five-nouns"], n=MT("يَخْلِطُونَ", "they mix", "karıştırırlar»a"))],
 [R("mdf", "الذَّنْبِ", "dhanb", g=["tibaq"], n=HADD("طِبَاقٌ بَيْنَ «الْبَرِيءَ» وَ«ذِي الذَّنْبِ»: مَعْنَيَانِ مُتَضَادَّانِ", "a ṭibāq between «the innocent» and «the guilty»: two contrary meanings", "«suçsuz» ile «suçlu» arasında tıbâk: iki zıt mânâ")),
  LA_N("وَلَا", c="w"),
  V("d", "يَنْفَعُ", "nafaa", n=CL("atf", "يَخْلِطُونَ", "they mix", "karıştırırlar")),
  R("maf", "الْخَلِيَّ", "khaliyy-hr", n=ZW("يُرِيدُ بِالْخَلِيِّ: الْبَرِيءَ الْخَالِيَ مِنَ الذَّنْبِ", "by خَلِيّ he means the innocent, free of guilt", "«halî» ile suçtan uzak suçsuzu kastediyor")),
  R("fail", "الْخَلَاءُ", "khala-amr", g=["mulhaq-bil-jinas"], n=N3(QAF, ZW("فَلَا تَنْفَعُ الْبَرِيءَ بَرَاءَةُ سَاحَتِهِ مِنَ الذَّنْبِ", "so his being clear of guilt does not help the innocent", "suçsuzun, eteğinin suçtan temiz olması ona fayda vermez"),
     HADD("يُلْحَقُ بِالْجِنَاسِ مَا يَجْمَعُهُ الِاشْتِقَاقُ: «الْخَلِيَّ» وَ«الْخَلَاءُ» مِنْ أَصْلٍ وَاحِدٍ", "what derivation brings together is attached to jinās: «the clear» and «being clear» come from one root", "iştikakın bir araya getirdiği cinasa ilhak edilir: «halî» ve «halâ» aynı kökten")))])
VV(18, "They claim that all who struck the ʿayr are clients of ours, and that we are answerable for their clientage.",
  "«Ayr»ı vuran herkesin bizim mevlâlarımız olduğunu ve onların velâsının (suçlarının) bize ait olduğunu iddia ediyorlar.",
 [V("mw", "زَعَمُوا", "zaama-claim", g=["zanna-wa-akhawatuha"], n=N3(CL("ist"), NT("وَالْأَلِفُ فَارِقَةٌ", "the alif is the separating alif", "elif fârikadır"))),
  INNA("أَنَّ", which="anna"),
  R("isma", "كُلَّ", "kull", mud=True),
  PT("مَنْ", "man", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ", "a relative noun built on sukun, in the seat of jarr as the second term of the idafa", "sükûn üzere mebnî ism-i mevsûl, muzâfun ileyh olarak mahallen mecrûr", g=["ism-mawsul", "idafa-definiteness"], pos="pron"),
  V("m", "ضَرَبَ", "daraba", doer=HUWA("«مَنْ»", "«who»", "«men»e"), n=CL("sila"))],
 [R("maf", "الْعَيْرَ", "ayr", n=ZW("الْعَيْرُ فِي هٰذَا الْبَيْتِ يُفَسَّرُ بِالسَّيِّدِ، وَالْحِمَارِ، وَالْوَتِدِ، وَالْقَذَى، وَجَبَلٍ بِعَيْنِهِ؛ فَإِنْ فُسِّرَ بِالسَّيِّدِ فَهُوَ كُلَيْبُ وَائِلٍ", "العَيْر in this verse is explained as the lord, the wild ass, the tent-peg, a mote in the eye, and a certain mountain; taken as the lord, it is Kulayb of Wāʾil", "bu beyitteki «ayr» efendi, yaban eşeği, kazık, göze kaçan çöp ve belli bir dağ diye açıklanır; efendi diye açıklanırsa Vâil'in Küleyb'idir")),
  T("مُوَالٍ", "muwalin-hr", "noun", ["inna-wa-akhawatuha", "ism-maqsur-manqus", "ism-fail"], "خَبَرُ «أَنَّ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — اسْمٌ مَنْقُوصٌ.",
    "The predicate of أَنَّ, in raf' by a damma estimated on the ya that dropped where two quiescents met — a manqus noun.", "«Enne»nin haberi; iki sâkin karşılaştığı için düşen yâ üzerinde takdîrî damme ile merfû — menkûs isim."),
  JP("لَنَا", "li", "نَا", n=N3(MTH("صِفَةٍ لِـ«مُوَالٍ»", "an omitted adjective of «clients»", "«mevâlin»in mahzûf sıfatına"), DR("أَوْ بِـ«مُوَالٍ» نَفْسِهِ؛ وَ«أَنَّ» وَاسْمُهَا وَخَبَرُهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «زَعَمُوا»", "or on «clients» itself; أَنَّ with its noun and predicate makes a masdar standing in for the two objects of «they claim»", "ya da «mevâlin»in kendisine; «enne», ismi ve haberi «iddia ettiler»in iki mef'ûlünün yerini tutan bir masdardır"))),
  INNA("وَأَنَّا", which="anna", enc="نَا", c="w", n=DR("وَحُذِفَتْ إِحْدَى النُّونَيْنِ تَخْفِيفًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْمَصْدَرِ قَبْلَهُ", "one of the two nuns is dropped for lightness; the masdar it makes is joined to the masdar before it", "iki nûndan biri hafiflik için düşmüştür; te'vil edilen masdar öncekine ma'tûftur")),
  R("khba", "الْوَلَاءُ", "wala", g=["ijaz-al-hadhf", "hadhf-al-mudaf-wal-mudaf-ilayh"], n=N3(QAF, ZW("أَيْ أَصْحَابُ وَلَائِهِمْ، فَحَذَفَ الْمُضَافَ: تَلْحَقُنَا جَرَائِرُهُمْ", "that is, the holders of their clientage — he dropped the annexed word: their crimes are laid on us", "yani onların velâsının sahipleri; muzâfı hazfetti: onların suçları bize yüklenir"),
     NT("وَفِيهِ إِيجَازُ الْحَذْفِ بِحَذْفِ الْمُضَافِ، كَمَا ذَكَرَ الزَّوْزَنِيُّ", "an ījāz by omission — the annexed word is dropped, as al-Zawzanī says", "muzâfın hazfiyle îcâz-ı hazf; Zevzenî'nin belirttiği gibi")))])
VV(19, "They settled their purpose at nightfall, and when they woke at morning there was clamour among them —",
  "İşlerini akşam vakti kararlaştırdılar; sabaha erdiklerinde aralarında bir gürültü koptu —",
 [V("mw", "أَجْمَعُوا", "ajmaa-hr", g=["form-iv-verbs"], n=N3(CL("ist"), NT("وَالْأَلِفُ فَارِقَةٌ", "the alif is the separating alif", "elif fârikadır"), ZW("إِجْمَاعُ الْأَمْرِ: عَقْدُ الْقَلْبِ وَتَوْطِينُ النَّفْسِ عَلَيْهِ", "إِجْمَاع of a purpose is binding the heart and settling the soul upon it", "bir işe «icmâ»: kalbi ona bağlamak ve nefsi ona hazırlamak"))),
  R("maf", "أَمْرَهُمْ", "amr", enc="هُمْ", n=ZW("مِنْ قَتْلِنَا وَجِدَالِنَا", "to kill us and wrangle with us", "bizi öldürmek ve bizimle çekişmek")),
  R("zarfz", "عِشَاءً", "isha-evening", n=MZ("أَجْمَعُوا", "they settled", "kararlaştırdılar»a")),
  PT("فَلَمَّا", "lamma", "لَمَّا ظَرْفٌ بِمَعْنَى «حِينَ» مُتَعَلِّقٌ بِجَوَابِهِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ — وَقِيلَ: حَرْفُ وُجُودٍ لِوُجُودٍ (الدُّرَّةُ)", "لَمَّا is an adverb meaning «when», hanging on its answer and annexed to the clause after it — others: a particle of «one thing on another» (al-Durra)", "lemmâ: «hîne» anlamında zarf, cevabına müteallik, sonraki cümleye muzâf — vücûd li-vücûd harfi olduğu da söylenmiştir (Dürre)", c="f", g=["maful-fih"])],
 [V("mw", "أَصْبَحُوا", "asbaha", g=["form-iv-verbs"], n=N3(NT("تَامٌّ بِمَعْنَى: دَخَلُوا فِي الصَّبَاحِ", "complete, meaning «they entered upon morning»", "tamdır: «sabaha girdiler» anlamında"), CL("mdf", "لَمَّا", "لَمَّا", "lemmâ"))),
  T("أَصْبَحَتْ", "asbaha", "verb", ["kana-wa-akhawatuha", "form-iv-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ» مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ جَوَابُ «لَمَّا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A defective past verb, a sister of كَانَ, built on fatha; the ta marks the feminine — the clause is the answer of لَمَّا and has no seat.", "Kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; tâ te'nîs içindir — cümle «lemmâ»nın cevabıdır, mahalli yoktur."),
  JP("لَهُمْ", "li", "هُمْ", n=MTH("خَبَرِ «أَصْبَحَ» الْمُقَدَّمِ", "the omitted, fronted predicate of أَصْبَحَ", "«asbaha»nın öne alınmış mahzûf haberine")),
  R("ismk", "ضَوْضَاءُ", "dawda-hr", n=N3(NT("اسْمُ «أَصْبَحَ» مُؤَخَّرٌ", "the noun of أَصْبَحَ, placed after", "«asbaha»nın sona bırakılmış ismi"), QAF, ZW("الضَّوْضَاءُ: الْجَلَبَةُ وَالصِّيَاحُ", "ضَوْضَاء is din and shouting", "«davdâ»: gürültü ve bağırış")))])
VV(20, "of callers and of answerers and of horses neighing — and amid that, the grumbling of camels.",
  "çağıranlardan, cevap verenlerden, atların kişnemesinden — bunların arasında develerin böğürmesi.",
 [PR("مِنْ", "min", n=MTH("صِفَةٍ لِـ«ضَوْضَاءُ»", "an omitted adjective of «clamour»", "«davdâ»nın mahzûf sıfatına")),
  T("مُنَادٍ", "munadin-hr", "noun", ["huruf-jarr", "ism-maqsur-manqus", "ism-fail", "hadhf-wa-taqdir"], "مَجْرُورٌ بِـ«مِنْ» بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — اسْمٌ مَنْقُوصٌ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ (الدُّرَّةُ).",
    "In jarr after مِنْ by a kasra estimated on the ya that dropped where two quiescents met — a manqus noun, the adjective of an omitted noun (al-Durra).", "«Min» ile, iki sâkin karşılaştığı için düşen yâ üzerinde takdîrî kesre ile mecrûr — menkûs isim; mahzûf bir mevsûfun sıfatıdır (Dürre)."),
  PR("وَمِنْ", "min", c="w", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى مَا قَبْلَهُمَا", "the phrase is joined to the one before", "câr-mecrûr öncekine ma'tûftur")),
  R("majr", "مُجِيبٍ", "mujib-answerer", g=["ism-fail"]),
  PR("وَمِنْ", "min", c="w", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى مَا قَبْلَهُمَا", "the phrase is joined to the one before", "câr-mecrûr öncekine ma'tûftur"))],
 [R("majr", "تَصْهَالِ", "tashal-hr", mud=True, g=["masdar"], n=ZW("التَّصْهَالُ كَالصَّهِيلِ، وَتَفْعَالٌ لَا يَكُونُ إِلَّا مَصْدَرًا، وَتِفْعَالٌ لَا يَكُونُ إِلَّا اسْمًا", "تَصْهَال is like صَهِيل (neighing); تَفْعَال is only ever a masdar, تِفْعَال only ever a noun", "«tas'hâl», «sahîl» (kişneme) gibidir; «tef'âl» yalnız masdar, «tif'âl» yalnız isim olur")),
  R("mdf", "خَيْلٍ", "khayl", n=DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti")),
  R("zarfm", "خِلَالَ", "khilal-hr", mud=True, n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  PT("ذَاكَ", "dhaka", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ، وَالْكَافُ حَرْفُ خِطَابٍ", "a demonstrative built on sukun, in the seat of jarr as the second term of the idafa; the kaf is a particle of address", "sükûn üzere mebnî işaret ismi, muzâfun ileyh olarak mahallen mecrûr; kâf hitap harfidir", g=["asma-al-ishara", "idafa-definiteness"], pos="pron"),
  R("mub", "رُغَاءُ", "ruga-hr", g=["kinaya"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِـ«ضَوْضَاءُ»، أَوْ حَالٌ مِنْهَا (الدُّرَّةُ)", "placed after; the clause is a second adjective of «clamour», or a hal of it (al-Durra)", "sona bırakılmıştır; cümle «davdâ»nın ikinci sıfatı ya da ondan hâldir (Dürre)"), QAF_N,
     ZW("اخْتَلَطَتْ أَصْوَاتُ الدَّاعِينَ وَالْمُجِيبِينَ وَالْخَيْلِ وَالْإِبِلِ، يُرِيدُ بِذٰلِكَ تَجَمُّعَهُمْ وَتَأَهُّبَهُمْ", "the voices of callers, answerers, horses and camels mingled — by it he means their mustering and readying", "çağıranların, cevap verenlerin, atların ve develerin sesleri karıştı — bununla toplanmalarını ve hazırlanmalarını kastediyor"),
     NT("وَالْبَيْتُ كِنَايَةٌ عَنْ تَجَمُّعِهِمْ لِلْحَرْبِ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "the verse is a kināya for their gathering for war, as al-Zawzanī explains", "beyit, Zevzenî'nin açıkladığı gibi, savaş için toplanmalarından kinayedir")))])
VV(21, "O you who speak, who carry slander of us before ʿAmr — can that last?",
  "Ey Amr'ın huzurunda bizim hakkımızda konuşan, laf taşıyan! Bunun bir devamı olur mu?",
 [T("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "huruf-tanbih"], "«أَيُّ» مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ، وَ«هَا» حَرْفُ تَنْبِيهٍ — وَالْجُمْلَةُ النِّدَائِيَّةُ مُسْتَأْنَفَةٌ.",
    "«أَيُّ» is a vocative, an intended indefinite, built on damma in the seat of nasb, the calling particle left out; «هَا» is a particle of attention — the call is a fresh sentence.", "«Eyyu» kastedilmiş nekre münâdâ, damme üzere mebnî, mahallen mansûb; nidâ harfi mahzûf; «hâ» tenbîh harfidir — nidâ cümlesi müste'nefedir.", segs=SG(("أَيُّ", "ayyuha", "noun"), ("هَا", "ha-tanbih", "part"))),
  R("naatr", "النَّاطِقُ", "natiq", g=["ism-fail"], of=("أَيُّ", "you", "eyyu"), n=NT("عَلَى لَفْظِهِ", "following its form", "lafzına tâbi olarak")),
  R("naatr", "الْمُرَقِّشُ", "muraqqish-hr", g=["ism-fail"], of=("أَيُّ", "you", "eyyu"), n=N3(NT("ثَانٍ", "a second one", "ikinci"), ZW("الَّذِي يُبَلِّغُ عَنَّا الْمَلِكَ مَا يُرِيبُهُ وَيُشَكِّكُهُ فِي مَحَبَّتِنَا إِيَّاهُ", "the one who carries to the king, of us, what makes him suspect our love for him", "kral'a, bizim hakkımızda, ona duyduğumuz sevgiden şüphe ettirecek şeyleri ileten"))),
  JP("عَنَّا", "an", "نَا", n=MT("الْمُرَقِّشُ", "who carries slander", "laf taşıyan»a"))],
 [R("zarfm", "عِنْدَ", "inda", mud=True, n=MZ("الْمُرَقِّشُ", "who carries slander", "laf taşıyan»a")),
  NAME("mdf", "عَمْرٍو", "amr-name"),
  PT("وَهَلْ", "hal-istifham", "هَلْ حَرْفُ اسْتِفْهَامٍ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى النَّفْيِ: قَالَ الزَّوْزَنِيُّ: «وَهٰذَا اسْتِفْهَامٌ مَعْنَاهُ النَّفْيُ، أَيْ لَا بَقَاءَ لِذٰلِكَ»، وَالدُّرَّةُ: «حَرْفُ اسْتِفْهَامٍ مُفِيدٌ لِلنَّفْيِ»", "هَلْ is a particle of question — the question has left asking for denial: al-Zawzanī: «this is a question meaning denial: that has no lasting»; al-Durra: «a question particle giving denial»", "hel: istifhâm harfi — burada istifhâm nefy anlamına çıkmıştır: Zevzenî: «bu, anlamı nefy olan bir sorudur: bunun devamı yoktur»; Dürre: «nefy ifade eden istifhâm harfi»", c="wi", g=["al-istifham", "khuruj-al-istifham"]),
  T("لِذَاكَ", "li", "prep", ["huruf-jarr", "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ، وَ«ذَا» اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِاللَّامِ، وَالْكَافُ حَرْفُ خِطَابٍ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
    "The lam is a jarr letter; «ذَا» is a demonstrative built on sukun, in the seat of jarr after it; the kaf is a particle of address — the phrase hangs on an omitted, fronted khabar.", "Lâm cer harfidir; «zâ» sükûn üzere mebnî işaret ismi, lâm ile mahallen mecrûr; kâf hitap harfidir — câr-mecrûr öne alınmış mahzûf habere müteallik.", segs=SG(("لِ", "li", "prep"), ("ذَاكَ", "dhaka", "pron"))),
  R("mub", "بَقَاءُ", "baqa", g=["masdar"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "placed after; a fresh sentence", "sona bırakılmıştır; cümle müste'nefedir"), QAF_N))])
# =====================================================================================================================
# The poem — vv. 22–28 — عِزَّةٌ قَعْسَاءُ
# =====================================================================================================================
MA_ZAIDA = lambda: PT("مَا", "ma-zaida", "حَرْفٌ زَائِدٌ لَا عَمَلَ لَهُ — «صِلَةٌ زَائِدَةٌ» (الزَّوْزَنِيُّ)", "an extra particle that governs nothing — «an extra link-word» (al-Zawzanī)", "ameli olmayan zâid harf — «zâid sıla» (Zevzenî)", g=["anwa-ma", "huruf-al-ziyada-fil-kafiya"])
VV(22, "Do not think us (cowed) by your goading: before now our enemies have slandered us (to kings).",
  "Kışkırtman yüzünden bizi (boyun eğmiş) sanma: düşmanlarımız bizi daha önce de (krallara) gammazlamıştır.",
 [PT("لَا", "la-nahiya", "لَا نَاهِيَةٌ جَازِمَةٌ", "لَا of forbidding, which puts the verb in jazm", "cezmeden nehiy «lâ»sı", g=["la-nahiya"]),
  V(JZ("بِـ«لَا» النَّاهِيَةِ", "by the لَا of forbidding", "nehiy «lâ»sı ile"), "تَخَلْنَا", "khala-think", enc="نَا", encrole="maf1", doer=ANTA, g=["hollow-verbs", "zanna-wa-akhawatuha", "mafulayn"],
    n=N3(NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ: لَا تَخَلْنَا مُتَخَاشِعِينَ (الزَّوْزَنِيُّ) — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "its middle letter drops where two quiescents meet; the second object is left out: «do not think us cowed» (al-Zawzanī) — a fresh sentence", "orta harfi iki sâkin karşılaştığı için düşmüştür; ikinci mef'ûl mahzûftur: «bizi boyun eğmiş sanma» (Zevzenî) — cümle müste'nefedir"),
     ZW("يُخَاطِبُ مَنْ يَسْعَى بِهِمْ مِنْ بَنِي تَغْلِبَ إِلَى عَمْرِو بْنِ هِنْدٍ", "he addresses the man of Taghlib who informs against them to ʿAmr ibn Hind", "Amr b. Hind'e onları gammazlayan Tağlibli'ye hitap ediyor"))),
  PR("عَلَى", "ala", n=N3(MTH("الْمَفْعُولِ الثَّانِي", "the omitted second object", "mahzûf ikinci mef'ûle"), ZW("أَيْ عَلَى امْتِدَادِ غَرَاتِكَ", "that is, for all your long goading", "yani kışkırtmanın uzayıp gitmesine rağmen"))),
  R("majr", "غَرَاتِكَ", "ghara-hr", enc="كَ", n=ZW("الْغَرَاةُ: اسْمٌ بِمَعْنَى الْإِغْرَاءِ", "غَرَاة is a noun meaning goading on", "«garât»: kışkırtma anlamında bir isim")),
  INNA("إِنَّا", enc="نَا", n=DR("وَالْجُمْلَةُ تَعْلِيلٌ لِلنَّهْيِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause gives the reason for the forbidding and has no seat", "cümle nehyin ta'lîlidir, mahalli yoktur"))],
 [PT("قَبْلُ", "qablu", "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — قُطِعَ عَنِ الْإِضَافَةِ — مُتَعَلِّقٌ بِـ«وَشَى»", "an adverb of time built on damma, in the seat of nasb — cut off from annexation — hanging on «slandered»", "zaman zarfı, damme üzere mebnî, mahallen mansûb — izâfetten kesilmiştir — «gammazladı»ya müteallik", g=["maful-fih", "al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"], pos="noun"),
  MA_ZAIDA(),
  QAD(),
  V("ma", "وَشَى", "washa-hr", g=["naqis-verbs", "mithal-verbs"], n=CL("khb", "إِنَّ", "إِنَّ", "inne")),
  JP("بِنَا", "bi", "نَا", n=MT("وَشَى", "slandered", "gammazladı»ya")),
  R("fail", "الْأَعْدَاءُ", "aduww", g=["jam-taksir"], n=N3(QAF, ZW("فَقَدْ وَشَى بِنَا أَعْدَاؤُنَا إِلَى الْمُلُوكِ قَبْلَكَ، فَإِغْرَاؤُكَ الْمَلِكَ بِنَا لَا يَقْدَحُ فِي أَمْرِنَا", "our enemies slandered us to kings before you, so your goading the king against us does not harm our standing", "düşmanlarımız senden önce de bizi krallara gammazladı; senin kralı bize karşı kışkırtman işimize zarar vermez")))])
VV(23, "Yet we have stayed, for all the hatred, raised high by fortresses and a glory firm-rooted —",
  "Bütün kine rağmen, kaleler ve sarsılmaz bir izzet bizi yükselterek ayakta kaldık —",
 [V("mna", "فَبَقِينَا", "baqiya", c="fi", g=["naqis-verbs"], n=CL("ist")),
  PR("عَلَى", "ala", n=MT("بَقِيَ", "stayed", "kaldık»a")),
  R("majr", "الشَّنَاءَةِ", "shanaa-hr", n=ZW("الشَّنَاءَةُ: الْبُغْضُ؛ أَيْ عَلَى بُغْضِ النَّاسِ إِيَّانَا وَإِغْرَائِهِمُ الْمُلُوكَ بِنَا", "شَنَاءَة is hatred: for all men's hatred of us and their goading of kings against us", "«şenâe»: kin; yani insanların bize olan kinine ve kralları bize karşı kışkırtmalarına rağmen"))],
 [V("dy", "تَنْمِينَا", "nama-hr", enc="نَا", g=["naqis-verbs"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَا» الْفَاعِلِ، وَالرَّابِطُ الضَّمِيرُ", "the clause is a hal of the doer «we», in the seat of nasb; the pronoun is the link", "cümle fâil «nâ»dan hâl, mahallen mansûb; bağlayıcı zamirdir"), ZW("تَنْمِينَا: تَرْفَعُنَا", "تَنْمِينَا: it raises us", "«tenmînâ»: bizi yükseltir"))),
  R("fail", "حُصُونٌ", "hisn-amr", g=["jam-taksir"]),
  R("atfr", "وَعِزَّةٌ", "izza", c="w", of=("حُصُونٌ", "fortresses", "husûn")),
  R("naatr", "قَعْسَاءُ", "qasa-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("عِزَّةٌ", "glory", "izzet"), n=N3(QAF, ZW("حُصُونٌ مَنِيعَةٌ وَعِزَّةٌ ثَابِتَةٌ لَا تَزُولُ", "unassailable fortresses and a firm glory that does not pass", "zaptedilmez kaleler ve zâil olmayan sabit bir izzet")))])
VV(24, "which before this day has blinded the eyes of men — in it is rage, and refusal.",
  "ki bu günden önce insanların gözlerini kör etmiştir — onda öfke ve kabul etmeyiş vardır.",
 [R("zarfz", "قَبْلَ", "qabla", mud=True, n=MZ("بَيَّضَتْ", "blinded", "kör etti»ye")),
  MA_ZAIDA(),
  R("mdf", "الْيَوْمِ", "yawm"),
  V("mt", "بَيَّضَتْ", "bayyada", doer=HIYA("الْعِزَّةِ", "the glory", "izzete"), g=["form-ii-verbs", "kinaya"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ ثَانِيَةٌ لِـ«عِزَّةٌ»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهَا", "the clause is a second adjective of «glory», in the seat of raf', or a hal of it, in the seat of nasb", "cümle «izzet»in ikinci sıfatı olarak mahallen merfû, ya da ondan hâl olarak mahallen mansûb"),
     NT("وَفِيهِ كِنَايَةٌ: «وَتَبْيِيضُ الْعَيْنِ كِنَايَةٌ عَنِ الْإِعْمَاءِ» (الزَّوْزَنِيُّ)", "a kināya: «whitening the eye is a kināya for blinding» (al-Zawzanī)", "kinaye: «gözü ağartmak, kör etmekten kinayedir» (Zevzenî)"))),
  T("بِعُيُونِ", "ayn-eye", "noun", ["maful-bihi", "huruf-al-ziyada-fil-kafiya", "jam-taksir", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ«عُيُونِ» مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ، مُضَافٌ — «الْبَاءُ فِي بِعُيُونِ زَائِدَةٌ، أَيْ: بَيَّضَتْ عُيُونَ النَّاسِ» (الزَّوْزَنِيُّ).",
    "The ba is an extra jarr letter; «eyes» is the object, in nasb by an estimated fatha that the extra letter's vowel keeps from showing; annexed — «the ba of بِعُيُونِ is extra: it blinded men's eyes» (al-Zawzanī).", "Bâ zâid cer harfidir; «uyûn» mef'ûlün bihtir, zâid harfin harekesi mahalli işgal ettiği için takdîrî fetha ile mansûb; muzâf — «bi-uyûni'deki bâ zâiddir: insanların gözlerini ağarttı» (Zevzenî).", segs=SG(("بِ", "bi", "prep"), ("عُيُونِ", "ayn-eye", "noun")))],
 [R("mdf", "النَّاسِ", "nas"),
  JP("فِيهَا", "fi", "هَا", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "تَغَيُّظٌ", "taghayyuz-hr", g=["masdar", "majaz-aqli"], n=N3(DR("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «بَيَّضَتْ»", "placed after; the nominal clause is a hal of the doer of «blinded», in the seat of nasb", "sona bırakılmıştır; isim cümlesi «kör etti»nin fâilinden hâl, mahallen mansûb"),
     NT("وَفِيهِ مَجَازٌ: «وَجَعَلَ التَّغَيُّظَ وَالْإِبَاءَ لِلْعِزَّةِ مَجَازًا، وَهُمَا عِنْدَ التَّحْقِيقِ لَهُمْ» (الزَّوْزَنِيُّ)؛ وَهُوَ — عَلَى حَدِّ التَّلْخِيصِ — مَجَازٌ عَقْلِيٌّ: نِسْبَةُ الْمَعْنَى إِلَى غَيْرِ صَاحِبِهِ", "a majāz: «he gave the rage and the refusal to the glory as a figure, though in truth they are theirs» (al-Zawzanī); by the Talkhīṣ's definition it is a majāz ʿaqlī — a meaning ascribed to other than its owner", "mecâz: «öfkeyi ve kabul etmeyişi mecâzen izzete verdi; gerçekte onlar onlarındır» (Zevzenî); Telhîs'in tarifine göre mecâz-ı aklîdir — bir mânânın sahibinden başkasına nisbeti"))),
  R("atfr", "وَإِبَاءُ", "iba-hr", c="w", g=["masdar"], of=("تَغَيُّظٌ", "rage", "tagayyuz"), n=N3(QAF_N, ZW("يُرِيدُ أَنَّ النَّاسَ يَحْسُدُونَنَا عَلَى إِبَاءِ عِزَّتِنَا … حَتَّى كَأَنَّهُمْ عَمُوا عِنْدَ نَظَرِهِمْ إِلَيْنَا", "he means that men envy us the proud refusal of our glory … until it is as if they went blind on looking at us", "insanların izzetimizin kabul etmeyişini kıskandıklarını … bize bakınca sanki kör olduklarını kastediyor")))])
VV(25, "It is as though Fate, hurling at us, hurls at a black, jutting mountain whose crest the cloud parts from.",
  "Sanki ölüm (zaman) bize saldırırken, bulutların etrafından açıldığı kara, çıkıntılı bir dağa saldırır.",
 [KAANNA("وَكَأَنَّ", c="wi", g=TB, n=N3(DR("وَكَأَنَّ وَاسْمُهَا وَخَبَرُهَا جُمْلَةٌ مُسْتَأْنَفَةٌ", "كَأَنَّ with its noun and predicate is a fresh sentence", "keenne, ismi ve haberi müste'nef bir cümledir"),
     NT("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ «نَا» (قَوْمُ الشَّاعِرِ)، وَالْمُشَبَّهُ بِهِ الْجَبَلُ الْأَرْعَنُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — أَلَّا تُؤَثِّرَ فِيهِمُ النَّوَائِبُ — ذَكَرَهُ الزَّوْزَنِيُّ: «يُرِيدُ أَنَّ نَوَائِبَ الزَّمَانِ … لَا تُؤَثِّرُ فِيهِمْ … كَمَا لَا تُؤَثِّرُ فِي مِثْلِ هٰذَا الْجَبَلِ»", "a tashbih mursal mujmal: «us» (the poet's people) are likened to the jutting mountain; the particle is كَأَنَّ; the point of likeness — that misfortunes leave no mark on them — is al-Zawzanī's: «he means that the blows of time … leave no mark on them, as they leave none on such a mountain»", "teşbîh-i mürsel mücmel: müşebbeh «biz» (şairin kavmi), müşebbehün bih çıkıntılı dağ, edat «keenne»; vech-i şebeh — musibetlerin onlara tesir etmemesi — Zevzenî'dedir: «zamanın musibetleri onlara tesir etmez, bu dağa tesir etmediği gibi»"))),
  R("ismka", "الْمَنُونَ", "manun-hr", n=ZW("يُرِيدُ الدَّهْرَ", "he means Fate, time", "zamanı kastediyor")),
  V("dy", "تَرْدِي", "radaa-throw-hr", doer=HIYA("الْمَنُونِ", "Fate", "ölüme"), g=["naqis-verbs"], n=N3(CL("khb", "كَأَنَّ", "كَأَنَّ", "keenne"), ZW("الرَّدْيُ: الرَّمْيُ، وَالْفِعْلُ رَدَى يَرْدِي", "رَدْي is hurling; the verb is رَدَى يَرْدِي", "«redy»: atmak; fiili «redâ yerdî»"))),
  JP("بِنَا", "bi", "نَا", n=N3(MT("تَرْدِي", "hurls", "atar»a"), ZW("أَيْ تَرْدِينَا", "that is, hurls us", "yani bize atar")))],
 [R("maf", "أَرْعَنَ", "aran-mountain-hr", g=["mamnu-min-sarf", "hadhf-wa-taqdir"], n=N3(NT("وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: جَبَلًا أَرْعَنَ", "it takes no tanwin: a diptote, an adjective on the pattern of a verb; it is the adjective of an omitted noun, «a mountain jutting»", "tenvin almaz: sıfat ve fiil vezninde olduğu için gayr-i munsarif; mahzûf bir mevsûfun sıfatıdır: «çıkıntılı bir dağ»"), ZW("الْأَرْعَنُ: الْجَبَلُ الَّذِي لَهُ رَعْنٌ، وَالرَّعْنُ: أَنْفُ الْجَبَلِ الشَّاخِصُ الْبَارِزُ", "أَرْعَن is a mountain with a رَعْن, the jutting nose of a mountain", "«er'an»: «ra'n»ı olan dağ; «ra'n»: dağın çıkıntılı burnu"))),
  R("naatn", "جَوْنًا", "jawn-amr", of=("أَرْعَنَ", "jutting", "er'ane"), n=ZW("الْجَوْنُ: الْأَسْوَدُ وَالْأَبْيَضُ جَمِيعًا، وَالْمُرَادُ بِهِ الْأَسْوَدُ فِي الْبَيْتِ", "جَوْن is both black and white; here it means black", "«cevn» hem siyah hem beyazdır; beyitte siyah kastedilmiştir")),
  V("d", "يَنْجَابُ", "injaba-hr", g=["form-vii-verbs", "hollow-verbs"], n=N3(CL("nn", "أَرْعَنَ", "jutting", "er'ane»"), ZW("الِانْجِيَابُ: الِانْكِشَافُ وَالِانْشِقَاقُ", "اِنْجِيَاب is being cleared away, parted", "«incîyâb»: açılmak, yarılmak"))),
  JP("عَنْهُ", "an", "هُ", n=MT("يَنْجَابُ", "parts", "açılır»a")),
  R("fail", "الْعَمَاءُ", "ama-cloud-hr", n=N3(QAF, ZW("الْعَمَاءُ: السَّحَابُ؛ أَيْ يُحِيطُ بِهِ وَلَا يَبْلُغُ أَعْلَاهُ", "العَمَاء is cloud: it surrounds it and does not reach its top", "«amâ»: bulut; yani onu kuşatır, zirvesine ulaşmaz")))])
VV(26, "frowning on calamities, unloosened by any hard disaster of Fate.",
  "musibetlere karşı çatık kaşlı; zamanın hiçbir çetin felaketi onu gevşetemez.",
 [R("naatn", "مُكْفَهِرًّا", "mukfahirr-hr", g=["ism-fail"], of=("أَرْعَنَ", "jutting", "er'ane"), n=N3(DR("ثَالِثٌ، أَوْ حَالٌ مِنْهُ، وَيَجُوزُ رَفْعُهُ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ", "a third one, or a hal of it; it may also be read in raf' as the khabar of an omitted mubtada", "üçüncüsü, ya da ondan hâl; mahzûf bir mübtedânın haberi olarak merfû okunması da caizdir"), ZW("الِاكْفِهْرَارُ: شِدَّةُ الْعُبُوسِ وَالْقُطُوبِ؛ وَالْبَيْتُ مِنْ صِفَةِ الْأَرْعَنِ", "اِكْفِهْرَار is a deep frown and scowl; the verse describes the mountain", "«ikfihrâr»: şiddetli kaş çatma; beyit dağın vasfındandır"))),
  PR("عَلَى", "ala", n=MT("مُكْفَهِرًّا", "frowning", "kaş çatan»a")),
  R("majr", "الْحَوَادِثِ", "haditha-hr", g=["jam-taksir"]),
  LA_N()],
 [V("dw", "تَرْتُوهُ", "rata-hr", enc="هُ", g=["naqis-verbs"], n=N3(DR("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنْ «أَرْعَنَ»", "the clause can be an adjective or a hal of «jutting mountain»", "cümle «dağ»ın sıfatı da hâli de olabilir"), ZW("الرَّتْوُ: الشَّدُّ وَالْإِرْخَاءُ جَمِيعًا، وَهُوَ مِنَ الْأَضْدَادِ، وَلٰكِنَّهُ فِي الْبَيْتِ بِمَعْنَى الْإِرْخَاءِ", "رَتْو is both tightening and loosening, a word of opposite senses; in the verse it means loosening", "«retv» hem sıkmak hem gevşetmektir, ezdâddandır; beyitte gevşetmek anlamındadır"))),
  R("majr", "لِلدَّهْرِ", "dahr", j="li", n=MT("تَرْتُو", "loosens", "gevşetir»e")),
  R("fail", "مُؤْيِدٌ", "muyid-tf", n=ZW("الْمُؤْيِدُ: الدَّاهِيَةُ الْعَظِيمَةُ، مُشْتَقَّةٌ مِنَ الْأَيْدِ وَالْآدِ، وَهُمَا الْقُوَّةُ", "مُؤْيِد is a great disaster, from أَيْد and آد, strength", "«mu'yid»: büyük felaket; kuvvet anlamındaki «eyd» ve «âd»dan türemiştir")),
  R("naatr", "صَمَّاءُ", "asamm", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("مُؤْيِدٌ", "disaster", "mu'yid"), n=N3(QAF, ZW("الصَّمَّاءُ: الشَّدِيدَةُ، مِنَ الصَّمَمِ الَّذِي هُوَ الشِّدَّةُ وَالصَّلَابَةُ؛ يَقُولُ: وَنَحْنُ مِثْلُ هٰذَا الْجَبَلِ فِي الْمَنَعَةِ وَالْقُوَّةِ", "صَمَّاء is hard, from صَمَم, hardness; he says: and we are like this mountain in strength", "«sammâ»: çetin, sertlik anlamındaki «samem»den; diyor ki: biz de güç ve dokunulmazlıkta bu dağ gibiyiz")))])
VV(27, "Of Iram's ancient stock; with such as he the horses wheel, and they refuse his foe the driving-out (of their master).",
  "İrem soyundandır (köklü şereflidir); onun gibisiyle atlar dolaşır ve (sahiplerinin yurdundan) sürülmesini hasmına çok görürler.",
 [R("khb", "إِرَمِيٌّ", "iramiyy-hr", g=["ism-mansub", "kinaya", "hadhf-wa-taqdir"], n=N3(NT("وَالْمُبْتَدَأُ مَحْذُوفٌ تَقْدِيرُهُ: هُوَ (الدُّرَّةُ)", "its mubtada is left out: «he is» (al-Durra)", "mübtedâsı mahzûftur: «o» (Dürre)"), ZW("إِرَمُ: جَدُّ عَادٍ، وَهُوَ عَادُ بْنُ عَوْصِ بْنِ إِرَمَ بْنِ سَامٍ", "Iram is the forefather of ʿĀd: ʿĀd son of ʿAwṣ son of Iram son of Shem", "İrem, Âd'ın atasıdır: Âd b. Avs b. İrem b. Sâm"),
     NT("وَفِيهِ كِنَايَةٌ عَنْ قِدَمِ الشَّرَفِ: «هُوَ إِرَمِيٌّ مِنَ الْحَسَبِ قَدِيمُ الشَّرَفِ» (الزَّوْزَنِيُّ)", "a kināya for ancient nobility: «he is of Iram in lineage, of ancient honour» (al-Zawzanī)", "köklü şereften kinaye: «soyca İremlidir, şerefi eskidir» (Zevzenî)"))),
  R("majr", "بِمِثْلِهِ", "mithl", j="bi", enc="هُ", n=MT("جَالَتْ", "wheel", "dolaşır»a")),
  V("mtk", "جَالَتِ", "jala-hr", g=["hollow-verbs"], n=NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ، وَالْأُولَى «إِرَمِيٌّ» (الدُّرَّةُ)", "the clause is a second adjective of the omitted noun, in the seat of raf' — the first is «of Iram» (al-Durra)", "cümle mahzûf mevsûfun ikinci sıfatıdır, mahallen merfû — birincisi «İremli»dir (Dürre)"))],
 [R("fail", "الْخَيْلُ", "khayl", n=DR("وَرِوَايَتُهُ «جَالَتِ الْجِنُّ، فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ»", "his text reads «the jinn wheeled, and the … returned upon their foe»", "onun rivayeti: «cinler dolaştı, …lar hasmına döndü»")),
  V("da", "وَتَأْبَى", "aba", c="w", doer=HIYA("الْخَيْلِ", "the horses", "atlara"), g=["naqis-verbs"], n=CL("atf", "جَالَتِ", "wheeled", "dolaştı")),
  R("majr", "لِخَصْمِهَا", "khasm", j="li", enc="هَا", n=MT("تَأْبَى", "refuse", "çok görür»e")),
  T("الْإِجْلَاءُ", "ijla-hr", "noun", ["maful-bihi", "masdar", "al-qafiya"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — عَلَى شَرْحِ الزَّوْزَنِيِّ: «وَأَنْ تَأْبَى لِخَصْمِهَا أَنْ يُجْلَى صَاحِبُهَا عَنْ أَوْطَانِهِ» — بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا ضَمَّةُ الرَّوِيِّ — وَهُوَ قَافِيَةُ الْبَيْتِ: الضَّمَّةُ فِيهِ حَرَكَةُ الرَّوِيِّ عَلَى غَيْرِ إِعْرَابِهِ، وَاخْتِلَافُ حَرَكَةِ الرَّوِيِّ بِالْفَتْحِ وَالضَّمِّ يُسَمَّى الْإِصْرَافَ؛ وَفِي رِوَايَةِ الدُّرَّةِ «فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ» فَهُوَ فَاعِلٌ مَرْفُوعٌ.",
    "The object, in nasb — following al-Zawzanī's gloss, «and that they refuse their foe that their master be driven from his lands» — by a fatha estimated, kept from showing by the damma of the rawī — it is the rhyme-word: its damma is the rawī's vowel over another case, and the rawī's vowel shifting between fatha and damma is called iṣrāf; in al-Durra's text, «فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ», it is a doer in raf'.",
    "Mef'ûlün bih, mansûb — Zevzenî'nin şerhine göre: «hasmına, sahibinin yurdundan sürülmesini çok görmeleri» — revînin dammesinin görünmesine engel olduğu takdîrî fetha ile — kâfiye kelimesidir: damme, revînin harekesidir, kelimenin i'râbı değildir; revî harekesinin fetha ile damme arasında değişmesine «isrâf» denir; Dürre'nin rivayetinde («فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ») merfû fâildir.")])
VV(28, "A just king, the best of all who walk the earth — and short of what is in him falls all praise.",
  "Âdil bir kral, yeryüzünde yürüyenlerin en üstünü — övgü, onda olanın gerisinde kalır.",
 [R("khb", "مَلِكٌ", "malik-king", g=["hadhf-wa-taqdir"], n=N3(NT("وَالْمُبْتَدَأُ مَحْذُوفٌ تَقْدِيرُهُ: هُوَ (الدُّرَّةُ)", "its mubtada is left out: «he is» (al-Durra)", "mübtedâsı mahzûftur: «o» (Dürre)"), ZW("هُوَ مَلِكٌ عَادِلٌ", "he is a just king", "o âdil bir kraldır"))),
  R("naatr", "مُقْسِطٌ", "muqsit", g=["ism-fail"], of=("مَلِكٌ", "king", "melik"), n=ZW("الْإِقْسَاطُ: الْعَدْلُ", "إِقْسَاط is justice", "«iksât»: adalet")),
  R("atfr", "وَأَفْضَلُ", "afdal", c="w", mud=True, g=["ism-tafdil"], of=("مَلِكٌ", "king", "melik"), n=DR("وَرِوَايَتُهُ «وَأَكْمَلُ»", "his text reads «and the most perfect»", "onun rivayeti «ve ekmelu»dur")),
  PT("مَنْ", "man", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ", "a relative noun built on sukun, in the seat of jarr as the second term of the idafa", "sükûn üzere mebnî ism-i mevsûl, muzâfun ileyh olarak mahallen mecrûr", g=["ism-mawsul", "idafa-definiteness"], pos="pron")],
 [V("dy", "يَمْشِي", "masha", doer=HUWA("«مَنْ»", "«who»", "«men»e"), g=["naqis-verbs", "kinaya"], n=N3(CL("sila"), DR("وَالْمُتَعَلَّقُ مَحْذُوفٌ: يَمْشِي عَلَى الْأَرْضِ", "what it hangs on is left out: «walks on the earth»", "müteallakı mahzûftur: «yeryüzünde yürür»"),
     NT("وَفِيهِ كِنَايَةٌ عَنْ مَوْصُوفٍ: «مَنْ يَمْشِي» النَّاسُ — «أَيْ أَفْضَلُ النَّاسِ» (الزَّوْزَنِيُّ)", "a kināya for the thing described: «who walk» are mankind — «that is, the best of men» (al-Zawzanī)", "mevsûftan kinaye: «yürüyenler» insanlardır — «yani insanların en üstünü» (Zevzenî)"))),
  PR("وَمِنْ", "min", c="w", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "دُونِ", "dun", mud=True),
  PT("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ", "a relative noun built on sukun, in the seat of jarr as the second term of the idafa", "sükûn üzere mebnî ism-i mevsûl, muzâfun ileyh olarak mahallen mecrûr", g=["ism-mawsul", "anwa-ma"], pos="pron"),
  T("لَدَيْهِ", "lada", "noun", ["maful-fih", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةِ الْمَوْصُولِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.",
    "An adverb of place built on sukun, in the seat of nasb, hanging on the omitted ṣila of the relative; the ha is an attached pronoun in the seat of jarr as the second term of the idafa.", "Sükûn üzere mebnî mekân zarfı, mahallen mansûb, mevsûlün mahzûf sılasına müteallik; hâ bitişik zamir, muzâfun ileyh olarak mahallen mecrûr.", segs=SG(("لَدَيْ", "lada", "noun"), ("هِ", "pron-3ms", "pron"))),
  R("mub", "الثَّنَاءُ", "thana-hr", n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "placed after; the clause is joined to what goes before", "sona bırakılmıştır; cümle öncekine ma'tûftur"), QAF, ZW("وَالثَّنَاءُ قَاصِرٌ عَمَّا عِنْدَهُ", "and praise falls short of what he has", "övgü onda olanın gerisinde kalır")))])
# =====================================================================================================================
# The poem — vv. 29–35 — أَيُّمَا خُطَّةٍ أَرَدْتُمْ
# =====================================================================================================================
S_DIPT_F = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — by the fatha that stands for the kasra: a diptote, a feminine proper name", " — özel isim ve müennes olduğu için gayr-i munsarif: kesre yerine fetha ile")
SHART = NT("فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "in the seat of jazm as the verb of the condition", "şart fiili olarak mahallen meczûm")
AW = lambda: PT("أَوْ", "aw", "حَرْفُ عَطْفٍ", "a conjunction («or»)", "atıf harfi («veya»)", g=["atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya"])
JAWAB_M = lambda v: NT("وَالْفَاءُ وَاقِعَةٌ فِي جَوَابِ شَرْطٍ مُقَدَّرٍ — أَوْ إِنْ " + v + " — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُهُ (الدُّرَّةُ)", "the fa opens the answer of an understood condition — «or if you …» — and the clause is that answer, in the seat of jazm (al-Durra)", "fâ takdir edilen bir şartın («veya eğer … iseniz») cevabının başındadır; cümle onun cevabı olarak mahallen meczûmdur (Dürre)")
VV(29, "Whatever grave affair you wish — hand it over to us, and the councils of the nobles are healed by it.",
  "Hangi büyük işi isterseniz bize havale edin; ileri gelenlerin meclisleri onunla şifa bulur.",
 [T("أَيَّمَا", "ayy", "noun", ["huruf-al-shart-fil-kafiya", "maful-bihi", "anwa-ma"], "«أَيَّ» اسْمُ شَرْطٍ جَازِمٌ، مَفْعُولٌ بِهِ مُقَدَّمٌ لِفِعْلِ الشَّرْطِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ؛ وَ«مَا» زَائِدَةٌ (الدُّرَّةُ) — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "«أَيَّ» is a conditional noun that puts in jazm; it is the fronted object of the condition's verb, in nasb by the fatha, annexed; «مَا» is extra (al-Durra) — a fresh sentence.", "«Eyye» cezmeden şart ismidir; şart fiilinin öne alınmış mef'ûlü, fetha ile mansûb, muzâf; «mâ» zâiddir (Dürre) — cümle müste'nefedir.", segs=SG(("أَيَّ", "ayy", "noun"), ("مَا", "ma-zaida", "part"))),
  R("mdf", "خُطَّةٍ", "khutta-ant", n=ZW("الْخُطَّةُ: الْأَمْرُ الْعَظِيمُ الَّذِي يَحْتَاجُ إِلَى مَخْلَصٍ مِنْهُ", "خُطَّة is a grave affair from which a way out is needed", "«hutta»: kurtuluş yolu gerektiren büyük iş")),
  V("mtum", "أَرَدْتُمْ", "arada", g=["form-iv-verbs", "hollow-verbs", "in-shartiyya"], n=SHART)],
 [V(("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَوَاوُ الْجَمَاعَةِ " + _FA, "imperative built on the dropping of the nun; the waw of the group is the doer, in the seat of raf'", "nûnun hazfi üzere mebnî emir; cemâat vâvı fâildir, mahallen merfû"), "فَأَدُّوهَا", "adda", c="fj", enc="هَا", g=["imperative-amr", "form-ii-verbs", "naqis-verbs", "fail", "al-bariz-al-muttasil"],
    n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "the clause is the answer of the condition, in the seat of jazm", "cümle şartın cevabı olarak mahallen meczûm"), ZW("أَدُّوهَا: أَيْ فَوِّضُوهَا", "أَدُّوهَا: commit it", "«eddûhâ»: onu havale edin"))),
  JP("إِلَيْنَا", "ila", "نَا", n=MT("أَدُّوا", "hand over", "havale edin»e")),
  V("da", "تُشْفَى", "shafa", pas=True, g=["naqis-verbs"], n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «هَا» فِي «أَدُّوهَا»", "the clause is a hal of «it» in «hand it over», in the seat of nasb", "cümle «eddûhâ»daki «hâ»dan hâl, mahallen mansûb"), DR("وَرِوَايَتُهُ «تَمْشِي بِهَا الْأَمْلَاءُ»", "his text reads «the nobles walk with it»", "onun rivayeti «temşî bihe'l-emlâ»dır"))),
  JP("بِهَا", "bi", "هَا", n=MT("تُشْفَى", "are healed", "şifa bulur»a")),
  R("naib", "الْأَمْلَاءُ", "mala-chiefs", g=["jam-taksir"], n=N3(QAF, ZW("الْأَمْلَاءُ: الْجَمَاعَاتُ مِنَ الْأَشْرَافِ، الْوَاحِدُ مَلَأٌ، لِأَنَّهُمْ يَمْلَئُونَ الْقُلُوبَ وَالْعُيُونَ جَلَالَةً وَجَمَالًا؛ يُرِيدُ أَنَّهُمْ أُولُو رَأْيٍ وَحَزْمٍ", "أَمْلَاء are bodies of nobles, singular مَلَأ, for they fill hearts and eyes with majesty and beauty; he means that they are men of judgement and resolve", "«emlâ»: eşraf toplulukları, tekili «mele'»; kalpleri ve gözleri heybet ve güzellikle doldurdukları için; onların görüş ve kararlılık sahibi olduklarını kastediyor")))])
VV(30, "If you dig up what lies between Milḥa and al-Ṣāqib, in it are the dead and the living;",
  "Milha ile Sâkib arasında olanı eşelerseniz, orada ölüler de vardır diriler de;",
 [PT("إِنْ", "in-shartiyya", "حَرْفُ شَرْطٍ جَازِمٌ", "a conditional particle that puts in jazm", "cezmeden şart harfi", g=["in-shartiyya"]),
  V("mtum", "نَبَشْتُمْ", "nabasha-hr", n=N3(SHART, DR("وَالْجُمْلَةُ ابْتِدَائِيَّةٌ، وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ الْكَلَامُ", "the clause opens the speech; the answer of the condition is left out, shown by the speech", "cümle ibtidâiyyedir; şartın cevabı mahzûftur, söz ona delâlet eder"), ZW("إِنْ بَحَثْتُمْ عَنِ الْحُرُوبِ الَّتِي كَانَتْ بَيْنَنَا", "if you search out the wars there were between us", "aramızda olan savaşları araştırırsanız"))),
  PT("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "a relative noun built on sukun, in the seat of nasb as the object", "sükûn üzere mebnî ism-i mevsûl, mef'ûlün bih olarak mahallen mansûb", g=["ism-mawsul", "maful-bihi"], pos="pron"),
  R("zarfm", "بَيْنَ", "bayna", mud=True, n=MTH("صِلَةِ الْمَوْصُولِ", "the omitted ṣila of the relative", "mevsûlün mahzûf sılasına")),
  R("mdf", "مِلْحَةَ", "milha-hr", pos="propn", sign=S_DIPT_F, g=["mamnu-min-sarf"])],
 [R("atfj", "فَالصَّاقِبِ", "saqib-hr", pos="propn", c="f", of=("مِلْحَةَ", "Milḥa", "Milha")),
  JP("فِيهِ", "fi", "هُ", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "الْأَمْوَاتُ", "mayyit", g=["jam-taksir"], n=DR("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «مِلْحَةَ» وَ«الصَّاقِبِ»", "placed after; the nominal clause is a hal of «Milḥa» and «al-Ṣāqib», in the seat of nasb", "sona bırakılmıştır; isim cümlesi «Milha» ve «Sâkib»den hâl, mahallen mansûb")),
  R("atfr", "وَالْأَحْيَاءُ", "hayy", c="w", g=["jam-taksir", "tibaq", "istiara", "aqsam-al-istiara"], of=("الْأَمْوَاتُ", "the dead", "el-emvât"), n=N3(QAF,
     NT("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: سَمَّى الْقَتْلَى الَّذِينَ ثُئِرَ بِهِمْ أَحْيَاءً — قَالَ الزَّوْزَنِيُّ: «فَسَمَّى الَّذِي لَمْ يُثْأَرْ بِهَا أَمْوَاتًا، وَالَّذِي ثُئِرَ بِهِمْ أَحْيَاءً؛ لِأَنَّهُمْ … كَأَنَّهُمْ عَادُوا أَحْيَاءً، إِذْ لَمْ تَذْهَبْ دِمَاؤُهُمْ هَدَرًا»؛ وَتَسْمِيَتُهَا عَلَى حَدِّ التَّلْخِيصِ", "an istiʿāra taṣrīḥiyya: the avenged slain are called «the living» — al-Zawzanī: «he called those not avenged the dead, and those avenged the living, for … it is as if they had come back to life, since their blood was not spilt for nothing»; the name is by the Talkhīṣ's definition", "istiâre-i tasrîhiyye: intikamı alınmış maktuller «diriler» diye anılmıştır — Zevzenî: «intikamı alınmayanlara ölüler, alınanlara diriler dedi; çünkü… kanları heder olmadığından sanki yeniden dirildiler»; adlandırma Telhîs'in tarifine göredir"),
     HADD("طِبَاقٌ بَيْنَ «الْأَمْوَاتُ» وَ«الْأَحْيَاءُ»", "a ṭibāq between «the dead» and «the living»", "«ölüler» ile «diriler» arasında tıbâk")))])
VV(31, "or if you probe to the bottom — probing is a thing men take on, and in it is sickness, and cure;",
  "ya da iyice araştırırsanız — araştırma, insanların zahmetine katlandığı bir iştir; onda hastalık da vardır şifa da;",
 [AW(),
  V("mtum", "نَقَشْتُمْ", "naqasha", n=N3(NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «نَبَشْتُمْ»", "the clause is joined to «you dig up»", "cümle «eşelerseniz»e ma'tûftur"), ZW("النَّقْشُ: الِاسْتِقْصَاءُ، وَمِنْهُ قِيلَ لِاسْتِخْرَاجِ الشَّوْكِ مِنَ الْبَدَنِ نَقْشٌ", "نَقْش is probing to the end; from it, drawing a thorn out of the body is called نَقْش", "«nakş»: sonuna kadar araştırmak; bedenden diken çıkarmaya da bundan «nakş» denir"))),
  R("mub", "فَالنَّقْشُ", "naqsh", c="fj", n=JAWAB_M("نَقَشْتُمْ")),
  V("d", "يَجْشَمُهُ", "jashima-hr", enc="هُ", n=N3(CL("khb", "النَّقْشُ", "probing", "en-nakş"), DR("وَيُرْوَى بِالتَّاءِ وَالْيَاءِ، وَكِلَاهُمَا صَحِيحٌ", "it is related with ta and with ya, and both are sound", "tâ ve yâ ile rivayet edilir, ikisi de sahihtir"), ZW("فَهُوَ شَيْءٌ قَدْ يَتَكَلَّفُهُ النَّاسُ", "it is a thing men may take upon themselves with effort", "insanların zahmetine katlanabileceği bir iştir")))],
 [R("fail", "النَّاسُ", "nas"),
  JP("وَفِيهِ", "fi", "هُ", c="w", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "الْإِسْقَامُ", "isqam-hr", g=["masdar", "kinaya"], n=N3(NT("مُؤَخَّرٌ", "placed after", "sona bırakılmıştır"), DR("وَرِوَايَتُهُ «الصَّلَاحُ»", "his text reads «soundness»", "onun rivayeti «es-salâh»tır"),
     NT("وَفِيهِ كِنَايَةٌ: «كَنَّى بِالسَّقَمِ عَنِ الذَّنْبِ، وَبِالْبُرْءِ عَنْ بَرَاءَةِ السَّاحَةِ» (الزَّوْزَنِيُّ)", "a kināya: «by sickness he means guilt, and by cure being clear of blame» (al-Zawzanī)", "kinaye: «hastalıkla suçu, şifayla suçsuzluğu kinaye etti» (Zevzenî)"))),
  R("atfr", "وَالْإِبْرَاءُ", "ibra", c="w", g=["masdar", "tibaq"], of=("الْإِسْقَامُ", "sickness", "el-iskâm"), n=N3(QAF, ZW("الْإِسْقَامُ وَالْإِبْرَاءُ مَصْدَرَانِ؛ يُرِيدُ أَنَّ الِاسْتِقْصَاءَ يُبَيِّنُ بَرَاءَتَنَا مِنَ الذَّنْبِ، وَالذَّنْبُ ذَنْبُكُمْ", "إِسْقَام and إِبْرَاء are masdars; he means that probing will show us clear of guilt, and the guilt yours", "«iskâm» ve «ibrâ» masdardır; araştırmanın bizim suçsuzluğumuzu göstereceğini, suçun sizin olduğunu kastediyor"),
     HADD("طِبَاقٌ بَيْنَ «الْإِسْقَامُ» وَ«الْإِبْرَاءُ»", "a ṭibāq between «sickness» and «cure»", "«hastalık» ile «şifa» arasında tıbâk")))])
VV(32, "or if you keep silent about us, we are like one who shuts an eye with motes in its lid.",
  "ya da bizim hakkımızda susarsanız, biz de göz kapağında çöpler bulunan bir gözü yuman kimse gibiyiz.",
 [AW(),
  V("mtum", "سَكَتُّمْ", "sakata", n=NT("وَأُدْغِمَتْ تَاؤُهُ فِي التَّاءِ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «نَبَشْتُمْ»", "its ta merges into the ta of the doer; the clause is joined to «you dig up»", "tâsı fâil tâsına idgam edilmiştir; cümle «eşelerseniz»e ma'tûftur")),
  JP("عَنَّا", "an", "نَا", n=MT("سَكَتُّمْ", "you keep silent", "susarsanız»a")),
  T("فَكُنَّا", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ شَرْطٍ مُقَدَّرٍ (أَوْ إِنْ سَكَتُّمْ)، وَ«كَانَ» فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ الْمُقَدَّرِ (الدُّرَّةُ).",
    "The fa opens the answer of an understood condition («or if you keep silent»); كَانَ is a defective past verb built on sukun because نَا is attached, and نَا is its noun, in the seat of raf' — the clause is the answer of the understood condition, in the seat of jazm (al-Durra).", "Fâ takdir edilen şartın («veya eğer susarsanız») cevabının başındadır; «kâne», «nâ» bitiştiği için sükûn üzere mebnî nâkıs mâzî; «nâ» ismidir, mahallen merfû — cümle takdir edilen şartın cevabı olarak mahallen meczûm (Dürre).",
    segs=SG(("فَ", "fa", "conj"), ("كُنَّ", "kana", "verb"), ("ا", "pron-1p", "pron"))),
  T("كَمَنْ", "ka", "prep", ["huruf-jarr", "ism-mawsul", "kana-wa-akhawatuha"] + TB + ["aqsam-wajh-al-shabah"], "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «كَانَ» — وَفِيهِ تَشْبِيهُ تَمْثِيلٍ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ حَالُهُمْ فِي الْإِعْرَاضِ عَنْهُمْ مَعَ إِضْمَارِ الْحِقْدِ، وَالْمُشَبَّهُ بِهِ حَالُ مَنْ أَغْمَضَ عَيْنًا فِي جَفْنِهَا الْقَذَى، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ هَيْئَةُ مَنْ يُغْضِي عَلَى أَذًى يَكْتُمُهُ — وَصَفَهُ الزَّوْزَنِيُّ: «أَعْرَضْنَا عَنْكُمْ مَعَ إِضْمَارِنَا الْحِقْدَ عَلَيْكُمْ، كَمَنْ أَغْضَى الْجُفُونَ عَنِ الْقَذَى»، وَتَسْمِيَتُهُ تَمْثِيلًا عَلَى حَدِّ التَّلْخِيصِ.",
    "The kaf is the jarr letter of likening, and «مَنْ» is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on the omitted predicate of كَانَ — a tashbih of tamthīl, mursal and mujmal: their state, turning away while hiding rancour, is likened to the state of one who shuts an eye with motes in its lid; the particle is the kaf; the point of likeness is the figure of one who looks past a hurt he keeps hidden — al-Zawzanī describes it: «we turn from you while hiding our rancour against you, like one who lowers his lids over a mote»; the name tamthīl is by the Talkhīṣ's definition.",
    "Kâf teşbîh ve cer harfi; «men» sükûn üzere mebnî ism-i mevsûl, kâf ile mahallen mecrûr; câr-mecrûr «kâne»nin mahzûf haberine müteallik — temsîlî teşbîh, mürsel ve mücmel: kini gizleyerek yüz çevirme hâlleri, göz kapağında çöp bulunan gözünü yuman kimsenin hâline benzetilmiştir; edat kâf; vech-i şebeh, gizlediği bir acıya göz yuman kimsenin hey'etidir — Zevzenî tarif eder: «size kinimizi gizleyerek yüz çeviririz, çöpe göz kapaklarını yuman kimse gibi»; temsîl adı Telhîs'in tarifine göredir.",
    segs=SG(("كَ", "ka", "prep"), ("مَنْ", "man", "pron")))],
 [V("m", "أَغْمَضَ", "aghmada-hr", doer=HUWA("«مَنْ»", "«one who»", "«men»e"), g=["form-iv-verbs"], n=CL("sila")),
  R("maf", "عَيْنًا", "ayn-eye"),
  PR("فِي", "fi", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "جَفْنِهَا", "jafn", enc="هَا"),
  R("mub", "الْأَقْذَاءُ", "qadha", g=["jam-taksir"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«عَيْنًا»", "placed after; the nominal clause is a na't of «an eye», in the seat of nasb", "sona bırakılmıştır; isim cümlesi «bir göz»ün na'tı, mahallen mansûb"), QAF, ZW("الْأَقْذَاءُ: جَمْعُ الْقَذَى، وَالْقَذَى جَمْعُ قَذَاةٍ", "أَقْذَاء is the plural of قَذًى, itself the plural of قَذَاة, a mote", "«akzâ» «kazâ»nın, o da «kazât»ın (çöp) çoğuludur")))])
VV(33, "or if you withhold what you are asked — then who is it you were told of, that has the upper hand over us?",
  "ya da sizden istenen şeyi esirgerseniz — o zaman, bize üstün olduğu size haber verilen kim var ki?",
 [AW(),
  V("mtum", "مَنَعْتُمْ", "manaa", n=NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «نَبَشْتُمْ»", "the clause is joined to «you dig up»", "cümle «eşelerseniz»e ma'tûftur")),
  PT("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "a relative noun built on sukun, in the seat of nasb as the object", "sükûn üzere mebnî ism-i mevsûl, mef'ûlün bih olarak mahallen mansûb", g=["ism-mawsul", "maful-bihi"], pos="pron"),
  V("d5", "تُسْأَلُونَ", "saala", pas=True, g=["afal-khamsa", "mafulayn"], n=N3(NT("وَالْوَاوُ هِيَ الْمَفْعُولُ الْأَوَّلُ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ، وَهُوَ الْمَفْعُولُ الثَّانِي: تُسْأَلُونَهُ", "the waw is the first object — the clause is the relative's ṣila; the pronoun referring back is left out, the second object: «you are asked it»", "vâv birinci mef'ûldür — cümle sıladır; dönen zamir mahzûftur, ikinci mef'ûldür: «sizden istenen»"), ZW("مَا سَأَلْنَاكُمْ مِنَ الْمُهَادَنَةِ وَالْمُوَادَعَةِ", "what we asked of you: truce and peace", "sizden istediğimiz ateşkes ve barış"))),
  PT("فَمَنْ", "man", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ شَرْطٍ مُقَدَّرٍ (أَوْ إِنْ مَنَعْتُمْ)، وَ«مَنْ» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ الْمُقَدَّرِ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى النَّفْيِ: «اسْمُ اسْتِفْهَامٍ مُفِيدٌ لِلنَّفْيِ» (الدُّرَّةُ)، «أَيْ لَا قَوْمَ أَشْرَفُ مِنَّا» (الزَّوْزَنِيُّ)",
    "the fa opens the answer of an understood condition («or if you withhold»), and «مَنْ» is a question noun built on sukun, in the seat of raf' as mubtada; the clause is that answer, in the seat of jazm — the question has left asking for denial: «a question noun giving denial» (al-Durra), «that is, no people is nobler than we» (al-Zawzanī)",
    "fâ takdir edilen şartın («veya eğer esirgerseniz») cevabının başındadır; «men» sükûn üzere mebnî istifhâm ismi, mübtedâ olarak mahallen merfû; cümle o cevap olarak mahallen meczûm — istifhâm nefy anlamına çıkmıştır: «nefy ifade eden istifhâm ismi» (Dürre), «yani bizden şerefli kavim yoktur» (Zevzenî)",
    g=["al-istifham", "khuruj-al-istifham", "mubtada-khabar"], pos="pron", segs=SG(("فَ", "fa", "conj"), ("مَنْ", "man", "pron")))],
 [T("حُدِّثْتُمُوهُ", "haddatha", "verb", ["naib-al-fail", "form-ii-verbs", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ وَهُوَ الْمَفْعُولُ الْأَوَّلُ، وَالْمِيمُ عَلَامَةُ الْجَمْعِ حُرِّكَتْ بِالضَّمِّ فَتَوَلَّدَتْ وَاوُ الْإِشْبَاعِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَنْ».",
    "A passive past verb, built on sukun because the subject pronoun is attached; the ta is the deputy doer, the first object, in the seat of raf'; the mim marks the plural and, voweled with damma, grows the waw of ishbāʿ; the ha is the second object, in the seat of nasb — the clause is the khabar of «who», in the seat of raf'.",
    "Meçhul mâzî; ref zamiri bitiştiği için sükûn üzere mebnî; tâ nâib-i fâil — birinci mef'ûl — mahallen merfû; mîm cemʿ alâmetidir, damme ile harekelenince işbâ vâvı doğmuştur; hâ ikinci mef'ûl, mahallen mansûb — cümle «men»in haberi, mahallen merfû.",
    segs=SG(("حُدِّثْتُمُو", "haddatha", "verb"), ("هُ", "pron-3ms", "pron"))),
  JP("لَهُ", "li", "هُ", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  JP("عَلَيْنَا", "ala", "نَا", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْخَبَرِ الْمَحْذُوفِ، أَوْ بِمَحْذُوفٍ خَبَرٍ ثَانٍ (الدُّرَّةُ)", "the phrase hangs on the omitted khabar, or on an omitted second khabar (al-Durra)", "câr-mecrûr mahzûf habere, ya da mahzûf ikinci habere müteallik (Dürre)")),
  R("mub", "الْعَلَاءُ", "ala-height-hr", n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَالِثٌ لِـ«حُدِّثَ» (الدُّرَّةُ)", "placed after; the nominal clause is the third object of «you were told», in the seat of nasb (al-Durra)", "sona bırakılmıştır; isim cümlesi «haber verildi»nin üçüncü mef'ûlü, mahallen mansûb (Dürre)"), QAF, ZW("فَأَيُّ قَوْمٍ أُخْبِرْتُمْ عَنْهُمْ أَنَّهُمْ فَضَلُونَا؟ أَيْ لَا قَوْمَ أَشْرَفُ مِنَّا، فَلَا نَعْجِزُ عَنْ مُقَابَلَتِكُمْ بِمِثْلِ صَنِيعِكُمْ", "which people were you told of that surpassed us? — none is nobler than we, so we are not unable to pay you back in kind", "bizi geçtiği size haber verilen hangi kavim var? — bizden şerefli kavim yoktur; size yaptığınızın mislini yapmaktan âciz değiliz")))])
VV(34, "Do you know of the days when men were plundered in raid upon raid, and every tribe was howling?",
  "İnsanların karşılıklı baskınlarla yağmalandığı, her kabilenin feryat ettiği günleri bilmez misiniz?",
 [PT("هَلْ", "hal-istifham", "حَرْفُ اسْتِفْهَامٍ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى التَّقْرِيرِ: «حَرْفُ اسْتِفْهَامٍ مَعْنَاهُ التَّقْرِيرُ» (الدُّرَّةُ)؛ وَقَالَ الزَّوْزَنِيُّ: «وَهَلْ فِي الْبَيْتِ بِمَعْنَى قَدْ، لِأَنَّهُ يَحْتَجُّ عَلَيْهِمْ بِمَا عَلِمُوهُ»", "a particle of question — the question has left asking for affirmation: «a question particle meaning taqrīr» (al-Durra); al-Zawzanī: «هَلْ in the verse means قَدْ, for he argues against them from what they know»", "istifhâm harfi — istifhâm takrîr (ikrar ettirme) anlamına çıkmıştır: «anlamı takrîr olan istifhâm harfi» (Dürre); Zevzenî: «beyitteki hel, kad anlamındadır; çünkü onlara bildikleriyle delil getiriyor»", g=["al-istifham", "khuruj-al-istifham"]),
  V("mtum", "عَلِمْتُمْ", "alima", n=CL("ist")),
  R("maf", "أَيَّامَ", "yawm", mud=True, g=["jam-taksir"], n=NT("وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ جَرٍّ بِإِضَافَتِهِ إِلَيْهَا", "the clause after it is in the seat of jarr, it being annexed to that clause", "sonraki cümle, ona muzâf olduğu için mahallen mecrûr")),
  V("d", "يُنْتَهَبُ", "intahaba-amr", pas=True, g=["form-viii-verbs"], n=ZW("الِانْتِهَابُ: الْإِغَارَةُ", "اِنْتِهَاب is raiding", "«intihâb»: baskın"))],
 [R("naib", "النَّاسُ", "nas"),
  R("mutlaq", "غِوَارًا", "ghiwar-hr", g=["masdar"], n=N3(DR("عَامِلُهُ «يُنْتَهَبُ» إِذْ هُوَ بِمَعْنَاهُ: يُغَاوِرُونَ غِوَارًا", "governed by «are plundered», which shares its sense: «they raid one another in raids»", "âmili, aynı anlamda olduğu için «yağmalanır»dır: «baskın üstüne baskın yaparlar»"), ZW("الْغِوَارُ: الْمُغَاوَرَةُ", "غِوَار is raiding one another", "«ğıvâr»: karşılıklı baskın"))),
  R("majr", "لِكُلِّ", "kull", j="li", mud=True, n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mdf", "حَيٍّ", "hayy-tribe"),
  R("mub", "عُوَاءُ", "uwa-hr", g=["istiara", "aqsam-al-istiara"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ مُسْتَأْنَفَةٌ (الدُّرَّةُ)", "placed after; a fresh sentence (al-Durra)", "sona bırakılmıştır; cümle müste'nefedir (Dürre)"), QAF_N,
     NT("وَفِيهِ اسْتِعَارَةٌ: «الْعُوَاءُ: صَوْتُ الذِّئْبِ وَنَحْوِهِ، وَهُوَ هَاهُنَا مُسْتَعَارٌ لِلضَّجِيجِ وَالصِّيَاحِ» (الزَّوْزَنِيُّ)؛ وَهِيَ تَصْرِيحِيَّةٌ عَلَى حَدِّ التَّلْخِيصِ", "an istiʿāra: «عُوَاء is the howl of the wolf and the like, borrowed here for clamour and shouting» (al-Zawzanī); it is taṣrīḥiyya by the Talkhīṣ's definition", "istiâre: «uvâ', kurt ve benzerinin ulumasıdır; burada gürültü ve bağırış için istiâre edilmiştir» (Zevzenî); Telhîs'in tarifine göre tasrîhiyyedir")))])
VV(35, "when we drove the camels hard from the palm-fronds of al-Baḥrayn, until al-Ḥisāʾ brought them to a halt.",
  "develerimizi Bahreyn'in hurma dallarından alabildiğine sürdüğümüz, ta ki Hisâ onları durdurana dek.",
 [PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«عَلِمْتُمْ» فِي الْبَيْتِ قَبْلَهُ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb of past time built on sukun, in the seat of nasb, hanging on «you know» in the verse before, annexed to the clause after it", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; önceki beyitteki «bilirsiniz»e müteallik, sonraki cümleye muzâf", g=["maful-fih"], pos="noun"),
  V("mna", "رَفَعْنَا", "rafaa", n=CL("mdf", "إِذْ", "إِذْ", "iz")),
  R("maf", "الْجِمَالَ", "jamal-camel", g=["jam-taksir"]),
  PR("مِنْ", "min", n=MT("رَفَعْنَا", "we drove", "sürdük»e")),
  R("majr", "سَعَفِ", "saaf-hr", mud=True, n=ZW("السَّعَفُ: أَغْصَانُ النَّخْلَةِ، وَالْوَاحِدَةُ سَعَفَةٌ", "سَعَف are palm branches; one is سَعَفَة", "«sa'af»: hurma dalları; tekili «sa'afe»"))],
 [T("الْبَحْرَيْنِ", "bahrayn-hr", "propn", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ عَلَى صُورَةِ الْمُثَنَّى، وَهُوَ اسْمُ مَوْضِعٍ — وَجَعَلَهُ الدُّرَّةُ مَبْنِيًّا عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ.",
    "The second term of the idafa, in jarr by the ya in the shape of a dual; it is the name of a place — al-Durra treats it as built on kasra in the seat of jarr.", "Muzâfun ileyh, tesniye kalıbında yâ ile mecrûr; bir yer adıdır — Dürre onu kesre üzere mebnî, mahallen mecrûr sayar."),
  R("mutlaq", "سَيْرًا", "sayr", g=["masdar", "ijaz-al-hadhf"], n=N3(DR("عَامِلُهُ «رَفَعْنَا» إِذْ هُوَ بِمَعْنَاهُ، وَقِيلَ: عَامِلُهُ مَحْذُوفٌ تَقْدِيرُهُ: فَسَارَتْ سَيْرًا", "governed by «we drove», which shares its sense; others: its governor is left out, «and they went a going»", "âmili, aynı anlamda olduğu için «sürdük»tür; âmilinin mahzûf olduğu da söylenmiştir: «gittiler gidiş»"),
     NT("وَعَلَى الثَّانِي فِيهِ إِيجَازُ الْحَذْفِ: «أَيْ فَسَارَتْ سَيْرًا، فَحَذَفَ الْفِعْلَ لِدَلَالَةِ الْمَصْدَرِ عَلَيْهِ» (الزَّوْزَنِيُّ)", "on the second view it is an ījāz by omission: «that is, they went a going — he dropped the verb because the masdar shows it» (al-Zawzanī)", "ikinci görüşe göre îcâz-ı hazf vardır: «yani gittiler gidiş; masdar ona delâlet ettiği için fiili hazfetti» (Zevzenî)"))),
  PT("حَتَّى", "hatta", "حَرْفُ غَايَةٍ وَجَرٍّ، وَبَعْدَهُ «أَنْ» مُضْمَرَةٌ (الدُّرَّةُ) — وَقِيلَ: حَرْفُ ابْتِدَاءٍ وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ", "a jarr letter of «until», with an أَنْ understood after it (al-Durra) — others: a particle opening a fresh clause", "gâye ve cer harfi; ardında gizli bir «en» vardır (Dürre) — ibtidâ harfi olduğu ve sonraki cümlenin müste'nef olduğu da söylenmiştir", g=["huruf-jarr", "ila-hatta-fi-wal-ba-fil-kafiya"], pos="prep"),
  V("ma", "نَهَاهَا", "naha", enc="هَا", g=["naqis-verbs"], n=DR("وَهُوَ فِي مَحَلِّ نَصْبٍ بِـ«أَنْ» الْمُضْمَرَةِ، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِـ«حَتَّى»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَفَعْنَا»", "it is in the seat of nasb by the understood أَنْ; the masdar so made is in jarr after حَتَّى, and the phrase hangs on «we drove»", "gizli «en» ile mahallen mansûbdur; te'vil edilen masdar «hattâ» ile mecrûr, câr-mecrûr «sürdük»e müteallik")),
  R("fail", "الْحِسَاءُ", "hisa-hr", pos="propn", n=N3(QAF, ZW("الْحِسَاءُ: مَوْضِعٌ بِعَيْنِهِ؛ أَيْ طَوَيْنَا مَا بَيْنَ هٰذَيْنِ الْمَوْضِعَيْنِ سَيْرًا وَإِغَارَةً عَلَى الْقَبَائِلِ", "al-Ḥisāʾ is a particular place: we covered the ground between these two places, marching and raiding the tribes", "Hisâ belli bir yerdir: bu iki yer arasını yürüyerek ve kabilelere baskın yaparak kat ettik")))])
# =====================================================================================================================
# The poem — vv. 36–42 — يَوْمَ مِلْنَا عَلَى تَمِيمٍ
# =====================================================================================================================
THUMMA = lambda: PT("ثُمَّ", "thumma", "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي", "a conjunction of order with an interval", "tertip ve terâhî bildiren atıf harfi", g=["atf-nasaq"])
VV(36, "Then we turned upon Tamīm, and the sacred month came upon us with daughters of a people among us as slave-girls.",
  "Sonra Temîm'e yöneldik; haram aya girdiğimizde aramızda bir kavmin kızları cariyeydi.",
 [THUMMA(),
  V("mna", "مِلْنَا", "mala", g=["hollow-verbs"], n=NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «رَفَعْنَا» فَهِيَ فِي مَحَلِّ جَرٍّ مِثْلُهَا (الدُّرَّةُ)", "its middle letter drops where two quiescents meet; the clause is joined to «we drove» and, like it, is in the seat of jarr (al-Durra)", "orta harfi iki sâkin karşılaştığı için düşmüştür; cümle «sürdük»e ma'tûftur, onun gibi mahallen mecrûrdur (Dürre)")),
  PR("عَلَى", "ala", n=MT("مِلْنَا", "we turned", "yöneldik»e")),
  NAME("majr", "تَمِيمٍ", "tamim", n=ZW("ثُمَّ مِلْنَا مِنَ الْحِسَاءِ فَأَغَرْنَا عَلَى بَنِي تَمِيمٍ", "then we turned from al-Ḥisāʾ and raided the Banū Tamīm", "sonra Hisâ'dan dönüp Benî Temîm'e baskın yaptık"))],
 [V("mna", "فَأَحْرَمْنَا", "ahrama-hr", c="f", g=["form-iv-verbs"], n=N3(NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is joined to what goes before", "cümle öncekine ma'tûftur"), ZW("أَحْرَمْنَا: أَيْ دَخَلْنَا فِي الشَّهْرِ الْحَرَامِ", "أَحْرَمْنَا: we entered the sacred month", "«ahramnâ»: haram aya girdik"))),
  JP("وَفِينَا", "fi", "نَا", c="wh", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «إِمَاءُ»: كَانَ صِفَةً لَهُ فَلَمَّا قُدِّمَ عَلَيْهِ صَارَ حَالًا", "the phrase hangs on an omitted hal of «slave-girls»: it was its adjective, and placed before it became a hal", "câr-mecrûr «cariyeler»den mahzûf bir hâle müteallik: onun sıfatı idi, öne alınınca hâl oldu")),
  R("mub", "بَنَاتُ", "bint", mud=True, g=["jam-muannath-salim"]),
  R("mdf", "قَوْمٍ", "qawm", n=DR("وَرِوَايَتُهُ «بَنَاتُ مُرٍّ»", "his text reads «the daughters of Murr»", "onun rivayeti «benâtu Murrin»dir")),
  R("khb", "إِمَاءُ", "ama-handmaid", g=["jam-taksir"], n=N3(DR("وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَا» الْفَاعِلِ، وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ", "the nominal clause is a hal of the doer «we», in the seat of nasb; the links are the waw and the pronoun", "isim cümlesi fâil «nâ»dan hâl, mahallen mansûb; bağlayıcılar vâv ve zamirdir"), QAF_N, ZW("فَبَنَاتُ الَّذِينَ أَغَرْنَا عَلَيْهِمْ كُنَّ إِمَاءً لَنَا", "the daughters of those we had raided were slave-girls to us", "baskın yaptığımız kimselerin kızları bize cariye olmuştu")))])
VV(37, "The mighty would not stay in the level land, and flight did not help the lowly.",
  "Güçlü olan düz arazide kalmazdı; zayıfa da kaçmak fayda vermezdi.",
 [LA_N(),
  V("d", "يُقِيمُ", "aqama", g=["form-iv-verbs", "hollow-verbs"], n=CL("ist")),
  R("fail", "الْعَزِيزُ", "aziz", g=["sifa-mushabbaha"]),
  R("majr", "بِالْبَلَدِ", "balad", j="bi", n=N3(MT("يُقِيمُ", "stays", "kalır»a"), DR("وَرِوَايَتُهُ «فِي الْبَلَدِ»", "his text reads «in the land»", "onun rivayeti «fi'l-beledi»dir")))],
 [R("naatj", "السَّهْلِ", "sahl", of=("الْبَلَدِ", "the land", "el-beled")),
  LA_N("وَلَا", c="w"),
  V("d", "يَنْفَعُ", "nafaa", n=CL("atf", "لَا يُقِيمُ", "does not stay", "kalmaz")),
  R("maf", "الذَّلِيلَ", "dhalil", g=["sifa-mushabbaha", "tibaq"], n=HADD("طِبَاقٌ بَيْنَ «الْعَزِيزُ» وَ«الذَّلِيلَ»", "a ṭibāq between «the mighty» and «the lowly»", "«güçlü» ile «zayıf» arasında tıbâk")),
  R("fail", "النَّجَاءُ", "naja-speed-tf", n=N3(QAF, ZW("النَّجَاءُ — مَمْدُودًا وَمَقْصُورًا —: الْإِسْرَاعُ فِي السَّيْرِ؛ يُرِيدُ أَنَّ الشَّرَّ كَانَ شَامِلًا عَامًّا لَمْ يَسْلَمْ مِنْهُ الْعَزِيزُ وَلَا الذَّلِيلُ", "نَجَاء, long or short, is speed in going; he means that the evil was all-embracing, sparing neither the mighty nor the lowly", "«necâ» — memdûd ve maksûr —: yürüyüşte hız; kötülüğün herkesi kapsadığını, ne güçlünün ne zayıfın ondan kurtulduğunu kastediyor")))])
VV(38, "The one who flees from us is not saved by a mountain-top, nor by a rugged field of black stones.",
  "Bizden kaçanı ne bir dağ başı kurtarır ne de yürünmesi zor kara taşlı bir arazi.",
 [T("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، وَالْجُمْلَةُ بَعْدَهُ خَبَرُهُ — وَأَجَازَ الدُّرَّةُ أَنْ يَكُونَ «رَأْسُ طَوْدٍ» اسْمَهُ مُؤَخَّرًا، وَأَنْ تَكُونَ «لَيْسَ» حَرْفَ نَفْيٍ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "A defective, non-conjugating past verb built on fatha; its noun is the pronoun of the matter, left out, and the clause after it is its predicate — al-Durra also allows «a mountain-top» as its noun placed after, or لَيْسَ as a mere particle of negation; a fresh sentence.", "Câmid nâkıs mâzî, fetha üzere mebnî; ismi mahzûf şa'n zamiri, sonraki cümle haberidir — Dürre «dağ başı»nın sona bırakılmış ismi olmasını, ya da «leyse»nin nefy harfi olmasını da caiz görür; cümle müste'nefedir."),
  V("dy", "يُنْجِي", "anjaa", g=["form-iv-verbs", "naqis-verbs"], n=CL("khbn", "لَيْسَ", "لَيْسَ", "leyse")),
  PT("الَّذِي", "alladhi", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "a relative noun built on sukun, in the seat of nasb as the object", "sükûn üzere mebnî ism-i mevsûl, mef'ûlün bih olarak mahallen mansûb", g=["ism-mawsul", "maful-bihi"], pos="pron"),
  V("d", "يُوَائِلُ", "waala-hr", doer=HUWA("«الَّذِي»", "«the one who»", "«ellezî»ye"), g=["form-iii-verbs"], n=N3(CL("sila"), DR("وَرِوَايَتُهُ «لَيْسَ يُنْجِي مُوَائِلًا مِنْ حَذَارِ»", "his text reads «it does not save one fleeing from fear»", "onun rivayeti: «korkudan kaçanı kurtarmaz»"), ZW("وَأَلَ وَوَاءَلَ: أَيْ هَرَبَ وَفَزِعَ", "وَأَلَ and وَاءَلَ: he fled in fear", "«veele» ve «vâele»: korkup kaçtı"))),
  JP("مِنَّا", "min", "نَا", n=MT("يُوَائِلُ", "flees", "kaçar»a"))],
 [R("fail", "رَأْسُ", "ras", mud=True),
  R("mdf", "طَوْدٍ", "tawd-hr"),
  R("atfr", "وَحَرَّةٌ", "harra-hr", c="w", of=("رَأْسُ", "top", "re's")),
  R("naatr", "رَجْلَاءُ", "rajla-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("حَرَّةٌ", "stony field", "harra"), n=N3(QAF, ZW("الرَّجْلَاءُ: الْغَلِيظَةُ الشَّدِيدَةُ؛ لَمْ يَنْجُ الْهَارِبُ مِنَّا تَحَصُّنُهُ بِالْجَبَلِ وَلَا بِالْحَرَّةِ", "رَجْلَاء is rough and hard: the fugitive from us was not saved by taking refuge on a mountain or in a lava-field", "«raclâ»: sert ve çetin; bizden kaçan, dağa ya da harraya sığınmakla kurtulamadı")))])
VV(39, "A king who has humbled mankind — there is not found among them one equal to what is his.",
  "İnsanları boyun eğdirmiş bir kral; aralarında onda olana denk biri bulunmaz.",
 [R("khb", "مَلِكٌ", "malik-king", g=["hadhf-wa-taqdir"], n=N3(NT("وَالْمُبْتَدَأُ مَحْذُوفٌ تَقْدِيرُهُ: هُوَ (الدُّرَّةُ)", "its mubtada is left out: «he is» (al-Durra)", "mübtedâsı mahzûftur: «o» (Dürre)"), ZW("هُوَ مَلِكٌ ذَلَّلَ وَقَهَرَ الْخَلْقَ فَمَا يُوجَدُ فِيهِمْ مَنْ يُسَاوِيهِ فِي مَعَالِيهِ", "he is a king who humbled and subdued mankind, and none among them equals him in his high deeds", "insanları boyun eğdirip kahretmiş bir kraldır; yüce işlerinde ona denk kimse bulunmaz"))),
  V("m", "أَضْرَعَ", "adraa-hr", doer=HUWA("«مَلِكٌ»", "the king", "«melik»e"), g=["form-iv-verbs"], n=N3(CL("nr", "مَلِكٌ", "a king", "melikün»"), DR("وَرِوَايَتُهُ «أَضْلَعُ الْبَرِيَّةِ» اسْمًا صِفَةً لِـ«مَلِكٌ»، وَمَنْ رَوَى «أَضْرَعَ» فَهُوَ فِعْلٌ مَاضٍ", "his text reads «أَضْلَعُ الْبَرِيَّةِ», a noun, the adjective of «king»; whoever relates «أَضْرَعَ» makes it a past verb", "onun rivayeti «edla'u'l-beriyye» olup «melik»in sıfatıdır; «adra'a» diye rivayet eden onu mâzî fiil sayar"),
     ZW("أَضْرَعَ: ذَلَّلَ وَقَهَرَ، وَمِنْهُ قَوْلُهُمْ فِي الْمَثَلِ: الْحُمَّى أَضْرَعَتْنِي لَكَ", "أَضْرَعَ is to humble and subdue; so the proverb «fever has humbled me before you»", "«adra'a»: zelil ve mağlup etti; atasözü: «humma beni sana muhtaç etti»"))),
  R("maf", "الْبَرِيَّةَ", "bariyya"),
  LA_N()],
 [V("d", "يُوجَدُ", "wajada", pas=True, g=["mithal-verbs"], n=NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ ثَانِيَةٌ لِـ«مَلِكٌ»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ (الدُّرَّةُ)", "the clause is a second adjective of «king», in the seat of raf', or a hal of it, in the seat of nasb (al-Durra)", "cümle «melik»in ikinci sıfatı olarak mahallen merfû, ya da ondan hâl olarak mahallen mansûb (Dürre)")),
  JP("فِيهَا", "fi", "هَا", n=MT("يُوجَدُ", "is found", "bulunur»a")),
  T("لِمَا", "li", "prep", ["huruf-jarr", "ism-mawsul"], "اللَّامُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِاللَّامِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«كِفَاءُ» (الدُّرَّةُ).",
    "The lam is a jarr letter, and «مَا» is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «an equal» (al-Durra).", "Lâm cer harfi; «mâ» sükûn üzere mebnî ism-i mevsûl, lâm ile mahallen mecrûr; câr-mecrûr «denk»e müteallik (Dürre).", segs=SG(("لِ", "li", "prep"), ("مَا", "ma-mawsula", "pron"))),
  T("لَدَيْهِ", "lada", "noun", ["maful-fih", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةِ الْمَوْصُولِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.",
    "An adverb of place built on sukun, in the seat of nasb, hanging on the omitted ṣila of the relative; the ha is an attached pronoun in the seat of jarr as the second term of the idafa.", "Sükûn üzere mebnî mekân zarfı, mahallen mansûb, mevsûlün mahzûf sılasına müteallik; hâ bitişik zamir, muzâfun ileyh olarak mahallen mecrûr.", segs=SG(("لَدَيْ", "lada", "noun"), ("هِ", "pron-3ms", "pron"))),
  R("naib", "كِفَاءُ", "kifa-hr", g=["masdar"], n=N3(QAF_N, ZW("الْكَفَاءَةُ وَالْمُكَافَأَةُ: الْمُسَاوَاةُ، وَالْكِفَاءُ بِمَعْنَى الْمُكَافِئِ، فَالْمَصْدَرُ مَوْضُوعٌ مَوْضِعَ اسْمِ الْفَاعِلِ", "كَفَاءَة and مُكَافَأَة are equality; كِفَاء means «an equal» — the masdar set in the place of the active participle", "«kefâe» ve «mükâfee»: denklik; «kifâ'» denk anlamındadır — masdar ism-i fâil yerine konmuştur")))])
VV(40, "(Did you bear) the like of the hardships our people bore when al-Mundhir went raiding? Are we herdsmen to the son of Hind?",
  "Münzir savaşa çıktığında kavmimizin katlandığı zorluklar gibisine (siz katlandınız mı)? Biz Hind'in oğlunun çobanları mıyız?",
 [T("كَتَكَالِيفِ", "takalif", "noun", ["huruf-jarr", "jam-taksir", "maful-mutlaq", "ijaz-al-hadhf", "idafa-definiteness"], "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«تَكَالِيفِ» مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ، مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ مَعَ فِعْلِهِ: هَلْ تَكَلَّفْتُمْ تَكَلُّفًا كَائِنًا كَتَكَالِيفِ قَوْمِنَا (الدُّرَّةُ) — وَفِيهِ إِيجَازُ الْحَذْفِ: حُذِفَ الْفِعْلُ وَمَصْدَرُهُ لِدَلَالَةِ الْكَلَامِ عَلَيْهِمَا، كَمَا قَدَّرَهُ الدُّرَّةُ وَشَرَحَهُ الزَّوْزَنِيُّ: «هَلْ قَاسَيْتُمْ مِنَ الْمَشَاقِّ وَالشَّدَائِدِ مَا قَاسَى قَوْمُنَا».",
    "The kaf is the jarr letter of likening, and «hardships» is in jarr by the kasra, being annexed; annexed. The phrase hangs on the omitted adjective of an absolute object dropped with its verb: «did you bear a bearing like the hardships of our people?» (al-Durra) — an ījāz by omission: the verb and its masdar are dropped because the speech shows them, as al-Durra restores and al-Zawzanī explains: «have you suffered of toil and hardship what our people suffered?»",
    "Kâf teşbîh ve cer harfi; «tekâlîf», muzâf olduğu için kesre ile mecrûr; muzâf. Câr-mecrûr, fiiliyle birlikte hazfedilmiş bir mef'ûl-i mutlakın mahzûf sıfatına müteallik: «kavmimizin zorlukları gibi bir zahmete katlandınız mı?» (Dürre) — îcâz-ı hazf: fiil ve masdarı, söz onlara delâlet ettiği için hazfedilmiştir; Dürre'nin takdiri ve Zevzenî'nin şerhi: «kavmimizin çektiği meşakkat ve zorlukları siz de çektiniz mi?»",
    segs=SG(("كَ", "ka", "prep"), ("تَكَالِيفِ", "takalif", "noun"))),
  R("mdf", "قَوْمِنَا", "qawm", enc="نَا", n=N3(DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti"), ZW("التَّكَالِيفُ: الْمَشَاقُّ وَالشَّدَائِدُ", "تَكَالِيف are toils and hardships", "«tekâlîf»: meşakkatler ve zorluklar"))),
  PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِالْمَصْدَرِ الْمَحْذُوفِ أَوْ بِفِعْلِهِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb of past time built on sukun, in the seat of nasb, hanging on the omitted masdar or its verb, annexed to the clause after it", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; mahzûf masdara ya da fiiline müteallik, sonraki cümleye muzâf", g=["maful-fih"], pos="noun"),
  V("ma", "غَزَا", "ghaza", g=["naqis-verbs"], n=CL("mdf", "إِذْ", "إِذْ", "iz"))],
 [NAME("fail", "الْمُنْذِرُ", "mundhir-name", n=ZW("حِينَ غَزَا مُنْذِرٌ أَعْدَاءَهُ فَحَارَبَهُمْ", "when al-Mundhir raided his enemies and fought them", "Münzir düşmanlarına sefer edip onlarla savaştığında")),
  PT("هَلْ", "hal-istifham", "حَرْفُ اسْتِفْهَامٍ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى الْإِنْكَارِ وَالتَّعْيِيرِ: «ذَكَرَ أَنَّهُمْ نَصَرُوا الْمَلِكَ حِينَ لَمْ يَنْصُرْهُ بَنُو تَغْلِبَ، وَعَيَّرَهُمْ بِأَنَّهُمْ رِعَاءُ الْمَلِكِ، وَقَوْمُهُ يَأْنَفُونَ مِنْ ذٰلِكَ» (الزَّوْزَنِيُّ)", "a particle of question — the question has left asking for denial and reproach: «he says that they helped the king when Taghlib did not, and taunts them with being the king's herdsmen, a thing his own people disdain» (al-Zawzanī)", "istifhâm harfi — istifhâm inkâr ve ayıplama anlamına çıkmıştır: «Tağlib kralı desteklemediğinde onların desteklediğini anar; onları kralın çobanları olmakla ayıplar, kendi kavmi ise bundan kaçınır» (Zevzenî)", g=["al-istifham", "khuruj-al-istifham"]),
  NAHNU_M("نَحْنُ", c=None),
  R("majr", "لِابْنِ", "ibn", j="li", mud=True, n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «رِعَاءُ»: كَانَ صِفَةً لَهُ فَلَمَّا قُدِّمَ صَارَ حَالًا", "the phrase hangs on an omitted hal of «herdsmen»: it was its adjective and, placed first, became a hal", "câr-mecrûr «çobanlar»dan mahzûf bir hâle müteallik: onun sıfatı idi, öne alınınca hâl oldu")),
  NAME("mdf", "هِنْدٍ", "hind"),
  R("khb", "رِعَاءُ", "rai", g=["jam-taksir"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ الْمَحْذُوفِ", "the clause is what an omitted «saying» says, in the seat of nasb", "cümle mahzûf «demek» fiilinin mekûlü, mahallen mansûb"), QAF_N, NT("وَالرِّعَاءُ: جَمْعُ الرَّاعِي (حَاشِيَةُ الْمُحَقِّقِ)", "رِعَاء is the plural of رَاعٍ (the editor's note)", "«riâ'» «râî»nin çoğuludur (muhakkikin dipnotu)")))])
VV(41, "Whatever man of Taghlib they strike down — his blood is lost unavenged; dust be on him when he is struck!",
  "Tağlib'den kimi vurdularsa, kanı heder olur; vurulduğunda üstüne toprak örtülsün!",
 [PT("مَا", "ma-shartiyya", "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِـ«أَصَابُوا» — وَأَجَازَ الدُّرَّةُ أَنْ يَكُونَ مُبْتَدَأً، أَوِ اسْمًا مَوْصُولًا خَبَرُهُ «مَطْلُولٌ»", "a conditional noun built on sukun, in the seat of nasb as the fronted object of «they strike» — al-Durra also allows it to be a mubtada, or a relative noun whose khabar is «lost unavenged»", "cezmeden şart ismi, sükûn üzere mebnî, «vurdular»ın öne alınmış mef'ûlü olarak mahallen mansûb — Dürre onun mübtedâ, ya da haberi «heder» olan ism-i mevsûl olmasını da caiz görür", g=["huruf-al-shart-fil-kafiya", "maful-bihi"], pos="pron"),
  V("mw", "أَصَابُوا", "asaba", g=["form-iv-verbs", "hollow-verbs"], n=N3(SHART, NT("وَالْأَلِفُ فَارِقَةٌ", "the alif is the separating alif", "elif fârikadır"))),
  PR("مِنْ", "min", n=DR("وَهِيَ بَيَانٌ لِمَا أُبْهِمَ فِي «مَا»؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ", "it explains what «whatever» leaves vague; the phrase hangs on an omitted hal", "«mâ»daki belirsizliği açıklar; câr-mecrûr mahzûf bir hâle müteallik")),
  R("majr", "تَغْلَبِيٍّ", "taghlabiyy-hr", g=["ism-mansub"], n=NT("نِسْبَةٌ إِلَى تَغْلِبَ بِفَتْحِ اللَّامِ", "the nisba of Taghlib, with fatha on the lam", "Tağlib'e nisbet, lâm fethalı"))],
 [R("khb", "فَمَطْلُولٌ", "matlul-hr", c="fj", g=["ism-maful", "hadhf-wa-taqdir"], n=N3(NT("وَالْمُبْتَدَأُ مَحْذُوفٌ: فَهُوَ مَطْلُولٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "its mubtada is left out — «then he is lost unavenged» — and the clause is the answer of the condition, in the seat of jazm", "mübtedâsı mahzûftur: «o hederdir»; cümle şartın cevabı olarak mahallen meczûm"), ZW("طُلَّ دَمُهُ وَأُطِلَّ: أُهْدِرَ", "طُلَّ دَمُهُ and أُطِلَّ: his blood went unavenged", "«tulle demuhû» ve «utılle»: kanı heder oldu"))),
  JP("عَلَيْهِ", "ala", "هُ", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  IDHA(n=DR("وَجَوَابُهُ مَحْذُوفٌ: إِذَا أُصِيبَ فَعَلَيْهِ الْعَفَاءُ، وَهِيَ وَمَدْخُولُهَا مُعْتَرِضَةٌ", "its answer is left out — «when he is struck, then dust be on him» — and it with its clause is a parenthesis", "cevabı mahzûftur: «vurulduğunda üstüne toprak»; o ve girdiği cümle mu'tarızadır")),
  V("m", "أُصِيبَ", "asaba", pas=True, doer=HUWA("التَّغْلَبِيِّ", "the man of Taghlib", "Tağlibli'ye"), g=["form-iv-verbs", "hollow-verbs"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), DR("وَرِوَايَتُهُ «إِذَا تَوَلَّى»", "his text reads «when he turns away»", "onun rivayeti «izâ tevellâ»dır"))),
  R("mub", "الْعَفَاءُ", "afa-hr", g=["khabar-fi-mana-al-insha"], n=N3(NT("مُؤَخَّرٌ", "placed after", "sona bırakılmıştır"), QAF,
     DR("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ مَعْنَاهَا الدُّعَاءُ، أَوْ تَفْسِيرٌ لِـ«مَطْلُولٌ» — وَفِيهِ الْخَبَرُ بِمَعْنَى الْإِنْشَاءِ: الدُّعَاءُ عَلَيْهِ", "the clause is a fresh one meaning a curse, or it explains «lost unavenged» — a khabar meaning inshāʾ: a curse upon him", "cümle müste'neftir, anlamı bedduadır; ya da «heder»in açıklamasıdır — inşâ anlamında haber: ona beddua"),
     ZW("الْعَفَاءُ: الدُّرُوسُ، وَهُوَ أَيْضًا التُّرَابُ الَّذِي يُغَطِّي الْأَثَرَ؛ أُهْدِرَتْ دِمَاؤُهُمْ حَتَّى كَأَنَّهَا غُطِّيَتْ بِالتُّرَابِ وَدَرَسَتْ", "عَفَاء is effacement, and also the dust that covers a trace: their blood went unavenged, as if covered with dust and effaced", "«afâ'»: silinip gitme; izi örten toprak da denir: kanları heder edildi, sanki toprakla örtülüp silindi")))])
VV(42, "when he set Maysūn's domed tent on the high ground — and the nearest of her dwellings is al-ʿAwṣāʾ.",
  "(kral) Meysûn'un kubbeli çadırını yüksek yere kondurduğunda — onun yurtlarının en yakını da Avsâ'dır.",
 [PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ: «وَإِنَّمَا كَانَ هٰذَا حِينَ أَنْزَلَ الْمَلِكُ قُبَّةَ هٰذِهِ الْمَرْأَةِ» (الزَّوْزَنِيُّ) — وَجَعَلَهُ الدُّرَّةُ بَدَلًا مِنْ «إِذْ» قَبْلَهُ فِي رِوَايَتِهِ", "an adverb of past time built on sukun, in the seat of nasb, annexed to the clause after it: «this was only when the king set down this woman's tent» (al-Zawzanī) — al-Durra makes it a badal of the إِذْ before it in his text", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb, sonraki cümleye muzâf: «bu ancak kral bu kadının çadırını kondurduğunda oldu» (Zevzenî) — Dürre onu kendi rivayetindeki önceki «iz»den bedel sayar", g=["maful-fih"], pos="noun"),
  V("m", "أَحَلَّ", "ahalla", doer=HUWA("الْمَلِكِ", "the king", "krala"), g=["form-iv-verbs", "doubled-verbs", "mafulayn"], n=CL("mdf", "إِذْ", "إِذْ", "iz")),
  R("maf1", "الْعَلْيَاءَ", "alya", n=DR("وَإِنْ نُصِبَ عَلَى نَزْعِ الْخَافِضِ فَلَا بَأْسَ؛ وَرِوَايَتُهُ «الْعَلَاةَ»", "it may also be in nasb by the dropping of a jarr letter; his text reads «الْعَلَاةَ»", "cer harfinin düşmesiyle mansûb da olabilir; onun rivayeti «el-alâte»dir")),
  R("maf2", "قُبَّةَ", "qubba", mud=True)],
 [NAME("mdf", "مَيْسُونَ", "maysun-hr", sign=S_DIPT_F, g=["mamnu-min-sarf"], n=ZW("مَيْسُونُ: امْرَأَةٌ", "Maysūn is a woman", "Meysûn bir kadındır")),
  R("mub", "فَأَدْنَى", "adna-hr", c="f", mud=True, sign=S_AR, g=["ism-tafdil", "ism-maqsur-manqus"]),
  R("mdf", "دِيَارِهَا", "dar", enc="هَا", g=["jam-taksir"]),
  PLACE("khb", "الْعَوْصَاءُ", "awsa-hr", c=None, n=N3(QAF, DR("وَالْجُمْلَةُ الِاسْمِيَّةُ مَعْطُوفَةٌ عَلَى الْفِعْلِيَّةِ قَبْلَهَا، فَهِيَ فِي مَحَلِّ جَرٍّ مِثْلُهَا", "the nominal clause is joined to the verbal clause before it and, like it, is in the seat of jarr", "isim cümlesi önceki fiil cümlesine ma'tûftur; onun gibi mahallen mecrûrdur"), ZW("وَعَوْصَاءُ الَّتِي هِيَ أَقْرَبُ دِيَارِهَا إِلَى الْمَلِكِ", "and al-ʿAwṣāʾ, the nearest of her dwellings to the king", "ve yurtlarının krala en yakını olan Avsâ")))])
# =====================================================================================================================
# The poem — vv. 43–49 — وَأَمْرُ اللهِ بِلْغٌ
# =====================================================================================================================
MALIK = HUWA("الْمَلِكِ", "the king", "krala")
VV(43, "And there gathered to him robber-bands from every tribe, as though they were eagles.",
  "Her kabileden yağmacı çeteler onun yanına toplandı; sanki kartallardı.",
 [V("mtq", "فَتَأَوَّتْ", "taawwa-hr", c="f", g=["form-v-verbs", "naqis-verbs"], n=N3(NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is joined to what goes before", "cümle öncekine ma'tûftur"), ZW("التَّأَوِّي: التَّجَمُّعُ", "تَأَوِّي is gathering together", "«teevvî»: toplanmak"))),
  JP("لَهُ", "li", "هُ", n=MT("تَأَوَّتْ", "gathered", "toplandı»ya")),
  R("fail", "قَرَاضِبَةٌ", "qurdub-hr", g=["jam-taksir"], n=ZW("الْقُرْضُوبُ وَالْقِرْضَابُ: اللِّصُّ الْخَبِيثُ، وَالْجَمْعُ الْقَرَاضِبَةُ", "قُرْضُوب and قِرْضَاب are a wicked robber; the plural is قَرَاضِبَة", "«kurdûb» ve «kırdâb»: kötü hırsız; çoğulu «karâdibe»")),
  PR("مِنْ", "min", n=MTH("صِفَةٍ لِـ«قَرَاضِبَةٌ»", "an omitted adjective of «robber-bands»", "«karâdibe»nin mahzûf sıfatına"))],
 [R("majr", "كُلِّ", "kull", mud=True),
  R("mdf", "حَيٍّ", "hayy-tribe"),
  KAANNA("كَأَنَّهُمْ", enc="هُمْ", g=TB, n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِـ«قَرَاضِبَةٌ»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهَا", "the clause is an adjective of «robber-bands», in the seat of raf', or a hal of them, in the seat of nasb", "cümle «karâdibe»nin sıfatı olarak mahallen merfû, ya da ondan hâl olarak mahallen mansûb"),
     NT("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْقَرَاضِبَةُ، وَالْمُشَبَّهُ بِهِ الْعِقْبَانُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الْقُوَّةُ وَالشَّجَاعَةُ — ذَكَرَهُ الزَّوْزَنِيُّ: «كَأَنَّهُمْ عِقْبَانٌ لِقُوَّتِهِمْ وَشَجَاعَتِهِمْ»", "a tashbih mursal mujmal: the robber-bands are likened to eagles; the particle is كَأَنَّ; the point of likeness — strength and courage — is al-Zawzanī's: «as though they were eagles, for their strength and courage»", "teşbîh-i mürsel mücmel: müşebbeh çeteler, müşebbehün bih kartallar, edat «keenne»; vech-i şebeh — güç ve cesaret — Zevzenî'dedir: «güçleri ve cesaretleri sebebiyle sanki kartallar»"))),
  R("khbka", "أَلْقَاءُ", "liqwa-hr", g=["jam-taksir"], n=N3(QAF_N, ZW("الْأَلْقَاءُ: جَمْعُ لَقْوَةٍ، وَهِيَ الْعُقَابُ", "أَلْقَاء is the plural of لَقْوَة, the eagle", "«elkâ'» «lakve»nin, yani kartalın çoğuludur")))])
VV(44, "He led them out with the two black things for provision — and God's command reaches its end, by which the wretched are made wretched.",
  "Onlara iki kara şeyle (su ve hurmayla) öncülük etti — Allah'ın emri yerini bulur; bedbahtlar onunla bedbaht olur.",
 [V("ma", "فَهَدَاهُمْ", "hada", c="f", enc="هُمْ", doer=MALIK, g=["naqis-verbs"], n=N3(DR("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا، وَالِاسْتِئْنَافُ مُمْكِنٌ", "the clause is joined to what goes before; a fresh start is also possible", "cümle öncekine ma'tûftur; isti'nâf da mümkündür"), ZW("هَدَاهُمْ: أَيْ تَقَدَّمَهُمْ، وَقَدْ يَكُونُ هَدَى بِمَعْنَى قَادَ", "هَدَاهُمْ: he went before them; هَدَى may also mean «led»", "«hedâhum»: önlerine düştü; «hedâ» «yönetti» anlamında da olabilir"))),
  R("majr", "بِالْأَسْوَدَيْنِ", "aswadan-hr", j="bi", sign=S_MUTHY, g=["al-muthanna"], n=N3(MTH("حَالٍ مِنَ الْفَاعِلِ الْمُسْتَتِرِ", "an omitted hal of the hidden doer", "gizli fâilden mahzûf bir hâle"), ZW("الْأَسْوَدَانِ: الْمَاءُ وَالتَّمْرُ؛ وَكَانَ يَتَقَدَّمُهُمْ وَمَعَهُ زَادُهُمْ مِنَ الْمَاءِ وَالتَّمْرِ", "the two black things are water and dates: he went before them with their provision of water and dates", "«iki kara»: su ve hurma; önlerinde yürüyordu, yanında sudan ve hurmadan azıkları vardı"))),
  R("mub", "وَأَمْرُ", "amr", c="wh", mud=True, n=DR("وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «هَدَاهُمْ» أَوْ مِنْ مَفْعُولِهِ، وَالرَّابِطُ الْوَاوُ", "the nominal clause is a hal of the doer of «led them» or of its object, in the seat of nasb; the waw is the link", "isim cümlesi «onlara öncülük etti»nin fâilinden ya da mef'ûlünden hâl, mahallen mansûb; bağlayıcı vâvdır")),
  R("mdf", "اللهِ", "allah", pos="propn", n=DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti"))],
 [R("khb", "بِلْغٌ", "bilgh-hr", n=ZW("وَأَمْرُ اللهِ بَالِغٌ", "God's command is reaching (its end)", "Allah'ın emri yerini bulur")),
  V("da", "تَشْقَى", "shaqiya", g=["naqis-verbs"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ لِلْمُبْتَدَأِ", "the clause is a second khabar of the mubtada, in the seat of raf'", "cümle mübtedânın ikinci haberi, mahallen merfû"), DR("وَرِوَايَتُهُ «يَشْقَى» بِالْيَاءِ", "his text reads it with ya", "onun rivayeti yâ iledir"))),
  JP("بِهِ", "bi", "هُ", n=MT("تَشْقَى", "are made wretched", "bedbaht olur»a")),
  R("fail", "الْأَشْقِيَاءُ", "shaqi", g=["jam-taksir", "mulhaq-bil-jinas"], n=N3(QAF, ZW("وَأَمْرُ اللهِ بَالِغٌ مُبَالَغَةً يَشْقَى بِهِ الْأَشْقِيَاءُ فِي حُكْمِهِ وَقَضَائِهِ", "God's command reaches fully, the wretched made wretched by it in His judgement and decree", "Allah'ın emri tam yerini bulur; bedbahtlar O'nun hüküm ve kazasıyla bedbaht olur"),
     HADD("يُلْحَقُ بِالْجِنَاسِ مَا يَجْمَعُهُ الِاشْتِقَاقُ: «تَشْقَى» وَ«الْأَشْقِيَاءُ» مِنْ أَصْلٍ وَاحِدٍ", "what derivation brings together is attached to jinās: «are made wretched» and «the wretched» come from one root", "iştikakın bir araya getirdiği cinasa ilhak edilir: «teşkâ» ve «el-eşkıyâ» aynı kökten")))])
VV(45, "when you wished for them in your delusion, and an arrogant wish drove them on to you.",
  "aldanışınızla onları (savaşa) arzuladığınızda; şımarık bir arzu onları size sürükledi.",
 [PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«هَدَاهُمْ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ (الدُّرَّةُ)", "an adverb of past time built on sukun, in the seat of nasb, hanging on «he led them», annexed to the clause after it (al-Durra)", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «önlerine düştü»ye müteallik, sonraki cümleye muzâf (Dürre)", g=["maful-fih"], pos="noun"),
  V("d5", "تَمَنَّوْنَهُمْ", "tamanna", enc="هُمْ", g=["form-v-verbs", "naqis-verbs", "afal-khamsa"], n=N3(NT("وَأَصْلُهُ «تَتَمَنَّوْنَهُمْ»، حُذِفَتْ إِحْدَى التَّاءَيْنِ تَخْفِيفًا؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذْ» إِلَيْهَا", "its full form is تَتَمَنَّوْنَهُمْ, one of the two tas dropped for lightness; the clause is in the seat of jarr, إِذْ being annexed to it", "aslı «tetemennevnehum»dur, iki tâdan biri hafiflik için düşmüştür; cümle «iz»in ona muzâf olmasıyla mahallen mecrûr"), ZW("حِينَ تَمَنَّيْتُمْ قِتَالَهُمْ إِيَّاكُمْ وَمَصِيرَهُمْ إِلَيْكُمْ", "when you wished for them to fight you and come against you", "onların sizinle savaşmasını ve üzerinize gelmesini arzuladığınızda"))),
  R("mutlaq", "غُرُورًا", "ghurur-hr", g=["masdar"], n=N3(DR("مُرَادِفٌ لِمَصْدَرِ الْفِعْلِ قَبْلَهُ، أَوْ حَالٌ مِنْ وَاوِ الْجَمَاعَةِ بِتَأْوِيلِ «مَغْرُورِينَ»", "a synonym of the verb's own masdar; or a hal of the waw of the group, read as «deluded»", "önceki fiilin masdarıyla eş anlamlı; ya da «aldanmış olarak» te'viliyle cemâat vâvından hâl"), ZW("اغْتِرَارًا بِشَوْكَتِكُمْ وَعُدَّتِكُمْ", "deluded by your might and your numbers", "kuvvetinize ve sayınıza aldanarak"))),
  ],
 [V("mt", "فَسَاقَتْهُمْ", "saqa", c="f", enc="هُمْ", g=["hollow-verbs"], n=CL("atf", "تَمَنَّوْنَهُمْ", "you wished for them", "onları arzuladınız")),
  JP("إِلَيْكُمْ", "ila", "كُمْ", n=MT("سَاقَتْ", "drove", "sürükledi»ye")),
  R("fail", "أُمْنِيَّةٌ", "umniya", g=["mulhaq-bil-jinas"], n=N3(ZW("فَسَاقَتْهُمْ إِلَيْكُمْ أُمْنِيَّتُكُمُ الَّتِي كَانَتْ مَعَ الْبَطَرِ", "your wish, which went with insolence, drove them on to you", "şımarıklıkla birlikte olan arzunuz onları size sürükledi"), HADD("يُلْحَقُ بِالْجِنَاسِ مَا يَجْمَعُهُ الِاشْتِقَاقُ: «تَمَنَّوْنَ» وَ«أُمْنِيَّةٌ» مِنْ أَصْلٍ وَاحِدٍ", "what derivation brings together is attached to jinās: «you wished» and «a wish» come from one root", "iştikakın bir araya getirdiği cinasa ilhak edilir: «temennevne» ve «umniyye» aynı kökten"))),
  R("naatr", "أَشْرَاءُ", "ashra-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("أُمْنِيَّةٌ", "a wish", "umniyye"), n=N3(QAF, ZW("الْأَشَرُ: الْبَطَرُ، وَالْأَشْرَاءُ: الْبَطِرَةُ", "أَشَر is insolence; أَشْرَاء is insolent", "«eşer»: şımarıklık; «eşrâ'»: şımarık")))])
VV(46, "They did not come on you unawares; rather the mirage and the forenoon lifted their forms (to your sight).",
  "Size ansızın gelmediler; bilakis serap ve kuşluk vakti onların karaltılarını (gözünüze) yükseltti.",
 [LAM(),
  T("يَغُرُّوكُمُ", "gharra", "verb", ["lam-jazim", "afal-khamsa", "fail", "maful-bihi", "al-bariz-al-muttasil", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَوَاوُ الْجَمَاعَةِ " + _FA + "، وَ«كُمُ» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَحُرِّكَتْ مِيمُهُ بِالضَّمِّ لِإِقَامَةِ الْوَزْنِ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "A present verb in jazm by لَمْ, its sign the dropping of the nun, for it is one of the five verbs; the waw of the group is the doer, in the seat of raf'; «كُمُ» is the object, in the seat of nasb, its mim voweled with damma to keep the metre — a fresh sentence.", "«Lem» ile meczûm muzâri, ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; cemâat vâvı fâil, mahallen merfû; «kumu» mef'ûlün bih, mahallen mansûb; mîmi vezin için damme ile harekelenmiştir — cümle müste'nefedir.",
    segs=SG(("يَغُرُّو", "gharra", "verb"), ("كُمُ", "pron-2mp", "pron"))),
  R("mutlaq", "غُرُورًا", "ghurur-hr", g=["masdar"], n=ZW("لَمْ يُفَاجِئُوكُمْ مُفَاجَأَةً، وَلٰكِنْ أَتَوْكُمْ وَأَنْتُمْ تَرَوْنَهُمْ خِلَالَ السَّرَابِ", "they did not take you by surprise; they came on while you watched them through the mirage", "size ansızın gelmediler; siz onları serabın arasından görürken geldiler")),
  PT("وَلٰكِنْ", "lakin", "لٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُهْمَلٌ لَا عَمَلَ لَهُ", "لٰكِنْ is a particle of correction, light and governing nothing", "lâkin: istidrâk harfi, mühmel, ameli yoktur", c="w", g=["aw-imma-am-la-bal-lakin-fil-kafiya"])],
 [V("m", "رَفَعَ", "rafaa", g=["majaz-aqli"], n=N3(NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is joined to what goes before", "cümle öncekine ma'tûftur"), DR("وَيُرْوَى «يَرْفَعُ» بِالْمُضَارِعِ", "it is also related «lifts», in the present", "muzâri ile «yerfa'u» diye de rivayet edilir"),
     HADD("مَجَازٌ عَقْلِيٌّ: أُسْنِدَ الرَّفْعُ إِلَى الْآلِ وَالضَّحَاءِ وَهُمَا سَبَبُ ظُهُورِهِمْ — وَصَفَهُ الزَّوْزَنِيُّ: «حَتَّى كَأَنَّ السَّرَابَ يَرْفَعُ أَشْخَاصَهُمْ لَكُمْ»", "a majāz ʿaqlī: the lifting is assigned to the mirage and the forenoon, the causes of their being seen — al-Zawzanī describes it: «until it was as if the mirage were lifting their forms up for you»", "mecâz-ı aklî: yükseltme, onların görünmesinin sebebi olan serap ve kuşluğa isnad edilmiştir — Zevzenî tarif eder: «sanki serap onların karaltılarını size yükseltiyordu»"))),
  R("fail", "الْآلُ", "aal-mirage-tf", n=ZW("الْآلُ: مَا يُرَى كَالسَّرَابِ فِي طَرَفَيِ النَّهَارِ", "آل is what is seen like a mirage at either end of the day", "«âl»: günün iki ucunda serap gibi görünen şey")),
  R("maf", "شَخْصَهُمْ", "shakhs", enc="هُمْ"),
  R("atfr", "وَالضَّحَاءُ", "duhaa-hr", c="w", of=("الْآلُ", "the mirage", "el-âl"), n=N3(QAF, ZW("الضَّحَاءُ: بُعَيْدَ الضُّحَى", "ضَحَاء is a little after the forenoon", "«dahâ'»: kuşluktan biraz sonra")))])
VV(47, "O you who speak, who carry tales of us to ʿAmr — will that ever have an end?",
  "Ey Amr'ın huzurunda bizim hakkımızda konuşan, laf ileten! Bunun bir sonu olmayacak mı?",
 [T("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "huruf-tanbih"], "«أَيُّ» مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ، وَ«هَا» حَرْفُ تَنْبِيهٍ — وَالْجُمْلَةُ النِّدَائِيَّةُ مُسْتَأْنَفَةٌ.",
    "«أَيُّ» is a vocative, an intended indefinite, built on damma in the seat of nasb, the calling particle left out; «هَا» is a particle of attention — the call is a fresh sentence.", "«Eyyu» kastedilmiş nekre münâdâ, damme üzere mebnî, mahallen mansûb; nidâ harfi mahzûf; «hâ» tenbîh harfidir — nidâ cümlesi müste'nefedir.", segs=SG(("أَيُّ", "ayyuha", "noun"), ("هَا", "ha-tanbih", "part"))),
  R("naatr", "النَّاطِقُ", "natiq", g=["ism-fail"], of=("أَيُّ", "you", "eyyu"), n=DR("وَرِوَايَتُهُ «الشَّانِئُ»", "his text reads «the hater»", "onun rivayeti «eş-şânî'»dir")),
  R("naatr", "الْمُبَلِّغُ", "muballigh", g=["ism-fail"], of=("أَيُّ", "you", "eyyu"), n=NT("ثَانٍ، وَمَفْعُولُهُ مَحْذُوفٌ", "a second one; its object is left out", "ikinci; mef'ûlü mahzûftur")),
  JP("عَنَّا", "an", "نَا", n=MT("الْمُبَلِّغُ", "who carries tales", "ileten»e"))],
 [R("zarfm", "عِنْدَ", "inda", mud=True, n=MZ("الْمُبَلِّغُ", "who carries tales", "ileten»e")),
  NAME("mdf", "عَمْرٍو", "amr-name"),
  PT("وَهَلْ", "hal-istifham", "الْوَاوُ زَائِدَةٌ (الدُّرَّةُ)، وَ«هَلْ» حَرْفُ اسْتِفْهَامٍ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى الْحَضِّ عَلَى الِانْتِهَاءِ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ: «أَلَا تَنْتَهِي عَنْ تَبْلِيغِ الْأَخْبَارِ الْكَاذِبَةِ عَنَّا؟»", "the waw is extra (al-Durra), and هَلْ is a particle of question — the question has left asking for urging him to stop, as al-Zawzanī explains: «will you not stop carrying lying reports of us?»", "vâv zâiddir (Dürre), «hel» istifhâm harfidir — istifhâm, vazgeçmeye teşvik anlamına çıkmıştır; Zevzenî'nin şerhi: «hakkımızda yalan haberler iletmekten vazgeçmeyecek misin?»", g=["al-istifham", "khuruj-al-istifham"], segs=SG(("وَ", "wa", "conj"), ("هَلْ", "hal-istifham", "part"))),
  T("لِذَاكَ", "li", "prep", ["huruf-jarr", "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ، وَ«ذَا» اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِاللَّامِ، وَالْكَافُ حَرْفُ خِطَابٍ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
    "The lam is a jarr letter; «ذَا» is a demonstrative built on sukun, in the seat of jarr after it; the kaf is a particle of address — the phrase hangs on an omitted, fronted khabar.", "Lâm cer harfidir; «zâ» sükûn üzere mebnî işaret ismi, lâm ile mahallen mecrûr; kâf hitap harfidir — câr-mecrûr öne alınmış mahzûf habere müteallik.", segs=SG(("لِ", "li", "prep"), ("ذَاكَ", "dhaka", "pron"))),
  R("mub", "انْتِهَاءُ", "intiha", g=["masdar"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "placed after; a fresh sentence", "sona bırakılmıştır; cümle müste'nefedir"), QAF_N))])
VV(48, "He it is with whom we have, of good deeds, three signs — in every one of them the judgement (is ours).",
  "O, katında bizim iyiliklerimizden üç alâmet bulunan kişidir; her birinde hüküm (bizim lehimizedir).",
 [PT("مَنْ", "man", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ الَّذِي … — «هُوَ الَّذِي لَنَا عِنْدَهُ ثَلَاثُ آيَاتٍ» (الزَّوْزَنِيُّ)؛ وَأَجَازَ الدُّرَّةُ أَنْ يَكُونَ مُبْتَدَأً خَبَرُهُ الْجُمْلَةُ بَعْدَهُ", "a relative noun built on sukun, in the seat of raf' as the khabar of an omitted mubtada, «he is the one who …» — «he is the one with whom we have three signs» (al-Zawzanī); al-Durra also allows it to be a mubtada whose khabar is the clause after it", "sükûn üzere mebnî ism-i mevsûl, mahzûf mübtedânın haberi olarak mahallen merfû: «o, … kimsedir» — «o, katında bizim üç alâmetimiz bulunan kimsedir» (Zevzenî); Dürre onun, haberi sonraki cümle olan mübtedâ olmasını da caiz görür", g=["ism-mawsul", "hadhf-wa-taqdir"], pos="pron"),
  JP("لَنَا", "li", "نَا", n=MTH("صِلَةِ الْمَوْصُولِ", "the omitted ṣila of the relative", "mevsûlün mahzûf sılasına")),
  R("zarfm", "عِنْدَهُ", "inda", enc="هُ", n=MZ("الصِّلَةِ الْمَحْذُوفَةِ", "the omitted ṣila", "mahzûf sılaya")),
  PR("مِنَ", "min", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "الْخَيْرِ", "khayr")],
 [R("mub", "آيَاتٌ", "aya", g=["jam-muannath-salim"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ (الدُّرَّةُ)", "placed after; the nominal clause is a hal, in the seat of nasb (al-Durra)", "sona bırakılmıştır; isim cümlesi hâldir, mahallen mansûb (Dürre)"), ZW("أَيْ ثَلَاثُ دَلَائِلَ مِنْ دَلَائِلِ غَنَائِنَا وَحُسْنِ بَلَائِنَا فِي الْحُرُوبِ وَالْخُطُوبِ", "that is, three proofs of our worth and our fine trial in wars and grave affairs", "yani savaşlarda ve büyük işlerde değerimizin ve güzel imtihanımızın delillerinden üç delil"))),
  R("naatr", "ثَلَاثٌ", "thalath", of=("آيَاتٌ", "signs", "âyât")),
  PR("فِي", "fi", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "كُلِّهِنَّ", "kull", enc="هِنَّ"),
  R("mub", "الْقَضَاءُ", "qada", n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ ثَانِيَةٌ لِـ«آيَاتٌ»", "placed after; the clause is a second adjective of «signs», in the seat of raf'", "sona bırakılmıştır; cümle «âyât»ın ikinci sıfatı, mahallen merfû"), QAF, ZW("يُقْضَى لَنَا عَلَى خُصُومِنَا فِي كُلِّهَا", "in all of them judgement is given for us against our foes", "hepsinde hasımlarımıza karşı lehimize hüküm verilir")))])
VV(49, "A sign: the Shining Day of al-Shaqīqa, when Maʿadd came, every tribe with its banner,",
  "Bir alâmet: Şakîka'nın parlayan günü; Maadd geldiğinde, her kabilenin bir sancağı vardı;",
 [R("khb", "آيَةٌ", "aya", g=["hadhf-wa-taqdir"], n=DR("وَالْمُبْتَدَأُ مَحْذُوفٌ تَقْدِيرُهُ: الْأُولَى آيَةٌ؛ وَيَجُوزُ أَنْ يَكُونَ مُبْتَدَأً خَبَرُهُ مَحْذُوفٌ (مِنْهُنَّ آيَةٌ)، أَوْ بَدَلًا مِنْ «آيَاتٌ»", "its mubtada is left out: «the first is a sign»; it may also be a mubtada with an omitted khabar («of them is a sign»), or a badal of «signs»", "mübtedâsı mahzûftur: «birincisi bir alâmettir»; haberi mahzûf mübtedâ («onlardan biri bir alâmettir») ya da «âyât»tan bedel de olabilir")),
  R("naatr", "شَارِقُ", "shariq-hr", mud=True, g=["ism-fail", "kinaya"], of=("آيَةٌ", "a sign", "âyetün"), n=N3(DR("أَوْ بَدَلٌ مِنْهَا", "or a badal of it", "ya da ondan bedel"),
     NT("وَفِيهِ كِنَايَةٌ عَنْ مَوْصُوفٍ: «وَأَرَادَ بِشَارِقِ الشَّقِيقَةِ: الْحَرْبَ الَّتِي قَامَتْ بِهَا» (الزَّوْزَنِيُّ)", "a kināya for the thing described: «by the Shining of al-Shaqīqa he means the war that rose there» (al-Zawzanī)", "mevsûftan kinaye: «Şakîka'nın parlayanı ile orada çıkan savaşı kastetti» (Zevzenî)"))),
  R("mdf", "الشَّقِيقَةِ", "lb-shaqiqa", n=ZW("الشَّقِيقَةُ: أَرْضٌ صُلْبَةٌ بَيْنَ رَمْلَتَيْنِ، وَالْجَمْعُ شَقَائِقُ؛ وَالشُّرُوقُ: الطُّلُوعُ وَالْإِضَاءَةُ", "شَقِيقَة is hard ground between two sands, pl. شَقَائِق; شُرُوق is rising and shining", "«şakîka»: iki kum arasındaki sert arazi, ç. «şakâık»; «şurûk»: doğmak ve parlamak")),
  PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الشَّقِيقَةِ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ (الدُّرَّةُ)", "an adverb of past time built on sukun, in the seat of nasb, hanging on an omitted hal of «al-Shaqīqa», annexed to the clause after it (al-Durra)", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «Şakîka»dan mahzûf bir hâle müteallik, sonraki cümleye muzâf (Dürre)", g=["maful-fih"], pos="noun")],
 [V("mt", "جَاءَتْ", "jaa", g=["hollow-verbs"], n=CL("mdf", "إِذْ", "إِذْ", "iz")),
  NAME("fail", "مَعَدٌّ", "maadd-name"),
  R("majr", "لِكُلِّ", "kull", j="li", mud=True, n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mdf", "حَيٍّ", "hayy-tribe"),
  R("mub", "لِوَاءُ", "liwa-hr", n=N3(DR("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِـ«مَعَدٌّ»، وَالرَّابِطُ مَحْذُوفٌ: لِكُلِّ حَيٍّ مِنْهُمْ لِوَاءٌ", "placed after; the clause is an adjective of «Maʿadd», in the seat of raf'; the link is left out: «every tribe of them had a banner»", "sona bırakılmıştır; cümle «Maadd»ın sıfatı, mahallen merfû; bağlayıcı mahzûftur: «onlardan her kabilenin bir sancağı»"), QAF_N, ZW("حِينَ جَاءَتْ مَعَدٌّ بِأَلْوِيَتِهَا وَرَايَاتِهَا", "when Maʿadd came with their standards and banners", "Maadd sancakları ve bayraklarıyla geldiğinde")))])
# =====================================================================================================================
# The poem — vv. 50–56 — آيَاتٌ ثَلَاثٌ
# =====================================================================================================================
S_DIPT_AN = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", " — by the fatha that stands for the kasra: a diptote, a proper name ending in the added alif and nun", " — özel isim olup elif-nûn ziyadesi taşıdığı için gayr-i munsarif: kesre yerine fetha ile")
MIM_W = NT("وَحُرِّكَتْ مِيمُ «هُمُ» بِالضَّمِّ لِإِقَامَةِ الْوَزْنِ", "the mim of «هُمُ» is voweled with damma to keep the metre", "«humu»nun mîmi vezin için damme ile harekelenmiştir")
KAMA = lambda ar, en, tr: PT("كَمَا", "ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ بَعْدَهَا مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ (الدُّرَّةُ) — " + ar,
    "the kaf is the jarr letter of likening and «mā» makes a masdar: with the verb after it, it is a masdar in jarr after the kaf, and the phrase hangs on the omitted adjective of an omitted absolute object (al-Durra) — " + en,
    "kâf teşbîh ve cer harfi, «mâ» masdariyyedir: sonraki fiille birlikte kâf ile mecrûr bir masdardır; câr-mecrûr mahzûf bir mef'ûl-i mutlakın mahzûf sıfatına müteallik (Dürre) — " + tr,
    pos="prep", g=TB + ["huruf-jarr", "maful-mutlaq"], segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part")))
VV(50, "around Qays, clad in mail, with a lordly ram of the land of qaraẓ, as though he were a white hill —",
  "Kays'ın çevresinde, zırhlara bürünmüş, karaz diyarından (Yemen'den) bir koç (efendi) ile; o sanki beyaz bir tepeydi —",
 [R("zarfm", "حَوْلَ", "hawla", mud=True, n=MZ("جَاءَتْ", "came", "geldi»ye")),
  NAME("mdf", "قَيْسٍ", "qays-name-tf", n=ZW("أَرَادَ قَيْسَ بْنَ مَعْدِيكَرِبَ مِنْ مُلُوكِ حِمْيَرَ", "he means Qays ibn Maʿdīkarib, of the kings of Ḥimyar", "Himyer krallarından Kays b. Ma'dîkerib'i kastediyor")),
  R("hal", "مُسْتَلْئِمِينَ", "mustalim", sign=("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", " — by the ya, a sound masculine plural; its nun stands for the tanwin of the singular", " — cem-i müzekker sâlim olduğu için yâ ile; nûn müfreddeki tenvinin karşılığıdır"), g=["jam-mudhakkar-salim", "ism-fail"], n=N3(NT("صَاحِبُهَا «كُلِّ حَيٍّ» (الدُّرَّةُ)", "of «every tribe» (al-Durra)", "«her kabile»den hâl (Dürre)"), ZW("الِاسْتِلْئَامُ: لُبْسُ اللَّأْمَةِ، وَهِيَ الدِّرْعُ", "اِسْتِلْئَام is putting on the لَأْمَة, the coat of mail", "«istil'âm»: «le'me», yani zırh giymek"))),
  R("majr", "بِكَبْشٍ", "kabsh", j="bi", g=["istiara", "aqsam-al-istiara"], n=N3(MT("مُسْتَلْئِمِينَ", "clad in mail", "zırhlanmış»a"),
     NT("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: «الْكَبْشُ: السَّيِّدُ، مُسْتَعَارٌ لَهُ بِمَنْزِلَةِ الْقَرْمِ» (الزَّوْزَنِيُّ)", "an istiʿāra taṣrīḥiyya: «the ram is the lord, a borrowed word for him, like قَرْم (stallion)» (al-Zawzanī)", "istiâre-i tasrîhiyye: «koç efendidir; «karm» (aygır) gibi onun için istiâre edilmiştir» (Zevzenî)")))],
 [R("naatj", "قَرَظِيٍّ", "qarazi-hr", g=["ism-mansub"], of=("كَبْشٍ", "ram", "kebş"), n=ZW("الْقَرَظُ: شَجَرٌ يُدْبَغُ بِهِ الْأَدِيمُ، وَبِلَادُ الْقَرَظِ: الْيَمَنُ", "قَرَظ is a tree used to tan hides; the land of qaraẓ is Yemen", "«karaz»: deri tabaklanan bir ağaç; karaz diyarı Yemen'dir")),
  KAANNA("كَأَنَّهُ", enc="هُ", g=TB, n=N3(DR("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنْ «كَبْشٍ»", "the clause can be an adjective or a hal of «ram»", "cümle «koç»un sıfatı da hâli de olabilir"),
     NT("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ السَّيِّدُ، وَالْمُشَبَّهُ بِهِ الْهَضْبَةُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الْمَنَعَةُ وَالشَّوْكَةُ — ذَكَرَهُ الزَّوْزَنِيُّ: «كَأَنَّهُ فِي مَنَعَتِهِ وَشَوْكَتِهِ هَضْبَةٌ مِنَ الْهِضَابِ»", "a tashbih mursal mujmal: the lord is likened to the hill; the particle is كَأَنَّ; the point of likeness — strength and might — is al-Zawzanī's: «as though in his strength and might he were one of the hills»", "teşbîh-i mürsel mücmel: müşebbeh efendi, müşebbehün bih tepe, edat «keenne»; vech-i şebeh — dokunulmazlık ve güç — Zevzenî'dedir: «gücünde ve kuvvetinde sanki tepelerden bir tepe»"))),
  R("khbka", "عَبْلَاءُ", "abla-hill-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], n=N3(QAF, ZW("الْعَبْلَاءُ: هَضْبَةٌ بَيْضَاءُ؛ يُرِيدُ أَنَّهُمْ كَفُّوا عَادِيَةَ قَيْسٍ وَجَيْشِهِ عَنْ عَمْرِو بْنِ هِنْدٍ", "عَبْلَاء is a white hill; he means that they kept the onslaught of Qays and his army off ʿAmr ibn Hind", "«ablâ'»: beyaz tepe; Kays'ın ve ordusunun saldırısını Amr b. Hind'den savuşturduklarını kastediyor")))])
VV(51, "and a host of the sons of noble women, which nothing stays but a shining, far-stretched troop.",
  "ve soylu kadınların oğullarından bir topluluk ki onu ancak parıl parıl, uzayıp giden bir birlik durdurabilir.",
 [R("atfj", "وَصَتِيتٍ", "sitit-hr", c="w", of=("كَبْشٍ", "ram", "kebş"), n=ZW("الصَّتِيتُ: الْجَمَاعَةُ؛ وَالثَّانِيَةُ جَمَاعَةٌ مِنْ أَوْلَادِ الْحَرَائِرِ الْكَرَائِمِ", "صَتِيت is a host: the second (sign) is a host of the sons of noble freeborn women", "«satît»: topluluk; ikincisi soylu hür kadınların oğullarından bir topluluktur")),
  PR("مِنَ", "min", n=MTH("صِفَةٍ لِـ«صَتِيتٍ»: مَوْلُودٍ مِنَ الْعَوَاتِكِ (الدُّرَّةُ)", "an omitted adjective of «host»: «born of the noble women» (al-Durra)", "«satît»in mahzûf sıfatına: «soylu kadınlardan doğmuş» (Dürre)")),
  R("majr", "الْعَوَاتِكِ", "atika-hr", g=["jam-taksir"], n=ZW("الْعَوَاتِكُ: الشَّوَابُّ الْحَرَائِرُ الْخِيَارُ مِنَ النِّسَاءِ؛ أَيْ مِنْ أَوْلَادِ الْعَوَاتِكِ", "عَوَاتِك are young, freeborn, choice women: that is, of the sons of such women", "«avâtik»: kadınların genç, hür ve seçkin olanları; yani onların oğullarından")),
  LA_N(n=DR("وَرِوَايَتُهُ «مَا تَنْهَاهُ»", "his text reads «مَا تَنْهَاهُ»", "onun rivayeti «mâ tenhâhu»dur"))],
 [V("da", "تَنْهَاهُ", "naha", enc="هُ", g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِـ«صَتِيتٍ»، أَوْ حَالٌ مِنْهُ", "the clause is a second adjective of «host», or a hal of it", "cümle «satît»in ikinci sıfatı ya da ondan hâldir")),
  PT("إِلَّا", "illa", "حَرْفٌ مُفِيدٌ لِلْحَصْرِ لَا عَمَلَ لَهُ — وَالِاسْتِثْنَاءُ مُفَرَّغٌ — وَفِيهِ الْقَصْرُ بِطَرِيقِ النَّفْيِ وَالِاسْتِثْنَاءِ: «حَرْفٌ مُفِيدٌ لِلْحَصْرِ» (الدُّرَّةُ)", "a particle of restriction governing nothing — the exception is emptied (its excepted term fills the verb's own seat) — a qaṣr by negation and exception: «a particle giving restriction» (al-Durra)", "hasr ifade eden, ameli olmayan harf — istisna müferrağdır — nefy ve istisna yoluyla kasr: «hasr ifade eden harf» (Dürre)", g=["istithna-mufarragh", "qasr", "turuq-al-qasr"]),
  R("fail", "مُبْيَضَّةٌ", "mubyadd-hr", g=["ism-fail", "hadhf-wa-taqdir"], n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("إِلَّا كَتِيبَةٌ مُبْيَضَّةٌ بِبَيَاضِ دُرُوعِهَا وَبَيْضِهَا عَظِيمَةٌ مُمْتَدَّةٌ، وَقِيلَ: بَلْ مَعْنَاهُ إِلَّا سُيُوفٌ مُبْيَضَّةٌ طِوَالٌ", "nothing but a troop shining white with its mail and helmets, great and far-stretched; others: nothing but long white-shining swords", "ancak zırhlarının ve miğferlerinin beyazlığıyla parlayan, büyük ve uzayıp giden bir birlik; ya da: ancak uzun, parlak kılıçlar"))),
  R("naatr", "رَعْلَاءُ", "rala-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("مُبْيَضَّةٌ", "shining", "mubyadda"), n=N3(QAF, ZW("الرَّعْلَاءُ: الطَّوِيلَةُ الْمُمْتَدَّةُ", "رَعْلَاء is long, far-stretched", "«ra'lâ'»: uzun, uzayıp giden")))])
VV(52, "And we drove them back with thrusts from which (blood) came out as water comes out of the holes of the water-skins.",
  "Onları, su tulumlarının deliklerinden su nasıl çıkarsa (kanın) öyle çıktığı mızrak darbeleriyle geri püskürttük.",
 [V("mna", "فَرَدَدْنَاهُمُ", "radda", c="fi", enc="هُمُ", g=["doubled-verbs"], n=N3(CL("ist"), MIM_W)),
  R("majr", "بِطَعْنٍ", "tan", j="bi", g=["masdar"], n=MT("رَدَدْنَا", "we drove back", "geri püskürttük»e")),
  KAMA("وَجُمْلَةُ الْفِعْلِ الْمَحْذُوفِ صِفَةٌ لِـ«طَعْنٍ» — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ خُرُوجُ الدَّمِ مِنَ الْجِرَاحِ، وَالْمُشَبَّهُ بِهِ خُرُوجُ الْمَاءِ مِنْ خُرَبِ الْمَزَادِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ غَيْرُ مَذْكُورٍ؛ وَهُوَ قَوْلُ الزَّوْزَنِيِّ: «بِطَعْنٍ خَرَجَ الدَّمُ مِنْ جِرَاحِهِ خُرُوجَ الْمَاءِ مِنْ أَفْوَاهِ الْقِرَبِ وَثُقُوبِهَا»",
       "the clause of the omitted verb is an adjective of «thrusts» — a tashbih mursal mujmal: the blood coming out of the wounds is likened to water coming out of the holes of the water-skins; the particle is the kaf; the point of likeness is not stated; it is al-Zawzanī's «with thrusts from whose wounds blood came out as water comes out of the mouths and holes of skins»",
       "mahzûf fiilin cümlesi «darbeler»in sıfatıdır — teşbîh-i mürsel mücmel: kanın yaralardan çıkışı, suyun tulum deliklerinden çıkışına benzetilmiştir; edat kâf; vech-i şebeh zikredilmemiştir; Zevzenî: «yaralarından, suyun tulumların ağızlarından ve deliklerinden çıkışı gibi kan çıkan darbelerle»")],
 [V("d", "يَخْرُجُ", "kharaja"),
  PR("مِنْ", "min", n=MT("يَخْرُجُ", "comes out", "çıkar»a")),
  R("majr", "خُرْبَةِ", "khurba-hr", mud=True, n=ZW("خُرْبَةُ الْمَزَادِ: ثَقْبُهَا", "the خُرْبَة of a water-skin is its hole", "tulumun «hurbe»si deliğidir")),
  R("mdf", "الْمَزَادِ", "mazada", g=["jam-taksir"], n=ZW("الْمَزَادُ: جَمْعُ مَزَادَةٍ، وَهِيَ زِقُّ الْمَاءِ خَاصَّةً", "مَزَاد is the plural of مَزَادَة, a water-skin in particular", "«mezâd», «mezâde»nin, yani özellikle su tulumunun çoğuludur")),
  R("fail", "الْمَاءُ", "ma-water", n=QAF)])
VV(53, "and we drove them on to the hard ground of Thahlān, routed, their thighs bloodied.",
  "Onları kovalayarak Sehlân'ın sert yamacına sığınmaya zorladık; uylukları kana bulanmıştı.",
 [V("mna", "وَحَمَلْنَاهُمُ", "hamala", c="w", enc="هُمُ", n=N3(CL("atf", "رَدَدْنَاهُمُ", "we drove them back", "geri püskürttük"), MIM_W, ZW("أَلْجَأْنَاهُمْ إِلَى التَّحَصُّنِ بِغِلَظِ هٰذَا الْجَبَلِ", "we forced them to take refuge in the rough flank of this mountain", "onları bu dağın sert yamacına sığınmaya mecbur ettik"))),
  PR("عَلَى", "ala", n=MT("حَمَلْنَا", "we drove", "zorladık»a")),
  R("majr", "حَزْمِ", "hazm-hr", mud=True, n=N3(DR("وَرِوَايَتُهُ «حَزْنِ»", "his text reads «حَزْنِ»", "onun rivayeti «hazni»dir"), ZW("الْحَزْمُ: أَغْلَظُ مِنَ الْحَزْنِ", "حَزْم is rougher than حَزْن (rugged ground)", "«hazm», «hazn»dan (sarp yer) daha serttir")))],
 [NAME("mdf", "ثَهْلَانَ", "thahlan-hr", sign=S_DIPT_AN, g=["mamnu-min-sarf"], n=ZW("ثَهْلَانُ: جَبَلٌ بِعَيْنِهِ", "Thahlān is a particular mountain", "Sehlân belli bir dağdır")),
  R("hal", "شِلَالًا", "shilal-hr", g=["masdar"], n=N3(NT("صَاحِبُهَا الضَّمِيرُ فِي «حَمَلْنَاهُمُ»", "of the object pronoun in «we drove them»", "«hamelnâhum»daki zamirden hâl"), ZW("الشِّلَالُ: الطِّرَادُ", "شِلَال is driving off in pursuit", "«şilâl»: kovalama"))),
  V("m", "وَدُمِّيَ", "damma-hr", c="wh", pas=True, g=["form-ii-verbs", "naqis-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ الْمَفْعُولِ عَلَى تَقْدِيرِ «قَدْ»، وَالرَّابِطُ الْوَاوُ، وَيَحْسُنُ تَقْدِيرُ «مِنْهُمْ»", "the clause is a hal of the object pronoun, in the seat of nasb, with «قَدْ» understood; the waw is the link, and «of them» may well be understood", "cümle, «kad» takdiriyle mef'ûl zamirden hâl, mahallen mansûb; bağlayıcı vâvdır, «onlardan» takdiri de güzeldir")),
  R("naib", "الْأَنْسَاءُ", "nasa-vein-hr", g=["jam-taksir"], n=N3(QAF, ZW("الْأَنْسَاءُ: جَمْعُ النَّسَا، وَهُوَ عِرْقٌ مَعْرُوفٌ فِي الْفَخِذِ؛ وَالتَّدْمِيَةُ: اللَّطْخُ بِالدَّمِ؛ وَأَدْمَيْنَا أَفْخَاذَهُمْ بِالطَّعْنِ وَالضَّرْبِ", "أَنْسَاء is the plural of نَسًا, a well-known vein in the thigh; تَدْمِيَة is smearing with blood: we bloodied their thighs with thrust and blow", "«ensâ'», uyluktaki bilinen damar «nesâ»nın çoğuludur; «tedmiye»: kana bulamak; mızrak ve kılıçla uyluklarını kana buladık")))])
VV(54, "and we beat them back with thrusts (our spears plunging) as buckets are plunged in the full water of a stone-lined well.",
  "ve onları, taş örülü bir kuyunun bol suyunda kovaların daldırılıp oynatıldığı gibi (mızraklarımızı vücutlarında oynatan) darbelerle şiddetle geri püskürttük.",
 [V("mna", "وَجَبَهْنَاهُمُ", "jabaha-hr", c="w", enc="هُمُ", n=N3(CL("atf", "رَدَدْنَاهُمُ", "we drove them back", "geri püskürttük"), MIM_W, ZW("الْجَبْهُ: أَعْنَفُ الرَّدْعِ", "جَبْه is the harshest repulse", "«cebh»: en şiddetli geri püskürtme"))),
  R("majr", "بِطَعْنٍ", "tan", j="bi", g=["masdar"], n=MT("جَبَهْنَا", "we beat back", "püskürttük»e")),
  KAMA("وَمَذْهَبُ سِيبَوَيْهِ فِي مِثْلِهِ أَنْ يَكُونَ حَالًا مِنَ الْمَصْدَرِ الْمَفْهُومِ مِنَ الْفِعْلِ، لِأَنَّ حَذْفَ الْمَوْصُوفِ لَا يَجُوزُ إِلَّا فِي مَوَاضِعَ مَحْصُورَةٍ (الدُّرَّةُ) — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ تَحَرُّكُ الرِّمَاحِ فِي أَجْسَامِهِمْ، وَالْمُشَبَّهُ بِهِ تَحَرُّكُ الدِّلَاءِ فِي مَاءِ الْبِئْرِ، وَالْأَدَاةُ الْكَافُ؛ وَهُوَ قَوْلُ الزَّوْزَنِيِّ: «فَتَحَرَّكَتْ رِمَاحُنَا فِي أَجْسَامِهِمْ كَمَا تُحَرَّكُ الدِّلَاءُ فِي مَاءِ الْبِئْرِ الْمَطْوِيَّةِ بِالْحِجَارَةِ»",
       "Sībawayh's view in such a case is that it is a hal of the masdar understood from the verb, since dropping a described noun is allowed only in set places (al-Durra) — a tashbih mursal mujmal: the spears' moving in their bodies is likened to the buckets' moving in a well's water; the particle is the kaf; it is al-Zawzanī's «our spears moved in their bodies as the buckets are moved in the water of a well lined with stones»",
       "Sîbeveyh'in böyle bir yerdeki görüşü, onun fiilden anlaşılan masdardan hâl olmasıdır; çünkü mevsûfun hazfi ancak sınırlı yerlerde caizdir (Dürre) — teşbîh-i mürsel mücmel: mızrakların vücutlarında oynaması, kovaların kuyu suyunda oynamasına benzetilmiştir; edat kâf; Zevzenî: «mızraklarımız vücutlarında, taş örülü kuyunun suyunda kovaların oynatıldığı gibi oynadı»")],
 [V("d", "تُنْهَزُ", "nahaza-hr", pas=True, n=ZW("النَّهْزُ: التَّحْرِيكُ", "نَهْز is moving, plying", "«nehz»: hareket ettirmek")),
  PR("فِي", "fi", n=N3(MT("تُنْهَزُ", "are plunged", "daldırılır»a"), DR("وَرِوَايَتُهُ «عَنْ جُمَّةِ»", "his text reads «from the full water»", "onun rivayeti «an cummeti»dir"))),
  R("majr", "جُمَّةِ", "jumma-hr", mud=True, n=ZW("الْجُمَّةُ: الْمَاءُ الْكَثِيرُ الْمُجْتَمِعُ", "جُمَّة is abundant gathered water", "«cumme»: toplanmış bol su")),
  R("mdf", "الطَّوِيِّ", "tawiyy-hr", n=ZW("الطَّوِيُّ: الْبِئْرُ الَّتِي طُوِيَتْ بِالْحِجَارَةِ أَوِ اللَّبِنِ", "طَوِيّ is a well lined with stones or bricks", "«tavîy»: taş ya da kerpiçle örülmüş kuyu")),
  R("naib", "الدِّلَاءُ", "dalw", g=["jam-taksir"], n=QAF)])
VV(55, "We did to them as God knows — and those who were doomed have no blood (to be avenged).",
  "Onlara Allah'ın bildiği (anlatılmaz) şeyi yaptık — helake gidenlerin kanları da (aranacak) değildir.",
 [V("mna", "وَفَعَلْنَا", "faala", c="w", n=CL("atf", "رَدَدْنَاهُمُ", "we drove them back", "geri püskürttük")),
  JP("بِهِمْ", "bi", "هِمْ", n=MT("فَعَلْنَا", "we did", "yaptık»a")),
  PT("كَمَا", "ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَصْدَرٍ مَحْذُوفٍ: فَعَلْنَا بِهِمْ فِعْلًا كَائِنًا مِثْلَ الَّذِي عَلِمَهُ اللهُ (الدُّرَّةُ) — وَفِيهِ كِنَايَةٌ عَنْ عِظَمِ مَا فَعَلُوا: «وَفَعَلْنَا بِهِمْ فِعْلًا بَلِيغًا لَا يُحِيطُ بِهِ عِلْمًا إِلَّا اللهُ» (الزَّوْزَنِيُّ)",
     "the kaf is the jarr letter of likening, and «mā» is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on the omitted adjective of an omitted masdar: «we did to them a deed like what God knows» (al-Durra) — a kināya for the enormity of what they did: «we did to them so great a deed that none but God can grasp it» (al-Zawzanī)",
     "kâf teşbîh ve cer harfi; «mâ» sükûn üzere mebnî ism-i mevsûl, kâf ile mahallen mecrûr; câr-mecrûr mahzûf bir masdarın mahzûf sıfatına müteallik: «onlara Allah'ın bildiği gibi bir iş yaptık» (Dürre) — yaptıklarının büyüklüğünden kinaye: «onlara öyle büyük bir iş yaptık ki onu ancak Allah bilir» (Zevzenî)",
     pos="prep", g=["huruf-jarr", "ism-mawsul", "kinaya"], segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-mawsula", "pron"))),
  V("m", "عَلِمَ", "alima", n=NT("وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: عَلِمَهُ", "the clause is the relative's ṣila; the pronoun referring back is left out: «knows it»", "cümle sıladır; dönen zamir mahzûftur: «onu bilir»")),
  R("fail", "اللهُ", "allah", pos="propn")],
 [PT("وَمَا", "ma-nafiya", "الْوَاوُ لِلْحَالِ، وَ«مَا» نَافِيَةٌ مُهْمَلَةٌ — أُبْطِلَ عَمَلُهَا بِـ«إِنْ» بَعْدَهَا", "the waw opens a hal; «مَا» denies and governs nothing — the إِنْ after it cancels its work", "vâv hâliyyedir; «mâ» nâfiyedir, amel etmez — ardındaki «in» amelini iptal eder", c="wh", g=["anwa-ma", "ma-la-mushabbaha"]),
  PT("إِنْ", "in-zaida", "حَرْفٌ زَائِدٌ لِلتَّوْكِيدِ لَا عَمَلَ لَهُ", "an extra particle for emphasis; it governs nothing", "te'kîd için zâid harf; ameli yoktur", g=["huruf-al-ziyada-fil-kafiya"]),
  R("majr", "لِلْحَائِنِينَ", "hain-hr", j="li", sign=("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", " — by the ya, a sound masculine plural; its nun stands for the tanwin of the singular", " — cem-i müzekker sâlim olduğu için yâ ile; nûn müfreddeki tenvinin karşılığıdır"), g=["jam-mudhakkar-salim", "ism-fail"], n=N3(MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere"), ZW("حَانَ: تَعَرَّضَ لِلْهَلَاكِ، وَحَانَ: هَلَكَ، يَحِينُ حَيْنًا", "حَانَ is to court destruction, and to perish; يَحِينُ حَيْنًا", "«hâne»: helake maruz kaldı, ve helak oldu; «yehînu haynen»"))),
  R("mub", "دِمَاءُ", "dam", g=["jam-taksir", "kinaya"], n=N3(DR("مُؤَخَّرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ، وَالرَّابِطُ الْوَاوُ", "placed after; the nominal clause is a hal, in the seat of nasb; the waw is the link", "sona bırakılmıştır; isim cümlesi hâldir, mahallen mansûb; bağlayıcı vâvdır"), QAF_N,
     NT("وَفِيهِ كِنَايَةٌ: «أَيْ لَمْ يُطْلَبْ بِثَأْرِهِمْ وَدِمَائِهِمْ» (الزَّوْزَنِيُّ)", "a kināya: «that is, no vengeance was sought for them and their blood» (al-Zawzanī)", "kinaye: «yani onların intikamı ve kanları aranmadı» (Zevzenî)")))])
VV(56, "Then Ḥujr — I mean the son of Umm Qaṭām — who had a green Persian (troop):",
  "Sonra Hucr'u — Ümmü Katâm'ın oğlunu kastediyorum — ki onun yeşil bir Fars (birliği) vardı:",
 [THUMMA(),
  R("atfn", "حُجْرًا", "hujr-hr", pos="propn", of=("هُمُ", "them", "hum"), n=N3(DR("مَعْطُوفٌ عَلَى الضَّمِيرِ الْمَفْعُولِ فِي «رَدَدْنَاهُمُ»", "joined to the object pronoun in «we drove them back»", "«reddednâhum»daki mef'ûl zamire ma'tûf"), ZW("ثُمَّ قَاتَلْنَا بَعْدَ ذٰلِكَ حُجْرَ بْنَ أُمِّ قَطَامِ", "then after that we fought Ḥujr son of Umm Qaṭām", "sonra bundan sonra Ümmü Katâm'ın oğlu Hucr ile savaştık"))),
  V("dy", "أَعْنِي", "ana-mean", doer=ANA, g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ مُفَسِّرَةٌ لِـ«حُجْرًا» لَا مَحَلَّ لَهَا", "the clause explains «Ḥujr» and has no seat", "cümle «Hucr»u açıklayan tefsîriyye cümlesidir, mahalli yoktur")),
  R("maf", "ابْنَ", "ibn", mud=True),
  R("mdf", "أُمِّ", "umm", mud=True),
  T("قَطَامِ", "qatam", "propn", ["idafa-definiteness", "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ — عَلَمٌ لِمُؤَنَّثٍ عَلَى «فَعَالِ» — وَرِوَايَةُ الدُّرَّةِ «قَطَامٍ» بِالتَّنْوِينِ لِضَرُورَةِ الشِّعْرِ.",
    "The second term of the idafa, built on kasra in the seat of jarr — a woman's name on the pattern فَعَالِ — al-Durra's text has «قَطَامٍ» with tanwin, by poetic licence.", "Muzâfun ileyh, kesre üzere mebnî, mahallen mecrûr — «fe'âli» kalıbında kadın adı — Dürre'nin rivayetinde şiir zarureti için tenvinli «katâmin»dir.")],
 [JP("وَلَهُ", "li", "هُ", c="wh", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "فَارِسِيَّةٌ", "farisiyya", g=["ism-mansub", "hadhf-wa-taqdir"], n=N3(DR("مُؤَخَّرٌ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «حُجْرًا»، وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ", "placed after; it is the adjective of an omitted noun; the clause is a hal of «Ḥujr», in the seat of nasb, linked by the waw and the pronoun", "sona bırakılmıştır; mahzûf bir mevsûfun sıfatıdır; cümle «Hucr»dan hâl, mahallen mansûb; bağlayıcılar vâv ve zamirdir"),
     ZW("وَكَانَتْ لَهُ كَتِيبَةٌ فَارِسِيَّةٌ، وَقِيلَ: بَلْ أَرَادَ: وَلَهُ دُرُوعٌ فَارِسِيَّةٌ", "he had a Persian troop; others: he means Persian coats of mail", "Fars birliği vardı; ya da: Fars zırhlarını kastetti"))),
  R("naatr", "خَضْرَاءُ", "akhdar", sign=S_DIPT_MR, g=["mamnu-min-sarf", "kinaya"], of=("فَارِسِيَّةٌ", "Persian", "fârisiyye"), n=N3(QAF,
     NT("وَفِيهِ كِنَايَةٌ عَنْ كَثْرَةِ السِّلَاحِ: «خَضْرَاءُ لِمَا رَكِبَ دُرُوعَهَا وَبَيْضَهَا مِنَ الصَّدَإِ» (الزَّوْزَنِيُّ)", "a kināya for the mass of arms: «green for the rust that has settled on its mail and helmets» (al-Zawzanī)", "silah bolluğundan kinaye: «zırhlarını ve miğferlerini kaplayan pastan dolayı yeşil» (Zevzenî)")))])
# =====================================================================================================================
# The poem — vv. 57–63 — أَسَدٌ فِي اللِّقَاءِ
# =====================================================================================================================
HUWA_KHB = NT("وَالْمُبْتَدَأُ مَحْذُوفٌ تَقْدِيرُهُ: هُوَ (الدُّرَّةُ)", "its mubtada is left out: «he is» (al-Durra)", "mübtedâsı mahzûftur: «o» (Dürre)")
VV(57, "A lion in the encounter, tawny, soft-treading — and a spring rain if a dust-laden year girds itself.",
  "Karşılaşmada bir aslan, kızıl renkli, yumuşak basan — sert, tozlu bir yıl (kötülüğe) hazırlanırsa da bir bahar.",
 [R("khb", "أَسَدٌ", "asad", g=["hadhf-wa-taqdir"] + TB, n=N3(HUWA_KHB,
     HADD("تَشْبِيهٌ بَلِيغٌ: الْمُشَبَّهُ حُجْرٌ، وَالْمُشَبَّهُ بِهِ الْأَسَدُ، حُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ — وَصَفَهُ الزَّوْزَنِيُّ: «كَانَ حُجْرٌ أَسَدًا فِي الْحَرْبِ … يُرِيدُ أَنَّهُ كَانَ لَيْثَ الْحَرْبِ»", "a tashbih baligh: Ḥujr is likened to the lion, with particle and point left out — al-Zawzanī describes it: «Ḥujr was a lion in war … he means that he was the lion of war»", "teşbîh-i belîğ: müşebbeh Hucr, müşebbehün bih aslan; edat ve vech-i şebeh hazfedilmiştir — Zevzenî tarif eder: «Hucr savaşta bir aslandı… savaşın aslanıydı»"))),
  PR("فِي", "fi", n=N3(MT("أَسَدٌ", "a lion", "aslan»a"), DR("لِأَنَّهُ بِمَعْنَى شُجَاعٍ", "for it means «brave»", "«cesur» anlamında olduğu için"))),
  R("majr", "اللِّقَاءِ", "liqa"),
  R("khb", "وَرْدٌ", "ward-red", n=N3(DR("خَبَرٌ ثَانٍ لِلْمُبْتَدَإِ الْمَحْذُوفِ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ آخَرَ", "a second khabar of the omitted mubtada, or the khabar of another omitted mubtada", "mahzûf mübtedânın ikinci haberi, ya da başka bir mahzûf mübtedânın haberi"), ZW("الْوَرْدُ: الَّذِي يَضْرِبُ لَوْنُهُ إِلَى الْحُمْرَةِ", "وَرْد is one whose colour runs to red", "«verd»: rengi kırmızıya çalan"))),
  R("khb", "هَمُوسٌ", "hamus-hr", g=["sighat-mubalagha"], n=N3(DR("خَبَرٌ ثَالِثٌ", "a third khabar", "üçüncü haber"), ZW("الْهَمْسُ: صَوْتُ الْقَدَمِ، وَجَعَلَ الْأَسَدَ هَمُوسًا لِأَنَّهُ يُسْمَعُ مِنْ رِجْلَيْهِ فِي مَشْيِهِ صَوْتٌ", "هَمْس is the sound of the foot; he makes the lion «soft-treading» because a sound is heard from his feet as he walks", "«hems»: ayak sesi; aslanı «hemûs» kıldı, çünkü yürürken ayaklarından bir ses duyulur")))],
 [R("atfr", "وَرَبِيعٌ", "rabi", c="w", g=TB, of=("أَسَدٌ", "a lion", "esed"), n=HADD("تَشْبِيهٌ بَلِيغٌ ثَانٍ: الْمُشَبَّهُ حُجْرٌ، وَالْمُشَبَّهُ بِهِ الرَّبِيعُ — «وَكَانَ لِلنَّاسِ بِمَنْزِلَةِ الرَّبِيعِ … غَيْثَ الْجَدْبِ» (الزَّوْزَنِيُّ)", "a second tashbih baligh: Ḥujr is likened to the spring — «he was to the people as the spring … the rain in the drought» (al-Zawzanī)", "ikinci teşbîh-i belîğ: müşebbeh Hucr, müşebbehün bih bahar — «halk için bahar mesabesindeydi… kıtlığın yağmuru» (Zevzenî)")),
  PT("إِنْ", "in-shartiyya", "حَرْفُ شَرْطٍ جَازِمٌ", "a conditional particle that puts in jazm", "cezmeden şart harfi", g=["in-shartiyya"]),
  V("mt", "شَمَّرَتْ", "shammara", g=["form-ii-verbs", "istiara-makniyya"], n=N3(NT("فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ: فَهُوَ رَبِيعٌ (الدُّرَّةُ)", "in the seat of jazm as the verb of the condition; its answer is left out, shown by what goes before: «then he is a spring» (al-Durra)", "şart fiili olarak mahallen meczûm; cevabı mahzûftur, öncesi ona delâlet eder: «o bir bahardır» (Dürre)"), DR("وَرِوَايَتُهُ «شَنِعَتْ»", "his text reads «grew hideous»", "onun rivayeti «şeniat»tır"), ZW("شَمَّرَتْ: اسْتَعَدَّتْ — تَهَيَّأَتْ وَاسْتَعَدَّتِ السَّنَةُ الشَّدِيدَةُ لِلشَّرِّ", "شَمَّرَتْ: it made ready — the hard year girded and readied itself for evil", "«şemmerat»: hazırlandı — çetin yıl kötülük için hazırlandı"),
     HADD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَتِ السَّنَةُ بِرَجُلٍ يُشَمِّرُ لِلْأَمْرِ، وَطُوِيَ الْمُشَبَّهُ بِهِ وَدُلَّ عَلَيْهِ بِلَازِمِهِ «شَمَّرَتْ»", "an istiʿāra makniyya: the year is likened to a man girding himself for a task, who is folded away and shown by what goes with him, «girded»", "istiâre-i mekniyye: yıl, bir iş için paçaları sıvayan adama benzetilmiş; müşebbehün bih hazfedilip lâzımı «şemmerat» ile ona işaret edilmiştir"))),
  R("fail", "غَبْرَاءُ", "ghabra-tf", sign=S_DIPT_MR, g=["mamnu-min-sarf"], n=N3(QAF, ZW("الْغَبْرَاءُ: السَّنَةُ الشَّدِيدَةُ، لِاغْبِرَارِ الْهَوَاءِ فِيهَا", "غَبْرَاء is a hard year, for the dust that hangs in its air", "«gabrâ'»: havası tozlu olduğu için çetin yıl")))])
VV(58, "And we loosed the iron collar from Imruʾ al-Qays, after his prison and his toil had lasted long.",
  "İmruülkays'ın boynundaki demir halkayı, hapsi ve çilesi uzun sürdükten sonra çözdük.",
 [V("mna", "وَفَكَكْنَا", "fakka", c="w", g=["doubled-verbs"], n=N3(NT("وَفُكَّ إِدْغَامُهُ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "its doubling is undone because the subject pronoun is attached; the clause is joined to what goes before", "ref zamiri bitiştiği için idgâmı çözülmüştür; cümle öncekine ma'tûftur"), ZW("وَخَلَّصْنَا امْرَأَ الْقَيْسِ مِنْ حَبْسِهِ وَعَنَائِهِ", "we freed Imruʾ al-Qays from his prison and his toil", "İmruülkays'ı hapsinden ve çilesinden kurtardık"))),
  R("maf", "غُلَّ", "ghull-hr", mud=True),
  T("امْرِئِ", "imru", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، وَالرَّاءُ تَتْبَعُ حَرَكَةَ الْهَمْزَةِ، مُضَافٌ.",
    "The second term of the idafa, in jarr by the kasra — the ra follows the vowel of the hamza; annexed.", "Muzâfun ileyh, kesre ile mecrûr — râ hemzenin harekesine tâbidir; muzâf."),
  NAME("mdf", "الْقَيْسِ", "qays"),
  JP("عَنْهُ", "an", "هُ", n=MT("فَكَكْنَا", "we loosed", "çözdük»e"))],
 [T("بَعْدَمَا", "bada", "noun", ["maful-fih", "anwa-ma"], "«بَعْدَ» ظَرْفُ زَمَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِـ«فَكَكْنَا»، مُضَافٌ، وَ«مَا» مَصْدَرِيَّةٌ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ بَعْدَهَا فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ: بَعْدَ طُولِ حَبْسِهِ (الدُّرَّةُ).",
    "«بَعْدَ» is an adverb of time in nasb hanging on «we loosed», annexed; «مَا» makes a masdar, and it with the verb after it is in the seat of jarr as the second term: «after the length of his prison» (al-Durra).", "«Ba'de» zaman zarfı, mansûb, «çözdük»e müteallik, muzâf; «mâ» masdariyyedir; sonraki fiille birlikte muzâfun ileyh olarak mahallen mecrûr bir masdardır: «hapsinin uzamasından sonra» (Dürre).", segs=SG(("بَعْدَ", "bada", "noun"), ("مَا", "ma-masdariyya", "part"))),
  V("m", "طَالَ", "tala-long", g=["hollow-verbs"]),
  R("fail", "حَبْسُهُ", "habs", enc="هُ", g=["masdar"]),
  R("atfr", "وَالْعَنَاءُ", "ana-toil", c="w", of=("حَبْسُهُ", "his prison", "habsuhû"), n=QAF)])
VV(59, "And with al-Jawn — the Jawn of the house of the Banū l-Aws — went a stubborn troop, like a great bulging hill.",
  "Cevn ile — Benî Evs ailesinin Cevn'i ile — inatçı bir birlik vardı; sanki büyük, kabarık bir tepeydi.",
 [R("zarfm", "وَمَعَ", "maa", c="wi", mud=True, n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  NAME("mdf", "الْجَوْنِ", "jawn-name-hr"),
  R("bdlj", "جَوْنِ", "jawn-name-hr", pos="propn", mud=True, of=("الْجَوْنِ", "al-Jawn", "el-Cevn"), n=ZW("وَالْجَوْنُ الثَّانِي بَدَلٌ مِنَ الْأَوَّلِ، وَالْأَوَّلُ فِي التَّقْدِيرِ مَحْذُوفٌ، كَقَوْلِهِ تَعَالَى: «الْأَسْبَابَ، أَسْبَابَ السَّمَاوَاتِ» (غَافِر: ٣٦–٣٧)", "the second Jawn is a badal of the first, and the first is, in the parsing, set aside — as in God's words «the ways, the ways of the heavens» (Ghāfir 40:36–37)", "ikinci Cevn birincisinden bedeldir; birincisi takdirde hazfedilmiş sayılır — Allah Teâlâ'nın «yolları, göklerin yollarını» (Gâfir 40:36–37) sözünde olduğu gibi")),
  R("mdf", "آلِ", "aal", mud=True),
  R("mdf", "بَنِي", "banu", mud=True, sign=S_BANI, g=["jam-mudhakkar-salim"])],
 [NAME("mdf", "الْأَوْسِ", "aws"),
  R("mub", "عَنُودٌ", "anud-hr", g=["hadhf-wa-taqdir", "sighat-mubalagha"], n=N3(NT("مُؤَخَّرٌ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: كَتِيبَةٌ عَنُودٌ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "placed after; it is the adjective of an omitted noun, «a troop stubborn»; a fresh sentence", "sona bırakılmıştır; mahzûf bir mevsûfun sıfatıdır: «inatçı bir birlik»; cümle müste'nefedir"), ZW("وَكَانَتْ مَعَ الْجَوْنِ كَتِيبَةٌ شَدِيدَةُ الْعِنَادِ", "with al-Jawn was a troop of fierce stubbornness", "Cevn'in yanında çok inatçı bir birlik vardı"))),
  KAANNA("كَأَنَّهَا", enc="هَا", g=TB, n=N3(CL("nr", "عَنُودٌ", "a stubborn (troop)", "anûdun»"),
     NT("وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْكَتِيبَةُ، وَالْمُشَبَّهُ بِهِ الْهَضْبَةُ الدَّفْوَاءُ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الشَّوْكَةُ وَالْعُدَّةُ — ذَكَرَهُ الزَّوْزَنِيُّ: «كَأَنَّهَا فِي شَوْكَتِهَا وَعُدَّتِهَا هَضْبَةٌ»", "a tashbih mursal mujmal: the troop is likened to the bulging hill; the particle is كَأَنَّ; the point of likeness — might and equipment — is al-Zawzanī's: «as though in its might and equipment it were a hill»", "teşbîh-i mürsel mücmel: müşebbeh birlik, müşebbehün bih kabarık tepe, edat «keenne»; vech-i şebeh — güç ve teçhizat — Zevzenî'dedir: «gücünde ve teçhizatında sanki bir tepe»"))),
  R("khbka", "دَفْوَاءُ", "dafwa-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], n=QAF)])
VV(60, "We did not flinch beneath the dust of battle when they turned away routed, and when the fire's heat blazed.",
  "Kovalanarak geri döndüklerinde ve ateşin harı alevlendiğinde, savaş tozunun altında sızlanmadık.",
 [PT("مَا", "ma-nafiya", "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ", "a particle of negation; it governs nothing", "nefy harfi; ameli yoktur", g=["anwa-ma"]),
  V("mna", "جَزِعْنَا", "jazia", n=CL("ist")),
  R("zarfm", "تَحْتَ", "tahta", mud=True, n=MZ("جَزِعْنَا", "we flinched", "sızlandık»a")),
  R("mdf", "الْعَجَاجَةِ", "ajaja-hr", n=ZW("الْعَجَاجَةُ: الْغُبَارُ", "عَجَاجَة is dust", "«acâce»: toz")),
  PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«جَزِعْنَا»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb of past time built on sukun, in the seat of nasb, hanging on «we flinched», annexed to the clause after it", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «sızlandık»a müteallik, sonraki cümleye muzâf", g=["maful-fih"], pos="noun")],
 [V("mwa", "وَلَّوْا", "walla-amr", g=["form-ii-verbs", "naqis-verbs"], n=N3(CL("mdf", "إِذْ", "إِذْ", "iz"), DR("وَرِوَايَتُهُ «إِذْ وَلَّتْ بِأَقْفَائِهَا وَحَرَّ الصِّلَاءُ»", "his text reads «when it turned its napes, and the fire grew hot»", "onun rivayeti: «enselerini dönüp gittiğinde ve ateş kızdığında»"))),
  R("hal", "شِلَالًا", "shilal-hr", g=["masdar"], n=NT("صَاحِبُهَا وَاوُ الْجَمَاعَةِ: «حِينَ تَوَلَّوْا فِي حَالِ الطِّرَادِ» (الزَّوْزَنِيُّ)", "of the waw of the group: «when they turned away in the state of being chased» (al-Zawzanī)", "cemâat vâvından hâl: «kovalanma hâlinde dönüp gittiklerinde» (Zevzenî)")),
  PT("وَإِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَعْطُوفٌ عَلَى «إِذْ» قَبْلَهُ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb of past time built on sukun, in the seat of nasb, joined to the إِذْ before it, annexed to the clause after it", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; önceki «iz»e ma'tûf, sonraki cümleye muzâf", c="w", g=["maful-fih"], pos="noun"),
  V("ma", "تَلَظَّى", "talazza", g=["form-v-verbs", "naqis-verbs"], n=N3(CL("mdf", "إِذْ", "إِذْ", "iz"), ZW("تَلَظَّى: تَلَهَّبَ", "تَلَظَّى is to blaze", "«telazzâ»: alevlendi"))),
  R("fail", "الصِّلَاءُ", "sila-hr", n=N3(QAF, ZW("الصِّلَاءُ وَالصِّلَى: مَصْدَرُ صَلِيتُ بِالنَّارِ أَصْلَى إِذَا نَالَكَ حَرُّهَا؛ وَلَا حِينَ تَلَهَّبَ نَارُ الْحَرْبِ", "صِلَاء and صِلًى are the masdar of صَلِيتُ بِالنَّارِ, to be reached by a fire's heat: «nor when the fire of war blazed»", "«sılâ'» ve «sılâ»: ateşin harının sana ulaşması; «savaşın ateşi alevlendiğinde de»")))])
VV(61, "And we gave him the lord of Ghassān in requital for al-Mundhir, perforce, when blood could not be measured out (in vengeance).",
  "Kan (kısasla) ölçülemezken, Münzir'e karşılık Gassân'ın efendisini zorla ona kısas olarak verdik.",
 [V("mna", "وَأَقَدْنَاهُ", "aqada-qawad", c="w", enc="هُ", g=["form-iv-verbs", "hollow-verbs"], n=N3(NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is joined to what goes before", "cümle öncekine ma'tûftur"), ZW("أَقَدْتُهُ: أَعْطَيْتُهُ الْقَوَدَ، وَهُوَ الْقِصَاصُ", "أَقَدْتُهُ: I gave him the قَوَد, retaliation", "«ekadtuhû»: ona kısas hakkını verdim"))),
  T("رَبَّ", "rabb", "noun", ["hadhf-al-jarr", "idafa-definiteness"], "مَنْصُوبٌ عَلَى نَزْعِ الْخَافِضِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، مُضَافٌ (الدُّرَّةُ) — «وَأَعْطَيْنَاهُ مَلِكَ غَسَّانَ قَوَدًا بِالْمُنْذِرِ» (الزَّوْزَنِيُّ).",
    "In nasb by the dropping of the jarr letter, its sign the fatha; annexed (al-Durra) — «we gave him the king of Ghassān in requital for al-Mundhir» (al-Zawzanī).", "Cer harfinin düşmesiyle mansûb, alâmeti fetha; muzâf (Dürre) — «ona Münzir'e karşılık Gassân kralını kısas olarak verdik» (Zevzenî)."),
  NAME("mdf", "غَسَّانَ", "ghassan-hr", sign=S_DIPT_AN, g=["mamnu-min-sarf"])],
 [NAME("majr", "بِالْمُنْذِرِ", "mundhir-name", j="bi", n=MT("أَقَدْنَا", "we gave in requital", "kısas olarak verdik»e")),
  R("mutlaq", "كَرْهًا", "karh-hr", g=["masdar"], n=DR("مِنْ غَيْرِ لَفْظِ عَامِلِهِ، أَوْ حَالٌ بِمَعْنَى «كَارِهًا»", "not of its governor's wording; or a hal meaning «unwilling»", "âmilinin lafzından değil; ya da «istemeyerek» anlamında hâl")),
  PT("إِذْ", "idh", "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«أَقَدْنَا»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb of past time built on sukun, in the seat of nasb, hanging on «we gave in requital», annexed to the clause after it", "geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «kısas olarak verdik»e müteallik, sonraki cümleye muzâf", g=["maful-fih"], pos="noun"),
  LA_N(),
  V("d", "تُكَالُ", "kala-measure", pas=True, g=["hollow-verbs", "istiara", "istiara-tabaiyya"], n=N3(CL("mdf", "إِذْ", "إِذْ", "iz"),
     NT("وَفِيهِ اسْتِعَارَةٌ: «وَجَعَلَ كَيْلَ الدِّمَاءِ مُسْتَعَارًا لِلْقِصَاصِ» (الزَّوْزَنِيُّ)؛ وَهِيَ — عَلَى حَدِّ التَّلْخِيصِ — تَبَعِيَّةٌ لِأَنَّهَا فِي الْفِعْلِ", "an istiʿāra: «he made the measuring of blood a borrowed word for retaliation» (al-Zawzanī); by the Talkhīṣ's definition it is tabaʿiyya, being in a verb", "istiâre: «kanın ölçülmesini kısas için istiâre etti» (Zevzenî); Telhîs'in tarifine göre fiilde olduğu için tebeiyyedir"))),
  R("naib", "الدِّمَاءُ", "dam", g=["jam-taksir"], n=N3(QAF, ZW("حِينَ عَجَزَ النَّاسُ عَنِ الِاقْتِصَاصِ وَإِدْرَاكِ الْأَثْآرِ — وَهٰذِهِ هِيَ الْآيَةُ الثَّالِثَةُ", "when men were unable to take retaliation and win their vengeance — and this is the third sign", "insanlar kısas almaktan ve intikamlarını almaktan âciz kaldığında — üçüncü alâmet budur")))])
VV(62, "And we brought them nine kings, nobles, whose spoils were costly.",
  "Onlara, ganimetleri pahalı dokuz soylu kral getirdik.",
 [V("mna", "وَأَتَيْنَاهُمُ", "ata", c="w", enc="هُمُ", g=["naqis-verbs"], n=N3(NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is joined to what goes before", "cümle öncekine ma'tûftur"), MIM_W, ZW("وَأَتَيْنَاهُمْ بِتِسْعَةٍ مِنَ الْمُلُوكِ وَقَدْ أَسَرْنَاهُمْ", "we brought them nine kings whom we had taken captive", "onlara esir aldığımız dokuz kral getirdik"))),
  R("majr", "بِتِسْعَةِ", "tisa", j="bi", mud=True, g=["asma-al-adad-fil-kafiya"], n=N3(MT("أَتَيْنَا", "we brought", "getirdik»e"), NT("وَتَمْيِيزُهُ «أَمْلَاكٍ» مَجْرُورٌ بِالْإِضَافَةِ", "its specifier «kings» is in jarr as the second term of the idafa", "temyîzi «emlâk» izâfetle mecrûrdur")))],
 [R("mdf", "أَمْلَاكٍ", "malik-king", g=["jam-taksir", "tamyiz"]),
  R("naatj", "كِرَامٍ", "karim", g=["jam-taksir"], of=("أَمْلَاكٍ", "kings", "emlâk")),
  R("mub", "أَسْلَابُهُمْ", "salab-hr", enc="هُمْ", g=["jam-taksir"], n=ZW("الْأَسْلَابُ: جَمْعُ السَّلَبِ، وَهُوَ الثِّيَابُ وَالسِّلَاحُ وَالْفَرَسُ", "أَسْلَاب is the plural of سَلَب: the clothes, the arms and the horse (stripped from the slain)", "«eslâb», «seleb»in, yani (öldürülenden alınan) elbise, silah ve atın çoğuludur")),
  R("khb", "أَغْلَاءُ", "ghali-dear-hr", sign=S_DIPT_MR, g=["jam-taksir", "mamnu-min-sarf"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ ثَانِيَةٌ لِـ«أَمْلَاكٍ»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ", "the clause is a second adjective of «kings», in the seat of jarr, or a hal of them, in the seat of nasb", "cümle «emlâk»ın ikinci sıfatı olarak mahallen mecrûr, ya da ondan hâl olarak mahallen mansûb"), NT("وَهُوَ جَمْعٌ عَلَى «أَفْعِلَاءَ» مَمْنُوعٌ مِنَ الصَّرْفِ", "a plural on أَفْعِلَاء, a diptote", "«ef'ilâ'» kalıbında çoğul, gayr-i munsarif"), QAF, ZW("كَانَتْ أَسْلَابُهُمْ غَالِيَةَ الْأَثْمَانِ لِعِظَمِ أَخْطَارِهِمْ وَجَلَالَةِ أَقْدَارِهِمْ", "their spoils were of high price for their great rank and the majesty of their station", "ganimetleri, mevkilerinin büyüklüğü ve kadirlerinin yüceliği sebebiyle pahalıydı")))])
VV(63, "And we begot ʿAmr son of Umm Unās, not long since, when the bride-price came to us.",
  "Ümmü Unâs'ın oğlu Amr'ı, mehir bize geldiğinde, yakın zamanda biz doğurduk.",
 [V("mna", "وَوَلَدْنَا", "walada", c="wi", g=["mithal-verbs", "majaz-aqli"], n=N3(CL("ist"), ZW("أَيْ زَوَّجْنَا أُمَّهُ مِنْ أَبِيهِ لَمَّا أَتَانَا مَهْرُهَا؛ يُرِيدُ: إِنَّا أَخْوَالُ هٰذَا الْمَلِكِ", "that is, we married his mother to his father when her bride-price reached us: he means, we are this king's maternal uncles", "yani mehri bize gelince annesini babasıyla evlendirdik; «biz bu kralın dayılarıyız» demek istiyor"),
     HADD("مَجَازٌ عَقْلِيٌّ: أُسْنِدَ الْوِلَادُ إِلَى الْقَبِيلَةِ، وَهِيَ سَبَبُهُ بِتَزْوِيجِ أُمِّهِ — كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "a majāz ʿaqlī: the begetting is assigned to the tribe, its cause through giving his mother in marriage — as al-Zawzanī explains", "mecâz-ı aklî: doğurma, annesini evlendirmekle onun sebebi olan kabileye isnad edilmiştir — Zevzenî'nin açıkladığı gibi"))),
  R("maf", "عَمْرَو", "amr-name", pos="propn", n=NT("وَحُذِفَ تَنْوِينُهُ لِوَصْفِهِ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ", "its tanwin drops because it is described by «son» annexed to a name", "bir özel isme muzâf «ibn» ile vasıflandığı için tenvini düşmüştür")),
  R("naatn", "بْنَ", "ibn", mud=True, of=("عَمْرَو", "ʿAmr", "Amr")),
  R("mdf", "أُمِّ", "umm", mud=True),
  NAME("mdf", "أُنَاسٍ", "unas-name-hr", sign=("بِالْكَسْرَةِ — وَقَدْ صُرِفَ لِلضَّرُورَةِ، وَحَقُّهُ الْمَنْعُ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ (الدُّرَّةُ)", " — by the kasra: given tanwin by poetic licence (ṣurifa lil-ḍarūra), though by rule a diptote, a feminine proper name (al-Durra)", " — kesre ile: şiir zarureti için munsarif kılınmıştır; aslında özel isim ve müennes olduğu için gayr-i munsariftir (Dürre)"), g=["mamnu-min-sarf"])],
 [PR("مِنْ", "min", n=MT("وَلَدْنَا", "we begot", "doğurduk»a")),
  R("majr", "قَرِيبٍ", "qarib"),
  PT("لَمَّا", "lamma", "ظَرْفٌ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«قَرِيبٍ» لِأَنَّهُ صِفَةٌ مُشَبَّهَةٌ (الدُّرَّةُ)، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "an adverb meaning «when», built on sukun, in the seat of nasb, hanging on «not long» since it is a ṣifa mushabbaha (al-Durra), annexed to the clause after it", "«hîne» anlamında zarf, sükûn üzere mebnî, mahallen mansûb; sıfat-ı müşebbehe olduğu için «yakın»a müteallik (Dürre), sonraki cümleye muzâf", g=["maful-fih"]),
  V("ma", "أَتَانَا", "ata", enc="نَا", g=["naqis-verbs"], n=CL("mdf", "لَمَّا", "لَمَّا", "lemmâ")),
  R("fail", "الْحِبَاءُ", "hiba-hr", n=N3(QAF, ZW("الْحِبَاءُ: الْمَهْرُ — «لَمَّا أَتَانَا مَهْرُهَا»", "حِبَاء is the bride-price: «when her bride-price came to us»", "«hıbâ'»: mehir — «mehri bize geldiğinde»")))])
# =====================================================================================================================
# The poem — vv. 64–70 — وَاذْكُرُوا حِلْفَ ذِي الْمَجَازِ
# =====================================================================================================================
AMR_W = lambda: ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَوَاوُ الْجَمَاعَةِ " + _FA + "، وَالْأَلِفُ فَارِقَةٌ", "imperative built on the dropping of the nun; the waw of the group is the doer, in the seat of raf'; the alif is the separating alif", "nûnun hazfi üzere mebnî emir; cemâat vâvı fâildir, mahallen merfû; elif fârikadır")
AMR_TAGS = ["imperative-amr", "fail", "al-bariz-al-muttasil"]
W5 = ("، وَوَاوُ الْجَمَاعَةِ " + _FA, "; the waw of the group is the doer, in the seat of raf'", "; cemaat vâvı fâildir, mahallen merfû")
VV(64, "Such (kinship) as this draws out good counsel for the people — a desert with deserts beyond it.",
  "Bunun gibisi (akrabalık) kavme samimi öğüdü çıkarır — ötesinde başka çöller bulunan bir çöl (gibi birbirine bağlı).",
 [R("mub", "مِثْلُهَا", "mithl", enc="هَا", n=ZW("مِثْلُ هٰذِهِ الْقَرَابَةِ", "the like of this kinship", "bu akrabalığın benzeri")),
  V("d", "تُخْرِجُ", "akhraja", doer=HIYA("«مِثْلُهَا»", "«the like of it»", "«misluhâ»ya"), g=["form-iv-verbs"], n=N3(CL("khb", "مِثْلُهَا", "the like of it", "misluhâ"), NT("وَأُنِّثَ الْفِعْلُ لِأَنَّ «مِثْلَ» اكْتَسَبَ التَّأْنِيثَ بِإِضَافَتِهِ إِلَى ضَمِيرِ الْمُؤَنَّثِ", "the verb is feminine because «like» takes the feminine from the feminine pronoun it is annexed to", "fiil müennestir, çünkü «misl» müennes zamire izâfetle te'nîs kazanmıştır"), DR("وَرِوَايَتُهُ «يُخْرِجُ»", "his text reads it with ya", "onun rivayeti yâ iledir"))),
  R("maf", "النَّصِيحَةَ", "nasiha")],
 [R("majr", "لِلْقَوْمِ", "qawm", j="li", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«النَّصِيحَةَ»، أَوْ بِـ«تُخْرِجُ»، وَالْأَوَّلُ أَقْوَى", "the phrase hangs on «counsel», or on «draws out» — the first is stronger", "câr-mecrûr «öğüt»e ya da «çıkarır»a müteallik; birincisi daha kuvvetlidir")),
  R("khb", "فَلَاةٌ", "falat-hr", g=["hadhf-wa-taqdir"] + TB, n=N3(DR("لِمُبْتَدَإٍ مَحْذُوفٍ عَلَى رِوَايَةِ الرَّفْعِ، وَيُرْوَى بِالنَّصْبِ حَالًا مِنْ فَاعِلِ «تُخْرِجُ»", "of an omitted mubtada, in the reading with raf'; it is also related in nasb, as a hal of the doer of «draws out»", "raf' rivayetine göre mahzûf mübtedânın haberi; «çıkarır»ın fâilinden hâl olarak nasb ile de rivayet edilir"),
     HADD("تَشْبِيهٌ بَلِيغٌ: الْمُشَبَّهُ الْقَرَابَةُ، وَالْمُشَبَّهُ بِهِ الْفَلَاةُ الْمُتَّصِلَةُ بِالْفَلَوَاتِ، حُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ — وَصَفَهُ الزَّوْزَنِيُّ: «قُرْبَى أَرْحَامٍ يَتَّصِلُ بَعْضُهَا بِبَعْضٍ كَفَلَوَاتٍ يَتَّصِلُ بَعْضُهَا بِبَعْضٍ»", "a tashbih baligh: the kinship is likened to a desert joined to deserts, with particle and point left out — al-Zawzanī describes it: «kinship of wombs linked one to another, like deserts linked one to another»", "teşbîh-i belîğ: müşebbeh akrabalık, müşebbehün bih başka çöllere bitişik çöl; edat ve vech-i şebeh hazfedilmiştir — Zevzenî tarif eder: «birbirine bağlı rahim akrabalığı, birbirine bağlı çöller gibi»"))),
  PR("مِنْ", "min", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "دُونِهَا", "dun", enc="هَا"),
  R("mub", "أَفْلَاءُ", "falat-hr", g=["jam-taksir"], n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِـ«فَلَاةٌ»", "placed after; the clause is an adjective of «a desert», in the seat of raf'", "sona bırakılmıştır; cümle «felât»ın sıfatı, mahallen merfû"), QAF_N, ZW("الْفَلَاةُ تُجْمَعُ عَلَى الْفَلَا، ثُمَّ تُجْمَعُ الْفَلَا عَلَى الْأَفْلَاءِ", "فَلَاة has the plural فَلًا, and فَلًا in turn the plural أَفْلَاء", "«felât» «felâ» diye, «felâ» da «eflâ'» diye cemʿlenir")))])
VV(65, "So leave off pride and feigned blindness; and if you feign blindness, in feigned blindness is the sickness.",
  "Kibri ve körlük taslamayı bırakın; körlük taslarsanız, asıl hastalık o körlük taslamaktadır.",
 [V(AMR_W(), "فَاتْرُكُوا", "taraka", c="fi", g=AMR_TAGS, n=CL("ist")),
  R("maf", "الطَّيْخَ", "taykh-hr", n=N3(DR("وَرِوَايَتُهُ «الْبَغْيَ»", "his text reads «wrongdoing»", "onun rivayeti «el-bağy»dir"), ZW("الطَّيْخُ: التَّكَبُّرُ", "طَيْخ is pride", "«tayh»: kibir"))),
  T("وَالتَّعَاشِي", "taashi-hr", "noun", ["atf-nasaq", "ism-maqsur-manqus", "masdar"], WA_AR + "«التَّعَاشِي» مَعْطُوفٌ عَلَى «الطَّيْخَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، سُكِّنَتْ ضَرُورَةً، أَوْ عَلَى لُغَةِ مَنْ يَقُولُ: رَأَيْتُ قَاضِيكْ (الدُّرَّةُ) — التَّعَاشِي: التَّعَامِي، وَهُمَا تَكَلُّفُ الْعَشَى وَالْعَمَى مِمَّنْ لَيْسَ بِهِ عَشًى وَلَا عَمًى (الزَّوْزَنِيُّ).",
    "The waw conjoins; «feigned blindness» is joined to «pride», in nasb by a fatha estimated on the ya, which is made quiescent by licence, or after the dialect that says «I saw your judge» with a quiescent ya (al-Durra) — تَعَاشِي is feigning blindness: putting on night-blindness and blindness by one who has neither (al-Zawzanī).",
    "«ve» + «teâşî» «tayh»a ma'tûftur; yâ üzerinde takdîrî fetha ile mansûb; yâ zaruretle, ya da «ra'eytu kâdîk» diyenlerin lehçesine göre sükûnlu kılınmıştır (Dürre) — «teâşî»: körlük taslamak, gece körlüğü ve körlüğü olmayanın onları taklit etmesi (Zevzenî).", segs=SG(("وَ", "wa", "conj"), ("التَّعَاشِي", "taashi-hr", "noun"))),
  T("وَإِمَّا", "in-shartiyya", "part", ["in-shartiyya", "anwa-ma"], WA_AR + "«إِمَّا» أَصْلُهَا «إِنْ» الشَّرْطِيَّةُ أُدْغِمَتْ فِي «مَا» الزَّائِدَةِ — وَالْغَالِبُ تَوْكِيدُ الْفِعْلِ بَعْدَهَا بِالنُّونِ، وَلَمْ يُؤَكَّدْ هُنَا (الدُّرَّةُ).",
    "The waw conjoins; «إِمَّا» is the conditional إِنْ merged with the extra مَا — the verb after it is usually strengthened with the nun of emphasis, and here it is not (al-Durra).", "«ve» + «immâ», şart «in»inin zâid «mâ»ya idgam edilmiş hâlidir — ardındaki fiil çoğunlukla te'kîd nûnuyla pekiştirilir, burada pekiştirilmemiştir (Dürre).", segs=SG(("وَ", "wa", "conj"), ("إِمَّ", "in-shartiyya", "part"), ("ا", "ma-zaida", "part")))],
 [V(JZ("بِـ«إِنْ»", "by إِنْ", "«in» ile", sign="nun"), "تَتَعَاشَوْا", "taasha-hr", g=["form-vi-verbs", "naqis-verbs", "afal-khamsa", "fail", "mulhaq-bil-jinas"], n=N3(W5, NT("فِعْلُ الشَّرْطِ، وَالْأَلِفُ فَارِقَةٌ", "the verb of the condition; the alif is the separating alif", "şart fiili; elif fârikadır"),
     HADD("يُلْحَقُ بِالْجِنَاسِ مَا يَجْمَعُهُ الِاشْتِقَاقُ: «تَتَعَاشَوْا» وَ«التَّعَاشِي» مِنْ أَصْلٍ وَاحِدٍ", "what derivation brings together is attached to jinās: «you feign blindness» and «feigned blindness» come from one root", "iştikakın bir araya getirdiği cinasa ilhak edilir: «tetaâşev» ve «et-teâşî» aynı kökten"))),
  PR("فَفِي", "fi", c="fj", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "التَّعَاشِي", "taashi-hr", sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " — by a kasra estimated on the ya", " — yâ üzerinde takdîrî kesre ile"), g=["ism-maqsur-manqus", "masdar"]),
  R("mub", "الدَّاءُ", "daa-amr", n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "placed after; the clause is the answer of the condition, in the seat of jazm", "sona bırakılmıştır; cümle şartın cevabı olarak mahallen meczûm"), QAF, ZW("يَعْنِي: أَفْضَى بِكُمْ ذٰلِكَ إِلَى شَرٍّ عَظِيمٍ", "he means: that will bring you to great evil", "yani bu sizi büyük bir kötülüğe götürür")))])
VV(66, "And remember the pact of Dhū l-Majāz, and the covenants and the sureties set down in it,",
  "Zü'l-Mecâz antlaşmasını ve orada ortaya konan ahitleri ve kefilleri hatırlayın;",
 [V(AMR_W(), "وَاذْكُرُوا", "dhakara", c="w", g=AMR_TAGS, n=CL("atf", "اتْرُكُوا", "leave off", "bırakın")),
  R("maf", "حِلْفَ", "hilf-hr", mud=True),
  R("mdf", "ذِي", "dhu", mud=True, sign=S_YA5, g=["five-nouns"]),
  NAME("mdf", "الْمَجَازِ", "majaz-place-hr", n=ZW("ذُو الْمَجَازِ: مَوْضِعٌ جَمَعَ بِهِ عَمْرُو بْنُ هِنْدٍ بَكْرًا وَتَغْلِبَ وَأَصْلَحَ بَيْنَهُمَا، وَأَخَذَ مِنْهُمَا الْوَثَائِقَ وَالرُّهُونَ", "Dhū l-Majāz is the place where ʿAmr ibn Hind brought Bakr and Taghlib together, made peace between them, and took bonds and hostages from them", "Zü'l-Mecâz, Amr b. Hind'in Bekir ile Tağlib'i topladığı, aralarını bulduğu ve onlardan teminat ve rehineler aldığı yerdir")),
  PT("وَمَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى «حِلْفَ»", "a relative noun built on sukun, in the seat of nasb, joined to «pact»", "sükûn üzere mebnî ism-i mevsûl, «hilf»e ma'tûf olarak mahallen mansûb", c="w", g=["ism-mawsul", "atf-nasaq"], pos="pron")],
 [V("m", "قُدِّمَ", "qaddama", pas=True, g=["form-ii-verbs"], n=CL("sila")),
  JP("فِيهِ", "fi", "هُ", n=MT("قُدِّمَ", "were set down", "ortaya kondu»ya")),
  R("naib", "الْعُهُودُ", "ahd", g=["jam-taksir"]),
  R("atfr", "وَالْكُفَلَاءُ", "kafil", c="w", g=["jam-taksir"], of=("الْعُهُودُ", "the covenants", "el-uhûd"), n=N3(QAF, ZW("وَاذْكُرُوا الْعَهْدَ الَّذِي كَانَ مِنَّا بِهٰذَا الْمَوْضِعِ وَتَقْدِيمَ الْكُفَلَاءِ فِيهِ", "remember the covenant we made at this place and the sureties set down in it", "bu yerde yaptığımız ahdi ve orada kefillerin ortaya konmasını hatırlayın")))])
VV(67, "for fear of wrong and transgression — and can whims undo what is in the parchments?",
  "haksızlık ve saldırıdan sakınarak — hevesler sayfalarda yazılı olanı bozabilir mi?",
 [R("lah", "حَذَرَ", "hadhar", mud=True, g=["masdar"], n=DR("عَامِلُهُ «قُدِّمَ»، أَوْ مَحْذُوفٌ", "governed by «were set down», or by an omitted verb", "âmili «ortaya kondu»dur, ya da mahzûftur")),
  R("mdf", "الْجَوْرِ", "jawr", n=DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ؛ وَرِوَايَتُهُ «الْخَوْنِ»", "a masdar annexed to its object; his text reads «treachery»", "masdarın mef'ûlüne izâfeti; onun rivayeti «el-havn»dir")),
  R("atfj", "وَالتَّعَدِّي", "taaddi-hr", c="w", sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " — by a kasra estimated on the ya", " — yâ üzerinde takdîrî kesre ile"), g=["ism-maqsur-manqus", "masdar"], of=("الْجَوْرِ", "wrong", "el-cevr")),
  PT("وَهَلْ", "hal-istifham", "الْوَاوُ لِلِاسْتِئْنَافِ، وَ«هَلْ» حَرْفُ اسْتِفْهَامٍ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى النَّفْيِ: «حَرْفُ اسْتِفْهَامٍ مَعْنَاهُ النَّفْيُ» (الدُّرَّةُ)؛ «يُرِيدُ أَنَّ مَا كُتِبَ فِي الْعُهُودِ لَا تُبْطِلُهُ أَهْوَاؤُكُمُ الضَّالَّةُ» (الزَّوْزَنِيُّ)", "the waw opens a fresh sentence; هَلْ is a particle of question — the question has left asking for denial: «a question particle meaning denial» (al-Durra); «he means that what is written in the covenants is not voided by your errant whims» (al-Zawzanī)", "vâv isti'nâfiyyedir; «hel» istifhâm harfi — istifhâm nefy anlamına çıkmıştır: «anlamı nefy olan istifhâm harfi» (Dürre); «ahitlerde yazılanı sapık heveslerinizin iptal edemeyeceğini kastediyor» (Zevzenî)", g=["al-istifham", "khuruj-al-istifham"], segs=SG(("وَ", "wa", "conj"), ("هَلْ", "hal-istifham", "part")))],
 [V("d", "يَنْقُضُ", "naqada-hr", n=CL("ist")),
  PT("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "a relative noun built on sukun, in the seat of nasb as the object", "sükûn üzere mebnî ism-i mevsûl, mef'ûlün bih olarak mahallen mansûb", g=["ism-mawsul", "maful-bihi"], pos="pron"),
  PR("فِي", "fi", n=MTH("صِلَةِ الْمَوْصُولِ", "the omitted ṣila of the relative", "mevsûlün mahzûf sılasına")),
  R("majr", "الْمَهَارِقِ", "muhraq-hr", g=["jam-taksir"], n=ZW("الْمَهَارِقُ: جَمْعُ الْمُهْرَقِ، وَهُوَ فَارِسِيٌّ مُعَرَّبٌ: يَأْخُذُونَ الْخِرْقَةَ وَيَطْلُونَهَا بِشَيْءٍ ثُمَّ يَصْقُلُونَهَا ثُمَّ يَكْتُبُونَ عَلَيْهَا", "مَهَارِق is the plural of مُهْرَق, a Persian word arabicised: they take a cloth, coat it with something, polish it, then write on it", "«mehârik», «muhrak»ın çoğuludur; Arapçalaşmış Farsça bir kelime: bir bez alıp bir şeyle sıvar, cilalar, sonra üzerine yazarlar")),
  R("fail", "الْأَهْوَاءُ", "hawa-desire", g=["jam-taksir"], n=QAF)])
VV(68, "And know that we and you, in what we stipulated on the day we differed, are equal.",
  "Bilin ki biz ve siz, ayrılığa düştüğümüz gün şart koştuklarımızda eşitiz.",
 [V(AMR_W(), "وَاعْلَمُوا", "alima", c="w", g=AMR_TAGS, n=CL("atf", "اذْكُرُوا", "remember", "hatırlayın")),
  INNA("أَنَّنَا", which="anna", enc="نَا"),
  PT("وَإِيَّاكُمْ", "iyya", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى «نَا» اسْمِ «أَنَّ»", "a detached pronoun built on sukun, in the seat of nasb, joined to «we», the noun of أَنَّ", "sükûn üzere mebnî munfasıl zamir, «enne»nin ismi «nâ»ya ma'tûf olarak mahallen mansûb", c="w", g=["atf-nasaq", "al-mabni-wal-mudmar"], pos="pron")],
 [T("فِيمَا", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "«فِي» حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَوَاءُ» لِأَنَّهُ بِمَعْنَى «مُسْتَوُونَ» (الدُّرَّةُ).",
    "«فِي» is a jarr letter and «مَا» a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «equal», which means «on a level» (al-Durra).", "«Fî» cer harfi, «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr «eşit»e müteallik, çünkü «müstevûn» anlamındadır (Dürre).", segs=SG(("فِي", "fi", "prep"), ("مَا", "ma-mawsula", "pron"))),
  V("mna", "اشْتَرَطْنَا", "ishtarata", g=["form-viii-verbs"], n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: اشْتَرَطْنَاهُ", "the pronoun referring back is left out: «stipulated it»", "dönen zamir mahzûftur: «onu şart koştuk»"))),
  R("zarfz", "يَوْمَ", "yawm", mud=True, n=MZ("اشْتَرَطْنَا", "we stipulated", "şart koştuk»a")),
  V("mna", "اخْتَلَفْنَا", "ikhtalafa", g=["form-viii-verbs"], n=CL("mdf", "يَوْمَ", "the day", "yevm")),
  R("khba", "سَوَاءُ", "sawa", n=N3(NT("وَ«أَنَّ» وَاسْمُهَا وَخَبَرُهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيِ «اعْلَمُوا»", "أَنَّ with its noun and predicate makes a masdar standing for the two objects of «know»", "«enne», ismi ve haberi «bilin»in iki mef'ûlünün yerini tutan bir masdardır"), QAF_N, ZW("أَنَّنَا وَإِيَّاكُمْ فِي تِلْكَ الشَّرَائِطِ الَّتِي أَوْثَقْنَاهَا يَوْمَ تَعَاقَدْنَا مُسْتَوُونَ", "we and you are equal in the conditions we bound fast on the day we made the compact", "antlaştığımız gün bağladığımız şartlarda biz ve siz eşitiz")))])
VV(69, "(You charge us) by false and wrongful pretext, as gazelles are slaughtered for the sheep in the fold.",
  "(Başkasının suçunu bize) asılsız ve haksız bir bahaneyle (yüklediniz); ağıldaki koyunlar yerine ceylanların kesildiği gibi.",
 [T("عَنَنًا", "anan-hr", "noun", ["maful-bihi", "hadhf-wa-taqdir"], "مَنْصُوبٌ بِفِعْلٍ مَحْذُوفٍ: مَفْعُولٌ بِهِ، أَوْ مَفْعُولٌ مُطْلَقٌ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ (الدُّرَّةُ) — أَيْ: أَلْزَمْتُمُونَا ذَنْبَ غَيْرِنَا عَنَنًا (الزَّوْزَنِيُّ)؛ الْعَنَنُ: الِاعْتِرَاضُ، وَالْفِعْلُ عَنَّ يَعِنُّ.",
    "In nasb by an omitted verb — its object, or an absolute object — its sign the fatha (al-Durra): «you have laid on us the guilt of others by pretext» (al-Zawzanī); عَنَن is cutting across, objecting — the verb is عَنَّ يَعِنُّ.", "Mahzûf bir fiille mansûb — mef'ûlün bih ya da mef'ûl-i mutlak — alâmeti fetha (Dürre): «başkasının suçunu bize bahaneyle yüklediniz» (Zevzenî); «anan»: araya girme, itiraz; fiili «anne yeinnu»."),
  R("naatn", "بَاطِلًا", "batil", of=("عَنَنًا", "pretext", "ananen")),
  R("atfn", "وَظُلْمًا", "zulm", c="w", of=("عَنَنًا", "pretext", "ananen"), g=["masdar"]),
  PT("كَمَا", "ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ بَعْدَهَا مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِـ«عَنَنًا» وَمَا عُطِفَ عَلَيْهِ (الدُّرَّةُ) — وَفِيهِ تَشْبِيهُ تَمْثِيلٍ مُرْسَلٌ: حَالُهُمْ فِي أَخْذِهِمْ بِذَنْبِ غَيْرِهِمْ بِحَالِ الظِّبَاءِ تُذْبَحُ عَنِ الْغَنَمِ الَّتِي وَجَبَ ذَبْحُهَا، وَالْأَدَاةُ الْكَافُ — وَصَفَهُ الزَّوْزَنِيُّ: «أَلْزَمْتُمُونَا ذَنْبَ غَيْرِنَا عَنَنًا كَمَا يُذْبَحُ الظَّبْيُ لِحَقٍّ وَجَبَ فِي الْغَنَمِ»، وَتَسْمِيَتُهُ تَمْثِيلًا عَلَى حَدِّ التَّلْخِيصِ",
     "the kaf is the jarr letter of likening and «mā» makes a masdar: with the verb after it, it is a masdar in jarr after the kaf; the phrase hangs on an omitted adjective of «pretext» and what is joined to it (al-Durra) — a tashbih of tamthīl, mursal: their being taken for others' guilt is likened to gazelles slaughtered in place of the sheep that were owed; the particle is the kaf — al-Zawzanī describes it: «you laid on us the guilt of others by pretext, as the gazelle is slaughtered for a due owed on the sheep»; the name tamthīl is by the Talkhīṣ's definition",
     "kâf teşbîh ve cer harfi, «mâ» masdariyyedir; sonraki fiille kâf ile mecrûr bir masdardır; câr-mecrûr «anan»ın ve ona ma'tûf olanın mahzûf sıfatına müteallik (Dürre) — temsîlî teşbîh, mürsel: başkasının suçuyla yakalanmaları, kesilmesi gereken koyunlar yerine kesilen ceylanların hâline benzetilmiştir; edat kâf — Zevzenî tarif eder: «başkasının suçunu bize bahaneyle yüklediniz; koyunlarda gereken bir hak için ceylanın kesildiği gibi»; temsîl adı Telhîs'in tarifine göredir",
     pos="prep", g=TB + ["huruf-jarr"], segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part")))],
 [V("d", "تُعْتَرُ", "atara-hr", pas=True, n=ZW("الْعَتْرُ: ذَبْحُ الْعَتِيرَةِ، وَهِيَ ذَبِيحَةٌ كَانَتْ تُذْبَحُ لِلْأَصْنَامِ فِي رَجَبٍ؛ وَكَانَ الرَّجُلُ يَنْذِرُ إِنْ بَلَّغَ اللهُ غَنَمَهُ مِائَةً ذَبَحَ مِنْهَا وَاحِدَةً، ثُمَّ رُبَّمَا ضَنَّتْ نَفْسُهُ بِهَا فَأَخَذَ ظَبْيًا فَذَبَحَهُ مَكَانَهَا", "عَتْر is slaughtering the عَتِيرَة, a victim slaughtered to the idols in Rajab; a man would vow, if God brought his flock to a hundred, to slaughter one of them — then, grudging it, he might take a gazelle and slaughter it in its place", "«atr»: Receb'de putlara kesilen «atîre»yi kesmek; adam, Allah koyunlarını yüze ulaştırırsa birini kesmeyi adardı; sonra kıyamayıp bir ceylan yakalar, onun yerine keserdi")),
  PR("عَنْ", "an", n=MT("تُعْتَرُ", "are slaughtered", "kesilir»e")),
  R("majr", "حُجْرَةِ", "hujra", mud=True, n=ZW("الْحُجْرَةُ: النَّاحِيَةُ", "حُجْرَة is a side, a quarter", "«hucre»: yan, taraf")),
  R("mdf", "الرَّبِيضِ", "rabid-hr", n=NT("الرَّبِيضُ: الْغَنَمُ فِي مَرَابِضِهَا (حَاشِيَةُ الْمُحَقِّقِ)", "رَبِيض is sheep in their folds (the editor's note)", "«rebîd»: ağıllarındaki koyunlar (muhakkikin dipnotu)")),
  R("naib", "الظِّبَاءُ", "zaby", g=["jam-taksir"], n=QAF)])
VV(70, "Is the guilt of Kinda on us, that their raider took spoil — and ours the requital?",
  "Kinde'nin akıncısı ganimet aldı diye onun günahı bize mi? Bedeli de bizden mi?",
 [T("أَعَلَيْنَا", "ala", "prep", ["al-istifham", "khuruj-al-istifham", "huruf-jarr", "al-bariz-al-muttasil"], "الْهَمْزَةُ حَرْفُ اسْتِفْهَامٍ «مَعْنَاهُ التَّوْبِيخُ وَالتَّقْرِيعُ» (الدُّرَّةُ)، وَ«عَلَى» حَرْفُ جَرٍّ، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ بِهِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ — وَفِيهِ خُرُوجُ الِاسْتِفْهَامِ إِلَى التَّوْبِيخِ: «يُوَبِّخُهُمْ وَيُعَيِّرُهُمْ» (الزَّوْزَنِيُّ)؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "The hamza is a particle of question «meaning rebuke and reproach» (al-Durra); عَلَى is a jarr letter and نَا is in the seat of jarr after it; the phrase hangs on an omitted, fronted khabar — the question has left asking for rebuke: «he rebukes and taunts them» (al-Zawzanī); a fresh sentence.",
    "Hemze «anlamı tevbîh ve azarlama olan» istifhâm harfidir (Dürre); «alâ» cer harfi, «nâ» onunla mahallen mecrûr; câr-mecrûr öne alınmış mahzûf habere müteallik — istifhâm tevbîhe çıkmıştır: «onları azarlıyor ve ayıplıyor» (Zevzenî); cümle müste'nefedir.",
    segs=SG(("أَ", "a-istifham", "part"), ("عَلَيْ", "ala", "prep"), ("نَا", "pron-1p", "pron"))),
  R("mub", "جُنَاحُ", "junah-hr", mud=True, n=N3(NT("مُؤَخَّرٌ", "placed after", "sona bırakılmıştır"), ZW("الْجُنَاحُ: الْإِثْمُ", "جُنَاح is sin, guilt", "«cunâh»: günah"))),
  NAME("mdf", "كِنْدَةَ", "kinda-hr", sign=S_DIPT_F, g=["mamnu-min-sarf"]),
  AN(n=DR("وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَرْفِ جَرٍّ مَحْذُوفٍ، مُتَعَلِّقٍ بِـ«جُنَاحُ» لِأَنَّهُ بِمَعْنَى الْمَصْدَرِ", "the masdar it makes is in jarr by a dropped jarr letter, hanging on «guilt», which has a masdar's sense", "te'vil edilen masdar mahzûf bir cer harfiyle mecrûrdur; masdar anlamında olduğu için «günah»a müteallik"))],
 [V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "يَغْنَمَ", "ghanima-hr", g=["nawasib-wa-jawazim-al-mudari"]),
  T("غَازِيهِمُ", "ghazi", "noun", ["fail", "ism-maqsur-manqus", "ism-fail", "al-bariz-al-muttasil", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ، وَ«هِمُ» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَحُرِّكَتْ مِيمُهُ بِالضَّمِّ لِإِقَامَةِ الْوَزْنِ.",
    "The doer, in raf' by a damma estimated on the ya; annexed, and «هِمُ» is the second term of the idafa, in the seat of jarr, its mim voweled with damma to keep the metre.", "Fâil; yâ üzerinde takdîrî damme ile merfû, muzâf; «himu» muzâfun ileyh, mahallen mecrûr; mîmi vezin için damme ile harekelenmiştir.", segs=SG(("غَازِي", "ghazi", "noun"), ("هِمُ", "pron-3mp", "pron"))),
  JP("وَمِنَّا", "min", "نَا", c="wh", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "الْجَزَاءُ", "jaza-answer", n=N3(DR("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «غَازِيهِمُ»، وَالرَّابِطُ الْوَاوُ", "placed after; the clause is a hal of «their raider», in the seat of nasb; the waw is the link", "sona bırakılmıştır; cümle «akıncıları»ndan hâl, mahallen mansûb; bağlayıcı vâvdır"), QAF, ZW("أَعَلَيْنَا ذَنْبُ كِنْدَةَ أَنْ يَغْنَمَ غَازِيهِمْ مِنْكُمْ، وَمِنَّا يَكُونُ جَزَاءُ ذٰلِكَ؟", "is the guilt of Kinda on us, that their raider took spoil from you, and is the requital of it to come from us?", "Kinde'nin akıncısı sizden ganimet aldı diye onun suçu bize mi, bunun bedeli de bizden mi olacak?")))])
# =====================================================================================================================
# The poem — vv. 71–76 — أَمْ عَلَيْنَا جَرَّى إِيَادٍ
# =====================================================================================================================
AM = lambda n=NO: PT("أَمْ", "am", "حَرْفُ عَطْفٍ، وَالْجُمْلَةُ بَعْدَهُ مَعْطُوفَةٌ عَلَى مِثْلِهَا قَبْلَهُ لَا مَحَلَّ لَهَا (الدُّرَّةُ)" + n[0], "a conjunction; the clause after it is joined to its like before it and has no seat (al-Durra)" + n[1], "atıf harfi; sonraki cümle öncekine ma'tûftur, mahalli yoktur (Dürre)" + n[2], g=["aw-imma-am-la-bal-lakin-fil-kafiya", "atf-nasaq"])
LA_Z = lambda: PT("وَلَا", "la-nafiya", "الْوَاوُ حَرْفُ عَطْفٍ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ (الدُّرَّةُ)", "the waw conjoins, and لَا is extra, strengthening the negation (al-Durra)", "vâv atıf harfi; «lâ» nefyi pekiştirmek için zâiddir (Dürre)", g=["la-nafiya", "atf-nasaq"], segs=SG(("وَ", "wa", "conj"), ("لَا", "la-nafiya", "part")))
VV(71, "Or is the crime of Iyād on us — (laid on us) as burdens are hung on the middle of the laden camel?",
  "Yoksa İyâd'ın suçu bize mi — yüklerin yüklü devenin ortasına asıldığı gibi (bize mi asılıyor)?",
 [AM(NT("— وَالِاسْتِفْهَامُ بِهَا مُتَّصِلٌ بِتَوْبِيخِ الْبَيْتِ قَبْلَهُ: «أَمْ عَلَيْنَا جِنَايَةُ إِيَادٍ؟» (الزَّوْزَنِيُّ)", "— the question it carries continues the rebuke of the verse before: «or is the crime of Iyād on us?» (al-Zawzanī)", "— taşıdığı soru önceki beytin azarlamasının devamıdır: «yoksa İyâd'ın suçu bize mi?» (Zevzenî)")),
  JP("عَلَيْنَا", "ala", "نَا", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "جَرَّى", "jarra-hr", mud=True, sign=S_AR, g=["ism-maqsur-manqus"], n=N3(NT("مُؤَخَّرٌ", "placed after", "sona bırakılmıştır"), ZW("الْجَرَاءُ وَالْجَرَّى — بِالْمَدِّ وَالْقَصْرِ —: الْجِنَايَةُ", "جَرَاء and جَرَّى, long and short, are a crime", "«cerâ'» ve «cerrâ» — memdûd ve maksûr —: suç"))),
  NAME("mdf", "إِيَادٍ", "iyad-hr", n=DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ وَرِوَايَتُهُ «جَرَّى الْعِبَادِ»", "a masdar annexed to its doer; his text reads «the crime of the ʿIbād»", "masdarın fâiline izâfeti; onun rivayeti «cerre'l-ıbâd»dır")),
  PT("كَمَا", "ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ بَعْدَهَا مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَصْدَرٍ مَحْذُوفٍ مَعَ فِعْلِهِ: أَتُحَمِّلُونَنَا ذُنُوبَ غَيْرِنَا تَحْمِيلًا كَتَعْلِيقِ الْأَثْقَالِ بِظَهْرِ الْبَعِيرِ؟ (الدُّرَّةُ) — وَفِيهِ تَشْبِيهُ تَمْثِيلٍ مُرْسَلٌ: حَالُهُمْ فِي تَحْمِيلِهِمْ جِنَايَةَ غَيْرِهِمْ بِحَالِ الْأَثْقَالِ تُعَلَّقُ عَلَى وَسَطِ الْبَعِيرِ الْمُحَمَّلِ، وَالْأَدَاةُ الْكَافُ — «أَلْزَمْتُمُونَا ذٰلِكَ كَمَا تُعَلَّقُ الْأَثْقَالُ عَلَى وَسَطِ الْبَعِيرِ الْمُحَمَّلِ» (الزَّوْزَنِيُّ)، وَتَسْمِيَتُهُ تَمْثِيلًا عَلَى حَدِّ التَّلْخِيصِ",
     "the kaf is the jarr letter of likening and «mā» makes a masdar: with the verb after it, it is a masdar in jarr after the kaf; the phrase hangs on the omitted adjective of a masdar dropped with its verb: «do you load us with others' sins as burdens are hung on a camel's back?» (al-Durra) — a tashbih of tamthīl, mursal: their being loaded with others' crime is likened to burdens hung on the middle of the laden camel; the particle is the kaf — «you laid that on us as burdens are hung on the middle of the laden camel» (al-Zawzanī); the name tamthīl is by the Talkhīṣ's definition",
     "kâf teşbîh ve cer harfi, «mâ» masdariyyedir; sonraki fiille kâf ile mecrûr bir masdardır; câr-mecrûr fiiliyle hazfedilmiş bir masdarın mahzûf sıfatına müteallik: «başkalarının günahlarını, yüklerin devenin sırtına asılması gibi bize mi yüklüyorsunuz?» (Dürre) — temsîlî teşbîh, mürsel: başkasının suçunun kendilerine yüklenmesi, yüklü devenin ortasına asılan yüklerin hâline benzetilmiştir; edat kâf — «yüklerin yüklü devenin ortasına asıldığı gibi bunu bize yüklediniz» (Zevzenî); temsîl adı Telhîs'in tarifine göredir",
     pos="prep", g=TB + ["huruf-jarr"], segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part")))],
 [V("m", "نِيطَ", "nata-hr", pas=True, g=["hollow-verbs"], n=ZW("النَّوْطُ: التَّعْلِيقُ", "نَوْط is hanging", "«nevt»: asmak")),
  R("majr", "بِجَوْزِ", "jawz-hr", j="bi", mud=True, n=N3(MT("نِيطَ", "are hung", "asıldı»ya"), ZW("الْجَوْزُ: الْوَسَطُ، وَالْجَمْعُ الْأَجْوَازُ", "جَوْز is the middle; the plural is أَجْوَاز", "«cevz»: orta; çoğulu «ecvâz»"))),
  R("mdf", "الْمُحَمَّلِ", "muhammal", g=["ism-maful"]),
  R("naib", "الْأَعْبَاءُ", "ib", g=["jam-taksir"], n=N3(QAF, ZW("الْعِبْءُ: الثِّقْلُ", "عِبْء is a load", "«ib'»: yük")))])
VV(72, "Not of us are al-Muḍarrabūn, nor Qays, nor Jandal, nor al-Ḥaddāʾ.",
  "Muḍarrebûn bizden değildir; ne Kays, ne Cendel, ne de Haddâ'.",
 [T("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins", "kinaya", "tarid-talwih-ramz"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ — وَفِيهِ تَعْرِيضٌ: «عَيَّرَهُمْ بِأَنَّهُمْ مِنْهُمْ» (الزَّوْزَنِيُّ)، أَيْ نَفْيُهُمْ عَنْهُ تَعْرِيضٌ بِأَنَّهُمْ مِنْ تَغْلِبَ.",
    "A defective, non-conjugating past verb built on fatha — a fresh sentence — and in it a taʿrīḍ (insinuation): «he taunts them with being of them» (al-Zawzanī) — disowning these people insinuates that they belong to Taghlib.", "Câmid nâkıs mâzî, fetha üzere mebnî — cümle müste'nefedir — tarîz vardır: «onların kendilerinden olduğunu söyleyerek onları ayıplıyor» (Zevzenî) — bunları kendinden saymaması, Tağlib'den olduklarına tarîzdir."),
  JP("مِنَّا", "min", "نَا", n=MTH("خَبَرِ «لَيْسَ» مُقَدَّمًا", "the omitted predicate of لَيْسَ, placed first", "öne alınmış mahzûf «leyse» haberine")),
  T("الْمُضَرَّبُونَ", "mudarrab-hr", "propn", ["kana-wa-akhawatuha", "jam-mudhakkar-salim"], "اسْمُ «لَيْسَ» مُؤَخَّرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ — «هٰؤُلَاءِ الْمُضَرَّبُونَ لَيْسُوا مِنَّا» (الزَّوْزَنِيُّ).",
    "The noun of لَيْسَ, placed after, in raf' by the waw, a sound masculine plural; its nun stands for the tanwin of the singular — «these Muḍarrabūn are not of us» (al-Zawzanī).", "«Leyse»nin sona bırakılmış ismi; cem-i müzekker sâlim olduğu için vâv ile merfû; nûn müfreddeki tenvinin karşılığıdır — «bu Muḍarrebûn bizden değildir» (Zevzenî)."),
  LA_Z()],
 [R("atfr", "قَيْسٌ", "qays-name-tf", pos="propn", of=("الْمُضَرَّبُونَ", "al-Muḍarrabūn", "el-Muḍarrebûn")),
  LA_Z(),
  R("atfr", "جَنْدَلٌ", "jandal-name-hr", pos="propn", of=("الْمُضَرَّبُونَ", "al-Muḍarrabūn", "el-Muḍarrebûn")),
  LA_Z(),
  R("atfr", "الْحَدَّاءُ", "hadda-hr", pos="propn", of=("الْمُضَرَّبُونَ", "al-Muḍarrabūn", "el-Muḍarrebûn"), n=QAF)])
VV(73, "Or (are) the crimes of the Banū ʿAtīq (on us)? We, if you break faith, are quit of you.",
  "Yoksa Benî Atîk'in suçları (bize mi)? Ahdi bozarsanız biz sizden uzağız.",
 [AM(),
  R("mub", "جَنَايَا", "janaya-hr", mud=True, sign=S_AR, g=["jam-taksir", "hadhf-wa-taqdir"], n=N3(NT("وَخَبَرُهُ مَحْذُوفٌ: أَمْ عَلَيْنَا جَنَايَا بَنِي عَتِيقٍ (الزَّوْزَنِيُّ)؛ وَجَعَلَهُ الدُّرَّةُ مَعْطُوفًا عَلَى «جَرَّى» قَبْلَهُ — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "its khabar is left out: «or are the crimes of the Banū ʿAtīq on us?» (al-Zawzanī); al-Durra makes it joined to «the crime» before it — a masdar annexed to its doer", "haberi mahzûftur: «yoksa Benî Atîk'in suçları bize mi?» (Zevzenî); Dürre onu önceki «cerrâ»ya ma'tûf sayar — masdarın fâiline izâfeti"))),
  R("mdf", "بَنِي", "banu", mud=True, sign=S_BANI, g=["jam-mudhakkar-salim"]),
  NAME("mdf", "عَتِيقٍ", "atiq-name-hr"),
  INNA("فَإِنَّا", enc="نَا", c="fi", n=NT("وَحُذِفَتْ إِحْدَى النُّونَيْنِ تَخْفِيفًا", "one of the two nuns is dropped for lightness", "iki nûndan biri hafiflik için düşmüştür"))],
 [T("مِنْكُمُ", "min", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَ«كُمُ» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِهِ، حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِإِقَامَةِ الْوَزْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بُرَآءُ».",
    "A jarr letter; «كُمُ» is an attached pronoun in the seat of jarr after it, its mim voweled with damma to keep the metre — the phrase hangs on «quit».", "Cer harfi; «kumu» onunla mahallen mecrûr bitişik zamir, mîmi vezin için damme ile harekelenmiştir — câr-mecrûr «uzak»a müteallik.", segs=SG(("مِنْ", "min", "prep"), ("كُمُ", "pron-2mp", "pron"))),
  PT("إِنْ", "in-shartiyya", "حَرْفُ شَرْطٍ جَازِمٌ", "a conditional particle that puts in jazm", "cezmeden şart harfi", g=["in-shartiyya"]),
  V("mtum", "غَدَرْتُمْ", "ghadara-hr", n=NT("فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ، وَالْجُمْلَةُ الشَّرْطِيَّةُ مُعْتَرِضَةٌ — «إِنْ نَقَضْتُمُ الْعَهْدَ فَإِنَّا بُرَآءُ مِنْكُمْ» (الزَّوْزَنِيُّ)", "in the seat of jazm as the verb of the condition; its answer is left out, shown by what goes before, and the conditional clause is a parenthesis — «if you break the covenant, we are quit of you» (al-Zawzanī)", "şart fiili olarak mahallen meczûm; cevabı mahzûftur, öncesi ona delâlet eder; şart cümlesi mu'tarızadır — «ahdi bozarsanız biz sizden uzağız» (Zevzenî)")),
  R("khbi", "بُرَآءُ", "bari", g=["jam-taksir", "mamnu-min-sarf"], n=N3(NT("وَهُوَ جَمْعٌ عَلَى «فُعَلَاءَ» مَمْنُوعٌ مِنَ الصَّرْفِ", "a plural on فُعَلَاء, a diptote", "«fuale'â» kalıbında çoğul, gayr-i munsarif"), QAF, DR("وَرِوَايَتُهُ «فَمَنْ يَغْدِرْ فَإِنَّا مِنْ حَرْبِهِمْ بُرَآءُ»", "his text reads «whoever breaks faith, we are quit of their war»", "onun rivayeti: «kim ahdi bozarsa biz onların savaşından uzağız»")))])
VV(74, "And eighty of Tamīm (raided you), in their hands spears whose points are death.",
  "Temîm'den seksen kişi de (size baskın yaptı); ellerinde, uçları ölüm olan mızraklar.",
 [T("وَثَمَانُونَ", "thamanun", "noun", ["fail", "hadhf-wa-taqdir", "jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], WA_ISTINAF[0] + "«ثَمَانُونَ» فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: غَزَاكُمْ ثَمَانُونَ، مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ؛ وَتَمْيِيزُهُ مَحْذُوفٌ: ثَمَانُونَ رَجُلًا (الدُّرَّةُ) — «وَغَزَاكُمْ ثَمَانُونَ مِنْ بَنِي تَمِيمٍ» (الزَّوْزَنِيُّ).",
    WA_ISTINAF[1] + "«eighty» is the doer of an omitted verb — «there raided you eighty» — in raf' by the waw, declining like the sound masculine plural, its nun standing for the tanwin; its specifier is left out: «eighty men» (al-Durra) — «and eighty of the Banū Tamīm raided you» (al-Zawzanī).",
    WA_ISTINAF[2] + "«semânûn» mahzûf bir fiilin fâilidir: «size seksen kişi baskın yaptı»; cem-i müzekker sâlime mülhak olduğu için vâv ile merfû, nûn tenvinin karşılığı; temyîzi mahzûftur: «seksen adam» (Dürre) — «Benî Temîm'den seksen kişi size baskın yaptı» (Zevzenî).", segs=SG(("وَ", "wa", "conj"), ("ثَمَانُونَ", "thamanun", "noun"))),
  PR("مِنْ", "min", n=MTH("صِفَةٍ لِلتَّمْيِيزِ الْمَحْذُوفِ", "an omitted adjective of the omitted specifier", "mahzûf temyîzin mahzûf sıfatına")),
  NAME("majr", "تَمِيمٍ", "tamim")],
 [R("majr", "بِأَيْدِيهِمْ", "yad", j="bi", enc="هِمْ", g=["jam-taksir"], sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " — by a kasra estimated on the ya", " — yâ üzerinde takdîrî kesre ile"), n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "رِمَاحٌ", "rumh", g=["jam-taksir"], n=DR("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "placed after; the clause is a hal, in the seat of nasb", "sona bırakılmıştır; cümle hâldir, mahallen mansûb")),
  R("mub", "صُدُورُهُنَّ", "sadr", enc="هُنَّ", g=["jam-taksir"], n=ZW("وَصَدْرُ كُلِّ شَيْءٍ: أَوَّلُهُ — رِمَاحٌ أَسِنَّتُهَا الْقَتْلُ", "the صَدْر of anything is its foremost part: spears whose heads are death", "her şeyin «sadr»ı onun önüdür: uçları ölüm olan mızraklar")),
  R("khb", "الْقَضَاءُ", "qada", n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِـ«رِمَاحٌ»", "the clause is an adjective of «spears», in the seat of raf'", "cümle «rimâh»ın sıfatı, mahallen merfû"), QAF, ZW("الْقَضَاءُ: الْقَتْلُ، أَيِ الْقَاتِلَةُ", "قَضَاء here is death, that is, deadly", "«kazâ'» burada öldürmedir, yani öldürücü")))])
VV(75, "They left them cut to pieces, and came home with spoil from which the camel-drivers' song deafens.",
  "Onları paramparça bıraktılar ve develeri sürenlerin türküsünün kulakları sağır ettiği ganimetlerle döndüler.",
 [V("mw", "تَرَكُوهُمْ", "taraka", enc="هُمْ", encrole="maf1", g=["mafulayn"], n=CL("ist")),
  R("maf2", "مُلَحَّبِينَ", "mulahhab-hr", sign=("بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", " — by the ya, a sound masculine plural; its nun stands for the tanwin of the singular", " — cem-i müzekker sâlim olduğu için yâ ile; nûn müfreddeki tenvinin karşılığıdır"), g=["jam-mudhakkar-salim", "ism-maful"], n=N3(DR("وَقِيلَ: حَالٌ مِنَ الْهَاءِ", "others: a hal of the ha", "hâdan hâl olduğu da söylenmiştir"), ZW("التَّلْحِيبُ: التَّقْطِيعُ؛ مُقَطَّعِينَ بِالسُّيُوفِ", "تَلْحِيب is cutting to pieces: hewn by swords", "«telhîb»: parçalamak; kılıçlarla paramparça"))),
  V("mw", "وَآبُوا", "aba-return", c="w", g=["hollow-verbs"], n=N3(CL("atf", "تَرَكُوهُمْ", "they left them", "onları bıraktılar"), ZW("الْأَوْبُ وَالْإِيَابُ: الرُّجُوعُ", "أَوْب and إِيَاب are returning", "«evb» ve «iyâb»: dönüş")))],
 [R("majr", "بِنِهَابٍ", "nahb", j="bi", g=["jam-taksir"], n=MT("آبُوا", "came home", "döndüler»e")),
  V("d", "يُصِمُّ", "asamma-v-hr", g=["form-iv-verbs", "doubled-verbs", "kinaya"], n=N3(CL("nj", "نِهَابٍ", "spoil", "nihâbin»"),
     NT("وَفِيهِ كِنَايَةٌ عَنْ كَثْرَةِ الْغَنَائِمِ: «يُصِمُّ حُدَاءُ حُدَاتِهَا آذَانَ السَّامِعِينَ؛ أَشَارَ بِذٰلِكَ إِلَى كَثْرَتِهَا» (الزَّوْزَنِيُّ)", "a kināya for the mass of the spoil: «the song of its drivers deafens the ears of those who hear — by it he points to its abundance» (al-Zawzanī)", "ganimetin bolluğundan kinaye: «sürücülerinin türküsü dinleyenlerin kulaklarını sağır eder; bununla onun çokluğuna işaret etti» (Zevzenî)"))),
  JP("مِنْهَا", "min", "هَا", n=N3(MT("يُصِمُّ", "deafens", "sağır eder»e"), DR("وَرِوَايَتُهُ «مِنْهُ»", "his text reads «from it» (masc.)", "onun rivayeti «minhu»dur"))),
  R("fail", "الْحُدَاءُ", "huda-hr", n=QAF)])
VV(76, "Or is the crime of Ḥanīfa on us, or (the crime of) what the dusty land gathered of Muḥārib?",
  "Yoksa Hanîfe'nin suçu bize mi, ya da tozlu toprağın Muhârib'den bir araya getirdiklerinin (suçu) mu?",
 [AM(),
  JP("عَلَيْنَا", "ala", "نَا", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "جَرَّى", "jarra-hr", mud=True, sign=S_AR, g=["ism-maqsur-manqus"], n=NT("مُؤَخَّرٌ", "placed after", "sona bırakılmıştır")),
  NAME("mdf", "حَنِيفَةَ", "hanifa", sign=S_DIPT_F, g=["mamnu-min-sarf"]),
  AM(NT("— وَرِوَايَةُ الدُّرَّةِ «أَوْ»", "— al-Durra's text has «or» (أَوْ)", "— Dürre'nin rivayetinde «ev»dir")),
  PT("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مَعْطُوفٌ عَلَى «جَرَّى» (الدُّرَّةُ) — وَعَلَى شَرْحِ الزَّوْزَنِيِّ: «أَمْ جِنَايَةُ مَا جَمَعَتِ الْأَرْضُ … مِنْ مُحَارِبٍ»، فَالْمُضَافُ مَحْذُوفٌ", "a relative noun built on sukun, in the seat of raf', joined to «the crime» (al-Durra) — after al-Zawzanī's gloss, «or the crime of what the land gathered … of Muḥārib», the annexed word is left out", "sükûn üzere mebnî ism-i mevsûl, «cerrâ»ya ma'tûf olarak mahallen merfû (Dürre) — Zevzenî'nin şerhine göre «yoksa toprağın Muhârib'den topladıklarının suçu mu» olup muzâf mahzûftur", g=["ism-mawsul", "atf-nasaq"], pos="pron")],
 [V("mt", "جَمَّعَتْ", "jammaa-hr", g=["form-ii-verbs"], n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: جَمَّعَتْهُ", "the pronoun referring back is left out: «gathered it»", "dönen zamir mahzûftur: «onu topladı»"), DR("وَرِوَايَتُهُ «جَمَعَتْ»", "his text reads «جَمَعَتْ» (Form I)", "onun rivayeti «cemaat»tır"))),
  PR("مِنْ", "min", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ، وَهُوَ بَيَانٌ لِـ«مَا»", "the phrase hangs on an omitted hal; it explains «what»", "câr-mecrûr mahzûf bir hâle müteallik; «mâ»yı açıklar")),
  NAME("majr", "مُحَارِبٍ", "muharib-name"),
  R("fail", "غَبْرَاءُ", "ghabra-tf", sign=S_DIPT_MR, g=["mamnu-min-sarf", "majaz-aqli"], n=N3(QAF, ZW("أَمْ جِنَايَةُ مَا جَمَعَتِ الْأَرْضُ أَوِ السَّنَةُ الْغَبْرَاءُ مِنْ مُحَارِبٍ", "or the crime of what the dusty earth, or the dusty year, gathered of Muḥārib", "yoksa tozlu toprağın ya da tozlu yılın Muhârib'den topladıklarının suçu mu"),
     HADD("مَجَازٌ عَقْلِيٌّ: أُسْنِدَ التَّجْمِيعُ إِلَى الْغَبْرَاءِ — الْأَرْضِ أَوِ السَّنَةِ — وَهِيَ مَكَانُهُ أَوْ زَمَانُهُ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "a majāz ʿaqlī: the gathering is assigned to the dusty one — the earth or the year — its place or its time, as al-Zawzanī explains", "mecâz-ı aklî: toplama, onun mekânı ya da zamanı olan «gabrâ»ya — toprağa ya da yıla — isnad edilmiştir; Zevzenî'nin açıkladığı gibi")))])
# =====================================================================================================================
# The poem — vv. 77–82 — وَالْبَلَاءُ بَلَاءُ
# =====================================================================================================================
VV(77, "Or is the crime of Quḍāʿa on us? Nay, there is not on us, in what they did, the least moisture (of guilt).",
  "Yoksa Kudâa'nın suçu bize mi? Hayır, onların işledikleri suçtan bize bir damla (pay) yoktur.",
 [AM(),
  JP("عَلَيْنَا", "ala", "نَا", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "جَرَّى", "jarra-hr", mud=True, sign=S_AR, g=["ism-maqsur-manqus"], n=NT("مُؤَخَّرٌ؛ مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "placed after; a masdar annexed to its doer", "sona bırakılmıştır; masdarın fâiline izâfeti")),
  NAME("mdf", "قُضَاعَةَ", "qudaa-amr", sign=S_DIPT_F, g=["mamnu-min-sarf"]),
  PT("أَمْ", "am", "حَرْفُ عَطْفٍ — وَهِيَ هُنَا بِمَعْنَى «بَلْ»، كَمَا شَرَحَهُ الزَّوْزَنِيُّ: «بَلْ لَيْسَ عَلَيْنَا فِي جِنَايَتِهِمْ نَدًى»؛ وَالْجُمْلَةُ بَعْدَهَا مُسْتَأْنَفَةٌ، وَهُوَ أَوْلَى مِنَ الْعَطْفِ (الدُّرَّةُ)", "a conjunction — here meaning «nay», as al-Zawzanī explains: «nay, there is not on us in their crime the least moisture»; the clause after it is a fresh one, which is better than joining it (al-Durra)", "atıf harfi — burada «bel» anlamındadır, Zevzenî'nin açıkladığı gibi: «hayır, onların suçunda bize bir damla yoktur»; sonraki cümle müste'neftir, bu atıftan evlâdır (Dürre)", g=["aw-imma-am-la-bal-lakin-fil-kafiya"])],
 [T("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ.", "A defective, non-conjugating past verb built on fatha.", "Câmid nâkıs mâzî, fetha üzere mebnî."),
  JP("عَلَيْنَا", "ala", "نَا", n=MTH("خَبَرِ «لَيْسَ» مُقَدَّمًا", "the omitted predicate of لَيْسَ, placed first", "öne alınmış mahzûf «leyse» haberine")),
  T("فِيمَا", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "«فِي» حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْخَبَرِ الْمَحْذُوفِ، أَوْ هُمَا خَبَرٌ ثَانٍ (الدُّرَّةُ).",
    "«فِي» is a jarr letter and «مَا» a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on the omitted predicate, or is a second predicate (al-Durra).", "«Fî» cer harfi, «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr mahzûf habere müteallik, ya da ikinci haberdir (Dürre).", segs=SG(("فِي", "fi", "prep"), ("مَا", "ma-mawsula", "pron"))),
  V("mwa", "جَنَوْا", "jana-v-hr", g=["naqis-verbs"], n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: جَنَوْهُ", "the pronoun referring back is left out: «committed it»", "dönen zamir mahzûftur: «onu işlediler»"))),
  T("أَنْدَاءُ", "nada-ant", "noun", ["kana-wa-akhawatuha", "jam-taksir", "kinaya", "al-qafiya"], "اسْمُ «لَيْسَ» مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ" + QAF_N[0] + " — وَفِيهِ كِنَايَةٌ: «بَلْ لَيْسَ عَلَيْنَا فِي جِنَايَتِهِمْ نَدًى، أَيْ لَا تَلْحَقُنَا وَلَا تَلْزَمُنَا تِلْكَ الْجِنَايَةُ» (الزَّوْزَنِيُّ).",
    "The noun of لَيْسَ, placed after, in raf' by the damma" + QAF_N[1] + " — a kināya: «nay, there is not on us in their crime the least moisture: that crime does not reach us nor bind us» (al-Zawzanī).",
    "«Leyse»nin sona bırakılmış ismi, damme ile merfû" + QAF_N[2] + " — kinaye: «hayır, onların suçunda bize bir damla yoktur; yani o suç bize ulaşmaz, bizi bağlamaz» (Zevzenî).")])
VV(78, "Then they came seeking to win back (their spoil), and neither a spotted ewe nor a white one came back to them.",
  "Sonra (ganimetlerini) geri almaya çalışarak geldiler; ne benekli bir koyun ne de beyaz bir koyun onlara geri döndü.",
 [THUMMA(),
  V("mw", "جَاءُوا", "jaa", g=["hollow-verbs"], n=N3(NT("وَالْأَلِفُ فَارِقَةٌ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the alif is the separating alif; the clause is joined to what goes before", "elif fârikadır; cümle öncekine ma'tûftur"), ZW("هٰذِهِ الْأَبْيَاتُ كُلُّهَا تَعْيِيرٌ لَهُمْ وَإِبَانَةٌ عَنْ تَعَدِّيهِمْ وَطَلَبِهِمُ الْمُحَالَ", "all these verses taunt them and lay bare their wrongdoing and their asking for the impossible", "bu beyitlerin hepsi onları ayıplamak, saldırganlıklarını ve imkânsızı istemelerini ortaya koymaktır"))),
  V("d5", "يَسْتَرْجِعُونَ", "istarjaa-hr", g=["form-x-verbs", "afal-khamsa"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «جَاءُوا»، وَالرَّابِطُ الضَّمِيرُ", "the clause is a hal of the doer of «they came», in the seat of nasb; the pronoun is the link", "cümle «geldiler»in fâilinden hâl, mahallen mansûb; bağlayıcı zamirdir")),
  LAM("فَلَمْ", c="f")],
 [V(JZ("بِـ«لَمْ»", "by لَمْ", "«lem» ile"), "تَرْجِعْ", "rajaa", n=CL("atf", "جَاءُوا", "they came", "geldiler")),
  JP("لَهُمْ", "li", "هُمْ", n=MT("تَرْجِعْ", "came back", "döndü»ye")),
  R("fail", "شَامَةٌ", "shama-hr", n=ZW("فَلَمْ تُرَدَّ عَلَيْهِمْ شَاةٌ زَهْرَاءُ — أَيْ بَيْضَاءُ — وَلَا ذَاتُ شَامَةٍ", "not a single ewe was given back to them, white or spotted", "onlara ne beyaz ne benekli bir koyun geri verildi")),
  LA_Z(),
  R("atfr", "زَهْرَاءُ", "azhar-hr", sign=S_DIPT_MR, g=["mamnu-min-sarf"], of=("شَامَةٌ", "a spotted one", "şâme"), n=QAF)])
VV(79, "They did not make the Banū Razāḥ lawful prey at Barqāʾ Niṭāʿ, so as to have a curse from them upon them.",
  "Benî Rezâh'ı Berkâu Nitâ'da helal saymadılar ki onların aleyhlerine bir bedduası olsun.",
 [LAM(),
  V(JZ("بِـ«لَمْ»", "by لَمْ", "«lem» ile", sign="nun"), "يُحِلُّوا", "ahalla", g=["form-iv-verbs", "doubled-verbs", "afal-khamsa", "fail", "kinaya", "tarid-talwih-ramz"], n=N3(W5, NT("وَالْأَلِفُ فَارِقَةٌ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "the alif is the separating alif — a fresh sentence", "elif fârikadır — cümle müste'nefedir"),
     ZW("أَحْلَلْتُهُ: جَعَلْتُهُ حَلَالًا؛ مَا أَحَلَّ قَوْمُنَا مَحَارِمَ هٰؤُلَاءِ الْقَوْمِ … يُعَيِّرُهُمْ بِأَنَّهُمْ أَحَلُّوا مَحَارِمَ هٰؤُلَاءِ الْقَوْمِ بِهٰذَا الْمَوْضِعِ فَدَعَوْا عَلَيْهِمْ", "أَحْلَلْتُهُ is «I made him lawful»: our people did not make this people's sanctities lawful … he taunts them with having done so at this place, so that they cursed them", "«ahleltuhû»: onu helal kıldım; kavmimiz bu kavmin haram şeylerini helal saymadı… onları, bu yerde bu kavmin haramlarını helal sayıp onların bedduasını almakla ayıplıyor"),
     NT("وَفِيهِ تَعْرِيضٌ: نَفْيُهُ عَنْ قَوْمِهِ تَعْيِيرٌ لِبَنِي تَغْلِبَ بِأَنَّهُمْ فَعَلُوهُ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "a taʿrīḍ: denying it of his own people taunts Taghlib with having done it, as al-Zawzanī explains", "tarîz: bunu kendi kavminden nefyetmesi, Tağlib'i bunu yapmış olmakla ayıplamaktır; Zevzenî'nin açıkladığı gibi"))),
  R("maf", "بَنِي", "banu", mud=True, sign=S_BANI, g=["jam-mudhakkar-salim"]),
  NAME("mdf", "رَزَاحٍ", "razah-hr")],
 [T("بِبَرْقَاءِ", "barqa-hr", "propn", ["huruf-jarr", "idafa-definiteness", "mamnu-min-sarf"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«بَرْقَاءِ» مَجْرُورٌ بِالْكَسْرَةِ — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ يُجَرُّ بِالْكَسْرَةِ لِإِضَافَتِهِ — مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُحِلُّوا» — وَيُرْوَى بِالْفَتْحِ عَلَى الْمَنْعِ مِنَ الصَّرْفِ، وَ«نِطَاعٍ» صِفَتُهُ (الدُّرَّةُ).",
    "The ba is a jarr letter, and «Barqāʾ» is in jarr by the kasra — a diptote takes kasra when annexed — annexed; the phrase hangs on «make lawful» — it is also related with fatha as a diptote, «Niṭāʿ» then being its adjective (al-Durra).", "Bâ cer harfi; «Berkâ'» kesre ile mecrûr — gayr-i munsarif izâfet hâlinde kesre ile mecrûr olur — muzâf; câr-mecrûr «helal saymadılar»a müteallik — gayr-i munsarif olarak fetha ile de rivayet edilir; o zaman «Nitâ'» sıfatıdır (Dürre).", segs=SG(("بِ", "bi", "prep"), ("بَرْقَاءِ", "barqa-hr", "propn"))),
  NAME("mdf", "نِطَاعٍ", "nitaa-hr"),
  JP("لَهُمْ", "li", "هُمْ", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  JP("عَلَيْهِمْ", "ala", "هِمْ", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْخَبَرِ الْمَحْذُوفِ أَيْضًا", "the phrase hangs on the omitted khabar too", "câr-mecrûr da mahzûf habere müteallik")),
  R("mub", "دُعَاءُ", "dua", n=N3(NT("مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «بَنِي رَزَاحٍ»؛ وَرِوَايَةُ الدُّرَّةِ «لَمْ يُخَلُّوا» وَالْجُمْلَةُ عِنْدَهُ مَفْعُولٌ ثَانٍ", "placed after; the clause is a hal of «the Banū Razāḥ», in the seat of nasb; al-Durra's text reads «they did not leave», and there the clause is a second object", "sona bırakılmıştır; cümle «Benî Rezâh»tan hâl, mahallen mansûb; Dürre'nin rivayeti «lem yuhallû»dur ve orada cümle ikinci mef'ûldür"), QAF_N))])
VV(80, "Then they went back from them with a back-breaking blow, and water does not cool the burning thirst.",
  "Sonra onların yanından bel kıran bir belâyla döndüler; su ise o yakıcı susuzluğu serinletmez.",
 [THUMMA(),
  V("mw", "فَاءُوا", "faa", g=["hollow-verbs"], n=N3(NT("وَالْأَلِفُ فَارِقَةٌ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the alif is the separating alif; the clause is joined to what goes before", "elif fârikadır; cümle öncekine ma'tûftur"), ZW("الْفَيْءُ: الرُّجُوعُ، وَالْفِعْلُ فَاءَ يَفِيءُ", "فَيْء is returning; the verb is فَاءَ يَفِيءُ", "«fey'»: dönüş; fiili «fâe yefî'u»"))),
  JP("مِنْهُمْ", "min", "هُمْ", n=MT("فَاءُوا", "they went back", "döndüler»e")),
  R("majr", "بِقَاصِمَةِ", "qasima-hr", j="bi", mud=True, g=["ism-fail", "kinaya"], n=N3(DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«فَاءُوا»، أَوْ بِمَحْذُوفٍ حَالٍ مِنْ وَاوِ الْجَمَاعَةِ؛ مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ", "the phrase hangs on «they went back», or on an omitted hal of the waw of the group; an active participle annexed to its object", "câr-mecrûr «döndüler»e, ya da cemâat vâvından mahzûf bir hâle müteallik; ism-i fâilin mef'ûlüne izâfeti"),
     NT("وَفِيهِ كِنَايَةٌ عَنْ مَوْصُوفٍ: «بِدَاهِيَةٍ قَصَمَتْ ظُهُورَهُمْ» (الزَّوْزَنِيُّ)", "a kināya for the thing described: «with a disaster that broke their backs» (al-Zawzanī)", "mevsûftan kinaye: «bellerini kıran bir belâyla» (Zevzenî)")))],
 [R("mdf", "الظَّهْرِ", "zahr"),
  LA_N("وَلَا", c="w"),
  V("d", "يَبْرَدُ", "barada-hr", n=NT("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا؛ وَهٰكَذَا ضُبِطَ فِي الطَّبْعَةِ بِفَتْحِ الرَّاءِ، وَالْمَعْرُوفُ فِي «بَرَدَ» الْمُتَعَدِّي «يَبْرُدُ»", "the clause is joined to what goes before; the edition prints it with fatha on the ra, though the usual form of the transitive بَرَدَ is يَبْرُدُ", "cümle öncekine ma'tûftur; baskıda râ fethalı basılmıştır; geçişli «bered»in bilinen muzârii ise «yebrudu»dur")),
  R("maf", "الْغَلِيلَ", "ghalil-hr", g=["istiara", "aqsam-al-istiara"], n=N3(ZW("وَغَلِيلُ أَجْوَافٍ لَا يُسَكِّنُهُ شُرْبُ الْمَاءِ، لِأَنَّهُ حَرَارَةُ الْحِقْدِ لَا حَرَارَةُ الْعَطَشِ؛ يُرِيدُ أَنَّهُمْ … لَمْ يَثْأَرُوا بِقَتْلَاهُمْ", "a burning in the breast that drinking water does not still, for it is the heat of rancour, not the heat of thirst: he means they did not avenge their slain", "su içmenin dindirmediği bir iç yanması; çünkü o susuzluğun değil kinin harareti: maktullerinin intikamını alamadıklarını kastediyor"),
     HADD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَ الْغَلِيلُ — حَرَارَةُ الْعَطَشِ — لِحَرَارَةِ الْحِقْدِ، وَالْقَرِينَةُ مَا شَرَحَهُ الزَّوْزَنِيُّ", "an istiʿāra taṣrīḥiyya: غَلِيل, the burning of thirst, is borrowed for the burning of rancour; the sign is what al-Zawzanī explains", "istiâre-i tasrîhiyye: susuzluk harareti olan «galîl», kin hararetine istiâre edilmiştir; karîne Zevzenî'nin açıkladığıdır"))),
  R("fail", "الْمَاءُ", "ma-water", n=QAF)])
VV(81, "Then horsemen, after that, with al-Ghallāq — no pity, and no sparing.",
  "Sonra, bundan sonra, Gallâk ile birlikte atlılar (size geldi) — ne merhamet vardı ne esirgeme.",
 [THUMMA(),
  T("خَيْلٌ", "khayl", "noun", ["fail", "hadhf-wa-taqdir"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ مَرْفُوعٌ بِالضَّمَّةِ (الدُّرَّةُ)، تَقْدِيرُهُ: ثُمَّ جَاءَتْكُمْ خَيْلٌ — «ثُمَّ جَاءَتْكُمْ خَيْلٌ مِنَ الْغَلَّاقِ فَأَغَارَتْ عَلَيْكُمْ» (الزَّوْزَنِيُّ).",
    "The doer of an omitted verb, in raf' by the damma (al-Durra): «then there came to you horsemen» — «then horsemen came on you from al-Ghallāq and raided you» (al-Zawzanī).", "Mahzûf bir fiilin fâili, damme ile merfû (Dürre): «sonra size atlılar geldi» — «sonra Gallâk'tan size atlılar gelip baskın yaptı» (Zevzenî)."),
  PR("مِنْ", "min", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَحْذُوفِ", "the phrase hangs on the omitted verb", "câr-mecrûr mahzûf fiile müteallik")),
  R("majr", "بَعْدِ", "bada", mud=True),
  PT("ذَاكَ", "dhaka", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ، وَالْكَافُ حَرْفُ خِطَابٍ", "a demonstrative built on sukun, in the seat of jarr as the second term of the idafa; the kaf is a particle of address", "sükûn üzere mebnî işaret ismi, muzâfun ileyh olarak mahallen mecrûr; kâf hitap harfidir", g=["asma-al-ishara", "idafa-definiteness"], pos="pron"),
  R("zarfm", "مَعَ", "maa", mud=True, n=MTH("صِفَةٍ لِـ«خَيْلٌ»", "an omitted adjective of «horsemen»", "«hayl»in mahzûf sıfatına"))],
 [NAME("mdf", "الْغَلَّاقِ", "ghallaq-hr"),
  PT("لَا", "la-nafiya", "حَرْفُ نَفْيٍ مُهْمَلٌ لِتَكَرُّرِهِ", "a particle of negation, left ungoverning because it is repeated", "nefy harfi; tekrarlandığı için amel etmez", g=["la-nafiya"]),
  R("mub", "رَأْفَةٌ", "rafa-hr", n=DR("وَخَبَرُهُ مَحْذُوفٌ: لَا عِنْدَهُمْ رَأْفَةٌ، وَيَحْتَمِلُ أَنْ يَكُونَ نَائِبَ فَاعِلٍ لِفِعْلٍ مَحْذُوفٍ: لَا تُوجَدُ عِنْدَهُمْ رَأْفَةٌ؛ وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنْ «خَيْلٌ»", "its khabar is left out — «they had no pity» — or it is the deputy doer of an omitted verb, «no pity was found with them»; the clause can be an adjective or a hal of «horsemen»", "haberi mahzûftur: «onlarda merhamet yok»; ya da mahzûf bir fiilin nâib-i fâilidir: «onlarda merhamet bulunmaz»; cümle «hayl»in sıfatı da hâli de olabilir")),
  LA_Z(),
  R("atfr", "إِبْقَاءُ", "ibqa-hr", g=["masdar"], of=("رَأْفَةٌ", "pity", "re'fe"), n=N3(QAF_N, ZW("وَلَمْ تَرْحَمْكُمْ وَلَمْ تُبْقِ عَلَيْكُمْ", "they showed you no mercy and did not spare you", "size merhamet etmediler ve sizi esirgemediler")))])
VV(82, "And he is the lord, and the witness to the day of al-Ḥiyārān — and the trial was a trial indeed.",
  "O, efendidir ve Hıyâreyn gününe tanıktır — imtihan da gerçek bir imtihandı.",
 [HUWA_MUB("وَهُوَ", c="wi", n=ZW("يُرِيدُ عَمْرَو بْنَ هِنْدٍ، فَإِنَّهُ شَهِدَ عَنَاءَهُمْ هٰذَا", "he means ʿAmr ibn Hind, who witnessed this toil of theirs", "Amr b. Hind'i kastediyor; çünkü onların bu çilesine tanık oldu")),
  R("khb", "الرَّبُّ", "rabb", n=NT("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ — أَيِ الْمَلِكُ (الزَّوْزَنِيُّ)", "a fresh sentence — that is, the king (al-Zawzanī)", "cümle müste'nefedir — yani kral (Zevzenî)")),
  R("atfr", "وَالشَّهِيدُ", "shahid-witness", c="w", of=("الرَّبُّ", "the lord", "er-Rabb")),
  PR("عَلَى", "ala", n=N3(MT("الشَّهِيدُ", "the witness", "tanık»a"), DR("لِأَنَّهُ بِمَعْنَى الشَّاهِدِ", "for it means «witnessing»", "«şâhid» anlamında olduğu için")))],
 [R("majr", "يَوْمِ", "yawm", mud=True),
  T("الْحِيَارَيْنِ", "hiyarayn-hr", "propn", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ عَلَى صُورَةِ الْمُثَنَّى، وَهُوَ اسْمُ مَوْضِعٍ — وَجَعَلَهُ الدُّرَّةُ مَبْنِيًّا عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ، مِثْلَ «الْبَحْرَيْنِ».",
    "The second term of the idafa, in jarr by the ya in the shape of a dual; it is the name of a place — al-Durra treats it as built on kasra in the seat of jarr, like «al-Baḥrayn».", "Muzâfun ileyh, tesniye kalıbında yâ ile mecrûr; bir yer adıdır — Dürre onu «el-Bahreyn» gibi kesre üzere mebnî, mahallen mecrûr sayar."),
  R("mub", "وَالْبَلَاءُ", "bala", c="wh", n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الرَّبُّ»، وَالرَّابِطُ الْوَاوُ", "the clause is a hal of «the lord», in the seat of nasb; the waw is the link", "cümle «er-Rabb»den hâl, mahallen mansûb; bağlayıcı vâvdır")),
  R("khb", "بَلَاءُ", "bala", n=N3(QAF_N, ZW("وَالْعَنَاءُ عَنَاءٌ، أَيْ قَدْ بَلَغَ الْغَايَةَ", "and the toil was a toil — that is, it reached the utmost", "çile de çileydi — yani son dereceye vardı")))])
# ==== TAIL (lexicon, manifest, writing) — new verses go ABOVE this line ==================================================
POEM_END = 82
PLAN = [(1, 8), (9, 14), (15, 21), (22, 28), (29, 35), (36, 42), (43, 49), (50, 56), (57, 63), (64, 70), (71, 76), (77, 82)]
TITLES_ALL = [
 {"ar": "خَبَرُ الْحَارِثِ بْنِ حِلِّزَةَ", "en": "al-Ḥārith ibn Ḥilliza's Story", "tr": "Hâris b. Hillize'nin Haberi"},
 {"ar": "آذَنَتْنَا بِبَيْنِهَا أَسْمَاءُ", "en": "Asmāʾ Has Told Us She Is Leaving", "tr": "Esmâ Ayrılacağını Bildirdi"},
 {"ar": "الزَّفُوفُ", "en": "The Swift-Paced Camel", "tr": "Seğirten Deve"},
 {"ar": "الْأَرَاقِمُ", "en": "The Arāqim", "tr": "Erâkım"},
 {"ar": "عِزَّةٌ قَعْسَاءُ", "en": "A Glory Firm-Rooted", "tr": "Sarsılmaz İzzet"},
 {"ar": "أَيُّمَا خُطَّةٍ أَرَدْتُمْ", "en": "Whatever Course You Choose", "tr": "Hangi Yolu Seçerseniz"},
 {"ar": "ثُمَّ مِلْنَا عَلَى تَمِيمٍ", "en": "Then We Turned upon Tamīm", "tr": "Sonra Temîm'e Yöneldik"},
 {"ar": "وَأَمْرُ اللهِ بِلْغٌ", "en": "God's Command Reaches Its End", "tr": "Allah'ın Emri Yerini Bulur"},
 {"ar": "آيَاتٌ ثَلَاثٌ", "en": "Three Signs", "tr": "Üç Alâmet"},
 {"ar": "أَسَدٌ فِي اللِّقَاءِ", "en": "A Lion in the Encounter", "tr": "Karşılaşmada Bir Aslan"},
 {"ar": "حِلْفُ ذِي الْمَجَازِ", "en": "The Pact of Dhū l-Majāz", "tr": "Zü'l-Mecâz Antlaşması"},
 {"ar": "أَمْ عَلَيْنَا جَرَّى إِيَادٍ", "en": "Is the Crime of Iyād on Us?", "tr": "İyâd'ın Suçu Bize mi?"},
 {"ar": "وَالْبَلَاءُ بَلَاءُ", "en": "And the Trial Was a Trial", "tr": "Ve İmtihan Gerçek İmtihandı"},
]
CHAPS, VNUMS = [CH[1]], []
for _a, _b in PLAN:
    if not all(n in VERSES for n in range(_a, _b + 1)): break
    _S = [VERSES[n] for n in range(_a, _b + 1)]
    for _i, _s in enumerate(_S, 1): _s["id"] = "s%d" % _i
    CHAPS.append(_S); VNUMS.append((_a, _b))
DONE_TO = VNUMS[-1][1] if VNUMS else 0
assert len(TITLES_ALL) >= len(CHAPS), ('titles', len(TITLES_ALL), len(CHAPS))
ALL_AUTHORED = [CH[1]] + [[VERSES[n]] for n in sorted(VERSES)]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs"}
for S in ALL_AUTHORED:
    for s in S:
        for t in s["tokens"]:
            t["grammar"] = list(dict.fromkeys(t.get("grammar", [])))
            if not t["grammar"]: del t["grammar"]
            for sg2 in t.get("segments", []): sg2["form"] = re.sub("^[ً-ْ]+", "", sg2["form"])
_GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
_bad = sorted({g for S in ALL_AUTHORED for s in S for t in s["tokens"] for g in t.get("grammar", []) if g not in _GR})
assert not _bad, _bad

# ---- the lexicon: every shelf key by lemma identity; the entries in NEW_GLOSS are new (all suffixed «-hr») ------------
PREF = ["muallaqat-zuhayr", "muallaqat-imri-al-qays", "qisas-al-nabiyyin-4", "talkhis-al-miftah", "al-kafiya", "sibawayh-fi-al-basra", "ayn-jalut", "bina-baghdad"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_MO = {}
for p in PREF:
    try: _MO[p] = json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _MO[p] = {}
FORCE = {}
# staged sister packages (the other Muʿallaqāt not yet on the shelf): a lemma they already key is REUSED by its key
_SP_STORIES = pathlib.Path("/tmp/claude-0/-home-user-Gallagher-s-Index-with-Python/612c64cf-e6b9-547d-9c53-f32b7b6377b6/scratchpad/stories")
for _root in (OUT_ROOT, _SP_STORIES):
    if not _root.exists() or _root.resolve() == (ROOT / "content/samples").resolve(): continue
    for _d in sorted(_root.iterdir()):
        if _d.name in _G or _d.name == SLUG or not (_d / "glossary.json").exists(): continue
        _G[_d.name] = json.loads((_d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        try: _MO[_d.name] = json.loads((_d / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
        except FileNotFoundError: _MO[_d.name] = {}
        PREF.append(_d.name)
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k, lemma):
    for p in PREF:
        if k in _MO[p] and _G[p].get(k, {}).get("lemma") == lemma: return _MO[p][k]
    return None
# ---- the lexicon: shelf (and staged sister) keys by lemma identity; NEW_GLOSS holds the new keys (all suffixed «-hr») ----
_sg1 = _sg.sound1
def N(lemma, root, en, tr, plural=None, pos="noun"):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": 6}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
def P(lemma, en, tr): return {"lemma": lemma, "pos": "propn", "gloss": {"en": en, "tr": tr}, "level": 6}
def VB(lemma, root, en, tr, form=None):
    e = {"lemma": lemma, "pos": "verb", "gloss": {"en": en, "tr": tr}, "level": 6, "root": root}
    if form: e["form"] = form
    return e
def SAMAI(v):
    v = dict(v); v["samai"] = True; return v
HOLLOW_N = "أَجْوَفُ: تُحْذَفُ عَيْنُهُ عِنْدَ السُّكُونِ — "
def F5(v, masdar, fail, note=None):
    return _sg.derived(_sg.B5, _sg.W5, "َ", v, v, v, masdar, fail, note=note)
def F8(v, core, masdar, fail, note=None):
    return _sg.derived(_sg.B8, _sg.W8, "َ", v, core, "اِ" + core, masdar, fail, note=note)   # the amr on the muḍāriʿ's stem: اِفْتَعِلْ
def F10(v, core, masdar, fail, note=None):
    return _sg.derived(_sg.B10, _sg.W10, "َ", v, core, "اِ" + core, masdar, fail, note=note)   # اِسْتَفْعِلْ
def F3(v, core, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    return _sg.derived(_sg.B3, _sg.W3, "ُ", v, core, core, masdar, fail, maful, pmz, pmd, note)
def F2(v, core, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    return _sg.derived(_sg.B2, _sg.W2, "ُ", v, core, core, masdar, fail, maful, pmz, pmd, note)
def F4(v, core, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    return _sg.derived(_sg.B4, _sg.W4, "ُ", v, core, amr, masdar, fail, maful, pmz, pmd, note)
def F4D(a, b, masdar, fail, note, maful=None, pmz=None, pmd=None):
    """a doubled Form IV verb: أَجَدَّ يُجِدُّ"""
    return _sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, masdar, fail, _sg.mazi14("أَ" + a + "َ" + b + "ّ", "أَ" + a + "ْ" + b + "َ" + b), _sg.mudari14("ُ", a + "ِ" + b + "ّ", a + "ْ" + b + "ِ" + b),
        ["أَ" + a + "ِ" + b + "َّ", "أَ" + a + "ِ" + b + "َّا", "أَ" + a + "ِ" + b + "ُّوا", "أَ" + a + "ِ" + b + "ِّي", "أَ" + a + "ِ" + b + "َّا", "أَ" + a + "ْ" + b + "ِ" + b + "ْنَ"],
        "يُ" + a + "ِ" + b + "َّ", "يُ" + a + "ِ" + b + "َّ", "تُ" + a + "ِ" + b + "َّ", maful=maful, pmz=pmz, pmd=pmd, note=note)
def CLONE(src, lemma, pairs, note=None):
    """a new paradigm cut from a shelf verb of the same build: every root letter in `pairs` replaced"""
    v = json.loads(json.dumps(find_verb(src, lemma)))
    assert v, src
    def _r(x):
        if isinstance(x, list): return [_r(y) for y in x]
        if not isinstance(x, str): return x
        for a, b in pairs: x = x.replace(a, b)
        return x
    v = {k: _r(x) for k, x in v.items() if k != "note"}
    if note: v["note"] = note
    return v
def DBL_D(f, l, masdar, fail, note=None, maful=None, pmz=None, pmd=None):
    """a doubled Form-I verb of bab ḍaraba: خَفَّ يَخِفُّ"""
    return _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", masdar, fail, _sg.mazi14(f + "َ" + l + "ّ", f + "َ" + l + "َ" + l), _sg.mudari14("َ", f + "ِ" + l + "ّ", f + "ْ" + l + "ِ" + l),
        [f + "ِ" + l + "َّ", f + "ِ" + l + "َّا", f + "ِ" + l + "ُّوا", f + "ِ" + l + "ِّي", f + "ِ" + l + "َّا", "اِ" + f + "ْ" + l + "ِ" + l + "ْنَ"], "يَ" + f + "ِ" + l + "َّ", "يَ" + f + "ِ" + l + "َّ", "تَ" + f + "ِ" + l + "َّ",
        maful=maful, pmz=pmz, pmd=pmd, note=note or ("مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَ" + f + "ِ" + l + "َّ، وَيَجُوزُ الْفَكُّ: لَمْ يَ" + f + "ْ" + l + "ِ" + l + "ْ."))
def DBL_N(f, l, masdar, fail, note=None, maful=None, pmz=None, pmd=None):
    """a doubled Form-I verb of bab naṣara: شَدَّ يَشُدُّ"""
    return _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", masdar, fail, _sg.mazi14(f + "َ" + l + "ّ", f + "َ" + l + "َ" + l), _sg.mudari14("َ", f + "ُ" + l + "ّ", f + "ْ" + l + "ُ" + l),
        [f + "ُ" + l + "َّ", f + "ُ" + l + "َّا", f + "ُ" + l + "ُّوا", f + "ُ" + l + "ِّي", f + "ُ" + l + "َّا", "اُ" + f + "ْ" + l + "ُ" + l + "ْنَ"], "يَ" + f + "ُ" + l + "َّ", "يَ" + f + "ُ" + l + "َّ", "تَ" + f + "ُ" + l + "َّ",
        maful=maful, pmz=pmz, pmd=pmd, note=note or ("مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَ" + f + "ُ" + l + "َّ، وَيَجُوزُ الْفَكُّ: لَمْ يَ" + f + "ْ" + l + "ُ" + l + "ْ."))
NEW_GLOSS, NEW_VERBS, TAILOR = {}, {}, {}
DIV, FLAGS = [], []
MUDAWWAR = []   # verses whose print splits a word between the hemistichs: «•» goes before that word
# ---- ch1 (the khabar) ----
def CLONE_B(src, lemma, pairs, **over):
    """CLONE, keeping the source's bab / wazn text (a root letter may also sit in the bab's model word) and overriding cells"""
    v = CLONE(src, lemma, pairs); s = find_verb(src, lemma)
    v["bab"], v["wazn"] = s["bab"], s["wazn"]
    v.update(over)
    return v
# ---- ch1 (the khabar) + v1 ----
TAILOR.update({
 "bakr": ("Bakr — here Bakr ibn Wāʾil, the great tribe of Rabīʿa to which Yashkur belongs", "Bekir — burada Yeşkür'ün bağlı olduğu büyük Rebîa kabilesi Bekir b. Vâil"),
 "harith-alam": ("al-Ḥārith — a man's name: here al-Ḥārith ibn Ḥilliza al-Yashkurī, the poet", "el-Hâris — erkek adı: burada şair Hâris b. Hillize el-Yeşkürî"),
 "amr-name": ("ʿAmr — a man's name, written with a silent waw: here ʿAmr ibn Hind, king of al-Ḥīra", "Amr — erkek adı, okunmayan bir vâv ile yazılır: burada Hîre kralı Amr b. Hind"),
 "hind": ("Hind — a woman's name: here the mother of ʿAmr ibn Hind, king of al-Ḥīra, who is named after her", "Hind — kadın adı: burada Hîre kralı Amr b. Hind'in annesi; oğlu onun adıyla anılır"),
 "taghlib-amr": ("Taghlib — the tribe of Taghlib ibn Wāʾil, kin and rival of Bakr; a diptote", "Tağlib — Bekir'in akrabası ve rakibi Tağlib b. Vâil kabilesi; gayr-i munsarif"),
 "abras": ("a leper — one who has baras, white patches on the skin (fem. بَرْصَاء; a diptote)", "alacalı, baraslı — derisinde beyaz lekeler olan (müen. بَرْصَاء; gayr-i munsarif)"),
})
NEW_GLOSS.update({
 "wail-hr": P("وَائِل", "Wāʾil — Wāʾil ibn Qāsiṭ, forefather of both Bakr and Taghlib", "Vâil — hem Bekir'in hem Tağlib'in atası Vâil b. Kâsıt"),
 "asma-hr": P("أَسْمَاء", "Asmāʾ — a woman's name (a diptote): the beloved of the ode's opening", "Esmâ — kadın adı (gayr-i munsarif): kasidenin girişindeki sevgili"),
 "thawi-hr": N("ثَاوٍ", "ث و ي", "one who stays, who abides in a place (ism fāʿil of ثَوَى; الثَّاوِي — a manqūṣ)", "bir yerde kalan, ikamet eden (ثَوَى'den ism-i fâil; الثَّاوِي — menkûs)"),
 "thawa-hr": N("ثَوَاء", "ث و ي", "staying, abiding in a place (masdar of ثَوَى يَثْوِي; also ثُوِيّ)", "bir yerde kalma, ikamet (ثَوَى يَثْوِي'nin masdarı; ثُوِيّ da denir)"),
 "malla-hr": VB("مَلَّ", "م ل ل", "to weary of, to be tired of (مَلَّ يَمَلُّ مَلَلًا; مَلَّ مِنْهُ)", "usanmak, bıkmak (مَلَّ يَمَلُّ مَلَلًا; مَلَّ مِنْهُ)", form="I"),
 "irtajala-hr": VB("اِرْتَجَلَ", "ر ج ل", "to improvise, to speak (verse or a speech) off-hand, unprepared (Form VIII)", "irticâl etmek, (şiir ya da hitabeyi) hazırlıksız söylemek (VIII. bâb)", form="VIII"),
 "sijf-hr": N("سِجْف", "س ج ف", "a curtain, a hanging screen (سِجْف and سَجْف; pl. سُجُوف)", "perde, asılı örtü (سِجْف ve سَجْف; ç. سُجُوف)"),
 "baras-hr": N("بَرَص", "ب ر ص", "baras, leprosy — white patches on the skin", "baras, alacalık — derideki beyaz lekeler"),
 "istihsan-hr": N("اِسْتِحْسَان", "ح س ن", "finding a thing good, admiring it (masdar of Form X اِسْتَحْسَنَ)", "bir şeyi güzel bulma, beğenme (X. bâb اِسْتَحْسَنَ'nin masdarı)"),
 "mutawakki-hr": N("مُتَوَكِّئ", "و ك أ", "leaning (on a staff) — ism fāʿil of تَوَكَّأَ (Form V)", "(bir asâya) dayanan — تَوَكَّأَ'nın (V. bâb) ism-i fâili"),
 "anaza-hr": N("عَنَزَة", "ع ن ز", "a short spear, a staff about half a spear long with a spike, leaned on (the editor: «بفتح النون»)", "kısa mızrak; ucunda demir bulunan, mızrağın yarısı boyunda, dayanılan asâ (muhakkik: «nûnun fethasıyla»)"),
 "irtazza-hr": VB("اِرْتَزَّ", "ر ز ز", "to drive in and stay fixed (as a knife in a wall); اِرْتَزَّ فِي جَسَدِهِ — it stuck fast in his body (Form VIII)", "saplanıp kalmak (duvara saplanan bıçak gibi); اِرْتَزَّ فِي جَسَدِهِ — bedenine saplandı (VIII. bâb)", form="VIII"),
})
NEW_VERBS.update({
 "malla-hr": CLONE_B("massa", "مَسَّ", [("س", "ل")], masdar="مَلَل", ismFail="مَالّ"),
 "irtajala-hr": F8("اِرْتَجَل", "رْتَجِل", "اِرْتِجَال", "مُرْتَجِل"),
 "irtazza-hr": CLONE_B("irtadda", "اِرْتَدَّ", [("د", "ز")]),
})
FLAGS += [
 (0, "«السِّجْفِ» فِي خَبَرِ ابْنِ قُتَيْبَةَ: كُسِرَتِ السِّينُ، وَيُقَالُ «السَّجْفُ» بِالْفَتْحِ أَيْضًا، وَالطَّبْعَةُ لَمْ تَضْبِطْهَا", "«السِّجْفِ» in Ibn Qutayba's khabar: given with kasra on the sin; السَّجْف with fatha is also said, and the edition does not vowel it", "İbn Kuteybe haberindeki «السِّجْفِ»: sîn kesreli verildi; fethalı «السَّجْف» de denir, baskı harekelememiştir"),
]
# ---- ch2 (vv. 1–8) ----
TAILOR.update({
 "ahd": ("a time; a covenant; (here, al-Zawzanī) a meeting — عَهِدَ يَعْهَدُ", "zaman; ahit; (burada, Zevzenî) buluşma — عَهِدَ يَعْهَدُ"),
 "unuq": ("neck (pl. أَعْنَاق); أَعْنَاقُ فِتَاقٍ — the heights of Mount Fitāq (al-Durra)", "boyun (ç. أَعْنَاق); أَعْنَاقُ فِتَاقٍ — Fitâk dağının dorukları (Dürre)"),
 "rawda": ("a meadow, a garden of herbage (pl. رِيَاض); رِيَاضُ الْقَطَا — a place: «the meadows of the sand-grouse»", "çayır, otlu bahçe (ç. رِيَاض); رِيَاضُ الْقَطَا — bir yer: «katâ kuşlarının çayırları»"),
 "wadi-valley": ("a valley, a watercourse (manqūṣ; pl. أَوْدِيَة)", "vadi, sel yatağı (menkûs; ç. أَوْدِيَة)"),
 "alwa": ("أَلْوَى بِالشَّيْءِ: to signal with a thing, to beckon with it (al-Zawzanī); also to carry it off (Form IV)", "أَلْوَى بِالشَّيْءِ: bir şeyle işaret etmek (Zevzenî); onu alıp götürmek (IV. bâb)"),
 "alya": ("high ground, a raised tract (a mamdūd; al-Zawzanī: «الْبُقْعَةُ الْعَالِيَةُ»)", "yüksek yer, yüksek arazi (memdûd; Zevzenî: «yüksek yer»)"),
 "ud": ("a piece of wood, a stick; (al-Durra) aloes-wood burnt for its scent", "odun, çubuk; (Dürre) tütsü olarak yakılan öd ağacı"),
 "akhir-last": ("last, latter; أَخِيرًا — at the last, at the end (here: at his last meeting with her — al-Durra)", "son, sonraki; أَخِيرًا — en sonunda (burada: onunla son buluşmasında — Dürre)"),
 "khazaza-amr": ("Khazāzā (also خَزَاز) — a mountain, a famous battle-ground of the Arabs; a diptote", "Hazâzâ (ve Hazâz) — Arapların meşhur bir savaş yeri olan dağ; gayr-i munsarif"),
})
NEW_GLOSS.update({
 "shamma-hr": P("شَمَّاء", "Shammāʾ — a well-known hill (al-Durra); بُرْقَةُ شَمَّاءَ, a place (a diptote)", "Şemmâ — bilinen bir tepe (Dürre); بُرْقَةُ شَمَّاءَ bir yer (gayr-i munsarif)"),
 "adna-hr": N("أَدْنَى", "د ن و", "nearer, nearest (elative of دَنَا «to be near»; fem. دُنْيَا)", "daha yakın, en yakın (دَنَا'dan ism-i tafdîl; müen. دُنْيَا)"),
 "khalsa-hr": P("الْخَلْصَاء", "al-Khalṣāʾ — a place, the nearest of Asmāʾ's dwellings", "el-Halsâ — bir yer; Esmâ'nın yurtlarının en yakını"),
 "muhayya-hr": P("الْمُحَيَّاة", "al-Muḥayyāh — a tract of land (al-Durra)", "el-Muhayyâ — bir arazi (Dürre)"),
 "sifah-hr": P("الصِّفَاح", "al-Ṣifāḥ — a place: hills lying together (sing. صَفْحَة — al-Durra)", "es-Sifâh — bir yer: bir arada duran tepeler (tek. صَفْحَة — Dürre)"),
 "fitaq-hr": P("فِتَاق", "Fitāq — a mountain (al-Durra)", "Fitâk — bir dağ (Dürre)"),
 "adhib-hr": P("عَاذِب", "ʿĀdhib — a valley (al-Durra)", "Âzib — bir vadi (Dürre)"),
 "wafa-place-hr": P("الْوَفَاء", "al-Wafāʾ — a tract of land (al-Durra)", "el-Vefâ — bir arazi (Dürre)"),
 "qata-hr": N("قَطًا", "ق ط و", "sand-grouse (a collective; one is قَطَاة) — a bird like the dove", "katâ kuşu (cins ismi; tekili قَطَاة) — güvercine benzer bir kuş"),
 "shurbub-hr": P("الشُّرْبُب", "al-Shurbub — a mountain (with fatḥa or ḍamma on the first bāʾ — al-Durra)", "eş-Şurbub — bir dağ (ilk bâ fethalı ya da dammeli — Dürre)"),
 "shubatan-hr": P("الشُّعْبَتَانِ", "al-Shuʿbatān — «the two prongs»: a hillock with two jutting horns (al-Durra)", "eş-Şu'betân — «iki çatal»: iki çıkıntılı boynuzu olan tepecik (Dürre)"),
 "abla-hr": P("الْأَبْلَاء", "al-Ablāʾ — a well (al-Durra)", "el-Eblâ — bir kuyu (Dürre)"),
 "ahida-hr": VB("عَهِدَ", "ع ه د", "to know, to meet (someone, in a place) — عَهِدَ يَعْهَدُ", "(birini bir yerde) tanımak, görmek — عَهِدَ يَعْهَدُ", form="I"),
 "dalh-hr": N("دَلْه", "د ل ه", "loss of one's wits, bewilderment (also دَلَه — al-Zawzanī)", "aklın gitmesi, şaşkınlık (دَلَه de denir — Zevzenî)"),
 "ahara-hr": VB("أَحَارَ", "ح و ر", "to give back, to return (a thing) — Form IV of حَارَ يَحُورُ «to return» (al-Zawzanī: «الْإِحَارَةُ: الرَّدُّ»)", "geri vermek, iade etmek — حَارَ يَحُورُ'un («dönmek») IV. bâbı (Zevzenî: «ihâre: geri vermek»)", form="IV"),
 "tanawwara-hr": VB("تَنَوَّرَ", "ن و ر", "to gaze at a fire from afar (Form V; al-Zawzanī: «التَّنَوُّرُ: النَّظَرُ إِلَى النَّارِ»)", "uzaktan bir ateşe bakmak (V. bâb; Zevzenî: «tenevvür: ateşe bakmak»)", form="V"),
 "sila-hr": N("صِلَاء", "ص ل ي", "warming oneself at a fire, being reached by its heat (masdar of صَلِيَ بِالنَّارِ; also صِلًى)", "ateşte ısınma, sıcaklığına ulaşma (صَلِيَ بِالنَّارِ'ın masdarı; صِلًى de denir)"),
 "aqiq-hr": P("الْعَقِيق", "al-ʿAqīq — a valley outside Medina (al-Durra)", "el-Akîk — Medine'nin dışında bir vadi (Dürre)"),
 "shakhsan-hr": P("شَخْصَانِ", "Shakhṣān — a hillock with two prongs, a dual in form (al-Durra)", "Şahsân — iki çatallı bir tepecik; şekilce tesniye (Dürre)"),
 "diya-hr": N("ضِيَاء", "ض و أ", "light, brightness (said of dawn or of a fire)", "ışık, aydınlık (fecir ya da ateş için)"),
})
NEW_VERBS.update({
 "ahida-hr": _sg1("samia", "عَهِد", "عْهَد", "اِعْهَد", "عَهْد", "عَاهِد", "مَعْهُود", "عُهِدَ", "يُعْهَدُ"),
 "ahara-hr": _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَحَار", "أَحَر", "حِير", "حِر", "أَحِر", "أَحِر", "إِحَارَة", "مُحِير", note="أَجْوَفُ: يُحِيرُ ← لَمْ يُحِرْ."),
 "tanawwara-hr": F5("تَنَوَّر", "تَنَوُّر", "مُتَنَوِّر"),
})
MUDAWWAR += [2, 3, 4, 5, 6, 8]
DIV += [
 (2, "الْبَيْتُ ٢ «دِيَارَهَا» ← «دِيَارِهَا» بِالْجَرِّ مُضَافًا إِلَيْهِ، وَالشَّاهِدَانِ: الدُّرَّةُ «دِيَارِهَا: مُضَافٌ إِلَيْهِ مَجْرُورٌ»، وَشَرْحُ الزَّوْزَنِيِّ «الَّتِي هِيَ أَقْرَبُ دِيَارِهَا»", "v. 2 «دِيَارَهَا» → «دِيَارِهَا» in jarr, the second term of the idafa — witnesses: al-Durra («in jarr, annexed to») and al-Zawzanī's own «the nearest of her dwellings»", "2. beyit «دِيَارَهَا» → muzâfun ileyh olarak mecrûr «دِيَارِهَا» — şahitler: Dürre ve Zevzenî'nin kendi şerhi"),
 (6, "الْبَيْتُ ٦ «وَبَعَيْنَيْكَ» ← «وَبِعَيْنَيْكَ» بِكَسْرِ بَاءِ الْجَرِّ، وَالشَّاهِدُ الدُّرَّةُ «بِعَيْنَيْكَ: جَارٌّ وَمَجْرُورٌ»", "v. 6 «وَبَعَيْنَيْكَ» → «وَبِعَيْنَيْكَ» with kasra on the jarr ba — witness: al-Durra («a jarr phrase»)", "6. beyit «وَبَعَيْنَيْكَ» → cer bâsı kesreli «وَبِعَيْنَيْكَ» — şahit: Dürre («câr-mecrûr»)"),
]
FLAGS += [
 (3, "الْبَيْتُ ٣ «فَالْمُحَيَّاةُ»: لَمْ تَضْبِطِ الطَّبْعَةُ الْحَاءَ، فَفُتِحَتْ، وَالْوَزْنُ لَا يَفْصِلُ بَيْنَ الْفَتْحِ وَالْكَسْرِ", "v. 3 «فَالْمُحَيَّاةُ»: the edition leaves the ḥa bare; fatha given, and the metre cannot choose between fatha and kasra", "3. beyit «فَالْمُحَيَّاةُ»: baskı hâ'yı harekelememiş; fetha verildi, vezin fetha ile kesre arasında karar veremez"),
]
# ---- ch3 (vv. 9–14) ----
TAILOR.update({
 "anasa": ("آنَسَ: to perceive, to catch sight or sound of (Form IV); also to put at ease", "آنَسَ: sezmek, görmek ya da duymak (IV. bâb); ayrıca alıştırmak, ünsiyet ettirmek"),
 "asr": ("an age; (here, al-Zawzanī) the late afternoon, the evening — «الْعَصْرُ: الْعَشِيُّ»", "çağ; (burada, Zevzenî) ikindi vakti, akşamüstü"),
 "lb-raj": ("a return; (here) the camel's bringing back of her legs, her stepping", "dönüş; (burada) devenin ayaklarını geri çekmesi, adımı"),
 "lb-khaffa": ("to be light; to hasten off — خَفَّ بِهِ: (speed) swept him off lightly", "hafif olmak; hızla gitmek — خَفَّ بِهِ: (hız) onu hafifçe alıp götürdü"),
 "ama-blind": ("blind (أَعْمَى, fem. عَمْيَاء — a diptote)", "kör (أَعْمَى, müen. عَمْيَاء — gayr-i munsarif)"),
})
NEW_GLOSS.update({
 "thawiyy-hr": N("ثَوِيّ", "ث و ي", "one who stays, a stay-at-home (= ثَاوٍ — al-Zawzanī)", "yerinde kalan, ikamet eden (= ثَاوٍ — Zevzenî)"),
 "zafuf-hr": N("زَفُوف", "ز ف ف", "swift-paced (an intensive of زَافّ; said first of the ostrich's gait, then borrowed for the camel)", "seğirten, hızlı yürüyen (زَافّ'ın mübalağası; önce deve kuşunun yürüyüşü için söylenir, sonra deveye istiâre edilir)", pos="adj"),
 "hiqla-hr": N("هِقْلَة", "ه ق ل", "a female ostrich (the male is هِقْل)", "dişi deve kuşu (erkeği هِقْل)"),
 "ral-hr": N("رَأْل", "ر أ ل", "a young ostrich (pl. رِئَال)", "deve kuşu yavrusu (ç. رِئَال)", plural="رِئَال"),
 "dawwiyy-hr": N("دَوِّيّ", "د و و", "of the waste — belonging to الدَّوّ, the waterless desert (fem. دَوِّيَّة)", "çöle ait — susuz çöl «ed-devv»e mensup (müen. دَوِّيَّة)", pos="adj"),
 "saqfa-hr": N("أَسْقَف", "س ق ف", "tall and stooping (fem. سَقْفَاء, a diptote; السَّقَف — height with a stoop)", "uzun ve eğik (müen. سَقْفَاء, gayr-i munsarif; السَّقَف — eğiklikle beraber uzunluk)", pos="adj"),
 "nabaa-hr": N("نَبْأَة", "ن ب أ", "a faint sound one hears or imagines", "duyulan ya da duyulur gibi olan gizli ses"),
 "imsa-hr": N("إِمْسَاء", "م س و", "the coming on of evening, entering upon evening (masdar of أَمْسَى)", "akşamın girmesi, akşama ulaşma (أَمْسَى'nin masdarı)"),
 "manin-hr": N("مَنِين", "م ن ن", "fine dust", "ince toz"),
 "ihba-hr": N("إِهْبَاء", "ه ب و", "stirring up dust (masdar of أَهْبَى; هَبَاء — motes of dust, pl. أَهْبَاء)", "toz kaldırma (أَهْبَى'nin masdarı; هَبَاء — toz zerresi, ç. أَهْبَاء)"),
 "tiraq-hr": N("طِرَاق", "ط ر ق", "a sole-piece — the layers of the camel's sole that wear off (al-Zawzanī)", "taban parçası — devenin aşınıp düşen taban katmanları (Zevzenî)"),
 "saqit-hr": N("سَاقِط", "س ق ط", "fallen, dropped (ism fāʿil of سَقَطَ; fem. pl. سَاقِطَات)", "düşmüş (سَقَطَ'nin ism-i fâili; müen. ç. سَاقِطَات)", pos="adj"),
 "talahha-hr": VB("تَلَهَّى", "ل ه و", "to amuse oneself, to make sport (with) — تَلَهَّى بِهِ (Form V)", "eğlenmek, oyalanmak — تَلَهَّى بِهِ (V. bâb)", form="V"),
})
NEW_VERBS.update({
 "talahha-hr": CLONE_B("tajalla", "تَجَلَّى", [("ل", "\0"), ("ج", "ل"), ("\0", "ه")], masdar="تَلَهٍّ (التَّلَهِّي)", ismFail="مُتَلَهٍّ (الْمُتَلَهِّي)"),
})
MUDAWWAR += [10, 11, 12]
# ---- ch4 (vv. 15–21) ----
TAILOR.update({
 "ana-mean": ("to mean, to intend; عُنِيَ بِالشَّيْءِ يُعْنَى (passive): to be concerned, troubled with a thing (al-Zawzanī)", "kastetmek; عُنِيَ بِالشَّيْءِ يُعْنَى (meçhul): bir şeyle meşgul olmak, uğraşmak (Zevzenî)"),
 "saa-bad": ("to be bad; سَاءَهُ يَسُوءُهُ: to grieve someone (al-Zawzanī: «سُؤْتُ الرَّجُلَ: أَحْزَنْتُهُ»); نُسَاءُ — we are grieved", "kötü olmak; سَاءَهُ يَسُوءُهُ: birini üzmek (Zevzenî); نُسَاءُ — üzülürüz"),
 "khala-amr": ("emptiness, being free (of a thing); (here) being clear of guilt", "boşluk, (bir şeyden) arî olma; (burada) suçtan temiz olma"),
 "ayr": ("an ass; in al-Ḥārith's verse explained (al-Zawzanī) as the lord (Kulayb), the wild ass, the tent-peg, a mote, or a mountain", "eşek; Hâris'in beytinde (Zevzenî) efendi (Küleyb), yaban eşeği, kazık, göz çöpü ya da bir dağ diye açıklanır"),
 "wala": ("walāʾ — clientage, the tie of patron and client; أَنَّا الْوَلَاءُ — that we bear (the crimes of) their clientage", "velâ — mevlâlık bağı; أَنَّا الْوَلَاءُ — onların velâsını (suçlarını) bizim taşıdığımız"),
 "naba-tidings": ("tidings, news (pl. أَنْبَاء)", "haber (ç. أَنْبَاء)"),
})
NEW_GLOSS.update({
 "haditha-hr": N("حَادِثَة", "ح د ث", "an event, a happening (pl. حَوَادِث)", "olay, hâdise (ç. حَوَادِث)", plural="حَوَادِث"),
 "arqam-hr": P("الْأَرَاقِم", "al-Arāqim — clans of Taghlib, so called because a woman likened their fathers' eyes to vipers' (أَرْقَم: a male viper — al-Zawzanī)", "el-Erâkım — Tağlib boyları; bir kadın atalarının gözlerini erkek yılanınkine benzettiği için (أَرْقَم: erkek yılan — Zevzenî)"),
 "ihfa-hr": N("إِحْفَاء", "ح ف و", "insistence, pressing hard (masdar of أَحْفَى — al-Zawzanī: «الْإِلْحَاحُ»)", "ısrar, üstelemek (أَحْفَى'nin masdarı — Zevzenî)"),
 "khaliyy-hr": N("خَلِيّ", "خ ل و", "free (of a thing); (here) innocent, clear of guilt (al-Zawzanī)", "(bir şeyden) arî; (burada) suçsuz (Zevzenî)", pos="adj"),
 "muwalin-hr": N("مُوَالٍ", "و ل ي", "a client, an ally (ism fāʿil of وَالَى; الْمُوَالِي — a manqūṣ)", "mevlâ, müttefik (وَالَى'nin ism-i fâili; الْمُوَالِي — menkûs)"),
 "ajmaa-hr": VB("أَجْمَعَ", "ج م ع", "أَجْمَعَ الْأَمْرَ: to resolve upon a matter, to settle one's purpose (Form IV)", "أَجْمَعَ الْأَمْرَ: bir işe karar vermek, azmetmek (IV. bâb)", form="IV"),
 "dawda-hr": N("ضَوْضَاء", "ض و ض", "din, clamour, shouting (al-Zawzanī)", "gürültü, patırtı, bağırış (Zevzenî)"),
 "munadin-hr": N("مُنَادٍ", "ن د و", "a caller, one who calls out (ism fāʿil of نَادَى; الْمُنَادِي — a manqūṣ)", "çağıran, seslenen (نَادَى'nin ism-i fâili; الْمُنَادِي — menkûs)"),
 "tashal-hr": N("تَصْهَال", "ص ه ل", "neighing (= صَهِيل; تَفْعَال is only a masdar — al-Zawzanī)", "kişneme (= صَهِيل; «tef'âl» yalnız masdardır — Zevzenî)"),
 "khilal-hr": N("خِلَال", "خ ل ل", "amid, among, in the midst of (an adverb)", "arasında, ortasında (zarf)"),
 "ruga-hr": N("رُغَاء", "ر غ و", "the grumbling cry of camels", "devenin böğürmesi"),
 "muraqqish-hr": N("مُرَقِّش", "ر ق ش", "one who embroiders talk — a carrier of slander, a tale-bearer (the editor: «مُبَلِّغُ النَّمِيمَةِ»)", "sözü süsleyen — laf taşıyan, koğucu (muhakkik: «nemîme ileten»)"),
})
NEW_VERBS.update({
 "ajmaa-hr": F4("أَجْمَع", "جْمِع", "أَجْمِع", "إِجْمَاع", "مُجْمِع", "مُجْمَع", "أُجْمِعَ", "يُجْمَعُ"),
})
MUDAWWAR += [15, 16, 17, 18, 20]
# ---- ch5 (vv. 22–28) ----
TAILOR.update({
 "bayyada": ("to whiten; بَيَّضَ الْعَيْنَ — to blind (whitening the eye is a kināya for blinding — al-Zawzanī) (Form II)", "ağartmak; بَيَّضَ الْعَيْنَ — kör etmek (gözü ağartmak körlükten kinayedir — Zevzenî) (II. bâb)"),
 "izza": ("might, glory, proud honour", "kudret, izzet, şeref"),
 "asamm": ("solid, hard; deaf (fem. صَمَّاء — hard, severe, of a disaster: al-Zawzanī «الصَّمَّاءُ: الشَّدِيدَةُ»); in ṣarf, a name of the doubled verb", "sert, katı; sağır (müen. صَمَّاء — çetin, şiddetli, felaket için: Zevzenî); sarfta muzâaf fiilin bir adı"),
 "muyid-tf": ("a dire calamity (al-Zawzanī: «الدَّاهِيَةُ الْعَظِيمَةُ», from أَيْد / آد, strength)", "büyük felaket (Zevzenî: «büyük belâ»; kuvvet anlamındaki أَيْد / آد'dan)"),
 "jawn-amr": ("black; also white — a word of opposite senses (pl. جُون); here black (al-Zawzanī)", "siyah; beyaz da — zıt anlamlı kelime (ç. جُون); burada siyah (Zevzenî)"),
 "malik-king": ("king — here ʿAmr ibn Hind (al-Zawzanī: «هُوَ مَلِكٌ عَادِلٌ»)", "kral — burada Amr b. Hind (Zevzenî: «âdil bir kraldır»)"),
})
NEW_GLOSS.update({
 "ghara-hr": N("غَرَاة", "غ ر و", "goading on, inciting (a noun meaning إِغْرَاء — al-Zawzanī)", "kışkırtma (إِغْرَاء anlamında isim — Zevzenî)"),
 "washa-hr": VB("وَشَى", "و ش ي", "to slander, to inform against someone (وَشَى بِهِ إِلَى …; وَشَى يَشِي وَشْيًا)", "gammazlamak, birini (birine) jurnallemek (وَشَى بِهِ إِلَى …; وَشَى يَشِي)", form="I"),
 "shanaa-hr": N("شَنَاءَة", "ش ن أ", "hatred (al-Zawzanī: «الْبُغْضُ»)", "kin, buğz (Zevzenî)"),
 "nama-hr": VB("نَمَى", "ن م ي", "to raise, to lift up (نَمَى يَنْمِي; تَنْمِينَا: it raises us — al-Zawzanī)", "yükseltmek (نَمَى يَنْمِي; تَنْمِينَا: bizi yükseltir — Zevzenî)", form="I"),
 "qasa-hr": N("أَقْعَس", "ق ع س", "firm, unyielding (fem. قَعْسَاء, a diptote — عِزَّةٌ قَعْسَاءُ: a glory firm and lasting, al-Zawzanī)", "sarsılmaz, boyun eğmez (müen. قَعْسَاء, gayr-i munsarif — عِزَّةٌ قَعْسَاءُ: sabit ve kalıcı izzet, Zevzenî)", pos="adj"),
 "taghayyuz-hr": N("تَغَيُّظ", "غ ي ظ", "rage, fury shown (masdar of Form V تَغَيَّظَ)", "öfke, hiddet gösterme (V. bâb تَغَيَّظَ'nin masdarı)"),
 "iba-hr": N("إِبَاء", "أ ب ي", "proud refusal, disdain (masdar of أَبَى)", "onurlu reddediş, kabul etmeyiş (أَبَى'nin masdarı)"),
 "manun-hr": N("مَنُون", "م ن ن", "Fate, time; death (al-Zawzanī: «الدَّهْرُ»)", "zaman, kader; ölüm (Zevzenî: «dehr»)"),
 "radaa-throw-hr": VB("رَدَى", "ر د ي", "to hurl, to throw (رَدَى يَرْدِي رَدْيًا — al-Zawzanī: «الرَّدْيُ: الرَّمْيُ»)", "atmak, fırlatmak (رَدَى يَرْدِي — Zevzenî)", form="I"),
 "aran-mountain-hr": N("أَرْعَن", "ر ع ن", "(a mountain) with a jutting nose (رَعْن — al-Zawzanī); a diptote", "çıkıntılı burnu (رَعْن) olan (dağ) (Zevzenî); gayr-i munsarif", pos="adj"),
 "injaba-hr": VB("اِنْجَابَ", "ج و ب", "to be cleared away, to part (of cloud) — Form VII (al-Zawzanī: «الِانْجِيَابُ: الِانْكِشَافُ وَالِانْشِقَاقُ»)", "açılmak, yarılmak (bulut için) — VII. bâb (Zevzenî)", form="VII"),
 "ama-cloud-hr": N("عَمَاء", "ع م ي", "cloud (al-Zawzanī: «الْعَمَاءُ: السَّحَابُ»)", "bulut (Zevzenî)"),
 "mukfahirr-hr": N("مُكْفَهِرّ", "ك ف ه ر", "frowning, grim; (of a mountain) massive, piled up (ism fāʿil of اِكْفَهَرَّ)", "kaşları çatık, asık; (dağ için) üst üste yığılmış (اِكْفَهَرَّ'nin ism-i fâili)", pos="adj"),
 "rata-hr": VB("رَتَا", "ر ت و", "to loosen, slacken; also to tighten — a word of opposite senses (رَتَا يَرْتُو; here «loosen» — al-Zawzanī)", "gevşetmek; sıkmak da — zıt anlamlı (رَتَا يَرْتُو; burada «gevşetmek» — Zevzenî)", form="I"),
 "iramiyy-hr": N("إِرَمِيّ", "أ ر م", "of Iram (the forefather of ʿĀd) — of ancient lineage and nobility (al-Zawzanī)", "İrem'e mensup (Âd'ın atası) — köklü soy ve şeref sahibi (Zevzenî)", pos="adj"),
 "jala-hr": VB("جَالَ", "ج و ل", "to wheel, to range about (horses in battle) — جَالَ يَجُولُ", "dolaşmak, savaşta at koşturmak — جَالَ يَجُولُ", form="I"),
 "ijla-hr": N("إِجْلَاء", "ج ل و", "driving (people) out of their land (masdar of أَجْلَى)", "(halkı) yurdundan sürme (أَجْلَى'nin masdarı)"),
 "thana-hr": N("ثَنَاء", "ث ن ي", "praise", "övgü, sena"),
})
NEW_VERBS.update({
 "washa-hr": CLONE_B("waqa", "وَقَى", [("ق", "ش")], masdar="وَشْي", ismFail="وَاشٍ (الْوَاشِي)"),
 "nama-hr": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "نَمَ", "نْم", "i", "اِنْم", "نَمْي", "نَامٍ"),
 "radaa-throw-hr": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "رَدَ", "رْد", "i", "اِرْد", "رَدْي", "رَادٍ"),
 "injaba-hr": _sg.derived_hollow(_sg.B7, _sg.W7, "َ", "اِنْجَاب", "اِنْجَب", "نْجَاب", "نْجَب", "اِنْجَب", "اِنْجَب", "اِنْجِيَاب", "مُنْجَاب"),
 "rata-hr": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "رَتَ", "رْت", "u", "اُرْت", "رَتْو", "رَاتٍ"),
 "jala-hr": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "جَال", "جُل", "جُول", "جُل", "جُول", "جُل", "جَوَلَان", "جَائِل", note=HOLLOW_N + "يَجُولُ ← لَمْ يَجُلْ."),
})
MUDAWWAR += [23, 24, 25, 26, 27, 28]
DIV += [
 (26, "الْبَيْتُ ٢٦ «مُؤَيدٌ» ← «مُؤْيِدٌ» بِسُكُونِ الْهَمْزَةِ وَكَسْرِ الْيَاءِ، وَالشَّاهِدُ الْوَزْنُ (لَا يَسْتَقِيمُ الْخَفِيفُ بِغَيْرِهِ)، وَاشْتِقَاقُ الزَّوْزَنِيِّ «مِنَ الْأَيْدِ وَالْآدِ»", "v. 26 «مُؤَيدٌ» → «مُؤْيِدٌ» with a quiescent hamza and kasra on the ya — witnesses: the metre (the khafīf does not scan otherwise) and al-Zawzanī's derivation «from أَيْد and آد»", "26. beyit «مُؤَيدٌ» → hemzesi sâkin, yâsı kesreli «مُؤْيِدٌ» — şahitler: vezin (hafîf başka türlü düzgün olmaz) ve Zevzenî'nin «eyd ve âd'dan» iştikakı"),
 (27, "الْبَيْتُ ٢٧ «لِخَصْمِهِا» ← «لِخَصْمِهَا» بِفَتْحِ الْهَاءِ، وَالشَّاهِدُ الدُّرَّةُ «لِخَصْمِهَا … وَهَا: ضَمِيرٌ مُتَّصِلٌ»", "v. 27 «لِخَصْمِهِا» → «لِخَصْمِهَا» with fatha on the ha — witness: al-Durra («and هَا is an attached pronoun»)", "27. beyit «لِخَصْمِهِا» → hâsı fethalı «لِخَصْمِهَا» — şahit: Dürre («hâ bitişik zamirdir»)"),
]
FLAGS += [
 (27, "الْبَيْتُ ٢٧ «وَتَأْبَى لِخَصْمِهَا الْإِجْلَاءُ»: أُعْرِبَ «الْإِجْلَاءُ» مَفْعُولًا بِهِ عَلَى شَرْحِ الزَّوْزَنِيِّ، فَضَمَّتُهُ حَرَكَةُ الرَّوِيِّ عَلَى النَّصْبِ (إِصْرَافٌ)، وَرِوَايَةُ الدُّرَّةِ «فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ» تَرْفَعُهُ فَاعِلًا", "v. 27 «وَتَأْبَى لِخَصْمِهَا الْإِجْلَاءُ»: «the driving-out» is parsed as the object after al-Zawzanī's gloss, so its damma is the rawī's vowel over a nasb (iṣrāf); al-Durra's text «فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ» has it in raf' as a doer", "27. beyit «وَتَأْبَى لِخَصْمِهَا الْإِجْلَاءُ»: «el-iclâ» Zevzenî'nin şerhine göre mef'ûl olarak i'râb edildi; dammesi nasb üzerindeki revî harekesidir (isrâf); Dürre'nin rivayeti «فَآبَتْ لِخَصْمِهَا الْأَجْلَاءُ» onu fâil olarak merfû kılar"),
]
# ---- ch6 (vv. 29–35) ----
TAILOR.update({
 "mala-chiefs": ("the chiefs, the notables (pl. أَمْلَاء — bodies of nobles, «for they fill hearts and eyes with majesty» — al-Zawzanī)", "ileri gelenler, eşraf (ç. أَمْلَاء — «kalpleri ve gözleri heybetle doldurdukları için» — Zevzenî)"),
 "naqasha": ("to carve, to engrave; to probe a thing to the bottom (al-Zawzanī: «النَّقْشُ: الِاسْتِقْصَاءُ»); to draw out a thorn", "oymak, nakşetmek; bir işi sonuna kadar araştırmak (Zevzenî: «nakş: istiksâ»); diken çıkarmak"),
 "naqsh": ("carving; probing to the bottom (al-Zawzanī)", "oyma; sonuna kadar araştırma (Zevzenî)"),
 "ibra": ("release, discharge; (here) curing, restoring to health — masdar of أَبْرَأَ (al-Zawzanī: «كَنَّى … بِالْبُرْءِ عَنْ بَرَاءَةِ السَّاحَةِ»)", "ibrâ, aklama; (burada) iyileştirme — أَبْرَأَ'nın masdarı (Zevzenî: şifa ile suçsuzluğu kinaye etti)"),
 "naha": ("to forbid; to stop, to bring to a halt (نَهَاهَا: it stopped them)", "nehyetmek, yasaklamak; durdurmak (نَهَاهَا: onları durdurdu)"),
 "hayy": ("living, alive (pl. أَحْيَاء)", "diri, canlı (ç. أَحْيَاء)"),
})
NEW_GLOSS.update({
 "nabasha-hr": VB("نَبَشَ", "ن ب ش", "to dig up, to exhume; to search out (نَبَشَ يَنْبُشُ نَبْشًا)", "eşelemek, kazıp çıkarmak; araştırmak (نَبَشَ يَنْبُشُ)", form="I"),
 "milha-hr": P("مِلْحَة", "Milḥa — a place (a diptote)", "Milha — bir yer (gayr-i munsarif)"),
 "saqib-hr": P("الصَّاقِب", "al-Ṣāqib — a place", "es-Sâkib — bir yer"),
 "jashima-hr": VB("جَشِمَ", "ج ش م", "to take on (a hard thing) with effort, to undertake (جَشِمَ يَجْشَمُ)", "(zor bir işe) zahmetle girişmek, katlanmak (جَشِمَ يَجْشَمُ)", form="I"),
 "isqam-hr": N("إِسْقَام", "س ق م", "making sick, sickness (masdar of أَسْقَمَ; a kināya for guilt — al-Zawzanī)", "hasta etme, hastalık (أَسْقَمَ'nin masdarı; suçtan kinaye — Zevzenî)"),
 "aghmada-hr": VB("أَغْمَضَ", "غ م ض", "to shut (the eye), to close the lids (Form IV)", "(gözü) yummak, kapamak (IV. bâb)", form="IV"),
 "ala-height-hr": N("عَلَاء", "ع ل و", "height, eminence, the upper hand", "yücelik, üstünlük"),
 "ghiwar-hr": N("غِوَار", "غ و ر", "raiding one another (= مُغَاوَرَة — al-Zawzanī)", "karşılıklı baskın (= مُغَاوَرَة — Zevzenî)"),
 "uwa-hr": N("عُوَاء", "ع و ي", "howling (of a wolf or dog); here, by borrowing, clamour and shouting (al-Zawzanī)", "uluma (kurt, köpek); burada istiâre ile gürültü ve bağırış (Zevzenî)"),
 "saaf-hr": N("سَعَف", "س ع ف", "palm-fronds, palm branches (one is سَعَفَة)", "hurma dalları (tekili سَعَفَة)"),
 "bahrayn-hr": P("الْبَحْرَيْنِ", "al-Baḥrayn — the land on the Gulf coast (a dual in form)", "el-Bahreyn — Körfez kıyısındaki ülke (şekilce tesniye)"),
 "hisa-hr": P("الْحِسَاء", "al-Ḥisāʾ — a place (al-Zawzanī)", "el-Hisâ — bir yer (Zevzenî)"),
})
NEW_VERBS.update({
 "nabasha-hr": _sg1("nasara", "نَبَش", "نْبُش", "اُنْبُش", "نَبْش", "نَابِش", "مَنْبُوش", "نُبِشَ", "يُنْبَشُ"),
 "jashima-hr": _sg1("samia", "جَشِم", "جْشَم", "اِجْشَم", "جَشَم", "جَاشِم"),
 "aghmada-hr": F4("أَغْمَض", "غْمِض", "أَغْمِض", "إِغْمَاض", "مُغْمِض", "مُغْمَض", "أُغْمِضَ", "يُغْمَضُ"),
})
MUDAWWAR += [29, 30, 31, 32, 33, 34, 35]
DIV += [
 (29, "الْبَيْتُ ٢٩ «أَيُّمَا» ← «أَيَّمَا» بِالنَّصْبِ مَفْعُولًا بِهِ مُقَدَّمًا لِـ«أَرَدْتُمْ»، وَالشَّاهِدُ الدُّرَّةُ «اسْمُ شَرْطٍ جَازِمٌ مَفْعُولٌ بِهِ مُقَدَّمٌ لِفِعْلِ شَرْطِهِ»", "v. 29 «أَيُّمَا» → «أَيَّمَا» in nasb, the fronted object of «you wish» — witness: al-Durra («a conditional noun, the fronted object of its condition's verb»)", "29. beyit «أَيُّمَا» → «istediniz»in öne alınmış mef'ûlü olarak mansûb «أَيَّمَا» — şahit: Dürre («şart fiilinin öne alınmış mef'ûlü»)"),
 (31, "الْبَيْتُ ٣١ «يَجْشَمَهُ» ← «يَجْشَمُهُ» بِالرَّفْعِ، وَالشَّاهِدُ الدُّرَّةُ: الْفِعْلُ وَفَاعِلُهُ خَبَرُ «النَّقْشُ»، وَلَا نَاصِبَ لَهُ", "v. 31 «يَجْشَمَهُ» → «يَجْشَمُهُ» in raf' — witness: al-Durra (the verb with its doer is the khabar of «probing»; nothing puts it in nasb)", "31. beyit «يَجْشَمَهُ» → merfû «يَجْشَمُهُ» — şahit: Dürre (fiil ve fâili «en-nakş»ın haberidir; onu nasbeden yoktur)"),
 (32, "الْبَيْتُ ٣٢ «فَكَنَّا» ← «فَكُنَّا» بِضَمِّ الْكَافِ، وَالشَّاهِدُ الدُّرَّةُ «كُنَّا: فِعْلٌ مَاضٍ نَاقِصٌ»", "v. 32 «فَكَنَّا» → «فَكُنَّا» with damma on the kaf — witness: al-Durra («a defective past verb»)", "32. beyit «فَكَنَّا» → kâfı dammeli «فَكُنَّا» — şahit: Dürre («nâkıs mâzî fiil»)"),
]
# ---- ch7 (vv. 36–42) ----
TAILOR.update({
 "sahl": ("easy; (of land) level, plain (الْبَلَدُ السَّهْلُ — the open country)", "kolay; (arazi için) düz, ova (الْبَلَدُ السَّهْلُ — açık arazi)"),
 "rai": ("a shepherd, a herdsman (a manqūṣ; pl. رُعَاة and رِعَاء)", "çoban (menkûs; ç. رُعَاة ve رِعَاء)"),
 "mundhir-name": ("al-Mundhir — a man's name; here al-Mundhir, king of al-Ḥīra, father of ʿAmr ibn Hind", "el-Münzir — erkek adı; burada Hîre kralı, Amr b. Hind'in babası Münzir"),
 "ahalla": ("to make lawful; أَحَلَّهُ الْمَكَانَ — to set someone down in a place, to settle him there (Form IV)", "helal kılmak; أَحَلَّهُ الْمَكَانَ — birini bir yere kondurmak, yerleştirmek (IV. bâb)"),
 "qubba": ("a dome; a domed tent (of leather)", "kubbe; kubbeli (deri) çadır"),
 "takalif": ("burdens, hardships, the toils a thing lays on one (al-Zawzanī: «الْمَشَاقُّ وَالشَّدَائِدُ»)", "yükler, zorluklar, meşakkatler (Zevzenî: «meşakkatler ve şiddetler»)"),
})
NEW_GLOSS.update({
 "ahrama-hr": VB("أَحْرَمَ", "ح ر م", "to enter upon the sacred month (al-Zawzanī); to enter the state of iḥrām (Form IV)", "haram aya girmek (Zevzenî); ihrama girmek (IV. bâb)", form="IV"),
 "waala-hr": VB("وَاءَلَ", "و أ ل", "to flee in fear, to seek refuge (= وَأَلَ — al-Zawzanī) (Form III)", "korkup kaçmak, sığınak aramak (= وَأَلَ — Zevzenî) (III. bâb)", form="III"),
 "tawd-hr": N("طَوْد", "ط و د", "a lofty mountain", "yüksek dağ"),
 "harra-hr": N("حَرَّة", "ح ر ر", "a lava-field: ground of black stones as if burnt (the editor's note)", "harra: yanmış gibi kara taşlarla kaplı arazi (muhakkikin dipnotu)"),
 "rajla-hr": N("رَجْلَاء", "ر ج ل", "(of stony ground) rough and hard, hard to walk on (al-Zawzanī: «الْغَلِيظَةُ الشَّدِيدَةُ»; a diptote)", "(taşlık arazi için) sert, çetin, yürünmesi zor (Zevzenî; gayr-i munsarif)", pos="adj"),
 "adraa-hr": VB("أَضْرَعَ", "ض ر ع", "to humble, to bring low (Form IV; al-Zawzanī: «ذَلَّلَ وَقَهَرَ»)", "boyun eğdirmek, zelil kılmak (IV. bâb; Zevzenî)", form="IV"),
 "kifa-hr": N("كِفَاء", "ك ف أ", "an equal, a match (a masdar standing for مُكَافِئ — al-Zawzanī)", "denk, eş (مُكَافِئ yerine masdar — Zevzenî)"),
 "taghlabiyy-hr": N("تَغْلَبِيّ", "غ ل ب", "a man of Taghlib (the nisba of تَغْلِب, with fatḥa on the lām)", "Tağlibli (تَغْلِب'e nisbet, lâm fethalı)", pos="adj"),
 "matlul-hr": N("مَطْلُول", "ط ل ل", "(of blood) spilt unavenged, left unrequited (طُلَّ دَمُهُ — al-Zawzanī)", "(kan için) heder edilmiş, intikamı alınmamış (طُلَّ دَمُهُ — Zevzenî)", pos="adj"),
 "afa-hr": N("عَفَاء", "ع ف و", "effacement; the dust that covers a trace (عَلَيْهِ الْعَفَاءُ — a curse: dust be on him)", "silinip gitme; izi örten toprak (عَلَيْهِ الْعَفَاءُ — beddua: üstüne toprak)"),
 "maysun-hr": P("مَيْسُون", "Maysūn — a woman's name (a diptote)", "Meysûn — kadın adı (gayr-i munsarif)"),
 "awsa-hr": P("الْعَوْصَاء", "al-ʿAwṣāʾ — a place, the nearest of Maysūn's dwellings", "el-Avsâ — bir yer; Meysûn'un yurtlarının en yakını"),
})
NEW_VERBS.update({
 "ahrama-hr": F4("أَحْرَم", "حْرِم", "أَحْرِم", "إِحْرَام", "مُحْرِم"),
 "waala-hr": F3("وَاءَل", "وَائِل", "مُوَاءَلَة", "مُوَائِل"),
 "adraa-hr": F4("أَضْرَع", "ضْرِع", "أَضْرِع", "إِضْرَاع", "مُضْرِع", "مُضْرَع", "أُضْرِعَ", "يُضْرَعُ"),
})
MUDAWWAR += [36, 37, 39, 40, 41, 42]
DIV += [
 (40, "الْبَيْتُ ٤٠ «إِذَ» ← «إِذْ» بِالسُّكُونِ، وَالشَّاهِدُ الدُّرَّةُ «إِذْ: ظَرْفٌ … مَبْنِيٌّ عَلَى السُّكُونِ»", "v. 40 «إِذَ» → «إِذْ» with sukun — witness: al-Durra («an adverb … built on sukun»)", "40. beyit «إِذَ» → sükûnlu «إِذْ» — şahit: Dürre («sükûn üzere mebnî zarf»)"),
]
# ---- ch8 (vv. 43–49) ----
TAILOR.update({
 "hada": ("to guide; to lead, to go before (هَدَاهُمْ: he went before them — al-Zawzanī)", "doğru yolu göstermek; önlerine düşmek, yönetmek (هَدَاهُمْ: önlerine düştü — Zevzenî)"),
 "lb-shaqiqa": ("a stretch of hard ground between two tracts of sand (pl. شَقَائِق); الشَّقِيقَةُ — the place of the battle (al-Zawzanī)", "iki kum arası sert arazi (ç. شَقَائِق); الشَّقِيقَةُ — savaşın yeri (Zevzenî)"),
 "shaqi": ("wretched, damned (pl. أَشْقِيَاء)", "bedbaht, şaki (ç. أَشْقِيَاء)"),
 "aya": ("a sign; a verse of the Qurʾān; (here) a proof, a token of worth (al-Zawzanī: «دَلَائِلُ غَنَائِنَا»)", "alâmet; Kur'ân âyeti; (burada) delil, değer nişanesi (Zevzenî)"),
 "qada": ("a decree; judgement (given in someone's favour)", "kazâ, hüküm (birinin lehine verilen)"),
 "maadd-name": ("Maʿadd — Maʿadd ibn ʿAdnān, forefather of the northern Arabs; (here) the tribes descended from him", "Maadd — kuzey Araplarının atası Maadd b. Adnân; (burada) ondan gelen kabileler"),
})
NEW_GLOSS.update({
 "taawwa-hr": VB("تَأَوَّى", "أ و ي", "to gather, to flock together (Form V; al-Zawzanī: «التَّأَوِّي: التَّجَمُّعُ»)", "toplanmak, bir araya gelmek (V. bâb; Zevzenî)", form="V"),
 "qurdub-hr": N("قُرْضُوب", "ق ر ض ب", "a wicked robber, a thief (also قِرْضَاب; pl. قَرَاضِبَة — al-Zawzanī)", "kötü hırsız, haydut (قِرْضَاب da denir; ç. قَرَاضِبَة — Zevzenî)", plural="قَرَاضِبَة"),
 "liqwa-hr": N("لَقْوَة", "ل ق و", "an eagle (pl. أَلْقَاء — al-Zawzanī)", "kartal (ç. أَلْقَاء — Zevzenî)", plural="أَلْقَاء"),
 "aswadan-hr": N("الْأَسْوَدَانِ", "س و د", "«the two black things»: water and dates (al-Zawzanī)", "«iki kara»: su ve hurma (Zevzenî)"),
 "bilgh-hr": N("بِلْغ", "ب ل غ", "reaching its end, accomplishing (أَمْرُ اللهِ بِلْغٌ: God's command reaches its end — = بَالِغ, al-Zawzanī)", "yerini bulan, sonuca ulaşan (أَمْرُ اللهِ بِلْغٌ — = بَالِغ, Zevzenî)", pos="adj"),
 "ghurur-hr": N("غُرُور", "غ ر ر", "delusion, being deceived; taking by surprise (masdar of غَرَّ)", "aldanma, aldanış; gafil avlama (غَرَّ'nin masdarı)"),
 "ashra-hr": N("أَشْرَاء", "أ ش ر", "insolent, arrogant (fem.; أَشَر — insolence, al-Zawzanī; a diptote)", "şımarık, kibirli (müen.; أَشَر — şımarıklık, Zevzenî; gayr-i munsarif)", pos="adj"),
 "duhaa-hr": N("ضَحَاء", "ض ح و", "the late forenoon, a little after الضُّحَى (al-Zawzanī)", "kuşluktan biraz sonrası (Zevzenî)"),
 "shariq-hr": N("شَارِق", "ش ر ق", "shining, rising (of the sun); one coming from the east (the editor); شَارِقُ الشَّقِيقَةِ — the battle at al-Shaqīqa (al-Zawzanī)", "parlayan, doğan (güneş); doğudan gelen (muhakkik); شَارِقُ الشَّقِيقَةِ — Şakîka savaşı (Zevzenî)", pos="adj"),
 "liwa-hr": N("لِوَاء", "ل و ي", "a banner, a standard (pl. أَلْوِيَة)", "sancak, bayrak (ç. أَلْوِيَة)", plural="أَلْوِيَة"),
})
NEW_VERBS.update({
 "taawwa-hr": CLONE_B("tajalla", "تَجَلَّى", [("ج", "أ"), ("ل", "و")], masdar="تَأَوٍّ (التَّأَوِّي)", ismFail="مُتَأَوٍّ (الْمُتَأَوِّي)"),
})
MUDAWWAR += [45, 48, 49]
DIV += [
 (45, "الْبَيْتُ ٤٥ «أًمْنِيّةٌ» ← «أُمْنِيَّةٌ» بِضَمِّ الْهَمْزَةِ، وَالشَّاهِدَانِ: الدُّرَّةُ «أُمْنِيَّةٌ: فَاعِلُ سَاقَتْهُمْ»، وَشَرْحُ الزَّوْزَنِيِّ «أُمْنِيَّتُكُمْ»", "v. 45 «أًمْنِيّةٌ» → «أُمْنِيَّةٌ» with damma on the hamza — witnesses: al-Durra («the doer of drove them») and al-Zawzanī's own «your wish»", "45. beyit «أًمْنِيّةٌ» → hemzesi dammeli «أُمْنِيَّةٌ» — şahitler: Dürre ve Zevzenî'nin şerhi «umniyyetukum»"),
 (45, "الْبَيْتُ ٤٥ «أَشْرَاءٌ» ← «أَشْرَاءُ» بِلَا تَنْوِينٍ، وَالشَّاهِدَانِ: الْقَافِيَةُ (لَا تَنْوِينَ فِي سَائِرِ قَوَافِي الْقَصِيدَةِ فِي الطَّبْعَةِ)، وَأَنَّهُ عَلَى «فَعْلَاءَ» مَمْنُوعٌ مِنَ الصَّرْفِ", "v. 45 «أَشْرَاءٌ» → «أَشْرَاءُ» without tanwin — witnesses: the rhyme (no other rhyme-word of the ode is printed with tanwin) and its pattern فَعْلَاء, a diptote", "45. beyit «أَشْرَاءٌ» → tenvinsiz «أَشْرَاءُ» — şahitler: kâfiye (baskıda kasidenin başka hiçbir kâfiyesi tenvinli değildir) ve «fa'lâ'» kalıbında gayr-i munsarif oluşu"),
]
# ---- ch9 (vv. 50–56) ----
TAILOR.update({
 "qays-name-tf": ("Qays — a man's name (v. 50: Qays ibn Maʿdīkarib, of the kings of Ḥimyar — al-Zawzanī; v. 72: a people the poet disowns)", "Kays — erkek adı (50. beyit: Himyer krallarından Kays b. Ma'dîkerib — Zevzenî; 72. beyit: şairin kendinden saymadığı bir topluluk)"),
 "kabsh": ("a ram; by borrowing, a lord, the chief of a host (al-Zawzanī)", "koç; istiâre ile efendi, bir topluluğun reisi (Zevzenî)"),
 "mazada": ("a large water-skin (pl. مَزَاد — al-Zawzanī)", "büyük su tulumu (ç. مَزَاد — Zevzenî)"),
 "farisiyya": ("Persian; (here, al-Zawzanī) a Persian troop, or Persian coats of mail", "Farsça, Farsî; (burada, Zevzenî) bir Fars birliği ya da Fars zırhları"),
 "akhdar": ("green (fem. خَضْرَاء, a diptote); كَتِيبَةٌ خَضْرَاءُ — a troop dark-green with rusted iron", "yeşil (müen. خَضْرَاء, gayr-i munsarif); كَتِيبَةٌ خَضْرَاءُ — paslı demirden koyu yeşil birlik"),
 "dam": ("blood (pl. دِمَاء); مَا لَهُمْ دِمَاءُ — their blood is not avenged", "kan (ç. دِمَاء); مَا لَهُمْ دِمَاءُ — kanları aranmaz"),
})
NEW_GLOSS.update({
 "qarazi-hr": N("قَرَظِيّ", "ق ر ظ", "of the land of qaraẓ (the tanning tree) — Yemeni (al-Zawzanī)", "karaz (tabak ağacı) diyarından — Yemenli (Zevzenî)", pos="adj"),
 "abla-hill-hr": N("عَبْلَاء", "ع ب ل", "a white hill (al-Zawzanī); a diptote", "beyaz tepe (Zevzenî); gayr-i munsarif"),
 "sitit-hr": N("صَتِيت", "ص ت ت", "a host, a body of men (al-Zawzanī: «الْجَمَاعَةُ»)", "topluluk, cemaat (Zevzenî)"),
 "atika-hr": N("عَاتِكَة", "ع ت ك", "a noble woman: young, freeborn and choice (pl. عَوَاتِك — al-Zawzanī)", "soylu kadın: genç, hür ve seçkin (ç. عَوَاتِك — Zevzenî)", plural="عَوَاتِك"),
 "mubyadd-hr": N("مُبْيَضّ", "ب ي ض", "turning white, shining white (ism fāʿil of اِبْيَضَّ; fem. مُبْيَضَّة)", "beyazlaşan, bembeyaz parlayan (اِبْيَضَّ'nin ism-i fâili; müen. مُبْيَضَّة)", pos="adj"),
 "rala-hr": N("رَعْلَاء", "ر ع ل", "long and far-stretched (of a troop; al-Zawzanī); a diptote", "uzun ve uzayıp giden (birlik için; Zevzenî); gayr-i munsarif", pos="adj"),
 "khurba-hr": N("خُرْبَة", "خ ر ب", "a hole (in a water-skin — al-Zawzanī: «ثَقْبُهَا»)", "delik (tulumda — Zevzenî)"),
 "hazm-hr": N("حَزْم", "ح ز م", "rough, rugged ground — rougher than حَزْن (al-Zawzanī)", "sert, engebeli yer — «hazn»dan daha sert (Zevzenî)"),
 "thahlan-hr": P("ثَهْلَان", "Thahlān — a particular mountain (a diptote)", "Sehlân — belli bir dağ (gayr-i munsarif)"),
 "shilal-hr": N("شِلَال", "ش ل ل", "driving off in pursuit, a rout (al-Zawzanī: «الطِّرَادُ»)", "kovalayıp sürme, bozgun (Zevzenî)"),
 "damma-hr": VB("دَمَّى", "د م ي", "to bloody, to smear with blood (Form II; التَّدْمِيَةُ: اللَّطْخُ بِالدَّمِ — al-Zawzanī)", "kana bulamak (II. bâb; Zevzenî)", form="II"),
 "nasa-vein-hr": N("نَسًا", "ن س ي", "the sciatic vein in the thigh (pl. أَنْسَاء — al-Zawzanī)", "uyluktaki nesâ damarı (ç. أَنْسَاء — Zevzenî)", plural="أَنْسَاء"),
 "jabaha-hr": VB("جَبَهَ", "ج ب ه", "to repulse harshly, to beat back (جَبَهَ يَجْبَهُ جَبْهًا — al-Zawzanī: «أَعْنَفُ الرَّدْعِ»)", "şiddetle geri püskürtmek (جَبَهَ يَجْبَهُ — Zevzenî)", form="I"),
 "nahaza-hr": VB("نَهَزَ", "ن ه ز", "to move, to ply, to jerk (a bucket in a well) — نَهَزَ يَنْهَزُ (al-Zawzanī: «النَّهْزُ: التَّحْرِيكُ»)", "hareket ettirmek, (kuyuda kovayı) oynatmak — نَهَزَ يَنْهَزُ (Zevzenî)", form="I"),
 "jumma-hr": N("جُمَّة", "ج م م", "the gathered water of a well, abundant water (al-Zawzanī)", "kuyuda toplanmış bol su (Zevzenî)"),
 "tawiyy-hr": N("طَوِيّ", "ط و ي", "a well lined with stones or bricks (al-Zawzanī)", "taş ya da kerpiçle örülmüş kuyu (Zevzenî)"),
 "hain-hr": N("حَائِن", "ح ي ن", "one who courts destruction, who perishes (ism fāʿil of حَانَ يَحِينُ — al-Zawzanī)", "helake maruz kalan, helak olan (حَانَ يَحِينُ'nin ism-i fâili — Zevzenî)"),
 "hujr-hr": P("حُجْر", "Ḥujr — Ḥujr son of Umm Qaṭām, a prince of Kinda (al-Zawzanī)", "Hucr — Kinde emîrlerinden Ümmü Katâm'ın oğlu Hucr (Zevzenî)"),
})
NEW_VERBS.update({
 "damma-hr": _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "دَمَّ", "دَمّ", "i", "دَمّ", "تَدْمِيَة", "مُدَمٍّ (الْمُدَمِّي)", maful="مُدَمًّى", pmz="دُمِّيَ", pmd="يُدَمَّى"),
 "jabaha-hr": _sg1("fataha", "جَبَه", "جْبَه", "اِجْبَه", "جَبْه", "جَابِه", "مَجْبُوه", "جُبِهَ", "يُجْبَهُ"),
 "nahaza-hr": _sg1("fataha", "نَهَز", "نْهَز", "اِنْهَز", "نَهْز", "نَاهِز", "مَنْهُوز", "نُهِزَ", "يُنْهَزُ"),
})
MUDAWWAR += [51, 52, 53, 54]
DIV += [
 (53, "الْبَيْتُ ٥٣ «وَدُمّي الْأَنْسَاءِ» ← «وَدُمِّيَ الْأَنْسَاءُ» بِرَفْعِ الْأَنْسَاءِ نَائِبَ فَاعِلٍ، وَالشَّاهِدَانِ: الدُّرَّةُ «دُمِّيَ: فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، الْأَنْسَاءُ: نَائِبُ فَاعِلٍ»، وَشَرْحُ الزَّوْزَنِيِّ «وَأَدْمَيْنَا أَفْخَاذَهُمْ»", "v. 53 «وَدُمّي الْأَنْسَاءِ» → «وَدُمِّيَ الْأَنْسَاءُ», «the thighs» in raf' as deputy doer — witnesses: al-Durra («a passive past verb … the deputy doer») and al-Zawzanī's «we bloodied their thighs»", "53. beyit «وَدُمّي الْأَنْسَاءِ» → nâib-i fâil olarak merfû «وَدُمِّيَ الْأَنْسَاءُ» — şahitler: Dürre («meçhul mâzî … nâib-i fâil») ve Zevzenî'nin «uyluklarını kana buladık» şerhi"),
 (54, "الْبَيْتُ ٥٤ «وَجَبَهْنَاهُمْ» ← «وَجَبَهْنَاهُمُ» بِضَمِّ الْمِيمِ، وَالشَّاهِدُ الْوَزْنُ (وَكَذٰلِكَ طُبِعَ «رَدَدْنَاهُمُ» وَ«حَمَلْنَاهُمُ» فِي الْبَيْتَيْنِ ٥٢–٥٣)", "v. 54 «وَجَبَهْنَاهُمْ» → «وَجَبَهْنَاهُمُ» with damma on the mim — witness: the metre (as «رَدَدْنَاهُمُ» and «حَمَلْنَاهُمُ» are printed in vv. 52–53)", "54. beyit «وَجَبَهْنَاهُمْ» → mîmi dammeli «وَجَبَهْنَاهُمُ» — şahit: vezin (52–53. beyitlerde «reddednâhumu» ve «hamelnâhumu» da böyle basılmıştır)"),
]
# ---- ch10 (vv. 57–63) ----
TAILOR.update({
 "shammara": ("to roll up the sleeves, to gird oneself; (of a hard year, al-Zawzanī) to make ready (Form II)", "paçaları sıvamak, hazırlanmak; (çetin yıl için, Zevzenî) hazırlanmak (II. bâb)"),
 "ghabra-tf": ("the dusty one: the earth; (here, al-Zawzanī) a hard year, for the dust in its air (a diptote)", "tozlu olan: yeryüzü; (burada, Zevzenî) havası tozlu olduğu için çetin yıl (gayr-i munsarif)"),
 "fakka": ("to undo, to loose (a fetter); to solve", "çözmek, (bağı) açmak; halletmek"),
 "aws": ("Aws — a man's name; بَنُو الْأَوْسِ — a clan (al-Ḥārith's ode)", "Evs — erkek adı; بَنُو الْأَوْسِ — bir boy (Hâris'in kasidesi)"),
 "walla-amr": ("to turn (a thing) towards; (intransitive) to turn away, to turn one's back in flight (Form II)", "(bir şeyi) çevirmek; (geçişsiz) dönüp kaçmak, sırt çevirmek (II. bâb)"),
 "rabb": ("Lord; (of men) master, lord — رَبُّ غَسَّانَ: the king of Ghassān", "Rab; (insanlar için) efendi — رَبُّ غَسَّانَ: Gassân kralı"),
 "aqada-qawad": ("to give someone his retaliation, to deliver (a man) to be killed in requital (بِ: for the slain) — Form IV (al-Zawzanī: «أَقَدْتُهُ: أَعْطَيْتُهُ الْقَوَدَ»)", "birine kısas hakkını vermek, (birini) kısas için teslim etmek (بِ: maktul karşılığı) — IV. bâb (Zevzenî)"),
 "kala-measure": ("to measure out (grain); (here, by borrowing — al-Zawzanī) blood «measured» for retaliation", "(tahılı) ölçmek; (burada istiâre ile — Zevzenî) kısas için kanın «ölçülmesi»"),
 "walada": ("to beget, to bear; (here, al-Zawzanī) to be the forebears of — «we begot» = his mother was of us", "doğurmak; (burada, Zevzenî) atası olmak — «doğurduk» = annesi bizdendi"),
 "malik-king": ("king (pl. مُلُوك, أَمْلَاك) — here ʿAmr ibn Hind (al-Zawzanī: «هُوَ مَلِكٌ عَادِلٌ»)", "kral (ç. مُلُوك, أَمْلَاك) — burada Amr b. Hind (Zevzenî: «âdil bir kraldır»)"),
})
NEW_GLOSS.update({
 "hamus-hr": N("هَمُوس", "ه م س", "soft-treading, with a muffled footfall (of a lion — al-Zawzanī; an intensive)", "yumuşak basan, ayak sesi boğuk (aslan için — Zevzenî; mübalağa)", pos="adj"),
 "ghull-hr": N("غُلّ", "غ ل ل", "an iron collar, a shackle (pl. أَغْلَال)", "demir halka, boyunduruk (ç. أَغْلَال)"),
 "jawn-name-hr": P("الْجَوْن", "al-Jawn — a lord of the Banū l-Aws (al-Ḥārith's ode)", "el-Cevn — Benî Evs'in bir efendisi (Hâris'in kasidesi)"),
 "anud-hr": N("عَنُود", "ع ن د", "stubborn, obstinate (of a troop — al-Zawzanī: «شَدِيدَةُ الْعِنَادِ»)", "inatçı, dik başlı (birlik için — Zevzenî)", pos="adj"),
 "dafwa-hr": N("دَفْوَاء", "د ف و", "a great bulging hill (al-Zawzanī: «هَضْبَةٌ»); a diptote", "büyük, kabarık tepe (Zevzenî); gayr-i munsarif"),
 "ajaja-hr": N("عَجَاجَة", "ع ج ج", "dust (of battle) — al-Zawzanī: «الْغُبَارُ»", "(savaş) tozu — Zevzenî"),
 "ghassan-hr": P("غَسَّان", "Ghassān — the Arab kingdom on the Syrian marches (a diptote)", "Gassân — Şam sınırındaki Arap krallığı (gayr-i munsarif)"),
 "karh-hr": N("كَرْه", "ك ر ه", "compulsion, unwillingness — كَرْهًا: perforce", "zorlama, isteksizlik — كَرْهًا: zorla"),
 "salab-hr": N("سَلَب", "س ل ب", "spoil stripped from the slain: clothes, arms and horse (pl. أَسْلَاب — al-Zawzanī)", "öldürülenden soyulan ganimet: elbise, silah ve at (ç. أَسْلَاب — Zevzenî)", plural="أَسْلَاب"),
 "ghali-dear-hr": N("غَالٍ", "غ ل و", "costly, dear (pl. أَغْلَاء — a diptote)", "pahalı, değerli (ç. أَغْلَاء — gayr-i munsarif)", pos="adj"),
 "unas-name-hr": P("أُنَاس", "Unās — in أُمُّ أُنَاسٍ, the mother of ʿAmr ibn Hind's line (a diptote by rule)", "Unâs — أُمُّ أُنَاسٍ terkibinde (kural gereği gayr-i munsarif)"),
 "hiba-hr": N("حِبَاء", "ح ب و", "a gift; (here) the bride-price (al-Zawzanī: «مَهْرُهَا»)", "bağış; (burada) mehir (Zevzenî)"),
})
DIV += [
 (61, "الْبَيْتُ ٦١ «وَأَقْدْنَاهُ» ← «وَأَقَدْنَاهُ» بِفَتْحِ الْقَافِ، وَالشَّاهِدُ الْوَزْنُ (لَا يَلْتَقِي سَاكِنَانِ فِي حَشْوِ الْبَيْتِ)، وَشَرْحُ الزَّوْزَنِيِّ «أَقَدْتُهُ»", "v. 61 «وَأَقْدْنَاهُ» → «وَأَقَدْنَاهُ» with fatha on the qaf — witnesses: the metre (two quiescents cannot meet inside the line) and al-Zawzanī's «أَقَدْتُهُ»", "61. beyit «وَأَقْدْنَاهُ» → kâfı fethalı «وَأَقَدْنَاهُ» — şahitler: vezin (beyit içinde iki sâkin bir araya gelmez) ve Zevzenî'nin «ekadtuhû»su"),
 (62, "الْبَيْتُ ٦٢ «وَأَتْيْنَاهُمُ» ← «وَأَتَيْنَاهُمُ» بِفَتْحِ التَّاءِ، وَالشَّاهِدُ الْوَزْنُ، وَشَرْحُ الزَّوْزَنِيِّ «وَأَتَيْنَاهُمْ»", "v. 62 «وَأَتْيْنَاهُمُ» → «وَأَتَيْنَاهُمُ» with fatha on the ta — witnesses: the metre and al-Zawzanī's «وأتيناهم»", "62. beyit «وَأَتْيْنَاهُمُ» → tâsı fethalı «وَأَتَيْنَاهُمُ» — şahitler: vezin ve Zevzenî'nin şerhi"),
]
MUDAWWAR += [59, 60, 61, 62]
# ---- ch11 (vv. 64–70) ----
TAILOR.update({
 "hujra": ("a room, a chamber; (here) a side, a quarter (al-Zawzanī: «النَّاحِيَةُ»)", "oda; (burada) yan, taraf (Zevzenî)"),
 "hawa-desire": ("desire, caprice, whim (a maqṣūr noun; pl. أَهْوَاء)", "arzu, heves (maksûr isim; ç. أَهْوَاء)"),
 "jaza-answer": ("requital, recompense; (in grammar) the answer of a condition", "karşılık, ceza; (nahivde) şartın cevabı"),
 "ghazi": ("a raider, one who goes out on campaign (ism fāʿil of غَزَا; a manqūṣ)", "akıncı, sefere çıkan (غَزَا'nın ism-i fâili; menkûs)"),
 "daa-amr": ("a sickness, a disease (pl. أَدْوَاء); (here) the evil that follows (al-Zawzanī)", "hastalık (ç. أَدْوَاء); (burada) ardından gelen kötülük (Zevzenî)"),
})
NEW_GLOSS.update({
 "falat-hr": N("فَلَاة", "ف ل و", "a waterless desert (pl. فَلًا, and of that أَفْلَاء — al-Zawzanī)", "susuz çöl (ç. فَلًا, onun çoğulu da أَفْلَاء — Zevzenî)", plural="أَفْلَاء"),
 "taykh-hr": N("طَيْخ", "ط ي خ", "pride, arrogance (al-Zawzanī: «التَّكَبُّرُ»)", "kibir (Zevzenî)"),
 "taashi-hr": N("تَعَاشٍ", "ع ش و", "feigning blindness, pretending not to see (masdar of تَعَاشَى; التَّعَاشِي — a manqūṣ)", "körlük taslama, görmezden gelme (تَعَاشَى'nin masdarı; التَّعَاشِي — menkûs)"),
 "taasha-hr": VB("تَعَاشَى", "ع ش و", "to feign night-blindness, to pretend not to see (Form VI of affected action)", "gece körlüğü taslamak, görmezden gelmek (yapmacık bildiren VI. bâb)", form="VI"),
 "hilf-hr": N("حِلْف", "ح ل ف", "a pact, a sworn alliance", "antlaşma, yeminli ittifak"),
 "majaz-place-hr": P("الْمَجَاز", "al-Majāz — in ذُو الْمَجَازِ, the place where ʿAmr ibn Hind made peace between Bakr and Taghlib (al-Zawzanī)", "el-Mecâz — ذُو الْمَجَازِ terkibinde, Amr b. Hind'in Bekir ile Tağlib'i barıştırdığı yer (Zevzenî)"),
 "taaddi-hr": N("تَعَدٍّ", "ع د و", "transgression, aggression (masdar of تَعَدَّى; التَّعَدِّي — a manqūṣ)", "tecavüz, saldırı (تَعَدَّى'nin masdarı; التَّعَدِّي — menkûs)"),
 "naqada-hr": VB("نَقَضَ", "ن ق ض", "to undo, to break (a covenant) — نَقَضَ يَنْقُضُ", "bozmak, (ahdi) çözmek — نَقَضَ يَنْقُضُ", form="I"),
 "muhraq-hr": N("مُهْرَق", "ه ر ق", "a written sheet of polished, coated cloth — an arabicised Persian word (pl. مَهَارِق — al-Zawzanī)", "cilalanmış, sıvanmış bezden yazı sayfası — Arapçalaşmış Farsça (ç. مَهَارِق — Zevzenî)", plural="مَهَارِق"),
 "anan-hr": N("عَنَن", "ع ن ن", "cutting across, a pretext, an objection (al-Zawzanī: «الِاعْتِرَاضُ»; عَنَّ يَعِنُّ)", "araya girme, bahane, itiraz (Zevzenî; عَنَّ يَعِنُّ)"),
 "atara-hr": VB("عَتَرَ", "ع ت ر", "to slaughter the عَتِيرَة, a victim for the idols in Rajab (عَتَرَ يَعْتِرُ)", "Receb'de putlar için «atîre» kurbanı kesmek (عَتَرَ يَعْتِرُ)", form="I"),
 "rabid-hr": N("رَبِيض", "ر ب ض", "sheep lying in their folds (the editor's note)", "ağıllarında yatan koyunlar (muhakkikin dipnotu)"),
 "junah-hr": N("جُنَاح", "ج ن ح", "sin, guilt (al-Zawzanī: «الْإِثْمُ»)", "günah, suç (Zevzenî)"),
 "kinda-hr": P("كِنْدَة", "Kinda — the tribe of Kinda (a diptote)", "Kinde — Kinde kabilesi (gayr-i munsarif)"),
 "ghanima-hr": VB("غَنِمَ", "غ ن م", "to take spoil, to win booty (غَنِمَ يَغْنَمُ غُنْمًا)", "ganimet almak (غَنِمَ يَغْنَمُ)", form="I"),
})
NEW_VERBS.update({
 "taasha-hr": _sg.derived_naqis(_sg.B6, _sg.W6, "َ", "تَعَاشَ", "تَعَاش", "a", "تَعَاش", "تَعَاشٍ (التَّعَاشِي)", "مُتَعَاشٍ (الْمُتَعَاشِي)"),
 "naqada-hr": _sg1("nasara", "نَقَض", "نْقُض", "اُنْقُض", "نَقْض", "نَاقِض", "مَنْقُوض", "نُقِضَ", "يُنْقَضُ"),
 "atara-hr": _sg1("daraba", "عَتَر", "عْتِر", "اِعْتِر", "عَتْر", "عَاتِر", "مَعْتُور", "عُتِرَ", "يُعْتَرُ"),
 "ghanima-hr": _sg1("samia", "غَنِم", "غْنَم", "اِغْنَم", "غُنْم", "غَانِم", "مَغْنُوم", "غُنِمَ", "يُغْنَمُ"),
})
MUDAWWAR += [64, 66, 67, 68, 69, 70]
DIV += [
 (69, "الْبَيْتُ ٦٩ «تَعْتَرُ» ← «تُعْتَرُ» بِضَمِّ التَّاءِ مَبْنِيًّا لِلْمَجْهُولِ، وَالشَّاهِدُ الدُّرَّةُ «تُعْتَرُ: فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ … الظِّبَاءُ: نَائِبُ فَاعِلٍ»", "v. 69 «تَعْتَرُ» → passive «تُعْتَرُ» with damma on the ta — witness: al-Durra («a passive present … the gazelles: deputy doer»)", "69. beyit «تَعْتَرُ» → tâsı dammeli meçhul «تُعْتَرُ» — şahit: Dürre («meçhul muzâri… ceylanlar: nâib-i fâil»)"),
]
# ---- ch12 (vv. 71–76) ----
TAILOR.update({
 "muhammal": ("laden, loaded (ism mafʿūl of حَمَّلَ); الْمُحَمَّلُ — the laden camel", "yüklü (حَمَّلَ'nin ism-i mef'ûlü); الْمُحَمَّلُ — yüklü deve"),
 "ib": ("a burden, a load (pl. أَعْبَاء — al-Zawzanī: «الْعِبْءُ: الثِّقْلُ»)", "yük (ç. أَعْبَاء — Zevzenî)"),
 "hanifa": ("Ḥanīfa — a name; (here) the tribe of Banū Ḥanīfa (a diptote)", "Hanîfe — ad; (burada) Benî Hanîfe kabilesi (gayr-i munsarif)"),
 "muharib-name": ("Muḥārib — a name; (here) the tribe of Muḥārib", "Muhârib — ad; (burada) Muhârib kabilesi"),
 "nahb": ("plunder, spoil (pl. نِهَاب)", "yağma, ganimet (ç. نِهَاب)"),
 "bari": ("innocent, free of blame; quit of (مِنْ) — pl. بُرَآء (a diptote)", "suçsuz; (مِنْ) uzak, berî — ç. بُرَآء (gayr-i munsarif)"),
 "sadr": ("breast; the foremost part (صَدْرُ الرُّمْحِ — the spear's point — al-Zawzanī: «صَدْرُ كُلِّ شَيْءٍ: أَوَّلُهُ»)", "göğüs; ön kısım (صَدْرُ الرُّمْحِ — mızrağın ucu — Zevzenî)"),
 "qada": ("a decree; judgement; (v. 74, al-Zawzanī) death, killing — «الْقَضَاءُ: الْقَتْلُ»", "kazâ, hüküm; (74. beyit, Zevzenî) ölüm, öldürme"),
})
NEW_GLOSS.update({
 "jarra-hr": N("جَرَّى", "ج ر ر", "a crime, an offence (also جَرَاء — al-Zawzanī: «الْجِنَايَةُ»)", "suç, cinayet (جَرَاء da denir — Zevzenî)"),
 "iyad-hr": P("إِيَاد", "Iyād — an Arab tribe of Nizār", "İyâd — Nizâr'dan bir Arap kabilesi"),
 "nata-hr": VB("نَاطَ", "ن و ط", "to hang (a thing on another) — نَاطَ يَنُوطُ نَوْطًا (al-Zawzanī: «النَّوْطُ: التَّعْلِيقُ»)", "asmak — نَاطَ يَنُوطُ (Zevzenî)", form="I"),
 "jawz-hr": N("جَوْز", "ج و ز", "the middle (of a thing), the midst (pl. أَجْوَاز — al-Zawzanī)", "(bir şeyin) ortası (ç. أَجْوَاز — Zevzenî)"),
 "mudarrab-hr": P("الْمُضَرَّبُونَ", "al-Muḍarrabūn — a people the poet disowns (al-Ḥārith's ode; the print has «الْمَضَرَّبُونَ»)", "el-Muḍarrebûn — şairin kendinden saymadığı bir topluluk (Hâris'in kasidesi; baskıda «الْمَضَرَّبُونَ»)"),
 "jandal-name-hr": P("جَنْدَل", "Jandal — a people the poet disowns (al-Ḥārith's ode)", "Cendel — şairin kendinden saymadığı bir topluluk (Hâris'in kasidesi)"),
 "hadda-hr": P("الْحَدَّاء", "al-Ḥaddāʾ — a people the poet disowns (al-Ḥārith's ode)", "el-Haddâ' — şairin kendinden saymadığı bir topluluk (Hâris'in kasidesi)"),
 "janaya-hr": N("جِنَايَة", "ج ن ي", "a crime, an offence (pl. جَنَايَا)", "suç, cinayet (ç. جَنَايَا)", plural="جَنَايَا"),
 "atiq-name-hr": P("عَتِيق", "ʿAtīq — in بَنُو عَتِيقٍ, a clan", "Atîk — بَنُو عَتِيقٍ terkibinde bir boy"),
 "ghadara-hr": VB("غَدَرَ", "غ د ر", "to break faith, to betray (غَدَرَ يَغْدِرُ غَدْرًا)", "ahde vefasızlık etmek, ihanet etmek (غَدَرَ يَغْدِرُ)", form="I"),
 "mulahhab-hr": N("مُلَحَّب", "ل ح ب", "hewn, cut to pieces (ism mafʿūl of لَحَّبَ — al-Zawzanī: «التَّلْحِيبُ: التَّقْطِيعُ»)", "parçalanmış (لَحَّبَ'nin ism-i mef'ûlü — Zevzenî)", pos="adj"),
 "asamma-v-hr": VB("أَصَمَّ", "ص م م", "to deafen (Form IV, doubled: أَصَمَّ يُصِمُّ)", "sağır etmek (IV. bâb, muzâaf: أَصَمَّ يُصِمُّ)", form="IV"),
 "huda-hr": N("حُدَاء", "ح د و", "the camel-driver's song (masdar of حَدَا يَحْدُو)", "deve sürücüsünün türküsü (حَدَا يَحْدُو'nun masdarı)"),
 "jammaa-hr": VB("جَمَّعَ", "ج م ع", "to gather together, to amass (Form II)", "bir araya toplamak, yığmak (II. bâb)", form="II"),
})
NEW_VERBS.update({
 "nata-hr": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "نَاط", "نُط", "نُوط", "نُط", "نُوط", "نُط", "نَوْط", "نَائِط", "مَنُوط", "نِيطَ", "يُنَاطُ", HOLLOW_N + "يَنُوطُ ← لَمْ يَنُطْ."),
 "ghadara-hr": _sg1("daraba", "غَدَر", "غْدِر", "اِغْدِر", "غَدْر", "غَادِر", "مَغْدُور", "غُدِرَ", "يُغْدَرُ"),
 "asamma-v-hr": F4D("ص", "م", "إِصْمَام", "مُصِمّ", "مُضَاعَفٌ: يُصِمُّ ← لَمْ يُصِمَّ، وَيَجُوزُ الْفَكُّ: لَمْ يُصْمِمْ."),
 "jammaa-hr": F2("جَمَّع", "جَمِّع", "تَجْمِيع", "مُجَمِّع", "مُجَمَّع", "جُمِّعَ", "يُجَمَّعُ"),
})
MUDAWWAR += [71, 72, 74]
DIV += [
 (72, "الْبَيْتُ ٧٢ «الْمَضَرَّبُونَ» ← «الْمُضَرَّبُونَ» بِضَمِّ الْمِيمِ، وَالشَّاهِدُ الْبِنَاءُ: لَيْسَ فِي الْعَرَبِيَّةِ «مَفَعَّلٌ»، وَإِنَّمَا هُوَ «مُفَعَّلٌ» اسْمُ مَفْعُولِ «ضَرَّبَ»، وَنَصُّ الدُّرَّةِ «الْمُضَرَّبُونَ» بِلَا ضَبْطٍ", "v. 72 «الْمَضَرَّبُونَ» → «الْمُضَرَّبُونَ» with damma on the mim — witness: the word-pattern (Arabic has no مَفَعَّل; this is مُفَعَّل, the passive participle of ضَرَّبَ), with al-Durra's unvowelled «المضربون»", "72. beyit «الْمَضَرَّبُونَ» → mîmi dammeli «الْمُضَرَّبُونَ» — şahit: kalıp (Arapçada «mef'al» yoktur; bu, «darrabe»nin ism-i mef'ûlü «muf'al»dır), Dürre'nin harekesiz metniyle"),
 (76, "الْبَيْتُ ٧٦ «مِنَ مُحَارِبٍ» ← «مِنْ مُحَارِبٍ» بِسُكُونِ النُّونِ، وَالشَّاهِدَانِ: الْوَزْنُ، وَالدُّرَّةُ «مِنْ مُحَارِبٍ: جَارٌّ وَمَجْرُورٌ»", "v. 76 «مِنَ مُحَارِبٍ» → «مِنْ مُحَارِبٍ» with a quiescent nun — witnesses: the metre and al-Durra («a jarr phrase»)", "76. beyit «مِنَ مُحَارِبٍ» → nûnu sâkin «مِنْ مُحَارِبٍ» — şahitler: vezin ve Dürre"),
]
FLAGS += [
 (72, "الْبَيْتُ ٧٢ «الْمُضَرَّبُونَ»: اسْمُ قَوْمٍ لَمْ يَشْرَحْهُ الزَّوْزَنِيُّ وَلَا الدُّرَّةُ، وَضَمَّةُ مِيمِهِ مِنَ الْمُحَرِّرِ عَلَى الْبِنَاءِ", "v. 72 «الْمُضَرَّبُونَ»: the name of a people that neither al-Zawzanī nor al-Durra explains; the damma on its mim is the editor's, by the word-pattern", "72. beyit «الْمُضَرَّبُونَ»: Zevzenî'nin de Dürre'nin de açıklamadığı bir topluluk adı; mîmindeki damme kalıba göre editöre aittir"),
]
# ---- ch13 (vv. 77–82) ----
TAILOR.update({
 "nada-ant": ("dew, moisture; open-handedness (pl. أَنْدَاء); (v. 77) the least share of guilt (al-Zawzanī)", "çiy, nem; cömertlik (ç. أَنْدَاء); (77. beyit) suçtan en küçük pay (Zevzenî)"),
 "faa": ("to return, to go back (فَاءَ يَفِيءُ — al-Zawzanī: «الْفَيْءُ: الرُّجُوعُ»)", "dönmek (فَاءَ يَفِيءُ — Zevzenî)"),
 "bala": ("affliction, trial; valour shown in trial (الْبَلَاءُ بَلَاءٌ — the trial reached the utmost, al-Zawzanī)", "belâ, imtihan; imtihanda gösterilen yiğitlik (الْبَلَاءُ بَلَاءٌ — imtihan son dereceye vardı, Zevzenî)"),
 "rabb": ("Lord; (of men) master, lord, king — رَبُّ غَسَّانَ (v. 61); (v. 82) ʿAmr ibn Hind (al-Zawzanī: «الْمَلِكُ»)", "Rab; (insanlar için) efendi, kral — رَبُّ غَسَّانَ (61. beyit); (82. beyit) Amr b. Hind (Zevzenî: «kral»)"),
 "qudaa-amr": ("Quḍāʿa — a great confederation of Arab tribes (a diptote)", "Kudâa — büyük bir Arap kabileleri birliği (gayr-i munsarif)"),
})
NEW_GLOSS.update({
 "jana-v-hr": VB("جَنَى", "ج ن ي", "to commit (a crime) — جَنَى يَجْنِي جِنَايَةً", "(suç) işlemek — جَنَى يَجْنِي", form="I"),
 "istarjaa-hr": VB("اِسْتَرْجَعَ", "ر ج ع", "to seek to get back, to reclaim (Form X)", "geri almaya çalışmak, geri istemek (X. bâb)", form="X"),
 "shama-hr": N("شَامَة", "ش ي م", "a mole, a spot; (here) a ewe with a spot — «ذَاتُ شَامَةٍ» (al-Zawzanī)", "ben, benek; (burada) benekli koyun — «zâtu şâme» (Zevzenî)"),
 "azhar-hr": N("أَزْهَر", "ز ه ر", "bright, white (fem. زَهْرَاء — a white ewe, al-Zawzanī: «أَيْ بَيْضَاءُ»; a diptote)", "parlak, beyaz (müen. زَهْرَاء — beyaz koyun, Zevzenî; gayr-i munsarif)", pos="adj"),
 "razah-hr": P("رَزَاح", "Razāḥ — in بَنُو رَزَاحٍ, a clan", "Rezâh — بَنُو رَزَاحٍ terkibinde bir boy"),
 "barqa-hr": P("بَرْقَاء", "Barqāʾ — in بَرْقَاءُ نِطَاعٍ, a place (a diptote)", "Berkâ' — بَرْقَاءُ نِطَاعٍ terkibinde bir yer (gayr-i munsarif)"),
 "nitaa-hr": P("نِطَاع", "Niṭāʿ — a place, in بَرْقَاءُ نِطَاعٍ", "Nitâ' — بَرْقَاءُ نِطَاعٍ terkibinde bir yer"),
 "qasima-hr": N("قَاصِمَة", "ق ص م", "a breaker; قَاصِمَةُ الظَّهْرِ — a back-breaking disaster (al-Zawzanī: «دَاهِيَةٌ قَصَمَتْ ظُهُورَهُمْ»)", "kıran; قَاصِمَةُ الظَّهْرِ — bel kıran felaket (Zevzenî)"),
 "barada-hr": VB("بَرَدَ", "ب ر د", "to cool (a thing), to slake (thirst) — بَرَدَ يَبْرُدُ (v. 80 prints «يَبْرَدُ»)", "serinletmek, (susuzluğu) gidermek — بَرَدَ يَبْرُدُ (80. beyit «يَبْرَدُ» basılmıştır)", form="I"),
 "ghalil-hr": N("غَلِيل", "غ ل ل", "the burning of thirst; (here, al-Zawzanī) the burning of rancour", "susuzluk yanması; (burada, Zevzenî) kin yanması"),
 "ghallaq-hr": P("الْغَلَّاق", "al-Ghallāq — a name in al-Ḥārith's ode (horsemen came «with al-Ghallāq»)", "el-Gallâk — Hâris'in kasidesinde bir ad («Gallâk ile» atlılar geldi)"),
 "rafa-hr": N("رَأْفَة", "ر أ ف", "pity, tender mercy", "şefkat, merhamet"),
 "ibqa-hr": N("إِبْقَاء", "ب ق ي", "sparing, leaving alive (masdar of أَبْقَى)", "esirgeme, sağ bırakma (أَبْقَى'nin masdarı)"),
 "hiyarayn-hr": P("الْحِيَارَيْنِ", "al-Ḥiyārān — a place, the day of the battle there (a dual in form)", "el-Hıyâreyn — bir yer, oradaki savaş günü (şekilce tesniye)"),
})
NEW_VERBS.update({
 "jana-v-hr": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "جَنَ", "جْن", "i", "اِجْن", "جِنَايَة", "جَانٍ"),
 "istarjaa-hr": F10("اِسْتَرْجَع", "سْتَرْجِع", "اِسْتِرْجَاع", "مُسْتَرْجِع"),
 "barada-hr": _sg1("nasara", "بَرَد", "بْرُد", "اُبْرُد", "بَرْد", "بَارِد", "مَبْرُود", "بُرِدَ", "يُبْرَدُ"),
})
MUDAWWAR += [77, 78, 79, 80, 81, 82]
DIV += [
 (77, "الْبَيْتُ ٧٧ «جَرحى» ← «جَرَّى»، وَالشَّوَاهِدُ: نَصُّ الدُّرَّةِ «جَرَى قُضَاعَةَ»، وَالْكَلِمَةُ نَفْسُهَا فِي الْبَيْتَيْنِ ٧١ وَ٧٦ «جَرَّى»، وَشَرْحُ الزَّوْزَنِيِّ «أَمْ عَلَيْنَا جِنَايَةُ قُضَاعَةَ»", "v. 77 «جَرحى» → «جَرَّى» — witnesses: al-Durra's text «جرى قضاعة», the same word printed «جَرَّى» in vv. 71 and 76, and al-Zawzanī's «or is the crime of Quḍāʿa on us»", "77. beyit «جَرحى» → «جَرَّى» — şahitler: Dürre'nin metni, 71. ve 76. beyitlerde aynı kelimenin «cerrâ» basılışı ve Zevzenî'nin «yoksa Kudâa'nın suçu bize mi» şerhi"),
]
FLAGS += [
 (80, "الْبَيْتُ ٨٠ «يَبْرَدُ»: أُبْقِيَ عَلَى ضَبْطِ الطَّبْعَةِ بِفَتْحِ الرَّاءِ وَلَا شَاهِدَ ثَانٍ، وَالْمَعْرُوفُ فِي «بَرَدَ» الْمُتَعَدِّي «يَبْرُدُ»", "v. 80 «يَبْرَدُ»: kept as the edition vowels it, with fatha on the ra, for want of a second witness; the usual present of the transitive بَرَدَ is يَبْرُدُ", "80. beyit «يَبْرَدُ»: ikinci şahit bulunmadığından baskının harekesiyle (râ fethalı) bırakıldı; geçişli «bered»in bilinen muzârii «yebrudu»dur"),
]
DIV += [
 (81, "الْبَيْتُ ٨١ «إِبْقَاُء» ← «إِبْقَاءُ»: وُضِعَتِ الضَّمَّةُ عَلَى الْهَمْزَةِ، وَالشَّاهِدُ الْقَافِيَةُ (رَوِيُّهَا هَمْزَةٌ مَضْمُومَةٌ)", "v. 81 «إِبْقَاُء» → «إِبْقَاءُ»: the damma set on the hamza — witness: the rhyme (its rawī is a hamza with damma)", "81. beyit «إِبْقَاُء» → «إِبْقَاءُ»: damme hemzeye konmuştur — şahit: kâfiye (revîsi dammeli hemzedir)"),
]
_lid = lambda x: unicodedata.normalize("NFC", (x or "").replace("ـ", "")).strip()
_STAGED = {}
for d in OUT_ROOT.iterdir() if OUT_ROOT.exists() else []:
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
for k, e in NEW_GLOSS.items():
    hit = [p for p in PREF if k in _G[p] and _lid(_G[p][k].get("lemma")) != _lid(e["lemma"])]   # a shelf or sister package may hold the key with the SAME lemma (so the script re-runs after this package lands)
    assert not hit, (k, hit)
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
assert not missing, missing
unused_new = sorted(set(NEW_GLOSS) - used_all)
assert not unused_new, unused_new
GLOSS = {}
for k in sorted(used):
    e = json.loads(json.dumps(NEW_GLOSS.get(k) or find_gloss(k)))
    if k in TAILOR: e["gloss"] = {"en": TAILOR[k][0], "tr": TAILOR[k][1]}
    GLOSS[k] = e
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = NEW_VERBS.get(k) or find_verb(k, e["lemma"])
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par
assert all(k.endswith("-hr") for k in NEW_GLOSS), [k for k in NEW_GLOSS if not k.endswith("-hr")]

# ---- the manifest ------------------------------------------------------------------------------------------------------
_AD = lambda n: str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
TITLES = TITLES_ALL[:len(CHAPS)]
WHOLE = DONE_TO == POEM_END
# DIV: (verse, ar, en, tr) — a departure from the edition's print, with its witness.  FLAGS: (verse, ar, en, tr) — a vowel left
# for the scholar (editorial, and neither the metre nor the commentary settles it).
_div = sorted(d for d in DIV if d[0] <= DONE_TO); _flg = sorted(f for f in FLAGS if f[0] <= DONE_TO)
_ch_ar = "؛ ".join("الْفَصْلُ %s: %s–%s" % (_AD(i + 2), _AD(a), _AD(b)) for i, (a, b) in enumerate(VNUMS))
_ch_en = "; ".join("chapter %d: vv. %d–%d" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_ch_tr = "; ".join("%d. bölüm: %d–%d. beyitler" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_sofar_ar = "وَهِيَ هُنَا كَامِلَةٌ لَمْ يُتْرَكْ مِنْهَا بَيْتٌ وَلَمْ يُقَدَّمْ وَلَمْ يُؤَخَّرْ" if WHOLE else "وَالْمَنْشُورُ مِنْهَا هُنَا الْأَبْيَاتُ ١–%s مُتَّصِلَةً لَمْ يُتْرَكْ مِنْ وَسَطِهَا بَيْتٌ، وَبَقِيَّتُهَا (%s–٨٢) لَمْ تُنْشَرْ هُنَا بَعْدُ" % (_AD(DONE_TO), _AD(DONE_TO + 1))
_sofar_en = "given here WHOLE, none left out and none moved" if WHOLE else "of which this package gives vv. 1–%d as one unbroken run, with no verse skipped inside it; the rest of the ode (vv. %d–82) is not yet published here" % (DONE_TO, DONE_TO + 1)
_sofar_tr = "burada TAMAMI verilmiştir; hiçbiri atlanmamış, yeri değiştirilmemiştir" if WHOLE else "bu pakette 1–%d. beyitler, aradan hiçbir beyit atlanmadan, kesintisiz verilmiştir; kasidenin devamı (%d–82. beyitler) henüz yayımlanmamıştır" % (DONE_TO, DONE_TO + 1)
_mud = sorted(m for m in MUDAWWAR if m <= DONE_TO)
_m_ar = ("وَفِي الْأَبْيَاتِ الْمُدَوَّرَةِ — الَّتِي قَسَمَتِ الطَّبْعَةُ كَلِمَةً مِنْهَا بَيْنَ الشَّطْرَيْنِ، وَهِيَ: " + "، ".join(_AD(m) for m in _mud) + " — وُضِعَتْ «•» قَبْلَ تِلْكَ الْكَلِمَةِ، لِأَنَّ الْكَلِمَةَ لَا تُقْسَمُ. ") if _mud else ""
_m_en = ("In the run-on (mudawwar) verses, where the edition splits a word between the hemistichs — vv. " + ", ".join(str(m) for m in _mud) + " — «•» stands before that word, since a word is not divided. ") if _mud else ""
_m_tr = ("Baskının bir kelimeyi iki mısra arasında böldüğü müdevver beyitlerde — " + ", ".join(str(m) for m in _mud) + ". beyitler — «•» o kelimeden önce konmuştur, çünkü kelime bölünmez. ") if _mud else ""
_d_ar = ("وَخُولِفَ الْمَطْبُوعُ فِي هٰذِهِ الْمَوَاضِعِ بِشَاهِدٍ: " + "؛ ".join("(%s) " % _AD(i + 1) + d[1] for i, d in enumerate(_div)) + ". ") if _div else ""
_d_en = ("The edition's print is departed from in these places, each against a witness: " + "; ".join("(%d) " % (i + 1) + d[2] for i, d in enumerate(_div)) + ". ") if _div else ""
_d_tr = ("Matbû metinden şu yerlerde, her biri bir şahide dayanılarak ayrılınmıştır: " + "; ".join("(%d) " % (i + 1) + d[3] for i, d in enumerate(_div)) + ". ") if _div else ""
ATTR_AR = ("نَصٌّ مَنْقُولٌ بِلَفْظِهِ. الْفَصْلُ الْأَوَّلُ خَبَرُ الْحَارِثِ بْنِ حِلِّزَةَ فِي «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةِ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ٢٣٧٨٥)، ج ١ ص ١٩٣: الْفِقْرَةُ ٣١٩ كُلُّهَا، أَوَّلُهَا «هُوَ مِنْ بَنِي يَشْكُرَ» وَآخِرُهَا «وَهُوَ لَا يَشْعُرُ»، لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ؛ وَمَا بَعْدَهَا (ابْنُهُ مَذْعُورٌ، وَقَوْلُ الْأَصْمَعِيِّ إِنَّهُ أَقْوَى فِي قَصِيدَتِهِ، وَمَا يُتَمَثَّلُ بِهِ مِنْ شِعْرِهِ — الْفِقَرُ ٣٢٠–٣٢٢) غَيْرُ مَنْقُولٍ هُنَا. "
           "وَالْفُصُولُ بَعْدَهُ مُعَلَّقَتُهُ — وَهِيَ مِنَ الْبَحْرِ الْخَفِيفِ، وَرَوِيُّهَا هَمْزَةٌ مَضْمُومَةٌ قَبْلَهَا أَلِفٌ رِدْفًا — بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) وَتَرْتِيبِهِ وَعَدِّهِ فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةِ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م (الْكِتَابُ ١١٢٥٣)، ص ٢٦٩–٢٨٦، اثْنَانِ وَثَمَانُونَ بَيْتًا؛ " + _sofar_ar + ". " + _ch_ar + ". وَالْبَيْتُ جُمْلَةٌ وَاحِدَةٌ، وَعَلَامَةُ «•» آخِرُ صَدْرِهِ. " + _m_ar + "الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ عَلَى حَالِهِ بِإِمْلَاءِ هٰذَا الرَّفِّ، وَمَا تَرَكَتْهُ عَارِيًا — وَهُوَ حَرَكَاتُ خَبَرِ ابْنِ قُتَيْبَةَ كُلُّهَا سِوَى الشَّدَّاتِ (وَفَتْحَةُ نُونِ «عَنَزَةٍ» مِنْ حَاشِيَةِ الْمُحَقِّقِ)، وَكَثِيرٌ مِنْ حُرُوفِ الْأَبْيَاتِ وَأَوَاخِرِ كَلِمَاتِهَا — ضَبَطَهُ الْمُحَرِّرُ بِمَا يُوجِبُهُ الْإِعْرَابُ وَالْوَزْنُ وَالشَّرْحُ. " + _d_ar
           + ("وَتُرِكَ لِنَظَرِ الْعَالِمِ: " + "؛ ".join(f[1] for f in _flg) + ". " if _flg else "")
           + "إِعْرَابُ كُلِّ كَلِمَةٍ بِعِبَارَةِ هٰذَا الرَّفِّ، وَقَدْ رُوجِعَ عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ: إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهَ الدُّرَّة (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م؛ الْكِتَابُ ١٥١٠١٧، ج ١ ص ٤٥٥ – ج ٢ ص ٤) — وَهُوَ يَرْوِي الْقَصِيدَةَ سِتَّةً وَثَمَانِينَ بَيْتًا بِتَرْتِيبٍ غَيْرِ تَرْتِيبِ الزَّوْزَنِيِّ — وَمَا خَالَفَ فِيهِ رِوَايَةَ الزَّوْزَنِيِّ مَذْكُورٌ عَلَى كَلِمَتِهِ، وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ: مَا سَمَّاهُ أَوْ وَصَفَهُ الزَّوْزَنِيُّ أَوِ الدُّرَّةُ نُسِبَ إِلَيْهِ، وَمَا كَانَ بِحَدِّ التَّلْخِيصِ وَحْدَهُ قِيلَ فِيهِ: «عَلَى حَدِّ التَّلْخِيصِ». وَالتَّرْجَمَةُ مَعْنَى الْبَيْتِ عَلَى شَرْحِ الزَّوْزَنِيِّ، لَا شِعْرٌ. وَتَقْسِيمُ الْفُصُولِ وَعَنَاوِينُهَا وَعَلَامَاتُ التَّرْقِيمِ مِنَ الْمُحَرِّرِ، وَالنَّصُّ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.")
ATTR_EN = ("The RECEIVED text, word for word. Chapter 1 is the khabar of al-Ḥārith ibn Ḥilliza in Ibn Qutayba (d. 276 AH), al-Shiʿr wa-l-shuʿarāʾ, in the edition al-Maktaba al-Shāmila names «Dār al-Ḥadīth, Cairo, 1423 AH» (book 23785), vol. 1 p. 193: the whole of § 319, from «هُوَ مِنْ بَنِي يَشْكُرَ» to «وَهُوَ لَا يَشْعُرُ», with nothing cut from inside it; what follows it (his son Madhʿūr, al-Aṣmaʿī's charge that he committed iqwāʾ in the ode, and the lines of his quoted as proverbs — §§ 320–322) is not given here. "
           "The chapters after it are his Muʿallaqa — in the metre al-khafīf, rhyming on a hamza with ḍamma, with an alif before it (the ridf) — in the recension, order and verse-count of al-Zawzanī (d. 486 AH), Sharḥ al-Muʿallaqāt al-sabʿ, the edition Shamela names «Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423 AH / 2002 CE» (book 11253), pp. 269–286, eighty-two verses, " + _sofar_en + ": " + _ch_en + ". Each verse is one sentence, and «•» marks the end of its first hemistich. " + _m_en + "The vowelling has two layers. What the edition vowels is kept, in this shelf's spelling; what it leaves bare — every short vowel of Ibn Qutayba's khabar (the edition prints only its shaddas; the fatḥa of the nūn of «عَنَزَةٍ» is from the editor's footnote), and many letters and word-endings of the verses — is supplied editorially, as the iʿrāb, the metre and the commentary require. " + _d_en
           + ("Left for the scholar's judgement: " + "; ".join(f[2] for f in _flg) + ". " if _flg else "")
           + "The iʿrāb of every word is in this shelf's own wording and was checked against Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409 AH / 1989 CE; book 151017, vol. 1 p. 455 – vol. 2 p. 4) — he gives the ode in eighty-six verses in another order; where his text differs from al-Zawzanī's, the difference is noted on the word, and where he gives two readings the first is given and the second mentioned. The figures of balāgha are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ: one that al-Zawzanī or al-Durra names or describes is credited to him, and one that rests on the Talkhīṣ's definition alone says «by the Talkhīṣ's definition». The translation gives each verse's plain meaning after al-Zawzanī; it is not poetry. The division into chapters, their titles and the punctuation are editorial, and the text awaits scholarly review.")
ATTR_TR = ("Metin LAFZIYLA aktarılmıştır. 1. bölüm, Hâris b. Hillize'nin haberidir: İbn Kuteybe (ö. 276 h.), eş-Şi'r ve'ş-şuarâ, el-Mektebetü'ş-Şâmile'nin «Dâru'l-Hadîs, Kahire, 1423 h.» diye andığı baskı (kitap 23785), c. 1 s. 193: 319. paragrafın tamamı, «هُوَ مِنْ بَنِي يَشْكُرَ»dan «وَهُوَ لَا يَشْعُرُ»a kadar, ortasından hiçbir şey çıkarılmadan; sonrası (oğlu Mez'ûr, Asmaî'nin kasidede ikvâ yaptığı sözü ve darb-ı mesel olan beyitleri — 320–322. paragraflar) burada verilmemiştir. "
           "Sonraki bölümler onun muallakasıdır — hafîf bahrinden; revîsi dammeli hemze, öncesinde ridf olarak elif — Zevzenî'nin (ö. 486 h.) rivayeti, sıralaması ve beyit sayımıyla: Şerhu'l-Muallakâti's-seb', Şâmile'nin «Dâru İhyâi't-Türâsi'l-Arabî, 1423 h. / 2002 m.» diye andığı baskı (kitap 11253), s. 269–286, seksen iki beyit; " + _sofar_tr + ": " + _ch_tr + ". Her beyit tek cümledir; «•» işareti ilk mısraın sonudur. " + _m_tr + "Harekeleme iki katmandır: baskının harekelediği, bu rafın imlâsıyla aynen korunmuştur; çıplak bıraktığı — İbn Kuteybe haberinin şeddeler dışındaki bütün harekeleri («عَنَزَةٍ»nin nûnundaki fetha muhakkikin dipnotundandır), beyitlerin birçok harfi ve kelime sonu — i'râbın, veznin ve şerhin gerektirdiği şekilde editörce konmuştur. " + _d_tr
           + ("Âlimin değerlendirmesine bırakılanlar: " + "; ".join(f[3] for f in _flg) + ". " if _flg else "")
           + "Her kelimenin i'râbı bu rafın kendi ifadesiyledir ve Muhammed Ali Tâhâ ed-Dürre'nin Fethu'l-Kebîri'l-Müteâl: İ'râbü'l-Muallakâti'l-aşri't-tıvâl'i (Mektebetü's-Sevâdî, Cidde, 2. baskı, 1409 h. / 1989 m.; kitap 151017, c. 1 s. 455 – c. 2 s. 4) ile karşılaştırılmıştır — o, kasideyi başka bir sıra ile seksen altı beyit olarak verir; rivayetinin Zevzenî'ninkinden ayrıldığı yerler kelimesinin üzerinde belirtilmiştir; iki vecih zikrettiği yerde birincisi verilmiş, ikincisine işaret edilmiştir. Belâgat vecihleri Kazvînî'nin Telhîsu'l-Miftâh'ındaki bâblarla adlandırılmıştır: Zevzenî'nin yahut Dürre'nin adını koyduğu veya tarif ettiği vecih ona nisbet edilmiş, yalnız Telhîs'in tarifine dayanan vecih için «Telhîs'in tarifine göre» denmiştir. Tercüme, beytin Zevzenî şerhine göre düz mânasıdır; şiir değildir. Bölümleme, başlıklar ve noktalama editöre aittir; metin ilmî incelemeyi beklemektedir.")
MANIFEST = {
 "id": SLUG, "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ الْحَارِثِ بْنِ حِلِّزَةَ", "en": "The Muʿallaqa of al-Ḥārith ibn Ḥilliza", "tr": "Hâris b. Hillize'nin Muallakası"},
 "subtitle": {"ar": ("الْمُعَلَّقَةُ كَامِلَةً" if WHOLE else "الْمُعَلَّقَةُ") + " بِرِوَايَةِ الزَّوْزَنِيِّ، مَعَ خَبَرِ الشَّاعِرِ عَنِ ابْنِ قُتَيْبَةَ — بَيْتًا بَيْتًا بِالْإِعْرَابِ وَالْبَلَاغَةِ",
              "en": ("The whole ode" if WHOLE else "The ode") + " in al-Zawzanī's recension, with the poet's story from Ibn Qutayba — verse by verse, with full iʿrāb and balāgha",
              "tr": "Zevzenî rivayetiyle muallaka" + ("nın tamamı" if WHOLE else "") + " ve İbn Kuteybe'den şairin haberi — beyit beyit, tam i'râb ve belâgatıyla"},
 "level": 6, "levelName": "Master", "version": "0.1.0", "published": "2026-11-20", "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": [],
 "attribution": {"ar": unicodedata.normalize("NFC", ATTR_AR), "en": ATTR_EN, "tr": ATTR_TR, "reviewStatus": "pending-scholarly-review"},
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
print("chapters:", len(CHAPS), "verses in package: 1-%d" % DONE_TO, "| verses authored:", len(VERSES), "of", POEM_END,
      "| sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
