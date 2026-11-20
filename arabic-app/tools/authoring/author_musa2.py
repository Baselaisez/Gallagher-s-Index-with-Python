# -*- coding: utf-8 -*-
"""Author content/samples/musa-wa-bani-israil — «مُوسَى وَبَنُو إِسْرَائِيلَ», the ORIGINAL Level-1 sequel to the Mūsā story (wave 85).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Mūsā (al-Qaṣaṣ, Ṭāhā,
al-Shuʿarāʾ, al-Baqara) as it is commonly retold to children. No āya is quoted; no sentence here may be cited as
a classical text. Six chapters, sixty-three sentences. Every token carries trilingual iʿrāb. Verb paradigms and
glossary entries are COPIED from the packages that already own the lemma (the lemma-identity rule); only هَارُون, السَّامِرِيّ, أَرْبَعُونَ, تَوْبَة and the interrogative مَا are
new to the corpus (عَبَدَ and قَبِلَ are copied from the Qiṣaṣ — the lemma-identity rule).

    QISSA_PKG_ROOT=<dir> python3 author_musa2.py     # a dry run writes under <dir>/musa-wa-bani-israil
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "musa-wa-bani-israil"
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

# ============ «مُوسَى وَبَنُو إِسْرَائِيلَ» — the sequel: four chapters ============
MUSA_F = lambda punct=None: FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0], punct=punct)
ALLAH_F = lambda punct=None: FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl", punct=punct)
HARUN_F = lambda punct=None: FAIL("هَارُونُ", "harun", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], punct=punct)
NAS_F = lambda punct=None: FAIL("النَّاسُ", "nas", punct=punct)
QALA = lambda full="وَقَالَ", hidden=False, punct=None: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür", punct=punct)
def LI_AL(full, lex, gloss_tr, punct=None):
    """لِلنَّاسِ، لِلْقَوْمِ: the lam fused to the article"""
    return PREP(full, "li", gloss_tr=gloss_tr, segments=[seg("لِ", "li", "prep"), seg(full[1:], lex, "noun")], punct=punct)
def BANU_F(): return FAIL("بَنُو", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak, vâv ile merfû; nûnu izâfet için düşmüş, muzâf", sign="بِالْوَاوِ")
def ISRAIL(punct=None): return MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct=punct)
HAL5 = lambda full, lex, extra=None, punct=None: tok(full, lex, "verb", ["afal-khamsa", "hal"] + (extra or []),
    "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "One of the five verbs, in raf' by the kept nun; the waw is its doer — the clause is a hal (circumstantial), in the seat of nasb.",
    "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâildir — cümle hâl olarak mahallen mansûbdur.", punct=punct)
def LAHU(full, pron, pron_tr, punct=None, grammar=None):
    """لَهُ، لَهُمْ: the lam of jarr with its pronoun"""
    return tok(full, "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"] + (grammar or []),
        "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "The lam is a jarr letter; the attached pronoun fills the seat of jarr.", "Lâm cer harfi; bitişik zamir mahallen mecrûr" + pron_tr + ".",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg(full[1:], pron, "pron")])
def ALAYHIM(punct=None):
    return tok("عَلَيْهِمْ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "عَلَى حَرْفُ جَرٍّ، وَهُمْ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "عَلَى is a jarr letter; «them» fills the seat of jarr.", "«Alâ» cer harfi; «onlar» zamiri mahallen mecrûr.", punct=punct, segments=[seg("عَلَيْ", "ala", "prep"), seg("هِمْ", "pron-3mp", "pron")])

# ---- Chapter 1 — الْعِجْلُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Musa went to the mountain for forty nights.", "tr": "Mûsâ kırk gece dağa gitti."},
 "tokens": [
  MADI("ذَهَبَ", "dhahaba"), MUSA_F(), PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("الْجَبَلِ", "jabal"),
  tok("أَرْبَعِينَ", "arbaun", "noun", ["maful-fih", "jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "A time adverb (maf'ul fih), in nasb by the ya: the tens decline like the sound masculine plural.", "Zaman zarfı (mef'ûlün fîh), yâ ile mansûb: onluk sayılar cem-i müzekker sâlim gibi i'râb alır."),
  tok("لَيْلَةً", "layla", "noun", ["tamyiz", "asma-al-adad-fil-kafiya"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — تَمْيِيزُ الْعَدَدِ مِنْ أَحَدَ عَشَرَ إِلَى تِسْعَةٍ وَتِسْعِينَ مُفْرَدٌ مَنْصُوبٌ.", "A tamyiz (specifier) in nasb: the counted noun after eleven to ninety-nine is singular and mansub.", "Temyîz, mansûb: on birden doksan dokuza kadar sayıların temyîzi tekil ve mansûbdur.", punct="."),
 ]})
S1.append({"id": "s2", "translation": {"en": "And Harun was with the people.", "tr": "Ve Hârûn insanlarla birlikteydi."},
 "tokens": [
  KANA("وَكَانَ"), ISMK("هَارُونُ", "harun", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ خَبَرُ كَانَ.", "A place adverb «with», in nasb and annexed — the adverb phrase is the predicate of كَانَ.", "Mekân zarfı «ile birlikte», mansûb ve muzâf — zarf, kâne'nin haberidir."),
  MUDAF_ILAYH("النَّاسِ", "nas", punct="."),
 ]})
S1.append({"id": "s3", "translation": {"en": "And among the people there was a man whose name was al-Samiri.", "tr": "Ve kavmin içinde adı Sâmirî olan bir adam vardı."},
 "tokens": [
  KANA("وَكَانَ"), PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"), MAJR("الْقَوْمِ", "qawm"), ISMK("رَجُلٌ", "rajul", muakhkhar=True),
  tok("اسْمُهُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil", "naat-sifa"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِرَجُلٍ.", "A mubtada in raf', annexed to «his» — the whole clause is an adjective (na't) of «a man».", "Mübtedâ, merfû; «onun» zamirine muzâf — cümle, «bir adam»ın sıfatı olarak mahallen merfûdur.", segments=[seg("اسْمُ", "ism", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("السَّامِرِيُّ", "samiri", "propn", ["mubtada-khabar", "al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمٌ مَنْسُوبٌ.", "The khabar, in raf' — a nisba name.", "Haber, merfû — nisbet ismi.", punct="."),
 ]})
S1.append({"id": "s4", "translation": {"en": "So al-Samiri made a calf of gold.", "tr": "Bunun üzerine Sâmirî altından bir buzağı yaptı."},
 "tokens": [
  MADI("فَصَنَعَ", "sanaa"), FAIL("السَّامِرِيُّ", "samiri", "propn", ["al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"]), MAFUL("عِجْلًا", "ijl"),
  PREP("مِنْ", "min", "، وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِعِجْلًا", "; the jarr phrase describes the calf (a na't)", "; câr-mecrûr, «buzağı»nın sıfatıdır", gloss_tr="«-den»"),
  MAJR("ذَهَبٍ", "dhahab-gold", punct="."),
 ]})
S1.append({"id": "s5", "translation": {"en": "And he said to the people: «This is your lord.»", "tr": "Ve insanlara «İşte rabbiniz budur» dedi."},
 "tokens": [
  QALA("وَقَالَ", hidden=True), LI_AL("لِلنَّاسِ", "nas", "«insanlara»", punct=":"),
  tok("هَذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A demonstrative, built; it fills the mubtada's seat in raf'.", "İşaret ismi, mebnî; mübtedâ olarak mahallen merfû."),
  tok("رَبُّكُمْ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "The khabar in raf', annexed to «your».", "Haber, merfû; «sizin» zamirine muzâf.", punct=".", segments=[seg("رَبُّ", "rabb", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
 ]})
S1.append({"id": "s6", "translation": {"en": "So the people worshipped the calf.", "tr": "Bunun üzerine insanlar buzağıya taptı."},
 "tokens": [MADI("فَعَبَدَ", "abada"), NAS_F(), MAFUL("الْعِجْلَ", "ijl", punct=".")]})
S1.append({"id": "s7", "translation": {"en": "And Harun said to them: «Do not worship the calf!»", "tr": "Ve Hârûn onlara «Buzağıya tapmayın!» dedi."},
 "tokens": [
  QALA("وَقَالَ"), LAHU("لَهُمْ", "pron-3mp", " («onlara»)"), HARUN_F(punct=":"),
  tok("لَا", "la-nahiya", "part", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "لَا النَّاهِيَةُ، حَرْفُ نَهْيٍ وَجَزْمٍ.", "The prohibitive لَا: it forbids and puts the verb in jazm.", "Lâ-yı nâhiye: nehiy ve cezm harfi."),
  tok("تَعْبُدُوا", "abada", "verb", ["afal-khamsa", "nawasib-wa-jawazim-al-mudari", "la-nahiya"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ.", "Present verb in jazm after لَا; the sign of its jazm is the dropped nun (one of the five verbs); the waw is its doer.", "Lâ ile meczûm muzâri; cezm alâmeti nûnun düşmesidir (ef'âl-i hamseden); vâv fâildir."),
  MAFUL("الْعِجْلَ", "ijl", punct="!"),
 ]})
S1.append({"id": "s8", "translation": {"en": "But the people did not listen to Harun's words.", "tr": "Fakat insanlar Hârûn'un sözünü dinlemediler."},
 "tokens": [
  tok("فَمَا", "ma-nafiya", "part", ["atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; مَا negates the past verb and governs nothing.", "Fâ atıf harfi; mâ nâfiye, amel etmez.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  MADI("سَمِعَ", "samia"), NAS_F(),
  MAFUL("كَلَامَ", "kalam", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("هَارُونَ", "harun", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})

# ---- Chapter 2 — غَضَبُ مُوسَى ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "And Musa returned from the mountain.", "tr": "Ve Mûsâ dağdan döndü."},
 "tokens": [MADI("وَرَجَعَ", "rajaa"), MUSA_F(), tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter, voweled with fatha before the following ال.", "Cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."), MAJR("الْجَبَلِ", "jabal", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "And he saw the calf, and he saw the people bowing down to it.", "tr": "Buzağıyı gördü; insanları ona secde ederken gördü."},
 "tokens": [
  tok("فَرَأَى", "raa", "verb", ["naqis-verbs", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَرَأَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "The fa conjoins; a past verb with the fatha estimated on its alif; the doer is a hidden «he».", "Fâ atıf harfi; mâzî fiil, fetha elif üzerinde takdîrî; fâil gizli «o».", segments=[seg("فَ", "fa", "conj"), seg("رَأَى", "raa", "verb")]),
  MAFUL("الْعِجْلَ", "ijl", punct="،"),
  tok("وَرَأَى", "raa", "verb", ["naqis-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَرَأَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "The waw conjoins; a past verb with the fatha estimated on its alif; the doer is a hidden «he».", "Vâv atıf harfi; mâzî fiil, fetha elif üzerinde takdîrî; fâil gizli «o».", segments=[seg("وَ", "wa", "conj"), seg("رَأَى", "raa", "verb")]),
  MAFUL("النَّاسَ", "nas"), HAL5("يَسْجُدُونَ", "sajada"), LAHU("لَهُ", "pron-3ms", " («ona»)", punct="."),
 ]})
S2.append({"id": "s3", "translation": {"en": "So Musa grew very angry.", "tr": "Bunun üzerine Mûsâ şiddetle öfkelendi."},
 "tokens": [
  MADI("فَغَضِبَ", "ghadiba"), MUSA_F(),
  tok("غَضَبًا", "ghadab", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ غَضِبَ.", "A maf'ul mutlaq (the verb's own masdar), in nasb.", "Mef'ûlün mutlak (fiilin kendi masdarı), mansûb."),
  NAAT("شَدِيدًا", "shadid", "nasb", punct="."),
 ]})
S2.append({"id": "s4", "translation": {"en": "And he said to the people: «What is this calf?»", "tr": "Ve insanlara «Bu buzağı nedir?» dedi."},
 "tokens": [
  QALA("وَقَالَ", hidden=True), LI_AL("لِلنَّاسِ", "nas", "«insanlara»", punct=":"),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "مَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "Interrogative مَا «what», built; it fills the mubtada's seat.", "İstifhâm ismi «ne», mebnî; mübtedâ olarak mahallen merfû."),
  tok("هَذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "A demonstrative, built; it fills the khabar's seat.", "İşaret ismi, mebnî; haber olarak mahallen merfû."),
  tok("الْعِجْلُ", "ijl", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "A badal (the noun explaining the demonstrative), in raf'.", "İşaret isminden bedel, merfû.", punct="؟"),
 ]})
S2.append({"id": "s5", "translation": {"en": "Then Musa burned the calf.", "tr": "Sonra Mûsâ buzağıyı yaktı."},
 "tokens": [tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."), MADI("حَرَّقَ", "harraqa", ["form-ii-verbs"]), MUSA_F(), MAFUL("الْعِجْلَ", "ijl", punct=".")]})
S2.append({"id": "s6", "translation": {"en": "And the people repented to God.", "tr": "Ve insanlar Allah'a tövbe ettiler."},
 "tokens": [MADI("وَتَابَ", "taba-repent", ["hollow-verbs"]), NAS_F(), PREP("إِلَى", "ila", gloss_tr="«-e»"), MAJR("اللهِ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl", punct=".")]})
S2.append({"id": "s7", "translation": {"en": "So God accepted their repentance.", "tr": "Bunun üzerine Allah tövbelerini kabul etti."},
 "tokens": [MADI("فَقَبِلَ", "qabila"), ALLAH_F(),
  tok("تَوْبَتَهُمْ", "tawba", "noun", ["maful-bihi", "idafa-definiteness", "al-bariz-al-muttasil"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "The direct object, in nasb; annexed to «their».", "Mef'ûlün bih, mansûb; «onların» zamirine muzâf.", punct=".", segments=[seg("تَوْبَتَ", "tawba", "noun"), seg("هُمْ", "pron-3mp", "pron")])]})

# ---- Chapter 3 — فِي الصَّحْرَاءِ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "And the Children of Israel walked in the desert for forty years.", "tr": "Ve İsrailoğulları çölde kırk yıl yürüdüler."},
 "tokens": [
  tok("وَمَشَى", "masha", "verb", ["naqis-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَشَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "The waw conjoins; a past verb with the fatha estimated on its alif.", "Vâv atıf harfi; mâzî fiil, fetha elif üzerinde takdîrî.", segments=[seg("وَ", "wa", "conj"), seg("مَشَى", "masha", "verb")]),
  BANU_F(), ISRAIL(), PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الصَّحْرَاءِ", "sahra"),
  tok("أَرْبَعِينَ", "arbaun", "noun", ["maful-fih", "jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "A time adverb (maf'ul fih), in nasb by the ya: the tens decline like the sound masculine plural.", "Zaman zarfı (mef'ûlün fîh), yâ ile mansûb: onluk sayılar cem-i müzekker sâlim gibi i'râb alır."),
  tok("سَنَةً", "sana", "noun", ["tamyiz", "asma-al-adad-fil-kafiya"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "A tamyiz (the counted noun), in nasb.", "Temyîz, mansûb.", punct="."),
 ]})
S3.append({"id": "s2", "translation": {"en": "And the desert was hot.", "tr": "Ve çöl sıcaktı."},
 "tokens": [KANA("وَكَانَتِ", fem=True), ISMK("الصَّحْرَاءُ", "sahra"), KHK("حَارَّةً", "harr-hot", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "So God put a cloud above them.", "tr": "Bunun üzerine Allah üzerlerine bir bulut koydu."},
 "tokens": [MADI("فَجَعَلَ", "jaala"), ALLAH_F(),
  tok("فَوْقَهُمْ", "fawqa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "A place adverb «above», in nasb; annexed to «them».", "Mekân zarfı «üstünde», mansûb; «onlar» zamirine muzâf.", segments=[seg("فَوْقَ", "fawqa", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  MAFUL("سَحَابًا", "sahab", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "And God sent down upon them food from the sky.", "tr": "Ve Allah onlara gökten yiyecek indirdi."},
 "tokens": [MADI("وَأَنْزَلَ", "anzala", ["form-iv-verbs"]), ALLAH_F(), ALAYHIM(), MAFUL("طَعَامًا", "taam"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter, voweled with fatha before the following ال.", "Cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("السَّمَاءِ", "sama", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "And the food was good.", "tr": "Ve yiyecek güzeldi."},
 "tokens": [KANA("وَكَانَ"), ISMK("الطَّعَامُ", "taam"), KHK("طَيِّبًا", "tayyib-good", punct=".")]})
S3.append({"id": "s6", "translation": {"en": "But the people said: «We want another food.»", "tr": "Fakat insanlar «Biz başka bir yiyecek istiyoruz» dediler."},
 "tokens": [QALA("فَقَالَ"), NAS_F(punct=":"),
  tok("نَحْنُ", "nahnu", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun, built; it fills the mubtada's seat.", "Munfasıl zamir, mebnî; mübtedâ olarak mahallen merfû."),
  tok("نُرِيدُ", "arada", "verb", ["form-iv-verbs", "hollow-verbs", "mudari-marfu", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "Present verb in raf'; its doer is necessarily hidden (we) — the clause is the khabar.", "Merfû muzâri; fâili vücûben gizli (biz) — cümle haberdir."),
  MAFUL("طَعَامًا", "taam"),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "An adjective (na't) in nasb — a diptote.", "Na't, mansûb — gayr-i munsarif.", punct=".")]})
S3.append({"id": "s7", "translation": {"en": "So Musa said: «Enter the city.»", "tr": "Bunun üzerine Mûsâ «Şehre girin» dedi."},
 "tokens": [QALA("فَقَالَ"), MUSA_F(punct=":"),
  tok("ادْخُلُوا", "dakhala", "verb", ["imperative-amr", "afal-khamsa"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "An imperative, built on the dropped nun; the waw is its doer.", "Emir fiili, nûnun düşmesi üzere mebnî; vâv fâildir."),
  MAFUL("الْمَدِينَةَ", "madina", punct=".")]})

# ---- Chapter 4 — الْأَرْضُ الْمُقَدَّسَةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "And Musa said to his people: «Enter the holy land.»", "tr": "Ve Mûsâ kavmine «Kutsal toprağa girin» dedi."},
 "tokens": [QALA("وَقَالَ"), MUSA_F(),
  tok("لِقَوْمِهِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The lam is a jarr letter; «people» is in jarr, annexed to «his».", "Lâm cer harfi; «kavim» mecrûr, «onun» zamirine muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("ادْخُلُوا", "dakhala", "verb", ["imperative-amr", "afal-khamsa"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "An imperative, built on the dropped nun; the waw is its doer.", "Emir fiili, nûnun düşmesi üzere mebnî; vâv fâildir."),
  MAFUL("الْأَرْضَ", "ard"), NAAT("الْمُقَدَّسَةَ", "muqaddas", "nasb", ["ism-maful"], punct=".")]})
S4.append({"id": "s2", "translation": {"en": "But the people said: «In this land there are strong people.»", "tr": "Fakat kavim «Bu toprakta güçlü bir kavim var» dedi."},
 "tokens": [QALA("فَقَالَ"), FAIL("الْقَوْمُ", "qawm", punct=":"),
  PREP("فِي", "fi", "، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", "; the jarr phrase is the fronted khabar", "; câr-mecrûr, öne alınmış haberdir", gloss_tr="«-de»"),
  tok("هَذِهِ", "hadhihi", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "A demonstrative, built; it fills the seat of jarr.", "İşaret ismi, mebnî; mahallen mecrûr."),
  tok("الْأَرْضِ", "ard", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A badal (the noun explaining the demonstrative), in jarr.", "İşaret isminden bedel, mecrûr."),
  tok("قَوْمٌ", "qawm", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The mubtada, placed after its khabar, in raf'.", "Sonraya bırakılmış mübtedâ, merfû."),
  NAAT("أَقْوِيَاءُ", "qawi", "raf", ["mamnu-min-sarf"], " — جَمْعُ قَوِيٍّ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ", " — the plural of قَوِيّ on فُعَلَاء, a diptote", " — kavî'nin fuʿalâ' vezninde çoğulu, gayr-i munsarif", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "«And we will not enter it.»", "tr": "«Ve biz oraya girmeyiz.»"},
 "tokens": [
  tok("وَنَحْنُ", "nahnu", "pron", ["mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَنَحْنُ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; a detached pronoun fills the mubtada's seat.", "Vâv atıf harfi; munfasıl zamir mübtedâ olarak mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("نَحْنُ", "nahnu", "pron")]),
  tok("لَا", "la-nafiya", "part", [], "لَا النَّافِيَةُ، لَا عَمَلَ لَهَا.", "Negating لَا; it governs nothing.", "Lâ-yı nâfiye; amel etmez."),
  tok("نَدْخُلُهَا", "dakhala", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "Present verb in raf'; the doer is a hidden «we»; the attached «it» is the object — the clause is the khabar.", "Merfû muzâri; fâili vücûben gizli «biz»; bitişik «onu» mef'ûldür — cümle haberdir.", punct=".", segments=[seg("نَدْخُلُ", "dakhala", "verb"), seg("هَا", "pron-3fs", "pron")])]})
S4.append({"id": "s4", "translation": {"en": "So God was angry with them.", "tr": "Bunun üzerine Allah onlara gazap etti."},
 "tokens": [MADI("فَغَضِبَ", "ghadiba"), ALLAH_F(), ALAYHIM(punct=".")]})
S4.append({"id": "s5", "translation": {"en": "And Harun died in the desert; then Musa died.", "tr": "Ve Hârûn çölde öldü; sonra Mûsâ öldü."},
 "tokens": [MADI("وَمَاتَ", "mata-die", ["hollow-verbs"]), HARUN_F(), PREP("فِي", "fi", gloss_tr="«-de»"), MAJR("الصَّحْرَاءِ", "sahra", punct="،"),
  tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertîb ve terâhî bildiren atıf harfi."),
  MADI("مَاتَ", "mata-die", ["hollow-verbs"]), MUSA_F(punct=".")]})
S4.append({"id": "s6", "translation": {"en": "And Yusha was a prophet after Musa.", "tr": "Ve Mûsâ'dan sonra Yûşa peygamber idi."},
 "tokens": [KANA("وَكَانَ"), ISMK("يُوشَعُ", "yusha", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]), KHK("نَبِيًّا", "nabi"),
  tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "A time adverb «after», in nasb and annexed.", "Zaman zarfı «sonra», mansûb ve muzâf."),
  MUDAF_ILAYH("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "بِكَسْرَةٍ " + MUQ_ALIF[0], "", MUQ_ALIF[1], MUQ_ALIF[2], punct=".")]})
S4.append({"id": "s7", "translation": {"en": "Then the Children of Israel entered the holy land.", "tr": "Sonra İsrailoğulları kutsal toprağa girdiler."},
 "tokens": [MADI("فَدَخَلَ", "dakhala"), BANU_F(), ISRAIL(), MAFUL("الْأَرْضَ", "ard"), NAAT("الْمُقَدَّسَةَ", "muqaddas", "nasb", ["ism-maful"], punct=".")]})

TITLES = [
 {"ar": "الْعِجْلُ", "en": "The Calf", "tr": "Buzağı"},
 {"ar": "غَضَبُ مُوسَى", "en": "The Anger of Musa", "tr": "Mûsâ'nın Öfkesi"},
 {"ar": "فِي الصَّحْرَاءِ", "en": "In the Desert", "tr": "Çölde"},
 {"ar": "الْأَرْضُ الْمُقَدَّسَةُ", "en": "The Holy Land", "tr": "Kutsal Toprak"},
]
CHAPS = [S1, S2, S3, S4]

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule), plus the three new words
PREF = ["musa-wa-firawn", "bad-al-amali", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
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
 "harun": {"lemma": "هَارُون", "pos": "propn", "gloss": {"en": "Harun (Aaron), the brother of Musa — a diptote (foreign name)", "tr": "Hârûn, Mûsâ'nın kardeşi — gayr-i munsarıf (yabancı alem)"}, "level": 1},
 "samiri": {"lemma": "السَّامِرِيّ", "pos": "propn", "gloss": {"en": "al-Samiri, the man who made the calf (a nisba name)", "tr": "Sâmirî, buzağıyı yapan adam (nisbet ismi)"}, "level": 2},
 "arbaun": {"lemma": "أَرْبَعُونَ", "root": "ر ب ع", "pos": "noun", "gloss": {"en": "forty (declines by letters like the sound masculine plural: أَرْبَعِينَ in nasb and jarr)", "tr": "kırk (cem-i müzekker sâlim gibi harflerle i'râb alır: nasb ve cerde أَرْبَعِينَ)"}, "level": 1},
 "tawba": {"lemma": "تَوْبَة", "root": "ت و ب", "pos": "noun", "gloss": {"en": "repentance (the masdar of تَابَ)", "tr": "tövbe (tâbe'nin masdarı)"}, "level": 1},
 "ma-istifham": {"lemma": "مَا", "pos": "pron", "gloss": {"en": "what? (the interrogative مَا)", "tr": "ne? (istifhâm mâ'sı)"}, "level": 0},
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
 "id": "musa-wa-bani-israil",
 "storyGroup": "musa-wa-firawn",
 "title": {"ar": "مُوسَى وَبَنُو إِسْرَائِيلَ", "en": "Musa and the Children of Israel", "tr": "Mûsâ ve İsrailoğulları"},
 "subtitle": {"ar": "تَتِمَّةُ قِصَّةِ مُوسَى لِلْمُبْتَدِئِينَ — الْعِجْلُ، وَالصَّحْرَاءُ، وَالْأَرْضُ الْمُقَدَّسَةُ",
              "en": "The story of Musa continued, for beginners — the calf, the desert, the holy land",
              "tr": "Yeni başlayanlar için Mûsâ kıssasının devamı — buzağı, çöl, kutsal toprak"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-06",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": ["musa-wa-firawn"],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِتَتِمَّةِ قِصَّةِ مُوسَى كَمَا تُرْوَى لِلْأَطْفَالِ، عَلَى طَرِيقَةِ «قِصَصِ النَّبِيِّينَ» — لَيْسَ فِيهَا آيَةٌ مَنْقُولَةٌ، وَلَيْسَتْ نَصًّا تُرَاثِيًّا.",
  "en": "ORIGINAL Level-1 graded Arabic: the story of Musa continued as it is told to children (after the Qurʾānic narrative in al-Baqara, al-Aʿrāf, Ṭāhā and al-Māʾida), composed editorially in the manner of Nadwī's graded readers. No āya is quoted; nothing here is a classical text.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Mûsâ kıssasının çocuklara anlatıldığı şekliyle devamı (Bakara, A'râf, Tâhâ ve Mâide sûrelerindeki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde telif edilmiştir. Hiçbir âyet aktarılmamıştır; hiçbir cümle klasik bir metin değildir.",
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
