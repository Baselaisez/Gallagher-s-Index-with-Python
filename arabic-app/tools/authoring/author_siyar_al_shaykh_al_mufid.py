"""Author content/samples/siyar-al-shaykh-al-mufid — «تَرْجَمَةُ الشَّيْخِ الْمُفِيدِ», a RECEIVED text at Level 5 (Advanced).

RECEIVED TEXT, VERBATIM AND WHOLE: al-Dhahabī's entry no. 213, «الشَّيْخُ الْمُفِيدُ مُحَمَّدُ بْنُ مُحَمَّدِ بْنِ النُّعْمَانِ الْبَغْدَادِيُّ», in
«سِيَرُ أَعْلَامِ النُّبَلَاءِ» (the Muʾassasat al-Risāla edition as al-Maktaba al-Shāmila carries it, book 10906), vol. 17,
pp. 344–345 — from its heading to its last word, nothing left out. The three chapters are three ADJACENT spans, so the
package is one contiguous text:

  ch1  17/344       the heading; his titles, name and arts; Ibn Abī Ṭayy's account opens — to «وَالشِّعْرِ.»
  ch2  17/344       Ibn Abī Ṭayy's account: his debating, his worship, his memory, his teaching — to «كَثُرَ تَلَامِذَتُهُ.»
  ch3  17/344–345   ʿAḍud al-Dawla's visits, his appearance, age, works and death; al-Dhahabī's closing words

It is al-Dhahabī's own text, with his judgements as he wrote them; the package imports it and adds nothing to it.

THE TWO VOWELLING LAYERS. The edition is vowelled, though not on every letter. Its vowels are kept and normalised to the
shelf's spelling (no sukūn on a madd letter, fatḥa before the alif, tanwīn fatḥ before its alif, sukūn on the lām of the
qamarī article, the dagger alif of هٰذَا / ذٰلِكَ / لِلّٰهِ, بْنُ with its sukūn, the shadda of إِلَّا on its lām, NFC). Where the
edition leaves a letter bare the vowel is editorial (the list is in the manifest attribution). No word is changed, added
or dropped; the edition's colon after وَاسْمُهُ / وَيُعْرَفُ is not carried over, nor its brackets round the book title, and its
hyphens are set as dashes.

The verbatim page text lives in research/sources/siyar-al-shaykh-al-mufid-src.txt.  Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_siyar_al_shaykh_al_mufid.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "siyar-al-shaykh-al-mufid"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

PRON.update({"هِمُ": "pron-3mp", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُ": "pron-3ms", "هِ": "pron-3ms", "نَا": "pron-1p", "ي": "pron-1s"})
PRON_AR.update({"هِمُ": "هُمْ", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "نَا": "نَا", "ي": "الْيَاءُ"})

# ---- the clause seats and the standing notes (ar, en, tr) — the wording of author_siyar_abi_hanifa.py ------------------
Z = ("", "", "")
def cat(*ts): return tuple("".join(t[i] for t in ts) for i in range(3))
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
MAQUL_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekûlü'l-kavl olarak mahallen mansûb")
DROP = (" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ", " — it loses its tanwin because it is described by «ibn» annexed to a name", " — alem'e muzâf «ibn» ile vasıflandığı için tenvini düşmüştür")
DG = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
JM = lambda seat_ar, seat_en, seat_tr: ("، وَالْجَارُّ وَالْمَجْرُورُ " + seat_ar, "; the jarr phrase " + seat_en, "; câr-mecrûr " + seat_tr)
JM_KH_KANA = JM("مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ", "hangs on an omitted word that is the predicate of كَانَ", "kâne'nin mahzûf haberine müteallik")

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
def MBM(full, lex, n=Z, extra=None, punct=None, sign="بِالضَّمَّةِ"):
    """the mubtada that comes after its fronted khabar"""
    return tok(full, lex, "noun", ["mubtada-khabar", "taqdim-al-musnad"] + (extra or []), "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ " + sign + n[0] + ".",
        "The mubtada, placed after its khabar, in raf'" + n[1] + ".", "Haberinden sonra gelmiş mübtedâ, merfû" + n[2] + ".", punct=punct)
def KK(full, lex, n=Z, pos="noun", extra=None, punct=None, sign="بِالْفَتْحَةِ"): return KHK(full, lex, pos, extra, n[0], n[1], n[2], punct, None, sign)
def KKN(full, lex, nth, n=Z, extra=None, punct=None, sign="بِالْفَتْحَةِ"):
    """a second / third / fourth predicate of كَانَ"""
    o = {"2": ("ثَانٍ", "second", "ikinci"), "3": ("ثَالِثٌ", "third", "üçüncü"), "4": ("رَابِعٌ", "fourth", "dördüncü")}[nth]
    return tok(full, lex, "noun", ["kana-wa-akhawatuha"] + (extra or []), "خَبَرٌ " + o[0] + " لِكَانَ مَنْصُوبٌ " + sign + n[0] + ".",
        "A " + o[1] + " predicate of كَانَ, in nasb" + n[1] + ".", "Kâne'nin " + o[2] + " haberi, mansûb" + n[2] + ".", punct=punct)
CASE = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr", "mecrûr")}
def NA(full, lex, case, of=None, n=Z, pos="noun", extra=None, punct=None, nth=None, sign=None):
    """a na't: of = (ar, en, tr) names the noun it describes; nth = '2' / '3' for a second or third na't"""
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
AB_HEAD = {
 "mi": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", ["idafa-definiteness"]),
 "maful2": ("مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ", "The second object, in nasb", "İkinci mef'ûlün bih, mansûb", ["maful-bihi", "mafulayn"]),
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
def MINP(n=Z, punct=None): return PREP("مِنْ", "min", n[0], n[1], n[2], gloss_tr="«-den»", punct=punct)
def FIP(n=Z): return PREP("فِي", "fi", n[0], n[1], n[2], gloss_tr="«-de»")
def ALAP(n=Z): return PREP("عَلَى", "ala", n[0], n[1], n[2], gloss_tr="«üzerine»")
def W(full, lex, pos, grammar, rest_ar, rest_en, rest_tr, kind="atf", punct=None, stem_lex=None, extra_segs=None):
    """a token that opens with وَ: kind = atf | isti | hal"""
    k = {"atf": (WA_AR, "The waw conjoins; ", "«ve» + ", ["atf-nasaq"]),
         "isti": ("الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "The waw opens a new sentence; ", "Vâv isti'nâf içindir; ", ["anwa-al-waw"]),
         "hal": ("الْوَاوُ حَالِيَّةٌ، وَ", "The waw opens a hal clause; ", "Hâl vâvı; ", ["al-hal-jumla-wa-rabituha", "anwa-al-waw"])}[kind]
    return tok(full, lex, pos, grammar + k[3], k[0] + rest_ar, k[1] + rest_en, k[2] + rest_tr, punct=punct,
               segments=[seg("وَ", "wa", "conj")] + (extra_segs or [seg(full[2:], stem_lex or lex, pos)]))
def AT(full, lex, on, case="jarr", n=Z, pos="noun", extra=None, punct=None, sign=None):
    """a noun joined by وَ to a NAMED word: on = (ar, en, tr)"""
    c = CASE[case]
    return W(full, lex, pos, (extra or []), "مَعْطُوفٌ عَلَى «" + on[0] + "» " + (sign or c[0]) + n[0] + ".",
             "conjoined to «" + on[1] + "», in " + c[1] + n[1] + ".", "«" + on[2] + "» üzerine ma'tûf, " + c[2] + n[2] + ".", punct=punct)
def QILA(full, kind=None, n=Z, punct=":"):
    """قِيلَ — the passive of the hollow قَالَ; its deputy doer is the clause that is quoted after it"""
    ar = "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ جُمْلَةُ مَقُولِ الْقَوْلِ بَعْدَهُ فِي مَحَلِّ رَفْعٍ — وَأَصْلُهُ قُوِلَ: نُقِلَتْ كَسْرَةُ الْوَاوِ إِلَى الْقَافِ ثُمَّ قُلِبَتِ الْوَاوُ يَاءً" + n[0] + "."
    en = "قِيلَ is a past verb in the passive, built on fatha; its deputy doer is the quoted clause after it, in the seat of raf' — from قُوِلَ: the waw's kasra moved back onto the qaf and the waw turned into ya" + n[1] + "."
    tr = "قِيلَ fetha üzere mebnî meçhul mâzî; nâib-i fâili ardından gelen mekûlü'l-kavl cümlesidir, mahallen merfû — aslı قُوِلَ: vâvın kesresi kâfa nakledilmiş, vâv yâ'ya çevrilmiştir" + n[2] + "."
    g = ["naib-al-fail", "al-majhul-fil-kafiya", "hollow-verbs"]
    if kind: return W(full, "qala", "verb", g, ar, en, tr, kind=kind, punct=punct)
    return tok(full, "qala", "verb", g, ar, en, tr, punct=punct)
MASDAR = lambda v_ar, v_en, v_tr: (" — مَصْدَرُ " + v_ar, " — the masdar of " + v_en, " — " + v_tr + " fiilinin masdarı")
TAKSIR = lambda s_ar, s_en=None: (" — جَمْعُ " + s_ar, " — the plural of " + (s_en or s_ar), " — " + s_ar + " kelimesinin cem'i")
NISBA = lambda to_ar, to_en, to_tr: (" — اسْمٌ مَنْسُوبٌ إِلَى " + to_ar, " — a nisba to " + to_en, " — " + to_tr + " nisbet")
AL_KASRA = (" — وَجُرَّ بِالْكَسْرَةِ مَعَ أَنَّهُ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ لِدُخُولِ «الْ» عَلَيْهِ", " — a diptote pattern, yet it takes the kasra because it carries ال", " — müntehâ'l-cümû' vezninde olduğu hâlde «الْ» aldığı için kesre ile")
NUMAN = lambda punct=None: MI("النُّعْمَانِ", "numan", (" — عَلَمٌ عَلَى وَزْنِ فُعْلَانَ، وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ «الْ» عَلَيْهِ", " — a name on the pattern فُعْلَان; it takes the kasra because it carries ال", " — fu'lân vezninde alem; «الْ» aldığı için kesre ile"), "propn", punct=punct)
MUH_T = ("مُحَمَّدُ", "Muḥammad", "Muhammed")
def NAME_TAIL(punct=None):
    """…بْنُ مُحَمَّدِ بْنِ النُّعْمَانِ الْبَغْدَادِيُّ — the lineage after the first مُحَمَّدُ, as the heading and the opening both give it"""
    return [BN("raf", *MUH_T), MI("مُحَمَّدِ", "muhammad", DROP, "propn"), BN("jarr", "مُحَمَّدِ", "Muḥammad", "Muhammed"), NUMAN(),
            NA("الْبَغْدَادِيُّ", "baghdadi", "raf", MUH_T, NISBA("بَغْدَادَ", "Baghdad", "Bağdat'a"), extra=["ism-mansub"], punct=punct)]
MUFID_NAAT = lambda punct=None: NA("الْمُفِيدُ", "mufid", "raf", ("الشَّيْخُ", "the Shaykh", "Şeyh"),
    (" — اسْمُ فَاعِلٍ مِنْ أَفَادَ، وَهُوَ لَقَبُهُ الَّذِي اشْتَهَرَ بِهِ", " — the active participle of أَفَادَ «to give benefit»; «al-Shaykh al-Mufīd» is the title he is known by", " — efâde'nin ism-i fâili; «eş-Şeyhu'l-Müfîd» onun meşhur lakabıdır"), extra=["ism-fail", "form-iv-verbs"], punct=punct)

TITLES = [{"ar": "الشَّيْخُ الْمُفِيدُ", "en": "Al-Shaykh al-Mufīd", "tr": "Şeyh Müfîd"},
          {"ar": "مُنَاظَرَتُهُ وَتَعْلِيمُهُ", "en": "His Debating and His Teaching", "tr": "Münazarası ve Öğretimi"},
          {"ar": "صِفَتُهُ وَوَفَاتُهُ", "en": "His Appearance and His Death", "tr": "Şemâili ve Vefatı"}]

# ================================================ Chapter 1 — الشَّيْخُ الْمُفِيدُ (17/344) ================================================
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "The Shaykh al-Mufīd: Muḥammad ibn Muḥammad ibn al-Nuʿmān, the Baghdadi.",
  "tr": "Şeyh Müfîd: Muhammed b. Muhammed b. Nu'mân el-Bağdâdî."},
 "tokens": [
  tok("الشَّيْخُ", "shaykh", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"],
    "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هٰذِهِ تَرْجَمَةُ…، أَوْ: هُوَ، مَرْفُوعٌ بِالضَّمَّةِ — وَهٰذَا عُنْوَانُ التَّرْجَمَةِ فِي الْكِتَابِ.",
    "The predicate (khabar) of a dropped mubtada — «(this is) …» or «he is» — in raf' by the damma: this line is the heading of the entry in the book.",
    "Hazfedilmiş mübtedânın («bu, … tercemesidir» veya «o») haberi, damme ile merfû — bu satır, kitaptaki terceme (biyografi) maddesinin başlığıdır."),
  MUFID_NAAT(),
  tok("مُحَمَّدُ", "muhammad", "propn", ["badal", "atf-bayan", "al-badal-wa-aqsamuh-wa-atf-al-bayan"],
    "بَدَلٌ مِنَ «الشَّيْخُ» مَرْفُوعٌ بِالضَّمَّةِ، وَيَجُوزُ أَنْ يَكُونَ عَطْفَ بَيَانٍ — وَهُوَ اسْمُهُ بَعْدَ لَقَبِهِ؛ وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ.",
    "A badal of «the Shaykh», in raf' by the damma (it may also be read as an explanatory apposition, ʿaṭf bayān) — his given name, after his title; it loses its tanwin because it is described by «ibn» annexed to a name.",
    "«Şeyh»ten bedel, damme ile merfû (atf-ı beyân da olabilir) — lakabından sonra gelen ismidir; alem'e muzâf «ibn» ile vasıflandığı için tenvini düşmüştür.")]
  + NAME_TAIL()})

S1.append({"id": "s2", "translation": {
  "en": "The scholar of the Rāfiḍa, the author of the works, the Shaykh al-Mufīd;",
  "tr": "Râfıza'nın âlimi, eserlerin sahibi, Şeyh Müfîd;"},
 "tokens": [
  tok("عَالِمُ", "alim-scholar", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness", "ism-fail"],
    "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — هٰكَذَا تُفْتَتَحُ التَّرَاجِمُ بِأَوْصَافِ صَاحِبِهَا.",
    "The predicate (khabar) of a dropped mubtada — «he is» — in raf' by the damma, annexed: this is how a biographical entry opens, with the descriptions of its subject.",
    "Hazfedilmiş mübtedânın («o») haberi, damme ile merfû, muzâf — terceme (biyografi) maddeleri sahibinin vasıflarıyla böyle açılır."),
  MI("الرَّافِضَةِ", "rafida", (" — اسْمُ فَاعِلٍ مِنْ رَفَضَ، أُنِّثَ عَلَى إِرَادَةِ الْفِرْقَةِ؛ وَهُوَ الِاسْمُ الَّذِي يُطْلِقُهُ الذَّهَبِيُّ عَلَى الشِّيعَةِ الْإِمَامِيَّةِ", " — the active participle of رَفَضَ «to reject», in the feminine because a party (firqa) is meant; it is the name al-Dhahabī uses for the Imāmī Shīʿa", " — رَفَضَ «reddetmek» fiilinin ism-i fâili; «fırka» kastedildiği için müennestir; Zehebî'nin İmâmiyye Şîası için kullandığı addır"), extra=["ism-fail"], punct="،"),
  tok("صَاحِبُ", "sahib", "noun", ["mubtada-khabar", "idafa-definiteness"],
    "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A second predicate (khabar), in raf', annexed.", "İkinci haber, merfû, muzâf."),
  MI("التَّصَانِيفِ", "tasnif", cat(TAKSIR("تَصْنِيفٍ", "تَصْنِيف «a composed work»"), AL_KASRA), extra=["jam-taksir", "masdar"], punct="،"),
  tok("الشَّيْخُ", "shaykh", "noun", ["mubtada-khabar"],
    "خَبَرٌ ثَالِثٌ مَرْفُوعٌ بِالضَّمَّةِ.", "A third predicate (khabar), in raf'.", "Üçüncü haber, merfû."),
  MUFID_NAAT(punct="،")]})

S1.append({"id": "s3", "translation": {
  "en": "and his name is Muḥammad ibn Muḥammad ibn al-Nuʿmān, the Baghdadi, the Shīʿī; and he is known as Ibn al-Muʿallim.",
  "tr": "adı Muhammed b. Muhammed b. Nu'mân el-Bağdâdî eş-Şîî'dir; İbnü'l-Muallim diye tanınır."},
 "tokens": [
  W("وَاسْمُهُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"],
    "اسْمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْوَاوُ عَطَفَتْ جُمْلَةً عَلَى جُمْلَةٍ.",
    "«name» is the mubtada, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr — the waw joins this sentence to the one before it.",
    "«isim» mübtedâ, merfû, muzâf; bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr — vâv bu cümleyi önceki cümleye atfeder.",
    extra_segs=[seg("اسْمُ", "ism", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("مُحَمَّدُ", "muhammad", "propn", ["mubtada-khabar"],
    "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ.",
    "The predicate (khabar), in raf' — it loses its tanwin because it is described by «ibn» annexed to a name.",
    "Haber, merfû — alem'e muzâf «ibn» ile vasıflandığı için tenvini düşmüştür.")]
  + NAME_TAIL(punct="،") + [
  NA("الشِّيعِيُّ", "shii", "raf", None, NISBA("الشِّيعَةِ", "the Shīʿa", "Şîa'ya"), extra=["ism-mansub"], punct="،", nth="2"),
  W("وَيُعْرَفُ", "arafa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu"],
    "يُعْرَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ.",
    "«is known» is a present verb in the passive, in raf' by the damma; its deputy doer is a hidden pronoun «he» — its first letter takes damma and the letter before the last a fatha.",
    "«tanınır» meçhul muzâri, damme ile merfû; nâib-i fâili gizli zamir «o» — evveli mazmûm, âhirinden önceki harf meftûhtur."),
  BI_NOUN("بِابْنِ", "ibn", "ابْنِ", extra=["idafa-definiteness"],
    note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يُعْرَفُ»؛ وَثَبَتَتْ أَلِفُ «ابْن» لِأَنَّهُ لَيْسَ بَيْنَ عَلَمَيْنِ",
    note_en=", annexed — the jarr phrase attaches to «is known»; the alif of «ibn» is written here because it does not stand between two names",
    note_tr=", muzâf — câr-mecrûr «tanınır»a müteallik; «ibn» iki alem arasında olmadığı için elifi yazılır"),
  MI("الْمُعَلِّمِ", "muallim", (" — اسْمُ فَاعِلٍ مِنْ عَلَّمَ", " — the active participle of عَلَّمَ «to teach»: «the Teacher's son»", " — alleme'nin ism-i fâili: «Muallim'in oğlu»"), extra=["ism-fail", "form-ii-verbs"], punct=".")]})

S1.append({"id": "s4", "translation": {
  "en": "He was a man of arts, inquiries and kalām, and of iʿtizāl and letters.",
  "tr": "İlim dallarının, araştırmaların ve kelâmın, i'tizâlin ve edebin sahibiydi."},
 "tokens": [
  KANA_HID("كَانَ"),
  KK("صَاحِبَ", "sahib", MUDAF, extra=["idafa-definiteness"]),
  MI("فُنُونٍ", "fann", TAKSIR("فَنٍّ", "فَنّ «an art, a branch of learning»"), extra=["jam-taksir"]),
  AT("وَبُحُوثٍ", "bahth", ("فُنُونٍ", "arts", "ilim dalları"), n=TAKSIR("بَحْثٍ", "بَحْث «an inquiry»"), extra=["jam-taksir"]),
  AT("وَكَلَامٍ", "kalam", ("فُنُونٍ", "arts", "ilim dalları"), n=(" — أَيْ عِلْمِ الْكَلَامِ", " — that is, ʿilm al-kalām, the science of the articles of faith", " — yani ilm-i kelâm"), punct="،"),
  AT("وَاعْتِزَالٍ", "itizal", ("فُنُونٍ", "arts", "ilim dalları"), n=(" — مَصْدَرُ اعْتَزَلَ؛ أَيْ قَوْلٍ بِمَذْهَبِ الْمُعْتَزِلَةِ", " — the masdar of اعْتَزَلَ (Form VIII); that is, holding the doctrine of the Muʿtazila", " — i'tezele'nin masdarı (iftiâl bâbı); yani Mu'tezile mezhebini benimseme"), extra=["masdar", "form-viii-verbs"]),
  AT("وَأَدَبٍ", "adab", ("فُنُونٍ", "arts", "ilim dalları"), punct=".")]})

S1.append({"id": "s5", "translation": {
  "en": "Ibn Abī Ṭayy mentioned him in The History of the Imāmiyya, and wrote of him at length and in full,",
  "tr": "İbn Ebî Tay onu «Târîhu'l-İmâmiyye»de anmış, sözü uzatmış ve genişçe anlatmış,"},
 "tokens": [
  ENC_MADI("ذَكَرَهُ", "dhakara", "هُ", ["thulathi-mujarrad-babs"], note_ar=" مُقَدَّمٌ عَلَى الْفَاعِلِ", note_en=", placed before the doer", note_tr=" (fâilden önce gelmiştir)"),
  F("ابْنُ", "ibn", MUDAF, extra=["idafa-definiteness"]),
  AB("أَبِي", "mi"),
  MI("طَيٍّ", "tayy-name", (" — عَلَمٌ مُنْصَرِفٌ فَيُنَوَّنُ", " — a fully declined name, so it takes tanwin", " — munsarif alem; tenvin alır"), "propn"),
  FIP(JM("مُتَعَلِّقٌ بِـ«ذَكَرَ»", "attaches to «mentioned»", "«andı» fiiline müteallik")),
  J("تَارِيخِ", "tarikh", cat(MUDAF, (" — وَ«تَارِيخُ الْإِمَامِيَّةِ» اسْمُ كِتَابِهِ", " — «The History of the Imāmiyya» is the title of his book", " — «Târîhu'l-İmâmiyye» onun kitabının adıdır")), extra=["idafa-definiteness"]),
  MI("الْإِمَامِيَّةِ", "imamiyya", (" — اسْمٌ مَنْسُوبٌ إِلَى الْإِمَامِ، أُنِّثَ عَلَى إِرَادَةِ الْفِرْقَةِ", " — a nisba to الْإِمَام, in the feminine because a party is meant", " — «imam»a nisbet; «fırka» kastedildiği için müennestir"), extra=["ism-mansub"], punct="،"),
  MADI("فَأَطْنَبَ", "atnaba", ["form-iv-verbs"], hidden=True, note_ar=" — أَيْ أَطَالَ فِي ذِكْرِهِ وَوَصْفِهِ", note_en=" — «he went to great length» in describing him", note_tr=" — yani onu anlatırken sözü uzattı"),
  MADI("وَأَسْهَبَ", "ashaba", ["form-iv-verbs"], hidden=True, punct="،", note_ar=" — وَهُوَ بِمَعْنَى «أَطْنَبَ»: أَكْثَرَ الْكَلَامَ", note_en=" — close in sense to «أَطْنَبَ»: he spoke at great length", note_tr=" — «أَطْنَبَ» ile yakın anlamlı: sözü çok uzattı")]})

USUL_T = ("فُنُونِ الْعِلْمِ", "the branches of learning", "ilmin dalları")
S1.append({"id": "s6", "translation": {
  "en": "and said: He was without peer in all the branches of learning: the two uṣūl, fiqh, the reports, the knowledge of the transmitters, Qurʾān commentary, grammar and poetry.",
  "tr": "ve şöyle demiştir: İlmin bütün dallarında eşsizdi: iki usûl, fıkıh, ahbâr, ricâl bilgisi, tefsir, nahiv ve şiir."},
 "tokens": [
  QALA("وَقَالَ", hidden=True, punct=":"),
  KANA_HID("كَانَ", MAQUL_CL),
  KK("أَوْحَدَ", "awhad", (" بِلَا تَنْوِينٍ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ — أَيْ لَا نَظِيرَ لَهُ", ", with no tanwin: a description on the pattern أَفْعَل, barred from tanwin — «unique, without a peer»", "; ef'al vezninde vasıf olduğu için gayr-i munsarif, tenvinsiz — «eşsiz, benzersiz»"), extra=["mamnu-min-sarf"]),
  FIP(JM("مُتَعَلِّقٌ بِـ«أَوْحَدَ»", "attaches to «without peer»", "«eşsiz»e müteallik")),
  J("جَمِيعِ", "jami", MUDAF, extra=["idafa-definiteness"]),
  MI("فُنُونِ", "fann", cat(MUDAF, TAKSIR("فَنٍّ", "فَنّ")), extra=["jam-taksir"]),
  MI("الْعِلْمِ", "ilm", punct=":"),
  tok("الْأَصْلَيْنِ", "asl", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "al-muthanna"],
    "بَدَلٌ مِنْ «فُنُونِ الْعِلْمِ» — بَدَلُ مُفَصَّلٍ مِنْ مُجْمَلٍ — مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى؛ وَالْأَصْلَانِ: أُصُولُ الدِّينِ وَأُصُولُ الْفِقْهِ.",
    "A badal of «the branches of learning» — the detail after the sum — in jarr by the ya, because it is a dual; «the two uṣūl» are the foundations of the religion (uṣūl al-dīn) and the foundations of fiqh (uṣūl al-fiqh).",
    "«ilmin dalları»ndan bedel — mücmelden sonra gelen tafsil — tesniye olduğu için yâ ile mecrûr; «iki usûl»: usûlü'd-dîn ve usûlü'l-fıkıh.", punct="،"),
  AT("وَالْفِقْهِ", "fiqh", ("الْأَصْلَيْنِ", "the two uṣūl", "iki usûl"), punct="،"),
  AT("وَالْأَخْبَارِ", "khabar", ("الْأَصْلَيْنِ", "the two uṣūl", "iki usûl"), n=cat(TAKSIR("خَبَرٍ", "خَبَر"), (": الْأَحَادِيثُ وَالْآثَارُ الْمَرْوِيَّةُ", ": the transmitted reports and traditions", ": rivayet edilen hadis ve haberler")), extra=["jam-taksir"], punct="،"),
  AT("وَمَعْرِفَةِ", "marifa", ("الْأَصْلَيْنِ", "the two uṣūl", "iki usûl"), n=cat(MUDAF, MASDAR("عَرَفَ", "عَرَفَ", "arafe")), extra=["idafa-definiteness", "masdar"]),
  MI("الرِّجَالِ", "rajul", cat(TAKSIR("رَجُلٍ", "رَجُل"), ("؛ وَمَعْرِفَةُ الرِّجَالِ: الْعِلْمُ بِأَحْوَالِ رُوَاةِ الْأَخْبَارِ", "; «the knowledge of the men» is the science of the transmitters of reports and their standing", "; «ricâl bilgisi»: haberleri rivayet edenlerin hâllerini bilme ilmi")), extra=["jam-taksir"], punct="،"),
  AT("وَالتَّفْسِيرِ", "tafsir", ("الْأَصْلَيْنِ", "the two uṣūl", "iki usûl"), n=MASDAR("فَسَّرَ", "فَسَّرَ (Form II)", "fessere"), extra=["masdar"], punct="،"),
  AT("وَالنَّحْوِ", "nahw-grammar", ("الْأَصْلَيْنِ", "the two uṣūl", "iki usûl"), punct="،"),
  AT("وَالشِّعْرِ", "shir", ("الْأَصْلَيْنِ", "the two uṣūl", "iki usûl"), punct=".")]})

# ================================================ Chapter 2 — مُنَاظَرَتُهُ وَتَعْلِيمُهُ (17/344) ================================================
LAFZ = (" — وَالْإِضَافَةُ لَفْظِيَّةٌ: صِفَةٌ مُشَبَّهَةٌ أُضِيفَتْ إِلَى فَاعِلِهَا فِي الْمَعْنَى", " — a «verbal» idafa: the adjective is annexed to what is its doer in meaning", " — izâfet lafzîdir: sıfat-ı müşebbehe, mânâca fâiline muzâf olmuştur")
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "He used to debate the people of every creed, with the high standing he had in the Buwayhid state and the great rank he held with the caliphs;",
  "tr": "Büveyhî devletindeki azameti ve halifeler katındaki büyük rütbesiyle birlikte, her akidenin mensuplarıyla münazara ederdi;"},
 "tokens": [
  ISTI(KANA_HID("وَكَانَ")),
  MUDARI_KH("يُنَاظِرُ", "nazara-debate", ["form-iii-verbs"], note_ar="؛ وَبِنَاءُ الْمُفَاعَلَةِ لِلْمُشَارَكَةِ", note_en="; Form III shows an act done with another: «to debate with»", note_tr="; müfâale bâbı müşâreket içindir: «münazara etmek»"),
  O("أَهْلَ", "ahl", MUDAF, extra=["idafa-definiteness"]),
  MI("كُلِّ", "kull", MUDAF),
  MI("عَقِيدَةٍ", "aqida"),
  ZARF("مَعَ", "maa", "مَكَانٍ", "place", "Mekân", note_ar=" — لِلْمُصَاحَبَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «يُنَاظِرُ»", note_en=" — «with», for accompaniment; it hangs on an omitted hal of the doer of «debate»", note_tr=" — «ile birlikte», musâhabet için; «münazara eder» fiilinin fâilinden mahzûf hâle müteallik"),
  MI("الْعَظَمَةِ", "azama-grandeur"),
  FIP(JM("مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْعَظَمَةِ»", "hangs on an omitted hal of «the high standing»", "«azamet»ten mahzûf hâle müteallik")),
  J("الدَّوْلَةِ", "dawla"),
  NA("الْبُوَيْهِيَّةِ", "buwayhi", "jarr", ("الدَّوْلَةِ", "the state", "devlet"), NISBA("بَنِي بُوَيْهٍ", "the house of Buwayh", "Büveyhoğulları'na"), extra=["ism-mansub"], punct="،"),
  AT("وَالرُّتْبَةِ", "rutba", ("الْعَظَمَةِ", "the high standing", "azamet")),
  NA("الْجَسِيمَةِ", "jasim", "jarr", ("الرُّتْبَةِ", "the rank", "rütbe"), (" — صِفَةٌ مُشَبَّهَةٌ مِنْ جَسُمَ: الْعَظِيمَةُ", " — a ṣifa mushabbaha from جَسُمَ: «great, weighty»", " — cesume'den sıfat-ı müşebbehe: «büyük, muazzam»"), extra=["sifa-mushabbaha"]),
  ZARF("عِنْدَ", "inda", "مَكَانٍ", "place", "Mekân", note_ar=" — مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الرُّتْبَةِ»", note_en=" — «with, in the eyes of»; it hangs on an omitted hal of «the rank»", note_tr=" — «katında»; «rütbe»den mahzûf hâle müteallik"),
  MI("الْخُلَفَاءِ", "khalifa", cat(TAKSIR("خَلِيفَةٍ", "خَلِيفَة"), (" عَلَى فُعَلَاءَ، وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ «الْ» عَلَيْهِ", " on فُعَلَاء, a diptote pattern that takes the kasra here because it carries ال", "; fuʿalâ' vezninde, «الْ» aldığı için kesre ile")), extra=["jam-taksir"], punct="،")]})

S2.append({"id": "s2", "translation": {
  "en": "and he was strong of spirit, abundant in kindness, great in humility, much given to prayer and fasting, and wore coarse clothing;",
  "tr": "ruhu güçlü, iyiliği bol, huşûu büyük, namazı ve orucu çok biriydi; elbiselerin kabasını giyerdi;"},
 "tokens": [
  KANA_HID("وَكَانَ"),
  KK("قَوِيَّ", "qawi", cat(MUDAF, LAFZ), extra=["idafa-definiteness", "idafa-lafziyya", "sifa-mushabbaha"]),
  MI("النَّفْسِ", "nafs", punct="،"),
  KKN("كَثِيرَ", "kathir", "2", MUDAF, extra=["idafa-definiteness", "idafa-lafziyya", "sifa-mushabbaha"]),
  MI("الْبِرِّ", "birr", (" — الْإِحْسَانُ وَالصِّلَةُ", " — kindness and giving", " — iyilik ve ihsan"), punct="،"),
  KKN("عَظِيمَ", "azim", "3", MUDAF, extra=["idafa-definiteness", "idafa-lafziyya", "sifa-mushabbaha"]),
  MI("الْخُشُوعِ", "khushu", MASDAR("خَشَعَ", "خَشَعَ", "haşea"), extra=["masdar"], punct="،"),
  KKN("كَثِيرَ", "kathir", "4", MUDAF, extra=["idafa-definiteness", "idafa-lafziyya", "sifa-mushabbaha"]),
  MI("الصَّلَاةِ", "salat"),
  AT("وَالصَّوْمِ", "sawm", ("الصَّلَاةِ", "prayer", "namaz"), n=MASDAR("صَامَ", "صَامَ", "sâme"), extra=["masdar"], punct="،"),
  MUDARI_KH("يَلْبَسُ", "labisa", note_ar=" — خَبَرٌ خَامِسٌ جَاءَ جُمْلَةً بَعْدَ الْأَخْبَارِ الْمُفْرَدَةِ", note_en=" — a fifth predicate, this one a clause after the single-word ones", note_tr=" — müfred haberlerden sonra cümle olarak gelen beşinci haber"),
  O("الْخَشِنَ", "khashin", (" — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِلٍ", " — a ṣifa mushabbaha on فَعِل: «the coarse»", " — fa'il vezninde sıfat-ı müşebbehe: «kaba olan»"), extra=["sifa-mushabbaha"]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"],
    "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْخَشِنَ».",
    "A jarr letter that states the kind, voweled with fatha before the following ال — the jarr phrase hangs on an omitted hal of «the coarse».",
    "«-den» — cinsi beyan eden cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi — câr-mecrûr «kaba olan»dan mahzûf hâle müteallik."),
  J("الثِّيَابِ", "thawb", TAKSIR("ثَوْبٍ", "ثَوْب «a garment»"), extra=["jam-taksir"], punct="،")]})

S2.append({"id": "s3", "translation": {
  "en": "and he was constant in study and in teaching, and among the people with the surest memory.",
  "tr": "mütalaaya ve öğretmeye devam eden biriydi; insanların hâfızası en kuvvetli olanlarındandı."},
 "tokens": [
  KANA_HID("وَكَانَ"),
  KK("مُدِيمًا", "mudim", (" — اسْمُ فَاعِلٍ مِنْ أَدَامَ: الْمُوَاظِبُ عَلَى الشَّيْءِ", " — the active participle of أَدَامَ (Form IV): one who keeps a thing up", " — edâme'nin (if'âl bâbı) ism-i fâili: bir şeye devam eden"), extra=["ism-fail", "form-iv-verbs", "hollow-verbs"]),
  LI_AL("لِلْمُطَالَعَةِ", "mutalaa", "الْمُطَالَعَةِ", extra=["masdar", "shurut-amal-ism-al-fail"],
    note_ar=" — وَاللَّامُ لِتَقْوِيَةِ عَمَلِ اسْمِ الْفَاعِلِ «مُدِيمًا»، وَالْمَجْرُورُ مَفْعُولُهُ فِي الْمَعْنَى؛ وَالْمُطَالَعَةُ مَصْدَرُ طَالَعَ",
    note_en=" — the lam strengthens the government of the participle «constant in»: the noun is its object in meaning; الْمُطَالَعَة is the masdar of طَالَعَ (Form III), «to read closely»",
    note_tr=" — lâm, «devam eden» ism-i fâilinin amelini takviye eder; mecrûr mânâca onun mef'ûlüdür; الْمُطَالَعَة, tâlea'nın (müfâale) masdarıdır"),
  AT("وَالتَّعْلِيمِ", "talim", ("الْمُطَالَعَةِ", "study", "mütalaa"), n=MASDAR("عَلَّمَ", "عَلَّمَ (Form II)", "alleme"), extra=["masdar"], punct="،"),
  W("وَمِنْ", "min", "prep", ["huruf-jarr", "kana-wa-akhawatuha"],
    "مِنْ حَرْفُ جَرٍّ لِلتَّبْعِيضِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ مَعْطُوفٍ عَلَى خَبَرِ كَانَ «مُدِيمًا»، أَيْ: وَكَانَ مِنْ أَحْفَظِ النَّاسِ.",
    "مِنْ is a jarr letter of «some of» — the jarr phrase hangs on an omitted word conjoined to «constant», the predicate of كَانَ: «and he was among…».",
    "min: ba'ziyyet bildiren cer harfi — câr-mecrûr, kâne'nin haberi «devam eden»e ma'tûf mahzûfa müteallik: «…-lerdendi»."),
  J("أَحْفَظِ", "ahfaz", cat(MUDAF, (" — اسْمُ تَفْضِيلٍ مُضَافٌ إِلَى مَعْرِفَةٍ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ", " — an elative annexed to a definite noun: «the best of … at memorising»; it takes the kasra because it is annexed", " — ma'rifeye muzâf ism-i tafdîl; muzâf olduğu için kesre ile")), extra=["ism-tafdil", "idafa-definiteness"]),
  MI("النَّاسِ", "nas", punct=".")]})

S2.append({"id": "s4", "translation": {
  "en": "It was said: he left no book of the opponents but that he had learned it by heart, and by this he was able to untie the doubts those people raised;",
  "tr": "Denildi ki: Muhaliflerin hiçbir kitabını ezberlemeden bırakmamıştı; bu sayede o topluluğun şüphelerini çözmeye güç yetirdi;"},
 "tokens": [
  QILA("قِيلَ"),
  tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna", "al-bariz-al-muttasil"],
    "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — كُسِرَتْ هَمْزَتُهَا لِأَنَّهَا فِي أَوَّلِ الْجُمْلَةِ الْمَحْكِيَّةِ بِالْقَوْلِ — وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.",
    "إِنَّ is the particle of emphasis that puts its noun in nasb — its hamza takes kasra because it opens a clause quoted after «say»; the attached «he» is its noun, built on damma in the seat of nasb.",
    "İnne te'kîd ve nasb harfi — kavl'den sonra nakledilen cümlenin başında olduğu için hemzesi kesrelidir; bitişik «o» zamiri ismi, damme üzere mebnî, mahallen mansûb.",
    segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  MA_NAFIYA(),
  MADI("تَرَكَ", "taraka", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", note_en="; the clause fills the seat of raf' as the predicate of إِنَّ", note_tr="; cümle inne'nin haberi olarak mahallen merfû"),
  tok("لِلْمُخَالِفِينَ", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim", "ism-fail"],
    "اللَّامُ حَرْفُ جَرٍّ، وَالْمُخَالِفِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ فَاعِلٍ مِنْ خَالَفَ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنْ «كِتَابًا» تَقَدَّمَتْ عَلَيْهِ.",
    "The lam is a jarr letter; «the opponents» is in jarr by the ya, because it is a sound masculine plural — the active participle of خَالَفَ (Form III); the jarr phrase hangs on an omitted hal of «a book», placed before it.",
    "Lâm cer harfi; «muhalifler» cem-i müzekker sâlim olduğu için yâ ile mecrûr — hâlefe'nin (müfâale) ism-i fâili; câr-mecrûr «kitap»tan, onun önüne geçmiş mahzûf hâle müteallik.",
    segments=[seg("لِ", "li", "prep"), seg("الْمُخَالِفِينَ", "mukhalif", "noun")]),
  O("كِتَابًا", "kitab", (" — نَكِرَةٌ فِي سِيَاقِ النَّفْيِ فَتَعُمُّ", " — an indefinite noun under negation, so it takes in every book", " — nefiy siyâkında nekre olduğu için umum ifade eder")),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna", "qasr"],
    "أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ مِنْ أَعَمِّ الْأَحْوَالِ، فَمَا بَعْدَهَا حَالٌ.",
    "The particle of restriction, which governs nothing — the exception is «emptied» (mufarragh) out of every possible state, so what follows it is a hal.",
    "Amel etmeyen hasr edatı — istisnâ, bütün hâllerden müferrağdır; bu yüzden sonrası hâldir."),
  tok("وَحَفِظَهُ", "hafiza", "verb", ["al-hal-jumla-wa-rabituha", "anwa-al-waw", "al-bariz-al-muttasil", "maful-bihi", "thulathi-mujarrad-babs"],
    "الْوَاوُ حَالِيَّةٌ، وَحَفِظَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ؛ وَالْمَاضِي بَعْدَ «إِلَّا» يَقَعُ حَالًا بِلَا «قَدْ».",
    "The waw opens a hal clause; حَفِظَ is a past verb built on fatha, its doer a hidden «he», and the attached «it» is its object, in the seat of nasb — the clause is a hal, in the seat of nasb; after «إِلَّا» a past verb stands as a hal without «قَدْ».",
    "Hâl vâvı; حَفِظَ fetha üzere mebnî mâzî, fâili gizli zamir «o», bitişik «onu» zamiri mef'ûlün bih, mahallen mansûb — cümle hâl olarak mahallen mansûb; «إِلَّا»dan sonra mâzî, «قَدْ» olmadan hâl olur.",
    punct="،", segments=[seg("وَ", "wa", "conj"), seg("حَفِظَ", "hafiza", "verb"), seg("هُ", "pron-3ms", "pron")]),
  W("وَبِهٰذَا", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
    "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«قَدَرَ» مُقَدَّمٌ عَلَيْهِ؛ وَالْوَاوُ عَطَفَتْ جُمْلَةَ «قَدَرَ» عَلَى جُمْلَةِ «مَا تَرَكَ».",
    "the ba is a jarr letter of cause, and «this» is a demonstrative built on sukun, in the seat of jarr — the jarr phrase attaches to «he was able» and is placed before it; the waw joins the clause «he was able» to the clause «he left no…».",
    "bâ sebebiyet bildiren cer harfi; «bu» işaret ismi, sükûn üzere mebnî, mahallen mecrûr — câr-mecrûr «güç yetirdi» fiiline müteallik, ondan önce gelmiştir; vâv «güç yetirdi» cümlesini «bırakmadı» cümlesine atfeder.",
    extra_segs=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
  MADI("قَدَرَ", "qadara-able", hidden=True),
  ALAP(JM("مُتَعَلِّقٌ بِـ«قَدَرَ»", "attaches to «he was able»", "«güç yetirdi» fiiline müteallik")),
  J("حَلِّ", "hall-nathr", cat(MUDAF, (" — مَصْدَرُ حَلَّ الْعُقْدَةَ: فَكَّهَا؛ وَحَلُّ الشُّبْهَةِ: كَشْفُهَا وَالْجَوَابُ عَنْهَا", " — the masdar of حَلَّ «to untie (a knot)»; to «untie» a doubt is to clear it up and answer it", " — «(düğümü) çözmek» anlamındaki halle'nin masdarı; şüpheyi «çözmek»: onu açıklayıp cevaplamak")), extra=["idafa-definiteness", "masdar", "doubled-verbs"]),
  MI("شُبَهِ", "shubha", cat(MUDAF, TAKSIR("شُبْهَةٍ", "شُبْهَة «a doubt, a specious argument»")), extra=["jam-taksir"]),
  MI("الْقَوْمِ", "qawm", (" — أَيِ الْمُخَالِفِينَ", " — «those people», that is, the opponents", " — yani muhalifler"), punct="،")]})

S2.append({"id": "s5", "translation": {
  "en": "and he was among the keenest of people for teaching: he would go round the schools and the weavers' shops, look out for the quick-witted boy and hire him from his parents — he means: and so lead him astray —",
  "tr": "öğretmeye insanların en düşkün olanlarındandı: mekteplere ve dokumacı dükkânlarına uğrar, zeki çocuğu gözüne kestirir ve onu anne babasından ücretle tutardı — yani: böylece onu saptırırdı, demek istiyor —"},
 "tokens": [
  KANA_HID("وَكَانَ"),
  MINP(JM_KH_KANA),
  J("أَحْرَصِ", "ahras", cat(MUDAF, (" — اسْمُ تَفْضِيلٍ مُضَافٌ إِلَى مَعْرِفَةٍ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ", " — an elative annexed to a definite noun: «the keenest of…»; it takes the kasra because it is annexed", " — ma'rifeye muzâf ism-i tafdîl; muzâf olduğu için kesre ile")), extra=["ism-tafdil", "idafa-definiteness"]),
  MI("النَّاسِ", "nas"),
  ALAP(JM("مُتَعَلِّقٌ بِـ«أَحْرَصِ»", "attaches to «the keenest»", "«en düşkün»e müteallik")),
  J("التَّعْلِيمِ", "talim", MASDAR("عَلَّمَ", "عَلَّمَ (Form II)", "alleme"), extra=["masdar"], punct="،"),
  MUDARI_KH("يَدُورُ", "dara-turn", ["hollow-verbs"], note_ar=" — خَبَرٌ ثَانٍ بَعْدَ شِبْهِ الْجُمْلَةِ، يُبَيِّنُ حِرْصَهُ", note_en=" — a second predicate after the jarr phrase; it shows how keen he was", note_tr=" — şibh-i cümleden sonra gelen ikinci haber; düşkünlüğünü açıklar"),
  ALAP(JM("مُتَعَلِّقٌ بِـ«يَدُورُ»", "attaches to «he would go round»", "«dolaşır» fiiline müteallik")),
  J("الْمَكَاتِبِ", "maktab", cat((" — جَمْعُ مَكْتَبٍ: مَوْضِعُ تَعْلِيمِ الصِّبْيَانِ الْكِتَابَةَ", " — the plural of مَكْتَب: the place where boys are taught to write, a school", " — mekteb'in cem'i: çocuklara yazı öğretilen yer"), AL_KASRA), extra=["jam-taksir"]),
  AT("وَحَوَانِيتِ", "hanut", ("الْمَكَاتِبِ", "the schools", "mektepler"), n=cat(MUDAF, (" — جَمْعُ حَانُوتٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ", " — the plural of حَانُوت «a shop», on a diptote pattern; it takes the kasra because it is annexed", " — hânût'un («dükkân») müntehâ'l-cümû' veznindeki cem'i; muzâf olduğu için kesre ile")), extra=["jam-taksir", "idafa-definiteness"]),
  MI("الْحَاكَةِ", "haik", (" — جَمْعُ حَائِكٍ، وَأَصْلُهُ حَوَكَةٌ: قُلِبَتِ الْوَاوُ أَلِفًا لِتَحَرُّكِهَا وَانْفِتَاحِ مَا قَبْلَهَا", " — the plural of حَائِك «a weaver», from حَوَكَة: the waw, voweled after a fatha, turned into alif", " — hâik'in («dokumacı») cem'i; aslı حَوَكَة: harekeli vâv, öncesi meftûh olduğu için elife çevrilmiştir"), extra=["jam-taksir", "hollow-verbs"], punct="،"),
  MUDARI("فَيَتَلَمَّحُ", "talammaha", ["form-v-verbs"], note_ar=" — مَعْطُوفٌ عَلَى «يَدُورُ»، وَالْفَاءُ لِلتَّرْتِيبِ وَالتَّعْقِيبِ", note_en=" — conjoined to «he would go round»; the fa gives order and close succession", note_tr=" — «dolaşır» üzerine ma'tûf; fâ tertip ve ta'kîb içindir"),
  O("الصَّبِيَّ", "sabi-boy"),
  NA("الْفَطِنَ", "fatin-sharp", "nasb", ("الصَّبِيَّ", "the boy", "çocuk"), (" — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِلٍ مِنْ فَطِنَ", " — a ṣifa mushabbaha on فَعِل, from فَطِنَ: «quick-witted»", " — fatine'den fa'il vezninde sıfat-ı müşebbehe: «zeki, kavrayışlı»"), extra=["sifa-mushabbaha"], punct="،"),
  MUDARI("فَيَسْتَأْجِرُهُ", "istajara-hire", ["form-x-verbs"], enc="هُ", note_ar=" — مَعْطُوفٌ عَلَى «يَتَلَمَّحُ»", note_en=" — conjoined to «he would look out for»", note_tr=" — «gözüne kestirir» üzerine ma'tûf"),
  MINP(JM("مُتَعَلِّقٌ بِـ«يَسْتَأْجِرُ»", "attaches to «hire»", "«ücretle tutar» fiiline müteallik")),
  tok("أَبَوَيْهِ", "abawan", "noun", ["huruf-jarr", "al-muthanna", "idafa-definiteness", "al-bariz-al-muttasil"],
    "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْأَبَوَانِ: الْأَبُ وَالْأُمُّ، عَلَى التَّغْلِيبِ.",
    "In jarr after the letter, by the ya, because it is a dual — its nun drops in the idafa; annexed, and the attached «his» is the second term of the idafa, in the seat of jarr; «the two fathers» are the father and the mother, by taghlīb.",
    "Cer harfiyle mecrûr — tesniye olduğu için yâ ile; nûnu izâfetten dolayı düşmüştür; muzâf, bitişik «onun» zamiri muzâfun ileyh, mahallen mecrûr; «ebeveyn»: tağlîb yoluyla baba ve anne.",
    punct=" —", segments=[seg("أَبَوَيْ", "abawan", "noun"), seg("هِ", "pron-3ms", "pron")]),
  MUDARI("يَعْنِي", "ana-mean", ["jumla-mutarida"], naqis="ي",
    note_ar=" (ابْنُ أَبِي طَيٍّ) — وَالْجُمْلَةُ اعْتِرَاضِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ: كَلَامُ الذَّهَبِيِّ يُفَسِّرُ بِهِ قَوْلَ ابْنِ أَبِي طَيٍّ",
    note_en=" (Ibn Abī Ṭayy) — a parenthetical clause with no seat of its own: these are al-Dhahabī's words, glossing what Ibn Abī Ṭayy said",
    note_tr=" (İbn Ebî Tay) — cümle i'tirâziyyedir, i'râbdan mahalli yoktur: bu, Zehebî'nin İbn Ebî Tay'ın sözünü açıklayan sözüdür"),
  MUDARI("فَيُضِلُّهُ", "adalla", ["form-iv-verbs", "doubled-verbs"], enc="هُ", punct=" —",
    note_ar=" — تَعْطِفُهُ الْفَاءُ عَلَى «يَسْتَأْجِرُهُ» فِي الْكَلَامِ الْمُفَسَّرِ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَعْنِي»؛ وَالْفَاعِلُ لِلْمُفِيدِ وَالْهَاءُ لِلصَّبِيِّ",
    note_en=" — the fa joins it to «he would hire him» in the words being glossed, and the clause is the object of «he means», in the seat of nasb; the doer is al-Mufīd and «him» is the boy",
    note_tr=" — fâ, açıklanan sözdeki «onu ücretle tutar»a atfeder; cümle «demek istiyor» fiilinin mef'ûlü olarak mahallen mansûb; fâil Müfîd, «onu» zamiri çocuğa döner")]})

S2.append({"id": "s6", "translation": {
  "en": "he said: And by that his students became many.",
  "tr": "(İbn Ebî Tay) dedi ki: Bu sayede talebeleri çoğaldı."},
 "tokens": [
  MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=":",
    note_ar=" (ابْنُ أَبِي طَيٍّ)، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ — عَادَ الذَّهَبِيُّ إِلَى كَلَامِهِ بَعْدَ الِاعْتِرَاضِ",
    note_en=" (Ibn Abī Ṭayy); what is said is its object — al-Dhahabī returns to his words after the parenthesis",
    note_tr=" (İbn Ebî Tay); söylenen söz mef'ûlün bihtir — Zehebî, i'tirâzdan sonra onun sözüne döner"),
  W("وَبِذٰلِكَ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
    "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«كَثُرَ» مُقَدَّمٌ عَلَيْهِ؛ وَالْوَاوُ مِنَ الْكَلَامِ الْمَحْكِيِّ، تَعْطِفُ عَلَى مَا قَبْلَهَا فِيهِ.",
    "the ba is a jarr letter of cause, and «that» is a demonstrative built on sukun, in the seat of jarr (its lam marks distance, its kaf is the letter of address) — the jarr phrase attaches to «became many» and is placed before it; the waw belongs to the quoted words and joins them to what came before in them.",
    "bâ sebebiyet bildiren cer harfi; «o» işaret ismi, sükûn üzere mebnî, mahallen mecrûr (lâm uzaklık içindir, kâf hitap harfidir) — câr-mecrûr «çoğaldı» fiiline müteallik, ondan önce gelmiştir; vâv nakledilen söze aittir ve onu, o sözde öncesine atfeder.",
    extra_segs=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  MADI("كَثُرَ", "kathura", note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", note_en="; its doer follows — the clause is what is said, in the seat of nasb", note_tr="; fâili ardından gelir — cümle mekûlü'l-kavl olarak mahallen mansûb"),
  ENC_NOUN("تَلَامِذَتُهُ", "tilmidh", "هُ", "fail", extra=["jam-taksir"], punct=".", note_ar=" — جَمْعُ تِلْمِيذٍ", note_en=" — the plural of تِلْمِيذ «a student»", note_tr=" — tilmîz'in («talebe») cem'i")]})

# ================================================ Chapter 3 — صِفَتُهُ وَوَفَاتُهُ (17/344–345) ================================================
UQUD_Y = (" — مِنْ أَلْفَاظِ الْعُقُودِ", " by the ya — one of the tens, which decline like the sound masculine plural", " — ukûd lafızlarındandır; cem-i müzekker sâlime mülhak olduğu için yâ ile")
UQUD_W = (" — مِنْ أَلْفَاظِ الْعُقُودِ", " by the waw — one of the tens, which decline like the sound masculine plural", " — ukûd lafızlarındandır; cem-i müzekker sâlime mülhak olduğu için vâv ile")
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "And it was said: ʿAḍud al-Dawla would sometimes visit him, and say to him: «Intercede, and your intercession will be granted.»",
  "tr": "Şöyle de denildi: Adudüddevle zaman zaman onu ziyaret eder ve ona «Şefaat et, şefaatin kabul edilsin» derdi."},
 "tokens": [
  QILA("وَقِيلَ", kind="isti"),
  tok("رُبَّمَا", "rubba", "part", ["al-lam-wa-rubba-fil-kafiya", "anwa-ma"],
    "رُبَّ حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ، وَمَا كَافَّةٌ كَفَّتْهُ عَنِ الْعَمَلِ فَدَخَلَ عَلَى الْفِعْلِ — وَمَعْنَاهُ هُنَا: أَحْيَانًا.",
    "رُبَّ is a jarr letter (one «like the redundant»), and مَا is the «stopping» mā that keeps it from governing, so that it comes before a verb — here it means «at times».",
    "رُبَّ zâide benzeyen cer harfi; mâ onu amelden alıkoyan kâffe mâ'sıdır, böylece fiilin başına gelmiştir — burada anlamı: «zaman zaman».",
    segments=[seg("رُبَّ", "rubba", "part"), seg("مَا", "ma-kaffa", "part")]),
  ENC_MADI("زَارَهُ", "zara", "هُ", ["hollow-verbs", "thulathi-mujarrad-babs"], note_ar=" مُقَدَّمٌ عَلَى الْفَاعِلِ — وَالْجُمْلَةُ الْمَحْكِيَّةُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلِ «قِيلَ»", note_en=", placed before the doer — the quoted clause is the deputy doer of «it was said», in the seat of raf'", note_tr=" (fâilden önce gelmiştir) — nakledilen cümle «denildi» fiilinin nâib-i fâili olarak mahallen merfû"),
  F("عَضُدُ", "adud", cat(MUDAF, (" — وَ«عَضُدُ الدَّوْلَةِ» لَقَبُ الْمَلِكِ الْبُوَيْهِيِّ", " — «ʿAḍud al-Dawla», «the Arm of the Dynasty», is the title of the Buwayhid king", " — «Adudüddevle» («devletin pazusu») Büveyhî hükümdarının lakabıdır")), extra=["idafa-definiteness"]),
  MI("الدَّوْلَةِ", "dawla", punct="،"),
  MUDARI("وَيَقُولُ", "qala", ["hollow-verbs", "hikayat-al-hal", "maful-bihi"], punct=None,
    note_ar=" (عَضُدُ الدَّوْلَةِ)، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ — وَجَاءَ مُضَارِعًا بَعْدَ الْمَاضِي عَلَى حِكَايَةِ الْحَالِ الْمَاضِيَةِ",
    note_en=" (ʿAḍud al-Dawla); what is said is its object — a present after the past: the past scene is told as if it were before the eyes",
    note_tr=" (Adudüddevle); söylenen söz mef'ûlün bihtir — mâzîden sonra muzâri gelmesi hikâye-i hâl-i mâziye içindir"),
  LAHU2("لَهُ", "pron-3ms", " («ona»)", punct=":", note=JM("مُتَعَلِّقٌ بِـ«يَقُولُ»", "attaches to «say»", "«der» fiiline müteallik")),
  AMR("اشْفَعْ", "shafaa-verb", ["thulathi-mujarrad-babs"], **N3(MAQUL_CL)),
  tok("تُشَفَّعْ", "shaffaa", "verb", ["jawab-al-talab", "naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs", "nawasib-wa-jawazim-al-mudari", "al-iqtibas-wal-tadmin"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ لِأَنَّهُ جَوَابُ الطَّلَبِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — أَيْ تُقْبَلْ شَفَاعَتُكَ؛ وَاللَّفْظُ مِنْ حَدِيثِ الشَّفَاعَةِ: «وَاشْفَعْ تُشَفَّعْ».",
    "A present verb in the passive, in jazm because it answers the command, its sign the sukun; its deputy doer is the hidden «you» — «your intercession will be accepted»; the wording is taken from the ḥadīth of the Intercession: «وَاشْفَعْ تُشَفَّعْ».",
    "Meçhul muzâri; talebin cevabı olduğu için meczûm, alâmeti sükûn; nâib-i fâili vücûben müstetir zamir «sen» — «şefaatin kabul edilir»; lafız şefaat hadisinden alınmıştır: «وَاشْفَعْ تُشَفَّعْ».", punct=".")]})

S3.append({"id": "s2", "translation": {
  "en": "He was of middle height, lean and brown-skinned; he lived seventy-six years, and he has more than two hundred works —",
  "tr": "Orta boylu, zayıf ve esmerdi; yetmiş altı yıl yaşadı; iki yüzden fazla eseri vardır —"},
 "tokens": [
  ISTI(KANA_HID("وَكَانَ")),
  KK("رَبْعَةً", "raba", (" — الرَّبْعَةُ: الْمُتَوَسِّطُ الْقَامَةِ، لَا طَوِيلٌ وَلَا قَصِيرٌ؛ يُوصَفُ بِهِ الْمُذَكَّرُ وَالْمُؤَنَّثُ", " — رَبْعَة: of middle height, neither tall nor short; the word is used alike of a man and of a woman", " — رَبْعَة: orta boylu, ne uzun ne kısa; erkek ve kadın için aynı lafız kullanılır")),
  KKN("نَحِيفًا", "nahif", "2", (" — صِفَةٌ مُشَبَّهَةٌ: الْقَلِيلُ اللَّحْمِ", " — a ṣifa mushabbaha: «lean»", " — sıfat-ı müşebbehe: «zayıf, ince yapılı»"), extra=["sifa-mushabbaha"]),
  KKN("أَسْمَرَ", "asmar", "3", (" بِلَا تَنْوِينٍ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ", ", with no tanwin: a description of colour on أَفْعَل, barred from tanwin", "; ef'al vezninde renk bildiren vasıf olduğu için gayr-i munsarif, tenvinsiz"), extra=["mamnu-min-sarf", "sifa-mushabbaha"], punct="،"),
  MADI("عَاشَ", "asha-live", ["hollow-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", note_en=" — a new sentence, with no conjunction", note_tr=" — cümle müste'nefedir"),
  tok("سِتًّا", "sitt", "noun", ["maful-fih", "asma-al-adad-fil-kafiya"],
    "نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ مَنْصُوبٌ بِالْفَتْحَةِ — عَدَدٌ مُمَيِّزُهُ اسْمُ زَمَانٍ؛ وَجَاءَ بِلَا تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَةً» مُؤَنَّثٌ.",
    "It stands in for an adverb of time, in nasb by the fatha — a number whose counted noun is a word of time; it has no ta because the counted noun «year» is feminine.",
    "Zaman zarfının nâibi, fetha ile mansûb — temyizi zaman ismi olan sayı; ma'dûd «sene» müennes olduğu için tâ'sız gelmiştir."),
  AT("وَسَبْعِينَ", "sabun", ("سِتًّا", "six", "altı"), case="nasb", n=UQUD_Y, extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"),
  tok("سَنَةً", "sana", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"],
    "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ الْمَعْدُودَ بَعْدَ الْعَدَدِ، وَتَمْيِيزُ الْعُقُودِ مُفْرَدٌ مَنْصُوبٌ.",
    "A specifier (tamyiz), in nasb — it names what the number counts; after the tens the counted noun is singular and in nasb.",
    "Temyîz, mansûb — sayının neyi saydığını bildirir; ukûddan sonra ma'dûd müfred ve mansûb gelir.", punct="،"),
  W("وَلَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
    "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ.",
    "the lam is a jarr letter and the attached «him» fills the seat of jarr — the jarr phrase hangs on an omitted word that is the FRONTED khabar.",
    "lâm cer harfi; bitişik «o» zamiri mahallen mecrûr — câr-mecrûr öne alınmış mahzûf habere müteallik.",
    extra_segs=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
  MBM("أَكْثَرُ", "akthar", (" بِلَا تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ", ", with no tanwin — an elative, barred from tanwin", "; tenvinsiz — gayr-i munsarif ism-i tafdîl"), extra=["ism-tafdil", "mamnu-min-sarf"]),
  MINP(JM("مُتَعَلِّقٌ بِـ«أَكْثَرُ»", "attaches to «more»: «more than…»", "«daha çok»a müteallik: «…-den fazla»")),
  J("مِائَتَيْ", "mia", (" — وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ؛ وَتُكْتَبُ «مِائَةٌ» بِأَلِفٍ لَا تُنْطَقُ", ", by the ya, because it is a dual — its nun drops in the idafa; annexed; the alif of مِائَة is written, not spoken (miʾa)", " — tesniye olduğu için yâ ile; nûnu izâfetten dolayı düşmüştür; muzâf; مِائَة'nin elifi yazılır, okunmaz"), extra=["al-muthanna", "idafa-definiteness", "asma-al-adad-fil-kafiya"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى"),
  MI("مُصَنَّفٍ", "musannaf", (" — تَمْيِيزُ الْمِائَةِ: مُفْرَدٌ مَجْرُورٌ بِالْإِضَافَةِ؛ وَهُوَ اسْمُ مَفْعُولٍ مِنْ صَنَّفَ: الْكِتَابُ الْمُؤَلَّفُ", " — the counted noun after «hundred»: singular, in jarr by the idafa; the passive participle of صَنَّفَ (Form II): «a composed work»", " — yüzün temyizi: müfred, izâfetle mecrûr; sannefe'nin ism-i mef'ûlü: «telif edilmiş eser»"), extra=["ism-maful", "form-ii-verbs", "tamyiz"], punct=" —")]})

S3.append({"id": "s3", "translation": {
  "en": "until he said: He died in the year four hundred and thirteen, and eighty thousand escorted his bier.",
  "tr": "nihayet şöyle dedi: Dört yüz on üç yılında öldü; cenazesini seksen bin kişi uğurladı."},
 "tokens": [
  tok("إِلَى", "ila", "prep", ["huruf-jarr", "hadhf-wa-taqdir"],
    "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ تَقْدِيرُهُ: وَسَاقَ كَلَامَهُ؛ وَهٰذِهِ عِبَارَةُ الذَّهَبِيِّ فِي اخْتِصَارِ مَا يَنْقُلُهُ.",
    "A jarr letter of «as far as» — the jarr phrase hangs on words left unsaid: «(and he went on with his account) until…»; this is al-Dhahabī's phrase for cutting short what he quotes.",
    "«-e kadar» — intihâ-i gâye bildiren cer harfi; câr-mecrûr mahzûfa müteallik: «(sözünü sürdürdü,) nihayet…»; bu, Zehebî'nin naklettiği sözü kısaltırken kullandığı ifadedir."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"],
    "حَرْفٌ مَصْدَرِيٌّ، دَخَلَ عَلَى الْمَاضِي فَلَا يَعْمَلُ فِي لَفْظِهِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ قَالَ» فِي مَحَلِّ جَرٍّ بِإِلَى، أَيْ: إِلَى قَوْلِهِ.",
    "The masdar-making أَنْ; before a past verb it changes nothing in the verb's form — the masdar it builds, «his saying», fills the seat of jarr after إِلَى.",
    "Masdariyye harfi en; mâzînin başına geldiği için lafzında amel etmez — «أَنْ قَالَ»den kurulan müevvel masdar («demesi») ilâ ile mahallen mecrûr."),
  MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=":", note_ar=" (ابْنُ أَبِي طَيٍّ)، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en=" (Ibn Abī Ṭayy); what is said is its object", note_tr=" (İbn Ebî Tay); söylenen söz mef'ûlün bihtir"),
  MADI("مَاتَ", "mata-die", ["hollow-verbs"], hidden=True, **N3(MAQUL_CL)),
  ZARF("سَنَةَ", "sana", "زَمَانٍ", "time", "Zaman"),
  tok("ثَلَاثَ", "thalath", "noun", ["asma-al-adad-fil-kafiya", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar", "idafa-definiteness"],
    "الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمُرَكَّبِ «ثَلَاثَ عَشْرَةَ» مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْمُرَكَّبُ كُلُّهُ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَجَاءَ بِلَا تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ.",
    "The first part of the compound number «thirteen», built on fatha; the whole compound is built on the fatha of both parts and fills the seat of jarr as the second term of the idafa — it has no ta because the counted noun «year» is feminine.",
    "«On üç» mürekkeb sayısının birinci cüz'ü, fetha üzere mebnî; mürekkebin tamamı iki cüz'ünün fethası üzere mebnîdir ve muzâfun ileyh olarak mahallen mecrûrdur — ma'dûd «sene» müennes olduğu için tâ'sız gelmiştir."),
  tok("عَشْرَةَ", "ashara", "noun", ["asma-al-adad-fil-kafiya", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"],
    "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ — وَجَاءَ بِالتَّاءِ مُوَافِقًا لِلْمَعْدُودِ الْمُؤَنَّثِ، وَتُسَكَّنُ شِينُهُ مَعَ التَّاءِ.",
    "The second part of the compound number, built on fatha — it carries the ta, agreeing with the feminine counted noun, and with the ta its shin is quiescent.",
    "Mürekkeb sayının ikinci cüz'ü, fetha üzere mebnî — müennes ma'dûda uyarak tâ'lı gelmiştir; tâ ile birlikte şîni sâkin olur."),
  W("وَأَرْبَعِ", "arba", "noun", ["asma-al-adad-fil-kafiya", "idafa-definiteness"],
    "أَرْبَعِ مَعْطُوفٌ عَلَى مَحَلِّ «ثَلَاثَ عَشْرَةَ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَجَاءَ بِلَا تَاءٍ لِأَنَّ مَعْدُودَهُ «مِائَةٍ» مُؤَنَّثٌ.",
    "«four» is conjoined to the seat of «thirteen», in jarr by the kasra, and annexed — it has no ta because what it counts, «hundred», is feminine.",
    "«dört», «on üç»ün mahalline ma'tûf, kesre ile mecrûr, muzâf — saydığı «yüz» müennes olduğu için tâ'sız gelmiştir."),
  MI("مِائَةٍ", "mia", (" — تَمْيِيزُ الْعَدَدِ، وَتُفْرَدُ الْمِائَةُ مَعَ الثَّلَاثِ إِلَى التِّسْعِ؛ وَتُكْتَبُ بِأَلِفٍ لَا تُنْطَقُ", " — the counted noun; «hundred» stays singular after three to nine; its alif is written, not spoken (miʾa)", " — sayının temyizi; «yüz» üçten dokuza kadar olan sayılarla müfred kalır; elifi yazılır, okunmaz"), extra=["asma-al-adad-fil-kafiya"], punct="،"),
  ENC_MADI("وَشَيَّعَهُ", "shayyaa", "هُ", ["form-ii-verbs"], note_ar=" مُقَدَّمٌ عَلَى الْفَاعِلِ — أَيْ خَرَجُوا مَعَ جَنَازَتِهِ", note_en=", placed before the doer — «escorted him», that is, walked with his bier", note_tr=" (fâilden önce gelmiştir) — yani cenazesiyle birlikte yürüdüler"),
  F("ثَمَانُونَ", "thamanun", UQUD_W, extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ"),
  tok("أَلْفًا", "alf", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"],
    "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ الْمَعْدُودَ بَعْدَ الْعَدَدِ، وَتَمْيِيزُ الْعُقُودِ مُفْرَدٌ مَنْصُوبٌ.",
    "A specifier (tamyiz), in nasb — it names what the number counts; after the tens the counted noun is singular and in nasb.",
    "Temyîz, mansûb — sayının neyi saydığını bildirir; ukûddan sonra ma'dûd müfred ve mansûb gelir.", punct=".")]})

S3.append({"id": "s4", "translation": {
  "en": "And it was said: his writings reached two hundred;",
  "tr": "Şöyle de denildi: Telifleri iki yüze ulaştı;"},
 "tokens": [
  QILA("وَقِيلَ", kind="isti"),
  MADI("بَلَغَتْ", "balagha", fem=True, note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ الْمَحْكِيَّةُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلِ «قِيلَ»", note_en="; its doer follows — the quoted clause is the deputy doer of «it was said», in the seat of raf'", note_tr="; fâili ardından gelir — nakledilen cümle «denildi» fiilinin nâib-i fâili olarak mahallen merfû"),
  ENC_NOUN("تَوَالِيفُهُ", "talif", "هُ", "fail", extra=["jam-taksir"], note_ar=" — جَمْعُ تَأْلِيفٍ، وَأَصْلُهُ تَآلِيفُ: خُفِّفَتْ هَمْزَتُهُ فَصَارَتْ وَاوًا", note_en=" — the plural of تَأْلِيف «a written work», for تَآلِيف: its hamza is lightened into a waw", note_tr=" — te'lîf'in cem'i; aslı تَآلِيف: hemzesi tahfif edilerek vâv olmuştur"),
  O("مِائَتَيْنِ", "mia", ("", ", by the ya, because it is a dual: «two hundred»", " — tesniye olduğu için yâ ile: «iki yüz»"), extra=["al-muthanna", "asma-al-adad-fil-kafiya"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", punct="،")]})

S3.append({"id": "s5", "translation": {
  "en": "I have not come upon any of them — and to God belongs the praise —",
  "tr": "ben onlardan hiçbirine vâkıf olmadım — hamd Allah'adır —"},
 "tokens": [
  tok("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"],
    "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ، وَهِيَ مِنْ كَلَامِ الذَّهَبِيِّ صَاحِبِ الْكِتَابِ.",
    "لَمْ negates the present, turns it to the past and governs jazm — a new sentence: these are the words of al-Dhahabī, the author of the book.",
    "Lem: nefiy, cezm ve kalb harfi — cümle müste'nefedir; kitabın müellifi Zehebî'nin kendi sözüdür."),
  JAZM_V("أَقِفْ", "waqafa", ["mithal-verbs", "al-fail-al-mudmar-al-mustatir-wujuban"], hidden="أَنَا",
    note_ar=" — مِثَالٌ وَاوِيٌّ حُذِفَتْ وَاوُهُ فِي الْمُضَارِعِ؛ وَوَقَفَ عَلَى الشَّيْءِ: اطَّلَعَ عَلَيْهِ",
    note_en=" — a verb whose first radical is waw, dropped in the present; وَقَفَ عَلَى الشَّيْءِ: «to come upon a thing, to get to see it»",
    note_tr=" — misâl-i vâvî: vâvı muzâride düşer; وَقَفَ عَلَى الشَّيْءِ: «bir şeye vâkıf olmak, onu görmek»"),
  ALAP(JM("مُتَعَلِّقٌ بِـ«أَقِفْ»", "attaches to «come upon»", "«vâkıf olmadım» fiiline müteallik")),
  J("شَيْءٍ", "shay"),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («onlardan»)", punct=" —",
    note_ar="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«شَيْءٍ»؛ وَالضَّمِيرُ لِتَوَالِيفِهِ",
    note_en="; the jarr phrase qualifies «anything», in the seat of jarr; «them» are his writings",
    note_tr="; câr-mecrûr «şey» için na't, mahallen mecrûr; zamir onun teliflerine döner"),
  tok("وَلِلّٰهِ", "allah", "propn", ["huruf-jarr", "mubtada-khabar", "taqdim-al-musnad", "jumla-mutarida", "anwa-al-waw"],
    "الْوَاوُ اعْتِرَاضِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ؛ وَالْجُمْلَةُ اعْتِرَاضِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The waw opens a parenthesis; the lam is a jarr letter and the Name of Majesty is in jarr by the kasra — the jarr phrase hangs on an omitted word that is the FRONTED khabar; the clause is parenthetical and has no seat of its own.",
    "Vâv i'tirâziyyedir; lâm cer harfi, lafza-i celâl kesre ile mecrûr — câr-mecrûr öne alınmış mahzûf habere müteallik; cümle i'tirâziyyedir, i'râbdan mahalli yoktur.",
    segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  MBM("الْحَمْدُ", "hamd", MASDAR("حَمِدَ", "حَمِدَ", "hamide"), extra=["masdar"], punct=" —،")]})

S3.append({"id": "s6", "translation": {
  "en": "He bears the kunya Abū ʿAbd Allāh.",
  "tr": "Künyesi Ebû Abdullah'tır."},
 "tokens": [
  tok("يُكْنَى", "kana-kunya", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "naqis-verbs", "mudari-marfu", "mafulayn"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَهُوَ الْمَفْعُولُ الْأَوَّلُ فِي الْأَصْلِ؛ يُقَالُ: كَنَاهُ أَبَا فُلَانٍ. وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
    "A present verb in the passive, in raf' by a damma estimated on the alif; its deputy doer is a hidden pronoun «he» — the first object of the active verb, as in كَنَاهُ أَبَا فُلَانٍ «he called him Abū So-and-so». A new sentence.",
    "Meçhul muzâri, elif üzerinde takdîrî damme ile merfû; nâib-i fâili gizli zamir «o» — aslında birinci mef'ûldür; كَنَاهُ أَبَا فُلَانٍ «ona Ebû Filân künyesini verdi» denir. Cümle müste'nefedir."),
  AB("أَبَا", "maful2", (" — وَهُوَ كُنْيَتُهُ", " — it is his kunya", " — bu onun künyesidir")),
  MI("عَبْدِ", "abd", MUDAF),
  ALLAH_MI(punct=".")]})

CHAPS = [S1, S2, S3]
# tidy the grammar anchors: no tag twice on a token, and a derived (mazīd) verb does not carry the Form-I bāb tag that the
# kit's MADI helper adds by default (أَطْنَبَ is Form IV).
for _S in CHAPS:
    for _s in _S:
        for _t in _s["tokens"]:
            _g = list(dict.fromkeys(_t.get("grammar", [])))
            if _t["pos"] == "verb" and any(re.fullmatch(r"form-[ivx]+-verbs", x) for x in _g): _g = [x for x in _g if x != "thulathi-mujarrad-babs"]
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
def NN(lemma, root, en, tr, **kw): return {"lemma": lemma, **({"root": root} if root else {}), "pos": "noun", "gloss": {"en": en, "tr": tr}, "level": 5, **kw}
def NV(lemma, root, form, en, tr): return {"lemma": lemma, "root": root, "pos": "verb", "form": form, "gloss": {"en": en, "tr": tr}, "level": 5}
NEW_GLOSS = {
 "rafida": NN("الرَّافِضَة", "ر ف ض", "the Rāfiḍa, «the Rejecters» (ism fāʿil of رَفَضَ «to reject, to leave», in the feminine for a party) — the name by which al-Dhahabī and other Sunni authors call the Imāmī Shīʿa", "Râfıza, «reddedenler» (رَفَضَ «reddetmek, terk etmek» fiilinin ism-i fâili; fırka kastıyla müennes) — Zehebî'nin ve diğer Sünnî müelliflerin İmâmiyye Şîasına verdiği ad"),
 "tasnif": NN("تَصْنِيف", "ص ن ف", "composing a book, setting knowledge out in kinds (masdar of صَنَّفَ, Form II); a composed work", "kitap telif etme, tasnif (sannefe'nin masdarı, tef'îl bâbı); telif edilmiş eser", plural="تَصَانِيف"),
 "shii": NN("شِيعِيّ", "ش ي ع", "a Shīʿī — one of the Shīʿa (a nisba to الشِّيعَة)", "Şiî — Şîa'ya mensup (الشِّيعَة'ya nisbet)"),
 "tayy-name": NM("طَيّ", "Ṭayy — a man's name (so vowelled in the edition); here in the name of Ibn Abī Ṭayy: Yaḥyā ibn Abī Ṭayy Ḥumayd al-Ḥalabī (d. c. 630 AH), the Imāmī historian of Aleppo", "Tay — erkek ismi (matbû nüshada böyle harekelenmiştir); burada İbn Ebî Tay'ın adında: Halepli İmâmî tarihçi Yahyâ b. Ebî Tay Humeyd (ö. y. 630)"),
 "imamiyya": NN("الْإِمَامِيَّة", "أ م م", "the Imāmiyya — the Imāmī (Twelver) Shīʿa: a nisba to الْإِمَام, in the feminine for a party", "İmâmiyye — İmâmî (İsnâaşerî) Şîa: الْإِمَام'a nisbet, fırka kastıyla müennes"),
 "atnaba": NV("أَطْنَبَ", "ط ن ب", "IV", "to go to great length in speech or description, to be lavish in it (Form IV)", "sözü veya vasfı uzatmak, uzun uzadıya anlatmak (if'âl bâbı)"),
 "awhad": NN("أَوْحَد", "و ح د", "unique, without a peer (on أَفْعَل; a diptote)", "eşsiz, benzersiz (ef'al vezninde; gayr-i munsarif)"),
 "nazara-debate": NV("نَاظَرَ", "ن ظ ر", "III", "to debate with, to dispute with (Form III)", "münazara etmek, tartışmak (müfâale bâbı)"),
 "buwayhi": NN("بُوَيْهِيّ", None, "Buwayhid — of the house of Buwayh (a nisba): the Daylamī dynasty that ruled Iraq and western Iran, 334–447 AH", "Büveyhî — Büveyh hanedanına mensup (nisbet): Irak ve Batı İran'a hükmeden Deylemli hanedan (h. 334–447)"),
 "jasim": NN("جَسِيم", "ج س م", "great, weighty, considerable (ṣifa mushabbaha of جَسُمَ)", "büyük, muazzam (cesume'den sıfat-ı müşebbehe)"),
 "mudim": NN("مُدِيم", "د و م", "keeping a thing up, constant in it (ism fāʿil of أَدَامَ, Form IV)", "bir şeyi sürdüren, ona devam eden (edâme'nin ism-i fâili, if'âl bâbı)"),
 "mutalaa": NN("مُطَالَعَة", "ط ل ع", "reading closely, the study of books (masdar of طَالَعَ, Form III)", "mütalaa, kitapları dikkatle okuma (tâlea'nın masdarı, müfâale bâbı)"),
 "ahfaz": NN("أَحْفَظ", "ح ف ظ", "better / best at memorising, with the surest memory (elative of حَافِظ; a diptote)", "daha / en hâfız, hâfızası en kuvvetli (hâfız'ın ism-i tafdîli; gayr-i munsarif)"),
 "shubha": NN("شُبْهَة", "ش ب ه", "a doubt, a specious argument — what looks like a proof and is not", "şüphe; delile benzeyen fakat delil olmayan itiraz", plural="شُبَه"),
 "hanut": NN("حَانُوت", "ح ن ت", "a shop, a stall", "dükkân", plural="حَوَانِيت"),
 "talammaha": NV("تَلَمَّحَ", "ل م ح", "V", "to look out for, to pick out with a searching glance (Form V)", "gözüyle aramak, bakışıyla seçmek (tefa''ul bâbı)"),
 "fatin-sharp": NN("فَطِن", "ف ط ن", "quick-witted, sharp (ṣifa mushabbaha on فَعِل, from فَطِنَ)", "zeki, kavrayışı hızlı (fatine'den, fa'il vezninde sıfat-ı müşebbehe)"),
 "adud": NN("عَضُد", "ع ض د", "the upper arm; a support, a helper — عَضُدُ الدَّوْلَةِ «the Arm of the Dynasty»: the title of the Buwayhid king Fannā Khusraw (d. 372 AH)", "pazu; destek, yardımcı — عَضُدُ الدَّوْلَةِ «devletin pazusu»: Büveyhî hükümdarı Fennâ Hüsrev'in (ö. 372) lakabı", plural="أَعْضَاد"),
 "shaffaa": NV("شَفَّعَ", "ش ف ع", "II", "to accept someone's intercession (Form II); passive شُفِّعَ: to have one's intercession accepted", "birinin şefaatini kabul etmek (tef'îl bâbı); meçhulü شُفِّعَ: şefaati kabul edilmek"),
 "raba": NN("رَبْعَة", "ر ب ع", "of middle height, neither tall nor short (said alike of a man and of a woman)", "orta boylu; ne uzun ne kısa (erkek ve kadın için aynı lafız)"),
 "nahif": NN("نَحِيف", "ن ح ف", "lean, slender (ṣifa mushabbaha)", "zayıf, ince yapılı (sıfat-ı müşebbehe)"),
 "musannaf": NN("مُصَنَّف", "ص ن ف", "a composed work, a book (ism mafʿūl of صَنَّفَ)", "telif edilmiş eser, kitap (sannefe'nin ism-i mef'ûlü)", plural="مُصَنَّفَات"),
 "kana-kunya": NV("كَنَى", "ك ن ي", "I", "to call someone by a kunya (كَنَاهُ أَبَا فُلَانٍ); passive يُكْنَى: he bears the kunya…", "birine künye vermek (كَنَاهُ أَبَا فُلَانٍ); meçhulü يُكْنَى: künyesi …'dır"),
}
# keys that a SIBLING package minted and that are staged, not yet on the shelf: used from the shelf once they are there
SHARED = {
 "numan": NM("النُّعْمَان", "al-Nuʿmān — a man's name; here the grandfather of al-Shaykh al-Mufīd", "Nu'mân — erkek ismi; burada Şeyh Müfîd'in dedesi"),
 "sabun": NN("سَبْعُونَ", "س ب ع", "seventy (declines like the sound masculine plural: سَبْعِينَ)", "yetmiş (cem-i müzekker sâlim gibi i'râblanır: سَبْعِينَ)"),
}
# the gloss a reused key shows in THIS text: the lemma is the shelf's, the sense or the person is this entry's (the shelf's own sense is kept beside it)
GLOSS_HERE = {
 "numan": ("al-Nuʿmān — a man's name; here the grandfather of al-Shaykh al-Mufīd (elsewhere: Abū Ḥanīfa al-Nuʿmān ibn Thābit)", "Nu'mân — erkek ismi; burada Şeyh Müfîd'in dedesi (başka yerde: Ebû Hanîfe Nu'mân b. Sâbit)"),
 "mufid": ("giving benefit (the Form IV ism fāʿil of أَفَادَ) — الشَّيْخُ الْمُفِيدُ: the title of Muḥammad ibn Muḥammad ibn al-Nuʿmān (d. 413 AH); (elsewhere) conveying, expressing", "fayda veren (efâde'nin ism-i fâili) — الشَّيْخُ الْمُفِيدُ: Muhammed b. Muhammed b. Nu'mân'ın (ö. 413) lakabı; (başka yerde) ifade eden, bildiren"),
 "muhammad": ("Muḥammad — a man's name", "Muhammed — erkek ismi"),
 "shaykh": ("an old man; an elder, a teacher (shaykh)", "yaşlı adam; şeyh, hoca"),
 "sahib": ("companion; the owner of, a man of — صَاحِبُ التَّصَانِيفِ: the author of the works", "arkadaş; sahip — صَاحِبُ التَّصَانِيفِ: eserlerin müellifi"),
 "muallim": ("teacher — ابْنُ الْمُعَلِّمِ «the Teacher's son»: the name al-Mufīd was known by", "muallim, öğretmen — ابْنُ الْمُعَلِّمِ «Muallim'in oğlu»: Müfîd'in tanındığı ad"),
 "kalam": ("speech; عِلْمُ الْكَلَامِ — kalām, the science of the articles of faith and their proofs", "söz, konuşma; عِلْمُ الْكَلَامِ — kelâm ilmi: akaid esaslarını delilleriyle ele alan ilim"),
 "adab": ("good manners, propriety; letters, literary learning", "edeb, âdâb; edebiyat bilgisi"),
 "dhakara": ("to mention, to give an account of", "anmak, zikretmek"),
 "asl": ("root, origin; a foundation — الْأَصْلَانِ «the two foundations»: uṣūl al-dīn and uṣūl al-fiqh", "asıl, köken; temel — الْأَصْلَانِ «iki asıl»: usûlü'd-dîn ve usûlü'l-fıkıh"),
 "fiqh": ("understanding; fiqh — the science of the rulings of the Law, jurisprudence", "anlayış; fıkıh — şer'î hükümler ilmi"),
 "khabar": ("a report, an item of news; الْأَخْبَار: the transmitted reports, the traditions", "haber; الْأَخْبَار: rivayet edilen haberler, hadisler"),
 "rajul": ("a man — مَعْرِفَةُ الرِّجَالِ: the science of the transmitters of reports", "adam, erkek — مَعْرِفَةُ الرِّجَالِ: râvîleri tanıma ilmi (ricâl ilmi)"),
 "hafiza": ("to memorise, to keep by heart; to guard, to preserve", "ezberlemek, hıfzetmek; korumak"),
 "hall-nathr": ("an untying, a loosening; the clearing up of a doubt or difficulty (masdar of حَلَّ) — elsewhere, in the badīʿ: verse put into prose", "çözme; bir şüpheyi veya güçlüğü giderme (halle'nin masdarı) — başka yerde, bedî'de: nazmı nesre çevirme"),
 "qawm": ("a people, a group; الْقَوْم: «those people», the party spoken of", "kavim, topluluk; الْقَوْم: sözü edilen taife"),
 "maktab": ("a place of writing (ism makān of كَتَبَ): a school where boys are taught to write (pl. مَكَاتِب); a writing-desk", "yazı yeri (ketebe'nin ism-i mekânı): çocuklara yazı öğretilen mektep (c. مَكَاتِب); yazı masası"),
 "haik": ("a weaver (plural حَاكَة, and حَوَكَة with the waw kept sound)", "dokumacı (cem'i: حَاكَة; vâvı sahih kalarak حَوَكَة)"),
 "sabi-boy": ("a child, a boy", "çocuk, sabî"),
 "tilmidh": ("student, pupil (plural تَلَامِيذ and تَلَامِذَة)", "talebe, öğrenci (cem'i: تَلَامِيذ ve تَلَامِذَة)"),
 "rubba": ("«many a…», «sometimes» — a jarr letter; with the stopping مَا (رُبَّمَا) it comes before a verb: «at times»", "rubbe — «nice», «bazen» anlamında cer harfi; kâffe mâ'sıyla (رُبَّمَا) fiilin başına gelir: «zaman zaman»"),
 "shafaa-verb": ("to intercede (شَفَعَ لَهُ عِنْدَ)", "şefaat etmek (şefea lehû inde)"),
 "shayyaa": ("to escort in farewell, to see off; to walk with a bier to the grave (Form II)", "uğurlamak, teşyî etmek; cenazeyi kabre kadar uğurlamak (tef'îl bâbı)"),
 "talif": ("composition, the putting of words together (masdar, Form II); a written work — plural تَآلِيف, and with the hamza lightened تَوَالِيف", "te'lîf; kelimeleri birleştirme (masdar, tef'îl); telif edilmiş eser — cem'i تَآلِيف, hemzenin tahfifiyle تَوَالِيف"),
 "waqafa": ("to stop, to stand; وَقَفَ عَلَى الشَّيْءِ: to come upon a thing, to get to see it", "durmak; وَقَفَ عَلَى الشَّيْءِ: bir şeye vâkıf olmak, onu görmek"),
 "ashara": ("ten; ـَ عَشْرَةَ: the second part of the compound numbers eleven to nineteen with a feminine counted noun (ثَلَاثَ عَشْرَةَ سَنَةً)", "on; ـَ عَشْرَةَ: müennes ma'dûd ile on birden on dokuza kadar mürekkeb sayıların ikinci cüz'ü (ثَلَاثَ عَشْرَةَ سَنَةً)"),
 "birr": ("kindness, dutiful goodness; giving, charity", "birr, iyilik; ihsan"),
}
LEMMA_HERE = {"hadha": "هٰذَا", "dhalika": "ذٰلِكَ"}   # the text's spelling (the shelf holds both spellings under these keys)
_STAGED = {}
for d in (OUT_ROOT.iterdir() if OUT_ROOT.exists() else []):
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
for k, e in list(NEW_GLOSS.items()) + list(SHARED.items()):
    hit = [p for p in PKGS if k in _G[p]]
    if k in NEW_GLOSS: assert not hit, ("a key is a global claim — taken", k, hit)
    else: assert all(_lemma_id(_G[p][k]) == _lemma_id(e) for p in hit), ("shared key, another lemma on the shelf", k, hit)
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
    if e is None and k in SHARED: GLOSS[k] = SHARED[k]; continue
    if e is None: missing.append(k)
    else:
        GLOSS[k], ORIGIN[k] = json.loads(json.dumps(e)), p
        if k in GLOSS_HERE: GLOSS[k]["gloss"] = {"en": GLOSS_HERE[k][0], "tr": GLOSS_HERE[k][1]}
        if k in LEMMA_HERE:
            assert _lemma_id(GLOSS[k]) == _lemma_id({"lemma": LEMMA_HERE[k]}), k
            GLOSS[k]["lemma"] = LEMMA_HERE[k]
assert not missing, missing
assert not [k for k in GLOSS_HERE if k not in GLOSS], [k for k in GLOSS_HERE if k not in GLOSS]
assert not [k for k in NEW_GLOSS if k not in used], [k for k in NEW_GLOSS if k not in used]
MORPH = {"verbs": {}}
MORPH["verbs"]["atnaba"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْنَب", "طْنِب", "أَطْنِب", "إِطْنَاب", "مُطْنِب", None, None, None,
                                       "أَطْنَبَ فِي الْكَلَامِ: بَالَغَ فِيهِ وَأَطَالَ — لَازِمٌ.")
MORPH["verbs"]["nazara-debate"] = _sg.derived(_sg.B3, _sg.W3, "ُ", "نَاظَر", "نَاظِر", "نَاظِر", "مُنَاظَرَة", "مُنَاظِر", "مُنَاظَر", "نُوظِرَ", "يُنَاظَرُ",
                                              "نَاظَرَهُ: بَاحَثَهُ وَجَادَلَهُ.")
MORPH["verbs"]["talammaha"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَلَمَّح", "تَلَمَّح", "تَلَمَّح", "تَلَمُّح", "مُتَلَمِّح", "مُتَلَمَّح", "تُلُمِّحَ", "يُتَلَمَّحُ",
                                          "تَلَمَّحَ الشَّيْءَ: تَطَلَّبَهُ بِنَظَرِهِ.")
MORPH["verbs"]["shaffaa"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "شَفَّع", "شَفِّع", "شَفِّع", "تَشْفِيع", "مُشَفِّع", "مُشَفَّع", "شُفِّعَ", "يُشَفَّعُ",
                                        "شَفَّعَهُ: قَبِلَ شَفَاعَتَهُ.")
MORPH["verbs"]["kana-kunya"] = _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "كَنَ", "كْن", "i", "اِكْن", "كُنْيَة", "كَانٍ", "مَكْنِيّ", "كُنِيَ", "يُكْنَى",
                                          "كَنَاهُ أَبَا فُلَانٍ يَكْنِيهِ: سَمَّاهُ بِهِ كُنْيَةً.")
for k, e in GLOSS.items():
    if e.get("pos") != "verb" or k in MORPH["verbs"]: continue
    if k in ORIGIN and k in _M[ORIGIN[k]]: MORPH["verbs"][k] = _M[ORIGIN[k]][k]
    else:
        for p in PKGS:
            if k in _M[p] and _lemma_id(_G[p].get(k, {})) == _lemma_id(e): MORPH["verbs"][k] = _M[p][k]; break
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

ATTR_AR = "نَصٌّ مَنْقُولٌ بِلَفْظِهِ، كَامِلًا: التَّرْجَمَةُ رَقْم ٢١٣، «الشَّيْخُ الْمُفِيدُ مُحَمَّدُ بْنُ مُحَمَّدِ بْنِ النُّعْمَانِ الْبَغْدَادِيُّ»، مِنْ «سِيَرِ أَعْلَامِ النُّبَلَاءِ» لِشَمْسِ الدِّينِ الذَّهَبِيِّ (ت ٧٤٨ هـ)، طَبْعَةِ مُؤَسَّسَةِ الرِّسَالَةِ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ١٠٩٠٦)، الْجُزْءِ السَّابِعَ عَشَرَ، ص ٣٤٤–٣٤٥. التَّرْجَمَةُ كُلُّهَا مِنْ عُنْوَانِهَا إِلَى آخِرِ كَلِمَةٍ فِيهَا («يُكْنَى أَبَا عَبْدِ اللهِ»)، لَمْ يُتْرَكْ مِنْهَا شَيْءٌ؛ وَالْفُصُولُ الثَّلَاثَةُ ثَلَاثُ قِطَعٍ مُتَتَالِيَةٍ: (١) ص ٣٤٤ مِنَ الْعُنْوَانِ إِلَى «وَالشِّعْرِ»؛ (٢) ص ٣٤٤ مِنْ «وَكَانَ يُنَاظِرُ» إِلَى «كَثُرَ تَلَامِذَتُهُ»؛ (٣) ص ٣٤٤–٣٤٥ مِنْ «وَقِيلَ: رُبَّمَا زَارَهُ» إِلَى آخِرِهَا. وَهُوَ كَلَامُ الذَّهَبِيِّ بِأَحْكَامِهِ كَمَا كَتَبَهَا — وَمِنْهَا قَوْلُهُ «عَالِمُ الرَّافِضَةِ» وَ«يَعْنِي فَيُضِلُّهُ» وَ«لَمْ أَقِفْ عَلَى شَيْءٍ مِنْهَا — وَلِلّٰهِ الْحَمْدُ» — نُقِلَ كَمَا هُوَ بِلَا تَلْيِينٍ وَلَا تَعْلِيقٍ؛ وَأَكْثَرُ التَّرْجَمَةِ نَقْلُهُ عَنِ ابْنِ أَبِي طَيٍّ فِي «تَارِيخِ الْإِمَامِيَّةِ»، وَقَدِ اخْتَصَرَهُ بِقَوْلِهِ «إِلَى أَنْ قَالَ». الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ كَمَا هُوَ وَوُحِّدَ رَسْمُهُ عَلَى رَسْمِ الْمَكْتَبَةِ (لَا سُكُونَ عَلَى حَرْفِ الْمَدِّ، وَالْفَتْحَةُ قَبْلَ الْأَلِفِ، وَتَنْوِينُ النَّصْبِ قَبْلَ أَلِفِهِ، وَسُكُونُ لَامِ «الْ» الْقَمَرِيَّةِ وَبَاءِ «بْن»، وَالشَّدَّةُ عَلَى اللَّامِ فِي «إِلَّا»، وَالْأَلِفُ الْخَنْجَرِيَّةُ فِي «هٰذَا» وَ«ذٰلِكَ»)؛ وَمَا تَرَكَتْهُ الطَّبْعَةُ بِلَا شَكْلٍ ضَبَطْنَاهُ نَحْنُ، وَهُوَ: حَرَكَةُ آخِرِ الْكَلِمَةِ فِي: الرَّافِضَةِ، الْمُفِيدُ (فِي الْمَوْضِعِ الثَّانِي)، تَارِيخِ، الْإِمَامِيَّةِ، جَمِيعِ، فُنُونِ (فِي الْمَوْضِعِ الثَّانِي)، الْأَصْلَيْنِ، الرِّجَالِ، الْعَظَمَةِ، الدَّوْلَةِ (فِي الْمَوْضِعَيْنِ)، الْبُوَيْهِيَّةِ، الْخُلَفَاءِ، لِلْمُطَالَعَةِ، وَالتَّعْلِيمِ، لِلْمُخَالِفِينَ، وَحَفِظَهُ، قَدَرَ، شُبَهِ، الْقَوْمِ، أَبَوَيْهِ، مُصَنَّفٍ، وَأَرْبَعِ، مِائَةٍ؛ وَسُكُونُ حَرْفٍ فِي: الْأَصْلَيْنِ، وَالشِّعْرِ، وَالرُّتْبَةِ، لِلْمُطَالَعَةِ، وَالتَّعْلِيمِ، لِلْمُخَالِفِينَ، أَحْرَصِ، فَيَسْتَأْجِرُهُ، أَبَوَيْهِ، رَبْعَةً، أَسْمَرَ، مِائَتَيْ؛ وَحَرَكَةٌ فِي وَسَطِ الْكَلِمَةِ فِي: تَارِيخِ، قَوِيَّ، لِلْمُطَالَعَةِ، لِلْمُخَالِفِينَ، وَبِهٰذَا، أَحْرَصِ، الْمَكَاتِبِ، وَحَوَانِيتِ، الصَّبِيَّ، فَيَسْتَأْجِرُهُ، أَبَوَيْهِ، أَسْمَرَ، وَكَسْرَةُ الْمِيمِ فِي «مِائَتَيْ» وَ«مِائَةٍ» وَ«مِائَتَيْنِ»؛ وَشَدَّةُ التَّاءِ فِي «سِتًّا»؛ وَضَبْطُ «وَلِلّٰهِ» كُلُّهُ (وَهِيَ فِي الطَّبْعَةِ «وَلله»). وَ«رَبْعَةً» ضُبِطَتْ بِسُكُونِ الْبَاءِ عَلَى الْمَشْهُورِ، وَفِيهَا لُغَةٌ بِفَتْحِهَا. وَلَمْ تُغَيَّرْ كَلِمَةٌ وَلَمْ تُزَدْ وَلَمْ تُحْذَفْ، وَلَمْ يُصَحَّحْ شَيْءٌ مِنَ النَّصِّ عَلَى نُسْخَةٍ أُخْرَى. عَلَامَاتُ التَّرْقِيمِ لِلْمُحَقِّقِ، وَلَمْ نُثْبِتْ نُقْطَتَيْهِ بَعْدَ «وَاسْمُهُ» وَ«وَيُعْرَفُ»، وَلَا قَوْسَيْهِ حَوْلَ «تَارِيخِ الْإِمَامِيَّةِ»، وَلَا رَقْمَ التَّرْجَمَةِ وَنَجْمَتَهَا وَأَرْقَامَ الْحَوَاشِي، وَجُعِلَتِ الشَّرْطَةُ «—». وَلَمْ تُسْتَعْمَلْ حَوَاشِي الْمُحَقِّقِ. وَقَوْلُ عَضُدِ الدَّوْلَةِ «اشْفَعْ تُشَفَّعْ» لَفْظٌ مِنْ حَدِيثِ الشَّفَاعَةِ، نُبِّهَ عَلَيْهِ فِي إِعْرَابِهِ وَلَمْ يُغَيَّرْ. تَقْسِيمُ الْجُمَلِ (وَقَدْ قُسِمَتْ سِتُّ جُمَلٍ طَوِيلَةٍ مِنَ الطَّبْعَةِ عِنْدَ فَاصِلَةٍ أَوْ شَرْطَةٍ: الْفَصْلُ ١ الْجُمْلَتَانِ ٢–٣ ثُمَّ ٥–٦، وَالْفَصْلُ ٢ الْجُمَلُ ١–٣ ثُمَّ ٤–٦، وَالْفَصْلُ ٣ الْجُمْلَتَانِ ٢–٣ ثُمَّ الْجُمَلُ ٤–٦؛ وَمَا بَدَأَ مِنْهَا بِحَرْفِ عَطْفٍ أُعْرِبَ عَاطِفًا) وَعَنَاوِينُ الْفُصُولِ وَالتَّرْجَمَةُ إِلَى اللُّغَتَيْنِ وَكُلُّ إِعْرَابٍ اجْتِهَادُ الْمُؤَلِّفِ، بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ."
ATTR_EN = "The RECEIVED text, verbatim and WHOLE: entry no. 213, «الشَّيْخُ الْمُفِيدُ مُحَمَّدُ بْنُ مُحَمَّدِ بْنِ النُّعْمَانِ الْبَغْدَادِيُّ», in Siyar Aʿlām al-Nubalāʾ by Shams al-Dīn al-Dhahabī (d. 748 AH), in the Muʾassasat al-Risāla edition as al-Maktaba al-Shāmila carries it (book 10906), vol. 17, pp. 344–345. The entire entry is here, from its heading to its last word («يُكْنَى أَبَا عَبْدِ اللهِ»), with NOTHING left out: the three chapters are three ADJACENT spans — (1) p. 344, from the heading to «وَالشِّعْرِ»; (2) p. 344, from «وَكَانَ يُنَاظِرُ» to «كَثُرَ تَلَامِذَتُهُ»; (3) pp. 344–345, from «وَقِيلَ: رُبَّمَا زَارَهُ» to the end. It is al-Dhahabī's own text, with his judgements as he wrote them — among them «عَالِمُ الرَّافِضَةِ», «يَعْنِي فَيُضِلُّهُ» and «لَمْ أَقِفْ عَلَى شَيْءٍ مِنْهَا — وَلِلّٰهِ الْحَمْدُ» — carried over as they stand, neither softened nor commented on; most of the entry is his quotation from Ibn Abī Ṭayy's «تَارِيخُ الْإِمَامِيَّةِ», which he abridges with «إِلَى أَنْ قَالَ». TWO VOWELLING LAYERS: the edition is vowelled, though not on every letter. Its vowels are kept and only normalised to the shelf's spelling (no sukūn on a madd letter, fatḥa before the alif, tanwīn fatḥ before its alif, sukūn on the lām of the qamarī article and on the bāʾ of «بْن», the shadda of «إِلَّا» on its lām, the dagger alif of «هٰذَا» and «ذٰلِكَ»). Where the edition leaves a letter bare the vowel is OURS: the vowel of the last letter in الرَّافِضَةِ، الْمُفِيدُ (its second occurrence)، تَارِيخِ، الْإِمَامِيَّةِ، جَمِيعِ، فُنُونِ (its second occurrence)، الْأَصْلَيْنِ، الرِّجَالِ، الْعَظَمَةِ، الدَّوْلَةِ (both occurrences)، الْبُوَيْهِيَّةِ، الْخُلَفَاءِ، لِلْمُطَالَعَةِ، وَالتَّعْلِيمِ، لِلْمُخَالِفِينَ، وَحَفِظَهُ، قَدَرَ، شُبَهِ، الْقَوْمِ، أَبَوَيْهِ، مُصَنَّفٍ، وَأَرْبَعِ، مِائَةٍ; a sukūn in الْأَصْلَيْنِ، وَالشِّعْرِ، وَالرُّتْبَةِ، لِلْمُطَالَعَةِ، وَالتَّعْلِيمِ، لِلْمُخَالِفِينَ، أَحْرَصِ، فَيَسْتَأْجِرُهُ، أَبَوَيْهِ، رَبْعَةً، أَسْمَرَ، مِائَتَيْ; a vowel inside the word in تَارِيخِ، قَوِيَّ، لِلْمُطَالَعَةِ، لِلْمُخَالِفِينَ، وَبِهٰذَا، أَحْرَصِ، الْمَكَاتِبِ، وَحَوَانِيتِ، الصَّبِيَّ، فَيَسْتَأْجِرُهُ، أَبَوَيْهِ، أَسْمَرَ, and the kasra of the mīm in «مِائَتَيْ», «مِائَةٍ» and «مِائَتَيْنِ»; the shadda of the tāʾ in «سِتًّا»; and all the vowelling of «وَلِلّٰهِ» (printed «وَلله»). «رَبْعَةً» is given the sukūn of the well-known form; رَبَعَة with a fatḥa is also transmitted. NO word is changed, added or dropped, and no reading was emended against another witness. The punctuation is the editor's: his colon after «وَاسْمُهُ» and «وَيُعْرَفُ», his brackets round the book title «تَارِيخِ الْإِمَامِيَّةِ», the entry number, the star of the heading and the footnote marks are not carried over, and his hyphens are set as dashes. The edition's footnotes are not used. ʿAḍud al-Dawla's words «اشْفَعْ تُشَفَّعْ» are a phrase of the ḥadīth of the Intercession; the token's iʿrāb line says so, and the wording is untouched. Sentence division (six long periods of the edition are cut at a comma or a dash: ch1 s2–s3 and s5–s6, ch2 s1–s3 and s4–s6, ch3 s2–s3 and s4–s6; where a later part opens with a conjunction it is analysed as one), chapter titles, translations and every iʿrāb line are the author's own analysis. reviewStatus: pending-scholarly-review."
ATTR_TR = "LAFZIYLA ve TAM olarak aktarılan metin: Şemsüddîn ez-Zehebî'nin (ö. 748) «Siyeru A'lâmi'n-Nübelâ» adlı eserindeki 213 numaralı madde, «الشَّيْخُ الْمُفِيدُ مُحَمَّدُ بْنُ مُحَمَّدِ بْنِ النُّعْمَانِ الْبَغْدَادِيُّ»; Müessesetü'r-Risâle baskısı, el-Mektebetü'ş-Şâmile'deki hâliyle (kitap 10906), c. 17, s. 344–345. Madde, başlığından son kelimesine («يُكْنَى أَبَا عَبْدِ اللهِ») kadar eksiksizdir; HİÇBİR ŞEY bırakılmamıştır: üç bölüm, ARDIŞIK üç parçadır — (1) s. 344, başlıktan «وَالشِّعْرِ»ye kadar; (2) s. 344, «وَكَانَ يُنَاظِرُ»dan «كَثُرَ تَلَامِذَتُهُ»ya kadar; (3) s. 344–345, «وَقِيلَ: رُبَّمَا زَارَهُ»dan sonuna kadar. Bu, Zehebî'nin kendi metnidir ve hükümleri onun yazdığı gibidir — «عَالِمُ الرَّافِضَةِ», «يَعْنِي فَيُضِلُّهُ» ve «لَمْ أَقِفْ عَلَى شَيْءٍ مِنْهَا — وَلِلّٰهِ الْحَمْدُ» sözleri bunlardandır —; yumuşatılmadan ve üzerine yorum eklenmeden olduğu gibi aktarılmıştır. Maddenin çoğu, Zehebî'nin İbn Ebî Tay'ın «تَارِيخُ الْإِمَامِيَّةِ» adlı eserinden yaptığı ve «إِلَى أَنْ قَالَ» diyerek kısalttığı nakildir. İKİ HAREKE KATMANI: baskı harekelidir, fakat her harfte değil. Baskının harekeleri korunmuş, yalnızca kütüphanenin imlâsına göre birleştirilmiştir (med harfinde sükûn yok, fetha eliften önce, nasb tenvini elifinden önce, kamerî «الْ» lâmında ve «بْن» bâ'sında sükûn, «إِلَّا»da şeddenin lâm üzerinde olması, «هٰذَا» ve «ذٰلِكَ»de hançer elif). Baskının harekesiz bıraktığı harflerin harekesi BİZE aittir: şu kelimelerde son harfin harekesi: الرَّافِضَةِ، الْمُفِيدُ (ikinci geçtiği yerde)، تَارِيخِ، الْإِمَامِيَّةِ، جَمِيعِ، فُنُونِ (ikinci geçtiği yerde)، الْأَصْلَيْنِ، الرِّجَالِ، الْعَظَمَةِ، الدَّوْلَةِ (her iki yerde)، الْبُوَيْهِيَّةِ، الْخُلَفَاءِ، لِلْمُطَالَعَةِ، وَالتَّعْلِيمِ، لِلْمُخَالِفِينَ، وَحَفِظَهُ، قَدَرَ، شُبَهِ، الْقَوْمِ، أَبَوَيْهِ، مُصَنَّفٍ، وَأَرْبَعِ، مِائَةٍ; şu kelimelerde bir harfin sükûnu: الْأَصْلَيْنِ، وَالشِّعْرِ، وَالرُّتْبَةِ، لِلْمُطَالَعَةِ، وَالتَّعْلِيمِ، لِلْمُخَالِفِينَ، أَحْرَصِ، فَيَسْتَأْجِرُهُ، أَبَوَيْهِ، رَبْعَةً، أَسْمَرَ، مِائَتَيْ; şu kelimelerde kelime içindeki bir hareke: تَارِيخِ، قَوِيَّ، لِلْمُطَالَعَةِ، لِلْمُخَالِفِينَ، وَبِهٰذَا، أَحْرَصِ، الْمَكَاتِبِ، وَحَوَانِيتِ، الصَّبِيَّ، فَيَسْتَأْجِرُهُ، أَبَوَيْهِ، أَسْمَرَ, ayrıca «مِائَتَيْ», «مِائَةٍ» ve «مِائَتَيْنِ»deki mîmin kesresi; «سِتًّا»daki tâ'nın şeddesi; ve «وَلِلّٰهِ»nin bütün harekeleri (baskıda «وَلله»). «رَبْعَةً» meşhur okunuşa göre bâ'nın sükûnuyla harekelenmiştir; fethalı رَبَعَة de nakledilir. Hiçbir kelime değiştirilmemiş, eklenmemiş veya çıkarılmamıştır; başka bir nüshaya göre hiçbir okuyuş tashih edilmemiştir. Noktalama muhakkike aittir: «وَاسْمُهُ» ve «وَيُعْرَفُ»dan sonraki iki nokta, kitap adı «تَارِيخِ الْإِمَامِيَّةِ»nin etrafındaki parantez, madde numarası, başlıktaki yıldız ve dipnot işaretleri alınmamış, kısa çizgiler uzun çizgi yapılmıştır. Baskının dipnotları kullanılmamıştır. Adudüddevle'nin «اشْفَعْ تُشَفَّعْ» sözü şefaat hadisinden bir lafızdır; kelimenin i'râb satırında buna işaret edilmiş, lafza dokunulmamıştır. Cümle taksimi (baskının altı uzun cümlesi virgülde veya çizgide bölünmüştür: 1. bölüm c. 2–3 ve c. 5–6, 2. bölüm c. 1–3 ve c. 4–6, 3. bölüm c. 2–3 ve c. 4–6; sonraki parça atıf harfiyle başlıyorsa öyle tahlil edilmiştir), bölüm başlıkları, çeviriler ve bütün i'râb satırları müellifin kendi tahlilidir; ilmî incelemeyi beklemektedir."
MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "تَرْجَمَةُ الشَّيْخِ الْمُفِيدِ", "en": "The Entry on al-Shaykh al-Mufīd", "tr": "Şeyh Müfîd'in Tercemesi"},
 "subtitle": {"ar": "تَرْجَمَةُ الشَّيْخِ الْمُفِيدِ مُحَمَّدِ بْنِ مُحَمَّدِ بْنِ النُّعْمَانِ الْبَغْدَادِيِّ فِي «سِيَرِ أَعْلَامِ النُّبَلَاءِ» لِلذَّهَبِيِّ، كَامِلَةً — نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Al-Dhahabī's entry on al-Shaykh al-Mufīd Muḥammad ibn Muḥammad ibn al-Nuʿmān al-Baghdādī in Siyar Aʿlām al-Nubalāʾ, complete — the received text, word for word",
              "tr": "Zehebî'nin Siyeru A'lâmi'n-Nübelâ'sındaki Şeyh Müfîd Muhammed b. Muhammed b. Nu'mân el-Bağdâdî maddesi, tam olarak — metin lafzıyla aktarılmıştır"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": ATTR_AR,
  "en": ATTR_EN,
  "tr": ATTR_TR,
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
      "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "new:", sorted(k for k in GLOSS if k in NEW_GLOSS), "shared:", sorted(k for k in GLOSS if k in SHARED and k not in ORIGIN), "->", PKG)
