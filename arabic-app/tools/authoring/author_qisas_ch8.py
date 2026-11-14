# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 8: «رُؤْيَا عَجِيبَةٌ وَحَسَدُ الْإِخْوَةِ» — the opening of «أَحْسَنُ الْقَصَصِ» (the Yūsuf cycle),
sections 1–2 (print pp. 27–30): the boy Yūsuf and his dream, Yūsuf 12:4 as the print sets it (marked), Yaʿqūb's reading of it and his
warning; Binyāmīn, the brothers' envy, their council and the well. Every printed line is one sentence, split at the print's own
full stops; the vowelling is the print's.  python3 tools/authoring/author_qisas_ch8.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "رُؤْيَا عَجِيبَةٌ وَحَسَدُ الْإِخْوَةِ", "en": "A strange dream, and the brothers' envy", "tr": "Acayip bir rüya ve kardeşlerin kıskançlığı"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- local helpers
def yusuf_fail(punct=None): return fail_name("يُوسُفُ", "yusuf", "«Yūsuf»", "«Yusuf»", punct=punct)
def yaqub_fail(punct=None): return fail_name("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", punct=punct)
def name_ism_kana(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — kāna's ism, in rafʿ; a diptote name.", tr + " — kâne'nin ismi, merfû; gayr-i munsarıf özel isim.", punct=punct)
def yusuf_ism_kana(punct=None): return name_ism_kana("يُوسُفُ", "yusuf", "«Yūsuf»", "«Yusuf»", punct=punct)
def yaqub_ism_kana(punct=None): return name_ism_kana("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", punct=punct)
def name_maful(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "propn", ["maful-bihi", "mamnu-min-sarf"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the object; a diptote name.", tr + " — mef'ûl-i bih; gayr-i munsarıf özel isim.", punct=punct)
def name_atf(full, lex, en, tr, head, case, punct=None):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ"}[case]
    return tok(full, lex, "propn", ["atf-nasaq", "mamnu-min-sarf"], f"الْوَاوُ عَاطِفَةٌ، وَ{full[2:]} مَعْطُوفٌ عَلَى {head} {C} — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and» + " + en + " — joined to the name before it; a diptote.", "«ve» + " + tr + " — önceki isme atıf; gayr-i munsarıf.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(full[2:], lex, "propn")])
def name_badal(full, lex, en, tr, case, punct=None):
    C = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "rafʿ", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "naṣb", "mansub"), "jarr": ("مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ", "jarr (by a fatḥa)", "mecrur (fetha ile)")}[case]
    return tok(full, lex, "propn", ["badal", "mamnu-min-sarf"], f"بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) {C[0]} — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + f" — the badal of the word before, in {C[1]}; a diptote.", tr + f" — öncekinin bedeli, {C[2]}; gayr-i munsarıf.", punct=punct)
def name_mudaf_ilayh(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the muḍāf ilayh, jarr by a fatḥa; a diptote.", tr + " — muzâfun ileyh, fetha ile mecrur; gayr-i munsarıf.", punct=punct)
def khabar_kana(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [K] + list(tags), "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — kāna's khabar, in naṣb.", tr + " — kâne'nin haberi, mansub.", punct=punct)
def nat_nasb(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["naat-sifa"] + list(tags), "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the naʿt, in naṣb.", tr + " — sıfat, mansub.", punct=punct)
def nat_raf(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", ["naat-sifa"] + list(tags), "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — the naʿt, in rafʿ.", tr + " — sıfat, merfû.", punct=punct)
def kana_hidden(full="وَكَانَ", wa=True, punct=None):
    return tok(full, "kana", "verb", [K, "hollow-verbs"], W(wa) + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", Wen(wa) + "«he was» — kāna with its ism «he» concealed.", Wtr(wa) + "«o … idi» — kâne; ismi gizli «o».", punct=punct, segments=(wa_("كَانَ", "kana", "verb") if wa else None))
def khabar_kana_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", extra=""):
    return tok(full, lex, "verb", [K, "mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + (extra or "بِالضَّمَّةِ") + f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden} — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — a muḍāriʿ; the clause is kāna's khabar.", tr + " — muzâri; cümle kâne'nin haberidir.")
def lahu(full, pron_seg, pron_lex, role_ar, en, tr, tags=(), punct=None):
    return tok(full, "li", "prep", ["huruf-jarr"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — " + role_ar, en, tr, punct=punct, segments=[seg("لَ", "li", "prep"), seg(pron_seg, pron_lex, "pron")])
def ahada_ashara(role_ar, en, tr, punct=None, tags=()):
    """أَحَدَ عَشَرَ — the compound number, both halves built on fatḥa; the seat is stated on the first."""
    return [tok("أَحَدَ", "ahad", "noun", list(tags), "عَدَدٌ مُرَكَّبٌ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ " + role_ar, "«eleven (one-)» — the compound number, both halves built on fatḥa; " + en, "«on bir (bir-)» — bileşik sayı, iki parçası da fetha üzere mebnî; " + tr),
            tok("عَشَرَ", "ashar", "noun", list(tags), "عَجُزُ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ.", "«-teen (ten)» — the second half of the compound number, built on fatḥa.", "«on» — bileşik sayının ikinci yarısı, fetha üzere mebnî.", punct=punct)]
def tamyiz(full, lex, en, tr, punct=None):
    return tok(full, lex, "noun", ["tamyiz"], "تَمْيِيزُ الْعَدَدِ مَنْصُوبٌ بِالْفَتْحَةِ — مُفْرَدٌ بَعْدَ أَحَدَ عَشَرَ.", en + " — the tamyīz of the number, singular and in naṣb.", tr + " — sayının temyizi, müfred ve mansub.", punct=punct)
def kathiran(punct=None):
    return tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ.", "«much, greatly» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct=punct)
def akthar(punct=None):
    return tok("أَكْثَرَ", "akthar", "noun", ["maful-mutlaq", "ism-tafdil", "mamnu-min-sarf"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (حُبًّا أَكْثَرَ) — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more» — standing in for the absolute object; an elative, a diptote.", "«daha çok» — mef'ûl-i mutlak nâibi; ism-i tafdil, gayr-i munsarıf.", punct=punct)
def ruya(case, role_ar, en, tr, punct=None, tags=(), full=None, al=True):
    """الرُّؤْيَا — a فُعْلَى noun on the alif of femininity: the case is estimated on the alif."""
    full = full or ("الرُّؤْيَا" if al else "رُؤْيَا")
    return tok(full, "ruya-dream", "noun", list(tags) + ["ism-maqsur-manqus"], role_ar + " " + {"raf": "مَرْفُوعٌ بِضَمَّةٍ", "nasb": "مَنْصُوبٌ بِفَتْحَةٍ", "jarr": "مَجْرُورٌ بِكَسْرَةٍ"}[case] + " مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَقْصُورٌ.", en + " — the case estimated on the alif (a maqṣūr).", tr + " — hareke elif üzerinde takdîrî (maksûr).", punct=punct)
def bi_hadhihi(punct=None):
    return tok("بِهٰذِهِ", "hadhihi", "pron", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«with this» — the bāʾ of jarr on the demonstrative.", "«bu … ile» — cer bâsı ism-i işârette.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("هٰذِهِ", "hadhihi", "pron")])
def ya_abati():
    return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
            tok("أَبَتِ", "ab", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالتَّاءُ عِوَضٌ عَنْ يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ.", "«O my father» — a vocative annexed to the speaker's yāʾ; the tāʾ stands in for the dropped yāʾ, the kasra is its trace.", "«ey babacığım» — mütekellim yâsına muzâf münâdâ; tâ hazfedilen yânın ivazı, kesre yânın izidir.")]
def fi(punct=None): return tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(): return tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on, upon».", "«üzerine».")
def ila(): return tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e».")
def min_(punct=None): return tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from, of».", "«-den».", punct=punct)
def mudaf_jarr(full, lex, en, tr, prep, punct=None, tags=()):
    return tok(full, lex, "noun", ["huruf-jarr", "idafa-definiteness"] + list(tags), f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", en + " — in jarr; a muḍāf.", tr + " — mecrur; muzâf.", punct=punct)
def mudaf_pron(full, lex, pron_seg, pron_lex, role_ar, en, tr, tags=(), punct=None):
    host = full[:len(full) - len(pron_seg)]
    return tok(full, lex, "noun", list(tags) + ["idafa-definiteness"], role_ar + "، وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", en + " — annexed to the pronoun.", tr + " — zamire muzâf.", punct=punct, segments=[seg(host, lex, "noun"), seg(pron_seg, pron_lex, "pron")])
def verb_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), hidden="هُوَ", punct=None, wa=False, mudari=True, extra=""):
    host = full[:len(full) - len(pron_seg)]
    segs = ([seg("وَ", "wa", "conj"), seg(host[2:], lex, "verb")] if wa else [seg(host, lex, "verb")]) + [seg(pron_seg, pron_lex, "pron")]
    ar = W(wa) + ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ" if mudari else "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ") + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + "، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + extra + "."
    return tok(full, lex, "verb", list(tags) + ["maful-bihi"] + (["mudari-marfu"] if mudari else []), ar, Wen(wa) + en + " — the attached pronoun is its object.", Wtr(wa) + tr + " — bitişik zamir mef'ûlüdür.", punct=punct, segments=segs)
def khamsa_enc(full, lex, pron_seg, pron_lex, en, tr, tags=(), punct=None, wa=False, extra=""):
    host = full[:len(full) - len(pron_seg)]
    segs = ([seg("وَ", "wa", "conj"), seg(host[2:], lex, "verb")] if wa else [seg(host, lex, "verb")]) + [seg(pron_seg, pron_lex, "pron")]
    return tok(full, lex, "verb", list(tags) + ["afal-khamsa", "mudari-marfu", "maful-bihi"], W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + extra + ".", Wen(wa) + en + " — one of the five verbs; the wāw its doer, the attached pronoun its object.", Wtr(wa) + tr + " — ef'âl-i hamseden; vâv fâil, bitişik zamir mef'ûl.", punct=punct, segments=segs)
def amr_pl(full, lex, en, tr, pron_seg=None, pron_lex=None, tags=(), punct=None, wa=False):
    host = full if not pron_seg else full[:len(full) - len(pron_seg)]
    segs = None
    if wa or pron_seg: segs = ([seg("وَ", "wa", "conj"), seg(host[2:], lex, "verb")] if wa else [seg(host, lex, "verb")]) + ([seg(pron_seg, pron_lex, "pron")] if pron_seg else [])
    return tok(full, lex, "verb", list(tags) + ["imperative-amr"] + (["maful-bihi"] if pron_seg else []), W(wa) + "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ" + ("، وَالضَّمِيرُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" if pron_seg else "") + ".", Wen(wa) + en + " — a plural imperative, built on the dropping of the nūn; the wāw its doer" + (", the pronoun its object." if pron_seg else "."), Wtr(wa) + tr + " — nûnun hazfi üzere mebnî cemi emir; vâv fâil" + (", zamir mef'ûl." if pron_seg else "."), punct=punct, segments=segs)
def ikhwa(full, case, role_ar, en, tr, punct=None, tags=()):
    return tok(full, "akh", "noun", list(tags) + ["jam-taksir"], role_ar + " " + {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case] + " — جَمْعُ تَكْسِيرٍ.", en + " — a broken plural of أَخ.", tr + " — «kardeş»in cem-i mükesseri.", punct=punct)
def qala_h(full="قَالَ", wa=False, punct=None, fa=False):
    t = qala(full=full, punct=punct, wa=wa, hidden="هُوَ")
    if fa: t["segments"] = [seg("فَ", "fa", "conj"), seg(full[2:], "qala", "verb")]; t["irab"]["ar"] = "الْفَاءُ عَاطِفَةٌ، وَ" + t["irab"]["ar"]
    return t

# ================================================================ §1 رؤيا عجيبة (pp. 27–29)
sen("s1", "Yūsuf was a small boy, and he had eleven brothers.", "Yusuf küçük bir çocuktu ve on bir kardeşi vardı.", [
  kana(full="كَانَ", wa=False), yusuf_ism_kana(), khabar_kana("وَلَدًا", "walad", "«a boy»", "«bir çocuk»"), nat_nasb("صَغِيرًا", "saghir", "«small»", "«küçük»", punct="،"),
  kana(), lahu("لَهُ", "هُ", "pron-3ms", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«he had» (lit. «to him») — kāna's khabar, fronted.", "«vardı» (harfiyen «ona») — kâne'nin öne alınmış haberi.", tags=[K]),
  *ahada_ashara("فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ مُؤَخَّرٌ.", "kāna's delayed ism.", "kâne'nin geciktirilmiş ismi.", tags=[K]), tamyiz("أَخًا", "akh", "«brother(s)»", "«kardeş»", punct=".")])
sen("s2", "And Yūsuf was a handsome boy, and Yūsuf was a clever boy.", "Ve Yusuf güzel bir çocuktu; Yusuf zeki bir çocuktu.", [
  kana(), yusuf_ism_kana(), khabar_kana("غُلَامًا", "ghulam", "«a boy»", "«bir çocuk»"), nat_nasb("جَمِيلًا", "jamil", "«handsome»", "«güzel»", punct="،"),
  kana(), yusuf_ism_kana(), khabar_kana("غُلَامًا", "ghulam", "«a boy»", "«bir çocuk»"), nat_nasb("ذَكِيًّا", "dhaki", "«clever»", "«zeki»", punct=".")])
sen("s3", "And his father Yaʿqūb loved him more than all his brothers.", "Ve babası Yakub onu bütün kardeşlerinden daha çok seviyordu.", [
  kana(),
  tok("أَبُوهُ", "ab", "noun", [K, "five-nouns", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — kāna's ism, rafʿ by the wāw of the five nouns; annexed to «his».", "«babası» — kâne'nin ismi, esmâ-i hamseden olduğu için vâv ile merfû; «onun»a muzâf.", segments=[seg("أَبُو", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  name_badal("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", "raf"),
  verb_enc("يُحِبُّهُ", "ahabba", "هُ", "pron-3ms", "«loved him»", "«onu seviyordu»", tags=[K, "form-iv-verbs", "doubled-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  akthar(), min_(), mudaf_jarr("جَمِيعِ", "jami", "«all»", "«bütün»", "مِنْ"),
  mudaf_pron("إِخْوَتِهِ", "akh", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تَكْسِيرٍ", "«his brothers» — the muḍāf ilayh", "«kardeşleri» — muzâfun ileyh", punct=".")])
sen("s4", "One night Yūsuf saw a strange dream.", "Bir gece Yusuf acayip bir rüya gördü.", [
  tok("ذَاتَ", "dhat", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«one (night)» — an adverb of time in naṣb; annexed.", "«bir (gece)» — mansub zaman zarfı; muzâf."),
  tok("لَيْلَةٍ", "layla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«night» — the muḍāf ilayh.", "«gece» — muzâfun ileyh."),
  tok("رَأَى", "raa", "verb", ["naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«saw» — a māḍī, the fatḥa estimated on the alif.", "«gördü» — elif üzerinde takdîrî fetha üzere mebnî mâzî."), yusuf_fail(),
  ruya("nasb", "مَفْعُولٌ بِهِ", "«a dream» — the object", "«bir rüya» — mef'ûl-i bih", tags=["maful-bihi", "mamnu-min-sarf"], al=False),
  nat_nasb("عَجِيبَةً", "ajib", "«strange»", "«acayip»", punct=".")])
sen("s5", "He saw eleven stars, and he saw the sun and the moon — each bowing down to him.", "On bir yıldız gördü; güneşi ve ayı gördü: hepsi ona secde ediyordu.", [
  mazi("رَأَى", "raa", "«he saw»", "«gördü»", hidden="هُوَ", tags=["naqis-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ"),
  *ahada_ashara("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "the object.", "mef'ûl-i bih.", tags=["maful-bihi"]), tamyiz("كَوْكَبًا", "kawkab", "«star(s)»", "«yıldız»"),
  mazi("وَرَأَى", "raa", "«and he saw»", "«ve gördü»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "naqis-verbs"], extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ"),
  maful("الشَّمْسَ", "shams", "«the sun»", "«güneşi»"),
  tok("وَالْقَمَرَ", "qamar", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْقَمَرَ مَعْطُوفٌ عَلَى الشَّمْسَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and the moon» — joined to «the sun», in naṣb.", "«ve ayı» — «güneş»e atıf, mansub.", segments=[seg("وَ", "wa", "conj"), seg("الْقَمَرَ", "qamar", "noun")]),
  tok("كُلٌّ", "kull", "noun", ["mubtada-khabar", "hal"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ (كُلُّهُمْ) — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«each» — the mubtadaʾ, its tanwīn standing in for the dropped muḍāf ilayh; the clause is a ḥāl.", "«hepsi» — mübtedâ; tenvin hazfedilen muzâfun ileyhin ivazıdır; cümle hâldir."),
  tok("يَسْجُدُ", "sajada", "verb", ["mubtada-khabar", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«bows down» — the khabar clause.", "«secde eder» — haber cümlesi."),
  lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِيَسْجُدُ.", "«to him».", "«ona».", punct=".")])
sen("s6", "Young Yūsuf wondered greatly!", "Küçük Yusuf çok şaşırdı!", [
  mazi("تَعَجَّبَ", "taajjaba", "«wondered»", "«şaşırdı»", hidden=None, tags=["form-v-verbs"]), yusuf_fail(), nat_raf("الصَّغِيرُ", "saghir", "«the young»", "«küçük»"), kathiran(punct="!")])
sen("s7", "He did not understand this dream: how do the stars and the sun and the moon bow down to a man?", "Bu rüyayı anlamadı: yıldızlar, güneş ve ay bir adama nasıl secde eder?", [
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
  mazi("فَهِمَ", "fahima", "«understood»", "«anladı»", hidden="هُوَ"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«this»", "«bu»"),
  ruya("nasb", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«dream» — the badal of the demonstrative", "«rüya» — ism-i işâretin bedeli", tags=["badal"]),
  tok("كَيْفَ", "kayfa", "noun", ["al-istifham", "hal"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — the question noun, built; in the place of naṣb as a ḥāl.", "«nasıl» — istifham ismi, mebnî; mahallen mansub hâl."),
  tok("تَسْجُدُ", "sajada", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«bow down» — a muḍāriʿ; its doer follows.", "«secde eder» — muzâri; fâili sonra gelir."),
  tok("الْكَوَاكِبُ", "kawkab", "noun", ["fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ.", "«the stars» — the doer; a broken plural.", "«yıldızlar» — fâil; cem-i mükesser."),
  tok("وَالشَّمْسُ", "shams", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالشَّمْسُ مَعْطُوفٌ عَلَى الْكَوَاكِبُ مَرْفُوعٌ بِالضَّمَّةِ.", "«and the sun» — joined to the doer.", "«ve güneş» — fâile atıf.", segments=[seg("وَ", "wa", "conj"), seg("الشَّمْسُ", "shams", "noun")]),
  tok("وَالْقَمَرُ", "qamar", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْقَمَرُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and the moon» — joined.", "«ve ay» — atıf.", segments=[seg("وَ", "wa", "conj"), seg("الْقَمَرُ", "qamar", "noun")]),
  tok("لِرَجُلٍ", "rajul", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَرَجُلٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«to a man» — the jarr lām on an indefinite noun.", "«bir adama» — cer lâmı nekre isimde.", punct="؟", segments=[seg("لِ", "li", "prep"), seg("رَجُلٍ", "rajul", "noun")])])
sen("s8", "Young Yūsuf went to his father Yaʿqūb and told him this strange dream.", "Küçük Yusuf babası Yakub'a gitti ve ona bu acayip rüyayı anlattı.", [
  mazi("ذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None), yusuf_fail(), nat_raf("الصَّغِيرُ", "saghir", "«the young»", "«küçük»"), ila(),
  tok("أَبِيهِ", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — in jarr by the yāʾ of the five nouns; annexed to «his».", "«babası» — esmâ-i hamseden olduğu için yâ ile mecrur; «onun»a muzâf.", segments=[seg("أَبِي", "ab", "noun"), seg("هِ", "pron-3ms", "pron")]),
  name_badal("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub»", "jarr"),
  tok("وَحَكَى", "haka", "verb", ["atf-nasaq", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَحَكَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and told» — joined; the fatḥa estimated on the alif.", "«ve anlattı» — atıf; fetha elif üzerinde takdîrî.", segments=[seg("وَ", "wa", "conj"), seg("حَكَى", "haka", "verb")]),
  lahu("لَهُ", "هُ", "pron-3ms", "مُتَعَلِّقٌ بِحَكَى.", "«to him».", "«ona»."),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«this»", "«bu»"),
  ruya("nasb", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«dream» — the badal", "«rüya» — bedel", tags=["badal"]),
  tok("الْعَجِيبَةَ", "ajib", "noun", ["naat-sifa"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«strange» — the naʿt.", "«acayip» — sıfat.", punct=".")])
sen("s9", "«He said: O my father, I saw eleven stars and the sun and the moon; I saw them bowing down to me.» (Yūsuf 12:4)", "«Dedi: Babacığım, ben on bir yıldızla güneşi ve ayı gördüm; onları bana secde ederken gördüm.» (Yûsuf 12:4)", quran([
  qala_h(punct=None), *ya_abati(),
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the speaker's yāʾ as its ism, the nūn of protection between.", "«şüphesiz ben» — inne; mütekellim yâsı ismi, arada vikāye nûnu.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("رَأَيْتُ", "raa", "verb", ["inna-wa-akhawatuha", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«I saw» — a māḍī built on sukūn before the doer's tāʾ; the clause is inna's khabar.", "«gördüm» — fâil tâsı sebebiyle sükûn üzere mebnî mâzî; cümle inne'nin haberidir."),
  *ahada_ashara("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "the object.", "mef'ûl-i bih.", tags=["maful-bihi"]), tamyiz("كَوْكَبًا", "kawkab", "«star(s)»", "«yıldız»"),
  tok("وَالشَّمْسَ", "shams", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالشَّمْسَ مَعْطُوفٌ عَلَى أَحَدَ عَشَرَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and the sun» — joined to the object.", "«ve güneşi» — mef'ûle atıf.", segments=[seg("وَ", "wa", "conj"), seg("الشَّمْسَ", "shams", "noun")]),
  tok("وَالْقَمَرَ", "qamar", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْقَمَرَ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and the moon» — joined.", "«ve ayı» — atıf.", segments=[seg("وَ", "wa", "conj"), seg("الْقَمَرَ", "qamar", "noun")]),
  tok("رَأَيْتُهُمْ", "raa", "verb", ["maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ اسْتِئْنَافٌ بَيَانِيٌّ.", "«I saw them» — the tāʾ its doer, «them» its object; the clause restates the first.", "«onları gördüm» — tâ fâil, «onlar» mef'ûl; cümle ilkini açıklayan isti'nâftır.", segments=[seg("رَأَيْتُ", "raa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("لِي", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِسَاجِدِينَ.", "«to me» — attached to «bowing».", "«bana» — «secde eden»e bağlı.", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  tok("سَاجِدِينَ", "sajid", "noun", ["hal", "jam-mudhakkar-salim"], "حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«bowing down» — the ḥāl, naṣb by the yāʾ of the sound masculine plural.", "«secde ederken» — hâl, cem-i müzekker sâlim olduğu için yâ ile mansub.", punct=".")]))
sen("s10", "And his father Yaʿqūb was a prophet.", "Ve babası Yakub bir peygamberdi.", [
  kana(),
  tok("أَبُوهُ", "ab", "noun", [K, "five-nouns", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — kāna's ism, rafʿ by the wāw of the five nouns.", "«babası» — kâne'nin ismi, vâv ile merfû.", segments=[seg("أَبُو", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  name_badal("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»", "raf"), khabar_kana("نَبِيًّا", "nabi", "«a prophet»", "«bir peygamber»", punct=".")])
sen("s11", "Yaʿqūb rejoiced greatly at this dream.", "Yakub bu rüyaya çok sevindi.", [
  mazi("فَرِحَ", "fariha", "«rejoiced»", "«sevindi»", hidden=None), yaqub_fail(), bi_hadhihi(),
  ruya("jarr", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«dream» — the badal, in jarr", "«rüya» — bedel, mecrur", tags=["badal"]), kathiran(punct=".")])
sen("s12", "And he said: May Allah bless you, Yūsuf; you shall have a high standing.", "Ve dedi: Allah seni mübarek kılsın ey Yusuf; senin büyük bir şanın olacak.", [
  qala_h(wa=True, punct=None),
  mazi("بَارَكَ", "baraka-bless", "«may … bless»", "«mübarek kılsın»", hidden=None, tags=["form-iii-verbs"], extra_ar=" — دُعَاءٌ بِلَفْظِ الْخَبَرِ"), allah_fail(),
  lahu("لَكَ", "كَ", "pron-2ms", "مُتَعَلِّقٌ بِبَارَكَ.", "«you» (lit. «for you»).", "«seni» (harfiyen «senin için»)."),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("يُوسُفُ", "yusuf", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Yūsuf» — a single-name vocative, built on ḍamma in the place of naṣb.", "«Yusuf» — müfred alem münâdâ, zamme üzere mebnî, mahallen mansub.", punct="،"),
  tok("فَسَيَكُونُ", "kana", "verb", [K, "hollow-verbs", "mudari-marfu"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَالسِّينُ لِلتَّنْفِيسِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«so there shall be» — the fāʾ of resumption, the sīn of the future, and kāna's muḍāriʿ.", "«artık … olacak» — isti'nâf fâsı, gelecek sîni ve kâne'nin muzârisi.", segments=[seg("فَ", "fa", "conj"), seg("سَ", "sa", "part"), seg("يَكُونُ", "kana", "verb")]),
  lahu("لَكَ", "كَ", "pron-2ms", "وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُونُ مُقَدَّمٌ.", "«you (shall have)» — the fronted khabar of yakūn.", "«senin … olacak» — yekûn'un öne alınmış haberi.", tags=[K]),
  tok("شَأْنٌ", "shan", "noun", [K], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a (high) standing» — yakūn's ism, delayed.", "«bir şan» — yekûn'un geciktirilmiş ismi.", punct=".")])
sen("s13", "This dream is good tidings of knowledge and prophethood.", "Bu rüya ilim ve peygamberlik müjdesidir.", [
  ishara("هٰذِهِ", "hadhihi", "raf", "«this»", "«bu»"),
  ruya("raf", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«dream» — the badal of the demonstrative", "«rüya» — ism-i işâretin bedeli", tags=["badal"]),
  tok("بِشَارَةٌ", "bishara", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«good tidings» — the khabar.", "«müjde» — haber."),
  tok("بِعِلْمٍ", "ilm", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَعِلْمٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«of knowledge» — the bāʾ of jarr.", "«ilim ile» — cer bâsı.", segments=[seg("بِ", "bi", "prep"), seg("عِلْمٍ", "ilm", "noun")]),
  tok("وَنُبُوَّةٍ", "nubuwwa", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَنُبُوَّةٍ مَعْطُوفٌ عَلَى عِلْمٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«and prophethood» — joined to «knowledge», in jarr.", "«ve peygamberlik» — «ilim»e atıf, mecrur.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("نُبُوَّةٍ", "nubuwwa", "noun")])])
def qad_anama(first):
    return [tok("وَقَدْ", "qad", "part", ["qad-harf"], ("الْوَاوُ اسْتِئْنَافِيَّةٌ" if first else "الْوَاوُ عَاطِفَةٌ") + "، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — qad of confirmation before a māḍī.", "«ve gerçekten» — tahkik harfi kad.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
            mazi("أَنْعَمَ", "anama", "«bestowed favour»", "«nimet verdi»", hidden=None, tags=["form-iv-verbs"]), allah_fail(), ala(),
            mudaf_pron("جَدِّكَ", "jadd", "كَ", "pron-2ms", "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«your grandfather» — in jarr", "«deden» — mecrur", tags=["huruf-jarr"])]
sen("s14", "And Allah has indeed bestowed His favour on your grandfather Isḥāq, and Allah has bestowed His favour on your grandfather Ibrāhīm.", "Ve gerçekten Allah deden İshak'a nimet verdi; Allah deden İbrâhim'e de nimet verdi.", [
  *qad_anama(True), name_badal("إِسْحٰقَ", "ishaq", "«Isḥāq»", "«İshak»", "jarr"),
  *qad_anama(False), name_badal("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", "jarr", punct=".")])
sen("s15", "And He bestows His favour on you and bestows His favour on the house of Yaʿqūb.", "Ve O sana nimet verir, Yakub ailesine de nimet verir.", [
  tok("وَإِنَّهُ", "inna", "part", ["inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«and indeed He» — inna with its ism «He» attached.", "«ve şüphesiz O» — inne ve ismi «O».", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("يُنْعِمُ", "anama", "verb", ["inna-wa-akhawatuha", "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«bestows favour» — the clause is inna's khabar.", "«nimet verir» — cümle inne'nin haberidir."),
  tok("عَلَيْكَ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ.", "«on you».", "«sana».", segments=[seg("عَلَيْ", "ala", "prep"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَيُنْعِمُ", "anama", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُنْعِمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and bestows favour» — joined.", "«ve nimet verir» — atıf.", segments=[seg("وَ", "wa", "conj"), seg("يُنْعِمُ", "anama", "verb")]),
  ala(), mudaf_jarr("آلِ", "al-family", "«the house (of)»", "«ailesi»", "عَلَى"), name_mudaf_ilayh("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub»", punct=".")])
sen("s16", "And Yaʿqūb was an old man, and he knew the natures of people.", "Ve Yakub yaşlı bir adamdı; insanların tabiatlarını bilirdi.", [
  kana(), yaqub_ism_kana(), khabar_kana("شَيْخًا", "shaykh", "«an old man»", "«bir ihtiyar»"), nat_nasb("كَبِيرًا", "kabir", "«old (great)»", "«yaşlı»", punct="،"),
  kana_hidden(), khabar_kana_mudari("يَعْرِفُ", "arafa", "«knew»", "«bilirdi»"),
  tok("طَبَائِعَ", "tabia", "noun", ["maful-bihi", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«the natures» — the object; a muḍāf; a plural of the ultimate shape (a diptote).", "«tabiatlarını» — mef'ûl; muzâf; müntehe'l-cümû' kalıbı (gayr-i munsarıf)."),
  tok("النَّاسِ", "nas", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«people» — the muḍāf ilayh.", "«insanların» — muzâfun ileyh.", punct=".")])
sen("s17", "And he knew how Satan overcomes, and how Satan plays with man.", "Ve şeytanın nasıl galip geldiğini, şeytanın insanla nasıl oynadığını bilirdi.", [
  kana_hidden(), khabar_kana_mudari("يَعْرِفُ", "arafa", "«knew»", "«bilirdi»"),
  tok("كَيْفَ", "kayfa", "noun", ["al-istifham", "hal"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيَعْرِفُ.", "«how» — the question noun as a ḥāl; its clause is the object of «knew».", "«nasıl» — istifham ismi, hâl; cümle «bilirdi»nin mef'ûlüdür."),
  tok("يَغْلِبُ", "ghalaba", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«overcomes» — a muḍāriʿ; its doer follows.", "«galip gelir» — muzâri; fâili sonra gelir."),
  fail("الشَّيْطَانُ", "shaytan", "«Satan»", "«şeytan»", punct="،"),
  tok("وَكَيْفَ", "kayfa", "noun", ["atf-nasaq", "al-istifham", "hal"], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — joined; the question noun as a ḥāl.", "«ve nasıl» — atıf; istifham ismi, hâl.", segments=[seg("وَ", "wa", "conj"), seg("كَيْفَ", "kayfa", "noun")]),
  tok("يَلْعَبُ", "laiba", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«plays» — a muḍāriʿ.", "«oynar» — muzâri."),
  fail("الشَّيْطَانُ", "shaytan", "«Satan»", "«şeytan»"),
  tok("بِالْإِنْسَانِ", "insan", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْإِنْسَانِ مَجْرُورٌ بِالْكَسْرَةِ.", "«with man» — the bāʾ of jarr.", "«insanla» — cer bâsı.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الْإِنْسَانِ", "insan", "noun")])])
sen("s18", "So he said: My son, do not tell this dream to any of your brothers, for they will envy you and become an enemy to you.", "Bunun üzerine dedi: Oğlum, bu rüyayı kardeşlerinden hiçbirine anlatma; çünkü seni kıskanırlar ve sana düşman olurlar.", [
  qala_h(full="فَقَالَ", punct=None, fa=True),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("وَلَدِي", "walad", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my son» — a vocative annexed to the speaker's yāʾ, its fatḥa estimated.", "«oğlum» — mütekellim yâsına muzâf münâdâ, fethası takdîrî.", punct="،", segments=[seg("وَلَدِ", "walad", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("لَا", "la-nahiya", "part", ["la-nahiya"], "لَا نَاهِيَةٌ جَازِمَةٌ.", "«do not» — the prohibiting lā, a jazim.", "«-me» — cezm eden nehiy lâ'sı."),
  tok("تُخْبِرْ", "akhbara", "verb", ["la-nahiya", "lam-jazim", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«tell» — jazm by sukūn after the prohibiting lā; the doer «you» concealed.", "«anlatma» — nehiy lâ'sıyla sükûn ile meczum; fâil gizli «sen»."),
  bi_hadhihi(), ruya("jarr", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«dream» — the badal, in jarr", "«rüya» — bedel, mecrur", tags=["badal"]),
  maful("أَحَدًا", "ahad", "«anyone»", "«hiçbirine»"), min_(),
  mudaf_pron("إِخْوَتِكَ", "akh", "كَ", "pron-2ms", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — جَمْعُ تَكْسِيرٍ", "«your brothers» — in jarr", "«kardeşlerin» — mecrur", tags=["huruf-jarr", "jam-taksir"]),
  tok("فَإِنَّهُمْ", "inna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "الْفَاءُ تَعْلِيلِيَّةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«for they» — the fāʾ of reason and inna with its ism «they».", "«çünkü onlar» — ta'lil fâsı ve inne; ismi «onlar».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  khamsa_enc("يَحْسُدُونَكَ", "hasada", "كَ", "pron-2ms", "«envy you»", "«seni kıskanırlar»", tags=["inna-wa-akhawatuha"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  tok("وَيَكُونُونَ", "kana", "verb", ["atf-nasaq", K, "afal-khamsa", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَكُونُونَ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ اسْمُهَا.", "«and they will be» — kāna's muḍāriʿ among the five verbs; the wāw is its ism.", "«ve olurlar» — kâne'nin muzârisi, ef'âl-i hamseden; vâv ismidir.", segments=[seg("وَ", "wa", "conj"), seg("يَكُونُونَ", "kana", "verb")]),
  lahu("لَكَ", "كَ", "pron-2ms", "مُتَعَلِّقٌ بِعَدُوًّا.", "«to you».", "«sana»."),
  khabar_kana("عَدُوًّا", "aduww", "«an enemy»", "«düşman»", punct=".")])
# ================================================================ §2 حسد الإخوة (pp. 29–30)
sen("s19", "And Yūsuf had another brother, by his mother, whose name was Binyāmīn.", "Ve Yusuf'un annesinden başka bir kardeşi vardı; adı Bünyamin idi.", [
  kana(), yusuf_ism_kana(),
  lahu("لَهُ", "هُ", "pron-3ms", "وَشِبْهُ الْجُمْلَةِ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«had» — the fronted khabar of the clause that is kāna's khabar.", "«vardı» — kâne'nin haberi olan cümlenin öne alınmış haberi.", tags=[K]),
  tok("أَخٌ", "akh", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a brother» — the delayed mubtadaʾ.", "«bir kardeş» — geciktirilmiş mübtedâ."),
  tok("آخَرُ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — the naʿt; a diptote.", "«başka» — sıfat; gayr-i munsarıf."),
  min_(), mudaf_pron("أُمِّهِ", "umm", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", "«his mother» — in jarr", "«annesi» — mecrur", tags=["huruf-jarr"]),
  tok("اسْمُهُ", "ism-name", "noun", ["mubtada-khabar", "idafa-definiteness", "jumla-sifa"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِأَخٌ.", "«his name» — the mubtadaʾ; the clause is a naʿt of «a brother».", "«adı» — mübtedâ; cümle «kardeş»in sıfatıdır.", segments=[seg("اسْمُ", "ism-name", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("بِنْيَامِينُ", "binyamin", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Binyāmīn» — the khabar; a foreign name, a diptote.", "«Bünyamin» — haber; yabancı özel isim, gayr-i munsarıf.", punct=".")])
sen("s20", "And Yaʿqūb loved them both with an intense love, and he loved no one like them.", "Ve Yakub ikisini şiddetli bir sevgiyle severdi; onlar gibi kimseyi sevmezdi.", [
  kana(), yaqub_ism_kana(),
  verb_enc("يُحِبُّهُمَا", "ahabba", "هُمَا", "pron-3d", "«loved them both»", "«ikisini severdi»", tags=[K, "form-iv-verbs", "doubled-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  tok("حُبًّا", "hubb", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a love» — the absolute object.", "«bir sevgi(yle)» — mef'ûl-i mutlak."),
  nat_nasb("شَدِيدًا", "shadid", "«intense»", "«şiddetli»", punct="،"),
  kana_hidden(), la_nafiya(),
  tok("يُحِبُّ", "ahabba", "verb", [K, "la-nafiya", "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«loved» — rafʿ after the negating lā; the clause is kāna's khabar.", "«severdi» — nefiy lâ'sından sonra merfû; cümle kâne'nin haberidir."),
  mudaf_pron("مِثْلَهُمَا", "mithl", "هُمَا", "pron-3d", "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (نَعْتٌ تَقَدَّمَ عَلَى مَوْصُوفِهِ النَّكِرَةِ فَأُعْرِبَ حَالًا)", "«like them» — a ḥāl (a naʿt fronted before its indefinite noun)", "«onlar gibi» — hâl (nekre mevsûfunun önüne geçmiş sıfat)", tags=["hal"]),
  maful("أَحَدًا", "ahad", "«anyone»", "«kimseyi»", punct=".")])
sen("s21", "And the brothers envied Yūsuf and Binyāmīn and grew angry.", "Ve kardeşler Yusuf'u ve Bünyamin'i kıskanıyor ve öfkeleniyorlardı.", [
  kana(), ikhwa("الْإِخْوَةُ", "raf", "اسْمُ كَانَ", "«the brothers» — kāna's ism", "«kardeşler» — kâne'nin ismi", tags=[K]),
  khamsa("يَحْسُدُونَ", "hasada", "«envied»", "«kıskanıyorlardı»", tags=[K], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), name_atf("وَبِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin'i»", "يُوسُفَ", "nasb"),
  khamsa("وَيَغْضَبُونَ", "ghadiba", "«and grew angry»", "«ve öfkeleniyorlardı»", tags=["atf-nasaq"], wa=True, punct=".")])
sen("s22", "They used to say: Why does our father love Yūsuf and Binyāmīn more?", "Derlerdi: Babamız neden Yusuf'u ve Bünyamin'i daha çok seviyor?", [
  tok("كَانُوا", "kana", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ اسْمُهَا.", "«they were» — kāna with the group's wāw as its ism.", "«idiler» — kâne; cemi vâvı ismidir."),
  khamsa("يَقُولُونَ", "qala", "«saying»", "«derlerdi»", tags=[K, "hollow-verbs", "maful-bihi"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", punct=":"),
  tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَذَا زَائِدَةٌ — مُتَعَلِّقٌ بِيُحِبُّ.", "«why» — the jarr lām on the question-mā.", "«neden» — cer lâmı istifham mâ'sında."),
  tok("يُحِبُّ", "ahabba", "verb", ["mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«loves» — a muḍāriʿ; its doer follows.", "«sever» — muzâri; fâili sonra gelir."),
  tok("أَبُونَا", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our father» — the doer, rafʿ by the wāw of the five nouns; annexed to «our».", "«babamız» — fâil, esmâ-i hamseden olduğu için vâv ile merfû; «biz»e muzâf.", segments=[seg("أَبُو", "ab", "noun"), seg("نَا", "pron-1p", "pron")]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), name_atf("وَبِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin'i»", "يُوسُفَ", "nasb"), akthar(punct="؟")])
sen("s23", "And why does our father love Yūsuf and Binyāmīn while they are small and weak?", "Ve babamız Yusuf'u ve Bünyamin'i, ikisi küçük ve zayıfken, neden seviyor?", [
  tok("وَلِمَاذَا", "limadha", "pron", ["atf-nasaq", "al-istifham", "huruf-jarr"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ جَرٍّ.", "«and why» — joined; the jarr lām on the question-mā.", "«ve neden» — atıf; cer lâmı istifham mâ'sında.", segments=[seg("وَ", "wa", "conj"), seg("لِمَاذَا", "limadha", "pron")]),
  tok("يُحِبُّ", "ahabba", "verb", ["mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«loves» — a muḍāriʿ.", "«sever» — muzâri."),
  tok("أَبُونَا", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَنَا مُضَافٌ إِلَيْهِ.", "«our father» — the doer, rafʿ by the wāw.", "«babamız» — fâil, vâv ile merfû.", segments=[seg("أَبُو", "ab", "noun"), seg("نَا", "pron-1p", "pron")]),
  name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"), name_atf("وَبِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin'i»", "يُوسُفَ", "nasb"),
  tok("وَهُمَا", "pron-3d", "pron", ["hal", "anwa-al-waw", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَهُمَا ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while they two» — the wāw of ḥāl; the pronoun is the mubtadaʾ of a ḥāl clause.", "«ikisi … iken» — hâl vâvı; zamir hâl cümlesinin mübtedâsıdır.", segments=[seg("وَ", "wa", "conj"), seg("هُمَا", "pron-3d", "pron")]),
  tok("صَغِيرَانِ", "saghir", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى.", "«small» — the khabar, rafʿ by the alif of the dual.", "«küçük» — haber, tesniye olduğu için elif ile merfû."),
  tok("ضَعِيفَانِ", "daif", "noun", ["naat-sifa", "al-muthanna"], "نَعْتٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«weak» — the naʿt, rafʿ by the alif.", "«zayıf» — sıfat, elif ile merfû.", punct="؟")])
sen("s24", "Why does he not love us like Yūsuf and Binyāmīn, while we are strong young men?", "Bizi neden Yusuf ve Bünyamin gibi sevmiyor; biz güçlü gençleriz!", [
  tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ جَرٍّ.", "«why» — the jarr lām on the question-mā.", "«neden» — cer lâmı istifham mâ'sında."),
  la_nafiya(),
  verb_enc("يُحِبُّنَا", "ahabba", "نَا", "pron-1p", "«does … love us»", "«bizi sever»", tags=["la-nafiya", "form-iv-verbs"]),
  mudaf_pron("مِثْلَ", "mithl", "", "pron-3ms", "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (حُبًّا مِثْلَ حُبِّ يُوسُفَ)", "«like» — standing in for the absolute object", "«gibi» — mef'ûl-i mutlak nâibi", tags=["maful-mutlaq"]) if False else
  tok("مِثْلَ", "mithl", "noun", ["maful-mutlaq", "idafa-definiteness"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (حُبًّا مِثْلَ حُبِّ يُوسُفَ)، وَهُوَ مُضَافٌ.", "«like» — standing in for the absolute object (a love like the love of Yūsuf); a muḍāf.", "«gibi» — mef'ûl-i mutlak nâibi (Yusuf'u sevdiği gibi bir sevgi); muzâf."),
  name_mudaf_ilayh("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf»"), name_atf("وَبِنْيَامِينَ", "binyamin", "«Binyāmīn»", "«Bünyamin»", "يُوسُفَ", "jarr"),
  tok("نَحْنُ", "nahnu", "pron", ["mubtada-khabar", "hal"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ بِلَا وَاوٍ.", "«we» — the mubtadaʾ of a ḥāl clause with no wāw.", "«biz» — vâvsız hâl cümlesinin mübtedâsı."),
  tok("شُبَّانٌ", "shabb", "noun", ["mubtada-khabar", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ.", "«young men» — the khabar; a broken plural.", "«gençler» — haber; cem-i mükesser."),
  tok("أَقْوِيَاءُ", "qawi", "noun", ["naat-sifa", "jam-taksir", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.", "«strong» — the naʿt; barred from tanwīn by the alif of femininity.", "«güçlü» — sıfat; memdûd te'nis elifi sebebiyle tenvinsiz.", punct="،")])
sen("s25", "This is a strange matter.", "Bu acayip bir iştir.", [
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("أَمْرٌ", "amr", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a matter» — the khabar.", "«bir iş» — haber."),
  nat_raf("عَجِيبٌ", "ajib", "«strange»", "«acayip»", punct=".")])
sen("s26", "And Yūsuf was a small boy, so he told the dream to his brothers; and the brothers grew very angry when they heard the dream, and their envy grew intense.", "Ve Yusuf küçük bir çocuktu; rüyayı kardeşlerine anlattı. Kardeşler rüyayı duyunca çok öfkelendiler ve kıskançlıkları şiddetlendi.", [
  kana(), yusuf_ism_kana(), khabar_kana("وَلَدًا", "walad", "«a boy»", "«bir çocuk»"), nat_nasb("صَغِيرًا", "saghir", "«small»", "«küçük»", punct="،"),
  tok("فَحَكَى", "haka", "verb", ["naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَحَكَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«so he told» — the fāʾ of sequence; the doer concealed.", "«ve anlattı» — takip fâsı; fâil gizli.", segments=[seg("فَ", "fa", "conj"), seg("حَكَى", "haka", "verb")]),
  ruya("nasb", "مَفْعُولٌ بِهِ", "«the dream» — the object", "«rüyayı» — mef'ûl-i bih", tags=["maful-bihi"]),
  tok("لِإِخْوَتِهِ", "akh", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَإِخْوَةِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his brothers» — the jarr lām; annexed to «his».", "«kardeşlerine» — cer lâmı; «onun»a muzâf.", segments=[seg("لِ", "li", "prep"), seg("إِخْوَتِ", "akh", "noun"), seg("هِ", "pron-3ms", "pron")]),
  mazi("وَغَضِبَ", "ghadiba", "«and grew angry»", "«ve öfkelendi»", hidden=None, wa=True, tags=["atf-nasaq"]), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi."),
  tok("لَمَّا", "lamma", "part", ["maful-fih"], "لَمَّا ظَرْفٌ بِمَعْنَى حِينَ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِغَضِبَ.", "«when» — a time-adverb (ḥīna), attached to «grew angry».", "«-ınca» — zaman zarfı (hîne), «öfkelendi»ye bağlı."),
  mazi_pl("سَمِعُوا", "samia", "«they heard»", "«duydular»"),
  ruya("nasb", "مَفْعُولٌ بِهِ", "«the dream» — the object", "«rüyayı» — mef'ûl-i bih", tags=["maful-bihi"]),
  tok("وَاشْتَدَّ", "ishtadda", "verb", ["atf-nasaq", "form-viii-verbs", "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاشْتَدَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مُضَعَّفٌ مِنْ بَابِ الِافْتِعَالِ.", "«and grew intense» — joined; a doubled Form-VIII māḍī.", "«ve şiddetlendi» — atıf; iftiâl bâbından muzâaf mâzî.", segments=[seg("وَ", "wa", "conj"), seg("اشْتَدَّ", "ishtadda", "verb")]),
  mudaf_pron("حَسَدُهُمْ", "hasad", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "«their envy» — the doer", "«kıskançlıkları» — fâil", tags=["fail"], punct=".")])
sen("s27", "And the brothers gathered one day and said: Kill Yūsuf, or cast him into a far-off land.", "Ve kardeşler bir gün toplandılar ve dediler: Yusuf'u öldürün, yahut onu uzak bir yere atın.", [
  mazi("وَاجْتَمَعَ", "ijtamaa", "«gathered»", "«toplandı»", hidden=None, wa=True, tags=["form-viii-verbs"]), ikhwa("الْإِخْوَةُ", "raf", "فَاعِلٌ", "«the brothers» — the doer", "«kardeşler» — fâil", tags=["fail"]),
  tok("يَوْمًا", "yawm", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«one day» — an adverb of time.", "«bir gün» — zaman zarfı."),
  qalu(wa=True, punct=None),
  amr_pl("اقْتُلُوا", "qatala", "«kill»", "«öldürün»"), name_maful("يُوسُفَ", "yusuf", "«Yūsuf»", "«Yusuf'u»"),
  tok("أَوِ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ، وَكُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — the joining particle, its kasra for the meeting of two sukūns.", "«yahut» — atıf harfi; iki sâkinin karşılaşması için kesre."),
  amr_pl("اطْرَحُوهُ", "taraha", "«cast him»", "«onu atın»", pron_seg="هُ", pron_lex="pron-3ms", tags=["atf-nasaq"]),
  tok("أَرْضًا", "ard", "noun", ["maful-fih"], "مَفْعُولٌ فِيهِ مَنْصُوبٌ بِالْفَتْحَةِ (عَلَى تَقْدِيرِ: فِي أَرْضٍ).", "«(into) a land» — an adverb of place in naṣb (the «in» understood).", "«bir yere» — mef'ûl-i fîh, mansub («bir yerde» takdiriyle)."),
  nat_nasb("بَعِيدَةً", "baid", "«far-off»", "«uzak»", punct=".")])
sen("s28", "Then your father will be yours alone, and his love will be yours alone.", "O zaman babanız yalnız sizin olur; sevgisi de yalnız sizin olur.", [
  tok("حِينَئِذٍ", "hinaidhin", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ إِلَى إِذْ، وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ مَحْذُوفَةٍ.", "«then» — a time-adverb annexed to «idh»; the tanwīn stands in for a dropped clause.", "«o zaman» — «iz»e muzâf zaman zarfı; tenvin hazfedilen cümlenin ivazıdır."),
  tok("يَكُونُ", "kana", "verb", [K, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«will be» — kāna's muḍāriʿ.", "«olur» — kâne'nin muzârisi."),
  tok("أَبُوكُمْ", "ab", "noun", [K, "five-nouns", "idafa-definiteness"], "اسْمُ يَكُونُ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your father» — yakūn's ism, rafʿ by the wāw of the five nouns.", "«babanız» — yekûn'un ismi, vâv ile merfû.", segments=[seg("أَبُو", "ab", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
  lahu("لَكُمْ", "كُمْ", "pron-2mp", "مُتَعَلِّقٌ بِخَالِصًا.", "«to you».", "«sizin»."),
  khabar_kana("خَالِصًا", "khalis", "«alone (wholly)»", "«yalnız (sizin)»", punct="،"),
  tok("وَيَكُونُ", "kana", "verb", ["atf-nasaq", K, "hollow-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«and … will be» — joined.", "«ve … olur» — atıf.", segments=[seg("وَ", "wa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  mudaf_pron("حُبُّهُ", "hubb", "هُ", "pron-3ms", "اسْمُ يَكُونُ مَرْفُوعٌ بِالضَّمَّةِ", "«his love» — yakūn's ism", "«sevgisi» — yekûn'un ismi", tags=[K]),
  lahu("لَكُمْ", "كُمْ", "pron-2mp", "مُتَعَلِّقٌ بِخَالِصًا.", "«to you».", "«sizin»."),
  khabar_kana("خَالِصًا", "khalis", "«alone (wholly)»", "«yalnız (sizin)»", punct=".")])
sen("s29", "One of them said: No — rather, throw him into a well on a road; some travellers will pick him up.", "İçlerinden biri dedi: Hayır, onu bir yol üzerindeki bir kuyuya atın; yolculardan bazıları onu alır.", [
  qala_h(punct=None),
  mudaf_pron("أَحَدُهُمْ", "ahad", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "«one of them» — the doer", "«içlerinden biri» — fâil", tags=["fail"], punct=":"),
  tok("لَا", "la-nafiya", "part", ["la-nafiya"], "حَرْفُ جَوَابٍ لَا مَحَلَّ لَهُ.", "«no» — the answering particle.", "«hayır» — cevap harfi."),
  tok("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«rather» — the particle of correction.", "«bilakis» — idrab harfi."),
  amr_pl("أَلْقُوهُ", "alqa", "«throw him»", "«onu atın»", pron_seg="هُ", pron_lex="pron-3ms", tags=["naqis-verbs", "form-iv-verbs"]),
  fi(), tok("بِئْرٍ", "bir", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«a well» — in jarr.", "«bir kuyu» — mecrur."),
  tok("فِي", "fi", "prep", ["huruf-jarr", "jumla-sifa"], "حَرْفُ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِبِئْرٍ.", "«on» — the phrase is a naʿt of «a well».", "«üzerinde» — şibh-i cümle «kuyu»nun sıfatıdır."),
  tok("طَرِيقٍ", "tariq", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«a road» — in jarr.", "«bir yol» — mecrur."),
  verb_enc("يَأْخُذُهُ", "akhadha", "هُ", "pron-3ms", "«will pick him up»", "«onu alır»", tags=["jumla-sifa"], hidden=None, extra=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِطَرِيقٍ"),
  mudaf_jarr("بَعْضُ", "bad", "«some (of)»", "«bazıları»", "", tags=["fail"]) if False else
  tok("بَعْضُ", "bad", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«some (of)» — the doer; a muḍāf.", "«bazıları» — fâil; muzâf."),
  tok("الْمُسَافِرِينَ", "musafir", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the travellers» — the muḍāf ilayh, jarr by the yāʾ of the sound masculine plural.", "«yolcuların» — muzâfun ileyh, cem-i müzekker sâlim olduğu için yâ ile mecrur.", punct=".")])
sen("s30", "And all the brothers agreed to it.", "Ve bütün kardeşler buna razı oldu.", [
  mazi("وَوَافَقَ", "wafaqa", "«agreed»", "«razı oldu»", hidden=None, wa=True, tags=["form-iii-verbs"]),
  tok("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«to it».", "«buna».", segments=[seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("جَمِيعُ", "jami", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«all (of)» — the doer; a muḍāf.", "«bütün» — fâil; muzâf."),
  ikhwa("الْإِخْوَةِ", "jarr", "مُضَافٌ إِلَيْهِ", "«the brothers» — the muḍāf ilayh", "«kardeşler» — muzâfun ileyh", punct=".")])

# ---------------------------------------------------------------- glossary
NEW = {
 "dhaki": G("dhaki", "ذَكِيّ", "ذ ك و", "noun", "clever, intelligent (ṣifa mushabbaha)", "zeki, akıllı (sıfat-ı müşebbehe)", 1, plural="أَذْكِيَاء"),
 "ruya-dream": G("ruya-dream", "رُؤْيَا", "ر أ ي", "noun", "a dream, a vision seen in sleep (فُعْلَى — a diptote)", "rüya, uykuda görülen (fu'lâ kalıbı — gayr-i munsarıf)", 1),
 "sajid": G("sajid", "سَاجِد", "س ج د", "noun", "bowing down, prostrating (ism fāʿil of سَجَدَ)", "secde eden (secede'nin ism-i fâili)", 1, plural="سَاجِدُونَ"),
 "bishara": G("bishara", "بِشَارَة", "ب ش ر", "noun", "good tidings", "müjde", 1),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب و", "noun", "prophethood", "peygamberlik, nübüvvet", 1),
 "anama": G("anama", "أَنْعَمَ", "ن ع م", "verb", "to bestow favour (أَنْعَمَ عَلَى)", "nimet vermek, lütfetmek", 1, form="IV"),
 "tabia": G("tabia", "طَبِيعَة", "ط ب ع", "noun", "nature, natural disposition", "tabiat, huy", 2, plural="طَبَائِع"),
 "akhbara": G("akhbara", "أَخْبَرَ", "خ ب ر", "verb", "to tell, to inform (أَخْبَرَ فُلَانًا بِـ)", "haber vermek, bildirmek", 1, form="IV"),
 "hasada": G("hasada", "حَسَدَ", "ح س د", "verb", "to envy", "kıskanmak, haset etmek", 1, form="I"),
 "hasad": G("hasad", "حَسَد", "ح س د", "noun", "envy (maṣdar of حَسَدَ)", "haset, kıskançlık (hasede'nin masdarı)", 1),
 "shabb": G("shabb", "شَابّ", "ش ب ب", "noun", "a young man", "genç, delikanlı", 1, plural="شُبَّان"),
 "ishtadda": G("ishtadda", "اِشْتَدَّ", "ش د د", "verb", "to grow intense, to become severe", "şiddetlenmek, artmak", 2, form="VIII"),
 "musafir": G("musafir", "مُسَافِر", "س ف ر", "noun", "a traveller (ism fāʿil of سَافَرَ)", "yolcu (sâfere'nin ism-i fâili)", 1, plural="مُسَافِرُونَ"),
 "wafaqa": G("wafaqa", "وَافَقَ", "و ف ق", "verb", "to agree (وَافَقَ عَلَى)", "razı olmak, uymak", 1, form="III"),
 "binyamin": G("binyamin", "بِنْيَامِين", None, "propn", "Binyāmīn (Benjamin), Yūsuf's full brother", "Bünyamin, Yusuf'un öz kardeşi", 1),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("ilm", "علم"), ("jadd", "جد"), ("amr", "أمر"), ("bad", "بعض"), ("ghulam", "غلام"), ("jamil", "جميل"), ("jami", "جميع"), ("haka", "حكى"), ("shan", "شأن"), ("al-family", "آل"), ("shaykh", "شيخ"), ("insan", "إنسان"), ("hubb", "حب"), ("shadid", "شديد"), ("mithl", "مثل"), ("taraha", "طرح"), ("baid", "بعيد"), ("khalis", "خالص"), ("tariq", "طريق"), ("qad", "قد"), ("la-nahiya", "لا")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e and bare(_e["lemma"]).split(" ")[0].replace("ِ", "") == _lm, (_k, _e and _e["lemma"])
assert "grand" in (GLOSS_ADD.get("jadd") or TG["jadd"])["gloss"]["en"]
# the plural the corpus witnesses on an entry the package already owns (added, never changed)
_g = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
if not _g["entries"]["qawi"].get("plural"):
    _g["entries"]["qawi"]["plural"] = "أَقْوِيَاء"; (PKG / "glossary.json").write_text(json.dumps(_g, ensure_ascii=False, indent=1), encoding="utf-8"); print("qawi: plural أَقْوِيَاء added")
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].pop("ishtadda", None)   # the engine writes the geminate 2ms amr by the jazm bil-fath (اِشْتَدَّ) and the fakk only before the women's nun; the stored cells follow it
B4, W4 = "مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ"
put_morph(mo, "anama", _sg.derived(B4, W4, "ُ", "أَنْعَم", "نْعِم", "أَنْعِم", "إِنْعَام", "مُنْعِم", "مُنْعَم", "أُنْعِمَ", "يُنْعَمُ", note="يَتَعَدَّى بِعَلَى: أَنْعَمَ اللهُ عَلَيْهِ."))
put_morph(mo, "akhbara", _sg.derived(B4, W4, "ُ", "أَخْبَر", "خْبِر", "أَخْبِر", "إِخْبَار", "مُخْبِر", "مُخْبَر", "أُخْبِرَ", "يُخْبَرُ", note="مُتَعَدٍّ: أَخْبَرَ فُلَانًا بِالْأَمْرِ."))
put_morph(mo, "hasada", _sg.sound1("nasara", "حَسَد", "حْسُد", "اُحْسُد", "حَسَد", "حَاسِد", "مَحْسُود", "حُسِدَ", "يُحْسَدُ", note="مُتَعَدٍّ."))
put_morph(mo, "ishtadda", _sg.entry("مِنْ بَابِ الِافْتِعَالِ — مُضَعَّفٌ", "اِفْتَعَلَ يَفْتَعِلُ", "اِشْتِدَاد", "مُشْتَدّ",
                                    _sg.mazi14("اِشْتَدّ", "اِشْتَدَد"), _sg.mudari14("َ", "شْتَدّ", "شْتَدِد"), ["اِشْتَدَّ", "اِشْتَدَّا", "اِشْتَدُّوا", "اِشْتَدِّي", "اِشْتَدَّا", "اِشْتَدِدْنَ"],
                                    "يَشْتَدَّ", "يَشْتَدَّ", "تَشْتَدَّ", note="لَازِمٌ — مُضَعَّفٌ: الْمِثْلَانِ يُدْغَمَانِ حَيْثُ تَحَرَّكَ الثَّانِي (اِشْتَدَّ) وَيُفَكَّانِ أَمَامَ السَّاكِنِ (اِشْتَدَدْتُ)؛ الْجَزْمُ بِالْفَتْحِ."))
put_morph(mo, "wafaqa", _sg.derived("مِنْ بَابِ الْمُفَاعَلَةِ", "فَاعَلَ يُفَاعِلُ", "ُ", "وَافَق", "وَافِق", "وَافِق", "مُوَافَقَة", "مُوَافِق", "مُوَافَق", "وُوفِقَ", "يُوَافَقُ", note="يَتَعَدَّى بِعَلَى: وَافَقَ عَلَيْهِ — مِثَالٌ وَاوِيٌّ تَبْقَى وَاوُهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 8 (print pp. 27–30, the opening of «أَحْسَنُ الْقَصَصِ»: sections 1 «رُؤْيَا عَجِيبَة» and 2 «حَسَدُ الْإِخْوَة»): the boy Yūsuf and his dream (s1–s8), Yūsuf 12:4 as the print sets it (s9, marked), Yaʿqūb's reading of the dream and his warning (s10–s18); Binyāmīn, the brothers' envy, their council and the well (s19–s30). "
          "One printed line is one sentence, split at the print's own full stops where a line holds several (s1–s3, s6–s8, s16–s17, s21–s22, s24–s25); the sentence after «وَيَغْضَبُونَ» (s22) and the clause «نَحْنُ شُبَّانٌ أَقْوِيَاءُ» (s24) are cut as the sense requires where the print carries no stop. s27 echoes Yūsuf 12:9 in the print's own words (أَرْضًا بَعِيدَةً) and is not marked as a quotation.")
ADD_TR = (" Sekizinci bölüm (basılı s. 27–30, «أَحْسَنُ الْقَصَصِ»in başı: 1. kısım «رُؤْيَا عَجِيبَة» ve 2. kısım «حَسَدُ الْإِخْوَة»): çocuk Yusuf ve rüyası (s1–s8), Yûsuf 12:4 baskıdaki şekliyle (s9, işaretli), Yakub'un rüyayı yorumlayışı ve uyarısı (s10–s18); Bünyamin, kardeşlerin kıskançlığı, toplantıları ve kuyu (s19–s30). "
          "Basılı her satır bir cümledir; birden çok cümle taşıyan satırlar baskının noktalarından bölünmüştür (s1–s3, s6–s8, s16–s17, s21–s22, s24–s25); «وَيَغْضَبُونَ»den sonraki cümle (s22) ve «نَحْنُ شُبَّانٌ أَقْوِيَاءُ» (s24) baskıda nokta bulunmadığı hâlde mânâ gereği ayrılmıştır. s27, Yûsuf 12:9'u baskının kendi sözleriyle (أَرْضًا بَعِيدَةً) yansıtır; iktibas olarak işaretlenmemiştir.")
write_out(8, S, TITLE, ADD_EN, ADD_TR, "pp. 27–30", GLOSS_ADD)
report(8, S, GLOSS_ADD, ())
