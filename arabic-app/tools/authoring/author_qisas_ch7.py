# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 7: «الْكَعْبَةُ وَبَيْتُ الْمَقْدِسِ» — sections 15–16 of «من كسر الأصنام؟» (print pp. 23–26):
the building of the Kaʿba with the prayer of al-Baqara 2:127 as the print sets it (marked), the Muslims' turning and pilgrimage,
the prayers of blessing; then Sārah and Isḥāq, al-Shām and Bayt al-Maqdis, Yaʿqūb and his twelve sons, and the hand-over to Yūsuf's story.
Every printed line is one sentence (the first printed line of §15 holds two, split at its full stop); the vowelling is the print's
(إِسْحٰقُ with its dagger alif).  python3 tools/authoring/author_qisas_ch7.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْكَعْبَةُ وَبَيْتُ الْمَقْدِسِ", "en": "The Kaʿba and Bayt al-Maqdis", "tr": "Kâbe ve Beytülmakdis"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- local helpers
def ibrahim_fail(punct=None): return fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=punct)
def ismail_fail(punct=None): return fail_name("إِسْمَاعِيلُ", "ismail", "«Ismāʿīl»", "«İsmâil»", punct=punct)
def ishaq_fail(punct=None): return fail_name("إِسْحٰقُ", "ishaq", "«Isḥāq»", "«İshak»", punct=punct)
def name_ism_kana(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — kāna's ism, in rafʿ; a diptote name.", tr + " — kâne'nin ismi, merfû; gayr-i munsarıf özel isim.", punct=punct)
def name_jarr(full, lex, en, tr, prep, punct=None, tags=()):
    return tok(full, lex, "propn", ["huruf-jarr", "mamnu-min-sarf"] + list(tags), f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — in jarr by a fatḥa; a diptote name.", tr + " — fetha ile mecrur; gayr-i munsarıf özel isim.", punct=punct)
def name_atf_jarr(full, lex, en, tr, head, punct=None):
    return tok(full, lex, "propn", ["atf-nasaq", "mamnu-min-sarf"], f"الْوَاوُ عَاطِفَةٌ، وَ{full[2:]} مَعْطُوفٌ عَلَى {head} مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and» + " + en + " — joined to the name before it, jarr by a fatḥa; a diptote.", "«ve» + " + tr + " — önceki isme atıf, fetha ile mecrur; gayr-i munsarıf.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(full[2:], lex, "propn")])
def name_mudaf_ilayh(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the muḍāf ilayh, jarr by a fatḥa; a diptote.", tr + " — muzâfun ileyh, fetha ile mecrur; gayr-i munsarıf.", punct=punct)
def li_name(full, lex, en, tr, punct=None):
    """لِإِبْرَاهِيمَ، لِإِسْحٰقَ — the jarr lām on a diptote name, the phrase kāna's fronted khabar."""
    return tok(full, lex, "propn", [K, "huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ، وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.",
               en + " — the jarr lām; the phrase is kāna's khabar, fronted.", tr + " — cer lâmı; şibh-i cümle kâne'nin öne alınmış haberidir.", punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "propn")])
def li_al(full, lex, en, tr, punct=None, tags=()):
    """لِلّٰهِ — the jarr lām swallowing the article's alif (the ch4 helper)."""
    return tok(full, lex, "propn", ["huruf-jarr"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", en + " — the jarr lām on the name of Allah (the article's alif is swallowed); in jarr.", tr + " — cer lâmı lafza-i celâle bitişik (harf-i tarifin elifi düşer); mecrur.",
               punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[1:], lex, "propn")])
def fi(punct=None): return tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(): return tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on, upon».", "«üzerine».")
def ila(): return tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e».")
def min_(): return tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den».")
def kaba_jarr(punct=None, prep="إِلَى"):
    return tok("الْكَعْبَةِ", "kaaba", "propn", ["huruf-jarr"], f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the Kaʿba» — in jarr.", "«Kâbe» — mecrur.", punct=punct)
def kaba_maful(punct=None): return tok("الْكَعْبَةَ", "kaaba", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the Kaʿba» — the object, in naṣb.", "«Kâbe'yi» — mef'ûl-i bih, mansub.", punct=punct)
def sham_jarr(punct=None): return tok("الشَّامِ", "sham", "propn", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«al-Shām» — in jarr.", "«Şam» — mecrur.", punct=punct)
def bayt_maful(punct=None): return tok("بَيْتًا", "bayt", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a house» — the object, in naṣb.", "«bir ev» — mef'ûl-i bih, mansub.", punct=punct)
def an():
    return tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ.", "«to» — the subjunctive maṣdar particle; the clause it makes is the object.", "«-mek» — masdariyye nasb harfi; te'vîl edilen masdar mef'ûldür.")
def yabniya():
    return tok("يَبْنِيَ", "bana", "verb", ["an-masdariyya", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "«to build» — in naṣb after an, the fatḥa written on the yāʾ; the doer «he» is concealed.", "«inşa etmek» — en ile mansub, fetha yâ üzerinde açık; fâil gizli «o».")
def khabar_kana_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", extra=""):
    return tok(full, lex, "verb", [K, "mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + (extra or "بِالضَّمَّةِ") + f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden} — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — a muḍāriʿ; the clause is kāna's khabar.", tr + " — muzâri; cümle kâne'nin haberidir.")
def biyadihi(punct=None):
    return tok("بِيَدِهِ", "yad", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَيَدِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with his hand» — the bāʾ of jarr; annexed to «his».", "«eliyle» — cer bâsı; «onun»a muzâf.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("يَدِ", "yad", "noun"), seg("هِ", "pron-3ms", "pron")])
def allah_maful(punct=None): return tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object, in naṣb.", "«Allah'ı» — lafza-i celâl, mef'ûl-i bih, mansub.", punct=punct)
def wa_yadu(punct=None):
    return tok("وَيَدْعُو", "daa", "verb", ["atf-nasaq", "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَدْعُو فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and prays» — joined; the ḍamma estimated on the wāw.", "«ve dua eder» — atıf; damme vâv üzerinde takdîrî.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("يَدْعُو", "daa", "verb")])
def salla_line(name_full, name_lex, name_en, name_tr, wa=False):
    v = tok("وَصَلَّى" if wa else "صَلَّى", "salla", "verb", ["naqis-verbs", "form-ii-verbs"] + (["atf-nasaq"] if wa else []), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — دُعَاءٌ بِلَفْظِ الْخَبَرِ.", Wen(wa) + "«may … bless» — a māḍī, the fatḥa estimated on the alif; a prayer in the form of a statement.", Wtr(wa) + "«salât eylesin» — mâzî, fetha elif üzerinde takdîrî; haber kalıbında dua.", segments=(wa_("صَلَّى", "salla", "verb") if wa else None))
    return [v, allah_fail(), ala(), name_jarr(name_full, name_lex, name_en, name_tr, "عَلَى"),
            mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm eylesin»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-ii-verbs"], punct=".")]
def ismuhu(full="اسْمُهُ", pron_seg="هُ", pron_lex="pron-3ms", en="«his name»", tr="«adı»", head="وَلَدٌ"):
    return tok(full, "ism-name", "noun", ["mubtada-khabar", "idafa-definiteness", "jumla-sifa"], f"مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ{head}.", en + " — the mubtadaʾ, annexed to the pronoun; the clause is a naʿt of the noun before.", tr + " — mübtedâ, zamire muzâf; cümle önceki ismin sıfatıdır.", segments=[seg("اسْمُ", "ism-name", "noun"), seg(pron_seg, pron_lex, "pron")])
def kama():
    return tok("كَمَا", "kama", "part", ["huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ (بِنَاءً كَبِنَاءِ…).", "«as» — the kāf of jarr and the maṣdar-mā; the clause stands as a maṣdar in jarr.", "«gibi, -diği gibi» — cer kâfı ve masdariyye mâ; cümle masdar olarak mecrur sayılır.")
def lahu(role_ar, en, tr, tags=()):
    return tok("لَهُ", "li", "prep", ["huruf-jarr", "mubtada-khabar"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — " + role_ar, en, tr, segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")])

# ================================================================ §15 الكعبة (pp. 23–25)
sen("s1", "And Ibrāhīm went and came back after that, and he wanted to build a house for Allah.", "Ve İbrâhim gitti, ondan sonra döndü; Allah için bir ev yapmak istedi.", [
  mazi("وَذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None, wa=True), ibrahim_fail(),
  mazi("وَعَادَ", "ada-return", "«and came back»", "«ve döndü»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "hollow-verbs"]),
  tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«after» — an adverb of time in naṣb; a muḍāf.", "«sonra» — mansub zaman zarfı; muzâf."),
  ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«o, bu»", punct="،"),
  mazi("وَأَرَادَ", "arada", "«and wanted»", "«ve istedi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "hollow-verbs", "form-iv-verbs"]), an(), yabniya(), bayt_maful(),
  li_al("لِلّٰهِ", "allah", "«for Allah»", "«Allah için»", punct=".")])
sen("s2", "And the houses were many, but there was no house for Allah in which they worshipped Allah.", "Ve evler çoktu; fakat içinde Allah'a ibadet edilen bir Allah evi yoktu.", [
  tok("وَكَانَتِ", "kana", "verb", [K, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَكُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and … were» — kāna with the feminine tāʾ, its kasra for the meeting of two sukūns.", "«ve … idi» — kâne + te'nis tâsı; iki sâkinin karşılaşması için kesre.", segments=[seg("وَ", "wa", "conj"), seg("كَانَتِ", "kana", "verb")]),
  tok("الْبُيُوتُ", "bayt", "noun", [K, "jam-taksir"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ.", "«the houses» — kāna's ism, in rafʿ; a broken plural.", "«evler» — kâne'nin ismi, merfû; cem-i mükesser."),
  tok("كَثِيرَةً", "kathir", "noun", [K], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«many» — kāna's khabar, in naṣb.", "«çok» — kâne'nin haberi, mansub."),
  tok("وَمَا", "ma-nafiya", "part", ["anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and not» — the negating mā, no government.", "«ve … değil» — nefiy mâ'sı, amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  tok("كَانَ", "kana", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«was» — kāna.", "«idi» — kâne."),
  tok("بَيْتٌ", "bayt", "noun", [K], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«a house» — kāna's ism, in rafʿ.", "«bir ev» — kâne'nin ismi, merfû."),
  tok("لِلّٰهِ", "allah", "propn", [K, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«for Allah» — the jarr phrase is kāna's khabar.", "«Allah için» — şibh-i cümle kâne'nin haberidir.", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("يَعْبُدُونَ", "abada", "verb", ["afal-khamsa", "mudari-marfu", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِبَيْتٌ.", "«(in which) they worship» — one of the five verbs; the clause is a naʿt of «a house».", "«(içinde) ibadet ettikleri» — ef'âl-i hamseden; cümle «ev»in sıfatıdır."),
  tok("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«in it».", "«onda, içinde».", segments=[seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  allah_maful(punct=".")])
sen("s3", "And Ismāʿīl wanted to build a house for Allah with his father.", "Ve İsmâil babasıyla birlikte Allah için bir ev yapmak istedi.", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, wa=True, tags=["hollow-verbs", "form-iv-verbs"]), ismail_fail(), an(), yabniya(), bayt_maful(), li_al("لِلّٰهِ", "allah", "«for Allah»", "«Allah için»"),
  tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with» — an adverb in naṣb; a muḍāf.", "«ile» — mansub zarf; muzâf."),
  tok("وَالِدِهِ", "walid-father", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the muḍāf ilayh; itself annexed to «his».", "«babası» — muzâfun ileyh; kendisi de «onun»a muzâf.", punct=".", segments=[seg("وَالِدِ", "walid-father", "noun"), seg("هِ", "pron-3ms", "pron")])])
sen("s4", "And Ibrāhīm and Ismāʿīl carried the stones from the mountains.", "Ve İbrâhim ile İsmâil taşları dağlardan taşıdılar.", [
  mazi("وَنَقَلَ", "naqala", "«carried»", "«taşıdı»", hidden=None, wa=True), ibrahim_fail(),
  tok("وَإِسْمَاعِيلُ", "ismail", "propn", ["atf-nasaq", "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَإِسْمَاعِيلُ مَعْطُوفٌ عَلَى إِبْرَاهِيمُ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Ismāʿīl» — joined to the doer, in rafʿ.", "«ve İsmâil» — fâile atıf, merfû.", segments=[seg("وَ", "wa", "conj"), seg("إِسْمَاعِيلُ", "ismail", "propn")]),
  tok("الْحِجَارَةَ", "hijara", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the stones» — the object, in naṣb.", "«taşları» — mef'ûl-i bih, mansub."),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، فُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its nūn takes a fatḥa before the article.", "«-den» — nûnu iki sâkinin karşılaşması için fethalı."),
  tok("الْجِبَالِ", "jabal", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — جَمْعُ تَكْسِيرٍ.", "«the mountains» — in jarr; a broken plural.", "«dağlar» — mecrur; cem-i mükesser.", punct=".")])
sen("s5", "And Ibrāhīm was building the Kaʿba with his hand, and Ismāʿīl was building the Kaʿba with his hand.", "Ve İbrâhim Kâbe'yi eliyle yapıyordu; İsmâil de Kâbe'yi eliyle yapıyordu.", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_kana_mudari("يَبْنِي", "bana", "«was building»", "«yapıyordu»", tags=["naqis-verbs"], extra="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ"), kaba_maful(), biyadihi(),
  kana(), name_ism_kana("إِسْمَاعِيلُ", "ismail", "«Ismāʿīl»", "«İsmâil»"),
  khabar_kana_mudari("يَبْنِي", "bana", "«was building»", "«yapıyordu»", tags=["naqis-verbs"], extra="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ"), kaba_maful(), biyadihi(punct=".")])
sen("s6", "And Ibrāhīm was remembering Allah and praying.", "Ve İbrâhim Allah'ı zikrediyor ve dua ediyordu.", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"), khabar_kana_mudari("يَذْكُرُ", "dhakara", "«was remembering»", "«zikrediyordu»"), allah_maful(), wa_yadu(punct=".")])
sen("s7", "And Ismāʿīl was remembering Allah and praying.", "Ve İsmâil Allah'ı zikrediyor ve dua ediyordu.", [
  kana(), name_ism_kana("إِسْمَاعِيلُ", "ismail", "«Ismāʿīl»", "«İsmâil»"), khabar_kana_mudari("يَذْكُرُ", "dhakara", "«was remembering»", "«zikrediyordu»"), allah_maful(), wa_yadu(punct=".")])
sen("s8", "«Our Lord, accept from us; You are the All-Hearing, the All-Knowing.» (al-Baqara 2:127)", "«Rabbimiz, bizden kabul buyur; şüphesiz Sen işitensin, bilensin.» (Bakara 2:127)", quran([
  tok("رَبَّنَا", "rabb", "noun", ["vocative-munada", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ (يَا رَبَّنَا)، وَنَا مُضَافٌ إِلَيْهِ.", "«our Lord» — a vocative annexed to «our», in naṣb; the calling particle is dropped.", "«Rabbimiz» — «biz»e muzâf münâdâ, mansub; nidâ harfi hazfedilmiştir.", segments=[seg("رَبَّ", "rabb", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("تَقَبَّلْ", "taqabbala", "verb", ["imperative-amr", "form-v-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "«accept» — an imperative built on sukūn; the doer «You» is concealed.", "«kabul et» — sükûn üzere mebnî emir; fâil gizli «sen»."),
  tok("مِنَّا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — وَأُدْغِمَتْ نُونُ مِنْ فِي نُونِ نَا.", "«from us» — min with «us»; the two nūns merge.", "«bizden» — min + «biz»; iki nûn idgam edilmiştir.", segments=[seg("مِنْ", "min", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("إِنَّكَ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed You» — inna with its ism «You» attached.", "«şüphesiz Sen» — inne ve ismi «sen».", segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَنْتَ", "anta", "pron", ["damir-fasl"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ (وَيَجُوزُ أَنْ يَكُونَ مُبْتَدَأً، وَالْجُمْلَةُ خَبَرُ إِنَّ).", "«You» — the pronoun of separation, no place in iʿrāb (or a mubtadaʾ whose clause is inna's khabar).", "«Sen» — zamîr-i fasl, i'rabdan mahalli yok (veya mübtedâ; cümle inne'nin haberidir)."),
  tok("السَّمِيعُ", "samii", "noun", ["inna-wa-akhawatuha", "sifa-mushabbaha"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«the All-Hearing» — inna's khabar, in rafʿ.", "«işiten» — inne'nin haberi, merfû."),
  tok("الْعَلِيمُ", "alim", "noun", ["inna-wa-akhawatuha", "sifa-mushabbaha"], "خَبَرٌ ثَانٍ لِإِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«the All-Knowing» — a second khabar of inna.", "«bilen» — inne'nin ikinci haberi.", punct=".")]))
sen("s9", "And Allah accepted from Ibrāhīm and Ismāʿīl, and He blessed the Kaʿba.", "Ve Allah İbrâhim ile İsmâil'den kabul buyurdu ve Kâbe'yi mübarek kıldı.", [
  mazi("وَتَقَبَّلَ", "taqabbala", "«accepted»", "«kabul buyurdu»", hidden=None, wa=True, tags=["form-v-verbs"]), allah_fail(), min_(), name_jarr("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", "مِنْ"),
  name_atf_jarr("وَإِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil»", "إِبْرَاهِيمَ"),
  mazi("وَبَارَكَ", "baraka-bless", "«and blessed»", "«ve mübarek kıldı»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-iii-verbs"]), fi(), kaba_jarr(punct=".", prep="فِي")])
sen("s10", "We turn toward the Kaʿba in every prayer.", "Biz her namazda Kâbe'ye yöneliriz.", [
  tok("نَحْنُ", "nahnu", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«we» — a detached pronoun, built; the mubtadaʾ.", "«biz» — munfasıl zamir, mebnî; mübtedâ."),
  tok("نَتَوَجَّهُ", "tawajjaha", "verb", ["mubtada-khabar", "mudari-marfu", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«turn» — a muḍāriʿ; the clause is the khabar.", "«yöneliriz» — muzâri; cümle haberdir."),
  ila(), kaba_jarr(), fi(),
  tok("كُلِّ", "kull", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«every» — in jarr; a muḍāf.", "«her» — mecrur; muzâf."),
  tok("صَلَاةٍ", "salat", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«prayer» — the muḍāf ilayh.", "«namaz» — muzâfun ileyh.", punct=".")])
sen("s11", "And the Muslims travel to the Kaʿba in the days of the Pilgrimage.", "Ve Müslümanlar hac günlerinde Kâbe'ye yolculuk ederler.", [
  tok("وَيُسَافِرُ", "safara", "verb", ["mudari-marfu", "form-iii-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيُسَافِرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and … travel» — a muḍāriʿ in rafʿ; its doer follows.", "«ve … yolculuk eder» — merfû muzâri; fâili sonra gelir.", segments=[seg("وَ", "wa", "conj"), seg("يُسَافِرُ", "safara", "verb")]),
  tok("الْمُسْلِمُونَ", "muslim", "noun", ["fail", "jam-mudhakkar-salim"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the Muslims» — the doer, rafʿ by the wāw of the sound masculine plural.", "«Müslümanlar» — fâil, cem-i müzekker sâlim olduğu için vâv ile merfû."),
  ila(), kaba_jarr(), fi(),
  tok("أَيَّامِ", "yawm", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ — جَمْعُ تَكْسِيرٍ.", "«the days» — in jarr; a muḍāf.", "«günleri» — mecrur; muzâf."),
  tok("الْحَجِّ", "hajj", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the Pilgrimage» — the muḍāf ilayh.", "«hac» — muzâfun ileyh.", punct=".")])
sen("s12", "And they go around the Kaʿba and pray by it.", "Ve Kâbe'yi tavaf ederler ve onun yanında namaz kılarlar.", [
  khamsa("وَيَطُوفُونَ", "tafa", "«and they go around»", "«ve tavaf ederler»", tags=["hollow-verbs"], wa=True),
  tok("بِالْكَعْبَةِ", "kaaba", "propn", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْكَعْبَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«(around) the Kaʿba» — the bāʾ of jarr.", "«Kâbe'yi» — cer bâsı.", segments=[seg("بِ", "bi", "prep"), seg("الْكَعْبَةِ", "kaaba", "propn")]),
  tok("وَيُصَلُّونَ", "salla", "verb", ["atf-nasaq", "afal-khamsa", "mudari-marfu", "naqis-verbs", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُصَلُّونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَحُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and they pray» — one of the five verbs; the weak last radical dropped before the group's wāw.", "«ve namaz kılarlar» — ef'âl-i hamseden; illetli son harf cemi vâvından önce düşmüştür.", segments=[seg("وَ", "wa", "conj"), seg("يُصَلُّونَ", "salla", "verb")]),
  tok("عِنْدَهَا", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«by it» — an adverb of place in naṣb, annexed to «it».", "«onun yanında» — mansub mekân zarfı; «o»na muzâf.", punct=".", segments=[seg("عِنْدَ", "inda", "noun"), seg("هَا", "pron-3fs", "pron")])])
sen("s13", "May Allah bless the Kaʿba and accept from Ibrāhīm and Ismāʿīl.", "Allah Kâbe'yi mübarek kılsın ve İbrâhim ile İsmâil'den kabul buyursun.", [
  mazi("بَارَكَ", "baraka-bless", "«may … bless»", "«mübarek kılsın»", hidden=None, tags=["form-iii-verbs"], extra_ar=" — دُعَاءٌ بِلَفْظِ الْخَبَرِ"), allah_fail(), fi(), kaba_jarr(prep="فِي"),
  mazi("وَتَقَبَّلَ", "taqabbala", "«and accept»", "«ve kabul buyursun»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-v-verbs"]), min_(), name_jarr("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", "مِنْ"),
  name_atf_jarr("وَإِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil»", "إِبْرَاهِيمَ", punct=".")])
sen("s14", "May Allah bless Ibrāhīm and grant him peace.", "Allah İbrâhim'e salât ve selâm eylesin.", salla_line("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"))
sen("s15", "May Allah bless Ismāʿīl and grant him peace.", "Allah İsmâil'e salât ve selâm eylesin.", salla_line("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil»"))
sen("s16", "And may Allah bless Muḥammad and grant him peace.", "Ve Allah Muhammed'e salât ve selâm eylesin.", [
  tok("وَصَلَّى", "salla", "verb", ["naqis-verbs", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَصَلَّى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — دُعَاءٌ بِلَفْظِ الْخَبَرِ.", "«and may … bless» — a māḍī, the fatḥa estimated on the alif; a prayer in the form of a statement.", "«ve … salât eylesin» — mâzî, fetha elif üzerinde takdîrî; haber kalıbında dua.", segments=[seg("وَ", "wa", "conj"), seg("صَلَّى", "salla", "verb")]),
  allah_fail(), ala(),
  tok("مُحَمَّدٍ", "muhammad", "propn", ["huruf-jarr"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — عَلَمٌ مُنْصَرِفٌ.", "«Muḥammad» — in jarr by a kasra; a name that takes tanwīn.", "«Muhammed» — kesre ile mecrur; munsarıf özel isim."),
  mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm eylesin»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-ii-verbs"], punct=".")])
# ================================================================ §16 بيت المقدس (pp. 25–26)
sen("s17", "And Ibrāhīm had another wife, whose name was Sārah.", "Ve İbrâhim'in başka bir hanımı vardı; adı Sâre idi.", [
  kana(), li_name("لِإِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm had»", "«İbrâhim'in … vardı»"),
  tok("زَوْجٌ", "zawj", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a wife» — kāna's ism, delayed; in rafʿ.", "«bir hanım» — kâne'nin geciktirilmiş ismi, merfû."),
  tok("أُخْرَى", "ukhra", "noun", ["naat-sifa", "ism-maqsur-manqus", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَقْصُورٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — the naʿt, rafʿ by a ḍamma estimated on the alif; a maqṣūr diptote.", "«başka» — sıfat, elif üzerinde takdîrî damme ile merfû; maksûr, gayr-i munsarıf.", punct="،"),
  ismuhu("اسْمُهَا", "هَا", "pron-3fs", "«her name»", "«adı»", head="زَوْجٌ"),
  tok("سَارَةُ", "sara-name", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sārah» — the khabar, in rafʿ; a feminine name, a diptote.", "«Sâre» — haber, merfû; müennes özel isim, gayr-i munsarıf.", punct=".")])
sen("s18", "And Ibrāhīm had another son, from Sārah, whose name was Isḥāq.", "Ve İbrâhim'in Sâre'den başka bir oğlu vardı; adı İshak idi.", [
  kana(), li_name("لِإِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm had»", "«İbrâhim'in … vardı»"),
  tok("وَلَدٌ", "walad", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a son» — kāna's ism, delayed.", "«bir oğul» — kâne'nin geciktirilmiş ismi."),
  tok("آخَرُ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ.", "«another» — the naʿt, rafʿ with no tanwīn; a diptote (an adjective on a verb's pattern).", "«başka» — sıfat, tenvinsiz merfû; vasfiyet ve fiil vezni sebebiyle gayr-i munsarıf."),
  min_(), tok("سَارَةَ", "sara-name", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sārah» — in jarr by a fatḥa; a diptote.", "«Sâre'den» — fetha ile mecrur; gayr-i munsarıf."),
  ismuhu(head="وَلَدٌ"),
  tok("إِسْحٰقُ", "ishaq", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ (يُكْتَبُ بِأَلِفٍ خَنْجَرِيَّةٍ).", "«Isḥāq» — the khabar, in rafʿ; a foreign name, a diptote (the print writes it with a dagger alif).", "«İshak» — haber, merfû; yabancı özel isim, gayr-i munsarıf (baskı hançer elifle yazar).", punct=".")])
sen("s19", "And Ibrāhīm settled in al-Shām, and Isḥāq settled (there).", "Ve İbrâhim Şam'a yerleşti, İshak da yerleşti.", [
  mazi("وَسَكَنَ", "sakana", "«settled»", "«yerleşti»", hidden=None, wa=True), ibrahim_fail(), fi(), sham_jarr(punct="،"),
  mazi("وَسَكَنَ", "sakana", "«and settled»", "«ve yerleşti»", hidden=None, wa=True, tags=["atf-nasaq"]), ishaq_fail(punct=".")])
sen("s20", "And Isḥāq built a house for Allah in al-Shām, as his father and his brother had built a house for Allah in Mecca.", "Ve İshak, babası ile kardeşinin Mekke'de Allah için bir ev yaptıkları gibi, Şam'da Allah için bir ev yaptı.", [
  tok("وَبَنَى", "bana", "verb", ["naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَبَنَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and built» — a māḍī, the fatḥa estimated on the alif.", "«ve yaptı» — mâzî, fetha elif üzerinde takdîrî.", segments=[seg("وَ", "wa", "conj"), seg("بَنَى", "bana", "verb")]),
  ishaq_fail(), bayt_maful(), li_al("لِلّٰهِ", "allah", "«for Allah»", "«Allah için»"), fi(), sham_jarr(punct="،"), kama(),
  tok("بَنَى", "bana", "verb", ["naqis-verbs", "anwa-ma"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — صِلَةُ مَا الْمَصْدَرِيَّةِ.", "«built» — the māḍī inside the maṣdar-mā's clause.", "«yaptı(ğı)» — masdariyye mâ'nın sılasındaki mâzî."),
  tok("أَبُوهُ", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the doer, rafʿ by the wāw of the five nouns; annexed to «his».", "«babası» — fâil, esmâ-i hamseden olduğu için vâv ile merfû; «onun»a muzâf.", segments=[seg("أَبُو", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("وَأَخُوهُ", "akh", "noun", ["atf-nasaq", "five-nouns", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَأَخُو مَعْطُوفٌ عَلَى أَبُوهُ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his brother» — joined to «his father», rafʿ by the wāw of the five nouns.", "«ve kardeşi» — «babası»na atıf, esmâ-i hamseden olduğu için vâv ile merfû.", segments=[seg("وَ", "wa", "conj"), seg("أَخُو", "akh", "noun"), seg("هُ", "pron-3ms", "pron")]),
  bayt_maful(), li_al("لِلّٰهِ", "allah", "«for Allah»", "«Allah için»"), fi(),
  tok("مَكَّةَ", "makka", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Mecca» — in jarr by a fatḥa; a feminine name, a diptote.", "«Mekke» — fetha ile mecrur; müennes özel isim, gayr-i munsarıf.", punct=".")])
sen("s21", "And this mosque which Isḥāq built in al-Shām is Bayt al-Maqdis.", "Ve İshak'ın Şam'da yaptığı bu mescit Beytülmakdis'tir.", [
  tok("وَهٰذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — a demonstrative, built; the mubtadaʾ.", "«ve bu» — ism-i işâret, mebnî; mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هٰذَا", "hadha", "pron")]),
  tok("الْمَسْجِدُ", "masjid", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«mosque» — the badal of the demonstrative, in rafʿ.", "«mescit» — ism-i işâretin bedeli, merfû."),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلْمَسْجِدِ.", "«which» — the relative, built; a naʿt of «the mosque».", "«-diği» — ism-i mevsûl, mebnî; «mescit»in sıfatı."),
  tok("بَنَاهُ", "bana", "verb", ["naqis-verbs", "maful-bihi", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ (الْعَائِدُ) — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.", "«built it» — a māḍī; the hāʾ is the object and the returning pronoun; the clause is the relative's ṣila.", "«onu yaptı» — mâzî; hâ mef'ûl ve âid zamiri; cümle sıla, mahalli yok.", segments=[seg("بَنَا", "bana", "verb"), seg("هُ", "pron-3ms", "pron")]),
  ishaq_fail(), fi(), sham_jarr(),
  tok("هُوَ", "pron-3ms-munfasil", "pron", ["damir-fasl"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ مُبْتَدَأٌ ثَانٍ).", "«is» — the pronoun of separation (or a second mubtadaʾ).", "«-dir» — zamîr-i fasl (veya ikinci mübtedâ)."),
  tok("بَيْتُ", "bayt", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the House» — the khabar, in rafʿ; a muḍāf.", "«Beyt» — haber, merfû; muzâf."),
  tok("الْمَقْدِسِ", "maqdis", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«of the Sanctuary» — the muḍāf ilayh.", "«Makdis» — muzâfun ileyh.", punct=".")])
sen("s22", "And it is the Farthest Mosque, around which Allah has blessed; and Allah blessed the children of Isḥāq as He blessed the children of Ismāʿīl, and among them were prophets and kings.", "Ve o, çevresini Allah'ın mübarek kıldığı Mescid-i Aksâ'dır; Allah, İsmâil'in çocuklarını mübarek kıldığı gibi İshak'ın çocuklarını da mübarek kıldı; içlerinde peygamberler ve hükümdarlar vardı.", [
  tok("وَهُوَ", "pron-3ms-munfasil", "pron", ["mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and it» — a detached pronoun; the mubtadaʾ.", "«ve o» — munfasıl zamir; mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "pron-3ms-munfasil", "pron")]),
  tok("الْمَسْجِدُ", "masjid", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Mosque» — the khabar.", "«Mescid» — haber."),
  tok("الْأَقْصَى", "aqsa", "noun", ["naat-sifa", "ism-tafdil", "ism-maqsur-manqus"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمُ تَفْضِيلٍ مَقْصُورٌ.", "«the Farthest» — the naʿt, rafʿ by an estimated ḍamma; an elative, maqṣūr.", "«Aksâ (en uzak)» — sıfat, takdîrî damme ile merfû; maksûr ism-i tafdil."),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ.", "«which» — the relative; a second naʿt.", "«-diği» — ism-i mevsûl; ikinci sıfat."),
  mazi("بَارَكَ", "baraka-bless", "«blessed»", "«mübarek kıldı»", hidden=None, tags=["form-iii-verbs", "ism-mawsul"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"), allah_fail(),
  tok("حَوْلَهُ", "hawl", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ (الْعَائِدُ).", "«around it» — an adverb of place in naṣb, annexed to the returning pronoun.", "«çevresini» — mansub mekân zarfı; âid zamirine muzâf.", punct="،", segments=[seg("حَوْلَ", "hawl", "noun"), seg("هُ", "pron-3ms", "pron")]),
  mazi("وَبَارَكَ", "baraka-bless", "«and blessed»", "«ve mübarek kıldı»", hidden=None, wa=True, tags=["form-iii-verbs"]), allah_fail(), fi(),
  tok("أَوْلَادِ", "walad", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ — جَمْعُ تَكْسِيرٍ.", "«the children» — in jarr; a muḍāf; a broken plural.", "«çocukları» — mecrur; muzâf; cem-i mükesser."),
  name_mudaf_ilayh("إِسْحٰقَ", "ishaq", "«of Isḥāq»", "«İshak'ın»"), kama(),
  mazi("بَارَكَ", "baraka-bless", "«blessed»", "«mübarek kıldı»", hidden="هُوَ", tags=["form-iii-verbs", "anwa-ma"], extra_ar=" — صِلَةُ مَا الْمَصْدَرِيَّةِ"), fi(),
  tok("أَوْلَادِ", "walad", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the children» — in jarr; a muḍāf.", "«çocukları» — mecrur; muzâf."),
  name_mudaf_ilayh("إِسْمَاعِيلَ", "ismail", "«of Ismāʿīl»", "«İsmâil'in»", punct="،"),
  kana(),
  tok("فِيهِمْ", "fi", "prep", [K, "huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهِمْ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«among them» — the jarr phrase is kāna's khabar, fronted.", "«içlerinde» — şibh-i cümle kâne'nin öne alınmış haberidir.", segments=[seg("فِي", "fi", "prep"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("أَنْبِيَاءُ", "nabi", "noun", [K, "mamnu-min-sarf", "jam-taksir"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.", "«prophets» — kāna's ism, delayed; no tanwīn, barred by the alif of femininity.", "«peygamberler» — kâne'nin geciktirilmiş ismi; memdûd te'nis elifi sebebiyle tenvinsiz."),
  tok("وَمُلُوكٌ", "malik-king", "noun", ["atf-nasaq", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَمُلُوكٌ مَعْطُوفٌ عَلَى أَنْبِيَاءُ مَرْفُوعٌ بِالضَّمَّةِ.", "«and kings» — joined to «prophets», in rafʿ.", "«ve hükümdarlar» — «peygamberler»e atıf, merfû.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("مُلُوكٌ", "malik-king", "noun")])])
sen("s23", "And Isḥāq had a son whose name was Yaʿqūb, and he was a prophet.", "Ve İshak'ın bir oğlu vardı; adı Yakub idi ve o bir peygamberdi.", [
  kana(), li_name("لِإِسْحٰقَ", "ishaq", "«Isḥāq had»", "«İshak'ın … vardı»"),
  tok("وَلَدٌ", "walad", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a son» — kāna's ism, delayed.", "«bir oğul» — kâne'nin geciktirilmiş ismi."),
  ismuhu(head="وَلَدٌ"),
  tok("يَعْقُوبُ", "yaqub", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yaʿqūb» — the khabar; a foreign name, a diptote.", "«Yakub» — haber; yabancı özel isim, gayr-i munsarıf."),
  tok("وَكَانَ", "kana", "verb", [K, "hollow-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "«and he was» — kāna with its ism «he» concealed.", "«ve o … idi» — kâne; ismi gizli «o».", segments=[seg("وَ", "wa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("نَبِيًّا", "nabi", "noun", [K], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a prophet» — kāna's khabar, in naṣb.", "«bir peygamber» — kâne'nin haberi, mansub.", punct=".")])
sen("s24", "And Yaʿqūb had twelve sons, among them Yūsuf the son of Yaʿqūb.", "Ve Yakub'un on iki oğlu vardı; içlerinden biri Yakub oğlu Yusuf'tu.", [
  kana(), name_ism_kana("يَعْقُوبُ", "yaqub", "«Yaʿqūb»", "«Yakub»"),
  lahu("وَشِبْهُ الْجُمْلَةِ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«had» (lit. «to him») — the fronted khabar of a nominal clause that is kāna's khabar.", "«vardı» (harfiyen «ona») — kâne'nin haberi olan isim cümlesinin öne alınmış haberi.", tags=[K]),
  tok("اثْنَا", "ithnan", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى — صَدْرُ الْعَدَدِ الْمُرَكَّبِ.", "«two-» — the delayed mubtadaʾ, rafʿ by the alif (attached to the dual); the first half of the compound number.", "«on iki (iki)» — geciktirilmiş mübtedâ, tesniyeye mülhak olduğu için elif ile merfû; bileşik sayının ilk yarısı."),
  tok("عَشَرَ", "ashar", "noun", ["mubtada-khabar"], "جُزْءٌ مِنَ الْعَدَدِ الْمُرَكَّبِ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ — يَقُومُ مَقَامَ نُونِ الْمُثَنَّى.", "«-teen (ten)» — the second half of the compound number, built on fatḥa; it stands where the dual's nūn would.", "«on» — bileşik sayının ikinci yarısı, fetha üzere mebnî; tesniye nûnunun yerini tutar."),
  tok("وَلَدًا", "walad", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — تَمْيِيزُ الْعَدَدِ مِنْ أَحَدَ عَشَرَ إِلَى تِسْعَةٍ وَتِسْعِينَ مُفْرَدٌ مَنْصُوبٌ.", "«son(s)» — the tamyīz of the number, singular and in naṣb (11 to 99).", "«oğul» — sayının temyizi, 11–99 arasında müfred ve mansub.", punct="،"),
  tok("مِنْهُمْ", "min", "prep", ["huruf-jarr", "mubtada-khabar"], "مِنْ حَرْفُ جَرٍّ، وَهُمْ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ خَبَرٌ مُقَدَّمٌ.", "«among them» — the fronted khabar.", "«içlerinden» — öne alınmış haber.", segments=[seg("مِنْ", "min", "prep"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("يُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūsuf» — the delayed mubtadaʾ; a foreign name, a diptote.", "«Yusuf» — geciktirilmiş mübtedâ; yabancı özel isim, gayr-i munsarıf."),
  tok("بْنُ", "ibn", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ (أَوْ نَعْتٌ) مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ — وَحُذِفَتْ أَلِفُهُ بَيْنَ عَلَمَيْنِ.", "«son of» — a badal (or naʿt) of the name, in rafʿ; a muḍāf, its alif dropped between two names.", "«oğlu» — ismin bedeli (veya sıfatı), merfû; muzâf, elifi iki özel isim arasında düşer."),
  name_mudaf_ilayh("يَعْقُوبَ", "yaqub", "«Yaʿqūb»", "«Yakub»", punct=".")])
sen("s25", "And Yūsuf has a wondrous story in the Qurʾān.", "Ve Yusuf'un Kur'an'da şaşırtıcı bir kıssası vardır.", [
  tok("وَيُوسُفُ", "yusuf", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيُوسُفُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Yūsuf» — the mubtadaʾ; a diptote.", "«ve Yusuf» — mübtedâ; gayr-i munsarıf.", segments=[seg("وَ", "wa", "conj"), seg("يُوسُفُ", "yusuf", "propn")]),
  lahu("وَشِبْهُ الْجُمْلَةِ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ الْأَوَّلِ.", "«has» (lit. «to him») — the fronted khabar of the inner clause, which is the first mubtadaʾ's khabar.", "«vardır» (harfiyen «ona») — iç cümlenin öne alınmış haberi; cümle ilk mübtedânın haberidir."),
  tok("قِصَّةٌ", "qissa", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a story» — the delayed mubtadaʾ.", "«bir kıssa» — geciktirilmiş mübtedâ."),
  tok("عَجِيبَةٌ", "ajib", "noun", ["naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«wondrous» — the naʿt.", "«şaşırtıcı» — sıfat."),
  fi(), tok("الْقُرْآنِ", "quran", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the Qurʾān» — in jarr.", "«Kur'an» — mecrur.", punct=".")])
sen("s26", "And here is this story for you!", "Ve işte sana bu kıssa!", [
  tok("وَإِلَيْكَ", "ilayka-ism-fil", "part", ["ism-fil"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِلَيْكَ اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى خُذْ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: أَنْتَ.", "«and here, take» — a noun-verb (ism fiʿl) meaning «take!»; the doer «you» is concealed.", "«ve işte, al» — ism-i fiil, «al!» mânasında; fâil gizli «sen».", segments=[seg("وَ", "wa", "conj"), seg("إِلَيْكَ", "ilayka-ism-fil", "part")]),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«this»", "«bu»", tags=["ism-fil"]),
  tok("الْقِصَّةَ", "qissa", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«story» — the badal of the demonstrative, in naṣb.", "«kıssa» — ism-i işâretin bedeli, mansub.", punct="!")])

# ---------------------------------------------------------------- glossary
NEW = {
 "ajib": G("ajib", "عَجِيب", "ع ج ب", "noun", "wondrous, strange (ṣifa mushabbaha)", "şaşırtıcı, acayip (sıfat-ı müşebbehe)", 1),
 "sham": G("sham", "الشَّام", None, "propn", "al-Shām — Greater Syria", "Şam — Suriye bölgesi", 1),
 "tafa": G("tafa", "طَافَ", "ط و ف", "verb", "to go around, to circumambulate (طَافَ بِـ)", "tavaf etmek, etrafında dönmek", 1, form="I"),
 "taqabbala": G("taqabbala", "تَقَبَّلَ", "ق ب ل", "verb", "to accept (an offering, a prayer)", "kabul etmek, kabul buyurmak", 1, form="V"),
 "tawajjaha": G("tawajjaha", "تَوَجَّهَ", "و ج ه", "verb", "to turn one's face toward (تَوَجَّهَ إِلَى)", "yönelmek, yüzünü çevirmek", 1, form="V"),
 "sara-name": G("sara-name", "سَارَة", None, "propn", "Sārah, Ibrāhīm's first wife, the mother of Isḥāq", "Sâre — İbrâhim'in ilk hanımı, İshak'ın annesi", 1),
 "maqdis": G("maqdis", "الْمَقْدِس", "ق د س", "noun", "the sanctuary; بَيْتُ الْمَقْدِسِ — the holy House of Jerusalem", "mukaddes yer; Beytülmakdis — Kudüs'teki mukaddes ev", 2),
 "aqsa": G("aqsa", "الْأَقْصَى", "ق ص و", "noun", "the farthest (an elative, maqṣūr); الْمَسْجِدُ الْأَقْصَى", "en uzak (maksûr ism-i tafdil); Mescid-i Aksâ", 2),
 "ashar": G("ashar", "عَشَرَ", "ع ش ر", "noun", "ten — the second part of the compound numbers eleven to nineteen (أَحَدَ عَشَرَ … تِسْعَةَ عَشَرَ)", "on — on bir'den on dokuz'a bileşik sayıların ikinci parçası", 1),
 "samii": G("samii", "سَمِيع", "س م ع", "noun", "all-hearing (ṣifa mushabbaha; an attribute of Allah)", "her şeyi işiten (sıfat-ı müşebbehe; Allah'ın sıfatı)", 1),
 "ilayka-ism-fil": G("ilayka-ism-fil", "إِلَيْكَ", None, "part", "«here, take!» — إِلَيْكَ used as a noun-verb (ism fiʿl) meaning خُذْ", "«al, işte!» — ism-i fiil olarak إِلَيْكَ, خُذْ mânasında", 2),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
for _k, _lm in [("ishaq", "إسحاق"), ("yaqub", "يعقوب"), ("yusuf", "يوسف"), ("kaaba", "الكعبة"), ("inda", "عند"), ("alim", "عليم"), ("muhammad", "محمد"), ("ithnan", "اثنان"), ("bana", "بنى"), ("sakana", "سكن"), ("naqala", "نقل")]:
    _e = GLOSS_ADD.get(_k) or TG.get(_k); assert _e and bare(_e["lemma"]).replace("ِ", "") == _lm, (_k, _e and _e["lemma"])
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tafa", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "طَاف", "طُف", "طُوف", "طُف", "طُوف", "طُف", "طَوَاف", "طَائِف", maful="مَطُوف", pmz="طِيفَ", pmd="يُطَافُ", note="لَازِمٌ — يَتَعَدَّى بِالْبَاءِ: طَافَ بِالْبَيْتِ."))
put_morph(mo, "taqabbala", _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَقَبَّل", "تَقَبَّل", "تَقَبَّل", "تَقَبُّل", "مُتَقَبِّل", "مُتَقَبَّل", "تُقُبِّلَ", "يُتَقَبَّلُ", note="مُتَعَدٍّ — مُطَاوِعُ «قَبَّلَ»."))
put_morph(mo, "tawajjaha", _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَوَجَّه", "تَوَجَّه", "تَوَجَّه", "تَوَجُّه", "مُتَوَجِّه", note="لَازِمٌ — يَتَعَدَّى بِإِلَى؛ مِثَالٌ وَاوِيٌّ تَبْقَى وَاوُهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 7 (print pp. 23–26, sections 15 «الْكَعْبَة» and 16 «بَيْتُ الْمَقْدِسِ»): the building of the Kaʿba (s1–s7), the prayer of al-Baqara 2:127 as the print sets it (s8, marked), the Muslims' turning and pilgrimage and the prayers of blessing (s9–s16); Sārah and Isḥāq, al-Shām and Bayt al-Maqdis, Yaʿqūb and his twelve sons, the hand-over to Yūsuf's story (s17–s26). "
          "One printed line is one sentence; the first printed line of section 15 holds two sentences and is split at its full stop (s1, s2). The print's own spellings are kept: إِسْحٰقُ with a dagger alif, لِلّٰهِ, هٰذَا.")
ADD_TR = (" Yedinci bölüm (basılı s. 23–26, 15. kısım «الْكَعْبَة» ve 16. kısım «بَيْتُ الْمَقْدِسِ»): Kâbe'nin yapılışı (s1–s7), Bakara 2:127 duası baskıdaki şekliyle (s8, işaretli), Müslümanların yönelişi ve haccı ile salât duaları (s9–s16); Sâre ve İshak, Şam ve Beytülmakdis, Yakub ve on iki oğlu, Yusuf kıssasına geçiş (s17–s26). "
          "Basılı her satır bir cümledir; 15. kısmın ilk satırı iki cümle taşır ve noktasından bölünmüştür (s1, s2). Baskının imlâsı korunmuştur: hançer elifli إِسْحٰقُ, لِلّٰهِ, هٰذَا.")
write_out(7, S, TITLE, ADD_EN, ADD_TR, "pp. 23–26", GLOSS_ADD)
report(7, S, GLOSS_ADD, ())
