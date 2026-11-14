# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 17: «بَيْنَ يُوسُفَ وَإِخْوَتِهِ» — «أَحْسَنُ الْقَصَصِ» section 18 (print pp. 53–55):
the dialogue between Yūsuf and his brothers, the order for food, Yūsuf 12:59, the condition and the returned money. Every printed
line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch17.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "بَيْنَ يُوسُفَ وَإِخْوَتِهِ", "en": "Between Yūsuf and his brothers", "tr": "Yusuf ile kardeşleri arasında"}
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

# ================================================================ §18 بين يوسف وإخوته (pp. 53–55)
sen("s1", "And Yūsuf spoke to them and said to them:", "Yusuf onlarla konuştu ve onlara dedi:", [
  verb_enc("وَكَلَّمَهُمْ", "kallama", "هُمْ", "pron-3mp", "«spoke to them»", "«onlarla konuştu»", mudari=False, hidden=None, wa=True, tags=["form-ii-verbs"]), yusuf_fail(),
  qala(full="وَقَالَ", wa=True, hidden="هُوَ", punct=None), lahu("لَهُمْ", "هُمْ", "pron-3mp", "مُتَعَلِّقٌ بِقَالَ.", "«to them».", "«onlara».", punct=":")])
sen("s2", "Where are you from?", "Nerelisiniz?", [
  min_(), tok("أَيْنَ", "ayna", "pron", ["al-istifham", "huruf-jarr", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ بِمِنْ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«where» — the question noun in the place of jarr after min; the phrase is the fronted khabar.", "«nere» — istifham ismi, min ile mahallen mecrur; şibh-i cümle mukaddem haber."),
  tok("أَنْتُمْ", "antum", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«you (pl.)» — the detached pronoun, the delayed mubtadaʾ.", "«siz» — munfasıl zamir, muahhar mübtedâ.", punct="؟")])
sen("s3", "They said: From Canaan!", "Dediler: Kenan'dan!", [
  qalu_(), min_(),
  tok("كَنْعَانَ", "kanan", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ — وَشِبْهُ الْجُمْلَةِ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ (نَحْنُ مِنْ كَنْعَانَ).", "«Canaan» — in jarr by a fatḥa: a foreign diptote name; the phrase is the khabar of an omitted «we».", "«Kenan» — fetha ile mecrur: yabancı gayr-i munsarıf isim; şibh-i cümle hazfedilmiş «biz»in haberi.", punct="!")])
sen("s4", "He said: Who is your father?", "Dedi: Babanız kim?", [
  qala(hidden="هُوَ"), man_mubt(), abu_kum(punct="؟")])
sen("s5", "They said: Yaʿqūb, son of Isḥāq, son of Ibrāhīm (upon them be blessings and peace).", "Dediler: Yakub, İshak oğlu, İbrahim oğlu (onlara salât ve selâm olsun).", [
  qalu_(),
  tok("يَعْقُوبُ", "yaqub", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: أَبُونَا، مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yaʿqūb» — the khabar of an omitted «our father is»; a diptote name.", "«Yakub» — hazfedilmiş «babamız»ın haberi; gayr-i munsarıf özel isim."),
  tok("بْنُ", "ibn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ — حُذِفَتْ أَلِفُهُ لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.", "«son (of)» — the naʿt; its alif dropped between two names.", "«oğlu» — sıfat; iki özel isim arasında elifi düşmüş."),
  tok("إِسْحٰقَ", "ishaq", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Isḥāq» — the muḍāf ilayh, jarr by a fatḥa; a diptote.", "«İshak» — muzâfun ileyh, fetha ile mecrur; gayr-i munsarıf."),
  tok("بْنِ", "ibn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِإِسْحٰقَ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«son (of)» — the naʿt of Isḥāq, in jarr; a muḍāf.", "«oğlu» — İshak'ın sıfatı, mecrur; muzâf."),
  tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the muḍāf ilayh, jarr by a fatḥa; a diptote.", "«İbrahim» — muzâfun ileyh, fetha ile mecrur; gayr-i munsarıf."),
  tok("عَلَيْهِمُ", "ala", "prep", ["huruf-jarr", "mubtada-khabar"], "عَلَى حَرْفُ جَرٍّ، وَهِمْ فِي مَحَلِّ جَرٍّ، وَضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ (جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ).", "«upon them» — the phrase is the fronted khabar of a parenthetical prayer; the mīm takes a ḍamma before the wasl.", "«onlara» — şibh-i cümle muteriza dua cümlesinin mukaddem haberi; mîm iki sâkin için zammeli.", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِمُ", "pron-3mp", "pron")]),
  tok("الصَّلَوَاتُ", "salat", "noun", ["mubtada-khabar", "jam-muannath-salim"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«blessings» — the delayed mubtadaʾ; a sound feminine plural.", "«salâtlar» — muahhar mübtedâ; cem-i müennes sâlim."),
  tok("وَالسَّلَامُ", "salam", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالسَّلَامُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and peace» — joined, in rafʿ.", "«ve selâm» — ma'tûf, merfû.", punct=".", segments=wa_("السَّلَامُ", "salam", "noun"))])
S[-1]["tokens"][6]["quoteBefore"] = "("; S[-1]["tokens"][8]["quoteAfter"] = ")"
sen("s6", "He said: Have you another brother?", "Dedi: Başka bir kardeşiniz var mı?", [
  qala(hidden="هُوَ"),
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«is there…?» — the question particle.", "«… mı?» — istifham harfi."),
  lakum(role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ", tags=["mubtada-khabar"]),
  akh_mubt_muakhkhar(),
  tok("آخَرُ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (وَصْفٌ عَلَى أَفْعَلَ).", "«another» — the naʿt; a diptote adjective on أَفْعَل.", "«başka» — sıfat; أَفْعَل vezninde gayr-i munsarıf.", punct="؟")])
sen("s7", "They said: Yes, we have a brother whose name is Binyāmīn!", "Dediler: Evet, adı Bünyamin olan bir kardeşimiz var!", [
  qalu_(),
  tok("نَعَمْ", "naam", "part", [], "حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«yes» — the answer particle.", "«evet» — cevap harfi."),
  lana(), akh_mubt_muakhkhar(),
  *ismuhu_name("بِنْيَامِينُ", "binyamin", "«Binyāmīn»", "«Bünyamin»", punct="!")])
sen("s8", "He said: Why did he not come with you?", "Dedi: Niçin sizinle gelmedi?", [
  qala(hidden="هُوَ"),
  tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِجَاءَ.", "«why» — the jarr lām over the question noun.", "«niçin» — cer lâmı ve istifham ismi."),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
  mazi("جَاءَ", "jaa", "«did (not) come»", "«gelmedi»", hidden="هُوَ", tags=["hollow-verbs"]),
  maa_pron("مَعَكُمْ", "كُمْ", "pron-2mp", "«with you»", "«sizinle»", role="مُتَعَلِّقٌ بِجَاءَ", punct="؟")])
sen("s9", "They said: Because our father does not leave him and does not like him to be far from him.", "Dediler: Çünkü babamız onu bırakmaz ve ondan uzak olmasını sevmez.", [
  qalu_(),
  tok("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«because» — the lām of cause over anna.", "«çünkü» — ta'lîl lâmı ve enne."),
  mudaf_pron("وَالِدَنَا", "walid-father", "نَا", "pron-1p", "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ", "«our father» — anna's ism", "«babamız» — enne'nin ismi", tags=["inna-wa-akhawatuha"]),
  la_nafiya(),
  verb_enc("يَتْرُكُهُ", "taraka", "هُ", "pron-3ms", "«leave him»", "«onu bırakmaz»", tags=["inna-wa-akhawatuha", "la-nafiya"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  la_nafiya(wa=True),
  mudari("يُحِبُّ", "ahabba", "«like»", "«sevmez»", tags=["la-nafiya", "atf-nasaq", "form-iv-verbs", "doubled-verbs"]),
  an_("يُحِبُّ", "«like»", "«sever»"),
  tok("يَبْعُدَ", "baada", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to be far» — in naṣb after an; «he» concealed.", "«uzak olmayı» — en ile mansub; fâil gizli «o»."),
  tok("عَنْهُ", "an", "prep", ["huruf-jarr"], "عَنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَبْعُدَ.", "«from him».", "«ondan».", punct=".", segments=[seg("عَنْ", "an", "prep"), seg("هُ", "pron-3ms", "pron")])])
sen("s10", "He said: For what reason does he not leave him — is he a very small child?", "Dedi: Hangi sebeple onu bırakmaz, o çok küçük bir çocuk mu?", [
  qala(hidden="هُوَ"),
  tok("لِأَيِّ", "ayy", "pron", ["al-istifham", "huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَأَيِّ اسْمُ اسْتِفْهَامٍ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِيَتْرُكُ.", "«for what» — the jarr lām over the question noun أَيّ, the one interrogative that declines; a muḍāf.", "«hangi … için» — cer lâmı ve i'rab alan tek istifham ismi أَيّ; muzâf.", segments=[seg("لِ", "li", "prep"), seg("أَيِّ", "ayy", "pron")]),
  mi("شَيْءٍ", "shay", "«thing»", "«şey»"),
  la_nafiya(),
  verb_enc("يَتْرُكُهُ", "taraka", "هُ", "pron-3ms", "«leave him»", "«onu bırakmaz»", tags=["la-nafiya"]),
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«is…?» — the question particle.", "«… mı?» — istifham harfi."),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«he» — the detached pronoun as mubtadaʾ.", "«o» — munfasıl zamir, mübtedâ."),
  khabar_raf("وَلَدٌ", "walad", "«a child»", "«bir çocuk»"),
  nat_raf("صَغِيرٌ", "saghir", "«small»", "«küçük»"),
  jiddan(punct="؟")])
sen("s11", "They said: No — but he had a brother whose name was Yūsuf; he went out with us once, and we went off racing and left Yūsuf by our baggage, and the wolf ate him.", "Dediler: Hayır — ama onun Yusuf adında bir kardeşi vardı; bir kez bizimle gitti, biz de yarışmaya gittik ve Yusuf'u eşyamızın yanında bıraktık; onu kurt yedi.", [
  qalu_(),
  tok("لَا", "la-jawab", "part", [], "حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«no» — the answer particle.", "«hayır» — cevap harfi.", punct=":"),
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«ama» — muhaffef lâkin, amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  kana_bare(),
  lahu("لَهُ", "هُ", "pron-3ms", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«he had» — the phrase is kāna's fronted khabar.", "«onun … vardı» — şibh-i cümle kâne'nin mukaddem haberi.", tags=[K]),
  tok("أَخٌ", "akh", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a brother» — kāna's delayed ism.", "«bir kardeş» — kâne'nin muahhar ismi."),
  *ismuhu_name("يُوسُفُ", "yusuf", "«Yūsuf»", "«Yusuf»", punct="،"),
  mazi("ذَهَبَ", "dhahaba", "«he went»", "«gitti»", hidden="هُوَ"),
  maa_pron("مَعَنَا", "نَا", "pron-1p", "«with us»", "«bizimle»", role="مُتَعَلِّقٌ بِذَهَبَ"),
  tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (اسْمُ مَرَّةٍ).", "«once» — standing in for the absolute object (the noun of one time).", "«bir kez» — mef'ûl-i mutlak nâibi (ism-i merre).", punct="،"),
  tok("وَذَهَبْنَا", "dhahaba", "verb", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَذَهَبْنَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرُ الْمُتَكَلِّمِينَ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«and we went» — a māḍī on sukūn before nā, the doer «we».", "«ve gittik» — nâ'dan önce sükûn üzere mebnî mâzî; nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("ذَهَبْ", "dhahaba", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("نَسْتَبِقُ", "istabaqa", "verb", ["hal", "mudari-marfu", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«racing one another» — a muḍāriʿ with «we» concealed; the clause is a ḥāl.", "«yarışarak» — muzâri, fâil gizli «biz»; cümle hâldir."),
  tok("وَتَرَكْنَا", "taraka", "verb", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَتَرَكْنَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«and we left» — a māḍī on sukūn before nā, the doer «we».", "«ve bıraktık» — nâ'dan önce sükûn üzere mebnî mâzî; nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("تَرَكْ", "taraka", "verb"), seg("نَا", "pron-1p", "pron")]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«by» — an adverb of place; a muḍāf.", "«yanında» — mekân zarfı; muzâf."),
  mudaf_pron("مَتَاعِنَا", "mata-goods", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "«our baggage» — the muḍāf ilayh", "«eşyamız» — muzâfun ileyh"),
  tok("فَأَكَلَهُ", "akala", "verb", ["atf-nasaq", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَأَكَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«and … ate him» — joined by fāʾ; the pronoun its object.", "«ve onu yedi» — fâ ile ma'tûf; zamir mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("أَكَلَ", "akala", "verb"), seg("هُ", "pron-3ms", "pron")]),
  dhib_fail(punct=".")])
sen("s12", "And Yūsuf laughed inwardly, but said nothing.", "Yusuf içinden güldü, fakat bir şey söylemedi.", [
  mazi("وَضَحِكَ", "dahika", "«laughed»", "«güldü»", hidden=None, wa=True), yusuf_fail(),
  fi(), mudaf_pron("نَفْسِهِ", "nafs", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«himself» — in jarr", "«kendisi» — mecrur", tags=["huruf-jarr"]),
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«fakat» — muhaffef lâkin, amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  lam_jazim(),
  tok("يَقُلْ", "qala", "verb", ["lam-jazim", "hollow-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«did (not) say» — jazm after lam; the hollow verb's wāw dropped before the sukūn.", "«söylemedi» — lem ile meczum; ecvef fiilin vâvı iki sâkin için düşmüş."),
  maful("شَيْئًا", "shay", "«anything»", "«bir şey»", punct=".")])
sen("s13", "And Yūsuf longed for his brother Binyāmīn.", "Yusuf kardeşi Bünyamin'i özledi.", [
  mazi("وَاشْتَاقَ", "ishtaqa", "«longed»", "«özledi»", hidden=None, wa=True, tags=["form-viii-verbs", "hollow-verbs"]), yusuf_fail(),
  ila(), tok("أَخِيهِ", "akh", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his brother» — in jarr by the yāʾ of the five nouns; annexed to the pronoun.", "«kardeşi» — beş isimden olduğu için yâ ile mecrur; zamire muzâf.", segments=[seg("أَخِي", "akh", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("بِنْيَامِينَ", "binyamin", "propn", ["badal", "mamnu-min-sarf"], "بَدَلٌ مِنْ أَخِيهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ (أَوْ عَطْفُ بَيَانٍ).", "«Binyāmīn» — the badal of «his brother», jarr by a fatḥa: a diptote (or an explanatory apposition).", "«Bünyamin» — «kardeşi»nin bedeli, fetha ile mecrur: gayr-i munsarıf (ya da atf-ı beyan).", punct=".")])
sen("s14", "And Allah wanted to test Yaʿqūb a second time.", "Allah, Yakub'u ikinci bir kez sınamak istedi.", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), allah_fail(),
  an_("أَرَادَ", "«wanted»", "«istedi»"),
  tok("يَمْتَحِنَ", "imtahana", "verb", ["an-masdariyya", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to test» — in naṣb after an; «He» concealed.", "«sınamayı» — en ile mansub; fâil gizli «O»."),
  name_maful("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub'u»"),
  tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a time» — standing in for the absolute object.", "«bir kez» — mef'ûl-i mutlak nâibi."),
  nat_nasb("ثَانِيَةً", "thani", "«second»", "«ikinci»", punct=".")])
sen("s15", "So Yūsuf ordered food for them.", "Bunun üzerine Yusuf onlar için yiyecek verilmesini emretti.", [
  fa_mazi("فَأَمَرَ", "amara-v", "«so … ordered»", "«bunun üzerine … emretti»", hidden=None),
  lahu("لَهُمْ", "هُمْ", "pron-3mp", "مُتَعَلِّقٌ بِأَمَرَ.", "«for them».", "«onlar için»."),
  yusuf_fail(),
  tok("بِالطَّعَامِ", "taam", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالطَّعَامِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِأَمَرَ.", "«food» — in jarr after the bāʾ.", "«yiyecek» — bâ ile mecrur.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الطَّعَامِ", "taam", "noun")])])
sen("s16", "And he said to them: «Bring me a brother of yours from your father.» (Yūsuf 12:59)", "Ve onlara dedi: «Bana babanızdan olan bir kardeşinizi getirin.» (Yûsuf 12:59)", [
  qala(full="وَقَالَ", wa=True, hidden="هُوَ", punct=None), lahu("لَهُمْ", "هُمْ", "pron-3mp", "مُتَعَلِّقٌ بِقَالَ.", "«to them».", "«onlara».", punct=":"),
  *quran([
  tok("ائْتُونِي", "ata", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«bring me» — a plural imperative, the nūn dropped; the wāw its doer; the nūn of protection and the speaker's yāʾ as object.", "«bana getirin» — nûnun hazfi ile mebnî emir; vâv fâil; vikâye nûnu ve mütekellim yâsı mef'ûl.", segments=[seg("ائْتُو", "ata", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("بِأَخٍ", "akh", "noun", ["huruf-jarr", "five-nouns"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَخٍ مَجْرُورٌ بِالْكَسْرَةِ — الْأَسْمَاءُ الْخَمْسَةُ تُعْرَبُ بِالْحَرَكَاتِ إِذَا لَمْ تُضَفْ.", "«a brother» — in jarr after the bāʾ; the five nouns decline by vowels when not annexed.", "«bir kardeş» — bâ ile mecrur; beş isim muzâf olmayınca harekeyle i'rab olunur.", segments=[seg("بِ", "bi", "prep"), seg("أَخٍ", "akh", "noun")]),
  lakum(role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِأَخٍ", tags=["naat-sifa"]),
  min_(),
  tok("أَبِيكُمْ", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«your father» — in jarr by the yāʾ of the five nouns; annexed to the pronoun.", "«babanız» — beş isimden olduğu için yâ ile mecrur; zamire muzâf.", punct=".", segments=[seg("أَبِي", "ab", "noun"), seg("كُمْ", "pron-2mp", "pron")])])])
sen("s17", "And you will find no food if you do not bring him.", "Onu getirmezseniz yiyecek bulamazsınız.", [
  la_nafiya(wa=True),
  khamsa("تَجِدُونَ", "wajada", "«you will find»", "«bulursunuz»", tags=["la-nafiya", "mithal-verbs"], extra_ar=" — مِثَالٌ وَاوِيٌّ حُذِفَتْ وَاوُهُ"),
  maful("طَعَامًا", "taam", "«food»", "«yiyecek»"),
  tok("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، غَيْرُ جَازِمٍ.", "«if, when» — the conditional time adverb; it governs no jazm.", "«-se, -diğinde» — şart manası taşıyan zaman zarfı; cezm etmez."),
  lam_jazim(),
  tok("تَأْتُوا", "ata", "verb", ["lam-jazim", "afal-khamsa", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ — فِعْلُ الشَّرْطِ.", "«you (do not) bring» — jazm after lam, the nūn dropped; the wāw its doer; the condition's verb.", "«getirmezseniz» — lem ile meczum, nûnun hazfi ile; vâv fâil; şart fiili."),
  tok("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِتَأْتُوا.", "«him».", "«onu».", punct=".", segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")])])
sen("s18", "And Yūsuf gave orders about their money, and it was put into their baggage.", "Yusuf paraları hakkında emir verdi ve para eşyalarının içine kondu.", [
  mazi("وَأَمَرَ", "amara-v", "«gave orders»", "«emretti»", hidden=None, wa=True), yusuf_fail(),
  tok("بِمَالِهِمْ", "mal", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَالِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِأَمَرَ.", "«about their money» — in jarr after the bāʾ; annexed to the pronoun.", "«paraları hakkında» — bâ ile mecrur; zamire muzâf.", segments=[seg("بِ", "bi", "prep"), seg("مَالِ", "mal", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("فَوُضِعَ", "wadaa", "verb", ["atf-nasaq", "naib-al-fail", "mithal-verbs"], "الْفَاءُ عَاطِفَةٌ، وَوُضِعَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (الْمَالُ).", "«and it was put» — a passive māḍī; its deputy doer «it» (the money) concealed.", "«ve kondu» — meçhul mâzî; nâib-i fâil gizli «o» (para).", segments=[seg("فَ", "fa", "conj"), seg("وُضِعَ", "wadaa", "verb")]),
  fi(), mudaf_pron("مَتَاعِهِمْ", "mata-goods", "هِمْ", "pron-3mp", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«their baggage» — in jarr", "«eşyaları» — mecrur", tags=["huruf-jarr"], punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "kanan": G("kanan", "كَنْعَان", None, "propn", "Canaan — the land of Yaʿqūb (a foreign diptote)", "Kenan — Yakub'un ülkesi (yabancı, gayr-i munsarıf)", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("kallama", "كلم"), ("imtahana", "امتحن"), ("thani", "ثاني"), ("wadaa", "وضع"), ("walad", "ولد"), ("saghir", "صغير"), ("ism-name", "اسم"), ("antum", "أنتم"), ("salat", "صلاة"), ("salam", "سلام"), ("hal-istifham", "هل"), ("naam", "نعم"), ("limadha", "لماذا"), ("ayy", "أي"), ("marra-once", "مرة"), ("istabaqa", "استبق"), ("mata-goods", "متاع"), ("amara-v", "أمر"), ("ab", "أب"), ("ishaq", "إسحاق"), ("ibrahim", "إبراهيم")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 17 (print pp. 53–55, «أَحْسَنُ الْقَصَصِ» section 18 «بَيْنَ يُوسُفَ وَإِخْوَتِهِ»): the questions and answers between Yūsuf and his brothers — Canaan, Yaʿqūb son of Isḥāq son of Ibrāhīm, the other brother Binyāmīn, the lost brother «eaten by the wolf», Yūsuf's inward laugh and his longing, the order for food, Yūsuf 12:59 (s16, marked), the condition, and the money returned into the baggage. "
          "One printed line is one sentence; the print's «!» after كَنْعَانَ (s3) and بِنْيَامِينُ (s7) and its «؟» are kept; the print's parenthetical blessing in s5 is set in parentheses, not as a quotation; the saying verbs keep the print's colon, and s11's «لَا:» keeps the print's colon after the answer particle; the print's parentheses around the aya are read as quotation marks.")
ADD_TR = (" On yedinci bölüm (basılı s. 53–55, «أَحْسَنُ الْقَصَصِ» 18. kısım «بَيْنَ يُوسُفَ وَإِخْوَتِهِ»): Yusuf ile kardeşleri arasındaki sorular ve cevaplar — Kenan, İshak oğlu İbrahim oğlu Yakub, diğer kardeş Bünyamin, «kurdun yediği» kayıp kardeş, Yusuf'un içinden gülmesi ve özlemi, yiyecek emri, Yûsuf 12:59 (s16, işaretli), şart ve eşyaya geri konan para. "
          "Basılı her satır bir cümledir; baskının كَنْعَانَ (s3) ve بِنْيَامِينُ (s7) sonrasındaki «!» ve «؟» işaretleri korunmuştur; s5'teki parantez içi dua tırnak değil parantezle dizilmiştir; söyleme fiilleri baskının iki noktasını korur, s11'deki «لَا:» cevap harfinden sonraki baskı iki noktasını korur; baskının âyeti saran parantezleri tırnak olarak okunmuştur.")
write_out(17, S, TITLE, ADD_EN, ADD_TR, "pp. 53–55", GLOSS_ADD)
report(17, S, GLOSS_ADD, ())
