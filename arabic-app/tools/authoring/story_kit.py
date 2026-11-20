"""story_kit — the authoring kit for an ORIGINAL graded story (wave 113).

Every original story from «مُوسَى وَفِرْعَوْنُ» (wave 82) to «جُحَا وَالْحِمَارُ» (wave 110) carried a private copy of the same
helper library: tok()/seg() for a token and its clitic segments, the house wordings of the iʿrāb lines (FAIL, MAFUL, MUBTADA,
KHABAR, MUDAF_ILAYH, NAAT, ATF, HAL, BADAL, the كَانَ and إِنَّ families, the verb shapes MADI/MADI_T/ENC_MADI/VERB_WAW/
DUAL_MADI/MUDARI/MUDARI5/MANSUB_AN/AMR, the jarr letters and their fused pronouns, the particles) and the pronoun tables
PRON/PRON_AR. Twenty copies of six hundred lines is twenty places for the wording to drift, so from wave 113 the library
lives HERE, once, exactly as the Juḥā story left it (tools/authoring/author_juha.py lines 18–694, verbatim but for tok(),
which now NFC-normalises every Arabic string). An author script does

    from story_kit import *          # after putting tools/authoring on sys.path
    import sarf_gen as _sg           # for a NEW verb's paradigm

and writes only its sentences, its new glossary entries and its manifest. The earlier scripts keep their private copies —
they regenerate packages that are already on the shelf, and a kit edit must never silently re-author a shipped text.
RULES THAT TRAVEL WITH THE KIT: a lex key is global (reuse by lemma identity, never rebuild a paradigm under an existing
key); the syntactic claim comes FIRST in an iʿrāb line and any sarf commentary after it (RoleEngine reads the line);
`published` is authored, never derived; every manifest keeps reviewStatus pending-scholarly-review.
"""
import json, os, pathlib, re, sys, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import sarf_gen as _sg

DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)

def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    """one token of a chapter — the surface in its three layers, the lex key, the part of speech, the grammar anchors and
    the trilingual iʿrāb. Every Arabic string is NFC-normalised on the way in: the corpus stores fatḥa BEFORE shadda, and a
    string typed the other way round is visually identical and string-unequal (the sarf_gen trap, now closed here too)."""
    N = lambda x: unicodedata.normalize("NFC", x) if isinstance(x, str) else x
    full = N(full)
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": N(ar), "en": en, "tr": tr}
    if segments: t["segments"] = [{**sg_, "form": N(sg_["form"])} for sg_ in segments]
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}

# ---- the house wordings ------------------------------------------------------------------------------------------
WA_AR = "الْوَاوُ عَاطِفَةٌ، وَ"
FA_AR = "الْفَاءُ عَاطِفَةٌ، وَ"
def _pre(full):
    """a وَ / فَ prefix on the token: (prefix letter, bare stem, segments head, the three i'rab openings)"""
    # (wave 167) a word's own first radical is no conjunction: وَجَدَ (wajada), وَصَلُوا (wasala), فَرِحَ (fariha), وَلَدٌ (walad).
    # The helper is called as _pre(full) from builders that hold the token's key in a local named `lex`; a key that opens
    # with the same letter (w / f) marks the letter as the lemma's — unless the letter is written twice (وَوَجَدَ) or the
    # article follows it (وَالْوَلَدُ). tools/authoring/fix_radical_prefix.py holds the paradigm-exact form of the same test.
    import sys as _sys, re as _re
    _lex = _sys._getframe(1).f_locals.get("lex")
    if isinstance(_lex, str) and not _re.match(r"^[اٱ]لْ?|^[اٱ]ل[ء-ي]ّ", full[2:]) and ((full.startswith("وَ") and _lex[:1] == "w" and not full[2:].startswith("و")) or (full.startswith("فَ") and _lex[:1] == "f" and not full[2:].startswith("ف"))):
        return "", full, None, "", "", ""
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

# ============ «نُوحٌ وَالسَّفِينَةُ» — the fifth ORIGINAL Level-1 story: four chapters (wave 90) ============
PRON.update({"هِمْ": "pron-3mp", "كُمْ": "pron-2mp"})
PRON_AR.update({"هِمْ": "هُمْ", "كُمْ": "كُمْ"})
NUH_F = lambda punct=None: FAIL("نُوحٌ", "nuh", "propn", note_ar=" — عَلَمٌ أَعْجَمِيٌّ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ فَهُوَ مُنْصَرِفٌ", note_en=" — a three-letter foreign name with a quiescent middle, so it keeps its tanwin", note_tr=" — ortası sâkin üç harfli yabancı özel isim; bu yüzden munsariftir", punct=punct)
NUH_ISMK = lambda punct=None: ISMK("نُوحٌ", "nuh", "propn", note_ar=" — عَلَمٌ أَعْجَمِيٌّ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ فَهُوَ مُنْصَرِفٌ", note_en=" — a three-letter foreign name with a quiescent middle, so it keeps its tanwin", note_tr=" — ortası sâkin üç harfli yabancı özel isim; bu yüzden munsariftir", punct=punct)
ALLAH_F = lambda punct=None: FAIL("اللهُ", "allah", "propn", note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=punct)
ALLAH_MAF = lambda punct=None: MAFUL("اللهَ", "allah", "propn", note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=punct)
def JARR_PRON(full, lex, head, enc, tr, punct=None, extra=None, note_ar="", note_en="", note_tr=""):
    """مِنْهُ، بِهِ، إِلَيْهِمْ، فِيهَا: a jarr letter fused to its pronoun"""
    return tok(full, lex, "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + (extra or []),
        "حَرْفُ جَرٍّ، وَالضَّمِيرُ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ" + note_ar + ".", "A jarr letter; the attached pronoun fills the seat of jarr" + note_en + ".", "Cer harfi; bitişik zamir mahallen mecrûr" + tr + note_tr + ".",
        punct=punct, segments=[seg(head, lex, "prep"), seg(enc, PRON[enc], "pron")])
def ZARF(full, lex, kind="مَكَانٍ", kind_en="place", kind_tr="mekân", extra=None, punct=None, note_ar="", note_en="", note_tr="", mudaf=True, segments=None):
    g = ["maful-fih"] + (["idafa-definiteness"] if mudaf else []) + (extra or [])
    return tok(full, lex, "noun", g, "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ" + ("، مُضَافٌ" if mudaf else "") + note_ar + ".",
        "An adverb of " + kind_en + ", in nasb" + (" and annexed" if mudaf else "") + note_en + ".", kind_tr + " zarfı, mansûb" + (", muzâf" if mudaf else "") + note_tr + ".", punct=punct, segments=segments)
def VERB_WAW(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="", tense="mazi"):
    """قَالُوا، سَخِرُوا، كَانُوا: a past verb with the waw of the group"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    g = ["al-bariz-al-muttasil", "fail"] + (extra or [])
    return tok(full, lex, "verb", g,
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note_ar + ".",
        en0 + "past verb built on damma because the waw of the group is attached; that waw is the doer, in the seat of raf'" + note_en + ".",
        tr0 + "cemâat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâildir, mahallen merfû" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem[:-1], lex, "verb"), seg("ا", "pron-3mp", "pron")] if s])
def MUDARI5(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="", role_ar="", role_en="", role_tr=""):
    """يَعْبُدُونَ، يَنْظُرُونَ: one of the five verbs in raf'"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, lex, "verb", ["afal-khamsa", "mudari-marfu", "al-bariz-al-muttasil"] + (extra or []),
        ar0 + "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + role_ar + note_ar + ".",
        en0 + "one of the five verbs, in raf' by the kept nun; the waw is its doer, in the seat of raf'" + role_en + note_en + ".",
        tr0 + "ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâildir, mahallen merfû" + role_tr + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem, lex, "verb")] if s] if sg else None)
