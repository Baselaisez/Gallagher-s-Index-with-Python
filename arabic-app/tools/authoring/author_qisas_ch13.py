# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 13: «حِكْمَةُ يُوسُفَ، وَمَوْعِظَةُ التَّوْحِيدِ» — «أَحْسَنُ الْقَصَصِ» sections 10–11 (print pp. 41–44):
Yūsuf's reflection on need and obedience, his patience and the promise of the interpretation (Yūsuf 12:37); the sermon of tawḥīd —
why his Lord taught him (12:38), the one creed for all (12:38), the many lords against the One (12:39, 35:40, 31:11), the names the
fathers invented and the straight religion (12:40). Every printed line is one sentence, split at the print's own full stops; the
vowelling is the print's.  python3 tools/authoring/author_qisas_ch13.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "حِكْمَةُ يُوسُفَ، وَمَوْعِظَةُ التَّوْحِيدِ", "en": "Yūsuf's wisdom, and the sermon of tawḥīd", "tr": "Yusuf'un hikmeti ve tevhid vaazı"}
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
    return tok("مِمَّا", "min", "prep", ["huruf-jarr", "ism-mawsul", "mubtada-khabar"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«of what» — min fused with the relative mā; the phrase is the khabar.", "«-den» — min ile ism-i mevsûl mâ bitişik; şibh-i cümle haber.", segments=[seg("مِنْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")])
def amr_pl(full, lex, en, tr, tags=(), punct=None, wa=False, fa=False, extra=""):
    j = "وَ" if wa else ("فَ" if fa else "")
    return tok(full, lex, "verb", ["imperative-amr"] + list(tags), (("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "الْفَاءُ عَاطِفَةٌ، وَ") if j else "") + "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ" + extra + ".", (Wen(wa) if wa else ("«and so» + " if fa else "")) + en + " — a plural imperative, built on the dropped nūn; the wāw is the doer.", (Wtr(wa) if wa else ("«ve» + " if fa else "")) + tr + " — nûnun hazfi üzere mebnî cemi emir; vâv fâildir.", punct=punct, segments=([seg(j, "wa" if wa else "fa", "conj"), seg(full[2:], lex, "verb")] if j else None))
def ila_al(full, lex, en, tr, punct=None, wa=False):
    return [tok("وَإِلَى" if wa else "إِلَى", "ila", "prep", ["huruf-jarr"] + (["atf-nasaq"] if wa else []), W(wa) + "حَرْفُ جَرٍّ.", Wen(wa) + "«to».", Wtr(wa) + "«-e».", segments=(wa_("إِلَى", "ila", "prep") if wa else None)), majrur(full, lex, en, tr, "إِلَى", punct=punct)]

# ================================================================ §10 حكمة يوسف (pp. 41–42)
sen("s1", "Yūsuf said to himself:", "Yusuf kendi kendine dedi:", [
  qala(punct=None, hidden=None), yusuf_fail(), fi(), mudaf_pron("نَفْسِهِ", "nafs", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«himself» — in jarr", "«kendisi» — mecrur", tags=["huruf-jarr"], punct=":")])
sen("s2", "Indeed need has driven the two men to me.", "Şüphesiz ihtiyaç bu iki adamı bana sürükledi.", [
  inna(), ism_inna("الْحَاجَةَ", "haja", "«need»", "«ihtiyaç»"),
  mazi_ta("سَاقَتِ", "saqa", "«has driven»", "«sürükledi»", tags=["inna-wa-akhawatuha", "hollow-verbs"], extra="، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("الرَّجُلَيْنِ", "rajul", "noun", ["maful-bihi", "al-muthanna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُثَنًّى.", "«the two men» — the object; the dual's naṣb shows as a yāʾ.", "«iki adamı» — mef'ûl; tesniyenin nasbı yâ ile."),
  tok("إِلَيَّ", "ila", "prep", ["huruf-jarr", "ya-al-mutakallim"], "إِلَى حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِسَاقَتْ.", "«to me».", "«bana».", punct=".", segments=[seg("إِلَ", "ila", "prep"), seg("يَّ", "pron-1s", "pron")])])
sen("s3", "And indeed the one in need grows soft and submits.", "Ve şüphesiz ihtiyaç sahibi yumuşar ve boyun eğer.", [
  inna(full="وَإِنَّ", wa=True), tok("صَاحِبَ", "sahib", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the one (of)» — the ism of inna; a muḍāf.", "«sahibi» — inne'nin ismi; muzâf."), mi("الْحَاجَةِ", "haja", "«need»", "«ihtiyaç»"),
  mudari("يَلِينُ", "lana", "«grows soft»", "«yumuşar»", tags=["inna-wa-akhawatuha", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("وَيَخْضَعُ", "khadaa-submit", "verb", ["atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَخْضَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and submits» — joined onto the khabar.", "«ve boyun eğer» — habere matuf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَخْضَعُ", "khadaa-submit", "verb")])])
sen("s4", "And indeed the one in need obeys and listens.", "Ve şüphesiz ihtiyaç sahibi itaat eder ve dinler.", [
  inna(full="وَإِنَّ", wa=True), tok("صَاحِبَ", "sahib", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the one (of)» — the ism of inna; a muḍāf.", "«sahibi» — inne'nin ismi; muzâf."), mi("الْحَاجَةِ", "haja", "«need»", "«ihtiyaç»"),
  mudari("يُطِيعُ", "ataa", "«obeys»", "«itaat eder»", tags=["inna-wa-akhawatuha", "hollow-verbs", "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("وَيَسْمَعُ", "samia", "verb", ["atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَسْمَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and listens» — joined onto the khabar.", "«ve dinler» — habere matuf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَسْمَعُ", "samia", "verb")])])
sen("s5", "So had I said something to the two of them, they would have listened, and the people of the prison would have listened.", "O ikisine bir şey söyleseydim, ikisi de dinlerdi, zindan ehli de dinlerdi.", [
  tok("فَلَوْ", "law", "part", ["hikayat-al-hal"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ (حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ).", "«so if» — the unreal law: the condition failed, so its answer failed.", "«şayet … -seydi» — cezmetmeyen şart harfi lev (imtinâ harfi).", segments=[seg("فَ", "fa", "conj"), seg("لَوْ", "law", "part")]),
  tok("قُلْتُ", "qala", "verb", ["hikayat-al-hal", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — فِعْلُ الشَّرْطِ.", "«I said» — the verb of the condition; the speaker's tāʾ its doer.", "«söyleseydim» — şart fiili; mütekellim tâ'sı fâil.", segments=[seg("قُلْ", "qala", "verb"), seg("تُ", "pron-1s", "pron")]),
  lahuma(), maful("شَيْئًا", "shay", "«something»", "«bir şey»"),
  tok("لَسَمِعَا", "samia", "verb", ["hikayat-al-hal"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَسَمِعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرُ الِاثْنَيْنِ فَاعِلٌ — جَوَابُ لَوْ.", "«they two would have listened» — the lām of the answer of law; the alif of the two its doer.", "«ikisi dinlerdi» — lev'in cevabının lâmı; tesniye elifi fâil.", segments=[seg("لَ", "lam-jawab", "part"), seg("سَمِعَ", "samia", "verb"), seg("ا", "pron-3md", "pron")]),
  mazi("وَسَمِعَ", "samia", "«and would have listened»", "«ve dinlerdi»", hidden=None, wa=True, tags=["atf-nasaq"]), *ahl_sijn("فَاعِلٌ", "the doer", "fâil", punct=".")])
sen("s6", "But Yūsuf did not hurry.", "Fakat Yusuf acele etmedi.", [
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«fakat» — tahfifli lâkin, amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنْ", "lakin", "part")]),
  tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ.", "«Yūsuf» — the mubtadaʾ.", "«Yusuf» — mübtedâ."),
  lam_jazim(), tok("يَسْتَعْجِلْ", "istajala", "verb", ["lam-jazim", "form-x-verbs", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«did (not) hurry» — jazm after lam; the clause is the khabar.", "«acele etmedi» — lem ile meczûm; cümle haber.", punct=".")])
sen("s7", "Rather he said to the two of them:", "Aksine o ikisine dedi:", [
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«rather» — the particle of turning away.", "«aksine» — idrâb harfi."),
  qala(punct=None, hidden="هُوَ"), lahuma(punct=":")])
sen("s8", "I will tell you both the interpretation of the dream before your food comes to you.", "Yemeğiniz size gelmeden önce rüyanın tabirini ikinize bildireceğim.", [
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the mubtadaʾ.", "«ben» — mübtedâ."),
  verb_enc("أُخْبِرُكُمَا", "akhbara", "كُمَا", "pron-2d", "«I tell you both»", "«ikinize bildiririm»", hidden="أَنَا", tags=["form-iv-verbs", "mubtada-khabar"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  tok("بِتَأْوِيلِ", "tawil", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَتَأْوِيلِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the interpretation (of)» — a muḍāf.", "«tabirini» — muzâf.", segments=[seg("بِ", "bi", "prep"), seg("تَأْوِيلِ", "tawil", "noun")]),
  tok("الرُّؤْيَا", "ruya-dream", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the dream» — the muḍāf ilayh.", "«rüyanın» — muzâfun ileyh."),
  tok("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«before» — an adverb of time; a muḍāf.", "«önce» — zaman zarfı; muzâf."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "idafa-definiteness"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that» — the masdar-maker; its clause is the muḍāf ilayh of «before».", "«-mesi» — masdariye; cümlesi «önce»nin muzâfun ileyhi."),
  mansub_enc("يَأْتِيَكُمَا", "ata", "كُمَا", "pron-2d", "«comes to you both»", "«ikinize gelir»", tags=["naqis-verbs"]),
  mudaf_pron("طَعَامُكُمَا", "taam", "كُمَا", "pron-2d", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "«your food» — the doer", "«yemeğiniz» — fâil", tags=["fail"], punct=".")])
sen("s9", "So the two sat down and were reassured.", "İkisi oturdu ve rahatladı.", [
  tok("فَجَلَسَا", "jalasa", "verb", ["atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَجَلَسَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرُ الِاثْنَيْنِ فَاعِلٌ.", "«so the two sat» — the alif of the two is the doer.", "«böylece ikisi oturdu» — tesniye elifi fâil.", segments=[seg("فَ", "fa", "conj"), seg("جَلَسَ", "jalasa", "verb"), seg("ا", "pron-3md", "pron")]),
  dual_mazi("وَاطْمَأَنَّا", "itmaanna", "«and were reassured»", "«ve rahatladı»", tags=["atf-nasaq", "doubled-verbs"], punct=".")])
sen("s10", "Then Yūsuf said to the two of them:", "Sonra Yusuf o ikisine dedi:", [
  tok("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "«then» — joining with a delay.", "«sonra» — terâhî ile tertip atfı."),
  qala(punct=None, hidden=None), lahuma(), yusuf_fail(punct=":")])
sen("s11", "I am learned in the interpretation of dreams; «that is of what my Lord has taught me.» (Yūsuf 12:37)", "Ben rüya tabirini bilirim; «işte bu, Rabbimin bana öğrettiklerindendir.» (Yûsuf 12:37)", [
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the mubtadaʾ.", "«ben» — mübtedâ."),
  tok("عَالِمٌ", "alim-scholar", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«learned» — the khabar.", "«bilen» — haber."),
  tok("بِتَأْوِيلِ", "tawil", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَتَأْوِيلِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِعَالِمٌ.", "«in the interpretation (of)» — a muḍāf, hanging on «learned».", "«tabirini» — muzâf; «bilen»e bağlı.", segments=[seg("بِ", "bi", "prep"), seg("تَأْوِيلِ", "tawil", "noun")]),
  tok("الرُّؤْيَا", "ruya-dream", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«dreams» — the muḍāf ilayh.", "«rüyanın» — muzâfun ileyh.", punct="،"),
  *quran([dhalikuma(), mimma(), *allamani_rabbi(punct=".", extra=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا")])])
sen("s12", "So the two rejoiced and were reassured.", "İkisi sevindi ve rahatladı.", [
  tok("فَفَرِحَا", "fariha", "verb", ["atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَفَرِحَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرُ الِاثْنَيْنِ فَاعِلٌ.", "«so the two rejoiced» — the alif of the two is the doer.", "«böylece ikisi sevindi» — tesniye elifi fâil.", segments=[seg("فَ", "fa", "conj"), seg("فَرِحَ", "fariha", "verb"), seg("ا", "pron-3md", "pron")]),
  dual_mazi("وَاطْمَأَنَّا", "itmaanna", "«and were reassured»", "«ve rahatladı»", tags=["atf-nasaq", "doubled-verbs"], punct=".")])
sen("s13", "And here Yūsuf found the opportunity, and began his sermon.", "İşte burada Yusuf fırsatı buldu ve vaazına başladı.", [
  tok("وَهُنَا", "huna", "noun", ["maful-fih", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُنَا اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and here» — the demonstrative of place, an adverb.", "«ve burada» — mekân işâreti, zarf.", segments=[seg("وَ", "wa", "conj"), seg("هُنَا", "huna", "noun")]),
  mazi("وَجَدَ", "wajada", "«found»", "«buldu»", hidden=None, tags=["mithal-verbs"]), yusuf_fail(), maful("الْفُرْصَةَ", "fursa", "«the opportunity»", "«fırsatı»"),
  fa_mazi("فَبَدَأَ", "badaa", "«and began»", "«ve başladı»", hidden="هُوَ", tags=["atf-nasaq"]),
  mudaf_pron("مَوْعِظَتَهُ", "mawiza", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his sermon» — the object", "«vaazını» — mef'ûl", tags=["maful-bihi"], punct=".")])

# ================================================================ §11 موعظة التوحيد (pp. 42–44)
sen("s14", "Yūsuf said: «that is of what my Lord has taught me.» (Yūsuf 12:37)", "Yusuf dedi: «işte bu, Rabbimin bana öğrettiklerindendir.» (Yûsuf 12:37)", [
  qala(punct=None, hidden=None), yusuf_fail(), *quran([dhalikuma(), mimma(), *allamani_rabbi(punct=".", extra=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا")])])
sen("s15", "But Allah does not give His knowledge to everyone.", "Fakat Allah ilmini herkese vermez.", [
  wa_lakinna(), allah_ism(part="لٰكِنَّ"), la_nafiya(),
  neg_mudari("يُؤْتِي", "aataa", "«gives»", "«verir»", hidden="هُوَ", tags=["inna-wa-akhawatuha", "naqis-verbs", "form-iv-verbs"], extra=" (مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ) — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  mudaf_pron("عِلْمَهُ", "ilm", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ", "«His knowledge» — the first object", "«ilmini» — birinci mef'ûl", tags=["maful-bihi"]),
  tok("كُلَّ", "kull", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«every (one)» — the second object; a muḍāf.", "«her» — ikinci mef'ûl; muzâf."),
  tok("أَحَدٍ", "ahad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«one» — the muḍāf ilayh.", "«biri» — muzâfun ileyh.", punct=".")])
sen("s16", "Indeed Allah does not give His knowledge to the idolater.", "Şüphesiz Allah ilmini müşriğe vermez.", [
  inna(), allah_ism(), la_nafiya(),
  neg_mudari("يُؤْتِي", "aataa", "«gives»", "«verir»", hidden="هُوَ", tags=["inna-wa-akhawatuha", "naqis-verbs", "form-iv-verbs"], extra=" (مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ) — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  mudaf_pron("عِلْمَهُ", "ilm", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ", "«His knowledge» — the first object", "«ilmini» — birinci mef'ûl", tags=["maful-bihi"]),
  tok("الْمُشْرِكَ", "mushrik", "noun", ["maful-bihi", "ism-fail"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the idolater» — the second object.", "«müşriği» — ikinci mef'ûl.", punct=".")])
sen("s17", "Do you two know why my Lord taught me?", "Rabbimin bana niçin öğrettiğini biliyor musunuz?", [
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«do …?» — the question particle.", "«… mi?» — istifham harfi."),
  tok("تَعْرِفَانِ", "arafa", "verb", ["afal-khamsa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ ضَمِيرُ الِاثْنَيْنِ فَاعِلٌ.", "«you two know» — one of the five verbs; the alif of the two its doer.", "«ikiniz biliyor» — ef'âl-i hamseden; tesniye elifi fâil."),
  tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ جَرٍّ — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ تَعْرِفَانِ.", "«why» — the lām of jarr over the question word; the clause is the object of «know».", "«niçin» — cer lâmı ve istifham ismi; cümle «biliyor»un mef'ûlü.", segments=[seg("لِ", "li", "prep"), seg("مَاذَا", "madha", "pron")]),
  *allamani_rabbi(punct="؟")])
sen("s18", "Because I have left the way of the people of idolatry.", "Çünkü ben şirk ehlinin yolunu bıraktım.", [
  li_pron("لِأَنِّي", "pron-1s", "«because I» — the lām of cause over anna with the speaker's yāʾ as its ism.", "«çünkü ben» — ta'lil lâmı ve enne; mütekellim yâ'sı ismi.", "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ اسْمُهَا."),
  mazi_1s("تَرَكْتُ", "taraka", "«I left»", "«bıraktım»", tags=["inna-wa-akhawatuha"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  tok("طَرِيقَ", "tariq", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the way (of)» — the object; a muḍāf.", "«yolunu» — mef'ûl; muzâf."),
  tok("أَهْلِ", "ahl", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the people (of)» — a muḍāf ilayh that is itself a muḍāf.", "«ehli» — muzâfun ileyh ve muzâf."),
  mi("الشِّرْكِ", "shirk", "«idolatry»", "«şirk»", punct=".")])
sen("s19", "«And I have followed the creed of my fathers Ibrāhīm, Isḥāq and Yaʿqūb.» (Yūsuf 12:38)", "«Ve atalarım İbrahim, İshak ve Yakub'un dinine uydum.» (Yûsuf 12:38)", quran([
  mazi_1s("وَاتَّبَعْتُ", "ittabaa", "and I have followed", "ve uydum", tags=["form-viii-verbs"], wa=True),
  tok("مِلَّةَ", "milla", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the creed (of)» — the object; a muḍāf.", "«dinini» — mef'ûl; muzâf."),
  tok("آبَائِي", "ab", "noun", ["idafa-definiteness", "ya-al-mutakallim", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my fathers» — the muḍāf ilayh, annexed in turn to the speaker's yāʾ.", "«atalarım» — muzâfun ileyh; mütekellim yâ'sına muzâf.", segments=[seg("آبَائِ", "ab", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["badal", "mamnu-min-sarf"], "بَدَلٌ مِنْ آبَائِي مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the badal of «my fathers»; a diptote, its jarr a fatḥa.", "«İbrahim» — «atalarım»dan bedel; gayr-i munsarıf, ceri fetha."),
  tok("وَإِسْحٰقَ", "ishaq", "propn", ["atf-nasaq", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَإِسْحٰقَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Isḥāq» — joined; a diptote.", "«ve İshak» — matuf; gayr-i munsarıf.", segments=[seg("وَ", "wa", "conj"), seg("إِسْحٰقَ", "ishaq", "propn")]),
  tok("وَيَعْقُوبَ", "yaqub", "propn", ["atf-nasaq", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَيَعْقُوبَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Yaʿqūb» — joined; a diptote.", "«ve Yakub» — matuf; gayr-i munsarıf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَعْقُوبَ", "yaqub", "propn")])]))
sen("s20", "«It was not for us to associate anything with Allah.» (Yūsuf 12:38)", "«Allah'a herhangi bir şeyi ortak koşmak bize yaraşmazdı.» (Yûsuf 12:38)", quran([
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not» — the negating mā.", "«değil» — nefiy mâ'sı."),
  kana_bare(),
  tok("لَنَا", "li", "prep", ["huruf-jarr", K], "اللَّامُ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«for us» — the phrase is kāna's fronted khabar.", "«bize» — şibh-i cümle kâne'nin öne alınmış haberi.", segments=[seg("لَ", "li", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", K], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ مُؤَخَّرٌ.", "«that» — its clause is kāna's delayed ism.", "«-mak» — masdariye; cümlesi kâne'nin geciktirilmiş ismi."),
  tok("نُشْرِكَ", "ashraka", "verb", ["an-masdariyya", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ.", "«(that) we associate» — naṣb after an; the doer «we» concealed.", "«ortak koşmamız» — en ile mansub; fâil gizli «biz»."),
  tok("بِاللهِ", "allah", "propn", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«with Allah».", "«Allah'a».", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ زَائِدٌ.", "«(any)» — the redundant min.", "«(hiç)» — zâid min."),
  tok("شَيْءٍ", "shay", "noun", ["maful-bihi", "huruf-jarr"], "مَفْعُولٌ بِهِ مَجْرُورٌ لَفْظًا بِمِنِ الزَّائِدَةِ مَنْصُوبٌ مَحَلًّا.", "«anything» — the object, in jarr by the letter and in naṣb by place.", "«bir şeyi» — mef'ûl; lafzen mecrur, mahallen mansub.", punct=".")]))
sen("s21", "Yūsuf said:", "Yusuf dedi:", [qala(punct=None, hidden=None), yusuf_fail(punct=":")])
sen("s22", "And this tawḥīd is not for us alone.", "Ve bu tevhid yalnız bize değildir.", [
  tok("وَهٰذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — the demonstrative, the mubtadaʾ.", "«ve bu» — ism-i işâret, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هٰذَا", "hadha", "pron")]),
  tok("التَّوْحِيدُ", "tawhid", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "«tawḥīd» — the badal of the demonstrative.", "«tevhid» — ism-i işâretten bedel."),
  tok("لَيْسَ", "laysa", "verb", [K, "mubtada-khabar"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.", "«is not» — the frozen laysa with «it» concealed; the clause is the khabar.", "«değildir» — câmid leyse; ismi gizli; cümle haber."),
  tok("لَنَا", "li", "prep", ["huruf-jarr", K], "اللَّامُ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ لَيْسَ.", "«for us» — the phrase is laysa's khabar.", "«bize» — şibh-i cümle leyse'nin haberi.", segments=[seg("لَ", "li", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("فَقَطْ", "faqat", "part", ["huruf-tanbih"], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ، مَبْنِيٌّ.", "«only» — qaṭ with its ornamental fāʾ.", "«yalnız» — zâid fâ ve kat.", punct=".")])
sen("s23", "Rather it is for all people.", "Aksine o bütün insanlar içindir.", [
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«rather» — the particle of turning away.", "«aksine» — idrâb harfi."),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«it» — the mubtadaʾ.", "«o» — mübtedâ."),
  tok("لِلنَّاسِ", "nas", "noun", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَالنَّاسِ مَجْرُورٌ بِالْكَسْرَةِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«for the people» — the phrase is the khabar.", "«insanlar için» — şibh-i cümle haber.", segments=[seg("لِ", "li", "prep"), seg("لنَّاسِ", "nas", "noun")]),
  tok("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«all» — the ḥāl.", "«hepsi» — hâl.", punct=".")])
sen("s24", "«That is of the bounty of Allah upon us and upon the people, but most of the people do not give thanks.» (Yūsuf 12:38)", "«Bu, Allah'ın bize ve insanlara olan lütfundandır; fakat insanların çoğu şükretmez.» (Yûsuf 12:38)", quran([
  ishara("ذٰلِكَ", "dhalika", "raf", "«that»", "«bu»"),
  tok("مِنْ", "min", "prep", ["huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«of» — the phrase is the khabar.", "«-den» — şibh-i cümle haber."),
  tok("فَضْلِ", "fadl", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the bounty (of)» — a muḍāf.", "«lütfu» — muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh."),
  tok("عَلَيْنَا", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِفَضْلِ.", "«upon us».", "«bize».", segments=[seg("عَلَيْ", "ala", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("وَعَلَى", "ala", "prep", ["huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَعَلَى حَرْفُ جَرٍّ.", "«and upon».", "«ve … üzerine».", segments=[seg("وَ", "wa", "conj"), seg("عَلَى", "ala", "prep")]),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlar»", "عَلَى"),
  wa_lakinna(), *akthar_nas(), la_nafiya(),
  khamsa("يَشْكُرُونَ", "shakara", "«give thanks»", "«şükrederler»", tags=["inna-wa-akhawatuha", "la-nafiya"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ", punct=".")]))
sen("s25", "And here Yūsuf stopped and asked the two of them:", "Ve burada Yusuf durdu ve o ikisine sordu:", [
  tok("وَهُنَا", "huna", "noun", ["maful-fih", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُنَا اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and here» — the demonstrative of place, an adverb.", "«ve burada» — mekân işâreti, zarf.", segments=[seg("وَ", "wa", "conj"), seg("هُنَا", "huna", "noun")]),
  mazi("وَقَفَ", "waqafa", "«stopped»", "«durdu»", hidden=None, tags=["mithal-verbs"]), yusuf_fail(),
  verb_enc("وَسَأَلَهُمَا", "saala", "هُمَا", "pron-3d", "«and asked the two of them»", "«ve o ikisine sordu»", mudari=False, hidden="هُوَ", wa=True, tags=["atf-nasaq"], punct=":")])
sen("s26", "You say: the lord of the land, and the lord of the sea, and the lord of provision, and the lord of the rain.", "Siz diyorsunuz: karanın rabbi, denizin rabbi, rızkın rabbi, yağmurun rabbi.", [
  khamsa("تَقُولُونَ", "qala", "«you say»", "«diyorsunuz»", tags=["hollow-verbs", "maful-bihi"], extra_ar=" — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", punct=":"), *four_lords(khabar=True)])
sen("s27", "And we say: Allah is the Lord of the worlds.", "Biz ise diyoruz: Allah âlemlerin Rabbidir.", [
  tok("وَنَحْنُ", "nahnu", "pron", ["mubtada-khabar", "anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَنَحْنُ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and we» — the mubtadaʾ.", "«biz ise» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("نَحْنُ", "nahnu", "pron")]),
  tok("نَقُولُ", "qala", "verb", ["mubtada-khabar", "mudari-marfu", "hollow-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«say» — the clause is the khabar; what is said is its object.", "«diyoruz» — cümle haber; söylenen söz mef'ûl.", punct=":"),
  tok("اللهُ", "allah", "propn", ["mubtada-khabar"], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — the mubtadaʾ.", "«Allah» — mübtedâ."),
  tok("رَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the Lord (of)» — the khabar; a muḍāf.", "«Rabbi» — haber; muzâf."),
  tok("الْعَالَمِينَ", "alam", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«the worlds» — the muḍāf ilayh; jarr by the yāʾ, attached to the sound plural.", "«âlemlerin» — muzâfun ileyh; sâlim çoğula mülhak, ceri yâ ile.", punct=".")])
sen("s28", "«Are diverse lords better, or Allah, the One, the Subduer?» (Yūsuf 12:39)", "«Çeşitli rabler mi daha hayırlı, yoksa tek ve kahredici olan Allah mı?» (Yûsuf 12:39)", quran([
  tok("ءَأَرْبَابٌ", "rabb", "noun", ["al-istifham", "mubtada-khabar", "jam-taksir"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَأَرْبَابٌ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ (سَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ وَصْفُهَا).", "«are lords …?» — the question hamza over the mubtadaʾ; the nakira may open because it is described.", "«rabler mi …?» — istifham hemzesi; mübtedâ (nekre, sıfatla caiz).", segments=[seg("ءَ", "hamza-istifham", "part"), seg("أَرْبَابٌ", "rabb", "noun")]),
  tok("مُتَفَرِّقُونَ", "mutafarriq", "noun", ["naat-sifa", "jam-mudhakkar-salim", "ism-fail"], "نَعْتٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«diverse» — the naʿt; rafʿ by the wāw of the sound plural.", "«çeşitli» — sıfat; sâlim çoğulun refi vâv ile."),
  tok("خَيْرٌ", "khayr", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ (اسْمُ تَفْضِيلٍ عَلَى غَيْرِ قِيَاسٍ).", "«better» — the khabar; an irregular elative.", "«daha hayırlı» — haber; kıyas dışı ism-i tafdil."),
  tok("أَمِ", "am", "part", ["atf-nasaq", "al-istifham"], "أَمِ الْمُتَّصِلَةُ حَرْفُ عَطْفٍ (مُعَادِلَةٌ لِلْهَمْزَةِ)، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — the am that pairs with the question hamza; its kasra for the meeting of two sukūns.", "«yoksa» — hemzeye denk gelen muttasıl em; kesresi iki sâkin için."),
  tok("اللهُ", "allah", "propn", ["atf-nasaq"], "لَفْظُ الْجَلَالَةِ مَعْطُوفٌ عَلَى أَرْبَابٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — joined onto «lords».", "«Allah» — «rabler»e matuf."),
  tok("الْوَاحِدُ", "wahid", "noun", ["naat-sifa"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the One» — the naʿt.", "«tek olan» — sıfat."),
  tok("الْقَهَّارُ", "qahhar", "noun", ["naat-sifa", "sighat-mubalagha"], "نَعْتٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ (صِيغَةُ مُبَالَغَةٍ عَلَى فَعَّال).", "«the Subduer» — a second naʿt; an intensive on فَعَّال.", "«kahredici» — ikinci sıfat; fe'âl vezninde mübalağa.", punct="؟")]))
sen("s29", "Where is the lord of the land, and the lord of the sea, and the lord of provision, and the lord of the rain?", "Nerede karanın rabbi, denizin rabbi, rızkın rabbi, yağmurun rabbi?", [
  tok("أَيْنَ", "ayna", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ خَبَرٌ مُقَدَّمٌ.", "«where» — the question word of place, the fronted khabar.", "«nerede» — mekân istifhamı, öne alınmış haber."), *four_lords(khabar=False, punct="؟")])
sen("s30", "«Show me what they have created of the earth; or have they a share in the heavens?» (Fāṭir 35:40)", "«Gösterin bana, yerden neyi yaratmışlar? Yoksa onların göklerde bir ortaklığı mı var?» (Fâtır 35:40)", quran([
  tok("أَرُونِي", "ara", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi", "form-iv-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.", "«show me» — a plural imperative; the wāw its doer, the speaker's yāʾ its first object.", "«gösterin bana» — cemi emir; vâv fâil, mütekellim yâ'sı birinci mef'ûl.", segments=[seg("أَرُو", "ara", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("مَاذَا", "madha", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِخَلَقُوا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ لِأَرُونِي.", "«what» — the fronted object of «created»; the clause is the second object of «show».", "«neyi» — «yarattılar»ın öne alınmış mef'ûlü; cümle «gösterin»in ikinci mef'ûlü."),
  mazi_pl("خَلَقُوا", "khalaqa", "«they have created»", "«yarattılar»"),
  min_(full="مِنَ"), majrur("الْأَرْضِ", "ard", "«the earth»", "«yer»", "مِنْ"),
  tok("أَمْ", "am", "part", ["atf-nasaq"], "أَمِ الْمُنْقَطِعَةُ بِمَعْنَى بَلْ وَالْهَمْزَةِ.", "«or (rather)» — the disjoined am, «nay — do they…?»", "«yoksa» — munkatı' em: bel ve hemze mânâsında."),
  lahu("لَهُمْ", "هُمْ", "pron-3mp", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«have they» — the fronted khabar.", "«onların var mı» — öne alınmış haber."),
  tok("شِرْكٌ", "shirk", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a share» — the delayed mubtadaʾ.", "«bir ortaklık» — geciktirilmiş mübtedâ."),
  fi(), majrur("السَّمٰوَاتِ", "samawat", "«the heavens»", "«gökler»", "فِي", punct=".")]))
sen("s31", "Look at the earth and at the sky, and look at man.", "Yere ve göğe bakın, insana bakın.", [
  amr_pl("اُنْظُرُوا", "nazara", "look", "bakın"), *ila_al("الْأَرْضِ", "ard", "«the earth»", "«yer»"), *ila_al("السَّمَاءِ", "sama", "«the sky»", "«gök»", wa=True),
  amr_pl("وَانْظُرُوا", "nazara", "look", "bakın", wa=True, tags=["atf-nasaq"]), *ila_al("الْإِنْسَانِ", "insan", "«man»", "«insan»", punct=".")])
sen("s32", "«This is the creation of Allah; so show me what those besides Him have created.» (Luqmān 31:11)", "«İşte bu Allah'ın yaratmasıdır; gösterin bana, O'ndan başkaları neyi yaratmış?» (Lokmân 31:11)", quran([
  ishara("هٰذَا", "hadha", "raf", "«this»", "«işte bu»"),
  tok("خَلْقُ", "khalq", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the creation (of)» — the khabar; a muḍāf.", "«yaratması» — haber; muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh."),
  tok("فَأَرُونِي", "ara", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi", "form-iv-verbs", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَأَرُونِي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«so show me» — a plural imperative; the speaker's yāʾ its first object.", "«öyleyse gösterin bana» — cemi emir; mütekellim yâ'sı birinci mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("أَرُو", "ara", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("مَاذَا", "madha", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِخَلَقَ — وَالْجُمْلَةُ مَفْعُولٌ ثَانٍ لِأَرُونِي.", "«what» — the fronted object of «created».", "«neyi» — «yarattı»nın öne alınmış mef'ûlü."),
  mazi("خَلَقَ", "khalaqa", "«have created»", "«yarattı»", hidden=None),
  tok("الَّذِينَ", "alladhina", "pron", ["ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«those who» — the relative, the doer.", "«… olanlar» — ism-i mevsûl, fâil."),
  tok("مِنْ", "min", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ صِلَةُ الْمَوْصُولِ.", "«from» — the phrase is the relative's ṣila.", "«-den» — şibh-i cümle sıla."),
  mudaf_pron("دُونِهِ", "duna", "هِ", "pron-3ms", "ظَرْفٌ مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«besides Him» — in jarr", "«O'ndan başka» — mecrur", tags=["huruf-jarr"], punct=".")]))
sen("s33", "And how are there a lord of the land, and a lord of the sea, and a lord of provision, and a lord of the rain?", "Ve nasıl olur da karanın rabbi, denizin rabbi, rızkın rabbi, yağmurun rabbi olsun?", [
  tok("وَكَيْفَ", "kayfa", "noun", ["al-istifham", "mubtada-khabar", "anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«and how» — the question word, the fronted khabar.", "«ve nasıl» — istifham ismi, öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("كَيْفَ", "kayfa", "noun")]), *four_lords(khabar=False, punct="؟")])
sen("s34", "«Names which you have named, you and your fathers.» (Yūsuf 12:40)", "«Sizin ve atalarınızın taktığı birtakım adlar.» (Yûsuf 12:40)", quran([
  tok("أَسْمَاءٌ", "ism-name", "noun", ["mubtada-khabar", "jam-taksir"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ، مَرْفُوعٌ بِالضَّمَّةِ.", "«(they are) names» — the khabar of an omitted «they».", "«(onlar) adlardır» — hazfedilmiş mübtedânın haberi."),
  tok("سَمَّيْتُمُوهَا", "samma", "verb", ["naat-sifa", "maful-bihi", "naqis-verbs", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ، وَالْوَاوُ لِلْإِشْبَاعِ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِأَسْمَاءٌ.", "«which you have named» — the tāʾ its doer, the hā its object; the clause describes the names.", "«taktığınız» — tâ fâil, hâ mef'ûl; cümle adların sıfatı.", segments=[seg("سَمَّيْ", "samma", "verb"), seg("تُمُو", "pron-2mp", "pron"), seg("هَا", "pron-3fs", "pron")]),
  tok("أَنْتُمْ", "antum", "pron", ["tawkid"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلتَّاءِ (لِيَصِحَّ الْعَطْفُ عَلَيْهَا).", "«you» — a tawkīd of the doer's tāʾ, so that a noun may be joined to it.", "«siz» — tâ'nın te'kidi (atıf sahih olsun diye)."),
  tok("وَآبَاؤُكُمْ", "ab", "noun", ["atf-nasaq", "idafa-definiteness", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَآبَاؤُ مَعْطُوفٌ عَلَى التَّاءِ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«and your fathers» — joined onto the tāʾ; annexed to «your».", "«ve atalarınız» — tâ'ya matuf; «siz»e muzâf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("آبَاؤُ", "ab", "noun"), seg("كُمْ", "pron-2mp", "pron")])]))
sen("s35", "Judgement is Allah's, sovereignty is Allah's, the earth is Allah's, the command is Allah's.", "Hüküm Allah'ındır, mülk Allah'ındır, yer Allah'ındır, emir Allah'ındır.", [
  tok("الْحُكْمُ", "hukm", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«judgement» — the mubtadaʾ.", "«hüküm» — mübtedâ."), li_al("لِلّٰهِ", "allah", "«is Allah's»", "«Allah'ındır»", punct="،"),
  tok("الْمُلْكُ", "mulk", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«sovereignty» — the mubtadaʾ.", "«mülk» — mübtedâ."), li_al("لِلّٰهِ", "allah", "«is Allah's»", "«Allah'ındır»", punct="،"),
  tok("الْأَرْضُ", "ard", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the earth» — the mubtadaʾ.", "«yer» — mübtedâ."), li_al("لِلّٰهِ", "allah", "«is Allah's»", "«Allah'ındır»", punct="،"),
  tok("الْأَمْرُ", "amr", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the command» — the mubtadaʾ.", "«emir» — mübtedâ."), li_al("لِلّٰهِ", "allah", "«is Allah's»", "«Allah'ındır»", punct=".")])
sen("s36", "«Worship none but Him.» (Yūsuf 12:40)", "«O'ndan başkasına kulluk etmeyin.» (Yûsuf 12:40)", quran([
  la_nahiya_(),
  tok("تَعْبُدُوا", "abada", "verb", ["la-nahiya", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«(do not) worship» — jazm after the prohibiting lā, the nūn dropped; the wāw its doer.", "«kulluk etmeyin» — nehiy lâ'sı ile meczûm, nûnu düşmüş; vâv fâil."),
  tok("إِلَّا", "illa", "part", ["qasr", "istithna"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except» — the restricting illā of a voided exception.", "«ancak» — hasr edatı (müferrağ istisna)."),
  tok("إِيَّاهُ", "iyya", "pron", ["maful-bihi", "qasr"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«Him» — the detached object pronoun.", "«O'na» — munfasıl nasb zamiri, mef'ûl.", punct=".", segments=[seg("إِيَّا", "iyya", "pron"), seg("هُ", "pron-3ms", "pron")])]))
sen("s37", "«That is the right religion.» (Yūsuf 12:40)", "«İşte dosdoğru din budur.» (Yûsuf 12:40)", quran([
  ishara("ذٰلِكَ", "dhalika", "raf", "«that»", "«işte bu»"),
  tok("الدِّينُ", "din", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the religion» — the khabar.", "«din» — haber."),
  tok("الْقَيِّمُ", "qayyim", "noun", ["naat-sifa"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the right» — the naʿt.", "«dosdoğru» — sıfat.", punct=".")]))
sen("s38", "«But most of the people do not know.» (Yūsuf 12:40)", "«Fakat insanların çoğu bilmez.» (Yûsuf 12:40)", quran([
  wa_lakinna(), *akthar_nas(), la_nafiya(),
  khamsa("يَعْلَمُونَ", "alima", "«know»", "«bilirler»", tags=["inna-wa-akhawatuha", "la-nafiya"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ", punct=".")]))

# ---------------------------------------------------------------- glossary
NEW = {
 "lana": G("lana", "لَانَ", "ل ي ن", "verb", "to become soft, to yield", "yumuşamak", 2, form="I"),
 "khadaa-submit": G("khadaa-submit", "خَضَعَ", "خ ض ع", "verb", "to submit, to humble oneself", "boyun eğmek", 2, form="I"),
 "istajala": G("istajala", "اِسْتَعْجَلَ", "ع ج ل", "verb", "to hurry, to be in haste", "acele etmek", 2, form="X"),
 "itmaanna": G("itmaanna", "اِطْمَأَنَّ", "ط م أ ن", "verb", "to be reassured, to be at ease (a quadriliteral on اِفْعَلَلَّ)", "rahatlamak, huzur bulmak (اِفْعَلَلَّ vezninde rubâî)", 2, form="رُبَاعِيّ"),
 "badaa": G("badaa", "بَدَأَ", "ب د أ", "verb", "to begin", "başlamak", 1, form="I"),
 "fursa": G("fursa", "فُرْصَة", "ف ر ص", "noun", "an opportunity", "fırsat", 2, plural="فُرَص"),
 "milla": G("milla", "مِلَّة", "م ل ل", "noun", "a creed, a religious community", "millet, din", 2, plural="مِلَل"),
 "ashraka": G("ashraka", "أَشْرَكَ", "ش ر ك", "verb", "to associate (a partner with Allah)", "ortak koşmak", 2, form="IV"),
 "mutafarriq": G("mutafarriq", "مُتَفَرِّق", "ف ر ق", "noun", "diverse, scattered (ism fāʿil of تَفَرَّقَ)", "çeşitli, dağınık (teferraka'nın ism-i fâili)", 2, plural="مُتَفَرِّقُونَ"),
 "qahhar": G("qahhar", "قَهَّار", "ق ه ر", "noun", "the Subduer, all-compelling (an intensive on فَعَّال)", "Kahhâr, her şeye galip (فَعَّال vezninde mübalağa)", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("haja", "حاجة"), ("saqa", "ساق"), ("sahib", "صاحب"), ("ataa", "أطاع"), ("law", "لو"), ("lam-jawab", "ل"), ("pron-2d", "كما"), ("aataa", "آتى"), ("shirk", "شرك"), ("ittabaa", "اتبع"), ("tawhid", "توحيد"), ("faqat", "فقط"), ("huwa", "هو"), ("ana", "أنا"), ("fadl", "فضل"), ("shakara", "شكر"), ("waqafa", "وقف"), ("wahid", "واحد"), ("am", "أم"), ("ara", "أرى"), ("samawat", "سماء"), ("sama", "سماء"), ("alladhina", "الذين"), ("duna", "دون"), ("samma", "سمى"), ("hukm", "حكم"), ("mulk", "ملك"), ("iyya", "إيا"), ("din", "دين"), ("qayyim", "قيم"), ("khalq", "خلق"), ("allama", "علم")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("lana", "khadaa-submit", "istajala", "itmaanna", "badaa", "ashraka"): mo["verbs"].pop(_k, None)
put_morph(mo, "lana", _sg.idgham(_sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "لَان", "لِن", "لِين", "لِن", "لِين", "لِن", "لِين", "لَيِّن", note="لَازِمٌ: لَانَ يَلِينُ، لِنْتُ.")))
put_morph(mo, "khadaa-submit", _sg.sound1("fataha", "خَضَع", "خْضَع", "اِخْضَع", "خُضُوع", "خَاضِع", note="لَازِمٌ، يَتَعَدَّى بِاللَّامِ: خَضَعَ لَهُ — حَلْقِيُّ الْعَيْنِ فَبَابُهُ فَتَحَ."))
put_morph(mo, "istajala", _sg.derived("مِنْ بَابِ الِاسْتِفْعَالِ", "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ", "اِسْتَعْجَل", "سْتَعْجِل", "اِسْتَعْجِل", "اِسْتِعْجَال", "مُسْتَعْجِل", "مُسْتَعْجَل", "اُسْتُعْجِلَ", "يُسْتَعْجَلُ", note="لَازِمٌ وَمُتَعَدٍّ: اِسْتَعْجَلَ الْأَمْرَ."))
put_morph(mo, "itmaanna", _sg.entry("رُبَاعِيٌّ مَزِيدٌ — اِفْعَلَلَّ", "اِفْعَلَلَّ يَفْعَلِلُّ", "اِطْمِئْنَان", "مُطْمَئِنّ",
    ["اِطْمَأَنَّ", "اِطْمَأَنَّا", "اِطْمَأَنُّوا", "اِطْمَأَنَّتْ", "اِطْمَأَنَّتَا", "اِطْمَأْنَنَّ", "اِطْمَأْنَنْتَ", "اِطْمَأْنَنْتُمَا", "اِطْمَأْنَنْتُمْ", "اِطْمَأْنَنْتِ", "اِطْمَأْنَنْتُمَا", "اِطْمَأْنَنْتُنَّ", "اِطْمَأْنَنْتُ", "اِطْمَأْنَنَّا"],
    ["يَطْمَئِنُّ", "يَطْمَئِنَّانِ", "يَطْمَئِنُّونَ", "تَطْمَئِنُّ", "تَطْمَئِنَّانِ", "يَطْمَأْنِنَّ", "تَطْمَئِنُّ", "تَطْمَئِنَّانِ", "تَطْمَئِنُّونَ", "تَطْمَئِنِّينَ", "تَطْمَئِنَّانِ", "تَطْمَأْنِنَّ", "أَطْمَئِنُّ", "نَطْمَئِنُّ"],
    ["اِطْمَئِنَّ", "اِطْمَئِنَّا", "اِطْمَئِنُّوا", "اِطْمَئِنِّي", "اِطْمَئِنَّا", "اِطْمَأْنِنَّ"],
    "يَطْمَئِنَّ", "يَطْمَئِنَّ", "تَطْمَئِنَّ", note="لَازِمٌ — رُبَاعِيٌّ مَزِيدٌ عَلَى اِفْعَلَلَّ: الْمِثْلَانِ يُدْغَمَانِ حَيْثُ تَحَرَّكَ الثَّانِي وَيُفَكَّانِ أَمَامَ السَّاكِنِ (اِطْمَأْنَنْتُ)؛ الْهَمْزَةُ تُرْسَمُ عَلَى نَبْرَةٍ بَعْدَ الْكَسْرَةِ (يَطْمَئِنُّ)."))
put_morph(mo, "badaa", _sg.sound1("fataha", "بَدَأ", "بْدَأ", "اِبْدَأ", "بَدْء", "بَادِئ", "مَبْدُوء", "بُدِئَ", "يُبْدَأُ", note="مُتَعَدٍّ وَلَازِمٌ: بَدَأَ مَوْعِظَتَهُ — مَهْمُوزُ اللَّامِ، حَلْقِيُّ الْعَيْنِ فَبَابُهُ فَتَحَ."))
put_morph(mo, "ashraka", _sg.derived("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَشْرَك", "شْرِك", "أَشْرِك", "إِشْرَاك", "مُشْرِك", "مُشْرَك", "أُشْرِكَ", "يُشْرَكُ", note="مُتَعَدٍّ: أَشْرَكَ بِاللهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 13 (print pp. 41–44, «أَحْسَنُ الْقَصَصِ» sections 10 «حِكْمَةُ يُوسُف» and 11 «مَوْعِظَةُ التَّوْحِيد»): Yūsuf's reflection on need, his patience and his promise with Yūsuf 12:37 (s11, s14, marked); the sermon of tawḥīd — 12:38 in three lines (s19, s20, s24), 12:39 (s28), Fāṭir 35:40 (s30), Luqmān 31:11 (s32), 12:40 in four lines (s34, s36, s37, s38), all as the print sets them and marked. "
          "One printed line is one sentence; s5 is given the full stop the print lacks at the page break; the saying verbs of s1, s7, s10, s21 and s25 keep the print's colon and s26–s27 take an editorial one; the print's parentheses around the ayas are read as quotation marks, and its ءَأَرْبَابٌ keeps the muṣḥaf's seatless first hamza.")
ADD_TR = (" On üçüncü bölüm (basılı s. 41–44, «أَحْسَنُ الْقَصَصِ» 10. kısım «حِكْمَةُ يُوسُف» ve 11. kısım «مَوْعِظَةُ التَّوْحِيد»): Yusuf'un ihtiyaç üzerine düşüncesi, sabrı ve vaadi, Yûsuf 12:37 ile (s11, s14, işaretli); tevhid vaazı — 12:38 üç satırda (s19, s20, s24), 12:39 (s28), Fâtır 35:40 (s30), Lokmân 31:11 (s32), 12:40 dört satırda (s34, s36, s37, s38), hepsi baskıdaki şekliyle ve işaretli. "
          "Basılı her satır bir cümledir; s5'e baskının sayfa sonunda bıraktığı nokta eklenmiştir; s1, s7, s10, s21 ve s25'in söyleme fiilleri baskının iki noktasını korur, s26–s27 editöryal bir iki nokta alır; baskının âyetleri saran parantezleri tırnak olarak okunmuş, ءَأَرْبَابٌ mushafın kürsüsüz ilk hemzesiyle bırakılmıştır.")
write_out(13, S, TITLE, ADD_EN, ADD_TR, "pp. 41–44", GLOSS_ADD)
report(13, S, GLOSS_ADD, ())
