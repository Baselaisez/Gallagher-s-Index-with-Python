"""Author content/samples/muallaqat-amr-ibn-kulthum — «مُعَلَّقَةُ عَمْرِو بْنِ كُلْثُومٍ», a RECEIVED text at Level 6 (Master).

Chapter 1 is the poet's khabar, VERBATIM from Ibn Qutayba, «الشعر والشعراء» (Dār al-Ḥadīth, Cairo 1423, 1/228–229, § 385;
shamela.ws/book/23785/221–222): one contiguous span, the killing of ʿAmr ibn Hind. The chapters after it are the Muʿallaqa
in al-Zawzanī's text, order and count («شرح المعلقات السبع», shamela.ws/book/11253/232–252, pp. 215–235): 103 verses, cut by
PLAN below. A verse is ONE sentence; the last token of its first hemistich carries punctAfter "•". The iʿrāb of every
token was checked against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال» (shamela.ws/book/151017/328–447, vol. 1
pp. 334–453 — he gives the ode in another order and count, 118 verses) and is written in the shelf's own wording; the
balāgha is named on the token that carries it, after the syntax. A figure a commentator names or describes is written
plainly with his name; one that rests on the Talkhīṣ's definition alone says «عَلَى حَدِّ التَّلْخِيصِ».

Sources on disk: research/sources/muallaqat-amr-ibn-kulthum-src.txt (Ibn Qutayba), -zawzani.txt, -durra.txt.

THIS FILE IS ASSEMBLED from parts kept in the author's work folder (head / chapter blocks / lexicon / tail); it is the
single source of the package. RESUMABLE: verses are filed by number through VV(); the chapters are cut from PLAN as far
as the verses reach, and the attribution says how far the package goes. To continue, add VV(n, …) blocks before the
«TAIL» marker, their new keys to NEW_GLOSS / NEW_VERBS, and run:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_amr_ibn_kulthum.py
"""
import json, os, pathlib, sys, unicodedata, re

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-amr-ibn-kulthum"
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
# the rhyme: the rawī is a nūn with fatḥa, the qāfiya muṭlaqa — the alif after the nūn is the waṣl (alif al-iṭlāq)
ITLAQ = (" — وَالْأَلِفُ لِلْإِطْلَاقِ", " — the final alif is the alif of iṭlāq (the rhyme is unbound)", " — sondaki elif ıtlâk elifidir (kâfiye mutlaktır)")
S_JMSI = (S_JMS[0] + "، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ، وَالْأَلِفُ لِلْإِطْلَاقِ", S_JMS[1] + "; its nun stands for the tanwin of the singular, and the final alif is the alif of iṭlāq", S_JMS[2] + "; nûn müfreddeki tenvinin karşılığıdır, sondaki elif ıtlâk elifidir")
S_JMSRI = (S_JMSR[0] + "، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ، وَالْأَلِفُ لِلْإِطْلَاقِ", S_JMSR[1] + "; its nun stands for the tanwin of the singular, and the final alif is the alif of iṭlāq", S_JMSR[2] + "; nûn müfreddeki tenvinin karşılığıdır, sondaki elif ıtlâk elifidir")
TANW_ALIF = (" — وَالْأَلِفُ فِي آخِرِهِ بَدَلٌ مِنَ التَّنْوِينِ فِي الْقَافِيَةِ", " — at the rhyme its final alif stands in for the tanwin", " — kâfiyede sondaki elif tenvinden bedeldir")

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
# Chapter 1 — خَبَرُ عَمْرِو بْنِ كُلْثُومٍ (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/228–229, from § 385 — verbatim, contiguous)
# =====================================================================================================================
AMR_H = DZ("هُوَ يَعُودُ عَلَى عَمْرِو بْنِ هِنْدٍ", "«he» — ʿAmr ibn Hind", "Amr b. Hind'e dönen gizli «o»")
AMR_K = DZ("هُوَ يَعُودُ عَلَى عَمْرِو بْنِ كُلْثُومٍ", "«he» — ʿAmr ibn Kulthūm", "Amr b. Külsûm'a dönen gizli «o»")
HIND_F = DZ("هِيَ يَعُودُ عَلَى هِنْدٍ", "«she» — Hind", "Hind'e dönen gizli «o»")
UMM_F = DZ("هِيَ يَعُودُ عَلَى أُمِّهِ", "«she» — his mother", "annesine dönen gizli «o»")
IBN = lambda role, full, n=NO: R(role, full, "ibn", mud=True, n=n)
def NAME(role, full, lex, sign=None, n=NO, p=None, g=()):
    return R(role, full, lex, pos="propn", sign=sign, n=n, p=p, g=g)
HIND_J = lambda p=None: NAME("mdf", "هِنْدٍ", "hind", p=p)
S_DIPT_T = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ", " — by the fatha that stands for the kasra: a diptote, being a proper name on the pattern of a verb", " — özel isim ve fiil vezninde olduğu için gayr-i munsarif: kesre yerine fetha ile")
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Now ʿAmr ibn Hind had ordered his mother to send the servants away when he called for the dainties, and to make Laylā serve.",
  "tr": "Amr b. Hind, tatlıları/nadide yiyecekleri istediğinde annesine hizmetçileri uzaklaştırmasını ve Leylâ'ya hizmet ettirmesini emretmişti."},
 "tokens": [QAD("وَقَدْ", c="wi"),
  T("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرُ الشَّأْنِ مُسْتَتِرٌ، وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ خَبَرُهُ.",
    "A defective past verb built on fatha; its noun is the hidden pronoun of the matter (ḍamīr al-shaʾn), and the clause after it is its predicate, in the seat of nasb.",
    "Fetha üzere mebnî nâkıs mâzî; ismi gizli şa'n zamiridir, ondan sonraki cümle mahallen mansûb haberidir."),
  V("m", "أَمَرَ", "amara-command", n=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ»", " — the clause is the predicate of كَانَ, in the seat of nasb", " — cümle «kâne»nin haberi, mahallen mansûb")),
  NAME("fail", "عَمْرُو", "amr-name"),
  IBN("naatr", "بْنُ"), HIND_J(),
  R("maf", "أُمَّهُ", "umm", enc="هُ"),
  AN(n=(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ مَنْصُوبٌ عَلَى نَزْعِ الْخَافِضِ: أَمَرَهَا بِتَنْحِيَةِ الْخَدَمِ", " — it and its verb make a masdar, in nasb by the dropping of the jarr letter: «he ordered her to the sending-away of the servants»", " — fiille birlikte masdar olur; cer harfinin düşmesiyle mansûbdur: «hizmetçileri uzaklaştırmayı emretti»")),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "تُنَحِّيَ", "nahha-amr", doer=UMM_F, g=["form-ii-verbs", "naqis-verbs"]),
  R("maf", "الْخَدَمَ", "khadam-servants"),
  IDHA(n=(" — وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ", " — its answer is left out, shown by what goes before", " — cevabı mahzûftur, öncesi ona delâlet eder")),
  V("ma", "دَعَا", "daa", doer=AMR_H, g=["naqis-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  R("majr", "بِالطُّرَفِ", "turfa", j="bi", g=["jam-taksir"], n=MT("دَعَا", "called", "istedi»ye"), p="،"),
  V(NS("لِعَطْفِهِ عَلَى «تُنَحِّيَ»", "being joined to «send away»", "«uzaklaştırsın»a atfedildiği için"), "وَتَسْتَخْدِمَ", "istakhdama-amr", c="w", doer=UMM_F, g=["form-x-verbs"]),
  NAME("maf", "لَيْلَى", "layla-alam", sign=S_AN, g=["ism-maqsur-manqus"], p=".")]})
S1.append({"id": "s2", "translation": {
  "en": "ʿAmr ibn Hind called for a table and set it up, and they ate; then he called for the dainties.",
  "tr": "Amr b. Hind bir sofra istedi ve onu kurdu, yediler; sonra tatlıları istedi."},
 "tokens": [V("ma", "فَدَعَا", "daa", c="fi", g=["naqis-verbs"]),
  NAME("fail", "عَمْرُو", "amr-name"), IBN("naatr", "بْنُ"), HIND_J(),
  R("majr", "بِمَائِدَةٍ", "maida", j="bi", n=MT("دَعَا", "called", "istedi»ye")),
  V("m", "فَنَصَبَهَا", "nasaba-set", c="f", enc="هَا", doer=AMR_H, p="،"),
  V("mw", "فَأَكَلُوا", "akala", c="f", p="،"),
  PT("ثُمَّ", "thumma", "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي", "a conjunction of order with an interval", "tertip ve terâhî bildiren atıf harfi", g=["atf-nasaq"]),
  V("ma", "دَعَا", "daa", doer=AMR_H, g=["naqis-verbs"], n=CL("atf", "أَكَلُوا", "they ate", "yediler")),
  R("majr", "بِالطُّرَفِ", "turfa", j="bi", g=["jam-taksir"], n=MT("دَعَا", "called", "istedi»ye"), p=".")]})
S1.append({"id": "s3", "translation": {
  "en": "Hind said: «Laylā, hand me that dish!»",
  "tr": "Hind: «Leylâ, şu tabağı bana uzat!» dedi."},
 "tokens": [V("mt", "فَقَالَتْ", "qala", c="fi", g=["hollow-verbs"]),
  NAME("fail", "هِنْدٌ", "hind", n=(" — وَصُرِفَ لِأَنَّهُ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ، وَيَجُوزُ فِيهِ الْمَنْعُ", " — given tanwin, being a three-letter name with a quiescent middle; it may also be left a diptote", " — orta harfi sâkin üç harfli isim olduğu için munsarif kılınmıştır; gayr-i munsarif yapmak da caizdir"), p=":"),
  PT("يَا", "ya-nida", "حَرْفُ نِدَاءٍ", "the particle of calling", "nidâ harfi", g=["vocative-munada"]),
  T("لَيْلَى", "layla-alam", "propn", ["vocative-munada", "ism-maqsur-manqus"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ فِي مَحَلِّ نَصْبٍ.",
    "A single proper-name vocative, built on a damma estimated on the alif, in the seat of nasb.", "Müfred alem münâdâ: elif üzerinde takdîrî damme üzere mebnî, mahallen mansûb."),
  V("a5y", "نَاوِلِينِي", "nawala-amr", enc="نِي", encrole="maf1", g=["form-iii-verbs", "ya-al-mutakallim", "mafulayn"], n=(" — وَالنُّونُ لِلْوِقَايَةِ؛ وَجُمْلَةُ النِّدَاءِ وَمَا بَعْدَهَا فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", " — the nun is the nun of protection; the call and what follows it are what she said, in the seat of nasb", " — nûn vikâye nûnudur; nidâ cümlesi ve sonrası mahallen mansûb mekûl-i kavldir")),
  T("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "mafulayn"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
    "A demonstrative built on sukun, in the seat of nasb as the second object; the lam marks distance and the kaf is a particle of address.", "Sükûn üzere mebnî işaret ismi, mahallen mansûb ikinci mef'ûl; lâm uzaklık, kâf hitap harfidir."),
  R("bdln", "الطَّبَقَ", "tabaq-amr", of=("ذٰلِكَ", "that", "şu"), p="!")]})
S1.append({"id": "s4", "translation": {
  "en": "Laylā said: «Let the one who has the need get up to her need.»",
  "tr": "Leylâ: «İhtiyacı olan, ihtiyacına kendisi kalksın» dedi."},
 "tokens": [V("mt", "فَقَالَتْ", "qala", c="fi", g=["hollow-verbs"]),
  NAME("fail", "لَيْلَى", "layla-alam", sign=S_AR, g=["ism-maqsur-manqus"], p=":"),
  T("لِتَقُمْ", "qama", "verb", ["lam-amr", "hollow-verbs", "jawazim-al-mudari-wal-amr-fil-kafiya"],
    "اللَّامُ لَامُ الْأَمْرِ حَرْفُ جَزْمٍ، وَتَقُمْ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِهَا وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "The lam is the lam of command, a jazm particle; تَقُمْ is a present verb in jazm by it, its sign the sukun, its middle waw dropped where two quiescents meet; the clause is what she said, in the seat of nasb.",
    "Lâm emir lâmıdır, cezm harfi; «tekum» onunla meczûm muzâri, alâmeti sükûn; iki sâkin buluştuğu için ayn'el-fiili (vâv) düşmüştür; cümle mahallen mansûb mekûl-i kavldir.",
    segs=SG(("لِ", "lam-amr", "part"), ("تَقُمْ", "qama", "verb"))),
  R("fail", "صَاحِبَةُ", "sahib", mud=True),
  R("mdf", "الْحَاجَةِ", "haja"),
  PR("إِلَى", "ila", n=MT("تَقُمْ", "get up", "kalksın»a")),
  R("majr", "حَاجَتِهَا", "haja", enc="هَا", p=".")]})
S1.append({"id": "s5", "translation": {
  "en": "Hind said it to her again and pressed her, and Laylā cried out: «O the shame of it! Help, O Taghlib!»",
  "tr": "Hind sözünü tekrarladı ve ısrar etti; bunun üzerine Leylâ: «Vay zilletime! Yetiş ey Tağlib!» diye haykırdı."},
 "tokens": [V("mt", "فَأَعَادَتْ", "aada", c="fi", doer=HIND_F, g=["form-iv-verbs", "hollow-verbs", "hadhf-al-maful"], n=(" — وَالْمَفْعُولُ مَحْذُوفٌ: أَعَادَتْ عَلَيْهَا الْقَوْلَ", " — the object is left out: she said it to her again", " — mef'ûl mahzûftur: sözü ona tekrarladı")),
  JP("عَلَيْهَا", "ala", "هَا", n=MT("أَعَادَتْ", "said again", "tekrarladı»ya")),
  V("mt", "وَأَلَحَّتْ", "alahha-amr", c="w", doer=HIND_F, g=["form-iv-verbs", "doubled-verbs"], p="،"),
  V("mt", "فَصَاحَتْ", "saha-shout", c="f", g=["hollow-verbs"]),
  NAME("fail", "لَيْلَى", "layla-alam", sign=S_AR, g=["ism-maqsur-manqus"], p=":"),
  T("وَاذُلَّاهْ", "dhull", "noun", ["vocative-munada"],
    "«وَا» حَرْفُ نُدْبَةٍ، وَ«ذُلَّ» مُنَادًى مَنْدُوبٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ مَنَعَ مِنْ ظُهُورِهِ فَتْحَةُ الْمُنَاسَبَةِ لِأَلِفِ النُّدْبَةِ، فِي مَحَلِّ نَصْبٍ، وَالْأَلِفُ لِلنُّدْبَةِ، وَالْهَاءُ لِلسَّكْتِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "وَا is the particle of lament (nudba); ذُلّ «shame» is the lamented, built on a damma that is only estimated — the fatha that suits the alif of lament takes its place — in the seat of nasb; the alif is the alif of lament and the ha is the ha of pause; the cry is what she said, in the seat of nasb.",
    "«Vâ» nüdbe harfidir; «zull» nüdbe münâdâsıdır: nüdbe elifine uygun fetha görünmesine engel olan takdîrî damme üzere mebnî, mahallen mansûb; elif nüdbe elifi, hâ sekt hâsıdır; cümle mahallen mansûb mekûl-i kavldir.",
    p="!", segs=SG(("وَا", "wa-nudba", "part"), ("ذُلَّاهْ", "dhull", "noun"))),
  PT("يَا", "ya-nida", "حَرْفُ نِدَاءٍ وَاسْتِغَاثَةٍ", "the particle of calling, here a call for help", "nidâ ve istiğâse harfi", g=["vocative-munada"]),
  T("لَتَغْلِبَ", "taghlib-amr", "propn", ["vocative-munada", "huruf-jarr", "mamnu-min-sarf"],
    "اللَّامُ لَامُ الِاسْتِغَاثَةِ، حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى الْفَتْحِ، وَ«تَغْلِبَ» مُسْتَغَاثٌ بِهِ مَجْرُورٌ بِاللَّامِ " + S_DIPT_T[0] + "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَا» لِنِيَابَتِهَا عَنْ «أَدْعُو».",
    "The lam is the lam of the call for help, a jarr letter built on fatha; «Taghlib» is the one called to help, in jarr by the lam" + S_DIPT_T[1] + "; the phrase hangs on يَا, which stands for «I call».",
    "Lâm istiğâse lâmıdır, fetha üzere mebnî cer harfi; «Tağlib» kendisinden yardım istenen (müstegâsün bih), lâm ile mecrûr" + S_DIPT_T[2] + "; câr-mecrûr «ed'û» yerine geçen «yâ»ya müteallik.",
    p="!", segs=SG(("لَ", "li", "prep"), ("تَغْلِبَ", "taghlib-amr", "propn")))]})
S1.append({"id": "s6", "translation": {
  "en": "ʿAmr ibn Kulthūm heard her, and the blood rose in his face; he looked at ʿAmr ibn Hind and saw the evil in his face.",
  "tr": "Amr b. Külsûm onu duydu, yüzüne kan hücum etti; Amr b. Hind'e baktı ve yüzündeki kötülüğü sezdi."},
 "tokens": [V("m", "فَسَمِعَهَا", "samia", c="fi", enc="هَا"),
  NAME("fail", "عَمْرُو", "amr-name"), IBN("naatr", "بْنُ"), NAME("mdf", "كُلْثُومٍ", "kulthum"),
  V("m", "فَثَارَ", "thara", c="f", g=["hollow-verbs"]),
  R("fail", "الدَّمُ", "dam"),
  PR("فِي", "fi", n=MT("ثَارَ", "rose", "hücum etti»ye")),
  R("majr", "وَجْهِهِ", "wajh", enc="هِ", p="،"),
  V("m", "وَنَظَرَ", "nazara", c="w", doer=AMR_K),
  PR("إِلَى", "ila", n=MT("نَظَرَ", "looked", "baktı»ya")),
  NAME("majr", "عَمْرِو", "amr-name"), IBN("naatj", "بْنِ"), HIND_J(p="،"),
  V("m", "فَعَرَفَ", "arafa", c="f", doer=AMR_K),
  R("maf", "الشَّرَّ", "sharr"),
  PR("فِي", "fi", n=MT("عَرَفَ", "saw", "sezdi»ye")),
  R("majr", "وَجْهِهِ", "wajh", enc="هِ", n=(" — أَيْ فِي وَجْهِ عَمْرِو بْنِ هِنْدٍ", " — that is, in ʿAmr ibn Hind's face", " — yani Amr b. Hind'in yüzünde"), p=".")]})
S1.append({"id": "s7", "translation": {
  "en": "So he went to a sword of ʿAmr ibn Hind's hanging in the pavilion — there was no other sword there — and struck ʿAmr ibn Hind's head with it until he killed him.",
  "tr": "Bunun üzerine Amr b. Hind'in otağda asılı duran kılıcına yöneldi — orada ondan başka kılıç yoktu — ve onunla Amr b. Hind'in başına vurup onu öldürdü."},
 "tokens": [V("m", "فَقَامَ", "qama", c="fi", doer=AMR_K, g=["hollow-verbs"]),
  PR("إِلَى", "ila", n=MT("قَامَ", "went", "yöneldi»ye")),
  R("majr", "سَيْفٍ", "sayf"),
  R("majr", "لِعَمْرِو", "amr-name", pos="propn", j="li", n=MTH("نَعْتٍ لِـ«سَيْفٍ»", "an omitted adjective of «a sword»", "«kılıç»ın mahzûf sıfatına")),
  IBN("naatj", "بْنِ"), HIND_J(),
  R("naatj", "مُعَلَّقٍ", "muallaq", g=["ism-maful"], of=("سَيْفٍ", "a sword", "kılıç")),
  R("majr", "بِالرِّوَاقِ", "riwaq", j="bi", n=MT("مُعَلَّقٍ", "hanging", "asılı»ya"), p="،"),
  T("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens a hal clause; لَيْسَ is a defective, frozen past verb built on fatha; the clause is a hal, in the seat of nasb.",
    "Vâv hâliyyedir; «leyse» fetha üzere mebnî, câmid nâkıs mâzî; cümle mahallen mansûb hâldir.", segs=SG(("وَ", "wa", "conj"), ("لَيْسَ", "laysa", "verb"))),
  T("هُنَاكَ", "hunaka", "noun", ["asma-al-ishara", "maful-fih"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «لَيْسَ» مُقَدَّمٍ، وَالْكَافُ حَرْفُ خِطَابٍ.",
    "A demonstrative of place built on sukun, in the seat of nasb as an adverb; it hangs on the omitted, fronted predicate of لَيْسَ; the kaf is a particle of address.",
    "Mekân için işaret ismi, sükûn üzere mebnî, zarf olarak mahallen mansûb; «leyse»nin öne alınmış mahzûf haberine müteallik; kâf hitap harfidir."),
  T("سَيْفٌ", "sayf", "noun", ["kana-wa-akhawatuha"], "اسْمُ «لَيْسَ» مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of لَيْسَ, put after its predicate, in raf'.", "«Leyse»nin sona bırakılmış ismi, merfû."),
  R("naatr", "غَيْرُهُ", "ghayr", enc="هُ", of=("سَيْفٌ", "sword", "kılıç"), p="،"),
  V("m", "فَضَرَبَ", "daraba", c="f", doer=AMR_K),
  JP("بِهِ", "bi", "هِ", n=MT("ضَرَبَ", "struck", "vurdu»ya")),
  R("maf", "رَأْسَ", "ras", mud=True),
  NAME("mdf", "عَمْرِو", "amr-name"), IBN("naatj", "بْنِ"), HIND_J(),
  PT("حَتَّى", "hatta", "حَرْفُ ابْتِدَاءٍ وَغَايَةٍ", "a particle of limit that opens a fresh clause", "gâye bildiren ibtidâ harfi", g=["ila-hatta-fi-wal-ba-fil-kafiya"]),
  V("m", "قَتَلَهُ", "qatala", enc="هُ", doer=AMR_K, n=(" — وَالْجُمْلَةُ بَعْدَ «حَتَّى» الِابْتِدَائِيَّةِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — the clause after this حَتَّى has no seat of its own", " — ibtidâiyye «hattâ»dan sonraki cümlenin i'râbda mahalli yoktur"), p=".")]})
S1.append({"id": "s8", "translation": {
  "en": "He called out among the Banū Taghlib, and they plundered everything in the pavilion, drove off his thoroughbred camels and set out towards al-Jazīra.",
  "tr": "Benî Tağlib arasında seslendi; otağda ne varsa yağmaladılar, onun soylu develerini sürüp götürdüler ve Cezîre'ye doğru yola koyuldular."},
 "tokens": [V("ma", "وَنَادَى", "nada", c="wi", doer=AMR_K, g=["form-iii-verbs", "naqis-verbs"]),
  PR("فِي", "fi", n=MT("نَادَى", "called out", "seslendi»ye")),
  R("majr", "بَنِي", "banu", mud=True, sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", " — by the ya, as it declines like the sound masculine plural", " — cem-i müzekker sâlime mülhak olduğu için yâ ile"), g=["jam-mudhakkar-salim"]),
  NAME("mdf", "تَغْلِبَ", "taghlib-amr", sign=S_DIPT_T, g=["mamnu-min-sarf"], p="،"),
  V("mw", "فَانْتَهَبُوا", "intahaba-amr", c="f", g=["form-viii-verbs"]),
  R("maf", "جَمِيعَ", "jami", mud=True),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A relative noun built on sukun, in the seat of jarr as the second term of the idafa.", "Sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr muzâfun ileyh."),
  PR("فِي", "fi", n=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِلَةِ الْمَوْصُولِ", "; the phrase hangs on the omitted ṣila of the relative", "; câr-mecrûr mevsûlün mahzûf sılasına müteallik")),
  R("majr", "الرِّوَاقِ", "riwaq", p="،"),
  V("mw", "وَسَاقُوا", "saqa", c="w", g=["hollow-verbs"]),
  R("maf", "نَجَائِبَهُ", "najiba-amr", enc="هُ", g=["jam-taksir"], p="،"),
  V("mw", "وَسَارُوا", "sara-go", c="w", g=["hollow-verbs"]),
  R("zarfm", "نَحْوَ", "nahw", mud=True, n=MZ("سَارُوا", "set out", "yola koyuldular»a")),
  R("mdf", "الْجَزِيرَةِ", "jazira-amr", pos="propn", p=".")]})
CH[1] = S1
# =====================================================================================================================
# The poem — vv. 1–8 — الصَّبُوحُ
# =====================================================================================================================
ROLE["isml"] = ("اسْمُ «مَا» الْحِجَازِيَّةِ مَرْفُوعٌ", "the noun of the Ḥijāzī مَا, in raf'", "Hicâzî «mâ»nın ismi, merfû", "raf", ["ma-la-mushabbaha"])
ROLE["khbma"] = ("خَبَرُ «مَا» الْحِجَازِيَّةِ مَنْصُوبٌ", "the predicate of the Ḥijāzī مَا, in nasb", "Hicâzî «mâ»nın haberi, mansûb", "nasb", ["ma-la-mushabbaha"])
ROLE["munm"] = ("مُنَادًى مُضَافٌ مَنْصُوبٌ", "a vocative that is annexed, in nasb", "muzâf münâdâ, mansûb", "nasb", ["vocative-munada"])
JARR["biz"] = ("bi", "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ", "The ba is an extra jarr letter; ", "Bâ zâid cer harfidir; ")
Y5 = ("، وَيَاءُ الْمُخَاطَبَةِ " + _FA, "; the ya of the woman addressed is the doer, in the seat of raf'", "; muhâtaba yâsı fâildir, mahallen merfû")
W5 = ("، وَوَاوُ الْجَمَاعَةِ " + _FA, "; the waw of the group is the doer, in the seat of raf'", "; cemaat vâvı fâildir, mahallen merfû")
NO_HADHF = lambda: NT("وَحَرْفُ النِّدَاءِ مَحْذُوفٌ", "the particle of calling is left out", "nidâ harfi mahzûftur")
def UMM_AMR(note=NO):
    return [R("munm", "أُمَّ", "umm", n=N3(NO_HADHF(), note)), R("mdf", "عَمْرٍو", "amr-name", pos="propn")]
SAQIYA = DZ("أَنْتِ", "«you» (fem.)", "gizli zamir «sen» (müennes)")
KHAMR = HIYA("الْخَمْرِ", "the wine", "şaraba")
VV(1, "Ho! Wake, (cup-bearer,) with your great bowl and give us the morning draught, and do not keep back the wines of al-Andarīn —",
  "Hey! Uyan da büyük kadehinle bize sabah şarabını sun; Enderîn şaraplarını esirgeme —",
 [PT("أَلَا", "ala-tanbih", "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ لَا عَمَلَ لَهُ — وَالْقَصِيدَةُ مِنَ الْبَحْرِ الْوَافِرِ، وَرَوِيُّهَا نُونٌ مَفْتُوحَةٌ بَعْدَهَا أَلِفُ الْإِطْلَاقِ، وَقَبْلَهَا يَاءٌ أَوْ وَاوٌ رِدْفًا", "a particle that opens the speech and calls attention; it governs nothing — the ode is in the metre al-wāfir; its rhyme-letter is a nun with fatha followed by the alif of iṭlāq, with a ya or waw before it as ridf", "istiftâh ve tenbîh harfi, ameli yoktur — kaside vâfir bahrindendir; revîsi fethalı nûn, ardından ıtlâk elifi, öncesinde ridf olarak yâ yahut vâv", g=["huruf-tanbih", "ilm-al-arud", "al-qafiya"]),
  V("a5y", "هُبِّي", "habba-blow", g=["doubled-verbs"], n=N3(CL("ibt"), ZW("هَبَّ مِنْ نَوْمِهِ هَبًّا: إِذَا اسْتَيْقَظَ", "هَبَّ مِنْ نَوْمِهِ: he woke from his sleep", "«hebbe min nevmihî»: uykusundan uyandı"))),
  R("majr", "بِصَحْنِكِ", "sahn-amr", j="bi", enc="كِ", n=N3(MT("هُبِّي", "wake", "uyan»a"), ZW("الصَّحْنُ: الْقَدَحُ الْعَظِيمُ", "صَحْن is a great bowl", "«sahn»: büyük kadeh"))),
  V("a5y", "فَاصْبَحِينَا", "sabaha", c="f", enc="نَا", n=N3(CL("atf", "هُبِّي", "wake", "uyan"), ZW("الصَّبْحُ: سَقْيُ الصَّبُوحِ", "صَبْح is giving the morning draught", "«sabh»: sabah şarabını sunmak")))],
 [PT("وَلَا", "la-nahiya", "لَا نَاهِيَةٌ جَازِمَةٌ", "لَا of forbidding, which puts the verb in jazm", "cezmeden nehiy «lâ»sı", c="w", g=["la-nahiya"]),
  V(JZ("بِـ«لَا» النَّاهِيَةِ", "by the لَا of forbidding", "nehiy «lâ»sı ile", sign="nun"), "تُبْقِي", "abqa-v", g=["form-iv-verbs", "naqis-verbs", "afal-khamsa", "fail"], n=N3(Y5, CL("atf", "هُبِّي", "wake", "uyan"))),
  R("maf", "خُمُورَ", "khamr", mud=True, g=["jam-taksir"]),
  R("mdf", "الْأَنْدَرِينَا", "andarin-amr", pos="propn", g=["jam-mudhakkar-salim"], sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ، وَالْأَلِفُ لِلْإِطْلَاقِ", " — by the ya, as it declines like the sound masculine plural; its nun stands for the tanwin of the singular, and the final alif is the alif of iṭlāq", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûn müfreddeki tenvinin karşılığı, sondaki elif ıtlâk elifidir"),
    n=N3(DR("وَيَجُوزُ أَنْ يُعْرَبَ بِالْحَرَكَاتِ عَلَى النُّونِ، فَيَكُونُ مَجْرُورًا بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", "it may also take its vowels on the nun, and be a diptote in jarr by the fatha", "nûn üzerinde harekelerle i'râb edilip gayr-i munsarif olarak fetha ile mecrûr da olabilir"), ZW("الْأَنْدَرُونَ: قُرًى بِالشَّامِ", "al-Andarūn are villages in Syria", "Enderûn: Şam'da köyler")))])
VV(2, "mixed with water, as though wars-blossom were in it; when the water has mingled with it, we grow open-handed.",
  "suyla karıştırılmış olarak, sanki içinde vers çiçeği varmış gibi; su ona karıştığında cömertleşiriz.",
 [R("hal", "مُشَعْشَعَةً", "mushashaa-amr", g=["ism-maful"], n=N3(NT("صَاحِبُهَا «خُمُورَ الْأَنْدَرِينَا»", "of «the wines of al-Andarīn»", "«Enderîn şarapları»nın hâli"), DR("وَقِيلَ: مَفْعُولٌ بِهِ ثَانٍ لِـ«اصْبَحِينَا»", "some make it the second object of «give us the morning draught»", "«bize sabah şarabı sun»un ikinci mef'ûlü olduğu da söylenmiştir"), ZW("شَعْشَعْتُ الشَّرَابَ: مَزَجْتُهُ بِالْمَاءِ", "شَعْشَعَ is to mix a drink with water", "«şa'şa'tu'ş-şerâbe»: içkiyi suyla karıştırdım"))),
  KAANNA("كَأَنَّ", g=TB + ["aqsam-wajh-al-shabah"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ مِنْ «خُمُورَ»", "the clause is a second hal of «wines», in the seat of nasb", "cümle «şaraplar»ın ikinci hâli, mahallen mansûb"),
    (" — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْخَمْرُ الْمَمْزُوجَةُ، وَالْمُشَبَّهُ بِهِ نَوْرُ الْحُصِّ الْأَحْمَرُ أُلْقِيَ فِيهَا، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — شِدَّةُ الْحُمْرَةِ — ذَكَرَهُ الزَّوْزَنِيُّ وَلَمْ يُذْكَرْ فِي الْبَيْتِ: «كَأَنَّهَا مِنْ شِدَّةِ حُمْرَتِهَا بَعْدَ امْتِزَاجِهَا بِالْمَاءِ أُلْقِيَ فِيهَا نَوْرُ هٰذَا النَّبْتِ»",
     " — a tashbih mursal mujmal: the mixed wine is likened to the red blossom of wars dropped into it; the particle is كَأَنَّ; the point of likeness — the depth of the red — is named by al-Zawzanī, not in the verse: «as if, from the depth of its red once mixed with water, this plant's blossom had been thrown into it»",
     " — teşbîh-i mürsel mücmel: müşebbeh suyla karışmış şarap, müşebbehün bih içine atılmış kırmızı vers çiçeği, edat «keenne»; vech-i şebeh — kızıllığın koyuluğu — beyitte değil, Zevzenî'de zikredilir: «suyla karıştıktan sonra kızıllığının koyuluğundan sanki içine bu bitkinin çiçeği atılmış»"))),
  R("ismka", "الْحُصَّ", "huss-amr", n=ZW("الْحُصُّ: الْوَرْسُ، نَبْتٌ لَهُ نَوَّارٌ أَحْمَرُ يُشْبِهُ الزَّعْفَرَانَ", "حُصّ is wars, a plant with a red blossom like saffron", "«huss»: vers, safrana benzeyen kırmızı çiçekli bir bitki")),
  JP("فِيهَا", "fi", "هَا", n=MTH("خَبَرِ «كَأَنَّ»", "the omitted predicate of كَأَنَّ", "«keenne»nin mahzûf haberine"))],
 [IDHA(),
  MA_Z(),
  R("fail", "الْمَاءُ", "ma", n=DR("فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ بَعْدَهُ: إِذَا خَالَطَهَا الْمَاءُ، وَالْجُمْلَةُ الْمَحْذُوفَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "it is the doer of an omitted verb that the one after it explains — «when the water mingled with it» — and that omitted clause is in the seat of jarr, إِذَا being annexed to it", "sonraki fiilin açıkladığı mahzûf bir fiilin fâilidir: «su ona karıştığında»; mahzûf cümle «izâ»nın ona muzâf olmasıyla mahallen mecrûrdur")),
  V("m", "خَالَطَهَا", "khalata-amr", enc="هَا", doer=HUWA("الْمَاءِ", "the water", "suya"), g=["form-iii-verbs"], n=NT("وَالْجُمْلَةُ مُفَسِّرَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause explains the omitted one and has no seat of its own", "cümle tefsîriyyedir, i'râbda mahalli yoktur")),
  V("mna", "سَخِينَا", "sakhiya-amr", g=["naqis-verbs"], n=N3(CL("jawab"), DR("وَإِنْ جُعِلَ «سَخِينًا» صِفَةً بِمَعْنَى الْحَارِّ فَهُوَ حَالٌ مِنَ «الْمَاءُ»، وَ«إِذَا» حِينَئِذٍ ظَرْفٌ مُجَرَّدٌ مِنَ الشَّرْطِ", "if «سَخِينًا» is taken as an adjective, «hot», it is a hal of «the water», and إِذَا is then a plain adverb", "«sehînen» «sıcak» anlamında sıfat sayılırsa «su»dan hâldir; o zaman «izâ» şart anlamından soyulmuş zarftır"),
    ZW("مِنْ سَخِيَ يَسْخَى سَخَاءً: جُدْنَا بِعَقَائِلِ أَمْوَالِنَا", "from سَخِيَ يَسْخَى: we gave freely of our dearest goods", "«sehiye yeshâ»dan: en kıymetli mallarımızı cömertçe dağıttık")))])
VV(3, "It turns the man with a need aside from his desire when he tastes it, until he grows mild.",
  "İhtiyaç sahibini, onu tattığında, yumuşayıncaya dek arzusundan çevirir.",
 [V("d", "تَجُورُ", "jara-stray-tf", doer=KHAMR, g=["hollow-verbs"], n=N3(CL("ist"), ZW("يَمْدَحُ الْخَمْرَ: تُمِيلُ صَاحِبَ الْحَاجَةِ عَنْ حَاجَتِهِ وَهَوَاهُ", "he praises the wine: it turns the man with a need away from his need and his desire", "şarabı över: ihtiyaç sahibini ihtiyacından ve arzusundan çevirir"))),
  R("majr", "بِذِي", "dhu", j="bi", mud=True, sign=S_YA5, g=["five-nouns"], n=MT("تَجُورُ", "turns", "çevirir»e")),
  R("mdf", "اللُّبَانَةِ", "lb-lubana"),
  PR("عَنْ", "an", n=MT("تَجُورُ", "turns", "çevirir»e")),
  R("majr", "هَوَاهُ", "hawa-desire", enc="هُ", sign=S_AJ, g=["ism-maqsur-manqus"])],
 [IDHA(plain=True, n=MZ("تَجُورُ", "turns", "çevirir»e")),
  MA_Z(),
  V("m", "ذَاقَهَا", "dhaqa", enc="هَا", doer=HUWA("ذِي اللُّبَانَةِ", "the man with a need", "ihtiyaç sahibine"), g=["hollow-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  HATTA(),
  V(NS("بِـ«أَنْ» مُضْمَرَةً وُجُوبًا بَعْدَ «حَتَّى»", "by an أَنْ understood after حَتَّى", "«hattâ»dan sonra gizli «en» ile"), "يَلِينَا", "lana", doer=HUWA("ذِي اللُّبَانَةِ", "the man with a need", "ihtiyaç sahibine"), g=["hollow-verbs", "nawasib-wa-jawazim-al-mudari"],
    n=N3(ITLAQ, NT("وَ«أَنْ» الْمُضْمَرَةُ وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِـ«حَتَّى»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَجُورُ»", "the understood أَنْ and the verb make a masdar in jarr after حَتَّى, and that phrase hangs on «turns»", "gizli «en» ile fiil «hattâ» ile mecrûr bir masdar olur; câr-mecrûr «çevirir»e müteallik")))])
VV(4, "You see the narrow-chested, grasping miser, when it is passed round to him, holding his wealth cheap for its sake.",
  "Göğsü dar, cimri ve hırslı adamı, şarap ona sunulup dolaştırıldığında, onun uğruna malını hor görür hâlde görürsün.",
 [V("da", "تَرَى", "raa", doer=ANTA, g=["naqis-verbs"], n=CL("ist")),
  R("maf", "اللَّحِزَ", "lahiz-amr", g=["sifa-mushabbaha", "hadhf-wa-taqdir"], n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("اللَّحِزُ: الضَّيِّقُ الصَّدْرِ؛ تَرَى الْإِنْسَانَ الضَّيِّقَ الصَّدْرِ", "لَحِز is narrow-chested: «you see the narrow-chested man»", "«lahiz»: göğsü dar; «göğsü dar insanı görürsün»"))),
  R("naatn", "الشَّحِيحَ", "shahih-amr", g=["sifa-mushabbaha"], n=ZW("الشَّحِيحُ: الْبَخِيلُ الْحَرِيصُ", "شَحِيح is the grasping miser", "«şahîh»: hırslı cimri")),
  IDHA(plain=True, n=MZ("تَرَى", "see", "görürsün»e")),
  V("mt", "أُمِرَّتْ", "amarra-amr", pas=True, doer=KHAMR, g=["form-iv-verbs", "doubled-verbs"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), ZW("أَيْ إِذَا أُدِيرَتْ عَلَيْهِ", "that is, when it is passed round to him", "yani ona sunulup dolaştırıldığında")))],
 [JP("عَلَيْهِ", "ala", "هِ", n=MT("أُمِرَّتْ", "passed round", "dolaştırıldı»ya")),
  R("majr", "لِمَالِهِ", "mal", j="li", enc="هِ", n=MT("مُهِينَا", "holding cheap", "hor gören»e")),
  JP("فِيهَا", "fi", "هَا", n=N3(MT("مُهِينَا", "holding cheap", "hor gören»e"), ZW("أَيْ فِي شُرْبِهَا", "that is, in drinking it", "yani onu içmekte"))),
  R("hal", "مُهِينَا", "muhin-amr", g=["ism-fail"], n=N3(TANW_ALIF, NT("صَاحِبُهَا مَوْصُوفُ «اللَّحِزَ» الْمَحْذُوفُ", "of the omitted noun that «narrow-chested» describes", "«dar göğüslü»nün mahzûf mevsûfunun hâli"), DR("وَإِنْ كَانَتْ «تَرَى» عِلْمِيَّةً فَهُوَ مَفْعُولٌ بِهِ ثَانٍ", "if «see» is the seeing of the mind, it is the second object", "«görürsün» kalbî fiil sayılırsa ikinci mef'ûldür")))])
VV(5, "You turned the cup away from us, Umm ʿAmr, though the cup's course was to the right.",
  "Kadehi bizden çevirdin, ey Ümmü Amr; oysa kadehin yolu sağdandı.",
 [V("mti", "صَبَنْتِ", "sabana-amr", n=N3(CL("ist"), ZW("الصَّبْنُ: الصَّرْفُ؛ وَكَانَ مَجْرَى الْكَأْسِ عَلَى الْيَمِينِ فَأَجْرَيْتِهَا عَلَى الْيَسَارِ", "صَبْن is turning away; the cup's course was to the right, and you sent it round to the left", "«sabn»: çevirmek; kadehin yolu sağdandı, sen onu soldan dolaştırdın"), DR("وَرِوَايَتُهُ: «صَدَدْتِ»", "his text reads «صَدَدْتِ»", "onun rivayeti «sadadti»dir"))),
  R("maf", "الْكَأْسَ", "kas"),
  JP("عَنَّا", "an", "نَا", n=MT("صَبَنْتِ", "turned away", "çevirdin»e"))] + UMM_AMR(),
 [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "al-hal-jumla-wa-rabituha", "al-fail-al-muzhar-wa-tanith-amilih"],
    "الْوَاوُ حَالِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَذُكِّرَ لِأَنَّ تَأْنِيثَ «الْكَأْسِ» مَجَازِيٌّ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الْكَأْسَ» الْأُولَى، وَالرَّابِطُ الْوَاوُ وَإِعَادَةُ «الْكَأْسِ» بِلَفْظِهَا (الدُّرَّةُ).",
    "The waw opens a hal clause; كَانَ is a defective past verb built on fatha, left masculine because «cup» is feminine only in grammar; the clause is a hal of the first «cup», in the seat of nasb, tied by the waw and by «cup» repeated (al-Durra).",
    "Vâv hâliyyedir; «kâne» fetha üzere mebnî nâkıs mâzî; «ke's»in müennesliği mecâzî olduğu için müzekker gelmiştir; cümle ilk «kadeh»ten hâl, mahallen mansûb; râbıt vâv ve «ke's»in aynen tekrarıdır (Dürre).", segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  R("ismk", "الْكَأْسُ", "kas"),
  R("mub", "مَجْرَاهَا", "majra", enc="هَا", sign=S_AR, n=DR("وَقِيلَ: بَدَلُ اشْتِمَالٍ مِنَ «الْكَأْسُ»، وَ«الْيَمِينَا» ظَرْفٌ مُتَعَلِّقٌ بِخَبَرِ «كَانَ»", "some make it a badal of inclusion from «the cup», with «to the right» an adverb hanging on the predicate of كَانَ", "«kadeh»ten bedel-i iştimâl de denmiştir; o zaman «sağdan» «kâne»nin haberine müteallik zarftır")),
  R("zarfm", "الْيَمِينَا", "yamin", n=N3(ITLAQ, (" — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَإِ، وَجُمْلَةُ «مَجْرَاهَا الْيَمِينَا» فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ»", " — it hangs on the omitted khabar of the mubtada, and «its course (was) to the right» is the predicate of كَانَ, in the seat of nasb", " — mübtedânın mahzûf haberine müteallik; «yolu sağdan» cümlesi «kâne»nin haberi, mahallen mansûb")))])
VV(6, "Yet your companion whom you do not serve the morning draught is not the worst of the three, Umm ʿAmr.",
  "Ey Ümmü Amr, sabah şarabı sunmadığın arkadaşın, o üçün en kötüsü değildir.",
 [PT("وَمَا", "ma-hijaziyya", "مَا نَافِيَةٌ حِجَازِيَّةٌ تَعْمَلُ عَمَلَ «لَيْسَ»", "مَا, the Ḥijāzī negative that works like لَيْسَ", "«leyse» gibi amel eden Hicâzî nefy «mâ»sı", c="wi", g=["ma-la-mushabbaha"]),
  R("isml", "شَرُّ", "sharr", mud=True, g=["ism-tafdil"], n=NT("وَهُوَ اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ (أَشَرُّ)", "it is an elative whose hamza is dropped (أَشَرّ)", "hemzesi düşmüş ism-i tafdîldir (eşerr)")),
  R("mdf", "الثَّلَاثَةِ", "thalatha")] + UMM_AMR(NT("وَجُمْلَةُ النِّدَاءِ مُعْتَرِضَةٌ بَيْنَ اسْمِ «مَا» وَخَبَرِهَا", "the call stands between the noun of مَا and its predicate", "nidâ cümlesi «mâ»nın ismi ile haberi arasında mu'tarızadır")),
 [R("khbma", "بِصَاحِبِكِ", "sahib", j="biz", enc="كِ", sign=("بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", " by a fatha that is only estimated, the place being taken by the vowel of the extra jarr letter", " — zâid cer harfinin harekesi yeri işgal ettiği için takdîrî fetha ile"), g=["huruf-al-ziyada-fil-kafiya"],
    n=ZW("أَيْ لَسْتُ شَرَّ أَصْحَابِي، فَكَيْفَ أَخَّرْتِنِي وَتَرَكْتِ سَقْيِي الصَّبُوحَ؟", "that is, I am not the worst of my companions, so why did you put me last and leave me without the morning draught?", "yani ben arkadaşlarımın en kötüsü değilim; beni neden sona bıraktın da sabah şarabını bana sunmadın?")),
  T("الَّذِي", "alladhi", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«صَاحِبِكِ» عَلَى لَفْظِهِ.", "A relative noun built on sukun, in the seat of jarr as an adjective of «your companion», following its outward case.", "Sükûn üzere mebnî ism-i mevsûl, lafzına göre «arkadaşın»ın na'tı olarak mahallen mecrûr."),
  LA_N(),
  V("d5y", "تَصْبَحِينَا", "sabaha", n=N3(ITLAQ, CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: لَا تَصْبَحِينَهُ", "the pronoun that returns to the relative is left out: «whom you do not serve»", "mevsûle dönen zamir mahzûftur: «ona sunmadığın»")))])
VV(7, "Many a cup I have drunk in Baʿlabakk, and another in Damascus and Qāṣirīn.",
  "Nice kadehler içtim Ba'lebekk'te, bir başkasını da Dımaşk'ta ve Kâsırîn'de.",
 [R("mub", "وَكَأْسٍ", "kas", c="wr", sign=("بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ «رُبَّ» الْمَحْذُوفَةِ، وَهِيَ حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ", " by a damma that is only estimated, the place being taken by the kasra of the omitted رُبَّ, a jarr letter like an extra one", " — mahzûf «rubbe»nin (zâide benzeyen cer harfi) harekesi yeri işgal ettiği için takdîrî damme ile"), g=["al-lam-wa-rubba-fil-kafiya"],
    n=N3(NT("وَخَبَرُهُ مَحْذُوفٌ", "its khabar is left out", "haberi mahzûftur"), DR("وَيَجُوزُ أَنْ يَكُونَ مَفْعُولًا بِهِ مُقَدَّمًا لِـ«شَرِبْتُ»", "it may also be the fronted object of «I drank»", "«içtim»in öne alınmış mef'ûlü de olabilir"), ZW("يَقُولُ: وَرُبَّ كَأْسٍ شَرِبْتُهَا بِهٰذِهِ الْبَلْدَةِ", "he says: many a cup I drank in this town", "der ki: nice kadehi bu beldede içtim"))),
  QAD(),
  V("mtu", "شَرِبْتُ", "shariba", n=NT("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«كَأْسٍ»، وَالرَّابِطُ مَحْذُوفٌ: شَرِبْتُهَا", "the clause is an adjective of «cup», in the seat of jarr, its tie left out: «drank it»", "cümle «kadeh»in na'tı, mahallen mecrûr; râbıt mahzûftur: «onu içtim»")),
  R("majr", "بِبَعْلَبَكٍّ", "balabakk", pos="propn", j="bi", sign=("بِالْكَسْرَةِ، وَصُرِفَ لِلضَّرُورَةِ، وَحَقُّهُ الْمَنْعُ لِلْعَلَمِيَّةِ وَالتَّرْكِيبِ الْمَزْجِيِّ (الدُّرَّةُ)", " — by the kasra: it is declined (ṣurifa) for the metre's need, though by right a diptote, a proper name fused from two (al-Durra)", " — kesre ile; vezin zarureti için munsarif kılınmıştır, aslında alem ve mezcî terkip olduğu için gayr-i munsariftir (Dürre)"), g=["mamnu-min-sarf"], n=MT("شَرِبْتُ", "drank", "içtim»e"))],
 [R("atfj", "وَأُخْرَى", "ukhra", c="w", sign=S_AJ, of=("كَأْسٍ", "cup", "kadeh"), n=NT("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: وَكَأْسٍ أُخْرَى", "it is the adjective of an omitted noun: «and another cup»", "mahzûf bir mevsûfun sıfatıdır: «ve başka bir kadeh»")),
  PR("فِي", "fi", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «بِبَعْلَبَكٍّ» مُتَعَلِّقَانِ بِـ«شَرِبْتُ»", "the phrase is joined to «in Baʿlabakk» and hangs on «I drank»", "câr-mecrûr «Ba'lebekk'te»ye ma'tûf, «içtim»e müteallik")),
  R("majr", "دِمَشْقَ", "dimashq", pos="propn", sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — by the fatha that stands for the kasra: a diptote, a proper name of a (feminine) town", " — özel isim ve müennes (belde adı) olduğu için gayr-i munsarif: kesre yerine fetha ile"), g=["mamnu-min-sarf"]),
  R("atfj", "وَقَاصِرِينَا", "qasirin-amr", pos="propn", c="w", of=("دِمَشْقَ", "Damascus", "Dımaşk"), g=["mamnu-min-sarf"], sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ (الدُّرَّةُ)، وَالْأَلِفُ لِلْإِطْلَاقِ", " — by the fatha that stands for the kasra: a diptote, a foreign proper name (al-Durra); the final alif is the alif of iṭlāq", " — yabancı özel isim olduğu için gayr-i munsarif: kesre yerine fetha ile (Dürre); sondaki elif ıtlâk elifidir"))])
VV(8, "And we — the fated deaths will overtake us, decreed for us, and we decreed for them.",
  "Biz ise — ölümler bize mutlaka yetişecek; onlar bizim için takdir edilmiştir, biz de onlar için takdir edilmişiz.",
 [INNA("وَإِنَّا", enc="نَا", c="wi", n=DR("وَأَصْلُهُ «إِنَّنَا»، حُذِفَتْ إِحْدَى النُّونَاتِ لِلتَّخْفِيفِ", "its root form is إِنَّنَا, one nun dropped for ease", "aslı «innenâ»dır; hafiflik için nûnlardan biri düşmüştür")),
  PT("سَوْفَ", "sawfa", "حَرْفُ اسْتِقْبَالٍ وَتَسْوِيفٍ لَا عَمَلَ لَهُ", "a particle of the (far) future; it governs nothing", "istikbal (teswîf) harfi, ameli yoktur"),
  V("d", "تُدْرِكُنَا", "adraka", enc="نَا", g=["form-iv-verbs"], n=CL("khb", "إِنَّ", "إِنَّ", "inne")),
  R("fail", "الْمَنَايَا", "maniyya", sign=S_AR, g=["jam-taksir"], n=ZW("الْمَنَايَا: جَمْعُ الْمَنِيَّةِ، وَهِيَ تَقْدِيرُ الْمَوْتِ", "مَنَايَا is the plural of مَنِيَّة, the decree of death", "«menâyâ», ölümün takdiri olan «meniyye»nin cem'idir"))],
 [R("hal", "مُقَدَّرَةً", "muqaddar", g=["ism-maful"], n=NT("صَاحِبُهَا «الْمَنَايَا»", "of «the fated deaths»", "«ölümler»in hâli")),
  JP("لَنَا", "li", "نَا", n=MT("مُقَدَّرَةً", "decreed", "takdir edilmiş»e")),
  R("atfn", "وَمُقَدَّرِينَا", "muqaddar", c="w", of=("مُقَدَّرَةً", "decreed", "takdir edilmiş"), sign=S_JMSI, g=["jam-mudhakkar-salim"], n=DR("وَهُوَ فِي الْمَعْنَى حَالٌ مِنْ «نَا» فِي «تُدْرِكُنَا»، وَمُتَعَلَّقُهُ مَحْذُوفٌ: وَمُقَدَّرِينَ لَهَا", "in meaning it is a hal of «us» in «will overtake us», and what it hangs on is left out: «and decreed for them»", "anlamca «bize yetişecek»teki «bize»den hâldir; taalluku mahzûftur: «ve onlar için takdir edilmiş»"))])
# ---- vv. 9–15 — قِفِي قَبْلَ التَّفَرُّقِ ----
S_DIPT_AF = (S_DIPT[0] + " لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", S_DIPT[1] + " (the feminine alif mamduda)", S_DIPT[2] + " (memdûde te'nîs elifi sebebiyle)")
JWT = lambda v_ar, v_en, v_tr: JZ("فِي جَوَابِ الْأَمْرِ", "in answer to the command", "emrin cevabı olarak")
JWT_N = NT("وَجَزْمُهُ عِنْدَ الْجُمْهُورِ بِشَرْطٍ مَحْذُوفٍ: إِنْ تَقِفِي …؛ وَالْجُمْلَةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "most hold it in jazm by an omitted condition, «if you stay …»; the clause has no seat of its own", "cumhura göre mahzûf bir şartla meczûmdur: «durursan …»; cümlenin i'râbda mahalli yoktur")
WOMAN = HIYA("الْمَرْأَةِ", "the woman", "kadına")
VV(9, "Stay before we part, O lady of the litter: we shall tell you the certain truth, and you shall tell us.",
  "Ayrılmadan önce dur, ey hevdeçteki kadın: sana kesin olanı haber verelim, sen de bize haber ver.",
 [V("a5y", "قِفِي", "waqafa", g=["mithal-verbs"], n=N3(CL("ibt"), ZW("قِفِي مَطِيَّتَكِ أَيَّتُهَا الْحَبِيبَةُ الظَّاعِنَةُ", "stop your mount, O departing beloved", "ey göçüp giden sevgili, bineğini durdur"))),
  R("zarfz", "قَبْلَ", "qabla", mud=True, n=MZ("قِفِي", "stay", "dur»a")),
  R("mdf", "التَّفَرُّقِ", "tafarruq-amr", g=["masdar"]),
  PT("يَا", "ya-nida", "حَرْفُ نِدَاءٍ", "the particle of calling", "nidâ harfi", g=["vocative-munada"]),
  T("ظَعِينَا", "zaina", "noun", ["vocative-munada"], "مُنَادًى مُرَخَّمٌ — أَصْلُهُ «يَا ظَعِينَةُ» — مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْحَرْفِ الْمَحْذُوفِ (التَّاءِ) عَلَى لُغَةِ مَنْ يَنْتَظِرُ، فِي مَحَلِّ نَصْبٍ، وَالْأَلِفُ لِلْإِطْلَاقِ؛ وَجُمْلَةُ النِّدَاءِ مُعْتَرِضَةٌ بَيْنَ الْأَمْرِ وَجَوَابِهِ (الدُّرَّةُ) — الظَّعِينَةُ: الْمَرْأَةُ فِي الْهَوْدَجِ، فَعِيلَةٌ بِمَعْنَى فَاعِلَةٍ (الزَّوْزَنِيُّ).",
    "A shortened vocative (tarkhim) — in full «يَا ظَعِينَةُ» — built on a damma estimated on the dropped letter (the ta), as those say who keep the word's last vowel in view; in the seat of nasb; the final alif is the alif of iṭlāq; the call stands between the command and its answer (al-Durra) — ظَعِينَة is a woman in her litter, a فَعِيلَة in the sense of an active participle (al-Zawzanī).",
    "Terhîm edilmiş münâdâ — aslı «yâ za'înetu» — düşen harf (tâ) üzerinde takdîrî damme üzere mebnî (son harfi bekleyenlerin lügatine göre), mahallen mansûb; sondaki elif ıtlâk elifidir; nidâ cümlesi emir ile cevabı arasında mu'tarızadır (Dürre) — «za'îne»: hevdeçteki kadın; fâile anlamında fa'île (Zevzenî).")],
 [V(JWT(0, 0, 0), "نُخَبِّرْكِ", "khabbara", enc="كِ", encrole="maf1", doer=NAHNU, g=["form-ii-verbs", "jawab-al-talab", "mafulayn"], n=JWT_N),
  R("maf2", "الْيَقِينَ", "yaqin"),
  V(JZ("لِعَطْفِهِ عَلَى «نُخَبِّرْكِ»", "being joined to «we shall tell you»", "«haber verelim»e atfedildiği için", sign="nun"), "وَتُخْبِرِينَا", "akhbara", c="w", enc="نَا", encrole="maf1", g=["form-iv-verbs", "afal-khamsa", "fail", "mafulayn", "hadhf-al-maful"],
    n=N3(Y5, NT("وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ لِدَلَالَةِ مَا قَبْلَهُ عَلَيْهِ (الدُّرَّةُ)", "the second object is left out, shown by what goes before (al-Durra)", "ikinci mef'ûl, öncesi delâlet ettiği için mahzûftur (Dürre)")))])
VV(10, "Stay, that we may ask you: did you make a break because of the swiftness of parting, or did you betray the one who trusted you?",
  "Dur da sana soralım: ayrılığın çabukluğu yüzünden bağı mı kopardın, yoksa sana güvenene mi ihanet ettin?",
 [V("a5y", "قِفِي", "waqafa", g=["mithal-verbs"], n=CL("ibt")),
  V(JWT(0, 0, 0), "نَسْأَلْكِ", "saala", enc="كِ", encrole="maf1", doer=NAHNU, g=["jawab-al-talab", "mafulayn"], n=JWT_N),
  PT("هَلْ", "hal-istifham", "حَرْفُ اسْتِفْهَامٍ لَا عَمَلَ لَهُ؛ وَجُمْلَةُ «هَلْ أَحْدَثْتِ صَرْمًا» فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ«نَسْأَلْ»، عُلِّقَ عَنْهَا الْفِعْلُ لَفْظًا بِالِاسْتِفْهَامِ (الدُّرَّةُ)", "a particle of question that governs nothing; «did you make a break» is the second object of «we ask», the verb held back from it in form by the question (al-Durra)", "soru harfi, ameli yoktur; «bağı mı kopardın» cümlesi «soralım»ın ikinci mef'ûlü olarak mahallen mansûbdur; fiil, soru sebebiyle lafzen amelden alıkonmuştur (Dürre)", g=["al-istifham"]),
  V("mti", "أَحْدَثْتِ", "ahdatha", g=["form-iv-verbs"]),
  R("maf", "صَرْمًا", "sarm", n=ZW("الصَّرْمُ: الْقَطِيعَةُ", "صَرْم is breaking off", "«sarm»: ilişkiyi kesmek"))],
 [R("majr", "لِوَشْكِ", "washk-amr", j="li", mud=True, n=N3(MT("صَرْمًا", "a break", "kopuş»a"), NT("لِأَنَّهُ مَصْدَرٌ (الدُّرَّةُ)", "for it is a masdar (al-Durra)", "çünkü masdardır (Dürre)"), ZW("الْوَشْكُ: السُّرْعَةُ", "وَشْك is swiftness", "«veşk»: çabukluk"))),
  R("mdf", "الْبَيْنِ", "bayn-parting", n=DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti")),
  PT("أَمْ", "am", "حَرْفُ عَطْفٍ؛ وَجُمْلَةُ «خُنْتِ الْأَمِينَا» مَعْطُوفَةٌ عَلَى جُمْلَةِ «هَلْ أَحْدَثْتِ صَرْمًا» فَهِيَ فِي مَحَلِّ نَصْبٍ مِثْلُهَا (الدُّرَّةُ)", "a conjunction; «did you betray the trusting one» is joined to «did you make a break» and is in the seat of nasb like it (al-Durra)", "atıf harfi; «güvenene ihanet ettin» cümlesi «bağı mı kopardın» cümlesine ma'tûftur, onun gibi mahallen mansûbdur (Dürre)", g=["aw-imma-am-la-bal-lakin-fil-kafiya"]),
  V("mti", "خُنْتِ", "khana", g=["hollow-verbs"]),
  R("maf", "الْأَمِينَا", "amin", n=N3(ITLAQ, ZW("الْأَمِينُ بِمَعْنَى الْمَأْمُونِ: حَبِيبُكِ الَّذِي تُؤْمَنُ خِيَانَتُهُ", "أَمِين here means «the one trusted»: your lover, from whom no betrayal is feared", "«emîn» burada «kendisine güvenilen» demektir: ihanetinden emin olunan sevgilin")))])
VV(11, "— of a day of hateful war, of striking and thrusting, in which your kinsmen made their eyes glad.",
  "— savaşın çirkin bir gününü, vuruşu ve mızrak saplamasıyla; o gün amca oğulların gözlerini aydın ettiler.",
 [R("majr", "بِيَوْمِ", "yawm", j="bi", mud=True, n=N3(MT("نُخَبِّرْكِ", "we shall tell you", "haber verelim»e"), DR("وَقِيلَ: بِـ«قِفِي»", "some hang it on «stay»", "«dur»a müteallik diyenler de vardır"))),
  R("mdf", "كَرِيهَةٍ", "kariha-amr", n=ZW("الْكَرِيهَةُ مِنْ أَسْمَاءِ الْحَرْبِ، سُمِّيَتْ لِأَنَّ النُّفُوسَ تَكْرَهُهَا", "كَرِيهَة is one of the names of war, so called because souls hate it", "«kerîhe» savaşın adlarındandır; nefisler ondan hoşlanmadığı için böyle denmiştir")),
  R("mutlaq", "ضَرْبًا", "darb", n=NT("لِفِعْلٍ مَحْذُوفٍ: يُضْرَبُ فِيهِ ضَرْبًا (الزَّوْزَنِيُّ)", "of an omitted verb: «there is striking in it» (al-Zawzanī)", "mahzûf bir fiilin: «o günde vurulur» (Zevzenî)")),
  R("atfn", "وَطَعْنًا", "tan", c="w", of=("ضَرْبًا", "striking", "vuruş"))],
 [V("m", "أَقَرَّ", "aqarra", g=["form-iv-verbs", "doubled-verbs", "kinaya", "aqsam-al-kinaya"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِـ«طَعْنًا»، وَحُذِفَتْ صِفَةُ «ضَرْبًا» لِدَلَالَةِ هٰذِهِ عَلَيْهَا", "the clause is an adjective of «thrusting», in the seat of nasb; the adjective of «striking» is left out, this one showing it", "cümle «saplama»nın sıfatı, mahallen mansûb; «vuruş»un sıfatı, bu ona delâlet ettiği için hazfedilmiştir"),
    (" — وَفِيهِ كِنَايَةٌ عَنِ الظَّفَرِ بِالْبُغْيَةِ، وَصَفَهَا الزَّوْزَنِيُّ: «لِأَنَّ الْمُتَرَقِّبَ لِلشَّيْءِ يَطْمَحُ بِبَصَرِهِ إِلَيْهِ، فَإِذَا ظَفِرَ بِهِ قَرَّتْ عَيْنُهُ عَنِ الطُّمُوحِ إِلَيْهِ»؛ أَيْ فَازُوا بِبُغْيَتِهِمْ مِنْ قَهْرِ الْأَعْدَاءِ",
     " — a kināya for winning what one sought, which al-Zawzanī describes: «one who waits for a thing strains his eyes towards it, and when he wins it his eye settles and stops straining»: that is, they won what they sought, the crushing of the enemy",
     " — arzulanana kavuşmaktan kinâyedir; Zevzenî tarif eder: «bir şeyi bekleyen gözünü ona diker; ona kavuşunca gözü dikilmekten durulur»: yani düşmanı ezmek gibi dileklerine kavuştular"))),
  JP("بِهِ", "bi", "هِ", n=N3(MT("أَقَرَّ", "made glad", "aydın etti»ye"), NT("وَالْهَاءُ لِلْيَوْمِ", "the ha refers to the day", "hâ güne döner"))),
  R("fail", "مَوَالِيكِ", "mawla", enc="كِ", sign=("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " — by a damma estimated on the ya", " — yâ üzerinde takdîrî damme ile"), g=["jam-taksir"], n=ZW("أَيْ بَنُو أَعْمَامِكِ", "that is, your cousins", "yani amca oğulların")),
  R("maf", "الْعُيُونَا", "ayn-eye", g=["jam-taksir"], n=N3(ITLAQ, DR("وَيَجُوزُ أَنْ يَكُونَ تَمْيِيزًا", "it may also be a tamyiz", "temyîz de olabilir")))])
VV(12, "For tomorrow, and today, and the day after tomorrow are pledged to what you do not know.",
  "Çünkü yarın da, bugün de, yarından sonraki gün de bilmediğin şeylere rehindir.",
 [INNA("وَإِنَّ", c="wi"),
  R("ismi", "غَدًا", "ghad", n=DR("وَخَبَرُهُ مَحْذُوفٌ لِدَلَالَةِ خَبَرِ الثَّانِيَةِ عَلَيْهِ", "its predicate is left out, shown by the predicate of the second إِنَّ", "haberi, ikinci «inne»nin haberi delâlet ettiği için mahzûftur")),
  INNA("وَإِنَّ", c="w", n=DR("وَيَجُوزُ أَنْ تَكُونَ زَائِدَةً مُؤَكِّدَةً لَا عَمَلَ لَهَا", "it may also be an extra, emphasising إِنَّ that governs nothing", "amelsiz, te'kîd için zâid «inne» de olabilir")),
  R("ismi", "الْيَوْمَ", "yawm"),
  R("khbi", "رَهْنٌ", "rahn", g=TB, n=N3(ZW("أَيْ إِنَّ الْأَيَّامَ رَهْنٌ بِمَا لَا يُحِيطُ عِلْمُكِ بِهِ، أَيْ مُلَازِمَةٌ لَهُ", "that is, the days are pledged to what your knowledge does not take in — bound fast to it", "yani günler, bilginin kuşatmadığı şeylere rehindir, ona bağlıdır"),
    HADD("تَشْبِيهٌ بَلِيغٌ: الْمُشَبَّهُ الْأَيَّامُ (غَدٌ وَالْيَوْمُ وَبَعْدَ غَدٍ)، وَالْمُشَبَّهُ بِهِ الرَّهْنُ، حُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ، وَوَجْهُهُ الْمُلَازَمَةُ كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "a tashbih baligh: the days (tomorrow, today, the day after) are likened to a pledge, with both the particle and the point of likeness left out; the point is being bound fast, as al-Zawzanī explains", "teşbîh-i belîğ: müşebbeh günler (yarın, bugün, öbür gün), müşebbehün bih rehin; edat ve vech-i şebeh hazfedilmiştir; vech, Zevzenî'nin açıkladığı gibi bağlı kalmaktır")))],
 [R("atfn", "وَبَعْدَ", "bada", c="w", mud=True, of=("غَدًا", "tomorrow", "yarın"), n=DR("مَعْطُوفٌ عَلَى اسْمِ «إِنَّ»", "joined to the noun of إِنَّ", "«inne»nin ismine ma'tûf")),
  R("mdf", "غَدٍ", "ghad"),
  T("بِمَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَهْنٌ» لِأَنَّهُ مَصْدَرٌ (الدُّرَّةُ) — أَيْ بِمَا لَا تَعْلَمِينَ مِنَ الْحَوَادِثِ (الزَّوْزَنِيُّ).",
    "The ba is a jarr letter; مَا is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «pledged», a masdar (al-Durra) — that is, to the events you do not know (al-Zawzanī).",
    "Bâ cer harfi; «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr masdar olan «rehin»e müteallik (Dürre) — yani bilmediğin hâdiselere (Zevzenî).", segs=SG(("بِ", "bi", "prep"), ("مَا", "ma-mawsula", "pron"))),
  LA_N(),
  V("d5y", "تَعْلَمِينَا", "alima", n=N3(ITLAQ, CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: بِمَا لَا تَعْلَمِينَهُ", "the pronoun returning to the relative is left out: «what you do not know (of it)»", "mevsûle dönen zamir mahzûftur: «bilmediğin şey»")))])
VV(13, "She shows you, when you come in to her where none are by and she is safe from the eyes of those who nurse a hidden enmity, —",
  "Yanına kimsenin bulunmadığı bir anda girdiğinde, düşmanlığını içinde gizleyenlerin gözlerinden emin olarak sana gösterir —",
 [V("dy", "تُرِيكَ", "ara", enc="كَ", encrole="maf1", doer=WOMAN, g=["form-iv-verbs", "mafulayn", "iltifat"], n=N3(CL("ist"), ZW("تُرِيكَ هٰذِهِ الْمَرْأَةُ إِذَا أَتَيْتَهَا خَالِيَةً", "this woman shows you, when you come to her alone", "bu kadın, ona yalnızken vardığında sana gösterir"),
    HADD("الْتِفَاتٌ مِنَ الْخِطَابِ إِلَى الْغَيْبَةِ: كَانَ يُخَاطِبُهَا («قِفِي … لَا تَعْلَمِينَا») ثُمَّ أَخْبَرَ عَنْهَا بِضَمِيرِ الْغَائِبَةِ فِي «تُرِيكَ»، وَالْمُرَادُ وَاحِدٌ", "an iltifat from address to the third person: he was speaking to her («stay … you do not know»), then tells of her as «she» in «she shows you», the one meant being the same", "hitaptan gaybete iltifât: ona hitap ediyordu («dur … bilmediğin»), sonra «sana gösterir»de ondan gâib zamiriyle haber verdi; kastedilen aynıdır"))),
  IDHA(plain=True, n=MZ("تُرِيكَ", "shows you", "gösterir»e")),
  V("mta", "دَخَلْتَ", "dakhala", n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  PR("عَلَى", "ala", n=MT("دَخَلْتَ", "come in", "girdin»e")),
  R("majr", "خَلَاءٍ", "khala-amr")],
 [QAD("وَقَدْ", c="wh"),
  V("mt", "أَمِنَتْ", "amina", doer=WOMAN, n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ تَاءِ «دَخَلْتَ»، وَالرَّابِطُ الْوَاوُ", "the clause is a hal of the ta of «you come in», in the seat of nasb, tied by the waw", "cümle «girdin»deki tâdan hâl, mahallen mansûb; râbıt vâvdır")),
  R("maf", "عُيُونَ", "ayn-eye", mud=True, g=["jam-taksir"]),
  R("mdf", "الْكَاشِحِينَا", "kashih-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"], n=ZW("الْكَاشِحُ: الْمُضْمِرُ الْعَدَاوَةَ فِي كَشْحِهِ", "a كَاشِح is one who hides enmity in his flank", "«kâşih»: düşmanlığı böğründe gizleyen"))])
VV(14, "the two forearms of a long-necked, white, young she-camel, pure white in colour, whose womb has never held a young one;",
  "uzun boyunlu, beyaz, genç bir dişi devenin iki kolunu — rengi halis beyaz, rahmi hiç yavru taşımamış;",
 [R("maf2", "ذِرَاعَيْ", "dhira", mud=True, sign=S_MUTHM, g=["al-muthanna", "istiara", "arkan-al-istiara"], n=N3(NT("لِـ«تُرِي» فِي الْبَيْتِ قَبْلَهُ", "of «shows» in the verse before", "önceki beyitteki «gösterir»in"),
    (" — وَفِيهِ تَشْبِيهٌ وَصَفَهُ الزَّوْزَنِيُّ: «تُرِيكَ ذِرَاعَيْنِ مُمْتَلِئَتَيْنِ لَحْمًا كَذِرَاعَيْ نَاقَةٍ طَوِيلَةٍ»؛ وَهُوَ — عَلَى حَدِّ التَّلْخِيصِ — اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: ذُكِرَ الْمُشَبَّهُ بِهِ (ذِرَاعَا النَّاقَةِ) وَطُوِيَ الْمُشَبَّهُ (ذِرَاعَاهَا)، وَالْقَرِينَةُ «تُرِيكَ»",
     " — a likening that al-Zawzanī describes: «she shows you two forearms full of flesh like the forearms of a tall she-camel»; by the Talkhīṣ's definition it is an istiʿāra taṣrīḥiyya: what she is likened to (the camel's forearms) is named and what is likened (her own arms) folded away, «she shows you» being the sign",
     " — Zevzenî'nin tarif ettiği bir benzetme: «sana uzun bir devenin kolları gibi etle dolu iki kol gösterir»; Telhîs'in tarifine göre istiâre-i tasrîhiyyedir: müşebbehün bih (devenin kolları) zikredilmiş, müşebbeh (onun kolları) dürülmüştür; karîne «sana gösterir»dir"))),
  R("mdf", "عَيْطَلٍ", "aytal-amr", g=["hadhf-wa-taqdir"], n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: نَاقَةٍ عَيْطَلٍ", "it is the adjective of an omitted noun: «a long-necked she-camel»", "mahzûf bir mevsûfun sıfatıdır: «uzun boyunlu bir dişi deve»"), ZW("الْعَيْطَلُ: الطَّوِيلَةُ الْعُنُقِ مِنَ النُّوقِ", "عَيْطَل is a long-necked she-camel", "«aytal»: uzun boyunlu dişi deve"))),
  R("naatj", "أَدْمَاءَ", "adma-amr", sign=S_DIPT_AF, g=["mamnu-min-sarf"], n=ZW("الْأَدْمَاءُ: الْبَيْضَاءُ مِنْهَا؛ وَالْأُدْمَةُ الْبَيَاضُ فِي الْإِبِلِ", "أَدْمَاء is a white one; أُدْمَة is whiteness in camels", "«edmâ»: beyaz olanı; «üdme» develerde beyazlıktır")),
  R("naatj", "بِكْرٍ", "bikr", n=ZW("الْبِكْرُ: النَّاقَةُ الَّتِي حَمَلَتْ بَطْنًا وَاحِدًا؛ وَيُرْوَى «بَكْرٍ» بِفَتْحِ الْبَاءِ، وَهُوَ الْفَتِيُّ مِنَ الْإِبِلِ، وَالْكَسْرُ أَعْلَى الرِّوَايَتَيْنِ", "بِكْر is a she-camel that has carried one young; it is also read بَكْر, a young camel, but the kasra is the better reading", "«bikr»: bir kez gebe kalmış dişi deve; «bekr» diye de okunur — genç deve; kesreli okuyuş daha üstündür"))],
 [R("naatj", "هِجَانِ", "hijan-amr", mud=True, g=["idafa-lafziyya"], n=N3(ZW("الْهِجَانُ: الْأَبْيَضُ الْخَالِصُ الْبَيَاضِ، يَسْتَوِي فِيهِ الْوَاحِدُ وَالتَّثْنِيَةُ وَالْجَمْعُ", "هِجَان is pure white; it is the same for one, two and many", "«hicân»: halis beyaz; tekil, ikil ve çoğulda aynıdır"),
    DR("وَرِوَايَتُهُ مَكَانَ الشَّطْرِ: «تَرَبَّعَتِ الْأَجَارِعَ وَالْمُتُونَا»، وَهِيَ رِوَايَةٌ ذَكَرَهَا الزَّوْزَنِيُّ أَيْضًا؛ وَإِضَافَةُ «هِجَانِ» إِلَى «اللَّوْنِ» مِنْ إِضَافَةِ الْوَصْفِ إِلَى فَاعِلِهِ", "his text has in this hemistich «she has grazed the spring pastures of the sand-hills and the high grounds», a reading al-Zawzanī also gives; «pure white of colour» annexes the adjective to its doer", "onun rivayetinde bu mısra «kum tepelerinde ve sırtlarda baharı otlayarak geçirdi» şeklindedir; Zevzenî de bu rivayeti zikreder; «hicân»ın «levn»e izâfeti, vasfın fâiline izâfetidir"))),
  R("mdf", "اللَّوْنِ", "lawn"),
  LAM(),
  V(JZ("بِـ«لَمْ»", "by لَمْ", "«lem» ile"), "تَقْرَأْ", "qaraa", doer=HIYA("الْعَيْطَلِ", "the she-camel", "dişi deveye"), n=N3(DR("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنَ الْمَوْصُوفِ الْمَحْذُوفِ", "the clause can be an adjective or a hal of the omitted noun", "cümle mahzûf mevsûfun sıfatı da hâli de olabilir"), ZW("لَمْ تَقْرَأْ جَنِينًا: لَمْ تَضُمَّ فِيهِ رَحِمُهَا وَلَدًا", "لَمْ تَقْرَأْ جَنِينًا: her womb has never held a young one", "«lem takra' cenînen»: rahmi hiç yavru taşımadı"))),
  R("maf", "جَنِينًا", "janin", n=TANW_ALIF)])
VV(15, "and a breast like a casket of ivory, soft, guarded from the hands of those who would touch it.",
  "ve fildişi bir kutu gibi, yumuşak, dokunmak isteyenlerin ellerinden korunmuş bir göğüs.",
 [R("atfn", "وَثَدْيًا", "thady", c="w", of=("ذِرَاعَيْ", "the two forearms", "iki kol"), n=NT("فِي الْبَيْتِ قَبْلَهُ", "in the verse before", "önceki beyitte")),
  R("naatn", "مِثْلَ", "mithl", mud=True, of=("ثَدْيًا", "a breast", "göğüs"), g=TB, n=(" — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الثَّدْيُ، وَالْمُشَبَّهُ بِهِ حُقُّ الْعَاجِ، وَالْأَدَاةُ «مِثْلَ»، وَوَجْهُ الشَّبَهِ — الْبَيَاضُ وَالِاسْتِدَارَةُ — ذَكَرَهُ الزَّوْزَنِيُّ وَلَمْ يُذْكَرْ فِي الْبَيْتِ: «مِثْلَ حُقٍّ مِنْ عَاجٍ بَيَاضًا وَاسْتِدَارَةً»", " — a tashbih mursal mujmal: the breast is likened to a casket of ivory; the particle is مِثْلَ; the point of likeness — whiteness and roundness — is named by al-Zawzanī, not in the verse", " — teşbîh-i mürsel mücmel: müşebbeh göğüs, müşebbehün bih fildişi kutu, edat «misle»; vech-i şebeh — beyazlık ve yuvarlaklık — beyitte değil, Zevzenî'de zikredilir")),
  R("mdf", "حُقِّ", "huqq", mud=True),
  R("mdf", "الْعَاجِ", "aj-amr"),
  R("naatn", "رَخْصًا", "rakhs", of=("ثَدْيًا", "a breast", "göğüs"), n=ZW("رَخْصًا: لَيِّنًا", "رَخْص is soft", "«rahs»: yumuşak"))],
 [R("naatn", "حَصَانًا", "hasan-amr", of=("ثَدْيًا", "a breast", "göğüs"), n=N3(DR("وَقِيلَ: حَالٌ مِنَ الضَّمِيرِ فِي «تُرِيكَ»، وَالْأَوَّلُ أَقْوَى مَعْنًى", "some make it a hal of the pronoun in «shows you»; the first is stronger in meaning", "«gösterir»deki zamirden hâl olduğu da söylenmiştir; birincisi mânaca daha kuvvetlidir"), ZW("حَصَانًا: عَفِيفَةً، مُحْرَزَةً مِنْ أَكُفِّ مَنْ يَلْمِسُهَا", "حَصَان is chaste: guarded from the hands of any who would touch it", "«hasân»: iffetli; dokunmak isteyenin elinden korunmuş"))),
  PR("مِنْ", "min", n=MT("حَصَانًا", "guarded", "korunmuş»a")),
  R("majr", "أَكُفِّ", "kaff-hand", mud=True, g=["jam-taksir"]),
  R("mdf", "اللَّامِسِينَا", "lamis-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"])])
# ---- vv. 16–22 — الْوَجْدُ وَالْحُمُولُ ----
QAMA = HIYA("الْقَامَةِ الْمَحْذُوفَةِ", "the omitted «stature»", "mahzûf «boy»a")
NAQA = HIYA("أُمِّ السَّقْبِ", "the calf's mother", "yavrunun annesine")
VV(16, "and the two flanks of a supple stature that has grown up tall and long, whose haunches make her rise heavily with what lies next to them;",
  "ve uzayıp serpilmiş, uzun boylu, yumuşak bir boyun iki yanını; kalçaları, yanlarındaki ile birlikte onu ağır ağır kaldırır;",
 [R("atfn", "وَمَتْنَيْ", "matn", c="w", mud=True, sign=S_MUTHM, g=["al-muthanna"], n=DR("مَعْطُوفٌ عَلَى «ذِرَاعَيْ عَيْطَلٍ»", "joined to «the two forearms of a long-necked she-camel»", "«uzun boyunlu devenin iki kolu»na ma'tûf")),
  R("mdf", "لَدْنَةٍ", "ladn-amr", g=["hadhf-wa-taqdir"], n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("أَيْ وَمَتْنَيْ قَامَةٍ لَدْنَةٍ؛ اللَّدْنُ: اللَّيِّنُ", "that is, the flanks of a supple stature; لَدْن is soft, supple", "yani yumuşak bir boyun iki yanı; «ledn»: yumuşak"))),
  V("mt", "سَمَقَتْ", "samaqa-amr", doer=QAMA, n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "the clause is a second adjective of the omitted noun, in the seat of jarr", "cümle mahzûf mevsûfun ikinci sıfatı, mahallen mecrûr"), ZW("السُّمُوقُ: الطُّولُ", "سُمُوق is height", "«sumûk»: uzunluk"), DR("وَرِوَايَتُهُ: «طَالَتْ وَلَانَتْ»", "his text reads «grew long and soft»", "onun rivayeti «uzadı ve yumuşadı»dır"))),
  V("mt", "وَطَالَتْ", "tala-long", c="w", doer=QAMA, g=["hollow-verbs"], n=CL("atf", "سَمَقَتْ", "grew up tall", "serpildi"))],
 [R("mub", "رَوَادِفُهَا", "radifa-amr", enc="هَا", g=["jam-taksir"], n=ZW("الرَّادِفَتَانِ وَالرَّانِفَتَانِ: فَرْعَا الْأَلْيَتَيْنِ، وَالْجَمْعُ الرَّوَادِفُ", "the two رَادِفَة are the ends of the buttocks; the plural is رَوَادِف", "iki «râdife»: kaba etlerin uçları; cem'i «revâdif»")),
  V("d", "تَنُوءُ", "naa-weigh", doer=HIYA("الرَّوَادِفِ", "the haunches", "kalçalara"), g=["hollow-verbs"], n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ، وَجُمْلَةُ «رَوَادِفُهَا تَنُوءُ» صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ (الدُّرَّةُ)", "the clause is the khabar of the mubtada, in the seat of raf'; «her haunches rise heavily» can be an adjective or a hal (al-Durra)", "cümle mübtedânın haberi, mahallen merfû; «kalçaları ağır ağır kalkar» cümlesi sıfat da hâl de olabilir (Dürre)"), ZW("النَّوْءُ: النُّهُوضُ فِي تَثَاقُلٍ", "نَوْء is rising with heaviness", "«nev'»: ağırlıkla kalkmak"))),
  T("بِمَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَنُوءُ».",
    "The ba is a jarr letter; مَا is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «rise heavily».", "Bâ cer harfi; «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr «ağır ağır kalkar»a müteallik.", segs=SG(("بِ", "bi", "prep"), ("مَا", "ma-mawsula", "pron"))),
  V("mn", "وَلِينَا", "waliya", g=["mithal-verbs", "naqis-verbs"], n=N3(ITLAQ, CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: بِمَا وَلِينَهُ؛ وَالنُّونُ لِلرَّوَادِفِ", "the returning pronoun is left out: «with what they lie next to»; the nun refers to the haunches", "dönen zamir mahzûftur: «yanlarında olanla»; nûn kalçalara döner"), ZW("الْوَلْيُ: الْقُرْبُ، وَالْفِعْلُ وَلِيَ يَلِي", "وَلْي is nearness; the verb is وَلِيَ يَلِي", "«vely»: yakınlık; fiili «veliye yelî»"), DR("وَرِوَايَتُهُ: «بِمَا يَلِينَا»", "his text reads «بِمَا يَلِينَا»", "onun rivayeti «bimâ yelînâ»dır")))])
VV(17, "and a haunch the doorway is too narrow for, and a waist for whose sake I have been driven mad.",
  "ve kapının dar geldiği bir kalça, ve uğruna deli divane olduğum bir bel.",
 [R("atfn", "وَمَأْكَمَةً", "makama-amr", c="w", of=("مَتْنَيْ", "the two flanks", "iki yan"), n=ZW("الْمَأْكَمَةُ وَالْمَأْكِمَةُ: رَأْسُ الْوَرِكِ", "مَأْكَمَة (or مَأْكِمَة) is the top of the hip", "«me'keme» (ve «me'kime»): kalçanın başı")),
  V("d", "يَضِيقُ", "daqa", g=["hollow-verbs", "kinaya", "aqsam-al-kinaya"], n=N3(CL("nn", "مَأْكَمَةً", "a haunch", "kalça»nın"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ عِظَمِ وَرِكِهَا وَامْتِلَائِهَا، بَيَّنَهَا الزَّوْزَنِيُّ: «يَضِيقُ الْبَابُ عَنْهَا لِعِظَمِهَا وَضِخَمِهَا وَامْتِلَائِهَا بِاللَّحْمِ»", " — a kināya for the fullness of her hips, which al-Zawzanī makes plain: «the door is too narrow for it, for its size and bulk and fullness of flesh»", " — kalçasının iriliğinden ve dolgunluğundan kinâyedir; Zevzenî açıklar: «iriliği, hacmi ve etle dolgunluğu yüzünden kapı ona dar gelir»"))),
  R("fail", "الْبَابُ", "bab"),
  JP("عَنْهَا", "an", "هَا", n=MT("يَضِيقُ", "is too narrow", "dar gelir»e"))],
 [R("atfn", "وَكَشْحًا", "kashh", c="w", of=("مَأْكَمَةً", "a haunch", "kalça")),
  QAD(),
  T("جُنِنْتُ", "janna-amr", "verb", ["naib-al-fail", "al-bariz-al-muttasil", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْمُتَكَلِّمِ، وَالتَّاءُ " + _FAN + "، وَفُكَّ الْإِدْغَامُ لِسُكُونِ مَا بَعْدَهُ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِـ«كَشْحًا» (الدُّرَّةُ).",
    "A passive past verb built on sukun because the ta of the speaker is attached; that ta is the deputy doer, in the seat of raf'; the doubling is undone before the quiescent; the clause is an adjective of «a waist», in the seat of nasb (al-Durra).",
    "Meçhul mâzî, mütekellim tâsı bitiştiği için sükûn üzere mebnî; tâ nâib-i fâildir, mahallen merfû; sonrası sâkin olduğu için idgâm çözülmüştür; cümle «bel»in sıfatı, mahallen mansûb (Dürre)."),
  JP("بِهِ", "bi", "هِ", n=N3(MT("جُنِنْتُ", "I was driven mad", "deli oldum»a"), ZW("أَيْ جُنِنْتُ بِحُسْنِهِ", "that is, mad for its beauty", "yani onun güzelliği yüzünden deli oldum"))),
  R("mutlaq", "جُنُونَا", "junun-amr", n=TANW_ALIF)])
VV(18, "and two columns of ivory or marble, whose ornaments' jingle rings out with a ringing.",
  "ve fildişinden yahut mermerden iki sütun; süslerinin şıngırtısı çın çın öter.",
 [R("atfn", "وَسَارِيَتَيْ", "lb-sariya", c="w", mud=True, sign=S_MUTHM, g=["al-muthanna", "istiara", "arkan-al-istiara"], of=("ذِرَاعَيْ", "the two forearms", "iki kol"),
    n=(" — وَفِيهِ تَشْبِيهٌ وَصَفَهُ الزَّوْزَنِيُّ: «تُرِيكَ سَاقَيْنِ كَأُسْطُوَانَتَيْنِ مِنْ عَاجٍ أَوْ رُخَامٍ بَيَاضًا وَضِخَمًا»؛ وَهُوَ — عَلَى حَدِّ التَّلْخِيصِ — اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: ذُكِرَ الْمُشَبَّهُ بِهِ (السَّارِيَتَانِ) وَطُوِيَ الْمُشَبَّهُ (السَّاقَانِ)، وَالْجَامِعُ الْبَيَاضُ وَالضِّخَمُ",
       " — a likening al-Zawzanī describes: «she shows you two legs like two columns of ivory or marble, in whiteness and bulk»; by the Talkhīṣ's definition it is an istiʿāra taṣrīḥiyya: the columns are named and the legs folded away, whiteness and bulk being what joins them",
       " — Zevzenî'nin tarif ettiği benzetme: «sana beyazlıkta ve iri oluşta fildişinden yahut mermerden iki sütun gibi iki bacak gösterir»; Telhîs'in tarifine göre istiâre-i tasrîhiyyedir: sütunlar zikredilmiş, bacaklar dürülmüştür; câmi' beyazlık ve iriliktir")),
  R("mdf", "بَلَنْطٍ", "balant-amr", n=ZW("الْبَلَنْطُ: الْعَاجُ", "بَلَنْط is ivory", "«belent»: fildişi")),
  PT("أَوْ", "aw", "حَرْفُ عَطْفٍ", "a conjunction («or»)", "atıf harfi («yahut»)", g=["atf-nasaq"]),
  R("atfj", "رُخَامٍ", "rukham-amr", of=("بَلَنْطٍ", "ivory", "fildişi"), n=DR("وَرِوَايَتُهُ: «وَسَالِفَتَيْ رُخَامٍ أَوْ بَلَنْطٍ»", "his text reads «and two necks of marble or ivory»", "onun rivayeti «mermerden yahut fildişinden iki boyun»dur"))],
 [V("d", "يَرِنُّ", "ranna-amr", g=["doubled-verbs"], n=CL("nn", "سَارِيَتَيْ", "two columns", "iki sütun»un")),
  R("fail", "خُشَاشُ", "khushash-amr", mud=True, n=ZW("يُصَوِّتُ حَلْيُهُمَا، أَيْ خَلَاخِيلُهُمَا", "their ornaments — their anklets — ring out", "süsleri, yani halhalları ses verir")),
  R("mdf", "حَلْيِهِمَا", "haly-amr", enc="هِمَا"),
  R("mutlaq", "رَنِينًا", "ranin-amr", n=N3(TANW_ALIF, ZW("الرَّنِينُ: الصَّوْتُ", "رَنِين is sound", "«renîn»: ses")))])
VV(19, "No mother of a young calf who has lost him and sends her moaning cry back and forth has grieved as I grieve,",
  "Yavrusunu yitirip iniltisini tekrar tekrar yükselten bir dişi deve benim kederim gibi kederlenmedi,",
 [PT("فَمَا", "ma-nafiya", "مَا حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ", "مَا, a particle of negation that governs nothing", "«mâ» nefy harfi, ameli yoktur", c="fi", g=["anwa-ma"]),
  V("mt", "وَجَدَتْ", "wajada-amr", g=["mithal-verbs"], n=N3(CL("ist"), ZW("الْوَجْدُ: الْحُزْنُ، وَالْفِعْلُ وَجَدَ يَجِدُ", "وَجْد is grief; the verb is وَجَدَ يَجِدُ", "«vecd»: keder; fiili «vecede yecidu»"))),
  R("majr", "كَوَجْدِي", "wajd-amr", j="ka", enc="ي", sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْحَرَكَةِ الْمُنَاسِبَةِ", " by a kasra estimated before the ya of the speaker, the place being taken by the vowel that suits the ya", " — mütekellim yâsından önceki harf uygun hareke ile meşgul olduğu için takdîrî kesre ile"), g=["ya-al-mutakallim"],
    n=N3(MTH("صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ: وَجْدًا كَوَجْدِي", "an omitted adjective of an omitted absolute object: «a grief like my grief»", "mahzûf mef'ûl-i mutlakın mahzûf sıfatına: «benim kederim gibi bir keder»"), NT("وَهُوَ مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfetidir"))),
  R("fail", "أُمُّ", "umm", mud=True),
  R("mdf", "سَقْبٍ", "saqb-amr", n=ZW("السَّقْبُ بِمَنْزِلَةِ الصَّبِيِّ — عَنِ السِّيرَافِيِّ", "a سَقْب (among camels) is like a boy (among people) — after al-Sīrāfī", "«sakb» (develerde) erkek çocuk gibidir — Sîrâfî'den"))],
 [V("mt", "أَضَلَّتْهُ", "adalla", enc="هُ", doer=NAQA, g=["form-iv-verbs", "doubled-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِـ«أُمُّ سَقْبٍ»", "the clause is an adjective of «the calf's mother», in the seat of raf'", "cümle «yavrunun annesi»nin sıfatı, mahallen merfû")),
  V("mtk", "فَرَجَّعَتِ", "rajja-tf", c="f", doer=NAQA, g=["form-ii-verbs"], n=N3(CL("atf", "أَضَلَّتْهُ", "has lost him", "yitirdi"), ZW("التَّرْجِيعُ: تَرْدِيدُ الصَّوْتِ", "تَرْجِيع is sending the voice back and forth", "«terci'»: sesi tekrar tekrar döndürmek"))),
  R("maf", "الْحَنِينَا", "hanin-amr", n=N3(ITLAQ, ZW("الْحَنِينُ: صَوْتُ الْمُتَوَجِّعِ", "حَنِين is the cry of one in pain", "«hanîn»: acı çekenin sesi")))])
VV(20, "nor any grey-haired woman whose ill-fortune has left her, of nine sons, none but one hidden in the grave.",
  "ne de talihsizliği dokuz oğlundan kendisine kabre gömülmüş olandan başkasını bırakmamış ak saçlı bir kadın.",
 [PT("وَلَا", "la", "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ لَا عَمَلَ لَهَا", "لَا, extra, strengthening the negation; it governs nothing", "nefyi pekiştiren zâid «lâ», ameli yoktur", c="w", g=["huruf-al-ziyada-fil-kafiya"]),
  R("atfr", "شَمْطَاءُ", "shamta-amr", of=("أُمُّ سَقْبٍ", "the calf's mother", "yavrunun annesi"), sign=("بِالضَّمَّةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", " — by the damma, without tanwin: a diptote (the feminine alif mamduda)", " — damme ile; memdûde te'nîs elifi sebebiyle gayr-i munsarif olduğu için tenvinsiz"), g=["mamnu-min-sarf", "hadhf-wa-taqdir"],
    n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("الشَّمَطُ: بَيَاضُ الشَّعْرِ", "شَمَط is whiteness of the hair", "«şemat»: saçın ağarması"))),
  LAM(),
  V(JZ("بِـ«لَمْ»", "by لَمْ", "«lem» ile"), "يَتْرُكْ", "taraka", n=DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "the clause is a second adjective of the omitted noun, in the seat of raf'", "cümle mahzûf mevsûfun ikinci sıfatı, mahallen merfû")),
  R("fail", "شَقَاهَا", "shaqan-amr", enc="هَا", sign=S_AR, g=["ism-maqsur-manqus"], n=ZW("أَيْ شَقَاءُ جَدِّهَا", "that is, the ill-luck of her fortune", "yani bahtının talihsizliği"))],
 [JP("لَهَا", "li", "هَا", n=MT("يَتْرُكْ", "left", "bırakmadı»ya")),
  PR("مِنْ", "min", n=MT("يَتْرُكْ", "left", "bırakmadı»ya")),
  R("majr", "تِسْعَةٍ", "tisa", n=ZW("أَيْ مِنْ تِسْعَةِ بَنِينَ", "that is, of nine sons", "yani dokuz oğuldan")),
  PT("إِلَّا", "illa", "حَرْفُ حَصْرٍ لَا عَمَلَ لَهُ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ", "a particle of restriction that governs nothing; the exception is «emptied» (the verb works on what follows)", "hasr harfi, ameli yoktur; istisnâ müferrağdır", g=["istithna-mufarragh"]),
  R("maf", "جَنِينًا", "janin", n=N3(TANW_ALIF, ZW("الْجَنِينُ هُنَا: الْمَسْتُورُ فِي الْقَبْرِ", "جَنِين here is one hidden in the grave", "«cenîn» burada kabre gizlenmiş olandır")))])
VV(21, "I remembered the love of youth and longed (for her) when I saw her loaded camels being driven off at evening,",
  "Gençlik sevdasını hatırladım ve (ona) özlem duydum, yüklü develerinin akşamüstü sürülüp götürüldüğünü gördüğümde;",
 [V("mtu", "تَذَكَّرْتُ", "tadhakkara", g=["form-v-verbs"], n=CL("ist")),
  R("maf", "الصِّبَا", "siba-amr", sign=S_AN, g=["ism-maqsur-manqus"], n=ZW("أَيْ تَذَكَّرْتُ الْعِشْقَ وَالْهَوَى", "that is, I remembered love and passion", "yani aşkı ve sevdayı hatırladım")),
  V("mtu", "وَاشْتَقْتُ", "ishtaqa", c="w", g=["form-viii-verbs", "hollow-verbs", "tanazu"], n=DR("وَمُتَعَلَّقُهُ مَحْذُوفٌ: وَاشْتَقْتُ إِلَيْهَا", "what it hangs on is left out: «and I longed for her»", "taalluku mahzûftur: «ve onu özledim»")),
  PT("لَمَّا", "lamma", "ظَرْفٌ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِأَحَدِ الْفِعْلَيْنِ قَبْلَهُ عَلَى التَّنَازُعِ (الدُّرَّةُ)", "an adverb meaning «when», built on sukun, in the seat of nasb; it hangs on one of the two verbs before it, which contend for it (al-Durra)", "«hîne» anlamında zarf, sükûn üzere mebnî, mahallen mansûb; tenâzu' yoluyla önceki iki fiilden birine müteallik (Dürre)", g=["tanazu", "maful-fih"])],
 [V("mtu", "رَأَيْتُ", "raa", g=["naqis-verbs"], n=CL("mdf", "لَمَّا", "لَمَّا", "lemmâ")),
  R("maf", "حُمُولَهَا", "humul-amr", enc="هَا", g=["jam-taksir"], n=ZW("الْحُمُولُ: جَمْعُ حَامِلٍ، يُرِيدُ إِبِلَهَا", "حُمُول is a plural of حَامِل: he means her (loaded) camels", "«humûl», «hâmil»in cem'idir: onun (yüklü) develerini kastediyor")),
  R("zarfz", "أُصُلًا", "asil", g=["jam-taksir"], n=N3(MZ("حُدِينَا", "were driven", "sürüldüler»e"), NT("وَهُوَ جَمْعُ أَصِيلٍ؛ وَالْمَعْنَى عِنْدَ الزَّوْزَنِيِّ: سِيقَتْ عَشِيًّا", "it is the plural of أَصِيل, late afternoon; al-Zawzanī renders: «driven off at evening»", "«asîl»in cem'idir; Zevzenî'ye göre mâna: «akşamüstü sürüldü»"))),
  V("mn", "حُدِينَا", "hada-amr", pas=True, g=["naqis-verbs"], n=N3(ITLAQ, DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «حُمُولَهَا» إِنْ كَانَتْ «رَأَيْتُ» بَصَرِيَّةً، وَمَفْعُولٌ بِهِ ثَانٍ إِنْ كَانَتْ عِلْمِيَّةً", "the clause is a hal of «her loaded camels», in the seat of nasb, if «I saw» is of the eye; the second object if it is of the mind", "«gördüm» gözle görme ise cümle «yüklü develer»den hâl, mahallen mansûb; kalbî ise ikinci mef'ûldür")))])
VV(22, "and al-Yamāma came into view and towered up, like swords in the hands of men who draw them.",
  "Yemâme göründü ve yükseldi, kılıçlarını sıyıranların ellerindeki kılıçlar gibi.",
 [V("mtk", "فَأَعْرَضَتِ", "aarada", c="f", g=["form-iv-verbs"], n=N3(DR("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is joined to what goes before", "cümle öncekine ma'tûftur"), ZW("أَعْرَضَتْ: ظَهَرَتْ؛ عَرَضْتُ الشَّيْءَ فَأَعْرَضَ — وَهٰذَا مِنَ النَّوَادِرِ، وَمِثْلُهُ كَبَبْتُهُ فَأَكَبَّ", "أَعْرَضَتْ: it appeared; «I showed the thing and it appeared» — a rarity, like كَبَبْتُهُ فَأَكَبَّ", "«a'radat»: göründü; «onu gösterdim, o da göründü» — nâdir bir kullanımdır, «kebebtuhû fe-ekebbe» gibi"))),
  R("fail", "الْيَمَامَةُ", "yamama-amr", pos="propn", n=ZW("أَيْ قُرَى الْيَمَامَةِ", "that is, the villages of al-Yamāma", "yani Yemâme köyleri")),
  V("mt", "وَاشْمَخَرَّتْ", "ishmakharra-amr", c="w", doer=HIYA("الْيَمَامَةِ", "al-Yamāma", "Yemâme'ye"), g=["rubai-babs", "doubled-verbs"], n=ZW("اشْمَخَرَّتْ: ارْتَفَعَتْ", "اشْمَخَرَّتْ: it rose high", "«işmeharrat»: yükseldi"))],
 [R("majr", "كَأَسْيَافٍ", "sayf", j="ka", g=TB + ["jam-taksir"], n=N3(MTH("صِفَةٍ لِمَصْدَرٍ مَحْذُوفٍ وَاقِعٍ مَفْعُولًا مُطْلَقًا", "the omitted adjective of an omitted masdar standing as absolute object", "mef'ûl-i mutlak olan mahzûf masdarın mahzûf sıfatına"),
    (" — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ نَصَّ عَلَيْهِ الزَّوْزَنِيُّ: «شَبَّهَ ظُهُورَ قُرَاهَا بِظُهُورِ أَسْيَافٍ مَسْلُولَةٍ مِنْ أَغْمَادِهَا»؛ الْمُشَبَّهُ ظُهُورُ قُرَى الْيَمَامَةِ وَارْتِفَاعُهَا، وَالْمُشَبَّهُ بِهِ ظُهُورُ السُّيُوفِ الْمَسْلُولَةِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ الظُّهُورُ وَالِارْتِفَاعُ، مَذْكُورٌ فِي «أَعْرَضَتْ وَاشْمَخَرَّتْ»",
     " — a tashbih mursal mufassal that al-Zawzanī states: «he likens the appearing of its villages to the appearing of swords drawn from their scabbards»; the appearing and rising of al-Yamāma's villages is likened to drawn swords; the particle is the kaf; the point of likeness, appearing and rising, is named in «came into view and towered up»",
     " — Zevzenî'nin açıkça söylediği teşbîh-i mürsel mufassal: «köylerinin görünüşünü kınlarından sıyrılmış kılıçların görünüşüne benzetti»; müşebbeh Yemâme köylerinin görünüp yükselmesi, müşebbehün bih sıyrılmış kılıçlar, edat kâf; vech-i şebeh — görünmek ve yükselmek — «göründü ve yükseldi»de zikredilmiştir"))),
  R("majr", "بِأَيْدِي", "yad", j="bi", mud=True, sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " by a kasra estimated on the ya", " — yâ üzerinde takdîrî kesre ile"), g=["jam-taksir"], n=MTH("صِفَةٍ لِـ«أَسْيَافٍ»", "an omitted adjective of «swords»", "«kılıçlar»ın mahzûf sıfatına")),
  R("mdf", "مُصْلِتِينَا", "muslit-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail", "hadhf-wa-taqdir"], n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: رِجَالٍ مُصْلِتِينَ", "it is the adjective of an omitted noun: «men drawing (swords)»", "mahzûf bir mevsûfun sıfatıdır: «(kılıç) sıyıran adamlar»"), ZW("أَصْلَتَ السَّيْفَ: سَلَّهُ", "أَصْلَتَ السَّيْفَ is to draw the sword", "«asleta's-seyfe»: kılıcı sıyırdı")))])
# ---- vv. 23–29 — أَبَا هِنْدٍ ----
def JWTN(ar, en, tr):
    return NT("وَجَزْمُهُ عِنْدَ الْجُمْهُورِ بِشَرْطٍ مَحْذُوفٍ: " + ar + "؛ وَالْجُمْلَةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "most hold it in jazm by an omitted condition, «" + en + "»; the clause has no seat of its own", "cumhura göre mahzûf bir şartla meczûmdur: «" + tr + "»; cümlenin i'râbda mahalli yoktur")
RUBBA_S = ("بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ «رُبَّ» الْمَحْذُوفَةِ، وَهِيَ حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ", " by a damma that is only estimated, the place being taken by the kasra of the omitted رُبَّ, a jarr letter like an extra one", " — mahzûf «rubbe»nin (zâide benzeyen cer harfi) harekesi yeri işgal ettiği için takdîrî damme ile")
VV(23, "Abū Hind, do not be hasty against us: give us time, and we shall tell you the certain truth —",
  "Ebû Hind, bize karşı acele etme; bize mühlet ver de sana kesin olanı haber verelim —",
 [R("munm", "أَبَا", "ab", mud=True, sign=S_ALIF5, g=["five-nouns"], n=N3(NO_HADHF(), ZW("يُرِيدُ عَمْرَو بْنَ هِنْدٍ فَكَنَاهُ", "he means ʿAmr ibn Hind, calling him by his kunya", "Amr b. Hind'i kastediyor, ona künyesiyle hitap etti"))),
  R("mdf", "هِنْدٍ", "hind", pos="propn"),
  PT("فَلَا", "la-nahiya", "الْفَاءُ زَائِدَةٌ لِتَزْيِينِ اللَّفْظِ (الدُّرَّةُ)، وَلَا نَاهِيَةٌ جَازِمَةٌ", "the fa is extra, to grace the wording (al-Durra); لَا is the لَا of forbidding, which puts the verb in jazm", "fâ lafzı süslemek için zâiddir (Dürre); «lâ» cezmeden nehiy «lâ»sıdır", g=["la-nahiya", "huruf-al-ziyada-fil-kafiya"], segs=SG(("فَ", "fa", "conj"), ("لَا", "la-nahiya", "part"))),
  V(JZ("بِـ«لَا» النَّاهِيَةِ", "by the لَا of forbidding", "nehiy «lâ»sı ile"), "تَعْجَلْ", "ajila", doer=ANTA, n=NT("وَجُمْلَتَا النِّدَاءِ وَالنَّهْيِ ابْتِدَائِيَّتَانِ لَا مَحَلَّ لَهُمَا", "the call and the forbidding open the speech and have no seat of their own", "nidâ ve nehiy cümleleri ibtidâiyyedir, mahalleri yoktur")),
  JP("عَلَيْنَا", "ala", "نَا", n=MT("تَعْجَلْ", "be hasty", "acele etme»ye"))],
 [V("a", "وَأَنْظِرْنَا", "anzara-tf", c="w", enc="نَا", doer=ANTA, g=["form-iv-verbs"], n=CL("atf", "لَا تَعْجَلْ", "do not be hasty", "acele etme")),
  V(JZ("فِي جَوَابِ الْأَمْرِ", "in answer to the command", "emrin cevabı olarak"), "نُخَبِّرْكَ", "khabbara", enc="كَ", encrole="maf1", doer=NAHNU, g=["form-ii-verbs", "jawab-al-talab", "mafulayn"], n=JWTN("إِنْ تُنْظِرْنَا نُخَبِّرْكَ", "if you give us time, we shall tell you", "bize mühlet verirsen sana haber verelim")),
  R("maf2", "الْيَقِينَا", "yaqin", n=N3(ITLAQ, ZW("أَيْ بِالْيَقِينِ مِنْ أَمْرِنَا وَشَرَفِنَا", "that is, the certain truth of our standing and our honour", "yani durumumuzun ve şerefimizin kesin olanını")))])
VV(24, "that we take our banners down to (the waters of) war white, and bring them back red, having drunk their fill —",
  "sancaklarımızı (savaşın suyuna) beyaz indirir, kana kanmış olarak kırmızı geri getiririz —",
 [INNA("بِأَنَّا", "anna", enc="نَا", j="bi", g=["asbab-al-itnab", "ijaz-itnab-musawat"], n=N3(DR("وَحُذِفَتْ إِحْدَى النُّونَاتِ لِلتَّخْفِيفِ؛ وَ«أَنَّ» وَمَعْمُولَاهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِالْبَاءِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نُخَبِّرْكَ»؛ وَيَجُوزُ أَنْ تَكُونَ الْبَاءُ زَائِدَةً، فَيَكُونَ الْمَصْدَرُ بَدَلًا مِنَ «الْيَقِينَا»", "one nun is dropped for ease; أَنَّ with its two terms makes a masdar in jarr by the ba, the phrase hanging on «we shall tell you»; or the ba is extra and the masdar a badal of «the certain truth»", "nûnlardan biri hafiflik için düşmüştür; «enne» ve iki ma'mûlü bâ ile mecrûr bir masdar olur, câr-mecrûr «haber verelim»e müteallik; yahut bâ zâiddir ve masdar «kesin olan»dan bedeldir"),
    (" — وَفِيهِ إِطْنَابٌ بِالْإِيضَاحِ بَعْدَ الْإِبْهَامِ: أَبْهَمَ «الْيَقِينَا» فِي الْبَيْتِ قَبْلَهُ ثُمَّ فَسَّرَهُ هُنَا؛ قَالَ الزَّوْزَنِيُّ: «هٰذَا الْبَيْتُ تَفْسِيرُ الْيَقِينِ مِنَ الْبَيْتِ الْأَوَّلِ»", " — an iṭnāb by making plain after leaving vague: he left «the certain truth» vague in the verse before and explains it here; al-Zawzanī: «this verse explains the certain truth of the verse before»", " — ibhâmdan sonra îzâh yoluyla ıtnâb: önceki beyitte «kesin olan»ı müphem bıraktı, burada açıkladı; Zevzenî: «bu beyit önceki beyitteki kesin olanın açıklamasıdır»"))),
  V("d", "نُورِدُ", "awrada", doer=NAHNU, g=["form-iv-verbs"], n=CL("khb", "أَنَّ", "أَنَّ", "enne")),
  R("maf", "الرَّايَاتِ", "raya", sign=S_JFS, g=["jam-muannath-salim"], n=ZW("الرَّايَةُ: الْعَلَمُ، وَالْجَمْعُ الرَّايَاتُ وَالرَّايُ", "رَايَة is a banner; its plurals are رَايَات and رَاي", "«râye»: sancak; cem'i «râyât» ve «rây»")),
  R("hal", "بِيضًا", "abyad", g=["jam-taksir"], n=NT("صَاحِبُهَا «الرَّايَاتِ»", "of «the banners»", "«sancaklar»ın hâli"))],
 [V("d", "وَنُصْدِرُهُنَّ", "asdara", c="w", enc="هُنَّ", doer=NAHNU, g=["form-iv-verbs", "tibaq"], n=N3(CL("atf", "نُورِدُ", "we take down", "indiririz"),
    HADD("طِبَاقٌ بَيْنَ «نُورِدُ» وَ«نُصْدِرُ»: الْإِيرَادُ وَالْإِصْدَارُ ضِدَّانِ — الذَّهَابُ إِلَى الْمَاءِ وَالرُّجُوعُ عَنْهُ", "a ṭibāq between «take down» and «bring back»: taking to water and bringing back from it are contraries", "«indiririz» ile «geri getiririz» arasında tıbâk: suya indirmek ve sudan döndürmek zıttır"))),
  R("hal", "حُمْرًا", "ahmar", g=["jam-taksir", "kinaya", "aqsam-al-kinaya"], n=N3(NT("صَاحِبُهَا الضَّمِيرُ «هُنَّ»", "of the pronoun «them»", "«onları» zamirinin hâli"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ كَثْرَةِ الْقَتْلِ، بَيَّنَهَا الزَّوْزَنِيُّ: «وَنُرْجِعُهَا مِنْهَا حُمْرًا قَدْ رَوِينَ مِنْ دِمَاءِ الْأَبْطَالِ»", " — a kināya for much slaying, which al-Zawzanī makes plain: «we bring them back from it red, having drunk their fill of the blood of champions»", " — çok öldürmekten kinâyedir; Zevzenî açıklar: «onları oradan kahramanların kanına kanmış olarak kırmızı döndürürüz»"))),
  QAD(),
  V("mn", "رَوِينَا", "rawiya-drink", g=["naqis-verbs", "istiara-makniyya", "arkan-al-istiara"], n=N3(ITLAQ, DR("وَالنُّونُ لِلرَّايَاتِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ مِنَ الضَّمِيرِ «هُنَّ»", "the nun refers to the banners; the clause is a second hal of «them», in the seat of nasb", "nûn sancaklara döner; cümle «onları» zamirinin ikinci hâli, mahallen mansûb"),
    HADD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شَبَّهَ الرَّايَاتِ بِشَارِبٍ عَطْشَانَ، وَطَوَى الْمُشَبَّهَ بِهِ وَدَلَّ عَلَيْهِ بِلَازِمِهِ «رَوِينَ» (وَالرِّيُّ هُنَا مِنَ الدِّمَاءِ كَمَا شَرَحَهُ الزَّوْزَنِيُّ)", "an istiʿāra makniyya: the banners are likened to a thirsty drinker, who is folded away and shown by what goes with him, «they have drunk their fill» (of blood, as al-Zawzanī explains)", "istiâre-i mekniyye: sancaklar susamış bir içiciye benzetilmiş, müşebbehün bih dürülüp lâzımı olan «kandılar» ile gösterilmiştir (Zevzenî'nin açıkladığı gibi kanla)")))])
VV(25, "and of famous long days of ours in which we defied the king, (refusing) to submit.",
  "ve kralın sözünü dinlemediğimiz, ona boyun eğmeyi reddettiğimiz meşhur, uzun günlerimizi.",
 [R("atfj", "وَأَيَّامٍ", "yawm", c="w", g=["jam-taksir"], of=("الْمَصْدَرِ الْمُؤَوَّلِ فِي الْبَيْتِ قَبْلَهُ", "the masdar in the verse before", "önceki beyitteki masdar"), n=N3(DR("وَيَجُوزُ أَنْ تَكُونَ الْوَاوُ وَاوَ «رُبَّ» وَ«أَيَّامٍ» مُبْتَدَأً", "the waw may also be the waw of رُبَّ, with «days» a mubtada", "vâv «rubbe» vâvı, «günler» de mübtedâ olabilir"), ZW("الْأَيَّامُ: الْوَقَائِعُ هُنَا", "days here are battles", "günler burada savaşlardır"))),
  JP("لَنَا", "li", "نَا", n=MTH("صِفَةٍ لِـ«أَيَّامٍ»", "an omitted adjective of «days»", "«günler»in mahzûf sıfatına")),
  R("naatj", "غُرٍّ", "agharr-amr", g=["jam-taksir", "istiara-tabaiyya"], n=(" — وَفِيهِ اسْتِعَارَةٌ وَصَفَهَا الزَّوْزَنِيُّ: «الْغُرُّ بِمَعْنَى الْمَشَاهِيرِ، كَالْخَيْلِ الْغُرِّ لِاشْتِهَارِهَا فِيمَا بَيْنَ الْخَيْلِ»؛ وَهِيَ — عَلَى حَدِّ التَّلْخِيصِ — تَبَعِيَّةٌ فِي الصِّفَةِ: اسْتُعِيرَتِ الْغُرَّةُ لِلشُّهْرَةِ", " — an istiʿāra that al-Zawzanī describes: «غُرّ means famous, like horses with a blaze, which stand out among horses»; by the Talkhīṣ's definition it is a dependent (tabaʿiyya) istiʿāra in an adjective: the blaze is borrowed for fame", " — Zevzenî'nin tarif ettiği istiâre: «gurr meşhurlar demektir; atlar arasında göze çarpan alnı akıtmalı atlar gibi»; Telhîs'in tarifine göre sıfatta tebeiyye istiâresidir: alındaki akıtma şöhret için istiâre edilmiştir")),
  R("naatj", "طِوَالٍ", "tawil-long", g=["jam-taksir"])],
 [V("mna", "عَصَيْنَا", "asa", g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «أَيَّامٍ» بَعْدَ وَصْفِهِ", "the clause is a hal of «days», described as they are, in the seat of nasb", "cümle, nitelendikten sonra «günler»den hâl, mahallen mansûb")),
  R("maf", "الْمَلْكَ", "malik-king", n=NT("وَهُوَ «الْمَلِكُ» سُكِّنَتْ لَامُهُ تَخْفِيفًا", "it is الْمَلِك with its lam made quiescent for lightness", "«el-melik»tir; lâmı hafiflik için sâkin kılınmıştır")),
  JP("فِيهَا", "fi", "هَا", n=MT("عَصَيْنَا", "defied", "dinlemedik»e")),
  AN(n=N3(DR("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَنْصُوبٍ بِنَزْعِ الْخَافِضِ", "أَنْ and the verb make a masdar, in nasb by the dropping of the jarr letter", "«en» ile fiil, cer harfinin düşmesiyle mansûb bir masdar olur"),
    (" — وَفِيهِ إِيجَازٌ بِالْحَذْفِ وَصَفَهُ الزَّوْزَنِيُّ: «أَيْ كَرَاهِيَةَ أَنْ نَدِينَ، فَحَذَفَ الْمُضَافَ — هٰذَا عَلَى قَوْلِ الْبَصْرِيِّينَ — وَقَالَ الْكُوفِيُّونَ: تَقْدِيرُهُ أَنْ لَا نَدِينَ، فَحَذَفَ «لَا»»", " — an ījāz by omission that al-Zawzanī describes: «that is, out of dislike of submitting — the annexed noun is left out, as the Basrans hold; the Kufans read it ‹that we should not submit›, with لَا left out»", " — Zevzenî'nin tarif ettiği hazf yoluyla îcâz: «yani boyun eğmekten hoşlanmadığımız için; muzâf hazfedilmiştir — Basralılara göre; Kûfeliler ‹boyun eğmeyelim diye› der, «lâ» hazfedilmiştir»")), g=["ijaz-al-hadhf"]),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "نَدِينَا", "dana-amr", doer=NAHNU, g=["hollow-verbs"], n=ITLAQ)])
VV(26, "And many a lord of a people, whom they had crowned with the crown of kingship, who shielded those driven to seek refuge —",
  "Nice bir kavmin efendisi ki onu hükümdarlık tacıyla taçlandırmışlardı, sığınmaya muhtaç olanları korurdu —",
 [R("mub", "وَسَيِّدِ", "sayyid", c="wr", mud=True, sign=RUBBA_S, g=["al-lam-wa-rubba-fil-kafiya"], n=N3(DR("وَخَبَرُهُ جُمْلَةُ «تَرَكْنَا …» فِي الْبَيْتِ بَعْدَهُ", "its khabar is «we left …» in the next verse", "haberi sonraki beyitteki «bıraktık …» cümlesidir"), ZW("وَرُبَّ سَيِّدِ قَوْمٍ مُتَوَّجٍ بِتَاجِ الْمُلْكِ … قَهَرْنَاهُ", "many a lord of a people, crowned with the crown of kingship … we have crushed", "nice taçlı kavim efendisini … ezdik"))),
  R("mdf", "مَعْشَرٍ", "mashar"),
  QAD(),
  V("mw", "تَوَّجُوهُ", "tawwaja-amr", enc="هُ", g=["form-ii-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ عَلَى اللَّفْظِ، أَوْ رَفْعٍ عَلَى الْمَحَلِّ، صِفَةٌ لِـ«سَيِّدِ»", "the clause is an adjective of «lord», in the seat of jarr by its outward case, or of raf' by its seat", "cümle «efendi»nin sıfatıdır: lafza göre mahallen mecrûr, mahalline göre merfû"))],
 [R("majr", "بِتَاجِ", "taj", j="bi", mud=True, n=MT("تَوَّجُوهُ", "crowned him", "taçlandırdılar»a")),
  R("mdf", "الْمُلْكِ", "mulk"),
  V("dy", "يَحْمِي", "hama-protect", doer=HUWA("السَّيِّدِ", "the lord", "efendiye"), g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِـ«سَيِّدِ»", "the clause is a second adjective of «lord»", "cümle «efendi»nin ikinci sıfatıdır")),
  R("maf", "الْمُحْجَرِينَا", "muhjar-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-maful"], n=ZW("أَحْجَرْتُهُ: أَلْجَأْتُهُ؛ أَيْ حَامٍ لِلْمُلْجَئِينَ", "أَحْجَرْتُهُ is «I drove him to seek refuge»: a protector of those driven to it", "«ahcertuhû»: onu sığınmaya mecbur ettim; yani sığınmaya muhtaç olanların koruyucusu"))])
VV(27, "we left the horses standing over him, their reins hung on their necks, each resting on three legs.",
  "atlarımızı başında durur hâlde bıraktık; dizginleri boyunlarına takılmış, üç ayak üzerinde dinlenerek.",
 [V("mna", "تَرَكْنَا", "taraka", g=["mafulayn", "kinaya"], n=N3(DR("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «سَيِّدِ» فِي الْبَيْتِ قَبْلَهُ", "the clause is the khabar of «lord» in the verse before, in the seat of raf'", "cümle önceki beyitteki «efendi»nin haberi, mahallen merfû"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ قَتْلِهِ، بَيَّنَهَا الزَّوْزَنِيُّ: «قَتَلْنَاهُ وَحَبَسْنَا خَيْلَنَا عَلَيْهِ»", " — a kināya for his killing, which al-Zawzanī makes plain: «we killed him and kept our horses standing over him»", " — onu öldürmekten kinâyedir; Zevzenî açıklar: «onu öldürdük ve atlarımızı başında tuttuk»"))),
  R("maf1", "الْخَيْلَ", "khayl"),
  R("maf2", "عَاكِفَةً", "akif-amr", g=["ism-fail"], n=ZW("الْعُكُوفُ: الْإِقَامَةُ", "عُكُوف is staying in one place", "«ukûf»: bir yerde kalmak")),
  JP("عَلَيْهِ", "ala", "هِ", n=MT("عَاكِفَةً", "standing", "duran»a"))],
 [R("maf2", "مُقَلَّدَةً", "muqallad-amr", g=["ism-maful"], n=DR("مِنْ تَعَدُّدِ الْمَفْعُولِ الثَّانِي، كَمَا يَتَعَدَّدُ الْخَبَرُ", "the second object repeated, as a khabar may be", "ikinci mef'ûlün tekrarı; haberin birden çok olabilmesi gibi")),
  R("maf2", "أَعِنَّتَهَا", "inan", enc="هَا", g=["jam-taksir", "ism-maful"], n=NT("لِاسْمِ الْمَفْعُولِ «مُقَلَّدَةً»، وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ", "of the passive participle «hung with», whose deputy doer is the pronoun hidden in it", "«takılmış» ism-i mef'ûlünün ikinci mef'ûlü; nâib-i fâili onda gizli zamirdir")),
  R("maf2", "صُفُونَا", "safin-amr", g=["jam-taksir"], n=N3(TANW_ALIF, DR("مِنْ تَعَدُّدِ الْمَفْعُولِ الثَّانِي أَيْضًا", "again the second object repeated", "yine ikinci mef'ûlün tekrarı"), ZW("الصُّفُونُ: جَمْعُ صَافِنٍ؛ صَفَنَ الْفَرَسُ: إِذَا قَامَ عَلَى ثَلَاثِ قَوَائِمَ وَثَنَى سُنْبُكَ الرَّابِعَةِ", "صُفُون is the plural of صَافِن: a horse صَفَنَ when it stands on three legs and tips the fourth hoof", "«sufûn», «sâfin»in cem'idir: at üç ayak üzerinde durup dördüncü toynağının ucunu büktüğünde «safene» denir")))])
VV(28, "We pitched our tents at Dhū Ṭulūḥ, as far as al-Shāmāt, driving off those who had threatened us.",
  "Çadırlarımızı Zû Tulûh'ta, eş-Şâmât'a kadar kurduk; bizi tehdit edenleri sürüp uzaklaştırıyorduk.",
 [V("mna", "وَأَنْزَلْنَا", "anzala", c="wi", g=["form-iv-verbs"], n=CL("ist")),
  R("maf", "الْبُيُوتَ", "bayt", g=["jam-taksir"], n=ZW("أَيْ بُيُوتَنَا", "that is, our tents", "yani çadırlarımızı")),
  R("majr", "بِذِي", "dhu", j="bi", mud=True, sign=S_YA5, g=["five-nouns"], n=MT("أَنْزَلْنَا", "pitched", "kurduk»a")),
  R("mdf", "طُلُوحٍ", "tuluh-amr", pos="propn", n=ZW("أَيْ بِمَكَانٍ يُعْرَفُ بِذِي طُلُوحٍ", "that is, at a place known as Dhū Ṭulūḥ", "yani Zû Tulûh diye bilinen bir yerde"))],
 [PR("إِلَى", "ila", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «ذِي طُلُوحٍ»", "the phrase hangs on an omitted hal of «Dhū Ṭulūḥ»", "câr-mecrûr «Zû Tulûh»un mahzûf hâline müteallik")),
  R("majr", "الشَّامَاتِ", "shamat-amr", pos="propn", g=["jam-muannath-salim"]),
  V("dy", "نَنْفِي", "nafa", doer=NAHNU, g=["naqis-verbs"], n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَا» فِي «أَنْزَلْنَا»", "the clause is a hal of «we» in «we pitched», in the seat of nasb", "cümle «kurduk»taki «biz»den hâl, mahallen mansûb"), DR("وَرِوَايَتُهُ: «تَنْفِي»، فَالْجُمْلَةُ عِنْدَهُ حَالٌ مِنَ «الْبُيُوتَ»", "his text reads «تَنْفِي», «(the tents) drive off», so for him the clause is a hal of «the tents»", "onun rivayeti «tenfî»dir; ona göre cümle «çadırlar»dan hâldir"))),
  R("maf", "الْمُوعِدِينَا", "muid-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"], n=ZW("أَعْدَاءَنَا الَّذِينَ كَانُوا يُوعِدُونَنَا", "our enemies who used to threaten us", "bizi tehdit eden düşmanlarımızı"))])
VV(29, "The dogs of the tribe have snarled at us, and we have lopped the thorn-tree of those who dwell next to us.",
  "Kabilenin köpekleri bize hırladı; biz de bize komşu olanların keven ağacını budadık.",
 [QAD("وَقَدْ", c="wi"),
  V("mt", "هَرَّتْ", "harra-amr", g=["doubled-verbs", "kinaya", "aqsam-al-kinaya"], n=N3(CL("ist"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ كَثْرَةِ لُبْسِهِمُ السِّلَاحَ، بَيَّنَهَا الزَّوْزَنِيُّ: «قَدْ لَبِسْنَا الْأَسْلِحَةَ حَتَّى أَنْكَرَتْنَا الْكِلَابُ وَهَرَّتْ لِإِنْكَارِهَا إِيَّانَا»", " — a kināya for how heavily they went armed, which al-Zawzanī makes plain: «we put on our weapons until the dogs did not know us and snarled, not knowing us»", " — çok silah kuşanmalarından kinâyedir; Zevzenî açıklar: «silahlarımızı öyle kuşandık ki köpekler bizi tanımadı ve tanımadıkları için hırladılar»"))),
  R("fail", "كِلَابُ", "kalb", mud=True, g=["jam-taksir"]),
  R("mdf", "الْحَيِّ", "hayy-tribe"),
  JP("مِنَّا", "min", "نَا", n=MT("هَرَّتْ", "snarled", "hırladı»ya"))],
 [V("mna", "وَشَذَّبْنَا", "shadhdhaba-amr", c="w", g=["form-ii-verbs", "istiara", "arkan-al-istiara"], n=N3(CL("atf", "هَرَّتْ", "snarled", "hırladı"),
    (" — وَفِيهِ اسْتِعَارَةٌ نَصَّ عَلَيْهَا الزَّوْزَنِيُّ: «اسْتَعَارَ لِفَلِّ الْغَرْبِ وَكَسْرِ الشَّوْكَةِ تَشْذِيبَ الْقَتَادَةِ»؛ وَهِيَ تَصْرِيحِيَّةٌ: ذُكِرَ الْمُشَبَّهُ بِهِ (تَشْذِيبُ الْقَتَادَةِ) وَطُوِيَ الْمُشَبَّهُ (كَسْرُ شَوْكَةِ الْأَعْدَاءِ)", " — an istiʿāra that al-Zawzanī names: «he borrows the lopping of the thorn-tree for blunting the edge and breaking the might (the ‹thorn›) of the foe»; it is taṣrīḥiyya: the lopping is named and the breaking of the enemy's might folded away", " — Zevzenî'nin adını koyduğu istiâre: «düşmanın keskinliğini köreltmek ve şevketini kırmak için keven ağacını budamayı istiâre etti»; tasrîhiyyedir: budama zikredilmiş, düşmanın şevketini kırmak dürülmüştür"),
    ZW("التَّشْذِيبُ: نَفْيُ الشَّوْكِ وَالْأَغْصَانِ الزَّائِدَةِ عَنِ الشَّجَرِ", "تَشْذِيب is clearing a tree of its thorns and extra branches", "«teşzîb»: ağacı dikenlerinden ve fazla dallarından temizlemek"))),
  R("maf", "قَتَادَةَ", "qatada-amr", mud=True, n=ZW("الْقَتَادُ: شَجَرٌ ذُو شَوْكٍ، وَالْوَاحِدَةُ قَتَادَةٌ", "قَتَاد is a thorny tree; one is a قَتَادَة", "«katâd»: dikenli bir ağaç; teki «katâde»")),
  T("مَنْ", "man", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A relative noun built on sukun, in the seat of jarr as the second term of the idafa.", "Sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr muzâfun ileyh."),
  V("dy", "يَلِينَا", "waliya", enc="نَا", doer=HUWA("«مَنْ»", "«those who»", "«men»e"), g=["mithal-verbs", "naqis-verbs"], n=N3(CL("sila"), ZW("يَلِينَا: يَقْرُبُ مِنَّا", "يَلِينَا: is near us", "«yelînâ»: bize yakın olan")))])
# ---- vv. 30–36 — رَحَى الْحَرْبِ وَقِرَى الْأَضْيَافِ ----
def ISTZ(word_ar, word_en, word_tr, z_ar, z_en, z_tr, kind="تَصْرِيحِيَّةٌ", kind_en="taṣrīḥiyya", kind_tr="tasrîhiyye"):
    """an istiʿāra that al-Zawzanī names («استعار …»), with its Talkhīṣ class"""
    return (" — وَفِيهِ اسْتِعَارَةٌ " + kind + " نَصَّ عَلَيْهَا الزَّوْزَنِيُّ: «" + z_ar + "»؛ ذُكِرَ الْمُسْتَعَارُ مِنْهُ («" + word_ar + "») وَطُوِيَ الْمُسْتَعَارُ لَهُ",
            " — an istiʿāra " + kind_en + " that al-Zawzanī names: «" + z_en + "»; what is borrowed from («" + word_en + "») is named and what it is lent to folded away",
            " — Zevzenî'nin adını koyduğu istiâre-i " + kind_tr + ": «" + z_tr + "»; müsteârun minh («" + word_tr + "») zikredilmiş, müsteârun leh dürülmüştür")
IST_G = ["istiara", "arkan-al-istiara", "aqsam-al-istiara"]
VV(30, "Whenever we move our millstone against a people, they become flour for it in the encounter.",
  "Değirmen taşımızı ne zaman bir kavme götürsek, karşılaşmada onun unu olurlar.",
 [T("مَتَى", "mata", "noun", ["huruf-al-shart-fil-kafiya", "maful-fih"], "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ، مُتَعَلِّقٌ بِـ«نَنْقُلْ» بَعْدَهُ.",
    "A conditional noun that puts verbs in jazm, built on sukun, in the seat of nasb as an adverb of time; it hangs on «we move» after it.", "Cezmeden şart ismi, sükûn üzere mebnî, zaman zarfı olarak mahallen mansûb; sonraki «götürsek»e müteallik."),
  V(JZ("لِأَنَّهُ فِعْلُ الشَّرْطِ", "as the verb of the condition", "şart fiili olarak"), "نَنْقُلْ", "naqala", doer=NAHNU, n=CL("ibt")),
  PR("إِلَى", "ila", n=MT("نَنْقُلْ", "move", "götürsek»e")),
  R("majr", "قَوْمٍ", "qawm"),
  R("maf", "رَحَانَا", "raha", enc="نَا", sign=S_AN, g=["ism-maqsur-manqus"] + IST_G, n=N3(ZW("أَرَادَ بِالرَّحَى رَحَى الْحَرْبِ، وَهِيَ مُعْظَمُهَا", "by the millstone he means the millstone of war, its thick", "değirmen taşıyla savaşın değirmenini, yani en şiddetli yerini kastetti"),
    ISTZ("الرَّحَى", "the millstone", "değirmen taşı", "لَمَّا اسْتَعَارَ لِلْحَرْبِ اسْمَ الرَّحَى اسْتَعَارَ لِقَتْلَاهَا اسْمَ الطَّحِينِ", "having borrowed for war the name of the millstone, he borrowed for its slain the name of flour", "savaş için değirmen taşının adını istiâre edince, maktulleri için de unun adını istiâre etti")))],
 [V(JZ("لِأَنَّهُ جَوَابُ الشَّرْطِ", "as the answer of the condition", "şartın cevabı olarak", sign="nun"), "يَكُونُوا", "kana", g=["kana-wa-akhawatuha", "afal-khamsa", "hollow-verbs"], n=NT("فِعْلٌ نَاقِصٌ، وَوَاوُ الْجَمَاعَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ، وَالْأَلِفُ فَارِقَةٌ؛ وَالْجُمْلَةُ جَوَابُ شَرْطٍ جَازِمٍ لَمْ تَقْتَرِنْ بِالْفَاءِ فَلَا مَحَلَّ لَهَا", "a defective verb; the waw of the group is its noun, in the seat of raf', the alif only marks the plural; the answer of a jazm condition without fa, so it has no seat", "nâkıs fiil; cemaat vâvı mahallen merfû ismidir, elif fârikadır; cümle fâ almamış cezmeden şartın cevabıdır, mahalli yoktur")),
  PR("فِي", "fi", n=MT("يَكُونُوا", "become", "olurlar»a")),
  R("majr", "اللِّقَاءِ", "liqa"),
  JP("لَهَا", "li", "هَا", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «طَحِينًا»، كَانَ صِفَةً لَهُ فَلَمَّا تَقَدَّمَ عَلَيْهِ صَارَ حَالًا", "the phrase hangs on an omitted hal of «flour»: it was its adjective, and fronted it becomes a hal", "câr-mecrûr «un»un mahzûf hâline müteallik: sıfatı idi, öne geçince hâl oldu")),
  R("khbk", "طَحِينَا", "tahin-amr", g=IST_G, n=N3(TANW_ALIF, ISTZ("الطَّحِينِ", "flour", "un", "اسْتَعَارَ لِقَتْلَاهَا اسْمَ الطَّحِينِ؛ يَقُولُ: مَتَى حَارَبْنَا قَوْمًا قَتَلْنَاهُمْ", "he borrowed for its slain the name of flour: whenever we fight a people we kill them", "maktulleri için unun adını istiâre etti: hangi kavimle savaşsak onları öldürürüz")))])
VV(31, "Its leather mat will be the eastern side of Najd, and its handful of grain Quḍāʿa, all of them.",
  "Onun altındaki deri sergi Necd'in doğu yakası, ağzına atılan avuç dolusu tane de Kudâa'nın tamamı olur.",
 [V("d", "يَكُونُ", "kana", g=["kana-wa-akhawatuha", "hollow-verbs"], n=NT("فِعْلٌ مُضَارِعٌ نَاقِصٌ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا", "a defective present verb; the sentence is a fresh one with no seat", "nâkıs muzâri; cümle müste'neftir, mahalli yoktur")),
  R("ismk", "ثِفَالُهَا", "thifal", enc="هَا", g=IST_G, n=N3(ZW("الثِّفَالُ: خِرْقَةٌ أَوْ جِلْدَةٌ تُبْسَطُ تَحْتَ الرَّحَى لِيَقَعَ عَلَيْهَا الدَّقِيقُ", "ثِفَال is a cloth or hide spread under the millstone to catch the flour", "«sifâl»: unun üzerine düşmesi için değirmenin altına serilen bez yahut deri"),
    ISTZ("الثِّفَالِ", "the mat", "sergi", "فَاسْتَعَارَ لِلْمَعْرَكَةِ اسْمَ الثِّفَالِ", "he borrowed for the battlefield the name of the mat", "savaş alanı için serginin adını istiâre etti"))),
  R("zarfm", "شَرْقِيَّ", "sharqi", mud=True, n=DR("مُتَعَلِّقٌ بِمَحْذُوفٍ فِي مَحَلِّ نَصْبٍ خَبَرُ «يَكُونُ»؛ وَقِيلَ: هُوَ الْخَبَرُ نَفْسُهُ", "it hangs on the omitted predicate of يَكُونُ; some make it the predicate itself", "«yekûnu»nun mahzûf haberine müteallik; haberin kendisi olduğu da söylenmiştir")),
  R("mdf", "نَجْدٍ", "najd", pos="propn")],
 [R("atfr", "وَلُهْوَتُهَا", "lahwa-amr", c="w", enc="هَا", of=("ثِفَالُهَا", "its mat", "onun sergisi"), g=IST_G + ["muraat-al-nazir"], n=N3(ZW("اللُّهْوَةُ: الْقَبْضَةُ مِنَ الْحَبِّ تُلْقَى فِي فَمِ الرَّحَى", "لُهْوَة is the handful of grain thrown into the millstone's mouth", "«luhve»: değirmenin ağzına atılan avuç dolusu tane"),
    ISTZ("اللُّهْوَةِ", "the handful", "avuç", "وَاسْتَعَارَ لِلْقَتْلَى اسْمَ اللُّهْوَةِ لِيُشَاكِلَ الرَّحَى وَالطَّحِينَ", "he borrowed for the slain the name of the handful, to match the millstone and the flour", "maktuller için avucun adını, değirmen taşına ve una uysun diye istiâre etti"),
    HADD("مُرَاعَاةُ النَّظِيرِ: جَمَعَ الرَّحَى وَالطَّحِينَ وَالثِّفَالَ وَاللُّهْوَةَ، وَهِيَ أُمُورٌ مُتَنَاسِبَةٌ لَا بِالتَّضَادِّ", "murāʿāt al-naẓīr: he brings together millstone, flour, mat and handful — things that belong together, not as opposites", "murâât-ı nazîr: değirmen taşı, un, sergi ve avucu bir araya getirdi; zıtlıkla değil, birbirine uygunlukla bağlı şeyler"))),
  R("atfn", "قُضَاعَةَ", "qudaa-amr", pos="propn", sign=("بِالْفَتْحَةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — by the fatha, without tanwin: a diptote (a feminine proper name)", " — fetha ile; özel isim ve müennes olduğu için gayr-i munsarif, tenvinsiz"), g=["mamnu-min-sarf"], of=("شَرْقِيَّ نَجْدٍ", "the eastern side of Najd", "Necd'in doğusu")),
  R("twkn", "أَجْمَعِينَا", "ajmain", sign=S_JMSI, g=["jam-mudhakkar-salim"], of=("قُضَاعَةَ", "Quḍāʿa", "Kudâa"))])
VV(32, "You came down to us in the guests' lodging, so we hurried on your fare, lest you revile us.",
  "Bizde misafirlerin konağına indiniz; biz de bize sövmeyesiniz diye ziyafetinizi acele verdik.",
 [V("mtum", "نَزَلْتُمْ", "nazala", n=N3(CL("ist"), NT("وَالْمِيمُ عَلَامَةُ جَمْعِ الذُّكُورِ", "the mim marks the masculine plural", "mîm müzekker cem' alâmetidir"))),
  R("mutlaq", "مَنْزِلَ", "manzil", mud=True, n=DR("عَلَى أَنَّهُ مَصْدَرٌ مِيمِيٌّ؛ أَوْ ظَرْفُ مَكَانٍ مُتَعَلِّقٌ بِـ«نَزَلْتُمْ» عَلَى أَنَّهُ اسْمُ مَكَانٍ", "as a mimi masdar; or an adverb of place hanging on «you came down», as a noun of place", "mîmî masdar sayılırsa; yahut mekân ismi sayılırsa «indiniz»e müteallik mekân zarfı")),
  R("mdf", "الْأَضْيَافِ", "dayf", g=["jam-taksir"]),
  JP("مِنَّا", "min", "نَا", n=MT("نَزَلْتُمْ", "you came down", "indiniz»e"))],
 [V("mna", "فَأَعْجَلْنَا", "aajala-amr", c="f", g=["form-iv-verbs"], n=N3(CL("atf", "نَزَلْتُمْ", "you came down", "indiniz"), DR("وَرِوَايَتُهُ: «فَعَجَّلْنَا»", "his text reads «فَعَجَّلْنَا»", "onun rivayeti «fe-accelnâ»dır"))),
  R("maf", "الْقِرَى", "qira-amr", sign=S_AN, g=["ism-maqsur-manqus"] + IST_G, n=(" — وَفِيهِ اسْتِعَارَةٌ تَهَكُّمِيَّةٌ: جَعَلَ قِتَالَهُمْ قِرًى، وَالتَّهَكُّمُ نَصَّ عَلَيْهِ الزَّوْزَنِيُّ: «تَعَرَّضْتُمْ لِمُعَادَاتِنَا كَمَا يَتَعَرَّضُ الضَّيْفُ لِلْقِرَى، فَقَتَلْنَاكُمْ عِجَالًا كَمَا يُحْمَدُ تَعْجِيلُ قِرَى الضَّيْفِ، ثُمَّ قَالَ تَهَكُّمًا بِهِمْ وَاسْتِهْزَاءً: أَنْ تَشْتِمُونَا»؛ وَهِيَ — عَلَى حَدِّ التَّلْخِيصِ — مِنَ الْعِنَادِيَّةِ: اسْتُعْمِلَ اللَّفْظُ فِي ضِدِّهِ تَنْزِيلًا لِلتَّضَادِّ مَنْزِلَةَ التَّنَاسُبِ",
    " — a mocking (tahakkumiyya) istiʿāra: he makes their slaughter a guest's fare; the mockery is al-Zawzanī's word: «you exposed yourselves to our enmity as a guest seeks hospitality, so we killed you quickly, as speed in feeding a guest is praised; then he says in mockery and scorn: lest you revile us»; by the Talkhīṣ's definition it is of the ‹contrary› kind: a word used for its opposite, the opposition treated as if it were fitness",
    " — tehekküm istiâresi: onları öldürmeyi misafir ziyafeti yaptı; alay Zevzenî'nin sözüdür: «misafirin ziyafete talip olması gibi düşmanlığımıza talip oldunuz; misafir ziyafetinin çabuk verilmesi övüldüğü gibi sizi çabucak öldürdük; sonra alay ve istihza ile ‹bize sövmeyesiniz diye› dedi»; Telhîs'in tarifine göre inâdiyye kısmındandır: lafız zıddında kullanılmış, zıtlık uygunluk yerine konmuştur")),
  AN(n=N3(DR("وَالْمَصْدَرُ الْمُؤَوَّلُ مُضَافٌ إِلَيْهِ لِمَفْعُولٍ لِأَجْلِهِ مَحْذُوفٍ: كَرَاهِيَةَ شَتْمِكُمْ، عَلَى قَوْلِ الْبَصْرِيِّينَ", "the masdar is annexed to an omitted object of cause, «for dislike of your reviling», as the Basrans hold", "masdar, mahzûf bir mef'ûlün lehe muzâfun ileyhtir: «sövmenizden hoşlanmadığımız için» — Basralılara göre"), ZW("أَيْ كَرَاهِيَةَ أَنْ تَشْتِمُونَا، وَلِكَيْ لَا تَشْتِمُونَا", "that is, for dislike of your reviling us, and so that you should not revile us", "yani bize sövmenizden hoşlanmadığımız için ve sövmeyesiniz diye"))),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile", sign="nun"), "تَشْتِمُونَا", "shatama", enc="نَا", g=["afal-khamsa", "fail"], n=W5)])
VV(33, "We gave you a guest's fare and hurried on your fare just before dawn: a crushing rock that grinds.",
  "Size ziyafet verdik, ziyafetinizi şafaktan az önce acele verdik: öğüten, ezen bir kaya.",
 [V("mna", "قَرَيْنَاكُمْ", "qara-host", enc="كُمْ", encrole="maf1", g=["naqis-verbs", "mafulayn"], n=N3(NT("وَالْمِيمُ عَلَامَةُ جَمْعِ الذُّكُورِ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا", "the mim marks the masculine plural; the sentence is a fresh one with no seat", "mîm müzekker cem' alâmetidir; cümle müste'neftir, mahalli yoktur"))),
  V("mna", "فَعَجَّلْنَا", "ajjala-hasten", c="f", g=["form-ii-verbs"], n=CL("atf", "قَرَيْنَاكُمْ", "we gave you fare", "ziyafet verdik")),
  R("maf", "قِرَاكُمْ", "qira-amr", enc="كُمْ", sign=S_AN, g=["ism-maqsur-manqus"])],
 [R("zarfz", "قُبَيْلَ", "qubayla-amr", mud=True, n=N3(MZ("قَرَيْنَاكُمْ", "we gave you fare", "ziyafet verdik»e"), NT("وَهُوَ تَصْغِيرُ «قَبْلَ» لِلتَّقْرِيبِ", "it is the diminutive of قَبْلَ, «just before»", "«kable»nin yakınlık bildiren tasgîridir"))),
  R("mdf", "الصُّبْحِ", "subh"),
  R("maf2", "مِرْدَاةً", "mirdat-tf", g=IST_G + ["mafulayn"], n=N3(NT("لِـ«قَرَيْنَاكُمْ»", "of «we gave you fare»", "«ziyafet verdik»in"), ZW("الْمِرْدَاةُ: الصَّخْرَةُ الَّتِي يُكْسَرُ بِهَا الصُّخُورُ", "مِرْدَاة is the rock with which rocks are broken", "«mirdât»: kayaların kırıldığı kaya"),
    ISTZ("الْمِرْدَاةِ", "the crushing rock", "ezen kaya", "فَاسْتَعَارَ الْمِرْدَاةَ لِلْحَرْبِ … أَيْ حَرْبًا أَهْلَكَتْهُمْ أَشَدَّ إِهْلَاكٍ", "he borrowed the crushing rock for war … that is, a war that destroyed them utterly", "ezen kayayı savaş için istiâre etti … yani onları en şiddetli biçimde helâk eden bir savaş"))),
  R("naatn", "طَحُونَا", "tahun-amr", g=["sighat-mubalagha"], of=("مِرْدَاةً", "a crushing rock", "ezen kaya"), n=N3(TANW_ALIF, ZW("الطَّحُونُ: فَعُولٌ مِنَ الطَّحْنِ", "طَحُون is a فَعُول from grinding", "«tahûn»: öğütmekten fa'ûl")))])
VV(34, "We cover all our people (with our bounty) and keep our hands from (their goods), and we bear for them whatever (burden) they lay on us.",
  "Halkımızı (lütfumuzla) kuşatırız, (mallarından) el çekeriz; bize yükledikleri her yükü onların yerine taşırız.",
 [V("d", "نَعُمُّ", "amma-include", doer=NAHNU, g=["doubled-verbs"], n=N3(CL("ist"), ZW("نَعُمُّ عَشَائِرَنَا بِنَوَالِنَا وَسَيْبِنَا", "we cover our clans with our gifts and our bounty", "aşiretlerimizi ihsanımız ve bağışımızla kuşatırız"), DR("وَرِوَايَتُهُ لِلشَّطْرِ: «نُدَافِعُ عَنْهُمُ الْأَعْدَاءَ قِدْمًا»", "his text of this hemistich is «we have long fended off the foes from them»", "onun rivayetinde bu mısra «öteden beri düşmanları onlardan uzak tutarız»dır"))),
  R("maf", "أُنَاسَنَا", "unas", enc="نَا"),
  V("d", "وَنَعِفُّ", "affa-ant", c="w", doer=NAHNU, g=["doubled-verbs"], n=N3(CL("atf", "نَعُمُّ", "we cover", "kuşatırız"), ZW("وَنَعِفُّ عَنْ أَمْوَالِهِمْ", "we keep our hands from their goods", "mallarından el çekeriz"))),
  JP("عَنْهُمْ", "an", "هُمْ", n=MT("نَعِفُّ", "keep from", "el çekeriz»e"))],
 [V("d", "وَنَحْمِلُ", "hamala", c="w", doer=NAHNU, n=CL("atf", "نَعُمُّ", "we cover", "kuşatırız")),
  JP("عَنْهُمُ", "an", "هُمُ", n=N3(MT("نَحْمِلُ", "bear", "taşırız»a"), NT("وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِلْوَزْنِ (صِلَةُ مِيمِ الْجَمْعِ)", "the mim is given a damma for the metre (the lengthening of the plural mim)", "mîm vezin için damme ile harekelenmiştir (cem' mîminin sılası)"))),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "A relative noun built on sukun, in the seat of nasb as the object.", "Sükûn üzere mebnî ism-i mevsûl, mahallen mansûb mef'ûlün bih."),
  V("mw", "حَمَّلُونَا", "hammala", enc="نَا", encrole="maf1", g=["form-ii-verbs", "mulhaq-bil-jinas", "jinas"], n=N3(CL("sila"), DR("وَالْعَائِدُ مَحْذُوفٌ: مَا حَمَّلُونَاهُ", "the returning pronoun is left out: «what they laid on us»", "dönen zamir mahzûftur: «bize yükledikleri şey»"), ZW("مِنْ أَثْقَالِ حُقُوقِهِمْ وَمُؤْنَتِهِمْ", "of the burdens of their claims and their keep", "haklarının ve geçimlerinin yüklerinden"),
    HADD("مُلْحَقٌ بِالْجِنَاسِ: «نَحْمِلُ» وَ«حَمَّلُونَا» يَجْمَعُهُمَا الِاشْتِقَاقُ", "a figure joined to jinās: «we bear» and «they laid on us» share one derivation", "cinâsa mülhak: «taşırız» ile «yüklediler»i iştikak birleştirir")))])
VV(35, "We thrust with spears as long as men keep off from us, and we strike with swords when we are come upon.",
  "İnsanlar bizden uzak durdukça mızrakla vuruşuruz; üzerimize gelindiğinde kılıçla vururuz.",
 [V("d", "نُطَاعِنُ", "taana3-amr", doer=NAHNU, g=["form-iii-verbs"], n=CL("ist")),
  PT("مَا", "ma-masdariyya", "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ", "مَا, the particle that makes a masdar of time («as long as»)", "masdariyye-zarfiyye «mâ»", g=["anwa-ma"]),
  V("ma", "تَرَاخَى", "tarakha", g=["form-vi-verbs", "naqis-verbs"], n=N3(NT("وَ«مَا» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ، مُتَعَلِّقٌ بِـ«نُطَاعِنُ»", "مَا and the verb make a masdar of time, in the seat of nasb as an adverb, hanging on «we thrust»", "«mâ» ile fiil, zaman zarfı olarak mahallen mansûb bir masdar olur, «vuruşuruz»a müteallik"), ZW("التَّرَاخِي: الْبُعْدُ", "تَرَاخِي is keeping at a distance", "«terâhî»: uzak durmak"))),
  R("fail", "النَّاسُ", "nas"),
  JP("عَنَّا", "an", "نَا", n=MT("تَرَاخَى", "keep off", "uzak durdu»ya"))],
 [V("d", "وَنَضْرِبُ", "daraba", c="w", doer=NAHNU, g=["hadhf-al-maful"], n=N3(CL("atf", "نُطَاعِنُ", "we thrust", "vuruşuruz"), DR("وَالْمَفْعُولُ مَحْذُوفٌ", "the object is left out", "mef'ûl mahzûftur"))),
  R("majr", "بِالسُّيُوفِ", "sayf", j="bi", g=["jam-taksir"], n=MT("نَضْرِبُ", "strike", "vururuz»a")),
  IDHA(plain=True, n=MZ("نَضْرِبُ", "strike", "vururuz»a")),
  V("mna", "غُشِينَا", "ghashiya", pas=True, g=["naqis-verbs", "tibaq"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), ZW("الْغِشْيَانُ: الْإِتْيَانُ؛ أَيْ أَتَوْنَا فَقَرُبُوا مِنَّا؛ يُرِيدُ أَنَّ شَأْنَنَا طَعْنُ مَنْ لَا تَنَالُهُ سُيُوفُنَا", "غِشْيَان is coming upon: they came at us and drew near; he means it is our way to spear those our swords cannot reach", "«ğışyân»: gelmek; yani üzerimize geldiler, bize yaklaştılar; kılıçlarımızın yetişmediğini mızrakla vurmak âdetimizdir der"),
    HADD("طِبَاقٌ بَيْنَ «تَرَاخَى» وَ«غُشِينَا»: التَّبَاعُدُ وَالْإِتْيَانُ ضِدَّانِ، كَمَا شَرَحَهُمَا الزَّوْزَنِيُّ", "a ṭibāq between «keep off» and «are come upon»: keeping away and coming near are contraries, as al-Zawzanī glosses them", "«uzak durdu» ile «üzerimize gelindi» arasında tıbâk: Zevzenî'nin açıkladığı gibi uzaklaşmak ve yaklaşmak zıttır")))])
VV(36, "— with brown, supple, slender spears of al-Khaṭṭ's shafts, or with white (swords) that cut down (what they strike).",
  "— Hatt mızraklarından esmer, esnek, ince (mızraklar)la, yahut (vurduğunu) biçen beyaz (kılıçlar)la.",
 [R("majr", "بِسُمْرٍ", "asmar", j="bi", g=["jam-taksir", "hadhf-wa-taqdir"], n=N3(MT("نُطَاعِنُ", "we thrust", "vuruşuruz»a"), DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: بِرِمَاحٍ سُمْرٍ", "it is the adjective of an omitted noun: «with brown spears»", "mahzûf bir mevsûfun sıfatıdır: «esmer mızraklarla»"), ZW("تُوصَفُ الرِّمَاحُ بِالسُّمْرَةِ لِأَنَّ سُمْرَتَهَا دَالَّةٌ عَلَى نُضْجِهَا فِي مَنَابِتِهَا", "spears are called brown because their brownness shows they ripened where they grew", "mızraklar esmerlikle nitelenir, çünkü esmerlikleri bittikleri yerde olgunlaştıklarını gösterir"))),
  PR("مِنْ", "min", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سُمْرٍ»", "the phrase hangs on «brown»", "câr-mecrûr «esmer»e müteallik")),
  R("majr", "قَنَا", "qana", mud=True, sign=S_AJ, g=["jam-taksir", "ism-maqsur-manqus"]),
  R("mdf", "الْخَطِّيِّ", "khatti-amr", n=ZW("مِنْ رِمَاحِ الرَّجُلِ الْخَطِّيِّ، يُرِيدُ سَمْهَرًا", "of the spears of the man of al-Khaṭṭ — he means Samhar", "Hattlı adamın mızraklarından — Semher'i kastediyor")),
  R("naatj", "لُدْنٍ", "ladn-amr", g=["jam-taksir"], of=("سُمْرٍ", "brown", "esmer"), n=ZW("اللَّدْنُ: اللَّيِّنُ، وَالْجَمْعُ لُدْنٌ", "لَدْن is supple; its plural is لُدْن", "«ledn»: esnek; cem'i «ludn»"))],
 [R("naatj", "ذَوَابِلَ", "dhabil", sign=(S_DIPT[0] + " لِصِيغَةِ مُنْتَهَى الْجُمُوعِ", S_DIPT[1] + " (the furthest plural pattern)", S_DIPT[2] + " (müntehe'l-cumû' sîgası)"), g=["jam-taksir", "mamnu-min-sarf"], of=("سُمْرٍ", "brown", "esmer")),
  PT("أَوْ", "aw", "حَرْفُ عَطْفٍ", "a conjunction («or»)", "atıf harfi («yahut»)", g=["atf-nasaq"]),
  R("majr", "بِبِيضٍ", "abyad", j="bi", g=["jam-taksir", "hadhf-wa-taqdir", "laff-wa-nashr"], n=N3(DR("مَعْطُوفٌ عَلَى «بِسُمْرٍ»، وَهُوَ فِي التَّقْدِيرِ مُتَعَلِّقٌ بِـ«نَضْرِبُ» لَا بِـ«نُطَاعِنُ»؛ وَ«بِيضٌ» صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: سُيُوفٍ", "joined to «with brown», but in sense it hangs on «we strike», not «we thrust»; «white» is the adjective of an omitted «swords»", "«esmerle»ye ma'tûftur; takdiren «vururuz»a müteallik, «vuruşuruz»a değil; «beyaz», mahzûf «kılıçlar»ın sıfatıdır"),
    HADD("لَفٌّ وَنَشْرٌ مُرَتَّبٌ: ذَكَرَ «نُطَاعِنُ … وَنَضْرِبُ» فِي الْبَيْتِ قَبْلَهُ، ثُمَّ «بِسُمْرٍ» لِلطِّعَانِ وَ«بِبِيضٍ» لِلضَّرْبِ عَلَى تَرْتِيبِهِمَا، كَمَا رَدَّهُمَا الدُّرَّةُ", "laff wa-nashr in order: «we thrust … we strike» in the verse before, then «with brown (spears)» for the thrusting and «with white (swords)» for the striking, in the same order, as al-Durra pairs them", "sıralı leff ü neşr: önceki beyitte «vuruşuruz … vururuz», sonra aynı sırayla mızrak dövüşü için «esmerle», kılıç vuruşu için «beyazla»; Dürre de böyle eşleştirir"))),
  V("dn", "يَخْتَلِينَا", "ikhtala-amr", g=["form-viii-verbs", "naqis-verbs"], n=N3(ITLAQ, NT("وَالنُّونُ لِلْبِيضِ؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "the nun refers to the white (swords); the clause is a second adjective of the omitted noun, in the seat of jarr", "nûn beyaz (kılıçlar)a döner; cümle mahzûf mevsûfun ikinci sıfatı, mahallen mecrûr"), ZW("أَيْ يَقْطَعْنَ مَا ضُرِبَ بِهَا", "that is, they cut down whatever is struck with them", "yani onlarla vurulanı keserler"), DR("وَرِوَايَتُهُ: «يَعْتَلِينَا»", "his text reads «يَعْتَلِينَا»", "onun rivayeti «ya'telînâ»dır")))])
# ---- vv. 37–43 — مَجْدٌ مَوْرُوثٌ ----
def TSH(mb, mb_en, mb_tr, mbh, mbh_en, mbh_tr, adat, adat_en, adat_tr, z_ar, z_en, z_tr, wajh_in_verse=False, w=("", "", "")):
    """a tashbīh mursal (mujmal unless the wajh is in the verse), its wajh from al-Zawzanī"""
    kind = ("مُرْسَلٌ مُفَصَّلٌ", "mursal mufassal", "mürsel mufassal") if wajh_in_verse else ("مُرْسَلٌ مُجْمَلٌ", "mursal mujmal", "mürsel mücmel")
    tail = ("، مَذْكُورٌ فِي الْبَيْتِ", " — named in the verse", " — beyitte zikredilmiştir") if wajh_in_verse else ("، ذَكَرَهُ الزَّوْزَنِيُّ وَلَمْ يُذْكَرْ فِي الْبَيْتِ", " — named by al-Zawzanī, not in the verse", " — beyitte değil, Zevzenî'de zikredilir")
    return (" — وَفِيهِ تَشْبِيهٌ " + kind[0] + ": الْمُشَبَّهُ " + mb + "، وَالْمُشَبَّهُ بِهِ " + mbh + "، وَالْأَدَاةُ " + adat + "، وَوَجْهُ الشَّبَهِ " + w[0] + tail[0] + ": «" + z_ar + "»",
            " — a tashbih " + kind[1] + ": " + mb_en + " likened to " + mbh_en + "; the particle is " + adat_en + "; the point of likeness, " + w[1] + tail[1] + ": «" + z_en + "»",
            " — teşbîh-i " + kind[2] + ": müşebbeh " + mb_tr + ", müşebbehün bih " + mbh_tr + ", edat " + adat_tr + "; vech-i şebeh, " + w[2] + tail[2] + ": «" + z_tr + "»")
VV(37, "— as though the skulls of the champions in it were camel-loads tumbling down over stony ground.",
  "— sanki savaşta kahramanların kafatasları, taşlık yerlerde yuvarlanan deve yükleridir.",
 [KAANNA("كَأَنَّ", g=TB, n=TSH("جَمَاجِمُ الْأَبْطَالِ", "the champions' skulls", "kahramanların kafatasları", "وُسُوقُ الْإِبِلِ", "camel-loads", "deve yükleri", "«كَأَنَّ»", "كَأَنَّ", "«keenne»", "شَبَّهَ رُءُوسَهُمْ فِي عِظَمِهَا بِأَحْمَالِ الْإِبِلِ", "he likens their heads, in their size, to camel-loads", "başlarını büyüklükte deve yüklerine benzetti", w=("الْعِظَمُ", "size", "büyüklük"))),
  R("ismka", "جَمَاجِمَ", "jumjuma-tf", mud=True, g=["jam-taksir"]),
  R("mdf", "الْأَبْطَالِ", "batal-ant", g=["jam-taksir"], n=ZW("الْأَبْطَالُ: جَمْعُ بَطَلٍ، وَهُوَ الشُّجَاعُ الَّذِي يُبْطِلُ دِمَاءَ أَقْرَانِهِ", "أَبْطَال is the plural of بَطَل, the brave man who makes his peers' blood go unavenged", "«ebtâl», «batal»ın cem'idir: akranlarının kanını heder eden yiğit")),
  JP("فِيهَا", "fi", "هَا", n=MTH("حَالٍ مِنْ «جَمَاجِمَ»، وَالْهَاءُ لِلْحَرْبِ", "an omitted hal of «skulls»; the ha is the war", "«kafatasları»nın mahzûf hâline; hâ savaşa döner"))],
 [R("khbka", "وُسُوقٌ", "wasq-amr", g=["jam-taksir"], n=N3(ZW("الْوُسُوقُ: جَمْعُ وَسْقٍ، وَهُوَ حِمْلُ بَعِيرٍ", "وُسُوق is the plural of وَسْق, a camel-load", "«vusûk», «vesk»in cem'idir: bir deve yükü"), DR("وَرِوَايَتُهُ: «تَخَالُ جَمَاجِمَ الْأَبْطَالِ فِيهَا وُسُوقًا»، وَذَكَرَ رِوَايَةَ «كَأَنَّ» بِرَفْعِ «وُسُوقٌ» خَبَرًا لَهَا", "his text reads «you would think the skulls … camel-loads (وُسُوقًا)»; he gives the reading with كَأَنَّ, «وُسُوقٌ» in raf' as its predicate", "onun rivayeti «tehâlu … vusûkan»dır; «keenne»li rivayeti de, «vusûkun» onun haberi olarak merfû şeklinde zikreder"))),
  R("majr", "بِالْأَمَاعِزِ", "amaz-tf", j="bi", g=["jam-taksir"], n=N3(MT("يَرْتَمِينَا", "tumbling", "yuvarlanan»a"), ZW("الْأَمَاعِزُ: جَمْعُ الْأَمْعَزِ، وَهُوَ الْمَكَانُ الَّذِي تَكْثُرُ حِجَارَتُهُ", "أَمَاعِز is the plural of أَمْعَز, ground full of stones", "«emâiz», taşı bol yer olan «em'az»ın cem'idir"))),
  V("dn", "يَرْتَمِينَا", "irtama", g=["form-viii-verbs", "naqis-verbs"], n=N3(ITLAQ, NT("وَالنُّونُ لِلْوُسُوقِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِـ«وُسُوقٌ»", "the nun refers to the loads; the clause is an adjective of «camel-loads», in the seat of raf'", "nûn yüklere döner; cümle «deve yükleri»nin sıfatı, mahallen merfû"), ZW("الِارْتِمَاءُ لَازِمٌ وَمُتَعَدٍّ، وَهُوَ فِي الْبَيْتِ لَازِمٌ", "اِرْتِمَاء is both intransitive and transitive; here it is intransitive", "«irtimâ» hem lâzım hem müteaddîdir; beyitte lâzımdır")))])
VV(38, "With them we split the heads of the foe, splitting them, and we reap the necks, and (the swords) cut them down.",
  "Onlarla düşmanın başlarını yarar da yararız; boyunları orak gibi biçeriz, (kılıçlar) onları keser.",
 [V("d", "نَشُقُّ", "shaqqa", doer=NAHNU, g=["doubled-verbs"], n=CL("ist")),
  JP("بِهَا", "bi", "هَا", n=N3(MT("نَشُقُّ", "split", "yararız»a"), NT("وَالْهَاءُ لِلسُّيُوفِ", "the ha refers to the swords", "hâ kılıçlara döner"))),
  R("maf", "رُءُوسَ", "ras", mud=True, g=["jam-taksir"]),
  R("mdf", "الْقَوْمِ", "qawm"),
  R("mutlaq", "شَقًّا", "shaqq-amr", g=["maful-mutlaq"], n=NT("مُؤَكِّدٌ لِعَامِلِهِ", "strengthening its verb", "fiilini te'kîd eder"))],
 [V("d", "وَنَخْتَلِبُ", "ikhtalaba-amr", c="w", doer=NAHNU, g=["form-viii-verbs"], n=N3(CL("atf", "نَشُقُّ", "we split", "yararız"), ZW("الِاخْتِلَابُ: قَطْعُ الشَّيْءِ بِالْمِخْلَبِ، وَهُوَ الْمِنْجَلُ الَّذِي لَا أَسْنَانَ لَهُ", "اِخْتِلَاب is cutting with a مِخْلَب, a sickle without teeth", "«ihtilâb»: dişsiz orak olan «mihleb» ile kesmek"), DR("وَرِوَايَتُهُ: «وَنُخْلِيهَا الرِّقَابَ فَيَخْتَلِينَا»", "his text reads «and we give them the necks as fresh herbage, and they cut them»", "onun rivayeti «boyunları onlara yaş ot kılarız, onlar da biçer»dir"))),
  R("maf", "الرِّقَابَ", "raqaba", g=["jam-taksir"]),
  V("dn", "فَيَخْتَلِينَا", "ikhtala-amr", c="f", g=["form-viii-verbs", "naqis-verbs", "hadhf-al-maful"], n=N3(ITLAQ, NT("وَالنُّونُ لِلسُّيُوفِ، وَالْمَفْعُولُ مَحْذُوفٌ: فَيَخْتَلِينَهَا", "the nun refers to the swords, the object left out: «and they cut them down»", "nûn kılıçlara döner, mef'ûl mahzûftur: «onları biçerler»"), ZW("الِاخْتِلَاءُ: قَطْعُ الْخَلَا، وَهُوَ رَطْبُ الْحَشِيشِ؛ وَنَقْطَعُ بِهَا رِقَابَهُمْ فَيَقْطَعْنَ", "اِخْتِلَاء is cutting خَلًا, fresh grass: we cut their necks with them and they cut", "«ihtilâ»: yaş otu biçmek; onlarla boyunlarını keseriz, onlar da keser")))])
VV(39, "Rancour upon rancour shows itself against you and brings out the buried sickness.",
  "Kin üstüne kin sana karşı belirir ve gömülü hastalığı dışarı çıkarır.",
 [INNA("وَإِنَّ", c="wi"),
  R("ismi", "الضِّغْنَ", "dighn"),
  R("zarfz", "بَعْدَ", "bada", mud=True, n=DR("مُتَعَلِّقٌ بِمَحْذُوفٍ صِفَةٍ لِـ«الضِّغْنَ» عَلَى أَنَّ «أَلْ» لِلْجِنْسِ، أَوْ حَالٍ مِنْهُ عَلَى أَنَّهَا لِلتَّعْرِيفِ", "it hangs on an omitted adjective of «rancour» if its «al» marks the kind, or on an omitted hal if it is the definite «al»", "«el» cins için sayılırsa «kin»in mahzûf sıfatına, ta'rîf için sayılırsa mahzûf hâline müteallik")),
  R("mdf", "الضِّغْنِ", "dighn"),
  V("dw", "يَبْدُو", "bada-appear", doer=HUWA("الضِّغْنِ", "the rancour", "kine"), g=["naqis-verbs"], n=CL("khb", "إِنَّ", "إِنَّ", "inne"))],
 [JP("عَلَيْكَ", "ala", "كَ", n=MT("يَبْدُو", "shows itself", "belirir»e")),
  V("d", "وَيُخْرِجُ", "akhraja", c="w", doer=HUWA("الضِّغْنِ", "the rancour", "kine"), g=["form-iv-verbs"], n=CL("atf", "يَبْدُو", "shows itself", "belirir")),
  R("maf", "الدَّاءَ", "daa-amr", g=["istiara", "arkan-al-istiara"], n=N3(ZW("الدَّاءُ الْمَدْفُونُ مِنَ الْأَفْئِدَةِ، أَيْ يَبْعَثُ عَلَى الِانْتِقَامِ", "the sickness buried in the hearts — it rouses to revenge", "gönüllerde gömülü hastalık — yani intikama sevk eder"),
    HADD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَ «الدَّاءُ» لِلْحِقْدِ الْكَامِنِ، وَالْقَرِينَةُ ذِكْرُ «الضِّغْنِ»", "an istiʿāra taṣrīḥiyya: «sickness» is borrowed for hidden hatred, the mention of «rancour» being the sign", "istiâre-i tasrîhiyye: «hastalık» gizli kin için istiâre edilmiştir; karîne «kin»in zikridir"))),
  R("naatn", "الدَّفِينَا", "dafin-amr", g=["tibaq"], n=N3(ITLAQ, HADD("طِبَاقٌ بَيْنَ «يَبْدُو» وَ«الدَّفِينَا»: الظُّهُورُ وَالْخَفَاءُ ضِدَّانِ", "a ṭibāq between «shows itself» and «buried»: appearing and being hidden are contraries", "«belirir» ile «gömülü» arasında tıbâk: görünmek ve gizli olmak zıttır")))])
VV(40, "We have inherited glory — Maʿadd knows it — and we fight with spears in its defence until it stands out plain.",
  "Şerefi miras aldık — Mead bunu bilir —; onun uğrunda, o apaçık ortaya çıkana dek mızrakla vuruşuruz.",
 [V("mna", "وَرِثْنَا", "waritha", g=["mithal-verbs"], n=CL("ist")),
  R("maf", "الْمَجْدَ", "majd", n=ZW("أَيْ شَرَفَ آبَائِنَا", "that is, the honour of our fathers", "yani atalarımızın şerefi")),
  QAD(),
  V("mt", "عَلِمَتْ", "alima", g=["hadhf-al-maful"], n=DR("وَالْمَفْعُولُ مَحْذُوفٌ: ذٰلِكَ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الْمَجْدَ»", "the object is left out, «that»; the clause is a hal of «glory», in the seat of nasb", "mef'ûl mahzûftur: «bunu»; cümle «şeref»ten hâl, mahallen mansûb")),
  R("fail", "مَعَدٌّ", "maadd-name", pos="propn")],
 [V("d", "نُطَاعِنُ", "taana3-amr", doer=NAHNU, g=["form-iii-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَا» فِي «وَرِثْنَا»، وَيَجُوزُ الِاسْتِئْنَافُ", "the clause is a hal of «we» in «we inherited», in the seat of nasb; it may also open a fresh sentence", "cümle «miras aldık»taki «biz»den hâl, mahallen mansûb; müste'nef de olabilir")),
  R("zarfm", "دُونَهُ", "duna", enc="هُ", n=MZ("نُطَاعِنُ", "we fight", "vuruşuruz»a")),
  HATTA(),
  V(NS("بِـ«أَنْ» مُضْمَرَةً وُجُوبًا بَعْدَ «حَتَّى»", "by an أَنْ understood after حَتَّى", "«hattâ»dan sonra gizli «en» ile"), "يَبِينَا", "lb-bana", doer=HUWA("الْمَجْدِ", "the glory", "şerefe"), g=["hollow-verbs"], n=N3(ITLAQ, NT("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِـ«حَتَّى»، مُتَعَلِّقَانِ بِـ«نُطَاعِنُ»", "the understood أَنْ and the verb make a masdar in jarr after حَتَّى, hanging on «we fight»", "gizli «en» ile fiil «hattâ» ile mecrûr masdar olur, «vuruşuruz»a müteallik"), ZW("حَتَّى يَظْهَرَ الشَّرَفُ لَنَا", "until the honour shows plainly as ours", "şeref bizim olarak açıkça görününceye dek")))])
VV(41, "And we — when the tent-poles of the tribe come crashing down from the baggage-camels — we defend those who live next to us.",
  "Biz ise — kabilenin çadır direkleri yük develerinden yere yıkıldığında — bize komşu olanları koruruz.",
 [NAHNU_M("وَنَحْنُ", c="wi", n=NT("وَخَبَرُهُ جُمْلَةُ «إِذَا» وَجَوَابِهَا", "its khabar is the إِذَا clause with its answer", "haberi «izâ» cümlesi ile cevabıdır")),
  IDHA(),
  R("fail", "عِمَادُ", "imad-amr", mud=True, n=DR("فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ بَعْدَهُ، وَالْجُمْلَةُ الْمَحْذُوفَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "the doer of an omitted verb that the one after it explains; that omitted clause is in the seat of jarr, إِذَا being annexed to it", "sonraki fiilin açıkladığı mahzûf fiilin fâili; mahzûf cümle «izâ»nın izâfetiyle mahallen mecrûr")),
  R("mdf", "الْحَيِّ", "hayy-tribe"),
  V("mt", "خَرَّتْ", "kharra", doer=HIYA("الْعِمَادِ", "the tent-poles", "direklere"), g=["doubled-verbs"], n=NT("وَالْجُمْلَةُ مُفَسِّرَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause explains the omitted one and has no seat", "cümle tefsîriyyedir, mahalli yoktur"))],
 [PR("عَنِ", "an", n=N3(MT("خَرَّتْ", "came crashing down", "yıkıldı»ya"), NT("وَحُرِّكَتْ نُونُهُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "its nun takes kasra where two quiescents meet", "nûnu iki sâkin buluştuğu için kesre almıştır"))),
  R("majr", "الْأَحْفَاضِ", "hifd-amr", g=["jam-taksir"], n=N3(ZW("الْحَفَضُ: الْبَعِيرُ الَّذِي يَحْمِلُ خُرْثِيَّ الْبَيْتِ، وَالْجَمْعُ أَحْفَاضٌ؛ وَمَنْ رَوَى: «عَلَى الْأَحْفَاضِ» أَرَادَ بِهَا الْأَمْتِعَةَ، وَمَنْ رَوَى: «عَنِ الْأَحْفَاضِ» أَرَادَ بِهَا الْإِبِلَ", "حَفَض is the camel that carries the household goods (pl. أَحْفَاض); those who read «on the أَحْفَاض» mean the goods, those who read «from the أَحْفَاض» mean the camels", "«hafad»: ev eşyasını taşıyan deve (ç. «ahfâd»); «ale'l-ahfâd» diye rivayet eden eşyayı, «ani'l-ahfâd» diye rivayet eden develeri kasteder"), DR("وَرِوَايَتُهُ: «عَلَى الْأَحْفَاضِ»", "his text reads «on the أَحْفَاض»", "onun rivayeti «ale'l-ahfâd»dır"))),
  V("d", "نَمْنَعُ", "manaa", doer=NAHNU, n=NT("وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا، وَجُمْلَةُ «إِذَا» وَجَوَابِهَا فِي مَحَلِّ رَفْعٍ خَبَرُ «نَحْنُ»", "the clause is the answer of إِذَا and has no seat; the إِذَا clause with its answer is the khabar of «we», in the seat of raf'", "cümle «izâ»nın cevabıdır, mahalli yoktur; «izâ» cümlesi cevabıyla birlikte «biz»in haberi, mahallen merfû")),
  T("مَنْ", "man", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "A relative noun built on sukun, in the seat of nasb as the object.", "Sükûn üzere mebnî ism-i mevsûl, mahallen mansûb mef'ûlün bih."),
  V("dy", "يَلِينَا", "waliya", enc="نَا", doer=HUWA("«مَنْ»", "«those who»", "«men»e"), g=["mithal-verbs", "naqis-verbs"], n=N3(CL("sila"), ZW("نَمْنَعُ وَنَحْمِي مَنْ يَقْرُبُ مِنَّا مِنْ جِيرَانِنَا", "we defend and protect those of our neighbours who are near us", "bize yakın komşularımızı korur ve himaye ederiz")))])
VV(42, "We cut off their heads with no regard for kinship, so they do not know what they should beware of.",
  "Akrabalık gözetmeden başlarını keseriz; neden sakınacaklarını bilmezler.",
 [V("d", "نَجُذُّ", "jadhdha-amr", doer=NAHNU, g=["doubled-verbs"], n=N3(CL("ist"), ZW("الْجَذُّ: الْقَطْعُ", "جَذّ is cutting", "«cezz»: kesmek"))),
  R("maf", "رُءُوسَهُمْ", "ras", enc="هُمْ", g=["jam-taksir"]),
  PR("فِي", "fi", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الْفَاعِلِ: نَجُذُّ رُءُوسَهُمْ غَيْرَ بَارِّينَ", "the phrase hangs on an omitted hal of the doer: «we cut off their heads, not dutiful to them»", "câr-mecrûr fâilin mahzûf hâline müteallik: «onlara iyilik gözetmeden»")),
  R("majr", "غَيْرِ", "ghayr", mud=True),
  R("mdf", "بِرٍّ", "birr", n=ZW("أَيْ فِي عُقُوقٍ", "that is, in breach of the bond of kin", "yani akrabalık hakkını çiğneyerek"))],
 [PT("فَمَا", "ma-nafiya", "مَا حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ", "مَا, a particle of negation that governs nothing", "«mâ» nefy harfi, ameli yoktur", c="f", g=["anwa-ma"]),
  V("d5", "يَدْرُونَ", "dara", g=["naqis-verbs"], n=NT("وَهُوَ مُعَلَّقٌ عَنِ الْعَمَلِ لَفْظًا بِالِاسْتِفْهَامِ", "it is held back from governing in form by the question", "soru sebebiyle lafzen amelden alıkonmuştur")),
  T("مَاذَا", "madha", "pron", ["al-istifham", "ism-mawsul"], "«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَ«ذَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ مَفْعُولَيْ «يَدْرُونَ» (الدُّرَّةُ)، وَيَجُوزُ أَنْ تَكُونَ «مَاذَا» كَلِمَةً وَاحِدَةً اسْمَ اسْتِفْهَامٍ.",
    "مَا is a noun of question built on sukun, in the seat of raf' as mubtada, and ذَا a relative noun built on sukun, in the seat of raf' as khabar; the clause stands in the place of the objects of «they know», in the seat of nasb (al-Durra); مَاذَا may also be one interrogative word.",
    "«Mâ» sükûn üzere mebnî soru ismi, mahallen merfû mübtedâ; «zâ» sükûn üzere mebnî ism-i mevsûl, mahallen merfû haber; cümle «bilirler»in iki mef'ûlü yerine geçer, mahallen mansûb (Dürre); «mâzâ» tek bir soru ismi de olabilir."),
  V("d5", "يَتَّقُونَا", "ittaqa", g=["form-viii-verbs", "naqis-verbs"], n=N3(ITLAQ, CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: يَتَّقُونَهُ", "the returning pronoun is left out: «what they beware of»", "dönen zamir mahzûftur: «sakındıkları şey»"), ZW("وَلَا يَدْرُونَ مَاذَا يَحْذَرُونَ مِنَّا مِنَ الْقَتْلِ وَسَبْيِ الْحُرَمِ وَاسْتِبَاحَةِ الْأَمْوَالِ", "they do not know what to beware of from us — slaughter, the taking of their women, the seizing of their goods", "bizden neyi sakınacaklarını bilmezler: öldürülmeyi mi, kadınlarının esir edilmesini mi, mallarının yağmalanmasını mı")))])
VV(43, "It is as though our swords, ours and theirs, were wooden blades in the hands of boys at play.",
  "Sanki bizim ve onların kılıçları, oyun oynayanların elindeki tahta kılıçlardır.",
 [KAANNA("كَأَنَّ", g=TB, n=TSH("السُّيُوفُ فِي أَيْدِي الْفَرِيقَيْنِ", "the swords in both sides' hands", "iki tarafın elindeki kılıçlar", "الْمَخَارِيقُ بِأَيْدِي اللَّاعِبِينَ", "wooden blades in players' hands", "oyuncuların elindeki tahta kılıçlar", "«كَأَنَّ»", "كَأَنَّ", "«keenne»", "كُنَّا لَا نَحْفِلُ بِالضَّرْبِ بِالسُّيُوفِ كَمَا لَا يَحْفِلُ اللَّاعِبُونَ بِالضَّرْبِ بِالْمَخَارِيقِ، أَوْ كُنَّا نَضْرِبُ بِهَا فِي سُرْعَةٍ", "we cared no more for striking with swords than players care for striking with wooden blades — or, we struck with them as fast", "kılıçla vuruşmayı, oyuncuların tahta kılıçla vuruşmayı umursamadığı gibi umursamazdık; yahut onlarla öyle hızlı vururduk", w=("قِلَّةُ الْمُبَالَاةِ أَوِ السُّرْعَةُ", "carelessness, or speed", "umursamazlık yahut hız"))),
  R("ismka", "سُيُوفَنَا", "sayf", enc="نَا", g=["jam-taksir"]),
  JP("مِنَّا", "min", "نَا", n=MTH("حَالٍ مِنْ «سُيُوفَنَا»، وَالْعَامِلُ «كَأَنَّ» لِمَا فِيهَا مِنْ مَعْنَى الْفِعْلِ", "an omitted hal of «our swords», governed by كَأَنَّ for the verbal sense in it", "«kılıçlarımız»ın mahzûf hâline; âmil, fiil anlamı taşıdığı için «keenne»dir")),
  JP("وَمِنْهُمْ", "min", "هُمْ", c="w", n=N3(NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «مِنَّا»", "the phrase is joined to «ours»", "câr-mecrûr «bizden»e ma'tûf"), DR("وَرِوَايَتُهُ: «فِينَا وَفِيهِمْ»", "his text reads «among us and among them»", "onun rivayeti «bizde ve onlarda»dır")))],
 [R("khbka", "مَخَارِيقٌ", "mikhraq-amr", g=["jam-taksir", "mamnu-min-sarf"], sign=("بِالضَّمَّةِ — وَصُرِفَ لِلضَّرُورَةِ، وَحَقُّهُ الْمَنْعُ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ (الدُّرَّةُ)، وَبِالتَّنْوِينِ يَسْتَقِيمُ الْوَزْنُ", " — by the damma: declined (ṣurifa) for the metre's need, though by right a diptote on the furthest plural pattern (al-Durra); the tanwin is what the metre needs", " — damme ile; vezin zarureti için munsarif kılınmıştır, aslında müntehe'l-cumû' sîgası olduğu için gayr-i munsariftir (Dürre); vezin tenvinle düzelir"), n=ZW("الْمِخْرَاقُ مَعْرُوفٌ، وَالْمِخْرَاقُ أَيْضًا سَيْفٌ مِنْ خَشَبٍ", "the مِخْرَاق is well known; it is also a sword of wood", "«mihrâk» bilinir; tahtadan kılıca da «mihrâk» denir")),
  R("majr", "بِأَيْدِي", "yad", j="bi", mud=True, sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " by a kasra estimated on the ya", " — yâ üzerinde takdîrî kesre ile"), g=["jam-taksir"], n=MTH("صِفَةٍ لِـ«مَخَارِيقٌ»", "an omitted adjective of «wooden blades»", "«tahta kılıçlar»ın mahzûf sıfatına")),
  R("mdf", "لَاعِبِينَا", "laib-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"])])
# ---- vv. 44–50 — يَوْمُ الْهَوْلِ ----
ROLE["ismas"] = ("اسْمُ «تُصْبِحُ» مَرْفُوعٌ", "the noun of تُصْبِحُ (a sister of كَانَ), in raf'", "«tusbihu»nun ismi, merfû", "raf", ["kana-wa-akhawatuha"])
ROLE["khbas"] = ("خَبَرُ «تُصْبِحُ» مَنْصُوبٌ", "the predicate of تُصْبِحُ, in nasb", "«tusbihu»nun haberi, mansûb", "nasb", ["kana-wa-akhawatuha"])
ROLE["khbas2"] = ("خَبَرٌ ثَانٍ لِـ«تُصْبِحُ» مَنْصُوبٌ", "a second predicate of تُصْبِحُ, in nasb", "«tusbihu»nun ikinci haberi, mansûb", "nasb", ["kana-wa-akhawatuha"])
S_MULHAQ_I = ("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ، وَالْأَلِفُ لِلْإِطْلَاقِ", " — by the ya, as it declines like the sound masculine plural; its nun stands for the tanwin of the singular, and the final alif is the alif of iṭlāq", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûn müfreddeki tenvinin karşılığı, sondaki elif ıtlâk elifidir")
VV(44, "as though our clothes and theirs had been dyed with purple, or smeared with it.",
  "sanki bizim ve onların elbiseleri erguvanla boyanmış yahut sıvanmıştır.",
 [KAANNA("كَأَنَّ", g=TB, n=HADD("تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الثِّيَابُ الْمُضَرَّجَةُ بِالدَّمِ، وَالْمُشَبَّهُ بِهِ ثِيَابٌ خُضِبَتْ بِالْأُرْجُوَانِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الْحُمْرَةُ — غَيْرُ مَذْكُورٍ", "a tashbih mursal mujmal: clothes soaked in blood are likened to clothes dyed with purple; the particle is كَأَنَّ; the point of likeness, the red, is not named", "teşbîh-i mürsel mücmel: kana bulanmış elbiseler erguvanla boyanmış elbiselere benzetilmiş; edat «keenne»; vech-i şebeh — kızıllık — zikredilmemiştir")),
  R("ismka", "ثِيَابَنَا", "thawb", enc="نَا", g=["jam-taksir"]),
  JP("مِنَّا", "min", "نَا", n=MTH("حَالٍ مِنْ «ثِيَابَنَا»، وَالْعَامِلُ «كَأَنَّ»", "an omitted hal of «our clothes», governed by كَأَنَّ", "«elbiselerimiz»in mahzûf hâline; âmil «keenne»dir")),
  JP("وَمِنْهُمْ", "min", "هُمْ", c="w", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «مِنَّا»", "the phrase is joined to «ours»", "câr-mecrûr «bizden»e ma'tûf"))],
 [V("mn", "خُضِبْنَ", "khadaba-ant", pas=True, n=CL("khb", "كَأَنَّ", "كَأَنَّ", "keenne")),
  R("majr", "بِأَرْجُوَانٍ", "urjuwan-amr", j="bi", n=MT("خُضِبْنَ", "dyed", "boyandı»ya")),
  PT("أَوْ", "aw", "حَرْفُ عَطْفٍ", "a conjunction («or»)", "atıf harfi («yahut»)", g=["atf-nasaq"]),
  V("mn", "طُلِينَا", "tala-amr", pas=True, g=["naqis-verbs"], n=N3(ITLAQ, CL("atf", "خُضِبْنَ", "dyed", "boyandı")))])
VV(45, "When a tribe shrinks from going forward for dread of a terror that seems about to come,",
  "Bir kabile, gelmesi muhtemel görünen bir dehşetten korkarak ilerlemekten âciz kaldığında,",
 [IDHA(n=NT("وَجَوَابُهُ «نَصَبْنَا» فِي الْبَيْتِ بَعْدَهُ", "its answer is «we set up» in the next verse", "cevabı sonraki beyitteki «diktik»tir")),
  MA_Z(),
  V("m", "عَيَّ", "ayiya-amr", g=["naqis-verbs", "doubled-verbs"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), NT("وَأَصْلُهُ «عَيِيَ»، أُدْغِمَتِ الْيَاءُ فِي الْيَاءِ", "its root form is عَيِيَ, the two yas merged", "aslı «ayiye»dir; iki yâ idgâm edilmiştir"))),
  R("majr", "بِالْإِسْنَافِ", "isnaf-amr", j="bi", n=N3(MT("عَيَّ", "shrinks", "âciz kaldı»ya"), ZW("الْإِسْنَافُ: الْإِقْدَامُ", "إِسْنَاف is going forward", "«isnâf»: ileri atılmak"))),
  R("fail", "حَيٌّ", "hayy-tribe", n=ZW("أَيْ قَوْمٌ", "that is, a people", "yani bir kavim"))],
 [PR("مِنَ", "min", n=N3(MT("عَيَّ", "shrinks", "âciz kaldı»ya"), NT("وَهِيَ لِلتَّعْلِيلِ", "it gives the cause", "ta'lîl içindir"))),
  R("majr", "الْهَوْلِ", "hawl-amr"),
  R("naatj", "الْمُشَبَّهِ", "mushabbah", g=["ism-maful"], n=DR("وَهُوَ بِمَعْنَى الْمُشْتَبَهِ", "it means «uncertain»", "«müştebeh», yani belirsiz anlamındadır")),
  AN(n=DR("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مُضَافٍ إِلَيْهِ لِمَفْعُولٍ لِأَجْلِهِ مَحْذُوفٍ: كَرَاهِيَةَ أَنْ يَكُونَ", "أَنْ and the verb make a masdar annexed to an omitted object of cause: «for dread that it should come»", "«en» ile fiil, mahzûf mef'ûlün lehe muzâfun ileyh olan bir masdar olur: «olmasından korkarak»")),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "يَكُونَا", "kana", doer=HUWA("الْهَوْلِ", "the terror", "dehşete"), g=["hollow-verbs", "al-fil-al-tamm-wal-naqis"], n=N3(NT("وَهُوَ هُنَا تَامٌّ بِمَعْنَى «يَحْدُثُ»", "here it is complete, «to happen»", "burada «olmak, meydana gelmek» anlamında tâm fiildir"), ITLAQ, ZW("مَخَافَةَ هَوْلٍ مُنْتَظَرٍ مُتَوَقَّعٍ يُشْبِهُ أَنْ يَكُونَ وَيُمْكِنُ", "for fear of an awaited, expected terror that seems likely to come and may", "beklenen, umulan, olması muhtemel ve mümkün bir dehşet korkusuyla")))])
VV(46, "we set up (a host) like Rahwa, with a cutting edge, to guard (our honour), and we were the foremost.",
  "Rehve dağı gibi keskin (bir ordu) diktik, (şerefimizi) korumak için; öne geçenler biz olduk.",
 [V("mna", "نَصَبْنَا", "nasaba-set", g=["hadhf-al-maful"], n=DR("وَالْجُمْلَةُ جَوَابُ «إِذَا» فِي الْبَيْتِ قَبْلَهُ لَا مَحَلَّ لَهَا", "the clause is the answer of إِذَا in the verse before and has no seat", "cümle önceki beyitteki «izâ»nın cevabıdır, mahalli yoktur")),
  R("naatn", "مِثْلَ", "mithl", mud=True, g=TB + ["hadhf-wa-taqdir"], n=N3(DR("لِمَفْعُولٍ بِهِ مَحْذُوفٍ: نَصَبْنَا كَتِيبَةً مِثْلَ رَهْوَةَ", "of an omitted object: «we set up a squadron like Rahwa»", "mahzûf bir mef'ûlün: «Rehve gibi bir bölük diktik»"),
    (" — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ، حُذِفَ فِيهِ الْمُشَبَّهُ: «نَصَبْنَا خَيْلًا مِثْلَ هٰذَا الْجَبَلِ، أَوْ كَتِيبَةً ذَاتَ شَوْكَةٍ» (الزَّوْزَنِيُّ)؛ الْمُشَبَّهُ الْخَيْلُ أَوِ الْكَتِيبَةُ، وَالْمُشَبَّهُ بِهِ جَبَلُ رَهْوَةَ، وَالْأَدَاةُ «مِثْلَ»، وَوَجْهُ الشَّبَهِ غَيْرُ مَذْكُورٍ", " — a tashbih mursal mujmal with the likened thing left out: «we set up horsemen like this mountain, or a squadron with a sting» (al-Zawzanī); the horse or squadron is likened to Mount Rahwa; the particle is مِثْلَ; the point of likeness is not named", " — müşebbehi hazfedilmiş teşbîh-i mürsel mücmel: «bu dağ gibi atlılar yahut şevketli bir bölük diktik» (Zevzenî); müşebbeh atlılar ya da bölük, müşebbehün bih Rehve dağı, edat «misle»; vech-i şebeh zikredilmemiştir"))),
  R("mdf", "رَهْوَةَ", "rahwa-amr", pos="propn", sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ (الدُّرَّةُ)", " — by the fatha that stands for the kasra: a diptote, a proper name feminine in form (al-Durra)", " — alem ve lafzen müennes olduğu için gayr-i munsarif: kesre yerine fetha ile (Dürre)"), g=["mamnu-min-sarf"]),
  R("naatn", "ذَاتَ", "dhat", mud=True, n=DR("صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "a second adjective of the omitted noun", "mahzûf mevsûfun ikinci sıfatı")),
  R("mdf", "حَدٍّ", "hadd")],
 [R("lah", "مُحَافَظَةً", "muhafaza", n=N3(DR("وَقِيلَ: مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ، وَقِيلَ: حَالٌ", "some make it an absolute object of an omitted verb, others a hal", "mahzûf fiilin mef'ûl-i mutlakı, yahut hâl olduğu da söylenmiştir"), ZW("مُحَافَظَةً عَلَى أَحْسَابِنَا", "to guard our honour", "şereflerimizi korumak için"))),
  T("وَكُنَّا", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «نَصَبْنَا».",
    "The waw conjoins; كَانَ is a defective past verb built on sukun because نَا is attached, and نَا is its noun, in the seat of raf'; the clause is joined to «we set up».", "Vâv atıf harfi; «kâne» «nâ» bitiştiği için sükûn üzere mebnî nâkıs mâzî; «nâ» mahallen merfû ismidir; cümle «diktik»e ma'tûftur.", segs=SG(("وَ", "wa", "conj"), ("كُنَّا", "kana", "verb"))),
  R("khbk", "السَّابِقِينَا", "sabiq", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"], n=ZW("أَيْ سَبَقْنَا خُصُومَنَا: غَلَبْنَاهُمْ", "that is, we outstripped our foes — we overcame them", "yani hasımlarımızı geçtik: onları yendik"))])
VV(47, "with young men who count being killed a glory, and grey-heads tried and seasoned in wars.",
  "öldürülmeyi şeref sayan gençlerle ve savaşlarda denenmiş ak saçlılarla.",
 [R("majr", "بِشُبَّانٍ", "shabb", j="bi", g=["jam-taksir"], n=N3(DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ: نَغْلِبُ؛ وَرِوَايَتُهُ: «بِفِتْيَانٍ»", "the phrase hangs on an omitted verb, «we overcome»; his text reads «with youths (بِفِتْيَانٍ)»", "câr-mecrûr mahzûf bir fiile müteallik: «yeneriz»; onun rivayeti «bi-fityânin»dır"), ZW("نَسْبِقُ وَنَغْلِبُ بِشُبَّانٍ", "we outstrip and overcome with young men", "gençlerle öne geçer ve yeneriz"))),
  V("d5", "يَرَوْنَ", "raa", g=["naqis-verbs", "mafulayn", "al-mutaaddi-wa-afal-al-qulub"], n=NT("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«شُبَّانٍ»", "the clause is an adjective of «young men», in the seat of jarr", "cümle «gençler»in sıfatı, mahallen mecrûr")),
  R("maf1", "الْقَتْلَ", "qatl"),
  R("maf2", "مَجْدًا", "majd")],
 [R("atfj", "وَشِيبٍ", "ashyab", c="w", g=["jam-taksir", "tibaq"], of=("شُبَّانٍ", "young men", "gençler"), n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), HADD("طِبَاقٌ بَيْنَ «شُبَّانٍ» وَ«شِيبٍ»: الشَّبَابُ وَالشَّيْبُ ضِدَّانِ", "a ṭibāq between «young men» and «grey-heads»: youth and old age are contraries", "«gençler» ile «ak saçlılar» arasında tıbâk: gençlik ve ihtiyarlık zıttır"))),
  PR("فِي", "fi", n=MT("مُجَرَّبِينَا", "tried", "denenmiş»e")),
  R("majr", "الْحُرُوبِ", "harb", g=["jam-taksir"]),
  R("naatj", "مُجَرَّبِينَا", "mujarrab-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-maful"], n=ZW("وَشِيبٍ قَدْ مَرَنُوا عَلَى الْحُرُوبِ", "and grey-heads who have grown practised in wars", "savaşlara alışmış ak saçlılarla"))])
VV(48, "(We are) the challengers of all mankind, one and all, fighting their sons with swords in defence of our sons.",
  "(Biz) bütün insanlara meydan okuyanlarız, hepsine; çocuklarımızı korumak için onların oğullarıyla kılıç kılıca vuruşarak.",
 [R("khb", "حُدَيَّا", "hudayya-amr", mud=True, sign=S_AR, g=["hadhf-wa-taqdir"], n=N3(DR("لِمُبْتَدَإٍ مَحْذُوفٍ: نَحْنُ حُدَيَّا النَّاسِ؛ وَيَجُوزُ نَصْبُهُ عَلَى الْمَدْحِ، أَوْ عَلَى الْمَصْدَرِ", "of an omitted mubtada: «we are the challengers of mankind»; it may also be in nasb, in praise, or as a masdar", "mahzûf bir mübtedânın haberi: «biz insanların meydan okuyanlarıyız»; medh üzere, yahut masdar olarak mansûb da olabilir"), ZW("حُدَيَّا: اسْمٌ جَاءَ عَلَى صِيغَةِ التَّصْغِيرِ مِثْلَ ثُرَيَّا وَحُمَيَّا، وَهِيَ بِمَعْنَى التَّحَدِّي: نَتَحَدَّى النَّاسَ كُلَّهُمْ بِمِثْلِ مَجْدِنَا", "حُدَيَّا is a noun on the diminutive pattern, like ثُرَيَّا and حُمَيَّا, meaning challenge: we challenge all men to match our glory", "«hudeyyâ», «süreyyâ» ve «humeyyâ» gibi tasgîr kalıbında bir isimdir, meydan okuma anlamındadır: bütün insanlara şerefimizin benzerini getirsinler diye meydan okuruz"))),
  R("mdf", "النَّاسِ", "nas"),
  R("twkj", "كُلِّهِمُ", "kull", enc="هُمُ", of=("النَّاسِ", "mankind", "insanlar"), n=NT("وَضُمَّتِ الْمِيمُ لِلْوَزْنِ (صِلَةُ مِيمِ الْجَمْعِ)", "the mim takes a damma for the metre (the lengthening of the plural mim)", "mîm vezin için damme almıştır (cem' mîminin sılası)")),
  R("hal", "جَمِيعًا", "jamian", n=DR("مِنَ «النَّاسِ»، وَهِيَ حَالٌ مُؤَكِّدَةٌ", "of «mankind» — a hal that only strengthens", "«insanlar»dan hâl; te'kîd eden hâldir"))],
 [R("mutlaq", "مُقَارَعَةً", "muqaraa-amr", g=["masdar"], n=NT("لِفِعْلٍ مَحْذُوفٍ: نُقَارِعُ", "of an omitted verb, «we fight with swords»", "mahzûf bir fiilin: «kılıç kılıca vuruşuruz»")),
  R("maf", "بَنِيهِمْ", "banu", enc="هِمْ", sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"], n=NT("لِلْمَصْدَرِ «مُقَارَعَةً»", "of the masdar «fighting»", "«vuruşma» masdarının mef'ûlü")),
  PR("عَنْ", "an", n=MT("مُقَارَعَةً", "fighting", "vuruşma»ya")),
  R("majr", "بَنِينَا", "banu", enc="نَا", sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"], n=ZW("أَيْ نُضَارِبُهُمْ بِالسُّيُوفِ ذَبًّا عَنْ أَبْنَائِنَا، حِمَايَةً لِلْحَرِيمِ", "that is, we fight them with swords defending our sons, guarding our women", "yani oğullarımızı savunarak, harimimizi koruyarak onlarla kılıç kılıca vuruşuruz"))])
VV(49, "On the day we fear for them, our horses become troops and bands (scattered everywhere);",
  "Onlar için korktuğumuz günde atlılarımız bölük bölük, takım takım olur;",
 [PT("فَأَمَّا", "amma", "حَرْفُ شَرْطٍ وَتَفْصِيلٍ", "the particle of condition and detailing («as for»)", "şart ve tafsîl harfi", c="fi", g=["amma-tafsiliyya"]),
  R("zarfz", "يَوْمَ", "yawm", mud=True, n=MZ("تُصْبِحُ", "become", "olur»a")),
  R("mdf", "خَشْيَتِنَا", "khashya-amr", enc="نَا", g=["masdar"], n=NT("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti")),
  JP("عَلَيْهِمْ", "ala", "هِمْ", n=N3(MT("خَشْيَتِنَا", "our fear", "korkumuz»a"), ZW("أَيْ عَلَى أَبْنَائِنَا وَحُرَمِنَا مِنَ الْأَعْدَاءِ", "that is, for our sons and our women, from the enemy", "yani oğullarımız ve harimimiz için düşmandan")))],
 [V("d", "فَتُصْبِحُ", "asbaha", c="fj", g=["kana-wa-akhawatuha", "form-iv-verbs", "amma-tafsiliyya"], n=NT("وَهُوَ فِعْلٌ نَاقِصٌ؛ وَالْجُمْلَةُ جَوَابُ «أَمَّا» لَا مَحَلَّ لَهَا", "it is a defective verb; the clause is the answer of أَمَّا and has no seat", "nâkıs fiildir; cümle «emmâ»nın cevabıdır, mahalli yoktur")),
  R("ismas", "خَيْلُنَا", "khayl", enc="نَا"),
  R("khbas", "عُصَبًا", "usba", g=["jam-taksir"], n=ZW("الْعُصَبُ: جَمْعُ عُصْبَةٍ، وَهِيَ مَا بَيْنَ الْعَشَرَةِ وَالْأَرْبَعِينَ؛ أَيْ تَتَفَرَّقُ فِي كُلِّ وَجْهٍ لِذَبِّ الْأَعْدَاءِ عَنِ الْحُرَمِ", "عُصَب is the plural of عُصْبَة, a band of ten to forty; that is, they spread in every direction to drive the enemy off our women", "«usab», on ile kırk arası topluluk olan «usbe»nin cem'idir; yani düşmanı harimden uzaklaştırmak için her yöne dağılır")),
  R("khbas2", "ثُبِينَا", "thuba", sign=S_MULHAQ_I, g=["jam-mudhakkar-salim"], n=ZW("الثُّبَةُ: الْجَمَاعَةُ، وَالْجَمْعُ الثُّبَاتُ، وَالثُّبُونَ فِي الرَّفْعِ وَالثُّبِينَ فِي النَّصْبِ وَالْجَرِّ", "ثُبَة is a band; the plural is ثُبَات, or ثُبُونَ in raf' and ثُبِينَ in nasb and jarr", "«sube»: topluluk; cem'i «subât», ref'de «subûne», nasb ve cerde «subîne»"))])
VV(50, "and on the day we do not fear for them, we press hard on the raid, clad in our arms.",
  "onlar için korkmadığımız günde ise silahlarımızı kuşanmış olarak akında ileri gideriz.",
 [PT("وَأَمَّا", "amma", "حَرْفُ شَرْطٍ وَتَفْصِيلٍ", "the particle of condition and detailing («as for»)", "şart ve tafsîl harfi", c="w", g=["amma-tafsiliyya"]),
  R("zarfz", "يَوْمَ", "yawm", mud=True, n=MZ("نُمْعِنُ", "press hard", "ileri gideriz»e")),
  LA_N(),
  V("da", "نَخْشَى", "khashiya", doer=NAHNU, g=["naqis-verbs", "tibaq"], n=N3(CL("mdf", "يَوْمَ", "day", "gün"), HADD("طِبَاقُ السَّلْبِ بَيْنَ «خَشْيَتِنَا» فِي الْبَيْتِ قَبْلَهُ وَ«لَا نَخْشَى»: الْمَعْنَى الْوَاحِدُ مُثْبَتًا ثُمَّ مَنْفِيًّا", "a ṭibāq of negation between «our fear» in the verse before and «we do not fear»: one meaning affirmed, then denied", "önceki beyitteki «korkumuz» ile «korkmayız» arasında selb tıbâkı: aynı mâna önce müspet, sonra menfî"))),
  JP("عَلَيْهِمْ", "ala", "هِمْ", n=MT("نَخْشَى", "fear", "korkmayız»a"))],
 [V("d", "فَنُمْعِنُ", "amana-persist", c="fj", doer=NAHNU, g=["form-iv-verbs"], n=N3(NT("وَالْجُمْلَةُ جَوَابُ «أَمَّا» لَا مَحَلَّ لَهَا", "the clause is the answer of أَمَّا and has no seat", "cümle «emmâ»nın cevabıdır, mahalli yoktur"), ZW("الْإِمْعَانُ: الْإِسْرَاعُ وَالْمُبَالَغَةُ فِي الشَّيْءِ", "إِمْعَان is going fast and far in a thing", "«im'ân»: bir işte hızlanmak ve ileri gitmek"), DR("وَرِوَايَتُهُ لِلشَّطْرِ: «فَنُصْبِحُ فِي مَجَالِسِنَا ثُبِينَا»، وَذَكَرَ هٰذِهِ الرِّوَايَةَ", "his text of this hemistich is «we sit in our gatherings in bands»; he mentions this reading too", "onun rivayetinde bu mısra «meclislerimizde takım takım otururuz»dur; bu rivayeti de zikreder"))),
  T("غَارَةً", "ghara-ant", "noun", ["hadhf-al-jarr"], "مَنْصُوبٌ عَلَى نَزْعِ الْخَافِضِ بِالْفَتْحَةِ: فَنُمْعِنُ فِي الْغَارَةِ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ: «فَنُمْعِنُ فِي الْإِغَارَةِ عَلَى الْأَعْدَاءِ».",
    "In nasb by the dropping of the jarr letter: «we press hard in the raid», as al-Zawzanī glosses it: «we press hard in raiding the enemy».", "Cer harfinin düşmesiyle fetha ile mansûb: «akında ileri gideriz»; Zevzenî'nin açıklaması gibi: «düşmana akın etmekte ileri gideriz»."),
  R("hal", "مُتَلَبِّبِينَا", "mutalabbib-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"], n=N3(NT("مِنْ فَاعِلِ «نُمْعِنُ»", "of the doer of «we press hard»", "«ileri gideriz»in fâilinden"), ZW("التَّلَبُّبُ: لُبْسُ السِّلَاحِ؛ لَابِسِينَ أَسْلِحَتَنَا", "تَلَبُّب is putting on arms: wearing our weapons", "«telebbüb»: silah kuşanmak; silahlarımızı kuşanmış olarak")))])
# ---- vv. 51–57 — إِلَى عَمْرِو بْنِ هِنْدٍ ----
JUSHAM_S = ("بِالْكَسْرَةِ — عَلَى أَنَّهُ مَصْرُوفٌ حُذِفَ تَنْوِينُهُ لِوَصْفِهِ بِـ«ابْنِ» بَيْنَ عَلَمَيْنِ، كَمَا ضَبَطَتْهُ الطَّبْعَةُ", " — by the kasra, treated as declinable, its tanwin dropped because ابْن between two names describes it, as the edition vowels it", " — kesre ile; baskının harekelediği gibi munsarif sayılmış, iki alem arasında «ibn» ile nitelendiği için tenvini düşmüştür")
ISTF_INKAR = lambda z_ar, z_en, z_tr: (" — وَفِيهِ اسْتِفْهَامٌ خَرَجَ عَنْ حَقِيقَتِهِ إِلَى الْإِنْكَارِ وَالنَّفْيِ، بَيَّنَهُ الزَّوْزَنِيُّ: «" + z_ar + "»", " — a question that leaves its true sense for denial, as al-Zawzanī makes plain: «" + z_en + "»", " — hakikî anlamından inkâr ve nefye çıkmış soru; Zevzenî açıklar: «" + z_tr + "»")
def AMR_IBN_HIND():
    return [T("عَمْرَو", "amr-name", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مَبْنِيٌّ عَلَى الْفَتْحِ إِتْبَاعًا لِفَتْحَةِ «ابْنَ» بَعْدَهُ، فِي مَحَلِّ نَصْبٍ؛ وَيَجُوزُ ضَمُّهُ (الدُّرَّةُ).",
              "A single proper-name vocative, its particle left out, built on fatha to match the fatha of ابْنَ after it, in the seat of nasb; it may also take damma (al-Durra).", "Nidâ harfi mahzûf müfred alem münâdâ; sonraki «ibne»nin fethasına uyarak fetha üzere mebnî, mahallen mansûb; dammeli de olabilir (Dürre)."),
            R("naatn", "بْنَ", "ibn", mud=True, of=("عَمْرَو", "ʿAmr", "Amr"), n=NT("عَلَى مَحَلِّ الْمُنَادَى", "following the vocative's seat", "münâdânın mahalline göre")),
            R("mdf", "هِنْدٍ", "hind", pos="propn")]
VV(51, "— with a chief of the Banū Jusham ibn Bakr, with whom we crush the plain ground and the rugged.",
  "— Benî Cüşem b. Bekr'den bir reisle; onunla düz yeri de sarp yeri de ezeriz.",
 [R("majr", "بِرَأْسٍ", "ras", j="bi", n=N3(DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ: نَجِيءُ أَوْ نُغِيرُ", "the phrase hangs on an omitted verb: «we come» or «we raid»", "câr-mecrûr mahzûf bir fiile müteallik: «geliriz» yahut «akın ederiz»"), ZW("الرَّأْسُ: الرَّئِيسُ وَالسَّيِّدُ", "رَأْس is the chief, the lord", "«re's»: reis, efendi"))),
  PR("مِنْ", "min", n=MTH("صِفَةٍ لِـ«رَأْسٍ»", "an omitted adjective of «a chief»", "«reis»in mahzûf sıfatına")),
  R("majr", "بَنِي", "banu", mud=True, sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"]),
  R("mdf", "جُشَمِ", "jusham-amr", pos="propn", sign=JUSHAM_S),
  R("naatj", "بْنِ", "ibn", mud=True, of=("جُشَمِ", "Jusham", "Cüşem")),
  R("mdf", "بَكْرٍ", "bakr", pos="propn")],
 [V("d", "نَدُقُّ", "daqqa", doer=NAHNU, g=["doubled-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ الْفِعْلِ الْمَحْذُوفِ، وَالِاسْتِئْنَافُ مُمْكِنٌ", "the clause is a hal of the doer of the omitted verb, in the seat of nasb; it may also open a fresh sentence", "cümle mahzûf fiilin fâilinden hâl, mahallen mansûb; müste'nef de olabilir")),
  JP("بِهِ", "bi", "هِ", n=MT("نَدُقُّ", "crush", "ezeriz»e")),
  R("maf", "السُّهُولَةَ", "suhula-amr", g=["kinaya", "tibaq"], n=N3(
    (" — وَفِيهِ كِنَايَةٌ بَيَّنَهَا الزَّوْزَنِيُّ: «نَدُقُّ بِهِ السَّهْلَ وَالْحَزْنَ، أَيْ نَهْزِمُ الضِّعَافَ وَالْأَشِدَّاءَ»", " — a kināya that al-Zawzanī makes plain: «we crush with him the plain and the rugged, that is, we rout the weak and the strong»", " — Zevzenî'nin açıkladığı kinâye: «onunla düz yeri ve sarp yeri ezeriz, yani zayıfları da güçlüleri de bozguna uğratırız»"),
    HADD("طِبَاقٌ بَيْنَ «السُّهُولَةَ» وَ«الْحُزُونَا»: السَّهْلُ وَالْحَزْنُ ضِدَّانِ", "a ṭibāq between «the plain» and «the rugged», which are contraries", "«düz» ile «sarp» arasında tıbâk: ikisi zıttır"))),
  R("atfn", "وَالْحُزُونَا", "hazn", c="w", g=["jam-taksir"], of=("السُّهُولَةَ", "the plain", "düz yer"), n=ITLAQ)])
VV(52, "Let the peoples not think we have been broken and humbled, and that we have grown slack.",
  "Kavimler bizim kırılıp zelil olduğumuzu ve gevşediğimizi bilmesin — (biz öyle değiliz).",
 [PT("أَلَا", "ala-tanbih", "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ لَا عَمَلَ لَهُ", "a particle that opens the speech and calls attention; it governs nothing", "istiftâh ve tenbîh harfi, ameli yoktur", g=["huruf-tanbih"]),
  LA_N(),
  V("d", "يَعْلَمُ", "alima", g=["al-mutaaddi-wa-afal-al-qulub"], n=N3(CL("ist"), ZW("أَيْ لَسْنَا بِهٰذِهِ الصِّفَةِ فَتَعْلَمَنَا الْأَقْوَامُ بِهَا", "that is, we are not like that, for the peoples to know us so", "yani biz öyle değiliz ki kavimler bizi öyle bilsin"), DR("وَرِوَايَتُهُ: «أَلَا لَا يَحْسَبِ الْأَعْدَاءُ»، بِـ«لَا» النَّاهِيَةِ", "his text reads «let the enemy not reckon», with the لَا of forbidding", "onun rivayeti «elâ lâ yahsebi'l-a'dâ»dır, nehiy «lâ»sıyla"))),
  R("fail", "الْأَقْوَامُ", "qawm", g=["jam-taksir"]),
  INNA("أَنَّا", "anna", enc="نَا", n=NT("وَحُذِفَتْ إِحْدَى النُّونَاتِ لِلتَّخْفِيفِ؛ وَ«أَنَّ» وَمَعْمُولَاهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «يَعْلَمُ»", "one nun dropped for ease; أَنَّ with its two terms makes a masdar standing for the two objects of «know»", "nûnlardan biri hafiflik için düşmüştür; «enne» ve iki ma'mûlü «bilir»in iki mef'ûlü yerine geçen bir masdar olur"))],
 [V("mna", "تَضَعْضَعْنَا", "tadaada-amr", g=["rubai-babs"], n=N3(CL("khb", "أَنَّ", "أَنَّ", "enne"), ZW("التَّضَعْضُعُ: التَّكَسُّرُ وَالتَّذَلُّلُ؛ ضَعْضَعْتُهُ فَتَضَعْضَعَ، أَيْ كَسَرْتُهُ فَانْكَسَرَ", "تَضَعْضُع is being broken and humbled: «I broke it and it broke»", "«tada'du'»: kırılıp zelil olmak; «onu kırdım, o da kırıldı»"))),
  INNA("وَأَنَّا", "anna", enc="نَا", c="w", n=NT("وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْأَوَّلِ", "the masdar it makes is joined to the first", "oluşan masdar birincisine ma'tûftur")),
  QAD(),
  V("mna", "وَنِينَا", "wana", g=["naqis-verbs", "mithal-verbs"], n=N3(CL("khb", "أَنَّ", "أَنَّ", "enne"), ZW("الْوَنَى: الْفُتُورُ", "وَنًى is slackening", "«venâ»: gevşeklik"), NT("وَكُسِرَتْ نُونُهُ عَلَى «فَعِلَ» لِيَكُونَ رِدْفُ الْقَافِيَةِ يَاءً؛ وَالْمَشْهُورُ: وَنَى يَنِي", "its nun is given kasra (on فَعِلَ) so that the rhyme's ridf is a ya; the common form is وَنَى يَنِي", "ridfi yâ olsun diye nûnu kesreli («fa'ile») gelmiştir; meşhuru «venâ yenî»dir"), DR("وَرِوَايَتُهُ: «وَأَنَّا قَدْ فَنِينَا»", "his text reads «and that we have perished»", "onun rivayeti «ve ennâ kad fenînâ»dır")))])
VV(53, "Let none act the fool against us, or we shall play the fool beyond the folly of the fools.",
  "Hiç kimse bize karşı cahillik etmesin; yoksa biz de cahillerin cahilliğinden öte cahillik ederiz.",
 [PT("أَلَا", "ala-tanbih", "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ لَا عَمَلَ لَهُ", "a particle that opens the speech and calls attention; it governs nothing", "istiftâh ve tenbîh harfi, ameli yoktur", g=["huruf-tanbih"]),
  PT("لَا", "la-nahiya", "لَا نَاهِيَةٌ جَازِمَةٌ", "لَا of forbidding, which puts the verb in jazm", "cezmeden nehiy «lâ»sı", g=["la-nahiya"]),
  T("يَجْهَلَنْ", "jahila", "verb", ["nun-tawkid", "la-nahiya"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الْخَفِيفَةِ، فِي مَحَلِّ جَزْمٍ بِـ«لَا» النَّاهِيَةِ، وَالنُّونُ حَرْفُ تَوْكِيدٍ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "A present verb built on fatha because the light nun of emphasis is attached, in the seat of jazm by the لَا of forbidding; the nun is a particle of emphasis; the sentence is a fresh one.", "Hafif te'kîd nûnu bitiştiği için fetha üzere mebnî muzâri, nehiy «lâ»sıyla mahallen meczûm; nûn te'kîd harfidir; cümle müste'neftir.",
    segs=SG(("يَجْهَلَ", "jahila", "verb"), ("نْ", "nun-tawkid-khafifa", "part"))),
  R("fail", "أَحَدٌ", "ahad"),
  JP("عَلَيْنَا", "ala", "نَا", n=MT("يَجْهَلَنْ", "act the fool", "cahillik etmesin»e"))],
 [V(NS("بِـ«أَنْ» مُضْمَرَةً بَعْدَ فَاءِ السَّبَبِيَّةِ فِي جَوَابِ النَّهْيِ", "by an أَنْ understood after the fa of cause, in answer to the forbidding", "nehyin cevabında sebebiyye fâsından sonra gizli «en» ile"), "فَنَجْهَلَ", "jahila", c="fs", doer=NAHNU, g=["mushakala", "jawab-al-talab"], n=N3(DR("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَعْطُوفٍ بِالْفَاءِ عَلَى مَصْدَرٍ مُتَصَيَّدٍ مِمَّا قَبْلَهُ: لَا يَكُنْ جَهْلٌ مِنْ أَحَدٍ فَجَهْلٌ مِنَّا", "أَنْ and the verb make a masdar joined by the fa to one drawn from what precedes: «let there be no folly from anyone, and (then) folly from us»", "«en» ile fiil, öncekinden çıkarılan bir masdara fâ ile ma'tûf masdar olur: «kimseden cahillik olmasın ki bizden de cahillik olmasın»"),
    (" — وَفِيهِ الْمُشَاكَلَةُ وَصَفَهَا الزَّوْزَنِيُّ: «فَسُمِّيَ جَزَاءُ الْجَهْلِ جَهْلًا لِازْدِوَاجِ الْكَلَامِ وَحُسْنِ تَجَانُسِ اللَّفْظِ»، وَاسْتَشْهَدَ لَهَا بِقَوْلِهِ تَعَالَى: ﴿وَجَزَاءُ سَيِّئَةٍ سَيِّئَةٌ مِثْلُهَا﴾ ﴿وَمَكَرُوا وَمَكَرَ اللَّهُ﴾", " — mushākala, which al-Zawzanī describes: «the requital of folly is called folly for the pairing of the words and the beauty of their likeness», citing «the requital of an evil is an evil like it» and «they plotted, and God plotted»", " — Zevzenî'nin tarif ettiği müşâkele: «sözün eşleşmesi ve lafzın güzel uyumu için cahilliğin cezasına cahillik denmiştir»; buna «Bir kötülüğün cezası onun gibi bir kötülüktür» ve «Onlar tuzak kurdular, Allah da tuzak kurdu» âyetlerini delil getirir"))),
  R("zarfm", "فَوْقَ", "fawqa", mud=True, n=MZ("نَجْهَلَ", "play the fool", "cahillik ederiz»e")),
  R("mdf", "جَهْلِ", "jahl", mud=True, n=DR("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "a masdar annexed to its doer", "masdarın fâiline izâfeti")),
  R("mdf", "الْجَاهِلِينَا", "jahil", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail", "mulhaq-bil-jinas"], n=HADD("مُلْحَقٌ بِالْجِنَاسِ: «يَجْهَلَنْ» وَ«نَجْهَلَ» وَ«جَهْلِ» وَ«الْجَاهِلِينَا» يَجْمَعُهَا الِاشْتِقَاقُ", "a figure joined to jinās: «act the fool», «play the fool», «folly» and «the fools» share one derivation", "cinâsa mülhak: «cahillik etmesin», «cahillik ederiz», «cahillik» ve «cahiller»i iştikak birleştirir"))])
VV(54, "By what will, ʿAmr ibn Hind, should we be servants to your underlings?",
  "Hangi dilekle, ey Amr b. Hind, senin küçük krallarına hizmetçi olalım?",
 [R("majr", "بِأَيِّ", "ayy", j="bi", mud=True, g=["khuruj-al-istifham", "al-istifham"], n=N3(MT("نَكُونُ", "should we be", "olalım»a"), ISTF_INKAR("أَيُّ شَيْءٍ دَعَاكَ إِلَى هٰذِهِ الْمَشِيئَةِ الْمُحَالَةِ؟ يُرِيدُ أَنَّهُ لَمْ يَظْهَرْ مِنْهُمْ ضَعْفٌ يُطْمِعُ الْمَلِكَ فِي إِذْلَالِهِمْ", "what led you to this impossible wish? He means no weakness of theirs has shown that might tempt the king to humble them", "seni bu olmayacak dileğe ne sevk etti? Kralı onları zelil etmeye heveslendirecek bir zaaflarının görünmediğini kasteder"))),
  R("mdf", "مَشِيئَةٍ", "mashia")] + AMR_IBN_HIND(),
 [T("نَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا.",
    "A defective present verb in raf'; its noun is the hidden «we»; the sentence is a fresh one with no seat.", "Merfû nâkıs muzâri; ismi gizli «biz» zamiridir; cümle müste'neftir, mahalli yoktur."),
  R("majr", "لِقَيْلِكُمْ", "qayl-amr", j="li", enc="كُمْ", n=N3(MT("قَطِينًا", "servants", "hizmetçi»ye"), ZW("الْقَيْلُ: الْمَلِكُ دُونَ الْمَلِكِ الْأَعْظَمِ", "a قَيْل is a king below the great king", "«kayl»: büyük kralın altındaki kral"))),
  JP("فِيهَا", "fi", "هَا", n=N3(MT("نَكُونُ", "be", "olalım»a"), NT("وَالْهَاءُ لِلْمَشِيئَةِ", "the ha refers to the will", "hâ dileğe döner"))),
  R("khbk", "قَطِينًا", "lb-qatin", n=N3(TANW_ALIF, ZW("الْقَطِينُ: الْخَدَمُ", "قَطِين is servants", "«katîn»: hizmetçiler")))])
VV(55, "By what will, ʿAmr ibn Hind, do you heed the slanderers against us and make light of us?",
  "Hangi dilekle, ey Amr b. Hind, bizim hakkımızda koğucuları dinliyor ve bizi hor görüyorsun?",
 [R("majr", "بِأَيِّ", "ayy", j="bi", mud=True, g=["khuruj-al-istifham", "al-istifham", "asbab-al-itnab"], n=N3(MT("تُطِيعُ", "do you heed", "dinliyorsun»a"), ISTF_INKAR("أَيُّ شَيْءٍ دَعَاكَ إِلَى هٰذِهِ الْمَشِيئَةِ؟ أَيْ لَمْ يَظْهَرْ مِنَّا ضَعْفٌ يُطْمِعُ الْمَلِكَ فِينَا", "what led you to this wish? That is, no weakness of ours has shown that might tempt the king", "seni bu dileğe ne sevk etti? Yani kralı bize heveslendirecek bir zaafımız görünmedi"),
    HADD("إِطْنَابٌ بِالتَّكْرِيرِ: أَعَادَ صَدْرَ الْبَيْتِ قَبْلَهُ بِلَفْظِهِ لِتَأْكِيدِ الْإِنْكَارِ", "an iṭnāb by repetition: he repeats the first half of the verse before, word for word, to press the denial", "tekrîr yoluyla ıtnâb: inkârı pekiştirmek için önceki beytin ilk mısraını aynen tekrarlar"))),
  R("mdf", "مَشِيئَةٍ", "mashia")] + AMR_IBN_HIND(),
 [V("d", "تُطِيعُ", "ataa", doer=ANTA, g=["form-iv-verbs", "hollow-verbs"], n=CL("ist")),
  JP("بِنَا", "bi", "نَا", n=MT("تُطِيعُ", "heed", "dinliyorsun»a")),
  R("maf", "الْوُشَاةَ", "washin", g=["jam-taksir"]),
  V("dy", "وَتَزْدَرِينَا", "izdara-amr", c="w", enc="نَا", doer=ANTA, g=["form-viii-verbs", "naqis-verbs"], n=N3(CL("atf", "تُطِيعُ", "heed", "dinliyorsun"), ZW("ازْدَرَاهُ وَازْدَرَى بِهِ: قَصَّرَ بِهِ وَاحْتَقَرَهُ", "اِزْدَرَاهُ and اِزْدَرَى بِهِ: to belittle him, to despise him", "«izderâhu» ve «izderâ bihî»: onu küçümsedi, hor gördü")))])
VV(56, "Threaten us and menace us — gently! When were we ever servants to your mother?",
  "Bizi tehdit et, korkut — yavaş ol! Biz ne zaman annenin hizmetçisi olduk ki?",
 [V("a", "تَهَدَّدْنَا", "tahaddada-amr", enc="نَا", doer=ANTA, g=["form-v-verbs", "imperative-amr", "al-amr-wa-wujuhuh"], n=N3(CL("ibt"), DR("وَيُرْوَى: «تُهَدِّدُنَا وَتُوعِدُنَا» مُضَارِعَيْنِ مَرْفُوعَيْنِ — وَهُوَ عِنْدَ الزَّوْزَنِيِّ إِخْبَارٌ", "it is also read «you threaten us and menace us», two present verbs in raf' — for al-Zawzanī a statement", "«tühedidunâ ve tû'idunâ» diye iki merfû muzâri olarak da rivayet edilir — Zevzenî'ye göre o zaman haberdir"),
    (" — وَفِيهِ أَمْرٌ خَرَجَ عَنْ حَقِيقَتِهِ إِلَى الْإِهَانَةِ وَقِلَّةِ الْمُبَالَاةِ، بَيَّنَهُ الزَّوْزَنِيُّ: «لَمْ نَكُنْ خَدَمًا لَهَا حَتَّى نَعْبَأَ بِتَهْدِيدِكَ وَوَعِيدِكَ إِيَّانَا»", " — a command that leaves its true sense for contempt and unconcern, as al-Zawzanī makes plain: «we were never her servants, that we should care for your threats and menaces»", " — hakikî anlamından aşağılama ve umursamazlığa çıkmış emir; Zevzenî açıklar: «onun hizmetçileri olmadık ki tehdidini ve korkutmanı umursayalım»"))),
  V("a", "وَأَوْعِدْنَا", "awada", c="w", enc="نَا", doer=ANTA, g=["form-iv-verbs", "mithal-verbs"], n=CL("atf", "تَهَدَّدْنَا", "threaten us", "tehdit et")),
  T("رُوَيْدًا", "ruwaydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ تَصْغِيرُ «إِرْوَادٍ» تَصْغِيرَ التَّرْخِيمِ (الدُّرَّةُ) — أَيْ تَرَفَّقْ فِي تَهَدُّدِنَا وَإِيعَادِنَا وَلَا تُمْعِنْ فِيهِمَا (الزَّوْزَنِيُّ).",
    "An absolute object of an omitted verb, in nasb; it is the shortened diminutive of إِرْوَاد (al-Durra) — that is, go gently in threatening and menacing us, do not press it (al-Zawzanī).", "Mahzûf bir fiilin mef'ûl-i mutlakı, mansûb; «irvâd»ın terhîmli tasgîridir (Dürre) — yani bizi tehdit ve korkutmada yavaş ol, ileri gitme (Zevzenî).")],
 [T("مَتَى", "mata-istifham", "pron", ["al-istifham", "khuruj-al-istifham", "maful-fih"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ، مُتَعَلِّقٌ بِـ«كُنَّا» — وَفِيهِ اسْتِفْهَامٌ خَرَجَ إِلَى النَّفْيِ، بَيَّنَهُ الزَّوْزَنِيُّ: «أَيْ لَمْ نَكُنْ خَدَمًا لَهَا».",
    "A noun of question built on sukun, in the seat of nasb as an adverb of time, hanging on «we were» — a question that leaves its sense for denial, as al-Zawzanī makes plain: «that is, we were never her servants».", "Sükûn üzere mebnî soru ismi, zaman zarfı olarak mahallen mansûb, «olduk»a müteallik — nefye çıkmış soru; Zevzenî açıklar: «yani biz onun hizmetçileri olmadık»."),
  T("كُنَّا", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "A defective past verb built on sukun because نَا is attached, and نَا is its noun, in the seat of raf'; the sentence is a fresh one.", "«Nâ» bitiştiği için sükûn üzere mebnî nâkıs mâzî; «nâ» mahallen merfû ismidir; cümle müste'neftir."),
  R("majr", "لِأُمِّكَ", "umm", j="li", enc="كَ", n=MT("مُقْتَوِينَا", "servants", "hizmetçi»ye")),
  R("khbk", "مُقْتَوِينَا", "maqtawi-amr", sign=S_JMSI, g=["jam-mudhakkar-salim"], n=ZW("الْقَتْوُ: خِدْمَةُ الْمُلُوكِ … تَنْسُبُ إِلَيْهِ فَتَقُولُ: مَقْتَوِيٌّ، ثُمَّ يُجْمَعُ مَعَ طَرْحِ يَاءِ النِّسْبَةِ فَيُقَالُ: مَقْتَوُونَ فِي الرَّفْعِ، وَمَقْتَوِينَ فِي الْجَرِّ وَالنَّصْبِ", "قَتْو is serving kings … its nisba is مَقْتَوِيّ, whose plural drops the nisba ya: مَقْتَوُونَ in raf', مَقْتَوِينَ in jarr and nasb", "«katv»: krallara hizmet … nisbeti «maktevî»dir; nisbet yâsı atılarak cem'lenir: ref'de «maktevûne», cer ve nasbda «maktevîne»"))])
VV(57, "For our spear-shaft, ʿAmr, has defied the foe before you, refusing to bend.",
  "Çünkü bizim mızrağımız, ey Amr, senden önce de düşmanlara eğilmekten diretti.",
 [INNA("فَإِنَّ", c="fi"),
  R("ismi", "قَنَاتَنَا", "qana", enc="نَا", g=IST_G, n=ISTZ("الْقَنَاةِ", "the spear-shaft", "mızrak", "الْعَرَبُ تَسْتَعِيرُ لِلْعِزِّ اسْمَ الْقَنَاةِ؛ يُرِيدُ أَنَّ عِزَّهُمْ أَبَى أَنْ يَزُولَ … مَنِيعٌ لَا يُرَامُ", "the Arabs borrow the name of the spear-shaft for might; he means their might refused to pass away … unassailable", "Araplar izzet için mızrağın adını istiâre eder; izzetlerinin yok olmaktan diretip … dokunulmaz olduğunu kasteder")),
  PT("يَا", "ya-nida", "حَرْفُ نِدَاءٍ", "the particle of calling", "nidâ harfi", g=["vocative-munada"]),
  T("عَمْرُو", "amr-name", "propn", ["vocative-munada", "jumla-mutarida"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ؛ وَجُمْلَةُ النِّدَاءِ مُعْتَرِضَةٌ بَيْنَ اسْمِ «إِنَّ» وَخَبَرِهَا لَا مَحَلَّ لَهَا.",
    "A single proper-name vocative built on damma, in the seat of nasb; the call stands between the noun of إِنَّ and its predicate and has no seat.", "Müfred alem münâdâ, damme üzere mebnî, mahallen mansûb; nidâ cümlesi «inne»nin ismi ile haberi arasında mu'tarızadır, mahalli yoktur."),
  T("أَعْيَتْ", "aya4-amr", "verb", ["form-iv-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «قَنَاتَنَا»؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «إِنَّ» — أَيْ أَبَتْ (الزَّوْزَنِيُّ).",
    "A past verb built on a fatha estimated on the alif dropped where two quiescents meet; the ta marks the feminine; the doer is the hidden «she» — our spear-shaft; the clause is the predicate of إِنَّ, in the seat of raf' — that is, it refused (al-Zawzanī).", "İki sâkin buluştuğu için düşen elif üzerinde takdîrî fetha üzere mebnî mâzî; tâ te'nîs içindir; fâil «mızrağımız»a dönen gizli «o»dur; cümle «inne»nin haberi, mahallen merfû — yani diretti (Zevzenî).")],
 [PR("عَلَى", "ala", n=MT("أَعْيَتْ", "defied", "diretti»ye")),
  R("majr", "الْأَعْدَاءِ", "aduww", g=["jam-taksir"]),
  R("zarfz", "قَبْلَكَ", "qabla", enc="كَ", n=DR("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْأَعْدَاءِ»", "it hangs on an omitted hal of «the foe»", "«düşmanlar»ın mahzûf hâline müteallik")),
  AN(n=DR("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِحَرْفِ جَرٍّ مَحْذُوفٍ: بِأَنْ تَلِينَ، أَوْ لِأَنْ تَلِينَ", "أَنْ and the verb make a masdar in jarr by an omitted jarr letter: «at bending» or «for bending»", "«en» ile fiil, mahzûf bir cer harfiyle mecrûr masdar olur: «eğilmekte» yahut «eğilmek için»")),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "تَلِينَا", "lana", doer=HIYA("الْقَنَاةِ", "the spear-shaft", "mızrağa"), g=["hollow-verbs", "tarshih-wa-tajrid"], n=N3(ITLAQ, HADD("تَرْشِيحٌ لِلِاسْتِعَارَةِ: ذَكَرَ اللِّينَ، وَهُوَ مِمَّا يُلَائِمُ الْمُسْتَعَارَ مِنْهُ (الْقَنَاةَ)", "a tarshīḥ of the istiʿāra: he names bending, which belongs to what is borrowed from (the spear-shaft)", "istiârenin terşîhi: müsteârun minh olan mızrağa uygun düşen eğilmeyi zikretmiştir")))])
# ---- vv. 58–64 — الْقَنَاةُ الْعَصِيَّةُ، وَالْآبَاءُ ----
VK["mtn"] = (_M + "فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ", "past verb built on a fatha estimated on the alif dropped where two quiescents meet (the ta marks the feminine)", "iki sâkin buluştuğu için düşen elif üzerinde takdîrî fetha üzere mebnî mâzî (tâ te'nîs içindir)")
QANAT = HIYA("الْقَنَاةِ", "the spear-shaft", "mızrağa")
def HUDDITHTA(n=NO):
    return T("حُدِّثْتَ", "haddatha", "verb", ["naib-al-fail", "al-bariz-al-muttasil", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْمُخَاطَبِ، وَالتَّاءُ " + _FAN + "، وَهِيَ مَفْعُولُهُ الْأَوَّلُ" + n[0] + ".",
             "A passive past verb built on sukun because the ta of the one addressed is attached; that ta is the deputy doer, in the seat of raf' — the verb's first object" + n[1] + ".", "Meçhul mâzî, muhâtab tâsı bitiştiği için sükûn üzere mebnî; tâ nâib-i fâildir, mahallen merfû — fiilin birinci mef'ûlü" + n[2] + ".")
VV(58, "When the straightening-iron bites on it, it recoils, and turns on it hard and kicking back.",
  "Düzeltme demiri onu ısırdığında tiksinip çekilir ve ona sert, tepen (bir mızrak) olarak döner.",
 [IDHA(),
  V("m", "عَضَّ", "adda-bite", g=["doubled-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  R("fail", "الثِّقَافُ", "thiqaf-amr", n=ZW("الثِّقَافُ: الْحَدِيدَةُ الَّتِي يُقَوَّمُ بِهَا الرُّمْحُ", "ثِقَاف is the iron with which a spear is straightened", "«sikâf»: mızrağın düzeltildiği demir")),
  JP("بِهَا", "bi", "هَا", n=N3(MT("عَضَّ", "bites", "ısırdı»ya"), NT("وَالْهَاءُ لِلْقَنَاةِ", "the ha is the spear-shaft", "hâ mızrağa döner"))),
  V("mt", "اشْمَأَزَّتْ", "ishmaazza-amr", doer=QANAT, g=["rubai-babs", "majaz-murakkab", "aqsam-al-istiara"], n=N3(CL("jawab"),
    (" — وَفِيهِ اسْتِعَارَةٌ تَمْثِيلِيَّةٌ وَصَفَهَا الزَّوْزَنِيُّ: «جَعَلَ الْقَنَاةَ الَّتِي لَا يَتَهَيَّأُ تَقْوِيمُهَا مَثَلًا لِعِزَّتِهِمُ الَّتِي لَا تَضَعْضَعُ، وَجَعَلَ قَهْرَهَا مَنْ تَعَرَّضَ لِهَدْمِهَا كَنِفَارِ الْقَنَاةِ مِنَ التَّقْوِيمِ»", " — an istiʿāra tamthīliyya that al-Zawzanī describes: «he makes the spear-shaft that cannot be straightened a likeness of their might that is not broken, and its crushing of whoever tries to pull it down like the shaft's recoil from straightening»", " — Zevzenî'nin tarif ettiği istiâre-i temsîliyye: «düzeltilemeyen mızrağı, sarsılmayan izzetlerine misal kıldı; izzetin onu yıkmaya kalkanı ezmesini de mızrağın düzeltilmekten kaçmasına benzetti»"),
    ZW("اشْمَأَزَّتْ: نَفَرَتْ مِنَ التَّقْوِيمِ", "اشْمَأَزَّتْ: it recoiled from the straightening", "«işmeezzet»: düzeltilmekten ürküp kaçtı")))],
 [V("mtn", "وَوَلَّتْهُ", "walla-amr", c="w", enc="هُ", encrole="maf1", doer=QANAT, g=["form-ii-verbs", "naqis-verbs", "mafulayn"], n=N3(CL("atf", "اشْمَأَزَّتْ", "it recoils", "tiksinip çekilir"), ZW("وَوَلَّتِ الثِّقَافَ قَنَاةً صُلْبَةً شَدِيدَةً دَفُوعًا", "it turned on the iron, a hard, tough, kicking shaft", "demire sert, katı, iten bir mızrak olarak döndü"))),
  R("maf2", "عَشَوْزَنَةً", "ashawzana-amr", g=["hadhf-wa-taqdir"], n=N3(DR("وَهِيَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: قَنَاةً عَشَوْزَنَةً", "it is the adjective of an omitted noun: «a hard spear-shaft»", "mahzûf bir mevsûfun sıfatıdır: «sert bir mızrak»"), ZW("الْعَشَوْزَنَةُ: الصُّلْبَةُ الشَّدِيدَةُ", "عَشَوْزَنَة is hard and tough", "«aşevzene»: sert, katı"))),
  R("naatn", "زَبُونَا", "zabun-amr", of=("عَشَوْزَنَةً", "hard", "sert"), n=N3(TANW_ALIF, ZW("الزَّبُونُ: الدَّفُوعُ، وَأَصْلُهُ مِنْ قَوْلِهِمْ: زَبَنَتِ النَّاقَةُ حَالِبَهَا إِذَا ضَرَبَتْهُ بِثَفِنَاتِ رِجْلَيْهَا", "زَبُون is one that thrusts back; from «the she-camel زَبَنَتْ her milker», kicking him with the knobs of her legs", "«zebûn»: iten; aslı «deve sağanını tepti» sözündendir")))])
VV(59, "a hard one that, when it is turned, cries out and splits the nape and the brow of the man who straightens it.",
  "sert (bir mızrak) ki çevrildiğinde çınlar, düzeltenin ensesini ve alnını yarar.",
 [R("bdln", "عَشَوْزَنَةً", "ashawzana-amr", n=DR("مِنْ «عَشَوْزَنَةً» فِي الْبَيْتِ قَبْلَهُ", "of «hard» in the verse before", "önceki beyitteki «sert»ten")),
  IDHA(n=DR("وَجُمْلَةُ «إِذَا» وَمَا بَعْدَهَا فِي مَحَلِّ نَصْبٍ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "the إِذَا clause with what follows is a second adjective of the omitted noun, in the seat of nasb", "«izâ» cümlesi sonrasıyla birlikte mahzûf mevsûfun ikinci sıfatı, mahallen mansûb")),
  V("mt", "انْقَلَبَتْ", "inqalaba-amr", doer=QANAT, g=["form-vii-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  V("mt", "أَرَنَّتْ", "aranna-amr", doer=QANAT, g=["form-iv-verbs", "doubled-verbs"], n=N3(CL("jawab"), ZW("أَرَنَّتْ: صَوَّتَتْ، وَالْإِرْنَانُ هُنَا لَازِمٌ وَقَدْ يَكُونُ مُتَعَدِّيًا", "أَرَنَّتْ: it cried out; إِرْنَان is intransitive here, though it may be transitive", "«erannet»: ses çıkardı; «irnân» burada lâzımdır, müteaddî de olabilir")))],
 [V("d", "تَشُجُّ", "shajja", doer=QANAT, g=["doubled-verbs", "mubalagha-maqbula"], n=N3(NT("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ أُخْرَى لِلْمَوْصُوفِ الْمَحْذُوفِ", "the clause is another adjective of the omitted noun, in the seat of nasb", "cümle mahzûf mevsûfun bir başka sıfatı, mahallen mansûb"), DR("وَرِوَايَتُهُ: «تَدُقُّ»", "his text reads «تَدُقُّ», «crushes»", "onun rivayeti «teduḳḳu»dur"),
    (" — وَفِيهِ مُبَالَغَةٌ نَصَّ عَلَيْهَا الزَّوْزَنِيُّ: «ثُمَّ بَالَغَ فِي وَصْفِ الْقَنَاةِ بِأَنَّهَا تُصَوِّتُ إِذَا أُرِيدَ تَثْقِيفُهَا، وَلَمْ تُطَاوِعِ الْغَامِزَ بَلْ تَشُجُّ قَفَاهُ وَجَبِينَهُ؛ كَذٰلِكَ عِزَّتُهُمْ لَا تَضَعْضَعُ لِمَنْ رَامَهَا بَلْ تُهْلِكُهُ»", " — a mubālagha al-Zawzanī names: «then he goes further in describing the shaft: it cries out when one would straighten it, and does not yield to the one who presses it but splits his nape and brow; so their might does not give way to whoever seeks it, but destroys him»", " — Zevzenî'nin adını koyduğu mübalağa: «sonra mızrağı, düzeltilmek istenince çınlayan, sıkana boyun eğmeyip ensesini ve alnını yaran diye nitelemekte mübalağa etti; izzetleri de onu isteyene boyun eğmez, onu helâk eder»"))),
  R("maf", "قَفَا", "qafan-amr", mud=True, sign=S_AN, g=["ism-maqsur-manqus"]),
  R("mdf", "الْمُثَقِّفِ", "muthaqqif-amr", g=["ism-fail"]),
  R("atfn", "وَالْجَبِينَا", "jabin", c="w", of=("قَفَا", "the nape", "ense"), n=ITLAQ)])
VV(60, "Have you been told of any failing in Jusham ibn Bakr, in the affairs of those of old?",
  "Cüşem b. Bekr'de, eskilerin işlerinde bir eksiklik olduğu sana haber verildi mi?",
 [PT("فَهَلْ", "hal-istifham", "حَرْفُ اسْتِفْهَامٍ لَا عَمَلَ لَهُ", "a particle of question that governs nothing", "soru harfi, ameli yoktur", c="fi", g=["al-istifham"]),
  HUDDITHTA(NT("وَ«حَدَّثَ» يَنْصِبُ ثَلَاثَةَ مَفَاعِيلَ (الدُّرَّةُ)", "حَدَّثَ takes three objects (al-Durra)", "«haddese» üç mef'ûl alır (Dürre)")),
  PR("فِي", "fi", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حُدِّثْتَ»، وَهُمَا فِي مَحَلِّ نَصْبٍ مَفْعُولُهُ الثَّانِي", "the phrase hangs on «you have been told» and stands as its second object", "câr-mecrûr «sana haber verildi»ye müteallik, ikinci mef'ûlü yerindedir")),
  R("majr", "جُشَمِ", "jusham-amr", pos="propn", sign=JUSHAM_S),
  R("naatj", "بْنِ", "ibn", mud=True, of=("جُشَمِ", "Jusham", "Cüşem")),
  R("mdf", "بَكْرٍ", "bakr", pos="propn")],
 [R("majr", "بِنَقْصٍ", "naqs", j="bi", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حُدِّثْتَ»، وَهُمَا فِي مَحَلِّ نَصْبٍ مَفْعُولُهُ الثَّالِثُ", "the phrase hangs on «you have been told» and stands as its third object", "câr-mecrûr «sana haber verildi»ye müteallik, üçüncü mef'ûlü yerindedir")),
  PR("فِي", "fi", n=MT("نَقْصٍ", "failing", "eksiklik»e")),
  R("majr", "خُطُوبِ", "khatb-amr", mud=True, g=["jam-taksir"]),
  R("mdf", "الْأَوَّلِينَا", "awwal", sign=S_JMSI, g=["jam-mudhakkar-salim"], n=ZW("أَيْ فِي أُمُورِ الْقُرُونِ الْمَاضِيَةِ", "that is, in the affairs of the bygone generations", "yani geçmiş nesillerin işlerinde"))])
VV(61, "We have inherited the glory of ʿAlqama ibn Sayf, who laid the strongholds of glory open to us by force.",
  "Alkame b. Seyf'in şerefini miras aldık; şerefin kalelerini bize zorla açan oydu.",
 [V("mna", "وَرِثْنَا", "waritha", g=["mithal-verbs"], n=CL("ist")),
  R("maf", "مَجْدَ", "majd", mud=True),
  R("mdf", "عَلْقَمَةَ", "alqama", pos="propn", sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ (الدُّرَّةُ)", " — by the fatha that stands for the kasra: a diptote, a proper name feminine in form (al-Durra)", " — alem ve lafzen müennes olduğu için gayr-i munsarif: kesre yerine fetha ile (Dürre)"), g=["mamnu-min-sarf"]),
  R("naatj", "بْنِ", "ibn", mud=True, of=("عَلْقَمَةَ", "ʿAlqama", "Alkame")),
  R("mdf", "سَيْفٍ", "sayf-name-amr", pos="propn")],
 [V("m", "أَبَاحَ", "abaha-amr", doer=HUWA("عَلْقَمَةَ", "ʿAlqama", "Alkame'ye"), g=["form-iv-verbs", "hollow-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «عَلْقَمَةَ» عَلَى تَقْدِيرِ «قَدْ»", "the clause is a hal of «ʿAlqama», in the seat of nasb, with قَدْ understood", "cümle, «kad» takdir edilerek «Alkame»den hâl, mahallen mansûb")),
  JP("لَنَا", "li", "نَا", n=MT("أَبَاحَ", "laid open", "açtı»ya")),
  R("maf", "حُصُونَ", "hisn-amr", mud=True, g=["jam-taksir", "istiara-makniyya"], n=HADD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَ الْمَجْدُ بِمَدِينَةٍ مُحَصَّنَةٍ، وَطُوِيَ الْمُشَبَّهُ بِهِ وَدَلَّ عَلَيْهِ لَازِمُهُ «الْحُصُونُ» (تَخْيِيلٌ)", "an istiʿāra makniyya: glory is likened to a walled city, which is folded away and shown by what goes with it, the «strongholds» (takhyīl)", "istiâre-i mekniyye: şeref, kaleli bir şehre benzetilmiş; müşebbehün bih dürülüp lâzımı olan «kaleler» ile gösterilmiştir (tahyîl)")),
  R("mdf", "الْمَجْدِ", "majd"),
  R("hal", "دِينَا", "din-qahr-amr", n=N3(TANW_ALIF, DR("مِنْ «حُصُونَ الْمَجْدِ»؛ وَيُرْوَى مَكَانَهُ «حِينًا» ظَرْفًا", "of «the strongholds of glory»; «for a time» is also read in its place, an adverb", "«şerefin kaleleri»nden hâl; yerine zarf olarak «hînen» de rivayet edilir"), ZW("الدِّينُ: الْقَهْرُ؛ أَيْ جَعَلَ لَنَا حُصُونَ الْمَجْدِ مُبَاحَةً قَهْرًا وَعَنْوَةً", "دِين is subjugation: he made the strongholds of glory free to us by force and compulsion", "«dîn»: kahır; yani şerefin kalelerini bize zorla ve cebren mubah kıldı")))])
VV(62, "I have inherited Muhalhil, and one better than he, Zuhayr — how excellent a treasure for those who lay up treasure!",
  "Mühelhil'i ve ondan daha hayırlısı Züheyr'i miras aldım — biriktirenlerin birikimi ne güzel bir birikimdir!",
 [V("mtu", "وَرِثْتُ", "waritha", g=["mithal-verbs"], n=CL("ist")),
  R("maf", "مُهَلْهِلًا", "muhalhil-amr", pos="propn", g=["ijaz-al-hadhf"], n=(" — وَفِيهِ إِيجَازٌ بِحَذْفِ الْمُضَافِ، بَيَّنَهُ الزَّوْزَنِيُّ: «وَرِثْتُ مَجْدَ مُهَلْهِلٍ»", " — an ījāz by leaving out the annexed noun, as al-Zawzanī makes plain: «I inherited the glory of Muhalhil»", " — muzâfın hazfiyle îcâz; Zevzenî açıklar: «Mühelhil'in şerefini miras aldım»")),
  R("atfn", "وَالْخَيْرَ", "khayr", c="w", of=("مُهَلْهِلًا", "Muhalhil", "Mühelhil"), n=ZW("أَيْ وَمَجْدَ الرَّجُلِ الَّذِي هُوَ خَيْرٌ مِنْهُ", "that is, and the glory of the man who is better than he", "yani ondan daha hayırlı olan adamın şerefini")),
  JP("مِنْهُ", "min", "هُ", n=MT("الْخَيْرَ", "better", "daha hayırlı»ya"))],
 [R("bdln", "زُهَيْرًا", "zuhayr", pos="propn", of=("الْخَيْرَ", "the better", "daha hayırlı"), n=DR("بَدَلُ كُلٍّ مِنْ كُلٍّ، أَوْ عَطْفُ بَيَانٍ", "a badal of the whole, or an explaining apposition", "bedel-i küll, yahut atf-ı beyân")),
  T("نِعْمَ", "nima-verb", "verb", ["afal-al-madh-wal-dhamm-fil-kafiya", "khabar-insha"], "فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ مَبْنِيٌّ عَلَى الْفَتْحِ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ، وَالْمَخْصُوصُ بِالْمَدْحِ مَحْذُوفٌ: هُوَ.",
    "A frozen past verb that makes praise, built on fatha; the sentence is a fresh one, and the one praised is left out: «he».", "Medih inşâ eden câmid mâzî, fetha üzere mebnî; cümle müste'neftir, övülen (mahsûs) mahzûftur: «o»."),
  R("fail", "ذُخْرُ", "dhukhr-amr", mud=True),
  R("mdf", "الذَّاخِرِينَا", "dhakhir-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail", "mulhaq-bil-jinas"], n=HADD("مُلْحَقٌ بِالْجِنَاسِ: «ذُخْرُ» وَ«الذَّاخِرِينَا» يَجْمَعُهُمَا الِاشْتِقَاقُ", "a figure joined to jinās: «treasure» and «those who lay up treasure» share one derivation", "cinâsa mülhak: «birikim» ile «biriktirenler»i iştikak birleştirir"))])
VV(63, "and ʿAttāb and Kulthūm, all of them: through them we have come into the heritage of the noblest.",
  "ve Attâb'ı ve Külsûm'u, hepsini; en kerimlerin mirasına onlar sayesinde eriştik.",
 [R("atfn", "وَعَتَّابًا", "attab-amr", pos="propn", c="w", of=("مُهَلْهِلًا", "Muhalhil", "Mühelhil"), n=NT("فِي الْبَيْتِ قَبْلَهُ", "in the verse before", "önceki beyitte")),
  R("atfn", "وَكُلْثُومًا", "kulthum", pos="propn", c="w", of=("عَتَّابًا", "ʿAttāb", "Attâb")),
  R("hal", "جَمِيعًا", "jamian", n=DR("حَالٌ مُؤَكِّدَةٌ مِنَ الْأَعْلَامِ قَبْلَهُ", "a hal that strengthens, of the names before it", "önceki özel isimlerden te'kîd eden hâl"))],
 [JP("بِهِمْ", "bi", "هِمْ", g=["turuq-al-qasr"], n=N3(MT("نِلْنَا", "we have come into", "eriştik»e"), HADD("قَصْرٌ بِتَقْدِيمِ مَا حَقُّهُ التَّأْخِيرُ: قَدَّمَ «بِهِمْ» عَلَى «نِلْنَا»، أَيْ بِهِمْ لَا بِغَيْرِهِمْ", "a restriction by fronting what would come later: «through them» stands before «we have come into» — through them and no others", "sonra gelmesi gereken öne alınarak kasr: «onlar sayesinde» «eriştik»ten önce gelmiştir — başkalarıyla değil, onlarla"))),
  V("mna", "نِلْنَا", "nala", g=["hollow-verbs"], n=CL("ist")),
  R("maf", "تُرَاثَ", "turath-amr", mud=True),
  R("mdf", "الْأَكْرَمِينَا", "akram-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-tafdil"], n=ZW("أَيْ حُزْنَا مَآثِرَهُمْ وَمَفَاخِرَهُمْ", "that is, we came to own their noble deeds and their glories", "yani onların menkıbelerine ve övünç vesilelerine sahip olduk"))])
VV(64, "and Dhū l-Bura, of whom you have been told: through him we are guarded, and we guard those driven to seek refuge.",
  "ve sana anlatılan Zü'l-Bure'yi: onun sayesinde korunur, sığınmaya muhtaç olanları da biz koruruz.",
 [R("atfn", "وَذَا", "dhu", c="w", mud=True, sign=S_ALIF5, g=["five-nouns"], of=("مُهَلْهِلًا", "Muhalhil", "Mühelhil")),
  R("mdf", "الْبُرَةِ", "bura-tf", n=ZW("ذُو الْبُرَةِ: مِنْ بَنِي تَغْلِبَ، سُمِّيَ بِهِ لِشَعَرٍ عَلَى أَنْفِهِ يَسْتَدِيرُ كَالْحَلْقَةِ", "Dhū l-Bura was of Taghlib, so called for hair on his nose that curled round like a ring", "Zü'l-Bure Tağlib'dendir; burnunun üstünde halka gibi kıvrılan kıl yüzünden bu adı almıştır")),
  T("الَّذِي", "alladhi", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«ذَا الْبُرَةِ».", "A relative noun built on sukun, in the seat of nasb as an adjective of «Dhū l-Bura».", "Sükûn üzere mebnî ism-i mevsûl, «Zü'l-Bure»nin na'tı olarak mahallen mansûb."),
  HUDDITHTA(NT("وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا", "the clause is the relative's ṣila, with no seat", "cümle mevsûlün sılasıdır, mahalli yoktur")),
  JP("عَنْهُ", "an", "هُ", n=MT("حُدِّثْتَ", "you have been told", "anlatıldı»ya"))],
 [JP("بِهِ", "bi", "هِ", n=MT("نُحْمَى", "we are guarded", "korunuruz»a")),
  V("da", "نُحْمَى", "hama-protect", pas=True, doer=NAHNU, g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «ذَا الْبُرَةِ»، وَالرَّابِطُ الضَّمِيرُ الْمَجْرُورُ", "the clause is a hal of «Dhū l-Bura», in the seat of nasb, tied by the pronoun after the ba", "cümle «Zü'l-Bure»den hâl, mahallen mansûb; râbıt mecrûr zamirdir")),
  V("dy", "وَنَحْمِي", "hama-protect", c="w", doer=NAHNU, g=["naqis-verbs"], n=CL("atf", "نُحْمَى", "we are guarded", "korunuruz")),
  R("maf", "الْمُحْجَرِينَا", "muhjar-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-maful"], n=N3(ZW("وَبِهِ نَحْمِي الْفُقَرَاءَ الْمُلْجَئِينَ إِلَى الِاسْتِجَارَةِ بِغَيْرِهِمْ", "and through him we guard the poor who are driven to seek protection from others", "ve onun sayesinde başkalarına sığınmak zorunda kalan yoksulları koruruz"), DR("وَرِوَايَتُهُ: «الْمُلْجَئِينَا»", "his text reads «الْمُلْجَئِينَا»", "onun rivayeti «el-mülceînâ»dır")))])
# ---- vv. 65–71 — نَحْنُ ----
def MATA_SH(n=NO):
    return T("مَتَى", "mata", "noun", ["huruf-al-shart-fil-kafiya", "maful-fih"], "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ، مُتَعَلِّقٌ بِفِعْلِ الشَّرْطِ بَعْدَهُ" + n[0] + ".",
             "A conditional noun that puts verbs in jazm, built on sukun, in the seat of nasb as an adverb of time; it hangs on the condition verb after it" + n[1] + ".", "Cezmeden şart ismi, sükûn üzere mebnî, zaman zarfı olarak mahallen mansûb; sonraki şart fiiline müteallik" + n[2] + ".")
S_JMSRI2 = ("بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", " — by the waw, a sound masculine plural; its nun stands for the tanwin of the singular", " — cem-i müzekker sâlim olduğu için vâv ile; nûn müfreddeki tenvinin karşılığıdır")
VV(65, "And of us, before him, was the one who strove (for glory), Kulayb — and what glory is there that we have not come close to?",
  "Ondan önce (şeref için) koşan Küleyb de bizdendir — hangi şeref vardır ki ona yaklaşmamış olalım?",
 [JP("وَمِنَّا", "min", "نَا", c="wi", g=["taqdim-al-musnad"], n=N3(MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere"), HADD("تَقْدِيمُ الْمُسْنَدِ لِلتَّخْصِيصِ وَالِافْتِخَارِ: قَدَّمَ «مِنَّا» عَلَى «السَّاعِي»، أَيْ مِنَّا لَا مِنْ غَيْرِنَا", "the musnad is fronted to single out and to boast: «of us» stands before «the one who strove» — of us and not of others", "müsnedin tahsis ve iftihar için öne alınması: «bizden» «koşan»dan önce gelmiştir — başkalarından değil, bizden"))),
  R("zarfz", "قَبْلَهُ", "qabla", enc="هُ", n=NT("مُتَعَلِّقٌ بِالْخَبَرِ الْمَحْذُوفِ، وَالْهَاءُ لِذِي الْبُرَةِ", "it hangs on the omitted khabar; the ha is Dhū l-Bura", "mahzûf habere müteallik; hâ Zü'l-Bure'ye döner")),
  R("mub", "السَّاعِي", "lb-sai", sign=("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", " — by a damma estimated on the ya", " — yâ üzerinde takdîrî damme ile"), g=["ism-maqsur-manqus", "ism-fail"], n=N3(NT("مُؤَخَّرٌ", "put after its khabar", "haberinden sonraya bırakılmış"), ZW("السَّاعِي لِلْمَعَالِي", "the one who strove for high things", "yücelikler için koşan"))),
  R("bdlr", "كُلَيْبٌ", "kulayb-amr", pos="propn", of=("السَّاعِي", "the one who strove", "koşan"), n=ZW("يَعْنِي كُلَيْبَ وَائِلٍ", "he means Kulayb of Wāʾil", "Küleyb-i Vâil'i kastediyor"))],
 [R("mub", "فَأَيُّ", "ayy", c="fi", mud=True, g=["khuruj-al-istifham", "al-istifham"], n=HADD("اسْتِفْهَامٌ خَرَجَ إِلَى النَّفْيِ، وَالدَّلِيلُ «إِلَّا» بَعْدَهُ: لَا مَجْدَ إِلَّا قَدْ وَلِينَاهُ", "a question that has turned into a denial, as the إِلَّا after it shows: «there is no glory but we have come close to it»", "nefye çıkmış soru; delili sonraki «illâ»dır: «yaklaşmadığımız hiçbir şeref yoktur»")),
  R("mdf", "الْمَجْدِ", "majd"),
  PT("إِلَّا", "illa", "حَرْفُ حَصْرٍ لَا عَمَلَ لَهُ", "a particle of restriction that governs nothing", "hasr harfi, ameli yoktur", g=["istithna-mufarragh"]),
  QAD(),
  V("mna", "وَلِينَا", "waliya", g=["mithal-verbs", "naqis-verbs"], n=N3(CL("khb", "أَيُّ", "what", "hangi"), DR("وَالرَّابِطُ مَحْذُوفٌ: إِلَّا قَدْ وَلِينَاهُ؛ وَنَصَبَ أَبُو عَمْرٍو وَالْأَصْمَعِيُّ «أَيَّ» مَفْعُولًا مُقَدَّمًا، وَلَمْ يُجِزْهُ الْكِسَائِيُّ وَالْفَرَّاءُ", "the tie is left out: «but we have come close to it»; Abū ʿAmr and al-Aṣmaʿī read أَيَّ in nasb as a fronted object, which al-Kisāʾī and al-Farrāʾ did not allow", "râbıt mahzûftur: «ona yaklaşmışızdır»; Ebû Amr ve Esmaî «eyye»yi öne alınmış mef'ûl olarak mansûb okumuş, Kisâî ve Ferrâ bunu caiz görmemiştir"), ZW("أَيْ قَرُبْنَا مِنْهُ فَحَوَيْنَاهُ", "that is, we came near it and took it in", "yani ona yaklaşıp onu elde ettik")))])
VV(66, "Whenever we tie our yoked camel with a rope, she snaps the rope or breaks the neck of her yoke-fellow.",
  "Ne zaman (yanına koşulan) devemizi bir iple bağlasak, ya ipi koparır ya da eşinin boynunu kırar.",
 [MATA_SH(),
  V(JZ("لِأَنَّهُ فِعْلُ الشَّرْطِ", "as the verb of the condition", "şart fiili olarak"), "نَعْقِدْ", "aqada", doer=NAHNU, g=["majaz-murakkab", "aqsam-al-istiara"], n=N3(CL("ibt"),
    (" — وَفِيهِ اسْتِعَارَةٌ تَمْثِيلِيَّةٌ بَيَّنَ الزَّوْزَنِيُّ مَعْنَاهَا: «وَالْمَعْنَى: مَتَى قُرِنَّا بِقَوْمٍ فِي قِتَالٍ أَوْ جِدَالٍ غَلَبْنَاهُمْ وَقَهَرْنَاهُمْ»", " — an istiʿāra tamthīliyya whose meaning al-Zawzanī makes plain: «the sense is: whenever we are matched with a people in fighting or disputing, we overcome and crush them»", " — Zevzenî'nin anlamını açıkladığı istiâre-i temsîliyye: «mâna şudur: ne zaman savaşta ya da tartışmada bir kavimle eşleştirilsek onları yener ve ezeriz»"))),
  R("maf", "قَرِينَتَنَا", "qarina", enc="نَا", n=ZW("مَتَى قَرَنَّا نَاقَتَنَا بِأُخْرَى", "whenever we yoke our she-camel to another", "devemizi bir başkasına ne zaman koşsak")),
  R("majr", "بِحَبْلٍ", "habl", j="bi", n=MT("نَعْقِدْ", "tie", "bağlasak»a"))],
 [V(JZ("لِأَنَّهُ جَوَابُ الشَّرْطِ", "as the answer of the condition", "şartın cevabı olarak", sign="fatha"), "تَجُذَّ", "jadhdha-amr", doer=HIYA("الْقَرِينَةِ", "the yoked camel", "koşulan deveye"), g=["doubled-verbs"], n=N3(NT("وَالْجُمْلَةُ جَوَابُ شَرْطٍ جَازِمٍ لَمْ تَقْتَرِنْ بِالْفَاءِ فَلَا مَحَلَّ لَهَا", "the answer of a jazm condition without fa, so it has no seat", "fâ almamış cezmeden şartın cevabıdır, mahalli yoktur"), DR("وَرِوَايَتُهُ: «نَجُذَّ الْوَصْلَ أَوْ نَقِصِ الْقَرِينَا»", "his text reads «we snap the bond or break the yoke-fellow»", "onun rivayeti «bağı koparırız ya da eşi kırarız»dır"))),
  R("maf", "الْحَبْلَ", "habl"),
  PT("أَوْ", "aw", "حَرْفُ عَطْفٍ", "a conjunction («or»)", "atıf harfi («yahut»)", g=["atf-nasaq"]),
  V(JZ("لِعَطْفِهِ عَلَى جَوَابِ الشَّرْطِ", "being joined to the answer of the condition", "şartın cevabına atfedildiği için", sign="kasr"), "تَقِصِ", "waqasa-amr", doer=HIYA("الْقَرِينَةِ", "the yoked camel", "koşulan deveye"), g=["mithal-verbs"], n=ZW("الْوَقْصُ: دَقُّ الْعُنُقِ، وَالْفِعْلُ وَقَصَ يَقِصُ", "وَقْص is breaking the neck; the verb is وَقَصَ يَقِصُ", "«vaks»: boynu kırmak; fiili «vakasa yakısu»")),
  R("maf", "الْقَرِينَا", "qarin-amr", n=ITLAQ)])
VV(67, "We are found the most jealous of them all in guarding what must be guarded, and the most faithful of them when they swear an oath.",
  "Korunması gerekeni korumada onların en çetini, yemin ettiklerinde en vefalısı biz bulunuruz.",
 [V("d", "وَنُوجَدُ", "wajada", c="wi", pas=True, doer=NAHNU, g=["mithal-verbs", "mafulayn"], n=DR("وَنَائِبُ الْفَاعِلِ هُوَ الْمَفْعُولُ الْأَوَّلُ", "the deputy doer is the first object", "nâib-i fâil birinci mef'ûldür")),
  T("نَحْنُ", "nahnu", "pron", ["tawkid", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ نَائِبِ الْفَاعِلِ (الدُّرَّةُ).",
    "A detached pronoun built on damma, in the seat of raf', strengthening the hidden pronoun that is the deputy doer (al-Durra).", "Damme üzere mebnî ayrı zamir, nâib-i fâil olan gizli zamiri te'kîd eder, mahallen merfû (Dürre)."),
  R("maf2", "أَمْنَعَهُمْ", "amna-amr", enc="هُمْ", g=["ism-tafdil"], n=DR("وَجُوِّزَ رَفْعُهُ خَبَرًا لِـ«نَحْنُ»", "it could also be in raf' as the khabar of «we»", "«biz»in haberi olarak merfû olması da caiz görülmüştür")),
  R("tamyiz", "ذِمَارًا", "dhimar-amr", n=ZW("الذِّمَارُ: الْعَهْدُ وَالْحِلْفُ وَالذِّمَّةُ، سُمِّيَ بِهِ لِأَنَّهُ يُتَذَمَّرُ لَهُ، أَيْ يُتَغَضَّبُ لِمُرَاعَاتِهِ", "ذِمَار is the pledge, the alliance, the protection — so named because one grows angry (يُتَذَمَّرُ) in keeping it", "«zimâr»: ahit, antlaşma, zimmet; onu gözetmek için öfkelenildiği (yutezemmeru) için bu adı almıştır"))],
 [R("atfn", "وَأَوْفَاهُمْ", "awfa-el-amr", c="w", enc="هُمْ", sign=S_AN, g=["ism-tafdil"], of=("أَمْنَعَهُمْ", "the most jealous of them", "en çetinleri")),
  IDHA(plain=True, n=DR("مُتَعَلِّقٌ بِـ«أَوْفَى»", "it hangs on «most faithful»", "«en vefalı»ya müteallik")),
  V("mw", "عَقَدُوا", "aqada", n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  R("maf", "يَمِينَا", "yamin", n=N3(TANW_ALIF, DR("وَقِيلَ: تَمْيِيزٌ لِـ«أَوْفَى»، وَمَفْعُولُ «عَقَدُوا» مَحْذُوفٌ", "some make it a tamyiz of «most faithful», the object of «they swear» being left out", "«en vefalı»nın temyîzi olduğu, «akdettiler»in mef'ûlünün mahzûf olduğu da söylenmiştir")))])
VV(68, "And we, on the morning (the fire) was kindled at Khazāzā, gave help above the help of all who helped.",
  "Biz, Hazâzâ'da (savaş ateşi) yakıldığı sabah, yardım edenlerin yardımının üstünde yardım ettik.",
 [NAHNU_M("وَنَحْنُ", c="wi"),
  R("zarfz", "غَدَاةَ", "ghadat", mud=True, n=MZ("رَفَدْنَا", "gave help", "yardım ettik»e")),
  T("أُوقِدَ", "awqada", "verb", ["form-iv-verbs", "naib-al-fail", "ijaz-al-hadhf"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ مَحْذُوفٌ لِدَلَالَةِ الْمَقَامِ عَلَيْهِ، وَلَمْ يُؤَنَّثِ الْفِعْلُ لِأَنَّ تَأْنِيثَهُ مَجَازِيٌّ (الدُّرَّةُ)؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «غَدَاةَ» إِلَيْهَا — وَفِيهِ إِيجَازٌ بِالْحَذْفِ: الْمَحْذُوفُ «نَارُ الْحَرْبِ»، صَرَّحَ بِهِ الزَّوْزَنِيُّ: «غَدَاةَ أُوقِدَتْ نَارُ الْحَرْبِ».",
    "A passive past verb built on fatha; its deputy doer is left out, the setting showing it, and the verb is not made feminine because that feminine is only grammatical (al-Durra); the clause is in the seat of jarr, «the morning» being annexed to it — an ījāz by omission: what is left out is «the fire of war», which al-Zawzanī states: «the morning the fire of war was kindled».",
    "Fetha üzere mebnî meçhul mâzî; nâib-i fâil, makam delâlet ettiği için mahzûftur; müennesliği mecâzî olduğu için fiil müennes getirilmemiştir (Dürre); cümle «sabah»ın ona izâfetiyle mahallen mecrûr — hazf yoluyla îcâz: mahzûf «savaş ateşi»dir, Zevzenî açıkça söyler: «savaş ateşinin yakıldığı sabah»."),
  PR("فِي", "fi", n=MT("أُوقِدَ", "was kindled", "yakıldı»ya")),
  R("majr", "خَزَازَى", "khazaza-amr", pos="propn", sign=("بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَقْصُورَةِ", " — by a fatha estimated on the alif standing for the kasra: a diptote with the feminine alif maqṣūra", " — maksûre te'nîs elifi sebebiyle gayr-i munsarif: kesre yerine elif üzerinde takdîrî fetha ile"), g=["mamnu-min-sarf", "ism-maqsur-manqus"], n=DR("وَرِوَايَتُهُ: «فِي خَزَازٍ»", "his text reads «at Khazāz»", "onun rivayeti «fî Hazâzin»dır"))],
 [V("mna", "رَفَدْنَا", "rafada-amr", n=N3(CL("khb", "نَحْنُ", "we", "biz"), ZW("الرَّفْدُ: الْإِعَانَةُ؛ أَعَنَّا نِزَارًا … يَفْتَخِرُ بِإِعَانَةِ قَوْمِهِ بَنِي نِزَارٍ فِي مُحَارَبَتِهِمُ الْيَمَنَ", "رَفْد is helping: we helped Nizār … he boasts of his people's help to the Banū Nizār in their war with Yemen", "«refd»: yardım etmek; Nizâr'a yardım ettik … kavminin, Benî Nizâr'a Yemen'e karşı savaşlarında yardımıyla övünür"))),
  R("zarfm", "فَوْقَ", "fawqa", mud=True, n=MZ("رَفَدْنَا", "gave help", "yardım ettik»e")),
  R("mdf", "رِفْدِ", "rifd-amr", mud=True, n=ZW("وَالرِّفْدُ: الِاسْمُ", "رِفْد is the noun", "«rifd» isimdir")),
  R("mdf", "الرَّافِدِينَا", "rafid-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail", "mulhaq-bil-jinas"], n=HADD("مُلْحَقٌ بِالْجِنَاسِ: «رَفَدْنَا» وَ«رِفْدِ» وَ«الرَّافِدِينَا» يَجْمَعُهَا الِاشْتِقَاقُ", "a figure joined to jinās: «we helped», «help» and «the helpers» share one derivation", "cinâsa mülhak: «yardım ettik», «yardım» ve «yardım edenler»i iştikak birleştirir"))])
VV(69, "And we are the ones who held (our herds) back at Dhū Arāṭā, where the great milch-camels champed the old blackened grass.",
  "Biz, Zû Erâtâ'da (sürülerimizi) tutanlarız; orada iri, sütlü develer kararmış eski otu çiğnedi.",
 [NAHNU_M("وَنَحْنُ", c="w"),
  R("khb", "الْحَابِسُونَ", "habis-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "hadhf-al-maful", "kinaya"], n=N3(DR("وَفَاعِلُهُ مُسْتَتِرٌ فِيهِ، وَمَفْعُولُهُ مَحْذُوفٌ", "its doer is hidden in it and its object left out", "fâili içinde gizli, mef'ûlü mahzûftur"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ ثَبَاتِهِمْ فِي نُصْرَةِ قَوْمِهِمْ، بَيَّنَهَا الزَّوْزَنِيُّ: «حَبَسْنَا أَمْوَالَنَا بِهٰذَا الْمَوْضِعِ حَتَّى سَفَّتِ النُّوقُ الْغِزَارُ قَدِيمَ النَّبْتِ وَأَسْوَدَهُ، لِإِعَانَةِ قَوْمِنَا»", " — a kināya for their standing fast in their people's support, which al-Zawzanī makes plain: «we held our herds at this place until the rich milch-camels champed the old, blackened grass, to help our people»", " — kavimlerine yardımda sebatlarından kinâyedir; Zevzenî açıklar: «sürülerimizi bu yerde tuttuk; öyle ki sütü bol develer eski, kararmış otu çiğnedi; kavmimize yardım için»"))),
  R("majr", "بِذِي", "dhu", j="bi", mud=True, sign=S_YA5, g=["five-nouns"], n=MT("الْحَابِسُونَ", "who held back", "tutanlar»a")),
  R("mdf", "أَرَاطَى", "arata-amr", pos="propn", sign=("بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَقْصُورَةِ (الدُّرَّةُ)", " — by a fatha estimated on the alif standing for the kasra: a diptote with the feminine alif maqṣūra (al-Durra)", " — maksûre te'nîs elifi sebebiyle gayr-i munsarif: kesre yerine elif üzerinde takdîrî fetha ile (Dürre)"), g=["mamnu-min-sarf", "ism-maqsur-manqus"])],
 [V("d", "تَسَفُّ", "saffa-ant", g=["doubled-verbs"], n=N3(DR("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا", "the sentence is a fresh one with no seat", "cümle müste'neftir, mahalli yoktur"), ZW("تَسَفُّ: أَيْ تَأْكُلُ يَابِسًا، وَالْمَصْدَرُ السُّفُوفُ", "تَسَفُّ: she eats dry fodder; the masdar is سُفُوف", "«tesuffu»: kuru yem yer; masdarı «sufûf»"))),
  R("fail", "الْجِلَّةُ", "jilla-amr", n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("الْجِلَّةُ: الْكِبَارُ مِنَ الْإِبِلِ", "جِلَّة are the full-grown among camels", "«cille»: develerin iri olanları"))),
  R("naatr", "الْخُورُ", "akhwar-amr", g=["jam-taksir"], n=ZW("الْخُورُ: الْكَثِيرَةُ الْأَلْبَانِ، وَقِيلَ: الْغِزَارُ مِنَ الْإِبِلِ، وَالنَّاقَةُ خَوْرَاءُ", "خُور are those rich in milk, or the copious milkers among camels; one is خَوْرَاء", "«hûr»: sütü bol olanlar; bol sütlü develer de denmiştir; tekili «havrâ»")),
  R("maf", "الدَّرِينَا", "darin-amr", n=N3(ITLAQ, ZW("الدَّرِينُ: مَا اسْوَدَّ مِنَ النَّبْتِ وَقَدُمَ", "دَرِين is grass that has grown old and black", "«derîn»: eskiyip kararmış ot")))])
VV(70, "We are the ones who rule when we are obeyed, and we are the ones resolved (on war) when we are disobeyed.",
  "Biz, itaat edildiğimizde hükmedenleriz; isyan edildiğimizde azmedenler de biziz.",
 [NAHNU_M("وَنَحْنُ", c="w"),
  R("khb", "الْحَاكِمُونَ", "hakim-ruler", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail"], n=DR("وَفَاعِلُهُ مُسْتَتِرٌ فِيهِ، وَمَفْعُولُهُ مَحْذُوفٌ", "its doer is hidden in it and its object left out", "fâili içinde gizli, mef'ûlü mahzûftur")),
  IDHA(plain=True, n=N3(MZ("الْحَاكِمُونَ", "who rule", "hükmedenler»e"), DR("وَإِنْ جُعِلَتْ شَرْطِيَّةً فَجَوَابُهَا مَحْذُوفٌ دَلَّ عَلَيْهِ الْكَلَامُ", "if it is taken as conditional, its answer is left out, shown by the sentence", "şartiyye sayılırsa cevabı mahzûftur, söz ona delâlet eder"))),
  V("mna", "أُطِعْنَا", "ataa", pas=True, g=["form-iv-verbs", "hollow-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ"))],
 [NAHNU_M("وَنَحْنُ", c="w"),
  R("khb", "الْعَازِمُونَ", "azim-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail"]),
  IDHA(plain=True, n=MZ("الْعَازِمُونَ", "resolved", "azmedenler»e")),
  V("mna", "عُصِينَا", "asa", pas=True, g=["naqis-verbs", "tibaq"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), HADD("طِبَاقٌ بَيْنَ «أُطِعْنَا» وَ«عُصِينَا»: الطَّاعَةُ وَالْمَعْصِيَةُ ضِدَّانِ", "a ṭibāq between «we are obeyed» and «we are disobeyed», which are contraries", "«itaat edildik» ile «isyan edildik» arasında tıbâk: itaat ve isyan zıttır")))])
VV(71, "We are the ones who leave what displeases us, and we are the ones who take what pleases us.",
  "Hoşnut olmadığımızı bırakanlar biziz; hoşnut olduğumuzu alanlar da biziz.",
 [NAHNU_M("وَنَحْنُ", c="w"),
  R("khb", "التَّارِكُونَ", "tarik", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail"]),
  T("لِمَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ يُقَوِّي عَمَلَ اسْمِ الْفَاعِلِ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«التَّارِكُونَ».",
    "The lam is a jarr letter that strengthens the active participle's working; مَا is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «who leave».", "Lâm, ism-i fâilin amelini kuvvetlendiren cer harfidir; «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr «bırakanlar»a müteallik.", segs=SG(("لِ", "li", "prep"), ("مَا", "ma-mawsula", "pron"))),
  V("mna", "سَخِطْنَا", "sakhita-amr", n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: سَخِطْنَاهُ", "the returning pronoun is left out: «what we disliked»", "dönen zamir mahzûftur: «hoşnut olmadığımız şey»")))],
 [NAHNU_M("وَنَحْنُ", c="w"),
  R("khb", "الْآخِذُونَ", "akhidh-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "muqabala"], n=HADD("مُقَابَلَةٌ: «التَّارِكُونَ لِمَا سَخِطْنَا» يُقَابِلُهُ «الْآخِذُونَ لِمَا رَضِينَا» عَلَى التَّرْتِيبِ — التَّرْكُ وَالْأَخْذُ، وَالسُّخْطُ وَالرِّضَا", "a muqābala: «who leave what displeases us» is answered in order by «who take what pleases us» — leaving and taking, displeasure and pleasure", "mukâbele: «hoşnut olmadığımızı bırakanlar»a sırasıyla «hoşnut olduğumuzu alanlar» karşılık verir — bırakmak ve almak, hoşnutsuzluk ve hoşnutluk")),
  T("لِمَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ يُقَوِّي عَمَلَ اسْمِ الْفَاعِلِ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْآخِذُونَ».",
    "The lam is a jarr letter that strengthens the active participle's working; مَا is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «who take».", "Lâm, ism-i fâilin amelini kuvvetlendiren cer harfidir; «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr «alanlar»a müteallik.", segs=SG(("لِ", "li", "prep"), ("مَا", "ma-mawsula", "pron"))),
  V("mna", "رَضِينَا", "radiya", g=["naqis-verbs"], n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: رَضِينَاهُ", "the returning pronoun is left out: «what we were pleased with»", "dönen zamir mahzûftur: «hoşnut olduğumuz şey»")))])
# ---- vv. 72–78 — الْمَيْمَنَةُ وَالْمَيْسَرَةُ ----
S_DIPT_MJ = ("بِالْفَتْحَةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ", " — by the fatha, without tanwin: a diptote on the furthest plural pattern", " — fetha ile; müntehe'l-cumû' sîgası olduğu için gayr-i munsarif, tenvinsiz")
def FIMAN(gov_ar, gov_en, gov_tr):
    return T("فِيمَنْ", "man", "pron", ["ism-mawsul", "huruf-jarr"], "«فِي» حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«" + gov_ar + "».",
             "فِي is a jarr letter, and مَنْ a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «" + gov_en + "».", "«Fî» cer harfi; «men» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr «" + gov_tr + " müteallik.",
             segs=SG(("فِي", "fi", "prep"), ("مَنْ", "man", "pron")))
def ALAMMA(n=NO):
    return T("أَلَمَّا", "lamma", "part", ["al-istifham", "khuruj-al-istifham", "jawazim-al-mudari-wal-amr-fil-kafiya"], "الْهَمْزَةُ حَرْفُ اسْتِفْهَامٍ وَتَقْرِيرٍ، وَ«لَمَّا» حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ (الدُّرَّةُ)؛ وَقَالَ الزَّوْزَنِيُّ: «مَا» فِي «أَلَمَّا» صِلَةٌ زَائِدَةٌ، أَيْ: أَلَمْ" + n[0] + ".",
             "The hamza is a particle of question, here of making one own (taqrīr), and لَمَّا a particle of negation, jazm and turning to the past (al-Durra); al-Zawzanī says the مَا of أَلَمَّا is an extra particle, so «did … not»" + n[1] + ".", "Hemze soru ve takrîr harfi, «lemmâ» nefy, cezm ve kalb harfi (Dürre); Zevzenî'ye göre «elemmâ»daki «mâ» zâiddir, yani «elem»" + n[2] + ".",
             segs=SG(("أَ", "hamza-istifham", "part"), ("لَمَّا", "lamma", "part")))
TAQRIR = lambda z_ar, z_en, z_tr: (" — وَفِيهِ اسْتِفْهَامٌ خَرَجَ إِلَى التَّقْرِيرِ، سَمَّاهُ الدُّرَّةُ، وَبَيَّنَهُ الزَّوْزَنِيُّ: «" + z_ar + "»", " — a question that turns to making them own it (taqrīr), as al-Durra names it and al-Zawzanī makes plain: «" + z_en + "»", " — takrîre çıkmış soru; Dürre adını koyar, Zevzenî açıklar: «" + z_tr + "»")
VV(72, "We were the right wing when we met (the foe), and our brothers' sons were the left.",
  "(Düşmanla) karşılaştığımızda biz sağ kanat idik; kardeşlerimiz de sol kanat idi.",
 [T("وَكُنَّا", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ.",
    "The waw opens a fresh sentence; كَانَ is a defective past verb built on sukun because نَا is attached, and نَا is its noun, in the seat of raf'.", "Vâv isti'nâf içindir; «kâne» «nâ» bitiştiği için sükûn üzere mebnî nâkıs mâzî; «nâ» mahallen merfû ismidir.", segs=SG(("وَ", "wa", "conj"), ("كُنَّا", "kana", "verb"))),
  R("khbk", "الْأَيْمَنِينَ", "ayman", sign=(S_JMS[0] + "، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", S_JMS[1] + "; its nun stands for the tanwin of the singular", S_JMS[2] + "; nûn müfreddeki tenvinin karşılığıdır"), g=["jam-mudhakkar-salim"], n=ZW("كُنَّا حُمَاةَ الْمَيْمَنَةِ إِذَا لَقِينَا الْأَعْدَاءَ", "we were the defenders of the right wing when we met the enemy", "düşmanla karşılaştığımızda sağ kanadın koruyucuları bizdik")),
  IDHA(plain=True, n=DR("مُتَعَلِّقٌ بِـ«كَانَ»؛ وَإِنْ جُعِلَتْ شَرْطِيَّةً فَجَوَابُهَا مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ", "it hangs on «were»; if conditional, its answer is left out, shown by what precedes", "«idik»e müteallik; şartiyye sayılırsa cevabı mahzûftur, öncesi ona delâlet eder")),
  V("mna", "الْتَقَيْنَا", "iltaqa", g=["form-viii-verbs", "naqis-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ"))],
 [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ.", "The waw conjoins; كَانَ is a defective past verb built on fatha.", "Vâv atıf harfi; «kâne» fetha üzere mebnî nâkıs mâzî.", segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  R("khbk", "الْأَيْسَرِينَ", "aysar", sign=(S_JMS[0] + "، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", S_JMS[1] + "; its nun stands for the tanwin of the singular", S_JMS[2] + "; nûn müfreddeki tenvinin karşılığıdır"), g=["jam-mudhakkar-salim", "tibaq"], n=N3(NT("مُقَدَّمٌ عَلَى اسْمِهِ", "put before its noun", "isminden önce gelmiştir"), HADD("طِبَاقٌ بَيْنَ «الْأَيْمَنِينَ» وَ«الْأَيْسَرِينَ»: الْيَمِينُ وَالْيَسَارُ ضِدَّانِ", "a ṭibāq between «the right» and «the left», which are contraries", "«sağdakiler» ile «soldakiler» arasında tıbâk: sağ ve sol zıttır"))),
  R("ismk", "بَنُو", "banu", mud=True, sign=("بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the waw, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için vâv ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"], n=N3(NT("مُؤَخَّرٌ", "put after its predicate", "haberinden sonraya bırakılmış"), ZW("أَيْ إِخْوَانُنَا — يَعْنِي بَنِي بَكْرٍ", "that is, our brothers — he means the Banū Bakr", "yani kardeşlerimiz — Benî Bekr'i kasteder"))),
  R("mdf", "أَبِينَا", "ab", enc="نَا", sign=S_YA5, g=["five-nouns"])])
VV(73, "They charged a charge against those who faced them, and we charged a charge against those who faced us.",
  "Onlar karşılarındakilere bir hücum ettiler; biz de karşımızdakilere bir hücum ettik.",
 [V("mw", "فَصَالُوا", "sala-amr", c="f", g=["hollow-verbs"], n=NT("وَالْأَلِفُ فَارِقَةٌ", "the alif only marks the plural", "elif fârikadır")),
  R("mutlaq", "صَوْلَةً", "sawla", g=["mulhaq-bil-jinas"], n=HADD("مُلْحَقٌ بِالْجِنَاسِ: «صَالُوا» وَ«صَوْلَةً» وَ«صُلْنَا» يَجْمَعُهَا الِاشْتِقَاقُ", "a figure joined to jinās: «they charged», «a charge» and «we charged» share one derivation", "cinâsa mülhak: «hücum ettiler», «hücum» ve «hücum ettik»i iştikak birleştirir")),
  FIMAN("صَالُوا", "charged", "hücum ettiler»e"),
  V("dy", "يَلِيهِمْ", "waliya", enc="هِمْ", doer=HUWA("«مَنْ»", "«those who»", "«men»e"), g=["mithal-verbs", "naqis-verbs"], n=CL("sila"))],
 [V("mna", "وَصُلْنَا", "sala-amr", c="w", g=["hollow-verbs"], n=NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "its middle letter dropped where two quiescents meet", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür")),
  R("mutlaq", "صَوْلَةً", "sawla"),
  FIMAN("صُلْنَا", "we charged", "hücum ettik»e"),
  V("dy", "يَلِينَا", "waliya", enc="نَا", doer=HUWA("«مَنْ»", "«those who»", "«men»e"), g=["mithal-verbs", "naqis-verbs"], n=N3(CL("sila"), ZW("فَحَمَلَ بَنُو بَكْرٍ عَلَى مَنْ يَلِيهِمْ مِنَ الْأَعْدَاءِ، وَحَمَلْنَا عَلَى مَنْ يَلِينَا", "the Banū Bakr charged the enemies facing them, and we charged those facing us", "Benî Bekr karşılarındaki düşmana, biz de karşımızdakine hücum ettik")))])
VV(74, "They came back with spoil and captives, and we came back with kings in fetters.",
  "Onlar ganimet ve esirlerle döndüler; biz ise zincire vurulmuş krallarla döndük.",
 [V("mw", "فَآبُوا", "aba-return", c="f", g=["hollow-verbs"], n=ZW("الْأَوْبُ: الرُّجُوعُ", "أَوْب is returning", "«evb»: dönmek")),
  R("majr", "بِالنِّهَابِ", "nahb", j="bi", g=["jam-taksir"], n=N3(MT("آبُوا", "came back", "döndüler»e"), ZW("النِّهَابُ: الْغَنَائِمُ، الْوَاحِدُ نَهْبٌ", "نِهَاب is spoil; the singular is نَهْب", "«nihâb»: ganimetler; tekili «nehb»"))),
  R("majr", "وَبِالسَّبَايَا", "sabiyya-amr", c="w", j="bi", sign=S_AJ, g=["jam-taksir"], n=NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «بِالنِّهَابِ»", "the phrase is joined to «with spoil»", "câr-mecrûr «ganimetle»ye ma'tûf"))],
 [V("mna", "وَأُبْنَا", "aba-return", c="w", g=["hollow-verbs"], n=NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "its middle letter dropped where two quiescents meet", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür")),
  R("majr", "بِالْمُلُوكِ", "malik-king", j="bi", g=["jam-taksir"], n=MT("أُبْنَا", "came back", "döndük»e")),
  R("hal", "مُصَفَّدِينَا", "musaffad-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-maful"], n=N3(NT("مِنَ «الْمُلُوكِ»", "of «kings»", "«krallar»ın hâli"), ZW("التَّصْفِيدُ: التَّقْيِيدُ؛ أَيِ اغْتَنَمُوا الْأَمْوَالَ وَأَسَرْنَا الْمُلُوكَ", "تَصْفِيد is fettering: they took goods as spoil, and we took kings captive", "«tasfîd»: zincire vurmak; yani onlar malları ganimet aldılar, biz kralları esir ettik")))])
VV(75, "Away with you, Banū Bakr, away! Have you not yet learned the certain truth about us?",
  "Uzak durun, ey Benî Bekr, uzak durun! Bizim hakkımızda kesin olanı hâlâ öğrenmediniz mi?",
 [T("إِلَيْكُمْ", "ilayka-ism-fil", "part", ["asma-al-afal-wal-aswat-wal-murakkabat", "ism-fil"], "اسْمُ فِعْلِ أَمْرٍ مَنْقُولٌ مِنَ الْجَارِّ وَالْمَجْرُورِ مَبْنِيٌّ عَلَى السُّكُونِ، بِمَعْنَى: تَنَحَّوْا، وَفَاعِلُهُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتُمْ؛ وَالْجُمْلَةُ ابْتِدَائِيَّةٌ (الدُّرَّةُ) — يُقَالُ: إِلَيْكَ إِلَيْكَ، أَيْ تَنَحَّ (الزَّوْزَنِيُّ).",
    "A noun of command taken over from a jarr phrase, built on sukun, meaning «keep away!»; its doer is the hidden «you (pl.)»; the sentence opens the speech (al-Durra) — one says إِلَيْكَ إِلَيْكَ, «stand aside» (al-Zawzanī).", "Câr-mecrûrdan nakledilmiş emir ism-i fiili, sükûn üzere mebnî, «uzak durun» anlamında; fâili gizli «siz»dir; cümle ibtidâiyyedir (Dürre) — «ileyke ileyke», yani çekil, denir (Zevzenî)."),
  PT("يَا", "ya-nida", "حَرْفُ نِدَاءٍ", "the particle of calling", "nidâ harfi", g=["vocative-munada"]),
  R("munm", "بَنِي", "banu", sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"]),
  R("mdf", "بَكْرٍ", "bakr", pos="propn"),
  T("إِلَيْكُمْ", "ilayka-ism-fil", "part", ["tawkid", "al-tawkid-al-lafzi-wal-manawi"], "تَوْكِيدٌ لَفْظِيٌّ لِـ«إِلَيْكُمْ» الْأَوَّلِ.", "A verbal (lafẓī) emphasis repeating the first «away with you».", "İlk «uzak durun»un lafzî te'kîdi.")],
 [ALAMMA(TAQRIR("أَيْ قَدْ عَلِمْتُمْ ذٰلِكَ لَنَا فَلَا تَتَعَرَّضُوا لَنَا", "that is, you have learned it of us, so do not stand in our way", "yani bunu bizim hakkımızda bildiniz, öyleyse bize sataşmayın")),
  V(JZ("بِـ«لَمَّا»", "by لَمَّا", "«lemmâ» ile", sign="nun"), "تَعْرِفُوا", "arafa", g=["afal-khamsa", "fail"], n=N3(W5, NT("وَالْأَلِفُ فَارِقَةٌ", "the alif only marks the plural", "elif fârikadır"))),
  JP("مِنَّا", "min", "نَا", n=MT("تَعْرِفُوا", "learned", "öğrenmediniz»e")),
  R("maf", "الْيَقِينَا", "yaqin", n=N3(ITLAQ, ZW("أَيْ مِنْ نَجْدَتِنَا وَبَأْسِنَا", "that is, of our valour and our might", "yani yiğitliğimizden ve gücümüzden")))])
VV(76, "Have you not learned of squadrons, of ours and yours, thrusting at one another and shooting at one another?",
  "Bizden ve sizden, birbirine mızrak saplayan ve birbirine ok atan bölükleri bilmediniz mi?",
 [ALAMMA(TAQRIR("أَلَمْ تَعْلَمُوا كَتَائِبَ مِنَّا وَمِنْكُمْ يَطْعَنُ بَعْضُهُمْ بَعْضًا وَيَرْمِي بَعْضُهُمْ بَعْضًا؟", "did you not learn of squadrons of ours and yours, some thrusting at others and some shooting at others?", "bizden ve sizden, birbirine mızrak saplayan, birbirine ok atan bölükleri bilmediniz mi?")),
  V(JZ("بِـ«لَمَّا»", "by لَمَّا", "«lemmâ» ile", sign="nun"), "تَعْلَمُوا", "alima", g=["afal-khamsa", "fail"], n=N3(W5, NT("وَالْأَلِفُ فَارِقَةٌ", "the alif only marks the plural", "elif fârikadır"), DR("وَرِوَايَتُهُ: «تَعْرِفُوا»", "his text reads «تَعْرِفُوا»", "onun rivayeti «ta'rifû»dur"))),
  JP("مِنَّا", "min", "نَا", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «كَتَائِبَ»: كَانَ صِفَةً لَهُ فَلَمَّا تَقَدَّمَ صَارَ حَالًا", "the phrase hangs on an omitted hal of «squadrons»: it was their adjective, and fronted it becomes a hal", "câr-mecrûr «bölükler»in mahzûf hâline müteallik: sıfatı idi, öne geçince hâl oldu")),
  JP("وَمِنْكُمْ", "min", "كُمْ", c="w", n=NT("وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «مِنَّا»", "the phrase is joined to «of ours»", "câr-mecrûr «bizden»e ma'tûf"))],
 [R("maf", "كَتَائِبَ", "katiba", sign=S_DIPT_MJ, g=["jam-taksir", "mamnu-min-sarf"]),
  V("dn", "يَطَّعِنَّ", "ittaana-amr", g=["form-viii-verbs"], n=N3(CL("nn", "كَتَائِبَ", "squadrons", "bölükler»in"), NT("وَأُدْغِمَتْ نُونُهُ فِي نُونِ النِّسْوَةِ", "its own nun is merged into the nun of the women", "kendi nûnu nisve nûnuna idgâm edilmiştir"), ZW("الِاطِّعَانُ وَالِارْتِمَاءُ مِثْلُ التَّطَاعُنِ وَالتَّرَامِي", "اِطِّعَان and اِرْتِمَاء are like تَطَاعُن and تَرَامِي: doing it to one another", "«ittı'ân» ve «irtimâ», «tetâun» ve «terâmî» gibidir: karşılıklı yapmak"))),
  V("dn", "وَيَرْتَمِينَا", "irtama", c="w", g=["form-viii-verbs", "naqis-verbs"], n=N3(ITLAQ, CL("atf", "يَطَّعِنَّ", "thrusting", "mızrak saplayan")))])
VV(77, "Upon us are helmets and Yemenī leather corselets, and swords that stand straight and bend.",
  "Üzerimizde miğferler ve Yemen işi deri zırhlar, doğrulup eğilen kılıçlar vardır.",
 [JP("عَلَيْنَا", "ala", "نَا", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "الْبَيْضُ", "bayda-egg", g=["jam-taksir"], n=N3(NT("مُؤَخَّرٌ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "put after its khabar; the sentence is a fresh one", "haberinden sonraya bırakılmış; cümle müste'neftir"), (" — وَالْبَيْضُ: جَمْعُ بَيْضَةٍ، وَهِيَ الْخُوذَةُ (حَاشِيَةُ الْمُحَقِّقِ)", " — بَيْض is the plural of بَيْضَة, a helmet (the editor's note)", " — «beyd», miğfer olan «beyda»nın cem'idir (muhakkikin hâşiyesi)"))),
  R("atfr", "وَالْيَلَبُ", "yalab-amr", c="w", of=("الْبَيْضُ", "helmets", "miğferler"), n=ZW("الْيَلَبُ: نَسِيجَةٌ مِنْ سُيُورٍ تُلْبَسُ تَحْتَ الْبَيْضِ", "يَلَب is a woven thing of leather thongs worn under the helmet", "«yeleb»: miğferin altına giyilen deri şeritlerden örgü")),
  R("naatr", "الْيَمَانِي", "yamani-amr", sign=("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ؛ وَأَصْلُهُ «يَمَنِيٌّ»، عُوِّضَتِ الْأَلِفُ مِنْ إِحْدَى يَاءَيِ النِّسْبَةِ", " — by a damma estimated on the ya; it is يَمَنِيّ with an alif making up for one of the two nisba yas", " — yâ üzerinde takdîrî damme ile; aslı «yemenî»dir, nisbet yâlarından birinin yerine elif getirilmiştir"), n=DR("وَعَدَّ تَقْدِيرَ الضَّمَّةِ ضَرُورَةً", "he counts the estimated damma a poet's licence", "dammenin takdirini şiir zarureti sayar"))],
 [R("atfr", "وَأَسْيَافٌ", "sayf", c="w", g=["jam-taksir"], of=("الْبَيْضُ", "helmets", "miğferler")),
  V("dn", "يَقُمْنَ", "qama", g=["hollow-verbs", "tibaq"], n=N3(CL("nr", "أَسْيَافٌ", "swords", "kılıçlar»ın"), NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "its middle letter dropped where two quiescents meet", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür"), DR("وَيُرْوَى «يُقَمْنَ» مَبْنِيًّا لِلْمَجْهُولِ", "it is also read as a passive, «are straightened»", "meçhul olarak «yukamne» diye de rivayet edilir"),
    HADD("طِبَاقٌ بَيْنَ «يَقُمْنَ» وَ«يَنْحَنِينَا»: الِاسْتِقَامَةُ وَالِانْحِنَاءُ ضِدَّانِ", "a ṭibāq between «stand straight» and «bend», which are contraries", "«doğrulur» ile «eğilir» arasında tıbâk: dikilmek ve eğilmek zıttır"))),
  V("dn", "وَيَنْحَنِينَا", "inhana-amr", c="w", g=["form-vii-verbs", "naqis-verbs"], n=N3(ITLAQ, CL("atf", "يَقُمْنَ", "stand straight", "doğrulur"), ZW("يَقُمْنَ وَيَنْحَنِينَ لِطُولِ الضِّرَابِ بِهَا", "they stand and bend from the long smiting with them", "onlarla uzun süre vuruşulduğu için doğrulur ve eğilirler")))])
VV(78, "Upon us is every full, gleaming coat of mail; you see folds in it above the belt.",
  "Üzerimizde her geniş, parlak zırh vardır; kuşağın üstünde onun kıvrımlarını görürsün.",
 [JP("عَلَيْنَا", "ala", "نَا", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("mub", "كُلُّ", "kull", mud=True, n=NT("مُؤَخَّرٌ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "put after its khabar; the sentence is a fresh one", "haberinden sonraya bırakılmış; cümle müste'neftir")),
  R("mdf", "سَابِغَةٍ", "sabigha", n=N3(DR("وَهِيَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("السَّابِغَةُ: الدِّرْعُ الْوَاسِعَةُ التَّامَّةُ", "سَابِغَة is a full, ample coat of mail", "«sâbiğa»: geniş, tam zırh"))),
  R("naatj", "دِلَاصٍ", "dilas-amr", of=("سَابِغَةٍ", "full", "geniş"), n=ZW("الدِّلَاصُ: الْبَرَّاقَةُ", "دِلَاص is gleaming", "«dilâs»: parlak"))],
 [V("da", "تَرَى", "raa", doer=ANTA, g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا", "the sentence is a fresh one with no seat", "cümle müste'neftir, mahalli yoktur")),
  R("zarfm", "فَوْقَ", "fawqa", mud=True, n=MZ("تَرَى", "see", "görürsün»e")),
  R("mdf", "النِّطَاقِ", "nitaq-amr", n=DR("وَرِوَايَتُهُ: «النِّجَادِ»", "his text reads «the sword-belt»", "onun rivayeti «en-nicâd»dır")),
  JP("لَهَا", "li", "هَا", n=MT("تَرَى", "see", "görürsün»e")),
  R("maf", "غُضُونَا", "ghadan-amr", g=["jam-taksir", "kinaya"], n=N3(TANW_ALIF, ZW("الْغُضُونُ: جَمْعُ غَضَنٍ، وَهُوَ التَّشَنُّجُ فِي الشَّيْءِ", "غُضُون is the plural of غَضَن, a fold or crease in a thing", "«ğudûn», bir şeydeki kırışıklık olan «ğaden»in cem'idir"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ سَعَةِ الدُّرُوعِ، بَيَّنَهَا الزَّوْزَنِيُّ: «تَرَى … فَوْقَ الْمِنْطَقَةِ لَهَا غُضُونًا لِسَعَتِهَا وَسُبُوغِهَا»", " — a kināya for the fullness of the mail, which al-Zawzanī makes plain: «you see folds in it above the belt, for its width and fullness»", " — zırhların genişliğinden kinâyedir; Zevzenî açıklar: «genişliği ve bolluğu yüzünden kuşağın üstünde kıvrımlarını görürsün»")))])
# ---- vv. 79–85 — الدُّرُوعُ وَالْجِيَادُ ----
KHAYL_F = HIYA("الْخَيْلِ", "the horses", "atlara")
VV(79, "When they are taken off the champions one day, you see the men's skins dark from them.",
  "Bir gün kahramanların üzerinden çıkarıldıklarında, onlar yüzünden adamların derilerini kararmış görürsün.",
 [IDHA(),
  V("mt", "وُضِعَتْ", "wadaa", pas=True, doer=HIYA("الدُّرُوعِ", "the coats of mail", "zırhlara"), g=["mithal-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  PR("عَنِ", "an", n=N3(MT("وُضِعَتْ", "are taken off", "çıkarıldı»ya"), NT("وَحُرِّكَتْ نُونُهُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "its nun takes kasra where two quiescents meet", "nûnu iki sâkin buluştuğu için kesre almıştır"))),
  R("majr", "الْأَبْطَالِ", "batal-ant", g=["jam-taksir"]),
  R("zarfz", "يَوْمًا", "yawm", n=MZ("وُضِعَتْ", "are taken off", "çıkarıldı»ya"))],
 [V("mtu", "رَأَيْتُ", "raa", g=["naqis-verbs", "mafulayn"], n=CL("jawab")),
  JP("لَهَا", "li", "هَا", n=N3(MT("رَأَيْتُ", "you see", "görürsün»e"), ZW("قَوْلُهُ: «لَهَا»، أَيْ لِلُبْسِهَا", "«from them», that is, from wearing them", "«onlar yüzünden», yani onları giymekten"))),
  R("maf1", "جُلُودَ", "jild", mud=True, g=["jam-taksir"]),
  R("mdf", "الْقَوْمِ", "qawm"),
  R("maf2", "جُونَا", "jawn-amr", g=["jam-taksir", "kinaya"], n=N3(TANW_ALIF, DR("أَوْ هُوَ حَالٌ مِنْ «جُلُودَ الْقَوْمِ»", "or it is a hal of «the men's skins»", "yahut «adamların derileri»nden hâldir"), ZW("الْجَوْنُ: الْأَسْوَدُ، وَالْجَوْنُ: الْأَبْيَضُ، وَالْجَمْعُ الْجُونُ", "جَوْن is black, and also white; the plural is جُون", "«cevn» siyahtır, beyaz da demektir; cem'i «cûn»"),
    (" — وَفِيهِ كِنَايَةٌ عَنْ طُولِ لُبْسِهِمُ الدُّرُوعَ، بَيَّنَهَا الزَّوْزَنِيُّ: «رَأَيْتَ جُلُودَهُمْ سُودًا لِلُبْسِهِمْ إِيَّاهَا»", " — a kināya for how long they wear their mail, which al-Zawzanī makes plain: «you see their skins black from their wearing them»", " — zırhları uzun süre giymelerinden kinâyedir; Zevzenî açıklar: «onları giymekten derilerini kararmış görürsün»")))])
VV(80, "as though their folds were the faces of pools rippled by the winds when they blow.",
  "sanki kıvrımları, rüzgârlar estiğinde dalgalandırdığı göllerin yüzleridir.",
 [KAANNA("كَأَنَّ", g=TB, n=N3(DR("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا", "the sentence is a fresh one with no seat", "cümle müste'neftir, mahalli yoktur"),
    TSH("غُضُونُ الدُّرُوعِ", "the folds of the mail", "zırhların kıvrımları", "مُتُونُ الْغُدْرَانِ تَضْرِبُهَا الرِّيَاحُ", "the faces of pools struck by the winds", "rüzgârların dövdüğü göllerin yüzleri", "«كَأَنَّ»", "كَأَنَّ", "«keenne»", "شَبَّهَ غُضُونَ الدِّرْعِ بِمُتُونِ الْغُدْرَانِ إِذَا ضَرَبَتْهَا الرِّيَاحُ فِي جَرْيِهَا، وَالطَّرَائِقَ الَّتِي تُرَى فِي الدُّرُوعِ بِالَّتِي تَرَاهَا فِي الْمَاءِ إِذَا ضَرَبَتْهُ الرِّيحُ", "he likens the folds of the mail to the faces of pools when the winds strike them as they blow — the streaks seen on mail to those you see on water when the wind strikes it", "zırhın kıvrımlarını, rüzgârlar eserken dövdüğü göllerin yüzlerine; zırhlarda görülen çizgileri, rüzgâr vurunca suda gördüğün çizgilere benzetti", w=("الطَّرَائِقُ الْمُتَمَوِّجَةُ", "the rippling streaks", "dalgalanan çizgiler")))),
  R("ismka", "غُضُونَهُنَّ", "ghadan-amr", enc="هُنَّ", g=["jam-taksir"], n=DR("وَرِوَايَتُهُ: «مُتُونَهُنَّ»", "his text reads «their surfaces»", "onun rivayeti «mütûnehunne»dir")),
  R("khbka", "مُتُونُ", "matn", mud=True, g=["jam-taksir"]),
  R("mdf", "غُدْرٍ", "ghadir-amr", g=["jam-taksir"], n=ZW("الْغُدْرُ: مُخَفَّفُ غُدُرٍ، وَهُوَ جَمْعُ غَدِيرٍ", "غُدْر is a lightened غُدُر, the plural of غَدِير", "«ğudr», «gadîr»in cem'i olan «ğudur»un hafifletilmişidir"))],
 [V("d", "تُصَفِّقُهَا", "saffaqa-amr", enc="هَا", g=["form-ii-verbs"], n=N3(CL("nr", "مُتُونُ غُدْرٍ", "the faces of pools", "göllerin yüzleri»nin"), ZW("تُصَفِّقُهُ: تَضْرِبُهُ", "تُصَفِّقُهُ: strikes it", "«tusaffikuhû»: onu döver"))),
  R("fail", "الرِّيَاحُ", "rih", g=["jam-taksir"]),
  IDHA(plain=True, n=MZ("تُصَفِّقُ", "ripple", "dalgalandırır»a")),
  V("mn", "جَرَيْنَا", "jara", g=["naqis-verbs"], n=N3(ITLAQ, NT("وَالنُّونُ لِلرِّيَاحِ؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "the nun refers to the winds; the clause is in the seat of jarr, إِذَا being annexed to it", "nûn rüzgârlara döner; cümle «izâ»nın izâfetiyle mahallen mecrûr")))])
VV(81, "And on the morning of alarm we are carried by short-coated steeds, known as ours: rescued (from the foe) and weaned (among us).",
  "Dehşet sabahında bizi kısa tüylü atlar taşır; bizim olarak bilinirler: (düşman elinden) kurtarılmış ve (yanımızda) sütten kesilmiş.",
 [V("d", "وَتَحْمِلُنَا", "hamala", c="wi", enc="نَا", n=CL("ist")),
  R("zarfz", "غَدَاةَ", "ghadat", mud=True, n=MZ("تَحْمِلُ", "carry", "taşır»a")),
  R("mdf", "الرَّوْعِ", "raw-amr", g=["majaz-mursal", "anwa-al-majaz"], n=N3(ZW("الرَّوْعُ: الْفَزَعُ، وَيُرِيدُ بِهِ الْحَرْبَ هُنَا", "رَوْع is alarm; here he means war by it", "«rev'»: korku; burada onunla savaşı kastediyor"),
    HADD("مَجَازٌ مُرْسَلٌ عَلَاقَتُهُ الْمُسَبَّبِيَّةُ: أُطْلِقَ الرَّوْعُ — وَهُوَ مُسَبَّبٌ عَنِ الْحَرْبِ — وَأُرِيدَتِ الْحَرْبُ، كَمَا بَيَّنَهُ الزَّوْزَنِيُّ", "a majāz mursal whose tie is effect-for-cause: alarm, which war brings about, is said and war is meant, as al-Zawzanī makes plain", "alâkası müsebbebiyyet olan mecâz-ı mürsel: savaşın doğurduğu korku söylenmiş, savaş kastedilmiştir; Zevzenî'nin açıkladığı gibi"))),
  R("fail", "جُرْدٌ", "ajrad-ant", g=["jam-taksir", "hadhf-wa-taqdir"], n=N3(DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ", "it is the adjective of an omitted noun", "mahzûf bir mevsûfun sıfatıdır"), ZW("الْجُرْدُ: الَّتِي رَقَّ شَعَرُ جَسَدِهَا وَقَصُرَ", "جُرْد are horses whose body-hair is fine and short", "«curd»: vücut kılı ince ve kısa olan atlar")))],
 [V("mn", "عُرِفْنَ", "arafa", pas=True, n=DR("وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِلْمَوْصُوفِ الْمَحْذُوفِ", "the clause is a second adjective of the omitted noun", "cümle mahzûf mevsûfun ikinci sıfatıdır")),
  JP("لَنَا", "li", "نَا", n=MT("عُرِفْنَ", "known", "bilindiler»e")),
  R("hal", "نَقَائِذَ", "naqidha-amr", sign=S_DIPT_MJ, g=["jam-taksir", "mamnu-min-sarf"], n=N3(DR("مِنْ نُونِ النِّسْوَةِ", "of the nun of «known»", "nisve nûnundan hâl"), ZW("النَّقَائِذُ: الْمُخَلَّصَاتُ مِنْ أَيْدِي الْأَعْدَاءِ، وَاحِدَتُهَا نَقِيذَةٌ، فَعِيلَةٌ بِمَعْنَى مُفْعَلَةٍ", "نَقَائِذ are those rescued from the enemy's hands; one is a نَقِيذَة, a فَعِيلَة meaning مُفْعَلَة", "«nekâiz»: düşman elinden kurtarılmışlar; tekili «nakîze», «muf'ale» anlamında fa'île"))),
  V("mn", "وَافْتُلِينَا", "iftala-amr", c="w", pas=True, g=["form-viii-verbs", "naqis-verbs"], n=N3(ITLAQ, CL("atf", "عُرِفْنَ", "known", "bilindiler"), ZW("الْفَلْوُ وَالِافْتِلَاءُ: الْفِطَامُ؛ وَفُطِمَتْ عِنْدَنَا", "فَلْو and اِفْتِلَاء are weaning: they were weaned among us", "«felv» ve «iftilâ»: sütten kesmek; yanımızda sütten kesildiler")))])
VV(82, "They went down (to battle) mailed, and came out dishevelled, like knots of the reins worn thin.",
  "(Savaşa) zırhlı olarak indiler, saçı başı dağınık çıktılar; yıpranmış dizgin düğümleri gibi.",
 [V("mn", "وَرَدْنَ", "warada", g=["mithal-verbs", "hadhf-al-maful"], n=DR("وَمَفْعُولُهُ مَحْذُوفٌ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "its object is left out; the sentence is a fresh one", "mef'ûlü mahzûftur; cümle müste'neftir")),
  R("hal", "دَوَارِعًا", "dari-amr", g=["jam-taksir", "mamnu-min-sarf"], sign=("بِالْفَتْحَةِ — وَنُوِّنَ لِلضَّرُورَةِ، وَحَقُّهُ الْمَنْعُ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ (الدُّرَّةُ)، وَبِالتَّنْوِينِ يَسْتَقِيمُ الْوَزْنُ", " — by the fatha: given tanwin for the metre's need, though by right a diptote on the furthest plural pattern (al-Durra); the tanwin is what the metre needs", " — fetha ile; vezin zarureti için tenvin almıştır, aslında müntehe'l-cumû' sîgası olduğu için gayr-i munsariftir (Dürre); vezin tenvinle düzelir"),
    n=N3(NT("مِنْ نُونِ النِّسْوَةِ", "of the nun of «they went down»", "nisve nûnundan hâl"), ZW("رَجُلٌ دَارِعٌ: عَلَيْهِ دِرْعٌ، وَدُرُوعُ الْخَيْلِ تَجَافِيفُهَا", "a man دَارِع wears a coat of mail; horses' mail is their barding", "«dâri'» adam: üzerinde zırh olan; atların zırhı ise «tecâfîf»leridir"))),
  V("mn", "وَخَرَجْنَ", "kharaja", c="w", g=["tibaq"], n=N3(CL("atf", "وَرَدْنَ", "went down", "indiler"), HADD("طِبَاقٌ بَيْنَ «وَرَدْنَ» وَ«خَرَجْنَ»: الْوُرُودُ وَالْخُرُوجُ ضِدَّانِ", "a ṭibāq between «went down (into)» and «came out», which are contraries", "«indiler» ile «çıktılar» arasında tıbâk: girmek ve çıkmak zıttır"))),
  R("hal", "شُعْثًا", "ashath-amr", g=["jam-taksir"], n=NT("مِنْ نُونِ النِّسْوَةِ", "of the nun of «came out»", "nisve nûnundan hâl"))],
 [R("majr", "كَأَمْثَالِ", "mithl", j="ka", mud=True, g=TB + ["jam-taksir"], n=N3(DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«خَرَجْنَ»، أَوْ بِمَحْذُوفٍ حَالٍ ثَانِيَةٍ", "the phrase hangs on «came out», or on an omitted second hal", "câr-mecrûr «çıktılar»a, yahut mahzûf ikinci bir hâle müteallik"),
    TSH("الْخَيْلُ الْبَالِيَةُ مِنَ الْكَلَالِ", "the horses worn thin with weariness", "yorgunluktan yıpranmış atlar", "الرَّصَائِعُ — عُقَدُ الْأَعِنَّةِ الْبَالِيَةُ", "the worn knots of the reins", "yıpranmış dizgin düğümleri", "الْكَافُ وَ«أَمْثَال»", "the kaf with أَمْثَال", "kâf ve «emsâl»", "خَرَجْنَ مِنْهَا شُعْثًا قَدْ بَلِينَ بِلَى عُقَدِ الْأَعِنَّةِ لِمَا نَالَهَا مِنَ الْكَلَالِ وَالْمَشَاقِّ فِيهَا", "they came out of it dishevelled, worn as the knots of the reins wear, from the weariness and toil they met in it", "oradan saçı başı dağınık çıktılar; yaşadıkları yorgunluk ve meşakkatten dizgin düğümlerinin yıprandığı gibi yıprandılar", wajh_in_verse=True, w=("الْبِلَى «قَدْ بَلِينَ»", "the wearing thin, «worn thin»", "yıpranma, «yıprandılar»")))),
  R("mdf", "الرَّصَائِعِ", "rasia-amr", g=["jam-taksir"], n=ZW("الرَّصَائِعُ: جَمْعُ الرَّصِيعَةِ، وَهِيَ عُقْدَةُ الْعِنَانِ عَلَى قَذَالِ الْفَرَسِ", "رَصَائِع is the plural of رَصِيعَة, the knot of the rein on the horse's poll", "«resâi'», atın ensesindeki dizgin düğümü olan «resîa»nın cem'idir")),
  QAD(),
  V("mn", "بَلِينَا", "balia", g=["naqis-verbs"], n=N3(ITLAQ, DR("وَالْجُمْلَةُ صِفَةٌ لِـ«الرَّصَائِعِ» عَلَى أَنَّ «أَلْ» فِيهَا لِلْجِنْسِ", "the clause is an adjective of «the knots», their «al» marking the kind", "cümle, «el» cins için sayılarak «düğümler»in sıfatıdır"), ZW("وَعَلَى شَرْحِهِ هِيَ لِلْخَيْلِ: قَدْ بَلِينَ بِلَى عُقَدِ الْأَعِنَّةِ", "in his gloss it is said of the horses: worn as the knots of the reins wear", "onun şerhine göre atlar içindir: dizgin düğümleri gibi yıprandılar")))])
VV(83, "We inherited them from fathers true (in deed and word), and we shall leave them to our sons when we die.",
  "Onları sadık (sözü özü doğru) atalardan miras aldık; öldüğümüzde de oğullarımıza miras bırakacağız.",
 [V("mna", "وَرِثْنَاهُنَّ", "waritha", enc="هُنَّ", g=["mithal-verbs"], n=CL("ist")),
  PR("عَنْ", "an", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَرِثْنَا»", "the phrase hangs on «we inherited»", "câr-mecrûr «miras aldık»a müteallik")),
  R("majr", "آبَاءِ", "ab", mud=True, g=["jam-taksir"]),
  R("mdf", "صِدْقٍ", "sidq", n=N3(NT("وَالْإِضَافَةُ لِلْوَصْفِ: آبَاءٍ صَادِقِينَ", "the idafa describes: «truthful fathers»", "izâfet vasıf içindir: «sadık atalar»"), ZW("مِنْ آبَاءٍ كِرَامٍ شَأْنُهُمُ الصِّدْقُ فِي الْفَعَالِ وَالْمَقَالِ", "from noble fathers whose way was truth in deed and word", "işte ve sözde doğruluğu şiar edinmiş kerim atalardan")))],
 [V("d", "وَنُورِثُهَا", "awratha", c="w", enc="هَا", encrole="maf1", doer=NAHNU, g=["form-iv-verbs", "mafulayn", "tibaq"], n=N3(CL("atf", "وَرِثْنَاهُنَّ", "we inherited them", "miras aldık"), HADD("طِبَاقٌ بَيْنَ «وَرِثْنَاهُنَّ» وَ«نُورِثُهَا»: الْأَخْذُ بِالْإِرْثِ وَالتَّرْكُ لِلْوَارِثِ مُتَقَابِلَانِ", "a ṭibāq between «we inherited them» and «we shall leave them»: receiving an inheritance and handing it on are opposed", "«miras aldık» ile «miras bırakacağız» arasında tıbâk: mirası almak ve mirasçıya bırakmak birbirine karşıttır"))),
  IDHA(plain=True, n=MZ("نُورِثُ", "shall leave", "miras bırakacağız»a")),
  V("mna", "مُتْنَا", "mata-die", g=["hollow-verbs"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "its middle letter dropped where two quiescents meet", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür"))),
  R("maf2", "بَنِينَا", "banu", sign=S_MULHAQ_I, g=["jam-mudhakkar-salim"], n=ZW("يُرِيدُ أَنَّهَا تَنَاتَجَتْ وَتَنَاسَلَتْ عِنْدَهُمْ قَدِيمًا", "he means they have bred and multiplied among them from of old", "onların yanında eskiden beri doğup üremiş olduklarını kasteder"))])
VV(84, "Behind us are white, fair women, for whom we fear that they be shared out (as captives) or brought low.",
  "Ardımızda beyaz, güzel kadınlar vardır; (esir olarak) paylaştırılmalarından yahut hor görülmelerinden sakınırız.",
 [PR("عَلَى", "ala", n=MTH("خَبَرٍ مُقَدَّمٍ", "an omitted, fronted khabar", "öne alınmış mahzûf habere")),
  R("majr", "آثَارِنَا", "athar", enc="نَا", g=["jam-taksir"]),
  R("mub", "بِيضٌ", "abyad", g=["jam-taksir", "hadhf-wa-taqdir"], n=N3(NT("مُؤَخَّرٌ", "put after its khabar", "haberinden sonraya bırakılmış"), DR("وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: نِسَاءٌ بِيضٌ", "it is the adjective of an omitted noun: «white women»", "mahzûf bir mevsûfun sıfatıdır: «beyaz kadınlar»"))),
  R("naatr", "حِسَانٌ", "hasan-adj", g=["jam-taksir"], of=("بِيضٌ", "white", "beyaz"))],
 [V("d", "نُحَاذِرُ", "hadhara3-amr", doer=NAHNU, g=["form-iii-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَا»، وَيَجُوزُ الِاسْتِئْنَافُ", "the clause is a hal of «us», in the seat of nasb; it may also be a fresh sentence", "cümle «biz»den hâl, mahallen mansûb; müste'nef de olabilir")),
  AN(n=NT("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَفْعُولٍ بِهِ لِـ«نُحَاذِرُ»", "أَنْ and the verb make a masdar, the object of «we fear»", "«en» ile fiil «sakınırız»ın mef'ûlü olan bir masdar olur")),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "تُقَسَّمَ", "qassama", pas=True, doer=HIYA("النِّسَاءِ", "the women", "kadınlara"), g=["form-ii-verbs", "kinaya"], n=(" — وَفِيهِ كِنَايَةٌ عَنِ السَّبْيِ، بَيَّنَهَا الزَّوْزَنِيُّ: «نُحَاذِرُ عَلَيْهَا أَنْ يَسْبِيَهَا الْأَعْدَاءُ فَتُقَسِّمَهَا وَتُهِينَهَا»", " — a kināya for captivity, which al-Zawzanī makes plain: «we fear for them that the enemy take them captive, share them out and humble them»", " — esaretten kinâyedir; Zevzenî açıklar: «düşmanın onları esir edip paylaştırmasından ve hor görmesinden sakınırız»")),
  PT("أَوْ", "aw", "حَرْفُ عَطْفٍ", "a conjunction («or»)", "atıf harfi («yahut»)", g=["atf-nasaq"]),
  V(NS("لِعَطْفِهِ عَلَى «تُقَسَّمَ»", "being joined to «be shared out»", "«paylaştırılsın»a atfedildiği için"), "تَهُونَا", "hana", doer=HIYA("النِّسَاءِ", "the women", "kadınlara"), g=["hollow-verbs"], n=ITLAQ)])
VV(85, "They have bound their husbands by a pledge: when they meet squadrons marked (for battle) —",
  "Kocalarından bir ahit almışlardır: (savaş için) nişanlı bölüklerle karşılaştıklarında —",
 [V("mn", "أَخَذْنَ", "akhadha", n=NT("وَالْجُمْلَةُ صَالِحَةٌ لِلِاسْتِئْنَافِ، وَلِلْوَصْفِيَّةِ مِنَ «الْبِيضِ» قَبْلَهُ", "the sentence may be a fresh one, or an adjective of «the white women» before it", "cümle müste'nef olabileceği gibi önceki «beyazlar»ın sıfatı da olabilir")),
  PR("عَلَى", "ala", n=MT("أَخَذْنَ", "bound", "aldılar»a")),
  R("majr", "بُعُولَتِهِنَّ", "baal-amr", enc="هِنَّ", g=["jam-taksir"], n=ZW("وَالْبُعُولُ وَالْبُعُولَةُ جَمْعُ بَعْلٍ، يُقَالُ لِلرَّجُلِ: هُوَ بَعْلُ الْمَرْأَةِ", "بُعُول and بُعُولَة are plurals of بَعْل: a man is called the بَعْل of the woman", "«buûl» ve «buûle», «ba'l»in cem'idir: adama kadının «ba'l»i denir")),
  R("maf", "عَهْدًا", "ahd")],
 [IDHA(n=DR("وَجَوَابُهَا مَحْذُوفٌ دَلَّ عَلَيْهِ جَوَابُ الْقَسَمِ فِي الْبَيْتِ بَعْدَهُ، لِأَنَّ «الْعَهْدَ» يَتَضَمَّنُ الْقَسَمَ", "its answer is left out, shown by the answer of the oath in the next verse — for «pledge» holds an oath", "cevabı mahzûftur; sonraki beyitteki yeminin cevabı ona delâlet eder, çünkü «ahit» yemin anlamı taşır")),
  V("mwa", "لَاقَوْا", "laqa-meet", g=["form-iii-verbs", "naqis-verbs"], n=N3(NT("وَالْأَلِفُ فَارِقَةٌ", "the alif only marks the plural", "elif fârikadır"), CL("mdf", "إِذَا", "إِذَا", "izâ"))),
  R("maf", "كَتَائِبَ", "katiba", sign=S_DIPT_MJ, g=["jam-taksir", "mamnu-min-sarf"]),
  R("naatn", "مُعْلِمِينَا", "mulim-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"], of=("كَتَائِبَ", "squadrons", "bölükler"), n=ZW("قَدْ أَعْلَمُوا أَنْفُسَهُمْ بِعَلَامَاتٍ يُعْرَفُونَ بِهَا فِي الْحُرُوبِ", "who have marked themselves with signs by which they are known in war", "savaşta tanınacakları nişanlarla kendilerini işaretlemiş olanlar"))])
# ---- vv. 86–91 — الظَّعَائِنُ ----
ROLE["khbl"] = ("خَبَرُ «لَيْسَ» مَنْصُوبٌ", "the predicate of لَيْسَ, in nasb", "«leyse»nin haberi, mansûb", "nasb", ["kana-wa-akhawatuha"])
NISA = HIYA("النِّسَاءِ", "the women", "kadınlara")
VV(86, "— they are surely to carry off horses and white (swords), and captives coupled together in iron.",
  "— mutlaka atlar, beyaz (kılıçlar) ve demirlere bağlanmış esirler kapacaklardır.",
 [T("لَيَسْتَلِبُنَّ", "istalaba-amr", "verb", ["form-viii-verbs", "nun-tawkid", "afal-khamsa"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ الَّذِي تَضَمَّنَهُ «عَهْدًا» فِي الْبَيْتِ قَبْلَهُ، وَ«يَسْتَلِبُنَّ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالنُّونِ الْمَحْذُوفَةِ لِتَوَالِي الْأَمْثَالِ، وَوَاوُ الْجَمَاعَةِ الْمَحْذُوفَةُ — الدَّالُّ عَلَيْهَا الضَّمَّةُ — " + _FA + "، وَالنُّونُ لِلتَّوْكِيدِ؛ وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا، وَجَوَابُ «إِذَا» مَحْذُوفٌ دَلَّ عَلَيْهِ جَوَابُ الْقَسَمِ (الدُّرَّةُ).",
    "The lam opens the answer of the oath held in «a pledge» in the verse before; يَسْتَلِبُنَّ is a present verb in raf' by a nun dropped because like letters follow one another; the dropped waw of the group, shown by the damma, is the doer, in the seat of raf'; the nun is of emphasis; the clause answers the oath and has no seat, and the answer of إِذَا is left out, the oath's answer showing it (al-Durra).",
    "Lâm, önceki beyitteki «ahit» kelimesinin taşıdığı yeminin cevabındadır; «yestelibunne», benzer harfler art arda geldiği için düşen nûn ile merfû muzâridir; dammenin delâlet ettiği düşmüş cemaat vâvı fâildir, mahallen merfû; nûn te'kîd içindir; cümle yeminin cevabıdır, mahalli yoktur; «izâ»nın cevabı mahzûftur, yeminin cevabı ona delâlet eder (Dürre).",
    segs=SG(("لَ", "lam-jawab", "part"), ("يَسْتَلِبُ", "istalaba-amr", "verb"), ("نَّ", "nun-tawkid", "part"))),
  R("maf", "أَفْرَاسًا", "faras", g=["jam-taksir"], n=DR("وَرِوَايَتُهُ: «أَبْدَانًا»", "his text reads «coats of mail (أَبْدَانًا)»", "onun rivayeti «ebdânen»dır")),
  R("atfn", "وَبِيضًا", "abyad", c="w", g=["jam-taksir"], of=("أَفْرَاسًا", "horses", "atlar"))],
 [R("atfn", "وَأَسْرَى", "asir", c="w", sign=S_AN, g=["jam-taksir", "ism-maqsur-manqus"], of=("أَفْرَاسًا", "horses", "atlar")),
  PR("فِي", "fi", n=MT("مُقَرَّنِينَا", "coupled", "bağlanmış»a")),
  R("majr", "الْحَدِيدِ", "hadid"),
  R("naatn", "مُقَرَّنِينَا", "muqarran-amr", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-maful"], of=("أَسْرَى", "captives", "esirler"), n=ZW("أَيْ وَأَسْرَى مِنْهُمْ قَدْ قُرِنُوا فِي الْحَدِيدِ", "that is, captives of theirs coupled together in iron", "yani demirlerde birbirine bağlanmış esirler"))])
VV(87, "You see us out in the open ground, while every tribe has taken fear of us for its companion.",
  "Bizi açık arazide görürsün; oysa her kabile bizden korkuyu kendine yoldaş edinmiştir.",
 [V("da", "تَرَانَا", "raa", enc="نَا", encrole="maf1", doer=ANTA, g=["naqis-verbs", "mafulayn"], n=CL("ist")),
  R("maf2", "بَارِزِينَ", "bariz", sign=(S_JMS[0] + "، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", S_JMS[1] + "; its nun stands for the tanwin of the singular", S_JMS[2] + "; nûn müfreddeki tenvinin karşılığıdır"), g=["jam-mudhakkar-salim", "ism-fail", "kinaya"], n=N3(DR("أَوْ هُوَ حَالٌ مِنْ «نَا» إِنْ كَانَتْ «تَرَى» بَصَرِيَّةً", "or it is a hal of «us» if «see» is of the eye", "«görürsün» gözle görme ise «biz»den hâldir"),
    (" — وَفِيهِ كِنَايَةٌ عَنِ الثِّقَةِ بِالْقُوَّةِ، بَيَّنَهَا الزَّوْزَنِيُّ: «تَرَانَا خَارِجِينَ إِلَى الْأَرْضِ الْبَرَازِ — وَهِيَ الصَّحْرَاءُ الَّتِي لَا جَبَلَ بِهَا — لِثِقَتِنَا بِنَجْدَتِنَا وَشَوْكَتِنَا»", " — a kināya for trust in their own strength, which al-Zawzanī makes plain: «you see us going out into the open ground — the desert without a mountain — for our trust in our valour and our might»", " — kendi güçlerine güvenden kinâyedir; Zevzenî açıklar: «bizi yiğitliğimize ve şevketimize güvendiğimiz için açık araziye — dağı olmayan çöle — çıkmış görürsün»"))),
  R("mub", "وَكُلُّ", "kull", c="wh", mud=True, n=NT("وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ (الدُّرَّةُ)", "the nominal clause is a hal, in the seat of nasb (al-Durra)", "isim cümlesi hâldir, mahallen mansûb (Dürre)")),
  R("mdf", "حَيٍّ", "hayy-tribe")],
 [QAD("قَدِ", kasr=True),
  V("mw", "اتَّخَذُوا", "ittakhadha", g=["form-viii-verbs", "mafulayn"], n=N3(NT("وَالْأَلِفُ فَارِقَةٌ؛ وَجُمِعَ حَمْلًا عَلَى مَعْنَى «كُلُّ حَيٍّ»", "the alif only marks the plural; it is plural following the sense of «every tribe»", "elif fârikadır; «her kabile»nin anlamına göre cem' getirilmiştir"), CL("khb", "كُلُّ", "every", "her"))),
  R("maf1", "مَخَافَتَنَا", "makhafa", enc="نَا", n=NT("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", "a masdar annexed to its object", "masdarın mef'ûlüne izâfeti")),
  R("maf2", "قَرِينَا", "qarin-amr", g=TB, n=N3(TANW_ALIF, HADD("تَشْبِيهٌ بَلِيغٌ: جُعِلَتْ مَخَافَتُهُمْ مِنَّا قَرِينًا لَهُمْ — وَالْمَفْعُولَانِ أَصْلُهُمَا مُبْتَدَأٌ وَخَبَرٌ — حُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ (الْمُلَازَمَةُ)؛ وَمَعْنَاهُ عِنْدَ الزَّوْزَنِيِّ: «كُلُّ قَبِيلَةٍ تَسْتَجِيرُ وَتَعْتَصِمُ بِغَيْرِهَا مَخَافَةَ سَطْوَتِنَا بِهَا»", "a tashbih baligh: their fear of us is made their companion — the two objects are at root a mubtada and khabar — with the particle and the point (keeping close) left out; al-Zawzanī's sense: «every tribe seeks protection and shelter with others for fear of our assault on it»", "teşbîh-i belîğ: bizden korkuları onlara yoldaş kılınmıştır — iki mef'ûl aslında mübtedâ ve haberdir — edat ve vech-i şebeh (ayrılmamak) hazfedilmiştir; Zevzenî'ye göre mâna: «her kabile, saldırımızdan korktuğu için başkasına sığınır»")))])
VV(88, "When they come (at evening), they walk gently, swaying as the backs of drinkers sway.",
  "(Akşamleyin) geldiklerinde ağır ağır yürürler, içkiye dalmışların sırtlarının sallandığı gibi salınarak.",
 [IDHA(),
  MA_Z(),
  V("mn", "رُحْنَ", "raha-become", g=["hollow-verbs"], n=N3(NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "its middle letter dropped where two quiescents meet", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür"), CL("mdf", "إِذَا", "إِذَا", "izâ"))),
  V("dn", "يَمْشِينَ", "masha", g=["naqis-verbs"], n=CL("jawab")),
  R("mutlaq", "الْهُوَيْنَى", "huwayna-amr", sign=S_AN, g=["ism-maqsur-manqus"], n=N3(DR("مِثْلُ «قَعَدَ الْقُرْفُصَاءَ»", "like «he sat squatting»", "«kaade'l-kurfusâ» gibi"), ZW("الْهُوَيْنَى: تَصْغِيرُ الْهُونَى، وَهِيَ تَأْنِيثُ الْأَهْوَنِ؛ يَمْشِينَ مَشْيًا رَفِيقًا لِثِقَلِ أَرْدَافِهِنَّ", "هُوَيْنَى is the diminutive of هُونَى, feminine of أَهْوَن: they walk gently for the weight of their haunches", "«huveynâ», «ehven»in müennesi «hûnâ»nın tasgîridir: kalçalarının ağırlığından yavaş yürürler")))],
 [T("كَمَا", "ma-masdariyya", "part", ["tashbih", "arkan-al-tashbih", "aqsam-al-tashbih", "huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» حَرْفٌ مَصْدَرِيٌّ، وَهِيَ وَالْفِعْلُ بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ: مَشْيًا كَاضْطِرَابِ … — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ نَصَّ عَلَيْهِ الزَّوْزَنِيُّ: «ثُمَّ شَبَّهَهُنَّ فِي تَبَخْتُرِهِنَّ بِالسُّكَارَى فِي مَشْيِهِمْ»؛ الْمُشَبَّهُ مَشْيُهُنَّ، وَالْمُشَبَّهُ بِهِ اضْطِرَابُ مُتُونِ الشَّارِبِينَ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ الِاضْطِرَابُ مَذْكُورٌ فِي الْبَيْتِ.",
    "The kaf is the jarr letter of likening, and مَا a masdar particle; with the verb it makes a masdar in jarr by the kaf, the phrase hanging on an omitted adjective of an absolute object: «a walk like the swaying …» — a tashbih mursal mufassal that al-Zawzanī states: «then he likens them, in their swaying gait, to drunkards walking»; their walk is likened to the swaying of drinkers' backs; the particle is the kaf; the point, swaying, is named in the verse.",
    "Kâf teşbîh ve cer harfi, «mâ» masdar harfidir; sonraki fiille kâf ile mecrûr bir masdar olur; câr-mecrûr mahzûf mef'ûl-i mutlakın mahzûf sıfatına müteallik: «… sallanışı gibi bir yürüyüş» — Zevzenî'nin açıkça söylediği teşbîh-i mürsel mufassal: «sonra onları salınışlarında sarhoşların yürüyüşüne benzetti»; müşebbeh onların yürüyüşü, müşebbehün bih içkiye dalmışların sırtlarının sallanışı, edat kâf; vech-i şebeh — sallanmak — beyitte zikredilmiştir.",
    segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part"))),
  V("mt", "اضْطَرَبَتْ", "idtaraba", g=["form-viii-verbs"]),
  R("fail", "مُتُونُ", "matn", mud=True, g=["jam-taksir"]),
  R("mdf", "الشَّارِبِينَا", "sharib", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"])])
VV(89, "They give our steeds their rations and say: «You are not our husbands if you do not defend us.»",
  "Atlarımızın yemini verirler ve «Bizi korumazsanız kocalarımız değilsiniz» derler.",
 [V("dn", "يَقُتْنَ", "qata-amr", g=["hollow-verbs"], n=N3(NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "its middle letter dropped where two quiescents meet; the sentence is a fresh one", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür; cümle müste'neftir"), ZW("الْقُوتُ: الْإِطْعَامُ بِقَدْرِ الْحَاجَةِ، وَالْفِعْلُ قَاتَ يَقُوتُ؛ يَعْلِفْنَ خَيْلَنَا الْجِيَادَ", "قُوت is feeding as much as is needed; the verb is قَاتَ يَقُوتُ: they fodder our fine horses", "«kût»: ihtiyaç kadar yedirmek; fiili «kâte yekûtu»: güzel atlarımıza yem verirler"))),
  R("maf", "جِيَادَنَا", "jawad", enc="نَا", g=["jam-taksir"]),
  V("dn", "وَيَقُلْنَ", "qala", c="w", g=["hollow-verbs"], n=NT("وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ", "its middle letter dropped where two quiescents meet", "iki sâkin buluştuğu için ayn'el-fiili düşmüştür")),
  T("لَسْتُمْ", "laysa", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَ«تُمْ» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "A defective, frozen past verb built on sukun because the subject pronoun is attached; تُمْ is its noun, in the seat of raf'; the clause is what they say, in the seat of nasb.", "Ref' zamiri bitiştiği için sükûn üzere mebnî câmid nâkıs mâzî; «tum» mahallen merfû ismidir; cümle mahallen mansûb mekûl-i kavldir.")],
 [R("khbl", "بُعُولَتَنَا", "baal-amr", enc="نَا", g=["jam-taksir"]),
  IDHA(n=NT("وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ", "its answer is left out, shown by what goes before", "cevabı mahzûftur, öncesi ona delâlet eder")),
  LAM(),
  V(JZ("بِـ«لَمْ»", "by لَمْ", "«lem» ile", sign="nun"), "تَمْنَعُونَا", "manaa", enc="نَا", g=["afal-khamsa", "fail"], n=N3(W5, CL("mdf", "إِذَا", "إِذَا", "izâ"), ZW("إِذَا لَمْ تَمْنَعُونَا مِنْ سَبْيِ الْأَعْدَاءِ إِيَّانَا", "if you do not defend us from being taken captive by the enemy", "bizi düşmanın esir etmesinden korumazsanız")))])
VV(90, "— women of the litters of the Banū Jusham ibn Bakr, who have joined to beauty noble lineage and religion.",
  "— Benî Cüşem b. Bekr'in hevdeçli kadınları; güzelliğe soyluluğu ve dindarlığı katmışlardır.",
 [R("khb", "ظَعَائِنُ", "zaina", sign=("بِالضَّمَّةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ", " — by the damma, without tanwin: a diptote on the furthest plural pattern", " — damme ile; müntehe'l-cumû' sîgası olduğu için gayr-i munsarif, tenvinsiz"), g=["jam-taksir", "mamnu-min-sarf", "hadhf-wa-taqdir"], n=DR("لِمُبْتَدَإٍ مَحْذُوفٍ: هُنَّ ظَعَائِنُ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "of an omitted mubtada: «they are women of the litters»; the sentence is a fresh one", "mahzûf bir mübtedânın haberi: «onlar hevdeçli kadınlardır»; cümle müste'neftir")),
  PR("مِنْ", "min", n=MTH("صِفَةٍ لِـ«ظَعَائِنُ»", "an omitted adjective of «women of the litters»", "«hevdeçli kadınlar»ın mahzûf sıfatına")),
  R("majr", "بَنِي", "banu", mud=True, sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"]),
  R("mdf", "جُشَمِ", "jusham-amr", pos="propn", sign=JUSHAM_S),
  R("naatj", "بْنِ", "ibn", mud=True, of=("جُشَمِ", "Jusham", "Cüşem")),
  R("mdf", "بَكْرٍ", "bakr", pos="propn")],
 [V("mn", "خَلَطْنَ", "khalata", n=DR("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «ظَعَائِنُ» بَعْدَ وَصْفِهِ، وَ«قَدْ» مُقَدَّرَةٌ؛ وَالِاسْتِئْنَافُ مُمْكِنٌ", "the clause is a hal of «women of the litters», described as they are, with قَدْ understood; it may also be a fresh sentence", "cümle, nitelendikten sonra «hevdeçli kadınlar»dan hâldir, «kad» takdir edilir; müste'nef de olabilir")),
  R("majr", "بِمِيسَمٍ", "misam-amr", j="bi", n=N3(MT("خَلَطْنَ", "joined", "kattılar»a"), ZW("الْمِيسَمُ: الْحُسْنُ، وَهُوَ مِنَ الْوَسَامِ وَالْوَسَامَةِ", "مِيسَم is beauty, from وَسَام and وَسَامَة", "«mîsem»: güzellik; «vesâm» ve «vesâme»dendir"))),
  R("maf", "حَسَبًا", "hasab", n=ZW("الْحَسَبُ: مَا يُحْسَبُ مِنْ مَكَارِمِ الْإِنْسَانِ وَمَكَارِمِ أَسْلَافِهِ، فَعَلٌ فِي مَعْنَى مَفْعُولٍ", "حَسَب is what is counted of a man's noble deeds and his forebears', a فَعَل in the sense of مَفْعُول", "«haseb»: insanın ve atalarının sayılan meziyetleri; mef'ûl anlamında fa'al")),
  R("atfn", "وَدِينًا", "din", c="w", of=("حَسَبًا", "noble lineage", "soyluluk"), n=TANW_ALIF)])
VV(91, "Nothing keeps the women of the litters (from capture) like a smiting from which you see forearms (flying) like the sticks of a boys' game.",
  "Hevdeçli kadınları (esirlikten) hiçbir şey, kolları çocuk oyunundaki çubuklar gibi (uçar) gördüğün bir vuruş kadar korumaz.",
 [PT("وَمَا", "ma-nafiya", "مَا حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ", "مَا, a particle of negation that governs nothing", "«mâ» nefy harfi, ameli yoktur", c="wi", g=["anwa-ma"]),
  V("m", "مَنَعَ", "manaa", n=CL("ist")),
  R("maf", "الظَّعَائِنَ", "zaina", g=["jam-taksir"], n=ZW("أَيْ مَا مَنَعَ النِّسَاءَ مِنْ سَبْيِ الْأَعْدَاءِ إِيَّاهُنَّ", "that is, nothing kept the women from being taken captive by the enemy", "yani kadınları düşmanın esir etmesinden hiçbir şey korumadı")),
  R("fail", "مِثْلُ", "mithl", mud=True),
  R("mdf", "ضَرْبٍ", "darb")],
 [V("da", "تَرَى", "raa", doer=ANTA, g=["naqis-verbs"], n=DR("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«ضَرْبٍ»", "the clause is an adjective of «a smiting», in the seat of jarr", "cümle «vuruş»un sıfatı, mahallen mecrûr")),
  JP("مِنْهُ", "min", "هُ", n=MT("تَرَى", "you see", "görürsün»e")),
  R("maf", "السَّوَاعِدَ", "saida-amr", g=["jam-taksir"]),
  R("majr", "كَالْقُلِينَا", "qula-amr", j="ka", sign=S_MULHAQ_I, g=TB + ["jam-mudhakkar-salim"], n=N3(DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «السَّوَاعِدَ»", "the phrase hangs on an omitted hal of «forearms»", "câr-mecrûr «kollar»ın mahzûf hâline müteallik"),
    TSH("السَّوَاعِدُ الْمُتَطَايِرَةُ", "the flying forearms", "uçuşan kollar", "الْقُلُونَ تَطِيرُ إِذَا ضُرِبَتْ بِالْمِقْلَى", "the tipcat-sticks that fly when struck with the bat", "sopayla vurulunca uçan çelik çubukları", "الْكَافُ", "the kaf", "kâf", "مَا مَنَعَ النِّسَاءَ … مِثْلَ ضَرْبٍ تَنْدُرُ وَتَطِيرُ مِنْهُ سَوَاعِدُ الْمَضْرُوبِينَ كَمَا تَطِيرُ الْقُلَةُ إِذَا ضُرِبَتْ بِالْمِقْلَى", "nothing kept the women … like a smiting from which the forearms of the smitten fly off as the stick flies when struck with the bat", "kadınları … vurulanların kollarının, sopayla vurulan çelik çubuğu gibi uçtuğu bir vuruş kadar hiçbir şey korumadı", w=("التَّطَايُرُ", "flying off", "uçuşmak"))))])
# ---- vv. 92–97 — قَدْ عَلِمَ الْقَبَائِلُ ----
CONJ["wt"] = ("wa", "الْوَاوُ اعْتِرَاضِيَّةٌ، وَ", "The waw opens a parenthesis; ", "Vâv i'tirâziyyedir; ")
S_MULHAQ_N = ("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ، وَالْأَلِفُ لِلْإِطْلَاقِ", " — by the ya, as it declines like the sound masculine plural; its nun stands for the tanwin of the singular, and the final alif is the alif of iṭlāq", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûn müfreddeki tenvinin karşılığı, sondaki elif ıtlâk elifidir")
def LIMA(gov_ar, gov_en, gov_tr):
    return T("لِمَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ يُقَوِّي عَمَلَ اسْمِ الْفَاعِلِ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِهَا، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«" + gov_ar + "».",
             "The lam is a jarr letter that strengthens the active participle's working; مَا is a relative noun built on sukun, in the seat of jarr after it; the phrase hangs on «" + gov_en + "».", "Lâm, ism-i fâilin amelini kuvvetlendiren cer harfidir; «mâ» sükûn üzere mebnî ism-i mevsûl, onunla mahallen mecrûr; câr-mecrûr «" + gov_tr + " müteallik.", segs=SG(("لِ", "li", "prep"), ("مَا", "ma-mawsula", "pron")))
ANNA_W = lambda: INNA("وَأَنَّا", "anna", enc="نَا", c="w", n=NT("وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْمَصْدَرِ قَبْلَهُ", "the masdar it makes is joined to the one before", "oluşan masdar öncekine ma'tûftur"))
VV(92, "It is as though, when the swords are drawn, we had begotten all mankind, every one of them.",
  "Kılıçlar sıyrıldığında sanki bütün insanları, hepsini biz doğurmuşuzdur.",
 [KAANNA("كَأَنَّا", enc="نَا", g=TB, n=N3(NT("وَحُذِفَتْ إِحْدَى النُّونَاتِ لِلتَّخْفِيفِ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "one nun dropped for ease; the sentence is a fresh one", "nûnlardan biri hafiflik için düşmüştür; cümle müste'neftir"),
    TSH("الشَّاعِرُ وَقَوْمُهُ فِي حِمَايَتِهِمُ النَّاسَ", "the poet's people in their protecting of all men", "şairin kavmi, insanları korumalarında", "آبَاءُ النَّاسِ جَمِيعًا", "the fathers of all mankind", "bütün insanların babaları", "«كَأَنَّ»", "كَأَنَّ", "«keenne»", "كَأَنَّ حَالَ اسْتِلَالِ السُّيُوفِ مِنْ أَغْمَادِهَا — أَيْ حَالَ الْحَرْبِ — وَلَدْنَا جَمِيعَ النَّاسِ، أَيْ نَحْمِيهِمْ حِمَايَةَ الْوَالِدِ وَلَدَهُ", "as though, when swords are drawn from their scabbards — that is, in war — we had begotten all men: we protect them as a father protects his child", "sanki kılıçlar kınlarından sıyrıldığında — yani savaşta — bütün insanları biz doğurmuşuz: babanın evladını koruduğu gibi onları koruruz", w=("الْحِمَايَةُ", "protection", "himaye")))),
  R("mub", "وَالسُّيُوفُ", "sayf", c="wt", g=["jam-taksir", "jumla-mutarida"]),
  R("khb", "مُسَلَّلَاتٌ", "musallal-amr", g=["jam-muannath-salim", "ism-maful"], n=DR("وَالْجُمْلَةُ مُعْتَرِضَةٌ بَيْنَ اسْمِ «كَأَنَّ» وَخَبَرِهَا؛ وَجُوِّزَ أَنْ تَكُونَ حَالًا مِنْ «نَا»، وَالْأَوَّلُ أَوْلَى", "the clause is a parenthesis between the noun of كَأَنَّ and its predicate; it could also be a hal of «us», but the first is better", "cümle «keenne»nin ismi ile haberi arasında mu'tarızadır; «biz»den hâl olması da caiz görülmüş, birincisi evlâdır"))],
 [V("mna", "وَلَدْنَا", "walada", g=["mithal-verbs"], n=CL("khb", "كَأَنَّ", "كَأَنَّ", "keenne")),
  R("maf", "النَّاسَ", "nas"),
  R("twkn", "طُرًّا", "turran", of=("النَّاسَ", "mankind", "insanlar"), n=DR("وَهُوَ بِمَعْنَى «جَمِيعًا»", "it means «all together»", "«hep birlikte» anlamındadır")),
  R("twkn", "أَجْمَعِينَا", "ajmain", sign=S_JMSI, g=["jam-mudhakkar-salim"], of=("النَّاسَ", "mankind", "insanlar"), n=DR("تَوْكِيدٌ بَعْدَ تَوْكِيدٍ", "an emphasis after an emphasis", "te'kîdden sonra te'kîd"))])
VV(93, "They roll the heads (of their foes) as sturdy lads roll balls in its level hollow.",
  "(Düşmanlarının) başlarını, iri yarı delikanlıların düz vadi yatağında topları yuvarladığı gibi yuvarlarlar.",
 [V("d5", "يُدَهْدُونَ", "dahda-amr", g=["rubai-babs", "naqis-verbs"], n=N3(CL("ist"), ZW("يُدَحْرِجُونَ رُءُوسَ أَقْرَانِهِمْ", "they roll the heads of their peers", "akranlarının başlarını yuvarlarlar"))),
  R("maf", "الرُّءُوسَ", "ras", g=["jam-taksir"]),
  T("كَمَا", "ma-masdariyya", "part", TB + ["huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ«مَا» حَرْفٌ مَصْدَرِيٌّ، وَهِيَ وَالْفِعْلُ بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ: يُدَهْدُونَ الرُّءُوسَ تَدَهْدِيًا كَتَدَهْدِيَةِ … (الدُّرَّةُ) — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ بَيَّنَهُ الزَّوْزَنِيُّ: «يُدَحْرِجُونَ رُءُوسَ أَقْرَانِهِمْ كَمَا يُدَحْرِجُ الْغِلْمَانُ الْغِلَاظُ الشِّدَادُ الْكُرَاتِ»؛ وَوَجْهُ الشَّبَهِ — الدَّحْرَجَةُ — مَذْكُورٌ فِي الْبَيْتِ.",
    "The kaf is the jarr letter of likening and مَا a masdar particle; with the verb it makes a masdar in jarr by the kaf, the phrase hanging on an omitted adjective of an absolute object: «they roll the heads with a rolling like …» (al-Durra) — a tashbih mursal mufassal that al-Zawzanī makes plain: «they roll their peers' heads as big, strong boys roll balls»; the point, rolling, is named in the verse.",
    "Kâf teşbîh ve cer harfi, «mâ» masdar harfidir; fiille birlikte kâf ile mecrûr masdar olur; câr-mecrûr mahzûf mef'ûl-i mutlakın mahzûf sıfatına müteallik (Dürre) — Zevzenî'nin açıkladığı teşbîh-i mürsel mufassal: «iri, güçlü oğlanların topları yuvarladığı gibi akranlarının başlarını yuvarlarlar»; vech-i şebeh — yuvarlamak — beyitte zikredilmiştir.",
    segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part"))),
  V("dy", "تُدَهْدِي", "dahda-amr", g=["rubai-babs", "naqis-verbs"])],
 [R("fail", "حَزَاوِرَةٌ", "hazawwar-amr", g=["jam-taksir"], n=ZW("الْحَزَوَّرُ: الْغُلَامُ الْغَلِيظُ الشَّدِيدُ، وَالْجَمْعُ الْحَزَاوِرَةُ", "حَزَوَّر is a sturdy, strong lad; the plural is حَزَاوِرَة", "«hazevver»: iri, güçlü oğlan; cem'i «hazâvira»")),
  R("majr", "بِأَبْطَحِهَا", "abtah", j="bi", enc="هَا", n=N3(MT("تُدَهْدِي", "roll", "yuvarlar»a"), ZW("فِي مَكَانٍ مُطْمَئِنٍّ مِنَ الْأَرْضِ", "in a low, level stretch of ground", "yerin çukur, düz bir yerinde"))),
  R("maf", "الْكُرِينَا", "kura-amr", sign=S_MULHAQ_N, g=["jam-mudhakkar-salim"], n=ZW("أَيِ الْكُرَاتِ", "that is, balls", "yani topları"))])
VV(94, "The tribes of Maʿadd know, when the domed tents are pitched in its broad valley, —",
  "Mead kabileleri bilir — kubbeli çadırlar onun geniş vadisinde kurulduğunda —",
 [QAD("وَقَدْ", c="wi"),
  V("m", "عَلِمَ", "alima", n=N3(CL("ist"), NT("وَذُكِّرَ لِأَنَّ الْفَاعِلَ جَمْعُ تَكْسِيرٍ", "it is left masculine because the doer is a broken plural", "fâil cem-i teksîr olduğu için müzekker gelmiştir"))),
  R("fail", "الْقَبَائِلُ", "qabila-tribe", g=["jam-taksir"]),
  PR("مِنْ", "min", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «الْقَبَائِلُ»", "the phrase hangs on an omitted hal of «the tribes»", "câr-mecrûr «kabileler»in mahzûf hâline müteallik")),
  R("majr", "مَعَدٍّ", "maadd-name", pos="propn")],
 [IDHA(plain=True, n=DR("مُتَعَلِّقٌ بِـ«عَلِمَ»", "it hangs on «know»", "«bilir»e müteallik")),
  R("naib", "قُبَبٌ", "qubba", g=["jam-taksir"], n=N3(DR("لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ بَعْدَهُ، وَالْجُمْلَةُ الْمَحْذُوفَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "of an omitted verb that the one after explains; that omitted clause is in the seat of jarr, إِذَا being annexed to it", "sonrakinin açıkladığı mahzûf bir fiilin nâib-i fâili; mahzûf cümle «izâ»nın izâfetiyle mahallen mecrûr"), ZW("الْقُبَبُ وَالْقِبَابُ جَمْعَا قُبَّةٍ", "قُبَب and قِبَاب are both plurals of قُبَّة", "«kubeb» ve «kıbâb», «kubbe»nin iki cem'idir"))),
  R("majr", "بِأَبْطَحِهَا", "abtah", j="bi", enc="هَا", n=MT("بُنِيَ", "pitched", "kuruldu»ya")),
  V("mn", "بُنِينَا", "bana", pas=True, g=["naqis-verbs"], n=N3(ITLAQ, NT("وَالْجُمْلَةُ مُفَسِّرَةٌ لَا مَحَلَّ لَهَا", "the clause explains the omitted one and has no seat", "cümle tefsîriyyedir, mahalli yoktur")))])
VV(95, "that we feed (our guests) when we are able, and destroy (our foes) when we are put to the test;",
  "gücümüz yettiğinde (misafirleri) doyuranlar, sınandığımızda (düşmanları) helâk edenler biz olduğumuzu;",
 [INNA("بِأَنَّا", "anna", enc="نَا", j="bi", n=NT("وَحُذِفَتْ إِحْدَى النُّونَاتِ لِلتَّخْفِيفِ؛ وَ«أَنَّ» وَمَعْمُولَاهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِالْبَاءِ، مُتَعَلِّقَانِ بِـ«عَلِمَ» فِي الْبَيْتِ قَبْلَهُ", "one nun is dropped for ease; أَنَّ with its two terms makes a masdar in jarr by the ba, hanging on «know» in the verse before", "nûnlardan biri hafiflik için düşmüştür; «enne» ve iki ma'mûlü bâ ile mecrûr masdar olur, önceki beyitteki «bilir»e müteallik")),
  R("khba", "الْمُطْعِمُونَ", "mutim-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "hadhf-al-maful"], n=N3(DR("وَمَفْعُولُهُ مَحْذُوفٌ", "its object is left out", "mef'ûlü mahzûftur"), ZW("نُطْعِمُ الضِّيفَانَ إِذَا قَدَرْنَا عَلَيْهِ", "we feed the guests when we are able", "gücümüz yettiğinde misafirleri doyururuz"))),
  IDHA(plain=True, n=MZ("الْمُطْعِمُونَ", "who feed", "doyuranlar»a")),
  V("mna", "قَدَرْنَا", "qadara-able", n=CL("mdf", "إِذَا", "إِذَا", "izâ"))],
 [ANNA_W(),
  R("khba", "الْمُهْلِكُونَ", "muhlik-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "hadhf-al-maful"]),
  IDHA(plain=True, n=MZ("الْمُهْلِكُونَ", "who destroy", "helâk edenler»e")),
  V("mna", "ابْتُلِينَا", "ibtala", pas=True, g=["form-viii-verbs", "naqis-verbs"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), ZW("وَنُهْلِكُ أَعْدَاءَنَا إِذَا اخْتَبَرُوا قِتَالَنَا", "and we destroy our enemies when they put our fighting to the test", "savaşımızı sınadıklarında düşmanlarımızı helâk ederiz")))])
VV(96, "that we withhold whatever we will, and alight wherever we please;",
  "dilediğimizi esirgeyenler, istediğimiz yere konanlar biz olduğumuzu;",
 [ANNA_W(),
  R("khba", "الْمَانِعُونَ", "mani-preventer", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail"], n=DR("وَرِوَايَتُهُ: «وَأَنَّا الْحَاكِمُونَ بِمَا أَرَدْنَا»", "his text reads «and that we judge as we will»", "onun rivayeti «ve ennâ'l-hâkimûne bimâ eradnâ»dır")),
  LIMA("الْمَانِعُونَ", "who withhold", "esirgeyenler»e"),
  V("mna", "أَرَدْنَا", "arada", g=["form-iv-verbs", "hollow-verbs"], n=N3(CL("sila"), NT("وَالْعَائِدُ مَحْذُوفٌ: أَرَدْنَاهُ", "the returning pronoun is left out: «what we will»", "dönen zamir mahzûftur: «dilediğimiz şey»"), ZW("نَمْنَعُ النَّاسَ مَا أَرَدْنَا مَنْعَهُ إِيَّاهُمْ", "we keep from men whatever we wish to keep from them", "insanlardan esirgemek istediğimizi esirgeriz")))],
 [ANNA_W(),
  R("khba", "النَّازِلُونَ", "nazil-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail"]),
  T("بِحَيْثُ", "haythu", "noun", ["huruf-jarr", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«حَيْثُ» ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِالْبَاءِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«النَّازِلُونَ».",
    "The ba is a jarr letter; حَيْثُ is an adverb of place built on damma, in the seat of jarr after the ba; the phrase hangs on «who alight».", "Bâ cer harfi; «hays» damme üzere mebnî mekân zarfı, bâ ile mahallen mecrûr; câr-mecrûr «konanlar»a müteallik.", segs=SG(("بِ", "bi", "prep"), ("حَيْثُ", "haythu", "noun"))),
  T("شِينَا", "shaa", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَنَا " + _FA + "؛ وَأَصْلُهُ «شِئْنَا»، خُفِّفَتْ هَمْزَتُهُ يَاءً؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «حَيْثُ» إِلَيْهَا — وَنَنْزِلُ حَيْثُ شِئْنَا مِنْ بِلَادِ الْعَرَبِ (الزَّوْزَنِيُّ).",
    "A past verb built on sukun because نَا is attached, and نَا is the doer, in the seat of raf'; it is شِئْنَا with its hamza lightened to a ya; the clause is in the seat of jarr, حَيْثُ being annexed to it — «we alight wherever we please in the Arabs' lands» (al-Zawzanī).", "«Nâ» bitiştiği için sükûn üzere mebnî mâzî; «nâ» mahallen merfû fâildir; aslı «şi'nâ»dır, hemzesi yâya hafifletilmiştir; cümle «hays»ın izâfetiyle mahallen mecrûr — «Arap diyarında dilediğimiz yere konarız» (Zevzenî).")])
VV(97, "that we leave alone when we are displeased, and take when we are pleased.",
  "hoşnut olmadığımızda bırakanlar, hoşnut olduğumuzda alanlar biz olduğumuzu.",
 [ANNA_W(),
  R("khba", "التَّارِكُونَ", "tarik", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "hadhf-al-maful"], n=NT("وَمَفْعُولُهُ مَحْذُوفٌ — وَلَيْسَ لِلدُّرَّةِ بَيْتٌ بِهٰذَا اللَّفْظِ، وَإِعْرَابُهُ عَلَى نَظِيرِهِ «وَنَحْنُ التَّارِكُونَ لِمَا سَخِطْنَا»", "its object is left out — al-Durra has no verse in these words; it is parsed like its twin, «we are the ones who leave what displeases us»", "mef'ûlü mahzûftur — Dürre'de bu lafızla bir beyit yoktur; benzeri olan «hoşnut olmadığımızı bırakanlar biziz» gibi i'râb edilir")),
  IDHA(plain=True, n=MZ("التَّارِكُونَ", "who leave", "bırakanlar»a")),
  V("mna", "سَخِطْنَا", "sakhita-amr", n=CL("mdf", "إِذَا", "إِذَا", "izâ"))],
 [ANNA_W(),
  R("khba", "الْآخِذُونَ", "akhidh-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "muqabala"], n=N3(ZW("أَيْ لَا نَقْبَلُ عَطَايَا مَنْ سَخِطْنَا عَلَيْهِ، وَنَقْبَلُ هَدَايَا مَنْ رَضِينَا عَنْهُ", "that is, we do not accept gifts from one we are displeased with, and we accept presents from one we are pleased with", "yani hoşnut olmadığımız kimsenin bağışını kabul etmeyiz, hoşnut olduğumuzun hediyesini kabul ederiz"),
    HADD("مُقَابَلَةٌ: «التَّارِكُونَ إِذَا سَخِطْنَا» يُقَابِلُهُ «الْآخِذُونَ إِذَا رَضِينَا» عَلَى التَّرْتِيبِ", "a muqābala: «who leave when displeased» is answered in order by «who take when pleased»", "mukâbele: «hoşnut olmadığımızda bırakanlar»a sırasıyla «hoşnut olduğumuzda alanlar» karşılık verir"))),
  IDHA(plain=True, n=MZ("الْآخِذُونَ", "who take", "alanlar»a")),
  V("mna", "رَضِينَا", "radiya", g=["naqis-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ"))])
# ---- vv. 98–103 — مَلَأْنَا الْبَرَّ ----
VV(98, "that we protect (our neighbours) when we are obeyed, and set ourselves (against them) when we are disobeyed.",
  "itaat edildiğimizde (komşularımızı) koruyanlar, isyan edildiğimizde (onlara karşı) azmedenler biz olduğumuzu.",
 [ANNA_W(),
  R("khba", "الْعَاصِمُونَ", "asim-protector", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "hadhf-al-maful"], n=N3(NT("وَمَفْعُولُهُ مَحْذُوفٌ — وَلَيْسَ لِلدُّرَّةِ بَيْتٌ بِهٰذَا اللَّفْظِ، وَإِعْرَابُهُ عَلَى نَظِيرِهِ «وَنَحْنُ الْحَاكِمُونَ إِذَا أُطِعْنَا»", "its object is left out — al-Durra has no verse in these words; it is parsed like its twin, «we are the ones who rule when we are obeyed»", "mef'ûlü mahzûftur — Dürre'de bu lafızla bir beyit yoktur; benzeri «itaat edildiğimizde hükmedenler biziz» gibi i'râb edilir"), ZW("وَأَنَّا نَعْصِمُ وَنَمْنَعُ جِيرَانَنَا إِذَا أَطَاعُونَا", "and that we guard and protect our neighbours when they obey us", "bize itaat ettiklerinde komşularımızı korur ve himaye ederiz"))),
  IDHA(plain=True, n=MZ("الْعَاصِمُونَ", "who protect", "koruyanlar»a")),
  V("mna", "أُطِعْنَا", "ataa", pas=True, g=["form-iv-verbs", "hollow-verbs"], n=CL("mdf", "إِذَا", "إِذَا", "izâ"))],
 [ANNA_W(),
  R("khba", "الْعَازِمُونَ", "azim-amr", sign=S_JMSRI2, g=["jam-mudhakkar-salim", "ism-fail", "jinas-mudari-lahiq", "jinas"], n=N3(ZW("وَنَعْزِمُ عَلَيْهِمْ بِالْعُدْوَانِ إِذَا عَصَوْنَا", "and we set ourselves to attack them when they disobey us", "bize isyan ettiklerinde onlara saldırmaya azmederiz"),
    HADD("جِنَاسٌ مُضَارِعٌ بَيْنَ «الْعَاصِمُونَ» وَ«الْعَازِمُونَ»: اخْتَلَفَا فِي حَرْفٍ وَاحِدٍ (الصَّادِ وَالزَّايِ) مُتَقَارِبَيِ الْمَخْرَجِ، وَاتَّفَقَا فِيمَا سِوَاهُ", "a jinās muḍāriʿ between «who protect» and «who set themselves»: they differ in one letter, ṣād and zāy, close in their point of articulation, and agree in all else", "«koruyanlar» ile «azmedenler» arasında muzâri' cinâs: mahreçleri yakın tek bir harfte (sâd ve zâ) ayrılır, gerisinde birleşir"))),
  IDHA(plain=True, n=MZ("الْعَازِمُونَ", "who set themselves", "azmedenler»e")),
  V("mna", "عُصِينَا", "asa", pas=True, g=["naqis-verbs", "tibaq"], n=N3(CL("mdf", "إِذَا", "إِذَا", "izâ"), HADD("طِبَاقٌ بَيْنَ «أُطِعْنَا» وَ«عُصِينَا»: الطَّاعَةُ وَالْمَعْصِيَةُ ضِدَّانِ", "a ṭibāq between «we are obeyed» and «we are disobeyed», which are contraries", "«itaat edildik» ile «isyan edildik» arasında tıbâk: itaat ve isyan zıttır")))])
VV(99, "We drink, when we come down to the water, the clear; and others drink the muddy and the mire.",
  "Suya indiğimizde biz duru olanını içeriz; başkaları ise bulanığını ve çamurunu içer.",
 [V("d", "وَنَشْرَبُ", "shariba", c="wi", doer=NAHNU, g=["kinaya", "aqsam-al-kinaya"], n=N3(CL("ist"),
    (" — وَفِيهِ كِنَايَةٌ بَيَّنَهَا الزَّوْزَنِيُّ: «وَنَأْخُذُ مِنْ كُلِّ شَيْءٍ أَفْضَلَهُ، وَنَدَعُ لِغَيْرِنَا أَرْذَلَهُ؛ يُرِيدُ لَهُمُ السَّادَةُ وَالْقَادَةُ، وَغَيْرُهُمْ أَتْبَاعٌ لَهُمْ»", " — a kināya that al-Zawzanī makes plain: «we take of everything the best and leave to others the worst; he means they are the lords and leaders, and the rest their followers»", " — Zevzenî'nin açıkladığı kinâye: «her şeyin en iyisini alır, en kötüsünü başkalarına bırakırız; efendiler ve önderler onlardır, diğerleri onlara tâbidir demek ister»"))),
  PT("إِنْ", "in-shartiyya", "حَرْفُ شَرْطٍ جَازِمٌ، وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ «نَشْرَبُ»", "the particle of condition that puts verbs in jazm; its answer is left out, shown by «we drink»", "cezmeden şart harfi; cevabı mahzûftur, «içeriz» ona delâlet eder", g=["in-shartiyya"]),
  V("mna", "وَرَدْنَا", "warada", g=["mithal-verbs"], n=NT("وَهُوَ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "it is in the seat of jazm as the verb of the condition", "şart fiili olarak mahallen meczûmdur")),
  R("maf", "الْمَاءَ", "ma"),
  R("maf", "صَفْوًا", "safw-amr", n=N3(NT("لِـ«نَشْرَبُ»، أَيْ نَشْرَبُ الصَّفْوَ", "of «we drink»: we drink the clear", "«içeriz»in mef'ûlü: duru olanı içeriz"), DR("وَرِوَايَتُهُ: «وَأَنَّا الشَّارِبُونَ الْمَاءَ صَفْوًا»، وَ«صَفْوًا» عِنْدَهُ حَالٌ مِنَ الْمَاءِ", "his text reads «and that we drink the water clear», where «clear» is a hal of «the water»", "onun rivayeti «ve ennâ'ş-şâribûne'l-mâe safven»dır; ona göre «safven» sudan hâldir")))],
 [V("d", "وَيَشْرَبُ", "shariba", c="w", n=CL("atf", "نَشْرَبُ", "we drink", "içeriz")),
  R("fail", "غَيْرُنَا", "ghayr", enc="نَا"),
  R("maf", "كَدِرًا", "kadir-amr", g=["tibaq"], n=HADD("طِبَاقٌ بَيْنَ «صَفْوًا» وَ«كَدِرًا»: الصَّفَاءُ وَالْكَدَرُ ضِدَّانِ", "a ṭibāq between «clear» and «muddy», which are contraries", "«duru» ile «bulanık» arasında tıbâk: duruluk ve bulanıklık zıttır")),
  R("atfn", "وَطِينَا", "tin", c="w", of=("كَدِرًا", "the muddy", "bulanık"), n=TANW_ALIF)])
VV(100, "Ho! Carry word from us to the Banū l-Ṭammāḥ and to Duʿmī: how have you found us?",
  "Hey! Bizden Benî Tammâh'a ve Du'mî'ye ulaştır: bizi nasıl buldunuz?",
 [PT("أَلَا", "ala-tanbih", "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ لَا عَمَلَ لَهُ", "a particle that opens the speech and calls attention; it governs nothing", "istiftâh ve tenbîh harfi, ameli yoktur", g=["huruf-tanbih"]),
  V("a", "أَبْلِغْ", "ablagha", doer=ANTA, g=["form-iv-verbs", "mafulayn"], n=CL("ibt")),
  R("maf1", "بَنِي", "banu", mud=True, sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " — by the ya, as it declines like the sound masculine plural; its nun drops in the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"]),
  R("mdf", "الطَّمَّاحِ", "tammah-amr", pos="propn"),
  JP("عَنَّا", "an", "نَا", n=MT("أَبْلِغْ", "carry word", "ulaştır»a"))],
 [R("atfn", "وَدُعْمِيًّا", "dumi-amr", pos="propn", c="w", of=("بَنِي الطَّمَّاحِ", "the Banū l-Ṭammāḥ", "Benî Tammâh")),
  T("فَكَيْفَ", "kayfa", "noun", ["al-istifham"], "الْفَاءُ زَائِدَةٌ لِتَزْيِينِ اللَّفْظِ (الدُّرَّةُ)، وَ«كَيْفَ» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ مُقَدَّمٌ لِـ«وَجَدْتُمُونَا».",
    "The fa is extra, to grace the wording (al-Durra); كَيْفَ is a noun of question built on fatha, in the seat of nasb as the fronted second object of «you have found us».", "Fâ lafzı süslemek için zâiddir (Dürre); «keyfe» fetha üzere mebnî soru ismi, «buldunuz»un öne alınmış ikinci mef'ûlü olarak mahallen mansûb.", segs=SG(("فَ", "fa", "conj"), ("كَيْفَ", "kayfa", "noun"))),
  T("وَجَدْتُمُونَا", "wajada", "verb", ["al-bariz-al-muttasil", "fail", "maful-bihi", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ " + _FA + "، وَالْمِيمُ عَلَامَةُ جَمْعِ الذُّكُورِ حُرِّكَتْ بِالضَّمِّ فَتَوَلَّدَتْ وَاوُ الْإِشْبَاعِ، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ؛ وَجُمْلَةُ «كَيْفَ وَجَدْتُمُونَا» فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ«أَبْلِغْ» (الدُّرَّةُ) — يَقُولُ: سَلْ هٰؤُلَاءِ كَيْفَ وَجَدُونَا؟ شُجْعَانًا أَمْ جُبَنَاءَ؟ (الزَّوْزَنِيُّ).",
    "A past verb built on sukun because the subject pronoun is attached; the ta is the doer, in the seat of raf'; the mim marks the masculine plural and takes a damma, so that a lengthening waw grows from it; نَا is the first object, in the seat of nasb; «how have you found us» is the second object of «carry word», in the seat of nasb (al-Durra) — he says: ask them how they found us — brave or cowards? (al-Zawzanī).",
    "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; tâ mahallen merfû fâildir; mîm müzekker cem' alâmetidir, damme alır, ondan işbâ' vâvı doğar; «nâ» mahallen mansûb birinci mef'ûldür; «bizi nasıl buldunuz» cümlesi «ulaştır»ın ikinci mef'ûlü, mahallen mansûb (Dürre) — der ki: onlara sor, bizi nasıl buldular, yiğit mi korkak mı? (Zevzenî).",
    segs=SG(("وَجَدْتُمُو", "wajada", "verb"), ("نَا", "pron-1p", "pron")))])
VV(101, "When a king would lay disgrace upon men, we refuse to let abasement settle among us.",
  "Bir kral insanlara zillet yüklemek istediğinde, biz aramızda zilletin yerleşmesini reddederiz.",
 [IDHA(),
  MA_Z(),
  R("fail", "الْمَلْكُ", "malik-king", n=N3(NT("وَهُوَ «الْمَلِكُ» سُكِّنَتْ لَامُهُ تَخْفِيفًا", "it is الْمَلِك with its lam made quiescent for lightness", "«el-melik»tir; lâmı hafiflik için sâkin kılınmıştır"), DR("فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ بَعْدَهُ، وَالْجُمْلَةُ الْمَحْذُوفَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "the doer of an omitted verb that the one after explains; that omitted clause is in the seat of jarr, إِذَا being annexed to it", "sonrakinin açıkladığı mahzûf bir fiilin fâili; mahzûf cümle «izâ»nın izâfetiyle mahallen mecrûr"))),
  V("m", "سَامَ", "sama-amr", doer=HUWA("الْمَلِكِ", "the king", "krala"), g=["hollow-verbs", "mafulayn"], n=N3(NT("وَالْجُمْلَةُ مُفَسِّرَةٌ لَا مَحَلَّ لَهَا", "the clause explains the omitted one and has no seat", "cümle tefsîriyyedir, mahalli yoktur"), ZW("السَّوْمُ: أَنْ تُجَشِّمَ إِنْسَانًا مَشَقَّةً وَشَرًّا؛ يُقَالُ: سَامَهُ خَسْفًا، أَيْ حَمَّلَهُ وَكَلَّفَهُ مَا فِيهِ ذُلٌّ", "سَوْم is laying hardship and harm on someone: سَامَهُ خَسْفًا, he loaded him with what brings abasement", "«sevm»: birine meşakkat ve kötülük yüklemek; «sâmehû hasfen»: ona zillet getiren şeyi yükledi"))),
  R("maf1", "النَّاسَ", "nas"),
  R("maf2", "خَسْفًا", "khasf", n=ZW("الْخَسْفُ وَالْخُسْفُ — بِفَتْحِ الْخَاءِ وَضَمِّهَا —: الذُّلُّ", "خَسْف (or خُسْف) is abasement", "«hasf» (ya da «husf»): zillet"))],
 [V("mna", "أَبَيْنَا", "aba", g=["naqis-verbs"], n=CL("jawab")),
  AN(n=NT("وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَفْعُولٍ بِهِ لِـ«أَبَيْنَا»", "أَنْ and the verb make a masdar, the object of «we refuse»", "«en» ile fiil «reddederiz»in mef'ûlü olan bir masdar olur")),
  V(NS("بِـ«أَنْ»", "by أَنْ", "«en» ile"), "نُقِرَّ", "aqarra", doer=NAHNU, g=["form-iv-verbs", "doubled-verbs"]),
  R("maf", "الذُّلَّ", "dhull"),
  JP("فِينَا", "fi", "نَا", n=N3(MT("نُقِرَّ", "let settle", "yerleşmesine izin vermek»e"), ZW("إِذَا أَكْرَهَ الْمَلِكُ النَّاسَ عَلَى مَا فِيهِ ذُلُّهُمْ أَبَيْنَا الِانْقِيَادَ لَهُ", "when the king forces men into what abases them, we refuse to submit to him", "kral insanları zilletlerine yol açan şeye zorladığında ona boyun eğmeyi reddederiz")))])
VV(102, "We have filled the land until it is too narrow for us, and the water of the sea we fill with ships.",
  "Karayı doldurduk, öyle ki bize dar geldi; denizin suyunu da gemilerle doldururuz.",
 [V("mna", "مَلَأْنَا", "malaa", n=CL("ist")),
  R("maf", "الْبَرَّ", "barr-land"),
  PT("حَتَّى", "hatta", "حَرْفُ غَايَةٍ وَجَرٍّ، وَ«أَنْ» مُضْمَرَةٌ بَعْدَهَا، وَهِيَ وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِـ«حَتَّى»، مُتَعَلِّقَانِ بِـ«مَلَأْنَا» (الدُّرَّةُ)؛ وَقِيلَ: حَرْفُ ابْتِدَاءٍ وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ", "a particle of limit and jarr with an أَنْ understood after it, the two making a masdar in jarr by حَتَّى that hangs on «we filled» (al-Durra); some make it a particle that opens a fresh clause", "gâye ve cer harfi; ondan sonra gizli «en» vardır, fiille birlikte «hattâ» ile mecrûr masdar olur, «doldurduk»a müteallik (Dürre); ibtidâ harfi olup sonraki cümlenin müste'nef olduğu da söylenmiştir", g=["ila-hatta-fi-wal-ba-fil-kafiya"]),
  V("m", "ضَاقَ", "daqa", doer=HUWA("الْبَرِّ", "the land", "karaya"), g=["hollow-verbs", "mubalagha-maqbula"], n=HADD("مُبَالَغَةٌ (إِغْرَاقٌ): ادَّعَى أَنَّ الْبَرَّ ضَاقَ عَنْهُمْ، وَهُوَ مُمْكِنٌ عَقْلًا مُمْتَنِعٌ عَادَةً", "a mubālagha (ighrāq): he claims the land grew too narrow for them — possible to reason, impossible in the way of things", "mübalağa (iğrâk): karanın onlara dar geldiğini iddia eder — aklen mümkün, âdeten imkânsız")),
  JP("عَنَّا", "an", "نَا", n=MT("ضَاقَ", "is too narrow", "dar geldi»ye"))],
 [R("mub", "وَمَاءُ", "ma", c="w", mud=True, n=DR("وَرِوَايَتُهُ: «وَظَهْرُ الْبَحْرِ»، وَيَجُوزُ فِيهِ النَّصْبُ مَفْعُولًا لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «نَمْلَؤُهُ»", "his text reads «and the back of the sea»; it may also be in nasb, the object of an omitted verb that «we fill it» explains", "onun rivayeti «ve zahru'l-bahri»dir; «doldururuz» fiilinin açıkladığı mahzûf bir fiilin mef'ûlü olarak mansûb da olabilir")),
  R("mdf", "الْبَحْرِ", "bahr", g=["tibaq"], n=HADD("طِبَاقٌ بَيْنَ «الْبَرَّ» وَ«الْبَحْرِ»", "a ṭibāq between «the land» and «the sea»", "«kara» ile «deniz» arasında tıbâk")),
  V("d", "نَمْلَؤُهُ", "malaa", enc="هُ", doer=NAHNU, n=CL("khb", "مَاءُ", "the water", "su")),
  R("tamyiz", "سَفِينَا", "safin-tf", n=N3(TANW_ALIF, DR("تَمْيِيزٌ", "a tamyiz (specifying with what it is filled)", "temyîz (neyle doldurulduğunu açıklar)"), ZW("عَمَمْنَا الدُّنْيَا بَرًّا وَبَحْرًا، فَضَاقَ الْبَرُّ عَنْ بُيُوتِنَا وَالْبَحْرُ عَنْ سُفُنِنَا", "we have covered the world, land and sea: the land is too narrow for our tents and the sea for our ships", "dünyayı karada ve denizde kapladık: kara çadırlarımıza, deniz gemilerimize dar geldi")))])
VV(103, "When a boy of ours reaches the age of weaning, the tyrants fall down before him prostrate.",
  "Bizden bir çocuk sütten kesilme çağına erdiğinde, zorbalar onun önünde secdeye kapanırlar.",
 [IDHA(),
  V("m", "بَلَغَ", "balagha", n=CL("mdf", "إِذَا", "إِذَا", "izâ")),
  R("maf", "الْفِطَامَ", "lb-fitam", n=ZW("إِذَا بَلَغَ صِبْيَانُنَا وَقْتَ الْفِطَامِ", "when our boys reach the time of weaning", "çocuklarımız sütten kesilme vaktine erdiğinde")),
  JP("لَنَا", "li", "نَا", n=DR("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «صَبِيٌّ»: كَانَ صِفَةً لَهُ فَلَمَّا تَقَدَّمَ صَارَ حَالًا", "the phrase hangs on an omitted hal of «a boy»: it was his adjective, and fronted it becomes a hal", "câr-mecrûr «çocuk»un mahzûf hâline müteallik: sıfatı idi, öne geçince hâl oldu")),
  R("fail", "صَبِيٌّ", "sabi-boy")],
 [V("d", "تَخِرُّ", "kharra", g=["doubled-verbs", "mubalagha-maqbula"], n=N3(CL("jawab"), HADD("مُبَالَغَةٌ (إِغْرَاقٌ): ادَّعَى سُجُودَ الْجَبَابِرَةِ لِصَبِيِّهِمْ عِنْدَ فِطَامِهِ، وَهُوَ مُمْكِنٌ عَقْلًا مُمْتَنِعٌ عَادَةً", "a mubālagha (ighrāq): he claims the tyrants bow down to their boy at his weaning — possible to reason, impossible in the way of things", "mübalağa (iğrâk): zorbaların çocuklarına sütten kesildiğinde secde ettiğini iddia eder — aklen mümkün, âdeten imkânsız"))),
  JP("لَهُ", "li", "هُ", n=MT("تَخِرُّ", "fall down", "kapanırlar»a")),
  R("fail", "الْجَبَابِرُ", "jabbar", g=["jam-taksir"], n=ZW("سَجَدَتْ لَهُمُ الْجَبَابِرَةُ مِنْ غَيْرِنَا", "the tyrants of other peoples bow down to them", "başka kavimlerin zorbaları onlara secde eder")),
  R("hal", "سَاجِدِينَا", "sajid", sign=S_JMSI, g=["jam-mudhakkar-salim", "ism-fail"], n=N3(ITLAQ, NT("مِنَ «الْجَبَابِرُ»", "of «the tyrants»", "«zorbalar»ın hâli")))])
# ==== TAIL (lexicon, manifest, writing) — new verses go ABOVE this line ==================================================
POEM_END = 103
PLAN = [(1, 8), (9, 15), (16, 22), (23, 29), (30, 36), (37, 43), (44, 50), (51, 57), (58, 64), (65, 71), (72, 78), (79, 85), (86, 91), (92, 97), (98, 103)]
TITLES_ALL = [
 {"ar": "خَبَرُ عَمْرِو بْنِ كُلْثُومٍ", "en": "ʿAmr ibn Kulthūm's Story", "tr": "Amr b. Külsûm'un Haberi"},
 {"ar": "الصَّبُوحُ", "en": "The Morning Draught", "tr": "Sabah Şarabı"},
 {"ar": "قِفِي قَبْلَ التَّفَرُّقِ", "en": "Stay Before We Part", "tr": "Ayrılmadan Önce Dur"},
 {"ar": "الْوَجْدُ وَالْحُمُولُ", "en": "Longing, and the Departing Litters", "tr": "Hasret ve Göç Eden Hevdeçler"},
 {"ar": "أَبَا هِنْدٍ", "en": "Abū Hind, Do Not Hasten", "tr": "Ebû Hind, Acele Etme"},
 {"ar": "رَحَى الْحَرْبِ وَقِرَى الْأَضْيَافِ", "en": "The Millstone of War, and the Guests' Fare", "tr": "Savaşın Değirmeni ve Misafirlerin Ziyafeti"},
 {"ar": "مَجْدٌ مَوْرُوثٌ", "en": "Glory Inherited", "tr": "Mirasla Gelen Şeref"},
 {"ar": "يَوْمُ الْهَوْلِ", "en": "The Day of Terror", "tr": "Dehşet Günü"},
 {"ar": "إِلَى عَمْرِو بْنِ هِنْدٍ", "en": "To ʿAmr ibn Hind", "tr": "Amr b. Hind'e"},
 {"ar": "الْقَنَاةُ الْعَصِيَّةُ، وَالْآبَاءُ", "en": "The Unbending Spear, and the Fathers", "tr": "Eğilmeyen Mızrak ve Atalar"},
 {"ar": "نَحْنُ", "en": "We", "tr": "Biz"},
 {"ar": "الْمَيْمَنَةُ وَالْمَيْسَرَةُ", "en": "The Right Wing and the Left", "tr": "Sağ Kanat ve Sol Kanat"},
 {"ar": "الدُّرُوعُ وَالْجِيَادُ", "en": "Mail and Steeds", "tr": "Zırhlar ve Atlar"},
 {"ar": "الظَّعَائِنُ", "en": "The Women of the Litters", "tr": "Hevdeçteki Kadınlar"},
 {"ar": "قَدْ عَلِمَ الْقَبَائِلُ", "en": "The Tribes Know", "tr": "Kabileler Bilir"},
 {"ar": "مَلَأْنَا الْبَرَّ", "en": "We Filled the Land", "tr": "Karayı Doldurduk"},
]
CHAPS, VNUMS = [CH[1]], []
for _a, _b in PLAN:
    if not all(n in VERSES for n in range(_a, _b + 1)): break
    _S = [VERSES[n] for n in range(_a, _b + 1)]
    for _i, _s in enumerate(_S, 1): _s["id"] = "s%d" % _i
    CHAPS.append(_S); VNUMS.append((_a, _b))
DONE_TO = VNUMS[-1][1] if VNUMS else 0
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

# ---- the lexicon: every shelf key by lemma identity; the entries in NEW_GLOSS are new (all prefixed «lb-») ------------
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
# ---- the lexicon: shelf (and staged sister) keys by lemma identity; NEW_GLOSS holds the new keys (all suffixed «-amr») ----
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
# ---- ch1 (the khabar) ----
TAILOR.update({
 "amr-name": ("ʿAmr — a man's name, written with a silent waw: here ʿAmr ibn Kulthūm the poet, and ʿAmr ibn Hind, king of al-Ḥīra", "Amr — erkek adı, okunmayan bir vâv ile yazılır: burada şair Amr b. Külsûm ve Hîre kralı Amr b. Hind"),
 "hind": ("Hind — a woman's name: here the mother of ʿAmr ibn Hind, king of al-Ḥīra, who is named after her", "Hind — kadın adı: burada Hîre kralı Amr b. Hind'in annesi; oğlu onun adıyla anılır"),
 "layla-alam": ("Laylā — a woman's name: here Laylā bint Muhalhil, the mother of ʿAmr ibn Kulthūm", "Leylâ — kadın adı: burada Amr b. Külsûm'un annesi Leylâ bint Mühelhil"),
 "kulthum": ("Kulthūm — a man's name: Kulthūm ibn Mālik of Taghlib, the father of the poet ʿAmr", "Külsûm — erkek adı: Tağlib'den Külsûm b. Mâlik, şair Amr'ın babası"),
 "turfa": ("a rare and choice thing; pl. طُرَف: dainties, the choice things brought in after a meal", "nadide ve seçkin şey; ç. طُرَف: yemekten sonra getirilen nadide yiyecekler"),
 "riwaq": ("a canopy, a pavilion; the great tent of a king (pl. أَرْوِقَة)", "çardak, otağ; hükümdarın büyük çadırı (ç. أَرْوِقَة)"),
})
NEW_GLOSS.update({
 "taghlib-amr": P("تَغْلِب", "Taghlib — the tribe of Taghlib ibn Wāʾil, ʿAmr ibn Kulthūm's people; a diptote (a proper name on the pattern of a verb)", "Tağlib — Tağlib b. Vâil kabilesi, Amr b. Külsûm'un kavmi; gayr-i munsarif (fiil veznindeki özel isim)"),
 "nahha-amr": VB("نَحَّى", "ن ح ي", "to put aside, to send out of the way (Form II)", "bir kenara koymak, ortadan uzaklaştırmak (tef'îl)", "II"),
 "istakhdama-amr": VB("اِسْتَخْدَمَ", "خ د م", "to take into service, to make (someone) serve (Form X)", "hizmete almak, birine hizmet ettirmek (istif'âl)", "X"),
 "nawala-amr": VB("نَاوَلَ", "ن و ل", "to hand (a thing) to someone (Form III; two objects)", "(bir şeyi) birine uzatmak, vermek (müfâale; iki mef'ûl alır)", "III"),
 "tabaq-amr": N("طَبَق", "ط ب ق", "a dish, a tray (pl. أَطْبَاق)", "tabak, sini (ç. أَطْبَاق)", "أَطْبَاق"),
 "alahha-amr": VB("أَلَحَّ", "ل ح ح", "to press, to insist (Form IV, doubled; with عَلَى)", "ısrar etmek, üstelemek (if'âl, muzaaf; عَلَى ile)", "IV"),
 "intahaba-amr": VB("اِنْتَهَبَ", "ن ه ب", "to plunder, to carry off as spoil (Form VIII)", "yağmalamak, ganimet olarak alıp götürmek (ifti'âl)", "VIII"),
 "najiba-amr": N("نَجِيبَة", "ن ج ب", "a thoroughbred she-camel, a noble swift camel (pl. نَجَائِب)", "soylu, hızlı dişi deve (ç. نَجَائِب)", "نَجَائِب"),
 "jazira-amr": P("الْجَزِيرَة", "al-Jazīra — the upper land between the Tigris and the Euphrates, the country of Taghlib", "el-Cezîre — Dicle ile Fırat arasındaki yukarı ülke, Tağlib'in yurdu"),
})
NEW_VERBS.update({
 "nahha-amr": _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "نَحَّ", "نَحّ", "i", "نَحّ", "تَنْحِيَة", "مُنَحٍّ (الْمُنَحِّي)", maful="مُنَحًّى", pmz="نُحِّيَ", pmd="يُنَحَّى"),
 "istakhdama-amr": F10("اِسْتَخْدَم", "سْتَخْدِم", "اِسْتِخْدَام", "مُسْتَخْدِم"),
 "nawala-amr": F3("نَاوَل", "نَاوِل", "مُنَاوَلَة", "مُنَاوِل", "مُنَاوَل", "نُووِلَ", "يُنَاوَلُ"),
 "alahha-amr": F4D("ل", "ح", "إِلْحَاح", "مُلِحّ", "مُضَاعَفٌ: يُلِحُّ — لَمْ يُلِحَّ."),
 "intahaba-amr": F8("اِنْتَهَب", "نْتَهِب", "اِنْتِهَاب", "مُنْتَهِب"),
})
FLAGS.append((0, "ضَبْطُ «الطُّرَفِ» فِي الْخَبَرِ (جَمْعُ طُرْفَةٍ: مَا يُسْتَطْرَفُ مِنَ الطَّعَامِ)؛ الْمَطْبُوعُ غَيْرُ مَشْكُولٍ", "the vowelling of «الطُّرَفِ» in the khabar (pl. of طُرْفَة, choice dainties); the edition leaves it bare", "haberdeki «الطُّرَفِ» kelimesinin harekesi (طُرْفَة'nin cem'i, nadide yiyecekler); baskı harekesizdir"))
# ---- ch2 (vv. 1–8) ----
TAILOR.update({
 "habba-blow": ("to blow (of wind); to rouse oneself, to wake (هَبَّ مِنْ نَوْمِهِ, al-Zawzanī) — هَبَّ يَهُبُّ", "esmek (rüzgâr); uykudan uyanmak (هَبَّ مِنْ نَوْمِهِ, Zevzenî) — هَبَّ يَهُبُّ"),
 "muqaddar": ("decreed, apportioned; estimated (ism mafʿūl of قَدَّرَ)", "takdir edilmiş, biçilmiş (قَدَّرَ'den ism-i mef'ûl)"),
 "maniyya": ("death; the decree of death (pl. مَنَايَا)", "ölüm; ölümün takdiri (ç. مَنَايَا)"),
})
NEW_GLOSS.update({
 "sahn-amr": N("صَحْن", "ص ح ن", "a great drinking-bowl (pl. صُحُون)", "büyük içki kadehi (ç. صُحُون)", "صُحُون"),
 "andarin-amr": P("الْأَنْدَرِين", "al-Andarīn (al-Andarūn) — villages in Syria, famed for their wine", "Enderîn (Enderûn) — Şam'da şarabıyla meşhur köyler"),
 "mushashaa-amr": N("مُشَعْشَع", "ش ع ش ع", "(a drink) mixed with water, thinned (ism maf'ul of شَعْشَعَ)", "suyla karıştırılmış, inceltilmiş (içki) (شَعْشَعَ'den ism-i mef'ûl)"),
 "huss-amr": N("حُصّ", "ح ص ص", "wars, a plant with a red blossom like saffron", "vers, safrana benzeyen kırmızı çiçekli bitki"),
 "khalata-amr": VB("خَالَطَ", "خ ل ط", "to mingle with, to mix with (Form III)", "karışmak, birbirine karışmak (müfâale)", "III"),
 "sakhiya-amr": VB("سَخِيَ", "س خ و", "to be open-handed, generous (سَخِيَ يَسْخَى; also سَخُوَ and سَخَا يَسْخُو — al-Zawzanī)", "cömert olmak (سَخِيَ يَسْخَى; ayrıca سَخُوَ ve سَخَا يَسْخُو — Zevzenî)"),
 "lahiz-amr": N("لَحِز", "ل ح ز", "narrow-chested, mean-spirited", "göğsü dar, hasis"),
 "shahih-amr": N("شَحِيح", "ش ح ح", "grasping, miserly — avarice joined to greed (pl. أَشِحَّة، أَشِحَّاء، شِحَاح)", "hırslı cimri — hırsla birlikte cimrilik (ç. أَشِحَّة، أَشِحَّاء، شِحَاح)", "أَشِحَّاء"),
 "amarra-amr": VB("أَمَرَّ", "م ر ر", "to make pass, to pass round (Form IV, doubled); أُمِرَّتْ عَلَيْهِ: it was passed round to him", "geçirmek, dolaştırmak (if'âl, muzaaf); أُمِرَّتْ عَلَيْهِ: ona sunulup dolaştırıldı", "IV"),
 "muhin-amr": N("مُهِين", "ه و ن", "holding cheap, scorning (ism fa'il of أَهَانَ)", "hor gören, değersiz sayan (أَهَانَ'dan ism-i fâil)"),
 "sabana-amr": VB("صَبَنَ", "ص ب ن", "to turn (a thing) away from someone (صَبَنَ يَصْبِنُ صَبْنًا)", "(bir şeyi) birinden çevirmek (صَبَنَ يَصْبِنُ صَبْنًا)"),
 "qasirin-amr": P("قَاصِرِين", "Qāṣirīn — a town of Syria named with Damascus; a diptote", "Kâsırîn — Dımaşk ile anılan bir Şam beldesi; gayr-i munsarif"),
})
NEW_VERBS.update({
 "khalata-amr": F3("خَالَط", "خَالِط", "مُخَالَطَة", "مُخَالِط", "مُخَالَط", "خُولِطَ", "يُخَالَطُ"),
 "sakhiya-amr": _sg.naqis1("samia", "نَاقِصٌ يَائِيٌّ", "y", "سَخِ", "سْخ", "a", "اِسْخ", "سَخَاء", "سَخِيّ", note="نَاقِصٌ: سَخِيَ يَسْخَى — لَمْ يَسْخَ؛ وَفِيهِ لُغَتَانِ أُخْرَيَانِ: سَخُوَ يَسْخُو، وَسَخَا يَسْخُو (الزَّوْزَنِيُّ)."),
 "amarra-amr": F4D("م", "ر", "إِمْرَار", "مُمِرّ", "مُضَاعَفٌ: يُمِرُّ — لَمْ يُمِرَّ؛ وَالْمَجْهُولُ أُمِرَّ يُمَرُّ.", maful="مُمَرّ", pmz="أُمِرَّ", pmd="يُمَرُّ"),
 "sabana-amr": _sg1("daraba", "صَبَن", "صْبِن", "اِصْبِن", "صَبْن", "صَابِن", "مَصْبُون", "صُبِنَ", "يُصْبَنُ"),
})
DIV += [
 (2, "الْبَيْتُ ٢ «الْمَاُء» ← «الْمَاءُ» (الضَّمَّةُ عَلَى الْهَمْزَةِ لَا عَلَى الْأَلِفِ)، وَالشَّاهِدُ الْإِعْرَابُ عِنْدَ الدُّرَّةِ (فَاعِلٌ)", "v. 2 «الْمَاُء» → «الْمَاءُ» (the damma belongs on the hamza, not the alif) — witness: al-Durra's iʿrāb (a doer, in raf')", "2. beyit «الْمَاُء» → «الْمَاءُ» (damme elifin değil hemzenin üzerindedir) — şahit: Dürre'nin i'râbı (fâil)"),
 (7, "الْبَيْتُ ٧ «وِكَأسٍ» ← «وَكَأْسٍ» بِفَتْحِ الْوَاوِ، وَالشَّاهِدُ الدُّرَّةُ: «الْوَاوُ وَاوُ رُبَّ»", "v. 7 «وِكَأسٍ» → «وَكَأْسٍ» with fatha on the waw — witness: al-Durra, «the waw is the waw of رُبَّ»", "7. beyit «وِكَأسٍ» → «وَكَأْسٍ», vâv fethalı — şahit: Dürre, «vâv rubbe vâvıdır»"),
]
# ---- ch3 (vv. 9–15) ----
TAILOR.update({
 "mawla": ("a mawlā: a client, a freedman tied to a tribe; also a kinsman, a cousin (pl. مَوَالٍ — in v. 11 «your cousins», al-Zawzanī)", "mevlâ: bir kabileye bağlı azatlı, himaye altındaki kişi; akraba, amca oğlu (ç. مَوَالٍ — 11. beyitte «amca oğulların», Zevzenî)"),
 "aqarra": ("to affirm, to acknowledge; أَقَرَّ عَيْنَهُ: to gladden him, to give him what he longs for (Form IV, doubled)", "ikrar etmek, kabul etmek; أَقَرَّ عَيْنَهُ: gözünü aydın etmek, dileğine kavuşturmak (if'âl, muzaaf)"),
 "qaraa": ("to read, to recite; of a she-camel, لَمْ تَقْرَأْ جَنِينًا: her womb has never held a young one (al-Zawzanī)", "okumak; dişi deve için لَمْ تَقْرَأْ جَنِينًا: rahmi hiç yavru taşımadı (Zevzenî)"),
 "bikr": ("the first of its kind; a virgin; of a she-camel, one that has carried a single young (al-Zawzanī)", "türünün ilki; bakire; dişi deve için bir kez gebe kalmış olan (Zevzenî)"),
 "rahn": ("a pledge, a security; what is held fast and bound to a thing", "rehin, teminat; bir şeye sıkıca bağlı tutulan"),
})
NEW_GLOSS.update({
 "tafarruq-amr": N("تَفَرُّق", "ف ر ق", "parting, going separate ways (masdar of تَفَرَّقَ)", "ayrılık, dağılıp gitme (تَفَرَّقَ'nin masdarı)"),
 "washk-amr": N("وَشْك", "و ش ك", "swiftness, haste (al-Zawzanī); وَشِيك: swift", "çabukluk, acele (Zevzenî); وَشِيك: çabuk"),
 "kariha-amr": N("كَرِيهَة", "ك ر ه", "a name of war, «the hateful one» (pl. كَرَائِه) — souls hate it (al-Zawzanī)", "savaşın adlarından «çirkin olan» (ç. كَرَائِه) — nefisler ondan hoşlanmaz (Zevzenî)", "كَرَائِه"),
 "khala-amr": N("خَلَاء", "خ ل و", "an empty place; privacy, being alone with someone", "boş yer; kimsenin bulunmadığı an, baş başa kalma"),
 "kashih-amr": N("كَاشِح", "ك ش ح", "one who nurses a hidden enmity (in his كَشْح, his flank), or turns his flank away — a foe", "düşmanlığını böğründe (كَشْح) gizleyen yahut böğrünü dönüp yüz çeviren — düşman"),
 "aytal-amr": N("عَيْطَل", "ع ط ل", "a long-necked she-camel", "uzun boyunlu dişi deve"),
 "adma-amr": N("أَدْمَاء", "أ د م", "(of a she-camel) white (fem. of آدَم; أُدْمَة in camels is whiteness — al-Zawzanī); a diptote", "(dişi deve için) beyaz (آدَم'ın müennesi; develerde «üdme» beyazlıktır — Zevzenî); gayr-i munsarif", pos="adj"),
 "hijan-amr": N("هِجَان", "ه ج ن", "pure white; the same for one, two and many (said of camels, men and others)", "halis beyaz; tekil, ikil ve çoğulda aynıdır (deve, insan vb. için)", pos="adj"),
 "aj-amr": N("عَاج", "ع و ج", "ivory", "fildişi"),
 "hasan-amr": N("حَصَان", "ح ص ن", "chaste, guarded, kept from any who would touch (fem.)", "iffetli, korunmuş, dokunmak isteyenden uzak tutulmuş (müennes)", pos="adj"),
 "lamis-amr": N("لَامِس", "ل م س", "one who touches (ism fa'il of لَمَسَ)", "dokunan (لَمَسَ'den ism-i fâil)"),
})
DIV += [
 (9, "الْبَيْتُ ٩ «الْيَقِينَا» فِي حَشْوِ الْبَيْتِ ← «الْيَقِينَ»، وَالشَّاهِدُ الْوَزْنُ (لَا يَسْتَقِيمُ الْوَافِرُ بِالْمَدِّ) وَنَصُّ الدُّرَّةِ «نُخَبِّرْكِ الْيَقِينَ»", "v. 9 «الْيَقِينَا» inside the verse → «الْيَقِينَ» — witnesses: the metre (al-wāfir does not stand with the long vowel) and al-Durra's text «نخبرك اليقين»", "9. beyit, beytin ortasındaki «الْيَقِينَا» → «الْيَقِينَ» — şahitler: vezin (vâfir uzun hece ile yürümez) ve Dürre'nin metni «نخبرك اليقين»"),
 (15, "الْبَيْتُ ١٥ «أكُفِ» ← «أَكُفِّ» بِالتَّشْدِيدِ، وَالشَّاهِدُ الْوَزْنُ", "v. 15 «أكُفِ» → «أَكُفِّ» with the shadda — witness: the metre", "15. beyit «أكُفِ» → şeddeli «أَكُفِّ» — şahit: vezin"),
]
# ---- ch4 (vv. 16–22) ----
TAILOR.update({
 "matn": ("the back, the flank: مَتْنَانِ, the two flanks on either side of the spine (pl. مُتُون); also the surface, the text", "sırt, yan: مَتْنَانِ, omurganın iki yanı (ç. مُتُون); ayrıca bir şeyin yüzü, metin"),
 "waliya": ("to be next to, to follow closely (وَلِيَ يَلِي — al-Zawzanī: الْوَلْيُ الْقُرْبُ); to take charge of", "bitişik olmak, hemen ardından gelmek (وَلِيَ يَلِي — Zevzenî: «vely» yakınlıktır); bir işi üstlenmek"),
 "lb-sariya": ("a column, a pillar (pl. سَوَارٍ — al-Zawzanī: الْأُسْطُوَانَةُ); also a cloud that comes and rains by night", "sütun, direk (ç. سَوَارٍ — Zevzenî: «ustuvâne»); ayrıca gece gelip yağan bulut"),
 "aarada": ("to turn away (عَنْ); and, rarely, to appear, to come into view: عَرَضْتُهُ فَأَعْرَضَ (al-Zawzanī) (Form IV)", "yüz çevirmek (عَنْ); nâdiren görünmek, ortaya çıkmak: عَرَضْتُهُ فَأَعْرَضَ (Zevzenî) (if'âl)"),
 "asil": ("the late afternoon, the evening (pl. أُصُل، آصَال)", "ikindiden sonrası, akşamüstü (ç. أُصُل، آصَال)"),
})
NEW_GLOSS.update({
 "ladn-amr": N("لَدْن", "ل د ن", "soft, supple (pl. لُدْن; fem. لَدْنَة)", "yumuşak, esnek (ç. لُدْن; müennesi لَدْنَة)", "لُدْن", pos="adj"),
 "samaqa-amr": VB("سَمَقَ", "س م ق", "to rise tall, to grow high (سَمَقَ يَسْمُقُ سُمُوقًا)", "uzayıp yükselmek, boy atmak (سَمَقَ يَسْمُقُ سُمُوقًا)"),
 "radifa-amr": N("رَادِفَة", "ر د ف", "the end of the buttock (الرَّادِفَتَانِ, also الرَّانِفَتَانِ; pl. رَوَادِف)", "kaba etin ucu (الرَّادِفَتَانِ, ayrıca الرَّانِفَتَانِ; ç. رَوَادِف)", "رَوَادِف"),
 "makama-amr": N("مَأْكَمَة", "أ ك م", "the top of the hip (also مَأْكِمَة; pl. مَآكِم)", "kalçanın başı (ayrıca مَأْكِمَة; ç. مَآكِم)", "مَآكِم"),
 "janna-amr": VB("جَنَّ", "ج ن ن", "to cover, to hide (جَنَّ يَجُنُّ); passive جُنَّ: to be driven mad, to go mad (جُنُون)", "örtmek, gizlemek (جَنَّ يَجُنُّ); meçhulü جُنَّ: aklını yitirmek, delirmek (جُنُون)"),
 "junun-amr": N("جُنُون", "ج ن ن", "madness (masdar of جُنَّ)", "delilik (جُنَّ'nin masdarı)"),
 "balant-amr": N("بَلَنْط", "ب ل ن ط", "ivory (al-Zawzanī)", "fildişi (Zevzenî)"),
 "rukham-amr": N("رُخَام", "ر خ م", "marble", "mermer"),
 "ranna-amr": VB("رَنَّ", "ر ن ن", "to ring, to give out a sound (رَنَّ يَرِنُّ رَنِينًا)", "çınlamak, ses vermek (رَنَّ يَرِنُّ رَنِينًا)"),
 "khushash-amr": N("خُشَاش", "خ ش ش", "the jingle of ornaments (al-Zawzanī paraphrases «خُشَاشُ حَلْيِهِمَا» as «their ornaments, their anklets»)", "süslerin şıngırtısı (Zevzenî «خُشَاشُ حَلْيِهِمَا»yı «süsleri, yani halhalları» diye açıklar)"),
 "haly-amr": N("حَلْي", "ح ل ي", "an ornament, jewellery (pl. حُلِيّ)", "süs, ziynet (ç. حُلِيّ)", "حُلِيّ"),
 "ranin-amr": N("رَنِين", "ر ن ن", "a ringing sound (masdar of رَنَّ)", "çınlama sesi (رَنَّ'nin masdarı)"),
 "wajada-amr": VB("وَجَدَ", "و ج د", "to grieve (وَجَدَ يَجِدُ وَجْدًا — al-Zawzanī)", "kederlenmek (وَجَدَ يَجِدُ وَجْدًا — Zevzenî)"),
 "wajd-amr": N("وَجْد", "و ج د", "grief (masdar of وَجَدَ)", "keder, hüzün (وَجَدَ'nin masdarı)"),
 "saqb-amr": N("سَقْب", "س ق ب", "a camel's male young, a new-born calf (pl. أَسْقُب، سِقَاب) — among camels like a boy among people (al-Sīrāfī in al-Zawzanī)", "devenin erkek yavrusu (ç. أَسْقُب، سِقَاب) — develerde, insanlardaki erkek çocuk gibi (Zevzenî'de Sîrâfî'den)", "سِقَاب"),
 "hanin-amr": N("حَنِين", "ح ن ن", "a moaning, yearning cry — the voice of one in pain (al-Zawzanī)", "inleme, özlem sesi — acı çekenin sesi (Zevzenî)"),
 "shamta-amr": N("شَمْطَاء", "ش م ط", "grey-haired (fem. of أَشْمَط; شَمَط: whiteness of the hair); a diptote", "ak saçlı (أَشْمَط'ın müennesi; şemat: saçın ağarması); gayr-i munsarif", pos="adj"),
 "shaqan-amr": N("شَقًا", "ش ق و", "ill-fortune, misery (= شَقَاء)", "bahtsızlık, sefalet (= شَقَاء)"),
 "siba-amr": N("صِبًا", "ص ب و", "youthful love, the passion of youth (al-Zawzanī: الْعِشْقُ وَالْهَوَى)", "gençlik sevdası (Zevzenî: aşk ve sevda)"),
 "humul-amr": N("حُمُول", "ح م ل", "loaded camels, the camels that carry the litters (al-Zawzanī: جَمْعُ حَامِلٍ)", "yüklü develer, hevdeçleri taşıyan develer (Zevzenî: «hâmil»in cem'i)"),
 "hada-amr": VB("حَدَا", "ح د و", "to drive camels on with song (حَدَا يَحْدُو حُدَاءً)", "develeri türkü söyleyerek sürmek (حَدَا يَحْدُو حُدَاءً)"),
 "yamama-amr": P("الْيَمَامَة", "al-Yamāma — the region of central Arabia (the villages of al-Yamāma, al-Zawzanī)", "Yemâme — orta Arabistan'da bir bölge (Zevzenî: Yemâme köyleri)"),
 "ishmakharra-amr": VB("اِشْمَخَرَّ", "ش م خ ر", "to rise high, to tower (a quadriliteral on اِفْعَلَلَّ)", "yükselmek, yücelmek (اِفْعَلَلَّ vezninde rubâî)"),
 "muslit-amr": N("مُصْلِت", "ص ل ت", "one who draws (a sword) (ism fa'il of أَصْلَتَ)", "(kılıç) sıyıran (أَصْلَتَ'ten ism-i fâil)"),
})
NEW_VERBS.update({
 "samaqa-amr": _sg1("nasara", "سَمَق", "سْمُق", "اُسْمُق", "سُمُوق", "سَامِق"),
 "janna-amr": DBL_N("ج", "ن", "جَنّ", "جَانّ", maful="مَجْنُون", pmz="جُنَّ", pmd="يُجَنُّ", note="مُضَاعَفٌ: جَنَّهُ يَجُنُّهُ: سَتَرَهُ؛ وَجُنَّ الرَّجُلُ — بِالْمَجْهُولِ — جُنُونًا فَهُوَ مَجْنُونٌ."),
 "ranna-amr": DBL_D("ر", "ن", "رَنِين", "رَانّ"),
 "wajada-amr": CLONE("wajada", "وَجَدَ", [], note="مِثَالٌ وَاوِيٌّ: وَجَدَ يَجِدُ — تُحْذَفُ فَاؤُهُ فِي الْمُضَارِعِ؛ وَمَصْدَرُهُ بِمَعْنَى الْحُزْنِ «وَجْدٌ» (الزَّوْزَنِيُّ)."),
 "hada-amr": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "حَدَ", "حْد", "u", "اُحْد", "حُدَاء", "حَادٍ", "مَحْدُوّ", "حُدِيَ", "يُحْدَى"),
 "ishmakharra-amr": CLONE("isbakarra", "اِسْبَكَرَّ", [("س", "ش"), ("ب", "م"), ("ك", "خ")]),
})
NEW_VERBS["wajada-amr"]["masdar"] = "وَجْد"
NEW_VERBS["ishmakharra-amr"].update({k: find_verb("isbakarra", "اِسْبَكَرَّ")[k] for k in ("bab", "wazn")})
DIV += [(20, "الْبَيْتُ ٢٠ «إَلَّا» ← «إِلَّا»، وَالشَّاهِدُ الدُّرَّةُ (حَرْفُ حَصْرٍ)", "v. 20 «إَلَّا» → «إِلَّا» — witness: al-Durra (the particle of restriction)", "20. beyit «إَلَّا» → «إِلَّا» — şahit: Dürre (hasr harfi)")]
# ---- ch5 (vv. 23–29) ----
TAILOR.update({
 "asdara": ("to bring back (from the water); to issue, to send out (Form IV)", "(sudan) geri getirmek; çıkarmak, göndermek (if'âl)"),
 "awrada": ("to bring (the herds) down to the water; to bring in, to adduce (Form IV)", "(sürüyü) suya indirmek; getirmek, zikretmek (if'âl)"),
 "nafa": ("to drive away, to banish; to deny, to negate (نَفَى يَنْفِي)", "sürüp uzaklaştırmak; inkâr etmek, nefyetmek (نَفَى يَنْفِي)"),
 "inan": ("a rein (pl. أَعِنَّة)", "dizgin (ç. أَعِنَّة)"),
 "hayy-tribe": ("a tribe, a tribal encampment (pl. أَحْيَاء)", "kabile, kabile obası (ç. أَحْيَاء)"),
})
NEW_GLOSS.update({
 "agharr-amr": N("أَغَرّ", "غ ر ر", "blazed, having a white blaze on the forehead (of a horse); hence famous, renowned (pl. غُرّ — al-Zawzanī)", "alnı akıtmalı (at); buradan meşhur, ünlü (ç. غُرّ — Zevzenî)", "غُرّ", pos="adj"),
 "dana-amr": VB("دَانَ", "د ي ن", "to submit, to obey (دَانَ يَدِينُ)", "boyun eğmek, itaat etmek (دَانَ يَدِينُ)"),
 "tawwaja-amr": VB("تَوَّجَ", "ت و ج", "to crown (Form II)", "taç giydirmek (tef'îl)", "II"),
 "muhjar-amr": N("مُحْجَر", "ح ج ر", "one driven to seek refuge (ism maf'ul of أَحْجَرَ: أَلْجَأَ — al-Zawzanī)", "sığınmaya muhtaç bırakılmış (أَحْجَرَ'den ism-i mef'ûl: sığınmaya mecbur etti — Zevzenî)"),
 "akif-amr": N("عَاكِف", "ع ك ف", "staying, keeping in one place (ism fa'il of عَكَفَ)", "bir yerde duran, kalan (عَكَفَ'ten ism-i fâil)"),
 "muqallad-amr": N("مُقَلَّد", "ق ل د", "hung with (as a necklace), with (the reins) hung on its neck (ism maf'ul of قَلَّدَ)", "boynuna (gerdanlık gibi) takılmış (قَلَّدَ'den ism-i mef'ûl)"),
 "safin-amr": N("صَافِن", "ص ف ن", "(of a horse) standing on three legs, the fourth hoof tipped (pl. صُفُون)", "(at için) üç ayak üzerinde durup dördüncü toynağını büken (ç. صُفُون)", "صُفُون"),
 "tuluh-amr": P("طُلُوح", "Ṭulūḥ — in ذُو طُلُوح, a place", "Tulûh — ذُو طُلُوح terkibinde bir yer"),
 "shamat-amr": P("الشَّامَات", "al-Shāmāt — a stretch of country", "eş-Şâmât — bir arazi"),
 "muid-amr": N("مُوعِد", "و ع د", "one who threatens (ism fa'il of أَوْعَدَ)", "tehdit eden (أَوْعَدَ'den ism-i fâil)"),
 "harra-amr": VB("هَرَّ", "ه ر ر", "(of a dog) to snarl, to growl in dislike (هَرَّ يَهِرُّ)", "(köpek için) hoşlanmadığına hırlamak (هَرَّ يَهِرُّ)"),
 "shadhdhaba-amr": VB("شَذَّبَ", "ش ذ ب", "to lop, to clear a tree of its thorns and extra branches (Form II)", "budamak, ağacı dikenlerinden ve fazla dallarından temizlemek (tef'îl)", "II"),
 "qatada-amr": N("قَتَادَة", "ق ت د", "one tree of the qatād, a thorny shrub (tragacanth)", "keven ağacı (dikenli bir çalı), tek bir tanesi"),
})
NEW_VERBS.update({
 "dana-amr": _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "دَان", "دِن", "دِين", "دِن", "دِين", "دِن", "دِين", "دَائِن", note=HOLLOW_N + "يَدِينُ ← لَمْ يَدِنْ."),
 "tawwaja-amr": F2("تَوَّج", "تَوِّج", "تَتْوِيج", "مُتَوِّج", "مُتَوَّج", "تُوِّجَ", "يُتَوَّجُ"),
 "harra-amr": DBL_D("ه", "ر", "هَرِير", "هَارّ"),
 "shadhdhaba-amr": F2("شَذَّب", "شَذِّب", "تَشْذِيب", "مُشَذِّب", "مُشَذَّب", "شُذِّبَ", "يُشَذَّبُ"),
})
# ---- ch6 (vv. 30–36) ----
TAILOR.update({
 "raha": ("a millstone (a maqṣūr noun); رَحَى الْحَرْبِ: the thick of the battle (al-Zawzanī)", "değirmen taşı (maksûr isim); رَحَى الْحَرْبِ: savaşın en şiddetli yeri (Zevzenî)"),
 "ghashiya": ("to cover, to overwhelm; to come upon, to come at (غِشْيَان: إِتْيَان — al-Zawzanī)", "örtmek, bürümek; üzerine gelmek (gışyân: gelmek — Zevzenî)"),
 "abyad": ("white (pl. بِيض); بِيضٌ: white (swords)", "beyaz (ç. بِيض); بِيضٌ: beyaz (kılıçlar)"),
})
NEW_GLOSS.update({
 "tahin-amr": N("طَحِين", "ط ح ن", "flour, what is ground (فَعِيل in the sense of مَفْعُول)", "un, öğütülmüş şey (mef'ûl anlamında fa'îl)"),
 "lahwa-amr": N("لُهْوَة", "ل ه و", "a handful of grain thrown into the mouth of a hand-mill (al-Zawzanī)", "el değirmeninin ağzına atılan avuç dolusu tane (Zevzenî)"),
 "qudaa-amr": P("قُضَاعَة", "Quḍāʿa — a great tribal confederation of the Arabs; a diptote", "Kudâa — büyük bir Arap kabileler birliği; gayr-i munsarif"),
 "aajala-amr": VB("أَعْجَلَ", "ع ج ل", "to hurry (a thing) on, to hasten it (Form IV)", "(bir şeyi) acele ettirmek, çabuklaştırmak (if'âl)", "IV"),
 "qira-amr": N("قِرًى", "ق ر ي", "a guest's fare, the food of hospitality (a maqṣūr noun)", "misafire sunulan yemek, ziyafet (maksûr isim)"),
 "tahun-amr": N("طَحُون", "ط ح ن", "that grinds hard (an intensive فَعُول from طَحْن)", "çok öğüten, ezen (طَحْن'den mübalağalı fa'ûl)", pos="adj"),
 "qubayla-amr": N("قُبَيْلَ", "ق ب ل", "just before (the diminutive of قَبْلَ)", "hemen önce (قَبْلَ'nin tasgîri)"),
 "taana3-amr": VB("طَاعَنَ", "ط ع ن", "to fight with spears, to exchange spear-thrusts (Form III)", "mızrakla vuruşmak, karşılıklı mızrak saplamak (müfâale)", "III"),
 "khatti-amr": N("خَطِّيّ", "خ ط ط", "of al-Khaṭṭ (the coast of al-Baḥrayn where spears were sold); قَنَا الْخَطِّيِّ: the famous Khaṭṭī spears — al-Zawzanī: the spears of «the man of al-Khaṭṭ», Samhar", "Hatt'a mensup (mızrakların satıldığı Bahreyn kıyısı); قَنَا الْخَطِّيِّ: meşhur Hattî mızraklar — Zevzenî: «Hattlı adam» Semher'in mızrakları"),
 "ikhtala-amr": VB("اِخْتَلَى", "خ ل ي", "to cut down (fresh herbage); of swords, to cut down what they strike (Form VIII)", "(yaş otu) biçmek; kılıç için vurduğunu biçmek (ifti'âl)", "VIII"),
})
NEW_VERBS.update({
 "aajala-amr": F4("أَعْجَل", "عْجِل", "أَعْجِل", "إِعْجَال", "مُعْجِل"),
 "taana3-amr": F3("طَاعَن", "طَاعِن", "مُطَاعَنَة", "مُطَاعِن", "مُطَاعَن", "طُوعِنَ", "يُطَاعَنُ"),
 "ikhtala-amr": _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِخْتَلَ", "خْتَل", "i", "اِخْتَل", "اِخْتِلَاء", "مُخْتَلٍ (الْمُخْتَلِي)"),
})
DIV += [(31, "الْبَيْتُ ٣١ «شَرْقِيِّ» ← «شَرْقِيَّ» بِالْفَتْحِ، وَالشَّاهِدُ الدُّرَّةُ: «ظَرْفُ مَكَانٍ … فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُونُ»", "v. 31 «شَرْقِيِّ» → «شَرْقِيَّ» with fatha — witness: al-Durra, «an adverb of place … the predicate of يَكُونُ, in nasb»", "31. beyit «شَرْقِيِّ» → fethalı «شَرْقِيَّ» — şahit: Dürre, «mekân zarfı … «yekûnu»nun haberi, mansûb»")]
# ---- ch7 (vv. 37–43) ----
TAILOR.update({
 "raqaba": ("the neck; a slave (by naming the whole by the neck) (pl. رِقَاب)", "boyun; köle (bütünü boyunla anmak yoluyla) (ç. رِقَاب)"),
 "irtama": ("to throw to one another; (intransitive, as in v. 37) to tumble, to fall heavily (Form VIII)", "birbirine atmak; (37. beyitteki gibi lâzım) yuvarlanmak, ağırca düşmek (ifti'âl)"),
})
NEW_GLOSS.update({
 "wasq-amr": N("وَسْق", "و س ق", "a camel-load (pl. وُسُوق)", "bir deve yükü (ç. وُسُوق)", "وُسُوق"),
 "shaqq-amr": N("شَقّ", "ش ق ق", "splitting (masdar of شَقَّ)", "yarmak (شَقَّ'nin masdarı)"),
 "ikhtalaba-amr": VB("اِخْتَلَبَ", "خ ل ب", "to cut with a toothless sickle (مِخْلَب), to reap (Form VIII)", "dişsiz orakla (mihleb) kesmek, biçmek (ifti'âl)", "VIII"),
 "daa-amr": N("دَاء", "د و ء", "a sickness, a disease (pl. أَدْوَاء)", "hastalık, dert (ç. أَدْوَاء)", "أَدْوَاء"),
 "dafin-amr": N("دَفِين", "د ف ن", "buried, hidden (فَعِيل in the sense of مَدْفُون)", "gömülü, gizli (medfûn anlamında fa'îl)", pos="adj"),
 "imad-amr": N("عِمَاد", "ع م د", "a tent-pole; the poles that hold up the tents (عِمَادُ الْحَيِّ)", "çadır direği; çadırları ayakta tutan direkler (عِمَادُ الْحَيِّ)"),
 "hifd-amr": N("حَفَض", "ح ف ض", "household goods; a camel that carries them (pl. أَحْفَاض — al-Zawzanī)", "ev eşyası; onu taşıyan deve (ç. أَحْفَاض — Zevzenî)", "أَحْفَاض"),
 "jadhdha-amr": VB("جَذَّ", "ج ذ ذ", "to cut off (جَذَّ يَجُذُّ جَذًّا)", "kesip koparmak (جَذَّ يَجُذُّ جَذًّا)"),
 "mikhraq-amr": N("مِخْرَاق", "خ ر ق", "a play-sword, a sword of wood (or twisted cloth) used in a children's game (pl. مَخَارِيق)", "oyun kılıcı, çocuk oyununda kullanılan tahtadan (yahut bükülmüş bezden) kılıç (ç. مَخَارِيق)", "مَخَارِيق"),
 "laib-amr": N("لَاعِب", "ل ع ب", "one who plays (ism fa'il of لَعِبَ)", "oynayan (لَعِبَ'den ism-i fâil)"),
})
NEW_VERBS.update({
 "ikhtalaba-amr": F8("اِخْتَلَب", "خْتَلِب", "اِخْتِلَاب", "مُخْتَلِب"),
 "jadhdha-amr": DBL_N("ج", "ذ", "جَذّ", "جَاذّ", maful="مَجْذُوذ", pmz="جُذَّ", pmd="يُجَذُّ"),
})
DIV += [(38, "الْبَيْتُ ٣٨ «فَتَختَلينا» ← «فَيَخْتَلِينَا» بِالْيَاءِ، وَالشَّاهِدَانِ: نَصُّ الدُّرَّةِ «فَيَخْتَلِينَا»، وَشَرْحُ الزَّوْزَنِيِّ نَفْسُهُ «فَيَقْطَعْنَ»", "v. 38 «فَتَختَلينا» → «فَيَخْتَلِينَا» with ya — witnesses: al-Durra's text «فيختلينا» and al-Zawzanī's own gloss «فيقطعن»", "38. beyit «فَتَختَلينا» → yâ ile «فَيَخْتَلِينَا» — şahitler: Dürre'nin metni «فيختلينا» ve Zevzenî'nin kendi şerhi «فيقطعن»")]
# ---- ch8 (vv. 44–50) ----
TAILOR.update({
 "mushabbah": ("likened (ism mafʿūl of شَبَّهَ); the mushabbah of a tashbīh; in v. 45 = مُشْتَبَه, doubtful, seeming (al-Durra)", "benzetilen (شَبَّهَ'den ism-i mef'ûl); teşbîhte müşebbeh; 45. beyitte «müştebeh», belirsiz, olacakmış gibi görünen (Dürre)"),
 "hadd": ("an edge (of a blade); a limit; a prescribed punishment", "(kılıç) ağız; sınır; had cezası"),
 "thuba": ("a company, a band (pl. ثُبَات, and ثُبُونَ / ثُبِينَ like the sound masculine plural)", "topluluk, takım (ç. ثُبَات; ayrıca cem-i müzekker gibi ثُبُونَ / ثُبِينَ)"),
})
NEW_GLOSS.update({
 "urjuwan-amr": N("أُرْجُوَان", "ر ج و", "purple, a red dye (also a red flower); printed here أَرْجُوَان", "erguvan, kırmızı boya (kırmızı bir çiçek de); burada «ercuvân» diye basılmış"),
 "tala-amr": VB("طَلَى", "ط ل ي", "to smear, to coat (with a dye or salve) (طَلَى يَطْلِي)", "(boya yahut merhemle) sıvamak, sürmek (طَلَى يَطْلِي)"),
 "ayiya-amr": VB("عَيِيَ", "ع ي ي", "to be unable, to fail at (بِ); also عَيَّ by merging (عَيِيَ يَعْيَا)", "âciz kalmak, beceremez olmak (بِ ile); idgâmla عَيَّ de denir (عَيِيَ يَعْيَا)"),
 "isnaf-amr": N("إِسْنَاف", "س ن ف", "going forward, advancing (al-Zawzanī: الْإِقْدَام)", "ileri atılmak (Zevzenî: الْإِقْدَام)"),
 "hawl-amr": N("هَوْل", "ه و ل", "terror, a dread thing (pl. أَهْوَال)", "dehşet, korkunç şey (ç. أَهْوَال)", "أَهْوَال"),
 "rahwa-amr": P("رَهْوَة", "Rahwa — a mountain (al-Zawzanī: «this mountain»); a diptote", "Rehve — bir dağ (Zevzenî: «bu dağ»); gayr-i munsarif"),
 "mujarrab-amr": N("مُجَرَّب", "ج ر ب", "tried, tested, seasoned (ism maf'ul of جَرَّبَ)", "denenmiş, tecrübeli (جَرَّبَ'den ism-i mef'ûl)"),
 "hudayya-amr": N("حُدَيَّا", "ح د ي", "a challenge; the challenger (a noun on the diminutive pattern like ثُرَيَّا — al-Zawzanī: بِمَعْنَى التَّحَدِّي)", "meydan okuma; meydan okuyan (ثُرَيَّا gibi tasgîr kalıbında bir isim — Zevzenî: «tehaddî» anlamında)"),
 "muqaraa-amr": N("مُقَارَعَة", "ق ر ع", "fighting with swords, striking one another (masdar of قَارَعَ)", "kılıç kılıca vuruşma (قَارَعَ'nin masdarı)"),
 "khashya-amr": N("خَشْيَة", "خ ش ي", "fear, dread (masdar of خَشِيَ)", "korku, endişe (خَشِيَ'nin masdarı)"),
 "mutalabbib-amr": N("مُتَلَبِّب", "ل ب ب", "clad in arms (ism fa'il of تَلَبَّبَ — al-Zawzanī: التَّلَبُّبُ لُبْسُ السِّلَاحِ)", "silah kuşanmış (تَلَبَّبَ'den ism-i fâil — Zevzenî: «telebbüb» silah kuşanmaktır)"),
})
NEW_VERBS.update({
 "tala-amr": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "طَلَ", "طْل", "i", "اِطْل", "طَلْي", "طَالٍ", "مَطْلِيّ", "طُلِيَ", "يُطْلَى"),
 "ayiya-amr": _sg.naqis1("samia", "لَفِيفٌ مَقْرُونٌ", "y", "عَيِ", "عْي", "a", "اِعْي", "عِيّ", "عَيِيّ", note="عَيِيَ يَعْيَا — وَيُقَالُ بِالْإِدْغَامِ فِي الْمَاضِي: عَيَّ، وَبِهِ جَاءَ الْبَيْتُ ٤٥."),
})
DIV += [(49, "الْبَيْتُ ٤٩ «فَتُصْبِحَ» ← «فَتُصْبِحُ» بِالرَّفْعِ، لِأَنَّهُ جَوَابُ «أَمَّا» بَعْدَ الْفَاءِ، وَالشَّاهِدُ إِعْرَابُ الدُّرَّةِ لِنَظِيرِهِ «فَنُصْبِحُ» (مُضَارِعٌ مَرْفُوعٌ بَعْدَ فَاءِ جَوَابِ «أَمَّا»)", "v. 49 «فَتُصْبِحَ» → «فَتُصْبِحُ» in raf', the answer of أَمَّا after the fa — witness: al-Durra's iʿrāb of the parallel «فَنُصْبِحُ» (a present verb in raf' after the fa of أَمَّا's answer)", "49. beyit «فَتُصْبِحَ» → merfû «فَتُصْبِحُ», fâdan sonra «emmâ»nın cevabı — şahit: Dürre'nin benzer «fe-nusbihu» i'râbı (emmâ cevabının fâsından sonra merfû muzâri)")]
FLAGS += [(44, "هَمْزَةُ «بِأَرْجُوَانٍ» (ب ٤٤): مَفْتُوحَةٌ فِي الْمَطْبُوعِ فَأُبْقِيَتْ، وَالْمَعْرُوفُ فِي الْمَعَاجِمِ «أُرْجُوَانٌ» بِالضَّمِّ", "the hamza of «بِأَرْجُوَانٍ» (v. 44): printed with fatha and kept; the dictionaries give أُرْجُوَان with damma", "«bi-ercuvânin»ın hemzesi (44. beyit): baskıda fethalıdır, korunmuştur; sözlüklerde dammeli «ürcuvân»dır")]
# ---- ch9 (vv. 51–57) ----
TAILOR.update({
 "lb-qatin": ("servants (al-Zawzanī: الْقَطِينُ الْخَدَمُ); a company of people dwelling together (pl. قُطُن)", "hizmetçiler (Zevzenî: «katîn» hizmetçilerdir); bir arada oturan topluluk (ç. قُطُن)"),
 "ras": ("the head; the chief, the lord (al-Zawzanī: الرَّأْسُ الرَّئِيسُ وَالسَّيِّدُ) (pl. رُءُوس)", "baş; reis, efendi (Zevzenî) (ç. رُءُوس)"),
 "hazn": ("hard, rugged ground (pl. حُزُون) — the opposite of سَهْل", "sert, engebeli yer (ç. حُزُون) — «sehl»in zıddı"),
 "wana": ("to flag, to slacken (وَنَى يَنِي; in v. 52 وَنِينَا, on فَعِلَ for the rhyme)", "gevşemek, usanmak (وَنَى يَنِي; 52. beyitte kafiye için «fa'ile» üzere وَنِينَا)"),
})
NEW_GLOSS.update({
 "jusham-amr": P("جُشَم", "Jusham — Jusham ibn Bakr, the clan of Taghlib from which ʿAmr ibn Kulthūm came", "Cüşem — Cüşem b. Bekr, Amr b. Külsûm'un mensup olduğu Tağlib boyu"),
 "suhula-amr": N("سُهُولَة", "س ه ل", "plain, level ground; smoothness (al-Zawzanī: السَّهْل)", "düz, engelsiz yer; kolaylık (Zevzenî: «sehl»)"),
 "tadaada-amr": VB("تَضَعْضَعَ", "ض ع ض ع", "to be broken, to be humbled (a quadriliteral on تَفَعْلَلَ; ضَعْضَعْتُهُ فَتَضَعْضَعَ — al-Zawzanī)", "kırılmak, zelil olmak (تَفَعْلَلَ vezninde rubâî; ضَعْضَعْتُهُ فَتَضَعْضَعَ — Zevzenî)"),
 "qayl-amr": N("قَيْل", "ق و ل", "a lesser king, a prince below the great king (pl. أَقْيَال)", "büyük kralın altındaki kral, emîr (ç. أَقْيَال)", "أَقْيَال"),
 "izdara-amr": VB("اِزْدَرَى", "ز ر ي", "to belittle, to despise (Form VIII; its ta turns to dal after the zay)", "küçümsemek, hor görmek (ifti'âl; tâsı zâdan sonra dâle döner)", "VIII"),
 "tahaddada-amr": VB("تَهَدَّدَ", "ه د د", "to threaten (Form V)", "tehdit etmek (tefa''ul)", "V"),
 "maqtawi-amr": N("مَقْتَوِيّ", "ق ت و", "one in the service of kings (nisba of مَقْتًى, «service»; pl. مَقْتَوُونَ / مَقْتَوِينَ with the nisba ya dropped — al-Zawzanī); printed here مُقْتَوِينَا", "krallara hizmet eden («maktâ» hizmetin nisbeti; ç. nisbet yâsı atılarak مَقْتَوُونَ / مَقْتَوِينَ — Zevzenî); burada مُقْتَوِينَا diye basılmış"),
 "aya4-amr": VB("أَعْيَا", "ع ي ي", "to defeat, to be too hard for; to refuse (Form IV; al-Zawzanī: أَبَتْ)", "âciz bırakmak, zor gelmek; diretmek (if'âl; Zevzenî: «diretti»)", "IV"),
})
NEW_VERBS.update({
 "tadaada-amr": _sg.derived("مَزِيدُ الرُّبَاعِيِّ — بَابُ التَّفَعْلُلِ: تَفَعْلَلَ يَتَفَعْلَلُ", "تَفَعْلَلَ يَتَفَعْلَلُ", "َ", "تَضَعْضَع", "تَضَعْضَع", "تَضَعْضَع", "تَضَعْضُع", "مُتَضَعْضِع"),
 "izdara-amr": _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِزْدَرَ", "زْدَر", "i", "اِزْدَر", "اِزْدِرَاء", "مُزْدَرٍ (الْمُزْدَرِي)", note="اِفْتَعَلَ مِنْ «زَرَى»: تُقْلَبُ تَاؤُهُ دَالًا بَعْدَ الزَّايِ."),
 "tahaddada-amr": F5("تَهَدَّد", "تَهَدُّد", "مُتَهَدِّد"),
 "aya4-amr": _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَعْيَ", "عْي", "i", "أَعْي", "إِعْيَاء", "مُعْيٍ (الْمُعْيِي)"),
})
FLAGS += [
 (51, "حَرَكَةُ «جُشَمِ» (ب ٥١، ٦٠، ٩٠): مَكْسُورَةٌ فِي الْمَطْبُوعِ عَلَى أَنَّهُ مَصْرُوفٌ حُذِفَ تَنْوِينُهُ قَبْلَ «ابْنِ»، فَأُبْقِيَتْ؛ وَإِنْ عُدَّ مَعْدُولًا كَـ«عُمَرَ» فَحَقُّهُ الْفَتْحُ", "the vowel of «جُشَمِ» (vv. 51, 60, 90): printed with kasra, as a declinable name whose tanwin drops before ابْن, and kept; if it is counted a diptote like عُمَر it should take fatha", "«Cüşemi»nin harekesi (51, 60, 90. beyitler): baskıda «ibn»den önce tenvini düşmüş munsarif isim olarak kesrelidir, korunmuştur; «Umer» gibi ma'dûl sayılırsa fethalı olmalıdır"),
 (52, "نُونُ «وَنِينَا» (ب ٥٢): غَيْرُ مَشْكُولَةٍ فِي الْمَطْبُوعِ، وَضُبِطَتْ بِالْكَسْرِ لِأَنَّ رِدْفَ الْقَافِيَةِ يَاءٌ، وَالْمَشْهُورُ فِي الْمَعَاجِمِ «وَنَى يَنِي» (وَنَيْنَا)", "the nun of «وَنِينَا» (v. 52): unvowelled in the edition; written with kasra because the rhyme's ridf is a ya, though the dictionaries' common form is وَنَى يَنِي (وَنَيْنَا)", "«venînâ»nın nûnu (52. beyit): baskıda harekesizdir; kafiyenin ridfi yâ olduğu için kesreli yazılmıştır; sözlüklerde meşhur olan «venâ yenî»dir (veneynâ)"),
 (56, "مِيمُ «مُقْتَوِينَا» (ب ٥٦): مَضْمُومَةٌ فِي الْمَطْبُوعِ فَأُبْقِيَتْ، وَشَرْحُ الزَّوْزَنِيِّ (جَمْعُ «مَقْتَوِيٍّ» نِسْبَةً إِلَى الْمَقْتَى) يَقْتَضِي الْفَتْحَ؛ وَالضَّمُّ رِوَايَةُ اللِّسَانِ مِنَ «الِاقْتِوَاءِ»، كَمَا فِي حَاشِيَةِ «الشِّعْرِ وَالشُّعَرَاءِ»", "the mim of «مُقْتَوِينَا» (v. 56): printed with damma and kept; al-Zawzanī's derivation (plural of مَقْتَوِيّ, nisba of مَقْتًى) implies fatha; the damma is the Lisān's reading from اِقْتِوَاء, as the note to al-Shiʿr wa-l-shuʿarāʾ says", "«muktevînâ»nın mîmi (56. beyit): baskıda dammelidir, korunmuştur; Zevzenî'nin açıklaması («maktâ»ya nisbet «maktevî»nin cem'i) fethayı gerektirir; damme, eş-Şi'r ve'ş-şuarâ hâşiyesinde belirtildiği gibi Lisân'ın «iktivâ»dan rivayetidir"),
]
# ---- ch10 (vv. 58–64) ----
TAILOR.update({
 "naqs": ("a failing, a shortcoming (masdar of نَقَصَ); in grammar, dropping the last letter", "eksiklik, kusur (نَقَصَ'nin masdarı); nahivde son harfi düşürme"),
 "alqama": ("ʿAlqama — here ʿAlqama ibn Sayf, a forefather of Taghlib; a diptote", "Alkame — burada Tağlib'in atalarından Alkame b. Seyf; gayr-i munsarif"),
 "zuhayr": ("Zuhayr — a man's name; in v. 62 Zuhayr of Taghlib, an ancestor of ʿAmr's mother", "Züheyr — erkek adı; 62. beyitte Amr'ın annesinin atalarından Tağlibli Züheyr"),
 "khayr": ("good; خَيْرٌ مِنْهُ: better than he", "hayır, iyi; خَيْرٌ مِنْهُ: ondan daha hayırlı"),
 "bura-tf": ("a ring set in a camel's nose (pl. بُرًى); ذُو الْبُرَةِ: a man of Taghlib, named for hair on his nose that curled like a ring (al-Zawzanī)", "devenin burnuna takılan halka (ç. بُرًى); ذُو الْبُرَةِ: burnunun üstünde halka gibi kıvrılan kıl yüzünden bu adı alan Tağlibli bir adam (Zevzenî)"),
})
NEW_GLOSS.update({
 "thiqaf-amr": N("ثِقَاف", "ث ق ف", "the iron with which a spear-shaft is straightened", "mızrağın düzeltildiği demir"),
 "ishmaazza-amr": VB("اِشْمَأَزَّ", "ش م أ ز", "to shrink away in loathing, to recoil (a quadriliteral on اِفْعَلَلَّ)", "tiksinip çekilmek, ürkmek (اِفْعَلَلَّ vezninde rubâî)"),
 "walla-amr": VB("وَلَّى", "و ل ي", "to turn (a thing) towards; وَلَّاهُ ظَهْرَهُ: to turn one's back on him (Form II; two objects)", "bir şeyi birine çevirmek; وَلَّاهُ ظَهْرَهُ: ona sırtını döndü (tef'îl; iki mef'ûl)", "II"),
 "ashawzana-amr": N("عَشَوْزَنَة", "ع ش ز ن", "hard, tough (of a spear-shaft)", "sert, katı (mızrak için)", pos="adj"),
 "zabun-amr": N("زَبُون", "ز ب ن", "that thrusts back, kicking (of a she-camel that kicks her milker; hence الزَّبَانِيَة — al-Zawzanī)", "geri iten, tepen (sağanını tepen deve için; «zebâniye» de bundandır — Zevzenî)", pos="adj"),
 "inqalaba-amr": VB("اِنْقَلَبَ", "ق ل ب", "to be turned over, to turn round (Form VII)", "ters dönmek, dönmek (infi'âl)", "VII"),
 "aranna-amr": VB("أَرَنَّ", "ر ن ن", "to cry out, to give a ringing sound (Form IV, doubled)", "çınlamak, ses çıkarmak (if'âl, muzaaf)", "IV"),
 "qafan-amr": N("قَفًا", "ق ف و", "the nape of the neck (a maqṣūr noun)", "ense (maksûr isim)"),
 "muthaqqif-amr": N("مُثَقِّف", "ث ق ف", "one who straightens (a spear) (ism fa'il of ثَقَّفَ)", "(mızrağı) düzelten (ثَقَّفَ'tan ism-i fâil)"),
 "khatb-amr": N("خَطْب", "خ ط ب", "an affair, a matter of moment (pl. خُطُوب)", "iş, önemli hâl (ç. خُطُوب)", "خُطُوب"),
 "sayf-name-amr": P("سَيْف", "Sayf — in عَلْقَمَةُ بْنُ سَيْفٍ, a forefather of Taghlib", "Seyf — عَلْقَمَةُ بْنُ سَيْفٍ terkibinde, Tağlib'in atalarından"),
 "abaha-amr": VB("أَبَاحَ", "ب و ح", "to lay open, to make free (to someone) (Form IV, hollow)", "açmak, birine mubah kılmak (if'âl, ecvef)", "IV"),
 "hisn-amr": N("حِصْن", "ح ص ن", "a fortress, a stronghold (pl. حُصُون)", "kale, hisar (ç. حُصُون)", "حُصُون"),
 "din-qahr-amr": N("دِين", "د ي ن", "subjugation, force (al-Zawzanī: الدِّينُ الْقَهْرُ, as in ﴿غَيْرَ مَدِينِينَ﴾ «not subjugated»)", "kahır, zor (Zevzenî: «dîn» kahırdır; ﴿غَيْرَ مَدِينِينَ﴾ «kahredilmemiş» gibi)"),
 "muhalhil-amr": P("مُهَلْهِل", "Muhalhil — Muhalhil ibn Rabīʿa of Taghlib, the poet, maternal grandfather of ʿAmr ibn Kulthūm", "Mühelhil — Tağlibli şair Mühelhil b. Rebîa, Amr b. Külsûm'un anneannesi tarafından dedesi"),
 "dhukhr-amr": N("ذُخْر", "ذ خ ر", "a treasure laid up (pl. أَذْخَار)", "biriktirilmiş hazine (ç. أَذْخَار)"),
 "dhakhir-amr": N("ذَاخِر", "ذ خ ر", "one who lays up treasure (ism fa'il of ذَخَرَ)", "hazine biriktiren (ذَخَرَ'den ism-i fâil)"),
 "attab-amr": P("عَتَّاب", "ʿAttāb — ʿAttāb ibn Saʿd of Taghlib, a forefather of ʿAmr ibn Kulthūm", "Attâb — Amr b. Külsûm'un atalarından Tağlibli Attâb b. Sa'd"),
 "turath-amr": N("تُرَاث", "و ر ث", "an inheritance, a heritage (its ta from waw)", "miras (tâsı vâvdan dönmüştür)"),
 "akram-amr": N("أَكْرَم", "ك ر م", "nobler, noblest (elative of كَرِيم; pl. أَكْرَمُونَ)", "daha kerim, en kerim (كَرِيم'in ism-i tafdîli; ç. أَكْرَمُونَ)", pos="adj"),
})
def _fixhamza(v):
    def f(x):
        if isinstance(x, list): return [f(y) for y in x]
        if isinstance(x, str): return x.replace("أِ", "ئِ").replace("ِأْ", "ِئْ")
        return x
    return {k: f(x) for k, x in v.items()}
NEW_VERBS.update({
 "ishmaazza-amr": _fixhamza(dict(CLONE("isbakarra", "اِسْبَكَرَّ", [("س", "ش"), ("ب", "م"), ("ك", "أ"), ("ر", "ز")]), **{k: find_verb("isbakarra", "اِسْبَكَرَّ")[k] for k in ("bab", "wazn")})),
 "walla-amr": _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "وَلَّ", "وَلّ", "i", "وَلّ", "تَوْلِيَة", "مُوَلٍّ (الْمُوَلِّي)"),
 "inqalaba-amr": _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْقَلَب", "نْقَلِب", "اِنْقَلِب", "اِنْقِلَاب", "مُنْقَلِب"),
 "aranna-amr": F4D("ر", "ن", "إِرْنَان", "مُرِنّ", "مُضَاعَفٌ: يُرِنُّ — لَمْ يُرِنَّ."),
 "abaha-amr": _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ", _sg.W4, "ُ", "أَبَاح", "أَبَح", "بِيح", "بِح", "أَبِيح", "أَبِح", "إِبَاحَة", "مُبِيح", maful="مُبَاح", pmz="أُبِيحَ", pmd="يُبَاحُ"),
})
DIV += [(62, "الْبَيْتُ ٦٢ «ذُخْرِ» ← «ذُخْرُ» بِالرَّفْعِ فَاعِلًا لِـ«نِعْمَ»، وَالشَّاهِدُ الدُّرَّةُ: «ذُخْرُ: فَاعِلُ نِعْمَ»", "v. 62 «ذُخْرِ» → «ذُخْرُ» in raf' as the doer of نِعْمَ — witness: al-Durra, «ذخر: the doer of نعم»", "62. beyit «ذُخْرِ» → «ni'me»nin fâili olarak merfû «ذُخْرُ» — şahit: Dürre, «zuhr: ni'me'nin fâili»")]
NEW_VERBS["aya4-amr"] = json.loads(json.dumps(NEW_VERBS["aya4-amr"], ensure_ascii=False).replace("يَى", "يَا"))
# ---- ch11 (vv. 65–71) ----
TAILOR.update({
 "qarina": ("a she-camel yoked to another (v. 66, al-Zawzanī: «ناقتنا»); in balāgha, the sign that turns a word from its first sense", "bir başkasına koşulan dişi deve (66. beyit, Zevzenî: «devemiz»); belâgatta lafzı ilk anlamından çeviren karîne"),
 "hakim-ruler": ("one who rules, who judges; a ruler (ism fāʿil of حَكَمَ)", "hükmeden, hüküm veren; hâkim (حَكَمَ'den ism-i fâil)"),
})
NEW_GLOSS.update({
 "kulayb-amr": P("كُلَيْب", "Kulayb — Kulayb Wāʾil of Taghlib, the great chief whose killing began the war of al-Basūs; the uncle of ʿAmr's mother", "Küleyb — Tağlib'in büyük reisi Küleyb-i Vâil; öldürülmesi Besûs savaşını başlatmıştır; Amr'ın annesinin amcası"),
 "qarin-amr": N("قَرِين", "ق ر ن", "the one yoked or tied to another, a companion in harness", "bir başkasına koşulan, eş, yoldaş"),
 "waqasa-amr": VB("وَقَصَ", "و ق ص", "to break the neck (وَقَصَ يَقِصُ وَقْصًا — al-Zawzanī)", "boynunu kırmak (وَقَصَ يَقِصُ وَقْصًا — Zevzenî)"),
 "amna-amr": N("أَمْنَع", "م ن ع", "more (most) jealous in guarding, more unassailable (elative of مَنِيع)", "korumada daha (en) çetin, daha dokunulmaz (مَنِيع'in ism-i tafdîli)", pos="adj"),
 "dhimar-amr": N("ذِمَار", "ذ م ر", "what a man must guard and defend — pledge, alliance, protection (al-Zawzanī)", "insanın korumakla yükümlü olduğu şey — ahit, antlaşma, zimmet (Zevzenî)"),
 "awfa-el-amr": N("أَوْفَى", "و ف ي", "more (most) faithful in keeping one's word (elative of وَفِيّ)", "sözünde daha (en) vefalı (وَفِيّ'nin ism-i tafdîli)", pos="adj"),
 "khazaza-amr": P("خَزَازَى", "Khazāzā — a mountain where Nizār defeated Yemen; a diptote (feminine alif maqṣūra)", "Hazâzâ — Nizâr'ın Yemen'i yendiği bir dağ; gayr-i munsarif (maksûre te'nîs elifi)"),
 "rafada-amr": VB("رَفَدَ", "ر ف د", "to help, to aid (رَفَدَ يَرْفِدُ رَفْدًا)", "yardım etmek (رَفَدَ يَرْفِدُ رَفْدًا)"),
 "rifd-amr": N("رِفْد", "ر ف د", "help, aid (the noun; رَفْد is the masdar — al-Zawzanī)", "yardım (isim; «refd» masdardır — Zevzenî)"),
 "rafid-amr": N("رَافِد", "ر ف د", "one who helps (ism fa'il of رَفَدَ)", "yardım eden (رَفَدَ'den ism-i fâil)"),
 "habis-amr": N("حَابِس", "ح ب س", "one who holds back, who keeps in (ism fa'il of حَبَسَ)", "tutan, alıkoyan (حَبَسَ'ten ism-i fâil)"),
 "arata-amr": P("أَرَاطَى", "Arāṭā — in ذُو أَرَاطَى, a place; a diptote (feminine alif maqṣūra)", "Erâtâ — ذُو أَرَاطَى terkibinde bir yer; gayr-i munsarif"),
 "jilla-amr": N("جِلَّة", "ج ل ل", "the full-grown, the great ones among camels (al-Zawzanī)", "develerin iri, büyük olanları (Zevzenî)"),
 "akhwar-amr": N("خَوْرَاء", "خ و ر", "(of a she-camel) rich in milk, a copious milker (pl. خُور — al-Zawzanī)", "(dişi deve için) sütü bol (ç. خُور — Zevzenî)", "خُور", pos="adj"),
 "darin-amr": N("دَرِين", "د ر ن", "grass grown old and black (al-Zawzanī)", "eskiyip kararmış ot (Zevzenî)"),
 "azim-amr": N("عَازِم", "ع ز م", "resolved, determined (ism fa'il of عَزَمَ)", "azmeden, kararlı (عَزَمَ'den ism-i fâil)"),
 "sakhita-amr": VB("سَخِطَ", "س خ ط", "to be displeased with, to dislike (سَخِطَ يَسْخَطُ)", "hoşnut olmamak, beğenmemek (سَخِطَ يَسْخَطُ)"),
 "akhidh-amr": N("آخِذ", "أ خ ذ", "one who takes (ism fa'il of أَخَذَ)", "alan (أَخَذَ'den ism-i fâil)"),
})
NEW_VERBS.update({
 "waqasa-amr": dict(CLONE("wajada", "وَجَدَ", [("ج", "ق"), ("د", "ص")], note="مِثَالٌ وَاوِيٌّ: وَقَصَ يَقِصُ — تُحْذَفُ فَاؤُهُ فِي الْمُضَارِعِ وَالْأَمْرِ."), masdar="وَقْص", ismFail="وَاقِص"),
 "rafada-amr": _sg1("daraba", "رَفَد", "رْفِد", "اِرْفِد", "رَفْد", "رَافِد", "مَرْفُود", "رُفِدَ", "يُرْفَدُ"),
 "sakhita-amr": _sg1("samia", "سَخِط", "سْخَط", "اِسْخَط", "سَخَط", "سَاخِط", "مَسْخُوط", "سُخِطَ", "يُسْخَطُ"),
})
# ---- ch12 (vv. 72–78) ----
TAILOR.update({
 "ayman": ("on the right; the right-hand side (pl. أَيْمَنُونَ: those of the right wing)", "sağdaki; sağ taraf (ç. أَيْمَنُونَ: sağ kanattakiler)"),
 "aysar": ("on the left; easier (pl. أَيْسَرُونَ: those of the left wing)", "soldaki; daha kolay (ç. أَيْسَرُونَ: sol kanattakiler)"),
 "nahb": ("plunder, spoil (pl. نِهَاب)", "yağma, ganimet (ç. نِهَاب)"),
 "ilayka-ism-fil": ("إِلَيْكَ / إِلَيْكُمْ: a noun of command from a jarr phrase — «keep away! stand aside!» (al-Zawzanī); also «here, take!»", "إِلَيْكَ / إِلَيْكُمْ: câr-mecrûrdan emir ism-i fiili — «uzak dur! çekil!» (Zevzenî); ayrıca «al!»"),
 "lamma": ("when (with a past verb); with a present verb, in jazm: not (yet)", "-dığında (mâzî ile); muzâri ile, cezmederek: henüz değil"),
 "bayda-egg": ("an egg; a helmet (pl. بَيْض, بُيُوض)", "yumurta; miğfer (ç. بَيْض, بُيُوض)"),
})
NEW_GLOSS.update({
 "sala-amr": VB("صَالَ", "ص و ل", "to charge, to attack (صَالَ يَصُولُ صَوْلَةً)", "hücum etmek, saldırmak (صَالَ يَصُولُ صَوْلَةً)"),
 "sabiyya-amr": N("سَبِيَّة", "س ب ي", "a woman taken captive (pl. سَبَايَا)", "esir alınmış kadın (ç. سَبَايَا)", "سَبَايَا"),
 "musaffad-amr": N("مُصَفَّد", "ص ف د", "fettered, bound (ism maf'ul of صَفَّدَ — al-Zawzanī: التَّصْفِيدُ التَّقْيِيدُ)", "zincire vurulmuş, bağlı (صَفَّدَ'den ism-i mef'ûl — Zevzenî)"),
 "ittaana-amr": VB("اِطَّعَنَ", "ط ع ن", "to thrust spears at one another (Form VIII; = تَطَاعَنَ — al-Zawzanī)", "birbirine mızrak saplamak (ifti'âl; = تَطَاعَنَ — Zevzenî)", "VIII"),
 "yalab-amr": N("يَلَب", "ي ل ب", "a corselet woven of leather thongs, worn under the helmet (al-Zawzanī)", "miğferin altına giyilen, deri şeritlerden örülmüş zırh (Zevzenî)"),
 "yamani-amr": N("يَمَانٍ", "ي م ن", "of Yemen, Yemenī (= يَمَنِيّ, an alif making up for one nisba ya)", "Yemen'e mensup (= يَمَنِيّ; nisbet yâlarından birinin yerine elif)", pos="adj"),
 "inhana-amr": VB("اِنْحَنَى", "ح ن ي", "to bend, to be bowed (Form VII)", "eğilmek, bükülmek (infi'âl)", "VII"),
 "dilas-amr": N("دِلَاص", "د ل ص", "gleaming, smooth and bright (of mail)", "parlak, düzgün ve parıldayan (zırh için)", pos="adj"),
 "nitaq-amr": N("نِطَاق", "ن ط ق", "a belt, a girdle (= مِنْطَقَة)", "kuşak, kemer (= مِنْطَقَة)"),
 "ghadan-amr": N("غَضَن", "غ ض ن", "a fold, a crease (pl. غُضُون)", "kıvrım, kırışık (ç. غُضُون)", "غُضُون"),
})
NEW_VERBS.update({
 "sala-amr": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "صَال", "صُل", "صُول", "صُل", "صُول", "صُل", "صَوْل", "صَائِل", note=HOLLOW_N + "يَصُولُ ← لَمْ يَصُلْ."),
 "ittaana-amr": F8("اِطَّعَن", "طَّعِن", "اِطِّعَان", "مُطَّعِن", note="اِفْتَعَلَ مِنْ «طَعَنَ»: تُقْلَبُ تَاؤُهُ طَاءً وَتُدْغَمُ."),
 "inhana-amr": _sg.derived_naqis(_sg.B7, _sg.W7, "َ", "اِنْحَنَ", "نْحَن", "i", "اِنْحَن", "اِنْحِنَاء", "مُنْحَنٍ (الْمُنْحَنِي)"),
})
DIV += [
 (72, "الْبَيْتُ ٧٢ «الأَيْسَرَيْنِ» ← «الْأَيْسَرِينَ» جَمْعًا كَـ«الْأَيْمَنِينَ»، وَالشَّاهِدُ الدُّرَّةُ (خَبَرُ كَانَ … وَعَلَامَةُ نَصْبِهِ مِثْلُ الْأَوَّلِ: الْيَاءُ فِي جَمْعِ الْمُذَكَّرِ السَّالِمِ)", "v. 72 «الأَيْسَرَيْنِ» (a dual) → «الْأَيْسَرِينَ», a plural like «الْأَيْمَنِينَ» — witness: al-Durra (the predicate of كَانَ, its nasb sign as in the first: the ya of the sound masculine plural)", "72. beyit «الأَيْسَرَيْنِ» (tesniye) → «الْأَيْمَنِينَ» gibi cem' «الْأَيْسَرِينَ» — şahit: Dürre (kâne'nin haberi, nasb alâmeti birincisi gibi cem-i müzekker sâlim yâsı)"),
 (76, "الْبَيْتُ ٧٦ «كَتَائِبُ» ← «كَتَائِبَ» بِالنَّصْبِ مَفْعُولًا بِهِ، وَالشَّاهِدُ الدُّرَّةُ: «كَتَائِبَ: مَفْعُولٌ بِهِ»، وَشَرْحُ الزَّوْزَنِيِّ «أَلَمْ تَعْلَمُوا كَتَائِبَ»", "v. 76 «كَتَائِبُ» → «كَتَائِبَ» in nasb as the object — witnesses: al-Durra («كتائب: مفعول به») and al-Zawzanī's gloss «ألم تعلموا كتائب»", "76. beyit «كَتَائِبُ» → mef'ûl olarak mansûb «كَتَائِبَ» — şahitler: Dürre («ketâib: mef'ûlün bih») ve Zevzenî'nin şerhi"),
 (77, "الْبَيْتُ ٧٧ «وَأَسْيَافٍ» ← «وَأَسْيَافٌ» بِالرَّفْعِ عَطْفًا عَلَى «الْبَيْضُ»، وَالشَّاهِدُ الدُّرَّةُ: «أَسْيَافٌ: مَعْطُوفٌ عَلَى الْبَيْضِ»", "v. 77 «وَأَسْيَافٍ» → «وَأَسْيَافٌ» in raf', joined to «helmets» — witness: al-Durra («أسياف: معطوف على البيض»)", "77. beyit «وَأَسْيَافٍ» → «miğferler»e ma'tûf olarak merfû «وَأَسْيَافٌ» — şahit: Dürre"),
]
# ---- ch13 (vv. 79–85) ----
TAILOR.update({
 "warada": ("to come down to water; to come, to arrive; to go into (battle)", "suya inmek; gelmek, varmak; (savaşa) girmek"),
 "hana": ("to be held cheap, to be humbled (هَانَ يَهُونُ); of words, to grow light", "hor görülmek, zelil olmak (هَانَ يَهُونُ); söz için hafiflemek"),
 "ahd": ("a pledge, a covenant; a meeting, coming upon", "ahit, söz; karşılaşma, rastlama"),
 "hasan-adj": ("fine, good, fair (pl. حِسَان)", "güzel, iyi (ç. حِسَان)"),
})
NEW_GLOSS.update({
 "jawn-amr": N("جَوْن", "ج و ن", "black; also white — a word of opposite senses (pl. جُون — al-Zawzanī)", "siyah; beyaz da — zıt anlamlı kelime (ç. جُون — Zevzenî)", "جُون", pos="adj"),
 "ghadir-amr": N("غَدِير", "غ د ر", "a pool of rain-water left by a flood (pl. غُدُر، غُدْر، غُدْرَان)", "selden kalan yağmur gölü (ç. غُدُر، غُدْر، غُدْرَان)", "غُدْرَان"),
 "saffaqa-amr": VB("صَفَّقَ", "ص ف ق", "to strike, to dash (water) to and fro (Form II)", "vurmak, (suyu) dalgalandırmak (tef'îl)", "II"),
 "raw-amr": N("رَوْع", "ر و ع", "alarm, fright (al-Zawzanī: الْفَزَعُ — here war)", "korku, dehşet (Zevzenî: «feza'» — burada savaş)"),
 "naqidha-amr": N("نَقِيذَة", "ن ق ذ", "(a mare) rescued from the enemy's hands (pl. نَقَائِذ; فَعِيلَة in the sense of مُفْعَلَة)", "düşman elinden kurtarılmış (kısrak) (ç. نَقَائِذ; muf'ale anlamında fa'île)", "نَقَائِذ"),
 "iftala-amr": VB("اِفْتَلَى", "ف ل و", "to wean (a foal) (Form VIII; فَلْو and اِفْتِلَاء: weaning — al-Zawzanī)", "(tayı) sütten kesmek (ifti'âl; Zevzenî: «felv» ve «iftilâ» sütten kesmektir)", "VIII"),
 "dari-amr": N("دَارِع", "د ر ع", "wearing a coat of mail; of horses, barded (pl. دَوَارِع)", "zırhlı; atlar için zırh giydirilmiş (ç. دَوَارِع)", "دَوَارِع", pos="adj"),
 "ashath-amr": N("أَشْعَث", "ش ع ث", "dishevelled, with matted, dusty hair (pl. شُعْث)", "saçı başı dağınık, tozlu (ç. شُعْث)", "شُعْث", pos="adj"),
 "rasia-amr": N("رَصِيعَة", "ر ص ع", "the knot of the rein on a horse's poll (pl. رَصَائِع)", "atın ensesindeki dizgin düğümü (ç. رَصَائِع)", "رَصَائِع"),
 "hadhara3-amr": VB("حَاذَرَ", "ح ذ ر", "to beware of, to guard against (Form III)", "sakınmak, kaçınmak (müfâale)", "III"),
 "baal-amr": N("بَعْل", "ب ع ل", "a husband (pl. بُعُول، بُعُولَة)", "koca (ç. بُعُول، بُعُولَة)", "بُعُولَة"),
 "mulim-amr": N("مُعْلِم", "ع ل م", "one who marks himself for battle with a sign (ism fa'il of أَعْلَمَ)", "savaş için kendini bir nişanla işaretleyen (أَعْلَمَ'den ism-i fâil)"),
})
NEW_VERBS.update({
 "saffaqa-amr": F2("صَفَّق", "صَفِّق", "تَصْفِيق", "مُصَفِّق", "مُصَفَّق", "صُفِّقَ", "يُصَفَّقُ"),
 "iftala-amr": _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِفْتَلَ", "فْتَل", "i", "اِفْتَل", "اِفْتِلَاء", "مُفْتَلٍ (الْمُفْتَلِي)", maful="مُفْتَلًى", pmz="اُفْتُلِيَ", pmd="يُفْتَلَى"),
 "hadhara3-amr": F3("حَاذَر", "حَاذِر", "مُحَاذَرَة", "مُحَاذِر", "مُحَاذَر", "حُوذِرَ", "يُحَاذَرُ"),
})
# ---- ch14 (vv. 86–91) ----
TAILOR.update({
 "asir": ("a captive (pl. أَسْرَى، أُسَارَى)", "esir (ç. أَسْرَى، أُسَارَى)"),
 "bariz": ("out in the open, standing forth (ism fāʿil of بَرَزَ); in grammar, the pronoun that shows", "açıkta, ortaya çıkmış (بَرَزَ'den ism-i fâil); nahivde görünen (bâriz) zamir"),
 "raha-become": ("to go or come in the evening (رَاحَ يَرُوحُ); to become", "akşamleyin gitmek ya da gelmek (رَاحَ يَرُوحُ); olmak"),
 "sharib": ("one who drinks; a drinker of wine (pl. شَارِبُونَ)", "içen; şarap içen (ç. شَارِبُونَ)"),
 "jawad": ("generous; of a horse, a fine, swift steed (pl. جِيَاد)", "cömert; at için soylu, hızlı at (ç. جِيَاد)"),
 "hasab": ("noble lineage — what is counted of a man's and his forebears' noble deeds (a فَعَل meaning مَفْعُول — al-Zawzanī); measure", "soyluluk — insanın ve atalarının sayılan meziyetleri (mef'ûl anlamında fa'al — Zevzenî); ölçü"),
 "khalata": ("to mix, to join together (خَلَطَ يَخْلِطُ)", "karıştırmak, bir araya getirmek (خَلَطَ يَخْلِطُ)"),
})
NEW_GLOSS.update({
 "istalaba-amr": VB("اِسْتَلَبَ", "س ل ب", "to snatch away, to carry off as spoil (Form VIII)", "kapıp götürmek, yağma etmek (ifti'âl)", "VIII"),
 "muqarran-amr": N("مُقَرَّن", "ق ر ن", "coupled, bound together (ism maf'ul of قَرَّنَ)", "birbirine bağlanmış (قَرَّنَ'den ism-i mef'ûl)"),
 "huwayna-amr": N("هُوَيْنَى", "ه و ن", "a gentle, easy pace (diminutive of هُونَى, feminine of أَهْوَن — al-Zawzanī)", "yavaş, ağır yürüyüş («ehven»in müennesi «hûnâ»nın tasgîri — Zevzenî)"),
 "qata-amr": VB("قَاتَ", "ق و ت", "to feed with a ration, to give one's daily food (قَاتَ يَقُوتُ قُوتًا)", "azık vermek, gündelik yiyeceği vermek (قَاتَ يَقُوتُ قُوتًا)"),
 "misam-amr": N("مِيسَم", "و س م", "beauty, comeliness (from وَسَام / وَسَامَة — al-Zawzanī)", "güzellik, yakışıklılık (وَسَام / وَسَامَة'dan — Zevzenî)"),
 "saida-amr": N("سَاعِد", "س ع د", "the forearm (pl. سَوَاعِد)", "önkol (ç. سَوَاعِد)", "سَوَاعِد"),
 "qula-amr": N("قُلَة", "ق ل و", "the short stick struck with a bat in the boys' game of tipcat (pl. قُلُونَ / قُلِينَ like the sound masculine plural)", "çocukların çelik çomak oyununda sopayla vurulan kısa çubuk (ç. قُلُونَ / قُلِينَ)"),
})
NEW_VERBS.update({
 "istalaba-amr": F8("اِسْتَلَب", "سْتَلِب", "اِسْتِلَاب", "مُسْتَلِب"),
 "qata-amr": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "قَات", "قُت", "قُوت", "قُت", "قُوت", "قُت", "قُوت", "قَائِت", note=HOLLOW_N + "يَقُوتُ ← لَمْ يَقُتْ؛ وَيَقُتْنَ مَعَ نُونِ النِّسْوَةِ."),
})
DIV += [
 (87, "الْبَيْتُ ٨٧ «حَيِّ» ← «حَيٍّ» بِالتَّنْوِينِ، مُضَافًا إِلَيْهِ نَكِرَةً، وَالشَّاهِدُ الدُّرَّةُ: «كُلٌّ مُبْتَدَأٌ، وَهُوَ مُضَافٌ، وَحَيٍّ مُضَافٌ إِلَيْهِ»", "v. 87 «حَيِّ» → «حَيٍّ» with tanwin, an indefinite second term of the idafa — witness: al-Durra («كل: mubtada, annexed; حي: the second term»)", "87. beyit «حَيِّ» → tenvinli «حَيٍّ», nekre muzâfun ileyh — şahit: Dürre"),
 (91, "الْبَيْتُ ٩١ «مِثْلَ» ← «مِثْلُ» بِالرَّفْعِ فَاعِلًا لِـ«مَنَعَ»، وَالشَّاهِدُ الدُّرَّةُ: «مِثْلُ: فَاعِلٌ»", "v. 91 «مِثْلَ» → «مِثْلُ» in raf' as the doer of «kept» — witness: al-Durra («مثل: فاعل»)", "91. beyit «مِثْلَ» → «korudu»nun fâili olarak merfû «مِثْلُ» — şahit: Dürre («misl: fâil»)"),
]
# ---- ch15 (vv. 92–97) ----
TAILOR.update({
 "mani-preventer": ("one who withholds, who keeps from (ism fāʿil of مَنَعَ; pl. مَانِعُونَ)", "esirgeyen, alıkoyan (مَنَعَ'den ism-i fâil; ç. مَانِعُونَ)"),
 "turran": ("all together, one and all (= جَمِيعًا)", "hep birlikte, istisnasız (= جَمِيعًا)"),
})
NEW_GLOSS.update({
 "musallal-amr": N("مُسَلَّل", "س ل ل", "drawn (of swords), unsheathed (ism maf'ul of سَلَّلَ; fem. pl. مُسَلَّلَات)", "sıyrılmış, kınından çekilmiş (kılıç) (سَلَّلَ'den ism-i mef'ûl; müen. ç. مُسَلَّلَات)"),
 "dahda-amr": VB("دَهْدَى", "د ه د ه", "to roll (a thing) along (a quadriliteral; = دَحْرَجَ — al-Zawzanī)", "(bir şeyi) yuvarlamak (rubâî; = دَحْرَجَ — Zevzenî)"),
 "hazawwar-amr": N("حَزَوَّر", "ح ز ر", "a sturdy, strong lad (pl. حَزَاوِرَة — al-Zawzanī)", "iri yarı, güçlü delikanlı (ç. حَزَاوِرَة — Zevzenî)", "حَزَاوِرَة"),
 "kura-amr": N("كُرَة", "ك ر و", "a ball (pl. كُرَات, and كُرِينَ / كُرُونَ like the sound masculine plural)", "top (ç. كُرَات; ayrıca cem-i müzekker gibi كُرِينَ / كُرُونَ)"),
 "mutim-amr": N("مُطْعِم", "ط ع م", "one who feeds (others) (ism fa'il of أَطْعَمَ)", "(başkalarını) doyuran (أَطْعَمَ'den ism-i fâil)"),
 "muhlik-amr": N("مُهْلِك", "ه ل ك", "one who destroys (ism fa'il of أَهْلَكَ)", "helâk eden (أَهْلَكَ'ten ism-i fâil)"),
 "nazil-amr": N("نَازِل", "ن ز ل", "one who alights, who halts and settles (ism fa'il of نَزَلَ)", "konan, konaklayan (نَزَلَ'den ism-i fâil)"),
})
NEW_VERBS.update({
 "dahda-amr": SAMAI(_sg.derived_naqis("رُبَاعِيٌّ مُجَرَّدٌ: فَعْلَلَ يُفَعْلِلُ — وَأَصْلُهُ «دَهْدَهَ»، قُلِبَتْ هَاؤُهُ الْأَخِيرَةُ يَاءً", "فَعْلَلَ يُفَعْلِلُ", "ُ", "دَهْدَ", "دَهْد", "i", "دَهْد", "دَهْدَاة", "مُدَهْدٍ (الْمُدَهْدِي)", note="سَمَاعِيٌّ: دَهْدَى يُدَهْدِي — مِنْ «دَهْدَهَ» بِقَلْبِ الْهَاءِ الْأَخِيرَةِ يَاءً.")),
})
# ---- ch16 (vv. 98–103) ----
TAILOR.update({
 "asim-protector": ("one who guards, a protector (ism fāʿil of عَصَمَ; pl. عَاصِمُونَ)", "koruyan, hâmi (عَصَمَ'den ism-i fâil; ç. عَاصِمُونَ)"),
 "khasf": ("abasement, disgrace (خَسْف or خُسْف — al-Zawzanī); سَامَهُ خَسْفًا: he loaded him with disgrace", "zillet, aşağılanma (hasf ya da husf — Zevzenî); سَامَهُ خَسْفًا: ona zillet yükledi"),
 "jabbar": ("a tyrant, a haughty overbearing man (an intensive; pl. جَبَابِرَة، جَبَابِر)", "zorba, mağrur ve zalim (mübalağa sîgası; ç. جَبَابِرَة، جَبَابِر)"),
 "safin-tf": ("ships — the plural (collective) of سَفِينَة", "gemiler — سَفِينَة'nin cem'i (cins ismi)"),
})
NEW_GLOSS.update({
 "safw-amr": N("صَفْو", "ص ف و", "the clear part (of water), what is pure and unmixed", "(suyun) duru kısmı, saf ve katışıksız olan"),
 "kadir-amr": N("كَدِر", "ك د ر", "muddy, turbid (of water)", "bulanık (su için)", pos="adj"),
 "tammah-amr": P("الطَّمَّاح", "al-Ṭammāḥ — in بَنُو الطَّمَّاحِ, a clan of the Arabs", "et-Tammâh — بَنُو الطَّمَّاحِ terkibinde bir Arap boyu"),
 "dumi-amr": P("دُعْمِيّ", "Duʿmī — a clan of Rabīʿa (named after its forefather Duʿmī)", "Du'mî — Rebîa'dan bir boy (atası Du'mî'ye nisbetle)"),
 "sama-amr": VB("سَامَ", "س و م", "to lay (hardship, disgrace) on someone (سَامَ يَسُومُ سَوْمًا; two objects)", "birine (meşakkat, zillet) yüklemek (سَامَ يَسُومُ سَوْمًا; iki mef'ûl)"),
})
NEW_VERBS.update({
 "sama-amr": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "سَام", "سُم", "سُوم", "سُم", "سُوم", "سُم", "سَوْم", "سَائِم", "مَسُوم", "سِيمَ", "يُسَامُ", HOLLOW_N + "يَسُومُ ← لَمْ يَسُمْ."),
})
DIV += [
 (101, "الْبَيْتُ ١٠١ «النَّاسُ» ← «النَّاسَ» بِالنَّصْبِ مَفْعُولًا أَوَّلَ لِـ«سَامَ»، وَالشَّاهِدُ الدُّرَّةُ: «النَّاسَ: مَفْعُولٌ بِهِ أَوَّلُ»، وَشَرْحُ الزَّوْزَنِيِّ «سَامَهُ خَسْفًا»", "v. 101 «النَّاسُ» → «النَّاسَ» in nasb as the first object of «lay on» — witnesses: al-Durra («the first object») and al-Zawzanī's «سامه خسفًا»", "101. beyit «النَّاسُ» → «yükledi»nin birinci mef'ûlü olarak mansûb «النَّاسَ» — şahitler: Dürre ve Zevzenî'nin «sâmehû hasfen» açıklaması"),
 (103, "الْبَيْتُ ١٠٣ «صَبِيٌ» ← «صَبِيٌّ» بِالتَّشْدِيدِ، وَالشَّاهِدُ الْوَزْنُ", "v. 103 «صَبِيٌ» → «صَبِيٌّ» with the shadda — witness: the metre", "103. beyit «صَبِيٌ» → şeddeli «صَبِيٌّ» — şahit: vezin"),
]
# ---- collation (all chapters) ----
DIV += [
 (50, "الْبَيْتُ ٥٠ «مُتَلَبِّينا» ← «مُتَلَبِّبِينَا» بِبَاءَيْنِ، وَالشَّوَاهِدُ: الْوَزْنُ (لَا يَتِمُّ الْوَافِرُ إِلَّا بِهِمَا)، وَشَرْحُ الزَّوْزَنِيِّ نَفْسُهُ «التَّلَبُّبُ: لُبْسُ السِّلَاحِ»، وَنَصُّ الدُّرَّةِ «مُتَلَبِّبِينَا»", "v. 50 «مُتَلَبِّينا» → «مُتَلَبِّبِينَا» with two bas — witnesses: the metre (the wāfir is not complete without them), al-Zawzanī's own gloss «تَلَبُّب is putting on arms», and al-Durra's text «متلببينا»", "50. beyit «مُتَلَبِّينا» → iki bâ ile «مُتَلَبِّبِينَا» — şahitler: vezin, Zevzenî'nin kendi şerhi («telebbüb» silah kuşanmaktır) ve Dürre'nin metni"),
 (66, "الْبَيْتُ ٦٦ «قَرِينَتِنَا» ← «قَرِينَتَنَا» بِالنَّصْبِ مَفْعُولًا لِـ«نَعْقِدْ»، وَالشَّاهِدُ الدُّرَّةُ: «قَرِينَتَنَا: مَفْعُولٌ بِهِ»", "v. 66 «قَرِينَتِنَا» → «قَرِينَتَنَا» in nasb as the object of «we tie» — witness: al-Durra («the object»)", "66. beyit «قَرِينَتِنَا» → «bağlasak»ın mef'ûlü olarak mansûb «قَرِينَتَنَا» — şahit: Dürre"),
 (95, "الْبَيْتُ ٩٥ «الْمُطْمِعُونَ» ← «الْمُطْعِمُونَ»، وَالشَّاهِدَانِ: نَصُّ الدُّرَّةِ «الْمُطْعِمُونَ»، وَشَرْحُ الزَّوْزَنِيِّ نَفْسُهُ «أَنَّا نُطْعِمُ الضِّيفَانَ»", "v. 95 «الْمُطْمِعُونَ» → «الْمُطْعِمُونَ» — witnesses: al-Durra's text «المطعمون» and al-Zawzanī's own gloss «that we feed the guests»", "95. beyit «الْمُطْمِعُونَ» → «الْمُطْعِمُونَ» — şahitler: Dürre'nin metni ve Zevzenî'nin kendi şerhi «misafirleri doyururuz»"),
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
assert all(k.endswith("-amr") for k in NEW_GLOSS), [k for k in NEW_GLOSS if not k.endswith("-amr")]

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
_sofar_ar = "وَهِيَ هُنَا كَامِلَةٌ لَمْ يُتْرَكْ مِنْهَا بَيْتٌ وَلَمْ يُقَدَّمْ وَلَمْ يُؤَخَّرْ" if WHOLE else "وَالْمَنْشُورُ مِنْهَا هُنَا الْأَبْيَاتُ ١–%s مُتَّصِلَةً لَمْ يُتْرَكْ مِنْ وَسَطِهَا بَيْتٌ، وَبَقِيَّتُهَا (%s–١٠٣) لَمْ تُنْشَرْ هُنَا بَعْدُ" % (_AD(DONE_TO), _AD(DONE_TO + 1))
_sofar_en = "given here WHOLE, none left out and none moved" if WHOLE else "of which this package gives vv. 1–%d as one unbroken run, with no verse skipped inside it; the rest of the ode (vv. %d–103) is not yet published here" % (DONE_TO, DONE_TO + 1)
_sofar_tr = "burada TAMAMI verilmiştir; hiçbiri atlanmamış, yeri değiştirilmemiştir" if WHOLE else "bu pakette 1–%d. beyitler, aradan hiçbir beyit atlanmadan, kesintisiz verilmiştir; kasidenin devamı (%d–103. beyitler) henüz yayımlanmamıştır" % (DONE_TO, DONE_TO + 1)
_d_ar = ("وَخُولِفَ الْمَطْبُوعُ فِي هٰذِهِ الْمَوَاضِعِ بِشَاهِدٍ: " + "؛ ".join("(%s) " % _AD(i + 1) + d[1] for i, d in enumerate(_div)) + ". ") if _div else ""
_d_en = ("The edition's print is departed from in these places, each against a witness: " + "; ".join("(%d) " % (i + 1) + d[2] for i, d in enumerate(_div)) + ". ") if _div else ""
_d_tr = ("Matbû metinden şu yerlerde, her biri bir şahide dayanılarak ayrılınmıştır: " + "; ".join("(%d) " % (i + 1) + d[3] for i, d in enumerate(_div)) + ". ") if _div else ""
ATTR_AR = ("نَصٌّ مَنْقُولٌ بِلَفْظِهِ. الْفَصْلُ الْأَوَّلُ مِنْ خَبَرِ عَمْرِو بْنِ كُلْثُومٍ فِي «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةِ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ٢٣٧٨٥)، ج ١ ص ٢٢٨–٢٢٩، مِنَ الْفِقْرَةِ ٣٨٥: قِطْعَةٌ مُتَّصِلَةٌ وَاحِدَةٌ لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ، أَوَّلُهَا «وَقَدْ كَانَ أَمَرَ عَمْرُو بْنُ هِنْدٍ أُمَّهُ» وَآخِرُهَا «وَسَارُوا نَحْوَ الْجَزِيرَةِ»؛ وَمَا قَبْلَهَا مِنَ الْخَبَرِ (نَسَبُهُ، وَسُؤَالُ عَمْرِو بْنِ هِنْدٍ نُدَمَاءَهُ، وَمَجِيءُ عَمْرٍو وَأُمِّهِ لَيْلَى بِنْتِ مُهَلْهِلٍ إِلَى الْحِيرَةِ) وَمَا بَعْدَهَا (الْبَيْتَانِ مِنَ الْمُعَلَّقَةِ وَمَا يَلِيهِمَا) غَيْرُ مَنْقُولٍ هُنَا؛ وَالْوَاوُ فِي «وَلَيْسَ هُنَاكَ سَيْفٌ غَيْرُهُ» زِيَادَةُ الْمُحَقِّقِ بَيْنَ مَعْقُوفَيْنِ مِنْ نُسَخٍ أُخَرَ وَالْخِزَانَةِ، أُثْبِتَتْ وَحُذِفَ الْمَعْقُوفَانِ. "
           "وَالْفُصُولُ بَعْدَهُ مُعَلَّقَتُهُ — وَهِيَ مِنَ الْبَحْرِ الْوَافِرِ، وَرَوِيُّهَا نُونٌ مَفْتُوحَةٌ بَعْدَهَا أَلِفُ الْإِطْلَاقِ، وَقَبْلَهَا يَاءٌ أَوْ وَاوٌ رِدْفًا — بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) وَتَرْتِيبِهِ وَعَدِّهِ فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةِ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م (الْكِتَابُ ١١٢٥٣)، ص ٢١٥–٢٣٥، مِائَةٌ وَثَلَاثَةُ أَبْيَاتٍ؛ " + _sofar_ar + ". " + _ch_ar + ". وَالْبَيْتُ جُمْلَةٌ وَاحِدَةٌ، وَعَلَامَةُ «•» آخِرُ صَدْرِهِ. الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ عَلَى حَالِهِ بِإِمْلَاءِ هٰذَا الرَّفِّ، وَمَا تَرَكَتْهُ عَارِيًا — وَهُوَ حَرَكَاتُ خَبَرِ ابْنِ قُتَيْبَةَ كُلُّهَا سِوَى الشَّدَّاتِ، وَكَثِيرٌ مِنْ حُرُوفِ الْأَبْيَاتِ وَأَوَاخِرِ كَلِمَاتِهَا — ضَبَطَهُ الْمُحَرِّرُ بِمَا يُوجِبُهُ الْإِعْرَابُ وَالْوَزْنُ وَالشَّرْحُ. " + _d_ar
           + ("وَتُرِكَ لِنَظَرِ الْعَالِمِ: " + "؛ ".join(f[1] for f in _flg) + ". " if _flg else "")
           + "إِعْرَابُ كُلِّ كَلِمَةٍ بِعِبَارَةِ هٰذَا الرَّفِّ، وَقَدْ رُوجِعَ عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ: إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهَ الدُّرَّة (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م؛ الْكِتَابُ ١٥١٠١٧، ج ١ ص ٣٢٣–٤٥٣) — وَهُوَ يَرْوِي الْقَصِيدَةَ مِائَةً وَثَمَانِيَةَ عَشَرَ بَيْتًا بِتَرْتِيبٍ غَيْرِ تَرْتِيبِ الزَّوْزَنِيِّ، وَلَيْسَ عِنْدَهُ الْبَيْتَانِ ٩٧–٩٨، وَإِنَّمَا عِنْدَهُ نَظِيرَاهُمَا ٧٠–٧١ (٧٣–٧٤ عِنْدَهُ)، فَأُعْرِبَا عَلَيْهِمَا — وَمَا خَالَفَ فِيهِ رِوَايَةَ الزَّوْزَنِيِّ مَذْكُورٌ عَلَى كَلِمَتِهِ، وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ: مَا سَمَّاهُ أَوْ وَصَفَهُ الزَّوْزَنِيُّ أَوِ الدُّرَّةُ نُسِبَ إِلَيْهِ، وَمَا كَانَ بِحَدِّ التَّلْخِيصِ وَحْدَهُ قِيلَ فِيهِ: «عَلَى حَدِّ التَّلْخِيصِ». وَالتَّرْجَمَةُ مَعْنَى الْبَيْتِ عَلَى شَرْحِ الزَّوْزَنِيِّ، لَا شِعْرٌ. وَتَقْسِيمُ الْفُصُولِ وَعَنَاوِينُهَا وَعَلَامَاتُ التَّرْقِيمِ مِنَ الْمُحَرِّرِ، وَالنَّصُّ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.")
ATTR_EN = ("The RECEIVED text, word for word. Chapter 1 is from the khabar of ʿAmr ibn Kulthūm in Ibn Qutayba (d. 276 AH), al-Shiʿr wa-l-shuʿarāʾ, in the edition al-Maktaba al-Shāmila names «Dār al-Ḥadīth, Cairo, 1423 AH» (book 23785), vol. 1 pp. 228–229, from § 385: one contiguous span with nothing cut from inside it, from «وَقَدْ كَانَ أَمَرَ عَمْرُو بْنُ هِنْدٍ أُمَّهُ» to «وَسَارُوا نَحْوَ الْجَزِيرَةِ»; what comes before it in the khabar (his lineage, ʿAmr ibn Hind's question to his boon-companions, the coming of ʿAmr and his mother Laylā bint Muhalhil to al-Ḥīra) and after it (the two verses of the Muʿallaqa and what follows) is not given here. The waw of «وَلَيْسَ هُنَاكَ سَيْفٌ غَيْرُهُ» is the editor's addition in square brackets, from other manuscripts and al-Khizāna; it is kept and the brackets dropped. "
           "The chapters after it are his Muʿallaqa — in the metre al-wāfir, rhyming on a nūn with fatḥa followed by the alif of iṭlāq, with a yāʾ or wāw before it (the ridf) — in the recension, order and verse-count of al-Zawzanī (d. 486 AH), Sharḥ al-Muʿallaqāt al-sabʿ, the edition Shamela names «Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423 AH / 2002 CE» (book 11253), pp. 215–235, one hundred and three verses, " + _sofar_en + ": " + _ch_en + ". Each verse is one sentence, and «•» marks the end of its first hemistich. The vowelling has two layers. What the edition vowels is kept, in this shelf's spelling; what it leaves bare — every short vowel of Ibn Qutayba's khabar (the edition prints only its shaddas), and many letters and word-endings of the verses — is supplied editorially, as the iʿrāb, the metre and the commentary require. " + _d_en
           + ("Left for the scholar's judgement: " + "; ".join(f[2] for f in _flg) + ". " if _flg else "")
           + "The iʿrāb of every word is in this shelf's own wording and was checked against Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409 AH / 1989 CE; book 151017, vol. 1 pp. 323–453) — he gives the ode in a hundred and eighteen verses in another order, and lacks vv. 97–98, having only their near-twins vv. 70–71 (his 73–74), on which those two are parsed; where his text differs from al-Zawzanī's, the difference is noted on the word, and where he gives two readings the first is given and the second mentioned. The figures of balāgha are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ: one that al-Zawzanī or al-Durra names or describes is credited to him, and one that rests on the Talkhīṣ's definition alone says «by the Talkhīṣ's definition». The translation gives each verse's plain meaning after al-Zawzanī; it is not poetry. The division into chapters, their titles and the punctuation are editorial, and the text awaits scholarly review.")
ATTR_TR = ("Metin LAFZIYLA aktarılmıştır. 1. bölüm, Amr b. Külsûm'un haberindendir: İbn Kuteybe (ö. 276 h.), eş-Şi'r ve'ş-şuarâ, el-Mektebetü'ş-Şâmile'nin «Dâru'l-Hadîs, Kahire, 1423 h.» diye andığı baskı (kitap 23785), c. 1 s. 228–229, 385. paragraftan: ortasından hiçbir şey çıkarılmamış tek ve kesintisiz bir parça, «وَقَدْ كَانَ أَمَرَ عَمْرُو بْنُ هِنْدٍ أُمَّهُ»dan «وَسَارُوا نَحْوَ الْجَزِيرَةِ»ya kadar; haberin bundan önceki kısmı (nesebi, Amr b. Hind'in nedimlerine sorusu, Amr'ın ve annesi Leylâ bint Mühelhil'in Hîre'ye gelişi) ile sonraki kısmı (muallakadan iki beyit ve devamı) burada verilmemiştir. «وَلَيْسَ هُنَاكَ سَيْفٌ غَيْرُهُ»deki vâv, muhakkikin başka nüshalardan ve el-Hizâne'den köşeli parantez içinde eklediği ziyadedir; korunmuş, parantez kaldırılmıştır. "
           "Sonraki bölümler onun muallakasıdır — vâfir bahrinden; revîsi fethalı nûn, ardından ıtlâk elifi, öncesinde ridf olarak yâ yahut vâv — Zevzenî'nin (ö. 486 h.) rivayeti, sıralaması ve beyit sayımıyla: Şerhu'l-Muallakâti's-seb', Şâmile'nin «Dâru İhyâi't-Türâsi'l-Arabî, 1423 h. / 2002 m.» diye andığı baskı (kitap 11253), s. 215–235, yüz üç beyit; " + _sofar_tr + ": " + _ch_tr + ". Her beyit tek cümledir; «•» işareti ilk mısraın sonudur. Harekeleme iki katmandır: baskının harekelediği, bu rafın imlâsıyla aynen korunmuştur; çıplak bıraktığı — İbn Kuteybe haberinin şeddeler dışındaki bütün harekeleri, beyitlerin birçok harfi ve kelime sonu — i'râbın, veznin ve şerhin gerektirdiği şekilde editörce konmuştur. " + _d_tr
           + ("Âlimin değerlendirmesine bırakılanlar: " + "; ".join(f[3] for f in _flg) + ". " if _flg else "")
           + "Her kelimenin i'râbı bu rafın kendi ifadesiyledir ve Muhammed Ali Tâhâ ed-Dürre'nin Fethu'l-Kebîri'l-Müteâl: İ'râbü'l-Muallakâti'l-aşri't-tıvâl'i (Mektebetü's-Sevâdî, Cidde, 2. baskı, 1409 h. / 1989 m.; kitap 151017, c. 1 s. 323–453) ile karşılaştırılmıştır — o, kasideyi başka bir sıra ile yüz on sekiz beyit olarak verir ve onda 97–98. beyitler yoktur; yalnız onlara çok benzeyen 70–71. beyitler (onun 73–74.leri) vardır, bu ikisi onlara göre i'râb edilmiştir; rivayetinin Zevzenî'ninkinden ayrıldığı yerler kelimesinin üzerinde belirtilmiştir; iki vecih zikrettiği yerde birincisi verilmiş, ikincisine işaret edilmiştir. Belâgat vecihleri Kazvînî'nin Telhîsu'l-Miftâh'ındaki bâblarla adlandırılmıştır: Zevzenî'nin yahut Dürre'nin adını koyduğu veya tarif ettiği vecih ona nisbet edilmiş, yalnız Telhîs'in tarifine dayanan vecih için «Telhîs'in tarifine göre» denmiştir. Tercüme, beytin Zevzenî şerhine göre düz mânasıdır; şiir değildir. Bölümleme, başlıklar ve noktalama editöre aittir; metin ilmî incelemeyi beklemektedir.")
MANIFEST = {
 "id": SLUG, "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ عَمْرِو بْنِ كُلْثُومٍ", "en": "The Muʿallaqa of ʿAmr ibn Kulthūm", "tr": "Amr b. Külsûm'un Muallakası"},
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
