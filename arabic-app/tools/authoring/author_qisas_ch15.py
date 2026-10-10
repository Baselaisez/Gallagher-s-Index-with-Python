# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 15: «الْمَلِكُ يُرْسِلُ إِلَى يُوسُفَ، وَيُوسُفُ عَلَى خَزَائِنِ الْأَرْضِ» — «أَحْسَنُ الْقَصَصِ» sections 14–16 (print pp. 47–51):
the king sends for Yūsuf (12:54), Yūsuf asks for the inquiry and leaves the prison innocent, and the sermon on trust that ends with
«اِجْعَلْنِي عَلَى خَزَائِنِ الْأَرْضِ» (12:55). Every printed line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch15.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْمَلِكُ يُرْسِلُ إِلَى يُوسُفَ، وَيُوسُفُ عَلَى خَزَائِنِ الْأَرْضِ", "en": "The king sends for Yūsuf, and Yūsuf over the treasuries of the land", "tr": "Kral Yusuf'u çağırtır ve Yusuf yeryüzünün hazinelerinin başında"}
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

# ================================================================ §14 الملك يرسل إلى يوسف (p. 47)
sen("s1", "And when the king heard this interpretation and this plan, he rejoiced greatly, and said: Who is the author of this interpretation?", "Kral bu tabiri ve tedbiri duyunca çok sevindi ve dedi: Bu tabirin sahibi kim?", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw", "idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، فِي مَحَلِّ نَصْبٍ.", "«and when» — the resumptive wāw; lammā is a time adverb carrying the sense of a condition.", "«ve …-ince» — istînâf vâvı; lemmâ şart manası taşıyan zaman zarfı.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("سَمِعَ", "samia", "«heard»", "«duydu»", hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ"), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"),
  badal_("التَّأْوِيلَ", "tawil", "nasb", "«interpretation»", "«tabiri»"),
  tok("وَالتَّدْبِيرَ", "tadbir", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالتَّدْبِيرَ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and the plan» — joined, in naṣb.", "«ve tedbiri» — ma'tûf, mansub.", segments=wa_("التَّدْبِيرَ", "tadbir", "noun")),
  mazi("فَرِحَ", "fariha", "«he rejoiced»", "«sevindi»", hidden="هُوَ", extra_ar=" — جَوَابُ لَمَّا"), jiddan(punct="،"),
  qala(full="وَقَالَ", wa=True, hidden="هُوَ"),
  man_mubt(), tok("صَاحِبُ", "sahib", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the author (of)» — the khabar; a muḍāf.", "«sahibi» — haber; muzâf."),
  hadha_pron_jarr("هٰذَا", "hadha", "«this»", "«bu»"),
  badal_("التَّأْوِيلِ", "tawil", "jarr", "«interpretation»", "«tabirin»", punct="؟")])
sen("s2", "And the king said: Who is this noble man who gave us good counsel and pointed the way to the plan?", "Kral dedi: Bize öğüt veren ve tedbiri gösteren bu kerim adam kim?", [
  qala(full="وَقَالَ", wa=True, hidden=None), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"], punct=":"),
  man_mubt(), tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«this» — the demonstrative, the khabar.", "«bu» — ism-i işâret, haber."),
  badal_("الرَّجُلُ", "rajul", "raf", "«man»", "«adam»"), nat_raf("الْكَرِيمُ", "karim", "«noble»", "«kerim»"),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ.", "«who» — the relative, a second naʿt.", "«ki o» — ism-i mevsûl, ikinci sıfat."),
  mazi("نَصَحَ", "nasaha", "«gave counsel»", "«öğüt verdi»", hidden="هُوَ", tags=["ism-mawsul"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  lahu("لَنَا", "نَا", "pron-1p", "مُتَعَلِّقٌ بِنَصَحَ.", "«to us».", "«bize»."),
  mazi("وَدَلَّ", "dalla", "«and pointed»", "«ve gösterdi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "doubled-verbs"]),
  ala(), majrur("التَّدْبِيرِ", "tadbir", "«the plan»", "«tedbir»", "عَلَى", punct="؟")])
sen("s3", "The cupbearer said: This is Yūsuf the truthful, and he is the one who told me that I would be a cupbearer to my master the king.", "Sâkî dedi: Bu, Yusuf es-Sıddîk'tır; efendim krala sâkî olacağımı haber veren odur.", [
  qala(hidden=None, punct=None), saqi_fail(punct=":"),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the khabar; a diptote name.", "«Yusuf» — haber; gayr-i munsarıf özel isim."),
  tok("الصِّدِّيقُ", "siddiq", "noun", ["naat-sifa"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ — صِيغَةُ مُبَالَغَةٍ عَلَى فِعِّيل.", "«the truthful» — the naʿt; an intensive on فِعِّيل.", "«sıddîk» — sıfat; فِعِّيل vezninde mübalağa."),
  tok("وَهُوَ", "huwa", "pron", ["anwa-al-waw", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and he» — the detached pronoun as mubtadaʾ.", "«ve o» — munfasıl zamir, mübtedâ.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«the one who» — the relative, the khabar.", "«o kimse ki» — ism-i mevsûl, haber."),
  mazi("أَخْبَرَ", "akhbara", "«told»", "«haber verdi»", hidden="هُوَ", tags=["ism-mawsul", "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  tok("أَنِّي", "anna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَخْبَرَ.", "«that I» — anna with the speaker's yāʾ as its ism; the clause is the object of «told».", "«benim …-ceğimi» — enne, mütekellim yâsı ismi; te'vilî masdar «haber verdi»nin mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("سَأَكُونُ", "kana", "verb", [K, "inna-wa-akhawatuha", "hollow-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَأَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهَا مُسْتَتِرٌ وُجُوبًا: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«I will be» — the future sīn on kāna's muḍāriʿ; its ism «I» concealed; the clause is anna's khabar.", "«olacağım» — istikbal sîni ile kâne'nin muzârisi; ismi gizli «ben»; cümle enne'nin haberi.", segments=[seg("سَ", "sa", "part"), seg("أَكُونُ", "kana", "verb")]),
  tok("سَاقِيًا", "saqi", "noun", [K, "ism-maqsur-manqus"], "خَبَرُ أَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ.", "«a cupbearer» — the khabar of «I will be»; the manqūṣ shows its fatḥa.", "«sâkî» — «olacağım»ın haberi; mankûs fethasını gösterir."),
  tok("لِسَيِّدِي", "sayyid", "noun", ["huruf-jarr", "ya-al-mutakallim", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَسَيِّدِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«to my master» — in jarr, the kasra estimated before the speaker's yāʾ.", "«efendime» — mecrur, kesresi mütekellim yâsından önce takdîrî.", segments=[seg("لِ", "li", "prep"), seg("سَيِّدِ", "sayyid", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("الْمَلِكِ", "malik-king", "noun", ["badal"], "بَدَلٌ مِنْ سَيِّدِي مَجْرُورٌ بِالْكَسْرَةِ (أَوْ عَطْفُ بَيَانٍ).", "«the king» — the badal of «my master» (or an explanatory apposition).", "«kral» — «efendim»in bedeli (ya da atf-ı beyan).", punct=".")])
sen("s4", "And the king longed to meet Yūsuf, and sent for Yūsuf, and the king said: «Bring him to me; I will take him for myself.» (Yūsuf 12:54)", "Kral Yusuf'la görüşmeyi özledi, Yusuf'a haber gönderdi ve kral dedi: «Onu bana getirin, onu kendime ayırayım.» (Yûsuf 12:54)", [
  mazi("وَاشْتَاقَ", "ishtaqa", "«longed»", "«özledi»", hidden=None, wa=True, tags=["form-viii-verbs", "hollow-verbs"]), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  ila(), tok("لِقَاءِ", "liqa", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«meeting (with)» — in jarr; a muḍāf.", "«görüşme» — mecrur; muzâf."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", punct="،"),
  mazi("وَأَرْسَلَ", "arsala", "«and sent»", "«ve gönderdi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-iv-verbs"]),
  ila(), tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr after ilā, by a fatḥa: a diptote name.", "«Yusuf'a» — ilâ ile mecrur, fetha ile: gayr-i munsarıf özel isim."),
  qala(full="وَقَالَ", wa=True, hidden=None, punct=None), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  *quran([
  tok("ائْتُونِي", "ata", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — أَمْرُ أَتَى، هَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«bring me» — a plural imperative, the nūn dropped; the wāw its doer; the nūn of protection and the speaker's yāʾ as object; the amr of أَتَى on a waṣl hamza.", "«bana getirin» — nûnun hazfi ile mebnî emir; vâv fâil; vikâye nûnu ve mütekellim yâsı mef'ûl; etâ'nın emri, vasıl hemzesiyle.", segments=[seg("ائْتُو", "ata", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِائْتُونِي.", "«him» — bi + the pronoun: «bring (with) him».", "«onu» — bâ ve zamir.", segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("أَسْتَخْلِصْهُ", "istakhlasa", "verb", ["jawab-al-talab", "form-x-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا، وَالْهَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«(that) I may take him for myself» — jazm as the answer of the command; «I» concealed; the pronoun its object.", "«onu kendime ayırayım» — talebin cevabında meczum; fâil gizli «ben»; zamir mef'ûl.", segments=[seg("أَسْتَخْلِصْ", "istakhlasa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("لِنَفْسِي", "nafs", "noun", ["huruf-jarr", "ya-al-mutakallim", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَنَفْسِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«for myself» — in jarr before the speaker's yāʾ.", "«kendim için» — mütekellim yâsından önce mecrur.", punct=".", segments=[seg("لِ", "li", "prep"), seg("نَفْسِ", "nafs", "noun"), seg("ي", "pron-1s", "pron")])])])

# ================================================================ §15 يوسف يسأل التفتيش (pp. 47–49)
sen("s5", "And when the messenger came to Yūsuf and said to him, «The king summons you!» — Yūsuf was not content to leave the prison like that.", "Elçi Yusuf'a gelip ona «Kral seni çağırıyor!» deyince, Yusuf zindandan böyle çıkmaya razı olmadı.", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw", "idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، فِي مَحَلِّ نَصْبٍ.", "«and when» — the resumptive wāw; lammā is a time adverb carrying the sense of a condition.", "«ve …-ince» — istînâf vâvı; lemmâ şart manası taşıyan zaman zarfı.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("جَاءَ", "jaa", "«came»", "«geldi»", hidden=None, tags=["hollow-verbs"], extra_ar=" — فِعْلُ الشَّرْطِ"), fail("الرَّسُولُ", "rasul", "«the messenger»", "«elçi»"),
  ila(), tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr after ilā, by a fatḥa: a diptote name.", "«Yusuf'a» — ilâ ile mecrur, fetha ile: gayr-i munsarıf özel isim."),
  qala(full="وَقَالَ", wa=True, hidden="هُوَ", punct=None), lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِقَالَ.", "«to him».", "«ona»."),
  inna(), malik_("الْمَلِكَ", "nasb", "اسْمُ إِنَّ", "«the king» — the ism of inna.", "«kral» — inne'nin ismi.", tags=["inna-wa-akhawatuha"]),
  verb_enc("يَدْعُوكَ", "daa", "كَ", "pron-2ms", "«summons you»", "«seni çağırıyor»", tags=["inna-wa-akhawatuha", "naqis-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", punct="!"),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
  mazi("رَضِيَ", "radiya", "«was content»", "«razı oldu»", hidden=None, tags=["naqis-verbs"], extra_ar=" — جَوَابُ لَمَّا"), yusuf_fail(),
  an_("رَضِيَ", "«was content»", "«razı oldu»"),
  tok("يَخْرُجَ", "kharaja", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to leave» — in naṣb after an; «he» concealed.", "«çıkmaya» — en ile mansub; fâil gizli «o»."),
  min_(full="مِنَ"), majrur("السِّجْنِ", "sijn", "«the prison»", "«zindan»", "مِنْ"),
  tok("هٰكَذَا", "hakadha", "pron", ["hal", "asma-al-ishara"], "الْهَاءُ لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ — فِي مَحَلِّ نَصْبٍ حَالٌ (أَوْ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ: خُرُوجًا هٰكَذَا).", "«like that» — the demonstrative compound, as a ḥāl (or the naʿt of an omitted maṣdar).", "«böyle» — işaret bileşiği, hâl (ya da hazfedilmiş masdarın sıfatı).", punct=".")])
sen("s6", "And the people would say: This is Yūsuf! This one was in the prison yesterday; he betrayed the ʿAzīz.", "İnsanlar derdi ki: Bu Yusuf! Bu dün zindandaydı; o Aziz'e ihanet etti.", [
  tok("وَيَقُولُ", "qala", "verb", ["anwa-al-waw", "mudari-marfu", "hollow-verbs", "maful-bihi"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«and … would say» — a muḍāriʿ in rafʿ; what is said is its object.", "«ve … derdi» — merfû muzâri; söylenen söz mef'ûlüdür.", segments=wa_("يَقُولُ", "qala", "verb")),
  nas_fail(),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the khabar; a diptote name.", "«Yusuf» — haber; gayr-i munsarıf.", punct="!"),
  ishara("هٰذَا", "hadha", "raf", "«this one»", "«bu»"),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "mubtada-khabar"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.", "«was» — kāna with «he» concealed; the clause is the mubtadaʾ's khabar.", "«idi» — kâne, ismi gizli «o»; cümle mübtedânın haberi."),
  tok("أَمْسِ", "ams", "noun", ["maful-fih", "al-murab-wal-mabni-wal-irab"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ.", "«yesterday» — a time adverb built on kasra.", "«dün» — kesre üzere mebnî zaman zarfı."),
  *fi_sijn_khabar(punct="،"),
  tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed he» — inna with its pronoun ism.", "«şüphesiz o» — inne, zamir ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  mazi("خَانَ", "khana", "«betrayed»", "«ihanet etti»", hidden="هُوَ", tags=["inna-wa-akhawatuha", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  maful("الْعَزِيزَ", "aziz", "«the ʿAzīz»", "«Aziz'e»", punct=".")])
sen("s7", "Indeed Yūsuf was great of soul, proud; indeed Yūsuf was great of mind, keen.", "Şüphesiz Yusuf yüce ruhlu, onurluydu; şüphesiz Yusuf büyük akıllı, zekiydi.", [
  inna(), ism_inna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", tags=["mamnu-min-sarf"], extra=" — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ"),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "inna-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«was» — kāna with «he» concealed; the clause is inna's khabar.", "«idi» — kâne, ismi gizli «o»; cümle inne'nin haberi."),
  tok("كَبِيرَ", "kabir", "noun", [K, "idafa-definiteness", "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ (إِضَافَةُ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا).", "«great (of)» — kāna's khabar; a ṣifa mushabbaha annexed to its own subject.", "«büyük» — kâne'nin haberi; sıfat-ı müşebbehe fâiline muzâf."),
  mi("النَّفْسِ", "nafs", "«soul»", "«ruh»"),
  khabar_kana("أَبِيًّا", "abiyy", "«proud, unbending»", "«onurlu»", second=True, punct="،", tags=["sifa-mushabbaha"]),
  inna(), ism_inna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", tags=["mamnu-min-sarf"], extra=" — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ"),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "inna-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«was» — kāna with «he» concealed; the clause is inna's khabar.", "«idi» — kâne, ismi gizli «o»; cümle inne'nin haberi."),
  tok("كَبِيرَ", "kabir", "noun", [K, "idafa-definiteness", "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«great (of)» — kāna's khabar; a muḍāf.", "«büyük» — kâne'nin haberi; muzâf."),
  mi("الْعَقْلِ", "aql", "«mind»", "«akıl»"),
  khabar_kana("ذَكِيًّا", "dhaki", "«keen»", "«zeki»", second=True, punct=".", tags=["sifa-mushabbaha"])])
sen("s8", "Had anyone been in Yūsuf's place in the prison, and the king's messenger come to him —", "Yusuf'un yerinde zindanda biri olsaydı ve kralın elçisi ona gelseydi —", [
  tok("لَوْ", "law", "part", ["hikayat-al-hal"], "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ، حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«had, if» — the unreal conditional, governing no jazm.", "«-seydi» — cezm etmeyen şart harfi, imtinâ harfi."),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "hikayat-al-hal"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — فِعْلُ الشَّرْطِ.", "«been» — kāna as the condition's verb.", "«olsaydı» — şart fiili olarak kâne."),
  tok("أَحَدٌ", "ahad", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«anyone» — kāna's ism.", "«biri» — kâne'nin ismi."),
  tok("مَكَانَ", "makan", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — وَشِبْهُ الْجُمْلَةِ خَبَرُ كَانَ.", "«in the place (of)» — an adverb of place; the phrase is kāna's khabar.", "«yerinde» — mekân zarfı; şibh-i cümle kâne'nin haberi."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  fi(), majrur("السِّجْنِ", "sijn", "«the prison»", "«zindan»", "فِي"),
  verb_enc("وَجَاءَهُ", "jaa", "هُ", "pron-3ms", "«and … come to him»", "«ve ona gelseydi»", mudari=False, hidden=None, wa=True, tags=["hollow-verbs"]),
  *rasul_malik("فَاعِلٌ", "the doer", "fâil", punct=".", tags=["fail"])])
sen("s9", "and the king's messenger said to him, «The king summons you and awaits you» — this man would have hurried to the prison door and gone out.", "ve kralın elçisi ona «Kral seni çağırıyor ve bekliyor» deseydi — bu adam zindan kapısına koşar ve çıkardı.", [
  qala(full="وَقَالَ", wa=True, hidden=None, punct=None), lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِقَالَ.", "«to him».", "«ona»."),
  *rasul_malik("فَاعِلٌ", "the doer", "fâil", tags=["fail"]),
  inna(), malik_("الْمَلِكَ", "nasb", "اسْمُ إِنَّ", "«the king» — the ism of inna.", "«kral» — inne'nin ismi.", tags=["inna-wa-akhawatuha"]),
  verb_enc("يَدْعُوكَ", "daa", "كَ", "pron-2ms", "«summons you»", "«seni çağırıyor»", tags=["inna-wa-akhawatuha", "naqis-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  verb_enc("وَيَنْتَظِرُكَ", "intazara", "كَ", "pron-2ms", "«and awaits you»", "«ve seni bekliyor»", wa=True, tags=["form-viii-verbs"]),
  tok("لَأَسْرَعَ", "asraa", "verb", ["hikayat-al-hal", "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَأَسْرَعَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — جَوَابُ لَوْ.", "«(he) would have hurried» — the lām of law's answer on a māḍī.", "«koşardı» — lev'in cevap lâmı mâzî üzerinde.", segments=[seg("لَ", "lam-jawab", "part"), seg("أَسْرَعَ", "asraa", "verb")]),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "fail"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this» — the demonstrative, the doer.", "«bu» — ism-i işâret, fâil."),
  badal_("الرَّجُلُ", "rajul", "raf", "«man»", "«adam»"),
  ila(), tok("بَابِ", "bab", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the door (of)» — in jarr; a muḍāf.", "«kapısı» — mecrur; muzâf."),
  mi("السِّجْنِ", "sijn", "«the prison»", "«zindan»"),
  mazi("وَخَرَجَ", "kharaja", "«and gone out»", "«ve çıkardı»", hidden="هُوَ", wa=True, tags=["atf-nasaq"], punct=".")])
sen("s10", "But Yūsuf did not hurry.", "Fakat Yusuf acele etmedi.", [
  wa_lakinna(), name_ism_lakinna("يُوسُفَ"),
  lam_jazim(), tok("يُسْرِعْ", "asraa", "verb", ["lam-jazim", "form-iv-verbs", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", "«did (not) hurry» — jazm after lam; the clause is lākinna's khabar.", "«acele etmedi» — lem ile meczum; cümle lâkinne'nin haberi.", punct=".")])
sen("s11", "But Yūsuf was not in haste.", "Fakat Yusuf ivedi davranmadı.", [
  wa_lakinna(), name_ism_lakinna("يُوسُفَ"),
  lam_jazim(), tok("يَسْتَعْجِلْ", "istajala", "verb", ["lam-jazim", "form-x-verbs", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", "«was (not) in haste» — jazm after lam; the clause is lākinna's khabar.", "«ivedi davranmadı» — lem ile meczum; cümle lâkinne'nin haberi.", punct=".")])
sen("s12", "Rather he said to the king's messenger: I want the inquiry; I want the investigation of my case.", "Aksine kralın elçisine dedi: Ben soruşturma istiyorum; ben davamın araştırılmasını istiyorum.", [
  tok("بَلْ", "bal", "part", ["anwa-ma"], "حَرْفُ إِضْرَابٍ.", "«rather» — the particle of correction.", "«aksine» — idrâb harfi."),
  qala(hidden="هُوَ", punct=None),
  tok("لِرَسُولِ", "rasul", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَرَسُولِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِقَالَ.", "«to the messenger (of)» — in jarr; a muḍāf.", "«elçisine» — mecrur; muzâf.", segments=[seg("لِ", "li", "prep"), seg("رَسُولِ", "rasul", "noun")]),
  mi("الْمَلِكِ", "malik-king", "«the king»", "«kral»", punct=":"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the detached pronoun as mubtadaʾ.", "«ben» — munfasıl zamir, mübtedâ."),
  mudari_1s("أُرِيدُ", "arada", "«want»", "«istiyorum»", tags=["mubtada-khabar", "form-iv-verbs", "hollow-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  maful("التَّفْتِيشَ", "taftish", "«the inquiry»", "«soruşturmayı»"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the detached pronoun as mubtadaʾ.", "«ben» — munfasıl zamir, mübtedâ."),
  mudari_1s("أُرِيدُ", "arada", "«want»", "«istiyorum»", tags=["mubtada-khabar", "form-iv-verbs", "hollow-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  maful("الْبَحْثَ", "bahth", "«the investigation»", "«araştırmayı»"),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of, about».", "«hakkında»."),
  tok("قَضِيَّتِي", "qadiyya", "noun", ["huruf-jarr", "ya-al-mutakallim", "idafa-definiteness"], "مَجْرُورٌ بِعَنْ بِكَسْرَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my case» — in jarr before the speaker's yāʾ.", "«davam» — mütekellim yâsından önce mecrur.", punct=".", segments=[seg("قَضِيَّتِ", "qadiyya", "noun"), seg("ي", "pron-1s", "pron")])])
sen("s13", "And the king asked about Yūsuf, and the king learned, and the people learned, that Yūsuf was innocent.", "Kral Yusuf'u sordu; kral da insanlar da Yusuf'un suçsuz olduğunu öğrendi.", [
  mazi("وَسَأَلَ", "saala", "«asked»", "«sordu»", hidden=None, wa=True), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«hakkında»."),
  tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِعَنْ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr by a fatḥa: a diptote name.", "«Yusuf'u» — fetha ile mecrur: gayr-i munsarıf."),
  mazi("وَعَلِمَ", "alima", "«and learned»", "«ve öğrendi»", hidden=None, wa=True, tags=["atf-nasaq"]), malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"]),
  mazi("وَعَلِمَ", "alima", "«and learned»", "«ve öğrendi»", hidden=None, wa=True, tags=["atf-nasaq"]), nas_fail(),
  anna(obj_of="عَلِمَ"), name_ism_anna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  anna_khabar("بَرِيءٌ", "bari", "«innocent»", "«suçsuz»", punct=".", tags=["sifa-mushabbaha"])])
sen("s14", "And Yūsuf went out innocent, and the king honoured him.", "Yusuf suçsuz olarak çıktı ve kral ona ikramda bulundu.", [
  mazi("وَخَرَجَ", "kharaja", "«went out»", "«çıktı»", hidden=None, wa=True), yusuf_fail(),
  tok("بَرِيئًا", "bari", "noun", ["hal", "sifa-mushabbaha"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«innocent» — the ḥāl.", "«suçsuz olarak» — hâl."),
  verb_enc("وَأَكْرَمَهُ", "akrama", "هُ", "pron-3ms", "«and honoured him»", "«ve ona ikram etti»", mudari=False, hidden=None, wa=True, tags=["form-iv-verbs"]),
  malik_("الْمَلِكُ", "raf", "فَاعِلٌ", "«the king» — the doer.", "«kral» — fâil.", tags=["fail"], punct=".")])

# ================================================================ §16 على خزائن الأرض (pp. 49–51)
sen("s15", "And Yūsuf knew that trustworthiness was scarce among people.", "Yusuf, emanetin insanlar arasında az olduğunu biliyordu.", [
  *kana_yalamu("يَعْلَمُ", "alima", "«knew»", "«biliyordu»"),
  anna(obj_of="يَعْلَمُ"), anna_ism("الْأَمَانَةَ", "amana", "«trustworthiness»", "«emanet»"), anna_khabar("قَلِيلَةٌ", "qalil", "«scarce»", "«az»"), *fi_nas(punct=".")])
sen("s16", "And Yūsuf knew that treachery was plentiful among people.", "Yusuf, hıyanetin insanlar arasında çok olduğunu biliyordu.", [
  *kana_yalamu("يَعْلَمُ", "alima", "«knew»", "«biliyordu»"),
  anna(obj_of="يَعْلَمُ"), anna_ism("الْخِيَانَةَ", "khiyana", "«treachery»", "«hıyanet»"), anna_khabar("كَثِيرَةٌ", "kathir", "«plentiful»", "«çok»"), *fi_nas(punct=".")])
sen("s17", "And Yūsuf saw that the people were betraying Allah's wealth.", "Yusuf, insanların Allah'ın mallarına hıyanet ettiğini görüyordu.", [
  *kana_yalamu("يَرَى", "raa", "«saw»", "«görüyordu»", tags=["naqis-verbs"]),
  anna(obj_of="يَرَى"), anna_ism("النَّاسَ", "nas", "«the people»", "«insanlar»"),
  khamsa("يَخُونُونَ", "khana", "«betray»", "«hıyanet ederler»", tags=["inna-wa-akhawatuha", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  fi(), *amwal("أَمْوَالِ", "فِي", "«the wealth (of)»", "«malları»", punct=".")])
sen("s18", "And he saw that in the land there were many treasuries, but they were going to waste.", "Yeryüzünde pek çok hazine olduğunu, fakat bunların zayi olduğunu görüyordu.", [
  kana_hidden(), khabar_kana_mudari("يَرَى", "raa", "«saw»", "«görüyordu»", tags=["naqis-verbs"]),
  anna(obj_of="يَرَى"),
  tok("فِي", "fi", "prep", ["huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ مُقَدَّمٌ.", "«in» — the phrase is anna's khabar, fronted.", "«-de» — şibh-i cümle enne'nin mukaddem haberi."),
  majrur("الْأَرْضِ", "ard", "«the land»", "«yeryüzü»", "فِي"),
  tok("خَزَائِنَ", "khizana", "noun", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«treasuries» — anna's delayed ism; a diptote plural.", "«hazineler» — enne'nin muahhar ismi; gayr-i munsarıf cemi."),
  nat_nasb("كَثِيرَةً", "kathir", "«many»", "«pek çok»"),
  tok("وَلٰكِنَّهَا", "lakinna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ، وَهَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«but they» — lākinna with its pronoun ism.", "«fakat onlar» — lâkinne, zamir ismi.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("ضَائِعَةٌ", "dai-lost", "noun", ["inna-wa-akhawatuha", "ism-fail"], "خَبَرُ لٰكِنَّ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ فَاعِلٍ مِنْ ضَاعَ.", "«going to waste» — lākinna's khabar; the ism fāʿil of ضَاعَ.", "«zayi» — lâkinne'nin haberi; dâa'nın ism-i fâili.", punct=".")])
sen("s19", "They were going to waste because the governors did not fear Allah in them.", "Zayi oluyordu, çünkü emîrler onlar hakkında Allah'tan korkmuyordu.", [
  tok("إِنَّهَا", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed they» — inna with its pronoun ism.", "«şüphesiz onlar» — inne, zamir ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("ضَائِعَةٌ", "dai-lost", "noun", ["inna-wa-akhawatuha", "ism-fail"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«going to waste» — inna's khabar.", "«zayi» — inne'nin haberi."),
  tok("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«because» — the lām of cause over anna.", "«çünkü» — ta'lîl lâmı ve enne."),
  tok("الْأُمَرَاءَ", "amir", "noun", ["inna-wa-akhawatuha", "mamnu-min-sarf", "jam-taksir"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ أَمِيرٍ عَلَى فُعَلَاءَ.", "«the governors» — anna's ism; the plural of أَمِير.", "«emîrler» — enne'nin ismi; «emîr»in cem'i."),
  la_nafiya(),
  khamsa("يَخَافُونَ", "khafa", "«fear»", "«korkarlar»", tags=["inna-wa-akhawatuha", "la-nafiya", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah'tan» — mef'ûl."),
  tok("فِيهَا", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَخَافُونَ.", "«in them».", "«onlar hakkında».", punct=".", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])])
sen("s20", "So their dogs eat, and the people find nothing to eat.", "Böylece onların köpekleri yer, insanlar ise yiyecek bir şey bulamaz.", [
  tok("فَتَأْكُلُ", "akala", "verb", ["atf-nasaq", "mudari-marfu"], "الْفَاءُ لِلسَّبَبِيَّةِ وَالتَّفْرِيعِ، وَتَأْكُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«so … eat» — the fāʾ of consequence; a muḍāriʿ in rafʿ.", "«böylece … yer» — sebep fâsı; merfû muzâri.", segments=[seg("فَ", "fa", "conj"), seg("تَأْكُلُ", "akala", "verb")]),
  mudaf_pron("كِلَابُهُمْ", "kalb", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ كَلْبٍ", "«their dogs» — the doer; the plural of كَلْب", "«köpekleri» — fâil; «köpek»in cem'i", tags=["fail", "jam-taksir"]),
  *la_yajidu(),
  khamsa("يَأْكُلُونَ", "akala", "«they eat»", "«yerler»", tags=["ism-mawsul"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: يَأْكُلُونَهُ", punct=".")])
sen("s21", "And their houses are clothed, and the people find nothing to wear.", "Onların evleri giyinir, insanlar ise giyecek bir şey bulamaz.", [
  tok("وَتَلْبَسُ", "labisa", "verb", ["atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَتَلْبَسُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and … are clothed» — a muḍāriʿ in rafʿ.", "«ve … giyinir» — merfû muzâri.", segments=wa_("تَلْبَسُ", "labisa", "verb")),
  mudaf_pron("بُيُوتُهُمْ", "bayt", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ بَيْتٍ", "«their houses» — the doer; the plural of بَيْت", "«evleri» — fâil; «ev»in cem'i", tags=["fail", "jam-taksir"]),
  *la_yajidu(),
  khamsa("يَلْبَسُونَ", "labisa", "«they wear»", "«giyerler»", tags=["ism-mawsul"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ", punct=".")])
sen("s22", "And none benefits the people with the treasuries of the land except one who is a keeper and knowing.", "İnsanlara yeryüzünün hazineleriyle ancak koruyucu ve bilen kimse fayda verir.", [
  la_nafiya(wa=True),
  neg_mudari("يَنْفَعُ", "nafaa", "«benefits»", "«fayda verir»", hidden=None, extra=" — وَالْفَاعِلُ مُؤَخَّرٌ بَعْدَ إِلَّا"),
  maful("النَّاسَ", "nas", "«the people»", "«insanlara»"),
  *khazain_ard(prep="بِ", role="مُتَعَلِّقٌ بِيَنْفَعُ"),
  tok("إِلَّا", "illa", "part", ["qasr", "istithna"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except» — the restricting illā of a voided exception.", "«ancak» — hasr edatı (müferrağ istisna)."),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«one who» — the relative, as the doer.", "«kimse ki» — ism-i mevsûl, fâil."),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "ism-mawsul"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«is» — kāna with «he» concealed; the relative's clause.", "«olan» — kâne, ismi gizli «o»; sıla cümlesi."),
  *hafiz_alim(punct=".")])
sen("s23", "And whoever is a keeper but not knowing does not know where the treasuries of the land are nor how to profit by them.", "Koruyucu olup da bilen olmayan, yeryüzünün hazinelerinin nerede olduğunu ve onlardan nasıl yararlanılacağını bilmez.", [
  man_shart(),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "ism-mawsul"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«is» — kāna with «he» concealed; the relative's clause.", "«olan» — kâne, ismi gizli «o»; sıla cümlesi."),
  tok("حَفِيظًا", "hafiz-keeper", "noun", [K, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a keeper» — kāna's khabar.", "«koruyucu» — kâne'nin haberi."),
  ma_nafiya_(),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "atf-nasaq"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — مَعْطُوفٌ عَلَى الصِّلَةِ.", "«is» — kāna, joined onto the relative's clause.", "«olan» — kâne, sılaya ma'tûf."),
  tok("عَلِيمًا", "alim", "noun", [K, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«knowing» — kāna's khabar.", "«bilen» — kâne'nin haberi."),
  la_nafiya(),
  neg_mudari("يَعْلَمُ", "alima", "«knows»", "«bilir»", hidden="هُوَ", tags=["mubtada-khabar"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ مَنْ"),
  tok("أَيْنَ", "ayna", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ خَبَرٌ مُقَدَّمٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيَعْلَمُ (مُعَلَّقٌ بِالِاسْتِفْهَامِ).", "«where» — the question adverb as a fronted khabar; the clause is the object of «knows».", "«nerede» — istifham zarfı, mukaddem haber; cümle «bilir»in mef'ûlü."),
  *khazain_ard(case="raf"),
  tok("وَكَيْفَ", "kayfa", "noun", ["atf-nasaq", "al-istifham", "hal"], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — the question noun as a ḥāl.", "«ve nasıl» — istifham ismi, hâl.", segments=wa_("كَيْفَ", "kayfa", "noun")),
  mudari("يَنْتَفِعُ", "intafaa", "«profits»", "«yararlanır»", tags=["form-viii-verbs"]),
  tok("بِهَا", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَنْتَفِعُ.", "«by them».", "«onlardan».", punct=".", segments=[seg("بِ", "bi", "prep"), seg("هَا", "pron-3fs", "pron")])])
sen("s24", "And whoever is knowing but not a keeper eats of them and betrays in them.", "Bilen olup da koruyucu olmayan, onlardan yer ve onlara hıyanet eder.", [
  man_shart(),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "ism-mawsul"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«is» — kāna with «he» concealed; the relative's clause.", "«olan» — kâne, ismi gizli «o»; sıla cümlesi."),
  tok("عَلِيمًا", "alim", "noun", [K, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«knowing» — kāna's khabar.", "«bilen» — kâne'nin haberi."),
  ma_nafiya_(),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "atf-nasaq"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — مَعْطُوفٌ عَلَى الصِّلَةِ.", "«is» — kāna, joined onto the relative's clause.", "«olan» — kâne, sılaya ma'tûf."),
  tok("حَفِيظًا", "hafiz-keeper", "noun", [K, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a keeper» — kāna's khabar.", "«koruyucu» — kâne'nin haberi."),
  mudari("يَأْكُلُ", "akala", "«eats»", "«yer»", tags=["mubtada-khabar"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ مَنْ"),
  tok("مِنْهَا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَأْكُلُ.", "«of them».", "«onlardan».", segments=[seg("مِنْ", "min", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("وَيَخُونُ", "khana", "verb", ["atf-nasaq", "mudari-marfu", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَخُونُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and betrays» — joined; a hollow muḍāriʿ.", "«ve hıyanet eder» — ma'tûf; ecvef muzâri.", segments=wa_("يَخُونُ", "khana", "verb")),
  tok("فِيهَا", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَخُونُ.", "«in them».", "«onlar hakkında».", punct=".", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])])
sen("s25", "And Yūsuf was a keeper and knowing.", "Yusuf koruyucu ve bilendi.", [
  kana(), yusuf_ism_kana(), *hafiz_alim(punct=".")])
sen("s26", "And Yūsuf did not want to let the governors eat the people's wealth.", "Yusuf, emîrlerin insanların mallarını yemesine izin vermek istemiyordu.", [
  kana(), yusuf_ism_kana(), la_nafiya(),
  tok("يُرِيدُ", "arada", "verb", [K, "la-nafiya", "mudari-marfu", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«want» — rafʿ after the negating lā; the clause is kāna's khabar.", "«istemek» — nefiy lâ'sından sonra merfû; cümle kâne'nin haberi."),
  an_("يُرِيدُ", "«want»", "«istiyordu»"),
  tok("يَتْرُكَ", "taraka", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to let» — in naṣb after an; «he» concealed.", "«bırakmayı» — en ile mansub; fâil gizli «o»."),
  tok("الْأُمَرَاءَ", "amir", "noun", ["maful-bihi", "mamnu-min-sarf", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ أَمِيرٍ.", "«the governors» — the object; the plural of أَمِير.", "«emîrleri» — mef'ûl; «emîr»in cem'i."),
  khamsa("يَأْكُلُونَ", "akala", "«eat»", "«yerler»", tags=["hal"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْأُمَرَاءِ"),
  *amwal("أَمْوَالَ", None, "«the wealth (of)»", "«mallarını»", punct=".", mudaf_ilayh=("النَّاسِ", "nas", "noun", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the people» — the muḍāf ilayh.", "«insanlar» — muzâfun ileyh."))])
sen("s27", "And Yūsuf could not bear to see the people go hungry and die.", "Yusuf, insanların aç kalıp öldüğünü görmeye dayanamıyordu.", [
  kana(), yusuf_ism_kana(), la_nafiya(),
  tok("يَقْدِرُ", "qadara-able", "verb", [K, "la-nafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«could» — rafʿ after the negating lā; the clause is kāna's khabar.", "«gücü yetmek» — nefiy lâ'sından sonra merfû; cümle kâne'nin haberi."),
  an_("يَقْدِرُ", "«could»", "«gücü yetiyordu»"),
  tok("يَرَى", "raa", "verb", ["an-masdariyya", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to see» — in naṣb after an, the fatḥa estimated on the alif.", "«görmeyi» — en ile mansub, fethası elif üzerinde takdîrî."),
  maful("النَّاسَ", "nas", "«the people»", "«insanları»"),
  khamsa("يَجُوعُونَ", "jaa-hunger", "«go hungry»", "«acıkırlar»", tags=["hal", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ النَّاسِ"),
  khamsa("وَيَمُوتُونَ", "mata-die", "«and die»", "«ve ölürler»", wa=True, tags=["atf-nasaq", "hollow-verbs"], punct=".")])
sen("s28", "And Yūsuf was not ashamed of the truth.", "Yusuf haktan utanmazdı.", [
  kana(), yusuf_ism_kana(), la_nafiya(),
  tok("يَسْتَحِي", "istahya", "verb", [K, "la-nafiya", "mudari-marfu", "form-x-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ (وَفِيهِ لُغَتَانِ: يَسْتَحْيِي وَيَسْتَحِي).", "«is ashamed» — rafʿ after lā, the ḍamma estimated on the yāʾ; the clause is kāna's khabar (the verb has two forms, يَسْتَحْيِي and يَسْتَحِي).", "«utanmak» — lâ'dan sonra merfû, zammesi yâ üzerinde takdîrî; cümle kâne'nin haberi (fiilin iki şekli vardır: يَسْتَحْيِي ve يَسْتَحِي)."),
  min_(full="مِنَ"), majrur("الْحَقِّ", "haqq", "«the truth»", "«hak»", "مِنْ", punct=".")])
sen("s29", "So he said to the king:", "Bunun üzerine krala dedi:", [
  qala_h(full="فَقَالَ", fa=True, punct=None),
  tok("لِلْمَلِكِ", "malik-king", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمَلِكِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِقَالَ.", "«to the king» — in jarr.", "«krala» — mecrur.", punct=":", segments=[seg("لِ", "li", "prep"), seg("لْمَلِكِ", "malik-king", "noun")])])
sen("s30", "«Set me over the treasuries of the land; indeed I am a keeper, knowing.» (Yūsuf 12:55)", "«Beni yeryüzünün hazinelerinin başına getir; şüphesiz ben koruyucu ve bilenim.» (Yûsuf 12:55)", quran([
  tok("اِجْعَلْنِي", "jaala", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.", "«set me» — an imperative on sukūn; «you» concealed; the nūn of protection and the speaker's yāʾ as first object.", "«beni getir» — sükûn üzere mebnî emir; fâil gizli «sen»; vikâye nûnu, mütekellim yâsı birinci mef'ûl.", segments=[seg("اِجْعَلْ", "jaala", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ.", "«over» — the phrase stands as the second object.", "«başına» — şibh-i cümle ikinci mef'ûl."),
  *khazain_ard(),
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the speaker's yāʾ as its ism.", "«şüphesiz ben» — inne, mütekellim yâsı ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  *hafiz_alim(case="raf", punct=".")]))
sen("s31", "And so Yūsuf became the trustee of the treasuries of Egypt.", "Böylece Yusuf Mısır hazinelerinin emîni oldu.", [
  tok("وَهٰكَذَا", "hakadha", "pron", ["anwa-al-waw", "asma-al-ishara", "maful-mutlaq"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰكَذَا: الْهَاءُ لِلتَّنْبِيهِ وَالْكَافُ لِلتَّشْبِيهِ وَذَا اسْمُ إِشَارَةٍ — فِي مَحَلِّ نَصْبٍ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ (كَوْنًا هٰكَذَا).", "«and so» — the demonstrative compound, standing for an omitted maṣdar.", "«ve böylece» — işaret bileşiği, hazfedilmiş masdarın sıfatı.", segments=wa_("هٰكَذَا", "hakadha", "pron")),
  kana(wa=False, full="كَانَ"), yusuf_ism_kana(),
  khabar_kana("أَمِينًا", "amin", "«a trustee»", "«emîn»"),
  tok("لِخَزَائِنِ", "khizana", "noun", ["huruf-jarr", "idafa-definiteness", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَخَزَائِنِ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ — مُتَعَلِّقٌ بِأَمِينًا.", "«over the treasuries (of)» — in jarr after the lām; a muḍāf.", "«hazinelerinin» — lâm ile mecrur; muzâf.", segments=[seg("لِ", "li", "prep"), seg("خَزَائِنِ", "khizana", "noun")]),
  name_mudaf_ilayh("مِصْرَ", "misr", "«Egypt»", "«Mısır»", punct=".")])
sen("s32", "And the people were greatly relieved, and praised Allah.", "İnsanlar pek rahatladı ve Allah'a hamdettiler.", [
  mazi("وَاسْتَرَاحَ", "istaraha", "«were relieved»", "«rahatladı»", hidden=None, wa=True, tags=["form-x-verbs", "hollow-verbs"]), nas_fail(), jiddan(),
  mazi_pl("وَحَمِدُوا", "hamida", "«and praised»", "«ve hamdettiler»", wa=True, tags=["atf-nasaq"]),
  tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah'a» — mef'ûl.", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "ishtaqa": G("ishtaqa", "اِشْتَاقَ", "ش و ق", "verb", "to long (for), to yearn (اِشْتَاقَ إِلَى)", "özlemek, hasret çekmek", 3, form="VIII"),
 "istakhlasa": G("istakhlasa", "اِسْتَخْلَصَ", "خ ل ص", "verb", "to take for oneself, to single out", "kendine ayırmak, seçmek", 3, form="X"),
 "intazara": G("intazara", "اِنْتَظَرَ", "ن ظ ر", "verb", "to wait for, to await", "beklemek", 2, form="VIII"),
 "asraa": G("asraa", "أَسْرَعَ", "س ر ع", "verb", "to hurry, to be quick", "acele etmek, hızlanmak", 2, form="IV"),
 "abiyy": G("abiyy", "أَبِيّ", "أ ب ي", "noun", "proud, unbending, refusing what is base (ṣifa mushabbaha)", "onurlu, boyun eğmez (sıfat-ı müşebbehe)", 3),
 "taftish": G("taftish", "تَفْتِيش", "ف ت ش", "noun", "an inquiry, an investigation (maṣdar of فَتَّشَ)", "soruşturma, teftiş (fetteşe'nin masdarı)", 3),
 "bahth": G("bahth", "بَحْث", "ب ح ث", "noun", "an investigation, a search (maṣdar of بَحَثَ)", "araştırma (bahase'nin masdarı)", 2),
 "qadiyya": G("qadiyya", "قَضِيَّة", "ق ض ي", "noun", "a case, a cause (at law)", "dava, mesele", 3, plural="قَضَايَا"),
 "khizana": G("khizana", "خِزَانَة", "خ ز ن", "noun", "a treasury, a storehouse", "hazine, ambar", 2, plural="خَزَائِن"),
 "dai-lost": G("dai-lost", "ضَائِع", "ض ي ع", "noun", "lost, going to waste (ism fāʿil of ضَاعَ)", "zayi, kaybolmuş (dâa'nın ism-i fâili)", 3),
 "kalb": G("kalb", "كَلْب", "ك ل ب", "noun", "a dog", "köpek", 1, plural="كِلَاب"),
 "labisa": G("labisa", "لَبِسَ", "ل ب س", "verb", "to wear, to put on; (of a house) to be clothed, furnished", "giymek; (ev) donatılmak", 1, form="I"),
 "hafiz-keeper": G("hafiz-keeper", "حَفِيظ", "ح ف ظ", "noun", "a keeper, a guardian (ṣifa mushabbaha on فَعِيل)", "koruyucu, muhafız (فَعِيل vezninde sıfat-ı müşebbehe)", 2),
 "jaa-hunger": G("jaa-hunger", "جَاعَ", "ج و ع", "verb", "to be hungry", "acıkmak", 2, form="I"),
 "istahya": G("istahya", "اِسْتَحْيَا", "ح ي ي", "verb", "to be ashamed (of) — also written اِسْتَحَى، يَسْتَحِي", "utanmak — اِسْتَحَى، يَسْتَحِي de yazılır", 3, form="X"),
 "istaraha": G("istaraha", "اِسْتَرَاحَ", "ر و ح", "verb", "to be relieved, to rest", "rahatlamak, dinlenmek", 2, form="X"),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("siddiq", "صديق"), ("liqa", "لقاء"), ("rasul", "رسول"), ("radiya", "رضي"), ("ams", "أمس"), ("aql", "عقل"), ("bab", "باب"), ("amana", "أمانة"), ("mal", "مال"), ("amir", "أمير"), ("intafaa", "انتفع"), ("mata-die", "مات"), ("hamida", "حمد"), ("law", "لو"), ("lam-jawab", "ل"), ("jaa", "جاء"), ("alim", "عليم"), ("khana", "خان"), ("nasaha", "نصح"), ("sayyid", "سيد"), ("hakadha", "هكذا"), ("dhaki", "ذكي"), ("bari", "بريء"), ("amin", "أمين"), ("kabir", "كبير"), ("ana", "أنا"), ("huwa", "هو")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("ishtaqa", "istakhlasa", "intazara", "asraa", "labisa", "jaa-hunger", "istahya", "istaraha"): mo["verbs"].pop(_k, None)
put_morph(mo, "ishtaqa", _sg.derived_hollow("مِنْ بَابِ الِافْتِعَالِ — أَجْوَفُ وَاوِيٌّ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِشْتَاق", "اِشْتَق", "شْتَاق", "شْتَق", "اِشْتَاق", "اِشْتَق", "اِشْتِيَاق", "مُشْتَاق", "مُشْتَاق (إِلَيْهِ)", "اُشْتِيقَ", "يُشْتَاقُ", note="لَازِمٌ، يَتَعَدَّى بِإِلَى: اِشْتَاقَ إِلَى لِقَائِهِ — قُلِبَتِ الْوَاوُ أَلِفًا لِتَحَرُّكِهَا وَانْفِتَاحِ مَا قَبْلَهَا."))
put_morph(mo, "istakhlasa", _sg.derived("مِنْ بَابِ الِاسْتِفْعَالِ", "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ", "اِسْتَخْلَص", "سْتَخْلِص", "اِسْتَخْلِص", "اِسْتِخْلَاص", "مُسْتَخْلِص", "مُسْتَخْلَص", "اُسْتُخْلِصَ", "يُسْتَخْلَصُ", note="مُتَعَدٍّ: اِسْتَخْلَصَهُ لِنَفْسِهِ."))
put_morph(mo, "intazara", _sg.derived("مِنْ بَابِ الِافْتِعَالِ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِنْتَظَر", "نْتَظِر", "اِنْتَظِر", "اِنْتِظَار", "مُنْتَظِر", "مُنْتَظَر", "اُنْتُظِرَ", "يُنْتَظَرُ", note="مُتَعَدٍّ: اِنْتَظَرَهُ."))
put_morph(mo, "asraa", _sg.derived("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَسْرَع", "سْرِع", "أَسْرِع", "إِسْرَاع", "مُسْرِع", "مُسْرَع", "أُسْرِعَ", "يُسْرَعُ", note="لَازِمٌ: أَسْرَعَ إِلَى الْبَابِ."))
put_morph(mo, "labisa", _sg.sound1("samia", "لَبِس", "لْبَس", "اِلْبَس", "لُبْس", "لَابِس", "مَلْبُوس", "لُبِسَ", "يُلْبَسُ", note="مُتَعَدٍّ: لَبِسَ الثَّوْبَ — مِنْ بَابِ سَمِعَ."))
put_morph(mo, "jaa-hunger", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "جَاع", "جُع", "جُوع", "جُع", "جُوع", "جُع", "جُوع", "جَائِع", note="لَازِمٌ: جَاعَ يَجُوعُ، جُعْتُ."))
put_morph(mo, "istahya", _sg.derived_naqis("مِنْ بَابِ الِاسْتِفْعَالِ — نَاقِصٌ يَائِيٌّ", "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ", "اِسْتَحْيَ", "سْتَحْي", "i", "اِسْتَحْي", "اِسْتِحْيَاء", "مُسْتَحْيٍ", "مُسْتَحْيًى (مِنْهُ)", "اُسْتُحْيِيَ", "يُسْتَحْيَا", note="لَازِمٌ، يَتَعَدَّى بِمِنْ: اِسْتَحْيَا مِنْهُ — فِيهِ لُغَتَانِ: اِسْتَحْيَا يَسْتَحْيِي (لُغَةُ الْحِجَازِ، الْمُثْبَتَةُ هُنَا) وَاِسْتَحَى يَسْتَحِي (لُغَةُ تَمِيمٍ)؛ النَّصُّ يَكْتُبُ يَسْتَحِي."))
put_morph(mo, "istaraha", _sg.derived_hollow("مِنْ بَابِ الِاسْتِفْعَالِ — أَجْوَفُ وَاوِيٌّ", "اِسْتَفْعَلَ يَسْتَفْعِلُ", "َ", "اِسْتَرَاح", "اِسْتَرَح", "سْتَرِيح", "سْتَرِح", "اِسْتَرِيح", "اِسْتَرِح", "اِسْتِرَاحَة", "مُسْتَرِيح", "مُسْتَرَاح", "اُسْتُرِيحَ", "يُسْتَرَاحُ", note="لَازِمٌ: اِسْتَرَاحَ النَّاسُ — نُقِلَتْ حَرَكَةُ الْوَاوِ إِلَى السَّاكِنِ قَبْلَهَا ثُمَّ قُلِبَتْ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 15 (print pp. 47–51, «أَحْسَنُ الْقَصَصِ» sections 14 «الْمَلِكُ يُرْسِلُ إِلَى يُوسُفَ», 15 «يُوسُفُ يَسْأَلُ التَّفْتِيشَ» and 16 «عَلَى خَزَائِنِ الْأَرْضِ»): the king's joy and his question, the cupbearer's answer, the summons with Yūsuf 12:54 (s4, marked); Yūsuf's refusal to leave the prison unexamined, the unreal condition of the hasty man, the inquiry and the acquittal; the sermon on trust and the treasuries, Yūsuf 12:55 (s30, marked), the trusteeship and the people's relief. "
          "One printed line is one sentence except where a page break cuts a sentence (s5 joins the lammā clause to its answer across pp. 47–48; s13 across pp. 48–49); the print's «!» after يَدْعُوكَ in s5 and after يُوسُفُ in s6 is kept; s29 (فَقَالَ لِلْمَلِكِ) closes on the print's full stop, read here as the colon that opens s30; the saying verbs of s1, s2, s3 and s12 keep the print's colon; the print's parentheses around the ayas are read as quotation marks.")
ADD_TR = (" On beşinci bölüm (basılı s. 47–51, «أَحْسَنُ الْقَصَصِ» 14. kısım «الْمَلِكُ يُرْسِلُ إِلَى يُوسُفَ», 15. kısım «يُوسُفُ يَسْأَلُ التَّفْتِيشَ» ve 16. kısım «عَلَى خَزَائِنِ الْأَرْضِ»): kralın sevinci ve sorusu, sâkînin cevabı, Yûsuf 12:54 ile çağrı (s4, işaretli); Yusuf'un zindandan soruşturmasız çıkmayı reddi, aceleci adamın gerçek dışı şartı, soruşturma ve beraat; emanet ve hazineler üzerine vaaz, Yûsuf 12:55 (s30, işaretli), hazine emînliği ve insanların ferahlaması. "
          "Basılı her satır bir cümledir; sayfa sonunun böldüğü yerlerde cümle birleştirilmiştir (s5 lemmâ cümlesini cevabıyla s. 47–48 arasında, s13 s. 48–49 arasında birleştirir); s5'te يَدْعُوكَ ve s6'da يُوسُفُ sonrasındaki baskı «!» korunmuştur; s29 (فَقَالَ لِلْمَلِكِ) baskıda nokta ile biter, burada s30'u açan iki nokta olarak okunmuştur; s1, s2, s3 ve s12'nin söyleme fiilleri baskının iki noktasını korur; baskının âyetleri saran parantezleri tırnak olarak okunmuştur.")
write_out(15, S, TITLE, ADD_EN, ADD_TR, "pp. 47–51", GLOSS_ADD)
report(15, S, GLOSS_ADD, ())
