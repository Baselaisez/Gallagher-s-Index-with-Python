# -*- coding: utf-8 -*-
"""Fill every missing verb paradigm in the corpus.

Two mechanical assembly engines (suffix-attach for sound/hollow/geminate,
a naqis engine for the three defective endings) produce the 14/14/6 tables;
everything lexical — masdar, participles, governed forms, passives, bab —
is stated explicitly per verb in SPEC and merely stored.

The engines are trusted only because they REPRODUCE the hand-authored
paradigms already in the corpus (qala, hajara, daa, baqiya, awsa, rama,
nada, tajalla, istafta, istaadda) cell-for-cell: see selftest().
Copies: paradigms are semantics-free, so a verb already authored in one
package is copied into another after a lemma identity check.
"""
import json, sys, unicodedata
from pathlib import Path

def nfc(x):
    if isinstance(x, str):
        return unicodedata.normalize("NFC", x)
    if isinstance(x, list):
        return [nfc(i) for i in x]
    if isinstance(x, dict):
        return {k: nfc(v) for k, v in x.items()}
    return x

ROOT = Path(__file__).resolve().parents[2] / "content"
DIA = "ًٌٍَُِّْٰ"
def bare(s):
    return "".join(ch for ch in s if ch not in DIA)

# ---------------------------------------------------------------- engines
def mazi14(v, c=None):
    """v: stem before vowel-initial suffixes; c: before consonant-initial."""
    c = c if c is not None else v
    return [v+"َ", v+"َا", v+"ُوا", v+"َتْ", v+"َتَا",
            c+"ْنَ", c+"ْتَ", c+"ْتُمَا", c+"ْتُمْ",
            c+"ْتِ", c+"ْتُمَا", c+"ْتُنَّ", c+"ْتُ", c+"ْنَا"]

def mazi_naqis(b, glide):
    """b ends in a fatha-bearing letter. glide 'w' -> دَعَا family, 'y' -> رَمَى."""
    if glide == "w":
        third, du, fpl, c = b+"ا", b+"وَا", b+"وْنَ", b+"وْ"
    else:
        third, du, fpl, c = b+"ى", b+"يَا", b+"يْنَ", b+"يْ"
    return [third, du, b+"وْا", b+"تْ", b+"تَا",
            fpl, c+"تَ", c+"تُمَا", c+"تُمْ",
            c+"تِ", c+"تُمَا", c+"تُنَّ", c+"تُ", c+"نَا"]

def mazi_naqis_kasra(b, pl3):
    """بَقِيَ family: b ends in kasra-bearing letter, pl3 authored (بَقُوا)."""
    return [b+"يَ", b+"يَا", pl3, b+"يَتْ", b+"يَتَا",
            b+"ينَ", b+"يتَ", b+"يتُمَا", b+"يتُمْ",
            b+"يتِ", b+"يتُمَا", b+"يتُنَّ", b+"يتُ", b+"ينَا"]

def _prefixes(yv):
    return "ي"+yv, "ت"+yv, "أ"+yv, "ن"+yv

def mudari14(yv, L, S=None):
    """Suffix-attach: sound (L==S), hollow (long/short), geminate (contracted/full)."""
    S = S if S is not None else L
    y, t, a, n = _prefixes(yv)
    return [y+L+"ُ", y+L+"َانِ", y+L+"ُونَ", t+L+"ُ", t+L+"َانِ",
            y+S+"ْنَ", t+L+"ُ", t+L+"َانِ", t+L+"ُونَ", t+L+"ِينَ",
            t+L+"َانِ", t+S+"ْنَ", a+L+"ُ", n+L+"ُ"]

NAQIS_ENDS = {
    "i": {"sg": "ِي", "du": "ِيَانِ", "pl": "ُونَ", "fpl": "ِينَ"},
    "u": {"sg": "ُو", "du": "ُوَانِ", "pl": "ُونَ", "fpl": "ُونَ"},
    "a": {"sg": "َى", "du": "َيَانِ", "pl": "َوْنَ", "fpl": "َيْنَ"},
}
def mudari_naqis(yv, bb, typ):
    e = NAQIS_ENDS[typ]
    y, t, a, n = _prefixes(yv)
    fsg2 = "ِينَ" if typ != "a" else "َيْنَ"   # تَمْضِينَ / تَدْعِينَ / تَبْقَيْنَ
    return [y+bb+e["sg"], y+bb+e["du"], y+bb+e["pl"], t+bb+e["sg"], t+bb+e["du"],
            y+bb+e["fpl"], t+bb+e["sg"], t+bb+e["du"], t+bb+e["pl"], t+bb+fsg2,
            t+bb+e["du"], t+bb+e["fpl"], a+bb+e["sg"], n+bb+e["sg"]]

def amr_attach(L, S=None):
    S = S if S is not None else L
    return [S+"ْ", L+"َا", L+"ُوا", L+"ِي", L+"َا", S+"ْنَ"]

def amr_naqis(bb, typ):
    if typ == "i":
        return [bb+"ِ", bb+"ِيَا", bb+"ُوا", bb+"ِي", bb+"ِيَا", bb+"ِينَ"]
    if typ == "u":
        return [bb+"ُ", bb+"ُوَا", bb+"ُوا", bb+"ِي", bb+"ُوَا", bb+"ُونَ"]
    return [bb+"َ", bb+"َيَا", bb+"َوْا", bb+"َيْ", bb+"َيَا", bb+"َيْنَ"]

# ---------------------------------------------------------------- builders
def entry(bab, wazn, masdar, fail, mazi, mudari, amr,
          mansub, majzum, majzum2, maful=None, pmz=None, pmd=None, note=None):
    e = {"bab": bab, "wazn": wazn, "masdar": masdar, "ismFail": fail,
         "mazi": mazi, "mudari": mudari, "amr": amr,
         "mansub": mansub, "majzum": majzum, "majzum2": majzum2}
    if maful: e["ismMaful"] = maful
    if pmz and pmd:
        e["majhulMazi"], e["majhulMudari"] = pmz, pmd
    if note: e["note"] = note
    return nfc(e)

BABS = {
    "nasara": ("مِنْ بَابِ نَصَرَ يَنْصُرُ", "فَعَلَ يَفْعُلُ"),
    "daraba": ("مِنْ بَابِ ضَرَبَ يَضْرِبُ", "فَعَلَ يَفْعِلُ"),
    "fataha": ("مِنْ بَابِ فَتَحَ يَفْتَحُ", "فَعَلَ يَفْعَلُ"),
    "samia":  ("مِنْ بَابِ سَمِعَ يَسْمَعُ", "فَعِلَ يَفْعَلُ"),
}

def sound1(bab, v, core, amr_stem, masdar, fail, maful=None, pmz=None, pmd=None, note=None, cls=""):
    b, w = BABS[bab]
    if cls: b += " — " + cls
    y, t = "يَ", "تَ"
    return entry(b, w, masdar, fail, mazi14(v), mudari14("َ", core),
                 amr_attach(amr_stem), y+core+"َ", y+core+"ْ", t+core+"ْ",
                 maful, pmz, pmd, note)

