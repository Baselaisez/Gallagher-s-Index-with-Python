# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 9: «وَفْدٌ إِلَى يَعْقُوبَ، وَإِلَى الْغَابَةِ» — «أَحْسَنُ الْقَصَصِ» sections 3–4 (print pp. 30–34):
the brothers' delegation to Yaʿqūb, Yūsuf 12:12 and 12:13 as the print sets them (marked), the leave given; the forest, the well,
the glad tidings in the well, the brothers' council and the ram's blood on the shirt. Every printed line is one sentence, split at
the print's own full stops; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch9.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "وَفْدٌ إِلَى يَعْقُوبَ، وَإِلَى الْغَابَةِ", "en": "A delegation to Yaʿqūb, and to the forest", "tr": "Yakub'a bir heyet, ve ormana"}
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
def min_(punct=None): return tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from, of».", "«-den».", punct=punct)
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

# ================================================================ §3 وفد إلى يعقوب (pp. 30–32)
sen("s1", "And when they had agreed on this plan, they came to Yaʿqūb.", "Bu görüşte anlaşınca Yakub'a geldiler.", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw", "maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«and when» — a time-word built; in the place of naṣb.", "«ve … -ınca» — «hîne» mânâsında zarf, mebnî; mahallen mansub.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi_pl("اتَّفَقُوا", "ittafaqa", "«they agreed»", "«anlaştılar»", tags=["form-viii-verbs"]), ala(),
  ishara("هٰذَا", "hadha", "jarr", "«this»", "«bu»"),
  tok("الرَّأْيِ", "ray", "noun", ["badal", "huruf-jarr"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«plan, opinion» — the badal of the demonstrative, in jarr.", "«görüş» — ism-i işâretin bedeli, mecrur."),
  tok("جَاؤُوا", "jaa", "verb", [], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ جَوَابُ لَمَّا.", "«they came» — a māḍī with the group's wāw as doer; the answer of «when».", "«geldiler» — cemi vâvı fâil; «-ınca»nın cevabı."),
  ila(), tok("يَعْقُوبَ", "yaqub", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yaʿqūb» — in jarr by a fatḥa; a diptote name.", "«Yakub» — fetha ile mecrur; gayr-i munsarıf.", punct=".")])
sen("s2", "And Yaʿqūb feared greatly for Yūsuf, and he knew that the brothers envied him and did not love him.", "Yakub Yusuf için çok korkuyordu ve kardeşlerin onu kıskandığını ve sevmediğini biliyordu.", [
  kana(), yaqub_ism_kana(), khabar_kana_mudari("يَخَافُ", "khafa", "«feared»", "«korkuyordu»", tags=["hollow-verbs"]), ala(),
  tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr by a fatḥa; a diptote.", "«Yusuf» — fetha ile mecrur; gayr-i munsarıf."),
  kathiran(punct="،"),
  kana_hidden(), khabar_kana_mudari("يَعْرِفُ", "arafa", "«knew»", "«biliyordu»"),
  anna(obj_of="يَعْرِفُ"), ikhwa("الْإِخْوَةَ", "nasb", "اسْمُ أَنَّ", "«the brothers» — the ism of anna", "«kardeşler» — enne'nin ismi", tags=["inna-wa-akhawatuha"]),
  khamsa_enc("يَحْسُدُونَهُ", "hasada", "هُ", "pron-3ms", "«envied him»", "«onu kıskanıyorlardı»", tags=["inna-wa-akhawatuha"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  la_nafiya(wa=True), khamsa_enc("يُحِبُّونَهُ", "ahabba", "هُ", "pron-3ms", "«love him»", "«onu sevmiyorlardı»", tags=["atf-nasaq", "form-iv-verbs"], punct=".")])
sen("s3", "And Yaʿqūb would not send Yūsuf with the brothers.", "Yakub Yusuf'u kardeşlerle göndermezdi.", [
  kana(), yaqub_ism_kana(), la_nafiya(), khabar_kana_mudari("يُرْسِلُ", "arsala", "«would send»", "«gönderirdi»", tags=["la-nafiya", "form-iv-verbs"]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), maa_(), ikhwa("الْإِخْوَةِ", "jarr", "مُضَافٌ إِلَيْهِ", "«the brothers» — the muḍāf ilayh", "«kardeşler» — muzâfun ileyh", punct=".")])
sen("s4", "And Yūsuf would play with his brother and not go far.", "Yusuf kardeşiyle oynar ve uzağa gitmezdi.", [
  kana(), yusuf_ism_kana(), khabar_kana_mudari("يَلْعَبُ", "laiba", "«would play»", "«oynardı»"), maa_(),
  tok("أَخِيهِ", "akh", "noun", ["five-nouns", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his brother» — the muḍāf ilayh, jarr by the yāʾ of the five nouns; itself annexed to the pronoun.", "«kardeşi» — muzâfun ileyh, beş isimden olduğu için yâ ile mecrur; zamire muzâf.", segments=[seg("أَخِي", "akh", "noun"), seg("هِ", "pron-3ms", "pron")]),
  la_nafiya(wa=True), mudari("يَذْهَبُ", "dhahaba", "«go»", "«gitmezdi»", tags=["atf-nasaq", "la-nafiya"]),
  tok("بَعِيدًا", "baid", "noun", ["maful-fih"], "مَفْعُولٌ فِيهِ (ظَرْفُ مَكَانٍ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«far» — an adverb of place, in naṣb.", "«uzağa» — mekân zarfı, mansub.", punct=".")])
sen("s5", "And the brothers knew that, but they had resolved on evil.", "Kardeşler bunu biliyorlardı; fakat kötülüğe karar vermişlerdi.", [
  kana(), ikhwa("الْإِخْوَةُ", "raf", "اسْمُ كَانَ", "«the brothers» — kāna's ism", "«kardeşler» — kâne'nin ismi", tags=[K]),
  khamsa("يَعْرِفُونَ", "arafa", "«knew»", "«biliyorlardı»", tags=[K], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  ishara("ذٰلِكَ", "dhalika", "nasb", "«that»", "«bunu»", punct="،"),
  tok("وَلٰكِنَّهُمْ", "lakinna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«but they» — lākinna with the attached pronoun as its ism.", "«fakat onlar» — lâkinne; bitişik zamir ismidir.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  mazi_pl("عَزَمُوا", "azama", "«had resolved»", "«karar vermişlerdi»", tags=["inna-wa-akhawatuha"]), ala(),
  majrur("الشَّرِّ", "sharr", "«evil»", "«kötülük»", "عَلَى", punct=".")])
sen("s6", "They said: O our father, why do you not send Yūsuf with us?", "Dediler: Ey babamız, Yusuf'u neden bizimle göndermiyorsun?", [
  qalu(punct=None), *ya_abana(),
  tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَذَا زَائِدَةٌ — مُتَعَلِّقٌ بِتُرْسِلُ.", "«why» — the jarr lām on the question-mā.", "«neden» — cer lâmı istifham mâ'sında."),
  la_nafiya(), mudari("تُرْسِلُ", "arsala", "«do you send»", "«gönderiyorsun»", hidden="أَنْتَ", tags=["la-nafiya", "form-iv-verbs"]),
  maa_pron("مَعَنَا", "نَا", "pron-1p", "«with us»", "«bizimle»"), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»", punct="؟")])
sen("s7", "What do you fear?", "Neden korkuyorsun?", [
  tok("مَاذَا", "madha", "pron", ["al-istifham"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what» — the question noun, built; the fronted object.", "«ne» — istifham ismi, mebnî; öne alınmış mef'ûl."),
  mudari("تَخَافُ", "khafa", "«do you fear»", "«korkuyorsun»", hidden="أَنْتَ", tags=["hollow-verbs"], punct="؟")])
sen("s8", "He is our dear brother, and our little brother, and we are the sons of one father.", "O bizim sevgili kardeşimiz, küçük kardeşimizdir; biz bir babanın oğullarıyız.", [
  tok("هُوَ", "pron-3ms-munfasil", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«he» — the mubtadaʾ.", "«o» — mübtedâ."),
  tok("أَخُونَا", "akh", "noun", ["mubtada-khabar", "five-nouns", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَنَا مُضَافٌ إِلَيْهِ.", "«our brother» — the khabar, rafʿ by the wāw of the five nouns.", "«kardeşimiz» — haber, beş isimden olduğu için vâv ile merfû.", segments=[seg("أَخُو", "akh", "noun"), seg("نَا", "pron-1p", "pron")]),
  nat_raf("الْعَزِيزُ", "aziz", "«dear»", "«sevgili»", punct="،"),
  tok("وَأَخُونَا", "akh", "noun", ["atf-nasaq", "five-nouns", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَأَخُونَا مَعْطُوفٌ عَلَى الْخَبَرِ مَرْفُوعٌ بِالْوَاوِ، وَنَا مُضَافٌ إِلَيْهِ.", "«and our brother» — joined to the khabar, rafʿ by the wāw.", "«ve kardeşimiz» — habere atıf, vâv ile merfû.", segments=[seg("وَ", "wa", "conj"), seg("أَخُو", "akh", "noun"), seg("نَا", "pron-1p", "pron")]),
  nat_raf("الصَّغِيرُ", "saghir", "«little»", "«küçük»", punct="،"),
  tok("وَنَحْنُ", "nahnu", "pron", ["atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَنَحْنُ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and we» — the mubtadaʾ of a joined clause.", "«ve biz» — atfedilen cümlenin mübtedâsı.", segments=[seg("وَ", "wa", "conj"), seg("نَحْنُ", "nahnu", "pron")]),
  tok("أَبْنَاءُ", "ibn", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ — جَمْعُ تَكْسِيرٍ.", "«the sons (of)» — the khabar; a muḍāf; a broken plural.", "«oğulları» — haber; muzâf; cem-i mükesser."),
  tok("أَبٍ", "ab", "noun", ["idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَلٰكِنَّهُ غَيْرُ مُضَافٍ فَيُعْرَبُ بِالْحَرَكَةِ.", "«of one father» — the muḍāf ilayh, jarr by a kasra: a five-noun NOT annexed declines by the vowel.", "«bir babanın» — muzâfun ileyh, kesre ile mecrur: muzâf olmayan beş isim harekeyle i'râb olunur.", punct=".")])
sen("s9", "Brothers always play together, so why do we not go and play together?", "Kardeşler hep birlikte oynarlar; biz neden gidip birlikte oynamayalım?", [
  tok("وَالْإِخْوَةُ", "akh", "noun", ["mubtada-khabar", "jam-taksir", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْإِخْوَةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and brothers» — the mubtadaʾ.", "«ve kardeşler» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْإِخْوَةُ", "akh", "noun")]),
  tok("دَائِمًا", "daiman", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«always» — an adverb of time, in naṣb.", "«daima» — zaman zarfı, mansub."),
  khamsa("يَلْعَبُونَ", "laiba", "«play»", "«oynarlar»", tags=["mubtada-khabar"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  tok("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«together» — the ḥāl.", "«birlikte» — hâl.", punct="،"),
  tok("فَلِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ جَرٍّ.", "«so why» — the fāʾ, then the jarr lām on the question-mā.", "«öyleyse neden» — fâ, sonra cer lâmı istifham mâ'sında.", segments=[seg("فَ", "fa", "conj"), seg("لِمَاذَا", "limadha", "pron")]),
  la_nafiya(), mudari("نَذْهَبُ", "dhahaba", "«do we go»", "«gidelim»", hidden="نَحْنُ", tags=["la-nafiya"]),
  tok("نَحْنُ", "nahnu", "pron", ["tawkid"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ.", "«we» — a tawkīd of the concealed doer.", "«biz» — gizli zamirin te'kidi."),
  mudari("وَنَلْعَبُ", "laiba", "«and play»", "«ve oynayalım»", hidden="نَحْنُ", tags=["atf-nasaq"]),
  tok("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«together» — the ḥāl.", "«birlikte» — hâl.", punct="؟")])
sen("s10", "«Send him with us tomorrow, to run about and play; and we shall surely keep him safe.» (Yūsuf 12:12)", "«Onu yarın bizimle gönder; gezsin, oynasın. Biz onu elbette koruruz.» (Yûsuf 12:12)", quran([
  amr_enc("أَرْسِلْهُ", "arsala", "هُ", "pron-3ms", "«send him»", "«onu gönder»", tags=["form-iv-verbs"]),
  maa_pron("مَعَنَا", "نَا", "pron-1p", "«with us»", "«bizimle»"),
  tok("غَدًا", "ghad", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«tomorrow» — an adverb of time.", "«yarın» — zaman zarfı."),
  tok("يَرْتَعْ", "rataa", "verb", ["jawab-al-talab", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ لِأَنَّهُ جَوَابُ الطَّلَبِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«(that) he may run about» — in jazm as the answer of the command.", "«gezsin» — talebin cevabı olarak meczum."),
  tok("وَيَلْعَبْ", "laiba", "verb", ["atf-nasaq", "jawab-al-talab"], "الْوَاوُ عَاطِفَةٌ، وَيَلْعَبْ مَعْطُوفٌ عَلَى يَرْتَعْ مَجْزُومٌ بِالسُّكُونِ.", "«and play» — joined, in jazm.", "«ve oynasın» — atıf, meczum.", segments=[seg("وَ", "wa", "conj"), seg("يَلْعَبْ", "laiba", "verb")]),
  tok("وَإِنَّا", "inna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ حَالِيَّةٌ أَوِ اسْتِئْنَافِيَّةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«and indeed we» — inna with the attached «we» as its ism.", "«ve şüphesiz biz» — inne; bitişik «biz» ismidir.", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("نَا", "pron-1p", "pron")]),
  lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِحَافِظُونَ.", "«(for) him» — attached to «keepers».", "«onu» — «koruyucular»a bağlı."),
  tok("لَحَافِظُونَ", "hafiz", "noun", ["inna-wa-akhawatuha", "jam-mudhakkar-salim"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَحَافِظُونَ خَبَرُ إِنَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«surely keepers» — the slid lām of emphasis; the khabar of inna, rafʿ by the wāw of the sound plural.", "«elbette koruyucular» — te'kid lâmı; inne'nin haberi, vâv ile merfû.", punct=".", segments=[seg("لَ", "lam-ibtida", "part"), seg("حَافِظُونَ", "hafiz", "noun")])]))
sen("s11", "And Yaʿqūb was an old man, and Yaʿqūb was wise and forbearing.", "Yakub yaşlı bir ihtiyardı; Yakub akıllı ve halim idi.", [
  kana(), yaqub_ism_kana(), khabar_kana("شَيْخًا", "shaykh", "«an old man»", "«bir ihtiyar»"), nat_nasb("كَبِيرًا", "kabir", "«old (great in years)»", "«yaşlı»", punct="،"),
  kana(), yaqub_ism_kana(), khabar_kana("عَاقِلًا", "aqil", "«wise»", "«akıllı»"), khabar_kana("حَلِيمًا", "halim", "«forbearing»", "«halim»", second=True, punct=".")])
sen("s12", "And Yaʿqūb did not like Yūsuf to be far from him.", "Yakub Yusuf'un kendisinden uzaklaşmasını istemezdi.", [
  kana(), yaqub_ism_kana(), la_nafiya(), khabar_kana_mudari("يُحِبُّ", "ahabba", "«liked»", "«severdi»", tags=["la-nafiya", "form-iv-verbs"]),
  an_(obj_of="يُحِبُّ", en_of="«liked»", tr_of="«severdi»"),
  tok("يَبْعُدَ", "baada", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«be far» — in naṣb after an; its doer follows.", "«uzaklaşsın» — en ile mansub; fâili sonra gelir."),
  tok("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«from him».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), seg("هُ", "pron-3ms", "pron")]),
  yusuf_fail(punct=".")])
sen("s13", "And he feared greatly for Yūsuf.", "Ve Yusuf için çok korkuyordu.", [
  kana_hidden(), khabar_kana_mudari("يَخَافُ", "khafa", "«feared»", "«korkuyordu»", tags=["hollow-verbs"]), ala(),
  tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr by a fatḥa.", "«Yusuf» — fetha ile mecrur."), kathiran(punct=".")])
sen("s14", "So he said to his sons: «I fear that the wolf may eat him while you are heedless of him.» (Yūsuf 12:13)", "Oğullarına dedi: «Siz ondan habersizken onu kurdun yemesinden korkarım.» (Yûsuf 12:13)", [
  qala_h(fa=True, full="فَقَالَ", punct=None),
  tok("لِأَبْنَائِهِ", "ibn", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَأَبْنَاءِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his sons» — in jarr; annexed to the pronoun.", "«oğullarına» — mecrur; zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("أَبْنَائِ", "ibn", "noun"), seg("هِ", "pron-3ms", "pron")]),
  *quran([
  mudari("أَخَافُ", "khafa", "«I fear»", "«korkarım»", hidden="أَنَا", tags=["hollow-verbs"]),
  an_(obj_of="أَخَافُ", en_of="«I fear»", tr_of="«korkarım»"),
  mansub_enc("يَأْكُلَهُ", "akala", "هُ", "pron-3ms", "«(that) … eat him»", "«onu yemesinden»"), dhib_fail(),
  hal_pron("وَأَنْتُمْ", "antum", "you", "siz"),
  tok("عَنْهُ", "an", "prep", ["huruf-jarr"], "عَنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِغَافِلُونَ.", "«of him» — attached to «heedless».", "«ondan» — «habersiz»e bağlı.", segments=[seg("عَنْ", "an", "prep"), seg("هُ", "pron-3ms", "pron")]),
  khabar_waw("غَافِلُونَ", "ghafil", "«heedless»", "«habersiz»", punct=".")])])
sen("s15", "They said: Never! How could the wolf eat him while we are present?", "Dediler: Asla! Biz hazırken kurt onu nasıl yer?", [
  qalu(punct=None),
  tok("أَبَدًا", "abadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ (لَا يَأْكُلُهُ أَبَدًا).", "«never» — an adverb of time; its verb is understood («he will never eat him»).", "«asla» — zaman zarfı; fiili mukadder.", punct="!"),
  tok("كَيْفَ", "kayfa", "noun", ["al-istifham", "hal"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — the question noun; in the place of naṣb as a ḥāl.", "«nasıl» — istifham ismi; mahallen mansub hâl."),
  verb_enc("يَأْكُلُهُ", "akala", "هُ", "pron-3ms", "«eat him»", "«onu yer»", hidden=None), dhib_fail(),
  hal_pron("وَنَحْنُ", "nahnu", "we", "biz"), khabar_waw("حَاضِرُونَ", "hadir", "«present»", "«hazır»", punct="؟")])
sen("s16", "And how could he eat him, while we are strong young men?", "Biz güçlü gençlerken onu nasıl yer?", [
  tok("وَكَيْفَ", "kayfa", "noun", ["atf-nasaq", "al-istifham", "hal"], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — joined; the question noun as a ḥāl.", "«ve nasıl» — atıf; istifham ismi, hâl.", segments=[seg("وَ", "wa", "conj"), seg("كَيْفَ", "kayfa", "noun")]),
  verb_enc("يَأْكُلُهُ", "akala", "هُ", "pron-3ms", "«eat him»", "«onu yer»", punct="،"),
  hal_pron("وَنَحْنُ", "nahnu", "we", "biz"),
  tok("شُبَّانٌ", "shabb", "noun", ["mubtada-khabar", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ.", "«young men» — the khabar; a broken plural.", "«gençler» — haber; cem-i mükesser."),
  tok("أَقْوِيَاءُ", "qawi", "noun", ["naat-sifa", "jam-taksir", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.", "«strong» — the naʿt; a diptote by the alif of femininity.", "«güçlü» — sıfat; te'nis elifi sebebiyle gayr-i munsarıf.", punct="؟")])
sen("s17", "And Yaʿqūb gave Yūsuf leave.", "Ve Yakub Yusuf'a izin verdi.", [
  mazi("وَأَذِنَ", "adhina", "«gave leave»", "«izin verdi»", hidden=None, wa=True), yaqub_fail(), li_name("لِيُوسُفَ", "yusuf", "Yūsuf", "Yusuf", punct=".")])
# ================================================================ §4 إلى الغابة (pp. 32–34)
sen("s18", "And the brothers rejoiced greatly when Yaʿqūb gave Yūsuf leave.", "Yakub Yusuf'a izin verince kardeşler çok sevindi.", [
  mazi("وَفَرِحَ", "fariha", "«rejoiced»", "«sevindi»", hidden=None, wa=True), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]), kathiran(),
  tok("لَمَّا", "lamma", "part", ["maful-fih"], "ظَرْفٌ بِمَعْنَى حِينَ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«when» — a time-word, built.", "«-ınca» — zarf, mebnî."),
  mazi("أَذِنَ", "adhina", "«gave leave»", "«izin verdi»", hidden=None), yaqub_fail(), li_name("لِيُوسُفَ", "yusuf", "Yūsuf", "Yusuf", punct=".")])
sen("s19", "And they went to a forest and threw Yūsuf into a well in the forest, and they had no mercy on little Yūsuf, nor on Yaʿqūb, the old man.", "Bir ormana gittiler ve Yusuf'u ormandaki bir kuyuya attılar; küçük Yusuf'a acımadılar, yaşlı ihtiyar Yakub'a da acımadılar.", [
  mazi_pl("وَذَهَبُوا", "dhahaba", "«they went»", "«gittiler»", wa=True), ila(), majrur("غَابَةٍ", "ghaba-forest", "«a forest»", "«bir orman»", "إِلَى"),
  tok("وَأَلْقَوْا", "alqa", "verb", ["atf-nasaq", "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَلْقَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ.", "«and they threw» — a nāqiṣ māḍī: the alif dropped before the group's wāw, the ḍamma estimated on it.", "«ve attılar» — nâkıs mâzî: elif cemi vâvından önce düşmüş, zamme takdîrî.", segments=[seg("وَ", "wa", "conj"), seg("أَلْقَوْا", "alqa", "verb")]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), fi(), majrur("بِئْرٍ", "bir", "«a well»", "«bir kuyu»", "فِي"),
  tok("فِي", "fi", "prep", ["huruf-jarr", "jumla-sifa"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِبِئْرٍ.", "«in» — the phrase is a naʿt of «a well».", "«-de» — şibh-i cümle «kuyu»nun sıfatı."),
  majrur("الْغَابَةِ", "ghaba-forest", "«the forest»", "«orman»", "فِي"),
  lam_jazim(wa=True), majzum_pl("يَرْحَمُوا", "rahima", "«they had (no) mercy»", "«acımadılar»"),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'a»"), nat_nasb("الصَّغِيرَ", "saghir", "«little»", "«küçük»", punct="،"),
  lam_jazim(wa=True), majzum_pl("يَرْحَمُوا", "rahima", "«they had (no) mercy»", "«acımadılar»"),
  name_maful("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub'a»"), nat_nasb("الشَّيْخَ", "shaykh", "«the old man»", "«ihtiyar»"), nat_nasb("الْكَبِيرَ", "kabir", "«aged»", "«yaşlı»", punct=".")])
sen("s20", "And Yūsuf was a small boy, and his heart was small.", "Yusuf küçük bir çocuktu ve kalbi küçüktü.", [
  kana(), yusuf_ism_kana(), khabar_kana("وَلَدًا", "walad", "«a boy»", "«bir çocuk»"), nat_nasb("صَغِيرًا", "saghir", "«small»", "«küçük»", punct="،"),
  kana(), mudaf_pron("قَلْبُهُ", "qalb", "هُ", "pron-3ms", "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ", "«his heart» — kāna's ism", "«kalbi» — kâne'nin ismi", tags=[K]), khabar_kana("صَغِيرًا", "saghir", "«small»", "«küçük»", punct=".")])
sen("s21", "And the well was deep, and the well was dark.", "Kuyu derindi ve kuyu karanlıktı.", [
  kanat(), tok("الْبِئْرُ", "bir", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the well» — kāna's ism.", "«kuyu» — kâne'nin ismi."), khabar_kana("عَمِيقَةً", "amiq", "«deep»", "«derin»", punct="،"),
  kanat(), tok("الْبِئْرُ", "bir", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the well» — kāna's ism.", "«kuyu» — kâne'nin ismi."), khabar_kana("مُظْلِمَةً", "muzlim", "«dark»", "«karanlık»", punct=".")])
sen("s22", "And Yūsuf was alone.", "Ve Yusuf yalnızdı.", [kana(), yusuf_ism_kana(), khabar_kana("وَحِيدًا", "wahid-alone", "«alone»", "«yalnız»", punct=".")])
sen("s23", "But Allah gave Yūsuf glad tidings and said to him: Do not grieve and do not fear.", "Fakat Allah Yusuf'u müjdeledi ve ona dedi: Üzülme ve korkma.", [
  tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kardeşi lâkinne.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")]),
  allah_ism(part="لٰكِنَّ"),
  mazi("بَشَّرَ", "bashshara", "«gave glad tidings (to)»", "«müjdeledi»", hidden="هُوَ", tags=["inna-wa-akhawatuha", "form-ii-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  qala_h(wa=True, full="وَقَالَ", punct=None), lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِقَالَ.", "«to him».", "«ona».", punct=":"),
  la_nahiya_(), nahy("تَحْزَنْ", "hazina", "«do not grieve»", "«üzülme»"),
  la_nahiya_(wa=True), nahy("وَتَخَفْ", "khafa", "«do not fear»", "«korkma»", extra="، وَحُذِفَتِ الْأَلِفُ لِالْتِقَاءِ السَّاكِنَيْنِ", tags=["hollow-verbs"], wa=True, punct=".")])
sen("s24", "Indeed Allah is with you, and you shall have a high standing.", "Şüphesiz Allah seninledir; senin büyük bir şanın olacak.", [
  inna(), allah_ism(),
  tok("مَعَكَ", "maa", "noun", ["inna-wa-akhawatuha", "maful-fih", "idafa-definiteness"], "مَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ، وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«with you» — the adverb annexed to the pronoun; the phrase is inna's khabar.", "«seninle» — zamire muzâf zarf; şibh-i cümle inne'nin haberi.", punct="،", segments=[seg("مَعَ", "maa", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَسَيَكُونُ", "kana", "verb", ["atf-nasaq", K, "hollow-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَالسِّينُ حَرْفُ اسْتِقْبَالٍ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and there shall be» — the sīn of the future on kāna's muḍāriʿ.", "«ve olacak» — istikbal sîni kâne'nin muzârisinde.", segments=[seg("وَ", "wa", "conj"), seg("سَ", "sa", "part"), seg("يَكُونُ", "kana", "verb")]),
  lahu("لَكَ", "كَ", "pron-2ms", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُونُ مُقَدَّمٌ.", "«(to) you» — yakūn's khabar, fronted.", "«senin» — yekûn'un öne alınmış haberi.", tags=[K]),
  tok("شَأْنٌ", "shan", "noun", [K], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a standing» — yakūn's delayed ism.", "«bir şan» — yekûn'un geciktirilmiş ismi.", punct=".")])
sen("s25", "The brothers will come to you, and you will tell them of what they did.", "Kardeşler sana gelecek ve sen onlara yaptıklarını haber vereceksin.", [
  sa_mudari("سَيَحْضُرُ", "hadara", "«will come»", "«gelecek»", hidden=None),
  tok("إِلَيْكَ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ.", "«to you».", "«sana».", segments=[seg("إِلَيْ", "ila", "prep"), seg("كَ", "pron-2ms", "pron")]),
  ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]),
  verb_enc("وَتُخْبِرُهُمْ", "akhbara", "هُمْ", "pron-3mp", "«and you will tell them»", "«ve onlara haber vereceksin»", hidden="أَنْتَ", wa=True, tags=["atf-nasaq", "form-iv-verbs"]),
  tok("بِمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«of what» — the bāʾ of jarr on the relative mā.", "«-dığını» — cer bâsı ism-i mevsûl mâ'da.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  mazi_pl_enc("فَعَلُوهُ", "faala", "هُ", "pron-3ms", "«they did (it)»", "«yaptılar»", tags=["ism-mawsul"], punct=".")])
sen("s26", "And when they had finished their business and thrown Yūsuf into the well, they gathered and said: What shall we tell our father?", "İşlerini bitirip Yusuf'u kuyuya atınca toplandılar ve dediler: Babamıza ne diyeceğiz?", [
  tok("وَلَمَّا", "lamma", "part", ["anwa-al-waw", "maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«and when» — a time-word built.", "«ve … -ınca» — zarf, mebnî.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi_pl("فَرَغُوا", "faragha", "«they had finished»", "«bitirdiler»"), min_(),
  mudaf_pron("شَأْنِهِمْ", "shan", "هِمْ", "pron-3mp", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«their business» — in jarr", "«işleri» — mecrur", tags=["huruf-jarr"]),
  tok("وَأَلْقَوْا", "alqa", "verb", ["atf-nasaq", "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَلْقَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ.", "«and had thrown» — joined; a nāqiṣ māḍī.", "«ve attılar» — atıf; nâkıs mâzî.", segments=[seg("وَ", "wa", "conj"), seg("أَلْقَوْا", "alqa", "verb")]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), fi(), majrur("الْبِئْرِ", "bir", "«the well»", "«kuyu»", "فِي"),
  mazi_pl("اجْتَمَعُوا", "ijtamaa", "«they gathered»", "«toplandılar»", tags=["form-viii-verbs"]), qalu(wa=True),
  tok("مَاذَا", "madha", "pron", ["al-istifham"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«what» — the fronted object.", "«ne» — öne alınmış mef'ûl."),
  mudari("نَقُولُ", "qala", "«shall we say»", "«diyeceğiz»", hidden="نَحْنُ", tags=["hollow-verbs"]),
  tok("لِأَبِينَا", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَأَبِي مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَنَا مُضَافٌ إِلَيْهِ.", "«to our father» — jarr by the yāʾ of the five nouns.", "«babamıza» — beş isimden olduğu için yâ ile mecrur.", punct="؟", segments=[seg("لِ", "li", "prep"), seg("أَبِي", "ab", "noun"), seg("نَا", "pron-1p", "pron")])])
sen("s27", "One of them said: Our father used to say «I fear the wolf may eat him» — so we shall tell him: You spoke truly, O our father; the wolf has eaten him.", "Biri dedi: Babamız «onu kurdun yemesinden korkarım» derdi; ona deriz ki: Doğru söyledin ey babamız, onu kurt yedi.", [
  qala_h(punct=None), mudaf_pron("بَعْضُهُمْ", "bad", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "«one of them» — the doer", "«onlardan biri» — fâil", tags=["fail"], punct=":"),
  kana(full="كَانَ", wa=False),
  tok("أَبُونَا", "ab", "noun", [K, "five-nouns", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَنَا مُضَافٌ إِلَيْهِ.", "«our father» — kāna's ism, rafʿ by the wāw.", "«babamız» — kâne'nin ismi, vâv ile merfû.", segments=[seg("أَبُو", "ab", "noun"), seg("نَا", "pron-1p", "pron")]),
  khabar_kana_mudari("يَقُولُ", "qala", "«used to say»", "«derdi»", tags=["hollow-verbs", "maful-bihi"], extra="بِالضَّمَّةِ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ"),
  mudari("أَخَافُ", "khafa", "«I fear»", "«korkarım»", hidden="أَنَا", tags=["hollow-verbs"]), an_(obj_of="أَخَافُ", en_of="«I fear»", tr_of="«korkarım»"),
  mansub_enc("يَأْكُلَهُ", "akala", "هُ", "pron-3ms", "«(that) … eat him»", "«onu yemesinden»"), dhib_fail(),
  tok("فَنَقُولُ", "qala", "verb", ["atf-nasaq", "hollow-verbs", "mudari-marfu", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَنَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«so we shall say» — a muḍāriʿ with «we» concealed; what is said is its object.", "«o zaman deriz» — fâil gizli «biz»; söylenen söz mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("نَقُولُ", "qala", "verb")]),
  lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِنَقُولُ.", "«to him».", "«ona»."),
  tok("صَدَقْتَ", "sadaqa-verb", "verb", ["fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ.", "«you spoke truly» — a māḍī built on sukūn before the doer's tāʾ.", "«doğru söyledin» — fâil tâ'sı ile sükûn üzere mebnî mâzî."),
  *ya_abana(), qad_(), akalahu(), dhib_fail(punct=".")])
sen("s28", "The brothers agreed to that, and said: Yes, we shall tell him: O our father, the wolf has eaten him.", "Kardeşler buna razı oldu ve dediler: Evet, ona deriz ki: Ey babamız, onu kurt yedi.", [
  mazi("وَافَقَ", "wafaqa", "«agreed»", "«razı oldu»", hidden=None, tags=["form-iii-verbs"]), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]), ala(),
  ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«buna»", punct="،"),
  qalu(wa=True, punct=None), tok("نَعَمْ", "naam", "part", [], "حَرْفُ جَوَابٍ لَا مَحَلَّ لَهُ.", "«yes» — the answering particle.", "«evet» — cevap harfi."),
  mudari("نَقُولُ", "qala", "«we shall say»", "«deriz»", hidden="نَحْنُ", tags=["hollow-verbs", "maful-bihi"], extra_ar="، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ"),
  lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِنَقُولُ.", "«to him».", "«ona»."),
  *ya_abana(), qad_(), akalahu(), dhib_fail(punct=".")])
sen("s29", "One of the brothers said: But what is the sign of that?", "Kardeşlerden biri dedi: Fakat bunun delili ne?", [
  qala_h(punct=None), tok("بَعْضُ", "bad", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«one (of)» — the doer; a muḍāf.", "«biri» — fâil; muzâf."),
  ikhwa("الْإِخْوَانِ", "jarr", "مُضَافٌ إِلَيْهِ", "«the brothers» — the muḍāf ilayh (the other plural of أَخ)", "«kardeşler» — muzâfun ileyh («kardeş»in diğer cem'i)", punct=":"),
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin; it governs nothing.", "«fakat» — tahfif edilmiş lâkin; amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنْ", "lakin", "part")]),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the question noun as mubtadaʾ.", "«ne» — istifham ismi, mübtedâ."),
  tok("آيَةُ", "aya", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the sign (of)» — the khabar; a muḍāf.", "«delili» — haber; muzâf."),
  hadha_pron_jarr("ذٰلِكَ", "dhalika", "«that»", "«bunun»", punct="؟")])
sen("s30", "They said: The sign of that is the blood.", "Dediler: Bunun delili kandır.", [
  qalu(punct=None), tok("آيَةُ", "aya", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the sign (of)» — the mubtadaʾ; a muḍāf.", "«delili» — mübtedâ; muzâf."),
  hadha_pron_jarr("ذٰلِكَ", "dhalika", "«that»", "«bunun»"),
  tok("الدَّمُ", "dam-blood", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the blood» — the khabar.", "«kan» — haber.", punct=".")])
sen("s31", "And the brothers took a ram and slaughtered it.", "Kardeşler bir koç aldılar ve onu kestiler.", [
  mazi("وَأَخَذَ", "akhadha", "«took»", "«aldı»", hidden=None, wa=True), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]),
  maful("كَبْشًا", "kabsh", "«a ram»", "«bir koç»"), mazi_pl_enc("وَذَبَحُوهُ", "dhabaha", "هُ", "pron-3ms", "«and slaughtered it»", "«ve onu kestiler»", wa=True, tags=["atf-nasaq"], punct=".")])
sen("s32", "And they took Yūsuf's shirt and dyed it.", "Yusuf'un gömleğini aldılar ve onu boyadılar.", [
  mazi_pl("وَأَخَذُوا", "akhadha", "«they took»", "«aldılar»", wa=True),
  tok("قَمِيصَ", "qamis", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the shirt (of)» — the object; a muḍāf.", "«gömleğini» — mef'ûl; muzâf."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"), mazi_pl_enc("وَصَبَغُوهُ", "sabagha", "هُ", "pron-3ms", "«and dyed it»", "«ve onu boyadılar»", wa=True, tags=["atf-nasaq"], punct=".")])
sen("s33", "And the brothers rejoiced greatly, and said: Now our father will believe.", "Kardeşler çok sevindiler ve dediler: Şimdi babamız inanır.", [
  mazi("وَفَرِحَ", "fariha", "«rejoiced»", "«sevindi»", hidden=None, wa=True), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]), jiddan(punct=":"),
  qalu(wa=True, punct=None),
  tok("الْآنَ", "al-an", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«now» — a time-adverb built on fatḥa.", "«şimdi» — fetha üzere mebnî zaman zarfı."),
  tok("يُصَدِّقُ", "saddaqa", "verb", ["mudari-marfu", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«will believe» — a muḍāriʿ; its doer follows.", "«inanır» — muzâri; fâili sonra gelir."),
  tok("أَبُونَا", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَنَا مُضَافٌ إِلَيْهِ.", "«our father» — the doer, rafʿ by the wāw.", "«babamız» — fâil, vâv ile merfû.", punct=".", segments=[seg("أَبُو", "ab", "noun"), seg("نَا", "pron-1p", "pron")])])

# ---------------------------------------------------------------- glossary
NEW = {
 "ghaba-forest": G("ghaba-forest", "غَابَة", "غ ي ب", "noun", "a forest, a thicket", "orman, ağaçlık", 1, plural="غَابَات"),
 "wahid-alone": G("wahid-alone", "وَحِيد", "و ح د", "noun", "alone, lonely (ṣifa mushabbaha)", "yalnız, tek başına (sıfat-ı müşebbehe)", 1),
 "hazina": G("hazina", "حَزِنَ", "ح ز ن", "verb", "to grieve, to be sad", "üzülmek, kederlenmek", 1, form="I"),
 "adhina": G("adhina", "أَذِنَ", "أ ذ ن", "verb", "to give leave, to permit (أَذِنَ لِـ)", "izin vermek", 1, form="I"),
 "sabagha": G("sabagha", "صَبَغَ", "ص ب غ", "verb", "to dye, to stain", "boyamak", 1, form="I"),
 "faragha": G("faragha", "فَرَغَ", "ف ر غ", "verb", "to finish (فَرَغَ مِنْ), to be free of", "bitirmek, boşalmak (فَرَغَ مِنْ)", 1, form="I"),
 "rataa": G("rataa", "رَتَعَ", "ر ت ع", "verb", "to run about freely, to graze at will", "serbestçe gezinmek, otlamak", 2, form="I"),
 "daiman": G("daiman", "دَائِمًا", "د و م", "noun", "always (an adverb of time)", "daima, her zaman (zaman zarfı)", 1),
 "hafiz": G("hafiz", "حَافِظ", "ح ف ظ", "noun", "a keeper, a guardian (ism fāʿil of حَفِظَ)", "koruyucu, muhafız (hafiza'nın ism-i fâili)", 1, plural="حَافِظُونَ"),
 "ghafil": G("ghafil", "غَافِل", "غ ف ل", "noun", "heedless, inattentive (ism fāʿil of غَفَلَ)", "gafil, habersiz (gafele'nin ism-i fâili)", 1, plural="غَافِلُونَ"),
 "sadaqa-verb": G("sadaqa-verb", "صَدَقَ", "ص د ق", "verb", "to speak the truth", "doğru söylemek", 1, form="I"),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("dhib", "ذئب"), ("qamis", "قميص"), ("dam-blood", "دم"), ("aya", "آية"), ("amiq", "عميق"), ("muzlim", "مظلم"), ("bashshara", "بشر"), ("hadara", "حضر"), ("saddaqa", "صدق"), ("rahima", "رحم"), ("azama", "عزم"), ("sharr", "شر"), ("aziz", "عزيز"), ("aqil", "عاقل"), ("ittafaqa", "اتفق"), ("ray", "رأي"), ("hadir", "حاضر"), ("abadan", "أبدا"), ("ghad", "غد"), ("qalb", "قلب"), ("al-an", "الآن"), ("baada", "بعد"), ("lam-jazim", "لم"), ("antum", "أنتم"), ("an", "عن")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm, (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("hazina", "adhina", "sabagha", "faragha", "rataa", "sadaqa-verb"): mo["verbs"].pop(_k, None)
put_morph(mo, "hazina", _sg.idgham(_sg.sound1("samia", "حَزِن", "حْزَن", "اِحْزَن", "حُزْن", "حَزِين", note="لَازِمٌ: حَزِنَ عَلَيْهِ — وَاللَّامُ نُونٌ تُدْغَمُ فِي نُونِ النِّسْوَةِ (حَزِنَّ).")))
put_morph(mo, "adhina", _sg.idgham(_sg.sound1("samia", "أَذِن", "أْذَن", "اِئْذَن", "إِذْن", "آذِن", "مَأْذُون", "أُذِنَ", "يُؤْذَنُ", note="يَتَعَدَّى بِاللَّامِ: أَذِنَ لَهُ — مَهْمُوزُ الْفَاءِ؛ أَمْرُهُ اِئْذَنْ.")))
put_morph(mo, "sabagha", _sg.sound1("nasara", "صَبَغ", "صْبُغ", "اُصْبُغ", "صَبْغ", "صَابِغ", "مَصْبُوغ", "صُبِغَ", "يُصْبَغُ", note="مُتَعَدٍّ."))
put_morph(mo, "faragha", _sg.sound1("nasara", "فَرَغ", "فْرُغ", "اُفْرُغ", "فَرَاغ", "فَارِغ", note="لَازِمٌ: فَرَغَ مِنْ عَمَلِهِ."))
put_morph(mo, "rataa", _sg.sound1("fataha", "رَتَع", "رْتَع", "اِرْتَع", "رَتْع", "رَاتِع", note="لَازِمٌ — حَلْقِيُّ الْعَيْنِ فَبَابُهُ فَتَحَ."))
put_morph(mo, "sadaqa-verb", _sg.sound1("nasara", "صَدَق", "صْدُق", "اُصْدُق", "صِدْق", "صَادِق", "مَصْدُوق", "صُدِقَ", "يُصْدَقُ", note="لَازِمٌ وَمُتَعَدٍّ: صَدَقَ فُلَانًا الْحَدِيثَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 9 (print pp. 30–34, «أَحْسَنُ الْقَصَصِ» sections 3 «وَفْدٌ إِلَى يَعْقُوب» and 4 «إِلَى الْغَابَة»): the brothers' plea to Yaʿqūb (s1–s9), Yūsuf 12:12 as the print sets it (s10, marked), Yaʿqūb's fear and his answer with Yūsuf 12:13 in the print's words — the aya's opening وَ dropped, as printed (s11–s14, the quotation marked), the brothers' reply and the leave (s15–s17); the forest and the well, the glad tidings in the well, the council, the ram and the dyed shirt (s18–s33). "
          "One printed line is one sentence, split at the print's own full stops where a line holds several (s8–s9, s11, s20–s21); s14 joins the print's «فَقَالَ لِأَبْنَائِهِ:» to the quotation that follows it across the page break; the colon after «جِدًّا» in s33 is the print's own.")
ADD_TR = (" Dokuzuncu bölüm (basılı s. 30–34, «أَحْسَنُ الْقَصَصِ» 3. kısım «وَفْدٌ إِلَى يَعْقُوب» ve 4. kısım «إِلَى الْغَابَة»): kardeşlerin Yakub'a ricası (s1–s9), Yûsuf 12:12 baskıdaki şekliyle (s10, işaretli), Yakub'un korkusu ve Yûsuf 12:13'ü baskının kelimeleriyle veren cevabı — âyetin baştaki وَ'ı baskıda düşmüştür (s11–s14, alıntı işaretli), kardeşlerin cevabı ve izin (s15–s17); orman ve kuyu, kuyudaki müjde, kardeşlerin meclisi, koç ve boyanan gömlek (s18–s33). "
          "Basılı her satır bir cümledir; birden çok cümle taşıyan satırlar baskının noktalarından bölünmüştür (s8–s9, s11, s20–s21); s14 baskının «فَقَالَ لِأَبْنَائِهِ:» satırını sayfa sonunu aşan alıntıyla birleştirir; s33'te «جِدًّا»dan sonraki iki nokta baskının kendi işaretidir.")
write_out(9, S, TITLE, ADD_EN, ADD_TR, "pp. 30–34", GLOSS_ADD)
report(9, S, GLOSS_ADD, ())
