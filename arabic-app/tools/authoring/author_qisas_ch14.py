# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 14: «تَأْوِيلُ الرُّؤْيَا، وَرُؤْيَا الْمَلِكِ» — «أَحْسَنُ الْقَصَصِ» sections 12–13 (print pp. 44–47):
the interpretation given to the two prisoners (Yūsuf 12:41, 12:42), the cupbearer's forgetting and the years in prison; the king's
dream of the cows and the ears, the courtiers' dismissal, the cupbearer's visit, and Yūsuf's counsel — seven years of sowing, the
famine, the relief. Every printed line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch14.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "تَأْوِيلُ الرُّؤْيَا، وَرُؤْيَا الْمَلِكِ", "en": "The interpretation of the dream, and the king's dream", "tr": "Rüyanın tabiri ve kralın rüyası"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
# ---------------------------------------------------------------- local helpers (the chapter-8 set, lifted)
def yusuf_fail(punct=None): return fail_name("يُوسُفُ", "yusuf", "«Yūsuf»", "«Yusuf»", punct=punct)
def yaqub_fail(punct=None): return fail_name("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", punct=punct)
def name_ism_kana(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — kāna's ism, in rafʿ; a diptote name.", tr + " — kâne'nin ismi, merfû; gayr-i munsarıf özel isim.", punct=punct)
def yusuf_ism_kana(punct=None): return name_ism_kana("يُوسُفُ", "yusuf", "«Yūsuf»", "«Yusuf»", punct=punct)
def yaqub_ism_kana(punct=None): return name_ism_kana("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", punct=punct)
def name_maful(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "propn", ["maful-bihi", "mamnu-min-sarf"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the object; a diptote name.", tr + " — mef'ûl-i bih; gayr-i munsarıf özel isim.", punct=punct)
def name_mudaf_ilayh(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the muḍāf ilayh, jarr by a fatḥa; a diptote.", tr + " — muzâfun ileyh, fetha ile mecrur; gayr-i munsarıf.", punct=punct)
def li_name(full, lex, en, tr, punct=None, tags=(), role="مُتَعَلِّقٌ بِالْفِعْلِ قَبْلَهُ"):
    return tok(full, lex, "propn", ["huruf-jarr", "mamnu-min-sarf"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالِاسْمُ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ — " + role + ".", "«to " + en + "» — the jarr lām; a diptote name takes a fatḥa for its jarr.", "«" + tr + "'a» — cer lâmı; gayr-i munsarıf özel isim cerde fetha alır.", punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "propn")])
def khabar_kana(full, lex, en, tr, punct=None, tags=(), second=False):
    return tok(full, lex, "noun", [K] + list(tags), ("خَبَرٌ ثَانٍ لِكَانَ" if second else "خَبَرُ كَانَ") + " مَنْصُوبٌ بِالْفَتْحَةِ.", en + (" — a second khabar of kāna, in naṣb." if second else " — kāna's khabar, in naṣb."), tr + (" — kâne'nin ikinci haberi, mansub." if second else " — kâne'nin haberi, mansub."), punct=punct)
def nat_nasb(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["naat-sifa"] + list(tags), "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the naʿt, in naṣb.", tr + " — sıfat, mansub.", punct=punct)
def nat_raf(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["naat-sifa"] + list(tags), "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — the naʿt, in rafʿ.", tr + " — sıfat, merfû.", punct=punct)
def kana_hidden(full="وَكَانَ", wa=True, punct=None):
    return tok(full, "kana", "verb", [K, "hollow-verbs"], W(wa) + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", Wen(wa) + "«he was» — kāna with its ism «he» concealed.", Wtr(wa) + "«o … idi» — kâne; ismi gizli «o».", punct=punct, segments=(wa_("كَانَ", "kana", "verb") if wa else None))
def kanat(full="وَكَانَتِ", wa=True, punct=None):
    return tok(full, "kana", "verb", [K, "hollow-verbs"], W(wa) + "كَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", Wen(wa) + "«was» — kāna with the feminine tāʾ; its kasra is for the meeting of two sukūns.", Wtr(wa) + "«idi» — kâne, te'nis tâ'sı ile; kesresi iki sâkinin karşılaşması içindir.", punct=punct, segments=(wa_("كَانَتِ", "kana", "verb") if wa else None))
def khabar_kana_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", extra="", wa=False, punct=None):
    return tok(full, lex, "verb", [K, "mudari-marfu"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + (extra or "بِالضَّمَّةِ") + f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden} — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", Wen(wa) + en + " — a muḍāriʿ; the clause is kāna's khabar.", Wtr(wa) + tr + " — muzâri; cümle kâne'nin haberidir.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def lahu(full, pron_seg, pron_lex, role_ar, en, tr, tags=(), punct=None):
    return tok(full, "li", "prep", ["huruf-jarr"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — " + role_ar, en, tr, punct=punct, segments=[seg("لَ", "li", "prep"), seg(pron_seg, pron_lex, "pron")])
def kathiran(punct=None):
    return tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ.", "«much, greatly» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct=punct)
def jiddan(punct=None):
    return tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very much» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct=punct)
def fi(punct=None): return tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(): return tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on, upon».", "«üzerine».")
def ila(): return tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e».")
def min_(punct=None, full="مِنْ"): return tok(full, "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ." + ("" if full == "مِنْ" else " (حُرِّكَتْ نُونُهُ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ)"), "«from, of».", "«-den».", punct=punct)
def majrur(full, lex, en, tr, prep, punct=None, tags=(), mudaf=False):
    return tok(full, lex, "noun", ["huruf-jarr"] + (["idafa-definiteness"] if mudaf else []) + list(tags), f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + ("، وَهُوَ مُضَافٌ." if mudaf else "."), en + " — in jarr" + ("; a muḍāf." if mudaf else "."), tr + " — mecrur" + ("; muzâf." if mudaf else "."), punct=punct)
def mudaf_pron(full, lex, pron_seg, pron_lex, role_ar, en, tr, tags=(), punct=None, pos="noun"):
    host = full[:len(full) - len(pron_seg)]
    return tok(full, lex, pos, list(tags) + ["idafa-definiteness"], role_ar + "، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", en + " — annexed to the pronoun.", tr + " — zamire muzâf.", punct=punct, segments=[seg(host, lex, pos), seg(pron_seg, pron_lex, "pron")])
def verb_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), hidden="هُوَ", punct=None, wa=False, mudari=True, extra="", fa=False):
    host = full[:len(full) - len(pron_seg)]
    j = "وَ" if wa else ("فَ" if fa else "")
    segs = ([seg(j, "wa" if wa else "fa", "conj"), seg(host[2:], lex, "verb")] if j else [seg(host, lex, "verb")]) + [seg(pron_seg, pron_lex, "pron")]
    ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")) + ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ" if mudari else "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ") + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + "، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + extra + "."
    return tok(full, lex, "verb", list(tags) + ["maful-bihi"] + (["mudari-marfu"] if mudari else []), ar, Wen(wa) + en + " — the attached pronoun is its object.", Wtr(wa) + tr + " — bitişik zamir mef'ûlüdür.", punct=punct, segments=segs)
def mansub_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), punct=None):
    host = full[:len(full) - len(pron_seg)]
    return tok(full, lex, "verb", ["an-masdariyya", "maful-bihi"] + list(tags), "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", en + " — in naṣb after an; the attached pronoun is its object.", tr + " — en ile mansub; bitişik zamir mef'ûlüdür.", punct=punct, segments=[seg(host, lex, "verb"), seg(pron_seg, pron_lex, "pron")])
def khamsa_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), punct=None, wa=False, extra=""):
    host = full[:len(full) - len(pron_seg)]
    segs = ([seg("وَ", "wa", "conj"), seg(host[2:], lex, "verb")] if wa else [seg(host, lex, "verb")]) + [seg(pron_seg, pron_lex, "pron")]
    return tok(full, lex, "verb", list(tags) + ["afal-khamsa", "mudari-marfu", "maful-bihi"], W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + extra + ".", Wen(wa) + en + " — one of the five verbs; the wāw its doer, the attached pronoun its object.", Wtr(wa) + tr + " — ef'âl-i hamseden; vâv fâil, bitişik zamir mef'ûl.", punct=punct, segments=segs)
def mazi_pl_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), punct=None, wa=False):
    host = full[:len(full) - len(pron_seg)]
    segs = ([seg("وَ", "wa", "conj"), seg(host[2:], lex, "verb")] if wa else [seg(host, lex, "verb")]) + [seg(pron_seg, pron_lex, "pron")]
    return tok(full, lex, "verb", list(tags) + ["maful-bihi"], W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", Wen(wa) + en + " — a māḍī with the group's wāw as doer; the attached pronoun its object.", Wtr(wa) + tr + " — cemi vâvı fâil; bitişik zamir mef'ûl.", punct=punct, segments=segs)
def amr_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), punct=None):
    host = full[:len(full) - len(pron_seg)]
    return tok(full, lex, "verb", list(tags) + ["imperative-amr", "maful-bihi"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", en + " — an imperative built on sukūn; «you» concealed; the attached pronoun its object.", tr + " — sükûn üzere mebnî emir; fâil gizli «sen»; bitişik zamir mef'ûl.", punct=punct, segments=[seg(host, lex, "verb"), seg(pron_seg, pron_lex, "pron")])
def ikhwa(full, case, role_ar, en, tr, punct=None, tags=(), lex="akh"):
    return tok(full, lex, "noun", list(tags) + ["jam-taksir"], role_ar + " " + {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case] + " — جَمْعُ تَكْسِيرٍ.", en + " — a broken plural of أَخ.", tr + " — «kardeş»in cem-i mükesseri.", punct=punct)
def qala_h(full="قَالَ", wa=False, punct=None, fa=False):
    t = qala(full=full, punct=punct, wa=wa, hidden="هُوَ")
    if fa: t["segments"] = [seg("فَ", "fa", "conj"), seg(full[2:], "qala", "verb")]; t["irab"]["ar"] = "الْفَاءُ عَاطِفَةٌ، وَ" + t["irab"]["ar"]
    return t
def maa_pron(full, pron_seg, pron_lex, en, tr, role="مُتَعَلِّقٌ بِالْفِعْلِ قَبْلَهُ", punct=None, tags=()):
    return tok(full, "maa", "noun", ["maful-fih", "idafa-definiteness"] + list(tags), "مَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — " + role + ".", en + " — the adverb «with» annexed to the pronoun.", tr + " — zarf «ile», zamire muzâf.", punct=punct, segments=[seg("مَعَ", "maa", "noun"), seg(pron_seg, pron_lex, "pron")])
def maa_(punct=None):
    return tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with» — an adverb of place, in naṣb; a muḍāf.", "«ile» — mekân zarfı, mansub; muzâf.", punct=punct)
def ya_abana(punct=None):
    return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
            tok("أَبَانَا", "ab", "noun", ["vocative-munada", "five-nouns", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْأَلِفُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَنَا مُضَافٌ إِلَيْهِ.", "«O our father» — the annexed vocative, naṣb by the alif of the five nouns.", "«ey babamız» — muzâf münâdâ, beş isimden olduğu için elif ile mansub.", punct=punct, segments=[seg("أَبَا", "ab", "noun"), seg("نَا", "pron-1p", "pron")])]
def lam_jazim(punct=None, wa=False):
    return tok("وَلَمْ" if wa else "لَمْ", "lam-jazim", "part", ["lam-jazim"], W(wa) + "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", Wen(wa) + "«did not» — negates, puts the verb in jazm and turns it to the past.", Wtr(wa) + "«-medi» — nefiy, cezm ve kalb harfi.", punct=punct, segments=(wa_("لَمْ", "lam-jazim", "part") if wa else None))
def majzum_pl(full, lex, en, tr, tags=(), punct=None):
    return tok(full, lex, "verb", ["lam-jazim", "afal-khamsa"] + list(tags), "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", en + " — in jazm after lam, the nūn dropped; the wāw its doer.", tr + " — lem ile meczum, nûnun hazfi ile; vâv fâil.", punct=punct)
def nahy(full, lex, en, tr, extra="", tags=(), punct=None, wa=False):
    return tok(full, lex, "verb", ["la-nahiya"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + extra + "، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", Wen(wa) + en + " — jazm after the prohibiting lā; «you» concealed.", Wtr(wa) + tr + " — nehiy lâ'sı ile meczum; fâil gizli «sen».", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def la_nahiya_(wa=False):
    return tok("وَلَا" if wa else "لَا", "la-nahiya", "part", ["la-nahiya"], W(wa) + "لَا النَّاهِيَةُ، حَرْفُ جَزْمٍ.", Wen(wa) + "«do not» — the prohibiting lā, a jazm particle.", Wtr(wa) + "«-me» — nehiy lâ'sı, cezm harfi.", segments=(wa_("لَا", "la-nahiya", "part") if wa else None))
def hal_pron(full, lex, en, tr, punct=None):
    return tok(full, lex, "pron", ["hal", "anwa-al-waw", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَالضَّمِيرُ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while " + en + "» — the wāw of ḥāl; the detached pronoun is the mubtadaʾ of the ḥāl clause.", "«" + tr + " iken» — hâl vâvı; munfasıl zamir hâl cümlesinin mübtedâsı.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(full[2:], lex, "pron")])
def khabar_waw(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["mubtada-khabar", "jam-mudhakkar-salim"] + list(tags), "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", en + " — the khabar, rafʿ by the wāw of the sound masculine plural.", tr + " — haber, cem-i müzekker sâlim olduğu için vâv ile merfû.", punct=punct)
def dhib_fail(punct=None): return fail("الذِّئْبُ", "dhib", "«the wolf»", "«kurt»", punct=punct)
def an_(obj_of="أَرَادَ", en_of="«wanted»", tr_of="«istedi»"):
    return tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], f"حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِـ{obj_of}.", f"«that» — the subjunctive maṣdar particle; the clause is the object of {en_of}.", f"«-mesini» — nasb eden masdariyye harfi; te'vilî masdar {tr_of}nin mef'ûlü.")
def sa_mudari(full, lex, en, tr, hidden="هُوَ", tags=(), punct=None, wa=False, extra=""):
    j = "وَ" if wa else ""
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), W(wa) + "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَالْفِعْلُ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + extra + ".", Wen(wa) + en + " — the sīn of the future on a muḍāriʿ in rafʿ.", Wtr(wa) + tr + " — istikbal sîni muzârinin başında; merfû.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("سَ", "sa", "part"), seg(full[len(j) + 1:], lex, "verb")])
def qad_(): return tok("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«indeed» — the particle of confirmation before a past verb.", "«gerçekten» — tahkik harfi.")
def akalahu(punct=None): return verb_enc("أَكَلَهُ", "akala", "هُ", "pron-3ms", "«ate him»", "«onu yedi»", mudari=False, hidden=None, punct=punct)
def hadha_pron_jarr(full, lex, en, tr, punct=None):
    return tok(full, lex, "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", en + " — a demonstrative, built; the muḍāf ilayh.", tr + " — ism-i işâret, mebnî; muzâfun ileyh.", punct=punct)


def ikhwan_fail(punct=None): return ikhwa("الْإِخْوَانُ", "raf", "فَاعِلٌ", "«the brothers» — the doer (the other plural of أَخ)", "«kardeşler» — fâil («kardeş»in diğer cem'i)", tags=["fail"], punct=punct)
def kana_khabar_jarr(full, lex, en, tr, prep, punct=None, tags=()):
    return tok(full, lex, "noun", [K, "huruf-jarr"] + list(tags), f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — in jarr; the phrase is kāna's khabar.", tr + " — mecrur; şibh-i cümle kâne'nin haberi.", punct=punct)
def mazi_pl_naqis(full, lex, en, tr, tags=(), punct=None, wa=False):
    return tok(full, lex, "verb", ["naqis-verbs"] + list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ.", Wen(wa) + en + " — a nāqiṣ māḍī: its alif dropped before the group's wāw.", Wtr(wa) + tr + " — nâkıs mâzî: elifi cemi vâvından önce düşmüş.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def fa_mazi(full, lex, en, tr, hidden="هُوَ", tags=(), punct=None, extra_ar=""):
    t = mazi(full, lex, en, tr, hidden=hidden, tags=["atf-nasaq"] + list(tags), punct=punct, extra_ar=extra_ar)
    t["segments"] = [seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")]; t["irab"]["ar"] = "الْفَاءُ عَاطِفَةٌ، وَ" + t["irab"]["ar"]; t["irab"]["en"] = "«and so» + " + t["irab"]["en"]; t["irab"]["tr"] = "«böylece» + " + t["irab"]["tr"]
    return t


def aziz_fail(punct=None): return fail("الْعَزِيزُ", "aziz", "«the ʿAzīz»", "«Aziz»", punct=punct)
def imraat_aziz(role_ar, en, tr, case="raf", punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ"}[case]
    return [tok("امْرَأَةُ" if case == "raf" else "امْرَأَةَ", "imraa", "noun", list(tags) + ["idafa-definiteness"], role_ar + " " + C + "، وَهُوَ مُضَافٌ.", en + " — a muḍāf.", tr + " — muzâf."),
            tok("الْعَزِيزِ", "aziz", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the ʿAzīz» — the muḍāf ilayh.", "«Aziz» — muzâfun ileyh.", punct=punct)]
def ila_sijn(punct=None, role="مُتَعَلِّقٌ بِالْفِعْلِ قَبْلَهُ"):
    return [ila(), tok("السِّجْنِ", "sijn", "noun", ["huruf-jarr"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — " + role + ".", "«the prison» — in jarr.", "«hapishane» — mecrur.", punct=punct)]
def fa_idha(): return tok("فَإِذَا", "idha", "part", ["idha-shartiyya"], "الْفَاءُ عَاطِفَةٌ، وَإِذَا لِلْمُفَاجَأَةِ — حَرْفٌ (أَوْ ظَرْفُ مَكَانٍ) لَا يَلِيهِ إِلَّا جُمْلَةٌ اسْمِيَّةٌ.", "«and lo!» — the idhā of surprise; only a nominal sentence follows it.", "«bir de ne görsün» — mufâcee idhâ'sı; ardından yalnız isim cümlesi gelir.", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")])
def man_istif(): return tok("مَنْ", "man-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the question noun as mubtadaʾ.", "«kim» — istifham ismi, mübtedâ.")
def yashtari(): return tok("يَشْتَرِي", "ishtara", "verb", ["mubtada-khabar", "mudari-marfu", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«buys» — a muḍāriʿ, the ḍamma estimated on the yāʾ; the clause is the khabar.", "«satın alır» — muzâri, zamme yâ üzerinde takdîrî; cümle haberdir.")
def hadha_ghulam(punct=None):
    return [ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"), tok("الْغُلَامَ", "ghulam", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«boy» — the badal of the demonstrative, in naṣb.", "«çocuğu» — ism-i işâretin bedeli, mansub.", punct=punct)]
# ---------------------------------------------------------------- chapter-12 helpers
def ahl_sijn(role_ar, en, tr, punct=None, tags=()):
    return [tok("أَهْلُ", "ahl", "noun", list(tags) + ["idafa-definiteness"], role_ar + " مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the people (of)» — " + en + "; a muḍāf.", "«ehli» — " + tr + "; muzâf."),
            tok("السِّجْنِ", "sijn", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the prison» — the muḍāf ilayh.", "«zindan» — muzâfun ileyh.", punct=punct)]
def name_ism_anna(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the ism of anna; a diptote name.", tr + " — enne'nin ismi; gayr-i munsarıf özel isim.", punct=punct)
def dual_mazi(full, lex, en, tr, tags=(), punct=None, wa=True, extra=""):
    host = full[2:] if wa else full
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرُ الِاثْنَيْنِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + extra + ".", Wen(wa) + en + " — a māḍī; the alif of the two is its doer.", Wtr(wa) + tr + " — mâzî; tesniye elifi fâildir.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(host[:-1], lex, "verb"), seg("ا", "pron-3md", "pron")])
def mudari_1s(full, lex, en, tr, tags=(), punct=None, extra=""):
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا" + extra + ".", en + " — a muḍāriʿ; the doer «I» is concealed of necessity.", tr + " — muzari; fâil vücûben gizli «ben».", punct=punct)
def alaysa(punct=None):
    return tok("أَلَيْسَ", "laysa", "verb", ["al-istifham", K, "khuruj-al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«are … not?» — the question hamza (expecting «yes») over the frozen laysa.", "«… değil mi?» — takrîrî istifham hemzesi, câmid nâkıs fiil leyse.", punct=punct, segments=[seg("أَ", "hamza-istifham", "part"), seg("لَيْسَ", "laysa", "verb")])
def ala_q(punct=None):
    return tok("أَلَا", "hamza-istifham", "part", ["al-istifham", "khuruj-al-istifham", "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَا نَافِيَةٌ.", "«do … not?» — the question hamza over the negating lā: a question that affirms.", "«… değil mi?» — nefiy lâ'sı üzerinde takrîrî istifham hemzesi.", punct=punct, segments=[seg("أَ", "hamza-istifham", "part"), seg("لَا", "la-nafiya", "part")])
def lakinnahu(punct=None):
    return tok("وَلٰكِنَّهُ", "lakinna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«but he» — lākinna with its pronoun ism.", "«fakat o» — lâkinne, zamir ismi.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُ", "pron-3ms", "pron")])
def kana_khabar_lakinna(punct=None):
    return tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "inna-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", "«he was» — kāna with «he» concealed; the clause is lākinna's khabar.", "«o … idi» — kâne; ismi gizli; cümle lâkinne'nin haberi.", punct=punct)
def kana_bare(punct=None):
    return tok("كَانَ", "kana", "verb", [K, "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«was» — kāna: it raises its ism and puts its khabar in naṣb.", "«idi» — kâne: ismini ref, haberini nasb eder.", punct=punct)
def fi_sijn_khabar(punct=None, of="كَانَ"):
    return [tok("فِي", "fi", "prep", ["huruf-jarr", K], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ " + of + ".", "«in» — the phrase is the khabar of " + ("kāna" if of == "كَانَ" else of) + ".", "«-de» — şibh-i cümle " + ("kâne'nin" if of == "كَانَ" else of) + " haberi."),
            majrur("السِّجْنِ", "sijn", "«the prison»", "«zindan»", "فِي", punct=punct)]
def kulli_(noun_full, noun_lex, noun_en, noun_tr, punct=None):
    return [tok("كُلِّ", "kull", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«every» — in jarr after fī; a muḍāf.", "«her» — fî ile mecrur; muzâf."),
            tok(noun_full, noun_lex, "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", noun_en + " — the muḍāf ilayh.", noun_tr + " — muzâfun ileyh.", punct=punct)]


# ---------------------------------------------------------------- chapter-13 helpers
def li_al(full, lex, en, tr, punct=None, role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ"):
    return tok(full, lex, "propn", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ (دَخَلَتِ اللَّامُ عَلَى الْأَلِفِ فَحُذِفَتْ) — " + role + ".", en + " — the lām of jarr swallowing the article's alif; the phrase is the khabar.", tr + " — cer lâmı harf-i tarifin elifini yutmuş; şibh-i cümle haber.", punct=punct, segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")])
def mazi_1s(full, lex, en, tr, tags=(), punct=None, extra="", wa=False):
    host = full[2:] if wa else full
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرُ الْمُتَكَلِّمِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + extra + ".", Wen(wa) + en + " — a māḍī on sukūn before the speaker's tāʾ, which is its doer.", Wtr(wa) + tr + " — fâil tâ'sından önce sükûn üzere mâzî; tâ fâildir.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(host[:-2], lex, "verb"), seg("تُ", "pron-1s", "pron")])
def lahuma(punct=None, role="مُتَعَلِّقٌ بِالْفِعْلِ قَبْلَهُ"):
    return lahu("لَهُمَا", "هُمَا", "pron-3d", role + ".", "«to the two of them».", "«o ikisine».", punct=punct)
def rabb_khabar(punct=None, first=False):
    return tok("رَبُّ" if first else "وَرَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"] + ([] if first else ["atf-nasaq"]), ("" if first else "الْوَاوُ عَاطِفَةٌ، وَ") + ("خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هٰذَا، مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ." if first else "رَبُّ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ."), ("«the lord (of)» — the khabar of an omitted «this»; a muḍāf." if first else "«and the lord (of)» — joined; a muḍāf."), ("«rabbi» — hazfedilmiş «bu»nun haberi; muzâf." if first else "«ve rabbi» — matuf; muzâf."), punct=punct, segments=(None if first else [seg("وَ", "wa", "conj"), seg("رَبُّ", "rabb", "noun")]))
def rabb_mubt(punct=None, first=False):
    return tok("رَبُّ" if first else "وَرَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"] + ([] if first else ["atf-nasaq"]), ("" if first else "الْوَاوُ عَاطِفَةٌ، وَ") + ("مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ." if first else "رَبُّ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ."), ("«the lord (of)» — the delayed mubtadaʾ; a muḍāf." if first else "«and the lord (of)» — joined; a muḍāf."), ("«rabbi» — geciktirilmiş mübtedâ; muzâf." if first else "«ve rabbi» — matuf; muzâf."), punct=punct, segments=(None if first else [seg("وَ", "wa", "conj"), seg("رَبُّ", "rabb", "noun")]))
def mi(full, lex, en, tr, punct=None):
    return tok(full, lex, "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", en + " — the muḍāf ilayh.", tr + " — muzâfun ileyh.", punct=punct)
def four_lords(khabar=True, punct="."):
    f = rabb_khabar if khabar else rabb_mubt
    return [f(first=True), mi("الْبَرِّ", "barr", "«the land»", "«kara»"), f(), mi("الْبَحْرِ", "bahr", "«the sea»", "«deniz»"), f(), mi("الرِّزْقِ", "rizq", "«provision»", "«rızık»"), f(), mi("الْمَطَرِ", "matar", "«the rain»", "«yağmur»", punct=punct)]
def wa_lakinna(punct=None):
    return tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«but» — lākinna, a sister of inna.", "«fakat» — lâkinne, inne'nin kız kardeşi.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")])
def akthar_nas():
    return [tok("أَكْثَرَ", "akthar", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«most (of)» — the ism of lākinna; a muḍāf.", "«çoğu» — lâkinne'nin ismi; muzâf."), mi("النَّاسِ", "nas", "«the people»", "«insanlar»")]
def allamani_rabbi(punct=None, extra=""):
    return [verb_enc("عَلَّمَنِي", "allama", "نِي", "pron-1s", "«taught me»", "«bana öğretti»", mudari=False, hidden=None, tags=["form-ii-verbs", "ya-al-mutakallim"], extra=extra),
            tok("رَبِّي", "rabb", "noun", ["fail", "ya-al-mutakallim", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the doer, its ḍamma estimated before the speaker's yāʾ.", "«Rabbim» — fâil; zammesi mütekellim yâ'sından önce takdîrî.", punct=punct, segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")])]
def dhalikuma():
    return tok("ذٰلِكُمَا", "dhalika", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْكَافُ لِلْخِطَابِ وَالْمِيمُ وَالْأَلِفُ لِلتَّثْنِيَةِ.", "«that (you two)» — the demonstrative, the mubtadaʾ; its kāf addresses the two.", "«işte bu (ikinize)» — ism-i işâret, mübtedâ; kâfı tesniye muhâtaplarına.")
def mimma():
    return tok("مِمَّا", "min", "prep", ["huruf-jarr", "ism-mawsul", "mubtada-khabar"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«of what» — min fused with the relative mā; the phrase is the khabar.", "«-den» — min ile ism-i mevsûl mâ bitişik; şibh-i cümle haber.", segments=[seg("مِمْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")])
def amr_pl(full, lex, en, tr, tags=(), punct=None, wa=False, fa=False, extra=""):
    j = "وَ" if wa else ("فَ" if fa else "")
    return tok(full, lex, "verb", ["imperative-amr"] + list(tags), (("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "الْفَاءُ عَاطِفَةٌ، وَ") if j else "") + "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ" + extra + ".", (Wen(wa) if wa else ("«and so» + " if fa else "")) + en + " — a plural imperative, built on the dropped nūn; the wāw is the doer.", (Wtr(wa) if wa else ("«ve» + " if fa else "")) + tr + " — nûnun hazfi üzere mebnî cemi emir; vâv fâildir.", punct=punct, segments=([seg(j, "wa" if wa else "fa", "conj"), seg(full[2:], lex, "verb")] if j else None))
def ila_al(full, lex, en, tr, punct=None, wa=False):
    return [tok("وَإِلَى" if wa else "إِلَى", "ila", "prep", ["huruf-jarr"] + (["atf-nasaq"] if wa else []), W(wa) + "حَرْفُ جَرٍّ.", Wen(wa) + "«to».", Wtr(wa) + "«-e».", segments=(wa_("إِلَى", "ila", "prep") if wa else None)), majrur(full, lex, en, tr, "إِلَى", punct=punct)]


# ---------------------------------------------------------------- chapter-14 helpers
def khabar_mudari(full, lex, tags, en, tr, punct=None, hidden="هُوَ"):
    return tok(full, lex, "verb", ["mubtada-khabar", "mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden} — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", en + " — a muḍāriʿ, its ḍamma estimated; the clause is the khabar.", tr + " — muzâri, zammesi takdîrî; cümle haberdir.", punct=punct)
def nat_jarr(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", ["naat-sifa"] + list(tags), "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".", en + " — the naʿt, in jarr.", tr + " — sıfat, mecrur.", punct=punct)
def sab_maful(full="سَبْعَ", punct=None, wa=False, zarf=False):
    ar = ("ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ" if zarf else "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — اسْمُ عَدَدٍ")
    if wa: ar = "الْوَاوُ عَاطِفَةٌ، وَسَبْعَ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — اسْمُ عَدَدٍ"
    return tok(full, "sab-seven", "noun", (["atf-nasaq"] if wa else []) + (["maful-fih"] if zarf else ["maful-bihi"]) + ["idafa-definiteness"], ar + ".", Wen(wa) + "«seven» — " + ("an adverb of time" if zarf else ("joined, in naṣb" if wa else "the object")) + "; a muḍāf (the number 3–10 annexes its counted noun, a plural in jarr).", Wtr(wa) + "«yedi» — " + ("zaman zarfı" if zarf else ("ma'tûf, mansub" if wa else "mef'ûl")) + "; muzâf (3–10 arası sayı, ma'dûdunu cemi mecrur olarak muzâfun ileyh yapar).", punct=punct, segments=(wa_("سَبْعَ", "sab-seven", "noun") if wa else None))
def madud(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["idafa-definiteness", "jam-muannath-salim"] + list(tags), "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، وَهُوَ الْمَعْدُودُ.", en + " — the counted noun as muḍāf ilayh; a sound feminine plural.", tr + " — ma'dûd, muzâfun ileyh; cem-i müennes sâlim.", punct=punct)
def sinin(full="سِنِينَ", role="مُضَافٌ إِلَيْهِ مَجْرُورٌ", sign="الْيَاءُ", en="«years»", tr="«yıl»", punct=None, tags=(), en_role="the muḍāf ilayh", tr_role="muzâfun ileyh"):
    return tok(full, "sana", "noun", list(tags) + ["jam-mudhakkar-salim"], role + " وَعَلَامَةُ " + ("جَرِّهِ" if "مَجْرُور" in role else "نَصْبِهِ") + " " + sign + " لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", en + " — " + en_role + "; سِنُونَ is attached to the sound masculine plural and declines by its letter.", tr + " — " + tr_role + "; سِنُونَ cem-i müzekker sâlime mülhaktır, harfle i'rab olunur.", punct=punct)
def saqi_fail(full="السَّاقِي", wa=False, punct=None):
    return tok(full, "saqi", "noun", ["fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.", "«the cupbearer» — the doer; a manqūṣ, its ḍamma estimated on the yāʾ.", "«sâkî» — fâil; ism-i mankûs, zammesi yâ üzerinde takdîrîdir.", punct=punct)
def malik_(full, case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok(full, "malik-king", "noun", list(tags), role_ar + " " + C + ".", en, tr, punct=punct)
def tawil_jarr(full="بِتَأْوِيلِ", prep="بِ", en="«with the interpretation (of)»", tr="«tabiriyle»", punct=None, tags=()):
    p = {"بِ": "bi", "عَنْ": None}[prep]
    segs = [seg("بِ", "bi", "prep"), seg("تَأْوِيلِ", "tawil", "noun")] if prep == "بِ" else None
    return tok(full, "tawil", "noun", ["huruf-jarr", "idafa-definiteness"] + list(tags), ("الْبَاءُ حَرْفُ جَرٍّ، وَتَأْوِيلِ " if prep == "بِ" else "") + f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", en + " — in jarr; a muḍāf.", tr + " — mecrur; muzâf.", punct=punct, segments=segs)
def ruya_mi(full="الرُّؤْيَا", punct=None, pron=None):
    if pron:
        return tok(full, "ruya-dream", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«his dream» — the muḍāf ilayh (a maqṣūr: its kasra estimated), itself annexed to the pronoun.", "«rüyası» — muzâfun ileyh (maksûr: kesresi takdîrî), zamire muzâf.", punct=punct, segments=[seg("رُؤْيَا", "ruya-dream", "noun"), seg(pron, "pron-3ms", "pron")])
    return tok(full, "ruya-dream", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ.", "«the dream» — the muḍāf ilayh; a maqṣūr, its kasra estimated on the alif.", "«rüya» — muzâfun ileyh; maksûr, kesresi elif üzerinde takdîrî.", punct=punct)
def an_sijn(punct=None): return [ila(), tok("السِّجْنِ", "sijn", "noun", ["huruf-jarr"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — مُتَعَلِّقٌ بِذَهَبَ.", "«the prison» — in jarr.", "«zindan» — mecrur.", punct=punct)]
def hadhihi_(case, punct=None, tags=()):
    C = {"nasb": "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ", "jarr": "فِي مَحَلِّ جَرٍّ"}[case]
    return tok("هٰذِهِ", "hadhihi", "pron", ["asma-al-ishara"] + list(tags), "اسْمُ إِشَارَةٍ مَبْنِيٌّ " + C + ".", "«these / this» — a demonstrative, built; " + ("the object, fronted." if case == "nasb" else "in the place of jarr."), "«bu» — ism-i işâret, mebnî; " + ("mukaddem mef'ûl." if case == "nasb" else "mahallen mecrur."), punct=punct)
def badal_(full, lex, case, en, tr, punct=None, extra="", sign=None):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    if sign: C = sign
    return tok(full, lex, "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ " + C + extra + ".", en + " — the badal of the demonstrative.", tr + " — ism-i işâretin bedeli.", punct=punct)

# ================================================================ §12 تأويل الرؤيا (pp. 44–45)
sen("s1", "And when Yūsuf had finished his sermon, he told the two of them the interpretation of the dream.", "Yusuf vaazını bitirince, ikisine rüyanın tabirini haber verdi.", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw", "idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، فِي مَحَلِّ نَصْبٍ.", "«and when» — the resumptive wāw; lammā is a time adverb carrying the sense of a condition.", "«ve …-ince» — istînâf vâvı; lemmâ şart manası taşıyan zaman zarfı.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("فَرَغَ", "faragha", "«had finished»", "«bitirdi»", hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ"), yusuf_fail(),
  min_(), mudaf_pron("مَوْعِظَتِهِ", "mawiza", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his sermon» — in jarr", "«vaazı» — mecrur", tags=["huruf-jarr"]),
  tok("أَخْبَرَهُمَا", "akhbara", "verb", ["maful-bihi", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — جَوَابُ لَمَّا.", "«he told the two of them» — a māḍī, «he» concealed; the dual pronoun its object; lammā's answer.", "«ikisine haber verdi» — mâzî, fâil gizli «o»; tesniye zamiri mef'ûl; lemmâ'nın cevabı.", segments=[seg("أَخْبَرَ", "akhbara", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  tawil_jarr(), ruya_mi(punct=".")])
sen("s2", "He said: «As for one of you two, he will serve his master wine.» (Yūsuf 12:41)", "Dedi: «İkinizden birine gelince, efendisine şarap sunacak.» (Yûsuf 12:41)", [
  qala(hidden="هُوَ"), *quran([
  tok("أَمَّا", "amma", "part", ["amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ، جَوَابُهُ مَقْرُونٌ بِالْفَاءِ.", "«as for» — the particle of detailing; its answer takes the fāʾ.", "«-e gelince» — tafsîl harfi; cevabı fâ ile gelir."),
  tok("أَحَدُكُمَا", "ahad", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«one of you two» — the mubtadaʾ, annexed to the dual pronoun.", "«ikinizden biri» — mübtedâ, tesniye zamirine muzâf.", segments=[seg("أَحَدُ", "ahad", "noun"), seg("كُمَا", "pron-2d", "pron")]),
  tok("فَيَسْقِي", "saqa-water", "verb", ["amma-tafsiliyya", "mudari-marfu", "naqis-verbs", "mubtada-khabar"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَيَسْقِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«then he will serve (drink)» — the fāʾ of ammā's answer; a nāqiṣ muḍāriʿ, its ḍamma estimated; the clause is the khabar.", "«o … sunacak» — emmâ'nın cevap fâsı; nâkıs muzâri, zammesi takdîrî; cümle haberdir.", segments=[seg("فَ", "fa", "conj"), seg("يَسْقِي", "saqa-water", "verb")]),
  mudaf_pron("رَبَّهُ", "rabb", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ", "«his master» — the first object", "«efendisine» — birinci mef'ûl", tags=["maful-bihi"]),
  tok("خَمْرًا", "khamr", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«wine» — the second object of سَقَى.", "«şarap» — sakâ'nın ikinci mef'ûlü.", punct=".")])])
sen("s3", "«And as for the other, he will be crucified, and the birds will eat from his head.» (Yūsuf 12:41)", "«Diğerine gelince, asılacak ve kuşlar başından yiyecek.» (Yûsuf 12:41)", quran([
  tok("وَأَمَّا", "amma", "part", ["atf-nasaq", "amma-tafsiliyya"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for» — the second share of the detailing.", "«diğerine gelince» — tafsîlin ikinci payı.", segments=wa_("أَمَّا", "amma", "part")),
  tok("الْآخَرُ", "akhar", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the other» — the mubtadaʾ.", "«diğeri» — mübtedâ."),
  tok("فَيُصْلَبُ", "salaba-crucify", "verb", ["amma-tafsiliyya", "naib-al-fail", "mubtada-khabar"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَيُصْلَبُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«then he will be crucified» — the fāʾ of ammā's answer; a passive muḍāriʿ, its deputy doer «he» concealed; the clause is the khabar.", "«asılacak» — emmâ'nın cevap fâsı; meçhul muzâri, nâib-i fâil gizli «o»; cümle haberdir.", segments=[seg("فَ", "fa", "conj"), seg("يُصْلَبُ", "salaba-crucify", "verb")]),
  tok("فَتَأْكُلُ", "akala", "verb", ["atf-nasaq", "mudari-marfu"], "الْفَاءُ عَاطِفَةٌ، وَتَأْكُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and (so) eat» — joined by fāʾ; a muḍāriʿ in rafʿ (its doer follows).", "«ve yer» — fâ ile ma'tûf; merfû muzâri (fâili sonra gelir).", segments=[seg("فَ", "fa", "conj"), seg("تَأْكُلُ", "akala", "verb")]),
  fail("الطَّيْرُ", "tayr", "«the birds»", "«kuşlar»", extra_ar=" — اسْمُ جِنْسٍ جَمْعِيٌّ، يُؤَنَّثُ فِعْلُهُ"),
  min_(), mudaf_pron("رَأْسِهِ", "ras", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his head» — in jarr", "«başı» — mecrur", tags=["huruf-jarr"], punct=".")]))
sen("s4", "And he said to the first: «Mention me before your master.» (Yūsuf 12:42)", "Birincisine dedi: «Beni efendinin yanında an.» (Yûsuf 12:42)", [
  qala(full="وَقَالَ", wa=True, hidden="هُوَ", punct=None),
  tok("لِلْأَوَّلِ", "awwal", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَوَّلِ مَجْرُورٌ بِالْكَسْرَةِ (دَخَلَتِ اللَّامُ عَلَى الْأَلِفِ فَحُذِفَتْ) — مُتَعَلِّقٌ بِقَالَ.", "«to the first» — the jarr lām swallowing the article's alif.", "«birincisine» — cer lâmı, harf-i tarifin elifini yutar.", punct=":", segments=[seg("لِ", "li", "prep"), seg("لْأَوَّلِ", "awwal", "noun")]),
  *quran([
  tok("اُذْكُرْنِي", "dhakara", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«mention me» — an imperative on sukūn; «you» concealed; the nūn of protection, then the speaker's yāʾ as object.", "«beni an» — sükûn üzere mebnî emir; fâil gizli «sen»; vikâye nûnu, mütekellim yâsı mef'ûl.", segments=[seg("اُذْكُرْ", "dhakara", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«before, with» — an adverb of place; a muḍāf.", "«yanında» — mekân zarfı; muzâf."),
  mudaf_pron("رَبِّكَ", "rabb", "كَ", "pron-2ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "«your master» — the muḍāf ilayh", "«efendin» — muzâfun ileyh", punct=".")])])
sen("s5", "And the two men went out; so the first became a cupbearer to the king, and the other was crucified.", "İki adam çıktı; birincisi krala sâkî oldu, diğeri ise asıldı.", [
  mazi("وَخَرَجَ", "kharaja", "«went out»", "«çıktı»", hidden=None, wa=True),
  tok("الرَّجُلَانِ", "rajul", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى.", "«the two men» — the doer; the dual's rafʿ shows as an alif.", "«iki adam» — fâil; tesniyenin ref'i elifle.", punct="،"),
  tok("فَكَانَ", "kana", "verb", [K, "hollow-verbs", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«so … became» — kāna after the fāʾ of sequence.", "«böylece … oldu» — tertip fâsından sonra kâne.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("الْأَوَّلُ", "awwal", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the first» — kāna's ism.", "«birincisi» — kâne'nin ismi."),
  tok("سَاقِيًا", "saqi", "noun", [K, "ism-maqsur-manqus"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ — الْمَنْقُوصُ تَظْهَرُ فَتْحَتُهُ.", "«a cupbearer» — kāna's khabar; the manqūṣ shows its fatḥa on the yāʾ.", "«sâkî» — kâne'nin haberi; mankûsun fethası yâ üzerinde zâhirdir.", punct=None),
  tok("لِلْمَلِكِ", "malik-king", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمَلِكِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِسَاقِيًا.", "«to the king» — in jarr, hanging on «cupbearer».", "«krala» — mecrur, «sâkî»ye müteallik.", segments=[seg("لِ", "li", "prep"), seg("لْمَلِكِ", "malik-king", "noun")]),
  tok("وَصُلِبَ", "salaba-crucify", "verb", ["atf-nasaq", "naib-al-fail"], "الْوَاوُ عَاطِفَةٌ، وَصُلِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and was crucified» — a passive māḍī.", "«ve asıldı» — meçhul mâzî.", segments=wa_("صُلِبَ", "salaba-crucify", "verb")),
  tok("الْآخَرُ", "akhar", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«the other» — the deputy doer of the passive.", "«diğeri» — nâib-i fâil.", punct=".")])
sen("s6", "And the cupbearer forgot to mention Yūsuf before the king.", "Sâkî, Yusuf'u kralın yanında anmayı unuttu.", [
  mazi("وَنَسِيَ", "nasiya", "«forgot»", "«unuttu»", hidden=None, wa=True, tags=["naqis-verbs"]), saqi_fail(),
  an_("نَسِيَ", "«forgot»", "«unuttu»"),
  tok("يَذْكُرَ", "dhakara", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to mention» — in naṣb after an; «he» concealed.", "«anmayı» — en ile mansub; fâil gizli «o»."),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«before» — an adverb of place; a muḍāf.", "«yanında» — mekân zarfı; muzâf."),
  mi("الْمَلِكِ", "malik-king", "«the king»", "«kral»", punct=".")])
sen("s7", "And Yūsuf stayed in the prison for years.", "Yusuf yıllarca zindanda kaldı.", [
  mazi("وَأَقَامَ", "aqama", "«stayed»", "«kaldı»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), yusuf_fail(),
  fi(), majrur("السِّجْنِ", "sijn", "«the prison»", "«zindan»", "فِي"),
  sinin(role="ظَرْفُ زَمَانٍ مَنْصُوبٌ", sign="الْيَاءُ", en="«(for) years»", tr="«yıllarca»", tags=["maful-fih"], en_role="an adverb of time", tr_role="zaman zarfı", punct=".")])

# ================================================================ §13 رؤيا الملك (pp. 45–47)
sen("s8", "And the king of Egypt saw a wondrous dream.", "Mısır kralı şaşılası bir rüya gördü.", [
  mazi("وَرَأَى", "raa", "«saw»", "«gördü»", hidden=None, wa=True, tags=["naqis-verbs"]),
  tok("مَلِكُ", "malik-king", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the king (of)» — the doer; a muḍāf.", "«kralı» — fâil; muzâf."),
  name_mudaf_ilayh("مِصْرَ", "misr", "«Egypt»", "«Mısır»"),
  tok("رُؤْيَا", "ruya-dream", "noun", ["maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ.", "«a dream» — the object; a maqṣūr, its fatḥa estimated on the alif.", "«bir rüya» — mef'ûl; maksûr, fethası elif üzerinde takdîrî."),
  nat_nasb("عَجِيبَةً", "ajib", "«wondrous»", "«şaşılası»", punct=".")])
sen("s9", "He saw in his sleep seven fat cows.", "Uykusunda yedi semiz inek gördü.", [
  mazi("رَأَى", "raa", "«he saw»", "«gördü»", hidden="هُوَ", tags=["naqis-verbs"]), fi(), majrur("الْمَنَامِ", "manam", "«sleep»", "«uyku»", "فِي"),
  sab_maful(), madud("بَقَرَاتٍ", "baqara", "«cows»", "«inek»"),
  nat_jarr("سِمَانٍ", "samin", "«fat»", "«semiz»", tags=["jam-taksir"], extra=" — جَمْعُ تَكْسِيرٍ لِسَمِينٍ، نَعْتٌ لِجَمْعٍ", punct=".")])
sen("s10", "And seven lean cows were eating these cows.", "Ve bu inekleri yedi zayıf inek yiyordu.", [
  tok("وَيَأْكُلُ", "akala", "verb", ["anwa-al-waw", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَأْكُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and … eat» — a muḍāriʿ in rafʿ; its object is fronted and its doer delayed.", "«ve … yer» — merfû muzâri; mef'ûlü öne, fâili sona alınmıştır.", segments=wa_("يَأْكُلُ", "akala", "verb")),
  hadhihi_("nasb"),
  badal_("الْبَقَرَاتِ", "baqara", "nasb", "«the cows»", "«inekleri»", sign="مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ"),
  tok("سَبْعُ", "sab-seven", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ — اسْمُ عَدَدٍ.", "«seven» — the delayed doer; a muḍāf.", "«yedi» — muahhar fâil; muzâf."),
  madud("بَقَرَاتٍ", "baqara", "«cows»", "«inek»"),
  nat_jarr("عِجَافٍ", "ajfa", "«lean»", "«zayıf»", tags=["jam-taksir"], extra=" — جَمْعُ عَجْفَاءَ", punct=".")])
sen("s11", "And the king saw seven green ears of grain and seven dry ones.", "Kral yedi yeşil başak ve yedi kuru başak gördü.", [
  mazi("وَرَأَى", "raa", "«saw»", "«gördü»", hidden=None, wa=True, tags=["naqis-verbs"]), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  sab_maful(), madud("سُنْبُلَاتٍ", "sunbula", "«ears of grain»", "«başak»"),
  nat_jarr("خُضْرٍ", "akhdar", "«green»", "«yeşil»", tags=["jam-taksir"], extra=" — جَمْعُ أَخْضَرَ"),
  sab_maful(full="وَسَبْعَ", wa=True), madud("سُنْبُلَاتٍ", "sunbula", "«ears of grain»", "«başak»"),
  tok("يَابِسَاتٍ", "yabis", "noun", ["naat-sifa", "jam-muannath-salim"], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«dry» — the naʿt; a sound feminine plural.", "«kuru» — sıfat; cem-i müennes sâlim.", punct=".")])
sen("s12", "The king wondered at this strange dream, and asked his companions about the interpretation of the dream.", "Kral bu garip rüyaya şaştı ve nedimlerine rüyanın tabirini sordu.", [
  mazi("تَعَجَّبَ", "taajjaba", "«wondered»", "«şaştı»", hidden=None, tags=["form-v-verbs"]), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  min_(), hadhihi_("jarr"),
  badal_("الرُّؤْيَا", "ruya-dream", "jarr", "«the dream»", "«rüya»", sign="مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ"),
  nat_jarr("الْعَجِيبَةِ", "ajib", "«strange»", "«garip»"),
  mazi("وَسَأَلَ", "saala", "«and asked»", "«ve sordu»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  mudaf_pron("جُلَسَاءَهُ", "jalis", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his companions» — the object", "«nedimlerini» — mef'ûl", tags=["maful-bihi", "jam-taksir"]),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«hakkında»."),
  tawil_jarr(full="تَأْوِيلِ", prep="عَنْ", en="«the interpretation (of)»", tr="«tabiri»"), ruya_mi(punct=".")])
sen("s13", "They said: This is nothing; the sleeper sees many things that have no reality.", "Dediler: Bu bir şey değil; uyuyan, gerçeği olmayan birçok şey görür.", [
  qalu(), ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("لَيْسَ", "laysa", "verb", [K, "mubtada-khabar"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.", "«is not» — the frozen sister of kāna; its ism «it» concealed; the clause is the khabar.", "«değil» — kâne'nin câmid kız kardeşi; ismi gizli «o»; cümle haberdir."),
  tok("بِشَيْءٍ", "shay", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَشَيْءٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "«anything» — the redundant bāʾ on laysa's khabar: jarr in form, naṣb in place.", "«bir şey» — leyse'nin haberi üzerinde zâid bâ: lafzan mecrur, mahallen mansub.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")]),
  tok("النَّائِمُ", "naim-sleeper", "noun", ["mubtada-khabar", "ism-fail"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the sleeper» — the mubtadaʾ.", "«uyuyan» — mübtedâ."),
  khabar_mudari("يَرَى", "raa", ["naqis-verbs"], "«sees»", "«görür»"),
  tok("أَشْيَاءَ", "shay", "noun", ["maful-bihi", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«things» — the object; a diptote plural.", "«şeyler» — mef'ûl; gayr-i munsarıf cemi."),
  nat_nasb("كَثِيرَةً", "kathir", "«many»", "«birçok»"),
  tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "naat-sifa"], "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِأَشْيَاءَ.", "«no» — the lā that denies the whole genus; the clause describes «things».", "«hiç … yok» — cins için nefiy lâ'sı; cümle «şeyler»in sıfatıdır."),
  tok("حَقِيقَةَ", "haqiqa", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«reality» — the ism of lā, built on fatḥa.", "«gerçek» — lâ'nın ismi, feth üzere mebnî."),
  lahu("لَهَا", "هَا", "pron-3fs", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ لَا.", "«to them» — the phrase is lā's khabar.", "«onların» — şibh-i cümle lâ'nın haberi.", tags=["la-nafiya-lil-jins"], punct=".")])
sen("s14", "But the cupbearer said: No; rather, I will tell you the interpretation of this dream.", "Fakat sâkî dedi: Hayır, aksine size bu rüyanın tabirini haber vereceğim.", [
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«fakat» — muhaffef lâkin, amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  qala(hidden=None), saqi_fail(punct=":"),
  tok("لَا", "la-jawab", "part", [], "حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«no» — the answer particle.", "«hayır» — cevap harfi.", punct="،"),
  tok("بَلْ", "bal", "part", ["anwa-ma"], "حَرْفُ إِضْرَابٍ.", "«rather» — the particle of correction.", "«aksine» — idrâb harfi."),
  tok("أُخْبِرُكُمْ", "akhbara", "verb", ["mudari-marfu", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«I will tell you» — a muḍāriʿ; «I» concealed of necessity; the attached pronoun its object.", "«size haber veririm» — muzâri; fâil vücûben gizli «ben»; bitişik zamir mef'ûl.", segments=[seg("أُخْبِرُ", "akhbara", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  tawil_jarr(), hadhihi_("jarr"),
  badal_("الرُّؤْيَا", "ruya-dream", "jarr", "«the dream»", "«rüya»", sign="مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", punct=".")])
sen("s15", "And the cupbearer went to the prison and asked Yūsuf about the interpretation of the king's dream.", "Sâkî zindana gitti ve Yusuf'a kralın rüyasının tabirini sordu.", [
  mazi("وَذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None, wa=True), saqi_fail(), *an_sijn(),
  mazi("وَسَأَلَ", "saala", "«and asked»", "«ve sordu»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'a»"),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«hakkında»."),
  tawil_jarr(full="تَأْوِيلِ", prep="عَنْ", en="«the interpretation (of)»", tr="«tabiri»"),
  tok("رُؤْيَا", "ruya-dream", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَهُوَ مُضَافٌ.", "«the dream (of)» — a muḍāf ilayh that is itself a muḍāf.", "«rüyası» — kendisi de muzâf olan muzâfun ileyh."),
  mi("الْمَلِكِ", "malik-king", "«the king»", "«kral»", punct=".")])
sen("s16", "Yūsuf was generous, noble, compassionate toward Allah's creation, so he told him the interpretation.", "Yusuf cömert, kerem sahibi, Allah'ın yarattıklarına şefkatliydi; bu yüzden ona tabiri haber verdi.", [
  kana_bare(), yusuf_ism_kana(),
  khabar_kana("جَوَادًا", "jawad", "«generous»", "«cömert»"), khabar_kana("كَرِيمًا", "karim", "«noble»", "«kerem sahibi»", second=True),
  tok("مُشْفِقًا", "mushfiq", "noun", [K, "ism-fail", "form-iv-verbs"], "خَبَرٌ ثَالِثٌ لِكَانَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ مِنْ أَشْفَقَ.", "«compassionate» — a third khabar of kāna; the ism fāʿil of أَشْفَقَ.", "«şefkatli» — kâne'nin üçüncü haberi; eşfaka'nın ism-i fâili."),
  ala(), tok("خَلْقِ", "khalq", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِمُشْفِقًا.", "«the creation (of)» — in jarr; a muḍāf.", "«yarattıkları» — mecrur; muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh."),
  verb_enc("فَأَخْبَرَهُ", "akhbara", "هُ", "pron-3ms", "«so he told him»", "«bu yüzden ona haber verdi»", mudari=False, hidden="هُوَ", fa=True, tags=["form-iv-verbs"]),
  tok("بِالتَّأْوِيلِ", "tawil", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّأْوِيلِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِأَخْبَرَ.", "«the interpretation» — in jarr after the bāʾ.", "«tabiri» — bâ ile mecrur.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("التَّأْوِيلِ", "tawil", "noun")])])
sen("s17", "And Yūsuf was generous and noble; he did not know stinginess.", "Yusuf cömert ve kerem sahibiydi; cimriliği bilmezdi.", [
  kana(), yusuf_ism_kana(),
  khabar_kana("جَوَادًا", "jawad", "«generous»", "«cömert»"), khabar_kana("كَرِيمًا", "karim", "«noble»", "«kerem sahibi»", second=True),
  la_nafiya(),
  tok("يَعْرِفُ", "arafa", "verb", ["la-nafiya", "mudari-marfu", "naat-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِكَرِيمًا.", "«did not know» — rafʿ after the negating lā; the clause describes «noble».", "«bilmezdi» — nefiy lâ'sından sonra merfû; cümle «kerem sahibi»nin sıfatıdır."),
  maful("الْبُخْلَ", "bukhl", "«stinginess»", "«cimriliği»", punct=".")])
sen("s18", "So Yūsuf told the interpretation, and pointed the way to the plan.", "Böylece Yusuf tabiri haber verdi ve tedbiri gösterdi.", [
  fa_mazi("فَأَخْبَرَ", "akhbara", "«so … told»", "«böylece … haber verdi»", hidden=None, tags=["form-iv-verbs"]), yusuf_fail(),
  tok("بِالتَّأْوِيلِ", "tawil", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّأْوِيلِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِأَخْبَرَ.", "«the interpretation» — in jarr after the bāʾ.", "«tabiri» — bâ ile mecrur.", segments=[seg("بِ", "bi", "prep"), seg("التَّأْوِيلِ", "tawil", "noun")]),
  mazi("وَدَلَّ", "dalla", "«and pointed»", "«ve gösterdi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "doubled-verbs"]),
  ala(), majrur("التَّدْبِيرِ", "tadbir", "«the plan»", "«tedbir»", "عَلَى", punct=".")])
sen("s19", "He said: You will sow for seven years; and leave what you have harvested in its ear, except a little of what you eat.", "Dedi: Yedi yıl ekeceksiniz; biçtiğinizi, yediğiniz az bir miktar dışında, başağında bırakın.", [
  qala(hidden="هُوَ", punct=None),
  khamsa("تَزْرَعُونَ", "zaraa", "«you will sow»", "«ekeceksiniz»"),
  sab_maful(zarf=True), sinin(punct="،"),
  amr_pl("وَاتْرُكُوا", "taraka", "«and leave»", "«ve bırakın»", wa=True),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the relative, as object.", "«-dığınızı» — ism-i mevsûl, mef'ûl."),
  tok("حَصَدْتُمْ", "hasada-harvest", "verb", ["ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«you have harvested» — a māḍī on sukūn before the doer's tāʾ; the relative's clause.", "«biçtiniz» — fâil tâ'sından önce sükûn üzere mebnî mâzî; sıla cümlesi."),
  fi(), mudaf_pron("سُنْبُلِهِ", "sunbul", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«its ear» — in jarr", "«başağı» — mecrur", tags=["huruf-jarr"]),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except» — the particle of exception.", "«dışında» — istisnâ edatı."),
  tok("قَلِيلًا", "qalil", "noun", ["istithna"], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ.", "«a little» — the excepted, in naṣb.", "«az bir miktar» — müstesnâ, mansub."),
  tok("مِمَّا", "min", "prep", ["huruf-jarr", "ism-mawsul", "naat-sifa"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ نَعْتٌ لِقَلِيلًا.", "«of what» — min fused with the relative mā; the phrase describes «a little».", "«-dığınızdan» — min ile mevsûl mâ; şibh-i cümle «az»ın sıfatıdır.", segments=[seg("مِنْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  khamsa("تَأْكُلُونَ", "akala", "«you eat»", "«yersiniz»", tags=["ism-mawsul"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ", punct=".")])
sen("s20", "And after that there will be a general famine in which you eat what you have stored, except a little.", "Ondan sonra, biriktirdiğinizi az bir miktar dışında yediğiniz genel bir kıtlık olacak.", [
  tok("وَيَكُونُ", "kana", "verb", ["anwa-al-waw", "mudari-marfu", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ بِالضَّمَّةِ (بِمَعْنَى يَحْدُثُ).", "«and there will be» — kāna complete, «to happen»; a muḍāriʿ in rafʿ.", "«ve olacak» — tâm kâne, «meydana gelmek»; merfû muzâri.", segments=wa_("يَكُونُ", "kana", "verb")),
  tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«after» — an adverb of time; a muḍāf.", "«sonra» — zaman zarfı; muzâf."),
  hadha_pron_jarr("ذٰلِكَ", "dhalika", "«that»", "«o»"),
  fail("قَحْطٌ", "qaht", "«a famine»", "«bir kıtlık»"), nat_raf("عَامٌّ", "amm", "«general»", "«genel»"),
  khamsa("تَأْكُلُونَ", "akala", "«you eat»", "«yersiniz»", tags=["naat-sifa"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِقَحْطٍ"),
  tok("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِتَأْكُلُونَ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the relative, as object.", "«-dığınızı» — ism-i mevsûl, mef'ûl."),
  tok("خَزَنْتُمْ", "khazana", "verb", ["ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«you have stored» — a māḍī on sukūn before the doer's tāʾ; the relative's clause.", "«biriktirdiniz» — fâil tâ'sından önce sükûn üzere mebnî mâzî; sıla cümlesi."),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except» — the particle of exception.", "«dışında» — istisnâ edatı."),
  tok("قَلِيلًا", "qalil", "noun", ["istithna"], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ.", "«a little» — the excepted, in naṣb.", "«az bir miktar» — müstesnâ, mansub.", punct=".")])
sen("s21", "And this famine will last for seven years.", "Bu kıtlık yedi yıl sürecek.", [
  tok("وَيَطُولُ", "tala-long", "verb", ["anwa-al-waw", "mudari-marfu", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَطُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and … will last» — a hollow muḍāriʿ in rafʿ; its doer follows.", "«ve … sürer» — ecvef muzâri, merfû; fâili sonra gelir.", segments=wa_("يَطُولُ", "tala-long", "verb")),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "fail"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this» — the demonstrative, the doer.", "«bu» — ism-i işâret, fâil."),
  badal_("الْقَحْطُ", "qaht", "raf", "«famine»", "«kıtlık»"),
  ila(), tok("سَبْعِ", "sab-seven", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ — اسْمُ عَدَدٍ.", "«seven» — in jarr after ilā; a muḍāf.", "«yedi» — ilâ ile mecrur; muzâf."),
  sinin(punct=".")])
sen("s22", "And after that comes relief, and the people have plenty.", "Ondan sonra bolluk gelir ve insanlar berekete kavuşur.", [
  tok("وَبَعْدَ", "bada", "noun", ["anwa-al-waw", "maful-fih", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَبَعْدَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِيَأْتِي.", "«and after» — an adverb of time, fronted; a muḍāf.", "«ve … sonra» — öne alınmış zaman zarfı; muzâf.", segments=wa_("بَعْدَ", "bada", "noun")),
  hadha_pron_jarr("ذٰلِكَ", "dhalika", "«that»", "«o»"),
  tok("يَأْتِي", "ata", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ.", "«comes» — a nāqiṣ muḍāriʿ, its ḍamma estimated on the yāʾ.", "«gelir» — nâkıs muzâri, zammesi yâ üzerinde takdîrî."),
  fail("النَّصْرُ", "nasr", "«relief»", "«bolluk»"),
  tok("وَيُخْصِبُ", "akhsaba", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُخْصِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and have plenty» — a Form-IV muḍāriʿ in rafʿ.", "«ve bereketlenir» — if'âl bâbından merfû muzâri.", segments=wa_("يُخْصِبُ", "akhsaba", "verb")),
  nas_fail(punct=".")])
sen("s23", "And the cupbearer went and told the king the interpretation of his dream.", "Sâkî gitti ve krala rüyasının tabirini haber verdi.", [
  mazi("وَذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None, wa=True), saqi_fail(),
  mazi("وَأَخْبَرَ", "akhbara", "«and told»", "«ve haber verdi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-iv-verbs"]),
  malik_("الْمَلِكَ", "nasb", "مَفْعُولٌ بِهِ", "«the king» — the object.", "«kralı» — mef'ûl.", tags=["maful-bihi"]),
  tawil_jarr(), ruya_mi(full="رُؤْيَاهُ", pron="هُ", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "salaba-crucify": G("salaba-crucify", "صَلَبَ", "ص ل ب", "verb", "to crucify", "asmak, çarmıha germek", 2, form="I"),
 "hasada-harvest": G("hasada-harvest", "حَصَدَ", "ح ص د", "verb", "to reap, to harvest (حَسَدَ with the sīn is to envy)", "biçmek, hasat etmek (sîn ile حَسَدَ: kıskanmak)", 2, form="I"),
 "saqi": G("saqi", "سَاقٍ (السَّاقِي)", "س ق ي", "noun", "a cupbearer (ism fāʿil of سَقَى, a manqūṣ)", "sâkî, içki sunan (sakâ'nın ism-i fâili, mankûs)", 2, plural="سُقَاة"),
 "sab-seven": G("sab-seven", "سَبْع", "س ب ع", "noun", "seven (with a masculine counted noun the number is سَبْعَة; with a feminine one, سَبْع)", "yedi (ma'dûd müzekker ise سَبْعَة, müennes ise سَبْع)", 1),
 "baqara": G("baqara", "بَقَرَة", "ب ق ر", "noun", "a cow", "inek", 1, plural="بَقَرَات"),
 "samin": G("samin", "سَمِين", "س م ن", "noun", "fat, plump (ṣifa mushabbaha)", "semiz, şişman (sıfat-ı müşebbehe)", 2, plural="سِمَان"),
 "ajfa": G("ajfa", "عَجْفَاء", "ع ج ف", "noun", "lean, emaciated (feminine of أَعْجَف)", "zayıf, cılız (a'cef'in müennesi)", 3, plural="عِجَاف"),
 "sunbula": G("sunbula", "سُنْبُلَة", "س ن ب ل", "noun", "an ear of grain", "başak", 2, plural="سُنْبُلَات"),
 "sunbul": G("sunbul", "سُنْبُل", "س ن ب ل", "noun", "ears of grain (collective)", "başak (cins ismi)", 2),
 "akhdar": G("akhdar", "أَخْضَر", "خ ض ر", "noun", "green (a colour on أَفْعَل, a diptote)", "yeşil (أَفْعَل vezninde renk, gayr-i munsarıf)", 1, plural="خُضْر"),
 "jalis": G("jalis", "جَلِيس", "ج ل س", "noun", "a companion in session, a courtier", "nedim, meclis arkadaşı", 3, plural="جُلَسَاء"),
 "mushfiq": G("mushfiq", "مُشْفِق", "ش ف ق", "noun", "compassionate, tender (ism fāʿil of أَشْفَقَ)", "şefkatli, merhametli (eşfaka'nın ism-i fâili)", 3),
 "qaht": G("qaht", "قَحْط", "ق ح ط", "noun", "famine, drought", "kıtlık, kuraklık", 2),
 "khazana": G("khazana", "خَزَنَ", "خ ز ن", "verb", "to store, to lay up", "depolamak, biriktirmek", 2, form="I"),
 "akhsaba": G("akhsaba", "أَخْصَبَ", "خ ص ب", "verb", "to have plenty, to become fertile", "bolluğa ermek, bereketlenmek", 3, form="IV"),
 "la-jawab": G("la-jawab", "لَا (حَرْفُ جَوَابٍ)", None, "part", "no (the answer particle)", "hayır (cevap harfi)", 1),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("amma", "أما"), ("awwal", "أول"), ("aqama", "أقام"), ("sana", "سنة"), ("naim-sleeper", "نائم"), ("haqiqa", "حقيقة"), ("bukhl", "بخل"), ("dalla", "دل"), ("tadbir", "تدبير"), ("zaraa", "زرع"), ("qalil", "قليل"), ("amm", "عام"), ("tala-long", "طال"), ("nasr", "نصر"), ("yabis", "يابس"), ("khalq", "خلق"), ("shay", "شيء"), ("an", "عن"), ("hasada", "حسد")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("salaba-crucify", "khazana", "akhsaba"): mo["verbs"].pop(_k, None)
put_morph(mo, "hasada-harvest", _sg.sound1("nasara", "حَصَد", "حْصُد", "اُحْصُد", "حَصْد", "حَاصِد", "مَحْصُود", "حُصِدَ", "يُحْصَدُ", note="مُتَعَدٍّ: حَصَدَ الزَّرْعَ — وَبَابُهُ نَصَرَ وَضَرَبَ."))
put_morph(mo, "salaba-crucify", _sg.sound1("daraba", "صَلَب", "صْلِب", "اِصْلِب", "صَلْب", "صَالِب", "مَصْلُوب", "صُلِبَ", "يُصْلَبُ", note="مُتَعَدٍّ: صَلَبَ الْمُجْرِمَ."))
put_morph(mo, "khazana", _sg.idgham(_sg.sound1("nasara", "خَزَن", "خْزُن", "اُخْزُن", "خَزْن", "خَازِن", "مَخْزُون", "خُزِنَ", "يُخْزَنُ", note="مُتَعَدٍّ: خَزَنَ الطَّعَامَ — لَامُهُ نُونٌ فَتُدْغَمُ فِي نُونِ النِّسْوَةِ وَنَا (خَزَنَّ، خَزَنَّا).")))
put_morph(mo, "akhsaba", _sg.derived("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَخْصَب", "خْصِب", "أَخْصِب", "إِخْصَاب", "مُخْصِب", "مُخْصَب", "أُخْصِبَ", "يُخْصَبُ", note="لَازِمٌ: أَخْصَبَ النَّاسُ، أَخْصَبَتِ الْأَرْضُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 14 (print pp. 44–47, «أَحْسَنُ الْقَصَصِ» sections 12 «تَأْوِيلُ الرُّؤْيَا» and 13 «رُؤْيَا الْمَلِكِ»): the interpretation given to the two men with Yūsuf 12:41 in the print's two lines (s2, s3, marked) and 12:42 (s4, marked); the cupbearer's forgetting and the years in prison; the king's dream of the seven fat and seven lean cows and the seven green and seven dry ears; the courtiers' dismissal, the cupbearer's visit, Yūsuf's generosity and his counsel — the seven years of sowing, the famine and the relief. "
          "One printed line is one sentence; s19 is the author's own retelling of Yūsuf 12:47–49 and is NOT marked as a quotation, because the print sets it without parentheses and its wording differs from the aya; the saying verbs of s2, s4, s13 and s14 keep the print's colon, s19 has none in the print and takes none; the print's parentheses around the ayas are read as quotation marks.")
ADD_TR = (" On dördüncü bölüm (basılı s. 44–47, «أَحْسَنُ الْقَصَصِ» 12. kısım «تَأْوِيلُ الرُّؤْيَا» ve 13. kısım «رُؤْيَا الْمَلِكِ»): iki adama verilen tabir, baskının iki satırındaki Yûsuf 12:41 (s2, s3, işaretli) ve 12:42 (s4, işaretli) ile; sâkînin unutması ve zindandaki yıllar; kralın yedi semiz ve yedi zayıf inek, yedi yeşil ve yedi kuru başak rüyası; nedimlerin geçiştirmesi, sâkînin ziyareti, Yusuf'un cömertliği ve öğüdü — yedi yıl ekim, kıtlık ve ferahlık. "
          "Basılı her satır bir cümledir; s19 Yûsuf 12:47–49'un yazarın kendi anlatımıdır ve alıntı olarak işaretlenmemiştir, çünkü baskı onu parantezsiz dizer ve lafzı âyetten farklıdır; s2, s4, s13 ve s14'ün söyleme fiilleri baskının iki noktasını korur, s19'da baskıda iki nokta yoktur ve eklenmemiştir; baskının âyetleri saran parantezleri tırnak olarak okunmuştur.")
write_out(14, S, TITLE, ADD_EN, ADD_TR, "pp. 44–47", GLOSS_ADD)
report(14, S, GLOSS_ADD, ())