LAM_JAZM = lambda full="لَمْ": tok(full, "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], (FA_AR if full.startswith("فَ") else "") + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", ("The fa conjoins; " if full.startswith("فَ") else "") + "لَمْ: the particle of negation and jazm that turns the present to the past.", ("«bunun üzerine» + " if full.startswith("فَ") else "") + "lem: nefy, cezm ve kalb harfi.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")] if full.startswith("فَ") else None)
ILLA = lambda: tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"], "أَدَاةُ اسْتِثْنَاءٍ — وَالِاسْتِثْنَاءُ مُفَرَّغٌ، فَمَا بَعْدَهَا يَأْخُذُ إِعْرَابَهُ مِنْ مَوْقِعِهِ.", "The particle of exception; the exception is «emptied» (mufarragh): what follows takes the case its own position demands.", "İstisnâ edatı; istisnâ müferrağdır — sonrası i'râbını kendi mevkiinden alır.")
def MAJHUL(full, lex, extra=None, punct=None, fem=False, note_ar="", note_en="", note_tr=""):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    ta = "، وَالتَّاءُ لِلتَّأْنِيثِ" if fem else ""
    return tok(full, lex, "verb", ["naib-al-fail", "al-majhul-fil-kafiya"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ" + ta + " — ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ" + note_ar + ".",
        en0 + "a past verb in the passive, built on fatha" + (" (the ta marks the feminine)" if fem else "") + " — its first letter takes damma and the letter before the last a kasra" + note_en + ".",
        tr0 + "meçhul mâzî, fetha üzere mebnî" + (" (tâ te'nîs içindir)" if fem else "") + " — evveli mazmûm, âhirinden önceki harf meksûr" + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def NAIB(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="", sign="بِالضَّمَّةِ"):
    return tok(full, lex, "noun", ["naib-al-fail"] + (extra or []), "نَائِبُ فَاعِلٍ مَرْفُوعٌ " + sign + note_ar + ".", "The deputy doer (na'ib al-fa'il), in raf'" + note_en + ".", "Nâib-i fâil, merfû" + note_tr + ".", punct=punct)
ILAYHIM = lambda punct=None: JARR_PRON("إِلَيْهِمْ", "ila", "إِلَيْ", "هِمْ", " («onlara»)", punct=punct)
MINHU = lambda punct=None: JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", punct=punct)
BIHI = lambda punct=None: JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («ona»)", punct=punct)
MINHUM = lambda punct=None: JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", punct=punct)
AN_KASRA = lambda: tok("عَنِ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter «from», voweled with kasra before the following ال.", "«-den» — cer harfi; iki sâkin karşılaştığı için kesre ile harekelendi.")
KAFIRIN_J = lambda punct=None, note_ar="", note_en="", note_tr="": tok("الْكَافِرِينَ", "kafir", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ" + note_ar + ".", "In jarr by the ya — a sound masculine plural" + note_en + ".", "Cem-i müzekker sâlim olduğu için yâ ile mecrûr" + note_tr + ".", punct=punct)
MUMINUN_F = lambda punct=None: FAIL("الْمُؤْمِنُونَ", "mumin", extra=["jam-mudhakkar-salim", "ism-fail"], sign="بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the waw, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için vâv ile", punct=punct)
SAFINA_MAF = lambda punct=None: MAFUL("السَّفِينَةَ", "safina", punct=punct)
SAFINA_MI = lambda punct=None: MUDAF_ILAYH("السَّفِينَةِ", "safina", punct=punct)
SAFINA_J = lambda punct=None: MAJR("السَّفِينَةِ", "safina", punct=punct)
MA_F = lambda punct=None: FAIL("الْمَاءُ", "ma-water", punct=punct)

# ---- the pronoun tables need the plural «you» (also damma-voweled before ال) and the kasra-/damma-voweled «them»
PRON.update({"كُمْ": "pron-2mp", "كُمُ": "pron-2mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp", "ي": "pron-1s"})
PRON_AR.update({"كُمْ": "كُمْ", "كُمُ": "كُمْ", "هِمْ": "هِمْ", "هُمُ": "هُمْ"})

# ============ «هُودٌ وَعَادٌ» — the eighth story: four chapters ============
THREE = (" — عَلَمٌ أَعْجَمِيٌّ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ فَهُوَ مُنْصَرِفٌ", " — a three-letter foreign name with a quiescent middle, so it keeps its tanwin", " — ortası sâkin üç harfli yabancı özel isim; bu yüzden munsariftir")
HUD_F = lambda punct=None: FAIL("هُودٌ", "hud-prophet", "propn", [], *THREE, punct=punct)
HUD_ISMK = lambda punct=None: ISMK("هُودٌ", "hud-prophet", "propn", [], *THREE, punct=punct)
HUD_KH = lambda punct=None: KHABAR("هُودٌ", "hud-prophet", punct=punct, note_ar=THREE[0], note_en=THREE[1], note_tr=THREE[2])
HUD_MAF = lambda punct=None: MAFUL("هُودًا", "hud-prophet", "propn", [], *THREE, punct=punct)
HUD_MUNADA = lambda punct=None: tok("هُودُ", "hud-prophet", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on damma, in the seat of nasb.", "Münâdâ: müfred alem, damme üzere mebnî, mahallen mansûb.", punct=punct)
AAD_MI = lambda punct=None: MUDAF_ILAYH("عَادٍ", "aad", "propn", [], note_ar=" — اسْمُ قَبِيلَةٍ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ فَهُوَ مُنْصَرِفٌ", note_en=" — a tribe's three-letter name with a quiescent middle, so it keeps its tanwin", note_tr=" — ortası sâkin üç harfli kabile adı; bu yüzden munsariftir", punct=punct)
QAWM_AAD_ISMK = lambda: tok("قَوْمُ", "qawm", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of كَانَ, in raf', annexed.", "Kâne'nin ismi, merfû; muzâf.")
QAWM_AAD_F = lambda: FAIL("قَوْمُ", "qawm", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf")
QAWMI = lambda punct=None: tok("قَوْمِ", "qawm", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ الْمَحْذُوفَةِ.", "The vocative «my people», annexed to a dropped ya of the speaker: in nasb by an estimated fatha, the kasra pointing to the dropped ya.", "Münâdâ «kavmim»: hazfedilmiş mütekellim yâ'sına muzâf; takdîrî fetha ile mansûb, kesre hazfedilen yâ'ya delâlet eder.", punct=punct)
FI = lambda: PREP("فِي", "fi", gloss_tr="«-de»")
MIN = lambda: PREP("مِنْ", "min", gloss_tr="«-den»")
ILA = lambda: PREP("إِلَى", "ila", gloss_tr="«-e»")
ALA = lambda: PREP("عَلَى", "ala", gloss_tr="«üzerine»")
ALLAH_J = lambda punct=None: MAJR("اللهِ", "allah", "propn", note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=punct)
def KANU(full):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
        ar0 + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.",
        en0 + "كَانُوا is the defective past verb built on damma before the waw of the group; that waw is the noun of كَانَ, in the seat of raf'.",
        tr0 + "kânû: cemâat vâvı bitiştiği için damme üzere mebnî nâkıs mâzî; vâv, kâne'nin ismi olarak mahallen merfû.",
        segments=[s for s in [sg, seg(stem[:-1], "kana", "verb"), seg("ا", "pron-3mp", "pron")] if s])
KANAT_K = lambda full="وَكَانَتِ": tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    (WA_AR if full.startswith("وَ") else FA_AR) + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    ("The waw conjoins; " if full.startswith("وَ") else "The fa conjoins; ") + "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb; the ta marks the feminine and is voweled with kasra before the following ال.",
    ("«ve» + " if full.startswith("وَ") else "«bunun üzerine» + ") + "«idi» — nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.",
    segments=[seg(full[:2], "wa" if full.startswith("وَ") else "fa", "conj"), seg(full[2:], "kana", "verb")])
KANA_HID = lambda full="وَكَانَ": tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    (WA_AR if full.startswith("وَ") else FA_AR if full.startswith("فَ") else "") + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    ("The waw conjoins; " if full.startswith("وَ") else "The fa conjoins; " if full.startswith("فَ") else "") + "كَانَ is the defective past verb; its noun is the hidden pronoun «he».",
    ("«ve» + " if full.startswith("وَ") else "«bunun üzerine» + " if full.startswith("فَ") else "") + "nâkıs mâzî fiil kâne; ismi gizli zamir «o».",
    segments=[seg(full[:2], "wa" if full.startswith("وَ") else "fa", "conj"), seg(full[2:], "kana", "verb")] if full[0] in "وف" else None)
SARAT = lambda full="وَصَارَتْ": tok(full, "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    WA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.",
    "The waw conjoins; صَارَ «became» is a sister of كَانَ; the ta marks the feminine, and its noun is the hidden pronoun «she».",
    "«ve» + sâra «oldu», kâne'nin kardeşlerinden; tâ te'nîs içindir, ismi gizli zamir «o».", segments=[seg("وَ", "wa", "conj"), seg(full[2:], "sara", "verb")])
WA_LA_NAFIYA = lambda: tok("وَلَا", "la-nafiya", "part", ["la-nafiya"], WA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The waw conjoins; لَا negates and governs nothing.", "«ve» + nefiy lâ'sı; amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
LA_NAFIYA = lambda: tok("لَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The negating لَا, which governs nothing.", "Nefiy lâ'sı; amel etmez.")
LA_NAHIYA = lambda: tok("لَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "لَا النَّاهِيَةُ حَرْفُ نَهْيٍ وَجَزْمٍ.", "The prohibitive لَا «do not», which governs jazm.", "Nehiy lâ'sı: nehiy ve cezm harfi.")
def FIVE_JAZM(full, lex, by, by_en, by_tr, extra=None, enc=None, punct=None, shart=False):
    """لَا تَعْبُدُوا، لَمْ تُؤْمِنُوا، لَمْ يَتُوبُوا: one of the five verbs in jazm by the dropped nun"""
    stem = full[:-len(enc)] if enc else full
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    sh = (" — وَالْفِعْلُ فِعْلُ الشَّرْطِ", "; the verb is the condition's verb", "; fiil şart fiilidir") if shart else ("", "", "")
    segs = [seg(stem[:-1] if not enc else stem, lex, "verb")] + ([seg("ا", "pron-3mp", "pron")] if not enc else []) + ([seg(enc, PRON[enc], "pron")] if enc else [])
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil"] + (["maful-bihi"] if enc else []) + (["al-majzum-wal-shart-wal-jaza"] if shart else []) + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ" + by + " وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + encs + sh[0] + ".",
        "Present verb in jazm by " + by_en + ", its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf'" + ("; the attached pronoun is its object" if enc else "") + sh[1] + ".",
        by_tr + " ile meczûm muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû" + ("; bitişik zamir mef'ûlün bih" if enc else "") + sh[2] + ".", punct=punct, segments=segs)
def VERB_WAW_ENC(full, lex, enc, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """كَذَّبُوهُ: a past verb with the waw of the group and an enclitic object"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)]
    return tok(full, lex, "verb", ["al-bariz-al-muttasil", "fail", "maful-bihi"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note_ar + ".",
        en0 + "past verb built on damma before the waw of the group; that waw is the doer, and the attached pronoun after it is the object, in the seat of nasb" + note_en + ".",
        tr0 + "cemâat vâvı bitiştiği için damme üzere mebnî mâzî; vâv fâil, sonundaki bitişik zamir mef'ûlün bih — mahallen mansûb" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem_v[:-1], lex, "verb"), seg("و", "pron-3mp", "pron"), seg(enc, PRON[enc], "pron")] if s])
def ISHARA(full, lex, seat_ar, seat_en, seat_tr, built_ar="السُّكُونِ", built_en="sukun", built_tr="sükûn", extra=None, punct=None):
    return tok(full, lex, "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى " + built_ar + " فِي مَحَلِّ " + seat_ar + ".", "A demonstrative, built on " + built_en + ", in the seat of " + seat_en + ".", "İşaret ismi, " + built_tr + " üzere mebnî, " + seat_tr + " olarak mahallen.", punct=punct)
def BADAL(full, lex, case, extra=None, punct=None):
    sign = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, lex, "noun", ["badal", "asma-al-ishara"] + (extra or []), "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ " + sign + ".", "A badal of the demonstrative, in the same case.", "İşaret isminden bedel; onun i'râbını alır.", punct=punct)
def LI_AL(full, lex, stem, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    return tok(full, "li", "prep", ["huruf-jarr"] + (extra or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَ" + stem + " مَجْرُورٌ بِالْكَسْرَةِ" + note_ar + ".", "The lam is a jarr letter; the noun after it is in jarr" + note_en + ".", "Lâm cer harfi; sonraki isim mecrûr" + note_tr + ".",
        punct=punct, segments=[seg("لِ", "li", "prep"), seg(stem, lex, "noun")])
KULLUHUM = lambda punct=None: tok("كُلُّهُمْ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يُؤَكِّدُ الْفَاعِلَ قَبْلَهُ.", "A tawkid of meaning «all of them», in raf' like the doer it strengthens; annexed to the pronoun «them», which fills the seat of jarr.", "Ma'nevî te'kîd «hepsi», pekiştirdiği fâil gibi merfû; «onlar» zamirine muzâf, zamir mahallen mecrûr.", punct=punct, segments=[seg("كُلُّ", "kull", "noun"), seg("هُمْ", "pron-3mp", "pron")])
WAHDAHU = lambda punct=None: tok("وَحْدَهُ", "wahda", "noun", ["hal", "idafa-definiteness", "al-bariz-al-muttasil"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَوَحْدَهُ لَا يَقَعُ إِلَّا حَالًا.", "The hal «alone», in nasb and annexed to the pronoun «him»; وَحْدَهُ is only ever a hal.", "Hâl «yalnız, tek başına», mansûb; «o» zamirine muzâf — vahdehû yalnız hâl olarak gelir.", punct=punct, segments=[seg("وَحْدَ", "wahda", "noun"), seg("هُ", "pron-3ms", "pron")])
def INNA_ENC(full, enc, tr, punct=None, extra=None):
    """إِنَّهَا، إِنَّهُ، لَكِنَّهُ: the verb-like particle with its attached noun"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    lex = "lakinna" if stem.startswith("لَكِنَّ") or stem.startswith("لٰكِنَّ") else "inna"
    head = stem[:-len(enc)]
    name_ar = "لَكِنَّ" if lex == "lakinna" else "إِنَّ"
    return tok(full, lex, "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"] + (extra or []),
        ar0 + name_ar + " حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُهَا.",
        en0 + name_ar + " is the verb-like particle; the attached pronoun is its noun in the seat of nasb — the clause after it is its predicate, in the seat of raf'.",
        tr0 + name_ar + " fiile benzeyen harf; bitişik zamir ismi, mahallen mansûb — sonraki cümle haberi, mahallen merfû" + tr + ".",
        punct=punct, segments=[s for s in [sg, seg(head, lex, "part"), seg(enc, PRON[enc], "pron")] if s])
MUDARI_F = lambda full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="": tok(full, lex, "verb", ["mudari-marfu"] + (extra or []),
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ" + note_ar + ".", "Present verb in raf'; the doer is the hidden pronoun «she»" + note_en + ".", "Merfû muzâri; fâil gizli zamir «o» (müennes)" + note_tr + ".", punct=punct)
ALLADHI = lambda: tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "A relative pronoun «the one who», built on sukun, in the seat of raf' as the khabar.", "İsm-i mevsûl «…-en», sükûn üzere mebnî, haber olarak mahallen merfû.")
SILA = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
RAAW = lambda full="رَأَوْا", punct=None: tok(full, "raa", "verb", ["thulathi-mujarrad-babs", "naqis-verbs", "al-bariz-al-muttasil", "fail"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
    "Past verb built on a damma estimated on the alif, which drops before the waw of the group (two quiescents meeting); the waw is its doer, in the seat of raf'.",
    "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî damme ile mebnî mâzî; cemâat vâvı fâil, mahallen merfû.", punct=punct, segments=[seg(full[:-1], "raa", "verb"), seg("ا", "pron-3mp", "pron")])
MAN_SHART = lambda full="فَمَنْ": tok(full, "man", "pron", ["al-majzum-wal-shart-wal-jaza", "mubtada-khabar", "al-mabni-wal-mudmar"], (FA_AR if full.startswith("فَ") else WA_AR) + "مَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", ("The fa conjoins; " if full.startswith("فَ") else "The waw conjoins; ") + "«whoever» is a conditional noun that governs jazm, built on sukun, in the seat of raf' as mubtada.", ("«bunun üzerine» + " if full.startswith("فَ") else "«ve» + ") + "men: cezmeden şart ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû.", segments=[seg(full[:2], "fa" if full.startswith("فَ") else "wa", "conj"), seg("مَنْ", "man", "pron")])
SHART_V = lambda full, lex, extra=None: tok(full, lex, "verb", ["al-majzum-wal-shart-wal-jaza"] + (extra or []), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Past verb built on fatha, in the seat of jazm as the condition's verb; the doer «he» is hidden.", "Fetha üzere mebnî mâzî, şart fiili olarak mahallen meczûm; fâil gizli zamir «o».")
JAWAB_V = lambda full, lex, extra=None, punct=None, alif=False: tok(full, lex, "verb", ["al-majzum-wal-shart-wal-jaza"] + (extra or []), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى " + ("فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ" if alif else "الْفَتْحِ") + " فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُ الْمُبْتَدَأِ.", "Past verb built on fatha" + (" (estimated on the alif)" if alif else "") + ", in the seat of jazm as the condition's answer; the doer «he» is hidden — the condition and its answer together are the khabar of «whoever».", "Fetha" + (" (elif üzerinde takdîrî)" if alif else "") + " üzere mebnî mâzî, şartın cevabı olarak mahallen meczûm; fâil gizli zamir «o» — şart ve cevap cümleleri mübtedânın haberidir.", punct=punct)
KH_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", "; the clause fills the seat of raf' as the khabar", "; cümle haber olarak mahallen merfû")
NAAT_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِرَجُلٍ", "; the clause qualifies «a man» — in the seat of nasb as its na't", "; cümle «adam»ın na'tı olarak mahallen mansûb")
JAWAB_MADI = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "; the clause fills the seat of jazm as the condition's answer", "; cümle şartın cevabı olarak mahallen meczûm")

# ============ «دَاوُدُ وَجَالُوتُ» — the ninth ORIGINAL story, the first at Level 2: four chapters (wave 97) ============
PRON.update({"كُمْ": "pron-2mp", "كُمُ": "pron-2mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "نَا": "pron-1p"})
PRON_AR.update({"كُمْ": "كُمْ", "كُمُ": "كُمْ", "هِمْ": "هِمْ", "هُمُ": "هُمْ", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "نَا": "نَا"})
DIPT_SUL = (" — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", " — a foreign proper name, barred from tanwin (diptote)", " — yabancı özel isim, gayr-i munsarıf")
DAWUD_F = lambda punct=None: FAIL("دَاوُدُ", "dawud", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
DAWUD_ISMK = lambda punct=None: ISMK("دَاوُدُ", "dawud", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
DAWUD_KH = lambda punct=None: KHABAR("دَاوُدُ", "dawud", ["mamnu-min-sarf"], note_ar=DIPT_SUL[0], note_en=DIPT_SUL[1], note_tr=DIPT_SUL[2], punct=punct)
TALUT_F = lambda punct=None: FAIL("طَالُوتُ", "talut", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
TALUT_MAF = lambda punct=None: MAFUL("طَالُوتَ", "talut", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
TALUT_MI = lambda punct=None: MUDAF_ILAYH("طَالُوتَ", "talut", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_SUL[0], note_en=DIPT_SUL[1], note_tr=DIPT_SUL[2], punct=punct)
JALUT_F = lambda punct=None: FAIL("جَالُوتُ", "jalut", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
JALUT_MAF = lambda punct=None: MAFUL("جَالُوتَ", "jalut", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
JALUT_KH = lambda punct=None: KHABAR("جَالُوتُ", "jalut", ["mamnu-min-sarf"], note_ar=DIPT_SUL[0], note_en=DIPT_SUL[1], note_tr=DIPT_SUL[2], punct=punct)
ALLAH_J = lambda punct=None: MAJR("اللهِ", "allah", "propn", note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=punct)
ALLAH_ISMI = lambda punct=None: tok("اللهَ", "allah", "propn", ["inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — لَفْظُ الْجَلَالَةِ.", "The noun of إِنَّ, in nasb — the Name of Majesty.", "İnne'nin ismi, mansûb — lafza-i celâl.", punct=punct)
ISM_INNA = lambda full, lex, extra=None, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha"] + (extra or []), "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of إِنَّ, in nasb.", "İnne'nin ismi, mansûb.", punct=punct)
KH_INNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi olarak mahallen merfû")
KH_MUQ2 = ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate of كَانَ", "; câr-mecrûr, kâne'nin öne alınmış haberidir")
KH_KANA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
HAL_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause fills the seat of nasb as a hal", "; cümle hâl olarak mahallen mansûb")
NAAT_CL2 = lambda of: (" — وَالْجُمْلَةُ فِي مَحَلِّ " + of[0] + " نَعْتٌ لِـ" + of[1], "; the clause qualifies «" + of[2] + "» as its na't", "; cümle «" + of[3] + "» için na't")
FI = lambda role=("", "", ""): PREP("فِي", "fi", *role, gloss_tr="«-de»")
MIN = lambda role=("", "", ""), punct=None: PREP("مِنْ", "min", *role, gloss_tr="«-den»", punct=punct)
ILA = lambda: PREP("إِلَى", "ila", gloss_tr="«-e»")
ALA = lambda: PREP("عَلَى", "ala", gloss_tr="«üzerine»")
def KANU(full):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
        ar0 + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.",
        en0 + "كَانُوا is the defective past verb built on damma before the waw of the group; that waw is the noun of كَانَ, in the seat of raf'.",
        tr0 + "kânû: cemâat vâvı bitiştiği için damme üzere mebnî nâkıs mâzî; vâv, kâne'nin ismi olarak mahallen merfû.",
        segments=[s for s in [sg, seg(stem[:-1], "kana", "verb"), seg("ا", "pron-3mp", "pron")] if s])
KANAT_K = lambda full="وَكَانَتِ": tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    "The waw conjoins; كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb; the ta marks the feminine and is voweled with kasra before the following ال.",
    "«ve» + «idi» — nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.",
    segments=[seg("وَ", "wa", "conj"), seg(full[2:], "kana", "verb")])
KANA_HID = lambda full="وَكَانَ", note=("", "", ""): tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    (WA_AR if full.startswith("وَ") else FA_AR if full.startswith("فَ") else "") + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + note[0] + ".",
    ("The waw conjoins; " if full.startswith("وَ") else "The fa conjoins; " if full.startswith("فَ") else "") + "كَانَ is the defective past verb; its noun is the hidden pronoun «he»" + note[1] + ".",
    ("«ve» + " if full.startswith("وَ") else "«bunun üzerine» + " if full.startswith("فَ") else "") + "nâkıs mâzî fiil kâne; ismi gizli zamir «o»" + note[2] + ".",
    segments=[seg(full[:2], "wa" if full.startswith("وَ") else "fa", "conj"), seg(full[2:], "kana", "verb")] if full[0] in "وف" else None)
LA_NAFIYA = lambda: tok("لَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The negating لَا, which governs nothing.", "Nefiy lâ'sı; amel etmez.")
WA_LA_NAFIYA = lambda: tok("وَلَا", "la-nafiya", "part", ["la-nafiya"], WA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The waw conjoins; لَا negates and governs nothing.", "«ve» + nefiy lâ'sı; amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
LA_NAHIYA = lambda: tok("لَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "لَا النَّاهِيَةُ حَرْفُ نَهْيٍ وَجَزْمٍ.", "The prohibitive لَا «do not», which governs jazm.", "Nehiy lâ'sı: nehiy ve cezm harfi.")
WA_LAM = lambda: tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates the present, turns it to the past and governs jazm.", "«ve» + lem: nefiy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")])
def JAZM_V(full, lex, extra=None, punct=None, by="لَمْ", by_en="لَمْ", by_tr="lem", hidden=None, note_ar="", note_en="", note_tr=""):
    """يَصْبِرْ، يَخْرُجْ: a present verb in jazm by the sukun; hidden = the hidden doer's pronoun, or None when the doer follows"""
    hid = ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + hidden) if hidden else "، وَالْفَاعِلُ بَعْدَهُ"
    hid_en = ("; the doer is a hidden pronoun «" + hidden + "»") if hidden else "; its doer follows"
    hid_tr = ("; fâil gizli zamir «" + hidden + "»") if hidden else "; fâili ondan sonra gelir"
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari"] + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ" + by + " وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + hid + note_ar + ".",
        "Present verb in jazm by " + by_en + ", its sign the sukun" + hid_en + note_en + ".", by_tr + " ile meczûm muzâri, alâmeti sükûn" + hid_tr + note_tr + ".", punct=punct)
def FIVE_JAZM(full, lex, by, by_en, by_tr, extra=None, enc=None, punct=None):
    stem = full[:-len(enc)] if enc else full
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    segs = [seg(stem[:-1] if not enc else stem, lex, "verb")] + ([seg("ا", "pron-3mp", "pron")] if not enc else []) + ([seg(enc, PRON[enc], "pron")] if enc else [])
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil"] + (["maful-bihi"] if enc else []) + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ" + by + " وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + encs + ".",
        "Present verb in jazm by " + by_en + ", its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf'" + ("; the attached pronoun is its object" if enc else "") + ".",
        by_tr + " ile meczûm muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû" + ("; bitişik zamir mef'ûlün bih" if enc else "") + ".", punct=punct, segments=segs)
def FIVE_NASB(full, lex, extra=None, punct=None, by="أَنْ", by_en="أَنْ", by_tr="en", atf=False):
    """تَخْرُجُوا: one of the five verbs in nasb by the dropped nun; atf=True for a verb conjoined to one already in nasb"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    gov = ("مَعْطُوفٌ عَلَى الْمَنْصُوبِ قَبْلَهُ، مَنْصُوبٌ مِثْلَهُ", "conjoined to the verb in nasb before it and in nasb like it", "öncesindeki mansûb fiile ma'tûf, onun gibi mansûb") if atf else ("مَنْصُوبٌ بِـ" + by, "put in nasb by " + by_en, by_tr + " ile mansûb")
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil"] + (["atf-nasaq"] if atf else []) + (extra or []),
        ar0 + "فِعْلٌ مُضَارِعٌ " + gov[0] + " وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
        en0 + "present verb " + gov[1] + ", its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf'.",
        tr0 + gov[2] + " muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû.", punct=punct, segments=[s for s in [sg, seg(stem[:-1], lex, "verb"), seg("ا", "pron-3mp", "pron")] if s])
def VERB_WAW(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="", alif=False):
    """قَالُوا، جَاءُوا، دَعَوُا: a past verb with the waw of the group (alif=True for the naqis whose weak letter dropped)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    built = ("مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ", "built on a damma estimated on the alif, which dropped before the waw of the group", "cemâat vâvı önünde düşen elif üzerindeki takdîrî damme ile mebnî") if alif else ("مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ", "built on damma because the waw of the group is attached", "cemâat vâvı bitiştiği için damme üzere mebnî")
    return tok(full, lex, "verb", ["al-bariz-al-muttasil", "fail"] + (["naqis-verbs"] if alif else []) + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ " + built[0] + "، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note_ar + ".",
        en0 + "past verb " + built[1] + "; that waw is the doer, in the seat of raf'" + note_en + ".",
        tr0 + built[2] + " mâzî; vâv fâildir, mahallen merfû" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem[:-1], lex, "verb"), seg("ا", "pron-3mp", "pron")] if s])
def LAMMA2(full="وَلَمَّا", punct=None):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "lamma", "part", ["maful-fih", "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"],
        ar0 + "لَمَّا ظَرْفُ زَمَانٍ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
        en0 + "لَمَّا «when» is an adverb of time meaning «at the time that», built on sukun in the seat of nasb, annexed to the clause after it.",
        tr0 + "lemmâ: «…-diği zaman» anlamında zaman zarfı, sükûn üzere mebnî, mahallen mansûb; sonraki cümleye muzâf.", punct=punct, segments=[sg, seg(stem, "lamma", "part")] if sg else None)
LAMMA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause fills the seat of jarr, annexed to لَمَّا", "; cümle lemmâ'ya muzâfun ileyh olarak mahallen mecrûr")
def BI_NOUN(full, lex, stem, extra=None, punct=None, note_ar="", note_en="", note_tr="", pos="noun", sign="بِالْكَسْرَةِ", enc=None):
    segs = [seg("بِ", "bi", "prep")] + ([seg(stem[:-len(enc)], lex, pos), seg(enc, PRON[enc], "pron")] if enc else [seg(stem, lex, pos)])
    encs = ("، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ") if enc else ""
    return tok(full, "bi", "prep", ["huruf-jarr"] + (["idafa-definiteness", "al-bariz-al-muttasil"] if enc else []) + (extra or []),
        "الْبَاءُ حَرْفُ جَرٍّ، وَ" + (stem[:-len(enc)] if enc else stem) + " مَجْرُورٌ " + sign + encs + note_ar + ".", "The ba is a jarr letter; the noun after it is in jarr" + ("; it is annexed to the attached pronoun" if enc else "") + note_en + ".", "Bâ cer harfi; sonraki isim mecrûr" + ("; bitişik zamire muzâf" if enc else "") + note_tr + ".",
        punct=punct, segments=segs)
def LI_ENC(full, lex, stem, enc, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """لِجُنْدِهِ: the lam of jarr, its noun annexed to a pronoun"""
    return tok(full, "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَ" + stem + " مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        "The lam is a jarr letter; the noun after it is in jarr and annexed to the attached pronoun" + note_en + ".", "Lâm cer harfi; sonraki isim mecrûr, bitişik zamire muzâf" + note_tr + ".",
        punct=punct, segments=[seg("لِ", "li", "prep"), seg(stem, lex, "noun"), seg(enc, PRON[enc], "pron")])
LI_TALUT = lambda punct=None: tok("لِطَالُوتَ", "li", "prep", ["huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَطَالُوتَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "The lam is a jarr letter; the diptote name after it takes fatha in place of kasra.", "Lâm cer harfi; gayr-i munsarıf isim kesre yerine fetha ile mecrûr.", punct=punct, segments=[seg("لِ", "li", "prep"), seg("طَالُوتَ", "talut", "propn")])
def LAHU2(full, pron, pron_tr, punct=None, grammar=None, note=("", "", "")):
    return tok(full, "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + (grammar or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ" + note[0] + ".", "The lam is a jarr letter; the attached pronoun fills the seat of jarr" + note[1] + ".", "Lâm cer harfi; bitişik zamir mahallen mecrûr" + pron_tr + note[2] + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg(full[1:], pron, "pron")])
ILAYHI = lambda punct=None: JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)", punct=punct)
ALAYNA = lambda punct=None: JARR_PRON("عَلَيْنَا", "ala", "عَلَيْ", "نَا", " («üzerimize»)", punct=punct)
ALAYHIM = lambda punct=None: JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onların üzerine»)", punct=punct)
ALAYHI = lambda punct=None: JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («ona»)", punct=punct)
MINKUM = lambda punct=None: JARR_PRON("مِنْكُمْ", "min", "مِنْ", "كُمْ", " («sizden»)", punct=punct)
MAA_ENC = lambda punct=None: tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb and annexed to the pronoun «him».", "Mekân zarfı «ile», mansûb; «o» zamirine muzâf.", punct=punct, segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")])
ISHARA = lambda full, lex, seat_ar, seat_en, seat_tr, built_ar="السُّكُونِ", built_en="sukun", built_tr="sükûn", extra=None, punct=None: tok(full, lex, "pron", ["asma-al-ishara"] + (extra or []),
    "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى " + built_ar + " فِي مَحَلِّ " + seat_ar + ".", "A demonstrative, built on " + built_en + ", in the seat of " + seat_en + ".", "İşaret ismi, " + built_tr + " üzere mebnî, mahallen " + seat_tr + ".", punct=punct)
HADHA_J = lambda: ISHARA("هَذَا", "hadha", "جَرٍّ", "jarr", "mecrûr")
BI_HADHA = lambda: tok("بِهَذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "The ba is a jarr letter; the demonstrative after it is built on sukun, in the seat of jarr.", "Bâ cer harfi; işaret ismi sükûn üzere mebnî, mahallen mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("هَذَا", "hadha", "pron")])
HAULAI_J = lambda: ISHARA("هَؤُلَاءِ", "haulai", "جَرٍّ", "jarr", "mecrûr", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre")
def BADAL(full, lex, case, extra=None, punct=None, sign=None, note_ar="", note_en="", note_tr=""):
    s = sign or {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, lex, "noun", ["badal", "asma-al-ishara"] + (extra or []), "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ " + s + note_ar + ".", "A badal of the demonstrative, in the same case" + note_en + ".", "İşaret isminden bedel; aynı i'râbı alır" + note_tr + ".", punct=punct)
KULLUHUM = lambda punct=None: tok("كُلُّهُمْ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يُؤَكِّدُ الْفَاعِلَ قَبْلَهُ.", "A tawkid of meaning «all of them», in raf' like the doer it strengthens; annexed to the pronoun «them», which fills the seat of jarr.", "Ma'nevî te'kîd «hepsi», pekiştirdiği fâil gibi merfû; «onlar» zamirine muzâf, zamir mahallen mecrûr.", punct=punct, segments=[seg("كُلُّ", "kull", "noun"), seg("هُمْ", "pron-3mp", "pron")])
def INNA_ENC(full, enc, tr, punct=None, extra=None):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    lex = "lakinna" if stem.startswith("لَكِنَّ") else "inna"
    head = stem[:-len(enc)]; name_ar = "لَكِنَّ" if lex == "lakinna" else "إِنَّ"
    return tok(full, lex, "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"] + (extra or []),
        ar0 + name_ar + " حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهَا خَبَرُهَا فِي مَحَلِّ رَفْعٍ.",
        en0 + name_ar + " is the verb-like particle; the attached pronoun is its noun in the seat of nasb — the clause after it is its predicate, in the seat of raf'.",
        tr0 + name_ar + " fiile benzeyen harf; bitişik zamir ismi, mahallen mansûb — sonraki cümle haberi, mahallen merfû" + tr + ".",
        punct=punct, segments=[s for s in [sg, seg(head, lex, "part"), seg(enc, PRON[enc], "pron")] if s])
MUDARI_DF = lambda full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="": tok(full, lex, "verb", ["mudari-marfu"] + (extra or []),
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ" + note_ar + ".", "Present verb in raf'; its doer follows" + note_en + ".", "Merfû muzâri; fâili ondan sonra gelir" + note_tr + ".", punct=punct)
SILA = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
RAAW = lambda full="رَأَوْا", punct=None, note=("", "", ""): tok(full, "raa", "verb", ["thulathi-mujarrad-babs", "naqis-verbs", "al-bariz-al-muttasil", "fail"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note[0] + ".",
    "Past verb built on a damma estimated on the alif, which drops before the waw of the group; the waw is its doer, in the seat of raf'" + note[1] + ".",
    "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî damme ile mebnî mâzî; cemâat vâvı fâil, mahallen merfû" + note[2] + ".", punct=punct, segments=[seg(full[:-1], "raa", "verb"), seg("ا", "pron-3mp", "pron")])
MAN_SHART = lambda full="فَمَنْ": tok(full, "man", "pron", ["al-majzum-wal-shart-wal-jaza", "mubtada-khabar", "al-mabni-wal-mudmar"], (FA_AR if full.startswith("فَ") else WA_AR) + "مَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُهُ.", ("The fa conjoins; " if full.startswith("فَ") else "The waw conjoins; ") + "مَنْ «whoever» is the conditional noun that governs jazm, built on sukun in the seat of raf' as mubtada; the condition and its answer are its khabar.", ("«bunun üzerine» + " if full.startswith("فَ") else "«ve» + ") + "men «kim …-sa»: cezm eden şart ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû; şart ve cevap cümleleri haberidir.", segments=[seg(full[:2], "fa" if full.startswith("فَ") else "wa", "conj"), seg("مَنْ", "man", "pron")])
SHART_V = lambda full, lex, extra=None: tok(full, lex, "verb", ["al-majzum-wal-shart-wal-jaza"] + (extra or []), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Past verb built on fatha, in the seat of jazm as the condition's verb; the doer «he» is hidden.", "Fetha üzere mebnî mâzî, şart fiili olarak mahallen meczûm; fâil gizli zamir «o».")
JAWAB_MADI = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "; the clause fills the seat of jazm as the condition's answer", "; cümle şartın cevabı olarak mahallen meczûm")
PRON_MUB = lambda full, lex, built="الْفَتْحِ", built_en="fatha", built_tr="fetha", punct=None, pre=None: tok(full, lex, "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"] + (["al-hal-jumla-wa-rabituha"] if pre == "hal" else []),
    ("الْوَاوُ حَالِيَّةٌ، وَ" if pre == "hal" else WA_AR if pre == "wa" else FA_AR if pre == "fa" else "") + "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى " + built + " فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ" + (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ" if pre == "hal" else "") + ".",
    ("The waw opens a hal clause; " if pre == "hal" else "The waw conjoins; " if pre == "wa" else "The fa conjoins; " if pre == "fa" else "") + "a detached pronoun built on " + built_en + ", in the seat of raf' as mubtada" + (" — the clause is a hal, in the seat of nasb" if pre == "hal" else "") + ".",
    ("Hâl vâvı; " if pre == "hal" else "«ve» + " if pre == "wa" else "«bunun üzerine» + " if pre == "fa" else "") + "munfasıl zamir, " + built_tr + " üzere mebnî, mübtedâ olarak mahallen merfû" + (" — cümle hâl olarak mahallen mansûb" if pre == "hal" else "") + ".",
    punct=punct, segments=[seg(full[:2], "wa" if full.startswith("وَ") else "fa", "conj"), seg(full[2:], lex, "pron")] if pre else None)
KAYFA_HAL = lambda full="كَيْفَ", punct=None: tok(full, "kayfa", "noun", ["al-istifham", "hal"], (FA_AR if full.startswith("فَ") else "") + "كَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", ("The fa conjoins; " if full.startswith("فَ") else "") + "كَيْفَ «how» is an interrogative noun built on fatha, in the seat of nasb as a hal.", ("«bunun üzerine» + " if full.startswith("فَ") else "") + "keyfe «nasıl»: istifhâm ismi, fetha üzere mebnî, hâl olarak mahallen mansûb.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg("كَيْفَ", "kayfa", "noun")] if full.startswith("فَ") else None)
WA_QAD = lambda: tok("وَقَدْ", "qad", "part", ["al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُمَا فِي مَحَلِّ نَصْبٍ حَالٌ.", "The waw opens a hal clause; قَدْ affirms the past — the clause is a hal, in the seat of nasb.", "Hâl vâvı; kad tahkîk harfi — sonraki cümle hâl olarak mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")])
QAD_K = lambda: tok("قَدِ", "qad", "part", [], "قَدْ حَرْفُ تَحْقِيقٍ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "قَدْ affirms the past; it is voweled with kasra before the following hamzat al-waṣl.", "Kad tahkîk harfi; iki sâkin karşılaştığı için kesre ile harekelendi.")
QAD = lambda: tok("قَدْ", "qad", "part", [], "قَدْ حَرْفُ تَحْقِيقٍ.", "قَدْ affirms the past verb after it.", "Kad tahkîk harfi.")
WA_LAW = lambda: tok("وَلَوْ", "law", "part", ["huruf-al-shart-fil-kafiya", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ، وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "The waw opens a hal clause; لَوْ «even if» is a conditional particle that governs no jazm; the clause after it is a hal, in the seat of nasb.", "Hâl vâvı; lev «…-se bile»: cezm etmeyen şart harfi; sonraki cümle hâl olarak mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("لَوْ", "law", "part")])
MAWSUL_MAF = lambda full, lex, built="الْفَتْحِ", built_en="fatha", built_tr="fetha", second=False: tok(full, lex, "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى " + built + " فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + (" ثَانٍ" if second else "") + ".", "A relative pronoun built on " + built_en + ", in the seat of nasb as the " + ("second " if second else "") + "object.", "İsm-i mevsûl, " + built_tr + " üzere mebnî, " + ("ikinci " if second else "") + "mef'ûlün bih olarak mahallen mansûb.")
ALLADHI_NAAT = lambda: tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِلَفْظِ الْجَلَالَةِ.", "A relative pronoun built on sukun, in the seat of nasb as a na't of the Name of Majesty.", "İsm-i mevsûl, sükûn üzere mebnî, lafza-i celâlin na'tı olarak mahallen mansûb.")
def WIQAYA_V(full, lex, stem, tense_ar, tense_en, tense_tr, extra=None, punct=None, hidden="هُوَ", wujub=False, note_ar="", note_en="", note_tr="", pre=None):
    """يُقَاتِلُنِي، نَجَّانِي، أَتُقَاتِلُنِي: a verb with the nun of guarding and the speaker's ya as object"""
    segs = ([seg("أَ", "hamza-istifham", "part")] if pre == "a" else []) + [seg(stem, lex, "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]
    hid = ("، وَالْفَاعِلُ مُسْتَتِرٌ " + ("وُجُوبًا " if wujub else "") + "تَقْدِيرُهُ: " + hidden) if hidden else ""
    return tok(full, lex, "verb", ["ya-al-mutakallim", "al-bariz-al-muttasil", "maful-bihi"] + (["al-istifham"] if pre == "a" else []) + (extra or []),
        ("الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَ" if pre == "a" else "") + tense_ar + hid + "، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note_ar + ".",
        ("The hamza asks a question; " if pre == "a" else "") + tense_en + (("; the doer «" + hidden + "» is hidden" + (" of necessity" if wujub else "")) if hidden else "") + "; the nun guards the verb's ending and the ya of the speaker is its object, in the seat of nasb" + note_en + ".",
        ("İstifhâm hemzesi; " if pre == "a" else "") + tense_tr + (("; fâil gizli zamir «" + hidden + "»") if hidden else "") + "; nûn vikâye içindir, mütekellim yâ'sı mef'ûlün bih — mahallen mansûb" + note_tr + ".", punct=punct, segments=segs)
def MAJHUL_NA(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """أُخْرِجْنَا: the passive past with «we» as its deputy doer"""
    return tok(full, lex, "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "al-bariz-al-muttasil"] + (extra or []),
        "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ" + note_ar + ".",
        "A past verb in the passive, built on sukun before the attached «we»; that نَا is the deputy doer, in the seat of raf'" + note_en + ".",
        "Meçhul mâzî, «biz» zamiri bitiştiği için sükûn üzere mebnî; nâ nâib-i fâil, mahallen merfû" + note_tr + ".", punct=punct, segments=[seg(full[:-2], lex, "verb"), seg("نَا", "pron-1p", "pron")])
def YA_MUTAKALLIM_N(full, lex, stem, role_ar, role_en, role_tr, extra=None, punct=None, prep=None):
    """جُنْدِي، بِرَبِّي: a noun annexed to the speaker's ya (optionally under a jarr letter)"""
    segs = ([seg(prep[0], prep[1], "prep")] if prep else []) + [seg(stem, lex, "noun"), seg("ي", "pron-1s", "pron")]
    # (wave 128) the estimated vowel is the CASE's vowel, hidden by the kasra the yāʾ demands: ḍamma for rafʿ, fatḥa for naṣb,
    # kasra for jarr — the helper used to write «kasra» for every case, and the SignEngine's audit caught the marfūʿ lines
    vowel = "بِضَمَّةٍ" if "مَرْفُوع" in role_ar else "بِفَتْحَةٍ" if "مَنْصُوب" in role_ar else "بِكَسْرَةٍ"
    hidden_by = "" if vowel == "بِكَسْرَةٍ" else " مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ"
    return tok(full, (prep[1] if prep else lex), ("prep" if prep else "noun"), ["ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"] + (["huruf-jarr"] if prep else []) + (extra or []),
        (prep[2] + "، وَ" if prep else "") + stem + " " + role_ar + " " + vowel + " مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ" + hidden_by + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        (prep[3] + "; " if prep else "") + role_en + " — the vowel is estimated before the speaker's ya; the noun is annexed, and the ya is the second term of the idafa in the seat of jarr.",
        (prep[4] + "; " if prep else "") + role_tr + " — hareke mütekellim yâ'sından önce takdîrîdir; isim muzâf, yâ muzâfun ileyh — mahallen mecrûr.", punct=punct, segments=segs)
BANU_ISMK = lambda: tok("بَنُو", "banu", "noun", ["kana-wa-akhawatuha", "jam-mudhakkar-salim", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "The noun of كَانَ, in raf' — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa.", "Kâne'nin ismi, merfû — cem-i müzekker sâlime mülhak, vâv ile merfû; nûnu izâfet için düşmüş, muzâf.")
BANU_F = lambda: tok("بَنُو", "banu", "noun", ["fail", "jam-mudhakkar-salim", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "The doer (fa'il), in raf' — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa.", "Fâil, merfû — cem-i müzekker sâlime mülhak, vâv ile merfû; nûnu izâfet için düşmüş, muzâf.")
ISRAIL_MI = lambda punct=None: tok("إِسْرَائِيلَ", "israil", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "The second term of the idafa, in jarr — a foreign proper name, barred from tanwin.", "Muzâfun ileyh, mecrûr — yabancı özel isim, gayr-i munsarif.", punct=punct)
SALIM_J = lambda full, lex, role, extra=None, punct=None: tok(full, lex, "noun", [role[3], "jam-mudhakkar-salim"] + (extra or []), role[0] + " بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", role[1] + " — by the ya, a sound masculine plural.", role[2] + " — cem-i müzekker sâlim olduğu için yâ ile.", punct=punct)
R_NAAT_J = ("نَعْتٌ مَجْرُورٌ", "An adjective agreeing with its noun, in jarr", "Na't, mevsûfuna uyar; mecrûr", "naat-sifa")
R_MAF = ("مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", "maful-bihi")
R_BADAL_J = ("بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ", "A badal of the demonstrative, in jarr", "İşaret isminden bedel, mecrûr", "badal")
DEPUTY_MUTLAQ = lambda full, lex, punct=None, verb="شَرِبَ": tok(full, lex, "noun", ["maful-mutlaq", "sifa-mushabbaha"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ، أَيْ: شُرْبًا " + full.replace("ً", "") + "ً.", "Stands in for the absolute object, in nasb — an adjective of an omitted masdar («a little/much drinking»).", "Mef'ûlün mutlakın nâibi, mansûb — hazfedilmiş masdarın sıfatı («az/çok içmek»).", punct=punct)
MUTLAQ = lambda full, lex, punct=None: tok(full, lex, "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ الْفِعْلِ قَبْلَهُ، يُؤَكِّدُهُ.", "The absolute object (maf'ul mutlaq), in nasb — the verb's own masdar, strengthening it.", "Mef'ûlün mutlak, mansûb — fiilin kendi masdarı; onu pekiştirir.", punct=punct)
TAMYIZ = lambda full, lex, punct=None: tok(full, lex, "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ جِهَةَ التَّفْضِيلِ.", "A specifier (tamyiz), in nasb — it names the respect in which the comparison holds.", "Temyîz, mansûb — üstünlüğün hangi yönden olduğunu belirtir.", punct=punct)
LAYSA_HID = lambda full="فَلَيْسَ", note=("", "", ""): tok(full, "laysa", "verb", ["kana-wa-akhawatuha"] + (["al-fa-fi-jawab-al-shart", "al-majzum-wal-shart-wal-jaza"] if full.startswith("فَ") else []),
    ("الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَ" if full.startswith("فَ") else WA_AR if full.startswith("وَ") else "") + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + note[0] + ".",
    ("The fa binds the condition's answer; " if full.startswith("فَ") else "The waw conjoins; " if full.startswith("وَ") else "") + "لَيْسَ «is not» is the frozen defective verb; its noun is the hidden pronoun «he»" + note[1] + ".",
    ("Fâ şartın cevabını bağlar; " if full.startswith("فَ") else "«ve» + " if full.startswith("وَ") else "") + "leyse: câmid nâkıs fiil; ismi gizli zamir «o»" + note[2] + ".", segments=[seg(full[:2], "fa" if full.startswith("فَ") else "wa", "conj"), seg("لَيْسَ", "laysa", "verb")] if full[0] in "وف" else None)
KH_LAYSA = ("، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ", "; the jarr phrase is the predicate of لَيْسَ", "; câr-mecrûr leyse'nin haberidir")
JAWAB_T = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "; the clause fills the seat of jazm as the condition's answer", "; cümle şartın cevabı olarak mahallen meczûm")
MUMININ_MAF = lambda punct=None: SALIM_J("الْمُؤْمِنِينَ", "mumin", R_MAF, ["ism-fail"], punct=punct)
SABIRIN_J = lambda punct=None: SALIM_J("الصَّابِرِينَ", "sabir", R_NAAT_J, ["ism-fail"], punct=punct)
SABIRIN_MAF = lambda punct=None: SALIM_J("الصَّابِرِينَ", "sabir", R_MAF, ["ism-fail"], punct=punct)
KAFIRIN_BADAL = lambda punct=None: SALIM_J("الْكَافِرِينَ", "kafir", R_BADAL_J, ["ism-fail", "asma-al-ishara"], punct=punct)
QALA_H = lambda full="وَقَالَ", punct=":": QALA(full, hidden=True, punct=punct)
AMR5 = lambda full, lex, extra=None, punct=None: AMR(full, lex, extra, punct=punct, waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi")

IDHA = lambda full="وَإِذَا": tok(full, "idha", "noun", ["huruf-al-shart-fil-kafiya", "maful-fih"], (WA_AR if full.startswith("وَ") else "") + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ، خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ، مَبْنِيٌّ عَلَى السُّكُونِ.", ("The waw conjoins; " if full.startswith("وَ") else "") + "إِذَا «when»: the adverb of future time that governs its condition and is governed by its answer; built on sukun.", ("«ve» + " if full.startswith("وَ") else "") + "izâ «-dığı zaman»: gelecek zaman zarfı, şartına muzâf ve cevabıyla mansûb; sükûn üzere mebnî.", segments=[seg("وَ", "wa", "conj"), seg("إِذَا", "idha", "noun")] if full.startswith("وَ") else None)
WA_LA_NAHIYA = lambda: tok("وَلَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], WA_AR + "لَا النَّاهِيَةُ حَرْفُ نَهْيٍ وَجَزْمٍ.", "The waw conjoins; the prohibitive لَا governs jazm.", "«ve» + nehiy lâ'sı: nehiy ve cezm harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nahiya", "part")])
KAMA = lambda: tok("كَمَا", "kama", "part", ["huruf-jarr", "an-masdariyya"], "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَمَا مَصْدَرِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْكَافِ.", "The kaf is a jarr letter of likeness and مَا builds a masdar: «just as …»; the clause stands in jarr after the kaf.", "Kâf teşbîh için cer harfi, mâ masdariyye: «…-diği gibi»; müevvel masdar kâf ile mecrûr.")
HAKADHA = lambda: tok("وَهٰكَذَا", "hakadha", "pron", ["asma-al-ishara", "maful-fih"], WA_AR + "هَا لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ — وَالْمَجْمُوعُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ: كَانَ كَوْنًا هٰكَذَا.", "The waw resumes; «thus»: the hā of alerting, the kāf of likeness and the demonstrative, together in the seat of nasb as the description of an omitted verbal noun.", "«ve» + «işte böyle»: tenbih hâ'sı, teşbih kâfı ve işaret ismi; bütünü hazfedilmiş masdarın sıfatı olarak mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("هٰكَذَا", "hakadha", "pron")])
# ============ «جُحَا وَالْحِمَارُ» — the twentieth ORIGINAL story, the twelfth at Level 2 (wave 110): the folk tale of Juḥā, his son and the donkey ============
def DUAL_MADI(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """أَكَلَا، نَسِيَا، قَالَا: a past verb with the alif of the two as its doer"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, lex, "verb", ["al-muthanna", "fail", "al-bariz-al-muttasil"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note_ar + ".",
        en0 + "past verb built on fatha; the alif of the two is its doer, in the seat of raf'" + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî; tesniye elifi fâil, mahallen merfû" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem[:-1], lex, "verb"), seg("ا", "pron-3d", "pron")] if s])
def DUAL_ENC_MADI(full, lex, enc, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """عَصَيَا رَبَّهُمَا is not this — this is a dual verb whose object is an enclitic (not used yet; kept for symmetry)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    stem_v = stem[:-len(enc)]
    return tok(full, lex, "verb", ["al-muthanna", "fail", "al-bariz-al-muttasil", "maful-bihi"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note_ar + ".",
        en0 + "past verb built on fatha; the alif of the two is its doer and the attached pronoun its object" + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî; tesniye elifi fâil, bitişik zamir mef'ûl" + note_tr + ".",
        punct=punct, segments=[s for s in [sg, seg(stem_v[:-1], lex, "verb"), seg("ا", "pron-3d", "pron"), seg(enc, PRON[enc], "pron")] if s])
WA_LAM = lambda: tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates, governs jazm and turns the present to the past.", "«ve» + lem: nefy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")])
BIMA = lambda: tok("بِمَا", "bi", "prep", ["huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.", "The ba is a jarr letter; مَا «what» is the relative pronoun, built on sukun, in the seat of jarr.", "Bâ cer harfi; mâ ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")])
LIANNAHU = lambda: tok("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "huruf-jarr"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "The lam gives the reason; أَنَّ is the verb-like particle and the attached «He» is its noun in the seat of nasb.", "Lâm ta'lîl içindir; enne te'kîd ve nasb harfi; «O» ismi, mahallen mansûb.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")])
KH_ANNA = lambda full, lex, extra=None, punct=None: tok(full, lex, "noun", ["inna-wa-akhawatuha"] + (extra or []), "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of أَنَّ, in raf'.", "Enne'nin haberi, merfû.", punct=punct)
AKHAR_NAAT = lambda full, case, punct=None: NAAT(full, "akhar", case, ["mamnu-min-sarf"], note_ar="، وَآخَرُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، فَلَا يُنَوَّنُ", note_en=" — آخَر «another» is barred from tanwin (an adjective on the أَفْعَل pattern)", note_tr=" — âhar vasfiyet ve ef'al vezni sebebiyle gayr-i munsarıf; tenvin almaz", punct=punct)
ANNAHU = lambda note=("", "", ""): tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا" + note[0] + ".", "أَنَّ is the verb-like particle; the attached «he» is its noun in the seat of nasb" + note[1] + ".", "Enne te'kîd ve nasb harfi; bitişik «o» ismi, mahallen mansûb" + note[2] + ".", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")])
HATTA_IBT = lambda: tok("حَتَّى", "hatta", "part", ["huruf-jarr"], "حَرْفُ غَايَةٍ وَابْتِدَاءٍ، وَمَا بَعْدَهُ جُمْلَةٌ مُسْتَأْنَفَةٌ.", "حَتَّى «until» here opens a new clause (the ibtidāʾ use); the past verb after it is a sentence of its own.", "Hattâ «nihayet»: ibtidâ içindir; sonraki mâzî fiil müste'nef cümledir.")
JUHA_NOTE = ("، وَجُحَا اسْمٌ مَقْصُورٌ تُقَدَّرُ عَلَى أَلِفِهِ الْحَرَكَاتُ كُلُّهَا لِلتَّعَذُّرِ", " — جُحَا is a maqṣūr name: every case vowel is estimated on its alif", " — Cuhâ maksûr isimdir: bütün harekeler elifi üzerinde takdîrîdir")
JUHA_F = lambda punct=None: FAIL("جُحَا", "juha", "propn", ["ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", note_ar=JUHA_NOTE[0], note_en=JUHA_NOTE[1], note_tr=JUHA_NOTE[2], punct=punct)
JUHA_MI = lambda punct=None: MUDAF_ILAYH("جُحَا", "juha", "propn", ["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", note_ar=JUHA_NOTE[0], note_en=JUHA_NOTE[1], note_tr=JUHA_NOTE[2], punct=punct)
HIMAR_F = lambda punct=None: FAIL("الْحِمَارُ", "himar", punct=punct)
NAS_F = lambda punct=None: FAIL("النَّاسُ", "nas", punct=punct)
IBNUHU_F = lambda punct=None: ENC_NOUN("ابْنُهُ", "ibn", "هُ", "fail", punct=punct)
IBNAHU = lambda punct=None, note=("", "", ""): ENC_NOUN("ابْنَهُ", "ibn", "هُ", "maful", note_ar=note[0], note_en=note[1], note_tr=note[2], punct=punct)
LI_IBNIHI = lambda punct=None: LI_ENC("لِابْنِهِ", "ibn", "ابْنِ", "هِ", punct=punct)
MAAHUMA_KH = lambda pre="", punct=None: tok(pre + "مَعَهُمَا", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar", "al-hal-jumla-wa-rabituha"], ("الْوَاوُ حَالِيَّةٌ، وَ" if pre else "") + "مَعَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِخَبَرٍ مُقَدَّمٍ مَحْذُوفٍ" + ("، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ" if pre else "") + ".", ("The waw opens a hal clause; " if pre else "") + "the adverb «with» in nasb, annexed to «the two of them», hangs on an omitted fronted predicate" + ("; the clause is a hal in the seat of nasb" if pre else "") + ".", ("Hâl vâvı; " if pre else "") + "mansûb zarf «ile», «o ikisi»ne muzâf — mahzûf öne alınmış habere müteallık" + ("; cümle hâl, mahallen mansûb" if pre else "") + ".", punct=punct, segments=([seg("وَ", "wa", "conj")] if pre else []) + [seg("مَعَ", "maa", "noun"), seg("هُمَا", "pron-3d", "pron")])
KHALFAHU = lambda punct=None: tok("خَلْفَهُ", "khalf", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "An adverb of place «behind», in nasb, annexed to «him».", "Mekân zarfı «arkasında», mansûb, «o»na muzâf.", punct=punct, segments=[seg("خَلْفَ", "khalf", "noun"), seg("هُ", "pron-3ms", "pron")])
DUAL_ENC_MAJR = lambda full, lex, enc, extra=None, punct=None: tok(full, lex, "noun", ["al-muthanna", "huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []), "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَ" + PRON_AR[enc] + " مُضَافٌ إِلَيْهِ.", "In jarr by the ya — a dual whose nun drops before the annexed pronoun.", "Tesniye olduğu için yâ ile mecrûr; izâfet sebebiyle nûnu düşmüş; zamir muzâfun ileyh.", punct=punct, segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
MARRA_BIHIMA = lambda pre: [MADI(pre + "مَرَّ", "marra", ["doubled-verbs"]), JARR_PRON("بِهِمَا", "bi", "بِ", "هِمَا", " («o ikisine»)"), FAIL("قَوْمٌ", "qawm", note_ar=" — فَاعِلٌ مُؤَخَّرٌ بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en=" — the doer, placed after the jarr phrase", note_tr=" — câr-mecrûrdan sonraya bırakılmış fâil")]
UNZURU = lambda: AMR("انْظُرُوا", "nazara", waw=True)
QASI_NAAT = lambda punct=None: tok("الْقَاسِي", "qasin", "noun", ["naat-sifa", "ism-maqsur-manqus", "ism-fail"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ مُعَرَّفٌ بِأَلْ، فَتَثْبُتُ يَاؤُهُ.", "An adjective in jarr by a kasra estimated on the ya — a manqūṣ noun with the article, so its ya stays.", "Na't, yâ üzerindeki takdîrî kesre ile mecrûr — harf-i tarifli mankûs isim; yâ'sı sabit kalır.", punct=punct)
HAL_CL_MUDARI = lambda full, lex, extra=None, punct=None, who="هُوَ": MUDARI(full, lex, extra, punct=punct, who=who, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", note_en=" — the clause is a hal, in the seat of nasb", note_tr=" — cümle hâl, mahallen mansûb")
MAKANAHU = lambda punct=None: tok("مَكَانَهُ", "makan", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "An adverb of place «in his place», in nasb, annexed to «him».", "Mekân zarfı «onun yerine», mansûb, «o»na muzâf.", punct=punct, segments=[seg("مَكَانَ", "makan", "noun"), seg("هُ", "pron-3ms", "pron")])
MA_TAAJJUB = lambda: tok("مَا", "ma-taajjubiyya", "pron", ["fil-al-taajjub-fil-kafiya", "mubtada-khabar"], "مَا التَّعَجُّبِيَّةُ نَكِرَةٌ تَامَّةٌ بِمَعْنَى «شَيْءٌ»، مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The مَا of wonder — an indefinite «something», built on sukun in the seat of raf' as mubtada.", "Taaccüb mâ'sı — «bir şey» mânâsında tam nekre; sükûn üzere mebnî, mübtedâ olarak mahallen merfû.")
AAJABA = lambda: tok("أَعْجَبَ", "aajaba", "verb", ["fil-al-taajjub-fil-kafiya", "form-iv-verbs"], "فِعْلُ تَعَجُّبٍ مَاضٍ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا يَعُودُ عَلَى مَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ مَا.", "The frozen verb of wonder (أَفْعَلَ), built on fatha; its hidden doer refers back to مَا — the clause is the predicate of مَا.", "Câmid taaccüb fiili (ef'ale), fetha üzere mebnî; fâil vücûben gizli, mâ'ya râci — cümle mâ'nın haberi.")
MUTAAJJAB = lambda full, lex, punct=None: MAFUL(full, lex, extra=["fil-al-taajjub-fil-kafiya"], note_ar=" — الْمُتَعَجَّبُ مِنْهُ", note_en=" — the thing wondered at", note_tr=" — müteaccebün minh", punct=punct)
ABUHU = lambda pre="", punct=None: tok(pre + "أَبُوهُ", "ab", "noun", ["five-nouns", "mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"] + (["al-hal-jumla-wa-rabituha"] if pre else []), ("الْوَاوُ حَالِيَّةٌ، وَ" if pre else "") + "أَبُو مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ" + ("، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ" if pre else "") + ".", ("The waw opens a hal clause; " if pre else "") + "«his father» is the mubtada, in raf' by the waw — one of the five nouns, annexed to «his»" + ("; the clause is a hal" if pre else "") + ".", ("Hâl vâvı; " if pre else "") + "«babası» mübtedâ, esmâ-i hamseden olduğu için vâv ile merfû; «onun»a muzâf" + ("; cümle hâl" if pre else "") + ".", punct=punct, segments=([seg("وَ", "wa", "conj")] if pre else []) + [seg("أَبُو", "ab", "noun"), seg("هُ", "pron-3ms", "pron")])
KH_CL_MUDARI = lambda full, lex, extra=None, punct=None, who="هُوَ": MUDARI(full, lex, extra, punct=punct, who=who, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en=" — the clause is the predicate", note_tr=" — cümle haberdir")
DUAL_SARA = lambda: tok("فَصَارَا", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-muthanna", "al-bariz-al-muttasil"], FA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَأَلِفُ الِاثْنَيْنِ اسْمُهُ فِي مَحَلِّ رَفْعٍ.", "The fa conjoins; صَارَ «became» is a sister of كَانَ; the alif of the two is its noun in the seat of raf'.", "«bunun üzerine» + nâkıs fiil sâra; tesniye elifi ismi, mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("صَارَ", "sara", "verb"), seg("ا", "pron-3d", "pron")])
DUAL_MUDARI = lambda full, lex, role, extra=None, punct=None: tok(full, lex, "verb", ["afal-khamsa", "al-muthanna", "al-bariz-al-muttasil", "mudari-marfu"] + (extra or []), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ" + role[0] + ".", "Present verb in raf' by the retained nun (one of the five verbs); the alif of the two is its doer" + role[1] + ".", "Nûnun sübûtu ile merfû muzâri (ef'âl-i hamseden); tesniye elifi fâil" + role[2] + ".", punct=punct, segments=[seg(full[:-len("انِ")], lex, "verb"), seg("انِ", "pron-3d", "pron")])
A_LA = lambda: tok("أَلَا", "ala-ard", "part", ["al-istifham", "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ دَخَلَتْ عَلَى لَا النَّافِيَةِ — وَمَجْمُوعُهُمَا لِلْعَرْضِ وَالتَّوْبِيخِ.", "The hamza of reproachful question on the negating لَا — together an urging «will you not…?».", "İnkârî istifhâm hemzesi nefiy lâ'sının üzerine gelmiş — bütünü arz ve tevbîh için «…-mez misiniz?».", segments=[seg("أَ", "hamza-istifham", "part"), seg("لَا", "la-nafiya", "part")])
ITHNANI = lambda: tok("اثْنَانِ", "ithnan", "noun", ["mubtada-khabar", "al-muthanna", "asma-al-adad-fil-kafiya"], "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ.", "The mubtada «two», in raf' by the alif — it declines like a dual; its nun stands for the tanwin.", "Mübtedâ «iki», tesniyeye mülhak olduğu için elif ile merfû; nûn tenvinin karşılığı.")
BI_LA = lambda full, lex, stem, punct=None: tok(full, "bi", "prep", ["huruf-jarr", "la-nafiya"], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا نَافِيَةٌ زَائِدَةٌ بَيْنَ الْجَارِّ وَالْمَجْرُورِ، وَ" + stem + " مَجْرُورٌ بِالْكَسْرَةِ.", "The ba is a jarr letter; لَا «no» slips in between it and its noun, which stays in jarr — «with no …».", "Bâ cer harfi; nefiy lâ'sı câr ile mecrûr arasına girmiş; isim mecrûr — «…-sız».", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part"), seg(stem, lex, "noun")])
WA_HUWA_HAL = lambda: PRON_MUB("وَهُوَ", "huwa", pre="hal")
WA_HUMA_HAL = lambda: tok("وَهُمَا", "huma", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar", "al-hal-jumla-wa-rabituha", "al-muthanna"], "الْوَاوُ حَالِيَّةٌ، وَهُمَا ضَمِيرٌ مُنْفَصِلٌ لِلْمُثَنَّى مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "The waw opens a hal clause; «they two» is the detached dual pronoun, built on sukun, in the seat of raf' as mubtada.", "Hâl vâvı; «o ikisi» tesniye munfasıl zamiri, sükûn üzere mebnî, mübtedâ olarak mahallen merfû — cümle hâl.", segments=[seg("وَ", "wa", "conj"), seg("هُمَا", "huma", "pron")])
HADHAYNI = lambda: tok("هٰذَيْنِ", "hadhani", "pron", ["asma-al-ishara", "al-muthanna"], "اسْمُ إِشَارَةٍ لِلْمُثَنَّى مَجْرُورٌ بِالْيَاءِ (يُعْرَبُ إِعْرَابَ الْمُثَنَّى).", "The dual demonstrative «these two», in jarr by the ya — it declines like a dual.", "Tesniye işaret ismi «bu ikisi», yâ ile mecrûr (tesniye gibi i'râb olunur).")
AHMAQAYNI = lambda punct=None: tok("الْأَحْمَقَيْنِ", "ahmaq", "noun", ["badal", "al-muthanna", "mamnu-min-sarf"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — وَمُفْرَدُهُ أَحْمَقُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ.", "A substitute for the demonstrative, in jarr by the ya — a dual; its singular أَحْمَقُ is a diptote (an adjective on أَفْعَل).", "İşaret isminden bedel, tesniye olduğu için yâ ile mecrûr — müfredi ahmak, ef'al vezninde gayr-i munsarıf sıfat.", punct=punct)
LAM_YABQA = lambda: [LAM_JAZM(), tok("يَبْقَ", "baqiya", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (يَبْقَى ← يَبْقَ)، وَالْفَاعِلُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَ إِلَّا.", "The defective present verb in jazm by لَمْ, its sign the dropped weak letter (يَبْقَى → يَبْقَ); its doer is the clause after إِلَّا.", "Lem ile meczûm nâkıs muzâri, alâmeti illet harfinin hazfi (yebkâ → yebka); fâili illâ'dan sonraki masdar-ı müevvel.")]
ILLA_FAIL = lambda: tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ فَاعِلُ يَبْقَ.", "The particle of the emptied exception; the أَنْ-clause after it is the doer of «remains», in the seat of raf'.", "Müferrağ istisnâ edatı; sonraki masdar-ı müevvel, yebka'nın fâili olarak mahallen merfû.")
RAAHUMA = lambda: tok("رَآهُمَا", "raa", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَكُتِبَتِ الْهَمْزَةُ وَالْأَلِفُ مَدَّةً.", "Past verb built on a fatha estimated on the alif; «the two of them» is its attached object; the doer follows — hamza and alif are written as one madda.", "Elif üzerindeki takdîrî fetha ile mebnî mâzî; «o ikisi» bitişik mef'ûl; fâil ondan sonra gelir — hemze ile elif medde olarak yazılmıştır.", segments=[seg("رَآ", "raa", "verb"), seg("هُمَا", "pron-3d", "pron")])
MA_NAFIYA = lambda: tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا النَّافِيَةُ، لَا عَمَلَ لَهَا مَعَ الْفِعْلِ.", "The negating مَا, which governs nothing before a verb.", "Nefiy mâ'sı; fiil önünde amel etmez.")
QATTU = lambda punct=None: tok("قَطُّ", "qattu", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ زَمَانٍ لِاسْتِغْرَاقِ الْمَاضِي الْمَنْفِيِّ، مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The adverb «ever» covering all the negated past, built on damma in the seat of nasb.", "Menfî mâzînin tamamını kapsayan zaman zarfı «hiç», damme üzere mebnî, mahallen mansûb.", punct=punct)
KHUDH = lambda: AMR("خُذْ", "akhadha", note_ar=" — وَحُذِفَتْ هَمْزَةُ أَخَذَ فِي أَمْرِهِ", note_en=" — the hamza of أَخَذَ is dropped in its imperative", note_tr=" — ehaze'nin emrinde hemzesi düşer")
SHART_HOLLOW = lambda full, lex, punct=None: tok(full, lex, "verb", ["al-majzum-wal-shart-wal-jaza", "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Past verb built on fatha, in the seat of jazm as the condition's verb; the doer «he» is hidden.", "Fetha üzere mebnî mâzî, şart fiili olarak mahallen meczûm; fâil gizli «o».", punct=punct)
YURDIYA = lambda: MANSUB_AN("يُرْضِيَ", "arda", ["form-iv-verbs", "naqis-verbs"], note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha shows on the ya, which bears it easily", note_tr=" — fetha hafif olduğu için yâ üzerinde zâhirdir")
LAM_YURDI = lambda: [LAM_JAZM(), tok("يُرْضِ", "arda", "verb", ["nawasib-wa-jawazim-al-mudari", "al-majzum-wal-shart-wal-jaza", "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (يُرْضِي ← يُرْضِ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَجُمْلَةُ لَمْ وَمَا بَعْدَهَا جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "Present verb in jazm by لَمْ, its sign the dropped weak letter (يُرْضِي → يُرْضِ); the doer «he» is hidden — the لَمْ-clause is the condition's answer.", "Lem ile meczûm muzâri, alâmeti illet harfinin hazfi (yurdî → yurdi); fâil gizli «o» — lem cümlesi şartın cevabı, mahallen meczûm.")]
RIDA_MUB = lambda: tok("رِضَا", "rida", "noun", ["mubtada-khabar", "ism-maqsur-manqus", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ، مُضَافٌ.", "The mubtada, in raf' by a damma estimated on the alif — a maqṣūr noun, annexed.", "Mübtedâ, elif üzerindeki takdîrî damme ile merfû — maksûr isim, muzâf.")
LA_TUDRAKU = lambda punct=None: tok("تُدْرَكُ", "adraka", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "form-iv-verbs", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِغَايَةٌ.", "The present verb in the passive, in raf'; the deputy doer is the hidden «it» — the clause qualifies «a goal» in the seat of raf'.", "Meçhul merfû muzâri; nâib-i fâil gizli «o» — cümle «gaye»nin na'tı, mahallen merfû.", punct=punct)

