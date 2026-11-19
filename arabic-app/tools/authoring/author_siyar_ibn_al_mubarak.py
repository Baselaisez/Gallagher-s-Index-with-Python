"""Author content/samples/siyar-ibn-al-mubarak — «مِنْ سِيرَةِ عَبْدِ اللهِ بْنِ الْمُبَارَكِ», a RECEIVED text at Level 5 (Advanced).

RECEIVED TEXT, VERBATIM: four passages of al-Dhahabī's entry on ʿAbd Allāh ibn al-Mubārak (no. 112) in
«سِيَرُ أَعْلَامِ النُّبَلَاءِ» (the Muʾassasat al-Risāla edition as al-Maktaba al-Shāmila carries it, book 10906), vol. 8,
pp. 378–387, set in six chapters. Each chapter is ONE contiguous span — it may stop early, it never skips:

  ch1  8/378–379  the opening of the entry: the heading with his name, his titles, his birth, his first shaykh, his journeys
                  for knowledge, the frontier, trade and the ḥajj — to «إِلَى الْحَجِّ»
  ch2  8/384      Ashʿath ibn Shuʿba's khabar: al-Rashīd at al-Raqqa — «هٰذَا وَاللهِ الْمُلْكُ»
  ch3  8/385      al-Khaṭīb's khabar of the pilgrims' provisions, first half (the isnād — «وَأَطْيَبَ الْحَلْوَى»)
  ch4  8/385–386  the same khabar, second half («ثُمَّ يُخْرِجُهُمْ مِنْ بَغْدَادَ» — «عَلَيْهَا اسْمُهُ»); ch3 + ch4 are adjacent
  ch5  8/386–387  Muḥammad ibn ʿĪsā's khabar of the young man's debt, first half (the isnād — «مَا عَاشَ»)
  ch6  8/387      the same khabar, second half («فَأُخْرِجَ الرَّجُلُ» — «بَعْدَ مَوْتِ عَبْدِ اللهِ»); ch5 + ch6 are adjacent

THE TWO VOWELLING LAYERS. The edition is vowelled, though not on every letter. Its vowels are kept and normalised to the
shelf's spelling (no sukūn on a madd letter, fatḥa before the alif, tanwīn fatḥ before its alif, sukūn on the lām of the
qamarī article, the dagger alif of هٰذَا and الرَّحْمٰن, بْنُ with its sukūn, NFC). Where the edition leaves a letter bare the
vowel is editorial; the script itself computes that list against the saved source (see `_layers()` below) and the manifest
attribution carries it. ONE reading is corrected against a witness (خُوَارِزْميَّةٌ → خُوَارِزْمِيَّةً); the edition's colon
after a topic (مَوْلِدُهُ: / فَأَقْدَمُ شَيْخٍ لَقِيَهُ:) is not carried over, and its hyphens are set as dashes.

The verbatim page text lives in research/sources/siyar-ibn-al-mubarak-src.txt.  Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_siyar_ibn_al_mubarak.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "siyar-ibn-al-mubarak"
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

# ---- this package's own helpers --------------------------------------------------------------------------------------------
def T(full, lex, pos, g, ar, en, tr, punct=None, segs=None): return tok(full, lex, pos, g, ar, en, tr, punct=punct, segments=segs)
FBAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
D_ADL_R = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ فَلَا يُنَوَّنُ", " — a proper name barred from tanwin (a name «turned» from عَامِر)", " — alemiyyet ve adl sebebiyle gayr-i munsarif; tenvin almaz")
D_MARW = ("، عَلَمٌ عَلَى بَلْدَةٍ أَعْجَمِيٌّ مُؤَنَّثٌ، مَمْنُوعٌ مِنَ الصَّرْفِ — وَإِنْ كَانَ ثُلَاثِيًّا سَاكِنَ الْوَسَطِ — لِاجْتِمَاعِ الْعُجْمَةِ مَعَ الْعَلَمِيَّةِ وَالتَّأْنِيثِ؛ هٰكَذَا ضَبَطَتْهُ الطَّبْعَةُ",
          " — a town's name, foreign and feminine: barred from tanwin, though it has three letters with a quiescent middle, because foreignness joins the name and the feminine; the fatha stands for the kasra — so the edition vowels it",
          " — yabancı ve müennes şehir adı; ortası sâkin üç harfli olsa da ucme, alemiyyet ve te'nîs birleştiği için gayr-i munsarif, kesre yerine fetha ile — baskı böyle harekelemiştir")
NISBA = lambda ar, en, tr: (" — اسْمٌ مَنْسُوبٌ إِلَى " + ar, " — a nisba to " + en, " — " + tr + " nisbet")
SALIM_Y = "بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ"
MULHAQ_Y = "بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"
UQUD = ["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"]
def HADDATHANA(n=Z, punct=None): return ENC_MADI("حَدَّثَنَا", "haddatha", "نَا", ["form-ii-verbs"], punct=punct, **N3(cat(FBAAD, n)))
def HADDATHANI(n=Z): return WIQAYA_V("حَدَّثَنِي", "haddatha", "حَدَّثَ", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "past verb built on fatha", "fetha üzere mebnî mâzî", extra=["form-ii-verbs"], hidden=None, **N3(cat(FBAAD, n)))
def AKHBARANA(n=Z): return ENC_MADI("أَخْبَرَنَا", "akhbara", "نَا", ["form-iv-verbs"], **N3(cat(FBAAD, n)))
SAMITU = lambda n=Z: MADI_T("سَمِعْتُ", "samia", who="ana", **N3(n))
MAQUL = ("، وَالْجُمْلَةُ بَعْدَهُ مَقُولُ الْقَوْلِ", "; the clause after it is what is said", "; sonraki cümle mekûlü'l-kavldir")
def PN(full, lex, head_ar, head_en, head_tr, g, n=Z, punct=None):
    """a proper name in a seat the kit's noun helpers cannot give it (they write pos «noun»)"""
    return tok(full, lex, "propn", g, head_ar + n[0] + ".", head_en + n[1] + ".", head_tr + n[2] + ".", punct=punct)
def FAQALA(full, who_ar=None, punct=":", fem=False):
    """فَقَالَ / قَالَ with its hidden doer"""
    return (QALAT if fem else QALA)(full, hidden=True, punct=punct)
def YAQULU(full, lex="qala", n=Z, punct=":", who="هُوَ"):
    return MUDARI(full, lex, ["hollow-verbs", "maful-bihi"], punct=punct, who=who, **N3(cat(("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; söylenen söz mef'ûlün bihtir"), n)))
def LAHU3(full, pron, pron_tr, punct=None, note=Z):
    """لَهُ / لَهُمْ — the kit's LAHU2 with the segments cut after the lām's fatḥa (the kit leaves the fatḥa on the pronoun)"""
    t = LAHU2(full, pron, pron_tr, punct=punct, note=note)
    t["segments"] = [seg("لَ", "li", "prep"), seg(full[2:], pron, "pron")]
    return t
def LAHUM(n=Z, punct=None): return LAHU3("لَهُمْ", "pron-3mp", " («onlar için»)", punct=punct, note=n)
def ALAYHIM2(n=Z, punct=None): return JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onlara»)", punct=punct, **N3(n))
ZAMAN = ("زَمَانٍ", "time", "Zaman")
def TMZ(full, lex, n, punct=None):
    """the tamyīz of a number (the kit's TAMYIZ speaks of a comparison)"""
    return tok(full, lex, "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ" + n[0] + ".", "A specifier (tamyiz), in nasb" + n[1] + ".", "Temyîz, mansûb" + n[2] + ".", punct=punct)
TMZ_UQUD = (" — تَمْيِيزُ الْعَدَدِ: وَمَا يُعَدُّ بِالْعُقُودِ (مِنْ عِشْرِينَ إِلَى تِسْعِينَ) مُفْرَدٌ مَنْصُوبٌ", " — it names what is counted: after the tens (twenty to ninety) the thing counted stands in the singular, in nasb", " — sayılanı belirtir: ukûd (yirmiden doksana) sayılarından sonra temyiz müfred ve mansûb gelir")
def QH(full, who=None, punct=":"):
    """قَالَ / فَقَالَ with a hidden doer; who = (ar, en, tr) names the speaker"""
    t = QALA(full, hidden=True, punct=punct)
    if who:
        for k, x in zip(("ar", "en", "tr"), (" — وَالْقَائِلُ " + who[0], " — the speaker is " + who[1], " — konuşan: " + who[2])): t["irab"][k] = t["irab"][k][:-1] + x + "."
    return t
FATA = ("الْفَتَى", "the young man", "genç")
def ADD(t, n):
    """append a note triple to a finished token's three iʿrāb lines (before the full stop)"""
    for k, x in zip(("ar", "en", "tr"), n): t["irab"][k] = t["irab"][k][:-1] + x + "."
    return t
# the en/tr half of a case SIGN the kit's helpers state in Arabic only (their `sign=` reaches the Arabic line alone)
S_SALIM = ("", " by the ya (a sound masculine plural)", " (yâ ile: cem-i müzekker sâlim)")
S_MULHAQ = ("", " by the ya (it declines like the sound masculine plural)", " (yâ ile: cem-i müzekker sâlime mülhak)")
S_DUAL = ("", " by the ya (a dual)", " (yâ ile: tesniye)")
S_K_ALIF = ("", " by a kasra estimated on the alif", " (elif üzerinde takdîrî kesre ile)")
S_D_YA = ("", " by a damma estimated on the ya", " (yâ üzerinde takdîrî damme ile)")
def IT(t):
    """the kit's hidden «he» where the pronoun is a thing, not a person"""
    assert "«he»" in t["irab"]["en"]; t["irab"]["en"] = t["irab"]["en"].replace("«he»", "«it»"); return t
D_FIL = ("، عَلَمٌ عَلَى وَزْنِ الْفِعْلِ مَمْنُوعٌ مِنَ الصَّرْفِ", " — a proper name on the pattern of a verb, barred from tanwin: the fatha stands for the kasra", " — fiil vezninde alem, gayr-i munsarif; kesre yerine fetha ile")
def FA_IDHA(): return tok("فَإِذَا", "idha", "noun", ["huruf-al-shart-fil-kafiya", "maful-fih", "idha-shartiyya"],
    FA_AR + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ، خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ، مَبْنِيٌّ عَلَى السُّكُونِ.",
    "The fa conjoins; إِذَا «when»: the adverb of time that governs its condition and is governed by its answer; built on sukun.",
    "«bunun üzerine» + izâ «-dığı zaman»: zaman zarfı, şartına muzâf ve cevabıyla mansûb; sükûn üzere mebnî.", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "noun")])
IDHA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا", "; the clause fills the seat of jarr, annexed to إِذَا", "; cümle izâ'ya muzâfun ileyh olarak mahallen mecrûr")
IDHA_JAWAB = (" — وَالْجُمْلَةُ جَوَابُ إِذَا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of إِذَا and has no seat of its own", "; cümle izâ'nın cevabıdır, i'râbdan mahalli yoktur")
def FA_LA(): return tok("فَلَا", "la-nafiya", "part", ["la-nafiya"], FA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; لَا negates and governs nothing.", "«bunun üzerine» + nefiy lâ'sı; amel etmez.", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")])
def YAZALU(): return tok("يَزَالُ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"],
    "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَ«لَا يَزَالُ» يُفِيدُ الِاسْتِمْرَارَ: يَبْقَى يَفْعَلُ.",
    "A defective present verb, one of كَانَ's sisters, in raf' by the damma; its noun is the hidden pronoun «he» — «لَا يَزَالُ» means «he keeps on».",
    "Kâne'nin kardeşlerinden nâkıs muzâri, damme ile merfû; ismi gizli zamir «o» — «lâ yezâlü» devamlılık bildirir: «yapmaya devam eder».")
KH_YAZAL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «لَا يَزَالُ»", "; the clause fills the seat of nasb as the predicate of «لَا يَزَالُ»", "; cümle «lâ yezâlü»nün haberi olarak mahallen mansûb")
HIKAYA = (" — وَالْمُضَارِعُ لِحِكَايَةِ الْحَالِ الْمَاضِيَةِ: عَادَةٌ كَانَتْ تَتَكَرَّرُ", " — the present tense relates a past habit as though it were before the eye", " — muzâri, geçmişteki bir âdeti gözler önündeymiş gibi anlatır (hikâye-i hâl)")
def MA_ISTIFHAM(seat_ar, seat_en, seat_tr, extra=None):
    return tok("مَا", "ma-istifham", "pron", ["al-istifham"] + (extra or []), "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ " + seat_ar + ".", "The interrogative noun «what?», built on sukun, " + seat_en + ".", "İstifhâm ismi «ne?», sükûn üzere mebnî, " + seat_tr + ".")
def KADHA(n=Z, punct=None):
    return tok("كَذَا", "kadha", "part", ["al-kinayat-wal-zuruf-al-mabniyya", "maful-bihi", "hadhf-wa-taqdir"],
        "كِنَايَةٌ عَنْ شَيْءٍ مُبْهَمٍ مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ، أَيْ: أَمَرُونِي أَنْ أَشْتَرِيَ كَذَا — وَأَصْلُهَا كَافُ التَّشْبِيهِ وَ«ذَا» الْإِشَارِيَّةُ ثُمَّ صَارَتَا كَلِمَةً وَاحِدَةً" + n[0] + ".",
        "«Such-and-such» — a word that stands for a thing left unnamed, built on sukun, in the seat of nasb as the object of a verb left unsaid: «they told me to buy such-and-such»; it began as the kāf of likeness with the demonstrative ذَا, and the two became one word" + n[1] + ".",
        "«Şunu» — belirsiz bir şeyden kinâye, sükûn üzere mebnî; hazfedilmiş fiilin mef'ûlün bihi olarak mahallen mansûb: «şunu almamı söylediler»; aslı teşbih kâfı ile işaret ismi «zâ»dır, sonra tek kelime olmuştur" + n[2] + ".", punct=punct)
def WA_KADHA(punct=None):
    return tok("وَكَذَا", "kadha", "part", ["al-kinayat-wal-zuruf-al-mabniyya", "atf-nasaq"],
        WA_AR + "كَذَا مَعْطُوفَةٌ عَلَى الْأُولَى فِي مَحَلِّ نَصْبٍ — وَالتَّكْرَارُ لِلدَّلَالَةِ عَلَى تَعَدُّدِ الْأَشْيَاءِ.",
        "The waw conjoins; «and such-and-such» is conjoined to the first, in the seat of nasb — the word is repeated to show that the things are several.",
        "«ve» + «şunu», ilkine ma'tûf, mahallen mansûb — tekrar, şeylerin birden fazla olduğunu gösterir.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("كَذَا", "kadha", "part")])
def RAQQA(case, punct=None, n=Z):
    full = {"nasb": "الرَّقَّةَ", "jarr": "الرَّقَّةِ"}[case]
    h = {"nasb": ("مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", ["maful-bihi"]), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "In jarr after the letter", "Cer harfiyle mecrûr", ["huruf-jarr"])}[case]
    return PN(full, "raqqa-city", h[0], h[1], h[2], h[3], n, punct)
def NAFAQAT(enc, punct=None):
    full = "نَفَقَاتِ" + enc
    return tok(full, "nafaqa", "noun", ["maful-bihi", "jam-muannath-salim", "idafa-definiteness", "al-bariz-al-muttasil"],
        "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — النَّفَقَةُ: مَا يُعِدُّهُ الْمُسَافِرُ مِنَ الْمَالِ لِيُنْفِقَهُ فِي سَفَرِهِ.",
        "The direct object, in nasb by the kasra that stands for the fatha — a sound feminine plural; annexed, and the attached pronoun is the second term of the idafa, in the seat of jarr. A نَفَقَة is the money a traveller sets aside to spend on his journey.",
        "Mef'ûlün bih; cem-i müennes sâlim olduğu için fetha yerine kesre ile mansûb; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr. Nafaka: yolcunun yolda harcamak üzere hazırladığı para.", punct=punct,
        segments=[seg("نَفَقَاتِ", "nafaqa", "noun"), seg(enc, PRON[enc], "pron")])

TITLES = [{"ar": "شَيْخُ الْإِسْلَامِ ابْنُ الْمُبَارَكِ", "en": "The Shaykh al-Islām, Ibn al-Mubārak", "tr": "Şeyhülislâm İbnü'l-Mübârek"},
          {"ar": "هٰذَا وَاللهِ الْمُلْكُ", "en": "This, by God, Is Kingship", "tr": "Vallahi Asıl Saltanat Budur"},
          {"ar": "نَفَقَاتُ الْحُجَّاجِ", "en": "The Pilgrims' Provisions", "tr": "Hacıların Harçlıkları"},
          {"ar": "الصُّرَّةُ عَلَيْهَا اسْمُهُ", "en": "The Purse with His Name on It", "tr": "Üzerinde Adı Yazılı Kese"},
          {"ar": "الشَّابُّ الْمَحْبُوسُ", "en": "The Young Man in Prison", "tr": "Hapisteki Genç"},
          {"ar": "جَاءَ رَجُلٌ فَقَضَى دَيْنِي", "en": "A Man Came and Paid My Debt", "tr": "Bir Adam Geldi, Borcumu Ödedi"}]

IBN_MUB = ("ابْنُ الْمُبَارَكِ", "Ibn al-Mubārak", "İbnü'l-Mübârek")
def MUBARAK(punct=None, n=Z): return MI("الْمُبَارَكِ", "mubarak-name", n, "propn", punct=punct)
def IBN(case, role, n=Z):
    """ابْنُ الْمُبَارَكِ at the head of a name: role = fail | ismk | maful | majr | mi"""
    full = {"raf": "ابْنُ", "nasb": "ابْنَ", "jarr": "ابْنِ"}[case]
    h = {"fail": ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "The doer (fa'il), in raf'", "Fâil, merfû", ["fail"]),
         "ismk": ("اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ", "The noun of كَانَ, in raf'", "Kâne'nin ismi, merfû", ["kana-wa-akhawatuha"]),
         "mi": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", ["idafa-definiteness"])}[role]
    return tok(full, "ibn", "noun", h[3] + ["idafa-definiteness"], h[0] + "، مُضَافٌ — وَثَبَتَتْ أَلِفُهُ لِأَنَّهُ لَمْ يَقَعْ بَيْنَ عَلَمَيْنِ" + n[0] + ".",
               h[1] + ", annexed — it keeps its alif, for it does not stand between two names" + n[1] + ".", h[2] + ", muzâf — iki alem arasında olmadığı için elifi yazılır" + n[2] + ".")

# ================================================ Chapter 1 — شَيْخُ الْإِسْلَامِ ابْنُ الْمُبَارَكِ (8/378–379) ================================================
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "ʿAbd Allāh ibn al-Mubārak ibn Wāḍiḥ al-Ḥanẓalī. [The letter ʿayn after the name is the biographers' sign that the authors of all Six Books narrate from him.]",
  "tr": "Abdullah b. Mübârek b. Vâzıh el-Hanzalî. [İsimden sonraki «ع» harfi, Kütüb-i Sitte müelliflerinin hepsinin ondan rivayet ettiğini gösteren remizdir.]"},
 "tokens": [
  tok("عَبْدُ", "abd", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
    "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هٰذَا، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَهُوَ عُنْوَانُ التَّرْجَمَةِ: اسْمُ صَاحِبِهَا.",
    "The predicate (khabar) of a dropped mubtada — «this is» — in raf' by the damma, annexed: the heading of the entry, the name of its subject.",
    "Hazfedilmiş mübtedânın («bu») haberi, damme ile merfû, muzâf — terceme (biyografi) maddesinin başlığı: sahibinin adı."),
  ALLAH_MI(),
  BN("raf", "عَبْدُ اللهِ", "ʿAbd Allāh", "Abdullah"),
  MUBARAK(n=(" — عَلَمٌ مَنْقُولٌ مِنِ اسْمِ الْمَفْعُولِ مِنْ «بَارَكَ»", " — a name taken over from the passive participle of بَارَكَ, «blessed»", " — «bâreke» fiilinin ism-i mef'ûlünden nakledilmiş alem")),
  BN("jarr", "الْمُبَارَكِ", "al-Mubārak", "Mübârek"),
  MI("وَاضِحٍ", "wadih-name", pos="propn"),
  NA("الْحَنْظَلِيُّ", "hanzali", "raf", ("عَبْدُ اللهِ", "ʿAbd Allāh", "Abdullah"), NISBA("بَنِي حَنْظَلَةَ مِنْ تَمِيمٍ", "the Banū Ḥanẓala of Tamīm", "Temîm'den Hanzala oğullarına"), extra=["ism-mansub"], punct=" (ع)")]})

