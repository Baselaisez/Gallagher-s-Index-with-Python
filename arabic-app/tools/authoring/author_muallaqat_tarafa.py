"""Author content/samples/muallaqat-tarafa — «مُعَلَّقَةُ طَرَفَةَ بْنِ الْعَبْدِ», a RECEIVED text at Level 6 (Master).

Chapter 1 is the poet's khabar, VERBATIM from Ibn Qutayba, «الشعر والشعراء» (Dār al-Ḥadīth, Cairo 1423, 1/182, §§ 295–296;
shamela.ws/book/23785/175). The other chapters are the WHOLE Muʿallaqa — 103 verses — in al-Zawzanī's text, order and
count («شرح المعلقات السبع», printed pp. 89–120, shamela.ws/book/11253/99–130), cut by PLAN (below). A verse is ONE
sentence; the last token of its first hemistich carries punctAfter "•". The iʿrāb of every token was checked against
Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب المعلقات العشر الطوال» (1/163–321, shamela.ws/book/151017/162–318)
and is written in the shelf's own wording; al-Tibrīzī's vowelled «شرح القصائد العشر» (shamela.ws/book/37488/54–99) is the
second witness for the verse text. The balāgha is named on the token that carries it, after the syntax, in the categories
of al-Qazwīnī's Talkhīṣ, each figure on one of two bases: a commentator names or describes it, or it meets the Talkhīṣ's
own definition («عَلَى حَدِّ التَّلْخِيصِ»). The verbatim sources live in research/sources/muallaqat-tarafa-src.txt,
-durra.txt and -tibrizi.txt.

The Shamela e-text of al-Zawzanī repeats printed p. 98 in the place of p. 97, so his vv. 21–22 (and his commentary on
vv. 20–22) are missing there: the two verses are given from al-Tibrīzī's vowelled text and al-Durra, in the place
al-Zawzanī's numbering fixes for them (20 → 23), and the attribution says so.

Resumable: a verse is filed by its NUMBER in VERSE; only the chapters whose verses are all written are published (PLAN /
DONE). Verses are inserted above the line «# ==== VERSES ABOVE ====», lexicon entries above «# ==== GLOSS ABOVE ====»,
paradigms above «# ==== NEW VERBS ABOVE ====».

Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_tarafa.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-tarafa"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import tok, seg      # the shared token builder (NFC-normalises every Arabic string)
import sarf_gen as _sg

N = lambda s: unicodedata.normalize("NFC", s)
def T(full, lex, pos, g, ar, en, tr, p=None, s=None):
    """one token: surface, key, part of speech, grammar anchors, the trilingual iʿrāb, the mark after it, the clitic chain"""
    return tok(full, lex, pos, g, ar, en, tr, punct=p, segments=[seg(*x) for x in s] if s else None)

HEMI = "•"
_PK = {"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp", "كَ": "pron-2ms", "نِي": "pron-1s",
       "ي": "pron-1s", "يَ": "pron-1s", "نَا": "pron-1p", "كِ": "pron-2fs", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هُنَّ": "pron-3fp", "هِنَّ": "pron-3fp", "كُمْ": "pron-2mp"}
def P(form): return (form, _PK[form], "pron")
_PRN = {"هُ": ("الْهَاءُ", "the هُ", "«hû»"), "هِ": ("الْهَاءُ", "the هِ", "«hî»"), "هَا": ("هَا", "هَا", "هَا"), "ي": ("الْيَاءُ", "the ya", "yâ"), "يَ": ("الْيَاءُ", "the ya", "yâ"),
        "نِي": ("الْيَاءُ", "the ya", "yâ"), "كَ": ("الْكَافُ", "the kaf", "kâf"), "كِ": ("الْكَافُ", "the kaf", "kâf"), "هُمَا": ("هُمَا", "هُمَا", "هُمَا"), "هِمَا": ("هِمَا", "هِمَا", "هِمَا"),
        "نَا": ("نَا", "نَا", "نَا"), "هُمْ": ("هُمْ", "هُمْ", "هُمْ"), "هِمْ": ("هِمْ", "هِمْ", "هِمْ"), "هُمُ": ("هُمْ", "هُمْ", "هُمْ"), "هُنَّ": ("هُنَّ", "هُنَّ", "هُنَّ"), "هِنَّ": ("هِنَّ", "هِنَّ", "هِنَّ"), "كُمْ": ("كُمْ", "كُمْ", "كُمْ")}

# =====================================================================================================================
# The line builders. A line is an (ar, en, tr) triple; L carries the grammar anchors its wording implies.
# =====================================================================================================================
class L(tuple):
    tags = ()
    sent = False     # a note that is a sentence of its own (a figure): it follows a full stop, not a semicolon
    def __add__(self, o):
        r = L(a + b for a, b in zip(self, o)); r.tags = tuple(self.tags) + tuple(getattr(o, "tags", ()))
        return r
def mk(ar, en, tr, *tags):
    r = L((ar, en, tr)); r.tags = tags
    return r
def cap(s): return s[:1].upper() + s[1:]
def low(s, tr=False):
    if tr and s[:1] in "İI": return {"İ": "i", "I": "ı"}[s[0]] + s[1:]
    return s[:1].lower() + s[1:]

_C = {"raf": ("مَرْفُوعٌ", "in raf'", "merfû"), "nasb": ("مَنْصُوبٌ", "in nasb", "mansûb"), "jarr": ("مَجْرُورٌ", "in jarr", "mecrûr")}
_V = {"raf": ("الضَّمَّةِ", "damma", "damme", "ضَمَّةٍ"), "nasb": ("الْفَتْحَةِ", "fatha", "fetha", "فَتْحَةٍ"), "jarr": ("الْكَسْرَةِ", "kasra", "kesre", "كَسْرَةٍ")}
YA_MUQ = "مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ"
def SIGN(case, sign=""):
    c, v = _C[case], _V[case]
    if sign == "": return mk(c[0] + " بِ" + v[0], c[1] + " by the " + v[1], v[2] + " ile " + c[2])
    if sign == "alif": return mk(c[0] + " بِالْأَلِفِ لِأَنَّهُ مُثَنًّى", c[1] + " by the alif, being a dual", "tesniye olduğu için elif ile " + c[2], "al-muthanna")
    if sign == "ya2": return mk(c[0] + " بِالْيَاءِ لِأَنَّهُ مُثَنًّى", c[1] + " by the ya, being a dual", "tesniye olduğu için yâ ile " + c[2], "al-muthanna")
    if sign == "waw": return mk(c[0] + " بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", c[1] + " by the waw, being a sound masculine plural", "cem-i müzekker sâlim olduğu için vâv ile " + c[2], "jam-mudhakkar-salim")
    if sign == "yaj": return mk(c[0] + " بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", c[1] + " by the ya, being a sound masculine plural", "cem-i müzekker sâlim olduğu için yâ ile " + c[2], "jam-mudhakkar-salim")
    if sign == "mulhaq": return mk(c[0] + (" بِالْوَاوِ" if case == "raf" else " بِالْيَاءِ") + " لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", c[1] + " by the " + ("waw" if case == "raf" else "ya") + ", being joined to the sound masculine plural", "cem-i müzekker sâlime mülhak olduğu için " + ("vâv" if case == "raf" else "yâ") + " ile " + c[2], "jam-mudhakkar-salim")
    if sign == "fatha": return mk("مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", "in jarr by the fatha in place of the kasra, being a diptote", "gayr-i munsarif olduğu için kesre yerine fetha ile mecrûr", "mamnu-min-sarf")
    if sign == "kasra": return mk("مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ", "in nasb by the kasra in place of the fatha, being a sound feminine plural", "cem-i müennes sâlim olduğu için fetha yerine kesre ile mansûb", "jam-muannath-salim")
    if sign == "maq": return mk(c[0] + " بِ" + v[3] + " مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", c[1] + " by a " + v[1] + " estimated on the alif", "elif üzerinde takdîrî " + v[2] + " ile " + c[2], "ism-maqsur-manqus")
    if sign == "maqh": return mk(c[0] + " بِ" + v[3] + " مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", c[1] + " by a " + v[1] + " estimated on the alif that falls before the tanwin", "tenvin sebebiyle düşen elif üzerinde takdîrî " + v[2] + " ile " + c[2], "ism-maqsur-manqus")
    if sign == "man": return mk(c[0] + " بِ" + v[3] + " مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", c[1] + " by a " + v[1] + " estimated on the ya", "yâ üzerinde takdîrî " + v[2] + " ile " + c[2], "ism-maqsur-manqus")
    if sign == "manh": return mk(c[0] + " بِ" + v[3] + " مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", c[1] + " by a " + v[1] + " estimated on the ya that falls before the tanwin", "tenvin sebebiyle düşen yâ üzerinde takdîrî " + v[2] + " ile " + c[2], "ism-maqsur-manqus")
    if sign == "yam": return mk(c[0] + " بِ" + v[3] + " مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ, c[1] + " by a " + v[1] + " estimated before the speaker's ya, whose kasra holds the place", "mütekellim yâsından önceki harf üzerinde takdîrî " + v[2] + " ile " + c[2], "ya-al-mutakallim")
    if sign == "five":
        h = {"raf": ("الْوَاوِ", "waw", "vâv"), "nasb": ("الْأَلِفِ", "alif", "elif"), "jarr": ("الْيَاءِ", "ya", "yâ")}[case]
        return mk(c[0] + " بِ" + h[0] + " لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", c[1] + " by the " + h[1] + ", being one of the five nouns", "esmâ-i hamseden olduğu için " + h[2] + " ile " + c[2], "five-nouns")
    raise KeyError(sign)
_INNA = ("إِنَّ", "أَنَّ", "كَأَنَّ", "لَيْتَ", "لٰكِنَّ", "لَعَلَّ")
_R = {"fail": ("فَاعِلٌ", "The doer", "Fâil", "raf", "fail"), "naib": ("نَائِبُ فَاعِلٍ", "The deputy doer", "Nâib-i fâil", "raf", "naib-al-fail"),
      "mub": ("مُبْتَدَأٌ", "The mubtada", "Mübteda", "raf", "mubtada-khabar"), "mubm": ("مُبْتَدَأٌ مُؤَخَّرٌ", "The mubtada, placed last", "Sona bırakılmış mübteda", "raf", "mubtada-khabar"),
      "kh": ("خَبَرٌ", "The predicate", "Haber", "raf", "mubtada-khabar"), "khm": ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ", "The predicate of an omitted mubtada", "Mahzûf mübtedanın haberi", "raf", "mubtada-khabar"),
      "kh2": ("خَبَرٌ ثَانٍ", "A second predicate", "İkinci haber", "raf", "mubtada-khabar"),
      "maf": ("مَفْعُولٌ بِهِ", "The direct object", "Mef'ûlün bih", "nasb", "maful-bihi"), "maf1": ("مَفْعُولٌ بِهِ أَوَّلُ", "The first object", "Birinci mef'ûl", "nasb", "mafulayn"),
      "maf2": ("مَفْعُولٌ بِهِ ثَانٍ", "The second object", "İkinci mef'ûl", "nasb", "mafulayn"), "hal": ("حَالٌ", "A hal", "Hâl", "nasb", "hal"),
      "tam": ("تَمْيِيزٌ", "A tamyiz (specifier)", "Temyîz", "nasb", "tamyiz"), "mi": ("مُضَافٌ إِلَيْهِ", "The second term of the idafa", "Muzâfun ileyh", "jarr", "idafa-definiteness"),
      "maj": ("", "", "", "jarr", "huruf-jarr"), "zz": ("ظَرْفُ زَمَانٍ", "An adverb of time", "Zaman zarfı", "nasb", "maful-fih"), "zm": ("ظَرْفُ مَكَانٍ", "An adverb of place", "Mekân zarfı", "nasb", "maful-fih"),
      "mm": ("مَفْعُولٌ مُطْلَقٌ", "An absolute object", "Mef'ûlün mutlak", "nasb", "maful-mutlaq"), "ml": ("مَفْعُولٌ لِأَجْلِهِ", "An object of cause", "Mef'ûlün lieclih", "nasb", "maful-lah"),
      "mun": ("مُنَادًى مُضَافٌ", "A vocative, annexed", "Muzâf münâdâ", "nasb", "vocative-munada"), "mst": ("مُسْتَثْنًى", "The thing excepted", "Müstesnâ", "nasb", "istithna")}
def R(role, sign="", case=None):
    """role [+ sign]: «فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ». role may be «ism:كَأَنَّ» / «kh:لَيْسَ» for the noun and predicate of a nāsikh."""
    if role.startswith(("ism:", "kh:")):
        k, w = role.split(":"); inna = w in _INNA
        case = case or (("nasb" if inna else "raf") if k == "ism" else ("raf" if inna else "nasb"))
        nm = ("اسْمُ " + w, "The noun of " + w, w + "'nin ismi") if k == "ism" else ("خَبَرُ " + w, "The predicate of " + w, w + "'nin haberi")
        s = SIGN(case, sign)
        r = mk(nm[0] + " " + s[0], nm[1] + ", " + s[1], nm[2] + ", " + s[2], "inna-wa-akhawatuha" if inna else "kana-wa-akhawatuha", *s.tags)
        return r
    a, e, t, c, tag = _R[role]; s = SIGN(case or c, sign)
    if role == "maj": return mk(s[0], cap(s[1]), cap(s[2]), tag, *s.tags)
    return mk(a + " " + s[0], e + ", " + s[1], t + ", " + s[2], tag, *s.tags)
def NA(of, case, sign="", nth=""):
    """نَعْتٌ لِـ«…»"""
    s = SIGN(case, sign); n = {"": ("نَعْتٌ", "An adjective", "na'tı"), "2": ("نَعْتٌ ثَانٍ", "A second adjective", "ikinci na'tı"), "3": ("نَعْتٌ ثَالِثٌ", "A third adjective", "üçüncü na'tı"), "4": ("نَعْتٌ رَابِعٌ", "A fourth adjective", "dördüncü na'tı")}[nth]
    return mk(n[0] + " لِـ«" + of + "» " + s[0], n[1] + " of «" + of + "», " + s[1], "«" + of + "» kelimesinin " + n[2] + ", " + s[2], "naat-sifa", *s.tags)
def AT(on, case, sign=""):
    s = SIGN(case, sign)
    return mk("مَعْطُوفٌ عَلَى «" + on + "» " + s[0], "Conjoined to «" + on + "», " + s[1], "«" + on + "» kelimesine ma'tûf, " + s[2], "atf-nasaq", *s.tags)
def BD(of, case, sign=""):
    s = SIGN(case, sign)
    return mk("بَدَلٌ مِنْ «" + of + "» " + s[0], "A badal of «" + of + "», " + s[1], "«" + of + "» kelimesinden bedel, " + s[2], "badal", *s.tags)
MUD = mk("، مُضَافٌ", ", annexed", ", muzâf", "idafa-definiteness")
def IDF(pr):
    a, e, t = _PRN[pr]
    return mk("، مُضَافٌ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" % a, ", annexed; %s is its second term" % e, ", muzâf; %s muzâfun ileyh" % t, "idafa-definiteness")
QAFIYA = mk("، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ", "; its tanwin is dropped for the rhyme", "; tenvini kafiye için düşmüştür", "al-qafiya")
KASR_Q = mk("، وَحُرِّكَ بِالْكَسْرِ لِلرَّوِيِّ (حَرَكَةُ الْقَافِيَةِ الْمُطْلَقَةِ)", ", which gives way to the kasra of the rhyme (the qāfiya is unbound)", ", yerini revî harekesi olan kesreye bırakmıştır (kâfiye mutlaktır)", "al-qafiya")
def ON(x): return ("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«%s»" % x, "the phrase hangs on «%s»" % x, "câr-mecrûrun müteallakı «%s»" % x)
def ZON(x): return ("مُتَعَلِّقٌ بِـ«%s»" % x, "it hangs on «%s»" % x, "müteallakı «%s»" % x)
_H = {"hal": ("حَالٍ مِنْ", "hal of", "kelimesinden mahzûf hâle"), "naat": ("نَعْتٍ لِـ", "adjective of", "kelimesinin mahzûf na'tına"), "naat2": ("نَعْتٍ ثَانٍ لِـ", "second adjective of", "kelimesinin mahzûf ikinci na'tına"),
      "kh": ("خَبَرٍ لِـ", "predicate of", "kelimesinin mahzûf haberine"), "khm": ("خَبَرٍ مُقَدَّمٍ لِـ", "predicate, set first, of", "kelimesinin öne geçmiş mahzûf haberine")}
def ONH(kind, x, zarf=False):
    """the phrase (or the adverb) hangs on an OMITTED hal / naʿt / khabar of «x»"""
    h = _H[kind]
    lead = ("مُتَعَلِّقٌ", "it hangs", "") if zarf else ("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ", "the phrase hangs", "câr-mecrûr ")
    q = "«%s»" % x
    return (lead[0] + " بِمَحْذُوفٍ " + h[0] + (" " if not h[0].endswith("ـ") else "") + q, lead[1] + " on an omitted " + h[1] + " " + q, lead[2] + q + " " + h[2] + " müteallik")
def HID(pron, ref=None, naib=False):
    """the hidden doer; ref = an (ar-genitive, en, tr-dative) triple, or a quoted Arabic word"""
    f = ("نَائِبُ الْفَاعِلِ", "its deputy doer", "nâib-i fâili") if naib else ("الْفَاعِلُ", "its doer", "fâili")
    if ref:
        if isinstance(ref, str): ref = ("«" + ref + "»", "«" + ref + "»", "«" + ref + "» kelimesine")
        return ("، وَ%s مُسْتَتِرٌ تَقْدِيرُهُ: %s يَعُودُ عَلَى %s" % (f[0], pron, ref[0]), "; %s is a hidden pronoun returning to %s" % (f[1], ref[1]), "; %s %s dönen gizli zamir" % (f[2], ref[2]))
    w = N(pron) in (N("أَنَا"), N("نَحْنُ"), N("أَنْتَ"))
    en = {N("أَنَا"): "I", N("نَحْنُ"): "we", N("أَنْتَ"): "you", N("هُوَ"): "he", N("هِيَ"): "she", N("أَنْتِ"): "you (fem.)"}[N(pron)]
    return ("، وَ%s مُسْتَتِرٌ %sتَقْدِيرُهُ: %s" % (f[0], "وُجُوبًا " if w else "", pron), "; %s is the hidden «%s»" % (f[1], en), "; %s %sgizli «%s»" % (f[2], "vücûben " if w else "", pron))
_JM = {"ist": ("وَالْجُمْلَةُ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause opens a new sentence and has no seat", "cümle istînâfiyyedir, i'râbdan mahalli yoktur"),
       "ibt": ("وَالْجُمْلَةُ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause opens the speech and has no seat", "cümle ibtidâiyyedir, i'râbdan mahalli yoktur"),
       "sila": ("وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause is the relative's ṣila and has no seat", "cümle sıladır, i'râbdan mahalli yoktur"),
       "maqul": ("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "the clause is what is said, in the seat of nasb", "cümle mekūlü'l-kavl olarak mahallen mansûb"),
       "jz": ("وَالْجُمْلَةُ جَوَابُ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause answers the condition and has no seat", "cümle şartın cevabıdır, i'râbdan mahalli yoktur"),
       "jzm": ("وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "the clause is the answer of the condition, in the seat of jazm", "cümle şartın cevabı olarak mahallen meczûm"),
       "itr": ("وَالْجُمْلَةُ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause is parenthetical and has no seat", "cümle mu'tarızadır, i'râbdan mahalli yoktur"),
       "qasam": ("وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause answers the oath and has no seat", "cümle kasemin cevabıdır, i'râbdan mahalli yoktur")}
_CS = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}
def JM(kind, x=None, case="jarr"):
    """the seat of the clause this word heads"""
    if kind in _JM: return _JM[kind]
    q = "«%s»" % x; c = _CS[case]
    if kind == "sifa": return ("وَالْجُمْلَةُ فِي مَحَلِّ %s نَعْتٌ لِـ%s" % (c[0], q), "the clause qualifies %s, in the seat of %s" % (q, c[1]), "cümle %s kelimesinin na'tı olarak mahallen %s" % (q, c[2]))
    if kind == "hal": return ("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ %s" % q, "the clause is a hal of %s, in the seat of nasb" % q, "cümle %s kelimesinden hâl olarak mahallen mansûb" % q)
    if kind == "kh": return ("وَالْجُمْلَةُ فِي مَحَلِّ %s خَبَرُ %s" % (_CS["raf" if case == "jarr" else case][0], q), "the clause is the predicate of %s, in the seat of %s" % (q, _CS["raf" if case == "jarr" else case][1]), "cümle %s kelimesinin haberi olarak mahallen %s" % (q, _CS["raf" if case == "jarr" else case][2]))
    if kind == "jawab": return ("وَالْجُمْلَةُ جَوَابُ %s لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ" % q, "the clause answers %s and has no seat" % q, "cümle %s kelimesinin cevabıdır, i'râbdan mahalli yoktur" % q)
    if kind == "mudaf": return ("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ %s إِلَيْهَا" % q, "the clause is in the seat of jarr, %s being annexed to it" % q, "cümle, %s kelimesinin muzâfun ileyhi olarak mahallen mecrûr" % q)
    if kind == "atf": return ("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ %s" % q, "the clause is conjoined to the clause of %s" % q, "cümle %s cümlesine ma'tûf" % q)
    if kind == "maf": return ("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ%s" % q, "the clause is the second object of %s, in the seat of nasb" % q, "cümle %s fiilinin ikinci mef'ûlü olarak mahallen mansûb" % q)
    raise KeyError(kind)
HADD = ("عَلَى حَدِّ التَّلْخِيصِ", "by the Talkhīṣ's definition", "Telhîs'in tarifine göre")
def HD(ar, en, tr):
    """a figure no commentator names, that meets the Talkhīṣ's own definition"""
    r = L(("وَفِيهِ — " + HADD[0] + " — " + ar, "B" + HADD[1][1:] + ", " + en, HADD[2] + " " + tr)); r.sent = True
    return r
_TK = {"mm": ("مُرْسَلٌ مُجْمَلٌ", "mursal mujmal", "Teşbih-i mürsel mücmel"), "mf": ("مُرْسَلٌ مُفَصَّلٌ", "mursal mufaṣṣal", "Teşbih-i mürsel mufassal"),
       "bl": ("بَلِيغٌ", "balīgh", "Teşbih-i belîğ"), "tm": ("تَمْثِيلِيٌّ مُرْسَلٌ", "tamthīlī (mursal)", "Teşbih-i temsîlî (mürsel)"), "mk": ("مُؤَكَّدٌ مُفَصَّلٌ", "muʾakkad mufaṣṣal", "Teşbih-i müekked mufassal")}
_AD = {"ka": ("الْكَافُ", "the kaf", "kâf"), "kaanna": ("كَأَنَّ", "كَأَنَّ", "كَأَنَّ"), "mithl": ("«مِثْلُ»", "«مِثْلُ»", "«مِثْلُ»"), "kama": ("الْكَافُ فِي «كَمَا»", "the kaf of «كَمَا»", "«كَمَا»daki kâf"), "kaannama": ("كَأَنَّمَا", "كَأَنَّمَا", "كَأَنَّمَا")}
def TSB(kind, m, mb, adat=None, wajh=None, src="z"):
    """a tashbīh with its pillars. m / mb / wajh are (ar, en, tr); src: z = al-Zawzanī says «شَبَّهَ», d = al-Durra, t = al-Tibrīzī, h = by the definition"""
    k = _TK[kind]; s = {"z": ("الزَّوْزَنِيُّ", "al-Zawzanī", "Zevzenî"), "d": ("الدُّرَّةُ", "al-Durra", "Dürre"), "t": ("التِّبْرِيزِيُّ", "al-Tibrīzī", "Tebrîzî"), "h": None}[src]
    ar = "تَشْبِيهٌ " + k[0] + ": الْمُشَبَّهُ " + m[0] + "، وَالْمُشَبَّهُ بِهِ " + mb[0]
    en = "a tashbih " + k[1] + ": the thing likened is " + m[1] + ", the thing it is likened to is " + mb[1]
    tr = k[2] + ": müşebbeh " + m[2] + ", müşebbehün bih " + mb[2]
    if adat:
        ar += "، وَالْأَدَاةُ " + _AD[adat][0]; en += ", the particle is " + _AD[adat][1]; tr += ", edat " + _AD[adat][2]
    else:
        ar += "، وَالْأَدَاةُ مَحْذُوفَةٌ"; en += ", the particle is left out"; tr += ", edat mahzûf"
    if wajh:
        ar += "، وَوَجْهُ الشَّبَهِ " + wajh[0]; en += ", and the point of likeness is " + wajh[1]; tr += ", vech-i şebeh " + wajh[2]
    elif kind in ("mm", "tm"):
        ar += "، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ"; en += ", and the point of likeness is left unsaid"; tr += ", vech-i şebeh mahzûf"
    if s:
        r = L(("وَفِيهِ " + ar + " (" + s[0] + ")", "There is " + en + " (" + s[1] + ")", tr + " (" + s[2] + ")")); r.sent = True
        return r
    return HD(ar, "there is " + en, low(tr, True) + " vardır")
TSB_TAGS = ["tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"]

_CL = {"wa": ("الْوَاوُ عَاطِفَةٌ، وَ", "The waw conjoins; ", "Vâv atıf; ", ("وَ", "wa", "conj")), "fa": ("الْفَاءُ عَاطِفَةٌ، وَ", "The fa conjoins; ", "Fâ atıf; ", ("فَ", "fa", "conj")),
       "wa-ist": ("الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "The waw opens a new sentence; ", "Vâv istînâfiyye; ", ("وَ", "wa", "conj")), "fa-ist": ("الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ", "The fa opens a new sentence; ", "Fâ istînâfiyye; ", ("فَ", "fa", "conj")),
       "wa-hal": ("الْوَاوُ وَاوُ الْحَالِ، وَ", "The waw is the waw of the hal; ", "Vâv hâliye; ", ("وَ", "wa", "conj")),
       "wa-rubba": ("الْوَاوُ وَاوُ رُبَّ، وَ", "The waw is the waw of رُبَّ («many a …»); ", "Vâv, vâv-ı rubbe'dir («nice …»); ", ("وَ", "wa", "conj")),
       "wa-qasam": ("الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَ", "The waw is the jarr letter of the oath; ", "Vâv kasem ve cer harfi; ", ("وَ", "wa", "conj")),
       "fa-jaza": ("الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَ", "The fa ties the answer to its condition; ", "Fâ cevap râbıtası; ", ("فَ", "fa", "conj")),
       "fa-sabab": ("الْفَاءُ عَاطِفَةٌ تُفِيدُ السَّبَبِيَّةَ، وَ", "The fa conjoins, with the sense of consequence; ", "Fâ sebebiyet bildiren atıf harfi; ", ("فَ", "fa", "conj")),
       "bi": ("الْبَاءُ حَرْفُ جَرٍّ، وَ", "The ba is a jarr letter; ", "Bâ cer harfi; ", ("بِ", "bi", "prep")), "li": ("اللَّامُ حَرْفُ جَرٍّ، وَ", "The lam is a jarr letter; ", "Lâm cer harfi; ", ("لِ", "li", "prep")),
       "ka": ("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ", "The kaf is a jarr letter of likening; ", "Kâf teşbih bildiren cer harfi; ", ("كَ", "ka", "prep")),
       "la": ("اللَّامُ وَاقِعَةٌ فِي جَوَابِ «لَوْ»، وَ", "The lam stands in the answer of لَوْ; ", "Lâm «لَوْ»in cevabında gelen lâmdır; ", ("لَ", "lam-jawab", "part")),
       "la-ibt": ("اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَ", "The lam is the lam of emphasis, slid on to the predicate; ", "Lâm, habere kaydırılmış te'kîd lâmıdır (lâm-ı müzahlaka); ", ("لَ", "la-ibtida", "part")),
       "la-qasam": ("اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَ", "The lam stands in the answer of the oath; ", "Lâm kasemin cevabında gelen lâmdır; ", ("لَ", "lam-jawab", "part")),
       "a": ("الْهَمْزَةُ حَرْفُ اسْتِفْهَامٍ، وَ", "The hamza is the particle of question; ", "Hemze istifham harfi; ", ("أَ", "a-istifham", "part"))}
_CLTAG = {"wa": "atf-nasaq", "fa": "atf-nasaq", "bi": "huruf-jarr", "li": "huruf-jarr", "ka": "huruf-jarr", "wa-hal": "al-hal-jumla-wa-rabituha", "wa-ist": "anwa-al-waw", "wa-rubba": "al-lam-wa-rubba-fil-kafiya", "wa-qasam": "huruf-al-qasam-fil-kafiya", "fa-jaza": "al-fa-fi-jawab-al-shart"}
def _build(full, pre, enc, stem, body, notes, p, lex, pos, tags):
    """prefix clitics + the word's own line + notes; segments when the token is a chain"""
    full = N(full); cl = [c for c in (pre.split("+") if pre else [])]
    rest = full; segs = []; lead = ["", "", ""]
    for c in cl:
        a, e, t, sg_ = _CL[c]; segs.append(sg_)
        lead = [lead[0] + a, lead[1] + e, lead[2] + t]
        if stem is None:
            assert rest.startswith(N(sg_[0])), (full, c)
            rest = rest[len(N(sg_[0])):]
        if c in _CLTAG: tags.append(_CLTAG[c])
    if stem is not None: rest = N(stem) + (N(enc) if enc else "")
    core = rest[:len(rest) - len(N(enc))] if enc else rest
    if cl:
        line = [lead[0] + core + " " + body[0], lead[1] + core + " is " + low(body[1]), lead[2] + core + " " + low(body[2], True)]
    else:
        line = list(body)
    for i, n in enumerate(notes):
        sep = (" — ", " — ", " — ") if i == 0 else ((". ", ". ", ". ") if getattr(n, "sent", False) else ("؛ ", "; ", "; "))
        line = [line[k] + sep[k] + (cap(n[k]) if i == 0 and getattr(n, "sent", False) and k else n[k]) for k in range(3)]
        tags.extend(getattr(n, "tags", ()))
    line = [x if x.rstrip().endswith((".", "؟", "?", "!")) else x + "." for x in line]
    s = None
    if cl or enc:
        s = segs + [(core, lex, pos)] + ([P(enc)] if enc else [])
    seen = []
    for g in tags:
        if g and g not in seen: seen.append(g)
    return T(full, lex, pos, seen, line[0], cap(line[1]), cap(line[2]), p, s)
def NO(full, lex, role, *notes, g=None, p=None, pre=None, enc=None, pos="noun", stem=None, q=False):
    """a noun: role is a code for R() or a ready line; enc = an attached pronoun (annexation); q = the rhyme drops its tanwin"""
    if isinstance(role, str): role = R(role)
    tags = list(g or []) + list(getattr(role, "tags", ()))
    body = L(role)
    if enc: body = body + IDF(enc); tags.append("idafa-definiteness")
    if q: body = body + QAFIYA; tags.append("al-qafiya")
    return _build(full, pre, enc, stem, body, notes, p, lex, pos, tags)
_VK = {"madi": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى الْفَتْحِ", "A past%s verb built on fatha", "Fetha üzere mebnî%s mâzî"),
       "madi-f": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "A past%s verb built on fatha; the ta marks the feminine", "Fetha üzere mebnî%s mâzî; tâ te'nîs için"),
       "madi-fk": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "A past%s verb built on fatha; the ta marks the feminine, and takes a kasra because two quiescents meet", "Fetha üzere mebnî%s mâzî; tâ te'nîs için olup iki sâkin karşılaştığı için kesrelenmiştir"),
       "madi-muq": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A past%s verb built on a fatha estimated on the alif", "Elif üzerinde takdîrî fetha üzere mebnî%s mâzî"),
       "madi-fh": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ", "A past%s verb built on a fatha estimated on the alif that fell before the feminine ta", "Te'nîs tâsından önce düşen elif üzerinde takdîrî fetha üzere mebnî%s mâzî; tâ te'nîs için"),
       "madi-tu": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on sukun because the doer's ta is attached; the ta («I») is %s, in the seat of raf'", "Fâil tâsına bitiştiği için sükûn üzere mebnî%s mâzî; tâ («ben») %s, mahallen merfû"),
       "madi-ta": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on sukun because the doer's ta is attached; the ta («you») is %s, in the seat of raf'", "Fâil tâsına bitiştiği için sükûn üzere mebnî%s mâzî; tâ («sen») %s, mahallen merfû"),
       "madi-na": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on sukun because نَا is attached; نَا («we») is %s, in the seat of raf'", "«نَا»ya bitiştiği için sükûn üzere mebnî%s mâzî; نَا («biz») %s, mahallen merfû"),
       "madi-w": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on damma because the plural waw is attached; the waw is %s, in the seat of raf'", "Cemi vâvına bitiştiği için damme üzere mebnî%s mâzî; vâv %s, mahallen merfû"),
       "madi-2": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on fatha; the alif of the dual is %s, in the seat of raf'", "Fetha üzere mebnî%s mâzî; tesniye elifi %s, mahallen merfû"),
       "madi-2f": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْفَتْحِ لِمُنَاسَبَةِ الْأَلِفِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on fatha; the ta marks the feminine and takes a fatha before the alif; the alif of the dual is %s, in the seat of raf'", "Fetha üzere mebnî%s mâzî; tâ te'nîs için olup eliften dolayı fethalanmıştır; tesniye elifi %s, mahallen merfû"),
       "madi-fn": ("فِعْلٌ مَاضٍ%s مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A past%s verb built on sukun because the feminine nun is attached; the nun is %s, in the seat of raf'", "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî%s mâzî; nûn %s, mahallen merfû"),
       "mud": ("فِعْلٌ مُضَارِعٌ%s مَرْفُوعٌ بِالضَّمَّةِ", "A present%s verb in raf' by the damma", "Damme ile merfû%s muzâri"),
       "mud-w": ("فِعْلٌ مُضَارِعٌ%s مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ", "A present%s verb in raf' by a damma estimated on the waw", "Vâv üzerinde takdîrî damme ile merfû%s muzâri"),
       "mud-y": ("فِعْلٌ مُضَارِعٌ%s مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "A present%s verb in raf' by a damma estimated on the ya", "Yâ üzerinde takdîrî damme ile merfû%s muzâri"),
       "mud-a": ("فِعْلٌ مُضَارِعٌ%s مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A present%s verb in raf' by a damma estimated on the alif", "Elif üzerinde takdîrî damme ile merfû%s muzâri"),
       "mud5": ("فِعْلٌ مُضَارِعٌ%s مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A present%s verb in raf' by keeping its nun — one of the five verbs; the waw is %s, in the seat of raf'", "Ef'âl-i hamseden olduğu için nûnun sübûtuyla merfû%s muzâri; vâv %s, mahallen merfû"),
       "mud-fn": ("فِعْلٌ مُضَارِعٌ%s مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A present%s verb built on sukun because the feminine nun is attached; the nun is %s, in the seat of raf'", "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî%s muzâri; nûn %s, mahallen merfû"),
       "jz": ("فِعْلٌ مُضَارِعٌ%s مَجْزُومٌ %s وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "A present%s verb in jazm %s, its sign the sukun", "%s meczûm%s muzâri, cezm alâmeti sükûn"),
       "jz-ill": ("فِعْلٌ مُضَارِعٌ%s مَجْزُومٌ %s وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ", "A present%s verb in jazm %s, its sign the dropping of the weak letter", "%s meczûm%s muzâri, cezm alâmeti illet harfinin hazfi"),
       "jz5": ("فِعْلٌ مُضَارِعٌ%s مَجْزُومٌ %s وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "A present%s verb in jazm %s, its sign the dropping of the nun — one of the five verbs; the waw is the doer, in the seat of raf'", "%s meczûm%s muzâri, cezm alâmeti nûnun hazfi (ef'âl-i hamse); vâv fâil, mahallen merfû"),
       "ns": ("فِعْلٌ مُضَارِعٌ%s مَنْصُوبٌ %s وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "A present%s verb in nasb %s, its sign the fatha", "%s mansûb%s muzâri, nasb alâmeti fetha"),
       "ns-a": ("فِعْلٌ مُضَارِعٌ%s مَنْصُوبٌ %s وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A present%s verb in nasb %s, its sign a fatha estimated on the alif", "%s mansûb%s muzâri, nasb alâmeti elif üzerinde takdîrî fetha"),
       "amr": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ", "An imperative built on sukun", "Sükûn üzere mebnî emir"),
       "amr-ill": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ", "An imperative built on the dropping of its weak letter", "İllet harfinin hazfi üzere mebnî emir"),
       "amr-nun": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "An imperative built on the dropping of the nun; the ya of the woman addressed is the doer, in the seat of raf'", "Nûnun hazfi üzere mebnî emir; muhâtaba yâsı fâil, mahallen merfû"),
       "amr-w": ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "An imperative built on the dropping of the nun; the waw is the doer, in the seat of raf'", "Nûnun hazfi üzere mebnî emir; vâv fâil, mahallen merfû")}
_BY = {"lam": ("بِلَمْ", "by لَمْ", "لَمْ ile"), "la": ("بِلَا النَّاهِيَةِ", "by the prohibitive لَا", "Nehiy lâsıyla"), "shart": ("لِأَنَّهُ فِعْلُ الشَّرْطِ", "as the condition's verb", "Şart fiili olarak"),
       "jawab": ("لِأَنَّهُ جَوَابُ الشَّرْطِ", "as the answer of the condition", "Şartın cevabı olarak"), "talab": ("لِأَنَّهُ جَوَابُ الطَّلَبِ", "as the answer of the request", "Talebin cevabı olarak"),
       "atf-shart": ("عَطْفًا عَلَى فِعْلِ الشَّرْطِ", "being conjoined to the condition's verb", "Şart fiiline ma'tûf olarak"), "atf-jawab": ("عَطْفًا عَلَى جَوَابِ الشَّرْطِ", "being conjoined to the answer of the condition", "Şartın cevabına ma'tûf olarak"),
       "atf-lam": ("عَطْفًا عَلَى الْمَجْزُومِ بِلَمْ", "being conjoined to the verb in jazm by لَمْ", "لَمْ ile meczûm fiile ma'tûf olarak"),
       "an": ("بِأَنْ", "by أَنْ", "أَنْ ile"), "an-mudmara": ("بِأَنْ مُضْمَرَةً", "by a hidden أَنْ", "Gizli أَنْ ile"), "hatta": ("بِأَنْ مُضْمَرَةً وُجُوبًا بَعْدَ حَتَّى", "by an أَنْ hidden after حَتَّى", "حَتَّى'dan sonra vücûben gizli أَنْ ile"), "atf-ns": ("عَطْفًا عَلَى الْمَنْصُوبِ قَبْلَهُ", "being conjoined to the verb in nasb before it", "Önceki mansûb fiile ma'tûf olarak")}
_OBJ = lambda pr: ("، وَ%s%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" % ("النُّونُ لِلْوِقَايَةِ، وَ" if pr == "نِي" else "", _PRN[pr][0]), "; %s%s is its direct object, in the seat of nasb" % ("the nun guards the verb's ending, and " if pr == "نِي" else "", _PRN[pr][1]), "; %s%s mef'ûlün bih, mahallen mansûb" % ("nûn vikâye içindir, " if pr == "نِي" else "", _PRN[pr][2]))
def VB(full, lex, kind, *notes, who=None, g=None, p=None, pre=None, enc=None, by=None, maj=False, q=False, stem=None):
    """a verb. who: None (the doer is named in the verse or is an attached pronoun), a pronoun («أَنَا») or (pronoun, referent)"""
    m = ((" مَبْنِيٌّ لِلْمَجْهُولِ،" if kind.startswith("madi") else " مَبْنِيٌّ لِلْمَجْهُولِ"), " passive", " meçhul") if maj else ("", "", "")
    k = _VK[kind]; tags = list(g or [])
    f = ("نَائِبُ فَاعِلٍ", "the deputy doer", "nâib-i fâil") if maj else ("فَاعِلٌ", "the doer", "fâil")
    if kind in ("jz", "jz-ill", "jz5", "ns", "ns-a"):
        b = _BY[by] if isinstance(by, str) else by
        body = [k[0] % (m[0], b[0]), k[1] % (m[1], b[1]), k[2] % (b[2], m[2])]
        if by == "lam": tags.append("lam-jazim")
        if by in ("shart", "jawab", "atf-shart", "atf-jawab"): tags.append("al-majzum-wal-shart-wal-jaza")
        if by == "talab": tags.append("jawab-al-talab")
        if by == "la": tags.append("la-nahiya")
    elif kind.startswith("amr"):
        body = list(k); tags.append("imperative-amr")
    elif k[0].count("%s") == 2:
        body = [k[0] % (m[0], f[0]), k[1] % (m[1], f[1]), k[2] % (m[2], f[2])]
    else:
        body = [k[0] % m[0], k[1] % m[1], k[2] % m[2]]
    if kind.startswith("mud"): tags.append("mudari-marfu")
    if kind in ("mud5", "jz5"): tags.append("afal-khamsa")
    if maj: tags.append("al-majhul-fil-kafiya")
    body = L(body)
    if q: body = body + KASR_Q; tags.append("al-qafiya")
    if enc: body = body + _OBJ(enc); tags.append("maful-bihi")
    if who:
        body = body + (HID(who[0], who[1], naib=maj) if isinstance(who, tuple) else HID(who, naib=maj))
    return _build(full, pre, enc, stem, body, notes, p, lex, "verb", tags)
def PT(full, lex, line, *notes, g=None, p=None, pre=None, pos="part", stem=None):
    """a particle (or any word whose line is given whole)"""
    return _build(full, pre, None, stem, L(line), notes, p, lex, pos, list(g or []) + list(getattr(line, "tags", ())))
def HJ(full, lex, *notes, p=None, pre=None):
    return PT(full, lex, mk("حَرْفُ جَرٍّ", "A jarr letter", "Cer harfi", "huruf-jarr"), *notes, p=p, pre=pre, pos="prep")
_PL = {"بِ": ("الْبَاءُ", "The ba", "Bâ"), "لِ": ("اللَّامُ", "The lam", "Lâm"), "لَ": ("اللَّامُ", "The lam", "Lâm"), "كَ": ("الْكَافُ", "The kaf", "Kâf")}
def PJ(full, prep, plex, pron, *notes, ref=None, p=None, pre=None, g=None):
    """a jarr letter with its attached pronoun: بِهَا، لَهُ، عَلَيْهِ، فِيهِمَا"""
    nm = _PL.get(prep, (prep, prep, prep)); pn = _PRN[pron]
    r = ("", "", "")
    if ref:
        if isinstance(ref, str): ref = ("«" + ref + "»", "«" + ref + "»", "«" + ref + "» kelimesine")
        r = (" يَعُودُ عَلَى " + ref[0], ", returning to " + ref[1], ", " + ref[2] + " döner")
    body = mk(nm[0] + " حَرْفُ جَرٍّ، وَ" + pn[0] + " ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ" + r[0], nm[1] + " is a jarr letter; " + pn[1] + " is in the seat of jarr" + r[1], nm[2] + " cer harfi; " + pn[2] + " mahallen mecrûr" + r[2], "huruf-jarr")
    full = N(full); tags = list(g or []) + ["huruf-jarr"]
    cl = pre.split("+") if pre else []; segs = []; lead = ["", "", ""]
    for c in cl:
        a, e, t, sg_ = _CL[c]; segs.append(sg_); lead = [lead[0] + a, lead[1] + e, lead[2] + t]
        if c in _CLTAG: tags.append(_CLTAG[c])
    line = [lead[0] + body[0], lead[1] + (low(body[1]) if cl else body[1]), lead[2] + (low(body[2], True) if cl else body[2])]
    for i, n in enumerate(notes):
        sep = (" — ", " — ", " — ") if i == 0 else ((". ", ". ", ". ") if getattr(n, "sent", False) else ("؛ ", "; ", "; "))
        line = [line[k] + sep[k] + (cap(n[k]) if i == 0 and getattr(n, "sent", False) and k else n[k]) for k in range(3)]
        tags.extend(getattr(n, "tags", ()))
    line = [x + "." for x in line]
    seen = []
    for t_ in tags:
        if t_ not in seen: seen.append(t_)
    return T(full, plex, "prep", seen, line[0], cap(line[1]), cap(line[2]), p, segs + [(prep, plex, "prep"), P(pron)])
def nt(ar, en, tr, *tags):
    """a free note, with the anchors it teaches"""
    return mk(ar, en, tr, *tags)
LAM_J = mk("حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ", "The particle of negation that puts the verb in jazm and turns it to the past", "Nefy, cezm ve kalb harfi", "lam-jazim")
QAD_T = mk("حَرْفُ تَحْقِيقٍ", "A particle of certainty", "Tahkîk harfi", "qad-harf")
LA_NAFY = mk("حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ", "A particle of negation; it governs nothing", "Nefy harfi; amel etmez", "la-nafiya")
KAANNA_T = mk("حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يُفِيدُ التَّشْبِيهَ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ", "A verb-like particle of likening: it puts its noun in nasb and its predicate in raf'", "Teşbih bildiren fiile benzeyen harf; ismini nasb, haberini ref' eder", "inna-wa-akhawatuha")
INNA_T = mk("حَرْفُ تَوْكِيدٍ وَنَصْبٍ", "The particle of emphasis and nasb", "Tekit ve nasb harfi", "inna-wa-akhawatuha")
AW_T = mk("حَرْفُ عَطْفٍ", "A conjunction", "Atıf harfi", "atf-nasaq")
IDHA_SH = mk("ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ شَرْطِهِ", "An adverb for time to come that carries the sense of a condition, built on sukun in the seat of nasb and annexed to its condition clause", "Şart mânâsı taşıyan gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf", "maful-fih", "idha-shartiyya")
IN_SH = mk("حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ", "The conditional particle that puts two verbs in jazm", "İki fiili cezmeden şart harfi", "in-shartiyya", "al-majzum-wal-shart-wal-jaza")
MATA_SH = mk("اسْمُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ", "A conditional noun that puts two verbs in jazm, built on sukun in the seat of nasb as an adverb of time", "İki fiili cezmeden şart ismi; sükûn üzere mebnî, zaman zarfı olarak mahallen mansûb", "al-majzum-wal-shart-wal-jaza", "maful-fih")
LAW_T = mk("حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ، حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ", "A conditional particle that governs no jazm: what follows did not happen, so its answer did not", "Cezmetmeyen şart harfi; şart gerçekleşmediği için cevabın da gerçekleşmediğini bildirir", "huruf-al-shart-fil-kafiya")
MA_MASD = mk("حَرْفٌ مَصْدَرِيٌّ", "A masdar-making particle", "Masdar harfi", "anwa-ma")
MA_ZAID = mk("زَائِدَةٌ لِلتَّوْكِيدِ", "The added مَا, for emphasis", "Tekit için zâid mâ", "anwa-ma", "huruf-al-ziyada-fil-kafiya")
MA_NAFY = mk("حَرْفُ نَفْيٍ", "A particle of negation", "Nefy harfi", "anwa-ma")

S1 = []                      # the khabar's sentences, in order
VERSE = {}                   # the Muʿallaqa: al-Zawzanī's verse number -> its sentence
def V(n, en, tr, tokens):
    if n == 0: S1.append({"id": "s%d" % (len(S1) + 1), "translation": {"en": en, "tr": tr}, "tokens": tokens})
    else:
        assert n not in VERSE, n
        assert sum(1 for t in tokens if t.get("punctAfter") == HEMI) == 1, ("one hemistich mark", n)
        if "punctAfter" not in tokens[-1]: tokens[-1]["punctAfter"] = "."
        VERSE[n] = {"translation": {"en": en, "tr": tr}, "tokens": tokens}

# referents of hidden pronouns: (ar genitive, en, tr dative)
TARAFA = ("طَرَفَةَ", "Ṭarafa", "Tarafe'ye")
NAQA = ("النَّاقَةِ", "the she-camel", "deveye")
SHAIR = ("الشَّاعِرِ", "the poet", "şaire")

# =====================================================================================================================
# Chapter 1 — خَبَرُ طَرَفَةَ (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/182, §§ 295–296 — verbatim, contiguous)
# =====================================================================================================================
IBN = lambda case: NO("بْنِ" if case == "jarr" else "بْنُ", "ibn-bn", mk("نَعْتٌ لِلْعَلَمِ قَبْلَهُ " + SIGN(case)[0] + "، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ", "An adjective of the name before it, " + SIGN(case)[1] + ", annexed — its alif is dropped because it stands between two names", "Önceki özel ismin na'tı, " + SIGN(case)[2] + ", muzâf — iki özel isim arasında geldiği için elifi düşmüştür", "naat-sifa", "idafa-definiteness"))
V(0, "He is Ṭarafa, son of al-ʿAbd, son of Sufyān; and of them all he has the finest long ode.",
  "O, Tarafe b. el-Abd b. Süfyân'dır; şairler içinde uzun kasidesi en güzel olan odur.", [
 PT("هُوَ", "huwa", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as the mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar", "al-mabni-wal-mudmar"), pos="pron"),
 NO("طَرَفَةُ", "tarafa", R("kh"), nt("عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ، وَلَمْ يُنَوَّنْ", "a proper name with the feminine ta, barred from tanwin", "lafzî te'nîsli özel isim, gayr-i munsarif; tenvin almaz", "mamnu-min-sarf"), pos="propn"),
 IBN("raf"),
 NO("الْعَبْدِ", "abd", "mi", nt("«الْعَبْدُ» هُنَا عَلَمٌ عَلَى أَبِي الشَّاعِرِ", "«al-ʿAbd» is here the name of the poet's father", "«el-Abd» burada şairin babasının adıdır")),
 IBN("jarr"),
 NO("سُفْيَانَ", "sufyan", R("mi", "fatha"), nt("لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", "a proper name ending in the added alif and nun", "alemiyet ve zâid elif-nûn sebebiyle"), pos="propn", p="،"),
 PT("وَهُوَ", "huwa", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as the mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), pre="wa", pos="pron"),
 NO("أَجْوَدُهُمْ", "ajwad", R("kh"), nt("اسْمُ تَفْضِيلٍ مِنْ «جَادَ»؛ وَالضَّمِيرُ لِلشُّعَرَاءِ", "the elative of جَادَ «to be excellent»; «them» is the poets", "«جَادَ»den ism-i tafdîl; zamir şairlere döner", "ism-tafdil"), enc="هُمْ"),
 T("طَوِيلَةً", "tawila-ode", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "hadhf-wa-taqdir"],
   "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ، يُبَيِّنُ مَا فُضِّلَ فِيهِ — وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: قَصِيدَةً طَوِيلَةً؛ يُرِيدُ الْمُعَلَّقَةَ.",
   "A tamyiz (specifier), in nasb by the fatha: it says in what he excels — an adjective whose noun is left out, «a long (ode)»; he means the Muʿallaqa.",
   "Temyîz, fetha ile mansûb; hangi yönden üstün olduğunu bildirir — mevsûfu mahzûf bir sıfattır: «uzun (kaside)»; Muallaka'yı kasteder.", "."),
])
V(0, "It is he who says: «Khawla has ruins on the stony flat of Thahmad».",
  "«Havle'nin Sehmed'in taşlık düzlüğünde yurt kalıntıları var» diyen odur.", [
 PT("وَهُوَ", "huwa", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as the mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), pre="wa-ist", pos="pron"),
 NO("الْقَائِلُ", "qail", R("kh"), nt("اسْمُ فَاعِلٍ مِنْ «قَالَ»، وَمَقُولُ الْقَوْلِ بَعْدَهُ فِي مَحَلِّ نَصْبٍ؛ وَفِي تَعْرِيفِ الْخَبَرِ بِاللَّامِ قَصْرُهُ عَلَى الْمُبْتَدَإِ: هُوَ الْقَائِلُ لَا غَيْرُهُ", "the ism fa'il of قَالَ; what he said follows, in the seat of nasb. A predicate made definite by the article is restricted to its mubtada: he, and no other, is the one who said it", "«قَالَ»den ism-i fâil; mekūlü'l-kavl ondan sonra gelir, mahallen mansûb. Haberin lâm ile ma'rife olması onu mübtedaya hasreder: bunu söyleyen odur, başkası değil", "ism-fail", "qasr", "turuq-al-qasr"), p=":"),
 NO("لِخَوْلَةَ", "khawla", R("maj", "fatha"), nt("لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", "a feminine proper name", "alemiyet ve te'nîs sebebiyle"), ONH("khm", "أَطْلَالٌ"), pre="li", pos="propn", g=["taqdim-al-musnad"]),
 NO("أَطْلَالٌ", "talal", R("mubm"), nt("جَمْعُ طَلَلٍ؛ وَسَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ تَقَدُّمُ الْخَبَرِ الظَّرْفِ", "the plural of طَلَل; an indefinite may open the sentence because its predicate, a jarr phrase, is set before it", "«طَلَل»in cem'i; nekreyle başlamayı câr-mecrûr haberin öne geçmesi câiz kılmıştır", "jam-taksir")),
 NO("بِبُرْقَةِ", "burqa", R("maj") + MUD, ONH("naat", "أَطْلَالٌ"), pre="bi"),
 NO("ثَهْمَدِ", "thahmad", R("mi"), nt("صَدْرُ مَطْلَعِ الْمُعَلَّقَةِ، وَكُسِرَ آخِرُهُ بِلَا تَنْوِينٍ لِأَنَّهُ عَرُوضُ بَيْتٍ مُصَرَّعٍ", "the first hemistich of the Muʿallaqa; its last word takes the kasra without tanwin, being the end of the first half of a verse whose two halves rhyme", "Muallaka'nın ilk mısraı; musarra beytin ilk yarısının sonu olduğu için son kelime tenvinsiz kesrelidir"), pos="propn"),
])
V(0, "After it he has fine verse; and of his verse and ʿAbīd's the transmitters hold only a little.",
  "Ondan başka da güzel şiirleri vardır; râvîlerin elinde ise onun ve Abîd'in şiirinden ancak azı bulunur.", [
 PJ("وَلَهُ", "لَ", "li", "هُ", ONH("khm", "شِعْرٌ"), ref=TARAFA, pre="wa-ist", g=["taqdim-al-musnad"]),
 NO("بَعْدَهَا", "bada", R("zz"), nt("مُتَعَلِّقٌ بِمَا تَعَلَّقَ بِهِ الْخَبَرُ؛ وَالضَّمِيرُ لِلْقَصِيدَةِ", "it hangs on what the predicate hangs on; «it» is the ode", "haberin müteallakına bağlıdır; zamir kasideye döner"), enc="هَا"),
 NO("شِعْرٌ", "shir", R("mubm")),
 NO("حَسَنٌ", "hasan-adj", NA("شِعْرٌ", "raf"), nt("صِفَةٌ مُشَبَّهَةٌ", "a sifa mushabbaha", "sıfat-ı müşebbehe", "sifa-mushabbaha"), p="،"),
 PT("وَلَيْسَ", "laysa", mk("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ", "a defective past verb that does not conjugate, built on fatha: it puts its noun in raf' and its predicate in nasb", "fetha üzere mebnî, câmid nâkıs mâzî; ismini ref', haberini nasb eder", "kana-wa-akhawatuha", "qasr", "turuq-al-qasr"), nt("وَالنَّفْيُ بِهَا مَعَ «إِلَّا» طَرِيقُ قَصْرٍ: قَصَرَ مَا عِنْدَ الرُّوَاةِ عَلَى الْقَلِيلِ", "its negation with إِلَّا is a way of restriction: what the transmitters hold is confined to «the little»", "onunla nefy ve «إِلَّا» kasr yoludur: râvîlerin elindeki «az»a hasredilmiştir"), pre="wa", pos="verb"),
 NO("عِنْدَ", "inda", R("zm") + MUD, ONH("khm", "الْقَلِيلُ", zarf=True)),
 NO("الرُّوَاةِ", "rawin", "mi", nt("جَمْعُ رَاوٍ عَلَى فُعَلَةٍ", "the plural of رَاوٍ, on the pattern فُعَلَة", "«رَاوٍ»nin fu'ale vezninde cem'i", "jam-taksir")),
 HJ("مِنْ", "min", nt("لِلتَّبْعِيضِ", "for «some of»", "teb'îz için")),
 NO("شِعْرِهِ", "shir", "maj", ONH("hal", "الْقَلِيلُ"), enc="هِ"),
 NO("وَشِعْرِ", "shir", AT("شِعْرِهِ", "jarr") + MUD, pre="wa"),
 NO("عَبِيدٍ", "abid-poet", "mi", nt("هُوَ عَبِيدُ بْنُ الْأَبْرَصِ الْأَسَدِيُّ", "ʿAbīd ibn al-Abraṣ of Asad", "Esedoğullarından Abîd b. el-Ebras"), pos="propn"),
 PT("إِلَّا", "illa", mk("أَدَاةُ حَصْرٍ مُلْغَاةٌ لِأَنَّ الِاسْتِثْنَاءَ مُفَرَّغٌ", "A particle of restriction with no government, the exception being «emptied»", "İstisnâ müferrağ olduğu için amel etmeyen hasr edatı", "istithna-mufarragh")),
 NO("الْقَلِيلُ", "qalil", R("ism:لَيْسَ"), nt("مُؤَخَّرٌ", "placed last", "sona bırakılmıştır"), p="."),
])
V(0, "He stood high among his people by birth, and was bold in lampooning them and lampooning others.",
  "Kavmi içinde soylu bir yeri vardı; onları da başkalarını da hicvetmekte cüretkârdı.", [
 VB("وَكَانَ", "kana", "madi", nt("نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى طَرَفَةَ", "defective: it puts its noun in raf' and its predicate in nasb; its noun is a hidden pronoun returning to Ṭarafa", "nâkıs fiil: ismini ref', haberini nasb eder; ismi Tarafe'ye dönen gizli zamir", "kana-wa-akhawatuha"), pre="wa-ist", g=["hollow-verbs"]),
 HJ("فِي", "fi"),
 NO("حَسَبٍ", "hasab", "maj", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «كَانَ»؛ الْحَسَبُ: شَرَفُ الْآبَاءِ", "the phrase hangs on the omitted predicate of كَانَ; الحَسَب: the honour of one's forefathers", "câr-mecrûr «كَانَ»nin mahzûf haberine müteallik; الحَسَب: ataların şerefi")),
 HJ("مِنْ", "min"),
 NO("قَوْمِهِ", "qawm", "maj", ONH("naat", "حَسَبٍ"), enc="هِ", p="،"),
 NO("جَرِيئًا", "jari-bold", R("kh:كَانَ"), nt("خَبَرٌ ثَانٍ", "a second predicate", "ikinci haber"), nt("صِفَةٌ مُشَبَّهَةٌ مِنْ «جَرُؤَ»", "a sifa mushabbaha of جَرُؤَ", "«جَرُؤَ»den sıfat-ı müşebbehe", "sifa-mushabbaha")),
 HJ("عَلَى", "ala"),
 NO("هِجَائِهِمْ", "hija", "maj", ON("جَرِيئًا"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", "the masdar annexed to its object", "masdarın mef'ûlüne izâfeti", "masdar"), enc="هِمْ"),
 NO("وَهِجَاءِ", "hija", AT("هِجَائِهِمْ", "jarr") + MUD, pre="wa"),
 NO("غَيْرِهِمْ", "ghayr", "mi", enc="هِمْ", p="."),
])
V(0, "His sister was married to ʿAmr ibn Bishr ibn Marthad — and ʿAbd ʿAmr was the lord of the men of his day —",
  "Kız kardeşi Amr b. Bişr b. Mersed'in nikâhı altındaydı; Abdü Amr ise zamanındaki insanların efendisiydi.", [
 VB("وَكَانَتْ", "kana", "madi-f", nt("نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ", "defective: it puts its noun in raf' and its predicate in nasb", "nâkıs fiil: ismini ref', haberini nasb eder", "kana-wa-akhawatuha"), pre="wa-ist", g=["hollow-verbs"]),
 NO("أُخْتُهُ", "ukht", R("ism:كَانَ"), enc="هُ"),
 NO("عِنْدَ", "inda", R("zm") + MUD, nt("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «كَانَتْ»، أَيْ: زَوْجَةً لَهُ", "it hangs on the omitted predicate of كَانَتْ: she was «with» him, that is, his wife", "«كَانَتْ»in mahzûf haberine müteallik; «yanında» yani nikâhı altında")),
 NO("عَمْرِو", "amr-name", "mi", nt("كَذَا فِي الطَّبْعَةِ، وَالْمُرَادُ عَبْدُ عَمْرِو بْنِ بِشْرٍ كَمَا يَدُلُّ عَلَيْهِ مَا بَعْدَهُ؛ وَالْوَاوُ فِي «عَمْرٍو» زَائِدَةٌ لِلْفَرْقِ بَيْنَهُ وَبَيْنَ «عُمَرَ»", "so the edition; the man meant is ʿAbd ʿAmr ibn Bishr, as the next clause shows. The waw of عَمْرو is not sounded: it is written to tell the name from عُمَر", "baskıda böyledir; kastedilen, sonraki cümlenin gösterdiği gibi Abdü Amr b. Bişr'dir. «عَمْرو»daki vâv okunmaz; «عُمَر»den ayırmak için yazılır"), pos="propn"),
 IBN("jarr"),
 NO("بِشْرِ", "bishr", "mi", nt("وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ", "its tanwin is dropped, being a name described by «son of» annexed to a name", "bir özel isme muzâf «ibn» ile vasıflanan özel isim olduğu için tenvini düşmüştür"), pos="propn"),
 IBN("jarr"),
 NO("مَرْثَدٍ", "marthad", "mi", pos="propn", p="،"),
 VB("وَكَانَ", "kana", "madi", nt("نَاقِصٌ", "defective", "nâkıs fiil", "kana-wa-akhawatuha"), nt("وَالْجُمْلَةُ مُعْتَرِضَةٌ أَوْ حَالِيَّةٌ", "the clause is parenthetical, or a hal", "cümle mu'tarıza ya da hâliyedir"), pre="wa", g=["hollow-verbs"]),
 NO("عَبْدُ", "abd", R("ism:كَانَ") + MUD, nt("«عَبْدُ عَمْرٍو» عَلَمٌ مُرَكَّبٌ تَرْكِيبًا إِضَافِيًّا", "«ʿAbd ʿAmr» is a name made of an annexation", "«Abdü Amr» izâfet terkibi hâlinde bir özel isimdir")),
 NO("عَمْرٍو", "amr-name", "mi", pos="propn"),
 NO("سَيِّدَ", "sayyid", R("kh:كَانَ") + MUD),
 NO("أَهْلِ", "ahl", R("mi") + MUD),
 NO("زَمَانِهِ", "zaman", "mi", enc="هِ", p="،"),
])
V(0, "and Ṭarafa's sister complained to him of something in her husband's conduct; so he said:",
  "Tarafe'nin kız kardeşi kocasının bir hâlinden ona yakındı; bunun üzerine Tarafe şöyle dedi:", [
 VB("فَشَكَتْ", "shaka", "madi-fh", pre="fa", g=["naqis-verbs"]),
 NO("أُخْتُ", "ukht", R("fail") + MUD),
 NO("طَرَفَةَ", "tarafa", R("mi", "fatha"), pos="propn"),
 NO("شَيْئًا", "shay", "maf"),
 HJ("مِنْ", "min"),
 NO("أَمْرِ", "amr", R("maj") + MUD, ONH("naat", "شَيْئًا")),
 NO("زَوْجِهَا", "zawj", "mi", enc="هَا"),
 PJ("إِلَيْهِ", "إِلَيْ", "ila", "هِ", ON("شَكَتْ"), ref=TARAFA, p="،"),
 VB("فَقَالَ", "qala", "madi", nt("وَمَقُولُ الْقَوْلِ الْبَيْتَانِ بَعْدَهُ", "what he said is the two verses that follow", "söylediği söz, ardından gelen iki beyittir"), who=("هُوَ", TARAFA), pre="fa", g=["hollow-verbs"], p=":"),
])
V(0, "«There is no fault in him — save that he has wealth, and that he has a waist which, when he stands, is slender;",
  "«Onda hiçbir kusur yok; yalnız zenginliği var, bir de ayağa kalktığında ince duran bir beli;", [
 PT("وَلَا", "la-nafiya-lil-jins", mk("لَا نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ «إِنَّ»", "لَا that denies the whole kind; it governs as إِنَّ does", "cinsi nefyeden lâ; «إِنَّ» gibi amel eder", "la-nafiya-lil-jins", "takid-al-madh-wal-dhamm"),
    nt("وَالْوَاوُ بِحَسَبِ مَا قَبْلَهَا فِي الْقَصِيدَةِ. وَفِي الْبَيْتِ — عَلَى حَدِّ التَّلْخِيصِ — صُورَةُ تَأْكِيدِ الْمَدْحِ بِمَا يُشْبِهُ الذَّمَّ: اسْتَثْنَى مِنْ صِفَةِ ذَمٍّ مَنْفِيَّةٍ («لَا عَيْبَ فِيهِ») صِفَةَ مَدْحٍ («أَنَّ لَهُ غِنًى»)؛ وَالْكَلَامُ عَلَى الِاسْتِهْزَاءِ بِهِ لِبَدَانَتِهِ، كَمَا قَالَ مُحَقِّقُ الطَّبْعَةِ",
       "the waw follows what came before it in the poem. By the Talkhīṣ's definition the verse has the FORM of «praise made firmer by what looks like blame»: from a fault that is denied («no fault in him») a merit is excepted («that he has wealth»). But the words are said in mockery of him, for he was a fat man — so the editor of this edition notes",
       "vâv, kasidede öncesine göredir. Telhîs'in tarifine göre beyit «zemme benzeyen şeyle medhi te'kîd» SURETİNDEDİR: nefyedilen bir zem sıfatından («onda kusur yok») bir medih sıfatı («zenginliği var») istisna edilmiştir. Ne var ki söz, şişmanlığı sebebiyle onunla alay içindir — baskının muhakkiki böyle not eder"), stem="لَا", pre="wa"),
 NO("عَيْبَ", "ayb", mk("اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ", "The noun of لَا, built on fatha in the seat of nasb", "«لَا»nın ismi; fetha üzere mebnî, mahallen mansûb", "la-nafiya-lil-jins")),
 PJ("فِيهِ", "فِي", "fi", "هِ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «لَا»", "the phrase hangs on the omitted predicate of لَا", "câr-mecrûr «لَا»nın mahzûf haberine müteallik"), ref=("عَبْدِ عَمْرٍو", "ʿAbd ʿAmr", "Abdü Amr'a")),
 NO("غَيْرَ", "ghayr", R("mst") + MUD, nt("عَلَى الِاسْتِثْنَاءِ الْمُنْقَطِعِ، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "an exception of a different kind (munqaṭiʿ); the masdar that the clause after it makes is its second term, in the seat of jarr", "munkatı istisnâ üzere; ondan sonraki müevvel masdar muzâfun ileyh olarak mahallen mecrûr")),
 PT("أَنَّ", "anna", mk("حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرٍ", "The particle of emphasis and nasb that makes a masdar of its clause", "Tekit, nasb ve masdar harfi", "inna-wa-akhawatuha", "mawadi-fath-anna")),
 PJ("لَهُ", "لَ", "li", "هُ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «أَنَّ» مُقَدَّمٍ", "the phrase hangs on the omitted predicate of أَنَّ, set first", "câr-mecrûr «أَنَّ»nin öne geçmiş mahzûf haberine müteallik")),
 NO("غِنًى", "ghina", R("ism:أَنَّ", "maqh"), nt("مُؤَخَّرٌ", "placed last", "sona bırakılmıştır"), p=HEMI),
 PT("وَأَنَّ", "anna", mk("حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرٍ", "the particle of emphasis and nasb that makes a masdar of its clause", "tekit, nasb ve masdar harfi", "inna-wa-akhawatuha"), nt("وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْمَصْدَرِ قَبْلَهُ", "the masdar it makes is conjoined to the one before", "müevvel masdar öncekine ma'tûf"), pre="wa"),
 PJ("لَهُ", "لَ", "li", "هُ", nt("خَبَرُ «أَنَّ» مُقَدَّمٌ", "the predicate of أَنَّ, set first", "«أَنَّ»nin öne geçmiş haberi")),
 NO("كَشْحًا", "kashh", R("ism:أَنَّ"), nt("مُؤَخَّرٌ؛ الْكَشْحُ: الْخَصْرُ", "placed last; الكَشْح: the waist", "sona bırakılmıştır; الكَشْح: bel")),
 PT("إِذَا", "idha", IDHA_SH, nt("وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ «أَهْضَمَا»؛ وَالشَّرْطُ مُعْتَرِضٌ بَيْنَ الْمَوْصُوفِ وَصِفَتِهِ", "its answer is left out, shown by «slender»; the condition stands between the noun and its adjective", "cevabı mahzûftur, «أَهْضَمَا» ona delâlet eder; şart, mevsûf ile sıfatı arasında mu'tarızadır", "jumla-mutarida")),
 VB("قَامَ", "qama", "madi", JM("mudaf", "إِذَا"), who=("هُوَ", ("عَبْدِ عَمْرٍو", "ʿAbd ʿAmr", "Abdü Amr'a")), g=["hollow-verbs"]),
 NO("أَهْضَمَا", "ahdam", mk("نَعْتٌ لِـ«كَشْحًا» مَنْصُوبٌ بِالْفَتْحَةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»، وَالْأَلِفُ لِلْإِطْلَاقِ", "An adjective of «a waist», in nasb by the fatha; it takes no tanwin, being a diptote (an adjective on the pattern أَفْعَل), and its alif is the alif of the unbound rhyme", "«كَشْحًا»nın na'tı, fetha ile mansûb; vasfiyet ve «أَفْعَل» vezni sebebiyle gayr-i munsarif olduğu için tenvin almaz; elif ıtlak içindir", "naat-sifa", "mamnu-min-sarf", "al-qafiya"), nt("الْأَهْضَمُ: اللَّطِيفُ الْكَشْحِ الضَّامِرُ الْبَطْنِ", "الأَهْضَم: slim in the waist, lean in the belly", "الأَهْضَم: beli ince, karnı içeri çekik"), p="،"),
])
V(0, "and that the women of the tribe gather close about him, saying: A palm-branch from the best ground of Malham!»",
  "bir de kabilenin kadınları çevresinde toplanıp «Melhem vadisinin en verimli yerinden bir hurma dalı!» diyorlar.»", [
 PT("وَأَنَّ", "anna", mk("حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرٍ", "the particle of emphasis and nasb that makes a masdar of its clause", "tekit, nasb ve masdar harfi", "inna-wa-akhawatuha"), nt("وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى مَا قَبْلَهُ", "the masdar it makes is conjoined to those before", "müevvel masdar öncekilere ma'tûf"), pre="wa"),
 NO("نِسَاءَ", "nisa", R("ism:أَنَّ") + MUD),
 NO("الْحَيِّ", "hayy-tribe", "mi"),
 VB("يَعْكُفْنَ", "akafa", "mud-fn", JM("kh", "أَنَّ"), nt("عَكَفَ حَوْلَهُ: أَقَامَ عِنْدَهُ وَلَزِمَهُ", "عَكَفَ حَوْلَهُ: to stay close about someone", "عَكَفَ حَوْلَهُ: birinin çevresinden ayrılmamak")),
 NO("حَوْلَهُ", "hawla", R("zm"), ZON("يَعْكُفْنَ"), enc="هُ", p=HEMI),
 VB("يَقُلْنَ", "qala", "mud-fn", JM("hal", "نِسَاءَ"), g=["hollow-verbs"]),
 NO("عَسِيبٌ", "asib", R("khm"), nt("أَيْ: هُوَ عَسِيبٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ؛ الْعَسِيبُ: جَرِيدَةُ النَّخْلِ الْمُسْتَقِيمَةُ. وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — تَشْبِيهٌ بَلِيغٌ حُذِفَ فِيهِ الْمُشَبَّهُ وَالْأَدَاةُ وَوَجْهُ الشَّبَهِ: الْمُشَبَّهُ عَبْدُ عَمْرٍو، وَالْمُشَبَّهُ بِهِ الْعَسِيبُ", "that is, «he is a palm-branch»; the clause is what they say, in the seat of nasb. العَسِيب: a straight stripped palm-branch. By the Talkhīṣ's definition, a tashbih balīgh, with the thing likened, the particle and the point of likeness all left out: ʿAbd ʿAmr is likened to the palm-branch", "yani «o bir hurma dalıdır»; cümle mekūlü'l-kavl olarak mahallen mansûb. العَسِيب: yaprakları sıyrılmış düz hurma dalı. Telhîs'in tarifine göre müşebbehi, edatı ve vech-i şebehi hazfedilmiş bir teşbih-i belîğdir: Abdü Amr hurma dalına benzetilmiştir", "hadhf-wa-taqdir", "tashbih", "aqsam-al-tashbih")),
 HJ("مِنْ", "min"),
 NO("سَرَارَةِ", "sarara", R("maj") + MUD, ONH("naat", "عَسِيبٌ"), nt("سَرَارَةُ الْوَادِي: أَفْضَلُ مَوْضِعٍ فِيهِ", "سَرَارَة of a valley: its best ground", "vadinin سَرَارَة'si: en verimli yeri")),
 NO("مَلْهَمَا", "malham", mk("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ، وَالْأَلِفُ لِلْإِطْلَاقِ", "The second term of the idafa, in jarr by the fatha in place of the kasra — a diptote, the name of a place treated as feminine; its alif is the alif of the unbound rhyme", "Muzâfun ileyh; alemiyet ve te'nîs sebebiyle gayr-i munsarif olduğundan kesre yerine fetha ile mecrûr; elif ıtlak içindir", "idafa-definiteness", "mamnu-min-sarf", "al-qafiya"), nt("مَلْهَمٌ: قَرْيَةٌ بِالْيَمَامَةِ مَوْصُوفَةٌ بِكَثْرَةِ النَّخْلِ", "Malham: a village of al-Yamāma famed for its palms", "Melhem: Yemâme'de hurmalığıyla meşhur bir köy"), pos="propn", p="."),
])

# =====================================================================================================================
# The Muʿallaqa — verses filed by al-Zawzanī's number
# =====================================================================================================================
# ---- Khawla's ruins; the litters like ships; the fawn of the tribe: verses 1–6 --------------------------------------
ATLAL = ("الْأَطْلَالِ", "the ruins", "kalıntılara")
SAFINA = ("السَّفِينَةِ", "the ship", "gemiye")
def ZW(ar, en, tr):
    """al-Zawzanī's own words on the verse, as a sentence of the line"""
    r = L(("قَالَ الزَّوْزَنِيُّ: " + ar, "Al-Zawzanī: " + en, "Zevzenî: " + tr)); r.sent = True
    return r
V(1, "Khawla has ruins on the stony ground of Thahmad; they gleam like what is left of a tattoo on the back of a hand.",
  "Havle'nin Sehmed'in taşlık arazisinde yurt kalıntıları var; elin sırtında kalmış dövme izi gibi parlıyorlar.", [
 NO("لِخَوْلَةَ", "khawla", R("maj", "fatha"), nt("لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", "a feminine proper name", "alemiyet ve te'nîs sebebiyle"), ONH("khm", "أَطْلَالٌ"), pre="li", pos="propn", g=["taqdim-al-musnad"]),
 NO("أَطْلَالٌ", "talal", R("mubm"), nt("جَمْعُ طَلَلٍ: مَا شَخَصَ مِنْ رُسُومِ الدَّارِ؛ وَسَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ تَقَدُّمُ الْخَبَرِ", "the plural of طَلَل: what still stands of the traces of a dwelling; the indefinite may open the sentence because its predicate is set before it", "«طَلَل»in cem'i: yurt izlerinden ayakta kalan; nekreyle başlamayı haberin öne geçmesi câiz kılmıştır", "jam-taksir")),
 NO("بِبُرْقَةِ", "burqa", R("maj") + MUD, ONH("naat", "أَطْلَالٌ"), nt("وَجُوِّزَ تَعْلِيقُهُمَا بِـ«تَلُوحُ»", "they may also be hung on «تَلُوحُ»", "«تَلُوحُ» fiiline bağlanması da câiz görülmüştür"), pre="bi"),
 NO("ثَهْمَدِ", "thahmad", "mi", nt("وَالْبَيْتُ مُصَرَّعٌ: عَرُوضُهُ مُقَفَّاةٌ تَقْفِيَةَ ضَرْبِهِ", "the verse is muṣarraʿ: its first half ends on the rhyme of its second", "beyit musarradır: ilk mısraı da ikinci mısraın kafiyesiyle biter"), pos="propn", q=True, p=HEMI),
 VB("تَلُوحُ", "laha-verb", "mud", JM("sifa", "أَطْلَالٌ", "raf"), nt("وَيَجُوزُ أَنْ تَكُونَ حَالًا مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «بِبُرْقَةِ»؛ تَلُوحُ: تَلْمَعُ", "it may also be a hal of the pronoun hidden in «بِبُرْقَةِ»; تَلُوحُ: they gleam", "«بِبُرْقَةِ»deki gizli zamirden hâl olması da câizdir; تَلُوحُ: parlar"), who=("هِيَ", "أَطْلَالٌ"), g=["hollow-verbs", "jumla-sifa"]),
 NO("كَبَاقِي", "baqi", R("maj", "man") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: تَلُوحُ لَوْحًا كَلَوْحِ بَاقِي الْوَشْمِ؛ وَهُوَ مِنْ إِضَافَةِ الصِّفَةِ إِلَى الْمَوْصُوفِ", "the phrase hangs on an omitted adjective of an omitted absolute object: «they gleam with a gleam like that of the rest of a tattoo»; the adjective is annexed to the noun it describes", "câr-mecrûr, mahzûf mef'ûlün mutlakın mahzûf na'tına müteallik: «dövme kalıntısının parlayışı gibi bir parlayışla parlar»; sıfatın mevsûfuna izâfetidir", "hadhf-wa-taqdir", "maful-mutlaq"),
    TSB("mm", ("لَمَعَانُ آثَارِ دِيَارِهَا وَوُضُوحُهَا", "the gleam and plainness of the traces of her abodes", "yurdunun izlerinin parlayışı ve belirginliği"), ("لَمَعَانُ آثَارِ الْوَشْمِ فِي ظَاهِرِ الْكَفِّ", "the gleam of the marks of a tattoo on the back of the hand", "elin sırtındaki dövme izlerinin parlayışı"), "ka"), pre="ka", g=TSB_TAGS),
 NO("الْوَشْمِ", "washm", "mi"),
 HJ("فِي", "fi"),
 NO("ظَاهِرِ", "zahir", R("maj") + MUD, ONH("hal", "بَاقِي الْوَشْمِ")),
 NO("الْيَدِ", "yad", "mi", g=["al-qafiya"]),
])
V(2, "— while my companions, halting their mounts there over me, say: «Do not perish of grief; bear up.»",
  "Arkadaşlarım orada bineklerini başımda durdurmuş, «Üzüntüden helâk olma, dayan» diyorlardı.", [
 NO("وُقُوفًا", "wuquf", R("hal"), nt("وَالْعَامِلُ فِيهِ «تَلُوحُ» فِي الْبَيْتِ قَبْلَهُ (التِّبْرِيزِيُّ) — جَمْعُ وَاقِفٍ كَجَالِسٍ وَجُلُوسٍ، يَرْفَعُ «صَحْبِي» وَيَنْصِبُ «مَطِيَّهُمْ»", "its governor is «تَلُوحُ» in the verse before (al-Tibrīzī) — the plural of وَاقِف (as جُلُوس of جَالِس); it raises «صَحْبِي» and puts «مَطِيَّهُمْ» in nasb", "âmili önceki beyitteki «تَلُوحُ»dur (Tebrîzî) — «وَاقِف»in cem'idir (câlis–cülûs gibi); «صَحْبِي»yi ref', «مَطِيَّهُمْ»ü nasb eder", "jam-taksir")),
 PJ("بِهَا", "بِ", "bi", "هَا", ON("وُقُوفًا"), nt("الْبَاءُ بِمَعْنَى «فِي»", "the ba means «in»", "bâ «-de» anlamındadır"), ref=ATLAL),
 NO("صَحْبِي", "sahb", R("fail", "yam"), nt("فَاعِلُ «وُقُوفًا»؛ جَمْعُ صَاحِبٍ", "the doer of «وُقُوفًا»; the plural of صَاحِب", "«وُقُوفًا»nın fâili; «صَاحِب»in cem'i"), enc="ي"),
 PJ("عَلَيَّ", "عَلَيْ", "ala", "يَ", ON("وُقُوفًا"), nt("أَيْ: لِأَجْلِي أَوْ عَلَى رَأْسِي", "for my sake, or over my head", "benim için ya da başımda")),
 NO("مَطِيَّهُمْ", "matiyy", R("maf"), nt("مَفْعُولُ «وُقُوفًا»؛ الْمَطِيُّ: الْمَرَاكِبُ، وَاحِدَتُهَا مَطِيَّةٌ", "the object of «وُقُوفًا»; المَطِيّ: riding-beasts, singular مَطِيَّة", "«وُقُوفًا»nın mef'ûlü; المَطِيّ: binekler, tekili مَطِيَّة"), enc="هُمْ", p=HEMI),
 VB("يَقُولُونَ", "qala", "mud5", JM("hal", "صَحْبِي"), g=["hollow-verbs", "al-hal-jumla-wa-rabituha"]),
 PT("لَا", "la-nahiya", mk("نَاهِيَةٌ جَازِمَةٌ", "The prohibitive لَا, which puts the verb in jazm", "Cezm eden nehiy lâsı", "la-nahiya", "al-nahy-wa-wujuhuh", "al-amr-wa-wujuhuh"),
    HD("أَنَّ النَّهْيَ هُنَا وَالْأَمْرَ بَعْدَهُ الْتِمَاسٌ: طَلَبٌ مِنَ الْمُسَاوِي بِلَا اسْتِعْلَاءٍ، يَنْهَوْنَهُ عَنِ الْجَزَعِ وَيَأْمُرُونَهُ بِالتَّصَبُّرِ", "the prohibition here and the command after it are iltimās — a request between equals, with no claim of rank: they turn him from despair and bid him be patient", "buradaki nehiy ve ardından gelen emir iltimastır — üstünlük taslamadan denk kişiden yapılan talep: onu feryattan alıkoyar, sabra çağırırlar")),
 VB("تَهْلِكْ", "halaka", "jz", JM("maqul"), by="la", who="أَنْتَ"),
 NO("أَسًى", "asan", R("ml", "maqh"), nt("كَذَا أَعْرَبَ الزَّوْزَنِيُّ نَظِيرَهُ فِي مُعَلَّقَةِ امْرِئِ الْقَيْسِ؛ وَقِيلَ: مَفْعُولٌ مُطْلَقٌ أَوْ حَالٌ", "so al-Zawzanī parses its twin in the Muʿallaqa of Imruʾ al-Qays; it is also read as an absolute object, or as a hal", "Zevzenî, İmruülkays'ın Muallakası'ndaki benzerini böyle i'râb eder; mef'ûlün mutlak ya da hâl olduğu da söylenmiştir", "masdar")),
 VB("وَتَجَلَّدِ", "tajallada", "amr", nt("التَّجَلُّدُ: تَكَلُّفُ الْجَلَادَةِ وَهُوَ التَّصَبُّرُ (الزَّوْزَنِيُّ)؛ وَالْبَيْتُ بَيْتُ امْرِئِ الْقَيْسِ بِعَيْنِهِ إِلَّا الْقَافِيَةَ «وَتَجَمَّلِ»، وَقَالَ الزَّوْزَنِيُّ: تَفْسِيرُهُ هُنَا كَتَفْسِيرِهِ هُنَاكَ", "التَّجَلُّد: to put on fortitude, to make oneself patient (al-Zawzanī). The verse is Imruʾ al-Qays's own, all but its rhyme-word «وَتَجَمَّلِ»; al-Zawzanī: it is explained here as it is there", "التَّجَلُّد: kendini metin olmaya zorlamak, sabretmeye çalışmak (Zevzenî). Beyit, kafiye kelimesi «وَتَجَمَّلِ» dışında İmruülkays'ın beytinin aynıdır; Zevzenî: buradaki şerhi oradaki gibidir"), who="أَنْتَ", pre="wa", q=True, g=["form-v-verbs", "al-amr-wa-wujuhuh"]),
])
V(3, "The litters of the Mālikī woman, on the morning she left, were like great ships in the broad channels of Dad —",
  "Mâlikoğullarından o kadının mahfeleri, ayrılık sabahı, Ded vadisinin geniş yataklarında büyük gemiler gibiydi —", [
 PT("كَأَنَّ", "kaanna", KAANNA_T, JM("ist")),
 NO("حُدُوجَ", "hidj", R("ism:كَأَنَّ") + MUD, nt("جَمْعُ حِدْجٍ: مَرْكَبٌ مِنْ مَرَاكِبِ النِّسَاءِ", "the plural of حِدْج: a women's camel-litter", "«حِدْج»in cem'i: kadınların bindiği deve mahfesi", "jam-taksir")),
 NO("الْمَالِكِيَّةِ", "malikiyya", "mi", nt("مَنْسُوبَةٌ إِلَى بَنِي مَالِكٍ قَبِيلَةٍ مِنْ كَلْبٍ (الزَّوْزَنِيُّ)؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيِ: الْمَرْأَةِ الْمَالِكِيَّةِ", "a nisba to Banū Mālik, a clan of Kalb (al-Zawzanī); it describes a noun left out: «the Mālikī woman»", "Kelb'in bir kolu olan Benî Mâlik'e nisbet (Zevzenî); mahzûf mevsûfun sıfatıdır: «Mâlikli kadın»", "ism-mansub", "hadhf-wa-taqdir")),
 NO("غُدْوَةً", "ghudwa", R("zz"), nt("مُتَعَلِّقٌ بِمَا فِي «كَأَنَّ» مِنْ مَعْنَى التَّشْبِيهِ، أَيْ: غُدْوَةَ فِرَاقِهَا", "it hangs on the sense of likening in كَأَنَّ: «on the morning of her parting»", "«كَأَنَّ»deki teşbih mânâsına müteallik: «ayrıldığı sabah»"), p=HEMI),
 NO("خَلَايَا", "khaliyya", R("kh:كَأَنَّ", "maq") + MUD, nt("جَمْعُ خَلِيَّةٍ: السَّفِينَةُ الْعَظِيمَةُ", "the plural of خَلِيَّة: a great ship", "«خَلِيَّة»nin cem'i: büyük gemi", "jam-taksir"),
    TSB("mm", ("الْإِبِلُ وَعَلَيْهَا الْهَوَادِجُ", "the camels with the litters upon them", "üzerinde mahfeler bulunan develer"), ("السُّفُنُ الْعِظَامُ", "great ships", "büyük gemiler"), "kaanna"), g=TSB_TAGS),
 NO("سَفِينٍ", "safin", "mi", nt("جَمْعُ سَفِينَةٍ، وَقَدْ يَكُونُ وَاحِدًا", "the plural of سَفِينَة; it may also be a singular", "«سَفِينَة»nin cem'i; müfred de olabilir")),
 NO("بِالنَّوَاصِفِ", "nasifa", R("maj"), ONH("hal", "حُدُوجَ"), nt("جَمْعُ نَاصِفَةٍ: أَمَاكِنُ تَتَّسِعُ مِنْ نَوَاحِي الْأَوْدِيَةِ", "the plural of نَاصِفَة: places where the sides of a valley open out", "«نَاصِفَة»nin cem'i: vadilerin kenarlarında genişleyen yerler", "jam-taksir"), pre="bi"),
 HJ("مِنْ", "min"),
 NO("دَدِ", "dad", "maj", ONH("hal", "النَّوَاصِفِ"), nt("دَدٌ: قِيلَ اسْمُ وَادٍ فِي هٰذَا الْبَيْتِ، وَقِيلَ: اللَّهْوُ وَاللَّعِبُ (الزَّوْزَنِيُّ)", "دَد: said to be the name of a valley in this verse; also said to mean play and sport (al-Zawzanī)", "دَد: bu beyitte bir vadi adı olduğu söylenir; «oyun ve eğlence» anlamında olduğu da söylenmiştir (Zevzenî)"), q=True, pos="propn"),
])
V(4, "ships of ʿAdawlā, or of Ibn Yāmin's fleet, which the sailor now turns off the course and now holds straight.",
  "Adevlâ gemileri ya da İbn Yâmin'in gemilerinden; gemici onları kâh yoldan saptırır, kâh doğru yolda götürür.", [
 NO("عَدَوْلِيَّةٌ", "adawli", NA("خَلَايَا", "raf"), nt("وَتُرْوَى بِالْجَرِّ نَعْتًا لِـ«سَفِينٍ»، وَيَجُوزُ أَنْ تَكُونَ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ؛ عَدَوْلَى: قَبِيلَةٌ مِنْ أَهْلِ الْبَحْرَيْنِ (الزَّوْزَنِيُّ)", "also transmitted in jarr, describing «سَفِينٍ»; it may be the predicate of an omitted mubtada too. ʿAdawlā: a tribe of the people of al-Baḥrayn (al-Zawzanī)", "«سَفِينٍ»in na'tı olarak cer ile de rivayet edilir; mahzûf mübtedanın haberi de olabilir. Adevlâ: Bahreyn halkından bir kabile (Zevzenî)", "ism-mansub")),
 PT("أَوْ", "aw", AW_T),
 HJ("مِنْ", "min"),
 NO("سَفِينِ", "safin", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: أَوْ هِيَ مِنْ سَفِينِ ابْنِ يَامِنٍ؛ وَقَالَ ابْنُ الْأَنْبَارِيِّ: هُوَ نَسَقٌ عَلَى «عَدَوْلِيَّةٌ»", "the phrase hangs on the omitted predicate of an omitted mubtada: «or they are of Ibn Yāmin's ships»; Ibn al-Anbārī takes it as conjoined to «عَدَوْلِيَّةٌ»", "câr-mecrûr, mahzûf mübtedanın mahzûf haberine müteallik: «ya da onlar İbn Yâmin'in gemilerindendir»; İbnü'l-Enbârî onu «عَدَوْلِيَّةٌ»e ma'tûf sayar", "hadhf-wa-taqdir")),
 NO("ابْنِ", "ibn", R("mi") + MUD),
 NO("يَامِنٍ", "yamin-man", "mi", nt("ابْنُ يَامِنٍ: رَجُلٌ مِنْ أَهْلِ الْبَحْرَيْنِ؛ وَخَصَّ سُفُنَ هٰذِهِ الْقَبِيلَةِ وَهٰذَا الرَّجُلِ لِعِظَمِهَا (الزَّوْزَنِيُّ)", "Ibn Yāmin: a man of al-Baḥrayn; he names the ships of this tribe and of this man for their size (al-Zawzanī)", "İbn Yâmin: Bahreyn halkından bir adam; bu kabilenin ve bu adamın gemilerini büyüklükleri sebebiyle anmıştır (Zevzenî)"), pos="propn", p=HEMI),
 VB("يَجُورُ", "jara-stray", "mud", JM("sifa", "عَدَوْلِيَّةٌ", "raf"), nt("أَوْ مُسْتَأْنَفَةٌ؛ الْجَوْرُ: الْعُدُولُ عَنِ الطَّرِيقِ", "or it opens a new sentence; الجَوْر: to turn off the way", "ya da istînâfiyyedir; الجَوْر: yoldan sapmak"),
    ZW("ثُمَّ شَبَّهَ سَوْقَ الْإِبِلِ تَارَةً عَلَى الطَّرِيقِ وَتَارَةً عَلَى غَيْرِهِ بِإِجْرَاءِ الْمَلَّاحِ السَّفِينَةَ مَرَّةً عَلَى سَمْتِ الطَّرِيقِ وَمَرَّةً عَادِلًا عَنْهُ", "he then likens the driving of the camels, now on the road and now off it, to the sailor's steering the ship now along its course and now away from it", "sonra develerin kâh yol üzerinde kâh yol dışında sürülmesini, gemicinin gemiyi bir doğru rotada bir ondan saparak yürütmesine benzetmiştir"),
    HD("طِبَاقٌ بَيْنَ الْفِعْلَيْنِ «يَجُورُ» وَ«يَهْتَدِي»: الْعُدُولُ عَنِ الطَّرِيقِ وَلُزُومُهُ", "the two verbs «يَجُورُ» and «يَهْتَدِي» make a tibaq: leaving the way against keeping it", "«يَجُورُ» ile «يَهْتَدِي» fiilleri arasında tıbâk vardır: yoldan sapmak ile yolu tutmak"), g=["hollow-verbs", "jumla-sifa", "tashbih", "tibaq"]),
 PJ("بِهِ", "بِ", "bi", "هِ", ON("يَجُورُ"), nt("الْبَاءُ لِلتَّعْدِيَةِ (الزَّوْزَنِيُّ)؛ وَذُكِّرَ الضَّمِيرُ لِأَنَّ «السَّفِينَ» يُذَكَّرُ؛ وَفِي رِوَايَةِ التِّبْرِيزِيِّ وَالدُّرَّةِ: «بِهَا»", "the ba makes the verb transitive (al-Zawzanī); the pronoun is masculine because السَّفِين may be treated as masculine; al-Tibrīzī and al-Durra read «بِهَا»", "bâ ta'diye içindir (Zevzenî); «السَّفِين» müzekker sayılabildiği için zamir müzekkerdir; Tebrîzî ve Dürre «بِهَا» rivayet eder"), ref="سَفِينِ"),
 NO("الْمَلَّاحُ", "mallah", "fail"),
 NO("طَوْرًا", "tawr", R("zz"), ZON("يَجُورُ"), nt("الطَّوْرُ: التَّارَةُ", "الطَّوْر: a time, a turn", "الطَّوْر: kez, defa")),
 VB("وَيَهْتَدِي", "ihtada", "mud-y", JM("atf", "يَجُورُ"), nt("يُطَابِقُ «يَجُورُ»", "the contrary of «يَجُورُ»", "«يَجُورُ»nun zıddı"), who=("هُوَ", "الْمَلَّاحُ"), pre="wa", g=["form-viii-verbs", "naqis-verbs", "tibaq", "al-qafiya"]),
])
V(5, "Her prow cleaves the ripples of the water with her, as a player at fiyāl parts the heaped earth with his hand.",
  "Geminin göğsü suyun dalgalarını yarar; tıpkı «fiyâl» oynayanın yığılmış toprağı eliyle ikiye ayırması gibi.", [
 VB("يَشُقُّ", "shaqqa", "mud", JM("ist"), g=["doubled-verbs"]),
 NO("حَبَابَ", "habab", R("maf") + MUD, nt("حَبَابُ الْمَاءِ: أَمْوَاجُهُ، الْوَاحِدَةُ حَبَابَةٌ", "حَبَاب of water: its ripples, singular حَبَابَة", "suyun حَبَاب'ı: dalgacıkları; tekili حَبَابَة")),
 NO("الْمَاءِ", "ma-water", "mi"),
 NO("حَيْزُومُهَا", "hayzum", "fail", nt("الْحَيْزُومُ: الصَّدْرُ", "الحَيْزُوم: the breast", "الحَيْزُوم: göğüs"), enc="هَا"),
 PJ("بِهَا", "بِ", "bi", "هَا", ON("يَشُقُّ"), ref=SAFINA, p=HEMI),
 PT("كَمَا", "kama", mk("الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَمَا مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ فِي مَحَلِّ جَرٍّ بِالْكَافِ", "The kaf is a jarr letter of likening and مَا makes a masdar of the verb after it; that masdar is in the seat of jarr by the kaf", "Kâf teşbih bildiren cer harfi, مَا masdariyye; ondan ve fiilden oluşan müevvel masdar kâf ile mahallen mecrûr", "huruf-jarr", "anwa-ma", "hadhf-wa-taqdir", "maful-mutlaq"),
    nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: يَشُقُّ شَقًّا كَشَقِّ الْمُفَايِلِ التُّرَابَ", "the phrase hangs on an omitted adjective of an omitted absolute object: «it cleaves with a cleaving like the player's parting of the earth»", "câr-mecrûr, mahzûf mef'ûlün mutlakın mahzûf na'tına müteallik: «oyuncunun toprağı yarışı gibi bir yarışla yarar»"),
    TSB("mm", ("شَقُّ السُّفُنِ الْمَاءَ", "the ships' cleaving of the water", "gemilerin suyu yarması"), ("شَقُّ الْمُفَايِلِ التُّرَابَ الْمَجْمُوعَ بِيَدِهِ", "the player's parting of the heaped earth with his hand", "oyuncunun yığılmış toprağı eliyle yarması"), "kama"), g=TSB_TAGS),
 VB("قَسَمَ", "qasama", "madi", nt("وَالْجُمْلَةُ صِلَةُ «مَا» الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause is the ṣila of the masdar-making مَا and has no seat", "cümle masdariyye «مَا»nın sılasıdır, i'râbdan mahalli yoktur")),
 NO("التُّرْبَ", "turb", "maf", nt("التُّرْبُ وَالتُّرَابُ وَاحِدٌ", "التُّرْب and التُّرَاب are one: earth, dust", "التُّرْب ile التُّرَاب birdir: toprak")),
 NO("الْمُفَايِلُ", "mufayil", "fail", nt("اسْمُ فَاعِلٍ مِنْ «فَايَلَ»؛ الْفِيَالُ: ضَرْبٌ مِنَ اللَّعِبِ: يُجْمَعُ التُّرَابُ فَيُدْفَنُ فِيهِ شَيْءٌ ثُمَّ يُقْسَمُ نِصْفَيْنِ وَيُسْأَلُ عَنِ الدَّفِينِ فِي أَيِّهِمَا هُوَ (الزَّوْزَنِيُّ)", "the ism fa'il of فَايَلَ. الفِيَال is a game: earth is heaped, something is hidden in it, the heap is cut in two, and one is asked in which half the hidden thing lies (al-Zawzanī)", "«فَايَلَ»den ism-i fâil. الفِيَال bir oyundur: toprak yığılır, içine bir şey gömülür, yığın ikiye bölünür ve gömülen şeyin hangi yarıda olduğu sorulur (Zevzenî)", "ism-fail")),
 NO("بِالْيَدِ", "yad", "maj", ON("قَسَمَ"), pre="bi", g=["al-qafiya"]),
])
V(6, "And in the tribe there is a dark-lipped fawn, grown and weaned, shaking down the arāk-fruit — wearing, one over the other, two strings of pearl and chrysolite.",
  "Kabilede, erâk meyvesini silkeleyen, dudakları esmer, büyümüş bir ceylan yavrusu var — üst üste iki dizi inci ve zebercet takınmış.", [
 HJ("وَفِي", "fi", pre="wa-ist"),
 NO("الْحَيِّ", "hayy-tribe", "maj", ONH("khm", "أَحْوَى"), g=["taqdim-al-musnad"]),
 NO("أَحْوَى", "ahwa", R("mubm", "maq"), nt("وَهُوَ فِي الْأَصْلِ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: ظَبْيٌ أَحْوَى؛ الْأَحْوَى: الَّذِي فِي شَفَتَيْهِ سُمْرَةٌ", "in origin an adjective whose noun is left out: «a dark-lipped (gazelle)»; الأَحْوَى: one with a dusky tinge on the lips", "aslında mevsûfu mahzûf bir sıfattır: «dudakları esmer (ceylan)»; الأَحْوَى: dudaklarında esmerlik olan", "hadhf-wa-taqdir"),
    ZW("يَقُولُ: وَفِي الْحَيِّ حَبِيبٌ يُشْبِهُ ظَبْيًا أَحْوَى؛ شَبَّهَهُ بِالظَّبْيِ فِي ثَلَاثَةِ أَشْيَاءَ: فِي كَحَلِ الْعَيْنَيْنِ وَحُوَّةِ الشَّفَتَيْنِ وَحُسْنِ الْجِيدِ", "he says: in the tribe is a loved one who resembles a dark-lipped gazelle; he likens him to the gazelle in three things — the darkness of the eyes, the dusk of the lips and the beauty of the neck", "der ki: kabilede dudakları esmer bir ceylana benzeyen bir sevgili var; onu ceylana üç şeyde benzetmiştir: gözlerin sürmeliliği, dudakların esmerliği ve boynun güzelliği"),
    HD("اسْتِعَارَةٌ مُصَرَّحَةٌ: ذُكِرَ الْمُشَبَّهُ بِهِ (الظَّبْيُ الْأَحْوَى الشَّادِنُ) وَأُرِيدَ الْمُشَبَّهُ (الْحَبِيبُ)", "an istiʿāra muṣarraḥa: the thing likened to (the dark-lipped fawn) is named, and the thing likened (the beloved) is meant", "istiâre-i musarraha vardır: müşebbehün bih (dudakları esmer ceylan yavrusu) zikredilmiş, müşebbeh (sevgili) kastedilmiştir"), g=["istiara", "aqsam-al-istiara"]),
 VB("يَنْفُضُ", "nafada", "mud", JM("sifa", "أَحْوَى", "raf"), ZW("أَيْ: فِي حَالِ نَفْضِ الظَّبْيِ ثَمَرَ الْأَرَاكِ، لِأَنَّهُ يَمُدُّ عُنُقَهُ فِي تِلْكَ الْحَالِ", "that is, as the gazelle shakes down the fruit of the arāk — for it stretches its neck then", "yani ceylan erâk meyvesini silkelerken; çünkü o sırada boynunu uzatır"),
    HD("تَرْشِيحٌ لِلِاسْتِعَارَةِ: وَصْفٌ يُلَائِمُ الْمُسْتَعَارَ مِنْهُ", "this is tarshīḥ of the istiʿāra: a description that suits the thing borrowed FROM (the gazelle)", "bu, istiârenin terşîhidir: müsteârun minhe (ceylana) uygun bir vasıf"), who=("هُوَ", "أَحْوَى"), g=["jumla-sifa", "tarshih-wa-tajrid"]),
 NO("الْمَرْدَ", "mard", "maf", nt("الْمَرْدُ: ثَمَرُ الْأَرَاكِ", "المَرْد: the fruit of the arāk tree", "المَرْد: erâk ağacının meyvesi")),
 NO("شَادِنٌ", "shadin", NA("أَحْوَى", "raf"), nt("وَقِيلَ: بَدَلٌ مِنْهُ؛ الشَّادِنُ: الْغَزَالُ الَّذِي قَوِيَ وَاسْتَغْنَى عَنْ أُمِّهِ (الزَّوْزَنِيُّ)", "also read as a badal of it; الشَّادِن: the young gazelle grown strong enough to do without its mother (al-Zawzanī)", "ondan bedel olduğu da söylenmiştir; الشَّادِن: güçlenip annesine muhtaç olmaktan çıkmış ceylan yavrusu (Zevzenî)"), p=HEMI),
 NO("مُظَاهِرُ", "muzahir", NA("أَحْوَى", "raf") + MUD, nt("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ، وَيَجُوزُ نَصْبُهُ حَالًا؛ الْمُظَاهِرُ: الَّذِي لَبِسَ عِقْدًا فَوْقَ عِقْدٍ", "the ism fa'il annexed to its object; it may also be read in nasb as a hal. المُظَاهِر: one who wears one necklace over another", "ism-i fâilin mef'ûlüne izâfeti; hâl olarak nasbı da câizdir. المُظَاهِر: gerdanlığı gerdanlık üstüne takan", "ism-fail", "idafa-lafziyya"),
    ZW("ثُمَّ صَرَّحَ بِأَنَّهُ يُرِيدُ إِنْسَانًا", "here he makes it plain that he means a human being", "burada bir insanı kastettiğini açıkça belirtir"),
    HD("تَجْرِيدٌ لِلِاسْتِعَارَةِ: وَصْفٌ يُلَائِمُ الْمُسْتَعَارَ لَهُ", "this is tajrīd of the istiʿāra: a description that suits the thing borrowed FOR (the beloved)", "bu, istiârenin tecrîdidir: müsteârun lehe (sevgiliye) uygun bir vasıf"), g=["tarshih-wa-tajrid"]),
 NO("سِمْطَيْ", "simt", R("mi", "ya2") + MUD, nt("وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ؛ السِّمْطُ: الْخَيْطُ الَّذِي نُظِمَتْ فِيهِ الْجَوَاهِرُ", "its nun is dropped for the annexation; السِّمْط: the thread on which gems are strung", "nûnu izâfet sebebiyle düşmüştür; السِّمْط: mücevherlerin dizildiği ip")),
 NO("لُؤْلُؤٍ", "lulu", "mi"),
 NO("وَزَبَرْجَدِ", "zabarjad", AT("لُؤْلُؤٍ", "jarr"), pre="wa", q=True),
])
# ---- Her smile and her face; then the she-camel: verses 7–13 ---------------------------------------------------------
HABIBA = ("الْحَبِيبَةِ", "the beloved", "sevgiliye")
MAWSUF_NAQA = nt("نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: بِنَاقَةٍ", "it describes a noun left out: «a she-camel»", "mahzûf mevsûfun sıfatıdır: «bir dişi deve»", "hadhf-wa-taqdir")
def NAQA_N(case="jarr", sign=""):
    """a further adjective of the she-camel that the adjectives of vv. 11 ff. describe"""
    s = SIGN(case, sign)
    return mk("نَعْتٌ آخَرُ لِلنَّاقَةِ الْمَوْصُوفَةِ فِي الْبَيْتِ ١١ " + s[0], "A further adjective of the she-camel described from verse 11 on, " + s[1], "11. beyitten beri vasfedilen devenin bir başka na'tı, " + s[2], "naat-sifa", *s.tags)
RAF_JAIZ = nt("وَيَجُوزُ رَفْعُهُ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ", "it may also be read in raf', as the predicate of an omitted mubtada", "mahzûf mübtedanın haberi olarak ref'i de câizdir")
V(7, "A doe that has left her young, grazing with a herd in a wooded sandy tract; she reaches for the tips of the arāk-fruit and wraps herself in its boughs.",
  "Yavrularını bırakmış bir ceylandır o; ağaçlı bir kumlukta sürüyle otlar; erâk meyvesinin uçlarına uzanır ve dallarına bürünür.", [
 NO("خَذُولٌ", "khadhul", R("khm"), nt("أَيْ: هِيَ خَذُولٌ؛ وَقِيلَ: نَعْتٌ لِـ«أَحْوَى». الْخَذُولُ: الَّتِي خَذَلَتْ أَوْلَادَهَا", "that is, «she is a doe that has left…»; it is also read as an adjective of «أَحْوَى». الخَذُول: one that has forsaken her young", "yani «o, … bir ceylandır»; «أَحْوَى»nın na'tı olduğu da söylenmiştir. الخَذُول: yavrularını bırakıp giden", "hadhf-wa-taqdir", "sighat-mubalagha")),
 VB("تُرَاعِي", "raa-graze", "mud-y", JM("hal", "خَذُولٌ"), nt("أَيْ: مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِيهَا، وَقِيلَ: نَعْتٌ لَهَا؛ تُرَاعِي رَبْرَبًا: تَرْعَى مَعَهُ", "that is, of the pronoun hidden in it; it is also read as its adjective. تُرَاعِي رَبْرَبًا: she grazes along with a herd", "yani ondaki gizli zamirden; na'tı olduğu da söylenmiştir. تُرَاعِي رَبْرَبًا: bir sürüyle birlikte otlar"), who=("هِيَ", "خَذُولٌ"), g=["form-iii-verbs", "naqis-verbs"]),
 NO("رَبْرَبًا", "rabrab", "maf", nt("الرَّبْرَبُ: الْقَطِيعُ مِنَ الظِّبَاءِ وَبَقَرِ الْوَحْشِ", "الرَّبْرَب: a herd of gazelles or of wild cattle", "الرَّبْرَب: ceylan ya da yaban sığırı sürüsü")),
 NO("بِخَمِيلَةٍ", "khamila", "maj", ON("تُرَاعِي"), nt("الْخَمِيلَةُ: رَمْلَةٌ مُنْبِتَةٌ، أَوْ أَرْضٌ ذَاتُ شَجَرٍ", "الخَمِيلَة: a sand-tract that bears growth, or ground with trees", "الخَمِيلَة: bitki bitiren kumluk ya da ağaçlı arazi"), pre="bi", p=HEMI),
 VB("تَنَاوَلُ", "tanawala", "mud", nt("أَصْلُهُ تَتَنَاوَلُ فَحُذِفَتْ إِحْدَى التَّاءَيْنِ تَخْفِيفًا؛ وَالْجُمْلَةُ كَجُمْلَةِ «تُرَاعِي»", "for تَتَنَاوَلُ, one of the two ta's dropped for lightness; the clause stands as the clause of «تُرَاعِي» does", "aslı تَتَنَاوَلُ olup iki tâ'dan biri hafiflik için düşmüştür; cümlenin mahalli «تُرَاعِي» cümlesi gibidir"), who=("هِيَ", "خَذُولٌ"), g=["form-vi-verbs"]),
 NO("أَطْرَافَ", "taraf", R("maf") + MUD, g=["jam-taksir"]),
 NO("الْبَرِيرِ", "barir", "mi", nt("الْبَرِيرُ: ثَمَرُ الْأَرَاكِ الْمُدْرِكُ الْبَالِغُ", "البَرِير: the ripe fruit of the arāk", "البَرِير: erâk ağacının olgun meyvesi")),
 VB("وَتَرْتَدِي", "irtada", "mud-y", JM("atf", "تَنَاوَلُ"), nt("وَالْمَفْعُولُ مَحْذُوفٌ أَيْ: تَرْتَدِي بِأَغْصَانِهِ", "its object is left out: «she wraps herself in its boughs»", "mef'ûlü mahzûftur: «dallarına bürünür»", "hadhf-al-maful"),
    ZW("وَإِنَّمَا خَصَّ تِلْكَ الْحَالَ لِمَدِّهَا عُنُقَهَا إِلَى ثَمَرِ الشَّجَرَةِ؛ شَبَّهَ طُولَ عُنُقِ الْحَبِيبِ وَحُسْنَهُ بِذٰلِكَ", "he singles out that state because she stretches her neck to the fruit of the tree: to that he likens the length and beauty of the loved one's neck", "o hâli özellikle anmıştır, çünkü ceylan o sırada boynunu ağacın meyvesine uzatır; sevgilinin boynunun uzunluğunu ve güzelliğini buna benzetmiştir"),
    HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْفِعْلِ: شَبَّهَ اسْتِتَارَهَا بِالْأَغْصَانِ بِلُبْسِ الرِّدَاءِ", "an istiʿāra tabaʿiyya in the verb: being hidden among the boughs is likened to putting on a mantle", "fiilde istiâre-i tebeiyye vardır: dalların arasında gizlenmesi ridâ giymeye benzetilmiştir"), who=("هِيَ", "خَذُولٌ"), pre="wa", g=["form-viii-verbs", "naqis-verbs", "istiara-tabaiyya", "tarshih-wa-tajrid", "al-qafiya"]),
])
V(8, "She smiles from a mouth dark in the gums, as though a camomile in flower had come up through pure sand — a dune that is moist for it.",
  "Diş etleri esmer bir ağızla gülümser; sanki saf kumun arasından çıkmış, kendisi için nemli duran bir kum tepesinde çiçek açmış bir papatya.", [
 VB("وَتَبْسِمُ", "basama", "mud", JM("ist"), who=("هِيَ", HABIBA), pre="wa-ist"),
 HJ("عَنْ", "an"),
 NO("أَلْمَى", "alma", R("maj", "maq"), ON("تَبْسِمُ"), nt("نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: عَنْ ثَغْرٍ أَلْمَى؛ الْأَلْمَى: الَّذِي يَضْرِبُ لَوْنُ شَفَتَيْهِ إِلَى السَّوَادِ", "it describes a noun left out: «from a (mouth) dark of lip»; الأَلْمَى: one whose lips shade towards black", "mahzûf mevsûfun sıfatıdır: «dudakları esmer (bir ağız)dan»; الأَلْمَى: dudaklarının rengi siyaha çalan", "hadhf-wa-taqdir")),
 PT("كَأَنَّ", "kaanna", KAANNA_T, nt("وَخَبَرُهَا مَحْذُوفٌ تَقْدِيرُهُ: كَأَنَّ بِهِ مُنَوِّرًا، وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ", "its predicate is left out — «as though there were in it a flowering camomile» — and the clause is a second adjective of the omitted noun", "haberi mahzûftur — «sanki onda çiçek açmış bir papatya vardır» — cümle mahzûf mevsûfun ikinci na'tıdır", "hadhf-wa-taqdir"),
    TSB("mm", ("ثَغْرُهَا", "her mouth with its teeth", "ağzı ve dişleri"), ("أُقْحُوَانٌ خَرَجَ نَوْرُهُ فِي دِعْصٍ نَدٍ", "a camomile that has come into flower on a moist dune", "nemli bir kum tepesinde çiçek açmış papatya"), "kaanna"), g=TSB_TAGS),
 NO("مُنَوِّرًا", "munawwir", R("ism:كَأَنَّ"), nt("يَعْنِي أُقْحُوَانًا مُنَوِّرًا، فَحَذَفَ الْمَوْصُوفَ اجْتِزَاءً بِدَلَالَةِ الصِّفَةِ عَلَيْهِ (الزَّوْزَنِيُّ)؛ اسْمُ فَاعِلٍ مِنْ «نَوَّرَ النَّبْتُ» إِذَا خَرَجَ نَوْرُهُ", "he means a flowering CAMOMILE, and leaves out the noun because the adjective shows it (al-Zawzanī); the ism fa'il of نَوَّرَ, said of a plant when its blossom comes out", "çiçek açmış PAPATYAYI kasteder; sıfat ona delâlet ettiği için mevsûfu hazfetmiştir (Zevzenî); bitki çiçek açtığında söylenen «نَوَّرَ»den ism-i fâil", "hadhf-wa-taqdir", "ism-fail"), p=HEMI),
 VB("تَخَلَّلَ", "takhallala", "madi", JM("sifa", "مُنَوِّرًا", "nasb"), who=("هُوَ", "مُنَوِّرًا"), g=["form-v-verbs", "jumla-sifa"]),
 NO("حُرَّ", "hurr", R("maf") + MUD, nt("حُرُّ كُلِّ شَيْءٍ: خَالِصُهُ", "the حُرّ of a thing: its pure, unmixed part", "bir şeyin حُرّ'ü: hâlisi, katışıksızı")),
 NO("الرَّمْلِ", "raml", "mi"),
 NO("دِعْصٍ", "dis", BD("الرَّمْلِ", "jarr"), nt("كَذَا فِي الطَّبْعَةِ بِالْجَرِّ؛ وَيُرْوَى بِالرَّفْعِ «دِعْصٌ» (التِّبْرِيزِيُّ)، وَعَلَيْهِ تَقْدِيرُ الزَّوْزَنِيِّ: «تَخَلَّلَ دِعْصٌ لَهُ نَدٍ حُرَّ الرَّمْلِ». الدِّعْصُ: الْكَثِيبُ مِنَ الرَّمْلِ", "so the edition, in jarr; it is also transmitted in raf', «دِعْصٌ» (al-Tibrīzī), and al-Zawzanī's paraphrase follows that reading: «a moist dune lies in the midst of the pure sand». الدِّعْص: a hill of sand", "baskıda cer ile böyledir; ref' ile «دِعْصٌ» de rivayet edilir (Tebrîzî); Zevzenî'nin takdiri de buna göredir: «saf kumun arasında nemli bir tepe bulunur». الدِّعْص: kum tepesi")),
 PJ("لَهُ", "لَ", "li", "هُ", ON("نَدِ"), ref=("الْأُقْحُوَانِ الْمُنَوِّرِ", "the camomile", "papatyaya")),
 NO("نَدِ", "nadin", NA("دِعْصٍ", "jarr", "manh"), nt("أَصْلُهُ «نَدٍ» فَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ؛ وَأَعْرَبَ الدُّرَّةُ «لَهُ» خَبَرًا مُقَدَّمًا وَ«نَدِ» مُبْتَدَأً مُؤَخَّرًا بِمَعْنَى النَّدَاوَةِ", "for نَدٍ, its tanwin dropped at the rhyme. Al-Durra parses «لَهُ» as a predicate set first and «نَدِ» as its mubtada, in the sense of «moisture»", "aslı «نَدٍ» olup tenvini kafiye için düşmüştür. Dürre «لَهُ»yu öne geçmiş haber, «نَدِ»yi «nemlilik» anlamında sona kalmış mübteda olarak i'râb eder"),
    ZW("وَإِنَّمَا جَعَلَهُ نَدِيًّا لِيَكُونَ الْأُقْحُوَانُ غَضًّا نَاضِرًا، وَشَرَطَ لَمَى الشَّفَتَيْنِ لِيَكُونَ أَبْلَغَ فِي بَرِيقِ الثَّغْرِ", "he makes the dune moist so that the camomile may be fresh and bright, and he adds the darkness of the lips because it sets off the gleam of the teeth", "papatya taze ve parlak olsun diye tepeyi nemli kılmış; dişlerin parıltısı daha belirgin olsun diye de dudakların esmerliğini şart koşmuştur"), g=["al-qafiya"]),
])
V(9, "The sun's rays have given it to drink — all but its gums, which are dusted with antimony; and she has bitten on nothing that would mar it.",
  "Ona güneşin ışınları su vermiştir — diş etleri hariç; onlara sürme serpilmiştir; o da dişlerini bozacak bir şeyi ısırmamıştır.", [
 VB("سَقَتْهُ", "saqa-water", "madi-fh", JM("ist"), nt("وَالْهَاءُ لِلثَّغْرِ، وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ", "the هُ is the mouth; the second object is left out", "«hû» ağza döner; ikinci mef'ûl mahzûftur"),
    ZW("سَقَاهُ شُعَاعُ الشَّمْسِ، أَيْ: كَأَنَّ الشَّمْسَ أَعَارَتْهُ ضَوْءَهَا", "the sun's rays watered it — that is, it is as though the sun had lent it its light", "ona güneşin ışınları su vermiştir, yani sanki güneş ona ışığını ödünç vermiştir"),
    HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْفِعْلِ: شَبَّهَ إِكْسَابَ الشَّمْسِ الثَّغْرَ بَرِيقَهُ بِالسَّقْيِ", "an istiʿāra tabaʿiyya in the verb: the sun's giving the mouth its gleam is likened to giving drink", "fiilde istiâre-i tebeiyye vardır: güneşin ağza parıltısını kazandırması su vermeye benzetilmiştir"), enc="هُ", g=["naqis-verbs", "istiara-tabaiyya", "hadhf-al-maful"]),
 NO("إِيَاةُ", "iyat", R("fail") + MUD, nt("إِيَاةُ الشَّمْسِ: شُعَاعُهَا", "إِيَاة of the sun: its rays", "güneşin إِيَاة'si: ışınları")),
 NO("الشَّمْسِ", "shams", "mi"),
 PT("إِلَّا", "illa", mk("حَرْفُ اسْتِثْنَاءٍ", "The particle of exception", "İstisnâ harfi", "istithna")),
 NO("لِثَاتِهِ", "litha", R("mst", "kasra"), nt("يَسْتَثْنِي اللِّثَاتِ لِأَنَّهُ لَا يُسْتَحَبُّ بَرِيقُهَا (الزَّوْزَنِيُّ)؛ اللِّثَةُ: مَغْرِزُ الْأَسْنَانِ", "he excepts the gums because a gleam in them is not admired (al-Zawzanī); اللِّثَة: the flesh in which the teeth are set", "diş etlerini istisna eder, çünkü onların parlaması güzel sayılmaz (Zevzenî); اللِّثَة: dişlerin yerleştiği et"), enc="هِ", p=HEMI),
 VB("أُسِفَّ", "asaffa", "madi", JM("hal", "لِثَاتِهِ"), nt("وَذُكِّرَ الضَّمِيرُ حَمْلًا عَلَى تَذْكِيرِ الْجَمْعِ، وَقِيلَ: يَعُودُ عَلَى الثَّغْرِ وَالْمُرَادُ اللِّثَاتُ؛ أَيْ: ذُرَّ عَلَيْهِ الْإِثْمِدُ", "the pronoun is masculine because a plural may be so treated; it is also said to return to the mouth, the gums being meant. That is: antimony has been dusted on them", "cem'in müzekker sayılabilmesine hamlen zamir müzekkerdir; ağza döndüğü, diş etlerinin kastedildiği de söylenmiştir. Yani üzerine sürme serpilmiştir"), who=("هُوَ", "لِثَاتِهِ"), maj=True, g=["form-iv-verbs", "doubled-verbs"]),
 PT("وَلَمْ", "lam-jazima", LAM_J, pre="wa-hal"),
 VB("تَكْدِمْ", "kadama", "jz", nt("وَالْجُمْلَةُ حَالٌ مِنْ نَائِبِ فَاعِلِ «أُسِفَّ»، أَوْ مُعْتَرِضَةٌ بَيْنَ الْفِعْلِ وَمُتَعَلِّقِهِ؛ الْكَدْمُ: الْعَضُّ، أَيْ: لَمْ تَعَضَّ بِأَسْنَانِهَا عَلَى شَيْءٍ يُؤَثِّرُ فِيهَا", "the clause is a hal of the deputy doer of «أُسِفَّ», or a parenthesis between the verb and what hangs on it. الكَدْم: biting — she has not bitten on anything that would mark her teeth", "cümle «أُسِفَّ»nin nâib-i fâilinden hâl ya da fiil ile müteallakı arasında mu'tarızadır. الكَدْم: ısırmak — dişlerinde iz bırakacak bir şeyi ısırmamıştır", "jumla-mutarida"), by="lam", who=("هِيَ", HABIBA)),
 PJ("عَلَيْهِ", "عَلَيْ", "ala", "هِ", ON("تَكْدِمْ")),
 NO("بِإِثْمِدِ", "ithmid", "maj", ON("أُسِفَّ"), nt("وَتَقْدِيرُهُ: أُسِفَّ بِإِثْمِدٍ وَلَمْ تَكْدِمْ عَلَيْهِ بِشَيْءٍ (الزَّوْزَنِيُّ)؛ الْإِثْمِدُ: الْكُحْلُ", "the order meant is: «dusted with antimony, and she has bitten on nothing» (al-Zawzanī); الإِثْمِد: kohl, antimony", "takdiri: «sürme serpilmiştir ve hiçbir şeyi ısırmamıştır» (Zevzenî); الإِثْمِد: sürme"), pre="bi", q=True),
])
V(10, "And from a face as though the sun had thrown its mantle over it — clear of hue, with no wrinkle in it.",
  "Ve sanki güneşin ridâsını üzerine attığı bir yüzle (gülümser) — rengi duru, hiç kırışmamış.", [
 NO("وَوَجْهٍ", "wajh", AT("أَلْمَى", "jarr"), nt("أَيْ: وَتَبْسِمُ عَنْ وَجْهٍ (الزَّوْزَنِيُّ)؛ وَيُرْوَى بِالرَّفْعِ", "that is, «and she smiles from a face» (al-Zawzanī); it is also transmitted in raf'", "yani «ve bir yüzle gülümser» (Zevzenî); ref' ile de rivayet edilir"), pre="wa"),
 PT("كَأَنَّ", "kaanna", KAANNA_T, JM("sifa", "وَجْهٍ")),
 NO("الشَّمْسَ", "shams", R("ism:كَأَنَّ")),
 VB("أَلْقَتْ", "alqa", "madi-fh", JM("kh", "كَأَنَّ"), who=("هِيَ", "الشَّمْسَ"), g=["form-iv-verbs", "naqis-verbs"]),
 NO("رِدَاءَهَا", "rida-cloak", "maf", ZW("كَأَنَّ الشَّمْسَ كَسَتْهُ ضِيَاءَهَا وَجَمَالَهَا، فَاسْتَعَارَ لِضِيَاءِ الشَّمْسِ اسْمَ الرِّدَاءِ", "it is as though the sun had clothed it in its light and beauty: he borrows the name «mantle» for the light of the sun", "sanki güneş ona ışığını ve güzelliğini giydirmiştir; güneşin ışığı için «ridâ» adını istiâre etmiştir"),
    HD("هِيَ اسْتِعَارَةٌ مُصَرَّحَةٌ: ذُكِرَ الْمُشَبَّهُ بِهِ (الرِّدَاءُ) وَأُرِيدَ الْمُشَبَّهُ (الضِّيَاءُ)", "it is an istiʿāra muṣarraḥa: the thing likened to (the mantle) is named and the thing likened (the light) is meant", "bu bir istiâre-i musarrahadır: müşebbehün bih (ridâ) zikredilmiş, müşebbeh (ışık) kastedilmiştir"), enc="هَا", g=["istiara", "aqsam-al-istiara"], p=HEMI),
 PJ("عَلَيْهِ", "عَلَيْ", "ala", "هِ", ON("أَلْقَتْ"), ref="وَجْهٍ"),
 NO("نَقِيِّ", "naqiyy", NA("وَجْهٍ", "jarr", nth="2") + MUD, nt("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا", "the sifa mushabbaha annexed to its doer", "sıfat-ı müşebbehenin fâiline izâfeti", "sifa-mushabbaha", "idafa-lafziyya"), pos="adj"),
 NO("اللَّوْنِ", "lawn", "mi"),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("يَتَخَدَّدِ", "takhaddada", "jz", JM("sifa", "وَجْهٍ"), nt("التَّخَدُّدُ: التَّشَنُّجُ وَالتَّغَضُّنُ", "التَّخَدُّد: to shrivel and wrinkle", "التَّخَدُّد: büzüşmek, kırışmak"),
    ZW("وَصَفَ وَجْهَهَا بِكَمَالِ الضِّيَاءِ وَالنَّقَاءِ وَالنَّضَارَةِ", "he describes her face as perfect in light, clearness and bloom", "yüzünü kemal derecesinde aydınlık, duruluk ve tazelikle vasfetmiştir"), by="lam", who=("هُوَ", "وَجْهٍ"), q=True, g=["form-v-verbs", "jumla-sifa"]),
])
V(11, "And I — when care comes upon me — drive it off with a brisk, swerving she-camel of quick pace, that travels at evening and at morning;",
  "Ben, gam çöktüğünde onu, akşam da sabah da yol alan, coşkusundan düz yürümeyen hızlı bir dişi deveyle savarım;", [
 PT("وَإِنِّي", "inna", INNA_T + mk("، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the ya is its noun, in the seat of nasb", "; yâ ismi, mahallen mansûb"), JM("ist"), pre="wa-ist", stem="إِنِّي"),
 VB("لَأُمْضِي", "amda", "mud-y", JM("kh", "إِنَّ"), nt("أُمْضِي الْهَمَّ: أُنْفِذُهُ", "أُمْضِي الْهَمَّ: I carry my purpose through, I see my care off", "أُمْضِي الْهَمَّ: tasamı (kararımı) yerine getirip savarım"), who="أَنَا", pre="la-ibt", g=["form-iv-verbs", "naqis-verbs"]),
 NO("الْهَمَّ", "hamm", "maf"),
 NO("عِنْدَ", "inda", R("zz") + MUD, ONH("hal", "الْهَمَّ", zarf=True), nt("وَهُوَ هُنَا بِمَعْنَى الْوَقْتِ؛ وَيَجُوزُ تَعْلِيقُهُ بِـ«أُمْضِي»", "it here means «at the time of»; it may also be hung on «أُمْضِي»", "burada «vaktinde» anlamındadır; «أُمْضِي»ye bağlanması da câizdir")),
 NO("احْتِضَارِهِ", "ihtidar", "mi", nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الِاحْتِضَارُ وَالْحُضُورُ وَاحِدٌ", "the masdar annexed to its doer; الاِحْتِضَار is the same as الحُضُور, «coming»", "masdarın fâiline izâfeti; الاِحْتِضَار ile الحُضُور birdir: «gelmek»", "masdar"), enc="هِ", p=HEMI),
 NO("بِعَوْجَاءَ", "awja", R("maj", "fatha"), nt("لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", "it ends in the long feminine alif", "elif-i memdûde ile müennes olduğu için"), ON("أُمْضِي"), MAWSUF_NAQA, nt("الْعَوْجَاءُ: الَّتِي لَا تَسْتَقِيمُ فِي سَيْرِهَا لِفَرْطِ نَشَاطِهَا", "العَوْجَاء: one that will not go straight, so high is her spirit", "العَوْجَاء: aşırı canlılığından dolayı düz yürümeyen"), pre="bi", g=["ism-mamdud"]),
 NO("مِرْقَالٍ", "mirqal", NA("عَوْجَاءَ", "jarr"), nt("مُبَالَغَةُ مُرْقِلٍ مِنَ الْإِرْقَالِ، وَهُوَ بَيْنَ السَّيْرِ وَالْعَدْوِ", "the intensive of مُرْقِل, from الإِرْقَال — a pace between walking and running", "«مُرْقِل»in mübalağası; الإِرْقَال: yürüyüş ile koşu arası bir gidiş", "sighat-mubalagha")),
 VB("تَرُوحُ", "raha-become", "mud", JM("sifa", "عَوْجَاءَ"), who=("هِيَ", NAQA), g=["hollow-verbs", "jumla-sifa", "tibaq"]),
 VB("وَتَغْتَدِي", "ightada", "mud-y", JM("atf", "تَرُوحُ"),
    ZW("يُرِيدُ أَنَّهَا تَصِلُ سَيْرَ اللَّيْلِ بِسَيْرِ النَّهَارِ وَسَيْرَ النَّهَارِ بِسَيْرِ اللَّيْلِ", "he means that she joins the night's journey to the day's and the day's to the night's", "onun gece yürüyüşünü gündüz yürüyüşüne, gündüzünkünü geceninkine eklediğini kasteder"),
    HD("طِبَاقٌ بَيْنَ الْفِعْلَيْنِ «تَرُوحُ» وَ«تَغْتَدِي»: سَيْرُ الْعَشِيِّ وَسَيْرُ الْغَدَاةِ؛ وَالْجَمْعُ بَيْنَهُمَا كِنَايَةٌ عَنْ دَوَامِ سَيْرِهَا", "the two verbs «تَرُوحُ» and «تَغْتَدِي» make a tibaq — going at evening against going at morning — and the pair together is a kinaya for her never ceasing to travel", "«تَرُوحُ» ile «تَغْتَدِي» fiilleri arasında tıbâk vardır: akşam yürüyüşü ile sabah yürüyüşü; ikisinin bir arada anılması yürüyüşünün sürekliliğinden kinâyedir"), who=("هِيَ", NAQA), pre="wa", g=["form-viii-verbs", "naqis-verbs", "tibaq", "kinaya", "al-qafiya"]),
])
V(12, "sure-footed, her bones like the planks of a great bier; I urged her on along a plain-marked road that was like the back of a striped cloak;",
  "Sürçmesinden emin olunan, kemikleri büyük bir tabutun tahtaları gibi olan (deve); onu, çizgili bir kumaşın sırtına benzeyen apaçık bir yolda sürdüm;", [
 NO("أَمُونٍ", "amun", NAQA_N(), RAF_JAIZ, nt("الْأَمُونُ: الَّتِي يُؤْمَنُ عِثَارُهَا", "الأَمُون: one whose stumbling need not be feared", "الأَمُون: sürçmesinden emin olunan")),
 NO("كَأَلْوَاحِ", "lawh-board", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ آخَرَ لِلنَّاقَةِ", "the phrase hangs on a further omitted adjective of the she-camel", "câr-mecrûr devenin mahzûf bir başka na'tına müteallik"),
    TSB("mm", ("عَرْضُ عِظَامِهَا", "the breadth of her bones", "kemiklerinin genişliği"), ("أَلْوَاحُ التَّابُوتِ الْعَظِيمِ", "the planks of a great bier", "büyük tabutun tahtaları"), "ka"), pre="ka", g=TSB_TAGS + ["jam-taksir"]),
 NO("الْإِرَانِ", "iran", "mi", nt("الْإِرَانُ: التَّابُوتُ الْعَظِيمُ", "الإِرَان: a great bier", "الإِرَان: büyük tabut")),
 VB("نَصَأْتُهَا", "nasaa-urge", "madi-tu", nt("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ؛ نَصَأْتُهَا بِالصَّادِ: زَجَرْتُهَا، وَ«نَسَأْتُهَا» بِالسِّينِ: ضَرَبْتُهَا بِالْمِنْسَأَةِ وَهِيَ الْعَصَا (الزَّوْزَنِيُّ)", "the clause may be an adjective or a hal. نَصَأْتُهَا, with ṣād: I urged her on; «نَسَأْتُهَا», with sīn: I struck her with the staff (al-Zawzanī)", "cümle sıfat da hâl de olabilir. Sâd ile نَصَأْتُهَا: onu sürdüm; sîn ile «نَسَأْتُهَا»: onu değnekle vurdum (Zevzenî)"), enc="هَا", p=HEMI),
 HJ("عَلَى", "ala"),
 NO("لَاحِبٍ", "lahib", "maj", ON("نَصَأْتُهَا"), nt("نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: طَرِيقٍ لَاحِبٍ؛ اللَّاحِبُ: الطَّرِيقُ الْوَاضِحُ", "it describes a noun left out: «a plain road»; اللَّاحِب: a clearly marked road", "mahzûf mevsûfun sıfatıdır: «apaçık bir yol»; اللَّاحِب: belirgin yol", "hadhf-wa-taqdir")),
 PT("كَأَنَّهُ", "kaanna", KAANNA_T + mk("، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the هُ is its noun, in the seat of nasb", "; «hû» ismi, mahallen mansûb"), JM("sifa", "لَاحِبٍ"),
    TSB("mm", ("الطَّرِيقُ", "the road", "yol"), ("الْكِسَاءُ الْمُخَطَّطُ", "a striped cloak", "çizgili kumaş"), "kaanna", ("أَنَّ فِيهِ أَمْثَالَ الْخُطُوطِ", "that it bears what look like stripes", "üzerinde çizgileri andıran izler bulunması")), g=TSB_TAGS, stem="كَأَنَّهُ"),
 NO("ظَهْرُ", "zahr", R("kh:كَأَنَّ") + MUD),
 NO("بُرْجُدِ", "burjud", "mi", nt("الْبُرْجُدُ: كِسَاءٌ مُخَطَّطٌ", "البُرْجُد: a striped cloak", "البُرْجُد: çizgili örtü"), q=True),
])
V(13, "built like a he-camel, firm of flesh; she runs as though she were a hen-ostrich showing herself to a sparse-plumed, ash-grey male.",
  "erkek deve yapılı, eti sıkı; sanki tüyü seyrek, kül rengi bir erkek devekuşuna kendini gösteren dişi bir devekuşuymuş gibi koşar.", [
 NO("جُمَالِيَّةٍ", "jumaliyya", NAQA_N(), RAF_JAIZ, nt("الْجُمَالِيَّةُ: النَّاقَةُ الَّتِي تُشْبِهُ الْجَمَلَ فِي وَثَاقَةِ الْخَلْقِ", "الجُمَالِيَّة: a she-camel like a he-camel in the firmness of her build", "الجُمَالِيَّة: yapısının sağlamlığında erkek deveye benzeyen dişi deve")),
 NO("وَجْنَاءَ", "wajna", NAQA_N("jarr", "fatha"), nt("لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ الْوَجْنَاءُ: الْمُكْتَنِزَةُ اللَّحْمِ، مِنَ الْوَجِينِ وَهُوَ الْأَرْضُ الصُّلْبَةُ", "it ends in the long feminine alif. الوَجْنَاء: firm and close of flesh, from الوَجِين, hard ground", "elif-i memdûde ile müennes olduğu için. الوَجْنَاء: eti sıkı ve dolgun; «sert arazi» anlamındaki الوَجِين'den", "ism-mamdud")),
 VB("تَرْدِي", "rada-run", "mud-y", nt("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ؛ الرَّدَيَانُ: عَدْوُ الْحِمَارِ بَيْنَ مُتَمَرَّغِهِ وَآرِيِّهِ، ثُمَّ يُسْتَعَارُ لِلْعَدْوِ (الزَّوْزَنِيُّ)", "the clause may be an adjective or a hal. الرَّدَيَان: in origin an ass's run between his rolling-place and his tether; then it is borrowed for running (al-Zawzanī)", "cümle sıfat da hâl de olabilir. الرَّدَيَان: aslında eşeğin yuvarlandığı yer ile bağlandığı yer arasındaki koşusu; sonra koşmak için müsteâr kullanılır (Zevzenî)"), who=("هِيَ", NAQA), g=["naqis-verbs"]),
 PT("كَأَنَّهَا", "kaanna", KAANNA_T + mk("، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; هَا is its noun, in the seat of nasb", "; هَا ismi, mahallen mansûb"), nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «تَرْدِي»", "the clause is a hal of the doer of «تَرْدِي», in the seat of nasb", "cümle «تَرْدِي»nin fâilinden hâl olarak mahallen mansûb"),
    TSB("mm", ("عَدْوُ النَّاقَةِ", "the she-camel's run", "devenin koşusu"), ("عَدْوُ النَّعَامَةِ وَهِيَ تَعْرِضُ لِلظَّلِيمِ", "the run of a hen-ostrich as she shows herself to the male", "erkeğine kendini gösteren dişi devekuşunun koşusu"), "kaanna"), g=TSB_TAGS, stem="كَأَنَّهَا", p=HEMI),
 NO("سَفَنَّجَةٌ", "safannaja", R("kh:كَأَنَّ"), nt("السَّفَنَّجَةُ: النَّعَامَةُ", "السَّفَنَّجَة: a hen-ostrich", "السَّفَنَّجَة: dişi devekuşu")),
 VB("تَبْرِي", "bara-show", "mud-y", JM("sifa", "سَفَنَّجَةٌ", "raf"), nt("تَبْرِي لَهُ: تَعْرِضُ لَهُ", "تَبْرِي لَهُ: she presents herself to him", "تَبْرِي لَهُ: ona kendini gösterir"), who=("هِيَ", "سَفَنَّجَةٌ"), g=["naqis-verbs", "jumla-sifa"]),
 NO("لِأَزْعَرَ", "azar", R("maj", "fatha"), nt("لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»", "an adjective on the pattern أَفْعَل", "vasfiyet ve «أَفْعَل» vezni sebebiyle"), ON("تَبْرِي"), nt("نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: لِظَلِيمٍ أَزْعَرَ؛ الْأَزْعَرُ: الْقَلِيلُ الشَّعْرِ", "it describes a noun left out: «a sparse-plumed (male ostrich)»; الأَزْعَر: thin of hair", "mahzûf mevsûfun sıfatıdır: «tüyü seyrek (bir erkek devekuşu)»; الأَزْعَر: tüyü az olan", "hadhf-wa-taqdir"), pre="li"),
 NO("أَرْبَدِ", "arbad", mk("نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ — صُرِفَ لِضَرُورَةِ الشِّعْرِ وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ كَـ«أَزْعَرَ»، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ", "A second adjective of the omitted noun, in jarr by the kasra — it is fully inflected by poetic licence, though by rule a diptote like «أَزْعَرَ», and its tanwin is dropped for the rhyme", "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr — şiir zarureti sebebiyle munsarif kılınmıştır; aslında «أَزْعَرَ» gibi gayr-i munsariftir; tenvini kafiye için düşmüştür", "naat-sifa", "mamnu-min-sarf", "al-qafiya"), nt("الْأَرْبَدُ: الَّذِي لَوْنُهُ لَوْنُ الرَّمَادِ", "الأَرْبَد: ash-coloured", "الأَرْبَد: kül rengi")),
])
# ---- The camel: her pace, her pasture, her tail and thighs: verses 14–20 ---------------------------------------------
def NMH(case, sign="", nth=""):
    """an adjective of a noun the verse leaves out (al-Durra: «صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ»)"""
    s = SIGN(case, sign); n = {"": ("نَعْتٌ", "An adjective", "na'tı"), "2": ("نَعْتٌ ثَانٍ", "A second adjective", "ikinci na'tı"), "3": ("نَعْتٌ ثَالِثٌ", "A third adjective", "üçüncü na'tı")}[nth]
    return mk(n[0] + " لِلْمَوْصُوفِ الْمَحْذُوفِ " + s[0], n[1] + " of the noun left out, " + s[1], "Mahzûf mevsûfun " + n[2] + ", " + s[2], "naat-sifa", "hadhf-wa-taqdir", *s.tags)
def SRF(role_ar, role_en, role_tr, why_ar, why_en, why_tr, *tags):
    """a diptote in jarr at the rhyme: it takes the kasra — ṣurifa lil-ḍarūra — and drops the tanwin for the rhyme"""
    return mk(role_ar + " مَجْرُورٌ بِالْكَسْرَةِ — صُرِفَ لِضَرُورَةِ الشِّعْرِ وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ " + why_ar + "، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ",
              role_en + ", in jarr by the kasra — it is fully inflected by poetic licence, though by rule a diptote " + why_en + ", and its tanwin is dropped for the rhyme",
              role_tr + ", kesre ile mecrûr — şiir zarureti sebebiyle munsarif kılınmıştır; aslında " + why_tr + " gayr-i munsariftir; tenvini kafiye için düşmüştür", "mamnu-min-sarf", "al-qafiya", *tags)
def S_(m):
    """a note that stands as a sentence of its own (a figure)"""
    m.sent = True
    return m
AFAL = ("لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»", "(an adjective on the pattern أَفْعَل)", "vasfiyet ve «أَفْعَل» vezni sebebiyle")
NUN_IDF = nt("وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", "its nun is dropped for the annexation", "nûnu izâfet sebebiyle düşmüştür")
NUN_IWAD = nt("وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ", "the nun stands for the tanwin of the singular", "nûn, müfreddeki tenvinin bedelidir")
AS_TUBARI = nt("وَالْجُمْلَةُ يَجُوزُ فِيهَا مَا جَازَ فِي جُمْلَةِ «تُبَارِي» (الْبَيْتُ ١٤)", "the clause may be read every way the clause «تُبَارِي» (v. 14) may", "cümlede, «تُبَارِي» cümlesinde (14. beyit) câiz olan her vecih câizdir")
V(14, "She vies with noble, swift she-camels, and sets shank after shank — the hind foot following the fore — upon a beaten road.",
  "Soylu, hızlı develerle yarışır; ayağının incik kemiğini incik kemiği ardınca — arka ayağını ön ayağının izine — çiğnenmiş bir yolun üstüne basar.", [
 VB("تُبَارِي", "bara-vie", "mud-y", nt("وَالْجُمْلَةُ نَعْتٌ آخَرُ لِلنَّاقَةِ الْمَوْصُوفَةِ فِي الْبَيْتِ ١١ أَوْ حَالٌ مِنْهَا، وَيَجُوزُ أَنْ تَكُونَ مُسْتَأْنَفَةً (الدُّرَّةُ)", "the clause is a further adjective of the she-camel described from v. 11, or a hal of her; it may also open a new sentence (al-Durra)", "cümle, 11. beyitten beri vasfedilen devenin bir başka sıfatı ya da ondan hâldir; istînâfiyye olması da câizdir (Dürre)", "jumla-sifa"),
    nt("بَارَيْتُ الرَّجُلَ: فَعَلْتُ مِثْلَ فِعْلِهِ مُغَالِبًا لَهُ (الزَّوْزَنِيُّ)", "بَارَيْتُ الرَّجُلَ: I did as he did, trying to outdo him (al-Zawzanī)", "بَارَيْتُ الرَّجُلَ: ona üstün gelmeye çalışarak onun yaptığını yaptım (Zevzenî)"), who=("هِيَ", NAQA), g=["form-iii-verbs", "naqis-verbs"]),
 NO("عِتَاقًا", "atiq-noble", "maf", nt("وَهُوَ فِي الْأَصْلِ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: نُوقًا عِتَاقًا؛ الْعِتَاقُ: جَمْعُ عَتِيقٍ، وَهُوَ الْكَرِيمُ", "in origin it describes a noun left out: «noble she-camels»; العِتَاق is the plural of عَتِيق, the noble", "aslında mahzûf bir mevsûfun sıfatıdır: «soylu develer»; العِتَاق, «soylu» anlamındaki عَتِيق'in cem'idir", "hadhf-wa-taqdir", "jam-taksir")),
 NO("نَاجِيَاتٍ", "najiya", NMH("nasb", "kasra"), nt("النَّاجِيَاتُ: الْمُسْرِعَاتُ فِي السَّيْرِ، مِنْ نَجَا يَنْجُو: أَسْرَعَ", "النَّاجِيَات: swift in going, from نَجَا يَنْجُو, to go fast", "النَّاجِيَات: yürüyüşte hızlı olanlar; نَجَا يَنْجُو: hızlı gitti")),
 VB("وَأَتْبَعَتْ", "atbaa", "madi-f", JM("atf", "تُبَارِي"), nt("يَنْصِبُ مَفْعُولَيْنِ", "it takes two objects", "iki mef'ûl alır"), who=("هِيَ", NAQA), pre="wa", g=["form-iv-verbs", "mafulayn"], p=HEMI),
 NO("وَظِيفًا", "wazif", "maf1", nt("الْوَظِيفُ: مَا بَيْنَ الرُّسْغِ إِلَى الرُّكْبَةِ، أَيْ: وَظِيفُ رِجْلِهَا (الزَّوْزَنِيُّ)", "الوَظِيف: the shank, from the pastern to the knee — that is, the shank of her hind leg (al-Zawzanī)", "الوَظِيف: bilek ile diz arası, incik — yani arka ayağının inciği (Zevzenî)")),
 NO("وَظِيفًا", "wazif", "maf2", nt("أَيْ: وَظِيفَ يَدِهَا؛ يَقُولُ: تُتْبِعُ وَظِيفَ رِجْلِهَا وَظِيفَ يَدِهَا (الزَّوْزَنِيُّ)", "that is, the shank of her foreleg: she makes the hind shank follow the fore (al-Zawzanī)", "yani ön ayağının inciği: arka ayağının inciğini ön ayağınınkinin ardınca getirir (Zevzenî)")),
 NO("فَوْقَ", "fawqa", R("zm") + MUD, ZON("أَتْبَعَتْ")),
 NO("مَوْرٍ", "mawr", "mi", nt("الْمَوْرُ: الطَّرِيقُ", "المَوْر: the road", "المَوْر: yol")),
 NO("مُعَبَّدِ", "muabbad", NA("مَوْرٍ", "jarr"), nt("وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ؛ الْمُعَبَّدُ: الْمُذَلَّلُ بِالسُّلُوكِ وَالْوَطْءِ", "its deputy doer is a pronoun hidden in it; المُعَبَّد: made smooth by going and treading", "nâib-i fâili içinde gizli zamirdir; المُعَبَّد: gidilip çiğnenerek düzlenmiş", "ism-maful"), q=True),
])
V(15, "She has spent the spring on the two Quffs among she-camels whose milk has dried, grazing the gardens of a valley whose best parts the second rains have watered, soft of soil.",
  "Baharı, sütü çekilmiş develer arasında iki Kuff'ta geçirdi; ikinci yağmurların suladığı, en verimli yerleri olan, toprağı yumuşak bir vadinin bahçelerinde otlar.", [
 VB("تَرَبَّعَتِ", "tarabbaa-ant", "madi-fk", AS_TUBARI, nt("التَّرَبُّعُ: رَعْيُ الرَّبِيعِ وَالْإِقَامَةُ بِالْمَكَانِ زَمَنَهُ", "التَّرَبُّع: grazing the spring pasture and staying at a place through the spring", "التَّرَبُّع: bahar otunu otlamak ve bahar boyunca bir yerde kalmak"), who=("هِيَ", NAQA), g=["form-v-verbs"]),
 NO("الْقُفَّيْنِ", "quff", R("maf", "ya2"), NUN_IWAD, nt("الْقُفُّ: مَا غَلُظَ مِنَ الْأَرْضِ وَارْتَفَعَ وَلَمْ يَبْلُغْ أَنْ يَكُونَ جَبَلًا، وَأَرَادَ قُفَّيْنِ مَعْرُوفَيْنِ (الزَّوْزَنِيُّ)", "القُفّ: rough, raised ground short of a mountain; he means two known places of that name (al-Zawzanī)", "القُفّ: dağ olacak kadar yükselmeyen sert, yüksek arazi; bilinen iki yeri kastetmiştir (Zevzenî)")),
 HJ("فِي", "fi"),
 NO("الشَّوْلِ", "shawl", R("maj"), ON("تَرَبَّعَتِ"), nt("أَيْ: بَيْنَ نُوقٍ؛ الشَّوْلُ: النُّوقُ الَّتِي جَفَّتْ ضُرُوعُهَا وَقَلَّتْ أَلْبَانُهَا، الْوَاحِدَةُ شَائِلَةٌ", "that is, among she-camels; الشَّوْل: she-camels whose udders have dried and whose milk is little — the singular is شَائِلَة", "yani develer arasında; الشَّوْل: memeleri kurumuş, sütü azalmış develer; tekili شَائِلَة")),
 VB("تَرْتَعِي", "irtaa", "mud-y", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «تَرَبَّعَتِ» الْمُسْتَتِرِ، وَالرَّابِطُ الضَّمِيرُ", "the clause is a hal of the hidden doer of «تَرَبَّعَتِ», in the seat of nasb, tied by the pronoun", "cümle «تَرَبَّعَتِ»nin gizli fâilinden hâl olarak mahallen mansûb; râbıt zamirdir", "al-hal-jumla-wa-rabituha"), nt("الِارْتِعَاءُ: الرَّعْيُ", "الاِرْتِعَاء: grazing", "الاِرْتِعَاء: otlamak"), who=("هِيَ", NAQA), g=["form-viii-verbs", "naqis-verbs"], p=HEMI),
 NO("حَدَائِقَ", "hadiqa", R("maf") + MUD, nt("جَمْعُ حَدِيقَةٍ: كُلُّ رَوْضَةٍ ارْتَفَعَتْ أَطْرَافُهَا وَانْخَفَضَ وَسَطُهَا", "the plural of حَدِيقَة: a meadow whose edges rise and whose middle lies low", "«حَدِيقَة»nın cem'i: kenarları yüksek, ortası çukur her çayırlık", "jam-taksir")),
 NO("مَوْلِيِّ", "mawliyy", R("mi") + MUD, nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: حَدَائِقَ وَادٍ مَوْلِيِّ الْأَسِرَّةِ؛ الْمَوْلِيُّ: الَّذِي أَصَابَهُ الْوَلِيُّ، وَهُوَ الْمَطَرُ الثَّانِي مِنْ أَمْطَارِ السَّنَةِ", "it describes a noun left out — «the gardens of a valley whose best parts have had the second rain»; المَوْلِيّ: watered by الوَلِيّ, the second rain of the year", "mahzûf bir mevsûfun sıfatıdır: «en verimli yerleri ikinci yağmuru almış bir vadinin bahçeleri»; المَوْلِيّ: yılın ikinci yağmuru olan الوَلِيّ'yi almış", "ism-maful"),
    ZW("تَقْدِيرُهُ: وَحَدَائِقَ وَادٍ مَوْلِيِّ الْأَسِرَّةِ، فَحَذَفَ الْمَوْصُوفَ ثِقَةً بِدَلَالَةِ الصِّفَةِ عَلَيْهِ", "its full form is «and the gardens of a valley whose best parts have been rained on»: he left out the noun described, trusting the adjective to point to it", "takdiri: «en verimli yerleri yağmur almış bir vadinin bahçeleri»; sıfatın ona delâletine güvenerek mevsûfu hazfetmiştir"), g=["hadhf-wa-taqdir", "ijaz-al-hadhf"]),
 NO("الْأَسِرَّةِ", "sirr", "mi", nt("جَمْعُ سِرٍّ: سِرُّ الْوَادِي وَسَرَارَتُهُ خَيْرُهُ وَأَفْضَلُهُ كَلَأً، وَالْجَمْعُ الْأَسِرَّةُ وَالسِّرَارُ (الزَّوْزَنِيُّ)", "the plural of سِرّ: the سِرّ or سَرَارَة of a valley is its best and richest pasture (al-Zawzanī)", "«سِرّ»ın cem'i: vadinin سِرّ'ı ya da سَرَارَة'si, otlağı en iyi ve en verimli yeridir (Zevzenî)", "jam-taksir")),
 NO("أَغْيَدِ", "aghyad", SRF("نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ", "A second adjective of the noun left out", "Mahzûf mevsûfun ikinci na'tı", *AFAL, "naat-sifa"), nt("الْأَغْيَدُ: النَّاعِمُ، أَيْ: نَاعِمُ التُّرْبَةِ", "الأَغْيَد: soft — here, soft of soil", "الأَغْيَد: yumuşak — burada: toprağı yumuşak")),
])
V(16, "She turns back at the call of the herdsman, and with a tufted tail wards off the onsets of a dark-red, matted stallion.",
  "Çobanın çağrısına geri döner; püskül püskül kuyruğuyla koyu kızıl, tüyü keçeleşmiş bir aygırın saldırılarını savar.", [
 VB("تَرِيعُ", "raa-return", "mud", AS_TUBARI, nt("الرَّيْعُ: الرُّجُوعُ، رَاعَ يَرِيعُ", "الرَّيْع: going back — رَاعَ يَرِيعُ", "الرَّيْع: dönmek — رَاعَ يَرِيعُ"), who=("هِيَ", NAQA), g=["hollow-verbs"]),
 HJ("إِلَى", "ila"),
 NO("صَوْتِ", "sawt", R("maj") + MUD, ON("تَرِيعُ")),
 NO("الْمُهِيبِ", "muhib", "mi", nt("الْمُهِيبُ: الَّذِي يَدْعُو الْإِبِلَ، أَهَابَ بِنَاقَتِهِ: دَعَاهَا", "المُهِيب: the one who calls the camels — أَهَابَ بِنَاقَتِهِ, he called his she-camel", "المُهِيب: develeri çağıran — أَهَابَ بِنَاقَتِهِ: devesini çağırdı", "ism-fail")),
 VB("وَتَتَّقِي", "ittaqa", "mud-y", JM("atf", "تَرِيعُ"), nt("الِاتِّقَاءُ: الْحَجْزُ بَيْنَ شَيْئَيْنِ، اتَّقَى قِرْنَهُ بِتُرْسِهِ: جَعَلَهُ حَاجِزًا بَيْنَهُ وَبَيْنَهُ", "الاِتِّقَاء: putting a barrier between two things — اتَّقَى قِرْنَهُ بِتُرْسِهِ, he warded off his foe with his shield", "الاِتِّقَاء: iki şey arasına engel koymak — اتَّقَى قِرْنَهُ بِتُرْسِهِ: kalkanını hasmıyla kendi arasına koydu"), who=("هِيَ", NAQA), pre="wa", g=["form-viii-verbs", "naqis-verbs"], p=HEMI),
 NO("بِذِي", "dhu", R("maj", "five") + MUD, ON("تَتَّقِي"), ZW("أَرَادَ: بِذَنَبٍ ذِي خُصَلٍ، فَحَذَفَ الْمَوْصُوفَ اكْتِفَاءً بِدَلَالَةِ الصِّفَةِ عَلَيْهِ", "he means «with a tail that has tufts»: he left out the noun described, the adjective sufficing to point to it", "«püsküllü bir kuyrukla» demek istemiştir; sıfatın delâleti yettiği için mevsûfu hazfetmiştir"), pre="bi", g=["hadhf-wa-taqdir"]),
 NO("خُصَلٍ", "khusla-lock", "mi", nt("جَمْعُ خُصْلَةٍ: الْقِطْعَةُ مِنَ الشَّعَرِ", "the plural of خُصْلَة, a lock of hair", "«خُصْلَة»nın cem'i: saç ya da kıl tutamı", "jam-taksir")),
 NO("رَوْعَاتِ", "rawa-fright", R("maf", "kasra") + MUD, nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الرَّوْعَةُ: الْفَزْعَةُ، مِنَ الرَّوْعِ وَهُوَ الْإِفْزَاعُ", "the masdar annexed to its doer; الرَّوْعَة: a fright, a sudden onset, from الرَّوْع, alarming", "masdarın fâiline izâfeti; الرَّوْعَة: ürkütüş, ani saldırı; الرَّوْع: korkutmak", "masdar"),
    ZW("يُرِيدُ أَنَّهَا لَا تُمَكِّنُهُ مِنْ ضِرَابِهَا، وَإِذَا لَمْ تَلْقَحْ كَانَتْ مُجْتَمِعَةَ الْقُوَى وَافِرَةَ اللَّحْمِ قَوِيَّةً عَلَى السَّيْرِ", "he means that she will not let him mount her; and when she does not conceive she keeps her strength whole, full of flesh and strong for the road", "aygırın kendisine aşmasına izin vermediğini kasteder; gebe kalmayınca gücü derli toplu, eti dolgun, yürüyüşe dayanıklı olur"),
    S_(mk("فَهُوَ كِنَايَةٌ: أُرِيدَ بِاتِّقَاءِ الْفَحْلِ بِذَنَبِهَا لَازِمُهُ، وَهُوَ بَقَاؤُهَا غَيْرَ لَاقِحٍ قَوِيَّةً، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "So it is a kinaya: by her warding the stallion off with her tail is meant what follows from it — that she stays unmated and strong — as al-Zawzanī explains", "Bu bir kinâyedir: aygırı kuyruğuyla savmasından onun lâzımı — gebe kalmayıp güçlü kalması — kastedilmiştir; Zevzenî böyle açıklar", "kinaya", "aqsam-al-kinaya"))),
 NO("أَكْلَفَ", "aklaf", R("mi", "fatha"), nt("لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»", "an adjective on the pattern أَفْعَل", "vasfiyet ve «أَفْعَل» vezni sebebiyle"), nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: رَوْعَاتِ فَحْلٍ أَكْلَفَ (الزَّوْزَنِيُّ)؛ الْأَكْلَفُ: الَّذِي يَضْرِبُ إِلَى السَّوَادِ", "it describes a noun left out — «the onsets of a dark-red stallion» (al-Zawzanī); الأَكْلَف: verging on black", "mahzûf bir mevsûfun sıfatıdır: «koyu kızıl bir aygırın saldırıları» (Zevzenî); الأَكْلَف: siyaha çalan", "hadhf-wa-taqdir")),
 NO("مُلْبِدِ", "mulbid", NMH("jarr", nth="2"), nt("الْمُلْبِدُ: ذُو وَبَرٍ مُتَلَبِّدٍ مِنَ الْبَوْلِ وَغَيْرِهِ", "المُلْبِد: with hair matted by urine and the like", "المُلْبِد: tüyü idrar vb. ile keçeleşmiş", "ism-fail"), q=True),
])
V(17, "As though the two wings of a white vulture flanked its two sides — pierced into the tail-bone with an awl.",
  "Sanki ak bir akbabanın iki kanadı onun iki yanını kuşatmış, bir bızla kuyruk kemiğine saplanmıştır.", [
 PT("كَأَنَّ", "kaanna", KAANNA_T, JM("ist")),
 NO("جَنَاحَيْ", "janah", R("ism:كَأَنَّ", "ya2") + MUD, NUN_IDF,
    TSB("mm", ("شَعَرُ ذَنَبِهَا", "the hair of her tail", "kuyruğunun kılları"), ("جَنَاحَا نَسْرٍ أَبْيَضَ", "the two wings of a white vulture", "ak bir akbabanın iki kanadı"), "kaanna"), g=TSB_TAGS),
 NO("مَضْرَحِيٍّ", "madrahi", "mi", nt("الْمَضْرَحِيُّ: الْأَبْيَضُ مِنَ النُّسُورِ، وَقِيلَ: الْعَظِيمُ مِنْهَا", "المَضْرَحِيّ: a white vulture; also said: a great one", "المَضْرَحِيّ: ak akbaba; büyüğü olduğu da söylenmiştir", "ism-mansub")),
 VB("تَكَنَّفَا", "takannafa", "madi-2", nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «كَأَنَّ»، أَوْ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«جَنَاحَيْ مَضْرَحِيٍّ»؛ التَّكَنُّفُ: الْكَوْنُ فِي كَنَفِ الشَّيْءِ، أَيْ: نَاحِيَتِهِ", "the clause is the predicate of «كَأَنَّ», in the seat of raf' — or an adjective of «جَنَاحَيْ مَضْرَحِيٍّ», in the seat of jarr; التَّكَنُّف: being at the كَنَف, the side, of a thing", "cümle «كَأَنَّ»nin haberi olarak mahallen merfû — ya da «جَنَاحَيْ مَضْرَحِيٍّ»nin na'tı olarak mahallen mecrûr; التَّكَنُّف: bir şeyin كَنَف'ında, yanında olmak"), g=["form-v-verbs"], p=HEMI),
 NO("حِفَافَيْهِ", "hifaf", R("maf", "ya2"), NUN_IDF, nt("وَالضَّمِيرُ لِلْعَسِيبِ؛ الْحِفَافُ: الْجَانِبُ", "the pronoun is the tail-bone's; الحِفَاف: the side", "zamir kuyruk kemiğinedir; الحِفَاف: yan"), enc="هِ"),
 VB("شُكَّا", "shakka", "madi-2", nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ لِـ«كَأَنَّ»؛ الشَّكُّ: الْغَرْزُ", "the clause is a second predicate of «كَأَنَّ», in the seat of raf'; الشَّكّ: piercing, sticking in", "cümle «كَأَنَّ»nin ikinci haberi olarak mahallen merfû; الشَّكّ: saplamak"), maj=True, g=["doubled-verbs"]),
 HJ("فِي", "fi"),
 NO("الْعَسِيبِ", "asib", R("maj"), ON("شُكَّا"), nt("الْعَسِيبُ: عَظْمُ الذَّنَبِ", "العَسِيب: the bone of the tail", "العَسِيب: kuyruk kemiği")),
 NO("بِمِسْرَدِ", "misrad", R("maj"), ON("شُكَّا"), nt("الْمِسْرَدُ وَالْمِسْرَادُ: الْإِشْفَى", "المِسْرَد or المِسْرَاد: an awl", "المِسْرَد ya da المِسْرَاد: biz", "ism-al-ala"), pre="bi", q=True),
])
V(18, "Now she lashes it behind the rear rider, and now upon a dried-up udder like a worn waterskin — withered, its milk cut off.",
  "Kâh onu (kuyruğunu) arkadaki terkideki adamın arkasına vurur, kâh eskimiş bir su tulumu gibi pörsümüş, kurumuş, sütü kesilmiş memelerin üzerine.", [
 NO("فَطَوْرًا", "tawr", R("zz"), nt("مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ، أَيْ: فَطَوْرًا تَضْرِبُ بِهِ (الزَّوْزَنِيُّ)", "it hangs on a verb left out: «now she strikes with it» (al-Zawzanī)", "mahzûf bir fiile müteallik: «kâh onunla vurur» (Zevzenî)", "hadhf-wa-taqdir"), pre="fa-ist"),
 PJ("بِهِ", "بِ", "bi", "هِ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَحْذُوفِ", "the phrase hangs on the verb left out", "câr-mecrûr mahzûf fiile müteallik"), ref=("الذَّنَبِ", "the tail", "kuyruğa")),
 NO("خَلْفَ", "khalf", R("zm") + MUD, nt("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ الضَّمِيرِ فِي «بِهِ»، وَيَجُوزُ تَعْلِيقُهُ بِالْفِعْلِ الْمَحْذُوفِ", "it hangs on an omitted hal of the pronoun in «بِهِ»; it may also hang on the verb left out", "«بِهِ»deki zamirden mahzûf hâle müteallik; mahzûf fiile bağlanması da câizdir")),
 NO("الزَّمِيلِ", "zamil", "mi", nt("الزَّمِيلُ: الرَّدِيفُ", "الزَّمِيل: the one riding behind", "الزَّمِيل: terkideki")),
 NO("وَتَارَةً", "tara-time", AT("طَوْرًا", "nasb"), nt("فَهُوَ ظَرْفٌ مِثْلُهُ لِلْفِعْلِ الْمَحْذُوفِ", "so it is an adverb like it, of the verb left out", "o da onun gibi mahzûf fiilin zarfıdır"), pre="wa", p=HEMI),
 HJ("عَلَى", "ala"),
 NO("حَشَفٍ", "hashaf", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَحْذُوفِ؛ الْحَشَفُ: الْأَخْلَافُ الَّتِي جَفَّ لَبَنُهَا فَتَشَنَّجَتْ (وَهُوَ عِنْدَ التِّبْرِيزِيِّ «حَشِفٍ» بِكَسْرِ الشِّينِ)", "the phrase hangs on the verb left out; الحَشَف: teats whose milk has dried so that they have shrivelled (al-Tibrīzī has «حَشِفٍ», with a kasra on the shin)", "câr-mecrûr mahzûf fiile müteallik; الحَشَف: sütü kuruyup büzüşmüş memeler (Tebrîzî'de şîn'in kesresiyle «حَشِفٍ»)"),
    S_(mk("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَ الْحَشَفُ — وَهُوَ رَدِيءُ التَّمْرِ الْيَابِسُ — لِلْأَخْلَافِ الْيَابِسَةِ، وَالْجَامِعُ الْيُبْسُ وَالتَّشَنُّجُ (قَالَ الزَّوْزَنِيُّ: «وَهُوَ مُسْتَعَارٌ مِنْ حَشَفِ التَّمْرِ أَوْ مِنَ الْحَشِيفِ، وَهُوَ الثَّوْبُ الْخَلَقُ»)", "There is an explicit istiara: الحَشَف — dry, worthless dates — is borrowed for the dried teats, the common ground being dryness and shrivelling (al-Zawzanī: «it is borrowed from the حَشَف of dates, or from الحَشِيف, a worn garment»)", "İstiâre-i tasrîhiyye vardır: kuru, değersiz hurma demek olan الحَشَف kurumuş memeler için iğreti alınmıştır; câmi' kuruluk ve büzüşmedir (Zevzenî: «hurmanın حَشَف'ından ya da eski elbise demek olan الحَشِيف'ten müsteârdır»)", "istiara", "aqsam-al-istiara"))),
 NO("كَالشَّنِّ", "shann", R("maj"), ONH("naat", "حَشَفٍ"), nt("الشَّنُّ: الْقِرْبَةُ الْخَلَقُ", "الشَّنّ: a worn-out waterskin", "الشَّنّ: eskimiş su tulumu"),
    TSB("mm", ("الْحَشَفُ", "the dried teats", "kurumuş memeler"), ("الشَّنُّ", "a worn waterskin", "eskimiş su tulumu"), "ka", src="h"), pre="ka", g=TSB_TAGS),
 NO("ذَاوٍ", "dhawin", NA("حَشَفٍ", "jarr", "manh", "2"), nt("الذُّوِيُّ: الذُّبُولُ، ذَوَى يَذْوِي", "الذُّوِيّ: withering — ذَوَى يَذْوِي", "الذُّوِيّ: solmak — ذَوَى يَذْوِي", "ism-fail")),
 NO("مُجَدَّدِ", "mujaddad", NA("حَشَفٍ", "jarr", "", "3"), nt("الْمُجَدَّدُ: الَّذِي جُدَّ لَبَنُهُ، أَيْ: قُطِعَ", "المُجَدَّد: whose milk has been cut off", "المُجَدَّد: sütü kesilmiş", "ism-maful"), q=True),
])
V(19, "She has two thighs filled out with flesh — as though they were the two leaves of the door of a lofty, smooth-walled castle;",
  "Etle doldurulmuş iki butu vardır; sanki yüksek, düz duvarlı bir köşkün kapısının iki kanadıdır onlar;", [
 PJ("لَهَا", "لَ", "li", "هَا", ONH("khm", "فَخِذَانِ"), JM("ist"), ref=NAQA),
 NO("فَخِذَانِ", "fakhidh", R("mubm", "alif"), NUN_IWAD),
 VB("أُكْمِلَ", "akmala", "madi", JM("sifa", "فَخِذَانِ", "raf"), maj=True, g=["form-iv-verbs"]),
 NO("النَّحْضُ", "nahd", "naib", nt("النَّحْضُ: اللَّحْمُ", "النَّحْض: flesh", "النَّحْض: et")),
 PJ("فِيهِمَا", "فِي", "fi", "هِمَا", ON("أُكْمِلَ"), ref="فَخِذَانِ", p=HEMI),
 PT("كَأَنَّهُمَا", "kaanna", KAANNA_T + mk("، وَهُمَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; هُمَا is its noun, in the seat of nasb", "; هُمَا ismi, mahallen mansûb"), nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«فَخِذَانِ»", "the clause is a second adjective of «فَخِذَانِ», in the seat of raf'", "cümle «فَخِذَانِ»nin ikinci na'tı olarak mahallen merfû"), stem="كَأَنَّهُمَا"),
 NO("بَابَا", "bab", R("kh:كَأَنَّ", "alif") + MUD, NUN_IDF,
    TSB("mm", ("فَخِذَاهَا", "her two thighs", "iki butu"), ("مِصْرَاعَا بَابِ قَصْرٍ عَالٍ", "the two leaves of the door of a lofty castle", "yüksek bir köşkün kapısının iki kanadı"), "kaanna"), g=TSB_TAGS),
 NO("مُنِيفٍ", "munif", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: بَابَا قَصْرٍ مُنِيفٍ، فَحَذَفَ الْمَوْصُوفَ (الزَّوْزَنِيُّ)؛ الْمُنِيفُ: الْعَالِي", "it describes a noun left out — «the two leaves of a lofty castle's door» (al-Zawzanī); المُنِيف: high", "mahzûf bir mevsûfun sıfatıdır: «yüksek bir köşkün kapı kanatları» (Zevzenî); المُنِيف: yüksek", "hadhf-wa-taqdir")),
 NO("مُمَرَّدِ", "mumarrad", NMH("jarr", nth="2"), nt("الْمُمَرَّدُ: الْمُمَلَّسُ، وَالْمُطَوَّلُ أَيْضًا، وَقَدْ أُوِّلَ قَوْلُهُ تَعَالَى: {صَرْحٌ مُمَرَّدٌ مِنْ قَوَارِيرَ} [النَّمْل: ٤٤] بِهِمَا (الزَّوْزَنِيُّ)", "المُمَرَّد: made smooth — also, made long; the Qurʾānic «صَرْحٌ مُمَرَّدٌ مِنْ قَوَارِيرَ» (al-Naml 27:44) has been read both ways (al-Zawzanī)", "المُمَرَّد: düzlenmiş — uzatılmış anlamına da gelir; «صَرْحٌ مُمَرَّدٌ مِنْ قَوَارِيرَ» âyeti (Neml 27:44) her iki mânâyla tevil edilmiştir (Zevzenî)", "ism-maful"), q=True),
])
V(20, "and vertebrae cased close like a well's stones, their rib-ends like bows, and a neck's under-side joined fast to close-stacked vertebrae.",
  "kuyu taşları gibi sıkı dizilmiş omurları vardır, kaburga uçları yaylar gibidir; boynunun altı da üst üste dizilmiş omurlara sıkıca bitiştirilmiştir.", [
 NO("وَطَيُّ", "tayy-fold", AT("فَخِذَانِ", "raf") + MUD, nt("وَيَجُوزُ أَنْ يَكُونَ مُبْتَدَأً خَبَرُهُ مَحْذُوفٌ، أَيْ: وَلَهَا طَيُّ مَحَالٍ؛ وَهُوَ مِنْ إِضَافَةِ الصِّفَةِ إِلَى الْمَوْصُوفِ، أَيْ: مَحَالٌ مَطْوِيَّةٌ (التِّبْرِيزِيُّ: «أَيْ لَهَا مَحَالٌ مَطْوِيَّةٌ»)؛ الطَّيُّ فِي الْأَصْلِ: بِنَاءُ الْبِئْرِ بِالْحِجَارَةِ", "it may also be a mubtada whose predicate is left out — «and she has…»; the adjective is annexed to the noun it qualifies: «vertebrae close-cased» (al-Tibrīzī: «that is, she has vertebrae close-cased»); الطَّيّ is in origin the lining of a well with stones", "mahzûf haberli mübteda da olabilir: «onun … vardır»; sıfatın mevsûfuna izâfetidir: «sıkı örülmüş omurlar» (Tebrîzî: «yani sıkı örülmüş omurları vardır»); الطَّيّ aslında kuyuyu taşla örmektir"),
    TSB("bl", ("تَرَاصُفُ فَقَارِ النَّاقَةِ وَتَدَانِيهَا", "the close fit of the she-camel's vertebrae", "devenin omurlarının sıkı sıkı dizilişi"), ("طَيُّ الْبِئْرِ بِالْحِجَارَةِ", "the stone lining of a well", "kuyunun taşla örülüşü"), src="d"), pre="wa", g=TSB_TAGS),
 NO("مَحَالٍ", "mahala", "mi", nt("جَمْعُ مَحَالَةٍ: فَقَارُ الظَّهْرِ", "the plural of مَحَالَة: the vertebrae of the back", "«مَحَالَة»nın cem'i: sırt omurları", "jam-taksir")),
 NO("كَالْحَنِيِّ", "haniyya", R("maj"), ONH("khm", "خُلُوفُهُ"), nt("الْحَنِيُّ: الْقِسِيُّ، وَاحِدَتُهَا حَنِيَّةٌ؛ وَهُوَ فِي الطَّبْعَةِ بِفَتْحِ الْحَاءِ، وَالتِّبْرِيزِيُّ يَرْوِيهِ بِضَمِّهَا وَيَذْكُرُ كَسْرَهَا", "الحَنِيّ: bows, the singular حَنِيَّة; the edition has a fatha on the ha, al-Tibrīzī a damma, and he mentions a kasra", "الحَنِيّ: yaylar, tekili حَنِيَّة; baskıda hâ fethalıdır, Tebrîzî dammeyle rivayet eder ve kesreyi de zikreder"),
    TSB("mm", ("خُلُوفُ الْمَحَالِ، وَهِيَ أَطْرَافُ الْأَضْلَاعِ", "the rib-ends of the vertebrae", "omurlara bitişik kaburga uçları"), ("الْقِسِيُّ", "bows", "yaylar"), "ka", src="h"), pre="ka", g=TSB_TAGS),
 NO("خُلُوفُهُ", "khilf-rib", R("mubm"), nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«طَيُّ مَحَالٍ»؛ وَإِنْ عُلِّقَ «كَالْحَنِيِّ» بِمَحْذُوفٍ نَعْتٍ كَانَ «خُلُوفُهُ» فَاعِلًا بِهِ (الدُّرَّةُ)؛ الْخُلُوفُ: أَطْرَافُ الْأَضْلَاعِ، الْوَاحِدُ خِلْفٌ", "the clause is an adjective of «طَيُّ مَحَالٍ», in the seat of raf'; if «كَالْحَنِيِّ» is hung on an omitted adjective, «خُلُوفُهُ» is the doer of that phrase (al-Durra); الخُلُوف: the ends of the ribs, the singular خِلْف", "cümle «طَيُّ مَحَالٍ»in na'tı olarak mahallen merfû; «كَالْحَنِيِّ» mahzûf bir na'ta bağlanırsa «خُلُوفُهُ» onun fâili olur (Dürre); الخُلُوف: kaburgaların uçları, tekili خِلْف", "jam-taksir"), enc="هُ", p=HEMI),
 NO("وَأَجْرِنَةٌ", "jiran", AT("طَيُّ", "raf"), nt("وَيَجُوزُ فِيهِ مَا جَازَ فِي «طَيُّ»؛ جَمْعُ جِرَانٍ: بَاطِنُ الْعُنُقِ، وَلَيْسَ لَهَا إِلَّا جِرَانٌ وَاحِدٌ، فَجَمَعَهُ بِمَا حَوْلَهُ", "it may be read every way «طَيُّ» may; the plural of جِرَان, the under-side of the neck — she has but one, so he made it plural with what is around it", "«طَيُّ»de câiz olan her vecih bunda da câizdir; «جِرَان»ın cem'i: boynun alt yüzü — tek boynu olduğu hâlde etrafındakilerle birlikte cem' getirmiştir", "jam-taksir"), pre="wa"),
 VB("لُزَّتْ", "lazza", "madi-f", JM("sifa", "أَجْرِنَةٌ", "raf"), nt("لُزَّتْ: قُرِنَ بَعْضُهَا إِلَى بَعْضٍ فَانْضَمَّتْ وَاشْتَدَّتْ", "لُزَّتْ: they were joined one to another, so that they drew close and held fast", "لُزَّتْ: birbirine bitiştirilip kenetlendi ve sağlamlaştı"), who=("هِيَ", "أَجْرِنَةٌ"), maj=True, g=["doubled-verbs"]),
 NO("بِدَأْيٍ", "day", R("maj"), ON("لُزَّتْ"), nt("الدَّأْيُ: خَرَزُ الظَّهْرِ وَالْعُنُقِ، الْوَاحِدَةُ دَأْيَةٌ", "الدَّأْي: the vertebrae of the back and neck, the singular دَأْيَة", "الدَّأْي: sırt ve boyun omurları, tekili دَأْيَة"), pre="bi"),
 NO("مُنَضَّدِ", "munaddad", NA("دَأْيٍ", "jarr"), nt("أَيْ: مَوْضُوعٍ بَعْضُهُ فَوْقَ بَعْضٍ", "that is, set one upon another", "yani üst üste konmuş", "ism-maful"), q=True),
])
# ---- The camel's frame: verses 21–27 (vv. 21–22 from al-Tibrīzī p. 66 and al-Durra, the e-text of al-Zawzanī lacking them) ----
_VK["mud5a"] = ("فِعْلٌ مُضَارِعٌ%s مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ %s", "A present%s verb in raf' by keeping its nun — one of the five verbs; the alif of the dual is %s, in the seat of raf'", "Ef'âl-i hamseden olduğu için nûnun sübûtuyla merfû%s muzâri; tesniye elifi %s, mahallen merfû")
_VK["nk-mud"] = ("فِعْلٌ مُضَارِعٌ%s، مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الْخَفِيفَةِ", "A present%s verb, built on fatha because the light nun of emphasis is attached", "Hafif te'kîd nûnu bitiştiği için fetha üzere mebnî%s muzâri")
_ORD = {"2": ("ثَانٍ", "A second", "İkinci"), "3": ("ثَالِثٌ", "A third", "Üçüncü"), "4": ("رَابِعٌ", "A fourth", "Dördüncü")}
def KHN(nth, sign=""):
    """the nth predicate of an omitted mubtada («هِيَ»)"""
    s = SIGN("raf", sign); o = _ORD[nth]
    return mk("خَبَرٌ " + o[0] + " لِلْمُبْتَدَإِ الْمَحْذُوفِ " + s[0], o[1] + " predicate of the omitted mubtada, " + s[1], "Mahzûf mübtedanın " + low(o[2], True) + " haberi, " + s[2], "mubtada-khabar", "hadhf-wa-taqdir", *s.tags)
HATTA_T = mk("حَرْفُ غَايَةٍ وَجَرٍّ", "A particle of limit and jarr", "Gâye ve cer harfi", "huruf-jarr")
V(21, "As though two lairs under a lote-tree flanked her — so wide is the space between her elbows and her breast — and bent bows lay under a backbone made strong.",
  "Sanki bir sedir ağacının dibindeki iki in onu iki yandan kuşatmış — dirsekleriyle göğsü arası o kadar geniştir — ve güçlü kılınmış bir sırtın altında bükülmüş yaylar vardır.", [
 PT("كَأَنَّ", "kaanna", KAANNA_T, JM("ist")),
 NO("كِنَاسَيْ", "kinas", R("ism:كَأَنَّ", "ya2") + MUD, NUN_IDF, nt("الْكِنَاسُ: بَيْتٌ يَتَّخِذُهُ الْوَحْشُ فِي أَصْلِ شَجَرَةٍ؛ وَثَنَّاهُ لِأَنَّهُ يَسْتَكِنُّ بِالْغَدَاةِ فِي ظِلِّهَا وَبِالْعَشِيِّ فِي فَيْئِهَا (التِّبْرِيزِيُّ)", "الكِنَاس: a lair a wild beast makes at the foot of a tree; it is dual because he shelters in its shade in the morning and in its shadow in the evening (al-Tibrīzī)", "الكِنَاس: yabani hayvanın bir ağacın dibinde edindiği in; sabah ağacın gölgesinde, akşam da öbür yandaki gölgesinde barındığı için tesniye getirilmiştir (Tebrîzî)"),
    TSB("mm", ("الْهَوَاءُ الَّذِي بَيْنَ مِرْفَقَيْهَا وَزَوْرِهَا", "the open space between her elbows and her breast", "dirsekleriyle göğsü arasındaki boşluk"), ("كِنَاسَا ضَالَةٍ", "two lairs under a lote-tree", "bir sedir ağacının dibindeki iki in"), "kaanna", src="t"), g=TSB_TAGS),
 NO("ضَالَةٍ", "dala-tree", "mi", nt("الضَّالُ: السِّدْرُ الْبَرِّيُّ، الْوَاحِدَةُ ضَالَةٌ", "الضَّال: the wild lote-tree; the singular is ضَالَة", "الضَّال: yabani sedir ağacı; tekili ضَالَة")),
 VB("يَكْنُفَانِهَا", "kanafa", "mud5a", JM("kh", "كَأَنَّ"), nt("كَنَفْتُ الشَّيْءَ: صِرْتُ فِي نَاحِيَتِهِ، وَالْكَنَفُ: النَّاحِيَةُ", "كَنَفْتُ الشَّيْءَ: I came to be at its side; الكَنَف is the side", "كَنَفْتُ الشَّيْءَ: onun yanında oldum; الكَنَف: yan"), enc="هَا", g=["afal-khamsa"], p=HEMI),
 NO("وَأَطْرَ", "atr", AT("كِنَاسَيْ", "nasb") + MUD, nt("فَتَكُونُ «كَأَنَّ» مُقَدَّرَةً قَبْلَهُ؛ وَهُوَ مِنْ إِضَافَةِ الصِّفَةِ إِلَى الْمَوْصُوفِ، أَيْ: قِسِيٌّ مَأْطُورَةٌ (الدُّرَّةُ)؛ الْأَطْرُ: الْعَطْفُ وَالْحَنْيُ", "so «كَأَنَّ» is understood again before it; the description is annexed to what it describes — «bows that are bent» (al-Durra); الأَطْر: bending, curving", "önünde «كَأَنَّ» takdir edilir; sıfatın mevsûfuna izâfetidir: «bükülmüş yaylar» (Dürre); الأَطْر: eğmek, bükmek", "masdar"), pre="wa"),
 NO("قِسِيٍّ", "qaws", "mi", nt("جَمْعُ قَوْسٍ", "the plural of قَوْس, a bow", "«قَوْس»un cem'i: yay", "jam-taksir"),
    TSB("mm", ("أَضْلَاعُهَا", "her ribs", "kaburgaları"), ("الْقِسِيُّ الْمَأْطُورَةُ", "bent bows", "bükülmüş yaylar"), "kaanna", src="t"), g=TSB_TAGS),
 NO("تَحْتَ", "tahta", R("zm") + MUD, nt("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ لِـ«كَأَنَّ» الْمُقَدَّرَةِ", "it hangs on the omitted predicate of the understood «كَأَنَّ»", "takdir edilen «كَأَنَّ»nin mahzûf haberine müteallik")),
 NO("صُلْبٍ", "sulb-back", "mi"),
 NO("مُؤَيَّدِ", "muayyad", NA("صُلْبٍ", "jarr"), nt("الْمُؤَيَّدُ: الْمُقَوَّى، وَالْأَيْدُ: الْقُوَّةُ", "المُؤَيَّد: made strong; الأَيْد is strength", "المُؤَيَّد: güçlendirilmiş; الأَيْد: kuvvet", "ism-maful"), q=True),
])
V(22, "She has two elbows set wide from her sides, as though she went along with the two buckets of a sturdy water-drawer.",
  "Göğsünden ayrık iki dirseği vardır; sanki güçlü bir sucunun iki kovasıyla yürüyor.", [
 PJ("لَهَا", "لَ", "li", "هَا", ONH("khm", "مِرْفَقَانِ"), nt("وَالْجُمْلَةُ يَجُوزُ فِيهَا مَا جَازَ فِي «لَهَا فَخِذَانِ» (الْبَيْتُ ١٩)", "the clause may be read every way «لَهَا فَخِذَانِ» (v. 19) may", "cümlede, «لَهَا فَخِذَانِ» (19. beyit) cümlesinde câiz olan her vecih câizdir"), ref=NAQA),
 NO("مِرْفَقَانِ", "marfiq", R("mubm", "alif"), NUN_IWAD, nt("الْمِرْفَقُ وَالْمَرْفِقُ: مَوْصِلُ الذِّرَاعِ فِي الْعَضُدِ", "المِرْفَق or المَرْفِق: where the forearm joins the upper arm", "المِرْفَق ya da المَرْفِق: önkolun pazıya birleştiği yer, dirsek")),
 NO("أَفْتَلَانِ", "aftal", NA("مِرْفَقَانِ", "raf", "alif"), nt("الْأَفْتَلَانِ: الْمُتَبَايِنَانِ كَأَنَّمَا فُتِلَا عَنْ صَدْرِهَا (التِّبْرِيزِيُّ)؛ وَقِيلَ: الْأَفْتَلُ الْقَوِيُّ الشَّدِيدُ", "الأَفْتَلَان: set apart, as though twisted away from her breast (al-Tibrīzī); also said: الأَفْتَل is strong and sturdy", "الأَفْتَلَان: göğsünden sanki bükülerek ayrılmış iki dirsek (Tebrîzî); الأَفْتَل'in güçlü, sağlam demek olduğu da söylenmiştir")),
 PT("كَأَنَّمَا", "ka-annama", mk("كَأَنَّ حَرْفُ تَشْبِيهٍ، وَمَا كَافَّةٌ كَفَّتْهَا عَنِ الْعَمَلِ", "كَأَنَّ is the particle of likening, and مَا restrains it from governing", "كَأَنَّ teşbih harfi; مَا onu amelden alıkoyan kâffedir", "innama-kaffa"), nt("وَيُرْوَى «كَأَنَّهَا» فَتَعْمَلُ «كَأَنَّ» (الدُّرَّةُ)", "it is also transmitted «كَأَنَّهَا», with كَأَنَّ governing (al-Durra)", "«كَأَنَّهَا» diye de rivayet edilir; o zaman «كَأَنَّ» amel eder (Dürre)"),
    TSB("tm", ("بُعْدُ مِرْفَقَيْهَا عَنْ جَنْبَيْهَا", "her elbows standing off from her sides", "dirseklerinin iki yanından uzak duruşu"), ("سَقَّاءٌ قَوِيٌّ حَمَلَ دَلْوَيْنِ بِيَمِينِهِ وَيَسَارِهِ فَبَانَتْ يَدَاهُ عَنْ جَنْبَيْهِ", "a strong water-carrier with a bucket in his right hand and one in his left, so that his arms stand off from his sides", "sağ ve sol eliyle iki kova taşıyan, bu yüzden kolları iki yanından ayrık duran güçlü bir sucu"), "kaannama",
        ("التَّبَاعُدُ عَنِ الْجَنْبَيْنِ، صُورَةً مُنْتَزَعَةً مِنْ أُمُورٍ", "standing off from the sides — an image drawn from several things", "iki yandan uzak duruş — birkaç şeyden alınmış bir suret")), g=TSB_TAGS, p=HEMI),
 VB("تَمُرُّ", "marra", "mud", nt("وَالْجُمْلَةُ اسْتِئْنَافِيَّةٌ عَلَى رِوَايَةِ «كَأَنَّمَا»، وَخَبَرُ «كَأَنَّ» عَلَى رِوَايَةِ «كَأَنَّهَا»؛ وَالرِّوَايَةُ الْجَيِّدَةُ «تَمُرُّ» بِفَتْحِ التَّاءِ، وَيُرْوَى «تُمِرُّ»: تَفْتِلُ (التِّبْرِيزِيُّ)", "the clause opens a new sentence on the reading «كَأَنَّمَا», and is the predicate of «كَأَنَّ» on the reading «كَأَنَّهَا»; the good reading is «تَمُرُّ», with a fatha on the ta, and «تُمِرُّ», «twisting», is also transmitted (al-Tibrīzī)", "«كَأَنَّمَا» rivayetinde cümle istînâfiyye, «كَأَنَّهَا» rivayetinde «كَأَنَّ»nin haberidir; iyi rivayet tâ'nın fethasıyla «تَمُرُّ»dur, «تُمِرُّ» (büker) de rivayet edilir (Tebrîzî)"), who=("هِيَ", NAQA), g=["doubled-verbs"]),
 NO("بِسَلْمَيْ", "salm-bucket", R("maj", "ya2") + MUD, NUN_IDF, ON("تَمُرُّ"), nt("السَّلْمُ: الدَّلْوُ لَهَا عُرْوَةٌ وَاحِدَةٌ، نَحْوُ دَلْوِ السَّقَّائِينَ؛ وَقَالَ ابْنُ الْأَعْرَابِيِّ: أَرَادَ «تَمُرُّ سَلْمَيْ» فَزَادَ الْبَاءَ (التِّبْرِيزِيُّ)", "السَّلْم: a bucket with a single handle, like the water-carriers' buckets; Ibn al-Aʿrābī says he meant «تَمُرُّ سَلْمَيْ» and added the ba (al-Tibrīzī)", "السَّلْم: sucuların kovası gibi tek kulplu kova; İbnü'l-A'râbî «تَمُرُّ سَلْمَيْ» demek isteyip bâ'yı zâid getirdiğini söyler (Tebrîzî)"), pre="bi"),
 NO("دَالِجٍ", "dalij", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: رَجُلٍ دَالِجٍ (الدُّرَّةُ)؛ الدَّالِجُ: الَّذِي يَمْشِي بَيْنَ الْحَوْضِ وَالْبِئْرِ", "it describes a noun left out — «a man drawing water» (al-Durra); الدَّالِج: one who goes between the trough and the well", "mahzûf bir mevsûfun sıfatıdır: «su taşıyan bir adam» (Dürre); الدَّالِج: havuzla kuyu arasında gidip gelen", "hadhf-wa-taqdir", "ism-fail")),
 NO("مُتَشَدِّدِ", "mutashaddid", NMH("jarr", nth="2"), nt("وَفِيهِ وَفِي «دَالِجٍ» ضَمِيرٌ مُسْتَتِرٌ هُوَ فَاعِلُهُمَا يَعُودُ عَلَى الْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)؛ الْمُتَشَدِّدُ: الشَّدِيدُ الْقَوِيُّ", "it and «دَالِجٍ» each hold a hidden pronoun, their doer, returning to the noun left out (al-Durra); المُتَشَدِّد: strong, sturdy", "hem bunda hem «دَالِجٍ»de, mahzûf mevsûfa dönen ve fâilleri olan gizli bir zamir vardır (Dürre); المُتَشَدِّد: güçlü, sağlam", "ism-fail"), q=True),
])
V(23, "— like the bridge of a Greek whose owner swore it would be walled about until it was raised high with baked brick.",
  "— sahibi, tuğlayla yükseltilinceye kadar etrafının mutlaka çevrileceğine yemin ettiği bir Rum'un köprüsü gibi.", [
 NO("كَقَنْطَرَةِ", "qantara", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: هِيَ كَقَنْطَرَةِ الرُّومِيِّ، وَالْجُمْلَةُ اسْتِئْنَافِيَّةٌ؛ وَقِيلَ: مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مِرْفَقَانِ» (الدُّرَّةُ)", "the phrase hangs on the omitted predicate of an omitted mubtada — «she is like the Greek's bridge» — and the clause opens a new sentence; it is also said to hang on an omitted adjective of «مِرْفَقَانِ» (al-Durra)", "câr-mecrûr mahzûf mübtedanın mahzûf haberine müteallik: «o, Rum'un köprüsü gibidir»; cümle istînâfiyyedir; «مِرْفَقَانِ»in mahzûf na'tına müteallik olduğu da söylenmiştir (Dürre)", "hadhf-wa-taqdir"),
    TSB("mm", ("النَّاقَةُ فِي تَرَاصُفِ عِظَامِهَا وَتَدَاخُلِ أَعْضَائِهَا", "the she-camel, in the close fit of her bones and the knitting of her limbs", "kemiklerinin sıkı dizilişi ve uzuvlarının iç içe geçişiyle dişi deve"), ("قَنْطَرَةٌ تُبْنَى لِرَجُلٍ رُومِيٍّ", "a bridge built for a Greek", "bir Rum için yapılan köprü"), "ka"), pre="ka", g=TSB_TAGS),
 NO("الرُّومِيِّ", "rumi-greek", "mi", nt("أَيْ: الرَّجُلِ الرُّومِيِّ (الزَّوْزَنِيُّ)؛ وَقَصَدَ بِنَاءَ الرُّومِ لِإِحْكَامِهِ (التِّبْرِيزِيُّ)", "that is, the Greek man (al-Zawzanī); he chose the building of the Greeks for its firmness (al-Tibrīzī)", "yani Rum adam (Zevzenî); sağlamlığı için Rumların yapısını seçmiştir (Tebrîzî)", "ism-mansub")),
 VB("أَقْسَمَ", "aqsama", "madi", JM("ist"), nt("وَالْجُمْلَةُ الْقَسَمِيَّةُ وَجَوَابُهَا كَلَامٌ مُسْتَأْنَفٌ (الدُّرَّةُ)", "the oath with its answer is speech begun afresh (al-Durra)", "kasem cümlesi cevabıyla birlikte yeni başlayan bir sözdür (Dürre)"), g=["form-iv-verbs", "al-qasam-wal-shart-fil-kafiya"]),
 NO("رَبُّهَا", "rabb", "fail", nt("الرَّبُّ هُنَا: الْمَالِكُ صَاحِبُ الْقَنْطَرَةِ", "رَبّ here is the owner of the bridge", "رَبّ burada köprünün sahibidir"), enc="هَا", p=HEMI),
 VB("لَتُكْتَنَفَنْ", "iktanafa", "nk-mud", JM("qasam"), nt("أَيْ: وَاللّٰهِ لَتُكْتَنَفَنْ (الزَّوْزَنِيُّ)؛ الِاكْتِنَافُ: الْكَوْنُ فِي أَكْنَافِ الشَّيْءِ، أَيْ: لَيُحَاطَنَّ بِهَا", "that is, «by God, it shall be walled about» (al-Zawzanī); الاِكْتِنَاف: being at a thing's sides — «it shall be closed in on every side»", "yani «Allah'a andolsun ki etrafı çevrilecektir» (Zevzenî); الاِكْتِنَاف: bir şeyin yanlarında olmak — «etrafı mutlaka kuşatılacaktır»"), who=("هِيَ", "قَنْطَرَةِ"), maj=True, pre="la-qasam", g=["form-viii-verbs", "nun-tawkid", "al-qasam-wal-shart-fil-kafiya"]),
 PT("حَتَّى", "hatta", HATTA_T),
 VB("تُشَادَ", "shada-raise", "ns", nt("وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ» الْمُضْمَرَةِ وَالْفِعْلِ فِي مَحَلِّ جَرٍّ بِـ«حَتَّى»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُكْتَنَفَنْ»؛ الشَّيْدُ: الرَّفْعُ، وَالطَّلْيُ بِالشِّيدِ وَهُوَ الْجِصُّ", "the masdar made of the hidden أَنْ and the verb is in the seat of jarr by حَتَّى, and the phrase hangs on «تُكْتَنَفَنْ»; الشَّيْد: raising high, and plastering with الشِّيد, gypsum", "gizli «أَنْ» ile fiilden oluşan masdar «حَتَّى» ile mahallen mecrûrdur; câr-mecrûr «تُكْتَنَفَنْ»e müteallik; الشَّيْد: yükseltmek ve alçı demek olan الشِّيد ile sıvamak"), who=("هِيَ", "قَنْطَرَةِ"), by="hatta", maj=True, g=["hollow-verbs"]),
 NO("بِقَرْمَدِ", "qarmad", R("maj"), ON("تُشَادَ"), nt("الْقَرْمَدُ: الْآجُرُّ، وَقِيلَ: الصَّارُوجُ، الْوَاحِدَةُ قَرْمَدَةٌ", "القَرْمَد: baked brick; also said: lime-mortar — the singular قَرْمَدَة", "القَرْمَد: pişmiş tuğla; kireç harcı olduğu da söylenir — tekili قَرْمَدَة"), pre="bi", q=True),
])
V(24, "Reddish is the hair beneath her jaw, strong her back; long is the stride of her hind feet, and her forelegs swing freely.",
  "Çene altı kılları kızıla çalar, sırtı güçlendirilmiştir; arka ayağının adımı uzun, ön ayakları rahatça gidip gelir.", [
 NO("صُهَابِيَّةُ", "suhabiyya", R("khm") + MUD, nt("أَيْ: هِيَ صُهَابِيَّةُ الْعُثْنُونِ؛ وَيَجُوزُ جَرُّهُ نَعْتًا لِـ«عَوْجَاءَ» (الزَّوْزَنِيُّ)، وَنَصْبُهُ عَلَى الْمَدْحِ (الدُّرَّةُ)؛ الصُّهَابِيَّةُ: الَّتِي يَضْرِبُ لَوْنُهَا إِلَى الصُّهْبَةِ، وَهِيَ حُمْرَةٌ", "that is, «she is reddish of beard»; it may also be in jarr, describing «عَوْجَاءَ» (al-Zawzanī), or in nasb, in praise (al-Durra); الصُّهَابِيَّة: whose colour verges on الصُّهْبَة, a red", "yani «o, çene altı kılları kızıla çalandır»; «عَوْجَاءَ»nın na'tı olarak cerri (Zevzenî) ve medih için nasbı da câizdir (Dürre); الصُّهَابِيَّة: rengi kızıla (الصُّهْبَة) çalan", "hadhf-wa-taqdir", "ism-mansub")),
 NO("الْعُثْنُونِ", "uthnun", "mi", nt("مِنْ إِضَافَةِ الصِّفَةِ إِلَى فَاعِلِهَا؛ الْعُثْنُونُ: شَعَرَاتٌ تَحْتَ لَحْيِهَا الْأَسْفَلِ", "the description annexed to its doer; العُثْنُون: the hairs beneath her lower jaw", "sıfatın fâiline izâfeti; العُثْنُون: alt çenesinin altındaki kıllar", "idafa-lafziyya")),
 NO("مُوجَدَةُ", "mujad", KHN("2") + MUD, nt("الْمُوجَدَةُ: الْمُقَوَّاةُ، وَالْإِيجَادُ: التَّقْوِيَةُ، وَمِنْهُ: بَعِيرٌ أُجُدٌ (الزَّوْزَنِيُّ)؛ وَعِنْدَ التِّبْرِيزِيِّ «مُؤْجَدَةُ» بِالْهَمْزِ", "المُوجَدَة: made strong — الإِيجَاد is strengthening, as in بَعِيرٌ أُجُدٌ, a strongly built camel (al-Zawzanī); al-Tibrīzī writes «مُؤْجَدَةُ», with the hamza", "المُوجَدَة: güçlendirilmiş — الإِيجَاد güçlendirmektir; بَعِيرٌ أُجُدٌ (yapısı sağlam deve) de buradandır (Zevzenî); Tebrîzî hemzeyle «مُؤْجَدَةُ» yazar", "ism-maful")),
 NO("الْقَرَا", "qara-back", R("mi", "maq"), nt("وَهِيَ إِضَافَةُ اسْمِ الْمَفْعُولِ إِلَى نَائِبِ فَاعِلِهِ؛ الْقَرَا: الظَّهْرُ", "the passive participle annexed to its deputy doer; القَرَا: the back", "ism-i mef'ûlün nâib-i fâiline izâfeti; القَرَا: sırt", "idafa-lafziyya"), p=HEMI),
 NO("بَعِيدَةُ", "baid", KHN("3") + MUD),
 NO("وَخْدِ", "wakhd", R("mi") + MUD, nt("مِنْ إِضَافَةِ الصِّفَةِ إِلَى فَاعِلِهَا؛ الْوَخْدُ: الذَّمِيلُ، ضَرْبٌ مِنَ السَّيْرِ السَّرِيعِ، وَخَدَ يَخِدُ", "the description annexed to its doer; الوَخْد: a quick, ambling pace — وَخَدَ يَخِدُ", "sıfatın fâiline izâfeti; الوَخْد: hızlı bir yürüyüş türü — وَخَدَ يَخِدُ", "idafa-lafziyya")),
 NO("الرِّجْلِ", "rijl", "mi"),
 NO("مَوَّارَةُ", "mawwar", KHN("4") + MUD, nt("الْمَوَّارَةُ: مُبَالَغَةُ الْمَائِرَةِ؛ الْمَوْرُ: الذَّهَابُ وَالْمَجِيءُ", "المَوَّارَة: the intensive of المَائِرَة; المَوْر is going to and fro", "المَوَّارَة: المَائِرَة'nin mübalağası; المَوْر: gidip gelmek", "sighat-mubalagha")),
 NO("الْيَدِ", "yad", "mi", nt("مِنْ إِضَافَةِ صِيغَةِ الْمُبَالَغَةِ إِلَى فَاعِلِهَا", "the intensive annexed to its doer", "mübalağa sîgasının fâiline izâfeti", "idafa-lafziyya")),
])
V(25, "Her forelegs are twisted firm, as a rope is twisted away from the chest; and her upper arms are set slanting outward under a roof whose parts lean one upon another.",
  "Ön ayakları göğüsten dışa doğru bükülen ip gibi sıkıca bükülmüştür; pazıları da parçaları birbirine dayanmış bir çatının altında dışa doğru meyletmiştir.", [
 VB("أُمِرَّتْ", "amarra-twist", "madi-f", JM("ist"), nt("الْإِمْرَارُ: إِحْكَامُ الْفَتْلِ", "الإِمْرَار: twisting firm", "الإِمْرَار: sıkıca bükmek"), maj=True, g=["form-iv-verbs", "doubled-verbs"]),
 NO("يَدَاهَا", "yad", R("naib", "alif"), NUN_IDF, enc="هَا"),
 NO("فَتْلَ", "fatl", mk("مَنْصُوبٌ بِالْفَتْحَةِ عَلَى الْمَفْعُولِيَّةِ الْمُطْلَقَةِ، قَائِمٌ مَقَامَ صِفَةِ مَصْدَرٍ مَحْذُوفٍ، أَيْ: أُمِرَّتْ إِمْرَارًا مِثْلَ فَتْلِ شَزْرٍ، فَحُذِفَ الْمَصْدَرُ وَصِفَتُهُ وَأُقِيمَ مَا أُضِيفَتْ إِلَيْهِ مَقَامَهُمَا", "In nasb by the fatha as an absolute object, standing for the adjective of a masdar left out — «twisted with a twisting like the twist of a rope turned outward»: the masdar and its adjective are dropped and what the adjective was annexed to takes their place", "Mef'ûlün mutlak olarak fetha ile mansûb; mahzûf bir masdarın sıfatının yerini tutar: «göğüsten dışa bükülen ipin bükülüşü gibi bir bükülüşle bükülmüştür» — masdar ile sıfatı hazfedilmiş, sıfatın muzâfun ileyhi onların yerine konmuştur", "maful-mutlaq", "hadhf-wa-taqdir") + MUD, nt("وَقِيلَ: هُوَ نَفْسُهُ مَفْعُولٌ مُطْلَقٌ مُرَادِفٌ لِلْفِعْلِ (الدُّرَّةُ)", "it is also said to be itself an absolute object, a synonym of the verb (al-Durra)", "fiilin müradifi olarak bizzat mef'ûlün mutlak olduğu da söylenmiştir (Dürre)")),
 NO("شَزْرٍ", "shazr", "mi", nt("الْفَتْلُ الشَّزْرُ: مَا أُدِيرَ عَنِ الصَّدْرِ (الزَّوْزَنِيُّ)", "الفَتْل الشَّزْر: a twist turned away from the chest (al-Zawzanī)", "الفَتْل الشَّزْر: göğüsten dışa doğru çevrilen büküm (Zevzenî)")),
 VB("وَأُجْنِحَتْ", "ajnaha", "madi-f", JM("atf", "أُمِرَّتْ"), nt("الْإِجْنَاحُ: الْإِمَالَةُ، وَالْجُنُوحُ: الْمَيْلُ", "الإِجْنَاح: making to slant; الجُنُوح is slanting", "الإِجْنَاح: meylettirmek; الجُنُوح: meyletmek"), pre="wa", maj=True, g=["form-iv-verbs"], p=HEMI),
 PJ("لَهَا", "لَ", "li", "هَا", ON("أُجْنِحَتْ"), ref=NAQA),
 NO("عَضُدَاهَا", "adud", R("naib", "alif"), NUN_IDF, enc="هَا"),
 HJ("فِي", "fi"),
 NO("سَقِيفٍ", "saqif", R("maj"), ON("أُجْنِحَتْ"), nt("السَّقْفُ وَالسَّقِيفُ وَاحِدٌ (الزَّوْزَنِيُّ)؛ وَقِيلَ: السَّقِيفُ هُنَا زَوْرُهَا وَمَا فَوْقَهُ، وَأَصْلُهُ صَفَائِحُ مِنْ حِجَارَةٍ (التِّبْرِيزِيُّ)", "السَّقْف and السَّقِيف are one (al-Zawzanī); also said: السَّقِيف here is her breast and what is above it, its first sense being slabs of stone (al-Tibrīzī)", "السَّقْف ile السَّقِيف birdir (Zevzenî); burada السَّقِيف'in göğsü ve üstü olduğu da söylenmiştir; aslı taş levhalardır (Tebrîzî)"),
    HD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: سُمِّيَ مَا فَوْقَ عَضُدَيْهَا مِنْ جَنْبَيْهَا وَزَوْرِهَا سَقِيفًا لِشَبَهِهِ بِالسَّقْفِ فِي الصَّلَابَةِ وَالتَّرَاكُبِ، وَطُوِيَ ذِكْرُ الْمُشَبَّهِ (وَقَالَ الزَّوْزَنِيُّ: «تَحْتَ جَنْبَيْنِ كَأَنَّهُمَا سَقْفٌ»)", "there is an explicit istiara: what lies over her upper arms — her sides and breast — is called a roof for its likeness to one in hardness and the fitting of its parts, and the thing likened is not named (al-Zawzanī: «under two sides that are like a roof»)", "istiâre-i tasrîhiyye vardır: pazılarının üstündeki yanları ve göğsü, sertlik ve parçalarının birbirine geçmesi bakımından çatıya benzediği için «çatı» diye anılmış, müşebbeh zikredilmemiştir (Zevzenî: «çatı gibi iki yanın altında»)"), g=["istiara", "aqsam-al-istiara"]),
 NO("مُسَنَّدِ", "musannad", NA("سَقِيفٍ", "jarr"), nt("الْمُسَنَّدُ: الَّذِي أُسْنِدَ بَعْضُهُ إِلَى بَعْضٍ", "المُسَنَّد: whose parts are set leaning one on another", "المُسَنَّد: parçaları birbirine dayandırılmış", "ism-maful"), q=True),
])
V(26, "She swerves for very spirit, rushes on, big of head; and her shoulders are set high in a frame raised up and lifted.",
  "Coşkusundan yoldan sapan, son hızla atılan, iri başlı bir devedir; omuzları da yükseltilmiş, kaldırılmış bir yapı içinde yukarı dikilmiştir.", [
 NO("جَنُوحٌ", "januh", "khm", nt("أَيْ: هِيَ جَنُوحٌ؛ وَيَجُوزُ فِيهِ الْجَرُّ نَعْتًا عَلَى مَا مَرَّ (الزَّوْزَنِيُّ)؛ الْجَنُوحُ: مُبَالَغَةُ الْجَانِحَةِ، وَهِيَ الَّتِي تَمِيلُ فِي أَحَدِ الشِّقَّيْنِ لِنَشَاطِهَا فِي السَّيْرِ", "that is, «she is one that swerves»; it may also be in jarr, as an adjective, as before (al-Zawzanī); الجَنُوح: the intensive of الجَانِحَة, one that leans to one side for her spirit in going", "yani «o, çok meyledendir»; daha önce geçtiği gibi na't olarak cerri de câizdir (Zevzenî); الجَنُوح: الجَانِحَة'nin mübalağası — yürüyüşteki coşkusundan bir yana meyleden", "hadhf-wa-taqdir", "sighat-mubalagha")),
 NO("دِفَاقٌ", "difaq", KHN("2"), nt("الدِّفَاقُ: الْمُنْدَفِقَةُ فِي سَيْرِهَا، أَيِ: الْمُسْرِعَةُ غَايَةَ الْإِسْرَاعِ", "الدِّفَاق: one that pours herself along, going as fast as can be", "الدِّفَاق: yürüyüşünde boşanırcasına atılan, son derece hızlı giden")),
 NO("عَنْدَلٌ", "andal", KHN("3"), nt("الْعَنْدَلُ: الْعَظِيمَةُ الرَّأْسِ", "العَنْدَل: big of head", "العَنْدَل: iri başlı")),
 PT("ثُمَّ", "thumma", mk("حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ وَالتَّرَاخِيَ", "A conjunction of order with an interval", "Tertip ve terâhî bildiren atıf harfi", "atf-nasaq")),
 VB("أُفْرِعَتْ", "afraa", "madi-f", nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الْجُمْلَةِ الِاسْمِيَّةِ الْمُقَدَّرَةِ قَبْلَهَا؛ الْإِفْرَاعُ: التَّعْلِيَةُ، فَرَعْتُ الْجَبَلَ: عَلَوْتُهُ، وَأَفْرَعْتُهُ غَيْرِي: جَعَلْتُهُ يَعْلُوهُ", "the clause is conjoined to the nominal clause understood before it; الإِفْرَاع: raising high — فَرَعْتُ الْجَبَلَ, I climbed the mountain; أَفْرَعْتُهُ غَيْرِي, I made another climb it", "cümle önceki takdîrî isim cümlesine ma'tûftur; الإِفْرَاع: yükseltmek — فَرَعْتُ الْجَبَلَ: dağa çıktım; أَفْرَعْتُهُ غَيْرِي: başkasını ona çıkardım"), maj=True, g=["form-iv-verbs"], p=HEMI),
 PJ("لَهَا", "لَ", "li", "هَا", ON("أُفْرِعَتْ"), ref=NAQA),
 NO("كَتِفَاهَا", "katif", R("naib", "alif"), NUN_IDF, enc="هَا"),
 HJ("فِي", "fi"),
 NO("مُعَالًى", "muala", R("maj", "maqh"), ON("أُفْرِعَتْ"), ZW("يُرِيدُ: فِي خَلْقٍ مُعَالًى أَوْ ظَهْرٍ مُعَالًى، فَحَذَفَ الْمَوْصُوفَ اجْتِزَاءً بِدَلَالَةِ الصِّفَةِ عَلَيْهِ", "he means «in a frame (or a back) raised high»: he left out the noun described, content with the adjective's pointing to it", "«yükseltilmiş bir yapı (ya da sırt) içinde» demek ister; sıfatın delâletiyle yetinerek mevsûfu hazfetmiştir"), g=["ism-maful", "hadhf-wa-taqdir"]),
 NO("مُصَعَّدِ", "musaad", NMH("jarr", nth="2"), nt("الْمُعَالَاةُ وَالْإِعْلَاءُ وَالتَّعْلِيَةُ وَاحِدٌ، وَالتَّصْعِيدُ مِثْلُهَا (الزَّوْزَنِيُّ)", "المُعَالَاة, الإِعْلَاء and التَّعْلِيَة are one, and التَّصْعِيد is the same (al-Zawzanī)", "المُعَالَاة, الإِعْلَاء ve التَّعْلِيَة birdir; التَّصْعِيد de öyledir (Zevzenî)", "ism-maful"), q=True),
])
V(27, "The marks of the girth-strap on her vertebrae are like water-holes in a smooth rock on the back of rough, uneven ground.",
  "Kolan kayışının omurlarındaki izleri, engebeli sert bir arazinin sırtındaki düz bir kayada su birikmiş çukurlar gibidir.", [
 PT("كَأَنَّ", "kaanna", KAANNA_T, JM("ist")),
 NO("عُلُوبَ", "alb-mark", R("ism:كَأَنَّ") + MUD, nt("جَمْعُ عَلْبٍ: الْأَثَرُ، عَلَبْتُ الشَّيْءَ: أَثَّرْتُ فِيهِ", "the plural of عَلْب, a mark — عَلَبْتُ الشَّيْءَ, I left a mark on it", "«عَلْب»in cem'i: iz — عَلَبْتُ الشَّيْءَ: onda iz bıraktım", "jam-taksir")),
 NO("النِّسْعِ", "nis", "mi", nt("النِّسْعُ: سَيْرٌ كَهَيْئَةِ الْعِنَانِ تُشَدُّ بِهِ الْأَحْمَالُ", "النِّسْع: a strap shaped like a rein, with which loads are bound", "النِّسْع: yüklerin bağlandığı, dizgine benzer kayış")),
 HJ("فِي", "fi"),
 NO("دَأَيَاتِهَا", "dayat", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «عُلُوبَ النِّسْعِ»، وَالْعَامِلُ «كَأَنَّ» لِمَا فِيهَا مِنْ مَعْنَى الْفِعْلِ (الدُّرَّةُ)؛ الدَّأَيَاتُ: جَمْعُ دَأْيَةٍ، وَهِيَ الْفَقْرَةُ", "the phrase hangs on an omitted hal of «عُلُوبَ النِّسْعِ», governed by «كَأَنَّ» for the sense of a verb in it (al-Durra); الدَّأَيَات: the plural of دَأْيَة, a vertebra", "câr-mecrûr «عُلُوبَ النِّسْعِ»den mahzûf hâle müteallik; âmili, taşıdığı fiil mânâsı sebebiyle «كَأَنَّ»dir (Dürre); الدَّأَيَات: «دَأْيَة»nin cem'i, omur", "jam-muannath-salim"), enc="هَا", p=HEMI),
 NO("مَوَارِدُ", "mawrid", R("kh:كَأَنَّ"), nt("جَمْعُ مَوْرِدٍ: الْمَاءُ الَّذِي يُورَدُ", "the plural of مَوْرِد, water one comes down to", "«مَوْرِد»in cem'i: başına gelinen su", "jam-taksir"),
    TSB("mm", ("آثَارُ النِّسْعِ فِي ظَهْرِ النَّاقَةِ وَجَنْبَيْهَا", "the marks of the strap on her back and sides", "kayışın sırtındaki ve böğürlerindeki izleri"), ("نُقَرٌ فِيهَا مَاءٌ فِي صَخْرَةٍ مَلْسَاءَ", "hollows holding water in a smooth rock", "düz bir kayadaki su dolu çukurlar"), "kaanna"), g=TSB_TAGS),
 HJ("مِنْ", "min"),
 NO("خَلْقَاءَ", "khalqa", R("maj", "fatha"), nt("لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", "it ends in the long feminine alif", "elif-i memdûde ile müennes olduğu için"), ONH("naat", "مَوَارِدُ"),
    ZW("أَرَادَ: مِنْ صَخْرَةٍ خَلْقَاءَ، فَحَذَفَ الْمَوْصُوفَ؛ الْخَلْقَاءُ: الْمَلْسَاءُ … وَجَعَلَ جَنْبَهَا صُلْبًا كَالصَّخْرَةِ الْمَلْسَاءِ، وَجَعَلَ خَلْقَهَا فِي الشِّدَّةِ وَالصَّلَابَةِ كَالْأَرْضِ الْغَلِيظَةِ", "he means «from a smooth rock», leaving out the noun described; الخَلْقَاء: smooth … he makes her side hard like the smooth rock, and her frame, in toughness and hardness, like rough ground", "«düz bir kayadan» demek ister, mevsûfu hazfetmiştir; الخَلْقَاء: düz, kaygan … onun böğrünü düz kaya gibi sert, yapısını da sağlamlık ve sertlikte kaba arazi gibi kılmıştır"), pre=None, g=["ism-mamdud", "hadhf-wa-taqdir"]),
 HJ("فِي", "fi"),
 NO("ظَهْرِ", "zahr", R("maj") + MUD, ONH("naat", "خَلْقَاءَ")),
 NO("قَرْدَدِ", "qardad", "mi", nt("الْقَرْدَدُ: الْأَرْضُ الْغَلِيظَةُ الصُّلْبَةُ الَّتِي فِيهَا وِهَادٌ وَنِجَادٌ", "القَرْدَد: rough, hard ground with hollows and rises in it", "القَرْدَد: çukurları ve tümsekleri olan kaba, sert arazi"), q=True),
])
# ---- The neck, the skull, the cheek, the eyes: verses 28–33 -------------------------------------------------------------
AS_ATLA = nt("وَيَجُوزُ فِيهِ مَا جَازَ فِي «أَتْلَعُ» (الْبَيْتُ ٢٩)", "it may be read every way «أَتْلَعُ» (v. 29) may", "«أَتْلَعُ»de (29. beyit) câiz olan her vecih bunda da câizdir")
V(28, "Now they meet and now they part, as though they were white gussets in a slit shirt.",
  "Kâh birleşir, kâh ayrılırlar; sanki yırtmaçlı bir gömleğin beyaz ek parçalarıdır.", [
 VB("تَلَاقَى", "talaqa", "mud-a", nt("أَصْلُهُ «تَتَلَاقَى» فَحُذِفَتْ إِحْدَى التَّاءَيْنِ؛ وَالْفَاعِلُ يَعُودُ عَلَى «مَوَارِدُ»، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «مَوَارِدُ» أَوْ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لَهُ (الدُّرَّةُ)؛ تَلَاقَى: تَجْتَمِعُ", "its full form is «تَتَلَاقَى», one of the two ta's dropped; the doer returns to «مَوَارِدُ», and the clause is a hal of «مَوَارِدُ» in the seat of nasb, or a second adjective of it in the seat of raf' (al-Durra); تَلَاقَى: they come together", "aslı «تَتَلَاقَى»dır, iki tâ'dan biri düşmüştür; fâil «مَوَارِدُ»a döner; cümle «مَوَارِدُ»dan hâl olarak mahallen mansûb ya da onun ikinci na'tı olarak mahallen merfûdur (Dürre); تَلَاقَى: birleşirler"), g=["form-vi-verbs", "naqis-verbs"]),
 NO("وَأَحْيَانًا", "hin", R("zz"), ZON("تَبِينُ"), nt("جَمْعُ حِينٍ", "the plural of حِين, a time", "«حِين»in cem'i: vakit", "jam-taksir"), pre="wa"),
 VB("تَبِينُ", "lb-bana", "mud", JM("atf", "تَلَاقَى"), nt("تَبِينُ: تَفْتَرِقُ؛ يَعْنِي: هٰذِهِ الْمَوَارِدُ يَتَّصِلُ بَعْضُهَا بِبَعْضٍ أَحْيَانًا وَيَتَفَرَّقُ أَحْيَانًا (التِّبْرِيزِيُّ)", "تَبِينُ: they part; he means these water-hole marks now join one another and now stand apart (al-Tibrīzī)", "تَبِينُ: ayrılırlar; bu izlerin kâh birbirine bitiştiğini kâh ayrıldığını kasteder (Tebrîzî)"),
    HD("طِبَاقٌ بَيْنَ «تَلَاقَى» وَ«تَبِينُ»: الِاجْتِمَاعُ وَالِافْتِرَاقُ، وَبِهِمَا فَسَّرَهُمَا التِّبْرِيزِيُّ وَالدُّرَّةُ", "«تَلَاقَى» and «تَبِينُ» make a tibaq — coming together against parting — and so al-Tibrīzī and al-Durra explain them", "«تَلَاقَى» ile «تَبِينُ» arasında tıbâk vardır: birleşmek ile ayrılmak; Tebrîzî ve Dürre ikisini böyle açıklar"), who=("هِيَ", "مَوَارِدُ"), g=["hollow-verbs", "tibaq"]),
 PT("كَأَنَّهَا", "kaanna", KAANNA_T + mk("، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; هَا is its noun, in the seat of nasb", "; هَا ismi, mahallen mansûb"), nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «تَبِينُ» (الدُّرَّةُ)", "the clause is a hal of the doer of «تَبِينُ», in the seat of nasb (al-Durra)", "cümle «تَبِينُ»nun fâilinden hâl olarak mahallen mansûb (Dürre)"), stem="كَأَنَّهَا", p=HEMI),
 NO("بَنَائِقُ", "baniqa", R("kh:كَأَنَّ"), nt("جَمْعُ بَنِيقَةٍ: الرُّقْعَةُ تُزَادُ فِي الثَّوْبِ لِيَتَّسِعَ (الدُّرَّةُ)، وَهِيَ الدَّخَارِيصُ (التِّبْرِيزِيُّ)", "the plural of بَنِيقَة: a piece let into a garment to widen it (al-Durra) — a gusset (al-Tibrīzī: الدَّخَارِيص)", "«بَنِيقَة»nın cem'i: genişletmek için elbiseye eklenen parça (Dürre) — peş (Tebrîzî: الدَّخَارِيص)", "jam-taksir"),
    TSB("mm", ("آثَارُ النِّسْعِ الْمُتَّصِلَةُ وَالْمُتَفَرِّقَةُ", "the strap-marks, now joined and now apart", "kâh bitişen kâh ayrılan kayış izleri"), ("بَنَائِقُ بِيضٌ فِي قَمِيصٍ مُشَقَّقٍ", "white gussets in a slit shirt", "yırtmaçlı bir gömlekteki beyaz ek parçalar"), "kaanna", src="d"), g=TSB_TAGS),
 NO("غُرٌّ", "aghar", NA("بَنَائِقُ", "raf"), nt("الْغُرُّ: الْبِيضُ، جَمْعُ أَغَرَّ", "الغُرّ: white — the plural of أَغَرّ", "الغُرّ: beyazlar — «أَغَرّ»ın cem'i", "jam-taksir")),
 HJ("فِي", "fi"),
 NO("قَمِيصٍ", "qamis", R("maj"), ONH("naat2", "بَنَائِقُ")),
 NO("مُقَدَّدِ", "muqaddad", NA("قَمِيصٍ", "jarr"), nt("الْمُقَدَّدُ: الْمُشَقَّقُ", "المُقَدَّد: slit, cut into strips", "المُقَدَّد: yarılmış, yırtmaçlı", "ism-maful"), q=True),
])
V(29, "And a long neck, quick to rise: when she lifts it up, it is like the steering-oar of a river-boat going up the Tigris.",
  "Bir de uzun, çabuk kalkan bir boynu vardır; onu yukarı kaldırdığında Dicle'de akıntıya karşı giden bir teknenin dümeni gibidir.", [
 NO("وَأَتْلَعُ", "atla", R("mub"), nt("خَبَرُهُ مَحْذُوفٌ، أَيْ: وَلَهَا أَتْلَعُ، وَيَجُوزُ عَطْفُهُ عَلَى «مِرْفَقَانِ» (الْبَيْتُ ٢٢)؛ وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: عُنُقٌ أَتْلَعُ (الدُّرَّةُ)، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»؛ الْأَتْلَعُ: الطَّوِيلُ الْعُنُقِ", "its predicate is left out — «and she has a long (neck)» — and it may also be conjoined to «مِرْفَقَانِ» (v. 22); it describes a noun left out, «a long neck» (al-Durra), and takes no tanwin, being a diptote (an adjective on the pattern أَفْعَل); الأَتْلَع: long of neck", "haberi mahzûftur: «onun uzun (bir boynu) vardır»; «مِرْفَقَانِ»e (22. beyit) ma'tûf olması da câizdir; mahzûf bir mevsûfun sıfatıdır: «uzun bir boyun» (Dürre); vasfiyet ve «أَفْعَل» vezni sebebiyle gayr-i munsarif olduğundan tenvin almaz; الأَتْلَع: boynu uzun", "hadhf-wa-taqdir", "mamnu-min-sarf"), pre="wa"),
 NO("نَهَّاضٌ", "nahhad", NMH("raf", nth="2"), nt("النَّهَّاضُ: مُبَالَغَةُ النَّاهِضِ", "النَّهَّاض: the intensive of النَّاهِض, rising", "النَّهَّاض: النَّاهِض'in (kalkan) mübalağası", "sighat-mubalagha")),
 PT("إِذَا", "idha", mk("ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«نَهَّاضٌ» (الدُّرَّةُ)، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", "An adverb for time to come, built on sukun in the seat of nasb, hanging on «نَهَّاضٌ» (al-Durra), annexed to the clause after it", "Gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb; «نَهَّاضٌ»a müteallik (Dürre), kendinden sonraki cümleye muzâf", "maful-fih")),
 VB("صَعَّدَتْ", "saad-ii", "madi-f", JM("mudaf", "إِذَا"), nt("كَذَا فِي الطَّبْعَةِ بِالتَّشْدِيدِ، وَعِنْدَ التِّبْرِيزِيِّ «صَعَدَتْ»", "so the edition, with a shadda; al-Tibrīzī has «صَعَدَتْ»", "baskıda şeddeyle böyledir; Tebrîzî'de «صَعَدَتْ»"), who=("هِيَ", NAQA), g=["form-ii-verbs"]),
 PJ("بِهِ", "بِ", "bi", "هِ", ON("صَعَّدَتْ"), nt("وَالْبَاءُ لِلتَّعْدِيَةِ، أَيْ: بِالْعُنُقِ (الزَّوْزَنِيُّ)", "the ba makes the verb pass to its object — «it», the neck (al-Zawzanī)", "bâ ta'diye içindir; yani boynu (Zevzenî)"), ref=("«أَتْلَعُ»", "«أَتْلَعُ», the neck", "«أَتْلَعُ»a, yani boyna"), p=HEMI),
 NO("كَسُكَّانِ", "sukkan", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَالِثٍ لِلْمَوْصُوفِ الْمَحْذُوفِ، أَوْ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: هُوَ كَسُكَّانِ (الدُّرَّةُ)؛ السُّكَّانُ: ذَنَبُ السَّفِينَةِ", "the phrase hangs on an omitted third adjective of the noun left out, or on the omitted predicate of an omitted mubtada — «it is like the steering-oar» (al-Durra); السُّكَّان: the tail of a ship, its rudder", "câr-mecrûr mahzûf mevsûfun mahzûf üçüncü na'tına ya da mahzûf mübtedanın mahzûf haberine müteallik: «o, dümen gibidir» (Dürre); السُّكَّان: geminin kuyruğu, dümen"),
    TSB("mm", ("عُنُقُهَا إِذَا رَفَعَتْهُ", "her neck when she lifts it", "kaldırdığında boynu"), ("سُكَّانُ الْبُوصِيِّ الْمُصْعِدِ فِي دِجْلَةَ", "the rudder of a boat going up the Tigris", "Dicle'de akıntıya karşı giden teknenin dümeni"), "ka"),
    ZW("جَعَلَ عُنُقَهَا طَوِيلًا سَرِيعَ النُّهُوضِ، ثُمَّ شَبَّهَهُ فِي الِارْتِفَاعِ وَالِانْتِصَابِ بِسُكَّانِ السَّفِينَةِ فِي حَالِ جَرْيِهَا فِي الْمَاءِ", "he makes her neck long and quick to rise, then likens it, in its rising and standing upright, to a ship's rudder as she runs through the water", "boynunu uzun ve çabuk kalkan kılmış, sonra yükselip dikilmesinde onu suda akıp giden geminin dümenine benzetmiştir"), pre="ka", g=TSB_TAGS),
 NO("بُوصِيٍّ", "busi", "mi", nt("الْبُوصِيُّ: ضَرْبٌ مِنَ السُّفُنِ", "البُوصِيّ: a kind of boat", "البُوصِيّ: bir tür gemi")),
 NO("بِدِجْلَةَ", "dijla", R("maj", "fatha"), nt("لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", "a feminine proper name", "alemiyet ve te'nîs sebebiyle"), ON("مُصْعِدِ"), pre="bi", pos="propn"),
 NO("مُصْعِدِ", "musid", NA("بُوصِيٍّ", "jarr"), nt("أَيْ: سَفِينَةٍ فِي دِجْلَةَ تُصْعِدُ (الزَّوْزَنِيُّ)؛ الْمُصْعِدُ: الذَّاهِبُ صُعُدًا", "that is, a boat on the Tigris going upstream (al-Zawzanī); المُصْعِد: going up", "yani Dicle'de yukarı doğru giden bir gemi (Zevzenî); المُصْعِد: yukarı giden", "ism-fail"), q=True),
])
V(30, "And a skull like an anvil, as though where its parts meet it were joined fast to the edge of a file.",
  "Bir de örs gibi bir kafatası vardır; sanki birleşme yeri bir eğenin kenarına kenetlenmiştir.", [
 NO("وَجُمْجُمَةٌ", "jumjuma", AT("أَتْلَعُ", "raf"), AS_ATLA, nt("أَيْ: وَلَهَا جُمْجُمَةٌ (الزَّوْزَنِيُّ)؛ الْجُمْجُمَةُ: عَظْمُ الرَّأْسِ الْمُشْتَمِلُ عَلَى الدِّمَاغِ", "that is, «and she has a skull» (al-Zawzanī); الجُمْجُمَة: the bone of the head that holds the brain", "yani «onun bir kafatası vardır» (Zevzenî); الجُمْجُمَة: beyni kuşatan baş kemiği"), pre="wa"),
 NO("مِثْلُ", "mithl", NA("جُمْجُمَةٌ", "raf") + MUD,
    TSB("mm", ("جُمْجُمَتُهَا", "her skull", "kafatası"), ("الْعَلَاةُ", "an anvil", "örs"), "mithl"), ZW("يَقُولُ: وَلَهَا جُمْجُمَةٌ تُشْبِهُ الْعَلَاةَ فِي الصَّلَابَةِ", "he says: she has a skull like an anvil in hardness", "der ki: onun sertlikte örse benzeyen bir kafatası vardır"), g=TSB_TAGS),
 NO("الْعَلَاةِ", "alat", "mi", nt("الْعَلَاةُ: السَّنْدَانُ الَّذِي يَضْرِبُ عَلَيْهِ الْحَدَّادُ حَدِيدَهُ (الدُّرَّةُ)", "العَلَاة: the anvil on which the smith beats his iron (al-Durra)", "العَلَاة: demircinin demirini üstünde dövdüğü örs (Dürre)")),
 PT("كَأَنَّمَا", "ka-annama", mk("كَأَنَّ حَرْفُ تَشْبِيهٍ، وَمَا كَافَّةٌ كَفَّتْهَا عَنِ الْعَمَلِ", "كَأَنَّ is the particle of likening, and مَا restrains it from governing", "كَأَنَّ teşbih harfi; مَا onu amelden alıkoyan kâffedir", "innama-kaffa"), p=HEMI),
 VB("وَعَى", "waa", "madi-muq", nt("وَجُمْلَةُ «كَأَنَّمَا وَعَى…» فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«جُمْجُمَةٌ» (الدُّرَّةُ)؛ الْوَعْيُ: الْحِفْظُ وَالِاجْتِمَاعُ وَالِانْضِمَامُ، وَهُوَ فِي الْبَيْتِ عَلَى الْمَعْنَى الثَّانِي (الزَّوْزَنِيُّ)", "the clause «كَأَنَّمَا وَعَى…» is a second adjective of «جُمْجُمَةٌ», in the seat of raf' (al-Durra); الوَعْي: keeping, gathering, drawing together — in this verse the second sense (al-Zawzanī)", "«كَأَنَّمَا وَعَى…» cümlesi «جُمْجُمَةٌ»nin ikinci na'tı olarak mahallen merfû (Dürre); الوَعْي: korumak, toplanmak, kenetlenmek — beyitte ikinci anlamdadır (Zevzenî)"), g=["naqis-verbs"]),
 NO("الْمُلْتَقَى", "multaqa", R("fail", "maq"), nt("الْمُلْتَقَى: مَوْضِعُ الِالْتِقَاءِ، وَهُوَ طَرَفُ الْجُمْجُمَةِ لِأَنَّهُ يَلْتَقِي بِهِ فَرَاشُ الرَّأْسِ (الزَّوْزَنِيُّ)", "المُلْتَقَى: the place of meeting — the edge of the skull, where the plates of the head meet (al-Zawzanī)", "المُلْتَقَى: birleşme yeri — kafatasının kenarı, çünkü başın kemik levhaları orada birleşir (Zevzenî)", "ism-al-zaman-wal-makan")),
 PJ("مِنْهَا", "مِنْ", "min", "هَا", ONH("hal", "الْمُلْتَقَى"), ref="جُمْجُمَةٌ"),
 HJ("إِلَى", "ila"),
 NO("حَرْفِ", "harf", R("maj") + MUD, ON("وَعَى"), nt("الْحَرْفُ: النَّاحِيَةُ، وَالْجَمْعُ الْأَحْرُفُ وَالْحُرُوفُ", "الحَرْف: the edge, the side", "الحَرْف: kenar, yan")),
 NO("مِبْرَدِ", "mibrad", "mi", nt("اسْمُ آلَةٍ", "a noun of instrument", "ism-i âlet", "ism-al-ala"),
    HD("اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: ذَكَرَ الْمِبْرَدَ وَأَرَادَ حَدَّ عَظْمٍ يُشْبِهُهُ، وَطَوَى الْمُشَبَّهَ (قَالَ الزَّوْزَنِيُّ: «فَكَأَنَّمَا انْضَمَّ طَرَفُهَا إِلَى حَدِّ عَظْمٍ يُشْبِهُ الْمِبْرَدَ فِي الْحِدَّةِ وَالصَّلَابَةِ»)", "there is an explicit istiara: he names a file and means the edge of a bone that is like one, the thing likened left unsaid (al-Zawzanī: «as though its edge were joined to the edge of a bone like a file in sharpness and hardness»)", "istiâre-i tasrîhiyye vardır: eğeyi anıp ona benzeyen bir kemik kenarını kastetmiş, müşebbehi zikretmemiştir (Zevzenî: «sanki kenarı, keskinlik ve sertlikte eğeye benzeyen bir kemiğin kenarına kenetlenmiştir»)"), g=["istiara", "aqsam-al-istiara"], q=True),
])
V(31, "And a cheek like the parchment of a Syrian, and a lip like the tanned hide of a Yemeni — its cut not ragged.",
  "Bir de Şamlının kâğıdı gibi bir yanağı, Yemenlinin tabaklanmış sığır derisi gibi bir dudağı vardır; kesimi düzgündür, eğri büğrü değildir.", [
 NO("وَخَدٌّ", "khadd", AT("أَتْلَعُ", "raf"), AS_ATLA, pre="wa"),
 NO("كَقِرْطَاسِ", "qirtas", R("maj") + MUD, ONH("naat", "خَدٌّ"),
    TSB("mm", ("خَدُّهَا", "her cheek", "yanağı"), ("قِرْطَاسُ الشَّآمِي", "a Syrian's parchment", "Şamlının kâğıdı"), "ka"), ZW("شَبَّهَ خَدَّهَا فِي الِانْمِلَاسِ بِالْقِرْطَاسِ", "he likens her cheek in its smoothness to parchment", "yanağını düzlükte kâğıda benzetmiştir"), pre="ka", g=TSB_TAGS),
 NO("الشَّآمِي", "shaamin", R("mi", "man"), ZW("يَعْنِي: كَقِرْطَاسِ الرَّجُلِ الشَّآمِي، فَحَذَفَ الْمَوْصُوفَ اكْتِفَاءً بِدَلَالَةِ الصِّفَةِ", "he means «like the parchment of the Syrian man», leaving out the noun described, the adjective sufficing", "«Şamlı adamın kâğıdı gibi» demek ister; sıfatın delâletiyle yetinerek mevsûfu hazfetmiştir"), g=["ism-mansub", "hadhf-wa-taqdir"]),
 NO("وَمِشْفَرٌ", "mishfar", AT("خَدٌّ", "raf"), nt("الْمِشْفَرُ لِلْبَعِيرِ بِمَنْزِلَةِ الشَّفَةِ لِلْإِنْسَانِ", "the مِشْفَر of a camel is what the lip is to a man", "devenin مِشْفَر'ı insanın dudağı yerindedir"), pre="wa", p=HEMI),
 NO("كَسِبْتِ", "sibt-ant", R("maj") + MUD, ONH("naat", "مِشْفَرٌ"), nt("السِّبْتُ: جُلُودُ الْبَقَرِ الْمَدْبُوغَةُ بِالْقَرَظِ", "السِّبْت: ox-hides tanned with qaraẓ", "السِّبْت: karaz ile tabaklanmış sığır derileri"),
    TSB("mm", ("مِشْفَرُهَا", "her lip", "dudağı"), ("سِبْتُ الْيَمَانِي", "a Yemeni's tanned hide", "Yemenlinin tabaklanmış derisi"), "ka"), ZW("وَشَبَّهَ مِشْفَرَهَا بِالسِّبْتِ فِي اللِّينِ وَاسْتِقَامَةِ الْقَطْعِ", "and he likens her lip to tanned hide in its softness and the straightness of its cut", "dudağını da yumuşaklık ve kesimin düzgünlüğünde tabaklanmış deriye benzetmiştir"), pre="ka", g=TSB_TAGS),
 NO("الْيَمَانِي", "yamani", R("mi", "man"), nt("يُرِيدُ: كَسِبْتِ الرَّجُلِ الْيَمَانِي (الزَّوْزَنِيُّ)", "he means «like the tanned hide of the Yemeni man» (al-Zawzanī)", "«Yemenli adamın derisi gibi» demek ister (Zevzenî)", "ism-mansub", "hadhf-wa-taqdir")),
 NO("قِدُّهُ", "qidd", R("mub"), nt("وَالْجُمْلَةُ مِنَ الْمُبْتَدَإِ وَخَبَرِهِ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «سِبْتِ الْيَمَانِي»، وَالرَّابِطُ الضَّمِيرُ (الدُّرَّةُ)؛ وَهُوَ فِي الطَّبْعَةِ بِكَسْرِ الْقَافِ، وَعِنْدَ التِّبْرِيزِيِّ «قَدُّهُ» بِفَتْحِهَا", "the clause of mubtada and predicate is a hal of «سِبْتِ الْيَمَانِي», in the seat of nasb, tied by the pronoun (al-Durra); the edition has a kasra on the qaf, al-Tibrīzī «قَدُّهُ», with a fatha", "mübteda ile haberinden oluşan cümle «سِبْتِ الْيَمَانِي»den hâl olarak mahallen mansûb; râbıt zamirdir (Dürre); baskıda kâf kesrelidir, Tebrîzî'de fethayla «قَدُّهُ»"), enc="هُ"),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("يُحَرَّدِ", "harrada", "jz", JM("kh", "قِدُّهُ", "raf"), nt("التَّحْرِيدُ: اضْطِرَابُ الْقَطْعِ وَتَفَاوُتُهُ (الزَّوْزَنِيُّ)؛ وَرِوَايَةُ الدُّرَّةِ «يُجَرَّدِ»", "التَّحْرِيد: a cut that wavers and is uneven (al-Zawzanī); al-Durra's text has «يُجَرَّدِ»", "التَّحْرِيد: kesimin çarpık ve düzensiz olması (Zevzenî); Dürre'nin rivayeti «يُجَرَّدِ»dir"), who=("هُوَ", "قِدُّهُ"), by="lam", maj=True, q=True, g=["form-ii-verbs"]),
])
V(32, "And two eyes like two mirrors, sheltered in the two caves of brow-bones of rock, (clear as) the water of a rock-pool.",
  "Bir de iki ayna gibi iki gözü vardır; kaya gibi kaş kemiklerinin iki mağarasına, bir kaya çukurundaki suya sığınmışlardır.", [
 NO("وَعَيْنَانِ", "ayn-eye", AT("أَتْلَعُ", "raf", "alif"), NUN_IWAD, AS_ATLA, pre="wa"),
 NO("كَالْمَاوِيَّتَيْنِ", "mawiyya", R("maj", "ya2"), ONH("naat", "عَيْنَانِ"), NUN_IWAD, nt("الْمَاوِيَّةُ: الْمِرْآةُ", "المَاوِيَّة: a mirror", "المَاوِيَّة: ayna"),
    TSB("mm", ("عَيْنَاهَا", "her eyes", "gözleri"), ("مِرْآتَانِ", "two mirrors", "iki ayna"), "ka"), ZW("يَقُولُ: لَهَا عَيْنَانِ تُشْبِهَانِ مِرْآتَيْنِ فِي الصَّفَاءِ وَالنَّقَاءِ وَالْبَرِيقِ", "he says: she has two eyes like two mirrors in clearness, purity and gleam", "der ki: berraklık, temizlik ve parıltıda iki aynaya benzeyen iki gözü vardır"), pre="ka", g=TSB_TAGS),
 VB("اسْتَكَنَّتَا", "istakanna", "madi-2f", JM("sifa", "عَيْنَانِ", "raf"), nt("الِاسْتِكْنَانُ: طَلَبُ الْكِنِّ", "الاِسْتِكْنَان: seeking shelter", "الاِسْتِكْنَان: barınak aramak"), g=["form-x-verbs", "doubled-verbs"], p=HEMI),
 NO("بِكَهْفَيْ", "kahf", R("maj", "ya2") + MUD, NUN_IDF, ON("اسْتَكَنَّتَا"), nt("الْكَهْفُ: الْغَارُ", "الكَهْف: a cave", "الكَهْف: mağara"),
    S_(mk("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: ذَكَرَ الْكَهْفَيْنِ وَأَرَادَ غَارَيِ الْعَيْنَيْنِ لِغُؤُورِهِمَا، وَطَوَى الْمُشَبَّهَ (قَالَ الزَّوْزَنِيُّ: «وَشَبَّهَ عَيْنَيْهَا بِكَهْفَيْنِ فِي غُؤُورِهِمَا، وَحِجَاجَيْهَا بِالصَّخْرَةِ فِي الصَّلَابَةِ»)", "There is an explicit istiara: he names two caves and means the hollows of the eyes, for their depth, leaving the thing likened unsaid (al-Zawzanī: «he likens her eyes to two caves in their sunkenness, and her brow-bones to rock in hardness»)", "İstiâre-i tasrîhiyye vardır: iki mağarayı anıp derinliklerinden dolayı göz çukurlarını kastetmiş, müşebbehi zikretmemiştir (Zevzenî: «gözlerini derinlikte iki mağaraya, kaş kemiklerini sertlikte kayaya benzetmiştir»)", "istiara", "aqsam-al-istiara")), pre="bi"),
 NO("حِجَاجَيْ", "hijaj", R("mi", "ya2") + MUD, NUN_IDF, nt("الْحِجَاجُ: الْعُظَيْمُ الْمُشْرِفُ عَلَى الْعَيْنِ الَّذِي هُوَ مَنْبِتُ شَعَرِ الْحَاجِبِ", "الحِجَاج: the small bone over the eye on which the eyebrow grows", "الحِجَاج: kaşın bittiği, gözün üstündeki küçük kemik")),
 NO("صَخْرَةٍ", "sakhra", "mi", nt("أَيْ: حِجَاجَيْنِ مِنْ صَخْرَةٍ، كَقَوْلِهِمْ: بَابُ حَدِيدٍ، أَيْ: بَابٌ مِنْ حَدِيدٍ (الزَّوْزَنِيُّ)", "that is, two brow-bones of rock, as one says «a door of iron» (al-Zawzanī)", "yani kayadan iki kaş kemiği; «demir kapı», yani demirden kapı demeleri gibi (Zevzenî)")),
 NO("قَلْتِ", "qalt", BD("صَخْرَةٍ", "jarr") + MUD, nt("وَقِيلَ: نَعْتٌ لَهَا (الدُّرَّةُ)؛ الْقَلْتُ: النُّقْرَةُ فِي الْجَبَلِ يَسْتَنْقِعُ فِيهَا الْمَاءُ", "it is also said to be her adjective (al-Durra); القَلْت: a hollow in the mountain where water stands", "onun na'tı olduğu da söylenmiştir (Dürre); القَلْت: dağda suyun biriktiği çukur")),
 NO("مَوْرِدِ", "mawrid", "mi", nt("الْمَوْرِدُ: الْمَاءُ هُنَا (الزَّوْزَنِيُّ)؛ وَهُوَ مِنْ عَكْسِ الْإِضَافَةِ، إِذِ الْأَصْلُ: مَوْرِدُ قَلْتٍ (الدُّرَّةُ)", "المَوْرِد here is the water (al-Zawzanī); the annexation is turned about — the order would be «the water of a rock-pool» (al-Durra)", "المَوْرِد burada sudur (Zevzenî); izâfet tersine çevrilmiştir, aslı «kaya çukurunun suyu»dur (Dürre)"), q=True),
])
V(33, "They cast out every mote, so that you see them like the kohl-dark eyes of a startled wild cow, the mother of a calf.",
  "Her çöpü dışarı atarlar; onları, ürkütülmüş, yavrulu bir yaban sığırının sürmeli gözleri gibi görürsün.", [
 NO("طَحُورَانِ", "tahur", NA("عَيْنَانِ", "raf", "alif"), NUN_IWAD, nt("وَيَجُوزُ أَنْ يَكُونَ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ عَلَى الْقَطْعِ، أَيْ: هُمَا طَحُورَانِ (الدُّرَّةُ)؛ وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ فِيهِ؛ الطَّحُورُ: مُبَالَغَةُ الطَّاحِرِ، وَالطَّحْرُ وَالطَّرْحُ وَالدَّحْرُ وَاحِدٌ", "it may also be the predicate of an omitted mubtada, cut off — «they are two that cast out» (al-Durra); its doer is hidden in it; الطَّحُور: the intensive of الطَّاحِر — الطَّحْر, الطَّرْح and الدَّحْر are one", "kat' üzere mahzûf mübtedanın haberi de olabilir: «onlar çok atandır» (Dürre); fâili içinde gizlidir; الطَّحُور: الطَّاحِر'in mübalağası — الطَّحْر, الطَّرْح ve الدَّحْر birdir", "sighat-mubalagha")),
 NO("عُوَّارَ", "uwwar", R("maf") + MUD, nt("لِـ«طَحُورَانِ»، لِأَنَّ صِيغَةَ الْمُبَالَغَةِ تَعْمَلُ عَمَلَ فِعْلِهَا", "of «طَحُورَانِ», since an intensive form governs as its verb does", "«طَحُورَانِ»ın mef'ûlüdür; mübalağa sîgası fiilinin amelini işler", "shurut-amal-ism-al-fail")),
 NO("الْقَذَى", "qadha", R("mi", "maq"), nt("الْعُوَّارُ وَالْقَذَى وَاحِدٌ (الزَّوْزَنِيُّ)", "العُوَّار and القَذَى are one (al-Zawzanī)", "العُوَّار ile القَذَى birdir (Zevzenî)")),
 VB("فَتَرَاهُمَا", "raa", "mud-a", nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is conjoined to what precedes", "cümle öncesine ma'tûftur"), who="أَنْتَ", pre="fa-sabab", enc="هُمَا", g=["naqis-verbs"], p=HEMI),
 NO("كَمَكْحُولَتَيْ", "makhula", R("maj", "ya2") + MUD, NUN_IDF, ON("تَرَاهُمَا"), nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، وَأَصْلُ الْكَلَامِ: كَعَيْنَيْنِ مَكْحُولَتَيْنِ لِبَقَرَةٍ وَحْشِيَّةٍ مَذْعُورَةٍ (الدُّرَّةُ)؛ أَرَادَ بِالْمَكْحُولَتَيْنِ الْعَيْنَيْنِ، لَا تُكْحَلُ بَقَرُ الْوَحْشِ وَلٰكِنَّ الْعَيْنَ مَحَلُّ الْكُحْلِ عَلَى الْإِطْلَاقِ (الزَّوْزَنِيُّ)", "it describes a noun left out — in full, «like the two kohl-dark eyes of a startled wild cow» (al-Durra); by the two kohl-dark ones he means the eyes: wild cows are not painted with kohl, but the eye is the place of kohl in general (al-Zawzanī)", "mahzûf bir mevsûfun sıfatıdır; sözün aslı: «ürkütülmüş bir yaban sığırının sürmeli iki gözü gibi» (Dürre); «sürmeli iki»den gözleri kastetmiştir; yaban sığırına sürme çekilmez, ama göz genel olarak sürmenin yeridir (Zevzenî)", "hadhf-wa-taqdir", "ism-maful"),
    TSB("mm", ("عَيْنَا النَّاقَةِ", "the she-camel's eyes", "devenin gözleri"), ("عَيْنَا بَقَرَةٍ وَحْشِيَّةٍ لَهَا وَلَدٌ قَدْ أَفْزَعَهَا صَائِدٌ", "the eyes of a wild cow with a calf whom a hunter has startled", "bir avcının ürküttüğü yavrulu yaban sığırının gözleri"), "ka"), pre="ka", g=TSB_TAGS),
 NO("مَذْعُورَةٍ", "madhur", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: بَقَرَةٍ وَحْشِيَّةٍ مَذْعُورَةٍ، وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ؛ الذُّعْرُ: الْإِخَافَةُ", "it describes a noun left out — «a startled wild cow» — and its deputy doer is hidden in it; الذُّعْر: frightening", "mahzûf bir mevsûfun sıfatıdır: «ürkütülmüş bir yaban sığırı»; nâib-i fâili içinde gizlidir; الذُّعْر: korkutmak", "hadhf-wa-taqdir", "ism-maful")),
 NO("أُمِّ", "umm", NMH("jarr", nth="2") + MUD),
 NO("فَرْقَدِ", "farqad", "mi", nt("الْفَرْقَدُ: وَلَدُ الْبَقَرَةِ الْوَحْشِيَّةِ، وَالْجَمْعُ الْفَرَاقِدُ", "الفَرْقَد: the calf of a wild cow", "الفَرْقَد: yaban sığırının yavrusu"), q=True),
])
# ---- The ears, the heart, the nose; her pace at his will: verses 34–39 --------------------------------------------------
_NTH = {"": ("نَعْتٌ", "An adjective", "na'tı"), "2": ("نَعْتٌ ثَانٍ", "A second adjective", "ikinci na'tı"), "3": ("نَعْتٌ ثَالِثٌ", "A third adjective", "üçüncü na'tı"),
        "4": ("نَعْتٌ رَابِعٌ", "A fourth adjective", "dördüncü na'tı"), "5": ("نَعْتٌ خَامِسٌ", "A fifth adjective", "beşinci na'tı")}
def NMH(case, sign="", nth=""):
    """an adjective of a noun the verse leaves out (al-Durra: «صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ»)"""
    s = SIGN(case, sign); n = _NTH[nth]
    return mk(n[0] + " لِلْمَوْصُوفِ الْمَحْذُوفِ " + s[0], n[1] + " of the noun left out, " + s[1], "Mahzûf mevsûfun " + n[2] + ", " + s[2], "naat-sifa", "hadhf-wa-taqdir", *s.tags)
IN_COND = nt("وَهُوَ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "it is in the seat of jazm as the condition's verb", "şart fiili olarak mahallen meczûmdur", "al-majzum-wal-shart-wal-jaza")
IN_JAWAB = nt("وَهُوَ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالْجُمْلَةُ لَا مَحَلَّ لَهَا لِأَنَّهَا جَوَابُ شَرْطٍ غَيْرُ مُقْتَرِنٍ بِالْفَاءِ", "it is in the seat of jazm as the answer of the condition, and the clause has no seat, being an answer without the fa", "şartın cevabı olarak mahallen meczûmdur; fâ almamış şart cevabı olduğu için cümlenin mahalli yoktur", "al-majzum-wal-shart-wal-jaza")
V(34, "And two ears true in the wary listening of the night journey, to a faint stir or to a loud cry.",
  "Bir de gece yolculuğunda kulak kabartmakta yanılmayan iki kulağı vardır: gizli bir kıpırtıya da, yüksek bir sese de.", [
 NO("وَصَادِقَتَا", "sadiq", AT("أَتْلَعُ", "raf", "alif") + MUD, NUN_IDF, AS_ATLA, nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: وَلَهَا أُذُنَانِ صَادِقَتَا سَمْعِ التَّوَجُّسِ (الزَّوْزَنِيُّ)", "it describes a noun left out — «and she has two ears true in…» (al-Zawzanī)", "mahzûf bir mevsûfun sıfatıdır: «onun … doğru duyan iki kulağı vardır» (Zevzenî)", "hadhf-wa-taqdir"), pre="wa"),
 NO("سَمْعِ", "sam", R("mi") + MUD, nt("مِنْ إِضَافَةِ الصِّفَةِ إِلَى فَاعِلِهَا", "the description annexed to its doer", "sıfatın fâiline izâfeti", "idafa-lafziyya")),
 NO("التَّوَجُّسِ", "tawajjus", "mi", nt("التَّوَجُّسُ: التَّسَمُّعُ", "التَّوَجُّس: listening warily", "التَّوَجُّس: kulak kabartmak", "masdar")),
 NO("لِلسُّرَى", "sura-ant", R("maj", "maq"), nt("وَاللَّامُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَمْعِ» (الدُّرَّةُ)؛ السُّرَى: سَيْرُ اللَّيْلِ", "the lam means «in», and the phrase hangs on «سَمْعِ» (al-Durra); السُّرَى: travelling by night", "lâm «fî» anlamındadır; câr-mecrûr «سَمْعِ»e müteallik (Dürre); السُّرَى: gece yürüyüşü"), pre="li", p=HEMI),
 NO("لِهَجْسٍ", "hajs", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَمْعِ» أَيْضًا لِأَنَّهُ مَصْدَرٌ؛ الْهَجْسُ: الْحَرَكَةُ", "the phrase too hangs on «سَمْعِ», which is a masdar; الهَجْس: a stir, a movement", "câr-mecrûr da masdar olan «سَمْعِ»e müteallik; الهَجْس: kıpırtı"), pre="li"),
 NO("خَفِيٍّ", "khafi", NA("هَجْسٍ", "jarr")),
 PT("أَوْ", "aw", AW_T),
 NO("لِصَوْتٍ", "sawt", AT("لِهَجْسٍ", "jarr"), nt("فَهُوَ مُتَعَلِّقٌ بِـ«سَمْعِ» مِثْلَهُ", "so it too hangs on «سَمْعِ»", "o da onun gibi «سَمْعِ»e müteallik"), pre="li"),
 NO("مُنَدِّدِ", "munaddid", NA("صَوْتٍ", "jarr"), nt("التَّنْدِيدُ: رَفْعُ الصَّوْتِ؛ وَيُرْوَى «لِصَوْتِ مُنَدِّدِ» بِالْإِضَافَةِ، وَعِنْدَ التِّبْرِيزِيِّ «مُنَدَّدِ» بِفَتْحِ الدَّالِ نَعْتًا (الدُّرَّةُ)", "التَّنْدِيد: raising the voice; it is also transmitted «لِصَوْتِ مُنَدِّدِ», annexed, and al-Tibrīzī has «مُنَدَّدِ», with a fatha on the dal, as an adjective (al-Durra)", "التَّنْدِيد: sesi yükseltmek; izâfetle «لِصَوْتِ مُنَدِّدِ» diye de rivayet edilir; Tebrîzî'de dâl'ın fethasıyla na't olarak «مُنَدَّدِ» (Dürre)", "ism-fail"),
    HD("طِبَاقٌ بَيْنَ «خَفِيٍّ» وَ«مُنَدِّدِ»: الْخَفِيُّ وَالْمَرْفُوعُ (قَالَ الزَّوْزَنِيُّ: «لَا يَخْفَى عَلَيْهِمَا السِّرُّ الْخَفِيُّ وَلَا الصَّوْتُ الرَّفِيعُ»)", "«خَفِيٍّ» and «مُنَدِّدِ» make a tibaq — the faint against the loud (al-Zawzanī: «neither the faint secret nor the high voice escapes them»)", "«خَفِيٍّ» ile «مُنَدِّدِ» arasında tıbâk vardır: gizli ile yüksek (Zevzenî: «ne gizli fısıltı ne yüksek ses onlardan kaçar»)"), q=True, g=["tibaq"]),
])
V(35, "Sharp-pointed, in them you know her noble breed — like the ears of a wild ox alone at Ḥawmal.",
  "Mızrak ucu gibi sivridirler, soyluluğunu onlarda tanırsın; Havmel'de tek başına kalmış bir yaban öküzünün kulakları gibidir.", [
 NO("مُؤَلَّلَتَانِ", "muallal", NA("صَادِقَتَا", "raf", "alif"), NUN_IWAD, nt("أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ عَلَى الْقَطْعِ، أَيْ: هُمَا مُؤَلَّلَتَانِ (الدُّرَّةُ)؛ التَّأْلِيلُ: التَّحْدِيدُ وَالتَّدْقِيقُ، مِنَ الْأَلَّةِ وَهِيَ الْحَرْبَةُ", "or the predicate of an omitted mubtada, cut off — «they are sharp-pointed» (al-Durra); التَّأْلِيل: sharpening to a point, from الأَلَّة, a spear-head", "ya da kat' üzere mahzûf mübtedanın haberi: «onlar sivridir» (Dürre); التَّأْلِيل: sivriltmek, inceltmek — kısa mızrak demek olan الأَلَّة'den", "ism-maful")),
 VB("تَعْرِفُ", "arafa", "mud", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «مُؤَلَّلَتَانِ»، وَالرَّابِطُ الضَّمِيرُ فِي «فِيهِمَا» (الدُّرَّةُ)", "the clause is a hal of the pronoun hidden in «مُؤَلَّلَتَانِ», in the seat of nasb, tied by the pronoun of «فِيهِمَا» (al-Durra)", "cümle «مُؤَلَّلَتَانِ»daki gizli zamirden hâl olarak mahallen mansûb; râbıt «فِيهِمَا»daki zamirdir (Dürre)", "al-hal-jumla-wa-rabituha"), who="أَنْتَ"),
 NO("الْعِتْقَ", "itq", "maf", nt("الْعِتْقُ: الْكَرَمُ وَالنَّجَابَةُ", "العِتْق: nobility, fine breeding", "العِتْق: soyluluk, necabet")),
 PJ("فِيهِمَا", "فِي", "fi", "هِمَا", ON("تَعْرِفُ"), ref="مُؤَلَّلَتَانِ", p=HEMI),
 NO("كَسَامِعَتَيْ", "samia-ear", R("maj", "ya2") + MUD, NUN_IDF, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: هُمَا كَسَامِعَتَيْ شَاةٍ (الدُّرَّةُ)؛ السَّامِعَتَانِ: الْأُذُنَانِ", "the phrase hangs on the omitted predicate of an omitted mubtada — «they are like the two ears of…» (al-Durra); السَّامِعَتَان: the two ears", "câr-mecrûr mahzûf mübtedanın mahzûf haberine müteallik: «onlar … kulakları gibidir» (Dürre); السَّامِعَتَان: iki kulak"),
    TSB("mm", ("أُذُنَاهَا", "her ears", "kulakları"), ("أُذُنَا ثَوْرٍ وَحْشِيٍّ مُنْفَرِدٍ", "the ears of a wild ox on its own", "tek başına kalmış bir yaban öküzünün kulakları"), "ka"), pre="ka", g=TSB_TAGS),
 NO("شَاةٍ", "shat", "mi", nt("الشَّاةُ هُنَا: الثَّوْرُ الْوَحْشِيُّ", "الشَّاة here: the wild ox", "الشَّاة burada: yaban öküzü")),
 NO("بِحَوْمَلَ", "hawmal", R("maj", "fatha"), nt("لِلْعَلَمِيَّةِ؛ وَقَالَ الدُّرَّةُ: لِلْعَلَمِيَّةِ وَالْعُجْمَةِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«شَاةٍ»؛ حَوْمَلُ: مَوْضِعٌ بِعَيْنِهِ", "for being a proper name (al-Durra: a name, and foreign); the phrase hangs on an omitted adjective of «شَاةٍ»; Ḥawmal is a particular place", "alem olduğu için (Dürre: alemiyet ve ucmet); câr-mecrûr «شَاةٍ»nin mahzûf na'tına müteallik; Havmel belli bir yerdir"), pre="bi", pos="propn"),
 NO("مُفْرَدِ", "mufrad", NA("شَاةٍ", "jarr", "", "2"), nt("وَخَصَّ الْمُفْرَدَ لِأَنَّهُ أَشَدُّ فَزَعًا وَتَيَقُّظًا وَاحْتِرَازًا (الزَّوْزَنِيُّ)؛ وَذُكِّرَ لِأَنَّ الشَّاةَ هُنَا الثَّوْرُ", "he names the lone one because it is the most startled, wakeful and wary (al-Zawzanī); it is masculine because the شَاة here is the ox", "yalnız olanı seçmiştir, çünkü o en ürkek, en uyanık ve en tetikte olandır (Zevzenî); şâh burada öküz olduğu için müzekkerdir", "ism-maful"), q=True),
])
V(36, "And a heart quick to start, fast-beating, light, compact — like a rock-breaker of stone set among broad, firm-bound slabs.",
  "Bir de çabuk ürken, çok çarpan, hafif, derli toplu bir kalbi vardır; sağlam bağlanmış geniş taş levhalar arasındaki, taş kıran bir kaya gibi.", [
 NO("وَأَرْوَعُ", "arwa", AT("أَتْلَعُ", "raf"), AS_ATLA, nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: وَقَلْبٌ أَرْوَعُ (الدُّرَّةُ)، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»؛ الْأَرْوَعُ: الَّذِي يَرْتَاعُ لِكُلِّ شَيْءٍ لِفَرْطِ ذَكَائِهِ", "it describes a noun left out — «and a heart quick to start» (al-Durra) — and takes no tanwin, a diptote (an adjective on أَفْعَل); الأَرْوَع: one that starts at everything, so keen is it", "mahzûf bir mevsûfun sıfatıdır: «çabuk ürken bir kalp» (Dürre); vasfiyet ve «أَفْعَل» vezni sebebiyle gayr-i munsarif olduğundan tenvin almaz; الأَرْوَع: aşırı zekâsından her şeye irkilen", "hadhf-wa-taqdir", "mamnu-min-sarf"), pre="wa"),
 NO("نَبَّاضٌ", "nabbad", NMH("raf", nth="2"), nt("النَّبَّاضُ: الْكَثِيرُ الْحَرَكَةِ، مُبَالَغَةُ النَّابِضِ", "النَّبَّاض: much moving, beating — the intensive of النَّابِض", "النَّبَّاض: çok hareket eden, çarpan — النَّابِض'in mübalağası", "sighat-mubalagha")),
 NO("أَحَذُّ", "ahadhdh", NMH("raf", nth="3"), nt("وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»؛ الْأَحَذُّ: الْخَفِيفُ السَّرِيعُ", "it takes no tanwin, a diptote (an adjective on أَفْعَل); الأَحَذّ: light and quick", "vasfiyet ve «أَفْعَل» vezni sebebiyle gayr-i munsarif olduğundan tenvin almaz; الأَحَذّ: hafif ve çabuk", "mamnu-min-sarf")),
 NO("مُلَمْلَمٌ", "mulamlam", NMH("raf", nth="4"), nt("الْمُلَمْلَمُ: الْمُجْتَمِعُ الْخَلْقِ الشَّدِيدُ الصُّلْبُ", "المُلَمْلَم: compact of build, hard and firm", "المُلَمْلَم: yapısı derli toplu, sağlam ve sert", "ism-maful"), p=HEMI),
 NO("كَمِرْدَاةِ", "mirdat", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ خَامِسٍ لِلْمَوْصُوفِ الْمَحْذُوفِ؛ الْمِرْدَاةُ: الصَّخْرَةُ الَّتِي تُكْسَرُ بِهَا الصُّخُورُ", "the phrase hangs on an omitted fifth adjective of the noun left out; المِرْدَاة: the rock with which rocks are broken", "câr-mecrûr mahzûf mevsûfun mahzûf beşinci na'tına müteallik; المِرْدَاة: kayaların kırıldığı kaya", "ism-al-ala"),
    TSB("tm", ("الْقَلْبُ بَيْنَ الْأَضْلَاعِ", "the heart among the ribs", "kaburgalar arasındaki kalp"), ("حَجَرٌ صُلْبٌ بَيْنَ حِجَارَةٍ عِرَاضٍ", "a hard stone among broad stones", "geniş taşlar arasındaki sert bir taş"), "ka"), pre="ka", g=TSB_TAGS),
 NO("صَخْرٍ", "sakhr-rock", "mi", nt("وَالْإِضَافَةُ بِمَعْنَى «مِنْ»، أَيْ: كَمِرْدَاةٍ مِنْ صَخْرٍ، مِثْلُ قَوْلِهِمْ: هٰذَا ثَوْبُ خَزٍّ (الزَّوْزَنِيُّ)", "the annexation means «of» — a rock-breaker made of stone — as one says «a garment of silk» (al-Zawzanī)", "izâfet «min» anlamındadır: taştan bir kırıcı; «ipek elbise» demeleri gibi (Zevzenî)")),
 HJ("فِي", "fi"),
 NO("صَفِيحٍ", "safih", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ سَادِسٍ لِلْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)، أَيْ: فِيمَا بَيْنَ صَفِيحٍ (الزَّوْزَنِيُّ)؛ الصَّفِيحَةُ: الْحَجَرُ الْعَرِيضُ، وَالْجَمْعُ الصَّفَائِحُ وَالصَّفِيحُ", "the phrase hangs on an omitted sixth adjective of the noun left out (al-Durra) — «among slabs» (al-Zawzanī); الصَّفِيحَة: a broad stone — the plurals الصَّفَائِح and الصَّفِيح", "câr-mecrûr mahzûf mevsûfun mahzûf altıncı na'tına müteallik (Dürre): «levhalar arasında» (Zevzenî); الصَّفِيحَة: geniş taş; çoğulu الصَّفَائِح ve الصَّفِيح")),
 NO("مُصَمَّدِ", "musammad", NA("صَفِيحٍ", "jarr"), nt("نَعْتٌ لِلصَّفِيحِ عَلَى لَفْظِهِ دُونَ مَعْنَاهُ (الزَّوْزَنِيُّ)؛ الْمُصَمَّدُ: الْمُحْكَمُ الْمُوثَقُ", "it qualifies الصَّفِيح by its form, not its sense (al-Zawzanī); المُصَمَّد: firm, made fast", "الصَّفِيح'i mânâsına göre değil lafzına göre niteler (Zevzenî); المُصَمَّد: sağlam, bağlanmış", "ism-maful"), q=True),
])
V(37, "And a split lip, a nose pierced at its soft part, of fine breed: whenever she strikes the ground with it, she gains in pace.",
  "Bir de yarık bir dudağı, yumuşak yerinden delinmiş soylu bir burnu vardır; onu ne zaman yere vursa yürüyüşü artar.", [
 NO("وَأَعْلَمُ", "alam-split", AT("أَتْلَعُ", "raf"), AS_ATLA, nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: وَمِشْفَرٌ أَعْلَمُ (الدُّرَّةُ)، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»؛ الْأَعْلَمُ: الْمَشْقُوقُ الشَّفَةِ الْعُلْيَا", "it describes a noun left out — «and a split lip» (al-Durra) — and takes no tanwin, a diptote (an adjective on أَفْعَل); الأَعْلَم: split in the upper lip", "mahzûf bir mevsûfun sıfatıdır: «yarık bir dudak» (Dürre); vasfiyet ve «أَفْعَل» vezni sebebiyle gayr-i munsarif olduğundan tenvin almaz; الأَعْلَم: üst dudağı yarık", "hadhf-wa-taqdir", "mamnu-min-sarf"), pre="wa"),
 NO("مَخْرُوتٌ", "makhrut", NMH("raf", nth="2"), nt("الْمَخْرُوتُ: الْمَثْقُوبُ، وَالْخَرْتُ: الثَّقْبُ", "المَخْرُوت: pierced — الخَرْت is a hole", "المَخْرُوت: delinmiş — الخَرْت: delik", "ism-maful")),
 HJ("مِنَ", "min"),
 NO("الْأَنْفِ", "anf", R("maj"), ON("مَخْرُوتٌ")),
 NO("مَارِنٌ", "marin", NMH("raf", nth="3"), nt("الْمَارِنُ: مَا لَانَ مِنَ الْأَنْفِ", "المَارِن: the soft part of the nose", "المَارِن: burnun yumuşak kısmı"), p=HEMI),
 NO("عَتِيقٌ", "atiq-noble", NMH("raf", nth="4")),
 PT("مَتَى", "mata", MATA_SH + mk("، مُتَعَلِّقٌ بِـ«تَرْجُمْ»", ", hanging on «تَرْجُمْ»", ", «تَرْجُمْ»e müteallik"), nt("وَالْجُمْلَةُ الشَّرْطِيَّةُ نَعْتٌ آخَرُ لِلْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)", "the conditional sentence is a further adjective of the noun left out (al-Durra)", "şart cümlesi mahzûf mevsûfun bir başka na'tıdır (Dürre)")),
 VB("تَرْجُمْ", "rajama", "jz", who=("هِيَ", NAQA), by="shart"),
 PJ("بِهِ", "بِ", "bi", "هِ", ON("تَرْجُمْ"), ref=("الْمِشْفَرِ الْمَحْذُوفِ", "the lip left unnamed", "mahzûf dudağa")),
 NO("الْأَرْضَ", "ard", "maf", nt("يَقُولُ: عِنْدَمَا تَرْمِي الْأَرْضَ بِأَنْفِهَا وَرَأْسِهَا تَزْدَادُ فِي سَيْرِهَا (الزَّوْزَنِيُّ)", "he says: when she strikes the ground with nose and head she gains in pace (al-Zawzanī)", "der ki: yere burnuyla ve başıyla vurdukça yürüyüşü artar (Zevzenî)")),
 VB("تَزْدَدِ", "izdada", "jz", JM("jz"), who=("هِيَ", NAQA), by="jawab", q=True, g=["form-viii-verbs", "hollow-verbs"]),
])
V(38, "If I will, she does not race; and if I will, she races — for fear of a twisted whip of rawhide, firmly plaited.",
  "Dilersem koşmaz, dilersem koşar; kayıştan bükülmüş, sıkı örülmüş bir kamçının korkusundan.", [
 PT("وَإِنْ", "in-shartiyya", IN_SH, JM("ist"), pre="wa-ist"),
 VB("شِئْتُ", "shaa", "madi-tu", IN_COND, nt("وَهُوَ فِي الطَّبْعَةِ بِضَمِّ التَّاءِ، وَعِنْدَ التِّبْرِيزِيِّ «شِئْتَ»", "the edition has a damma on the ta; al-Tibrīzī has «شِئْتَ»", "baskıda tâ dammelidir; Tebrîzî'de «شِئْتَ»"), g=["hollow-verbs"]),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("تُرْقِلْ", "arqala", "jz", nt("وَجُمْلَةُ «لَمْ تُرْقِلْ» جَوَابُ الشَّرْطِ لَا مَحَلَّ لَهَا؛ الْإِرْقَالُ: دُونَ الْعَدْوِ وَفَوْقَ السَّيْرِ", "the clause «لَمْ تُرْقِلْ» answers the condition and has no seat; الإِرْقَال: a pace below running and above walking", "«لَمْ تُرْقِلْ» cümlesi şartın cevabıdır, mahalli yoktur; الإِرْقَال: koşudan aşağı, yürüyüşten yukarı bir gidiş", "al-majzum-wal-shart-wal-jaza"), who=("هِيَ", NAQA), by="lam", g=["form-iv-verbs"]),
 PT("وَإِنْ", "in-shartiyya", IN_SH, nt("وَالشَّرْطُ وَجَوَابُهُ مَعْطُوفَانِ عَلَى الشَّرْطِ الْأَوَّلِ وَجَوَابِهِ", "the condition and its answer are conjoined to the first condition and its answer", "şart ve cevabı, birinci şart ve cevabına ma'tûftur"), pre="wa"),
 VB("شِئْتُ", "shaa", "madi-tu", IN_COND, g=["hollow-verbs"]),
 VB("أَرْقَلَتْ", "arqala", "madi-f", IN_JAWAB,
    HD("طِبَاقُ السَّلْبِ بَيْنَ «لَمْ تُرْقِلْ» وَ«أَرْقَلَتْ»: فِعْلَا مَصْدَرٍ وَاحِدٍ، أَحَدُهُمَا مَنْفِيٌّ وَالْآخَرُ مُثْبَتٌ", "«لَمْ تُرْقِلْ» and «أَرْقَلَتْ» make a tibaq of negation: two verbs of one masdar, one denied and one affirmed", "«لَمْ تُرْقِلْ» ile «أَرْقَلَتْ» arasında tıbâk-ı selb vardır: biri menfî biri müsbet, aynı masdardan iki fiil"), who=("هِيَ", NAQA), g=["form-iv-verbs", "tibaq"], p=HEMI),
 NO("مَخَافَةَ", "makhafa", R("ml") + MUD, nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ، وَالْفَاعِلُ مَحْذُوفٌ، أَيْ: مَخَافَتَهَا مَلْوِيًّا (الدُّرَّةُ)", "the masdar annexed to its object, the doer left out — «her fearing a twisted one» (al-Durra)", "masdarın mef'ûlüne izâfeti; fâil mahzûftur: «onun bükülmüş birinden korkması» (Dürre)", "masdar")),
 NO("مَلْوِيٍّ", "malwiyy", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: سَوْطٍ مَلْوِيٍّ (الزَّوْزَنِيُّ)", "it describes a noun left out — «a twisted whip» (al-Zawzanī)", "mahzûf bir mevsûfun sıfatıdır: «bükülmüş bir kamçı» (Zevzenî)", "hadhf-wa-taqdir", "ism-maful")),
 HJ("مِنَ", "min"),
 NO("الْقِدِّ", "qidd", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ؛ الْقِدُّ: السَّيْرُ يُقَدُّ مِنَ الْجِلْدِ", "the phrase hangs on an omitted second adjective of the noun left out; القِدّ: a thong cut from hide", "câr-mecrûr mahzûf mevsûfun mahzûf ikinci na'tına müteallik; القِدّ: deriden kesilen kayış")),
 NO("مُحْصَدِ", "muhsad", NMH("jarr", nth="3"), nt("الْإِحْصَادُ: الْإِحْكَامُ وَالتَّوْثِيقُ", "الإِحْصَاد: making firm, plaiting fast", "الإِحْصَاد: sağlamlaştırmak, sıkıca örmek", "ism-maful"), q=True),
])
V(39, "And if I will, her head rises level with the saddle-front, and she swims with her forelegs, swift as the male ostrich.",
  "Dilersem başı semerin ön kaşıyla yükseklikte yarışır; ön kollarıyla, erkek devekuşunun hızıyla yüzercesine gider.", [
 PT("وَإِنْ", "in-shartiyya", IN_SH, JM("ist"), pre="wa-ist"),
 VB("شِئْتُ", "shaa", "madi-tu", IN_COND, g=["hollow-verbs"]),
 VB("سَامَى", "sama-vie", "madi-muq", IN_JAWAB, nt("الْمُسَامَاةُ: الْمُبَارَاةُ فِي السُّمُوِّ وَهُوَ الْعُلُوُّ؛ يَقُولُ: إِنْ شِئْتُ جَعَلْتُ رَأْسَهَا مُوَازِيًا لِوَاسِطِ رَحْلِهَا فِي الْعُلُوِّ بِجَذْبِي زِمَامَهَا إِلَيَّ (الزَّوْزَنِيُّ)", "المُسَامَاة: vying in height; he says: if I will, I bring her head level with her saddle-front by drawing her rein to me (al-Zawzanī)", "المُسَامَاة: yükseklikte yarışmak; der ki: dilersem yularını kendime çekerek başını semerinin ön kaşıyla aynı yüksekliğe getiririm (Zevzenî)"), g=["form-iii-verbs", "naqis-verbs"]),
 NO("وَاسِطَ", "wasit", R("maf") + MUD, nt("وَاسِطُ الْكُورِ لَهُ كَالْقَرَبُوسِ لِلسَّرْجِ", "the واسِط of the saddle is to it what the pommel is to a horse's saddle", "semerin وَاسِط'ı, eyerin kaşı gibidir")),
 NO("الْكُورِ", "kur", "mi", nt("الْكُورُ: الرَّحْلُ بِأَدَاتِهِ", "الكُور: the saddle with its gear", "الكُور: takımıyla semer")),
 NO("رَأْسُهَا", "ras", "fail", enc="هَا", p=HEMI),
 VB("وَعَامَتْ", "ama-swim", "madi-f", JM("atf", "سَامَى"), nt("الْعَوْمُ: السِّبَاحَةُ، عَامَ يَعُومُ", "العَوْم: swimming — عَامَ يَعُومُ", "العَوْم: yüzmek — عَامَ يَعُومُ"),
    HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْفِعْلِ: شُبِّهَ مَدُّهَا ضَبْعَيْهَا فِي سُرْعَةِ السَّيْرِ بِالْعَوْمِ، وَاسْتُعِيرَ لَهُ «عَامَتْ» (قَالَ الزَّوْزَنِيُّ: «حَتَّى كَأَنَّهَا تَسْبَحُ بِعَضُدَيْهَا»)", "there is a dependent istiara in the verb: her reaching out with her forelegs as she speeds is likened to swimming, and «عَامَتْ» is borrowed for it (al-Zawzanī: «so that she seems to swim with her upper arms»)", "fiilde istiâre-i tebeiyye vardır: hızla giderken ön kollarını uzatması yüzmeye benzetilmiş ve ona «عَامَتْ» fiili iğreti alınmıştır (Zevzenî: «sanki pazılarıyla yüzüyormuş gibi»)"), who=("هِيَ", NAQA), pre="wa", g=["hollow-verbs", "istiara-tabaiyya", "istiara"]),
 NO("بِضَبْعَيْهَا", "dab-arm", R("maj", "ya2"), NUN_IDF, ON("عَامَتْ"), nt("الضَّبْعُ: الْعَضُدُ", "الضَّبْع: the upper arm", "الضَّبْع: pazı"), enc="هَا", pre="bi"),
 NO("نَجَاءَ", "naja-speed", R("mm") + MUD, nt("مُرَادِفٌ لِمَصْدَرِ «عَامَتْ»، وَقِيلَ: نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ (الدُّرَّةُ)؛ النَّجَاءُ: الْإِسْرَاعُ", "a synonym of the masdar of «عَامَتْ»; also said to stand in for the absolute object (al-Durra); النَّجَاء: going fast", "«عَامَتْ»in masdarının müradifi; mef'ûlün mutlakın nâibi olduğu da söylenmiştir (Dürre); النَّجَاء: hızlı gitmek", "masdar"),
    TSB("bl", ("إِسْرَاعُ النَّاقَةِ", "the she-camel's speed", "devenin hızı"), ("إِسْرَاعُ الظَّلِيمِ", "the speed of the male ostrich", "erkek devekuşunun hızı"), src="z"), g=TSB_TAGS),
 NO("الْخَفَيْدَدِ", "khafaydad", "mi", nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الْخَفَيْدَدُ: الظَّلِيمُ، ذَكَرُ النَّعَامِ", "the masdar annexed to its doer; الخَفَيْدَد: the male ostrich", "masdarın fâiline izâfeti; الخَفَيْدَد: erkek devekuşu")),
])
# ---- «On such a one I ride»; the young man's boast: verses 40–47 -------------------------------------------------------
_CL["bi-z"] = ("الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ", "The ba is an added jarr letter; ", "Bâ zâid cer harfi; ", ("بِ", "bi", "prep"))
_CLTAG["bi-z"] = "huruf-al-ziyada-fil-kafiya"
def IDHA_Z(x):
    """إِذَا as a plain adverb of time hung on «x» (al-Durra)"""
    return mk("ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«%s» (الدُّرَّةُ)، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ" % x,
              "An adverb for time to come, built on sukun in the seat of nasb, hanging on «%s» (al-Durra), annexed to the clause after it" % x,
              "Gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb; «%s»e müteallik (Dürre), kendinden sonraki cümleye muzâf" % x, "maful-fih")
NI_OBJ = nt("وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "the nun guards the verb's ending, and the ya is its object, in the seat of nasb", "nûn vikâye içindir; yâ mef'ûlün bih, mahallen mansûb")
V(40, "On such a one as she I press on, when my companion says: «Would that I might ransom you from it — and ransom myself!»",
  "Onun gibisinin sırtında yoluma devam ederim; arkadaşım «Keşke seni ondan kurtarabilsem, kendimi de kurtarabilsem!» dediği zaman bile.", [
 HJ("عَلَى", "ala"),
 NO("مِثْلِهَا", "mithl", R("maj"), ON("أَمْضِي"), enc="هَا"),
 VB("أَمْضِي", "mada", "mud-y", JM("ist"), nt("يَقُولُ: عَلَى مِثْلِ هٰذِهِ النَّاقَةِ أَمْضِي فِي أَسْفَارِي (الزَّوْزَنِيُّ)", "he says: on such a she-camel as this I go on my journeys (al-Zawzanī)", "der ki: bu deve gibisinin sırtında yolculuklarıma devam ederim (Zevzenî)"), who="أَنَا", g=["naqis-verbs"]),
 PT("إِذَا", "idha", IDHA_Z("أَمْضِي")),
 VB("قَالَ", "qala", "madi", JM("mudaf", "إِذَا"), g=["hollow-verbs"]),
 NO("صَاحِبِي", "sahib", R("fail", "yam"), enc="ي", p=HEMI),
 PT("أَلَا", "ala-tanbih", mk("حَرْفُ تَنْبِيهٍ وَاسْتِفْتَاحٍ", "A particle that calls for attention and opens the speech", "Tenbih ve istiftâh harfi", "huruf-tanbih")),
 PT("لَيْتَنِي", "layta", mk("حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّمَنِّي، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "A verb-like particle of wishing; the nun guards its ending, and the ya is its noun, in the seat of nasb", "Temenni bildiren, fiile benzeyen harf; nûn vikâye içindir; yâ ismi, mahallen mansûb", "inna-wa-akhawatuha"),
    nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "the sentence is what is said, in the seat of nasb", "cümle mekūlü'l-kavl olarak mahallen mansûb"),
    HD("إِنْشَاءٌ طَلَبِيٌّ: تَمَنٍّ بِاللَّفْظِ الْمَوْضُوعِ لَهُ «لَيْتَ»، فِي أَمْرٍ يُحَبُّ وَلَا يُطْمَعُ فِي حُصُولِهِ", "an inshāʾ of request: a wish, made with لَيْتَ, the word set for it, for a thing loved and not hoped for", "talebî inşâ: temenni, onun için konmuş «لَيْتَ» lafzıyla; sevilen fakat gerçekleşmesi umulmayan bir şey için"), stem="لَيْتَنِي", g=["insha-wa-tamanni"]),
 VB("أَفْدِيكَ", "fada", "mud-y", JM("kh", "لَيْتَ", "raf"), who="أَنَا", enc="كَ", g=["naqis-verbs"]),
 PJ("مِنْهَا", "مِنْ", "min", "هَا", ON("أَفْدِي"), nt("أَيْ: مِنْ مَشَقَّةِ هٰذِهِ الشُّقَّةِ (الزَّوْزَنِيُّ)", "that is, from the hardship of this long journey (al-Zawzanī)", "yani bu uzun yolculuğun meşakkatinden (Zevzenî)")),
 VB("وَأَفْتَدِي", "iftada", "mud-y", JM("atf", "أَفْدِيكَ"), nt("أَيْ: وَأُنْجِي نَفْسِي (الزَّوْزَنِيُّ)", "that is, and save myself (al-Zawzanī)", "yani kendimi de kurtarırım (Zevzenî)"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «أَفْدِيكَ» وَ«أَفْتَدِي» الِاشْتِقَاقُ", "a figure joined to jinas: «أَفْدِيكَ» and «أَفْتَدِي» are brought together by derivation", "cinâsa mülhak: «أَفْدِيكَ» ile «أَفْتَدِي»yi iştikak bir araya getirmiştir"), who="أَنَا", pre="wa", g=["form-viii-verbs", "naqis-verbs", "mulhaq-bil-jinas"]),
])
V(41, "His soul rose up in him for fear, and he thought himself already lost — though at evening he was on no road where men lie in wait.",
  "Korkudan canı boğazına geldi; yol kesicilerin pusu kurduğu bir yolda olmasa bile kendini helâk olmuş sandı.", [
 VB("وَجَاشَتْ", "jasha", "madi-f", JM("atf", "أَمْضِي"), nt("أَيْ: ارْتَفَعَتْ نَفْسُهُ، أَيْ زَالَ قَلْبُهُ عَنْ مُسْتَقَرِّهِ لِفَرْطِ خَوْفِهِ (الزَّوْزَنِيُّ)", "that is, his soul rose — his heart left its place, so great was his fear (al-Zawzanī)", "yani canı yükseldi — korkusunun şiddetinden kalbi yerinden oynadı (Zevzenî)"),
    S_(mk("فَهُوَ كِنَايَةٌ عَنْ شِدَّةِ الْخَوْفِ، أُرِيدَ بِجَيَشَانِ النَّفْسِ لَازِمُهُ كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "So it is a kinaya for great fear: the soul's surging is said and what follows from it is meant, as al-Zawzanī explains", "Bu, korkunun şiddetinden kinâyedir: canın kabarması söylenmiş, lâzımı kastedilmiştir; Zevzenî böyle açıklar", "kinaya")), pre="wa", g=["hollow-verbs"]),
 PJ("إِلَيْهِ", "إِلَيْ", "ila", "هِ", ON("جَاشَتْ"), ref="صَاحِبِي"),
 NO("النَّفْسُ", "nafs", "fail"),
 NO("خَوْفًا", "khawf", mk("حَالٌ مِنَ «النَّفْسُ» مَنْصُوبٌ بِالْفَتْحَةِ، بِمَعْنَى: خَائِفَةً", "A hal of «النَّفْسُ», the doer, in nasb by the fatha — «afraid»", "«النَّفْسُ»tan hâl, fetha ile mansûb — «korkarak» anlamında", "hal"), nt("وَيَجُوزُ أَنْ يَكُونَ مَفْعُولًا لِأَجْلِهِ (الدُّرَّةُ)", "it may also be an object of cause (al-Durra)", "mef'ûlün lieclih olması da câizdir (Dürre)")),
 VB("وَخَالَهُ", "khala-think", "madi", JM("atf", "جَاشَتْ"), nt("وَالْهَاءُ أَوَّلُ مَفْعُولَيْهِ؛ خَالَهُ: ظَنَّهُ، وَالْخَيْلُولَةُ: الظَّنُّ (الزَّوْزَنِيُّ)", "the هُ is the first of its two objects; خَالَهُ: he thought him — الخَيْلُولَة is supposing (al-Zawzanī)", "hâ iki mef'ûlünün birincisidir; خَالَهُ: onu sandı — الخَيْلُولَة: zan (Zevzenî)"), who=("هُوَ", "صَاحِبِي"), enc="هُ", pre="wa", g=["hollow-verbs", "zanna-wa-akhawatuha", "mafulayn"], p=HEMI),
 NO("مُصَابًا", "musab", "maf2", nt("أَيْ: هَالِكًا (الزَّوْزَنِيُّ)", "that is, perished (al-Zawzanī)", "yani helâk olmuş (Zevzenî)", "ism-maful")),
 PT("وَلَوْ", "law", mk("حَرْفٌ وَصْلِيٌّ", "A particle of linking («even if»)", "Vasliyye harfi («-se bile»)", "huruf-al-shart-fil-kafiya"), nt("وَإِنْ عُدَّتْ شَرْطِيَّةً فَجَوَابُهَا مَحْذُوفٌ لِدَلَالَةِ مَا قَبْلَهُ عَلَيْهِ (الدُّرَّةُ)", "if it is taken as conditional, its answer is left out, what precedes pointing to it (al-Durra)", "şart edatı sayılırsa, öncesi delâlet ettiği için cevabı mahzûftur (Dürre)"), pre="wa-hal"),
 VB("أَمْسَى", "amsa", "madi-muq", nt("نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ عَلَى الصَّاحِبِ؛ وَجُمْلَةُ «لَوْ أَمْسَى…» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ مَفْعُولِ «خَالَ» الْأَوَّلِ، وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ (الدُّرَّةُ)", "it is defective; its noun is a hidden «he», returning to the companion; the clause «لَوْ أَمْسَى…» is a hal of the first object of «خَالَ», in the seat of nasb, tied by the waw and the pronoun (al-Durra)", "nâkıstır; ismi sahibe dönen gizli «هُوَ»dur; «لَوْ أَمْسَى…» cümlesi «خَالَ»in birinci mef'ûlünden hâl olarak mahallen mansûb; râbıt vâv ve zamirdir (Dürre)", "kana-wa-akhawatuha"), g=["naqis-verbs"]),
 HJ("عَلَى", "ala"),
 NO("غَيْرِ", "ghayr", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «أَمْسَى»", "the phrase hangs on the omitted predicate of «أَمْسَى»", "câr-mecrûr «أَمْسَى»nın mahzûf haberine müteallik")),
 NO("مَرْصَدِ", "marsad", "mi", nt("الْمَرْصَدُ: الطَّرِيقُ، وَكَذٰلِكَ الْمِرْصَادُ", "المَرْصَد: the road (where one lies in wait); so too المِرْصَاد", "المَرْصَد: yol (pusu kurulan); المِرْصَاد da öyledir", "ism-al-zaman-wal-makan"), q=True),
])
V(42, "When the men say «Who is the young man?», I think it is I who am meant; and I am not slow, nor do I falter.",
  "Kavim «Kimdir o yiğit?» dediğinde, kastedilenin ben olduğumu sanırım; ne gevşerim ne de duraksarım.", [
 PT("إِذَا", "idha", IDHA_SH, JM("ist")),
 NO("الْقَوْمُ", "qawm", "fail", nt("لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «قَالُوا»، وَالْجُمْلَةُ الْمَحْذُوفَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا، عَلَى مَذْهَبِ الْبَصْرِيِّينَ (الدُّرَّةُ)", "of a verb left out that «قَالُوا» explains; that omitted clause is in the seat of jarr, إِذَا being annexed to it — the Basrans' way (al-Durra)", "«قَالُوا»nun tefsir ettiği mahzûf bir fiilin fâilidir; mahzûf cümle «إِذَا»nın ona izâfetiyle mahallen mecrûr — Basralıların görüşü (Dürre)", "hadhf-wa-taqdir")),
 VB("قَالُوا", "qala", "madi-w", nt("وَالْجُمْلَةُ مُفَسِّرَةٌ لَا مَحَلَّ لَهَا", "the clause explains the omitted verb and has no seat", "cümle tefsiriyyedir, mahalli yoktur"), g=["hollow-verbs"]),
 PT("مَنْ", "man-istifham", mk("اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "An interrogative noun built on sukun, in the seat of raf' as mubtada", "Sükûn üzere mebnî istifham ismi; mübteda olarak mahallen merfû", "al-istifham", "mubtada-khabar"), pos="pron"),
 NO("فَتًى", "fata-youth", R("kh", "maqh"), JM("maqul"), nt("أَيْ: مَنْ فَتًى يَكْفِي مُهِمًّا أَوْ يَدْفَعُ شَرًّا؟ (الزَّوْزَنِيُّ)", "that is, «who is the young man to see a grave matter through, or ward off harm?» (al-Zawzanī)", "yani «önemli bir işi görecek ya da bir şerri savacak yiğit kim?» (Zevzenî)")),
 VB("خِلْتُ", "khala-think", "madi-tu", JM("jawab", "إِذَا"), g=["hollow-verbs", "zanna-wa-akhawatuha"]),
 PT("أَنَّنِي", "anna", INNA_T + mk("، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the nun guards its ending, and the ya is its noun, in the seat of nasb", "; nûn vikâye içindir; yâ ismi, mahallen mansûb"),
    nt("وَ«أَنَّ» وَمَعْمُولَاهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «خِلْتُ»", "أَنَّ with its two terms is read as a masdar that takes the place of the two objects of «خِلْتُ»", "«أَنَّ» ve iki ma'mûlü, «خِلْتُ»in iki mef'ûlünün yerini tutan masdar te'vilindedir", "mawadi-fath-anna"), stem="أَنَّنِي", p=HEMI),
 VB("عُنِيتُ", "ana-mean", "madi-tu", JM("kh", "أَنَّ", "raf"), nt("عَنَى يَعْنِي: أَرَادَ، وَمِنْهُ الْمَعْنَى وَهُوَ الْمُرَادُ (الزَّوْزَنِيُّ)", "عَنَى يَعْنِي: to mean, to intend — whence المَعْنَى, what is meant (al-Zawzanī)", "عَنَى يَعْنِي: kastetmek — المَعْنَى (kastedilen) de buradandır (Zevzenî)"), maj=True, g=["naqis-verbs"]),
 PT("فَلَمْ", "lam-jazima", LAM_J, pre="fa-sabab"),
 VB("أَكْسَلْ", "kasila", "jz", JM("atf", "عُنِيتُ"), who="أَنَا", by="lam"),
 PT("وَلَمْ", "lam-jazima", LAM_J, pre="wa"),
 VB("أَتَبَلَّدِ", "taballada", "jz", JM("atf", "أَكْسَلْ"), nt("التَّبَلُّدُ: ضِدُّ التَّجَلُّدِ وَالنَّشَاطِ، أَيِ: التَّحَيُّرُ وَالْفُتُورُ", "التَّبَلُّد: the opposite of briskness — standing at a loss, slackening", "التَّبَلُّد: çeviklik ve canlılığın zıddı — şaşırıp kalmak, gevşemek"), who="أَنَا", by="lam", q=True, g=["form-v-verbs"]),
])
V(43, "I came at her with the whip, and she sped on, while the mirage of the blazing, stony ground was trotting.",
  "Kamçıyla ona yöneldim, o da hızlandı; o sırada taşlık, kızgın arazinin serabı titreşip koşuyordu.", [
 VB("أَحَلْتُ", "ahala", "madi-tu", JM("ist"), nt("الْإِحَالَةُ: الْإِقْبَالُ هُنَا (الزَّوْزَنِيُّ)؛ وَالْجُمْلَةُ بِمَنْزِلَةِ جَوَابِ سُؤَالٍ مُقَدَّرٍ: مَاذَا تَفْعَلُ؟ (الدُّرَّةُ)", "الإِحَالَة here is coming at (al-Zawzanī); the clause is as if it answered a question understood: «what do you do?» (al-Durra)", "الإِحَالَة burada yönelmektir (Zevzenî); cümle takdîrî bir soruya — «ne yaparsın?» — cevap gibidir (Dürre)"), g=["form-iv-verbs", "hollow-verbs"]),
 PJ("عَلَيْهَا", "عَلَيْ", "ala", "هَا", ON("أَحَلْتُ"), ref=NAQA),
 NO("بِالْقَطِيعِ", "qati-whip", R("maj"), ON("أَحَلْتُ"), nt("الْقَطِيعُ: السَّوْطُ", "القَطِيع: the whip", "القَطِيع: kamçı"), pre="bi"),
 VB("فَأَجْذَمَتْ", "ajdhama", "madi-f", JM("atf", "أَحَلْتُ"), nt("الْإِجْذَامُ: الْإِسْرَاعُ فِي السَّيْرِ؛ وَعِنْدَ التِّبْرِيزِيِّ «فَأَجْدَمَتْ» بِالدَّالِ", "الإِجْذَام: speeding up; al-Tibrīzī has «فَأَجْدَمَتْ», with dal", "الإِجْذَام: yürüyüşte hızlanmak; Tebrîzî'de dâl ile «فَأَجْدَمَتْ»"), who=("هِيَ", NAQA), pre="fa", g=["form-iv-verbs"], p=HEMI),
 PT("وَقَدْ", "qad", QAD_T, nt("وَجُمْلَةُ «وَقَدْ خَبَّ…» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «أَجْذَمَتْ» الْمُسْتَتِرِ (الدُّرَّةُ)", "the clause «وَقَدْ خَبَّ…» is a hal of the hidden doer of «أَجْذَمَتْ», in the seat of nasb (al-Durra)", "«وَقَدْ خَبَّ…» cümlesi «أَجْذَمَتْ»in gizli fâilinden hâl olarak mahallen mansûb (Dürre)"), pre="wa-hal", stem="قَدْ"),
 VB("خَبَّ", "khabba", "madi", nt("الْخَبَبُ: ضَرْبٌ مِنَ الْعَدْوِ", "الخَبَب: a kind of trot", "الخَبَب: bir tür tırıs koşu"),
    HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْفِعْلِ: شُبِّهَ تَرَجْرُجُ الْآلِ وَاضْطِرَابُهُ بِخَبَبِ الْمَاشِي، وَاسْتُعِيرَ لَهُ «خَبَّ»", "a dependent istiara in the verb: the quivering of the mirage is likened to a trotting beast's gait, and «خَبَّ» is borrowed for it", "fiilde istiâre-i tebeiyye: serabın titreşip dalgalanması tırıs koşuya benzetilmiş ve ona «خَبَّ» fiili iğreti alınmıştır"), g=["doubled-verbs", "istiara-tabaiyya", "istiara"]),
 NO("آلُ", "aal-mirage", R("fail") + MUD, nt("الْآلُ: مَا يُرَى شِبْهَ السَّرَابِ طَرَفَيِ النَّهَارِ، وَالسَّرَابُ مَا كَانَ نِصْفَ النَّهَارِ", "الآل: what is seen like a mirage at either end of the day; السَّرَاب is that at midday", "الآل: günün iki ucunda serap gibi görünen şey; السَّرَاب gün ortasındakidir")),
 NO("الْأَمْعَزِ", "amaz", "mi", nt("الْأَمْعَزُ: مَكَانٌ يُخَالِطُ تُرَابَهُ حِجَارَةٌ أَوْ حَصًى", "الأَمْعَز: ground whose earth is mixed with stones or gravel", "الأَمْعَز: toprağına taş ya da çakıl karışmış yer")),
 NO("الْمُتَوَقِّدِ", "mutawaqqid", NA("الْأَمْعَزِ", "jarr"), nt("أَيِ: الْمُلْتَهِبِ حَرًّا", "that is, blazing with heat", "yani sıcaktan alev alev yanan", "ism-fail")),
])
V(44, "And she swaggered, as a slave-girl of the gathering swaggers, showing her master the long skirts of a white robe drawn out.",
  "Ve salınarak yürüdü; tıpkı meclisteki câriyenin, efendisine uzatılmış beyaz elbisesinin eteklerini göstererek salınması gibi.", [
 VB("فَذَالَتْ", "dhala-strut", "madi-f", JM("atf", "أَجْذَمَتْ"), nt("الذَّيْلُ: التَّبَخْتُرُ، ذَالَ يَذِيلُ", "الذَّيْل: swaggering — ذَالَ يَذِيلُ", "الذَّيْل: salınmak — ذَالَ يَذِيلُ"), who=("هِيَ", NAQA), pre="fa-sabab", g=["hollow-verbs"]),
 PT("كَمَا", "kama", mk("الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَمَا مَصْدَرِيَّةٌ", "The kaf is the jarr letter of likening, and مَا makes a masdar", "Kâf teşbih ve cer harfi; مَا masdariyye", "huruf-jarr", "anwa-ma"),
    nt("وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: ذَالَتْ ذَيْلًا مِثْلَ ذَيْلِ وَلِيدَةِ مَجْلِسٍ (الدُّرَّةُ)", "the masdar so made is in the seat of jarr by the kaf, and the phrase hangs on the omitted adjective of an omitted absolute object — «she swaggered a swagger like the slave-girl's» (al-Durra)", "te'vil edilen masdar kâf ile mahallen mecrûr; câr-mecrûr mahzûf bir mef'ûlün mutlakın mahzûf sıfatına müteallik: «câriyenin salınışı gibi bir salınışla salındı» (Dürre)", "maful-mutlaq"),
    TSB("mm", ("تَبَخْتُرُ النَّاقَةِ فِي السَّيْرِ", "the she-camel's swaggering gait", "devenin salınarak yürüyüşü"), ("تَبَخْتُرُ الْجَارِيَةِ فِي الرَّقْصِ", "a slave-girl's swaying in the dance", "câriyenin dansta salınışı"), "kama"),
    ZW("وَشَبَّهَ طُولَ ذَنَبِهَا بِطُولِ ذَيْلِهَا", "and he likens the length of her tail to the length of the girl's skirt", "kuyruğunun uzunluğunu da câriyenin eteğinin uzunluğuna benzetmiştir"), g=TSB_TAGS),
 VB("ذَالَتْ", "dhala-strut", "madi-f", JM("sila"), g=["hollow-verbs"]),
 NO("وَلِيدَةُ", "walida-girl", R("fail") + MUD, nt("الْوَلِيدَةُ: الصَّبِيَّةُ وَالْجَارِيَةُ، وَهِيَ فِي الْبَيْتِ بِمَعْنَى الْجَارِيَةِ (الزَّوْزَنِيُّ)", "الوَلِيدَة: a young girl or a slave-girl — in this verse a slave-girl (al-Zawzanī)", "الوَلِيدَة: kız çocuk ya da câriye — beyitte câriye anlamındadır (Zevzenî)")),
 NO("مَجْلِسٍ", "majlis", "mi", p=HEMI),
 VB("تُرِي", "ara", "mud-y", JM("sifa", "وَلِيدَةُ", "raf"), nt("أَوْ حَالٌ مِنْهَا لِتَخْصِيصِهَا بِالْإِضَافَةِ (الدُّرَّةُ)", "or a hal of her, since the annexation has made her particular (al-Durra)", "ya da izâfetle tahsis edildiği için ondan hâldir (Dürre)"), who=("هِيَ", "وَلِيدَةُ"), g=["form-iv-verbs", "naqis-verbs", "mafulayn"]),
 NO("رَبَّهَا", "rabb", "maf1", nt("أَيْ: سَيِّدَهَا", "that is, her master", "yani efendisi"), enc="هَا"),
 NO("أَذْيَالَ", "dhayl", R("maf2") + MUD, g=["jam-taksir"]),
 NO("سَحْلٍ", "sahl-cloth", "mi", nt("السَّحْلُ: الثَّوْبُ الْأَبْيَضُ مِنَ الْقُطْنِ وَغَيْرِهِ", "السَّحْل: a white garment of cotton or the like", "السَّحْل: pamuktan vb. beyaz elbise")),
 NO("مُمَدَّدِ", "mumaddad", NA("سَحْلٍ", "jarr"), nt("أَيْ: طَوِيلٍ (الزَّوْزَنِيُّ)", "that is, long (al-Zawzanī)", "yani uzun (Zevzenî)", "ism-maful"), q=True),
])
V(45, "I am not one who keeps to the low ground of the valleys for fear; but whenever the people ask for help, I give it.",
  "Korkudan vadilerin çukur yerlerine konan biri değilim; fakat kavim ne zaman yardım isterse yardım ederim.", [
 PT("وَلَسْتُ", "laysa", mk("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا", "A defective, frozen past verb built on sukun because the ta is attached; the ta is its noun, in the seat of raf'", "Tâ bitiştiği için sükûn üzere mebnî, câmid, nâkıs mâzî fiil; tâ ismi, mahallen merfû", "kana-wa-akhawatuha"), JM("ist"), pre="wa-ist", stem="لَسْتُ"),
 NO("بِحَلَّالِ", "hallal", mk("خَبَرُ «لَيْسَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "The predicate of لَيْسَ, in nasb by an estimated fatha, its place taken by the kasra of the added jarr letter", "«لَيْسَ»in haberi; mahalli zâid cer harfinin harekesi işgal ettiğinden takdîrî fetha ile mansûb", "kana-wa-akhawatuha") + MUD,
    nt("مِنْ إِضَافَةِ صِيغَةِ الْمُبَالَغَةِ إِلَى مَفْعُولِهَا؛ الْحَلَّالُ: مُبَالَغَةُ الْحَالِّ، مِنَ الْحُلُولِ", "the intensive annexed to its object; الحَلَّال: the intensive of الحَالّ, one who alights, from الحُلُول", "mübalağa sîgasının mef'ûlüne izâfeti; الحَلَّال: الحَالّ'ın (konan) mübalağası, الحُلُول'den", "sighat-mubalagha"), pre="bi-z"),
 NO("التِّلَاعِ", "tala", "mi", nt("التَّلْعَةُ: مَا ارْتَفَعَ مِنْ مَسِيلِ الْمَاءِ وَانْخَفَضَ عَنِ الْجِبَالِ، وَالْجَمْعُ التِّلَاعُ", "التَّلْعَة: ground above a water-course and below the mountains — the plural التِّلَاع", "التَّلْعَة: sel yatağından yüksek, dağlardan alçak yer — çoğulu التِّلَاع", "jam-taksir")),
 NO("مَخَافَةً", "makhafa", "ml", nt("وَجُوِّزَ أَنْ يَكُونَ مَفْعُولًا مُطْلَقًا (الدُّرَّةُ)", "it has also been allowed as an absolute object (al-Durra)", "mef'ûlün mutlak olması da câiz görülmüştür (Dürre)"),
    ZW("يَقُولُ: أَنَا لَا أَحُلُّ التِّلَاعَ مَخَافَةَ حُلُولِ الْأَضْيَافِ بِي أَوْ غَزْوِ الْأَعْدَاءِ إِيَّايَ", "he says: I do not keep to the low ground for fear of guests coming down on me or enemies raiding me", "der ki: misafirlerin bana konmasından ya da düşmanların bana baskın yapmasından korkarak çukur yerlere konmam"),
    S_(mk("فَهُوَ كِنَايَةٌ عَنْ كَرَمِهِ وَشَجَاعَتِهِ: نَفَى الِاسْتِتَارَ وَأَرَادَ لَازِمَهُ، أَنَّهُ يَبْرُزُ لِلضِّيفَانِ وَلِلْأَعْدَاءِ", "So it is a kinaya for his generosity and courage: he denies taking cover and means what follows from it — that he stands out in the open for guests and for foes", "Bu, cömertliğinden ve cesaretinden kinâyedir: gizlenmeyi nefyetmiş, lâzımını — misafirlere ve düşmanlara açıkta durduğunu — kastetmiştir", "kinaya")), p=HEMI),
 PT("وَلٰكِنْ", "lakin", mk("حَرْفُ اسْتِدْرَاكٍ مُهْمَلٌ لَا عَمَلَ لَهُ", "A particle of correction; it governs nothing", "İstidrâk harfi; amel etmez", "aw-imma-am-la-bal-lakin-fil-kafiya"), pre="wa"),
 PT("مَتَى", "mata", MATA_SH + mk("، مُتَعَلِّقٌ بِـ«يَسْتَرْفِدِ»", ", hanging on «يَسْتَرْفِدِ»", ", «يَسْتَرْفِدِ»e müteallik")),
 VB("يَسْتَرْفِدِ", "istarfada", "jz", nt("وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ؛ الِاسْتِرْفَادُ: الِاسْتِعَانَةُ", "it takes a kasra because two quiescents meet; الاِسْتِرْفَاد: asking for help", "iki sâkin karşılaştığı için kesrelenmiştir; الاِسْتِرْفَاد: yardım istemek"), by="shart", g=["form-x-verbs"]),
 NO("الْقَوْمُ", "qawm", "fail"),
 VB("أَرْفِدِ", "arfada", "jz", JM("jz"), nt("الرِّفْدُ وَالْإِرْفَادُ: الْإِعَانَةُ", "الرِّفْد and الإِرْفَاد: helping", "الرِّفْد ve الإِرْفَاد: yardım etmek"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «يَسْتَرْفِدِ» وَ«أَرْفِدِ» الِاشْتِقَاقُ", "a figure joined to jinas: «يَسْتَرْفِدِ» and «أَرْفِدِ» are brought together by derivation", "cinâsa mülhak: «يَسْتَرْفِدِ» ile «أَرْفِدِ»yi iştikak bir araya getirmiştir"), who="أَنَا", by="jawab", q=True, g=["form-iv-verbs", "mulhaq-bil-jinas"]),
])
V(46, "If you seek me in the circle of the tribe, you will find me; and if you hunt me in the wine-shops, you will catch me.",
  "Beni kavmin meclis halkasında ararsan bulursun; meyhanelerde avlamaya kalkarsan yakalarsın.", [
 PT("فَإِنْ", "in-shartiyya", IN_SH, nt("وَيُرْوَى بِالْوَاوِ (التِّبْرِيزِيُّ)", "it is also transmitted with waw (al-Tibrīzī)", "vâv ile de rivayet edilir (Tebrîzî)"), pre="fa-ist"),
 VB("تَبْغِنِي", "bagha", "jz-ill", nt("الْبُغَاءُ: الطَّلَبُ", "البُغَاء: seeking", "البُغَاء: aramak"), who="أَنْتَ", by="shart", enc="نِي", g=["naqis-verbs"]),
 HJ("فِي", "fi"),
 NO("حَلْقَةِ", "halqa", R("maj") + MUD, ON("تَبْغِ"), nt("تُجْمَعُ عَلَى الْحَلَقِ بِفَتْحِ الْحَاءِ وَاللَّامِ، وَهُوَ مِنَ الشَّوَاذِّ، وَعَلَى الْحِلَقِ (الزَّوْزَنِيُّ)", "its plural is الحَلَق, with fatha on ha and lam — a rare form — and الحِلَق (al-Zawzanī)", "çoğulu hâ ve lâm'ın fethasıyla الحَلَق'tır — şâz bir şekil — ve الحِلَق (Zevzenî)")),
 NO("الْقَوْمِ", "qawm", "mi"),
 VB("تَلْقَنِي", "laqiya", "jz-ill", JM("jz"), who="أَنْتَ", by="jawab", enc="نِي", g=["naqis-verbs"], p=HEMI),
 PT("وَإِنْ", "in-shartiyya", IN_SH, pre="wa"),
 VB("تَقْتَنِصْنِي", "iqtanasa", "jz",
    HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي الْفِعْلِ: شُبِّهَ طَلَبُهُ بِالِاقْتِنَاصِ، وَاسْتُعِيرَ لَهُ «تَقْتَنِصْ» وَ«تَصْطَدْ» (وَفَسَّرَهُ الزَّوْزَنِيُّ: «وَإِنْ تَطْلُبْنِي فِي بُيُوتِ الْخَمَّارِينَ تَصْطَدْنِي»)", "a dependent istiara in the verb: seeking him is likened to hunting, and «تَقْتَنِصْ» and «تَصْطَدْ» are borrowed for it (al-Zawzanī renders: «if you look for me in the wine-sellers' houses, you will catch me»)", "fiilde istiâre-i tebeiyye: onu aramak avlamaya benzetilmiş ve ona «تَقْتَنِصْ» ile «تَصْطَدْ» iğreti alınmıştır (Zevzenî: «beni meyhanecilerin evlerinde ararsan yakalarsın»)"), who="أَنْتَ", by="shart", enc="نِي", g=["form-viii-verbs", "istiara-tabaiyya", "istiara"]),
 HJ("فِي", "fi"),
 NO("الْحَوَانِيتِ", "hanut", R("maj"), ON("تَقْتَنِصْ"), nt("الْحَانُوتُ: بَيْتُ الْخَمَّارِ، وَالْجَمْعُ الْحَوَانِيتُ", "الحَانُوت: the wine-seller's house", "الحَانُوت: şarapçının evi, meyhane", "jam-taksir")),
 VB("تَصْطَدِ", "istada", "jz", JM("jz"), nt("وَالْمَفْعُولُ مَحْذُوفٌ، أَيْ: تَصْطَدْنِي (الزَّوْزَنِيُّ)؛ يُرِيدُ أَنْ يَجْمَعَ بَيْنَ الْجِدِّ وَالْهَزْلِ", "the object is left out — «you will catch me» (al-Zawzanī); he means he joins earnest and jest", "mef'ûl mahzûftur: «beni yakalarsın» (Zevzenî); ciddiyetle şakayı bir arada tuttuğunu kasteder", "hadhf-al-maful"), who="أَنْتَ", by="jawab", q=True, g=["form-viii-verbs", "hollow-verbs"]),
])
V(47, "And if the whole tribe meets together, you will find me tracing myself to the summit of the noble house, the one men resort to.",
  "Bütün kabile bir araya gelirse, beni o şerefli, kendisine başvurulan hanedanın zirvesine nisbet ederken bulursun.", [
 PT("وَإِنْ", "in-shartiyya", IN_SH, pre="wa"),
 VB("يَلْتَقِ", "iltaqa", "jz-ill", by="shart", g=["form-viii-verbs", "naqis-verbs"]),
 NO("الْحَيُّ", "hayy-tribe", "fail"),
 NO("الْجَمِيعُ", "jami", NA("الْحَيُّ", "raf"), nt("وَفِيهِ مَعْنَى التَّوْكِيدِ، وَقِيلَ: تَوْكِيدٌ لِـ«الْحَيُّ» وَ«أَلْ» عِوَضٌ مِنَ الضَّمِيرِ، أَيْ: جَمِيعُهُمْ (الدُّرَّةُ)", "it carries the sense of emphasis; it is also said to be an emphasis of «الْحَيُّ», the article standing for the pronoun — «all of them» (al-Durra)", "te'kîd anlamı taşır; «الْحَيُّ»nın te'kîdi olduğu ve «أَلْ»in zamirden bedel olduğu da söylenmiştir: «hepsi» (Dürre)")),
 VB("تُلَاقِنِي", "laqa-meet", "jz-ill", JM("jz"), who="أَنْتَ", by="jawab", enc="نِي", g=["form-iii-verbs", "naqis-verbs"], p=HEMI),
 HJ("إِلَى", "ila"),
 NO("ذِرْوَةِ", "dhirwa", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ، أَيْ: أَعْتَزِي إِلَى ذِرْوَةِ الْبَيْتِ، فَحَذَفَ الْفِعْلَ لِدَلَالَةِ الْحَرْفِ عَلَيْهِ (الزَّوْزَنِيُّ)، وَالْجُمْلَةُ حَالٌ مِنْ يَاءِ الْمُتَكَلِّمِ، أَيْ: مُنْتَمِيًا (الدُّرَّةُ)", "the phrase hangs on a verb left out — «tracing myself to the summit of the house» — the verb dropped because the preposition points to it (al-Zawzanī); that clause is a hal of the ya of «تُلَاقِنِي»: «claiming descent» (al-Durra)", "câr-mecrûr mahzûf bir fiile müteallik: «hanedanın zirvesine nisbet ederek»; harf ona delâlet ettiği için fiil hazfedilmiştir (Zevzenî); bu cümle mütekellim yâsından hâldir: «nisbet ederken» (Dürre)", "hadhf-wa-taqdir"),
    S_(mk("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: ذِرْوَةُ الْبَيْتِ لِأَعْلَى الشَّرَفِ (قَالَ الزَّوْزَنِيُّ: «أَيْ إِلَى أَعْلَى الشَّرَفِ، يُرِيدُ أَنَّهُ أَوْفَاهُمْ حَظًّا مِنَ الْحَسَبِ وَأَعْلَاهُمْ سَهْمًا مِنَ النَّسَبِ»)", "There is an explicit istiara: the summit of the house for the height of honour (al-Zawzanī: «that is, to the highest honour — he means he has the fullest share of them all in noble deeds and the highest in lineage»)", "İstiâre-i tasrîhiyye vardır: hanedanın zirvesi, şerefin en yücesi için (Zevzenî: «yani şerefin en yücesine; asalette en bol nasibi, soyda en yüksek payı onun olduğunu kasteder»)", "istiara", "aqsam-al-istiara"))),
 NO("الْبَيْتِ", "bayt", "mi"),
 NO("الشَّرِيفِ", "sharif", NA("الْبَيْتِ", "jarr")),
 NO("الْمُصَمَّدِ", "musammad", NA("الْبَيْتِ", "jarr", "", "2"), nt("الصَّمْدُ: الْقَصْدُ، وَالتَّصْمِيدُ مُبَالَغَةُ الصَّمْدِ (الزَّوْزَنِيُّ)، أَيِ: الَّذِي يُقْصَدُ كَثِيرًا", "الصَّمْد is resorting to, and التَّصْمِيد its intensive (al-Zawzanī) — «much resorted to»", "الصَّمْد: yönelmek; التَّصْمِيد onun mübalağasıdır (Zevzenî) — «kendisine çokça başvurulan»", "ism-maful")),
])
# ---- The boon companions, the singing girl, and the outcast: verses 48–54 -----------------------------------------------
QAYNA = ("الْقَيْنَةِ", "the singing girl", "şarkıcı câriyeye")
V(48, "My boon companions are fair-faced, like the stars; and a singing girl comes to us at evening, in a striped cloak or a saffron-dyed robe.",
  "İçki arkadaşlarım yıldızlar gibi ak yüzlüdür; akşamları da bize, çizgili bir hırka ya da safranla boyanmış bir elbise içinde şarkıcı bir câriye gelir.", [
 NO("نَدَامَايَ", "nadman", R("mub", "maq"), JM("ist"), nt("جَمْعُ نَدْمَانَ، وَهُوَ النَّدِيمُ", "the plural of نَدْمَان, a boon companion", "«نَدْمَان»ın cem'i: içki arkadaşı, nedim", "jam-taksir"), enc="يَ"),
 NO("بِيضٌ", "bid-white", "kh", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ (الدُّرَّةُ)", "it describes a noun left out (al-Durra)", "mahzûf bir mevsûfun sıfatıdır (Dürre)", "hadhf-wa-taqdir"),
    ZW("وَصَفَهُمْ بِالْبَيَاضِ تَلْوِيحًا إِلَى أَنَّهُمْ أَحْرَارٌ وَلَدَتْهُمْ حَرَائِرُ … أَوْ لِإِشْرَاقِ أَلْوَانِهِمْ إِذْ لَمْ يَلْحَقْهُمْ عَارٌ، أَوْ لِنَقَائِهِمْ مِنَ الْعُيُوبِ، أَوْ لِاشْتِهَارِهِمْ", "he calls them white as an allusion (talwīḥ) to their being free men born of free women … or for the brightness of their faces, no shame having touched them, or for their freedom from faults, or for their renown", "onları beyazlıkla vasfetmesi, hür kadınlardan doğmuş hür kimseler olduklarına telvîhtir … ya da hiçbir ar onlara bulaşmadığı için yüzlerinin parlaklığından, ya da kusurdan arı olmalarından, ya da meşhur olmalarından dolayıdır"),
    S_(mk("فَهُوَ كِنَايَةٌ مِنْ نَوْعِ التَّلْوِيحِ، سَمَّاهَا الزَّوْزَنِيُّ بِاسْمِهَا", "So it is a kinaya of the kind called talwīḥ — al-Zawzanī uses the very name", "Bu, telvîh türünden bir kinâyedir; Zevzenî onu adıyla anar", "kinaya", "tarid-talwih-ramz"))),
 NO("كَالنُّجُومِ", "najm", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بِيضٌ» لِأَنَّهُ جَمْعُ «أَبْيَضَ» وَهُوَ صِفَةٌ مُشَبَّهَةٌ، وَقِيلَ: بِمَحْذُوفٍ نَعْتٍ لَهُ (الدُّرَّةُ)", "the phrase hangs on «بِيضٌ», the plural of أَبْيَض, a ṣifa mushabbaha; also said: on an omitted adjective of it (al-Durra)", "câr-mecrûr, sıfat-ı müşebbehe olan «أَبْيَض»ın cem'i «بِيضٌ»a müteallik; onun mahzûf na'tına müteallik olduğu da söylenmiştir (Dürre)", "jam-taksir"),
    TSB("mf", ("نَدَامَاهُ", "his boon companions", "içki arkadaşları"), ("النُّجُومُ", "the stars", "yıldızlar"), "ka", ("الْبَيَاضُ وَالْإِشْرَاقُ، وَهُوَ مَذْكُورٌ فِي «بِيضٌ»", "whiteness and brightness, named in «بِيضٌ»", "beyazlık ve parlaklık — «بِيضٌ»da zikredilmiştir"), src="h"), pre="ka", g=TSB_TAGS),
 NO("وَقَيْنَةٌ", "qayna", R("mub"), nt("خَبَرُهُ مَحْذُوفٌ، أَيْ: وَلَنَا قَيْنَةٌ (الدُّرَّةُ)؛ الْقَيْنَةُ: الْجَارِيَةُ الْمُغَنِّيَةُ", "its predicate is left out — «and we have a singing girl» (al-Durra); القَيْنَة: a slave-girl who sings", "haberi mahzûftur: «bizim bir şarkıcı câriyemiz vardır» (Dürre); القَيْنَة: şarkı söyleyen câriye", "hadhf-wa-taqdir"), pre="wa", p=HEMI),
 VB("تَرُوحُ", "raha-become", "mud", JM("sifa", "قَيْنَةٌ", "raf"), nt("أَيْ: تَأْتِينَا رَوَاحًا، عَشِيًّا", "that is, she comes to us at evening", "yani bize akşam vakti gelir"), who=("هِيَ", "قَيْنَةٌ"), g=["hollow-verbs"]),
 PJ("عَلَيْنَا", "عَلَيْ", "ala", "نَا", ON("تَرُوحُ"), nt("وَعِنْدَ التِّبْرِيزِيِّ «إِلَيْنَا»", "al-Tibrīzī has «إِلَيْنَا»", "Tebrîzî'de «إِلَيْنَا»")),
 NO("بَيْنَ", "bayna", R("zm") + MUD, nt("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «تَرُوحُ»، أَيْ: لَابِسَةً (الدُّرَّةُ)", "it hangs on an omitted hal of the doer of «تَرُوحُ» — «wearing» (al-Durra)", "«تَرُوحُ»nun fâilinden mahzûf hâle müteallik: «giymiş olarak» (Dürre)")),
 NO("بُرْدٍ", "burd", "mi"),
 NO("وَمُجْسَدِ", "mujsad", AT("بُرْدٍ", "jarr"), nt("الْمُجْسَدُ: الثَّوْبُ الْمَصْبُوغُ بِالْجِسَادِ وَهُوَ الزَّعْفَرَانُ، وَقِيلَ: الْمُشْبَعُ الصِّبْغِ", "المُجْسَد: a robe dyed with الجِسَاد, saffron; also said: one steeped full in dye", "المُجْسَد: الجِسَاد yani safranla boyanmış elbise; boyası doymuş elbise olduğu da söylenmiştir", "ism-maful"), pre="wa", q=True),
])
V(49, "Wide is the opening of her collar, gentle she is under the companions' touch, soft and fine of skin where she is bared.",
  "Yakasının ağzı geniştir; nedimlerin dokunuşuna karşı yumuşak davranır; açık kalan yerlerinin teni ince ve yumuşaktır.", [
 NO("رَحِيبٌ", "rahib", NA("قَيْنَةٌ", "raf", "", "2"), nt("وَذُكِّرَ لِأَنَّهُ نَعْتٌ سَبَبِيٌّ رَفَعَ «قِطَابُ»؛ وَيَجُوزُ أَنْ يَكُونَ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: هِيَ رَحِيبٌ (الدُّرَّةُ)؛ الرَّحْبُ وَالرَّحِيبُ وَاحِدٌ: الْوَاسِعُ", "it is masculine because it is a sababī adjective whose doer is «قِطَابُ»; it may also be the predicate of an omitted mubtada (al-Durra); الرَّحْب and الرَّحِيب are one: wide", "«قِطَابُ»u ref eden sebebî na't olduğu için müzekkerdir; mahzûf mübtedanın haberi de olabilir (Dürre); الرَّحْب ile الرَّحِيب birdir: geniş", "sifa-mushabbaha")),
 NO("قِطَابُ", "qitab", R("fail") + MUD, nt("لِـ«رَحِيبٌ»؛ قِطَابُ الْجَيْبِ: مَخْرَجُ الرَّأْسِ مِنْهُ", "of «رَحِيبٌ»; قِطَاب الجَيْب: the opening through which the head goes", "«رَحِيبٌ»un fâili; قِطَاب الجَيْب: başın çıktığı yaka ağzı")),
 NO("الْجَيْبِ", "jayb", "mi", nt("الْجَيْبُ: فَتْحَةُ الثَّوْبِ عِنْدَ الصَّدْرِ", "الجَيْب: the opening of a garment at the breast", "الجَيْب: elbisenin göğüs açıklığı, yaka")),
 PJ("مِنْهَا", "مِنْ", "min", "هَا", ONH("hal", "الْجَيْبِ"), ref="قَيْنَةٌ"),
 NO("رَفِيقَةٌ", "rafiq", NA("قَيْنَةٌ", "raf", "", "3"), nt("أَيْ: رَفِيقَةٌ عَلَى جَسِّ النَّدَامَى إِيَّاهَا (الزَّوْزَنِيُّ)", "that is, gentle when the companions touch her (al-Zawzanī)", "yani nedimlerin kendisine dokunmasına karşı yumuşak (Zevzenî)", "sifa-mushabbaha"), p=HEMI),
 NO("بِجَسِّ", "jass", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَفِيقَةٌ» لِأَنَّهُ صِفَةٌ مُشَبَّهَةٌ؛ الْجَسُّ: اللَّمْسُ", "the phrase hangs on «رَفِيقَةٌ», a ṣifa mushabbaha; الجَسّ: touching", "câr-mecrûr sıfat-ı müşebbehe olan «رَفِيقَةٌ»ya müteallik; الجَسّ: dokunmak", "masdar"), pre="bi"),
 NO("النَّدَامَى", "nadman", R("mi", "maq"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "the masdar annexed to its doer", "masdarın fâiline izâfeti", "jam-taksir")),
 NO("بَضَّةُ", "badd", NA("قَيْنَةٌ", "raf", "", "4") + MUD, nt("الْبَضَاضَةُ: نُعُومَةُ الْبَدَنِ وَرِقَّةُ الْجِلْدِ", "البَضَاضَة: softness of body and fineness of skin", "البَضَاضَة: bedenin yumuşaklığı ve tenin inceliği", "sifa-mushabbaha")),
 NO("الْمُتَجَرَّدِ", "mutajarrad", "mi", nt("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا؛ الْمُتَجَرَّدُ: حَيْثُ تَتَجَرَّدُ، أَيْ: مَا يَعْرَى مِنْ جَسَدِهَا (الزَّوْزَنِيُّ)", "the ṣifa mushabbaha annexed to its doer; المُتَجَرَّد: where she is bared — what of her body is uncovered (al-Zawzanī)", "sıfat-ı müşebbehenin fâiline izâfeti; المُتَجَرَّد: açıldığı yer — bedeninin açık kalan kısmı (Zevzenî)", "idafa-lafziyya", "ism-al-zaman-wal-makan")),
])
V(50, "When we say «Let us hear you», she sets about it for us, at her own easy pace, languid-eyed, without straining.",
  "«Bize şarkı söyle» dediğimizde, ağır ağır, baygın bakışlı, zorlamadan söylemeye koyulur.", [
 PT("إِذَا", "idha", IDHA_SH, JM("ist")),
 PT("نَحْنُ", "nahnu", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ بَعْدَهُ (الدُّرَّةُ)", "A detached pronoun built on damma, in the seat of raf' as the doer of a verb left out that the next verb explains (al-Durra)", "Damme üzere mebnî munfasıl zamir; sonraki fiilin tefsir ettiği mahzûf fiilin fâili olarak mahallen merfû (Dürre)", "hadhf-wa-taqdir"), pos="pron"),
 VB("قُلْنَا", "qala", "madi-na", nt("وَالْجُمْلَةُ مُفَسِّرَةٌ لَا مَحَلَّ لَهَا", "the clause explains the omitted verb and has no seat", "cümle tefsiriyyedir, mahalli yoktur"), g=["hollow-verbs"]),
 VB("أَسْمِعِينَا", "asmaa", "amr-nun", JM("maqul"), nt("وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ، أَيْ: غِنَاءَكِ (الدُّرَّةُ)؛ أَسْمِعِينَا: أَيْ غَنِّينَا (الزَّوْزَنِيُّ)", "its second object is left out — «your singing» (al-Durra); أَسْمِعِينَا: sing to us (al-Zawzanī)", "ikinci mef'ûlü mahzûftur: «şarkını» (Dürre); أَسْمِعِينَا: bize şarkı söyle (Zevzenî)", "hadhf-al-maful"), enc="نَا", g=["form-iv-verbs", "mafulayn"]),
 VB("انْبَرَتْ", "inbara", "madi-fh", JM("jawab", "إِذَا"), nt("الِانْبِرَاءُ: الِاعْتِرَاضُ لِلشَّيْءِ وَالْأَخْذُ فِيهِ", "الاِنْبِرَاء: turning to a thing and setting about it", "الاِنْبِرَاء: bir işe yönelip ona koyulmak"), who=("هِيَ", QAYNA), g=["form-vii-verbs", "naqis-verbs"]),
 PJ("لَنَا", "لَ", "li", "نَا", ON("انْبَرَتْ"), p=HEMI),
 HJ("عَلَى", "ala"),
 NO("رِسْلِهَا", "risl", R("maj"), ON("انْبَرَتْ"), nt("عَلَى رِسْلِهَا: عَلَى تُؤَدَتِهَا وَوَقَارِهَا", "عَلَى رِسْلِهَا: at her leisure, with her gravity", "عَلَى رِسْلِهَا: ağır başlılıkla, acele etmeden"), enc="هَا"),
 NO("مَطْرُوقَةً", "matruqa", mk("حَالٌ مِنْ فَاعِلِ «انْبَرَتْ» الْمُسْتَتِرِ مَنْصُوبٌ بِالْفَتْحَةِ", "A hal of the hidden doer of «انْبَرَتْ», in nasb by the fatha", "«انْبَرَتْ»in gizli fâilinden hâl, fetha ile mansûb", "hal"), nt("الْمَطْرُوقَةُ: الَّتِي بِهَا ضَعْفٌ، وَيُرْوَى «مَطْرُوفَةً»: كَأَنَّهَا أُصِيبَ طَرْفُهَا لِفُتُورِ نَظَرِهَا (الزَّوْزَنِيُّ)", "المَطْرُوقَة: languid, with a weakness in her; it is also transmitted «مَطْرُوفَةً» — as though something had struck her eye, so languid is her glance (al-Zawzanī)", "المَطْرُوقَة: üzerinde bir gevşeklik bulunan; «مَطْرُوفَةً» diye de rivayet edilir — bakışının baygınlığından sanki gözüne bir şey değmiş gibi (Zevzenî)", "ism-maful")),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("تَشَدَّدِ", "tashaddada", "jz", nt("أَصْلُهُ «تَتَشَدَّدْ» فَحُذِفَتْ إِحْدَى التَّاءَيْنِ اسْتِثْقَالًا، وَمِثْلُهُ {تَنَزَّلُ الْمَلَائِكَةُ} (الزَّوْزَنِيُّ)؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ مِنْ فَاعِلِ «انْبَرَتْ»", "its full form is «تَتَشَدَّدْ», one ta dropped as too heavy, as in «تَنَزَّلُ الْمَلَائِكَةُ» (al-Zawzanī); the clause is a second hal of the doer of «انْبَرَتْ», in the seat of nasb", "aslı «تَتَشَدَّدْ»dır; ağırlıktan iki tâ'dan biri düşmüştür, {تَنَزَّلُ الْمَلَائِكَةُ} gibi (Zevzenî); cümle «انْبَرَتْ»in fâilinden ikinci hâl olarak mahallen mansûb", "al-hal-jumla-wa-rabituha"), who=("هِيَ", QAYNA), by="lam", q=True, g=["form-v-verbs"]),
])
V(51, "When she trills in her voice, you would think her voice the answering cries of camels that have lost a young one, mourning over a spring calf dead.",
  "Sesini titretip yinelediğinde, sesini, ölmüş bir bahar yavrusunun başında birbirine karşılık veren yavrusunu yitirmiş develerin iniltisi sanırsın.", [
 PT("إِذَا", "idha", IDHA_SH, JM("ist")),
 VB("رَجَّعَتْ", "rajja", "madi-f", JM("mudaf", "إِذَا"), nt("التَّرْجِيعُ: تَرْدِيدُ الصَّوْتِ وَتَغْرِيدُهُ", "التَّرْجِيع: turning the voice over and over, trilling", "التَّرْجِيع: sesi tekrar tekrar döndürüp şakımak"), who=("هِيَ", QAYNA), g=["form-ii-verbs"]),
 HJ("فِي", "fi"),
 NO("صَوْتِهَا", "sawt", R("maj"), ON("رَجَّعَتْ"), enc="هَا"),
 VB("خِلْتَ", "khala-think", "madi-ta", JM("jawab", "إِذَا"), g=["hollow-verbs", "zanna-wa-akhawatuha"]),
 NO("صَوْتَهَا", "sawt", "maf1", enc="هَا", p=HEMI),
 NO("تَجَاوُبَ", "tajawub", R("maf2") + MUD, nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "the masdar annexed to its doer", "masdarın fâiline izâfeti", "masdar"),
    TSB("bl", ("صَوْتُهَا فِي التَّحْزِينِ", "her voice in its grieving", "hüzünlendirmesinde onun sesi"), ("أَصْوَاتُ نُوقٍ تَصِيحُ عَلَى وَلَدٍ هَالِكٍ", "the cries of camels mourning a dead young one", "ölmüş yavrularının başında bağıran develerin sesleri"), src="z"), g=TSB_TAGS),
 NO("أَظْآرٍ", "zir", "mi", nt("الظِّئْرُ: الَّتِي لَهَا وَلَدٌ، وَالْجَمْعُ الْأَظْآرُ", "الظِّئْر: one that has a young one — the plural الأَظْآر", "الظِّئْر: yavrusu olan — çoğulu الأَظْآر", "jam-taksir")),
 HJ("عَلَى", "ala"),
 NO("رُبَعٍ", "ruba", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْمَصْدَرِ «تَجَاوُبَ» (الدُّرَّةُ)؛ الرُّبَعُ: مَا وُلِدَ مِنَ الْإِبِلِ فِي أَوَّلِ النِّتَاجِ", "the phrase hangs on the masdar «تَجَاوُبَ» (al-Durra); الرُّبَع: a camel-calf born at the start of the foaling season", "câr-mecrûr «تَجَاوُبَ» masdarına müteallik (Dürre); الرُّبَع: doğum mevsiminin başında doğan deve yavrusu"),
    S_(mk("وَعَلَى قَوْلٍ آخَرَ: الْأَظْآرُ النِّسَاءُ، وَ«الرُّبَعُ» مُسْتَعَارٌ لِوَلَدِ الْإِنْسَانِ، فَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ (الزَّوْزَنِيُّ: «وَالرُّبَعُ مُسْتَعَارٌ لِوَلَدِ الْإِنْسَانِ، فَشَبَّهَ صَوْتَهَا فِي التَّحْزِينِ وَالتَّرْقِيقِ بِأَصْوَاتِ النَّوَادِبِ وَالنَّوَائِحِ عَلَى صَبِيٍّ هَالِكٍ»)", "On another reading the أَظْآر are women and «الرُّبَع» is borrowed for a human child — an explicit istiara (al-Zawzanī: «الرُّبَع is borrowed for a man's child: he likens her voice, in its grief and tenderness, to the voices of women wailing over a dead boy»)", "Bir başka görüşe göre الأَظْآر kadınlardır ve «الرُّبَع» insan yavrusu için iğreti alınmıştır; istiâre-i tasrîhiyye vardır (Zevzenî: «الرُّبَع insan çocuğu için müsteârdır; onun sesini hüzün ve incelikte, ölmüş bir çocuğun başında ağıt yakan kadınların seslerine benzetmiştir»)", "istiara", "aqsam-al-istiara")), pre=None),
 NO("رَدِ", "radin", NA("رُبَعٍ", "jarr", "manh"), nt("وَالْكَسْرَةُ الظَّاهِرَةُ عَلَى الدَّالِ لِلْقَافِيَةِ، وَحَقُّهُ «رَدٍ» بِالتَّنْوِينِ (الدُّرَّةُ)؛ الرَّدَى: الْهَلَاكُ، رَدِيَ يَرْدَى", "the kasra seen on the dal is the rhyme's — by rule «رَدٍ», with tanwin (al-Durra); الرَّدَى: perishing — رَدِيَ يَرْدَى", "dâl'daki görünen kesre kafiye içindir; aslı tenvinle «رَدٍ»dir (Dürre); الرَّدَى: helâk olmak — رَدِيَ يَرْدَى", "al-qafiya", "sifa-mushabbaha")),
])
V(52, "And still my drinking of wines and my pleasure, my selling and my spending of what I had newly gained and what I had inherited,",
  "Şarap içmem, zevkim, satışım, yeni kazandığımı da miras kalanı da harcamam hiç durmadı —", [
 PT("وَمَا", "ma-nafiya", MA_NAFY, JM("ist"), pre="wa-ist"),
 VB("زَالَ", "zala-ant", "madi", nt("نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ»، وَخَبَرُهُ «إِلَى أَنْ…» فِي الْبَيْتِ ٥٣، فَفِي الْبَيْتَيْنِ تَضْمِينٌ (الدُّرَّةُ)", "it is defective, a sister of كَانَ; its predicate is «إِلَى أَنْ…» in v. 53, so the two verses are run on (tadmin) (al-Durra)", "nâkıstır, «كَانَ»nin kardeşi; haberi 53. beyitteki «إِلَى أَنْ…»dir; iki beyitte tazmîn vardır (Dürre)", "kana-wa-akhawatuha"), g=["hollow-verbs"]),
 NO("تَشْرَابِي", "tashrab", R("ism:زَالَ", "yam"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ التَّشْرَابُ: الشُّرْبُ، وَ«تَفْعَالٌ» مِنْ أَوْزَانِ الْمَصَادِرِ كَالتَّقْتَالِ (الزَّوْزَنِيُّ)", "the masdar annexed to its doer; التَّشْرَاب: drinking — تَفْعَال is a pattern of masdars, like التَّقْتَال (al-Zawzanī)", "masdarın fâiline izâfeti; التَّشْرَاب: içmek — «تَفْعَال» masdar vezinlerindendir, التَّقْتَال gibi (Zevzenî)", "masdar"), enc="ي"),
 NO("الْخُمُورَ", "khamr", "maf", nt("لِلْمَصْدَرِ «تَشْرَابِي»", "of the masdar «تَشْرَابِي»", "«تَشْرَابِي» masdarının mef'ûlü", "amal-ism-al-tafdil-wal-masdar", "jam-taksir")),
 NO("وَلَذَّتِي", "ladhdha", AT("تَشْرَابِي", "raf", "yam"), enc="ي", pre="wa", p=HEMI),
 NO("وَبَيْعِي", "bay", AT("تَشْرَابِي", "raf", "yam"), enc="ي", pre="wa"),
 NO("وَإِنْفَاقِي", "infaq", AT("تَشْرَابِي", "raf", "yam"), enc="ي", pre="wa"),
 NO("طَرِيفِي", "tarif-wealth", R("maf", "yam"), nt("لِلْمَصْدَرِ «إِنْفَاقِي»؛ الطَّرِيفُ وَالطَّارِفُ: الْمَالُ الْحَدِيثُ", "of the masdar «إِنْفَاقِي»; الطَّرِيف and الطَّارِف: newly gained wealth", "«إِنْفَاقِي» masdarının mef'ûlü; الطَّرِيف ve الطَّارِف: yeni kazanılmış mal", "amal-ism-al-tafdil-wal-masdar"), enc="ي"),
 NO("وَمُتْلَدِي", "mutlad", AT("طَرِيفِي", "nasb", "yam"), nt("التَّلِيدُ وَالتِّلَادُ وَالْمُتْلَدُ: الْمَالُ الْقَدِيمُ الْمَوْرُوثُ", "التَّلِيد, التِّلَاد and المُتْلَد: old, inherited wealth", "التَّلِيد, التِّلَاد ve المُتْلَد: eski, miras kalmış mal"),
    HD("طِبَاقٌ بَيْنَ «طَرِيفِي» وَ«مُتْلَدِي»: الْمَالُ الْمُسْتَحْدَثُ وَالْمَالُ الْمَوْرُوثُ، وَبِهِمَا فَسَّرَهُمَا الزَّوْزَنِيُّ", "«طَرِيفِي» and «مُتْلَدِي» make a tibaq — wealth newly got against wealth inherited — as al-Zawzanī explains them", "«طَرِيفِي» ile «مُتْلَدِي» arasında tıbâk vardır: yeni kazanılmış mal ile miras kalan mal; Zevzenî ikisini böyle açıklar"), enc="ي", pre="wa", g=["tibaq"]),
])
V(53, "— until the whole clan shunned me, and I was set apart as the tarred camel is set apart.",
  "— sonunda bütün aşiret benden uzak durdu; katranlanmış devenin tecrit edildiği gibi tecrit edildim.", [
 HJ("إِلَى", "ila", nt("وَالْجَارُّ وَالْمَجْرُورُ (الْمَصْدَرُ الْمُؤَوَّلُ) مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «زَالَ» فِي الْبَيْتِ ٥٢ (الدُّرَّةُ)", "the phrase (with the masdar so made) hangs on the omitted predicate of «زَالَ» in v. 52 (al-Durra)", "câr-mecrûr (te'vil edilen masdar) 52. beyitteki «زَالَ»in mahzûf haberine müteallik (Dürre)")),
 PT("أَنْ", "an-masdariyya", MA_MASD, nt("وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ» وَالْفِعْلِ فِي مَحَلِّ جَرٍّ بِـ«إِلَى»", "the masdar made of أَنْ and the verb is in the seat of jarr by إِلَى", "«أَنْ» ile fiilden te'vil edilen masdar «إِلَى» ile mahallen mecrûr", "an-masdariyya")),
 VB("تَحَامَتْنِي", "tahama", "madi-fh", nt("التَّحَامِي: التَّجَنُّبُ وَالِاعْتِزَالُ", "التَّحَامِي: shunning, keeping away", "التَّحَامِي: kaçınmak, uzak durmak"), enc="نِي", g=["form-vi-verbs", "naqis-verbs"]),
 NO("الْعَشِيرَةُ", "ashira", "fail"),
 NO("كُلُّهَا", "kull", mk("تَوْكِيدٌ لِـ«الْعَشِيرَةُ» مَرْفُوعٌ بِالضَّمَّةِ", "An emphasis of «الْعَشِيرَةُ», in raf' by the damma", "«الْعَشِيرَةُ»nin te'kîdi, damme ile merfû", "tawkid"), enc="هَا", p=HEMI),
 VB("وَأُفْرِدْتُ", "afrada", "madi-tu", JM("atf", "تَحَامَتْنِي"), maj=True, pre="wa", g=["form-iv-verbs"]),
 NO("إِفْرَادَ", "ifrad", R("mm") + MUD, nt("مُبَيِّنٌ لِلنَّوْعِ، مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ وَالْفَاعِلُ مَحْذُوفٌ (الدُّرَّةُ)", "it shows the kind; the masdar is annexed to its object, the doer left out (al-Durra)", "türü bildirir; masdarın mef'ûlüne izâfetidir, fâil mahzûftur (Dürre)", "masdar"),
    TSB("bl", ("إِفْرَادُ الْعَشِيرَةِ إِيَّاهُ", "his clan's setting him apart", "aşiretinin onu tecrit etmesi"), ("إِفْرَادُ الْبَعِيرِ الْمَطْلِيِّ بِالْقَطِرَانِ", "the setting apart of the camel smeared with tar", "katranla sıvanmış devenin tecridi"), src="z"), g=TSB_TAGS),
 NO("الْبَعِيرِ", "bair", "mi"),
 NO("الْمُعَبَّدِ", "muabbad", NA("الْبَعِيرِ", "jarr"), nt("الْبَعِيرُ الْمُعَبَّدُ: الْمُذَلَّلُ الْمَطْلِيُّ بِالْقَطِرَانِ (الزَّوْزَنِيُّ)", "the مُعَبَّد camel: one made tame and smeared with tar (al-Zawzanī)", "مُعَبَّد deve: uysallaştırılmış, katranla sıvanmış deve (Zevzenî)", "ism-maful")),
])
V(54, "I saw the sons of the dusty earth not disowning me, nor the people of that great tent of hide, stretched wide.",
  "Toprağın oğullarının (yoksulların) beni yadırgamadığını gördüm; o uzanıp giden büyük deri çadırın sahipleri de (zenginler de) yadırgamadı.", [
 VB("رَأَيْتُ", "raa", "madi-tu", JM("ist"), g=["naqis-verbs"]),
 NO("بَنِي", "ibn", R("maf", "mulhaq") + MUD, NUN_IDF),
 NO("غَبْرَاءَ", "ghabra", R("mi", "fatha"), nt("لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ الْغَبْرَاءُ: صِفَةُ الْأَرْضِ جُعِلَتْ كَالِاسْمِ لَهَا (الزَّوْزَنِيُّ)", "it ends in the long feminine alif; الغَبْرَاء: an epithet of the earth made almost its name (al-Zawzanī)", "elif-i memdûde ile müennes olduğu için; الغَبْرَاء: yerin sıfatı olup neredeyse ismi gibi kullanılmıştır (Zevzenî)", "ism-mamdud"),
    S_(mk("وَ«بَنُو غَبْرَاءَ» كِنَايَةٌ عَنِ الْفُقَرَاءِ (قَالَ الزَّوْزَنِيُّ: «رَأَيْتُ الْفُقَرَاءَ الَّذِينَ لَصِقُوا بِالْأَرْضِ مِنْ شِدَّةِ الْفَقْرِ»)", "«The sons of the dusty one» is a kinaya for the poor (al-Zawzanī: «I saw the poor, who cling to the earth for very poverty»)", "«Toprağın oğulları» yoksullardan kinâyedir (Zevzenî: «yoksulluğun şiddetinden yere yapışmış fakirleri gördüm»)", "kinaya"))),
 PT("لَا", "la-nafiya", LA_NAFY),
 VB("يُنْكِرُونَنِي", "ankara", "mud5", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ«رَأَيْتُ» إِنْ كَانَتْ قَلْبِيَّةً، أَوْ حَالٌ مِنْ «بَنِي غَبْرَاءَ» إِنْ كَانَتْ بَصَرِيَّةً (الدُّرَّةُ)", "the clause is the second object of «رَأَيْتُ», in the seat of nasb, if the seeing is of the mind — or a hal of «بَنِي غَبْرَاءَ» if it is of the eye (al-Durra)", "«رَأَيْتُ» kalbî ise cümle onun ikinci mef'ûlü, basarî ise «بَنِي غَبْرَاءَ»dan hâl olarak mahallen mansûb (Dürre)"), enc="نِي", g=["form-iv-verbs"], p=HEMI),
 PT("وَلَا", "la-nafiya", mk("زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ", "Added, to strengthen the negation", "Nefyi pekiştirmek için zâid", "la-nafiya", "huruf-al-ziyada-fil-kafiya"), pre="wa"),
 NO("أَهْلُ", "ahl", mk("مَعْطُوفٌ عَلَى وَاوِ الْجَمَاعَةِ فِي «يُنْكِرُونَنِي» مَرْفُوعٌ بِالضَّمَّةِ، وَسَاغَ لِلْفَصْلِ بِالْمَفْعُولِ (الدُّرَّةُ)", "Conjoined to the plural waw of «يُنْكِرُونَنِي», in raf' by the damma — allowed because the object stands between (al-Durra)", "«يُنْكِرُونَنِي»deki cemi vâvına ma'tûf, damme ile merfû; araya mef'ûl girdiği için câiz olmuştur (Dürre)", "atf-nasaq") + MUD,
    S_(mk("وَهُمْ كِنَايَةٌ عَنِ الْأَغْنِيَاءِ (قَالَ الزَّوْزَنِيُّ: «وَرَأَيْتُ الْأَغْنِيَاءَ الَّذِينَ لَهُمْ بُيُوتُ الْأَدَمِ لَا يُنْكِرُونَنِي»)", "They are a kinaya for the rich (al-Zawzanī: «and I saw the rich, who have houses of hide, not disowning me»)", "Bunlar zenginlerden kinâyedir (Zevzenî: «deri çadırları olan zenginlerin de beni yadırgamadığını gördüm»)", "kinaya"))),
 PT("هٰذَاكَ", "dhaka", mk("الْهَاءُ لِلتَّنْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْكَافُ حَرْفُ خِطَابٍ", "The ha draws attention; ذَا is a demonstrative built on sukun, in the seat of jarr as the second term of the idafa; the kaf marks the one addressed", "Hâ tenbih içindir; ذَا sükûn üzere mebnî işaret ismi, muzâfun ileyh olarak mahallen mecrûr; kâf hitap harfidir", "asma-al-ishara", "idafa-definiteness"), pos="pron"),
 NO("الطِّرَافِ", "tiraf", BD("هٰذَاكَ", "jarr"), nt("أَوْ عَطْفُ بَيَانٍ عَلَيْهِ (الدُّرَّةُ)؛ الطِّرَافُ: الْبَيْتُ مِنَ الْأَدَمِ", "or an explaining apposition to it (al-Durra); الطِّرَاف: a tent of tanned hide", "ya da ona atf-ı beyândır (Dürre); الطِّرَاف: deriden çadır", "atf-bayan")),
 NO("الْمُمَدَّدِ", "mumaddad", NA("الطِّرَافِ", "jarr"),
    ZW("وَكَنَّى بِتَمْدِيدِهِ عَنْ عِظَمِهِ", "by its being stretched wide he means, by kinaya, its greatness", "uzatılmasıyla büyüklüğünü kinâye yoluyla anlatmıştır"), g=["ism-maful", "kinaya"]),
])
# ---- The reproacher; the three joys of a young man's life: verses 55–61 -------------------------------------------------
_CL["fa-tafri"] = ("الْفَاءُ لِلتَّفْرِيعِ، وَ", "The fa branches off from what was said; ", "Fâ tefrî' içindir; ", ("فَ", "fa", "conj"))
V(55, "O you who blame me for being present at the battle and for taking my share of pleasures — can you make me live for ever?",
  "Ey savaşa katılmamı ve zevklere erişmemi kınayan adam! Sen beni ölümsüz kılabilir misin?", [
 PT("أَلَا", "ala-tanbih", mk("حَرْفُ تَنْبِيهٍ وَاسْتِفْتَاحٍ", "A particle that calls for attention and opens the speech", "Tenbih ve istiftâh harfi", "huruf-tanbih"), JM("ist")),
 PT("أَيُّهٰذَا", "ayyuha", mk("أَيُّ مُنَادًى نَكِرَةٌ مَقْصُودَةٌ حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ، مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ؛ وَهَا حَرْفُ تَنْبِيهٍ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«أَيُّ» عَلَى لَفْظِهِ", "أَيُّ is a vocative, a particular indefinite, its يَا dropped, built on damma in the seat of nasb; هَا draws attention, and ذَا is a demonstrative built on sukun, in the seat of raf' as the adjective of أَيُّ by its form", "أَيُّ, nidâ harfi hazfedilmiş, kastedilen nekire münâdâ; damme üzere mebnî, mahallen mansûb; هَا tenbih harfi; ذَا sükûn üzere mebnî işaret ismi, lafzına göre «أَيُّ»nün na'tı olarak mahallen merfû", "vocative-munada", "asma-al-ishara"), pos="pron"),
 NO("اللَّائِمِي", "laim", mk("بَدَلٌ أَوْ عَطْفُ بَيَانٍ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ, "A badal or explaining apposition of the demonstrative, in raf' by a damma estimated before the speaker's ya", "İşaret isminden bedel ya da atf-ı beyân; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû", "badal", "ya-al-mutakallim"),
    nt("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ، وَهِيَ لَا تُفِيدُهُ تَعْرِيفًا فَاغْتُفِرَ دُخُولُ «أَلْ» عَلَيْهِ (الدُّرَّةُ)", "an active participle annexed to its object — an annexation that does not make it definite, so the article is let pass on it (al-Durra)", "ism-i fâilin mef'ûlüne izâfeti; bu izâfet onu marife yapmadığı için «أَلْ» girmesine göz yumulmuştur (Dürre)", "idafa-lafziyya", "ism-fail"), enc="ي"),
 VB("أَحْضُرَ", "hadara", "ns", nt("عَلَى رِوَايَةِ الْكُوفِيِّينَ، وَسَهَّلَ حَذْفَ «أَنْ» ذِكْرُهَا فِي الْمَعْطُوفِ «وَأَنْ أَشْهَدَ»؛ وَيُرْوَى بِالرَّفْعِ «أَحْضُرُ» وَهُوَ رِوَايَةُ الْبَصْرِيِّينَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِـ«عَنْ» مَحْذُوفَةٍ مُتَعَلِّقَةٍ بِـ«اللَّائِمِي»، أَيْ: عَنْ حُضُورِ الْوَغَى (الدُّرَّةُ)", "so the Kufans' reading — the dropping of أَنْ eased by its presence in «وَأَنْ أَشْهَدَ»; the Basrans read it in raf', «أَحْضُرُ»; the masdar is in jarr by an omitted عَنْ hanging on «اللَّائِمِي» — «for being present at the battle» (al-Durra)", "Kûfelilerin rivayetine göredir; ma'tûftaki «وَأَنْ أَشْهَدَ» onu hazfetmeyi kolaylaştırmıştır; Basralılar ref' ile «أَحْضُرُ» okur; te'vil edilen masdar «اللَّائِمِي»ye müteallik mahzûf «عَنْ» ile mecrûrdur: «savaşa katılmaktan (dolayı)» (Dürre)", "nawasib-wa-jawazim-al-mudari"), who="أَنَا", by=("بِأَنْ مَحْذُوفَةٍ", "by an أَنْ left out", "Mahzûf أَنْ ile")),
 NO("الْوَغَى", "wagha", R("maf", "maq"), nt("الْوَغَى: أَصْلُهُ صَوْتُ الْأَبْطَالِ فِي الْحَرْبِ، ثُمَّ جُعِلَ اسْمًا لِلْحَرْبِ (الزَّوْزَنِيُّ)", "الوَغَى: first the cry of the champions in battle, then made a name for battle itself (al-Zawzanī)", "الوَغَى: aslı savaşta kahramanların sesidir, sonra savaşın adı olmuştur (Zevzenî)"), p=HEMI),
 PT("وَأَنْ", "an-masdariyya", mk("حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ", "The masdar-making particle that governs nasb", "Masdar ve nasb harfi", "an-masdariyya"), pre="wa"),
 VB("أَشْهَدَ", "shahida", "ns", nt("وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى مَا قَبْلَهُ", "the masdar so made is conjoined to the one before", "te'vil edilen masdar öncekine ma'tûftur"), who="أَنَا", by="an"),
 NO("اللَّذَّاتِ", "ladhdha", R("maf", "kasra")),
 PT("هَلْ", "hal-istifham", mk("حَرْفُ اسْتِفْهَامٍ", "The particle of question", "İstifham harfi", "al-istifham"),
    HD("اسْتِفْهَامٌ خَرَجَ عَنْ مَعْنَاهُ إِلَى النَّفْيِ وَالْإِنْكَارِ: لَسْتَ مُخْلِدِي، وَبِهِ صَرَّحَ فِي الْبَيْتِ بَعْدَهُ «فَإِنْ كُنْتَ لَا تَسْطِيعُ دَفْعَ مَنِيَّتِي»", "a question that has left its meaning for denial — «you cannot make me live for ever» — as the next verse says outright: «if you cannot ward off my death»", "anlamından çıkıp nefy ve inkâra geçmiş istifham: «beni ölümsüz kılamazsın»; sonraki beyit bunu açıkça söyler: «ölümümü savamıyorsan»"), g=["khuruj-al-istifham"]),
 PT("أَنْتَ", "anta", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), pos="pron"),
 NO("مُخْلِدِي", "mukhlid", R("kh", "yam"), nt("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ؛ الْإِخْلَادُ وَالتَّخْلِيدُ: الْإِبْقَاءُ؛ وَالْجُمْلَةُ اسْتِئْنَافِيَّةٌ", "an active participle annexed to its object; الإِخْلَاد and التَّخْلِيد: making to last for ever; the clause opens a new sentence", "ism-i fâilin mef'ûlüne izâfeti; الإِخْلَاد ve التَّخْلِيد: ebedî kılmak; cümle istînâfiyyedir", "ism-fail"), enc="ي"),
])
V(56, "And if you cannot ward off my death, then let me hasten to meet it with what my hand possesses.",
  "Ölümümü savmaya gücün yetmiyorsa bırak da elimdeki her şeyle ona doğru koşayım.", [
 PT("فَإِنْ", "in-shartiyya", IN_SH, JM("ist"), pre="fa-ist"),
 PT("كُنْتَ", "kana", mk("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْمُخَاطَبِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا", "A defective past verb built on sukun because the ta of the one addressed is attached, in the seat of jazm as the condition's verb; the ta is its noun, in the seat of raf'", "Muhatap tâsına bitiştiği için sükûn üzere mebnî nâkıs mâzî; şart fiili olarak mahallen meczûm; tâ ismi, mahallen merfû", "kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza"), pos="verb"),
 PT("لَا", "la-nafiya", LA_NAFY),
 VB("تَسْطِيعُ", "istaa", "mud", JM("kh", "كَانَ", "nasb"), nt("اسْطَاعَ يَسْطِيعُ لُغَةٌ فِي اسْتَطَاعَ (الزَّوْزَنِيُّ)", "اسْطَاعَ يَسْطِيعُ is a dialect form of اسْتَطَاعَ (al-Zawzanī)", "اسْطَاعَ يَسْطِيعُ, اسْتَطَاعَ'ın bir lehçesidir (Zevzenî)"), who="أَنْتَ", g=["form-x-verbs", "hollow-verbs"]),
 NO("دَفْعَ", "daf-repel", R("maf") + MUD, nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", "the masdar annexed to its object", "masdarın mef'ûlüne izâfeti", "masdar")),
 NO("مَنِيَّتِي", "maniyya", R("mi", "yam"), enc="ي", p=HEMI),
 VB("فَدَعْنِي", "da-leave", "amr", JM("jzm"), who="أَنْتَ", enc="نِي", pre="fa-jaza"),
 VB("أُبَادِرْهَا", "badara", "jz", nt("وَعِنْدَ الْجُمْهُورِ جَزْمُهُ بِشَرْطٍ مَحْذُوفٍ (الدُّرَّةُ)؛ يَقُولُ: فَدَعْنِي أُبَادِرِ الْمَوْتَ بِإِنْفَاقِ أَمْلَاكِي (الزَّوْزَنِيُّ)", "for most grammarians its jazm is by a condition left out (al-Durra); he says: let me race death by spending what I own (al-Zawzanī)", "çoğunluğa göre cezmi mahzûf bir şart iledir (Dürre); der ki: bırak, mallarımı harcayarak ölümün önüne geçeyim (Zevzenî)"), who="أَنَا", by="talab", enc="هَا", g=["form-iii-verbs"]),
 PT("بِمَا", "ma-mawsula", mk("مَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أُبَادِرْ»", "مَا is a relative noun built on sukun, in the seat of jarr; the phrase hangs on «أُبَادِرْ»", "مَا sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr; câr-mecrûr «أُبَادِرْ»a müteallik", "ism-mawsul"), pre="bi", pos="pron"),
 VB("مَلَكَتْ", "malaka", "madi-f", JM("sila"), nt("وَالْعَائِدُ مَحْذُوفٌ، أَيْ: مَلَكَتْهُ", "the pronoun returning to مَا is left out — «what my hand possesses»", "mevsûle dönen zamir mahzûftur: «elimin sahip olduğu»")),
 NO("يَدِي", "yad", R("fail", "yam"), enc="ي"),
])
V(57, "Were it not for three things that make up a young man's life — by your fortune! — I should not care when my visitors rise to leave me.",
  "Yiğidin hayatını oluşturan üç şey olmasaydı — talihine andolsun! — beni ziyarete gelenlerin ne zaman kalkıp gideceğine aldırmazdım.", [
 PT("وَلَوْلَا", "lawla", mk("حَرْفُ امْتِنَاعٍ لِوُجُودٍ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ", "The particle of «not, because of», carrying the sense of a condition", "Bir şeyin varlığından dolayı başkasının yokluğunu bildiren, şart mânâlı harf", "huruf-al-shart-fil-kafiya"), JM("ist"), pre="wa-ist"),
 NO("ثَلَاثٌ", "thalath", R("mub"), nt("وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا بَعْدَ «لَوْلَا»؛ وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: ثَلَاثُ خِصَالٍ (الدُّرَّةُ)", "its predicate must be left out after لَوْلَا; it describes a noun left out — «three qualities» (al-Durra)", "«لَوْلَا»dan sonra haberi vücûben mahzûftur; mahzûf bir mevsûfun sıfatıdır: «üç haslet» (Dürre)", "hadhf-wa-taqdir")),
 PT("هُنَّ", "hunna", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«ثَلَاثٌ»", "the clause is an adjective of «ثَلَاثٌ», in the seat of raf'", "cümle «ثَلَاثٌ»ün na'tı olarak mahallen merfû", "jumla-sifa"), pos="pron"),
 HJ("مِنْ", "min"),
 NO("عِيشَةِ", "isha", R("maj") + MUD, ONH("kh", "هُنَّ")),
 NO("الْفَتَى", "fata-youth", R("mi", "maq"), p=HEMI),
 NO("وَجَدِّكَ", "jadd", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُقْسِمُ، وَالْجُمْلَةُ الْقَسَمِيَّةُ مُعْتَرِضَةٌ بَيْنَ «لَوْلَا» وَجَوَابِهَا (الدُّرَّةُ)؛ الْجَدُّ: الْحَظُّ وَالْبَخْتُ، وَقَوْلُهُ «وَجَدِّكَ» قَسَمٌ (الزَّوْزَنِيُّ)", "the phrase hangs on a verb left out, «I swear», and the oath is a parenthesis between لَوْلَا and its answer (al-Durra); الجَدّ: fortune, luck — «وَجَدِّكَ» is an oath (al-Zawzanī)", "câr-mecrûr mahzûf «أُقْسِمُ» fiiline müteallik; kasem cümlesi «لَوْلَا» ile cevabı arasında mu'tarızadır (Dürre); الجَدّ: talih, baht — «وَجَدِّكَ» bir yemindir (Zevzenî)", "jumla-mutarida"),
    HD("إِطْنَابٌ بِالِاعْتِرَاضِ: جُمْلَةُ قَسَمٍ لَا مَحَلَّ لَهَا فِي أَثْنَاءِ الْكَلَامِ بَيْنَ الشَّرْطِ وَجَوَابِهِ، لِتَوْكِيدِهِ", "an amplification by parenthesis: an oath-clause without a seat, set inside the speech between the condition and its answer, to make it firm", "i'tirâz yoluyla ıtnâb: şartla cevabı arasına giren, i'râbdan mahalli olmayan bir kasem cümlesi — sözü pekiştirmek için"), enc="كَ", pre="wa-qasam", g=["asbab-al-itnab"]),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("أَحْفِلْ", "hafala", "jz", JM("jawab", "لَوْلَا"), nt("وَجَوَابُ الْقَسَمِ مَحْذُوفٌ لِدَلَالَةِ جَوَابِ الشَّرْطِ عَلَيْهِ (الدُّرَّةُ)؛ الْحَفْلُ: الْمُبَالَاةُ", "the oath's answer is left out, the condition's answer pointing to it (al-Durra); الحَفْل: caring", "kasemin cevabı, şartın cevabı ona delâlet ettiği için mahzûftur (Dürre); الحَفْل: aldırmak"), who="أَنَا", by="lam"),
 PT("مَتَى", "mata-istifham", mk("اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ، مُتَعَلِّقٌ بِـ«قَامَ»، وَقَدْ عَلَّقَ «أَحْفِلْ» عَنِ الْعَمَلِ لَفْظًا", "An interrogative noun built on sukun, in the seat of nasb as an adverb of time, hanging on «قَامَ»; it holds «أَحْفِلْ» back from governing in form", "Sükûn üzere mebnî istifham ismi; zaman zarfı olarak mahallen mansûb, «قَامَ»a müteallik; «أَحْفِلْ»i lafzen amelden alıkoymuştur", "al-istifham", "maful-fih"), pos="pron"),
 VB("قَامَ", "qama", "madi", g=["hollow-verbs"]),
 NO("عُوَّدِي", "aid", R("fail", "yam"), nt("الْعُوَّدُ: جَمْعُ عَائِدٍ مِنَ الْعِيَادَةِ", "العُوَّد: the plural of عَائِد, one visiting the sick", "العُوَّد: hasta ziyaretçisi anlamındaki عَائِد'in cem'i", "jam-taksir"),
    ZW("يَقُولُ: لَمْ أُبَالِ مَتَى قَامَ عُوَّدِي مِنْ عِنْدِي آيِسِينَ مِنْ حَيَاتِي، أَيْ: لَمْ أُبَالِ مَتَى مِتُّ", "he says: I should not care when my visitors rose from my side despairing of my life — that is, I should not care when I died", "der ki: ziyaretçilerimin hayatımdan ümit keserek yanımdan ne zaman kalkacaklarına aldırmazdım, yani ne zaman öleceğime aldırmazdım"),
    S_(mk("فَهُوَ كِنَايَةٌ عَنِ الْمَوْتِ", "So it is a kinaya for death", "Bu, ölümden kinâyedir", "kinaya")), enc="ي"),
])
V(58, "Of them is my getting before the women who blame me with a draught of dark-red wine that foams when water is poured upon it.",
  "Onlardan biri, beni kınayan kadınlardan önce davranıp, üzerine su döküldüğünde köpüren koyu kızıl bir yudum içmemdir.", [
 PJ("فَمِنْهُنَّ", "مِنْ", "min", "هُنَّ", ONH("khm", "سَبْقِي"), ref="ثَلَاثٌ", pre="fa-tafri"),
 NO("سَبْقِي", "sabq", R("mubm", "yam"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ وَيُرْوَى «سَبْقُ الْعَاذِلَاتِ» (التِّبْرِيزِيُّ)", "the masdar annexed to its doer; it is also transmitted «سَبْقُ الْعَاذِلَاتِ» (al-Tibrīzī)", "masdarın fâiline izâfeti; «سَبْقُ الْعَاذِلَاتِ» diye de rivayet edilir (Tebrîzî)", "masdar"), enc="ي"),
 NO("الْعَاذِلَاتِ", "adhila", R("maf", "kasra"), nt("لِلْمَصْدَرِ «سَبْقِي»", "of the masdar «سَبْقِي»", "«سَبْقِي» masdarının mef'ûlü", "amal-ism-al-tafdil-wal-masdar")),
 NO("بِشَرْبَةٍ", "sharba", R("maj"), ON("سَبْقِي"), pre="bi", p=HEMI),
 NO("كُمَيْتٍ", "kumayt", NA("شَرْبَةٍ", "jarr"), nt("أَيْ: كُمَيْتِ اللَّوْنِ (الزَّوْزَنِيُّ)، وَهُوَ لَوْنٌ بَيْنَ الْحُمْرَةِ وَالسَّوَادِ", "that is, dark-red in colour (al-Zawzanī) — a colour between red and black", "yani koyu kızıl renkli (Zevzenî) — kırmızı ile siyah arası bir renk")),
 PT("مَتَى", "mata", MATA_SH + mk("، مُتَعَلِّقٌ بِـ«تُعْلَ»", ", hanging on «تُعْلَ»", ", «تُعْلَ»ya müteallik"), nt("وَالْجُمْلَةُ الشَّرْطِيَّةُ نَعْتٌ ثَانٍ لِـ«شَرْبَةٍ»", "the conditional sentence is a second adjective of «شَرْبَةٍ»", "şart cümlesi «شَرْبَةٍ»nin ikinci na'tıdır")),
 PT("مَا", "ma-zaida", MA_ZAID),
 VB("تُعْلَ", "ala-rise", "jz-ill", who=("هِيَ", "شَرْبَةٍ"), by="shart", maj=True),
 NO("بِالْمَاءِ", "ma-water", R("maj"), ON("تُعْلَ"), pre="bi"),
 VB("تُزْبِدِ", "azbada", "jz", JM("jz"), nt("أَيْ: أَزْبَدَتْ (الزَّوْزَنِيُّ)", "that is, it foamed (al-Zawzanī)", "yani köpürdü (Zevzenî)"), who=("هِيَ", "شَرْبَةٍ"), by="jawab", q=True, g=["form-iv-verbs"]),
])
V(59, "And my wheeling round, when the hard-pressed calls for help, on a horse bowed in the foreleg, like a wolf of the ghaḍā thickets that you have startled as he goes down to water.",
  "Sıkışmış biri yardım çağırdığında, ön ayağında hafif eğrilik olan bir atla, suya inerken ürküttüğün ğadâ çalılığının kurdu gibi geri dönüp saldırmamdır.", [
 NO("وَكَرِّي", "karr-wheel", AT("سَبْقِي", "raf", "yam"), nt("أَوْ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ، أَيْ: وَمِنْهُنَّ كَرِّي (الدُّرَّةُ)؛ مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الْكَرُّ: الْعَطْفُ", "or a mubtada whose predicate is left out — «and of them is my wheeling» (al-Durra); the masdar annexed to its doer; الكَرّ: turning back to charge", "ya da haberi mahzûf bir mübteda: «onlardan biri de dönüp saldırmamdır» (Dürre); masdarın fâiline izâfeti; الكَرّ: geri dönüp saldırmak", "masdar"), enc="ي", pre="wa"),
 PT("إِذَا", "idha", IDHA_Z("كَرِّي")),
 VB("نَادَى", "nada", "madi-muq", JM("mudaf", "إِذَا"), g=["form-iii-verbs", "naqis-verbs"]),
 NO("الْمُضَافُ", "mudaf", "fail", nt("الْمُضَافُ: الْخَائِفُ الْمَذْعُورُ، وَالْمُلْجَأُ (الزَّوْزَنِيُّ)", "المُضَاف: one frightened and hard-pressed, driven to seek refuge (al-Zawzanī)", "المُضَاف: korkmuş, sıkışmış, sığınmaya muhtaç kalmış kişi (Zevzenî)", "ism-maful")),
 NO("مُحَنَّبًا", "muhannab", R("maf"), nt("لِلْمَصْدَرِ «كَرِّي»، وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: وَكَرِّي فَرَسًا مُحَنَّبًا (الدُّرَّةُ)؛ وَقَالَ ابْنُ الْأَنْبَارِيِّ: حَالٌ مِنَ «الْمُضَافُ»؛ الْمُحَنَّبُ: الَّذِي فِي يَدِهِ انْحِنَاءٌ، وَهُوَ مَحْمُودٌ فِي الْفَرَسِ", "the object of the masdar «كَرِّي»; it describes a noun left out — «my wheeling a horse bowed…» (al-Durra); Ibn al-Anbārī takes it as a hal of «الْمُضَافُ»; المُحَنَّب: with a bow in the foreleg — praised in a horse", "«كَرِّي» masdarının mef'ûlü; mahzûf bir mevsûfun sıfatıdır: «ön ayağı eğri bir atı döndürmem» (Dürre); İbnü'l-Enbârî onu «الْمُضَافُ»tan hâl sayar; المُحَنَّب: ön ayağında eğrilik olan — atta övülen bir vasıf", "hadhf-wa-taqdir", "ism-maful"), p=HEMI),
 NO("كَسِيدِ", "sid-wolf", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ أَوْ حَالٍ مِنْهُ (الدُّرَّةُ)؛ السِّيدُ: الذِّئْبُ", "the phrase hangs on an omitted second adjective of the noun left out, or a hal of it (al-Durra); السِّيد: the wolf", "câr-mecrûr mahzûf mevsûfun mahzûf ikinci na'tına ya da ondan hâle müteallik (Dürre); السِّيد: kurt"),
    TSB("mm", ("فَرَسُهُ فِي شِدَّةِ عَدْوِهِ", "his horse in the fury of its run", "koşusunun şiddetinde atı"), ("ذِئْبُ الْغَضَا إِذَا نُبِّهَ وَهُوَ يُرِيدُ الْمَاءَ", "the wolf of the ghaḍā startled as it makes for water", "suya inerken ürkütülen ğadâ kurdu"), "ka"),
    ZW("ثُمَّ شَبَّهَ فَرَسَهُ بِذِئْبٍ اجْتَمَعَ لَهُ ثَلَاثُ خِلَالٍ: كَوْنُهُ فِيمَا بَيْنَ الْغَضَا، وَذِئْبُ الْغَضَا أَخْبَثُ الذِّئَابِ، وَإِثَارَةُ الْإِنْسَانِ إِيَّاهُ، وَوُرُودُهُ الْمَاءَ، وَهُمَا يَزِيدَانِ فِي شِدَّةِ الْعَدْوِ", "then he likens his horse to a wolf in which three things meet: it lives among the ghaḍā, and the ghaḍā wolf is the most cunning of wolves; a man has roused it; and it is going down to water — both of these add to the fury of its run", "sonra atını üç hasleti bir araya gelmiş bir kurda benzetir: ğadâ çalılığında yaşar — ğadâ kurdu kurtların en kurnazıdır —, bir insan onu ürkütmüştür ve suya inmektedir; bu ikisi koşusunun şiddetini artırır"), pre="ka", g=TSB_TAGS),
 NO("الْغَضَا", "ghada", R("mi", "maq"), nt("الْغَضَا: شَجَرٌ", "الغَضَا: a kind of tree (tamarisk-like scrub)", "الغَضَا: bir tür ağaç (ılgına benzer çalı)")),
 VB("نَبَّهْتَهُ", "nabbaha", "madi-ta", nt("وَالْجُمْلَةُ صَالِحَةٌ لِلْحَالِيَّةِ وَالْوَصْفِيَّةِ (الدُّرَّةُ)", "the clause may be a hal or an adjective (al-Durra)", "cümle hâl de sıfat da olabilir (Dürre)"), enc="هُ", g=["form-ii-verbs"]),
 NO("الْمُتَوَرِّدِ", "mutawarrid", NA("سِيدِ الْغَضَا", "jarr"), nt("أَيْ: وَهُوَ يُرِيدُ الْمَاءَ (الزَّوْزَنِيُّ)؛ الْوِرْدُ وَالتَّوَرُّدُ وَاحِدٌ؛ وَجَعَلَهُ الدُّرَّةُ مِنْ صِفَاتِ الْمَوْصُوفِ الْمَحْذُوفِ", "that is, as it makes for water (al-Zawzanī); الوِرْد and التَّوَرُّد are one; al-Durra counts it among the adjectives of the noun left out", "yani suya giderken (Zevzenî); الوِرْد ile التَّوَرُّد birdir; Dürre onu mahzûf mevsûfun sıfatları arasında sayar", "ism-fail")),
])
V(60, "And my shortening of the cloudy day — and a cloudy day is a delight — with a soft, full-bodied woman beneath the tent of hide raised on its poles.",
  "Ve bulutlu günü — bulutlu gün ne hoştur! — direklerle yükseltilmiş deri çadırın altında dolgun, yumuşak bir kadınla kısaltmamdır.", [
 NO("وَتَقْصِيرُ", "taqsir", AT("سَبْقِي", "raf") + MUD, nt("أَوْ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ كَـ«كَرِّي»؛ قَصَّرْتُ الشَّيْءَ: جَعَلْتُهُ قَصِيرًا؛ وَشَرَطَ تَقْصِيرَ الْيَوْمِ لِأَنَّ أَوْقَاتَ اللَّهْوِ وَالطَّرَبِ أَقْصَرُ الْأَوْقَاتِ (الزَّوْزَنِيُّ)", "or a mubtada whose predicate is left out, as with «كَرِّي»; قَصَّرْتُ الشَّيْءَ: I made it short — he speaks of shortening the day because the hours of pleasure are the shortest hours (al-Zawzanī)", "ya da «كَرِّي» gibi haberi mahzûf bir mübteda; قَصَّرْتُ الشَّيْءَ: onu kısalttım — günü kısaltmayı söylemiştir, çünkü eğlence ve neşe vakitleri vakitlerin en kısasıdır (Zevzenî)", "masdar"), pre="wa"),
 NO("يَوْمِ", "yawm", R("mi") + MUD, nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", "the masdar annexed to its object", "masdarın mef'ûlüne izâfeti")),
 NO("الدَّجْنِ", "dajn", "mi", nt("الدَّجْنُ: إِلْبَاسُ الْغَيْمِ آفَاقَ السَّمَاءِ", "الدَّجْن: clouds covering the horizons of the sky", "الدَّجْن: bulutların göğün ufuklarını örtmesi")),
 NO("وَالدَّجْنُ", "dajn", R("mub"), nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ، وَيَجُوزُ أَنْ تَكُونَ مُعْتَرِضَةً", "the clause is a hal, in the seat of nasb; it may also be a parenthesis", "cümle hâl olarak mahallen mansûb; mu'tarıza olması da câizdir"),
    HD("وَضْعُ الظَّاهِرِ مَوْضِعَ الْمُضْمَرِ: أَعَادَ «الدَّجْنُ» اسْمًا ظَاهِرًا، وَمُقْتَضَى الظَّاهِرِ «وَهُوَ مُعْجِبٌ»", "the explicit noun put where a pronoun was due: he repeats «الدَّجْنُ» in full, where the plain course was «and it is a delight»", "zamirin yerine açık isim konmuştur: «الدَّجْنُ»u açık isim olarak tekrarlamıştır; zâhirin gereği «وَهُوَ مُعْجِبٌ» idi"), pre="wa-hal", g=["khilaf-muqtada-al-zahir"]),
 NO("مُعْجِبٌ", "mujib-pleasing", "kh", nt("أَيْ: يُعْجِبُ الْإِنْسَانَ (الزَّوْزَنِيُّ)", "that is, it delights a man (al-Zawzanī)", "yani insanın hoşuna gider (Zevzenî)", "ism-fail"), p=HEMI),
 NO("بِبَهْكَنَةٍ", "bahkana", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَقْصِيرُ»، أَيْ: بِالتَّمَتُّعِ بِبَهْكَنَةٍ؛ الْبَهْكَنَةُ: الْمَرْأَةُ الْحَسَنَةُ الْخَلْقِ السَّمِينَةُ النَّاعِمَةُ", "the phrase hangs on «تَقْصِيرُ» — «by taking my joy with…»; البَهْكَنَة: a woman fair of form, full and soft", "câr-mecrûr «تَقْصِيرُ»e müteallik: «… ile eğlenerek»; البَهْكَنَة: yaratılışı güzel, dolgun ve yumuşak kadın"), pre="bi"),
 NO("تَحْتَ", "tahta", R("zm") + MUD, ONH("naat", "بَهْكَنَةٍ", zarf=True)),
 NO("الطِّرَافِ", "tiraf", "mi"),
 NO("الْمُعَمَّدِ", "muammad", NA("الطِّرَافِ", "jarr"), nt("الْمُعَمَّدُ: الْمَرْفُوعُ بِالْعُمُدِ", "المُعَمَّد: raised on poles", "المُعَمَّد: direklerle yükseltilmiş", "ism-maful")),
])
V(61, "As though the anklets and the armlets had been hung upon an ʿushar bush or a castor-plant left unlopped.",
  "Sanki halhallar ve pazıbentler, dalları budanmamış bir uşar ya da kene otu ağacına asılmıştır.", [
 PT("كَأَنَّ", "kaanna", KAANNA_T, JM("ist")),
 NO("الْبُرِينَ", "bura", R("ism:كَأَنَّ", "mulhaq"), nt("جَمْعُ بُرَةٍ: حَلْقَةٌ تُجْعَلُ فِي أَنْفِ النَّاقَةِ", "the plural of بُرَة, a ring set in a she-camel's nose", "«بُرَة»nın cem'i: devenin burnuna takılan halka"),
    S_(mk("وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَتِ الْبُرَةُ لِلْأَسْوِرَةِ وَالْخَلَاخِيلِ (قَالَ الزَّوْزَنِيُّ: «اسْتِعَارَةٌ لِلْأَسْوِرَةِ وَالْخَلَاخِيلِ»)", "There is an explicit istiara: the camel's nose-ring is borrowed for bracelets and anklets (al-Zawzanī: «a borrowing for the bracelets and anklets»)", "İstiâre-i tasrîhiyye vardır: devenin burun halkası bilezik ve halhallar için iğreti alınmıştır (Zevzenî: «bilezik ve halhallar için istiâredir»)", "istiara", "aqsam-al-istiara"))),
 NO("وَالدَّمَالِيجَ", "dumluj", AT("الْبُرِينَ", "nasb"), nt("جَمْعُ دُمْلُجٍ: الْمِعْضَدُ", "the plural of دُمْلُج, an armlet", "«دُمْلُج»un cem'i: pazıbent", "jam-taksir"), pre="wa"),
 VB("عُلِّقَتْ", "allaqa", "madi-f", JM("kh", "كَأَنَّ", "raf"), who=("هِيَ", ("«الْبُرِينَ» وَ«الدَّمَالِيجَ»", "«الْبُرِينَ» and «الدَّمَالِيجَ»", "«الْبُرِينَ» ve «الدَّمَالِيجَ»ye")), maj=True, g=["form-ii-verbs"], p=HEMI),
 HJ("عَلَى", "ala"),
 NO("عُشَرٍ", "ushar", R("maj"), ON("عُلِّقَتْ"), nt("الْعُشَرُ وَالْخِرْوَعُ: ضَرْبَانِ مِنَ الشَّجَرِ", "العُشَر and الخِرْوَع: two kinds of tree", "العُشَر ve الخِرْوَع: iki tür ağaç"),
    TSB("mm", ("سَاعِدَاهَا وَسَاقَاهَا", "her forearms and her shins", "önkolları ve baldırları"), ("أَحَدُ هٰذَيْنِ الشَّجَرَيْنِ", "one of these two trees", "bu iki ağaçtan biri"), "kaanna"),
    ZW("شَبَّهَ سَاعِدَيْهَا وَسَاقَيْهَا بِأَحَدِ هٰذَيْنِ الشَّجَرَيْنِ فِي الِامْتِلَاءِ وَالنَّعْمَةِ وَالضَّخَامَةِ", "he likens her forearms and shins to one of these two trees in fullness, softness and bulk", "önkollarını ve baldırlarını dolgunluk, yumuşaklık ve iriliklerinde bu iki ağaçtan birine benzetmiştir"), g=TSB_TAGS),
 PT("أَوْ", "aw", AW_T),
 NO("خِرْوَعٍ", "khirwa", AT("عُشَرٍ", "jarr")),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("يُخَضَّدِ", "khaddada", "jz", JM("sifa", "خِرْوَعٍ"), nt("وَحُذِفَ نَظِيرُهَا بَعْدَ «عُشَرٍ» (الدُّرَّةُ)؛ التَّخْضِيدُ: التَّشْذِيبُ مِنَ الْأَغْصَانِ وَالْأَوْرَاقِ، وَجَعَلَهُ غَيْرَ مُخَضَّدٍ لِيَكُونَ أَغْلَظَ (الزَّوْزَنِيُّ)", "its like is left out after «عُشَرٍ» (al-Durra); التَّخْضِيد: lopping boughs and leaves — he makes it unlopped so as to be the thicker (al-Zawzanī)", "benzeri «عُشَرٍ»dan sonra hazfedilmiştir (Dürre); التَّخْضِيد: dal ve yaprakları budamak — daha kalın olsun diye onu budanmamış kılmıştır (Zevzenî)"), who=("هُوَ", "خِرْوَعٍ"), by="lam", maj=True, q=True, g=["form-ii-verbs"]),
])
# ---- Death, which levels the graves: verses 62–67 ------------------------------------------------------------------------
_CL["sa"] = ("السِّينُ حَرْفُ اسْتِقْبَالٍ، وَ", "The sin marks the near future; ", "Sîn istikbal harfidir; ", ("سَ", "sa-istiqbal", "part"))
_CL["la-ibtida"] = ("اللَّامُ لَامُ الِابْتِدَاءِ، وَ", "The lam is the lam of emphasis opening the clause; ", "Lâm ibtidâ lâmıdır; ", ("لَ", "la-ibtida", "part"))
V(62, "— a noble man who gives his soul its fill of drink while he lives: you shall know, if we die tomorrow, which of us is the thirsty one.",
  "— hayattayken kendine kana kana içiren cömert bir adamım; yarın ölürsek hangimizin susuz olduğunu bileceksin.", [
 NO("كَرِيمٌ", "karim", "khm", JM("ist"), nt("أَيْ: أَنَا كَرِيمٌ، وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ (الدُّرَّةُ)", "that is, «I am a noble man»; it describes a noun left out (al-Durra)", "yani «ben cömert biriyim»; mahzûf bir mevsûfun sıfatıdır (Dürre)", "hadhf-wa-taqdir", "sifa-mushabbaha")),
 VB("يُرَوِّي", "rawwa", "mud-y", nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ؛ يَقُولُ: يُرَوِّي نَفْسَهُ أَيَّامَ حَيَاتِهِ بِالْخَمْرِ (الزَّوْزَنِيُّ)", "the clause is a second adjective of the noun left out, in the seat of raf'; he says: he gives his soul its fill of wine all his days (al-Zawzanī)", "cümle mahzûf mevsûfun ikinci na'tı olarak mahallen merfû; der ki: hayatı boyunca kendine şarabı kana kana içirir (Zevzenî)", "jumla-sifa"), who=("هُوَ", "كَرِيمٌ"), g=["form-ii-verbs", "naqis-verbs"]),
 NO("نَفْسَهُ", "nafs", "maf", enc="هُ"),
 HJ("فِي", "fi"),
 NO("حَيَاتِهِ", "hayat", R("maj"), ON("يُرَوِّي"), enc="هِ", p=HEMI),
 VB("سَتَعْلَمُ", "alima", "mud", JM("ist"), nt("وَقَدْ عُلِّقَ عَنِ الْعَمَلِ لَفْظًا بِالِاسْتِفْهَامِ بَعْدَهُ (الدُّرَّةُ)", "it is held back from governing in form by the question after it (al-Durra)", "sonraki istifham sebebiyle lafzen amelden alıkonmuştur (Dürre)", "al-mutaaddi-wa-afal-al-qulub"), who="أَنْتَ", pre="sa"),
 PT("إِنْ", "in-shartiyya", IN_SH, nt("وَجَوَابُ الشَّرْطِ مَحْذُوفٌ يَدُلُّ عَلَيْهِ السِّيَاقُ، وَالشَّرْطُ مُعْتَرِضٌ بَيْنَ الْفِعْلِ وَمَا سَدَّ مَسَدَّ مَفْعُولَيْهِ (الدُّرَّةُ)", "the answer of the condition is left out, the context pointing to it; the condition stands as a parenthesis between the verb and what fills its two objects (al-Durra)", "şartın cevabı mahzûftur, siyak ona delâlet eder; şart, fiil ile iki mef'ûlünün yerini tutan cümle arasında mu'tarızadır (Dürre)", "hadhf-wa-taqdir")),
 VB("مُتْنَا", "mata-die", "madi-na", IN_COND, g=["hollow-verbs"]),
 NO("غَدًا", "ghad", R("zz"), ZON("مُتْنَا")),
 NO("أَيُّنَا", "ayy", mk("اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "An interrogative noun, the mubtada, in raf' by the damma", "İstifham ismi, mübteda, damme ile merfû", "al-istifham", "mubtada-khabar"), nt("وَجُمْلَةُ «أَيُّنَا الصَّدِي» فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ مَفْعُولَيْ «تَعْلَمُ»", "the clause «أَيُّنَا الصَّدِي» fills the place of the two objects of «تَعْلَمُ», in the seat of nasb", "«أَيُّنَا الصَّدِي» cümlesi «تَعْلَمُ»nun iki mef'ûlünün yerini tutar, mahallen mansûb"), enc="نَا", pos="pron"),
 NO("الصَّدِي", "sadin", R("kh", "man"), nt("الصَّدِي: الْعَطْشَانُ؛ يُرِيدُ أَنَّهُ يَمُوتُ رَيَّانَ وَعَاذِلُهُ يَمُوتُ عَطْشَانَ (الزَّوْزَنِيُّ)", "الصَّدِي: the thirsty one; he means that he will die with his thirst slaked, and his blamer die thirsty (al-Zawzanī)", "الصَّدِي: susuz; kendisinin kanmış olarak, kınayanının ise susuz olarak öleceğini kasteder (Zevzenî)", "sifa-mushabbaha"),
    HD("طِبَاقٌ بَيْنَ «يُرَوِّي» وَ«الصَّدِي»: الرِّيُّ وَالْعَطَشُ، فِعْلٌ وَاسْمٌ", "«يُرَوِّي» and «الصَّدِي» make a tibaq — slaking against thirst, a verb against a noun", "«يُرَوِّي» ile «الصَّدِي» arasında tıbâk vardır: kanmak ile susuzluk — biri fiil, biri isim"), g=["tibaq"]),
])
V(63, "I see the grave of the grasping man, miserly with his wealth, like the grave of the wastrel squandering in idle folly.",
  "Malına cimri, hırslı adamın kabrini, boş işlerde malını har vurup harman savuran sapkının kabri gibi görürüm.", [
 VB("أَرَى", "raa", "mud-a", JM("ist"), who="أَنَا", g=["naqis-verbs"]),
 NO("قَبْرَ", "qabr", R("maf1") + MUD),
 NO("نَحَّامٍ", "nahham", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ (الدُّرَّةُ)؛ النَّحَّامُ: الْحَرِيصُ عَلَى الْجَمْعِ وَالْمَنْعِ", "it describes a noun left out (al-Durra); النَّحَّام: one greedy to gather and to withhold", "mahzûf bir mevsûfun sıfatıdır (Dürre); النَّحَّام: toplamaya ve vermemeye hırslı", "hadhf-wa-taqdir", "sighat-mubalagha")),
 NO("بَخِيلٍ", "bakhil", NMH("jarr", nth="2")),
 NO("بِمَالِهِ", "mal", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بَخِيلٍ» لِأَنَّهُ صِفَةٌ مُشَبَّهَةٌ", "the phrase hangs on «بَخِيلٍ», a ṣifa mushabbaha", "câr-mecrûr sıfat-ı müşebbehe olan «بَخِيلٍ»e müteallik"), enc="هِ", pre="bi", p=HEMI),
 NO("كَقَبْرِ", "qabr", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ ثَانٍ لِـ«أَرَى» مَحْذُوفٍ (الدُّرَّةُ)", "the phrase hangs on an omitted adjective of the omitted second object of «أَرَى» (al-Durra)", "câr-mecrûr «أَرَى»nın mahzûf ikinci mef'ûlünün mahzûf na'tına müteallik (Dürre)"),
    TSB("mm", ("قَبْرُ الْبَخِيلِ", "the miser's grave", "cimrinin kabri"), ("قَبْرُ الْغَوِيِّ الْمُفْسِدِ", "the squanderer's grave", "müsrif sapkının kabri"), "ka", src="h"),
    ZW("يَقُولُ: لَا فَرْقَ بَيْنَ الْبَخِيلِ وَالْجَوَادِ بَعْدَ الْوَفَاةِ، فَلِمَ أَبْخَلُ بِأَعْلَاقِي؟", "he says: there is no difference between miser and open-handed after death, so why should I be sparing of my treasures?", "der ki: ölümden sonra cimri ile cömert arasında fark yoktur; öyleyse değerli mallarımı niçin esirgeyeyim?"), pre="ka", g=TSB_TAGS),
 NO("غَوِيٍّ", "ghawiyy", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ؛ الْغَوِيُّ: الْغَاوِي الضَّالُّ", "it describes a noun left out; الغَوِيّ: one gone astray", "mahzûf bir mevsûfun sıfatıdır; الغَوِيّ: yoldan çıkmış sapkın", "hadhf-wa-taqdir", "sifa-mushabbaha")),
 HJ("فِي", "fi"),
 NO("الْبَطَالَةِ", "batala", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«غَوِيٍّ» لِأَنَّهُ صِفَةٌ مُشَبَّهَةٌ", "the phrase hangs on «غَوِيٍّ», a ṣifa mushabbaha", "câr-mecrûr sıfat-ı müşebbehe olan «غَوِيٍّ»e müteallik")),
 NO("مُفْسِدِ", "mufsid", NMH("jarr", nth="2"), nt("أَيِ: الْمُفْسِدِ بِمَالِهِ (الزَّوْزَنِيُّ)", "that is, squandering his wealth (al-Zawzanī)", "yani malını telef eden (Zevzenî)", "ism-fail"),
    HD("طِبَاقٌ بَيْنَ «بَخِيلٍ بِمَالِهِ» وَ«مُفْسِدِ» الْمَالِ: الْإِمْسَاكُ وَالتَّبْذِيرُ", "«بَخِيلٍ بِمَالِهِ» and «مُفْسِدِ» make a tibaq — holding wealth back against squandering it", "«بَخِيلٍ بِمَالِهِ» ile «مُفْسِدِ» arasında tıbâk vardır: malı tutmak ile saçıp savurmak"), q=True, g=["tibaq"]),
])
V(64, "You see two mounds of earth, and on them broad, hard slabs from a stone-field laid in rows.",
  "İki toprak yığını görürsün; üzerlerinde, sıra sıra dizilmiş taş levhalardan sert, geniş taşlar vardır.", [
 VB("تَرَى", "raa", "mud-a", JM("ist"), who="أَنْتَ", g=["naqis-verbs"]),
 NO("جُثْوَتَيْنِ", "juthwa", R("maf", "ya2"), NUN_IWAD, nt("الْجُثْوَةُ: الْكُومَةُ مِنَ التُّرَابِ وَغَيْرِهِ، وَالْجَمْعُ الْجُثَى؛ أَيْ: قَبْرَيِ الْبَخِيلِ وَالْجَوَادِ (الزَّوْزَنِيُّ)", "الجُثْوَة: a heap of earth or the like (pl. الجُثَى) — the graves of the miser and of the open-handed (al-Zawzanī)", "الجُثْوَة: toprak vb. yığını (çoğ. الجُثَى) — cimrinin ve cömerdin kabirleri (Zevzenî)")),
 HJ("مِنْ", "min"),
 NO("تُرَابٍ", "turab", R("maj"), ONH("naat", "جُثْوَتَيْنِ")),
 PJ("عَلَيْهِمَا", "عَلَيْ", "ala", "هِمَا", ONH("khm", "صَفَائِحُ"), ref="جُثْوَتَيْنِ", p=HEMI),
 NO("صَفَائِحُ", "safih", R("mubm"), nt("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنْ «جُثْوَتَيْنِ» (الدُّرَّةُ)؛ جَمْعُ صَفِيحَةٍ: الْحَجَرُ الْعَرِيضُ", "the clause may be an adjective or a hal of «جُثْوَتَيْنِ» (al-Durra); the plural of صَفِيحَة, a broad stone", "cümle «جُثْوَتَيْنِ»in sıfatı da hâli de olabilir (Dürre); «صَفِيحَة»nın cem'i: geniş taş", "jam-taksir")),
 NO("صُمٌّ", "summ", NA("صَفَائِحُ", "raf"), nt("أَيْ: صِلَابٌ", "that is, hard", "yani sert")),
 HJ("مِنْ", "min"),
 NO("صَفِيحٍ", "safih", R("maj"), ONH("naat2", "صَفَائِحُ"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «صَفَائِحُ» وَ«صَفِيحٍ» الِاشْتِقَاقُ", "a figure joined to jinas: «صَفَائِحُ» and «صَفِيحٍ» are brought together by derivation", "cinâsa mülhak: «صَفَائِحُ» ile «صَفِيحٍ»i iştikak bir araya getirmiştir"), g=["mulhaq-bil-jinas"]),
 NO("مُنَضَّدِ", "munaddad", NA("صَفِيحٍ", "jarr"), nt("التَّنْضِيدُ: مُبَالَغَةُ النَّضْدِ", "التَّنْضِيد: the intensive of النَّضْد, laying in rows", "التَّنْضِيد: النَّضْد'in (dizmek) mübalağası", "ism-maful"), q=True),
])
V(65, "I see death choosing out the noble, and singling out the choicest of the hard-fisted miser's wealth.",
  "Ölümün cömertleri seçtiğini, eli sıkı cimrinin malının en seçkinini de ayırıp aldığını görürüm.", [
 VB("أَرَى", "raa", "mud-a", JM("ist"), who="أَنَا", g=["naqis-verbs"]),
 NO("الْمَوْتَ", "mawt", "maf"),
 VB("يَعْتَامُ", "itama", "mud", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ«أَرَى» إِنْ كَانَ قَلْبِيًّا، أَوْ حَالٌ مِنَ «الْمَوْتَ» إِنْ كَانَ بَصَرِيًّا (الدُّرَّةُ)؛ الِاعْتِيَامُ: الِاخْتِيَارُ", "the clause is the second object of «أَرَى» if the seeing is of the mind, or a hal of «الْمَوْتَ» if of the eye (al-Durra); الاِعْتِيَام: choosing", "«أَرَى» kalbî ise cümle ikinci mef'ûl, basarî ise «الْمَوْتَ»ten hâl olarak mahallen mansûb (Dürre); الاِعْتِيَام: seçmek"),
    HD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَ الْمَوْتُ بِمُخْتَارٍ يَنْتَقِي، وَطُوِيَ ذِكْرُ الْمُشَبَّهِ بِهِ وَرُمِزَ إِلَيْهِ بِلَازِمِهِ «يَعْتَامُ» وَ«يَصْطَفِي»", "an implied istiara: death is likened to one who picks and chooses; the thing it is likened to is not named but pointed to by what belongs to it, «يَعْتَامُ» and «يَصْطَفِي»", "istiâre-i mekniyye: ölüm, seçip ayıran birine benzetilmiş; müşebbehün bih zikredilmemiş, lâzımı olan «يَعْتَامُ» ve «يَصْطَفِي» ile ona işaret edilmiştir"), who=("هُوَ", "الْمَوْتَ"), g=["form-viii-verbs", "hollow-verbs", "istiara-makniyya", "istiara"]),
 NO("الْكِرَامَ", "karim", "maf", nt("جَمْعُ كَرِيمٍ", "the plural of كَرِيم", "«كَرِيم»in cem'i", "jam-taksir")),
 VB("وَيَصْطَفِي", "istafa", "mud-y", JM("atf", "يَعْتَامُ"), nt("يَقُولُ: أَرَى الْمَوْتَ يَخْتَارُ الْكِرَامَ بِالْإِفْنَاءِ، وَيَصْطَفِي كَرِيمَةَ مَالِ الْبَخِيلِ (الزَّوْزَنِيُّ)", "he says: I see death choose out the noble to destroy them, and single out the choicest of the miser's wealth (al-Zawzanī)", "der ki: ölümün cömertleri yok etmek için seçtiğini, cimrinin malının en değerlisini de ayırdığını görürüm (Zevzenî)"), who=("هُوَ", "الْمَوْتَ"), pre="wa", g=["form-viii-verbs", "naqis-verbs"], p=HEMI),
 NO("عَقِيلَةَ", "aqila", R("maf") + MUD, nt("الْعَقَائِلُ: كَرَائِمُ الْمَالِ وَالنِّسَاءِ، الْوَاحِدَةُ عَقِيلَةٌ", "العَقَائِل: the choicest of wealth and of women; the singular عَقِيلَة", "العَقَائِل: malın ve kadınların en seçkinleri; tekili عَقِيلَة")),
 NO("مَالِ", "mal", R("mi") + MUD),
 NO("الْفَاحِشِ", "fahish", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ؛ الْفَاحِشُ: الْبَخِيلُ", "it describes a noun left out; الفَاحِش: the miser", "mahzûf bir mevsûfun sıfatıdır; الفَاحِش: cimri", "hadhf-wa-taqdir", "ism-fail"),
    HD("طِبَاقٌ بَيْنَ «الْكِرَامَ» وَ«الْفَاحِشِ» وَهُوَ الْبَخِيلُ: الْجُودُ وَالْبُخْلُ", "«الْكِرَامَ» and «الْفَاحِشِ» — the miser — make a tibaq: open hand against closed", "«الْكِرَامَ» ile cimri demek olan «الْفَاحِشِ» arasında tıbâk vardır: cömertlik ile cimrilik"), g=["tibaq"]),
 NO("الْمُتَشَدِّدِ", "mutashaddid", NMH("jarr", nth="2"), nt("أَيِ: الْمُمْسِكِ الشَّدِيدِ الْبُخْلِ", "that is, tight-fisted, hard in his meanness", "yani eli sıkı, cimriliği katı", "ism-fail")),
])
V(66, "I see life as a treasure that dwindles every night; and what the days and time keep lessening must run out.",
  "Hayatı her gece eksilen bir hazine olarak görürüm; günlerin ve zamanın eksilttiği şey ise tükenir.", [
 VB("أَرَى", "raa", "mud-a", JM("ist"), nt("قَلْبِيَّةٌ تَنْصِبُ مَفْعُولَيْنِ", "of the mind, taking two objects", "kalbîdir, iki mef'ûl alır", "mafulayn"), who="أَنَا", g=["naqis-verbs", "zanna-wa-akhawatuha"]),
 NO("الْعَيْشَ", "aysh", "maf1", nt("وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «الدَّهْرَ»", "al-Tibrīzī and al-Durra have «الدَّهْرَ»", "Tebrîzî ve Dürre'de «الدَّهْرَ»")),
 NO("كَنْزًا", "kanz", "maf2", TSB("bl", ("الْعَيْشُ وَالْبَقَاءُ", "life and lasting", "hayat ve beka"), ("كَنْزٌ يَنْقُصُ كُلَّ لَيْلَةٍ", "a treasure that dwindles every night", "her gece eksilen bir hazine"), src="z"), g=TSB_TAGS),
 NO("نَاقِصًا", "naqis", NA("كَنْزًا", "nasb"), g=["ism-fail"]),
 NO("كُلَّ", "kull", R("zz") + MUD, nt("مُتَعَلِّقٌ بِـ«نَاقِصًا»، وَاكْتَسَبَ الظَّرْفِيَّةَ بِإِضَافَتِهِ إِلَى «لَيْلَةٍ»", "it hangs on «نَاقِصًا», taking its adverbial force from its annexation to «لَيْلَةٍ»", "«نَاقِصًا»ya müteallik; zarflığı «لَيْلَةٍ»ye izâfetinden almıştır")),
 NO("لَيْلَةٍ", "layla", "mi", p=HEMI),
 PT("وَمَا", "ma-shartiyya", mk("اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَهُوَ أَوْلَى مِنْ جَعْلِهِ مَفْعُولًا لِلْفِعْلِ بَعْدَهُ (الدُّرَّةُ)", "A conditional noun that puts two verbs in jazm, built on sukun, in the seat of raf' as mubtada — better than taking it as the object of the verb after it (al-Durra)", "İki fiili cezmeden şart ismi; sükûn üzere mebnî, mübteda olarak mahallen merfû — sonraki fiilin mef'ûlü saymaktan evlâdır (Dürre)", "al-majzum-wal-shart-wal-jaza", "mubtada-khabar"), pre="wa-ist", pos="pron"),
 VB("تَنْقُصِ", "naqasa", "jz", nt("وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَمَفْعُولُهُ ضَمِيرٌ مَحْذُوفٌ يَعُودُ عَلَى «مَا»، أَيْ: تَنْقُصْهُ (الزَّوْزَنِيُّ: «وَمَا تَنْقُصُهُ الْأَيَّامُ»)", "it takes a kasra because two quiescents meet; its object is a pronoun left out, returning to مَا (al-Zawzanī: «and what the days lessen»)", "iki sâkin karşılaştığı için kesrelenmiştir; mef'ûlü «مَا»ya dönen mahzûf bir zamirdir (Zevzenî: «günlerin eksilttiği şey»)", "hadhf-al-maful"), by="shart"),
 NO("الْأَيَّامُ", "yawm", "fail", g=["jam-taksir"]),
 NO("وَالدَّهْرُ", "dahr", AT("الْأَيَّامُ", "raf"), pre="wa"),
 VB("يَنْفَدِ", "nafida", "jz", JM("jz"), nt("وَخَبَرُ «مَا» جُمْلَتَا الشَّرْطِ وَالْجَوَابِ عَلَى الْمُرَجَّحِ (الدُّرَّةُ)؛ النَّفَادُ: الْفَنَاءُ", "the predicate of مَا is the two clauses, condition and answer, on the preferred view (al-Durra); النَّفَاد: running out", "tercih edilen görüşe göre «مَا»nın haberi şart ve cevap cümlelerinin ikisidir (Dürre); النَّفَاد: tükenmek"),
    HD("تَذْيِيلٌ جَارٍ مَجْرَى الْمَثَلِ: عَقَّبَ قَوْلَهُ «أَرَى الْعَيْشَ كَنْزًا نَاقِصًا» بِجُمْلَةٍ تَشْتَمِلُ عَلَى مَعْنَاهُ لِلتَّوْكِيدِ، تَسْتَقِلُّ بِنَفْسِهَا (وَبِهَذَا الْمَعْنَى شَرَحَهُ الزَّوْزَنِيُّ: «وَمَا لَا يَزَالُ يَنْقُصُ فَإِنَّ مَآلَهُ إِلَى النَّفَادِ»)", "a tadhyil that runs as a proverb: he follows «I see life as a dwindling treasure» with a clause that holds its meaning, to confirm it, and stands on its own (so al-Zawzanī explains it: «what keeps lessening must come to nothing»)", "darb-ı mesel yerine geçen tezyîl: «hayatı eksilen bir hazine görürüm» sözünü, onun mânâsını içeren ve kendi başına durabilen bir cümleyle te'kid için izlemiştir (Zevzenî de böyle açıklar: «durmadan eksilen şeyin sonu tükenmektir»)"), who=("هُوَ", "مَا"), by="jawab", q=True, g=["tadhyil"]),
])
V(67, "By your life! Death, all the while it misses a young man, is like a long tether let out, whose two ends are in the hand.",
  "Ömrüne andolsun ki ölüm, bir yiğidi ıskaladığı sürece, salıverilmiş uzun bir otlak ipi gibidir; iki ucu da eldedir.", [
 NO("لَعَمْرُكَ", "amr-qasam", R("mub"), nt("وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي؛ الْعَمْرُ وَالْعُمْرُ وَالْعُمُرُ بِمَعْنًى، وَلَا يُسْتَعْمَلُ فِي الْقَسَمِ إِلَّا بِفَتْحِ الْعَيْنِ (الزَّوْزَنِيُّ)", "its predicate must be left out — «is my oath»; العَمْر, العُمْر and العُمُر mean one thing, and in an oath only the fatha on the ʿayn is used (al-Zawzanī)", "haberi vücûben mahzûftur: «yeminimdir»; العَمْر, العُمْر ve العُمُر aynı anlamdadır; yeminde yalnız ayn'ın fethasıyla kullanılır (Zevzenî)", "hadhf-wa-taqdir", "huruf-al-qasam-fil-kafiya"), enc="كَ", pre="la-ibtida"),
 PT("إِنَّ", "inna", INNA_T, JM("qasam")),
 NO("الْمَوْتَ", "mawt", R("ism:إِنَّ")),
 PT("مَا", "ma-masdariyya", mk("حَرْفٌ مَصْدَرِيٌّ ظَرْفِيٌّ", "A masdar-making particle of time («as long as»)", "Zaman bildiren masdar harfi («-dığı sürece»)", "anwa-ma"), nt("وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ، أَيْ: مُدَّةَ إِخْطَائِهِ الْفَتَى (الزَّوْزَنِيُّ)، مُتَعَلِّقٌ بِمَا فِي «إِنَّ» مِنْ مَعْنَى الْفِعْلِ (الدُّرَّةُ)", "the masdar so made is in the seat of nasb as an adverb of time — «for the time it misses the young man» (al-Zawzanī), hanging on the verbal sense in إِنَّ (al-Durra)", "te'vil edilen masdar zarf olarak mahallen mansûb: «yiğidi ıskaladığı müddetçe» (Zevzenî); «إِنَّ»deki fiil mânâsına müteallik (Dürre)")),
 VB("أَخْطَأَ", "akhtaa", "madi", JM("sila"), nt("أَيْ: جَاوَزَهُ", "that is, passed him by", "yani onu geçip gitti"), who=("هُوَ", "الْمَوْتَ"), g=["form-iv-verbs"]),
 NO("الْفَتَى", "fata-youth", R("maf", "maq"), p=HEMI),
 NO("لَكَالطِّوَلِ", "tiwal", R("maj"), ONH("kh", "إِنَّ"), nt("الطِّوَلُ: الْحَبْلُ الَّذِي يُطَوَّلُ لِلدَّابَّةِ فَتَرْعَى فِيهِ", "الطِّوَل: the rope let out long for a beast so that it may graze", "الطِّوَل: hayvan otlasın diye uzatılan ip"),
    TSB("tm", ("الْمَوْتُ فِي إِمْهَالِهِ الْفَتَى وَقُدْرَتِهِ عَلَيْهِ مَتَى شَاءَ", "death, letting the young man run while able to take him when it will", "ölümün, yiğide mühlet verip dilediği an onu yakalayabilmesi"), ("حَبْلٌ طُوِّلَ لِلدَّابَّةِ تَرْعَى فِيهِ وَطَرَفَاهُ بِيَدِ صَاحِبِهَا", "a tether let out for a grazing beast, its two ends in its owner's hand", "otlayan hayvana uzatılmış, iki ucu sahibinin elinde olan ip"), "ka"),
    ZW("لَمَّا جَعَلَ الْمَوْتَ بِمَنْزِلَةِ صَاحِبِ الدَّابَّةِ الَّتِي أَرْخَى طِوَلَهَا قَالَ: مَتَى شَاءَ الْمَوْتُ قَادَ الْفَتَى لِهَلَاكِهِ", "having made death stand as the owner of a beast whose tether he has let out, he means: whenever death wills, it leads the young man to his ruin", "ölümü, ipini salıvermiş hayvan sahibi yerine koyunca şunu demiş olur: ölüm ne zaman dilerse yiğidi helâkine sürükler"), pre="la-ibt+ka", g=TSB_TAGS),
 NO("الْمُرْخَى", "murkha", NA("الطِّوَلِ", "jarr", "maq"), nt("وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ؛ الْإِرْخَاءُ: الْإِرْسَالُ", "its deputy doer is hidden in it; الإِرْخَاء: letting loose", "nâib-i fâili içinde gizlidir; الإِرْخَاء: salıvermek", "ism-maful")),
 NO("وَثِنْيَاهُ", "thiny", R("mub", "alif"), NUN_IDF, nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الطِّوَلِ الْمُرْخَى»، وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ؛ الثِّنْيُ: الطَّرَفُ، أَيْ: طَرَفَاهُ (الزَّوْزَنِيُّ)؛ وَجَعَلَهُ الدُّرَّةُ مُفْرَدًا مَقْصُورًا مَرْفُوعًا بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", "the clause is a hal of «الطِّوَلِ الْمُرْخَى», tied by the waw and the pronoun; الثِّنْي: the end — «its two ends» (al-Zawzanī); al-Durra takes it as a maqsur singular in raf' by a damma estimated on the alif", "cümle «الطِّوَلِ الْمُرْخَى»den hâl olarak mahallen mansûb; râbıt vâv ve zamirdir; الثِّنْي: uç — «iki ucu» (Zevzenî); Dürre onu elif üzerinde takdîrî damme ile merfû maksûr bir müfred sayar"), enc="هُ", pre="wa-hal"),
 NO("بِالْيَدِ", "yad", R("maj"), ONH("kh", "ثِنْيَاهُ"), pre="bi"),
])
# ---- The reproach of his cousin Mālik: verses 68–73 ----------------------------------------------------------------------
MALIK = ("مَالِكٍ", "Mālik", "Mâlik'e")
V(68, "Why is it that I see myself and my cousin Mālik thus: whenever I draw near to him, he moves off from me and keeps away?",
  "Bana ne oluyor ki kendimi ve amcamın oğlu Mâlik'i şöyle görüyorum: ona ne zaman yaklaşsam benden uzaklaşır, ırak durur?", [
 PT("فَمَا", "ma-istifham", mk("اسْمُ اسْتِفْهَامٍ يُفِيدُ التَّعَجُّبَ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "An interrogative noun with the sense of wonder, built on sukun, in the seat of raf' as mubtada", "Taaccüp ifade eden istifham ismi; sükûn üzere mebnî, mübteda olarak mahallen merfû", "al-istifham", "mubtada-khabar"), JM("ist"),
    S_(mk("وَفِيهِ اسْتِفْهَامٌ خَرَجَ عَنْ مَعْنَاهُ إِلَى التَّعَجُّبِ، سَمَّاهُ الدُّرَّةُ «مُفِيدًا لِلتَّعَجُّبِ»، وَقَالَ الزَّوْزَنِيُّ: «يَسْتَغْرِبُ هِجْرَانَهُ إِيَّاهُ مَعَ تَقَرُّبِهِ مِنْهُ»", "The question has left its meaning for wonder: al-Durra calls it «conveying wonder», and al-Zawzanī says: «he marvels at his cousin's shunning him though he draws near to him»", "İstifham anlamından çıkıp taaccübe geçmiştir: Dürre onu «taaccüp ifade eden» diye anar; Zevzenî der ki: «kendisi yaklaştığı hâlde amcaoğlunun ondan uzaklaşmasına şaşar»", "khuruj-al-istifham")), pre="fa-ist", pos="pron"),
 PJ("لِي", "لِ", "li", "ي", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِـ«مَا»", "the phrase hangs on the omitted predicate of «مَا»", "câr-mecrûr «مَا»nın mahzûf haberine müteallik")),
 VB("أَرَانِي", "raa", "mud-a", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ يَاءِ «لِي»، وَهُوَ أَقْوَى مِنْ جَعْلِهَا ابْتِدَائِيَّةً (الدُّرَّةُ)؛ وَكَوْنُ الْفَاعِلِ وَالْمَفْعُولِ ضَمِيرَيْنِ لِمُسَمًّى وَاحِدٍ مِنْ خَصَائِصِ أَفْعَالِ الْقُلُوبِ", "the clause is a hal of the ya of «لِي», in the seat of nasb — stronger, al-Durra says, than taking it as opening the speech; a doer and object that are pronouns of one person is a mark of the verbs of the heart", "cümle «لِي»deki yâ'dan hâl olarak mahallen mansûb — Dürre'ye göre ibtidâiyye saymaktan daha güçlüdür; fâil ile mef'ûlün aynı kişiye ait iki zamir olması kalp fiillerinin özelliğidir", "al-mutaaddi-wa-afal-al-qulub"), who="أَنَا", enc="نِي", g=["naqis-verbs"]),
 NO("وَابْنَ", "ibn", mk("مَعْطُوفٌ عَلَى يَاءِ الْمُتَكَلِّمِ فِي «أَرَانِي» مَنْصُوبٌ بِالْفَتْحَةِ", "Conjoined to the speaker's ya in «أَرَانِي», in nasb by the fatha", "«أَرَانِي»deki mütekellim yâsına ma'tûf, fetha ile mansûb", "atf-nasaq") + MUD, pre="wa"),
 NO("عَمِّي", "amm-uncle", R("mi", "yam"), enc="ي"),
 NO("مَالِكًا", "malik-name", BD("ابْنَ عَمِّي", "nasb"), nt("أَوْ عَطْفُ بَيَانٍ عَلَيْهِ (الدُّرَّةُ)", "or an explaining apposition to it (al-Durra)", "ya da ona atf-ı beyândır (Dürre)", "atf-bayan"), pos="propn", p=HEMI),
 PT("مَتَى", "mata", MATA_SH + mk("، مُتَعَلِّقٌ بِـ«أَدْنُ»", ", hanging on «أَدْنُ»", ", «أَدْنُ»ya müteallik"), nt("وَالْجُمْلَةُ الشَّرْطِيَّةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ«أَرَى» (الدُّرَّةُ)", "the conditional sentence is the second object of «أَرَى», in the seat of nasb (al-Durra)", "şart cümlesi «أَرَى»nın ikinci mef'ûlü olarak mahallen mansûb (Dürre)")),
 VB("أَدْنُ", "dana", "jz-ill", who="أَنَا", by="shart", g=["naqis-verbs"]),
 PJ("مِنْهُ", "مِنْ", "min", "هُ", ON("أَدْنُ"), ref="مَالِكًا"),
 VB("يَنْأَ", "naa", "jz-ill", JM("jz"),
    HD("طِبَاقٌ بَيْنَ «أَدْنُ» وَ«يَنْأَ»: الدُّنُوُّ وَالنَّأْيُ", "«أَدْنُ» and «يَنْأَ» make a tibaq — drawing near against moving away", "«أَدْنُ» ile «يَنْأَ» arasında tıbâk vardır: yaklaşmak ile uzaklaşmak"), who=("هُوَ", MALIK), by="jawab", g=["naqis-verbs", "tibaq"]),
 PJ("عَنِّي", "عَنْ", "an", "ي", ON("يَنْأَ")),
 VB("وَيَبْعُدِ", "baada", "jz", nt("وَيَجُوزُ فِي الْمُضَارِعِ الْمَعْطُوفِ عَلَى جَوَابِ الشَّرْطِ الرَّفْعُ وَالنَّصْبُ، وَلٰكِنَّ الْقَافِيَةَ لَا تُبِيحُ غَيْرَ الْجَزْمِ (الدُّرَّةُ)", "a present verb conjoined to the answer of a condition may also be in raf' or nasb, but the rhyme allows only jazm (al-Durra)", "şartın cevabına ma'tûf muzâride ref' ve nasb da câizdir; fakat kafiye cezmden başkasına izin vermez (Dürre)"),
    ZW("النَّأْيُ وَالْبُعْدُ وَاحِدٌ، فَجَمَعَ بَيْنَهُمَا لِلتَّأْكِيدِ وَإِثْبَاتِ الْقَافِيَةِ", "النَّأْي and البُعْد are one; he joins them for emphasis and to make the rhyme", "النَّأْي ile البُعْد birdir; ikisini te'kid için ve kafiyeyi kurmak için bir araya getirmiştir"),
    S_(mk("فَهُوَ إِطْنَابٌ بِعَطْفِ الْمُرَادِفِ لِلتَّأْكِيدِ، كَمَا قَالَ الزَّوْزَنِيُّ", "So it is an amplification by joining a synonym, for emphasis, as al-Zawzanī says", "Bu, te'kid için müradifi atfetmekle yapılmış bir ıtnâbdır; Zevzenî böyle der", "asbab-al-itnab")), who=("هُوَ", MALIK), by="atf-jawab", pre="wa", q=True),
])
V(69, "He blames me — and I know not why he blames me — as Qurṭ son of Maʿbad blamed me among the tribe.",
  "Beni kınıyor — ve neden kınadığını bilmiyorum — tıpkı Kurt b. Ma'bed'in kabile içinde beni kınadığı gibi.", [
 VB("يَلُومُ", "lama", "mud", JM("ist"), who=("هُوَ", MALIK), g=["hollow-verbs"]),
 PT("وَمَا", "ma-nafiya", MA_NAFY, nt("وَجُمْلَةُ «مَا أَدْرِي…» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «يَلُومُ»، وَالرَّابِطُ الْوَاوُ؛ وَإِنْ عُدَّتْ مُعْتَرِضَةً فَلَا مَحَلَّ لَهَا (الدُّرَّةُ)", "the clause «مَا أَدْرِي…» is a hal of the doer of «يَلُومُ», in the seat of nasb, tied by the waw; taken as a parenthesis it has no seat (al-Durra)", "«مَا أَدْرِي…» cümlesi «يَلُومُ»un fâilinden hâl olarak mahallen mansûb, râbıt vâvdır; mu'tarıza sayılırsa mahalli yoktur (Dürre)"), pre="wa-hal"),
 VB("أَدْرِي", "dara", "mud-y", nt("وَقَدْ عُلِّقَ عَنِ الْعَمَلِ لَفْظًا بِالِاسْتِفْهَامِ بَعْدَهُ", "it is held back from governing in form by the question after it", "sonraki istifham sebebiyle lafzen amelden alıkonmuştur", "al-mutaaddi-wa-afal-al-qulub"), who="أَنَا", g=["naqis-verbs"]),
 PT("عَلَامَ", "ma-istifham", mk("عَلَى حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، حُذِفَتْ أَلِفُهُ لِدُخُولِ حَرْفِ الْجَرِّ عَلَيْهِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَلُومُنِي»", "عَلَى is a jarr letter, and مَا an interrogative noun built on sukun in the seat of jarr, its alif dropped because a jarr letter has come upon it; the phrase hangs on «يَلُومُنِي»", "عَلَى cer harfi; مَا sükûn üzere mebnî istifham ismi, mahallen mecrûr; cer harfi girdiği için elifi düşmüştür; câr-mecrûr «يَلُومُنِي»ye müteallik", "al-istifham", "huruf-jarr"), pos="pron"),
 VB("يَلُومُنِي", "lama", "mud", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ مَفْعُولَيْ «أَدْرِي»", "the clause fills the place of the two objects of «أَدْرِي», in the seat of nasb", "cümle «أَدْرِي»nin iki mef'ûlünün yerini tutar, mahallen mansûb"), who=("هُوَ", MALIK), enc="نِي", g=["hollow-verbs"], p=HEMI),
 PT("كَمَا", "kama", mk("الْكَافُ حَرْفُ تَشْبِيهٍ وَجَرٍّ، وَمَا مَصْدَرِيَّةٌ", "The kaf is the jarr letter of likening, and مَا makes a masdar", "Kâf teşbih ve cer harfi; مَا masdariyye", "huruf-jarr", "anwa-ma"),
    nt("وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: يَلُومُ لَوْمًا كَلَوْمِ قُرْطٍ (الدُّرَّةُ)", "the masdar is in the seat of jarr by the kaf, and the phrase hangs on the omitted adjective of an omitted absolute object — «he blames with a blame like Qurṭ's» (al-Durra)", "masdar kâf ile mahallen mecrûr; câr-mecrûr mahzûf bir mef'ûlün mutlakın mahzûf sıfatına müteallik: «Kurt'un kınaması gibi bir kınamayla kınar» (Dürre)", "maful-mutlaq"),
    TSB("mm", ("لَوْمُ مَالِكٍ إِيَّاهُ", "Mālik's blaming him", "Mâlik'in onu kınaması"), ("لَوْمُ قُرْطٍ إِيَّاهُ", "Qurṭ's blaming him", "Kurt'un onu kınaması"), "kama"),
    ZW("يُرِيدُ أَنَّ لَوْمَهُ إِيَّاهُ ظُلْمٌ صُرَاحٌ كَمَا كَانَ لَوْمُ قُرْطٍ إِيَّاهُ كَذٰلِكَ", "he means that Mālik's blame of him is plain wrong, as Qurṭ's blame of him was", "Mâlik'in onu kınamasının, Kurt'unki gibi apaçık bir zulüm olduğunu kasteder"), g=TSB_TAGS),
 VB("لَامَنِي", "lama", "madi", JM("sila"), enc="نِي", g=["hollow-verbs"]),
 HJ("فِي", "fi"),
 NO("الْحَيِّ", "hayy-tribe", R("maj"), ON("لَامَنِي")),
 NO("قُرْطُ", "qurt-name", "fail", nt("رَجُلٌ مِنَ الْقَبِيلَةِ", "a man of the tribe", "kabileden bir adam"), pos="propn"),
 IBN("raf"),
 NO("مَعْبَدِ", "mabad-name", "mi", nt("وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «أَعْبَدِ»", "al-Tibrīzī and al-Durra have «أَعْبَدِ»", "Tebrîzî ve Dürre'de «أَعْبَدِ»"), pos="propn", q=True),
])
V(70, "He has made me despair of every good I sought from him, as though we had laid it in the grave of one buried in his niche.",
  "Ondan istediğim her hayırdan beni ümitsiz bıraktı; sanki onu lahdine gömülmüş birinin kabrine koymuşuz gibi.", [
 VB("وَأَيْأَسَنِي", "ayasa", "madi", JM("atf", "يَلُومُ"), nt("أَيْ: قَنَّطَنِي مَالِكٌ (الزَّوْزَنِيُّ)", "that is, Mālik made me lose hope (al-Zawzanī)", "yani Mâlik beni ümitsizliğe düşürdü (Zevzenî)"), who=("هُوَ", MALIK), enc="نِي", pre="wa", g=["form-iv-verbs"]),
 HJ("مِنْ", "min"),
 NO("كُلِّ", "kull", R("maj") + MUD, ON("أَيْأَسَنِي")),
 NO("خَيْرٍ", "khayr", "mi"),
 VB("طَلَبْتُهُ", "talaba", "madi-tu", JM("sifa", "خَيْرٍ"), enc="هُ", p=HEMI),
 PT("كَأَنَّا", "kaanna", KAANNA_T + mk("، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; نَا is its noun, in the seat of nasb", "; نَا ismi, mahallen mansûb"), nt("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِـ«خَيْرٍ» إِنْ لَمْ تُعَدَّ مُسْتَأْنَفَةً (الدُّرَّةُ)", "the clause is a second adjective of «خَيْرٍ», in the seat of jarr, unless it is taken as opening a new sentence (al-Durra)", "cümle, istînâfiyye sayılmazsa «خَيْرٍ»in ikinci na'tı olarak mahallen mecrûr (Dürre)"),
    TSB("tm", ("يَأْسُهُ مِنْ خَيْرِ مَالِكٍ", "his despair of any good from Mālik", "Mâlik'ten bir hayır görmekten ümidini kesmesi"), ("طَلَبٌ وُضِعَ فِي قَبْرِ مَيِّتٍ لَا يُرْجَى خَيْرُهُ", "a request laid in the grave of a dead man, whose good none hopes for", "hayrı umulmayan bir ölünün kabrine konmuş bir istek"), "kaanna"),
    ZW("يُرِيدُ أَنَّهُ آيَسَهُ مِنْ كُلِّ خَيْرٍ طَلَبَهُ كَمَا أَنَّ الْمَيِّتَ لَا يُرْجَى خَيْرُهُ", "he means that Mālik made him despair of every good he sought, as no good is hoped for from the dead", "ölünün hayrının umulmadığı gibi, Mâlik'in de onu istediği her hayırdan ümitsiz bıraktığını kasteder"), stem="كَأَنَّا", g=TSB_TAGS),
 VB("وَضَعْنَاهُ", "wadaa", "madi-na", JM("kh", "كَأَنَّ", "raf"), enc="هُ"),
 HJ("إِلَى", "ila"),
 NO("رَمْسِ", "rams", R("maj") + MUD, ON("وَضَعْنَاهُ"), nt("الرَّمْسُ: الْقَبْرُ، وَأَصْلُهُ الدَّفْنُ", "الرَّمْس: the grave — first, burying", "الرَّمْس: kabir — aslı gömmektir")),
 NO("مُلْحَدِ", "mulhad", "mi", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: رَجُلٍ مُلْحَدٍ (الزَّوْزَنِيُّ: «قَبْرِ رَجُلٍ مَدْفُونٍ فِي اللَّحْدِ»)؛ أَلْحَدْتُ الرَّجُلَ: جَعَلْتُ لَهُ لَحْدًا", "it describes a noun left out — «a man laid in his niche» (al-Zawzanī: «the grave of a man buried in the niche»); أَلْحَدْتُ الرَّجُلَ: I made him a burial niche", "mahzûf bir mevsûfun sıfatıdır: «lahde konmuş bir adam» (Zevzenî: «lahde gömülmüş bir adamın kabri»); أَلْحَدْتُ الرَّجُلَ: ona lahit yaptım", "hadhf-wa-taqdir", "ism-maful"), q=True),
])
V(71, "— for nothing I had said, except that I went searching and did not neglect the camels of Maʿbad.",
  "— söylediğim hiçbir şey yüzünden değil; yalnız şu kadar var ki aradım ve Ma'bed'in yük develerini ihmal etmedim.", [
 HJ("عَلَى", "ala", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: يَلُومُنِي (الدُّرَّةُ)", "the phrase hangs on a verb left out, «he blames me» (al-Durra)", "câr-mecrûr mahzûf «يَلُومُنِي» fiiline müteallik (Dürre)", "hadhf-wa-taqdir")),
 NO("غَيْرِ", "ghayr", R("maj") + MUD),
 NO("شَيْءٍ", "shay", "mi", nt("وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «ذَنْبٍ»", "al-Tibrīzī and al-Durra have «ذَنْبٍ»", "Tebrîzî ve Dürre'de «ذَنْبٍ»")),
 VB("قُلْتُهُ", "qala", "madi-tu", JM("sifa", "شَيْءٍ"), enc="هُ", g=["hollow-verbs"]),
 NO("غَيْرَ", "ghayr", mk("مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ الْمُنْقَطِعِ بِالْفَتْحَةِ", "In nasb by the fatha, as a cut-off exception", "Munkatı' istisna olarak fetha ile mansûb", "istithna") + MUD,
    ZW("وَقَوْلُهُ «غَيْرَ أَنَّنِي» اسْتِثْنَاءٌ مُنْقَطِعٌ تَقْدِيرُهُ: وَلٰكِنَّنِي", "«غَيْرَ أَنَّنِي» is a cut-off exception: «but I…»", "«غَيْرَ أَنَّنِي» munkatı' istisnadır; takdiri: «fakat ben…»"),
    HD("تَأْكِيدُ الْمَدْحِ بِمَا يُشْبِهُ الذَّمَّ: نَفَى عَنْ نَفْسِهِ مَا يُلَامُ عَلَيْهِ، ثُمَّ اسْتَثْنَى صِفَةَ مَدْحٍ — قِيَامَهُ بِحَقِّ أَخِيهِ — بِأَدَاةِ الِاسْتِثْنَاءِ كَأَنَّهَا ذَنْبٌ", "a praise made firm by what looks like blame: he denies any ground for blame, then excepts a thing to his credit — standing by his brother's right — with the particle of exception, as though it were a fault", "zemme benzeyen bir sözle övgüyü pekiştirme: kınanacak bir şeyi kendinden nefyetmiş, sonra kardeşinin hakkını gözetmesi gibi övgüye değer bir vasfı, sanki bir kusurmuş gibi istisna edatıyla istisna etmiştir"), g=["takid-al-madh-wal-dhamm"]),
 PT("أَنَّنِي", "anna", INNA_T + mk("، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the nun guards its ending, and the ya is its noun, in the seat of nasb", "; nûn vikâye içindir; yâ ismi, mahallen mansûb"), nt("وَ«أَنَّ» وَمَعْمُولَاهَا فِي تَأْوِيلِ مَصْدَرٍ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «غَيْرَ» إِلَيْهِ", "أَنَّ with its two terms is read as a masdar in the seat of jarr, «غَيْرَ» being annexed to it", "«أَنَّ» ve iki ma'mûlü, «غَيْرَ»nin ona izâfetiyle mahallen mecrûr bir masdar te'vilindedir", "mawadi-fath-anna"), stem="أَنَّنِي", p=HEMI),
 VB("نَشَدْتُ", "nashada", "madi-tu", JM("kh", "أَنَّ", "raf"), nt("النِّشْدَانُ: طَلَبُ الْمَفْقُودِ", "النِّشْدَان: searching for what is lost", "النِّشْدَان: kaybolanı aramak")),
 PT("فَلَمْ", "lam-jazima", LAM_J, pre="fa"),
 VB("أُغْفِلْ", "aghfala", "jz", JM("atf", "نَشَدْتُ"), nt("الْإِغْفَالُ: التَّرْكُ", "الإِغْفَال: leaving neglected", "الإِغْفَال: ihmal edip bırakmak"), who="أَنَا", by="lam", g=["form-iv-verbs"]),
 NO("حَمُولَةَ", "hamula-ant", R("maf") + MUD, nt("الْحَمُولَةُ: الْإِبِلُ الَّتِي تُطِيقُ أَنْ يُحْمَلَ عَلَيْهَا", "الحَمُولَة: camels strong enough to carry loads", "الحَمُولَة: yük taşıyabilecek develer")),
 NO("مَعْبَدِ", "mabad-name", "mi", nt("مَعْبَدٌ: أَخُوهُ (الزَّوْزَنِيُّ)؛ يَقُولُ: طَلَبْتُ إِبِلَ أَخِي وَلَمْ أَتْرُكْهَا، فَنَقَمَ ذٰلِكَ مِنِّي", "Maʿbad was his brother (al-Zawzanī); he says: I sought my brother's camels and did not let them go, and Mālik held it against me", "Ma'bed kardeşidir (Zevzenî); der ki: kardeşimin develerini aradım, onları bırakmadım; Mâlik de bunu bana kin sebebi yaptı"), pos="propn", q=True),
])
V(72, "I drew near him by our kinship — by your fortune! — and truly, whenever there comes a matter of utmost strain, I am there.",
  "Akrabalığımızla ona yakınlaştım — talihine andolsun! — doğrusu, ne zaman güç yetirmenin son sınırını gerektiren bir iş çıksa, orada bulunurum.", [
 VB("وَقَرَّبْتُ", "qarraba", "madi-tu", JM("atf", "نَشَدْتُ"), nt("وَالْمَفْعُولُ مَحْذُوفٌ، أَيْ: قَرَّبْتُ نَفْسِي (الزَّوْزَنِيُّ)", "the object is left out — «I brought myself near» (al-Zawzanī)", "mef'ûl mahzûftur: «kendimi yaklaştırdım» (Zevzenî)", "hadhf-al-maful"), pre="wa", g=["form-ii-verbs"]),
 NO("بِالْقُرْبَى", "qurba", R("maj", "maq"), ON("قَرَّبْتُ"), nt("الْقُرْبَى: اسْمٌ مِنَ الْقُرْبِ وَالْقَرَابَةِ، وَهُوَ أَصَحُّ الْقَوْلَيْنِ، وَقِيلَ: جَمْعُ قُرْبَةٍ (الزَّوْزَنِيُّ)", "القُرْبَى: a noun from nearness and kinship — the sounder view; also said to be the plural of قُرْبَة (al-Zawzanī)", "القُرْبَى: yakınlık ve akrabalıktan bir isimdir — en sahih görüş budur; «قُرْبَة»nın cem'i olduğu da söylenmiştir (Zevzenî)"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «قَرَّبْتُ» وَ«الْقُرْبَى» الِاشْتِقَاقُ", "a figure joined to jinas: «قَرَّبْتُ» and «الْقُرْبَى» are brought together by derivation", "cinâsa mülhak: «قَرَّبْتُ» ile «الْقُرْبَى»yı iştikak bir araya getirmiştir"), pre="bi", g=["mulhaq-bil-jinas"]),
 NO("وَجَدِّكَ", "jadd", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُقْسِمُ؛ أَيْ: أُقْسِمُ بِحَظِّكَ وَبَخْتِكَ (الزَّوْزَنِيُّ)", "the phrase hangs on a verb left out, «I swear» — «I swear by your fortune and luck» (al-Zawzanī)", "câr-mecrûr mahzûf «أُقْسِمُ» fiiline müteallik — «talihine ve bahtına yemin ederim» (Zevzenî)", "huruf-al-qasam-fil-kafiya"), enc="كَ", pre="wa-qasam"),
 PT("إِنَّنِي", "inna", INNA_T + mk("، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the nun guards its ending, and the ya is its noun, in the seat of nasb", "; nûn vikâye içindir; yâ ismi, mahallen mansûb"), JM("qasam"), stem="إِنَّنِي", p=HEMI),
 PT("مَتَى", "mata", MATA_SH + mk("، مُتَعَلِّقٌ بِفِعْلِ شَرْطِهِ", ", hanging on its condition's verb", ", şart fiiline müteallik"), nt("وَالْجُمْلَةُ الشَّرْطِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «إِنَّ» (الدُّرَّةُ)", "the conditional sentence is the predicate of «إِنَّ», in the seat of raf' (al-Durra)", "şart cümlesi «إِنَّ»nin haberi olarak mahallen merfû (Dürre)")),
 PT("يَكُ", "kana", mk("فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ لِأَنَّهُ فِعْلُ الشَّرْطِ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ عَلَى النُّونِ الْمَحْذُوفَةِ لِلتَّخْفِيفِ", "A defective present verb in jazm as the condition's verb, its sign the sukun on the nun, which is dropped to lighten the word", "Şart fiili olarak meczûm nâkıs muzâri; cezm alâmeti, hafiflik için düşürülen nûn üzerindeki sükûn", "kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza"), pos="verb"),
 NO("أَمْرٌ", "amr", R("ism:يَكُ")),
 NO("لِلنَّكِيثَةِ", "nakitha", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «يَكُ»؛ النَّكِيثَةُ: الْمُبَالَغَةُ فِي الْجَهْدِ وَأَقْصَى الطَّاقَةِ", "the phrase hangs on the omitted predicate of «يَكُ»; النَّكِيثَة: the utmost of effort, the very limit of strength", "câr-mecrûr «يَكُ»nun mahzûf haberine müteallik; النَّكِيثَة: gayretin en ileri derecesi, gücün son sınırı"), pre="li"),
 VB("أَشْهَدِ", "shahida", "jz", JM("jz"), nt("أَيْ: أَحْضُرْهُ وَأَنْصُرْهُ (الزَّوْزَنِيُّ)", "that is, I am there and give help (al-Zawzanī)", "yani orada bulunur ve yardım ederim (Zevzenî)"), who="أَنَا", by="jawab", q=True),
])
V(73, "If I am called to a grave matter, I am among its defenders; and if the enemies come at you with hardship, I strive my utmost.",
  "Büyük bir iş için çağrılırsam onun koruyucularından olurum; düşmanlar sana zorlukla gelirse, var gücümle çabalarım.", [
 PT("وَإِنْ", "in-shartiyya", IN_SH, JM("ist"), pre="wa-ist"),
 VB("أُدْعَ", "daa", "jz-ill", who="أَنَا", by="shart", maj=True, g=["naqis-verbs"]),
 NO("لِلْجُلَّى", "julla", R("maj", "maq"), ON("أُدْعَ"), nt("وَيُرْوَى «فِي الْجُلَّى» (التِّبْرِيزِيُّ، الدُّرَّةُ)؛ الْجُلَّى: تَأْنِيثُ الْأَجَلِّ، وَهِيَ الْخُطَّةُ الْعَظِيمَةُ", "also transmitted «فِي الْجُلَّى» (al-Tibrīzī, al-Durra); الجُلَّى: the feminine of الأَجَلّ — a grave affair", "«فِي الْجُلَّى» diye de rivayet edilir (Tebrîzî, Dürre); الجُلَّى: الأَجَلّ'ın müennesi — büyük iş"), pre="li"),
 PT("أَكُنْ", "kana", mk("فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ لِأَنَّهُ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا", "A defective present verb in jazm as the answer of the condition, its sign the sukun; its noun is the hidden «I»", "Şartın cevabı olarak meczûm nâkıs muzâri, cezm alâmeti sükûn; ismi vücûben gizli «أَنَا»", "kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza"), JM("jz"), pos="verb"),
 HJ("مِنْ", "min"),
 NO("حُمَاتِهَا", "hamin-ant", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «أَكُنْ»؛ الْحُمَاةُ: جَمْعُ الْحَامِي", "the phrase hangs on the omitted predicate of «أَكُنْ»; الحُمَاة: the plural of الحَامِي, a defender", "câr-mecrûr «أَكُنْ»un mahzûf haberine müteallik; الحُمَاة: الحَامِي'nin (koruyucu) cem'i", "jam-taksir"), enc="هَا", p=HEMI),
 PT("وَإِنْ", "in-shartiyya", IN_SH, pre="wa"),
 VB("يَأْتِكَ", "ata", "jz-ill", by="shart", enc="كَ", g=["naqis-verbs"]),
 NO("الْأَعْدَاءُ", "aduww", "fail", g=["jam-taksir"]),
 NO("بِالْجَهْدِ", "juhd", R("maj"), ON("يَأْتِ"), nt("وَقِيلَ: الْبَاءُ زَائِدَةٌ، فَيَكُونُ «الْجَهْدِ» مَفْعُولًا مُطْلَقًا لِـ«أَجْهَدِ» قُدِّمَ عَلَيْهِ، مَجْرُورًا لَفْظًا مَنْصُوبًا مَحَلًّا (الدُّرَّةُ)؛ وَبِزِيَادَةِ الْبَاءِ قَالَ الزَّوْزَنِيُّ", "also said: the ba is added, and «الْجَهْدِ» is an absolute object of «أَجْهَدِ» set before it, in jarr in form and in nasb in its seat (al-Durra) — al-Zawzanī holds the ba to be added", "bâ'nın zâid olduğu da söylenmiştir; o zaman «الْجَهْدِ», «أَجْهَدِ»nin öne alınmış mef'ûlün mutlakı olur, lafzen mecrûr, mahallen mansûb (Dürre) — Zevzenî de bâ'nın zâid olduğunu söyler"), pre="bi"),
 VB("أَجْهَدِ", "jahada", "jz", JM("jz"), nt("أَيْ: أَجْهَدْ فِي دَفْعِهِمْ عَنْكَ غَايَةَ الْجَهْدِ (الزَّوْزَنِيُّ)", "that is, I strive to the very utmost to drive them off you (al-Zawzanī)", "yani onları senden savmak için son derece gayret ederim (Zevzenî)"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «الْجَهْدِ» وَ«أَجْهَدِ» الِاشْتِقَاقُ", "a figure joined to jinas: «الْجَهْدِ» and «أَجْهَدِ» are brought together by derivation", "cinâsa mülhak: «الْجَهْدِ» ile «أَجْهَدِ»yi iştikak bir araya getirmiştir"), who="أَنَا", by="jawab", q=True, g=["mulhaq-bil-jinas"]),
])
# ---- The wrong done by one's own kin: verses 74–79 -------------------------------------------------------------------------
MAWLA = ("مَوْلَايَ", "«مَوْلَايَ», his cousin", "«مَوْلَايَ»ya, amcaoğluna")
V(74, "If they cast foul words at your honour, I will make them drink a cup from the pools of death before any threatening.",
  "Senin namusuna çirkin sözler atarlarsa, tehdide bile vakit bırakmadan onlara ölüm havuzlarından bir kadeh içiririm.", [
 PT("وَإِنْ", "in-shartiyya", IN_SH, nt("وَالشَّرْطُ وَجَوَابُهُ مَعْطُوفَانِ عَلَى مِثْلِهِمَا فِي الْبَيْتِ ٧٣ (الدُّرَّةُ)", "the condition and its answer are conjoined to their like in v. 73 (al-Durra)", "şart ve cevabı 73. beyitteki benzerlerine ma'tûftur (Dürre)"), pre="wa"),
 VB("يَقْذِفُوا", "qadhafa", "jz5", nt("وَالْأَلِفُ فَارِقَةٌ؛ الْقَذْفُ: السَّبُّ", "the alif is the separating alif; القَذْف: reviling", "elif fârikadır; القَذْف: sövmek"), by="shart"),
 NO("بِالْقَذْعِ", "qadha", R("maj"), ON("يَقْذِفُوا"), nt("الْقَذْعُ وَالْقَذَعُ: الْفُحْشُ", "القَذْع or القَذَع: foul speech", "القَذْع ya da القَذَع: çirkin söz"), pre="bi"),
 NO("عِرْضَكَ", "ird", "maf", nt("الْعِرْضُ: مَوْضِعُ الْمَدْحِ وَالذَّمِّ مِنَ الْإِنْسَانِ، قَالَهُ ابْنُ دُرَيْدٍ (الزَّوْزَنِيُّ)", "العِرْض: that in a man which is praised or blamed — so Ibn Durayd (al-Zawzanī)", "العِرْض: insanın övülen ve yerilen yanı — İbn Düreyd böyle der (Zevzenî)"), enc="كَ"),
 VB("أَسْقِهِمْ", "saqa-water", "jz-ill", JM("jz"), nt("وَالْهَاءُ أَوَّلُ مَفْعُولَيْهِ، وَالْمِيمُ عَلَامَةُ الْجَمْعِ", "the هِ is the first of its two objects, and the mim marks the plural", "hâ iki mef'ûlünün birincisidir, mîm cem' alâmetidir"), who="أَنَا", by="jawab", enc="هِمْ", g=["naqis-verbs", "mafulayn"], p=HEMI),
 NO("بِكَأْسِ", "kas", mk("مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "The second object, in nasb by an estimated fatha, its place taken by the kasra of the added jarr letter", "İkinci mef'ûl; mahalli zâid cer harfinin harekesi işgal ettiğinden takdîrî fetha ile mansûb", "mafulayn") + MUD, nt("وَيُرْوَى «بِشُرْبِ» (الزَّوْزَنِيُّ)", "also transmitted «بِشُرْبِ», «a drink of» (al-Zawzanī)", "«بِشُرْبِ» diye de rivayet edilir (Zevzenî)"), pre="bi-z"),
 NO("حِيَاضِ", "hawd", R("mi") + MUD, nt("جَمْعُ حَوْضٍ", "the plural of حَوْض, a pool", "«حَوْض»un cem'i: havuz", "jam-taksir")),
 NO("الْمَوْتِ", "mawt", "mi",
    HD("اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَ الْمَوْتُ بِمَاءٍ يُورَدُ وَيُشْرَبُ، وَطُوِيَ الْمُشَبَّهُ بِهِ وَرُمِزَ إِلَيْهِ بِلَوَازِمِهِ: الْحِيَاضِ وَالْكَأْسِ وَالسَّقْيِ (وَعَلَيْهِ شَرْحُ الزَّوْزَنِيِّ: «أَوْرَدْتُهُمْ حِيَاضَ الْمَوْتِ»)", "an implied istiara: death is likened to water one comes down to and drinks; the thing it is likened to is not named but pointed to by what belongs to it — the pools, the cup, the giving to drink (so al-Zawzanī renders it: «I bring them down to the pools of death»)", "istiâre-i mekniyye: ölüm, başına gelinip içilen suya benzetilmiş; müşebbehün bih zikredilmemiş, lâzımları olan havuzlar, kadeh ve içirmekle ona işaret edilmiştir (Zevzenî de böyle açıklar: «onları ölüm havuzlarına indiririm»)"), g=["istiara-makniyya", "istiara"]),
 NO("قَبْلَ", "qabla", R("zz") + MUD, ZON("أَسْقِ")),
 NO("التَّهَدُّدِ", "tahaddud", "mi", nt("التَّهَدُّدُ وَالتَّهْدِيدُ وَاحِدٌ؛ يُرِيدُ أَنَّهُ يُبِيدُهُمْ قَبْلَ تَهْدِيدِهِمْ (الزَّوْزَنِيُّ)", "التَّهَدُّد and التَّهْدِيد are one; he means he destroys them before he threatens them (al-Zawzanī)", "التَّهَدُّد ile التَّهْدِيد birdir; onları tehdit etmeden yok ettiğini kasteder (Zevzenî)", "masdar")),
])
V(75, "— with no wrong that I have done, and like one who has done wrong is my being lampooned, reviled with complaints and driven out.",
  "— işlediğim hiçbir suç olmaksızın; hicvedilmem, şikâyetlerle sövülmem ve kovulmam, suç işlemiş birininki gibidir.", [
 PT("بِلَا", "la-nafiya", mk("الْبَاءُ حَرْفُ جَرٍّ، وَلَا نَافِيَةٌ مُعْتَرِضَةٌ بَيْنَ الْجَارِّ وَمَجْرُورِهِ", "The ba is a jarr letter, and لَا a negation set between the jarr letter and its noun", "Bâ cer harfi; لَا, cer harfi ile mecrûru arasına girmiş nefy harfi", "huruf-jarr", "la-nafiya"), nt("وَإِنْ عُدَّتْ «لَا» اسْمًا بِمَعْنَى «غَيْرٍ» كَانَتْ هِيَ الْمَجْرُورَةَ الْمُضَافَةَ (الدُّرَّةُ)", "if لَا is taken as a noun meaning «other than», it is itself the noun in jarr, annexed (al-Durra)", "«لَا» «غَيْر» anlamında isim sayılırsa mecrûr ve muzâf olan odur (Dürre)")),
 NO("حَدَثٍ", "hadath", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ، أَيْ: أُجْفَى وَأُضَامُ بِلَا حَدَثٍ (الزَّوْزَنِيُّ، الدُّرَّةُ)؛ الْحَدَثُ: الْإِسَاءَةُ تُحْدَثُ", "the phrase hangs on a verb left out — «I am shunned and wronged with no wrong» (al-Zawzanī, al-Durra); الحَدَث: a wrong done", "câr-mecrûr mahzûf bir fiile müteallik: «hiçbir suç olmaksızın dışlanır ve zulme uğrarım» (Zevzenî, Dürre); الحَدَث: işlenen kötülük", "hadhf-wa-taqdir")),
 VB("أَحْدَثْتُهُ", "ahdatha", "madi-tu", JM("sifa", "حَدَثٍ"), enc="هُ", g=["form-iv-verbs"]),
 NO("وَكَمُحْدَثٍ", "muhdath", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ عَلَى رِوَايَةِ فَتْحِ الدَّالِ؛ وَعَلَى رِوَايَةِ كَسْرِهَا «كَمُحْدِثٍ» (التِّبْرِيزِيُّ) خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: هُوَ كَمُحْدِثٍ (الدُّرَّةُ)", "the phrase hangs on an omitted predicate set first, on the reading with a fatha on the dal; on the reading with a kasra, «كَمُحْدِثٍ» (al-Tibrīzī), it is the predicate of an omitted mubtada (al-Durra)", "dâl'ın fethası rivayetinde câr-mecrûr öne geçmiş mahzûf habere müteallik; kesresi rivayetinde «كَمُحْدِثٍ» (Tebrîzî) mahzûf mübtedanın haberidir (Dürre)"),
    TSB("mm", ("مَا يَلْقَاهُ مِنْ هِجَاءٍ وَشَكَاةٍ وَطَرْدٍ", "the lampoons, complaints and driving-out he meets", "uğradığı hiciv, şikâyet ve kovulma"), ("مَا يَلْقَاهُ مَنْ أَحْدَثَ إِسَاءَةً وَجَنَى جِنَايَةً", "what one meets who has done a wrong and committed an offence", "kötülük edip suç işleyen birinin uğradığı muamele"), "ka"),
    ZW("ثُمَّ أُهْجَى وَأُشْكَى وَأُطْرَدُ كَمَا يُهْجَى مَنْ أَحْدَثَ إِسَاءَةً وَجَرَّ جَرِيرَةً", "then I am lampooned, complained of and driven out, as one is lampooned who has done a wrong and brought on a crime", "sonra kötülük edip suça sebep olan biri nasıl hicvedilirse, ben de öyle hicvedilir, şikâyet edilir ve kovulurum"), pre="wa+ka", g=TSB_TAGS, p=HEMI),
 NO("هِجَائِي", "hija", R("mubm", "yam"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ، وَالْفَاعِلُ مَحْذُوفٌ؛ وَعَلَى رِوَايَةِ «كَمُحْدِثٍ» هُوَ مَفْعُولٌ لَهُ (الدُّرَّةُ)", "the masdar annexed to its object, the doer left out; on the reading «كَمُحْدِثٍ» it is that word's object (al-Durra)", "masdarın mef'ûlüne izâfeti, fâil mahzûftur; «كَمُحْدِثٍ» rivayetinde onun mef'ûlüdür (Dürre)", "masdar"), enc="ي"),
 NO("وَقَذْفِي", "qadhf", AT("هِجَائِي", "raf", "yam"), enc="ي", pre="wa"),
 NO("بِالشَّكَاةِ", "shakat", R("maj"), ON("قَذْفِي"), nt("الشِّكَايَةُ وَالشَّكْوَى وَالشَّكِيَّةُ وَالشَّكَاةُ وَاحِدٌ", "الشِّكَايَة, الشَّكْوَى, الشَّكِيَّة and الشَّكَاة are one: complaint", "الشِّكَايَة, الشَّكْوَى, الشَّكِيَّة ve الشَّكَاة birdir: şikâyet"), pre="bi"),
 NO("وَمُطْرَدِي", "mutrad", AT("هِجَائِي", "raf", "yam"), nt("الْمُطْرَدُ بِمَعْنَى الْإِطْرَادِ، وَأَطْرَدْتُهُ: صَيَّرْتُهُ طَرِيدًا", "المُطْرَد means الإِطْرَاد — أَطْرَدْتُهُ: I made him an outcast", "المُطْرَد, الإِطْرَاد anlamındadır — أَطْرَدْتُهُ: onu kovulmuş kıldım", "masdar"), enc="ي", pre="wa"),
])
V(76, "Had my lord been some other man than he, he would have eased my distress, or given me respite till the morrow.",
  "Efendim (amcaoğlum) ondan başka bir adam olsaydı, sıkıntımı giderirdi ya da bana yarına kadar mühlet verirdi.", [
 PT("فَلَوْ", "law", LAW_T, JM("ist"), pre="fa-ist"),
 VB("كَانَ", "kana", "madi", nt("نَاقِصٌ، فِعْلُ شَرْطِ «لَوْ»", "defective, the verb of the condition of لَوْ", "nâkıstır, «لَوْ»nun şart fiili", "kana-wa-akhawatuha"), g=["hollow-verbs"]),
 NO("مَوْلَايَ", "mawla", R("ism:كَانَ", "maq"), nt("أَيِ: ابْنُ عَمِّي (الزَّوْزَنِيُّ)", "that is, my cousin (al-Zawzanī)", "yani amcamın oğlu (Zevzenî)"), enc="يَ"),
 NO("امْرَأً", "imru", R("kh:كَانَ")),
 PT("هُوَ", "huwa", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), pos="pron"),
 NO("غَيْرُهُ", "ghayr", "kh", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«امْرَأً»؛ وَيَجُوزُ نَصْبُ «غَيْرَهُ» نَعْتًا وَ«هُوَ» ضَمِيرُ فَصْلٍ (الدُّرَّةُ)", "the clause is an adjective of «امْرَأً», in the seat of nasb; «غَيْرَهُ» may also be read in nasb as the adjective, with «هُوَ» a separating pronoun (al-Durra)", "cümle «امْرَأً»nın na'tı olarak mahallen mansûb; «غَيْرَهُ»nün na't olarak nasbı ve «هُوَ»nün fasl zamiri olması da câizdir (Dürre)", "jumla-sifa"), enc="هُ", p=HEMI),
 VB("لَفَرَّجَ", "farraja", "madi", JM("jawab", "لَوْ"), nt("فَرَّجْتُ الْأَمْرَ: كَشَفْتُهُ، وَالْفَرَجُ: انْكِشَافُ الْمَكْرُوهِ", "فَرَّجْتُ الأَمْرَ: I cleared it away — الفَرَج is the lifting of what is hateful", "فَرَّجْتُ الأَمْرَ: onu giderdim — الفَرَج: hoşa gitmeyenin kalkması"), who=("هُوَ", MAWLA), pre="la", g=["form-ii-verbs"]),
 NO("كَرْبِي", "karb", R("maf", "yam"), nt("كَرَبَهُ الْغَمُّ: إِذَا مَلَأَ صَدْرَهُ، وَالْكُرْبَةُ اسْمٌ مِنْهُ", "كَرَبَهُ الغَمُّ: grief filled his breast; الكُرْبَة is the noun", "كَرَبَهُ الغَمُّ: tasa göğsünü doldurdu; الكُرْبَة onun ismidir"), enc="ي"),
 PT("أَوْ", "aw", AW_T),
 VB("لَأَنْظَرَنِي", "anzara", "madi", JM("atf", "فَرَّجَ"), nt("الْإِنْظَارُ: الْإِمْهَالُ", "الإِنْظَار: granting respite", "الإِنْظَار: mühlet vermek"), who=("هُوَ", MAWLA), pre="la", enc="نِي", g=["form-iv-verbs"]),
 NO("غَدِي", "ghad", mk("ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُتَعَلِّقٌ بِـ«أَنْظَرَنِي»، وَكُسِرَتْ دَالُهُ لِضَرُورَةِ الشِّعْرِ فَتَوَلَّدَتْ يَاءُ الْإِشْبَاعِ (الدُّرَّةُ)", "An adverb of time in nasb, hanging on «أَنْظَرَنِي»; its dal takes a kasra for the verse's need, and the kasra is drawn out into a ya (al-Durra)", "Zaman zarfı, mansûb, «أَنْظَرَنِي»ye müteallik; şiir zarureti için dâl'ı kesrelenmiş, kesre uzatılıp yâ doğmuştur (Dürre)", "maful-fih", "al-qafiya"), nt("أَيْ: لَأَمْهَلَنِي زَمَانًا (الزَّوْزَنِيُّ)", "that is, he would have given me respite for a while (al-Zawzanī)", "yani bana bir süre mühlet verirdi (Zevzenî)")),
])
V(77, "But my lord is a man who chokes me, whether I thank or ask of him, or seek to ransom myself.",
  "Fakat efendim, teşekkür etsem de, istesem de, ya da kendimi kurtarmaya çalışsam da beni boğan bir adamdır.", [
 PT("وَلٰكِنَّ", "lakinna", mk("حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ", "A verb-like particle of correction: it puts its noun in nasb and its predicate in raf'", "İstidrâk bildiren, fiile benzeyen harf; ismini nasb, haberini ref' eder", "inna-wa-akhawatuha"), JM("ist"), pre="wa-ist"),
 NO("مَوْلَايَ", "mawla", R("ism:لٰكِنَّ", "maq"), enc="يَ"),
 NO("امْرُؤٌ", "imru", R("kh:لٰكِنَّ")),
 PT("هُوَ", "huwa", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on fatha, in the seat of raf' as mubtada", "Fetha üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«امْرُؤٌ»", "the clause is an adjective of «امْرُؤٌ», in the seat of raf'", "cümle «امْرُؤٌ»un na'tı olarak mahallen merfû", "jumla-sifa"), pos="pron"),
 NO("خَانِقِي", "khaniq", R("kh", "yam"), nt("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ؛ خَنَقْتُ الرَّجُلَ: عَصَرْتُ حَلْقَهُ", "an active participle annexed to its object; خَنَقْتُ الرَّجُلَ: I squeezed his throat", "ism-i fâilin mef'ûlüne izâfeti; خَنَقْتُ الرَّجُلَ: boğazını sıktım", "ism-fail"),
    HD("اسْتِعَارَةٌ تَبَعِيَّةٌ فِي اسْمِ الْفَاعِلِ: شُبِّهَ تَضْيِيقُهُ عَلَيْهِ بِالْخَنْقِ، وَاشْتُقَّ مِنْهُ «خَانِقِي» (وَقَالَ الزَّوْزَنِيُّ: «يُضَيِّقُ الْأَمْرَ عَلَيَّ حَتَّى كَأَنَّهُ يَأْخُذُ عَلَيَّ مُتَنَفَّسِي»)؛ وَبَيْنَهُ وَبَيْنَ «لَفَرَّجَ كَرْبِي» فِي الْبَيْتِ قَبْلَهُ طِبَاقٌ: التَّفْرِيجُ وَالتَّضْيِيقُ", "a dependent istiara in the participle: his hemming the poet in is likened to choking, and «خَانِقِي» is derived from it (al-Zawzanī: «he straitens things for me as though he took my very breath»); and between it and «لَفَرَّجَ كَرْبِي» in the verse before there is a tibaq — easing against straitening", "ism-i fâilde istiâre-i tebeiyye: şaire darlık vermesi boğmaya benzetilmiş ve ondan «خَانِقِي» türetilmiştir (Zevzenî: «nefes alacak yerimi elimden alıyormuş gibi işi bana daraltır»); onunla önceki beyitteki «لَفَرَّجَ كَرْبِي» arasında tıbâk vardır: ferahlatmak ile daraltmak"), enc="ي", g=["istiara-tabaiyya", "istiara", "tibaq"], p=HEMI),
 HJ("عَلَى", "ala"),
 NO("الشُّكْرِ", "shukr", R("maj"), ON("خَانِقِي")),
 NO("وَالتَّسْآلِ", "tasal", AT("الشُّكْرِ", "jarr"), nt("التَّسْآلُ: السُّؤَالُ", "التَّسْآل: asking", "التَّسْآل: istemek"), pre="wa"),
 PT("أَوْ", "aw", AW_T),
 PT("أَنَا", "ana", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on sukun, in the seat of raf' as mubtada", "Sükûn üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «هُوَ خَانِقِي» فَهِيَ فِي مَحَلِّ رَفْعٍ مِثْلُهَا (الدُّرَّةُ)", "the clause is conjoined to «هُوَ خَانِقِي», so it too is in the seat of raf' (al-Durra)", "cümle «هُوَ خَانِقِي» cümlesine ma'tûftur, o da mahallen merfûdur (Dürre)"), pos="pron"),
 NO("مُفْتَدِ", "muftadin", R("kh", "manh"), nt("وَأَثْبَتَ الدُّرَّةُ الْيَاءَ «مُفْتَدِي» لِلضَّرُورَةِ؛ يَقُولُ: أَوْ كُنْتُ فِي حَالِ افْتِدَائِي نَفْسِي مِنْهُ (الزَّوْزَنِيُّ)", "al-Durra writes the ya, «مُفْتَدِي», for the verse's need; he says: or when I am ransoming myself from him (al-Zawzanī)", "Dürre zaruret için yâ'yı yazar: «مُفْتَدِي»; der ki: ya da kendimi ondan kurtarmaya çalıştığım hâlde (Zevzenî)", "ism-fail"), q=True),
])
V(78, "And the wrong done by kinsmen is sharper in its sting to a man than the stroke of the Indian sword.",
  "Yakınların zulmü insana, Hint kılıcının darbesinden daha acı gelir.", [
 NO("وَظُلْمُ", "zulm", R("mub") + MUD, JM("ist"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ، وَيُحْتَمَلُ إِلَى مَفْعُولِهِ (الدُّرَّةُ)", "the masdar annexed to its doer — or possibly to its object (al-Durra)", "masdarın fâiline — belki de mef'ûlüne — izâfeti (Dürre)", "masdar"), pre="wa-ist"),
 NO("ذَوِي", "dhu", R("mi", "mulhaq") + MUD, NUN_IDF),
 NO("الْقُرْبَى", "qurba", R("mi", "maq")),
 NO("أَشَدُّ", "ashadd", "kh", nt("اسْمُ تَفْضِيلٍ", "an elative", "ism-i tafdîl", "ism-tafdil")),
 NO("مَضَاضَةً", "madada", mk("تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ يُبَيِّنُ جِهَةَ التَّفْضِيلِ فِي «أَشَدُّ»", "A tamyiz in nasb by the fatha, showing in what respect «أَشَدُّ» is greater", "«أَشَدُّ»daki üstünlüğün yönünü açıklayan temyîz, fetha ile mansûb", "tamyiz"), nt("مَضَّنِي الْأَمْرُ وَأَمَضَّنِي: بَلَغَ مِنْ قَلْبِي وَأَثَّرَ فِي نَفْسِي تَهْيِيجَ الْحُزْنِ وَالْغَضَبِ", "مَضَّنِي الأَمْرُ / أَمَضَّنِي: the thing reached my heart and stirred grief and anger in me", "مَضَّنِي الأَمْرُ / أَمَضَّنِي: iş kalbime işledi, içimde hüzün ve öfke uyandırdı"), p=HEMI),
 HJ("عَلَى", "ala"),
 NO("الْمَرْءِ", "mar", R("maj"), ON("أَشَدُّ")),
 HJ("مِنْ", "min"),
 NO("وَقْعِ", "waq-ant", R("maj") + MUD, ON("أَشَدُّ"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "the masdar annexed to its doer", "masdarın fâiline izâfeti", "masdar")),
 NO("الْحُسَامِ", "husam", "mi", nt("الْحُسَامُ: فُعَالٌ مِنَ الْحَسْمِ وَهُوَ الْقَطْعُ", "الحُسَام: a فُعَال from الحَسْم, cutting", "الحُسَام: kesmek demek olan الحَسْم'den فُعَال vezninde")),
 NO("الْمُهَنَّدِ", "muhannad-ant", NA("الْحُسَامِ", "jarr"), nt("أَيِ: الْمَطْبُوعِ بِالْهِنْدِ، أَوِ الْمُحَدَّدِ (الزَّوْزَنِيُّ)", "that is, forged in India, or sharpened (al-Zawzanī)", "yani Hint'te dövülmüş ya da bilenmiş (Zevzenî)", "ism-maful")),
])
V(79, "So leave me to my nature: I am thankful to you, even were my house to stand far off, at Ḍarghad.",
  "Öyleyse beni huyumla baş başa bırak; evim uzaklarda, Darğad'da konsa bile ben sana şükran duyarım.", [
 VB("فَذَرْنِي", "wadhara", "amr", JM("ist"), nt("أَيْ: خَلِّ بَيْنِي وَبَيْنَ خُلُقِي وَكِلْنِي إِلَى سَجِيَّتِي (الزَّوْزَنِيُّ)", "that is, leave me alone with my nature, trust me to my own temper (al-Zawzanī)", "yani beni huyumla baş başa bırak, mizacıma havale et (Zevzenî)"), who="أَنْتَ", enc="نِي", pre="fa-ist"),
 NO("وَخُلْقِي", "khuluq", mk("مَعْطُوفٌ عَلَى يَاءِ الْمُتَكَلِّمِ فِي «ذَرْنِي» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ, "Conjoined to the speaker's ya in «ذَرْنِي», in nasb by a fatha estimated before the speaker's ya", "«ذَرْنِي»deki mütekellim yâsına ma'tûf; mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb", "atf-nasaq", "ya-al-mutakallim"), enc="ي", pre="wa"),
 PT("إِنَّنِي", "inna", INNA_T + mk("، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا", "; the nun guards its ending, and the ya is its noun, in the seat of nasb", "; nûn vikâye içindir; yâ ismi, mahallen mansûb"), nt("وَالْجُمْلَةُ تَعْلِيلِيَّةٌ لَا مَحَلَّ لَهَا (الدُّرَّةُ)", "the clause gives the reason and has no seat (al-Durra)", "cümle ta'liliyyedir, mahalli yoktur (Dürre)"), stem="إِنَّنِي"),
 PJ("لَكَ", "لَ", "li", "كَ", ON("شَاكِرٌ")),
 NO("شَاكِرٌ", "shakir", R("kh:إِنَّ"), p=HEMI),
 PT("وَلَوْ", "law", LAW_T, nt("وَجَوَابُ «لَوْ» مَحْذُوفٌ لِدَلَالَةِ مَا قَبْلَهُ عَلَيْهِ، أَيْ: وَلَوْ حَلَّ بَيْتِي نَائِيًا لَكُنْتُ لَكَ شَاكِرًا (الدُّرَّةُ)", "the answer of لَوْ is left out, what precedes pointing to it — «even were my house far, I should be thankful to you» (al-Durra)", "«لَوْ»nun cevabı, öncesi delâlet ettiği için mahzûftur: «evim uzakta konsa da sana şükran duyardım» (Dürre)", "hadhf-wa-taqdir"), pre="wa"),
 VB("حَلَّ", "halla-settle", "madi", g=["doubled-verbs"]),
 NO("بَيْتِي", "bayt", R("fail", "yam"), enc="ي"),
 NO("نَائِيًا", "nai", mk("حَالٌ مِنْ «بَيْتِي» مَنْصُوبٌ بِالْفَتْحَةِ", "A hal of «بَيْتِي», in nasb by the fatha", "«بَيْتِي»den hâl, fetha ile mansûb", "hal"), g=["ism-fail"]),
 NO("عِنْدَ", "inda", R("zm") + MUD, ZON("حَلَّ")),
 NO("ضَرْغَدِ", "darghad", SRF("مُضَافٌ إِلَيْهِ", "The second term of the idafa", "Muzâfun ileyh", "لِلْعَلَمِيَّةِ وَالْعُجْمَةِ (الدُّرَّةُ)", "(a foreign proper name — al-Durra)", "alemiyet ve ucmet sebebiyle (Dürre)", "idafa-definiteness"), nt("ضَرْغَدُ: جَبَلٌ (الزَّوْزَنِيُّ)، وَقِيلَ: حَرَّةٌ بِأَرْضِ غَطَفَانَ (الدُّرَّةُ)", "Ḍarghad: a mountain (al-Zawzanī); also said: a lava-field in the land of Ghaṭafān (al-Durra)", "Darğad: bir dağ (Zevzenî); Gatafân yurdunda bir lav arazisi olduğu da söylenir (Dürre)"), pos="propn"),
])
# ---- «Had my Lord willed»; the sword: verses 80–85 -------------------------------------------------------------------------
KUNTU = mk("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْمُتَكَلِّمِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهُ", "A defective past verb built on sukun because the speaker's ta is attached; the ta is its noun, in the seat of raf'", "Mütekellim tâsına bitiştiği için sükûn üzere mebnî nâkıs mâzî; tâ ismi, mahallen merfû", "kana-wa-akhawatuha")
SAYF = ("السَّيْفِ الْمَوْصُوفِ", "the sword described", "vasfedilen kılıca")
V(80, "Had my Lord willed, I should have been Qays son of Khālid; had my Lord willed, I should have been ʿAmr son of Marthad.",
  "Rabbim dileseydi Kays b. Hâlid olurdum; Rabbim dileseydi Amr b. Mersed olurdum.", [
 PT("فَلَوْ", "law", LAW_T, JM("ist"), pre="fa-ist"),
 VB("شَاءَ", "shaa", "madi", nt("فِعْلُ شَرْطِ «لَوْ»", "the verb of the condition of لَوْ", "«لَوْ»nun şart fiili"),
    S_(mk("وَحُذِفَ مَفْعُولُهُ فِي الشَّطْرَيْنِ لِأَنَّ الْجَوَابَ يَدُلُّ عَلَيْهِ، أَيْ: لَوْ شَاءَ رَبِّي أَنْ يَجْعَلَنِي مِثْلَ قَيْسِ بْنِ خَالِدٍ لَكُنْتُهُ؛ وَهٰذَا الْحَذْفُ يَكْثُرُ فِي «شَاءَ» وَ«أَرَادَ» بَعْدَ «لَوْ»، وَلَا يُبْرِزُونَ الْمَفْعُولَ إِلَّا فِي الشَّيْءِ الْمُسْتَغْرَبِ كَقَوْلِهِ: «فَلَوْ شِئْتُ أَنْ أَبْكِيَ دَمًا لَبَكَيْتُهُ» (الدُّرَّةُ) — وَهُوَ حَذْفُ مَفْعُولِ الْمَشِيئَةِ لِلْبَيَانِ بَعْدَ الْإِبْهَامِ", "Its object is left out in both halves because the answer points to it — «had my Lord willed to make me like Qays son of Khālid, I should have been he»; this dropping is frequent with شَاءَ and أَرَادَ after لَوْ, and the object is spelt out only for something strange, as in «had I willed to weep blood, I would have wept it» (al-Durra) — the dropping of the object of willing, to explain after leaving it vague", "Mef'ûlü iki mısrada da hazfedilmiştir, çünkü cevap ona delâlet eder: «Rabbim beni Kays b. Hâlid gibi kılmayı dileseydi, o olurdum»; bu hazif «لَوْ»dan sonra «شَاءَ» ve «أَرَادَ»da çoktur; mef'ûl ancak garip bir şeyde açıkça söylenir: «kan ağlamayı dileseydim onu ağlardım» (Dürre) — ibhamdan sonra beyan için meşîet fiilinin mef'ûlünü hazfetmek", "hadhf-al-maful")), g=["hollow-verbs"]),
 NO("رَبِّي", "rabb", R("fail", "yam"), enc="ي"),
 PT("كُنْتُ", "kana", KUNTU, JM("jawab", "لَوْ"), pos="verb"),
 NO("قَيْسَ", "qays-name", R("kh:كَانَ"), nt("هٰذَانِ سَيِّدَانِ مِنْ سَادَاتِ الْعَرَبِ مَذْكُورَانِ بِوُفُورِ الْمَالِ وَنَجَابَةِ الْأَوْلَادِ وَشَرَفِ النَّسَبِ (الزَّوْزَنِيُّ)", "these two were lords among the Arabs, famed for wealth, fine sons and noble lineage (al-Zawzanī)", "bu ikisi Arapların efendilerindendir; mal bolluğu, evlatlarının necabeti ve soy şerefiyle anılırlar (Zevzenî)"), pos="propn"),
 IBN("nasb"),
 NO("خَالِدٍ", "khalid", "mi", pos="propn", p=HEMI),
 PT("وَلَوْ", "law", LAW_T, pre="wa"),
 VB("شَاءَ", "shaa", "madi", nt("فِعْلُ شَرْطِ «لَوْ»، وَمَفْعُولُهُ مَحْذُوفٌ كَالْأَوَّلِ", "the verb of the condition of لَوْ, its object left out as in the first half", "«لَوْ»nun şart fiili; mef'ûlü birincisindeki gibi mahzûftur", "hadhf-al-maful"), g=["hollow-verbs"]),
 NO("رَبِّي", "rabb", R("fail", "yam"), enc="ي"),
 PT("كُنْتُ", "kana", KUNTU, JM("jawab", "لَوْ"), pos="verb"),
 NO("عَمْرَو", "amr-name", R("kh:كَانَ"), nt("وَالْوَاوُ فَارِقَةٌ تُكْتَبُ وَلَا تُلْفَظُ", "the waw only distinguishes the name in writing and is not pronounced", "vâv yalnız yazıda ayırt etmek içindir, okunmaz"), pos="propn"),
 IBN("nasb"),
 NO("مَرْثَدِ", "marthad", "mi", pos="propn", q=True),
])
V(81, "and I should have become a man of great wealth, and noble sons, lords, sons of a lord, would have come to visit me.",
  "ve çok mal sahibi olurdum; efendi bir adamın soylu, efendi oğulları beni ziyarete gelirdi.", [
 PT("فَأَصْبَحْتُ", "asbaha", KUNTU, nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جَوَابِ «لَوْ»؛ وَعِنْدَ التِّبْرِيزِيِّ «فَأُلْفِيتُ»", "the clause is conjoined to the answer of لَوْ; al-Tibrīzī has «فَأُلْفِيتُ»", "cümle «لَوْ»nun cevabına ma'tûftur; Tebrîzî'de «فَأُلْفِيتُ»"), pre="fa-sabab", pos="verb"),
 NO("ذَا", "dhu", R("kh:أَصْبَحَ", "five") + MUD),
 NO("مَالٍ", "mal", "mi"),
 NO("كَثِيرٍ", "kathir", NA("مَالٍ", "jarr")),
 VB("وَزَارَنِي", "zara", "madi", JM("atf", "أَصْبَحْتُ"), nt("وَعِنْدَ التِّبْرِيزِيِّ «وَعَادَنِي»", "al-Tibrīzī has «وَعَادَنِي»", "Tebrîzî'de «وَعَادَنِي»"), enc="نِي", pre="wa", g=["hollow-verbs"], p=HEMI),
 NO("بَنُونَ", "banu", R("fail", "mulhaq"), NUN_IWAD),
 NO("كِرَامٌ", "karim", NA("بَنُونَ", "raf"), g=["jam-taksir"]),
 NO("سَادَةٌ", "sayyid", NA("بَنُونَ", "raf", "", "2"), nt("جَمْعُ سَيِّدٍ", "the plural of سَيِّد", "«سَيِّد»in cem'i", "jam-taksir")),
 NO("لِمُسَوَّدِ", "musawwad", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَالِثٍ لِـ«بَنُونَ»، أَوْ بِـ«سَادَةٌ» لِأَنَّهُ جَمْعُ سَيِّدٍ وَهُوَ صِفَةٌ مُشَبَّهَةٌ (الدُّرَّةُ)؛ لِرَجُلٍ مُسَوَّدٍ يَعْنِي بِهِ نَفْسَهُ، وَالتَّسْوِيدُ مَصْدَرُ سَوَّدْتُهُ فَسَادَ (الزَّوْزَنِيُّ)", "the phrase hangs on an omitted third adjective of «بَنُونَ», or on «سَادَةٌ», the plural of سَيِّد, a ṣifa mushabbaha (al-Durra); «of a man made lord» — he means himself (al-Zawzanī)", "câr-mecrûr «بَنُونَ»un mahzûf üçüncü na'tına ya da sıfat-ı müşebbehe olan «سَيِّد»in cem'i «سَادَةٌ»ya müteallik (Dürre); «efendi kılınmış bir adamın» — kendini kasteder (Zevzenî)", "ism-maful"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «سَادَةٌ» وَ«مُسَوَّدِ» الِاشْتِقَاقُ", "a figure joined to jinas: «سَادَةٌ» and «مُسَوَّدِ» are brought together by derivation", "cinâsa mülhak: «سَادَةٌ» ile «مُسَوَّدِ»i iştikak bir araya getirmiştir"), pre="li", q=True, g=["mulhaq-bil-jinas"]),
])
V(82, "I am the lean, light man whom you know — one who slips into things, keen as the head of a snake.",
  "Ben, tanıdığınız o eti az, çevik adamım; yılanın başı gibi uyanık, işlerin içine süzülen biriyim.", [
 PT("أَنَا", "ana", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on sukun, in the seat of raf' as mubtada", "Sükûn üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), JM("ist"), pos="pron"),
 NO("الرَّجُلُ", "rajul", "kh"),
 NO("الضَّرْبُ", "darb", NA("الرَّجُلُ", "raf"), nt("الضَّرْبُ: الرَّجُلُ الْخَفِيفُ اللَّحْمِ، وَالْعَرَبُ تَتَمَدَّحُ بِخِفَّةِ اللَّحْمِ (الزَّوْزَنِيُّ)", "الضَّرْب: a man light of flesh — the Arabs praise themselves for leanness (al-Zawzanī)", "الضَّرْب: eti az, hafif adam — Araplar etin azlığıyla övünür (Zevzenî)")),
 PT("الَّذِي", "alladhi", mk("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«الرَّجُلُ»", "A relative noun built on sukun, in the seat of raf' as a second adjective of «الرَّجُلُ»", "Sükûn üzere mebnî ism-i mevsûl; «الرَّجُلُ»ün ikinci na'tı olarak mahallen merfû", "ism-mawsul", "naat-sifa"), pos="pron"),
 VB("تَعْرِفُونَهُ", "arafa", "mud5", JM("sila"), enc="هُ", p=HEMI),
 NO("خَشَاشٌ", "khashash", "kh2", nt("يَقُولُ: أَنَا دَخَّالٌ فِي الْأُمُورِ بِخِفَّةٍ وَسُرْعَةٍ (الزَّوْزَنِيُّ)", "he says: I slip into affairs lightly and quickly (al-Zawzanī)", "der ki: ben işlerin içine hafiflik ve çabuklukla giren biriyim (Zevzenî)")),
 NO("كَرَأْسِ", "ras", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«خَشَاشٌ» لِأَنَّهُ بِمَعْنَى سَرِيعِ التَّدَخُّلِ، أَوْ بِمَحْذُوفٍ نَعْتٍ لَهُ (الدُّرَّةُ)", "the phrase hangs on «خَشَاشٌ», meaning «quick to slip in», or on an omitted adjective of it (al-Durra)", "câr-mecrûr «çabuk sokulan» anlamındaki «خَشَاشٌ»a ya da onun mahzûf na'tına müteallik (Dürre)"),
    TSB("mf", ("تَيَقُّظُهُ وَذَكَاءُ ذِهْنِهِ", "his wakefulness and keenness of mind", "uyanıklığı ve zihninin keskinliği"), ("رَأْسُ الْحَيَّةِ", "a snake's head", "yılanın başı"), "ka", ("سُرْعَةُ الْحَرَكَةِ وَشِدَّةُ التَّوَقُّدِ، وَهُوَ مَذْكُورٌ فِي «الْمُتَوَقِّدِ»", "quickness of movement and fierce keenness, named in «الْمُتَوَقِّدِ»", "hareketin çabukluğu ve keskin uyanıklık — «الْمُتَوَقِّدِ»de zikredilmiştir")), pre="ka", g=TSB_TAGS),
 NO("الْحَيَّةِ", "hayya-snake", "mi"),
 NO("الْمُتَوَقِّدِ", "mutawaqqid", NA("رَأْسِ", "jarr"), nt("أَيِ: الشَّدِيدِ التَّوَقُّدِ وَالْيَقَظَةِ", "that is, fiercely keen and wakeful", "yani son derece keskin ve uyanık", "ism-fail")),
])
V(83, "And I have sworn that my flank shall never cease to be a lining for a keen blade, thin of edges, of Indian steel —",
  "Ve yemin ettim ki böğrüm, iki ağzı ince, Hint işi keskin bir kılıca hep astar olacaktır —", [
 VB("فَآلَيْتُ", "ala-swear", "madi-tu", JM("ist"), nt("آلَيْتُ: حَلَفْتُ", "آلَيْتُ: I swore", "آلَيْتُ: yemin ettim"), pre="fa-ist", g=["form-iv-verbs", "naqis-verbs"]),
 PT("لَا", "la-nafiya", LA_NAFY),
 VB("يَنْفَكُّ", "infakka", "mud", nt("نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ»: لَا يَنْفَكُّ لَا يَزَالُ (الزَّوْزَنِيُّ)؛ وَجُمْلَةُ «لَا يَنْفَكُّ…» جَوَابُ «آلَيْتُ» لَا مَحَلَّ لَهَا لِتَضَمُّنِهِ مَعْنَى الْقَسَمِ (الدُّرَّةُ)", "defective, a sister of كَانَ — لَا يَنْفَكُّ is لَا يَزَالُ, «never ceases» (al-Zawzanī); the clause «لَا يَنْفَكُّ…» answers «آلَيْتُ», which carries the sense of an oath, and has no seat (al-Durra)", "nâkıstır, «كَانَ»nin kardeşi: لَا يَنْفَكُّ = لَا يَزَالُ (Zevzenî); «لَا يَنْفَكُّ…» cümlesi yemin anlamı taşıyan «آلَيْتُ»in cevabıdır, mahalli yoktur (Dürre)", "kana-wa-akhawatuha"), g=["form-vii-verbs", "doubled-verbs"]),
 NO("كَشْحِي", "kashh", R("ism:يَنْفَكُّ", "yam"), enc="ي"),
 NO("بِطَانَةً", "bitana", R("kh:يَنْفَكُّ"), nt("الْبِطَانَةُ: نَقِيضُ الظِّهَارَةِ", "البِطَانَة: the lining, the opposite of the outer face", "البِطَانَة: astar, yüzün zıddı"),
    TSB("bl", ("كَشْحُهُ", "his flank", "böğrü"), ("الْبِطَانَةُ لِلظِّهَارَةِ", "a lining to an outer garment", "yüze göre astar"), src="z"), g=TSB_TAGS, p=HEMI),
 NO("لِعَضْبٍ", "adb", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«بِطَانَةً»، وَ«عَضْبٍ» نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: لِسَيْفٍ عَضْبٍ (الدُّرَّةُ)؛ الْعَضْبُ: السَّيْفُ الْقَاطِعُ", "the phrase hangs on an omitted adjective of «بِطَانَةً», and «عَضْبٍ» describes a noun left out — «a keen sword» (al-Durra); العَضْب: the cutting sword", "câr-mecrûr «بِطَانَةً»nin mahzûf na'tına müteallik; «عَضْبٍ» mahzûf bir mevsûfun sıfatıdır: «keskin bir kılıç» (Dürre); العَضْب: keskin kılıç", "hadhf-wa-taqdir"), pre="li"),
 NO("رَقِيقِ", "raqiq", NMH("jarr", nth="2") + MUD),
 NO("الشَّفْرَتَيْنِ", "shafra", R("mi", "ya2"), NUN_IWAD, nt("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا؛ شَفْرَتَا السَّيْفِ: حَدَّاهُ", "the ṣifa mushabbaha annexed to its doer; the two شَفْرَة of a sword are its two edges", "sıfat-ı müşebbehenin fâiline izâfeti; kılıcın iki شَفْرَة'sı iki ağzıdır", "idafa-lafziyya")),
 NO("مُهَنَّدِ", "muhannad-ant", NMH("jarr", nth="3"), q=True),
])
V(84, "— a cutting sword: when I rise to take vengeance with it, its first stroke spares it a second; it is no chopper of trees.",
  "— keskin bir kılıç: onunla öç almaya kalktığımda ilk darbesi ikinciye gerek bırakmaz; ağaç kesilen bir bıçak değildir o.", [
 NO("حُسَامٍ", "husam", NMH("jarr", nth="4"), nt("وَالْمَوْصُوفُ الْمَحْذُوفُ هُوَ السَّيْفُ فِي الْبَيْتِ ٨٣؛ وَيَجُوزُ فِيهِ الرَّفْعُ لُغَةً وَلَمْ يُرْوَ بِهِ (الدُّرَّةُ)", "the noun left out is the sword of v. 83; raf' would be sound Arabic but is not transmitted (al-Durra)", "mahzûf mevsûf 83. beyitteki kılıçtır; ref' dil bakımından câizdir ama rivayet edilmemiştir (Dürre)")),
 PT("إِذَا", "idha", IDHA_SH, nt("وَ«إِذَا» وَمَدْخُولُهَا فِي مَحَلِّ جَرٍّ نَعْتٌ خَامِسٌ لِلْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)", "إِذَا with what follows is a fifth adjective of the noun left out, in the seat of jarr (al-Durra)", "«إِذَا» ve sonrası, mahzûf mevsûfun beşinci na'tı olarak mahallen mecrûr (Dürre)")),
 PT("مَا", "ma-zaida", MA_ZAID),
 VB("قُمْتُ", "qama", "madi-tu", JM("mudaf", "إِذَا"), g=["hollow-verbs"]),
 NO("مُنْتَصِرًا", "muntasir", mk("حَالٌ مِنْ فَاعِلِ «قُمْتُ» مَنْصُوبٌ بِالْفَتْحَةِ", "A hal of the doer of «قُمْتُ», in nasb by the fatha", "«قُمْتُ»un fâilinden hâl, fetha ile mansûb", "hal"), nt("الِانْتِصَارُ: الِانْتِقَامُ", "الاِنْتِصَار: taking vengeance", "الاِنْتِصَار: öç almak", "ism-fail")),
 PJ("بِهِ", "بِ", "bi", "هِ", ON("مُنْتَصِرًا"), ref=SAYF, p=HEMI),
 VB("كَفَى", "kafa", "madi-muq", JM("jawab", "إِذَا"), g=["naqis-verbs"]),
 NO("الْعَوْدَ", "awd", "maf", nt("وَقَالَ التِّبْرِيزِيُّ: مَنْصُوبٌ لِأَنَّهُ فِي مَوْضِعِ الْحَالِ عِنْدَ سِيبَوَيْهِ (الدُّرَّةُ)؛ أَيِ: الضَّرْبَةَ الثَّانِيَةَ", "al-Tibrīzī says it is in nasb because it stands in place of a hal, after Sībawayh (al-Durra); that is, the second stroke", "Tebrîzî, Sîbeveyh'e göre hâl yerinde olduğu için mansûb olduğunu söyler (Dürre); yani ikinci darbe")),
 PJ("مِنْهُ", "مِنْ", "min", "هُ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْعَوْدَ» لِأَنَّهُ مَصْدَرٌ", "the phrase hangs on «الْعَوْدَ», a masdar", "câr-mecrûr masdar olan «الْعَوْدَ»e müteallik"), ref=SAYF),
 NO("الْبَدْءُ", "bad-beginning", "fail", nt("أَيِ: الضَّرْبَةُ الْأُولَى تُغْنِي عَنِ الثَّانِيَةِ (الزَّوْزَنِيُّ)", "that is, the first stroke spares the need of a second (al-Zawzanī)", "yani ilk darbe ikinciye ihtiyaç bırakmaz (Zevzenî)"),
    HD("طِبَاقٌ بَيْنَ «الْعَوْدَ» وَ«الْبَدْءُ»: الْإِعَادَةُ وَالِابْتِدَاءُ", "«الْعَوْدَ» and «الْبَدْءُ» make a tibaq — doing again against doing first", "«الْعَوْدَ» ile «الْبَدْءُ» arasında tıbâk vardır: tekrar etmek ile ilk yapmak"), g=["tibaq"]),
 PT("لَيْسَ", "laysa", mk("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى السَّيْفِ الْمَوْصُوفِ", "A defective, frozen past verb; its noun is a hidden pronoun returning to the sword described", "Câmid, nâkıs mâzî fiil; ismi vasfedilen kılıca dönen gizli zamirdir", "kana-wa-akhawatuha"), nt("وَجُمْلَةُ «لَيْسَ بِمِعْضَدِ» فِي مَحَلِّ جَرٍّ نَعْتٌ سَادِسٌ لِلْمَوْصُوفِ الْمَحْذُوفِ، أَوْ حَالٌ مِنْهُ (الدُّرَّةُ)", "the clause «لَيْسَ بِمِعْضَدِ» is a sixth adjective of the noun left out, in the seat of jarr, or a hal of it (al-Durra)", "«لَيْسَ بِمِعْضَدِ» cümlesi mahzûf mevsûfun altıncı na'tı olarak mahallen mecrûr ya da ondan hâldir (Dürre)")),
 NO("بِمِعْضَدِ", "midad", mk("خَبَرُ «لَيْسَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "The predicate of لَيْسَ, in nasb by an estimated fatha, its place taken by the kasra of the added jarr letter", "«لَيْسَ»in haberi; mahalli zâid cer harfinin harekesi işgal ettiğinden takdîrî fetha ile mansûb", "kana-wa-akhawatuha"),
    nt("الْمِعْضَدُ: سَيْفٌ يُقْطَعُ بِهِ الشَّجَرُ، نَفَاهُ لِأَنَّهُ مِنْ أَرْدَإِ السُّيُوفِ (الزَّوْزَنِيُّ)", "المِعْضَد: a blade for cutting down trees — he denies it, as the meanest of swords (al-Zawzanī)", "المِعْضَد: ağaç kesilen kılıç — kılıçların en kötüsü olduğu için onu nefyetmiştir (Zevzenî)", "ism-al-ala"), pre="bi-z", q=True),
])
V(85, "— a brother to be trusted, that turns not back from what it strikes; when men say «Enough!», the one who holds it back says «Enough for me!»",
  "— güvenilir bir kardeş gibidir; vurduğu yerden geri dönmez; «Yavaş!» dendiğinde onu tutan sahibi «Bana yeter!» der.", [
 NO("أَخِي", "akh", mk("نَعْتٌ آخَرُ لِلْمَوْصُوفِ الْمَحْذُوفِ فِي الْبَيْتِ ٨٣ " + SIGN("jarr", "five")[0], "A further adjective of the noun left out in v. 83, " + SIGN("jarr", "five")[1], "83. beyitteki mahzûf mevsûfun bir başka na'tı, " + SIGN("jarr", "five")[2], "naat-sifa", "five-nouns") + MUD,
    TSB("bl", ("السَّيْفُ", "the sword", "kılıç"), ("الْأَخُ الَّذِي يُوثَقُ بِإِخَائِهِ", "a brother whose brotherhood can be trusted", "kardeşliğine güvenilen kardeş"), src="z"),
    ZW("يَقُولُ: هٰذَا السَّيْفُ سَيْفٌ يُوثَقُ بِمَضَائِهِ كَالْأَخِ الَّذِي يُوثَقُ بِإِخَائِهِ", "he says: this is a sword whose cutting can be trusted, like a brother whose brotherhood can be trusted", "der ki: bu kılıç, kardeşliğine güvenilen kardeş gibi, keskinliğine güvenilen bir kılıçtır"), g=TSB_TAGS),
 NO("ثِقَةٍ", "thiqa", "mi"),
 PT("لَا", "la-nafiya", LA_NAFY),
 VB("يَنْثَنِي", "inthana", "mud-y", nt("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنَ الْمَوْصُوفِ الْمَحْذُوفِ (الدُّرَّةُ)؛ الِانْثِنَاءُ: الِانْصِرَافُ", "the clause may be an adjective or a hal of the noun left out (al-Durra); الاِنْثِنَاء: turning away", "cümle mahzûf mevsûfun sıfatı da hâli de olabilir (Dürre); الاِنْثِنَاء: dönüp gitmek"), who=("هُوَ", SAYF), g=["form-vii-verbs", "naqis-verbs"]),
 HJ("عَنْ", "an"),
 NO("ضَرِيبَةٍ", "dariba", R("maj"), ON("يَنْثَنِي"), nt("الضَّرِيبَةُ: مَا يُضْرَبُ بِالسَّيْفِ", "الضَّرِيبَة: what is struck with the sword", "الضَّرِيبَة: kılıçla vurulan şey"), p=HEMI),
 PT("إِذَا", "idha", IDHA_SH, JM("ist")),
 VB("قِيلَ", "qala", "madi", nt("وَنَائِبُ الْفَاعِلِ يَعُودُ عَلَى الْقَوْلِ الْمَفْهُومِ مِنَ الْمَقَامِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "its deputy doer returns to the saying the setting implies; the clause is in the seat of jarr, إِذَا being annexed to it", "nâib-i fâili makamdan anlaşılan söze döner; cümle «إِذَا»nın ona izâfetiyle mahallen mecrûr"), maj=True, g=["hollow-verbs"]),
 NO("مَهْلًا", "mahl", R("mm"), nt("لِفِعْلٍ مَحْذُوفٍ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ (الدُّرَّةُ)؛ مَهْلًا: أَيْ كُفَّ", "of a verb left out, and the clause is what is said, in the seat of nasb (al-Durra); مَهْلًا: hold back!", "mahzûf bir fiilin mef'ûlün mutlakı; cümle mekūlü'l-kavl olarak mahallen mansûb (Dürre); مَهْلًا: dur, vazgeç!", "hadhf-wa-taqdir")),
 VB("قَالَ", "qala", "madi", JM("jawab", "إِذَا"), g=["hollow-verbs"]),
 NO("حَاجِزُهُ", "hajiz", "fail", nt("أَيْ: مَانِعُ السَّيْفِ وَهُوَ صَاحِبُهُ (الزَّوْزَنِيُّ)", "that is, the one who holds the sword back — its owner (al-Zawzanī)", "yani kılıcı tutan, sahibi (Zevzenî)", "ism-fail"), enc="هُ"),
 NO("قَدِي", "qad-hasb", mk("اسْمٌ بِمَعْنَى «حَسْبُ» مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَخَبَرُهُ مَحْذُوفٌ: حَسْبِي ذٰلِكَ", "A noun meaning حَسْبُ, «enough», the mubtada, in raf' by a damma estimated before the speaker's ya; its predicate is left out — «that is enough for me»", "«حَسْبُ» anlamında isim, mübteda; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû; haberi mahzûftur: «bu bana yeter»", "mubtada-khabar", "hadhf-wa-taqdir"),
    nt("وَقِيلَ: مَبْنِيٌّ عَلَى السُّكُونِ حُرِّكَ بِالْكَسْرِ لِلضَّرُورَةِ وَالْيَاءُ لِلْإِشْبَاعِ، وَقِيلَ: اسْمُ فِعْلٍ بِمَعْنَى «يَكْفِي» حُذِفَتْ نُونُ وِقَايَتِهِ ضَرُورَةً (الدُّرَّةُ)؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ؛ قَدِي وَقَدْنِي: حَسْبِي (الزَّوْزَنِيُّ)", "also said: built on sukun with a kasra for the verse's need and the ya drawn out; or a verb-noun meaning «suffices», its guarding nun dropped by licence (al-Durra); the clause is what is said, in the seat of nasb; قَدِي or قَدْنِي: enough for me (al-Zawzanī)", "sükûn üzere mebnî olup zaruretten kesrelendiği, yâ'nın işbâ' yâsı olduğu da; «يَكْفِي» anlamında isim-fiil olup vikâye nûnunun zaruretten düştüğü de söylenmiştir (Dürre); cümle mekūlü'l-kavl olarak mahallen mansûb; قَدِي ya da قَدْنِي: bana yeter (Zevzenî)"), enc="ي", pos="noun"),
])
# ---- The camel slaughtered for the guests: verses 86–91 --------------------------------------------------------------------
SHAYKH = ("الشَّيْخِ", "the old man", "ihtiyara")
V(86, "When the men race for their weapons, you will find me not to be overcome, once my hand has got hold of its hilt.",
  "Kavim silahlarına koştuğunda, elim onun kabzasını kavradığında beni yenilmez bulursun.", [
 PT("إِذَا", "idha", IDHA_SH, JM("ist")),
 VB("ابْتَدَرَ", "ibtadara", "madi", JM("mudaf", "إِذَا"), nt("ابْتَدَرَ الْقَوْمُ السِّلَاحَ: اسْتَبَقُوهُ", "ابْتَدَرَ القَوْمُ السِّلَاحَ: they raced one another to their arms", "ابْتَدَرَ القَوْمُ السِّلَاحَ: silahlara koşuştular"), g=["form-viii-verbs"]),
 NO("الْقَوْمُ", "qawm", "fail"),
 NO("السِّلَاحَ", "silah", "maf"),
 VB("وَجَدْتَنِي", "wajada", "madi-ta", JM("jawab", "إِذَا"), nt("وَالْيَاءُ أَوَّلُ مَفْعُولَيْهِ", "the ya is the first of its two objects", "yâ iki mef'ûlünün birincisidir", "mafulayn"), enc="نِي", p=HEMI),
 NO("مَنِيعًا", "mani", "maf2", nt("الْمَنِيعُ: الَّذِي لَا يُقْهَرُ وَلَا يُغْلَبُ", "المَنِيع: one who is not overpowered or overcome", "المَنِيع: kahrolunmayan, yenilmeyen", "sifa-mushabbaha")),
 PT("إِذَا", "idha", IDHA_Z("وَجَدَ"), nt("وَيَجُوزُ تَعْلِيقُهُ بِـ«مَنِيعًا» لِأَنَّهُ صِفَةٌ مُشَبَّهَةٌ (الدُّرَّةُ)", "it may also hang on «مَنِيعًا», a ṣifa mushabbaha (al-Durra)", "sıfat-ı müşebbehe olan «مَنِيعًا»ya bağlanması da câizdir (Dürre)")),
 VB("بَلَّتْ", "balla-seize", "madi-f", nt("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا؛ بَلَّ بِالشَّيْءِ: ظَفِرَ بِهِ (الزَّوْزَنِيُّ)", "the clause is in the seat of jarr, إِذَا being annexed to it; بَلَّ بِالشَّيْءِ: he got hold of the thing (al-Zawzanī)", "cümle «إِذَا»nın ona izâfetiyle mahallen mecrûr; بَلَّ بِالشَّيْءِ: onu ele geçirdi (Zevzenî)"), g=["doubled-verbs"]),
 NO("بِقَائِمِهِ", "qaim", R("maj"), ON("بَلَّتْ"), nt("قَائِمُ السَّيْفِ: مَقْبِضُهُ", "the قَائِم of a sword is its hilt", "kılıcın قَائِم'ı kabzasıdır"), enc="هِ", pre="bi"),
 NO("يَدِي", "yad", R("fail", "yam"), enc="ي"),
])
V(87, "And many a herd of kneeling, sleeping camels — the fear of me has roused the first of them, as I walk with a keen blade drawn.",
  "Nice çökmüş, uyuyan deve sürüsü vardır ki benden korkuları öndekilerini ayağa kaldırmıştır; ben ise kınından çekilmiş keskin bir kılıçla yürürüm.", [
 NO("وَبَرْكٍ", "bark", mk("مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ «رُبَّ» الْمُقَدَّرَةِ", "The mubtada, in raf' by an estimated damma, its place taken by the kasra of the near-redundant jarr letter رُبَّ, understood", "Mübteda; mahalli, takdir edilen ve zâide benzeyen «رُبَّ» cer harfinin harekesince işgal edildiğinden takdîrî damme ile merfû", "mubtada-khabar"), nt("الْبَرْكُ: الْإِبِلُ الْكَثِيرَةُ الْبَارِكَةُ؛ وَجَعَلَهُ الدُّرَّةُ نَعْتًا لِمَوْصُوفٍ مَحْذُوفٍ", "البَرْك: a great herd of camels kneeling; al-Durra makes it describe a noun left out", "البَرْك: çökmüş çok sayıda deve; Dürre onu mahzûf bir mevsûfun sıfatı sayar"), pre="wa-rubba"),
 NO("هُجُودٍ", "hujud", NA("بَرْكٍ", "jarr"), nt("جَمْعُ هَاجِدٍ، وَهُوَ النَّائِمُ", "the plural of هَاجِد, sleeping", "«هَاجِد»in cem'i: uyuyan", "jam-taksir")),
 PT("قَدْ", "qad", QAD_T, nt("وَجُمْلَةُ «قَدْ أَثَارَتْ…» فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ «بَرْكٍ»، وَإِنْ جُعِلَتْ نَعْتًا لَهُ فَالْخَبَرُ مَحْذُوفٌ (الدُّرَّةُ)", "the clause «قَدْ أَثَارَتْ…» is the predicate of the mubtada «بَرْكٍ», in the seat of raf'; if it is taken as its adjective, the predicate is left out (al-Durra)", "«قَدْ أَثَارَتْ…» cümlesi «بَرْكٍ» mübtedasının haberi olarak mahallen merfû; onun sıfatı sayılırsa haber mahzûftur (Dürre)")),
 VB("أَثَارَتْ", "athara", "madi-f", ZW("يُرِيدُ أَنَّهُ أَرَادَ أَنْ يَنْحَرَ بَعِيرًا مِنْهَا فَنَفَرَتْ مِنْهُ لِتَعَوُّدِهَا ذٰلِكَ مِنْهُ", "he means that he set out to slaughter one of them, and they fled from him, being used to that from him", "onlardan birini kesmek istediğini, develerin de buna alışık oldukları için ondan kaçtıklarını kasteder"),
    S_(mk("فَهُوَ كِنَايَةٌ عَنْ كَثْرَةِ نَحْرِهِ الْإِبِلَ لِلْأَضْيَافِ وَالنَّدَامَى، أَيْ: عَنْ كَرَمِهِ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "So it is a kinaya for his often slaughtering camels for guests and companions — for his generosity — as al-Zawzanī explains", "Bu, misafirler ve nedimler için çokça deve kesmesinden, yani cömertliğinden kinâyedir; Zevzenî böyle açıklar", "kinaya")), g=["form-iv-verbs", "hollow-verbs"]),
 NO("مَخَافَتِي", "makhafa", R("fail", "yam"), nt("مَصْدَرٌ مُضَافٌ إِلَى الْمَفْعُولِ، أَيْ: مَخَافَتُهَا إِيَّايَ (الزَّوْزَنِيُّ)؛ وَعِنْدَ الدُّرَّةِ إِلَى فَاعِلِهِ", "a masdar annexed to its object — «their fear of me» (al-Zawzanī); al-Durra takes it as annexed to its doer", "mef'ûlüne muzâf masdar: «onların benden korkması» (Zevzenî); Dürre'ye göre fâiline muzâftır", "masdar"), enc="ي", p=HEMI),
 NO("بَوَادِيَهَا", "badiya", R("maf"), nt("بَوَادِيهَا: أَوَائِلُهَا وَسَوَابِقُهَا (الزَّوْزَنِيُّ)؛ وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «نَوَادِيَهَا»", "بَوَادِيهَا: the first and foremost of them (al-Zawzanī); al-Tibrīzī and al-Durra have «نَوَادِيَهَا»", "بَوَادِيهَا: öndekileri, ilkleri (Zevzenî); Tebrîzî ve Dürre'de «نَوَادِيَهَا»", "jam-taksir"), enc="هَا"),
 VB("أَمْشِي", "masha", "mud-y", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ يَاءِ الْمُتَكَلِّمِ فِي «مَخَافَتِي» (الدُّرَّةُ)", "the clause is a hal of the speaker's ya in «مَخَافَتِي», in the seat of nasb (al-Durra)", "cümle «مَخَافَتِي»deki mütekellim yâsından hâl olarak mahallen mansûb (Dürre)", "al-hal-jumla-wa-rabituha"), who="أَنَا", g=["naqis-verbs"]),
 NO("بِعَضْبٍ", "adb", R("maj"), ON("أَمْشِي"), pre="bi"),
 NO("مُجَرَّدِ", "mujarrad", NA("عَضْبٍ", "jarr"), nt("أَيْ: مَسْلُولٍ مِنْ غِمْدِهِ", "that is, drawn from its sheath", "yani kınından çekilmiş", "ism-maful"), q=True),
])
V(88, "Then there passed a huge, fat she-camel, with a full udder, the choicest of the wealth of an old man, dry as a heavy staff, quarrelsome.",
  "Derken iri, semiz, memesi dolgun bir dişi deve geçti; kocaman bir asa gibi kurumuş, kavgacı bir ihtiyarın malının en seçkini.", [
 VB("فَمَرَّتْ", "marra", "madi-f", JM("atf", "أَثَارَتْ"), pre="fa", g=["doubled-verbs"]),
 NO("كَهَاةٌ", "kahat", "fail", nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: نَاقَةٌ كَهَاةٌ (الدُّرَّةُ)؛ الْكَهَاةُ: النَّاقَةُ الضَّخْمَةُ السَّمِينَةُ", "it describes a noun left out — «a huge she-camel» (al-Durra); الكَهَاة: a big, fat she-camel", "mahzûf bir mevsûfun sıfatıdır: «iri bir dişi deve» (Dürre); الكَهَاة: iri, semiz dişi deve", "hadhf-wa-taqdir")),
 NO("ذَاتُ", "dhat", NMH("raf", nth="2") + MUD),
 NO("خَيْفٍ", "khayf", "mi", nt("الْخَيْفُ: جِلْدُ الضَّرْعِ، وَجَمْعُهُ أَخْيَافٌ", "الخَيْف: the skin of the udder", "الخَيْف: memenin derisi")),
 NO("جُلَالَةٌ", "julala", NMH("raf", nth="3"), nt("الْجُلَالَةُ: النَّاقَةُ الضَّخْمَةُ السَّمِينَةُ، كَالْكَهَاةِ", "الجُلَالَة: a big, fat she-camel, as الكَهَاة", "الجُلَالَة: الكَهَاة gibi iri, semiz dişi deve"), p=HEMI),
 NO("عَقِيلَةُ", "aqila", NMH("raf", nth="4") + MUD),
 NO("شَيْخٍ", "shaykh", "mi", nt("قِيلَ: أَرَادَ بِهِ أَبَاهُ، يُرِيدُ أَنَّهُ نَحَرَ كَرَائِمَ مَالِ أَبِيهِ لِنُدَمَائِهِ، وَهُوَ أَحْرَى الْقَوْلَيْنِ بِالصَّوَابِ (الزَّوْزَنِيُّ)", "it is said he means his own father — that he slaughtered his father's choicest camels for his companions; this is the likelier view (al-Zawzanī)", "babasını kastettiği söylenir — babasının en seçkin develerini nedimleri için kestiğini; iki görüşten doğruya en yakını budur (Zevzenî)")),
 NO("كَالْوَبِيلِ", "wabil", R("maj"), ONH("naat", "شَيْخٍ"), nt("الْوَبِيلُ: الْعَصَا الضَّخْمَةُ", "الوَبِيل: a heavy staff", "الوَبِيل: kalın asa"),
    TSB("mm", ("الشَّيْخُ وَقَدْ يَبِسَ جِلْدُهُ وَنَحَلَ جِسْمُهُ مِنَ الْكِبَرِ", "the old man, his skin dried and his body wasted with age", "yaşlılıktan derisi kurumuş, bedeni zayıflamış ihtiyar"), ("الْعَصَا الضَّخْمَةُ", "a heavy staff", "kalın asa"), "ka"), pre="ka", g=TSB_TAGS),
 NO("يَلَنْدَدِ", "yalandad", NA("شَيْخٍ", "jarr", "", "2"), nt("الْيَلَنْدَدُ وَالْأَلَنْدَدُ وَالْأَلَدُّ: الشَّدِيدُ الْخُصُومَةِ", "اليَلَنْدَد, الأَلَنْدَد and الأَلَدّ: fierce in quarrel", "اليَلَنْدَد, الأَلَنْدَد ve الأَلَدّ: kavgada çetin"), q=True),
])
V(89, "He says, when the shank and the leg have fallen: «Do you not see that you have brought on a dire calamity?»",
  "İncik ve bacak yere düşmüşken der ki: «Görmüyor musun, korkunç bir felakete yol açtın?»", [
 VB("يَقُولُ", "qala", "mud", nt("وَالْجُمْلَةُ صَالِحَةٌ لِلْوَصْفِيَّةِ وَالْحَالِيَّةِ مِنْ «شَيْخٍ»، وَالِاسْتِئْنَافُ مُمْكِنٌ (الدُّرَّةُ)", "the clause may be an adjective or a hal of «شَيْخٍ», or open a new sentence (al-Durra)", "cümle «شَيْخٍ»in sıfatı ya da hâli olabilir; istînâf da mümkündür (Dürre)"), who=("هُوَ", SHAYKH), g=["hollow-verbs"]),
 PT("وَقَدْ", "qad", QAD_T, nt("وَجُمْلَةُ «قَدْ تَرَّ…» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «يَقُولُ»، وَالرَّابِطُ الْوَاوُ (الدُّرَّةُ)", "the clause «قَدْ تَرَّ…» is a hal of the doer of «يَقُولُ», in the seat of nasb, tied by the waw (al-Durra)", "«قَدْ تَرَّ…» cümlesi «يَقُولُ»un fâilinden hâl olarak mahallen mansûb; râbıt vâvdır (Dürre)"), pre="wa-hal", stem="قَدْ"),
 VB("تَرَّ", "tarra", "madi", nt("تَرَّ: سَقَطَ", "تَرَّ: it fell", "تَرَّ: düştü"), g=["doubled-verbs"]),
 NO("الْوَظِيفُ", "wazif", "fail"),
 NO("وَسَاقُهَا", "saq", AT("الْوَظِيفُ", "raf"), enc="هَا", pre="wa", p=HEMI),
 PT("أَلَسْتَ", "laysa", mk("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْمُخَاطَبِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا", "A defective, frozen past verb built on sukun because the ta of the one addressed is attached; the ta is its noun, in the seat of raf'", "Muhatap tâsına bitiştiği için sükûn üzere mebnî, câmid, nâkıs mâzî; tâ ismi, mahallen merfû", "kana-wa-akhawatuha"),
    nt("وَجُمْلَةُ «أَلَسْتَ تَرَى…» فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "the clause «أَلَسْتَ تَرَى…» is what is said, in the seat of nasb", "«أَلَسْتَ تَرَى…» cümlesi mekūlü'l-kavl olarak mahallen mansûb"),
    HD("اسْتِفْهَامٌ خَرَجَ إِلَى التَّقْرِيرِ وَالتَّوْبِيخِ: دَخَلَتِ الْهَمْزَةُ عَلَى النَّفْيِ لِيَحْمِلَهُ عَلَى الْإِقْرَارِ بِمَا أَتَى", "a question that has turned to making him own it, with reproach: the hamza comes upon a negation to bring him to admit what he has done", "takrîr ve azarlamaya dönmüş istifham: hemze, yaptığını ikrar ettirmek için nefye girmiştir"), pre="a", stem="لَسْتَ", pos="verb", g=["khuruj-al-istifham"]),
 VB("تَرَى", "raa", "mud-a", nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «لَيْسَ»", "the clause is the predicate of «لَيْسَ», in the seat of nasb", "cümle «لَيْسَ»in haberi olarak mahallen mansûb"), who="أَنْتَ", g=["naqis-verbs"]),
 PT("أَنْ", "an-mukhaffafa", mk("مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ", "أَنْ lightened from أَنَّ; its noun, the pronoun of the matter, is left out", "Ağırından hafifletilmiş أَنْ; ismi olan şe'n zamiri mahzûftur", "masail-inna-wal-mukhaffafa-fil-kafiya")),
 PT("قَدْ", "qad", QAD_T),
 VB("أَتَيْتَ", "ata", "madi-ta", nt("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنْ»، وَ«أَنْ» وَمَا بَعْدَهَا سَدَّتْ مَسَدَّ مَفْعُولَيْ «تَرَى»", "the clause is the predicate of أَنْ, in the seat of raf'; أَنْ with what follows fills the place of the two objects of «تَرَى»", "cümle «أَنْ»in haberi olarak mahallen merfû; «أَنْ» ve sonrası «تَرَى»nın iki mef'ûlünün yerini tutar"), g=["naqis-verbs"]),
 NO("بِمُؤْيِدِ", "muyid", R("maj"), ON("أَتَيْتَ"), nt("الْمُؤْيِدُ: الدَّاهِيَةُ الْعَظِيمَةُ الشَّدِيدَةُ", "المُؤْيِد: a great, dire calamity", "المُؤْيِد: büyük, çetin felaket"), pre="bi", q=True),
])
V(90, "And he said: «Come — what do you think should be done with a wine-bibber whose wrong against us is heavy and deliberate?»",
  "Ve dedi ki: «Bize karşı taşkınlığı ağır ve kasıtlı olan bir şarap düşkünü hakkında ne düşünüyorsunuz?»", [
 VB("وَقَالَ", "qala", "madi", JM("atf", "يَقُولُ"), who=("هُوَ", SHAYKH), pre="wa", g=["hollow-verbs"]),
 PT("أَلَا", "ala-tanbih", mk("حَرْفُ تَنْبِيهٍ وَاسْتِفْتَاحٍ", "A particle that calls for attention and opens the speech", "Tenbih ve istiftâh harfi", "huruf-tanbih")),
 PT("مَاذَا", "madha", mk("مَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَذَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرُهُ", "مَا is an interrogative noun built on sukun, the mubtada in the seat of raf'; ذَا is a relative noun built on sukun, its predicate, in the seat of raf'", "مَا sükûn üzere mebnî istifham ismi, mübteda olarak mahallen merfû; ذَا sükûn üzere mebnî ism-i mevsûl, haberi olarak mahallen merfû", "al-istifham", "ism-mawsul"), nt("وَيَجُوزُ جَعْلُ «مَاذَا» كُلِّهِ مَفْعُولًا مُقَدَّمًا لِـ«تَرَوْنَ» (الدُّرَّةُ)", "«مَاذَا» may also be taken whole as the object of «تَرَوْنَ», set first (al-Durra)", "«مَاذَا»nın tamamı «تَرَوْنَ»un öne alınmış mef'ûlü de sayılabilir (Dürre)"), pos="pron"),
 VB("تَرَوْنَ", "raa", "mud5", nt("وَالْجُمْلَةُ صِلَةُ «ذَا» لَا مَحَلَّ لَهَا، وَجُمْلَةُ «مَاذَا تَرَوْنَ» فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "the clause is the ṣila of ذَا and has no seat; «مَاذَا تَرَوْنَ» is what is said, in the seat of nasb", "cümle «ذَا»nın sılasıdır, mahalli yoktur; «مَاذَا تَرَوْنَ» mekūlü'l-kavl olarak mahallen mansûb"), g=["naqis-verbs"]),
 NO("بِشَارِبٍ", "sharib", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ، تَقْدِيرُهُ: أَنْ يُفْعَلَ وَنَحْوُهُ (الزَّوْزَنِيُّ)؛ وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: بِرَجُلٍ شَارِبٍ (الدُّرَّةُ)", "the phrase hangs on a verb left out — «what should be done» or the like (al-Zawzanī); it describes a noun left out, «a man who drinks» (al-Durra)", "câr-mecrûr mahzûf bir fiile müteallik: «ne yapılmalı» vb. (Zevzenî); mahzûf bir mevsûfun sıfatıdır: «içen bir adam» (Dürre)", "hadhf-wa-taqdir", "ism-fail"), pre="bi", p=HEMI),
 NO("شَدِيدٍ", "shadid", NMH("jarr", nth="2")),
 PJ("عَلَيْنَا", "عَلَيْ", "ala", "نَا", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«شَدِيدٍ»", "the phrase hangs on «شَدِيدٍ»", "câr-mecrûr «شَدِيدٍ»e müteallik")),
 NO("بَغْيُهُ", "baghy", "fail", nt("لِـ«شَدِيدٍ»", "of «شَدِيدٍ»", "«شَدِيدٍ»in fâili"), enc="هُ"),
 NO("مُتَعَمِّدِ", "mutaammid", NMH("jarr", nth="3"), nt("أَيْ: عَنْ تَعَمُّدٍ وَقَصْدٍ (الزَّوْزَنِيُّ)", "that is, purposely and by design (al-Zawzanī)", "yani kasten ve bilerek (Zevzenî)", "ism-fail"), q=True),
])
V(91, "And he said: «Let him be: its profit is only for him; and unless you hold back the farthest of the herd, he will slaughter more.»",
  "Ve dedi ki: «Bırakın onu; onun faydası yalnız onadır. Sürünün uzaktakilerini alıkoymazsanız daha fazlasını keser.»", [
 VB("وَقَالَ", "qala", "madi", JM("atf", "قَالَ"), who=("هُوَ", SHAYKH), pre="wa", g=["hollow-verbs"]),
 VB("ذَرُوهُ", "wadhara", "amr-w", JM("maqul"), nt("ذَرُوهُ: دَعُوهُ، وَالْمَاضِي مِنْهُمَا غَيْرُ مُسْتَعْمَلٍ عِنْدَ جُمْهُورِ الْأَئِمَّةِ اجْتِزَاءً بِـ«تَرَكَ» (الزَّوْزَنِيُّ)", "ذَرُوهُ: let him be — the past of these two verbs is not used, most authorities say, تَرَكَ doing its work (al-Zawzanī)", "ذَرُوهُ: onu bırakın — imamların çoğuna göre bu iki fiilin mâzîsi kullanılmaz, «تَرَكَ» onun yerini tutar (Zevzenî)"), enc="هُ"),
 PT("إِنَّمَا", "innama", mk("كَافَّةٌ وَمَكْفُوفَةٌ: «إِنَّ» كَفَّتْهَا «مَا» عَنِ الْعَمَلِ، وَهِيَ أَدَاةُ قَصْرٍ", "The restrained and restraining pair: مَا keeps إِنَّ from governing — a particle of restriction", "Kâffe ve mekfûfe: مَا, «إِنَّ»yi amelden alıkoymuştur; kasr edatıdır", "innama-kaffa"),
    HD("قَصْرٌ بِـ«إِنَّمَا»: قَصَرَ نَفْعَهَا عَلَيْهِ، أَيْ: لَا نَفْعَ لَهَا إِلَّا لَهُ (وَعَلَّلَهُ الزَّوْزَنِيُّ: «لِأَنَّهُ وَلَدِي الَّذِي يَرِثُنِي»)", "a restriction by إِنَّمَا: her profit is confined to him — «she profits none but him» (al-Zawzanī gives the reason: «for he is my son who will inherit from me»)", "«إِنَّمَا» ile kasr: onun faydası ona hasredilmiştir — «ondan başkasına faydası yoktur» (Zevzenî sebebini söyler: «çünkü o bana vâris olacak oğlumdur»)"), g=["qasr", "turuq-al-qasr"]),
 NO("نَفْعُهَا", "naf", R("mub"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ", "the masdar annexed to its doer", "masdarın fâiline izâfeti", "masdar"), enc="هَا"),
 PJ("لَهُ", "لَ", "li", "هُ", ONH("kh", "نَفْعُهَا"), nt("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ، وَهِيَ تَعْلِيلٌ لِلتَّرْكِ (الدُّرَّةُ)", "the clause is what is said, in the seat of nasb, and gives the reason for letting him be (al-Durra)", "cümle mekūlü'l-kavl olarak mahallen mansûb; bırakmanın gerekçesidir (Dürre)"), ref=TARAFA, p=HEMI),
 PT("وَإِلَّا", "in-shartiyya", mk("إِنْ حَرْفُ شَرْطٍ جَازِمٌ أُدْغِمَتْ نُونُهُ فِي «لَا» النَّافِيَةِ", "إِنْ, the conditional particle that governs jazm, its nun merged into the negating لَا", "Cezmeden şart harfi إِنْ; nûnu nefy edatı «لَا»ya idğam edilmiştir", "in-shartiyya", "al-majzum-wal-shart-wal-jaza"), pre="wa"),
 VB("تَكُفُّوا", "kaffa", "jz5", nt("وَالْأَلِفُ فَارِقَةٌ؛ الْكَفُّ: الْمَنْعُ (الزَّوْزَنِيُّ)؛ وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «تَرُدُّوا»", "the alif is the separating alif; الكَفّ: holding back (al-Zawzanī); al-Tibrīzī and al-Durra have «تَرُدُّوا»", "elif fârikadır; الكَفّ: alıkoymak (Zevzenî); Tebrîzî ve Dürre'de «تَرُدُّوا»"), by="shart", g=["doubled-verbs"]),
 NO("قَاصِيَ", "qasi", R("maf") + MUD, nt("مِنْ إِضَافَةِ الصِّفَةِ إِلَى الْمَوْصُوفِ (الدُّرَّةُ)، أَيْ: مَا بَعُدَ مِنْ هٰذِهِ الْإِبِلِ", "the description annexed to what it describes (al-Durra) — the farther ones of these camels", "sıfatın mevsûfa izâfeti (Dürre): bu develerin uzaktakileri", "ism-fail")),
 NO("الْبَرْكِ", "bark", "mi"),
 VB("يَزْدَدِ", "izdada", "jz", JM("jz"), nt("أَيْ: يَزْدَدْ طَرَفَةُ مِنْ عَقْرِهَا وَنَحْرِهَا (الزَّوْزَنِيُّ)", "that is, Ṭarafa will hamstring and slaughter more of them (al-Zawzanī)", "yani Tarafe onlardan daha fazlasını keser (Zevzenî)"), who=("هُوَ", TARAFA), by="jawab", q=True, g=["form-viii-verbs", "hollow-verbs"]),
])
# ---- His charge to Maʿbad's daughter: verses 92–97 -------------------------------------------------------------------------
IMRI = ("«امْرِئٍ»", "«امْرِئٍ»", "«امْرِئٍ»e")
def NA_IMRI(nth, sign=""):
    """the nth adjective of «امْرِئٍ» (v. 94), in jarr"""
    s = SIGN("jarr", sign); o = {"2": ("ثَانٍ", "second", "ikinci"), "3": ("ثَالِثٌ", "third", "üçüncü"), "4": ("رَابِعٌ", "fourth", "dördüncü"), "5": ("خَامِسٌ", "fifth", "beşinci")}[nth]
    return mk("نَعْتٌ " + o[0] + " لِـ«امْرِئٍ» فِي الْبَيْتِ ٩٤ " + s[0], "A " + o[1] + " adjective of «امْرِئٍ» in v. 94, " + s[1], "94. beyitteki «امْرِئٍ»in " + o[2] + " na'tı, " + s[2], "naat-sifa", *s.tags)
V(92, "Then the slave-women spent the day roasting her unborn calf in the hot ashes, and the choice cuts of fat hump were brought round to us.",
  "Câriyeler gün boyu onun karnındaki yavruyu sıcak külde kızarttılar; bize de besili hörgücün parçaları getirilip dolaştırıldı.", [
 VB("فَظَلَّ", "zalla-remain", "madi", nt("نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ»، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا (الدُّرَّةُ)", "defective, a sister of كَانَ; the clause is conjoined to what precedes (al-Durra)", "nâkıstır, «كَانَ»nin kardeşi; cümle öncesine ma'tûftur (Dürre)", "kana-wa-akhawatuha"), pre="fa-sabab", g=["doubled-verbs"]),
 NO("الْإِمَاءُ", "ama-handmaid", R("ism:ظَلَّ"), nt("جَمْعُ أَمَةٍ", "the plural of أَمَة", "«أَمَة»nın cem'i", "jam-taksir")),
 VB("يَمْتَلِلْنَ", "imtalla", "mud-fn", JM("kh", "ظَلَّ", "nasb"), nt("وَفُكَّ إِدْغَامُهُ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ؛ الِامْتِلَالُ: جَعْلُ الشَّيْءِ فِي الْمَلَّةِ، وَهِيَ الْجَمْرُ وَالرَّمَادُ الْحَارُّ", "its doubling is undone because the feminine nun is attached; الاِمْتِلَال: putting a thing in المَلَّة, the embers and hot ashes", "nûn-ı nisveye bitiştiği için idğamı çözülmüştür; الاِمْتِلَال: bir şeyi المَلَّة'ye, yani kora ve sıcak küle koymak"), g=["form-viii-verbs", "doubled-verbs"]),
 NO("حُوَارَهَا", "huwar", "maf", nt("الْحُوَارُ لِلنَّاقَةِ بِمَنْزِلَةِ الْوَلَدِ لِلْإِنْسَانِ", "the حُوَار of a she-camel is what a child is to a human", "devenin حُوَار'ı insanın çocuğu yerindedir"),
    S_(mk("وَفِيهِ كِنَايَةٌ: ذِكْرُ الْحُوَارِ دَالٌّ عَلَى أَنَّهَا كَانَتْ حُبْلَى، وَهِيَ مِنْ أَنْفَسِ الْإِبِلِ عِنْدَهُمْ (الزَّوْزَنِيُّ)، فَهُوَ كِنَايَةٌ عَنْ كَرَمِهِ بِأَنْفَسِ الْمَالِ", "There is a kinaya: naming the unborn calf shows she was with young — among the most prized of camels to them (al-Zawzanī) — so it points to his giving away the most precious of wealth", "Kinâye vardır: yavrunun anılması devenin gebe olduğunu gösterir; bu da onlarca en kıymetli develerdendir (Zevzenî); böylece malın en değerlisini cömertçe vermesinden kinâyedir", "kinaya")), enc="هَا", p=HEMI),
 VB("وَيُسْعَى", "saa-verb", "mud-a", JM("atf", "يَمْتَلِلْنَ"), nt("وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «بِالسَّدِيفِ» (الدُّرَّةُ)؛ أَيْ: يَسْعَى الْخَدَمُ عَلَيْنَا (الزَّوْزَنِيُّ)", "its deputy doer is the phrase «بِالسَّدِيفِ» (al-Durra) — «the servants go round to us» (al-Zawzanī)", "nâib-i fâili «بِالسَّدِيفِ» câr-mecrûrudur (Dürre) — «hizmetçiler bize dolaşıp getirir» (Zevzenî)"), maj=True, pre="wa", g=["naqis-verbs"]),
 PJ("عَلَيْنَا", "عَلَيْ", "ala", "نَا", ON("يُسْعَى")),
 NO("بِالسَّدِيفِ", "sadif", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ (الدُّرَّةُ)؛ السَّدِيفُ: السَّنَامُ، وَقِيلَ: قِطَعُ السَّنَامِ", "the phrase is in the seat of raf' as deputy doer (al-Durra); السَّدِيف: the hump — or cuts of the hump", "câr-mecrûr nâib-i fâil olarak mahallen merfû (Dürre); السَّدِيف: hörgüç — ya da hörgüç parçaları"), pre="bi"),
 NO("الْمُسَرْهَدِ", "musarhad", NA("السَّدِيفِ", "jarr"), nt("الْمُسَرْهَدُ: الْمُرَبَّى، أَيِ: الْمُسَمَّنُ", "المُسَرْهَد: well fed, fattened", "المُسَرْهَد: iyi beslenmiş, semirtilmiş", "ism-maful")),
])
V(93, "So if I die, proclaim my death with the praise I deserve, and rend your collar for me, O daughter of Maʿbad.",
  "Ölürsem ölümümü layık olduğum övgüyle duyur ve benim için yakanı yırt, ey Ma'bed'in kızı.", [
 PT("فَإِنْ", "in-shartiyya", IN_SH, JM("ist"), pre="fa-ist"),
 VB("مُتُّ", "mata-die", "madi-tu", IN_COND, nt("وَعِنْدَ التِّبْرِيزِيِّ «مِتُّ» بِكَسْرِ الْمِيمِ", "al-Tibrīzī has «مِتُّ», with a kasra on the mim", "Tebrîzî'de mîm'in kesresiyle «مِتُّ»"), g=["hollow-verbs"]),
 VB("فَانْعَيْنِي", "naa-announce", "amr-nun", JM("jzm"), nt("النَّعْيُ: إِشَاعَةُ خَبَرِ الْمَوْتِ، نَعَى يَنْعَى", "النَّعْي: spreading the news of a death — نَعَى يَنْعَى", "النَّعْي: ölüm haberini yaymak — نَعَى يَنْعَى"), enc="نِي", pre="fa-jaza", g=["naqis-verbs"]),
 PT("بِمَا", "ma-mawsula", mk("مَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«انْعَيْ»", "مَا is a relative noun built on sukun, in the seat of jarr; the phrase hangs on «انْعَيْ»", "مَا sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr; câr-mecrûr «انْعَيْ»ye müteallik", "ism-mawsul"), pre="bi", pos="pron"),
 PT("أَنَا", "ana", mk("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "A detached pronoun built on sukun, in the seat of raf' as mubtada", "Sükûn üzere mebnî munfasıl zamir; mübteda olarak mahallen merfû", "mubtada-khabar"), pos="pron"),
 NO("أَهْلُهُ", "ahl", "kh", nt("وَالْجُمْلَةُ صِلَةُ «مَا» لَا مَحَلَّ لَهَا، وَالْعَائِدُ الْهَاءُ؛ أَهْلُهُ: مُسْتَحِقُّهُ، كَقَوْلِهِ تَعَالَى: {وَكَانُوا أَحَقَّ بِهَا وَأَهْلَهَا} [الْفَتْح: ٢٦] (الزَّوْزَنِيُّ)", "the clause is the ṣila of مَا and has no seat, the هُ returning to it; أَهْلُهُ: deserving of it, as in «and they were most entitled to it and worthy of it» (al-Fatḥ 48:26) (al-Zawzanī)", "cümle «مَا»nın sılasıdır, mahalli yoktur; âid zamir hâ'dır; أَهْلُهُ: ona layık, {وَكَانُوا أَحَقَّ بِهَا وَأَهْلَهَا} (Fetih 48:26) âyetindeki gibi (Zevzenî)"), enc="هُ", p=HEMI),
 VB("وَشُقِّي", "shaqqa", "amr-nun", JM("atf", "انْعَيْنِي"), nt("فَهِيَ فِي مَحَلِّ جَزْمٍ مِثْلُهَا (الدُّرَّةُ)؛ يُوصِيهَا بِالثَّنَاءِ عَلَيْهِ وَالْبُكَاءِ (الزَّوْزَنِيُّ)", "so it too is in the seat of jazm (al-Durra); he charges her to praise him and weep (al-Zawzanī)", "o da onun gibi mahallen meczûmdur (Dürre); ona kendisini övmesini ve ağlamasını vasiyet eder (Zevzenî)"), pre="wa", g=["doubled-verbs"]),
 PJ("عَلَيَّ", "عَلَيْ", "ala", "يَ", ON("شُقِّي")),
 NO("الْجَيْبَ", "jayb", "maf"),
 PT("يَا", "ya-nida", mk("حَرْفُ نِدَاءٍ", "The vocative particle", "Nidâ harfi", "vocative-munada")),
 NO("ابْنَةَ", "ibna-ant", R("mun") + MUD, nt("ابْنَةُ أَخِيهِ، وَمَعْبَدٌ أَخُوهُ (الزَّوْزَنِيُّ)", "his brother's daughter — Maʿbad was his brother (al-Zawzanī)", "kardeşinin kızı — Ma'bed onun kardeşidir (Zevzenî)")),
 NO("مَعْبَدِ", "mabad-name", "mi", pos="propn", q=True),
])
V(94, "And do not make me like a man whose aim is not as my aim, who does not avail as I avail nor stand where I stand —",
  "Beni, gayesi benim gayem gibi olmayan, benim gibi iş görmeyen, benim gibi savaş yerlerinde bulunmayan bir adam gibi tutma —", [
 PT("وَلَا", "la-nahiya", mk("لَا نَاهِيَةٌ جَازِمَةٌ", "لَا of prohibition, which puts the verb in jazm", "Cezmeden nehiy lâsı", "la-nahiya"), nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «انْعَيْنِي» فَهِيَ فِي مَحَلِّ جَزْمٍ مِثْلُهَا (الدُّرَّةُ)", "the clause is conjoined to «انْعَيْنِي», so it too is in the seat of jazm (al-Durra)", "cümle «انْعَيْنِي»ye ma'tûftur, o da mahallen meczûmdur (Dürre)"), pre="wa"),
 PT("تَجْعَلِينِي", "jaala", mk("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ", "A present verb in jazm by the prohibitive لَا, its sign the dropping of the nun — one of the five verbs; the ya of the woman addressed is the doer, in the seat of raf'; the nun guards the ending, and the speaker's ya is the first object, in the seat of nasb", "Nehiy lâsıyla meczûm muzâri; ef'âl-i hamseden olduğu için cezm alâmeti nûnun hazfi; muhâtaba yâsı fâil, mahallen merfû; nûn vikâye içindir; mütekellim yâsı birinci mef'ûl, mahallen mansûb", "la-nahiya", "afal-khamsa", "mafulayn"), pos="verb"),
 NO("كَامْرِئٍ", "imru", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ الْمَفْعُولِ الثَّانِي، وَالْكُوفِيُّ يَجْعَلُ الْكَافَ اسْمًا بِمَعْنَى «مِثْلَ» فَهِيَ الْمَفْعُولُ الثَّانِي (الدُّرَّةُ)", "the phrase stands as the second object; the Kufan makes the kaf a noun meaning «like», itself the second object (al-Durra)", "câr-mecrûr ikinci mef'ûl yerindedir; Kûfeli kâfı «gibi» anlamında isim sayar, ikinci mef'ûl odur (Dürre)"), pre="ka"),
 PT("لَيْسَ", "laysa", mk("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "A defective, frozen past verb built on fatha", "Fetha üzere mebnî, câmid, nâkıs mâzî", "kana-wa-akhawatuha"), nt("وَجُمْلَةُ «لَيْسَ هَمُّهُ كَهَمِّي» فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«امْرِئٍ»", "the clause «لَيْسَ هَمُّهُ كَهَمِّي» is an adjective of «امْرِئٍ», in the seat of jarr", "«لَيْسَ هَمُّهُ كَهَمِّي» cümlesi «امْرِئٍ»in na'tı olarak mahallen mecrûr", "jumla-sifa"), pos="verb"),
 NO("هَمُّهُ", "hamm", R("ism:لَيْسَ"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الْهَمُّ أَصْلُهُ الْقَصْدُ، ثُمَّ يُجْعَلُ اسْمًا لِدَاعِيَةِ النَّفْسِ إِلَى الْعُلَا (الزَّوْزَنِيُّ)", "the masdar annexed to its doer; الهَمّ is in origin intent, then a name for the soul's urge toward the heights (al-Zawzanī)", "masdarın fâiline izâfeti; الهَمّ aslında kasıttır, sonra nefsi yücelere çeken dürtünün adı olmuştur (Zevzenî)", "masdar"), enc="هُ", p=HEMI),
 NO("كَهَمِّي", "hamm", R("maj", "yam"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «لَيْسَ»", "the phrase hangs on the omitted predicate of «لَيْسَ»", "câr-mecrûr «لَيْسَ»in mahzûf haberine müteallik"), enc="ي", pre="ka"),
 PT("وَلَا", "la-nafiya", LA_NAFY, pre="wa"),
 VB("يُغْنِي", "aghna", "mud-y", nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «لَيْسَ هَمُّهُ…» فَهِيَ نَعْتٌ مِثْلُهَا", "the clause is conjoined to «لَيْسَ هَمُّهُ…», so it too is an adjective", "cümle «لَيْسَ هَمُّهُ…» cümlesine ma'tûftur, o da na'ttır"), who=("هُوَ", IMRI), g=["form-iv-verbs", "naqis-verbs"]),
 NO("غَنَائِي", "ghana-avail", mk("مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، عَلَى تَقْدِيرِ «مِثْلَ»", "An absolute object in nasb by a fatha estimated before the speaker's ya, «like» being understood", "Mef'ûlün mutlak; «مِثْلَ» takdiriyle, mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb", "maful-mutlaq", "ya-al-mutakallim"),
    nt("أَيْ: وَلَا يُغْنِي غَنَاءً مِثْلَ غَنَائِي؛ الْغَنَاءُ: الْكِفَايَةُ (الزَّوْزَنِيُّ)", "that is, he does not avail with an availing like mine; الغَنَاء: sufficing (al-Zawzanī)", "yani benim iş görmem gibi iş görmez; الغَنَاء: yetmek, iş görmek (Zevzenî)"),
    HD("مُلْحَقٌ بِالْجِنَاسِ: جَمَعَ «يُغْنِي» وَ«غَنَائِي» الِاشْتِقَاقُ", "a figure joined to jinas: «يُغْنِي» and «غَنَائِي» are brought together by derivation", "cinâsa mülhak: «يُغْنِي» ile «غَنَائِي»yi iştikak bir araya getirmiştir"), enc="ي", g=["mulhaq-bil-jinas"]),
 NO("وَمَشْهَدِي", "mashhad", AT("غَنَائِي", "nasb", "yam"), nt("وَهُوَ مَصْدَرٌ مِيمِيٌّ بِمَعْنَى الشُّهُودِ وَهُوَ الْحُضُورُ، أَيْ: وَلَا يَشْهَدُ الْوَقَائِعَ شُهُودًا مِثْلَ شُهُودِي (الزَّوْزَنِيُّ)", "it is a masdar with mim meaning الشُّهُود, being present — «nor is present at the battles as I am present» (al-Zawzanī)", "الشُّهُود (hazır bulunmak) anlamında mîmli masdardır: «savaşlarda benim bulunduğum gibi bulunmaz» (Zevzenî)", "masdar"), enc="ي", pre="wa"),
])
V(95, "slow to a great matter, quick to foulness, broken, pushed about by men's fists —",
  "büyük işlere ağır, çirkinliğe çabuk, zelil, adamların yumruklarıyla itilip kakılan —", [
 NO("بَطِيءٍ", "bati", NA_IMRI("2"), nt("وَيَجُوزُ رَفْعُهُ فِي الْعَرَبِيَّةِ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ، وَالْقَافِيَةُ تُرَجِّحُ الْجَرَّ (الدُّرَّةُ)؛ الْبُطْءُ: ضِدُّ الْعَجَلَةِ", "raf' would be sound Arabic, as the predicate of an omitted mubtada, but the rhyme favours the jarr (al-Durra); البُطْء: the opposite of haste", "mahzûf mübtedanın haberi olarak ref'i dil bakımından câizdir; kafiye cerri tercih ettirir (Dürre); البُطْء: aceleciliğin zıddı", "sifa-mushabbaha")),
 HJ("عَنِ", "an"),
 NO("الْجُلَّى", "julla", R("maj", "maq"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بَطِيءٍ» لِأَنَّهُ صِفَةٌ مُشَبَّهَةٌ؛ الْجُلَّى: الْأَمْرُ الْعَظِيمُ", "the phrase hangs on «بَطِيءٍ», a ṣifa mushabbaha; الجُلَّى: the great matter", "câr-mecrûr sıfat-ı müşebbehe olan «بَطِيءٍ»e müteallik; الجُلَّى: büyük iş")),
 NO("سَرِيعٍ", "sari", NA_IMRI("3"),
    HD("مُقَابَلَةٌ: أَتَى بِـ«بَطِيءٍ عَنِ الْجُلَّى» ثُمَّ بِمَا يُقَابِلُهُ عَلَى التَّرْتِيبِ «سَرِيعٍ إِلَى الْخَنَا»: الْبُطْءُ وَالسُّرْعَةُ، وَالْبُعْدُ عَنِ الشَّيْءِ وَالْقَصْدُ إِلَيْهِ، وَالْأَمْرُ الْعَظِيمُ وَالْفُحْشُ", "a muqabala: he gives «slow to a great matter», then what answers it point for point, «quick to foulness» — slowness and speed, keeping off and making toward, the great matter and the foul", "mukâbele: «büyük işe ağır»ı, sonra sırasıyla ona karşılık geleni getirmiştir: «çirkinliğe çabuk» — ağırlık ile çabukluk, uzak durmak ile yönelmek, büyük iş ile çirkinlik"), g=["muqabala", "sifa-mushabbaha"]),
 HJ("إِلَى", "ila"),
 NO("الْخَنَا", "khana", R("maj", "maq"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَرِيعٍ»؛ الْخَنَا: الْفُحْشُ", "the phrase hangs on «سَرِيعٍ»; الخَنَا: foulness", "câr-mecrûr «سَرِيعٍ»e müteallik; الخَنَا: çirkinlik"), p=HEMI),
 NO("ذَلُولٍ", "dhalul", NA_IMRI("4"), nt("وَعِنْدَ التِّبْرِيزِيِّ «ذَلِيلٍ»", "al-Tibrīzī has «ذَلِيلٍ»", "Tebrîzî'de «ذَلِيلٍ»")),
 NO("بِأَجْمَاعِ", "jum-fist", R("maj") + MUD, nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُلَهَّدِ» بَعْدَهُمَا، وَعَلَى رِوَايَةِ كَسْرِ الْهَمْزَةِ «بِإِجْمَاعِ» بِـ«ذَلُولٍ» (الدُّرَّةُ)؛ جُمْعُ الْكَفِّ: الْكَفُّ مَجْمُوعَةً، وَالْجَمْعُ الْأَجْمَاعُ", "the phrase hangs on «مُلَهَّدِ» after it — on the reading with a kasra, «بِإِجْمَاعِ», on «ذَلُولٍ» (al-Durra); جُمْع الكَفّ: the hand closed, the fist — the plural الأَجْمَاع", "câr-mecrûr sonraki «مُلَهَّدِ»e müteallik — hemzenin kesresiyle «بِإِجْمَاعِ» rivayetinde «ذَلُولٍ»e (Dürre); جُمْع الكَفّ: yumruk — çoğulu الأَجْمَاع", "jam-taksir"), pre="bi"),
 NO("الرِّجَالِ", "rajul", "mi"),
 NO("مُلَهَّدِ", "mulahhad", NA_IMRI("5"), nt("وَلَا يَجُوزُ فِيهِ الرَّفْعُ لِلْقَافِيَةِ، وَهُوَ الَّذِي يُرَجِّحُ جَرَّ مَا قَبْلَهُ (الدُّرَّةُ)؛ التَّلْهِيدُ: مُبَالَغَةُ اللَّهْدِ وَهُوَ الدَّفْعُ بِجُمْعِ الْكَفِّ", "raf' is barred here by the rhyme, which is what favours the jarr of the words before (al-Durra); التَّلْهِيد: the intensive of اللَّهْد, pushing with the fist", "kafiye sebebiyle ref' câiz değildir; öncekilerin cerrini tercih ettiren de budur (Dürre); التَّلْهِيد: yumrukla itmek demek olan اللَّهْد'in mübalağası", "ism-maful"), q=True),
])
V(96, "Were I a weakling among men, the enmity of the man with a following, and of the man alone, would have harmed me;",
  "Erkekler arasında zayıf biri olsaydım, adamları olanın da tek başına olanın da düşmanlığı bana zarar verirdi;", [
 PT("فَلَوْ", "law", LAW_T, JM("ist"), pre="fa-ist"),
 PT("كُنْتُ", "kana", KUNTU, nt("فِعْلُ شَرْطِ «لَوْ»", "the verb of the condition of لَوْ", "«لَوْ»nun şart fiili"), pos="verb"),
 NO("وَغْلًا", "waghl", R("kh:كَانَ"), nt("الْوَغْلُ: أَصْلُهُ الضَّعِيفُ، وَيُسْتَعَارُ لِلَّئِيمِ؛ وَيُرْوَى «وَغْدًا»، وَهُوَ اللَّئِيمُ (الزَّوْزَنِيُّ)", "الوَغْل: in origin the weak, then borrowed for the base; it is also transmitted «وَغْدًا», the base (al-Zawzanī)", "الوَغْل: aslı zayıftır, alçak için de iğreti kullanılır; «وَغْدًا» (alçak) diye de rivayet edilir (Zevzenî)")),
 HJ("فِي", "fi"),
 NO("الرِّجَالِ", "rajul", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَغْلًا» لِأَنَّهُ بِمَعْنَى ضَعِيفٍ، أَوْ بِمَحْذُوفٍ نَعْتٍ لَهُ (الدُّرَّةُ)", "the phrase hangs on «وَغْلًا», which means «weak», or on an omitted adjective of it (al-Durra)", "câr-mecrûr «zayıf» anlamındaki «وَغْلًا»ya ya da onun mahzûf na'tına müteallik (Dürre)")),
 VB("لَضَرَّنِي", "darra", "madi", JM("jawab", "لَوْ"), nt("وَذُكِّرَ الْفِعْلُ وَفَاعِلُهُ «عَدَاوَةُ» لِأَنَّ تَأْنِيثَهَا غَيْرُ حَقِيقِيٍّ", "the verb is masculine though its doer «عَدَاوَةُ» is feminine, the feminine being not a real one", "fâili «عَدَاوَةُ» müennes olduğu hâlde fiil müzekkerdir, çünkü te'nîsi hakiki değildir", "al-fail-al-muzhar-wa-tanith-amilih"), enc="نِي", pre="la", g=["doubled-verbs"], p=HEMI),
 NO("عَدَاوَةُ", "adawa", R("fail") + MUD),
 NO("ذِي", "dhu", R("mi", "five") + MUD),
 NO("الْأَصْحَابِ", "sahib", "mi", nt("جَمْعُ صَاحِبٍ: الْأَتْبَاعُ", "the plural of صَاحِب — followers", "«صَاحِب»in cem'i — taraftarlar", "jam-taksir")),
 NO("وَالْمُتَوَحِّدِ", "mutawahhid", AT("ذِي", "jarr"), nt("أَيِ: الْمُنْفَرِدِ الَّذِي لَا أَتْبَاعَ لَهُ (الزَّوْزَنِيُّ)", "that is, the man alone, without followers (al-Zawzanī)", "yani taraftarı olmayan yalnız adam (Zevzenî)", "ism-fail"),
    HD("طِبَاقٌ بَيْنَ «ذِي الْأَصْحَابِ» وَ«الْمُتَوَحِّدِ»: ذُو الْأَتْبَاعِ وَالْمُنْفَرِدُ", "«ذِي الْأَصْحَابِ» and «الْمُتَوَحِّدِ» make a tibaq — the man with a following against the man alone", "«ذِي الْأَصْحَابِ» ile «الْمُتَوَحِّدِ» arasında tıbâk vardır: taraftarı olan ile yalnız olan"), pre="wa", g=["tibaq"]),
])
V(97, "but my daring against them has kept men from me, and my going forward, my truthfulness and my descent.",
  "fakat onlara karşı cesaretim, atılganlığım, sözümün doğruluğu ve soyum adamları benden uzak tuttu.", [
 PT("وَلٰكِنْ", "lakin", mk("حَرْفُ اسْتِدْرَاكٍ مُهْمَلٌ لَا عَمَلَ لَهُ", "A particle of correction; it governs nothing", "İstidrâk harfi; amel etmez", "aw-imma-am-la-bal-lakin-fil-kafiya"), nt("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا، وَالِاسْتِئْنَافُ مُمْكِنٌ (الدُّرَّةُ)", "the sentence is conjoined to what precedes, or opens afresh (al-Durra)", "cümle öncesine ma'tûftur; istînâf da mümkündür (Dürre)"), pre="wa"),
 VB("نَفَى", "nafa", "madi-muq", g=["naqis-verbs"]),
 PJ("عَنِّي", "عَنْ", "an", "ي", ON("نَفَى")),
 NO("الرِّجَالَ", "rajul", "maf", nt("أَيْ: نَفَى عَنِّي مُبَارَاةَ الرِّجَالِ وَمُجَارَاتَهُمْ (الزَّوْزَنِيُّ)؛ وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «الْأَعَادِيَ»", "that is, it kept from me men's vying and contending with me (al-Zawzanī); al-Tibrīzī and al-Durra have «الْأَعَادِيَ»", "yani adamların benimle yarışmasını ve çekişmesini benden uzak tuttu (Zevzenî); Tebrîzî ve Dürre'de «الْأَعَادِيَ»", "hadhf-wa-taqdir")),
 NO("جَرَاءَتِي", "jaraa", R("fail", "yam"), nt("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الْجُرْأَةُ وَالْجَرَاءَةُ وَاحِدٌ", "the masdar annexed to its doer; الجُرْأَة and الجَرَاءَة are one", "masdarın fâiline izâfeti; الجُرْأَة ile الجَرَاءَة birdir", "masdar"), enc="ي", p=HEMI),
 PJ("عَلَيْهِمْ", "عَلَيْ", "ala", "هِمْ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْمَصْدَرِ «جَرَاءَتِي»", "the phrase hangs on the masdar «جَرَاءَتِي»", "câr-mecrûr «جَرَاءَتِي» masdarına müteallik"), ref="الرِّجَالَ"),
 NO("وَإِقْدَامِي", "lb-iqdam", AT("جَرَاءَتِي", "raf", "yam"), nt("أَيْ: فِي الْحُرُوبِ (الزَّوْزَنِيُّ)", "that is, in war (al-Zawzanī)", "yani savaşlarda (Zevzenî)"), enc="ي", pre="wa"),
 NO("وَصِدْقِي", "sidq", AT("جَرَاءَتِي", "raf", "yam"), nt("أَيْ: صِدْقُ صَرِيمَتِي (الزَّوْزَنِيُّ)", "that is, the truth of my resolve (al-Zawzanī)", "yani azmimin sadakati (Zevzenî)"), enc="ي", pre="wa"),
 NO("وَمَحْتِدِي", "mahtid", AT("جَرَاءَتِي", "raf", "yam"), nt("الْمَحْتِدُ: الْأَصْلُ، أَيْ: كَرَمُ أَصْلِي (الزَّوْزَنِيُّ)", "المَحْتِد: the root, descent — «the nobility of my descent» (al-Zawzanī)", "المَحْتِد: asıl, soy — «soyumun asaleti» (Zevzenî)"), enc="ي", pre="wa"),
])
# ---- The close: «The days will show you»: verses 98–103 -----------------------------------------------------------------
V(98, "By your life! My affair is no cloud of gloom upon me by day, nor is my night endless upon me.",
  "Ömrüne andolsun ki ne gündüzüm işimi üzerime çöken bir kasvet yapar, ne de gecem üzerimde bitmek bilmeyen bir uzunluktadır.", [
 NO("لَعَمْرُكَ", "amr-qasam", R("mub"), nt("وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي (الدُّرَّةُ)", "its predicate must be left out — «is my oath» (al-Durra)", "haberi vücûben mahzûftur: «yeminimdir» (Dürre)", "hadhf-wa-taqdir", "huruf-al-qasam-fil-kafiya"), enc="كَ", pre="la-ibtida"),
 PT("مَا", "ma-nafiya", mk("نَافِيَةٌ حِجَازِيَّةٌ تَعْمَلُ عَمَلَ «لَيْسَ»", "The Ḥijāzī negative مَا, which governs as لَيْسَ does", "«لَيْسَ» gibi amel eden Hicazî nefy mâsı", "ma-la-mushabbaha"), JM("qasam")),
 NO("أَمْرِي", "amr", mk("اسْمُ «مَا» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ, "The noun of مَا, in raf' by a damma estimated before the speaker's ya", "«مَا»nın ismi; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû", "ma-la-mushabbaha", "ya-al-mutakallim"), enc="ي"),
 PJ("عَلَيَّ", "عَلَيْ", "ala", "يَ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «غُمَّةٍ»، كَانَ نَعْتًا لَهَا فَلَمَّا تَقَدَّمَ صَارَ حَالًا (الدُّرَّةُ)", "the phrase hangs on an omitted hal of «غُمَّةٍ» — it would have been its adjective, but set before it, it becomes a hal (al-Durra)", "câr-mecrûr «غُمَّةٍ»den mahzûf hâle müteallik; onun na'tı iken öne geçince hâl olmuştur (Dürre)")),
 NO("بِغُمَّةٍ", "ghumma", mk("خَبَرُ «مَا» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ", "The predicate of مَا, in nasb by an estimated fatha, its place taken by the kasra of the added jarr letter", "«مَا»nın haberi; mahalli zâid cer harfinin harekesi işgal ettiğinden takdîrî fetha ile mansûb", "ma-la-mushabbaha"),
    nt("الْغُمَّةُ وَالْغَمُّ وَاحِدٌ، وَأَصْلُ الْغَمِّ التَّغْطِيَةُ، وَمِنْهُ الْغَمَامُ لِأَنَّهُ يَغُمُّ السَّمَاءَ (الزَّوْزَنِيُّ)", "الغُمَّة and الغَمّ are one; الغَمّ is first covering — whence الغَمَام, cloud, for it covers the sky (al-Zawzanī)", "الغُمَّة ile الغَمّ birdir; الغَمّ'ın aslı örtmektir — göğü örttüğü için bulut (الغَمَام) de buradandır (Zevzenî)"), pre="bi-z", p=HEMI),
 NO("نَهَارِي", "nahar", R("zz", "yam"), nt("مُتَعَلِّقٌ بِـ«مَا» لِمَا فِيهَا مِنْ مَعْنَى النَّفْيِ، أَوْ بِـ«غُمَّةٍ»، أَوْ بِـ«أَمْرِي» (الدُّرَّةُ)", "it hangs on مَا for its sense of negation, or on «غُمَّةٍ», or on «أَمْرِي» (al-Durra)", "nefy anlamı taşıdığı için «مَا»ya, ya da «غُمَّةٍ»ye veya «أَمْرِي»ye müteallik (Dürre)"), enc="ي"),
 PT("وَلَا", "la-nafiya", mk("زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ", "Added, to strengthen the negation", "Nefyi pekiştirmek için zâid", "la-nafiya", "huruf-al-ziyada-fil-kafiya"), pre="wa"),
 NO("لَيْلِي", "layl", AT("أَمْرِي", "raf", "yam"), nt("وَإِعْرَابُهُ مِثْلُ إِعْرَابِهِ (الدُّرَّةُ)", "parsed like it (al-Durra)", "i'râbı onun gibidir (Dürre)"),
    HD("طِبَاقٌ بَيْنَ «نَهَارِي» وَ«لَيْلِي»", "«نَهَارِي» and «لَيْلِي» make a tibaq — day against night", "«نَهَارِي» ile «لَيْلِي» arasında tıbâk vardır: gündüz ile gece"), enc="ي", g=["tibaq"]),
 PJ("عَلَيَّ", "عَلَيْ", "ala", "يَ", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «سَرْمَدِ»", "the phrase hangs on an omitted hal of «سَرْمَدِ»", "câr-mecrûr «سَرْمَدِ»den mahzûf hâle müteallik")),
 NO("بِسَرْمَدِ", "sarmad", mk("مَعْطُوفٌ عَلَى «غُمَّةٍ»، مَجْرُورٌ لَفْظًا بِالْبَاءِ الزَّائِدَةِ مَنْصُوبٌ مَحَلًّا", "Conjoined to «غُمَّةٍ», in jarr in form by the added ba and in nasb in its seat", "«غُمَّةٍ»ye ma'tûf; zâid bâ ile lafzen mecrûr, mahallen mansûb", "atf-nasaq"),
    ZW("أَيْ: لَا يَطُولُ عَلَيَّ لَيْلِي حَتَّى كَأَنَّهُ صَارَ دَائِمًا سَرْمَدًا؛ وَتَلْخِيصُ الْمَعْنَى أَنَّهُ تَمَدَّحَ بِمَضَاءِ الصَّرِيمَةِ وَذَكَاءِ الْعَزِيمَةِ: لَا تَغُمُّنِي النَّوَائِبُ فَيَطُولَ لَيْلِي وَيُظْلِمَ نَهَارِي", "that is, my night does not drag on as though it had become everlasting; the sum of the meaning is that he boasts of resolve that cuts through and a quick will: misfortunes do not cloud me so that my night grows long and my day dark", "yani gecem sanki ebedî olmuş gibi uzamaz; mânânın özeti, keskin kararlılığı ve uyanık azmiyle övünmesidir: belalar beni kasvete boğmaz ki gecem uzasın, gündüzüm kararsın"),
    S_(mk("فَالْبَيْتُ كِنَايَةٌ عَنْ مَضَاءِ عَزِيمَتِهِ، كَمَا لَخَّصَهُ الزَّوْزَنِيُّ", "So the verse is a kinaya for the keenness of his resolve, as al-Zawzanī sums it up", "Beyit, azminin keskinliğinden kinâyedir; Zevzenî böyle özetler", "kinaya")), pre="bi-z", q=True),
])
V(99, "And many a day I have held my soul firm in its battle, guarding what must be guarded, and against its threats —",
  "Nice gün savaşında, korunması gerekeni gözeterek ve tehditlerine karşı canımı (yerinde) tuttum —", [
 NO("وَيَوْمَ", "yawm", mk("مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ، مَنْصُوبٌ بِالْفَتْحَةِ", "The object of a verb left out, «remember», in nasb by the fatha", "Mahzûf «اذْكُرْ» fiilinin mef'ûlü, fetha ile mansûb", "maful-bihi", "hadhf-wa-taqdir") + MUD,
    nt("عَلَى رِوَايَةِ النَّصْبِ؛ وَيُرْوَى بِالْجَرِّ عَلَى أَنَّ الْوَاوَ وَاوُ رُبَّ (الدُّرَّةُ)، وَبِهِ شَرَحَهُ الزَّوْزَنِيُّ: «وَرُبَّ يَوْمٍ حَبَسْتُ نَفْسِي…»", "on the reading in nasb; it is also transmitted in jarr, the waw being the waw of رُبَّ (al-Durra) — and so al-Zawzanī explains it: «and many a day I held my soul…»", "nasb rivayetine göredir; vâv'ın vâv-ı rubbe olmasıyla cer ile de rivayet edilir (Dürre); Zevzenî de böyle açıklar: «nice gün canımı tuttum…»"), pre="wa-ist"),
 VB("حَبَسْتُ", "habasa", "madi-tu", JM("mudaf", "يَوْمَ"), nt("أَيْ: حَبَسْتُ نَفْسِي عَلَى الْقِتَالِ وَالْفَزَعَاتِ وَتَهَدُّدِ الْأَقْرَانِ (الزَّوْزَنِيُّ)", "that is, I held my soul to the fighting, the alarms and the threats of my peers (al-Zawzanī)", "yani canımı savaşta, korkulu anlarda ve akranların tehditleri karşısında tuttum (Zevzenî)")),
 NO("النَّفْسَ", "nafs", "maf"),
 NO("عِنْدَ", "inda", R("zm") + MUD, ZON("حَبَسْتُ")),
 NO("عِرَاكِهِ", "irak", "mi", nt("الْعِرَاكُ وَالْمُعَارَكَةُ: الْقِتَالُ، وَأَصْلُهُمَا مِنَ الْعَرْكِ وَهُوَ الدَّلْكُ", "العِرَاك and المُعَارَكَة: fighting — from العَرْك, rubbing", "العِرَاك ve المُعَارَكَة: savaş — aslı ovmak demek olan العَرْك'ten"), enc="هِ", p=HEMI),
 NO("حِفَاظًا", "hifaz", "ml", nt("الْحِفَاظُ: الْمُحَافَظَةُ عَلَى مَا تَجِبُ الْمُحَافَظَةُ عَلَيْهِ مِنْ حِمَايَةِ الْحَوْزَةِ وَالذَّبِّ عَنِ الْحَرِيمِ (الزَّوْزَنِيُّ)", "الحِفَاظ: guarding what must be guarded — the defence of one's ground and of one's women (al-Zawzanī)", "الحِفَاظ: korunması gerekeni korumak — yurdu savunmak, haremi müdafaa etmek (Zevzenî)", "masdar")),
 HJ("عَلَى", "ala"),
 NO("عَوْرَاتِهِ", "awra", R("maj"), nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حِفَاظًا»", "the phrase hangs on «حِفَاظًا»", "câr-mecrûr «حِفَاظًا»ya müteallik", "jam-muannath-salim"), enc="هِ"),
 NO("وَالتَّهَدُّدِ", "tahaddud", AT("عِرَاكِهِ", "jarr"), nt("أَيْ: وَعِنْدَ التَّهَدُّدِ (الدُّرَّةُ)", "that is, and at the threatening (al-Durra)", "yani tehdit anında da (Dürre)"), pre="wa"),
])
V(100, "— upon ground where the young man fears death, where, when the shoulder-flesh jostles, it quivers.",
  "— yiğidin orada ölümden korktuğu, omuz etlerinin birbirine çarpışınca titrediği bir yerde.", [
 HJ("عَلَى", "ala", nt("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حَبَسْتُ» فِي الْبَيْتِ ٩٩ (الدُّرَّةُ)", "the phrase hangs on «حَبَسْتُ» in v. 99 (al-Durra)", "câr-mecrûr 99. beyitteki «حَبَسْتُ»e müteallik (Dürre)")),
 NO("مَوْطِنٍ", "mawtin", R("maj"), nt("الْمَوْطِنُ: الْمَوْضِعُ", "المَوْطِن: the place", "المَوْطِن: yer")),
 VB("يَخْشَى", "khashiya", "mud-a", JM("sifa", "مَوْطِنٍ"), g=["naqis-verbs"]),
 NO("الْفَتَى", "fata-youth", R("fail", "maq"), nt("أَيِ: الْكَرِيمُ (الزَّوْزَنِيُّ)", "that is, the noble man (al-Zawzanī)", "yani soylu kişi (Zevzenî)")),
 NO("عِنْدَهُ", "inda", R("zm"), ZON("يَخْشَى"), enc="هُ"),
 NO("الرَّدَى", "rada", R("maf", "maq"), nt("الرَّدَى: الْهَلَاكُ", "الرَّدَى: perishing", "الرَّدَى: helâk"), p=HEMI),
 PT("مَتَى", "mata", MATA_SH + mk("، مُتَعَلِّقٌ بِـ«تَعْتَرِكْ»", ", hanging on «تَعْتَرِكْ»", ", «تَعْتَرِكْ»e müteallik"), nt("وَ«مَتَى» وَمَدْخُولُهَا فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِـ«مَوْطِنٍ»، وَالرَّابِطُ الضَّمِيرُ فِي «فِيهِ» (الدُّرَّةُ)", "مَتَى with what follows is a second adjective of «مَوْطِنٍ», in the seat of jarr, tied by the pronoun in «فِيهِ» (al-Durra)", "«مَتَى» ve sonrası «مَوْطِنٍ»in ikinci na'tı olarak mahallen mecrûr; râbıt «فِيهِ»deki zamirdir (Dürre)")),
 VB("تَعْتَرِكْ", "itaraka", "jz", nt("الِاعْتِرَاكُ وَالتَّعَارُكُ وَاحِدٌ", "الاِعْتِرَاك and التَّعَارُك are one: jostling, grappling", "الاِعْتِرَاك ile التَّعَارُك birdir: çarpışmak"), by="shart", g=["form-viii-verbs"]),
 PJ("فِيهِ", "فِي", "fi", "هِ", ON("تَعْتَرِكْ"), ref="مَوْطِنٍ"),
 NO("الْفَرَائِصُ", "farisa-ant", "fail", nt("جَمْعُ فَرِيصَةٍ: لَحْمَةٌ عِنْدَ مَجْمَعِ الْكَتِفِ تُرْعَدُ عِنْدَ الْفَزَعِ", "the plural of فَرِيصَة, a piece of flesh where the shoulder joins, which quivers in fright", "«فَرِيصَة»nın cem'i: omuzun birleştiği yerde, korkuda titreyen et parçası", "jam-taksir")),
 VB("تُرْعَدِ", "arada", "jz", JM("jz"), nt("أَيْ: أُرْعِدَتْ مِنْ فَرْطِ الْفَزَعِ وَهَوْلِ الْمَقَامِ (الزَّوْزَنِيُّ)", "that is, it quivered for very fright and the terror of the place (al-Zawzanī)", "yani korkunun şiddetinden ve yerin dehşetinden titredi (Zevzenî)"),
    S_(mk("فَهُوَ كِنَايَةٌ عَنْ هَوْلِ الْمَقَامِ: ذَكَرَ رِعْدَةَ الْفَرَائِصِ وَأَرَادَ لَازِمَهَا مِنْ شِدَّةِ الْفَزَعِ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "So it is a kinaya for the terror of the place: he names the quivering of the shoulder-flesh and means what follows from it, extreme fear, as al-Zawzanī explains", "Bu, yerin dehşetinden kinâyedir: omuz etlerinin titremesini anmış, lâzımı olan korkunun şiddetini kastetmiştir; Zevzenî böyle açıklar", "kinaya")), who=("هِيَ", "الْفَرَائِصُ"), by="jawab", maj=True, q=True, g=["form-iv-verbs"]),
])
V(101, "And many a yellow arrow, held to the fire, I have waited by the fire to see how it would fall, and have trusted it to the hand of a man who never wins.",
  "Nice ateşte tutulmuş sarı (kumar) okunun dönüşünü ateşin başında bekledim ve onu hiç kazanamayan birinin eline emanet ettim.", [
 NO("وَأَصْفَرَ", "asfar", mk("مُبْتَدَأٌ مَجْرُورٌ لَفْظًا بِـ«رُبَّ» الْمَحْذُوفَةِ، وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ «أَفْعَلَ»، مَرْفُوعٌ مَحَلًّا", "A mubtada, in jarr in form by the رُبَّ understood — its sign the fatha for the kasra, a diptote (an adjective on أَفْعَل) — and in raf' in its seat", "Mübteda; takdir edilen «رُبَّ» ile lafzen mecrûr — vasfiyet ve «أَفْعَل» vezni sebebiyle gayr-i munsarif olduğundan kesre yerine fetha ile — mahallen merfû", "mubtada-khabar", "mamnu-min-sarf"),
    nt("وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: وَرُبَّ قِدْحٍ أَصْفَرَ (الزَّوْزَنِيُّ)", "it describes a noun left out — «many a yellow arrow (of the game)» (al-Zawzanī)", "mahzûf bir mevsûfun sıfatıdır: «nice sarı (kumar) oku» (Zevzenî)", "hadhf-wa-taqdir"), pre="wa-rubba"),
 NO("مَضْبُوحٍ", "madbuh", NMH("jarr", nth="2"), nt("ضَبَحْتُ الشَّيْءَ: قَرَّبْتُهُ مِنَ النَّارِ حَتَّى أَثَّرَتْ فِيهِ، وَإِنَّمَا فُعِلَ ذٰلِكَ لِيَصْلُبَ وَيَصْفَرَّ (الزَّوْزَنِيُّ)", "ضَبَحْتُ الشَّيْءَ: I held the thing to the fire till it took the mark of it — done so that it should harden and yellow (al-Zawzanī)", "ضَبَحْتُ الشَّيْءَ: onu ateşe yaklaştırdım, ateş onda iz bıraktı — sertleşsin ve sararsın diye yapılır (Zevzenî)", "ism-maful")),
 VB("نَظَرْتُ", "nazara", "madi-tu", nt("وَجُمْلَةُ «نَظَرْتُ…» فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ (الدُّرَّةُ)؛ نَظَرْتُ: انْتَظَرْتُ، وَمِنْهُ قَوْلُهُ تَعَالَى: {انْظُرُونَا نَقْتَبِسْ مِنْ نُورِكُمْ} [الْحَدِيد: ١٣] (الزَّوْزَنِيُّ)", "the clause «نَظَرْتُ…» is the predicate of the mubtada, in the seat of raf' (al-Durra); نَظَرْتُ: I waited for — as in «wait for us, that we may take of your light» (al-Ḥadīd 57:13) (al-Zawzanī)", "«نَظَرْتُ…» cümlesi mübtedanın haberi olarak mahallen merfû (Dürre); نَظَرْتُ: bekledim — {انْظُرُونَا نَقْتَبِسْ مِنْ نُورِكُمْ} (Hadîd 57:13) âyetindeki gibi (Zevzenî)")),
 NO("حِوَارَهُ", "hiwar", "maf", nt("الْحِوَارُ: مُرَاجَعَةُ الْحَدِيثِ، وَأَصْلُهُ مِنْ حَارَ يَحُورُ إِذَا رَجَعَ؛ أَيِ: انْتَظَرْتُ فَوْزَهُ أَوْ خَيْبَتَهُ (الزَّوْزَنِيُّ)", "الحِوَار: the coming back of talk — from حَارَ يَحُورُ, to return: I waited to see whether it would win or fail (al-Zawzanī)", "الحِوَار: sözün geri dönüşü — حَارَ يَحُورُ (dönmek) kökünden: kazanmasını ya da kaybetmesini bekledim (Zevzenî)"), enc="هُ", p=HEMI),
 HJ("عَلَى", "ala"),
 NO("النَّارِ", "nar", R("maj"), ON("نَظَرْتُ")),
 VB("وَاسْتَوْدَعْتُهُ", "istawdaa", "madi-tu", JM("atf", "نَظَرْتُ"), nt("وَالْهَاءُ أَوَّلُ مَفْعُولَيْهِ؛ اسْتَوْدَعْتُهُ وَأَوْدَعْتُهُ وَاحِدٌ", "the هُ is the first of its two objects; اسْتَوْدَعْتُهُ and أَوْدَعْتُهُ are one", "hâ iki mef'ûlünün birincisidir; اسْتَوْدَعْتُهُ ile أَوْدَعْتُهُ birdir", "mafulayn"), enc="هُ", pre="wa", g=["form-x-verbs"]),
 NO("كَفَّ", "kaff-hand", R("maf2") + MUD),
 NO("مُجْمِدِ", "mujmid", "mi", nt("الْمُجْمِدُ: الَّذِي لَا يَفُوزُ، وَأَصْلُهُ مِنَ الْجُمُودِ (الزَّوْزَنِيُّ)", "المُجْمِد: one who never wins — first from الجُمُود, being frozen (al-Zawzanī)", "المُجْمِد: hiç kazanamayan — aslı donmak demek olan الجُمُود'dan (Zevzenî)", "ism-fail"),
    ZW("يَفْتَخِرُ بِالْمَيْسِرِ، وَإِنَّمَا افْتَخَرَتِ الْعَرَبُ بِهِ لِأَنَّهُ لَا يَرْكَنُ إِلَيْهِ إِلَّا سَمْحٌ جَوَادٌ، ثُمَّ كَمَّلَ الْمَفْخَرَةَ بِإِيدَاعِ قِدْحِهِ كَفَّ مُجْمِدٍ قَلِيلِ الْفَوْزِ", "he boasts of the game of arrows — the Arabs boasted of it because none but the open-handed would turn to it — and crowns the boast by trusting his arrow to the hand of a man who seldom wins", "kumar okuyla (meysir) övünür — Araplar onunla övünürdü, çünkü ona ancak eli açık cömert kişi yanaşır —; sonra okunu kazancı az birinin eline emanet ederek övüncünü tamamlar"),
    S_(mk("فَالْبَيْتُ كِنَايَةٌ عَنْ كَرَمِهِ، كَمَا شَرَحَهُ الزَّوْزَنِيُّ", "So the verse is a kinaya for his generosity, as al-Zawzanī explains", "Beyit onun cömertliğinden kinâyedir; Zevzenî böyle açıklar", "kinaya")), q=True),
])
V(102, "The days will show you what you did not know, and news will come to you from one you did not provision.",
  "Günler sana bilmediğin şeyleri gösterecek; azık vermediğin biri de sana haberler getirecek.", [
 VB("سَتُبْدِي", "abda", "mud-y", JM("ist"), nt("يَقُولُ: سَتُطْلِعُكَ الْأَيَّامُ عَلَى مَا تَغْفُلُ عَنْهُ (الزَّوْزَنِيُّ)", "he says: the days will bring you to see what you are heedless of (al-Zawzanī)", "der ki: günler seni gafil olduğun şeylere muttali kılacak (Zevzenî)"), pre="sa", g=["form-iv-verbs", "naqis-verbs"]),
 PJ("لَكَ", "لَ", "li", "كَ", ON("تُبْدِي")),
 NO("الْأَيَّامُ", "yawm", "fail",
    HD("مَجَازٌ عَقْلِيٌّ: أُسْنِدَ الْإِبْدَاءُ إِلَى الْأَيَّامِ وَهِيَ زَمَانُهُ لَا فَاعِلُهُ (الْإِسْنَادُ إِلَى الزَّمَانِ)", "a majaz ʿaqli: the showing is ascribed to the days, which are its time and not its doer (ascription to the time)", "mecâz-ı aklî: göstermek, onun faili değil zamanı olan günlere isnat edilmiştir (zamana isnat)"), g=["jam-taksir", "majaz-aqli"]),
 PT("مَا", "ma-mawsula", mk("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "A relative noun built on sukun, in the seat of nasb as the object", "Sükûn üzere mebnî ism-i mevsûl; mef'ûlün bih olarak mahallen mansûb", "ism-mawsul", "maful-bihi"), pos="pron"),
 PT("كُنْتَ", "kana", mk("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْمُخَاطَبِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهُ", "A defective past verb built on sukun because the ta of the one addressed is attached; the ta is its noun, in the seat of raf'", "Muhatap tâsına bitiştiği için sükûn üzere mebnî nâkıs mâzî; tâ ismi, mahallen merfû", "kana-wa-akhawatuha"), nt("وَالْجُمْلَةُ صِلَةُ «مَا» لَا مَحَلَّ لَهَا، وَالْعَائِدُ مَحْذُوفٌ: مَا كُنْتَ جَاهِلًا بِهِ (الدُّرَّةُ)", "the clause is the ṣila of مَا and has no seat; the pronoun returning to it is left out — «what you were ignorant of» (al-Durra)", "cümle «مَا»nın sılasıdır, mahalli yoktur; âid zamir mahzûftur: «bilmediğin şey» (Dürre)", "hadhf-wa-taqdir"), pos="verb"),
 NO("جَاهِلًا", "jahil", R("kh:كَانَ"), p=HEMI),
 VB("وَيَأْتِيكَ", "ata", "mud-y", JM("atf", "تُبْدِي"), enc="كَ", pre="wa", g=["naqis-verbs"]),
 NO("بِالْأَخْبَارِ", "khabar", R("maj"), ON("يَأْتِي"), nt("جَمْعُ خَبَرٍ", "the plural of خَبَر", "«خَبَر»in cem'i", "jam-taksir"), pre="bi"),
 PT("مَنْ", "man", mk("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "A relative noun built on sukun, in the seat of raf' as the doer", "Sükûn üzere mebnî ism-i mevsûl; fâil olarak mahallen merfû", "ism-mawsul", "fail"), pos="pron"),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("تُزَوِّدِ", "zawwada", "jz", JM("sila"), nt("وَالْعَائِدُ مَحْذُوفٌ، أَيْ: مَنْ لَمْ تُزَوِّدْهُ (الدُّرَّةُ؛ وَالزَّوْزَنِيُّ: «مَنْ لَمْ تُزَوِّدْهُ»)", "the returning pronoun is left out — «one whom you did not provision» (al-Durra; al-Zawzanī: «one you did not provision»)", "âid zamir mahzûftur: «azık vermediğin kimse» (Dürre; Zevzenî: «azık vermediğin kimse»)", "hadhf-wa-taqdir"), who="أَنْتَ", by="lam", q=True, g=["form-ii-verbs"]),
])
V(103, "News will come to you from one for whom you bought no traveller's gear, and to whom you set no appointed time.",
  "Yolcu takımını kendisi için satın almadığın, kendisine bir buluşma vakti de belirlemediğin biri sana haberler getirecek.", [
 VB("وَيَأْتِيكَ", "ata", "mud-y", JM("atf", "يَأْتِيكَ"), enc="كَ", pre="wa", g=["naqis-verbs"]),
 NO("بِالْأَخْبَارِ", "khabar", R("maj"), ON("يَأْتِي"), pre="bi"),
 PT("مَنْ", "man", mk("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "A relative noun built on sukun, in the seat of raf' as the doer", "Sükûn üzere mebnî ism-i mevsûl; fâil olarak mahallen merfû", "ism-mawsul", "fail"), pos="pron"),
 PT("لَمْ", "lam-jazima", LAM_J),
 VB("تَبِعْ", "baa", "jz", JM("sila"), nt("بَاعَ قَدْ يَكُونُ بِمَعْنَى اشْتَرَى، وَهُوَ فِي الْبَيْتِ بِهٰذَا الْمَعْنَى (الزَّوْزَنِيُّ)", "بَاعَ can mean «to buy», and in this verse it does (al-Zawzanī)", "بَاعَ «satın almak» anlamına da gelir; beyitte bu anlamdadır (Zevzenî)"), who="أَنْتَ", by="lam", g=["hollow-verbs"]),
 PJ("لَهُ", "لَ", "li", "هُ", ON("تَبِعْ"), ref="مَنْ", p=HEMI),
 NO("بَتَاتًا", "batat", "maf", nt("الْبَتَاتُ: كِسَاءُ الْمُسَافِرِ وَأَدَاتُهُ", "البَتَات: a traveller's cloak and gear", "البَتَات: yolcunun örtüsü ve takımı")),
 PT("وَلَمْ", "lam-jazima", LAM_J, pre="wa"),
 VB("تَضْرِبْ", "daraba", "jz", JM("atf", "تَبِعْ"), nt("أَيْ: لَمْ تُبَيِّنْ، كَقَوْلِهِ تَعَالَى: {ضَرَبَ اللّٰهُ مَثَلًا} [النَّحْل: ٧٥] أَيْ بَيَّنَ وَأَوْضَحَ (الزَّوْزَنِيُّ)", "that is, you did not set out plainly — as in «God has struck a parable» (al-Naḥl 16:75), that is, has set it out clearly (al-Zawzanī)", "yani belirtmedin — {ضَرَبَ اللّٰهُ مَثَلًا} (Nahl 16:75) âyetinde «açıkladı, beyan etti» demek olduğu gibi (Zevzenî)"), who="أَنْتَ", by="lam"),
 PJ("لَهُ", "لَ", "li", "هُ", ON("تَضْرِبْ"), ref="مَنْ"),
 NO("وَقْتَ", "waqt", R("maf") + MUD),
 NO("مَوْعِدِ", "mawid", "mi", q=True),
])
# ==== VERSES ABOVE ====

# =====================================================================================================================
# The package: lexicon, paradigms, manifest
# =====================================================================================================================
AR_DIG = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
def ar_num(n): return str(n).translate(AR_DIG)
TOTAL = 103   # the poem's verses in al-Zawzanī's count
PLAN = [  # (first verse, last verse, the chapter's theme) — every verse of the poem, in al-Zawzanī's order, none skipped
 (1, 6, ("أَطْلَالُ خَوْلَةَ وَالظَّعَائِنُ", "Khawla's ruins; the litters like ships; the fawn of the tribe", "Havle'nin yurt kalıntıları; gemilere benzeyen mahfeler; kabilenin ceylanı")),
 (7, 13, ("ثَغْرُهَا وَوَجْهُهَا، ثُمَّ النَّاقَةُ", "Her smile and her face; then the she-camel", "Gülüşü ve yüzü; ardından dişi deve")),
 (14, 20, ("سَيْرُ النَّاقَةِ وَمَرْعَاهَا وَذَنَبُهَا وَفَخِذَاهَا", "The camel: her pace, her pasture, her tail and thighs", "Deve: yürüyüşü, otlağı, kuyruğu ve butları")),
 (21, 27, ("خَلْقُ النَّاقَةِ: الْمِرْفَقَانِ وَالْقَنْطَرَةُ وَالظَّهْرُ", "The camel's frame: the elbows, the Greek's bridge, the back", "Devenin yapısı: dirsekler, Rûmî'nin köprüsü, sırt")),
 (28, 33, ("الْعُنُقُ وَالْجُمْجُمَةُ وَالْخَدُّ وَالْعَيْنَانِ", "The neck, the skull, the cheek, the eyes", "Boyun, kafatası, yanak, gözler")),
 (34, 39, ("الْأُذُنَانِ وَالْقَلْبُ وَالْأَنْفُ وَسَيْرُهَا كَمَا يَشَاءُ", "The ears, the heart, the nose; her pace at his will", "Kulaklar, kalp, burun; dilediğince yürüyüşü")),
 (40, 47, ("عَلَى مِثْلِهَا أَمْضِي، وَفَخْرُ الْفَتَى", "«On such a one I ride»; the young man's boast", "«Böylesinin sırtında giderim»; yiğidin övünmesi")),
 (48, 54, ("النَّدَامَى وَالْقَيْنَةُ وَإِفْرَادُ الْبَعِيرِ الْمُعَبَّدِ", "The boon companions, the singing girl, and the outcast", "Nedimler, şarkıcı câriye ve dışlanan adam")),
 (55, 61, ("اللَّائِمُ وَالثَّلَاثُ الَّتِي هِيَ مِنْ عِيشَةِ الْفَتَى", "The reproacher; the three joys of a young man's life", "Kınayan kişi; yiğidin hayatındaki üç zevk")),
 (62, 67, ("الْمَوْتُ يُسَوِّي بَيْنَ الْقُبُورِ", "Death, which levels the graves", "Kabirleri bir eden ölüm")),
 (68, 73, ("عِتَابُ ابْنِ الْعَمِّ مَالِكٍ", "The reproach of his cousin Mālik", "Amcaoğlu Mâlik'e sitem")),
 (74, 79, ("ظُلْمُ ذَوِي الْقُرْبَى", "The wrong done by one's own kin", "Yakınların zulmü")),
 (80, 85, ("لَوْ شَاءَ رَبِّي، وَالسَّيْفُ", "«Had my Lord willed»; the sword", "«Rabbim dileseydi»; kılıç")),
 (86, 91, ("عَقْرُ النَّاقَةِ لِلضِّيفَانِ", "The camel slaughtered for the guests", "Misafirler için kesilen deve")),
 (92, 97, ("وَصِيَّتُهُ لِابْنَةِ مَعْبَدٍ", "His charge to Maʿbad's daughter", "Ma'bed'in kızına vasiyeti")),
 (98, 103, ("خَاتِمَةُ الْقَصِيدَةِ: سَتُبْدِي لَكَ الْأَيَّامُ", "The close: «The days will show you»", "Kasidenin sonu: «Günler sana gösterecek»")),
]
assert [a for a, b, t in PLAN] == [1] + [b + 1 for a, b, t in PLAN[:-1]] and PLAN[-1][1] == TOTAL and all(6 <= b - a + 1 <= 8 for a, b, t in PLAN)
# only what is finished is published: the chapters whose verses are all authored, contiguously from verse 1
DONE = 0
while DONE + 1 in VERSE: DONE += 1
READY = [(a, b, t) for a, b, t in PLAN if b <= DONE]
LAST = READY[-1][1] if READY else 0
CHAPS = [S1] + [[{"id": "s%d" % (i + 1), **VERSE[n]} for i, n in enumerate(range(a, b + 1))] for a, b, t in READY]
TITLES = [{"ar": "خَبَرُ طَرَفَةَ عِنْدَ ابْنِ قُتَيْبَةَ", "en": "The poet's story, from Ibn Qutayba", "tr": "Şairin haberi — İbn Kuteybe'den"}] + [
    {"ar": "%s (الْأَبْيَاتُ %s–%s)" % (t[0], ar_num(a), ar_num(b)), "en": "%s (verses %d–%d)" % (t[1], a, b), "tr": "%s (%d–%d. beyitler)" % (t[2], a, b)} for a, b, t in READY]
ALL_AUTHORED = S1 + [VERSE[n] for n in sorted(VERSE)]     # every sentence written so far, published or waiting

# ---- the lexicon: every key by lemma identity from the shelf; the entries in NEW_GLOSS are new ---------------------------
PREF = ["muallaqat-imri-al-qays", "muallaqat-zuhayr", "talkhis-al-miftah", "al-kafiya", "izhar-al-asrar", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "marah-al-arwah", "tasrif-al-izzi",
        "bad-al-amali", "abu-hanifa-wa-al-safina", "alb-arslan-wa-malazgird", "ibn-khaldun-wa-timur", "fath-al-qustantiniyya"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
# the packages staged beside this one (parallel authors) count as shelf for the global-key check
PREF += sorted(d.name for d in OUT_ROOT.iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG) if OUT_ROOT != ROOT / "content/samples" else []
def _pkg_dir(p): return (ROOT / "content/samples" / p) if (ROOT / "content/samples" / p / "glossary.json").exists() else (OUT_ROOT / p)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
def find_gloss(k):
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

def G(lemma, pos, en, tr, level=6, root=None, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
NEW_GLOSS = {
 # ---- the khabar ----
 "tarafa": G("طَرَفَة", "propn", "Ṭarafa ibn al-ʿAbd of Bakr — the poet of this Muʿallaqa, killed young (a diptote)", "Bekroğullarından Tarafe b. el-Abd — bu Muallaka'nın genç yaşta öldürülen şairi (gayr-i munsarif)"),
 "sufyan": G("سُفْيَان", "propn", "Sufyān — a man's name (a diptote)", "Süfyân — erkek adı (gayr-i munsarif)"),
 "ajwad": G("أَجْوَد", "noun", "better, finer; the finest (elative of جَيِّد)", "daha iyi, daha güzel; en iyisi (جَيِّد'den ism-i tafdîl)", 5, "ج و د"),
 "tawila-ode": G("طَوِيلَة", "noun", "a long one — here: a long ode (the Muʿallaqa)", "uzun olan — burada: uzun kaside (Muallaka)", 5, "ط و ل"),
 "khawla": G("خَوْلَة", "propn", "Khawla — a woman's name: a woman of Kalb, al-Zawzanī says (a diptote)", "Havle — kadın adı; Zevzenî'ye göre Kelb kabilesinden bir kadın (gayr-i munsarif)"),
 "burqa": G("بُرْقَة", "noun", "ground where stones or gravel are mixed with the earth (pl. بُرَق, بِرَاق)", "toprağına taş ya da çakıl karışmış yer (çoğ. بُرَق, بِرَاق)", 6, "ب ر ق"),
 "thahmad": G("ثَهْمَد", "propn", "Thahmad — a place", "Sehmed — bir yer adı"),
 "rawin": G("رَاوٍ", "noun", "a transmitter (of verse or of reports) (pl. رُوَاة)", "râvî, (şiir ya da haber) nakleden (çoğ. رُوَاة)", 5, "ر و ي", "رُوَاة"),
 "abid-poet": G("عَبِيد", "propn", "ʿAbīd ibn al-Abraṣ — an early poet of the tribe of Asad", "Abîd b. el-Ebras — Esed kabilesinden eski bir şair"),
 "hija": G("هِجَاء", "noun", "lampoon, satire in verse (masdar of هَجَا)", "hiciv, şiirle yerme (هَجَا'nın masdarı)", 5, "ه ج و"),
 "ahdam": G("أَهْضَم", "noun", "slender in the waist, lean-bellied (fem. هَضْمَاء)", "beli ince, karnı içeri çekik (müennesi هَضْمَاء)", 6, "ه ض م"),
 "akafa": G("عَكَفَ", "verb", "to keep to, to stay close about (عَكَفَ يَعْكُفُ)", "bir yere/kimseye bağlanıp ayrılmamak (عَكَفَ يَعْكُفُ)", 5, "ع ك ف", form="I"),
 "asib": G("عَسِيب", "noun", "a straight palm-branch stripped of its leaves; also the bone of the tail (pl. عُسُب)", "yaprakları sıyrılmış düz hurma dalı; ayrıca kuyruk kemiği (çoğ. عُسُب)", 6, "ع س ب", "عُسُب"),
 "sarara": G("سَرَارَة", "noun", "the best and most fertile ground of a valley", "vadinin en iyi, en verimli yeri", 6, "س ر ر"),
 "malham": G("مَلْهَم", "propn", "Malham — a village of al-Yamāma famed for its palms (a diptote)", "Melhem — Yemâme'de hurmalığıyla ünlü bir köy (gayr-i munsarif)"),
 # ---- verses 1–6 ----
 "tajallada": G("تَجَلَّدَ", "verb", "to put on fortitude, to make oneself bear up (Form V)", "kendini metin olmaya zorlamak, dayanmaya çalışmak (tefa''ul)", 6, "ج ل د", form="V"),
 "hidj": G("حِدْج", "noun", "a women's camel-litter (pl. حُدُوج, أَحْدَاج)", "kadınların bindiği deve mahfesi (çoğ. حُدُوج, أَحْدَاج)", 6, "ح د ج", "حُدُوج"),
 "malikiyya": G("مَالِكِيَّة", "noun", "a woman of Banū Mālik — a clan of Kalb, al-Zawzanī says", "Benî Mâlik'ten kadın — Zevzenî'ye göre Kelb'in bir kolu", 6, "م ل ك"),
 "khaliyya": G("خَلِيَّة", "noun", "a great ship (pl. خَلَايَا)", "büyük gemi (çoğ. خَلَايَا)", 6, "خ ل و", "خَلَايَا"),
 "safin": G("سَفِين", "noun", "ships — the plural of سَفِينَة (itself pluralised سُفُن); it may also be a singular", "gemiler — سَفِينَة'nin cem'i (kendi cem'i سُفُن); müfred de olabilir", 6, "س ف ن"),
 "nasifa": G("نَاصِفَة", "noun", "a place where the side of a valley opens out, a broad channel (pl. نَوَاصِف)", "vadi kenarının genişlediği yer, geniş su yatağı (çoğ. نَوَاصِف)", 6, "ن ص ف", "نَوَاصِف"),
 "dad": G("دَد", "propn", "Dad — said to be a valley; the word also means play, sport", "Ded — bir vadi adı olduğu söylenir; kelime «oyun, eğlence» anlamına da gelir"),
 "adawli": G("عَدَوْلِيّ", "noun", "of ʿAdawlā — a tribe of al-Baḥrayn known for its great ships (fem. عَدَوْلِيَّة)", "Adevlâ'ya mensup — büyük gemileriyle bilinen Bahreynli bir kabile (müennesi عَدَوْلِيَّة)", 6),
 "yamin-man": G("يَامِن", "propn", "Yāmin — «Ibn Yāmin», a shipowner of al-Baḥrayn", "Yâmin — «İbn Yâmin»: Bahreynli bir gemi sahibi"),
 "jara-stray": G("جَارَ", "verb", "to turn off the way, to swerve; (elsewhere) to act unjustly (جَارَ يَجُورُ)", "yoldan sapmak; (başka yerde) zulmetmek (جَارَ يَجُورُ)", 5, "ج و ر", form="I"),
 "habab": G("حَبَاب", "noun", "the ripples, the small waves of water (sing. حَبَابَة)", "suyun dalgacıkları (tekili حَبَابَة)", 6, "ح ب ب"),
 "hayzum": G("حَيْزُوم", "noun", "the breast; of a ship, the prow (pl. حَيَازِيم)", "göğüs; gemide pruva (çoğ. حَيَازِيم)", 6, "ح ز م", "حَيَازِيم"),
 "turb": G("تُرْب", "noun", "earth, dust — the same as تُرَاب", "toprak — تُرَاب ile aynı", 6, "ت ر ب"),
 "mufayil": G("مُفَايِل", "noun", "a player at الفِيَال — the game of hiding a thing in a heap of earth and parting the heap in two", "«fiyâl» oyuncusu — toprak yığınına bir şey gömüp yığını ikiye bölerek oynanan oyun", 6, "ف ي ل"),
 "ahwa": G("أَحْوَى", "noun", "dark-lipped, dusky; a gazelle with a dark tinge (fem. حَوَّاء, pl. حُوّ)", "dudakları esmer, koyu renkli; rengi koyuya çalan ceylan (müennesi حَوَّاء, çoğ. حُوّ)", 6, "ح و و"),
 "nafada": G("نَفَضَ", "verb", "to shake (a thing, so that what is on it falls) (نَفَضَ يَنْفُضُ)", "silkelemek (نَفَضَ يَنْفُضُ)", 5, "ن ف ض", form="I"),
 "mard": G("مَرْد", "noun", "the fruit of the arāk tree", "erâk ağacının meyvesi", 6, "م ر د"),
 "shadin": G("شَادِن", "noun", "a young gazelle grown strong enough to leave its mother", "güçlenip annesinden ayrılabilen ceylan yavrusu", 6, "ش د ن"),
 "muzahir": G("مُظَاهِر", "noun", "wearing one thing over another — a garment, a coat of mail, a necklace (ism fa'il of ظَاهَرَ)", "bir şeyi diğerinin üstüne giyen/takan — elbise, zırh, gerdanlık (ظَاهَرَ'den ism-i fâil)", 6, "ظ ه ر"),
 "simt": G("سِمْط", "noun", "the thread on which gems are strung; a string of gems (pl. سُمُوط)", "mücevherlerin dizildiği ip; mücevher dizisi (çoğ. سُمُوط)", 6, "س م ط", "سُمُوط"),
 # ---- verses 7–13 ----
 "khadhul": G("خَذُول", "noun", "a doe that has left her young behind (to graze with the herd)", "yavrularını bırakıp (sürüyle otlamaya) giden ceylan", 6, "خ ذ ل"),
 "raa-graze": G("رَاعَى", "verb", "to graze along with (a herd); (elsewhere) to watch, to have regard for (Form III)", "(bir sürüyle) birlikte otlamak; (başka yerde) gözetmek (müfâale)", 6, "ر ع ي", form="III"),
 "rabrab": G("رَبْرَب", "noun", "a herd of gazelles or of wild cattle", "ceylan ya da yaban sığırı sürüsü", 6, "ر ب ب"),
 "khamila": G("خَمِيلَة", "noun", "a sand-tract that bears growth; ground thick with trees (pl. خَمَائِل)", "bitki bitiren kumluk; ağaçlık arazi (çoğ. خَمَائِل)", 6, "خ م ل", "خَمَائِل"),
 "barir": G("بَرِير", "noun", "the ripe fruit of the arāk tree (sing. بَرِيرَة)", "erâk ağacının olgun meyvesi (tekili بَرِيرَة)", 6, "ب ر ر"),
 "irtada": G("اِرْتَدَى", "verb", "to put on a mantle, to wrap oneself (in a thing) (Form VIII)", "ridâ giymek, (bir şeye) bürünmek (iftiâl)", 6, "ر د ي", form="VIII"),
 "alma": G("أَلْمَى", "noun", "dark of lip or gum (fem. لَمْيَاء, pl. لُمْي)", "dudağı ya da diş eti esmer (müennesi لَمْيَاء, çoğ. لُمْي)", 6, "ل م ي"),
 "munawwir": G("مُنَوِّر", "noun", "in flower, blossoming (ism fa'il of نَوَّرَ) — here: a flowering camomile", "çiçek açmış (نَوَّرَ'den ism-i fâil) — burada: çiçek açmış papatya", 6, "ن و ر"),
 "takhallala": G("تَخَلَّلَ", "verb", "to pass into the midst of, to come up through (Form V)", "arasına girmek, içinden geçip çıkmak (tefa''ul)", 6, "خ ل ل", form="V"),
 "dis": G("دِعْص", "noun", "a hill of sand, a dune (pl. أَدْعَاص)", "kum tepesi (çoğ. أَدْعَاص)", 6, "د ع ص", "أَدْعَاص"),
 "nadin": G("نَدٍ", "noun", "moist, damp — short of being wet (from نَدِيَ يَنْدَى)", "nemli, rutubetli — ıslaklık derecesine varmayan (نَدِيَ يَنْدَى'dan)", 6, "ن د ي"),
 "iyat": G("إِيَاة", "noun", "the rays, the radiance of the sun", "güneşin ışınları, ışıltısı", 6, "أ ي ي"),
 "litha": G("لِثَة", "noun", "the gum, the flesh in which the teeth are set (pl. لِثَات)", "diş eti (çoğ. لِثَات)", 6, "ل ث ي", "لِثَات"),
 "asaffa": G("أَسَفَّ", "verb", "to dust, to sprinkle (a powder) on a thing (Form IV; passive أُسِفَّ)", "(toz hâlinde bir şeyi) serpmek (if'âl; meçhulü أُسِفَّ)", 6, "س ف ف", form="IV"),
 "kadama": G("كَدَمَ", "verb", "to bite (كَدَمَ يَكْدِمُ)", "ısırmak (كَدَمَ يَكْدِمُ)", 6, "ك د م", form="I"),
 "ithmid": G("إِثْمِد", "noun", "antimony, kohl", "sürme taşı, sürme", 6, "ث م د"),
 "takhaddada": G("تَخَدَّدَ", "verb", "to shrivel, to become wrinkled (Form V)", "büzüşmek, kırışmak (tefa''ul)", 6, "خ د د", form="V"),
 "ihtidar": G("اِحْتِضَار", "noun", "coming, being present — the same as حُضُور (masdar of اِحْتَضَرَ)", "gelme, hazır olma — حُضُور ile aynı (اِحْتَضَرَ'nin masdarı)", 6, "ح ض ر"),
 "awja": G("عَوْجَاء", "noun", "a she-camel that will not go straight, so high is her spirit (lit. «crooked»; a diptote)", "aşırı canlılığından düz yürümeyen dişi deve (lafzen «eğri»; gayr-i munsarif)", 6, "ع و ج"),
 "mirqal": G("مِرْقَال", "noun", "very swift of pace — the intensive of مُرْقِل, from الإِرْقَال, a pace between walking and running", "çok hızlı yürüyen — مُرْقِل'in mübalağası; الإِرْقَال: yürüyüşle koşu arası gidiş", 6, "ر ق ل"),
 "amun": G("أَمُون", "noun", "sure-footed, strongly built (of a she-camel): one whose stumbling is not feared", "ayağı sağlam, yapısı kuvvetli (dişi deve): sürçmesinden korkulmayan", 6, "أ م ن"),
 "iran": G("إِرَان", "noun", "a great bier, a wooden coffin", "büyük tabut", 6, "أ ر ن"),
 "nasaa-urge": G("نَصَأَ", "verb", "to urge on, to drive (a beast) with a shout (نَصَأَ يَنْصَأُ)", "(hayvanı) haykırarak sürmek (نَصَأَ يَنْصَأُ)", 6, "ن ص أ", form="I"),
 "lahib": G("لَاحِب", "noun", "a plain, clearly marked road", "apaçık, belirgin yol", 6, "ل ح ب"),
 "burjud": G("بُرْجُد", "noun", "a thick striped cloak", "çizgili kalın örtü", 6),
 "jumaliyya": G("جُمَالِيَّة", "noun", "a she-camel built like a he-camel, firm of frame", "erkek deve yapılı, sağlam bünyeli dişi deve", 6, "ج م ل"),
 "wajna": G("وَجْنَاء", "noun", "a she-camel firm and close of flesh; also: large in the cheeks (a diptote)", "eti sıkı ve dolgun dişi deve; ayrıca: elmacık kemikleri iri (gayr-i munsarif)", 6, "و ج ن"),
 "rada-run": G("رَدَى", "verb", "to run — in origin of an ass, between his rolling-place and his tether (رَدَى يَرْدِي رَدَيَانًا)", "koşmak — aslında eşeğin yuvarlandığı yer ile bağı arasındaki koşusu (رَدَى يَرْدِي رَدَيَانًا)", 6, "ر د ي", form="I"),
 "safannaja": G("سَفَنَّجَة", "noun", "a hen-ostrich", "dişi devekuşu", 6),
 "bara-show": G("بَرَى", "verb", "بَرَى لَهُ: to present oneself to, to come up before (بَرَى يَبْرِي)", "بَرَى لَهُ: birine kendini göstermek, karşısına çıkmak (بَرَى يَبْرِي)", 6, "ب ر ي", form="I"),
 "azar": G("أَزْعَر", "noun", "thin of hair or plumage (fem. زَعْرَاء)", "tüyü ya da saçı seyrek (müennesi زَعْرَاء)", 6, "ز ع ر"),
 "arbad": G("أَرْبَد", "noun", "ash-coloured, dusky grey (fem. رَبْدَاء)", "kül rengi, boz (müennesi رَبْدَاء)", 6, "ر ب د"),
 # ---- verses 14–20 ----
 "bara-vie": G("بَارَى", "verb", "to vie with, to match another in what he does, trying to outdo him (Form III)", "biriyle yarışmak, üstün gelmeye çalışarak onun yaptığını yapmak (müfâale)", 6, "ب ر ي", form="III"),
 "najiya": G("نَاجِيَة", "noun", "a swift she-camel, fast in going (pl. نَاجِيَات; from نَجَا يَنْجُو, to go fast)", "yürüyüşte hızlı dişi deve (çoğ. نَاجِيَات; نَجَا يَنْجُو: hızlı gitti)", 6, "ن ج و", "نَاجِيَات"),
 "wazif": G("وَظِيف", "noun", "the shank of a beast's leg, from the pastern to the knee", "hayvanın bacağında bilekle diz arası, incik", 6, "و ظ ف"),
 "mawr": G("مَوْر", "noun", "a road, a beaten track", "yol, çiğnenmiş iz", 6, "م و ر"),
 "muabbad": G("مُعَبَّد", "noun", "made smooth, beaten down (of a road, v. 14); tamed and smeared with tar (of a camel, v. 53) — ism maf'ul of عَبَّدَ", "düzlenmiş, çiğnenmiş (yol, 14. beyit); uysallaştırılıp katranla sıvanmış (deve, 53. beyit) — عَبَّدَ'den ism-i mef'ûl", 6, "ع ب د"),
 "quff": G("قُفّ", "noun", "rough, raised ground short of a mountain (pl. قِفَاف)", "dağ olacak kadar yükselmeyen sert, yüksek arazi (çoğ. قِفَاف)", 6, "ق ف ف", "قِفَاف"),
 "shawl": G("شَوْل", "noun", "she-camels whose udders have dried and whose milk is little (sing. شَائِلَة)", "memeleri kurumuş, sütü azalmış dişi develer (tekili شَائِلَة)", 6, "ش و ل"),
 "irtaa": G("اِرْتَعَى", "verb", "to graze, to pasture (Form VIII)", "otlamak (iftiâl)", 6, "ر ع ي", form="VIII"),
 "hadiqa": G("حَدِيقَة", "noun", "a meadow whose edges rise and whose middle lies low; a walled garden (pl. حَدَائِق)", "kenarları yüksek, ortası çukur çayırlık; duvarla çevrili bahçe (çoğ. حَدَائِق)", 6, "ح د ق", "حَدَائِق"),
 "mawliyy": G("مَوْلِيّ", "noun", "watered by the second rain of the year (الوَلِيّ)", "yılın ikinci yağmurunu (الوَلِيّ) almış", 6, "و ل ي"),
 "aghyad": G("أَغْيَد", "noun", "soft, tender (fem. غَيْدَاء, pl. غِيد; a diptote)", "yumuşak, nazik (müennesi غَيْدَاء, çoğ. غِيد; gayr-i munsarif)", 6, "غ ي د"),
 "raa-return": G("رَاعَ", "verb", "to turn back, to return (رَاعَ يَرِيعُ رَيْعًا)", "geri dönmek (رَاعَ يَرِيعُ رَيْعًا)", 6, "ر ي ع", form="I"),
 "muhib": G("مُهِيب", "noun", "one who calls the camels to him (ism fa'il of أَهَابَ)", "develeri yanına çağıran (أَهَابَ'den ism-i fâil)", 6, "ه ي ب"),
 "khusla-lock": G("خُصْلَة", "noun", "a lock of hair, a tuft (pl. خُصَل)", "saç ya da kıl tutamı, püskül (çoğ. خُصَل)", 6, "خ ص ل", "خُصَل"),
 "aklaf": G("أَكْلَف", "noun", "dark red verging on black (a diptote)", "siyaha çalan koyu kızıl (gayr-i munsarif)", 6, "ك ل ف"),
 "mulbid": G("مُلْبِد", "noun", "with matted hair (ism fa'il of أَلْبَدَ)", "tüyü keçeleşmiş (أَلْبَدَ'den ism-i fâil)", 6, "ل ب د"),
 "madrahi": G("مَضْرَحِيّ", "noun", "a white vulture; also said: a great one", "ak akbaba; büyüğü olduğu da söylenir", 6),
 "takannafa": G("تَكَنَّفَ", "verb", "to flank, to be at the two sides of (Form V; from كَنَف, side)", "iki yanını kuşatmak (tefa''ul; كَنَف: yan)", 6, "ك ن ف", form="V"),
 "hifaf": G("حِفَاف", "noun", "the side of a thing (pl. أَحِفَّة)", "bir şeyin yanı (çoğ. أَحِفَّة)", 6, "ح ف ف", "أَحِفَّة"),
 "asib": G("عَسِيب", "noun", "the bone of the tail (pl. عُسُب); (elsewhere) a stripped palm-branch", "kuyruk kemiği (çoğ. عُسُب); (başka yerde) yaprağı soyulmuş hurma dalı", 6, "ع س ب", "عُسُب"),
 "misrad": G("مِسْرَد", "noun", "an awl (also مِسْرَاد; pl. مَسَارِد)", "biz (مِسْرَاد da denir; çoğ. مَسَارِد)", 6, "س ر د", "مَسَارِد"),
 "shann": G("شَنّ", "noun", "a worn-out waterskin (pl. شِنَان)", "eskimiş su tulumu (çoğ. شِنَان)", 6, "ش ن ن", "شِنَان"),
 "dhawin": G("ذَاوٍ", "noun", "withered, dried (ism fa'il of ذَوَى يَذْوِي; a manqus noun)", "solmuş, kurumuş (ذَوَى يَذْوِي'den ism-i fâil; menkûs isim)", 6, "ذ و ي"),
 "mujaddad": G("مُجَدَّد", "noun", "cut off — of an udder whose milk has been cut off", "kesilmiş — sütü kesilmiş meme", 6, "ج د د"),
 "nahd": G("نَحْض", "noun", "flesh", "et", 6, "ن ح ض"),
 "tayy-fold": G("طَيّ", "noun", "folding; the lining of a well with stones — here: close-set, as if stone-cased", "katlama; kuyuyu taşla örme — burada: taş örgü gibi sıkı dizilmiş", 6, "ط و ي"),
 "mahala": G("مَحَالَة", "noun", "a vertebra of the back (pl. مَحَال)", "sırt omuru (çoğ. مَحَال)", 6, None, "مَحَال"),
 "haniyya": G("حَنِيَّة", "noun", "a bow (pl. حَنِيّ — also read حُنِيّ, حِنِيّ — and حَنَايَا)", "yay (çoğ. حَنِيّ — حُنِيّ, حِنِيّ diye de okunur — ve حَنَايَا)", 6, "ح ن و", "حَنِيّ"),
 "khilf-rib": G("خِلْف", "noun", "the end of a rib, the short rib (pl. خُلُوف)", "kaburga ucu, kısa kaburga (çoğ. خُلُوف)", 6, "خ ل ف", "خُلُوف"),
 "jiran": G("جِرَان", "noun", "the under-side of a camel's neck (pl. أَجْرِنَة)", "devenin boynunun alt yüzü (çoğ. أَجْرِنَة)", 6, "ج ر ن", "أَجْرِنَة"),
 "lazza": G("لَزَّ", "verb", "to join fast, to bind one thing close to another (لَزَّ يَلُزُّ)", "sıkıca bitiştirmek, bir şeyi ötekine kenetlemek (لَزَّ يَلُزُّ)", 6, "ل ز ز", form="I"),
 "day": G("دَأْي", "noun", "the vertebrae of the back and neck (sing. دَأْيَة)", "sırt ve boyun omurları (tekili دَأْيَة)", 6, "د أ ي"),
 # ---- verses 21–27 ----
 "kinas": G("كِنَاس", "noun", "the lair a wild beast makes at the foot of a tree (pl. كُنُس)", "yabani hayvanın bir ağacın dibinde edindiği in (çoğ. كُنُس)", 6, "ك ن س", "كُنُس"),
 "dala-tree": G("ضَالَة", "noun", "a wild lote-tree (coll. ضَال)", "yabani sedir ağacı (cins ismi ضَال)", 6, "ض ي ل"),
 "kanafa": G("كَنَفَ", "verb", "to be at the side of, to flank (كَنَفَ يَكْنُفُ)", "bir şeyin yanında olmak, yanından kuşatmak (كَنَفَ يَكْنُفُ)", 6, "ك ن ف", form="I"),
 "atr": G("أَطْر", "noun", "bending, curving (masdar of أَطَرَ)", "eğme, bükme (أَطَرَ'nin masdarı)", 6, "أ ط ر"),
 "aftal": G("أَفْتَل", "noun", "set apart, as if twisted away (of a camel's elbow); strong (fem. فَتْلَاء)", "(devenin dirseği için) sanki bükülerek ayrılmış; güçlü (müennesi فَتْلَاء)", 6, "ف ت ل"),
 "salm-bucket": G("سَلْم", "noun", "a bucket with a single handle, such as water-carriers use", "sucuların kullandığı türden tek kulplu kova", 6, "س ل م"),
 "dalij": G("دَالِج", "noun", "one who carries the bucket from the well to the trough", "kovayı kuyudan havuza taşıyan", 6, "د ل ج"),
 "mutashaddid": G("مُتَشَدِّد", "noun", "sturdy, strong (v. 22); tight-fisted, hard in meanness (v. 65) — ism fa'il of تَشَدَّدَ", "sağlam, güçlü (22. beyit); eli sıkı, cimriliği katı (65. beyit) — تَشَدَّدَ'den ism-i fâil", 6, "ش د د"),
 "qantara": G("قَنْطَرَة", "noun", "an arched bridge (pl. قَنَاطِر)", "kemerli köprü (çoğ. قَنَاطِر)", 6, None, "قَنَاطِر"),
 "rumi-greek": G("رُومِيّ", "noun", "a Greek, a man of the Rūm (a nisba)", "Rum, Rumlardan bir adam (nisbe)", 6, "ر و م"),
 "iktanafa": G("اِكْتَنَفَ", "verb", "to close in on every side, to wall about (Form VIII)", "her yandan kuşatmak, etrafını çevirmek (iftiâl)", 6, "ك ن ف", form="VIII"),
 "shada-raise": G("شَادَ", "verb", "to raise (a building) high; to plaster with gypsum (شَادَ يَشِيدُ)", "(binayı) yükseltmek; alçıyla sıvamak (شَادَ يَشِيدُ)", 6, "ش ي د", form="I"),
 "qarmad": G("قَرْمَد", "noun", "baked brick; also said: lime-mortar", "pişmiş tuğla; kireç harcı olduğu da söylenir", 6),
 "suhabiyya": G("صُهَابِيّ", "noun", "reddish, of a colour verging on red (fem. صُهَابِيَّة)", "kızıla çalan (müennesi صُهَابِيَّة)", 6, "ص ه ب"),
 "uthnun": G("عُثْنُون", "noun", "the hairs beneath a camel's lower jaw; a beard", "devenin alt çenesinin altındaki kıllar; sakal", 6),
 "mujad": G("مُوجَد", "noun", "made strong, strongly built (also مُؤْجَد)", "güçlendirilmiş, sağlam yapılı (مُؤْجَد da denir)", 6, "أ ج د"),
 "qara-back": G("قَرًا", "noun", "the back (pl. أَقْرَاء)", "sırt (çoğ. أَقْرَاء)", 6, "ق ر و", "أَقْرَاء"),
 "wakhd": G("وَخْد", "noun", "a quick ambling pace (وَخَدَ يَخِدُ)", "hızlı, rahvan bir yürüyüş (وَخَدَ يَخِدُ)", 6, "و خ د"),
 "mawwar": G("مَوَّار", "noun", "swinging freely to and fro (intensive of مَائِر)", "rahatça gidip gelen (مَائِر'in mübalağası)", 6, "م و ر"),
 "amarra-twist": G("أَمَرَّ", "verb", "to twist (a rope) firm (Form IV)", "(ipi) sıkıca bükmek (if'âl)", 6, "م ر ر", form="IV"),
 "fatl": G("فَتْل", "noun", "twisting (masdar of فَتَلَ)", "bükme (فَتَلَ'nin masdarı)", 6, "ف ت ل"),
 "shazr": G("شَزْر", "noun", "a twist turned away from the chest; (of a look) sidelong", "göğüsten dışa doğru çevrilen büküm; (bakış için) yan", 6, "ش ز ر"),
 "ajnaha": G("أَجْنَحَ", "verb", "to make to slant, to set leaning (Form IV)", "meylettirmek, eğik koymak (if'âl)", 6, "ج ن ح", form="IV"),
 "saqif": G("سَقِيف", "noun", "a roof (= سَقْف); slabs of stone", "çatı (= سَقْف); taş levhalar", 6, "س ق ف"),
 "musannad": G("مُسَنَّد", "noun", "with its parts leaning one upon another (ism maf'ul of سَنَّدَ)", "parçaları birbirine dayandırılmış (سَنَّدَ'den ism-i mef'ûl)", 6, "س ن د"),
 "januh": G("جَنُوح", "noun", "much given to swerving, leaning to one side for spirit (intensive)", "coşkusundan çok meyleden, bir yana yatan (mübalağa)", 6, "ج ن ح"),
 "difaq": G("دِفَاق", "noun", "rushing on, going as fast as can be", "boşanırcasına atılan, son derece hızlı giden", 6, "د ف ق"),
 "andal": G("عَنْدَل", "noun", "big of head (of a she-camel)", "iri başlı (dişi deve)", 6),
 "afraa": G("أَفْرَعَ", "verb", "to raise high, to make to rise above (Form IV)", "yükseltmek, üstüne çıkarmak (if'âl)", 6, "ف ر ع", form="IV"),
 "katif": G("كَتِف", "noun", "the shoulder, the shoulder-blade (pl. أَكْتَاف)", "omuz, kürek kemiği (çoğ. أَكْتَاف)", 6, "ك ت ف", "أَكْتَاف"),
 "muala": G("مُعَالًى", "noun", "raised high (ism maf'ul of عَالَى)", "yükseltilmiş (عَالَى'den ism-i mef'ûl)", 6, "ع ل و"),
 "musaad": G("مُصَعَّد", "noun", "lifted up, raised (ism maf'ul of صَعَّدَ)", "yukarı kaldırılmış (صَعَّدَ'den ism-i mef'ûl)", 6, "ص ع د"),
 "alb-mark": G("عَلْب", "noun", "a mark, a trace pressed in (pl. عُلُوب)", "basılarak kalmış iz (çoğ. عُلُوب)", 6, "ع ل ب", "عُلُوب"),
 "nis": G("نِسْع", "noun", "a broad strap shaped like a rein, for binding loads (pl. أَنْسَاع, نُسُوع)", "yük bağlamaya yarayan, dizgine benzer geniş kayış (çoğ. أَنْسَاع, نُسُوع)", 6, "ن س ع", "أَنْسَاع"),
 "dayat": G("دَأْيَة", "noun", "a vertebra (pl. دَأَيَات)", "omur (çoğ. دَأَيَات)", 6, "د أ ي", "دَأَيَات"),
 "mawrid": G("مَوْرِد", "noun", "a watering place, water one comes down to (pl. مَوَارِد)", "suvat, başına gelinen su (çoğ. مَوَارِد)", 6, "و ر د", "مَوَارِد"),
 "khalqa": G("خَلْقَاء", "noun", "smooth (of a rock; fem. of أَخْلَق; a diptote)", "düz, kaygan (kaya için; أَخْلَق'in müennesi; gayr-i munsarif)", 6, "خ ل ق"),
 # ---- verses 28–33 ----
 "talaqa": G("تَلَاقَى", "verb", "to meet one another, to come together (Form VI)", "birbiriyle buluşmak, bir araya gelmek (tefâul)", 6, "ل ق ي", form="VI"),
 "baniqa": G("بَنِيقَة", "noun", "a gusset, a piece let into a garment to widen it (pl. بَنَائِق)", "peş, genişletmek için elbiseye eklenen parça (çoğ. بَنَائِق)", 6, "ب ن ق", "بَنَائِق"),
 "muqaddad": G("مُقَدَّد", "noun", "slit, cut into strips (ism maf'ul of قَدَّدَ)", "yarılmış, şeritlere kesilmiş (قَدَّدَ'den ism-i mef'ûl)", 6, "ق د د"),
 "atla": G("أَتْلَع", "noun", "long of neck (fem. تَلْعَاء; a diptote)", "boynu uzun (müennesi تَلْعَاء; gayr-i munsarif)", 6, "ت ل ع"),
 "nahhad": G("نَهَّاض", "noun", "quick to rise (intensive of نَاهِض)", "çabuk kalkan (نَاهِض'in mübalağası)", 6, "ن ه ض"),
 "saad-ii": G("صَعَّدَ", "verb", "to go up; with بِ, to lift up (Form II)", "yukarı çıkmak; بِ ile: yukarı kaldırmak (tef'îl)", 6, "ص ع د", form="II"),
 "sukkan": G("سُكَّان", "noun", "the rudder, the tail of a ship", "dümen, geminin kuyruğu", 6, "س ك ن"),
 "busi": G("بُوصِيّ", "noun", "a kind of boat", "bir tür gemi, tekne", 6),
 "musid": G("مُصْعِد", "noun", "going up, going upstream (ism fa'il of أَصْعَدَ)", "yukarı, akıntıya karşı giden (أَصْعَدَ'den ism-i fâil)", 6, "ص ع د"),
 "jumjuma": G("جُمْجُمَة", "noun", "the skull (pl. جَمَاجِم)", "kafatası (çoğ. جَمَاجِم)", 6, None, "جَمَاجِم"),
 "alat": G("عَلَاة", "noun", "an anvil", "örs", 6, "ع ل و"),
 "multaqa": G("مُلْتَقًى", "noun", "a place of meeting, a joint", "birleşme yeri", 6, "ل ق ي"),
 "mibrad": G("مِبْرَد", "noun", "a file (the tool)", "eğe (alet)", 6, "ب ر د"),
 "qirtas": G("قِرْطَاس", "noun", "parchment, a sheet to write on (pl. قَرَاطِيس)", "yazı kâğıdı, parşömen (çoğ. قَرَاطِيس)", 6, None, "قَرَاطِيس"),
 "shaamin": G("شَآمٍ", "noun", "Syrian, a man of al-Shaʾm (nisba with its yāʾ lightened: الشَّآمِي)", "Şamlı, Şam ehlinden (yâsı hafifletilmiş nisbe: الشَّآمِي)", 6, "ش أ م"),
 "mishfar": G("مِشْفَر", "noun", "a camel's lip (pl. مَشَافِر)", "devenin dudağı (çoğ. مَشَافِر)", 6, "ش ف ر", "مَشَافِر"),
 "qidd": G("قِدّ", "noun", "a strip cut lengthwise; the cut (of leather)", "boyuna kesilmiş şerit; (derinin) kesimi", 6, "ق د د"),
 "harrada": G("حَرَّدَ", "verb", "to cut unevenly, raggedly (Form II)", "çarpık, düzensiz kesmek (tef'îl)", 6, "ح ر د", form="II"),
 "mawiyya": G("مَاوِيَّة", "noun", "a mirror", "ayna", 6),
 "istakanna": G("اِسْتَكَنَّ", "verb", "to take shelter, to be sheltered (Form X)", "barınmak, sığınmak (istif'âl)", 6, "ك ن ن", form="X"),
 "hijaj": G("حِجَاج", "noun", "the brow-bone, on which the eyebrow grows (pl. أَحِجَّة)", "kaşın bittiği kemik (çoğ. أَحِجَّة)", 6, "ح ج ج", "أَحِجَّة"),
 "qalt": G("قَلْت", "noun", "a hollow in rock where water stands (pl. قِلَات)", "kayada suyun biriktiği çukur (çoğ. قِلَات)", 6, "ق ل ت", "قِلَات"),
 "tahur": G("طَحُور", "noun", "that casts out much (intensive of طَاحِر)", "çok atan, dışarı iten (طَاحِر'in mübalağası)", 6, "ط ح ر"),
 "uwwar": G("عُوَّار", "noun", "a mote in the eye (= قَذًى; pl. عَوَاوِير)", "gözdeki çöp (= قَذًى; çoğ. عَوَاوِير)", 6, "ع و ر"),
 "makhula": G("مَكْحُول", "noun", "painted with kohl, kohl-dark (fem. مَكْحُولَة)", "sürmeli (müennesi مَكْحُولَة)", 6, "ك ح ل"),
 "madhur": G("مَذْعُور", "noun", "startled, frightened (ism maf'ul of ذَعَرَ)", "ürkütülmüş, korkutulmuş (ذَعَرَ'den ism-i mef'ûl)", 6, "ذ ع ر"),
 "farqad": G("فَرْقَد", "noun", "the calf of a wild cow (pl. فَرَاقِد)", "yaban sığırının yavrusu (çoğ. فَرَاقِد)", 6, None, "فَرَاقِد"),
 # ---- verses 34–39 ----
 "tawajjus": G("تَوَجُّس", "noun", "listening warily (masdar of تَوَجَّسَ)", "tetikte kulak kabartma (تَوَجَّسَ'in masdarı)", 6, "و ج س"),
 "hajs": G("هَجْس", "noun", "a faint stir, a movement", "hafif kıpırtı, hareket", 6, "ه ج س"),
 "munaddid": G("مُنَدِّد", "noun", "loud, raising the voice (ism fa'il of نَدَّدَ)", "yüksek sesli, sesini yükselten (نَدَّدَ'den ism-i fâil)", 6, "ن د د"),
 "muallal": G("مُؤَلَّل", "noun", "sharpened to a point like a spear-head (ism maf'ul of أَلَّلَ)", "mızrak ucu gibi sivriltilmiş (أَلَّلَ'den ism-i mef'ûl)", 6, "أ ل ل"),
 "samia-ear": G("سَامِعَة", "noun", "an ear (lit. «the hearing one»)", "kulak (lafzen «işiten»)", 6, "س م ع"),
 "arwa": G("أَرْوَع", "noun", "quick to start at everything for keenness (of a heart); (of a man) striking (a diptote)", "keskinliğinden her şeye irkilen (kalp); (insan için) heybetli (gayr-i munsarif)", 6, "ر و ع"),
 "nabbad": G("نَبَّاض", "noun", "much beating, ever moving (intensive of نَابِض)", "çok çarpan, hep hareket eden (نَابِض'in mübalağası)", 6, "ن ب ض"),
 "ahadhdh": G("أَحَذّ", "noun", "light and quick (a diptote)", "hafif ve çabuk (gayr-i munsarif)", 6, "ح ذ ذ"),
 "mulamlam": G("مُلَمْلَم", "noun", "compact, gathered together, hard and firm", "derli toplu, sert ve sağlam", 6, "ل م م"),
 "mirdat": G("مِرْدَاة", "noun", "a rock with which rocks are broken", "kayaların kırıldığı kaya, taş kırıcı", 6, "ر د ي"),
 "safih": G("صَفِيح", "noun", "broad flat stones, slabs (sing. صَفِيحَة; also pl. صَفَائِح)", "geniş yassı taşlar, levhalar (tekili صَفِيحَة; çoğ. صَفَائِح da)", 6, "ص ف ح"),
 "musammad": G("مُصَمَّد", "noun", "firm, made fast (v. 36); much resorted to (v. 47; from الصَّمْد, resorting to)", "sağlam, sıkıca bağlanmış (36. beyit); kendisine çokça başvurulan (47. beyit; الصَّمْد: yönelmek)", 6, "ص م د"),
 "alam-split": G("أَعْلَم", "noun", "split in the upper lip (a diptote; distinct from أَعْلَم «more knowing»)", "üst dudağı yarık (gayr-i munsarif; «daha bilgili» anlamındaki أَعْلَم'den ayrıdır)", 6, "ع ل م"),
 "makhrut": G("مَخْرُوت", "noun", "pierced (from خَرْت, a hole)", "delinmiş (خَرْت: delik)", 6, "خ ر ت"),
 "marin": G("مَارِن", "noun", "the soft part of the nose", "burnun yumuşak kısmı", 6, "م ر ن"),
 "arqala": G("أَرْقَلَ", "verb", "to go at a pace between walking and running, to race (Form IV)", "yürüyüşle koşu arası bir hızla gitmek (if'âl)", 6, "ر ق ل", form="IV"),
 "malwiyy": G("مَلْوِيّ", "noun", "twisted (ism maf'ul of لَوَى)", "bükülmüş (لَوَى'den ism-i mef'ûl)", 6, "ل و ي"),
 "muhsad": G("مُحْصَد", "noun", "firmly plaited, made fast (ism maf'ul of أَحْصَدَ)", "sıkıca örülmüş, sağlamlaştırılmış (أَحْصَدَ'den ism-i mef'ûl)", 6, "ح ص د"),
 "sama-vie": G("سَامَى", "verb", "to vie with in height (Form III)", "yükseklikte yarışmak (müfâale)", 6, "س م و", form="III"),
 "wasit": G("وَاسِط", "noun", "the front-piece of a camel-saddle, like the pommel of a horse's saddle", "deve semerinin ön kaşı, eyerin kaşı gibi", 6, "و س ط"),
 "ama-swim": G("عَامَ", "verb", "to swim (عَامَ يَعُومُ عَوْمًا)", "yüzmek (عَامَ يَعُومُ عَوْمًا)", 6, "ع و م", form="I"),
 "dab-arm": G("ضَبْع", "noun", "the upper arm (pl. أَضْبَاع)", "pazı, üst kol (çoğ. أَضْبَاع)", 6, "ض ب ع", "أَضْبَاع"),
 "naja-speed": G("نَجَاء", "noun", "going fast, speed", "hızla gitmek, sürat", 6, "ن ج و"),
 "khafaydad": G("خَفَيْدَد", "noun", "the male ostrich", "erkek devekuşu", 6, "خ ف د"),
 # ---- verses 40–47 ----
 "fada": G("فَدَى", "verb", "to ransom (فَدَى يَفْدِي)", "fidye verip kurtarmak (فَدَى يَفْدِي)", 6, "ف د ي", form="I"),
 "iftada": G("اِفْتَدَى", "verb", "to ransom oneself, to save oneself (Form VIII)", "kendini fidyeyle kurtarmak (iftiâl)", 6, "ف د ي", form="VIII"),
 "musab": G("مُصَاب", "noun", "struck down, lost (ism maf'ul of أَصَابَ)", "musibete uğramış, helâk olmuş (أَصَابَ'den ism-i mef'ûl)", 6, "ص و ب"),
 "marsad": G("مَرْصَد", "noun", "a road where men lie in wait (pl. مَرَاصِد)", "pusu kurulan yol (çoğ. مَرَاصِد)", 6, "ر ص د", "مَرَاصِد"),
 "kasila": G("كَسِلَ", "verb", "to be slow, to be slack (كَسِلَ يَكْسَلُ)", "tembel davranmak, gevşemek (كَسِلَ يَكْسَلُ)", 6, "ك س ل", form="I"),
 "taballada": G("تَبَلَّدَ", "verb", "to stand at a loss, to falter, to slacken (Form V)", "şaşırıp kalmak, duraksamak, gevşemek (tefa''ul)", 6, "ب ل د", form="V"),
 "qati-whip": G("قَطِيع", "noun", "a whip; (elsewhere) a herd", "kamçı; (başka yerde) sürü", 6, "ق ط ع"),
 "ajdhama": G("أَجْذَمَ", "verb", "to speed up, to go fast (Form IV)", "hızlanmak, hızlı gitmek (if'âl)", 6, "ج ذ م", form="IV"),
 "khabba": G("خَبَّ", "verb", "to trot; (of a mirage) to quiver (خَبَّ يَخُبُّ خَبَبًا)", "tırıs gitmek; (serap için) titreşmek (خَبَّ يَخُبُّ خَبَبًا)", 6, "خ ب ب", form="I"),
 "aal-mirage": G("آل", "noun", "a mirage seen at either end of the day", "günün iki ucunda görülen serap", 6, "أ و ل"),
 "amaz": G("أَمْعَز", "noun", "stony ground, earth mixed with stones or gravel (pl. أَمَاعِز)", "taşlık arazi, taş ya da çakıl karışık toprak (çoğ. أَمَاعِز)", 6, "م ع ز", "أَمَاعِز"),
 "mutawaqqid": G("مُتَوَقِّد", "noun", "blazing (ism fa'il of تَوَقَّدَ)", "alev alev yanan (تَوَقَّدَ'den ism-i fâil)", 6, "و ق د"),
 "dhala-strut": G("ذَالَ", "verb", "to swagger, to sway proudly (ذَالَ يَذِيلُ)", "salınarak yürümek (ذَالَ يَذِيلُ)", 6, "ذ ي ل", form="I"),
 "walida-girl": G("وَلِيدَة", "noun", "a young girl; a slave-girl (pl. وَلَائِد)", "kız çocuk; câriye (çoğ. وَلَائِد)", 6, "و ل د", "وَلَائِد"),
 "sahl-cloth": G("سَحْل", "noun", "a white garment of cotton or the like", "pamuktan vb. beyaz elbise", 6, "س ح ل"),
 "mumaddad": G("مُمَدَّد", "noun", "drawn out, long (ism maf'ul of مَدَّدَ)", "uzatılmış, uzun (مَدَّدَ'den ism-i mef'ûl)", 6, "م د د"),
 "hallal": G("حَلَّال", "noun", "one who often alights, keeps to a place (intensive of حَالّ)", "çokça konan, bir yere yerleşen (حَالّ'ın mübalağası)", 6, "ح ل ل"),
 "tala": G("تَلْعَة", "noun", "ground above a water-course and below the mountains (pl. تِلَاع)", "sel yatağından yüksek, dağlardan alçak yer (çoğ. تِلَاع)", 6, "ت ل ع", "تِلَاع"),
 "istarfada": G("اِسْتَرْفَدَ", "verb", "to ask for help (Form X)", "yardım istemek (istif'âl)", 6, "ر ف د", form="X"),
 "arfada": G("أَرْفَدَ", "verb", "to help, to give aid (Form IV)", "yardım etmek (if'âl)", 6, "ر ف د", form="IV"),
 "iqtanasa": G("اِقْتَنَصَ", "verb", "to hunt, to catch (Form VIII)", "avlamak, yakalamak (iftiâl)", 6, "ق ن ص", form="VIII"),
 "hanut": G("حَانُوت", "noun", "a wine-seller's house, a shop (pl. حَوَانِيت)", "şarapçının evi, dükkân (çoğ. حَوَانِيت)", 6, None, "حَوَانِيت"),
 "istada": G("اِصْطَادَ", "verb", "to hunt, to catch (Form VIII)", "avlamak, yakalamak (iftiâl)", 6, "ص ي د", form="VIII"),
 # ---- verses 48–54 ----
 "nadman": G("نَدْمَان", "noun", "a boon companion, a drinking-fellow (pl. نَدَامَى)", "içki arkadaşı, nedim (çoğ. نَدَامَى)", 6, "ن د م", "نَدَامَى"),
 "qayna": G("قَيْنَة", "noun", "a singing slave-girl (pl. قَيْنَات, قِيَان)", "şarkıcı câriye (çoğ. قَيْنَات, قِيَان)", 6, "ق ي ن", "قِيَان"),
 "mujsad": G("مُجْسَد", "noun", "a robe dyed with saffron (الجِسَاد); a robe steeped in dye", "safranla (الجِسَاد) boyanmış elbise; boyası doymuş elbise", 6, "ج س د"),
 "rahib": G("رَحِيب", "noun", "wide, ample", "geniş", 6, "ر ح ب"),
 "qitab": G("قِطَاب", "noun", "قِطَاب الجَيْب: the opening of a garment through which the head goes", "قِطَاب الجَيْب: elbisenin başın geçtiği yaka ağzı", 6, "ق ط ب"),
 "jayb": G("جَيْب", "noun", "the opening of a garment at the breast, the collar (pl. جُيُوب)", "elbisenin göğüs açıklığı, yaka (çoğ. جُيُوب)", 6, "ج ي ب", "جُيُوب"),
 "rafiq": G("رَفِيق", "noun", "gentle, soft in manner (fem. رَفِيقَة)", "yumuşak huylu, nazik (müennesi رَفِيقَة)", 6, "ر ف ق"),
 "jass": G("جَسّ", "noun", "touching, feeling with the hand", "elle dokunma, yoklama", 6, "ج س س"),
 "badd": G("بَضّ", "noun", "soft of body, fine of skin (fem. بَضَّة)", "bedeni yumuşak, teni ince (müennesi بَضَّة)", 6, "ب ض ض"),
 "mutajarrad": G("مُتَجَرَّد", "noun", "where one is bared, the uncovered part of the body", "açılan yer, bedenin açık kalan kısmı", 6, "ج ر د"),
 "asmaa": G("أَسْمَعَ", "verb", "to make (someone) hear; أَسْمِعِينَا: sing to us (Form IV)", "işittirmek; أَسْمِعِينَا: bize şarkı söyle (if'âl)", 6, "س م ع", form="IV"),
 "risl": G("رِسْل", "noun", "ease, a leisurely pace — عَلَى رِسْلِهَا: at her leisure", "ağırlık, acelesizlik — عَلَى رِسْلِهَا: ağır ağır", 6, "ر س ل"),
 "matruqa": G("مَطْرُوق", "noun", "languid, with a weakness in one (fem. مَطْرُوقَة)", "gevşek, baygın (müennesi مَطْرُوقَة)", 6, "ط ر ق"),
 "tashaddada": G("تَشَدَّدَ", "verb", "to strain, to be forceful (Form V)", "zorlamak, sertleşmek (tefa''ul)", 6, "ش د د", form="V"),
 "rajja": G("رَجَّعَ", "verb", "to trill, to turn the voice over (Form II)", "sesi titretip yinelemek (tef'îl)", 6, "ر ج ع", form="II"),
 "tajawub": G("تَجَاوُب", "noun", "answering one another (masdar of تَجَاوَبَ)", "birbirine karşılık verme (تَجَاوَبَ'ün masdarı)", 6, "ج و ب"),
 "zir": G("ظِئْر", "noun", "a she-camel (or woman) that has a young one; a nurse (pl. أَظْآر)", "yavrusu olan dişi deve (ya da kadın); sütanne (çoğ. أَظْآر)", 6, "ظ أ ر", "أَظْآر"),
 "ruba": G("رُبَع", "noun", "a camel-calf born at the start of the foaling season (pl. رِبَاع)", "doğum mevsiminin başında doğan deve yavrusu (çoğ. رِبَاع)", 6, "ر ب ع"),
 "radin": G("رَدٍ", "noun", "perishing, dead (from رَدِيَ يَرْدَى)", "helâk olan, ölü (رَدِيَ يَرْدَى'dan)", 6, "ر د ي"),
 "tashrab": G("تَشْرَاب", "noun", "drinking, much drinking (a masdar on تَفْعَال)", "içmek, çok içmek («تَفْعَال» vezninde masdar)", 6, "ش ر ب"),
 "tarif-wealth": G("طَرِيف", "noun", "newly gained wealth (also طَارِف)", "yeni kazanılmış mal (طَارِف da denir)", 6, "ط ر ف"),
 "mutlad": G("مُتْلَد", "noun", "old, inherited wealth (also تَلِيد, تِلَاد)", "eski, miras kalmış mal (تَلِيد, تِلَاد da denir)", 6, "ت ل د"),
 "tahama": G("تَحَامَى", "verb", "to shun, to keep away from (Form VI)", "kaçınmak, uzak durmak (tefâul)", 6, "ح م ي", form="VI"),
 "ghabra": G("غَبْرَاء", "noun", "the dusty one — the earth (fem. of أَغْبَر; a diptote); بَنُو غَبْرَاء: the poor", "tozlu olan — yeryüzü (أَغْبَر'in müennesi; gayr-i munsarif); بَنُو غَبْرَاء: yoksullar", 6, "غ ب ر"),
 "tiraf": G("طِرَاف", "noun", "a tent of tanned hide (pl. طُرُوف)", "deriden çadır (çoğ. طُرُوف)", 6, "ط ر ف"),
 # ---- verses 55–61 ----
 "laim": G("لَائِم", "noun", "one who blames, a reproacher (ism fa'il of لَامَ)", "kınayan, ayıplayan (لَامَ'dan ism-i fâil)", 6, "ل و م"),
 "mukhlid": G("مُخْلِد", "noun", "one who makes (another) live for ever (ism fa'il of أَخْلَدَ)", "(birini) ebedî kılan (أَخْلَدَ'den ism-i fâil)", 6, "خ ل د"),
 "istaa": G("اِسْطَاعَ", "verb", "to be able (اِسْطَاعَ يَسْطِيعُ — a dialect form of اِسْتَطَاعَ, its ta dropped; Form X by its root)", "güç yetirmek (اِسْطَاعَ يَسْطِيعُ — tâ'sı düşmüş, اِسْتَطَاعَ'ın lehçe şekli; kökü bakımından istif'âl)", 6, "ط و ع", form="X"),
 "hafala": G("حَفَلَ", "verb", "to care, to mind (حَفَلَ يَحْفِلُ)", "aldırmak, umursamak (حَفَلَ يَحْفِلُ)", 6, "ح ف ل", form="I"),
 "adhila": G("عَاذِلَة", "noun", "a woman who blames, a reproacher (pl. عَاذِلَات, عَوَاذِل)", "kınayan kadın (çoğ. عَاذِلَات, عَوَاذِل)", 6, "ع ذ ل", "عَوَاذِل"),
 "sharba": G("شَرْبَة", "noun", "a draught, a single drink", "bir yudum, bir içim", 6, "ش ر ب"),
 "azbada": G("أَزْبَدَ", "verb", "to foam, to froth (Form IV)", "köpürmek (if'âl)", 6, "ز ب د", form="IV"),
 "karr-wheel": G("كَرّ", "noun", "wheeling round to charge again (masdar of كَرَّ)", "geri dönüp yeniden saldırma (كَرَّ'nin masdarı)", 6, "ك ر ر"),
 "muhannab": G("مُحَنَّب", "noun", "bowed in the foreleg (of a horse — a praised trait)", "ön ayağında eğrilik olan (at için övülen bir vasıf)", 6, "ح ن ب"),
 "sid-wolf": G("سِيد", "noun", "a wolf (pl. سِيدَان)", "kurt (çoğ. سِيدَان)", 6, "س ي د"),
 "ghada": G("غَضًا", "noun", "ghaḍā, a desert tree of the tamarisk kind", "ğadâ, ılgın türünden bir çöl ağacı", 6, "غ ض ي"),
 "mutawarrid": G("مُتَوَرِّد", "noun", "going down to water (ism fa'il of تَوَرَّدَ)", "suya inen (تَوَرَّدَ'den ism-i fâil)", 6, "و ر د"),
 "dajn": G("دَجْن", "noun", "clouds covering the sky; a cloudy day", "göğü örten bulutlar; bulutlu gün", 6, "د ج ن"),
 "bahkana": G("بَهْكَنَة", "noun", "a woman fair of form, full and soft", "yaratılışı güzel, dolgun ve yumuşak kadın", 6),
 "muammad": G("مُعَمَّد", "noun", "raised on poles (ism maf'ul of عَمَّدَ)", "direklerle yükseltilmiş (عَمَّدَ'den ism-i mef'ûl)", 6, "ع م د"),
 "bura": G("بُرَة", "noun", "a ring set in a camel's nose (pl. بُرًى, بُرَات, بُرُونَ / بُرِينَ)", "devenin burnuna takılan halka (çoğ. بُرًى, بُرَات, بُرُونَ / بُرِينَ)", 6, "ب ر و"),
 "dumluj": G("دُمْلُج", "noun", "an armlet worn on the upper arm (pl. دَمَالِيج)", "pazıbent (çoğ. دَمَالِيج)", 6, None, "دَمَالِيج"),
 "ushar": G("عُشَر", "noun", "ʿushar, a large-leaved desert shrub", "uşar, iri yapraklı bir çöl çalısı", 6, "ع ش ر"),
 "khirwa": G("خِرْوَع", "noun", "the castor-oil plant", "kene otu (hint yağı bitkisi)", 6),
 "khaddada": G("خَضَّدَ", "verb", "to lop (a tree) of its boughs and leaves (Form II)", "(ağacın) dallarını, yapraklarını budamak (tef'îl)", 6, "خ ض د", form="II"),
 # ---- verses 62–67 ----
 "rawwa": G("رَوَّى", "verb", "to give (one) drink to the full, to slake (Form II)", "kana kana içirmek, susuzluğunu gidermek (tef'îl)", 6, "ر و ي", form="II"),
 "sadin": G("صَدٍ", "noun", "thirsty (a manqus: الصَّدِي)", "susuz (menkûs: الصَّدِي)", 6, "ص د ي"),
 "nahham": G("نَحَّام", "noun", "greedy to gather and to withhold", "toplamaya ve vermemeye hırslı", 6, "ن ح م"),
 "ghawiyy": G("غَوِيّ", "noun", "one gone astray, a wastrel", "yoldan çıkmış, sapkın", 6, "غ و ي"),
 "batala": G("بَطَالَة", "noun", "idle folly, idleness", "boş iş, aylaklık", 6, "ب ط ل"),
 "juthwa": G("جُثْوَة", "noun", "a heap, a mound of earth (pl. جُثًى)", "yığın, toprak tümseği (çoğ. جُثًى)", 6, "ج ث و"),
 "itama": G("اِعْتَامَ", "verb", "to choose out, to pick the best (Form VIII)", "seçip ayırmak, en iyisini almak (iftiâl)", 6, "ع ي م", form="VIII"),
 "aqila": G("عَقِيلَة", "noun", "the choicest of a thing — of wealth or of women (pl. عَقَائِل)", "bir şeyin en seçkini — malın ya da kadınların (çoğ. عَقَائِل)", 6, "ع ق ل", "عَقَائِل"),
 "tiwal": G("طِوَل", "noun", "a long tether let out for a grazing beast", "otlayan hayvana uzatılan uzun ip", 6, "ط و ل"),
 "murkha": G("مُرْخًى", "noun", "let loose, let out (ism maf'ul of أَرْخَى)", "salıverilmiş, gevşetilmiş (أَرْخَى'den ism-i mef'ûl)", 6, "ر خ و"),
 # ---- verses 68–73 ----
 "baada": G("بَعُدَ", "verb", "to be far, to keep away (بَعُدَ يَبْعُدُ)", "uzak olmak, uzak durmak (بَعُدَ يَبْعُدُ)", 6, "ب ع د", form="I"),
 "qurt-name": G("قُرْط", "propn", "Qurṭ — a man's name (here Qurṭ son of Maʿbad, of the poet's tribe)", "Kurt — erkek adı (burada şairin kabilesinden Kurt b. Ma'bed)", 6),
 "mabad-name": G("مَعْبَد", "propn", "Maʿbad — a man's name (here the poet's brother)", "Ma'bed — erkek adı (burada şairin kardeşi)", 6),
 "ayasa": G("أَيْأَسَ", "verb", "to make (one) despair (Form IV)", "ümitsizliğe düşürmek (if'âl)", 6, "ي أ س", form="IV"),
 "rams": G("رَمْس", "noun", "a grave; (first) burying", "kabir; (aslı) gömme", 6, "ر م س"),
 "mulhad": G("مُلْحَد", "noun", "laid in a burial niche (ism maf'ul of أَلْحَدَ)", "lahde konmuş (أَلْحَدَ'den ism-i mef'ûl)", 6, "ل ح د"),
 "nashada": G("نَشَدَ", "verb", "to search for (what is lost) (نَشَدَ يَنْشُدُ نِشْدَانًا)", "(kaybolanı) aramak (نَشَدَ يَنْشُدُ نِشْدَانًا)", 6, "ن ش د", form="I"),
 "aghfala": G("أَغْفَلَ", "verb", "to neglect, to leave unheeded (Form IV)", "ihmal etmek, gözden kaçırıp bırakmak (if'âl)", 6, "غ ف ل", form="IV"),
 "qurba": G("قُرْبَى", "noun", "kinship, nearness of blood", "akrabalık, kan yakınlığı", 6, "ق ر ب"),
 "nakitha": G("نَكِيثَة", "noun", "the utmost of effort, the limit of one's strength", "gayretin son derecesi, gücün son sınırı", 6, "ن ك ث"),
 "julla": G("جُلَّى", "noun", "a grave affair, a great matter (fem. of أَجَلّ; also جَلَّاء)", "büyük iş, önemli mesele (أَجَلّ'ın müennesi; جَلَّاء da denir)", 6, "ج ل ل"),
 "jahada": G("جَهَدَ", "verb", "to strive, to exert oneself to the utmost (جَهَدَ يَجْهَدُ)", "son derece çabalamak (جَهَدَ يَجْهَدُ)", 6, "ج ه د", form="I"),
 # ---- verses 74–79 ----
 "qadha": G("قَذْع", "noun", "foul speech (also قَذَع)", "çirkin söz (قَذَع da denir)", 6, "ق ذ ع"),
 "ird": G("عِرْض", "noun", "honour — that in a man which is praised or blamed (pl. أَعْرَاض)", "namus, şeref — insanın övülen ve yerilen yanı (çoğ. أَعْرَاض)", 6, "ع ر ض", "أَعْرَاض"),
 "tahaddud": G("تَهَدُّد", "noun", "threatening (= تَهْدِيد)", "tehdit (= تَهْدِيد)", 6, "ه د د"),
 "hija": G("هِجَاء", "noun", "lampooning, satire", "hiciv, yergi", 6, "ه ج و"),
 "shakat": G("شَكَاة", "noun", "complaint (= شَكْوَى, شِكَايَة)", "şikâyet (= شَكْوَى, شِكَايَة)", 6, "ش ك و"),
 "mutrad": G("مُطْرَد", "noun", "being driven out (= إِطْرَاد, a masdar)", "kovulma (= إِطْرَاد, masdar)", 6, "ط ر د"),
 "farraja": G("فَرَّجَ", "verb", "to ease, to clear away (a distress) (Form II)", "(sıkıntıyı) gidermek, açmak (tef'îl)", 6, "ف ر ج", form="II"),
 "anzara": G("أَنْظَرَ", "verb", "to grant respite, to give time (Form IV)", "mühlet vermek, süre tanımak (if'âl)", 6, "ن ظ ر", form="IV"),
 "khaniq": G("خَانِق", "noun", "one who chokes, throttles (ism fa'il of خَنَقَ)", "boğan, boğazını sıkan (خَنَقَ'ten ism-i fâil)", 6, "خ ن ق"),
 "muftadin": G("مُفْتَدٍ", "noun", "one ransoming himself (ism fa'il of اِفْتَدَى; a manqus)", "kendini fidyeyle kurtaran (اِفْتَدَى'den ism-i fâil; menkûs)", 6, "ف د ي"),
 "madada": G("مَضَاضَة", "noun", "a sting, a burning pain of grief and anger", "acı, hüzün ve öfkenin yakıcı sızısı", 6, "م ض ض"),
 "darghad": G("ضَرْغَد", "propn", "Ḍarghad — a mountain (al-Zawzanī); also said: a lava-field in Ghaṭafān", "Darğad — bir dağ (Zevzenî); Gatafân'da bir lav arazisi olduğu da söylenir", 6),
 # ---- verses 80–85 ----
 "qays-name": G("قَيْس", "propn", "Qays — a man's name (here Qays son of Khālid, a lord of the Arabs)", "Kays — erkek adı (burada Arap efendilerinden Kays b. Hâlid)", 6, "ق ي س"),
 "musawwad": G("مُسَوَّد", "noun", "made a lord (ism maf'ul of سَوَّدَ)", "efendi kılınmış (سَوَّدَ'den ism-i mef'ûl)", 6, "س و د"),
 "khashash": G("خَشَاش", "noun", "lean and nimble, one who slips quickly into affairs", "zayıf ve çevik, işlerin içine çabucak giren", 6, "خ ش ش"),
 "raqiq": G("رَقِيق", "noun", "thin, fine", "ince", 6, "ر ق ق"),
 "muntasir": G("مُنْتَصِر", "noun", "taking vengeance (ism fa'il of اِنْتَصَرَ)", "öç alan (اِنْتَصَرَ'den ism-i fâil)", 6, "ن ص ر"),
 "midad": G("مِعْضَد", "noun", "a blade for cutting trees, a chopper", "ağaç kesmeye yarayan bıçak, balta", 6, "ع ض د"),
 "inthana": G("اِنْثَنَى", "verb", "to turn back, to turn away (Form VII)", "geri dönmek, yüz çevirmek (infiâl)", 6, "ث ن ي", form="VII"),
 "dariba": G("ضَرِيبَة", "noun", "what is struck with the sword (pl. ضَرَائِب)", "kılıçla vurulan şey (çoğ. ضَرَائِب)", 6, "ض ر ب", "ضَرَائِب"),
 "qad-hasb": G("قَدْ", "noun", "enough (= حَسْب) — قَدِي, قَدْنِي: enough for me", "yeter (= حَسْب) — قَدِي, قَدْنِي: bana yeter", 6),
 # ---- verses 86–91 ----
 "mani": G("مَنِيع", "noun", "not to be overcome, unassailable", "yenilmez, ulaşılmaz", 6, "م ن ع"),
 "balla-seize": G("بَلَّ", "verb", "بَلَّ بِالشَّيْءِ: to get hold of a thing", "بَلَّ بِالشَّيْءِ: bir şeyi ele geçirmek", 6, "ب ل ل", form="I"),
 "bark": G("بَرْك", "noun", "a great herd of camels kneeling", "çökmüş çok sayıda deve", 6, "ب ر ك"),
 "hujud": G("هُجُود", "noun", "sleeping (pl. of هَاجِد)", "uyuyanlar (هَاجِد'in cem'i)", 6, "ه ج د"),
 "kahat": G("كَهَاة", "noun", "a big, fat she-camel", "iri, semiz dişi deve", 6, "ك ه و"),
 "khayf": G("خَيْف", "noun", "the skin of the udder (pl. أَخْيَاف)", "memenin derisi (çoğ. أَخْيَاف)", 6, "خ ي ف", "أَخْيَاف"),
 "julala": G("جُلَالَة", "noun", "a big, fat she-camel", "iri, semiz dişi deve", 6, "ج ل ل"),
 "wabil": G("وَبِيل", "noun", "a heavy staff, a cudgel", "kalın asa, sopa", 6, "و ب ل"),
 "yalandad": G("يَلَنْدَد", "noun", "fierce in quarrel (also أَلَنْدَد, أَلَدّ)", "kavgada çetin (أَلَنْدَد, أَلَدّ da denir)", 6, "ل د د"),
 "tarra": G("تَرَّ", "verb", "to fall off, to drop (of a limb cut) (تَرَّ يَتِرُّ / يَتُرُّ)", "(kesilen uzuv) düşmek (تَرَّ يَتِرُّ / يَتُرُّ)", 6, "ت ر ر", form="I"),
 "muyid": G("مُؤْيِد", "noun", "a dire calamity", "çetin felaket", 6, "أ ي د"),
 "mutaammid": G("مُتَعَمِّد", "noun", "deliberate, doing a thing on purpose (ism fa'il of تَعَمَّدَ)", "kasıtlı, bilerek yapan (تَعَمَّدَ'den ism-i fâil)", 6, "ع م د"),
 "qasi": G("قَاصٍ", "noun", "far, the farthest (ism fa'il of قَصَا; a manqus)", "uzak, en uzaktaki (قَصَا'dan ism-i fâil; menkûs)", 6, "ق ص و"),
 # ---- verses 92–97 ----
 "imtalla": G("اِمْتَلَّ", "verb", "to roast in hot ashes and embers (المَلَّة) (Form VIII)", "sıcak külde ve korda (المَلَّة) kızartmak (iftiâl)", 6, "م ل ل", form="VIII"),
 "huwar": G("حُوَار", "noun", "a camel's calf, the young of a she-camel", "deve yavrusu", 6, "ح و ر"),
 "sadif": G("سَدِيف", "noun", "the hump of a camel; cuts of the hump", "devenin hörgücü; hörgüç parçaları", 6, "س د ف"),
 "musarhad": G("مُسَرْهَد", "noun", "well fed, fattened", "iyi beslenmiş, semirtilmiş", 6),
 "naa-announce": G("نَعَى", "verb", "to announce a death, to spread the news of it (نَعَى يَنْعَى)", "ölüm haberini duyurmak (نَعَى يَنْعَى)", 6, "ن ع ي", form="I"),
 "ghana-avail": G("غَنَاء", "noun", "availing, sufficing, usefulness", "iş görme, yetme, fayda", 6, "غ ن ي"),
 "khana": G("خَنًا", "noun", "foulness, obscene speech", "çirkinlik, müstehcen söz", 6, "خ ن ي"),
 "jum-fist": G("جُمْع", "noun", "the closed hand, the fist (also جِمْع; pl. أَجْمَاع)", "kapalı el, yumruk (جِمْع da denir; çoğ. أَجْمَاع)", 6, "ج م ع", "أَجْمَاع"),
 "mulahhad": G("مُلَهَّد", "noun", "much pushed about with the fist (ism maf'ul of لَهَّدَ)", "yumrukla çokça itilip kakılmış (لَهَّدَ'den ism-i mef'ûl)", 6, "ل ه د"),
 "waghl": G("وَغْل", "noun", "weak; (borrowed) base, mean", "zayıf; (iğreti) alçak", 6, "و غ ل"),
 "mutawahhid": G("مُتَوَحِّد", "noun", "alone, without followers (ism fa'il of تَوَحَّدَ)", "yalnız, taraftarsız (تَوَحَّدَ'den ism-i fâil)", 6, "و ح د"),
 "mahtid": G("مَحْتِد", "noun", "root, origin, descent", "asıl, kök, soy", 6, "ح ت د"),
 # ---- verses 98–103 ----
 "ghumma": G("غُمَّة", "noun", "a cloud of gloom, a covering grief (= غَمّ; first, covering)", "kasvet, insanı örten keder (= غَمّ; aslı: örtmek)", 6, "غ م م"),
 "irak": G("عِرَاك", "noun", "fighting, battle (from العَرْك, rubbing)", "savaş, çarpışma (ovmak demek olan العَرْك'ten)", 6, "ع ر ك"),
 "hifaz": G("حِفَاظ", "noun", "guarding what must be guarded — one's ground, one's women, one's honour", "korunması gerekeni gözetmek — yurdu, haremi, namusu", 6, "ح ف ظ"),
 "itaraka": G("اِعْتَرَكَ", "verb", "to jostle, to grapple together (Form VIII)", "birbirine çarpışmak, boğuşmak (iftiâl)", 6, "ع ر ك", form="VIII"),
 "arada": G("أَرْعَدَ", "verb", "to make tremble; passive أُرْعِدَ: to quiver (Form IV)", "titretmek; meçhulü أُرْعِدَ: titremek (if'âl)", 6, "ر ع د", form="IV"),
 "madbuh": G("مَضْبُوح", "noun", "held to the fire till marked by it (ism maf'ul of ضَبَحَ)", "ateşte tutulup iz almış (ضَبَحَ'ten ism-i mef'ûl)", 6, "ض ب ح"),
 "hiwar": G("حِوَار", "noun", "the coming back of talk, a reply; here: how the arrow returns, win or lose", "sözün geri dönüşü, cevap; burada: okun kazanıp kaybederek dönüşü", 6, "ح و ر"),
 "mujmid": G("مُجْمِد", "noun", "one who never wins at the game of arrows (from الجُمُود)", "kumar okunda hiç kazanamayan (الجُمُود'dan)", 6, "ج م د"),
 "zawwada": G("زَوَّدَ", "verb", "to provision, to give one food for a journey (Form II)", "azık vermek, yol azığı sağlamak (tef'îl)", 6, "ز و د", form="II"),
 "batat": G("بَتَات", "noun", "a traveller's cloak and gear (pl. أَبِتَّة)", "yolcunun örtüsü ve takımı (çoğ. أَبِتَّة)", 6, "ب ت ت"),
 # ==== GLOSS ABOVE ====
}
# A lex key is GLOBAL, and other Muʿallaqāt are being authored at the same time: every NEW key of this package is given the
# suffix «-tf» when the package is cut, so that it cannot meet another package's key. In the tokens above and in NEW_GLOSS /
# NEW_VERBS the keys are written without it; a key that is NOT in NEW_GLOSS is a shelf key, reused by lemma identity.
SUF = "-tf"
for _s in S1 + list(VERSE.values()):
    for _t in _s["tokens"]:
        if _t["lex"] in NEW_GLOSS: _t["lex"] += SUF
        for _g in _t.get("segments", []):
            if _g["lex"] in NEW_GLOSS: _g["lex"] += SUF
NEW_GLOSS = {k + SUF: v for k, v in NEW_GLOSS.items()}
_lid = lambda x: "".join(c for c in unicodedata.normalize("NFD", x or "") if not unicodedata.combining(c))
for k in NEW_GLOSS:
    hit = [p for p in PREF if k in _G[p] and _lid(_G[p][k].get("lemma")) != _lid(NEW_GLOSS[k]["lemma"])]   # a sister package may hold the key with the SAME word
    assert not hit, (k, hit)

def _keys(sentences):
    u = set()
    for s in sentences:
        for t in s["tokens"]:
            u.add(t["lex"])
            for sg2 in t.get("segments", []): u.add(sg2["lex"])
    return u
used, used_all = _keys([s for S in CHAPS for s in S]), _keys(ALL_AUTHORED)
no_entry = [k for k in sorted(used_all) if k not in NEW_GLOSS and find_gloss(k) is None]
assert not no_entry, no_entry
GLOSS = {}
for k in sorted(used):
    GLOSS[k] = dict(NEW_GLOSS.get(k) or find_gloss(k))
unused_new = [k for k in NEW_GLOSS if k not in used_all]
assert not unused_new, unused_new
# same lemma and key as the shelf, but the gloss shown in THIS poem is the sense its verses use (after al-Zawzanī)
def REGLOSS(k, en, tr):
    assert k in used_all, k
    if k in GLOSS: GLOSS[k] = {**GLOSS[k], "gloss": {"en": en, "tr": tr}}
REGLOSS("hasab", "inherited honour, noble descent; (elsewhere) measure, accordance", "soydan gelen şeref, asalet; (başka yerde) ölçü, miktar")
REGLOSS("marthad", "Marthad — a man's name", "Mersed — erkek adı")
REGLOSS("bishr", "Bishr — a man's name", "Bişr — erkek adı")
REGLOSS("zahir", "the outer side, the back (of the hand); (elsewhere) manifest", "dış yüz, (elin) sırtı; (başka yerde) açık, zâhir")
REGLOSS("wuquf", "halting, standing — the plural of وَاقِف (as جُلُوس of جَالِس); also the masdar of وَقَفَ", "duranlar — وَاقِف'in cem'i (جَالِس–جُلُوس gibi); ayrıca وَقَفَ'nin masdarı")
REGLOSS("baqi", "what remains, the rest of a thing (ism fa'il of بَقِيَ)", "geri kalan, bir şeyin kalıntısı (بَقِيَ'den ism-i fâil)")
REGLOSS("hurr", "the pure, unmixed part of a thing; (elsewhere) free", "bir şeyin hâlisi, katışıksızı; (başka yerde) hür")
REGLOSS("tanawala", "to reach out for, to take with the hand (Form VI)", "uzanıp almak (tefâul)")
REGLOSS("raha-become", "to go or travel in the evening (رَاحَ يَرُوحُ); (elsewhere) a sister of كَانَ", "akşam vakti gitmek, yol almak (رَاحَ يَرُوحُ); (başka yerde) كَانَ'nin kardeşi")
REGLOSS("amda", "to carry through, to see off (a care, a purpose) (Form IV)", "(bir kaygıyı, bir kararı) yerine getirip savmak (if'âl)")
REGLOSS("alqa", "to throw, to cast (Form IV)", "atmak, bırakmak (if'âl)")
REGLOSS("ittaqa", "to ward off (a thing) with something set between, as a shield; (elsewhere) to fear God, to be wary", "bir şeyi araya bir engel (kalkan gibi) koyarak savmak; (başka yerde) Allah'tan korkmak, sakınmak")
REGLOSS("sirr", "the best and richest part of a valley (pl. أَسِرَّة); (elsewhere) a secret", "vadinin en iyi, en verimli yeri (çoğ. أَسِرَّة); (başka yerde) sır")
REGLOSS("shakka", "to pierce, to stick (a thing) into (شَكَّ يَشُكُّ); (elsewhere) to doubt", "delmek, saplamak (شَكَّ يَشُكُّ); (başka yerde) şüphe etmek")
REGLOSS("zamil", "one who rides behind another, a pillion rider; (elsewhere) a fellow", "terkide binen; (başka yerde) arkadaş")
REGLOSS("hashaf", "teats whose milk has dried so that they shrivel; (elsewhere) worthless dried dates", "sütü kuruyup büzüşmüş memeler; (başka yerde) kuru, değersiz hurma")
REGLOSS("muayyad", "made strong, strengthened (ism maf'ul of أَيَّدَ)", "güçlendirilmiş (أَيَّدَ'den ism-i mef'ûl)")
REGLOSS("marfiq", "the elbow (also مِرْفَق); (elsewhere) a thing to lean on", "dirsek (مِرْفَق da denir); (başka yerde) dayanılacak şey")
REGLOSS("rabb", "the Lord (v. 80); owner, master of a thing (vv. 23, 44)", "Rab (80. beyit); bir şeyin sahibi, efendisi (23. ve 44. beyitler)")
REGLOSS("lb-bana", "to part, to stand apart (بَانَ يَبِينُ); (elsewhere) to be plain", "ayrılmak, uzak durmak (بَانَ يَبِينُ); (başka yerde) açık olmak")
REGLOSS("harf", "the edge, the side of a thing; (elsewhere) a letter, a particle", "bir şeyin kenarı, yanı; (başka yerde) harf")
REGLOSS("itq", "nobility, fine breeding (in a beast); (elsewhere) the freeing of a slave", "soyluluk, necabet (hayvanda); (başka yerde) köle azadı")
REGLOSS("shat", "here: the wild ox; (elsewhere) a sheep, a ewe", "burada: yaban öküzü; (başka yerde) koyun")
REGLOSS("mufrad", "alone, solitary; (elsewhere) a single word, the singular", "yalnız, tek başına; (başka yerde) tek kelime, müfred")
REGLOSS("khafi", "faint, hidden; (elsewhere, in usul) the hidden", "hafif, gizli; (başka yerde, usûlde) hafî")
REGLOSS("rajama", "to strike, to pelt (the ground); (elsewhere) to stone", "(yere) vurmak, çarpmak; (başka yerde) taşlamak")
REGLOSS("ahala", "to come at, to turn upon (Form IV); (elsewhere) to deem impossible", "yönelmek, üzerine varmak (if'âl); (başka yerde) imkânsız saymak")
REGLOSS("dhirwa", "the top, the summit of a thing (also ذِرْوَة; pl. ذُرًى)", "bir şeyin tepesi, zirvesi (ذِرْوَة da denir; çoğ. ذُرًى)")
REGLOSS("ifrad", "setting apart, isolating (masdar of أَفْرَدَ); (elsewhere) keeping a word singular", "tecrit etme, ayırma (أَفْرَدَ'nin masdarı); (başka yerde) müfred tutma")
REGLOSS("jadd", "fortune, luck — وَجَدِّكَ: by your fortune!; (elsewhere) a grandfather", "talih, baht — وَجَدِّكَ: talihine andolsun!; (başka yerde) dede")
REGLOSS("aid", "one visiting the sick (pl. عُوَّد); (elsewhere) returning", "hasta ziyaretçisi (çoğ. عُوَّد); (başka yerde) dönen")
REGLOSS("kumayt", "dark red, between red and black — of wine; (elsewhere) a bay horse", "koyu kızıl, kırmızı ile siyah arası — şarap için; (başka yerde) doru at")
REGLOSS("mudaf", "one hard-pressed, driven to seek refuge; (elsewhere, in grammar) the annexed noun", "sıkışmış, sığınmaya muhtaç kalmış; (başka yerde, nahivde) muzâf")
REGLOSS("taqsir", "making short, shortening; (elsewhere) falling short", "kısaltma; (başka yerde) kusur, eksik bırakma")
REGLOSS("naqis", "dwindling, lessening (ism fa'il of نَقَصَ); (elsewhere, in grammar) defective", "eksilen, azalan (نَقَصَ'ten ism-i fâil); (başka yerde, nahivde) nâkıs")
REGLOSS("fahish", "a miser (al-Zawzanī); (elsewhere) gross, outrageous", "cimri (Zevzenî); (başka yerde) çirkin, aşırı")
REGLOSS("thiny", "the end of a rope (dual ثِنْيَا); (elsewhere) a fold, a side", "ipin ucu (ikili ثِنْيَا); (başka yerde) kıvrım, yan")
REGLOSS("summ", "hard, solid (of stones; pl. of أَصَمّ); (elsewhere) deaf", "sert, som (taşlar için; أَصَمّ'ın cem'i); (başka yerde) sağır")
REGLOSS("shahida", "to be present at, to attend (and lend help); (elsewhere) to bear witness", "bir yerde hazır bulunmak (ve yardım etmek); (başka yerde) şahitlik etmek")
REGLOSS("hadath", "a wrong done, an offence; (elsewhere) a young man", "işlenmiş kötülük, suç; (başka yerde) genç")
REGLOSS("muhdath", "a thing done, a wrong committed (ism maf'ul of أَحْدَثَ); (elsewhere) originated", "işlenmiş şey, işlenmiş suç (أَحْدَثَ'ten ism-i mef'ûl); (başka yerde) sonradan olmuş")
REGLOSS("mawla", "lord, kinsman — here: his cousin; (elsewhere) master, protecting lord", "efendi, akraba — burada: amcaoğlu; (başka yerde) efendi, koruyucu")
REGLOSS("tasal", "asking (a masdar of سَأَلَ on تَفْعَال)", "istemek (سَأَلَ'in تَفْعَال vezninde masdarı)")
REGLOSS("darb", "lean of flesh, light (of a man); (elsewhere) a kind; a striking", "eti az, hafif (adam); (başka yerde) tür; vuruş")
REGLOSS("bitana", "a lining (the opposite of the outer face); (elsewhere) an inner circle of confidants", "astar (yüzün zıddı); (başka yerde) sırdaşlar")
REGLOSS("awd", "doing again — here: a second stroke; (elsewhere) a return", "tekrar etmek — burada: ikinci darbe; (başka yerde) dönüş")
REGLOSS("hajiz", "one who holds back, restrains; (elsewhere) a barrier", "alıkoyan, tutan; (başka yerde) engel")
REGLOSS("qaim", "the hilt of a sword; (elsewhere) standing, subsisting", "kılıcın kabzası; (başka yerde) ayakta duran, kâim")
REGLOSS("badiya", "بَوَادِي الإِبِل: the first, the foremost of the camels; (elsewhere) the desert", "بَوَادِي الإِبِل: develerin öndekileri, ilkleri; (başka yerde) çöl")
REGLOSS("ahl", "deserving, worthy of (أَهْلُهُ: deserving of it); (elsewhere) people of", "layık, ehil (أَهْلُهُ: ona layık); (başka yerde) ehli, halkı")
REGLOSS("mashhad", "being present (a masdar with mim, = شُهُود); (elsewhere) a scene", "hazır bulunma (mîmli masdar, = شُهُود); (başka yerde) sahne")
REGLOSS("hamm", "care, worry (v. 11); aim, the soul's urge toward the heights (v. 94; in origin, intent)", "tasa (11. beyit); gaye, nefsi yücelere çeken dürtü (94. beyit; aslı: kasıt)")
REGLOSS("nazara", "to wait for (= انْتَظَرَ, v. 101); (elsewhere) to look at", "beklemek (= انْتَظَرَ, 101. beyit); (başka yerde) bakmak")
REGLOSS("baa", "to buy (as in v. 103 — al-Zawzanī); to sell", "satın almak (103. beyitteki gibi — Zevzenî); satmak")
# ==== REGLOSS ABOVE ====

# ---- paradigms: the shelf's own where the verb is on the shelf; a new verb is built by sarf_gen, or cell for cell on a shelf verb of the same class
MORPH = {"verbs": {}}
def _like(model, pairs, **over):
    """a paradigm on the model of a shelf verb of the same class: the radicals swapped cell for cell, the lexical fields restated"""
    m = json.loads(json.dumps(model, ensure_ascii=False))
    def sw(x):
        if isinstance(x, list): return [sw(c) for c in x]
        for a, b in pairs: x = x.replace(a, "\x00" + b)
        return x.replace("\x00", "")
    out = {k: (sw(v) if k in ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2", "majhulMazi", "majhulMudari") else v) for k, v in m.items()
           if k in ("bab", "wazn", "mazi", "mudari", "amr", "mansub", "majzum", "majzum2", "majhulMazi", "majhulMudari")}
    out.update(over)
    return json.loads(N(json.dumps(out, ensure_ascii=False)))
_marra = find_verb("marra")
def _dbl(f, l, masdar, fail, maful, v="ُ", bab="nasara"):
    """a doubled verb of bāb naṣara (v = ḍamma) or ḍaraba (v = kasra), in the shape sarf_gen states مَرَّ"""
    b = {"nasara": ("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ"), "daraba": ("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ")}[bab]
    return _sg.entry(b[0], b[1], masdar, fail, _sg.mazi14(f + "َ" + l + "ّ", f + "َ" + l + "َ" + l),
                     _sg.mudari14("َ", f + v + l + "ّ", f + "ْ" + l + v + l),
                     [f + v + l + "َّ", f + v + l + "َّا", f + v + l + "ُّوا", f + v + l + "ِّي", f + v + l + "َّا", ("اُ" if v == "ُ" else "اِ") + f + "ْ" + l + v + l + "ْنَ"],
                     "يَ" + f + v + l + "َّ", "يَ" + f + v + l + "َّ", "تَ" + f + v + l + "َّ", maful=maful,
                     note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَ" + f + v + l + "َّ، وَيَجُوزُ لَمْ يَ" + f + "ْ" + l + v + l + "ْ.")
def _cells(e): return {k: e[k] for k in ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2")}
assert _marra and _cells(_dbl("م", "ر", "مُرُور", "مَارّ", None)) == _cells(json.loads(N(json.dumps(_marra, ensure_ascii=False)))), "dbl"
NEW_VERBS = {
 "akafa": _sg.sound1("nasara", "عَكَف", "عْكُف", "اُعْكُف", "عُكُوف", "عَاكِف"),
 "tajallada": _sg.derived(_sg.B5, _sg.W5, "َ", "تَجَلَّد", "تَجَلَّد", "تَجَلَّد", "تَجَلُّد", "مُتَجَلِّد"),
 "jara-stray": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "جَار", "جُر", "جُور", "جُر", "جُور", "جُر", "جَوْر", "جَائِر"),
 "nafada": _sg.sound1("nasara", "نَفَض", "نْفُض", "اُنْفُض", "نَفْض", "نَافِض", "مَنْفُوض", "نُفِضَ", "يُنْفَضُ"),
 "raa-graze": _sg.derived_naqis(_sg.B3 + " — نَاقِصٌ", _sg.W3, "ُ", "رَاعَ", "رَاع", "i", "رَاع", "مُرَاعَاة", "مُرَاعٍ", "مُرَاعًى", "رُوعِيَ", "يُرَاعَى"),
 "irtada": _sg.derived_naqis(_sg.B8 + " — نَاقِصٌ", _sg.W8, "َ", "اِرْتَدَ", "رْتَد", "i", "اِرْتَد", "اِرْتِدَاء", "مُرْتَدٍ"),
 "takhallala": _sg.derived(_sg.B5, _sg.W5, "َ", "تَخَلَّل", "تَخَلَّل", "تَخَلَّل", "تَخَلُّل", "مُتَخَلِّل"),
 "asaffa": _like(find_verb("ahabba"), [("ح", "س"), ("ب", "ف")], masdar="إِسْفَاف", ismFail="مُسِفّ", ismMaful="مُسَفّ", majhulMazi="أُسِفَّ", majhulMudari="يُسَفُّ", note="مُضَاعَفٌ مِنَ الْإِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُسِفَّ، وَيَجُوزُ لَمْ يُسْفِفْ."),
 "kadama": _sg.sound1("daraba", "كَدَم", "كْدِم", "اِكْدِم", "كَدْم", "كَادِم", "مَكْدُوم", "كُدِمَ", "يُكْدَمُ"),
 "takhaddada": _sg.derived(_sg.B5, _sg.W5, "َ", "تَخَدَّد", "تَخَدَّد", "تَخَدَّد", "تَخَدُّد", "مُتَخَدِّد"),
 "nasaa-urge": _sg.seat_hamza(_sg.sound1("fataha", "نَصَأ", "نْصَأ", "اِنْصَأ", "نَصْء", "نَاصِئ", "مَنْصُوء", "نُصِئَ", "يُنْصَأُ", cls="مَهْمُوزُ اللَّامِ")),
 "rada-run": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "رَدَ", "رْد", "i", "اِرْد", "رَدَيَان", "رَادٍ"),
 "bara-show": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "بَرَ", "بْر", "i", "اِبْر", "بَرْي", "بَارٍ"),
 "bara-vie": _sg.derived_naqis(_sg.B3 + " — نَاقِصٌ", _sg.W3, "ُ", "بَارَ", "بَار", "i", "بَار", "مُبَارَاة", "مُبَارٍ", "مُبَارًى", "بُورِيَ", "يُبَارَى"),
 "irtaa": _sg.derived_naqis(_sg.B8 + " — نَاقِصٌ", _sg.W8, "َ", "اِرْتَعَ", "رْتَع", "i", "اِرْتَع", "اِرْتِعَاء", "مُرْتَعٍ"),
 "raa-return": _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "رَاع", "رِع", "رِيع", "رِع", "رِيع", "رِع", "رَيْع", "رَائِع"),
 "takannafa": _sg.derived(_sg.B5, _sg.W5, "َ", "تَكَنَّف", "تَكَنَّف", "تَكَنَّف", "تَكَنُّف", "مُتَكَنِّف"),
 "lazza": dict(_dbl("ل", "ز", "لَزّ", "لَازّ", "مَلْزُوز"), majhulMazi=N("لُزَّ"), majhulMudari=N("يُلَزُّ")),
 "kanafa": _sg.sound1("nasara", "كَنَف", "كْنُف", "اُكْنُف", "كَنْف", "كَانِف", "مَكْنُوف", "كُنِفَ", "يُكْنَفُ"),
 "iktanafa": _sg.derived(_sg.B8, _sg.W8, "َ", "اِكْتَنَف", "كْتَنِف", "اِكْتَنِف", "اِكْتِنَاف", "مُكْتَنِف", "مُكْتَنَف", "اُكْتُنِفَ", "يُكْتَنَفُ"),
 "shada-raise": _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "شَاد", "شِد", "شِيد", "شِد", "شِيد", "شِد", "شَيْد", "شَائِد", "مَشِيد", "شِيدَ", "يُشَادُ"),
 "amarra-twist": _like(find_verb("ahabba"), [("ح", "م"), ("ب", "ر")], masdar="إِمْرَار", ismFail="مُمِرّ", ismMaful="مُمَرّ", majhulMazi="أُمِرَّ", majhulMudari="يُمَرُّ", note="مُضَاعَفٌ مِنَ الْإِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُمِرَّ، وَيَجُوزُ لَمْ يُمْرِرْ."),
 "ajnaha": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَجْنَح", "جْنِح", "أَجْنِح", "إِجْنَاح", "مُجْنِح", "مُجْنَح", "أُجْنِحَ", "يُجْنَحُ"),
 "afraa": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْرَع", "فْرِع", "أَفْرِع", "إِفْرَاع", "مُفْرِع", "مُفْرَع", "أُفْرِعَ", "يُفْرَعُ"),
 "talaqa": _sg.derived_naqis(_sg.B6 + " — نَاقِصٌ", _sg.W6, "َ", "تَلَاقَ", "تَلَاق", "a", "تَلَاق", "تَلَاقٍ", "مُتَلَاقٍ"),
 "saad-ii": _sg.derived(_sg.B2, _sg.W2, "ُ", "صَعَّد", "صَعِّد", "صَعِّد", "تَصْعِيد", "مُصَعِّد", "مُصَعَّد", "صُعِّدَ", "يُصَعَّدُ"),
 "harrada": _sg.derived(_sg.B2, _sg.W2, "ُ", "حَرَّد", "حَرِّد", "حَرِّد", "تَحْرِيد", "مُحَرِّد", "مُحَرَّد", "حُرِّدَ", "يُحَرَّدُ"),
 "istakanna": dict(_sg.entry(_sg.B10 + " — مُضَاعَفٌ", _sg.W10, "اِسْتِكْنَان", "مُسْتَكِنّ", _sg.mazi14("اِسْتَكَنّ", "اِسْتَكْنَن"), _sg.mudari14("َ", "سْتَكِنّ", "سْتَكْنِن"),
     ["اِسْتَكِنَّ", "اِسْتَكِنَّا", "اِسْتَكِنُّوا", "اِسْتَكِنِّي", "اِسْتَكِنَّا", "اِسْتَكْنِنَّ"], "يَسْتَكِنَّ", "يَسْتَكِنَّ", "تَسْتَكِنَّ",
     note="مُضَاعَفٌ مِنَ الِاسْتِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسْتَكِنَّ، وَيَجُوزُ لَمْ يَسْتَكْنِنْ.")),
 "arqala": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَرْقَل", "رْقِل", "أَرْقِل", "إِرْقَال", "مُرْقِل"),
 "sama-vie": _sg.derived_naqis(_sg.B3 + " — نَاقِصٌ", _sg.W3, "ُ", "سَامَ", "سَام", "i", "سَام", "مُسَامَاة", "مُسَامٍ"),
 "ama-swim": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "عَام", "عُم", "عُوم", "عُم", "عُوم", "عُم", "عَوْم", "عَائِم"),
 "fada": _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "فَدَ", "فْد", "i", "اِفْد", "فِدَاء", "فَادٍ", "مَفْدِيّ", "فُدِيَ", "يُفْدَى"),
 "iftada": _sg.derived_naqis(_sg.B8 + " — نَاقِصٌ", _sg.W8, "َ", "اِفْتَدَ", "فْتَد", "i", "اِفْتَد", "اِفْتِدَاء", "مُفْتَدٍ"),
 "kasila": _sg.sound1("samia", "كَسِل", "كْسَل", "اِكْسَل", "كَسَل", "كَسِل", note="كَسِلَ يَكْسَلُ كَسَلًا — لَازِمٌ، وَالصِّفَةُ كَسِلٌ وَكَسْلَانُ."),
 "taballada": _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَلَّد", "تَبَلَّد", "تَبَلَّد", "تَبَلُّد", "مُتَبَلِّد"),
 "ajdhama": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَجْذَم", "جْذِم", "أَجْذِم", "إِجْذَام", "مُجْذِم"),
 "khabba": _dbl("خ", "ب", "خَبَب", "خَابّ", None),
 "dhala-strut": _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "ذَال", "ذِل", "ذِيل", "ذِل", "ذِيل", "ذِل", "ذَيْل", "ذَائِل"),
 "istarfada": _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَرْفَد", "سْتَرْفِد", "اِسْتَرْفِد", "اِسْتِرْفَاد", "مُسْتَرْفِد"),
 "arfada": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَرْفَد", "رْفِد", "أَرْفِد", "إِرْفَاد", "مُرْفِد"),
 "iqtanasa": _sg.derived(_sg.B8, _sg.W8, "َ", "اِقْتَنَص", "قْتَنِص", "اِقْتَنِص", "اِقْتِنَاص", "مُقْتَنِص"),
 "istada": _sg.derived_hollow(_sg.B8 + " — أَجْوَفُ يَائِيٌّ", _sg.W8, "َ", "اِصْطَاد", "اِصْطَد", "صْطَاد", "صْطَد", "اِصْطَاد", "اِصْطَد", "اِصْطِيَاد", "مُصْطَاد", note="أَجْوَفُ مِنَ الِافْتِعَالِ، وَتَاؤُهُ مُبْدَلَةٌ طَاءً بَعْدَ الصَّادِ: اِصْطَادَ يَصْطَادُ — لَمْ يَصْطَدْ."),
 "asmaa": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْمَع", "سْمِع", "أَسْمِع", "إِسْمَاع", "مُسْمِع", "مُسْمَع", "أُسْمِعَ", "يُسْمَعُ"),
 "tashaddada": _sg.derived(_sg.B5, _sg.W5, "َ", "تَشَدَّد", "تَشَدَّد", "تَشَدَّد", "تَشَدُّد", "مُتَشَدِّد"),
 "rajja": _sg.derived(_sg.B2, _sg.W2, "ُ", "رَجَّع", "رَجِّع", "رَجِّع", "تَرْجِيع", "مُرَجِّع", "مُرَجَّع", "رُجِّعَ", "يُرَجَّعُ"),
 "tahama": _sg.derived_naqis(_sg.B6 + " — نَاقِصٌ", _sg.W6, "َ", "تَحَامَ", "تَحَام", "a", "تَحَام", "تَحَامٍ", "مُتَحَامٍ"),
 "istaa": dict(_sg.derived_hollow(_sg.B10 + " — أَجْوَفُ، حُذِفَتْ تَاؤُهُ", _sg.W10, "َ", "اِسْطَاع", "اِسْطَع", "سْطِيع", "سْطِع", "اِسْطِيع", "اِسْطِع", "اِسْطَاعَة", "مُسْطِيع",
     note="لُغَةٌ فِي اسْتَطَاعَ يَسْتَطِيعُ حُذِفَتْ مِنْهَا التَّاءُ تَخْفِيفًا: اِسْطَاعَ يَسْطِيعُ — لَمْ يَسْطِعْ؛ مَسْمُوعٌ لَا يُقَاسُ عَلَيْهِ."), samai=True),
 "hafala": _sg.sound1("daraba", "حَفَل", "حْفِل", "اِحْفِل", "حَفْل", "حَافِل"),
 "azbada": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَزْبَد", "زْبِد", "أَزْبِد", "إِزْبَاد", "مُزْبِد"),
 "khaddada": _sg.derived(_sg.B2, _sg.W2, "ُ", "خَضَّد", "خَضِّد", "خَضِّد", "تَخْضِيد", "مُخَضِّد", "مُخَضَّد", "خُضِّدَ", "يُخَضَّدُ"),
 "rawwa": _sg.derived_naqis(_sg.B2 + " — نَاقِصٌ", _sg.W2, "ُ", "رَوَّ", "رَوّ", "i", "رَوّ", "تَرْوِيَة", "مُرَوٍّ"),
 "itama": _sg.derived_hollow(_sg.B8 + " — أَجْوَفُ يَائِيٌّ", _sg.W8, "َ", "اِعْتَام", "اِعْتَم", "عْتَام", "عْتَم", "اِعْتَام", "اِعْتَم", "اِعْتِيَام", "مُعْتَام", note="أَجْوَفُ مِنَ الِافْتِعَالِ: اِعْتَامَ يَعْتَامُ — لَمْ يَعْتَمْ."),
 "baada": _sg.sound1("karuma", "بَعُد", "بْعُد", "اُبْعُد", "بُعْد", "بَعِيد", note="بَعُدَ يَبْعُدُ بُعْدًا — لَازِمٌ، وَالصِّفَةُ بَعِيدٌ."),
 "ayasa": _sg.entry(_sg.B4 + " — مِثَالٌ يَائِيٌّ مَهْمُوزُ الْعَيْنِ", _sg.W4, "إِيئَاس", "مُوئِس", _sg.mazi14("أَيْأَس"), _sg.mudari14("ُ", "وئِس"),
     ["أَيْئِسْ", "أَيْئِسَا", "أَيْئِسُوا", "أَيْئِسِي", "أَيْئِسَا", "أَيْئِسْنَ"], "يُوئِسَ", "يُوئِسْ", "تُوئِسْ", "مُوأَس",
     note="مِثَالٌ يَائِيٌّ مِنَ الْإِفْعَالِ: تُقْلَبُ يَاؤُهُ وَاوًا بَعْدَ الضَّمَّةِ — أَيْأَسَ يُوئِسُ إِيئَاسًا فَهُوَ مُوئِسٌ، كَأَيْقَنَ يُوقِنُ."),
 "nashada": _sg.sound1("nasara", "نَشَد", "نْشُد", "اُنْشُد", "نِشْدَان", "نَاشِد", "مَنْشُود", "نُشِدَ", "يُنْشَدُ"),
 "aghfala": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَغْفَل", "غْفِل", "أَغْفِل", "إِغْفَال", "مُغْفِل", "مُغْفَل", "أُغْفِلَ", "يُغْفَلُ"),
 "jahada": _sg.sound1("fataha", "جَهَد", "جْهَد", "اِجْهَد", "جَهْد", "جَاهِد"),
 "farraja": _sg.derived(_sg.B2, _sg.W2, "ُ", "فَرَّج", "فَرِّج", "فَرِّج", "تَفْرِيج", "مُفَرِّج", "مُفَرَّج", "فُرِّجَ", "يُفَرَّجُ"),
 "anzara": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْظَر", "نْظِر", "أَنْظِر", "إِنْظَار", "مُنْظِر", "مُنْظَر", "أُنْظِرَ", "يُنْظَرُ"),
 "inthana": _sg.derived_naqis(_sg.B7 + " — نَاقِصٌ", _sg.W7, "َ", "اِنْثَنَ", "نْثَن", "i", "اِنْثَن", "اِنْثِنَاء", "مُنْثَنٍ"),
 "balla-seize": _sg.entry("مِنْ بَابِ سَمِعَ يَسْمَعُ — مُضَاعَفٌ", "فَعِلَ يَفْعَلُ", "بَلَل", "بَالّ", _sg.mazi14("بَلّ", "بَلِل"), _sg.mudari14("َ", "بَلّ", "بْلَل"),
     ["بَلَّ", "بَلَّا", "بَلُّوا", "بَلِّي", "بَلَّا", "اِبْلَلْنَ"], "يَبَلَّ", "يَبَلَّ", "تَبَلَّ", note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَبَلَّ، وَيَجُوزُ لَمْ يَبْلَلْ."),
 "tarra": _dbl("ت", "ر", "تُرُور", "تَارّ", None, v="ِ", bab="daraba"),
 "imtalla": _sg.entry(_sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِمْتِلَال", "مُمْتَلّ", _sg.mazi14("اِمْتَلّ", "اِمْتَلَل"), _sg.mudari14("َ", "مْتَلّ", "مْتَلِل"),
     ["اِمْتَلَّ", "اِمْتَلَّا", "اِمْتَلُّوا", "اِمْتَلِّي", "اِمْتَلَّا", "اِمْتَلِلْنَ"], "يَمْتَلَّ", "يَمْتَلَّ", "تَمْتَلَّ",
     note="مُضَاعَفٌ مِنَ الِافْتِعَالِ: يُفَكُّ مَعَ الضَّمَائِرِ السَّاكِنَةِ — يَمْتَلِلْنَ؛ الْجَزْمُ بِالْفَتْحِ: لَمْ يَمْتَلَّ، وَيَجُوزُ لَمْ يَمْتَلِلْ."),
 "naa-announce": _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ", "y", "نَعَ", "نْع", "a", "اِنْع", "نَعْي", "نَاعٍ", "مَنْعِيّ", "نُعِيَ", "يُنْعَى"),
 "itaraka": _sg.derived(_sg.B8, _sg.W8, "َ", "اِعْتَرَك", "عْتَرِك", "اِعْتَرِك", "اِعْتِرَاك", "مُعْتَرِك"),
 "arada": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَرْعَد", "رْعِد", "أَرْعِد", "إِرْعَاد", "مُرْعِد", "مُرْعَد", "أُرْعِدَ", "يُرْعَدُ"),
 "zawwada": _sg.derived(_sg.B2, _sg.W2, "ُ", "زَوَّد", "زَوِّد", "زَوِّد", "تَزْوِيد", "مُزَوِّد", "مُزَوَّد", "زُوِّدَ", "يُزَوَّدُ"),
 # ==== NEW VERBS ABOVE ====
}
NEW_VERBS = {k + SUF: v for k, v in NEW_VERBS.items()}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = NEW_VERBS.get(k) if k in NEW_GLOSS else find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par
assert set(NEW_VERBS) == {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}, set(NEW_VERBS) ^ {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}

# ---- the attribution: built from what is published, so that it never claims more than the chapters hold -------------------------
def PAGE_OF(n):
    """the printed page on which al-Zawzanī's edition sets verse n"""
    for a, pg in ((102, 120), (98, 119), (94, 118), (91, 117), (88, 116), (84, 115), (79, 114), (75, 113), (72, 112), (68, 111), (63, 110), (60, 109), (56, 108), (53, 107), (50, 106), (47, 105),
                  (44, 104), (40, 103), (36, 102), (33, 101), (28, 100), (26, 99), (23, 98), (21, 97), (17, 96), (16, 95), (14, 94), (11, 93), (8, 92), (6, 91), (4, 90), (1, 89)):
        if n >= a: return pg
LAST_PAGE = PAGE_OF(LAST) if LAST else 89
# slips of the e-text corrected against a witness: (verse, ar, en, tr)
CORR = [
 (2, "الْبَيْتُ ٢ «على مَطِيِّهُمْ» ← «عَلَيَّ مَطِيَّهُمْ» (الْوَزْنُ، وَالتِّبْرِيزِيُّ ص ٥٥، وَالدُّرَّةُ ١/١٧٤، وَنَصُّ الزَّوْزَنِيِّ نَفْسُهُ فِي مُعَلَّقَةِ امْرِئِ الْقَيْسِ)",
  "v. 2 «على مَطِيِّهُمْ» → «عَلَيَّ مَطِيَّهُمْ» (the metre; al-Tibrīzī p. 55; al-Durra 1/174; al-Zawzanī's own text of the same verse in the Muʿallaqa of Imruʾ al-Qays)",
  "2. beyit «على مَطِيِّهُمْ» → «عَلَيَّ مَطِيَّهُمْ» (vezin; Tebrîzî s. 55; Dürre 1/174; Zevzenî'nin İmruülkays Muallakası'ndaki aynı beyit için kendi metni)"),
 (12, "الْبَيْتُ ١٢ «نَضَأتُها» بِالضَّادِ ← «نَصَأْتُهَا» بِالصَّادِ (شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ: «نَصَأْتُهَا، بِالصَّادِ: زَجَرْتُهَا»)",
  "v. 12 «نَضَأتُها», with ḍād → «نَصَأْتُهَا», with ṣād (al-Zawzanī's own commentary: «نصأتها، بالصاد: زجرتها»)",
  "12. beyit dâd ile «نَضَأتُها» → sâd ile «نَصَأْتُهَا» (Zevzenî'nin kendi şerhi: «نصأتها، بالصاد: زجرتها»)"),
 (13, "الْبَيْتُ ١٣ «جَمالِيّةٍ» بِفَتْحِ الْجِيمِ ← «جُمَالِيَّةٍ» بِضَمِّهَا (الْمَعَاجِمُ: «نَاقَةٌ جُمَالِيَّةٌ، بِالضَّمِّ»؛ وَلَا شَاهِدَ ثَانِيًا لِلْبَيْتِ، قَالَ الدُّرَّةُ: لَمْ يَذْكُرْهُ غَيْرُ الزَّوْزَنِيِّ)",
  "v. 13 «جَمالِيّةٍ», with a fatḥa on the jīm → «جُمَالِيَّةٍ», with a ḍamma (the lexica: «نَاقَةٌ جُمَالِيَّةٌ، بالضم»; the verse has no second witness — al-Durra: none but al-Zawzanī gives it)",
  "13. beyit cîm'in fethasıyla «جَمالِيّةٍ» → dammesiyle «جُمَالِيَّةٍ» (sözlükler: «نَاقَةٌ جُمَالِيَّةٌ، بالضم»; beytin ikinci bir şahidi yoktur — Dürre: onu Zevzenî'den başkası zikretmemiştir)"),
 (17, "الْبَيْتُ ١٧ «بِمَسْرَدِ» بِفَتْحِ الْمِيمِ ← «بِمِسْرَدِ» بِكَسْرِهَا (التِّبْرِيزِيُّ ص ٦٤؛ وَهُوَ اسْمُ آلَةٍ، وَالزَّوْزَنِيُّ نَفْسُهُ: «الْمِسْرَدُ وَالْمِسْرَادُ: الْإِشْفَى»)",
  "v. 17 «بِمَسْرَدِ», with a fatha on the mim → «بِمِسْرَدِ», with a kasra (al-Tibrīzī p. 64; it is a noun of instrument — al-Zawzanī's own gloss: «the مسرد or مسراد: an awl»)",
  "17. beyit mîm'in fethasıyla «بِمَسْرَدِ» → kesresiyle «بِمِسْرَدِ» (Tebrîzî s. 64; ism-i âlettir — Zevzenî'nin kendi açıklaması: «مسرد ya da مسراد: biz»)"),
 (19, "الْبَيْتُ ١٩ «فَخِذَانٍ» بِالتَّنْوِينِ ← «فَخِذَانِ» (التِّبْرِيزِيُّ ص ٦٥؛ وَالدُّرَّةُ ١/١٩٥: «وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ»؛ وَالْمُثَنَّى لَا يُنَوَّنُ)",
  "v. 19 «فَخِذَانٍ», with tanwin → «فَخِذَانِ» (al-Tibrīzī p. 65; al-Durra 1/195: «the nun stands for the tanwin»; a dual takes no tanwin)",
  "19. beyit tenvinli «فَخِذَانٍ» → «فَخِذَانِ» (Tebrîzî s. 65; Dürre 1/195: «nûn tenvinin bedelidir»; tesniye tenvin almaz)"),
 (20, "الْبَيْتُ ٢٠ «وَطَيٍّ» مَجْرُورًا مُنَوَّنًا ← «وَطَيُّ» مَرْفُوعًا مُضَافًا (التِّبْرِيزِيُّ ص ٦٥: «وَطَيُّ مَحَالٍ»؛ وَالدُّرَّةُ ١/١٩٦: مَعْطُوفٌ عَلَى «فَخِذَانِ»؛ وَالْمُضَافُ لَا يُنَوَّنُ)",
  "v. 20 «وَطَيٍّ», in jarr with tanwin → «وَطَيُّ», in raf' and annexed (al-Tibrīzī p. 65: «وَطَيُّ مَحَالٍ»; al-Durra 1/196: conjoined to «فَخِذَانِ»; an annexed noun takes no tanwin)",
  "20. beyit tenvinli ve mecrûr «وَطَيٍّ» → merfû ve muzâf «وَطَيُّ» (Tebrîzî s. 65: «وَطَيُّ مَحَالٍ»; Dürre 1/196: «فَخِذَانِ»e ma'tûf; muzâf tenvin almaz)"),
 (25, "الْبَيْتُ ٢٥ «أُلها عَضُداها» ← «لَهَا عَضُدَاهَا» (التِّبْرِيزِيُّ ص ٦٧؛ وَالدُّرَّةُ ١/٢٠٢؛ وَالْوَزْنُ)",
  "v. 25 «أُلها عَضُداها» → «لَهَا عَضُدَاهَا» (al-Tibrīzī p. 67; al-Durra 1/202; the metre)",
  "25. beyit «أُلها عَضُداها» → «لَهَا عَضُدَاهَا» (Tebrîzî s. 67; Dürre 1/202; vezin)"),
 (31, "الْبَيْتُ ٣١ «وَخَذٌّ» بِالذَّالِ ← «وَخَدٌّ» بِالدَّالِ (التِّبْرِيزِيُّ ص ٧٠؛ وَالدُّرَّةُ ١/٢٠٨؛ وَشَرْحُ الزَّوْزَنِيِّ نَفْسِهِ: «شَبَّهَ خَدَّهَا»)",
  "v. 31 «وَخَذٌّ», with dhal → «وَخَدٌّ», with dal (al-Tibrīzī p. 70; al-Durra 1/208; al-Zawzanī's own commentary: «he likens her cheek»)",
  "31. beyit zâl ile «وَخَذٌّ» → dâl ile «وَخَدٌّ» (Tebrîzî s. 70; Dürre 1/208; Zevzenî'nin kendi şerhi: «yanağını benzetti»)"),
 (33, "الْبَيْتُ ٣٣ «كَمَكْحُولَتَيّ» بِتَشْدِيدِ الْيَاءِ ← «كَمَكْحُولَتَيْ» (الدُّرَّةُ ١/٢١٠: مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ؛ وَالْوَزْنُ)",
  "v. 33 «كَمَكْحُولَتَيّ», with a shadda on the ya → «كَمَكْحُولَتَيْ» (al-Durra 1/210: a dual whose nun is dropped for the annexation; the metre)",
  "33. beyit yâ'sı şeddeli «كَمَكْحُولَتَيّ» → «كَمَكْحُولَتَيْ» (Dürre 1/210: izâfet sebebiyle nûnu düşmüş tesniye; vezin)"),
 (34, "الْبَيْتُ ٣٤ «مَنَدِّدِ» بِفَتْحِ الْمِيمِ ← «مُنَدِّدِ» بِضَمِّهَا (اسْمُ فَاعِلٍ مِنْ نَدَّدَ؛ وَالتِّبْرِيزِيُّ ص ٧١ «مُنَدَّدِ» بِضَمِّ الْمِيمِ؛ وَكَسْرُ الدَّالِ مِنَ الطَّبْعَةِ أُبْقِيَ)",
  "v. 34 «مَنَدِّدِ», with a fatha on the mim → «مُنَدِّدِ», with a damma (an ism fa'il of نَدَّدَ; al-Tibrīzī p. 71 «مُنَدَّدِ», with a damma on the mim; the edition's kasra on the dal is kept)",
  "34. beyit mîm'in fethasıyla «مَنَدِّدِ» → dammesiyle «مُنَدِّدِ» (نَدَّدَ'den ism-i fâil; Tebrîzî s. 71 mîm'in dammesiyle «مُنَدَّدِ»; baskının dâl'daki kesresi korundu)"),
 (38, "الْبَيْتُ ٣٨ «مِنَ الْقَدّ» بِفَتْحِ الْقَافِ ← «مِنَ الْقِدِّ» بِكَسْرِهَا (التِّبْرِيزِيُّ ص ٧٣؛ وَالْقِدُّ: السَّيْرُ مِنَ الْجِلْدِ، وَبِهِ يُلْوَى السَّوْطُ كَمَا شَرَحَ الزَّوْزَنِيُّ: «سَوْطٌ مَلْوِيٌّ مِنَ الْقِدِّ»)",
  "v. 38 «من القَدّ», with a fatha on the qaf → «مِنَ الْقِدِّ», with a kasra (al-Tibrīzī p. 73; القِدّ is a thong of hide, of which the whip is twisted, as al-Zawzanī explains: «a whip twisted of rawhide»)",
  "38. beyit kâf'ın fethasıyla «من القَدّ» → kesresiyle «مِنَ الْقِدِّ» (Tebrîzî s. 73; القِدّ deriden kayıştır, kamçı ondan bükülür — Zevzenî'nin açıkladığı gibi: «kayıştan bükülmüş kamçı»)"),
 (50, "الْبَيْتُ ٥٠ «مَطُْروقَةً» بِحَرَكَتَيْنِ عَلَى الطَّاءِ ← «مَطْرُوقَةً» (شَرْحُ الزَّوْزَنِيِّ: «الْمَطْرُوقَةُ: الَّتِي بِهَا ضَعْفٌ»؛ وَضَبْطُ التِّبْرِيزِيِّ ص ٧٩ «مَطْرُوفَةً»)",
  "v. 50 «مَطُْروقَةً», with two marks on the ta → «مَطْرُوقَةً» (al-Zawzanī's gloss «المطروقة: one with a weakness in her»; al-Tibrīzī's vowelling p. 79, «مَطْرُوفَةً»)",
  "50. beyit tâ üzerinde iki harekeli «مَطُْروقَةً» → «مَطْرُوقَةً» (Zevzenî'nin açıklaması: «المطروقة: üzerinde bir zaaf bulunan»; Tebrîzî'nin zabtı s. 79 «مَطْرُوفَةً»)"),
 (53, "الْبَيْتُ ٥٣ «إِلَى أَنّ» بِتَشْدِيدِ النُّونِ ← «إِلَى أَنْ» (التِّبْرِيزِيُّ ص ٨٠؛ وَالدُّرَّةُ ١/٢٣٩: «أَنْ: حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ»؛ وَالْوَزْنُ)",
  "v. 53 «إلى أنّ», with a shadda on the nun → «إِلَى أَنْ» (al-Tibrīzī p. 80; al-Durra 1/239: «أن: the masdar-making particle»; the metre)",
  "53. beyit nûn'u şeddeli «إلى أنّ» → «إِلَى أَنْ» (Tebrîzî s. 80; Dürre 1/239: «أن: masdar harfi»; vezin)"),
 (54, "الْبَيْتُ ٥٤ «غَبَراءَ» بِفَتْحِ الْبَاءِ ← «غَبْرَاءَ» بِسُكُونِهَا (التِّبْرِيزِيُّ ص ٨٠؛ وَالْوَزْنُ لَا يَسْتَقِيمُ بِالْفَتْحِ)",
  "v. 54 «غَبَراءَ», with a fatha on the ba → «غَبْرَاءَ», with a sukun (al-Tibrīzī p. 80; the metre does not allow the fatha)",
  "54. beyit bâ'nın fethasıyla «غَبَراءَ» → sükûnuyla «غَبْرَاءَ» (Tebrîzî s. 80; vezin fethayla yürümez)"),
 (63, "الْبَيْتُ ٦٣ «نَحّامِ» بِلَا تَنْوِينٍ ← «نَحَّامٍ» (التِّبْرِيزِيُّ ص ٨٥؛ وَالدُّرَّةُ ١/٢٥٤: «بَخِيلٍ» نَعْتٌ ثَانٍ لَا مُضَافٌ إِلَيْهِ؛ وَالْوَزْنُ لَا يَسْتَقِيمُ إِلَّا بِالتَّنْوِينِ)",
  "v. 63 «نَحّامِ», without tanwin → «نَحَّامٍ» (al-Tibrīzī p. 85; al-Durra 1/254: «بَخِيلٍ» is a second adjective, not annexed; the metre stands only with the tanwin)",
  "63. beyit tenvinsiz «نَحّامِ» → «نَحَّامٍ» (Tebrîzî s. 85; Dürre 1/254: «بَخِيلٍ» muzâfun ileyh değil ikinci na'ttır; vezin ancak tenvinle yürür)"),
 (64, "الْبَيْتُ ٦٤ «جُثَوَتَيْنِ» بِفَتْحِ الثَّاءِ ← «جُثْوَتَيْنِ» بِسُكُونِهَا (التِّبْرِيزِيُّ ص ٨٥؛ وَالْوَزْنُ؛ وَالْوَاحِدَةُ جُثْوَةٌ كَمَا فِي شَرْحِ الزَّوْزَنِيِّ)",
  "v. 64 «جُثَوَتَيْنِ», with a fatha on the tha → «جُثْوَتَيْنِ», with a sukun (al-Tibrīzī p. 85; the metre; the singular جُثْوَة, as in al-Zawzanī's commentary)",
  "64. beyit sâ'nın fethasıyla «جُثَوَتَيْنِ» → sükûnuyla «جُثْوَتَيْنِ» (Tebrîzî s. 85; vezin; tekili Zevzenî'nin şerhindeki gibi جُثْوَة)"),
 (79, "الْبَيْتُ ٧٩ «نَائِبًا» بِالْبَاءِ ← «نَائِيًا» بِالْيَاءِ (التِّبْرِيزِيُّ ص ٩٢؛ وَالدُّرَّةُ ١/٢٧٧؛ وَشَرْحُ الزَّوْزَنِيِّ نَفْسِهِ: «وَإِنْ بَعُدَتْ غَايَةَ الْبُعْدِ»)",
  "v. 79 «نَائِبًا», with ba → «نَائِيًا», with ya (al-Tibrīzī p. 92; al-Durra 1/277; al-Zawzanī's own commentary: «even if I went as far as can be»)",
  "79. beyit bâ ile «نَائِبًا» → yâ ile «نَائِيًا» (Tebrîzî s. 92; Dürre 1/277; Zevzenî'nin kendi şerhi: «en uzak yere gitsem de»)"),
 (81, "الْبَيْتُ ٨١ «كَثيرِ» بِلَا تَنْوِينٍ ← «كَثِيرٍ» (التِّبْرِيزِيُّ ص ٩٢؛ وَالدُّرَّةُ ١/٢٨٠ «كَثِيرٍ»: نَعْتُ «مَالٍ»؛ وَالْوَزْنُ لَا يَسْتَقِيمُ إِلَّا بِالتَّنْوِينِ)",
  "v. 81 «كثيرِ», without tanwin → «كَثِيرٍ» (al-Tibrīzī p. 92; al-Durra 1/280 «كثيرٍ», the adjective of «مَالٍ»; the metre stands only with the tanwin)",
  "81. beyit tenvinsiz «كثيرِ» → «كَثِيرٍ» (Tebrîzî s. 92; Dürre 1/280 «كثيرٍ»: «مَالٍ»in na'tı; vezin ancak tenvinle yürür)"),
 (88, "الْبَيْتُ ٨٨ «ذَاتُ حَيْف» بِالْحَاءِ ← «ذَاتُ خَيْفٍ» بِالْخَاءِ (شَرْحُ الزَّوْزَنِيِّ نَفْسِهِ: «الْخَيْفُ: جِلْدُ الضَّرْعِ»؛ وَالتِّبْرِيزِيُّ ص ٩٥؛ وَالدُّرَّةُ ١/٢٨٨)",
  "v. 88 «ذاتُ حَيْف», with ḥa → «ذَاتُ خَيْفٍ», with kha (al-Zawzanī's own commentary: «الخيف: the skin of the udder»; al-Tibrīzī p. 95; al-Durra 1/288)",
  "88. beyit hâ ile «ذاتُ حَيْف» → hı ile «ذَاتُ خَيْفٍ» (Zevzenî'nin kendi şerhi: «الخيف: memenin derisi»; Tebrîzî s. 95; Dürre 1/288)"),
 (91, "الْبَيْتُ ٩١ «نَفْعَهَا» بِالنَّصْبِ ← «نَفْعُهَا» بِالرَّفْعِ (التِّبْرِيزِيُّ ص ٩٦؛ وَالدُّرَّةُ ١/٢٩٢: مُبْتَدَأٌ بَعْدَ «إِنَّمَا» الْكَافَّةِ)؛ وَ«الْبْرَكِ» ← «الْبَرْكِ» (التِّبْرِيزِيُّ؛ وَالْوَزْنُ)",
  "v. 91 «نَفْعَهَا», in nasb → «نَفْعُهَا», in raf' (al-Tibrīzī p. 96; al-Durra 1/292: a mubtada after the restraining إِنَّمَا); and «البْرَكِ» → «الْبَرْكِ» (al-Tibrīzī; the metre)",
  "91. beyit mansûb «نَفْعَهَا» → merfû «نَفْعُهَا» (Tebrîzî s. 96; Dürre 1/292: kâffe «إِنَّمَا»dan sonra mübteda); ve «البْرَكِ» → «الْبَرْكِ» (Tebrîzî; vezin)"),
 (100, "الْبَيْتُ ١٠٠ «تَعْتَرِكُ» بِالضَّمِّ ← «تَعْتَرِكْ» بِالسُّكُونِ (التِّبْرِيزِيُّ ص ٩٩؛ وَالدُّرَّةُ ١/٣٠٢: فِعْلُ شَرْطٍ مَجْزُومٌ بِـ«مَتَى»؛ وَالْوَزْنُ)",
  "v. 100 «تعترِكُ», with a damma → «تَعْتَرِكْ», with a sukun (al-Tibrīzī p. 99; al-Durra 1/302: the condition's verb in jazm by مَتَى; the metre)",
  "100. beyit dammeli «تعترِكُ» → sükûnlu «تَعْتَرِكْ» (Tebrîzî s. 99; Dürre 1/302: «مَتَى» ile meczûm şart fiili; vezin)"),
 (102, "الْبَيْتُ ١٠٢ «تُزَوَّدِ» بِفَتْحِ الْوَاوِ ← «تُزَوِّدِ» بِكَسْرِهَا (شَرْحُ الزَّوْزَنِيِّ نَفْسِهِ: «مَنْ لَمْ تُزَوِّدْهُ»؛ وَالدُّرَّةُ ١/٣٠٦: فَاعِلُهُ «أَنْتَ» وَالْعَائِدُ مَحْذُوفٌ)",
  "v. 102 «تُزَوَّدِ», with a fatha on the waw → «تُزَوِّدِ», with a kasra (al-Zawzanī's own commentary: «one whom you did not provision»; al-Durra 1/306: its doer is «you», the returning pronoun left out)",
  "102. beyit vâv'ın fethasıyla «تُزَوَّدِ» → kesresiyle «تُزَوِّدِ» (Zevzenî'nin kendi şerhi: «azık vermediğin kimse»; Dürre 1/306: fâili «أَنْتَ», âid zamir mahzûf)"),
 # ==== CORR ABOVE ====
]
# what is left for the scholar: (verse — 0 for the khabar, ar, en, tr)
SCHOLAR = [
 (0, "«عِنْدَ عَمْرِو بْنِ بِشْرٍ» فِي الْخَبَرِ (كَذَا فِي الطَّبْعَةِ، وَالرَّجُلُ عَبْدُ عَمْرِو بْنِ بِشْرٍ كَمَا فِي تَتِمَّةِ الْكَلَامِ؛ أُبْقِيَ النَّصُّ عَلَى حَالِهِ لِعَدَمِ الشَّاهِدِ)",
  "«عند عمرو بن بشر» in the khabar (so the edition; the man is ʿAbd ʿAmr ibn Bishr, as the rest of the sentence shows — the reading is kept, there being no second witness)",
  "haberdeki «عند عمرو بن بشر» (baskıda böyledir; cümlenin devamının gösterdiği gibi adam Abdü Amr b. Bişr'dir — ikinci bir şahit bulunmadığından metin olduğu gibi bırakıldı)"),
 (0, "ضَبْطُ «يَعْكُفْنَ» (بِضَمِّ الْكَافِ، وَيَجُوزُ كَسْرُهَا) وَ«سَرَارَةِ» وَ«مَلْهَمَا»", "the vowelling of «يَعْكُفْنَ» (ḍamma on the kāf; a kasra is also sound), «سَرَارَةِ» and «مَلْهَمَا»", "«يَعْكُفْنَ» (kâf'ın dammesiyle; kesresi de câizdir), «سَرَارَةِ» ve «مَلْهَمَا» kelimelerinin zabtı"),
 (4, "«يَجُورُ بِهِ» فِي الْبَيْتِ ٤ (كَذَا فِي طَبْعَةِ الزَّوْزَنِيِّ بِتَذْكِيرِ الضَّمِيرِ، وَعِنْدَ التِّبْرِيزِيِّ وَالدُّرَّةِ «بِهَا»؛ وَالْوَزْنُ يَحْتَمِلُهُمَا) وَرَفْعُ «عَدَوْلِيَّةٌ» (وَهِيَ عِنْدَ التِّبْرِيزِيِّ مَجْرُورَةٌ)",
  "«يَجُورُ بِهِ» in v. 4 (so al-Zawzanī's edition, with a masculine pronoun; al-Tibrīzī and al-Durra read «بِهَا»; the metre allows both), and the raf' of «عَدَوْلِيَّةٌ» (al-Tibrīzī's text has jarr)",
  "4. beyitteki «يَجُورُ بِهِ» (Zevzenî baskısında müzekker zamirle böyledir; Tebrîzî ve Dürre'de «بِهَا»; vezin ikisine de uyar) ve «عَدَوْلِيَّةٌ»in ref'i (Tebrîzî metninde mecrûrdur)"),
 (8, "جَرُّ «دِعْصٍ» فِي الْبَيْتِ ٨ (كَذَا فِي الطَّبْعَةِ، وَتَقْدِيرُ الزَّوْزَنِيِّ وَرِوَايَةُ التِّبْرِيزِيِّ عَلَى الرَّفْعِ «دِعْصٌ»)، وَإِعْرَابُ «لَهُ نَدِ»",
  "the jarr of «دِعْصٍ» in v. 8 (so the edition; al-Zawzanī's paraphrase and al-Tibrīzī's text have raf', «دِعْصٌ»), and the parse of «لَهُ نَدِ»",
  "8. beyitteki «دِعْصٍ»in cerri (baskıda böyledir; Zevzenî'nin takdiri ve Tebrîzî'nin rivayeti ref' iledir: «دِعْصٌ») ve «لَهُ نَدِ»nin i'râbı"),
 (13, "ضَمُّ جِيمِ «جُمَالِيَّةٍ» فِي الْبَيْتِ ١٣ (فِي الطَّبْعَةِ مَفْتُوحَةٌ، وَصُحِّحَتْ مِنَ الْمَعَاجِمِ وَحْدَهَا)",
  "the ḍamma on the jīm of «جُمَالِيَّةٍ» in v. 13 (the edition prints a fatḥa; corrected from the lexica alone)",
  "13. beyitteki «جُمَالِيَّةٍ»in cîminin dammesi (baskıda fethalıdır; yalnızca sözlüklere dayanılarak düzeltildi)"),
 (20, "فَتْحُ حَاءِ «الْحَنِيِّ» فِي الْبَيْتِ ٢٠ (كَذَا فِي الطَّبْعَةِ؛ وَالتِّبْرِيزِيُّ يَضُمُّهَا وَيَذْكُرُ الْكَسْرَ)",
  "the fatha on the ha of «الْحَنِيِّ» in v. 20 (so the edition; al-Tibrīzī has a damma and mentions a kasra)",
  "20. beyitteki «الْحَنِيِّ»nin hâsının fethası (baskıda böyledir; Tebrîzî dammeyle okur, kesreyi de zikreder)"),
 (29, "تَشْدِيدُ «صَعَّدَتْ» فِي الْبَيْتِ ٢٩ (كَذَا فِي الطَّبْعَةِ، وَعِنْدَ التِّبْرِيزِيِّ «صَعَدَتْ»، وَقَوْلُ الزَّوْزَنِيِّ «وَالْبَاءُ لِلتَّعْدِيَةِ» أَلْيَقُ بِالْمُجَرَّدِ؛ وَالْوَزْنُ يَحْتَمِلُهُمَا)",
  "the shadda of «صَعَّدَتْ» in v. 29 (so the edition; al-Tibrīzī has «صَعَدَتْ», and al-Zawzanī's remark that the ba makes the verb transitive suits the bare verb better; the metre allows both)",
  "29. beyitteki «صَعَّدَتْ»in şeddesi (baskıda böyledir; Tebrîzî'de «صَعَدَتْ»; Zevzenî'nin «bâ ta'diye içindir» sözü mücerred fiile daha uygundur; vezin ikisine de elverir)"),
 (31, "كَسْرُ قَافِ «قِدُّهُ» فِي الْبَيْتِ ٣١ (كَذَا فِي الطَّبْعَةِ، وَعِنْدَ التِّبْرِيزِيِّ «قَدُّهُ» بِالْفَتْحِ، وَتَفْسِيرُ الزَّوْزَنِيِّ «اضْطِرَابُ الْقَطْعِ» يُقَوِّي الْفَتْحَ)",
  "the kasra on the qaf of «قِدُّهُ» in v. 31 (so the edition; al-Tibrīzī has «قَدُّهُ», with a fatha, and al-Zawzanī's gloss «an uneven cutting» favours the fatha)",
  "31. beyitteki «قِدُّهُ»nun kâfının kesresi (baskıda böyledir; Tebrîzî'de fethayla «قَدُّهُ»; Zevzenî'nin «kesimin çarpıklığı» açıklaması fethayı destekler)"),
 (38, "ضَمُّ تَاءِ «شِئْتُ» فِي الْبَيْتَيْنِ ٣٨ وَ٣٩ (كَذَا فِي الطَّبْعَةِ، وَشَرْحُ الزَّوْزَنِيِّ «وَجَذْبِي زِمَامَهَا إِلَيَّ» عَلَى التَّكَلُّمِ؛ وَعِنْدَ التِّبْرِيزِيِّ «شِئْتَ» بِالْفَتْحِ)",
  "the damma on the ta of «شِئْتُ» in vv. 38 and 39 (so the edition, and al-Zawzanī's «my drawing her rein to me» is in the first person; al-Tibrīzī has «شِئْتَ», «you»)",
  "38. ve 39. beyitlerdeki «شِئْتُ»nin tâ'sının dammesi (baskıda böyledir; Zevzenî'nin «yularını kendime çekmem» açıklaması birinci şahıstır; Tebrîzî'de fethayla «شِئْتَ»)"),
 (59, "إِعْرَابُ «الْمُتَوَرِّدِ» فِي الْبَيْتِ ٥٩ نَعْتًا لِـ«سِيدِ الْغَضَا» عَلَى مَعْنَى الزَّوْزَنِيِّ (وَجَعَلَهُ الدُّرَّةُ مِنْ صِفَاتِ الْفَرَسِ الْمَحْذُوفِ، وَهُوَ نَكِرَةٌ وَ«الْمُتَوَرِّدِ» مَعْرِفَةٌ)",
  "the parse of «الْمُتَوَرِّدِ» in v. 59 as an adjective of «سِيدِ الْغَضَا», after al-Zawzanī's sense (al-Durra makes it describe the omitted horse, which is indefinite while «الْمُتَوَرِّدِ» is definite)",
  "59. beyitteki «الْمُتَوَرِّدِ»nin Zevzenî'nin mânâsına göre «سِيدِ الْغَضَا»nın na'tı olarak i'râbı (Dürre onu mahzûf atın sıfatı sayar; oysa at nekire, «الْمُتَوَرِّدِ» marifedir)"),
 (67, "إِعْرَابُ «ثِنْيَاهُ» فِي الْبَيْتِ ٦٧ مُثَنًّى عَلَى تَفْسِيرِ الزَّوْزَنِيِّ «وَطَرَفَاهُ بِيَدِ صَاحِبِهِ» (وَعِنْدَ الدُّرَّةِ مُفْرَدٌ مَقْصُورٌ)",
  "the parse of «ثِنْيَاهُ» in v. 67 as a dual, after al-Zawzanī's «its two ends in its owner's hand» (al-Durra: a maqsur singular)",
  "67. beyitteki «ثِنْيَاهُ»nun Zevzenî'nin «iki ucu sahibinin elinde» açıklamasına göre tesniye olarak i'râbı (Dürre'ye göre maksûr müfred)"),
 (76, "إِعْرَابُ «غَدِي» فِي الْبَيْتِ ٧٦ ظَرْفًا كُسِرَتْ دَالُهُ وَوُلِّدَتْ يَاؤُهُ لِلْقَافِيَةِ عَلَى قَوْلِ الدُّرَّةِ (وَيُحْتَمَلُ أَنْ تَكُونَ الْيَاءُ يَاءَ الْمُتَكَلِّمِ: «غَدِي»)",
  "the parse of «غَدِي» in v. 76 as an adverb whose dal takes the rhyme's kasra, drawn out into a ya, after al-Durra (the ya may also be the speaker's: «my morrow»)",
  "76. beyitteki «غَدِي»nin Dürre'ye göre, dâl'ı kafiye için kesrelenip yâ'sı uzatmadan doğmuş bir zarf olarak i'râbı (yâ'nın mütekellim yâsı olması da muhtemeldir: «yarınım»)"),
 (86, "بَابُ «بَلَّتْ» فِي الْبَيْتِ ٨٦ (بَلَّ بِالشَّيْءِ: ظَفِرَ بِهِ؛ جُعِلَ مِنْ بَابِ سَمِعَ «يَبَلُّ»، وَلَمْ يَضْبِطْهُ الزَّوْزَنِيُّ)",
  "the bāb of «بَلَّتْ» in v. 86 (بَلَّ بِالشَّيْءِ, to get hold of a thing: set down as of bāb samiʿa, «يَبَلُّ»; al-Zawzanī does not vowel it)",
  "86. beyitteki «بَلَّتْ»in babı (بَلَّ بِالشَّيْءِ: ele geçirmek; semi'a babından «يَبَلُّ» olarak kaydedildi; Zevzenî harekelememiştir)"),
 (99, "نَصْبُ «وَيَوْمَ» فِي الْبَيْتِ ٩٩ (كَذَا فِي الطَّبْعَةِ، فَأُعْرِبَ مَفْعُولًا لِـ«اذْكُرْ» الْمَحْذُوفِ عَلَى أَحَدِ وَجْهَيِ الدُّرَّةِ؛ وَشَرْحُ الزَّوْزَنِيِّ «وَرُبَّ يَوْمٍ» عَلَى الْجَرِّ، وَيَجُوزُ عَلَيْهِ بِنَاءُ «يَوْمَ» عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى جُمْلَةٍ فِعْلُهَا مَاضٍ)",
  "the nasb of «وَيَوْمَ» in v. 99 (so the edition, and parsed as the object of an omitted «remember», one of al-Durra's two readings; al-Zawzanī's «and many a day» reads jarr, on which «يَوْمَ» may also be built on fatha, being annexed to a clause with a past verb)",
  "99. beyitteki «وَيَوْمَ»in nasbı (baskıda böyledir; Dürre'nin iki vechinden birine göre mahzûf «اذْكُرْ»un mef'ûlü olarak i'râb edildi; Zevzenî'nin «nice gün» açıklaması cerre göredir, buna göre «يَوْمَ» mâzî fiilli bir cümleye muzâf olduğundan fetha üzere mebnî de olabilir)"),
 # ==== SCHOLAR ABOVE ====
]
_corr = sorted((c for c in CORR if c[0] <= LAST), key=lambda c: c[0])
_sch = sorted((c for c in SCHOLAR if c[0] <= LAST), key=lambda c: c[0])
_whole = LAST == TOTAL
_runs_ar = "؛ ".join("الْفَصْلُ %s: %s–%s" % (ar_num(i), ar_num(a), ar_num(b)) for i, (a, b, t) in enumerate(READY, 2))
_runs_en = "; ".join("chapter %d: %d–%d" % (i, a, b) for i, (a, b, t) in enumerate(READY, 2))
_runs_tr = "; ".join("%d. bölüm: %d–%d" % (i, a, b) for i, (a, b, t) in enumerate(READY, 2))
_gap = LAST >= 22
ATTR_AR = (
 "نَصٌّ مُتَلَقًّى. الْفَصْلُ الْأَوَّلُ قِطْعَةٌ مُتَّصِلَةٌ بِحُرُوفِهَا مِنْ تَرْجَمَةِ طَرَفَةَ بْنِ الْعَبْدِ فِي «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةُ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ، ١/١٨٢ (الْفِقْرَتَانِ ٢٩٥ وَ٢٩٦): مِنْ «هُوَ طَرَفَةُ بْنُ الْعَبْدِ بْنِ سُفْيَانَ» إِلَى آخِرِ الْبَيْتَيْنِ «…عَسِيبٌ مِنْ سَرَارَةِ مَلْهَمَا»؛ وَتَتِمَّةُ الْخَبَرِ (بُلُوغُ الشِّعْرِ عَمْرَو بْنَ هِنْدٍ وَكِتَابُهُ إِلَى عَامِلِهِ بِالْبَحْرَيْنِ وَمَقْتَلُ طَرَفَةَ) لَمْ تُؤْخَذْ. "
 + ("وَسَائِرُ الْفُصُولِ هِيَ الْمُعَلَّقَةُ كَامِلَةً — %s أَبْيَاتٍ — " % ar_num(TOTAL) if _whole else "وَسَائِرُ الْفُصُولِ هِيَ الْمُعَلَّقَةُ مِنْ أَوَّلِهَا إِلَى الْبَيْتِ %s مِنْ %s (وَتَتْلُوهَا بَقِيَّةُ الْأَبْيَاتِ فِي فُصُولٍ لَاحِقَةٍ) — " % (ar_num(LAST), ar_num(TOTAL)))
 + "بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةُ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م، ص ٨٩–%s: نَصُّهُ وَتَرْتِيبُهُ وَعَدُّهُ، لَمْ يُتْرَكْ بَيْتٌ وَلَمْ يُتَخَطَّ مَوْضِعٌ. أَبْيَاتُ الْفُصُولِ: %s. وَالْقَصِيدَةُ مِنَ الطَّوِيلِ، وَرَوِيُّهَا الدَّالُ الْمَكْسُورَةُ. " % (ar_num(LAST_PAGE), _runs_ar)
 + ("وَالنَّصُّ الْإِلِكْتُرُونِيُّ لِشَرْحِ الزَّوْزَنِيِّ كَرَّرَ الصَّفْحَةَ ٩٨ فِي مَوْضِعِ الصَّفْحَةِ ٩٧، فَسَقَطَ مِنْهُ الْبَيْتَانِ ٢١ وَ٢٢ وَشَرْحُ الْأَبْيَاتِ ٢٠–٢٢ إِلَّا آخِرَهُ؛ فَأُخِذَ الْبَيْتَانِ مِنْ «شَرْحِ الْقَصَائِدِ الْعَشْرِ» لِلتِّبْرِيزِيِّ (ص ٦٦) وَمِنَ الدُّرَّةِ (١/١٩٧–١٩٩)، وَمَوْضِعُهُمَا ثَابِتٌ بِعَدِّ الزَّوْزَنِيِّ (٢٠ ثُمَّ ٢٣) وَبِمَا بَقِيَ مِنْ شَرْحِهِ لِلْبَيْتِ ٢٢. " if _gap else "")
 + "الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ طَبْعَةُ الزَّوْزَنِيِّ أُبْقِيَ عَلَى حَالِهِ (مَعَ تَوْحِيدِ الرَّسْمِ)، وَمَا تَرَكَتْهُ بِلَا شَكْلٍ ضَبَطَهُ الْمُحَرِّرُ بِدَلَالَةِ الْوَزْنِ وَالشَّرْحِ وَضَبْطِ التِّبْرِيزِيِّ؛ وَنَصُّ ابْنِ قُتَيْبَةَ لَيْسَ فِي طَبْعَتِهِ إِلَّا الشَّدَّاتُ، فَسَائِرُ شَكْلِهِ مِنَ الْمُحَرِّرِ، وَيَاؤُهُ الْمُتَطَرِّفَةُ الْمُهْمَلَةُ (فى، الحىّ) كُتِبَتْ يَاءً مَنْقُوطَةً. "
 + ("مَا خُولِفَ فِيهِ رَسْمُ النَّصِّ الْإِلِكْتُرُونِيِّ بِشَاهِدٍ: " + "؛ ".join(c[1] for c in _corr) + ". " if _corr else "")
 + "الْإِعْرَابُ رُوجِعَ كَلِمَةً كَلِمَةً عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهٰ الدُّرَّةِ (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م، ١/١٦٣–٣٢١)، وَكُتِبَ بِعِبَارَةِ هٰذَا الْمَشْرُوعِ، وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي؛ وَرِوَايَتُهُ مِئَةٌ وَعِشْرُونَ بَيْتًا يُخَالِفُ عَدُّهَا وَتَرْتِيبُهَا الزَّوْزَنِيَّ. وَالْمَعَانِي وَشَرْحُ الْغَرِيبِ وَالتَّرْجَمَةُ عَنِ الزَّوْزَنِيِّ. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ، وَكُلُّ وَجْهٍ عَلَى أَحَدِ أَصْلَيْنِ: أَنْ يُسَمِّيَهُ شَارِحٌ أَوْ يَصِفَهُ (الزَّوْزَنِيُّ، التِّبْرِيزِيُّ، الدُّرَّةُ)، أَوْ أَنْ يَنْطَبِقَ عَلَيْهِ حَدُّ التَّلْخِيصِ نَفْسِهِ فَيُقَالَ فِي سَطْرِهِ «عَلَى حَدِّ التَّلْخِيصِ»؛ وَلَمْ يَسْتَشْهِدِ التَّلْخِيصُ بِبَيْتٍ مِنْ هٰذِهِ الْمُعَلَّقَةِ. "
 + ("تُرِكَ لِنَظَرِ الْعَالِمِ: " + "؛ ".join(c[1] for c in _sch) + "." if _sch else ""))
ATTR_EN = (
 "A RECEIVED text. Chapter 1 is one contiguous span, verbatim, of the entry on Ṭarafa ibn al-ʿAbd in Ibn Qutayba (d. 276 AH), «الشعر والشعراء», the edition al-Maktaba al-Shāmila names Dār al-Ḥadīth, Cairo, 1423 AH, vol. 1 p. 182 (§§ 295–296) — from «هو طرفة بن العبد بن سفيان» to the end of the two verses «…عسيب من سرارة ملهما»; nothing is retold. The sequel of the report (the verses reach ʿAmr ibn Hind, his letter to his governor in al-Baḥrayn, the poet's death) is NOT included. "
 + ("The other chapters give the Muʿallaqa WHOLE — all %d verses — " % TOTAL if _whole else "The other chapters give the Muʿallaqa from its first verse to verse %d of %d (the remaining verses follow in later chapters) — " % (LAST, TOTAL))
 + "in the recension of al-Zawzanī (d. 486 AH), «شرح المعلقات السبع», Dār Iḥyāʾ al-Turāth al-ʿArabī, 1st ed. 1423 AH / 2002 CE, pp. 89–%d: his text, his order and his NUMBERING; no verse is left out and no run is skipped. The verses of each chapter — %s. The metre is al-ṭawīl; the rhyme-letter is a dāl with kasra. " % (LAST_PAGE, _runs_en)
 + ("THE E-TEXT'S GAP: the Shamela transcription of al-Zawzanī repeats printed p. 98 in the place of p. 97, so his verses 21 and 22 and his commentary on verses 20–22 (all but its last lines) are missing from it. The two verses are given from al-Tibrīzī, «شرح القصائد العشر» (p. 66, fully vowelled) and al-Durra (1/197–199); their place is fixed by al-Zawzanī's own numbering (20, then 23) and by what survives of his commentary on verse 22. " if _gap else "")
 + "VOWELLING, two layers: the vowels al-Zawzanī's edition prints are kept, normalised to the shelf's spelling; the letters it leaves bare are vowelled by the editor, as the metre, the commentary and al-Tibrīzī's vowelled text require. Ibn Qutayba's page prints only the shaddas — every other vowel in chapter 1 is editorial — and its undotted final yāʾ (فى، الحىّ) is written ي. "
 + ("DEPARTURES from the e-text's print, each against a witness (was → now): " + "; ".join(c[2] for c in _corr) + ". " if _corr else "")
 + "THE IʿRĀB of every verse token was checked against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب المعلقات العشر الطوال» (Maktabat al-Sawādī, Jidda, 2nd ed. 1409 AH / 1989 CE, vol. 1 pp. 163–321) and written in the shelf's own wording; where he gives two readings the first is given and the second mentioned. His recension has 120 verses and counts and orders them differently. The meanings, the glosses of the rare words and the translations follow al-Zawzanī; the amatory verses are translated plainly, as he explains them. THE FIGURES are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ, each on one of two bases: a commentator (al-Zawzanī, al-Tibrīzī, al-Durra) names or describes it, or it meets the Talkhīṣ's own definition exactly — and then its line says «by the Talkhīṣ's definition». The Talkhīṣ itself cites no verse of this Muʿallaqa. "
 + ("LEFT FOR THE SCHOLAR: " + "; ".join(c[2] for c in _sch) + "." if _sch else ""))
ATTR_TR = (
 "MERVÎ (alınmış) metin. 1. bölüm, İbn Kuteybe'nin (ö. 276 h.) «الشعر والشعراء» adlı eserindeki Tarafe b. el-Abd maddesinden kesintisiz ve harfiyen alınmış tek bir parçadır (el-Mektebetü'ş-Şâmile'nin Dârü'l-Hadîs, Kahire, 1423 h. olarak andığı baskı, 1/182, §§ 295–296): «هو طرفة بن العبد بن سفيان»dan «…عسيب من سرارة ملهما» ile biten iki beytin sonuna kadar; hiçbir şey yeniden anlatılmamıştır. Haberin devamı (şiirin Amr b. Hind'e ulaşması, Bahreyn'deki âmiline yazdığı mektup ve Tarafe'nin öldürülmesi) ALINMAMIŞTIR. "
 + ("Diğer bölümler Muallaka'yı BÜTÜNÜYLE — %d beytin tamamını — " % TOTAL if _whole else "Diğer bölümler Muallaka'yı ilk beytinden %d. beytine kadar (toplam %d beyit; kalan beyitler sonraki bölümlerde gelecektir) — " % (LAST, TOTAL))
 + "Zevzenî'nin (ö. 486 h.) rivayetiyle verir («شرح المعلقات السبع», Dâru İhyâi't-Türâsi'l-Arabî, 1. baskı 1423 h. / 2002 m., s. 89–%d): metin, sıra ve beyit NUMARALARI onundur; hiçbir beyit dışarıda bırakılmamış, hiçbir yer atlanmamıştır. Bölümlerin beyitleri — %s. Kasidenin vezni tavîl, revîsi kesreli dâldir. " % (LAST_PAGE, _runs_tr)
 + ("E-METİNDEKİ BOŞLUK: Zevzenî şerhinin Şâmile'deki metni, basılı 97. sayfanın yerinde 98. sayfayı tekrar eder; bu yüzden 21. ve 22. beyitler ile 20–22. beyitlerin şerhi (son satırları dışında) orada yoktur. Bu iki beyit Tebrîzî'nin tamamen harekeli «شرح القصائد العشر»inden (s. 66) ve Dürre'den (1/197–199) alınmıştır; yerleri Zevzenî'nin kendi numaralamasıyla (20, ardından 23) ve 22. beytin şerhinden kalan kısımla sabittir. " if _gap else "")
 + "HAREKELEME iki katmandır: Zevzenî baskısının bastığı harekeler korunmuş, yalnızca rafın imlâsına uydurulmuştur; baskının harekesiz bıraktığı harfleri editör, veznin, şerhin ve Tebrîzî'nin harekeli metninin gerektirdiği şekilde harekelemiştir. İbn Kuteybe'nin sayfasında yalnız şeddeler basılıdır — 1. bölümdeki diğer bütün harekeler editöre aittir — ve noktasız son yâ (فى، الحىّ) «ي» ile yazılmıştır. "
 + ("E-METNİN yazımından, her biri bir şahide dayanılarak AYRILINAN YERLER (eski → yeni): " + "; ".join(c[3] for c in _corr) + ". " if _corr else "")
 + "İ'RÂB: beyitlerdeki her kelimenin i'râbı Muhammed Ali Tâhâ ed-Dürre'nin «فتح الكبير المتعال إعراب المعلقات العشر الطوال» adlı eseriyle (Mektebetü's-Sevâdî, Cidde, 2. baskı 1409 h. / 1989 m., 1/163–321) karşılaştırılmış ve rafın kendi ifadesiyle yazılmıştır; iki vecih verdiği yerde birincisi esas alınmış, ikincisine işaret edilmiştir. Onun rivayeti 120 beyittir; beyitleri farklı sayar ve sıralar. Mânâlar, garîb kelimelerin açıklamaları ve çeviriler Zevzenî'ye dayanır; gazel beyitleri onun açıkladığı şekilde, sade bir dille çevrilmiştir. SANATLAR Kazvînî'nin Telhîsü'l-Miftâh'ındaki başlıklarla adlandırılmıştır; her sanat iki esastan birine dayanır: ya bir şârih (Zevzenî, Tebrîzî, Dürre) onu adlandırır yahut tarif eder, ya da Telhîs'in kendi tarifine tam olarak uyar — bu durumda satırda «Telhîs'in tarifine göre» denir. Telhîs'in kendisi bu Muallaka'dan hiçbir beyti şahit getirmez. "
 + ("ÂLİMİN NAZARINA BIRAKILANLAR: " + "; ".join(c[3] for c in _sch) + "." if _sch else ""))

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ طَرَفَةَ بْنِ الْعَبْدِ", "en": "The Muʿallaqa of Ṭarafa ibn al-ʿAbd", "tr": "Tarafe b. el-Abd'in Muallakası"},
 "subtitle": {"ar": "خَبَرُ الشَّاعِرِ عِنْدَ ابْنِ قُتَيْبَةَ، ثُمَّ مُعَلَّقَتُهُ بِرِوَايَةِ الزَّوْزَنِيِّ بَيْتًا بَيْتًا، مَعَ الْإِعْرَابِ وَالْبَلَاغَةِ",
              "en": "The poet's story from Ibn Qutayba, then his Muʿallaqa in al-Zawzanī's recension, verse by verse, with full iʿrāb and the figures of balāgha",
              "tr": "Şairin İbn Kuteybe'deki haberi, ardından Zevzenî rivayetiyle Muallakası — beyit beyit, tam i'râb ve belâgat sanatlarıyla"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {"ar": N(ATTR_AR), "en": ATTR_EN, "tr": ATTR_TR, "reviewStatus": "pending-scholarly-review"},
}
import shutil
if (PKG / "chapters").exists(): shutil.rmtree(PKG / "chapters")      # a chapter file from an earlier layout must not survive
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("published: khabar + verses 1–%d of %d (%d chapters); authored and waiting: %s" % (LAST, TOTAL, len(CHAPS), sorted(n for n in VERSE if n > LAST)))
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