def hollow1(bab, cls, Lm, Sm, L, S, La, Sa, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    b, w = BABS[bab]
    return entry(b + " — " + cls, w, masdar, fail, mazi14(Lm, Sm),
                 mudari14("َ", L, S), amr_attach(La, Sa),
                 "يَ"+L+"َ", "يَ"+S+"ْ", "تَ"+S+"ْ", maful, pmz, pmd, note)

def naqis1(bab, cls, glide, b_mazi, bb, typ, amr_bb, masdar, fail,
           maful=None, pmz=None, pmd=None, note=None):
    bb_, w = BABS[bab]
    mansub = "يَ"+bb+({"i": "ِيَ", "u": "ُوَ", "a": "َى"}[typ])
    majzum = "يَ"+bb+({"i": "ِ", "u": "ُ", "a": "َ"}[typ])
    majzum2 = "تَ"+bb+({"i": "ِ", "u": "ُ", "a": "َ"}[typ])
    return entry(bb_ + " — " + cls, w, masdar, fail,
                 mazi_naqis(b_mazi, glide), mudari_naqis("َ", bb, typ),
                 amr_naqis(amr_bb, typ), mansub, majzum, majzum2,
                 maful, pmz, pmd, note)

def derived(bab_ar, wazn, yv, v, core, amr_stem, masdar, fail,
            maful=None, pmz=None, pmd=None, note=None):
    y, t = "ي"+yv, "ت"+yv
    return entry(bab_ar, wazn, masdar, fail, mazi14(v), mudari14(yv, core),
                 amr_attach(amr_stem), y+core+"َ", y+core+"ْ", t+core+"ْ",
                 maful, pmz, pmd, note)

def derived_hollow(bab_ar, wazn, yv, Lm, Sm, L, S, La, Sa, masdar, fail,
                   maful=None, pmz=None, pmd=None, note=None):
    y, t = "ي"+yv, "ت"+yv
    return entry(bab_ar, wazn, masdar, fail, mazi14(Lm, Sm), mudari14(yv, L, S),
                 amr_attach(La, Sa), y+L+"َ", y+S+"ْ", t+S+"ْ", maful, pmz, pmd, note)

def derived_naqis(bab_ar, wazn, yv, b_mazi, bb, typ, amr_bb, masdar, fail,
                  maful=None, pmz=None, pmd=None, note=None):
    y, t = "ي"+yv, "ت"+yv
    mansub = y+bb+({"i": "ِيَ", "u": "ُوَ", "a": "َى"}[typ])
    majzum = y+bb+({"i": "ِ", "u": "ُ", "a": "َ"}[typ])
    majzum2 = t+bb+({"i": "ِ", "u": "ُ", "a": "َ"}[typ])
    return entry(bab_ar, wazn, masdar, fail, mazi_naqis(b_mazi, "y"),
                 mudari_naqis(yv, bb, typ), amr_naqis(amr_bb, typ),
                 mansub, majzum, majzum2, maful, pmz, pmd, note)

B2  = "الْبَابُ الثَّانِي: فَعَّلَ يُفَعِّلُ تَفْعِيلًا"
B3  = "بَابُ الْمُفَاعَلَةِ: فَاعَلَ يُفَاعِلُ"
B4  = "الْبَابُ الرَّابِعُ: أَفْعَلَ يُفْعِلُ إِفْعَالًا"
B5  = "بَابُ التَّفَعُّلِ: تَفَعَّلَ يَتَفَعَّلُ"
B6  = "بَابُ التَّفَاعُلِ: تَفَاعَلَ يَتَفَاعَلُ"
B7  = "بَابُ الِانْفِعَالِ: اِنْفَعَلَ يَنْفَعِلُ"
B8  = "بَابُ الِافْتِعَالِ: اِفْتَعَلَ يَفْتَعِلُ"
B10 = "بَابُ الِاسْتِفْعَالِ: اِسْتَفْعَلَ يَسْتَفْعِلُ"
W2, W3, W4 = "فَعَّلَ يُفَعِّلُ", "فَاعَلَ يُفَاعِلُ", "أَفْعَلَ يُفْعِلُ"
W5, W6, W7 = "تَفَعَّلَ يَتَفَعَّلُ", "تَفَاعَلَ يَتَفَاعَلُ", "اِنْفَعَلَ يَنْفَعِلُ"
W8, W10 = "اِفْتَعَلَ يَفْتَعِلُ", "اِسْتَفْعَلَ يَسْتَفْعِلُ"

LAYSA = {
    "jamid": True,
    "bab": "فِعْلٌ مَاضٍ جَامِدٌ",
    "wazn": "فَعِلَ (أَصْلُهُ لَيِسَ)",
    "mazi": ["لَيْسَ", "لَيْسَا", "لَيْسُوا", "لَيْسَتْ", "لَيْسَتَا",
             "لَسْنَ", "لَسْتَ", "لَسْتُمَا", "لَسْتُمْ",
             "لَسْتِ", "لَسْتُمَا", "لَسْتُنَّ", "لَسْتُ", "لَسْنَا"],
    "note": "جَامِدٌ: لَا مُضَارِعَ لَهُ وَلَا أَمْرَ وَلَا مَصْدَرَ — يُصَرَّفُ فِي الْمَاضِي فَقَطْ، وَيَعْمَلُ عَمَلَ كَانَ.",
}
LAYSA = nfc(LAYSA)

NAQIS_Y_NOTE = "نَاقِصٌ يَائِيٌّ: تُحْذَفُ الْيَاءُ فِي الْجَزْمِ — لَمْ يَمْضِ."
NAQIS_W_NOTE = "نَاقِصٌ وَاوِيٌّ: تُحْذَفُ الْوَاوُ فِي الْجَزْمِ — لَمْ يَعْفُ."
HOLLOW_NOTE  = "أَجْوَفُ: تُحْذَفُ عَيْنُهُ قَبْلَ السَّوَاكِنِ — {ex}."

# ---------------------------------------------------------------- SPEC
SAMTI = {}

# --- Form I sound
SAMTI["amada"]   = sound1("daraba", "عَمَد", "عْمِد", "اِعْمِد", "عَمْد", "عَامِد")
SAMTI["badhala"] = sound1("nasara", "بَذَل", "بْذُل", "اُبْذُل", "بَذْل", "بَاذِل",
                          "مَبْذُول", "بُذِلَ", "يُبْذَلُ")
SAMTI["bahatha"] = sound1("fataha", "بَحَث", "بْحَث", "اِبْحَث", "بَحْث", "بَاحِث",
                          "مَبْحُوث عَنْهُ", "بُحِثَ", "يُبْحَثُ")
SAMTI["hamida"]  = sound1("samia", "حَمِد", "حْمَد", "اِحْمَد", "حَمْد", "حَامِد",
                          "مَحْمُود", "حُمِدَ", "يُحْمَدُ")
SAMTI["haqara"]  = sound1("daraba", "حَقَر", "حْقِر", "اِحْقِر", "حَقْر", "حَاقِر",
                          "مَحْقُور", "حُقِرَ", "يُحْقَرُ")
SAMTI["jaala"]   = sound1("fataha", "جَعَل", "جْعَل", "اِجْعَل", "جَعْل", "جَاعِل",
                          "مَجْعُول", "جُعِلَ", "يُجْعَلُ")
SAMTI["kashafa"] = sound1("daraba", "كَشَف", "كْشِف", "اِكْشِف", "كَشْف", "كَاشِف",
                          "مَكْشُوف", "كُشِفَ", "يُكْشَفُ")
SAMTI["marida"]  = sound1("samia", "مَرِض", "مْرَض", "اِمْرَض", "مَرَض", "مَرِيض",
                          note="لَازِمٌ؛ وَالصِّفَةُ الْمُشَبَّهَةُ «مَرِيضٌ» تَقُومُ مَقَامَ اسْمِ الْفَاعِلِ.")
SAMTI["nahada"]  = sound1("fataha", "نَهَض", "نْهَض", "اِنْهَض", "نُهُوض", "نَاهِض")
SAMTI["nasara"]  = sound1("nasara", "نَصَر", "نْصُر", "اُنْصُر", "نَصْر", "نَاصِر",
                          "مَنْصُور", "نُصِرَ", "يُنْصَرُ",
                          note="هَذَا الْفِعْلُ هُوَ مِثَالُ الْبَابِ الْأَوَّلِ نَفْسُهُ.")
SAMTI["qaada"]   = sound1("nasara", "قَعَد", "قْعُد", "اُقْعُد", "قُعُود", "قَاعِد")
SAMTI["qabila"]  = sound1("samia", "قَبِل", "قْبَل", "اِقْبَل", "قَبُول", "قَابِل",
                          "مَقْبُول", "قُبِلَ", "يُقْبَلُ")
SAMTI["rafaa"]   = sound1("fataha", "رَفَع", "رْفَع", "اِرْفَع", "رَفْع", "رَافِع",
                          "مَرْفُوع", "رُفِعَ", "يُرْفَعُ")
SAMTI["saluha"]  = sound1("nasara", "صَلَح", "صْلُح", "اُصْلُح", "صَلَاح", "صَالِح",
                          note="لَازِمٌ؛ وَسُمِعَ أَيْضًا يَصْلَحُ بِالْفَتْحِ.")
SAMTI["shatama"] = sound1("daraba", "شَتَم", "شْتِم", "اِشْتِم", "شَتْم", "شَاتِم",
                          "مَشْتُوم", "شُتِمَ", "يُشْتَمُ")

# --- Form I hollow
SAMTI["ada-visit"] = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "عَاد", "عُد", "عُود", "عُد",
                             "عُود", "عُد", "عِيَادَة", "عَائِد", "مَعُود",
                             "عِيدَ", "يُعَادُ", HOLLOW_NOTE.format(ex="عُدْتَ"))
