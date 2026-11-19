"""Author content/samples/siyar-abi-hanifa — «مِنْ سِيرَةِ أَبِي حَنِيفَةَ», a RECEIVED text at Level 5 (Advanced).

RECEIVED TEXT, VERBATIM: six contiguous spans of al-Dhahabī's entry on Imam Abū Ḥanīfa al-Nuʿmān ibn Thābit (no. 163) in
«سِيَرُ أَعْلَامِ النُّبَلَاءِ» (the Muʾassasat al-Risāla edition as al-Maktaba al-Shāmila carries it, book 10906), vol. 6,
pp. 390–403. The spans, in the entry's own order (each chapter is ONE span — it may stop early, it never skips):

  ch1  6/390–391  the opening of the entry: his name and lineage, his birth, whom he saw and narrated from — to «وَلَمْ يَصِحَّ»
  ch2  6/394      his line and his trade: al-ʿIjlī, ʿUmar ibn Ḥammād, and three of the reports of where his father came from
  ch3  6/395      Yaḥyā ibn Maʿīn's four statements on him, the last with Ibn Hubayra's beating over the judgeship
  ch4  6/399      Abū Yūsuf's khabar of the night vigil, the Qurʾān in one rakʿa, the old man giving fatwā in Kufa's mosque
  ch5  6/401      Bishr ibn al-Walīd's khabar: al-Manṣūr, the two oaths, the prison
  ch6  6/403      Ibn al-Mubārak and al-Shāfiʿī on his fiqh, al-Dhahabī's own verdict and verse, his death

THE TWO VOWELLING LAYERS. The edition is vowelled, though not on every letter. Its vowels are kept and normalised to the
shelf's spelling (no sukūn on a madd letter, fatḥa before the alif, tanwīn fatḥ before its alif, sukūn on the lām of the
qamarī article, the dagger alif of هٰذَا and الرَّحْمٰن, بْنُ with its sukūn, NFC). Where the edition leaves a letter bare the
vowel is editorial (the list is in the manifest attribution). No word is changed, added or dropped; the edition's colon
after عَنْ / وُلِدَ / رَأَى / رَوَى and after a topic (أَبُو حَنِيفَةَ: تَيْمِيٌّ) is not carried over, and its hyphens are set as dashes.

The verbatim page text lives in research/sources/siyar-abi-hanifa-src.txt.  Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_siyar_abi_hanifa.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "siyar-abi-hanifa"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

PRON.update({"هِمُ": "pron-3mp", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُ": "pron-3ms", "هِ": "pron-3ms", "نَا": "pron-1p", "ي": "pron-1s"})
PRON_AR.update({"هِمُ": "هُمْ", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "نَا": "نَا", "ي": "الْيَاءُ"})

# ---- the clause seats and the standing notes (ar, en, tr) ---------------------------------------------------------------
Z = ("", "", "")
def cat(*ts): return tuple("".join(t[i] for t in ts) for i in range(3))
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
MAQUL_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekûlü'l-kavl olarak mahallen mansûb")
DROP = (" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ", " — it loses its tanwin because it is described by «ibn» annexed to a name", " — alem'e muzâf «ibn» ile vasıflandığı için tenvini düşmüştür")
SILA_T = SILA
AID = ("، وَالْعَائِدُ مَحْذُوفٌ", "; the pronoun that returns to the relative is left unsaid", "; âid zamiri hazfedilmiştir")
DG = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
D_TA = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", " — a man's name with the feminine ta, barred from tanwin: the fatha stands for the kasra", " — lafzen müennes (tâ'lı) alem, gayr-i munsarif; kesre yerine fetha ile")
D_AJ = ("، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", " — a foreign proper name, barred from tanwin: the fatha stands for the kasra", " — yabancı özel isim, gayr-i munsarif; kesre yerine fetha ile")
D_AJ_R = ("، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ فَلَا يُنَوَّنُ", " — a foreign proper name, barred from tanwin", " — yabancı özel isim, gayr-i munsarif; tenvin almaz")
D_BALAD = ("، عَلَمٌ عَلَى بَلْدَةٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a town's name, feminine and proper, barred from tanwin: the fatha stands for the kasra", " — şehir adı; alemiyyet ve te'nîs sebebiyle gayr-i munsarif, kesre yerine fetha ile")
D_FIL_R = ("، عَلَمٌ عَلَى وَزْنِ الْفِعْلِ مَمْنُوعٌ مِنَ الصَّرْفِ فَلَا يُنَوَّنُ", " — a proper name on the pattern of a verb, barred from tanwin", " — fiil vezninde alem, gayr-i munsarif; tenvin almaz")
JM = lambda seat_ar, seat_en, seat_tr: ("، وَالْجَارُّ وَالْمَجْرُورُ " + seat_ar, "; the jarr phrase " + seat_en, "; câr-mecrûr " + seat_tr)
JM_KHABAR = JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ", "hangs on an omitted word that is the khabar", "mahzûf habere müteallik")
JM_KH_INNA = JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ إِنَّ", "hangs on an omitted word that is the predicate of إِنَّ", "inne'nin mahzûf haberine müteallik")
JM_KH_KANA = JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ", "hangs on an omitted word that is the predicate of كَانَ", "kâne'nin mahzûf haberine müteallik")
def NAAT_OF(seat, of_ar, of_en, of_tr):
    """the clause is the na't of a named indefinite noun"""
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return (" — وَالْجُمْلَةُ فِي مَحَلِّ " + s[0] + " نَعْتٌ لِـ«" + of_ar + "»", "; the clause qualifies «" + of_en + "», in the seat of " + s[1], "; cümle «" + of_tr + "» için na't, mahallen " + s[2])

def ISTI(t):
    """the waw that opens a sentence after a full stop is the waw of resumption, not a conjunction"""
    ir = t["irab"]
    assert ir["ar"].startswith(WA_AR) and ir["en"].startswith("The waw conjoins; ") and ir["tr"].startswith("«ve» + "), ir
    ir["ar"] = "الْوَاوُ لِلِاسْتِئْنَافِ، وَ" + ir["ar"][len(WA_AR):]
    ir["en"] = "The waw opens a new sentence; " + ir["en"][len("The waw conjoins; "):]
    ir["tr"] = "Vâv isti'nâf içindir; " + ir["tr"][len("«ve» + "):]
    t["grammar"] = [g for g in t.get("grammar", []) if g != "atf-nasaq"] + ["anwa-al-waw"]
    return t
def N3(n): return {"note_ar": n[0], "note_en": n[1], "note_tr": n[2]}

