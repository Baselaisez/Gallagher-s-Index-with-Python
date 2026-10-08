# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 11: «مِنَ الْبِئْرِ إِلَى الْقَصْرِ، وَالْوَفَاءُ وَالْأَمَانَةُ» — «أَحْسَنُ الْقَصَصِ» sections 7–8 (print pp. 36–38):
the caravan, the bucket and «يَا بُشْرَى» (12:19), the market of Egypt and the ʿAzīz; the wife's attempt, Yūsuf's refusal, the ʿAzīz's
verdict (12:29), the city's wonder (12:31), «السِّجْنُ أَحَبُّ إِلَيَّ» (12:33) and the prison. Every printed line is one sentence, split at
the print's own full stops; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch11.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "مِنَ الْبِئْرِ إِلَى الْقَصْرِ، وَالْوَفَاءُ وَالْأَمَانَةُ", "en": "From the well to the palace; fidelity and trust", "tr": "Kuyudan saraya; vefa ve emanet"}
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

# ================================================================ §7 من البئر إلى القصر (pp. 36–37)
sen("s1", "And a company was travelling through this forest.", "Bir kafile bu ormanda yolculuk ediyordu.", [
  tok("وَكَانَتْ", "kana", "verb", [K, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … was» — kāna with the feminine tāʾ.", "«ve … idi» — kâne, te'nis tâ'sı ile.", segments=[seg("وَ", "wa", "conj"), seg("كَانَتْ", "kana", "verb")]),
  tok("جَمَاعَةٌ", "jamaa", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«a company» — kāna's ism.", "«bir kafile» — kâne'nin ismi."),
  khabar_kana_mudari("تُسَافِرُ", "safara", "«was travelling»", "«yolculuk ediyordu»", hidden="هِيَ", tags=["form-iii-verbs"]),
  fi(), ishara("هٰذِهِ", "hadhihi", "jarr", "«this»", "«bu»"), tok("الْغَابَةِ", "ghaba-forest", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«forest» — the badal, in jarr.", "«orman» — bedel, mecrur.", punct=".")])
sen("s2", "And they grew thirsty on the way, and searched for a well.", "Yolda susadılar ve bir kuyu aradılar.", [
  mazi_pl("وَعَطِشُوا", "atisha", "«they grew thirsty»", "«susadılar»", wa=True), fi(), majrur("الطَّرِيقِ", "tariq", "«the way»", "«yol»", "فِي", punct="،"),
  mazi_pl("وَبَحَثُوا", "bahatha", "«and they searched»", "«ve aradılar»", wa=True, tags=["atf-nasaq"]),
  tok("عَنْ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for» (lit. «about»).", "«-i (aramak)»."), majrur("بِئْرٍ", "bir", "«a well»", "«bir kuyu»", "عَنْ", punct=".")])
sen("s3", "And they saw a well, and sent a man to it to bring them water.", "Bir kuyu gördüler ve onlara su getirsin diye ona bir adam gönderdiler.", [
  mazi_pl_naqis("وَرَأَوْا", "raa", "«they saw»", "«gördüler»", wa=True), maful("بِئْرًا", "bir", "«a well»", "«bir kuyu»", punct="،"),
  tok("فَأَرْسَلُوا", "arsala", "verb", ["atf-nasaq", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأَرْسَلُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«and so they sent» — the group's wāw its doer.", "«ve gönderdiler» — cemi vâvı fâil.", segments=[seg("فَ", "fa", "conj"), seg("أَرْسَلُوا", "arsala", "verb")]),
  tok("إِلَيْهَا", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«to it».", "«ona».", segments=[seg("إِلَيْ", "ila", "prep"), seg("هَا", "pron-3fs", "pron")]),
  maful("رَجُلًا", "rajul", "«a man»", "«bir adam»"),
  tok("لِيَأْتِيَ", "ata", "verb", ["lam-taleel", "naqis-verbs"], "اللَّامُ لَامُ التَّعْلِيلِ، وَيَأْتِيَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَهَا وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to bring» — the lām of purpose; naṣb by a hidden an.", "«getirsin diye» — ta'lil lâmı; gizli en ile mansub.", segments=[seg("لِ", "li", "prep"), seg("يَأْتِيَ", "ata", "verb")]),
  lahu("لَهُمْ", "هُمْ", "pron-3mp", "مُتَعَلِّقٌ بِيَأْتِيَ.", "«to them».", "«onlara»."),
  tok("بِالْمَاءِ", "ma-water", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ (لِلتَّعْدِيَةِ)، وَالْمَاءِ مَجْرُورٌ بِالْكَسْرَةِ.", "«(with) the water» — the bāʾ that makes «come» into «bring».", "«suyu» — «gelmek»i «getirmek» yapan bâ.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الْمَاءِ", "ma-water", "noun")])])
sen("s4", "The man came to the well and let down his bucket.", "Adam kuyuya geldi ve kovasını sarkıttı.", [
  mazi("جَاءَ", "jaa", "«came»", "«geldi»", hidden=None), fail("الرَّجُلُ", "rajul", "«the man»", "«adam»"), ila(), majrur("الْبِئْرِ", "bir", "«the well»", "«kuyu»", "إِلَى", punct="،"),
  mazi("وَأَدْلَى", "adla", "«and let down»", "«ve sarkıttı»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "naqis-verbs", "form-iv-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ"),
  mudaf_pron("دَلْوَهُ", "dalw", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "«his bucket» — the object", "«kovasını» — mef'ûl", tags=["maful-bihi"], punct=".")])
sen("s5", "And he drew up the bucket, and lo — the bucket was heavy!", "Kovayı çekti; bir de ne görsün, kova ağır!", [
  mazi("وَنَزَعَ", "nazaa", "«and he drew up»", "«ve çekti»", hidden="هُوَ", wa=True), maful("الدَّلْوَ", "dalw", "«the bucket»", "«kovayı»", punct="،"),
  fa_idha(), tok("الدَّلْوُ", "dalw", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the bucket» — the mubtadaʾ.", "«kova» — mübtedâ."),
  tok("ثَقِيلَةٌ", "thaqil", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«heavy» — the khabar.", "«ağır» — haber.", punct="!")])
sen("s6", "And he pulled it out — and lo, in the bucket was a boy!", "Onu çıkardı; bir de ne görsün, kovada bir çocuk!", [
  verb_enc("وَأَخْرَجَهَا", "akhraja", "هَا", "pron-3fs", "«and he pulled it out»", "«ve onu çıkardı»", mudari=False, wa=True, tags=["atf-nasaq", "form-iv-verbs"]),
  fa_idha(), tok("فِي", "fi", "prep", ["huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«in» — the phrase is the fronted khabar.", "«-de» — şibh-i cümle öne alınmış haber."),
  majrur("الدَّلْوِ", "dalw", "«the bucket»", "«kova»", "فِي"),
  tok("غُلَامٌ", "ghulam", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a boy» — the delayed mubtadaʾ.", "«bir çocuk» — geciktirilmiş mübtedâ.", punct="!")])
sen("s7", "The man was astonished and called out: «O good news! This is a boy.» (Yūsuf 12:19)", "Adam şaşırdı ve seslendi: «Müjde! Bu bir çocuk.» (Yûsuf 12:19)", [
  mazi("دَهِشَ", "dahisha", "«was astonished»", "«şaşırdı»", hidden=None), fail("الرَّجُلُ", "rajul", "«the man»", "«adam»"),
  mazi("وَنَادَى", "nada", "«and called out»", "«ve seslendi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "naqis-verbs", "form-iii-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ", punct=":"),
  *quran([
  tok("يٰبُشْرَى", "bushra", "noun", ["vocative-munada", "ism-maqsur-manqus"], "يَا حَرْفُ نِدَاءٍ (رُسِمَتْ مُتَّصِلَةً فِي الْمُصْحَفِ)، وَبُشْرَى مُنَادًى مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ.", "«O good news» — the vocative written joined, as the muṣḥaf writes it; a maqṣūr munādā built on an estimated ḍamma.", "«ey müjde» — nidâ, mushafta bitişik yazılır; maksûr münâdâ, takdîrî zamme üzere mebnî.", segments=[seg("يٰ", "ya-nida", "part"), seg("بُشْرَى", "bushra", "noun")]),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"), tok("غُلَامٌ", "ghulam", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a boy» — the khabar.", "«bir çocuk» — haber.", punct=".")])])
sen("s8", "And the people rejoiced greatly, and hid him.", "İnsanlar çok sevindi ve onu sakladılar.", [
  mazi("وَفَرِحَ", "fariha", "«rejoiced»", "«sevindi»", hidden=None, wa=True), nas_fail(), jiddan(),
  tok("وَأَخْفَوْهُ", "akhfa", "verb", ["atf-nasaq", "naqis-verbs", "form-iv-verbs", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَأَخْفَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and they hid him» — a nāqiṣ māḍī with the group's wāw as doer and «him» its object.", "«ve onu sakladılar» — nâkıs mâzî; cemi vâvı fâil, «onu» mef'ûl.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("أَخْفَوْ", "akhfa", "verb"), seg("هُ", "pron-3ms", "pron")])])
sen("s9", "And they reached Egypt, and stood in the market and called out:", "Mısır'a vardılar; çarşıda durup seslendiler:", [
  mazi_pl("وَوَصَلُوا", "wasala", "«they reached»", "«vardılar»", wa=True, tags=["mithal-verbs"]), ila(),
  tok("مِصْرَ", "misr", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«Egypt» — in jarr by a fatḥa; a diptote (a feminine proper name).", "«Mısır» — fetha ile mecrur; gayr-i munsarıf (müennes alem).", punct="،"),
  mazi_pl("وَقَامُوا", "qama", "«and they stood»", "«ve durdular»", wa=True, tags=["atf-nasaq", "hollow-verbs"]), fi(), majrur("السُّوقِ", "suq", "«the market»", "«çarşı»", "فِي"),
  mazi_pl_naqis("وَنَادَوْا", "nada", "«and called out»", "«ve seslendiler»", wa=True, tags=["atf-nasaq", "form-iii-verbs"], punct=":")])
sen("s10", "Who will buy this boy?", "Bu çocuğu kim satın alır?", [man_istif(), yashtari(), *hadha_ghulam(punct="؟")])
sen("s11", "Who will buy this boy?", "Bu çocuğu kim satın alır?", [man_istif(), yashtari(), *hadha_ghulam(punct="؟")])
sen("s12", "The ʿAzīz bought Yūsuf for a few dirhams.", "Aziz Yusuf'u birkaç dirheme satın aldı.", [
  mazi("اِشْتَرَى", "ishtara", "«bought»", "«satın aldı»", hidden=None, tags=["form-viii-verbs", "naqis-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ"), aziz_fail(), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  tok("بِدَرَاهِمَ", "dirham", "noun", ["huruf-jarr", "mamnu-min-sarf", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ (لِلْعِوَضِ)، وَدَرَاهِمَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«for dirhams» — the bāʾ of price; a diptote plural takes a fatḥa for its jarr.", "«dirhemlere» — bedel bâsı; gayr-i munsarıf cemi cerde fetha alır.", segments=[seg("بِ", "bi", "prep"), seg("دَرَاهِمَ", "dirham", "noun")]),
  tok("مَعْدُودَةٍ", "madud", "noun", ["naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ.", "«few (counted)» — the naʿt; an ism mafʿūl.", "«sayılı» — sıfat; ism-i mef'ûl.", punct=".")])
sen("s13", "And the merchants sold him, and did not know Yūsuf.", "Tüccarlar onu sattılar ve Yusuf'u tanımadılar.", [
  verb_enc("وَبَاعَهُ", "baa", "هُ", "pron-3ms", "«and … sold him»", "«ve onu sattı»", mudari=False, hidden=None, wa=True, tags=["hollow-verbs"]),
  tok("التُّجَّارُ", "tajir", "noun", ["fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ.", "«the merchants» — the doer; a broken plural.", "«tüccarlar» — fâil; cem-i mükesser."),
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and … not» — the negating mā.", "«ve … -medi» — nefiy mâ'sı.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  mazi_pl("عَرَفُوا", "arafa", "«they knew»", "«tanıdılar»"), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»", punct=".")])
sen("s14", "And the ʿAzīz took him to his palace, and said to his wife: Treat Yūsuf well; he is a sensible boy.", "Aziz onu sarayına götürdü ve karısına dedi: Yusuf'a iyi davran; o aklı başında bir çocuktur.", [
  mazi("وَذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None, wa=True),
  tok("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ (لِلتَّعْدِيَةِ: ذَهَبَ بِهِ = أَذْهَبَهُ)، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«(took) him» — the bāʾ that makes «went» into «took».", "«onu (götürdü)» — «gitti»yi «götürdü» yapan bâ.", segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  aziz_fail(), ila(), mudaf_pron("قَصْرِهِ", "qasr", "هِ", "pron-3ms", "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his palace» — in jarr", "«sarayı» — mecrur", tags=["huruf-jarr"], punct="،"),
  qala_h(wa=True, full="وَقَالَ", punct=None),
  tok("لِامْرَأَتِهِ", "imraa", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَامْرَأَةِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his wife» — in jarr; annexed to the pronoun.", "«karısına» — mecrur; zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("امْرَأَةِ", "imraa", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("أَكْرِمِي", "akrama", "verb", ["imperative-amr", "form-iv-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ ضَمِيرُ الْمُخَاطَبَةِ فَاعِلٌ.", "«treat well» (fem. sg.) — an imperative built on the dropped nūn; the yāʾ of address is its doer.", "«iyi davran» (dişil) — nûnun hazfi üzere mebnî emir; muhâtaba yâ'sı fâil."),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'a»", punct="،"),
  tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed he» — inna with the attached pronoun as its ism.", "«şüphesiz o» — inne; bitişik zamir ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  khabar_inna("وَلَدٌ", "walad", "«a boy»", "«bir çocuk»"), nat_raf("رَشِيدٌ", "rashid", "«sensible»", "«aklı başında»", punct=".")])
# ================================================================ §8 الوفاء والأمانة (pp. 37–38)
sen("s15", "And the ʿAzīz's wife tried to seduce Yūsuf into betrayal.", "Aziz'in karısı Yusuf'u ihanete çağırdı.", [
  tok("وَرَاوَدَتِ", "rawada", "verb", ["anwa-al-waw", "form-iii-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَرَاوَدَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and … tried to seduce» — a māḍī with the feminine tāʾ, its kasra for the meeting of two sukūns.", "«ve … çağırdı» — te'nis tâ'lı mâzî; kesresi iki sâkinin karşılaşması için.", segments=[seg("وَ", "wa", "conj"), seg("رَاوَدَتِ", "rawada", "verb")]),
  *imraat_aziz("فَاعِلٌ", "«the wife (of)» — the doer", "«karısı» — fâil", tags=["fail"]), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  ala(), majrur("الْخِيَانَةِ", "khiyana", "«betrayal»", "«ihanet»", "عَلَى", punct=".")])
sen("s16", "But Yūsuf refused, and said: Never!", "Fakat Yusuf reddetti ve dedi: Asla!", [
  tok("وَلٰكِنْ", "lakin", "part", ["anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin, no government.", "«fakat» — tahfif edilmiş lâkin; amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنْ", "lakin", "part")]),
  tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the mubtadaʾ; a diptote.", "«Yusuf» — mübtedâ; gayr-i munsarıf."),
  mazi("أَبَى", "aba", "«refused»", "«reddetti»", hidden="هُوَ", tags=["mubtada-khabar", "naqis-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", punct="،"),
  qala_h(wa=True, full="وَقَالَ", punct=None), tok("كَلَّا", "kalla", "part", [], "حَرْفُ رَدْعٍ وَزَجْرٍ.", "«never!» — the particle of rebuke.", "«asla!» — red' ve zecr harfi.", punct="!")])
sen("s17", "I do not betray my master; he has been good to me and honoured me.", "Ben efendime ihanet etmem; o bana iyilik etti ve beni ağırladı.", [
  tok("أَنَا", "pron-1s-munfasil", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the mubtadaʾ.", "«ben» — mübtedâ."),
  la_nafiya(), mudari("أَخُونُ", "khana", "«betray»", "«ihanet etmem»", hidden="أَنَا", tags=["la-nafiya", "hollow-verbs", "mubtada-khabar"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  tok("سَيِّدِي", "sayyid", "noun", ["maful-bihi", "ya-al-mutakallim", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my master» — the object, its fatḥa estimated before the speaker's yāʾ.", "«efendimi» — mef'ûl, fethası mütekellim yâ'sından önce takdîrî.", punct="،", segments=[seg("سَيِّدِ", "sayyid", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed he» — inna with its pronoun ism.", "«şüphesiz o» — inne; zamir ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  mazi("أَحْسَنَ", "ahsana", "«has been good»", "«iyilik etti»", hidden="هُوَ", tags=["inna-wa-akhawatuha", "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("إِلَيَّ", "ila", "prep", ["huruf-jarr", "ya-al-mutakallim"], "إِلَى حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ فِي مَحَلِّ جَرٍّ — وَقُلِبَتْ أَلِفُ إِلَى يَاءً وَأُدْغِمَتْ.", "«to me» — the alif of ilā turns yāʾ before the speaker's yāʾ and merges.", "«bana» — ilâ'nın elifi mütekellim yâ'sından önce yâ olur ve idgam edilir.", segments=[seg("إِلَ", "ila", "prep"), seg("يَّ", "pron-1s", "pron")]),
  tok("وَأَكْرَمَنِي", "akrama", "verb", ["atf-nasaq", "form-iv-verbs", "maful-bihi", "ya-al-mutakallim"], "الْوَاوُ عَاطِفَةٌ، وَأَكْرَمَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and honoured me» — joined; the nūn of protection before the speaker's yāʾ, which is its object.", "«ve beni ağırladı» — atıf; vikâye nûnu mütekellim yâ'sından önce, yâ mef'ûl.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("أَكْرَمَ", "akrama", "verb"), seg("نِي", "pron-1s", "pron")])])
sen("s18", "Indeed I fear Allah.", "Ben Allah'tan korkarım.", [
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the speaker's yāʾ as its ism, the nūn of protection between.", "«şüphesiz ben» — inne; mütekellim yâ'sı ismi, arada vikâye nûnu.", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  mudari("أَخَافُ", "khafa", "«I fear»", "«korkarım»", hidden="أَنَا", tags=["inna-wa-akhawatuha", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah» — mef'ûl.", punct=".")])
sen("s19", "And the ʿAzīz's wife grew angry and complained to her husband.", "Aziz'in karısı öfkelendi ve kocasına şikâyet etti.", [
  tok("وَغَضِبَتِ", "ghadiba", "verb", ["anwa-al-waw"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَغَضِبَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and … grew angry» — the feminine tāʾ, its kasra for the meeting of sukūns.", "«ve … öfkelendi» — te'nis tâ'sı; kesresi iki sâkin için.", segments=[seg("وَ", "wa", "conj"), seg("غَضِبَتِ", "ghadiba", "verb")]),
  *imraat_aziz("فَاعِلٌ", "«the wife (of)» — the doer", "«karısı» — fâil", tags=["fail"]),
  tok("وَشَكَتْ", "shaka", "verb", ["atf-nasaq", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَشَكَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and complained» — a nāqiṣ māḍī, its alif dropped before the feminine tāʾ.", "«ve şikâyet etti» — nâkıs mâzî; elifi te'nis tâ'sından önce düşmüş.", segments=[seg("وَ", "wa", "conj"), seg("شَكَتْ", "shaka", "verb")]),
  ila(), mudaf_pron("زَوْجِهَا", "zawj", "هَا", "pron-3fs", "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«her husband» — in jarr", "«kocası» — mecrur", tags=["huruf-jarr"], punct=".")])
sen("s20", "And the ʿAzīz knew that the woman was lying.", "Aziz kadının yalancı olduğunu anladı.", [
  mazi("وَعَرَفَ", "arafa", "«knew»", "«anladı»", hidden=None, wa=True), aziz_fail(), anna(obj_of="عَرَفَ"),
  ism_inna("الْمَرْأَةَ", "imraa", "«the woman»", "«kadın»", part="أَنَّ"), khabar_inna("كَاذِبَةٌ", "kadhib-liar", "«lying»", "«yalancı»", part="أَنَّ", tags=["ism-fail"], punct=".")])
sen("s21", "And he knew that Yūsuf was trustworthy.", "Ve Yusuf'un emin olduğunu anladı.", [
  mazi("وَعَرَفَ", "arafa", "«and he knew»", "«ve anladı»", hidden="هُوَ", wa=True), anna(obj_of="عَرَفَ"),
  tok("يُوسُفَ", "yusuf", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the ism of anna; a diptote.", "«Yusuf» — enne'nin ismi; gayr-i munsarıf."),
  khabar_inna("أَمِينٌ", "amin", "«trustworthy»", "«emin»", part="أَنَّ", punct=".")])
sen("s22", "So he said to his wife: «Indeed you were of the wrongdoers.» (Yūsuf 12:29)", "Karısına dedi: «Şüphesiz sen hata edenlerdensin.» (Yûsuf 12:29)", [
  qala_h(fa=True, full="فَقَالَ", punct=None),
  tok("لِزَوْجِهِ", "zawj", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَزَوْجِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالزَّوْجُ يُقَالُ لِلْمَرْأَةِ أَيْضًا.", "«to his wife» — in jarr; زَوْج is said of the wife too.", "«karısına» — mecrur; زَوْج kadına da denir.", segments=[seg("لِ", "li", "prep"), seg("زَوْجِ", "zawj", "noun"), seg("هِ", "pron-3ms", "pron")]),
  *quran([
  tok("إِنَّكِ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرُ الْمُخَاطَبَةِ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed you» (fem.) — inna with the addressed woman's kāf as its ism.", "«şüphesiz sen» (dişil) — inne; muhâtaba kâfı ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("كِ", "pron-2fs", "pron")]),
  tok("كُنْتِ", "kana", "verb", ["inna-wa-akhawatuha", K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ ضَمِيرُ الْمُخَاطَبَةِ اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«you were» — kāna with the addressed woman's tāʾ as its ism; the clause is inna's khabar.", "«idin» — kâne; muhâtaba tâ'sı ismi; cümle inne'nin haberi."),
  min_(full="مِنَ"), tok("الْخَاطِئِينَ", "khati", "noun", ["huruf-jarr", K, "jam-mudhakkar-salim"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«the wrongdoers» — jarr by the yāʾ of the sound plural; the phrase is kāna's khabar.", "«hata edenler» — cem-i müzekker sâlimin yâ'sı ile mecrur; şibh-i cümle kâne'nin haberi.", punct=".")])])
sen("s23", "And Yūsuf became known in Egypt for his beauty; whenever anyone saw him he said: «This is no human; this is none but a noble angel.» (Yūsuf 12:31)", "Yusuf Mısır'da güzelliğiyle tanındı; onu kim görse derdi: «Bu bir insan değil; bu ancak kerim bir melektir.» (Yûsuf 12:31)", [
  tok("وَعُرِفَ", "arafa", "verb", ["anwa-al-waw", "naib-al-fail"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَعُرِفَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … became known» — a passive māḍī.", "«ve … tanındı» — meçhul mâzî.", segments=[seg("وَ", "wa", "conj"), seg("عُرِفَ", "arafa", "verb")]),
  tok("يُوسُفُ", "yusuf", "propn", ["naib-al-fail", "mamnu-min-sarf"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the deputy doer; a diptote.", "«Yusuf» — nâib-i fâil; gayr-i munsarıf."),
  fi(), tok("مِصْرَ", "misr", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Egypt» — in jarr by a fatḥa.", "«Mısır» — fetha ile mecrur."),
  tok("بِجَمَالِهِ", "jamal", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ (لِلسَّبَبِيَّةِ)، وَجَمَالِ مَجْرُورٌ بِالْكَسْرَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«for his beauty» — the bāʾ of cause.", "«güzelliği sebebiyle» — sebep bâsı.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("جَمَالِ", "jamal", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("وَإِذَا", "idha", "part", ["atf-nasaq", "idha-shartiyya", "maful-fih"], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and whenever» — the time-adverb of condition.", "«ve … -dığında» — şart mânâlı zaman zarfı.", segments=[seg("وَ", "wa", "conj"), seg("إِذَا", "idha", "part")]),
  verb_enc("رَآهُ", "raa", "هُ", "pron-3ms", "«saw him»", "«onu gördü»", mudari=False, hidden=None, tags=["idha-shartiyya", "naqis-verbs"], extra=" — فِعْلُ الشَّرْطِ، وَفَتْحُهُ مُقَدَّرٌ عَلَى الْأَلِفِ"),
  fail("أَحَدٌ", "ahad", "«anyone»", "«biri»"),
  mazi("قَالَ", "qala", "«he said»", "«derdi»", hidden="هُوَ", tags=["idha-shartiyya", "hollow-verbs", "maful-bihi"], extra_ar=" — جَوَابُ إِذَا، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ"),
  *quran([
  tok("مَا", "ma-nafiya", "part", ["anwa-ma", "anwa-ma"], "مَا نَافِيَةٌ حِجَازِيَّةٌ تَعْمَلُ عَمَلَ لَيْسَ: تَرْفَعُ الِاسْمَ وَتَنْصِبُ الْخَبَرَ.", "«not» — the Ḥijāzī mā working like laysa: rafʿ on its ism, naṣb on its khabar.", "«değil» — leyse gibi amel eden Hicâzî mâ: ismini ref, haberini nasb eder."),
  tok("هٰذَا", "hadha", "pron", ["anwa-ma", "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ مَا.", "«this» — the demonstrative as the ism of mā.", "«bu» — ism-i işâret, mâ'nın ismi."),
  tok("بَشَرًا", "bashar", "noun", ["anwa-ma"], "خَبَرُ مَا الْحِجَازِيَّةِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a human» — the khabar of the Ḥijāzī mā, in naṣb.", "«bir insan» — Hicâzî mâ'nın haberi, mansub.", punct="،"),
  tok("إِنْ", "in-nafiya", "part", ["qasr", "istithna"], "إِنْ نَافِيَةٌ بِمَعْنَى مَا، لَا عَمَلَ لَهَا.", "«not» — the negating in, like mā; no government.", "«değil» — mâ mânâsında nefiy in'i; amel etmez."),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("إِلَّا", "illa", "part", ["qasr", "istithna"], "حَرْفُ اسْتِثْنَاءٍ مُلْغًى (أَدَاةُ حَصْرٍ).", "«except» — the voided exception particle: the frame of restriction.", "«ancak» — ilgâ edilmiş istisnâ harfi: hasr edatı."),
  tok("مَلَكٌ", "malak", "noun", ["mubtada-khabar", "qasr"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«an angel» — the khabar.", "«bir melek» — haber."),
  nat_raf("كَرِيمٌ", "karim", "«noble»", "«kerim»", punct=".")])])
sen("s24", "And the woman's anger grew intense, and she said to Yūsuf: Then you shall go to prison!", "Kadının öfkesi şiddetlendi ve Yusuf'a dedi: Öyleyse hapse gidersin!", [
  mazi("وَاشْتَدَّ", "ishtadda", "«grew intense»", "«şiddetlendi»", hidden=None, wa=True, tags=["form-viii-verbs", "doubled-verbs"]),
  tok("غَضَبُ", "ghadab", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the anger (of)» — the doer; a muḍāf.", "«öfkesi» — fâil; muzâf."),
  tok("الْمَرْأَةِ", "imraa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the woman» — the muḍāf ilayh.", "«kadın» — muzâfun ileyh."),
  tok("وَقَالَتْ", "qala", "verb", ["atf-nasaq", "hollow-verbs", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَقَالَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«and she said» — joined; the feminine tāʾ; what is said is its object.", "«ve dedi» — atıf; te'nis tâ'sı; söylenen söz mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("قَالَتْ", "qala", "verb")]),
  li_name("لِيُوسُفَ", "yusuf", "Yūsuf", "Yusuf", punct=":"),
  tok("إِذَنْ", "idhan-jawab", "part", ["an-masdariyya"], "حَرْفُ جَوَابٍ وَجَزَاءٍ، مُلْغًى هُنَا لِأَنَّ الْفِعْلَ بَعْدَهُ مَرْفُوعٌ.", "«then» — the particle of answer and consequence; voided here, the verb after it in rafʿ.", "«öyleyse» — cevap ve cezâ harfi; burada ilgâ edilmiş, fiil merfû."),
  mudari("تَذْهَبُ", "dhahaba", "«you shall go»", "«gidersin»", hidden="أَنْتَ"), *ila_sijn(punct="!")])
sen("s25", "Yūsuf said: «Prison is dearer to me!» (Yūsuf 12:33)", "Yusuf dedi: «Hapis bana daha sevimlidir!» (Yûsuf 12:33)", [
  qala_h(punct=None), yusuf_fail(punct=":"),
  *quran([
  tok("السِّجْنُ", "sijn", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«prison» — the mubtadaʾ.", "«hapis» — mübtedâ."),
  tok("أَحَبُّ", "ahabb", "noun", ["mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«dearer» — the khabar; an elative, a diptote.", "«daha sevimli» — haber; ism-i tafdil, gayr-i munsarıf."),
  tok("إِلَيَّ", "ila", "prep", ["huruf-jarr", "ya-al-mutakallim"], "إِلَى حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِأَحَبُّ.", "«to me» — attached to «dearer».", "«bana» — «daha sevimli»ye bağlı.", punct="!", segments=[seg("إِلَ", "ila", "prep"), seg("يَّ", "pron-1s", "pron")])])])
sen("s26", "And after some days the ʿAzīz decided to send Yūsuf to prison.", "Birkaç gün sonra Aziz, Yusuf'u hapse göndermeyi uygun gördü.", [
  tok("وَبَعْدَ", "bada", "noun", ["anwa-al-waw", "maful-fih", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَبَعْدَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«and after» — an adverb of time; a muḍāf.", "«ve … sonra» — zaman zarfı; muzâf.", segments=[seg("وَ", "wa", "conj"), seg("بَعْدَ", "bada", "noun")]),
  tok("أَيَّامٍ", "yawm", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تَكْسِيرٍ.", "«days» — the muḍāf ilayh; a broken plural.", "«günler» — muzâfun ileyh; cem-i mükesser."),
  mazi("رَأَى", "raa", "«decided (saw fit)»", "«uygun gördü»", hidden=None, tags=["naqis-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ"), aziz_fail(),
  an_(obj_of="رَأَى", en_of="«saw fit»", tr_of="«uygun gördü»"),
  mudari("يُرْسِلَ", "arsala", "«(to) send»", "«göndermeyi»", hidden="هُوَ", tags=["an-masdariyya", "form-iv-verbs"]) if False else tok("يُرْسِلَ", "arsala", "verb", ["an-masdariyya", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«(to) send» — in naṣb after an; the doer concealed.", "«göndermeyi» — en ile mansub; fâil gizli."),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), *ila_sijn(punct=".")])
sen("s27", "And the ʿAzīz knew that Yūsuf was innocent.", "Aziz Yusuf'un suçsuz olduğunu biliyordu.", [
  kana(), tok("الْعَزِيزُ", "aziz", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the ʿAzīz» — kāna's ism.", "«Aziz» — kâne'nin ismi."), khabar_kana_mudari("يَعْرِفُ", "arafa", "«knew»", "«biliyordu»"),
  anna(obj_of="يَعْرِفُ"), tok("يُوسُفَ", "yusuf", "propn", ["inna-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the ism of anna.", "«Yusuf» — enne'nin ismi."),
  khabar_inna("بَرِيءٌ", "bari", "«innocent»", "«suçsuz»", part="أَنَّ", punct=".")])
sen("s28", "And Yūsuf entered the prison.", "Ve Yusuf hapse girdi.", [
  mazi("وَدَخَلَ", "dakhala", "«entered»", "«girdi»", hidden=None, wa=True), yusuf_fail(), maful("السِّجْنَ", "sijn", "«the prison»", "«hapse»", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "dalw": G("dalw", "دَلْو", "د ل و", "noun", "a bucket (feminine)", "kova (müennes)", 1, plural="دِلَاء"),
 "adla": G("adla", "أَدْلَى", "د ل و", "verb", "to let down (a bucket) — أَدْلَى دَلْوَهُ", "sarkıtmak (kovayı)", 2, form="IV"),
 "nazaa": G("nazaa", "نَزَعَ", "ن ز ع", "verb", "to pull out, to draw up", "çekmek, çıkarmak", 1, form="I"),
 "akhfa": G("akhfa", "أَخْفَى", "خ ف ي", "verb", "to hide (something)", "saklamak, gizlemek", 1, form="IV"),
 "misr": G("misr", "مِصْر", None, "propn", "Egypt (a diptote: feminine proper name)", "Mısır (gayr-i munsarıf: müennes alem)", 1),
 "madud": G("madud", "مَعْدُود", "ع د د", "noun", "counted, few (ism mafʿūl of عَدَّ)", "sayılı, az (adde'nin ism-i mef'ûlü)", 1),
 "shaka": G("shaka", "شَكَا", "ش ك و", "verb", "to complain (شَكَا إِلَى)", "şikâyet etmek", 1, form="I"),
 "kadhib-liar": G("kadhib-liar", "كَاذِب", "ك ذ ب", "noun", "lying, a liar (ism fāʿil of كَذَبَ)", "yalancı (kezebe'nin ism-i fâili)", 1, plural="كَاذِبُونَ"),
 "amin": G("amin", "أَمِين", "أ م ن", "noun", "trustworthy, faithful (ṣifa mushabbaha)", "emin, güvenilir (sıfat-ı müşebbehe)", 1, plural="أُمَنَاء"),
 "khati": G("khati", "خَاطِئ", "خ ط أ", "noun", "wrongdoer, sinner (ism fāʿil of خَطِئَ)", "hata eden, günahkâr (hatıe'nin ism-i fâili)", 1, plural="خَاطِئُونَ"),
 "ghadab": G("ghadab", "غَضَب", "غ ض ب", "noun", "anger (maṣdar of غَضِبَ)", "öfke (gadıbe'nin masdarı)", 1),
 "sijn": G("sijn", "سِجْن", "س ج ن", "noun", "a prison", "hapishane, zindan", 1, plural="سُجُون"),
 "ahabb": G("ahabb", "أَحَبّ", "ح ب ب", "noun", "dearer, more beloved (elative of حَبِيب)", "daha sevimli, daha sevgili (habîb'in ism-i tafdili)", 2),
 "bari": G("bari", "بَرِيء", "ب ر أ", "noun", "innocent, free of blame", "suçsuz, berî", 1, plural="بُرَآء"),
 "idhan-jawab": G("idhan-jawab", "إِذَنْ", None, "part", "then, in that case (the particle of answer; it governs the muḍāriʿ in naṣb only when it opens the clause and the verb follows directly)", "öyleyse, o hâlde (cevap harfi; muzâriyi ancak cümle başında ve fiil hemen ardından gelince nasb eder)", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("jamaa", "جماعة"), ("bahatha", "بحث"), ("thaqil", "ثقيل"), ("akhraja", "أخرج"), ("nada", "نادى"), ("bushra", "بشرى"), ("suq", "سوق"), ("ishtara", "اشترى"), ("dirham", "درهم"), ("tajir", "تاجر"), ("qasr", "قصر"), ("imraa", "امرأة"), ("akrama", "أكرم"), ("rawada", "راود"), ("khiyana", "خيانة"), ("aba", "أبى"), ("kalla", "كلا"), ("khana", "خان"), ("ahsana", "أحسن"), ("jamal", "جمال"), ("malak", "ملك"), ("karim", "كريم"), ("bada", "بعد"), ("dakhala", "دخل"), ("qama", "قام"), ("rajul", "رجل"), ("pron-2fs", "ك"), ("in-nafiya", "إن"), ("illa", "إلا")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e, _k
    _w = bare(_e["lemma"]).split(" ")[0].replace("ِ", "")
    assert _w.replace("ال", "", 1) == _lm.replace("ال", "", 1) or _w == _lm or _w.startswith(_lm) or _lm.startswith(_w.lstrip("ـ")), (_k, _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k in ("adla", "nazaa", "akhfa", "shaka"): mo["verbs"].pop(_k, None)
put_morph(mo, "adla", _sg.derived_naqis("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَدْلَ", "دْل", "i", "أَدْل", "إِدْلَاء", "مُدْلٍ (الْمُدْلِي)", "مُدْلًى (الْمُدْلَى)", "أُدْلِيَ", "يُدْلَى", note="مُتَعَدٍّ: أَدْلَى دَلْوَهُ — نَاقِصٌ وَاوِيٌّ تُقْلَبُ وَاوُهُ يَاءً فِي الْمَزِيدِ."))
put_morph(mo, "nazaa", _sg.sound1("fataha", "نَزَع", "نْزَع", "اِنْزَع", "نَزْع", "نَازِع", "مَنْزُوع", "نُزِعَ", "يُنْزَعُ", note="مُتَعَدٍّ — حَلْقِيُّ الْعَيْنِ فَبَابُهُ فَتَحَ."))
put_morph(mo, "akhfa", _sg.derived_naqis("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَخْفَ", "خْف", "i", "أَخْف", "إِخْفَاء", "مُخْفٍ (الْمُخْفِي)", "مُخْفًى (الْمُخْفَى)", "أُخْفِيَ", "يُخْفَى", note="مُتَعَدٍّ: أَخْفَاهُ — ضِدُّ أَظْهَرَهُ."))
put_morph(mo, "shaka", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "شَكَ", "شْك", "u", "اُشْك", "شَكْوَى", "شَاكٍ (الشَّاكِي)", "مَشْكُوّ", "شُكِيَ", "يُشْكَى", note="يَتَعَدَّى بِإِلَى: شَكَا إِلَيْهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 11 (print pp. 36–38, «أَحْسَنُ الْقَصَصِ» sections 7 «مِنَ الْبِئْرِ إِلَى الْقَصْر» and 8 «الْوَفَاءُ وَالْأَمَانَة»): the caravan, the bucket and the cry of Yūsuf 12:19 «يَا بُشْرَى هٰذَا غُلَامٌ» as the print sets it with the muṣḥaf's joined يٰبُشْرَى (s7, marked), the market of Egypt and the ʿAzīz (s9–s14); the wife's attempt and Yūsuf's refusal (s15–s18), the ʿAzīz's verdict with Yūsuf 12:29 (s22, marked), the city's wonder with Yūsuf 12:31 as the print sets it, its two clauses parted by the print's comma (s23, marked), «السِّجْنُ أَحَبُّ إِلَيَّ» of 12:33 (s25, marked) and the prison (s26–s28). "
          "One printed line is one sentence, split at the print's own full stops and question marks where a line holds several (s9–s11, s16–s17); s14 and s24 join the print's saying verb to the speech that follows its colon; the print's parentheses around the ayas are read as quotation marks.")
ADD_TR = (" On birinci bölüm (basılı s. 36–38, «أَحْسَنُ الْقَصَصِ» 7. kısım «مِنَ الْبِئْرِ إِلَى الْقَصْر» ve 8. kısım «الْوَفَاءُ وَالْأَمَانَة»): kervan, kova ve Yûsuf 12:19'un «يَا بُشْرَى هٰذَا غُلَامٌ» nidâsı baskıdaki şekliyle, mushafın bitişik يٰبُشْرَى imlâsıyla (s7, işaretli), Mısır çarşısı ve Aziz (s9–s14); kadının teşebbüsü ve Yusuf'un reddi (s15–s18), Aziz'in Yûsuf 12:29 ile hükmü (s22, işaretli), şehrin hayreti Yûsuf 12:31 ile baskıdaki şekliyle, iki cümlesi baskının virgülüyle ayrılmış (s23, işaretli), 12:33'ün «السِّجْنُ أَحَبُّ إِلَيَّ» sözü (s25, işaretli) ve zindan (s26–s28). "
          "Basılı her satır bir cümledir; birden çok cümle taşıyan satırlar baskının noktalarından ve soru işaretlerinden bölünmüştür (s9–s11, s16–s17); s14 ve s24 baskının söyleme fiilini iki noktadan sonraki sözle birleştirir; baskının âyetleri saran parantezleri tırnak olarak okunmuştur.")
write_out(11, S, TITLE, ADD_EN, ADD_TR, "pp. 36–38", GLOSS_ADD)
report(11, S, GLOSS_ADD, ())
