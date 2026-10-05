# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 22: «يُوسُفُ يُرْسِلُ إِلَى يَعْقُوبَ، وَيَعْقُوبُ عِنْدَ يُوسُفَ» — «أَحْسَنُ الْقَصَصِ» sections 23–24 (print pp. 64–67):
Yūsuf's longing, the shirt (12:93–98), Yaʿqūb comes to Egypt, the prostration and the dream fulfilled (12:100, 12:4), Yūsuf's thanks.
Every printed line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch22.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "يُوسُفُ يُرْسِلُ إِلَى يَعْقُوبَ، وَيَعْقُوبُ عِنْدَ يُوسُفَ", "en": "Yūsuf sends to Yaʿqūb; Yaʿqūb with Yūsuf", "tr": "Yusuf Yakub'a haber gönderiyor; Yakub Yusuf'un yanında"}
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


# ---------------------------------------------------------------- chapter-15 helpers
def name_ism_lakinna(full, lex="yusuf", en="«Yūsuf»", tr="«Yusuf»", punct=None):
    return tok(full, lex, "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the ism of lākinna; a diptote name.", tr + " — lâkinne'nin ismi; gayr-i munsarıf özel isim.", punct=punct)
def man_mubt(punct=None):
    return tok("مَنْ", "man-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the question noun as mubtadaʾ.", "«kim» — istifham ismi, mübtedâ.", punct=punct)
def man_shart(full="وَمَنْ", wa=True):
    return tok(full, "man", "pron", ["anwa-al-waw", "ism-mawsul", "mubtada-khabar"], W(wa) + "مَنْ اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ (وَيَصِحُّ جَعْلُهَا شَرْطِيَّةً).", Wen(wa) + "«whoever» — the relative مَنْ as mubtadaʾ (a conditional reading is also possible).", Wtr(wa) + "«her kim» — mevsûl men, mübtedâ (şart okunuşu da mümkündür).", segments=(wa_("مَنْ", "man", "pron") if wa else None))
