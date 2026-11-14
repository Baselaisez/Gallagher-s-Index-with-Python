# -*- coding: utf-8 -*-
"""Author content/samples/musa-fi-madyan — «مُوسَى فِي مَدْيَنَ», the fourth ORIGINAL Level-1 story of the Mūsā group (wave 88).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Mūsā's flight to Madyan
(al-Qaṣaṣ 14–29) as it is commonly retold to children. No āya is quoted; no sentence here may be cited as a classical
text. Four chapters, thirty-nine sentences. Every token carries trilingual iʿrāb. Verb paradigms and glossary entries are
COPIED from the packages that already own the lemma (the lemma-identity rule); only خَائِف, الرُّعَاة, اسْتَأْجَرَ and
ثَمَانِي are new to the corpus.

    QISSA_PKG_ROOT=<dir> python3 author_musa4.py     # a dry run writes under <dir>/musa-fi-madyan
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "musa-fi-madyan"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
import sarf_gen as _sg

DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)

def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}

# ---- the house wordings ------------------------------------------------------------------------------------------
WA_AR = "الْوَاوُ عَاطِفَةٌ، وَ"
FA_AR = "الْفَاءُ عَاطِفَةٌ، وَ"
def _pre(full):
    """a وَ / فَ prefix on the token: (prefix letter, bare stem, segments head, the three i'rab openings)"""
    if full.startswith("وَ"): return "وَ", full[2:], seg("وَ", "wa", "conj"), WA_AR, "The waw conjoins; ", "«ve» + "
    if full.startswith("فَ"): return "فَ", full[2:], seg("فَ", "fa", "conj"), FA_AR, "The fa conjoins; ", "«bunun üzerine» + "
    return "", full, None, "", "", ""

def KANA(full="كَانَ", punct=None, fem=False):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    ta = "، وَالتَّاءُ لِلتَّأْنِيثِ" if fem else ""
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        ar0 + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + ta + ".",
        en0 + "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb" + (" (the ta marks the feminine)" if fem else "") + ".",
        tr0 + "«idi» — nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder" + (" (tâ te'nîs içindir)" if fem else "") + ".",
        punct=punct, segments=[sg, seg(stem, "kana", "verb")] if sg else None)

def SARA(full, punct=None):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        ar0 + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
        en0 + "صَارَ «became» is one of كَانَ's sisters: it raises its noun and puts its predicate in nasb.",
        tr0 + "«oldu» — kâne'nin kardeşlerinden nâkıs fiil; ismini ref, haberini nasb eder.",
        punct=punct, segments=[sg, seg(stem, "sara", "verb")] if sg else None)

def ISMK(full, lex, pos="noun", extra=None, note_ar="", note_en="", note_tr="", punct=None, segments=None, sign="بِالضَّمَّةِ", muakhkhar=False):
    g = ["kana-wa-akhawatuha"] + (extra or [])
    mu = " مُؤَخَّرٌ" if muakhkhar else ""
    return tok(full, lex, pos, g,
        "اسْمُ كَانَ" + mu + " مَرْفُوعٌ " + sign + note_ar + ".",
        "The noun of كَانَ" + (" (placed after its predicate)" if muakhkhar else "") + ", in raf'" + note_en + ".",
        "Kâne'nin ismi" + (" (haberinden sonraya bırakılmış)" if muakhkhar else "") + ", merfû" + note_tr + ".", punct=punct, segments=segments)

def KHK(full, lex, pos="noun", extra=None, note_ar="", note_en="", note_tr="", punct=None, segments=None, sign="بِالْفَتْحَةِ"):
    g = ["kana-wa-akhawatuha"] + (extra or [])
    return tok(full, lex, pos, g,
        "خَبَرُ كَانَ مَنْصُوبٌ " + sign + note_ar + ".",
        "The predicate of كَانَ, in nasb" + note_en + ".",
        "Kâne'nin haberi, mansûb" + note_tr + ".", punct=punct, segments=segments)

def PREP(full, lex, role_ar="", role_en="", role_tr="", punct=None, segments=None, gloss_tr=""):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, lex, "prep", ["huruf-jarr"],
        ar0 + "حَرْفُ جَرٍّ" + role_ar + ".", en0 + "a jarr letter" + role_en + ".", tr0 + gloss_tr + " — cer harfi" + role_tr + ".",
        punct=punct, segments=segments or ([sg, seg(stem, lex, "prep")] if sg else None))
KH_MUQ = ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate of كَانَ", "; câr-mecrûr, kâne'nin öne alınmış haberidir")

def MAJR(full, lex, pos="noun", extra=None, note_ar="", note_en="", note_tr="", punct=None, segments=None, sign="بِالْكَسْرَةِ"):
    return tok(full, lex, pos, ["huruf-jarr"] + (extra or []),
        "مَجْرُورٌ " + sign + note_ar + ".", "In jarr after the letter" + note_en + ".", "Cer harfiyle mecrûr" + note_tr + ".", punct=punct, segments=segments)

DIPT = ("، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", " — a foreign proper name, barred from tanwin", " — yabancı özel isim, gayr-i munsarif")
DIPT_F = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ", " — a feminine proper name, barred from tanwin", " — müennes özel isim, gayr-i munsarif")
FATHA_JARR = "بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ"
MUQ_ALIF = ("مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", " — the vowel is estimated on the alif", " — hareke elif üzerinde takdîrîdir")

def MADI(full, lex, extra=None, fem=False, hidden=False, punct=None, note_ar="", note_en="", note_tr="", kasra=False):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    ta = "، وَالتَّاءُ لِلتَّأْنِيثِ" + ("، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ" if kasra else "") if fem else ""
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + ("هِيَ" if fem else "هُوَ") if hidden else ""
    return tok(full, lex, "verb", ["thulathi-mujarrad-babs"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + ta + hid + note_ar + ".",
        en0 + "past verb built on fatha" + (" (the ta marks the feminine" + (", voweled with kasra before the following ال" if kasra else "") + ")" if fem else "") + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + (" (tâ te'nîs içindir" + ("; iki sâkin karşılaştığı için kesre ile harekelendi" if kasra else "") + ")" if fem else "") + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)

def FAIL(full, lex, pos="noun", extra=None, note_ar="", note_en="", note_tr="", punct=None, segments=None, sign="بِالضَّمَّةِ"):
    return tok(full, lex, pos, ["fail"] + (extra or []),
        "فَاعِلٌ مَرْفُوعٌ " + sign + note_ar + ".", "The doer (fa'il), in raf'" + note_en + ".", "Fâil, merfû" + note_tr + ".", punct=punct, segments=segments)

def MAFUL(full, lex, pos="noun", extra=None, note_ar="", note_en="", note_tr="", punct=None, segments=None, sign="بِالْفَتْحَةِ"):
    return tok(full, lex, pos, ["maful-bihi"] + (extra or []),
        "مَفْعُولٌ بِهِ مَنْصُوبٌ " + sign + note_ar + ".", "The direct object, in nasb" + note_en + ".", "Mef'ûlün bih, mansûb" + note_tr + ".", punct=punct, segments=segments)

def MUDAF_ILAYH(full, lex, pos="noun", extra=None, sign="بِالْكَسْرَةِ", note_ar="", note_en="", note_tr="", punct=None):
    return tok(full, lex, pos, ["idafa-definiteness"] + (extra or []),
        "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + sign + note_ar + ".", "The second term of the idafa, in jarr" + note_en + ".", "Muzâfun ileyh, mecrûr" + note_tr + ".", punct=punct)

def NAAT(full, lex, case="raf", extra=None, note_ar="", note_en="", note_tr="", punct=None):
    sign = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, lex, "noun", ["naat-sifa"] + (extra or []),
        "نَعْتٌ " + sign + note_ar + ".", "An adjective (na't), agreeing with its noun" + note_en + ".", "Na't (sıfat), mevsûfuna uyar" + note_tr + ".", punct=punct)

def ATF(full, lex, pos="noun", case="raf", extra=None, note_ar="", note_en="", note_tr="", punct=None, segments=None, sign=None):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    sign = sign or {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, lex, pos, ["atf-nasaq"] + (extra or []),
        ar0 + "مَعْطُوفٌ " + sign + note_ar + ".", en0 + "conjoined to the word before it, in the same case" + note_en + ".", tr0 + "ma'tûf; öncekinin i'râbını alır" + note_tr + ".",
        punct=punct, segments=segments or ([sg, seg(stem, lex, pos)] if sg else None))

def MUDARI_KH(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="", hidden=True):
    """a mudari' whose clause is the khabar of kana (the doer hidden, or the waw of the five verbs)"""
    return tok(full, lex, "verb", ["kana-wa-akhawatuha", "mudari-marfu"] + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ" + note_ar + ".",
        "Present verb in raf'; its doer is a hidden pronoun, and the clause fills the seat of كَانَ's predicate" + note_en + ".",
        "Merfû muzâri; fâili gizli zamir — cümle, kâne'nin haberi olarak mahallen mansûbdur" + note_tr + ".", punct=punct)
def MUDARI5_KH(full, lex, extra=None, punct=None, segments=None, note_ar="", note_en="", note_tr=""):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, lex, "verb", ["afal-khamsa", "kana-wa-akhawatuha"] + (extra or []),
        ar0 + "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ" + note_ar + ".",
        en0 + "one of the five verbs, in raf' by the kept nun; the waw is its doer, and the clause fills the seat of كَانَ's predicate" + note_en + ".",
        tr0 + "ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâildir — cümle, kâne'nin haberi olarak mahallen mansûbdur" + note_tr + ".",
        punct=punct, segments=segments or ([sg, seg(stem, lex, "verb")] if sg else None))

