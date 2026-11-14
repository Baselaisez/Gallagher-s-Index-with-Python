# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 19: «بِنْيَامِينُ عِنْدَ يُوسُفَ» — «أَحْسَنُ الْقَصَصِ» section 20 (print pp. 56–59):
Binyāmīn before Yūsuf (12:69), the vessel in the baggage, the exchange with the brothers (12:73–75, 12:77–79) and Binyāmīn kept.
Every printed line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch19.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "بِنْيَامِينُ عِنْدَ يُوسُفَ", "en": "Binyāmīn with Yūsuf", "tr": "Bünyamin Yusuf'un yanında"}
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

# ================================================================ §20 بنيامين عند يوسف (pp. 56–59)
sen("s1", "And the brothers entered by different gates, as their father had ordered them, and reached Yūsuf.", "Kardeşler, babalarının emrettiği gibi ayrı ayrı kapılardan girdiler ve Yusuf'a ulaştılar.", [
  mazi("وَدَخَلَ", "dakhala", "«entered»", "«girdi»", hidden=None, wa=True), ikhwa_fail(),
  min_(), tok("أَبْوَابٍ", "bab", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — جَمْعُ بَابٍ.", "«gates» — in jarr; the plural of بَاب.", "«kapılar» — mecrur; «kapı»nın cem'i."),
  nat_jarr("مُتَفَرِّقَةٍ", "mutafarriq", "«different»", "«ayrı ayrı»", tags=["ism-fail"]),
  tok("كَمَا", "kama", "part", ["huruf-jarr", "ism-mawsul"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ.", "«as» — the kāf of jarr over the maṣdar-mā.", "«gibi» — cer kâfı ve masdariyye mâ.", segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  verb_enc("أَمَرَهُمْ", "amara-v", "هُمْ", "pron-3mp", "«had ordered them»", "«onlara emretmişti»", mudari=False, hidden=None),
  mudaf_pron("أَبُوهُمْ", "ab", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "«their father» — the doer, rafʿ by the wāw of the five nouns", "«babaları» — fâil, beş isimden olduğu için vâv ile merfû", tags=["fail", "five-nouns"]),
  mazi_pl("وَوَصَلُوا", "wasala", "«and reached»", "«ve ulaştılar»", wa=True, tags=["atf-nasaq", "mithal-verbs"]),
  ila(), tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr by a fatḥa: a diptote name.", "«Yusuf'a» — fetha ile mecrur: gayr-i munsarıf.", punct=".")])
sen("s2", "And when Yūsuf saw Binyāmīn he rejoiced greatly, and lodged him in his house.", "Yusuf Bünyamin'i görünce çok sevindi ve onu evine yerleştirdi.", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw", "idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، فِي مَحَلِّ نَصْبٍ.", "«and when» — the resumptive wāw; lammā is a time adverb carrying the sense of a condition.", "«ve …-ince» — istînâf vâvı; lemmâ şart manası taşıyan zaman zarfı.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("رَأَى", "raa", "«saw»", "«gördü»", hidden=None, tags=["naqis-verbs"], extra_ar=" — فِعْلُ الشَّرْطِ"), yusuf_fail(), binyamin_maful(),
  mazi("فَرِحَ", "fariha", "«he rejoiced»", "«sevindi»", hidden="هُوَ", extra_ar=" — جَوَابُ لَمَّا"), jiddan(),
  verb_enc("وَأَنْزَلَهُ", "anzala", "هُ", "pron-3ms", "«and lodged him»", "«ve onu yerleştirdi»", mudari=False, hidden="هُوَ", wa=True, tags=["form-iv-verbs"]),
  fi(), mudaf_pron("بَيْتِهِ", "bayt", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his house» — in jarr", "«evi» — mecrur", tags=["huruf-jarr"], punct=".")])
sen("s3", "And Yūsuf said to Binyāmīn, «Indeed I am your brother,» and Binyāmīn was reassured.", "Yusuf Bünyamin'e «Şüphesiz ben senin kardeşinim» dedi ve Bünyamin huzur buldu.", [
  qala(full="وَقَالَ", wa=True, hidden=None, punct=None), yusuf_fail(),
  li_name("لِبِنْيَامِينَ", "binyamin", "Binyāmīn", "Bünyamin", role="مُتَعَلِّقٌ بِقَالَ"),
  *quran([
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the speaker's yāʾ as its ism.", "«şüphesiz ben» — inne, mütekellim yâsı ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَنَا", "ana", "pron", ["tawkid", "inna-wa-akhawatuha"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ — تَوْكِيدٌ لِاسْمِ إِنَّ (أَوْ ضَمِيرُ فَصْلٍ).", "«I» — the detached pronoun confirming inna's ism (or a pronoun of separation).", "«ben» — inne'nin ismini te'kid eden munfasıl zamir (ya da fasl zamiri)."),
  tok("أَخُوكَ", "akh", "noun", ["inna-wa-akhawatuha", "five-nouns", "idafa-definiteness"], "خَبَرُ إِنَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your brother» — inna's khabar, rafʿ by the wāw of the five nouns.", "«kardeşin» — inne'nin haberi, beş isimden olduğu için vâv ile merfû.", segments=[seg("أَخُو", "akh", "noun"), seg("كَ", "pron-2ms", "pron")])]),
  mazi("وَاطْمَأَنَّ", "itmaanna", "«and … was reassured»", "«ve … huzur buldu»", hidden=None, wa=True), binyamin_fail(punct=".")])
sen("s4", "And Yūsuf met Binyāmīn after a long time, and he remembered his mother and his father, and remembered his house, and remembered his childhood.", "Yusuf Bünyamin'le uzun bir zaman sonra karşılaştı; annesini ve babasını andı, evini andı, çocukluğunu andı.", [
  mazi("وَلَقِيَ", "laqiya", "«met»", "«karşılaştı»", hidden=None, wa=True, tags=["naqis-verbs"]), yusuf_fail(), binyamin_maful(),
  tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«after» — an adverb of time; a muḍāf.", "«sonra» — zaman zarfı; muzâf."),
  mi("زَمَنٍ", "zaman-period", "«a time»", "«zaman»"), nat_jarr("طَوِيلٍ", "tawil-long", "«long»", "«uzun»", tags=["sifa-mushabbaha"]),
  fa_mazi("فَذَكَرَ", "dhakara", "«and he remembered»", "«ve andı»", hidden="هُوَ"),
  mudaf_pron("أُمَّهُ", "umm", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his mother» — the object", "«annesini» — mef'ûl", tags=["maful-bihi"]),
  tok("وَأَبَاهُ", "ab", "noun", ["atf-nasaq", "five-nouns", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَأَبَا مَعْطُوفٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْأَلِفُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his father» — joined, naṣb by the alif of the five nouns.", "«ve babasını» — ma'tûf, beş isimden olduğu için elif ile mansub.", segments=[seg("وَ", "wa", "conj"), seg("أَبَا", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  mazi("وَذَكَرَ", "dhakara", "«and remembered»", "«ve andı»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  mudaf_pron("بَيْتَهُ", "bayt", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his house» — the object", "«evini» — mef'ûl", tags=["maful-bihi"]),
  mazi("وَذَكَرَ", "dhakara", "«and remembered»", "«ve andı»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  mudaf_pron("صِغَرَهُ", "sighar", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his childhood» — the object", "«çocukluğunu» — mef'ûl", tags=["maful-bihi"], punct=".")])
sen("s5", "And Yūsuf wanted Binyāmīn to stay with him, so that he might see him every day and speak with him and ask him about his house.", "Yusuf, Bünyamin'in yanında kalmasını istedi; onu her gün görsün, onunla konuşsun ve ona evini sorsun diye.", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), yusuf_fail(),
  an_("أَرَادَ", "«wanted»", "«istedi»"),
  tok("يَبْقَى", "baqiya", "verb", ["an-masdariyya", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ.", "«(that) … stay» — in naṣb after an, the fatḥa estimated on the alif.", "«kalmasını» — en ile mansub, fethası elif üzerinde takdîrî."),
  indahu(role="مُتَعَلِّقٌ بِيَبْقَى"), binyamin_fail(),
  verb_enc("يَرَاهُ", "raa", "هُ", "pron-3ms", "«he might see him»", "«onu görsün»", hidden="هُوَ", tags=["hal", "naqis-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  tok("كُلَّ", "kull", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (نَابَ عَنِ الظَّرْفِ)، وَهُوَ مُضَافٌ.", "«every» — standing as an adverb of time; a muḍāf.", "«her» — zarf yerine geçen, mansub; muzâf."),
  mi("يَوْمٍ", "yawm", "«day»", "«gün»"),
  verb_enc("وَيُكَلِّمُهُ", "kallama", "هُ", "pron-3ms", "«and speak with him»", "«ve onunla konuşsun»", hidden="هُوَ", wa=True, tags=["form-ii-verbs"]),
  verb_enc("وَيَسْأَلُهُ", "saala", "هُ", "pron-3ms", "«and ask him»", "«ve ona sorsun»", hidden="هُوَ", wa=True),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«hakkında»."),
  mudaf_pron("بَيْتِهِ", "bayt", "هِ", "pron-3ms", "مَجْرُورٌ بِعَنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his house» — in jarr", "«evi» — mecrur", tags=["huruf-jarr"], punct=".")])
sen("s6", "But how was that to be done, when Binyāmīn was returning tomorrow to Canaan?", "Fakat buna nasıl yol bulunur, Bünyamin yarın Kenan'a dönüyorken?", [
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«fakat» — muhaffef lâkin, amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  *kayfa_sabil(wa=False, punct="،"),
  tok("وَبِنْيَامِينُ", "binyamin", "propn", ["anwa-al-waw", "hal", "mubtada-khabar", "mamnu-min-sarf"], "الْوَاوُ حَالِيَّةٌ، وَبِنْيَامِينُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while Binyāmīn» — the wāw of ḥāl; the mubtadaʾ of the ḥāl clause.", "«Bünyamin … iken» — hâl vâvı; hâl cümlesinin mübtedâsı.", segments=wa_("بِنْيَامِينُ", "binyamin", "propn")),
  khabar_raf("رَاجِعٌ", "raji", "«returning»", "«dönen»", tags=["ism-fail"]),
  tok("غَدًا", "ghadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — مُتَعَلِّقٌ بِرَاجِعٌ.", "«tomorrow» — an adverb of time.", "«yarın» — zaman zarfı."),
  ila(), tok("كَنْعَانَ", "kanan", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Canaan» — in jarr by a fatḥa: a foreign diptote name.", "«Kenan'a» — fetha ile mecrur: gayr-i munsarıf.", punct="؟")])
sen("s7", "And how was that to be done, when the brothers had pledged to Allah that they would bring him back with them?", "Ve buna nasıl yol bulunur, kardeşler onu yanlarında geri getireceklerine dair Allah'a söz vermişken?", [
  *kayfa_sabil(),
  tok("وَالْإِخْوَةُ", "akh", "noun", ["anwa-al-waw", "hal", "mubtada-khabar", "jam-taksir"], "الْوَاوُ حَالِيَّةٌ، وَالْإِخْوَةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while the brothers» — the wāw of ḥāl; the mubtadaʾ of the ḥāl clause.", "«kardeşler … iken» — hâl vâvı; hâl cümlesinin mübtedâsı.", segments=wa_("الْإِخْوَةُ", "akh", "noun")),
  mazi_pl("عَاهَدُوا", "ahada", "«had pledged»", "«söz vermişlerdi»", tags=["mubtada-khabar", "form-iii-verbs"]),
  tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — وَجُمْلَةُ عَاهَدُوا فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«Allah» — the object; the verb clause is the khabar.", "«Allah'a» — mef'ûl; fiil cümlesi haberdir."),
  tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«that» — the maṣdar particle; the clause is in the place of jarr after ʿalā.", "«-mek» — masdariyye harfi; te'vilî masdar alâ ile mahallen mecrur."),
  tok("يَرْجِعُوا", "rajaa", "verb", ["an-masdariyya", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«they bring back» — in naṣb after an, the nūn dropped; the wāw its doer.", "«geri dönerler» — en ile mansub, nûnun hazfi ile; vâv fâil."),
  tok("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَرْجِعُوا.", "«with him».", "«onunla».", segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  maa_pron("مَعَهُمْ", "هُمْ", "pron-3mp", "«with them»", "«yanlarında»", role="مُتَعَلِّقٌ بِيَرْجِعُوا", punct="؟")])
sen("s8", "And how could Yūsuf hold Binyāmīn with him without a reason?", "Yusuf Bünyamin'i yanında sebepsiz nasıl alıkoyabilirdi?", [
  tok("وَكَيْفَ", "kayfa", "noun", ["anwa-al-waw", "al-istifham", "hal"], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — the question noun as a ḥāl.", "«ve nasıl» — istifham ismi, hâl.", segments=wa_("كَيْفَ", "kayfa", "noun")),
  tok("يُمْكِنُ", "amkana", "verb", ["mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«is it possible» — a muḍāriʿ whose doer is the an-clause after it.", "«mümkün olur» — fâili sonraki te'vilî masdar olan muzâri."),
  li_name("لِيُوسُفَ", "yusuf", "Yūsuf", "Yusuf", role="مُتَعَلِّقٌ بِيُمْكِنُ"),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "fail"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ فَاعِلُ يُمْكِنُ.", "«that» — the maṣdar particle; the clause is the doer of «is possible».", "«-mesi» — masdariyye harfi; te'vilî masdar «mümkün olur»un fâili."),
  tok("يَحْبِسَ", "habasa", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he hold» — in naṣb after an; «he» concealed.", "«alıkoyması» — en ile mansub; fâil gizli «o»."),
  binyamin_maful(), indahu(role="مُتَعَلِّقٌ بِيَحْبِسَ"),
  *bighayri_sabab(punct="؟", role="مُتَعَلِّقٌ بِيَحْبِسَ")])
sen("s9", "And the people would say: The ʿAzīz has held a Canaanite with him without a reason; indeed this is a great wrong.", "İnsanlar derdi ki: Aziz yanında sebepsiz bir Kenanlıyı alıkoydu; şüphesiz bu büyük bir zulümdür.", [
  tok("وَيَقُولُ", "qala", "verb", ["anwa-al-waw", "mudari-marfu", "hollow-verbs", "maful-bihi"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«and … would say» — a muḍāriʿ in rafʿ; what is said is its object.", "«ve … derdi» — merfû muzâri; söylenen söz mef'ûlüdür.", segments=wa_("يَقُولُ", "qala", "verb")),
  nas_fail(punct=":"),
  qad_(), mazi("حَبَسَ", "habasa", "«has held»", "«alıkoydu»", hidden=None), aziz_fail(), indahu(role="مُتَعَلِّقٌ بِحَبَسَ"),
  tok("كَنْعَانِيًّا", "kanani", "noun", ["maful-bihi", "ism-mansub"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمٌ مَنْسُوبٌ إِلَى كَنْعَانَ.", "«a Canaanite» — the object; a nisba to Canaan.", "«bir Kenanlıyı» — mef'ûl; Kenan'a nispet."),
  *bighayri_sabab(punct="،", role="مُتَعَلِّقٌ بِحَبَسَ"),
  inna(), tok("هٰذَا", "hadha", "pron", ["inna-wa-akhawatuha", "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«this» — the demonstrative as inna's ism.", "«bu» — ism-i işâret, inne'nin ismi."),
  tok("لَظُلْمٌ", "zulm", "noun", ["inna-wa-akhawatuha"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَظُلْمٌ خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«surely a wrong» — the slid lām of emphasis on inna's khabar.", "«elbette bir zulüm» — inne'nin haberi üzerinde te'kid lâmı.", segments=[seg("لَ", "lam-ibtida", "part"), seg("ظُلْمٌ", "zulm", "noun")]),
  nat_raf("عَظِيمٌ", "azim", "«great»", "«büyük»", punct=".")])
sen("s10", "But Yūsuf was keen and wise.", "Fakat Yusuf zeki ve akıllıydı.", [
  wa_lakinna(), name_ism_lakinna("يُوسُفَ"), kana_khabar_lakinna(),
  khabar_kana("ذَكِيًّا", "dhaki", "«keen»", "«zeki»", tags=["sifa-mushabbaha"]), khabar_kana("عَاقِلًا", "aqil", "«wise»", "«akıllı»", second=True, punct=".", tags=["ism-fail"])])
sen("s11", "Yūsuf had a precious vessel, and he used to drink from it.", "Yusuf'un değerli bir kabı vardı ve ondan içerdi.", [
  kana_bare(),
  tok("عِنْدَ", "inda", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«with» — the phrase is kāna's fronted khabar.", "«yanında» — şibh-i cümle kâne'nin mukaddem haberi."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  tok("إِنَاءٌ", "inaa", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a vessel» — kāna's delayed ism.", "«bir kap» — kâne'nin muahhar ismi."),
  nat_raf("ثَمِينٌ", "thamin", "«precious»", "«değerli»", punct="،", tags=["sifa-mushabbaha"]),
  kana_hidden(), khabar_kana_mudari("يَشْرَبُ", "shariba", "«drink»", "«içerdi»"),
  tok("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَشْرَبُ.", "«from it».", "«ondan».", punct=".", segments=[seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")])])
sen("s12", "He put this vessel in Binyāmīn's baggage, and a crier called out: Indeed you are thieves!", "Bu kabı Bünyamin'in eşyasına koydu ve bir tellâl seslendi: Şüphesiz siz hırsızlarsınız!", [
  mazi("وَضَعَ", "wadaa", "«he put»", "«koydu»", hidden="هُوَ", tags=["mithal-verbs"]),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"), badal_("الْإِنَاءَ", "inaa", "nasb", "«vessel»", "«kabı»"),
  fi(), tok("مَتَاعِ", "mata-goods", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the baggage (of)» — in jarr; a muḍāf.", "«eşyası» — mecrur; muzâf."),
  name_mudaf_ilayh("بِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin»"),
  mazi("وَأَذَّنَ", "adhdhana", "«and … called out»", "«ve … seslendi»", hidden=None, wa=True, tags=["atf-nasaq", "form-ii-verbs"]),
  fail("مُؤَذِّنٌ", "muadhdhin", "«a crier»", "«bir tellâl»", tags=["ism-fail"]),
  inna_kum(), la_khabar_pl("لَسَارِقُونَ", "sariq", "«surely thieves»", "«elbette hırsızlar»", punct="!", tags=["ism-fail"])])
sen("s13", "And the brothers turned round and said: What are you missing?", "Kardeşler döndüler ve dediler: Neyi kaybettiniz?", [
  mazi("وَالْتَفَتَ", "iltafata", "«turned round»", "«döndüler»", hidden=None, wa=True, tags=["form-viii-verbs"]), ikhwa_fail(punct="،"),
  qalu(full="وَقَالُوا", wa=True, punct=None, tags=["atf-nasaq"]),
  tok("مَاذَا", "ma-istifham", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what» — the question noun as the fronted object.", "«neyi» — istifham ismi, mukaddem mef'ûl."),
  khamsa("تَفْقِدُونَ", "faqada", "«are you missing»", "«kaybettiniz»", punct="؟")])
sen("s14", "They said: We are missing the king's cup (vessel), and whoever brings it shall have a camel's load.", "Dediler: Kralın su kabını (kabını) kaybettik; onu getirene bir deve yükü var.", [
  qalu_(),
  mudari("نَفْقِدُ", "faqada", "«we are missing»", "«kaybettik»", hidden="نَحْنُ"),
  tok("صُوَاعَ", "suwa", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the cup (of)» — the object; a muḍāf.", "«su kabını» — mef'ûl; muzâf."),
  tok("إِنَاءَ", "inaa", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ مِنْ صُوَاعَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — تَفْسِيرُ الْمُؤَلِّفِ بَيْنَ قَوْسَيْنِ.", "«vessel» — the author's bracketed gloss, read as a badal of «cup».", "«kap» — yazarın parantez içi açıklaması, «su kabı»nın bedeli olarak okunur."),
  mi("الْمَلِكِ", "malik-king", "«the king»", "«kral»", punct="،"),
  tok("وَلِمَنْ", "man", "pron", ["anwa-al-waw", "ism-mawsul", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«and for whoever» — the jarr lām over the relative; the phrase is the fronted khabar.", "«ve her kim …-se ona» — cer lâmı ve mevsûl; şibh-i cümle mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مَنْ", "man", "pron")]),
  mazi("جَاءَ", "jaa", "«brings»", "«getirir»", hidden="هُوَ", tags=["ism-mawsul", "hollow-verbs"], extra_ar=" — صِلَةُ الْمَوْصُولِ"),
  tok("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِجَاءَ.", "«it».", "«onu».", segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("حِمْلُ", "himl", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«a load (of)» — the delayed mubtadaʾ; a muḍāf.", "«yükü» — muahhar mübtedâ; muzâf."),
  mi("بَعِيرٍ", "bair", "«a camel»", "«deve»", punct=".")])
sen("s15", "«They said: By Allah, you know well that we did not come to make mischief in the land, and we are not thieves!» (Yūsuf 12:73)", "«Dediler: Allah'a yemin olsun, siz de bilirsiniz ki biz bu ülkede bozgunculuk etmeye gelmedik ve biz hırsız değiliz!» (Yûsuf 12:73)", quran([
  qalu(punct=None), ta_allah(),
  tok("لَقَدْ", "qad", "part", ["qad-harf"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«indeed» — the lām of the oath's answer over qad.", "«gerçekten» — kasemin cevap lâmı ve tahkik kad'ı.", segments=[seg("لَ", "lam-jawab", "part"), seg("قَدْ", "qad", "part")]),
  tok("عَلِمْتُمْ", "alima", "verb", ["maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — جَوَابُ الْقَسَمِ.", "«you know» — a māḍī on sukūn before the doer's tāʾ; the oath's answer.", "«bildiniz» — fâil tâ'sından önce sükûn üzere mebnî mâzî; kasemin cevabı.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma", "maful-bihi"], "مَا نَافِيَةٌ — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ مَفْعُولُ عَلِمْتُمْ (سَدَّتْ مَسَدَّ الْمَفْعُولَيْنِ).", "«not» — the negating mā; its clause is the object of «you know».", "«-medik» — nefiy mâ'sı; cümlesi «bildiniz»in mef'ûlüdür."),
  tok("جِئْنَا", "jaa", "verb", ["hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — حُذِفَتْ أَلِفُهُ وَكُسِرَ أَوَّلُهُ.", "«we came» — a hollow māḍī before nā, its alif dropped and the first letter given a kasra.", "«geldik» — nâ'dan önce ecvef mâzî; elifi düşmüş, ilk harfi kesreli.", segments=[seg("جِئْ", "jaa", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("لِنُفْسِدَ", "afsada", "verb", ["lam-taleel", "form-iv-verbs"], "اللَّامُ لَامُ التَّعْلِيلِ، وَنُفْسِدَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ.", "«to make mischief» — the lām of purpose; naṣb by a hidden an; «we» concealed.", "«bozgunculuk etmeye» — ta'lîl lâmı; gizli en ile mansub; fâil gizli «biz».", segments=[seg("لِ", "li", "prep"), seg("نُفْسِدَ", "afsada", "verb")]),
  fi(), majrur("الْأَرْضِ", "ard", "«the land»", "«ülke»", "فِي"),
  ma_nafiya_(),
  tok("كُنَّا", "kana", "verb", [K, "hollow-verbs", "anwa-ma"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا اسْمُهَا — أُدْغِمَتْ نُونُ الْفِعْلِ فِي نُونِ الضَّمِيرِ.", "«we were» — kāna before nā, which is its ism; the two nūns assimilated.", "«değildik» — nâ'dan önce kâne; nâ ismi; iki nûn idgam edilmiş.", segments=[seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("سَارِقِينَ", "sariq", "noun", [K, "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«thieves» — kāna's khabar, naṣb by the yāʾ of the sound plural.", "«hırsızlar» — kâne'nin haberi, cem-i müzekker sâlim olduğu için yâ ile mansub.", punct="!")]))
sen("s16", "«They said: Then what shall be his requital, if you are liars?» (Yūsuf 12:74)", "«Dediler: Eğer yalancıysanız onun cezası ne olacak?» (Yûsuf 12:74)", quran([
  qalu(punct=None),
  tok("فَمَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَمَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«then what» — the question noun as mubtadaʾ.", "«o hâlde ne» — istifham ismi, mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-istifham", "pron")]),
  jazauhu("خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ", "«his requital» — the khabar", "«onun cezası» — haber", tags=["mubtada-khabar"]),
  tok("إِنْ", "in-shart", "part", ["idha-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional particle, governing jazm.", "«eğer» — cezm eden şart harfi."),
  tok("كُنْتُمْ", "kana", "verb", [K, "hollow-verbs", "idha-shartiyya"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهَا — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«you are» — kāna as the condition's verb, in the place of jazm; the tāʾ its ism; the answer is understood from what precedes.", "«iseniz» — şart fiili olarak kâne, mahallen meczum; tâ ismi; cevap öncekinden anlaşılır.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("كَاذِبِينَ", "kadhib-liar", "noun", [K, "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«liars» — kāna's khabar, naṣb by the yāʾ of the sound plural.", "«yalancılar» — kâne'nin haberi, yâ ile mansub.", punct="؟")]))
sen("s17", "«They said: His requital is that whoever it is found in whose saddlebag, he himself is its requital; thus we requite the wrongdoers!» (Yūsuf 12:75)", "«Dediler: Onun cezası, kimin yükünde bulunursa işte o onun cezasıdır; biz zalimleri böyle cezalandırırız!» (Yûsuf 12:75)", quran([
  qalu(punct=None),
  jazauhu("مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "«its requital» — the mubtadaʾ", "«onun cezası» — mübtedâ", tags=["mubtada-khabar"]),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ ثَانٍ (أَوْ شَرْطِيَّةٌ) — وَالْجُمْلَةُ مِنَ الْمُبْتَدَأِ الثَّانِي وَخَبَرِهِ خَبَرُ الْأَوَّلِ.", "«whoever» — the relative (or conditional) as a second mubtadaʾ; the clause is the first mubtadaʾ's khabar.", "«her kim» — mevsûl (ya da şart) olarak ikinci mübtedâ; cümle ilk mübtedânın haberi."),
  tok("وُجِدَ", "wajada", "verb", ["ism-mawsul", "naib-al-fail", "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (الصُّوَاعُ) — صِلَةُ الْمَوْصُولِ.", "«it is found» — a passive māḍī with its deputy doer «it» (the cup) concealed; the relative's clause.", "«bulunur» — meçhul mâzî, nâib-i fâil gizli «o» (su kabı); sıla cümlesi."),
  fi(), mudaf_pron("رَحْلِهِ", "rahl", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his saddlebag» — in jarr", "«yükü» — mecrur", tags=["huruf-jarr"]),
  tok("فَهُوَ", "huwa", "pron", ["mubtada-khabar"], "الْفَاءُ زَائِدَةٌ فِي الْخَبَرِ (لِتَضَمُّنِ الْمُبْتَدَأِ مَعْنَى الشَّرْطِ)، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«then he» — the fāʾ added to the khabar because the mubtadaʾ carries a conditional sense; the pronoun a mubtadaʾ.", "«işte o» — mübtedâ şart manası taşıdığı için habere gelen fâ; zamir mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  jazauhu("خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ", "«its requital» — the khabar", "«onun cezası» — haber", tags=["mubtada-khabar"]),
  tok("كَذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "huruf-jarr", "maful-mutlaq"], "الْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ (جَزَاءً كَذٰلِكَ).", "«thus» — the kāf over the demonstrative, describing an omitted maṣdar.", "«böyle» — ism-i işâret üzerinde kâf; hazfedilmiş masdarın sıfatı.", segments=[seg("كَ", "ka", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  mudari("نَجْزِي", "jaza", "«we requite»", "«cezalandırırız»", hidden="نَحْنُ", tags=["naqis-verbs"], extra_ar=" (بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ)"),
  tok("الظَّالِمِينَ", "zalim", "noun", ["maful-bihi", "jam-mudhakkar-salim", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the wrongdoers» — the object, naṣb by the yāʾ of the sound plural.", "«zalimleri» — mef'ûl, yâ ile mansub.", punct="!")]))
sen("s18", "And the vessel came out of Binyāmīn's baggage; so the brothers were ashamed, but said without shame:", "Kap Bünyamin'in eşyasından çıktı; kardeşler utandılar, fakat utanmadan dediler:", [
  mazi("وَخَرَجَ", "kharaja", "«came out»", "«çıktı»", hidden=None, wa=True), fail("الْإِنَاءُ", "inaa", "«the vessel»", "«kap»"),
  min_(), tok("مَتَاعِ", "mata-goods", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the baggage (of)» — in jarr; a muḍāf.", "«eşyası» — mecrur; muzâf."),
  name_mudaf_ilayh("بِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin»"),
  fa_mazi("فَخَجِلَ", "khajila", "«so … were ashamed»", "«böylece … utandı»", hidden=None), ikhwa_fail(),
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«fakat» — muhaffef lâkin, amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  qalu(punct=None),
  min_(), tok("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ — فِي مَحَلِّ نَصْبٍ حَالٌ.", "«without» — in jarr; a muḍāf; the phrase stands as a ḥāl.", "«-sız» — mecrur; muzâf; şibh-i cümle hâldir."),
  mi("خَجَلٍ", "khajal", "«shame»", "«utanma»", punct=":")])
sen("s19", "If (Binyāmīn) steals, then a brother of his (Yūsuf) stole before. (after Yūsuf 12:77)", "(Bünyamin) çalıyorsa, daha önce onun bir kardeşi (Yusuf) çalmıştı. (Yûsuf 12:77'den)", [
  tok("إِنْ", "in-shart", "part", ["idha-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional particle, governing jazm.", "«eğer» — cezm eden şart harfi."),
  tok("يَسْرِقْ", "saraqa", "verb", ["idha-shartiyya"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِإِنْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ — فِعْلُ الشَّرْطِ.", "«steals» — jazm after in; the condition's verb.", "«çalarsa» — in ile meczum; şart fiili."),
  tok("بِنْيَامِينُ", "binyamin", "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ؛ وَالِاسْمُ بَيْنَ قَوْسَيْنِ تَفْسِيرُ الْمُؤَلِّفِ لِلضَّمِيرِ الْمُسْتَتِرِ.", "«Binyāmīn» — the doer; the bracketed name is the author's gloss of the concealed pronoun.", "«Bünyamin» — fâil; parantezli isim yazarın gizli zamiri açıklamasıdır."),
  tok("فَقَدْ", "qad", "part", ["qad-harf", "idha-shartiyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«then indeed» — the fāʾ of the condition's answer over qad.", "«o hâlde gerçekten» — şartın cevap fâsı ve tahkik kad'ı.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("سَرَقَ", "saraqa", "«stole»", "«çaldı»", hidden=None, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ"),
  tok("أَخٌ", "akh", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a brother» — the doer.", "«bir kardeş» — fâil."),
  lahu("لَهُ", "هُ", "pron-3ms", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِأَخٍ.", "«of his» — the phrase describes «a brother».", "«onun» — şibh-i cümle «kardeş»in sıfatı.", tags=["naat-sifa"]),
  tok("يُوسُفُ", "yusuf", "propn", ["badal", "mamnu-min-sarf"], "بَدَلٌ مِنْ أَخٌ مَرْفُوعٌ بِالضَّمَّةِ — تَفْسِيرُ الْمُؤَلِّفِ بَيْنَ قَوْسَيْنِ.", "«Yūsuf» — the author's bracketed gloss, read as a badal of «a brother».", "«Yusuf» — yazarın parantez içi açıklaması, «kardeş»in bedeli olarak okunur."),
  min_(), tok("قَبْلُ", "qabla", "noun", ["huruf-jarr", "al-murab-wal-mabni-wal-irab"], "ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ — لِقَطْعِهِ عَنِ الْإِضَافَةِ.", "«before» — the adverb built on ḍamma when cut from its annex.", "«önce» — izafetten kesilince zamme üzere mebnî zarf.", punct=".")])
S[-1]["tokens"][2]["quoteBefore"] = "("; S[-1]["tokens"][2]["quoteAfter"] = ")"; S[-1]["tokens"][7]["quoteBefore"] = "("; S[-1]["tokens"][7]["quoteAfter"] = ")"
sen("s20", "And Yūsuf heard this slander, and kept silent and was not angry; and Yūsuf was noble and forbearing.", "Yusuf bu iftirayı duydu, sustu ve kızmadı; Yusuf kerim ve halîm idi.", [
  mazi("وَسَمِعَ", "samia", "«heard»", "«duydu»", hidden=None, wa=True), yusuf_fail(),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"), badal_("الْبُهْتَانَ", "buhtan", "nasb", "«slander»", "«iftirayı»"),
  fa_mazi("فَسَكَتَ", "sakata", "«and kept silent»", "«ve sustu»", hidden="هُوَ"),
  lam_jazim(wa=True), tok("يَغْضَبْ", "ghadiba", "verb", ["lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«was (not) angry» — jazm after lam; «he» concealed.", "«kızmadı» — lem ile meczum; fâil gizli «o»."),
  kana(), yusuf_ism_kana(), khabar_kana("كَرِيمًا", "karim", "«noble»", "«kerim»"), khabar_kana("حَلِيمًا", "halim", "«forbearing»", "«halîm»", second=True, punct=".", tags=["sifa-mushabbaha"])])
sen("s21", "«They said: O ʿAzīz, indeed he has a father, an old man of great age; so take one of us in his place — indeed we see you among the doers of good.» (Yūsuf 12:78)", "«Dediler: Ey Aziz, onun çok yaşlı bir babası var; onun yerine birimizi al — şüphesiz biz seni iyilik edenlerden görüyoruz.» (Yûsuf 12:78)", quran([
  qalu(punct=None),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("أَيُّهَا", "ayyuha", "noun", ["vocative-munada"], "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَهَا لِلتَّنْبِيهِ — يُتَوَصَّلُ بِهِ إِلَى نِدَاءِ مَا فِيهِ ال.", "«O (you)» — the vocative built on ḍamma, with the hā of alerting; the bridge to calling a word with ال.", "«ey» — zamme üzere mebnî münâdâ, tenbih hâ'sı ile; harf-i tarifli ismin nidâsına köprü.", segments=[seg("أَيُّ", "ayyuha", "noun"), seg("هَا", "ayyuha", "noun")]),
  tok("الْعَزِيزُ", "aziz", "noun", ["vocative-munada", "naat-sifa"], "نَعْتٌ لِأَيُّ (أَوْ بَدَلٌ) مَرْفُوعٌ بِالضَّمَّةِ تَبَعًا لِلَفْظِ أَيُّ.", "«ʿAzīz» — the naʿt of أَيّ (or its badal), in rafʿ following its form.", "«Aziz» — eyy'in sıfatı (ya da bedeli), lafzına tâbi olarak merfû."),
  inna(), lahu("لَهُ", "هُ", "pron-3ms", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ مُقَدَّمٌ.", "«he has» — the phrase is inna's fronted khabar.", "«onun … var» — şibh-i cümle inne'nin mukaddem haberi.", tags=["inna-wa-akhawatuha"]),
  tok("أَبًا", "ab", "noun", ["inna-wa-akhawatuha", "five-nouns"], "اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ — الْأَسْمَاءُ الْخَمْسَةُ تُعْرَبُ بِالْحَرَكَاتِ إِذَا لَمْ تُضَفْ.", "«a father» — inna's delayed ism; the five nouns decline by vowels when not annexed.", "«bir baba» — inne'nin muahhar ismi; beş isim muzâf olmayınca harekeyle i'rab olunur."),
  nat_nasb("شَيْخًا", "shaykh", "«an old man»", "«yaşlı»"), nat_nasb("كَبِيرًا", "kabir", "«of great age»", "«çok»"),
  tok("فَخُذْ", "akhadha", "verb", ["imperative-amr"], "الْفَاءُ لِلتَّفْرِيعِ، وَخُذْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — حُذِفَتْ هَمْزَتُهُ تَخْفِيفًا.", "«so take» — an imperative on sukūn, its hamza dropped (the light امر of أَخَذَ).", "«öyleyse al» — sükûn üzere mebnî emir, hemzesi hafifletilerek düşmüş.", segments=[seg("فَ", "fa", "conj"), seg("خُذْ", "akhadha", "verb")]),
  mudaf_pron("أَحَدَنَا", "ahad", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«one of us» — the object", "«birimizi» — mef'ûl", tags=["maful-bihi"]),
  mudaf_pron("مَكَانَهُ", "makan", "هُ", "pron-3ms", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ", "«in his place» — an adverb of place", "«onun yerine» — mekân zarfı", tags=["maful-fih"]),
  inna_na(),
  verb_enc("نَرَاكَ", "raa", "كَ", "pron-2ms", "«we see you»", "«seni görüyoruz»", hidden="نَحْنُ", tags=["inna-wa-akhawatuha", "naqis-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  min_(full="مِنَ"), tok("الْمُحْسِنِينَ", "muhsin", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَشِبْهُ الْجُمْلَةِ مَفْعُولٌ ثَانٍ لِنَرَى.", "«the doers of good» — in jarr by the yāʾ of the sound plural; the phrase is the second object of «we see».", "«iyilik edenler» — yâ ile mecrur; şibh-i cümle «görüyoruz»un ikinci mef'ûlü.", punct=".")]))
sen("s22", "«He said: Allah forbid that we should take any but him with whom we found our property; then indeed we would be wrongdoers.» (Yūsuf 12:79)", "«Dedi: Malımızı yanında bulduğumuz kimseden başkasını almaktan Allah'a sığınırız; o zaman biz elbette zalimler oluruz.» (Yûsuf 12:79)", quran([
  qala(punct=None, hidden="هُوَ"),
  tok("مَعَاذَ", "maadh", "noun", ["maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ لِفِعْلٍ مَحْذُوفٍ (نَعُوذُ)، وَهُوَ مُضَافٌ.", "«(we take) refuge» — the absolute object of an omitted verb; a muḍāf.", "«sığınırız» — hazfedilmiş fiilin mef'ûl-i mutlakı; muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِمِنْ مَحْذُوفَةٍ (مِنْ أَنْ نَأْخُذَ).", "«that» — the maṣdar particle; the clause is governed by an omitted «from».", "«-mekten» — masdariyye harfi; te'vilî masdar hazfedilmiş «min» ile mecrur."),
  tok("نَأْخُذَ", "akhadha", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ.", "«we take» — in naṣb after an; «we» concealed.", "«alalım» — en ile mansub; fâil gizli «biz»."),
  tok("إِلَّا", "illa", "part", ["qasr", "istithna"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except» — the restricting illā of a voided exception.", "«-den başka» — hasr edatı (müferrağ istisna)."),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«him whom» — the relative, as object.", "«kimse ki» — ism-i mevsûl, mef'ûl."),
  tok("وَجَدْنَا", "wajada", "verb", ["ism-mawsul", "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — صِلَةُ الْمَوْصُولِ.", "«we found» — a māḍī before nā, the doer «we»; the relative's clause.", "«bulduk» — nâ'dan önce sükûn üzere mebnî mâzî; nâ fâil; sıla cümlesi.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("نَا", "pron-1p", "pron")]),
  mudaf_pron("مَتَاعَنَا", "mata-goods", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«our property» — the object", "«malımızı» — mef'ûl", tags=["maful-bihi"]),
  indahu(role="مُتَعَلِّقٌ بِوَجَدْنَا، وَالْهَاءُ هِيَ الْعَائِدُ"),
  inna_na(),
  tok("إِذًا", "idhan", "part", [], "حَرْفُ جَوَابٍ وَجَزَاءٍ مُهْمَلٌ (لَمْ يَلِهِ فِعْلٌ مُضَارِعٌ).", "«then» — the answer particle, here governing nothing.", "«o zaman» — cevap harfi, burada amel etmez."),
  la_khabar_pl("لَظَالِمُونَ", "zalim", "«surely wrongdoers»", "«elbette zalimler»", punct=".", tags=["ism-fail"])]))
sen("s23", "And so Binyāmīn stayed with Yūsuf, and the two brothers rejoiced together.", "Böylece Bünyamin Yusuf'un yanında kaldı ve iki kardeş birlikte sevindi.", [
  tok("وَهٰكَذَا", "hakadha", "pron", ["anwa-al-waw", "asma-al-ishara", "maful-mutlaq"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰكَذَا فِي مَحَلِّ نَصْبٍ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ (بَقَاءً هٰكَذَا).", "«and so» — the demonstrative compound, describing an omitted maṣdar.", "«ve böylece» — işaret bileşiği, hazfedilmiş masdarın sıfatı.", segments=wa_("هٰكَذَا", "hakadha", "pron")),
  mazi("بَقِيَ", "baqiya", "«stayed»", "«kaldı»", hidden=None, tags=["naqis-verbs"]), binyamin_fail(),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with» — an adverb of place; a muḍāf.", "«yanında» — mekân zarfı; muzâf."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  mazi("وَفَرِحَ", "fariha", "«and rejoiced»", "«ve sevindi»", hidden=None, wa=True, tags=["atf-nasaq"]),
  tok("الْأَخَوَانِ", "akh", "noun", ["fail", "al-muthanna", "five-nouns"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى — مُثَنَّى أَخٍ تُرَدُّ إِلَيْهِ وَاوُهُ.", "«the two brothers» — the doer; the dual's rafʿ shows as an alif, and أَخ takes its wāw back in the dual.", "«iki kardeş» — fâil; tesniyenin ref'i elifle; tesniyede «ah»ın vâvı geri gelir."),
  tok("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«together» — the ḥāl.", "«birlikte» — hâl.", punct=".")])
sen("s24", "Indeed Yūsuf had been alone for a long time, seeing no one of his family.", "Şüphesiz Yusuf uzun zamandır yalnızdı; ailesinden kimseyi görmüyordu.", [
  inna(), ism_inna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", tags=["mamnu-min-sarf"], extra=" — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ"),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs", "inna-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«had been» — kāna with «he» concealed; the clause is inna's khabar.", "«idi» — kâne, ismi gizli «o»; cümle inne'nin haberi."),
  khabar_kana("وَحِيدًا", "wahid-alone", "«alone»", "«yalnız»", tags=["sifa-mushabbaha"]),
  tok("مُنْذُ", "mundhu", "noun", ["huruf-jarr", "huruf-jarr-nawadir"], "حَرْفُ جَرٍّ (لِابْتِدَاءِ الْغَايَةِ فِي الزَّمَانِ).", "«since, for» — the jarr letter of a time's beginning.", "«-den beri» — zamanda başlangıç cer harfi."),
  majrur("زَمَنٍ", "zaman-period", "«a time»", "«zaman»", "مُنْذُ"), nat_jarr("طَوِيلٍ", "tawil-long", "«long»", "«uzun»", tags=["sifa-mushabbaha"]),
  la_nafiya(), neg_mudari("يَرَى", "raa", "«seeing»", "«görüyordu»", hidden="هُوَ", tags=["hal", "naqis-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  maful("أَحَدًا", "ahad", "«anyone»", "«kimseyi»"),
  min_(), mudaf_pron("أَهْلِهِ", "ahl", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his family» — in jarr", "«ailesi» — mecrur", tags=["huruf-jarr"], punct=".")])
sen("s25", "And Allah had driven Binyāmīn to him — should he not keep him with him, to see him and speak with him?", "Allah Bünyamin'i ona sürüklemişti — onu yanında tutup görmesin ve onunla konuşmasın mı?", [
  tok("وَقَدْ", "qad", "part", ["anwa-al-waw", "qad-harf"], "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — the wāw of ḥāl over qad.", "«hâlbuki» — hâl vâvı ve tahkik kad'ı.", segments=wa_("قَدْ", "qad", "part")),
  mazi("سَاقَ", "saqa", "«had driven»", "«sürüklemişti»", hidden=None, tags=["hollow-verbs"]), allah_fail(),
  tok("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِسَاقَ.", "«to him».", "«ona».", segments=[seg("إِلَيْ", "ila", "prep"), seg("هِ", "pron-3ms", "pron")]),
  binyamin_maful(),
  tok("أَفَلَا", "hamza-istifham", "part", ["al-istifham", "khuruj-al-istifham", "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«should … not?» — the question hamza over the fāʾ and the negating lā.", "«… -masın mı?» — inkârî istifham hemzesi, fâ ve nefiy lâ'sı.", segments=[seg("أَ", "hamza-istifham", "part"), seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  verb_enc("يَحْبِسُهُ", "habasa", "هُ", "pron-3ms", "«keep him»", "«onu tutsun»", hidden="هُوَ", tags=["la-nafiya"]),
  indahu(role="مُتَعَلِّقٌ بِيَحْبِسُ"),
  verb_enc("يَرَاهُ", "raa", "هُ", "pron-3ms", "«to see him»", "«onu görsün»", hidden="هُوَ", tags=["hal", "naqis-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  verb_enc("وَيُكَلِّمُهُ", "kallama", "هُ", "pron-3ms", "«and speak with him»", "«ve onunla konuşsun»", hidden="هُوَ", wa=True, tags=["form-ii-verbs"], punct=".")])
sen("s26", "And is it a wrong that a brother should stay with his brother?", "Bir kardeşin kardeşinin yanında kalması zulüm müdür?", [
  tok("وَهَلْ", "hal-istifham", "part", ["anwa-al-waw", "al-istifham", "khuruj-al-istifham"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهَلْ حَرْفُ اسْتِفْهَامٍ إِنْكَارِيٍّ.", "«and is…?» — the question particle meaning denial.", "«ve … mi?» — inkârî istifham harfi.", segments=wa_("هَلْ", "hal-istifham", "part")),
  min_(full="مِنَ"), tok("الظُّلْمِ", "zulm", "noun", ["huruf-jarr", "mubtada-khabar"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«a wrong» — in jarr; the phrase is the fronted khabar.", "«zulüm» — mecrur; şibh-i cümle mukaddem haber."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that» — the maṣdar particle; the clause is the delayed mubtadaʾ.", "«-ması» — masdariyye harfi; te'vilî masdar muahhar mübtedâ."),
  tok("يُقِيمَ", "aqama", "verb", ["an-masdariyya", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«should stay» — in naṣb after an.", "«kalması» — en ile mansub."),
  tok("أَخٌ", "akh", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a brother» — the doer.", "«bir kardeş» — fâil."),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with» — an adverb of place; a muḍāf.", "«yanında» — mekân zarfı; muzâf."),
  akh_five("أَخِيهِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ", "جَرِّهِ الْيَاءُ", "«his brother» — the muḍāf ilayh", "«kardeşi» — muzâfun ileyh", punct=".")])
sen("s27", "Never! Never!", "Asla! Asla!", [
  tok("أَبَدًا", "abadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ لِفِعْلٍ مَحْذُوفٍ (لَيْسَ ذٰلِكَ ظُلْمًا أَبَدًا).", "«never» — an adverb of time for an omitted clause.", "«asla» — hazfedilmiş cümlenin zaman zarfı.", punct="!"),
  tok("أَبَدًا", "abadan", "noun", ["maful-fih", "tawkid"], "تَوْكِيدٌ لَفْظِيٌّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«never» — a verbal emphasis by repetition.", "«asla» — tekrarla lafzî te'kid.", punct="!")])

# ---------------------------------------------------------------- glossary
NEW = {
 "zaman-period": G("zaman-period", "زَمَن", "ز م ن", "noun", "a time, a period", "zaman, süre", 2, plural="أَزْمَان"),
 "sighar": G("sighar", "صِغَر", "ص غ ر", "noun", "childhood, smallness (maṣdar of صَغُرَ)", "çocukluk, küçüklük (sağura'nın masdarı)", 2),
 "ghadan": G("ghadan", "غَدًا", "غ د و", "noun", "tomorrow (an adverb of time)", "yarın (zaman zarfı)", 1),
 "habasa": G("habasa", "حَبَسَ", "ح ب س", "verb", "to hold back, to detain", "alıkoymak, hapsetmek", 2, form="I"),
 "kanani": G("kanani", "كَنْعَانِيّ", None, "noun", "a Canaanite (a nisba to كَنْعَان)", "Kenanlı (Kenan'a nispet)", 2),
 "thamin": G("thamin", "ثَمِين", "ث م ن", "noun", "precious, costly (ṣifa mushabbaha)", "değerli, kıymetli (sıfat-ı müşebbehe)", 2),
 "adhdhana": G("adhdhana", "أَذَّنَ", "أ ذ ن", "verb", "to call out, to proclaim (Form II)", "seslenmek, ilan etmek (tef'îl bâbı)", 2, form="II"),
 "muadhdhin": G("muadhdhin", "مُؤَذِّن", "أ ذ ن", "noun", "a crier, a proclaimer (ism fāʿil of أَذَّنَ)", "tellâl, seslenen (ezzene'nin ism-i fâili)", 2),
 "iltafata": G("iltafata", "اِلْتَفَتَ", "ل ف ت", "verb", "to turn round, to turn toward", "dönmek, bakmak", 3, form="VIII"),
 "faqada": G("faqada", "فَقَدَ", "ف ق د", "verb", "to miss, to lose", "kaybetmek, yitirmek", 2, form="I"),
 "suwa": G("suwa", "صُوَاع", "ص و ع", "noun", "the king's drinking cup, a measure", "kralın su kabı, ölçek", 3),
 "himl": G("himl", "حِمْل", "ح م ل", "noun", "a load (that is carried)", "yük", 2, plural="أَحْمَال"),
 "bair": G("bair", "بَعِير", "ب ع ر", "noun", "a camel", "deve", 1, plural="أَبْعِرَة"),
 "ta-qasam": G("ta-qasam", "تَـ (الْقَسَم)", None, "prep", "the tāʾ of the oath — a jarr letter that enters only on the name of Allah", "kasem tâ'sı — yalnız Allah lafzına gelen cer harfi", 3),
 "khajal": G("khajal", "خَجَل", "خ ج ل", "noun", "shame, embarrassment (maṣdar of خَجِلَ)", "utanma, mahcubiyet (hacile'nin masdarı)", 2),
 "saraqa": G("saraqa", "سَرَقَ", "س ر ق", "verb", "to steal", "çalmak", 1, form="I"),
 "buhtan": G("buhtan", "بُهْتَان", "ب ه ت", "noun", "a slander, a false accusation", "iftira, bühtan", 3),
 "muhsin": G("muhsin", "مُحْسِن", "ح س ن", "noun", "a doer of good (ism fāʿil of أَحْسَنَ)", "iyilik eden (ahsene'nin ism-i fâili)", 2, plural="مُحْسِنُونَ"),
 "maadh": G("maadh", "مَعَاذ", "ع و ذ", "noun", "refuge (a maṣdar: مَعَاذَ اللهِ = we take refuge in Allah)", "sığınma (masdar: مَعَاذَ اللهِ = Allah'a sığınırız)", 3),
 "mundhu": G("mundhu", "مُنْذُ", None, "prep", "since, for (a time) — a jarr letter", "-den beri (zaman) — cer harfi", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("anzala", "أنزل"), ("tawil-long", "طويل"), ("sabil", "سبيل"), ("raji", "راجع"), ("amkana", "أمكن"), ("sabab", "سبب"), ("zulm", "ظلم"), ("inaa", "إناء"), ("sariq", "سارق"), ("afsada", "أفسد"), ("jaza", "جزى"), ("rahl", "رحل"), ("ayyuha", "أي"), ("ghayr", "غير"), ("saqa", "ساق"), ("aqama", "أقام"), ("wasala", "وصل"), ("ma-istifham", "ما"), ("idhan", "إذا"), ("umm", "أم"), ("shaykh", "شيخ"), ("abadan", "أبدا"), ("jami", "جميع"), ("wahid-alone", "وحيد")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("habasa", "adhdhana", "iltafata", "faqada", "saraqa"): mo["verbs"].pop(_k, None)
put_morph(mo, "habasa", _sg.sound1("daraba", "حَبَس", "حْبِس", "اِحْبِس", "حَبْس", "حَابِس", "مَحْبُوس", "حُبِسَ", "يُحْبَسُ", note="مُتَعَدٍّ: حَبَسَهُ عِنْدَهُ."))
put_morph(mo, "adhdhana", _sg.derived("مِنْ بَابِ التَّفْعِيلِ — مَهْمُوزُ الْفَاءِ", "فَعَّلَ يُفَعِّلُ", "ُ", "أَذَّن", "ؤَذِّن", "أَذِّن", "تَأْذِين", "مُؤَذِّن", "مُؤَذَّن", "أُذِّنَ", "يُؤَذَّنُ", note="لَازِمٌ وَمُتَعَدٍّ: أَذَّنَ مُؤَذِّنٌ، أَذَّنَ بِالصَّلَاةِ — الْهَمْزَةُ تُرْسَمُ عَلَى وَاوٍ بَعْدَ الضَّمَّةِ (يُؤَذِّنُ)."))
put_morph(mo, "iltafata", _sg.idgham(_sg.derived("مِنْ بَابِ الِافْتِعَالِ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِلْتَفَت", "لْتَفِت", "اِلْتَفِت", "اِلْتِفَات", "مُلْتَفِت", "مُلْتَفَت (إِلَيْهِ)", "اُلْتُفِتَ", "يُلْتَفَتُ", note="لَازِمٌ، يَتَعَدَّى بِإِلَى: اِلْتَفَتَ إِلَيْهِ.")))
put_morph(mo, "faqada", _sg.sound1("daraba", "فَقَد", "فْقِد", "اِفْقِد", "فَقْد", "فَاقِد", "مَفْقُود", "فُقِدَ", "يُفْقَدُ", note="مُتَعَدٍّ: فَقَدَ الشَّيْءَ."))
put_morph(mo, "saraqa", _sg.sound1("daraba", "سَرَق", "سْرِق", "اِسْرِق", "سَرِقَة", "سَارِق", "مَسْرُوق", "سُرِقَ", "يُسْرَقُ", note="مُتَعَدٍّ: سَرَقَ الْمَالَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 19 (print pp. 56–59, «أَحْسَنُ الْقَصَصِ» section 20 «بِنْيَامِينُ عِنْدَ يُوسُفَ»): the entry by different gates, Yūsuf and Binyāmīn with 12:69 (s3, marked), Yūsuf's longing and the three questions of the way, the vessel in the baggage, the crier, the exchange with the brothers in 12:73–75 (s15, s16, s17, marked), the slander after 12:77 (s19 — the print sets it WITHOUT parentheses and with the two names bracketed as the author's glosses, so it is not marked), the plea and the answer, 12:78–79 (s21, s22, marked), and Binyāmīn kept. "
          "One printed line is one sentence except s5 (joined across pp. 56–57); the print's «!» and «؟» are kept, s27 keeps both; s14's bracketed إِنَاءَ is the print's gloss of صُوَاعَ, read as a badal; the saying verbs keep the print's colon, s18 takes the print's; the print's parentheses around the ayas are read as quotation marks.")
ADD_TR = (" On dokuzuncu bölüm (basılı s. 56–59, «أَحْسَنُ الْقَصَصِ» 20. kısım «بِنْيَامِينُ عِنْدَ يُوسُفَ»): ayrı kapılardan giriş, Yusuf ile Bünyamin 12:69 ile (s3, işaretli), Yusuf'un özlemi ve yolun üç sorusu, eşyadaki kap, tellâl, kardeşlerle 12:73–75'teki konuşma (s15, s16, s17, işaretli), 12:77'den sonraki iftira (s19 — baskı onu parantezSİZ ve iki ismi yazarın açıklaması olarak parantezli dizer, bu yüzden işaretlenmemiştir), rica ve cevap 12:78–79 (s21, s22, işaretli) ve alıkonan Bünyamin. "
          "Basılı her satır bir cümledir; s5 s. 56–57 arasında birleştirilmiştir; baskının «!» ve «؟» işaretleri korunmuş, s27 her ikisini de taşır; s14'teki parantezli إِنَاءَ baskının صُوَاعَ açıklamasıdır, bedel olarak okunmuştur; söyleme fiilleri baskının iki noktasını korur, s18 baskınınkini alır; baskının âyetleri saran parantezleri tırnak olarak okunmuştur.")
write_out(19, S, TITLE, ADD_EN, ADD_TR, "pp. 56–59", GLOSS_ADD)
report(19, S, GLOSS_ADD, ())
