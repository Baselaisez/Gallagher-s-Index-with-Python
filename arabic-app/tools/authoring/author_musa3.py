# -*- coding: utf-8 -*-
"""Author content/samples/musa-wal-khadir — «مُوسَى وَالْخَضِرُ», the third ORIGINAL Level-1 story of the Mūsā group (wave 86).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Mūsā and al-Khiḍr (al-Kahf 60–82)
as it is commonly retold to children. No āya is quoted; no sentence here may be cited as a classical text. Four chapters,
thirty-nine sentences. Every token carries trilingual iʿrāb. Verb paradigms and glossary entries are COPIED from the
packages that already own the lemma (the lemma-identity rule); only الْخَضِر, خَرَقَ and الصَّخْرَة are new to the corpus.

    QISSA_PKG_ROOT=<dir> python3 author_musa3.py     # a dry run writes under <dir>/musa-wal-khadir
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "musa-wal-khadir"
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

# ============ «مُوسَى وَالْخَضِرُ» — the third story: four chapters ============
MUSA_F = lambda punct=None: FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0], punct=punct)
ALLAH_F = lambda punct=None: FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl", punct=punct)
KHADIR_F = lambda punct=None: FAIL("الْخَضِرُ", "khadir", "propn", [], punct=punct)
KHADIR_M = lambda punct=None: MAFUL("الْخَضِرَ", "khadir", "propn", [], punct=punct)
QALA = lambda full="وَقَالَ", hidden=False, punct=None: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=punct)
PRON = {"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمَا": "pron-3d", "كَ": "pron-2ms", "نِي": "pron-1s", "ي": "pron-1s", "نَا": "pron-1p"}
PRON_AR = {"هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "هَا": "هَا", "هُمَا": "هُمَا", "كَ": "الْكَافُ", "نِي": "الْيَاءُ", "ي": "الْيَاءُ", "نَا": "نَا"}
def LAHU(full, pron, pron_tr, punct=None, grammar=None):
    return tok(full, "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + (grammar or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "The lam is a jarr letter; the attached pronoun fills the seat of jarr.", "Lâm cer harfi; bitişik zamir mahallen mecrûr" + pron_tr + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg(full[1:], pron, "pron")])
def DUAL_MADI(full, lex, extra=None, punct=None, naqis=False, note_ar="", note_en="", note_tr=""):
    """أَخَذَا، رَكِبَا، نَسِيَا: the alif of the two is the doer"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    built = "مَبْنِيٌّ عَلَى الْفَتْحِ" if not naqis else "مَبْنِيٌّ عَلَى الْفَتْحِ (رُدَّتِ الْأَلِفُ إِلَى أَصْلِهَا الْيَاءِ قَبْلَ أَلِفِ الِاثْنَيْنِ)"
    return tok(full, lex, "verb", ["thulathi-mujarrad-babs", "al-muthanna", "al-bariz-al-muttasil"] + (["naqis-verbs"] if naqis else []) + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ " + built + "، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note_ar + ".",
        en0 + "past verb built on fatha" + (" (the final alif returns to its original ya before the alif of the two)" if naqis else "") + "; the alif of the two is its doer, an attached pronoun in the seat of raf'" + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + (" (tesniye elifinden önce sondaki elif aslı olan yâ'ya döner)" if naqis else "") + "; tesniye elifi fâildir — bitişik zamir, mahallen merfû" + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def MADI_T(full, lex, who="anta", extra=None, punct=None, enc=None, note_ar="", note_en="", note_tr=""):
    """خَرَقْتَ، قُلْتُ، خَرَقْتُهَا: the ta of the doer, with an optional enclitic object"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)] if enc else stem
    ta = {"anta": ("تَاءُ الْمُخَاطَبِ", "you"), "ana": ("تَاءُ الْمُتَكَلِّمِ", "I")}[who]
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    g = ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "fail"] + (["maful-bihi"] if enc else []) + (extra or [])
    segs = [s for s in [sg, seg(stem_v, lex, "verb"), (seg(enc, PRON[enc], "pron") if enc else None)] if s]
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَ" + ta[0] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + encs + note_ar + ".",
        en0 + "past verb built on sukun because the ta of the doer is attached; that ta («" + ta[1] + "») is the doer, in the seat of raf'" + ("; the attached pronoun after it is the object, in the seat of nasb" if enc else "") + note_en + ".",
        tr0 + "fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ fâildir, mahallen merfû" + ("; sonundaki bitişik zamir mef'ûlün bih, mahallen mansûb" if enc else "") + note_tr + ".",
        punct=punct, segments=segs if len(segs) > 1 else None)
def ENC_MADI(full, lex, enc, extra=None, punct=None, first=False, alif=False, hidden=False, note_ar="", note_en="", note_tr=""):
    """عَلَّمَهُ، أَعْطَاهُمَا، أَخَذَهُ: a past verb with its enclitic object (first=True when a second object follows)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)]
    built = "مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ" if alif else "مَبْنِيٌّ عَلَى الْفَتْحِ"
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    g = ["al-bariz-al-muttasil", "maful-bihi"] + (["mafulayn"] if first else []) + (["naqis-verbs"] if alif else []) + (extra or [])
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مَاضٍ " + built + hid + "، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + (" أَوَّلُ" if first else "") + note_ar + ".",
        en0 + "past verb built on fatha" + (" (estimated on the alif)" if alif else "") + ("; the doer is a hidden pronoun" if hidden else "") + "; the attached pronoun is its " + ("FIRST object" if first else "object") + ", in the seat of nasb" + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + (" (fetha elif üzerinde takdîrî)" if alif else "") + ("; fâil gizli zamir" if hidden else "") + "; bitişik zamir " + ("BİRİNCİ mef'ûlün bih" if first else "mef'ûlün bih") + ", mahallen mansûb" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem_v, lex, "verb"), seg(enc, PRON[enc], "pron")] if s])