# ============ «مُوسَى فِي مَدْيَنَ» — the fourth story: four chapters ============
MUSA_F = lambda punct=None: FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0], punct=punct)
MUSA_ISMK = lambda punct=None: ISMK("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0], punct=punct)
ALLAH_MI = lambda punct=None: MUDAF_ILAYH("اللهِ", "allah", "propn", [], note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=punct)
SHAYKH_F = lambda punct=None: FAIL("الشَّيْخُ", "shaykh", punct=punct)
QALA = lambda full="وَقَالَ", hidden=False, punct=None: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=punct)
QALAT = lambda full="وَقَالَتْ", hidden=True, punct=None: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], fem=True, hidden=hidden, note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=punct)
PRON = {"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هُمْ": "pron-3mp", "كَ": "pron-2ms", "كُمَا": "pron-2d", "نِي": "pron-1s", "ي": "pron-1s", "نَا": "pron-1p"}
PRON_AR = {"هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "هَا": "هَا", "هُمَا": "هُمَا", "هِمَا": "هُمَا", "هُمْ": "هُمْ", "كَ": "الْكَافُ", "كُمَا": "كُمَا", "نِي": "الْيَاءُ", "ي": "الْيَاءُ", "نَا": "نَا"}
THUMMA = lambda: tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi.")
YA = lambda: tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "The vocative particle «O».", "Nidâ harfi «ey».")
MINA = lambda: tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter, voweled with fatha before the following ال.", "«-den» — cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi.")
LIMADHA = lambda: tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "The lam is a jarr letter; مَاذَا «what» is the interrogative noun in the seat of jarr — «for what?».", "Lâm cer harfi; mâzâ istifhâm ismi, mahallen mecrûr — «niçin?».")
HUNAKA = lambda punct=None: tok("هُنَاكَ", "hunaka", "noun", ["asma-al-ishara", "maful-fih"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", "The demonstrative of far place «there», built on fatha, in the seat of nasb as an adverb of place.", "Uzak mekân için işaret ismi «orada», fetha üzere mebnî; mahallen mansûb mekân zarfı.", punct=punct)
HUNA = lambda punct=None: tok("هُنَا", "huna", "noun", ["asma-al-ishara", "maful-fih"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", "The demonstrative of place «here», built on sukun, in the seat of nasb as an adverb of place.", "Mekân için işaret ismi «burada», sükûn üzere mebnî; mahallen mansûb mekân zarfı.", punct=punct)
INDA = lambda punct=None: tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of place «at», in nasb and annexed.", "«Yanında» — mekân zarfı, mansûb, muzâf.", punct=punct)
MAA = lambda punct=None: tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of place «with», in nasb and annexed.", "«ile» — mekân zarfı, mansûb, muzâf.", punct=punct)
def LAHU(full, pron, pron_tr, punct=None, grammar=None):
    return tok(full, "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + (grammar or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "The lam is a jarr letter; the attached pronoun fills the seat of jarr.", "Lâm cer harfi; bitişik zamir mahallen mecrûr" + pron_tr + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg(full[1:], pron, "pron")])
def HAL(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """خَائِفًا: the hal — the doer's state at the time of the verb"""
    return tok(full, lex, "noun", ["hal"] + (extra or []),
        "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ هَيْئَةَ صَاحِبِهِ وَقْتَ الْفِعْلِ" + note_ar + ".",
        "The hal (circumstantial accusative), in nasb — it states the doer's condition at the time of the action" + note_en + ".",
        "Hâl, mansûb — sahibinin fiil anındaki durumunu bildirir" + note_tr + ".", punct=punct)
def MADI_ALIF(full, lex, extra=None, hidden=False, punct=None, note_ar="", note_en="", note_tr=""):
    """رَأَى، مَشَى، سَقَى، دَعَا: a past naqis verb built on an estimated fatha"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", ["thulathi-mujarrad-babs", "naqis-verbs"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ" + hid + note_ar + ".",
        en0 + "past verb built on a fatha estimated on the alif" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "elif üzerindeki takdîrî fetha ile mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def ENC_NOUN(full, lex, enc, role, extra=None, punct=None, note_ar="", note_en="", note_tr="", sign=None, segments=None):
    """a noun annexed to an enclitic pronoun in any seat: role = maful | fail | majr | mubtada | ismk | mudaf"""
    stem = full[:-len(enc)]
    head = {
        "maful": ("مَفْعُولٌ بِهِ مَنْصُوبٌ " + (sign or "بِالْفَتْحَةِ"), "The direct object, in nasb", "Mef'ûlün bih, mansûb", ["maful-bihi"]),
        "fail": ("فَاعِلٌ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "The doer, in raf'", "Fâil, merfû", ["fail"]),
        "majr": ("مَجْرُورٌ " + (sign or "بِالْكَسْرَةِ"), "In jarr after the letter", "Cer harfiyle mecrûr", ["huruf-jarr"]),
        "mubtada": ("مُبْتَدَأٌ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "The mubtada, in raf'", "Mübtedâ, merfû", ["mubtada-khabar"]),
        "ismk": ("اسْمُ كَانَ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "The noun of كَانَ, in raf'", "Kâne'nin ismi, merfû", ["kana-wa-akhawatuha"]),
        "mudaf": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ " + (sign or "بِالْكَسْرَةِ"), "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", ["idafa-definiteness"]),
    }[role]
    return tok(full, lex, "noun", head[3] + ["idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        head[0] + "، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        head[1] + "; annexed, and the attached pronoun is the second term of the idafa, in the seat of jarr" + note_en + ".",
        head[2] + "; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr" + note_tr + ".",
        punct=punct, segments=segments or [seg(stem, lex, "noun"), seg(enc, PRON[enc], "pron")])
def MADI_T(full, lex, who="anta", extra=None, punct=None, enc=None, note_ar="", note_en="", note_tr="", shart=False):
    """عَمِلْتَ، قَبِلْتُ: the ta of the doer; shart=True seats the verb as the condition's verb in the seat of jazm"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)] if enc else stem
    ta = {"anta": ("تَاءُ الْمُخَاطَبِ", "you"), "ana": ("تَاءُ الْمُتَكَلِّمِ", "I")}[who]
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    sh = ("، وَالْفِعْلُ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "; the verb stands in the seat of jazm as the verb of the condition", "; fiil, şart fiili olarak mahallen meczûm") if shart else ("", "", "")
    g = ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "fail"] + (["maful-bihi"] if enc else []) + (["in-shartiyya", "al-majzum-wal-shart-wal-jaza"] if shart else []) + (extra or [])
    segs = [s for s in [sg, seg(stem_v, lex, "verb"), (seg(enc, PRON[enc], "pron") if enc else None)] if s]
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَ" + ta[0] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + encs + sh[0] + note_ar + ".",
        en0 + "past verb built on sukun because the ta of the doer is attached; that ta («" + ta[1] + "») is the doer, in the seat of raf'" + ("; the attached pronoun after it is the object, in the seat of nasb" if enc else "") + sh[1] + note_en + ".",
        tr0 + "fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ fâildir, mahallen merfû" + ("; sonundaki bitişik zamir mef'ûlün bih, mahallen mansûb" if enc else "") + sh[2] + note_tr + ".",
        punct=punct, segments=segs if len(segs) > 1 else None)
def ENC_MADI(full, lex, enc, extra=None, punct=None, alif=False, hidden=False, fem=False, note_ar="", note_en="", note_tr=""):
    """سَأَلَهُمَا: a past verb with its enclitic object"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)]
    built = "مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ" if alif else "مَبْنِيٌّ عَلَى الْفَتْحِ"
    ta = "، وَالتَّاءُ لِلتَّأْنِيثِ" if fem else ""
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + ("هِيَ" if fem else "هُوَ") if hidden else ""
    g = ["al-bariz-al-muttasil", "maful-bihi"] + (["naqis-verbs"] if alif else []) + (extra or [])
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مَاضٍ " + built + ta + hid + "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note_ar + ".",
        en0 + "past verb built on fatha" + (" (estimated on the alif)" if alif else "") + (" (the ta marks the feminine)" if fem else "") + ("; the doer is a hidden pronoun" if hidden else "") + "; the attached pronoun is its object, in the seat of nasb" + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + (" (fetha elif üzerinde takdîrî)" if alif else "") + (" (tâ te'nîs içindir)" if fem else "") + ("; fâil gizli zamir" if hidden else "") + "; bitişik zamir mef'ûlün bih, mahallen mansûb" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem_v, lex, "verb"), seg(enc, PRON[enc], "pron")] if s])
def MUDARI(full, lex, extra=None, punct=None, who="هُوَ", enc=None, naqis=None, note_ar="", note_en="", note_tr="", wujub=False, segments=None):
    """a present verb in raf' with a hidden doer (naqis = 'ي' | 'و' | 'ا' for the estimated damma)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)] if enc else stem
    sign = {None: "بِالضَّمَّةِ", "ي": "بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "و": "بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ", "ا": "بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"}[naqis]
    sign_en = {None: "", "ي": " (the damma is estimated on the ya)", "و": " (the damma is estimated on the waw)", "ا": " (the damma is estimated on the alif)"}[naqis]
    sign_tr = {None: "", "ي": " (damme yâ üzerinde takdîrî)", "و": " (damme vâv üzerinde takdîrî)", "ا": " (damme elif üzerinde takdîrî)"}[naqis]
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ " + ("وُجُوبًا " if wujub else "") + "تَقْدِيرُهُ: " + who
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    g = ["mudari-marfu"] + (["naqis-verbs"] if naqis else []) + (["al-bariz-al-muttasil", "maful-bihi"] if enc else []) + (["al-fail-al-mudmar-al-mustatir-wujuban"] if wujub else []) + (extra or [])
    segs = segments or [s for s in [sg, seg(stem_v, lex, "verb"), (seg(enc, PRON[enc], "pron") if enc else None)] if s]
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign + hid + encs + note_ar + ".",
        en0 + "present verb in raf'" + sign_en + "; the doer is a hidden pronoun «" + who + "»" + ("; the attached pronoun is its object, in the seat of nasb" if enc else "") + note_en + ".",
        tr0 + "merfû muzâri" + sign_tr + "; fâil gizli zamir «" + who + "»" + ("; bitişik zamir mef'ûlün bih, mahallen mansûb" if enc else "") + note_tr + ".",
        punct=punct, segments=segs if len(segs) > 1 else None)
def MANSUB_AN(full, lex, extra=None, punct=None, who="هُوَ", enc=None, by="أَنْ", role_ar="", role_en="", role_tr="", note_ar="", note_en="", note_tr="", wujub=False, hidden=True):
    """يَقْتُلُوكَ، يَنْصُرَهُ، تَعْمَلَ: a present verb put in nasb by أَنْ (or by أَنْ hidden after حَتَّى / لِ)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)] if enc else stem
    hid = ("، وَالْفَاعِلُ مُسْتَتِرٌ " + ("وُجُوبًا " if wujub else "") + "تَقْدِيرُهُ: " + who) if hidden else "، وَالْفَاعِلُ بَعْدَهُ"
    hid_en = ("; the doer is a hidden pronoun «" + who + "»") if hidden else "; its doer follows"
    hid_tr = ("; fâil gizli zamir «" + who + "»") if hidden else "; fâili ondan sonra gelir"
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    g = ["nawasib-wa-jawazim-al-mudari"] + (["al-bariz-al-muttasil", "maful-bihi"] if enc else []) + (["al-fail-al-mudmar-al-mustatir-wujuban"] if wujub else []) + (extra or [])
    segs = [s for s in [sg, seg(stem_v, lex, "verb"), (seg(enc, PRON[enc], "pron") if enc else None)] if s]
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ" + by + " وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ" + hid + encs + role_ar + note_ar + ".",
        en0 + "present verb put in nasb by " + by + ", its sign the fatha" + hid_en + ("; the attached pronoun is its object, in the seat of nasb" if enc else "") + role_en + note_en + ".",
        tr0 + by + " ile mansûb muzâri, alâmeti fetha" + hid_tr + ("; bitişik zamir mef'ûlün bih, mahallen mansûb" if enc else "") + role_tr + note_tr + ".",
        punct=punct, segments=segs if len(segs) > 1 else None)
def AMR(full, lex, extra=None, punct=None, enc=None, built="السُّكُونِ", built_en="sukun", built_tr="sükûn", waw=False, wiqaya=False, note_ar="", note_en="", note_tr="", segments=None):
    """انْصُرْنِي، اخْرُجْ، اسْتَأْجِرْهُ، أَعْطِنِي، اجْلِسُوا: the imperative"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)] if enc else stem
    if wiqaya: stem_v = stem_v[:-2] if stem_v.endswith("نِ") else stem_v
    doer = ("، وَوَاوُ الْجَمَاعَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "; the waw of the group is its doer, in the seat of raf'", "; cemâat vâvı fâildir, mahallen merfû") if waw else \
           ("، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ", "; the doer «you» is a pronoun that must stay hidden", "; fâil «sen» — vücûben müstetir zamir")
    wq = ("، وَالنُّونُ لِلْوِقَايَةِ", "; the nun guards the verb's ending", "; nûn vikâye içindir") if wiqaya else ("", "", "")
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    g = ["imperative-amr"] + (["al-bariz-al-muttasil", "maful-bihi"] if enc else []) + (["ya-al-mutakallim"] if enc in ("نِي", "ي") else []) + (["al-fail-al-mudmar-al-mustatir-wujuban"] if not waw else ["al-bariz-al-muttasil"]) + (extra or [])
    segs = segments or ([s for s in [sg, seg(stem_v, lex, "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")] if s] if wiqaya else [s for s in [sg, seg(stem_v, lex, "verb"), (seg(enc, PRON[enc], "pron") if enc else None)] if s])
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى " + built + doer[0] + wq[0] + encs + note_ar + ".",
        en0 + "imperative built on " + built_en + doer[1] + wq[1] + ("; the attached pronoun is its object, in the seat of nasb" if enc else "") + note_en + ".",
        tr0 + built_tr + " üzere mebnî emir" + doer[2] + wq[2] + ("; bitişik zamir mef'ûlün bih, mahallen mansûb" if enc else "") + note_tr + ".",
        punct=punct, segments=segs if len(segs) > 1 else None)
def KHABAR(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="", sign="بِالضَّمَّةِ"):
    return tok(full, lex, "noun", ["mubtada-khabar"] + (extra or []), "خَبَرٌ مَرْفُوعٌ " + sign + note_ar + ".", "The predicate (khabar), in raf'" + note_en + ".", "Haber, merfû" + note_tr + ".", punct=punct)
def MUBTADA(full, lex, pos="noun", extra=None, punct=None, note_ar="", note_en="", note_tr="", sign="بِالضَّمَّةِ", segments=None):
    return tok(full, lex, pos, ["mubtada-khabar"] + (extra or []), "مُبْتَدَأٌ مَرْفُوعٌ " + sign + note_ar + ".", "The mubtada (subject of a nominal sentence), in raf'" + note_en + ".", "Mübtedâ, merfû" + note_tr + ".", punct=punct, segments=segments)
AN = lambda role_ar="", role_en="", role_tr="": tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ" + role_ar + ".", "The masdar-making أَنْ, which puts the verb in nasb" + role_en + ".", "Masdariyye ve nasb harfi en" + role_tr + ".")
AN_MAFUL = lambda: AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ", "; the clause it builds is the object of «wanted»", "; kurduğu müevvel masdar «istedi»nin mef'ûlüdür")
INNA = lambda punct=None: tok("إِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "إِنَّ «indeed» puts its noun in nasb and raises its predicate.", "Te'kîd ve nasb harfi inne: ismini nasb, haberini ref eder.", punct=punct)
WA_ISTINAF = ("الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "The waw opens a new clause; ", "Vâv isti'nâf içindir; ")
IN_SHART = lambda full="وَإِنْ": tok(full, "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], (WA_AR if full.startswith("وَ") else "") + "إِنْ حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ.", ("The waw conjoins; " if full.startswith("وَ") else "") + "the conditional إِنْ «if», which governs two verbs in jazm.", ("«ve» + " if full.startswith("وَ") else "") + "cezmeden şart harfi in: iki fiili cezmeder.", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")] if full.startswith("وَ") else None)

# ---- Chapter 1 — الْخُرُوجُ مِنْ مِصْرَ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Musa was living in the house of Pharaoh.", "tr": "Mûsâ Firavun'un evinde yaşıyordu."},
 "tokens": [KANA("كَانَ"), MUSA_ISMK(), MUDARI_KH("يَعِيشُ", "asha-live", ["hollow-verbs"]), PREP("فِي", "fi", gloss_tr="«-de»"),
  MAJR("بَيْتِ", "bayt", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2], punct=".")]})
S1.append({"id": "s2", "translation": {"en": "And Musa grew up and became a strong man.", "tr": "Mûsâ büyüdü ve güçlü bir adam oldu."},
 "tokens": [MADI("وَكَبِرَ", "kabira"), MUSA_F(), SARA("وَصَارَ"), KHK("رَجُلًا", "rajul"), NAAT("قَوِيًّا", "qawi", "nasb", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "One day Musa entered the city.", "tr": "Bir gün Mûsâ şehre girdi."},
 "tokens": [PREP("وَفِي", "fi", gloss_tr="«-de»"), MAJR("يَوْمٍ", "yawm"), MADI("دَخَلَ", "dakhala"), MUSA_F(), MAFUL("الْمَدِينَةَ", "madina", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "And he saw a man from Pharaoh's people striking a man from the Children of Israel.", "tr": "Firavun'un kavminden bir adamın İsrâiloğullarından bir adamı dövdüğünü gördü."},
 "tokens": [MADI_ALIF("فَرَأَى", "raa", ["maful-bihi"], hidden=True),
  MAFUL("رَجُلًا", "rajul"), PREP("مِنْ", "min", gloss_tr="«-den»"), MAJR("قَوْمِ", "qawm", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2]),
  MUDARI("يَضْرِبُ", "daraba", ["jumla-sifa"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِرَجُلًا (الْجُمَلُ بَعْدَ النَّكِرَاتِ صِفَاتٌ)", note_en="; the clause fills the seat of nasb as an adjective of «a man» (a clause after an indefinite noun is its adjective)", note_tr="; cümle, «bir adam»ın sıfatı olarak mahallen mansûbdur (nekreden sonraki cümleler sıfattır)"),
  MAFUL("رَجُلًا", "rajul"), PREP("مِنْ", "min", gloss_tr="«-den»"),
  tok("بَنِي", "banu", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "idafa-definiteness"], "مَجْرُورٌ بِالْيَاءِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "In jarr by the ya — a word treated like the sound masculine plural; its nun is dropped for the annexation.", "Yâ ile mecrûr — cem-i müzekker sâlime mülhak; izâfet için nûnu düşmüş, muzâf."),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2], punct=".")]})
S1.append({"id": "s5", "translation": {"en": "So the man said: «O Musa, help me!»", "tr": "Adam dedi ki: «Ey Mûsâ, bana yardım et!»"},
 "tokens": [QALA("فَقَالَ"), FAIL("الرَّجُلُ", "rajul", punct=":"), YA(),
  tok("مُوسَى", "musa", "propn", ["vocative-munada", "ism-maqsur-manqus"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on an estimated damma, in the seat of nasb.", "Münâdâ: müfred alem, elif üzerindeki takdîrî damme ile mebnî, mahallen mansûb.", punct="،"),
  AMR("انْصُرْنِي", "nasara", ["thulathi-mujarrad-babs"], enc="نِي", wiqaya=True, punct="!")]})
S1.append({"id": "s6", "translation": {"en": "So Musa struck the wrongdoing man, and he died.", "tr": "Mûsâ zâlim adama vurdu, adam da öldü."},
 "tokens": [MADI("فَضَرَبَ", "daraba"), MUSA_F(), MAFUL("الرَّجُلَ", "rajul"), NAAT("الظَّالِمَ", "zalim", "nasb", ["ism-fail"], punct="،"), MADI("فَمَاتَ", "mata-die", ["hollow-verbs"], hidden=True, punct=".")]})
S1.append({"id": "s7", "translation": {"en": "And Musa was greatly afraid.", "tr": "Mûsâ çok korktu."},
 "tokens": [MADI("وَخَافَ", "khafa", ["hollow-verbs"]), MUSA_F(),
  tok("خَوْفًا", "khawf", "noun", ["maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ خَافَ، يُؤَكِّدُ الْفِعْلَ.", "The absolute object (maf'ul mutlaq), in nasb — the masdar of its own verb, strengthening it.", "Mef'ûl-i mutlak, mansûb — kendi fiilinin masdarı; fiili te'kîd eder."),
  NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct=".")]})
S1.append({"id": "s8", "translation": {"en": "On the next day a man came to Musa.", "tr": "Ertesi gün bir adam Mûsâ'ya geldi."},
 "tokens": [PREP("وَفِي", "fi", gloss_tr="«-de»"), MAJR("الْيَوْمِ", "yawm"), tok("الثَّانِي", "thani", "noun", ["naat-sifa", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.", "An adjective in jarr by a kasra estimated on the ya — a manqus noun.", "Na't, yâ üzerindeki takdîrî kesre ile mecrûr — mankûs isim."),
  MADI("جَاءَ", "jaa", ["hollow-verbs"]), FAIL("رَجُلٌ", "rajul"), PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], sign="بِكَسْرَةٍ " + MUQ_ALIF[0], note_en=MUQ_ALIF[1], note_tr=MUQ_ALIF[2], punct=".")]})
S1.append({"id": "s9", "translation": {"en": "And he said: «O Musa, Pharaoh's people want to kill you, so leave the city.»", "tr": "Ve dedi ki: «Ey Mûsâ, Firavun'un kavmi seni öldürmek istiyor; şehirden çık.»"},
 "tokens": [QALA("وَقَالَ", hidden=True, punct=":"), YA(),
  tok("مُوسَى", "musa", "propn", ["vocative-munada", "ism-maqsur-manqus"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on an estimated damma, in the seat of nasb.", "Münâdâ: müfred alem, elif üzerindeki takdîrî damme ile mebnî, mahallen mansûb.", punct="،"),
  INNA(), tok("قَوْمَ", "qawm", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of إِنَّ, in nasb, annexed.", "İnne'nin ismi, mansûb, muzâf."),
  MUDAF_ILAYH("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2]),
  tok("يُرِيدُونَ", "arada", "verb", ["afal-khamsa", "inna-wa-akhawatuha", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "One of the five verbs, in raf' by the kept nun; the waw is its doer, and the clause fills the seat of raf' as the predicate of إِنَّ.", "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâildir — cümle, inne'nin haberi olarak mahallen merfûdur."),
  AN_MAFUL(),
  tok("يَقْتُلُوكَ", "qatala", "verb", ["afal-khamsa", "nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "Present verb put in nasb by أَنْ, its sign the dropped nun (one of the five verbs); the waw is its doer and the attached kaf «you» is its object.", "En ile mansûb muzâri, alâmeti nûnun düşmesi (ef'âl-i hamseden); vâv fâil, bitişik kâf «seni» mef'ûlün bih.", punct="،", segments=[seg("يَقْتُلُو", "qatala", "verb"), seg("كَ", "pron-2ms", "pron")]),
  AMR("فَاخْرُجْ", "kharaja", ["thulathi-mujarrad-babs"]), MINA(), MAJR("الْمَدِينَةِ", "madina", punct=".")]})
S1.append({"id": "s10", "translation": {"en": "So Musa left Egypt afraid.", "tr": "Mûsâ korku içinde Mısır'dan çıktı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja"), MUSA_F(), PREP("مِنْ", "min", gloss_tr="«-den»"),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F[0], note_en=DIPT_F[1], note_tr=DIPT_F[2]),
  HAL("خَائِفًا", "khaif", ["ism-fail"], punct=".")]})
S1.append({"id": "s11", "translation": {"en": "And he walked in the desert for many days.", "tr": "Ve çölde günlerce yürüdü."},
 "tokens": [MADI_ALIF("وَمَشَى", "masha", hidden=True),
  PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الصَّحْرَاءِ", "sahra"),
  tok("أَيَّامًا", "yawm", "noun", ["maful-fih", "jam-taksir"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ تَكْسِيرٍ لِيَوْمٍ.", "An adverb of time, in nasb — the broken plural of «day».", "Zaman zarfı, mansûb — «gün»ün cem-i mükesseri."),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct=".")]})

# ---- Chapter 2 — عِنْدَ الْبِئْرِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "Then Musa reached Madyan.", "tr": "Sonra Mûsâ Medyen'e ulaştı."},
 "tokens": [THUMMA(), MADI("وَصَلَ", "wasala", ["mithal-verbs"]), MUSA_F(), PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("مَدْيَنَ", "madyan", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2], punct=".")]})
S2.append({"id": "s2", "translation": {"en": "And there was a well near Madyan.", "tr": "Medyen'in yakınında bir kuyu vardı."},
 "tokens": [KANA("وَكَانَ"),
  tok("عِنْدَ", "inda", "noun", ["kana-wa-akhawatuha", "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ خَبَرُ كَانَ مُقَدَّمٌ.", "An adverb of place «at», in nasb and annexed — the adverb is the FRONTED predicate of كَانَ.", "«Yanında» — mekân zarfı, mansûb, muzâf — zarf, kâne'nin öne alınmış haberidir."),
  MUDAF_ILAYH("مَدْيَنَ", "madyan", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2]),
  ISMK("بِئْرٌ", "bir", muakhkhar=True, punct=".")]})
S2.append({"id": "s3", "translation": {"en": "And at the well he found many people watering their sheep.", "tr": "Kuyunun başında koyunlarını sulayan birçok insan buldu."},
 "tokens": [MADI("فَوَجَدَ", "wajada", ["mithal-verbs"], hidden=True), INDA(), MUDAF_ILAYH("الْبِئْرِ", "bir"), MAFUL("نَاسًا", "nas"),
  tok("كَثِيرِينَ", "kathir", "noun", ["naat-sifa", "jam-mudhakkar-salim"], "نَعْتٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "An adjective in nasb by the ya — a sound masculine plural.", "Na't, cem-i müzekker sâlim olduğu için yâ ile mansûb.", punct="،"),
  tok("يَسْقُونَ", "saqa-water", "verb", ["afal-khamsa", "naqis-verbs", "al-hal-jumla-wa-rabituha"], "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ نَاسًا (وَقِيلَ: نَعْتٌ).", "One of the five verbs, in raf' by the kept nun; the waw is its doer — the clause fills the seat of nasb as the hal of «people» (or, some say, their adjective).", "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâil — cümle, «insanlar»ın hâli olarak mahallen mansûb (sıfat da denmiştir)."),
  ENC_NOUN("غَنَمَهُمْ", "ghanam", "هُمْ", "maful", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "And there were two women there with their sheep.", "tr": "Orada koyunlarıyla birlikte iki kadın vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  tok("هُنَاكَ", "hunaka", "noun", ["kana-wa-akhawatuha", "asma-al-ishara", "maful-fih"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ — وَالظَّرْفُ خَبَرُ كَانَ مُقَدَّمٌ.", "The demonstrative of place «there», built on fatha, in the seat of nasb as an adverb — the adverb is the FRONTED predicate of كَانَ.", "Mekân için işaret ismi «orada», fetha üzere mebnî, mahallen mansûb zarf — zarf, kâne'nin öne alınmış haberidir."),
  ISMK("امْرَأَتَانِ", "imraa", extra=["al-muthanna"], sign="بِالْأَلِفِ لِأَنَّهُ مُثَنًّى", note_en=" — by the alif, a dual", note_tr=" — tesniye olduğu için elif ile", muakhkhar=True),
  MAA(), ENC_NOUN("غَنَمِهِمَا", "ghanam", "هِمَا", "mudaf", punct=".", segments=[seg("غَنَمِ", "ghanam", "noun"), seg("هِمَا", "pron-3d", "pron")])]})
S2.append({"id": "s5", "translation": {"en": "So Musa asked the two: «Why do you two not water your sheep?»", "tr": "Mûsâ ikisine sordu: «Niçin koyunlarınızı sulamıyorsunuz?»"},
 "tokens": [ENC_MADI("فَسَأَلَهُمَا", "saala", "هُمَا"), MUSA_F(punct=":"), LIMADHA(),
  tok("لَا", "la-nafiya", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ.", "The negating لَا, which governs nothing.", "Nefy harfi lâ; amel etmez."),
  tok("تَسْقِيَانِ", "saqa-water", "verb", ["afal-khamsa", "naqis-verbs", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "One of the five verbs, in raf' by the kept nun; the alif of the two is its doer, in the seat of raf'.", "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; tesniye elifi fâildir, mahallen merfû."),
  ENC_NOUN("غَنَمَكُمَا", "ghanam", "كُمَا", "maful", punct="؟")]})
S2.append({"id": "s6", "translation": {"en": "The two said: «We do not water until the shepherds leave, and our father is a weak old man.»", "tr": "İkisi dedi ki: «Çobanlar gidinceye kadar sulayamayız; babamız da güçsüz bir ihtiyardır.»"},
 "tokens": [tok("قَالَتَا", "qala", "verb", ["hollow-verbs", "al-muthanna", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "Past verb built on fatha; the ta marks the feminine, and the alif of the two is its doer, in the seat of raf'; what is said is its object.", "Fetha üzere mebnî mâzî; tâ te'nîs içindir, tesniye elifi fâildir — mahallen merfû; söylenen söz mef'ûlün bihtir.", punct=":", segments=[seg("قَالَتَ", "qala", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("لَا", "la-nafiya", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ.", "The negating لَا, which governs nothing.", "Nefy harfi lâ; amel etmez."),
  MUDARI("نَسْقِي", "saqa-water", who="نَحْنُ", naqis="ي", wujub=True),
  tok("حَتَّى", "hatta", "part", ["huruf-jarr", "an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهَا مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "حَتَّى «until»: a particle of end-point and jarr; the present verb after it is put in nasb by a hidden أَنْ.", "Hattâ «-inceye kadar»: gâye ve cer harfi; ondan sonraki muzâri gizli bir en ile mansûbdur."),
  MANSUB_AN("يَذْهَبَ", "dhahaba", by="أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", hidden=False),
  FAIL("الرُّعَاةُ", "rai", extra=["jam-taksir"], note_ar=" — جَمْعُ رَاعٍ", note_en=" — the broken plural of «shepherd»", note_tr=" — «çoban»ın cem-i mükesseri", punct="،"),
  tok("وَأَبُونَا", "ab", "noun", ["mubtada-khabar", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"], WA_ISTINAF[0] + "أَبُونَا مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", WA_ISTINAF[1] + "«our father» is the mubtada, in raf' by the waw as one of the five nouns; annexed to the pronoun «our», which fills the seat of jarr.", WA_ISTINAF[2] + "«babamız» mübtedâ, esmâ-i hamseden olduğu için vâv ile merfû; muzâf, «-mız» zamiri muzâfun ileyh — mahallen mecrûr.", segments=[seg("وَ", "wa", "conj"), seg("أَبُو", "ab", "noun"), seg("نَا", "pron-1p", "pron")]),
  KHABAR("شَيْخٌ", "shaykh"), NAAT("ضَعِيفٌ", "daif", "raf", ["sifa-mushabbaha"], punct=".")]})
S2.append({"id": "s7", "translation": {"en": "So Musa watered the sheep for the two of them.", "tr": "Bunun üzerine Mûsâ onlar için koyunları suladı."},
 "tokens": [MADI_ALIF("فَسَقَى", "saqa-water"), MUSA_F(),
  LAHU("لَهُمَا", "pron-3d", " («ikisine»)"), MAFUL("الْغَنَمَ", "ghanam", punct=".")]})
S2.append({"id": "s8", "translation": {"en": "Then he sat in the shade and called upon his Lord.", "tr": "Sonra gölgeye oturdu ve Rabbine duâ etti."},
 "tokens": [THUMMA(), MADI("جَلَسَ", "jalasa", hidden=True), PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الظِّلِّ", "zill"),
  MADI_ALIF("وَدَعَا", "daa", hidden=True),
  ENC_NOUN("رَبَّهُ", "rabb", "هُ", "maful", punct=".")]})
S2.append({"id": "s9", "translation": {"en": "And he said: «O my Lord, I am poor, so give me of Your good.»", "tr": "Ve dedi ki: «Ey Rabbim, ben fakirim; bana hayrından ver.»"},
 "tokens": [QALA("وَقَالَ", hidden=True, punct=":"), YA(),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ.", "The vocative annexed to the dropped ya of the speaker («my Lord»), in nasb by an estimated fatha; the kasra marks where the ya was.", "Hazfedilmiş mütekellim yâ'sına muzâf münâdâ («Rabbim»), takdîrî fetha ile mansûb; kesre yâ'nın delilidir.", punct="،"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «I», built on sukun, in the seat of raf' as mubtada.", "Munfasıl zamir «ben», sükûn üzere mebnî, mübtedâ olarak mahallen merfû."),
  KHABAR("فَقِيرٌ", "faqir", ["sifa-mushabbaha"], punct="،"),
  AMR("فَأَعْطِنِي", "aata", ["form-iv-verbs", "naqis-verbs"], enc="نِي", wiqaya=True, built="حَذْفِ حَرْفِ الْعِلَّةِ", built_en="the dropped weak letter", built_tr="illet harfinin hazfi", note_ar=" — وَالْفَاءُ لِلسَّبَبِيَّةِ", note_en=" (the fa marks the consequence)", note_tr=" (fâ sebebiyet içindir)"),
  PREP("مِنْ", "min", gloss_tr="«-den»"), ENC_NOUN("خَيْرِكَ", "khayr", "كَ", "majr", punct=".")]})

# ---- Chapter 3 — الشَّيْخُ الصَّالِحُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "Then one of the two came to Musa, shy as she walked.", "tr": "Sonra ikisinden biri utana utana Mûsâ'ya geldi."},
 "tokens": [THUMMA(), MADI("جَاءَتْ", "jaa", ["hollow-verbs"], fem=True),
  tok("إِحْدَاهُمَا", "ihda", "noun", ["fail", "ism-maqsur-manqus", "idafa-definiteness", "al-bariz-al-muttasil"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The doer «one of the two», in raf' by a damma estimated on the alif; annexed to the dual pronoun, which fills the seat of jarr.", "Fâil «ikisinden biri», elif üzerindeki takdîrî damme ile merfû; muzâf, tesniye zamiri muzâfun ileyh — mahallen mecrûr.", segments=[seg("إِحْدَا", "ihda", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], sign="بِكَسْرَةٍ " + MUQ_ALIF[0], note_en=MUQ_ALIF[1], note_tr=MUQ_ALIF[2]),
  tok("وَهِيَ", "hiya", "pron", ["al-hal-jumla-wa-rabituha", "mubtada-khabar"], "الْوَاوُ لِلْحَالِ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ، وَالْوَاوُ رَابِطُهَا.", "The waw of the hal, and «she» is a detached pronoun in the seat of raf' as mubtada — the nominal clause fills the seat of nasb as a hal, and the waw binds it.", "Hâl vâvı; «o» munfasıl zamir, mübtedâ — mahallen merfû; isim cümlesi hâl olarak mahallen mansûb, vâv da onun râbıtasıdır.", segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")]),
  MUDARI("تَسْتَحْيِي", "istahya", ["form-x-verbs", "mubtada-khabar"], who="هِيَ", naqis="ي", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en="; the clause is the predicate, in the seat of raf'", note_tr="; cümle haberdir — mahallen merfû", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "And she said: «My father invites you to our house.»", "tr": "Ve dedi ki: «Babam seni evimize çağırıyor.»"},
 "tokens": [QALAT("وَقَالَتْ", punct=":"),
  tok("أَبِي", "ab", "noun", ["mubtada-khabar", "five-nouns", "ya-al-mutakallim", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَأُفْرِدَ لِإِضَافَتِهِ إِلَى الْيَاءِ.", "The mubtada «my father», in raf' by a damma estimated before the ya of the speaker; annexed to that ya — one of the five nouns, which shows no letter-sign when annexed to the ya.", "Mübtedâ «babam», mütekellim yâ'sından önceki takdîrî damme ile merfû; yâ'ya muzâf — esmâ-i hamseden olup yâ'ya izâfetle harfle i'râbdan çıkar.", segments=[seg("أَبِ", "ab", "noun"), seg("ي", "pron-1s", "pron")]),
  MUDARI("يَدْعُوكَ", "daa", ["mubtada-khabar"], enc="كَ", naqis="و", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en="; the clause is the predicate, in the seat of raf'", note_tr="; cümle haberdir — mahallen merfû"),
  PREP("إِلَى", "ila", gloss_tr="«-e»"), ENC_NOUN("بَيْتِنَا", "bayt", "نَا", "majr", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "So Musa went with her to her father.", "tr": "Mûsâ onunla birlikte babasına gitti."},
 "tokens": [MADI("فَذَهَبَ", "dhahaba"), MUSA_F(), tok("مَعَهَا", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb, annexed to «her».", "«İle» — mekân zarfı, mansûb; «onun» zamirine muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("هَا", "pron-3fs", "pron")]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  tok("أَبِيهَا", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "In jarr by the ya, as one of the five nouns; annexed to «her».", "Esmâ-i hamseden olduğu için yâ ile mecrûr; «onun» zamirine muzâf.", punct=".", segments=[seg("أَبِي", "ab", "noun"), seg("هَا", "pron-3fs", "pron")])]})
S3.append({"id": "s4", "translation": {"en": "And her father was a righteous old man.", "tr": "Babası sâlih bir ihtiyardı."},
 "tokens": [KANA("وَكَانَ"),
  tok("أَبُوهَا", "ab", "noun", ["kana-wa-akhawatuha", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"], "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "The noun of كَانَ, in raf' by the waw as one of the five nouns; annexed to «her».", "Kâne'nin ismi, esmâ-i hamseden olduğu için vâv ile merfû; «onun» zamirine muzâf.", segments=[seg("أَبُو", "ab", "noun"), seg("هَا", "pron-3fs", "pron")]),
  KHK("شَيْخًا", "shaykh"), NAAT("صَالِحًا", "salih", "nasb", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "And Musa told him his story.", "tr": "Mûsâ ona hikâyesini anlattı."},
 "tokens": [MADI("فَقَصَّ", "qassa", ["doubled-verbs"]), MUSA_F(),
  tok("عَلَيْهِ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "A jarr letter; the attached pronoun «him» fills the seat of jarr.", "Cer harfi; bitişik zamir «ona» mahallen mecrûr.", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")]),
  ENC_NOUN("قِصَّتَهُ", "qissa", "هُ", "maful", punct=".")]})
S3.append({"id": "s6", "translation": {"en": "The old man said: «Do not fear, for you are far from Pharaoh and his people.»", "tr": "İhtiyar dedi ki: «Korkma; sen Firavun'dan ve kavminden uzaktasın.»"},
 "tokens": [QALA("فَقَالَ"), SHAYKH_F(punct=":"),
  tok("لَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "لَا النَّاهِيَةُ، حَرْفُ نَهْيٍ وَجَزْمٍ.", "The prohibitive لَا «do not», which governs jazm.", "Nehiy lâ'sı: nehiy ve cezm harfi."),
  tok("تَخَفْ", "khafa", "verb", ["nawasib-wa-jawazim-al-mudari", "la-nahiya", "hollow-verbs", "al-fail-al-mudmar-al-mustatir-wujuban"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "Present verb put in jazm by the prohibitive لَا, its sign the sukun; the hollow verb drops its middle letter where two sukuns meet; the doer «you» must stay hidden.", "Nehiy lâ'sı ile meczûm muzâri, alâmeti sükûn; ecvef fiilin orta harfi iki sâkin karşılaştığı için düşmüştür; fâil «sen» vücûben müstetir.", punct="،"),
  tok("فَأَنْتَ", "anta", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْفَاءُ لِلتَّعْلِيلِ، وَأَنْتَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The fa gives the reason; «you» is a detached pronoun, built, in the seat of raf' as mubtada.", "Fâ ta'lîl içindir; «sen» munfasıl zamir, mebnî, mübtedâ olarak mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("أَنْتَ", "anta", "pron")]),
  KHABAR("بَعِيدٌ", "baid", ["sifa-mushabbaha"]), PREP("عَنْ", "an", gloss_tr="«-den»"),
  MAJR("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2]),
  ATF("وَقَوْمِهِ", "qawm", case="jarr", extra=["idafa-definiteness", "al-bariz-al-muttasil"], note_ar="، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", note_en="; annexed to «his»", note_tr="; «onun» zamirine muzâf", punct=".", segments=[seg("وَ", "wa", "conj"), seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")])]})
S3.append({"id": "s7", "translation": {"en": "And one of the two girls said: «O my father, hire him, for he is a strong and trustworthy man.»", "tr": "İki kızdan biri dedi ki: «Babacığım, onu ücretle tut; o güçlü ve güvenilir bir adamdır.»"},
 "tokens": [QALAT("وَقَالَتْ", hidden=False),
  tok("إِحْدَى", "ihda", "noun", ["fail", "ism-maqsur-manqus", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ.", "The doer «one (of)», in raf' by a damma estimated on the alif; annexed.", "Fâil «biri», elif üzerindeki takdîrî damme ile merfû; muzâf."),
  MUDAF_ILAYH("الْبِنْتَيْنِ", "bint", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", note_en=" — by the ya, a dual", note_tr=" — tesniye olduğu için yâ ile", punct=":"),
  YA(), tok("أَبَتِ", "ab", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالتَّاءُ عِوَضٌ عَنْ يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَهِيَ مُضَافٌ إِلَيْهِ.", "The annexed vocative «my father», in nasb by an estimated fatha; the ta replaces the dropped ya of the speaker, which is the second term of the idafa.", "Muzâf münâdâ «babacığım», takdîrî fetha ile mansûb; tâ, hazfedilmiş mütekellim yâ'sının ivazıdır — o yâ muzâfun ileyhtir.", punct="،"),
  AMR("اسْتَأْجِرْهُ", "istajara", ["form-x-verbs"], enc="هُ", punct="،"),
  tok("فَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْفَاءُ لِلتَّعْلِيلِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The fa gives the reason; «he» is a detached pronoun, built, in the seat of raf' as mubtada.", "Fâ ta'lîl içindir; «o» munfasıl zamir, mebnî, mübtedâ olarak mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  KHABAR("رَجُلٌ", "rajul"), NAAT("قَوِيٌّ", "qawi", "raf", ["sifa-mushabbaha"]), NAAT("أَمِينٌ", "amin", "raf", ["sifa-mushabbaha"], note_ar=" — نَعْتٌ ثَانٍ", note_en=" — a second adjective", note_tr=" — ikinci na't", punct=".")]})

# ---- Chapter 4 — عَشْرُ سِنِينَ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "The old man said to Musa: «I want to marry you to one of my two daughters,»", "tr": "İhtiyar Mûsâ'ya dedi ki: «Seni iki kızımdan biriyle evlendirmek istiyorum;»"},
 "tokens": [QALA("فَقَالَ"), SHAYKH_F(),
  tok("لِمُوسَى", "li", "prep", ["huruf-jarr", "ism-maqsur-manqus"], "حَرْفُ جَرٍّ، وَمُوسَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "A jarr letter; Musa is in jarr by a kasra estimated on the alif.", "Cer harfi; Mûsâ elif üzerindeki takdîrî kesre ile mecrûr.", punct=":", segments=[seg("لِ", "li", "prep"), seg("مُوسَى", "musa", "propn")]),
  MUDARI("أُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"], who="أَنَا", wujub=True), AN_MAFUL(),
  MANSUB_AN("أُزَوِّجَكَ", "zawwaja", ["form-ii-verbs", "mafulayn"], who="أَنَا", enc="كَ", wujub=True, note_ar=" أَوَّلُ", note_en=" (the FIRST object)", note_tr=" (BİRİNCİ mef'ûl)"),
  tok("إِحْدَى", "ihda", "noun", ["maful-bihi", "mafulayn", "ism-maqsur-manqus", "idafa-definiteness"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ.", "The SECOND object «one (of)», in nasb by a fatha estimated on the alif; annexed.", "İKİNCİ mef'ûlün bih «biri», elif üzerindeki takdîrî fetha ile mansûb; muzâf."),
  tok("بِنْتَيَّ", "bint", "noun", ["idafa-definiteness", "al-muthanna", "ya-al-mutakallim", "al-bariz-al-muttasil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَيَاءُ الْمُتَكَلِّمِ مُضَافٌ إِلَيْهِ، وَأُدْغِمَتْ يَاءُ الْمُثَنَّى فِي يَاءِ الْمُتَكَلِّمِ.", "The second term of the idafa «my two daughters», in jarr by the ya as a dual; its nun is dropped for the annexation, and the ya of the speaker is annexed to it — the two yas merge.", "Muzâfun ileyh «iki kızım», tesniye olduğu için yâ ile mecrûr; izâfet için nûnu düşmüş, mütekellim yâ'sı ona muzâfun ileyh — iki yâ idgam edilmiştir.", punct="،", segments=[seg("بِنْتَيْ", "bint", "noun"), seg("يَ", "pron-1s", "pron")])]})
S4.append({"id": "s2", "translation": {"en": "«on condition that you work for me eight years.»", "tr": "«Bana sekiz yıl çalışman şartıyla.»"},
 "tokens": [PREP("عَلَى", "ala", role_ar="، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهَا فِي مَحَلِّ جَرٍّ — أَيْ: عَلَى شَرْطِ عَمَلِكَ", role_en="; the clause built by أَنْ after it fills the seat of jarr — «on (the condition of) your working»", role_tr="; ondan sonraki müevvel masdar mahallen mecrûr — «çalışman şartıyla»", gloss_tr="«üzerine»"),
  AN(), MANSUB_AN("تَعْمَلَ", "amila", who="أَنْتَ", wujub=True),
  tok("عِنْدِي", "inda", "noun", ["maful-fih", "ya-al-mutakallim", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَيَاءُ الْمُتَكَلِّمِ مُضَافٌ إِلَيْهِ.", "An adverb of place «with me», in nasb by a fatha that cannot appear because the ending carries the kasra the ya requires; annexed to the ya of the speaker.", "Mekân zarfı «yanımda», takdîrî fetha ile mansûb (son harf yâ'nın gerektirdiği kesreyle meşgûldür); mütekellim yâ'sına muzâf.", segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("ثَمَانِيَ", "thamani", "noun", ["asma-al-adad-fil-kafiya", "maful-fih", "idafa-definiteness", "ism-maqsur-manqus"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ (تَظْهَرُ الْفَتْحَةُ عَلَى يَاءِ الْمَنْقُوصِ)، مُضَافٌ — عَدَدٌ مُفْرَدٌ، وَمَعْدُودُهُ مُؤَنَّثٌ فَجَاءَ بِلَا تَاءٍ.", "An adverb of time «eight (years)», in nasb by a visible fatha (the fatha shows on the ya of a manqus); annexed — a simple number whose counted noun is feminine, so it takes no ta.", "Zaman zarfı «sekiz (yıl)», zâhir fetha ile mansûb (mankûsun yâ'sında fetha görünür); muzâf — müfred sayı; ma'dûdu müennes olduğundan tâ'sızdır."),
  tok("سِنِينَ", "sana", "noun", ["asma-al-adad-fil-kafiya", "idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — تَمْيِيزُ الْعَدَدِ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ جَمْعٌ مَجْرُورٌ بِالْإِضَافَةِ.", "The second term of the idafa «years», in jarr by the ya — a word treated like the sound masculine plural; the counted noun of three to ten is a plural in jarr by annexation.", "Muzâfun ileyh «yıllar», cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr — üçten ona kadar sayının ma'dûdu izâfetle mecrûr cemidir.", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "«And if you work ten years, that is better.»", "tr": "«On yıl çalışırsan, bu daha iyidir.»"},
 "tokens": [IN_SHART("وَإِنْ"), MADI_T("عَمِلْتَ", "amila", "anta", shart=True),
  tok("عَشْرَ", "ashr", "noun", ["asma-al-adad-fil-kafiya", "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — عَدَدٌ مُفْرَدٌ، وَمَعْدُودُهُ مُؤَنَّثٌ فَجَاءَ بِلَا تَاءٍ.", "An adverb of time «ten (years)», in nasb; annexed — a simple number whose counted noun is feminine, so it takes no ta.", "Zaman zarfı «on (yıl)», mansûb; muzâf — müfred sayı; ma'dûdu müennes olduğundan tâ'sızdır."),
  tok("سِنِينَ", "sana", "noun", ["asma-al-adad-fil-kafiya", "idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "The second term of the idafa «years», in jarr by the ya — a word treated like the sound masculine plural.", "Muzâfun ileyh «yıllar», cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr.", punct="،"),
  tok("فَذَلِكَ", "dhalika", "pron", ["al-fa-fi-jawab-al-shart", "asma-al-ishara", "mubtada-khabar", "al-majzum-wal-shart-wal-jaza"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَذَلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "The fa introduces the condition's answer; «that» is a demonstrative, built, in the seat of raf' as mubtada — the nominal clause fills the seat of jazm as the answer of the condition.", "Fâ, şartın cevabına gelmiştir; «bu» işaret ismi, mebnî, mübtedâ olarak mahallen merfû — isim cümlesi şartın cevabı olarak mahallen meczûm.", segments=[seg("فَ", "fa", "conj"), seg("ذَلِكَ", "dhalika", "pron")]),
  KHABAR("خَيْرٌ", "khayr", ["ism-tafdil"], note_ar=" — اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ: أَخْيَرُ", note_en=" — the elative «better», whose hamza is dropped", note_tr=" — ism-i tafdîl «daha hayırlı»; hemzesi düşmüştür", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "Musa said: «I accept.»", "tr": "Mûsâ dedi ki: «Kabul ettim.»"},
 "tokens": [QALA("قَالَ"), MUSA_F(punct=":"), MADI_T("قَبِلْتُ", "qabila", "ana", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "So the old man's daughter became a wife to Musa.", "tr": "Böylece ihtiyarın kızı Mûsâ'ya eş oldu."},
 "tokens": [SARA("فَصَارَتْ"), ISMK("بِنْتُ", "bint", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الشَّيْخِ", "shaykh"),
  KHK("زَوْجَةً", "zawja"),
  tok("لِمُوسَى", "li", "prep", ["huruf-jarr", "ism-maqsur-manqus"], "حَرْفُ جَرٍّ، وَمُوسَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "A jarr letter; Musa is in jarr by a kasra estimated on the alif.", "Cer harfi; Mûsâ elif üzerindeki takdîrî kesre ile mecrûr.", punct=".", segments=[seg("لِ", "li", "prep"), seg("مُوسَى", "musa", "propn")])]})
S4.append({"id": "s6", "translation": {"en": "And Musa worked for the old man ten years.", "tr": "Mûsâ ihtiyarın yanında on yıl çalıştı."},
 "tokens": [MADI("وَعَمِلَ", "amila"), MUSA_F(), INDA(), MUDAF_ILAYH("الشَّيْخِ", "shaykh"),
  tok("عَشْرَ", "ashr", "noun", ["asma-al-adad-fil-kafiya", "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of time «ten (years)», in nasb; annexed.", "Zaman zarfı «on (yıl)», mansûb; muzâf."),
  tok("سِنِينَ", "sana", "noun", ["asma-al-adad-fil-kafiya", "idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "The second term of the idafa «years», in jarr by the ya — a word treated like the sound masculine plural.", "Muzâfun ileyh «yıllar», cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr.", punct=".")]})
S4.append({"id": "s7", "translation": {"en": "And he used to tend the sheep in the desert.", "tr": "Çölde koyun güderdi."},
 "tokens": [KANA("وَكَانَ"), tok("يَرْعَى", "raa-pasture", "verb", ["kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ، وَاسْمُ كَانَ ضَمِيرٌ مُسْتَتِرٌ.", "Present verb in raf' by a damma estimated on the alif; its doer is a hidden pronoun, and the clause fills the seat of كَانَ's predicate (the noun of كَانَ is the hidden pronoun).", "Elif üzerindeki takdîrî damme ile merfû muzâri; fâili gizli zamir — cümle, kâne'nin haberi olarak mahallen mansûb (kâne'nin ismi gizli zamirdir)."),
  MAFUL("الْغَنَمَ", "ghanam"), PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الصَّحْرَاءِ", "sahra", punct=".")]})
S4.append({"id": "s8", "translation": {"en": "Then Musa wanted to return to Egypt.", "tr": "Sonra Mûsâ Mısır'a dönmek istedi."},
 "tokens": [THUMMA(), MADI("أَرَادَ", "arada", ["hollow-verbs", "form-iv-verbs"]), MUSA_F(), AN_MAFUL(), MANSUB_AN("يَرْجِعَ", "rajaa"),
  PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F[0], note_en=DIPT_F[1], note_tr=DIPT_F[2], punct=".")]})
S4.append({"id": "s9", "translation": {"en": "So he left Madyan with his family.", "tr": "Âilesiyle birlikte Medyen'den çıktı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja", hidden=True), PREP("مِنْ", "min", gloss_tr="«-den»"),
  MAJR("مَدْيَنَ", "madyan", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT[0], note_en=DIPT[1], note_tr=DIPT[2]),
  MAA(), ENC_NOUN("أَهْلِهِ", "ahl", "هِ", "mudaf", punct=".")]})
S4.append({"id": "s10", "translation": {"en": "And on the way he saw a fire on the mountain.", "tr": "Yolda dağın üzerinde bir ateş gördü."},
 "tokens": [PREP("وَفِي", "fi", gloss_tr="«-de»"), MAJR("الطَّرِيقِ", "tariq"),
  MADI_ALIF("رَأَى", "raa", ["maful-bihi"], hidden=True),
  MAFUL("نَارًا", "nar"), PREP("عَلَى", "ala", gloss_tr="«üzerinde»"), MAJR("الْجَبَلِ", "jabal", punct=".")]})
S4.append({"id": "s11", "translation": {"en": "He said to his family: «Sit here; I am going to the fire.»", "tr": "Âilesine dedi ki: «Burada oturun; ben ateşe gidiyorum.»"},
 "tokens": [QALA("فَقَالَ", hidden=True),
  tok("لِأَهْلِهِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَأَهْلِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The lam is a jarr letter; «family» is in jarr, annexed to «his».", "Lâm cer harfi; «âile» mecrûr, «onun» zamirine muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("أَهْلِ", "ahl", "noun"), seg("هِ", "pron-3ms", "pron")]),
  AMR("اجْلِسُوا", "jalasa", ["thulathi-mujarrad-babs"], waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi", segments=[seg("اجْلِسُو", "jalasa", "verb"), seg("ا", "pron-3mp", "pron")]),
  HUNA(punct="،"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «I», built on sukun, in the seat of raf' as mubtada.", "Munfasıl zamir «ben», sükûn üzere mebnî, mübtedâ olarak mahallen merfû."),
  MUDARI("أَذْهَبُ", "dhahaba", ["mubtada-khabar"], who="أَنَا", wujub=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en="; the clause is the predicate, in the seat of raf'", note_tr="; cümle haberdir — mahallen merfû"),
  PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("النَّارِ", "nar", punct=".")]})
S4.append({"id": "s12", "translation": {"en": "And there Musa became the messenger of Allah.", "tr": "Ve orada Mûsâ Allah'ın elçisi oldu."},
 "tokens": [tok("وَهُنَاكَ", "hunaka", "noun", ["asma-al-ishara", "maful-fih"], WA_AR + "هُنَاكَ اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", "The waw conjoins; «there» is the demonstrative of far place, built on fatha, in the seat of nasb as an adverb of place.", "«ve» + «orada» — uzak mekân için işaret ismi, fetha üzere mebnî; mahallen mansûb mekân zarfı.", segments=[seg("وَ", "wa", "conj"), seg("هُنَاكَ", "hunaka", "noun")]),
  SARA("صَارَ"), MUSA_ISMK(), KHK("رَسُولَ", "rasul", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), ALLAH_MI(punct=".")]})

TITLES = [
 {"ar": "الْخُرُوجُ مِنْ مِصْرَ", "en": "Leaving Egypt", "tr": "Mısır'dan Çıkış"},
 {"ar": "عِنْدَ الْبِئْرِ", "en": "At the Well", "tr": "Kuyunun Başında"},
 {"ar": "الشَّيْخُ الصَّالِحُ", "en": "The Righteous Old Man", "tr": "Sâlih İhtiyar"},
 {"ar": "عَشْرُ سِنِينَ", "en": "Ten Years", "tr": "On Yıl"},
]
CHAPS = [S1, S2, S3, S4]

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule), plus the four new words
PREF = ["musa-wal-khadir", "musa-wa-bani-israil", "musa-wa-firawn", "bad-al-amali", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
        "jumal-al-tadrib", "talkhis-al-miftah", "al-kafiya", "izhar-al-asrar", "aqaid-ahl-al-sunna", "wasiyyat-abi-hanifa"]
FORCE = {"amana": "yunus-wa-al-hut"}   # the verb آمَنَ (qisas-2's `amana` is the noun أَمَانَة — a key collision upstream)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF}
def find_gloss(k):
    if k in FORCE: return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    if k in FORCE and k in _M[FORCE[k]]: return _M[FORCE[k]][k]
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

NEW_GLOSS = {
 "khaif": {"lemma": "خَائِف", "root": "خ و ف", "pos": "noun", "gloss": {"en": "afraid, fearful (the ism fa'il of خَافَ)", "tr": "korkmuş, korkan (خَافَ fiilinin ism-i fâili)"}, "level": 1},
 "rai": {"lemma": "رَاعٍ", "root": "ر ع ي", "pos": "noun", "plural": "رُعَاة", "gloss": {"en": "a shepherd (a manqus noun; pl. رُعَاة)", "tr": "çoban (mankûs isim; ç. رُعَاة)"}, "level": 2},
 "istajara": {"lemma": "اِسْتَأْجَرَ", "root": "أ ج ر", "pos": "verb", "form": "X", "gloss": {"en": "to hire, to take into one's pay (اِسْتَأْجَرَ يَسْتَأْجِرُ)", "tr": "ücretle tutmak, kiralamak (اِسْتَأْجَرَ يَسْتَأْجِرُ)"}, "level": 2},
 "thamani": {"lemma": "ثَمَانِي", "root": "ث م ن", "pos": "noun", "gloss": {"en": "eight — the form used before a feminine counted noun (ثَمَانِي سِنِينَ); shaped like a manqus noun, its ya keeps a visible fatha in nasb", "tr": "sekiz — müennes ma'dûddan önceki şekli (ثَمَانِي سِنِينَ); mankûs isim şeklinde, nasbda yâ'sında fetha görünür"}, "level": 2},
}
used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k)
    if e is None: missing.append(k)
    else: GLOSS[k] = e
assert not missing, missing

MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = find_verb(k)
    if v: MORPH["verbs"][k] = v
MORPH["verbs"]["istajara"] = _sg.derived(_sg.B10, "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ", "اِسْتَأْجَر", "سْتَأْجِر", "اِسْتَأْجِر", "اِسْتِئْجَار", "مُسْتَأْجِر", maful="مُسْتَأْجَر", pmz="اُسْتُؤْجِرَ", pmd="يُسْتَأْجَرُ")
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": "musa-fi-madyan",
 "storyGroup": "musa-wa-firawn",
 "title": {"ar": "مُوسَى فِي مَدْيَنَ", "en": "Musa in Madyan", "tr": "Mûsâ Medyen'de"},
 "subtitle": {"ar": "قِصَّةُ الْهِجْرَةِ إِلَى مَدْيَنَ لِلْمُبْتَدِئِينَ — الْبِئْرُ، وَالشَّيْخُ الصَّالِحُ، وَعَشْرُ سِنِينَ",
              "en": "The flight to Madyan, for beginners — the well, the righteous old man, the ten years",
              "tr": "Yeni başlayanlar için Medyen'e hicret kıssası — kuyu, sâlih ihtiyar, on yıl"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-08",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": ["musa-wa-firawn", "musa-wa-bani-israil", "musa-wal-khadir"],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِقِصَّةِ مُوسَى فِي مَدْيَنَ كَمَا تُرْوَى لِلْأَطْفَالِ (عَلَى ضَوْءِ سُورَةِ الْقَصَصِ، الْآيَاتِ ١٤–٢٩)، عَلَى طَرِيقَةِ الْقِرَاءَةِ الْمُتَدَرِّجَةِ لِلنَّدْوِيِّ. لَمْ تُنْقَلْ آيَةٌ بِنَصِّهَا، وَلَا يُسْتَشْهَدُ بِجُمْلَةٍ هُنَا عَلَى أَنَّهَا نَصٌّ تُرَاثِيٌّ. الرَّابِعَةُ مِنْ قِصَصِ مُوسَى فِي هٰذَا الْبَرْنَامَجِ، كُتِبَتْ لِلْحَالِ وَالنِّدَاءِ وَالْمُثَنَّى الْمُؤَنَّثِ وَالْعَدَدِ وَلَا النَّاهِيَةِ وَالشَّرْطِ.",
  "en": "ORIGINAL Level-1 graded Arabic: the story of Musa in Madyan as it is told to children (after the Qurʾānic narrative in al-Qaṣaṣ 14–29), composed editorially in the manner of Nadwī's graded readers — short كَانَ-framed sentences, one event per line, the vocabulary repeated. No āya is quoted verbatim; no sentence here may be cited as a classical text. The fourth of the Musa stories in this programme, written to meet the hal, the vocative, the feminine dual, the number with its counted noun, the prohibitive لَا and the conditional إِنْ.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Mûsâ'nın Medyen kıssasının çocuklara anlatıldığı şekli (Kasas sûresi 14–29. âyetlerindeki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde telif edilmiştir — kısa, kâne ile kurulu cümleler, her satırda bir olay, tekrar eden kelime hazinesi. Hiçbir âyet aynen aktarılmamıştır; buradaki hiçbir cümle klasik bir metin olarak kaynak gösterilemez. Bu programdaki Mûsâ kıssalarının dördüncüsü; hâl, nidâ, müennes tesniye, sayı ve ma'dûdu, nehiy lâ'sı ve şart için yazıldı.",
  "reviewStatus": "pending-scholarly-review",
 },
}

(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
