"""Author content/samples/muallaqat-labid — «مُعَلَّقَةُ لَبِيدِ بْنِ رَبِيعَةَ», a RECEIVED text at Level 6 (Master).

Chapter 1 is the poet's khabar, VERBATIM from Ibn Qutayba, «الشعر والشعراء» (Dār al-Ḥadīth, Cairo 1423, 1/267, § 469;
shamela.ws/book/23785/260). The chapters after it are the Muʿallaqa in al-Zawzanī's text, order and count («شرح المعلقات
السبع», shamela.ws/book/11253/183–214, pp. 171–202): 88 verses, cut by PLAN below. A verse is ONE sentence; the last token
of its first hemistich carries punctAfter "•". The iʿrāb of every token was checked against Muḥammad ʿAlī Ṭāhā al-Durra,
«فتح الكبير المتعال» (shamela.ws/book/151017/548–664, vol. 2 pp. 7–123) and is written in the shelf's wording; the balāgha
is named on the token that carries it, after the syntax. A figure a commentator names or describes is written plainly
with his name; one that rests on the Talkhīṣ's definition alone says «عَلَى حَدِّ التَّلْخِيصِ».

Sources on disk: research/sources/muallaqat-labid-src.txt (Ibn Qutayba), muallaqat-labid-zawzani.txt, muallaqat-labid-durra.txt.

RESUMABLE: verses are filed by number through VV(); the chapters are cut from PLAN as far as the verses reach, and the
attribution says how far the package goes. To continue, add VV(n, …) blocks before the «TAIL» marker, their new keys to
NEW_GLOSS / NEW_VERBS, and run:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_labid.py
"""
import json, os, pathlib, sys, unicodedata, re

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-labid"
PKG = OUT_ROOT / SLUG

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import tok, seg, WA_AR, FA_AR, WA_ISTINAF
import sarf_gen as _sg

NO = ("", "", "")
def cap(s): return s[:1].upper() + s[1:]
def N3(*t):
    """join note triples"""
    return tuple("".join(x) for x in zip(*t)) if t else NO
def T(full, lex, pos, g, ar, en, tr, p=None, segs=None):
    return tok(full, lex, pos, list(g), ar, en, tr, punct=p, segments=segs)
def SG(*triples): return [seg(f, l, q) for f, l, q in triples]

PRON = {"هَا": "pron-3fs", "هُ": "pron-3ms", "هِ": "pron-3ms", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُنَّ": "pron-3fp", "هِنَّ": "pron-3fp",
        "هُمَا": "pron-3d", "هِمَا": "pron-3d", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "نَا": "pron-1p"}
PRON_AR = {"هَا": "هَا", "هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُنَّ": "هُنَّ", "هِنَّ": "هُنَّ", "هُمَا": "هُمَا", "هِمَا": "هُمَا",
           "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "نَا": "نَا"}
CONJ = {"w": ("wa", WA_AR, "The waw conjoins; ", "«ve» + "), "f": ("fa", FA_AR, "The fa conjoins; ", "«fe» + "),
        "wi": ("wa",) + WA_ISTINAF, "fi": ("fa", "الْفَاءُ لِلِاسْتِئْنَافِ، وَ", "The fa opens a new clause; ", "Fâ isti'nâf içindir; "),
        "wh": ("wa", "الْوَاوُ وَاوُ الْحَالِ، وَ", "The waw of hal; ", "Vâv hâliyyedir; ")}
JARR = {"bi": ("bi", "الْبَاءُ حَرْفُ جَرٍّ، وَ", "The ba is a jarr letter; ", "Bâ cer harfi; "),
        "ka": ("ka", "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَ", "The kaf is the jarr letter of likening; ", "Kâf teşbîh ve cer harfi; "),
        "li": ("li", "اللَّامُ حَرْفُ جَرٍّ، وَ", "The lam is a jarr letter; ", "Lâm cer harfi; ")}
SIGN = {"raf": "بِالضَّمَّةِ", "nasb": "بِالْفَتْحَةِ", "jarr": "بِالْكَسْرَةِ"}
ROLE = {
 "fail": ("فَاعِلٌ مَرْفُوعٌ", "the doer (fa'il), in raf'", "fâil, merfû", "raf", ["fail"]),
 "naib": ("نَائِبُ فَاعِلٍ مَرْفُوعٌ", "the deputy doer (na'ib al-fa'il), in raf'", "nâib-i fâil, merfû", "raf", ["naib-al-fail"]),
 "maf": ("مَفْعُولٌ بِهِ مَنْصُوبٌ", "the direct object, in nasb", "mef'ûlün bih, mansûb", "nasb", ["maful-bihi"]),
 "mub": ("مُبْتَدَأٌ مَرْفُوعٌ", "the mubtada, in raf'", "mübtedâ, merfû", "raf", ["mubtada-khabar"]),
 "khb": ("خَبَرُ الْمُبْتَدَأِ مَرْفُوعٌ", "the khabar of the mubtada, in raf'", "mübtedânın haberi, merfû", "raf", ["mubtada-khabar"]),
 "mdf": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "the second term of the idafa, in jarr", "muzâfun ileyh, mecrûr", "jarr", ["idafa-definiteness"]),
 "majr": ("مَجْرُورٌ", "in jarr after the letter", "cer harfiyle mecrûr", "jarr", ["huruf-jarr"]),
 "hal": ("حَالٌ مَنْصُوبٌ", "a hal, in nasb", "hâl, mansûb", "nasb", ["hal"]),
 "zarfz": ("ظَرْفُ زَمَانٍ مَنْصُوبٌ", "an adverb of time, in nasb", "zaman zarfı, mansûb", "nasb", ["maful-fih"]),
 "zarfm": ("ظَرْفُ مَكَانٍ مَنْصُوبٌ", "an adverb of place, in nasb", "mekân zarfı, mansûb", "nasb", ["maful-fih"]),
 "ismk": ("اسْمُ كَانَ مَرْفُوعٌ", "the noun of كَانَ, in raf'", "kâne'nin ismi, merfû", "raf", ["kana-wa-akhawatuha"]),
 "ismi": ("اسْمُ إِنَّ مَنْصُوبٌ", "the noun of إِنَّ, in nasb", "inne'nin ismi, mansûb", "nasb", ["inna-wa-akhawatuha"]),
 "tamyiz": ("تَمْيِيزٌ مَنْصُوبٌ", "a tamyiz (specifier), in nasb", "temyîz, mansûb", "nasb", ["tamyiz"]),
}
for _c, _a, _e, _t in (("r", "مَرْفُوعٌ", "raf'", "merfû", ), ("n", "مَنْصُوبٌ", "nasb", "mansûb"), ("j", "مَجْرُورٌ", "jarr", "mecrûr")):
    _k = {"r": "raf", "n": "nasb", "j": "jarr"}[_c]
    ROLE["naat" + _c] = ("نَعْتٌ " + _a, "an adjective (na't), in " + _e + " like its noun", "na't (sıfat), mevsûfu gibi " + _t, _k, ["naat-sifa"])
    ROLE["atf" + _c] = ("مَعْطُوفٌ " + _a, "conjoined to the word before it, in " + _e, "ma'tûf, " + _t, _k, ["atf-nasaq"])
    ROLE["bdl" + _c] = ("بَدَلٌ " + _a, "a badal (substitute), in " + _e + " like the word it stands for", "bedel, mübdelün minh gibi " + _t, _k, ["badal"])
MUD = ("، مُضَافٌ", ", annexed", ", muzâf")
ENC3 = ("، مُضَافٌ، وَ%s ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; annexed, and the attached pronoun is the second term of the idafa, in the seat of jarr", "; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr")

