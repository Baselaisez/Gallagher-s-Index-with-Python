# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 20: «إِلَى يَعْقُوبَ» — «أَحْسَنُ الْقَصَصِ» section 21 (print pp. 59–61):
the brothers at a loss, the eldest stays behind (12:81), Yaʿqūb reads the hand of Allah in it, and his trust (12:83).
Every printed line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch20.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "إِلَى يَعْقُوبَ", "en": "To Yaʿqūb", "tr": "Yakub'a"}
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

# ================================================================ §21 إلى يعقوب (pp. 59–61)
sen("s1", "And the brothers were at a loss: how would they return to their father?!", "Kardeşler şaşırıp kaldı: babalarına nasıl dönecekler?!", [
  mazi("وَتَحَيَّرَ", "tahayyara", "«were at a loss»", "«şaşırıp kaldı»", hidden=None, wa=True, tags=["form-v-verbs"]), ikhwa_fail(),
  tok("كَيْفَ", "kayfa", "pron", ["al-istifham", "hal"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — the question noun, as the ḥāl.", "«nasıl» — istifham ismi, hâl."),
  khamsa("يَرْجِعُونَ", "rajaa", "«would they return»", "«dönecekler»"), ila(), abihim(prep="إِلَى", punct="؟!")])
sen("s2", "And the brothers pondered: what would they say to their father?!", "Kardeşler düşündü: babalarına ne diyecekler?!", [
  mazi("وَفَكَّرَ", "fakkara", "«pondered»", "«düşündü»", hidden=None, wa=True, tags=["form-ii-verbs"]), ikhwa_fail(),
  tok("مَاذَا", "ma-istifham", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what» — the question noun as the fronted object.", "«ne» — istifham ismi, öne alınmış mef'ûl."),
  khamsa("يَقُولُونَ", "qala", "«would they say»", "«diyecekler»", tags=["hollow-verbs"]),
  abihim(prep="لِ", punct="؟!.")])
sen("s3", "They had bereaved him yesterday of Yūsuf; will they bereave him today of Binyāmīn!", "Dün onu Yusuf'tan ettiler; bugün de mi Bünyamin'den edecekler!", [
  inna_pron("إِنَّهُمْ", "هُمْ", "pron-3mp", "«indeed they»", "«muhakkak onlar»"),
  mazi_pl_enc("فَجَعُوهُ", "fajaa", "هُ", "pron-3ms", "«bereaved him»", "«onu acıya boğdular»", tags=["inna-wa-akhawatuha"]), amsi()] + name_fi("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", punct="،") + [
  tok("أَفَيَفْجَعُونَهُ", "fajaa", "verb", ["al-istifham", "khuruj-al-istifham", "mudari-marfu", "maful-bihi"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْفَاءُ عَاطِفَةٌ، وَيَفْجَعُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«will they then bereave him?» — the hamza of denial over the fā; a five-verb, its wāw the doer, the hāʾ its object.", "«onu yine mi acıya boğacaklar?» — inkârî istifham hemzesi; ef'âl-i hamseden, vâv fâil, hâ mef'ûl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("فَ", "fa", "conj"), seg("يَفْجَعُونَ", "fajaa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  al_yawm()] + name_fi("بِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin»", punct="!"))
sen("s4", "As for their eldest, he refused to return to Yaʿqūb and said to his brothers:", "En büyükleri ise Yakub'a dönmeyi reddetti ve kardeşlerine dedi:", [
  tok("أَمَّا", "amma", "part", ["amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — the particle of detailing.", "«-e gelince» — tafsil harfi."),
  mudaf_pron("كَبِيرُهُمْ", "kabir", "هُمْ", "pron-3mp", "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "«their eldest»", "«en büyükleri»", tags=["mubtada-khabar", "amma-tafsiliyya"]),
  fa_mazi("فَأَبَى", "aba", "«refused»", "«reddetti»", hidden="هُوَ", tags=["naqis-verbs", "mubtada-khabar"], extra_ar=" — وَالْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  an_(obj_of="أَبَى", en_of="«refused»", tr_of="«reddetti»"), yarjia()] + ila_name("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub»") + [
  qala(full="وَقَالَ", punct=None, wa=True),
  tok("لِإِخْوَتِهِ", "akh", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَإِخْوَةِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his brothers» — in jarr; annexed to the pronoun.", "«kardeşlerine» — mecrur; zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("إِخْوَتِ", "akh", "noun"), seg("هِ", "pron-3ms", "pron")])])
sen("s5", "«Return to your father and say: O our father, your son has stolen, and we testify only to what we knew, and we were not keepers of the unseen.» (Yūsuf 12:81)", "«Babanıza dönün ve deyin: Ey babamız, oğlun çaldı; biz ancak bildiğimize şahitlik ettik ve gaybı bilenler değildik.» (Yûsuf 12:81)", quran([
  amr_pl("ارْجِعُوا", "rajaa", "«return»", "«dönün»"), ila(),
  tok("أَبِيكُمْ", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your father» — jarr by the yāʾ of the five nouns.", "«babanıza» — beş isimden, yâ ile mecrur.", segments=[seg("أَبِي", "ab", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
  amr_pl("فَقُولُوا", "qala", "«and say»", "«ve deyin»", fa=True, tags=["hollow-verbs"])] + ya_abana() + [
  inna(),
  tok("ابْنَكَ", "ibn", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your son» — the ism of inna; annexed to the pronoun.", "«oğlun» — inne'nin ismi; zamire muzâf.", segments=[seg("ابْنَ", "ibn", "noun"), seg("كَ", "pron-2ms", "pron")]),
  mazi("سَرَقَ", "saraqa", "«has stolen»", "«çaldı»", hidden="هُوَ", tags=["inna-wa-akhawatuha"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and not».", "«ve … değil».", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("شَهِدْنَا", "shahida", "verb", [], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا الْفَاعِلِينَ، وَنَا ضَمِيرٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«we testified» — the doers' nā.", "«şahitlik ettik» — fâil nâ'sı.", segments=[seg("شَهِدْ", "shahida", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ حَصْرٍ — اسْتِثْنَاءٌ مُفَرَّغٌ.", "«except» — the restricting illā of the emptied exception.", "«ancak» — müferrağ istisnanın hasr edatı."),
  tok("بِمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِشَهِدْنَا.", "«to what» — the relative mā after bi.", "«bildiğimize» — bâ ve ism-i mevsûl.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("عَلِمْنَا", "alima", "verb", ["ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«we knew» — the relative clause.", "«bildik» — sıla cümlesi.", segments=[seg("عَلِمْ", "alima", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and not».", "«ve … değil».", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("كُنَّا", "kana", "verb", [K, "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا ضَمِيرٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.", "«we were (not)» — kāna with nā as its ism.", "«değildik» — kâne; nâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("لِلْغَيْبِ", "ghayb", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْغَيْبِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِحَافِظِينَ.", "«of the unseen» — in jarr, attached to the khabar.", "«gaybı» — mecrur; haberle ilgili.", segments=[seg("لِ", "li", "prep"), seg("الْغَيْبِ", "ghayb", "noun")]),
  tok("حَافِظِينَ", "hafiz", "noun", [K, "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«keepers» — kāna's khabar, naṣb by the yāʾ of the sound plural.", "«koruyucular» — kâne'nin haberi, cem-i müzekker sâlim, yâ ile mansub.", punct=".")]))
sen("s6", "And when Yaʿqūb heard the story he knew that Allah had a hand in it.", "Yakub hikâyeyi işitince anladı ki bunda Allah'ın bir eli var.", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the lammā of time with its condition.", "«ve … -ınca» — şart manası taşıyan lemmâ.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("سَمِعَ", "samia", "«heard»", "«işitti»", hidden=None), yaqub_fail(), maful("الْقِصَّةَ", "qissa", "«the story»", "«hikâyeyi»"),
  mazi("عَلِمَ", "alima", "«he knew»", "«anladı»", hidden="هُوَ"), anna(obj_of="عَلِمَ"),
  li_al("لِلّٰهِ", "allah", "«Allah has»", "«Allah'ın»", role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ مُقَدَّمٌ"),
  ism_inna_muakhkhar("يَدًا", "yad", "«a hand»", "«bir eli»", part="أَنَّ"), fi(), ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«bunda»", punct=".")])
sen("s7", "And that Allah was testing him.", "Ve Allah'ın onu imtihan etmekte olduğunu.", [
  anna(wa=True, obj_of="عَلِمَ"), allah_ism(part="أَنَّ"),
  mudaf_pron("مُمْتَحِنُهُ", "mumtahin", "هُ", "pron-3ms", "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ", "«is the one testing him»", "«onu imtihan edendir»", tags=["inna-wa-akhawatuha", "ism-fail"], punct=".")])
sen("s8", "Yesterday he was bereaved of Yūsuf and today he is bereaved of Binyāmīn; indeed Allah does not gather two calamities upon him, indeed Allah does not bereave him of two sons.", "Dün Yusuf'tan edildi, bugün Bünyamin'den ediliyor; Allah onun üzerinde iki musibeti toplamaz, Allah onu iki oğuldan etmez.", [
  amsi(), fujia()] + name_fi("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»") + [al_yawm(wa=True), fujia("يُفْجَعُ", mudari=True)] + name_fi("بِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin»") + [
  inna(), allah_ism(), la_nafiya(), mudari("يَجْمَعُ", "jamaa-gather", "«gathers»", "«toplamaz»", hidden="هُوَ", tags=["inna-wa-akhawatuha"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  alayhi("عَلَيْهِ", "هِ", "pron-3ms", "«upon him».", "«onun üzerinde»."),
  tok("مُصِيبَتَيْنِ", "musiba", "noun", ["maful-bihi", "al-muthanna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُثَنًّى.", "«two calamities» — the object, naṣb by the yāʾ of the dual.", "«iki musibeti» — mef'ûl; tesniye, yâ ile mansub.", punct="،"),
  inna(), allah_ism(), la_nafiya(), verb_enc("يَفْجَعُهُ", "fajaa", "هُ", "pron-3ms", "«bereaves him»", "«onu acıya boğmaz»", tags=["inna-wa-akhawatuha"]), fi(),
  tok("ابْنَيْنِ", "ibn", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى.", "«two sons» — jarr by the yāʾ of the dual.", "«iki oğuldan» — tesniye, yâ ile mecrur.", punct=".")])
sen("s9", "Indeed Allah does not bereave him of two sons like Yūsuf and Binyāmīn.", "Allah onu Yusuf ve Bünyamin gibi iki oğuldan etmez.", [
  inna(), allah_ism(), la_nafiya(), verb_enc("يَفْجَعُهُ", "fajaa", "هُ", "pron-3ms", "«bereaves him»", "«onu acıya boğmaz»", tags=["inna-wa-akhawatuha"]), fi(),
  tok("ابْنَيْنِ", "ibn", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى.", "«two sons» — jarr by the yāʾ of the dual.", "«iki oğuldan» — tesniye, yâ ile mecrur."),
  tok("كَيُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf", "naat-sifa"], "الْكَافُ حَرْفُ جَرٍّ، وَيُوسُفَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ — وَشِبْهُ الْجُمْلَةِ نَعْتٌ لِابْنَيْنِ.", "«like Yūsuf» — the kāf of likeness; the phrase describes the two sons.", "«Yusuf gibi» — teşbih kâfı; şibh-i cümle «iki oğul»un sıfatı.", segments=[seg("كَ", "ka", "prep"), seg("يُوسُفَ", "yusuf", "propn")]),
  tok("وَبِنْيَامِينَ", "binyamin", "propn", ["atf-nasaq", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَبِنْيَامِينَ مَعْطُوفٌ عَلَى يُوسُفَ مَجْرُورٌ بِالْفَتْحَةِ.", "«and Binyāmīn» — joined to Yūsuf.", "«ve Bünyamin» — Yusuf'a ma'tûf.", punct=".", segments=wa_("بِنْيَامِينَ", "binyamin", "propn"))])
sen("s10", "Indeed Allah has a hidden hand in that.", "Allah'ın bunda gizli bir eli var.", [
  inna(), li_al("لِلّٰهِ", "allah", "«Allah has»", "«Allah'ın»", role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ مُقَدَّمٌ"), fi(), ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«bunda»"),
  ism_inna_muakhkhar("يَدًا", "yad", "«a hand»", "«bir eli»"), nat_nasb("خَفِيَّةً", "khafi", "«hidden»", "«gizli»", punct=".")])
sen("s11", "Indeed Allah has a concealed wisdom in that.", "Allah'ın bunda saklı bir hikmeti var.", [
  inna(), li_al("لِلّٰهِ", "allah", "«Allah has»", "«Allah'ın»", role="وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ مُقَدَّمٌ"), fi(), ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«bunda»"),
  ism_inna_muakhkhar("حِكْمَةً", "hikma", "«a wisdom»", "«bir hikmeti»"), nat_nasb("مَخْفِيَّةً", "makhfi", "«concealed»", "«saklı»", punct=".")])
sen("s12", "Indeed Allah has not ceased to test His servants, then He gladdens them and bestows His favour upon them", "Allah kullarını imtihan etmeye devam eder, sonra onları sevindirir ve onlara nimet verir", [
  inna(), allah_ism(), lam_jazim(),
  tok("يَزَلْ", "zala", "verb", [K, "lam-jazim", "hollow-verbs", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«has not ceased» — zāla in the jussive after lam; its ism «He» concealed; the clause is inna's khabar.", "«devam eder» — lem ile meczum zâle; ismi gizli «O»; cümle inne'nin haberi."),
  khabar_kana_mudari("يَمْتَحِنُ", "imtahana", "«testing»", "«imtihan etmeye»", tags=["form-viii-verbs"]),
  mudaf_pron("عِبَادَهُ", "abd", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«His servants»", "«kullarını»", tags=["maful-bihi", "jam-taksir"]),
  thumma_(), verb_enc("يَسُرُّهُمْ", "sarra", "هُمْ", "pron-3mp", "«gladdens them»", "«onları sevindirir»", tags=["doubled-verbs", "atf-nasaq"]),
  mudari("وَيُنْعِمُ", "anama", "«and bestows favour»", "«ve nimet verir»", hidden="هُوَ", tags=["form-iv-verbs", "atf-nasaq"], extra_ar=" — وَالْوَاوُ عَاطِفَةٌ"),
  alayhi("عَلَيْهِمْ", "هِمْ", "pron-3mp", "«upon them».", "«onlara».")])
sen("s13", "Then the eldest son stayed in Egypt too, and refused to return to Canaan.", "Sonra büyük oğul da Mısır'da kaldı ve Kenan'a dönmeyi reddetti.", [
  thumma_(atf=False), inna(), ism_inna("الِابْنَ", "ibn", "«the son»", "«oğul»"), nat_nasb("الْكَبِيرَ", "kabir", "«the eldest»", "«büyük»"),
  mazi("بَقِيَ", "baqiya", "«stayed»", "«kaldı»", hidden="هُوَ", tags=["naqis-verbs", "inna-wa-akhawatuha"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ")] + fi_misr() + [aydan(),
  mazi("وَأَبَى", "aba", "«and refused»", "«ve reddetti»", hidden="هُوَ", wa=True, tags=["naqis-verbs"]), an_(obj_of="أَبَى", en_of="«refused»", tr_of="«reddetti»"), yarjia()] + ila_name("كَنْعَانَ", "kanan", "«Canaan»", "«Kenan»", punct="."))
sen("s14", "Is he then to be bereaved of the third as well, when he has already been bereaved of two before?", "Daha önce ikisinden edilmişken üçüncüsünden de mi edilecek?", [
  tok("أَفَيُفْجَعُ", "fajaa", "verb", ["al-istifham", "khuruj-al-istifham", "naib-al-fail", "mudari-marfu"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْفَاءُ عَاطِفَةٌ، وَيُفْجَعُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«is he then to be bereaved?» — the hamza of denial; a passive muḍāriʿ.", "«bir de mi edilecek?» — inkârî hemze; meçhul muzâri.", segments=[seg("أَ", "hamza-istifham", "part"), seg("فَ", "fa", "conj"), seg("يُفْجَعُ", "fajaa", "verb")]),
  fi(), majrur("الثَّالِثِ", "thalith", "«the third»", "«üçüncü»", "فِي"), aydan(),
  tok("وَقَدْ", "qad", "part", ["qad-harf", "hal"], "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ حَالٌ.", "«when already» — the wāw of ḥāl with qad.", "«hâlbuki» — hâl vâvı, tahkik kad'ı.", segments=wa_("قَدْ", "qad", "part")),
  fujia(tags=["hal"]), min_(),
  tok("قَبْلُ", "qabl", "noun", ["huruf-jarr", "al-murab-wal-mabni-wal-irab"], "ظَرْفٌ مَقْطُوعٌ عَنِ الْإِضَافَةِ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ.", "«before» — the zarf cut from its annexation, built on the ḍamma.", "«önce» — izafetten kesilmiş zarf, zamme üzere mebnî."),
  fi(), tok("اثْنَيْنِ", "ithnan", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْيَاءُ — مُلْحَقٌ بِالْمُثَنَّى.", "«two» — jarr by the yāʾ; attached to the dual.", "«ikisinden» — tesniyeye mülhak, yâ ile mecrur.", punct=".")])
sen("s15", "Indeed this will not be.", "Bu olmaz.", [
  inna(), ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»", tags=["inna-wa-akhawatuha"]), la_nafiya(),
  tok("يَكُونُ", "kana", "verb", ["mudari-marfu", "hollow-verbs", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ تَامٌّ (بِمَعْنَى يَحْدُثُ) مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«will (not) be» — the complete kāna, «happen»; the clause is inna's khabar.", "«olmaz» — tam kâne; cümle inne'nin haberi.", punct=".")])
sen("s16", "And here Yaʿqūb was reassured and said:", "Ve burada Yakub huzur buldu ve dedi:", [
  tok("وَهُنَا", "huna", "noun", ["anwa-al-waw", "maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُنَا اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and here» — the place demonstrative as a zarf.", "«ve burada» — mekân işaret ismi, zarf.", segments=wa_("هُنَا", "huna", "noun")),
  mazi("اطْمَأَنَّ", "itmaanna", "«was reassured»", "«huzur buldu»", hidden=None, tags=["doubled-verbs"]), yaqub_fail(), qala(full="وَقَالَ", wa=True)])
sen("s17", "«May Allah bring them all to me; indeed He is the All-Knowing, the All-Wise.» (Yūsuf 12:83)", "«Umulur ki Allah onların hepsini bana getirir; şüphesiz O Alîm'dir, Hakîm'dir.» (Yûsuf 12:83)", quran([
  tok("عَسَى", "asa-hope", "verb", ["naqis-verbs"], "فِعْلٌ مَاضٍ جَامِدٌ مِنْ أَفْعَالِ الرَّجَاءِ، يَعْمَلُ عَمَلَ كَانَ.", "«may it be that» — the frozen verb of hope, working as kāna does.", "«umulur ki» — recâ fiillerinden câmid fiil, kâne gibi amel eder."),
  tok("اللهُ", "allah", "propn", [K], "لَفْظُ الْجَلَالَةِ اسْمُ عَسَى مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — the ism of ʿasā.", "«Allah» — asâ'nın ismi."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", K], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ خَبَرُ عَسَى.", "«that» — the maṣdar particle; the clause is the khabar of ʿasā.", "«-mesi» — masdariyye harfi; te'vilî masdar asâ'nın haberi."),
  tok("يَأْتِيَنِي", "ata", "verb", ["an-masdariyya", "naqis-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«will bring me» — manṣūb after an; the nūn of protection, the yāʾ its object.", "«bana getirir» — en ile mansub; vikaye nûnu, yâ mef'ûl.", segments=[seg("يَأْتِيَ", "ata", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("بِهِمْ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَأْتِيَنِي.", "«them» — bi with the pronoun.", "«onları» — bâ ve zamir.", segments=[seg("بِ", "bi", "prep"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«all together» — the ḥāl.", "«hepsini» — hâl."),
  inna_pron("إِنَّهُ", "هُ", "pron-3ms", "«indeed He»", "«şüphesiz O»"),
  tok("هُوَ", "huwa", "pron", ["tawkid"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«He» — the pronoun of separation.", "«O» — fasıl zamiri."),
  khabar_inna("الْعَلِيمُ", "alim", "«the All-Knowing»", "«Alîm»"), khabar_inna("الْحَكِيمُ", "hakim", "«the All-Wise»", "«Hakîm»", extra=" — خَبَرٌ ثَانٍ")]))

# ---------------------------------------------------------------- glossary
NEW = {
 "fakkara": G("fakkara", "فَكَّرَ", "ف ك ر", "verb", "to think, to ponder (Form II)", "düşünmek (tef'îl bâbı)", 2, form="II"),
 "fajaa": G("fajaa", "فَجَعَ", "ف ج ع", "verb", "to bereave, to afflict with a loss (فَجَعَهُ فِي ابْنِهِ)", "acıya boğmak, (bir yakınından) etmek", 3, form="I"),
 "mumtahin": G("mumtahin", "مُمْتَحِن", "م ح ن", "noun", "one who tests (ism fāʿil of اِمْتَحَنَ)", "imtihan eden (imtehane'nin ism-i fâili)", 3),
 "jamaa-gather": G("jamaa-gather", "جَمَعَ", "ج م ع", "verb", "to gather, to bring together", "toplamak, bir araya getirmek", 2, form="I"),
 "musiba": G("musiba", "مُصِيبَة", "ص و ب", "noun", "a calamity, a misfortune", "musibet, felaket", 2, plural="مَصَائِب"),
 "makhfi": G("makhfi", "مَخْفِيّ", "خ ف ي", "noun", "concealed, hidden (ism mafʿūl of أَخْفَى)", "saklı, gizlenmiş (ahfâ'nın ism-i mef'ûlü)", 2),
 "asa-hope": G("asa-hope", "عَسَى", "ع س ي", "verb", "may it be that, perhaps — the frozen verb of hope (a sister of kāna)", "umulur ki, belki — recâ fiili (kâne'nin kardeşlerinden)", 3),
 "hakim": G("hakim", "حَكِيم", "ح ك م", "noun", "wise, the All-Wise (a name of Allah)", "hikmet sahibi, Hakîm (Allah'ın adı)", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("rajaa", "رجع"), ("aba", "أبى"), ("ams", "أمس"), ("ghayb", "غيب"), ("hafiz", "حافظ"), ("qissa", "قصة"), ("yad", "يد"), ("hikma", "حكمة"), ("khafi", "خفي"), ("zala", "زال"), ("imtahana", "امتحن"), ("abd", "عبد"), ("sarra", "سر"), ("anama", "أنعم"), ("thalith", "ثالث"), ("qabl", "قبل"), ("ithnan", "اثنان"), ("huna", "هنا"), ("itmaanna", "اطمأن"), ("ata", "أتى"), ("jami", "جميع"), ("alim", "عليم"), ("illa", "إلا"), ("ma-mawsula", "ما"), ("ma-nafiya", "ما"), ("shahida", "شهد"), ("thumma", "ثم"), ("ka", "ك"), ("amma", "أما"), ("huwa", "هو")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("fakkara", "fajaa", "jamaa-gather", "asa-hope"): mo["verbs"].pop(_k, None)
put_morph(mo, "asa-hope", {"jamid": True, "bab": "فِعْلٌ مَاضٍ جَامِدٌ مِنْ أَفْعَالِ الرَّجَاءِ", "wazn": "فَعَلَ (نَاقِصٌ يَائِيٌّ)",
  "mazi": ["عَسَى", "عَسَيَا", "عَسَوْا", "عَسَتْ", "عَسَتَا", "عَسَيْنَ", "عَسَيْتَ", "عَسَيْتُمَا", "عَسَيْتُمْ", "عَسَيْتِ", "عَسَيْتُمَا", "عَسَيْتُنَّ", "عَسَيْتُ", "عَسَيْنَا"],
  "note": "جَامِدٌ: لَا مُضَارِعَ لَهُ وَلَا أَمْرَ وَلَا مَصْدَرَ — يُصَرَّفُ فِي الْمَاضِي فَقَطْ، وَيَعْمَلُ عَمَلَ كَانَ: اسْمُهُ مَرْفُوعٌ وَخَبَرُهُ مُضَارِعٌ مَقْرُونٌ بِأَنْ (عَسَى اللهُ أَنْ يَأْتِيَنِي بِهِمْ)."})
put_morph(mo, "fakkara", _sg.derived("مِنْ بَابِ التَّفْعِيلِ", "فَعَّلَ يُفَعِّلُ", "ُ", "فَكَّر", "فَكِّر", "فَكِّر", "تَفْكِير", "مُفَكِّر", "مُفَكَّر", "فُكِّرَ", "يُفَكَّرُ", note="لَازِمٌ غَالِبًا: فَكَّرَ فِي الْأَمْرِ."))
put_morph(mo, "fajaa", _sg.sound1("fataha", "فَجَع", "فْجَع", "اِفْجَع", "فَجْع", "فَاجِع", "مَفْجُوع", "فُجِعَ", "يُفْجَعُ", note="مُتَعَدٍّ: فَجَعَهُ فِي ابْنِهِ — وَيَكْثُرُ مَبْنِيًّا لِلْمَجْهُولِ: فُجِعَ فِيهِ."))
put_morph(mo, "jamaa-gather", _sg.sound1("fataha", "جَمَع", "جْمَع", "اِجْمَع", "جَمْع", "جَامِع", "مَجْمُوع", "جُمِعَ", "يُجْمَعُ", note="مُتَعَدٍّ: جَمَعَ الْمَالَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 20 (print pp. 59–61, «أَحْسَنُ الْقَصَصِ» section 21 «إِلَى يَعْقُوبَ»): the brothers at a loss, the eldest refusing to return with Yūsuf 12:81 (s5, marked), Yaʿqūb reading the hand of Allah in the second loss, "
          "the eldest staying in Egypt, Yaʿqūb's trust in 12:83 (s17, marked). One printed line is one sentence; the print's «؟!» and «!» are kept, s2 keeps the print's «؟!.»; s12 and s17 end as the print does, without a stop; "
          "the print sets its two ayas in round brackets — they are marked here with the guillemets the earlier chapters use.")
ADD_TR = (" Yirminci bölüm (basılı s. 59–61, «أَحْسَنُ الْقَصَصِ» 21. kısım «إِلَى يَعْقُوبَ»): şaşkın kardeşler, dönmeyi reddeden en büyük kardeş ve Yûsuf 12:81 (s5, işaretli), ikinci kayıpta Allah'ın elini gören Yakub, "
          "Mısır'da kalan büyük oğul, Yakub'un 12:83 ile güveni (s17, işaretli). Basılı her satır bir cümledir; baskının «؟!» ve «!» işaretleri korunmuş, s2 baskıdaki «؟!.» ile biter; s12 ve s17 baskıdaki gibi noktasız biter; "
          "baskı iki ayeti yuvarlak parantezle verir — burada önceki bölümlerdeki tırnaklarla işaretlenmiştir.")
write_out(20, S, TITLE, ADD_EN, ADD_TR, "pp. 59–61", GLOSS_ADD)
report(20, S, GLOSS_ADD, ())