def MAFUL2(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    return tok(full, lex, "noun", ["maful-bihi", "mafulayn"] + (extra or []),
        "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ" + note_ar + ".", "The SECOND object, in nasb" + note_en + ".", "İKİNCİ mef'ûlün bih, mansûb" + note_tr + ".", punct=punct)
def ZARF(full, lex, kind="مَكَانٍ", extra=None, punct=None, note_ar="", note_en="", note_tr="", segments=None):
    return tok(full, lex, "noun", ["maful-fih"] + (extra or []),
        "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ" + note_ar + ".", "An adverb of " + ("place" if kind == "مَكَانٍ" else "time") + ", in nasb" + note_en + ".", ("Mekân" if kind == "مَكَانٍ" else "Zaman") + " zarfı, mansûb" + note_tr + ".", punct=punct, segments=segments)
LAN = lambda: tok("لَنْ", "lan", "part", ["nawasib-wa-jawazim-al-mudari", "nawasib-al-mudari-fil-kafiya"], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "لَنْ negates the future and puts the verb in nasb.", "Len: istikbâli nefyeder ve fiili nasb eder.")
def TASBIR(punct=None, who="أَنْتَ"):
    return tok("تَصْبِرَ", "sabara", "verb", ["nawasib-wa-jawazim-al-mudari", "al-fail-al-mudmar-al-mustatir-wujuban"],
        "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: " + who + ".",
        "Present verb put in nasb by لَنْ, its sign the fatha; the doer «you» is a pronoun that must stay hidden.",
        "Len ile mansûb muzâri, alâmeti fetha; fâil «sen» — vücûben müstetir zamir.", punct=punct)
MAI = lambda punct=None: tok("مَعِي", "maa", "noun", ["maful-fih", "ya-al-mutakallim", "idafa-definiteness"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَيَاءُ الْمُتَكَلِّمِ مُضَافٌ إِلَيْهِ.",
    "An adverb of place «with me», in nasb by an estimated fatha (the kasra before the ya of the speaker takes its place); the ya is the second term of the idafa.",
    "«Benimle» — mekân zarfı, takdîrî fetha ile mansûb (mütekellim yâ'sına uyan kesre yerini tutar); yâ muzâfun ileyhtir.", punct=punct, segments=[seg("مَعِ", "maa", "noun"), seg("ي", "pron-1s", "pron")])
INNAKA = lambda punct=None: tok("إِنَّكَ", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"],
    "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُهَا.",
    "إِنَّ is the verb-like particle; the attached «you» is its noun in the seat of nasb — the clause after it is its predicate, in the seat of raf'.",
    "İnne, fiile benzeyen harf; bitişik «sen» zamiri ismidir, mahallen mansûb — sonraki cümle haberi, mahallen merfû.", punct=punct, segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")])
LIMADHA = lambda: tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "The lam is a jarr letter; مَاذَا «what» is an interrogative noun, built, in the seat of jarr: «for what? why?».", "Lâm cer harfi; «mâzâ» soru ismi, mebnî, mahallen mecrûr: «niçin?».")
HUNAKA = lambda punct=None: tok("هُنَاكَ", "hunaka", "noun", ["asma-al-ishara", "maful-fih"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", "The demonstrative of far place «there», built on fatha, in the seat of nasb as an adverb of place.", "«Orada» — uzak mekân için işaret ismi, fetha üzere mebnî, mekân zarfı olarak mahallen mansûb.", punct=punct)
def AMMA(full, lex, punct=None):
    """أَمَّا السَّفِينَةُ: the particle of detailing and its mubtada"""
    return [tok(full, "amma", "part", ["amma-tafsiliyya", "amma-fil-kafiya"], ("الْوَاوُ عَاطِفَةٌ، وَ" if full.startswith("وَ") else "") + "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ، وَجَوَابُهَا مَقْرُونٌ بِالْفَاءِ.", ("The waw conjoins; " if full.startswith("وَ") else "") + "أَمَّا «as for» is the particle of condition and detailing; its answer is tied to the fa.", ("«ve» + " if full.startswith("وَ") else "") + "«…-e gelince» — şart ve tafsîl harfi emmâ; cevabı fâ ile bağlanır.", segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")] if full.startswith("وَ") else None),
            tok(lex[0], lex[1], "noun", ["mubtada-khabar", "amma-tafsiliyya"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَجُمْلَةُ الْجَوَابِ خَبَرُهُ.", "The mubtada, in raf' — the clause of the answer is its predicate.", "Mübtedâ, merfû — cevap cümlesi haberidir.", punct=punct)]
def FAKANA(punct=None, fem=False):
    ta = "، وَالتَّاءُ لِلتَّأْنِيثِ" if fem else ""
    return tok("فَكَانَتْ" if fem else "فَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "amma-tafsiliyya", "hollow-verbs"],
        "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + ta + ".",
        "The fa answers أَمَّا; كَانَ is the defective past verb that raises its noun and puts its predicate in nasb" + (" (the ta marks the feminine)" if fem else "") + ".",
        "Fâ, emmâ'nın cevabına gelmiştir; kâne nâkıs mâzî: ismini ref, haberini nasb eder" + (" (tâ te'nîs içindir)" if fem else "") + ".", punct=punct, segments=[seg("فَ", "fa", "conj"), seg("كَانَتْ" if fem else "كَانَ", "kana", "verb")])

# ---- Chapter 1 — الْعَبْدُ الصَّالِحُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Al-Khidr was a righteous servant.", "tr": "Hızır sâlih bir kul idi."},
 "tokens": [KANA("كَانَ"), ISMK("الْخَضِرُ", "khadir", "propn"), KHK("عَبْدًا", "abd"), NAAT("صَالِحًا", "salih", "nasb", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "And Allah taught him much knowledge.", "tr": "Ve Allah ona çok ilim öğretti."},
 "tokens": [ENC_MADI("وَعَلَّمَهُ", "allama", "هُ", ["form-ii-verbs"], first=True), ALLAH_F(), MAFUL2("عِلْمًا", "ilm"), NAAT("كَثِيرًا", "kathir", "nasb", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "And Musa wanted to follow him.", "tr": "Ve Mûsâ ona tâbi olmak istedi."},
 "tokens": [MADI("وَأَرَادَ", "arada", ["hollow-verbs", "form-iv-verbs"]), MUSA_F(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ.", "The masdar-making أَنْ puts the verb in nasb; the clause it builds is the object of «wanted».", "Masdariyye en: fiili nasb eder; kurduğu müevvel masdar «istedi»nin mef'ûlüdür."),
  tok("يَتْبَعَهُ", "tabia-follow", "verb", ["nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "Present verb put in nasb by أَنْ, its sign the fatha; the doer «he» is hidden; the attached «him» is the object.", "En ile mansûb muzâri, alâmeti fetha; fâil «o» gizli zamir; bitişik «onu» mef'ûlün bihtir.", punct=".", segments=[seg("يَتْبَعَ", "tabia-follow", "verb"), seg("هُ", "pron-3ms", "pron")])]})
S1.append({"id": "s4", "translation": {"en": "So Musa went to the sea with his young servant Yusha.", "tr": "Bunun üzerine Mûsâ genç hizmetkârı Yûşa ile denize gitti."},
 "tokens": [MADI("فَذَهَبَ", "dhahaba"), MUSA_F(), PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("الْبَحْرِ", "bahr"),
  tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of place «with», in nasb and annexed.", "«ile» — mekân zarfı, mansûb, muzâf."),
  tok("فَتَاهُ", "fata-youth", "noun", ["idafa-definiteness", "ism-maqsur-manqus", "al-bariz-al-muttasil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The second term of the idafa, in jarr by a kasra estimated on the alif; itself annexed to «his».", "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr; kendisi de «onun» zamirine muzâf.", segments=[seg("فَتَا", "fata-youth", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("يُوشَعَ", "yusha", "propn", ["badal", "mamnu-min-sarf"], "بَدَلٌ مِنْ فَتَاهُ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "A substitute (badal) for «his young servant», in jarr by fatha in place of kasra — a foreign proper name, barred from tanwin.", "«Genç hizmetkârı»ndan bedel, kesre yerine fetha ile mecrûr — yabancı özel isim, gayr-i munsarif.", punct=".")]})
S1.append({"id": "s5", "translation": {"en": "And the two of them took a fish with them.", "tr": "Ve ikisi yanlarına bir balık aldılar."},
 "tokens": [DUAL_MADI("وَأَخَذَا", "akhadha"),
  tok("مَعَهُمَا", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb and annexed to «the two of them».", "«İkisiyle» — mekân zarfı, mansûb, «o ikisi» zamirine muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  MAFUL("حُوتًا", "hut", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "But the two forgot the fish at the rock.", "tr": "Fakat ikisi balığı kayanın yanında unuttular."},
 "tokens": [DUAL_MADI("فَنَسِيَا", "nasiya", naqis=True), MAFUL("الْحُوتَ", "hut"),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of place «at», in nasb and annexed.", "«Yanında» — mekân zarfı, mansûb, muzâf."),
  MUDAF_ILAYH("الصَّخْرَةِ", "sakhra", punct=".")]})
S1.append({"id": "s7", "translation": {"en": "And Musa found al-Khidr there.", "tr": "Ve Mûsâ Hızır'ı orada buldu."},
 "tokens": [MADI("وَوَجَدَ", "wajada", ["mithal-verbs"]), MUSA_F(), KHADIR_M(), HUNAKA(punct=".")]})
S1.append({"id": "s8", "translation": {"en": "So Musa said to him: «Teach me some of your knowledge.»", "tr": "Mûsâ ona dedi ki: «Bana ilminden öğret.»"},
 "tokens": [QALA("فَقَالَ"), LAHU("لَهُ", "pron-3ms", " («ona»)"), MUSA_F(punct=":"),
  tok("عَلِّمْنِي", "allama", "verb", ["imperative-amr", "form-ii-verbs", "al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "An imperative built on sukun; the doer «you» must stay hidden; the nun guards the verb's ending, and the ya «me» is the object, in the seat of nasb.", "Sükûn üzere mebnî emir; fâil «sen» vücûben müstetir; nûn vikâye nûnu; yâ «beni» mef'ûlün bih, mahallen mansûb.", segments=[seg("عَلِّمْ", "allama", "verb"), seg("نِي", "pron-1s", "pron")]),
  PREP("مِنْ", "min", gloss_tr="«-den»"),
  tok("عِلْمِكَ", "ilm", "noun", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "In jarr after the letter; annexed to «your».", "Cer harfiyle mecrûr; «senin» zamirine muzâf.", punct=".", segments=[seg("عِلْمِ", "ilm", "noun"), seg("كَ", "pron-2ms", "pron")])]})

# ---- Chapter 2 — السَّفِينَةُ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "Al-Khidr said: «You will never be patient with me.»", "tr": "Hızır dedi ki: «Sen benimle asla sabredemeyeceksin.»"},
 "tokens": [QALA("قَالَ"), KHADIR_F(punct=":"), INNAKA(), LAN(), TASBIR(), MAI(punct=".")]})
S2.append({"id": "s2", "translation": {"en": "Musa said: «I shall be patient, if Allah wills.»", "tr": "Mûsâ dedi ki: «İnşallah sabredeceğim.»"},
 "tokens": [QALA("قَالَ"), MUSA_F(punct=":"),
  tok("سَوْفَ", "sawfa", "part", ["mudari-marfu"], "حَرْفُ اسْتِقْبَالٍ وَتَنْفِيسٍ.", "The particle of the (far) future.", "İstikbâl harfi «-ecek»."),
  tok("أَصْبِرُ", "sabara", "verb", ["mudari-marfu", "al-fail-al-mudmar-al-mustatir-wujuban"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.", "Present verb in raf' by the damma; the doer «I» must stay hidden.", "Damme ile merfû muzâri; fâil «ben» vücûben müstetir."),
  tok("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "The conditional إِنْ, which governs jazm.", "Cezmeden şart harfi in."),
  tok("شَاءَ", "shaa", "verb", ["in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "Past verb built on fatha, in the seat of jazm as the verb of the condition; its answer is omitted, shown by what came before.", "Fetha üzere mebnî mâzî, şart fiili olarak mahallen meczûm; cevabı önceki sözden anlaşıldığı için hazfedilmiştir."),
  ALLAH_F(punct=".")]})
S2.append({"id": "s3", "translation": {"en": "Then the two boarded a ship.", "tr": "Sonra ikisi bir gemiye bindiler."},
 "tokens": [tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."), DUAL_MADI("رَكِبَا", "rakiba"), MAFUL("سَفِينَةً", "safina", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "And al-Khidr tore a hole in the ship.", "tr": "Ve Hızır gemiyi deldi."},
 "tokens": [MADI("فَخَرَقَ", "kharaqa"), KHADIR_F(), MAFUL("السَّفِينَةَ", "safina", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "So Musa said: «Why did you tear the ship?»", "tr": "Mûsâ dedi ki: «Gemiyi niçin deldin?»"},
 "tokens": [QALA("فَقَالَ"), MUSA_F(punct=":"), LIMADHA(), MADI_T("خَرَقْتَ", "kharaqa", "anta"), MAFUL("السَّفِينَةَ", "safina", punct="؟")]})
S2.append({"id": "s6", "translation": {"en": "Al-Khidr said: «I told you: you will never be patient.»", "tr": "Hızır dedi ki: «Sana demiştim: asla sabredemeyeceksin.»"},
 "tokens": [QALA("قَالَ"), KHADIR_F(punct=":"), MADI_T("قُلْتُ", "qala", "ana", ["hollow-verbs"], note_ar="، وَحُذِفَتْ عَيْنُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" (the hollow verb drops its middle letter before the ta)", note_tr=" (ecvef fiil, tâ'dan önce orta harfini düşürür)"),
  LAHU("لَكَ", "pron-2ms", " («sana»)", punct=":"), LAN(), TASBIR(punct=".")]})
S2.append({"id": "s7", "translation": {"en": "So Musa was patient and fell silent.", "tr": "Bunun üzerine Mûsâ sabretti ve sustu."},
 "tokens": [MADI("فَصَبَرَ", "sabara"), MUSA_F(), MADI("وَسَكَتَ", "sakata", hidden=True, punct=".")]})

# ---- Chapter 3 — الْغُلَامُ وَالْجِدَارُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "Then the two left the ship.", "tr": "Sonra ikisi gemiden çıktılar."},
 "tokens": [tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."), DUAL_MADI("خَرَجَا", "kharaja"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter, voweled with fatha before the following ال.", "«-den» — cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("السَّفِينَةِ", "safina", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "And the two saw a boy on the road.", "tr": "Ve ikisi yolda bir oğlan gördüler."},
 "tokens": [DUAL_MADI("فَرَأَيَا", "raa", naqis=True), MAFUL("غُلَامًا", "ghulam"), PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الطَّرِيقِ", "tariq", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "And al-Khidr killed the boy.", "tr": "Ve Hızır oğlanı öldürdü."},
 "tokens": [MADI("فَقَتَلَ", "qatala"), KHADIR_F(), MAFUL("الْغُلَامَ", "ghulam", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "So Musa became angry and said: «Why did you kill the boy?»", "tr": "Mûsâ öfkelendi ve dedi ki: «Oğlanı niçin öldürdün?»"},
 "tokens": [MADI("فَغَضِبَ", "ghadiba"), MUSA_F(), QALA("وَقَالَ", hidden=True, punct=":"), LIMADHA(), MADI_T("قَتَلْتَ", "qatala", "anta"), MAFUL("الْغُلَامَ", "ghulam", punct="؟")]})
S3.append({"id": "s5", "translation": {"en": "Al-Khidr said: «You will never be patient with me.»", "tr": "Hızır dedi ki: «Sen benimle asla sabredemeyeceksin.»"},
 "tokens": [QALA("قَالَ"), KHADIR_F(punct=":"), LAN(), TASBIR(), MAI(punct=".")]})
S3.append({"id": "s6", "translation": {"en": "Then the two entered a village.", "tr": "Sonra ikisi bir köye girdiler."},
 "tokens": [tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."), DUAL_MADI("دَخَلَا", "dakhala"), MAFUL("قَرْيَةً", "qarya", punct=".")]})
S3.append({"id": "s7", "translation": {"en": "And the two asked its people for food.", "tr": "Ve ikisi köy halkından yemek istediler."},
 "tokens": [DUAL_MADI("فَطَلَبَا", "talaba"), MAFUL("طَعَامًا", "taam"), PREP("مِنْ", "min", gloss_tr="«-den»"),
  tok("أَهْلِهَا", "ahl", "noun", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "In jarr after the letter; annexed to «its».", "Cer harfiyle mecrûr; «onun» zamirine muzâf.", punct=".", segments=[seg("أَهْلِ", "ahl", "noun"), seg("هَا", "pron-3fs", "pron")])]})
S3.append({"id": "s8", "translation": {"en": "But the people of the village did not give them any food.", "tr": "Fakat köy halkı onlara hiç yemek vermedi."},
 "tokens": [tok("فَمَا", "ma-nafiya", "part", ["atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; مَا negates the past verb and governs nothing.", "Fâ atıf harfi; mâ nâfiye, amel etmez.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  ENC_MADI("أَعْطَاهُمَا", "aata", "هُمَا", ["form-iv-verbs"], first=True, alif=True),
  FAIL("أَهْلُ", "ahl", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الْقَرْيَةِ", "qarya"), MAFUL2("طَعَامًا", "taam", punct=".")]})
S3.append({"id": "s9", "translation": {"en": "And the two found a wall in the village.", "tr": "Ve ikisi köyde bir duvar buldular."},
 "tokens": [DUAL_MADI("وَوَجَدَا", "wajada", ["mithal-verbs"]), PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الْقَرْيَةِ", "qarya"), MAFUL("جِدَارًا", "jidar", punct=".")]})
S3.append({"id": "s10", "translation": {"en": "So al-Khidr set the wall upright.", "tr": "Bunun üzerine Hızır duvarı doğrulttu."},
 "tokens": [MADI("فَأَقَامَ", "aqama", ["hollow-verbs", "form-iv-verbs"]), KHADIR_F(), MAFUL("الْجِدَارَ", "jidar", punct=".")]})
S3.append({"id": "s11", "translation": {"en": "So Musa said: «Why did you set up the wall without a wage?»", "tr": "Mûsâ dedi ki: «Duvarı niçin ücretsiz doğrulttun?»"},
 "tokens": [QALA("فَقَالَ"), MUSA_F(punct=":"), LIMADHA(), MADI_T("أَقَمْتَ", "aqama", "anta", ["hollow-verbs", "form-iv-verbs"], note_ar="، وَحُذِفَتْ عَيْنُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" (the hollow verb drops its middle letter before the ta)", note_tr=" (ecvef fiil, tâ'dan önce orta harfini düşürür)"), MAFUL("الْجِدَارَ", "jidar"),
  tok("بِلَا", "bi", "prep", ["huruf-jarr", "la-nafiya"], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The ba is a jarr letter; لَا negates and governs nothing: «without».", "Bâ cer harfi; lâ nâfiye, amel etmez: «-sız».", segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part")]),
  MAJR("أَجْرٍ", "ajr", punct="؟")]})
S3.append({"id": "s12", "translation": {"en": "Al-Khidr said: «Now I shall tell you the reason, then I shall go.»", "tr": "Hızır dedi ki: «Şimdi sana sebebi söyleyeceğim, sonra gideceğim.»"},
 "tokens": [QALA("قَالَ"), KHADIR_F(punct=":"),
  tok("الْآنَ", "al-an", "noun", ["maful-fih", "al-kinayat-wal-zuruf-al-mabniyya"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "An adverb of time «now», built on fatha, in the seat of nasb.", "«Şimdi» — zaman zarfı, fetha üzere mebnî, mahallen mansûb."),
  tok("سَأَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", "al-fail-al-mudmar-al-mustatir-wujuban"], "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَأَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.", "The sin marks the near future; «I shall say» is a present verb in raf' by the damma, its doer «I» hidden of necessity.", "Sîn istikbâl harfi; «söyleyeceğim» damme ile merfû muzâri, fâil «ben» vücûben müstetir.", segments=[seg("سَ", "sawfa", "part"), seg("أَقُولُ", "qala", "verb")]),
  LAHU("لَكَ", "pron-2ms", " («sana»)"), MAFUL("السَّبَبَ", "sabab"),
  tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."),
  tok("أَذْهَبُ", "dhahaba", "verb", ["mudari-marfu", "atf-nasaq", "al-fail-al-mudmar-al-mustatir-wujuban"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ مَعْطُوفٌ عَلَى أَقُولُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.", "Present verb in raf', conjoined to «I shall say»; the doer «I» is hidden of necessity.", "Damme ile merfû muzâri, «söyleyeceğim»e ma'tûf; fâil «ben» vücûben müstetir.", punct=".")]})

# ---- Chapter 4 — السَّبَبُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "As for the ship, it belonged to poor people.", "tr": "Gemiye gelince: o, yoksul kimselerin idi."},
 "tokens": [*AMMA("أَمَّا", ("السَّفِينَةُ", "safina")), FAKANA(fem=True),
  tok("لِمَسَاكِينَ", "miskin", "noun", ["huruf-jarr", "mamnu-min-sarf", "jam-taksir", "kana-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ، وَمَسَاكِينَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "The lam is a jarr letter; «poor people» is in jarr by fatha in place of kasra, barred from tanwin by its shape (the plural of the extreme pattern); the phrase is the predicate of كَانَ, whose noun «it» is hidden.", "Lâm cer harfi; «yoksullar» kesre yerine fetha ile mecrûr — sîga-i müntehe'l-cümû' üzere gayr-i munsarif; câr-mecrûr kâne'nin haberi, ismi «o» müstetir.", punct=".", segments=[seg("لِ", "li", "prep"), seg("مَسَاكِينَ", "miskin", "noun")])]})
S4.append({"id": "s2", "translation": {"en": "And there was a wrongdoing king who used to take every ship.", "tr": "Ve her gemiyi alan zâlim bir kral vardı."},
 "tokens": [KANA("وَكَانَ"), HUNAKA(), ISMK("مَلِكٌ", "malik-king", muakhkhar=True, note_ar=" — وَهُنَاكَ خَبَرٌ مُقَدَّمٌ", note_en=" — «there» is its fronted predicate", note_tr=" — «orada» öne alınmış haberidir"),
  NAAT("ظَالِمٌ", "zalim", "raf", ["ism-fail"]),
  tok("يَأْخُذُ", "akhadha", "verb", ["mudari-marfu", "naat-sifa", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِمَلِكٍ.", "Present verb in raf'; its doer «he» is hidden — the clause is a second adjective of «king», in the seat of raf'.", "Damme ile merfû muzâri; fâil «o» gizli — cümle, «kral»ın ikinci sıfatı olarak mahallen merfû."),
  MAFUL("كُلَّ", "kull", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("سَفِينَةٍ", "safina", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "So I tore it, so that the king would leave it alone.", "tr": "Ben de kral onu bıraksın diye deldim."},
 "tokens": [MADI_T("فَخَرَقْتُهَا", "kharaqa", "ana", enc="هَا"),
  tok("لِيَتْرُكَهَا", "taraka", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"], "اللَّامُ لَامُ التَّعْلِيلِ، وَيَتْرُكَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "The lam of purpose; «leave» is a present verb put in nasb by an أَنْ understood after the lam, its sign the fatha; the attached «it» is the object.", "Ta'lîl lâmı; «bıraksın» lâmdan sonra gizli en ile mansûb muzâri, alâmeti fetha; bitişik «onu» mef'ûlün bihtir.", segments=[seg("لِ", "li", "prep"), seg("يَتْرُكَ", "taraka", "verb"), seg("هَا", "pron-3fs", "pron")]),
  FAIL("الْمَلِكُ", "malik-king", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "And as for the boy, his two parents were believers.", "tr": "Oğlana gelince: onun anne-babası mümin idiler."},
 "tokens": [*AMMA("وَأَمَّا", ("الْغُلَامُ", "ghulam")), FAKANA(),
  tok("أَبَوَاهُ", "ab", "noun", ["kana-wa-akhawatuha", "al-muthanna", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"], "اسْمُ كَانَ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى (أَبَوَانِ: الْأَبُ وَالْأُمُّ تَغْلِيبًا)، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The noun of كَانَ, in raf' by the alif because it is a dual («the two fathers» = father and mother, by predominance); its nun is dropped for the idafa, and «his» is the second term.", "Kâne'nin ismi, tesniye olduğu için elif ile merfû («iki baba» = anne-baba, tağlîb yoluyla); nûnu izâfet için düşmüş; «onun» muzâfun ileyh.", segments=[seg("أَبَوَا", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  KHK("مُؤْمِنَيْنِ", "mumin", extra=["al-muthanna", "ism-fail"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "And the boy was a wrongdoer.", "tr": "Ve oğlan zâlim idi."},
 "tokens": [KANA("وَكَانَ"), ISMK("الْغُلَامُ", "ghulam"), KHK("ظَالِمًا", "zalim", extra=["ism-fail"], punct=".")]})
S4.append({"id": "s6", "translation": {"en": "So Allah gave the two of them a righteous child.", "tr": "Bunun üzerine Allah o ikisine sâlih bir çocuk verdi."},
 "tokens": [ENC_MADI("فَأَعْطَاهُمَا", "aata", "هُمَا", ["form-iv-verbs"], first=True, alif=True), ALLAH_F(), MAFUL2("وَلَدًا", "walad"), NAAT("صَالِحًا", "salih", "nasb", punct=".")]})
S4.append({"id": "s7", "translation": {"en": "And as for the wall, it belonged to two orphan boys.", "tr": "Duvara gelince: o, iki yetim oğlanın idi."},
 "tokens": [*AMMA("وَأَمَّا", ("الْجِدَارُ", "jidar")), FAKANA(),
  tok("لِغُلَامَيْنِ", "ghulam", "noun", ["huruf-jarr", "al-muthanna", "kana-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ، وَغُلَامَيْنِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "The lam is a jarr letter; «two boys» is in jarr by the ya because it is a dual — the phrase is the predicate of كَانَ, whose noun «it» is hidden.", "Lâm cer harfi; «iki oğlan» tesniye olduğu için yâ ile mecrûr — câr-mecrûr kâne'nin haberi, ismi «o» müstetir.", segments=[seg("لِ", "li", "prep"), seg("غُلَامَيْنِ", "ghulam", "noun")]),
  tok("يَتِيمَيْنِ", "yatim", "noun", ["naat-sifa", "al-muthanna"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "An adjective in jarr by the ya, a dual agreeing with its noun.", "Na't, tesniye olduğu için yâ ile mecrûr.", punct=".")]})
S4.append({"id": "s8", "translation": {"en": "And beneath it there was a treasure for the two of them.", "tr": "Ve onun altında o ikisine ait bir hazine vardı."},
 "tokens": [KANA("وَكَانَ"),
  tok("تَحْتَهُ", "tahta", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "kana-wa-akhawatuha"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرُ كَانَ مُقَدَّمٌ.", "An adverb of place «beneath», in nasb and annexed to «it» — the adverb is the fronted predicate of كَانَ.", "«Altında» — mekân zarfı, mansûb, «onun» zamirine muzâf — zarf, kâne'nin öne alınmış haberidir.", segments=[seg("تَحْتَ", "tahta", "noun"), seg("هُ", "pron-3ms", "pron")]),
  ISMK("كَنْزٌ", "kanz", muakhkhar=True), LAHU("لَهُمَا", "pron-3d", " («o ikisine»)", punct=".", grammar=["naat-sifa"])]})
S4.append({"id": "s9", "translation": {"en": "And their father was a righteous man.", "tr": "Ve babaları sâlih bir adam idi."},
 "tokens": [KANA("وَكَانَ"),
  tok("أَبُوهُمَا", "ab", "noun", ["kana-wa-akhawatuha", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"], "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "The noun of كَانَ, in raf' by the waw because it is one of the five nouns; annexed to «the two of them».", "Kâne'nin ismi, esmâ-i hamseden olduğu için vâv ile merfû; «o ikisi» zamirine muzâf.", segments=[seg("أَبُو", "ab", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  KHK("رَجُلًا", "rajul"), NAAT("صَالِحًا", "salih", "nasb", punct=".")]})
S4.append({"id": "s10", "translation": {"en": "So Allah wanted to keep the treasure for the two of them.", "tr": "Allah hazineyi o ikisi için korumak istedi."},
 "tokens": [MADI("فَأَرَادَ", "arada", ["hollow-verbs", "form-iv-verbs"]), ALLAH_F(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ.", "The masdar-making أَنْ puts the verb in nasb; the clause it builds is the object of «wanted».", "Masdariyye en: fiili nasb eder; kurduğu müevvel masdar «istedi»nin mef'ûlüdür."),
  tok("يَحْفَظَ", "hafiza", "verb", ["nawasib-wa-jawazim-al-mudari"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Present verb put in nasb by أَنْ, its sign the fatha; the doer «He» is hidden.", "En ile mansûb muzâri, alâmeti fetha; fâil «O» gizli zamir."),
  MAFUL("الْكَنْزَ", "kanz"), LAHU("لَهُمَا", "pron-3d", " («o ikisine»)", punct=".")]})
S4.append({"id": "s11", "translation": {"en": "Then al-Khidr said: «This is the command of Allah.»", "tr": "Sonra Hızır dedi ki: «Bu, Allah'ın emridir.»"},
 "tokens": [tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."), QALA("قَالَ"), KHADIR_F(punct=":"),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A demonstrative, built; it fills the mubtada's seat in raf'.", "İşaret ismi, mebnî; mübtedâ olarak mahallen merfû."),
  tok("أَمْرُ", "amr", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The khabar, in raf' and annexed.", "Haber, merfû, muzâf."),
  MUDAF_ILAYH("اللهِ", "allah", "propn", [], note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=".")]})
S4.append({"id": "s12", "translation": {"en": "And Musa returned to his people.", "tr": "Ve Mûsâ kavmine döndü."},
 "tokens": [MADI("وَرَجَعَ", "rajaa"), MUSA_F(), PREP("إِلَى", "ila", gloss_tr="«-e»"),
  tok("قَوْمِهِ", "qawm", "noun", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "In jarr after the letter; annexed to «his».", "Cer harfiyle mecrûr; «onun» zamirine muzâf.", punct=".", segments=[seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")])]})

TITLES = [
 {"ar": "الْعَبْدُ الصَّالِحُ", "en": "The Righteous Servant", "tr": "Sâlih Kul"},
 {"ar": "السَّفِينَةُ", "en": "The Ship", "tr": "Gemi"},
 {"ar": "الْغُلَامُ وَالْجِدَارُ", "en": "The Boy and the Wall", "tr": "Oğlan ve Duvar"},
 {"ar": "السَّبَبُ", "en": "The Reason", "tr": "Sebep"},
]
CHAPS = [S1, S2, S3, S4]

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule), plus the three new words
PREF = ["musa-wa-bani-israil", "musa-wa-firawn", "bad-al-amali", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
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
 "khadir": {"lemma": "الْخَضِر", "root": "خ ض ر", "pos": "propn", "gloss": {"en": "al-Khidr, the righteous servant whom Musa followed (named with the article; read al-Khaḍir / al-Khiḍr)", "tr": "Hızır, Mûsâ'nın peşine düştüğü sâlih kul (harf-i tarifle anılır; el-Hadır / el-Hızır okunur)"}, "level": 1},
 "kharaqa": {"lemma": "خَرَقَ", "root": "خ ر ق", "pos": "verb", "form": "I", "gloss": {"en": "to tear, to make a hole in (خَرَقَ يَخْرِقُ)", "tr": "delmek, yırtmak (خَرَقَ يَخْرِقُ)"}, "level": 2},
 "sakhra": {"lemma": "صَخْرَة", "root": "ص خ ر", "pos": "noun", "plural": "صَخَرَات / صُخُور", "gloss": {"en": "a rock, a boulder", "tr": "kaya"}, "level": 2},
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
MORPH["verbs"]["kharaqa"] = _sg.sound1("daraba", "خَرَق", "خْرِق", "اِخْرِق", "خَرْق", "خَارِق", maful="مَخْرُوق", pmz="خُرِقَ", pmd="يُخْرَقُ")
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": "musa-wal-khadir",
 "storyGroup": "musa-wa-firawn",
 "title": {"ar": "مُوسَى وَالْخَضِرُ", "en": "Musa and al-Khidr", "tr": "Mûsâ ve Hızır"},
 "subtitle": {"ar": "قِصَّةُ الْعَبْدِ الصَّالِحِ لِلْمُبْتَدِئِينَ — السَّفِينَةُ، وَالْغُلَامُ، وَالْجِدَارُ",
              "en": "The story of the righteous servant, for beginners — the ship, the boy, the wall",
              "tr": "Yeni başlayanlar için sâlih kulun kıssası — gemi, oğlan, duvar"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-07",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": ["musa-wa-firawn", "musa-wa-bani-israil"],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِقِصَّةِ مُوسَى وَالْخَضِرِ كَمَا تُرْوَى لِلْأَطْفَالِ (عَلَى ضَوْءِ سُورَةِ الْكَهْفِ، الْآيَاتِ ٦٠–٨٢)، عَلَى طَرِيقَةِ الْقِرَاءَةِ الْمُتَدَرِّجَةِ لِلنَّدْوِيِّ. لَمْ تُنْقَلْ آيَةٌ بِنَصِّهَا، وَلَا يُسْتَشْهَدُ بِجُمْلَةٍ هُنَا عَلَى أَنَّهَا نَصٌّ تُرَاثِيٌّ. الثَّالِثَةُ مِنْ قِصَصِ مُوسَى فِي هٰذَا الْبَرْنَامَجِ.",
  "en": "ORIGINAL Level-1 graded Arabic: the story of Musa and al-Khidr as it is told to children (after the Qurʾānic narrative in al-Kahf 60–82), composed editorially in the manner of Nadwī's graded readers — short كَانَ-framed sentences, one event per line, the vocabulary repeated. No āya is quoted verbatim; no sentence here may be cited as a classical text. The third of the Musa stories in this programme, written to meet the dual, the five nouns and أَمَّا … فَ.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Mûsâ ile Hızır kıssasının çocuklara anlatıldığı şekli (Kehf sûresi 60–82. âyetlerindeki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde telif edilmiştir — kısa, kâne ile kurulu cümleler, her satırda bir olay, tekrar eden kelime hazinesi. Hiçbir âyet aynen aktarılmamıştır; buradaki hiçbir cümle klasik bir metin olarak kaynak gösterilemez. Bu programdaki Mûsâ kıssalarının üçüncüsü; tesniye, esmâ-i hamse ve «emmâ … fe» için yazıldı.",
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