SAMTI["ghaba"]   = hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "غَاب", "غِب", "غِيب", "غِب",
                           "غِيب", "غِب", "غَيْبَة", "غَائِب",
                           note=HOLLOW_NOTE.format(ex="غِبْتَ"))
SAMTI["hana"]    = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "هَان", "هُن", "هُون", "هُن",
                           "هُون", "هُن", "هَوْن", "هَيِّن",
                           note="لَازِمٌ؛ وَالصِّفَةُ الْمُشَبَّهَةُ «هَيِّنٌ» تَقُومُ مَقَامَ اسْمِ الْفَاعِلِ.")
SAMTI["khada"]   = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "خَاض", "خُض", "خُوض", "خُض",
                           "خُوض", "خُض", "خَوْض", "خَائِض",
                           note=HOLLOW_NOTE.format(ex="خُضْتَ"))
SAMTI["mata-die"] = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "مَات", "مُت", "مُوت", "مُت",
                            "مُوت", "مُت", "مَوْت", "مَيِّت",
                            note="قِيَاسُ اسْمِ الْفَاعِلِ «مَائِتٌ» وَالْمُسْتَعْمَلُ «مَيِّتٌ»؛ وَسُمِعَ مِتَّ بِالْكَسْرِ.")
SAMTI["sada"]    = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "سَاد", "سُد", "سُود", "سُد",
                           "سُود", "سُد", "سِيَادَة", "سَائِد", "مَسُود",
                           note="وَالْمَصْدَرُ الْقَدِيمُ السُّؤْدُدُ.")
SAMTI["shana"]   = hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "شَان", "شِن", "شِين", "شِن",
                           "شِين", "شِن", "شَيْن", "شَائِن", "مَشِين",
                           "شِينَ", "يُشَانُ", HOLLOW_NOTE.format(ex="شِنْتَ"))
SAMTI["zana"]    = hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "زَان", "زِن", "زِين", "زِن",
                           "زِين", "زِن", "زَيْن", "زَائِن",
                           note=HOLLOW_NOTE.format(ex="زِنْتَ"))
SAMTI["zara"]    = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "زَار", "زُر", "زُور", "زُر",
                           "زُور", "زُر", "زِيَارَة", "زَائِر", "مَزُور",
                           "زِيرَ", "يُزَارُ", HOLLOW_NOTE.format(ex="زُرْتَ"))

# --- Form I naqis
SAMTI["mada"] = naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "مَضَ", "مْض", "i", "اِمْض",
                       "مُضِيّ", "مَاضٍ (الْمَاضِي)", note=NAQIS_Y_NOTE)
SAMTI["jara"] = naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "جَرَ", "جْر", "i", "اِجْر",
                       "جَرْي", "جَارٍ (الْجَارِي)",
                       note="نَاقِصٌ يَائِيٌّ: لَمْ يَجْرِ.")
SAMTI["qada"] = naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "قَضَ", "قْض", "i", "اِقْض",
                       "قَضَاء", "قَاضٍ (الْقَاضِي)", "مَقْضِيّ",
                       "قُضِيَ", "يُقْضَى", "نَاقِصٌ يَائِيٌّ: لَمْ يَقْضِ.")
SAMTI["afa"]  = naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "عَفَ", "عْف", "u", "اُعْف",
                       "عَفْو", "عَافٍ (الْعَافِي)", "مَعْفُوٌّ عَنْهُ",
                       "عُفِيَ", "يُعْفَى", NAQIS_W_NOTE)
SAMTI["jafa"] = naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "جَفَ", "جْف", "u", "اُجْف",
                       "جَفَاء", "جَافٍ (الْجَافِي)", "مَجْفُوّ",
                       note="نَاقِصٌ وَاوِيٌّ: لَمْ يَجْفُ.")
SAMTI["waliya"] = entry("مِنْ بَابِ حَسِبَ يَحْسِبُ — لَفِيفٌ مَفْرُوقٌ", "فَعِلَ يَفْعِلُ",
                        "وِلَايَة", "وَالٍ (الْوَالِي)",
                        mazi_naqis_kasra("وَلِ", "وَلُوا"), mudari_naqis("َ", "ل", "i"),
                        amr_naqis("ل", "i"), "يَلِيَ", "يَلِ", "تَلِ",
                        note="لَفِيفٌ مَفْرُوقٌ: تَسْقُطُ الْوَاوُ فِي الْمُضَارِعِ كَوَعَدَ، "
                             "وَتُعَامَلُ الْيَاءُ مُعَامَلَةَ النَّاقِصِ — أَمْرُهُ: لِ.")
SAMTI["laysa"] = LAYSA

# --- geminate Form I
SAMTI["damma-verb"] = entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
                            "ضَمّ", "ضَامّ", mazi14("ضَمّ", "ضَمَم"),
                            mudari14("َ", "ضُمّ", "ضْمُم"),
                            ["ضُمَّ", "ضُمَّا", "ضُمُّوا", "ضُمِّي", "ضُمَّا", "اُضْمُمْنَ"],
                            "يَضُمَّ", "يَضُمَّ", "تَضُمَّ", "مَضْمُوم", "ضُمَّ", "يُضَمُّ",
                            "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ لِلتَّخَلُّصِ مِنَ الْتِقَاءِ السَّاكِنَيْنِ — لَمْ يَضُمَّ، وَيَجُوزُ لَمْ يَضْمُمْ.")