def khabar_raf(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", ["mubtada-khabar"] + list(tags), "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ" + extra + ".", en + " — the khabar.", tr + " — haber.", punct=punct)
def mubt_raf(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", ["mubtada-khabar"] + list(tags), "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ" + extra + ".", en + " — the mubtadaʾ.", tr + " — mübtedâ.", punct=punct)
def rasul_malik(role_ar, en, tr, punct=None, tags=()):
    return [tok("رَسُولُ", "rasul", "noun", list(tags) + ["idafa-definiteness"], role_ar + " مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the messenger (of)» — " + en + "; a muḍāf.", "«elçisi» — " + tr + "; muzâf."), mi("الْمَلِكِ", "malik-king", "«the king»", "«kral»", punct=punct)]
def khazain_ard(prep=None, punct=None, role="مُتَعَلِّقٌ بِمَا قَبْلَهُ", case="jarr", tags=()):
    if prep == "بِ":
        first = tok("بِخَزَائِنِ", "khizana", "noun", ["huruf-jarr", "idafa-definiteness", "mamnu-min-sarf"] + list(tags), "الْبَاءُ حَرْفُ جَرٍّ، وَخَزَائِنِ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ (وَلَوْلَا الْإِضَافَةُ لَجُرَّ بِالْفَتْحَةِ، فَهُوَ صِيغَةُ مُنْتَهَى الْجُمُوعِ) — " + role + ".", "«with the treasuries (of)» — in jarr after the bāʾ; a muḍāf, so the diptote plural takes its kasra.", "«hazineleriyle» — bâ ile mecrur; muzâf olduğu için gayr-i munsarıf cemi kesre alır.", segments=[seg("بِ", "bi", "prep"), seg("خَزَائِنِ", "khizana", "noun")])
    elif prep == "لِ":
        first = tok("لِخَزَائِنِ", "khizana", "noun", ["huruf-jarr", "idafa-definiteness", "mamnu-min-sarf"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَخَزَائِنِ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ — " + role + ".", "«for the treasuries (of)» — in jarr after the lām; a muḍāf.", "«hazineleri için» — lâm ile mecrur; muzâf.", segments=[seg("لِ", "li", "prep"), seg("خَزَائِنِ", "khizana", "noun")])
    elif case == "raf":
        first = tok("خَزَائِنُ", "khizana", "noun", ["mubtada-khabar", "idafa-definiteness", "mamnu-min-sarf"] + list(tags), "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the treasuries (of)» — the delayed mubtadaʾ; a muḍāf.", "«hazineleri» — muahhar mübtedâ; muzâf.")
    else:
        first = tok("خَزَائِنِ", "khizana", "noun", ["huruf-jarr", "idafa-definiteness", "mamnu-min-sarf"] + list(tags), "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ لِأَنَّهُ مُضَافٌ — " + role + ".", "«the treasuries (of)» — in jarr after ʿalā; a muḍāf.", "«hazineleri» — alâ ile mecrur; muzâf.")
    return [first, mi("الْأَرْضِ", "ard", "«the land»", "«yeryüzü»", punct=punct)]
def hafiz_alim(case="nasb", of="كَانَ", punct=None, tags=()):
    if case == "nasb":
        return [tok("حَفِيظًا", "hafiz-keeper", "noun", [K, "sifa-mushabbaha"] + list(tags), "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a keeper» — kāna's khabar.", "«koruyucu» — kâne'nin haberi."),
                tok("عَلِيمًا", "alim", "noun", [K, "sifa-mushabbaha"], "خَبَرٌ ثَانٍ لِكَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«knowing» — a second khabar of kāna.", "«bilen» — kâne'nin ikinci haberi.", punct=punct)]
    return [tok("حَفِيظٌ", "hafiz-keeper", "noun", ["inna-wa-akhawatuha", "sifa-mushabbaha"] + list(tags), "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«a keeper» — inna's khabar.", "«koruyucu» — inne'nin haberi."),
            tok("عَلِيمٌ", "alim", "noun", ["inna-wa-akhawatuha", "sifa-mushabbaha"], "خَبَرٌ ثَانٍ لِإِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«knowing» — a second khabar of inna.", "«bilen» — inne'nin ikinci haberi.", punct=punct)]
def kana_yalamu(verb_full, lex, en, tr, tags=(), hidden="هُوَ", punct=None):
    return [kana(), yusuf_ism_kana(), khabar_kana_mudari(verb_full, lex, en, tr, tags=tags, hidden=hidden, punct=punct)]
def anna_ism(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + list(tags), "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the ism of anna.", tr + " — enne'nin ismi.", punct=punct)
def anna_khabar(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + list(tags), "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — the khabar of anna.", tr + " — enne'nin haberi.", punct=punct)
def fi_nas(punct=None):
    return [fi(), majrur("النَّاسِ", "nas", "«the people»", "«insanlar»", "فِي", punct=punct)]
def amwal(full, prep_ar, en, tr, punct=None, mudaf_ilayh=("اللهِ", "allah", "propn", "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh.")):
    first = tok(full, "mal", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"] if prep_ar else ["maful-bihi", "idafa-definiteness", "jam-taksir"], (f"مَجْرُورٌ بِـ{prep_ar} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" if prep_ar else "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ") + "، وَهُوَ مُضَافٌ — جَمْعُ مَالٍ.", en + " — a muḍāf; the plural of مَال.", tr + " — muzâf; «mal»ın cem'i.")
    w, lx, ps, ar, e, t = mudaf_ilayh
    return [first, tok(w, lx, ps, ["idafa-definiteness"], ar, e, t, punct=punct)]
def la_yajidu(punct=None):
    return [la_nafiya(wa=True), neg_mudari("يَجِدُ", "wajada", "«find»", "«bulur»", hidden=None, tags=["mithal-verbs"], extra=" — مِثَالٌ وَاوِيٌّ حُذِفَتْ وَاوُهُ"), nas_fail(),
            tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the relative, as object.", "«-ecek şey» — ism-i mevsûl, mef'ûl.")]
def kana_ism_hidden_khabar(kh_full, kh_lex, kh_en, kh_tr, punct=None, wa=True, tags=()):
    return [kana_hidden(wa=wa), khabar_kana(kh_full, kh_lex, kh_en, kh_tr, punct=punct, tags=tags)]
def ma_nafiya_(wa=True):
    return tok("وَمَا" if wa else "مَا", "ma-nafiya", "part", ["anwa-ma", "anwa-al-waw"], W(wa) + "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", Wen(wa) + "«not» — the negating mā, no government.", Wtr(wa) + "«değil» — nefiy mâ'sı, amel etmez.", segments=(wa_("مَا", "ma-nafiya", "part") if wa else None))


# ---------------------------------------------------------------- chapter-16 helpers
def fi_misr(role="مُتَعَلِّقٌ بِمَا قَبْلَهُ", punct=None, khabar_of=None, wa=False):
    ar = "حَرْفُ جَرٍّ" + (f" — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ {khabar_of}" if khabar_of else "")
    return [tok("وَفِي" if wa else "فِي", "fi", "prep", ["huruf-jarr"] + (["anwa-al-waw"] if wa else []), W(wa) + ar + ".", Wen(wa) + "«in»" + (" — the phrase is the fronted khabar." if khabar_of else "."), Wtr(wa) + "«-de»" + (" — şibh-i cümle mukaddem haber." if khabar_of else "."), segments=(wa_("فِي", "fi", "prep") if wa else None)),
            tok("مِصْرَ", "misr", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ — " + role + ".", "«Egypt» — in jarr by a fatḥa: a diptote name.", "«Mısır» — fetha ile mecrur: gayr-i munsarıf özel isim.", punct=punct)]
def ikhwat_yusuf(role_ar, en, tr, case="raf", punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return [tok({"raf": "إِخْوَةُ", "nasb": "إِخْوَةَ", "jarr": "إِخْوَةِ"}[case], "akh", "noun", list(tags) + ["idafa-definiteness", "jam-taksir"], role_ar + " " + C + "، وَهُوَ مُضَافٌ — جَمْعُ أَخٍ.", "«the brothers (of)» — " + en + "; a muḍāf.", "«kardeşleri» — " + tr + "; muzâf."),
            name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", punct=punct)]
def hum_mubt(full="وَهُمْ", wa=True, hal=True, punct=None):
    return tok(full, "hum", "pron", (["hal", "anwa-al-waw"] if hal else ["anwa-al-waw"]) + ["mubtada-khabar"], (("الْوَاوُ حَالِيَّةٌ، وَ" if hal else "الْوَاوُ عَاطِفَةٌ، وَ") if wa else "") + "هُمْ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ" + (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ" if hal else "") + ".", ("«while they» — the wāw of ḥāl; " if hal else "«and they» — ") + "the detached pronoun as mubtadaʾ.", ("«onlar … iken» — hâl vâvı; " if hal else "«ve onlar» — ") + "munfasıl zamir, mübtedâ.", punct=punct, segments=(wa_("هُمْ", "hum", "pron") if wa else None))
def la_yarifun(punct=None, extra=""):
    return [la_nafiya(), khamsa("يَعْرِفُونَ", "arafa", "«know»", "«bilirler»", tags=["la-nafiya", "mubtada-khabar"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ" + extra, punct=punct)]
def annahu(obj_of="يَعْرِفُونَ", en_of="«know»", tr_of="«bilirler»"):
    return tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha"], f"أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ {obj_of}.", f"«that he» — anna with its pronoun ism; the clause is the object of {en_of}.", f"«onun …-duğunu» — enne, zamir ismi; te'vilî masdar {tr_of}nin mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")])
def fi_bir(punct=None, of="كَانَ"):
    return [tok("فِي", "fi", "prep", ["huruf-jarr", K], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ " + of + ".", "«in» — the phrase is kāna's khabar.", "«-de» — şibh-i cümle kâne'nin haberi."), majrur("الْبِئْرِ", "bir", "«the well»", "«kuyu»", "فِي", punct=punct)]
def bir_ism_kanat(punct=None): return tok("الْبِئْرُ", "bir", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the well» — kāna's ism.", "«kuyu» — kâne'nin ismi.", punct=punct)
def haula_ism_anna(punct=None):
    return tok("هٰؤُلَاءِ", "haulai", "pron", ["inna-wa-akhawatuha", "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«these» — the plural demonstrative, built on kasra, as anna's ism.", "«bunlar» — cemi ism-i işâret, kesre üzere mebnî, enne'nin ismi.", punct=punct)
def humu_fasl(punct=None):
    return tok("هُمُ", "hum", "pron", ["damir-fasl", "inna-wa-akhawatuha"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ (وَيَجُوزُ جَعْلُهُ مُبْتَدَأً وَمَا بَعْدَهُ خَبَرُهُ)، وَضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«they» — the pronoun of separation, with no place in iʿrāb (or a mubtadaʾ with the relative as its khabar); its mīm takes a ḍamma before the wasl.", "«onlar» — fasl zamiri, mahalli yok (ya da mübtedâ, mevsûl haberi); mîmi iki sâkinin karşılaşması için zammeli.", punct=punct)
def alladhina_khabar(punct=None):
    return tok("الَّذِينَ", "alladhina", "pron", ["ism-mawsul", "inna-wa-akhawatuha"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«the ones who» — the plural relative, as anna's khabar.", "«onlar ki» — cemi ism-i mevsûl, enne'nin haberi.", punct=punct)


# ---------------------------------------------------------------- chapter-17 helpers
def qalu_(punct=":"): return qalu(punct=punct)
def lakum(punct=None, role="مُتَعَلِّقٌ بِمَا قَبْلَهُ", tags=()):
    return lahu("لَكُمْ", "كُمْ", "pron-2mp", role + ".", "«to you (pl.)».", "«size».", tags=tags, punct=punct)
def lana(punct=None, role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ", tags=("mubtada-khabar",)):
    return lahu("لَنَا", "نَا", "pron-1p", role + ".", "«we have» — the fronted khabar.", "«bizim var» — mukaddem haber.", tags=tags, punct=punct)
def akh_mubt_muakhkhar(punct=None):
    return tok("أَخٌ", "akh", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a brother» — the delayed mubtadaʾ.", "«bir kardeş» — muahhar mübtedâ.", punct=punct)
def ismuhu_name(name_full, name_lex, name_en, name_tr, punct=None):
    return [mudaf_pron("اسْمُهُ", "ism-name", "هُ", "pron-3ms", "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "«his name» — the mubtadaʾ of the describing clause", "«adı» — sıfat cümlesinin mübtedâsı", tags=["mubtada-khabar", "naat-sifa"]),
            tok(name_full, name_lex, "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِأَخٍ.", name_en + " — the khabar; the clause describes «a brother».", name_tr + " — haber; cümle «kardeş»in sıfatıdır.", punct=punct)]
def abu_kum(full="أَبُوكُمْ", role_ar="خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", en="«your father» — the khabar, rafʿ by the wāw of the five nouns", tr="«babanız» — haber, beş isimden olduğu için vâv ile merfû", tags=("mubtada-khabar",), punct=None):
    host = full[:-len("كُمْ")]
    return tok(full, "ab", "noun", list(tags) + ["five-nouns", "idafa-definiteness"], role_ar + "، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", en + "; annexed to the pronoun.", tr + "; zamire muzâf.", punct=punct, segments=[seg(host, "ab", "noun"), seg("كُمْ", "pron-2mp", "pron")])


# ---------------------------------------------------------------- chapter-18 helpers
def abihim(prep="إِلَى", punct=None, role="مُتَعَلِّقٌ بِمَا قَبْلَهُ"):
    full = {"إِلَى": "أَبِيهِمْ", "لِ": "لِأَبِيهِمْ"}[prep]
    segs = ([seg("لِ", "li", "prep")] if prep == "لِ" else []) + [seg("أَبِي", "ab", "noun"), seg("هِمْ", "pron-3mp", "pron")]
    return tok(full, "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], ("اللَّامُ حَرْفُ جَرٍّ، وَ" if prep == "لِ" else "") + f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — " + role + ".", "«their father» — in jarr by the yāʾ of the five nouns; annexed to the pronoun.", "«babaları» — beş isimden olduğu için yâ ile mecrur; zamire muzâf.", punct=punct, segments=segs)
def arsil(full="أَرْسِلْ", punct=None):
    return tok(full, "arsala", "verb", ["imperative-amr", "form-iv-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "«send» — an imperative on sukūn; «you» concealed.", "«gönder» — sükûn üzere mebnî emir; fâil gizli «sen».", punct=punct)
def akh_five(full, pron_seg, pron_lex, role_ar, sign, en, tr, punct=None, tags=()):
    host = full[:len(full) - len(pron_seg)]
    return tok(full, "akh", "noun", list(tags) + ["five-nouns", "idafa-definiteness"], role_ar + " وَعَلَامَةُ " + sign + " لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", en + " — one of the five nouns, declining by a letter; annexed to the pronoun.", tr + " — beş isimden, harfle i'rab olunur; zamire muzâf.", punct=punct, segments=[seg(host, "akh", "noun"), seg(pron_seg, pron_lex, "pron")])
def binyamin_maful(punct=None): return name_maful("بِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin'i»", punct=punct)
def hafiz_tamyiz(punct=None):
    return tok("حَافِظًا", "hafiz", "noun", ["tamyiz", "ism-fail"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ (مُحَوَّلٌ عَنِ الْمُبْتَدَأِ: حِفْظُ اللهِ خَيْرٌ).", "«as a keeper» — the tamyīz of «best» (turned from «Allah's keeping is best»).", "«koruyucu olarak» — temyiz («Allah'ın koruması hayırlıdır»dan çevrilmiş).", punct=punct)


# ---------------------------------------------------------------- chapter-19 helpers
def ikhwa_fail(full="الْإِخْوَةُ", punct=None): return ikhwa(full, "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"], punct=punct)
def binyamin_fail(punct=None): return fail_name("بِنْيَامِينُ", "binyamin", "«Binyāmīn»", "«Bünyamin»", punct=punct)
def indahu(punct=None, role="مُتَعَلِّقٌ بِمَا قَبْلَهُ", tags=()):
    return tok("عِنْدَهُ", "inda", "noun", ["maful-fih", "idafa-definiteness"] + list(tags), "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — " + role + ".", "«with him» — the adverb of place annexed to the pronoun.", "«yanında» — zamire muzâf mekân zarfı.", punct=punct, segments=[seg("عِنْدَ", "inda", "noun"), seg("هُ", "pron-3ms", "pron")])
def kayfa_sabil(wa=True, punct=None):
    return [tok("وَكَيْفَ" if wa else "كَيْفَ", "kayfa", "noun", ["al-istifham", "mubtada-khabar"] + (["anwa-al-waw"] if wa else []), W(wa) + "كَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", Wen(wa) + "«how» — the question noun as the fronted khabar.", Wtr(wa) + "«nasıl» — istifham ismi, mukaddem haber.", segments=(wa_("كَيْفَ", "kayfa", "noun") if wa else None)),
            mubt_raf("السَّبِيلُ", "sabil", "«the way»", "«yol»", extra=" مُؤَخَّرٌ"),
            ila(), tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "huruf-jarr"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِإِلَى.", "«that» — the demonstrative, in the place of jarr.", "«ona» — ism-i işâret, mahallen mecrur.", punct=punct)]
def bighayri_sabab(punct=None, role="مُتَعَلِّقٌ بِمَا قَبْلَهُ"):
    return [tok("بِغَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — " + role + ".", "«without» — bi + غَيْر, a muḍāf.", "«-sız» — bâ ve ğayr, muzâf.", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
            mi("سَبَبٍ", "sabab", "«a reason»", "«sebep»", punct=punct)]
def inna_kum(): return tok("إِنَّكُمْ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed you» — inna with its pronoun ism.", "«şüphesiz siz» — inne, zamir ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("كُمْ", "pron-2mp", "pron")])
def inna_na(): return tok("إِنَّا", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed we» — inna with its pronoun ism.", "«şüphesiz biz» — inne, zamir ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("نَا", "pron-1p", "pron")])
def la_khabar_pl(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha", "jam-mudhakkar-salim"] + list(tags), "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَالِاسْمُ خَبَرُ إِنَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", en + " — the slid lām of emphasis on inna's khabar, rafʿ by the wāw of the sound plural.", tr + " — inne'nin haberi üzerinde te'kid lâmı; cem-i müzekker sâlim olduğu için vâv ile merfû.", punct=punct, segments=[seg("لَ", "lam-ibtida", "part"), seg(full[1:], lex, "noun")])
def ta_allah(punct=None):
    return tok("تَاللهِ", "allah", "propn", ["huruf-jarr", "huruf-jarr-nawadir"], "التَّاءُ حَرْفُ جَرٍّ وَقَسَمٍ لَا تَدْخُلُ إِلَّا عَلَى لَفْظِ الْجَلَالَةِ، وَاللهِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِفِعْلِ قَسَمٍ مَحْذُوفٍ.", "«by Allah» — the tāʾ of the oath, a jarr letter that enters on the jalāla alone.", "«Allah'a yemin olsun» — kasem tâ'sı, yalnız lafza-i celâle gelen cer harfi.", punct=punct, segments=[seg("تَ", "ta-qasam", "prep"), seg("اللهِ", "allah", "propn")])
def jazauhu(role_ar, en, tr, punct=None, tags=()):
    return mudaf_pron("جَزَاؤُهُ", "jaza-answer", "هُ", "pron-3ms", role_ar, en, tr, tags=list(tags), punct=punct)


# ================================================================ chapter-20 helpers
def name_fi(full, lex, en, tr, punct=None, tags=()):
    return [fi(), tok(full, lex, "propn", ["huruf-jarr", "mamnu-min-sarf"] + list(tags), "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — in jarr by a fatḥa; a diptote name.", tr + " — fetha ile mecrur; gayr-i munsarıf özel isim.", punct=punct)]
def amsi(punct=None):
    return tok("أَمْسِ", "ams", "noun", ["maful-fih", "al-murab-wal-mabni-wal-irab"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ.", "«yesterday» — a time adverb, built on the kasra.", "«dün» — kesre üzere mebnî zaman zarfı.", punct=punct)
def al_yawm(punct=None, wa=False):
    return tok("وَالْيَوْمَ" if wa else "الْيَوْمَ", "yawm", "noun", ["maful-fih"] + (["atf-nasaq"] if wa else []), W(wa) + "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", Wen(wa) + "«today» — a time adverb, in naṣb.", Wtr(wa) + "«bugün» — mansub zaman zarfı.", punct=punct, segments=(wa_("الْيَوْمَ", "yawm", "noun") if wa else None))
def fujia(full="فُجِعَ", mudari=False, tags=(), punct=None):
    return tok(full, "fajaa", "verb", ["naib-al-fail"] + (["mudari-marfu"] if mudari else []) + list(tags), ("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ" if mudari else "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ") + "، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", ("«he is bereaved»" if mudari else "«he was bereaved»") + " — a passive; its deputy doer «he» is concealed.", ("«acıya boğuluyor»" if mudari else "«acıya boğuldu»") + " — meçhul; nâib-i fâil gizli «o».", punct=punct)
def yarjia(punct=None):
    return tok("يَرْجِعَ", "rajaa", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "«to return» — manṣūb after an; the doer «he» concealed.", "«dönmeyi» — en ile mansub; fâil gizli «o».", punct=punct)
def ila_name(full, lex, en, tr, punct=None):
    return [ila(), tok(full, lex, "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — in jarr by a fatḥa; a diptote.", tr + " — fetha ile mecrur; gayr-i munsarıf.", punct=punct)]
def inna_pron(full, pron_seg, pron_lex, en, tr, punct=None):
    return tok(full, "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", en + " — inna with the pronoun as its ism.", tr + " — inne; zamir ismi.", punct=punct, segments=[seg("إِنَّ", "inna", "part"), seg(pron_seg, pron_lex, "pron")])
def alayhi(full, pron_seg, pron_lex, en, tr, punct=None):
    return tok(full, "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِالْفِعْلِ قَبْلَهُ.", en, tr, punct=punct, segments=[seg("عَلَيْ", "ala", "prep"), seg(pron_seg, pron_lex, "pron")])
def ism_inna_muakhkhar(full, lex, en, tr, punct=None, part="إِنَّ"):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"], f"اسْمُ {part} مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en + f" — the delayed ism of {'anna' if part == 'أَنَّ' else 'inna'}.", tr + f" — {'enne' if part == 'أَنَّ' else 'inne'}'nin muahhar ismi.", punct=punct)
def thumma_(full="ثُمَّ", atf=True):
    return tok(full, "thumma", "conj" if atf else "part", ["atf-nasaq"] if atf else [], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي." if atf else "حَرْفُ اسْتِئْنَافٍ (ثُمَّ الْعَاطِفَةُ لِلْجُمَلِ).", "«then» — the conjunction of sequence with delay." if atf else "«then» — opening a new sentence.", "«sonra» — terâhî ifade eden atıf harfi." if atf else "«sonra» — istînaf harfi.")
def aydan(punct=None):
    return tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (آضَ يَئِيضُ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«also» — the absolute object of an elided verb.", "«de» — mahzuf fiilin mef'ûl-i mutlakı.", punct=punct)

# ================================================================ chapter-21 helpers
def allah_jarr(prep, en, tr, punct=None, tags=()):
    return tok("اللهِ", "allah", "propn", ["huruf-jarr"] + list(tags), f"لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", en + " — in jarr.", tr + " — mecrur.", punct=punct)
def yusuf_mubt(punct=None):
    return tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the mubtadaʾ.", "«Yusuf» — mübtedâ.", punct=punct)
def yusuf_khabar(punct=None, of=None):
    return tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar" if not of else "inna-wa-akhawatuha", "mamnu-min-sarf"], (f"خَبَرُ {of}" if of else "خَبَرٌ") + " مَرْفُوعٌ بِالضَّمَّةِ.", "«Yūsuf» — the khabar" + (f" of {of}" if of else "") + ".", "«Yusuf» — haber.", punct=punct)
def huwa_fasl(punct=None):
    return tok("هُوَ", "huwa", "pron", ["tawkid"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«(he)» — the pronoun of separation.", "«o» — fasıl zamiri.", punct=punct)
def huwa_mubt(full="هُوَ", wa=False, punct=None):
    return tok(full, "huwa", "pron", ["mubtada-khabar"] + (["anwa-al-waw"] if wa else []), ("الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ" if wa else "") + "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", Wen(wa) + "«he» — the mubtadaʾ.", Wtr(wa) + "«o» — mübtedâ.", punct=punct, segments=(wa_("هُوَ", "huwa", "pron") if wa else None))
def alladhi_(role_ar="فِي مَحَلِّ رَفْعٍ خَبَرٌ", en="the khabar", tr="haber", tags=("mubtada-khabar",)):
    return tok("الَّذِي", "alladhi", "pron", ["ism-mawsul"] + list(tags), "اسْمٌ مَوْصُولٌ مَبْنِيٌّ " + role_ar + ".", "«the one who» — the relative, " + en + ".", "«… olan» — ism-i mevsûl, " + tr + ".")
def hal_q(): return tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«is …?» — the question particle.", "«… mi?» — istifham harfi.")
def mata_(wa=False):
    return [tok("وَإِلَى" if wa else "إِلَى", "ila", "prep", ["huruf-jarr"] + (["atf-nasaq"] if wa else []), W(wa) + "حَرْفُ جَرٍّ.", Wen(wa) + "«until».", Wtr(wa) + "«-e kadar».", segments=(wa_("إِلَى", "ila", "prep") if wa else None)),
            tok("مَتَى", "mata", "pron", ["al-istifham", "huruf-jarr"], "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِإِلَى.", "«when» — the time question noun after ilā: «until when».", "«ne zamana» — zaman istifham ismi, ilâ ile mecrur.")]
def ara_1s(punct=None):
    return tok("أَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا.", "«shall I see» — rafʿ by an estimated ḍamma on the alif.", "«göreceğim» — elif üzerinde takdiri zamme ile merfû.", punct=punct)
def faqrahum(): return mudaf_pron("فَقْرَهُمْ", "faqr", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«their poverty»", "«yoksulluklarını»", tags=["maful-bihi"])
def wa_musibatahum(): return tok("وَمُصِيبَتَهُمْ", "musiba", "noun", ["atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَمُصِيبَتَهُمْ مَعْطُوفٌ عَلَى فَقْرَهُمْ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«and their calamity» — joined to «their poverty».", "«ve musibetlerini» — ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("مُصِيبَتَ", "musiba", "noun"), seg("هُمْ", "pron-3mp", "pron")])
def abi_1s(role_ar, en, tr, punct=None, tags=()):
    return tok("أَبِي", "ab", "noun", list(tags) + ["five-nouns", "ya-al-mutakallim", "idafa-definiteness"], role_ar + " بِحَرَكَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", en + " — the mark estimated before the speaker's yāʾ.", tr + " — mütekellim yâsından önce takdiri hareke.", punct=punct, segments=[seg("أَبِ", "ab", "noun"), seg("ي", "pron-1s", "pron")])
def yamlik(punct=None, hidden=True):
    return tok("يَمْلِكْ", "malaka", "verb", ["lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else "") + ".", "«could (not) hold» — jussive after lam.", "«tutamadı» — lem ile meczum.", punct=punct)
def nafsahu(punct=None): return mudaf_pron("نَفْسَهُ", "nafs", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«himself»", "«kendini»", tags=["maful-bihi"], punct=punct)
def tum_mazi(full, lex, en, tr, tags=(), punct=None, extra=""):
    host = full[:-3]
    return tok(full, lex, "verb", list(tags), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + extra + ".", en + " — the doers' tāʾ.", tr + " — fâil tâ'sı.", punct=punct, segments=[seg(host, lex, "verb"), seg("تُمْ", "pron-2mp", "pron")])

# ================================================================ §22 يظهر السر (pp. 61–64)
# ================================================================ chapter-22 helpers
def qad_mazi(full, lex, en, tr, hidden="هُوَ", tags=(), punct=None, wa=False, extra=""):
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + extra + ".", Wen(wa) + en + (f" — the doer «{hidden}» concealed." if hidden else "."), Wtr(wa) + tr + ".", punct=punct)
def wa_qad(role="hal"):
    return tok("وَقَدْ", "qad", "part", ["qad-harf"] + (["hal"] if role == "hal" else ["anwa-al-waw"]), ("الْوَاوُ حَالِيَّةٌ" if role == "hal" else "الْوَاوُ عَاطِفَةٌ") + "، وَقَدْ حَرْفُ تَحْقِيقٍ.", ("«when already»" if role == "hal" else "«and indeed»") + " — qad of affirmation.", ("«hâlbuki»" if role == "hal" else "«ve gerçekten»") + " — tahkik kad'ı.", segments=wa_("قَدْ", "qad", "part"))
def sirr_fail(full="السِّرُّ", punct=None): return fail(full, "sirr", "«the secret»", "«sır»", punct=punct)
def kayfa_(wa=True):
    return tok("وَكَيْفَ" if wa else "كَيْفَ", "kayfa", "pron", ["al-istifham", "hal"] + (["anwa-al-waw"] if wa else []), ("الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ" if wa else "") + "كَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", Wen(wa) + "«how» — the question noun, as the ḥāl.", Wtr(wa) + "«nasıl» — istifham ismi, hâl.", segments=(wa_("كَيْفَ", "kayfa", "pron") if wa else None))
def yatibu(full, lex="taba", en="«is pleasant»", tr="«tat verir»", tags=(), punct=None):
    return tok(full, lex, "verb", ["mudari-marfu", "hollow-verbs"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — a muḍāriʿ in rafʿ.", tr + " — merfû muzâri.", punct=punct)
def lahu_(role="مُتَعَلِّقٌ بِالْفِعْلِ قَبْلَهُ."): return lahu("لَهُ", "هُ", "pron-3ms", role, "«to him».", "«ona».")
def wa_la_atf(full, lex, en, tr, punct=None, tags=()):
    # two tokens: the joining wāw with the repeated lā, then the joined noun (a token never holds a space — the grader aligns by whitespace)
    return [tok("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا لِتَأْكِيدِ النَّفْيِ.", "«nor» — the wāw joins, the lā repeats the negation.", "«ne de» — vâv atıf, lâ nefyi tekrar eder.", segments=wa_("لَا", "la-nafiya", "part")),
            tok(full, lex, "noun", ["atf-nasaq"] + list(tags), "مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«" + en + "» — joined, in rafʿ.", "«" + tr + "» — ma'tûf, merfû.", punct=punct)]
def yaqub_mi(punct=None): return name_mudaf_ilayh("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub'un»", punct=punct)
def yusuf_mi(punct=None): return name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'un»", punct=punct)
def inni(punct=None): return inna_pron("إِنِّي", "ي", "pron-1s", "«indeed I»", "«ben»", punct=punct)
def amr_pl_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), punct=None, fa=False, wa=False):
    host = full[:len(full) - len(pron_seg)]; j = "وَ" if wa else ("فَ" if fa else "")
    segs = ([seg(j, "wa" if wa else "fa", "conj"), seg(host[2:], lex, "verb")] if j else [seg(host, lex, "verb")]) + [seg(pron_seg, pron_lex, "pron")]
    return tok(full, lex, "verb", ["imperative-amr", "maful-bihi"] + list(tags), (("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "الْفَاءُ عَاطِفَةٌ، وَ") if j else "") + "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", (Wen(wa) if wa else "") + en + " — an imperative of the plural; the attached pronoun its object.", (Wtr(wa) if wa else "") + tr + " — çoğul emir; bitişik zamir mef'ûl.", punct=punct, segments=segs)

# ================================================================ §23 يوسف يرسل إلى يعقوب (pp. 64–65)
sen("s1", "And Yūsuf longed to meet Yaʿqūb; and how would he not long for him, when the separation had been long.", "Yusuf, Yakub'a kavuşmayı özledi; ayrılık uzamışken onu nasıl özlemesin.", [
  mazi("وَاشْتَاقَ", "ishtaqa", "«longed»", "«özledi»", hidden=None, wa=True, tags=["form-viii-verbs", "hollow-verbs"]), yusuf_fail(), ila(),
  tok("لِقَاءِ", "liqa", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«meeting» — in jarr; a muḍāf.", "«kavuşmaya» — mecrur; muzâf."), yaqub_mi(punct="،"),
  kayfa_(), la_nafiya(), mudari("يَشْتَاقُ", "ishtaqa", "«would he long»", "«özlemesin»", hidden="هُوَ", tags=["form-viii-verbs", "hollow-verbs"]),
  tok("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«for him».", "«onu».", segments=[seg("إِلَيْ", "ila", "prep"), seg("هِ", "pron-3ms", "pron")]),
  wa_qad(), mazi("طَالَ", "tala-long", "«had grown long»", "«uzamıştı»", hidden=None, tags=["hollow-verbs", "hal"]), fail("الْفِرَاقُ", "firaq", "«the separation»", "«ayrılık»", punct=".")])
sen("s2", "And why should he be patient now, when the secret has come out.", "Sır ortaya çıkmışken şimdi niçin sabretsin.", [
  tok("وَلِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ جَرٍّ.", "«and why» — the lām of jarr on the question noun.", "«ve niçin» — cer lâmı ve istifham ismi.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مَاذَا", "ma-istifham", "pron")]),
  mudari("يَصْبِرُ", "sabara", "«should he be patient»", "«sabretsin»", hidden="هُوَ"),
  tok("الْآنَ", "al-an", "noun", ["maful-fih", "al-murab-wal-mabni-wal-irab"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«now» — a built time adverb.", "«şimdi» — mebnî zaman zarfı."),
  wa_qad(), mazi("ظَهَرَ", "zahara", "«has come out»", "«ortaya çıktı»", hidden=None, tags=["hal"]), sirr_fail(punct=".")])
sen("s3", "And how could drink and food be pleasant to him while to his father no drink, no food and no sleep is pleasant.", "Babasına ne içecek, ne yiyecek, ne uyku tat verirken, ona içecek ve yiyecek nasıl tat versin.", [
  kayfa_(), yatibu("يَطِيبُ"), lahu_(), fail("الشَّرَابُ", "sharab", "«drink»", "«içecek»"),
  tok("وَالطَّعَامُ", "taam", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالطَّعَامُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and food» — joined.", "«ve yiyecek» — ma'tûf.", segments=wa_("الطَّعَامُ", "taam", "noun")),
  tok("وَأَبُوهُ", "ab", "noun", ["hal", "anwa-al-waw", "five-nouns", "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ حَالِيَّةٌ، وَأَبُوهُ مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ حَالٌ.", "«while his father» — the wāw of ḥāl; the five-noun mubtadaʾ by its wāw.", "«babası ise» — hâl vâvı; beş isimden mübtedâ, vâv ile merfû.", segments=[seg("وَ", "wa", "conj"), seg("أَبُو", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  la_nafiya(), yatibu("يَطِيبُ", tags=["mubtada-khabar"]), lahu_(), fail("شَرَابٌ", "sharab", "«drink»", "«içecek»"),
  ] + wa_la_atf("طَعَامٌ", "taam", "food", "yiyecek") + wa_la_atf("مَنَامٌ", "manam", "sleep", "uyku", punct="."))
sen("s4", "The secret has been uncovered, the secret has come out, and Allah has willed that Yaʿqūb's eye be cooled.", "Sır açığa çıktı, sır ortaya çıktı ve Allah Yakub'un gözünün aydın olmasını diledi.", [
  tok("قَدِ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ، كُسِرَتْ دَالُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«indeed» — qad, its dāl given a kasra for the meeting of two sukūns.", "«gerçekten» — iki sükûnun karşılaşması için dâl'i kesreli kad."),
  mazi("انْكَشَفَ", "inkashafa", "«has been uncovered»", "«açığa çıktı»", hidden=None, tags=["form-vii-verbs"]), sirr_fail(punct="،"),
  wa_qad(role="atf"), mazi("ظَهَرَ", "zahara", "«has come out»", "«ortaya çıktı»", hidden=None), sirr_fail(punct="،"),
  wa_qad(role="atf"), mazi("أَرَادَ", "arada", "«has willed»", "«diledi»", hidden=None, tags=["form-iv-verbs", "hollow-verbs"]), allah_fail(), an_(obj_of="أَرَادَ"),
  tok("تَقَرَّ", "qarra", "verb", ["an-masdariyya", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«be cooled» — manṣūb after an (a doubled verb).", "«aydın olmasını» — en ile mansub (muzaaf fiil)."),
  tok("عَيْنُ", "ayn", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the eye (of)» — the doer; a muḍāf.", "«gözü» — fâil; muzâf."), yaqub_mi(punct=".")])
sen("s5", "And Yaʿqūb had gone blind from much weeping and grief", "Yakub çok ağlamaktan ve hüzünden kör olmuştu", [
  kana(), yaqub_ism_kana(), qad_(),
  tok("عَمِيَ", "amiya", "verb", [K, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«had gone blind» — the clause is kāna's khabar.", "«kör olmuştu» — cümle kâne'nin haberi."),
  min_(), tok("كَثْرَةِ", "kathra", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«much (of)» — in jarr; a muḍāf.", "«çokluğundan» — mecrur; muzâf."),
  mi("الْبُكَاءِ", "bukaa", "«weeping»", "«ağlama»"),
  tok("وَالْحُزْنِ", "huzn", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْحُزْنِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and grief» — joined.", "«ve hüzün» — ma'tûf.", segments=wa_("الْحُزْنِ", "huzn", "noun"))])
sen("s6", "So Yūsuf said:", "Yusuf dedi:", [fa_mazi("فَقَالَ", "qala", "«said»", "«dedi»", hidden=None, tags=["hollow-verbs"]), yusuf_fail(punct=":")])
sen("s7", "«Go with this shirt of mine and cast it over my father's face: he will come seeing; and bring me your family, all together.» (Yūsuf 12:93)", "«Şu gömleğimi götürün ve babamın yüzüne koyun, gözleri açılır; ve bütün ailenizi bana getirin.» (Yûsuf 12:93)", quran([
  amr_pl("اذْهَبُوا", "dhahaba", "«go»", "«gidin»"),
  tok("بِقَمِيصِي", "qamis", "noun", ["huruf-jarr", "ya-al-mutakallim", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَقَمِيصِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«with my shirt».", "«gömleğimle».", segments=[seg("بِ", "bi", "prep"), seg("قَمِيصِ", "qamis", "noun"), seg("ي", "pron-1s", "pron")]),
  ishara("هٰذَا", "hadha", "jarr", "«this»", "«bu»", tags=["naat-sifa"]),
  amr_pl_enc("فَأَلْقُوهُ", "alqa", "هُ", "pron-3ms", "«and cast it»", "«ve onu koyun»", fa=True, tags=["naqis-verbs"]), ala(),
  tok("وَجْهِ", "wajh", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the face (of)».", "«yüzüne»."), abi_1s("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "«my father»", "«babamın»"),
  tok("يَأْتِ", "ata", "verb", ["jawab-al-talab", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he will come» — jussive as the answer to the command, its weak letter dropped.", "«gelir» — talebin cevabı olarak meczum; illet harfi düşmüş."),
  tok("بَصِيرًا", "basir", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«seeing» — the ḥāl.", "«görür hâlde» — hâl.", punct="،"),
  tok("وَأْتُونِي", "ata", "verb", ["atf-nasaq", "imperative-amr", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَفِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and bring me» — the imperative; the nūn of protection, the yāʾ its object.", "«ve bana getirin» — emir; vikaye nûnu, yâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("أْتُو", "ata", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("بِأَهْلِكُمْ", "ahl", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَهْلِ مَجْرُورٌ بِالْكَسْرَةِ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«your family».", "«ailenizi».", segments=[seg("بِ", "bi", "prep"), seg("أَهْلِ", "ahl", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("أَجْمَعِينَ", "ajmain", "noun", ["tawkid", "jam-mudhakkar-salim"], "تَوْكِيدٌ مَعْنَوِيٌّ لِأَهْلِكُمْ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ.", "«all together» — the emphasis of totality, jarr by the yāʾ.", "«hepsini» — manevî te'kid, yâ ile mecrur.", punct=".")]))
# ================================================================ §24 يعقوب عند يوسف (pp. 65–67)
sen("s8", "And when the men set out with Yūsuf's shirt to Canaan, Yaʿqūb sensed the scent of Yūsuf and said: «Indeed I find the smell of Yūsuf.» (Yūsuf 12:94)", "Adamlar Yusuf'un gömleğiyle Kenan'a doğru yola çıkınca Yakub Yusuf'un kokusunu duydu ve dedi: «Ben Yusuf'un kokusunu alıyorum.» (Yûsuf 12:94)", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve … -ınca».", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("سَارَ", "sara-travel", "«set out»", "«yola çıktı»", hidden=None, tags=["hollow-verbs"]), fail("الرِّجَالُ", "rajul", "«the men»", "«adamlar»", tags=["jam-taksir"]),
  tok("بِقَمِيصِ", "qamis", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَقَمِيصِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«with the shirt (of)».", "«gömleğiyle».", segments=[seg("بِ", "bi", "prep"), seg("قَمِيصِ", "qamis", "noun")]), yusuf_mi()] + ila_name("كَنْعَانَ", "kanan", "«Canaan»", "«Kenan»", punct="،") + [
  mazi("أَحَسَّ", "ahassa", "«sensed»", "«duydu»", hidden=None, tags=["form-iv-verbs", "doubled-verbs"]), yaqub_fail(),
  tok("رَائِحَةَ", "raiha", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the scent (of)».", "«kokusunu»."), yusuf_mi(punct="،"),
  qala(full="وَقَالَ", wa=True, punct=":")] + quran([
  inni(), tok("لَأَجِدُ", "wajada", "verb", ["tawkid", "mudari-marfu", "inna-wa-akhawatuha", "mithal-verbs"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَأَجِدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I do find» — the sliding lām on the muḍāriʿ; the clause is inna's khabar.", "«gerçekten alıyorum» — müzahlaka lâmı; cümle inne'nin haberi.", segments=[seg("لَ", "lam-ibtida", "part"), seg("أَجِدُ", "wajada", "verb")]),
  tok("رِيحَ", "rih", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the smell (of)».", "«kokusunu»."), yusuf_mi(punct=".")]))
sen("s9", "«They said: By Allah, you are surely in your old error.» (Yūsuf 12:95)", "«Dediler: Allah'a yemin olsun, sen hâlâ eski şaşkınlığındasın.» (Yûsuf 12:95)", quran([
  qalu(punct=None), ta_allah(), inna_pron("إِنَّكَ", "كَ", "pron-2ms", "«indeed you»", "«sen»"),
  tok("لَفِي", "fi", "prep", ["tawkid", "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ الْمُزَحْلَقَةُ، وَفِي حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ خَبَرُ إِنَّ.", "«surely in» — the sliding lām; the phrase is inna's khabar.", "«gerçekten … -dasın» — müzahlaka lâmı; şibh-i cümle haber.", segments=[seg("لَ", "lam-ibtida", "part"), seg("فِي", "fi", "prep")]),
  mudaf_pron("ضَلَالِكَ", "dalal", "كَ", "pron-2ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«your error»", "«şaşkınlığında»", tags=["huruf-jarr"]),
  nat_jarr("الْقَدِيمِ", "qadim", "«old»", "«eski»", punct=".")]))
sen("s10", "But Yaʿqūb was truthful: «Then when the bearer of good news came, he cast it over his face and he regained his sight. He said: Did I not tell you that I know from Allah what you do not know?» (Yūsuf 12:96)", "Fakat Yakub doğru söylüyordu: «Müjdeci gelince gömleği yüzüne koydu, gözleri açılıverdi. Dedi: Size, Allah'tan sizin bilmediğinizi bilirim dememiş miydim?» (Yûsuf 12:96)", [
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا يَعْمَلُ.", "«but» — the lightened lākin, which governs nothing.", "«fakat» — amel etmeyen muhaffef lâkin.", segments=wa_("لٰكِنْ", "lakin", "part")),
  kana_bare(), yaqub_ism_kana(), khabar_kana("صَادِقًا", "sadiq", "«truthful»", "«doğru söyleyen»", punct="،")] + quran([
  tok("فَلَمَّا", "lamma", "part", [], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ.", "«then when».", "«… -ınca».", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  tok("أَنْ", "an-masdariyya", "part", [], "زَائِدَةٌ بَعْدَ لَمَّا.", "«(that)» — the extra an after lammā.", "«(ki)» — lemmâ'dan sonra zâid en."),
  mazi("جَاءَ", "jaa", "«came»", "«geldi»", hidden=None, tags=["hollow-verbs"]), fail("الْبَشِيرُ", "bashir", "«the bearer of good news»", "«müjdeci»"),
  verb_enc("أَلْقَاهُ", "alqa", "هُ", "pron-3ms", "«he cast it»", "«onu koydu»", mudari=False, hidden="هُوَ", tags=["naqis-verbs", "form-iv-verbs"]), ala(),
  mudaf_pron("وَجْهِهِ", "wajh", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his face»", "«yüzüne»", tags=["huruf-jarr"]),
  fa_mazi("فَارْتَدَّ", "irtadda", "«and he turned back»", "«ve döndü»", hidden="هُوَ", tags=["form-viii-verbs", "doubled-verbs"]),
  tok("بَصِيرًا", "basir", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«seeing» — the ḥāl.", "«görür hâlde» — hâl.", punct="،"),
  qala(punct=None), tok("أَلَمْ", "lam-jazim", "part", ["al-istifham", "lam-jazim", "khuruj-al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«did I not?» — the question hamza over lam.", "«… -medim mi?» — takrirî istifham hemzesi ve lem.", segments=[seg("أَ", "hamza-istifham", "part"), seg("لَمْ", "lam-jazim", "part")]),
  tok("أَقُلْ", "qala", "verb", ["lam-jazim", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«(did I not) say» — jussive, its middle letter dropped.", "«demedim mi» — meczum; ayn harfi düşmüş."),
  lakum(punct=None, role="مُتَعَلِّقٌ بِأَقُلْ"), inni(),
  tok("أَعْلَمُ", "alima", "verb", ["mudari-marfu", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I know» — the clause is inna's khabar.", "«bilirim» — cümle inne'nin haberi."),
  min_(full="مِنَ"), allah_jarr("مِنْ", "«from Allah»", "«Allah'tan»"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what».", "«-ini»."), la_nafiya(),
  khamsa("تَعْلَمُونَ", "alima", "«you know»", "«bilirsiniz»", extra_ar=" — صِلَةُ الْمَوْصُولِ", punct=".")]))
sen("s11", "«They said: O our father, ask forgiveness for us for our sins; indeed we were sinners.» (Yūsuf 12:97)", "«Dediler: Ey babamız, günahlarımız için bize mağfiret dile; biz gerçekten hatalıydık.» (Yûsuf 12:97)", quran([
  qalu(punct=None)] + ya_abana() + [
  tok("اسْتَغْفِرْ", "istaghfara", "verb", ["imperative-amr", "form-x-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«ask forgiveness» — an imperative.", "«mağfiret dile» — emir."),
  lana(punct=None, role="مُتَعَلِّقٌ بِاسْتَغْفِرْ", tags=()),
  mudaf_pron("ذُنُوبَنَا", "dhanb", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«our sins»", "«günahlarımızı»", tags=["maful-bihi", "jam-taksir"]),
  inna_na(), tok("كُنَّا", "kana", "verb", [K, "hollow-verbs", "inna-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهَا — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«we were» — the clause is inna's khabar.", "«idik» — cümle inne'nin haberi.", segments=[seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("خَاطِئِينَ", "khati", "noun", [K, "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«sinners» — kāna's khabar.", "«hatalı» — kâne'nin haberi.")]))
sen("s12", "«He said: I shall ask my Lord to forgive you; indeed He is the Forgiving, the Merciful.» (Yūsuf 12:98)", "«Dedi: Sizin için Rabbimden mağfiret dileyeceğim; şüphesiz O Gafûr'dur, Rahîm'dir.» (Yûsuf 12:98)", quran([
  qala(punct=None), tok("سَوْفَ", "sawfa", "part", [], "حَرْفُ تَنْفِيسٍ وَاسْتِقْبَالٍ.", "«shall» — the particle of the future.", "«-ecek» — istikbal harfi."),
  tok("أَسْتَغْفِرُ", "istaghfara", "verb", ["mudari-marfu", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا.", "«I shall ask forgiveness».", "«mağfiret dileyeceğim»."),
  lakum(punct=None, role="مُتَعَلِّقٌ بِأَسْتَغْفِرُ"),
  tok("رَبِّي", "rabb", "noun", ["maful-bihi", "ya-al-mutakallim", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the object.", "«Rabbimden» — mef'ûl.", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
  inna_pron("إِنَّهُ", "هُ", "pron-3ms", "«indeed He»", "«şüphesiz O»"), huwa_fasl(),
  khabar_inna("الْغَفُورُ", "ghafur", "«the Forgiving»", "«Gafûr»"), khabar_inna("الرَّحِيمُ", "rahim-merciful", "«the Merciful»", "«Rahîm»", extra=" — خَبَرٌ ثَانٍ", punct=".")]))
sen("s13", "And when Yaʿqūb reached Egypt, Yūsuf received him — and do not ask about the joy and gladness of the two.", "Yakub Mısır'a varınca Yusuf onu karşıladı; ikisinin sevincini ve mutluluğunu hiç sorma.", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve … -ınca».", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("وَصَلَ", "wasala", "«reached»", "«vardı»", hidden=None, tags=["mithal-verbs"]), yaqub_fail()] + ila_name("مِصْرَ", "misr", "«Egypt»", "«Mısır»") + [
  verb_enc("اسْتَقْبَلَهُ", "istaqbala", "هُ", "pron-3ms", "«received him»", "«onu karşıladı»", mudari=False, hidden=None, tags=["form-x-verbs"]), yusuf_fail(punct="،"),
  tok("وَلَا", "la", "part", ["anwa-al-waw", "lam-jazim"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«and do not» — the prohibiting lā.", "«ve … -ma» — nehiy lâ'sı.", segments=wa_("لَا", "la", "part")),
  tok("تَسْأَلْ", "saala", "verb", ["lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«(do not) ask» — jussive after the prohibiting lā.", "«sorma» — nehiy lâ'sı ile meczum."),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«-i»."),
  mudaf_pron("فَرَحِهِمَا", "farah", "هِمَا", "pron-3d", "مَجْرُورٌ بِعَنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«the joy of the two»", "«ikisinin sevincini»", tags=["huruf-jarr"]),
  tok("وَسُرُورِهِمَا", "surur", "noun", ["atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَسُرُورِ مَعْطُوفٌ مَجْرُورٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«and their gladness» — joined.", "«ve mutluluğunu» — ma'tûf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("سُرُورِ", "surur", "noun"), seg("هِمَا", "pron-3d", "pron")])])
sen("s14", "It was a memorable day in Egypt, and it was a blessed day.", "Mısır'da unutulmaz bir gündü ve mübarek bir gündü.", [
  kana_hidden(), khabar_kana("يَوْمًا", "yawm", "«a day»", "«bir gün»"), nat_nasb("مَشْهُودًا", "mashhud", "«memorable»", "«unutulmaz»", tags=["ism-maful"])] + fi_misr() + [
  kana_hidden(), khabar_kana("يَوْمًا", "yawm", "«a day»", "«bir gün»"), nat_nasb("مُبَارَكًا", "mubarak", "«blessed»", "«mübarek»", punct=".", tags=["ism-maful"])])
sen("s15", "And Yūsuf raised his parents upon the throne, and they all fell down in prostration to Yūsuf.", "Yusuf ana-babasını tahta çıkardı ve hepsi Yusuf'a secdeye kapandılar.", [
  mazi("وَرَفَعَ", "rafaa", "«raised»", "«çıkardı»", hidden=None, wa=True), yusuf_fail(),
  tok("أَبَوَيْهِ", "ab", "noun", ["maful-bihi", "al-muthanna", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his two parents» — the object, naṣb by the yāʾ of the dual, its nūn dropped for the annexation.", "«ana-babasını» — mef'ûl; tesniye, yâ ile mansub, nûnu izafet için düşmüş.", segments=[seg("أَبَوَيْ", "ab", "noun"), seg("هِ", "pron-3ms", "pron")]),
  ala(), majrur("الْعَرْشِ", "arsh", "«the throne»", "«taht»", "عَلَى"),
  mazi_pl("وَوَقَعُوا", "waqaa", "«and they fell»", "«ve kapandılar»", wa=True, tags=["mithal-verbs"]),
  mudaf_pron("كُلُّهُمْ", "kull", "هُمْ", "pron-3mp", "تَوْكِيدٌ مَعْنَوِيٌّ لِلْوَاوِ مَرْفُوعٌ بِالضَّمَّةِ", "«all of them»", "«hepsi»", tags=["tawkid"]),
  tok("سُجَّدًا", "sajid", "noun", ["hal", "jam-taksir"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ سَاجِدٍ.", "«prostrating» — the ḥāl; a broken plural of سَاجِد.", "«secde eder hâlde» — hâl; sâcid'in cem-i mükesseri."),
  li_name("لِيُوسُفَ", "yusuf", "«to Yūsuf»", "«Yusuf'a»", punct=".")])
sen("s16", "And Yūsuf said: «This is the interpretation of my dream of before; my Lord has made it true.» (Yūsuf 12:100)", "Yusuf dedi: «İşte bu, önceki rüyamın tabiridir; Rabbim onu gerçek kıldı.» (Yûsuf 12:100)", [
  qala(full="وَقَالَ", wa=True, punct=None), yusuf_fail(punct=":")] + quran([
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»", tags=["mubtada-khabar"]),
  tok("تَأْوِيلُ", "tawil", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the interpretation (of)» — the khabar.", "«tabiri» — haber."),
  tok("رُؤْيَايَ", "ruya-dream", "noun", ["idafa-definiteness", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my dream».", "«rüyamın».", segments=[seg("رُؤْيَا", "ruya-dream", "noun"), seg("يَ", "pron-1s", "pron")]),
  min_(), tok("قَبْلُ", "qabl", "noun", ["huruf-jarr", "al-murab-wal-mabni-wal-irab"], "ظَرْفٌ مَقْطُوعٌ عَنِ الْإِضَافَةِ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ.", "«before».", "«önceki»."),
  qad_(), verb_enc("جَعَلَهَا", "jaala", "هَا", "pron-3fs", "«has made it»", "«onu kıldı»", mudari=False, hidden=None),
  tok("رَبِّي", "rabb", "noun", ["fail", "ya-al-mutakallim", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the doer.", "«Rabbim» — fâil.", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
  maful("حَقًّا", "haqq", "«true»", "«gerçek»", punct=".", extra_ar=" — مَفْعُولٌ بِهِ ثَانٍ")]))
sen("s17", "«Indeed I saw eleven stars and the sun and the moon; I saw them prostrating to me.» (Yūsuf 12:4)", "«Ben on bir yıldızı, güneşi ve ayı gördüm; onları bana secde eder hâlde gördüm.» (Yûsuf 12:4)", quran([
  inni(), mazi_1s("رَأَيْتُ", "raa", "«I saw»", "«gördüm»", tags=["inna-wa-akhawatuha", "naqis-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  tok("أَحَدَ", "ahad", "noun", ["maful-bihi", "al-murab-wal-mabni-wal-irab"], "مَفْعُولٌ بِهِ — الْعَدَدُ الْمُرَكَّبُ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ نَصْبٍ.", "«eleven» — the compound number, built on the fatḥa of both parts, as the object.", "«on bir» — iki cüzü fetha üzere mebnî mürekkep sayı, mef'ûl."),
  tok("عَشَرَ", "ashar", "noun", ["al-murab-wal-mabni-wal-irab"], "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«(eleven)» — the second part of the compound number.", "«(on bir)» — mürekkep sayının ikinci cüzü."),
  tok("كَوْكَبًا", "kawkab", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«stars» — the tamyīz of the number.", "«yıldız» — sayının temyizi."),
  tok("وَالشَّمْسَ", "shams", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالشَّمْسَ مَعْطُوفٌ مَنْصُوبٌ.", "«and the sun».", "«ve güneşi».", segments=wa_("الشَّمْسَ", "shams", "noun")),
  tok("وَالْقَمَرَ", "qamar", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْقَمَرَ مَعْطُوفٌ مَنْصُوبٌ.", "«and the moon».", "«ve ayı».", segments=wa_("الْقَمَرَ", "qamar", "noun")),
  tok("رَأَيْتُهُمْ", "raa", "verb", ["maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ أَوَّلُ.", "«I saw them» — the tāʾ its doer, the pronoun its first object.", "«onları gördüm» — tâ fâil, zamir birinci mef'ûl.", segments=[seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("لِي", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِسَاجِدِينَ.", "«to me».", "«bana».", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  tok("سَاجِدِينَ", "sajid", "noun", ["hal", "jam-mudhakkar-salim", "ism-fail"], "حَالٌ (أَوْ مَفْعُولٌ بِهِ ثَانٍ) مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ.", "«prostrating» — the ḥāl (or the second object), naṣb by the yāʾ.", "«secde eder hâlde» — hâl (veya ikinci mef'ûl), yâ ile mansub.", punct=".")]))
sen("s18", "And Yūsuf praised Allah with a good and abundant praise.", "Yusuf Allah'a güzel ve bol bir hamd ile hamdetti.", [
  mazi("وَحَمِدَ", "hamida", "«praised»", "«hamdetti»", hidden=None, wa=True), yusuf_fail(), tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah'a» — mef'ûl."),
  tok("حَمْدًا", "hamd", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a praise» — the absolute object.", "«bir hamd ile» — mef'ûl-i mutlak."),
  nat_nasb("طَيِّبًا", "tayyib", "«good»", "«güzel»"), nat_nasb("كَثِيرًا", "kathir", "«abundant»", "«bol»", punct=".")])
sen("s19", "And Yūsuf gave thanks for that with a great thanksgiving", "Yusuf buna büyük bir şükürle şükretti", [
  mazi("وَشَكَرَ", "shakara", "«gave thanks»", "«şükretti»", hidden=None, wa=True), yusuf_fail(), ala(), ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«buna»"),
  tok("شُكْرًا", "shukr", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a thanksgiving» — the absolute object.", "«bir şükürle» — mef'ûl-i mutlak."), nat_nasb("عَظِيمًا", "azim", "«great»", "«büyük»")])
sen("s20", "And Yaʿqūb and the house of Yaʿqūb stayed in Egypt a long time", "Yakub ve Yakub'un ailesi uzun bir zaman Mısır'da kaldı", [
  mazi("وَبَقِيَ", "baqiya", "«stayed»", "«kaldı»", hidden=None, wa=True, tags=["naqis-verbs"]), yaqub_fail(),
  tok("وَآلُ", "al-family", "noun", ["atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَآلُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«and the house (of)» — joined; a muḍāf.", "«ve ailesi» — ma'tûf; muzâf.", segments=wa_("آلُ", "al-family", "noun")), yaqub_mi()] + fi_misr() + [
  tok("زَمَنًا", "zaman-period", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a time» — an adverb of time.", "«bir zaman» — zaman zarfı."), nat_nasb("طَوِيلًا", "tawil-long", "«long»", "«uzun»")])
sen("s21", "And Yaʿqūb and his wife died in Egypt.", "Yakub ve eşi Mısır'da öldü.", [
  mazi("وَمَاتَ", "mata-die", "«died»", "«öldü»", hidden=None, wa=True, tags=["hollow-verbs"]), yaqub_fail(),
  tok("وَزَوْجُهُ", "zawj", "noun", ["atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَزَوْجُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his wife» — joined.", "«ve eşi» — ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("زَوْجُ", "zawj", "noun"), seg("هُ", "pron-3ms", "pron")])] + fi_misr(punct="."))

# ---------------------------------------------------------------- glossary
NEW = {
 "tala-long": G("tala-long", "طَالَ", "ط و ل", "verb", "to grow long, to last long (a hollow verb, يَطُولُ)", "uzamak, uzun sürmek (ecvef, yetûlü)", 2, form="I"),
 "al-an": G("al-an", "الْآنَ", None, "noun", "now (a built time adverb)", "şimdi (mebnî zaman zarfı)", 1),
 "taba": G("taba", "طَابَ", "ط ي ب", "verb", "to be pleasant, to be good (a hollow verb, يَطِيبُ)", "hoş olmak, tat vermek (ecvef, yetîbü)", 2, form="I"),
 "inkashafa": G("inkashafa", "اِنْكَشَفَ", "ك ش ف", "verb", "to be uncovered (Form VII)", "açığa çıkmak (infiâl bâbı)", 3, form="VII"),
 "qarra": G("qarra", "قَرَّ", "ق ر ر", "verb", "to settle, to be cooled (قَرَّتْ عَيْنُهُ = his eye was cooled, he rejoiced)", "yerleşmek, (gözü) aydın olmak", 3, form="I"),
 "amiya": G("amiya", "عَمِيَ", "ع م ي", "verb", "to go blind", "kör olmak", 2, form="I"),
 "bukaa": G("bukaa", "بُكَاء", "ب ك ي", "noun", "weeping (maṣdar of بَكَى)", "ağlama (bekâ'nın masdarı)", 2),
 "sara-travel": G("sara-travel", "سَارَ", "س ي ر", "verb", "to travel, to set out (a hollow verb, يَسِيرُ)", "yola çıkmak, yürümek (ecvef, yesîru)", 2, form="I"),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but — the lightened lākin, which governs nothing", "fakat — amel etmeyen muhaffef lâkin", 2),
 "bashir": G("bashir", "بَشِير", "ب ش ر", "noun", "a bearer of good news", "müjdeci", 2, plural="بُشَرَاء"),
 "irtadda": G("irtadda", "اِرْتَدَّ", "ر د د", "verb", "to turn back, to return (Form VIII, doubled; اِرْتَدَّ بَصِيرًا = regained his sight)", "geri dönmek (iftiâl bâbı, muzaaf)", 3, form="VIII"),
 "sawfa": G("sawfa", "سَوْفَ", None, "part", "shall — the particle of the (more distant) future", "-ecek — (uzak) istikbal harfi", 1),
 "ghafur": G("ghafur", "غَفُور", "غ ف ر", "noun", "the Forgiving (a name of Allah; a sighat mubalagha)", "Gafûr, çok bağışlayan (Allah'ın adı; mübalağa sigası)", 2),
 "farah": G("farah", "فَرَح", "ف ر ح", "noun", "joy (maṣdar of فَرِحَ)", "sevinç (feriha'nın masdarı)", 1),
 "surur": G("surur", "سُرُور", "س ر ر", "noun", "gladness, happiness", "mutluluk, sürur", 2),
 "mashhud": G("mashhud", "مَشْهُود", "ش ه د", "noun", "witnessed, memorable (ism mafʿūl of شَهِدَ)", "şahit olunan, unutulmaz (şehide'nin ism-i mef'ûlü)", 3),
 "mubarak": G("mubarak", "مُبَارَك", "ب ر ك", "noun", "blessed (ism mafʿūl of بَارَكَ)", "mübarek (bâreke'nin ism-i mef'ûlü)", 2),
 "al-family": G("al-family", "آل", "أ و ل", "noun", "the family, the house (of)", "aile, hanedan", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("ishtaqa", "اشتاق"), ("liqa", "لقاء"), ("firaq", "فراق"), ("limadha", "لماذا"), ("zahara", "ظهر"), ("sharab", "شراب"), ("manam", "منام"), ("arada", "أراد"), ("ayn", "عين"), ("kathra", "كثرة"), ("qamis", "قميص"), ("alqa", "ألقى"), ("wajh", "وجه"), ("basir", "بصير"), ("ahl", "أهل"), ("ajmain", "أجمع"), ("rajul", "رجل"), ("ahassa", "أحس"), ("raiha", "رائحة"), ("wajada", "وجد"), ("rih", "ريح"), ("dalal", "ضلال"), ("qadim", "قديم"), ("sadiq", "صادق"), ("jaa", "جاء"), ("istaghfara", "استغفر"), ("dhanb", "ذنب"), ("wasala", "وصل"), ("istaqbala", "استقبل"), ("rafaa", "رفع"), ("arsh", "عرش"), ("waqaa", "وقع"), ("sajid", "ساجد"), ("ruya-dream", "رؤيا"), ("jaala", "جعل"), ("haqq", "حق"), ("ahad", "أحد"), ("ashar", "عشر"), ("kawkab", "كوكب"), ("shams", "شمس"), ("qamar", "قمر"), ("hamida", "حمد"), ("hamd", "حمد"), ("shakara", "شكر"), ("shukr", "شكر"), ("azim", "عظيم"), ("mata-die", "مات"), ("zawj", "زوج")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("tala-long", "taba", "inkashafa", "qarra", "amiya", "sara-travel", "irtadda"): mo["verbs"].pop(_k, None)
put_morph(mo, "tala-long", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "طَال", "طُل", "طُول", "طُل", "طُول", "طُل", "طُول", "طَائِل", note="لَازِمٌ: طَالَ الْفِرَاقُ — طَالَ يَطُولُ، طُلْتُ."))
put_morph(mo, "taba", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "طَاب", "طِب", "طِيب", "طِب", "طِيب", "طِب", "طِيب", "طَائِب", note="لَازِمٌ: طَابَ الطَّعَامُ — طَابَ يَطِيبُ، طِبْتُ."))
put_morph(mo, "inkashafa", _sg.derived("مِنْ بَابِ الِانْفِعَالِ", "اِنْفَعَلَ يَنْفَعِلُ", "َ", "اِنْكَشَف", "نْكَشِف", "اِنْكَشِف", "اِنْكِشَاف", "مُنْكَشِف", note="لَازِمٌ (مُطَاوِعُ كَشَفَ): اِنْكَشَفَ السِّرُّ."))
put_morph(mo, "amiya", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ يَائِيٌّ", _sg.BABS["samia"][1], "عَمًى", "أَعْمَى (وَالْقِيَاسُ عَامٍ)",
                                 _sg.mazi_naqis_kasra("عَمِ", "عَمُوا"), _sg.mudari_naqis("َ", "عْم", "a"), _sg.amr_naqis("اِعْم", "a"),
                                 "يَعْمَى", "يَعْمَ", "تَعْمَ", note="نَاقِصٌ مِنْ بَابِ سَمِعَ: عَمِيَ يَعْمَى — عَمِيتُ، عَمُوا؛ لَازِمٌ: عَمِيَ الرَّجُلُ."))
put_morph(mo, "sara-travel", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "سَار", "سِر", "سِير", "سِر", "سِير", "سِر", "سَيْر", "سَائِر", note="لَازِمٌ: سَارَ الرِّجَالُ — سَارَ يَسِيرُ، سِرْتُ."))
put_morph(mo, "qarra", _sg.entry(_sg.BABS["samia"][0] + " — مُضَاعَفٌ", _sg.BABS["samia"][1], "قُرَّة (وَقَرَار)", "قَارّ", _sg.mazi14("قَرّ", "قَرِر"), _sg.mudari14("َ", "قَرّ", "قْرَر"),
                                 ["قَرَّ", "قَرَّا", "قَرُّوا", "قَرِّي", "قَرَّا", "اِقْرَرْنَ"], "يَقَرَّ", "يَقَرَّ", "تَقَرَّ",
                                 note="مُضَاعَفٌ مِنْ بَابِ سَمِعَ: قَرَّ يَقَرُّ — قَرِرْتُ، يَقْرَرْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ؛ لَازِمٌ: قَرَّتْ عَيْنُهُ."))
put_morph(mo, "irtadda", _sg.entry("مِنْ بَابِ الِافْتِعَالِ — مُضَعَّفٌ", "اِفْتَعَلَ يَفْتَعِلُ", "اِرْتِدَاد", "مُرْتَدّ",
                                   _sg.mazi14("اِرْتَدّ", "اِرْتَدَد"), _sg.mudari14("َ", "رْتَدّ", "رْتَدِد"), ["اِرْتَدَّ", "اِرْتَدَّا", "اِرْتَدُّوا", "اِرْتَدِّي", "اِرْتَدَّا", "اِرْتَدِدْنَ"],
                                   "يَرْتَدَّ", "يَرْتَدَّ", "تَرْتَدَّ", note="لَازِمٌ — مُضَعَّفٌ (مُطَاوِعُ رَدَّ): الْمِثْلَانِ يُدْغَمَانِ حَيْثُ تَحَرَّكَ الثَّانِي (اِرْتَدَّ) وَيُفَكَّانِ أَمَامَ السَّاكِنِ (اِرْتَدَدْتُ)؛ الْجَزْمُ بِالْفَتْحِ: اِرْتَدَّ بَصِيرًا."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 22 (print pp. 64–67, «أَحْسَنُ الْقَصَصِ» sections 23 «يُوسُفُ يُرْسِلُ إِلَى يَعْقُوبَ» and 24 «يَعْقُوبُ عِنْدَ يُوسُفَ»): Yūsuf's longing and the shirt with 12:93 (s7), the scent with 12:94 (s8, the aya marked inside the line), "
          "12:95 (s9), 12:96 (s10, marked inside the line after the author's «but Yaʿqūb was truthful»), 12:97 (s11), 12:98 (s12), Yaʿqūb received in Egypt, the prostration, 12:100 (s16, inside the line) and 12:4 (s17), the praise and the stay. "
          "One printed line is one sentence; s5, s19 and s20 end as the print does, without a stop; the print sets its ayas in round brackets, marked here with the guillemets of the earlier chapters.")
ADD_TR = (" Yirmi ikinci bölüm (basılı s. 64–67, «أَحْسَنُ الْقَصَصِ» 23. kısım «يُوسُفُ يُرْسِلُ إِلَى يَعْقُوبَ» ve 24. kısım «يَعْقُوبُ عِنْدَ يُوسُفَ»): Yusuf'un özlemi ve gömlek 12:93 ile (s7), koku 12:94 ile (s8, ayet satır içinde işaretli), "
          "12:95 (s9), 12:96 (s10, yazarın «fakat Yakub doğru söylüyordu» sözünden sonra satır içinde işaretli), 12:97 (s11), 12:98 (s12), Yakub'un Mısır'da karşılanışı, secde, 12:100 (s16, satır içinde) ve 12:4 (s17), hamd ve kalış. "
          "Basılı her satır bir cümledir; s5, s19 ve s20 baskıdaki gibi noktasız biter; baskı ayetleri yuvarlak parantezle verir, burada önceki bölümlerin tırnaklarıyla işaretlenmiştir.")
write_out(22, S, TITLE, ADD_EN, ADD_TR, "pp. 64–67", GLOSS_ADD)
report(22, S, GLOSS_ADD, ())
