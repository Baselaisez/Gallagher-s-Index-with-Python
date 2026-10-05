# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 23: «حُسْنُ الْعَاقِبَةِ» — «أَحْسَنُ الْقَصَصِ» section 25 (print pp. 67–68):
Yūsuf's kingship and his prayer (12:101), the end of volume 1.
Every printed line is one sentence; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch23.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "حُسْنُ الْعَاقِبَةِ", "en": "The good end", "tr": "Güzel âkıbet"}
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
# ================================================================ chapter-23 helpers
def wa_la_atf(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["atf-nasaq", "la-nafiya"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَلَا لِتَأْكِيدِ النَّفْيِ، وَالِاسْمُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«nor " + en + "» — joined, the lā repeating the negation.", "«ne de " + tr + "» — ma'tûf; lâ nefyi tekrar eder.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part"), seg(full[4:], lex, "noun")])
def hal_(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["hal"] + list(tags), "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the ḥāl, naṣb by fatḥa.", tr + " — hâl, fetha ile mansub.", punct=punct)
def yusuf_mi(punct=None): return name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'un»", punct=punct)
def yusuf_maful(punct=None): return name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»", punct=punct)
def majzum(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra=""):
    return tok(full, lex, "verb", ["lam-jazim"] + list(tags), "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + extra + ".", en + " — a muḍāriʿ in jazm after lam, the sign the sukūn.", tr + " — lem ile meczum muzâri, alâmeti sükûn.", punct=punct)
def majzum_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), hidden="هُوَ", punct=None):
    host = full[:len(full) - len(pron_seg)]
    return tok(full, lex, "verb", ["lam-jazim", "maful-bihi"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", en + " — in jazm after lam; the attached pronoun is its object.", tr + " — lem ile meczum; bitişik zamir mef'ûlüdür.", punct=punct, segments=[seg(host, lex, "verb"), seg(pron_seg, pron_lex, "pron")])
def kk_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), wa=True, punct=None, hidden="هُوَ"):
    # a wa-joined mudari with an object pronoun, joined onto kana's khabar clause
    return verb_enc(full, lex, pron_seg, pron_lex, en, tr, tags=list(tags) + [K], hidden=hidden, punct=punct, wa=wa, extra=" — مَعْطُوفٌ عَلَى جُمْلَةِ خَبَرِ كَانَ")
def allah_maful(punct=None): return tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah'ı» — mef'ûl.", punct=punct)
def allah_mi(punct=None): return tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«(of) Allah» — the muḍāf ilayh.", "«Allah'ın» — muzâfun ileyh.", punct=punct)
def la_kk(full, lex, en, tr, tags=(), punct=None, wa=False):
    # لَا + mudari as kana's khabar clause
    return tok(full, lex, "verb", [K, "mudari-marfu", "la-nafiya"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ الْمَنْفِيَّةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — a muḍāriʿ; the negated clause is kāna's khabar.", tr + " — muzâri; olumsuz cümle kâne'nin haberidir.", punct=punct)
def an_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, wa=False, extra=""):
    return tok(full, lex, "verb", ["an-masdariyya"] + list(tags) + (["atf-nasaq"] if wa else []), W(wa) + ("مَعْطُوفٌ عَلَى يَمُوتَ: " if wa else "") + "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + extra + ".", Wen(wa) + en + " — manṣūb after an.", Wtr(wa) + tr + " — en ile mansub.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def mawt_mm(punct=None): return tok("مَوْتَ", "mawt", "noun", ["maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ مُبَيِّنٌ لِلنَّوْعِ، وَهُوَ مُضَافٌ.", "«the death (of)» — the absolute object naming the kind; a muḍāf.", "«ölümü» — nev'i bildiren mef'ûl-i mutlak; muzâf.", punct=punct)
def maa_mi(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["idafa-definiteness"] + list(tags), "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + ("وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ" if full.endswith("ِينَ") else "بِالْكَسْرَةِ") + ".", en + " — the muḍāf ilayh of مَعَ.", tr + " — maa'nın muzâfun ileyhi.", punct=punct)
def maa_z(): return tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with» — an adverb of place; a muḍāf.", "«ile, beraber» — mekân zarfı; muzâf.")
def enc_2s(full, lex, en, tr, tags=(), extra="", punct=None, wa=False, amr=False):
    # آتَيْتَنِي / عَلَّمْتَنِي — mazi 2ms with the speaker's ya; or an amr with it
    host = full[:len(full) - 2]
    ar = W(wa) + ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: أَنْتَ" if amr else "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ") + "، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + extra + "."
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + ([seg(host[2:] if wa else host, lex, "verb"), seg("تَ", "pron-2ms", "pron")] if not amr else [seg(host[2:] if wa else host, lex, "verb")]) + [seg("نِي", "pron-1s", "pron")]
    return tok(full, lex, "verb", (["imperative-amr"] if amr else []) + ["ya-al-mutakallim", "maful-bihi"] + list(tags), ar, Wen(wa) + en + " — the nūn of protection and the speaker's yāʾ as the object.", Wtr(wa) + tr + " — vikâye nûnu ve mütekellim yâ'sı mef'ûl.", punct=punct, segments=segs)
# ---------------------------------------------------------------- §25 حُسْنُ الْعَاقِبَةِ (print pp. 67–68)
sen("s1", "And this great kingship did not distract Yūsuf from Allah, nor did it change him.", "Bu büyük hükümdarlık Yusuf'u Allah'tan alıkoymadı ve onu değiştirmedi.", [
  lam_jazim(wa=True), majzum("يَشْغَلْ", "shaghala", "«distract»", "«alıkoymadı»", hidden=None, extra=" — وَالْفَاعِلُ مُتَأَخِّرٌ: الْمُلْكُ"),
  yusuf_maful(),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»", tags=["asma-al-ishara", "fail"]),
  tok("الْمُلْكُ", "mulk", "noun", ["fail", "badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ الْفَاعِلُ فِي الْمَعْنَى، أُخِّرَ عَنِ الْمَفْعُولِ.", "«the kingship» — badal of the demonstrative, the doer in sense, delayed after the object.", "«hükümdarlık» — işaret isminden bedel; mânâca fâil, mef'ûlden sonraya bırakılmış."),
  nat_raf("الْعَظِيمُ", "azim", "«the great»", "«büyük»"),
  tok("عَنِ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، كُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its nūn given a kasra for the meeting of two sukūns.", "«-den» — iki sükûn için nûnu kesreli."),
  allah_jarr("عَنْ", "«Allah»", "«Allah'tan»"),
  lam_jazim(wa=True), majzum_enc("يُغَيِّرْهُ", "ghayyara", "هُ", "pron-3ms", "«change him»", "«onu değiştirmedi»", tags=["form-ii-verbs"], hidden="هُوَ", punct=".")])
sen("s2", "And Yūsuf used to remember Allah, worship Him and fear Him.", "Yusuf Allah'ı anar, O'na ibadet eder ve O'ndan korkardı.", [
  kana(), yusuf_ism_kana(), khabar_kana_mudari("يَذْكُرُ", "dhakara", "«remembers»", "«anar»"), allah_maful(),
  kk_enc("وَيَعْبُدُهُ", "abada", "هُ", "pron-3ms", "«and worships Him»", "«ve O'na ibadet eder»"),
  kk_enc("وَيَخَافُهُ", "khafa", "هُ", "pron-3ms", "«and fears Him»", "«ve O'ndan korkar»", tags=["hollow-verbs"], punct=".")])
sen("s3", "And Yūsuf used to rule by the rule of Allah and carry out the commands of Allah.", "Yusuf Allah'ın hükmüyle hükmeder ve Allah'ın emirlerini yerine getirirdi.", [
  kana(), yusuf_ism_kana(), khabar_kana_mudari("يَحْكُمُ", "hakama", "«rules»", "«hükmeder»"),
  tok("بِحُكْمِ", "hukm", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَحُكْمِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«by the rule (of)» — in jarr; a muḍāf.", "«hükmüyle» — mecrur; muzâf.", segments=[seg("بِ", "bi", "prep"), seg("حُكْمِ", "hukm", "noun")]),
  allah_mi(),
  tok("وَيُنَفِّذُ", "naffadha", "verb", [K, "mudari-marfu", "form-ii-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَيُنَفِّذُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — مَعْطُوفٌ عَلَى جُمْلَةِ خَبَرِ كَانَ.", "«and carries out» — a Form II muḍāriʿ joined onto kāna's khabar clause.", "«ve yerine getirir» — tef'îl bâbından muzâri, kâne'nin haber cümlesine ma'tûf.", segments=wa_("يُنَفِّذُ", "naffadha", "verb")),
  tok("أَوَامِرَ", "amr", "noun", ["maful-bihi", "mamnu-min-sarf", "jam-taksir", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — أَوَامِرُ جَمْعُ أَمْرٍ بِمَعْنَى الطَّلَبِ، عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.", "«the commands (of)» — the object; a muḍāf. أَوَامِر is the plural of أَمْر in the sense of a command (the أُمُور plural means «matters»), on the diptote plural pattern.", "«emirlerini» — mef'ûl; muzâf. Evâmir, «buyruk» anlamındaki emr'in cem'idir (umûr «işler» demektir); müntehe'l-cumû' vezninde."),
  allah_mi(punct=".")])
sen("s4", "And Yūsuf did not see the kingship as great, nor did he count it as anything great", "Yusuf hükümdarlığı büyük görmez ve onu büyük bir şey saymazdı", [
  kana(), yusuf_ism_kana(), la_nafiya(),
  la_kk("يَرَى", "raa", "«sees»", "«görür»", tags=["naqis-verbs"]),
  tok("الْمُلْكَ", "mulk", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ — رَأَى هُنَا بِمَعْنَى ظَنَّ، تَنْصِبُ مَفْعُولَيْنِ.", "«the kingship» — the first object; رَأَى here means «deem» and takes two objects.", "«hükümdarlığı» — birinci mef'ûl; burada raâ «sanmak» anlamında, iki mef'ûl alır."),
  tok("كَبِيرًا", "kabir", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«(as) great» — the second object.", "«büyük» — ikinci mef'ûl."),
  tok("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor» — the wāw joins, the lā repeats the negation.", "«ne de» — vâv atıf, lâ nefyi pekiştirir.", segments=wa_("لَا", "la-nafiya", "part")),
  tok("يَعُدُّهُ", "adda-count", "verb", [K, "mudari-marfu", "doubled-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ — مَعْطُوفٌ عَلَى جُمْلَةِ خَبَرِ كَانَ (مُضَاعَفٌ).", "«counts it» — a doubled muḍāriʿ joined onto kāna's khabar clause; the pronoun its first object.", "«onu sayar» — muzaaf muzâri, kâne'nin haber cümlesine ma'tûf; zamir birinci mef'ûl.", segments=[seg("يَعُدُّ", "adda-count", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("شَيْئًا", "shay", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — عَدَّ تَنْصِبُ مَفْعُولَيْنِ.", "«(as) a thing» — the second object; عَدَّ takes two objects.", "«bir şey» — ikinci mef'ûl; adde iki mef'ûl alır."),
  nat_nasb("كَبِيرًا", "kabir", "«great»", "«büyük»")])
sen("s5", "And Yūsuf did not like to die the death of a king and be gathered with the kings.", "Yusuf bir kral ölümüyle ölmeyi ve krallarla haşrolunmayı sevmezdi.", [
  kana(), yusuf_ism_kana(), la_nafiya(),
  la_kk("يُحِبُّ", "ahabba", "«likes»", "«sever»", tags=["form-iv-verbs", "doubled-verbs"]),
  an_(obj_of="يُحِبُّ", en_of="«likes»", tr_of="«sever»"),
  an_mudari("يَمُوتَ", "mata-die", "«(that) he die»", "«ölmeyi»", tags=["hollow-verbs"]),
  mawt_mm(), mi("مَلِكٍ", "malik-king", "«a king»", "«bir kralın»"),
  an_mudari("وَيُحْشَرَ", "hashara", "«and be gathered»", "«ve haşrolunmayı»", tags=["naib-al-fail"], hidden=None, wa=True, extra=" — مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ"),
  maa_z(), maa_mi("الْمُلُوكِ", "malik-king", "«the kings»", "«krallar»", punct=".", tags=["jam-taksir"])])
sen("s6", "Rather he liked to die the death of a servant and be gathered with the righteous.", "Bilakis bir kul ölümüyle ölmeyi ve salihlerle haşrolunmayı severdi.", [
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ وَاسْتِئْنَافٍ.", "«rather» — the particle of turning away (iḍrāb), opening a new sentence.", "«bilakis» — idrâb ve istînâf harfi."),
  kana_bare(), khabar_kana_mudari("يُحِبُّ", "ahabba", "«likes»", "«sever»", tags=["form-iv-verbs", "doubled-verbs"], extra="بِالضَّمَّةِ — وَاسْمُ كَانَ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ"),
  an_(obj_of="يُحِبُّ", en_of="«likes»", tr_of="«sever»"),
  an_mudari("يَمُوتَ", "mata-die", "«(that) he die»", "«ölmeyi»", tags=["hollow-verbs"]),
  mawt_mm(), mi("عَبْدٍ", "abd", "«a servant»", "«bir kulun»"),
  an_mudari("وَيُحْشَرَ", "hashara", "«and be gathered»", "«ve haşrolunmayı»", tags=["naib-al-fail"], hidden=None, wa=True, extra=" — مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ"),
  maa_z(), maa_mi("الصَّالِحِينَ", "salih", "«the righteous»", "«salihler»", punct=".", tags=["jam-mudhakkar-salim", "ism-fail"])])
sen("s7", "And Yūsuf's prayer was:", "Yusuf'un duası şuydu:", [
  kana(), tok("دُعَاءُ", "dua", "noun", [K, "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ — وَخَبَرُهَا الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ.", "«the prayer (of)» — kāna's ism, a muḍāf; its khabar is the quoted prayer that follows.", "«duası» — kâne'nin ismi, muzâf; haberi ardından gelen nakledilen duadır."),
  yusuf_mi(punct=":")])
sen("s8", "«My Lord, You have given me of the kingship and taught me of the interpretation of events — Creator of the heavens and the earth, You are my protector in this world and the hereafter; take me as a Muslim and join me with the righteous.» (Yūsuf 12:101)", "«Rabbim, bana hükümdarlıktan verdin ve bana olayların yorumunu öğrettin — göklerin ve yerin Yaratıcısı, dünyada ve ahirette benim velîm sensin; beni müslüman olarak vefat ettir ve beni salihlere kat.» (Yûsuf 12:101)", quran([
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا، وَهُوَ مُضَافٌ.", "«My Lord» — a vocative with its yā dropped, naṣb estimated before the dropped speaker's yāʾ; the kasra is its trace.", "«Rabbim» — nida harfi düşmüş münâdâ; nasbı, düşen mütekellim yâ'sından öncesinde takdîrî; kesre onun izidir."),
  qad_(),
  enc_2s("آتَيْتَنِي", "aataa", "«You have given me»", "«bana verdin»", tags=["form-iv-verbs", "naqis-verbs"]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ، فُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of» — the partitive min; its nūn given a fatḥa before the article.", "«-den (bir kısım)» — teb'îz için; nûnu fethalı."),
  majrur("الْمُلْكِ", "mulk", "«the kingship»", "«hükümdarlıktan»", "مِنْ"),
  enc_2s("وَعَلَّمْتَنِي", "allama", "«and taught me»", "«ve bana öğrettin»", tags=["form-ii-verbs", "atf-nasaq"], wa=True),
  min_(), majrur("تَأْوِيلِ", "tawil", "«the interpretation (of)»", "«yorumunu»", "مِنْ", mudaf=True),
  mi("الْأَحَادِيثِ", "hadith", "«events, sayings»", "«olayların, sözlerin»", punct="،"),
  tok("فَاطِرَ", "fatir", "noun", ["vocative-munada", "ism-fail", "idafa-definiteness"], "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ مَنْصُوبٌ بِالْفَتْحَةِ لِأَنَّهُ مُضَافٌ (وَقِيلَ: نَعْتٌ لِرَبِّ عَلَى الْمَحَلِّ).", "«Creator (of)» — a vocative with its yā dropped, naṣb by fatḥa because it is annexed (some read it as a naʿt of رَبِّ on the place).", "«Yaratıcısı» — nida harfi düşmüş münâdâ, muzâf olduğundan fetha ile mansub (bazıları mahallen rabbi'nin na'ti sayar)."),
  tok("السَّمٰوَاتِ", "samawat", "noun", ["idafa-definiteness", "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ (رُسِمَ بِالْأَلِفِ الْخَنْجَرِيَّةِ كَمَا فِي الْمُصْحَفِ).", "«the heavens» — the muḍāf ilayh; a sound feminine plural, written with the dagger alif as in the muṣḥaf.", "«göklerin» — muzâfun ileyh; cem'-i müennes sâlim, Mushaf'taki gibi hançer elifle yazılmış."),
  tok("وَالْأَرْضِ", "ard", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْأَرْضِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and the earth» — joined.", "«ve yerin» — ma'tûf.", segments=wa_("الْأَرْضِ", "ard", "noun")),
  tok("أَنْتَ", "anta", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«You» — the detached pronoun as mubtadaʾ.", "«Sen» — munfasıl zamir, mübtedâ."),
  tok("وَلِيِّي", "wali", "noun", ["mubtada-khabar", "ya-al-mutakallim", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my protector» — the khabar, the ḍamma estimated before the speaker's yāʾ; a muḍāf.", "«velîm» — haber, zamme mütekellim yâ'sından önce takdîrî; muzâf.", segments=[seg("وَلِيِّ", "wali", "noun"), seg("ي", "pron-1s", "pron")]),
  fi(), tok("الدُّنْيَا", "dunya", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ كَسْرَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ.", "«this world» — in jarr, the kasra estimated on the alif (a maqṣūr noun).", "«dünyada» — mecrur, kesre elif üzerinde takdîrî (maksûr isim)."),
  tok("وَالْآخِرَةِ", "akhira", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْآخِرَةِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and the hereafter» — joined.", "«ve ahirette» — ma'tûf.", segments=wa_("الْآخِرَةِ", "akhira", "noun")),
  enc_2s("تَوَفَّنِي", "tawaffa", "«take me (in death)»", "«beni vefat ettir»", tags=["form-v-verbs", "naqis-verbs"], amr=True, extra=" — حُذِفَتْ أَلِفُهُ لِلْبِنَاءِ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ"),
  hal_("مُسْلِمًا", "muslim", "«as a Muslim»", "«müslüman olarak»", tags=["ism-fail"]),
  enc_2s("وَأَلْحِقْنِي", "alhaqa", "«and join me»", "«ve beni kat»", tags=["form-iv-verbs", "atf-nasaq"], amr=True, wa=True),
  tok("بِالصَّالِحِينَ", "salih", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "الْبَاءُ حَرْفُ جَرٍّ، وَالصَّالِحِينَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«with the righteous» — in jarr by the yāʾ of the sound plural.", "«salihlere» — cem'-i müzekker sâlim, yâ ile mecrur.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الصَّالِحِينَ", "salih", "noun")])]))
sen("s9", "And Allah took him as a Muslim and joined him with his fathers Ibrāhīm, Isḥāq and Yaʿqūb — may Allah bless them and our Prophet, and grant peace.", "Allah onu müslüman olarak vefat ettirdi ve babaları İbrahim, İshak ve Yakub'a kattı — Allah onlara ve Peygamberimize salât ve selâm eylesin.", [
  verb_enc("وَتَوَفَّاهُ", "tawaffa", "هُ", "pron-3ms", "«took him (in death)»", "«onu vefat ettirdi»", tags=["form-v-verbs", "naqis-verbs"], hidden=None, wa=True, mudari=False, extra=" — وَالْفَاعِلُ مُتَأَخِّرٌ"),
  allah_fail(), hal_("مُسْلِمًا", "muslim", "«as a Muslim»", "«müslüman olarak»", tags=["ism-fail"]),
  verb_enc("وَأَلْحَقَهُ", "alhaqa", "هُ", "pron-3ms", "«and joined him»", "«ve onu kattı»", tags=["form-iv-verbs"], wa=True, mudari=False),
  tok("بِآبَائِهِ", "ab", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَآبَاءِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with his fathers» — in jarr; annexed to the pronoun.", "«babalarına» — mecrur; zamire muzâf.", segments=[seg("بِ", "bi", "prep"), seg("آبَاءِ", "ab", "noun"), seg("هِ", "pron-3ms", "pron")]),
  badal_("إِبْرَاهِيمَ", "ibrahim", "jarr", "«Ibrāhīm»", "«İbrahim»", extra=" — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", sign="الْفَتْحَةُ"),
  tok("وَإِسْحٰقَ", "ishaq", "propn", ["atf-nasaq", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَإِسْحٰقَ مَعْطُوفٌ عَلَى إِبْرَاهِيمَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (رُسِمَ بِالْأَلِفِ الْخَنْجَرِيَّةِ).", "«and Isḥāq» — joined; jarr by fatḥa, a diptote name (written with the dagger alif).", "«ve İshak» — ma'tûf; gayr-i munsarif, fetha ile mecrur (hançer elifle yazılmış).", segments=wa_("إِسْحٰقَ", "ishaq", "propn")),
  tok("وَيَعْقُوبَ", "yaqub", "propn", ["atf-nasaq", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَيَعْقُوبَ مَعْطُوفٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Yaʿqūb» — joined; jarr by fatḥa, a diptote.", "«ve Yakub» — ma'tûf; gayr-i munsarif, fetha ile mecrur.", segments=wa_("يَعْقُوبَ", "yaqub", "propn")),
  mazi("صَلَّى", "salla", "«may (Allah) bless»", "«salât eylesin»", hidden=None, tags=["naqis-verbs", "form-ii-verbs"], extra_ar=" — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ"),
  allah_fail(),
  tok("عَلَيْهِمْ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِصَلَّى.", "«upon them».", "«onlara».", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("وَعَلَى", "ala", "prep", ["atf-nasaq", "huruf-jarr"], "الْوَاوُ عَاطِفَةٌ، وَعَلَى حَرْفُ جَرٍّ.", "«and upon».", "«ve … üzerine».", segments=wa_("عَلَى", "ala", "prep")),
  tok("نَبِيِّنَا", "nabi", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Prophet» — in jarr; annexed to the pronoun.", "«Peygamberimize» — mecrur; zamire muzâf.", segments=[seg("نَبِيِّ", "nabi", "noun"), seg("نَا", "pron-1p", "pron")]),
  mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm eylesin»", hidden="هُوَ", wa=True, tags=["form-ii-verbs"], punct=".")])
# ---------------------------------------------------------------- glossary
NEW = {
 "naffadha": G("naffadha", "نَفَّذَ", "ن ف ذ", "verb", "to carry out, to execute (Form II)", "yerine getirmek, icra etmek (tef'îl bâbı)", 3, form="II"),
 "hashara": G("hashara", "حَشَرَ", "ح ش ر", "verb", "to gather, to raise up (for the Day of Gathering)", "haşretmek, toplamak", 3, form="I"),
 "fatir": G("fatir", "فَاطِر", "ف ط ر", "noun", "Creator, Originator (ism fāʿil of فَطَرَ; a name of Allah)", "Yaratan, yoktan var eden (fatara'nın ism-i fâili; Allah'ın adı)", 3),
 "akhira": G("akhira", "آخِرَة", "أ خ ر", "noun", "the hereafter, the last abode", "ahiret, son yurt", 1),
 "tawaffa": G("tawaffa", "تَوَفَّى", "و ف ي", "verb", "to take (a soul) in death (Form V; تَوَفَّاهُ اللهُ = Allah took him)", "vefat ettirmek, (ruhu) almak (tefa''ul bâbı)", 3, form="V"),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("shaghala", "شغل"), ("ghayyara", "غير"), ("hakama", "حكم"), ("adda-count", "عد"), ("mawt", "موت"), ("salih", "صالح"), ("dua", "دعاء"), ("hadith", "حديث"), ("wali", "ولي"), ("dunya", "دنيا"), ("alhaqa", "ألحق"), ("aataa", "آتى"), ("mulk", "ملك"), ("amr", "أمر"), ("hukm", "حكم")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm or _w == _lm, (_k, _e["lemma"])
assert GLOSS_ADD.get("adda-count", {}).get("pos") == "verb" and GLOSS_ADD.get("ghayyara", {}).get("pos") == "verb"
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("naffadha", "hashara", "tawaffa"): mo["verbs"].pop(_k, None)
put_morph(mo, "naffadha", _sg.derived("مِنْ بَابِ التَّفْعِيلِ", "فَعَّلَ يُفَعِّلُ", "ُ", "نَفَّذ", "نَفِّذ", "نَفِّذ", "تَنْفِيذ", "مُنَفِّذ", "مُنَفَّذ", "نُفِّذَ", "يُنَفَّذُ", note="مُتَعَدٍّ: نَفَّذَ الْأَمْرَ."))
put_morph(mo, "hashara", _sg.sound1("nasara", "حَشَر", "حْشُر", "اُحْشُر", "حَشْر", "حَاشِر", "مَحْشُور", "حُشِرَ", "يُحْشَرُ", note="مُتَعَدٍّ: حَشَرَ اللهُ النَّاسَ — حَشَرَ يَحْشُرُ (وَيَحْشِرُ)."))
put_morph(mo, "tawaffa", _sg.derived_naqis("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَوَفَّ", "تَوَفّ", "a", "تَوَفّ", "تَوَفٍّ (التَّوَفِّي)", "مُتَوَفٍّ (الْمُتَوَفِّي)", "مُتَوَفًّى (الْمُتَوَفَّى)", "تُوُفِّيَ", "يُتَوَفَّى", note="مُتَعَدٍّ: تَوَفَّى اللهُ فُلَانًا — نَاقِصٌ يَائِيٌّ مِنْ بَابِ التَّفَعُّلِ، مُضَارِعُهُ يَتَوَفَّى، وَأَمْرُهُ تَوَفَّ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 23 (print pp. 67–68, «أَحْسَنُ الْقَصَصِ» section 25 «حُسْنُ الْعَاقِبَة» — the last section of volume 1): Yūsuf's kingship does not distract him from Allah (s1–s6), his prayer with Yūsuf 12:101 (s7–s8, the aya marked; the print opens it with «وَكَانَ دُعَاءُ يُوسُفَ:» and closes it with a round bracket, which stands here as the closing guillemet), his death and the blessing on the prophets (s9). "
          "One printed line is one sentence; s4 ends as the print does, without a stop; the aya runs across the page break (pp. 67–68) and is set as one sentence. With this sentence volume 1 of the print is complete.")
ADD_TR = (" Yirmi üçüncü bölüm (basılı s. 67–68, «أَحْسَنُ الْقَصَصِ» 25. kısım «حُسْنُ الْعَاقِبَة» — birinci cildin son kısmı): Yusuf'un hükümdarlığı onu Allah'tan alıkoymaz (s1–s6), Yûsuf 12:101 ile duası (s7–s8, ayet işaretli; baskı onu «وَكَانَ دُعَاءُ يُوسُفَ:» ile açar ve yuvarlak parantezle kapatır, burada kapanış tırnağı olarak durur), vefatı ve peygamberlere salât (s9). "
          "Basılı her satır bir cümledir; s4 baskıdaki gibi noktasız biter; ayet sayfa sonunu aşar (s. 67–68) ve tek cümle olarak verilmiştir. Bu cümleyle baskının birinci cildi tamamlanmıştır.")
write_out(23, S, TITLE, ADD_EN, ADD_TR, "pp. 67–68", GLOSS_ADD)
report(23, S, GLOSS_ADD, ())