SAMTI["ramma"] = entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
                       "رَمّ", "رَامّ", mazi14("رَمّ", "رَمَم"),
                       mudari14("َ", "رُمّ", "رْمُم"),
                       ["رُمَّ", "رُمَّا", "رُمُّوا", "رُمِّي", "رُمَّا", "اُرْمُمْنَ"],
                       "يَرُمَّ", "يَرُمَّ", "تَرُمَّ", "مَرْمُوم", "رُمَّ", "يُرَمُّ",
                       "مُضَاعَفٌ: لَمْ يَرُمَّ، وَيَجُوزُ لَمْ يَرْمُمْ.")

# --- Form II
SAMTI["arrafa"]  = derived(B2, W2, "ُ", "عَرَّف", "عَرِّف", "عَرِّف", "تَعْرِيف",
                           "مُعَرِّف", "مُعَرَّف", "عُرِّفَ", "يُعَرَّفُ")
SAMTI["baddaa"]  = derived(B2, W2, "ُ", "بَدَّع", "بَدِّع", "بَدِّع", "تَبْدِيع",
                           "مُبَدِّع", "مُبَدَّع", "بُدِّعَ", "يُبَدَّعُ")
SAMTI["dallala"] = derived(B2, W2, "ُ", "ضَلَّل", "ضَلِّل", "ضَلِّل", "تَضْلِيل",
                           "مُضَلِّل", "مُضَلَّل", "ضُلِّلَ", "يُضَلَّلُ")
SAMTI["farragha"] = derived(B2, W2, "ُ", "فَرَّغ", "فَرِّغ", "فَرِّغ", "تَفْرِيغ",
                            "مُفَرِّغ", "مُفَرَّغ", "فُرِّغَ", "يُفَرَّغُ")
SAMTI["qarraba"] = derived(B2, W2, "ُ", "قَرَّب", "قَرِّب", "قَرِّب", "تَقْرِيب",
                           "مُقَرِّب", "مُقَرَّب", "قُرِّبَ", "يُقَرَّبُ")
SAMTI["qassara"] = derived(B2, W2, "ُ", "قَصَّر", "قَصِّر", "قَصِّر", "تَقْصِير", "مُقَصِّر")
SAMTI["wassa"]   = derived_naqis(B2 + " — نَاقِصٌ", W2, "ُ", "وَصَّ", "وَصّ", "i", "وَصّ",
                                 "تَوْصِيَة", "مُوَصٍّ", "مُوَصًّى",
                                 "وُصِّيَ", "يُوَصَّى",
                                 "نَاقِصٌ مِنَ التَّفْعِيلِ: يُوَصِّي ← لَمْ يُوَصِّ.")

# --- Form III
SAMTI["badara"]  = derived(B3, W3, "ُ", "بَادَر", "بَادِر", "بَادِر", "مُبَادَرَة", "مُبَادِر")
SAMTI["hafaza"]  = derived(B3, W3, "ُ", "حَافَظ", "حَافِظ", "حَافِظ", "مُحَافَظَة", "مُحَافِظ")
SAMTI["khadama"] = derived(B3, W3, "ُ", "خَادَم", "خَادِم", "خَادِم", "مُخَادَمَة", "مُخَادِم")
SAMTI["latafa"]  = derived(B3, W3, "ُ", "لَاطَف", "لَاطِف", "لَاطِف", "مُلَاطَفَة",
                           "مُلَاطِف", "مُلَاطَف", "لُوطِفَ", "يُلَاطَفُ")
SAMTI["dara-mudarah"] = derived_naqis(B3 + " — نَاقِصٌ", W3, "ُ", "دَارَ", "دَار", "i", "دَار",
                                      "مُدَارَاة", "مُدَارٍ", "مُدَارًى",
                                      "دُورِيَ", "يُدَارَى",
                                      "نَاقِصٌ مِنَ الْمُفَاعَلَةِ: يُدَارِي ← لَمْ يُدَارِ.")

# --- Form IV
SAMTI["anzala"] = derived(B4, W4, "ُ", "أَنْزَل", "نْزِل", "أَنْزِل", "إِنْزَال",
                          "مُنْزِل", "مُنْزَل", "أُنْزِلَ", "يُنْزَلُ")
SAMTI["aqbala"] = derived(B4, W4, "ُ", "أَقْبَل", "قْبِل", "أَقْبِل", "إِقْبَال", "مُقْبِل")
SAMTI["azhara"] = derived(B4, W4, "ُ", "أَظْهَر", "ظْهِر", "أَظْهِر", "إِظْهَار",
                          "مُظْهِر", "مُظْهَر", "أُظْهِرَ", "يُظْهَرُ")
SAMTI["abda"]   = derived_naqis(B4 + " — نَاقِصٌ", W4, "ُ", "أَبْدَ", "بْد", "i", "أَبْد",
                                "إِبْدَاء", "مُبْدٍ", "مُبْدًى", "أُبْدِيَ", "يُبْدَى",
                                "نَاقِصٌ مِنَ الْإِفْعَالِ: يُبْدِي ← لَمْ يُبْدِ.")
SAMTI["afsha"]  = derived_naqis(B4 + " — نَاقِصٌ", W4, "ُ", "أَفْشَ", "فْش", "i", "أَفْش",
                                "إِفْشَاء", "مُفْشٍ", "مُفْشًى", "أُفْشِيَ", "يُفْشَى",
                                "نَاقِصٌ مِنَ الْإِفْعَالِ: يُفْشِي ← لَمْ يُفْشِ.")
SAMTI["aghatha"] = derived_hollow(B4 + " — أَجْوَفُ", W4, "ُ", "أَغَاث", "أَغَث",
                                  "غِيث", "غِث", "أَغِيث", "أَغِث", "إِغَاثَة",
                                  "مُغِيث", "مُغَاث", "أُغِيثَ", "يُغَاثُ",
                                  "أَجْوَفُ مِنَ الْإِفْعَالِ: يُغِيثُ ← لَمْ يُغِثْ.")
SAMTI["asaba"]  = derived_hollow(B4 + " — أَجْوَفُ", W4, "ُ", "أَصَاب", "أَصَب",
                                 "صِيب", "صِب", "أَصِيب", "أَصِب", "إِصَابَة",
                                 "مُصِيب", "مُصَاب", "أُصِيبَ", "يُصَابُ",
                                 "أَجْوَفُ مِنَ الْإِفْعَالِ: يُصِيبُ ← لَمْ يُصِبْ.")
SAMTI["asaa"] = entry(B4 + " — أَجْوَفُ مَهْمُوزُ اللَّامِ", W4, "إِسَاءَة", "مُسِيء",
                      ["أَسَاءَ", "أَسَاءَا", "أَسَاءُوا", "أَسَاءَتْ", "أَسَاءَتَا",
                       "أَسَأْنَ", "أَسَأْتَ", "أَسَأْتُمَا", "أَسَأْتُمْ",
                       "أَسَأْتِ", "أَسَأْتُمَا", "أَسَأْتُنَّ", "أَسَأْتُ", "أَسَأْنَا"],
                      ["يُسِيءُ", "يُسِيئَانِ", "يُسِيئُونَ", "تُسِيءُ", "تُسِيئَانِ",
                       "يُسِئْنَ", "تُسِيءُ", "تُسِيئَانِ", "تُسِيئُونَ", "تُسِيئِينَ",
                       "تُسِيئَانِ", "تُسِئْنَ", "أُسِيءُ", "نُسِيءُ"],
                      ["أَسِئْ", "أَسِيئَا", "أَسِيئُوا", "أَسِيئِي", "أَسِيئَا", "أَسِئْنَ"],
                      "يُسِيءَ", "يُسِئْ", "تُسِئْ",
                      note="أَجْوَفُ مَهْمُوزُ اللَّامِ: يُسِيءُ ← لَمْ يُسِئْ.")