def R(role, full, lex, enc=None, n=NO, g=(), pos="noun", mud=False, sign=None, c=None, j=None, p=None):
    """a noun in a named seat: c = a conjunction written on it (w / f / wi / fi / wh), j = a jarr letter written on it
    (bi / ka / li), enc = its attached pronoun, mud = annexed to the next word, sign = (ar, en, tr) when not the default"""
    full = unicodedata.normalize("NFC", full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    r = ROLE[role]; head = r[0]
    if j:
        k, a, e, t = JARR[j]; segs.append(seg(stem[:2], k, "prep")); stem = stem[2:]
        ar0 += a; en0 += e; tr0 += t; head = "«" + stem + "» اسْمٌ مَجْرُورٌ"
    core = stem[:-len(enc)] if enc else stem
    sg = sign or (SIGN[r[3]], "", "")
    a = ar0 + head + " " + sg[0]; e = en0 + r[1] + sg[1]; t = tr0 + r[2] + sg[2]
    if enc: a += ENC3[0] % PRON_AR[enc]; e += ENC3[1]; t += ENC3[2]
    elif mud: a += MUD[0]; e += MUD[1]; t += MUD[2]
    segs.append(seg(core, lex, pos))
    if enc: segs.append(seg(enc, PRON[enc], "pron"))
    tags = list(r[4]) + (["idafa-definiteness", "al-bariz-al-muttasil"] if enc else ["idafa-definiteness"] if mud else []) + (["huruf-jarr"] if j else []) + list(g)
    return tok(full, lex, pos, tags, a + n[0] + ".", cap(e + n[1] + "."), cap(t + n[2] + "."), punct=p, segments=segs if len(segs) > 1 else None)

_M = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى "
VK = {
 "m": (_M + "الْفَتْحِ", "past verb built on fatha", "fetha üzere mebnî mâzî"),
 "ma": (_M + "فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "past verb built on a fatha estimated on the alif", "elif üzerindeki takdîrî fetha ile mebnî mâzî"),
 "mt": (_M + "الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "past verb built on fatha (the ta marks the feminine)", "fetha üzere mebnî mâzî (tâ te'nîs içindir)"),
 "mn": (_M + "السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "past verb built on sukun because the nun of the women is attached; that nun is the doer, in the seat of raf'", "nûn-ı nisve bitiştiği için sükûn üzere mebnî mâzî; nûn fâildir, mahallen merfû"),
 "mw": (_M + "الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "past verb built on damma because the waw of the group is attached; that waw is the doer, in the seat of raf'", "cemâat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâildir, mahallen merfû"),
 "mtu": (_M + "السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "past verb built on sukun because the ta of the doer is attached; that ta («I») is the doer, in the seat of raf'", "fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ («ben») fâildir, mahallen merfû"),
 "d": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ", "present verb in raf'", "merfû muzâri"),
 "da": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "present verb in raf' by a damma estimated on the alif", "elif üzerinde takdîrî damme ile merfû muzâri"),
 "dy": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "present verb in raf' by a damma estimated on the ya", "yâ üzerinde takdîrî damme ile merfû muzâri"),
 "dw": ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ", "present verb in raf' by a damma estimated on the waw", "vâv üzerinde takdîrî damme ile merfû muzâri"),
}
def DZ(ar, en, tr):
    """a hidden doer: DZ("هِيَ يَعُودُ عَلَى الدِّيَارِ", "«she» — the dwellings", "«diyâr»a dönen gizli «o»")"""
    return (ar, en, tr)
def V(kind, full, lex, n=NO, g=(), enc=None, c=None, pas=False, doer=None, p=None):
    full = unicodedata.normalize("NFC", full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    a, e, t = VK[kind]
    if pas:
        a = a.replace("فِعْلٌ مَاضٍ", "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ", 1).replace("فِعْلٌ مُضَارِعٌ", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ", 1)
        e = "passive " + e; t = "meçhul " + t
    if doer:
        a += ("، وَنَائِبُ الْفَاعِلِ" if pas else "، وَالْفَاعِلُ") + " مُسْتَتِرٌ تَقْدِيرُهُ: " + doer[0]
        e += ("; its deputy doer is the hidden " if pas else "; the doer is the hidden ") + doer[1]
        t += ("; nâib-i fâil " if pas else "; fâil ") + doer[2]
    core = stem[:-len(enc)] if enc else stem
    if enc:
        a += "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ"
        e += "; the attached pronoun is the object, in the seat of nasb"; t += "; bitişik zamir mef'ûlün bih, mahallen mansûb"
    segs.append(seg(core, lex, "verb"))
    if enc: segs.append(seg(enc, PRON[enc], "pron"))
    tags = (["mudari-marfu"] if kind[0] == "d" else []) + (["naib-al-fail"] if pas else []) + (["maful-bihi", "al-bariz-al-muttasil"] if enc else []) + (["al-bariz-al-muttasil", "fail"] if kind in ("mn", "mw", "mtu") else []) + list(g)
    return tok(full, lex, "verb", tags, ar0 + a + n[0] + ".", cap(en0 + e + n[1] + "."), cap(tr0 + t + n[2] + "."), punct=p, segments=segs if len(segs) > 1 else None)
def PR(full, lex, n=NO, g=(), p=None):
    """a jarr letter standing alone"""
    return T(full, lex, "prep", ["huruf-jarr"] + list(g), "حَرْفُ جَرٍّ" + n[0] + ".", "A jarr letter" + n[1] + ".", "Cer harfi" + n[2] + ".", p=p)
def JP(full, lex, enc, n=NO, g=(), p=None, c=None):
    """a jarr letter with its attached pronoun: بِهَا، مِنْهَا، عَلَيْهِ"""
    full = unicodedata.normalize("NFC", full); ar0 = en0 = tr0 = ""; segs = []; stem = full
    if c:
        k, a, e, t = CONJ[c]; ar0, en0, tr0 = a, e, t; segs.append(seg(stem[:2], k, "conj")); stem = stem[2:]
    segs += [seg(stem[:-len(enc)], lex, "prep"), seg(enc, PRON[enc], "pron")]
    return tok(full, lex, "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + list(g),
        ar0 + "حَرْفُ جَرٍّ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِهِ" + n[0] + ".",
        cap(en0 + "a jarr letter; the attached pronoun is in the seat of jarr after it" + n[1] + "."),
        cap(tr0 + "cer harfi; bitişik zamir onunla mahallen mecrûr" + n[2] + "."), punct=p, segments=segs)
def MT(ar, en, tr):
    """«وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ…» — tr carries its own case ending"""
    return (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«" + ar + "»", "; the phrase hangs on «" + en + "»", "; câr-mecrûr «" + tr + " müteallik")
def ZW(ar, en, tr):
    """a gloss or a reading that is al-Zawzanī's"""
    return (" — " + ar + " (الزَّوْزَنِيُّ)", " — " + en + " (al-Zawzanī)", " — " + tr + " (Zevzenî)")
def HADD(ar, en, tr):
    """a figure that rests on the Talkhīṣ's definition alone"""
    return (" — وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — " + ar, " — by the Talkhīṣ's definition, " + en, " — Telhîs'in tarifine göre " + tr)
RHYME = (" — وَهِيَ كَلِمَةُ الْقَافِيَةِ: الرَّوِيُّ مِيمٌ مَضْمُومَةٌ، وَالْهَاءُ بَعْدَهَا وَصْلٌ، وَأَلِفُهَا خُرُوجٌ، وَالْأَلِفُ قَبْلَ الْمِيمِ رِدْفٌ — وَعَلَيْهَا الْقَصِيدَةُ كُلُّهَا",
         " — the rhyme-word: the rawī is a mīm with damma, the ha after it is the waṣl, its alif the khurūj, and the alif before the mīm the ridf — so through the whole ode",
         " — kâfiye kelimesi: revî dammeli mîm, ondan sonraki hâ vasl, hâ'nın elifi hurûc, mîmden önceki elif ridftir — kaside baştan sona böyledir")

CH = {}
# =====================================================================================================================
# Chapter 1 — خَبَرُ لَبِيدٍ (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/267, § 469 — verbatim, contiguous)
# =====================================================================================================================
LABID_F = lambda n=NO, p=None: R("fail", "لَبِيدٌ", "lb-labid", pos="propn", n=n, p=p)
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Labīd lived to see Islam: he came to the Messenger of God — God bless him and grant him peace — in the delegation of the Banū Kilāb, and they accepted Islam and went back to their own country.",
  "tr": "Lebîd İslâm'a yetişti; Benî Kilâb heyeti içinde Resûlullah'ın — Allah ona salât ve selâm eylesin — huzuruna geldi; Müslüman oldular ve yurtlarına döndüler."},
 "tokens": [V("m", "وَأَدْرَكَ", "adraka", c="wi", g=["form-iv-verbs"], n=(" — وَالْوَاوُ تَصِلُ هٰذَا الْخَبَرَ بِمَا قَبْلَهُ مِنْ تَرْجَمَتِهِ", " — the waw ties this report to what came before it in his entry", " — vâv bu haberi tercemesinin önceki kısmına bağlar")),
  LABID_F(),
  R("maf", "الْإِسْلَامَ", "islam", g=["masdar"], n=(" — أَيْ عَاشَ حَتَّى بَلَغَ زَمَانَهُ", " — he lived on into its time", " — yani onun zamanına kadar yaşadı"), p="،"),
  V("m", "وَقَدِمَ", "qadima", c="w", doer=DZ("هُوَ يَعُودُ عَلَى لَبِيدٍ", "«he» — Labīd", "Lebîd'e dönen gizli «o»")),
  PR("عَلَى", "ala", n=MT("قَدِمَ", "came", "geldi»ye")),
  R("majr", "رَسُولِ", "rasul", mud=True),
  R("mdf", "اللهِ", "allah", pos="propn", n=(" — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl")),
  V("ma", "صَلَّى", "salla", g=["form-ii-verbs", "naqis-verbs", "khabar-fi-mana-al-insha", "jumla-mutarida"], n=(" — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ: خَبَرٌ لَفْظًا إِنْشَاءٌ مَعْنًى", " — a parenthetical prayer with no seat of its own: a report in form, a request in meaning", " — i'râbdan mahalli olmayan dua cümlesi (mu'tarıza): lafzen haber, mânen inşâ")),
  R("fail", "اللهُ", "allah", pos="propn"),
  JP("عَلَيْهِ", "ala", "هِ", n=MT("صَلَّى", "bless", "salât eylesin»e")),
  V("m", "وَسَلَّمَ", "sallama", c="w", g=["form-ii-verbs"], doer=DZ("هُوَ يَعُودُ عَلَى اللهِ", "«He» — God", "Allah'a dönen gizli «O»")),
  PR("فِي", "fi", n=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «قَدِمَ»", "; the phrase hangs on an omitted hal of the doer of «came»: «being among …»", "; câr-mecrûr «geldi»nin fâilinden mahzûf bir hâle müteallik")),
  R("majr", "وَفْدِ", "lb-wafd", mud=True),
  R("mdf", "بَنِي", "banu", mud=True, sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " by the ya — it is treated as a sound masculine plural, and its nun drops for the idafa", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"]),
  R("mdf", "كِلَابٍ", "lb-kilab", pos="propn", n=(" — كِلَابُ بْنُ رَبِيعَةَ بْنِ عَامِرِ بْنِ صَعْصَعَةَ، وَلَبِيدٌ مِنْ وَلَدِهِ", " — Kilāb ibn Rabīʿa of ʿĀmir ibn Ṣaʿṣaʿa; Labīd is of his line", " — Kilâb b. Rebîa (Âmir b. Sa'saa'dan); Lebîd onun soyundandır"), p="،"),
  V("mw", "فَأَسْلَمُوا", "aslama", c="f", g=["form-iv-verbs"], n=(" — يَعُودُ عَلَى الْوَفْدِ", " — «they» are the delegation", " — zamir heyete döner")),
  V("mw", "وَرَجَعُوا", "rajaa", c="w"),
  PR("إِلَى", "ila", n=MT("رَجَعُوا", "went back", "döndüler»e")),
  R("majr", "بِلَادِهِمْ", "bilad", enc="هِمْ", g=["jam-taksir"], p=".")]})
S1.append({"id": "s2", "translation": {
  "en": "Then Labīd came to Kufa, and his sons with him;",
  "tr": "Sonra Lebîd, oğullarıyla birlikte Kûfe'ye geldi;"},
 "tokens": [T("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with an interval.", "Tertîb ve terâhî bildiren atıf harfi."),
  V("m", "قَدِمَ", "qadima"),
  LABID_F(),
  R("maf", "الْكُوفَةَ", "kufa", pos="propn", n=(" — وَ«قَدِمَ» يَتَعَدَّى إِلَى الْمَكَانِ بِنَفْسِهِ: قَدِمَ الْبَلَدَ", " — «to come to» takes the place directly as its object", " — «kadime» fiili mekânı doğrudan mef'ûl alır")),
  T("وَبَنُوهُ", "banu", "noun", ["atf-nasaq", "jam-mudhakkar-salim", "idafa-definiteness", "al-bariz-al-muttasil"],
     WA_AR + "بَنُو مَعْطُوفٌ عَلَى «لَبِيدٌ» مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَجَازَ الْعَطْفُ عَلَى الْفَاعِلِ بَعْدَ الْمَفْعُولِ لِلْفَصْلِ بِهِ.",
     "The waw conjoins; «his sons» is joined to «Labīd», in raf' by the waw — it is treated as a sound masculine plural, its nun dropped for the idafa — and the attached «his» is in the seat of jarr. The object standing between makes the late conjoining to the doer smooth.",
     "«ve» + «oğulları»: «Lebîd»e ma'tûf; cem-i müzekker sâlime mülhak olduğu için vâv ile merfû, nûnu izâfetle düşmüştür; bitişik zamir muzâfun ileyh, mahallen mecrûr. Araya mef'ûl girdiği için fâile sonradan atıf güzel düşer.",
     p="،", segs=SG(("وَ", "wa", "conj"), ("بَنُو", "banu", "noun"), ("هُ", "pron-3ms", "pron")))]})
S1.append({"id": "s3", "translation": {
  "en": "then his sons went back to the desert after that,",
  "tr": "bundan sonra oğulları çöle döndü,"},
 "tokens": [V("m", "فَرَجَعَ", "rajaa", c="f"),
  T("بَنُوهُ", "banu", "noun", ["fail", "jam-mudhakkar-salim", "idafa-definiteness", "al-bariz-al-muttasil"],
     "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "The doer, in raf' by the waw — treated as a sound masculine plural, its nun dropped for the idafa; the attached «his» is in the seat of jarr.",
     "Fâil; cem-i müzekker sâlime mülhak olduğu için vâv ile merfû, nûnu izâfetle düşmüştür; bitişik zamir muzâfun ileyh, mahallen mecrûr.",
     segs=SG(("بَنُو", "banu", "noun"), ("هُ", "pron-3ms", "pron"))),
  PR("إِلَى", "ila", n=MT("رَجَعَ", "went back", "döndü»ye")),
  R("majr", "الْبَادِيَةِ", "badiya"),
  R("zarfz", "بَعْدَ", "bada", mud=True, n=(" — مُتَعَلِّقٌ بِـ«رَجَعَ»؛ وَ«بَعْدَ ذٰلِكَ» بَيْنَ قَوْسَيْنِ فِي الْمَطْبُوعِ", " — it hangs on «went back»; the edition prints «after that» between brackets", " — «döndü»ye müteallik; «bundan sonra» ibaresi matbûda parantez içindedir")),
  T("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "idafa-definiteness"],
     "ذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
     "ذَا is the demonstrative, built on sukun, in the seat of jarr as the second term of the idafa; the lam marks distance and the kaf is the letter of address.",
     "«zâ» işaret ismi, sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr; lâm uzaklık, kâf hitap harfidir.", p="،")]})
S1.append({"id": "s4", "translation": {
  "en": "and Labīd stayed on until he died there,",
  "tr": "Lebîd ise orada ölünceye kadar kaldı,"},
 "tokens": [V("m", "فَأَقَامَ", "aqama", c="f", g=["form-iv-verbs", "hollow-verbs"]),
  LABID_F(),
  PR("إِلَى", "ila", n=(" — لِانْتِهَاءِ الْغَايَةِ، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ مَجْرُورٌ بِهِ، وَهُمَا مُتَعَلِّقَانِ بِـ«أَقَامَ»", " of the end-point; the masdar built by what follows is in jarr after it, and the phrase hangs on «stayed»", " — intihâ-i gâye içindir; sonraki müevvel masdar onunla mecrûr, ikisi «kaldı»ya müteallik")),
  T("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ لَا عَمَلَ لَهُ فِي الْمَاضِي لَفْظًا.", "The masdar-making particle; before a past verb it changes nothing in wording.", "Masdar harfi; mâzî fiilde lafzen amel etmez."),
  V("m", "مَاتَ", "mata-die", g=["hollow-verbs"], doer=DZ("هُوَ يَعُودُ عَلَى لَبِيدٍ", "«he» — Labīd", "Lebîd'e dönen gizli «o»"), n=(" — وَ«أَنْ» وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ: إِلَى مَوْتِهِ", " — أَنْ and the verb stand for a masdar: «until his death»", " — «en» ile fiil masdar te'vîlindedir: «ölümüne kadar»")),
  JP("بِهَا", "bi", "هَا", n=(" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالضَّمِيرُ لِلْكُوفَةِ؛ مُتَعَلِّقَانِ بِـ«مَاتَ»", " — the ba means «in», and «it» is Kufa; the phrase hangs on «died»", " — bâ «-de» anlamındadır, zamir Kûfe'ye döner; «öldü»ye müteallik"), p="،")]})
S1.append({"id": "s5", "translation": {
  "en": "and he was buried in the open ground of the Banū Jaʿfar ibn Kilāb.",
  "tr": "ve Benî Ca'fer b. Kilâb'ın sahrasına defnedildi."},
 "tokens": [V("m", "فَدُفِنَ", "dafana", c="f", pas=True, doer=DZ("هُوَ يَعُودُ عَلَى لَبِيدٍ", "«he» — Labīd", "Lebîd'e dönen gizli «o»")),
  PR("فِي", "fi", n=MT("دُفِنَ", "was buried", "defnedildi»ye")),
  R("majr", "صَحْرَاءِ", "sahra", mud=True, g=["ism-mamdud"], n=(" — وَجُرَّ بِالْكَسْرَةِ مَعَ أَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ لِأَنَّهُ مُضَافٌ", " — it takes the kasra, though it ends in the long feminine alif, because it is annexed", " — elif-i memdûde ile bittiği hâlde muzâf olduğu için kesre ile mecrûr")),
  R("mdf", "بَنِي", "banu", mud=True, sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", " by the ya, its nun dropped for the idafa", " — yâ ile; nûnu izâfet sebebiyle düşmüştür"), g=["jam-mudhakkar-salim"]),
  R("mdf", "جَعْفَرِ", "jafar", pos="propn", n=(" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْن» مُضَافًا إِلَى عَلَمٍ؛ وَهُمْ رَهْطُ لَبِيدٍ", " — its tanwin drops because the name is described by «son of» + a name; they are Labīd's own clan", " — «ibn» ile vasıflanıp bir aleme muzâf olduğu için tenvini düşer; bunlar Lebîd'in kendi boyudur")),
  R("naatj", "بْنِ", "ibn-bn", mud=True, n=(" — وَحُذِفَتْ أَلِفُهُ لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ", " — its alif is dropped because it stands between two names", " — iki alem arasında olduğu için elifi yazılmaz")),
  R("mdf", "كِلَابٍ", "lb-kilab", pos="propn", p=".")]})
S1.append({"id": "s6", "translation": {
  "en": "It is said that his death fell at the beginning of Muʿāwiya's caliphate,",
  "tr": "Vefatının Muâviye'nin hilâfetinin başında olduğu söylenir,"},
 "tokens": [V("d", "وَيُقَالُ", "qala", c="wi", pas=True, g=["hollow-verbs"], n=(" — وَنَائِبُ الْفَاعِلِ جُمْلَةُ «إِنَّ وَفَاتَهُ …» عَلَى الْحِكَايَةِ", " — its deputy doer is the quoted sentence «his death was …»", " — nâib-i fâil, hikâye yoluyla «vefatı … idi» cümlesidir")),
  T("إِنَّ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — كُسِرَتْ هَمْزَتُهَا لِوُقُوعِهَا بَعْدَ الْقَوْلِ.", "The particle of emphasis that puts its noun in nasb — its hamza takes kasra because it follows «say».", "Te'kîd ve nasb harfi — kavlden sonra geldiği için hemzesi kesrelidir."),
  R("ismi", "وَفَاتَهُ", "lb-wafat", enc="هُ"),
  T("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
     "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْوَفَاةِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.",
     "كَانَ, the defective past verb, built on fatha, with the feminine ta; its noun is the hidden «she» — the death — and the clause is the predicate of إِنَّ, in the seat of raf'.",
     "Kâne: nâkıs mâzî, fetha üzere mebnî, tâ te'nîs içindir; ismi «vefat»a dönen gizli «o» — cümle inne'nin haberi, mahallen merfû."),
  PR("فِي", "fi", n=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «كَانَتْ»", "; the phrase hangs on the omitted predicate of كَانَتْ", "; câr-mecrûr «kânet»in mahzûf haberine müteallik")),
  R("majr", "أَوَّلِ", "awwal", mud=True),
  R("mdf", "خِلَافَةِ", "khilafa", mud=True),
  R("mdf", "مُعَاوِيَةَ", "lb-muawiya", pos="propn", g=["mamnu-min-sarf"], sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", " by the fatha in place of the kasra: a proper name with the feminine ta, barred from tanwin", " — fetha ile: lafzî te'nîsli özel isim, gayr-i munsarif"), n=(" — مُعَاوِيَةُ بْنُ أَبِي سُفْيَانَ", " — Muʿāwiya ibn Abī Sufyān", " — Muâviye b. Ebî Süfyân"), p="،")]})
S1.append({"id": "s7", "translation": {
  "en": "and that he died at the age of a hundred and fifty-seven years.",
  "tr": "ve yüz elli yedi yaşında öldüğü (söylenir)."},
 "tokens": [T("وَأَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "atf-nasaq"],
     WA_AR + "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — هٰكَذَا فِي الْمَطْبُوعِ بِفَتْحِ الْهَمْزَةِ، وَمَا قَبْلَهُ «إِنَّ» بِكَسْرِهَا؛ فَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى نَائِبِ فَاعِلِ «يُقَالُ» عَلَى مَعْنَى: وَيُذْكَرُ أَنَّهُ.",
     "The waw conjoins; أَنَّ puts its noun in nasb, and the attached «he» is that noun — so the edition prints it, with fatha on the hamza, though إِنَّ before it has kasra; the masdar it builds is joined to the deputy doer of «it is said», in the sense «and it is reported that he …».",
     "«ve» + enne: te'kîd ve nasb harfi; bitişik zamir ismidir, mahallen mansûb — matbûda hemzenin fethasıyla böyledir, önceki ise kesreli «inne»dir; müevvel masdar «denir»in nâib-i fâiline ma'tûftur: «ve onun … olduğu zikredilir» anlamında.",
     segs=SG(("وَ", "wa", "conj"), ("أَنَّ", "anna", "part"), ("هُ", "pron-3ms", "pron"))),
  V("m", "مَاتَ", "mata-die", g=["hollow-verbs"], doer=DZ("هُوَ", "«he»", "gizli «o»"), n=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", " — the clause is the predicate of أَنَّ, in the seat of raf'", " — cümle enne'nin haberi, mahallen merfû")),
  T("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "hal", "al-hal-jumla-wa-rabituha", "anwa-al-waw"],
     "الْوَاوُ وَاوُ الْحَالِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «مَاتَ».",
     "The waw of hal; هُوَ is a detached pronoun built on fatha, in the seat of raf' as mubtada — the nominal clause is a hal of the doer of «died», in the seat of nasb.",
     "Vâv hâliyyedir; «hüve» fetha üzere mebnî munfasıl zamir, mübtedâ olarak mahallen merfû — isim cümlesi «öldü»nün fâilinden hâl, mahallen mansûb.",
     segs=SG(("وَ", "wa", "conj"), ("هُوَ", "huwa", "pron"))),
  R("khb", "ابْنُ", "ibn", mud=True, n=(" — «ابْنُ كَذَا سَنَةً»: بَلَغَ ذٰلِكَ مِنَ الْعُمُرِ", " — «the son of so many years»: one who has reached that age", " — «şu kadar yılın oğlu»: o yaşa ulaşmış kimse")),
  R("mdf", "مِائَةٍ", "mia", g=["asma-al-adad-fil-kafiya"]),
  R("atfj", "وَسَبْعٍ", "sab-seven", c="w", g=["asma-al-adad-fil-kafiya"]),
  R("atfj", "وَخَمْسِينَ", "khamsun", c="w", g=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign=("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", " by the ya — the tens decline like the sound masculine plural", " — cem-i müzekker sâlime mülhak olduğu için yâ ile")),
  T("سَنَةً", "sana", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"],
     "تَمْيِيزُ الْعَدَدِ «مِائَةٍ وَسَبْعٍ وَخَمْسِينَ» مَنْصُوبٌ بِالْفَتْحَةِ.", "The tamyiz (specifier) of the number «a hundred and fifty-seven», in nasb.", "«Yüz elli yedi» sayısının temyîzi, mansûb.", p=".")]})
CH[1] = S1

# =====================================================================================================================
# The poem — every verse of al-Zawzanī's recension, filed by his number
# =====================================================================================================================
VERSES = {}
def VV(n, en, tr, first, second):
    """one verse = one sentence: «•» closes the first hemistich, a full stop the verse"""
    first, second = [t for t in first if t], [t for t in second if t]
    first[-1]["punctAfter"] = "•"
    second[-1].setdefault("punctAfter", ".")
    assert n not in VERSES, n
    VERSES[n] = {"id": "v%d" % n, "translation": {"en": en, "tr": tr}, "tokens": first + second}
DIYAR = DZ("هِيَ يَعُودُ عَلَى الدِّيَارِ", "«she» — the dwellings", "«diyâr»a dönen gizli «o»")

# ---- vv. 1–7 — الدِّيَارُ الْعَافِيَةُ ----
VV(1, "The dwellings are effaced — the places of brief halt and the places of long stay — at Minā; its Ghawl and its Rijām have gone wild.",
  "Minâ'daki yurtlar — kısa konak yerleri de uzun ikamet yerleri de — silinip gitti; oranın Gavl'i de Ricâm'ı da ıssızlaşıp yabanileşti.",
 [T("عَفَتِ", "afa", "verb", ["naqis-verbs", "al-lazim-wal-mutaaddi", "ilm-al-arud"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَعَفَا لَازِمٌ وَمُتَعَدٍّ، وَهُوَ فِي الْبَيْتِ لَازِمٌ: دَرَسَ وَانْمَحَى (الزَّوْزَنِيُّ). وَالْقَصِيدَةُ مِنَ الْبَحْرِ الْكَامِلِ: «مُتَفَاعِلُنْ» سِتَّ مَرَّاتٍ.",
     "Past verb built on a fatha estimated on the alif, which has dropped where two quiescents met; the feminine ta takes kasra before the ال. عَفَا is both intransitive and transitive, and here intransitive: «to be effaced» (al-Zawzanī). The ode is in the metre al-kāmil — مُتَفَاعِلُنْ six times.",
     "İki sâkinin karşılaşması sebebiyle düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; te'nîs tâ'sı da iki sâkin karşılaştığı için kesre ile harekelenmiştir. «Afâ» hem lâzım hem müteaddîdir; beyitte lâzımdır: «silindi, izi kalmadı» (Zevzenî). Kaside kâmil bahrindendir: altı kere «mütefâilün»."),
  R("fail", "الدِّيَارُ", "dar", g=["jam-taksir"], n=(" — جَمْعُ دَارٍ؛ وَالْجُمْلَةُ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", " — the plural of دَار; the sentence opens the ode and has no seat", " — «dâr»ın cem'i; cümle ibtidâiyyedir, i'râbdan mahalli yoktur")),
  R("bdlr", "مَحَلُّهَا", "mahall", enc="هَا", g=["al-badal-wa-aqsamuh-wa-atf-al-bayan", "tibaq"], n=(" — بَدَلُ بَعْضٍ مِنْ كُلٍّ مِنَ «الدِّيَارُ». وَالْمَحَلُّ مِنَ الدِّيَارِ: مَا حُلَّ فِيهِ لِأَيَّامٍ مَعْدُودَةٍ (الزَّوْزَنِيُّ)", " — a badal of part for whole, from «the dwellings». الْمَحَلّ is the part of an encampment where one halts for a few days (al-Zawzanī)", " — «diyâr»dan bedel-i ba'z mine'l-küll. «Mahall»: yurdun birkaç günlüğüne konulan yeri (Zevzenî)")),
  R("atfr", "فَمُقَامُهَا", "lb-muqam", c="f", enc="هَا", g=["tibaq"], n=N3(ZW("وَالْمُقَامُ مِنْهَا: مَا طَالَتِ الْإِقَامَةُ بِهِ", "الْمُقَام is the part where the stay was long", "«mukâm»: uzun süre kalınan yer"), HADD("طِبَاقٌ بَيْنَ «مَحَلُّهَا» وَ«مُقَامُهَا»، وَالتَّقَابُلُ فِي تَفْسِيرِ الزَّوْزَنِيِّ: مَا كَانَ لِلْحُلُولِ دُونَ الْإِقَامَةِ وَمَا كَانَ لِلْإِقَامَةِ", "«their halting-place» and «their abode» make a tibaq; the opposition is in al-Zawzanī's gloss: what was for alighting only, not for staying, and what was for staying", "«mahall» ile «mukâm» arasında tıbâk vardır; karşıtlık Zevzenî'nin açıklamasındadır: ikamet için değil yalnız konmak için olan ve ikamet için olan")))],
 [R("majr", "بِمِنًى", "lb-mina", j="bi", pos="propn", g=["ism-maqsur-manqus"], sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", " — by a kasra estimated on the alif", " — elif üzerinde takdîrî kesre ile"), n=N3((" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَفَتْ»، أَوْ بِمَحْذُوفٍ حَالٍ مِنَ «الدِّيَارُ» (الدُّرَّةُ)", " — the ba means «in»; the phrase hangs on «are effaced», or on an omitted hal of «the dwellings» (al-Durra)", " — bâ «-de» anlamındadır; câr-mecrûr «silindi»ye yahut «diyâr»dan mahzûf bir hâle müteallik (Dürre)"), ZW("مَوْضِعٌ بِحِمَى ضَرِيَّةَ غَيْرُ مِنَى الْحَرَمِ، وَهُوَ يَنْصَرِفُ وَلَا يَنْصَرِفُ، وَقَدْ صُرِفَ هُنَا", "a place in the reserve of Ḍariyya, not the Minā of the Sanctuary; the name is found with tanwin and without, and has it here", "Dariyye korusunda bir yer; Harem'deki Minâ değildir; munsarif de gayr-i munsarif de kullanılır, burada munsariftir"))),
  V("m", "تَأَبَّدَ", "lb-taabbada", g=["form-v-verbs", "al-hal-jumla-wa-rabituha"], n=N3(ZW("تَأَبَّدَ: تَوَحَّشَ", "تَأَبَّدَ: it went wild, was left to the wild beasts", "«teebbede»: yabanileşti, vahşi hayvanlara kaldı"), (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الدِّيَارُ» بِتَقْدِيرِ «قَدْ»، وَالرَّابِطُ الضَّمِيرُ (الدُّرَّةُ)", " — the clause is a hal of «the dwellings», in the seat of nasb, with قَدْ understood; the pronoun ties it (al-Durra)", " — cümle, «kad» takdiriyle «diyâr»dan hâl, mahallen mansûb; râbıt zamirdir (Dürre)"))),
  R("fail", "غَوْلُهَا", "lb-ghawl", enc="هَا", pos="propn", g=["hadhf-al-mudaf-wal-mudaf-ilayh", "ijaz-al-hadhf"], n=ZW("الْغَوْلُ وَالرِّجَامُ جَبَلَانِ مَعْرُوفَانِ، وَالضَّمِيرُ لِلدِّيَارِ؛ أَيْ: تَأَبَّدَتْ دِيَارُ غَوْلِهَا وَدِيَارُ رِجَامِهَا، فَحُذِفَ الْمُضَافُ — وَهُوَ إِيجَازٌ بِالْحَذْفِ", "al-Ghawl and al-Rijām are two well-known mountains, and «its» is the dwellings; that is, «the dwellings of its Ghawl and of its Rijām went wild», with the first term of the idafa left out — brevity by omission", "Gavl ile Ricâm bilinen iki dağdır, zamir yurtlara döner; yani «Gavl'indeki ve Ricâm'ındaki yurtlar yabanileşti»; muzâf hazfedilmiştir — hazif yoluyla îcâz")),
  R("atfr", "فَرِجَامُهَا", "lb-rijam", c="f", enc="هَا", pos="propn", g=["al-qafiya"], n=RHYME)])
VV(2, "And the torrent-beds of al-Rayyān: their trace is laid bare, worn — as the stones there hold their writing.",
  "Reyyân dağının sel yatakları da öyle: izleri, eskimiş hâlde, çırılçıplak ortaya çıkmıştır — tıpkı oradaki taşların yazıları saklaması gibi.",
 [R("mub", "فَمَدَافِعُ", "lb-madfa", c="f", mud=True, g=["jam-taksir"], n=N3(ZW("الْمَدَافِعُ: أَمَاكِنُ يَنْدَفِعُ عَنْهَا الْمَاءُ مِنَ الرُّبَى، الْوَاحِدُ مَدْفَعٌ؛ وَهُوَ عِنْدَهُ مَعْطُوفٌ عَلَى «غَوْلُهَا»", "مَدَافِع are the places on high ground from which water runs off, singular مَدْفَع; he takes the word as joined to «its Ghawl»", "«medâfi'»: yüksek yerlerden suyun akıp gittiği yerler, tekili «medfa'»; ona göre kelime «Gavl'i»ne ma'tûftur"), (" — وَقَدَّمَ الدُّرَّةُ أَنَّهُ مُبْتَدَأٌ خَبَرُهُ جُمْلَةُ «عُرِّيَ رَسْمُهَا»، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا، وَهُوَ الْمُثْبَتُ هُنَا", " — al-Durra gives first that it is a mubtada whose khabar is the clause «their trace is laid bare», the sentence being joined to the one before; that is the reading written here", " — Dürre ise önce, onun mübtedâ, «izleri çıplak bırakıldı» cümlesinin haber olduğunu ve cümlenin öncekine atfedildiğini söyler; burada bu yazılmıştır"))),
  R("mdf", "الرَّيَّانِ", "lb-rayyan", pos="propn", n=ZW("جَبَلٌ مَعْرُوفٌ", "a well-known mountain", "bilinen bir dağ")),
  V("m", "عُرِّيَ", "arra", pas=True, g=["form-ii-verbs", "naqis-verbs", "anwa-al-khabar"], n=N3(ZW("التَّعْرِيَةُ مَصْدَرُ عَرَّيْتُهُ فَعَرِيَ؛ وَإِنَّمَا عَرَّاهَا السُّيُولُ", "تَعْرِيَة is to strip a thing bare; it is the torrents that stripped them", "«ta'riye»: bir şeyi soyup çıplak bırakmak; onları soyan sellerdir"), (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", " — the clause is the khabar, in the seat of raf'", " — cümle mübtedânın haberi, mahallen merfû"))),
  R("naib", "رَسْمُهَا", "rasm", enc="هَا")],
 [R("hal", "خَلَقًا", "lb-khalaq", n=ZW("حَالٌ مِنْ «رَسْمُهَا» وَالْعَامِلُ فِيهِ «عُرِّيَ»؛ وَالْخَلَقُ: الْبَالِي", "a hal of «their trace», governed by «is laid bare»; خَلَق is «worn, threadbare»", "«izleri»nden hâl, âmili «çıplak bırakıldı»; «halak»: eskimiş, yıpranmış")),
  T("كَمَا", "ka", "prep", ["huruf-jarr", "anwa-ma", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
     "الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَمَا مَصْدَرِيَّةٌ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «مَا ضَمِنَ» مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ: عُرِّيَ تَعْرِيَةً كَتَضْمِينِ الْحِجَارَةِ الْكِتَابَةَ (الدُّرَّةُ) — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ بَقَاءُ الرَّسْمِ عَلَى قِدَمِ الْأَيَّامِ، وَالْمُشَبَّهُ بِهِ بَقَاءُ الْكِتَابِ فِي الْحَجَرِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ — وَهُوَ الثَّبَاتُ وَالْبَقَاءُ — غَيْرُ مَذْكُورٍ. قَالَ الزَّوْزَنِيُّ: شَبَّهَ بَقَاءَ الْآثَارِ لِقِدَمِ الْأَيَّامِ بِبَقَاءِ الْكِتَابِ فِي الْحَجَرِ.",
     "The kaf is the jarr letter of likening and مَا is masdar-making; the masdar built from «as … hold» is in jarr by the kaf, and the phrase hangs on an omitted na't of an omitted maf'ul mutlaq: «laid bare as stones are made to hold writing» (al-Durra). It is a tashbih mursal mujmal: the thing likened is the trace lasting on through the long years, the thing it is likened to is writing lasting in stone, the particle is the kaf, and the point of likeness — lasting — is not stated. Al-Zawzanī: «he likens the traces' lasting, old as they are, to writing lasting in stone».",
     "Kâf teşbîh ve cer harfi, «mâ» masdariyyedir; «mâ damine»den müevvel masdar kâf ile mecrûrdur; câr-mecrûr mahzûf bir mef'ûl-i mutlakın mahzûf na'tına mütealliktir: «taşların yazıyı içinde tutması gibi bir çıplak bırakılışla» (Dürre). Burada teşbîh-i mürsel mücmel vardır: müşebbeh, izin uzun zamana rağmen kalması; müşebbehün bih, yazının taşta kalması; edat kâf; vech-i şebeh — sebat ve kalıcılık — zikredilmemiştir. Zevzenî: «eserlerin, günlerin eskiliğine rağmen kalışını yazının taşta kalışına benzetti».",
     segs=SG(("كَ", "ka", "prep"), ("مَا", "ma-masdariyya", "part"))),
  V("m", "ضَمِنَ", "damina", n=(" — وَالْفَاعِلُ «سِلَامُهَا» مُؤَخَّرٌ عَنِ الْمَفْعُولِ", "; its doer, «its stones», comes after the object", "; fâili «taşları» mef'ûlden sonraya bırakılmıştır")),
  R("maf", "الْوُحِيَّ", "lb-wahy", g=["jam-taksir"], n=ZW("مُقَدَّمٌ عَلَى الْفَاعِلِ. الْوَحْيُ: الْكِتَابَةُ وَالْكِتَابُ، وَالْجَمْعُ الْوُحِيُّ", "placed before the doer. وَحْي is writing, an inscription; its plural is وُحِيّ", "fâilden öne alınmıştır. «Vahy»: yazı, kitâbe; cem'i «vuhiyy»")),
  R("fail", "سِلَامُهَا", "lb-silam", enc="هَا", g=["jam-taksir"], n=ZW("السِّلَامُ: الْحِجَارَةُ، وَالْوَاحِدَةُ سَلِمَةٌ بِكَسْرِ اللَّامِ؛ وَالضَّمِيرُ الْمُضَافُ إِلَيْهِ عَائِدٌ إِلَى «الْوُحِيِّ»", "سِلَام are stones, singular سَلِمَة with kasra on the lam; the pronoun it is annexed to returns to «the writings»", "«silâm»: taşlar, tekili lâmın kesresiyle «selime»; muzâfun ileyh olan zamir «yazılar»a döner"))])
VV(3, "Blackened traces: since their people were last there, whole years have run out and passed — their free months and their sacred months.",
  "Kararmış yurt kalıntıları: sakinleriyle son buluşmalarından beri nice yıllar — helâl aylarıyla, haram aylarıyla — dolup geçmiştir.",
 [R("khb", "دِمَنٌ", "dimna", g=["jam-taksir", "hadhf-wa-taqdir"], n=N3((" — لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ (الدُّرَّةُ)", " — of an omitted mubtada, «they are» (al-Durra)", " — mahzûf mübtedânın haberi: «onlar» (Dürre)"), ZW("أَيْ هِيَ آثَارُ دِيَارٍ؛ جَمْعُ دِمْنَةٍ", "that is, «they are the traces of dwellings»; the plural of دِمْنَة", "yani «onlar yurt kalıntılarıdır»; «dimne»nin cem'i"))),
  V("m", "تَجَرَّمَ", "lb-tajarrama", g=["form-v-verbs", "jumla-sifa"], n=N3(ZW("التَّجَرُّمُ: التَّكَمُّلُ وَالِانْقِطَاعُ، يُقَالُ: تَجَرَّمَتِ السَّنَةُ", "تَجَرُّم is to be completed and to come to an end, as one says of a year", "«tecerrüm»: tamamlanıp sona ermek; yıl için söylenir"), (" — وَالْفَاعِلُ «حِجَجٌ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«دِمَنٌ»", " — its doer is «years»; the clause is a na't of «traces», in the seat of raf'", " — fâili «yıllar»dır; cümle «dimen»in na'tı, mahallen merfû"))),
  R("zarfz", "بَعْدَ", "bada", mud=True, n=(" — مُتَعَلِّقٌ بِـ«تَجَرَّمَ»", " — it hangs on «have run out»", " — «dolup geçti»ye müteallik")),
  R("mdf", "عَهْدِ", "ahd", mud=True, g=["masdar"], n=ZW("الْعَهْدُ: اللِّقَاءُ", "عَهْد here is «meeting, being with»", "«ahd»: burada buluşma, bir arada olma")),
  R("mdf", "أَنِيسِهَا", "anis", enc="هَا", n=(" — أَيْ سُكَّانِهَا", " — its people, those who lived there", " — yani orada oturanlar"))],
 [R("fail", "حِجَجٌ", "hijja-year", g=["jam-taksir"], n=ZW("جَمْعُ حِجَّةٍ وَهِيَ السَّنَةُ", "the plural of حِجَّة, a year", "«hicce»nin cem'i: yıl")),
  V("mn", "خَلَوْنَ", "khala", g=["naqis-verbs", "jumla-sifa"], n=N3(ZW("الْخُلُوُّ: الْمُضِيُّ، وَمِنْهُ الْأُمَمُ الْخَالِيَةُ؛ وَالْمُضْمَرُ رَاجِعٌ إِلَى الْحِجَجِ", "خُلُوّ is «passing away», as in «the nations that have passed»; the pronoun returns to the years", "«hulüvv»: geçip gitmek; zamir yıllara döner"), (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«حِجَجٌ»", " — the clause is a na't of «years», in the seat of raf'", " — cümle «yıllar»ın na'tı, mahallen merfû"))),
  R("bdlr", "حَلَالُهَا", "halal", enc="هَا", g=["al-badal-wa-aqsamuh-wa-atf-al-bayan", "tibaq"], n=ZW("بَدَلٌ مِنَ «حِجَجٌ» — وَهُوَ بَدَلُ بَعْضٍ مِنْ كُلٍّ عِنْدَ الدُّرَّةِ — وَأَرَادَ بِالْحَلَالِ أَشْهُرَ الْحِلِّ", "a badal of «years» — of part for whole, says al-Durra; by «the free» he means the months in which fighting is free", "«yıllar»dan bedel — Dürre'ye göre bedel-i ba'z mine'l-küll; «helâl» ile hill aylarını kasteder")),
  R("atfr", "وَحَرَامُهَا", "haram", c="w", enc="هَا", g=["tibaq"], n=N3(ZW("وَبِالْحَرَامِ الْأَشْهُرَ الْحُرُمَ؛ وَالسَّنَةُ لَا تَعْدُو أَشْهُرَ الْحُرُمِ وَأَشْهُرَ الْحِلِّ، فَعَبَّرَ عَنْ مُضِيِّ السَّنَةِ بِمُضِيِّهِمَا", "and by «the sacred» the sacred months; a year is nothing but the two, so he speaks of the year's passing by the passing of both", "«haram» ile de haram ayları kasteder; yıl bu ikisinden ibarettir, bu yüzden yılın geçişini ikisinin geçişiyle ifade etmiştir"), HADD("طِبَاقٌ بَيْنَ «حَلَالُهَا» وَ«حَرَامُهَا»: اسْمَانِ مُتَضَادَّانِ", "«their free» and «their sacred» make a tibaq: two nouns that are opposites", "«helâli» ile «haramı» arasında tıbâk vardır: zıt iki isim")))])
VV(4, "They were given the rains of the spring stars, and the rain of the thunder-clouds fell on them — the downpour and the soft showers.",
  "Bu yurtlara bahar yıldızlarının yağmurları nasip oldu; gök gürültülü bulutların yağmuru — sağanağı da çisentisi de — üzerlerine düştü.",
 [V("mt", "رُزِقَتْ", "razaqa", pas=True, g=["mafulayn"], doer=DZ("هِيَ يَعُودُ عَلَى الدِّيَارِ وَالدِّمَنِ، وَهُوَ الْمَفْعُولُ الْأَوَّلُ فِي الْأَصْلِ", "«she» — the dwellings and their traces — which was the first object", "yurtlara ve kalıntılara dönen gizli «o»; aslında birinci mef'ûldür")),
  R("maf", "مَرَابِيعَ", "lb-mirba", mud=True, g=["mafulayn", "mamnu-min-sarf", "jam-taksir", "hadhf-al-mudaf-wal-mudaf-ilayh"], n=N3((" — وَهُوَ الْمَفْعُولُ الثَّانِي، مَمْنُوعٌ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ", " — the second object; a «farthest plural», barred from tanwin", " — ikinci mef'ûl; muntehe'l-cumû' vezninde olduğu için gayr-i munsarif"), ZW("مَرَابِيعُ النُّجُومِ: الْأَنْوَاءُ الرَّبِيعِيَّةُ، الْوَاحِدُ مِرْبَاعٌ؛ وَالْمَعْنَى: رُزِقَتْ أَمْطَارَ الْأَنْوَاءِ الرَّبِيعِيَّةِ — عَلَى تَقْدِيرِ مُضَافٍ", "مَرَابِيعُ النُّجُومِ are the star-settings of spring that bring rain, singular مِرْبَاع; the sense is «they were given the rains of the spring stars», a first term of the idafa being understood", "«merâbîu'n-nücûm»: yağmur getiren bahar nev'leri, tekili «mirbâ'»; mâna: «bahar nev'lerinin yağmurları nasip oldu» — bir muzâf takdir edilir"))),
  R("mdf", "النُّجُومِ", "najm", g=["jam-taksir"]),
  V("m", "وَصَابَهَا", "lb-saba", c="w", enc="هَا", g=["hollow-verbs"], n=ZW("الصَّوْبُ: الْإِصَابَةُ، يُقَالُ: صَابَهُ أَمْرُ كَذَا وَأَصَابَهُ بِمَعْنًى", "صَوْب is «to hit, to reach»: صَابَهُ and أَصَابَهُ mean the same", "«savb»: isabet etmek; «sâbehû» ile «esâbehû» aynı mânadadır"))],
 [R("fail", "وَدْقُ", "lb-wadq", mud=True, n=ZW("الْوَدْقُ: الْمَطَرُ", "وَدْق is rain", "«vedk»: yağmur")),
  R("mdf", "الرَّوَاعِدِ", "lb-raida", g=["jam-taksir"], n=ZW("ذَوَاتُ الرَّعْدِ مِنَ السَّحَابِ، وَاحِدَتُهَا رَاعِدَةٌ", "the clouds that carry thunder, singular رَاعِدَة", "gök gürültülü bulutlar, tekili «râide»")),
  R("bdlr", "جَوْدُهَا", "lb-jawd", enc="هَا", g=["al-badal-wa-aqsamuh-wa-atf-al-bayan"], n=N3((" — بَدَلُ بَعْضٍ مِنْ كُلٍّ مِنْ «وَدْقُ الرَّوَاعِدِ» (الدُّرَّةُ)", " — a badal of part for whole, from «the rain of the thunder-clouds» (al-Durra)", " — «gök gürültülü bulutların yağmuru»ndan bedel-i ba'z mine'l-küll (Dürre)"), ZW("الْجَوْدُ: الْمَطَرُ التَّامُّ الْعَامُّ", "جَوْد is the full, wide-spread rain", "«cevd»: bol ve her yeri tutan yağmur"))),
  R("atfr", "فَرِهَامُهَا", "lb-rihma", c="f", enc="هَا", g=["jam-taksir"], n=ZW("الرِّهَامُ: جَمْعُ رِهْمَةٍ وَهِيَ الْمَطْرَةُ الَّتِي فِيهَا لِينٌ", "رِهَام is the plural of رِهْمَة, a soft, gentle shower", "«rihâm»: «rihme»nin cem'i; yumuşak, ince yağmur"))])
VV(5, "— from every cloud that comes by night, and every morning cloud that darkens the sky, and every evening cloud whose rumblings answer one another.",
  "— geceleyin gelen her buluttan, sabahleyin gelip ufku karartan her buluttan ve gürlemeleri birbirine cevap veren her akşam bulutundan.",
 [PR("مِنْ", "min", n=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«صَابَهَا» فِي الْبَيْتِ قَبْلَهُ، وَيَجُوزُ الْقَطْعُ عَلَى أَنَّهُمَا خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ (الدُّرَّةُ)؛ وَفَسَّرَ بِهِ تِلْكَ الْأَمْطَارَ (الزَّوْزَنِيُّ)", "; the phrase hangs on «fell on them» in the verse before, or it may be cut off as the khabar of an omitted mubtada (al-Durra); with it he explains those rains (al-Zawzanī)", "; câr-mecrûr önceki beyitteki «üzerlerine düştü»ye mütealliktir; kat' ile mahzûf bir mübtedânın haberi de olabilir (Dürre); bununla o yağmurları açıklar (Zevzenî)")),
  R("majr", "كُلِّ", "kull", mud=True),
  R("mdf", "سَارِيَةٍ", "lb-sariya", g=["ism-fail", "hadhf-wa-taqdir"], n=ZW("صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: السَّارِيَةُ السَّحَابَةُ الْمَاطِرَةُ لَيْلًا", "a quality whose noun is left out: سَارِيَة is the cloud that rains by night", "mevsûfu hazfedilmiş sıfat: «sâriye», geceleyin yağan bulut")),
  R("atfj", "وَغَادٍ", "lb-ghadin", c="w", g=["ism-fail", "ism-maqsur-manqus"], sign=("بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", " — by a kasra estimated on the ya, which has dropped before the tanwin", " — tenvin sebebiyle düşen yâ üzerinde takdîrî kesre ile"), n=(" — أَيْ سَحَابٍ غَادٍ يَأْتِي غُدْوَةً، فَلِذَا ذُكِّرَ (الدُّرَّةُ)", " — «a morning cloud», one that comes early in the day; hence the masculine (al-Durra)", " — yani sabah erken gelen bulut; bu yüzden müzekkerdir (Dürre)")),
  R("naatj", "مُدْجِنٍ", "lb-mudjin", g=["ism-fail"], n=ZW("الْمُدْجِنُ: الْمُلْبِسُ آفَاقَ السَّمَاءِ بِظَلَامِهِ لِفَرْطِ كَثَافَتِهِ", "مُدْجِن is the cloud so dense that it wraps the horizons in darkness", "«müdcin»: yoğunluğundan ufukları karanlığa bürüyen bulut"))],
 [R("atfj", "وَعَشِيَّةٍ", "ashiyya", c="w", g=["hadhf-al-mudaf-wal-mudaf-ilayh", "muraat-al-nazir"], n=N3((" — وَالْأَصْلُ: وَسَحَابِ عَشِيَّةٍ، فَحُذِفَ الْمُضَافُ (الدُّرَّةُ). جَمَعَ لَهَا أَمْطَارَ السَّنَةِ: أَمْطَارُ الشِّتَاءِ أَكْثَرُهَا لَيْلًا، وَالرَّبِيعِ غَدَاةً، وَالصَّيْفِ عَشِيًّا (الزَّوْزَنِيُّ)", " — properly «and the cloud of an evening», the first term left out (al-Durra). He gathers for the place the rains of the whole year: winter rain falls mostly by night, spring rain in the morning, summer rain at evening (al-Zawzanī)", " — aslı «bir akşamın bulutu»dur, muzâf hazfedilmiştir (Dürre). Yurda yılın bütün yağmurlarını toplar: kış yağmurlarının çoğu gece, baharınkiler sabah, yazınkiler akşam yağar (Zevzenî)"), HADD("مُرَاعَاةُ النَّظِيرِ: جَمَعَ السَّارِيَةَ وَالْغَادِيَ وَالْعَشِيَّةَ، وَهِيَ مُتَنَاسِبَةٌ لَا بِالتَّضَادِّ", "a murāʿāt al-naẓīr: the night-cloud, the morning-cloud and the evening are brought together, things that belong with one another without being opposites", "mürâât-ı nazîr vardır: gece bulutu, sabah bulutu ve akşam, zıtlık olmaksızın birbiriyle münasebetli şeyler olarak bir araya getirilmiştir"))),
  R("naatj", "مُتَجَاوِبٍ", "lb-mutajawib", g=["ism-fail", "istiara", "istiara-tabaiyya"], n=N3((" — نَعْتٌ سَبَبِيٌّ لِلسَّحَابِ الْمَحْذُوفِ، رَفَعَ «إِرْزَامُهَا» فَاعِلًا (الدُّرَّةُ)", " — a causal na't of the omitted «cloud»; it raises «its rumbling» as its doer (al-Durra)", " — mahzûf «bulut»un sebebî na'tı; «gürlemesi»ni fâil olarak ref eder (Dürre)"), ZW("أَيْ كَأَنَّ رُعُودَهَا تَتَجَاوَبُ — فَالتَّجَاوُبُ مُسْتَعَارٌ لِتَتَابُعِ أَصْوَاتِ الرَّعْدِ: اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ", "that is, «as though its thunders answered one another» — «answering» is borrowed for peal following peal: an istiʿāra taṣrīḥiyya tabaʿiyya", "yani «sanki gök gürültüleri birbirine cevap veriyor» — «cevaplaşma», gök gürültüsünün art arda gelişi için istiare edilmiştir: istiâre-i tasrîhiyye tebeiyye"))),
  R("fail", "إِرْزَامُهَا", "lb-irzam", enc="هَا", g=["masdar", "shurut-amal-ism-al-fail"], n=ZW("فَاعِلُ «مُتَجَاوِبٍ». الْإِرْزَامُ: التَّصْوِيتُ، وَقَدْ أَرْزَمَتِ النَّاقَةُ إِذَا رَغَتْ", "the doer of «answering one another». إِرْزَام is making a sound: أَرْزَمَتِ النَّاقَةُ, the she-camel groaned", "«birbirine cevap veren»in fâili. «İrzâm»: ses çıkarmak; deve böğürdüğünde «erzemet» denir"))])
VV(6, "So the shoots of the wild rocket stood high, and on both sides of the valley the gazelles bore their young, and the ostriches laid.",
  "Böylece yabani tere sürgünleri boy verdi; vadinin iki yakasında ceylanlar yavruladı, devekuşları da yumurtladı.",
 [V("ma", "فَعَلَا", "ala-rise", c="f", g=["naqis-verbs"], n=(" — وَالْفَاءُ عَاطِفَةٌ أَوِ اسْتِئْنَافِيَّةٌ (الدُّرَّةُ)", " — the fa conjoins, or opens a new clause (al-Durra)", " — fâ atıf yahut isti'nâf içindir (Dürre)")),
  R("fail", "فُرُوعُ", "far-branch", mud=True, g=["jam-taksir"], n=(" — وَيُرْوَى بِالنَّصْبِ مَفْعُولًا بِهِ وَالْفَاعِلُ ضَمِيرُ السَّيْلِ، وَالرَّفْعُ أَجْوَدُ (الدُّرَّةُ)", " — also read in nasb as an object, the doer being «the torrent»; raf' is the better reading (al-Durra)", " — mef'ûl olarak nasb ile de rivayet edilir, o zaman fâil «sel»in zamiridir; ref daha iyidir (Dürre)")),
  R("mdf", "الْأَيْهَقَانِ", "lb-ayhaqan", n=ZW("بِفَتْحِ الْهَاءِ وَضَمِّهَا: ضَرْبٌ مِنَ النَّبْتِ وَهُوَ الْجِرْجِيرُ الْبَرِّيُّ", "with fatha or damma on the ha: a kind of plant, the wild rocket", "hâ'nın fethası veya dammesiyle: bir bitki türü, yabani tere")),
  V("mt", "وَأَطْفَلَتْ", "lb-atfala", c="w", g=["form-iv-verbs"], n=ZW("أَطْفَلَتْ: صَارَتْ ذَوَاتِ أَطْفَالٍ", "أَطْفَلَتْ: they came to have young", "«etfelet»: yavru sahibi oldular"))],
 [R("majr", "بِالْجَلْهَتَيْنِ", "lb-jalha", j="bi", g=["al-muthanna"], sign=("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", " — by the ya, for it is a dual", " — tesniye olduğu için yâ ile"), n=N3(MT("أَطْفَلَتْ", "bore their young", "yavruladı»ya"), ZW("الْجَلْهَتَانِ: جَانِبَا الْوَادِي", "الْجَلْهَتَانِ are the two sides of the valley", "«celhetân»: vadinin iki yakası"))),
  R("fail", "ظِبَاؤُهَا", "zaby", enc="هَا", g=["jam-taksir"], n=(" — فَاعِلُ «أَطْفَلَتْ»؛ جَمْعُ ظَبْيٍ", " — the doer of «bore their young»; the plural of ظَبْي", " — «yavruladı»nın fâili; «zaby»in cem'i")),
  T("وَنَعَامُهَا", "lb-naam", "noun", ["fail", "ijaz-al-hadhf", "hadhf-wa-taqdir", "idafa-definiteness", "al-bariz-al-muttasil"],
     "الْوَاوُ عَاطِفَةٌ، وَنَعَامُ فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يُرِيدُ: وَأَطْفَلَتْ ظِبَاؤُهَا وَبَاضَتْ نَعَامُهَا، لِأَنَّ النَّعَامَ تَبِيضُ وَلَا تَلِدُ الْأَطْفَالَ، وَلٰكِنَّهُ عَطَفَ النَّعَامَ عَلَى الظِّبَاءِ فِي الظَّاهِرِ لِزَوَالِ اللَّبْسِ (الزَّوْزَنِيُّ)؛ فَفِيهِ إِيجَازٌ بِحَذْفِ الْفِعْلِ، مِنْ بَابِ «عَلَفْتُهَا تِبْنًا وَمَاءً بَارِدًا» (الدُّرَّةُ).",
     "The waw conjoins; «their ostriches» is the doer of an omitted verb, in raf', annexed to the attached pronoun, which is in the seat of jarr. He means «their gazelles bore young and their ostriches laid» — for ostriches lay eggs and bear no young — but in wording he joins the ostriches to the gazelles, since no one can mistake it (al-Zawzanī). It is brevity by dropping the verb, of the kind «I fed her straw and cold water» (al-Durra).",
     "«ve» + «devekuşları»: mahzûf bir fiilin fâili, merfû; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr. Kastı «ceylanları yavruladı, devekuşları yumurtladı»dır; çünkü devekuşu yumurtlar, yavru doğurmaz; fakat karışıklık ihtimali olmadığı için lafızda devekuşlarını ceylanlara atfetmiştir (Zevzenî). Fiilin hazfiyle îcâz vardır; «ona saman ve soğuk su yedirdim» kabilindendir (Dürre).",
     segs=SG(("وَ", "wa", "conj"), ("نَعَامُ", "lb-naam", "noun"), ("هَا", "pron-3fs", "pron")))])
VV(7, "And the wide-eyed wild cows rest quietly over their new-born calves, having lately calved, while their young gather into herds on the open plain.",
  "İri gözlü yaban sığırları, yeni doğurmuş olarak, yavrularının başında sükûnetle durur; yavruları da açık ovada sürü sürü toplanır.",
 [R("mub", "وَالْعِينُ", "lb-ayna", c="wi", g=["jam-taksir", "hadhf-wa-taqdir", "kinaya"], n=N3(ZW("الْعِينُ: وَاسِعَاتُ الْعُيُونِ، أَيِ الْبَقَرُ الْعِينُ — صِفَةٌ أُقِيمَتْ مَقَامَ الْمَوْصُوفِ. وَالْمَعْنَى مِنْ هٰذَا الْكَلَامِ أَنَّهَا صَارَتْ مَغْنَى الْوُحُوشِ بَعْدَ كَوْنِهَا مَغْنَى الْإِنْسِ", "الْعِين are «the wide-eyed», that is, the wild cows — the quality standing for its noun. What these words mean is that the place has become the home of wild beasts after being the home of people", "«în»: iri gözlüler, yani yaban sığırları — sıfat mevsûfun yerine geçmiştir. Bu sözden maksat, yurdun insanların meskeni iken vahşi hayvanların meskeni hâline geldiğidir"), (" — فَالْبَيْتُ كِنَايَةٌ عَنْ خُلُوِّ الدِّيَارِ مِنْ أَهْلِهَا: ذَكَرَ سُكُونَ الْوَحْشِ بِهَا وَأَرَادَ لَازِمَهُ", " — so the verse is a kināya for the dwellings being empty of their people: he names the wild creatures' ease there and means what must go with it", " — beyit, yurdun sakinlerinden boşalmasından kinayedir: vahşi hayvanların orada rahatça durmasını zikreder, bunun lâzımını kasteder"))),
  R("khb", "سَاكِنَةٌ", "sakin", g=["ism-fail"], n=(" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", " — a fresh sentence", " — cümle müste'nefedir")),
  PR("عَلَى", "ala", n=MT("سَاكِنَةٌ", "rest", "sükûnetle durur»a")),
  R("majr", "أَطْلَائِهَا", "tala-fawn", enc="هَا", g=["jam-taksir"], n=ZW("الطَّلَا: وَلَدُ الْوَحْشِ حِينَ يُولَدُ إِلَى أَنْ يَأْتِيَ عَلَيْهِ شَهْرٌ، وَالْجَمْعُ الْأَطْلَاءُ", "طَلًا is the young of a wild animal from birth until it is a month old; plural أَطْلَاء", "«talâ»: yabani hayvanın doğduğu andan bir aylık oluncaya kadarki yavrusu; cem'i «atlâ»"))],
 [R("hal", "عُوذًا", "lb-aidh", g=["jam-taksir"], n=N3(ZW("حَالٌ مِنَ «الْعِينُ». الْعُوذُ: الْحَدِيثَاتُ النِّتَاجِ، الْوَاحِدَةُ عَائِذٌ", "a hal of «the wide-eyed». عُوذ are those that have newly given birth, singular عَائِذ", "«în»den hâl. «Ûz»: yeni doğurmuş olanlar, tekili «âiz»"), (" — وَقَدَّمَ الدُّرَّةُ أَنَّهُ حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «سَاكِنَةٌ»، لِأَنَّ الْجُمْهُورَ لَا يُجِيزُونَ الْحَالَ مِنَ الْمُبْتَدَأِ", " — al-Durra gives first that it is a hal of the pronoun hidden in «resting», since most grammarians do not allow a hal of the mubtada", " — Dürre önce, onun «sâkine»deki gizli zamirden hâl olduğunu söyler; çünkü cumhur mübtedâdan hâl gelmesini caiz görmez"))),
  V("d", "تَأَجَّلُ", "lb-taajjala", g=["form-v-verbs", "al-hal-jumla-wa-rabituha"], n=N3((" — وَأَصْلُهُ «تَتَأَجَّلُ» فَحُذِفَتْ إِحْدَى التَّاءَيْنِ تَخْفِيفًا؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ (الدُّرَّةُ)", " — properly تَتَأَجَّلُ, one of the two ta's dropped for lightness; the clause is a second hal, in the seat of nasb (al-Durra)", " — aslı «teteeccelü»dür, tahfîf için iki tâ'dan biri hazfedilmiştir; cümle ikinci hâl, mahallen mansûb (Dürre)"), ZW("الْإِجْلُ: الْقَطِيعُ مِنْ بَقَرِ الْوَحْشِ، وَالتَّأَجُّلُ: صَيْرُورَتُهَا إِجْلًا إِجْلًا", "إِجْل is a herd of wild cows, and تَأَجُّل is their forming herd after herd", "«icl»: yaban sığırı sürüsü; «teeccül»: sürü sürü olmaları"))),
  R("majr", "بِالْفَضَاءِ", "fada-open", j="bi", g=["ism-mamdud"], n=N3(MT("تَأَجَّلُ", "gather into herds", "sürü sürü toplanır»a"), ZW("الْفَضَاءُ: الصَّحْرَاءُ", "الْفَضَاء is the open desert", "«fezâ»: açık çöl, sahra"))),
  R("fail", "بِهَامُهَا", "lb-baham", enc="هَا", g=["jam-taksir"], n=ZW("فَاعِلُ «تَأَجَّلُ». الْبِهَامُ: أَوْلَادُ الضَّأْنِ، وَاحِدُهَا بَهْمٌ، وَبَقَرُ الْوَحْشِ بِمَنْزِلَةِ الضَّأْنِ عِنْدَ الْعَرَبِ", "the doer of «gather into herds». بِهَام are the young of sheep, singular بَهْم; and the Arabs class wild cows with sheep", "«sürü sürü toplanır»ın fâili. «Bihâm»: koyun yavruları, tekili «behm»; Araplara göre yaban sığırı koyun menzilesindedir"))])

# ---- vv. 8–15 — سُؤَالُ الطُّلُولِ، وَظُعُنُ الْحَيِّ ----
ROLE["khbka"] = ("خَبَرُ كَأَنَّ مَرْفُوعٌ", "the predicate of كَأَنَّ, in raf'", "keenne'nin haberi, merfû", "raf", ["inna-wa-akhawatuha"])
ROLE["ismka"] = ("اسْمُ كَأَنَّ مَنْصُوبٌ", "the noun of كَأَنَّ, in nasb", "keenne'nin ismi, mansûb", "nasb", ["inna-wa-akhawatuha"])
def KAANNA(full, n=NO, enc=None, g=()):
    """كَأَنَّ alone, or with its noun attached"""
    a = "حَرْفُ تَشْبِيهٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ"; e = "The particle of likening, one of إِنَّ's sisters: it puts its noun in nasb"; t = "Teşbîh ve nasb harfi, inne'nin kardeşlerinden"
    if enc:
        a += "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا"; e += "; the attached pronoun is its noun, in the seat of nasb"; t += "; bitişik zamir ismidir, mahallen mansûb"
    return T(full, "kaanna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"] + (["al-bariz-al-muttasil"] if enc else []) + list(g), a + n[0] + ".", e + n[1] + ".", t + n[2] + ".",
             segs=SG(("كَأَنَّ", "kaanna", "part"), (enc, PRON[enc], "pron")) if enc else None)
TB = ["tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"]
VV(8, "And the torrents have uncovered the ruins, so that they are like books whose texts the pens write afresh;",
  "Seller kalıntıların üstünü açmıştır; öyle ki onlar, kalemlerin satırlarını yeniden yazdığı kitaplar gibidir;",
 [V("ma", "وَجَلَا", "jala", c="wi", g=["naqis-verbs"], n=N3((" — وَالْعَطْفُ مُمْكِنٌ (الدُّرَّةُ)", " — it may also be read as conjoining (al-Durra)", " — atıf da mümkündür (Dürre)"), ZW("جَلَا: كَشَفَ", "جَلَا: to uncover", "«celâ»: açığa çıkardı"))),
  R("fail", "السُّيُولُ", "sayl", g=["jam-taksir"], n=(" — جَمْعُ سَيْلٍ", " — the plural of سَيْل", " — «seyl»in cem'i")),
  PR("عَنِ", "an", n=N3((" — وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", ", voweled with kasra before the ال", " — iki sâkin karşılaştığı için kesre ile harekelendi"), MT("جَلَا", "have uncovered", "açığa çıkardı»ya"))),
  R("majr", "الطُّلُولِ", "talal", g=["jam-taksir"], n=ZW("جَمْعُ الطَّلَلِ؛ أَيْ كَشَفَتْ عَنْ أَطْلَالِ الدِّيَارِ فَأَظْهَرَتْهَا بَعْدَ سَتْرِ التُّرَابِ إِيَّاهَا", "the plural of طَلَل; that is, they uncovered the ruins of the dwellings and brought them to light after the dust had covered them", "«talel»in cem'i; yani toprağın örttüğü yurt kalıntılarını açıp ortaya çıkardı")),
  KAANNA("كَأَنَّهَا", enc="هَا", g=TB + ["al-hal-jumla-wa-rabituha"], n=N3((" يَعُودُ عَلَى الطُّلُولِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الطُّلُولِ» (الدُّرَّةُ)", " — the ruins; the clause is a hal of «the ruins», in the seat of nasb (al-Durra)", " — kalıntılara döner; cümle «tulûl»den hâl, mahallen mansûb (Dürre)"), (" — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الطُّلُولُ الَّتِي كَشَفَتْ عَنْهَا السُّيُولُ، وَالْمُشَبَّهُ بِهِ زُبُرٌ تُجِدُّ الْأَقْلَامُ كِتَابَتَهَا، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ — الظُّهُورُ بَعْدَ الدُّرُوسِ — غَيْرُ مَذْكُورٍ. قَالَ الزَّوْزَنِيُّ: شَبَّهَ كَشْفَ السُّيُولِ عَنِ الْأَطْلَالِ بِتَجْدِيدِ الْكُتَّابِ سُطُورَ الْكِتَابِ الدَّارِسِ، وَظُهُورَ الْأَطْلَالِ بَعْدَ دُرُوسِهَا بِظُهُورِ السُّطُورِ بَعْدَ دُرُوسِهَا", " — a tashbih mursal mujmal: the thing likened is the ruins the torrents have uncovered; it is likened to books whose writing the pens renew; the particle is كَأَنَّ; the point of likeness — showing again after being effaced — is not stated. Al-Zawzanī: «he likens the torrents' uncovering of the ruins to scribes renewing the lines of a faded book, and the ruins showing after they were effaced to the lines showing after they had faded»", " — teşbîh-i mürsel mücmel vardır: müşebbeh, sellerin üstünü açtığı kalıntılar; müşebbehün bih, kalemlerin yazısını yenilediği kitaplar; edat «keenne»; vech-i şebeh — silindikten sonra yeniden görünmek — zikredilmemiştir. Zevzenî: «sellerin kalıntıları açmasını kâtiplerin silik kitabın satırlarını yenilemesine, kalıntıların silindikten sonra görünmesini satırların silindikten sonra görünmesine benzetti»")))],
 [R("khbka", "زُبُرٌ", "lb-zabur", g=["jam-taksir"], n=ZW("جَمْعُ زَبُورٍ وَهُوَ الْكِتَابُ: فَعُولٌ بِمَعْنَى الْمَفْعُولِ", "the plural of زَبُور, a book: a فَعُول with the sense of the passive participle, «what is written»", "«zebûr»un cem'i: kitap; mef'ûl mânasında «feûl»")),
  V("d", "تُجِدُّ", "lb-ajadda", g=["form-iv-verbs", "doubled-verbs", "jumla-sifa"], n=N3(ZW("الْإِجْدَادُ وَالتَّجْدِيدُ وَاحِدٌ", "إِجْدَاد and تَجْدِيد are one: to make new", "«icdâd» ile «tecdîd» aynıdır: yenilemek"), (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«زُبُرٌ»", " — the clause is a na't of «books», in the seat of raf'", " — cümle «kitaplar»ın na'tı, mahallen merfû"))),
  R("maf", "مُتُونَهَا", "matn", enc="هَا", g=["jam-taksir"], n=(" — مُقَدَّمٌ عَلَى الْفَاعِلِ؛ أَيْ كِتَابَتَهَا وَسُطُورَهَا", " — placed before the doer; «their texts», the writing and lines on them", " — fâilden öne alınmıştır; yani yazıları ve satırları")),
  R("fail", "أَقْلَامُهَا", "qalam", enc="هَا", g=["jam-taksir", "majaz-aqli"], n=N3(ZW("وَ«أَقْلَامُ» مُضَافَةٌ إِلَى ضَمِيرِ «زُبُرٌ»", "«pens» is annexed to the pronoun of «books»", "«kalemler», «kitaplar»ın zamirine muzâftır"), HADD("مَجَازٌ عَقْلِيٌّ: أَسْنَدَ التَّجْدِيدَ إِلَى الْأَقْلَامِ وَهِيَ آلَتُهُ وَسَبَبُهُ، وَالْمُجَدِّدُ الْكَاتِبُ — وَبِهِ فَسَّرَ الزَّوْزَنِيُّ: «بِتَجْدِيدِ الْكُتَّابِ»", "a majāz ʿaqlī: the renewing is ascribed to the pens, its instrument and means, while the one who renews is the scribe — and so al-Zawzanī glosses it: «the scribes' renewing»", "mecâz-ı aklî vardır: yenileme, âleti ve sebebi olan kalemlere isnad edilmiştir; yenileyen ise kâtiptir — Zevzenî de «kâtiplerin yenilemesi» diye açıklar")))])
VV(9, "or like a tattooing-woman's going-over of her tattoo, its lampblack sprinkled into rings above which the tattoo shows out clear.",
  "yahut dövmeci kadının dövmeyi yeniden işlemesi gibidir: is çivitini halkalara serpmiş, dövme de onların üzerinde belirmiştir.",
 [T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «yahut»."),
  R("atfr", "رَجْعُ", "lb-raj", mud=True, g=["masdar", "imal-al-masdar"] + TB, n=N3((" — مَعْطُوفٌ عَلَى «زُبُرٌ» فِي الْبَيْتِ قَبْلَهُ، مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ (الدُّرَّةُ)", " — joined to «books» in the verse before; the masdar is annexed to its doer (al-Durra)", " — önceki beyitteki «kitaplar»a ma'tûf; masdar fâiline muzâftır (Dürre)"), ZW("الرَّجْعُ: التَّرْدِيدُ وَالتَّجْدِيدُ. عَطَفَ عَلَى الْمُشَبَّهِ بِهِ الْأَوَّلِ مُشَبَّهًا بِهِ ثَانِيًا: شَبَّهَ ظُهُورَ الْأَطْلَالِ بَعْدَ دُرُوسِهَا بِتَجْدِيدِ الْكِتَابَةِ وَتَجْدِيدِ الْوَشْمِ", "رَجْع is going over a thing again, renewing it. To the first thing likened-to he joins a second: he likens the ruins' showing after they were effaced to the renewing of writing and the renewing of a tattoo", "«rec'»: tekrar üzerinden geçmek, yenilemek. İlk müşebbehün bihe ikinci bir müşebbehün bih atfeder: kalıntıların silindikten sonra görünmesini yazının yenilenmesine ve dövmenin yenilenmesine benzetir"))),
  R("mdf", "وَاشِمَةٍ", "lb-washima", g=["ism-fail", "hadhf-wa-taqdir"], n=(" — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: امْرَأَةٍ وَاشِمَةٍ (الدُّرَّةُ)", " — a quality whose noun is left out: «a woman who tattoos» (al-Durra)", " — mevsûfu hazfedilmiş sıfat: «dövme yapan kadın» (Dürre)")),
  V("m", "أُسِفَّ", "lb-asaffa", pas=True, g=["form-iv-verbs", "doubled-verbs", "mafulayn", "jumla-sifa"], n=N3(ZW("الْإِسْفَافُ: الذَّرُّ، يُقَالُ: أَسْفَفْتُ الدَّوَاءَ الْجُرْحَ وَالْكُحْلَ الْعَيْنَ", "إِسْفَاف is sprinkling a powder into a thing: one says it of medicine into a wound and kohl into the eye", "«isfâf»: toz hâlindeki şeyi serpmek; yaraya ilaç, göze sürme için söylenir"), (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)", " — the clause is a second na't of the omitted noun, in the seat of jarr (al-Durra)", " — cümle mahzûf mevsûfun ikinci na'tı, mahallen mecrûr (Dürre)"))),
  R("naib", "نَؤُورُهَا", "lb-nauur", enc="هَا", g=["mafulayn"], n=ZW("اسْمُ مَا لَمْ يُسَمَّ فَاعِلُهُ، وَهُوَ الْمَفْعُولُ الْأَوَّلُ فِي الْأَصْلِ. النَّؤُورُ: النَّقْشُ الْمُتَّخَذُ مِنْ دُخَانِ السِّرَاجِ وَالنَّارِ، وَقِيلَ النِّيلَجُ", "the noun of the verb whose doer is not named — it was the first object. نَؤُور is the pigment made from the smoke of a lamp or fire; others say indigo", "fâili anılmayan fiilin ismi; aslında birinci mef'ûldür. «Neûr»: kandil ve ateş isinden elde edilen boya; çivit olduğu da söylenmiştir"))],
 [R("maf", "كِفَفًا", "lb-kiffa", g=["mafulayn", "jam-taksir"], n=ZW("هُوَ الْمَفْعُولُ الثَّانِي، بَقِيَ عَلَى انْتِصَابِهِ بَعْدَ إِسْنَادِ الْفِعْلِ إِلَى الْمَفْعُولِ. الْكِفَفُ: جَمْعُ كِفَّةٍ بِكَسْرِ الْكَافِ وَهِيَ الدَّارَاتُ، وَكُلُّ شَيْءٍ مُسْتَدِيرٍ كِفَّةٌ", "the second object, left in nasb after the verb was given to the first. كِفَف is the plural of كِفَّة with kasra on the kaf: rings — anything round is a كِفَّة", "ikinci mef'ûldür; fiil birinci mef'ûle isnad edildikten sonra mansûb kalmıştır. «Kifef»: kâfın kesresiyle «kiffe»nin cem'i: halkalar; yuvarlak her şeye «kiffe» denir")),
  V("m", "تَعَرَّضَ", "taarrada", g=["form-v-verbs", "jumla-sifa"], n=N3(ZW("تَعَرَّضَ وَأَعْرَضَ: ظَهَرَ وَلَاحَ", "تَعَرَّضَ, like أَعْرَضَ: it showed, it stood out", "«taarrada» ve «a'rada»: göründü, belirdi"), (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«كِفَفًا»", " — the clause is a na't of «rings», in the seat of nasb", " — cümle «halkalar»ın na'tı, mahallen mansûb"))),
  R("zarfm", "فَوْقَهُنَّ", "fawqa", enc="هُنَّ", n=(" — مُتَعَلِّقٌ بِـ«تَعَرَّضَ»، وَالضَّمِيرُ لِلْكِفَفِ", " — it hangs on «shows out»; «them» are the rings", " — «belirdi»ye müteallik; zamir halkalara döner")),
  R("fail", "وِشَامُهَا", "washm", enc="هَا", g=["jam-taksir"], n=ZW("فَاعِلُ «تَعَرَّضَ»، وَقَدْ أُضِيفَ إِلَى ضَمِيرِ الْوَاشِمَةِ. الْوِشَامُ: جَمْعُ وَشْمٍ", "the doer of «shows out», annexed to the pronoun of the tattooing-woman. وِشَام is the plural of وَشْم", "«belirdi»nin fâili; dövmeci kadının zamirine muzâftır. «Vişâm»: «veşm»in cem'i"))])
VV(10, "So I stood questioning them — but how do we question deaf, enduring stones whose speech never comes clear?",
  "Durup onlara sordum — ama sözü hiç açığa çıkmayan sağır, kalıcı taşlara nasıl soru sorulur ki?",
 [V("mtu", "فَوَقَفْتُ", "waqafa", c="fi", g=["mithal-verbs"]),
  V("d", "أَسْأَلُهَا", "saala", enc="هَا", g=["al-fail-al-mudmar-al-mustatir-wujuban", "al-hal-jumla-wa-rabituha", "hadhf-al-maful", "tajahul-al-arif"], doer=DZ("أَنَا وُجُوبًا", "«I», which must stay hidden", "vücûben gizli «ben»"), n=N3((" — يَعُودُ عَلَى الطُّلُولِ، وَالْمُتَعَلِّقُ مَحْذُوفٌ: أَسْأَلُهَا عَنِ الْأَحِبَّةِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ تَاءِ الْفَاعِلِ (الدُّرَّةُ)", " — «them» are the ruins; what he asks about is left out: «about the loved ones». The clause is a hal of the ta of the doer, in the seat of nasb (al-Durra)", " — zamir kalıntılara döner; sorulan şey hazfedilmiştir: «sevgilileri sordum». Cümle fâil tâ'sından hâl, mahallen mansûb (Dürre)"), HADD("تَجَاهُلُ الْعَارِفِ: سَأَلَ مَا يَعْلَمُ أَنَّهُ لَا يُجِيبُ، وَالنُّكْتَةُ التَّحَيُّرُ وَالتَّدَلُّهُ فِي الْحُبِّ — قَالَ الزَّوْزَنِيُّ: لَوَّحَ إِلَى أَنَّ الدَّاعِيَ إِلَى هٰذَا السُّؤَالِ فَرْطُ الْكَلَفِ وَالشَّغَفِ وَغَايَةُ الْوَلَهِ، لِأَنَّ الْهَوَى وَالْمُصِيبَةَ يُدَلِّهَانِ صَاحِبَهُمَا", "a tajāhul al-ʿārif: he questions what he knows cannot answer, and the point is the lover's bewilderment — al-Zawzanī: «he hints that what drove him to ask was the excess of his passion and longing; for love and loss bewilder a man»", "tecâhül-i ârif vardır: cevap veremeyeceğini bildiği şeye soru sorar; nüktesi aşkta şaşkınlık ve kendinden geçmedir — Zevzenî: «bu soruya sevk edenin aşırı tutku ve özlem olduğuna işaret eder; çünkü sevda ve musibet insanı şaşkına çevirir»"))),
  T("وَكَيْفَ", "kayfa", "noun", ["al-istifham", "khuruj-al-istifham", "mubtada-khabar", "jumla-mutarida", "anwa-al-waw"],
     "الْوَاوُ لِلِاعْتِرَاضِ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ — وَالْجُمْلَةُ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا. وَالِاسْتِفْهَامُ لَيْسَ عَلَى حَقِيقَتِهِ: مَعْنَاهُ التَّعَجُّبُ (الدُّرَّةُ)؛ أَيْ: كَيْفَ يُجْدِي هٰذَا السُّؤَالُ عَلَى صَاحِبِهِ؟ (الزَّوْزَنِيُّ).",
     "The waw opens a parenthesis; كَيْفَ is the interrogative noun, built on fatha, in the seat of raf' as a fronted khabar — the sentence is parenthetical and has no seat. The question is not a real one: it expresses wonder (al-Durra) — «what use is such asking to the one who asks?» (al-Zawzanī).",
     "Vâv i'tirâziyyedir; «keyfe» fetha üzere mebnî istifhâm ismi, mukaddem haber olarak mahallen merfû — cümle mu'tarızadır, i'râbdan mahalli yoktur. İstifhâm hakiki değildir: taaccüb bildirir (Dürre); yani «bu soru soran kişiye ne fayda sağlar?» (Zevzenî).",
     segs=SG(("وَ", "wa", "conj"), ("كَيْفَ", "kayfa", "noun"))),
  R("mub", "سُؤَالُنَا", "sual", enc="نَا", g=["masdar", "imal-al-masdar"], n=(" — مُبْتَدَأٌ مُؤَخَّرٌ؛ مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", " — placed after its khabar; the masdar is annexed to its doer", " — haberinden sonraya bırakılmıştır; masdar fâiline muzâftır"))],
 [R("maf", "صُمًّا", "asamm", g=["imal-al-masdar", "hadhf-wa-taqdir"], n=ZW("مَفْعُولٌ بِهِ لِلْمَصْدَرِ «سُؤَالُ» (الدُّرَّةُ)، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: حِجَارَةً صُمًّا. الصُّمُّ: الصِّلَابُ، وَالْوَاحِدُ أَصَمُّ", "the object of the masdar «questioning» (al-Durra), and a quality whose noun is left out: «deaf stones». صُمّ are the hard and solid, singular أَصَمّ", "«sorma» masdarının mef'ûlü (Dürre); mevsûfu hazfedilmiş sıfattır: «sağır taşlar». «Summ»: sert, katı olanlar; tekili «esamm»")),
  R("naatn", "خَوَالِدَ", "khalid-abiding", g=["mamnu-min-sarf", "jam-taksir"], n=ZW("وَلَمْ يُنَوَّنْ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ. خَوَالِدُ: بَوَاقٍ", "without tanwin, being a «farthest plural». خَوَالِد: lasting, abiding", "muntehe'l-cumû' vezninde olduğu için tenvinsizdir. «Havâlid»: bâki kalanlar")),
  T("مَا", "ma-nafiya", "part", ["ma-la-mushabbaha"], "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ.", "A particle of negation; it governs nothing here.", "Nefy harfi; burada amel etmez."),
  V("d", "يَبِينُ", "lb-bana", g=["hollow-verbs", "jumla-sifa"], n=ZW("يَبِينُ: يَظْهَرُ؛ وَيُرْوَى «مَا يَبِينُ» وَ«مَا يُبِينُ» بِفَتْحِ الْيَاءِ وَضَمِّهَا، وَهُمَا بِمَعْنَى ظَهَرَ. وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَالِثٌ لِلْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)", "يَبِينُ: comes clear; read with fatha or damma on the ya, both meaning «to be plain». The clause is a third na't of the omitted noun, in the seat of nasb (al-Durra)", "«yebînü»: açığa çıkar; yâ'nın fethası ve dammesiyle rivayet edilir, ikisi de «belirmek» anlamındadır. Cümle mahzûf mevsûfun üçüncü na'tı, mahallen mansûb (Dürre)")),
  R("fail", "كَلَامُهَا", "kalam", enc="هَا")])
VV(11, "They lie bare. The whole tribe was once there; then they set out from them early in the day, and their tent-trench and their panic-grass were left behind.",
  "Kalıntılar bomboş kaldı. Bir zamanlar bütün kabile oradaydı; sonra sabah erkenden oradan göçtüler; çadır hendeği ile sümâm otu geride bırakıldı.",
 [V("mt", "عَرِيَتْ", "lb-ariya", g=["naqis-verbs"], doer=DZ("هِيَ يَعُودُ عَلَى الطُّلُولِ", "«she» — the ruins", "kalıntılara dönen gizli «o»"), n=N3((" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", " — a fresh sentence", " — cümle müste'nefedir"), ZW("أَيْ عَرِيَتْ عَنْ قُطَّانِهَا", "that is, bare of those who dwelt there", "yani sakinlerinden boşaldı"))),
  T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-hal-jumla-wa-rabituha", "anwa-al-waw"],
     "الْوَاوُ وَاوُ الْحَالِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «عَرِيَتْ» بِإِضْمَارِ «قَدْ» (الدُّرَّةُ).",
     "The waw of hal; كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb — the clause is a hal of the doer of «lie bare», in the seat of nasb, with قَدْ understood (al-Durra).",
     "Vâv hâliyyedir; kâne nâkıs mâzî fiil: ismini ref, haberini nasb eder — cümle, «kad» takdiriyle «boş kaldı»nın fâilinden hâl, mahallen mansûb (Dürre).",
     segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  JP("بِهَا", "bi", "هَا", g=["taqdim-al-musnad"], n=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «كَانَ» مُقَدَّمٍ", "; the phrase hangs on the omitted, fronted predicate of كَانَ", "; câr-mecrûr kâne'nin mahzûf mukaddem haberine müteallik")),
  R("ismk", "الْجَمِيعُ", "jami", n=(" — اسْمُهَا مُؤَخَّرٌ؛ أَيْ جَمِيعُ الْحَيِّ", " — its noun, placed last; «all of them», the whole tribe", " — sona bırakılmış ismi; yani kabilenin tamamı")),
  V("mw", "فَأَبْكَرُوا", "lb-abkara", c="f", g=["form-iv-verbs"], n=ZW("بَكَرْتُ مِنَ الْمَكَانِ وَأَبْكَرْتُ: سِرْتُ مِنْهُ بُكْرَةً", "أَبْكَرَ مِنَ الْمَكَانِ: he left the place early in the morning", "«ebkera mine'l-mekân»: oradan sabah erkenden yola çıktı"))],
 [JP("مِنْهَا", "min", "هَا", n=MT("أَبْكَرُوا", "set out early", "erkenden göçtüler»e")),
  V("m", "وَغُودِرَ", "lb-ghadara", c="w", pas=True, g=["form-iii-verbs"], n=ZW("الْمُغَادَرَةُ: التَّرْكُ؛ أَيْ لَمْ يَبْقَ بِمَنَازِلِهِمْ مِنْهُمْ آثَارٌ إِلَّا النُّؤْيُ وَالثُّمَامُ", "مُغَادَرَة is leaving a thing behind; that is, nothing of them remained in their camp but the trench and the panic-grass", "«mugâdere»: terk etmek; yani konak yerlerinde onlardan hendek ile sümâmdan başka iz kalmadı")),
  R("naib", "نُؤْيُهَا", "nuy", enc="هَا", n=ZW("النُّؤْيُ: نُهَيْرٌ يُحْفَرُ حَوْلَ الْبَيْتِ لِيَنْصَبَّ إِلَيْهِ الْمَاءُ", "نُؤْي is the little channel dug round a tent so that the rain-water drains into it", "«nü'y»: yağmur suyu içine aksın diye çadırın çevresine kazılan küçük hendek")),
  R("atfr", "وَثُمَامُهَا", "lb-thumam", c="w", enc="هَا", n=ZW("الثُّمَامُ: ضَرْبٌ مِنَ الشَّجَرِ رِخْوٌ يُسَدُّ بِهِ خَلَلُ الْبُيُوتِ", "ثُمَام is a soft kind of plant with which the gaps of the tents are stopped", "«sümâm»: çadırların aralıklarını tıkamakta kullanılan yumuşak bir bitki"))])
VV(12, "The litter-camels of the tribe stirred your longing when they loaded up and went into their coverts, group by group, their tent-frames creaking,",
  "Kabilenin hevdeçli develeri, yüklerini yükleyip bölük bölük hevdeçlere — sığınaklarına — girdikleri zaman seni özleme düşürdü; çadırları gıcırdıyordu.",
 [V("mt", "شَاقَتْكَ", "lb-shaqa", enc="كَ", g=["hollow-verbs", "tajrid", "iltifat"], n=N3(ZW("أَيْ حَمَلَتْكَ عَلَى الِاشْتِيَاقِ وَالْحَنِينِ", "that is, moved you to longing and yearning", "yani seni özleme ve hasrete sevk etti"), (" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ (الدُّرَّةُ)", " — a fresh sentence (al-Durra)", " — cümle müste'nefedir (Dürre)"), HADD("تَجْرِيدٌ بِمُخَاطَبَةِ الْإِنْسَانِ نَفْسَهُ، وَالْتِفَاتٌ مِنَ التَّكَلُّمِ فِي «فَوَقَفْتُ» إِلَى الْخِطَابِ", "a tajrīd — the man addressing himself — and an iltifāt from the first person of «I stood» to the second", "kişinin kendine hitabı yoluyla tecrîd ve «durdum»daki tekellümden hitaba iltifât vardır"))),
  R("fail", "ظُعْنُ", "lb-zun", mud=True, g=["jam-taksir"], n=ZW("بِتَسْكِينِ الْعَيْنِ تَخْفِيفُ الظُّعُنِ بِضَمِّهَا، وَهِيَ جَمْعُ الظَّعُونِ: الْبَعِيرُ الَّذِي عَلَيْهِ هَوْدَجٌ وَفِيهِ امْرَأَةٌ؛ وَقَدْ يَكُونُ جَمْعَ ظَعِينَةٍ", "with sukun on the ʿayn, a lightened form of ظُعُن, the plural of ظَعُون: the camel that carries a litter with a woman in it; or it may be the plural of ظَعِينَة", "ayn'ın sükûnuyla, «zuun»un hafifletilmişi; «zaûn»un cem'i: üzerinde içinde kadın bulunan hevdeç taşıyan deve; «zaîne»nin cem'i de olabilir")),
  R("mdf", "الْحَيِّ", "hayy-tribe"),
  R("zarfz", "حِينَ", "hina", mud=True, n=(" — مُتَعَلِّقٌ بِـ«شَاقَتْكَ»، وَيَجُوزُ بِنَاؤُهُ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى جُمْلَةٍ فِعْلُهَا مَاضٍ (الدُّرَّةُ)", " — it hangs on «stirred your longing»; it may also be taken as built on fatha, being annexed to a clause with a past verb (al-Durra)", " — «seni özleme düşürdü»ye müteallik; fiili mâzî olan cümleye muzâf olduğu için fetha üzere mebnî sayılması da caizdir (Dürre)")),
  V("mw", "تَحَمَّلُوا", "tahammala", g=["form-v-verbs"], n=(" — وَالضَّمِيرُ لِلْحَيِّ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «حِينَ» إِلَيْهَا", " — «they» are the tribe; the clause is in the seat of jarr, حِينَ being annexed to it", " — zamir kabileye döner; cümle, «hîne» kendisine muzâf olduğu için mahallen mecrûr"))],
 [V("mw", "فَتَكَنَّسُوا", "lb-takannasa", c="f", g=["form-v-verbs", "istiara", "istiara-tabaiyya"], n=ZW("التَّكَنُّسُ: دُخُولُ الْكِنَاسِ وَالِاسْتِكْنَانُ بِهِ؛ جَعَلَ الْهَوَادِجَ لِلنِّسَاءِ بِمَنْزِلَةِ الْكُنُسِ لِلْوَحْشِ — فَهُوَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شَبَّهَ دُخُولَ الْهَوَادِجِ بِدُخُولِ الْكِنَاسِ ثُمَّ اشْتَقَّ مِنْهُ الْفِعْلَ", "تَكَنُّس is entering the covert and hiding in it; he makes the litters for the women what coverts are for wild creatures — an istiʿāra taṣrīḥiyya tabaʿiyya: entering the litters is likened to entering the covert, and the verb is drawn from it", "«tekennüs»: yabani hayvanın inine girip gizlenmesi; hevdeçleri kadınlar için vahşi hayvanların inleri menzilesinde kılmıştır — istiâre-i tasrîhiyye tebeiyye: hevdeçlere giriş ine girişe benzetilmiş, fiil bundan türetilmiştir")),
  R("hal", "قُطُنًا", "lb-qatin", g=["jam-taksir"], n=ZW("حَالٌ مِنْ وَاوِ الْجَمَاعَةِ إِنْ جُعِلَ جَمْعَ قَطِينٍ وَهُوَ الْجَمَاعَةُ، وَمَفْعُولٌ بِهِ إِنْ جُعِلَ قُطْنًا: دَخَلْنَ هَوَادِجَ غُطِّيَتْ بِثِيَابِ الْقُطْنِ", "a hal of the waw of the group if it is the plural of قَطِين, a company; an object if it is «cotton»: they went into litters covered with cotton cloths", "«katîn»in (topluluk) cem'i sayılırsa cemâat vâvından hâl; «pamuk» sayılırsa mef'ûlün bih: pamuklu kumaşlarla örtülü hevdeçlere girdiler")),
  V("d", "تَصِرُّ", "lb-sarra", g=["doubled-verbs", "al-hal-jumla-wa-rabituha"], n=ZW("الصَّرِيرُ: صَوْتُ الْبَابِ وَالرَّحْلِ وَغَيْرِ ذٰلِكَ؛ أَيْ فِي حَالِ صَرِيرِ خِيَامِهِنَّ الْمَحْمُولَةِ لِجِدَّتِهَا — فَالْجُمْلَةُ حَالٌ، وَجَعَلَهَا الدُّرَّةُ نَعْتًا لِـ«قُطُنًا»", "صَرِير is the creak of a door, a saddle and the like; that is, «while their tents, carried along, creaked for newness» — so the clause is a hal; al-Durra makes it a na't of قُطُنًا", "«sarîr»: kapı, semer ve benzerinin gıcırtısı; yani «taşınan çadırları yeniliğinden gıcırdarken» — cümle hâldir; Dürre onu «kutunen»in na'tı sayar")),
  R("fail", "خِيَامُهَا", "lb-khayma", enc="هَا", g=["jam-taksir"], n=ZW("وَالْمُضْمَرُ الَّذِي أُضِيفَ إِلَيْهِ «الْخِيَامُ» لِلظُّعْنِ", "the pronoun «tents» is annexed to is the litter-camels", "«çadırlar»ın muzâf olduğu zamir hevdeçli develere döner"))])
VV(13, "— each of them a litter hung about with cloths, its poles shaded by a spread laid over it: a thin awning, and its side-curtain;",
  "— her biri kumaşlarla sarılmış bir hevdeç; çubuklarını üzerine atılmış bir örtü gölgeler: ince bir tente ve onun yan perdesi;",
 [PR("مِنْ", "min", g=["hadhf-wa-taqdir"], n=N3((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَأٍ مَحْذُوفٍ: هِيَ مِنْ كُلِّ … (الدُّرَّةُ)", "; the phrase hangs on the omitted khabar of an omitted mubtada: «they are of every …» (al-Durra)", "; câr-mecrûr mahzûf bir mübtedânın mahzûf haberine müteallik: «onlar her … türündendir» (Dürre)"), ZW("ثُمَّ فَصَّلَ الظُّعْنَ", "here he sets the litter-camels out in detail", "burada hevdeçli develeri ayrıntısıyla anlatır"))),
  R("majr", "كُلِّ", "kull", mud=True),
  R("mdf", "مَحْفُوفٍ", "lb-mahfuf", g=["ism-maful", "hadhf-wa-taqdir"], n=ZW("صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: هَوْدَجٍ مَحْفُوفٍ؛ حُفَّ الْهَوْدَجُ بِالثِّيَابِ إِذَا غُطِّيَ بِهَا", "a quality whose noun is left out: «a litter hung about»; a litter is حُفَّ with cloths when it is covered with them", "mevsûfu hazfedilmiş sıfat: «sarılmış hevdeç»; hevdeç kumaşlarla örtüldüğünde «huffe» denir")),
  V("d", "يُظِلُّ", "lb-azalla", g=["form-iv-verbs", "doubled-verbs", "al-hal-jumla-wa-rabituha"], n=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «مَحْفُوفٍ» (الدُّرَّةُ)", " — the clause is a hal of the pronoun hidden in «hung about», in the seat of nasb (al-Durra)", " — cümle «mahfûf»taki gizli zamirden hâl, mahallen mansûb (Dürre)")),
  R("maf", "عِصِيَّهُ", "asa-staff", enc="هُ", g=["jam-taksir"], n=ZW("مُقَدَّمٌ عَلَى الْفَاعِلِ. الْعِصِيُّ هُنَا: عِيدَانُ الْهَوْدَجِ", "placed before the doer. The «staffs» here are the poles of the litter", "fâilden öne alınmıştır. «Isıyy» burada hevdecin çubuklarıdır"))],
 [R("fail", "زَوْجٌ", "lb-zawj", n=ZW("فَاعِلُ «يُظِلُّ». الزَّوْجُ: النَّمَطُ مِنَ الثِّيَابِ", "the doer of «shades». زَوْج here is a spread of cloth laid over a litter", "«gölgeler»in fâili. «Zevc» burada hevdecin üzerine atılan kumaş örtüdür")),
  JP("عَلَيْهِ", "ala", "هِ", g=["taqdim-al-musnad"], n=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ", "; the phrase hangs on an omitted, fronted khabar", "; câr-mecrûr mahzûf mukaddem habere müteallik")),
  R("mub", "كِلَّةٌ", "killa", g=["jumla-sifa"], n=N3((" — مُبْتَدَأٌ مُؤَخَّرٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«زَوْجٌ» (الدُّرَّةُ)", " — placed after its khabar; the clause is a na't of «a spread», in the seat of raf' (al-Durra)", " — haberinden sonraya bırakılmıştır; cümle «örtü»nün na'tı, mahallen merfû (Dürre)"), ZW("الْكِلَّةُ: السِّتْرُ الرَّقِيقُ، وَعَبَّرَ بِهَا عَنِ السِّتْرِ الَّذِي يُلْقَى فَوْقَ الْهَوْدَجِ لِئَلَّا تُؤْذِيَ الشَّمْسُ صَاحِبَتَهُ", "كِلَّة is a thin veil; by it he means the cover thrown over the litter so that the sun may not hurt the woman in it", "«kille»: ince örtü; bununla, güneş içindeki kadını rahatsız etmesin diye hevdecin üstüne atılan örtüyü kasteder"))),
  R("atfr", "وَقِرَامُهَا", "lb-qiram", c="w", enc="هَا", n=ZW("الْقِرَامُ: السِّتْرُ، وَعَبَّرَ بِهِ عَنِ السِّتْرِ الْمُرْسَلِ عَلَى جَوَانِبِ الْهَوْدَجِ؛ وَالْمُضْمَرُ لِلْعِصِيِّ أَوِ الْكِلَّةِ", "قِرَام is a curtain; by it he means the one let down over the sides of the litter; the pronoun is the poles, or the awning", "«kırâm»: perde; bununla hevdecin yanlarına sarkıtılan perdeyi kasteder; zamir çubuklara yahut tenteye döner"))])
VV(14, "— in companies, as though the wild cows of Tūḍiḥ were on the camels' backs, and the gazelles of Wajra, the white ones, with necks bent to their young.",
  "— bölük bölük; sanki develerin üzerinde Tûdıh'ın yaban inekleri ve Vecre'nin, yavrularına boyun bükmüş ak ceylanları vardı.",
 [R("hal", "زُجَلًا", "lb-zujla", g=["jam-taksir"], n=ZW("حَالٌ وَالْعَامِلُ فِيهَا «تَحَمَّلُوا» فِي الْبَيْتِ ١٢. الزُّجَلُ: الْجَمَاعَاتُ، الْوَاحِدَةُ زُجْلَةٌ", "a hal governed by «loaded up» in v. 12. زُجَل are companies, singular زُجْلَة", "âmili 12. beyitteki «yüklerini yüklediler» olan hâl. «Zücel»: topluluklar, tekili «zücle»")),
  KAANNA("كَأَنَّ", g=TB + ["al-hal-jumla-wa-rabituha"], n=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ مِنْ وَاوِ الْجَمَاعَةِ (الدُّرَّةُ). وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ النِّسَاءُ فِي الْهَوَادِجِ — وَلَمْ يُلْفَظْ بِهِ — وَالْمُشَبَّهُ بِهِ نِعَاجُ تُوضِحَ وَظِبَاءُ وَجْرَةَ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ غَيْرُ مَذْكُورٍ. قَالَ الزَّوْزَنِيُّ: شَبَّهَ النِّسَاءَ بِبَقَرِ تُوضِحَ وَظِبَاءِ وَجْرَةَ فِي كَحَلِ أَعْيُنِهَا", " — the clause is a second hal of the waw of the group, in the seat of nasb (al-Durra). It is a tashbih mursal mujmal: the thing likened is the women in the litters — not uttered — and they are likened to the wild cows of Tūḍiḥ and the gazelles of Wajra; the particle is كَأَنَّ, and the point of likeness is not stated. Al-Zawzanī: «he likens the women to the cows of Tūḍiḥ and the gazelles of Wajra in the darkness of their eyes»", " — cümle cemâat vâvından ikinci hâl, mahallen mansûb (Dürre). Teşbîh-i mürsel mücmel vardır: müşebbeh hevdeçlerdeki kadınlardır — lafzen anılmamıştır —; müşebbehün bih Tûdıh'ın yaban inekleri ve Vecre'nin ceylanları; edat «keenne»; vech-i şebeh zikredilmemiştir. Zevzenî: «kadınları, gözlerinin sürmeliliğinde Tûdıh sığırlarına ve Vecre ceylanlarına benzetti»")),
  R("ismka", "نِعَاجَ", "naja", mud=True, g=["jam-taksir"], n=ZW("النِّعَاجُ: إِنَاثُ بَقَرِ الْوَحْشِ، الْوَاحِدَةُ نَعْجَةٌ", "نِعَاج are the females of the wild cow, singular نَعْجَة", "«niâc»: yaban sığırının dişileri, tekili «na'ce»")),
  R("mdf", "تُوضِحَ", "tudih", pos="propn", g=["mamnu-min-sarf"], sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", " by the fatha in place of the kasra: a place-name barred from tanwin", " — gayr-i munsarif yer adı olduğu için kesre yerine fetha ile")),
  R("zarfm", "فَوْقَهَا", "fawqa", enc="هَا", n=(" — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «كَأَنَّ»، وَالضَّمِيرُ لِلْإِبِلِ وَلَمْ يَجْرِ لَهَا ذِكْرٌ (الدُّرَّةُ)", " — it hangs on the omitted predicate of كَأَنَّ; «them» are the camels, though they have not been named (al-Durra)", " — keenne'nin mahzûf haberine müteallik; zamir, adı geçmediği hâlde develere döner (Dürre)"))],
 [R("atfn", "وَظِبَاءَ", "zaby", c="w", mud=True, g=["jam-taksir"], n=(" — مَعْطُوفٌ عَلَى «نِعَاجَ»", " — joined to «wild cows»", " — «yaban inekleri»ne ma'tûf")),
  R("mdf", "وَجْرَةَ", "wajra", pos="propn", g=["mamnu-min-sarf"], sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " by the fatha in place of the kasra: a feminine place-name barred from tanwin", " — alemiyet ve te'nîs sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile"), n=ZW("وَجْرَةُ: مَوْضِعٌ بِعَيْنِهِ", "Wajra is a particular place", "Vecre belirli bir yerdir")),
  R("hal", "عُطَّفًا", "atif", g=["jam-taksir", "ism-fail"], n=ZW("حَالٌ مِنْ «ظِبَاءَ وَجْرَةَ». الْعُطَّفُ: جَمْعُ الْعَاطِفِ، مِنَ الْعَطْفِ الَّذِي هُوَ التَّرَحُّمُ أَوِ الَّذِي هُوَ الثَّنْيُ: فِي حَالِ تَرَحُّمِهَا عَلَى أَوْلَادِهَا أَوْ عَطْفِهَا أَعْنَاقَهَا لِلنَّظَرِ إِلَيْهَا، لِأَنَّ عُيُونَهَا أَحْسَنُ مَا تَكُونُ فِي هٰذِهِ الْحَالِ", "a hal of «the gazelles of Wajra». عُطَّف is the plural of عَاطِف, from عَطْف as tenderness or as bending: tender over their young, or bending their necks to look at them — for their eyes are at their loveliest then", "«Vecre ceylanları»ndan hâl. «Uttaf»: «âtıf»ın cem'i; şefkat veya bükme anlamındaki «atf»tan: yavrularına şefkat ederken yahut onlara bakmak için boyunlarını bükerken — çünkü gözleri en güzel bu hâlde olur")),
  R("fail", "أَرْآمُهَا", "rim", enc="هَا", g=["jam-taksir", "shurut-amal-ism-al-fail"], n=ZW("رُفِعَ لِأَنَّهُ فَاعِلٌ وَالْعَامِلُ فِيهِ الْحَالُ «عُطَّفًا» السَّادَّةُ مَسَدَّ الْفِعْلِ. الْأَرْآمُ: جَمْعُ الرِّئْمِ وَهُوَ الظَّبْيُ الْخَالِصُ الْبَيَاضِ", "in raf' as a doer, governed by the hal «bending», which does a verb's work. أَرْآم is the plural of رِئْم, the pure-white gazelle", "fâil olduğu için merfûdur; âmili, fiil yerini tutan hâl «uttafen»dir. «Er'âm»: «ri'm»in cem'i: bembeyaz ceylan"))])
VV(15, "They were urged on, and the mirage fell away from them, so that they were like the bends of the valley of Bīsha — its tamarisks and its great rocks.",
  "Develer hızlandırıldı; serap onlardan ayrıldı; öyle ki Bîşe vadisinin kıvrımları — ılgın ağaçları ve iri kayaları — gibiydiler.",
 [V("mt", "حُفِزَتْ", "lb-hafaza", pas=True, doer=DZ("هِيَ يَعُودُ عَلَى الظُّعْنِ، وَالْمُرَادُ الرِّكَابُ الَّتِي تُقِلُّهَا", "«she» — the litter-camels, the mounts that carry them", "hevdeçli develere, yani onları taşıyan bineklere dönen gizli «o»"), n=ZW("الْحَفْزُ: الدَّفْعُ؛ أَيْ ضُرِبَتِ الرِّكَابُ لِتَجِدَّ فِي السَّيْرِ", "حَفْز is driving forward; that is, the mounts were struck so as to quicken their pace", "«hafz»: itmek, sürmek; yani binekler hızlansın diye vuruldu")),
  V("m", "وَزَايَلَهَا", "lb-zayala", c="w", enc="هَا", g=["form-iii-verbs"], n=ZW("أَيْ فَارَقَهَا قِطَعُ السَّرَابِ: لَاحَتْ خِلَالَ قِطَعِ السَّرَابِ وَلَمَعَتْ", "that is, the patches of mirage parted from them: they showed and glinted through its patches", "yani serap parçaları onlardan ayrıldı: serap parçaları arasında görünüp parladılar")),
  R("fail", "السَّرَابُ", "lb-sarab"),
  KAANNA("كَأَنَّهَا", enc="هَا", g=TB + ["al-hal-jumla-wa-rabituha"], n=(" يَعُودُ عَلَى الظُّعْنِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ الْوَاقِعِ مَفْعُولًا بِهِ (الدُّرَّةُ). وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الظُّعْنُ، وَالْمُشَبَّهُ بِهِ مُنْعَطَفَاتُ وَادِي بِيشَةَ بِأَثْلِهَا وَحِجَارَتِهَا الْعِظَامِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ غَيْرُ مَذْكُورٍ. قَالَ الزَّوْزَنِيُّ: شَبَّهَهَا فِي الْعِظَمِ وَالضِّخَمِ بِهِمَا", " — the litter-camels; the clause is a hal of the pronoun that stands as object, in the seat of nasb (al-Durra). It is a tashbih mursal mujmal: the litter-camels are likened to the bends of the valley of Bīsha with its tamarisks and great rocks; the particle is كَأَنَّ, and the point of likeness is not stated. Al-Zawzanī: «he likens them to the two in size and bulk»", " — hevdeçli develere döner; cümle mef'ûl olan zamirden hâl, mahallen mansûb (Dürre). Teşbîh-i mürsel mücmel vardır: müşebbeh hevdeçli develer; müşebbehün bih ılgınları ve iri kayalarıyla Bîşe vadisinin kıvrımları; edat «keenne»; vech-i şebeh zikredilmemiştir. Zevzenî: «onları büyüklük ve irilikte bu ikisine benzetti»"))],
 [R("khbka", "أَجْزَاعُ", "lb-jiz", mud=True, g=["jam-taksir"], n=ZW("الْأَجْزَاعُ: جَمْعُ جِزْعٍ وَهُوَ مُنْعَطَفُ الْوَادِي", "أَجْزَاع is the plural of جِزْع, the bend of a valley", "«eczâ'»: «ciz'»in cem'i: vadinin kıvrımı")),
  R("mdf", "بِيشَةَ", "lb-bisha", pos="propn", g=["mamnu-min-sarf"], sign=("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " by the fatha in place of the kasra: a feminine place-name barred from tanwin", " — alemiyet ve te'nîs sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile"), n=ZW("بِيشَةُ: وَادٍ بِعَيْنِهِ", "Bīsha is a particular valley", "Bîşe belirli bir vadidir")),
  R("bdlr", "أَثْلُهَا", "lb-athl", enc="هَا", g=["al-badal-wa-aqsamuh-wa-atf-al-bayan"], n=ZW("بَدَلٌ مِنْ «أَجْزَاعُ بِيشَةَ» (الدُّرَّةُ)، وَالضَّمِيرُ لِبِيشَةَ. الْأَثْلُ: شَجَرٌ يُشْبِهُ الطَّرْفَاءَ إِلَّا أَنَّهُ أَعْظَمُ مِنْهَا", "a badal of «the bends of Bīsha» (al-Durra); the pronoun is Bīsha. أَثْل is a tree like the tamarisk, but larger", "«Bîşe'nin kıvrımları»ndan bedel (Dürre); zamir Bîşe'ye döner. «Esl»: ılgına benzeyen, fakat ondan büyük bir ağaç")),
  R("atfr", "وَرِضَامُهَا", "lb-ridam", c="w", enc="هَا", n=ZW("الرِّضَامُ: الْحِجَارَةُ الْعِظَامُ، الْوَاحِدَةُ رَضْمَةٌ", "رِضَام are great rocks, singular رَضْمَة", "«rıdâm»: iri kayalar, tekili «radme»"))])

# ---- vv. 16–21 — نَوَارُ، وَقَطْعُ اللُّبَانَةِ ----
CONJ["fj"] = ("fa", "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَ", "The fa ties the answer to its condition; ", "Fâ şartın cevabını bağlar; ")
NAWAR = DZ("هِيَ يَعُودُ عَلَى نَوَارَ", "«she» — Nawār", "Nevâr'a dönen gizli «o»")
DIPT_F3 = ("بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " by the fatha in place of the kasra: a feminine proper name barred from tanwin", " — alemiyet ve te'nîs sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile")
SURIFA = (" — وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ لِأَنَّهُ عَلَمٌ، وَصُرِفَ لِضَرُورَةِ الشِّعْرِ: لَا يَسْتَقِيمُ الْوَزْنُ إِلَّا بِتَنْوِينِهِ", " — as a proper name it should take no tanwin; it is declined in full by poetic licence, for the metre stands only with the tanwin", " — özel isim olduğu için gayr-i munsarif olması gerekirken şiir zarûretiyle tenvinlenmiştir: vezin ancak tenvinle doğrulur")
VV(16, "But no — what is it you remember of Nawār, now that she is far away and her ties, the strong ropes and the frayed ends alike, are cut?",
  "Ama bırak bunu — Nevâr uzaklaşmış, bağlarının sağlamı da çürüğü de kopmuşken onun nesini hatırlıyorsun?",
 [T("بَلْ", "bal", "part", ["aw-imma-am-la-bal-lakin-fil-kafiya"], "حَرْفُ إِضْرَابٍ لِلِانْتِقَالِ مِنْ كَلَامٍ إِلَى آخَرَ مِنْ غَيْرِ إِبْطَالٍ لِمَا سَبَقَ (الزَّوْزَنِيُّ): أَضْرَبَ عَنْ صِفَةِ الدِّيَارِ وَأَخَذَ فِي كَلَامٍ آخَرَ.", "The particle of turning away — here a passing from one subject to another, without cancelling what went before (al-Zawzanī): he leaves the dwellings and takes up something else.", "İdrâb harfi — burada önceki sözü iptal etmeksizin bir sözden başka söze geçiş içindir (Zevzenî): yurt tasvirini bırakıp başka bir söze başlar."),
  T("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar", "al-mabni-wal-mudmar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَيَجُوزُ أَنْ يَكُونَ مَفْعُولًا بِهِ مُقَدَّمًا لِـ«تَذَكَّرُ» (الدُّرَّةُ).", "The interrogative noun «what», built on sukun, in the seat of raf' as mubtada; or it may be the fronted object of «you remember» (al-Durra).", "İstifhâm ismi «ne», sükûn üzere mebnî, mübtedâ olarak mahallen merfû; «hatırlıyorsun»un öne alınmış mef'ûlü de olabilir (Dürre)."),
  V("d", "تَذَكَّرُ", "tadhakkara", g=["form-v-verbs", "al-fail-al-mudmar-al-mustatir-wujuban", "tajrid", "anwa-al-khabar"], doer=DZ("أَنْتَ وُجُوبًا", "«you», which must stay hidden", "vücûben gizli «sen»"), n=N3((" — وَأَصْلُهُ «تَتَذَكَّرُ» فَحُذِفَتْ إِحْدَى التَّاءَيْنِ، وَالْمَفْعُولُ مَحْذُوفٌ: تَتَذَكَّرُهُ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَا» (الدُّرَّةُ)", " — properly تَتَذَكَّرُ, one ta dropped; its object is left out; the clause is the khabar of مَا, in the seat of raf' (al-Durra)", " — aslı «tetezekkerü»dür, iki tâ'dan biri hazfedilmiştir; mef'ûlü mahzûftur; cümle «mâ»nın haberi, mahallen merfû (Dürre)"), ZW("قَالَ مُخَاطِبًا نَفْسَهُ: أَيَّ شَيْءٍ تَتَذَكَّرُ مِنْ نَوَارَ — فَهُوَ تَجْرِيدٌ بِمُخَاطَبَةِ الْإِنْسَانِ نَفْسَهُ", "he says it addressing himself: «what do you remember of Nawār?» — a tajrīd, the man speaking to himself", "kendine hitap ederek söyler: «Nevâr'ın nesini hatırlıyorsun?» — kişinin kendine hitabı yoluyla tecrîd"))),
  PR("مِنْ", "min", n=MT("تَذَكَّرُ", "you remember", "hatırlıyorsun»a")),
  R("majr", "نَوَارَ", "lb-nawar", pos="propn", g=["mamnu-min-sarf"], sign=DIPT_F3, n=ZW("اسْمُ امْرَأَةٍ يُشَبِّبُ بِهَا", "the name of the woman he sings of", "hakkında gazel söylediği kadının adı")),
  T("وَقَدْ", "qad", "part", ["qad-harf", "al-hal-jumla-wa-rabituha", "anwa-al-waw"], "الْوَاوُ وَاوُ الْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ يُقَرِّبُ الْمَاضِيَ مِنَ الْحَالِ.", "The waw of hal; قَدْ affirms, and brings the past close to the present.", "Vâv hâliyyedir; «kad» tahkîk harfidir, mâzîyi hâle yaklaştırır.", segs=SG(("وَ", "wa", "conj"), ("قَدْ", "qad", "part"))),
  T("نَأَتْ", "naa", "verb", ["naqis-verbs", "al-hal-jumla-wa-rabituha"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى نَوَارَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَوَارَ». النَّأْيُ: الْبُعْدُ (الزَّوْزَنِيُّ).", "Past verb built on a fatha estimated on the alif, which has dropped before the quiescent ta of the feminine; the doer is the hidden «she» — Nawār — and the clause is a hal of «Nawār», in the seat of nasb. نَأْي is being far (al-Zawzanī).", "Sâkin te'nîs tâ'sı sebebiyle düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil Nevâr'a dönen gizli «o» — cümle «Nevâr»dan hâl, mahallen mansûb. «Ne'y»: uzaklık (Zevzenî).")],
 [V("mt", "وَتَقَطَّعَتْ", "taqattaa", c="w", g=["form-v-verbs"], n=(" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْحَالِ", " — the clause is joined to the hal-clause", " — cümle hâl cümlesine ma'tûftur")),
  R("fail", "أَسْبَابُهَا", "sabab", enc="هَا", g=["jam-taksir", "tibaq"]),
  R("atfr", "وَرِمَامُهَا", "rumma", c="w", enc="هَا", g=["jam-taksir", "tibaq", "istiara"], n=N3(ZW("الرِّمَامُ: جَمْعُ الرُّمَّةِ وَهِيَ قِطْعَةٌ مِنَ الْحَبْلِ خَلَقَةٌ ضَعِيفَةٌ؛ وَالْمَعْنَى: تَقَطَّعَتْ أَسْبَابُ وِصَالِهَا مَا قَوِيَ مِنْهَا وَمَا ضَعُفَ — فَالْحِبَالُ مُسْتَعَارَةٌ لِعَلَائِقِ الْوِصَالِ: اسْتِعَارَةٌ تَصْرِيحِيَّةٌ", "رِمَام is the plural of رُمَّة, a worn, weak piece of rope; the sense is «the ties of union with her are cut, the strong of them and the weak» — the ropes are borrowed for the bonds of love: an istiʿāra taṣrīḥiyya", "«rimâm»: «rumme»nin cem'i: eskimiş, zayıf ip parçası; mâna: «onunla vuslat bağları, sağlamı da zayıfı da koptu» — ipler vuslat bağları için istiare edilmiştir: istiâre-i tasrîhiyye"), HADD("طِبَاقٌ بَيْنَ «أَسْبَابُهَا» وَ«رِمَامُهَا»، وَالتَّقَابُلُ فِي تَفْسِيرِ الزَّوْزَنِيِّ: مَا قَوِيَ وَمَا ضَعُفَ", "«her ropes» and «her frayed ends» make a tibaq; the opposition is in al-Zawzanī's gloss: the strong and the weak", "«esbâb» ile «rimâm» arasında tıbâk vardır; karşıtlık Zevzenî'nin açıklamasındadır: sağlam olan ve zayıf olan")))])
VV(17, "A woman of Murra: she has settled at Fayd and become a neighbour of the people of the Ḥijāz — so how are you to reach her?",
  "O, Mürre kabilesinden bir kadındır; Feyd'e yerleşmiş, Hicaz halkına komşu olmuştur — sen ona nereden ulaşacaksın?",
 [R("khb", "مُرِّيَّةٌ", "lb-murri", g=["ism-mansub", "hadhf-wa-taqdir"], n=N3((" — لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ (الدُّرَّةُ)", " — of an omitted mubtada, «she is» (al-Durra)", " — mahzûf mübtedânın haberi: «o» (Dürre)"), ZW("مَنْسُوبَةٌ إِلَى مُرَّةَ", "of the tribe of Murra", "Mürre kabilesine mensup"))),
  V("mt", "حَلَّتْ", "halla-settle", g=["doubled-verbs", "jumla-sifa"], doer=NAWAR, n=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«مُرِّيَّةٌ»", " — the clause is a na't of «a woman of Murra», in the seat of raf'", " — cümle «Mürreli kadın»ın na'tı, mahallen merfû")),
  R("majr", "بِفَيْدَ", "lb-fayd", j="bi", pos="propn", g=["mamnu-min-sarf"], sign=DIPT_F3, n=N3(MT("حَلَّتْ", "has settled", "yerleşti»ye"), ZW("فَيْدُ: بَلَدٌ مَعْرُوفٌ، وَلَمْ يَصْرِفْهَا لِاسْتِجْمَاعِهَا التَّأْنِيثَ وَالتَّعْرِيفَ، وَصَرْفُهَا سَائِغٌ أَيْضًا كَهِنْدَ وَدَعْدَ", "Fayd is a well-known town; he gives it no tanwin because it is both feminine and a proper name, though tanwin is allowed too, as with Hind and Daʿd", "Feyd bilinen bir beldedir; hem müennes hem alem olduğu için tenvinlememiştir; Hind ve Da'd gibi tenvinlenmesi de caizdir"))),
  V("mt", "وَجَاوَرَتْ", "jawara", c="w", g=["form-iii-verbs"], doer=NAWAR, n=ZW("يُرِيدُ أَنَّهَا تَحُلُّ بِفَيْدَ أَحْيَانًا وَتُجَاوِرُ أَهْلَ الْحِجَازِ أَحْيَانًا، لِأَنَّ بَيْنَهُمَا مَسَافَةً بَعِيدَةً", "he means that she is at Fayd at some seasons and beside the people of the Ḥijāz at others, for the two lie far apart", "kastı, onun bazen Feyd'de konakladığı, bazen Hicaz halkına komşu olduğudur; çünkü ikisinin arası uzaktır"))],
 [R("maf", "أَهْلَ", "ahl", mud=True),
  R("mdf", "الْحِجَازِ", "lb-hijaz", pos="propn"),
  T("فَأَيْنَ", "ayna", "noun", ["al-istifham", "khuruj-al-istifham", "maful-fih", "mubtada-khabar", "taqdim-al-musnad"],
     "الْفَاءُ عَاطِفَةٌ — وَالِاسْتِئْنَافُ مُمْكِنٌ (الدُّرَّةُ) — وَأَيْنَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ. وَالِاسْتِفْهَامُ لَيْسَ عَلَى حَقِيقَتِهِ بَلْ لِلِاسْتِبْعَادِ: أَيْ تَعَذَّرَ عَلَيْكَ طَلَبُهَا، وَكَيْفَ يَتَيَسَّرُ لَكَ الْوُصُولُ إِلَيْهَا؟ (الزَّوْزَنِيُّ).",
     "The fa conjoins — or opens a new clause (al-Durra); أَيْنَ is the interrogative noun, built on fatha, in the seat of nasb as an adverb of place that hangs on an omitted, fronted khabar. The question is not a real one: it puts the thing out of reach — «seeking her is beyond you; how should you come to her?» (al-Zawzanī).",
     "Fâ atıf içindir — isti'nâf da mümkündür (Dürre); «eyne» fetha üzere mebnî istifhâm ismi, mahallen mansûb mekân zarfı; mahzûf mukaddem habere mütealliktir. İstifhâm hakiki değildir, istib'âd içindir: «onu aramak sana imkânsız oldu; ona ulaşmak nasıl kolay olsun?» (Zevzenî).",
     segs=SG(("فَ", "fa", "conj"), ("أَيْنَ", "ayna", "noun"))),
  JP("مِنْكَ", "min", "كَ", n=(" — مُتَعَلِّقَانِ بِالْخَبَرِ الْمَحْذُوفِ؛ وَالْخِطَابُ لِنَفْسِهِ", "; the phrase hangs on the omitted khabar; the «you» is himself", "; mahzûf habere müteallik; hitap kendinedir")),
  R("mub", "مَرَامُهَا", "lb-maram", enc="هَا", n=ZW("مُبْتَدَأٌ مُؤَخَّرٌ. الْمَرَامُ: الْمَطْلَبُ", "placed after its khabar. مَرَام is «the seeking, the place where one seeks»", "haberinden sonraya bırakılmıştır. «Merâm»: arama, talep"))])
VV(18, "— on the eastern sides of the Two Mountains, or at Muḥajjar; then Farda takes her in, and the Rukhām that lies next to it;",
  "— İki Dağ'ın doğu yakalarında yahut Muhaccer'de; sonra onu Ferde ve ona bitişik Ruhâm barındırır;",
 [R("majr", "بِمَشَارِقِ", "mashriq", j="bi", mud=True, g=["jam-taksir", "hadhf-wa-taqdir"], n=N3((" — وَجُرَّ بِالْكَسْرَةِ مَعَ أَنَّهُ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ لِأَنَّهُ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: حَلَّتْ (الدُّرَّةُ)", " — it takes the kasra, though a «farthest plural», because it is annexed; the phrase hangs on an omitted verb, «she has settled» (al-Durra)", " — muntehe'l-cumû' vezninde olduğu hâlde muzâf olduğu için kesre ile mecrûrdur; câr-mecrûr mahzûf bir fiile müteallik: «yerleşti» (Dürre)"), ZW("أَيْ جَوَانِبِهِمَا الَّتِي تَلِي الْمَشْرِقَ", "that is, their sides that face the east", "yani doğuya bakan yanları"))),
  R("mdf", "الْجَبَلَيْنِ", "jabal", g=["al-muthanna"], sign=("بِالْيَاءِ لِأَنَّهُ مُثَنًّى", " by the ya, for it is a dual", " — tesniye olduğu için yâ ile"), n=ZW("عَنَى بِالْجَبَلَيْنِ جَبَلَيْ طَيِّئٍ: أَجَأً وَسَلْمَى", "by «the Two Mountains» he means the two mountains of Ṭayyiʾ, Ajaʾ and Salmā", "«İki Dağ» ile Tay kabilesinin iki dağını, Ece ve Selmâ'yı kasteder")),
  T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «yahut»."),
  R("majr", "بِمُحَجَّرٍ", "lb-muhajjar", j="bi", pos="propn", n=N3((" — مَعْطُوفَانِ عَلَى «بِمَشَارِقِ»", " — joined to «on the eastern sides»", " — «doğu yakalarında»ya ma'tûf"), ZW("الْمُحَجَّرُ: جَبَلٌ آخَرُ", "Muḥajjar is another mountain", "Muhaccer başka bir dağdır")))],
 [V("mt", "فَتَضَمَّنَتْهَا", "tadammana", c="f", enc="هَا", g=["form-v-verbs"], n=ZW("تَضَمَّنَ الْمَوْضِعُ فُلَانًا: إِذَا حَصَلَ فِيهِ", "a place تَضَمَّنَ someone when he has come to be in it", "bir yer birini «tazammun» eder: o kimse orada bulunur")),
  R("fail", "فَرْدَةٌ", "lb-farda", pos="propn", n=N3(ZW("جَبَلٌ مُنْفَرِدٌ عَنْ سَائِرِ الْجِبَالِ، سُمِّيَ بِهَا لِانْفِرَادِهَا", "a mountain standing apart from the rest, named for its standing alone", "diğer dağlardan ayrı duran bir dağ; tek başına durduğu için bu adı almıştır"), SURIFA)),
  R("atfr", "فَرُخَامُهَا", "lb-rukham", c="f", enc="هَا", pos="propn", n=ZW("رُخَامٌ: أَرْضٌ مُتَّصِلَةٌ بِفَرْدَةَ، لِذٰلِكَ أَضَافَهَا إِلَيْهَا. وَإِنَّمَا يُحْصِي مَنَازِلَهَا عِنْدَ حُلُولِهَا بِفَيْدَ، وَهٰذِهِ الْجِبَالُ قَرِيبَةٌ مِنْهَا بَعِيدَةٌ مِنَ الْحِجَازِ", "Rukhām is a tract adjoining Farda, which is why he annexes it to it. He is counting her halting-places when she is at Fayd: these mountains are near it and far from the Ḥijāz", "Ruhâm, Ferde'ye bitişik bir arazidir; bu yüzden onu ona izâfe etmiştir. Feyd'de konakladığı zamanki menzillerini saymaktadır; bu dağlar Feyd'e yakın, Hicaz'a uzaktır"))])
VV(19, "then Ṣuwāʾiq — if she goes towards Yemen, then the likely place for her there is Wiḥāf al-Qahr, or its Ṭilkhām.",
  "sonra Suvâik — Yemen tarafına giderse, orada bulunması umulan yer Vihâfü'l-Kahr yahut oranın Tılhâm'ıdır.",
 [R("atfr", "فَصُوَائِقٌ", "lb-sawaiq", c="f", pos="propn", n=N3((" — مَعْطُوفٌ عَلَى «فَرْدَةٌ» فِي الْبَيْتِ قَبْلَهُ (الدُّرَّةُ)", " — joined to «Farda» in the verse before (al-Durra)", " — önceki beyitteki «Ferde»ye ma'tûf (Dürre)"), ZW("صُوَائِقُ: مَوْضِعٌ مَعْرُوفٌ", "Ṣuwāʾiq is a well-known place", "Suvâik bilinen bir yerdir"), SURIFA)),
  T("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "The conditional particle «if», which puts two verbs in jazm.", "Cezmeden şart harfi «eğer»."),
  V("mt", "أَيْمَنَتْ", "lb-aymana", g=["form-iv-verbs", "mithal-verbs", "in-shartiyya"], doer=NAWAR, n=N3((" — وَهُوَ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "; it stands in the seat of jazm as the verb of the condition", "; şart fiili olarak mahallen meczûm"), ZW("أَيْمَنَ الرَّجُلُ: إِذَا أَتَى الْيَمَنَ، مِثْلُ أَعْرَقَ إِذَا أَتَى الْعِرَاقَ", "أَيْمَنَ: he went to Yemen, as أَعْرَقَ is «he went to Iraq»", "«eymene»: Yemen'e gitti; «a'raka»nın «Irak'a gitti» olması gibi"))),
  R("khb", "فَمَظِنَّةٌ", "mazinna", c="fj", g=["al-fa-fi-jawab-al-shart", "taqdim-al-musnad"], n=N3((" — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ (الدُّرَّةُ)", " — a fronted khabar; the nominal clause is the answer of the condition, in the seat of jazm (al-Durra)", " — mukaddem haber; isim cümlesi şartın cevabı, mahallen meczûm (Dürre)"), ZW("مَظِنَّةُ الشَّيْءِ: حَيْثُ يُظَنُّ كَوْنُهُ فِيهِ، وَهُوَ مِنَ الظَّنِّ بِالظَّاءِ", "the مَظِنَّة of a thing is where it is thought to be — from ظَنّ, with ẓāʾ", "bir şeyin «mazınne»si: bulunduğu zannedilen yer; zâ ile «zann»dan")))],
 [JP("فِيهَا", "fi", "هَا", n=(" — مُتَعَلِّقَانِ بِـ«مَظِنَّةٌ»، وَالضَّمِيرُ لِصُوَائِقَ؛ وَرِوَايَةُ الدُّرَّةِ «مِنْهَا»", "; the phrase hangs on «the likely place»; «it» is Ṣuwāʾiq; al-Durra's text reads مِنْهَا", "; «mazınne»ye müteallik; zamir Suvâik'e döner; Dürre'nin rivayeti «minhâ»dır")),
  R("mub", "وِحَافُ", "lb-wihaf", mud=True, pos="propn", n=ZW("مُبْتَدَأٌ مُؤَخَّرٌ. وِحَافُ الْقَهْرِ — بِالرَّاءِ غَيْرَ مُعْجَمَةٍ، وَمِنْهُمْ مَنْ رَوَاهُ بِالزَّايِ — مَوْضِعٌ مَعْرُوفٌ", "placed after its khabar. Wiḥāf al-Qahr — with rāʾ; some read it with zāy — is a well-known place", "haberinden sonraya bırakılmıştır. Vihâfü'l-Kahr — râ iledir; zâ ile rivayet eden de vardır — bilinen bir yerdir")),
  R("mdf", "الْقَهْرِ", "lb-qahr", pos="propn"),
  T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «yahut»."),
  R("atfr", "طِلْخَامُهَا", "lb-tilkham", enc="هَا", pos="propn", n=ZW("طِلْخَامٌ: مَوْضِعٌ مَعْرُوفٌ أَيْضًا؛ وَهُمَا خَاصَّانِ بِالْإِضَافَةِ إِلَى صُوَائِقَ: إِنْ أَتَتِ الْيَمَنَ حَلَّتْ بِوِحَافِ الْقَهْرِ أَوْ طِلْخَامٍ مِنْ صُوَائِقَ", "Ṭilkhām too is a well-known place; the two are particular parts of Ṣuwāʾiq: if she goes to Yemen she settles at Wiḥāf al-Qahr or at Ṭilkhām, within Ṣuwāʾiq", "Tılhâm da bilinen bir yerdir; ikisi Suvâik'e nisbetle hususî yerlerdir: Yemen'e giderse Suvâik'in Vihâfü'l-Kahr'ına yahut Tılhâm'ına yerleşir"))])
VV(20, "So cut off your need of one whose bond is ready to give way — the worst of those who keep a friendship is the one who is quick to break it.",
  "Öyleyse bağı kopmaya yüz tutmuş kimseden dileğini kes — dostluğu sürdürenlerin en kötüsü onu çabucak kesip atandır.",
 [T("فَاقْطَعْ", "qataa", "verb", ["imperative-amr", "al-fail-al-mudmar-al-mustatir-wujuban", "tajrid", "tibaq"],
     "الْفَاءُ لِلِاسْتِئْنَافِ، وَاقْطَعْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — أَضْرَبَ عَنْ ذِكْرِ نَوَارَ وَأَقْبَلَ عَلَى نَفْسِهِ مُخَاطِبًا إِيَّاهَا (الزَّوْزَنِيُّ): فَالْأَمْرُ تَجْرِيدٌ بِمُخَاطَبَةِ الْإِنْسَانِ نَفْسَهُ — وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — طِبَاقٌ بَيْنَ «اقْطَعْ» وَ«وَصْلُهُ»: فِعْلٌ وَاسْمٌ مُتَضَادَّانِ.",
     "The fa opens a new clause; اقْطَعْ is an imperative built on sukun, and its doer, «you», must stay hidden. He turns from Nawār to himself and addresses his own soul (al-Zawzanī): the command is a tajrīd, the man speaking to himself. By the Talkhīṣ's definition «cut» and «his bond» make a tibaq: a verb and a noun that are opposites.",
     "Fâ isti'nâf içindir; «ıkta'» sükûn üzere mebnî emir, fâili vücûben gizli «sen». Nevâr'ı anmayı bırakıp kendi nefsine dönerek ona hitap eder (Zevzenî): emir, kişinin kendine hitabı yoluyla tecrîddir. Telhîs'in tarifine göre «kes» ile «vaslı» arasında tıbâk vardır: zıt bir fiil ile bir isim.",
     segs=SG(("فَ", "fa", "conj"), ("اقْطَعْ", "qataa", "verb"))),
  R("maf", "لُبَانَةَ", "lb-lubana", mud=True, n=ZW("اللُّبَانَةُ: الْحَاجَةُ؛ أَيْ لُبَانَتَكَ مِنْهُ، لِأَنَّ قَطْعَ لُبَانَتِهِ مِنْكَ لَيْسَ إِلَيْكَ", "لُبَانَة is a need, a desire; that is, «your need of him» — for cutting off his need of you is not in your hands", "«lübâne»: ihtiyaç, dilek; yani «senin ondan dileğini» — çünkü onun senden dileğini kesmek senin elinde değildir")),
  T("مَنْ", "man-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A relative noun «the one who», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «…-en kimse», sükûn üzere mebnî; muzâfun ileyh olarak mahallen mecrûr."),
  V("m", "تَعَرَّضَ", "taarrada", g=["form-v-verbs"], n=ZW("وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا؛ أَيْ مَنْ كَانَ وَصْلُهُ مُعَرَّضًا لِلزَّوَالِ وَالِانْتِقَاضِ", "the clause is the relative's ṣila and has no seat; that is, one whose bond lies open to ending and undoing", "cümle sıla cümlesidir, mahalli yoktur; yani bağı sona ermeye ve bozulmaya yüz tutmuş kimse")),
  R("fail", "وَصْلُهُ", "wasl", enc="هُ", g=["masdar", "tibaq", "mulhaq-bil-jinas"])],
 [T("وَلَشَرُّ", "sharr", "noun", ["mubtada-khabar", "huruf-al-qasam-fil-kafiya", "ism-tafdil", "idafa-definiteness"],
     "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ وَالْمُقْسَمُ بِهِ مَحْذُوفٌ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ (الدُّرَّةُ)، وَشَرُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَهُوَ اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ. وَيُرْوَى: «وَلَخَيْرُ وَاصِلِ»، وَهِيَ أَوْجَهُ الرِّوَايَتَيْنِ عِنْدَ الزَّوْزَنِيِّ.",
     "The waw is the jarr letter of oath, the thing sworn by left out, and the lam opens the oath's answer (al-Durra); شَرُّ is the mubtada, in raf', annexed — an elative that has lost its hamza. It is also read وَلَخَيْرُ وَاصِلِ «the best of those who keep …», which al-Zawzanī thinks the better of the two readings.",
     "Vâv kasem ve cer harfidir, yemin edilen hazfedilmiştir; lâm kasemin cevabına dahildir (Dürre); «şerru» mübtedâ, merfû, muzâf — hemzesi düşmüş ism-i tafdîl. «Ve le-hayru vâsıli» diye de rivayet edilir; Zevzenî'ye göre iki rivayetin daha yerindesi budur.",
     segs=SG(("وَ", "wa", "conj"), ("لَ", "lam-qasam", "part"), ("شَرُّ", "sharr", "noun"))),
  R("mdf", "وَاصِلِ", "wasil", mud=True, g=["ism-fail", "tibaq", "mulhaq-bil-jinas"], n=N3((" — مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ (الدُّرَّةُ)", " — the active participle annexed to its object (al-Durra)", " — ism-i fâil mef'ûlüne muzâftır (Dürre)"), HADD("إِلْحَاقٌ بِالْجِنَاسِ بَيْنَ «وَصْلُهُ» وَ«وَاصِلِ»: يَجْمَعُهُمَا الِاشْتِقَاقُ", "«his bond» and «one who keeps» are joined to the jinās: one root gathers them", "«vaslı» ile «vâsıl» cinâsa mülhaktır: ikisini iştikak birleştirir"))),
  R("mdf", "خُلَّةٍ", "lb-khulla", n=ZW("الْخُلَّةُ: الْمَوَدَّةُ الْمُتَنَاهِيَةُ، وَالْخَلِيلُ وَالْخِلُّ وَالْخُلَّةُ وَاحِدٌ", "خُلَّة is love at its utmost; and خَلِيل, خِلّ and خُلَّة are one — «a close friend»", "«hulle»: son derecede sevgi; «halîl», «hıll» ve «hulle» aynıdır — «yakın dost»")),
  R("khb", "صَرَّامُهَا", "lb-sarram", enc="هَا", g=["sighat-mubalagha", "tibaq"], n=N3(ZW("الصَّرَّامُ: الْقَطَّاعُ، فَعَّالٌ مِنَ الصَّرْمِ وَهُوَ الْقَطْعُ؛ أَيْ شَرُّ وَاصِلِي الْأَحْبَابِ قَطَّاعُهَا", "صَرَّام is «one who cuts again and again», a فَعَّال from صَرْم, cutting; that is, the worst of those who keep friends is the one who breaks with them", "«sarrâm»: çokça kesen; kesmek anlamındaki «sarm»dan «fa''âl»; yani dostluk sürdürenlerin en kötüsü onu kesip atandır"), HADD("طِبَاقٌ بَيْنَ «وَاصِلِ» وَ«صَرَّامُهَا»: اسْمَانِ مُتَضَادَّانِ", "«one who keeps» and «one who breaks it» make a tibaq: two nouns that are opposites", "«vâsıl» ile «sarrâm» arasında tıbâk vardır: zıt iki isim")))])
VV(21, "And give your full affection to the one who deals fairly with you — though breaking with him is still open to you, should the friendship go lame and its prop give way.",
  "Sana güzel davranana da tam ve bol bir sevgi sun — fakat dostluk aksar ve dayanağı eğrilirse ondan kopmak yine elindedir.",
 [T("وَاحْبُ", "lb-haba", "verb", ["imperative-amr", "naqis-verbs", "al-fail-al-mudmar-al-mustatir-wujuban", "atf-nasaq"],
     "الْوَاوُ عَاطِفَةٌ، وَاحْبُ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ (الْوَاوِ)، وَالضَّمَّةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — حَبَوْتُهُ بِكَذَا أَحْبُوهُ حِبَاءً: إِذَا أَعْطَيْتُهُ إِيَّاهُ (الزَّوْزَنِيُّ).",
     "The waw conjoins; احْبُ is an imperative built on the dropping of its weak letter (the waw), the damma left as its trace; the doer «you» must stay hidden. حَبَوْتُهُ بِكَذَا: I bestowed such a thing on him (al-Zawzanī).",
     "«ve» + «uhbü»: illet harfinin (vâvın) hazfi üzere mebnî emir; önceki damme ona delildir; fâil vücûben gizli «sen». «Habevtühû bi-kezâ»: ona şunu bağışladım (Zevzenî).",
     segs=SG(("وَ", "wa", "conj"), ("احْبُ", "lb-haba", "verb"))),
  R("maf", "الْمُجَامِلَ", "lb-mujamil", g=["ism-fail"], n=ZW("الْمُجَامِلُ: الْمُصَانِعُ؛ وَيُرْوَى «الْمُحَامِلَ» أَيِ الَّذِي يَتَحَمَّلُ أَذَاكَ كَمَا تَتَحَمَّلُ أَذَاهُ", "مُجَامِل is one who deals courteously with you; also read الْمُحَامِلَ, one who bears with you as you bear with him", "«mücâmil»: sana güzel muamele eden; «el-muhâmil» diye de rivayet edilir: senin eziyetine katlandığın gibi eziyetine katlanan")),
  R("majr", "بِالْجَزِيلِ", "jazil", j="bi", g=["hadhf-wa-taqdir"], n=N3(MT("احْبُ", "give", "sun»a"), ZW("أَيِ الْوُدِّ الْجَزِيلِ؛ وَالْجَزَالَةُ: الْكَمَالُ وَالتَّمَامُ", "that is, «with ample affection»; جَزَالَة is fullness and completeness", "yani «bol sevgiyle»; «cezâlet»: kemal ve tamlık"))),
  R("mub", "وَصَرْمُهُ", "sarm", c="wh", enc="هُ", g=["masdar", "al-hal-jumla-wa-rabituha"], n=N3((" — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الْمُجَامِلَ» (الدُّرَّةُ)", " — the nominal clause is a hal of «the one who deals fairly», in the seat of nasb (al-Durra)", " — isim cümlesi «güzel davranan»dan hâl, mahallen mansûb (Dürre)"), ZW("الصَّرْمُ: الْقَطِيعَةُ", "صَرْم is breaking off", "«sarm»: ilişkiyi kesmek")))],
 [R("khb", "بَاقٍ", "baqi", g=["ism-fail", "ism-maqsur-manqus"], sign=("بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", " — by a damma estimated on the ya, which has dropped before the tanwin", " — tenvin sebebiyle düşen yâ üzerinde takdîrî damme ile"), n=ZW("أَيْ فَأَنْتَ قَادِرٌ عَلَى صَرْمِهِ وَقَطِيعَتِهِ", "that is, you still have it in your power to break with him", "yani ondan kopmaya hâlâ gücün yeter")),
  T("إِذَا", "idha", "noun", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«بَاقٍ» (الدُّرَّةُ)، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time to come, built on sukun, in the seat of nasb; it hangs on «still open» (al-Durra) and is annexed to the clause after it.", "Gelecek zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «bâkî»ye mütealliktir (Dürre) ve sonraki cümleye muzâftır."),
  V("mt", "ظَلَعَتْ", "lb-zalaa", g=["istiara", "istiara-tabaiyya"], doer=DZ("هِيَ يَعُودُ عَلَى الْخُلَّةِ", "«she» — the friendship", "dostluğa dönen gizli «o»"), n=N3((" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", " — the clause is in the seat of jarr, إِذَا being annexed to it", " — cümle, «izâ» kendisine muzâf olduğu için mahallen mecrûr"), ZW("الظَّلْعُ: غَمْزٌ فِي الدَّوَابِّ؛ أَيْ إِنْ ضَعُفَتْ أَسْبَابُهَا وَدَعَائِمُهَا — فَالظَّلْعُ مُسْتَعَارٌ لِضَعْفِ الْمَوَدَّةِ: اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ", "ظَلْع is a limp in a beast; that is, «if its ties and props grow weak» — the limp is borrowed for the weakening of affection: an istiʿāra taṣrīḥiyya tabaʿiyya", "«zal'»: hayvanlardaki aksama; yani «bağları ve dayanakları zayıflarsa» — aksama, sevginin zayıflaması için istiare edilmiştir: istiâre-i tasrîhiyye tebeiyye"))),
  V("m", "وَزَاغَ", "zagha", c="w", g=["hollow-verbs"], n=ZW("الزَّيْغُ: الْمَيْلُ", "زَيْغ is leaning aside", "«zeyğ»: eğrilmek, meyletmek")),
  R("fail", "قِوَامُهَا", "qiwam", enc="هَا", n=ZW("قِوَامُ الشَّيْءِ: مَا يَقُومُ بِهِ؛ وَالْمُضْمَرُ لِلْخُلَّةِ", "the قِوَام of a thing is what it stands by; the pronoun is the friendship", "bir şeyin «kıvâm»ı: onu ayakta tutan şey; zamir dostluğa döner"))])

# ==== TAIL (lexicon, manifest, writing) — new verses go ABOVE this line ==================================================
POEM_END = 88
PLAN = [(1, 7), (8, 15), (16, 21), (22, 29), (30, 35), (36, 41), (42, 47), (48, 54), (55, 61), (62, 69), (70, 76), (77, 82), (83, 88)]
TITLES_ALL = [
 {"ar": "خَبَرُ لَبِيدٍ", "en": "Labīd's Story", "tr": "Lebîd'in Haberi"},
 {"ar": "الدِّيَارُ الْعَافِيَةُ", "en": "The Effaced Dwellings", "tr": "Silinmiş Yurtlar"},
 {"ar": "سُؤَالُ الطُّلُولِ، وَظُعُنُ الْحَيِّ", "en": "Questioning the Ruins, and the Tribe's Departing Litters", "tr": "Kalıntılara Soru ve Kabilenin Göç Eden Hevdeçleri"},
 {"ar": "نَوَارُ، وَقَطْعُ اللُّبَانَةِ", "en": "Nawār, and Cutting the Bond", "tr": "Nevâr ve Bağın Kesilmesi"},
 {"ar": "النَّاقَةُ، وَالْأَتَانُ وَفَحْلُهَا", "en": "The She-Camel, and the Wild Ass with Her Mate", "tr": "Dişi Deve ile Yaban Eşeği ve Erkeği"},
 {"ar": "وُرُودُ الْعَيْنِ", "en": "Down to the Spring", "tr": "Pınara İniş"},
 {"ar": "الْبَقَرَةُ الْمَسْبُوعَةُ", "en": "The Wild Cow Robbed of Her Calf", "tr": "Yavrusu Yırtıcılara Yem Olan Yaban İneği"},
 {"ar": "لَيْلَةُ الْمَطَرِ، وَسَبْعُ لَيَالٍ", "en": "The Night of Rain, and Seven Nights of Searching", "tr": "Yağmur Gecesi ve Yedi Gecelik Arayış"},
 {"ar": "الرُّمَاةُ وَالْكِلَابُ", "en": "The Hunters and the Hounds", "tr": "Avcılar ve Tazılar"},
 {"ar": "لَيَالِي اللَّهْوِ وَالْمُدَامِ", "en": "Nights of Company and Wine", "tr": "Eğlence ve Şarap Geceleri"},
 {"ar": "غَدَاةُ الرِّيحِ، وَالْفَرَسُ فِي الثَّغْرِ", "en": "The Windy Morning, and the Mare on the Frontier", "tr": "Rüzgârlı Sabah ve Sınırda Kısrak"},
 {"ar": "الْمَجْلِسُ، وَالْجَزُورُ، وَالضَّيْفُ", "en": "The Assembly, the Slaughter-Camel and the Guest", "tr": "Meclis, Kesimlik Deve ve Misafir"},
 {"ar": "فَخْرُ الْقَوْمِ", "en": "The Pride of the Tribe", "tr": "Kavmin Övüncü"},
 {"ar": "قِسْمَةُ الْمَلِيكِ، وَخَاتِمَةُ الْقَصِيدَةِ", "en": "What the King Has Apportioned, and the Close of the Ode", "tr": "Melîk'in Taksimi ve Kasidenin Sonu"},
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
FORCE = {"haram": "kitab-al-sulh"}
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k, lemma):
    for p in PREF:
        if k in _MO[p] and _G[p].get(k, {}).get("lemma") == lemma: return _MO[p][k]
    return None
# a reused entry keeps its lemma, root and level; where its shelf gloss was written for another book, the gloss is fitted to the poem
TAILOR = {
 "afa": ("to be effaced, to be wiped out (intransitive, as in v. 1); to efface; to pardon (عَفَا يَعْفُو)", "silinmek, izi kalmamak (1. beyitteki gibi lâzım); silmek; affetmek (عَفَا يَعْفُو)"),
 "dar": ("a dwelling, an abode; a tribe's camping-ground (pl. دِيَار، دُور)", "ev, yurt; kabilenin konak yeri (ç. دِيَار، دُور)"),
 "mahall": ("a place where one alights; in v. 1 the part of a camp used for a few days' halt", "konulan yer; 1. beyitte yurdun birkaç günlük konak yeri"),
 "damina": ("to hold within itself, to contain; to guarantee (ضَمِنَ يَضْمَنُ)", "içinde tutmak, ihtiva etmek; kefil olmak (ضَمِنَ يَضْمَنُ)"),
 "anis": ("a companion; (collective) the people of a place, those who make it lived-in", "can yoldaşı; (topluluk ismi) bir yerin sakinleri, orayı şenlendirenler"),
 "halal": ("lawful, free; in v. 3 the months in which fighting is free (أَشْهُرُ الْحِلِّ)", "helâl, serbest; 3. beyitte savaşın serbest olduğu aylar (hill ayları)"),
 "haram": ("forbidden, sacred; in v. 3 the sacred months (الْأَشْهُرُ الْحُرُمُ)", "haram, mukaddes; 3. beyitte haram aylar"),
 "far-branch": ("a branch, the upper shoot of a plant (pl. فُرُوع)", "dal, bitkinin üst sürgünü (ç. فُرُوع)"),
 "sakin": ("at rest, still, quiet; dwelling (ism fa'il of سَكَنَ)", "sakin, durgun; oturan (سَكَنَ'den ism-i fâil)"),
 "jafar": ("Jaʿfar — here Jaʿfar ibn Kilāb, forefather of Labīd's clan (the Banū Jaʿfar)", "Ca'fer — burada Ca'fer b. Kilâb, Lebîd'in boyunun (Benî Ca'fer) atası"),
 "banu": ("sons; بَنُو فُلَانٍ «the sons of So-and-so», a tribe (declines like the sound masculine plural: بَنُو، بَنِي)", "oğullar; بَنُو فُلَانٍ «falan oğulları», kabile (cem-i müzekker sâlim gibi çekilir: بَنُو، بَنِي)"),

 "matn": ("the back, the surface of a thing; in v. 8 the face of a written page, its text (pl. مُتُون)", "bir şeyin sırtı, yüzü; 8. beyitte yazılı sahifenin yüzü, metni (ç. مُتُون)"),
 "asamm": ("solid, hard; deaf (pl. صُمّ)", "sert, katı; sağır (ç. صُمّ)"),
 "taarrada": ("to show itself, to stand out (Form V); to put oneself in the way of", "görünmek, belirmek (tefa''ul); bir şeyin önüne çıkmak"),
 "tahammala": ("to load up and move off (of a tribe breaking camp) (Form V); to bear", "yükünü yükleyip göç etmek (tefa''ul); yüklenmek"),
 "atif": ("bending (the neck); tender, compassionate (ism fa'il of عَطَفَ; pl. عُطَّف)", "(boynunu) büken; şefkatli (عَطَفَ'den ism-i fâil; ç. عُطَّف)"),
 "jala": ("to uncover, to lay bare; to make plain (جَلَا يَجْلُو)", "açığa çıkarmak, üstünü açmak (جَلَا يَجْلُو)"),

 "sabab": ("a rope; a tie, a means, whatever leads to a thing (pl. أَسْبَاب)", "ip; bağ, vasıta, bir şeye ulaştıran şey (ç. أَسْبَاب)"),
 "rumma": ("a worn, weak piece of rope (pl. رِمَام، رُمَم)", "eskimiş, zayıf ip parçası (ç. رِمَام، رُمَم)"),
 "tadammana": ("to take in, to hold within itself (Form V): تَضَمَّنَهُ الْمَوْضِعُ, he came to be in the place", "içine almak, barındırmak (tefa''ul): تَضَمَّنَهُ الْمَوْضِعُ, o yerde bulundu"),
 "wasil": ("one who joins, who keeps up a bond (ism fa'il of وَصَلَ); one who arrives", "bağı sürdüren, vuslat eden (وَصَلَ'den ism-i fâil); ulaşan"),
 "wasl": ("joining, union; keeping up a bond (masdar of وَصَلَ)", "birleşme, vuslat; bağı sürdürme (وَصَلَ'nin masdarı)"),
 "mashriq": ("the east, the side that faces the sunrise (pl. مَشَارِق)", "doğu, güneşin doğduğu yana bakan taraf (ç. مَشَارِق)"),
}
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

NEW_GLOSS = {
 # ---- the khabar ----
 "lb-labid": P("لَبِيد", "Labīd ibn Rabīʿa al-ʿĀmirī (d. c. 41 AH), poet of the Muʿallaqa, a Companion", "Lebîd b. Rebîa el-Âmirî (ö. yak. 41 h.), muallaka şairi, sahâbî"),
 "lb-wafd": N("وَفْد", "و ف د", "a delegation, envoys who come to a ruler (pl. وُفُود)", "heyet, bir hükümdara gelen elçiler topluluğu (ç. وُفُود)", "وُفُود"),
 "lb-kilab": P("كِلَاب", "Kilāb — Kilāb ibn Rabīʿa, of ʿĀmir ibn Ṣaʿṣaʿa; the tribe descended from him", "Kilâb — Kilâb b. Rebîa (Âmir b. Sa'saa'dan); onun soyundan gelen kabile"),
 "lb-wafat": N("وَفَاة", "و ف ي", "death (pl. وَفَيَات)", "vefat, ölüm (ç. وَفَيَات)", "وَفَيَات"),
 "lb-muawiya": P("مُعَاوِيَة", "Muʿāwiya ibn Abī Sufyān, the first Umayyad caliph (r. 41–60 AH); a diptote", "Muâviye b. Ebî Süfyân, ilk Emevî halifesi (h. 41–60); gayr-i munsarif"),
 # ---- vv. 1–7 ----
 "lb-muqam": N("مُقَام", "ق و م", "a place of long stay, an abode (noun of place of أَقَامَ)", "uzun süre kalınan yer, ikametgâh (أَقَامَ'den ism-i mekân)"),
 "lb-mina": P("مِنًى", "Minā — in v. 1 a place in the reserve of Ḍariyya in Najd, not the Minā of Mecca", "Minâ — 1. beyitte Necid'de Dariyye korusunda bir yer; Mekke'deki Minâ değil"),
 "lb-taabbada": VB("تَأَبَّدَ", "ء ب د", "to go wild, to be left to the wild beasts (Form V; of a deserted place)", "yabanileşmek, vahşi hayvanlara kalmak (tefa''ul; terk edilmiş yer için)", "V"),
 "lb-ghawl": P("الْغَوْل", "al-Ghawl — a mountain in Labīd's country", "Gavl — Lebîd'in yurdunda bir dağ"),
 "lb-rijam": P("الرِّجَام", "al-Rijām — a mountain in Labīd's country", "Ricâm — Lebîd'in yurdunda bir dağ"),
 "lb-madfa": N("مَدْفَع", "د ف ع", "a channel down which water runs off high ground, a torrent-bed (pl. مَدَافِع)", "yüksek yerden suyun akıp gittiği yer, sel yatağı (ç. مَدَافِع)", "مَدَافِع"),
 "lb-rayyan": P("الرَّيَّان", "al-Rayyān — a mountain in the land of the Banū ʿĀmir", "Reyyân — Benî Âmir yurdunda bir dağ"),
 "lb-khalaq": N("خَلَق", "خ ل ق", "worn, threadbare, old (said of one and of many alike)", "eskimiş, yıpranmış (tekil ve çoğul için aynı)"),
 "lb-wahy": N("وَحْي", "و ح ي", "writing, an inscription (pl. وُحِيّ)", "yazı, kitâbe (ç. وُحِيّ)", "وُحِيّ"),
 "lb-silam": N("سِلَام", "س ل م", "stones (sg. سَلِمَة)", "taşlar (tekili سَلِمَة)"),
 "lb-tajarrama": VB("تَجَرَّمَ", "ج ر م", "to be completed and run out (Form V; of a year or a span of time)", "tamamlanıp sona ermek (tefa''ul; yıl ve süre için)", "V"),
 "lb-mirba": N("مِرْبَاع", "ر ب ع", "a spring rain-star; مَرَابِيعُ النُّجُومِ: the star-settings of spring that bring rain", "bahar yağmur yıldızı; مَرَابِيعُ النُّجُومِ: yağmur getiren bahar nev'leri", "مَرَابِيع"),
 "lb-saba": VB("صَابَ", "ص و ب", "to fall on, to reach, to hit (صَابَ يَصُوبُ) — the same as أَصَابَ", "üzerine düşmek, isabet etmek (صَابَ يَصُوبُ) — أَصَابَ ile aynı"),
 "lb-wadq": N("وَدْق", "و د ق", "rain", "yağmur"),
 "lb-raida": N("رَاعِدَة", "ر ع د", "a thunder-cloud (pl. رَوَاعِد)", "gök gürültülü bulut (ç. رَوَاعِد)", "رَوَاعِد"),
 "lb-jawd": N("جَوْد", "ج و د", "a full, wide-spread rain, a downpour", "bol ve her yeri tutan yağmur, sağanak"),
 "lb-rihma": N("رِهْمَة", "ر ه م", "a soft, gentle shower (pl. رِهَام، رِهَم)", "yumuşak, ince yağmur (ç. رِهَام، رِهَم)", "رِهَام"),
 "lb-sariya": N("سَارِيَة", "س ر ي", "a cloud that comes and rains by night (pl. سَوَارٍ)", "geceleyin gelip yağan bulut (ç. سَوَارٍ)", "سَوَارٍ"),
 "lb-ghadin": N("غَادٍ", "غ د و", "coming in the early morning; a morning cloud (الْغَادِي)", "sabah erken gelen; sabah bulutu (الْغَادِي)"),
 "lb-mudjin": N("مُدْجِن", "د ج ن", "(a cloud) that wraps the whole sky in darkness (ism fa'il of أَدْجَنَ)", "göğün her yanını karanlığa bürüyen (bulut) (أَدْجَنَ'den ism-i fâil)"),
 "lb-mutajawib": N("مُتَجَاوِب", "ج و ب", "answering one another (ism fa'il of تَجَاوَبَ)", "birbirine cevap veren (تَجَاوَبَ'den ism-i fâil)"),
 "lb-irzam": N("إِرْزَام", "ر ز م", "a rumbling, a groaning sound (masdar of أَرْزَمَ: of a she-camel, of thunder)", "gürleme, böğürme sesi (أَرْزَمَ'nin masdarı: deve ve gök gürültüsü için)"),
 "lb-ayhaqan": N("أَيْهَقَان", "ء ه ق", "wild rocket (a desert plant)", "yabani tere (bir çöl bitkisi)"),
 "lb-atfala": VB("أَطْفَلَ", "ط ف ل", "to have young, to become a mother of young (Form IV; of a female animal)", "yavru sahibi olmak, yavrulamak (if'âl; dişi hayvan için)", "IV"),
 "lb-jalha": N("جَلْهَة", "ج ل ه", "the side of a valley; الْجَلْهَتَانِ: its two sides", "vadinin yakası; الْجَلْهَتَانِ: iki yakası"),
 "lb-naam": N("نَعَام", "ن ع م", "ostriches (collective; one: نَعَامَة)", "devekuşları (cins ismi; teki: نَعَامَة)"),
 "lb-ayna": N("عَيْنَاء", "ع ي ن", "wide-eyed (fem.; pl. عِين) — الْعِين: the wild cows", "iri gözlü (müennes; ç. عِين) — الْعِين: yaban sığırları", "عِين"),
 "lb-aidh": N("عَائِذ", "ع و ذ", "(a female) that has newly given birth (pl. عُوذ)", "yeni doğurmuş (dişi) (ç. عُوذ)", "عُوذ"),
 "lb-taajjala": VB("تَأَجَّلَ", "ء ج ل", "to gather into herds (Form V; from إِجْل, a herd of wild cows)", "sürü sürü toplanmak (tefa''ul; إِجْل «yaban sığırı sürüsü»nden)", "V"),
 "lb-baham": N("بَهْم", "ب ه م", "the young of sheep, lambs (pl. بِهَام); here the calves of the wild cows", "koyun yavruları, kuzular (ç. بِهَام); burada yaban sığırlarının yavruları", "بِهَام"),

 # ---- vv. 8–15 ----
 "lb-zabur": N("زَبُور", "ز ب ر", "a book, a written scroll (pl. زُبُر): a فَعُول in the sense of «written»", "kitap, yazılı sahife (ç. زُبُر): «yazılmış» anlamında feûl", "زُبُر"),
 "lb-ajadda": VB("أَجَدَّ", "ج د د", "to make new, to renew (Form IV, doubled) — the same as جَدَّدَ", "yenilemek (if'âl, muzaaf) — جَدَّدَ ile aynı", "IV"),
 "lb-raj": N("رَجْع", "ر ج ع", "going over a thing again, renewing it (masdar of رَجَعَ in its transitive sense)", "bir şeyin üzerinden tekrar geçmek, yenilemek (müteaddî رَجَعَ'nin masdarı)"),
 "lb-washima": N("وَاشِمَة", "و ش م", "a woman who tattoos (ism fa'il, fem., of وَشَمَ)", "dövme yapan kadın (وَشَمَ'den müennes ism-i fâil)"),
 "lb-asaffa": VB("أَسَفَّ", "س ف ف", "to sprinkle (a powder) into a thing — kohl into the eye, pigment into a tattoo (Form IV, doubled)", "(toz hâlindeki şeyi) serpmek — göze sürme, dövmeye boya (if'âl, muzaaf)", "IV"),
 "lb-nauur": N("نَؤُور", "ن و ر", "lampblack — the pigment of soot rubbed into a tattoo; some say indigo", "is boyası — dövmeye sürülen kurum boyası; çivit de denmiştir"),
 "lb-kiffa": N("كِفَّة", "ك ف ف", "a ring, anything round (pl. كِفَف)", "halka, yuvarlak olan her şey (ç. كِفَف)", "كِفَف"),
 "lb-bana": VB("بَانَ", "ب ي ن", "to be plain, to come clear (بَانَ يَبِينُ)", "açığa çıkmak, belirmek (بَانَ يَبِينُ)"),
 "lb-ariya": VB("عَرِيَ", "ع ر ي", "to be bare, to be stripped of (عَرِيَ يَعْرَى; with عَنْ / مِنْ)", "çıplak kalmak, bir şeyden soyulup boşalmak (عَرِيَ يَعْرَى)"),
 "lb-abkara": VB("أَبْكَرَ", "ب ك ر", "to set out early in the morning (Form IV) — the same as بَكَرَ and بَكَّرَ", "sabah erkenden yola çıkmak (if'âl) — بَكَرَ ve بَكَّرَ ile aynı", "IV"),
 "lb-ghadara": VB("غَادَرَ", "غ د ر", "to leave behind (Form III)", "geride bırakmak, terk etmek (müfâale)", "III"),
 "lb-thumam": N("ثُمَام", "ث م م", "panic-grass — a soft plant used to stop the gaps of tents", "sümâm otu — çadır aralıklarını tıkamakta kullanılan yumuşak bir bitki"),
 "lb-shaqa": VB("شَاقَ", "ش و ق", "to stir longing in (شَاقَ يَشُوقُ)", "özlem uyandırmak, iştiyaka düşürmek (شَاقَ يَشُوقُ)"),
 "lb-zun": N("ظُعْن", "ظ ع ن", "litter-camels, camels that carry women in their litters (a lightened ظُعُن, pl. of ظَعُون); or the women themselves (pl. of ظَعِينَة)", "hevdeçli develer (ظُعُن'un hafifletilmişi, ظَعُون'un cem'i); yahut hevdeçlerdeki kadınlar (ظَعِينَة'nin cem'i)"),
 "lb-takannasa": VB("تَكَنَّسَ", "ك ن س", "to go into the covert (كِنَاس) and hide there (Form V; of gazelles) — in v. 12 said of women entering their litters", "inine (كِنَاس) girip gizlenmek (tefa''ul; ceylan için) — 12. beyitte hevdeçlere giren kadınlar için", "V"),
 "lb-qatin": N("قَطِين", "ق ط ن", "a company of people dwelling together (pl. قُطُن)", "bir arada oturan topluluk (ç. قُطُن)", "قُطُن"),
 "lb-sarra": VB("صَرَّ", "ص ر ر", "to creak, to grate (صَرَّ يَصِرُّ صَرِيرًا)", "gıcırdamak (صَرَّ يَصِرُّ صَرِيرًا)"),
 "lb-khayma": N("خَيْمَة", "خ ي م", "a tent, a booth of branches (pl. خِيَام، خِيَم)", "çadır, dallardan çardak (ç. خِيَام، خِيَم)", "خِيَام"),
 "lb-mahfuf": N("مَحْفُوف", "ح ف ف", "surrounded, hung about (with cloths) (ism maf'ul of حَفَّ)", "çevrilmiş, (kumaşlarla) sarılmış (حَفَّ'den ism-i mef'ûl)"),
 "lb-azalla": VB("أَظَلَّ", "ظ ل ل", "to shade, to cast its shadow over (Form IV, doubled)", "gölgelemek, üzerine gölge salmak (if'âl, muzaaf)", "IV"),
 "lb-zawj": N("زَوْج", "ز و ج", "in v. 13: a spread of cloth laid over a litter (pl. أَزْوَاج)", "13. beyitte: hevdecin üzerine atılan kumaş örtü (ç. أَزْوَاج)", "أَزْوَاج"),
 "lb-qiram": N("قِرَام", "ق ر م", "a curtain, a coloured woollen hanging (pl. قُرُم)", "perde, renkli yün örtü (ç. قُرُم)", "قُرُم"),
 "lb-zujla": N("زُجْلَة", "ز ج ل", "a company, a group (pl. زُجَل)", "topluluk, bölük (ç. زُجَل)", "زُجَل"),
 "lb-hafaza": VB("حَفَزَ", "ح ف ز", "to drive forward, to urge on (حَفَزَ يَحْفِزُ)", "itmek, sürmek, hızlandırmak (حَفَزَ يَحْفِزُ)"),
 "lb-zayala": VB("زَايَلَ", "ز ي ل", "to part from, to leave (Form III)", "ayrılmak, terk etmek (müfâale)", "III"),
 "lb-sarab": N("سَرَاب", "س ر ب", "the mirage", "serap"),
 "lb-jiz": N("جِزْع", "ج ز ع", "the bend of a valley (pl. أَجْزَاع)", "vadinin kıvrımı (ç. أَجْزَاع)", "أَجْزَاع"),
 "lb-bisha": P("بِيشَة", "Bīsha — a valley on the road to Yemen; a diptote", "Bîşe — Yemen yolu üzerinde bir vadi; gayr-i munsarif"),
 "lb-athl": N("أَثْل", "ء ث ل", "the athl-tree, a large tamarisk", "esl ağacı, iri bir ılgın türü"),
 "lb-ridam": N("رِضَام", "ر ض م", "great rocks piled one on another (one: رَضْمَة)", "üst üste yığılmış iri kayalar (teki: رَضْمَة)"),

 # ---- vv. 16–21 ----
 "lb-nawar": P("نَوَار", "Nawār — the woman of Labīd's nasīb; a diptote", "Nevâr — Lebîd'in nesîbindeki kadın; gayr-i munsarif"),
 "lb-murri": N("مُرِّيّ", "م ر ر", "of the tribe of Murra (nisba; fem. مُرِّيَّة)", "Mürre kabilesine mensup (nisbet; müennesi مُرِّيَّة)"),
 "lb-fayd": P("فَيْد", "Fayd — a town in Najd on the Iraq pilgrim road; a diptote here", "Feyd — Necid'de, Irak hac yolu üzerinde bir belde; burada gayr-i munsarif"),
 "lb-hijaz": P("الْحِجَاز", "the Ḥijāz", "Hicaz"),
 "lb-maram": N("مَرَام", "ر و م", "seeking, what one seeks; the place where a thing is sought", "arama, istenen şey; bir şeyin arandığı yer"),
 "lb-muhajjar": P("مُحَجَّر", "Muḥajjar — a mountain near Fayd", "Muhaccer — Feyd yakınında bir dağ"),
 "lb-farda": P("فَرْدَة", "Farda — a mountain standing alone, near Fayd", "Ferde — Feyd yakınında tek başına duran bir dağ"),
 "lb-rukham": P("رُخَام", "Rukhām — a tract of land adjoining Farda", "Ruhâm — Ferde'ye bitişik bir arazi"),
 "lb-sawaiq": P("صُوَائِق", "Ṣuwāʾiq — a place towards Yemen", "Suvâik — Yemen tarafında bir yer"),
 "lb-aymana": VB("أَيْمَنَ", "ي م ن", "to go to Yemen, to head towards Yemen (Form IV)", "Yemen'e gitmek, Yemen yönüne yönelmek (if'âl)", "IV"),
 "lb-wihaf": P("وِحَاف", "Wiḥāf — in وِحَافُ الْقَهْرِ, a place within Ṣuwāʾiq", "Vihâf — وِحَافُ الْقَهْرِ terkibinde; Suvâik içinde bir yer"),
 "lb-qahr": P("الْقَهْر", "al-Qahr — a mountain; وِحَافُ الْقَهْرِ is named after it", "Kahr — bir dağ; وِحَافُ الْقَهْرِ ona nisbetle adlandırılır"),
 "lb-tilkham": P("طِلْخَام", "Ṭilkhām — a place within Ṣuwāʾiq", "Tılhâm — Suvâik içinde bir yer"),
 "lb-lubana": N("لُبَانَة", "ل ب ن", "a need, a desire one still has of someone (pl. لُبَانَات)", "ihtiyaç, birinden beklenen dilek (ç. لُبَانَات)", "لُبَانَات"),
 "lb-khulla": N("خُلَّة", "خ ل ل", "close friendship, love at its utmost; a close friend (of one and of many)", "yakın dostluk, son derecede sevgi; yakın dost (tekil ve çoğul için)"),
 "lb-sarram": N("صَرَّام", "ص ر م", "one who is quick to cut off, who breaks ties again and again (an intensive فَعَّال)", "çokça kesen, bağları çabucak koparan (mübalağa sîgası فَعَّال)"),
 "lb-haba": VB("حَبَا", "ح ب و", "to bestow on, to give freely (حَبَا يَحْبُو; with بِ of the gift)", "bağışlamak, cömertçe vermek (حَبَا يَحْبُو; verilen şey بِ ile)"),
 "lb-mujamil": N("مُجَامِل", "ج م ل", "one who deals courteously and fairly with another (ism fa'il of جَامَلَ)", "başkasına nazik ve güzel muamele eden (جَامَلَ'den ism-i fâil)"),
 "lb-zalaa": VB("ظَلَعَ", "ظ ل ع", "to limp, to go lame (ظَلَعَ يَظْلَعُ; of a beast)", "aksamak, topallamak (ظَلَعَ يَظْلَعُ; hayvan için)"),
}
HOLLOW_N = "أَجْوَفُ: تُحْذَفُ عَيْنُهُ عِنْدَ السُّكُونِ — "
def F5(v, masdar, fail, note=None):
    """a sound Form V verb"""
    return _sg.derived(_sg.B5, _sg.W5, "َ", v, v, v, masdar, fail, note=note) if note else _sg.derived(_sg.B5, _sg.W5, "َ", v, v, v, masdar, fail)
def F4D(a, b, masdar, fail, note, maful=None, pmz=None, pmd=None):
    """a doubled Form IV verb: أَجَدَّ يُجِدُّ"""
    return _sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, masdar, fail, _sg.mazi14("أَ" + a + "َ" + b + "ّ", "أَ" + a + "ْ" + b + "َ" + b), _sg.mudari14("ُ", a + "ِ" + b + "ّ", a + "ْ" + b + "ِ" + b),
        ["أَ" + a + "ِ" + b + "َّ", "أَ" + a + "ِ" + b + "َّا", "أَ" + a + "ِ" + b + "ُّوا", "أَ" + a + "ِ" + b + "ِّي", "أَ" + a + "ِ" + b + "َّا", "أَ" + a + "ْ" + b + "ِ" + b + "ْنَ"],
        "يُ" + a + "ِ" + b + "َّ", "يُ" + a + "ِ" + b + "َّ", "تُ" + a + "ِ" + b + "َّ", maful=maful, pmz=pmz, pmd=pmd, note=note)
NEW_VERBS = {
 "lb-taabbada": F5("تَأَبَّد", "تَأَبُّد", "مُتَأَبِّد"),
 "lb-tajarrama": F5("تَجَرَّم", "تَجَرُّم", "مُتَجَرِّم"),
 "lb-taajjala": F5("تَأَجَّل", "تَأَجُّل", "مُتَأَجِّل"),
 "lb-atfala": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْفَل", "طْفِل", "أَطْفِل", "إِطْفَال", "مُطْفِل", note="أَطْفَلَتِ الْأُنْثَى: صَارَتْ ذَاتَ طِفْلٍ — لَازِمٌ."),
 "lb-saba": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "صَاب", "صُب", "صُوب", "صُب", "صُوب", "صُب", "صَوْب", "صَائِب", "مَصُوب", "صِيبَ", "يُصَابُ", HOLLOW_N + "يَصُوبُ ← لَمْ يَصُبْ."),

 "lb-ajadda": F4D("ج", "د", "إِجْدَاد", "مُجِدّ", "مُضَاعَفٌ: يُجِدُّ — لَمْ يُجِدَّ."),
 "lb-asaffa": F4D("س", "ف", "إِسْفَاف", "مُسِفّ", "مُضَاعَفٌ: يُسِفُّ — لَمْ يُسِفَّ؛ وَالْمَجْهُولُ أُسِفَّ.", maful="مُسَفّ", pmz="أُسِفَّ", pmd="يُسَفُّ"),
 "lb-azalla": F4D("ظ", "ل", "إِظْلَال", "مُظِلّ", "مُضَاعَفٌ: يُظِلُّ — لَمْ يُظِلَّ."),
 "lb-bana": _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "بَان", "بِن", "بِين", "بِن", "بِين", "بِن", "بَيَان", "بَائِن", note=HOLLOW_N + "يَبِينُ ← لَمْ يَبِنْ — لَازِمٌ."),
 "lb-shaqa": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "شَاق", "شُق", "شُوق", "شُق", "شُوق", "شُق", "شَوْق", "شَائِق", "مَشُوق", "شِيقَ", "يُشَاقُ", HOLLOW_N + "يَشُوقُ ← لَمْ يَشُقْ."),
 "lb-ariya": _sg.naqis1("samia", "نَاقِصٌ يَائِيٌّ", "y", "عَرِ", "عْر", "a", "اِعْر", "عُرْي", "عَارٍ (الْعَارِي)", note="نَاقِصٌ: عَرِيَ يَعْرَى — لَمْ يَعْرَ، بِحَذْفِ الْأَلِفِ."),
 "lb-abkara": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْكَر", "بْكِر", "أَبْكِر", "إِبْكَار", "مُبْكِر"),
 "lb-ghadara": _sg.derived(_sg.B3, _sg.W3, "ُ", "غَادَر", "غَادِر", "غَادِر", "مُغَادَرَة", "مُغَادِر", "مُغَادَر", "غُودِرَ", "يُغَادَرُ"),
 "lb-zayala": _sg.derived(_sg.B3, _sg.W3, "ُ", "زَايَل", "زَايِل", "زَايِل", "مُزَايَلَة", "مُزَايِل", "مُزَايَل", "زُويِلَ", "يُزَايَلُ"),
 "lb-takannasa": F5("تَكَنَّس", "تَكَنُّس", "مُتَكَنِّس"),
 "lb-hafaza": _sg1("daraba", "حَفَز", "حْفِز", "اِحْفِز", "حَفْز", "حَافِز", "مَحْفُوز", "حُفِزَ", "يُحْفَزُ"),
 "lb-sarra": _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "صَرِير", "صَارّ", _sg.mazi14("صَرّ", "صَرَر"), _sg.mudari14("َ", "صِرّ", "صْرِر"),
     ["صِرَّ", "صِرَّا", "صِرُّوا", "صِرِّي", "صِرَّا", "اِصْرِرْنَ"], "يَصِرَّ", "يَصِرَّ", "تَصِرَّ", note="مُضَاعَفٌ لَازِمٌ: الْجَزْمُ بِالْفَتْحِ (لَمْ يَصِرَّ)، وَيَجُوزُ الْفَكُّ: لَمْ يَصْرِرْ."),

 "lb-aymana": dict(_sg.entry(_sg.B4 + " — مِثَالٌ يَائِيٌّ", _sg.W4, "إِيمَان", "مُومِن", _sg.mazi14("أَيْمَن"), _sg.mudari14("ُ", "ومِن"),
     ["أَيْمِنْ", "أَيْمِنَا", "أَيْمِنُوا", "أَيْمِنِي", "أَيْمِنَا", "أَيْمِنَّ"], "يُومِنَ", "يُومِنْ", "تُومِنْ",
     note="مِثَالٌ يَائِيٌّ: تُقْلَبُ يَاؤُهُ وَاوًا بَعْدَ الضَّمَّةِ فِي الْمُضَارِعِ وَاسْمِ الْفَاعِلِ — أَيْمَنَ يُومِنُ فَهُوَ مُومِنٌ: أَتَى الْيَمَنَ."), samai=True),
 "lb-haba": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "حَبَ", "حْب", "u", "اُحْب", "حِبَاء", "حَابٍ", "مَحْبُوّ", "حُبِيَ", "يُحْبَى"),
 "lb-zalaa": _sg1("fataha", "ظَلَع", "ظْلَع", "اِظْلَع", "ظَلْع", "ظَالِع", note="ظَلَعَ الْبَعِيرُ يَظْلَعُ ظَلْعًا: غَمَزَ فِي مَشْيِهِ — لَازِمٌ."),
}
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

# ---- the manifest ------------------------------------------------------------------------------------------------------
_AD = lambda n: str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
TITLES = TITLES_ALL[:len(CHAPS)]
WHOLE = DONE_TO == POEM_END
# DIV: (verse, ar, en, tr) — a departure from the edition's print, with its witness.  FLAGS: (verse, ar, en, tr) — an editorial vowel
# that neither the metre nor the commentary settles.
DIV = [
 (8, "الْبَيْتُ ٨ «الطَّلولِ» ← «الطُّلُولِ» بِضَمِّ الطَّاءِ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ (الطُّلُولُ: جَمْعُ الطَّلَلِ) وَنَصُّ الدُّرَّةِ", "v. 8 «الطَّلولِ» → «الطُّلُولِ», with damma on the ṭāʾ — witness: al-Zawzanī's own gloss (the plural of طَلَل) and al-Durra's text", "8. beyit «الطَّلولِ» → «الطُّلُولِ», tâ'nın dammesiyle — şahit: Zevzenî'nin kendi açıklaması (طَلَل'in cem'i) ve Dürre'nin metni"),
 (16, "الْبَيْتُ ١٦ «تَذَكَّرَ» ← «تَذَكَّرُ» مُضَارِعًا مَرْفُوعًا (أَصْلُهُ تَتَذَكَّرُ)، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ (أَيَّ شَيْءٍ تَتَذَكَّرِينَ) وَإِعْرَابُ الدُّرَّةِ", "v. 16 «تَذَكَّرَ» → «تَذَكَّرُ», a present verb in raf' (for تَتَذَكَّرُ) — witness: al-Zawzanī's own paraphrase («what do you remember») and al-Durra's iʿrāb", "16. beyit «تَذَكَّرَ» → «تَذَكَّرُ», merfû muzâri (aslı تَتَذَكَّرُ) — şahit: Zevzenî'nin kendi açıklaması («neyi hatırlıyorsun») ve Dürre'nin i'râbı"),
 (9, "الْبَيْتُ ٩ «نَئُورُها» ← «نَؤُورُهَا» (كُرْسِيُّ الْهَمْزَةِ فَقَطْ)، وَالشَّاهِدُ نَصُّ الدُّرَّةِ", "v. 9 «نَئُورُها» → «نَؤُورُهَا» (the seat of the hamza only) — witness: al-Durra's text", "9. beyit «نَئُورُها» → «نَؤُورُهَا» (yalnız hemzenin kürsüsü) — şahit: Dürre'nin metni"),
]
FLAGS = [
 (0, "هَمْزَةُ «وَأَنَّهُ مَاتَ» فِي الْخَبَرِ (مَفْتُوحَةٌ فِي الْمَطْبُوعِ بَعْدَ «إِنَّ» الْمَكْسُورَةِ)", "the hamza of «وَأَنَّهُ مَاتَ» in the khabar (printed with fatha after a إِنَّ with kasra)", "haberdeki «وَأَنَّهُ مَاتَ» hemzesi (matbûda, kesreli «inne»den sonra fethalıdır)"),
 (19, "مِيمُ «فَمَظِنَّةٌ» وَظَاؤُهَا (ب ١٩: فِي الْمَطْبُوعِ «فَمِظَنّةٌ» بِكَسْرِ الْمِيمِ، وَكُتِبَتْ هُنَا عَلَى الْمَشْهُورِ فِي اللُّغَةِ بِفَتْحِ الْمِيمِ وَكَسْرِ الظَّاءِ، وَلَا شَاهِدَ مَضْبُوطًا عَلَيْهِ فِي الشَّرْحَيْنِ)", "the mīm and ẓāʾ of «فَمَظِنَّةٌ» (v. 19: the edition prints «فَمِظَنّةٌ», with kasra on the mīm; the usual dictionary form is written here, and neither commentary vowels the word)", "«فَمَظِنَّةٌ» kelimesinin mîm ve zâ'sı (19. beyit: matbûda mîmin kesresiyle «فَمِظَنّةٌ»; burada lügatte meşhur olan şekil yazıldı; iki şerhte de kelime harekeli değildir)"),
 (18, "تَنْوِينُ «فَرْدَةٌ» (ب ١٨) وَ«فَصُوَائِقٌ» (ب ١٩): هُوَ فِي الْمَطْبُوعِ وَبِهِ يَسْتَقِيمُ الْوَزْنُ، وَعَدُّهُ صَرْفًا لِلضَّرُورَةِ مِنَ الْمُحَرِّرِ", "the tanwin of «فَرْدَةٌ» (v. 18) and «فَصُوَائِقٌ» (v. 19): it is the edition's and the metre needs it; calling it a poet's licence is the editor's own remark", "«فَرْدَةٌ» (18. beyit) ve «فَصُوَائِقٌ» (19. beyit) tenvini: matbûdadır ve vezin onu gerektirir; bunu şiir zarûreti saymak editörün kendi notudur"),
 (6, "هَاءُ «الْأَيْهَقَانِ» (ب ٦: بِالْفَتْحِ وَالضَّمِّ عِنْدَ الزَّوْزَنِيِّ، وَاخْتِيرَ الْفَتْحُ)", "the ha of «الْأَيْهَقَانِ» (v. 6: al-Zawzanī allows fatha and damma; fatha is written)", "«الْأَيْهَقَانِ» kelimesinin hâ'sı (6. beyit: Zevzenî'ye göre fetha ve damme caizdir; fetha yazıldı)"),
]
_div = sorted(d for d in DIV if d[0] <= DONE_TO); _flg = sorted(f for f in FLAGS if f[0] <= DONE_TO)
_ch_ar = "؛ ".join("الْفَصْلُ %s: %s–%s" % (_AD(i + 2), _AD(a), _AD(b)) for i, (a, b) in enumerate(VNUMS))
_ch_en = "; ".join("chapter %d: vv. %d–%d" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_ch_tr = "; ".join("%d. bölüm: %d–%d. beyitler" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_sofar_ar = "وَهِيَ هُنَا كَامِلَةٌ: ثَمَانِيَةٌ وَثَمَانُونَ بَيْتًا لَمْ يُتْرَكْ مِنْهَا بَيْتٌ وَلَمْ يُقَدَّمْ وَلَمْ يُؤَخَّرْ" if WHOLE else "وَالْمَنْشُورُ مِنْهَا هُنَا الْأَبْيَاتُ ١–%s مُتَّصِلَةً لَمْ يُتْرَكْ مِنْ وَسَطِهَا بَيْتٌ، وَتَتِمَّةُ الْقَصِيدَةِ (الْأَبْيَاتُ %s–٨٨) لَمْ تُنْشَرْ بَعْدُ" % (_AD(DONE_TO), _AD(DONE_TO + 1))
_sofar_en = "given here WHOLE — eighty-eight verses, none left out and none moved" if WHOLE else "of which this package gives vv. 1–%d as one unbroken run, with no verse skipped inside it; the rest of the ode (vv. %d–88) is not yet published here" % (DONE_TO, DONE_TO + 1)
_sofar_tr = "burada TAMAMI verilmiştir: seksen sekiz beyit; hiçbiri atlanmamış, yeri değiştirilmemiştir" if WHOLE else "bu pakette 1–%d. beyitler, aradan hiçbir beyit atlanmadan, kesintisiz verilmiştir; kasidenin devamı (%d–88. beyitler) henüz yayımlanmamıştır" % (DONE_TO, DONE_TO + 1)
_d_ar = ("وَخُولِفَ شَكْلُ الْمَطْبُوعِ أَوْ رَسْمُهُ فِي هٰذِهِ الْمَوَاضِعِ بِشَاهِدٍ: " + "؛ ".join("(%s) " % _AD(i + 1) + d[1] for i, d in enumerate(_div)) + ". ") if _div else "وَلَمْ يُخَالَفْ رَسْمُ الْمَطْبُوعِ فِي شَيْءٍ مِنَ الْأَبْيَاتِ الْمَنْشُورَةِ. "
_d_en = ("The edition's print is departed from in these places, each against a witness: " + "; ".join("(%d) " % (i + 1) + d[2] for i, d in enumerate(_div)) + ". ") if _div else "The edition's consonantal text is nowhere departed from in the verses given. "
_d_tr = ("Matbû metinden şu yerlerde, her biri bir şahide dayanılarak ayrılınmıştır: " + "; ".join("(%d) " % (i + 1) + d[3] for i, d in enumerate(_div)) + ". ") if _div else "Verilen beyitlerde matbûun harf iskeletinden hiçbir yerde ayrılınmamıştır. "
ATTR_AR = ("نَصٌّ مَنْقُولٌ بِلَفْظِهِ. الْفَصْلُ الْأَوَّلُ مِنْ خَبَرِ لَبِيدِ بْنِ رَبِيعَةَ فِي «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةِ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ٢٣٧٨٥)، ج ١ ص ٢٦٧، الْفِقْرَةُ ٤٦٩ كَامِلَةً: قِطْعَةٌ مُتَّصِلَةٌ وَاحِدَةٌ لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ؛ وَتُرِكَ رَقْمُ الْفِقْرَةِ وَالْقَوْسَانِ حَوْلَ «بَعْدَ ذٰلِكَ». وَالْفُصُولُ بَعْدَهُ مُعَلَّقَتُهُ — وَهِيَ مِنَ الْبَحْرِ الْكَامِلِ، وَرَوِيُّهَا مِيمٌ مَضْمُومَةٌ بَعْدَهَا هَاءُ الْوَصْلِ وَأَلِفُ الْخُرُوجِ — بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) وَتَرْتِيبِهِ وَعَدِّهِ فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةِ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م (الْكِتَابُ ١١٢٥٣)، ص ١٧١–٢٠٢، ثَمَانِيَةٌ وَثَمَانُونَ بَيْتًا؛ " + _sofar_ar + ". " + _ch_ar + ". وَالْبَيْتُ جُمْلَةٌ وَاحِدَةٌ، وَعَلَامَةُ «•» آخِرُ صَدْرِهِ. الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ عَلَى حَالِهِ بِإِمْلَاءِ هٰذَا الرَّفِّ، وَمَا تَرَكَتْهُ عَارِيًا — وَهُوَ حَرَكَاتُ خَبَرِ ابْنِ قُتَيْبَةَ كُلُّهَا سِوَى الشَّدَّاتِ، وَبَعْضُ حُرُوفِ الْأَبْيَاتِ وَأَوَاخِرُ كَثِيرٍ مِنْ كَلِمَاتِهَا — ضَبَطَهُ الْمُحَرِّرُ بِمَا يُوجِبُهُ الْوَزْنُ وَالشَّرْحُ. " + _d_ar
           + ("وَمِمَّا ضَبَطَهُ الْمُحَرِّرُ وَلَمْ يَقْطَعْ بِهِ وَزْنٌ وَلَا شَرْحٌ: " + "؛ ".join(f[1] for f in _flg) + ". " if _flg else "")
           + "إِعْرَابُ كُلِّ كَلِمَةٍ بِعِبَارَةِ هٰذَا الرَّفِّ، وَقَدْ رُوجِعَ عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ: إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهَ الدُّرَّة (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م؛ الْكِتَابُ ١٥١٠١٧، ج ٢ ص ٧–١٢٣) — وَهُوَ يَرْوِي الْقَصِيدَةَ تِسْعَةً وَثَمَانِينَ بَيْتًا — وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ: مَا سَمَّاهُ أَوْ وَصَفَهُ الزَّوْزَنِيُّ أَوِ الدُّرَّةُ نُسِبَ إِلَيْهِ، وَمَا كَانَ بِحَدِّ التَّلْخِيصِ وَحْدَهُ قِيلَ فِيهِ: «عَلَى حَدِّ التَّلْخِيصِ». وَالتَّرْجَمَةُ مَعْنَى الْبَيْتِ عَلَى شَرْحِ الزَّوْزَنِيِّ، لَا شِعْرٌ. وَتَقْسِيمُ الْفُصُولِ وَعَنَاوِينُهَا وَعَلَامَاتُ التَّرْقِيمِ مِنَ الْمُحَرِّرِ، وَالنَّصُّ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.")
ATTR_EN = ("The RECEIVED text, word for word. Chapter 1 is from the khabar of Labīd ibn Rabīʿa in Ibn Qutayba (d. 276 AH), al-Shiʿr wa-l-shuʿarāʾ, in the edition al-Maktaba al-Shāmila names «Dār al-Ḥadīth, Cairo, 1423 AH» (book 23785), vol. 1 p. 267, the whole of § 469: one contiguous span with nothing cut from inside it; only the paragraph number and the brackets round «بَعْدَ ذٰلِكَ» are left out. The chapters after it are his Muʿallaqa — in the metre al-kāmil, rhyming on a mīm with damma followed by the hāʾ of the waṣl and its alif — in the recension, order and verse-count of al-Zawzanī (d. 486 AH), Sharḥ al-Muʿallaqāt al-sabʿ, the edition Shamela names «Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423 AH / 2002 CE» (book 11253), pp. 171–202, eighty-eight verses, " + _sofar_en + ": " + _ch_en + ". Each verse is one sentence, and «•» marks the end of its first hemistich. The vowelling has two layers. What the edition vowels is kept, in this shelf's spelling; what it leaves bare — every short vowel of Ibn Qutayba's khabar (the edition prints only its shaddas), some letters of the verses and many of their word-endings — is supplied editorially, as the metre and the commentary require. " + _d_en
           + ("Editorial vowels that neither the metre nor the commentary settles: " + "; ".join(f[2] for f in _flg) + ". " if _flg else "")
           + "The iʿrāb of every word is in this shelf's own wording and was checked against Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409 AH / 1989 CE; book 151017, vol. 2 pp. 7–123) — he counts eighty-nine verses — and where he gives two readings the first is given and the second mentioned. The figures of balāgha are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ: one that al-Zawzanī or al-Durra names or describes is credited to him, and one that rests on the Talkhīṣ's definition alone says «by the Talkhīṣ's definition». The translation gives each verse's plain meaning after al-Zawzanī; it is not poetry. The division into chapters, their titles and the punctuation are editorial, and the text awaits scholarly review.")
ATTR_TR = ("Metin LAFZIYLA aktarılmıştır. 1. bölüm, Lebîd b. Rebîa'nın haberindendir: İbn Kuteybe (ö. 276 h.), eş-Şi'r ve'ş-şuarâ, el-Mektebetü'ş-Şâmile'nin «Dâru'l-Hadîs, Kahire, 1423 h.» diye andığı baskı (kitap 23785), c. 1 s. 267, 469. paragrafın tamamı: ortasından hiçbir şey çıkarılmamış tek ve kesintisiz bir parça; yalnız paragraf numarası ile «بَعْدَ ذٰلِكَ» çevresindeki parantez bırakılmıştır. Sonraki bölümler onun muallakasıdır — kâmil bahrinden, revîsi dammeli mîm, ardından vasl hâ'sı ve hurûc elifi — Zevzenî'nin (ö. 486 h.) rivayeti, sıralaması ve beyit sayımıyla: Şerhu'l-Muallakâti's-seb', Şâmile'nin «Dâru İhyâi't-Türâsi'l-Arabî, 1423 h. / 2002 m.» diye andığı baskı (kitap 11253), s. 171–202, seksen sekiz beyit; " + _sofar_tr + ": " + _ch_tr + ". Her beyit tek cümledir; «•» işareti ilk mısraın sonudur. Harekeleme iki katmandır: baskının harekelediği, bu rafın imlâsıyla aynen korunmuştur; çıplak bıraktığı — İbn Kuteybe haberinin şeddeler dışındaki bütün harekeleri, beyitlerin bazı harfleri ve birçok kelime sonu — vezin ve şerhin gerektirdiği şekilde editörce konmuştur. " + _d_tr
           + ("Editörün koyduğu, vezin ve şerhin kesinleştirmediği harekeler: " + "; ".join(f[3] for f in _flg) + ". " if _flg else "")
           + "Her kelimenin i'râbı bu rafın kendi ifadesiyledir ve Muhammed Ali Tâhâ ed-Dürre'nin Fethu'l-Kebîri'l-Müteâl: İ'râbü'l-Muallakâti'l-aşri't-tıvâl'i (Mektebetü's-Sevâdî, Cidde, 2. baskı, 1409 h. / 1989 m.; kitap 151017, c. 2 s. 7–123) ile karşılaştırılmıştır — o, kasideyi seksen dokuz beyit olarak rivayet eder; iki vecih zikrettiği yerde birincisi verilmiş, ikincisine işaret edilmiştir. Belâgat vecihleri Kazvînî'nin Telhîsu'l-Miftâh'ındaki bâblarla adlandırılmıştır: Zevzenî'nin yahut Dürre'nin adını koyduğu veya tarif ettiği vecih ona nisbet edilmiş, yalnız Telhîs'in tarifine dayanan vecih için «Telhîs'in tarifine göre» denmiştir. Tercüme, beytin Zevzenî şerhine göre düz mânasıdır; şiir değildir. Bölümleme, başlıklar ve noktalama editöre aittir; metin ilmî incelemeyi beklemektedir.")
MANIFEST = {
 "id": SLUG, "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ لَبِيدِ بْنِ رَبِيعَةَ", "en": "The Muʿallaqa of Labīd ibn Rabīʿa", "tr": "Lebîd b. Rebîa'nın Muallakası"},
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
