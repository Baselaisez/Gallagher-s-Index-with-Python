# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 12: «مَوْعِظَةُ السِّجْنِ» — «أَحْسَنُ الْقَصَصِ» section 9 (print pp. 38–41):
Yūsuf in the prison, loved and honoured; the two men and their dreams (Yūsuf 12:36 in the print's two lines); the people of
his time and their many lords; the sermon's four questions; the two «but he was» sentences; the prophets proclaim the truth.
Every printed line is one sentence, split at the print's own full stops; the vowelling is the print's.
python3 tools/authoring/author_qisas_ch12.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "مَوْعِظَةُ السِّجْنِ", "en": "The sermon of the prison", "tr": "Zindan vaazı"}
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

# ================================================================ §9 موعظة السجن (pp. 38–41)
sen("s1", "And Yūsuf entered the prison, and all the people of the prison came to know that Yūsuf was a noble young man.", "Yusuf zindana girdi; zindan ehlinin hepsi Yusuf'un soylu bir genç olduğunu anladı.", [
  mazi("وَدَخَلَ", "dakhala", "«and entered»", "«ve girdi»", hidden=None, wa=True), yusuf_fail(), maful("السِّجْنَ", "sijn", "«the prison»", "«zindana»", punct="،"),
  mazi("وَعَرَفَ", "arafa", "«and came to know»", "«ve anladı»", hidden=None, wa=True, tags=["atf-nasaq"]), *ahl_sijn("فَاعِلٌ", "the doer", "fâil"),
  tok("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (وَقِيلَ: تَوْكِيدٌ).", "«all of them» — the ḥāl (some read it as a tawkīd).", "«hepsi» — hâl (te'kid de denmiştir)."),
  anna(obj_of="عَرَفَ"), name_ism_anna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  khabar_inna("شَابٌّ", "shabb", "«a young man»", "«bir genç»", part="أَنَّ"), nat_raf("كَرِيمٌ", "karim", "«noble»", "«soylu»", punct=".")])