# --- Form V / VI
SAMTI["tafaqqada"] = derived(B5, W5, "َ", "تَفَقَّد", "تَفَقَّد", "تَفَقَّد",
                             "تَفَقُّد", "مُتَفَقِّد", "مُتَفَقَّد")
SAMTI["taqaddama"] = derived(B5, W5, "َ", "تَقَدَّم", "تَقَدَّم", "تَقَدَّم",
                             "تَقَدُّم", "مُتَقَدِّم")
SAMTI["tawajjaa"]  = derived(B5, W5, "َ", "تَوَجَّع", "تَوَجَّع", "تَوَجَّع",
                             "تَوَجُّع", "مُتَوَجِّع")
SAMTI["taahada"]   = derived(B6, W6, "َ", "تَعَاهَد", "تَعَاهَد", "تَعَاهَد",
                             "تَعَاهُد", "مُتَعَاهِد", "مُتَعَاهَد")
SAMTI["tatawala"]  = derived(B6, W6, "َ", "تَطَاوَل", "تَطَاوَل", "تَطَاوَل",
                             "تَطَاوُل", "مُتَطَاوِل")
SAMTI["taala"] = derived_naqis(B6 + " — نَاقِصٌ", W6, "َ", "تَعَالَ", "تَعَال", "a", "تَعَال",
                               "تَعَالٍ (التَّعَالِي)", "مُتَعَالٍ",
                               note="نَاقِصٌ مِنَ التَّفَاعُلِ؛ فِي حَقِّ اللهِ تَعَالَى "
                                    "يُسْتَعْمَلُ مَاضِيهِ ثَنَاءً — وَأَمْرُهُ لِلْمُخَاطَبِ: تَعَالَ.")

# --- Form VII / VIII
SAMTI["inqabada"] = derived(B7, W7, "َ", "اِنْقَبَض", "نْقَبِض", "اِنْقَبِض",
                            "اِنْقِبَاض", "مُنْقَبِض")
SAMTI["imtahana"] = derived(B8, W8, "َ", "اِمْتَحَن", "مْتَحِن", "اِمْتَحِن",
                            "اِمْتِحَان", "مُمْتَحِن", "مُمْتَحَن", "اُمْتُحِنَ", "يُمْتَحَنُ")
SAMTI["ittasala"] = derived(B8 + " — مِثَالٌ", W8, "َ", "اِتَّصَل", "تَّصِل", "اِتَّصِل",
                            "اِتِّصَال", "مُتَّصِل",
                            note="أَصْلُهُ اِوْتَصَلَ: قُلِبَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ.")
SAMTI["izdada"] = derived_hollow(B8 + " — أَجْوَفُ", W8, "َ", "اِزْدَاد", "اِزْدَد",
                                 "زْدَاد", "زْدَد", "اِزْدَاد", "اِزْدَد",
                                 "اِزْدِيَاد", "مُزْدَاد",
                                 note="أَصْلُهُ اِزْتَيَدَ: أُبْدِلَتْ تَاءُ الِافْتِعَالِ دَالًا بَعْدَ الزَّايِ.")
SAMTI["ihtaja"] = derived_hollow(B8 + " — أَجْوَفُ", W8, "َ", "اِحْتَاج", "اِحْتَج",
                                 "حْتَاج", "حْتَج", "اِحْتَاج", "اِحْتَج",
                                 "اِحْتِيَاج", "مُحْتَاج",
                                 note="أَجْوَفُ مِنَ الِافْتِعَالِ: يَحْتَاجُ ← لَمْ يَحْتَجْ.")

# --- Form X
SAMTI["istamala"]  = derived(B10, W10, "َ", "اِسْتَعْمَل", "سْتَعْمِل", "اِسْتَعْمِل",
                             "اِسْتِعْمَال", "مُسْتَعْمِل", "مُسْتَعْمَل",
                             "اُسْتُعْمِلَ", "يُسْتَعْمَلُ")
SAMTI["istanhada"] = derived(B10, W10, "َ", "اِسْتَنْهَض", "سْتَنْهِض", "اِسْتَنْهِض",
                             "اِسْتِنْهَاض", "مُسْتَنْهِض", "مُسْتَنْهَض")
SAMTI["istansara"] = derived(B10, W10, "َ", "اِسْتَنْصَر", "سْتَنْصِر", "اِسْتَنْصِر",
                             "اِسْتِنْصَار", "مُسْتَنْصِر", "مُسْتَنْصَر")
SAMTI["istaqbala"] = derived(B10, W10, "َ", "اِسْتَقْبَل", "سْتَقْبِل", "اِسْتَقْبِل",
                             "اِسْتِقْبَال", "مُسْتَقْبِل", "مُسْتَقْبَل",
                             "اُسْتُقْبِلَ", "يُسْتَقْبَلُ")
SAMTI["istaghatha"] = derived_hollow(B10 + " — أَجْوَفُ", W10, "َ", "اِسْتَغَاث", "اِسْتَغَث",
                                     "سْتَغِيث", "سْتَغِث", "اِسْتَغِيث", "اِسْتَغِث",
                                     "اِسْتِغَاثَة", "مُسْتَغِيث", "مُسْتَغَاثٌ بِهِ",
                                     note="أَجْوَفُ مِنَ الِاسْتِفْعَالِ: يَسْتَغِيثُ ← لَمْ يَسْتَغِثْ.")