S1.append({"id": "s2", "translation": {
  "en": "The Imam, the Shaykh al-Islām, the scholar of his age and the commander of the God-fearing in his time,",
  "tr": "İmam, Şeyhülislâm, zamanının âlimi ve vaktinde takvâ sahiplerinin emîri;"},
 "tokens": [
  tok("الْإِمَامُ", "imam", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"],
    "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ، مَرْفُوعٌ بِالضَّمَّةِ — هٰكَذَا تُفْتَتَحُ التَّرَاجِمُ بِأَوْصَافِ صَاحِبِهَا.",
    "The predicate (khabar) of a dropped mubtada — «he is» — in raf' by the damma: this is how a biographical entry opens, with the titles of its subject.",
    "Hazfedilmiş mübtedânın («o») haberi, damme ile merfû — terceme (biyografi) maddeleri sahibinin vasıflarıyla böyle açılır.", punct="،"),
  tok("شَيْخُ", "shaykh", "noun", ["mubtada-khabar", "idafa-definiteness"],
    "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A second predicate (khabar), in raf', annexed.", "İkinci haber, merfû, muzâf."),
  MI("الْإِسْلَامِ", "islam", punct="،"),
  tok("عَالِمُ", "alim-scholar", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-fail"],
    "خَبَرٌ ثَالِثٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A third predicate (khabar), in raf', annexed.", "Üçüncü haber, merfû, muzâf."),
  ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf", punct="،"),
  ATF("وَأَمِيرُ", "amir", case="raf", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَالْمَعْطُوفُ عَلَيْهِ «عَالِمُ»", note_en="; conjoined to «the scholar», and annexed", note_tr="; «âlim»e ma'tûf, muzâf"),
  MI("الْأَتْقِيَاءِ", "taqi", (" — جَمْعُ تَقِيٍّ عَلَى أَفْعِلَاءَ", " — the broken plural of تَقِيّ, on أَفْعِلَاء", " — takî'nin ef'ilâ' vezninde cem-i teksîri"), extra=["jam-taksir"]),
  FIP(JM("مُتَعَلِّقٌ بِـ«أَمِيرُ»", "attaches to «the commander»", "«emîr»e müteallik")),
  ENC_NOUN("وَقْتِهِ", "waqt", "هِ", "majr", punct="،")]})

S1.append({"id": "s3", "translation": {
  "en": "Abū ʿAbd al-Raḥmān, the Ḥanẓalī by clientage, the Turk, then the man of Marw; the ḥāfiẓ, the frontier-fighter, one of the great landmarks — and his mother was a woman of Khwārazm.",
  "tr": "Ebû Abdurrahman; velâ yoluyla Hanzalî, (aslen) Türk, sonra Mervli; hâfız, gâzi, önde gelen büyük şahsiyetlerden biri — annesi de Hârizmli idi."},
 "tokens": [
  AB("أَبُو", "badal_raf", (" — وَهُوَ كُنْيَتُهُ", " — it is his kunya", " — bu onun künyesidir")),
  MI("عَبْدِ", "abd", MUDAF, extra=["idafa-definiteness"]),
  MI("الرَّحْمٰنِ", "rahman", (" — مِنْ أَسْمَاءِ اللهِ الْحُسْنَى", " — one of the Names of God", " — Allah'ın güzel isimlerinden"), "propn"),
  NA("الْحَنْظَلِيُّ", "hanzali", "raf", ("أَبُو عَبْدِ الرَّحْمٰنِ", "Abū ʿAbd al-Raḥmān", "Ebû Abdurrahman"), extra=["ism-mansub"]),
  tok("مَوْلَاهُمْ", "mawla", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "ism-maqsur-manqus", "idafa-definiteness", "al-bariz-al-muttasil"],
    "بَدَلٌ مِنَ «الْحَنْظَلِيُّ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى بَنِي حَنْظَلَةَ الْمَفْهُومِينَ مِنَ النِّسْبَةِ — وَيَجُوزُ أَنْ يَكُونَ خَبَرًا لِمُبْتَدَأٍ مَحْذُوفٍ، أَيْ: هُوَ مَوْلَاهُمْ؛ وَالْمَعْنَى أَنَّ نِسْبَتَهُ إِلَيْهِمْ نِسْبَةُ وَلَاءٍ لَا نِسْبَةُ نَسَبٍ.",
    "A badal of «the Ḥanẓalī», in raf' by a damma estimated on the alif; annexed, and the attached «them» — the Banū Ḥanẓala, understood from the nisba — is the second term of the idafa, in the seat of jarr. It may also be read as the predicate of a dropped «he is»: «their client». The formula says that he is theirs by the tie of walāʾ, not by descent.",
    "«Hanzalî»den bedel, elif üzerinde takdîrî damme ile merfû; muzâf, bitişik «onlar» zamiri (nisbetten anlaşılan Hanzala oğulları) muzâfun ileyh, mahallen mecrûr. Hazfedilmiş «o» mübtedâsının haberi de olabilir: «onların mevlâsı». Bu kalıp, nisbetin nesep değil velâ yoluyla olduğunu bildirir.", punct="،",
    segments=[seg("مَوْلَا", "mawla", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  NA("التُّرْكِيُّ", "turki", "raf", None, (" — مَنْسُوبٌ إِلَى التُّرْكِ: كَانَ أَبُوهُ تُرْكِيًّا", " — a nisba to the Turks: his father was a Turk", " — Türklere nisbet: babası Türk idi"), extra=["ism-mansub"], punct="،", nth="2"),
  THUMMA(),
  ATF("الْمَرْوَزِيُّ", "marwazi", pos="propn", case="raf", extra=["ism-mansub"], punct="،",
      note_ar=" عَلَى «التُّرْكِيُّ»: تُرْكِيُّ الْأَصْلِ ثُمَّ مِنْ أَهْلِ مَرْوَ؛ وَالنِّسْبَةُ إِلَى مَرْوَ «مَرْوَزِيٌّ» بِزِيَادَةِ الزَّايِ عَلَى غَيْرِ قِيَاسٍ",
      note_en=" — conjoined to «the Turk»: a Turk by origin, then a man of Marw; the nisba to Marw is مَرْوَزِيّ, with an added zāy against the rule",
      note_tr=" — «Türk»e ma'tûf: aslen Türk, sonra Mervli; Merv'e nisbet kıyasa aykırı olarak zây ilavesiyle «Mervezî»dir"),
  NA("الْحَافِظُ", "hafiz", "raf", None, (" — اسْمُ فَاعِلٍ مِنْ حَفِظَ؛ وَالْحَافِظُ عِنْدَ الْمُحَدِّثِينَ: مَنِ اتَّسَعَ حِفْظُهُ لِلْحَدِيثِ وَرِجَالِهِ", " — the active participle of حَفِظَ; among the ḥadīth scholars a ḥāfiẓ is a master who holds a vast store of ḥadīth and its transmitters by heart", " — hafıza'nın ism-i fâili; muhaddislerde hâfız: hadisleri ve râvîlerini geniş ölçüde ezberinde tutan âlim"), extra=["ism-fail"], punct="،", nth="3"),
  NA("الْغَازِي", "ghazi", "raf", None, cat(S_D_YA, (" — اسْمُ فَاعِلٍ مَنْقُوصٌ مِنْ غَزَا", " — a manqūṣ active participle of غَزَا: the one who goes out to fight on the frontier", " — gazâ'nın menkûs ism-i fâili: sınırda cihada çıkan")), extra=["ism-fail", "ism-maqsur-manqus"], punct="،", sign="مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ"),
  tok("أَحَدُ", "ahad", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "idafa-definiteness"],
    "بَدَلٌ مِنْ «أَبُو عَبْدِ الرَّحْمٰنِ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A badal of «Abū ʿAbd al-Raḥmān», in raf' by the damma, annexed.", "«Ebû Abdurrahman»dan bedel, damme ile merfû, muzâf."),
  MI("الْأَعْلَامِ", "alam-banner", (" — جَمْعُ عَلَمٍ، وَهُوَ الْجَبَلُ وَالرَّايَةُ، ثُمَّ اسْتُعِيرَ لِلرَّجُلِ الْمَشْهُورِ الَّذِي يُهْتَدَى بِهِ", " — the plural of عَلَم «a mountain, a banner», then used of the famous man by whom others find their way", " — alem'in cem'i: dağ, sancak; sonra kendisiyle yol bulunan meşhur kimse için istiâre edilmiştir"), extra=["jam-taksir", "istiara"], punct="،"),
  KANA("وَكَانَتْ", fem=True),
  ENC_NOUN("أُمُّهُ", "umm", "هُ", "ismk"),
  KK("خُوَارِزْمِيَّةً", "khwarizmi-nisba", (" — مَنْسُوبَةٌ إِلَى خُوَارِزْمَ؛ وَوَقَعَ فِي الطَّبْعَةِ هُنَا بِالرَّفْعِ «خُوَارِزْمِيَّةٌ» فَصُحِّحَ عَلَى مَا فِيهَا نَفْسِهَا (٨/٣٨١) وَفِي «الْبِدَايَةِ وَالنِّهَايَةِ»", " — a nisba to Khwārazm; the edition prints a damma here («خُوَارِزْمِيَّةٌ»), corrected by its own text at 8/381 and by al-Bidāya wa-l-Nihāya", " — Hârizm'e nisbet; baskıda burada ref ile «خُوَارِزْمِيَّةٌ» basılmış, aynı baskının 8/381'deki metnine ve «el-Bidâye ve'n-Nihâye»ye göre düzeltilmiştir"), extra=["ism-mansub"], punct=".")]})

S1.append({"id": "s4", "translation": {"en": "His birth was in the year one hundred and eighteen.", "tr": "Doğumu yüz on sekiz yılındadır."},
 "tokens": [
  ENC_NOUN("مَوْلِدُهُ", "mawlid", "هُ", "mubtada", note_ar=" — مَصْدَرٌ مِيمِيٌّ مِنْ وُلِدَ بِمَعْنَى الْوِلَادَةِ", note_en=" — a mīmī masdar of وُلِدَ: «his birth»", note_tr=" — vülide'nin mîmî masdarı: «doğumu»"),
  FIP(JM_KHABAR),
  J("سَنَةِ", "sana", MUDAF, extra=["idafa-definiteness"]),
  tok("ثَمَانِ", "thamani", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"],
    "الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمُرَكَّبِ «ثَمَانِيَ عَشْرَةَ»، وَالْعَدَدُ الْمُرَكَّبُ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَحُذِفَتْ يَاؤُهُ هُنَا وَبَقِيَتِ الْكَسْرَةُ دَلِيلًا عَلَيْهَا، وَهِيَ لُغَةٌ فِيهِ؛ هٰكَذَا ضَبَطَتْهُ الطَّبْعَةُ.",
    "The first part of the compound number «eighteen»; the compound is built on the fatha of both parts, in the seat of jarr as the second term of the idafa — here its yāʾ is dropped and the kasra is left to point to it, one of the transmitted forms of the word; so the edition vowels it.",
    "«On sekiz» mürekkeb sayısının ilk cüzü; mürekkeb sayı iki cüzünün fethası üzere mebnîdir, muzâfun ileyh olarak mahallen mecrûr — burada yâ'sı hazfedilmiş, kesre ona delil olarak kalmıştır; bu da kelimede nakledilen bir lügattir; baskı böyle harekelemiştir."),
  tok("عَشْرَةَ", "ashara", "noun", ["asma-al-adad-fil-kafiya", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"],
    "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ — أُنِّثَ مُوَافَقَةً لِلْمَعْدُودِ الْمُؤَنَّثِ (سَنَة)، وَذُكِّرَ الْجُزْءُ الْأَوَّلُ عَلَى خِلَافِهِ.",
    "The second part of the compound number, built on fatha — it is feminine in agreement with the counted noun (سَنَة), while the first part goes against it in the masculine.",
    "Mürekkeb sayının ikinci cüzü, fetha üzere mebnî — ma'dûd (سَنَة) müennes olduğu için ona uyarak müennes gelmiş, ilk cüz ise ona aykırı olarak müzekker gelmiştir."),
  ATF("وَمِائَةٍ", "mia", case="jarr", extra=["asma-al-adad-fil-kafiya"], punct=".", note_ar=" عَلَى مَحَلِّ الْعَدَدِ الْمُرَكَّبِ؛ وَأَلِفُهَا تُكْتَبُ وَلَا تُنْطَقُ؛ أَيْ سَنَةَ ١١٨ مِنَ الْهِجْرَةِ", note_en=" — conjoined to the seat of the compound number; its alif is written, not spoken; that is, year 118 of the Hijra", note_tr=" — mürekkeb sayının mahalline ma'tûf; elifi yazılır, okunmaz; yani hicretin 118. yılı")]})

S1.append({"id": "s5", "translation": {"en": "He set out to seek knowledge when he was twenty years old.", "tr": "Yirmi yaşındayken ilim talebine başladı."},
 "tokens": [
  MADI("فَطَلَبَ", "talaba", hidden=True),
  O("الْعِلْمَ", "ilm"),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"),
  KB("ابْنُ", "ibn", cat(MUDAF, (" — «ابْنُ كَذَا سَنَةً» كِنَايَةٌ عَنِ السِّنِّ", " — «the son of so many years» is the idiom for age", " — «şu kadar senenin oğlu» yaş bildiren deyimdir")), ["idafa-definiteness"]),
  MI("عِشْرِينَ", "ishrun", S_MULHAQ, extra=UQUD, sign=MULHAQ_Y),
  TMZ("سَنَةً", "sana", TMZ_UQUD, punct=".")]})

S1.append({"id": "s6", "translation": {
  "en": "The earliest shaykh he met was al-Rabīʿ ibn Anas al-Khurāsānī: he found a way to get in to him in the prison, and heard from him some forty ḥadīths;",
  "tr": "Görüştüğü en eski hoca Rebî' b. Enes el-Horasânî'dir: bir çaresini bulup hapishanede yanına girmiş ve ondan kırk kadar hadis dinlemiştir;"},
 "tokens": [
  FA("فَأَقْدَمُ", "aqdam", "noun", ["mubtada-khabar", "ism-tafdil", "idafa-definiteness"],
     "أَقْدَمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ مُضَافٌ إِلَى نَكِرَةٍ.", "«the earliest» is the mubtada, in raf', annexed — an elative annexed to an indefinite noun.", "«en eski» mübtedâ, merfû, muzâf — nekreye muzâf ism-i tafdîl."),
  MI("شَيْخٍ", "shaykh"),
  ENC_MADI("لَقِيَهُ", "laqiya", "هُ", hidden=True, **N3(NAAT_OF("jarr", "شَيْخٍ", "a shaykh", "şeyh"))),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"],
    "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ ثَانٍ — وَجُمْلَةُ «هُوَ الرَّبِيعُ» فِي مَحَلِّ رَفْعٍ خَبَرُ «أَقْدَمُ»؛ وَلَيْسَ ضَمِيرَ فَصْلٍ عِنْدَ الْجُمْهُورِ، لِأَنَّ مَا قَبْلَهُ نَكِرَةٌ.",
    "A detached pronoun built on fatha, in the seat of raf' as a second mubtada — the clause «he is al-Rabīʿ» is the predicate of «the earliest», in the seat of raf'; on the majority view it is not a pronoun of separation, because the word before it is indefinite.",
    "Munfasıl zamir, fetha üzere mebnî, ikinci mübtedâ olarak mahallen merfû — «o, Rebî'dir» cümlesi «en eski»nin haberi, mahallen merfû; cumhura göre fasıl zamiri değildir, çünkü öncesi nekredir."),
  PN("الرَّبِيعُ", "rabi-name", "خَبَرُ «هُوَ» مَرْفُوعٌ بِالضَّمَّةِ", "The predicate of «he», in raf' by the damma", "«o»nun haberi, damme ile merfû", ["mubtada-khabar"]),
  BN("raf", "الرَّبِيعُ", "al-Rabīʿ", "Rebî'"),
  MI("أَنَسٍ", "anas", pos="propn"),
  NA("الْخُرَاسَانِيُّ", "khurasani", "raf", ("الرَّبِيعُ", "al-Rabīʿ", "Rebî'"), NISBA("خُرَاسَانَ", "Khurāsān", "Horasan'a"), extra=["ism-mansub"], punct="،"),
  MADI("تَحَيَّلَ", "tahayyala", ["form-v-verbs"], hidden=True, note_ar=" يَعُودُ عَلَى ابْنِ الْمُبَارَكِ — وَالْجُمْلَةُ اسْتِئْنَافِيَّةٌ؛ تَحَيَّلَ: طَلَبَ الْحِيلَةَ وَتَلَطَّفَ حَتَّى وَصَلَ", note_en=" — Ibn al-Mubārak; the clause opens a new statement. تَحَيَّلَ: «he used a stratagem, he contrived a way»", note_tr=" — İbnü'l-Mübârek; cümle isti'nâfiyyedir. تَحَيَّلَ: «çare aradı, bir yolunu buldu»"),
  MADI("وَدَخَلَ", "dakhala", hidden=True),
  ILAYHI(),
  ILAP(JM("بَدَلٌ مِنَ الْجَارِّ وَالْمَجْرُورِ قَبْلَهُ بِإِعَادَةِ الْجَارِّ: دَخَلَ إِلَيْهِ، أَيْ: إِلَى السِّجْنِ الَّذِي هُوَ فِيهِ", "is a badal of the jarr phrase before it, with the letter repeated: «he went in to him», that is, into the prison where he was", "öncesindeki câr-mecrûrdan, cer harfi tekrar edilerek bedeldir: «yanına girdi», yani bulunduğu hapishaneye")),
  J("السِّجْنِ", "sijn", punct="،"),
  MADI("فَسَمِعَ", "samia", hidden=True),
  MINHU(),
  O("نَحْوًا", "nahw", (" — أَيْ: قَدْرًا قَرِيبًا مِنْ أَرْبَعِينَ", " — «about», that is, an amount close to forty", " — «kadar», yani kırka yakın bir miktar")),
  MINP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِـ«نَحْوًا»", "hangs on an omitted word that qualifies «about»", "«nahven» için mahzûf bir na'te müteallik")),
  J("أَرْبَعِينَ", "arbaun", S_MULHAQ, extra=UQUD, sign=MULHAQ_Y),
  TMZ("حَدِيثًا", "hadith", TMZ_UQUD, punct="،")]})

S1.append({"id": "s7", "translation": {
  "en": "then he set out on his travels in the year one hundred and forty-one, and took knowledge from the last of the Successors,",
  "tr": "sonra yüz kırk bir yılında yolculuğa çıktı ve tâbiîlerden hayatta kalanlardan ilim aldı;"},
 "tokens": [
  THUMMA(),
  MADI("ارْتَحَلَ", "irtahala", ["form-viii-verbs"], hidden=True),
  FIP(),
  J("سَنَةِ", "sana", MUDAF, extra=["idafa-definiteness"]),
  MI("إِحْدَى", "ihda", cat(S_K_ALIF, (" — مُؤَنَّثُ «أَحَد» فِي الْعَدَدِ الْمَعْطُوفِ", " — the feminine of أَحَد in the conjoined number", " — ma'tûf sayıda «ehad»in müennesi")), extra=["ism-maqsur-manqus", "asma-al-adad-fil-kafiya"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"),
  ATF("وَأَرْبَعِينَ", "arbaun", case="jarr", extra=UQUD, sign="مَجْرُورٌ " + MULHAQ_Y, note_en=" — in jarr by the ya (it declines like the sound masculine plural)", note_tr=" — yâ ile mecrûr (cem-i müzekker sâlime mülhak)"),
  ATF("وَمِائَةٍ", "mia", case="jarr", extra=["asma-al-adad-fil-kafiya"], punct="،", note_ar=" — أَيْ سَنَةَ ١٤١ مِنَ الْهِجْرَةِ", note_en=" — that is, year 141 of the Hijra", note_tr=" — yani hicretin 141. yılı"),
  MADI("وَأَخَذَ", "akhadha", hidden=True, note_ar=" — وَالْمَفْعُولُ مَحْذُوفٌ، أَيْ: أَخَذَ الْعِلْمَ", note_en="; its object is left unsaid: «he took knowledge»", note_tr="; mef'ûlü hazfedilmiştir: «ilim aldı»"),
  AN_PREP(),
  J("بَقَايَا", "baqiyya", cat(S_K_ALIF, MUDAF, (" — جَمْعُ بَقِيَّةٍ: مَنْ بَقِيَ مِنْهُمْ حَيًّا", " — the plural of بَقِيَّة: those of them who were still alive", " — bakiyye'nin cem'i: onlardan hayatta kalanlar")), extra=["jam-taksir", "idafa-definiteness", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"),
  MI("التَّابِعِينَ", "tabi", cat(S_SALIM, (" — جَمْعُ تَابِعٍ، وَهُمْ مَنْ لَقُوا الصَّحَابَةَ", " — the plural of تَابِع: the Successors, those who met the Companions", " — tâbi'in cem'i: sahâbeye yetişenler, tâbiîn")), extra=["jam-mudhakkar-salim", "ism-fail"], sign=SALIM_Y, punct="،")]})

S1.append({"id": "s8", "translation": {
  "en": "and he travelled and roamed a great deal — and so on until he died — in seeking knowledge, on campaign, in trade, in spending on his brothers in God and in fitting them out to go with him to the ḥajj.",
  "tr": "çokça sefere çıkıp diyar diyar dolaştı — ve ölünceye kadar da böyle devam etti —: ilim talebi için, gazâ için, ticaret için, Allah için kardeş edindiklerine infak etmek ve onları kendisiyle birlikte hacca gitmek üzere donatmak için."},
 "tokens": [
  MADI("وَأَكْثَرَ", "akthara", ["form-iv-verbs"], hidden=True),
  MINA(),
  J("التَّرْحَالِ", "tarhal", (" — مَصْدَرٌ عَلَى «تَفْعَالٍ» يَدُلُّ عَلَى الْكَثْرَةِ: كَثْرَةُ الِارْتِحَالِ", " — a masdar on تَفْعَال, the pattern of doing a thing much: constant journeying", " — çokluk bildiren «tef'âl» vezninde masdar: çokça yolculuk"), extra=["masdar"]),
  ATF("وَالتَّطْوَافِ", "tatwaf", case="jarr", extra=["masdar"], punct="،", note_ar=" — مَصْدَرٌ عَلَى «تَفْعَالٍ» مِنْ طَافَ: كَثْرَةُ الطَّوَافِ فِي الْبِلَادِ", note_en=" — a masdar on تَفْعَال from طَافَ: much roaming through the lands", note_tr=" — tâfe'den «tef'âl» vezninde masdar: beldeleri çokça dolaşma"),
  PREP("وَإِلَى", "ila", gloss_tr="«-e kadar»",
       role_ar=" لِانْتِهَاءِ الْغَايَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ دَلَّ عَلَيْهِ مَا قَبْلَهُ، أَيْ: وَدَامَ عَلَى ذٰلِكَ إِلَى أَنْ مَاتَ، فَالْوَاوُ عَطَفَتْ جُمْلَةً عَلَى جُمْلَةٍ؛ وَيَجُوزُ أَنْ يَكُونَ مَعْطُوفًا عَلَى ظَرْفٍ مُقَدَّرٍ يَدُلُّ عَلَيْهِ السِّيَاقُ، أَيْ: أَكْثَرَ مِنْ ذٰلِكَ حِينَئِذٍ وَإِلَى أَنْ مَاتَ",
       role_en=" of the end-point — the jarr phrase hangs on a verb left unsaid that the words before it point to: «and he kept to that until he died», so the waw joins a sentence to a sentence; it may also be read as conjoined to a time left unsaid that the context supplies: «he did so then, and until he died»",
       role_tr=" (gâye bildirir) — câr-mecrûr, öncesinin delâlet ettiği mahzûf bir fiile mütealliktir: «ve ölünceye kadar buna devam etti»; böylece vâv cümleyi cümleye atfeder; siyâkın gösterdiği mukadder bir zarfa ma'tûf da olabilir: «o zaman ve ölünceye kadar böyle yaptı»"),
  AN(" — وَلَا يَعْمَلُ فِي الْمَاضِي لَفْظًا؛ وَالْمَصْدَرُ الْمُؤَوَّلُ (أَيْ: مَوْتِهِ) فِي مَحَلِّ جَرٍّ بِإِلَى", "; before a past verb it changes nothing in the word; the clause it builds («his death») is in the seat of jarr after إِلَى", "; mâzîde lafzen amel etmez; kurduğu müevvel masdar («ölümü») ilâ ile mahallen mecrûr"),
  MADI("مَاتَ", "mata-die", ["hollow-verbs"], hidden=True),
  FIP(JM("مُتَعَلِّقٌ بِـ«التَّرْحَالِ وَالتَّطْوَافِ»", "attaches to «journeying and roaming»", "«yolculuk ve dolaşma»ya müteallik")),
  J("طَلَبِ", "talab", MUDAF, extra=["idafa-definiteness", "masdar"]),
  MI("الْعِلْمِ", "ilm", (" — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ", " — the masdar annexed to its object", " — masdarın mef'ûlüne izâfeti"), punct="،"),
  PREP("وَفِي", "fi", gloss_tr="«-de»"),
  J("الْغَزْوِ", "ghazw", (" — مَصْدَرُ غَزَا: الْخُرُوجُ لِقِتَالِ الْعَدُوِّ", " — the masdar of غَزَا: going out to fight the enemy", " — gazâ'nın masdarı: düşmanla savaşmaya çıkma"), extra=["masdar"], punct="،"),
  PREP("وَفِي", "fi", gloss_tr="«-de»"),
  J("التِّجَارَةِ", "tijara", punct="،"),
  ATF("وَالْإِنْفَاقِ", "infaq", case="jarr", extra=["masdar"], note_ar=" عَلَى «التِّجَارَةِ» — مَصْدَرُ أَنْفَقَ", note_en=" — conjoined to «trade»; the masdar of أَنْفَقَ", note_tr=" — «ticaret»e ma'tûf; enfeka'nın masdarı"),
  ALAP(JM("مُتَعَلِّقٌ بِـ«الْإِنْفَاقِ»", "attaches to «spending»", "«infak»a müteallik")),
  J("الْإِخْوَانِ", "akh", (" — جَمْعُ أَخٍ", " — a broken plural of أَخ", " — ah'ın cem-i teksîri"), extra=["jam-taksir"]),
  FIP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْإِخْوَانِ»: الْإِخْوَانُ فِي اللهِ مَنْ جَمَعَتْهُمُ الْمَحَبَّةُ لِأَجْلِهِ", "hangs on an omitted hal of «the brothers»: brothers «in God» are those whom love for His sake has joined", "«kardeşler»den mahzûf bir hâle müteallik: «Allah için kardeşler», O'nun rızası için birbirini sevenlerdir")),
  ALLAH_J(punct="،"),
  tok("وَتَجْهِيزِهِمْ", "tajhiz", "noun", ["atf-nasaq", "masdar", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "تَجْهِيزِ مَعْطُوفٌ عَلَى «الْإِنْفَاقِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ.",
    "The waw conjoins; «fitting out» is conjoined to «spending», in jarr and annexed; the attached «them» is the second term of the idafa, in the seat of jarr — the masdar annexed to its object.",
    "«ve» + «donatma», «infak»a ma'tûf, mecrûr, muzâf; bitişik «onlar» zamiri muzâfun ileyh, mahallen mecrûr — masdarın mef'ûlüne izâfeti.",
    segments=[seg("وَ", "wa", "conj"), seg("تَجْهِيزِ", "tajhiz", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  MAA_ENC(),
  ILAP(JM("مُتَعَلِّقٌ بِـ«تَجْهِيزِ»", "attaches to «fitting out»", "«donatma»ya müteallik")),
  J("الْحَجِّ", "hajj", punct=".")]})

# ================================================ Chapter 2 — هٰذَا وَاللهِ الْمُلْكُ (8/384) ================================================
FAIL_PN = ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "The doer (fa'il), in raf'", "Fâil, merfû")
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "ʿUmar ibn Mudrik [said]: al-Qāsim ibn ʿAbd al-Raḥmān narrated to us: Ashʿath ibn Shuʿba al-Maṣṣīṣī narrated to us; he said:",
  "tr": "Ömer b. Müdrik [dedi ki]: Bize Kâsım b. Abdurrahman anlattı; (dedi ki:) bize Eş'as b. Şu'be el-Massîsî anlattı; dedi ki:"},
 "tokens": [
  PN("عُمَرُ", "umar", "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: قَالَ، مَرْفُوعٌ بِالضَّمَّةِ", "The doer of a verb left unsaid — «said» — in raf'", "Hazfedilmiş «dedi» fiilinin fâili, merfû", ["fail", "hadhf-wa-taqdir"] + DG,
     cat(D_ADL_R, (" — هٰكَذَا يَخْتَصِرُ الذَّهَبِيُّ: يَذْكُرُ الرَّاوِيَ ثُمَّ يَسُوقُ قَوْلَهُ", " — this is al-Dhahabī's shorthand: he names the transmitter and goes straight to his words", " — Zehebî'nin ihtisar tarzı: râvîyi anar, sonra doğrudan sözünü nakleder"))),
  BN("raf", "عُمَرُ", "ʿUmar", "Ömer"),
  MI("مُدْرِكٍ", "mudrik-name", pos="propn", punct=":"),
  HADDATHANA(MAQUL_CL),
  PN("الْقَاسِمُ", "qasim", *FAIL_PN, ["fail"]),
  BN("raf", "الْقَاسِمُ", "al-Qāsim", "Kâsım"),
  MI("عَبْدِ", "abd", MUDAF, extra=["idafa-definiteness"]),
  MI("الرَّحْمٰنِ", "rahman", pos="propn", punct="،"),
  HADDATHANA((" — وَالْقَائِلُ الْقَاسِمُ، بِحَذْفِ «قَالَ» اخْتِصَارًا", " — it is al-Qāsim who speaks; «he said» is dropped for brevity, as isnāds do", " — konuşan Kâsım'dır; isnadlarda âdet olduğu üzere «dedi» ihtisaren hazfedilmiştir")),
  PN("أَشْعَثُ", "ashath", *FAIL_PN, ["fail"] + DG, D_FIL_R),
  BN("raf", "أَشْعَثُ", "Ashʿath", "Eş'as"),
  MI("شُعْبَةَ", "shuba", D_TA, "propn", DG, sign=FATHA_JARR),
  NA("الْمَصِّيصِيُّ", "missisi", "raf", ("أَشْعَثُ", "Ashʿath", "Eş'as"), NISBA("الْمَصِّيصَةِ، ثَغْرٍ مِنْ ثُغُورِ الشَّامِ", "al-Maṣṣīṣa, a frontier town of Syria", "Şam sınır şehirlerinden Massîsa'ya"), extra=["ism-mansub"], punct="،"),
  QH("قَالَ", ("أَشْعَثُ", "Ashʿath", "Eş'as"))]})

S2.append({"id": "s2", "translation": {
  "en": "Al-Rashīd came to al-Raqqa, and the people went streaming after Ibn al-Mubārak; sandals were torn apart and the dust rose,",
  "tr": "Reşîd Rakka'ya geldi; halk İbnü'l-Mübârek'in peşinden akın etti, (izdihamdan) pabuçlar koptu, toz kalktı;"},
 "tokens": [
  MADI("قَدِمَ", "qadima", **N3(cat(FBAAD, MAQUL_CL))),
  F("الرَّشِيدُ", "rashid", (" — لَقَبُ الْخَلِيفَةِ هَارُونَ", " — the title of the caliph Hārūn", " — Halife Hârûn'un lakabı")),
  RAQQA("nasb", punct="،", n=(" — قَدِمَ يَتَعَدَّى إِلَى الْمَكَانِ بِنَفْسِهِ", " — قَدِمَ takes the place it comes to as its direct object", " — «kadime» fiili varılan yeri doğrudan mef'ûl alır")),
  MADI("فَانْجَفَلَ", "injafala", ["form-vii-verbs"], **N3(cat(FBAAD, (" — انْجَفَلَ الْقَوْمُ: أَسْرَعُوا مُنْدَفِعِينَ بِجَمَاعَتِهِمْ", " — اِنْجَفَلَ of a crowd: to break away and rush off in a body", " — «incefele»: topluluğun hep birden hızla akın etmesi")))),
  F("النَّاسُ", "nas"),
  ZARF("خَلْفَ", "khalf"),
  IBN("jarr", "mi"),
  MUBARAK(punct="،"),
  MADI("وَتَقَطَّعَتِ", "taqattaa", ["form-v-verbs"], fem=True, kasra=True, **N3(FBAAD)),
  F("النِّعَالُ", "nal", (" — جَمْعُ نَعْلٍ؛ أَيْ: مِنْ شِدَّةِ الزِّحَامِ", " — the plural of نَعْل; that is, from the press of the crowd", " — na'l'in cem'i; yani izdihamın şiddetinden"), extra=["jam-taksir"], punct="،"),
  MADI("وَارْتَفَعَتِ", "irtafaa", ["form-viii-verbs"], fem=True, kasra=True, **N3(FBAAD)),
  F("الْغَبَرَةُ", "ghabara", (" — الْغَبَرَةُ: الْغُبَارُ", " — الْغَبَرَة is dust", " — «ğabera»: toz"), punct="،")]})

S2.append({"id": "s3", "translation": {
  "en": "so a concubine of the Commander of the Faithful, the mother of a child of his, looked down from a tower of the Palace of Wood and said: “What is this?”",
  "tr": "bunun üzerine Emîrü'l-mü'minîn'in bir ümmüveledi Ahşap Köşk'ün bir burcundan baktı ve «Bu da ne?» dedi."},
 "tokens": [
  MADI("فَأَشْرَفَتْ", "ashrafa", ["form-iv-verbs"], fem=True, **N3(cat(FBAAD, (" — أَشْرَفَ: أَطَلَّ مِنْ مَكَانٍ عَالٍ", " — أَشْرَفَ: to look out from a high place", " — «eşrafe»: yüksek bir yerden bakmak")))),
  F("أُمُّ", "umm", cat(MUDAF, (" — أُمُّ الْوَلَدِ: الْجَارِيَةُ الَّتِي وَلَدَتْ لِسَيِّدِهَا", " — an أُمّ وَلَد is a slave woman who has borne her master a child", " — ümmüveled: efendisinden çocuk doğurmuş câriye")), extra=["idafa-definiteness"]),
  MI("وَلَدٍ", "walad"),
  LI_AL("لِأَمِيرِ", "amir", "أَمِيرِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِـ«أُمُّ وَلَدٍ»", note_en=", annexed; the jarr phrase hangs on an omitted word that qualifies «a mother of a child»", note_tr=", muzâf; câr-mecrûr «ümmüveled» için mahzûf bir na'te müteallik"),
  MI("الْمُؤْمِنِينَ", "mumin", S_SALIM, extra=["jam-mudhakkar-salim", "ism-fail"], sign=SALIM_Y),
  MINP(JM("مُتَعَلِّقٌ بِـ«أَشْرَفَتْ»", "attaches to «looked down»", "«baktı»ya müteallik")),
  J("بُرْجٍ", "burj"),
  MINP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِـ«بُرْجٍ»", "hangs on an omitted word that qualifies «a tower»", "«burç» için mahzûf bir na'te müteallik")),
  J("قَصْرِ", "qasr-palace", MUDAF, extra=["idafa-definiteness"]),
  MI("الْخَشَبِ", "khashab", (" — «قَصْرُ الْخَشَبِ»: اسْمُ قَصْرٍ لِلرَّشِيدِ بِالرَّقَّةِ عَلَى مَا يُفْهَمُ مِنَ الْخَبَرِ", " — «the Palace of Wood»: by the report, the name of a palace of al-Rashīd's at al-Raqqa", " — «Ahşap Köşk»: haberden anlaşıldığına göre Reşîd'in Rakka'daki bir köşkünün adı"), punct="،"),
  QALAT("فَقَالَتْ", punct=":"),
  MA_ISTIFHAM("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "in the seat of raf' as the mubtada — the clause is what is said, in the seat of nasb", "mübtedâ olarak mahallen merfû — cümle mekûlü'l-kavl, mahallen mansûb", ["mubtada-khabar"]),
  HADHA("رَفْعٍ خَبَرٌ", "raf' as the khabar", "merfû (haber)", punct="؟")]})

S2.append({"id": "s4", "translation": {"en": "They said: “A scholar of the people of Khurāsān has arrived.”", "tr": "Dediler ki: «Horasan ahalisinden bir âlim geldi.»"},
 "tokens": [
  VERB_WAW("قَالُوا", "qala", ["hollow-verbs", "maful-bihi"], punct=":", note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir"),
  MB("عَالِمٌ", "alim-scholar", (" — وَسَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ وَصْفُهَا بِالْجَارِّ وَالْمَجْرُورِ بَعْدَهَا", " — an indefinite noun may open the sentence here because the jarr phrase after it describes it", " — nekre ile başlamayı, ardından gelen câr-mecrûr ile vasıflanması câiz kılmıştır"), extra=["ism-fail"]),
  MINP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِـ«عَالِمٌ»", "hangs on an omitted word that qualifies «a scholar»", "«âlim» için mahzûf bir na'te müteallik")),
  J("أَهْلِ", "ahl", MUDAF, extra=["idafa-definiteness"]),
  MI("خُرَاسَانَ", "khurasan", D_AJ, "propn", DG, sign=FATHA_JARR),
  MADI("قَدِمَ", "qadima", hidden=True, punct=".", **N3(KH_CL))]})

S2.append({"id": "s5", "translation": {
  "en": "She said: “This, by God, is kingship — not the kingship of Hārūn, who cannot gather the people except with guards and henchmen.”",
  "tr": "Kadın dedi ki: «Vallahi asıl saltanat budur; insanları ancak zaptiyeler ve yardımcılarla toplayabilen Hârûn'un saltanatı değil!»"},
 "tokens": [
  QALAT("قَالَتْ", punct=":"),
  HADHA("رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû (mübtedâ)", punct=" —"),
  tok("وَاللهِ", "wa-qasam", "part", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "huruf-jarr", "jumla-mutarida"],
    "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ — وَجُمْلَةُ الْقَسَمِ مُعْتَرِضَةٌ بَيْنَ الْمُبْتَدَأِ وَخَبَرِهِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The waw of the oath, a jarr letter; the Name of Majesty is sworn by, in jarr by the kasra — the oath is a parenthesis between the mubtada and its khabar, with no seat of its own.",
    "Kasem vâvı, cer harfi; lafza-i celâl kendisine yemin edilen, kesre ile mecrûr — kasem cümlesi mübtedâ ile haberi arasında mu'tarızadır, i'râbdan mahalli yoktur.", punct=" —",
    segments=[seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  KB("الْمُلْكُ", "mulk", (" — وَتَعْرِيفُ الْخَبَرِ بِـ«الْ» يُفِيدُ الْحَصْرَ: هٰذَا هُوَ الْمُلْكُ الْحَقُّ", " — the article on the predicate confines it: this, and nothing else, is true kingship", " — haberin «el» ile marife gelmesi hasr bildirir: gerçek saltanat işte budur"), ["qasr"], punct="،"),
  tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"],
    "لَا النَّافِيَةُ لِلْجِنْسِ عَلَى ضَبْطِ الطَّبْعَةِ (مُلْكَ بِالْفَتْحِ)، تَعْمَلُ عَمَلَ إِنَّ — وَالْأَقْيَسُ أَنْ تَكُونَ عَاطِفَةً تَنْفِي عَمَّا بَعْدَهَا مَا أُثْبِتَ لِمَا قَبْلَهَا، فَيُرْفَعَ مَا بَعْدَهَا (لَا مُلْكُ هَارُونَ) عَطْفًا عَلَى «الْمُلْكُ».",
    "The لَا that denies the kind, by the edition's vowelling (مُلْكَ with fatha); it governs like إِنَّ. The reading the rule itself gives is the conjunction «not», which denies of what follows what was affirmed of what precedes: the next word is then in raf' (لَا مُلْكُ هَارُونَ), conjoined to «kingship».",
    "Baskının harekesine göre (مُلْكَ fetha ile) cinsi nefyeden lâ; inne gibi amel eder. Kıyasa daha uygun olan ise atıf lâ'sı olmasıdır: öncesi için ispat edileni sonrasından nefyeder; o zaman sonrası «el-mülkü»ye ma'tûf olarak merfû okunur (لَا مُلْكُ هَارُونَ)."),
  tok("مُلْكَ", "mulk", "noun", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins", "idafa-definiteness", "hadhf-wa-taqdir"],
    "اسْمُ لَا مَنْصُوبٌ بِالْفَتْحَةِ لِأَنَّهُ مُضَافٌ، وَخَبَرُهَا مَحْذُوفٌ — وَاسْمُ «لَا» هٰذِهِ لَا يَكُونُ إِلَّا نَكِرَةً، وَهُوَ هُنَا مُعَرَّفٌ بِالْإِضَافَةِ إِلَى الْعَلَمِ، فَيُؤَوَّلُ بِالنَّكِرَةِ كَمَا أُوِّلَ قَوْلُهُمْ: «قَضِيَّةٌ وَلَا أَبَا حَسَنٍ لَهَا»؛ وَالْمَعْنَى: لَيْسَ مُلْكُ هَارُونَ بِمُلْكٍ يُعْتَدُّ بِهِ عِنْدَ هٰذَا.",
    "The noun of لَا, in nasb by the fatha because it is annexed; its predicate is left unsaid. The noun of this لَا must be indefinite, and here the idafa to a proper name makes it definite; so it has to be taken as indefinite in sense, the way the grammarians take the saying «قَضِيَّةٌ وَلَا أَبَا حَسَنٍ لَهَا» («a hard case, and no Abū Ḥasan for it»). The sense: beside this, the kingship of Hārūn is no kingship worth the name.",
    "Lâ'nın ismi; muzâf olduğu için fetha ile mansûb, haberi mahzûftur. Bu lâ'nın ismi ancak nekre olur; burada ise aleme izâfetle marifedir; bu yüzden, nahivcilerin «قَضِيَّةٌ وَلَا أَبَا حَسَنٍ لَهَا» sözünü te'vil ettikleri gibi, nekre te'viliyle anlaşılır. Mânâ: bunun yanında Hârûn'un saltanatı saltanat sayılmaz."),
  MI("هَارُونَ", "harun", D_AJ, "propn", DG, sign=FATHA_JARR),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"],
    "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«هَارُونَ».", "A relative pronoun built on sukun, in the seat of jarr as a na't of «Hārūn».", "İsm-i mevsûl, sükûn üzere mebnî, «Hârûn»un na'tı olarak mahallen mecrûr."),
  LA_NAFIYA(),
  MUDARI("يَجْمَعُ", "jamaa-gather", **N3(SILA_T)),
  O("النَّاسَ", "nas"),
  ILLA(),
  BI_NOUN("بِشُرَطٍ", "shurta", "شُرَطٍ", extra=["jam-taksir"], note_ar=" — جَمْعُ شُرْطَةٍ: أَعْوَانُ السُّلْطَانِ الَّذِينَ يَحْفَظُونَ الْأَمْنَ", note_en=" — the plural of شُرْطَة: the ruler's guard, who keep order", note_tr=" — şurta'nın cem'i: asayişi sağlayan sultan görevlileri"),
  ATF("وَأَعْوَانٍ", "awn", case="jarr", extra=["jam-taksir"], punct=".", note_ar=" — جَمْعُ عَوْنٍ: الْمُعِينُ وَالْخَادِمُ", note_en=" — the plural of عَوْن: a helper, a henchman", note_tr=" — avn'in cem'i: yardımcı, hizmetli")]})

# ================================================ Chapter 3 — نَفَقَاتُ الْحُجَّاجِ (8/385) ================================================
ABI_SHAQIQ = ("عَلِيُّ بْنُ الْحَسَنِ بْنِ شَقِيقٍ", "ʿAlī ibn al-Ḥasan ibn Shaqīq", "Ali b. Hasan b. Şakîk")
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "Al-Khaṭīb said: ʿUmar ibn Ibrāhīm and Abū Muḥammad al-Khallāl informed us; they said:",
  "tr": "Hatîb dedi ki: Bize Ömer b. İbrâhîm ile Ebû Muhammed el-Hallâl haber verdi; dediler ki:"},
 "tokens": [
  QALA("قَالَ"),
  F("الْخَطِيبُ", "khatib-preacher", (" — هُوَ أَبُو بَكْرٍ الْخَطِيبُ الْبَغْدَادِيُّ صَاحِبُ «تَارِيخِ بَغْدَادَ»", " — Abū Bakr al-Khaṭīb al-Baghdādī, the author of the History of Baghdad", " — «Târîhu Bağdâd» müellifi Ebû Bekir el-Hatîb el-Bağdâdî"), punct=":"),
  AKHBARANA(MAQUL_CL),
  PN("عُمَرُ", "umar", *FAIL_PN, ["fail"] + DG, D_ADL_R),
  BN("raf", "عُمَرُ", "ʿUmar", "Ömer"),
  MI("إِبْرَاهِيمَ", "ibrahim", D_AJ, "propn", DG, sign=FATHA_JARR, punct="،"),
  W("وَأَبُو", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"],
    "أَبُو مَعْطُوفٌ عَلَى «عُمَرُ» مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abū» is conjoined to «ʿUmar», in raf' by the waw — one of the five nouns; annexed.", "«Ebû», «Ömer»e ma'tûf; esmâ-i hamseden olduğu için vâv ile merfû; muzâf."),
  MI("مُحَمَّدٍ", "muhammad", pos="propn"),
  NA("الْخَلَّالُ", "khallal", "raf", ("أَبُو مُحَمَّدٍ", "Abū Muḥammad", "Ebû Muhammed"), (" — لَقَبٌ عَلَى «فَعَّالٍ» لِلْحِرْفَةِ: بَائِعُ الْخَلِّ", " — a byname on فَعَّال, the pattern of a trade: the vinegar-seller", " — meslek bildiren «fa''âl» vezninde lakap: sirke satıcısı"), "propn", ["sighat-mubalagha"], punct="،"),
  VERB_WAW("قَالُوا", "qala", ["hollow-verbs", "maful-bihi"], punct=":",
    note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ — وَالْوَاوُ لِشُيُوخِ الْخَطِيبِ؛ وَهٰكَذَا وَقَعَ فِي الطَّبْعَتَيْنِ بِلَفْظِ الْجَمْعِ وَالْمَذْكُورُ اثْنَانِ",
    note_en="; what is said is its object — the waw is al-Khaṭīb's shaykhs; both editions have the plural here though two are named",
    note_tr="; söylenen söz mef'ûlün bihtir — vâv, Hatîb'in hocalarına döner; iki kişi anıldığı hâlde her iki baskıda da cemi sîgasıyla gelmiştir")]})

S3.append({"id": "s2", "translation": {
  "en": "Ismāʿīl ibn Muḥammad ibn Ismāʿīl the secretary narrated to us: Aḥmad ibn al-Ḥasan the Qurʾān-teacher narrated to us: I heard ʿAbd Allāh ibn Aḥmad al-Dawraqī,",
  "tr": "Bize kâtip İsmâîl b. Muhammed b. İsmâîl anlattı; (dedi ki:) bize kıraat hocası Ahmed b. Hasan anlattı; (dedi ki:) Abdullah b. Ahmed ed-Devrakî'den işittim;"},
 "tokens": [
  HADDATHANA(MAQUL_CL),
  PN("إِسْمَاعِيلُ", "ismail", *FAIL_PN, ["fail"] + DG, D_AJ_R),
  BN("raf", "إِسْمَاعِيلُ", "Ismāʿīl", "İsmâîl"),
  MI("مُحَمَّدِ", "muhammad", DROP, "propn"),
  BN("jarr", "مُحَمَّدِ", "Muḥammad", "Muhammed"),
  MI("إِسْمَاعِيلَ", "ismail", D_AJ, "propn", DG, sign=FATHA_JARR),
  NA("الْكَاتِبُ", "katib", "raf", ("إِسْمَاعِيلُ", "Ismāʿīl", "İsmâîl"), extra=["ism-fail"], punct="،"),
  HADDATHANA(),
  PN("أَحْمَدُ", "ahmad", *FAIL_PN, ["fail"] + DG, D_FIL_R),
  BN("raf", "أَحْمَدُ", "Aḥmad", "Ahmed"),
  MI("الْحَسَنِ", "hasan-name", pos="propn"),
  NA("الْمُقْرِئُ", "muqri", "raf", ("أَحْمَدُ", "Aḥmad", "Ahmed"), (" — اسْمُ فَاعِلٍ مِنْ أَقْرَأَ: مَنْ يُعَلِّمُ النَّاسَ قِرَاءَةَ الْقُرْآنِ", " — the active participle of أَقْرَأَ: one who teaches the recitation of the Qurʾān", " — akrae'nin ism-i fâili: Kur'ân kıraati öğreten kimse"), extra=["ism-fail"], punct="،"),
  SAMITU((" — وَالْقَائِلُ أَحْمَدُ بْنُ الْحَسَنِ", " — the speaker is Aḥmad ibn al-Ḥasan", " — konuşan: Ahmed b. Hasan")),
  O("عَبْدَ", "abd", MUDAF, extra=["idafa-definiteness"]),
  ALLAH_MI(),
  BN("nasb", "عَبْدَ اللهِ", "ʿAbd Allāh", "Abdullah"),
  MI("أَحْمَدَ", "ahmad", D_FIL, "propn", DG, sign=FATHA_JARR),
  NA("الدَّوْرَقِيَّ", "dawraqi", "nasb", ("عَبْدَ اللهِ", "ʿAbd Allāh", "Abdullah"), (" — اسْمٌ مَنْسُوبٌ", " — a nisba", " — ism-i mensûb"), "propn", ["ism-mansub"], punct="،")]})

S3.append({"id": "s3", "translation": {
  "en": "[who said:] I heard Muḥammad ibn ʿAlī ibn al-Ḥasan ibn Shaqīq [say]: I heard my father; he said:",
  "tr": "(o dedi ki:) Muhammed b. Ali b. Hasan b. Şakîk'ten işittim; (dedi ki:) babamdan işittim; dedi ki:"},
 "tokens": [
  SAMITU((" — وَالْقَائِلُ الدَّوْرَقِيُّ، بِحَذْفِ «يَقُولُ» قَبْلَهُ اخْتِصَارًا", " — the speaker is al-Dawraqī; «saying» is dropped before it for brevity", " — konuşan: Devrakî; öncesindeki «diyordu» ihtisaren hazfedilmiştir")),
  O("مُحَمَّدَ", "muhammad", DROP, "propn"),
  BN("nasb", "مُحَمَّدَ", "Muḥammad", "Muhammed"),
  MI("عَلِيِّ", "ali", DROP, "propn"),
  BN("jarr", "عَلِيِّ", "ʿAlī", "Ali"),
  MI("الْحَسَنِ", "hasan-name", pos="propn"),
  BN("jarr", "الْحَسَنِ", "al-Ḥasan", "Hasan"),
  MI("شَقِيقٍ", "shaqiq-name", pos="propn", punct="،"),
  SAMITU((" — وَالْقَائِلُ مُحَمَّدُ بْنُ عَلِيٍّ", " — the speaker is Muḥammad ibn ʿAlī", " — konuşan: Muhammed b. Ali")),
  YA_MUTAKALLIM_N("أَبِي", "ab", "أَبِ", "مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", extra=["maful-bihi"], punct="،"),
  QH("قَالَ", ABI_SHAQIQ)]})

S3.append({"id": "s4", "translation": {
  "en": "Whenever the season of the ḥajj came, Ibn al-Mubārak's brethren among the people of Marw would gather to him and say: “We will travel in your company.” And he would say: “Hand over your travelling-money.”",
  "tr": "Hac mevsimi geldiğinde, Merv ahalisinden olan kardeşleri İbnü'l-Mübârek'in yanında toplanır ve «Sana yoldaşlık edeceğiz» derlerdi. O da «Harçlıklarınızı getirin» derdi."},
 "tokens": [
  ADD(KANA("كَانَ"), MAQUL_CL),
  IBN("raf", "ismk"),
  MUBARAK(),
  tok("إِذَا", "idha", "noun", ["huruf-al-shart-fil-kafiya", "maful-fih", "idha-shartiyya", "kana-wa-akhawatuha"],
    "ظَرْفٌ لِلزَّمَانِ فِيهِ مَعْنَى الشَّرْطِ، خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ، مَبْنِيٌّ عَلَى السُّكُونِ — وَهُوَ هُنَا لِلْعَادَةِ الْمُتَكَرِّرَةِ فِي الْمَاضِي؛ وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
    "إِذَا «whenever»: an adverb of time with the force of a condition; it governs its condition and is governed by its answer; built on sukun — here of a habit repeated in the past; the whole «whenever … » sentence fills the seat of nasb as the predicate of كَانَ.",
    "İzâ «ne zaman … -se»: şart mânâsı taşıyan zaman zarfı; şartına muzâf, cevabıyla mansûb; sükûn üzere mebnî — burada geçmişte tekrarlanan âdet içindir; şart ve cevap cümlesi kâne'nin haberi olarak mahallen mansûb."),
  tok("كَانَ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs"],
    "فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «حَلَّ وَجَاءَ» مَبْنِيٌّ عَلَى الْفَتْحِ، يَكْتَفِي بِفَاعِلِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا.",
    "A past verb, the COMPLETE كَانَ — «came, set in» — built on fatha; it needs only a doer. The clause fills the seat of jarr, annexed to إِذَا.",
    "Tam fiil olan kâne — «geldi, girdi» —, fetha üzere mebnî mâzî; yalnız fâil alır. Cümle izâ'ya muzâfun ileyh olarak mahallen mecrûr."),
  F("وَقْتُ", "waqt", MUDAF, extra=["idafa-definiteness"]),
  MI("الْحَجِّ", "hajj", punct="،"),
  MADI("اجْتَمَعَ", "ijtamaa", ["form-viii-verbs"], **N3(cat(FBAAD, IDHA_JAWAB))),
  ILAYHI(),
  ENC_NOUN("إِخْوَانُهُ", "akh", "هُ", "fail", extra=["jam-taksir"]),
  MINP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنْ «إِخْوَانُهُ»", "hangs on an omitted hal of «his brethren»", "«kardeşleri»nden mahzûf bir hâle müteallik")),
  J("أَهْلِ", "ahl", MUDAF, extra=["idafa-definiteness"]),
  MI("مَرْوَ", "marw", D_MARW, "propn", DG, sign=FATHA_JARR, punct="،"),
  MUDARI5("فَيَقُولُونَ", "qala", ["hollow-verbs", "maful-bihi", "hikayat-al-hal"], punct=":", **N3(cat(("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; söylenen söz mef'ûlün bihtir"), HIKAYA))),
  MUDARI("نَصْحَبُكَ", "sahiba", who="نَحْنُ", enc="كَ", wujub=True, punct=".", **N3(MAQUL_CL)),
  YAQULU("فَيَقُولُ"),
  tok("هَاتُوا", "hati", "noun", ["imperative-amr", "ism-fil", "al-bariz-al-muttasil", "fail"],
    "فِعْلُ أَمْرٍ جَامِدٌ عَلَى الصَّحِيحِ بِمَعْنَى «أَعْطُوا»، بِدَلِيلِ اتِّصَالِ ضَمَائِرِ الرَّفْعِ بِهِ (هَاتِي، هَاتُوا) — وَعَدَّهُ بَعْضُهُمُ اسْمَ فِعْلِ أَمْرٍ — مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
    "«Give here!» — on the sounder view an imperative verb that has no past or present tense (jāmid), since the subject pronouns attach to it (هَاتِي، هَاتُوا); some count it a verbal noun of command. It is built on the dropped nun before the waw of the group, and that waw is its doer, in the seat of raf'.",
    "«Verin, getirin!» — sahih görüşe göre câmid emir fiili; delili, ref zamirlerinin ona bitişmesidir (هَاتِي، هَاتُوا); kimileri emir ism-i fiili sayar. Cemâat vâvı bitiştiği için nûnun hazfi üzere mebnî; vâv fâildir, mahallen merfû.",
    segments=[seg("هَاتُو", "hati", "noun"), seg("ا", "pron-2mp", "pron")]),
  NAFAQAT("كُمْ", punct=".")]})

S3.append({"id": "s5", "translation": {
  "en": "So he would take their money, put it in a chest and lock it away; then he would hire mounts for them and take them out from Marw to Baghdad,",
  "tr": "Harçlıklarını alır, bir sandığa koyup üzerini kilitler; sonra onlar için binek kiralar ve onları Merv'den Bağdat'a götürürdü;"},
 "tokens": [
  MUDARI("فَيَأْخُذُ", "akhadha"),
  NAFAQAT("هِمْ", punct="،"),
  MUDARI("فَيَجْعَلُهَا", "jaala", enc="هَا"),
  FIP(),
  J("صُنْدُوقٍ", "sunduq", punct="،"),
  MUDARI("وَيُقْفِلُ", "aqfala", ["form-iv-verbs"], note_ar=" — أَقْفَلَ عَلَى الشَّيْءِ: أَغْلَقَ عَلَيْهِ بِالْقُفْلِ", note_en=" — أَقْفَلَ عَلَى: to shut a thing away under lock", note_tr=" — «akfele alâ»: bir şeyin üzerini kilitlemek"),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («üzerine»)", punct="،"),
  THUMMA(),
  MUDARI("يَكْتَرِي", "iktara", ["form-viii-verbs"], naqis="ي", note_ar=" — اكْتَرَى: اسْتَأْجَرَ، أَيْ: يَسْتَأْجِرُ لَهُمُ الدَّوَابَّ لِلرُّكُوبِ وَالْحَمْلِ", note_en=" — اِكْتَرَى: to hire — that is, he hires mounts for them to ride and to carry their loads", note_tr=" — «ikterâ»: kiralamak — yani onlar için binek ve yük hayvanı kiralar"),
  LAHUM(punct="،"),
  MUDARI("وَيُخْرِجُهُمْ", "akhraja", ["form-iv-verbs"], enc="هُمْ"),
  MINP(),
  J("مَرْوَ", "marw", D_MARW, "propn", DG, sign=FATHA_JARR),
  ILAP(),
  J("بَغْدَادَ", "baghdad", D_BALAD, "propn", DG, sign=FATHA_JARR, punct="،")]})

S3.append({"id": "s6", "translation": {
  "en": "and all the while he kept spending on them and feeding them the finest food and the finest sweets,",
  "tr": "bu arada durmadan onlara harcar, en güzel yemekleri ve en güzel tatlıları yedirirdi;"},
 "tokens": [
  FA_LA(),
  YAZALU(),
  MUDARI("يُنْفِقُ", "anfaqa", ["form-iv-verbs", "kana-wa-akhawatuha"], **N3(KH_YAZAL)),
  ALAYHIM2(punct="،"),
  MUDARI("وَيُطْعِمُهُمْ", "atama", ["form-iv-verbs", "mafulayn"], enc="هُمْ", note_ar=" أَوَّلُ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «يُنْفِقُ»", note_en=" — its first object; the clause is conjoined to «spending»", note_tr=" — birinci mef'ûl; cümle «harcar»a ma'tûf"),
  tok("أَطْيَبَ", "atyab", "noun", ["maful-bihi", "mafulayn", "ism-tafdil", "idafa-definiteness"],
    "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ مِنْ «طَيِّبٍ».", "The second object, in nasb by the fatha, annexed — the elative of طَيِّب.", "İkinci mef'ûlün bih, fetha ile mansûb, muzâf — tayyib'in ism-i tafdîli."),
  MI("الطَّعَامِ", "taam", punct="،"),
  ATF("وَأَطْيَبَ", "atyab", case="nasb", extra=["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MI("الْحَلْوَى", "halwa", cat(S_K_ALIF, (" — اسْمٌ مَقْصُورٌ: كُلُّ مَا عُولِجَ مِنَ الطَّعَامِ بِحَلَاوَةٍ", " — a noun ending in alif maqṣūra: anything made sweet", " — maksûr isim: tatlı ile yapılan her yiyecek")), extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", punct="،")]})

# ================================================ Chapter 4 — الصُّرَّةُ عَلَيْهَا اسْمُهُ (8/385–386) ================================================
def YUKHRIJUHUM(): return MUDARI("يُخْرِجُهُمْ", "akhraja", ["form-iv-verbs"], enc="هُمْ")
def MAKKA(kind, punct=None):
    f = MI if kind == "mi" else J
    return f("مَكَّةَ", "makka", D_BALAD, "propn", DG, sign=FATHA_JARR, punct=punct)
def LI_KULL(): return LI_AL("لِكُلِّ", "kull", "كُلِّ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf")
def MA_AMARAKA():
    """مَا أَمَرَكَ عِيَالُكَ أَنْ تَشْتَرِيَ لَهُمْ — the question he puts to each of them"""
    return [
      MA_ISTIFHAM("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ؛ وَلَمْ يُجْعَلْ مَفْعُولًا مُقَدَّمًا لِـ«تَشْتَرِيَ» لِأَنَّ مَعْمُولَ صِلَةِ «أَنْ» لَا يَتَقَدَّمُ عَلَيْهَا", "in the seat of raf' as the mubtada — the clause is what is said, in the seat of nasb; it is not taken as the fronted object of «buy», because nothing governed by the verb after أَنْ may come before أَنْ", "mübtedâ olarak mahallen merfû — cümle mekûlü'l-kavl, mahallen mansûb; «teşteriye»nin öne alınmış mef'ûlü sayılmaz, çünkü «en»in sılasının ma'mûlü «en»in önüne geçemez", ["mubtada-khabar"]),
      ENC_MADI("أَمَرَكَ", "amara-command", "كَ", **N3(cat(FBAAD, (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَا»، وَالرَّابِطُ ضَمِيرٌ مَحْذُوفٌ هُوَ مَفْعُولُ «تَشْتَرِيَ»، أَيْ: مَا أَمَرَكَ عِيَالُكَ أَنْ تَشْتَرِيَهُ", "; the clause is the predicate of «what», in the seat of raf'; the pronoun that ties it to «what» is left unsaid — it is the object of «buy»: أَنْ تَشْتَرِيَهُ", "; cümle «mâ»nın haberi, mahallen merfû; râbıt zamiri mahzûftur — bu zamir «teşteriye»nin mef'ûlüdür: أَنْ تَشْتَرِيَهُ")))),
      ENC_NOUN("عِيَالُكَ", "iyal", "كَ", "fail", note_ar=" — الْعِيَالُ: أَهْلُ بَيْتِ الرَّجُلِ الَّذِينَ يَعُولُهُمْ", note_en=" — عِيَال: a man's household, those he keeps", note_tr=" — iyâl: kişinin geçimini üstlendiği ev halkı"),
      AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ بِنَزْعِ الْخَافِضِ، أَيْ: أَمَرَكَ بِأَنْ تَشْتَرِيَ؛ وَحَذْفُ الْجَارِّ قَبْلَ «أَنْ» مُطَّرِدٌ", "; the clause it builds is in the seat of nasb once its jarr letter is dropped — «told you to buy», that is, بِأَنْ تَشْتَرِيَ; dropping the jarr letter before أَنْ is regular", "; kurduğu müevvel masdar cer harfinin hazfiyle mahallen mansûbdur: «بِأَنْ تَشْتَرِيَ»; «en»den önce cer harfinin hazfi kıyâsîdir"),
      MANSUB_AN("تَشْتَرِيَ", "ishtara", ["form-viii-verbs", "naqis-verbs"], who="أَنْتَ", wujub=True, note_ar=" — وَالْمَفْعُولُ ضَمِيرٌ مَحْذُوفٌ يَعُودُ عَلَى «مَا»، أَيْ: تَشْتَرِيَهُ، وَهُوَ الرَّابِطُ", note_en="; its object is a pronoun left unsaid that returns to «what» — «to buy (it)» — and it is what ties the clause to «what»", note_tr="; mef'ûlü «mâ»ya dönen mahzûf zamirdir: «(onu) satın almanı»; râbıt da odur"),
      LAHUM()]
def FAYAQULU_KADHA(end):
    """فَيَقُولُ: كَذَا وَكَذَا."""
    return [YAQULU("فَيَقُولُ", n=(" — وَالْقَائِلُ كُلُّ وَاحِدٍ مِنْهُمْ", " — the speaker is each one of them", " — konuşan: onlardan her biri")), KADHA(), WA_KADHA(punct=end)]

S4 = []
S4.append({"id": "s1", "translation": {
  "en": "then he would take them out of Baghdad in the best of dress and in every mark of honour, until they reached the City of the Messenger — God bless him and grant him peace —",
  "tr": "sonra onları en güzel kıyafetle ve tam bir mürüvvet içinde Bağdat'tan çıkarır, Resûl'ün — Allah ona salât ve selâm eylesin — şehrine varıncaya kadar (böyle götürür);"},
 "tokens": [
  THUMMA(),
  YUKHRIJUHUM(),
  MINP(),
  J("بَغْدَادَ", "baghdad", D_BALAD, "propn", DG, sign=FATHA_JARR),
  BI_NOUN("بِأَحْسَنِ", "ahsan", "أَحْسَنِ", extra=["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ — وَجُرَّ بِالْكَسْرَةِ مَعَ أَنَّهُ عَلَى «أَفْعَلَ» لِأَنَّهُ مُضَافٌ؛ وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en="; annexed — it takes the kasra although it is on أَفْعَل, because it is annexed; the ba means «with, in»", note_tr="; muzâf — «ef'al» vezninde olduğu hâlde muzâf olduğu için kesre ile mecrûr; bâ musâhabe içindir"),
  MI("زِيٍّ", "ziyy", (" — الزِّيُّ: الْهَيْئَةُ وَاللِّبَاسُ", " — زِيّ: dress, outward appearance", " — ziy: kılık kıyafet"), punct="،"),
  ATF("وَأَكْمَلِ", "akmal", case="jarr", extra=["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ — وَالْمَعْطُوفُ عَلَيْهِ «أَحْسَنِ»", note_en=", annexed — conjoined to «the best»", note_tr=", muzâf — «en güzel»e ma'tûf"),
  MI("مُرُوءَةٍ", "muruwa", (" — الْمُرُوءَةُ: كَمَالُ الرُّجُولِيَّةِ وَمَحَاسِنُ الْأَخْلَاقِ وَالْعَادَاتِ", " — مُرُوءَة: manly honour, all that becomes a man in his ways", " — mürüvvet: insanlığın kemâli, güzel ahlâk ve âdâb"), punct="،"),
  tok("حَتَّى", "hatta", "part", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari", "ila-hatta-fi-wal-ba-fil-kafiya"],
    "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِحَتَّى.",
    "حَتَّى «until»: a jarr letter of the end-point; the present verb after it is put in nasb by a hidden أَنْ, and the clause that أَنْ builds is in the seat of jarr after حَتَّى.",
    "Hattâ «-inceye kadar»: gâye ve cer harfi; sonraki muzâri vücûben gizli en ile mansûbdur, müevvel masdar hattâ ile mahallen mecrûrdur."),
  FIVE_NASB("يَصِلُوا", "wasala", ["mithal-verbs"], by="أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", by_en="an أَنْ hidden after حَتَّى", by_tr="hattâ'dan sonra gizli en"),
  ILAP(),
  J("مَدِينَةِ", "madina", MUDAF, extra=["idafa-definiteness"]),
  MI("الرَّسُولِ", "rasul", punct=" —"),
  MADI_ALIF("صَلَّى", "salla", ["form-ii-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا", note_en="; its doer follows — the clause is a prayer set in parenthesis, with no seat of its own", note_tr="; fâili ardından gelir — cümle duâ cümlesidir, mu'tarızadır, i'râbdan mahalli yoktur"),
  ALLAH_F(),
  ALAYHI(),
  MADI("وَسَلَّمَ", "sallama", ["form-ii-verbs"], hidden=True, punct=" —")]})

S4.append({"id": "s2", "translation": {
  "en": "and he would say to each one: “What did your family tell you to buy for them from Medina, of its choice things?” And he would say: “Such-and-such.”",
  "tr": "ve her birine: «Ailen Medine'den, oranın nâdide şeylerinden kendileri için ne almanı söyledi?» derdi. O da: «Şunu şunu» derdi."},
 "tokens": [
  YAQULU("فَيَقُولُ", punct=None), LI_KULL(), MI("وَاحِدٍ", "wahid", punct=":")] + MA_AMARAKA() + [
  MINA(),
  J("الْمَدِينَةِ", "madina", (" — «الْمَدِينَةُ» بِالتَّعْرِيفِ عَلَمٌ بِالْغَلَبَةِ عَلَى مَدِينَةِ الرَّسُولِ ﷺ", " — with the article, «the City» is by long use the proper name of the Prophet's city ﷺ", " — harf-i ta'rîfli «el-Medîne», galebe yoluyla Resûlullah'ın ﷺ şehrinin özel adı olmuştur")),
  MINP(JM("بَدَلٌ مِنَ الْجَارِّ وَالْمَجْرُورِ قَبْلَهُ، أَيْ: مِنْ طُرَفِ الْمَدِينَةِ", "is a badal of the jarr phrase before it: «from Medina», that is, from its choice things", "öncesindeki câr-mecrûrdan bedeldir: «Medine'den», yani oranın nâdide şeylerinden")),
  ENC_NOUN("طُرَفِهَا", "turfa", "هَا", "majr", extra=["jam-taksir"], punct="؟", note_ar=" — جَمْعُ طُرْفَةٍ: الشَّيْءُ الْمُسْتَحْدَثُ الْمُعْجِبُ الَّذِي يُهْدَى", note_en=" — the plural of طُرْفَة: a novelty, a choice thing brought home as a gift", note_tr=" — turfe'nin cem'i: hediye olarak götürülen nâdide, hoş şey")] + FAYAQULU_KADHA(".")})

S4.append({"id": "s3", "translation": {
  "en": "Then he would take them on to Mecca, and when they had completed their ḥajj he said to each one of them: “What did your family tell you to buy for them of the goods of Mecca?” And he would say: “Such-and-such.”",
  "tr": "Sonra onları Mekke'ye götürürdü; haclarını eda ettiklerinde her birine: «Ailen Mekke'nin mallarından kendileri için ne almanı söyledi?» derdi. O da: «Şunu şunu» derdi."},
 "tokens": [
  THUMMA(), YUKHRIJUHUM(), ILAP(), MAKKA("j", punct="،"),
  FA_IDHA(),
  VERB_WAW("قَضَوْا", "qada-verb", ["thulathi-mujarrad-babs"], alif=True, note_ar=IDHA_CL[0] + "؛ قَضَى الْحَجَّ: أَدَّاهُ وَأَتَمَّهُ", note_en=IDHA_CL[1] + "; قَضَى الْحَجَّ: to perform the ḥajj to its end", note_tr=IDHA_CL[2] + "; «kadâ'l-hacc»: haccı eda edip tamamlamak"),
  ENC_NOUN("حَجَّهُمْ", "hajj", "هُمْ", "maful", punct="،"),
  ADD(QALA("قَالَ", hidden=True, punct=None), IDHA_JAWAB),
  LI_KULL(), MI("وَاحِدٍ", "wahid"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", punct=":", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«وَاحِدٍ»", note_en="; the jarr phrase qualifies «one», in the seat of jarr", note_tr="; câr-mecrûr «biri» için na't, mahallen mecrûr")] + MA_AMARAKA() + [
  MINP(),
  J("مَتَاعِ", "mata-goods", MUDAF, extra=["idafa-definiteness"]),
  MAKKA("mi", punct="؟")] + FAYAQULU_KADHA(".")})

S4.append({"id": "s4", "translation": {
  "en": "So he would buy it for them; then he would take them out of Mecca, and he kept on spending on them until they came back to Marw, and then he would plaster their houses and their doors.",
  "tr": "O da onlar için satın alır; sonra onları Mekke'den çıkarır, Merv'e varıncaya kadar durmadan onlara harcar, (varınca da) evlerini ve kapılarını kireçle sıvatırdı."},
 "tokens": [
  MUDARI("فَيَشْتَرِي", "ishtara", ["form-viii-verbs"], naqis="ي"),
  LAHUM(punct="،"),
  THUMMA(), YUKHRIJUHUM(), MINP(), MAKKA("j", punct="،"),
  FA_LA(), YAZALU(),
  MUDARI("يُنْفِقُ", "anfaqa", ["form-iv-verbs", "kana-wa-akhawatuha"], **N3(KH_YAZAL)),
  ALAYHIM2(),
  ILAP(JM("مُتَعَلِّقٌ بِـ«يُنْفِقُ»", "attaches to «spending»", "«harcar»a müteallik")),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ (أَيْ: صَيْرُورَتِهِمْ) فِي مَحَلِّ جَرٍّ بِإِلَى", "; the clause it builds («their coming») is in the seat of jarr after إِلَى", "; kurduğu müevvel masdar («varmaları») ilâ ile mahallen mecrûr"),
  ADD(FIVE_NASB("يَصِيرُوا", "sara", ["hollow-verbs", "al-fil-al-tamm-wal-naqis"]), (" — وَ«صَارَ» هُنَا تَامَّةٌ بِمَعْنَى رَجَعَ وَانْتَهَى، فَالْوَاوُ فَاعِلُهَا", " — صَارَ is here the complete verb, «to come back to, to end at»: the waw is its doer", " — «sâra» burada tam fiildir: «dönmek, varmak»; vâv fâilidir")),
  ILAP(),
  J("مَرْوَ", "marw", D_MARW, "propn", DG, sign=FATHA_JARR, punct="،"),
  MUDARI("فَيُجَصِّصُ", "jassasa", ["form-ii-verbs"], note_ar=" — جَصَّصَ الْبَيْتَ: طَلَاهُ بِالْجِصِّ، أَيْ: يُجَدِّدُ بُيُوتَهُمْ", note_en=" — جَصَّصَ: to coat with gypsum plaster — he has their houses done up afresh", note_tr=" — «cassasa»: kireçle (alçıyla) sıvamak — evlerini yeniletir"),
  ENC_NOUN("بُيُوتَهُمْ", "bayt", "هُمْ", "maful", extra=["jam-taksir"]),
  tok("وَأَبْوَابَهُمْ", "bab", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "أَبْوَابَ مَعْطُوفٌ عَلَى «بُيُوتَ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The waw conjoins; «doors» is conjoined to «houses», in nasb and annexed; the attached «their» is the second term of the idafa, in the seat of jarr.",
    "«ve» + «kapılar», «evler»e ma'tûf, mansûb, muzâf; bitişik «onların» zamiri muzâfun ileyh, mahallen mecrûr.", punct="،",
    segments=[seg("وَ", "wa", "conj"), seg("أَبْوَابَ", "bab", "noun"), seg("هُمْ", "pron-3mp", "pron")])]})

S4.append({"id": "s5", "translation": {
  "en": "And when three days had passed, he made a banquet for them and gave them new clothes;",
  "tr": "Üç gün geçince onlara bir ziyafet verir ve onları giydirirdi;"},
 "tokens": [
  FA_IDHA(),
  IT(KANA_HID("كَانَ", note=(" يَعُودُ عَلَى الْوَقْتِ الْمَفْهُومِ مِنَ السِّيَاقِ" + IDHA_CL[0], " — the time understood from the context" + IDHA_CL[1], " — siyâktan anlaşılan vakte döner" + IDHA_CL[2]))),
  ZARF("بَعْدَ", "bada", *ZAMAN, note_ar=" — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ", note_en=" — it hangs on an omitted word that is the predicate of كَانَ", note_tr=" — kâne'nin mahzûf haberine müteallik"),
  MI("ثَلَاثَةِ", "thalatha", cat(MUDAF, (" — وَجَاءَ الْعَدَدُ بِالتَّاءِ لِأَنَّ مُفْرَدَ الْمَعْدُودِ (يَوْم) مُذَكَّرٌ", " — the number takes the ta because the singular of the counted noun (يَوْم) is masculine", " — sayılanın müfredi (yevm) müzekker olduğu için sayı tâ ile gelmiştir")), extra=["idafa-definiteness", "asma-al-adad-fil-kafiya"]),
  MI("أَيَّامٍ", "yawm", (" — جَمْعُ يَوْمٍ؛ وَتَمْيِيزُ الثَّلَاثَةِ إِلَى الْعَشَرَةِ جَمْعٌ مَجْرُورٌ", " — the plural of يَوْم; what is counted from three to ten stands in the plural, in jarr", " — yevm'in cem'i; üçten ona kadar sayıların temyizi cemi ve mecrûr gelir"), extra=["jam-taksir"], punct="،"),
  MADI("عَمِلَ", "amila", hidden=True, **N3(IDHA_JAWAB)),
  LAHUM(),
  O("وَلِيمَةً", "walima", (" — الْوَلِيمَةُ: طَعَامٌ يُصْنَعُ لِدَعْوَةٍ وَفَرَحٍ", " — وَلِيمَة: a feast made for guests on a glad occasion", " — velîme: davet ve sevinç için hazırlanan yemek")),
  ENC_MADI("وَكَسَاهُمْ", "kasa", "هُمْ", alif=True, hidden=True, punct="،", note_ar=" — وَكَسَا يَتَعَدَّى إِلَى مَفْعُولَيْنِ، وَالثَّانِي مَحْذُوفٌ، أَيْ: كَسَاهُمْ ثِيَابًا", note_en=" — كَسَا takes two objects; the second is left unsaid: «he clothed them (in garments)»", note_tr=" — «kesâ» iki mef'ûl alır; ikincisi mahzûftur: «onlara (elbise) giydirdi»")]})

S4.append({"id": "s6", "translation": {
  "en": "and when they had eaten and were glad, he called for the chest, opened it, and handed to every man of them his own purse with his name on it.",
  "tr": "yiyip sevindiklerinde sandığı getirtir, açar ve onlardan her adama, üzerinde adı yazılı kesesini verirdi."},
 "tokens": [
  FA_IDHA(),
  VERB_WAW("أَكَلُوا", "akala", ["thulathi-mujarrad-babs"], note_ar=IDHA_CL[0], note_en=IDHA_CL[1], note_tr=IDHA_CL[2]),
  tok("وَسُرُّوا", "sarra", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "doubled-verbs", "al-bariz-al-muttasil", "atf-nasaq"],
    WA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — مِنْ سَرَّهُ يَسُرُّهُ: أَفْرَحَهُ.",
    "The waw conjoins; a past verb in the passive, built on damma before the waw of the group; that waw is the deputy doer, in the seat of raf' — from سَرَّهُ «he gladdened him»: «they were made glad».",
    "«ve» + meçhul mâzî, cemâat vâvı bitiştiği için damme üzere mebnî; vâv nâib-i fâil, mahallen merfû — «serrahû» (onu sevindirdi) fiilinden: «sevindirildiler».", punct="،",
    segments=[seg("وَ", "wa", "conj"), seg("سُرُّو", "sarra", "verb"), seg("ا", "pron-3mp", "pron")]),
  MADI_ALIF("دَعَا", "daa", hidden=True, note_ar=IDHA_JAWAB[0] + "؛ دَعَا بِالشَّيْءِ: طَلَبَ إِحْضَارَهُ", note_en=IDHA_JAWAB[1] + "; دَعَا بِـ: to call for a thing to be brought", note_tr=IDHA_JAWAB[2] + "; «deâ bi»: bir şeyin getirilmesini istemek"),
  BI_NOUN("بِالصُّنْدُوقِ", "sunduq", "الصُّنْدُوقِ", punct="،"),
  ENC_MADI("فَفَتَحَهُ", "fataha", "هُ", hidden=True, punct="،"),
  MADI("وَدَفَعَ", "dafaa", hidden=True, note_ar=" — دَفَعَ إِلَيْهِ الشَّيْءَ: سَلَّمَهُ إِيَّاهُ", note_en=" — دَفَعَ إِلَى: to hand a thing over to someone", note_tr=" — «defea ilâ»: bir şeyi birine teslim etmek"),
  ILAP(),
  J("كُلِّ", "kull", MUDAF, extra=["idafa-definiteness"]),
  MI("رَجُلٍ", "rajul"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«رَجُلٍ»", note_en="; the jarr phrase qualifies «a man», in the seat of jarr", note_tr="; câr-mecrûr «adam» için na't, mahallen mecrûr"),
  ENC_NOUN("صُرَّتَهُ", "surra", "هُ", "maful", note_ar=" — الصُّرَّةُ: مَا يُصَرُّ فِيهِ الدَّرَاهِمُ وَيُشَدُّ", note_en=" — صُرَّة: a pouch in which coins are tied up", note_tr=" — surre: içine para konup ağzı bağlanan kese"),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («üzerinde»)", extra=["taqdim-al-musnad", "al-hal-jumla-wa-rabituha"], note_ar="، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ — وَجُمْلَةُ «عَلَيْهَا اسْمُهُ» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «صُرَّتَهُ»، وَالرَّابِطُ الضَّمِيرُ", note_en="; the jarr phrase hangs on an omitted word that is the fronted khabar — the clause «with his name on it» is a hal of «his purse», in the seat of nasb, tied to it by the pronoun", note_tr="; câr-mecrûr öne alınmış mahzûf habere müteallik — «üzerinde adı (yazılı)» cümlesi «kesesi»nden hâl, mahallen mansûb; râbıt zamirdir"),
  tok("اسْمُهُ", "ism-name", "noun", ["mubtada-khabar", "taqdim-al-musnad", "idafa-definiteness", "al-bariz-al-muttasil"],
    "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The mubtada, placed after its khabar, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr.",
    "Haberinden sonra gelmiş mübtedâ, merfû, muzâf; bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr.", punct=".",
    segments=[seg("اسْمُ", "ism-name", "noun"), seg("هُ", "pron-3ms", "pron")])]})

# ================================================ Chapter 5 — الشَّابُّ الْمَحْبُوسُ (8/386–387) ================================================
ASHRA_N = (" — هٰكَذَا ضُبِطَتْ فِي الطَّبْعَةِ بِسُكُونِ الشِّينِ، وَالْمَشْهُورُ فِي الْعَدَدِ الْمُفْرَدِ «عَشَرَة» بِفَتْحِهَا؛ وَجَاءَ بِالتَّاءِ لِأَنَّ مُفْرَدَ الْمَعْدُودِ (أَلْف) مُذَكَّرٌ",
           " — so the edition vowels it, with a quiescent shīn; the usual form of the simple number is عَشَرَة, with fatha. It takes the ta because the singular of the counted noun (أَلْف) is masculine",
           " — baskı şîni sâkin olarak böyle harekelemiştir; müfred sayıda meşhur olan fetha ile «عَشَرَة»dir. Sayılanın müfredi (elf) müzekker olduğu için sayı tâ ile gelmiştir")
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Muḥammad ibn al-Mundhir said: Yaʿqūb ibn Isḥāq narrated to me: Muḥammad ibn ʿĪsā narrated to me; he said:",
  "tr": "Muhammed b. Münzir dedi ki: Bana Ya'kûb b. İshâk anlattı; (dedi ki:) bana Muhammed b. Îsâ anlattı; dedi ki:"},
 "tokens": [
  QALA("قَالَ"),
  PN("مُحَمَّدُ", "muhammad", *FAIL_PN, ["fail"], DROP),
  BN("raf", "مُحَمَّدُ", "Muḥammad", "Muhammed"),
  MI("الْمُنْذِرِ", "mundhir-name", pos="propn", punct=":"),
  HADDATHANI(MAQUL_CL),
  PN("يَعْقُوبُ", "yaqub", *FAIL_PN, ["fail"] + DG, D_AJ_R),
  BN("raf", "يَعْقُوبُ", "Yaʿqūb", "Ya'kûb"),
  MI("إِسْحَاقَ", "ishaq", D_AJ, "propn", DG, sign=FATHA_JARR, punct="،"),
  HADDATHANI(),
  PN("مُحَمَّدُ", "muhammad", *FAIL_PN, ["fail"], DROP),
  BN("raf", "مُحَمَّدُ", "Muḥammad", "Muhammed"),
  MI("عِيسَى", "isa", (" — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ، وَهُوَ مَقْصُورٌ فَتُقَدَّرُ الْحَرَكَةُ عَلَى أَلِفِهِ", " — a foreign name, barred from tanwin; it ends in alif maqṣūra, so its case-vowel is estimated on the alif", " — yabancı özel isim, gayr-i munsarif; maksûr olduğu için harekesi elif üzerinde takdîrîdir"),
     "propn", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ نِيَابَةً عَنِ الْكَسْرَةِ", punct="،"),
  QH("قَالَ", ("مُحَمَّدُ بْنُ عِيسَى", "Muḥammad ibn ʿĪsā", "Muhammed b. Îsâ"))]})

S5.append({"id": "s2", "translation": {
  "en": "Ibn al-Mubārak used to go back and forth to Ṭarasūs a great deal, and he would put up at an inn in al-Raqqa.",
  "tr": "İbnü'l-Mübârek Tarsus'a çok gidip gelirdi; Rakka'da da bir handa konaklardı."},
 "tokens": [
  ADD(KANA("كَانَ"), MAQUL_CL),
  IBN("raf", "ismk"),
  MUBARAK(),
  KK("كَثِيرَ", "kathir", cat(MUDAF, (" — صِفَةٌ مُشَبَّهَةٌ أُضِيفَتْ إِلَى فَاعِلِهَا فِي الْمَعْنَى (إِضَافَةٌ لَفْظِيَّةٌ): كَثُرَ اخْتِلَافُهُ", " — an adjective annexed to what is its doer in sense (a «verbal» idafa): «his goings were many»", " — mânâca fâiline muzâf sıfat-ı müşebbehe (lafzî izâfet): «gidip gelmesi çoktu»")), extra=["sifa-mushabbaha", "idafa-lafziyya", "idafa-definiteness"]),
  MI("الِاخْتِلَافِ", "ikhtilaf", (" — مَصْدَرُ اخْتَلَفَ إِلَى الْمَكَانِ: تَرَدَّدَ إِلَيْهِ مَرَّةً بَعْدَ مَرَّةٍ", " — the masdar of اِخْتَلَفَ إِلَى: to go to a place again and again", " — «ihtelefe ilâ»nın masdarı: bir yere tekrar tekrar gidip gelmek"), extra=["masdar"]),
  ILAP(JM("مُتَعَلِّقٌ بِـ«الِاخْتِلَافِ»", "attaches to «going back and forth»", "«gidip gelme»ye müteallik")),
  J("طَرَسُوسَ", "tarasus", D_BALAD, "propn", DG, sign=FATHA_JARR, punct="،"),
  KANA_HID("وَكَانَ"),
  MUDARI("يَنْزِلُ", "nazala", ["kana-wa-akhawatuha"], **N3(KH_KANA_CL)),
  RAQQA("nasb", n=(" — نَزَلَ الْمَكَانَ: حَلَّ بِهِ، يَتَعَدَّى بِنَفْسِهِ", " — نَزَلَ الْمَكَانَ «to alight at a place» takes the place as its direct object", " — «nezele'l-mekâne»: bir yere konmak; yeri doğrudan mef'ûl alır")),
  FIP(),
  J("خَانٍ", "khan-inn", (" — الْخَانُ: مَنْزِلُ الْمُسَافِرِينَ، فَارِسِيٌّ مُعَرَّبٌ", " — خَان: a lodging-house for travellers, a Persian word made Arabic", " — hân: yolcuların konakladığı yer; Farsçadan Arapçaya geçmiştir"), punct="،")]})

S5.append({"id": "s3", "translation": {
  "en": "And a young man used to come to him, see to his needs and hear ḥadīth from him.",
  "tr": "Bir genç de onun yanına gelip gider, ihtiyaçlarını görür ve ondan hadis dinlerdi."},
 "tokens": [
  KANA("فَكَانَ"),
  IK("شَابٌّ", "shabb"),
  MUDARI("يَخْتَلِفُ", "ikhtalafa", ["form-viii-verbs", "kana-wa-akhawatuha"], **N3(KH_KANA_CL)),
  ILAYHI(punct="،"),
  MUDARI("وَيَقُومُ", "qama", ["hollow-verbs"]),
  BI_NOUN("بِحَوَائِجِهِ", "haja", "حَوَائِجِهِ", enc="هِ", extra=["jam-taksir"], punct="،", note_ar=" — جَمْعُ حَاجَةٍ؛ وَقَامَ بِالْأَمْرِ: تَوَلَّاهُ", note_en=" — the plural of حَاجَة; قَامَ بِـ: to take a matter upon oneself", note_tr=" — hâcet'in cem'i; «kâme bi»: bir işi üstlenmek"),
  MUDARI("وَيَسْمَعُ", "samia"),
  MINHU(),
  O("الْحَدِيثَ", "hadith", punct="،")]})

S5.append({"id": "s4", "translation": {
  "en": "Then ʿAbd Allāh came one time and did not see him; and he went out with the call to arms in haste.",
  "tr": "Abdullah bir defasında geldi ve onu göremedi; sonra aceleyle umumi sefere çıktı."},
 "tokens": [
  MADI("فَقَدِمَ", "qadima", **N3(FBAAD)),
  F("عَبْدُ", "abd", MUDAF, extra=["idafa-definiteness"]),
  ALLAH_MI(),
  tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq"],
    "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ عَدَدَ الْفِعْلِ: قَدِمَ قَدْمَةً وَاحِدَةً، أَيْ: فِي إِحْدَى الْمَرَّاتِ.",
    "It stands in for the absolute object, in nasb by the fatha — it counts the act: «he came one coming», that is, on one occasion.",
    "Mef'ûl-i mutlaktan nâib, fetha ile mansûb — fiilin sayısını bildirir: «bir geliş geldi», yani bir defasında.", punct="،"),
  LAM_JAZM("فَلَمْ"),
  tok("يَرَهُ", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْأَلِفِ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَأَصْلُ يَرَى: يَرْأَى، حُذِفَتْ هَمْزَتُهُ تَخْفِيفًا.",
    "Present verb in jazm by لَمْ, its sign the dropped weak letter (the alif); the doer is a hidden pronoun «he», and the attached pronoun is its object, in the seat of nasb — يَرَى is from يَرْأَى: its hamza was dropped to lighten the word.",
    "Lem ile meczûm muzâri, alâmeti illet harfinin (elifin) hazfi; fâil gizli zamir «o», bitişik zamir mef'ûlün bih, mahallen mansûb — يَرَى'nın aslı يَرْأَى'dır; hemzesi tahfif için hazfedilmiştir.", punct="،",
    segments=[seg("يَرَ", "raa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  MADI("فَخَرَجَ", "kharaja", hidden=True),
  FIP(),
  J("النَّفِيرِ", "nafir", (" — النَّفِيرُ: الْقَوْمُ يَنْفِرُونَ لِلْقِتَالِ، وَخُرُوجُهُمْ إِلَيْهِ عِنْدَ الِاسْتِنْفَارِ", " — النَّفِير: the body of men who go out to fight, and their going out when the call is raised", " — nefîr: savaşa çıkan topluluk ve çağrı yapılınca sefere çıkış")),
  HAL("مُسْتَعْجِلًا", "mustajil", ["ism-fail"], punct="،")]})

S5.append({"id": "s5", "translation": {
  "en": "When he came back he asked about the young man, and [the man he asked] said: “In prison, over ten thousand dirhams.”",
  "tr": "Dönünce genci sordu; (sorduğu kimse) «On bin dirhem yüzünden hapiste» dedi."},
 "tokens": [
  LAMMA2("فَلَمَّا"),
  MADI("رَجَعَ", "rajaa", hidden=True, punct="،", **N3(LAMMA_CL)),
  MADI("سَأَلَ", "saala", hidden=True, note_ar=" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", note_en="; the clause is the answer of لَمَّا and has no seat of its own", note_tr="; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur"),
  AN_K(),
  J("الشَّابِّ", "shabb", punct="،"),
  ADD(QALA("فَقَالَ", hidden=True, punct=":"), (" — وَالضَّمِيرُ يَعُودُ عَلَى الْمَسْؤُولِ الْمَفْهُومِ مِنْ «سَأَلَ»؛ هٰكَذَا فِي الطَّبْعَتَيْنِ بِالْإِفْرَادِ", " — the pronoun is the one who was asked, understood from «he asked»; so both editions have it, in the singular", " — zamir, «sordu»dan anlaşılan sorulan kimseye döner; her iki baskıda da böyle müfred gelmiştir")),
  tok("مَحْبُوسٌ", "mahbus", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "ism-maful"],
    "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ، مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولٍ مِنْ حَبَسَ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "The predicate (khabar) of a dropped mubtada — «he is» — in raf' by the damma; the passive participle of حَبَسَ. The clause is what is said, in the seat of nasb.",
    "Hazfedilmiş mübtedânın («o») haberi, damme ile merfû — habese'nin ism-i mef'ûlü; cümle mekûlü'l-kavl olarak mahallen mansûb."),
  ALAP(JM("مُتَعَلِّقٌ بِـ«مَحْبُوسٌ»، وَ«عَلَى» لِلتَّعْلِيلِ: بِسَبَبِ دَيْنٍ قَدْرُهُ ذٰلِكَ", "attaches to «imprisoned»; عَلَى gives the cause: on account of a debt of that sum", "«mahbûs»a müteallik; «alâ» ta'lîl içindir: o miktardaki borç sebebiyle")),
  J("عَشْرَةِ", "ashara", cat(MUDAF, ASHRA_N), extra=["idafa-definiteness", "asma-al-adad-fil-kafiya"]),
  MI("آلَافِ", "alf", cat(MUDAF, (" — جَمْعُ أَلْفٍ", " — the plural of أَلْف", " — elf'in cem'i")), extra=["jam-taksir", "idafa-definiteness", "asma-al-adad-fil-kafiya"]),
  MI("دِرْهَمٍ", "dirham", (" — تَمْيِيزُ الْأَلْفِ مُفْرَدٌ مَجْرُورٌ بِالْإِضَافَةِ", " — what is counted by «a thousand» stands in the singular, in jarr by the idafa", " — «bin»in temyizi müfred ve izâfetle mecrûr gelir"), punct=".")]})

S5.append({"id": "s6", "translation": {
  "en": "So he had himself directed to the creditor, weighed out ten thousand for him, and made him swear to tell no one as long as he lived.",
  "tr": "Bunun üzerine alacaklıyı sorup buldu, ona on bin (dirhem) tartıp verdi ve yaşadığı müddetçe kimseye haber vermeyeceğine dair ona yemin ettirdi."},
 "tokens": [
  MADI("فَاسْتَدَلَّ", "istadalla", ["form-x-verbs", "doubled-verbs"], hidden=True, note_ar=" — اسْتَدَلَّ عَلَى الشَّيْءِ: طَلَبَ أَنْ يُدَلَّ عَلَيْهِ", note_en=" — اِسْتَدَلَّ عَلَى: to ask to be shown the way to someone", note_tr=" — «istedelle alâ»: birinin yerinin kendisine gösterilmesini istemek"),
  ALAP(),
  J("الْغَرِيمِ", "gharim", (" — الْغَرِيمُ هُنَا: صَاحِبُ الدَّيْنِ، وَيُطْلَقُ أَيْضًا عَلَى الْمَدِينِ", " — غَرِيم here is the creditor; the word is also used of the debtor", " — garîm burada alacaklıdır; borçlu için de kullanılır"), punct="،"),
  MADI("وَوَزَنَ", "wazana", ["mithal-verbs"], hidden=True, note_ar=" — كَانَتِ الدَّرَاهِمُ تُوزَنُ عِنْدَ الدَّفْعِ", note_en=" — coins were weighed out when they were paid", note_tr=" — dirhemler ödenirken tartılırdı"),
  LAHU3("لَهُ", "pron-3ms", " («ona»)"),
  O("عَشْرَةَ", "ashara", MUDAF, extra=["idafa-definiteness", "asma-al-adad-fil-kafiya"]),
  MI("آلَافٍ", "alf", (" — وَالتَّمْيِيزُ مَحْذُوفٌ، أَيْ: عَشَرَةَ آلَافِ دِرْهَمٍ", " — the thing counted is left unsaid: ten thousand dirhams", " — temyiz mahzûftur: on bin dirhem"), extra=["jam-taksir", "asma-al-adad-fil-kafiya"], punct="،"),
  ENC_MADI("وَحَلَّفَهُ", "hallafa", "هُ", ["form-ii-verbs"], hidden=True, note_ar=" — حَلَّفَهُ: طَلَبَ مِنْهُ الْحَلِفَ", note_en=" — حَلَّفَهُ: he made him swear", note_tr=" — «hallefehû»: ona yemin ettirdi"),
  tok("أَلَّا", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari", "la-nafiya", "hadhf-al-jarr"],
    "أَنْ حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ، وَلَا نَافِيَةٌ، وَأُدْغِمَتِ النُّونُ فِي اللَّامِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَنْصُوبٌ بِنَزْعِ الْخَافِضِ، أَيْ: حَلَّفَهُ عَلَى أَلَّا يُخْبِرَ.",
    "أَنْ, the masdar-making particle that governs nasb, with the negating لَا — the nun is merged into the lam; the clause they build is in nasb once its jarr letter is dropped: «he made him swear (to) tell no one».",
    "Masdariyye ve nasb harfi en ile nefiy lâ'sı; nûn lâma idgam edilmiştir — müevvel masdar cer harfinin hazfiyle mansûbdur: «haber vermemesi üzerine yemin ettirdi».",
    segments=[seg("أَ", "an-masdariyya", "part"), seg("لَّا", "la-nafiya", "part")]),
  MANSUB_AN("يُخْبِرَ", "akhbara", ["form-iv-verbs"]),
  O("أَحَدًا", "ahad"),
  tok("مَا", "ma-masdariyya", "part", ["an-masdariyya", "maful-fih", "anwa-ma"],
    "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ بَعْدَهَا نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ، أَيْ: مُدَّةَ عَيْشِهِ.",
    "The مَا of duration: with the verb after it, it builds a masdar that stands as an adverb of time — «for as long as he lived».",
    "Masdariyye-zarfiyye mâ'sı: sonraki fiille birlikte zaman zarfı yerine geçen bir masdar kurar — «yaşadığı müddetçe»."),
  MADI("عَاشَ", "asha-live", ["hollow-verbs"], hidden=True, punct="،", note_ar=" — وَالظَّاهِرُ أَنَّ الضَّمِيرَ لِابْنِ الْمُبَارَكِ، بِدَلِيلِ آخِرِ الْخَبَرِ: «إِلَّا بَعْدَ مَوْتِ عَبْدِ اللهِ»", note_en=" — most likely Ibn al-Mubārak, as the end of the report shows: «not until after ʿAbd Allāh's death»", note_tr=" — zâhire göre İbnü'l-Mübârek'e döner; haberin sonu buna delildir: «ancak Abdullah'ın ölümünden sonra»")]})

# ================================================ Chapter 6 — جَاءَ رَجُلٌ فَقَضَى دَيْنِي (8/387) ================================================
ABA_ABD = lambda end: [
  YA(),
  tok("أَبَا", "ab", "noun", ["vocative-munada", "five-nouns", "idafa-definiteness"],
    "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ.", "The vocative, annexed, in nasb by the alif — one of the five nouns.", "Muzâf münâdâ; esmâ-i hamseden olduğu için elif ile mansûb."),
  MI("عَبْدِ", "abd", MUDAF, extra=["idafa-definiteness"]),
  MI("الرَّحْمٰنِ", "rahman", (" — كُنْيَةُ ابْنِ الْمُبَارَكِ", " — the kunya of Ibn al-Mubārak", " — İbnü'l-Mübârek'in künyesi"), "propn", punct=end)]
S6 = []
S6.append({"id": "s1", "translation": {
  "en": "So the man was let out, and Ibn al-Mubārak travelled on by night; and the young man caught up with him two days' journey from al-Raqqa.",
  "tr": "Böylece adam (hapisten) çıkarıldı; İbnü'l-Mübârek de gece yola koyuldu. Genç, Rakka'dan iki konak ötede ona yetişti."},
 "tokens": [
  MAJHUL("فَأُخْرِجَ", "akhraja", ["form-iv-verbs"]),
  NAIB("الرَّجُلُ", "rajul", punct="،", note_ar=" — أَيِ الشَّابُّ الْمَحْبُوسُ", note_en=" — the young man who had been imprisoned", note_tr=" — yani hapisteki genç"),
  MADI_ALIF("وَسَرَى", "sara-night", **N3(cat(FBAAD, (" — سَرَى: سَارَ لَيْلًا", " — سَرَى: to travel by night", " — «serâ»: gece yol almak")))),
  IBN("raf", "fail"),
  MUBARAK(punct="،"),
  ENC_MADI("فَلَحِقَهُ", "lahiqa", "هُ", **N3(FBAAD)),
  F("الْفَتَى", "fata-youth", (" — اسْمٌ مَقْصُورٌ", " — a noun ending in alif maqṣūra: the damma is estimated on the alif", " — maksûr isim; damme elif üzerinde takdîrîdir"), extra=["ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"),
  ALAP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ، أَيْ: لَحِقَهُ وَهُوَ عَلَى مَسَافَةِ مَرْحَلَتَيْنِ", "hangs on an omitted hal: «he caught up with him when he was two stages away»", "mahzûf bir hâle müteallik: «o iki konak mesafedeyken ona yetişti»")),
  J("مَرْحَلَتَيْنِ", "marhala", cat(S_DUAL, (" — الْمَرْحَلَةُ: الْمَسَافَةُ الَّتِي يَقْطَعُهَا الْمُسَافِرُ فِي يَوْمٍ", " — مَرْحَلَة: a stage, the distance a traveller covers in a day", " — merhale: yolcunun bir günde aldığı mesafe, konak")), extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى"),
  MINA(),
  RAQQA("jarr", punct="،")]})

S6.append({"id": "s2", "translation": {
  "en": "He said to me [so the text reads; it is the young man who is addressed]: “Young man, where have you been? I did not see you!”",
  "tr": "(İbnü'l-Mübârek) bana [metinde böyledir; muhatap gençtir] dedi ki: «Ey delikanlı, neredeydin? Seni göremedim!»"},
 "tokens": [
  QH("فَقَالَ", IBN_MUB, punct=None),
  tok("لِي", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"],
    "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — هٰكَذَا فِي الطَّبْعَتَيْنِ «لِي» بِيَاءِ الْمُتَكَلِّمِ، وَالْمُخَاطَبُ هُوَ الْفَتَى، وَالسِّيَاقُ يَقْتَضِي «لَهُ»؛ فَكَأَنَّ الرَّاوِيَ يَحْكِي هُنَا لَفْظَ الْفَتَى نَفْسِهِ.",
    "The lam is a jarr letter; the ya of the speaker fills the seat of jarr. Both editions read «to me», though the one addressed is the young man and the context calls for «to him» — as if the narrator here slips into the young man's own telling.",
    "Lâm cer harfi; mütekellim yâ'sı mahallen mecrûr. Her iki baskıda da «bana» şeklindedir; oysa muhatap gençtir ve siyâk «ona» gerektirir — sanki râvî burada gencin kendi ifadesini nakletmektedir.", punct=":",
    segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  YA(),
  tok("فَتَى", "fata-youth", "noun", ["vocative-munada", "ism-maqsur-manqus"],
    "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ فِي مَحَلِّ نَصْبٍ.",
    "The vocative — an indefinite noun aimed at one person — built on a damma estimated on the alif, in the seat of nasb.",
    "Münâdâ (nekre-i maksûde); elif üzerinde takdîrî damme üzere mebnî, mahallen mansûb."),
  tok("أَيْنَ", "ayna", "pron", ["al-istifham", "maful-fih", "kana-wa-akhawatuha", "taqdim-al-musnad"],
    "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ مُقَدَّمٌ.",
    "The interrogative «where?», built on fatha, in the seat of nasb as an adverb of place; it hangs on an omitted word that is the fronted predicate of كَانَ.",
    "İstifhâm ismi «nerede?», fetha üzere mebnî, mekân zarfı olarak mahallen mansûb; kâne'nin öne alınmış mahzûf haberine müteallik."),
  tok("كُنْتَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ اسْمُهَا — وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    "كَانَ, the defective past verb, built on sukun before the ta (its middle letter dropped where two quiescents met); the ta «you» is its noun, built on fatha in the seat of raf'.",
    "Nâkıs mâzî kâne; tâ bitiştiği için sükûn üzere mebnî (iki sâkin karşılaşınca aynı düştü); tâ «sen» ismi, fetha üzere mebnî, mahallen merfû.", punct="؟"),
  LAM_JAZM("لَمْ"),
  tok("أَرَكَ", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "al-fail-al-mudmar-al-mustatir-wujuban"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْأَلِفِ)، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "Present verb in jazm by لَمْ, its sign the dropped weak letter (the alif); the doer «I» is a pronoun that must stay hidden, and the attached «you» is its object, in the seat of nasb.",
    "Lem ile meczûm muzâri, alâmeti illet harfinin (elifin) hazfi; fâil vücûben müstetir «ben», bitişik «sen» zamiri mef'ûlün bih, mahallen mansûb.", punct="!",
    segments=[seg("أَرَ", "raa", "verb"), seg("كَ", "pron-2ms", "pron")])]})

S6.append({"id": "s3", "translation": {"en": "He said: “Abū ʿAbd al-Raḥmān! I was in prison for a debt.”", "tr": "(Genç) dedi ki: «Ey Ebû Abdurrahman! Bir borç yüzünden hapisteydim.»"},
 "tokens": [
  QH("قَالَ", FATA)] + ABA_ABD("!") + [
  tok("كُنْتُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ اسْمُهَا.",
    "كَانَ, the defective past verb, built on sukun before the ta; the ta «I» is its noun, built on damma in the seat of raf'.",
    "Nâkıs mâzî kâne; tâ bitiştiği için sükûn üzere mebnî; tâ «ben» ismi, damme üzere mebnî, mahallen merfû."),
  KK("مَحْبُوسًا", "mahbus", extra=["ism-maful"]),
  BI_NOUN("بِدَيْنٍ", "dayn", "دَيْنٍ", punct=".", note_ar=" — وَالْبَاءُ لِلسَّبَبِيَّةِ", note_en=" — the ba gives the cause: «because of a debt»", note_tr=" — bâ sebebiyye içindir: «bir borç yüzünden»")]})

S6.append({"id": "s4", "translation": {
  "en": "He said: “And how did you get free?” He said: “A man came and paid my debt, and I never learned [who].”",
  "tr": "«Peki nasıl kurtuldun?» dedi. (Genç) dedi ki: «Bir adam geldi, borcumu ödedi; (kim olduğunu) öğrenemedim.»"},
 "tokens": [
  QH("قَالَ", IBN_MUB),
  tok("وَكَيْفَ", "kayfa", "noun", ["al-istifham", "hal", "anwa-al-waw"],
    "الْوَاوُ لِلِاسْتِئْنَافِ فِي أَوَّلِ الْمَقُولِ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens the quoted words; كَيْفَ «how» is an interrogative noun built on fatha, in the seat of nasb as a hal.",
    "Vâv, nakledilen sözün başında isti'nâf içindir; keyfe «nasıl»: istifhâm ismi, fetha üzere mebnî, hâl olarak mahallen mansûb.",
    segments=[seg("وَ", "wa", "conj"), seg("كَيْفَ", "kayfa", "noun")]),
  MADI_T("خَلَصْتَ", "khalasa", who="anta", punct="؟", note_ar=" — خَلَصَ مِنَ الشَّيْءِ: نَجَا وَسَلِمَ مِنْهُ", note_en=" — خَلَصَ: to get clear of a thing, to come out safe", note_tr=" — «halasa»: bir şeyden kurtulmak"),
  QH("قَالَ", FATA),
  MADI("جَاءَ", "jaa", ["hollow-verbs"], **N3(cat(FBAAD, MAQUL_CL))),
  F("رَجُلٌ", "rajul"),
  MADI_ALIF("فَقَضَى", "qada-verb", hidden=True, note_ar=" — قَضَى الدَّيْنَ: أَدَّاهُ", note_en=" — قَضَى الدَّيْنَ: to pay off a debt", note_tr=" — «kadâ'd-deyn»: borcu ödemek"),
  YA_MUTAKALLIM_N("دَيْنِي", "dayn", "دَيْنِ", "مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", extra=["maful-bihi"], punct="،"),
  WA_LAM(),
  tok("أَدْرِ", "dara", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs", "al-fail-al-mudmar-al-mustatir-wujuban", "hadhf-al-maful"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ) وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْمَفْعُولُ مَحْذُوفٌ، أَيْ: لَمْ أَدْرِ مَنْ هُوَ.",
    "Present verb in jazm by لَمْ, its sign the dropped weak letter (the ya), the kasra left to point to it; the doer «I» is a pronoun that must stay hidden — its object is left unsaid: «I did not know (who he was)».",
    "Lem ile meczûm muzâri, alâmeti illet harfinin (yâ'nın) hazfi, kesre ona delildir; fâil vücûben müstetir «ben» — mef'ûlü mahzûftur: «(kim olduğunu) bilemedim».", punct=".")]})

S6.append({"id": "s5", "translation": {
  "en": "He said: “Then praise God.” And the man did not come to know of it until after ʿAbd Allāh's death.",
  "tr": "(İbnü'l-Mübârek) «Öyleyse Allah'a hamdet» dedi. Adam (borcunu kimin ödediğini) ancak Abdullah'ın ölümünden sonra öğrendi."},
 "tokens": [
  QH("قَالَ", IBN_MUB),
  tok("فَاحْمَدِ", "hamida", "verb", ["imperative-amr", "al-fail-al-mudmar-al-mustatir-wujuban", "al-fa-fi-jawab-al-shart", "hadhf-wa-taqdir"],
    "الْفَاءُ الْفَصِيحَةُ — أَفْصَحَتْ عَنْ شَرْطٍ مُقَدَّرٍ، أَيْ: إِذَا كَانَ الْأَمْرُ كَذٰلِكَ فَاحْمَدِ اللهَ — وَاحْمَدْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.",
    "The «eloquent» fa: it speaks for a condition left unsaid — «if that is how it was, then praise God»; اِحْمَدْ is an imperative built on sukun, voweled with kasra before the following ال, and its doer «you» is a pronoun that must stay hidden.",
    "Fâ-i fasîha: mukadder bir şartı haber verir — «madem öyle, Allah'a hamdet»; اِحْمَدْ sükûn üzere mebnî emirdir, iki sâkin karşılaştığı için kesre ile harekelenmiştir; fâil vücûben müstetir «sen».",
    segments=[seg("فَ", "fa", "conj"), seg("احْمَدِ", "hamida", "verb")]),
  ALLAH_MAF(punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "anwa-al-waw"],
    "الْوَاوُ لِلِاسْتِئْنَافِ — مِنْ كَلَامِ الرَّاوِي لَا مِنْ كَلَامِ ابْنِ الْمُبَارَكِ — وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
    "The waw opens a new sentence — the narrator's own words, not Ibn al-Mubārak's; لَمْ is the particle of negation and jazm that turns the present to the past.",
    "Vâv isti'nâf içindir — bu söz İbnü'l-Mübârek'in değil râvînindir; lem: nefy, cezm ve kalb harfi.",
    segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  JAZM_V("يَعْلَمِ", "alima", note_ar=" — وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْمَفْعُولُ مَحْذُوفٌ، أَيْ: لَمْ يَعْلَمْ مَنْ قَضَى دَيْنَهُ", note_en=" — it takes a kasra before the following ال; its object is left unsaid: «(who had paid his debt)»", note_tr=" — iki sâkin karşılaştığı için kesre ile harekelendi; mef'ûlü mahzûftur: «(borcunu kimin ödediğini)»"),
  F("الرَّجُلُ", "rajul"),
  ILLA(),
  ZARF("بَعْدَ", "bada", *ZAMAN),
  MI("مَوْتِ", "mawt", MUDAF, extra=["idafa-definiteness", "masdar"]),
  MI("عَبْدِ", "abd", MUDAF, extra=["idafa-definiteness"]),
  ALLAH_MI(punct=".")]})

CHAPS = [S1, S2, S3, S4, S5, S6]
# tidy the grammar anchors: no tag twice on a token, and a derived (mazīd) verb does not carry the Form-I bāb tag that the
# kit's MADI helper adds by default (اجْتَمَعَ is Form VIII).
for _S in CHAPS:
    for _s in _S:
        for _t in _s["tokens"]:
            _g = list(dict.fromkeys(_t.get("grammar", [])))
            if any(re.fullmatch(r"form-[ivx]+-verbs", x) for x in _g): _g = [x for x in _g if x != "thulathi-mujarrad-babs"]
            _t["grammar"] = _g

# ---- the text check: every chapter against the saved source, letter by letter --------------------------------------------
_AR = re.compile("[ء-ي]")
_MARK = "ًٌٍَُِّْٰ"
def _src_words(ch):
    txt = (ROOT / "research/sources/siyar-ibn-al-mubarak-src.txt").read_text(encoding="utf-8")
    parts = re.split(r"^# https://\S+ — .*\[chapter (\d)\]\s*$", txt, flags=re.M)
    words = []
    for n, body in zip(parts[1::2], parts[2::2]):
        if int(n) != ch: continue
        body = re.sub(r"\([٠-٩]+\)|\(ع\)|ـ", " ", body.replace("[…]", " "))
        for w in body.split():
            w = unicodedata.normalize("NFC", re.sub(r"[^ء-ي" + _MARK + "]", "", w))
            if _AR.search(w): words.append(w)
    return words
def _split(w):
    out = []
    for c in w:
        if c in _MARK and out: out[-1][1] += c
        else: out.append([c, ""])
    return [(a, "".join(sorted(b))) for a, b in out]
def _layers():
    """returns (mismatches, editorial): a mismatch is a letter whose EDITION vowel the package changed (it must be a declared
    normalisation or the declared correction); editorial is the list of words where a bare letter of the edition got a vowel"""
    bad, ours = [], []
    for ci, S in enumerate(CHAPS, 1):
        src = _src_words(ci); mine = [t["surface"]["full"] for s in S for t in s["tokens"]]
        assert len(src) == len(mine), ("word count", ci, len(src), len(mine), [(a, b) for a, b in zip(src, mine) if bare(a) != bare(b)][:3])
        for a, b in zip(src, mine):
            A, B = _split(a), _split(unicodedata.normalize("NFC", b))
            assert [x[0] for x in A] == [x[0] for x in B], ("letters differ", ci, a, b)
            ed = []
            for i, ((la, ma), (lb, mb)) in enumerate(zip(A, B)):
                if ma == mb: continue
                nxt = A[i + 1][0] if i + 1 < len(A) else ""
                if la == "ا" and ma in ("َ", "ً", "َّ") and mb == "": continue                     # لاَ → لَا ، حَدِيْثاً → حَدِيثًا
                if nxt == "ا" and A[i + 1][1] in ("َ", "ً", "َّ") and "".join(sorted(ma + A[i + 1][1])) == mb: continue
                if la in "وي" and ma == "ْ" and mb == "" and i > 0 and ("ُ" in B[i - 1][1] or "ِ" in B[i - 1][1]): continue   # no sukūn on a madd letter
                if ma == "َ" and mb == "ٰ": continue                                              # the dagger alif
                if bare(a) == "الله" or bare(a) == "لله": continue                                 # the Name in the shelf's spelling
                if ma == "" and la == "ل" and i >= 1 and A[i - 1][0] == "ا" and mb == "ْ": continue   # الْ
                if ma == "" and la == "ب" and bare(a) == "بن" and mb == "ْ": continue                # بْن
                if ma == "": ed.append((lb, mb)); continue
                bad.append((ci, a, b, la, ma, mb))
            if ed: ours.append((ci, b, ed))
    return bad, ours

# the ONE correction, and the editorial layer exactly as the manifest attribution lists it — a change in a chapter that moves
# either list stops the script here, so the attribution cannot drift from the text
_bad, _ours = _layers()
assert _bad == [(1, "خُوَارِزْميَّةٌ", "خُوَارِزْمِيَّةً", "ة", "ٌ", "ً")], _bad
EDITORIAL = {  # word → the letters the edition leaves bare and the package vowels
 "السِّجْنِ": "جْ", "وَالْإِنْفَاقِ": "نْ", "وَتَجْهِيزِهِمْ": "جْ مْ", "وَارْتَفَعَتِ": "رْ", "فَأَشْرَفَتْ": "شْ", "يَكْتَرِي": "كْ", "يُنْفِقُ": "نْ", "وَيُطْعِمُهُمْ": "طْ مْ",
 "الْحَلْوَى": "لْ", "وَأَكْمَلِ": "كْ", "تَشْتَرِيَ": "شْ", "الِاخْتِلَافِ": "لِ خْ", "مُسْتَعْجِلًا": "عْ", "خَلَصْتَ": "لَ صْ", "أَدْرِ": "دْ",
 "مَوْلَاهُمْ": "مْ", "نَفَقَاتِكُمْ": "مْ", "نَفَقَاتِهِمْ": "مْ", "لَهُمْ": "مْ", "وَيُخْرِجُهُمْ": "مْ", "يُخْرِجُهُمْ": "مْ", "عَلَيْهِمْ": "مْ", "حَجَّهُمْ": "مْ", "مِنْهُمْ": "مْ",
 "بُيُوتَهُمْ": "مْ", "وَأَبْوَابَهُمْ": "مْ", "وَكَسَاهُمْ": "مْ",
 "خُوَارِزْمِيَّةً": "مِ", "وَمِائَةٍ": "مِ", "فَسَمِعَ": "سَ", "بَقَايَا": "بَ", "الْحَجِّ": "حَ", "مُرُوءَةٍ": "ءَ", "لِأَمِيرِ": "لِ"}
_seen = {}
for _ci, _w, _ed in _ours:
    _w = unicodedata.normalize("NFC", _w); _e = " ".join(l + m for l, m in _ed)
    if _w == "يُخْرِجُهُمْ" and _e == "جُ مْ": _e = "مْ"      # once (ch4 s4) the edition also leaves the jīm of يُخْرِجهُم bare
    _seen.setdefault(_w, set()).add(_e)
_decl = {unicodedata.normalize("NFC", k): {v} for k, v in EDITORIAL.items()}
assert _seen == _decl, ({k: v for k, v in _seen.items() if _decl.get(k) != v}, [k for k in _decl if k not in _seen])

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
def NX(lemma, en, tr, **kw): return {"lemma": lemma, "pos": "noun", "gloss": {"en": en, "tr": tr}, "level": 5, **kw}
def NV(lemma, root, form, en, tr): return {"lemma": lemma, "root": root, "pos": "verb", "form": form, "gloss": {"en": en, "tr": tr}, "level": 5}
NEW_GLOSS = {
 # the five keys below are also claimed, with the same lemma, by the staged sibling package «siyar-abi-hanifa» (same book)
 "mubarak-name": NM("الْمُبَارَك", "al-Mubārak — in the name of Ibn al-Mubārak: ʿAbd Allāh ibn al-Mubārak (d. 181 AH), the imam of Marw", "Mübârek — İbnü'l-Mübârek'in adında: Abdullah b. Mübârek (ö. 181), Merv'in imamı"),
 "rabi-name": NM("الرَّبِيع", "al-Rabīʿ — a man's name; here al-Rabīʿ ibn Anas al-Bakrī (d. c. 139 AH), a Successor of Basra who settled in Khurāsān", "Rebî' — erkek ismi; burada Basralı olup Horasan'a yerleşen tâbiî Rebî' b. Enes el-Bekrî (ö. y. 139)"),
 "anas": NM("أَنَس", "Anas — a man's name; here the father of al-Rabīʿ ibn Anas (the best-known bearer of the name is the Companion Anas ibn Mālik)", "Enes — erkek ismi; burada Rebî' b. Enes'in babası (ismin en meşhur sahibi sahâbî Enes b. Mâlik'tir)"),
 "muqri": NN("مُقْرِئ", "ق ر أ", "a teacher of Qurʾān recitation (ism fāʿil of أَقْرَأَ, Form IV)", "kıraat öğreten kimse, kıraat hocası (akrae'nin ism-i fâili, if'âl bâbı)"),
 "iyal": NN("عِيَال", "ع ي ل", "dependants — those whom a man feeds and keeps (plural of عَيِّل)", "iyâl — bir kimsenin geçimini üstlendiği kimseler (ayyil'in cem'i)"),
 # names and nisbas
 "wadih-name": NM("وَاضِح", "Wāḍiḥ — a man's name («clear»); here the grandfather of ʿAbd Allāh ibn al-Mubārak", "Vâzıh — erkek ismi («açık»); burada Abdullah b. Mübârek'in dedesi"),
 "hanzali": NX("حَنْظَلِيّ", "a Ḥanẓalī — of the Banū Ḥanẓala, a great clan of Tamīm (a nisba); here by clientage", "Hanzalî — Temîm'in büyük kollarından Hanzala oğullarına mensup (nisbet); burada velâ yoluyla"),
 "turki": NX("تُرْكِيّ", "a Turk, Turkish (the nisba of التُّرْك)", "Türk, Türkî (التُّرْك'e nisbet)"),
 "khurasani": NX("خُرَاسَانِيّ", "of Khurāsān, a Khurāsānī (the nisba of خُرَاسَان)", "Horasanlı (خُرَاسَان'a nisbet)"),
 "khwarizmi-nisba": NX("خُوَارِزْمِيّ", "Khwārazmian — of Khwārazm, the land on the lower Oxus (a nisba; the edition vowels the rāʾ with kasra)", "Hârizmli — Ceyhun'un aşağı havzasındaki Hârizm'e mensup (nisbet; baskı râ'yı kesre ile harekelemiştir)"),
 "missisi": NX("مَصِّيصِيّ", "of al-Maṣṣīṣa (Mopsuestia), a frontier town of the Syrian marches (a nisba; vowelled as the edition has it)", "Massîsalı — Şam sınır boyundaki Massîsa (Misis) şehrine mensup (nisbet; baskıdaki harekesiyle)"),
 "mudrik-name": NM("مُدْرِك", "Mudrik — a man's name; here in the name of the transmitter ʿUmar ibn Mudrik", "Müdrik — erkek ismi; burada râvî Ömer b. Müdrik'in adında"),
 "ashath": NM("أَشْعَث", "Ashʿath — a man's name on the pattern أَفْعَل («dishevelled»), a diptote; here Ashʿath ibn Shuʿba al-Maṣṣīṣī", "Eş'as — «ef'al» vezninde erkek ismi («saçı dağınık»), gayr-i munsarif; burada Eş'as b. Şu'be el-Massîsî"),
 "shuba": NM("شُعْبَة", "Shuʿba — a man's name with the feminine tāʾ (a diptote)", "Şu'be — tâ'lı erkek ismi (gayr-i munsarif)"),
 "raqqa-city": NM("الرَّقَّة", "al-Raqqa — the city on the Euphrates in al-Jazīra, a residence of Hārūn al-Rashīd", "Rakka — el-Cezîre'de Fırat kıyısındaki şehir; Hârûn Reşîd'in ikamet ettiği yerlerden"),
 "marw": NM("مَرْو", "Marw — the chief city of Khurāsān, Ibn al-Mubārak's home (a diptote in the edition's vowelling)", "Merv — Horasan'ın baş şehri, İbnü'l-Mübârek'in memleketi (baskının harekesine göre gayr-i munsarif)"),
 "khallal": NM("الْخَلَّال", "al-Khallāl «the vinegar-seller» — a byname on فَعَّال; here Abū Muḥammad al-Khallāl, a teacher of al-Khaṭīb al-Baghdādī", "Hallâl «sirke satıcısı» — «fa''âl» vezninde lakap; burada Hatîb el-Bağdâdî'nin hocası Ebû Muhammed el-Hallâl"),
 "dawraqi": NM("الدَّوْرَقِيّ", "al-Dawraqī — a nisba; here ʿAbd Allāh ibn Aḥmad al-Dawraqī, a ḥadīth transmitter of Baghdad", "Devrakî — nisbet; burada Bağdatlı hadis râvîsi Abdullah b. Ahmed ed-Devrakî"),
 "hasan-name": NM("الْحَسَن", "al-Ḥasan — a man's name («the good, the fair»)", "Hasan — erkek ismi («güzel, iyi»)"),
 "shaqiq-name": NM("شَقِيق", "Shaqīq — a man's name; here in the name of ʿAlī ibn al-Ḥasan ibn Shaqīq of Marw (d. 215 AH), a close student of Ibn al-Mubārak", "Şakîk — erkek ismi; burada İbnü'l-Mübârek'in yakın talebesi Mervli Ali b. Hasan b. Şakîk'in (ö. 215) adında"),
 "mundhir-name": NM("الْمُنْذِر", "al-Mundhir — a man's name («the warner»); here in the name of the transmitter Muḥammad ibn al-Mundhir", "Münzir — erkek ismi («uyaran»); burada râvî Muhammed b. Münzir'in adında"),
 "tarasus": NM("طَرَسُوس", "Ṭarasūs (Tarsus) — the frontier city of Cilicia, a base of the campaigns against Byzantium (a diptote)", "Tarsus — Kilikya'daki sınır şehri, Bizans'a karşı seferlerin üslerinden (gayr-i munsarif)"),
 # nouns
 "ghazi": NN("غَازٍ", "غ ز و", "one who goes out on campaign, a frontier-fighter (ism fāʿil of غَزَا; a manqūṣ: الْغَازِي; pl. غُزَاة)", "gazâya çıkan, gâzi (gazâ'nın ism-i fâili; menkûs: الْغَازِي; cem'i غُزَاة)"),
 "aqdam": NN("أَقْدَم", "ق د م", "older, earlier; the earliest (elative of قَدِيم; a diptote)", "daha eski, en eski (kadîm'in ism-i tafdîli; gayr-i munsarif)"),
 "mawlid": NN("مَوْلِد", "و ل د", "birth; the time or place of birth (from وُلِدَ)", "doğum; doğum zamanı veya yeri (vülide'den)"),
 "tarhal": NN("تَرْحَال", "ر ح ل", "much journeying (a masdar on تَفْعَال, the pattern of doing a thing much)", "çokça yolculuk (çokluk bildiren «tef'âl» vezninde masdar)"),
 "tatwaf": NN("تَطْوَاف", "ط و ف", "much going about, roaming (a masdar on تَفْعَال from طَافَ)", "çokça dolaşma (tâfe'den «tef'âl» vezninde masdar)"),
 "ghazw": NN("غَزْو", "غ ز و", "going out to fight the enemy, campaigning (masdar of غَزَا)", "düşmanla savaşmaya çıkma, gazâ (gazâ'nın masdarı)"),
 "infaq": NN("إِنْفَاق", "ن ف ق", "spending (masdar of أَنْفَقَ, Form IV)", "harcama, infak (enfeka'nın masdarı, if'âl bâbı)"),
 "ghabara": NN("غَبَرَة", "غ ب ر", "dust, a cloud of dust", "toz, toz bulutu"),
 "burj": NN("بُرْج", "ب ر ج", "a tower", "burç, kule", plural="بُرُوج"),
 "nafaqa": NN("نَفَقَة", "ن ف ق", "money for expenses; a traveller's provision-money", "harçlık, masraf için ayrılan para; yol harçlığı", plural="نَفَقَات"),
 "halwa": NN("حَلْوَى", "ح ل و", "sweets, anything made sweet (a noun ending in alif maqṣūra)", "tatlı, helva (maksûr isim)"),
 "walima": NN("وَلِيمَة", "و ل م", "a banquet, a feast given for guests", "ziyafet, velîme", plural="وَلَائِم"),
 "nafir": NN("نَفِير", "ن ف ر", "the call to arms; the body of men who go out to fight", "sefer çağrısı, nefîr; savaşa çıkan topluluk"),
 "mustajil": NN("مُسْتَعْجِل", "ع ج ل", "in haste, hurrying (ism fāʿil of اِسْتَعْجَلَ, Form X)", "acele eden (ista'cele'nin ism-i fâili, istif'âl bâbı)"),
 "mahbus": NN("مَحْبُوس", "ح ب س", "imprisoned, held (ism mafʿūl of حَبَسَ)", "hapsedilmiş, mahpus (habese'nin ism-i mef'ûlü)"),
 "gharim": NN("غَرِيم", "غ ر م", "a creditor; also a debtor — either party to a debt", "alacaklı; ayrıca borçlu — borcun iki tarafından her biri", plural="غُرَمَاء"),
 "marhala": NN("مَرْحَلَة", "ر ح ل", "a stage — a day's journey", "merhale, konak — bir günlük yol", plural="مَرَاحِل"),
 # verbs
 "tahayyala": NV("تَحَيَّلَ", "ح و ل", "V", "to use a stratagem, to contrive a way (Form V)", "çare aramak, bir yolunu bulmak (tefa''ul bâbı)"),
 "irtahala": NV("اِرْتَحَلَ", "ر ح ل", "VIII", "to set out, to travel away (Form VIII)", "yola çıkmak, göç etmek (iftiâl bâbı)"),
 "injafala": NV("اِنْجَفَلَ", "ج ف ل", "VII", "(of a crowd) to break away and rush off in a body (Form VII)", "(topluluk) hep birden hızla akın etmek (infiâl bâbı)"),
 "taqattaa": NV("تَقَطَّعَ", "ق ط ع", "V", "to be cut to pieces, to snap apart (Form V)", "parça parça olmak, kopmak (tefa''ul bâbı)"),
 "ashrafa": NV("أَشْرَفَ", "ش ر ف", "IV", "to look down from a height; to overlook (عَلَى) (Form IV)", "yüksekten bakmak; (alâ ile) bir yere yukarıdan bakmak (if'âl bâbı)"),
 "aqfala": NV("أَقْفَلَ", "ق ف ل", "IV", "to lock (Form IV)", "kilitlemek (if'âl bâbı)"),
 "iktara": NV("اِكْتَرَى", "ك ر ي", "VIII", "to hire (a mount, a house) (Form VIII, nāqiṣ)", "kiralamak (binek, ev) (iftiâl bâbı, nâkıs)"),
 "jassasa": NV("جَصَّصَ", "ج ص ص", "II", "to plaster with gypsum (Form II)", "kireçle, alçıyla sıvamak (tef'îl bâbı)"),
 "kasa": NV("كَسَا", "ك س و", "I", "to clothe (someone in something — two objects) (كَسَا يَكْسُو)", "giydirmek (iki mef'ûl alır) (كَسَا يَكْسُو)"),
 "istadalla": NV("اِسْتَدَلَّ", "د ل ل", "X", "to ask the way to (عَلَى); to seek a proof, to infer (Form X, doubled)", "(alâ ile) birinin yerini sormak; delil aramak, istidlâl etmek (istif'âl bâbı, muzaaf)"),
 "hallafa": NV("حَلَّفَ", "ح ل ف", "II", "to make (someone) swear (Form II)", "yemin ettirmek (tef'îl bâbı)"),
 "khalasa": NV("خَلَصَ", "خ ل ص", "I", "to get free, to come out safe (مِنْ); to be pure (خَلَصَ يَخْلُصُ)", "kurtulmak (min ile); saf olmak (خَلَصَ يَخْلُصُ)"),
}
# the gloss a reused key shows in THIS text: the lemma is the shelf's, the sense or the person is this entry's
GLOSS_HERE = {
 "alam-banner": ("a mountain, a landmark; a banner — and so an eminent man by whom others find their way (pl. أَعْلَام)", "dağ, işaret; sancak — buradan: kendisiyle yol bulunan meşhur kimse (cem'i أَعْلَام)"),
 "mawla": ("mawlā — a client (a freedman and his descendants, tied to a tribe by walāʾ); also a master, a protecting lord", "mevlâ — velâ bağıyla bir kabileye bağlı kimse (âzatlı ve onun soyu); ayrıca efendi, koruyucu"),
 "hafiz": ("a keeper, a guardian (ism fāʿil of حَفِظَ); among the ḥadīth scholars a ḥāfiẓ: a master with a vast store of ḥadīth by heart", "koruyan, muhafız (hafıza'nın ism-i fâili); muhaddislerde hâfız: pek çok hadisi ezberinde tutan âlim"),
 "tabi": ("a follower (ism fāʿil of تَبِعَ); التَّابِعُونَ: the Successors, the generation that met the Companions", "tâbi olan (tebia'nın ism-i fâili); التَّابِعُونَ: sahâbeye yetişen nesil, tâbiîn"),
 "taqi": ("God-fearing, pious (pl. أَتْقِيَاء)", "takvâ sahibi, müttakî (cem'i أَتْقِيَاء)"),
 "rashid": ("rightly guided, sensible; الرَّشِيد: the title of the caliph Hārūn (r. 170–193 AH)", "doğru yolu bulmuş, reşîd; الرَّشِيد: Halife Hârûn'un (hilâfeti 170–193) lakabı"),
 "harun": ("Hārūn — a foreign name, a diptote; here the ʿAbbāsid caliph Hārūn al-Rashīd (r. 170–193 AH) (elsewhere: the prophet Hārūn, brother of Mūsā)", "Hârûn — yabancı isim, gayr-i munsarif; burada Abbâsî halifesi Hârûn Reşîd (hilâfeti 170–193) (başka yerde: Hz. Mûsâ'nın kardeşi Hz. Hârûn)"),
 "khatib-preacher": ("a preacher, the one who gives the Friday sermon; here الْخَطِيب is Abū Bakr al-Khaṭīb al-Baghdādī (d. 463 AH), the author of the History of Baghdad", "hatip, cuma hutbesini okuyan; burada الْخَطِيب: «Târîhu Bağdâd» müellifi Ebû Bekir el-Hatîb el-Bağdâdî (ö. 463)"),
 "qasim": ("al-Qāsim — a man's name; here the transmitter al-Qāsim ibn ʿAbd al-Raḥmān", "Kâsım — erkek ismi; burada râvî Kâsım b. Abdurrahman"),
 "umar": ("ʿUmar — a diptote name; here the transmitters ʿUmar ibn Mudrik and ʿUmar ibn Ibrāhīm", "Ömer — gayr-i munsarif isim; burada râvîler Ömer b. Müdrik ve Ömer b. İbrâhîm"),
 "ibrahim": ("Ibrāhīm — a foreign name, a diptote; here the father of ʿUmar ibn Ibrāhīm (elsewhere: the prophet Ibrāhīm)", "İbrâhîm — yabancı isim, gayr-i munsarif; burada Ömer b. İbrâhîm'in babası (başka yerde: Hz. İbrâhîm)"),
 "ismail": ("Ismāʿīl — a foreign name, a diptote; here Ismāʿīl ibn Muḥammad the secretary and his grandfather (elsewhere: the prophet Ismāʿīl)", "İsmâîl — yabancı isim, gayr-i munsarif; burada kâtip İsmâîl b. Muhammed ve dedesi (başka yerde: Hz. İsmâîl)"),
 "ishaq": ("Isḥāq — a foreign name, a diptote; here the father of Yaʿqūb ibn Isḥāq (elsewhere: the prophet Isḥāq)", "İshâk — yabancı isim, gayr-i munsarif; burada Ya'kûb b. İshâk'ın babası (başka yerde: Hz. İshâk)"),
 "yaqub": ("Yaʿqūb — a foreign name, a diptote; here the transmitter Yaʿqūb ibn Isḥāq (elsewhere: the prophet Yaʿqūb; the qāḍī Abū Yūsuf Yaʿqūb)", "Ya'kûb — yabancı isim, gayr-i munsarif; burada râvî Ya'kûb b. İshâk (başka yerde: Hz. Ya'kûb; Kadı Ebû Yûsuf Ya'kûb)"),
 "isa": ("ʿĪsā — a foreign name ending in alif maqṣūra, a diptote; here the father of Muḥammad ibn ʿĪsā (elsewhere: the prophet ʿĪsā, peace be upon him)", "Îsâ — maksûr yabancı isim, gayr-i munsarif; burada Muhammed b. Îsâ'nın babası (başka yerde: Hz. Îsâ aleyhisselâm)"),
 "muhammad": ("Muḥammad — a man's name", "Muhammed — erkek ismi"),
 "ali": ("ʿAlī — a man's name; here ʿAlī ibn al-Ḥasan ibn Shaqīq of Marw (d. 215 AH)", "Ali — erkek ismi; burada Mervli Ali b. Hasan b. Şakîk (ö. 215)"),
 "shurta": ("the guard, the police; a guardsman (pl. شُرَط)", "zaptiye, şurta; zaptiye eri (cem'i شُرَط)"),
 "awn": ("help, aid; a helper, a henchman (pl. أَعْوَان)", "yardım; yardımcı, hizmetli (cem'i أَعْوَان)"),
 "nahw": ("direction, side; نَحْوَ: toward; نَحْوٌ مِنْ كَذَا: about, some", "yön, taraf; نَحْوَ: -e doğru; نَحْوٌ مِنْ كَذَا: … kadar, yaklaşık"),
 "akh": ("brother (one of the five nouns; pl. إِخْوَة and إِخْوَان)", "kardeş (esmâ-i hamseden; cem'i إِخْوَة ve إِخْوَان)"),
 "qada-verb": ("to decree, to judge; to carry out to the end (a rite, a need); to pay (a debt)", "hükmetmek; (bir ibadeti, bir ihtiyacı) yerine getirmek, eda etmek; (borcu) ödemek"),
 "dafaa": ("to push, to repel; دَفَعَ إِلَيْهِ: to hand over to", "itmek, savmak; دَفَعَ إِلَيْهِ: ona teslim etmek"),
 "daa": ("to call; to pray; دَعَا بِهِ: to call for a thing to be brought", "çağırmak; dua etmek; دَعَا بِهِ: bir şeyin getirilmesini istemek"),
 "nazala": ("to come down, to dismount; to alight at, to put up in (a place)", "inmek; (bir yere) konmak, konaklamak"),
 "ikhtalafa": ("to differ; اِخْتَلَفَ إِلَى: to go repeatedly to, to frequent (Form VIII)", "ihtilâf etmek; اِخْتَلَفَ إِلَى: bir yere tekrar tekrar gidip gelmek (iftiâl bâbı)"),
 "qama": ("to stand; قَامَ بِـ: to see to, to take charge of", "kalkmak, ayakta durmak; قَامَ بِـ: bir işi üstlenmek, görmek"),
 "sara": ("to become (a sister of كَانَ); as a complete verb, صَارَ إِلَى: to come to, to end at", "olmak (kâne'nin kardeşlerinden); tam fiil olarak صَارَ إِلَى: -e varmak, dönmek"),
 "wazana": ("to weigh; to weigh out (money in payment) (a mithāl: وَزَنَ يَزِنُ)", "tartmak; (ödeme olarak parayı) tartıp vermek (misâl: وَزَنَ يَزِنُ)"),
 "amila": ("to do, to make; to act, to work", "yapmak; amel etmek, çalışmak"),
 "madina": ("a city; الْمَدِينَة: Medina, the City of the Prophet ﷺ", "şehir; الْمَدِينَة: Medine, Hz. Peygamber'in ﷺ şehri"),
 "abd": ("a servant, a slave; in names, عَبْدُ اللهِ «the servant of God»", "kul, köle; isimlerde عَبْدُ اللهِ «Allah'ın kulu»"),
 "rajul": ("a man", "adam, erkek"),
 "shaykh": ("an old man; an elder, a teacher (shaykh)", "yaşlı adam; şeyh, hoca"),
 "umm": ("mother; أُمُّ وَلَدٍ: a slave woman who has borne her master a child", "anne; أُمُّ وَلَدٍ: efendisinden çocuk doğurmuş câriye, ümmüveled"),
 "atyab": ("better, finest, most pleasant (elative of طَيِّب)", "daha güzel, en güzel, en hoş (tayyib'in ism-i tafdîli)"),
 "ashara": ("ten (عَشَرَة before a masculine noun counted; in the compounds 11–19 its second part is عَشَرَ / عَشْرَةَ)", "on (sayılan müzekker olduğunda عَشَرَة; 11–19 mürekkeb sayılarında ikinci cüz عَشَرَ / عَشْرَةَ)"),
 "haddatha": ("to narrate (ḥadīth), to relate; to talk to (Form II)", "(hadis) rivayet etmek, nakletmek; konuşmak (tef'îl bâbı)"),
 "jaala": ("to make; to put, to set", "kılmak, yapmak; koymak"),
 "mumin": ("a believer (ism fāʿil of آمَنَ, Form IV); أَمِيرُ الْمُؤْمِنِينَ: the Commander of the Faithful, the caliph", "mü'min (âmene'nin ism-i fâili, if'âl bâbı); أَمِيرُ الْمُؤْمِنِينَ: müminlerin emîri, halife"),
 "turfa": ("a curiosity, a rare and choice thing brought as a gift (pl. طُرَف)", "nâdide, hoş şey; hediyelik (cem'i طُرَف)"),
 "kadha": ("such-and-such — a word that stands for a thing left unnamed; (elsewhere) likewise, so", "şöyle şöyle, şu şu — adı anılmayan şeyden kinâye; (başka yerde) böylece, aynı şekilde"),
 "ikhtilaf": ("going repeatedly to a place, frequenting it (masdar of اِخْتَلَفَ إِلَى, Form VIII); also: disagreement", "bir yere tekrar tekrar gidip gelme (ihtelefe ilâ'nın masdarı, iftiâl bâbı); ayrıca: ihtilâf, görüş ayrılığı"),
 "ahad": ("one (of several); after a negative: anyone", "biri; olumsuzdan sonra: hiç kimse"),
 "zala": ("(with مَا or لَا) to keep on, never to cease: مَا زَالَ / لَا يَزَالُ", "(mâ veya lâ ile) devam etmek, sürdürmek: مَا زَالَ / لَا يَزَالُ"),
 "baqiyya": ("what remains, the remainder; the last survivors of a group (pl. بَقَايَا)", "geri kalan, bakiye; bir topluluktan hayatta kalanlar (cem'i بَقَايَا)"),
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
assert not [k for k in NEW_GLOSS if k not in used], [k for k in NEW_GLOSS if k not in used]
assert not [k for k in GLOSS_HERE if k not in GLOSS], [k for k in GLOSS_HERE if k not in GLOSS]

MORPH = {"verbs": {}}
_NV = MORPH["verbs"]
_NV["tahayyala"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَيَّل", "تَحَيَّل", "تَحَيَّل", "تَحَيُّل", "مُتَحَيِّل", note="تَحَيَّلَ يَتَحَيَّلُ تَحَيُّلًا: طَلَبَ الْحِيلَةَ وَاحْتَالَ — وَالْيَاءُ فِيهِ مُنْقَلِبَةٌ عَنْ وَاوٍ (مِنَ الْحَوْلِ).")
_NV["irtahala"] = _sg.derived(_sg.B8, _sg.W8, "َ", "اِرْتَحَل", "رْتَحِل", "اِرْتَحِل", "اِرْتِحَال", "مُرْتَحِل")
_NV["injafala"] = _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْجَفَل", "نْجَفِل", "اِنْجَفِل", "اِنْجِفَال", "مُنْجَفِل", note="اِنْجَفَلَ الْقَوْمُ: أَسْرَعُوا مُنْدَفِعِينَ بِجَمَاعَتِهِمْ.")
_NV["taqattaa"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَقَطَّع", "تَقَطَّع", "تَقَطَّع", "تَقَطُّع", "مُتَقَطِّع")
_NV["ashrafa"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَشْرَف", "شْرِف", "أَشْرِف", "إِشْرَاف", "مُشْرِف", "مُشْرَف", "أُشْرِفَ", "يُشْرَفُ")
_NV["aqfala"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْفَل", "قْفِل", "أَقْفِل", "إِقْفَال", "مُقْفِل", "مُقْفَل", "أُقْفِلَ", "يُقْفَلُ")
_NV["iktara"] = _sg.derived_naqis(_sg.B8 + " — نَاقِصٌ", _sg.W8, "َ", "اِكْتَرَ", "كْتَر", "i", "اِكْتَر", "اِكْتِرَاء", "مُكْتَرٍ", "مُكْتَرًى", "اُكْتُرِيَ", "يُكْتَرَى",
                                    "اِكْتَرَى يَكْتَرِي: اسْتَأْجَرَ — نَاقِصٌ مِنَ الِافْتِعَالِ: تُقَدَّرُ الضَّمَّةُ عَلَى يَائِهِ.")
_NV["jassasa"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "جَصَّص", "جَصِّص", "جَصِّص", "تَجْصِيص", "مُجَصِّص", "مُجَصَّص", "جُصِّصَ", "يُجَصَّصُ")
_NV["hallafa"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "حَلَّف", "حَلِّف", "حَلِّف", "تَحْلِيف", "مُحَلِّف", "مُحَلَّف", "حُلِّفَ", "يُحَلَّفُ")
_NV["kasa"] = _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "كَسَ", "كْس", "u", "اُكْس", "كَسْو", "كَاسٍ", "مَكْسُوّ", "كُسِيَ", "يُكْسَى")
_NV["khalasa"] = _sg.sound1("nasara", "خَلَص", "خْلُص", "اُخْلُص", "خَلَاص", "خَالِص", note="خَلَصَ يَخْلُصُ خُلُوصًا وَخَلَاصًا مِنْ بَابِ نَصَرَ.")
# اِسْتَدَلَّ: the doubled Form X paradigm of the shelf's اِسْتَجَدَّ (ج د د), letter for letter, with ج → د and د → ل
_src_x = None
for _p in PKGS:
    if "istajadda" in _M[_p]: _src_x = _M[_p]["istajadda"]; break
assert _src_x and _src_x["mazi"][0] == unicodedata.normalize("NFC", "اِسْتَجَدَّ"), _src_x and _src_x["mazi"][0]
_tr = str.maketrans({"ج": "د", "د": "ل"})
_x = lambda v: [c.translate(_tr) for c in v] if isinstance(v, list) else v.translate(_tr)
_NV["istadalla"] = {**{k: _x(v) for k, v in _src_x.items() if k not in ("bab", "wazn", "note")}, "bab": _src_x["bab"], "wazn": _src_x["wazn"],
                    "note": "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسْتَدِلَّ؛ وَيُفَكُّ الْإِدْغَامُ مَعَ ضَمِيرِ الرَّفْعِ الْمُتَحَرِّكِ: اِسْتَدْلَلْتُ."}
assert _NV["istadalla"]["mazi"][0] == unicodedata.normalize("NFC", "اِسْتَدَلَّ") and _NV["istadalla"]["masdar"] == unicodedata.normalize("NFC", "اِسْتِدْلَال"), _NV["istadalla"]
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
 "title": {"ar": "مِنْ سِيرَةِ عَبْدِ اللهِ بْنِ الْمُبَارَكِ", "en": "From the Life of ʿAbd Allāh ibn al-Mubārak", "tr": "Abdullah b. Mübârek'in Hayatından"},
 "subtitle": {"ar": "أَخْبَارٌ مُخْتَارَةٌ مِنْ تَرْجَمَةِ عَبْدِ اللهِ بْنِ الْمُبَارَكِ فِي «سِيَرِ أَعْلَامِ النُّبَلَاءِ» لِلذَّهَبِيِّ — نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Selected reports from al-Dhahabī's entry on ʿAbd Allāh ibn al-Mubārak in Siyar Aʿlām al-Nubalāʾ — the received text, word for word",
              "tr": "Zehebî'nin Siyeru A'lâmi'n-Nübelâ'sındaki Abdullah b. Mübârek maddesinden seçilmiş haberler — metin lafzıyla aktarılmıştır"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "نَصٌّ مَنْقُولٌ بِلَفْظِهِ مِنْ تَرْجَمَةِ عَبْدِ اللهِ بْنِ الْمُبَارَكِ (رَقْم ١١٢) فِي «سِيَرِ أَعْلَامِ النُّبَلَاءِ» لِشَمْسِ الدِّينِ الذَّهَبِيِّ (ت ٧٤٨ هـ)، طَبْعَةِ مُؤَسَّسَةِ الرِّسَالَةِ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ١٠٩٠٦)، الْجُزْءِ الثَّامِنِ، ص ٣٧٨–٣٨٧. كُلُّ فَصْلٍ قِطْعَةٌ مُتَّصِلَةٌ وَاحِدَةٌ لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ: (١) ص ٣٧٨–٣٧٩ مِنْ عُنْوَانِ التَّرْجَمَةِ إِلَى «إِلَى الْحَجِّ»؛ (٢) ص ٣٨٤ خَبَرُ أَشْعَثَ بْنِ شُعْبَةَ؛ (٣) وَ(٤) ص ٣٨٥–٣٨٦ خَبَرُ الْخَطِيبِ فِي نَفَقَاتِ الْحُجَّاجِ بِإِسْنَادِهِ، وَهُمَا قِطْعَتَانِ مُتَتَالِيَتَانِ؛ (٥) وَ(٦) ص ٣٨٦–٣٨٧ خَبَرُ مُحَمَّدِ بْنِ عِيسَى فِي الشَّابِّ الْمَحْبُوسِ، وَهُمَا مُتَتَالِيَتَانِ. وَتُرِكَ مَا بَيْنَ الْقِطَعِ: سَرْدُ شُيُوخِهِ وَتَلَامِيذِهِ وَحَدِيثُ «الْمَاءُ مِنَ الْمَاءِ» وَأَخْبَارُ وَلَائِهِ وَمَوْلِدِهِ وَخَبَرَاهُ مَعَ حَمَّادِ بْنِ زَيْدٍ وَأَقْوَالُ الْأَئِمَّةِ فِيهِ (ص ٣٧٩–٣٨٤)؛ وَأَقْوَالُ الْأَوْزَاعِيِّ وَشُعْبَةَ وَإِسْمَاعِيلَ بْنِ عَيَّاشٍ وَخَبَرُ الصُّوفِيَّةِ فِي طَرِيقِ الْمَصِّيصَةِ (ص ٣٨٤–٣٨٥)؛ وَخَبَرُ خَادِمِهِ وَخَبَرُ الدَّيْنِ ذِي السَّبْعِ مِائَةِ دِرْهَمٍ (ص ٣٨٦)؛ وَبَاقِي التَّرْجَمَةِ مِنْ ص ٣٨٧ إِلَى آخِرِهَا، وَفِيهِ ثَنَاءُ الْأَئِمَّةِ وَأَقْوَالُهُ وَأَخْبَارُ غَزْوِهِ وَمَسَائِلُ الِاعْتِقَادِ. الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ كَمَا هُوَ وَوُحِّدَ رَسْمُهُ عَلَى رَسْمِ الْمَكْتَبَةِ (لَا سُكُونَ عَلَى حَرْفِ الْمَدِّ، وَالْفَتْحَةُ قَبْلَ الْأَلِفِ، وَتَنْوِينُ النَّصْبِ قَبْلَ أَلِفِهِ، وَسُكُونُ لَامِ «الْ» الْقَمَرِيَّةِ وَبَاءِ «بْن»، وَالْأَلِفُ الْخَنْجَرِيَّةُ فِي «هٰذَا» وَ«الرَّحْمٰنِ»، وَلَفْظُ الْجَلَالَةِ فِي الصَّلَاةِ عَلَى النَّبِيِّ بِرَسْمِ «اللهُ»)؛ وَمَا تَرَكَتْهُ الطَّبْعَةُ بِلَا شَكْلٍ ضَبَطْنَاهُ نَحْنُ، وَهُوَ: سُكُونُ حَرْفٍ فِي (السِّجْنِ، وَالْإِنْفَاقِ، وَتَجْهِيزِهِمْ، وَارْتَفَعَتِ، فَأَشْرَفَتْ، يَكْتَرِي، يُنْفِقُ، وَيُطْعِمُهُمْ، الْحَلْوَى، وَأَكْمَلِ، تَشْتَرِيَ، الِاخْتِلَافِ، مُسْتَعْجِلًا، خَلَصْتَ، أَدْرِ)، وَسُكُونُ مِيمِ الْجَمْعِ فِي (مَوْلَاهُمْ، وَتَجْهِيزِهِمْ، نَفَقَاتِكُمْ، نَفَقَاتِهِمْ، لَهُمْ، يُخْرِجُهُمْ، عَلَيْهِمْ، وَيُطْعِمُهُمْ، حَجَّهُمْ، مِنْهُمْ، بُيُوتَهُمْ، وَأَبْوَابَهُمْ، وَكَسَاهُمْ)، وَكَسْرَةُ الْمِيمِ فِي «خُوَارِزْمِيَّةً» وَ«مِائَةٍ»، وَفَتْحَةُ السِّينِ فِي «فَسَمِعَ» وَالْبَاءِ فِي «بَقَايَا» وَالْحَاءِ فِي «الْحَجِّ» (الْفَصْل ٣) وَالْهَمْزَةِ فِي «مُرُوءَةٍ» وَاللَّامِ فِي «خَلَصْتَ»، وَضَمَّةُ الْجِيمِ فِي «يُخْرِجُهُمْ» (الْفَصْل ٤، الْجُمْلَة ٤)، وَكَسْرَةُ اللَّامِ فِي «لِأَمِيرِ» وَلَامِ التَّعْرِيفِ فِي «الِاخْتِلَافِ». تَصْحِيحٌ وَاحِدٌ: «خُوَارِزْميَّةٌ» ← «خُوَارِزْمِيَّةً» (خَبَرُ كَانَ)، وَالشَّاهِدُ: ضَبْطُ الطَّبْعَةِ نَفْسِهَا فِي ص ٣٨١ «كَانَتْ أُمُّ عَبْدِ اللهِ بْنِ الْمُبَارَكِ خُوَارِزْمِيَّةً» وَ«الْبِدَايَةُ وَالنِّهَايَةُ» لِابْنِ كَثِيرٍ (ت التُّرْكِيّ ١٣/٦١٠) «وَكَانَتْ أُمُّهُ خَوَارِزْمِيَّةً». وَلَمْ تُغَيَّرْ كَلِمَةٌ غَيْرُهَا. وَأُبْقِيَ عَلَى مَا فِي الطَّبْعَةِ مَعَ التَّنْبِيهِ عَلَيْهِ فِي الْإِعْرَابِ: «لَا مُلْكَ هَارُونَ» بِفَتْحِ الْكَافِ (وَكَذَا فِي «الْبِدَايَةِ وَالنِّهَايَةِ» ١٣/٦١١)، وَ«عَشْرَةِ آلَافٍ» بِسُكُونِ الشِّينِ، وَ«ثَمَانِ عَشْرَةَ»، وَ«مَرْوَ» مَمْنُوعَةً مِنَ الصَّرْفِ، وَ«الْمَصِّيصِيُّ» بِفَتْحِ الْمِيمِ، وَ«فَقَالَ لِي: يَا فَتَى» وَ«قَالُوا» بَعْدَ اثْنَيْنِ وَ«فَقَالَ: مَحْبُوسٌ» كَمَا فِي الطَّبْعَتَيْنِ (الرِّسَالَةِ وَدَارِ الْحَدِيثِ). عَلَامَاتُ التَّرْقِيمِ لِلْمُحَقِّقِ: لَمْ نُثْبِتْ نُقْطَتَيْهِ بَعْدَ «مَوْلِدُهُ» وَ«لَقِيَهُ»، وَلَا رَقْمَ التَّرْجَمَةِ وَنَجْمَتَهَا وَأَرْقَامَ الْحَوَاشِي، وَجُعِلَتِ الشَّرْطَةُ «—»؛ وَرَمْزُ «(ع)» بَعْدَ الِاسْمِ فِي الْعُنْوَانِ أُبْقِيَ كَمَا هُوَ، وَمَعْنَاهُ أَنَّ أَصْحَابَ الْكُتُبِ السِّتَّةِ رَوَوْا لَهُ. تَقْسِيمُ الْجُمَلِ وَعَنَاوِينُ الْفُصُولِ وَالتَّرْجَمَةُ وَكُلُّ إِعْرَابٍ اجْتِهَادُ الْمُؤَلِّفِ، بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "The RECEIVED text, verbatim: four passages from the entry on ʿAbd Allāh ibn al-Mubārak (no. 112) in Siyar Aʿlām al-Nubalāʾ by Shams al-Dīn al-Dhahabī (d. 748 AH), in the Muʾassasat al-Risāla edition as al-Maktaba al-Shāmila carries it (book 10906), vol. 8, pp. 378–387, set in six chapters. Each chapter is ONE contiguous span with nothing taken out of its middle: (1) pp. 378–379, from the heading of the entry to «إِلَى الْحَجِّ»; (2) p. 384, Ashʿath ibn Shuʿba's report of al-Rashīd at al-Raqqa, with its isnād; (3) and (4) pp. 385–386, al-Khaṭīb's report of the pilgrims' provisions with its isnād, from «قَالَ الْخَطِيبُ» to «عَلَيْهَا اسْمُهُ» — two ADJACENT spans, cut after «وَأَطْيَبَ الْحَلْوَى»; (5) and (6) pp. 386–387, Muḥammad ibn ʿĪsā's report of the young man's debt with its isnād, from «قَالَ مُحَمَّدُ بْنُ الْمُنْذِرِ» to «بَعْدَ مَوْتِ عَبْدِ اللهِ» — two adjacent spans, cut after «مَا عَاشَ». LEFT OUT between the spans: pp. 379–384 — the lists of his teachers and students, the ḥadīth «الْمَاءُ مِنَ الْمَاءِ» with its isnād, where he travelled, the reports of his clientage, his parents and his birth-year, the black clothes of his childhood, his sitting at home, the two reports with Ḥammād ibn Zayd, the sneeze, and the first words of praise; pp. 384–385 — the words of al-Awzāʿī, Shuʿba and Ismāʿīl ibn ʿAyyāsh, and the Ṣūfīs and the basin on the road to al-Maṣṣīṣa; p. 386 — his servant's report of the last banquet and of the hundred thousand dirhams a year, and the debt of seven hundred dirhams with the letter to his steward; and the rest of the entry from p. 387 to its end — al-Fuḍayl's question about his trading, the imams' praise, his memory, his sayings, his fighting in disguise, the creed reports against the Jahmiyya, his wealth and his table. TWO VOWELLING LAYERS: the edition is vowelled, though not on every letter. Its vowels are kept and only normalised to the shelf's spelling (no sukūn on a madd letter, fatḥa before the alif, tanwīn fatḥ before its alif, sukūn on the lām of the qamarī article and on the bāʾ of «بْن», the dagger alif of «هٰذَا» and «الرَّحْمٰن», and the Name written «اللهُ» in the blessing on the Prophet). Where the edition leaves a letter bare the vowel is OURS: the sukūn of a consonant in السِّجْنِ، وَالْإِنْفَاقِ، وَتَجْهِيزِهِمْ، وَارْتَفَعَتِ، فَأَشْرَفَتْ، يَكْتَرِي، يُنْفِقُ (ch3)، وَيُطْعِمُهُمْ، الْحَلْوَى، وَأَكْمَلِ، تَشْتَرِيَ، الِاخْتِلَافِ، مُسْتَعْجِلًا، خَلَصْتَ، أَدْرِ; the sukūn of the plural mīm in مَوْلَاهُمْ، وَتَجْهِيزِهِمْ، نَفَقَاتِكُمْ، نَفَقَاتِهِمْ، لَهُمْ، يُخْرِجُهُمْ، عَلَيْهِمْ، وَيُطْعِمُهُمْ، حَجَّهُمْ، مِنْهُمْ، بُيُوتَهُمْ، وَأَبْوَابَهُمْ، وَكَسَاهُمْ; the kasra of the mīm in «خُوَارِزْمِيَّةً» and in «مِائَةٍ»; the fatḥa of the sīn in «فَسَمِعَ», of the bāʾ in «بَقَايَا», of the ḥāʾ in «الْحَجِّ» (ch3), of the hamza in «مُرُوءَةٍ» and of the lām in «خَلَصْتَ»; the ḍamma of the jīm in «يُخْرِجُهُمْ» (ch4 s4); the kasra of the lām in «لِأَمِيرِ» and of the article's lām in «الِاخْتِلَافِ». ONE CORRECTION against a witness: «خُوَارِزْميَّةٌ» → «خُوَارِزْمِيَّةً» (ch1 s3, the predicate of كَانَتْ, which the edition prints with a ḍamma); witnesses: the edition's own vowelling of the same statement at 8/381, «كَانَتْ أُمُّ عَبْدِ اللهِ بنِ المُبَارَكِ خُوَارِزمِيَّةً», and Ibn Kathīr, al-Bidāya wa-l-Nihāya (ed. al-Turkī) 13/610, «وَكَانَتْ أُمُّهُ خَوَارِزْمِيَّةً» (Shamela book 4445, page 8278). NO other word or vowel of the edition is changed. KEPT AS PRINTED and remarked on in the iʿrāb, for the scholar to rule on: «لَا مُلْكَ هَارُونَ» with fatḥa on the kāf (ch2 s5; al-Bidāya wa-l-Nihāya 13/611 has the same fatḥa in its own wording of the story; the line also gives the regular reading «لَا مُلْكُ»); «عَشْرَةِ آلَافٍ» / «عَشْرَةَ آلَافٍ» with a quiescent shīn (ch5 s5–s6; the usual form is عَشَرَة); «ثَمَانِ عَشْرَةَ» (ch1 s4); «مَرْوَ» as a diptote; «الْمَصِّيصِيُّ» with fatḥa on the mīm; «فَقَالَ لِي: يَا فَتَى» (ch6 s2, where the context calls for «لَهُ»), «قَالُوا» after two named shaykhs (ch3 s1) and «فَقَالَ: مَحْبُوسٌ» in the singular (ch5 s5) — these three stand so in both editions on Shamela, al-Risāla and Dār al-Ḥadīth (book 22669, 7/365 and 368–369); compared word for word, the Dār al-Ḥadīth text of our six spans differs from al-Risāla's — the layout of the heading apart — in one word only, «يُطْعِمُهُمْ» without the wāw (ch3 s6), where al-Risāla's «وَيُطْعِمُهُمْ» is kept. The punctuation is the editor's: his colon after the topics «مَوْلِدُهُ» and «فَأَقْدَمُ شَيْخٍ لَقِيَهُ» is not carried over, his hyphens are set as dashes, and the entry's serial number, the footnote star of the heading and the footnote marks are dropped; the siglum «(ع)» after the name in the heading is kept as it stands (set as punctuation, not as a word) — it marks a transmitter whose ḥadīth all Six Books carry. The edition's footnotes are not used. Sentence division: ch1 s2–s3, ch1 s6–s8, ch2 s2–s3, ch3 s2–s3, ch3 s5 – ch4 s2, ch4 s4–s6, ch5 s2–s5 and ch5 s6 – ch6 s2 are each ONE period of the edition, cut at a comma — once, between ch4 s1 and s2, after the blessing on the Prophet, where the edition has no comma — (the next sentence then opens with its conjunction, analysed as such); ch3 s4, ch4 s2, ch4 s3 and ch6 s4 each join two short periods of the edition (a question or a request with its answer). Chapter titles, translations and every iʿrāb line are the author's own analysis. reviewStatus: pending-scholarly-review.",
  "tr": "LAFZIYLA AKTARILAN metin: Şemsüddîn ez-Zehebî'nin (ö. 748) «Siyeru A'lâmi'n-Nübelâ» adlı eserindeki Abdullah b. Mübârek maddesinden (no. 112) dört pasaj; Müessesetü'r-Risâle baskısı, el-Mektebetü'ş-Şâmile'deki hâliyle (kitap 10906), c. 8, s. 378–387; altı bölüm hâlinde. Her bölüm, ortasından hiçbir şey çıkarılmamış TEK bir kesintisiz parçadır: (1) s. 378–379, madde başlığından «إِلَى الْحَجِّ»ya kadar; (2) s. 384, Eş'as b. Şu'be'nin isnadıyla Reşîd'in Rakka'ya gelişi haberi; (3) ve (4) s. 385–386, Hatîb'in isnadıyla hacıların harçlıkları haberi, «قَالَ الْخَطِيبُ»den «عَلَيْهَا اسْمُهُ»ya kadar — «وَأَطْيَبَ الْحَلْوَى»dan sonra bölünmüş, birbirini TAKİP EDEN iki parça; (5) ve (6) s. 386–387, Muhammed b. Îsâ'nın isnadıyla hapisteki gencin borcu haberi, «قَالَ مُحَمَّدُ بْنُ الْمُنْذِرِ»den «بَعْدَ مَوْتِ عَبْدِ اللهِ»ye kadar — «مَا عَاشَ»dan sonra bölünmüş, birbirini takip eden iki parça. Parçalar arasında BIRAKILANLAR: s. 379–384 — hocalarının ve talebelerinin listeleri, isnadıyla «الْمَاءُ مِنَ الْمَاءِ» hadisi, gittiği beldeler, velâsına, anne-babasına ve doğum yılına dair rivayetler, çocukluğundaki siyah elbise, evinde oturması, Hammâd b. Zeyd ile iki haberi, aksırma haberi ve ilk övgü sözleri; s. 384–385 — Evzâî, Şu'be ve İsmâîl b. Ayyâş'ın sözleri ile Massîsa yolunda sûfîler ve leğen haberi; s. 386 — hizmetçisinin son ziyafet ve yılda yüz bin dirhem haberi ile yedi yüz dirhemlik borç ve vekiline yazdığı mektup; s. 387'den maddenin sonuna kadar kalan kısım — Fudayl'ın ticaretine dair sorusu, imamların övgüleri, hâfızası, sözleri, tanınmadan savaşması, Cehmiyye'ye karşı itikad rivayetleri, serveti ve sofrası. İKİ HAREKE KATMANI: baskı harekelidir, fakat her harfte değil. Baskının harekeleri korunmuş, yalnızca kütüphanenin imlâsına göre birleştirilmiştir (med harfinde sükûn yok, fetha eliften önce, nasb tenvini elifinden önce, kamerî «الْ» lâmında ve «بْن» bâ'sında sükûn, «هٰذَا» ve «الرَّحْمٰن»de hançer elif, salavattaki lafza-i celâl «اللهُ» imlâsıyla). Baskının harekesiz bıraktığı harflerin harekesi BİZE aittir: السِّجْنِ، وَالْإِنْفَاقِ، وَتَجْهِيزِهِمْ، وَارْتَفَعَتِ، فَأَشْرَفَتْ، يَكْتَرِي، يُنْفِقُ (3. bölüm)، وَيُطْعِمُهُمْ، الْحَلْوَى، وَأَكْمَلِ، تَشْتَرِيَ، الِاخْتِلَافِ، مُسْتَعْجِلًا، خَلَصْتَ، أَدْرِ kelimelerinde bir harfin sükûnu; مَوْلَاهُمْ، وَتَجْهِيزِهِمْ، نَفَقَاتِكُمْ، نَفَقَاتِهِمْ، لَهُمْ، يُخْرِجُهُمْ، عَلَيْهِمْ، وَيُطْعِمُهُمْ، حَجَّهُمْ، مِنْهُمْ، بُيُوتَهُمْ، وَأَبْوَابَهُمْ، وَكَسَاهُمْ kelimelerinde cemi mîminin sükûnu; «خُوَارِزْمِيَّةً» ve «مِائَةٍ»deki mîmin kesresi; «فَسَمِعَ»deki sînin, «بَقَايَا»daki bâ'nın, «الْحَجِّ»deki (3. bölüm) hâ'nın, «مُرُوءَةٍ»deki hemzenin ve «خَلَصْتَ»deki lâmın fethası; «يُخْرِجُهُمْ»deki (4. bölüm, 4. cümle) cîmin dammesi; «لِأَمِيرِ»deki lâmın ve «الِاخْتِلَافِ»taki ta'rîf lâmının kesresi. Bir şâhide dayanan TEK TASHİH: «خُوَارِزْميَّةٌ» → «خُوَارِزْمِيَّةً» (1. bölüm 3. cümle; kânet'in haberi, baskıda damme ile basılmış); şâhitler: aynı baskının aynı ifadeyi 8/381'de harekeleyişi, «كَانَتْ أُمُّ عَبْدِ اللهِ بنِ المُبَارَكِ خُوَارِزمِيَّةً», ve İbn Kesîr, el-Bidâye ve'n-Nihâye (Türkî neşri) 13/610, «وَكَانَتْ أُمُّهُ خَوَارِزْمِيَّةً» (Şâmile kitap 4445, sayfa 8278). Baskının başka hiçbir kelimesi ve harekesi değiştirilmemiştir. BASILDIĞI GİBİ BIRAKILAN ve i'râbda işaret edilen, âlimin hükmüne bırakılmış yerler: kâfın fethasıyla «لَا مُلْكَ هَارُونَ» (2. bölüm 5. cümle; el-Bidâye ve'n-Nihâye 13/611'de de hikâyenin kendi lafzında aynı fetha vardır; i'râb satırı kıyâsî okuyuş olan «لَا مُلْكُ»yü de zikreder); şîni sâkin «عَشْرَةِ آلَافٍ» / «عَشْرَةَ آلَافٍ» (5. bölüm 5–6. cümleler; meşhur olan عَشَرَة'dir); «ثَمَانِ عَشْرَةَ» (1. bölüm 4. cümle); gayr-i munsarif olarak «مَرْوَ»; mîmin fethasıyla «الْمَصِّيصِيُّ»; «فَقَالَ لِي: يَا فَتَى» (6. bölüm 2. cümle; siyâk «لَهُ» gerektirir), adı geçen iki hocadan sonra «قَالُوا» (3. bölüm 1. cümle) ve müfred sîgasıyla «فَقَالَ: مَحْبُوسٌ» (5. bölüm 5. cümle) — bu üçü Şâmile'deki her iki baskıda, Risâle ve Dâru'l-Hadîs (kitap 22669, 7/365 ve 368–369) baskılarında böyledir; kelime kelime karşılaştırıldığında Dâru'l-Hadîs metni, altı parçamızda — başlığın dizilişi dışında — Risâle'den yalnız bir kelimede ayrılır: vâvsız «يُطْعِمُهُمْ» (3. bölüm 6. cümle); burada Risâle'nin «وَيُطْعِمُهُمْ»ü korunmuştur. Noktalama muhakkike aittir: «مَوْلِدُهُ» ve «فَأَقْدَمُ شَيْخٍ لَقِيَهُ» konularından sonraki iki nokta alınmamış, kısa çizgiler uzun çizgi yapılmış, maddenin sıra numarası, başlıktaki dipnot yıldızı ve dipnot işaretleri atılmıştır; başlıkta isimden sonraki «(ع)» remzi olduğu gibi bırakılmıştır (kelime olarak değil, noktalama olarak) — Kütüb-i Sitte'nin hepsinde hadisi bulunan râvîyi gösterir. Baskının dipnotları kullanılmamıştır. Cümle taksimi: 1. bölüm c. 2–3, 1. bölüm c. 6–8, 2. bölüm c. 2–3, 3. bölüm c. 2–3, 3. bölüm c. 5 – 4. bölüm c. 2, 4. bölüm c. 4–6, 5. bölüm c. 2–5 ve 5. bölüm c. 6 – 6. bölüm c. 2 baskıda birer tek cümledir; virgülde bölünmüştür — bir yerde, 4. bölüm c. 1 ile 2 arasında, baskıda virgül bulunmayan salavattan sonra — (sonraki cümle atıf harfiyle başlar ve öyle tahlil edilmiştir); 3. bölüm c. 4, 4. bölüm c. 2, 4. bölüm c. 3 ve 6. bölüm c. 4 ise baskının ikişer kısa cümlesini (soru veya istek ile cevabını) birleştirir. Bölüm başlıkları, çeviriler ve bütün i'râb satırları müellifin kendi tahlilidir; ilmî incelemeyi beklemektedir.",
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
