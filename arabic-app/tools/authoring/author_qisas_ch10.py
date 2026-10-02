# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 10: «أَمَامَ يَعْقُوبَ، وَيُوسُفُ فِي الْبِئْرِ» — «أَحْسَنُ الْقَصَصِ» sections 5–6 (print pp. 34–36):
the brothers before Yaʿqūb with Yūsuf 12:16, 12:17 and 12:18 as the print sets them (marked), the whole shirt, the fine patience;
Yūsuf in the well at night. Every printed line is one sentence, split at
the print's own full stops; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch10.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "أَمَامَ يَعْقُوبَ، وَيُوسُفُ فِي الْبِئْرِ", "en": "Before Yaʿqūb, and Yūsuf in the well", "tr": "Yakub'un önünde, ve Yusuf kuyuda"}
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


def ikhwan_fail(punct=None): return ikhwa("الْإِخْوَانُ", "raf", "فَاعِلٌ", "«the brothers» — the doer (the other plural of أَخ)", "«kardeşler» — fâil («kardeş»in diğer cem'i)", tags=["fail"], punct=punct)
def kana_khabar_jarr(full, lex, en, tr, prep, punct=None, tags=()):
    return tok(full, lex, "noun", [K, "huruf-jarr"] + list(tags), f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — in jarr; the phrase is kāna's khabar.", tr + " — mecrur; şibh-i cümle kâne'nin haberi.", punct=punct)
def mazi_pl_naqis(full, lex, en, tr, tags=(), punct=None, wa=False):
    return tok(full, lex, "verb", ["naqis-verbs"] + list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ.", Wen(wa) + en + " — a nāqiṣ māḍī: its alif dropped before the group's wāw.", Wtr(wa) + tr + " — nâkıs mâzî: elifi cemi vâvından önce düşmüş.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def fa_mazi(full, lex, en, tr, hidden="هُوَ", tags=(), punct=None, extra_ar=""):
    t = mazi(full, lex, en, tr, hidden=hidden, tags=["atf-nasaq"] + list(tags), punct=punct, extra_ar=extra_ar)
    t["segments"] = [seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")]; t["irab"]["ar"] = "الْفَاءُ عَاطِفَةٌ، وَ" + t["irab"]["ar"]; t["irab"]["en"] = "«and so» + " + t["irab"]["en"]; t["irab"]["tr"] = "«böylece» + " + t["irab"]["tr"]
    return t

# ================================================================ §5 أمام يعقوب (pp. 34–35)
sen("s1", "«And they came to their father at nightfall, weeping.» (Yūsuf 12:16)", "«Ve akşamleyin ağlayarak babalarına geldiler.» (Yûsuf 12:16)", quran([
  tok("وَجَاؤُوا", "jaa", "verb", ["anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَجَاؤُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.", "«and they came» — a māḍī with the group's wāw as doer.", "«ve geldiler» — cemi vâvı fâil.", segments=[seg("وَ", "wa", "conj"), seg("جَاؤُوا", "jaa", "verb")]),
  tok("أَبَاهُمْ", "ab", "noun", ["maful-bihi", "five-nouns", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْأَلِفُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their father» — the object, naṣb by the alif of the five nouns.", "«babalarına» — mef'ûl, beş isimden olduğu için elif ile mansub.", segments=[seg("أَبَا", "ab", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("عِشَاءً", "isha-evening", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«at nightfall» — an adverb of time.", "«akşamleyin» — zaman zarfı."),
  khamsa("يَبْكُونَ", "baka", "«weeping»", "«ağlayarak»", tags=["hal", "naqis-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", punct=".")]))
sen("s2", "«They said: O our father, we went racing one another and left Yūsuf with our things, and the wolf ate him.» (Yūsuf 12:17)", "«Dediler: Ey babamız, biz yarışmaya gittik ve Yusuf'u eşyamızın yanında bıraktık; onu kurt yedi.» (Yûsuf 12:17)", quran([
  qalu(punct=None), *ya_abana(),
  tok("إِنَّا", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed we» — inna with the attached «we» as its ism.", "«şüphesiz biz» — inne; bitişik «biz» ismidir.", segments=[seg("إِنَّ", "inna", "part"), seg("نَا", "pron-1p", "pron")]),
  tok("ذَهَبْنَا", "dhahaba", "verb", ["inna-wa-akhawatuha"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«we went» — a māḍī built on sukūn before «we»; the clause is inna's khabar.", "«gittik» — «biz» ile sükûn üzere mebnî; cümle inne'nin haberi."),
  mudari("نَسْتَبِقُ", "istabaqa", "«racing one another»", "«yarışarak»", hidden="نَحْنُ", tags=["hal", "form-viii-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  tok("وَتَرَكْنَا", "taraka", "verb", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَتَرَكْنَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«and we left» — joined; «we» the doer.", "«ve bıraktık» — atıf; «biz» fâil.", segments=[seg("وَ", "wa", "conj"), seg("تَرَكْنَا", "taraka", "verb")]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with, by» — an adverb of place; a muḍāf.", "«yanında» — mekân zarfı; muzâf."),
  mudaf_pron("مَتَاعِنَا", "mata-goods", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "«our things» — the muḍāf ilayh", "«eşyamız» — muzâfun ileyh"),
  verb_enc("فَأَكَلَهُ", "akala", "هُ", "pron-3ms", "«and … ate him»", "«onu yedi»", mudari=False, hidden=None, fa=True, tags=["atf-nasaq"]), dhib_fail(punct=".")]))
sen("s3", "«And they brought false blood on his shirt», and said: This is Yūsuf's blood! (Yūsuf 12:18)", "«Gömleğinin üzerine yalan bir kan getirdiler» ve dediler: Bu Yusuf'un kanı! (Yûsuf 12:18)", [
  *quran([
  tok("وَجَاؤُوا", "jaa", "verb", ["anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَجَاؤُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«and they came» — the group's wāw its doer.", "«ve geldiler» — cemi vâvı fâil.", segments=[seg("وَ", "wa", "conj"), seg("جَاؤُوا", "jaa", "verb")]),
  ala(), mudaf_pron("قَمِيصِهِ", "qamis", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his shirt» — in jarr", "«gömleği» — mecrur", tags=["huruf-jarr"]),
  tok("بِدَمٍ", "dam-blood", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَدَمٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«with blood» — the bāʾ of jarr.", "«bir kan ile» — cer bâsı.", segments=[seg("بِ", "bi", "prep"), seg("دَمٍ", "dam-blood", "noun")]),
  tok("كَذِبٍ", "kadhib", "noun", ["naat-sifa"], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ — مَصْدَرٌ وُصِفَ بِهِ (أَيْ: مَكْذُوبٍ).", "«false» — the naʿt; a maṣdar used as an adjective.", "«yalan» — sıfat; sıfat olarak kullanılan masdar.")]),
  qalu(wa=True, punct=None), ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("دَمُ", "dam-blood", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the blood (of)» — the khabar; a muḍāf.", "«kanı» — haber; muzâf."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»", punct="!")])
sen("s4", "And their father Yaʿqūb was a prophet, and he was an old man.", "Babaları Yakub bir peygamberdi; yaşlı bir ihtiyardı.", [
  kana(), tok("أَبُوهُمْ", "ab", "noun", [K, "five-nouns", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their father» — kāna's ism, rafʿ by the wāw of the five nouns.", "«babaları» — kâne'nin ismi, vâv ile merfû.", segments=[seg("أَبُو", "ab", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  name_badal("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", "raf") if False else tok("يَعْقُوبُ", "yaqub", "propn", ["badal", "mamnu-min-sarf"], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yaʿqūb» — the badal of the word before, in rafʿ; a diptote.", "«Yakub» — öncekinin bedeli, merfû; gayr-i munsarıf."),
  khabar_kana("نَبِيًّا", "nabi", "«a prophet»", "«bir peygamber»", punct="،"),
  kana_hidden(), khabar_kana("شَيْخًا", "shaykh", "«an old man»", "«bir ihtiyar»"), nat_nasb("كَبِيرًا", "kabir", "«old»", "«yaşlı»", punct=".")])
sen("s5", "And he was wiser than his sons.", "Ve oğullarından daha akıllıydı.", [
  kana_hidden(), tok("أَعْقَلَ", "aqal", "noun", [K, "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ بِلَا تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«wiser» — kāna's khabar; an elative, a diptote.", "«daha akıllı» — kâne'nin haberi; ism-i tafdil, gayr-i munsarıf."),
  min_(), mudaf_pron("أَوْلَادِهِ", "walad", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — جَمْعُ تَكْسِيرٍ", "«his sons» — in jarr; a broken plural", "«oğulları» — mecrur; cem-i mükesser", tags=["huruf-jarr", "jam-taksir"], punct=".")])
sen("s6", "And Yaʿqūb knew that when a wolf eats a man it wounds him and tears his shirt.", "Yakub biliyordu ki kurt bir insanı yediğinde onu yaralar ve gömleğini yırtar.", [
  kana(), yaqub_ism_kana(), khabar_kana_mudari("يَعْرِفُ", "arafa", "«knew»", "«biliyordu»"),
  anna(obj_of="يَعْرِفُ"), tok("الذِّئْبَ", "dhib", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the wolf» — the ism of anna.", "«kurt» — enne'nin ismi."),
  tok("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«when» — the time-adverb of condition, built.", "«-dığında» — şart mânâlı zaman zarfı, mebnî."),
  mazi("أَكَلَ", "akala", "«eats»", "«yer»", hidden="هُوَ", tags=["idha-shartiyya"], extra_ar=" — فِعْلُ الشَّرْطِ"),
  maful("إِنْسَانًا", "insan", "«a man»", "«bir insanı»"),
  verb_enc("جَرَحَهُ", "jaraha", "هُ", "pron-3ms", "«it wounds him»", "«onu yaralar»", mudari=False, extra=" — وَالْجُمْلَةُ جَوَابُ إِذَا، وَالْجُمْلَةُ الشَّرْطِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", tags=["idha-shartiyya"]),
  mazi("وَشَقَّ", "shaqqa", "«and tears»", "«ve yırtar»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "doubled-verbs"]),
  mudaf_pron("قَمِيصَهُ", "qamis", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his shirt» — the object", "«gömleğini» — mef'ûl", tags=["maful-bihi"], punct=".")])
sen("s7", "And Yūsuf's shirt was whole.", "Yusuf'un gömleği sağlamdı.", [
  kana(), tok("قَمِيصُ", "qamis", "noun", [K, "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the shirt (of)» — kāna's ism; a muḍāf.", "«gömleği» — kâne'nin ismi; muzâf."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"), khabar_kana("سَالِمًا", "salim", "«whole»", "«sağlam»", punct=".")])
sen("s8", "And it was dyed in the blood.", "Ve kana boyanmıştı.", [
  kana_hidden(), khabar_kana("مَصْبُوغًا", "masbugh", "«dyed»", "«boyanmış»", tags=["ism-maful"]), fi(), majrur("الدَّمِ", "dam-blood", "«the blood»", "«kan»", "فِي", punct=".")])
sen("s9", "So Yaʿqūb knew that it was false blood, and that the story of the wolf was an invented story.", "Yakub anladı ki bu yalan bir kandır ve kurt hikâyesi uydurma bir hikâyedir.", [
  fa_mazi("فَعَرَفَ", "arafa", "«knew»", "«anladı»", hidden=None), yaqub_fail(),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha"], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ عَرَفَ.", "«that it» — anna with the attached pronoun as its ism; the clause is the object of «knew».", "«onun … olduğunu» — enne; bitişik zamir ismi; te'vilî masdar «anladı»nın mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("دَمُ", "dam-blood", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«blood (of)» — the khabar of anna; a muḍāf.", "«kanı» — enne'nin haberi; muzâf."),
  majrur("كَذِبٍ", "kadhib", "«falsehood»", "«yalan»", "", punct="،") if False else tok("كَذِبٍ", "kadhib", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«of falsehood» — the muḍāf ilayh.", "«yalan» — muzâfun ileyh.", punct="،"),
  anna(wa=True, obj_of="عَرَفَ"), tok("قِصَّةَ", "qissa", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the story (of)» — the ism of anna; a muḍāf.", "«hikâyesi» — enne'nin ismi; muzâf."),
  tok("الذِّئْبِ", "dhib", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the wolf» — the muḍāf ilayh.", "«kurt» — muzâfun ileyh."),
  khabar_inna("قِصَّةٌ", "qissa", "«a story»", "«bir hikâye»", part="أَنَّ"), tok("مَوْضُوعَةٌ", "mawdu", "noun", ["naat-sifa", "ism-maful"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولٍ.", "«invented» — the naʿt; an ism mafʿūl.", "«uydurma» — sıfat; ism-i mef'ûl.", punct=".")])
sen("s10", "So he said to his sons: No — this is a story you have made up. «So patience is fine.»", "Oğullarına dedi: Hayır, bu sizin uydurduğunuz bir hikâyedir. «Artık güzel bir sabır.»", [
  qala_h(fa=True, full="فَقَالَ", punct=None),
  tok("لِأَوْلَادِهِ", "walad", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَأَوْلَادِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his sons» — in jarr; annexed to the pronoun.", "«oğullarına» — mecrur; zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("أَوْلَادِ", "walad", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«no, rather» — the particle of correction.", "«hayır, bilakis» — idrab harfi."),
  ishara("هٰذِهِ", "hadhihi", "raf", "«this»", "«bu»"),
  tok("قِصَّةٌ", "qissa", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a story» — the khabar.", "«bir hikâye» — haber."),
  tok("وَضَعْتُمُوهَا", "wadaa", "verb", ["jumla-sifa", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ، وَالْوَاوُ لِلْإِشْبَاعِ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِقِصَّةٌ.", "«you (pl.) made it up» — the tāʾ its doer, the mīm for the plural, the wāw for the vowel's lengthening, «it» its object; the clause is a naʿt of «a story».", "«onu uydurdunuz» — tâ fâil, mîm cemi için, vâv işbâ için, «onu» mef'ûl; cümle «hikâye»nin sıfatı.", segments=[seg("وَضَعْتُمُو", "wadaa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  *quran([
  tok("فَصَبْرٌ", "sabr", "noun", ["mubtada-khabar", "anwa-al-waw"], "الْفَاءُ اسْتِئْنَافِيَّةٌ (أَوْ فَصِيحَةٌ)، وَصَبْرٌ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْخَبَرُ مَحْذُوفٌ (أَيْ: فَأَمْرِي صَبْرٌ جَمِيلٌ) — أَوْ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ.", "«so patience» — a mubtadaʾ whose khabar is omitted («my course is a fine patience»), or the khabar of an omitted mubtadaʾ.", "«artık sabır» — haberi hazfedilmiş mübtedâ («benim işim güzel bir sabırdır»), yahut hazfedilmiş mübtedânın haberi.", segments=[seg("فَ", "fa", "conj"), seg("صَبْرٌ", "sabr", "noun")]),
  nat_raf("جَمِيلٌ", "jamil", "«fine»", "«güzel»", punct=".")])])
sen("s11", "And Yaʿqūb grieved for Yūsuf with an intense grief, but he bore it with a fine patience.", "Yakub Yusuf'a şiddetle üzüldü; fakat güzel bir sabırla sabretti.", [
  mazi("وَحَزِنَ", "hazina", "«grieved»", "«üzüldü»", hidden=None, wa=True), yaqub_fail(), ala(),
  tok("يُوسُفَ", "yusuf", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — in jarr by a fatḥa.", "«Yusuf» — fetha ile mecrur."),
  tok("حُزْنًا", "huzn", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a grief» — the absolute object.", "«bir üzüntü» — mef'ûl-i mutlak."), nat_nasb("شَدِيدًا", "shadid", "«intense»", "«şiddetli»"),
  tok("وَلٰكِنَّهُ", "lakinna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«but he» — lākinna with the attached pronoun as its ism.", "«fakat o» — lâkinne; bitişik zamir ismidir.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُ", "pron-3ms", "pron")]),
  mazi("صَبَرَ", "sabara", "«he bore (it) patiently»", "«sabretti»", hidden="هُوَ", tags=["inna-wa-akhawatuha"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  tok("صَبْرًا", "sabr", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a patience» — the absolute object.", "«bir sabır» — mef'ûl-i mutlak."), nat_nasb("جَمِيلًا", "jamil", "«fine»", "«güzel»", punct=".")])
# ================================================================ §6 يوسف في البئر (pp. 35–36)
sen("s12", "And the brothers returned home, and left Yūsuf in the well.", "Kardeşler eve döndüler ve Yusuf'u kuyuda bıraktılar.", [
  mazi("وَرَجَعَ", "rajaa", "«returned»", "«döndü»", hidden=None, wa=True), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]),
  ila(), majrur("الْبَيْتِ", "bayt", "«the house»", "«ev»", "إِلَى", punct="،"),
  mazi_pl("وَتَرَكُوا", "taraka", "«and they left»", "«ve bıraktılar»", wa=True, tags=["atf-nasaq"]), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), fi(), majrur("الْبِئْرِ", "bir", "«the well»", "«kuyu»", "فِي", punct=".")])
sen("s13", "And the brothers ate the food, and slept on the bedding.", "Kardeşler yemeği yediler ve döşekte uyudular.", [
  mazi("وَأَكَلَ", "akala", "«ate»", "«yedi»", hidden=None, wa=True), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]),
  maful("الطَّعَامَ", "taam", "«the food»", "«yemeği»", punct="،"),
  mazi_pl("وَنَامُوا", "nama", "«and they slept»", "«ve uyudular»", wa=True, tags=["atf-nasaq", "hollow-verbs"]), ala(), majrur("الْفِرَاشِ", "firash", "«the bedding»", "«döşek»", "عَلَى", punct=".")])
sen("s14", "And Yūsuf was in the well, with no bedding and no food.", "Yusuf ise kuyudaydı; ne döşek vardı ne yemek.", [
  tok("وَيُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "anwa-al-waw", "mamnu-min-sarf"], "الْوَاوُ حَالِيَّةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَيُوسُفُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and Yūsuf» — the wāw of ḥāl; the mubtadaʾ.", "«Yusuf ise» — hâl vâvı; mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("يُوسُفُ", "yusuf", "propn")]),
  tok("فِي", "fi", "prep", ["huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«in» — the phrase is the khabar.", "«-de» — şibh-i cümle haberdir."), majrur("الْبِئْرِ", "bir", "«the well»", "«kuyu»", "فِي", punct="،"),
  tok("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "anwa-al-waw"], "الْوَاوُ حَالِيَّةٌ، وَلَا نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", "«and no» — the genus-denying lā, working like inna.", "«ve hiç … yok» — cins nefyi lâ'sı, inne gibi amel eder.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya-lil-jins", "part")]),
  tok("فِرَاشَ", "firash", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ (أَيْ: لَهُ).", "«bedding» — the ism of lā, built on fatḥa; its khabar («for him») omitted.", "«döşek» — lâ'nın ismi, fetha üzere mebnî; haberi («onun için») hazfedilmiş."),
  tok("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no» — joined; the genus-denying lā again.", "«ve hiç … yok» — atıf; cins nefyi lâ'sı.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya-lil-jins", "part")]),
  tok("طَعَامَ", "taam", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«food» — the ism of lā, built on fatḥa.", "«yemek» — lâ'nın ismi, fetha üzere mebnî.", punct=".")])
sen("s15", "And the brothers forgot Yūsuf, and slept.", "Kardeşler Yusuf'u unuttular ve uyudular.", [
  mazi("وَنَسِيَ", "nasiya", "«forgot»", "«unuttu»", hidden=None, wa=True, tags=["naqis-verbs"]), ikhwan_fail(), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»", punct="،"),
  mazi_pl("وَنَامُوا", "nama", "«and they slept»", "«ve uyudular»", wa=True, tags=["atf-nasaq", "hollow-verbs"], punct=".")])
sen("s16", "But Yūsuf did not sleep, and he did not forget anyone.", "Yusuf ise uyumadı ve kimseyi unutmadı.", [
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and … not» — the negating mā.", "«ve … -medi» — nefiy mâ'sı.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  mazi("نَامَ", "nama", "«slept»", "«uyudu»", hidden=None, tags=["hollow-verbs"]), yusuf_fail(punct="،"),
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and … not» — joined; the negating mā.", "«ve … -medi» — atıf; nefiy mâ'sı.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  mazi("نَسِيَ", "nasiya", "«forgot»", "«unuttu»", hidden="هُوَ", tags=["naqis-verbs"]), maful("أَحَدًا", "ahad", "«anyone»", "«kimseyi»", punct=".")])
sen("s17", "And Yaʿqūb kept remembering Yūsuf, and Yūsuf kept remembering Yaʿqūb.", "Yakub Yusuf'u anmaya devam etti; Yusuf da Yakub'u anmaya devam etti.", [
  tok("وَبَقِيَ", "baqiya", "verb", [K, "naqis-verbs", "anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَبَقِيَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ (بِمَعْنَى ظَلَّ) يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«and … kept» — baqiya as a sister of kāna («remained»): rafʿ on its ism, naṣb on its khabar.", "«ve … kaldı» — kâne'nin kardeşlerinden bakıye (zalle mânâsında): ismini ref, haberini nasb eder.", segments=[seg("وَ", "wa", "conj"), seg("بَقِيَ", "baqiya", "verb")]),
  yaqub_ism_kana(), khabar_kana_mudari("يَذْكُرُ", "dhakara", "«remembering»", "«anarak»"), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»", punct="،"),
  tok("وَبَقِيَ", "baqiya", "verb", [K, "naqis-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَبَقِيَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and … kept» — joined; baqiya as a sister of kāna.", "«ve … kaldı» — atıf; nâkıs fiil.", segments=[seg("وَ", "wa", "conj"), seg("بَقِيَ", "baqiya", "verb")]),
  yusuf_ism_kana(), khabar_kana_mudari("يَذْكُرُ", "dhakara", "«remembering»", "«anarak»"), name_maful("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub'u»", punct=".")])
sen("s18", "And Yūsuf was in the well, and the well was deep.", "Yusuf kuyudaydı ve kuyu derindi.", [
  kana(), yusuf_ism_kana(), tok("فِي", "fi", "prep", ["huruf-jarr", K], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«in» — the phrase is kāna's khabar.", "«-de» — şibh-i cümle kâne'nin haberi."), majrur("الْبِئْرِ", "bir", "«the well»", "«kuyu»", "فِي", punct="،"),
  kanat(), tok("الْبِئْرُ", "bir", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the well» — kāna's ism.", "«kuyu» — kâne'nin ismi."), khabar_kana("عَمِيقَةً", "amiq", "«deep»", "«derin»", punct=".")])
sen("s19", "And the well was in the forest, and the forest was desolate.", "Kuyu ormandaydı ve orman ıssızdı.", [
  kanat(), tok("الْبِئْرُ", "bir", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the well» — kāna's ism.", "«kuyu» — kâne'nin ismi."),
  tok("فِي", "fi", "prep", ["huruf-jarr", K], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«in» — the phrase is kāna's khabar.", "«-de» — şibh-i cümle kâne'nin haberi."), majrur("الْغَابَةِ", "ghaba-forest", "«the forest»", "«orman»", "فِي", punct="،"),
  kanat(), tok("الْغَابَةُ", "ghaba-forest", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the forest» — kāna's ism.", "«orman» — kâne'nin ismi."), khabar_kana("مُوحِشَةً", "muhish", "«desolate»", "«ıssız»", tags=["ism-fail"], punct=".")])
sen("s20", "And that was at night, and the night was dark.", "Bu gece vaktiydi ve gece karanlıktı.", [
  kana(), tok("ذٰلِكَ", "dhalika", "pron", [K, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«that» — the demonstrative as kāna's ism.", "«bu» — ism-i işâret, kâne'nin ismi."),
  tok("فِي", "fi", "prep", ["huruf-jarr", K], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«at» — the phrase is kāna's khabar.", "«-de» — şibh-i cümle kâne'nin haberi."), majrur("اللَّيْلِ", "layl", "«the night»", "«gece»", "فِي", punct="،"),
  kana(), tok("اللَّيْلُ", "layl", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the night» — kāna's ism.", "«gece» — kâne'nin ismi."), khabar_kana("مُظْلِمًا", "muzlim", "«dark»", "«karanlık»", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "isha-evening": G("isha-evening", "عِشَاء", "ع ش و", "noun", "nightfall, the evening", "akşam, yatsı vakti", 1),
 "istabaqa": G("istabaqa", "اِسْتَبَقَ", "س ب ق", "verb", "to race one another (Form VIII)", "yarışmak (iftiâl bâbı)", 2, form="VIII"),
 "mata-goods": G("mata-goods", "مَتَاع", "م ت ع", "noun", "goods, belongings", "eşya, mal", 1, plural="أَمْتِعَة"),
 "aqal": G("aqal", "أَعْقَل", "ع ق ل", "noun", "wiser, more sensible (elative of عَاقِل)", "daha akıllı (âkil'in ism-i tafdili)", 2),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to tear, to split (a doubled verb)", "yırtmak, yarmak (muzâaf)", 1, form="I"),
 "nama": G("nama", "نَامَ", "ن و م", "verb", "to sleep (hollow, yāʾ-type in the māḍī: نِمْتُ)", "uyumak (ecvef)", 1, form="I"),
 "firash": G("firash", "فِرَاش", "ف ر ش", "noun", "bedding, a bed", "döşek, yatak", 1, plural="فُرُش"),
 "muhish": G("muhish", "مُوحِش", "و ح ش", "noun", "desolate, lonely (ism fāʿil of أَوْحَشَ)", "ıssız, tenha (evhaşe'nin ism-i fâili)", 2),
 "masbugh": G("masbugh", "مَصْبُوغ", "ص ب غ", "noun", "dyed (ism mafʿūl of صَبَغَ)", "boyanmış (sabağa'nın ism-i mef'ûlü)", 1),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("baka", "بكى"), ("kadhib", "كذب"), ("jaraha", "جرح"), ("mawdu", "موضوع"), ("sabr", "صبر"), ("huzn", "حزن"), ("sabara", "صبر"), ("nasiya", "نسي"), ("inda", "عند"), ("la-nafiya-lil-jins", "لا"), ("idha", "إذا")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("istabaqa", "shaqqa", "nama"): mo["verbs"].pop(_k, None)
put_morph(mo, "istabaqa", _sg.derived("مِنْ بَابِ الِافْتِعَالِ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِسْتَبَق", "سْتَبِق", "اِسْتَبِق", "اِسْتِبَاق", "مُسْتَبِق", note="لَازِمٌ: اِسْتَبَقَ الْقَوْمُ — تَسَابَقُوا."))
put_morph(mo, "shaqqa", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَعَّفٌ", "فَعَلَ يَفْعُلُ", "شَقّ", "شَاقّ",
                                   _sg.mazi14("شَقّ", "شَقَق"), _sg.mudari14("َ", "شُقّ", "شْقُق"), ["شُقَّ", "شُقَّا", "شُقُّوا", "شُقِّي", "شُقَّا", "اُشْقُقْنَ"],
                                   "يَشُقَّ", "يَشُقَّ", "تَشُقَّ", "مَشْقُوق", "شُقَّ", "يُشَقُّ", note="مُتَعَدٍّ — مُضَعَّفٌ: الْمِثْلَانِ يُدْغَمَانِ حَيْثُ تَحَرَّكَ الثَّانِي (شَقَّ) وَيُفَكَّانِ أَمَامَ السَّاكِنِ (شَقَقْتُ)؛ الْجَزْمُ بِالْفَتْحِ."))
put_morph(mo, "nama", _sg.hollow1("samia", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ سَمِعَ)", "نَام", "نِم", "نَام", "نَم", "نَام", "نَم", "نَوْم", "نَائِم", note="لَازِمٌ: نَامَ يَنَامُ، نِمْتُ — الْعَيْنُ وَاوٌ وَالْمَاضِي عَلَى وَزْنِ فَعِلَ فَكُسِرَ أَوَّلُهُ عِنْدَ السُّكُونِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 10 (print pp. 34–36, «أَحْسَنُ الْقَصَصِ» sections 5 «أَمَامَ يَعْقُوب» and 6 «يُوسُفُ فِي الْبِئْر»): the brothers before Yaʿqūb — Yūsuf 12:16 (s1), 12:17 (s2) and the opening of 12:18 (s3) as the print sets them, marked, with the print's own «وَقَالُوا هٰذَا دَمُ يُوسُفَ» completing s3 outside the quotation; the whole shirt and Yaʿqūb's reading of it (s4–s9), his answer with the aya's «فَصَبْرٌ جَمِيلٌ» (s10, marked) and his grief (s11); Yūsuf in the well at night (s12–s20). "
          "One printed line is one sentence, split at the print's own full stops where a line holds several (s4, s7–s8); s11 is the print's own continuation after the aya; the print's parentheses around the ayas are read as quotation marks.")
ADD_TR = (" Onuncu bölüm (basılı s. 34–36, «أَحْسَنُ الْقَصَصِ» 5. kısım «أَمَامَ يَعْقُوب» ve 6. kısım «يُوسُفُ فِي الْبِئْر»): kardeşler Yakub'un önünde — Yûsuf 12:16 (s1), 12:17 (s2) ve 12:18'in başı (s3) baskıdaki şekliyle, işaretli; s3'ü tamamlayan «وَقَالُوا هٰذَا دَمُ يُوسُفَ» baskının kendi sözüdür ve alıntının dışındadır; sağlam gömlek ve Yakub'un onu okuyuşu (s4–s9), âyetin «فَصَبْرٌ جَمِيلٌ» sözünü taşıyan cevabı (s10, işaretli) ve hüznü (s11); Yusuf gece kuyuda (s12–s20). "
          "Basılı her satır bir cümledir; birden çok cümle taşıyan satırlar baskının noktalarından bölünmüştür (s4, s7–s8); s11 baskının âyetten sonraki kendi devamıdır; baskının âyetleri saran parantezleri tırnak olarak okunmuştur.")
write_out(10, S, TITLE, ADD_EN, ADD_TR, "pp. 34–36", GLOSS_ADD)
report(10, S, GLOSS_ADD, ())