SAMTI["istajadda"] = entry(B10 + " — مُضَاعَفٌ", W10, "اِسْتِجْدَاد", "مُسْتَجِدّ",
                           mazi14("اِسْتَجَدّ", "اِسْتَجْدَد"),
                           mudari14("َ", "سْتَجِدّ", "سْتَجْدِد"),
                           ["اِسْتَجِدَّ", "اِسْتَجِدَّا", "اِسْتَجِدُّوا",
                            "اِسْتَجِدِّي", "اِسْتَجِدَّا", "اِسْتَجْدِدْنَ"],
                           "يَسْتَجِدَّ", "يَسْتَجِدَّ", "تَسْتَجِدَّ", "مُسْتَجَدّ",
                           note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسْتَجِدَّ.")

# --- Chapter 9 verbs (teaching-etiquette section)
SAMTI["istaqarra"] = entry(B10 + " — مُضَاعَفٌ", W10, "اِسْتِقْرَار", "مُسْتَقِرّ",
                           mazi14("اِسْتَقَرّ", "اِسْتَقْرَر"),
                           mudari14("َ", "سْتَقِرّ", "سْتَقْرِر"),
                           ["اِسْتَقِرَّ", "اِسْتَقِرَّا", "اِسْتَقِرُّوا",
                            "اِسْتَقِرِّي", "اِسْتَقِرَّا", "اِسْتَقْرِرْنَ"],
                           "يَسْتَقِرَّ", "يَسْتَقِرَّ", "تَسْتَقِرَّ",
                           note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسْتَقِرَّ.")
SAMTI["alifa"] = sound1("samia", "أَلِف", "أْلَف", "اِئْلَف", "إِلْف", "آلِف",
                        "مَأْلُوف", "أُلِفَ", "يُؤْلَفُ",
                        note="مَهْمُوزُ الْفَاءِ — أَمْرُهُ اِئْلَفْ كَـاِئْذَنْ، وَأَتَكَلَّمُ: آلَفُ كَآخُذُ.")
SAMTI["alifa"]["mudari"][12] = "آلَفُ"   # two hamzas contract to madda, as in آخُذُ
SAMTI["aata"] = derived_naqis(B4 + " — نَاقِصٌ", W4, "ُ", "أَعْطَ", "عْط", "i", "أَعْط",
                              "إِعْطَاء", "مُعْطٍ", "مُعْطًى", "أُعْطِيَ", "يُعْطَى",
                              "نَاقِصٌ مِنَ الْإِفْعَالِ: يُعْطِي ← لَمْ يُعْطِ.")
SAMTI["ikhtalafa"] = derived(B8, W8, "َ", "اِخْتَلَف", "خْتَلِف", "اِخْتَلِف",
                             "اِخْتِلَاف", "مُخْتَلِف")
SAMTI["anasa"] = derived(B4, W4, "ُ", "آنَس", "ؤْنِس", "آنِس", "إِينَاس", "مُؤْنِس",
                         note="مَهْمُوزُ الْفَاءِ مِنَ الْإِفْعَالِ — أَتَكَلَّمُ: أُونِسُ بِقَلْبِ الْهَمْزَةِ السَّاكِنَةِ وَاوًا.")
SAMTI["anasa"]["mudari"][12] = "أُونِسُ"   # two hamzas: the sakin one becomes waw
SAMTI["mazaha"] = derived(B3, W3, "ُ", "مَازَح", "مَازِح", "مَازِح", "مُمَازَحَة", "مُمَازِح")
SAMTI["jalaba"] = sound1("daraba", "جَلَب", "جْلِب", "اِجْلِب", "جَلْب", "جَالِب",
                         "مَجْلُوب", "جُلِبَ", "يُجْلَبُ")
SAMTI["taghafala"] = derived(B6, W6, "َ", "تَغَافَل", "تَغَافَل", "تَغَافَل",
                             "تَغَافُل", "مُتَغَافِل")
SAMTI["rafaqa"] = sound1("nasara", "رَفَق", "رْفُق", "اُرْفُق", "رِفْق", "رَافِق")
SAMTI["amala"] = derived(B3, W3, "ُ", "عَامَل", "عَامِل", "عَامِل", "مُعَامَلَة",
                         "مُعَامِل", "مُعَامَل", "عُومِلَ", "يُعَامَلُ")
SAMTI["adda"] = derived_naqis(B2 + " — نَاقِصٌ", W2, "ُ", "أَدَّ", "ؤَدّ", "i", "أَدّ",
                              "تَأْدِيَة", "مُؤَدٍّ", "مُؤَدًّى", "أُدِّيَ", "يُؤَدَّى",
                              "نَاقِصٌ مِنَ التَّفْعِيلِ: يُؤَدِّي ← لَمْ يُؤَدِّ.")
SAMTI["khana"] = hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "خَان", "خُن", "خُون", "خُن",
                         "خُون", "خُن", "خِيَانَة", "خَائِن",
                         note=HOLLOW_NOTE.format(ex="خُنْتَ"))
SAMTI["tamassaka"] = derived(B5, W5, "َ", "تَمَسَّك", "تَمَسَّك", "تَمَسَّك",
                             "تَمَسُّك", "مُتَمَسِّك")
SAMTI["itasama"] = derived(B8, W8, "َ", "اِعْتَصَم", "عْتَصِم", "اِعْتَصِم",
                           "اِعْتِصَام", "مُعْتَصِم")
SAMTI["raja"] = naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "رَجَ", "رْج", "u", "اُرْج",
                       "رَجَاء", "رَاجٍ (الرَّاجِي)", "مَرْجُوّ",
                       "رُجِيَ", "يُرْجَى", "نَاقِصٌ وَاوِيٌّ: لَمْ يَرْجُ.")
SAMTI["salima"] = sound1("samia", "سَلِم", "سْلَم", "اِسْلَم", "سَلَامَة", "سَالِم")
SAMTI["shaa"] = entry("مِنْ بَابِ فَتَحَ يَفْتَحُ — أَجْوَفُ مَهْمُوزُ اللَّامِ", "فَعَلَ يَفْعَلُ",
                      "مَشِيئَة", "شَاءٍ",
                      ["شَاءَ", "شَاءَا", "شَاءُوا", "شَاءَتْ", "شَاءَتَا",
                       "شِئْنَ", "شِئْتَ", "شِئْتُمَا", "شِئْتُمْ",
                       "شِئْتِ", "شِئْتُمَا", "شِئْتُنَّ", "شِئْتُ", "شِئْنَا"],
                      ["يَشَاءُ", "يَشَاءَانِ", "يَشَاءُونَ", "تَشَاءُ", "تَشَاءَانِ",
                       "يَشَأْنَ", "تَشَاءُ", "تَشَاءَانِ", "تَشَاءُونَ", "تَشَائِينَ",
                       "تَشَاءَانِ", "تَشَأْنَ", "أَشَاءُ", "نَشَاءُ"],
                      ["شَأْ", "شَاءَا", "شَاءُوا", "شَائِي", "شَاءَا", "شَأْنَ"],
                      "يَشَاءَ", "يَشَأْ", "تَشَأْ",
                      note="أَجْوَفُ مَهْمُوزُ اللَّامِ: لَمْ يَشَأْ — وَأَمْرُهُ قَلِيلُ الِاسْتِعْمَالِ.")

# --- Chapter 10 verbs (farewell section)
SAMTI["radiya"] = entry("مِنْ بَابِ سَمِعَ يَسْمَعُ — نَاقِصٌ يَائِيٌّ", "فَعِلَ يَفْعَلُ",
                        "رِضًا (الرِّضَا)", "رَاضٍ (الرَّاضِي)",
                        mazi_naqis_kasra("رَضِ", "رَضُوا"),
                        mudari_naqis("َ", "رْض", "a"), amr_naqis("اِرْض", "a"),
                        "يَرْضَى", "يَرْضَ", "تَرْضَ",
                        "مَرْضِيّ", "رُضِيَ", "يُرْضَى",
                        "نَاقِصٌ كَبَقِيَ: تَسْقُطُ الْيَاءُ مَعَ ضَمَائِرِ الرَّفْعِ — رَضِيتَ، وَجَمْعُهُ رَضُوا.")
SAMTI["istamaa"] = derived(B8, W8, "َ", "اِسْتَمَع", "سْتَمِع", "اِسْتَمِع",
                           "اِسْتِمَاع", "مُسْتَمِع")
SAMTI["kallafa"] = derived(B2, W2, "ُ", "كَلَّف", "كَلِّف", "كَلِّف", "تَكْلِيف",
                           "مُكَلِّف", "مُكَلَّف", "كُلِّفَ", "يُكَلَّفُ")
SAMTI["qaddama"] = derived(B2, W2, "ُ", "قَدَّم", "قَدِّم", "قَدِّم", "تَقْدِيم",
                           "مُقَدِّم", "مُقَدَّم", "قُدِّمَ", "يُقَدَّمُ")
SAMTI["taraha"] = sound1("fataha", "طَرَح", "طْرَح", "اِطْرَح", "طَرْح", "طَارِح",
                         "مَطْرُوح", "طُرِحَ", "يُطْرَحُ")
SAMTI["ashara"] = derived(B3, W3, "ُ", "عَاشَر", "عَاشِر", "عَاشِر", "مُعَاشَرَة",
                          "مُعَاشِر", "مُعَاشَر", "عُوشِرَ", "يُعَاشَرُ")
