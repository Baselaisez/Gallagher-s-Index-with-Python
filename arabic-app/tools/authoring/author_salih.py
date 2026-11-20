"""Author content/samples/salih-wa-al-naqa — «صَالِحٌ وَالنَّاقَةُ», the sixth ORIGINAL Level-1 story (wave 93).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Ṣāliḥ and Thamūd (al-Aʿrāf
73–79, Hūd 61–68, al-Shuʿarāʾ 141–159, al-Shams 11–15) as it is commonly retold to children. No āya is quoted; no
sentence here may be cited as a classical text. Four chapters, forty sentences. Every token carries trilingual iʿrāb.
Verb paradigms and glossary entries are COPIED from the packages that already own the lemma (the lemma-identity rule);
only the verb عَقَرَ is new. The house helpers are shared with author_nuh.py / author_musa4.py verbatim.

    QISSA_PKG_ROOT=<dir> python3 author_salih.py     # a dry run writes under <dir>/salih-wa-al-naqa
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "salih-wa-al-naqa"
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

# ---- the pronoun tables need the plural «you» and the kasra-/damma-voweled «them»
PRON.update({"كُمْ": "pron-2mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp"})
PRON_AR.update({"كُمْ": "كُمْ", "هِمْ": "هِمْ", "هُمُ": "هُمْ"})

# ============ «صَالِحٌ وَالنَّاقَةُ» — the sixth story: four chapters ============
SALIH_F = lambda punct=None: FAIL("صَالِحٌ", "salih-nabi", "propn", note_ar=" — عَلَمٌ", note_en=" — a proper name", note_tr=" — özel isim", punct=punct)
SALIH_ISMK = lambda punct=None: ISMK("صَالِحٌ", "salih-nabi", "propn", note_ar=" — عَلَمٌ", note_en=" — a proper name", note_tr=" — özel isim", punct=punct)
SALIH_MUNADA = lambda punct=None: tok("صَالِحُ", "salih-nabi", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on damma, in the seat of nasb.", "Münâdâ: müfred alem, damme üzere mebnî, mahallen mansûb.", punct=punct)
QAWMI = lambda punct=None: tok("قَوْمِ", "qawm", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ الْمَحْذُوفَةِ.", "The vocative «my people», annexed to a dropped ya of the speaker: in nasb by an estimated fatha, the kasra pointing to the dropped ya.", "Münâdâ «kavmim»: hazfedilmiş mütekellim yâ'sına muzâf; takdîrî fetha ile mansûb, kesre hazfedilen yâ'ya delâlet eder.", punct=punct)
def KANU(full):
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
        ar0 + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.",
        en0 + "كَانُوا is the defective past verb built on damma before the waw of the group; that waw is the noun of كَانَ, in the seat of raf'.",
        tr0 + "kânû: cemâat vâvı bitiştiği için damme üzere mebnî nâkıs mâzî; vâv, kâne'nin ismi olarak mahallen merfû.",
        segments=[s for s in [sg, seg(stem[:-1], "kana", "verb"), seg("ا", "pron-3mp", "pron")] if s])
WA_LA_NAFIYA = lambda: tok("وَلَا", "la-nafiya", "part", ["la-nafiya"], WA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The waw conjoins; لَا negates and governs nothing.", "«ve» + nefiy lâ'sı; amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
LA_NAFIYA = lambda: tok("لَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The negating لَا, which governs nothing.", "Nefiy lâ'sı; amel etmez.")
WA_LA_NAHIYA = lambda: tok("وَلَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], WA_AR + "لَا النَّاهِيَةُ حَرْفُ نَهْيٍ وَجَزْمٍ.", "The waw conjoins; the prohibitive لَا «do not» governs jazm.", "«ve» + nehiy lâ'sı: nehiy ve cezm harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nahiya", "part")])
WA_LAM = lambda: tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates, gives jazm and turns the present to the past.", "«ve» + lem: nefiy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")])
def FIVE_JAZM(full, lex, by, by_en, by_tr, extra=None, enc=None, punct=None):
    """تَمَسُّوهَا، يَتُوبُوا، تَسْمَعُوا: one of the five verbs in jazm by the dropped nun"""
    stem = full[:-len(enc)] if enc else full
    encs = ("، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ") if enc else ""
    segs = [seg(stem[:-1] if not enc else stem, lex, "verb")] + ([seg("ا", "pron-3mp", "pron")] if not enc else []) + ([seg(enc, PRON[enc], "pron")] if enc else [])
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil"] + (["maful-bihi"] if enc else []) + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ" + by + " وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + encs + ".",
        "Present verb in jazm by " + by_en + ", its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf'" + ("; the attached pronoun is its object" if enc else "") + ".",
        by_tr + " ile meczûm muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû" + ("; bitişik zamir mef'ûlün bih" if enc else "") + ".", punct=punct, segments=segs)
def ISHARA(full, lex, seat_ar, seat_en, seat_tr, built_ar="السُّكُونِ", built_en="sukun", built_tr="sükûn", extra=None, punct=None):
    return tok(full, lex, "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى " + built_ar + " فِي مَحَلِّ " + seat_ar + ".", "A demonstrative, built on " + built_en + ", in the seat of " + seat_en + ".", "İşaret ismi, " + built_tr + " üzere mebnî, " + seat_tr + " olarak mahallen.", punct=punct)
def BADAL(full, lex, case, extra=None, punct=None):
    sign = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, lex, "noun", ["badal", "asma-al-ishara"] + (extra or []), "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ " + sign + ".", "A badal of the demonstrative, in the same case.", "İşaret isminden bedel; onun i'râbını alır.", punct=punct)
JIBAL_J = lambda punct=None: MAJR("الْجِبَالِ", "jabal", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِجَبَلٍ", note_en=" — the broken plural of «mountain»", note_tr=" — «dağ»ın cem-i mükesseri", punct=punct)
ASNAM_MAF = lambda punct=None: MAFUL("الْأَصْنَامَ", "sanam", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِصَنَمٍ", note_en=" — the broken plural of «idol»", note_tr=" — «put»un cem-i mükesseri", punct=punct)
KUFFAR_F = lambda punct=None: FAIL("الْكُفَّارُ", "kafir", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِكَافِرٍ", note_en=" — the broken plural of «denier»", note_tr=" — «kâfir»in cem-i mükesseri", punct=punct)
NAQA_MAF = lambda punct=None: MAFUL("النَّاقَةَ", "naqa", punct=punct)
NAQA_ISMK = lambda punct=None: ISMK("النَّاقَةُ", "naqa", punct=punct)
FI = lambda: PREP("فِي", "fi", gloss_tr="«-de»")
MIN = lambda: PREP("مِنْ", "min", gloss_tr="«-den»")
ILA = lambda: PREP("إِلَى", "ila", gloss_tr="«-e»")
ALLAH_J = lambda punct=None: MAJR("اللهِ", "allah", "propn", note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct=punct)
QALU = lambda punct=":": VERB_WAW("وَقَالُوا", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlün bihtir", punct=punct)
SILA = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
HAL_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause fills the seat of nasb as a hal", "; cümle hâl olarak mahallen mansûb")
KH_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", "; the clause fills the seat of raf' as the khabar", "; cümle haber olarak mahallen merfû")

# ---- Chapter 1 — ثَمُودُ وَصَالِحٌ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "The people of Thamud used to live in the mountains.", "tr": "Semûd kavmi dağlarda yaşardı."},
 "tokens": [KANA("كَانَ"), tok("قَوْمُ", "qawm", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of كَانَ, in raf', annexed.", "Kâne'nin ismi, merfû; muzâf."),
  MUDAF_ILAYH("ثَمُودَ", "thamud", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR + " لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (اسْمُ قَبِيلَةٍ أَعْجَمِيٌّ)", note_en=" — a diptote (the foreign name of a tribe), so the fatha stands in for the kasra", note_tr=" — gayr-i munsarıf (yabancı kabile adı); kesre yerine fetha"),
  MUDARI5_KH("يَسْكُنُونَ", "sakana", ["thulathi-mujarrad-babs"]), FI(), JIBAL_J(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "And they used to carve their houses in the mountains.", "tr": "Evlerini dağlara oyarlardı."},
 "tokens": [KANU("وَكَانُوا"), MUDARI5_KH("يَنْحِتُونَ", "nahata", ["thulathi-mujarrad-babs"]), ENC_NOUN("بُيُوتَهُمْ", "bayt", "هُمْ", "maful", extra=["jam-taksir"]), FI(), JIBAL_J(punct=".")]})
S1.append({"id": "s3", "translation": {"en": "They had a wide land and plenty of water.", "tr": "Geniş bir toprakları ve bol suları vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True), LAHU("لَهُمْ", "pron-3mp", " («onlara»)", grammar=["kana-wa-akhawatuha"]),
  ISMK("أَرْضٌ", "ard", muakhkhar=True, note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ قَبْلَهُ خَبَرُ كَانَ مُقَدَّمٌ", note_en="; the jarr phrase before it is the fronted predicate of كَانَ", note_tr="; önündeki câr-mecrûr kâne'nin öne alınmış haberidir"),
  NAAT("كَبِيرَةٌ", "kabir", "raf", ["sifa-mushabbaha"]), ATF("وَمَاءٌ", "ma-water", case="raf"), NAAT("كَثِيرٌ", "kathir", "raf", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "But they used to worship idols and did not worship Allah.", "tr": "Fakat putlara tapıyor, Allah'a kulluk etmiyorlardı."},
 "tokens": [KANU("فَكَانُوا"), MUDARI5_KH("يَعْبُدُونَ", "abada", ["thulathi-mujarrad-babs"]), ASNAM_MAF(punct="،"),
  WA_LA_NAFIYA(), MUDARI5("يَعْبُدُونَ", "abada", ["thulathi-mujarrad-babs"], role_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ", role_en="; the clause is joined to the predicate clause", role_tr="; cümle haber cümlesine ma'tûf"), ALLAH_MAF(punct=".")]})
S1.append({"id": "s5", "translation": {"en": "So Allah sent to them a man from among them, whose name was Salih.", "tr": "Allah onlara kendi içlerinden, adı Sâlih olan bir adam gönderdi."},
 "tokens": [MADI("فَأَرْسَلَ", "arsala", ["form-iv-verbs"]), ALLAH_F(), ILAYHIM(), MAFUL("رَجُلًا", "rajul"),
  MINHUM(punct="،"),
  ENC_NOUN("اسْمُهُ", "ism", "هُ", "mubtada", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِرَجُلٍ", note_en="; the clause qualifies «a man» — in the seat of nasb as its na't", note_tr="; cümle «adam»ın na'tı olarak mahallen mansûb"),
  KHABAR("صَالِحٌ", "salih-nabi", note_ar=" — عَلَمٌ", note_en=" — a proper name", note_tr=" — özel isim", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "Salih was a righteous, truthful man.", "tr": "Sâlih sâlih ve doğru sözlü bir adamdı."},
 "tokens": [KANA("وَكَانَ"), SALIH_ISMK(), KHK("رَجُلًا", "rajul"), NAAT("صَالِحًا", "salih", "nasb", ["ism-fail"]), NAAT("صَادِقًا", "sadiq", "nasb", ["ism-fail"], punct=".")]})
S1.append({"id": "s7", "translation": {"en": "Salih said to his people: «O my people, worship Allah and leave the idols.»", "tr": "Sâlih kavmine dedi ki: «Ey kavmim, Allah'a kulluk edin ve putları bırakın.»"},
 "tokens": [QALA("فَقَالَ"), SALIH_F(),
  tok("لِقَوْمِهِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The lam is a jarr letter; «people» is in jarr and annexed, the attached pronoun its second term.", "Lâm cer harfi; «kavim» mecrûr ve muzâf; bitişik zamir muzâfun ileyh.", punct=":", segments=[seg("لِ", "li", "prep"), seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")]),
  YA(), QAWMI(punct="،"),
  AMR("اعْبُدُوا", "abada", ["thulathi-mujarrad-babs"], waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi", segments=[seg("اعْبُدُو", "abada", "verb"), seg("ا", "pron-3mp", "pron")]),
  ALLAH_MAF(punct="،"),
  AMR("وَاتْرُكُوا", "taraka", ["thulathi-mujarrad-babs"], waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi", segments=[seg("وَ", "wa", "conj"), seg("اتْرُكُو", "taraka", "verb"), seg("ا", "pron-3mp", "pron")]),
  ASNAM_MAF(punct=".")]})
S1.append({"id": "s8", "translation": {"en": "The people said: «O Salih, why do you say these words?»", "tr": "Kavmi dedi ki: «Ey Sâlih, bu sözleri niçin söylüyorsun?»"},
 "tokens": [QALA("فَقَالَ"), FAIL("الْقَوْمُ", "qawm", punct=":"), YA(), SALIH_MUNADA(punct="،"), LIMADHA(),
  MUDARI("تَقُولُ", "qala", ["hollow-verbs"], who="أَنْتَ"),
  ISHARA("هَذَا", "hadha", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mef'ûlün bih", extra=["maful-bihi"]),
  BADAL("الْكَلَامَ", "kalam", "nasb", punct="؟")]})
S1.append({"id": "s9", "translation": {"en": "Most of the people called him a liar, and only a few of them believed in him.", "tr": "Kavmin çoğu onu yalanladı; onlardan ancak azı ona inandı."},
 "tokens": [ENC_MADI("فَكَذَّبَهُ", "kadhdhaba", "هُ", ["form-ii-verbs"]),
  tok("أَكْثَرُ", "akthar", "noun", ["fail", "idafa-definiteness", "ism-tafdil"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "The doer, in raf', annexed — an elative «most of».", "Fâil, merfû; muzâf — ism-i tafdîl «çoğu»."),
  MUDAF_ILAYH("الْقَوْمِ", "qawm", punct="،"), MADI("وَآمَنَ", "amana", ["form-iv-verbs"]), BIHI(), FAIL("قَلِيلٌ", "qalil"), MINHUM(punct=".")]})
S1.append({"id": "s10", "translation": {"en": "And those who believed in him were among the poor.", "tr": "Ona inananlar ise yoksullardandı."},
 "tokens": [KANA("وَكَانَ"),
  tok("الَّذِينَ", "alladhina", "pron", ["kana-wa-akhawatuha", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "A relative pronoun «those who», built on fatha, in the seat of raf' as the noun of كَانَ.", "İsm-i mevsûl «…-enler», fetha üzere mebnî, kâne'nin ismi olarak mahallen merfû."),
  VERB_WAW("آمَنُوا", "amana", ["form-iv-verbs", "ism-mawsul"], note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]), BIHI(), MINA(),
  MAJR("الْفُقَرَاءِ", "faqir", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِفَقِيرٍ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ", note_en=" — the broken plural of «poor»; the jarr phrase is the predicate of كَانَ", note_tr=" — «fakir»in cem-i mükesseri; câr-mecrûr kâne'nin haberidir", punct=".")]})

# ---- Chapter 2 — نَاقَةُ اللهِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "The people said to Salih: «Bring out for us a she-camel from this mountain; then we will believe in you.»", "tr": "Kavmi Sâlih'e dedi ki: «Bize şu dağdan bir dişi deve çıkar; o zaman sana inanırız.»"},
 "tokens": [QALA("فَقَالَ"), FAIL("الْقَوْمُ", "qawm"),
  tok("لِصَالِحٍ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَصَالِحٍ مَجْرُورٌ بِالْكَسْرَةِ.", "The lam is a jarr letter; Salih is in jarr.", "Lâm cer harfi; Sâlih mecrûr.", punct=":", segments=[seg("لِ", "li", "prep"), seg("صَالِحٍ", "salih-nabi", "propn")]),
  AMR("أَخْرِجْ", "akhraja", ["form-iv-verbs"]), LAHU("لَنَا", "pron-1p", " («bize»)"), MAFUL("نَاقَةً", "naqa"), MIN(),
  ISHARA("هَذَا", "hadha", "جَرٍّ", "jarr", "mecrûr", extra=["huruf-jarr"]), BADAL("الْجَبَلِ", "jabal", "jarr", punct="،"),
  THUMMA(), MUDARI("نُؤْمِنُ", "amana", ["form-iv-verbs"], who="نَحْنُ"), JARR_PRON("بِكَ", "bi", "بِ", "كَ", " («sana»)", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "So Salih called upon his Lord.", "tr": "Bunun üzerine Sâlih Rabbine dua etti."},
 "tokens": [MADI_ALIF("فَدَعَا", "daa"), SALIH_F(), ENC_NOUN("رَبَّهُ", "rabb", "هُ", "maful", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "And out of the mountain came a huge she-camel.", "tr": "Dağdan kocaman bir dişi deve çıktı."},
 "tokens": [MADI("فَخَرَجَتْ", "kharaja", fem=True), MINA(), MAJR("الْجَبَلِ", "jabal"),
  FAIL("نَاقَةٌ", "naqa", note_ar=" مُؤَخَّرٌ", note_en=" — placed after the jarr phrase", note_tr=" — câr-mecrûrdan sonraya bırakılmış"), NAAT("عَظِيمَةٌ", "azim", "raf", ["sifa-mushabbaha"], punct=".")]})
S2.append({"id": "s4", "translation": {"en": "Salih said: «This is the she-camel of Allah, and she is a sign for you.»", "tr": "Sâlih dedi ki: «Bu Allah'ın devesidir ve o sizin için bir âyettir.»"},
 "tokens": [QALA("فَقَالَ"), SALIH_F(punct=":"),
  ISHARA("هَذِهِ", "hadhihi", "رَفْعٍ مُبْتَدَأٌ", "raf' as mubtada", "mübtedâ", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre", extra=["mubtada-khabar"]),
  tok("نَاقَةُ", "naqa", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The khabar, in raf', annexed.", "Haber, merfû; muzâf."), ALLAH_MI(punct="،"),
  tok("وَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], WA_AR + "هِيَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; «she» is a detached pronoun built on fatha, in the seat of raf' as mubtada.", "«ve» + munfasıl zamir «o», fetha üzere mebnî, mübtedâ olarak mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")]),
  KHABAR("آيَةٌ", "aya"), LAHU("لَكُمْ", "pron-2mp", " («size»)", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "«Leave her to eat in Allah's earth,»", "tr": "«Onu bırakın, Allah'ın arzında yesin;»"},
 "tokens": [AMR("اتْرُكُوهَا", "taraka", ["thulathi-mujarrad-babs"], enc="هَا", waw=True, built="حَذْفِ النُّونِ", built_en="the dropped nun", built_tr="nûnun hazfi", segments=[seg("اتْرُكُو", "taraka", "verb"), seg("هَا", "pron-3fs", "pron")]),
  MUDARI("تَأْكُلُ", "akala", ["al-hal-jumla-wa-rabituha"], who="هِيَ", note_ar=HAL_CL[0], note_en=HAL_CL[1], note_tr=HAL_CL[2]), FI(),
  tok("أَرْضِ", "ard", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "In jarr after the letter, annexed.", "Mecrûr; muzâf."), ALLAH_MI(punct="،")]})
S2.append({"id": "s6", "translation": {"en": "«and do not touch her with harm.»", "tr": "«ve ona bir kötülükle dokunmayın.»"},
 "tokens": [WA_LA_NAHIYA(), FIVE_JAZM("تَمَسُّوهَا", "massa", "لَا النَّاهِيَةِ", "the prohibitive لَا", "Nehiy lâ'sı", extra=["la-nahiya", "doubled-verbs"], enc="هَا"),
  tok("بِسُوءٍ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَسُوءٍ مَجْرُورٌ بِالْكَسْرَةِ.", "The ba is a jarr letter; «harm» is in jarr.", "Bâ cer harfi; «kötülük» mecrûr.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("سُوءٍ", "su", "noun")])]})
S2.append({"id": "s7", "translation": {"en": "The she-camel drinks the water one day, and the people drink on another day.", "tr": "Deve suyu bir gün içer, kavim de başka bir gün içer."},
 "tokens": [
  tok("تَشْرَبُ", "shariba", "verb", ["mudari-marfu", "thulathi-mujarrad-babs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ بَعْدَهُ.", "Present verb in raf'; the ta marks the feminine, and the doer follows.", "Merfû muzâri; tâ te'nîs içindir, fâili ondan sonra gelir."),
  FAIL("النَّاقَةُ", "naqa"), MAFUL("الْمَاءَ", "ma-water"), ZARF("يَوْمًا", "yawm", "زَمَانٍ", "time", "Zaman", mudaf=False, punct="،"),
  tok("وَيَشْرَبُ", "shariba", "verb", ["mudari-marfu", "thulathi-mujarrad-babs"], WA_AR + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.", "The waw conjoins; present verb in raf', its doer following.", "«ve» + merfû muzâri; fâili ondan sonra gelir.", segments=[seg("وَ", "wa", "conj"), seg("يَشْرَبُ", "shariba", "verb")]),
  FAIL("الْقَوْمُ", "qawm"), ZARF("يَوْمًا", "yawm", "زَمَانٍ", "time", "Zaman", mudaf=False),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى وَزْنِ أَفْعَلَ، فَلَا تَنْوِينَ.", "A na't in nasb — a diptote of the أَفْعَل pattern, so it takes no tanwin.", "Na't, mansûb — ef'al vezninde gayr-i munsarıf; tenvin almaz.", punct=".")]})
S2.append({"id": "s8", "translation": {"en": "So the she-camel used to eat from the land and drink from the water.", "tr": "Deve topraktan yer, sudan içerdi."},
 "tokens": [KANA("فَكَانَتِ", fem=True), NAQA_ISMK(),
  tok("تَأْكُلُ", "akala", "verb", ["kana-wa-akhawatuha", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "Present verb in raf'; the doer is a hidden «she», and the clause fills the seat of كَانَ's predicate.", "Merfû muzâri; fâil gizli «o» zamiri — cümle kâne'nin haberi olarak mahallen mansûb."),
  MINA(), MAJR("الْأَرْضِ", "ard"),
  MUDARI("وَتَشْرَبُ", "shariba", ["thulathi-mujarrad-babs"], who="هِيَ", note_ar=" — مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ", note_en="; joined to the predicate clause", note_tr="; haber cümlesine ma'tûf"), MINA(), MAJR("الْمَاءِ", "ma-water", punct=".")]})
S2.append({"id": "s9", "translation": {"en": "And the people used to look at her and marvel.", "tr": "İnsanlar ona bakıp hayret ederlerdi."},
 "tokens": [KANA("وَكَانَ"), ISMK("النَّاسُ", "nas"), MUDARI5_KH("يَنْظُرُونَ", "nazara", ["thulathi-mujarrad-babs"]), JARR_PRON("إِلَيْهَا", "ila", "إِلَيْ", "هَا", " («ona»)"),
  MUDARI5("وَيَعْجَبُونَ", "ajiba", ["thulathi-mujarrad-babs"], role_ar=" — مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ", role_en="; joined to the predicate clause", role_tr="; haber cümlesine ma'tûf", punct=".")]})
S2.append({"id": "s10", "translation": {"en": "And the she-camel was a sign for the believers.", "tr": "Deve, mü'minler için bir âyetti."},
 "tokens": [KANA("وَكَانَتِ", fem=True), NAQA_ISMK(), KHK("آيَةً", "aya"),
  tok("لِلْمُؤْمِنِينَ", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُؤْمِنِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "The lam is a jarr letter; «the believers» is in jarr by the ya — a sound masculine plural.", "Lâm cer harfi; «mü'minler» cem-i müzekker sâlim olduğu için yâ ile mecrûr.", punct=".", segments=[seg("لِ", "li", "prep"), seg("الْمُؤْمِنِينَ", "mumin", "noun")])]})

# ---- Chapter 3 — عَقْرُ النَّاقَةِ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "But the deniers hated the she-camel.", "tr": "Fakat kâfirler deveden nefret ettiler."},
 "tokens": [MADI("فَكَرِهَ", "kariha"), KUFFAR_F(), NAQA_MAF(punct=".")]})
S3.append({"id": "s2", "translation": {"en": "They said: «This she-camel drinks our water and eats from our land.»", "tr": "Dediler ki: «Bu deve suyumuzu içiyor ve toprağımızdan yiyor.»"},
 "tokens": [QALU(), ISHARA("هَذِهِ", "hadhihi", "رَفْعٍ مُبْتَدَأٌ", "raf' as mubtada", "mübtedâ", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre", extra=["mubtada-khabar"]),
  BADAL("النَّاقَةُ", "naqa", "raf"),
  MUDARI("تَشْرَبُ", "shariba", ["thulathi-mujarrad-babs", "mubtada-khabar"], who="هِيَ", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]), ENC_NOUN("مَاءَنَا", "ma-water", "نَا", "maful", punct="،"),
  MUDARI("وَتَأْكُلُ", "akala", ["thulathi-mujarrad-babs"], who="هِيَ"), MIN(), ENC_NOUN("أَرْضِنَا", "ard", "نَا", "majr", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "So nine men of them gathered together.", "tr": "Bunun üzerine onlardan dokuz adam bir araya geldi."},
 "tokens": [MADI("فَاجْتَمَعَ", "ijtamaa", ["form-viii-verbs"]),
  tok("تِسْعَةُ", "tisa", "noun", ["fail", "idafa-definiteness", "asma-al-adad-fil-kafiya"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى جَمْعٍ، وَيُخَالِفُ مَعْدُودَهُ فِي التَّأْنِيثِ.", "The doer, in raf', annexed — three to ten are annexed to a plural and take the opposite gender of the counted noun.", "Fâil, merfû; muzâf — üçten ona kadar sayılar cemie muzâf olur ve ma'dûdun cinsine muhâlif gelir."),
  MUDAF_ILAYH("رِجَالٍ", "rajul", extra=["jam-taksir", "asma-al-adad-fil-kafiya"], note_ar=" — الْمَعْدُودُ جَمْعٌ", note_en=" — the counted noun, a plural", note_tr=" — ma'dûd, cemi"), MINHUM(punct=".")]})
S3.append({"id": "s4", "translation": {"en": "And they said: «We will hamstring the she-camel at night.»", "tr": "Dediler ki: «Deveyi gece keseceğiz.»"},
 "tokens": [QALU(), MUDARI("نَعْقِرُ", "aqara", ["thulathi-mujarrad-babs"], who="نَحْنُ"), NAQA_MAF(), FI(), MAJR("اللَّيْلِ", "layl", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "Then a man from among them hamstrung the she-camel, and the deniers rejoiced.", "tr": "İçlerinden bir adam deveyi kesti; kâfirler sevindi."},
 "tokens": [MADI("فَعَقَرَ", "aqara"), FAIL("رَجُلٌ", "rajul"), JARR_PRON("مِنْهُمُ", "min", "مِنْ", "هُمُ", " («onlardan»)", note_ar="، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِرَجُلٍ", note_en="; the mim takes damma before the following ال, and the phrase qualifies «a man»", note_tr="; iki sâkin karşılaştığı için mîm damme aldı; câr-mecrûr «adam»ın na'tıdır"),
  NAQA_MAF(punct="،"), MADI("وَفَرِحَ", "fariha"), KUFFAR_F(punct=".")]})
S3.append({"id": "s6", "translation": {"en": "Salih grieved with a deep grief.", "tr": "Sâlih derin bir üzüntüyle üzüldü."},
 "tokens": [MADI("فَحَزِنَ", "hazina"), SALIH_F(),
  tok("حُزْنًا", "huzn", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ الْفِعْلِ قَبْلَهُ، يُؤَكِّدُهُ.", "The absolute object (maf'ul mutlaq), in nasb — the verb's own masdar, strengthening it.", "Mef'ûlün mutlak, mansûb — fiilin kendi masdarı; onu pekiştirir."),
  NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct=".")]})
S3.append({"id": "s7", "translation": {"en": "He said to them: «The punishment will come to you after three days.»", "tr": "Onlara dedi ki: «Azap size üç gün sonra gelecek.»"},
 "tokens": [QALA("وَقَالَ", hidden=True), LAHU("لَهُمْ", "pron-3mp", " («onlara»)", punct=":"),
  tok("سَيَأْتِيكُمُ", "ata", "verb", ["mudari-marfu", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"], "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَيَأْتِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَكُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.", "The sin marks the future; «will come» is a present verb in raf' by a damma estimated on the ya; «you» is its object, and the doer follows.", "Sîn istikbâl harfi; «gelecek» yâ üzerindeki takdîrî damme ile merfû muzâri; «kum» mef'ûlün bih; fâili ondan sonra gelir.", segments=[seg("سَ", "sa", "part"), seg("يَأْتِي", "ata", "verb"), seg("كُمُ", "pron-2mp", "pron")]),
  FAIL("الْعَذَابُ", "adhab"), ZARF("بَعْدَ", "bada", "زَمَانٍ", "time", "Zaman"),
  tok("ثَلَاثَةِ", "thalatha", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى جَمْعٍ.", "The second term of the idafa, in jarr; itself annexed — three to ten are annexed to a plural.", "Muzâfun ileyh, mecrûr; kendisi de muzâf — üçten ona kadar sayılar cemie muzâf olur."),
  MUDAF_ILAYH("أَيَّامٍ", "yawm", extra=["jam-taksir", "asma-al-adad-fil-kafiya"], note_ar=" — جَمْعُ تَكْسِيرٍ لِيَوْمٍ", note_en=" — the broken plural of «day»", note_tr=" — «gün»ün cem-i mükesseri", punct=".")]})
S3.append({"id": "s8", "translation": {"en": "The deniers laughed and said: «O Salih, where is the punishment?»", "tr": "Kâfirler güldüler ve dediler ki: «Ey Sâlih, hani azap?»"},
 "tokens": [MADI("فَضَحِكَ", "dahika"), KUFFAR_F(), QALU(), YA(), SALIH_MUNADA(punct="،"),
  tok("أَيْنَ", "ayna", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "An interrogative «where», built on fatha, in the seat of raf' as the fronted khabar.", "İstifhâm ismi «nerede», fetha üzere mebnî, öne alınmış haber olarak mahallen merfû."),
  MUBTADA("الْعَذَابُ", "adhab", note_ar=" مُؤَخَّرٌ", note_en=" (placed last)", note_tr=" (sona bırakılmış)", punct="؟")]})
S3.append({"id": "s9", "translation": {"en": "And they said: «We do not fear the punishment.»", "tr": "Ve dediler ki: «Biz azaptan korkmuyoruz.»"},
 "tokens": [QALU(), tok("نَحْنُ", "nahnu", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «we», built on damma, in the seat of raf' as mubtada.", "Munfasıl zamir «biz», damme üzere mebnî, mübtedâ olarak mahallen merfû."),
  LA_NAFIYA(), MUDARI("نَخَافُ", "khafa", ["hollow-verbs", "mubtada-khabar"], who="نَحْنُ", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]), MAFUL("الْعَذَابَ", "adhab", punct=".")]})
S3.append({"id": "s10", "translation": {"en": "And they did not turn to Allah in repentance.", "tr": "Ve Allah'a tevbe etmediler."},
 "tokens": [WA_LAM(), FIVE_JAZM("يَتُوبُوا", "taba-repent", "لَمْ", "لَمْ", "Lem", extra=["lam-jazim", "hollow-verbs"]), ILA(), ALLAH_J(punct=".")]})

# ---- Chapter 4 — الصَّيْحَةُ وَالنَّجَاةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "When the third day came, the Cry came from the sky.", "tr": "Üçüncü gün gelince gökten o korkunç ses geldi."},
 "tokens": [tok("وَلَمَّا", "lamma", "part", ["maful-fih", "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"], WA_AR + "لَمَّا ظَرْفُ زَمَانٍ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "The waw conjoins; لَمَّا «when» is an adverb of time meaning «at the time that», built on sukun in the seat of nasb, annexed to the clause after it.", "«ve» + lemmâ: «…-diği zaman» anlamında zaman zarfı, sükûn üzere mebnî, mahallen mansûb; kendisinden sonraki cümleye muzâf.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
  MADI("جَاءَ", "jaa", ["hollow-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the clause fills the seat of jarr, annexed to لَمَّا", note_tr="; cümle lemmâ'ya muzâfun ileyh olarak mahallen mecrûr"),
  FAIL("الْيَوْمُ", "yawm"), NAAT("الثَّالِثُ", "thalith", "raf", punct="،"),
  MADI("جَاءَتِ", "jaa", ["hollow-verbs"], fem=True, kasra=True), FAIL("الصَّيْحَةُ", "sayha"), MINA(), MAJR("السَّمَاءِ", "sama", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "The Cry seized the deniers in their houses.", "tr": "O ses kâfirleri evlerinde yakaladı."},
 "tokens": [MADI("فَأَخَذَتِ", "akhadha", fem=True, kasra=True), FAIL("الصَّيْحَةُ", "sayha"), MAFUL("الْكُفَّارَ", "kafir", extra=["jam-taksir"]), FI(), ENC_NOUN("بُيُوتِهِمْ", "bayt", "هِمْ", "majr", extra=["jam-taksir"], punct=".")]})
S4.append({"id": "s3", "translation": {"en": "And they all died in their homes.", "tr": "Ve hepsi yurtlarında öldüler."},
 "tokens": [VERB_WAW("فَمَاتُوا", "mata-die", ["hollow-verbs"]),
  tok("جَمِيعًا", "jamian", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — وَصَاحِبُهُ وَاوُ الْجَمَاعَةِ.", "A hal, in nasb — its owner is the waw of the group («they, all of them»).", "Hâl, mansûb — sahibi cemâat vâvıdır («hepsi birden»)."),
  FI(), ENC_NOUN("دِيَارِهِمْ", "dar", "هِمْ", "majr", extra=["jam-taksir"], note_ar=" — دِيَار جَمْعُ تَكْسِيرٍ لِدَارٍ", note_en=" — the broken plural of «home»", note_tr=" — «yurt»un cem-i mükesseri", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "Not one of them remained.", "tr": "Onlardan hiç kimse kalmadı."},
 "tokens": [WA_LAM(), tok("يَبْقَ", "baqiya", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْأَلِفِ)، وَالْفَتْحَةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا.", "Present verb in jazm by لَمْ, its sign the dropped weak letter (the alif); the fatha before it points to it.", "Lem ile meczûm muzâri; alâmeti illet harfinin (elifin) hazfi; önceki fetha ona delâlet eder."),
  MINHUM(), FAIL("أَحَدٌ", "ahad", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "And Allah saved Salih and those who believed with him.", "tr": "Allah, Sâlih'i ve onunla birlikte iman edenleri kurtardı."},
 "tokens": [MADI_ALIF("وَنَجَّى", "najja", ["form-ii-verbs"]), ALLAH_F(), MAFUL("صَالِحًا", "salih-nabi", "propn"),
  tok("وَالَّذِينَ", "alladhina", "pron", ["atf-nasaq", "ism-mawsul"], WA_AR + "الَّذِينَ اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى صَالِحًا.", "The waw conjoins; «those who» is a relative pronoun built on fatha, in the seat of nasb, joined to Salih.", "«ve» + ism-i mevsûl «…-enler», fetha üzere mebnî, Sâlih'e ma'tûf olarak mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("الَّذِينَ", "alladhina", "pron")]),
  VERB_WAW("آمَنُوا", "amana", ["form-iv-verbs", "ism-mawsul"], note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "An adverb of place «with», in nasb and annexed; the attached pronoun is its second term, in the seat of jarr.", "Mekân zarfı «ile», mansûb; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr.", punct=".", segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")])]})
S4.append({"id": "s6", "translation": {"en": "Salih left the town, grieving.", "tr": "Sâlih üzgün bir hâlde beldeden çıktı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja"), SALIH_F(), MINA(), MAJR("الْبَلَدِ", "balad"), HAL("حَزِينًا", "hazin", ["sifa-mushabbaha"], punct=".")]})
S4.append({"id": "s7", "translation": {"en": "He said: «O my people, I called you to Allah, but you did not listen.»", "tr": "Dedi ki: «Ey kavmim, sizi Allah'a çağırdım; fakat dinlemediniz.»"},
 "tokens": [QALA("وَقَالَ", hidden=True, punct=":"), YA(), QAWMI(punct="،"),
  MADI_T("دَعَوْتُكُمْ", "daa", who="ana", extra=["naqis-verbs"], enc="كُمْ"), ILA(), ALLAH_J(),
  LAM_JAZM("فَلَمْ"), FIVE_JAZM("تَسْمَعُوا", "samia", "لَمْ", "لَمْ", "Lem", extra=["lam-jazim", "thulathi-mujarrad-babs"], punct=".")]})
S4.append({"id": "s8", "translation": {"en": "Salih and the believers settled in another town.", "tr": "Sâlih ve mü'minler başka bir beldeye yerleştiler."},
 "tokens": [MADI("وَسَكَنَ", "sakana"), SALIH_F(),
  ATF("وَالْمُؤْمِنُونَ", "mumin", case="raf", extra=["jam-mudhakkar-salim", "ism-fail"], sign="مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the waw, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için vâv ile"),
  FI(), MAJR("بَلَدٍ", "balad"),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (عَلَى وَزْنِ أَفْعَلَ).", "A na't in jarr, its sign a fatha in place of the kasra — a diptote of the أَفْعَل pattern.", "Na't, mecrûr; gayr-i munsarıf (ef'al vezni) olduğu için kesre yerine fetha.", punct=".")]})
S4.append({"id": "s9", "translation": {"en": "And they used to worship Allah and did not worship the idols.", "tr": "Allah'a kulluk ediyor, putlara tapmıyorlardı."},
 "tokens": [KANU("وَكَانُوا"), MUDARI5_KH("يَعْبُدُونَ", "abada", ["thulathi-mujarrad-babs"]), ALLAH_MAF(punct="،"),
  WA_LA_NAFIYA(), MUDARI5("يَعْبُدُونَ", "abada", ["thulathi-mujarrad-babs"], role_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ", role_en="; the clause is joined to the predicate clause", role_tr="; cümle haber cümlesine ma'tûf"), ASNAM_MAF(punct=".")]})
S4.append({"id": "s10", "translation": {"en": "Thus does Allah give victory to the believers and destroy the deniers.", "tr": "İşte Allah mü'minlere böyle yardım eder ve kâfirleri böyle helâk eder."},
 "tokens": [tok("وَهٰكَذَا", "hakadha", "pron", ["asma-al-ishara", "maful-mutlaq"], WA_AR + "«هٰكَذَا» بِمَعْنَى «مِثْلَ هٰذَا»: الْكَافُ حَرْفُ جَرٍّ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ، أَيْ: نَصْرًا مِثْلَ هٰذَا.", "The waw conjoins; «thus — like this»: the kaf is a jarr letter and ذَا the demonstrative in the seat of jarr; the phrase stands in for the absolute object (a victory like this).", "«ve» + «işte böyle»: kâf cer harfi, zâ işaret ismi mahallen mecrûr; câr-mecrûr mef'ûlün mutlak yerine mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("هٰكَذَا", "hakadha", "pron")]),
  tok("يَنْصُرُ", "nasara", "verb", ["mudari-marfu", "thulathi-mujarrad-babs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.", "Present verb in raf'; the doer follows.", "Merfû muzâri; fâili ondan sonra gelir."),
  ALLAH_F(),
  tok("الْمُؤْمِنِينَ", "mumin", "noun", ["maful-bihi", "jam-mudhakkar-salim", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "The direct object, in nasb by the ya — a sound masculine plural.", "Mef'ûlün bih; cem-i müzekker sâlim olduğu için yâ ile mansûb.", punct="،"),
  MUDARI("وَيُهْلِكُ", "ahlaka", ["form-iv-verbs"], who="هُوَ", note_ar=" — مَعْطُوفَةٌ عَلَى الْجُمْلَةِ قَبْلَهَا", note_en="; joined to the clause before it", note_tr="; önceki cümleye ma'tûf"),
  tok("الْكَافِرِينَ", "kafir", "noun", ["maful-bihi", "jam-mudhakkar-salim", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "The direct object, in nasb by the ya — a sound masculine plural.", "Mef'ûlün bih; cem-i müzekker sâlim olduğu için yâ ile mansûb.", punct=".")]})

TITLES = [
 {"ar": "ثَمُودُ وَصَالِحٌ", "en": "Thamud and Salih", "tr": "Semûd ve Sâlih"},
 {"ar": "نَاقَةُ اللهِ", "en": "The She-Camel of Allah", "tr": "Allah'ın Devesi"},
 {"ar": "عَقْرُ النَّاقَةِ", "en": "The Hamstringing of the She-Camel", "tr": "Devenin Kesilmesi"},
 {"ar": "الصَّيْحَةُ وَالنَّجَاةُ", "en": "The Cry and the Rescue", "tr": "Korkunç Ses ve Kurtuluş"},
]
CHAPS = [S1, S2, S3, S4]

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule), plus the one new verb
PREF = ["nuh-wa-al-safina", "musa-fi-madyan", "musa-wal-khadir", "musa-wa-bani-israil", "musa-wa-firawn", "bad-al-amali", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
        "jumal-al-tadrib", "talkhis-al-miftah", "al-kafiya", "izhar-al-asrar", "aqaid-ahl-al-sunna", "wasiyyat-abi-hanifa", "wasiyyat-abi-yusuf-l5"]
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
 "aqara": {"lemma": "عَقَرَ", "root": "ع ق ر", "pos": "verb", "gloss": {"en": "to hamstring, to slaughter (a camel) by cutting its legs", "tr": "(deveyi) ayaklarını keserek boğazlamak, kesmek"}, "level": 2},
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
MORPH["verbs"]["aqara"] = _sg.sound1("daraba", "عَقَر", "عْقِر", "اِعْقِر", "عَقْر", "عَاقِر", maful="مَعْقُور", pmz="عُقِرَ", pmd="يُعْقَرُ",
    note="فَعَلَ يَفْعِلُ — عَقَرَ النَّاقَةَ: قَطَعَ قَوَائِمَهَا.")
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": "salih-wa-al-naqa",
 "storyGroup": "salih-wa-al-naqa",
 "title": {"ar": "صَالِحٌ وَالنَّاقَةُ", "en": "Salih and the She-Camel", "tr": "Sâlih ve Deve"},
 "subtitle": {"ar": "قِصَّةُ صَالِحٍ وَثَمُودَ لِلْمُبْتَدِئِينَ — الدَّعْوَةُ، وَالنَّاقَةُ، وَالصَّيْحَةُ",
              "en": "The story of Salih and Thamud, for beginners — the call, the she-camel, the Cry",
              "tr": "Yeni başlayanlar için Sâlih ve Semûd kıssası — davet, deve, korkunç ses"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-07",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِقِصَّةِ صَالِحٍ عَلَيْهِ السَّلَامُ وَقَوْمِهِ ثَمُودَ كَمَا تُرْوَى لِلْأَطْفَالِ (عَلَى ضَوْءِ سُورَةِ الْأَعْرَافِ ٧٣–٧٩، وَهُودٍ ٦١–٦٨، وَالشُّعَرَاءِ ١٤١–١٥٩، وَالشَّمْسِ ١١–١٥)، عَلَى طَرِيقَةِ الْقِرَاءَةِ الْمُتَدَرِّجَةِ لِلنَّدْوِيِّ. لَمْ تُنْقَلْ آيَةٌ بِنَصِّهَا، وَلَا يُسْتَشْهَدُ بِجُمْلَةٍ هُنَا عَلَى أَنَّهَا نَصٌّ تُرَاثِيٌّ. كُتِبَتْ لِلْفِعْلِ الْمُؤَنَّثِ وَفَاعِلِهِ، وَلَا النَّاهِيَةِ مَعَ الْأَفْعَالِ الْخَمْسَةِ، وَالْبَدَلِ بَعْدَ اسْمِ الْإِشَارَةِ، وَالْعَدَدِ مَعَ مَعْدُودِهِ، وَالْمَفْعُولِ الْمُطْلَقِ، وَالْمَمْنُوعِ مِنَ الصَّرْفِ، وَالْمُضَارِعِ النَّاقِصِ الْمَجْزُومِ.",
  "en": "ORIGINAL Level-1 graded Arabic: the story of Salih (peace be upon him) and his people Thamud as it is told to children (after the Qurʾānic narrative in al-Aʿrāf 73–79, Hūd 61–68, al-Shuʿarāʾ 141–159 and al-Shams 11–15), composed editorially in the manner of Nadwī's graded readers — short كَانَ-framed sentences, one event per line, the vocabulary repeated. No āya is quoted verbatim; no sentence here may be cited as a classical text. Written to meet the feminine verb and its doer, the prohibitive لَا on the five verbs, the badal after a demonstrative, the number with its counted noun, the absolute object, the diptote, and the jussive of a weak-ending verb.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Sâlih aleyhisselâm ile kavmi Semûd'un kıssasının çocuklara anlatıldığı şekli (A'râf 73–79, Hûd 61–68, Şuarâ 141–159 ve Şems 11–15'teki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde telif edilmiştir — kısa, kâne ile kurulu cümleler, her satırda bir olay, tekrar eden kelime hazinesi. Hiçbir âyet aynen aktarılmamıştır; buradaki hiçbir cümle klasik bir metin olarak kaynak gösterilemez. Müennes fiil ve fâili, ef'âl-i hamse üzerinde nehiy lâ'sı, işaret isminden sonra bedel, sayı ve ma'dûdu, mef'ûlün mutlak, gayr-i munsarıf ve nâkıs muzârinin cezmi için yazıldı.",
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
