"""Author content/samples/sulayman-wa-al-hudhud — «سُلَيْمَانُ وَالْهُدْهُدُ», the seventh ORIGINAL Level-1 story (wave 94).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Sulaymān, the ant and the
hoopoe (al-Naml 15–44) as it is commonly retold to children. No āya is quoted; no sentence here may be cited as a
classical text. Four chapters, forty-four sentences. Every token carries trilingual iʿrāb. Verb paradigms and
glossary entries are COPIED from the packages that already own the lemma (the lemma-identity rule); no word is new.
The house helpers are shared with author_salih.py / author_nuh.py / author_musa4.py verbatim.

    QISSA_PKG_ROOT=<dir> python3 author_sulayman.py     # a dry run writes under <dir>/sulayman-wa-al-hudhud
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "sulayman-wa-al-hudhud"
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

# ---- the pronoun tables need the plural «you», the kasra-/damma-voweled «them» and the feminine «you»
PRON.update({"كُمْ": "pron-2mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp", "ي": "pron-1s"})
PRON_AR.update({"كُمْ": "كُمْ", "هِمْ": "هِمْ", "هُمُ": "هُمْ"})

# ============ «سُلَيْمَانُ وَالْهُدْهُدُ» — the seventh story: four chapters ============
DIPT_SUL = (" — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", " — a foreign proper name, barred from tanwin (diptote)", " — yabancı özel isim, gayr-i munsarıf")
SUL_F = lambda punct=None: FAIL("سُلَيْمَانُ", "sulayman", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
SUL_ISMK = lambda punct=None: ISMK("سُلَيْمَانُ", "sulayman", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
SUL_KH = lambda punct=None: KHABAR("سُلَيْمَانُ", "sulayman", ["mamnu-min-sarf"], punct=punct, note_ar=DIPT_SUL[0], note_en=DIPT_SUL[1], note_tr=DIPT_SUL[2])
SUL_J = lambda punct=None: MAJR("سُلَيْمَانَ", "sulayman", "propn", ["mamnu-min-sarf"], DIPT_SUL[0], DIPT_SUL[1] + ", so the fatha stands in for the kasra", DIPT_SUL[2] + "; kesre yerine fetha", punct=punct, sign=FATHA_JARR)
SUL_MI = lambda punct=None: MUDAF_ILAYH("سُلَيْمَانَ", "sulayman", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR + " لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=DIPT_SUL[1] + ", so the fatha stands in for the kasra", note_tr=DIPT_SUL[2] + "; kesre yerine fetha", punct=punct)
SUL_MUNADA = lambda punct=None: tok("سُلَيْمَانُ", "sulayman", "propn", ["vocative-munada", "mamnu-min-sarf"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on damma, in the seat of nasb.", "Münâdâ: müfred alem, damme üzere mebnî, mahallen mansûb.", punct=punct)
DAWUD_F = lambda punct=None: FAIL("دَاوُدُ", "dawud", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
DAWUD_ISMK = lambda punct=None: ISMK("دَاوُدُ", "dawud", "propn", ["mamnu-min-sarf"], *DIPT_SUL, punct=punct)
HUDHUD_F = lambda punct=None: FAIL("الْهُدْهُدُ", "hudhud", punct=punct)
HUDHUD_MAF = lambda punct=None: MAFUL("الْهُدْهُدَ", "hudhud", punct=punct)
MALIKA_F = lambda punct=None: FAIL("الْمَلِكَةُ", "malika", punct=punct)
MALIKA_J = lambda punct=None: MAJR("الْمَلِكَةِ", "malika", punct=punct)
JUNUD = (" — جَمْعُ تَكْسِيرٍ لِجُنْدٍ", " — the broken plural of «troop»", " — «asker»in cem-i mükesseri")
FI = lambda: PREP("فِي", "fi", gloss_tr="«-de»")
MIN = lambda: PREP("مِنْ", "min", gloss_tr="«-den»")
ILA = lambda: PREP("إِلَى", "ila", gloss_tr="«-e»")
ALA = lambda: PREP("عَلَى", "ala", gloss_tr="«üzerine»")
def KANU(full):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
        ar0 + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.",
        en0 + "كَانُوا is the defective past verb built on damma before the waw of the group; that waw is the noun of كَانَ, in the seat of raf'.",
        tr0 + "kânû: cemâat vâvı bitiştiği için damme üzere mebnî nâkıs mâzî; vâv, kâne'nin ismi olarak mahallen merfû.",
        segments=[s for s in [sg, seg(stem[:-1], "kana", "verb"), seg("ا", "pron-3mp", "pron")] if s])
def SARU(full):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
        ar0 + "صَارُوا فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ صَارَ.",
        en0 + "صَارُوا «they became» is a sister of كَانَ, built on damma before the waw of the group; that waw is its noun, in the seat of raf'.",
        tr0 + "sârû «oldular»: kâne'nin kardeşlerinden, cemâat vâvı bitiştiği için damme üzere mebnî; vâv, sâra'nın ismi olarak mahallen merfû.",
        segments=[s for s in [sg, seg(stem[:-1], "sara", "verb"), seg("ا", "pron-3mp", "pron")] if s])
KANAT_K = lambda full="وَكَانَتِ": tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    (WA_AR if full.startswith("وَ") else FA_AR if full.startswith("فَ") else "") + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    ("The waw conjoins; " if full.startswith("وَ") else "The fa conjoins; " if full.startswith("فَ") else "") + "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb; the ta marks the feminine and is voweled with kasra before the following ال.",
    ("«ve» + " if full.startswith("وَ") else "«bunun üzerine» + " if full.startswith("فَ") else "") + "«idi» — nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.",
    segments=[seg(full[:2], "wa" if full.startswith("وَ") else "fa", "conj"), seg(full[2:], "kana", "verb")])
WA_LA_NAFIYA = lambda: tok("وَلَا", "la-nafiya", "part", ["la-nafiya"], WA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The waw conjoins; لَا negates and governs nothing.", "«ve» + nefiy lâ'sı; amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
LA_NAFIYA = lambda: tok("لَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The negating لَا, which governs nothing.", "Nefiy lâ'sı; amel etmez.")
LA_NAHIYA = lambda: tok("لَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "لَا النَّاهِيَةُ حَرْفُ نَهْيٍ وَجَزْمٍ.", "The prohibitive لَا «do not», which governs jazm.", "Nehiy lâ'sı: nehiy ve cezm harfi.")
LAMMA = lambda full="وَلَمَّا": tok(full, "lamma", "part", ["maful-fih", "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"], WA_AR + "لَمَّا ظَرْفُ زَمَانٍ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "The waw conjoins; لَمَّا «when» is an adverb of time meaning «at the time that», built on sukun in the seat of nasb, annexed to the clause after it.", "«ve» + lemmâ: «…-diği zaman» anlamında zaman zarfı, sükûn üzere mebnî, mahallen mansûb; kendisinden sonraki cümleye muzâf.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")])
LAMMA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause fills the seat of jarr, annexed to لَمَّا", "; cümle lemmâ'ya muzâfun ileyh olarak mahallen mecrûr")
def ISHARA(full, lex, seat_ar, seat_en, seat_tr, built_ar="السُّكُونِ", built_en="sukun", built_tr="sükûn", extra=None, punct=None):
    return tok(full, lex, "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى " + built_ar + " فِي مَحَلِّ " + seat_ar + ".", "A demonstrative, built on " + built_en + ", in the seat of " + seat_en + ".", "İşaret ismi, " + built_tr + " üzere mebnî, " + seat_tr + " olarak mahallen.", punct=punct)
HADHIHI_J = lambda: ISHARA("هَذِهِ", "hadhihi", "جَرٍّ", "jarr", "mecrûr", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre")
def BADAL(full, lex, case, extra=None, punct=None):
    sign = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, lex, "noun", ["badal", "asma-al-ishara"] + (extra or []), "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ " + sign + ".", "A badal of the demonstrative, in the same case.", "İşaret isminden bedel; onun i'râbını alır.", punct=punct)
def LI_AL(full, lex, stem, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """لِلنَّمْلِ، لِلشَّمْسِ، لِلْهُدْهُدِ: the lam fused to a defined noun"""
    return tok(full, "li", "prep", ["huruf-jarr"] + (extra or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَ" + stem + " مَجْرُورٌ بِالْكَسْرَةِ" + note_ar + ".", "The lam is a jarr letter; the noun after it is in jarr" + note_en + ".", "Lâm cer harfi; sonraki isim mecrûr" + note_tr + ".",
        punct=punct, segments=[seg("لِ", "li", "prep"), seg(stem, lex, "noun")])
def BI_NOUN(full, lex, stem, extra=None, punct=None, note_ar="", note_en="", note_tr="", pos="noun", stem_ar=None, sign="بِالْكَسْرَةِ"):
    return tok(full, "bi", "prep", ["huruf-jarr"] + (extra or []),
        "الْبَاءُ حَرْفُ جَرٍّ، وَ" + (stem_ar or stem) + " مَجْرُورٌ " + sign + note_ar + ".", "The ba is a jarr letter; the noun after it is in jarr" + note_en + ".", "Bâ cer harfi; sonraki isim mecrûr" + note_tr + ".",
        punct=punct, segments=[seg("بِ", "bi", "prep"), seg(stem, lex, pos)])
MUTLAQ = lambda full, lex, punct=None: tok(full, lex, "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ الْفِعْلِ قَبْلَهُ، يُؤَكِّدُهُ.", "The absolute object (maf'ul mutlaq), in nasb — the verb's own masdar, strengthening it.", "Mef'ûlün mutlak, mansûb — fiilin kendi masdarı; onu pekiştirir.", punct=punct)
def FIVE_NASB(full, lex, extra=None, punct=None, by="أَنْ", by_en="أَنْ", by_tr="en"):
    """يَنْتَظِرُوا: one of the five verbs in nasb by the dropped nun"""
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil"] + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ" + by + " وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
        "Present verb put in nasb by " + by_en + ", its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf'.",
        by_tr + " ile mansûb muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû.", punct=punct, segments=[seg(full[:-1], lex, "verb"), seg("ا", "pron-3mp", "pron")])
def FEM2(full, lex, mode, extra=None, punct=None):
    """تَعْبُدِي (jazm after the prohibitive لَا) / اعْبُدِي (the imperative): the ya of the addressed woman"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    if mode == "jazm":
        ar = "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ."
        en = "present verb in jazm after the prohibitive لَا, its sign the dropped nun (one of the five verbs); the ya of the addressed woman is its doer, in the seat of raf'."
        tr = "nehiy lâ'sı ile meczûm muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; muhâtaba yâ'sı fâil, mahallen merfû."
        g = ["nawasib-wa-jawazim-al-mudari", "la-nahiya", "afal-khamsa", "al-bariz-al-muttasil"]
    else:
        ar = "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ."
        en = "imperative built on the dropped nun (its present is one of the five verbs); the ya of the addressed woman is its doer, in the seat of raf'."
        tr = "nûnun hazfi üzere mebnî emir (muzârii ef'âl-i hamsedendir); muhâtaba yâ'sı fâil, mahallen merfû."
        g = ["imperative-amr", "afal-khamsa", "al-bariz-al-muttasil"]
    return tok(full, lex, "verb", g + (extra or []), ar0 + ar, en0 + en, tr0 + tr, punct=punct, segments=[s for s in [sg, seg(stem[:-1], lex, "verb"), seg("ي", "pron-2fs", "pron")] if s])