# ---- the plain seats, each with a note triple -----------------------------------------------------------------------------
def F(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالضَّمَّةِ"): return FAIL(full, lex, pos, extra, n[0], n[1], n[2], punct, None, sign)
def O(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالْفَتْحَةِ"): return MAFUL(full, lex, pos, extra, n[0], n[1], n[2], punct, None, sign)
def MI(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالْكَسْرَةِ"): return MUDAF_ILAYH(full, lex, pos, extra, sign, n[0], n[1], n[2], punct)
def J(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالْكَسْرَةِ"): return MAJR(full, lex, pos, extra, n[0], n[1], n[2], punct, None, sign)
def MB(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالضَّمَّةِ"): return MUBTADA(full, lex, pos, extra, punct, n[0], n[1], n[2], sign)
def MBM(full, lex, n=Z, extra=None, punct=None, sign="بِالضَّمَّةِ"):
    """the mubtada that comes after its fronted khabar"""
    return tok(full, lex, "noun", ["mubtada-khabar", "taqdim-al-musnad"] + (extra or []), "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ " + sign + n[0] + ".",
        "The mubtada, placed after its khabar, in raf'" + n[1] + ".", "Haberinden sonra gelmiş mübtedâ, merfû" + n[2] + ".", punct=punct)
def KB(full, lex, n=Z, extra=None, punct=None, sign="بِالضَّمَّةِ"): return KHABAR(full, lex, extra, punct, n[0], n[1], n[2], sign)
def IK(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالضَّمَّةِ"): return ISMK(full, lex, pos, extra, n[0], n[1], n[2], punct, None, sign)
def KK(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالْفَتْحَةِ"): return KHK(full, lex, pos, extra, n[0], n[1], n[2], punct, None, sign)
CASE = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr", "mecrûr")}
def NA(full, lex, case, of=None, n=Z, pos="noun", extra=None, punct=None, nth=None, sign=None):
    """a na't: of = (ar, en, tr) names the noun it describes; nth = 'ثَانٍ' / 'ثَالِثٌ' for a second or third na't"""
    c = CASE[case]
    nth_t = {None: ("", "", "", "Na't (sıfat)"), "2": ("ثَانٍ ", "second ", "ikinci ", "İkinci na't (sıfat)"), "3": ("ثَالِثٌ ", "third ", "üçüncü ", "Üçüncü na't (sıfat)")}[nth]
    return tok(full, lex, pos, ["naat-sifa"] + (extra or []),
        "نَعْتٌ " + nth_t[0] + (("لِـ«" + of[0] + "» ") if of else "") + (sign or c[0]) + n[0] + ".",
        ("A " + nth_t[1] if nth else "An ") + "adjective (na't)" + ((" of «" + of[1] + "»") if of else "") + ", agreeing with its noun, in " + c[1] + n[1] + ".",
        (("«" + of[2] + "» isminin " + nth_t[2] + "na'tı") if of else nth_t[3]) + ", mevsûfuna uyar; " + c[2] + n[2] + ".", punct=punct)
def BN(case, of_ar, of_en, of_tr, punct=None):
    """بْنُ / بْنَ / بْنِ between two names: a na't of the first name, annexed to the second; its alif is dropped in writing"""
    full = {"raf": "بْنُ", "nasb": "بْنَ", "jarr": "بْنِ"}[case]; c = CASE[case]
    return tok(full, "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
        "نَعْتٌ لِـ«" + of_ar + "» " + c[0] + "، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
        "An adjective (na't) of «" + of_en + "», in " + c[1] + " and annexed — its alif is dropped in writing because it stands between two names.",
        "«" + of_tr + "» isminin na'tı, " + c[2] + ", muzâf — iki alem arasında geldiği için elifi yazıda düşer.", punct=punct)
HANIFA = lambda punct=None: tok("حَنِيفَةَ", "hanifa", "propn", ["idafa-definiteness"] + DG,
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.",
    "The second term of the idafa, in jarr — the fatha stands for the kasra: a proper name with the feminine ta, barred from tanwin.",
    "Muzâfun ileyh, mecrûr — alemiyyet ve te'nîs sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile.", punct=punct)
AB_HEAD = {
 "ismk": ("اسْمُ كَانَ مَرْفُوعٌ", "The noun of كَانَ, in raf'", "Kâne'nin ismi, merfû", ["kana-wa-akhawatuha"]),
 "mubtada": ("مُبْتَدَأٌ مَرْفُوعٌ", "The mubtada, in raf'", "Mübtedâ, merfû", ["mubtada-khabar"]),
 "fail": ("فَاعِلٌ مَرْفُوعٌ", "The doer (fa'il), in raf'", "Fâil, merfû", ["fail"]),
 "khabar": ("خَبَرٌ مَرْفُوعٌ", "The predicate (khabar), in raf'", "Haber, merfû", ["mubtada-khabar"]),
 "mi": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", ["idafa-definiteness"]),
 "majr": ("مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", ["huruf-jarr"]),
 "maful": ("مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", ["maful-bihi"]),
 "ism_anna": ("اسْمُ أَنَّ مَنْصُوبٌ", "The noun of أَنَّ, in nasb", "Enne'nin ismi, mansûb", ["inna-wa-akhawatuha"]),
 "badal_raf": ("بَدَلٌ مِنَ «الْإِمَامُ» مَرْفُوعٌ", "A badal of «the Imam», in raf'", "«İmam»dan bedel, merfû", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"]),
 "badal_jarr": ("بَدَلٌ مِنَ «الْقَاضِي» مَجْرُورٌ", "A badal of «the qāḍī», in jarr", "«Kadı»dan bedel, mecrûr", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"]),
}
def AB(full, role, n=Z, punct=None):
    """أَبُو / أَبَا / أَبِي — one of the five nouns, always annexed here (the kunya)"""
    letter = {"أَبُو": ("بِالْوَاوِ", "by the waw", "vâv ile"), "أَبَا": ("بِالْأَلِفِ", "by the alif", "elif ile"), "أَبِي": ("بِالْيَاءِ", "by the ya", "yâ ile")}[full]
    h = AB_HEAD[role]
    return tok(full, "ab", "noun", h[3] + ["five-nouns", "idafa-definiteness"],
        h[0] + " " + letter[0] + " لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ" + n[0] + ".",
        h[1] + " " + letter[1] + " — one of the five nouns; annexed" + n[1] + ".",
        h[2] + " — esmâ-i hamseden olduğu için " + letter[2] + "; muzâf" + n[2] + ".", punct=punct)
ALLAH_MI = lambda punct=None: MI("اللهِ", "allah", (" — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl"), "propn", punct=punct)
BANI_T = ("بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " by the ya — it declines like the sound masculine plural, and its nun drops in the idafa; annexed", " — cem-i müzekker sâlime mülhak olduğu için yâ ile; nûnu izâfetten dolayı düşmüştür; muzâf")
def LI_BANI(n=Z, punct=None):
    return tok("لِبَنِي", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim", "idafa-definiteness"],
        "اللَّامُ حَرْفُ جَرٍّ، وَبَنِي مَجْرُورٌ " + BANI_T[0] + n[0] + ".",
        "The lam is a jarr letter; «the sons of» is in jarr" + BANI_T[1] + n[1] + ".",
        "Lâm cer harfi; «oğulları» mecrûr" + BANI_T[2] + n[2] + ".", punct=punct, segments=[seg("لِ", "li", "prep"), seg("بَنِي", "banu", "noun")])
AN_PREP = lambda n=Z, punct=None: PREP("عَنْ", "an", n[0], n[1], n[2], gloss_tr="«-den»", punct=punct)
AN_K = lambda: AN_KASRA()
RAWI = JM("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ، أَيْ: نَاقِلًا عَنْهُ", "hangs on an omitted hal: «transmitting from him»", "mahzûf bir hâle müteallik: «ondan naklederek»")
def MINP(n=Z, punct=None): return PREP("مِنْ", "min", n[0], n[1], n[2], gloss_tr="«-den»", punct=punct)
def FIP(n=Z): return PREP("فِي", "fi", n[0], n[1], n[2], gloss_tr="«-de»")
def ALAP(n=Z): return PREP("عَلَى", "ala", n[0], n[1], n[2], gloss_tr="«üzerine»")
def ILAP(n=Z): return PREP("إِلَى", "ila", n[0], n[1], n[2], gloss_tr="«-e»")
def ANNA_T(role=Z):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna", "mawadi-fath-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".",
        "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
KH_ANNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
LA_JINS = lambda: tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"],
    "لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ إِنَّ: تَنْصِبُ الِاسْمَ وَتَرْفَعُ الْخَبَرَ.",
    "The لَا that denies the whole kind; it governs like إِنَّ — its noun in nasb, its predicate in raf'.",
    "Cinsi nefyeden lâ; inne gibi amel eder: ismini nasb, haberini ref eder.")
def ISM_LA(full, lex, punct=None):
    return tok(full, lex, "noun", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"],
        "اسْمُ لَا النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، لِأَنَّهُ مُفْرَدٌ نَكِرَةٌ.",
        "The noun of the لَا that denies the kind: built on fatha, in the seat of nasb — a single indefinite noun, so it takes no tanwin.",
        "Cinsi nefyeden lâ'nın ismi: müfred nekre olduğu için fetha üzere mebnî, mahallen mansûb.", punct=punct)
def HADHA(seat_ar, seat_en, seat_tr, extra=None, punct=None):
    return ISHARA("هٰذَا", "hadha", seat_ar, seat_en, seat_tr, extra=extra, punct=punct)
def MAJHUL_M(full, lex, sign_ar, sign_en, sign_tr, who="هُوَ", extra=None, punct=None, n=Z, naib=True):
    """a present verb in the passive: sign_* states its case and sign"""
    hid = ("، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: " + who, "; its deputy doer is a hidden pronoun «" + who + "»", "; nâib-i fâili gizli zamir «" + who + "»") if naib else Z
    return tok(full, lex, "verb", ["naib-al-fail", "al-majhul-fil-kafiya"] + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ " + sign_ar + hid[0] + n[0] + ".",
        "A present verb in the passive, " + sign_en + hid[1] + n[1] + ".",
        "Meçhul muzâri, " + sign_tr + hid[2] + n[2] + ".", punct=punct)
NAIB_HID = ("، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", "; its deputy doer is a hidden pronoun «he»", "; nâib-i fâili gizli zamir «o»")
def W(full, lex, pos, grammar, rest_ar, rest_en, rest_tr, kind="atf", punct=None, stem_lex=None, extra_segs=None):
    """a token that opens with وَ: kind = atf | isti | hal"""
    k = {"atf": (WA_AR, "The waw conjoins; ", "«ve» + ", ["atf-nasaq"]),
         "isti": ("الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "The waw opens a new sentence; ", "Vâv isti'nâf içindir; ", ["anwa-al-waw"]),
         "hal": ("الْوَاوُ حَالِيَّةٌ، وَ", "The waw opens a hal clause; ", "Hâl vâvı; ", ["al-hal-jumla-wa-rabituha", "anwa-al-waw"])}[kind]
    return tok(full, lex, pos, grammar + k[3], k[0] + rest_ar, k[1] + rest_en, k[2] + rest_tr, punct=punct,
               segments=[seg("وَ", "wa", "conj")] + (extra_segs or [seg(full[2:], stem_lex or lex, pos)]))
def FA(full, lex, pos, grammar, rest_ar, rest_en, rest_tr, punct=None, segs=None, head=(FA_AR, "The fa conjoins; ", "«bunun üzerine» + ")):
    return tok(full, lex, pos, grammar, head[0] + rest_ar, head[1] + rest_en, head[2] + rest_tr, punct=punct, segments=[seg("فَ", "fa", "conj")] + (segs or [seg(full[2:], lex, pos)]))
QALA_ISTI = lambda punct=None, hidden=False: ISTI(QALA("وَقَالَ", hidden=hidden, punct=punct))
RAWA_ISTI = lambda: ISTI(MADI_ALIF("وَرَوَى", "rawa", note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili ondan sonra gelir"))
QALA_HID = lambda punct=":": QALA("قَالَ", hidden=True, punct=punct)

TITLES = [{"ar": "الْإِمَامُ أَبُو حَنِيفَةَ", "en": "The Imam Abū Ḥanīfa", "tr": "İmam Ebû Hanîfe"},
          {"ar": "أَصْلُهُ وَصَنْعَتُهُ", "en": "His Origin and His Trade", "tr": "Aslı ve Mesleği"},
          {"ar": "قَوْلُ ابْنِ مَعِينٍ فِيهِ", "en": "Ibn Maʿīn's Word on Him", "tr": "İbn Maîn'in Onun Hakkındaki Sözü"},
          {"ar": "قِيَامُ اللَّيْلِ", "en": "The Night Vigil", "tr": "Gece İbadeti"},
          {"ar": "الْمَنْصُورُ وَالْقَضَاءُ", "en": "Al-Manṣūr and the Judgeship", "tr": "Mansûr ve Kadılık"},
          {"ar": "فِقْهُهُ وَوَفَاتُهُ", "en": "His Fiqh and His Death", "tr": "Fıkhı ve Vefatı"}]

# ================================================ Chapter 1 — الْإِمَامُ أَبُو حَنِيفَةَ (6/390–391) ================================================
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "The Imam, the jurist of the community, the scholar of Iraq: Abū Ḥanīfa al-Nuʿmān ibn Thābit ibn Zūṭā, the Taymī, the Kufan, client of the Banū Taym Allāh ibn Thaʿlaba.",
  "tr": "İmam, ümmetin fakihi, Irak'ın âlimi: Ebû Hanîfe Nu'mân b. Sâbit b. Zûtâ et-Teymî el-Kûfî; Teymullah b. Sa'lebe oğullarının mevlâsı."},
 "tokens": [
  tok("الْإِمَامُ", "imam", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"],
    "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ، مَرْفُوعٌ بِالضَّمَّةِ — هٰكَذَا تُفْتَتَحُ التَّرَاجِمُ بِأَوْصَافِ صَاحِبِهَا.",
    "The predicate (khabar) of a dropped mubtada — «he is» — in raf' by the damma: this is how a biographical entry opens, with the titles of its subject.",
    "Hazfedilmiş mübtedânın («o») haberi, damme ile merfû — terceme (biyografi) maddeleri sahibinin vasıflarıyla böyle açılır.", punct="،"),
  tok("فَقِيهُ", "faqih", "noun", ["mubtada-khabar", "idafa-definiteness", "sifa-mushabbaha"],
    "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A second predicate (khabar), in raf', annexed.", "İkinci haber, merfû, muzâf."),
  MI("الْمِلَّةِ", "milla", punct="،"),
  tok("عَالِمُ", "alim-scholar", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-fail"],
    "خَبَرٌ ثَالِثٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A third predicate (khabar), in raf', annexed.", "Üçüncü haber, merfû, muzâf."),
  MI("الْعِرَاقِ", "iraq", pos="propn", punct="،"),
  AB("أَبُو", "badal_raf", (" — وَهُوَ كُنْيَتُهُ", " — it is his kunya", " — bu onun künyesidir")), HANIFA(),
  tok("النُّعْمَانُ", "numan", "propn", ["badal", "atf-bayan", "al-badal-wa-aqsamuh-wa-atf-al-bayan"],
    "بَدَلٌ مِنْ «أَبُو حَنِيفَةَ» مَرْفُوعٌ بِالضَّمَّةِ، وَيَجُوزُ أَنْ يَكُونَ عَطْفَ بَيَانٍ — وَهُوَ اسْمُهُ بَعْدَ كُنْيَتِهِ.",
    "A badal of «Abū Ḥanīfa», in raf' by the damma (it may also be read as an explanatory apposition, ʿaṭf bayān) — his given name, after his kunya.",
    "«Ebû Hanîfe»den bedel, damme ile merfû (atf-ı beyân da olabilir) — künyesinden sonra gelen ismidir."),
  BN("raf", "النُّعْمَانُ", "al-Nuʿmān", "Nu'mân"),
  MI("ثَابِتِ", "thabit-name", DROP, "propn"),
  BN("jarr", "ثَابِتِ", "Thābit", "Sâbit"),
  MI("زُوطَى", "zuta", (" — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ، وَهُوَ مَقْصُورٌ فَتُقَدَّرُ الْحَرَكَةُ عَلَى أَلِفِهِ", " — a foreign name, barred from tanwin; it ends in alif maqṣūra, so its case-vowel is estimated on the alif", " — yabancı özel isim, gayr-i munsarif; maksûr olduğu için harekesi elif üzerinde takdîrîdir"),
     "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ نِيَابَةً عَنِ الْكَسْرَةِ"),
  NA("التَّيْمِيُّ", "taymi", "raf", ("النُّعْمَانُ", "al-Nuʿmān", "Nu'mân"), (" — اسْمٌ مَنْسُوبٌ إِلَى تَيْمِ اللهِ بِالْوَلَاءِ", " — a nisba to Taym Allāh, by clientage", " — velâ yoluyla Teymullah'a nisbet"), extra=["ism-mansub"], punct="،"),
  NA("الْكُوفِيُّ", "kufi", "raf", None, (" — مَنْسُوبٌ إِلَى الْكُوفَةِ", " — a nisba to Kufa", " — Kûfe'ye nisbet"), extra=["ism-mansub"], punct="،", nth="2"),
  tok("مَوْلَى", "mawla", "noun", ["naat-sifa", "ism-maqsur-manqus", "idafa-definiteness"],
    "نَعْتٌ ثَالِثٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ — وَالْمَوْلَى هُنَا مَنْ يَنْتَسِبُ إِلَى الْقَبِيلَةِ بِالْوَلَاءِ لَا بِالنَّسَبِ.",
    "A third adjective (na't), in raf' by a damma estimated on the alif; annexed — «mawlā» here is the client: one who belongs to the tribe by the tie of walāʾ, not by descent.",
    "Üçüncü na't, elif üzerinde takdîrî damme ile merfû; muzâf — burada «mevlâ», kabileye nesep yoluyla değil velâ bağıyla mensup olan kimsedir."),
  tok("بَنِي", "banu", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + BANI_T[0] + ".", "The second term of the idafa, in jarr" + BANI_T[1] + ".", "Muzâfun ileyh, mecrûr" + BANI_T[2] + "."),
  MI("تَيْمِ", "taym", MUDAF, "propn"), ALLAH_MI(),
  BN("jarr", "تَيْمِ اللهِ", "Taym Allāh", "Teymullah"),
  MI("ثَعْلَبَةَ", "thalaba", D_TA, "propn", DG, sign=FATHA_JARR, punct=".")]})
S1.append({"id": "s2", "translation": {"en": "It is said that he was of the sons of the Persians.", "tr": "Onun Fârisîlerin soyundan olduğu söylenir."},
 "tokens": [
  tok("يُقَالُ", "qala", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "hollow-verbs", "mudari-marfu"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ جُمْلَةُ مَقُولِ الْقَوْلِ بَعْدَهُ (إِنَّهُ…) فِي مَحَلِّ رَفْعٍ — وَأَصْلُهُ يُقْوَلُ: نُقِلَتْ فَتْحَةُ الْوَاوِ إِلَى الْقَافِ ثُمَّ قُلِبَتِ الْوَاوُ أَلِفًا.",
    "A present verb in the passive, in raf' by the damma; its deputy doer is the quoted clause after it («that he…»), in the seat of raf' — from يُقْوَلُ: the waw's fatha moved back onto the qaf and the waw turned into alif.",
    "Meçhul muzâri, damme ile merfû; nâib-i fâili ardından gelen mekûlü'l-kavl cümlesidir («onun … olduğu»), mahallen merfû — aslı يُقْوَلُ: vâvın fethası kâfa nakledilmiş, vâv elife çevrilmiştir.", punct=":"),
  tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna", "al-bariz-al-muttasil"],
    "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — كُسِرَتْ هَمْزَتُهَا لِأَنَّهَا فِي أَوَّلِ الْجُمْلَةِ الْمَحْكِيَّةِ بِالْقَوْلِ — وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.",
    "إِنَّ is the particle of emphasis that puts its noun in nasb — its hamza takes kasra because it opens a clause quoted after «say»; the attached «he» is its noun, built on damma in the seat of nasb.",
    "İnne te'kîd ve nasb harfi — kavl'den sonra nakledilen cümlenin başında olduğu için hemzesi kesrelidir; bitişik «o» zamiri ismi, damme üzere mebnî, mahallen mansûb.",
    segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  MINP(JM_KH_INNA),
  J("أَبْنَاءِ", "ibn", cat(MUDAF, (" — جَمْعُ ابْنٍ", " — the broken plural of ابْن", " — ibn'in cem-i teksîri")), extra=["jam-taksir", "idafa-definiteness"]),
  MI("الْفُرْسِ", "furs", punct=".")]})

S1.append({"id": "s3", "translation": {"en": "He was born in the year eighty, in the lifetime of the younger Companions.", "tr": "Seksen yılında, küçük sahâbîlerin hayatta olduğu dönemde doğdu."},
 "tokens": [
  MAJHUL("وُلِدَ", "walada", ["mithal-verbs"], note_ar=NAIB_HID[0], note_en=NAIB_HID[1], note_tr=NAIB_HID[2]),
  ZARF("سَنَةَ", "sana", "زَمَانٍ", "time", "Zaman"),
  MI("ثَمَانِينَ", "thamanun", (" — مِنْ أَلْفَاظِ الْعُقُودِ؛ أَيْ سَنَةَ ثَمَانِينَ مِنَ الْهِجْرَةِ", " — one of the tens, which decline like the sound masculine plural; that is, year 80 of the Hijra", " — ukûd lafızlarındandır, cem-i müzekker sâlim gibi i'râblanır; yani hicretin 80. yılı"),
     extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", punct="،"),
  FIP(), J("حَيَاةِ", "hayat", MUDAF, extra=["idafa-definiteness"]),
  MI("صِغَارِ", "saghir", cat(MUDAF, (" — جَمْعُ صَغِيرٍ؛ وَصِغَارُ الصَّحَابَةِ: مَنْ كَانُوا أَحْدَاثًا فِي عَهْدِ النَّبِيِّ ﷺ فَتَأَخَّرَتْ وَفَاتُهُمْ", " — the plural of صَغِير; «the younger Companions» are those who were young in the Prophet's time ﷺ and so died late", " — sağîr'in cem'i; «küçük sahâbîler»: Hz. Peygamber ﷺ zamanında yaşça küçük olup geç vefat edenler")), extra=["jam-taksir"]),
  MI("الصَّحَابَةِ", "sahaba", punct=".")]})

S1.append({"id": "s4", "translation": {
  "en": "He saw Anas ibn Mālik when he came to them at Kufa; yet not a single word is established as his from any of them.",
  "tr": "Enes b. Mâlik'i, Kûfe'ye yanlarına geldiğinde gördü; fakat onlardan hiçbirinden tek bir kelime (rivayet) ettiği sabit olmamıştır."},
 "tokens": [
  ISTI(MADI_ALIF("وَرَأَى", "raa", hidden=True)),
  O("أَنَسَ", "anas", DROP, "propn"), BN("nasb", "أَنَسَ", "Anas", "Enes"), MI("مَالِكٍ", "malik-name", pos="propn"),
  LAMMA2("لَمَّا"),
  MADI("قَدِمَ", "qadima", hidden=True, **N3(cat((" (أَنَسٌ)", " (Anas)", " (Enes)"), LAMMA_CL))),
  JARR_PRON("عَلَيْهِمُ", "ala", "عَلَيْ", "هِمُ", " («onların yanına»)", note_ar="، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en="; the mim takes a damma before the following ال, where two quiescents meet", note_tr="; iki sâkin karşılaştığı için mîm damme ile harekelendi"),
  O("الْكُوفَةَ", "kufa", (" — قَدِمَ يَتَعَدَّى إِلَى الْمَكَانِ بِنَفْسِهِ", " — قَدِمَ takes the place it comes to as its direct object", " — «kadime» fiili varılan yeri doğrudan mef'ûl alır"), "propn", punct="،"),
  WA_LAM(),
  JAZM_V("يَثْبُتْ", "thabata"),
  LAHU("لَهُ", "pron-3ms", " («onun için»)"),
  F("حَرْفٌ", "harf", (" — أَيْ كَلِمَةٌ وَاحِدَةٌ مِنَ الرِّوَايَةِ", " — «a letter», that is, a single word of narration", " — «bir harf», yani rivayetten tek bir kelime")),
  AN_PREP(), J("أَحَدٍ", "ahad"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", punct=".", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«أَحَدٍ»؛ وَالضَّمِيرُ لِلصَّحَابَةِ", note_en="; the jarr phrase qualifies «anyone», in the seat of jarr; «them» are the Companions", note_tr="; câr-mecrûr «kimse» için na't, mahallen mecrûr; zamir sahâbeye döner")]})

S1.append({"id": "s5", "translation": {
  "en": "He narrated from ʿAṭāʾ ibn Abī Rabāḥ — who was the eldest shaykh he had, and the best of them, by his own word.",
  "tr": "Atâ b. Ebî Rebâh'tan rivayet etti; o, hocalarının en yaşlısı ve — kendi ifadesine göre — en faziletlisiydi."},
 "tokens": [
  ISTI(MADI_ALIF("وَرَوَى", "rawa", hidden=True)),
  AN_PREP(),
  J("عَطَاءِ", "ata-name", DROP, "propn", ["ism-mamdud"]),
  BN("jarr", "عَطَاءِ", "ʿAṭāʾ", "Atâ"), AB("أَبِي", "mi"), MI("رَبَاحٍ", "rabah", pos="propn", punct="،"),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"),
  KB("أَكْبَرُ", "akbar", (" بِلَا تَنْوِينٍ لِأَنَّهُ مُضَافٌ — اسْمُ تَفْضِيلٍ مُضَافٌ إِلَى نَكِرَةٍ", ", annexed, so with no tanwin — an elative annexed to an indefinite noun", ", muzâf olduğu için tenvinsiz — nekreye muzâf ism-i tafdîl"), ["ism-tafdil", "idafa-definiteness"]),
  MI("شَيْخٍ", "shaykh"),
  LAHU2("لَهُ", "pron-3ms", " («onun»)", punct="،", note=JM("فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«شَيْخٍ»", "qualifies «a shaykh», in the seat of jarr", "«şeyh» için na't, mahallen mecrûr")),
  tok("وَأَفْضَلُهُمْ", "afdal", "noun", ["atf-nasaq", "ism-tafdil", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "أَفْضَلُ مَعْطُوفٌ عَلَى «أَكْبَرُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يَعُودُ عَلَى شُيُوخِهِ.",
    "The waw conjoins; «the best» is conjoined to «the eldest», in raf' and annexed; the attached «them» is the second term of the idafa, in the seat of jarr — it returns to his shaykhs.",
    "«ve» + «en faziletli», «en yaşlı»ya ma'tûf, merfû, muzâf; bitişik «onlar» zamiri muzâfun ileyh, mahallen mecrûr — hocalarına döner.", punct=" —",
    segments=[seg("وَ", "wa", "conj"), seg("أَفْضَلُ", "afdal", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  ALAP(),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr", "anwa-ma"],
    "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِعَلَى — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ، أَيْ: ذٰلِكَ كَائِنٌ عَلَى مَا قَالَ.",
    "A relative pronoun «what», built on sukun, in the seat of jarr after عَلَى — the jarr phrase hangs on a word left unsaid: «(that is so) according to what he said».",
    "İsm-i mevsûl «şey», sükûn üzere mebnî, alâ ile mahallen mecrûr — câr-mecrûr mahzûfa müteallik: «(bu,) onun söylediğine göredir»."),
  MADI("قَالَ", "qala", ["hollow-verbs"], hidden=True, punct=" —.", **N3(cat((" (أَبُو حَنِيفَةَ)", " (Abū Ḥanīfa)", " (Ebû Hanîfe)"), SILA_T, AID)))]})

S1.append({"id": "s6", "translation": {"en": "And from al-Shaʿbī; and from Ṭāwūs — though that is not sound.", "tr": "Şa'bî'den de (rivayet etti); Tâvûs'tan da — fakat bu sahih değildir."},
 "tokens": [
  tok("وَعَنِ", "an", "prep", ["huruf-jarr", "anwa-al-waw", "hadhf-wa-taqdir"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَعَنْ حَرْفُ جَرٍّ حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ دَلَّ عَلَيْهِ مَا قَبْلَهُ، تَقْدِيرُهُ: وَرَوَى.",
    "The waw opens a new sentence; عَنْ is a jarr letter, voweled with kasra before the following ال — the jarr phrase hangs on a verb left unsaid, which the sentence before supplies: «and he narrated».",
    "Vâv isti'nâf içindir; an cer harfi, iki sâkin karşılaştığı için kesre ile harekelendi — câr-mecrûr, önceki cümlenin delâlet ettiği mahzûf fiile müteallik: «ve rivayet etti».",
    segments=[seg("وَ", "wa", "conj"), seg("عَنِ", "an", "prep")]),
  J("الشَّعْبِيِّ", "shabi", (" — اسْمٌ مَنْسُوبٌ", " — a nisba name", " — nisbet ismi"), "propn", ["ism-mansub"], punct="،"),
  tok("وَعَنْ", "an", "prep", ["huruf-jarr", "atf-nasaq"], WA_AR + "عَنْ حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى «عَنِ الشَّعْبِيِّ».",
    "The waw conjoins; عَنْ is a jarr letter — the jarr phrase is conjoined to «from al-Shaʿbī».", "«ve» + an cer harfi — câr-mecrûr «Şa'bî'den» üzerine ma'tûf.",
    segments=[seg("وَ", "wa", "conj"), seg("عَنْ", "an", "prep")]),
  J("طَاوُوسٍ", "tawus", (" — عَلَمٌ مَنْقُولٌ عَنِ اسْمِ الطَّائِرِ فَهُوَ مُنْصَرِفٌ", " — a name taken from the word for the peacock, so it keeps its tanwin", " — tavus kuşunun adından alınmış alem; bu yüzden munsariftir"), "propn", punct=" —"),
  tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "anwa-al-waw"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَهُوَ تَعْقِيبٌ مِنَ الذَّهَبِيِّ.",
    "The waw opens a new clause; لَمْ negates the present, turns it to the past and governs jazm — the remark is al-Dhahabī's own.",
    "Vâv isti'nâf içindir; lem: nefiy, cezm ve kalb harfi — bu, Zehebî'nin kendi notudur.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يَصِحَّ", "sahha", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "doubled-verbs"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ الْمُقَدَّرُ، وَحُرِّكَ آخِرُهُ بِالْفَتْحِ لِلتَّخَلُّصِ مِنِ الْتِقَاءِ السَّاكِنَيْنِ لِأَنَّهُ مُضَعَّفٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — أَيْ ذٰلِكَ، وَهُوَ رِوَايَتُهُ عَنْ طَاوُوسٍ.",
    "Present verb in jazm by لَمْ, its sign an estimated sukun: a doubled verb, its last letter takes a fatha so that two quiescents do not meet; the doer is a hidden pronoun «it» — that is, his narrating from Ṭāwūs.",
    "Lem ile meczûm muzâri, alâmeti takdîrî sükûn: muzaaf olduğu için iki sâkin karşılaşmasın diye sonu fetha ile harekelendi; fâil gizli zamir «o» — yani Tâvûs'tan rivayet etmesi.", punct=" —.")]})

# ================================================ Chapter 2 — أَصْلُهُ وَصَنْعَتُهُ (6/394) ================================================
FAAAL = lambda what_ar, what_en, what_tr: (" — عَلَى وَزْنِ فَعَّالٍ لِصَاحِبِ الْحِرْفَةِ: " + what_ar, " — on the pattern فَعَّال, which names a man by his trade: " + what_en, " — meslek sahibini bildiren fa''âl vezninde: " + what_tr)
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "Aḥmad al-ʿIjlī said: Abū Ḥanīfa is a Taymī, of the clan of Ḥamza al-Zayyāt; he was a khazzāz, a seller of khazz cloth.",
  "tr": "Ahmed el-İclî dedi ki: Ebû Hanîfe Teymî'dir, Hamza ez-Zeyyât'ın kabilesindendir; hazz (ipekli kumaş) satan bir kumaşçı idi."},
 "tokens": [
  QALA("قَالَ"),
  F("أَحْمَدُ", "ahmad", D_FIL_R, "propn", DG),
  NA("الْعِجْلِيُّ", "ijli", "raf", ("أَحْمَدُ", "Aḥmad", "Ahmed"), (" — اسْمٌ مَنْسُوبٌ إِلَى بَنِي عِجْلٍ", " — a nisba to the Banū ʿIjl", " — İcl oğullarına nisbet"), "propn", ["ism-mansub"], punct=":"),
  AB("أَبُو", "mubtada"), HANIFA(),
  KB("تَيْمِيٌّ", "taymi", cat((" — اسْمٌ مَنْسُوبٌ", " — a nisba", " — ism-i mensûb"), MAQUL_CL), ["ism-mansub"], punct="،"),
  MINP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ ثَانٍ", "hangs on an omitted word that is a second khabar", "mahzûf ikinci habere müteallik")),
  J("رَهْطِ", "raht", MUDAF, extra=["idafa-definiteness"]),
  MI("حَمْزَةَ", "hamza-name", D_TA, "propn", DG, sign=FATHA_JARR),
  NA("الزَّيَّاتِ", "zayyat", "jarr", ("حَمْزَةَ", "Ḥamza", "Hamza"), cat((" — وَظَهَرَتْ عَلَيْهِ الْكَسْرَةُ لِأَنَّهُ مُنْصَرِفٌ", " — the kasra shows on it, for it is fully declined", " — munsarif olduğu için kesresi zâhirdir"), FAAAL("بَائِعُ الزَّيْتِ", "the oil-seller", "zeytinyağı satıcısı")), "propn", ["sighat-mubalagha"], punct="،"),
  KANA_HID("كَانَ", (" — وَالْجُمْلَةُ خَبَرٌ ثَالِثٌ عَنْ «أَبُو حَنِيفَةَ»", " — the clause is a third khabar of «Abū Ḥanīfa»", " — cümle «Ebû Hanîfe»nin üçüncü haberidir")),
  KK("خَزَّازًا", "khazzaz", FAAAL("بَائِعُ الْخَزِّ", "the seller of khazz", "hazz satıcısı"), extra=["sighat-mubalagha"]),
  MUDARI("يَبِيعُ", "baa", ["hollow-verbs", "jumla-sifa"], **N3(NAAT_OF("nasb", "خَزَّازًا", "a khazzāz", "kumaşçı"))),
  O("الْخَزَّ", "khazz", (" — وَالْخَزُّ: ثِيَابٌ تُنْسَجُ مِنْ حَرِيرٍ، أَوْ مِنْ صُوفٍ وَحَرِيرٍ", " — khazz: cloth woven of silk, or of wool and silk", " — hazz: ipekten veya yün ile ipekten dokunan kumaş"), punct=".")]})

S2.append({"id": "s2", "translation": {
  "en": "ʿUmar ibn Ḥammād ibn Abī Ḥanīfa said: As for Zūṭā, he was of the people of Kābul; and Thābit was born in Islam.",
  "tr": "Ömer b. Hammâd b. Ebî Hanîfe dedi ki: Zûtâ'ya gelince, o Kâbil ahalisindendir; Sâbit ise Müslüman olarak doğmuştur."},
 "tokens": [
  QALA_ISTI(),
  F("عُمَرُ", "umar", (" — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ فَلَا يُنَوَّنُ", " — a proper name barred from tanwin (a name turned from the pattern فَاعِل)", " — alemiyyet ve adl sebebiyle gayr-i munsarif; tenvin almaz"), "propn", DG),
  BN("raf", "عُمَرُ", "ʿUmar", "Ömer"), MI("حَمَّادِ", "hammad-name", DROP, "propn"),
  BN("jarr", "حَمَّادِ", "Ḥammād", "Hammâd"), AB("أَبِي", "mi"), HANIFA(punct=":"),
  tok("أَمَّا", "amma", "part", ["amma-tafsiliyya", "amma-fil-kafiya"],
    "حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ، وَتَلْزَمُ الْفَاءُ جَوَابَهُ.",
    "أَمَّا «as for»: a particle of condition, detailing and emphasis; its answer must open with the fa.",
    "Emmâ «…-e gelince»: şart, tafsîl ve te'kîd harfi; cevabının başına fâ gelmesi zorunludur."),
  MB("زُوطَى", "zuta", (" — عَلَمٌ أَعْجَمِيٌّ مَقْصُورٌ؛ وَخَبَرُهُ جُمْلَةُ «إِنَّهُ…»", " — a foreign name ending in alif maqṣūra; its khabar is the clause «he is…»", " — maksûr yabancı özel isim; haberi «o …» cümlesidir"), "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"),
  tok("فَإِنَّهُ", "inna", "part", ["amma-tafsiliyya", "inna-wa-akhawatuha", "al-bariz-al-muttasil", "al-fa-fi-khabar-al-mubtada"],
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَجُمْلَةُ إِنَّ وَمَعْمُولَيْهَا فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ «زُوطَى».",
    "The fa is the one that must open the answer of أَمَّا — it is no conjunction; إِنَّ is the particle of emphasis, and the attached «he» is its noun, in the seat of nasb — the whole إِنَّ clause is the khabar of «Zūṭā», in the seat of raf'.",
    "Fâ, emmâ'nın cevabının başına gelen fâ'dır, atıf değildir; inne te'kîd ve nasb harfi, bitişik «o» zamiri ismi, mahallen mansûb — inne cümlesi «Zûtâ» mübtedâsının haberi olarak mahallen merfû.",
    segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  MINP(JM_KH_INNA), J("أَهْلِ", "ahl", MUDAF, extra=["idafa-definiteness"]),
  MI("كَابُلَ", "kabul", D_BALAD, "propn", DG, sign=FATHA_JARR, punct="،"),
  MAJHUL("وَوُلِدَ", "walada", ["mithal-verbs"]),
  tok("ثَابِتٌ", "thabit-name", "propn", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ وَالِدُ أَبِي حَنِيفَةَ.", "The deputy doer (na'ib al-fa'il), in raf' — Thābit, Abū Ḥanīfa's father.", "Nâib-i fâil, merfû — Sâbit, Ebû Hanîfe'nin babasıdır."),
  ALAP(), J("الْإِسْلَامِ", "islam", (" — أَيْ وُلِدَ مُسْلِمًا", " — that is, he was born a Muslim", " — yani Müslüman olarak doğdu"), punct=".")]})

S2.append({"id": "s3", "translation": {
  "en": "Zūṭā had been a slave of the Banū Taym Allāh ibn Thaʿlaba; then he was freed, so his walāʾ belongs to them, and after them to the Banū Qafl.",
  "tr": "Zûtâ, Teymullah b. Sa'lebe oğullarının kölesi idi; sonra âzât edildi; bu yüzden velâsı onlara, sonra da Kafl oğullarına aittir."},
 "tokens": [
  ISTI(KANA("وَكَانَ")),
  IK("زُوطَى", "zuta", (" — عَلَمٌ أَعْجَمِيٌّ مَقْصُورٌ", " — a foreign name ending in alif maqṣūra: the damma is estimated on the alif", " — maksûr yabancı özel isim: damme elif üzerinde takdîrîdir"), "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"),
  KK("مَمْلُوكًا", "mamluk", (" — اسْمُ مَفْعُولٍ مِنْ مَلَكَ", " — the passive participle of مَلَكَ: «owned»", " — meleke'nin ism-i mef'ûlü: «köle»"), extra=["ism-maful"]),
  LI_BANI(JM("مُتَعَلِّقٌ بِـ«مَمْلُوكًا»", "attaches to «owned»", "«memlûk»e müteallik")),
  MI("تَيْمِ", "taym", MUDAF, "propn"), ALLAH_MI(), BN("jarr", "تَيْمِ اللهِ", "Taym Allāh", "Teymullah"),
  MI("ثَعْلَبَةَ", "thalaba", D_TA, "propn", DG, sign=FATHA_JARR, punct="،"),
  MAJHUL("فَأُعْتِقَ", "ataqa-free", ["form-iv-verbs"], punct="،", note_ar=NAIB_HID[0], note_en=NAIB_HID[1], note_tr=NAIB_HID[2]),
  FA("فَوَلَاؤُهُ", "wala", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil", "ism-mamdud"],
    "وَلَاءُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْفَاءُ تُفِيدُ السَّبَبِيَّةَ: الْوَلَاءُ ثَمَرَةُ الْعِتْقِ.",
    "«walāʾ» is the mubtada, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr — the fa gives the consequence: clientage follows from the freeing.",
    "«velâ» mübtedâ, merfû, muzâf; bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr — fâ sonucu bildirir: velâ, âzât etmenin neticesidir.",
    segs=[seg("وَلَاؤُ", "wala", "noun"), seg("هُ", "pron-3ms", "pron")]),
  LAHU2("لَهُمْ", "pron-3mp", " («onlara»)", punct="،", note=JM_KHABAR),
  THUMMA(),
  LI_BANI(JM("مَعْطُوفٌ عَلَى «لَهُمْ»", "is conjoined to «to them»", "«onlara» üzerine ma'tûf")),
  MI("قَفْلٍ", "qafl", pos="propn", punct=".")]})

S2.append({"id": "s4", "translation": {
  "en": "He said: Abū Ḥanīfa was a khazzāz, and his shop is well known, in the house of ʿAmr ibn Ḥurayth.",
  "tr": "(Ömer b. Hammâd) dedi ki: Ebû Hanîfe ipekli kumaş satıcısıydı; dükkânı, Amr b. Hureys'in evinde, bilinen bir yerdir."},
 "tokens": [
  QALA_HID(),
  KANA("وَكَانَ"), AB("أَبُو", "ismk"), HANIFA(),
  KK("خَزَّازًا", "khazzaz", FAAAL("بَائِعُ الْخَزِّ", "the seller of khazz", "hazz satıcısı"), extra=["sighat-mubalagha"], punct="،"),
  tok("وَدُكَّانُهُ", "dukkan", "noun", ["mubtada-khabar", "atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "دُكَّانُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The waw conjoins a second sentence; «shop» is the mubtada, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr.",
    "«ve» + «dükkân» mübtedâ, merfû, muzâf; bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr.",
    segments=[seg("وَ", "wa", "conj"), seg("دُكَّانُ", "dukkan", "noun"), seg("هُ", "pron-3ms", "pron")]),
  KB("مَعْرُوفٌ", "maruf", (" — اسْمُ مَفْعُولٍ مِنْ عَرَفَ", " — the passive participle of عَرَفَ: «known»", " — arafe'nin ism-i mef'ûlü: «bilinen»"), ["ism-maful"]),
  FIP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ ثَانٍ", "hangs on an omitted word that is a second khabar", "mahzûf ikinci habere müteallik")),
  J("دَارِ", "dar", MUDAF, extra=["idafa-definiteness"]),
  MI("عَمْرِو", "amr-name", cat(DROP, ("، وَالْوَاوُ تُكْتَبُ وَلَا تُنْطَقُ فَرْقًا بَيْنَهُ وَبَيْنَ عُمَرَ", "; the waw is written, not spoken, to tell it from ʿUmar", "; vâv Ömer'den ayırmak için yazılır, okunmaz")), "propn"),
  BN("jarr", "عَمْرِو", "ʿAmr", "Amr"), MI("حُرَيْثٍ", "hurayth", pos="propn", punct=".")]})

S2.append({"id": "s5", "translation": {
  "en": "Al-Naḍr ibn Muḥammad al-Marwazī said, from Yaḥyā ibn al-Naḍr, who said: Abū Ḥanīfa's father was from Nasā.",
  "tr": "Nadr b. Muhammed el-Mervezî, Yahyâ b. Nadr'dan naklen dedi ki: Ebû Hanîfe'nin babası Nesâ'dandı."},
 "tokens": [
  QALA_ISTI(),
  F("النَّضْرُ", "nadr", pos="propn"), BN("raf", "النَّضْرُ", "al-Naḍr", "Nadr"), MI("مُحَمَّدٍ", "muhammad", pos="propn"),
  NA("الْمَرْوَزِيُّ", "marwazi", "raf", ("النَّضْرُ", "al-Naḍr", "Nadr"), (" — مَنْسُوبٌ إِلَى مَرْوَ عَلَى غَيْرِ قِيَاسٍ بِزِيَادَةِ الزَّايِ", " — a nisba to Marw, irregular: a zay is added", " — Merv'e nisbet; kıyasa aykırı olarak zây eklenmiştir"), "propn", ["ism-mansub"]),
  AN_PREP(RAWI),
  J("يَحْيَى", "yahya", (" — عَلَمٌ عَلَى وَزْنِ الْفِعْلِ مَمْنُوعٌ مِنَ الصَّرْفِ، وَهُوَ مَقْصُورٌ", " — a proper name on the pattern of a verb, barred from tanwin; it ends in alif maqṣūra, so the vowel is estimated", " — fiil vezninde alem, gayr-i munsarif; maksûr olduğu için hareke takdîrîdir"), "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ نِيَابَةً عَنِ الْكَسْرَةِ"),
  BN("jarr", "يَحْيَى", "Yaḥyā", "Yahyâ"), MI("النَّضْرِ", "nadr", pos="propn", punct="،"),
  QALA("قَالَ", hidden=True, punct=":"),
  KANA("كَانَ"), IK("وَالِدُ", "walid-father", MUDAF, extra=["ism-fail", "idafa-definiteness"]), AB("أَبِي", "mi"), HANIFA(),
  MINP(JM_KH_KANA),
  J("نَسَا", "nasa", (" — عَلَمٌ عَلَى بَلْدَةٍ بِخُرَاسَانَ، مَمْنُوعٌ مِنَ الصَّرْفِ، وَهُوَ مَقْصُورٌ", " — the name of a town in Khurāsān, barred from tanwin; it ends in alif, so the vowel is estimated", " — Horasan'da bir şehrin adı, gayr-i munsarif; maksûr olduğu için hareke takdîrîdir"), "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ نِيَابَةً عَنِ الْكَسْرَةِ", punct=".")]})

S2.append({"id": "s6", "translation": {
  "en": "Sulaymān ibn al-Rabīʿ related from al-Ḥārith ibn Idrīs, who said: Abū Ḥanīfa — his origin is from Tirmidh.",
  "tr": "Süleyman b. Rebî', Hâris b. İdrîs'ten rivayet etti; o dedi ki: Ebû Hanîfe'nin aslı Tirmiz'dendir."},
 "tokens": [
  RAWA_ISTI(),
  F("سُلَيْمَانُ", "sulayman", D_AJ_R, "propn", DG), BN("raf", "سُلَيْمَانُ", "Sulaymān", "Süleyman"), MI("الرَّبِيعِ", "rabi-name", pos="propn", punct="،"),
  AN_K(), J("الْحَارِثِ", "harith-alam", pos="propn"), BN("jarr", "الْحَارِثِ", "al-Ḥārith", "Hâris"),
  MI("إِدْرِيسَ", "idris", D_AJ, "propn", DG, sign=FATHA_JARR, punct="،"),
  QALA("قَالَ", hidden=True, punct=":"),
  AB("أَبُو", "mubtada", (" — مُبْتَدَأٌ أَوَّلُ، وَخَبَرُهُ الْجُمْلَةُ الِاسْمِيَّةُ بَعْدَهُ", " — the first mubtada; its khabar is the nominal clause after it", " — birinci mübtedâ; haberi ardından gelen isim cümlesidir")), HANIFA(),
  ENC_NOUN("أَصْلُهُ", "asl", "هُ", "mubtada", note_ar=" — مُبْتَدَأٌ ثَانٍ، وَالْهَاءُ هُوَ الرَّابِطُ؛ وَجُمْلَةُ «أَصْلُهُ مِنْ تِرْمِذَ» فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ الْأَوَّلِ",
    note_en=" — a second mubtada, and its pronoun is the link; the clause «his origin is from Tirmidh» is the khabar of the first mubtada, in the seat of raf'",
    note_tr=" — ikinci mübtedâ; zamir râbıttır; «aslı Tirmiz'dendir» cümlesi birinci mübtedânın haberi olarak mahallen merfû"),
  MINP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ الْمُبْتَدَأِ الثَّانِي", "hangs on an omitted word that is the khabar of the second mubtada", "ikinci mübtedânın mahzûf haberine müteallik")),
  J("تِرْمِذَ", "tirmidh", D_BALAD, "propn", DG, sign=FATHA_JARR, punct=".")]})

S2.append({"id": "s7", "translation": {
  "en": "Abū ʿAbd al-Raḥmān al-Muqriʾ said: Abū Ḥanīfa is of the people of Bābil.",
  "tr": "Ebû Abdurrahman el-Mukrî dedi ki: Ebû Hanîfe Bâbil ahalisindendir."},
 "tokens": [
  QALA_ISTI(),
  AB("أَبُو", "fail"), MI("عَبْدِ", "abd", MUDAF, extra=["idafa-definiteness"]), MI("الرَّحْمٰنِ", "rahman", (" — مِنْ أَسْمَاءِ اللهِ الْحُسْنَى", " — one of the Names of God", " — Allah'ın güzel isimlerinden"), "propn"),
  tok("الْمُقْرِي", "muqri", "noun", ["naat-sifa", "ism-fail", "ism-maqsur-manqus"],
    "نَعْتٌ لِـ«أَبُو» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — وَأَصْلُهُ الْمُقْرِئُ بِالْهَمْزِ، اسْمُ فَاعِلٍ مِنْ أَقْرَأَ، وَخُفِّفَتْ هَمْزَتُهُ يَاءً كَمَا فِي الْمَطْبُوعِ.",
    "An adjective (na't) of «Abū», in raf' by a damma estimated on the ya — it is الْمُقْرِئ, the active participle of أَقْرَأَ «to teach recitation», printed here with its hamza lightened to a ya.",
    "«Ebû» isminin na'tı, yâ üzerinde takdîrî damme ile merfû — aslı hemzeli الْمُقْرِئ'dir (akrae'nin ism-i fâili: kıraat öğreten); matbû nüshadaki gibi hemzesi yâ'ya tahfif edilmiştir.", punct=":"),
  AB("أَبُو", "mubtada"), HANIFA(),
  MINP(cat(JM_KHABAR, MAQUL_CL)), J("أَهْلِ", "ahl", MUDAF, extra=["idafa-definiteness"]),
  MI("بَابِلَ", "babil", D_BALAD, "propn", DG, sign=FATHA_JARR, punct=".")]})

# ================================================ Chapter 3 — قَوْلُ ابْنِ مَعِينٍ فِيهِ (6/395) ================================================
YAHYA_MAF = lambda: O("يَحْيَى", "yahya", (" — عَلَمٌ عَلَى وَزْنِ الْفِعْلِ، مَقْصُورٌ", " — a proper name on the pattern of a verb; it ends in alif maqṣūra, so the fatha is estimated", " — fiil vezninde, maksûr alem: fetha takdîrîdir"), "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ")
SAMITU = lambda: MADI_T("سَمِعْتُ", "samia", who="ana", note_ar=MAQUL_CL[0], note_en=MAQUL_CL[1], note_tr=MAQUL_CL[2])
YAQULU_HAL = lambda of_ar, of_en, of_tr: MUDARI("يَقُولُ", "qala", ["hollow-verbs", "al-hal-jumla-wa-rabituha"], punct=":",
    note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «" + of_ar + "»، وَمَقُولُ الْقَوْلِ بَعْدَهَا", note_en="; the clause is a hal of «" + of_en + "», in the seat of nasb, and what he says follows", note_tr="; cümle «" + of_tr + "»dan hâl, mahallen mansûb; söylenen söz ardından gelir")
THIQA_N = (" — مَصْدَرُ وَثِقَ وُصِفَ بِهِ، فَيَسْتَوِي فِيهِ الْمُفْرَدُ وَالْجَمْعُ؛ وَهُوَ عِنْدَ الْمُحَدِّثِينَ: الرَّاوِي الْعَدْلُ الضَّابِطُ",
           " — the masdar of وَثِقَ used as a description, so it does not change for number; among the ḥadīth scholars it means the upright and accurate transmitter",
           " — vesika'nın masdarı olup vasıf olarak kullanılmıştır, tekil-çoğul değişmez; muhaddislerin ıstılahında: adâlet ve zabt sahibi râvî")
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "Muḥammad ibn Saʿd al-ʿAwfī said: I heard Yaḥyā ibn Maʿīn say: Abū Ḥanīfa was trustworthy; he would narrate a ḥadīth only if he had it by heart, and would not narrate what he had not memorised.",
  "tr": "Muhammed b. Sa'd el-Avfî dedi ki: Yahyâ b. Maîn'i şöyle derken işittim: Ebû Hanîfe sikaydı (güvenilir bir râvîydi); hadisi ancak ezberinde olanla rivayet eder, ezberlemediğini rivayet etmezdi."},
 "tokens": [
  QALA("قَالَ"),
  F("مُحَمَّدُ", "muhammad", DROP, "propn"), BN("raf", "مُحَمَّدُ", "Muḥammad", "Muhammed"), MI("سَعْدٍ", "sad-name", pos="propn"),
  NA("الْعَوْفِيُّ", "awfi", "raf", ("مُحَمَّدُ", "Muḥammad", "Muhammed"), (" — اسْمٌ مَنْسُوبٌ", " — a nisba", " — ism-i mensûb"), "propn", ["ism-mansub"], punct=":"),
  SAMITU(), YAHYA_MAF(), BN("nasb", "يَحْيَى", "Yaḥyā", "Yahyâ"), MI("مَعِينٍ", "main-name", pos="propn"),
  YAQULU_HAL("يَحْيَى", "Yaḥyā", "Yahyâ"),
  KANA("كَانَ"), AB("أَبُو", "ismk"), HANIFA(),
  KK("ثِقَةً", "thiqa", THIQA_N, extra=["masdar"], punct="،"),
  LA_NAFIYA(),
  MUDARI("يُحَدِّثُ", "haddatha", ["form-ii-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرٌ ثَانٍ لِكَانَ", note_en="; the clause is a second predicate of كَانَ, in the seat of nasb", note_tr="; cümle kâne'nin ikinci haberi olarak mahallen mansûb"),
  BI_NOUN("بِالْحَدِيثِ", "hadith", "الْحَدِيثِ"),
  ILLA(),
  BIMA(),
  MUDARI("يَحْفَظُهُ", "hafiza", enc="هُ", punct="،", **N3(cat(SILA_T, ("، وَالْهَاءُ هُوَ الْعَائِدُ", "; its pronoun is the one that returns to the relative", "; zamiri âiddir")))),
  WA_LA_NAFIYA(),
  MUDARI("يُحَدِّثُ", "haddatha", ["form-ii-verbs", "atf-nasaq"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «لَا يُحَدِّثُ» الْأُولَى", note_en="; the clause is conjoined to the first «he would not narrate»", note_tr="; cümle ilk «rivayet etmezdi» cümlesine ma'tûf"),
  BIMA(), LA_NAFIYA(),
  MUDARI("يَحْفَظُ", "hafiza", punct=".", **N3(cat(SILA_T, AID, (" تَقْدِيرُهُ: يَحْفَظُهُ", " («what he has not memorised»)", " (takdiri: يَحْفَظُهُ)"))))]})

S3.append({"id": "s2", "translation": {
  "en": "Ṣāliḥ ibn Muḥammad said: I heard Yaḥyā ibn Maʿīn say: Abū Ḥanīfa was trustworthy in ḥadīth.",
  "tr": "Sâlih b. Muhammed dedi ki: Yahyâ b. Maîn'i şöyle derken işittim: Ebû Hanîfe hadiste sikaydı."},
 "tokens": [
  QALA_ISTI(),
  F("صَالِحُ", "salih-nabi", DROP, "propn"), BN("raf", "صَالِحُ", "Ṣāliḥ", "Sâlih"), MI("مُحَمَّدٍ", "muhammad", pos="propn", punct=":"),
  SAMITU(), YAHYA_MAF(), BN("nasb", "يَحْيَى", "Yaḥyā", "Yahyâ"), MI("مَعِينٍ", "main-name", pos="propn"),
  YAQULU_HAL("يَحْيَى", "Yaḥyā", "Yahyâ"),
  KANA("كَانَ"), AB("أَبُو", "ismk"), HANIFA(),
  KK("ثِقَةً", "thiqa", THIQA_N, extra=["masdar"]),
  FIP(JM("مُتَعَلِّقٌ بِـ«ثِقَةً»", "attaches to «trustworthy»", "«sika»ya müteallik")), J("الْحَدِيثِ", "hadith", punct=".")]})

S3.append({"id": "s3", "translation": {
  "en": "Aḥmad ibn Muḥammad ibn al-Qāsim ibn Muḥriz related from Ibn Maʿīn: Abū Ḥanīfa — there was no harm in him.",
  "tr": "Ahmed b. Muhammed b. Kâsım b. Muhriz, İbn Maîn'den şunu rivayet etti: Ebû Hanîfe'de bir beis yoktu (rivayeti makbuldü)."},
 "tokens": [
  RAWA_ISTI(),
  F("أَحْمَدُ", "ahmad", D_FIL_R, "propn", DG), BN("raf", "أَحْمَدُ", "Aḥmad", "Ahmed"), MI("مُحَمَّدِ", "muhammad", DROP, "propn"),
  BN("jarr", "مُحَمَّدِ", "Muḥammad", "Muhammed"), MI("الْقَاسِمِ", "qasim", pos="propn"), BN("jarr", "الْقَاسِمِ", "al-Qāsim", "Kâsım"),
  MI("مُحْرِزٍ", "muhriz", pos="propn", punct="،"),
  AN_K(),
  J("ابْنِ", "ibn", cat(MUDAF, (" — وَثَبَتَتْ أَلِفُهُ لِأَنَّهُ لَمْ يَقَعْ بَيْنَ عَلَمَيْنِ", " — its alif is written, for it does not stand between two names", " — iki alem arasında olmadığı için elifi yazılır")), extra=["idafa-definiteness"]),
  MI("مَعِينٍ", "main-name", pos="propn", punct=":"),
  KANA("كَانَ"), AB("أَبُو", "ismk"), HANIFA(),
  LA_JINS(), ISM_LA("بَأْسَ", "bas"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onda»)", punct=".",
    note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ لَا؛ وَجُمْلَةُ «لَا بَأْسَ بِهِ» فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ — وَهِيَ مِنْ أَلْفَاظِ التَّعْدِيلِ عِنْدَ الْمُحَدِّثِينَ",
    note_en="; the jarr phrase hangs on the omitted predicate of لَا, and the clause «there is no harm in him» is the predicate of كَانَ, in the seat of nasb — among the ḥadīth scholars it is a term of accreditation",
    note_tr="; câr-mecrûr lâ'nın mahzûf haberine müteallik; «onda beis yok» cümlesi kâne'nin haberi olarak mahallen mansûb — muhaddislerin ta'dîl lafızlarındandır")]})

S3.append({"id": "s4", "translation": {
  "en": "And he said on another occasion: With us he is one of the people of truthfulness, and he was never accused of lying;",
  "tr": "Bir defasında da şöyle dedi: O, bizim nazarımızda doğruluk ehlindendir; yalanla itham edilmemiştir;"},
 "tokens": [
  QALA_ISTI(hidden=True),
  tok("مَرَّةً", "marra-once", "noun", ["maful-fih"],
    "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ فِي وَقْتٍ آخَرَ؛ وَالْقَائِلُ ابْنُ مَعِينٍ.",
    "An adverb of time, in nasb — «once», on another occasion; the speaker is Ibn Maʿīn.",
    "Zaman zarfı, mansûb — «bir defasında»; söyleyen İbn Maîn'dir.", punct=":"),
  PRON_MUB("هُوَ", "huwa"),
  tok("عِنْدَنَا", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — أَيْ فِي حُكْمِنَا، مَعْشَرَ الْمُحَدِّثِينَ.",
    "An adverb of place «with», in nasb and annexed; the attached «us» is the second term of the idafa, in the seat of jarr — «in our judgement», that of the ḥadīth scholars.",
    "Mekân zarfı «yanında», mansûb, muzâf; bitişik «biz» zamiri muzâfun ileyh, mahallen mecrûr — yani «biz muhaddislerin hükmünde».",
    segments=[seg("عِنْدَ", "inda", "noun"), seg("نَا", "pron-1p", "pron")]),
  MINP(JM_KHABAR), J("أَهْلِ", "ahl", MUDAF, extra=["idafa-definiteness"]), MI("الصِّدْقِ", "sidq", extra=["masdar"], punct="،"),
  WA_LAM(),
  MAJHUL_M("يُتَّهَمْ", "ittahama", "مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "in jazm by لَمْ, its sign the sukun", "lem ile meczûm, alâmeti sükûn",
    extra=["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-viii-verbs", "mithal-verbs"],
    n=(" — مِنَ اتَّهَمَ عَلَى افْتَعَلَ مِنَ الْوَهْمِ: أَصْلُهُ اِوْتَهَمَ، قُلِبَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ فِي تَاءِ الِافْتِعَالِ",
       " — from اتَّهَمَ, Form VIII of و ه م: it was اِوْتَهَمَ, whose waw turned into ta and merged into the ta of the pattern",
       " — ittehame'den (vehm kökünden iftiâl bâbı): aslı اِوْتَهَمَ; vâv tâ'ya çevrilip iftiâl tâ'sına idgâm edilmiştir")),
  BI_NOUN("بِالْكَذِبِ", "kadhib", "الْكَذِبِ", extra=["masdar"], punct="،")]})

S3.append({"id": "s5", "translation": {
  "en": "and indeed Ibn Hubayra had him beaten over the judgeship, yet he refused to be a judge.",
  "tr": "andolsun ki İbn Hübeyre onu kadılık yüzünden dövdürdü; o yine de kadı olmayı kabul etmedi."},
 "tokens": [
  tok("وَلَقَدْ", "qad", "part", ["qad-harf", "al-qasam-wal-shart-fil-kafiya", "atf-nasaq"],
    WA_AR + "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مَحْذُوفٍ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُمَا جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The waw conjoins; the lam opens the answer of an oath left unsaid, and قَدْ affirms the past verb after it — the clause is the oath's answer and has no seat.",
    "«ve» + lâm, hazfedilmiş bir kasemin cevabına gelmiştir; kad tahkîk harfidir — sonraki cümle kasemin cevabıdır, i'râbdan mahalli yoktur.",
    segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")]),
  ENC_MADI("ضَرَبَهُ", "daraba", "هُ", note_ar=" مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ", note_en=", placed before the doer, which follows", note_tr="; fâilden önce gelmiştir, fâil ardından gelir"),
  F("ابْنُ", "ibn", MUDAF, extra=["idafa-definiteness"]),
  MI("هُبَيْرَةَ", "hubayra", D_TA, "propn", DG, sign=FATHA_JARR),
  ALAP((" — وَ«عَلَى» هُنَا لِلتَّعْلِيلِ", " — عَلَى here gives the reason: «over, on account of»", " — «alâ» burada ta'lîl içindir: «… yüzünden»")),
  J("الْقَضَاءِ", "qada", (" — أَيْ لِيَلِيَ الْقَضَاءَ", " — that is, to make him take the office of judge", " — yani kadılık görevini üstlenmesi için"), extra=["masdar", "ism-mamdud"], punct="،"),
  MADI_ALIF("فَأَبَى", "aba", hidden=True),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«أَبَى»", "; the clause it builds is the object of «refused», in the seat of nasb", "; kurduğu müevvel masdar «reddetti»nin mef'ûlü, mahallen mansûb"),
  tok("يَكُونَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "nawasib-wa-jawazim-al-mudari"],
    "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "The present of كَانَ, in nasb by أَنْ, its sign the fatha; its noun is the hidden pronoun «he».", "Kâne'nin muzârisi, en ile mansûb, alâmeti fetha; ismi gizli zamir «o»."),
  KK("قَاضِيًا", "qadi", (" — اسْمٌ مَنْقُوصٌ تَظْهَرُ عَلَى يَائِهِ الْفَتْحَةُ لِخِفَّتِهَا؛ اسْمُ فَاعِلٍ مِنْ قَضَى", " — a manqūṣ noun: the fatha, being light, shows on its ya; the active participle of قَضَى", " — menkûs isim: fetha hafif olduğu için yâ üzerinde zâhirdir; kadâ'nın ism-i fâili"), extra=["ism-fail", "ism-maqsur-manqus"], punct=".")]})

# ================================================ Chapter 4 — قِيَامُ اللَّيْلِ (6/399) ================================================
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "Bishr ibn al-Walīd related from the qāḍī Abū Yūsuf, who said:",
  "tr": "Bişr b. Velîd, Kadı Ebû Yûsuf'tan şöyle dediğini rivayet etti:"},
 "tokens": [
  RAWA_ISTI(),
  F("بِشْرُ", "bishr", DROP, "propn"), BN("raf", "بِشْرُ", "Bishr", "Bişr"), MI("الْوَلِيدِ", "walid-alam", pos="propn", punct="،"),
  AN_K(),
  J("الْقَاضِي", "qadi", (" — اسْمٌ مَنْقُوصٌ", " — a manqūṣ noun: the kasra is estimated on its ya", " — menkûs isim: kesre yâ üzerinde takdîrîdir"), extra=["ism-fail", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ"),
  AB("أَبِي", "badal_jarr"),
  MI("يُوسُفَ", "yusuf", D_AJ, "propn", DG, sign=FATHA_JARR, punct="،"),
  QALA("قَالَ", hidden=True, punct=":")]})

S4.append({"id": "s2", "translation": {
  "en": "While I was walking with Abū Ḥanīfa, I suddenly heard a man say to another: «This is Abū Ḥanīfa; he does not sleep at night.»",
  "tr": "Ebû Hanîfe ile yürürken, birinin bir başkasına şöyle dediğini işittim: «Bu Ebû Hanîfe'dir; geceleri uyumaz.»"},
 "tokens": [
  tok("بَيْنَمَا", "baynama", "noun", ["maful-fih", "al-kinayat-wal-zuruf-al-mabniyya"],
    "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (بَيْنَ)، وَ«مَا» زَائِدَةٌ كَفَّتْهُ عَنِ الْإِضَافَةِ إِلَى الْمُفْرَدِ فَوَلِيَتْهُ الْجُمْلَةُ — وَالْعَامِلُ فِيهِ جَوَابُهُ «سَمِعْتُ».",
    "بَيْنَمَا «while»: the adverb بَيْنَ, in nasb, with an added مَا that keeps it from being annexed to a single noun, so a clause follows it — it is governed by its answer, «I heard».",
    "Beynemâ «…-iken»: mansûb zaman zarfı «beyne» ile onu müfrede muzâf olmaktan alıkoyan zâid «mâ»; bu yüzden ardından cümle gelir — âmili, cevabı olan «işittim»dir."),
  PRON_MUB("أَنَا", "ana", built="السُّكُونِ", built_en="sukun", built_tr="sükûn"),
  MUDARI("أَمْشِي", "masha", who="أَنَا", naqis="ي", wujub=True, **N3(KH_CL)),
  MAA(), AB("أَبِي", "mi"), HANIFA(punct="،"),
  tok("إِذْ", "idh", "noun", ["al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "al-kinayat-wal-zuruf-al-mabniyya"],
    "إِذْ لِلْمُفَاجَأَةِ، مَبْنِيٌّ عَلَى السُّكُونِ: حَرْفٌ لَا مَحَلَّ لَهُ عِنْدَ قَوْمٍ، وَظَرْفٌ عِنْدَ آخَرِينَ — وَالْجُمْلَةُ بَعْدَهُ جَوَابُ بَيْنَمَا.",
    "The إِذْ OF SURPRISE («and all at once»), built on sukun — a particle with no seat for some grammarians, an adverb for others; the clause after it answers بَيْنَمَا.",
    "Müfâcee iz'i («derken, ansızın»), sükûn üzere mebnî — kimine göre mahalli olmayan harf, kimine göre zarf; sonraki cümle beynemâ'nın cevabıdır."),
  MADI_T("سَمِعْتُ", "samia", who="ana"),
  O("رَجُلًا", "rajul"),
  MUDARI("يَقُولُ", "qala", ["hollow-verbs", "jumla-sifa"], **N3(cat(NAAT_OF("nasb", "رَجُلًا", "a man", "adam"), ("، وَمَقُولُ الْقَوْلِ بَعْدَهَا", ", and what he says follows", "; söylenen söz ardından gelir")))),
  tok("لِآخَرَ", "li", "prep", ["huruf-jarr", "mamnu-min-sarf"],
    "اللَّامُ حَرْفُ جَرٍّ، وَآخَرَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ — أَيْ لِرَجُلٍ آخَرَ.",
    "The lam is a jarr letter; آخَرَ «another» is in jarr — by a fatha in place of the kasra, for it is barred from tanwin (an adjective on the أَفْعَل pattern): «to another man».",
    "Lâm cer harfi; «bir başkası» mecrûr — vasfiyyet ve ef'al vezni sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile: «başka bir adama».", punct=":",
    segments=[seg("لِ", "li", "prep"), seg("آخَرَ", "akhar", "noun")]),
  HADHA("رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ", extra=["mubtada-khabar"]),
  AB("أَبُو", "khabar", MAQUL_CL), HANIFA(),
  LA_NAFIYA(),
  MUDARI("يَنَامُ", "nama", ["hollow-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ", note_en="; the clause is a second khabar, in the seat of raf'", note_tr="; cümle ikinci haber olarak mahallen merfû"),
  ZARF("اللَّيْلَ", "layl", "زَمَانٍ", "time", "Zaman", mudaf=False, punct=".")]})

S4.append({"id": "s3", "translation": {
  "en": "Abū Ḥanīfa said: «By God, nothing shall be told of me that I have not done.»",
  "tr": "Bunun üzerine Ebû Hanîfe dedi ki: «Vallahi, yapmadığım bir şey benim hakkımda konuşulmayacak.»"},
 "tokens": [
  QALA("فَقَالَ"), AB("أَبُو", "fail"), HANIFA(punct=":"),
  tok("وَاللهِ", "allah", "propn", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "huruf-jarr"],
    "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُقْسِمُ.",
    "The waw is the letter of the oath, a jarr letter; the Name of Majesty is what is sworn by, in jarr by the kasra — the jarr phrase hangs on a verb left unsaid: «I swear».",
    "Vâv kasem ve cer harfidir; lafza-i celâl kendisine yemin edilen (muksemün bih), kesre ile mecrûr — câr-mecrûr mahzûf «yemin ederim» fiiline müteallik.",
    segments=[seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  tok("لَا", "la-nafiya", "part", ["la-nafiya", "al-qasam-wal-shart-fil-kafiya"],
    "لَا نَافِيَةٌ لَا عَمَلَ لَهَا — وَالْجُمْلَةُ بَعْدَهَا جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The negating لَا, which governs nothing — the clause after it is the answer of the oath and has no seat.",
    "Nefiy lâ'sı; amel etmez — sonraki cümle kasemin cevabıdır, i'râbdan mahalli yoktur."),
  MAJHUL_M("يُتَحَدَّثُ", "tahaddatha", "مَرْفُوعٌ بِالضَّمَّةِ", "in raf' by the damma", "damme ile merfû", extra=["form-v-verbs", "mudari-marfu"], naib=False,
    n=("، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «عَنِّي» لِأَنَّ الْفِعْلَ لَازِمٌ", "; the verb is intransitive, so its deputy doer is the jarr phrase «of me»", "; fiil lâzım olduğu için nâib-i fâili «benden» câr-mecrûrudur")),
  tok("عَنِّي", "an", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim", "naib-al-fail"],
    "عَنْ حَرْفُ جَرٍّ، وَالنُّونُ لِلْوِقَايَةِ أُدْغِمَتْ فِيهَا نُونُ عَنْ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.",
    "عَنْ «of, about» is a jarr letter; the nun of guarding takes the nun of عَنْ into its doubling, and the speaker's ya fills the seat of jarr — the jarr phrase stands as the deputy doer, in the seat of raf'.",
    "An cer harfi; an'ın nûnu vikâye nûnuna idgâm edilmiş, mütekellim yâ'sı mahallen mecrûr — câr-mecrûr nâib-i fâil olarak mahallen merfû.",
    segments=[seg("عَنْ", "an", "prep"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  BIMA(), LAM_JAZM(),
  JAZM_V("أَفْعَلْ", "faala", hidden="أَنَا", punct="،", **N3(cat(("، وَاسْتِتَارُهُ وَاجِبٌ", " (it must stay hidden)", " (vücûben müstetir)"), SILA_T, AID, (" تَقْدِيرُهُ: أَفْعَلْهُ", " («what I have not done»)", " (takdiri: أَفْعَلْهُ)"))))]})

S4.append({"id": "s4", "translation": {
  "en": "So from then on he would keep the night alive in prayer, humble entreaty and supplication.",
  "tr": "Bundan sonra geceyi namaz, tazarru ve dua ile ihyâ ederdi."},
 "tokens": [
  KANA_HID("فَكَانَ", (" — وَهٰذَا مِنْ كَلَامِ أَبِي يُوسُفَ", " — this is Abū Yūsuf speaking again", " — bu, Ebû Yûsuf'un sözüdür")),
  MUDARI("يُحْيِي", "ahya", ["form-iv-verbs", "kana-wa-akhawatuha"], naqis="ي", **N3(KH_KANA_CL)),
  O("اللَّيْلَ", "layl", (" — وَإِحْيَاءُ اللَّيْلِ: قِيَامُهُ بِالْعِبَادَةِ، عَلَى الْمَجَازِ", " — «to give life to the night» is to spend it awake in worship, a figure of speech", " — «geceyi ihyâ etmek»: onu ibadetle geçirmek; mecazdır")),
  tok("صَلَاةً", "salat", "noun", ["hal", "masdar"],
    "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ فِي مَوْضِعِ الْحَالِ، أَيْ: مُصَلِّيًا؛ وَيَجُوزُ أَنْ يَكُونَ تَمْيِيزًا.",
    "A hal, in nasb — a masdar standing where a hal stands: «praying»; it may also be read as a specifier (tamyiz).",
    "Hâl, mansûb — hâl yerinde gelmiş masdar: «namaz kılarak»; temyîz olması da câizdir.", punct="،"),
  ATF("وَتَضَرُّعًا", "tadarru", case="nasb", extra=["masdar", "form-v-verbs"], punct="،", note_ar=" — مَصْدَرُ تَضَرَّعَ", note_en=" — the masdar of تَضَرَّعَ «to entreat humbly»", note_tr=" — tedarraa'nın masdarı"),
  ATF("وَدُعَاءً", "dua", case="nasb", extra=["masdar", "ism-mamdud"], punct=".")]})

S4.append({"id": "s5", "translation": {
  "en": "It has been related by two chains that Abū Ḥanīfa recited the whole Qurʾān in a single rakʿa.",
  "tr": "Ebû Hanîfe'nin Kur'an'ın tamamını bir rekâtta okuduğu iki ayrı yoldan rivayet edilmiştir."},
 "tokens": [
  W("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ حَرْفُ تَحْقِيقٍ.", "قَدْ affirms the past verb after it.", "kad tahkîk harfi.", kind="isti"),
  MAJHUL("رُوِيَ", "rawa", ["naqis-verbs"], note_ar="، وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» وَمَا بَعْدَهَا", note_en="; its deputy doer is the masdar that أَنَّ builds after it", note_tr="; nâib-i fâili, ardından gelen enne'nin kurduğu müevvel masdardır"),
  MINP(),
  J("وَجْهَيْنِ", "wajh", (" — أَيْ مِنْ طَرِيقَيْنِ، بِإِسْنَادَيْنِ", " — the dual: «by two ways», that is, two chains of transmission", " — tesniye: «iki yoldan», yani iki senedle"), extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", punct=":"),
  ANNA_T((" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ", "; the masdar it builds is the deputy doer, in the seat of raf'", "; kurduğu müevvel masdar nâib-i fâil olarak mahallen merfû")),
  AB("أَبَا", "ism_anna"), HANIFA(),
  MADI("قَرَأَ", "qaraa", hidden=True, **N3(KH_ANNA_CL)),
  O("الْقُرْآنَ", "quran"),
  tok("كُلَّهُ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
    "تَوْكِيدٌ مَعْنَوِيٌّ لِـ«الْقُرْآنَ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A tawkid of meaning «all of it», in nasb like «the Qurʾān», which it strengthens; annexed to the pronoun, which fills the seat of jarr.",
    "Ma'nevî te'kîd «tamamı», pekiştirdiği «Kur'an» gibi mansûb; zamire muzâf, zamir mahallen mecrûr.",
    segments=[seg("كُلَّ", "kull", "noun"), seg("هُ", "pron-3ms", "pron")]),
  FIP(), J("رَكْعَةٍ", "raka", (" — اسْمُ مَرَّةٍ مِنْ رَكَعَ", " — a noun of one act, from رَكَعَ «to bow»", " — rakea'dan ism-i merre"), punct=".")]})

S4.append({"id": "s6", "translation": {
  "en": "ʿAbd al-Raḥmān ibn Muḥammad ibn al-Mughīra said: I saw Abū Ḥanīfa as an old man giving fatwā to the people in the mosque of Kufa, with a tall black cap on his head.",
  "tr": "Abdurrahman b. Muhammed b. Mugîre dedi ki: Ebû Hanîfe'yi yaşlı bir zât iken, Kûfe mescidinde insanlara fetva verirken gördüm; başında uzun siyah bir kalensüve vardı."},
 "tokens": [
  QALA("قَالَ"),
  F("عَبْدُ", "abd", MUDAF, extra=["idafa-definiteness"]), MI("الرَّحْمٰنِ", "rahman", pos="propn"),
  BN("raf", "عَبْدُ الرَّحْمٰنِ", "ʿAbd al-Raḥmān", "Abdurrahman"), MI("مُحَمَّدِ", "muhammad", DROP, "propn"),
  BN("jarr", "مُحَمَّدِ", "Muḥammad", "Muhammed"),
  MI("الْمُغِيرَةِ", "mughira", (" — وَجُرَّ بِالْكَسْرَةِ مَعَ التَّأْنِيثِ لِأَنَّهُ مُعَرَّفٌ بِأَلْ", " — though a name with the feminine ta, it takes the kasra because it carries ال", " — tâ'lı alem olmakla birlikte el-takısı aldığı için kesre ile"), "propn", punct=":"),
  MADI_T("رَأَيْتُ", "raa", who="ana", extra=["naqis-verbs"], note_ar=MAQUL_CL[0], note_en=MAQUL_CL[1], note_tr=MAQUL_CL[2]),
  AB("أَبَا", "maful"), HANIFA(),
  HAL("شَيْخًا", "shaykh", note_ar=" — حَالٌ جَامِدَةٌ مُؤَوَّلَةٌ بِالْمُشْتَقِّ، أَيْ: كَبِيرَ السِّنِّ", note_en=" — a hal that is not a derived adjective, read as one: «being advanced in years»", note_tr=" — müştak ile te'vîl edilen câmid hâl: «yaşlı olarak»"),
  MUDARI("يُفْتِي", "afta", ["form-iv-verbs", "jumla-sifa"], naqis="ي", **N3(NAAT_OF("nasb", "شَيْخًا", "an old man", "yaşlı zât"))),
  O("النَّاسَ", "nas"),
  BI_NOUN("بِمَسْجِدِ", "masjid", "مَسْجِدِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَالْبَاءُ بِمَعْنَى «فِي»", note_en=", annexed — the ba here means «in»", note_tr=", muzâf — bâ burada «fî» anlamındadır"),
  MI("الْكُوفَةِ", "kufa", pos="propn", punct="،"),
  ALAP(),
  ENC_NOUN("رَأْسِهِ", "ras", "هِ", "majr", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ", note_en="; the jarr phrase hangs on an omitted word that is the FRONTED khabar", note_tr="; câr-mecrûr öne alınmış mahzûf habere müteallik"),
  MBM("قَلَنْسُوَةٌ", "qalansuwa", (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ مِنْ «أَبَا حَنِيفَةَ»", " — the clause is a second hal of «Abū Ḥanīfa», in the seat of nasb", " — cümle «Ebû Hanîfe»den ikinci hâl olarak mahallen mansûb"), extra=["al-hal-jumla-wa-rabituha"]),
  NA("سَوْدَاءُ", "aswad", "raf", ("قَلَنْسُوَةٌ", "a cap", "kalensüve"), (" بِلَا تَنْوِينٍ — مُؤَنَّثُ أَسْوَدَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", ", with no tanwin — the feminine of أَسْوَد, barred from tanwin by its long feminine alif", "; tenvinsiz — esved'in müennesi; elif-i memdûde ile bittiği için gayr-i munsarif"), extra=["mamnu-min-sarf", "ism-mamdud", "sifa-mushabbaha"]),
  NA("طَوِيلَةٌ", "tawil-long", "raf", None, extra=["sifa-mushabbaha"], punct=".", nth="2")]})

# ================================================ Chapter 5 — الْمَنْصُورُ وَالْقَضَاءُ (6/401) ================================================
AMIR_MUMININ = lambda role, n=Z: [
  {"maful": O("أَمِيرَ", "amir", cat(MUDAF, n), extra=["idafa-definiteness"]), "mubtada": MB("أَمِيرُ", "amir", cat(MUDAF, n), extra=["idafa-definiteness"])}[role],
  tok("الْمُؤْمِنِينَ", "mumin", "noun", ["idafa-definiteness", "jam-mudhakkar-salim", "ism-fail"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَ«أَمِيرُ الْمُؤْمِنِينَ» لَقَبُ الْخَلِيفَةِ.",
    "The second term of the idafa, in jarr by the ya — a sound masculine plural; «Commander of the Faithful» is the caliph's title.",
    "Muzâfun ileyh, cem-i müzekker sâlim olduğu için yâ ile mecrûr — «müminlerin emiri» halifenin lakabıdır.")]
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Isḥāq ibn Ibrāhīm al-Zuhrī said, from Bishr ibn al-Walīd, who said: Al-Manṣūr sent for Abū Ḥanīfa and pressed him to take the judgeship,",
  "tr": "İshâk b. İbrâhîm ez-Zührî, Bişr b. Velîd'den naklen dedi ki: Mansûr, Ebû Hanîfe'yi çağırttı ve ondan kadılığı üstlenmesini istedi;"},
 "tokens": [
  QALA("قَالَ"),
  F("إِسْحَاقُ", "ishaq", D_AJ_R, "propn", DG), BN("raf", "إِسْحَاقُ", "Isḥāq", "İshâk"),
  MI("إِبْرَاهِيمَ", "ibrahim", D_AJ, "propn", DG, sign=FATHA_JARR),
  NA("الزُّهْرِيُّ", "zuhri", "raf", ("إِسْحَاقُ", "Isḥāq", "İshâk"), (" — اسْمٌ مَنْسُوبٌ إِلَى بَنِي زُهْرَةَ", " — a nisba to the Banū Zuhra", " — Zühre oğullarına nisbet"), "propn", ["ism-mansub"]),
  AN_PREP(RAWI), J("بِشْرِ", "bishr", DROP, "propn"), BN("jarr", "بِشْرِ", "Bishr", "Bişr"), MI("الْوَلِيدِ", "walid-alam", pos="propn", punct="،"),
  QALA("قَالَ", hidden=True, punct=":"),
  MADI("طَلَبَ", "talaba", **N3(MAQUL_CL)),
  F("الْمَنْصُورُ", "mansur-caliph", (" — لَقَبُ الْخَلِيفَةِ أَبِي جَعْفَرٍ", " — the title of the caliph Abū Jaʿfar", " — Halife Ebû Ca'fer'in lakabı"), "propn"),
  AB("أَبَا", "maful"), HANIFA(punct="،"),
  ENC_MADI("فَأَرَادَهُ", "arada", "هُ", ["form-iv-verbs", "hollow-verbs"], hidden=True, note_ar=" — أَرَادَهُ عَلَى الْأَمْرِ: طَلَبَهُ مِنْهُ وَحَمَلَهُ عَلَيْهِ", note_en=" — أَرَادَهُ عَلَى: «he sought it of him, pressed him to it»", note_tr=" — «erâdehû alâ»: ondan bir şeyi istemek, onu ona zorlamak"),
  ALAP(), J("الْقَضَاءِ", "qada", (" — أَيْ وِلَايَةِ الْقَضَاءِ", " — that is, the office of judge", " — yani kadılık görevi"), extra=["masdar", "ism-mamdud"], punct="،")]})

S5.append({"id": "s2", "translation": {
  "en": "and swore that he must surely take the office; but he refused, and swore: «I will not do it.»",
  "tr": "ve onun bu görevi mutlaka üstleneceğine yemin etti; o ise kabul etmedi ve «Ben bunu yapmam» diye yemin etti."},
 "tokens": [
  MADI("وَحَلَفَ", "halafa", hidden=True, **N3((" (الْمَنْصُورُ)", " (al-Manṣūr)", " (Mansûr)"))),
  tok("لَيَلِيَنَّ", "waliya", "verb", ["nun-tawkid", "nun-al-tawkid-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "mithal-verbs", "naqis-verbs"],
    "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَيَلِيَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالنُّونُ حَرْفُ تَوْكِيدٍ لَا مَحَلَّ لَهُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (أَبُو حَنِيفَةَ) — وَالْمَفْعُولُ مَحْذُوفٌ أَيْ: لَيَلِيَنَّ الْقَضَاءَ؛ وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا.",
    "The lam opens the answer of the oath; يَلِيَنَّ is a present verb built on fatha because the heavy nun of emphasis is attached — that nun is a particle with no seat; the doer is a hidden «he» (Abū Ḥanīfa), and the object is left unsaid: «he shall surely take (the judgeship)». The clause is the oath's answer and has no seat.",
    "Lâm kasemin cevabına gelmiştir; يَلِيَنَّ şeddeli te'kîd nûnu bitiştiği için fetha üzere mebnî muzâridir — nûn te'kîd harfidir, mahalli yoktur; fâil gizli zamir «o» (Ebû Hanîfe), mef'ûl hazfedilmiştir: «(kadılığı) mutlaka üstlenecek». Cümle kasemin cevabıdır, mahalli yoktur.", punct="،",
    segments=[seg("لَ", "lam-qasam", "part"), seg("يَلِيَ", "waliya", "verb"), seg("نَّ", "nun-tawkid", "part")]),
  MADI_ALIF("فَأَبَى", "aba", hidden=True, punct="،", **N3((" (أَبُو حَنِيفَةَ)", " (Abū Ḥanīfa)", " (Ebû Hanîfe)"))),
  MADI("وَحَلَفَ", "halafa", hidden=True, punct=":"),
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna", "al-bariz-al-muttasil", "ya-al-mutakallim", "al-qasam-wal-shart-fil-kafiya"],
    "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — كُسِرَتْ هَمْزَتُهَا لِوُقُوعِهَا فِي جَوَابِ الْقَسَمِ — وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُهَا، وَحُذِفَتْ نُونُ الْوِقَايَةِ تَخْفِيفًا.",
    "إِنَّ is the particle of emphasis — its hamza takes kasra because it opens the answer of an oath; the speaker's ya is its noun, in the seat of nasb (the guarding nun is dropped for lightness).",
    "İnne te'kîd ve nasb harfi — kasemin cevabında olduğu için hemzesi kesrelidir; mütekellim yâ'sı ismi, mahallen mansûb (vikâye nûnu hafiflik için düşmüştür).",
    segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  LA_NAFIYA(),
  MUDARI("أَفْعَلُ", "faala", who="أَنَا", wujub=True, punct=".", **N3(KH_INNA))]})

S5.append({"id": "s3", "translation": {
  "en": "Al-Rabīʿ the chamberlain said: «You see the Commander of the Faithful swearing — and you swear?»",
  "tr": "Hâcib Rebî' dedi ki: «Müminlerin emirinin yemin ettiğini görüyorsun; sen de mi yemin ediyorsun?»"},
 "tokens": [
  QALA("فَقَالَ"),
  F("الرَّبِيعُ", "rabi-name", pos="propn"),
  NA("الْحَاجِبُ", "hajib", "raf", ("الرَّبِيعُ", "al-Rabīʿ", "Rebî'"), (" — اسْمُ فَاعِلٍ مِنْ حَجَبَ: مَنْ يَقِفُ عَلَى بَابِ الْخَلِيفَةِ", " — the active participle of حَجَبَ: the one who keeps the caliph's door", " — hacebe'nin ism-i fâili: halifenin kapısında duran görevli"), extra=["ism-fail"], punct=":"),
  MUDARI("تَرَى", "raa", who="أَنْتَ", naqis="ا", wujub=True, **N3((" — وَالِاسْتِفْهَامُ مُقَدَّرٌ، أَيْ: أَتَرَى؟ وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", " — the question is understood without its hamza: «do you see…?»; the clause is what is said", " — istifhâm hemzesi mukadderdir: «görüyor musun?»; cümle mekûlü'l-kavldir"))),
  *AMIR_MUMININ("maful"),
  MUDARI("يَحْلِفُ", "halafa", ["al-hal-jumla-wa-rabituha"], **N3((" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «أَمِيرَ الْمُؤْمِنِينَ»", "; the clause is a hal of «the Commander of the Faithful», in the seat of nasb", "; cümle «müminlerin emiri»nden hâl, mahallen mansûb"))),
  PRON_MUB("وَأَنْتَ", "anta", pre="hal"),
  MUDARI("تَحْلِفُ", "halafa", who="أَنْتَ", wujub=True, punct="؟", **N3(KH_CL))]})

S5.append({"id": "s4", "translation": {
  "en": "He said: «The Commander of the Faithful is better able than I to expiate his oath.»",
  "tr": "Dedi ki: «Müminlerin emiri, yemininin kefâretini ödemeye benden daha muktedirdir.»"},
 "tokens": [
  QALA_HID(),
  *AMIR_MUMININ("mubtada"),
  ALAP(JM("مُتَعَلِّقٌ بِـ«أَقْدَرُ» مُقَدَّمٌ عَلَيْهِ", "attaches to «better able» and is placed before it", "«daha muktedir»e müteallik; ondan önce gelmiştir")),
  J("كَفَّارَةِ", "kaffara", MUDAF, extra=["idafa-definiteness"]),
  ENC_NOUN("يَمِينِهِ", "yamin", "هِ", "mudaf"),
  KB("أَقْدَرُ", "aqdar", (" بِلَا تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", ", with no tanwin — an elative, barred from tanwin as an adjective on the pattern of a verb", "; tenvinsiz — vasfiyyet ve fiil vezni sebebiyle gayr-i munsarif ism-i tafdîl"), ["ism-tafdil", "mamnu-min-sarf"]),
  tok("مِنِّي", "min", "prep", ["huruf-jarr", "ya-al-mutakallim", "al-bariz-al-muttasil", "ism-tafdil"],
    "مِنْ حَرْفُ جَرٍّ يَدْخُلُ عَلَى الْمُفَضَّلِ عَلَيْهِ، وَالنُّونُ لِلْوِقَايَةِ أُدْغِمَتْ فِيهَا نُونُ مِنْ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.",
    "مِنْ «than» is the jarr letter that marks the one surpassed; the nun of guarding takes the nun of مِنْ into its doubling, and the speaker's ya fills the seat of jarr.",
    "Min cer harfi; kendisinden üstün tutulanın başına gelir; min'in nûnu vikâye nûnuna idgâm edilmiş, mütekellim yâ'sı mahallen mecrûr.", punct=".",
    segments=[seg("مِنْ", "min", "prep"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])]})

S5.append({"id": "s5", "translation": {
  "en": "So he ordered him to prison, and he died in it, in Baghdad.",
  "tr": "Bunun üzerine onun hapse götürülmesini emretti; o da Bağdat'ta, hapiste vefat etti."},
 "tokens": [
  MADI("فَأَمَرَ", "amara-command", hidden=True, **N3((" (الْمَنْصُورُ)", " (al-Manṣūr)", " (Mansûr)"))),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onun hakkında»)"),
  ILAP(),
  J("السِّجْنِ", "sijn", (" — أَيْ أَمَرَ بِحَمْلِهِ إِلَى السِّجْنِ", " — that is, he ordered him taken to prison", " — yani hapse götürülmesini emretti"), punct="،"),
  MADI("فَمَاتَ", "mata-die", ["hollow-verbs"], hidden=True, **N3((" (أَبُو حَنِيفَةَ)", " (Abū Ḥanīfa)", " (Ebû Hanîfe)"))),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («orada»)"),
  BI_NOUN("بِبَغْدَادَ", "baghdad", "بَغْدَادَ", extra=DG, pos="propn", sign=FATHA_JARR, punct=".",
    note_ar="، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ — وَالْبَاءُ بِمَعْنَى «فِي»", note_en=" — by a fatha standing in for the kasra: a feminine proper name (a city), barred from tanwin; the ba here means «in»", note_tr=" — kesre yerine fetha ile: müennes özel isim (şehir adı), gayr-i munsarif; bâ burada «fî» anlamındadır")]})

# ================================================ Chapter 6 — فِقْهُهُ وَوَفَاتُهُ (6/403) ================================================
TAFDIL = (" — اسْمُ تَفْضِيلٍ", " — an elative", " — ism-i tafdîl")
S6 = []
S6.append({"id": "s1", "translation": {
  "en": "Ibn al-Mubārak said: Abū Ḥanīfa is the most learned of people in fiqh.",
  "tr": "İbnü'l-Mübârek dedi ki: Ebû Hanîfe insanların en fakihidir."},
 "tokens": [
  QALA_ISTI(),
  F("ابْنُ", "ibn", MUDAF, extra=["idafa-definiteness"]), MI("الْمُبَارَكِ", "mubarak-name", pos="propn", punct=":"),
  AB("أَبُو", "mubtada"), HANIFA(),
  KB("أَفْقَهُ", "afqah", cat(MUDAF, (" — اسْمُ تَفْضِيلٍ مِنْ فَقُهَ، مُضَافٌ إِلَى مَعْرِفَةٍ؛ وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", " — the elative of فَقُهَ, annexed to a definite noun: «the most learned in fiqh of…»; the clause is what is said", " — fekuhe'den ism-i tafdîl, ma'rifeye muzâf: «…-in en fakihi»; cümle mekûlü'l-kavldir")), ["ism-tafdil", "idafa-definiteness"]),
  MI("النَّاسِ", "nas", punct=".")]})

S6.append({"id": "s2", "translation": {
  "en": "Al-Shāfiʿī said: In fiqh, people are the dependants of Abū Ḥanīfa.",
  "tr": "Şâfiî dedi ki: İnsanlar fıkıhta Ebû Hanîfe'nin iyâlidir (ona muhtaçtır)."},
 "tokens": [
  QALA_ISTI(),
  F("الشَّافِعِيُّ", "shafii", (" — اسْمٌ مَنْسُوبٌ إِلَى جَدِّهِ شَافِعٍ", " — a nisba to his forefather Shāfiʿ", " — dedesi Şâfi'e nisbet"), "propn", ["ism-mansub"], punct=":"),
  MB("النَّاسُ", "nas"),
  FIP(JM("مُتَعَلِّقٌ بِـ«عِيَالٌ» مُقَدَّمٌ عَلَيْهِ", "attaches to «dependants» and is placed before it", "«iyâl»e müteallik; ondan önce gelmiştir")), J("الْفِقْهِ", "fiqh", extra=["masdar"]),
  KB("عِيَالٌ", "iyal", cat((" — جَمْعُ عَيِّلٍ: مَنْ يَعُولُهُ غَيْرُهُ وَيُنْفِقُ عَلَيْهِ", " — the plural of عَيِّل: one whom another feeds and keeps", " — ayyil'in cem'i: geçimini başkasının sağladığı kimse"), MAQUL_CL), ["jam-taksir"]),
  ALAP(JM("مُتَعَلِّقٌ بِـ«عِيَالٌ»", "attaches to «dependants»", "«iyâl»e müteallik")), AB("أَبِي", "majr"), HANIFA(punct=".")]})

S6.append({"id": "s3", "translation": {
  "en": "I say: Leadership in fiqh and its fine points is conceded to this imam; and this is a matter in which there is no doubt.",
  "tr": "Derim ki: Fıkıhta ve onun inceliklerinde imamlık bu imama teslim edilmiştir; bu, hakkında şüphe bulunmayan bir husustur."},
 "tokens": [
  MADI_T("قُلْتُ", "qala", who="ana", extra=["hollow-verbs"], punct=":", note_ar="، وَحُذِفَتْ عَيْنُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْقَائِلُ الذَّهَبِيُّ صَاحِبُ الْكِتَابِ", note_en=" (the hollow verb drops its middle letter before the ta) — the speaker is al-Dhahabī, the author", note_tr=" (ecvef fiil, tâ'dan önce orta harfini düşürür) — söyleyen, kitabın müellifi Zehebî'dir"),
  MB("الْإِمَامَةُ", "imama-leadership", cat((" — مَصْدَرُ أَمَّ", " — the masdar of أَمَّ «to lead»", " — emme'nin masdarı"), MAQUL_CL), extra=["masdar"]),
  FIP(JM("مُتَعَلِّقٌ بِـ«الْإِمَامَةُ»", "attaches to «leadership»", "«imamlık»a müteallik")), J("الْفِقْهِ", "fiqh", extra=["masdar"]),
  tok("وَدَقَائِقِهِ", "daqiqa", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "دَقَائِقِ مَعْطُوفٌ عَلَى «الْفِقْهِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ دَقِيقَةٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ.",
    "The waw conjoins; «fine points» is conjoined to «fiqh», in jarr and annexed; the attached «its» is the second term of the idafa, in the seat of jarr — the plural of دَقِيقَة on a diptote pattern, which takes the kasra here because it is annexed.",
    "«ve» + «incelikler», «fıkıh»a ma'tûf, mecrûr, muzâf; bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr — dakîka'nın müntehâ'l-cümû' veznindeki cem'i; muzâf olduğu için kesre ile.",
    segments=[seg("وَ", "wa", "conj"), seg("دَقَائِقِ", "daqiqa", "noun"), seg("هِ", "pron-3ms", "pron")]),
  KB("مُسَلَّمَةٌ", "musallam", (" — اسْمُ مَفْعُولٍ مِنْ سَلَّمَ: مُعْتَرَفٌ بِهَا لَهُ", " — the passive participle of سَلَّمَ: «handed over, conceded»", " — selleme'nin ism-i mef'ûlü: «teslim edilmiş, kabul edilmiş»"), ["ism-maful"]),
  ILAP(JM("مُتَعَلِّقٌ بِـ«مُسَلَّمَةٌ»", "attaches to «conceded»", "«teslim edilmiş»e müteallik")),
  HADHA("جَرٍّ", "jarr", "mecrûr"), BADAL("الْإِمَامِ", "imam", "jarr", punct="،"),
  W("وَهٰذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "هٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
    "«this» is a demonstrative, built on sukun, in the seat of raf' as the mubtada.", "«bu» işaret ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû."),
  KB("أَمْرٌ", "amr"),
  LA_JINS(), ISM_LA("شَكَّ", "shakk"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)", punct=".",
    note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ لَا؛ وَجُمْلَةُ «لَا شَكَّ فِيهِ» فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«أَمْرٌ»",
    note_en="; the jarr phrase hangs on the omitted predicate of لَا, and the clause «there is no doubt in it» qualifies «a matter», in the seat of raf'",
    note_tr="; câr-mecrûr lâ'nın mahzûf haberine müteallik; «onda şüphe yok» cümlesi «husus» için na't, mahallen merfû")]})

S6.append({"id": "s4", "translation": {
  "en": "«And nothing at all holds true in men's minds, if the daylight itself stands in need of a proof.»",
  "tr": "«Gündüzün kendisi delile muhtaç olursa, zihinlerde hiçbir şey sahih olmaz.»"},
 "tokens": [
  tok("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"],
    "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا فِي الْقَصِيدَةِ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ خَبَرُهُ — وَالْبَيْتُ لِلْمُتَنَبِّي، تَمَثَّلَ بِهِ الذَّهَبِيُّ.",
    "The waw belongs to what came before it in the poem; لَيْسَ is the frozen defective verb, built on fatha: its noun is an unspoken «pronoun of the matter» and the clause after it is its predicate, in the seat of nasb — the line is al-Mutanabbī's, which al-Dhahabī quotes to make his point.",
    "Vâv, kasidede kendinden öncesine bağlıdır; leyse fetha üzere mebnî câmid nâkıs fiildir: ismi hazfedilmiş zamîr-i şân, sonraki cümle haberi olarak mahallen mansûb — beyit Mütenebbî'nindir; Zehebî onu temsil yoluyla zikretmiştir.",
    segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  MUDARI_DF("يَصِحُّ", "sahha", ["doubled-verbs"]),
  FIP(),
  J("الْأَذْهَانِ", "dhihn", (" — جَمْعُ ذِهْنٍ", " — the plural of ذِهْن «mind»", " — zihn'in cem'i"), extra=["jam-taksir"]),
  F("شَيْءٌ", "shay", punct="*"),
  tok("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"],
    "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ — وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.",
    "إِذَا «when, if»: an adverb of time with the force of a condition, built on sukun in the seat of nasb — its answer is left unsaid, for what came before it shows it.",
    "İzâ «-dığı zaman, -se»: şart mânâsı taşıyan zaman zarfı, sükûn üzere mebnî, mahallen mansûb — cevabı mahzûftur; öncesi ona delâlet eder."),
  MADI("احْتَاجَ", "ihtaja", ["form-viii-verbs", "hollow-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا", note_en="; its doer follows — the clause fills the seat of jarr, annexed to إِذَا", note_tr="; fâili ardından gelir — cümle izâ'ya muzâfun ileyh olarak mahallen mecrûr"),
  F("النَّهَارُ", "nahar"),
  ILAP(),
  J("دَلِيلِ", "dalil-proof", (" — وَلَمْ يُنَوَّنْ لِأَنَّهُ قَافِيَةُ الْبَيْتِ، تُشْبَعُ كَسْرَتُهُ", " — it carries no tanwin because it is the rhyme-word of the line: its kasra is drawn out", " — beytin kafiyesi olduğu için tenvin almamıştır; kesresi uzatılarak okunur"), extra=["al-qafiya"])]})

S6.append({"id": "s5", "translation": {
  "en": "His life could well fill two volumes of its own — may God be pleased with him, and have mercy on him.",
  "tr": "Onun hayatı başlı başına iki ciltte ele alınmaya elverişlidir — Allah ondan razı olsun ve ona rahmet etsin."},
 "tokens": [
  W("وَسِيرَتُهُ", "sira", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"],
    "سِيرَةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "«life-story» is the mubtada, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr.",
    "«hayat hikâyesi» mübtedâ, merfû, muzâf; bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr.", kind="isti",
    extra_segs=[seg("سِيرَتُ", "sira", "noun"), seg("هُ", "pron-3ms", "pron")]),
  MUDARI("تَحْتَمِلُ", "ihtamala", ["form-viii-verbs"], who="هِيَ", **N3(KH_CL)),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«تَحْتَمِلُ»", "; the clause it builds is the object of «can bear», in the seat of nasb", "; kurduğu müevvel masdar «elverişlidir»in mef'ûlü, mahallen mansûb"),
  MAJHUL_M("تُفْرَدَ", "afrada", "مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "in nasb by أَنْ, its sign the fatha", "en ile mansûb, alâmeti fetha", who="هِيَ",
    extra=["nawasib-wa-jawazim-al-mudari", "form-iv-verbs"], n=(" — أَيْ تُجْعَلَ فِي كِتَابٍ مُفْرَدٍ", " — «to be set apart», that is, given a book of its own", " — yani müstakil bir kitapta ele alınması")),
  FIP(),
  J("مُجَلَّدَيْنِ", "mujallad", (" — اسْمُ مَفْعُولٍ مِنْ جَلَّدَ الْكِتَابَ", " — the dual of مُجَلَّد, the passive participle of جَلَّدَ «to bind (a book)»", " — cellede'nin ism-i mef'ûlü olan mücelled'in tesniyesi"), extra=["al-muthanna", "ism-maful"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", punct=" —"),
  MADI("رَضِيَ", "radiya", ["khabar-fi-mana-al-insha", "naqis-verbs"], note_ar=" — وَالْجُمْلَةُ دُعَائِيَّةٌ لَا مَحَلَّ لَهَا: لَفْظُهَا خَبَرٌ وَمَعْنَاهَا الدُّعَاءُ", note_en=" — a sentence of prayer with no seat: a statement in form, a supplication in meaning", note_tr=" — dua cümlesidir, mahalli yoktur: lafzı haber, mânâsı duadır"),
  ALLAH_F(),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)", punct="،"),
  ENC_MADI("وَرَحِمَهُ", "rahima", "هُ", hidden=True, punct=" —.")]})

S6.append({"id": "s6", "translation": {
  "en": "He died a martyr, given poison to drink, in the year one hundred and fifty, at the age of seventy; over him stand a great dome and a splendid shrine in Baghdad — and God knows best.",
  "tr": "Yüz elli yılında, kendisine zehir içirilmiş olarak, şehit olarak vefat etti; yetmiş yaşındaydı. Bağdat'ta kabrinin üzerinde büyük bir kubbe ve görkemli bir meşhed vardır — en doğrusunu Allah bilir."},
 "tokens": [
  tok("تُوُفِّيَ", "tawaffa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-v-verbs", "naqis-verbs"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — ضُمَّ أَوَّلُهُ وَثَانِيهِ لِأَنَّهُ مَبْدُوءٌ بِتَاءٍ زَائِدَةٍ، وَكُسِرَ مَا قَبْلَ آخِرِهِ؛ أَيْ تَوَفَّاهُ اللهُ.",
    "A past verb in the passive, built on fatha; its deputy doer is a hidden «he» — its first AND second letters take damma because it opens with an added ta, and the letter before the last a kasra: «he was taken (in death)», that is, God took him.",
    "Meçhul mâzî, fetha üzere mebnî; nâib-i fâili gizli zamir «o» — zâid tâ ile başladığı için birinci ve ikinci harfi mazmûm, sondan önceki harfi meksûrdur: «vefat ettirildi», yani Allah onun ruhunu aldı."),
  HAL("شَهِيدًا", "shahid-martyr", punct="،"),
  tok("مَسْقِيًّا", "masqiyy", "noun", ["hal", "ism-maful", "naqis-verbs"],
    "حَالٌ ثَانِيَةٌ مَنْصُوبَةٌ بِالْفَتْحَةِ — اسْمُ مَفْعُولٍ مِنْ سَقَى، أَصْلُهُ مَسْقُويٌ: قُلِبَتِ الْوَاوُ يَاءً وَأُدْغِمَتْ فِي الْيَاءِ وَكُسِرَ مَا قَبْلَهَا؛ أَيْ سُقِيَ السُّمَّ.",
    "A second hal, in nasb — the passive participle of سَقَى, from مَسْقُويٌ: the waw turned into ya, merged into the ya, and the letter before took kasra; «given to drink», that is, poison.",
    "İkinci hâl, mansûb — sekâ'nın ism-i mef'ûlü; aslı مَسْقُويٌ: vâv yâ'ya çevrilip yâ'ya idgâm edilmiş, önceki harf kesrelenmiştir; «içirilmiş», yani zehir içirilmiş.", punct="،"),
  FIP(), J("سَنَةِ", "sana", MUDAF, extra=["idafa-definiteness"]),
  MI("خَمْسِينَ", "khamsun", (" — مِنْ أَلْفَاظِ الْعُقُودِ", " — one of the tens, which decline like the sound masculine plural", " — ukûd lafızlarındandır; cem-i müzekker sâlim gibi i'râblanır"), extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"),
  ATF("وَمِائَةٍ", "mia", case="jarr", extra=["asma-al-adad-fil-kafiya"], punct="،", note_ar=" — وَتُكْتَبُ بِأَلِفٍ لَا تُنْطَقُ", note_en=" — its alif is written, not spoken (miʾa)", note_tr=" — elifi yazılır, okunmaz"),
  W("وَلَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
    "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "the lam is a jarr letter and the attached «him» fills the seat of jarr — the jarr phrase hangs on an omitted word that is the FRONTED khabar; the clause is a hal, in the seat of nasb.",
    "lâm cer harfi; bitişik «o» zamiri mahallen mecrûr — câr-mecrûr öne alınmış mahzûf habere müteallik; cümle hâl olarak mahallen mansûb.", kind="hal",
    extra_segs=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
  MBM("سَبْعُونَ", "sabun", (" — مِنْ أَلْفَاظِ الْعُقُودِ", " by the waw — one of the tens, which decline like the sound masculine plural", " — ukûd lafızlarındandır; cem-i müzekker sâlime mülhak olduğu için vâv ile"), extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"),
  tok("سَنَةً", "sana", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"],
    "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ الْمَعْدُودَ بَعْدَ الْعَدَدِ، وَتَمْيِيزُ الْعُقُودِ مُفْرَدٌ مَنْصُوبٌ.",
    "A specifier (tamyiz), in nasb — it names what the number counts; after the tens the counted noun is singular and in nasb.",
    "Temyîz, mansûb — sayının neyi saydığını bildirir; ukûddan sonra ma'dûd müfred ve mansûb gelir.", punct="،"),
  W("وَعَلَيْهِ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
    "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ — أَيْ عَلَى قَبْرِهِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ.",
    "عَلَى is a jarr letter and the attached «him» fills the seat of jarr — «over him», that is, over his grave; the jarr phrase hangs on an omitted word that is the FRONTED khabar.",
    "alâ cer harfi; bitişik «o» zamiri mahallen mecrûr — «üzerinde», yani kabrinin üzerinde; câr-mecrûr öne alınmış mahzûf habere müteallik.", kind="isti",
    extra_segs=[seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")]),
  MBM("قُبَّةٌ", "qubba"),
  NA("عَظِيمَةٌ", "azim", "raf", None, extra=["sifa-mushabbaha"], punct="،"),
  ATF("وَمَشْهَدٌ", "mashhad", case="raf", note_ar=" — اسْمُ مَكَانٍ مِنْ شَهِدَ: مَوْضِعٌ يُزَارُ", note_en=" — a noun of place from شَهِدَ: a shrine, a place of visitation", note_tr=" — şehide'den ism-i mekân: ziyaret edilen yer"),
  NA("فَاخِرٌ", "fakhir", "raf", None, extra=["ism-fail"]),
  BI_NOUN("بِبَغْدَادَ", "baghdad", "بَغْدَادَ", extra=DG, pos="propn", sign=FATHA_JARR, punct=" —",
    note_ar="، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ — وَالْبَاءُ بِمَعْنَى «فِي»", note_en=" — by a fatha standing in for the kasra: a feminine proper name (a city), barred from tanwin; the ba here means «in»", note_tr=" — kesre yerine fetha ile: müennes özel isim (şehir adı), gayr-i munsarif; bâ burada «fî» anlamındadır"),
  W("وَاللهُ", "allah", "propn", ["mubtada-khabar"], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "the Name of Majesty is the mubtada, in raf'.", "lafza-i celâl mübtedâ, merfû.", kind="isti"),
  KB("أَعْلَمُ", "alam-tafdil", (" بِلَا تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ", ", with no tanwin — an elative, barred from tanwin", "; tenvinsiz — gayr-i munsarif ism-i tafdîl"), ["ism-tafdil", "mamnu-min-sarf"], punct=" —.")]})

CHAPS = [S1, S2, S3, S4, S5, S6]
# tidy the grammar anchors: no tag twice on a token, and a derived (mazīd) verb does not carry the Form-I bāb tag that the
# kit's MADI helper adds by default (احْتَاجَ is Form VIII).
for _S in CHAPS:
    for _s in _S:
        for _t in _s["tokens"]:
            _g = list(dict.fromkeys(_t.get("grammar", [])))
            if any(re.fullmatch(r"form-[ivx]+-verbs", x) for x in _g): _g = [x for x in _g if x != "thulathi-mujarrad-babs"]
            _t["grammar"] = _g

# ---- the lexicon: every key by lemma identity from the shelf (the majority reading of a key wins) ------------------------
PKGS = sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
_M = {p: (json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
          if (ROOT / "content/samples" / p / "morphology.json").exists() else {}) for p in PKGS}
_DIA = re.compile("[ً-ٰ]")
def _lemma_id(e): return _DIA.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))
def find_entry(k):
    """(gloss entry, owning package) — the reading of the key that most packages hold; ties go to the alphabetical first"""
    holders = [(p, _G[p][k]) for p in PKGS if k in _G[p]]
    if not holders: return None, None
    votes = collections.Counter(_lemma_id(e) for p, e in holders)
    best = votes.most_common(1)[0][0]
    group = [(p, e) for p, e in holders if _lemma_id(e) == best]
    if group[0][1].get("pos") == "verb":
        for p, e in group:
            if k in _M[p]: return e, p
    gl = collections.Counter(json.dumps(e.get("gloss"), ensure_ascii=False, sort_keys=True) for p, e in group).most_common(1)[0][0]
    for p, e in group:
        if json.dumps(e.get("gloss"), ensure_ascii=False, sort_keys=True) == gl: return e, p
    return group[0][1], group[0][0]

def NM(lemma, en, tr, **kw): return {"lemma": lemma, "pos": "propn", "gloss": {"en": en, "tr": tr}, "level": 5, **kw}
def NN(lemma, root, en, tr, **kw): return {"lemma": lemma, "root": root, "pos": "noun", "gloss": {"en": en, "tr": tr}, "level": 5, **kw}
NEW_GLOSS = {
 "numan": NM("النُّعْمَان", "al-Nuʿmān — the given name of Abū Ḥanīfa: al-Nuʿmān ibn Thābit (80–150 AH), the imam of Kufa", "Nu'mân — Ebû Hanîfe'nin adı: Nu'mân b. Sâbit (h. 80–150), Kûfe'nin imamı"),
 "zuta": NM("زُوطَى", "Zūṭā — Abū Ḥanīfa's grandfather, a man of Kābul; a foreign name ending in alif maqṣūra, so its case-vowels are estimated (the edition vowels the zāy with ḍamma; Zawṭā is also transmitted)", "Zûtâ — Ebû Hanîfe'nin dedesi, Kâbilli; maksûr yabancı isim olduğu için harekeleri takdîrîdir (matbû nüsha zây'ı damme ile harekelemiştir; Zevtâ okunuşu da nakledilir)"),
 "taymi": NN("تَيْمِيّ", "ت ي م", "a Taymī — of the tribe of Taym (a nisba); here of Taym Allāh ibn Thaʿlaba, by clientage", "Teymî — Teym kabilesine mensup (nisbet); burada velâ yoluyla Teymullah b. Sa'lebe'ye"),
 "thalaba": NM("ثَعْلَبَة", "Thaʿlaba — a man's name with the feminine tāʾ (a diptote); Taym Allāh ibn Thaʿlaba is a clan of Bakr ibn Wāʾil", "Sa'lebe — tâ'lı erkek ismi (gayr-i munsarif); Teymullah b. Sa'lebe, Bekr b. Vâil'in bir koludur"),
 "furs": NN("الْفُرْس", "ف ر س", "the Persians (a collective name of the people)", "Fârisîler, İranlılar (kavim adı)"),
 "anas": NM("أَنَس", "Anas — Anas ibn Mālik (d. c. 93 AH), the servant of the Prophet ﷺ and one of the last Companions to die", "Enes — Enes b. Mâlik (ö. y. 93), Hz. Peygamber'in ﷺ hizmetçisi ve en son vefat eden sahâbîlerden"),
 "ata-name": NM("عَطَاء", "ʿAṭāʾ — a man's name («a gift»); here ʿAṭāʾ ibn Abī Rabāḥ (d. 114 AH), the jurist of Mecca", "Atâ — erkek ismi («bağış»); burada Mekke fakihi Atâ b. Ebî Rebâh (ö. 114)"),
 "shabi": NM("الشَّعْبِيّ", "al-Shaʿbī — ʿĀmir ibn Sharāḥīl (d. c. 104 AH), the great Successor and judge of Kufa", "Şa'bî — Âmir b. Şerâhîl (ö. y. 104), Kûfeli büyük tâbiî ve kadı"),
 "ijli": NM("الْعِجْلِيّ", "al-ʿIjlī — Aḥmad ibn ʿAbd Allāh al-ʿIjlī (d. 261 AH), the Kufan ḥadīth critic; a nisba to the Banū ʿIjl", "İclî — Ahmed b. Abdullah el-İclî (ö. 261), Kûfeli hadis münekkidi; İcl oğullarına nisbet"),
 "zayyat": NM("الزَّيَّات", "al-Zayyāt «the oil-seller» — the byname of Ḥamza ibn Ḥabīb (d. 156 AH), the Kufan reader of the Qurʾān; on فَعَّال, the pattern of a trade", "Zeyyât «zeytinyağı satıcısı» — Kûfeli kıraat imamı Hamza b. Habîb'in (ö. 156) lakabı; meslek bildiren fa''âl vezninde"),
 "khazzaz": NN("خَزَّاز", "خ ز ز", "a khazzāz — a dealer in khazz cloth (فَعَّال of a trade)", "hazzâz — hazz kumaşı satan tüccar (meslek bildiren fa''âl)"),
 "khazz": NN("خَزّ", "خ ز ز", "khazz — a cloth woven of silk, or of wool and silk", "hazz — ipekten veya yün ile ipekten dokunan kumaş", plural="خُزُوز"),
 "kabul": NM("كَابُل", "Kābul — the city of Kābul (a foreign place-name, a diptote)", "Kâbil — Kâbil şehri (yabancı yer adı, gayr-i munsarif)"),
 "wala": NN("وَلَاء", "و ل ي", "walāʾ — clientage: the tie that binds a freed slave to the one who freed him and to that man's clan", "velâ — âzât edilen köleyi âzât edene ve onun kabilesine bağlayan bağ"),
 "qafl": NM("قَفْل", "Qafl — the Banū Qafl, a clan (so vowelled in the edition)", "Kafl — Kafl oğulları, bir kabile kolu (matbû nüshada böyle harekelenmiştir)"),
 "dukkan": NN("دُكَّان", "د ك ن", "a shop, a stall", "dükkân", plural="دَكَاكِين"),
 "nadr": NM("النَّضْر", "al-Naḍr — a man's name; here al-Naḍr ibn Muḥammad al-Marwazī, a student of Abū Ḥanīfa", "Nadr — erkek ismi; burada Ebû Hanîfe'nin talebesi Nadr b. Muhammed el-Mervezî"),
 "nasa": NM("نَسَا", "Nasā — a town of Khurāsān (a diptote ending in alif)", "Nesâ — Horasan'da bir şehir (elifle biten gayr-i munsarif isim)"),
 "tirmidh": NM("تِرْمِذ", "Tirmidh — a town on the river Jayḥūn (the Oxus); so vowelled in the edition", "Tirmiz — Ceyhun nehri kıyısında bir şehir; matbû nüshada böyle harekelenmiştir"),
 "idris": NM("إِدْرِيس", "Idrīs — a man's name (a foreign name, a diptote)", "İdrîs — erkek ismi (yabancı isim, gayr-i munsarif)"),
 "muqri": NN("مُقْرِئ", "ق ر أ", "a teacher of Qurʾān recitation (ism fāʿil of أَقْرَأَ); printed here with its hamza lightened, الْمُقْرِي — the byname of Abū ʿAbd al-Raḥmān ʿAbd Allāh ibn Yazīd (d. 213 AH)", "kıraat öğreten kimse (akrae'nin ism-i fâili); burada hemzesi tahfif edilerek الْمُقْرِي yazılmıştır — Ebû Abdurrahman Abdullah b. Yezîd'in (ö. 213) lakabı"),
 "babil": NM("بَابِل", "Bābil — Babylon, in Iraq (a diptote)", "Bâbil — Irak'ta Babil (gayr-i munsarif)"),
 "main-name": NM("مَعِين", "Maʿīn — in the name of Yaḥyā ibn Maʿīn (d. 233 AH), the imam of ḥadīth criticism", "Maîn — hadis tenkidinin imamı Yahyâ b. Maîn'in (ö. 233) adında"),
 "muhriz": NM("مُحْرِز", "Muḥriz — a man's name; here in the name of Ibn Muḥriz, who transmitted Ibn Maʿīn's judgements", "Muhriz — erkek ismi; burada İbn Maîn'in görüşlerini nakleden İbn Muhriz'in adında"),
 "ittahama": {"lemma": "اِتَّهَمَ", "root": "و ه م", "pos": "verb", "form": "VIII", "gloss": {"en": "to accuse, to suspect (someone of something, with بِ) — Form VIII of و ه م", "tr": "itham etmek, töhmet altında tutmak (bi ile) — vehm kökünden iftiâl bâbı"}, "level": 5},
 "hubayra": NM("هُبَيْرَة", "Hubayra — in the name of Ibn Hubayra: Yazīd ibn ʿUmar ibn Hubayra (d. 132 AH), the last Umayyad governor of Iraq", "Hübeyre — İbn Hübeyre'nin adında: Yezîd b. Ömer b. Hübeyre (ö. 132), Irak'ın son Emevî valisi"),
 "tadarru": NN("تَضَرُّع", "ض ر ع", "humble entreaty, lowly supplication (masdar of تَضَرَّعَ, Form V)", "tazarru, boyun bükerek yalvarma (tedarraa'nın masdarı, tefa''ul bâbı)"),
 "raka": NN("رَكْعَة", "ر ك ع", "a rakʿa — one cycle of the prayer (a noun of one act, from رَكَعَ)", "rekât — namazın bir bölümü (rakea'dan ism-i merre)", plural="رَكَعَات"),
 "mughira": NM("الْمُغِيرَة", "al-Mughīra — a man's name", "Mugîre — erkek ismi"),
 "qalansuwa": NN("قَلَنْسُوَة", "ق ل س", "a qalansuwa — a tall cap worn on the head (its nūn and wāw are added letters)", "kalensüve — başa giyilen uzun külah (nûn ve vâvı zâiddir)", plural="قَلَانِس"),
 "rabi-name": NM("الرَّبِيع", "al-Rabīʿ — a man's name; here al-Rabīʿ ibn Yūnus (d. c. 169 AH), the chamberlain (ḥājib) of the caliph al-Manṣūr", "Rebî' — erkek ismi; burada Halife Mansûr'un hâcibi Rebî' b. Yûnus (ö. y. 169)"),
 "aqdar": NN("أَقْدَر", "ق د ر", "more able, better able (elative of قَادِر; a diptote)", "daha muktedir, daha güçlü (kâdir'in ism-i tafdîli; gayr-i munsarif)"),
 "afqah": NN("أَفْقَه", "ف ق ه", "more / most learned in fiqh (elative of فَقِيه; a diptote)", "daha fakih, en fakih (fakîh'in ism-i tafdîli; gayr-i munsarif)"),
 "shafii": NM("الشَّافِعِيّ", "al-Shāfiʿī — the imam Muḥammad ibn Idrīs al-Shāfiʿī (150–204 AH)", "Şâfiî — İmam Muhammed b. İdrîs eş-Şâfiî (h. 150–204)"),
 "mubarak-name": NM("الْمُبَارَك", "al-Mubārak — in the name of Ibn al-Mubārak: ʿAbd Allāh ibn al-Mubārak (d. 181 AH), the imam of Marw", "Mübârek — İbnü'l-Mübârek'in adında: Abdullah b. Mübârek (ö. 181), Merv'in imamı"),
 "iyal": NN("عِيَال", "ع ي ل", "dependants — those whom a man feeds and keeps (plural of عَيِّل)", "iyâl — bir kimsenin geçimini üstlendiği kimseler (ayyil'in cem'i)"),
 "imama-leadership": NN("إِمَامَة", "أ م م", "leadership, the rank of an imam (masdar of أَمَّ)", "imamlık, önderlik (emme'nin masdarı)"),
 "musallam": NN("مُسَلَّم", "س ل م", "handed over, conceded, granted without dispute (ism mafʿūl of سَلَّمَ)", "teslim edilmiş, tartışmasız kabul edilmiş (selleme'nin ism-i mef'ûlü)"),
 "mujallad": NN("مُجَلَّد", "ج ل د", "a bound volume (ism mafʿūl of جَلَّدَ «to bind»)", "cilt, mücelled (cellede'nin ism-i mef'ûlü)", plural="مُجَلَّدَات"),
 "masqiyy": NN("مَسْقِيّ", "س ق ي", "given to drink (ism mafʿūl of سَقَى); here: made to drink poison", "içirilmiş (sekâ'nın ism-i mef'ûlü); burada: zehir içirilmiş"),
 "sabun": NN("سَبْعُونَ", "س ب ع", "seventy (declines like the sound masculine plural: سَبْعِينَ)", "yetmiş (cem-i müzekker sâlim gibi i'râblanır: سَبْعِينَ)"),
 "fakhir": NN("فَاخِر", "ف خ ر", "splendid, magnificent (ism fāʿil of فَخَرَ)", "görkemli, muhteşem (fehare'nin ism-i fâili)"),
 "zuhri": NM("الزُّهْرِيّ", "al-Zuhrī — a nisba to the Banū Zuhra; here Isḥāq ibn Ibrāhīm al-Zuhrī", "Zührî — Zühre oğullarına nisbet; burada İshâk b. İbrâhîm ez-Zührî"),
}
# the gloss a reused key shows in THIS text: the lemma is the shelf's, the sense or the person is this entry's (the shelf's own sense is kept beside it)
GLOSS_HERE = {
 "yusuf": ("Yūsuf — a name; here in the kunya of the qāḍī Abū Yūsuf (d. 182 AH), Abū Ḥanīfa's foremost student (elsewhere: the prophet Yūsuf; Yūsuf ibn Khālid al-Samtī)", "Yûsuf — isim; burada Ebû Hanîfe'nin en önde gelen talebesi Kadı Ebû Yûsuf'un (ö. 182) künyesinde (başka yerde: Hz. Yûsuf; Yûsuf b. Hâlid es-Semtî)"),
 "yahya": ("Yaḥyā — a name on the pattern of a verb, a diptote; here Yaḥyā ibn Maʿīn (d. 233 AH) and Yaḥyā ibn al-Naḍr", "Yahyâ — fiil vezninde, gayr-i munsarif isim; burada Yahyâ b. Maîn (ö. 233) ve Yahyâ b. Nadr"),
 "ishaq": ("Isḥāq — a foreign name, a diptote; here Isḥāq ibn Ibrāhīm al-Zuhrī (elsewhere: the prophet Isḥāq)", "İshâk — yabancı isim, gayr-i munsarif; burada İshâk b. İbrâhîm ez-Zührî (başka yerde: Hz. İshâk)"),
 "ibrahim": ("Ibrāhīm — a foreign name, a diptote; here the father of Isḥāq al-Zuhrī (elsewhere: the prophet Ibrāhīm)", "İbrâhîm — yabancı isim, gayr-i munsarif; burada İshâk ez-Zührî'nin babası (başka yerde: Hz. İbrâhîm)"),
 "sulayman": ("Sulaymān — a diptote name; here Sulaymān ibn al-Rabīʿ (elsewhere: the prophet Sulaymān)", "Süleyman — gayr-i munsarif isim; burada Süleyman b. Rebî' (başka yerde: Hz. Süleyman)"),
 "salih-nabi": ("Ṣāliḥ — a man's name; here the ḥāfiẓ Ṣāliḥ ibn Muḥammad (d. 293 AH) (elsewhere: the prophet Ṣāliḥ)", "Sâlih — erkek ismi; burada hâfız Sâlih b. Muhammed (ö. 293) (başka yerde: Hz. Sâlih)"),
 "taym": ("Taym — a tribal name; here Taym Allāh ibn Thaʿlaba, a clan of Bakr ibn Wāʾil", "Teym — kabile adı; burada Bekr b. Vâil'in bir kolu olan Teymullah b. Sa'lebe"),
 "thabit-name": ("Thābit — a man's name («firm»); here Abū Ḥanīfa's father", "Sâbit — erkek ismi («sağlam»); burada Ebû Hanîfe'nin babası"),
 "bishr": ("Bishr — a man's name; here Bishr ibn al-Walīd al-Kindī (d. 238 AH), Abū Yūsuf's student", "Bişr — erkek ismi; burada Ebû Yûsuf'un talebesi Bişr b. Velîd el-Kindî (ö. 238)"),
 "qasim": ("al-Qāsim — a man's name", "Kâsım — erkek ismi"),
 "umar": ("ʿUmar — a diptote name; here ʿUmar ibn Ḥammād, Abū Ḥanīfa's grandson", "Ömer — gayr-i munsarif isim; burada Ebû Hanîfe'nin torunu Ömer b. Hammâd"),
 "muhammad": ("Muḥammad — a man's name", "Muhammed — erkek ismi"),
 "malik-name": ("Mālik — a man's name; here the father of Anas ibn Mālik", "Mâlik — erkek ismi; burada Enes b. Mâlik'in babası"),
 "mansur-caliph": ("al-Manṣūr — Abū Jaʿfar ʿAbd Allāh al-Manṣūr (d. 158 AH), the second ʿAbbāsid caliph and the founder of Baghdad", "Mansûr — Ebû Ca'fer Abdullah el-Mansûr (ö. 158), ikinci Abbâsî halifesi ve Bağdat'ın kurucusu"),
 "qada": ("judging; the office of judge, the judgeship; (elsewhere) a decree", "hüküm verme; kadılık görevi; (başka yerde) hüküm, kazâ"),
 "mawla": ("mawlā — a client (a freedman and his descendants, tied to a tribe by walāʾ); also a master, a protecting lord", "mevlâ — velâ bağıyla bir kabileye bağlı kimse (âzatlı ve onun soyu); ayrıca efendi, koruyucu"),
 "maruf": ("known, well known (ism mafʿūl of عَرَفَ); also a kindness, the known good", "bilinen, tanınmış (arafe'nin ism-i mef'ûlü); ayrıca iyilik, ma'rûf"),
 "harf": ("a letter; a particle; a single word", "harf; edat; tek bir kelime"),
 "thiqa": ("trust, confidence (masdar of وَثِقَ); as a description: trustworthy — in ḥadīth, the upright and accurate transmitter", "güven (vesika'nın masdarı); vasıf olarak: güvenilir — hadiste adâlet ve zabt sahibi râvî"),
 "bas": ("harm; hardship, violent distress — لَا بَأْسَ بِهِ: «there is no harm in him»", "zarar; sıkıntı, şiddet — لَا بَأْسَ بِهِ: «onda bir beis yok»"),
 "mamluk": ("owned; a slave (ism mafʿūl of مَلَكَ); الْمَمَالِيك, the Mamluks", "sahip olunan; köle (meleke'nin ism-i mef'ûlü); الْمَمَالِيك, Memlükler"),
 "waliya": ("to take charge of; to hold (an office)", "bir işi üstlenmek; (bir görevi) yürütmek"),
 "fiqh": ("understanding; fiqh — the science of the rulings of the Law, jurisprudence", "anlayış; fıkıh — şer'î hükümler ilmi"),
 "mashhad": ("a shrine, a place of visitation over a grave; a scene (noun of place from شَهِدَ)", "meşhed, kabir üzerindeki ziyaretgâh; sahne (şehide'den ism-i mekân)"),
 "rajul": ("a man", "adam, erkek"),
 "wajh": ("face; way, manner; (in ḥadīth) a path of transmission", "yüz; yol, tarz; (hadiste) rivayet yolu"),
 "sahaba": ("the Companions of the Prophet ﷺ (a collective)", "sahâbe — Hz. Peygamber'in ﷺ ashâbı (topluluk ismi)"),
 "dar": ("a house, an abode; a large house with its courtyard", "ev, yurt; avlulu büyük ev"),
 "hafiza": ("to memorise, to keep by heart; to guard, to preserve", "ezberlemek, hıfzetmek; korumak"),
 "haddatha": ("to narrate (ḥadīth), to relate; to talk to (Form II)", "(hadis) rivayet etmek, nakletmek; konuşmak (tef'îl bâbı)"),
 "arada": ("to will, to want; أَرَادَهُ عَلَى الْأَمْرِ: to press someone to a thing (Form IV)", "istemek, dilemek; أَرَادَهُ عَلَى الْأَمْرِ: birini bir işe zorlamak (if'âl bâbı)"),
 "ahya": ("to bring to life; أَحْيَا اللَّيْلَ: to spend the night awake in worship (Form IV)", "diriltmek; أَحْيَا اللَّيْلَ: geceyi ibadetle geçirmek (if'âl bâbı)"),
 "afrada": ("to set apart; to give (a subject) a book of its own (Form IV)", "ayırmak; (bir konuya) müstakil bir kitap ayırmak (if'âl bâbı)"),
 "shaykh": ("an old man; an elder, a teacher (shaykh)", "yaşlı adam; şeyh, hoca"),
 "radiya": ("to be pleased with (رَضِيَ عَنْهُ: with a person; رَضِيَ بِهِ: with a thing)", "razı olmak (رَضِيَ عَنْهُ: bir kimseden; رَضِيَ بِهِ: bir şeye)"),
 "asl": ("root, origin; original state", "asıl, köken; ilk hâl"),
 "talaba": ("to seek; to ask for, to send for (someone)", "aramak, talep etmek; (birini) çağırtmak"),
}
LEMMA_HERE = {"hadha": "هٰذَا"}   # the text's spelling (the shelf holds both هَذَا and هٰذَا under this key)
_STAGED = {}
for d in (OUT_ROOT.iterdir() if OUT_ROOT.exists() else []):
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
for k, e in NEW_GLOSS.items():
    hit = [p for p in PKGS if k in _G[p]]
    assert not hit, ("a key is a global claim — taken", k, hit)
    for p, g in _STAGED.items():
        if k in g: assert _lemma_id(g[k]) == _lemma_id(e), ("staged clash", k, p, g[k].get("lemma"))

used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, ORIGIN, missing = {}, {}, []
for k in sorted(used):
    if k in NEW_GLOSS: GLOSS[k] = NEW_GLOSS[k]; continue
    e, p = find_entry(k)
    if e is None: missing.append(k)
    else:
        GLOSS[k], ORIGIN[k] = json.loads(json.dumps(e)), p
        if k in GLOSS_HERE: GLOSS[k]["gloss"] = {"en": GLOSS_HERE[k][0], "tr": GLOSS_HERE[k][1]}
        if k in LEMMA_HERE:
            assert _lemma_id(GLOSS[k]) == _lemma_id({"lemma": LEMMA_HERE[k]}), k
            GLOSS[k]["lemma"] = LEMMA_HERE[k]
assert not missing, missing
assert not [k for k in GLOSS_HERE if k not in GLOSS], [k for k in GLOSS_HERE if k not in GLOSS]
MORPH = {"verbs": {}}
MORPH["verbs"]["ittahama"] = _sg.derived(_sg.B8 + " — مِثَالٌ", _sg.W8, "َ", "اِتَّهَم", "تَّهِم", "اِتَّهِم", "اِتِّهَام", "مُتَّهِم", "مُتَّهَم", "اُتُّهِمَ", "يُتَّهَمُ",
                                         note="أَصْلُهُ اِوْتَهَمَ: قُلِبَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ.")
for k, e in GLOSS.items():
    if e.get("pos") != "verb" or k in MORPH["verbs"]: continue
    if k in ORIGIN and k in _M[ORIGIN[k]]: MORPH["verbs"][k] = _M[ORIGIN[k]][k]
    else:
        for p in PKGS:
            if k in _M[p] and _lemma_id(_G[p].get(k, {})) == _lemma_id(e): MORPH["verbs"][k] = _M[p][k]; break
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "مِنْ سِيرَةِ أَبِي حَنِيفَةَ", "en": "From the Life of Abū Ḥanīfa", "tr": "Ebû Hanîfe'nin Hayatından"},
 "subtitle": {"ar": "أَخْبَارٌ مُخْتَارَةٌ مِنْ تَرْجَمَةِ الْإِمَامِ أَبِي حَنِيفَةَ النُّعْمَانِ بْنِ ثَابِتٍ فِي «سِيَرِ أَعْلَامِ النُّبَلَاءِ» لِلذَّهَبِيِّ — نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Selected reports from al-Dhahabī's entry on Imam Abū Ḥanīfa al-Nuʿmān ibn Thābit in Siyar Aʿlām al-Nubalāʾ — the received text, word for word",
              "tr": "Zehebî'nin Siyeru A'lâmi'n-Nübelâ'sındaki İmam Ebû Hanîfe Nu'mân b. Sâbit maddesinden seçilmiş haberler — metin lafzıyla aktarılmıştır"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "نَصٌّ مَنْقُولٌ بِلَفْظِهِ مِنْ تَرْجَمَةِ الْإِمَامِ أَبِي حَنِيفَةَ النُّعْمَانِ بْنِ ثَابِتٍ (رَقْم ١٦٣) فِي «سِيَرِ أَعْلَامِ النُّبَلَاءِ» لِشَمْسِ الدِّينِ الذَّهَبِيِّ (ت ٧٤٨ هـ)، طَبْعَةِ مُؤَسَّسَةِ الرِّسَالَةِ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ١٠٩٠٦)، الْجُزْءِ السَّادِسِ، ص ٣٩٠–٤٠٣. كُلُّ فَصْلٍ قِطْعَةٌ مُتَّصِلَةٌ وَاحِدَةٌ لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ: (١) ص ٣٩٠–٣٩١ مِنْ أَوَّلِ التَّرْجَمَةِ إِلَى «وَلَمْ يَصِحَّ»؛ (٢) ص ٣٩٤؛ (٣) ص ٣٩٥؛ (٤) ص ٣٩٩؛ (٥) ص ٤٠١؛ (٦) ص ٤٠٣. وَتُرِكَ مَا بَيْنَ الْقِطَعِ: سَرْدُ شُيُوخِهِ وَتَلَامِيذِهِ وَكَلِمَةُ الذَّهَبِيِّ فِي طَلَبِهِ الْآثَارَ وَفِقْهِهِ (ص ٣٩٢)، وَبَاقِي الْأَقْوَالِ فِي أَصْلِهِ، وَحِكَايَةُ اخْتِيَارِهِ الْعُلُومَ — وَقَدْ حَكَمَ الذَّهَبِيُّ بِوَضْعِهَا — وَخَبَرَا صُحْبَتِهِ لِحَمَّادِ بْنِ أَبِي سُلَيْمَانَ، وَرُؤْيَاهُ وَتَعْبِيرُ ابْنِ سِيرِينَ لَهَا، وَسَائِرُ أَخْبَارِ عِبَادَتِهِ (وَمِنْهَا خَبَرُ صَلَاتِهِ الْعِشَاءَ وَالصُّبْحَ بِوُضُوءٍ وَاحِدٍ أَرْبَعِينَ سَنَةً، تُرِكَ لِأَنَّ ضَبْطَ «بِوُضُوءِ» فِي الطَّبْعَةِ مَوْضِعُ نَظَرٍ) وَصِفَتِهِ وَأَخْلَاقِهِ، وَأَقْوَالُهُ فِي الْقِيَاسِ وَالرِّوَايَةِ، وَبَاقِي ثَنَاءِ الْأَئِمَّةِ عَلَيْهِ، وَبَقِيَّةُ أَخْبَارِهِ مَعَ الْمَنْصُورِ وَالسِّجْنِ؛ وَتَرْجَمَةُ ابْنِهِ حَمَّادٍ بَعْدَهَا. الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ كَمَا هُوَ وَوُحِّدَ رَسْمُهُ عَلَى رَسْمِ الْمَكْتَبَةِ (لَا سُكُونَ عَلَى حَرْفِ الْمَدِّ، وَالْفَتْحَةُ قَبْلَ الْأَلِفِ، وَتَنْوِينُ النَّصْبِ قَبْلَ أَلِفِهِ، وَسُكُونُ لَامِ «الْ» الْقَمَرِيَّةِ وَبَاءِ «بْن»، وَالشَّدَّةُ عَلَى اللَّامِ فِي «إِلَّا»، وَالْأَلِفُ الْخَنْجَرِيَّةُ فِي «هٰذَا» وَ«الرَّحْمٰنِ»)؛ وَمَا تَرَكَتْهُ الطَّبْعَةُ بِلَا شَكْلٍ ضَبَطْنَاهُ نَحْنُ، وَهُوَ: سُكُونُ بَعْضِ الْحُرُوفِ (الْفُرْسِ، يَثْبُتْ، حَرْفٌ، رَهْطِ، فَأُعْتِقَ، أَصْلُهُ، أَمْشِي، اللَّيْلَ، يَحْلِفُ، تَحْلِفُ، أَمْرٌ، تُفْرَدَ)، وَحَرَكَةُ هَاءِ الضَّمِيرِ وَمِيمِ الْجَمْعِ (دُكَّانُهُ، يَحْفَظُهُ، ضَرَبَهُ، فَأَرَادَهُ، يَمِينِهِ، دَقَائِقِهِ، سِيرَتُهُ، مِنْهُمْ، أَفْضَلُهُمْ، لَهُمْ)، وَكَسْرَةُ اللَّامِ فِي «وُلِدَ»، وَاللَّامِ فِي «لِآخَرَ»، وَالْمِيمِ فِي «مِائَةٍ»، وَكَسْرَةُ «بْنِ» فِي «بْنِ مُحْرِزٍ». وَلَمْ تُغَيَّرْ كَلِمَةٌ وَلَمْ تُزَدْ وَلَمْ تُحْذَفْ وَلَمْ تُصَحَّحْ، وَلَمْ يُصَحَّحْ شَيْءٌ مِنَ النَّصِّ عَلَى نُسْخَةٍ أُخْرَى؛ وَأُبْقِيَ «الْمُقْرِي» كَمَا طُبِعَ (وَأَصْلُهُ الْمُقْرِئُ). عَلَامَاتُ التَّرْقِيمِ لِلْمُحَقِّقِ، وَلَمْ نُثْبِتْ نُقْطَتَيْهِ بَعْدَ «وُلِدَ» وَ«رَأَى» وَ«رَوَى» وَ«عَنْ» وَبَعْدَ «أَبُو حَنِيفَةَ» وَ«زُوطَى» وَ«تُوُفِّيَ» وَ«الزُّهْرِيُّ» وَ«الْمَرْوَزِيُّ»، وَجُعِلَتِ الشَّرْطَةُ «—»، وَفُصِلَ بَيْنَ شَطْرَيِ الْبَيْتِ بِعَلَامَةٍ. وَلَمْ تُسْتَعْمَلْ حَوَاشِي الْمُحَقِّقِ. وَالْبَيْتُ فِي الْفَصْلِ السَّادِسِ لِلْمُتَنَبِّي، أَوْرَدَهُ الذَّهَبِيُّ غَيْرَ مَنْسُوبٍ. تَقْسِيمُ الْجُمَلِ (وَقَدْ قُسِمَتْ أَرْبَعُ جُمَلٍ طَوِيلَةٍ مِنَ الطَّبْعَةِ عِنْدَ فَاصِلَةٍ أَوْ عِنْدَ «قَالَ:»: الْفَصْلُ ٣ الْجُمْلَتَانِ ٤–٥، وَالْفَصْلُ ٤ الْجُمْلَتَانِ ١–٢ ثُمَّ ٣–٤، وَالْفَصْلُ ٥ الْجُمْلَتَانِ ١–٢؛ وَمَا بَدَأَ مِنْهَا بِحَرْفِ عَطْفٍ أُعْرِبَ عَاطِفًا) وَعَنَاوِينُ الْفُصُولِ وَالتَّرْجَمَةُ وَكُلُّ إِعْرَابٍ اجْتِهَادُ الْمُؤَلِّفِ، بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "The RECEIVED text, verbatim: six passages from the entry on Imam Abū Ḥanīfa al-Nuʿmān ibn Thābit (no. 163) in Siyar Aʿlām al-Nubalāʾ by Shams al-Dīn al-Dhahabī (d. 748 AH), in the Muʾassasat al-Risāla edition as al-Maktaba al-Shāmila carries it (book 10906), vol. 6, pp. 390–403. Each chapter is ONE contiguous span with nothing taken out of its middle: (1) pp. 390–391, from the opening of the entry to «وَلَمْ يَصِحَّ»; (2) p. 394, from al-ʿIjlī's words to the report of Bābil; (3) p. 395, Ibn Maʿīn's four statements; (4) p. 399, from Bishr ibn al-Walīd's report to the cap in the mosque of Kufa; (5) p. 401, Bishr's report of al-Manṣūr; (6) p. 403, from Ibn al-Mubārak's word to «وَاللهُ أَعْلَمُ». LEFT OUT between the spans: the long lists of his teachers and students, with al-Dhahabī's remark on his search for āthār and his standing in fiqh (p. 392); the remaining reports of his origin (al-Anbār, the sons of Persia, the Nayrūz gift); the story of his choosing among the sciences, which al-Dhahabī himself judges fabricated, and the two reports of his years with Ḥammād ibn Abī Sulaymān; his dream and Ibn Sīrīn's reading of it; the other reports of his worship (among them the forty years' prayer with one ablution, left out because the edition's vowelling of «بِوُضُوءِ» there is doubtful), his appearance and character; his own sayings on qiyās and narration; the rest of the imams' praise; the other reports of al-Manṣūr and the prison; and the notice of his son Ḥammād that follows. TWO VOWELLING LAYERS: the edition is vowelled, though not on every letter. Its vowels are kept and only normalised to the shelf's spelling (no sukūn on a madd letter, fatḥa before the alif, tanwīn fatḥ before its alif, sukūn on the lām of the qamarī article and on the bāʾ of «بْن», the shadda of «إِلَّا» on its lām, the dagger alif of «هٰذَا» and «الرَّحْمٰن»). Where the edition leaves a letter bare the vowel is OURS: the sukūn of الْفُرْسِ، يَثْبُتْ، حَرْفٌ، رَهْطِ، فَأُعْتِقَ، أَصْلُهُ، أَمْشِي، اللَّيْلَ، يَحْلِفُ، تَحْلِفُ، أَمْرٌ، تُفْرَدَ; the vowel of the pronoun's hāʾ and the plural mīm in دُكَّانُهُ، يَحْفَظُهُ، ضَرَبَهُ، فَأَرَادَهُ، يَمِينِهِ، دَقَائِقِهِ، سِيرَتُهُ، مِنْهُمْ، أَفْضَلُهُمْ، لَهُمْ; the kasra of the lām in «وُلِدَ», of the lām in «لِآخَرَ», of the mīm in «مِائَةٍ» and of «بْنِ» in «بْنِ مُحْرِزٍ». NO word is changed, added, dropped or corrected, and no reading was emended against another witness; «الْمُقْرِي» is kept as printed (for الْمُقْرِئ). The punctuation is the editor's: his colon after «وُلِدَ», «رَأَى», «رَوَى», «عَنْ», after the topics «أَبُو حَنِيفَةَ» and «زُوطَى», after «تُوُفِّيَ» and before «عَنْ» in two isnāds is not carried over, his hyphens are set as dashes, and the verse's two hemistichs are marked. The verse in chapter 6 is al-Mutanabbī's; al-Dhahabī quotes it without naming him. The edition's footnotes are not used. Sentence division (ch3 s4–s5, ch4 s1–s2, ch4 s3–s4 and ch5 s1–s2 are each ONE period of the edition, cut at a comma or at «قَالَ:»; where the second half opens with a conjunction it is analysed as one), chapter titles, translations and every iʿrāb line are the author's own analysis. reviewStatus: pending-scholarly-review.",
  "tr": "LAFZIYLA AKTARILAN metin: Şemsüddîn ez-Zehebî'nin (ö. 748) «Siyeru A'lâmi'n-Nübelâ» adlı eserindeki İmam Ebû Hanîfe Nu'mân b. Sâbit maddesinden (no. 163) altı pasaj; Müessesetü'r-Risâle baskısı, el-Mektebetü'ş-Şâmile'deki hâliyle (kitap 10906), c. 6, s. 390–403. Her bölüm, ortasından hiçbir şey çıkarılmamış TEK bir kesintisiz parçadır: (1) s. 390–391, maddenin başından «وَلَمْ يَصِحَّ»ya kadar; (2) s. 394, İclî'nin sözünden Bâbil rivayetine kadar; (3) s. 395, İbn Maîn'in dört sözü; (4) s. 399, Bişr b. Velîd'in haberinden Kûfe mescidindeki kalensüveye kadar; (5) s. 401, Bişr'in Mansûr haberi; (6) s. 403, İbnü'l-Mübârek'in sözünden «وَاللهُ أَعْلَمُ»ya kadar. Parçalar arasında BIRAKILANLAR: hocalarının ve talebelerinin uzun listeleri ile Zehebî'nin onun âsâr talebine ve fıkıhtaki yerine dair sözü (s. 392); aslına dair diğer rivayetler (Enbâr, Fâris oğulları, Nevruz hediyesi); Zehebî'nin bizzat uydurma saydığı ilim seçme hikâyesi ve Hammâd b. Ebî Süleyman'la geçen yıllarına dair iki haber; rüyası ve İbn Sîrîn'in tabiri; ibadetine dair diğer haberler (bunlardan kırk yıl tek abdestle namaz haberi, baskıdaki «بِوُضُوءِ» harekesi şüpheli olduğu için alınmamıştır), şemâili ve ahlâkı; kıyas ve rivayete dair kendi sözleri; imamların diğer övgüleri; Mansûr ve hapisle ilgili diğer haberler; ardından gelen oğlu Hammâd'ın tercemesi. İKİ HAREKE KATMANI: baskı harekelidir, fakat her harfte değil. Baskının harekeleri korunmuş, yalnızca kütüphanenin imlâsına göre birleştirilmiştir (med harfinde sükûn yok, fetha eliften önce, nasb tenvini elifinden önce, kamerî «الْ» lâmında ve «بْن» bâ'sında sükûn, «إِلَّا»da şeddenin lâm üzerinde olması, «هٰذَا» ve «الرَّحْمٰن»de hançer elif). Baskının harekesiz bıraktığı harflerin harekesi BİZE aittir: الْفُرْسِ، يَثْبُتْ، حَرْفٌ، رَهْطِ، فَأُعْتِقَ، أَصْلُهُ، أَمْشِي، اللَّيْلَ، يَحْلِفُ، تَحْلِفُ، أَمْرٌ، تُفْرَدَ kelimelerindeki sükûn; دُكَّانُهُ، يَحْفَظُهُ، ضَرَبَهُ، فَأَرَادَهُ، يَمِينِهِ، دَقَائِقِهِ، سِيرَتُهُ، مِنْهُمْ، أَفْضَلُهُمْ، لَهُمْ kelimelerinde zamir hâ'sının ve cemi mîminin harekesi; «وُلِدَ»deki lâmın, «لِآخَرَ»deki lâmın, «مِائَةٍ»deki mîmin ve «بْنِ مُحْرِزٍ»deki «بْنِ»nin kesresi. Hiçbir kelime değiştirilmemiş, eklenmemiş, çıkarılmamış veya düzeltilmemiştir; başka bir nüshaya göre hiçbir okuyuş tashih edilmemiştir; «الْمُقْرِي» basıldığı gibi bırakılmıştır (الْمُقْرِئ yerine). Noktalama muhakkike aittir: «وُلِدَ», «رَأَى», «رَوَى», «عَنْ» kelimelerinden, «أَبُو حَنِيفَةَ» ve «زُوطَى» konularından, «تُوُفِّيَ»den sonraki ve iki isnadda «عَنْ»den önceki iki nokta alınmamış, kısa çizgiler uzun çizgi yapılmış, beytin iki mısraı işaretlenmiştir. 6. bölümdeki beyit Mütenebbî'nindir; Zehebî onu şairini anmadan zikreder. Baskının dipnotları kullanılmamıştır. Cümle taksimi (3. bölüm c. 4–5, 4. bölüm c. 1–2, 4. bölüm c. 3–4 ve 5. bölüm c. 1–2 baskıda birer tek cümledir; virgülde veya «قَالَ:»de bölünmüştür; ikinci yarı atıf harfiyle başlıyorsa öyle tahlil edilmiştir), bölüm başlıkları, çeviriler ve bütün i'râb satırları müellifin kendi tahlilidir; ilmî incelemeyi beklemektedir.",
  "reviewStatus": "pending-scholarly-review",
 },
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), [len(S) for S in CHAPS], "tokens:", sum(len(s["tokens"]) for s in ALL), "max:", max(len(s["tokens"]) for s in ALL),
      "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "new:", sorted(k for k in GLOSS if k in NEW_GLOSS), "->", PKG)