SAMTI["hazana"] = sound1("nasara", "حَزَن", "حْزُن", "اُحْزُن", "حُزْن", "حَازِن",
                         "مَحْزُون", "حُزِنَ", "يُحْزَنُ",
                         note="الْمُتَعَدِّي: حَزَنَهُ الْأَمْرُ يَحْزُنُهُ؛ وَاللَّازِمُ حَزِنَ يَحْزَنُ.")

# --- Chapter 11 verbs (epilogue)
SAMTI["shayyaa"] = derived(B2, W2, "ُ", "شَيَّع", "شَيِّع", "شَيِّع", "تَشْيِيع",
                           "مُشَيِّع", "مُشَيَّع", "شُيِّعَ", "يُشَيَّعُ")
SAMTI["balagha"] = sound1("nasara", "بَلَغ", "بْلُغ", "اُبْلُغ", "بُلُوغ", "بَالِغ",
                          "مَبْلُوغ", "بُلِغَ", "يُبْلَغُ")
SAMTI["qadima"] = sound1("samia", "قَدِم", "قْدَم", "اِقْدَم", "قُدُوم", "قَادِم")
SAMTI["istalama"] = derived(B10, W10, "َ", "اِسْتَعْلَم", "سْتَعْلِم", "اِسْتَعْلِم",
                            "اِسْتِعْلَام", "مُسْتَعْلِم", "مُسْتَعْلَم",
                            "اُسْتُعْلِمَ", "يُسْتَعْلَمُ")
SAMTI["marra"] = entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
                       "مُرُور", "مَارّ", mazi14("مَرّ", "مَرَر"),
                       mudari14("َ", "مُرّ", "مْرُر"),
                       ["مُرَّ", "مُرَّا", "مُرُّوا", "مُرِّي", "مُرَّا", "اُمْرُرْنَ"],
                       "يَمُرَّ", "يَمُرَّ", "تَمُرَّ",
                       note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَمُرَّ، وَيَجُوزُ لَمْ يَمْرُرْ.")
SAMTI["zahara"] = sound1("fataha", "ظَهَر", "ظْهَر", "اِظْهَر", "ظُهُور", "ظَاهِر")
SAMTI["saqata"] = sound1("nasara", "سَقَط", "سْقُط", "اُسْقُط", "سُقُوط", "سَاقِط")
SAMTI["zala"] = {
    "jamid": True,
    "bab": "مِنْ بَابِ سَمِعَ يَسْمَعُ — أَجْوَفُ، مِنْ أَخَوَاتِ كَانَ",
    "wazn": "فَعِلَ يَفْعَلُ",
    "mazi": mazi14("زَال", "زِل"),
    "mudari": mudari14("َ", "زَال", "زَل"),
    "mansub": "يَزَالَ", "majzum": "يَزَلْ", "majzum2": "تَزَلْ",
    "note": "«مَا زَالَ» الْمُلَازِمَةُ لِلنَّفْيِ: لَا أَمْرَ لَهَا وَلَا مَصْدَرَ مُسْتَعْمَلًا — "
            "وَتَعْمَلُ عَمَلَ كَانَ: مَا زَالَ الْعِلْمُ نُورًا.",
}
SAMTI["zala"] = nfc(SAMTI["zala"])

# ---------------------------------------------------------------- idgham
# The engines attach suffixes blindly; when the root's last radical equals the
# suffix's first letter, orthography demands idgham (كَانَ → كُنَّ، كُنَّا — the
# corpus convention, see kana and istadhana). Applied to the ن-final verbs
# (هَانَ شَانَ زَانَ اِمْتَحَنَ: نْنَ → نَّ) and to مَاتَ (تْتَ → تَّ).
def idgham(e):
    def fix(s):
        for a, b in (("نْنَ", "نَّ"), ("تْتَ", "تَّ"), ("تْتُ", "تُّ"), ("تْتِ", "تِّ")):
            s = s.replace(a, b)
        return s
    for f in ("mazi", "mudari", "amr"):
        e[f] = [fix(c) for c in e[f]]
    return e

for _lex in ("hana", "shana", "zana", "imtahana", "mata-die", "khana", "hazana"):
    SAMTI[_lex] = idgham(SAMTI[_lex])

# ---------------------------------------------------------------- other packages
KAFFARAT = {
    "atama": derived(B4, W4, "ُ", "أَطْعَم", "طْعِم", "أَطْعِم", "إِطْعَام",
                     "مُطْعِم", "مُطْعَم", "أُطْعِمَ", "يُطْعَمُ"),
    "halaqa": sound1("daraba", "حَلَق", "حْلِق", "اِحْلِق", "حَلْق", "حَالِق",
                     "مَحْلُوق", "حُلِقَ", "يُحْلَقُ"),
    "maha": naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "مَحَ", "مْح", "u", "اُمْح",
                   "مَحْو", "مَاحٍ (الْمَاحِي)", "مَمْحُوّ",
                   "مُحِيَ", "يُمْحَى", "نَاقِصٌ وَاوِيٌّ: لَمْ يَمْحُ."),
    "satara": sound1("nasara", "سَتَر", "سْتُر", "اُسْتُر", "سَتْر", "سَاتِر",
                     "مَسْتُور", "سُتِرَ", "يُسْتَرُ"),
}
ABU_YUSUF = {
    "dana": naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "دَنَ", "دْن", "u", "اُدْن",
                   "دُنُوّ", "دَانٍ (الدَّانِي)",
                   note="نَاقِصٌ وَاوِيٌّ: لَمْ يَدْنُ."),
    "laysa": LAYSA,
}
AQAID = {"laysa": LAYSA}

# copy list: target package -> {target lex: (source package, source lex)}
S = "wasiyyat-abi-hanifa-samti"
COPIES = {
    S: {
        "ajaba": "wasiyyat-abi-yusuf-l5", "akhraja": "yunus-wa-al-hut",
        "akrama": "wasiyyat-abi-hanifa", "akthara": "wasiyyat-abi-yusuf-l5",
        "alima": "aqaid-ahl-al-sunna", "ankara": "aqaid-ahl-al-sunna",
        "arafa": "mukhtasar-al-manar", "ata": "wasiyyat-abi-hanifa",
        "azama": "wasiyyat-abi-hanifa-l4", "azzama": "wasiyyat-abi-yusuf-l5",
        "dakhala": "aqaid-ahl-al-sunna", "istataa": "kitab-al-kaffarat",
        "jamaa": "wasiyyat-abi-yusuf-l5", "kana": "aqaid-ahl-al-sunna",
        "kharaja": "wasiyyat-abi-hanifa-l4", "qala": "aqaid-ahl-al-sunna",
        "qasada": "aqaid-ahl-al-sunna", "rahima": "wasiyyat-abi-hanifa",
        "saala": "wasiyyat-abi-yusuf-l5", "sabara": "wasiyyat-abi-hanifa",
        "sahiba": "wasiyyat-abi-hanifa", "samia": "min-muqaddimat-al-maqsud",
        "sara": "wasiyyat-abi-hanifa-l4", "tahawana": "wasiyyat-abi-yusuf-l5",
        "takallama": "wasiyyat-abi-hanifa", "taqarraba": "wasiyyat-abi-yusuf-l5",
        "waqqara": "wasiyyat-abi-yusuf-l5", "wasala": "ashab-al-fil",
        "akhadha": "wasiyyat-abi-yusuf-l5", "atama": "kitab-al-kaffarat",
        "wasala-iii": "wasiyyat-abi-yusuf-l5", "rakiba": "yunus-wa-al-hut",
        "waddaa": "wasiyyat-abi-hanifa", "jaa": "ashab-al-fil",
    },
    "wasiyyat-abi-yusuf-l5": {"raa": "kitab-al-buyu"},
}
COPIES_UPLOADS = {"deeds-are-by-intentions": {"qala": "aqaid-ahl-al-sunna"}}

