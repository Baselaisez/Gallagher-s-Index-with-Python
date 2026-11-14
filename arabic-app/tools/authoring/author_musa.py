# -*- coding: utf-8 -*-
"""Author content/samples/musa-wa-firawn — «مُوسَى وَفِرْعَوْنُ», an ORIGINAL Level-1 retelling (wave 82).

ORIGINAL graded Arabic, composed editorially in the manner of Nadwī's graded reader (short كَانَ-framed sentences,
one event per line, the vocabulary repeated until it is owned) from the Qurʾānic story of Mūsā (al-Qaṣaṣ, Ṭāhā,
al-Shuʿarāʾ, al-Baqara) as it is commonly retold to children. No āya is quoted; no sentence here may be cited as
a classical text. Six chapters, sixty-three sentences. Every token carries trilingual iʿrāb. Verb paradigms and
glossary entries are COPIED from the packages that already own the lemma (the lemma-identity rule); only كَبِرَ,
الصُّنْدُوق and النِّيل are new to the corpus.

    QISSA_PKG_ROOT=<dir> python3 author_musa.py      # a dry run writes under <dir>/musa-wa-firawn
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "musa-wa-firawn"
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

# ============ Chapter 1 — Pharaoh and the Children of Israel ============
S1 = []
S1.append({"id": "s1", "translation": {"en": "There was in Egypt an unjust king.", "tr": "Mısır'da zalim bir kral vardı."},
 "tokens": [
  KANA(),
  PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], DIPT_F[0], DIPT_F[1], DIPT_F[2], sign=FATHA_JARR),
  ISMK("مَلِكٌ", "malik-king", muakhkhar=True),
  NAAT("ظَالِمٌ", "zalim", "raf", ["ism-fail"], "", " — the ism fa'il of ظَلَمَ", " — zaleme'nin ism-i fâili", punct="."),
 ]})
S1.append({"id": "s2", "translation": {"en": "And the name of this king was Pharaoh.", "tr": "Ve bu kralın adı Firavun idi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("اسْمُ", "ism", note_ar="، مُضَافٌ", note_en=", the first term of an idafa", note_tr=", muzâf"),
  tok("هَذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A demonstrative, built; it fills the seat of the mudaf ilayh in jarr.", "İsm-i işâret, mebnî; mahallen mecrûr, muzâfun ileyh."),
  tok("الْمَلِكِ", "malik-king", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A badal (the noun explaining the demonstrative), in jarr.", "İsm-i işâretten bedel, mecrûr."),
  KHK("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S1.append({"id": "s3", "translation": {"en": "And Pharaoh used to say: «I am your lord.»", "tr": "Ve Firavun «Ben sizin rabbinizim» derdi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  MUDARI_KH("يَقُولُ", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür", punct=":"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun, built; it fills the mubtada's seat in raf'.", "Munfasıl zamir, mebnî; mahallen merfû mübtedâ."),
  tok("رَبُّكُمْ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "The khabar in raf', annexed to the attached pronoun «your».", "Haber, merfû; «sizin» zamirine muzâf.", punct=".", segments=[seg("رَبُّ", "rabb", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
 ]})
S1.append({"id": "s4", "translation": {"en": "And the people were afraid of Pharaoh.", "tr": "Ve insanlar Firavun'dan korkardı."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("النَّاسُ", "nas"),
  MUDARI5_KH("يَخَافُونَ", "khafa", ["hollow-verbs"]),
  PREP("مِنْ", "min", gloss_tr="«-den»"),
  MAJR("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], sign=FATHA_JARR, punct="."),
 ]})
S1.append({"id": "s5", "translation": {"en": "And there was in Egypt a weak people.", "tr": "Ve Mısır'da zayıf bir kavim vardı."},
 "tokens": [
  KANA("وَكَانَ"),
  PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], DIPT_F[0], DIPT_F[1], DIPT_F[2], sign=FATHA_JARR),
  ISMK("قَوْمٌ", "qawm", muakhkhar=True),
  NAAT("ضُعَفَاءُ", "daif", "raf", ["jam-taksir", "mamnu-min-sarf"], " — جَمْعُ ضَعِيفٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ", " — the broken plural of ضَعِيف on فُعَلَاء, barred from tanwin", " — zaîf'in fu'alâ' veznindeki cem'i, gayr-i munsarif", punct="."),
 ]})
S1.append({"id": "s6", "translation": {"en": "And the name of this people was «the Children of Israel».", "tr": "Ve bu kavmin adı «İsrailoğulları» idi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("اسْمُ", "ism", note_ar="، مُضَافٌ", note_en=", the first term of an idafa", note_tr=", muzâf"),
  tok("هَؤُلَاءِ", "haulai", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A demonstrative (plural), built; it fills the seat of the mudaf ilayh in jarr.", "İsm-i işâret (çoğul), mebnî; mahallen mecrûr, muzâfun ileyh."),
  tok("الْقَوْمِ", "qawm", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A badal of the demonstrative, in jarr.", "İsm-i işâretten bedel, mecrûr."),
  KHK("بَنِي", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], note_ar=" — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", note_en=" — attached to the sound masculine plural; its nun is dropped for the idafa", note_tr=" — cem-i müzekker sâlime mülhak; izâfet için nûnu düşmüş, muzâf", sign="بِالْيَاءِ"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S1.append({"id": "s7", "translation": {"en": "And Pharaoh used to oppress the Children of Israel.", "tr": "Ve Firavun İsrailoğullarına zulmederdi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  MUDARI_KH("يَظْلِمُ", "zalama"),
  MAFUL("بَنِي", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak; izâfet için nûnu düşmüş, muzâf", sign="بِالْيَاءِ"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S1.append({"id": "s8", "translation": {"en": "And he used to kill their sons.", "tr": "Ve onların oğullarını öldürürdü."},
 "tokens": [
  KANA("وَكَانَ", ),
  tok("يَقْتُلُ", "qatala", "verb", ["kana-wa-akhawatuha", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَاسْمُ كَانَ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُهَا.", "Present verb in raf' with a hidden doer; كَانَ's own noun is a hidden pronoun (he), and this clause is its predicate.", "Merfû muzâri, fâili gizli; kâne'nin ismi de gizli zamirdir (o), bu cümle onun haberidir."),
  MAFUL("أَوْلَادَهُمْ", "walad", "noun", ["jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ وَلَدٍ", ", annexed to «their» — the broken plural of وَلَد", ", «onların» zamirine muzâf — veled'in cem'i", punct=".", segments=[seg("أَوْلَادَ", "walad", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
 ]})
S1.append({"id": "s9", "translation": {"en": "And the Children of Israel used to weep and call upon God.", "tr": "Ve İsrailoğulları ağlar ve Allah'a dua ederlerdi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("بَنُو", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak, vâv ile merfû; izâfet için nûnu düşmüş, muzâf", sign="بِالْوَاوِ"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2]),
  MUDARI5_KH("يَبْكُونَ", "baka", ["naqis-verbs"]),
  tok("وَيَدْعُونَ", "daa", "verb", ["afal-khamsa", "atf-nasaq", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَدْعُونَ فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَعْطُوفٌ عَلَى يَبْكُونَ.", "The waw conjoins; one of the five verbs in raf' by the kept nun, the waw its doer — conjoined to «weep».", "«ve» + «dua ederler» — ef'âl-i hamseden, nûnun sübûtuyla merfû; «ağlarlar»a ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("يَدْعُونَ", "daa", "verb")]),
  MAFUL("اللهَ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl", punct="."),
 ]})
S1.append({"id": "s10", "translation": {"en": "And God heard their prayer.", "tr": "Ve Allah onların duasını işitti."},
 "tokens": [
  MADI("وَسَمِعَ", "samia"),
  FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl"),
  MAFUL("دُعَاءَهُمْ", "dua", "noun", ["idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ", ", annexed to «their»", ", «onların» zamirine muzâf", punct=".", segments=[seg("دُعَاءَ", "dua", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
 ]})

# ============ Chapter 2 — the birth of Musa ============
S2 = []
S2.append({"id": "s1", "translation": {"en": "And a beautiful boy was born among the Children of Israel.", "tr": "Ve İsrailoğulları arasında güzel bir çocuk doğdu."},
 "tokens": [
  tok("وَوُلِدَ", "walada", "verb", ["naib-al-fail", "mithal-verbs"], "الْوَاوُ عَاطِفَةٌ، وَوُلِدَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "The waw conjoins; a past verb in the passive («was born»).", "«ve» + «doğdu» — meçhul mâzî fiil (doğuruldu).", segments=[seg("وَ", "wa", "conj"), seg("وُلِدَ", "walada", "verb")]),
  PREP("فِي", "fi", gloss_tr="«arasında»"),
  MAJR("بَنِي", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural, in jarr by the ya; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak, yâ ile mecrûr; nûnu izâfet için düşmüş, muzâf", sign="بِالْيَاءِ"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2]),
  tok("وَلَدٌ", "walad", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "The deputy doer (the subject of the passive), in raf'.", "Nâib-i fâil, merfû."),
  NAAT("جَمِيلٌ", "jamil", "raf", punct="."),
 ]})
S2.append({"id": "s2", "translation": {"en": "And the name of this boy was Musa.", "tr": "Ve bu çocuğun adı Mûsâ idi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("اسْمُ", "ism", note_ar="، مُضَافٌ", note_en=", the first term of an idafa", note_tr=", muzâf"),
  tok("هَذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A demonstrative, built; it fills the seat of the mudaf ilayh in jarr.", "İsm-i işâret, mebnî; mahallen mecrûr, muzâfun ileyh."),
  tok("الْوَلَدِ", "walad", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A badal of the demonstrative, in jarr.", "İsm-i işâretten bedel, mecrûr."),
  KHK("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِفَتْحَةٍ " + MUQ_ALIF[0], punct="."),
 ]})
S2.append({"id": "s3", "translation": {"en": "And Musa's mother feared for her son.", "tr": "Ve Mûsâ'nın annesi oğlu için korktu."},
 "tokens": [
  MADI("وَخَافَتْ", "khafa", ["hollow-verbs"], fem=True),
  FAIL("أُمُّ", "umm", "noun", ["idafa-definiteness"], "، مُضَافٌ", ", the first term of an idafa", ", muzâf"),
  MUDAF_ILAYH("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "بِكَسْرَةٍ " + MUQ_ALIF[0], "", MUQ_ALIF[1], MUQ_ALIF[2]),
  PREP("عَلَى", "ala", gloss_tr="«için, üzerine»"),
  MAJR("وَلَدِهَا", "walad", "noun", ["idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ", ", annexed to «her»", ", «onun» zamirine muzâf", punct=".", segments=[seg("وَلَدِ", "walad", "noun"), seg("هَا", "pron-3fs", "pron")]),
 ]})
S2.append({"id": "s4", "translation": {"en": "So she put Musa in a box.", "tr": "Bunun üzerine Mûsâ'yı bir sandığa koydu."},
 "tokens": [
  MADI("فَوَضَعَتْ", "wadaa", ["mithal-verbs"], fem=True, hidden=True),
  MAFUL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِفَتْحَةٍ " + MUQ_ALIF[0]),
  PREP("فِي", "fi", gloss_tr="«-e, içine»"),
  MAJR("صُنْدُوقٍ", "sunduq", punct="."),
 ]})
S2.append({"id": "s5", "translation": {"en": "And she threw the box into the river.", "tr": "Ve sandığı nehre attı."},
 "tokens": [
  MADI("وَأَلْقَتِ", "alqa", ["form-iv-verbs", "naqis-verbs"], fem=True, hidden=True, kasra=True, note_ar=" — أَلْقَى فِعْلٌ مَزِيدٌ عَلَى أَفْعَلَ، نَاقِصٌ", note_en=" — Form IV, weak-final", note_tr=" — if'âl bâbından nâkıs fiil"),
  MAFUL("الصُّنْدُوقَ", "sunduq"),
  PREP("فِي", "fi", gloss_tr="«-e, içine»"),
  MAJR("النَّهْرِ", "nahr", punct="."),
 ]})
S2.append({"id": "s6", "translation": {"en": "And the river was big, and its name was the Nile.", "tr": "Ve nehir büyüktü; adı Nil idi."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("النَّهْرُ", "nahr"),
  KHK("كَبِيرًا", "kabir", punct="،"),
  KANA("وَكَانَ"),
  ISMK("اسْمُهُ", "ism", note_ar="، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", note_en=", annexed to «its»", note_tr=", «onun» zamirine muzâf", segments=[seg("اسْمُ", "ism", "noun"), seg("هُ", "pron-3ms", "pron")]),
  KHK("النِّيلَ", "nil", "propn", punct="."),
 ]})
S2.append({"id": "s7", "translation": {"en": "And Pharaoh's wife saw the box.", "tr": "Ve Firavun'un karısı sandığı gördü."},
 "tokens": [
  MADI("وَرَأَتِ", "raa", ["naqis-verbs"], fem=True, kasra=True),
  FAIL("امْرَأَةُ", "imraa", "noun", ["idafa-definiteness"], "، مُضَافٌ", ", the first term of an idafa", ", muzâf"),
  MUDAF_ILAYH("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2]),
  MAFUL("الصُّنْدُوقَ", "sunduq", punct="."),
 ]})
S2.append({"id": "s8", "translation": {"en": "And she opened the box, and saw in it a beautiful boy.", "tr": "Ve sandığı açtı; içinde güzel bir çocuk gördü."},
 "tokens": [
  MADI("وَفَتَحَتِ", "fataha", fem=True, hidden=True, kasra=True),
  MAFUL("الصُّنْدُوقَ", "sunduq", punct="،"),
  MADI("فَرَأَتْ", "raa", ["naqis-verbs"], fem=True, hidden=True),
  PREP("فِيهِ", "fi", "، وَالْهَاءُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ", "; the attached pronoun «it» is in jarr", "; «onun» zamiri mahallen mecrûr", gloss_tr="«içinde»", segments=[seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  MAFUL("وَلَدًا", "walad"),
  NAAT("جَمِيلًا", "jamil", "nasb", punct="."),
 ]})
S2.append({"id": "s9", "translation": {"en": "So she loved the boy.", "tr": "Bunun üzerine çocuğu sevdi."},
 "tokens": [
  MADI("فَأَحَبَّتِ", "ahabba", ["form-iv-verbs", "doubled-verbs"], fem=True, hidden=True, kasra=True, note_ar=" — أَحَبَّ فِعْلٌ مَزِيدٌ عَلَى أَفْعَلَ، مُضَاعَفٌ", note_en=" — Form IV, doubled", note_tr=" — if'âl bâbından muzâaf fiil"),
  MAFUL("الْوَلَدَ", "walad", punct="."),
 ]})
S2.append({"id": "s10", "translation": {"en": "And she said to Pharaoh: «This is my son.»", "tr": "Ve Firavun'a «Bu benim oğlumdur» dedi."},
 "tokens": [
  MADI("وَقَالَتْ", "qala", ["hollow-verbs", "maful-bihi"], fem=True, hidden=True, note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür"),
  PREP("لِفِرْعَوْنَ", "li", gloss_tr="«Firavun'a»", segments=[seg("لِ", "li", "prep"), seg("فِرْعَوْنَ", "firawn", "propn")], punct=":"),
  tok("هَذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A demonstrative, built; it fills the mubtada's seat in raf'.", "İsm-i işâret, mebnî; mahallen merfû mübtedâ."),
  tok("وَلَدِي", "walad", "noun", ["mubtada-khabar", "idafa-definiteness", "ya-al-mutakallim"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "The khabar in raf' — the damma is estimated before the speaker's ya; annexed to «my».", "Haber; damme mütekellim yâ'sından önce takdîrîdir; «benim»e muzâf.", punct=".", segments=[seg("وَلَدِ", "walad", "noun"), seg("ي", "pron-1s", "pron")]),
 ]})
S2.append({"id": "s11", "translation": {"en": "And Musa grew up in Pharaoh's house.", "tr": "Ve Mûsâ Firavun'un evinde büyüdü."},
 "tokens": [
  MADI("وَكَبِرَ", "kabira", note_ar=" — مِنْ بَابِ سَمِعَ", note_en=" — of the bab سَمِعَ يَسْمَعُ", note_tr=" — semi'a bâbından"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("فِي", "fi", gloss_tr="«-de»"),
  MAJR("بَيْتِ", "bayt", "noun", ["idafa-definiteness"], "، مُضَافٌ", ", the first term of an idafa", ", muzâf"),
  MUDAF_ILAYH("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})

# ============ Chapter 3 — Musa, the messenger of God ============
S3 = []
S3.append({"id": "s1", "translation": {"en": "And Musa left Egypt, and went to Madyan.", "tr": "Ve Mûsâ Mısır'dan çıktı ve Medyen'e gitti."},
 "tokens": [
  MADI("وَخَرَجَ", "kharaja"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("مِنْ", "min", gloss_tr="«-den»"),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], DIPT_F[0], DIPT_F[1], DIPT_F[2], sign=FATHA_JARR, punct="،"),
  MADI("وَذَهَبَ", "dhahaba", hidden=True),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("مَدْيَنَ", "madyan", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], sign=FATHA_JARR, punct="."),
 ]})
S3.append({"id": "s2", "translation": {"en": "And he stayed there a long time.", "tr": "Ve orada uzun bir zaman kaldı."},
 "tokens": [
  MADI("وَبَقِيَ", "baqiya", ["naqis-verbs"], hidden=True),
  tok("هُنَاكَ", "hunaka", "noun", ["maful-fih", "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", "A demonstrative of place, built on fatha; it fills the seat of an adverb of place (nasb).", "Mekân ism-i işâreti, fetha üzere mebnî; mahallen mansûb zarf-ı mekân."),
  tok("زَمَانًا", "zaman", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (مَفْعُولٌ فِيهِ).", "An adverb of time (maf'ul fih), in nasb.", "Zarf-ı zamân (mef'ûlün fîh), mansûb."),
  NAAT("طَوِيلًا", "tawil-long", "nasb", ["sifa-mushabbaha"], punct="."),
 ]})
S3.append({"id": "s3", "translation": {"en": "Then Musa returned to Egypt.", "tr": "Sonra Mûsâ Mısır'a döndü."},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "A conjunction of ordered sequence with a pause.", "Tertib ve terâhî bildiren atıf harfi."),
  MADI("رَجَعَ", "rajaa"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], DIPT_F[0], DIPT_F[1], DIPT_F[2], sign=FATHA_JARR, punct="."),
 ]})
S3.append({"id": "s4", "translation": {"en": "And God spoke to him on the way.", "tr": "Ve Allah yolda onunla konuştu."},
 "tokens": [
  tok("وَكَلَّمَهُ", "kallama", "verb", ["form-ii-verbs", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَكَلَّمَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "The waw conjoins; a Form II past verb, and the attached «him» is its object (nasb).", "«ve» + «onunla konuştu» — tef'îl bâbından mâzî; bitişik «onu» zamiri mahallen mansûb mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("كَلَّمَ", "kallama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl"),
  PREP("فِي", "fi", gloss_tr="«-de»"),
  MAJR("الطَّرِيقِ", "tariq", punct="."),
 ]})
S3.append({"id": "s5", "translation": {"en": "And God said to Musa: «Go to Pharaoh.»", "tr": "Ve Allah Mûsâ'ya «Firavun'a git» dedi."},
 "tokens": [
  MADI("وَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür"),
  FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl"),
  PREP("لِمُوسَى", "li", "، وَمُوسَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", "; Musa is in jarr with the kasra estimated on the alif", "; Mûsâ, elif üzerinde takdîrî kesre ile mecrûr", gloss_tr="«Mûsâ'ya»", segments=[seg("لِ", "li", "prep"), seg("مُوسَى", "musa", "propn")], punct=":"),
  tok("اِذْهَبْ", "dhahaba", "verb", ["imperative-amr"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "An imperative, built on sukun; its doer is necessarily hidden (you).", "Sükûn üzere mebnî emir fiili; fâili vücûben gizli (sen)."),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], sign=FATHA_JARR, punct="."),
 ]})
S3.append({"id": "s6", "translation": {"en": "So Musa went to Pharaoh.", "tr": "Bunun üzerine Mûsâ Firavun'a gitti."},
 "tokens": [
  MADI("فَذَهَبَ", "dhahaba"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], sign=FATHA_JARR, punct="."),
 ]})
S3.append({"id": "s7", "translation": {"en": "And Musa said: «O Pharaoh, I am the messenger of God.»", "tr": "Ve Mûsâ dedi ki: «Ey Firavun, ben Allah'ın elçisiyim.»"},
 "tokens": [
  MADI("وَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0], punct=":"),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "The vocative particle.", "Nidâ harfi."),
  tok("فِرْعَوْنُ", "firawn", "propn", ["vocative-munada", "mamnu-min-sarf"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "A single proper-name vocative, built on damma, in the seat of nasb.", "Müfred alem münâdâ; zamme üzere mebnî, mahallen mansûb.", punct="،"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun, built; it fills the mubtada's seat in raf'.", "Munfasıl zamir, mebnî; mahallen merfû mübtedâ."),
  tok("رَسُولُ", "rasul", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The khabar in raf', the first term of an idafa.", "Haber, merfû; muzâf."),
  MUDAF_ILAYH("اللهِ", "allah", "propn", [], note_ar=" — لَفْظُ الْجَلَالَةِ", note_en=" — the Name of Majesty", note_tr=" — lafza-i celâl", punct="."),
 ]})
S3.append({"id": "s8", "translation": {"en": "«God is your Lord and the Lord of the people.»", "tr": "«Allah senin Rabbin ve insanların Rabbidir.»"},
 "tokens": [
  tok("اللهُ", "allah", "propn", ["mubtada-khabar"], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The Name of Majesty as the mubtada, in raf'.", "Lafza-i celâl mübtedâ, merfû."),
  tok("رَبُّكَ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "The khabar in raf', annexed to «your».", "Haber, merfû; «senin» zamirine muzâf.", segments=[seg("رَبُّ", "rabb", "noun"), seg("كَ", "pron-2ms", "pron")]),
  ATF("وَرَبُّ", "rabb", "noun", "raf", ["idafa-definiteness"], "، مُضَافٌ", ", the first term of an idafa", ", muzâf"),
  MUDAF_ILAYH("النَّاسِ", "nas", punct="."),
 ]})
S3.append({"id": "s9", "translation": {"en": "Then Pharaoh grew angry and said: «I am the king, and I am your lord.»", "tr": "Bunun üzerine Firavun öfkelendi ve dedi: «Kral benim, rabbiniz de benim.»"},
 "tokens": [
  MADI("فَغَضِبَ", "ghadiba"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  MADI("وَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür", punct=":"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun, built; it fills the mubtada's seat in raf'.", "Munfasıl zamir, mebnî; mahallen merfû mübtedâ."),
  tok("الْمَلِكُ", "malik-king", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The khabar, in raf'.", "Haber, merfû.", punct="،"),
  tok("وَأَنَا", "ana", "pron", ["mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَأَنَا ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins a second clause; the detached pronoun is its mubtada.", "«ve» + «ben» — ikinci cümlenin mübtedâsı.", segments=[seg("وَ", "wa", "conj"), seg("أَنَا", "ana", "pron")]),
  tok("رَبُّكُمْ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "The khabar in raf', annexed to «your».", "Haber, merfû; «sizin» zamirine muzâf.", punct=".", segments=[seg("رَبُّ", "rabb", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
 ]})
S3.append({"id": "s10", "translation": {"en": "And Pharaoh did not believe.", "tr": "Ve Firavun iman etmedi."},
 "tokens": [
  tok("وَلَمْ", "lam-jazima", "part", ["lam-jazim", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates, puts the verb in jazm and turns its tense to the past.", "«ve» + «-medi» — nefiy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يُؤْمِنْ", "amana", "verb", ["lam-jazim", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ — آمَنَ عَلَى أَفْعَلَ، مَهْمُوزُ الْفَاءِ.", "Present verb in jazm after لَمْ, marked by sukun — Form IV of a hamza-initial root.", "Lem ile meczûm muzâri, alâmeti sükûn — if'âl bâbından, mehmûzü'l-fâ."),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})

# ============ Chapter 4 — the sea ============
S4 = []
S4.append({"id": "s1", "translation": {"en": "And Musa left Egypt with the Children of Israel.", "tr": "Ve Mûsâ İsrailoğullarıyla birlikte Mısır'dan çıktı."},
 "tokens": [
  MADI("وَخَرَجَ", "kharaja"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("مِنْ", "min", gloss_tr="«-den»"),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], DIPT_F[0], DIPT_F[1], DIPT_F[2], sign=FATHA_JARR),
  tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb (maf'ul fih) «with», in nasb; the first term of an idafa.", "Zarf (mef'ûlün fîh) «ile birlikte», mansûb; muzâf."),
  MUDAF_ILAYH("بَنِي", "banu", "noun", ["jam-mudhakkar-salim"], "بِالْيَاءِ", " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak; izâfet için nûnu düşmüş, muzâf"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S4.append({"id": "s2", "translation": {"en": "And Pharaoh went out after them with a big army.", "tr": "Ve Firavun büyük bir orduyla onların arkasından çıktı."},
 "tokens": [
  MADI("وَخَرَجَ", "kharaja"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  tok("وَرَاءَهُمْ", "wara", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "An adverb of place «behind», in nasb, annexed to «them».", "Zarf-ı mekân «arkasından», mansûb; «onlar» zamirine muzâf.", segments=[seg("وَرَاءَ", "wara", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  PREP("بِجَيْشٍ", "bi", gloss_tr="«bir orduyla»", segments=[seg("بِ", "bi", "prep"), seg("جَيْشٍ", "jaysh", "noun")]),
  NAAT("كَبِيرٍ", "kabir", "jarr", punct="."),
 ]})
S4.append({"id": "s3", "translation": {"en": "And Musa reached the sea.", "tr": "Ve Mûsâ denize vardı."},
 "tokens": [
  MADI("وَوَصَلَ", "wasala", ["mithal-verbs"]),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("الْبَحْرِ", "bahr", punct="."),
 ]})
S4.append({"id": "s4", "translation": {"en": "And Musa struck the sea with his staff.", "tr": "Ve Mûsâ asasıyla denize vurdu."},
 "tokens": [
  MADI("وَضَرَبَ", "daraba"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  MAFUL("الْبَحْرَ", "bahr"),
  tok("بِعَصَاهُ", "bi", "prep", ["huruf-jarr", "ism-maqsur-manqus", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَعَصَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The ba is a jarr letter; «staff» is in jarr with the kasra estimated on its alif, annexed to «his».", "Bâ cer harfi; «asâ», elif üzerinde takdîrî kesre ile mecrûr; «onun» zamirine muzâf.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("عَصَا", "asa-staff", "noun"), seg("هُ", "pron-3ms", "pron")]),
 ]})
S4.append({"id": "s5", "translation": {"en": "And a road came to be in the sea.", "tr": "Bunun üzerine denizde bir yol oluştu."},
 "tokens": [
  SARA("فَصَارَ"),
  PREP("فِي", "fi", "، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ صَارَ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate of صَارَ", "; câr-mecrûr, sâre'nin öne alınmış haberidir", gloss_tr="«-de»"),
  MAJR("الْبَحْرِ", "bahr"),
  tok("طَرِيقٌ", "tariq", "noun", ["kana-wa-akhawatuha"], "اسْمُ صَارَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of صَارَ, placed after its predicate, in raf'.", "Sâre'nin ismi (haberinden sonraya bırakılmış), merfû.", punct="."),
 ]})
S4.append({"id": "s6", "translation": {"en": "And Musa and his people walked along the road.", "tr": "Ve Mûsâ ve kavmi yolda yürüdü."},
 "tokens": [
  MADI("وَمَشَى", "masha", ["naqis-verbs"]),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  ATF("وَقَوْمُهُ", "qawm", "noun", "raf", ["idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", ", annexed to «his»", ", «onun» zamirine muzâf", segments=[seg("وَ", "wa", "conj"), seg("قَوْمُ", "qawm", "noun"), seg("هُ", "pron-3ms", "pron")]),
  PREP("فِي", "fi", gloss_tr="«-de»"),
  MAJR("الطَّرِيقِ", "tariq", punct="."),
 ]})
S4.append({"id": "s7", "translation": {"en": "And Pharaoh and his army entered the sea.", "tr": "Ve Firavun ve ordusu denize girdi."},
 "tokens": [
  MADI("وَدَخَلَ", "dakhala"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  ATF("وَجَيْشُهُ", "jaysh", "noun", "raf", ["idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", ", annexed to «his»", ", «onun» zamirine muzâf", segments=[seg("وَ", "wa", "conj"), seg("جَيْشُ", "jaysh", "noun"), seg("هُ", "pron-3ms", "pron")]),
  PREP("فِي", "fi", gloss_tr="«-e»"),
  MAJR("الْبَحْرِ", "bahr", punct="."),
 ]})
S4.append({"id": "s8", "translation": {"en": "Then the water came back, and Pharaoh and his army drowned.", "tr": "Bunun üzerine su geri döndü; Firavun ve ordusu boğuldu."},
 "tokens": [
  MADI("فَرَجَعَ", "rajaa"),
  FAIL("الْمَاءُ", "ma-water", punct="،"),
  MADI("وَغَرِقَ", "ghariqa"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  ATF("وَجَيْشُهُ", "jaysh", "noun", "raf", ["idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", ", annexed to «his»", ", «onun» zamirine muzâf", punct=".", segments=[seg("وَ", "wa", "conj"), seg("جَيْشُ", "jaysh", "noun"), seg("هُ", "pron-3ms", "pron")]),
 ]})
S4.append({"id": "s9", "translation": {"en": "And Musa and the Children of Israel were saved.", "tr": "Ve Mûsâ ve İsrailoğulları kurtuldu."},
 "tokens": [
  MADI("وَنَجَا", "naja-escape", ["naqis-verbs"]),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  ATF("وَبَنُو", "banu", "noun", "raf", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak, vâv ile merfû; nûnu izâfet için düşmüş, muzâf", sign="مَرْفُوعٌ بِالْوَاوِ", segments=[seg("وَ", "wa", "conj"), seg("بَنُو", "banu", "noun")]),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S4.append({"id": "s10", "translation": {"en": "And Musa thanked God.", "tr": "Ve Mûsâ Allah'a şükretti."},
 "tokens": [
  MADI("وَشَكَرَ", "shakara"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  MAFUL("اللهَ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl", punct="."),
 ]})


# ============ Chapter 5 — Musa and the magicians ============
S5 = []
S5.append({"id": "s1", "translation": {"en": "And Musa had a staff with him.", "tr": "Ve Mûsâ'nın yanında bir asâ vardı."},
 "tokens": [
  KANA("وَكَانَ"),
  tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ خَبَرُ كَانَ مُقَدَّمٌ.", "An adverb «with», in nasb, the first term of an idafa — the FRONTED predicate of كَانَ.", "Zarf «yanında», mansûb, muzâf — kâne'nin öne alınmış haberidir."),
  MUDAF_ILAYH("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "بِكَسْرَةٍ " + MUQ_ALIF[0], "", MUQ_ALIF[1], MUQ_ALIF[2]),
  ISMK("عَصًا", "asa-staff", extra=["ism-maqsur-manqus"], note_ar=" — اسْمٌ مَقْصُورٌ، وَالتَّنْوِينُ ظَاهِرٌ وَالضَّمَّةُ مُقَدَّرَةٌ", note_en=" — a maqsur noun: the tanwin shows, the damma is estimated", note_tr=" — maksûr isim: tenvin görünür, damme takdîrîdir", sign="بِضَمَّةٍ " + MUQ_ALIF[0], muakhkhar=True, punct="."),
 ]})
S5.append({"id": "s2", "translation": {"en": "And Musa threw his staff before Pharaoh.", "tr": "Ve Mûsâ asâsını Firavun'un önüne attı."},
 "tokens": [
  MADI("وَأَلْقَى", "alqa", ["form-iv-verbs", "naqis-verbs"], note_ar=" — أَلْقَى عَلَى أَفْعَلَ، نَاقِصٌ، مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ", note_en=" — Form IV, weak-final: the fatha is estimated on the alif", note_tr=" — if'âl bâbından nâkıs fiil: fetha elif üzerinde takdîrîdir"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  MAFUL("عَصَاهُ", "asa-staff", "noun", ["ism-maqsur-manqus", "idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", ", annexed to «his»", ", «onun» zamirine muzâf", sign="بِفَتْحَةٍ " + MUQ_ALIF[0], segments=[seg("عَصَا", "asa-staff", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("أَمَامَ", "amama", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of place «before, in front of», in nasb; the first term of an idafa.", "Zarf-ı mekân «önünde», mansûb; muzâf."),
  MUDAF_ILAYH("فِرْعَوْنَ", "firawn", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S5.append({"id": "s3", "translation": {"en": "And the staff became a big snake.", "tr": "Bunun üzerine asâ büyük bir yılan oldu."},
 "tokens": [
  tok("فَصَارَتِ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], FA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "The fa conjoins; صَارَ «became» is a sister of كَانَ; the ta marks the feminine, voweled with kasra before the following ال.", "«bunun üzerine» + «oldu» — kâne'nin kardeşi sâre; tâ te'nîs içindir, iki sâkin karşılaştığı için kesrelendi.", segments=[seg("فَ", "fa", "conj"), seg("صَارَتِ", "sara", "verb")]),
  tok("الْعَصَا", "asa-staff", "noun", ["kana-wa-akhawatuha", "ism-maqsur-manqus"], "اسْمُ صَارَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The noun of صَارَ, in raf' with the damma estimated on the alif.", "Sâre'nin ismi, elif üzerinde takdîrî damme ile merfû."),
  tok("حَيَّةً", "hayya-snake", "noun", ["kana-wa-akhawatuha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of صَارَ, in nasb.", "Sâre'nin haberi, mansûb."),
  NAAT("كَبِيرَةً", "kabir", "nasb", ["al-muannath-wa-alamatuh"], " — مُؤَنَّثٌ بِالتَّاءِ", " — feminine by the ta", " — tâ ile müennes", punct="."),
 ]})
S5.append({"id": "s4", "translation": {"en": "And Pharaoh was afraid.", "tr": "Ve Firavun korktu."},
 "tokens": [
  MADI("وَخَافَ", "khafa", ["hollow-verbs"]),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], punct="."),
 ]})
S5.append({"id": "s5", "translation": {"en": "And Pharaoh said: «This is magic.»", "tr": "Ve Firavun «Bu bir sihirdir» dedi."},
 "tokens": [
  MADI("وَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], note_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", note_en="; what is said is its object", note_tr="; söylenen söz mef'ûlüdür"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2], punct=":"),
  tok("هَذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A demonstrative, built; it fills the mubtada's seat in raf'.", "İsm-i işâret, mebnî; mahallen merfû mübtedâ."),
  tok("سِحْرٌ", "sihr", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The khabar, in raf'.", "Haber, merfû.", punct="."),
 ]})
S5.append({"id": "s6", "translation": {"en": "So Pharaoh gathered the magicians.", "tr": "Bunun üzerine Firavun sihirbazları topladı."},
 "tokens": [
  MADI("فَجَمَعَ", "jamaa-gather"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  MAFUL("السَّحَرَةَ", "sahir", "noun", ["jam-taksir"], " — جَمْعُ سَاحِرٍ", " — the broken plural of سَاحِر", " — sâhir'in cem'i", punct="."),
 ]})
S5.append({"id": "s7", "translation": {"en": "And the magicians threw their ropes.", "tr": "Ve sihirbazlar iplerini attılar."},
 "tokens": [
  MADI("وَأَلْقَى", "alqa", ["form-iv-verbs", "naqis-verbs"], note_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ", note_en=" — the fatha is estimated on the alif", note_tr=" — fetha elif üzerinde takdîrîdir"),
  FAIL("السَّحَرَةُ", "sahir", "noun", ["jam-taksir"], " — جَمْعُ سَاحِرٍ", " — the broken plural of سَاحِر", " — sâhir'in cem'i"),
  MAFUL("حِبَالَهُمْ", "habl", "noun", ["jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ حَبْلٍ", ", annexed to «their» — the broken plural of حَبْل", ", «onların» zamirine muzâf — habl'in cem'i", punct=".", segments=[seg("حِبَالَ", "habl", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
 ]})
S5.append({"id": "s8", "translation": {"en": "And the ropes became snakes.", "tr": "Bunun üzerine ipler yılanlar oldu."},
 "tokens": [
  tok("فَصَارَتِ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], FA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "The fa conjoins; صَارَ is the defective verb; the ta marks the feminine, voweled with kasra before the following ال.", "«bunun üzerine» + «oldu» — nâkıs fiil sâre; tâ te'nîs içindir, iki sâkin için kesrelendi.", segments=[seg("فَ", "fa", "conj"), seg("صَارَتِ", "sara", "verb")]),
  tok("الْحِبَالُ", "habl", "noun", ["kana-wa-akhawatuha", "jam-taksir"], "اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ حَبْلٍ.", "The noun of صَارَ, in raf' — the broken plural of حَبْل.", "Sâre'nin ismi, merfû — habl'in cem'i."),
  tok("حَيَّاتٍ", "hayya-snake", "noun", ["kana-wa-akhawatuha", "jam-muannath-salim"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "The predicate of صَارَ, in nasb — marked by KASRA, because it is a sound feminine plural.", "Sâre'nin haberi, mansûb — cem-i müennes sâlim olduğu için nasb alâmeti KESREDİR.", punct="."),
 ]})
S5.append({"id": "s9", "translation": {"en": "And Musa threw his staff, and it ate the snakes.", "tr": "Ve Mûsâ asâsını attı; asâ yılanları yedi."},
 "tokens": [
  MADI("وَأَلْقَى", "alqa", ["form-iv-verbs", "naqis-verbs"], note_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ", note_en=" — the fatha is estimated on the alif", note_tr=" — fetha elif üzerinde takdîrîdir"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  MAFUL("عَصَاهُ", "asa-staff", "noun", ["ism-maqsur-manqus", "idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", ", annexed to «his»", ", «onun» zamirine muzâf", sign="بِفَتْحَةٍ " + MUQ_ALIF[0], punct="،", segments=[seg("عَصَا", "asa-staff", "noun"), seg("هُ", "pron-3ms", "pron")]),
  MADI("فَأَكَلَتِ", "akala", fem=True, hidden=True, kasra=True, note_ar=" — أَيِ: الْعَصَا", note_en=" — that is, the staff", note_tr=" — yani asâ"),
  MAFUL("الْحَيَّاتِ", "hayya-snake", "noun", ["jam-muannath-salim"], " نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ", " — marked by KASRA, because it is a sound feminine plural", " — cem-i müennes sâlim olduğu için nasb alâmeti KESREDİR", sign="بِالْكَسْرَةِ", punct="."),
 ]})
S5.append({"id": "s10", "translation": {"en": "Then the magicians prostrated and said: «We believe in the Lord of Musa.»", "tr": "Bunun üzerine sihirbazlar secde ettiler ve «Mûsâ'nın Rabbine iman ettik» dediler."},
 "tokens": [
  MADI("فَسَجَدَ", "sajada"),
  FAIL("السَّحَرَةُ", "sahir", "noun", ["jam-taksir"], " — جَمْعُ سَاحِرٍ", " — the broken plural of سَاحِر", " — sâhir'in cem'i", punct="،"),
  tok("وَقَالُوا", "qala", "verb", ["hollow-verbs", "atf-nasaq", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَقَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "The waw conjoins; the past verb is built on damma before the plural waw, which is its doer; what is said is the object.", "«ve» + «dediler» — cemâat vâvına bitiştiği için zamme üzere mebnî mâzî; vâv fâildir; söylenen söz mef'ûlüdür.", punct=":", segments=[seg("وَ", "wa", "conj"), seg("قَالُوا", "qala", "verb")]),
  tok("آمَنَّا", "amana", "verb", ["form-iv-verbs", "fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا الْفَاعِلِينَ، وَنَا فَاعِلٌ — آمَنَ عَلَى أَفْعَلَ.", "A Form IV past verb, built on sukun before the attached «we», which is its doer.", "If'âl bâbından mâzî; fâil nâ'sına bitiştiği için sükûn üzere mebnî; nâ fâildir.", segments=[seg("آمَنْ", "amana", "verb"), seg("نَا", "pron-1p", "pron")]),
  PREP("بِرَبِّ", "bi", "، وَرَبِّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ", "; «Lord» is in jarr, the first term of an idafa", "; «Rab» mecrûr, muzâf", gloss_tr="«Rabbine»", segments=[seg("بِ", "bi", "prep"), seg("رَبِّ", "rabb", "noun")]),
  MUDAF_ILAYH("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "بِكَسْرَةٍ " + MUQ_ALIF[0], "", MUQ_ALIF[1], MUQ_ALIF[2], punct="."),
 ]})
S5.append({"id": "s11", "translation": {"en": "And Pharaoh grew very angry.", "tr": "Ve Firavun şiddetle öfkelendi."},
 "tokens": [
  MADI("وَغَضِبَ", "ghadiba"),
  FAIL("فِرْعَوْنُ", "firawn", "propn", ["mamnu-min-sarf"], DIPT[0], DIPT[1], DIPT[2]),
  tok("غَضَبًا", "ghadab", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "The absolute object (the verb's own masdar), in nasb.", "Mef'ûl-i mutlak (fiilin kendi mastarı), mansûb."),
  NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct="."),
 ]})

# ============ Chapter 6 — in the desert ============
S6 = []
S6.append({"id": "s1", "translation": {"en": "And the Children of Israel walked in the desert.", "tr": "Ve İsrailoğulları çölde yürüdüler."},
 "tokens": [
  MADI("وَمَشَى", "masha", ["naqis-verbs"]),
  FAIL("بَنُو", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak, vâv ile merfû; nûnu izâfet için düşmüş, muzâf", sign="بِالْوَاوِ"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2]),
  PREP("فِي", "fi", gloss_tr="«-de»"),
  MAJR("الصَّحْرَاءِ", "sahra", punct="."),
 ]})
S6.append({"id": "s2", "translation": {"en": "And the weather was hot, and they had no water with them.", "tr": "Ve hava sıcaktı; yanlarında su yoktu."},
 "tokens": [
  KANA("وَكَانَ"),
  ISMK("الْجَوُّ", "jaww"),
  KHK("حَارًّا", "harr-hot", punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", ["lam-jazim", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates, puts the verb in jazm and turns its tense to the past.", "«ve» + «-medi» — nefiy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يَكُنْ", "kana", "verb", ["lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "The defective verb in the present, in jazm after لَمْ (sukun); its waw dropped where two sukuns met (يَكُونْ → يَكُنْ).", "Nâkıs muzâri, lem ile meczûm (sükûn); iki sâkin karşılaşınca vâvı düştü (يَكُونْ → يَكُنْ)."),
  tok("مَعَهُمْ", "maa", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرُ يَكُنْ مُقَدَّمٌ.", "An adverb «with», in nasb, annexed to «them» — the FRONTED predicate of the verb.", "Zarf «yanlarında», mansûb, «onlar» zamirine muzâf — yekün'ün öne alınmış haberidir.", segments=[seg("مَعَ", "maa", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("مَاءٌ", "ma-water", "noun", ["kana-wa-akhawatuha"], "اسْمُ يَكُنْ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of the verb, placed after its predicate, in raf'.", "Yekün'ün ismi (haberinden sonraya bırakılmış), merfû.", punct="."),
 ]})
S6.append({"id": "s3", "translation": {"en": "So they said to Musa: «We want water.»", "tr": "Bunun üzerine Mûsâ'ya «Su istiyoruz» dediler."},
 "tokens": [
  tok("فَقَالُوا", "qala", "verb", ["hollow-verbs", "maful-bihi"], FA_AR + "قَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "The fa conjoins; the past verb is built on damma before the plural waw, which is its doer; what is said is the object.", "«bunun üzerine» + «dediler» — cemâat vâvına bitiştiği için zamme üzere mebnî; vâv fâildir; söylenen söz mef'ûlüdür.", segments=[seg("فَ", "fa", "conj"), seg("قَالُوا", "qala", "verb")]),
  PREP("لِمُوسَى", "li", "، وَمُوسَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", "; Musa is in jarr with the kasra estimated on the alif", "; Mûsâ, elif üzerinde takdîrî kesre ile mecrûr", gloss_tr="«Mûsâ'ya»", segments=[seg("لِ", "li", "prep"), seg("مُوسَى", "musa", "propn")], punct=":"),
  tok("نُرِيدُ", "arada", "verb", ["form-iv-verbs", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ — أَرَادَ عَلَى أَفْعَلَ، أَجْوَفُ.", "Present verb in raf'; its doer is necessarily hidden (we) — Form IV of a hollow root.", "Merfû muzâri; fâili vücûben gizli (biz) — if'âl bâbından ecvef fiil."),
  MAFUL("مَاءً", "ma-water", punct="."),
 ]})
S6.append({"id": "s4", "translation": {"en": "So Musa struck the rock with his staff.", "tr": "Bunun üzerine Mûsâ asâsıyla kayaya vurdu."},
 "tokens": [
  MADI("فَضَرَبَ", "daraba"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  MAFUL("الْحَجَرَ", "hajar"),
  tok("بِعَصَاهُ", "bi", "prep", ["huruf-jarr", "ism-maqsur-manqus", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ، وَعَصَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "The ba is a jarr letter; «staff» is in jarr with the kasra estimated on its alif, annexed to «his».", "Bâ cer harfi; «asâ», elif üzerinde takdîrî kesre ile mecrûr; «onun» zamirine muzâf.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("عَصَا", "asa-staff", "noun"), seg("هُ", "pron-3ms", "pron")]),
 ]})
S6.append({"id": "s5", "translation": {"en": "And much water came out of the rock.", "tr": "Bunun üzerine kayadan çok su çıktı."},
 "tokens": [
  MADI("فَخَرَجَ", "kharaja"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter, voweled with fatha before the following ال.", "«-den» — cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("الْحَجَرِ", "hajar"),
  FAIL("مَاءٌ", "ma-water"),
  NAAT("كَثِيرٌ", "kathir", "raf", punct="."),
 ]})
S6.append({"id": "s6", "translation": {"en": "So the Children of Israel drank and praised God.", "tr": "Bunun üzerine İsrailoğulları içtiler ve Allah'a hamdettiler."},
 "tokens": [
  MADI("فَشَرِبَ", "shariba"),
  FAIL("بَنُو", "banu", "noun", ["jam-mudhakkar-salim", "idafa-definiteness"], " — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ", " — attached to the sound masculine plural, raised by the waw; its nun is dropped for the idafa", " — cem-i müzekker sâlime mülhak, vâv ile merfû; nûnu izâfet için düşmüş, muzâf", sign="بِالْوَاوِ"),
  MUDAF_ILAYH("إِسْرَائِيلَ", "israil", "propn", ["mamnu-min-sarf"], FATHA_JARR, DIPT[0], DIPT[1], DIPT[2]),
  tok("وَحَمِدُوا", "hamida", "verb", ["atf-nasaq", "fail"], "الْوَاوُ عَاطِفَةٌ، وَحَمِدُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.", "The waw conjoins; the past verb is built on damma before the plural waw, which is its doer.", "«ve» + «hamdettiler» — cemâat vâvına bitiştiği için zamme üzere mebnî mâzî; vâv fâildir.", segments=[seg("وَ", "wa", "conj"), seg("حَمِدُوا", "hamida", "verb")]),
  MAFUL("اللهَ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl", punct="."),
 ]})
S6.append({"id": "s7", "translation": {"en": "And Musa went to the mountain.", "tr": "Ve Mûsâ dağa gitti."},
 "tokens": [
  MADI("وَذَهَبَ", "dhahaba"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("الْجَبَلِ", "jabal", punct="."),
 ]})
S6.append({"id": "s8", "translation": {"en": "And God spoke to Musa on the mountain.", "tr": "Ve Allah dağda Mûsâ ile konuştu."},
 "tokens": [
  MADI("وَكَلَّمَ", "kallama", ["form-ii-verbs"]),
  FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl"),
  MAFUL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِفَتْحَةٍ " + MUQ_ALIF[0]),
  PREP("عَلَى", "ala", gloss_tr="«üzerinde, -de»"),
  MAJR("الْجَبَلِ", "jabal", punct="."),
 ]})
S6.append({"id": "s9", "translation": {"en": "And God gave him the Torah.", "tr": "Ve Allah ona Tevrat'ı verdi."},
 "tokens": [
  tok("وَأَعْطَاهُ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "mafulayn"], "الْوَاوُ عَاطِفَةٌ، وَأَعْطَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ فِي مَحَلِّ نَصْبٍ — أَعْطَى يَنْصِبُ مَفْعُولَيْنِ.", "The waw conjoins; a Form IV past verb (fatha estimated on the alif); the attached «him» is its FIRST object — أَعْطَى takes two objects.", "«ve» + «ona verdi» — if'âl bâbından mâzî (fetha elif üzerinde takdîrî); bitişik «ona» birinci mef'ûl — a'tâ iki mef'ûl alır.", segments=[seg("وَ", "wa", "conj"), seg("أَعْطَى", "aata", "verb"), seg("هُ", "pron-3ms", "pron")]),
  FAIL("اللهُ", "allah", "propn", [], " — لَفْظُ الْجَلَالَةِ", " — the Name of Majesty", " — lafza-i celâl"),
  tok("التَّوْرَاةَ", "tawrat", "propn", ["mafulayn", "maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The SECOND object, in nasb.", "İkinci mef'ûlün bih, mansûb.", punct="."),
 ]})
S6.append({"id": "s10", "translation": {"en": "And in the Torah there was light and guidance.", "tr": "Ve Tevrat'ta nur ve hidayet vardı."},
 "tokens": [
  KANA("وَكَانَ"),
  PREP("فِي", "fi", *KH_MUQ, gloss_tr="«-de»"),
  MAJR("التَّوْرَاةِ", "tawrat", "propn"),
  ISMK("نُورٌ", "nur", muakhkhar=True),
  ATF("وَهُدًى", "huda", "noun", "raf", ["ism-maqsur-manqus"], " — اسْمٌ مَقْصُورٌ، التَّنْوِينُ ظَاهِرٌ وَالضَّمَّةُ مُقَدَّرَةٌ عَلَى الْأَلِفِ", " — a maqsur noun: the tanwin shows, the damma is estimated on the alif", " — maksûr isim: tenvin görünür, damme elif üzerinde takdîrîdir", sign="مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ", punct=".", segments=[seg("وَ", "wa", "conj"), seg("هُدًى", "huda", "noun")]),
 ]})
S6.append({"id": "s11", "translation": {"en": "And Musa returned to his people with the Torah.", "tr": "Ve Mûsâ Tevrat ile kavmine döndü."},
 "tokens": [
  MADI("وَرَجَعَ", "rajaa"),
  FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus"], "", MUQ_ALIF[1], MUQ_ALIF[2], sign="بِضَمَّةٍ " + MUQ_ALIF[0]),
  PREP("إِلَى", "ila", gloss_tr="«-e»"),
  MAJR("قَوْمِهِ", "qawm", "noun", ["idafa-definiteness", "al-bariz-al-muttasil"], "، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ", ", annexed to «his»", ", «onun» zamirine muzâf", segments=[seg("قَوْمِ", "qawm", "noun"), seg("هِ", "pron-3ms", "pron")]),
  PREP("بِالتَّوْرَاةِ", "bi", gloss_tr="«Tevrat ile»", segments=[seg("بِ", "bi", "prep"), seg("التَّوْرَاةِ", "tawrat", "propn")], punct="."),
 ]})

TITLES = [
 {"ar": "فِرْعَوْنُ وَبَنُو إِسْرَائِيلَ", "en": "Pharaoh and the Children of Israel", "tr": "Firavun ve İsrailoğulları"},
 {"ar": "مَوْلِدُ مُوسَى", "en": "The Birth of Musa", "tr": "Mûsâ'nın Doğumu"},
 {"ar": "مُوسَى رَسُولُ اللهِ", "en": "Musa, the Messenger of God", "tr": "Allah'ın Elçisi Mûsâ"},
 {"ar": "الْبَحْرُ", "en": "The Sea", "tr": "Deniz"},
 {"ar": "مُوسَى وَالسَّحَرَةُ", "en": "Musa and the Magicians", "tr": "Mûsâ ve Sihirbazlar"},
 {"ar": "فِي الصَّحْرَاءِ", "en": "In the Desert", "tr": "Çölde"},
]
CHAPS = [S1, S2, S3, S4, S5, S6]

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule), plus the three new words
PREF = ["qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-1", "yunus-wa-al-hut", "ashab-al-fil",
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
 "sunduq": {"lemma": "صُنْدُوق", "root": "ص ن د ق", "pos": "noun", "plural": "صَنَادِيق", "gloss": {"en": "box, chest", "tr": "sandık"}, "level": 1},
 "nil": {"lemma": "النِّيل", "pos": "propn", "gloss": {"en": "the Nile", "tr": "Nil (nehri)"}, "level": 0},
 "hayya-snake": {"lemma": "حَيَّة", "root": "ح ي ي", "pos": "noun", "plural": "حَيَّات", "gloss": {"en": "snake", "tr": "yılan"}, "level": 1},
 "sahir": {"lemma": "سَاحِر", "root": "س ح ر", "pos": "noun", "plural": "سَحَرَة", "gloss": {"en": "magician, sorcerer (ism fa'il)", "tr": "sihirbaz, büyücü (ism-i fâil)"}, "level": 2},
 "habl": {"lemma": "حَبْل", "root": "ح ب ل", "pos": "noun", "plural": "حِبَال", "gloss": {"en": "rope", "tr": "ip, halat"}, "level": 1},
 "harr-hot": {"lemma": "حَارّ", "root": "ح ر ر", "pos": "noun", "gloss": {"en": "hot (ism fa'il of حَرَّ)", "tr": "sıcak (harre'nin ism-i fâili)"}, "level": 1},
 "kabira": {"lemma": "كَبِرَ", "root": "ك ب ر", "pos": "verb", "form": "I", "gloss": {"en": "to grow up, grow big (كَبِرَ يَكْبَرُ)", "tr": "büyümek (كَبِرَ يَكْبَرُ)"}, "level": 1},
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
MORPH["verbs"]["kabira"] = _sg.sound1("samia", "كَبِر", "كْبَر", "اِكْبَر", "كِبَر", "كَبِير",
    note="فَعِلَ يَفْعَلُ — اسْمُ فَاعِلِهِ عَلَى فَعِيلٍ (صِفَةٌ مُشَبَّهَةٌ): كَبِيرٌ.")
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": "musa-wa-firawn",
 "storyGroup": "musa-wa-firawn",
 "title": {"ar": "مُوسَى وَفِرْعَوْنُ", "en": "Musa and Pharaoh", "tr": "Mûsâ ve Firavun"},
 "subtitle": {"ar": "قِصَّةُ مُوسَى لِلْمُبْتَدِئِينَ — جُمَلٌ قَصِيرَةٌ عَلَى طَرِيقَةِ «قِصَصِ النَّبِيِّينَ»",
              "en": "The story of Musa for beginners — short sentences in the manner of the graded readers",
              "tr": "Yeni başlayanlar için Mûsâ kıssası — «Kısasü'n-nebiyyîn» usûlünde kısa cümleler"},
 "level": 1,
 "levelName": "Elementary",
 "version": "0.1.0",
 "published": "2026-11-06",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": [],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِقِصَّةِ مُوسَى كَمَا تُرْوَى لِلْأَطْفَالِ، عَلَى طَرِيقَةِ الْقِرَاءَاتِ الْمُتَدَرِّجَةِ. لَا تُنْقَلُ فِيهَا آيَةٌ بِنَصِّهَا، وَلَيْسَتْ نَصًّا تُرَاثِيًّا.",
  "en": "ORIGINAL Level-1 graded Arabic: a retelling of the story of Musa as it is told to children (after the Qurʾānic narrative in al-Qaṣaṣ, Ṭāhā, al-Shuʿarāʾ and al-Baqara), composed editorially in the manner of Nadwī's graded reader — short كَانَ-framed sentences, one event per line, the vocabulary repeated. No āya is quoted verbatim; no sentence here may be cited as a classical text. The volume of Qiṣaṣ al-Nabiyyīn that tells this story has not been uploaded, so this is the project's own bridge between the Nūḥ and the Shuʿayb volumes.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: Mûsâ kıssasının çocuklara anlatıldığı şekliyle (Kasas, Tâhâ, Şuarâ ve Bakara sûrelerindeki Kur'ân kıssasından hareketle), Nedvî'nin «Kısasü'n-nebiyyîn» usûlünde — kâne ile kurulmuş kısa cümleler, her satırda bir olay, tekrarlanan kelimeler — editoryal olarak telif edilmiştir. Hiçbir âyet aynen aktarılmamıştır; buradaki hiçbir cümle klasik metin diye iktibas edilemez. Kısasü'n-nebiyyîn'in bu kıssayı anlatan cildi yüklenmediği için bu paket, Nûh ve Şuayb ciltleri arasındaki projenin kendi köprüsüdür.",
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