sen("s2", "And that Yūsuf had a great knowledge.", "Ve Yusuf'un yanında büyük bir ilim olduğunu.", [
  anna(wa=True, obj_of="عَرَفَ"), name_ism_anna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  tok("عِنْدَهُ", "inda", "noun", ["maful-fih", "idafa-definiteness", "mubtada-khabar"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«with him» — the adverb with its pronoun: the fronted khabar; the nominal clause is anna's khabar.", "«yanında» — zarf ve zamiri: öne alınmış haber; isim cümlesi enne'nin haberi.", segments=[seg("عِنْدَ", "inda", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("عِلْمٌ", "ilm", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a knowledge» — the delayed mubtadaʾ.", "«bir ilim» — geciktirilmiş mübtedâ."),
  nat_raf("عَظِيمٌ", "azim", "«great»", "«büyük»", punct=".")])
sen("s3", "And that in Yūsuf's breast was a merciful heart.", "Ve Yusuf'un göğsünde merhametli bir kalp olduğunu.", [
  anna(wa=True, obj_of="عَرَفَ"), name_ism_anna("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"),
  tok("فِي", "fi", "prep", ["huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«in» — the phrase is the fronted khabar; the nominal clause is anna's khabar.", "«-de» — şibh-i cümle öne alınmış haber; isim cümlesi enne'nin haberi."),
  mudaf_pron("صَدْرِهِ", "sadr", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his breast» — in jarr", "«göğsü» — mecrur", tags=["huruf-jarr"]),
  tok("قَلْبٌ", "qalb", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a heart» — the delayed mubtadaʾ.", "«bir kalp» — geciktirilmiş mübtedâ."),
  nat_raf("رَحِيمٌ", "rahim", "«merciful»", "«merhametli»", punct=".")])
sen("s4", "And the people of the prison loved Yūsuf and honoured him.", "Zindan ehli Yusuf'u sevdi ve ona ikram etti.", [
  mazi("وَأَحَبَّ", "ahabba", "«and loved»", "«ve sevdi»", hidden=None, wa=True, tags=["form-iv-verbs"]), *ahl_sijn("فَاعِلٌ", "the doer", "fâil"),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  mazi_pl_enc("وَأَكْرَمُوهُ", "akrama", "هُ", "pron-3ms", "«and they honoured him»", "«ve ona ikram ettiler»", wa=True, tags=["atf-nasaq", "form-iv-verbs"], punct=".")])
sen("s5", "And the people rejoiced in Yūsuf and held him in honour.", "İnsanlar Yusuf'a sevindi ve onu yücelttiler.", [
  mazi("وَفَرِحَ", "fariha", "«and rejoiced»", "«ve sevindi»", hidden=None, wa=True), nas_fail(),
  tok("بِيُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "الْبَاءُ حَرْفُ جَرٍّ، وَيُوسُفَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«in Yūsuf» — the diptote's jarr shows as a fatḥa.", "«Yusuf'a» — gayr-i munsarıfın ceri fetha ile.", segments=[seg("بِ", "bi", "prep"), seg("يُوسُفَ", "yusuf", "propn")]),
  mazi_pl_enc("وَعَظَّمُوهُ", "azzama", "هُ", "pron-3ms", "«and they held him in honour»", "«ve onu yücelttiler»", wa=True, tags=["atf-nasaq", "form-ii-verbs"], punct=".")])
sen("s6", "And two men entered the prison with him, and told him their dreams.", "Onunla birlikte zindana iki adam girdi ve ona rüyalarını anlattılar.", [
  mazi("وَدَخَلَ", "dakhala", "«and entered»", "«ve girdi»", hidden=None, wa=True), maa_pron("مَعَهُ", "هُ", "pron-3ms", "«with him»", "«onunla»"),
  maful("السِّجْنَ", "sijn", "«the prison»", "«zindana»"),
  tok("رَجُلَانِ", "rajul", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى.", "«two men» — the delayed doer; the dual's rafʿ shows as an alif.", "«iki adam» — geciktirilmiş fâil; tesniyenin refi elif ile."),
  dual_mazi("وَقَصَّا", "qassa", "«and the two told»", "«ve ikisi anlattı»", tags=["atf-nasaq", "doubled-verbs"]),
  tok("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِقَصَّا.", "«to him».", "«ona».", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")]),
  mudaf_pron("رُؤْيَاهُمَا", "ruya-dream", "هُمَا", "pron-3d", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", "«their (two) dreams» — the object, its fatḥa estimated on the alif", "«rüyalarını» — mef'ûl, fethası elif üzerinde takdîrî", tags=["maful-bihi", "ism-maqsur-manqus"], punct=".")])
sen("s7", "«And one of the two said: I see myself pressing wine.» (Yūsuf 12:36)", "«İkisinden biri dedi: Ben rüyamda kendimi şarap sıkarken görüyorum.» (Yûsuf 12:36)", quran([
  qala(wa=True, punct=None, hidden=None),
  mudaf_pron("أَحَدُهُمَا", "ahad", "هُمَا", "pron-3d", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "«one of the two» — the doer", "«ikisinden biri» — fâil", tags=["fail"]),
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the nūn of protection and the speaker's yāʾ as its ism.", "«şüphesiz ben» — inne; vikâye nûnu ve mütekellim yâ'sı ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("نِي", "pron-1s", "pron")]),
  tok("أَرَانِي", "raa", "verb", ["inna-wa-akhawatuha", "mudari-marfu", "ya-al-mutakallim", "maful-bihi", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«I see myself» — the dream-verb «see» with the speaker's yāʾ as its first object; the clause is inna's khabar.", "«kendimi görüyorum» — rüya fiili «görmek», mütekellim yâ'sı birinci mef'ûlü; cümle inne'nin haberi.", segments=[seg("أَرَا", "raa", "verb"), seg("نِي", "pron-1s", "pron")]),
  mudari_1s("أَعْصِرُ", "asara", "«I press»", "«sıkıyorum»", extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِأَرَى"),
  maful("خَمْرًا", "khamr", "«wine»", "«şarap»", punct=".")]))
sen("s8", "«And the other said: I see myself carrying bread on my head, of which the birds eat.» (Yūsuf 12:36)", "«Öteki dedi: Ben rüyamda başımın üstünde ekmek taşıdığımı, kuşların ondan yediğini görüyorum.» (Yûsuf 12:36)", quran([
  qala(wa=True, punct=None, hidden=None),
  tok("الْآخَرُ", "akhar", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the other» — the doer.", "«öteki» — fâil."),
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the nūn of protection and the speaker's yāʾ as its ism.", "«şüphesiz ben» — inne; vikâye nûnu ve mütekellim yâ'sı ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("نِي", "pron-1s", "pron")]),
  tok("أَرَانِي", "raa", "verb", ["inna-wa-akhawatuha", "mudari-marfu", "ya-al-mutakallim", "maful-bihi", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«I see myself» — the dream-verb «see» with the speaker's yāʾ as its first object; the clause is inna's khabar.", "«kendimi görüyorum» — rüya fiili «görmek», mütekellim yâ'sı birinci mef'ûlü; cümle inne'nin haberi.", segments=[seg("أَرَا", "raa", "verb"), seg("نِي", "pron-1s", "pron")]),
  mudari_1s("أَحْمِلُ", "hamala", "«I carry»", "«taşıyorum»", extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِأَرَى"),
  tok("فَوْقَ", "fawqa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«on top of» — an adverb of place; a muḍāf.", "«üstünde» — mekân zarfı; muzâf."),
  tok("رَأْسِي", "ras", "noun", ["idafa-definiteness", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my head» — the muḍāf ilayh, its kasra estimated before the speaker's yāʾ.", "«başımın» — muzâfun ileyh; kesresi mütekellim yâ'sından önce takdîrî.", segments=[seg("رَأْسِ", "ras", "noun"), seg("ي", "pron-1s", "pron")]),
  maful("خُبْزًا", "khubz", "«bread»", "«ekmek»"),
  tok("تَأْكُلُ", "akala", "verb", ["mudari-marfu", "naat-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِخُبْزًا.", "«eat» — the clause describes the bread (a naʿt clause).", "«yer» — cümle ekmeğin sıfatı."),
  fail("الطَّيْرُ", "tayr", "«the birds»", "«kuşlar»"),
  tok("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِتَأْكُلُ.", "«of it».", "«ondan».", punct=".", segments=[seg("مِنْ", "min", "prep"), seg("هُ", "pron-3ms", "pron")])]))
sen("s9", "And the two asked Yūsuf about the interpretation.", "İkisi Yusuf'a tabirini sordu.", [
  dual_mazi("وَسَأَلَا", "saala", "«and the two asked»", "«ve ikisi sordu»"), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'a»"),
  tok("عَنِ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَكُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«about» — its nūn takes a kasra before the article.", "«hakkında» — nûnu iki sâkin karşılaşınca kesre aldı."),
  majrur("التَّأْوِيلِ", "tawil", "«the interpretation»", "«tabir»", "عَنْ", punct=".")])
sen("s10", "And Yūsuf was learned in the interpretation of dreams.", "Yusuf rüya tabirini bilen biriydi.", [
  kana(), yusuf_ism_kana(), khabar_kana("عَالِمًا", "alim-scholar", "«learned»", "«bilen»", tags=["ism-fail"]),
  tok("بِتَأْوِيلِ", "tawil", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَتَأْوِيلِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِعَالِمًا.", "«in the interpretation (of)» — a muḍāf, hanging on «learned».", "«tabirini» — muzâf; «bilen»e bağlı.", segments=[seg("بِ", "bi", "prep"), seg("تَأْوِيلِ", "tawil", "noun")]),
  tok("الرُّؤْيَا", "ruya-dream", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«dreams» — the muḍāf ilayh, its kasra estimated on the alif.", "«rüyanın» — muzâfun ileyh; kesresi elif üzerinde takdîrî.", punct=".")])
sen("s11", "And Yūsuf was a prophet among the prophets.", "Yusuf peygamberlerden bir peygamberdi.", [
  kana(), yusuf_ism_kana(), khabar_kana("نَبِيًّا", "nabi", "«a prophet»", "«bir peygamber»"),
  min_(full="مِنَ"), tok("الْأَنْبِيَاءِ", "nabi", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ (مَمْنُوعٌ مِنَ الصَّرْفِ، وَإِنَّمَا جُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُعَرَّفٌ بِأَل).", "«the prophets» — a diptote plural that takes the kasra because the article defines it.", "«peygamberler» — gayr-i munsarıf çoğul; harf-i tarif aldığı için kesre ile mecrur.", punct=".")])
sen("s12", "And the people in his time used to worship other than Allah.", "Onun zamanında insanlar Allah'tan başkasına tapıyorlardı.", [
  kana(), tok("النَّاسُ", "nas", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — kāna's ism.", "«insanlar» — kâne'nin ismi."),
  fi(), mudaf_pron("زَمَانِهِ", "zaman", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his time» — in jarr", "«zamanı» — mecrur", tags=["huruf-jarr"]),
  khamsa("يَعْبُدُونَ", "abada", "«used to worship»", "«tapıyorlardı»", tags=[K], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  tok("غَيْرَ", "ghayr", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«other than» — the object; a muḍāf.", "«başkası» — mef'ûl; muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh.", punct=".")])
sen("s13", "And they set up many lords from their own selves.", "Kendi kendilerine pek çok rab uydurdular.", [
  mazi_pl("وَوَضَعُوا", "wadaa", "«and they set up»", "«ve koydular»", wa=True, tags=["mithal-verbs"]),
  maful("أَرْبَابًا", "rabb", "«lords»", "«rabler»", tags=["jam-taksir"]), nat_nasb("كَثِيرَةً", "kathir", "«many»", "«pek çok»"),
  min_(), tok("عِنْدِ", "inda", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ — الظَّرْفُ يُجَرُّ بِمِنْ.", "«from (the side of)» — the adverb ʿinda is itself put in jarr by min; a muḍāf.", "«yanından» — zarf, min ile mecrur; muzâf."),
  mudaf_pron("أَنْفُسِهِمْ", "nafs", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "«their own selves» — the muḍāf ilayh", "«kendileri» — muzâfun ileyh", tags=["jam-taksir"], punct=".")])
sen("s14", "And they said: this is the lord of the land, and this is the lord of the sea, and this is the lord of provision, and this is the lord of the rain.", "Dediler: bu karanın rabbi, bu denizin rabbi, bu rızkın rabbi, bu da yağmurun rabbi.", [
  qalu(wa=True),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"), tok("رَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the lord (of)» — the khabar; a muḍāf.", "«rabbi» — haber; muzâf."), tok("الْبَرِّ", "barr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the land» — the muḍāf ilayh.", "«kara» — muzâfun ileyh.", punct="،"),
  tok("وَهٰذَا", "hadha", "pron", ["asma-al-ishara", "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — a demonstrative, the mubtadaʾ.", "«ve bu» — ism-i işâret, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هٰذَا", "hadha", "pron")]), tok("رَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the lord (of)» — the khabar; a muḍāf.", "«rabbi» — haber; muzâf."), tok("الْبَحْرِ", "bahr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the sea» — the muḍāf ilayh.", "«deniz» — muzâfun ileyh.", punct="،"),
  tok("وَهٰذَا", "hadha", "pron", ["asma-al-ishara", "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — a demonstrative, the mubtadaʾ.", "«ve bu» — ism-i işâret, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هٰذَا", "hadha", "pron")]), tok("رَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the lord (of)» — the khabar; a muḍāf.", "«rabbi» — haber; muzâf."), tok("الرِّزْقِ", "rizq", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«provision» — the muḍāf ilayh.", "«rızık» — muzâfun ileyh.", punct="،"),
  tok("وَهٰذَا", "hadha", "pron", ["asma-al-ishara", "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — a demonstrative, the mubtadaʾ.", "«ve bu» — ism-i işâret, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هٰذَا", "hadha", "pron")]), tok("رَبُّ", "rabb", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the lord (of)» — the khabar; a muḍāf.", "«rabbi» — haber; muzâf."), tok("الْمَطَرِ", "matar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the rain» — the muḍāf ilayh.", "«yağmur» — muzâfun ileyh.", punct=".")])
sen("s15", "And Yūsuf used to see all of that and laugh.", "Yusuf bütün bunları görür ve gülerdi.", [
  kana(), yusuf_ism_kana(), khabar_kana_mudari("يَرَى", "raa", "«used to see»", "«görürdü»", extra="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", tags=["naqis-verbs"]),
  tok("كُلَّ", "kull", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«all (of)» — the object; a muḍāf.", "«bütün» — mef'ûl; muzâf."),
  ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«bunları»", tags=["idafa-definiteness"]),
  tok("وَيَضْحَكُ", "dahika", "verb", ["atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَضْحَكُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — مَعْطُوفٌ عَلَى يَرَى.", "«and laugh» — joined onto «see».", "«ve güler» — «görür»e matuf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَضْحَكُ", "dahika", "verb")])])
sen("s16", "And Yūsuf used to know all of that and weep.", "Yusuf bütün bunları bilir ve ağlardı.", [
  kana(), yusuf_ism_kana(), khabar_kana_mudari("يَعْلَمُ", "alima", "«used to know»", "«bilirdi»"),
  tok("كُلَّ", "kull", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«all (of)» — the object; a muḍāf.", "«bütün» — mef'ûl; muzâf."),
  ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«bunları»", tags=["idafa-definiteness"]),
  tok("وَيَبْكِي", "baka", "verb", ["atf-nasaq", "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَبْكِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — مَعْطُوفٌ عَلَى يَعْلَمُ.", "«and weep» — its ḍamma estimated on the yāʾ; joined onto «know».", "«ve ağlar» — zammesi yâ üzerinde takdîrî; «bilir»e matuf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَبْكِي", "baka", "verb")])])
sen("s17", "And Yūsuf wanted to call them to Allah.", "Yusuf onları Allah'a davet etmek istiyordu.", [
  kana(), yusuf_ism_kana(), khabar_kana_mudari("يُرِيدُ", "arada", "«wanted»", "«istiyordu»", tags=["hollow-verbs", "form-iv-verbs"]),
  an_(obj_of="يُرِيدُ", en_of="«wanted»", tr_of="«istiyordu»"),
  mansub_enc("يَدْعُوَهُمْ", "daa", "هُمْ", "pron-3mp", "«to call them»", "«onları davet etmek»", tags=["naqis-verbs"]),
  ila(), majrur("اللهِ", "allah", "«Allah»", "«Allah»", "إِلَى", punct=".")])
sen("s18", "And Allah had willed that this should be in the prison.", "Allah bunun zindanda olmasını dilemişti.", [
  tok("وَقَدْ", "qad", "part", ["qad-harf", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — the confirming qad.", "«ve gerçekten» — tahkik harfi kad.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("أَرَادَ", "arada", "«willed»", "«diledi»", hidden=None, tags=["hollow-verbs", "form-iv-verbs"]), allah_fail(),
  an_(obj_of="أَرَادَ", en_of="«willed»", tr_of="«diledi»"),
  tok("يَكُونَ", "kana", "verb", ["an-masdariyya", K, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«should be» — kāna's muḍāriʿ in naṣb after an.", "«olması» — kâne'nin muzarisi, en ile mansub."),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", K], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُونَ.", "«that» — the demonstrative, the ism of yakūna.", "«bu» — ism-i işâret, yekûne'nin ismi."),
  *fi_sijn_khabar(punct=".", of="يَكُونَ")])
sen("s19", "Do the people of the prison not deserve the sermon?", "Zindan ehli vaazı hak etmez mi?", [
  ala_q(), tok("يَسْتَحِقُّ", "istahaqqa", "verb", ["mudari-marfu", "form-x-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«deserve» — a muḍāriʿ in rafʿ.", "«hak eder» — merfû muzari."),
  *ahl_sijn("فَاعِلٌ", "the doer", "fâil"), maful("الْمَوْعِظَةَ", "mawiza", "«the sermon»", "«vaazı»", punct="؟")])
sen("s20", "Do the people of the prison not deserve mercy?", "Zindan ehli merhameti hak etmez mi?", [
  ala_q(), tok("يَسْتَحِقُّ", "istahaqqa", "verb", ["mudari-marfu", "form-x-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«deserve» — a muḍāriʿ in rafʿ.", "«hak eder» — merfû muzari."),
  *ahl_sijn("فَاعِلٌ", "the doer", "fâil"), maful("الرَّحْمَةَ", "rahma", "«mercy»", "«merhameti»", punct="؟")])
sen("s21", "Are the people of the prison not the servants of Allah?", "Zindan ehli Allah'ın kulları değil mi?", [
  alaysa(), *ahl_sijn("اسْمُ لَيْسَ", "the ism of laysa", "leyse'nin ismi"),
  tok("عِبَادَ", "ibad", "noun", [K, "idafa-definiteness", "jam-taksir"], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the servants (of)» — laysa's khabar; a muḍāf.", "«kulları» — leyse'nin haberi; muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah» — muzâfun ileyh.", punct="؟")])
sen("s22", "Are the people of the prison not the children of Adam?", "Zindan ehli Âdemoğulları değil mi?", [
  alaysa(), *ahl_sijn("اسْمُ لَيْسَ", "the ism of laysa", "leyse'nin ismi"),
  tok("بَنِي", "banu", "noun", [K, "idafa-definiteness", "jam-mudhakkar-salim"], "خَبَرُ لَيْسَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَهُوَ مُضَافٌ.", "«the sons (of)» — laysa's khabar; naṣb by the yāʾ (attached to the sound plural), the nūn dropped for the idafa.", "«oğulları» — leyse'nin haberi; nasbı yâ ile (sâlim çoğula mülhak), nûnu izâfet için düşmüş.", segments=[seg("بَنِي", "banu", "noun")]),
  tok("آدَمَ", "aadam", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Adam» — the muḍāf ilayh; a diptote, its jarr a fatḥa.", "«Âdem» — muzâfun ileyh; gayr-i munsarıf, ceri fetha.", punct="؟")])
sen("s23", "Yūsuf was in the prison, but he was free and bold.", "Yusuf zindandaydı, fakat o hür ve cesurdu.", [
  kana_bare(), yusuf_ism_kana(), *fi_sijn_khabar(), lakinnahu(), kana_khabar_lakinna(),
  khabar_kana("حُرًّا", "hurr", "«free»", "«hür»"), khabar_kana("جَرِيئًا", "jari-bold", "«bold»", "«cesur»", second=True, punct=".")])
sen("s24", "Yūsuf was poor, but he was open-handed and generous.", "Yusuf fakirdi, fakat o cömert ve eli açıktı.", [
  kana_bare(), yusuf_ism_kana(), khabar_kana("فَقِيرًا", "faqir", "«poor»", "«fakir»"), lakinnahu(), kana_khabar_lakinna(),
  khabar_kana("جَوَادًا", "jawad", "«open-handed»", "«cömert»"), khabar_kana("سَخِيًّا", "sakhi", "«generous»", "«eli açık»", second=True, punct=".")])
sen("s25", "Indeed the prophets proclaim the truth in every place.", "Şüphesiz peygamberler hakkı her yerde açıkça söylerler.", [
  inna(), tok("الْأَنْبِيَاءَ", "nabi", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the prophets» — the ism of inna.", "«peygamberler» — inne'nin ismi."),
  khamsa("يَجْهَرُونَ", "jahara", "«proclaim»", "«açıkça söylerler»", tags=["inna-wa-akhawatuha"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("بِالْحَقِّ", "haqq", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَقِّ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِيَجْهَرُونَ.", "«the truth» — in jarr after the bāʾ.", "«hakkı» — bâ ile mecrur.", segments=[seg("بِ", "bi", "prep"), seg("الْحَقِّ", "haqq", "noun")]),
  fi(), *kulli_("مَكَانٍ", "makan", "«place»", "«yer»", punct=".")])
sen("s26", "Indeed the prophets give freely of good in every age.", "Şüphesiz peygamberler her zamanda hayrı bol bol verirler.", [
  inna(), tok("الْأَنْبِيَاءَ", "nabi", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the prophets» — the ism of inna.", "«peygamberler» — inne'nin ismi."),
  khamsa("يَجُودُونَ", "jada", "«give freely»", "«bol bol verirler»", tags=["inna-wa-akhawatuha", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("بِالْخَيْرِ", "khayr", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْخَيْرِ مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِيَجُودُونَ.", "«of good» — in jarr after the bāʾ.", "«hayrı» — bâ ile mecrur.", segments=[seg("بِ", "bi", "prep"), seg("الْخَيْرِ", "khayr", "noun")]),
  fi(), *kulli_("زَمَانٍ", "zaman", "«age»", "«zaman»", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "rahim": G("rahim", "رَحِيم", "ر ح م", "noun", "merciful, compassionate (ṣifa mushabbaha)", "merhametli (sıfat-ı müşebbehe)", 1, plural="رُحَمَاء"),
 "khubz": G("khubz", "خُبْز", "خ ب ز", "noun", "bread", "ekmek", 1),
 "matar": G("matar", "مَطَر", "م ط ر", "noun", "rain", "yağmur", 1, plural="أَمْطَار"),
 "istahaqqa": G("istahaqqa", "اِسْتَحَقَّ", "ح ق ق", "verb", "to deserve, to be entitled to", "hak etmek, lâyık olmak", 2, form="X"),
 "mawiza": G("mawiza", "مَوْعِظَة", "و ع ظ", "noun", "a sermon, an admonition", "vaaz, öğüt", 2, plural="مَوَاعِظ"),
 "hurr": G("hurr", "حُرّ", "ح ر ر", "noun", "free (not a slave; of a free spirit)", "hür, özgür", 1, plural="أَحْرَار"),
 "jari-bold": G("jari-bold", "جَرِيء", "ج ر أ", "noun", "bold, daring (ṣifa mushabbaha)", "cesur, yürekli (sıfat-ı müşebbehe)", 2, plural="جُرَآء"),
 "faqir": G("faqir", "فَقِير", "ف ق ر", "noun", "poor (ṣifa mushabbaha)", "fakir (sıfat-ı müşebbehe)", 1, plural="فُقَرَاء"),
 "sakhi": G("sakhi", "سَخِيّ", "س خ و", "noun", "generous, open-handed", "cömert, eli açık", 2, plural="أَسْخِيَاء"),
 "jahara": G("jahara", "جَهَرَ", "ج ه ر", "verb", "to proclaim aloud, to declare openly (جَهَرَ بِ)", "açıkça söylemek, ilan etmek (cehera bi)", 2, form="I"),
 "jada": G("jada", "جَادَ", "ج و د", "verb", "to be generous, to give freely (جَادَ بِ)", "cömert davranmak, bol bol vermek (câde bi)", 2, form="I"),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("ahl", "أهل"), ("azim", "عظيم"), ("sadr", "صدر"), ("azzama", "عظم"), ("qassa", "قص"), ("asara", "عصر"), ("khamr", "خمر"), ("hamala", "حمل"), ("fawqa", "فوق"), ("ras", "رأس"), ("tayr", "طير"), ("tawil", "تأويل"), ("alim-scholar", "عالم"), ("zaman", "زمان"), ("ghayr", "غير"), ("barr", "بر"), ("bahr", "بحر"), ("rizq", "رزق"), ("dahika", "ضحك"), ("rahma", "رحمة"), ("ibad", "عباد"), ("banu", "بنون"), ("aadam", "آدم"), ("jawad", "جواد"), ("haqq", "حق"), ("makan", "مكان"), ("khayr", "خير"), ("pron-3md", "ا"), ("pron-1s", "ي")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "").replace("ـ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("istahaqqa", "jahara", "jada"): mo["verbs"].pop(_k, None)
put_morph(mo, "istahaqqa", _sg.entry("مِنْ بَابِ الِاسْتِفْعَالِ — مُضَعَّفٌ", "اِسْتَفْعَلَ يَسْتَفْعِلُ", "اِسْتِحْقَاق", "مُسْتَحِقّ",
                                     _sg.mazi14("اِسْتَحَقّ", "اِسْتَحْقَق"), _sg.mudari14("َ", "سْتَحِقّ", "سْتَحْقِق"), ["اِسْتَحِقَّ", "اِسْتَحِقَّا", "اِسْتَحِقُّوا", "اِسْتَحِقِّي", "اِسْتَحِقَّا", "اِسْتَحْقِقْنَ"],
                                     "يَسْتَحِقَّ", "يَسْتَحِقَّ", "تَسْتَحِقَّ", "مُسْتَحَقّ", "اُسْتُحِقَّ", "يُسْتَحَقُّ", note="مُتَعَدٍّ — مُضَعَّفٌ مِنْ بَابِ الِاسْتِفْعَالِ: الْمِثْلَانِ يُدْغَمَانِ حَيْثُ تَحَرَّكَ الثَّانِي (اِسْتَحَقَّ) وَيُفَكَّانِ أَمَامَ السَّاكِنِ (اِسْتَحْقَقْتُ)؛ الْجَزْمُ بِالْفَتْحِ."))
put_morph(mo, "jahara", _sg.sound1("fataha", "جَهَر", "جْهَر", "اِجْهَر", "جَهْر", "جَاهِر", "مَجْهُور", "جُهِرَ", "يُجْهَرُ", note="يَتَعَدَّى بِالْبَاءِ: جَهَرَ بِالْحَقِّ — حَلْقِيُّ الْعَيْنِ فَبَابُهُ فَتَحَ."))
put_morph(mo, "jada", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "جَاد", "جُد", "جُود", "جُد", "جُود", "جُد", "جُود", "جَائِد", note="لَازِمٌ، يَتَعَدَّى بِالْبَاءِ: جَادَ بِالْخَيْرِ — جَادَ يَجُودُ، جُدْتُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 12 (print pp. 38–41, «أَحْسَنُ الْقَصَصِ» section 9 «مَوْعِظَةُ السِّجْن»): Yūsuf in the prison, loved and honoured; the two men and their dreams — Yūsuf 12:36 as the print sets it in two parenthesised lines (s7, s8, marked); the people of his time and their invented lords; the sermon's four questions; the two «but he was» sentences; the prophets proclaim the truth. "
          "One printed line is one sentence; s6 is given the full stop the print lacks at the page break; s14 joins the print's saying verb to the speech after an editorial colon; the print's parentheses around the aya are read as quotation marks.")
ADD_TR = (" On ikinci bölüm (basılı s. 38–41, «أَحْسَنُ الْقَصَصِ» 9. kısım «مَوْعِظَةُ السِّجْن»): zindanda sevilen ve ikram gören Yusuf; iki adam ve rüyaları — Yûsuf 12:36 baskının parantez içindeki iki satırıyla (s7, s8, işaretli); zamanının insanları ve uydurdukları rabler; vaazın dört sorusu; iki «fakat o … idi» cümlesi; peygamberler hakkı açıkça söyler. "
          "Basılı her satır bir cümledir; s6'ya baskının sayfa sonunda bıraktığı nokta eklenmiştir; s14 baskının söyleme fiilini editöryal bir iki noktadan sonraki sözle birleştirir; baskının âyeti saran parantezleri tırnak olarak okunmuştur.")
write_out(12, S, TITLE, ADD_EN, ADD_TR, "pp. 38–41", GLOSS_ADD)
report(12, S, GLOSS_ADD, ())