AUTHORED = {S: SAMTI, "kitab-al-kaffarat": KAFFARAT,
            "wasiyyat-abi-yusuf-l5": ABU_YUSUF, "aqaid-ahl-al-sunna": AQAID}

# ---------------------------------------------------------------- selftest
def load_verbs(pkg, uploads=False):
    d = "user-uploads" if uploads else "samples"
    p = ROOT / d / pkg / "morphology.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"verbs": {}}

def selftest():
    """The engines must reproduce the corpus's hand-authored paradigms."""
    checks = []
    pool = {}
    for pkg in (ROOT / "samples").iterdir():
        for lex, e in load_verbs(pkg.name).get("verbs", {}).items():
            pool.setdefault(lex, e)

    def cmp(name, mine, theirs, fields=("mazi", "mudari", "amr", "mansub", "majzum", "majzum2")):
        for f in fields:
            if f not in theirs:
                continue
            if mine[f] != theirs[f]:
                raise SystemExit(f"SELFTEST FAIL {name}.{f}:\n  mine  ={mine[f]}\n  theirs={theirs[f]}")
        checks.append(name)

    cmp("hajara(sound1)", sound1("nasara", "هَجَر", "هْجُر", "اُهْجُر", "هَجْر", "هَاجِر"),
        pool["hajara"])
    cmp("qala(hollow1)", hollow1("nasara", "x", "قَال", "قُل", "قُول", "قُل",
                                 "قُول", "قُل", "قَوْل", "قَائِل"), pool["qala"])
    cmp("qama(hollow1)", hollow1("nasara", "x", "قَام", "قُم", "قُوم", "قُم",
                                 "قُوم", "قُم", "قِيَام", "قَائِم"), pool["qama"])
    cmp("daa(naqis1-w)", naqis1("nasara", "x", "w", "دَعَ", "دْع", "u", "اُدْع",
                                "دُعَاء", "دَاعٍ"), pool["daa"])
    cmp("rama(naqis1-y)", naqis1("daraba", "x", "y", "رَمَ", "رْم", "i", "اِرْم",
                                 "رَمْي", "رَامٍ"), pool["rama"])
    cmp("baqiya(kasra+a)", entry("x", "x", "بَقَاء", "بَاقٍ",
                                 mazi_naqis_kasra("بَقِ", "بَقُوا"),
                                 mudari_naqis("َ", "بْق", "a"), amr_naqis("اِبْق", "a"),
                                 "يَبْقَى", "يَبْقَ", "تَبْقَ"), pool["baqiya"])
    cmp("awsa(derived_naqis)", derived_naqis("x", "x", "ُ", "أَوْصَ", "وص", "i", "أَوْص",
                                             "إِيصَاء", "مُوصٍ"), pool["awsa"])
    cmp("nada(derived_naqis-III)", derived_naqis("x", "x", "ُ", "نَادَ", "نَاد", "i", "نَاد",
                                                 "مُنَادَاة", "مُنَادٍ"), pool["nada"])
    cmp("tajalla(derived_naqis-V)", derived_naqis("x", "x", "َ", "تَجَلَّ", "تَجَلّ", "a", "تَجَلّ",
                                                  "تَجَلٍّ", "مُتَجَلٍّ"), pool["tajalla"])
    cmp("istafta(derived_naqis-X)", derived_naqis("x", "x", "َ", "اِسْتَفْتَ", "سْتَفْت", "i", "اِسْتَفْت",
                                                  "اِسْتِفْتَاء", "مُسْتَفْتٍ"), pool["istafta"])
    cmp("istaadda(geminate-X)", entry("x", "x", "اِسْتِعْدَاد", "مُسْتَعِدّ",
                                      mazi14("اِسْتَعَدّ", "اِسْتَعْدَد"),
                                      mudari14("َ", "سْتَعِدّ", "سْتَعْدِد"),
                                      pool["istaadda"]["amr"],
                                      pool["istaadda"].get("mansub", ""),
                                      pool["istaadda"].get("majzum", ""),
                                      pool["istaadda"].get("majzum2", "")),
        pool["istaadda"], fields=("mazi", "mudari"))
    cmp("istataa(derived_hollow-X)", derived_hollow("x", "x", "َ", "اِسْتَطَاع", "اِسْتَطَع",
                                                    "سْتَطِيع", "سْتَطِع", "اِسْتَطِيع", "اِسْتَطِع",
                                                    "اِسْتِطَاعَة", "مُسْتَطِيع"), pool["istataa"])
    cmp("anzala-like(akrama IV)", derived(B4, W4, "ُ", "أَكْرَم", "كْرِم", "أَكْرِم",
                                          "إِكْرَام", "مُكْرِم"), pool["akrama"])
    cmp("waddaa(Form II)", derived(B2, W2, "ُ", "وَدَّع", "وَدِّع", "وَدِّع",
                                   "تَوْدِيع", "مُوَدِّع"), pool["waddaa"])
    print(f"selftest: {len(checks)} class reproductions OK: {', '.join(checks)}")

# ---------------------------------------------------------------- apply
def apply():
    total = 0
    for pkg, verbs in AUTHORED.items():
        p = ROOT / "samples" / pkg / "morphology.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        for lex, e in verbs.items():
            if lex not in data["verbs"]:
                data["verbs"][lex] = e
                total += 1
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    def do_copies(copies, uploads):
        nonlocal total
        d = "user-uploads" if uploads else "samples"
        for pkg, mapping in copies.items():
            p = ROOT / d / pkg / "morphology.json"
            data = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"verbs": {}}
            gl = json.loads((ROOT / d / pkg / "glossary.json").read_text(encoding="utf-8"))["entries"]
            for lex, src in mapping.items():
                if lex in data["verbs"]:
                    continue
                e = load_verbs(src)["verbs"][lex]
                # identity check: the copied paradigm must be the same verb
                if bare(e["mazi"][0]) != bare(gl[lex]["lemma"]):
                    raise SystemExit(f"copy mismatch {pkg}:{lex}: "
                                     f"{e['mazi'][0]} vs {gl[lex]['lemma']}")
                data["verbs"][lex] = e
                total += 1
            p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    do_copies(COPIES, uploads=False)
    do_copies(COPIES_UPLOADS, uploads=True)
    print(f"applied: {total} paradigms written")

if __name__ == "__main__":
    selftest()
    if "--apply" in sys.argv:
        apply()
    else:
        # review mode: dump everything authored for eyeballing
        for pkg, verbs in AUTHORED.items():
            for lex, e in sorted(verbs.items()):
                print(f"\n=== {pkg} :: {lex}  ({e['bab']})")
                print(" mazi  :", " ".join(e["mazi"]))
                if not e.get("jamid"):
                    print(" mudari:", " ".join(e["mudari"]))
                    print(" amr   :", " ".join(e["amr"]))
                    print(" gov   :", e.get("mansub"), e.get("majzum"), e.get("majzum2"))
                if e.get("majhulMazi"):
                    print(" majhul:", e["majhulMazi"], e["majhulMudari"])
