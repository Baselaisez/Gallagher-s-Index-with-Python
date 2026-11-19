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
       "la": ("اللَّامُ وَاقِعَةٌ فِي جَوَابِ «لَوْ»، وَ", "The lam stands in the answer of لَوْ; ", "Lâm «لَوْ»in cevabında gelen lâmdır; ", ("لَ", "la-jawab", "part")),
       "la-ibt": ("اللَّامُ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَ", "The lam is the lam of emphasis, slid on to the predicate; ", "Lâm, habere kaydırılmış te'kîd lâmıdır (lâm-ı müzahlaka); ", ("لَ", "la-ibtida", "part")),
       "la-qasam": ("اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَ", "The lam stands in the answer of the oath; ", "Lâm kasemin cevabında gelen lâmdır; ", ("لَ", "la-jawab", "part")),
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
