# -*- coding: utf-8 -*-
"""Author content/samples/nuh-wa-al-safina — «نُوحٌ وَالسَّفِينَةُ», the fifth ORIGINAL Level-1 story (wave 90).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Nūḥ (Hūd 25–48, Sūrat Nūḥ,
al-Qamar 9–15) as it is commonly retold to children. No āya is quoted; no sentence here may be cited as a classical
text. Four chapters, forty-one sentences. Every token carries trilingual iʿrāb. Verb paradigms and glossary entries
are COPIED from the packages that already own the lemma (the lemma-identity rule); only خَشَب and ذَكَر are new.
The house helpers are shared with author_musa4.py verbatim.

    QISSA_PKG_ROOT=<dir> python3 author_nuh.py     # a dry run writes under <dir>/nuh-wa-al-safina
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "nuh-wa-al-safina"
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

# ---- Chapter 1 — نُوحٌ وَقَوْمُهُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Nuh was a righteous man.", "tr": "Nûh sâlih bir adamdı."},
 "tokens": [KANA("كَانَ"), NUH_ISMK(), KHK("رَجُلًا", "rajul"), NAAT("صَالِحًا", "salih", "nasb", ["ism-fail"], punct=".")]})
S1.append({"id": "s2", "translation": {"en": "And his people used to worship idols.", "tr": "Kavmi ise putlara tapıyordu."},
 "tokens": [KANA("وَكَانَ"), ENC_NOUN("قَوْمُهُ", "qawm", "هُ", "ismk"),
  MUDARI5("يَعْبُدُونَ", "abada", ["kana-wa-akhawatuha"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", role_en="; the clause fills the seat of كَانَ's predicate", role_tr="; cümle, kâne'nin haberi olarak mahallen mansûb"),
  MAFUL("الْأَصْنَامَ", "sanam", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِصَنَمٍ", note_en=" — the broken plural of «idol»", note_tr=" — «put»un cem-i mükesseri", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "So Allah sent him to them as a messenger.", "tr": "Allah onu onlara elçi olarak gönderdi."},
 "tokens": [ENC_MADI("فَأَرْسَلَهُ", "arsala", "هُ", ["form-iv-verbs"]), ALLAH_F(), ILAYHIM(),
  HAL("رَسُولًا", "rasul", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "Nuh said to his people: «O my people, worship Allah, and do not worship the idols.»", "tr": "Nûh kavmine dedi ki: «Ey kavmim, Allah'a kulluk edin; putlara tapmayın.»"},
 "tokens": [QALA("فَقَالَ"), NUH_F(),
  tok("لِقَوْمِهِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The lam is a jarr letter; «people» is in jarr, annexed to «his».", "Lâm cer harfi; «kavim» mecrûr, «onun» zamirine muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")]),
  YA(), tok("قَوْمِ", "qawm", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ.", "The vocative annexed to the dropped ya of the speaker («my people»), in nasb by an estimated fatha; the kasra marks where the ya was.", "Hazfedilmiş mütekellim yâ'sına muzâf münâdâ («kavmim»), takdîrî fetha ile mansûb; kesre yâ'nın delilidir.", punct="،"),
  AMR("اعْبُدُوا", "abada", ["thulathi-mujarrad-babs"], waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi", segments=[seg("اعْبُدُو", "abada", "verb"), seg("ا", "pron-3mp", "pron")]),
  ALLAH_MAF(punct="،"),
  tok("وَلَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], WA_AR + "لَا النَّاهِيَةُ حَرْفُ نَهْيٍ وَجَزْمٍ.", "The waw conjoins; the prohibitive لَا «do not» governs jazm.", "«ve» + nehiy lâ'sı: nehiy ve cezm harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nahiya", "part")]),
  tok("تَعْبُدُوا", "abada", "verb", ["nawasib-wa-jawazim-al-mudari", "la-nahiya", "afal-khamsa", "al-bariz-al-muttasil"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ.", "Present verb put in jazm by the prohibitive لَا, its sign the dropped nun (one of the five verbs); the waw is its doer.", "Nehiy lâ'sı ile meczûm muzâri, alâmeti nûnun düşmesi (ef'âl-i hamseden); vâv fâildir.", segments=[seg("تَعْبُدُو", "abada", "verb"), seg("ا", "pron-3mp", "pron")]),
  MAFUL("الْأَصْنَامَ", "sanam", extra=["jam-taksir"], punct=".")]})
S1.append({"id": "s5", "translation": {"en": "But the people laughed at him and mocked his words.", "tr": "Fakat kavmi ona güldü ve sözleriyle alay etti."},
 "tokens": [MADI("فَضَحِكَ", "dahika"), FAIL("الْقَوْمُ", "qawm"), MINHU(),
  VERB_WAW("وَسَخِرُوا", "sakhira", ["thulathi-mujarrad-babs"]), PREP("مِنْ", "min", gloss_tr="«-den»"), ENC_NOUN("كَلَامِهِ", "kalam", "هِ", "majr", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "And they said: «You are only a man like us.»", "tr": "Ve dediler ki: «Sen de bizim gibi bir adamsın.»"},
 "tokens": [VERB_WAW("وَقَالُوا", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=":"),
  tok("أَنْتَ", "anta", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «you», built on fatha, in the seat of raf' as mubtada.", "Munfasıl zamir «sen», fetha üzere mebnî, mübtedâ olarak mahallen merfû."),
  KHABAR("رَجُلٌ", "rajul"),
  tok("مِثْلُنَا", "mithl", "noun", ["naat-sifa", "idafa-definiteness", "al-bariz-al-muttasil"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَمِثْلُ لَا تَتَعَرَّفُ بِالْإِضَافَةِ فَتَنْعَتُ النَّكِرَةَ.", "An adjective «like us», in raf'; annexed to «us» — مِثْل stays indefinite even when annexed, so it may describe an indefinite noun.", "Na't «bizim gibi», merfû; «biz» zamirine muzâf — misl izâfetle ma'rife olmaz, bu yüzden nekreyi niteler.", punct=".", segments=[seg("مِثْلُ", "mithl", "noun"), seg("نَا", "pron-1p", "pron")])]})
S1.append({"id": "s7", "translation": {"en": "And Nuh called his people night and day.", "tr": "Nûh kavmini gece gündüz çağırdı."},
 "tokens": [MADI_ALIF("وَدَعَا", "daa"), NUH_F(), ENC_NOUN("قَوْمَهُ", "qawm", "هُ", "maful"),
  ZARF("لَيْلًا", "layl", "زَمَانٍ", "time", "Zaman", mudaf=False), ATF("وَنَهَارًا", "nahar", case="nasb", extra=["maful-fih"], punct=".")]})
S1.append({"id": "s8", "translation": {"en": "And he kept calling them for long years.", "tr": "Uzun yıllar boyunca onları çağırmaya devam etti."},
 "tokens": [MADI("وَبَقِيَ", "baqiya", ["naqis-verbs"], hidden=True),
  MUDARI("يَدْعُوهُمْ", "daa", ["al-hal-jumla-wa-rabituha"], enc="هُمْ", naqis="و", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", note_en="; the clause fills the seat of nasb as a hal", note_tr="; cümle hâl olarak mahallen mansûb"),
  tok("سِنِينَ", "sana", "noun", ["maful-fih", "jam-mudhakkar-salim"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "An adverb of time «years», in nasb by the ya — a word treated like the sound masculine plural.", "Zaman zarfı «yıllar», cem-i müzekker sâlime mülhak olduğu için yâ ile mansûb."),
  NAAT("طَوِيلَةً", "tawil-long", "nasb", ["sifa-mushabbaha"], punct=".")]})
S1.append({"id": "s9", "translation": {"en": "But only a few of them believed in him.", "tr": "Fakat onlardan ancak pek azı ona inandı."},
 "tokens": [LAM_JAZM("فَلَمْ"),
  tok("يُؤْمِنْ", "amana", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ.", "Present verb put in jazm by لَمْ, its sign the sukun.", "Lem ile meczûm muzâri, alâmeti sükûn."),
  BIHI(), ILLA(),
  FAIL("قَلِيلٌ", "qalil", note_ar=" — بَعْدَ إِلَّا فِي الِاسْتِثْنَاءِ الْمُفَرَّغِ، فَأَخَذَ إِعْرَابَ مَوْقِعِهِ", note_en=" — after إِلَّا in an emptied exception, so it takes the case its position demands", note_tr=" — müferrağ istisnâda illâ'dan sonra; mevkiinin i'râbını almıştır"),
  MINHUM(punct=".")]})
S1.append({"id": "s10", "translation": {"en": "Nuh had a son, and his son was one of the deniers.", "tr": "Nûh'un bir oğlu vardı ve oğlu kâfirlerdendi."},
 "tokens": [KANA("وَكَانَ"),
  tok("لِنُوحٍ", "li", "prep", ["huruf-jarr", "kana-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ، وَنُوحٍ مَجْرُورٌ بِالْكَسْرَةِ" + KH_MUQ[0] + ".", "The lam is a jarr letter; Nuh is in jarr" + KH_MUQ[1] + ".", "Lâm cer harfi; Nûh mecrûr" + KH_MUQ[2] + ".", segments=[seg("لِ", "li", "prep"), seg("نُوحٍ", "nuh", "propn")]),
  ISMK("ابْنٌ", "ibn", muakhkhar=True, punct="،"),
  KANA("وَكَانَ"), ENC_NOUN("ابْنُهُ", "ibn", "هُ", "ismk"), MINA(),
  KAFIRIN_J(punct=".", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ", note_en="; the jarr phrase is the predicate of كَانَ", note_tr="; câr-mecrûr, kâne'nin haberidir")]})

# ---- Chapter 2 — بِنَاءُ السَّفِينَةِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "Then Allah commanded Nuh to make a big ship.", "tr": "Sonra Allah Nûh'a büyük bir gemi yapmasını emretti."},
 "tokens": [MADI("فَأَمَرَ", "amara-command"), ALLAH_F(), MAFUL("نُوحًا", "nuh", "propn"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِحَرْفِ جَرٍّ مَحْذُوفٍ، أَيْ: بِصُنْعِ سَفِينَةٍ", "; the clause it builds fills the seat of jarr after a dropped letter — «(with) the making of a ship»", "; kurduğu müevvel masdar, hazfedilmiş bir cer harfiyle mahallen mecrûr — «gemi yapmakla»"),
  MANSUB_AN("يَصْنَعَ", "sanaa"), MAFUL("سَفِينَةً", "safina"), NAAT("كَبِيرَةً", "kabir", "nasb", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "So Nuh began to make the ship out of wood.", "tr": "Nûh gemiyi tahtadan yapmaya başladı."},
 "tokens": [MADI("فَبَدَأَ", "badaa"), NUH_F(),
  MUDARI("يَصْنَعُ", "sanaa", ["al-hal-jumla-wa-rabituha"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", note_en="; the clause fills the seat of nasb as a hal", note_tr="; cümle hâl olarak mahallen mansûb"),
  SAFINA_MAF(), MINA(), MAJR("الْخَشَبِ", "khashab", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "And he used to work on it every day.", "tr": "Her gün onun üzerinde çalışırdı."},
 "tokens": [KANA("وَكَانَ"), MUDARI_KH("يَعْمَلُ", "amila"), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)"),
  ZARF("كُلَّ", "kull", "زَمَانٍ", "time", "Zaman", note_ar=" — نَابَ عَنِ الظَّرْفِ لِإِضَافَتِهِ إِلَيْهِ", note_en=" — it stands as the adverb because it is annexed to one", note_tr=" — zarfa muzâf olduğu için zarfın yerini tutar"),
  MUDAF_ILAYH("يَوْمٍ", "yawm", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "And the ship was far from the sea.", "tr": "Gemi ise denizden uzaktaydı."},
 "tokens": [KANA("وَكَانَتِ", fem=True), ISMK("السَّفِينَةُ", "safina"), KHK("بَعِيدَةً", "baid", extra=["sifa-mushabbaha"]), AN_KASRA(), MAJR("الْبَحْرِ", "bahr", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "So the deniers used to look at him and laugh at him.", "tr": "Kâfirler ona bakıp gülerlerdi."},
 "tokens": [KANA("فَكَانَ"), ISMK("الْكُفَّارُ", "kafir", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِكَافِرٍ", note_en=" — the broken plural of «denier»", note_tr=" — «kâfir»in cem-i mükesseri"),
  MUDARI5("يَنْظُرُونَ", "nazara", ["kana-wa-akhawatuha"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", role_en="; the clause fills the seat of كَانَ's predicate", role_tr="; cümle, kâne'nin haberi olarak mahallen mansûb"),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)"),
  MUDARI5("وَيَضْحَكُونَ", "dahika", ["atf-nasaq"], role_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ", role_en="; the clause is conjoined to the predicate clause", role_tr="; cümle, haber cümlesine ma'tûftur"),
  MINHU(punct=".")]})
S2.append({"id": "s6", "translation": {"en": "And they said: «O Nuh, why are you making a ship on dry land?»", "tr": "Ve dediler ki: «Ey Nûh, karada neden gemi yapıyorsun?»"},
 "tokens": [VERB_WAW("وَقَالُوا", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=":"),
  YA(), tok("نُوحُ", "nuh", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on damma, in the seat of nasb.", "Münâdâ: müfred alem, damme üzere mebnî, mahallen mansûb.", punct="،"),
  LIMADHA(), MUDARI("تَصْنَعُ", "sanaa", who="أَنْتَ", wujub=True), MAFUL("سَفِينَةً", "safina"),
  PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الْأَرْضِ", "ard", punct="؟")]})
S2.append({"id": "s7", "translation": {"en": "Nuh said: «Allah commanded me to do this, and the water is coming.»", "tr": "Nûh dedi ki: «Bunu bana Allah emretti; su geliyor.»"},
 "tokens": [QALA("فَقَالَ"), NUH_F(punct=":"),
  MUBTADA("اللهُ", "allah", "propn", note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl"),
  tok("أَمَرَنِي", "amara-command", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim", "mubtada-khabar"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "Past verb built on fatha; the doer is a hidden pronoun; the nun guards the verb's ending, and the ya «me» is its object, in the seat of nasb — the clause is the predicate, in the seat of raf'.", "Fetha üzere mebnî mâzî; fâil gizli zamir; nûn vikâye içindir, yâ «beni» mef'ûlün bih — mahallen mansûb; cümle haberdir, mahallen merfû.", segments=[seg("أَمَرَ", "amara-command", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("بِهَذَا", "bi", "prep", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "The ba is a jarr letter; «this» is a demonstrative, built, in the seat of jarr.", "Bâ cer harfi; «bu» işaret ismi, mebnî, mahallen mecrûr.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("هَذَا", "hadha", "pron")]),
  tok("وَالْمَاءُ", "ma-water", "noun", ["mubtada-khabar"], WA_ISTINAF[0] + "الْمَاءُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", WA_ISTINAF[1] + "«the water» is the mubtada, in raf'.", WA_ISTINAF[2] + "«su» mübtedâ, merfû.", segments=[seg("وَ", "wa", "conj"), seg("الْمَاءُ", "ma-water", "noun")]),
  MUDARI("يَأْتِي", "ata", ["mubtada-khabar"], naqis="ي", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en="; the clause is the predicate, in the seat of raf'", note_tr="; cümle haberdir — mahallen merfû", punct=".")]})
S2.append({"id": "s8", "translation": {"en": "Then Nuh took with him two of every animal: a male and a female.", "tr": "Sonra Nûh her hayvandan ikişer aldı: bir erkek ve bir dişi."},
 "tokens": [THUMMA(), MADI("أَخَذَ", "akhadha"), NUH_F(),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb, annexed to «him».", "«İle» — mekân zarfı, mansûb; «onun» zamirine muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  PREP("مِنْ", "min", gloss_tr="«-den»"), MAJR("كُلِّ", "kull", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("حَيَوَانٍ", "hayawan"),
  tok("اثْنَيْنِ", "ithnan", "noun", ["maful-bihi", "al-muthanna", "asma-al-adad-fil-kafiya"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى.", "The direct object «two», in nasb by the ya — a word that declines like the dual.", "Mef'ûlün bih «iki», tesniyeye mülhak olduğu için yâ ile mansûb.", punct=":"),
  tok("ذَكَرًا", "dhakar", "noun", ["badal"], "بَدَلٌ مِنِ اثْنَيْنِ مَنْصُوبٌ بِالْفَتْحَةِ — بَدَلُ تَفْصِيلٍ.", "A substitute (badal) for «two», in nasb — the two spelled out.", "«İki»den bedel, mansûb — tafsîl bedeli."),
  tok("وَأُنْثَى", "untha", "noun", ["atf-nasaq", "ism-maqsur-manqus"], WA_AR + "أُنْثَى مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ.", "The waw conjoins; «a female» is conjoined in nasb by a fatha estimated on the alif — a maqsur noun.", "«ve» + «bir dişi» — ma'tûf, elif üzerindeki takdîrî fetha ile mansûb — maksûr isim.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("أُنْثَى", "untha", "noun")])]})
S2.append({"id": "s9", "translation": {"en": "And the believers entered the ship with Nuh.", "tr": "Mü'minler Nûh ile birlikte gemiye girdiler."},
 "tokens": [MADI("وَدَخَلَ", "dakhala"), MUMINUN_F(), SAFINA_MAF(), MAA(), MUDAF_ILAYH("نُوحٍ", "nuh", "propn", punct=".")]})
S2.append({"id": "s10", "translation": {"en": "And they were few.", "tr": "Ve onlar az kimselerdi."},
 "tokens": [tok("وَكَانُوا", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"], WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "The waw conjoins; كَانَ is the defective past verb, built on damma because the waw of the group is attached — that waw is the noun of كَانَ, in the seat of raf'.", "«ve» + kâne: nâkıs mâzî fiil, cemâat vâvı bitiştiği için damme üzere mebnî; vâv kâne'nin ismidir — mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("كَانُو", "kana", "verb"), seg("ا", "pron-3mp", "pron")]),
  tok("قَلِيلِينَ", "qalil", "noun", ["kana-wa-akhawatuha", "jam-mudhakkar-salim"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "The predicate of كَانَ, in nasb by the ya — a sound masculine plural.", "Kâne'nin haberi, cem-i müzekker sâlim olduğu için yâ ile mansûb.", punct=".")]})

# ---- Chapter 3 — الطُّوفَانُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "And when Nuh entered the ship, the gates of the sky were opened and the rain came down.", "tr": "Nûh gemiye girince göğün kapıları açıldı ve yağmur indi."},
 "tokens": [tok("وَلَمَّا", "lamma", "part", ["maful-fih"], WA_AR + "لَمَّا ظَرْفُ زَمَانٍ بِمَعْنَى حِينَ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "The waw conjoins; لَمَّا «when» is an adverb of time meaning «at the time that», built on sukun in the seat of nasb, carrying the sense of a condition.", "«ve» + lemmâ «-ınca»: «hîne» mânâsında zaman zarfı, sükûn üzere mebnî, mahallen mansûb; şart mânâsı taşır.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
  MADI("دَخَلَ", "dakhala", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا إِلَيْهَا", note_en="; the clause fills the seat of jarr, annexed to لَمَّا", note_tr="; cümle lemmâ'ya muzâfun ileyh olarak mahallen mecrûr"),
  NUH_F(), SAFINA_MAF(punct="،"),
  MAJHUL("فُتِحَتْ", "fataha", fem=True, note_ar=" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا", note_en="; the clause answers لَمَّا and holds no seat", note_tr="; cümle lemmâ'nın cevabıdır, mahalli yoktur"),
  NAIB("أَبْوَابُ", "bab", ["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ تَكْسِيرٍ لِبَابٍ", note_en=", annexed — the broken plural of «gate»", note_tr=", muzâf — «kapı»nın cem-i mükesseri"),
  MUDAF_ILAYH("السَّمَاءِ", "sama", punct="،"),
  MADI("وَنَزَلَ", "nazala"), FAIL("الْمَطَرُ", "matar", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "And water came out from under the earth.", "tr": "Yerin altından da su çıktı."},
 "tokens": [MADI("وَخَرَجَ", "kharaja"), MA_F(), PREP("مِنْ", "min", gloss_tr="«-den»"),
  tok("تَحْتِ", "tahta", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ — ظَرْفٌ خَرَجَ عَنِ الظَّرْفِيَّةِ بِدُخُولِ مِنْ عَلَيْهِ، مُضَافٌ.", "In jarr after the letter — an adverb that has left adverbial use because مِنْ entered on it; annexed.", "Cer harfiyle mecrûr — min başına gelince zarflıktan çıkmış bir zarf; muzâf."),
  MUDAF_ILAYH("الْأَرْضِ", "ard", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "So the water became very abundant.", "tr": "Böylece su pek çoğaldı."},
 "tokens": [SARA("فَصَارَ"), ISMK("الْمَاءُ", "ma-water"), KHK("كَثِيرًا", "kathir"),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ نَائِبٌ عَنْ فِعْلِهِ، لِلتَّوْكِيدِ.", "An absolute object «very», in nasb — a masdar standing for its own verb, for emphasis.", "Mef'ûl-i mutlak «pek», mansûb — fiilinin yerini tutan masdar; te'kîd için.", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "And the water rose above the mountains.", "tr": "Su dağların üstüne yükseldi."},
 "tokens": [MADI_ALIF("وَعَلَا", "ala-rise"), MA_F(), ZARF("فَوْقَ", "fawqa"), MUDAF_ILAYH("الْجِبَالِ", "jabal", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِجَبَلٍ", note_en=" — the broken plural of «mountain»", note_tr=" — «dağ»ın cem-i mükesseri", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "And the ship was running on the water.", "tr": "Gemi suyun üzerinde yüzüp gidiyordu."},
 "tokens": [KANA("وَكَانَتِ", fem=True), ISMK("السَّفِينَةُ", "safina"),
  tok("تَجْرِي", "jara", "verb", ["kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "Present verb in raf' by a damma estimated on the ya; its doer is a hidden pronoun «she», and the clause fills the seat of كَانَ's predicate.", "Yâ üzerindeki takdîrî damme ile merfû muzâri; fâili gizli zamir «o» — cümle, kâne'nin haberi olarak mahallen mansûb."),
  PREP("عَلَى", "ala", gloss_tr="«üzerinde»"), MAJR("الْمَاءِ", "ma-water", punct=".")]})
S3.append({"id": "s6", "translation": {"en": "And Nuh saw his son far from the ship.", "tr": "Nûh oğlunu gemiden uzakta gördü."},
 "tokens": [MADI_ALIF("وَرَأَى", "raa", ["maful-bihi"]), NUH_F(), ENC_NOUN("ابْنَهُ", "ibn", "هُ", "maful"),
  HAL("بَعِيدًا", "baid", ["sifa-mushabbaha"]), AN_KASRA(), SAFINA_J(punct=".")]})
S3.append({"id": "s7", "translation": {"en": "So Nuh called out to him: «O my son, enter the ship with us!»", "tr": "Nûh ona seslendi: «Oğlum, bizimle birlikte gemiye gir!»"},
 "tokens": [ENC_MADI("فَنَادَاهُ", "nada", "هُ", ["form-iii-verbs"], alif=True), NUH_F(punct=":"), YA(),
  tok("ابْنِي", "ibn", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، وَيَاءُ الْمُتَكَلِّمِ مُضَافٌ إِلَيْهِ.", "The annexed vocative «my son», in nasb by a fatha that cannot appear because the ending carries the kasra the ya requires; the ya of the speaker is the second term of the idafa.", "Muzâf münâdâ «oğlum», takdîrî fetha ile mansûb (son harf yâ'nın gerektirdiği kesreyle meşgûldür); mütekellim yâ'sı muzâfun ileyhtir.", punct="،", segments=[seg("ابْنِ", "ibn", "noun"), seg("ي", "pron-1s", "pron")]),
  AMR("ادْخُلْ", "dakhala", ["thulathi-mujarrad-babs"]),
  tok("مَعَنَا", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb, annexed to «us».", "«İle» — mekân zarfı, mansûb; «biz» zamirine muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("نَا", "pron-1p", "pron")]),
  PREP("فِي", "fi", gloss_tr="«-e»"), SAFINA_J(punct="!")]})
S3.append({"id": "s8", "translation": {"en": "The son said: «I will go to the mountain, and the mountain will keep me from the water.»", "tr": "Oğlu dedi ki: «Dağa giderim; dağ beni sudan korur.»"},
 "tokens": [QALA("فَقَالَ"), FAIL("الِابْنُ", "ibn", punct=":"),
  MUDARI("أَذْهَبُ", "dhahaba", who="أَنَا", wujub=True), PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("الْجَبَلِ", "jabal", punct="،"),
  tok("وَالْجَبَلُ", "jabal", "noun", ["mubtada-khabar"], WA_AR + "الْجَبَلُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; «the mountain» is the mubtada, in raf'.", "«ve» + «dağ» mübtedâ, merfû.", segments=[seg("وَ", "wa", "conj"), seg("الْجَبَلُ", "jabal", "noun")]),
  tok("يَحْفَظُنِي", "hafiza", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "Present verb in raf'; the doer is a hidden pronoun; the nun guards the verb's ending and the ya «me» is its object, in the seat of nasb — the clause is the predicate, in the seat of raf'.", "Merfû muzâri; fâil gizli zamir; nûn vikâye içindir, yâ «beni» mef'ûlün bih — mahallen mansûb; cümle haberdir, mahallen merfû.", segments=[seg("يَحْفَظُ", "hafiza", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  MINA(), MAJR("الْمَاءِ", "ma-water", punct=".")]})
S3.append({"id": "s9", "translation": {"en": "Nuh said: «No one is saved today except by the mercy of Allah.»", "tr": "Nûh dedi ki: «Bugün Allah'ın rahmeti olmadan hiç kimse kurtulamaz.»"},
 "tokens": [QALA("فَقَالَ"), NUH_F(punct=":"),
  tok("لَا", "la-nafiya", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ.", "The negating لَا, which governs nothing.", "Nefy harfi lâ; amel etmez."),
  tok("يَنْجُو", "naja-escape", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ بَعْدَهُ.", "Present verb in raf' by a damma estimated on the waw; its doer follows.", "Vâv üzerindeki takdîrî damme ile merfû muzâri; fâili ondan sonra gelir."),
  ZARF("الْيَوْمَ", "yawm", "زَمَانٍ", "time", "Zaman", mudaf=False),
  FAIL("أَحَدٌ", "ahad"), ILLA(),
  tok("بِرَحْمَةِ", "bi", "prep", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَرَحْمَةِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَوْضِعِ الْحَالِ بَعْدَ إِلَّا.", "The ba is a jarr letter; «mercy» is in jarr and annexed — the jarr phrase stands as a hal after إِلَّا.", "Bâ cer harfi; «rahmet» mecrûr, muzâf — câr-mecrûr, illâ'dan sonra hâl mevkiindedir.", segments=[seg("بِ", "bi", "prep"), seg("رَحْمَةِ", "rahma", "noun")]),
  ALLAH_MI(punct=".")]})
S3.append({"id": "s10", "translation": {"en": "And the water came between the two of them, and the son drowned with the deniers.", "tr": "Su ikisinin arasına girdi ve oğul kâfirlerle birlikte boğuldu."},
 "tokens": [MADI("وَجَاءَ", "jaa", ["hollow-verbs"]), MA_F(),
  tok("بَيْنَهُمَا", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "An adverb of place «between», in nasb, annexed to the dual pronoun «the two of them».", "«Arasına» — mekân zarfı, mansûb; tesniye zamirine muzâf.", punct="،", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  MADI("فَغَرِقَ", "ghariqa"), FAIL("الِابْنُ", "ibn"), MAA(), MUDAF_ILAYH("الْكَافِرِينَ", "kafir", extra=["jam-mudhakkar-salim", "ism-fail"], sign="بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the ya, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için yâ ile", punct=".")]})
S3.append({"id": "s11", "translation": {"en": "And Nuh grieved deeply over his son.", "tr": "Nûh oğluna çok üzüldü."},
 "tokens": [MADI("وَحَزِنَ", "hazina"), NUH_F(), PREP("عَلَى", "ala", gloss_tr="«-e»"), ENC_NOUN("ابْنِهِ", "ibn", "هِ", "majr"),
  tok("حُزْنًا", "huzn", "noun", ["maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ حَزِنَ، يُؤَكِّدُ الْفِعْلَ.", "The absolute object (maf'ul mutlaq), in nasb — the masdar of its own verb, strengthening it.", "Mef'ûl-i mutlak, mansûb — kendi fiilinin masdarı; fiili te'kîd eder."),
  NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct=".")]})

# ---- Chapter 4 — النَّجَاةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "And the water stayed on the earth for many days.", "tr": "Su yeryüzünde günlerce kaldı."},
 "tokens": [MADI("وَبَقِيَ", "baqiya", ["naqis-verbs"]), MA_F(), PREP("عَلَى", "ala", gloss_tr="«üzerinde»"), MAJR("الْأَرْضِ", "ard"),
  tok("أَيَّامًا", "yawm", "noun", ["maful-fih", "jam-taksir"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ تَكْسِيرٍ لِيَوْمٍ.", "An adverb of time, in nasb — the broken plural of «day».", "Zaman zarfı, mansûb — «gün»ün cem-i mükesseri."),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "Then the rain stopped, and the water went down little by little.", "tr": "Sonra yağmur kesildi ve su yavaş yavaş çekildi."},
 "tokens": [THUMMA(), MADI("انْقَطَعَ", "inqataa", ["form-vii-verbs"]), FAIL("الْمَطَرُ", "matar", punct="،"),
  MADI("وَنَزَلَ", "nazala"), MA_F(),
  HAL("قَلِيلًا", "qalil"),
  tok("قَلِيلًا", "qalil", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi"], "تَوْكِيدٌ لَفْظِيٌّ مَنْصُوبٌ بِالْفَتْحَةِ — تَكْرَارُ الْحَالِ يُفِيدُ التَّدْرِيجَ.", "A verbal emphasis (tawkid lafzi), in nasb — repeating the hal gives the sense «by degrees».", "Lafzî te'kîd, mansûb — hâlin tekrarı tedrîc mânâsı verir.", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "And the ship came to rest on a high mountain.", "tr": "Gemi yüksek bir dağın üzerine oturdu."},
 "tokens": [tok("وَاسْتَوَتِ", "istawa", "verb", ["form-viii-verbs", "naqis-verbs"], WA_AR + "اسْتَوَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "The waw conjoins; «came to rest» is a past verb built on a fatha estimated on the alif that was dropped where two sukuns met; the ta marks the feminine and takes a kasra before the following ال.", "«ve» + «oturdu»: iki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; tâ te'nîs içindir ve iki sâkin karşılaştığı için kesre ile harekelendi.", segments=[seg("وَ", "wa", "conj"), seg("اسْتَوَتِ", "istawa", "verb")]),
  FAIL("السَّفِينَةُ", "safina"), PREP("عَلَى", "ala", gloss_tr="«üzerine»"), MAJR("جَبَلٍ", "jabal"),
  tok("عَالٍ", "alin-high", "noun", ["naat-sifa", "ism-maqsur-manqus", "ism-fail"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمٌ مَنْقُوصٌ نَكِرَةٌ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْيَاءِ.", "An adjective in jarr by a kasra estimated on the dropped ya — an indefinite manqus noun; the tanwin stands in for the ya.", "Na't, hazfedilen yâ üzerindeki takdîrî kesre ile mecrûr — nekre mankûs isim; tenvîn yâ'dan ivazdır.", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "So Nuh opened the door of the ship and came out of it.", "tr": "Nûh geminin kapısını açtı ve ondan çıktı."},
 "tokens": [MADI("فَفَتَحَ", "fataha"), NUH_F(), MAFUL("بَابَ", "bab", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), SAFINA_MI(),
  MADI("وَخَرَجَ", "kharaja", hidden=True), JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "And the believers and the animals came out with him.", "tr": "Mü'minler ve hayvanlar onunla birlikte çıktılar."},
 "tokens": [MADI("وَخَرَجَ", "kharaja"),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb, annexed to «him».", "«İle» — mekân zarfı, mansûb; «onun» zamirine muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  MUMINUN_F(),
  ATF("وَالْحَيَوَانَاتُ", "hayawan", case="raf", extra=["jam-muannath-salim"], note_ar=" — جَمْعُ مُؤَنَّثٍ سَالِمٌ لِحَيَوَانٍ", note_en=" — the sound feminine plural of «animal»", note_tr=" — «hayvan»ın cem-i müennes sâlimi", punct=".")]})
S4.append({"id": "s6", "translation": {"en": "And the earth was green and beautiful.", "tr": "Yeryüzü yemyeşil ve güzeldi."},
 "tokens": [KANA("وَكَانَتِ", fem=True), ISMK("الْأَرْضُ", "ard"),
  KHK("خَضْرَاءَ", "akhdar", extra=["mamnu-min-sarf", "ism-mamdud"], sign="بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=" — مُؤَنَّثُ أَخْضَرَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", note_en=" — the feminine of «green», barred from tanwin by the lengthened alif of femininity", note_tr=" — «yeşil»in müennesi; memdûd te'nîs elifi yüzünden gayr-i munsarif"),
  NAAT("جَمِيلَةً", "jamil", "nasb", punct=".")]})
S4.append({"id": "s7", "translation": {"en": "So Nuh thanked his Lord for the rescue.", "tr": "Nûh kurtuluş için Rabbine şükretti."},
 "tokens": [MADI("فَشَكَرَ", "shakara"), NUH_F(), ENC_NOUN("رَبَّهُ", "rabb", "هُ", "maful"), PREP("عَلَى", "ala", gloss_tr="«için»"), MAJR("النَّجَاةِ", "najat", punct=".")]})
S4.append({"id": "s8", "translation": {"en": "And Nuh lived many years after the flood.", "tr": "Nûh tûfandan sonra uzun yıllar yaşadı."},
 "tokens": [MADI("وَعَاشَ", "asha-live", ["hollow-verbs"]), NUH_F(), ZARF("بَعْدَ", "bada", "زَمَانٍ", "time", "Zaman"), MUDAF_ILAYH("الطُّوفَانِ", "tufan"),
  tok("سِنِينَ", "sana", "noun", ["maful-fih", "jam-mudhakkar-salim"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "An adverb of time «years», in nasb by the ya — a word treated like the sound masculine plural.", "Zaman zarfı «yıllar», cem-i müzekker sâlime mülhak olduğu için yâ ile mansûb."),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct=".")]})
S4.append({"id": "s9", "translation": {"en": "And he used to call people to the worship of Allah.", "tr": "İnsanları Allah'a kulluğa çağırırdı."},
 "tokens": [KANA("وَكَانَ"),
  tok("يَدْعُو", "daa", "verb", ["kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "Present verb in raf' by a damma estimated on the waw; its doer is a hidden pronoun, and the clause fills the seat of كَانَ's predicate.", "Vâv üzerindeki takdîrî damme ile merfû muzâri; fâili gizli zamir — cümle, kâne'nin haberi olarak mahallen mansûb."),
  MAFUL("النَّاسَ", "nas"), PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("عِبَادَةِ", "ibada", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), ALLAH_MI(punct=".")]})
S4.append({"id": "s10", "translation": {"en": "Nuh was a patient prophet — so be patient, you too, like Nuh.", "tr": "Nûh sabırlı bir peygamberdi — sen de Nûh gibi sabret."},
 "tokens": [KANA("وَكَانَ"), NUH_ISMK(), KHK("نَبِيًّا", "nabi"), NAAT("صَابِرًا", "sabir", "nasb", ["ism-fail"], punct="،"),
  AMR("فَاصْبِرْ", "sabara", ["thulathi-mujarrad-babs"]),
  tok("أَنْتَ", "anta", "pron", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ فِي اصْبِرْ.", "A detached pronoun «you», built on fatha, in the seat of raf' — it emphasises the pronoun hidden in «be patient».", "Munfasıl zamir «sen», fetha üzere mebnî, mahallen merfû — «sabret»teki gizli zamiri te'kîd eder."),
  tok("مِثْلَ", "mithl", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — أَيْ: مُمَاثِلًا لِنُوحٍ.", "A hal «like», in nasb and annexed — «being like Nuh».", "Hâl «gibi», mansûb, muzâf — «Nûh'a benzer olarak»."),
  MUDAF_ILAYH("نُوحٍ", "nuh", "propn", punct=".")]})

TITLES = [
 {"ar": "نُوحٌ وَقَوْمُهُ", "en": "Nuh and His People", "tr": "Nûh ve Kavmi"},
 {"ar": "بِنَاءُ السَّفِينَةِ", "en": "Building the Ship", "tr": "Geminin Yapılışı"},
 {"ar": "الطُّوفَانُ", "en": "The Flood", "tr": "Tûfan"},
 {"ar": "النَّجَاةُ", "en": "The Rescue", "tr": "Kurtuluş"},
]
CHAPS = [S1, S2, S3, S4]


# ---- the glossary: copied from the packages that own each key (the lemma-identity rule), plus the two new words
PREF = ["musa-fi-madyan", "musa-wal-khadir", "musa-wa-bani-israil", "musa-wa-firawn", "bad-al-amali", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
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
 "khashab": {"lemma": "خَشَب", "root": "خ ش ب", "pos": "noun", "plural": "أَخْشَاب", "gloss": {"en": "wood, timber", "tr": "tahta, kereste"}, "level": 1},
 "dhakar": {"lemma": "ذَكَر", "root": "ذ ك ر", "pos": "noun", "plural": "ذُكُور", "gloss": {"en": "a male (the pair of أُنْثَى)", "tr": "erkek (أُنْثَى «dişi»nin eşi)"}, "level": 1},
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
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": "nuh-wa-al-safina",
 "storyGroup": "nuh-wa-al-safina",
 "title": {"ar": "نُوحٌ وَالسَّفِينَةُ", "en": "Nuh and the Ship", "tr": "Nûh ve Gemi"},
 "subtitle": {"ar": "قِصَّةُ نُوحٍ وَالطُّوفَانِ لِلْمُبْتَدِئِينَ — الدَّعْوَةُ الطَّوِيلَةُ، وَالسَّفِينَةُ، وَالنَّجَاةُ",
              "en": "The story of Nuh and the flood, for beginners — the long call, the ship, the rescue",
              "tr": "Yeni başlayanlar için Nûh ve tûfan kıssası — uzun davet, gemi, kurtuluş"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-07",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِقِصَّةِ نُوحٍ عَلَيْهِ السَّلَامُ كَمَا تُرْوَى لِلْأَطْفَالِ (عَلَى ضَوْءِ سُورَةِ هُودٍ، الْآيَاتِ ٢٥–٤٨، وَسُورَةِ نُوحٍ، وَسُورَةِ الْقَمَرِ ٩–١٥)، عَلَى طَرِيقَةِ الْقِرَاءَةِ الْمُتَدَرِّجَةِ لِلنَّدْوِيِّ. لَمْ تُنْقَلْ آيَةٌ بِنَصِّهَا، وَلَا يُسْتَشْهَدُ بِجُمْلَةٍ هُنَا عَلَى أَنَّهَا نَصٌّ تُرَاثِيٌّ. كُتِبَتْ لِنَائِبِ الْفَاعِلِ، وَلَمْ الْجَازِمَةِ، وَالِاسْتِثْنَاءِ الْمُفَرَّغِ، وَجَمْعِ الْمُذَكَّرِ السَّالِمِ فِي أَحْوَالِهِ، وَالْمُثَنَّى، وَلَمَّا الْحِينِيَّةِ، وَالْبَدَلِ، وَالتَّوْكِيدِ اللَّفْظِيِّ.",
  "en": "ORIGINAL Level-1 graded Arabic: the story of Nuh (peace be upon him) as it is told to children (after the Qurʾānic narrative in Hūd 25–48, Sūrat Nūḥ and al-Qamar 9–15), composed editorially in the manner of Nadwī's graded readers — short كَانَ-framed sentences, one event per line, the vocabulary repeated. No āya is quoted verbatim; no sentence here may be cited as a classical text. Written to meet the deputy doer, the jussive لَمْ, the emptied exception, the sound masculine plural in its cases, the dual, لَمَّا of time, the badal and the verbal tawkid.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Nûh aleyhisselâmın kıssasının çocuklara anlatıldığı şekli (Hûd sûresi 25–48, Nûh sûresi ve Kamer sûresi 9–15'teki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde telif edilmiştir — kısa, kâne ile kurulu cümleler, her satırda bir olay, tekrar eden kelime hazinesi. Hiçbir âyet aynen aktarılmamıştır; buradaki hiçbir cümle klasik bir metin olarak kaynak gösterilemez. Nâib-i fâil, cezmeden lem, müferrağ istisnâ, hâlleriyle cem-i müzekker sâlim, tesniye, zaman lemmâ'sı, bedel ve lafzî te'kîd için yazıldı.",
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