RAAT = lambda full, punct=None: tok(full, "raa", "verb", ["thulathi-mujarrad-babs", "naqis-verbs"],
    (FA_AR if full.startswith("فَ") else WA_AR if full.startswith("وَ") else "") + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.",
    ("The fa conjoins; " if full.startswith("فَ") else "The waw conjoins; " if full.startswith("وَ") else "") + "past verb built on a fatha estimated on the alif, which drops before the feminine ta (two quiescents meeting); the doer «she» is hidden.",
    ("«bunun üzerine» + " if full.startswith("فَ") else "«ve» + " if full.startswith("وَ") else "") + "iki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; tâ te'nîs içindir, fâil gizli zamir «o».",
    punct=punct, segments=[seg(full[:2], "fa" if full.startswith("فَ") else "wa", "conj"), seg(full[2:], "raa", "verb")])
def RAAT_F(full, punct=None):
    """فَرَأَتْ نَمْلَةٌ: the same verb with its doer following"""
    t = RAAT(full, punct); t["irab"] = {"ar": FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "en": "The fa conjoins; past verb built on a fatha estimated on the alif, which drops before the feminine ta (two quiescents meeting).", "tr": "«bunun üzerine» + iki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; tâ te'nîs içindir."}; return t
HATTA = lambda: tok("حَتَّى", "hatta", "part", ["huruf-jarr", "an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهَا مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "حَتَّى «until»: a particle of end-point and jarr; the present verb after it is put in nasb by a hidden أَنْ.", "Hattâ «-inceye kadar»: gâye ve cer harfi; ondan sonraki muzâri gizli bir en ile mansûbdur.")
AYNA = lambda: tok("أَيْنَ", "ayna", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "An interrogative «where», built on fatha, in the seat of raf' as the fronted khabar.", "İstifhâm ismi «nerede», fetha üzere mebnî, öne alınmış haber olarak mahallen merfû.")
WA_HIYA = lambda: tok("وَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], WA_AR + "هِيَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; «she» is a detached pronoun built on fatha, in the seat of raf' as mubtada.", "«ve» + munfasıl zamir «o», fetha üzere mebnî, mübtedâ olarak mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")])
RABBI = lambda punct=None: tok("رَبِّ", "rabb", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ الْمَحْذُوفَةِ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ.", "The vocative «my Lord», annexed to a dropped ya of the speaker: in nasb by an estimated fatha, the kasra pointing to the dropped ya; the vocative particle is omitted.", "Münâdâ «Rabbim»: hazfedilmiş mütekellim yâ'sına muzâf; takdîrî fetha ile mansûb, kesre hazfedilen yâ'ya delâlet eder; nidâ harfi hazfedilmiştir.", punct=punct)
ANNA = lambda: tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "an-masdariyya"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَأَنَّ وَمَعْمُولَاهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ عَلِمَ.", "The heavy أَنَّ «that», a sister of إِنَّ: it puts its noun in nasb and raises its predicate; with its two terms it stands as a masdar in the place of the two objects of «knew».", "Ağır enne «ki»: inne'nin kardeşlerinden, ismini nasb, haberini ref eder; iki ma'mûlüyle birlikte masdar te'vîlinde «bildi»nin iki mef'ûlünün yerini tutar.")
KH_ANNA = (" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ", "; the jarr phrase is the predicate of أَنَّ", "; câr-mecrûr, enne'nin haberidir")
KULLUHUM = lambda punct=None: tok("كُلُّهُمْ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يُؤَكِّدُ الْفَاعِلَ قَبْلَهُ.", "A tawkid of meaning «all of them», in raf' like the doer it strengthens; annexed to the pronoun «them», which fills the seat of jarr.", "Ma'nevî te'kîd «hepsi», pekiştirdiği fâil gibi merfû; «onlar» zamirine muzâf, zamir mahallen mecrûr.", punct=punct, segments=[seg("كُلُّ", "kull", "noun"), seg("هُمْ", "pron-3mp", "pron")])
WAHDAHU = lambda punct=None: tok("وَحْدَهُ", "wahda", "noun", ["hal", "idafa-definiteness", "al-bariz-al-muttasil"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَوَحْدَهُ لَا يَقَعُ إِلَّا حَالًا.", "The hal «alone», in nasb and annexed to the pronoun «him»; وَحْدَهُ is only ever a hal.", "Hâl «yalnız, tek başına», mansûb; «o» zamirine muzâf — vahdehû yalnız hâl olarak gelir.", punct=punct, segments=[seg("وَحْدَ", "wahda", "noun"), seg("هُ", "pron-3ms", "pron")])
SA_MUDARI = lambda full, lex, stem, extra=None, punct=None: tok(full, lex, "verb", ["mudari-marfu", "al-fail-al-mudmar-al-mustatir-wujuban"] + (extra or []),
    "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَ" + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.",
    "The sin marks the near future; the present verb after it is in raf' by the damma, its doer «I» hidden of necessity.",
    "Sîn istikbâl harfi; muzâri damme ile merfû, fâil «ben» vücûben müstetir.", punct=punct, segments=[seg("سَ", "sawfa", "part"), seg(stem, lex, "verb")])
NAAT_WAW = lambda full, lex, punct=None: tok(full, lex, "noun", ["naat-sifa", "jam-mudhakkar-salim"], "نَعْتٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "An adjective agreeing with its noun, in raf' by the waw — a sound masculine plural.", "Na't, mevsûfuna uyar; cem-i müzekker sâlim olduğu için vâv ile merfû.", punct=punct)
QALA_H = lambda full="وَقَالَ", punct=":": QALA(full, hidden=True, punct=punct)
MUDARI_KH_F = lambda full, lex, extra=None, punct=None: tok(full, lex, "verb", ["kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs"] + (extra or []),
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
    "Present verb in raf' by a damma estimated on the ya; its doer «she» is hidden, and the clause fills the seat of كَانَ's predicate.",
    "Yâ üzerindeki takdîrî damme ile merfû muzâri; fâili gizli zamir «o» — cümle, kâne'nin haberi olarak mahallen mansûb.", punct=punct)
KH_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", "; the clause fills the seat of raf' as the khabar", "; cümle haber olarak mahallen merfû")
NAAT_CL_ISMK = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِابْنٍ", "; the clause qualifies «a son» — in the seat of raf' as its na't", "; cümle «oğul»un na'tı olarak mahallen merfû")
OBJ1 = ("، وَهُوَ الْمَفْعُولُ الْأَوَّلُ", "; it is the first of two objects", "; iki mef'ûlün ilki")
OBJ2 = (" — وَهُوَ الْمَفْعُولُ الثَّانِي", " — the second object", " — ikinci mef'ûl")

# ---- Chapter 1 — مُلْكُ سُلَيْمَانَ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Dawud was a prophet and a king.", "tr": "Dâvûd bir peygamber ve bir kraldı."},
 "tokens": [KANA("كَانَ"), DAWUD_ISMK(), KHK("نَبِيًّا", "nabi"), ATF("وَمَلِكًا", "malik-king", case="nasb", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "He had a son whose name was Sulayman.", "tr": "Onun adı Süleyman olan bir oğlu vardı."},
 "tokens": [KANA("وَكَانَ"), LAHU("لَهُ", "pron-3ms", " («ona»)", grammar=["kana-wa-akhawatuha"]),
  ISMK("ابْنٌ", "ibn", muakhkhar=True, note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ قَبْلَهُ خَبَرُ كَانَ مُقَدَّمٌ", note_en="; the jarr phrase before it is the fronted predicate of كَانَ", note_tr="; önündeki câr-mecrûr kâne'nin öne alınmış haberidir"),
  ENC_NOUN("اسْمُهُ", "ism", "هُ", "mubtada", note_ar=NAAT_CL_ISMK[0], note_en=NAAT_CL_ISMK[1], note_tr=NAAT_CL_ISMK[2]), SUL_KH(punct=".")]})
S1.append({"id": "s3", "translation": {"en": "When Dawud died, Sulayman became king.", "tr": "Dâvûd ölünce Süleyman kral oldu."},
 "tokens": [LAMMA(), MADI("مَاتَ", "mata-die", ["hollow-verbs"], note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), DAWUD_F(), SARA("صَارَ"), SUL_ISMK(), KHK("مَلِكًا", "malik-king", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "And Allah gave him a mighty kingdom.", "tr": "Allah ona büyük bir mülk verdi."},
 "tokens": [ENC_MADI("وَأَعْطَاهُ", "aata", "هُ", ["form-iv-verbs"], alif=True, note_ar=OBJ1[0], note_en=OBJ1[1], note_tr=OBJ1[2]), ALLAH_F(), MAFUL("مُلْكًا", "mulk", note_ar=OBJ2[0], note_en=OBJ2[1], note_tr=OBJ2[2]), NAAT("عَظِيمًا", "azim", "nasb", ["sifa-mushabbaha"], punct=".")]})
S1.append({"id": "s5", "translation": {"en": "And Allah taught him the speech of the birds.", "tr": "Allah ona kuşların dilini öğretti."},
 "tokens": [ENC_MADI("وَعَلَّمَهُ", "allama", "هُ", ["form-ii-verbs"], note_ar=OBJ1[0], note_en=OBJ1[1], note_tr=OBJ1[2]), ALLAH_F(), MAFUL("كَلَامَ", "kalam", note_ar="، مُضَافٌ" + OBJ2[0], note_en=", annexed" + OBJ2[1], note_tr=", muzâf" + OBJ2[2]), MUDAF_ILAYH("الطَّيْرِ", "tayr", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "So Sulayman used to understand the speech of the birds and the ants.", "tr": "Böylece Süleyman kuşların ve karıncaların dilini anlardı."},
 "tokens": [KANA("فَكَانَ"), SUL_ISMK(), MUDARI_KH("يَفْهَمُ", "fahima", ["thulathi-mujarrad-babs"]), MAFUL("كَلَامَ", "kalam", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الطَّيْرِ", "tayr"), ATF("وَالنَّمْلِ", "naml", case="jarr", punct=".")]})
S1.append({"id": "s7", "translation": {"en": "And the wind used to run at his command.", "tr": "Rüzgâr onun emriyle eserdi."},
 "tokens": [KANAT_K("وَكَانَتِ"), ISMK("الرِّيحُ", "rih"), MUDARI_KH_F("تَجْرِي", "jara"),
  tok("بِأَمْرِهِ", "bi", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَمْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The ba is a jarr letter; «command» is in jarr, annexed to «his».", "Bâ cer harfi; «emir» mecrûr, «onun» zamirine muzâf.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("أَمْرِ", "amr", "noun"), seg("هِ", "pron-3ms", "pron")])]})
S1.append({"id": "s8", "translation": {"en": "He had troops from among men, jinn and birds.", "tr": "İnsanlardan, cinlerden ve kuşlardan askerleri vardı."},
 "tokens": [KANA("وَكَانَ"), LAHU("لَهُ", "pron-3ms", " («ona»)", grammar=["kana-wa-akhawatuha"]),
  ISMK("جُنُودٌ", "jund", extra=["jam-taksir"], muakhkhar=True, note_ar=JUNUD[0] + "، وَالْجَارُّ وَالْمَجْرُورُ قَبْلَهُ خَبَرُ كَانَ مُقَدَّمٌ", note_en=JUNUD[1] + "; the jarr phrase before it is the fronted predicate of كَانَ", note_tr=JUNUD[2] + "; önündeki câr-mecrûr kâne'nin öne alınmış haberidir"),
  MINA(), MAJR("الْإِنْسِ", "ins"), ATF("وَالْجِنِّ", "jinn", case="jarr"), ATF("وَالطَّيْرِ", "tayr", case="jarr", punct=".")]})
S1.append({"id": "s9", "translation": {"en": "And Sulayman used to thank Allah for His favour.", "tr": "Süleyman nimeti için Allah'a şükrederdi."},
 "tokens": [KANA("وَكَانَ"), SUL_ISMK(), MUDARI_KH("يَشْكُرُ", "shakara", ["thulathi-mujarrad-babs"]), ALLAH_MAF(), ALA(), ENC_NOUN("نِعْمَتِهِ", "nima", "هِ", "majr", punct=".")]})
S1.append({"id": "s10", "translation": {"en": "And he used to say: «Praise be to Allah for this favour.»", "tr": "Ve şöyle derdi: «Bu nimet için hamd Allah'adır.»"},
 "tokens": [KANA("وَكَانَ"), SUL_ISMK(), MUDARI_KH("يَقُولُ", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=":"),
  MUBTADA("الْحَمْدُ", "hamd"),
  tok("لِلّٰهِ", "li", "prep", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "The lam is a jarr letter; the Name of Majesty is in jarr — the jarr phrase is the khabar.", "Lâm cer harfi; lafza-i celâl mecrûr — câr-mecrûr haberdir.", segments=[seg("لِ", "li", "prep"), seg("اللهِ", "allah", "propn")]),
  ALA(), HADHIHI_J(), BADAL("النِّعْمَةِ", "nima", "jarr", punct=".")]})

# ---- Chapter 2 — وَادِي النَّمْلِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "One day Sulayman went out with his troops.", "tr": "Bir gün Süleyman askerleriyle çıktı."},
 "tokens": [MADI("خَرَجَ", "kharaja"), SUL_F(), ZARF("يَوْمًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False), MAA(), ENC_NOUN("جُنُودِهِ", "jund", "هِ", "mudaf", extra=["jam-taksir"], punct=".")]})
S2.append({"id": "s2", "translation": {"en": "They passed by a valley in which there were many ants.", "tr": "İçinde çok karınca bulunan bir vadiden geçtiler."},
 "tokens": [VERB_WAW("فَمَرُّوا", "marra", ["thulathi-mujarrad-babs"]),
  tok("بِوَادٍ", "bi", "prep", ["huruf-jarr", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَوَادٍ اسْمٌ مَنْقُوصٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ، وَالتَّنْوِينُ عِوَضٌ عَنْهَا.", "The ba is a jarr letter; «a valley» is a manqus noun in jarr by a kasra estimated on the dropped ya, the tanwin standing in for it.", "Bâ cer harfi; «vâdi» mankûs isim, düşen yâ üzerindeki takdîrî kesre ile mecrûr; tenvîn yâ'dan ivazdır.", segments=[seg("بِ", "bi", "prep"), seg("وَادٍ", "wadi-valley", "noun")]),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («içinde»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِوَادٍ", note_en="; the jarr phrase is the fronted khabar, and the clause qualifies «a valley», in the seat of jarr", note_tr="; câr-mecrûr öne alınmış haber; cümle «vâdi»nin na'tı olarak mahallen mecrûr"),
  MUBTADA("نَمْلٌ", "naml", note_ar=" مُؤَخَّرٌ", note_en=" (placed after its predicate)", note_tr=" (haberinden sonraya bırakılmış)"), NAAT("كَثِيرٌ", "kathir", "raf", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "An ant saw the troops.", "tr": "Bir karınca askerleri gördü."},
 "tokens": [RAAT_F("فَرَأَتْ"), FAIL("نَمْلَةٌ", "namla"), MAFUL("الْجُنُودَ", "jund", extra=["jam-taksir"], note_ar=JUNUD[0], note_en=JUNUD[1], note_tr=JUNUD[2], punct=".")]})
S2.append({"id": "s4", "translation": {"en": "She feared for the ants.", "tr": "Karıncalar için korktu."},
 "tokens": [MADI("فَخَافَتْ", "khafa", ["hollow-verbs"], fem=True, hidden=True), ALA(), MAJR("النَّمْلِ", "naml", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "She said to the ants: «Enter your houses before the troops come.»", "tr": "Karıncalara dedi ki: «Askerler gelmeden evlerinize girin.»"},
 "tokens": [QALAT("فَقَالَتْ"), LI_AL("لِلنَّمْلِ", "naml", "النَّمْلِ", punct=":"),
  AMR("ادْخُلُوا", "dakhala", waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi"),
  ENC_NOUN("بُيُوتَكُمْ", "bayt", "كُمْ", "maful", extra=["jam-taksir"]), ZARF("قَبْلَ", "qabla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause it builds is annexed to «before», in the seat of jarr", "; kurduğu müevvel masdar muzâfun ileyh olarak mahallen mecrûr"),
  MANSUB_AN("يَأْتِيَ", "ata", ["naqis-verbs"], hidden=False), FAIL("الْجُنُودُ", "jund", extra=["jam-taksir"], punct=".")]})
S2.append({"id": "s6", "translation": {"en": "Sulayman heard the ant's words.", "tr": "Süleyman karıncanın sözünü işitti."},
 "tokens": [MADI("فَسَمِعَ", "samia"), SUL_F(), MAFUL("كَلَامَ", "kalam", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("النَّمْلَةِ", "namla", punct=".")]})
S2.append({"id": "s7", "translation": {"en": "He laughed at her words.", "tr": "Onun sözüne güldü."},
 "tokens": [MADI("فَضَحِكَ", "dahika", hidden=True), MIN(), ENC_NOUN("كَلَامِهَا", "kalam", "هَا", "majr", punct=".")]})
S2.append({"id": "s8", "translation": {"en": "And he thanked Allah for this favour.", "tr": "Bu nimet için Allah'a şükretti."},
 "tokens": [MADI("وَشَكَرَ", "shakara", hidden=True), ALLAH_MAF(), ALA(), HADHIHI_J(), BADAL("النِّعْمَةِ", "nima", "jarr", punct=".")]})
S2.append({"id": "s9", "translation": {"en": "He said: «My Lord, make me a thankful servant.»", "tr": "Dedi ki: «Rabbim, beni şükreden bir kul kıl.»"},
 "tokens": [QALA_H(), RABBI(punct="،"), AMR("اجْعَلْنِي", "jaala", enc="نِي", wiqaya=True, note_ar=OBJ1[0], note_en=OBJ1[1], note_tr=OBJ1[2]), MAFUL("عَبْدًا", "abd", note_ar=OBJ2[0], note_en=OBJ2[1], note_tr=OBJ2[2]), NAAT("شَاكِرًا", "shakir", "nasb", ["ism-fail"], punct=".")]})
S2.append({"id": "s10", "translation": {"en": "And he ordered the troops to wait until the ants had entered their houses.", "tr": "Askerlere, karıncalar evlerine girinceye kadar beklemelerini emretti."},
 "tokens": [MADI("وَأَمَرَ", "amara-command", hidden=True), MAFUL("الْجُنُودَ", "jund", extra=["jam-taksir"]),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِحَرْفِ جَرٍّ مَحْذُوفٍ، أَيْ: بِالِانْتِظَارِ", "; the clause it builds fills the seat of jarr after a dropped letter — «(with) waiting»", "; kurduğu müevvel masdar, hazfedilmiş bir cer harfiyle mahallen mecrûr — «beklemekle»"),
  FIVE_NASB("يَنْتَظِرُوا", "intazara", ["form-viii-verbs"]), HATTA(), MANSUB_AN("يَدْخُلَ", "dakhala", by="أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", hidden=False), FAIL("النَّمْلُ", "naml"), ENC_NOUN("بُيُوتَهُ", "bayt", "هُ", "maful", extra=["jam-taksir"], punct=".")]})

# ---- Chapter 3 — غَيْبَةُ الْهُدْهُدِ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "Sulayman used to inspect the birds every day.", "tr": "Süleyman her gün kuşları yoklardı."},
 "tokens": [KANA("وَكَانَ"), SUL_ISMK(), MUDARI_KH("يَتَفَقَّدُ", "tafaqqada", ["form-v-verbs"]), MAFUL("الطَّيْرَ", "tayr"), ZARF("كُلَّ", "kull", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), MUDAF_ILAYH("يَوْمٍ", "yawm", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "One day he looked and did not see the hoopoe.", "tr": "Bir gün baktı, hüdhüdü göremedi."},
 "tokens": [MADI("فَنَظَرَ", "nazara", hidden=True), ZARF("يَوْمًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False), LAM_JAZM("فَلَمْ"),
  tok("يَرَ", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Present verb in jazm after لَمْ, its sign the dropped weak letter; the doer «he» is hidden.", "Lem ile meczûm muzâri, alâmeti illet harfinin hazfi; fâil gizli zamir «o»."), HUDHUD_MAF(punct=".")]})
S3.append({"id": "s3", "translation": {"en": "He said: «Where is the hoopoe?»", "tr": "Dedi ki: «Hüdhüd nerede?»"},
 "tokens": [QALA_H("فَقَالَ"), AYNA(), MUBTADA("الْهُدْهُدُ", "hudhud", note_ar=" مُؤَخَّرٌ", note_en=" (placed after its predicate)", note_tr=" (haberinden sonraya bırakılmış)", punct="؟")]})
S3.append({"id": "s4", "translation": {"en": "«Why is he absent from the birds?»", "tr": "«Kuşların arasından niçin kayboldu?»"},
 "tokens": [LIMADHA(), MADI("غَابَ", "ghaba", ["hollow-verbs"], hidden=True), AN_KASRA(), MAJR("الطَّيْرِ", "tayr", punct="؟")]})
S3.append({"id": "s5", "translation": {"en": "And Sulayman grew very angry.", "tr": "Süleyman çok öfkelendi."},
 "tokens": [MADI("وَغَضِبَ", "ghadiba"), SUL_F(), MUTLAQ("غَضَبًا", "ghadab"), NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct=".")]})
S3.append({"id": "s6", "translation": {"en": "He said: «I shall punish the hoopoe severely.»", "tr": "Dedi ki: «Hüdhüdü şiddetle cezalandıracağım.»"},
 "tokens": [QALA_H(), SA_MUDARI("سَأُعَاقِبُ", "aqaba", "أُعَاقِبُ", ["form-iii-verbs"]), HUDHUD_MAF(), MUTLAQ("عِقَابًا", "iqab"), NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct=".")]})
S3.append({"id": "s7", "translation": {"en": "The hoopoe came after a little while.", "tr": "Az sonra hüdhüd geldi."},
 "tokens": [MADI("فَجَاءَ", "jaa", ["hollow-verbs"]), HUDHUD_F(), ZARF("بَعْدَ", "bada", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), MUDAF_ILAYH("قَلِيلٍ", "qalil", punct=".")]})
S3.append({"id": "s8", "translation": {"en": "He said: «O Sulayman, I have seen a wondrous thing.»", "tr": "Dedi ki: «Ey Süleyman, şaşılacak bir şey gördüm.»"},
 "tokens": [QALA_H(), YA(), SUL_MUNADA(punct="،"), MADI_T("رَأَيْتُ", "raa", who="ana", extra=["naqis-verbs"]), MAFUL("شَيْئًا", "shay"), NAAT("عَجِيبًا", "ajib", "nasb", ["sifa-mushabbaha"], punct=".")]})
S3.append({"id": "s9", "translation": {"en": "«I saw in the land of Saba a mighty queen.»", "tr": "«Sebe' ülkesinde büyük bir kraliçe gördüm.»"},
 "tokens": [MADI_T("رَأَيْتُ", "raa", who="ana", extra=["naqis-verbs"]), FI(), MAJR("أَرْضِ", "ard", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("سَبَإٍ", "saba"), MAFUL("مَلِكَةً", "malika"), NAAT("عَظِيمَةً", "azim", "nasb", ["sifa-mushabbaha"], punct=".")]})
S3.append({"id": "s10", "translation": {"en": "«She has a great throne and many troops.»", "tr": "«Onun büyük bir tahtı ve çok askeri var.»"},
 "tokens": [tok("وَلَهَا", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "mubtada-khabar"], WA_AR + "اللَّامُ حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "The waw conjoins; the lam is a jarr letter and «her» fills the seat of jarr — the jarr phrase is the fronted khabar.", "«ve» + lâm cer harfi; «onun» zamiri mahallen mecrûr — câr-mecrûr öne alınmış haberdir.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "li", "prep"), seg("هَا", "pron-3fs", "pron")]),
  MUBTADA("عَرْشٌ", "arsh", note_ar=" مُؤَخَّرٌ", note_en=" (placed after its predicate)", note_tr=" (haberinden sonraya bırakılmış)"), NAAT("كَبِيرٌ", "kabir", "raf", ["sifa-mushabbaha"]),
  ATF("وَجُنُودٌ", "jund", case="raf", extra=["jam-taksir"], note_ar=JUNUD[0], note_en=JUNUD[1], note_tr=JUNUD[2]), NAAT_WAW("كَثِيرُونَ", "kathir", punct=".")]})
S3.append({"id": "s11", "translation": {"en": "«She and her people bow down to the sun, and do not worship Allah.»", "tr": "«O ve kavmi güneşe secde ediyor, Allah'a kulluk etmiyorlar.»"},
 "tokens": [WA_HIYA(), ATF("وَقَوْمُهَا", "qawm", case="raf", extra=["idafa-definiteness", "al-bariz-al-muttasil"], note_ar="، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ", note_en=", annexed to «her»", note_tr=", «onun» zamirine muzâf", segments=[seg("وَ", "wa", "conj"), seg("قَوْمُ", "qawm", "noun"), seg("هَا", "pron-3fs", "pron")]),
  MUDARI5("يَسْجُدُونَ", "sajada", ["thulathi-mujarrad-babs"], role_ar=KH_CL[0], role_en=KH_CL[1], role_tr=KH_CL[2]), LI_AL("لِلشَّمْسِ", "shams", "الشَّمْسِ", punct="،"),
  WA_LA_NAFIYA(), MUDARI5("يَعْبُدُونَ", "abada", ["thulathi-mujarrad-babs"], role_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ", role_en="; the clause is joined to the predicate clause", role_tr="; cümle haber cümlesine ma'tûf"), ALLAH_MAF(punct=".")]})

# ---- Chapter 4 — الرِّسَالَةُ وَالْإِيمَانُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "Sulayman wrote a letter to the queen.", "tr": "Süleyman kraliçeye bir mektup yazdı."},
 "tokens": [MADI("فَكَتَبَ", "kataba"), SUL_F(), MAFUL("رِسَالَةً", "risala"), ILA(), MALIKA_J(punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He said to the hoopoe: «Go with this letter to her.»", "tr": "Hüdhüde dedi ki: «Bu mektupla ona git.»"},
 "tokens": [QALA_H(punct=None), LI_AL("لِلْهُدْهُدِ", "hudhud", "الْهُدْهُدِ", punct=":"), AMR("اذْهَبْ", "dhahaba"),
  tok("بِهَذِهِ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهَذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ.", "The ba is a jarr letter; «this» is a demonstrative built on kasra, in the seat of jarr.", "Bâ cer harfi; «bu» işaret ismi kesre üzere mebnî, mahallen mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("هَذِهِ", "hadhihi", "pron")]),
  BADAL("الرِّسَالَةِ", "risala", "jarr"), JARR_PRON("إِلَيْهَا", "ila", "إِلَيْ", "هَا", " («ona»)", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "The hoopoe flew to Saba and dropped the letter to the queen.", "tr": "Hüdhüd Sebe'e uçtu ve mektubu kraliçeye bıraktı."},
 "tokens": [MADI("فَطَارَ", "tara", ["hollow-verbs"]), HUDHUD_F(), ILA(), MAJR("سَبَإٍ", "saba", punct="،"), MADI_ALIF("وَأَلْقَى", "alqa", ["form-iv-verbs"], hidden=True), MAFUL("الرِّسَالَةَ", "risala"), ILA(), MALIKA_J(punct=".")]})
S4.append({"id": "s4", "translation": {"en": "The queen read the letter.", "tr": "Kraliçe mektubu okudu."},
 "tokens": [MADI("فَقَرَأَتِ", "qaraa", fem=True, kasra=True), MALIKA_F(), MAFUL("الرِّسَالَةَ", "risala", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "In it Sulayman called her to Islam.", "tr": "Süleyman onda onu İslâm'a çağırıyordu."},
 "tokens": [ENC_MADI("وَدَعَاهَا", "daa", "هَا", alif=True), SUL_F(), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)"), ILA(), MAJR("الْإِسْلَامِ", "islam", punct=".")]})
S4.append({"id": "s6", "translation": {"en": "He said to her: «Do not worship the sun; worship Allah alone.»", "tr": "Ona dedi ki: «Güneşe tapma; yalnız Allah'a kulluk et.»"},
 "tokens": [QALA_H(punct=None), LAHU("لَهَا", "pron-3fs", " («ona»)", punct=":"), LA_NAHIYA(), FEM2("تَعْبُدِي", "abada", "jazm", ["thulathi-mujarrad-babs"]), MAFUL("الشَّمْسَ", "shams", punct="،"), FEM2("وَاعْبُدِي", "abada", "amr"), ALLAH_MAF(), WAHDAHU(punct=".")]})
S4.append({"id": "s7", "translation": {"en": "The queen sent him a great gift.", "tr": "Kraliçe ona büyük bir hediye gönderdi."},
 "tokens": [MADI("فَأَرْسَلَتِ", "arsala", ["form-iv-verbs"], fem=True, kasra=True), MALIKA_F(), JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)"), MAFUL("هَدِيَّةً", "hadiyya"), NAAT("عَظِيمَةً", "azim", "nasb", ["sifa-mushabbaha"], punct=".")]})
S4.append({"id": "s8", "translation": {"en": "But Sulayman did not accept the gift.", "tr": "Fakat Süleyman hediyeyi kabul etmedi."},
 "tokens": [LAM_JAZM("فَلَمْ"), tok("يَقْبَلْ", "qabila", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ.", "Present verb in jazm after لَمْ, its sign the sukun.", "Lem ile meczûm muzâri, alâmeti sükûn."), SUL_F(), MAFUL("الْهَدِيَّةَ", "hadiyya", punct=".")]})
S4.append({"id": "s9", "translation": {"en": "He said: «I do not want your wealth; I want your faith.»", "tr": "Dedi ki: «Malınızı istemiyorum; îmânınızı istiyorum.»"},
 "tokens": [QALA_H(), LA_NAFIYA(), MUDARI("أُرِيدُ", "arada", ["hollow-verbs", "form-iv-verbs"], who="أَنَا", wujub=True), ENC_NOUN("مَالَكُمْ", "mal", "كُمْ", "maful", punct="،"),
  MUDARI("أُرِيدُ", "arada", ["hollow-verbs", "form-iv-verbs"], who="أَنَا", wujub=True), ENC_NOUN("إِيمَانَكُمْ", "iman", "كُمْ", "maful", punct=".")]})
S4.append({"id": "s10", "translation": {"en": "So the queen came to Sulayman with her people.", "tr": "Bunun üzerine kraliçe kavmiyle Süleyman'a geldi."},
 "tokens": [MADI("فَجَاءَتِ", "jaa", ["hollow-verbs"], fem=True, kasra=True), MALIKA_F(), ILA(), SUL_J(), MAA(), ENC_NOUN("قَوْمِهَا", "qawm", "هَا", "mudaf", punct=".")]})
S4.append({"id": "s11", "translation": {"en": "She saw his mighty kingdom, and knew that Sulayman's kingdom was from Allah.", "tr": "Onun büyük mülkünü gördü ve Süleyman'ın mülkünün Allah katından olduğunu anladı."},
 "tokens": [RAAT("فَرَأَتْ"), ENC_NOUN("مُلْكَهُ", "mulk", "هُ", "maful"), NAAT("الْعَظِيمَ", "azim", "nasb", ["sifa-mushabbaha"], punct="،"),
  MADI("وَعَلِمَتْ", "alima", fem=True, hidden=True), ANNA(),
  tok("مُلْكَ", "mulk", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb, annexed.", "Enne'nin ismi, mansûb; muzâf."), SUL_MI(),
  PREP("مِنْ", "min", role_ar=KH_ANNA[0], role_en=KH_ANNA[1], role_tr=KH_ANNA[2], gloss_tr="«-den»"),
  tok("عِنْدِ", "inda", "noun", ["huruf-jarr", "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ.", "The adverb «at» drawn into jarr by مِنْ, its sign the kasra; annexed.", "Mekân zarfı «kat», min ile mecrûr, alâmeti kesre; muzâf."), ALLAH_MI(punct=".")]})
S4.append({"id": "s12", "translation": {"en": "She believed in Allah, and all her people believed.", "tr": "Allah'a îmân etti; kavminin hepsi de îmân etti."},
 "tokens": [MADI("فَآمَنَتْ", "amana", ["form-iv-verbs"], fem=True, hidden=True),
  tok("بِاللهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "The ba is a jarr letter; the Name of Majesty is in jarr.", "Bâ cer harfi; lafza-i celâl mecrûr.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  MADI("وَآمَنَ", "amana", ["form-iv-verbs"]), ENC_NOUN("قَوْمُهَا", "qawm", "هَا", "fail"), KULLUHUM(punct=".")]})
S4.append({"id": "s13", "translation": {"en": "And they became Muslims.", "tr": "Ve müslüman oldular."},
 "tokens": [SARU("وَصَارُوا"), KHK("مُسْلِمِينَ", "muslim", extra=["jam-mudhakkar-salim", "ism-fail"], sign="بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the ya, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için yâ ile", punct=".")]})

TITLES = [
 {"ar": "مُلْكُ سُلَيْمَانَ", "en": "The Kingdom of Sulayman", "tr": "Süleyman'ın Mülkü"},
 {"ar": "وَادِي النَّمْلِ", "en": "The Valley of the Ants", "tr": "Karınca Vadisi"},
 {"ar": "غَيْبَةُ الْهُدْهُدِ", "en": "The Absence of the Hoopoe", "tr": "Hüdhüdün Kaybolması"},
 {"ar": "الرِّسَالَةُ وَالْإِيمَانُ", "en": "The Letter and the Faith", "tr": "Mektup ve Îmân"},
]
CHAPS = [S1, S2, S3, S4]


# ---- the glossary: copied from the packages that own each key (the lemma-identity rule); nothing is new
PREF = ["nuh-wa-al-safina", "musa-fi-madyan", "musa-wal-khadir", "musa-wa-bani-israil", "musa-wa-firawn", "bad-al-amali", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
        "jumal-al-tadrib", "talkhis-al-miftah", "al-kafiya", "izhar-al-asrar", "aqaid-ahl-al-sunna", "wasiyyat-abi-hanifa", "wasiyyat-abi-yusuf-l5", "aqaid-ahl-al-sunna"]
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

NEW_GLOSS = {}
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
 "id": "sulayman-wa-al-hudhud",
 "storyGroup": "sulayman-wa-al-hudhud",
 "title": {"ar": "سُلَيْمَانُ وَالْهُدْهُدُ", "en": "Sulayman and the Hoopoe", "tr": "Süleyman ve Hüdhüd"},
 "subtitle": {"ar": "قِصَّةُ سُلَيْمَانَ وَالنَّمْلَةِ وَالْهُدْهُدِ لِلْمُبْتَدِئِينَ — الْمُلْكُ، وَالْوَادِي، وَالرِّسَالَةُ",
              "en": "The story of Sulayman, the ant and the hoopoe, for beginners — the kingdom, the valley, the letter",
              "tr": "Yeni başlayanlar için Süleyman, karınca ve hüdhüd kıssası — mülk, vadi, mektup"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-07",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِقِصَّةِ سُلَيْمَانَ عَلَيْهِ السَّلَامُ مَعَ النَّمْلَةِ وَالْهُدْهُدِ وَمَلِكَةِ سَبَإٍ كَمَا تُرْوَى لِلْأَطْفَالِ (عَلَى ضَوْءِ سُورَةِ النَّمْلِ ١٥–٤٤)، عَلَى طَرِيقَةِ الْقِرَاءَةِ الْمُتَدَرِّجَةِ لِلنَّدْوِيِّ. لَمْ تُنْقَلْ آيَةٌ بِنَصِّهَا، وَلَا يُسْتَشْهَدُ بِجُمْلَةٍ هُنَا عَلَى أَنَّهَا نَصٌّ تُرَاثِيٌّ. كُتِبَتْ لِلْمَمْنُوعِ مِنَ الصَّرْفِ فِي أَحْوَالِهِ، وَالْمَفْعُولَيْنِ، وَالْمُنَادَى الْمُضَافِ إِلَى يَاءِ الْمُتَكَلِّمِ، وَلَا النَّاهِيَةِ مَعَ يَاءِ الْمُخَاطَبَةِ، وَالتَّوْكِيدِ الْمَعْنَوِيِّ، وَالْحَالِ «وَحْدَهُ»، وَأَنَّ وَمَعْمُولَيْهَا، وَالِاسْمِ الْمَنْقُوصِ.",
  "en": "ORIGINAL Level-1 graded Arabic: the story of Sulayman (peace be upon him) with the ant, the hoopoe and the queen of Saba as it is told to children (after the Qurʾānic narrative in al-Naml 15–44), composed editorially in the manner of Nadwī's graded readers — short كَانَ-framed sentences, one event per line, the vocabulary repeated. No āya is quoted verbatim; no sentence here may be cited as a classical text. Written to meet the diptote in its three cases, the verb with two objects, the vocative annexed to the speaker's ya, the prohibitive لَا with the feminine ya, the tawkid of meaning, the hal وَحْدَهُ, أَنَّ with its two terms, and the manqus noun.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Süleyman aleyhisselâmın karınca, hüdhüd ve Sebe' melikesi ile kıssasının çocuklara anlatıldığı şekli (Neml 15–44'teki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde telif edilmiştir — kısa, kâne ile kurulu cümleler, her satırda bir olay, tekrar eden kelime hazinesi. Hiçbir âyet aynen aktarılmamıştır; buradaki hiçbir cümle klasik bir metin olarak kaynak gösterilemez. Üç hâliyle gayr-i munsarıf, iki mef'ûl alan fiil, mütekellim yâ'sına muzâf münâdâ, muhâtaba yâ'sıyla nehiy lâ'sı, ma'nevî te'kîd, «vahdehû» hâli, enne ve iki ma'mûlü ve mankûs isim için yazıldı.",
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
