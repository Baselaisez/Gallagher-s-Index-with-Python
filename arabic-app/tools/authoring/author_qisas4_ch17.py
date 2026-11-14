# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 17: «قِصَّةُ أَيُّوبَ» — the story of Ayyūb and Yūnus opens: §1 (a different kind of story),
§2 (Ayyūb's patience), §3 (trial and gift, with 21:83–84); print pp. 26–28.
python3 tools/authoring/author_qisas4_ch17.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ أَيُّوبَ: مِحْنَةٌ وَمِنْحَةٌ", "en": "The story of Ayyūb: a trial and a gift", "tr": "Eyyûb'un kıssası: mihnet ve lütuf"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; IS = "al-istifham"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr", wa=False):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    if wa: return tok(full, lex, "noun", [AT, NA] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C[:-1] + " — مَعْطُوفٌ عَلَى النَّعْتِ قَبْلَهُ.", "«and» + " + en + " — a second naʿt, joined.", "«ve» + " + tr + " — ikinci sıfat, ma'tûf.", punct=punct, segments=wa_(full[2:], lex, "noun"))
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def noun_pron(full, lex, stem, pron_form, pron_lex, ar, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", list(tags), ar, en, tr, punct=punct, segments=[seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])
def atf(full, lex, en, tr, case="jarr", punct=None, tags=(), pos="noun", sign=None):
    C = {"jarr": "مَعْطُوفٌ مَجْرُورٌ " + (sign or "بِالْكَسْرَةِ"), "raf": "مَعْطُوفٌ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "nasb": "مَعْطُوفٌ مَنْصُوبٌ " + (sign or "بِالْفَتْحَةِ")}[case]
    return tok(full, lex, pos, [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C + ".", "«and» + " + en + " — joined by the wāw.", "«ve» + " + tr + " — vâv ile atıf.", punct=punct, segments=wa_(full[2:], lex, pos))
def prep(full, lex, en, tr, punct=None, ar="حَرْفُ جَرٍّ."): return tok(full, lex, "prep", [HJ], ar, en, tr, punct=punct)
def li_pron(full, pron_form, pron_lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, "li", "prep", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra + ".", en, tr, punct=punct, segments=[seg(full[:2], "li", "prep"), seg(pron_form, pron_lex, "pron")])
def v_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, fa=False, hidden="هُوَ", ta=False):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    body = (" فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ." if ta else f" فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}، وَالضَّمِيرُ مَفْعُولٌ بِهِ." if hidden else " فِعْلٌ مَاضٍ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.")
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + [MB] + list(tags), pre + stem + body, en + " — a māḍī; the pronoun is its object.", tr + " — mâzî; zamir mef'ûl.", punct=punct, segments=segs)

# ---------------------------------------------------------------- §1 قِصَّةُ أَيُّوبَ نَمَطٌ آخَرُ مِنَ الْقَصَصِ (print p. 26)
sen("s1", "The story of Ayyūb in the Qurʾān is another kind of story, and another manifestation of the manifestations of God's favours on His believing servants — the patient, the thankful — and on His beloved prophets;",
        "Eyyûb'un Kur'ân'daki kıssası başka bir tür kıssadır; Allah'ın mümin, sabreden ve şükreden kullarına ve sevgili peygamberlerine olan nimetlerinin tecellilerinden bir başka tecellidir;", [
  tok("وَقِصَّةُ", "qissa", "noun", [MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقِصَّةُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the story [of]» — the mubtadaʾ, annexed.", "«ve kıssası» — mübtedâ, muzâf.", segments=wa_("قِصَّةُ", "qissa", "noun")),
  tok("أَيُّوبَ", "ayyub", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ayyūb» — jarr by fatḥa (a diptote).", "«Eyyûb'un» — gayr-i munsarıf, fetha ile mecrûr."),
  fi(), majrur("الْقُرْآنِ", "quran", "«the Qurʾān»", "«Kur'ân'da»"),
  tok("نَمَطٌ", "namat", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a kind» — the khabar.", "«bir tür» — haber."),
  tok("آخَرُ", "akhar", "noun", [NA, MM], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — the naʿt; a diptote.", "«başka» — sıfat; gayr-i munsarıf."),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْقَصَصِ", "qasas", "«the stories»", "«kıssalar»", punct="،"),
  atf("وَمَظْهَرٌ", "mazhar", "«a manifestation»", "«bir tecelli»", "raf"),
  tok("آخَرُ", "akhar", "noun", [NA, MM], "نَعْتٌ مَرْفُوعٌ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another»", "«başka»"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("مَظَاهِرِ", "mazhar", "«the manifestations»", "«tecellilerinden»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("نِعَمِ", "nima", "«of the favours»", "«nimetlerinin»", tags=[ID, JT], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  noun_pron("عِبَادِهِ", "abd", "عِبَادِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His servants»", "«kullarına»", tags=[HJ, ID, JT]),
  tok("الْمُؤْمِنِينَ", "mumin", "noun", [NA, JS, "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«believing» — the naʿt, jarr by the yāʾ.", "«mümin» — sıfat, yâ ile mecrûr.", punct="،"),
  tok("الصَّابِرِينَ", "sabir", "noun", [NA, JS, "ism-fail"], "نَعْتٌ ثَانٍ مَجْرُورٌ بِالْيَاءِ.", "«the patient» — a second naʿt.", "«sabreden» — ikinci sıfat."),
  tok("الشَّاكِرِينَ", "shakir", "noun", [NA, JS, "ism-fail"], "نَعْتٌ ثَالِثٌ مَجْرُورٌ بِالْيَاءِ.", "«the thankful» — a third naʿt.", "«şükreden» — üçüncü sıfat.", punct="،"),
  tok("وَالْأَنْبِيَاءِ", "nabi", "noun", [AT, JT], "الْوَاوُ عَاطِفَةٌ، وَالْأَنْبِيَاءِ مَعْطُوفٌ عَلَى عِبَادِهِ مَجْرُورٌ.", "«and the prophets» — joined to «His servants».", "«ve peygamberlerine» — kullarına ma'tûf.", segments=wa_("الْأَنْبِيَاءِ", "nabi", "noun")),
  tok("الْمَحْبُوبِينَ", "mahbub", "noun", [NA, JS, "ism-maful"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«beloved» — the naʿt.", "«sevgili» — sıfat.", punct="؛"),
])
sen("s2", "he had a great deal of beasts, cattle and tillage, and pleasing children; then he was tried in all of that, and it went, down to the last of it;",
        "onun pek çok hayvanı, davarı ve ekini, hoş evlâtları vardı; sonra bunların hepsinde sınandı ve hepsi sonuncusuna kadar gitti;", [
  tok("فَقَدْ", "qad", "part", ["qad-harf"], "الْفَاءُ لِلتَّعْلِيلِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«indeed»", "«gerçekten»", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«there was»", "«vardı»"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«he had» — kāna's fronted khabar.", "«onun … vardı» — kâne'nin öne alınmış haberi.", tags=[KN], extra=" — خَبَرُ كَانَ مُقَدَّمٌ"),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الدَّوَابِّ", "dabba", "«beasts»", "«hayvanlar»", tags=[JT, "doubled-verbs"]),
  atf("وَالْأَنْعَامِ", "anam", "«cattle»", "«davarlar»", "jarr", tags=[JT]),
  atf("وَالْحَرْثِ", "harth", "«tillage»", "«ekin»", "jarr"),
  tok("شَيْءٌ", "shay", "noun", [KN], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a deal» (lit. a thing) — kāna's delayed ism.", "«bir şey» — kâne'nin ismi."),
  naat("كَثِيرٌ", "kathir", "«great»", "«pek çok»", case="raf", punct="،"),
  atf("وَأَوْلَادٌ", "walad", "«children»", "«evlâtlar»", "raf", tags=[JT]),
  naat("مَرْضِيَّةٌ", "mardi", "«pleasing»", "«hoş»", case="raf", tags=["ism-maful"], punct="،"),
  tok("فَابْتُلِيَ", "ibtala", "verb", [AT, NF, "naqis-verbs", "form-viii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَابْتُلِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«then he was tried» — a passive.", "«sonra sınandı» — meçhul.", segments=[seg("فَ", "fa", "conj"), seg("ابْتُلِيَ", "ibtala", "verb")]),
  fi(), tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ بِفِي.", "«that»", "«bunların»"),
  noun_pron("كُلِّهِ", "kull", "كُلِّ", "هِ", "pron-3ms", "تَوْكِيدٌ مَعْنَوِيٌّ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«all of» — an emphasis of totality.", "«hepsinde» — mânevî te'kid.", punct="،", tags=["tawkid", ID]),
  mazi("وَذَهَبَ", "dhahaba", "«and it went»", "«ve gitti»", tags=[AT], wa=True, hidden="هُوَ"),
  prep("عَنْ", "an", "«down to» (lit. to)", "«… -e kadar»"),
  noun_pron("آخِرِهِ", "akhir", "آخِرِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the last of it»", "«sonuncusuna»", punct="،", tags=[HJ, ID]),
])
sen("s3", "then he was tried in his body, so that nothing of him stayed sound but his heart and his tongue, with which he remembered God, Mighty and Majestic,",
        "sonra bedeninde sınandı; kalbi ve dili dışında sağlam bir yeri kalmadı; onlarla Aziz ve Celîl olan Allah'ı zikrediyordu,", [
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  tok("ابْتُلِيَ", "ibtala", "verb", [NF, "naqis-verbs", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«he was tried»", "«sınandı»"),
  fi(), noun_pron("جَسَدِهِ", "jasad", "جَسَدِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his body»", "«bedeninde»", punct="،", tags=[HJ, ID]),
  tok("فَلَمْ", "lam-jazima", "part", [AT, LJ], "الْفَاءُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«so that … not»", "«… -madı»", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يَبْقَ", "baqiya", "verb", [LJ, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ.", "«stayed» — jazm by the dropped weak letter.", "«kaldı» — illet harfinin düşmesiyle meczum."),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of him»", "«ondan»"),
  fail("سَلِيمٌ", "salim-sound", "«[anything] sound»", "«sağlam bir yer»", tags=["sifa-mushabbaha"]),
  tok("سِوَى", "siwa", "noun", ["istithna", ID], "اسْمٌ لِلِاسْتِثْنَاءِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«but» — the exceptive noun siwā, annexed.", "«… dışında» — istisnâ ismi sivâ, muzâf."),
  noun_pron("قَلْبِهِ", "qalb", "قَلْبِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his heart»", "«kalbi»", tags=[ID]),
  noun_pron("وَلِسَانِهِ", "lisan", "وَلِسَانِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَلِسَانِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his tongue»", "«ve dili»", tags=[AT, ID]),
  mudari("يَذْكُرُ", "dhakara", "«he remembered»", "«zikrediyordu»", tags=[HL, MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  prep_pron("بِهِمَا", "bi", "هِمَا", "pron-3d", "«with them both»", "«onlarla»"),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'ı» — mef'ûl."),
  mazi("عَزَّ", "azza-mighty", "«Mighty»", "«Aziz»", tags=["doubled-verbs", NA], hidden="هُوَ", extra_ar=" — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ"),
  mazi("وَجَلَّ", "jalla", "«and Majestic»", "«ve Celîl»", tags=[AT, "doubled-verbs"], wa=True, hidden="هُوَ", punct="،"),
])
sen("s4", "until his companions loathed him and he was set apart in a corner of the town; none of the people stayed to be tender to him but his wife, who used to look after him — and she too fell into need, so she came to serve people for his sake.",
        "öyle ki yanında oturan bile ondan tiksindi, şehrin bir köşesine tek başına bırakıldı; ona şefkat gösteren kimse kalmadı — yalnız işini gören karısı kaldı; o da muhtaç düştü ve onun uğruna insanlara hizmet eder oldu.", [
  tok("حَتَّى", "hatta", "part", [HJ], "حَرْفُ ابْتِدَاءٍ (غَايَةٍ).", "«until»", "«öyle ki»"),
  v_pron("عَافَهُ", "afa-loathe", "عَافَ", "هُ", "pron-3ms", "«loathed him»", "«ondan tiksindi»", tags=["hollow-verbs"], hidden=None),
  fail("الْجَلِيسُ", "jalis", "«the companion»", "«yanında oturan»", punct="،"),
  tok("وَأُفْرِدَ", "afrada", "verb", [AT, NF, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُفْرِدَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«and he was set apart» — a passive.", "«ve tek başına bırakıldı» — meçhul.", segments=wa_("أُفْرِدَ", "afrada", "verb")),
  fi(), majrur("نَاحِيَةٍ", "nahiya", "«a corner»", "«bir köşesine»"),
  prep("مِنَ", "min", "«of»", "«-in»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْبَلَدِ", "balad", "«the town»", "«şehrin»", punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … -madı»", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("يَبْقَ", "baqiya", "verb", [LJ, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ.", "«stayed»", "«kaldı»"),
  fail("أَحَدٌ", "ahad", "«anyone»", "«kimse»"),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlar»"),
  mudari("يَحْنُو", "hana-tender", "«to be tender»", "«şefkat gösterir»", tags=["jumla-sifa", "naqis-verbs"], hidden="هُوَ", extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْجُمْلَةُ نَعْتٌ لِأَحَدٌ"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«to him»", "«ona»", punct="،"),
  tok("سِوَى", "siwa", "noun", ["istithna", ID], "اسْمٌ لِلِاسْتِثْنَاءِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«but»", "«yalnız»"),
  noun_pron("زَوْجَتِهِ", "zawja", "زَوْجَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wife»", "«karısı»", tags=[ID]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«who»", "«… olan»"),
  tok("كَانَتْ", "kana", "verb", [MW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — صِلَةٌ.", "«used to» — kāna; the ṣila.", "«idi» — kâne; sıla."),
  mudari("تَقُومُ", "qama", "«look after»", "«görür»", tags=[KN, "hollow-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَتْ"),
  noun_pron("بِأَمْرِهِ", "amr-noun", "بِأَمْرِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَأَمْرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his affairs»", "«işini»", punct="،", tags=[HJ, ID]),
  mazi_ta("وَاحْتَاجَتْ", "ihtaja", "«and she fell into need»", "«ve muhtaç düştü»", tags=[AT, "hollow-verbs", "form-viii-verbs"], wa=True),
  tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (آضَ) مَنْصُوبٌ — بِمَعْنَى: كَذٰلِكَ.", "«too» — an absolute object of an understood verb.", "«o da» — mukadder fiilin mef'ûl-i mutlakı."),
  tok("فَصَارَتْ", "sara", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَصَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«so she came to» — ṣāra, a sister of kāna.", "«… oldu» — sâra, kâne'nin kardeşi.", segments=[seg("فَ", "fa", "conj"), seg("صَارَتْ", "sara", "verb")]),
  mudari("تَخْدُمُ", "khadama-serve", "«serve»", "«hizmet eder»", tags=[KN, MB], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ صَارَتْ"),
  maful_("النَّاسَ", "nas", "«people»", "«insanlara»"),
  prep("مِنْ", "min", "«for» (lit. from)", "«… uğruna»"),
  noun_pron("أَجْلِهِ", "ajl", "أَجْلِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مِنْ أَجْلِ: لِلتَّعْلِيلِ.", "«his sake»", "«onun uğruna»", punct=".", tags=[HJ, ID]),
])

# ---------------------------------------------------------------- §2 صَبْرُ أَيُّوبَ (print p. 27)
sen("s5", "And despite all this he was patient and thankful, his tongue ever busy with remembrance and thanks; he did not complain, nor reproach, nor grumble, nor grow angry;",
        "Bütün bunlara rağmen sabırlı ve şükredendi; dili zikir ve şükürle meşguldü; şikâyet etmiyor, sitem etmiyor, söylenmiyor, öfkelenmiyordu;", [
  kana(),
  tok("رَغْمَ", "raghma", "noun", [MF, ID], "مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ، مُضَافٌ — بِمَعْنَى: عَلَى الرَّغْمِ مِنْ.", "«despite»", "«rağmen»"),
  mudaf_ilayh("كُلِّ", "kull", "«all»", "«bütün»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this»", "«bunlara»"),
  tok("صَابِرًا", "sabir", "noun", [KN, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«patient» — kāna's khabar.", "«sabırlı» — kâne'nin haberi."),
  tok("شَاكِرًا", "shakir", "noun", [KN, "ism-fail"], "خَبَرٌ ثَانٍ لِكَانَ مَنْصُوبٌ.", "«thankful» — a second khabar.", "«şükreden» — ikinci haber."),
  mudari("يَلْهَجُ", "lahija", "«was ever busy»", "«meşguldü»", tags=[HL], hidden=None, extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  noun_pron("لِسَانُهُ", "lisan", "لِسَانُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his tongue» — the doer.", "«dili» — fâil.", tags=[FL, ID]),
  tok("بِالذِّكْرِ", "dhikr", "noun", [HJ, "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَالذِّكْرِ مَجْرُورٌ.", "«with remembrance»", "«zikirle»", segments=[seg("بِ", "bi", "prep"), seg("الذِّكْرِ", "dhikr", "noun")]),
  atf("وَالشُّكْرِ", "shukr", "«thanks»", "«şükürle»", "jarr", tags=["masdar"], punct="،"),
  la_nafiya(),
  neg_mudari("يَشْكُو", "shaka", "«complained»", "«şikâyet eder»", tags=["naqis-verbs"], hidden="هُوَ", extra=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ"),
  la_nafiya(wa=True),
  neg_mudari("يَتَعَتَّبُ", "taattaba", "«reproached»", "«sitem eder»", tags=[AT, "form-v-verbs"], hidden="هُوَ", extra=""),
  la_nafiya(wa=True),
  neg_mudari("يَتَذَمَّرُ", "tadhammara", "«grumbled»", "«söylenir»", tags=[AT, "form-v-verbs"], hidden="هُوَ", extra=""),
  la_nafiya(wa=True),
  neg_mudari("يَغْضَبُ", "ghadiba", "«grew angry»", "«öfkelenir»", tags=[AT], hidden="هُوَ", extra="", punct="،"),
])
sen("s6", "and he went on like that for long years, cast on the refuse-heap of the Children of Israel, with the vermin crawling over his body.",
        "ve uzun yıllar böyle kaldı; İsrâiloğullarının çöplüğüne atılmış, bedeninde haşerat dolaşırdı.", [
  mazi("وَدَامَ", "dama", "«and he went on»", "«ve devam etti»", tags=[AT, "hollow-verbs"], wa=True, hidden="هُوَ"),
  prep("عَلَى", "ala", "«in»", "«… üzere»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«that»", "«bu hâl»"),
  tok("سِنِينَ", "sana", "noun", [MF, JS], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«years» — a ẓarf, naṣb by the yāʾ (attached to the sound plural).", "«yıllar» — zarf; cem'-i müzekker sâlime mülhak, yâ ile mansub."),
  naat("طِوَالًا", "tiwal", "«long»", "«uzun»", case="nasb", tags=[JT]),
  tok("مُلْقًى", "mulqa", "noun", [HL, "ism-maful", "ism-maqsur-manqus"], "حَالٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمُ مَفْعُولٍ مَقْصُورٌ.", "«cast» — a ḥāl; a maqṣūr passive participle.", "«atılmış» — hâl; maksûr ism-i mef'ûl."),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("كُنَاسَةِ", "kunasa", "«the refuse-heap»", "«çöplüğüne»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  tok("بَنِي", "banu-israil", "noun", [ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«the Children [of]» — jarr by the yāʾ, its nūn dropped for the iḍāfa.", "«oğullarının» — yâ ile mecrûr; nûnu izâfet için düşmüş."),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Israel» — jarr by fatḥa.", "«İsrâil» — fetha ile mecrûr."),
  mudari("تَخْتَلِفُ", "ikhtalafa", "«crawling to and fro»", "«dolaşırdı»", tags=[HL, "form-viii-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  fail("الدَّوَابُّ", "dabba", "«the vermin»", "«haşerat»", tags=[JT]),
  fi(), noun_pron("جَسَدِهِ", "jasad", "جَسَدِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his body»", "«bedeninde»", punct=".", tags=[HJ, ID]),
])

# ---------------------------------------------------------------- §3 مِحْنَةٌ وَمِنْحَةٌ (print p. 27)
sen("s7", "When what God had willed of his trial was complete, and what He intended by it of perfecting him, raising his degrees and contentment with the decree, He inspired him with the answered prayer,",
        "Allah'ın onun sınanmasından dilediği ve onunla murat ettiği kemale erdirme, dereceleri yükseltme ve kazaya rıza tamamlanınca, ona kabul edilen duayı ilham etti;", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF, SH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -ınca»", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("تَمَّ", "tamma", "«was complete»", "«tamamlandı»", tags=[SH, "doubled-verbs"], hidden=None),
  tok("مَا", "ma-mawsula", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«what» — the doer.", "«… şey» — fâil."),
  v_pron("أَرَادَهُ", "arada", "أَرَادَ", "هُ", "pron-3ms", "«had willed»", "«diledi»", tags=[MW, "hollow-verbs", "form-iv-verbs"], hidden=None),
  allah_fail(),
  prep("مِنِ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  noun_pron("ابْتِلَائِهِ", "ibtila", "ابْتِلَائِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his trial»", "«sınanmasından»", punct="،", tags=[HJ, ID, "masdar"]),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and what»", "«ve … şey»", segments=wa_("مَا", "ma-mawsula", "pron")),
  mazi("أَرَادَ", "arada", "«He intended»", "«murat etti»", tags=[MW, "hollow-verbs", "form-iv-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by it»", "«onunla»"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  majrur("تَكْمِيلٍ", "takmil", "«perfecting»", "«kemale erdirme»", tags=["masdar"], punct="،"),
  atf("وَرَفْعِ", "raf", "«raising»", "«yükseltme»", "jarr", tags=[ID, "masdar"]),
  mudaf_ilayh("دَرَجَاتٍ", "daraja", "«degrees»", "«dereceleri»", tags=[JM], punct="،"),
  atf("وَالرِّضَا", "rida-contentment", "«contentment»", "«rıza»", "jarr", tags=["masdar", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ"),
  tok("بِالْقَضَاءِ", "qada", "noun", [HJ, "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْقَضَاءِ مَجْرُورٌ.", "«with the decree»", "«kazaya»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْقَضَاءِ", "qada", "noun")]),
  v_pron("أَلْهَمَهُ", "alhama", "أَلْهَمَ", "هُ", "pron-3ms", "«He inspired him»", "«ona ilham etti»", tags=[SH, MX, "form-iv-verbs"], hidden="هُوَ"),
  tok("الدُّعَاءَ", "dua", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«the prayer» — the second object.", "«duayı» — ikinci mef'ûl."),
  naat("الْمُسْتَجَابَ", "mustajab", "«answered»", "«kabul edilen»", case="nasb", tags=["ism-maful", "form-x-verbs"], punct="،"),
])
sen("s8", "in which his helplessness and misery showed, and that there is no refuge from God but to Him, and that He has power over all things;",
        "o duada aczi ve çaresizliği ortaya çıktı; Allah'tan yine O'na sığınmaktan başka sığınak olmadığı ve O'nun her şeye kadir olduğu belirdi;", [
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِلدُّعَاءِ.", "«in which» (lit. which)", "«… -ği»"),
  mazi("تَجَلَّى", "tajalla", "«showed»", "«ortaya çıktı»", tags=[MW, "naqis-verbs", "form-v-verbs"], hidden=None, extra_ar=" — صِلَةٌ"),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in it»", "«onda»"),
  noun_pron("عَجْزُهُ", "ajz", "عَجْزُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his helplessness» — the doer.", "«aczi» — fâil.", tags=[FL, ID, "masdar"]),
  noun_pron("وَبُؤْسُهُ", "bus", "وَبُؤْسُ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَبُؤْسُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his misery»", "«ve çaresizliği»", punct="،", tags=[AT, ID, "masdar"]),
  tok("وَأَنْ", "an-masdariyya", "part", [AT, AN], "الْوَاوُ عَاطِفَةٌ، وَأَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ وَاسْمُهَا ضَمِيرُ الشَّأْنِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى عَجْزُهُ.", "«and that» — the lightened an with the pronoun of the matter as its ism; the clause is joined to «his helplessness».", "«ve … olduğu» — tahfif edilmiş en; şe'n zamiri ismi; cümle «aczi»ne ma'tûf.", segments=wa_("أَنْ", "an-masdariyya", "part")),
  tok("لَا", "la-nafiya", "part", ["la-nafiya-lil-jins"], "لَا النَّافِيَةُ لِلْجِنْسِ.", "«no»", "«yok»"),
  tok("مَلْجَأَ", "malja", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«refuge» — lā's ism, built on fatḥa.", "«sığınak» — lâ'nın ismi."),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ."),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'tan»"),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ (حَصْرٍ).", "«but»", "«… -den başka»"),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Him» — standing in the place of lā's khabar.", "«O'na» — lâ'nın haberi yerinde.", tags=["la-nafiya-lil-jins"], punct="،"),
  tok("وَأَنَّهُ", "anna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«and that He»", "«ve O'nun … olduğu»", segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  khabar_inna("الْقَادِرُ", "qadir", "«has power» (lit. the Able)", "«kadir olduğu»", part="أَنَّ", tags=["ism-fail"]),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("كُلِّ", "kull", "«all»", "«her»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«things»", "«şeye»", punct="؛"),
])
sen("s9", "and God healed him in his body and his family, restored his wealth to him and blessed him in all of it, so that it became many times over; God, Blessed and Exalted, says:",
        "Allah onu bedeninde ve ailesinde iyileştirdi, malını ona geri verdi ve bunların hepsinde ona bereket verdi; böylece kat kat fazlası oldu. Allah Tebâreke ve Teâlâ buyurur ki:", [
  v_pron("وَعَافَاهُ", "afa-heal", "عَافَا", "هُ", "pron-3ms", "«and healed him»", "«ve onu iyileştirdi»", tags=["naqis-verbs", "form-iii-verbs"], wa=True, hidden=None),
  allah_fail(),
  fi(), noun_pron("بَدَنِهِ", "badan", "بَدَنِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his body»", "«bedeninde»", tags=[HJ, ID]),
  noun_pron("وَأَهْلِهِ", "ahl", "وَأَهْلِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَأَهْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his family»", "«ve ailesinde»", punct="،", tags=[AT, ID]),
  mazi("وَرَدَّ", "radda", "«and restored»", "«ve geri verdi»", tags=[AT, "doubled-verbs", MB], wa=True, hidden="هُوَ"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«to him»", "«ona»"),
  noun_pron("مَالَهُ", "mal", "مَالَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wealth»", "«malını»", punct="،", tags=[MB, ID]),
  mazi("وَبَارَكَ", "baraka-bless", "«and blessed»", "«ve bereket verdi»", tags=[AT, "form-iii-verbs"], wa=True, hidden="هُوَ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«him»", "«ona»"),
  fi(), majrur("كُلِّ", "kull", "«all»", "«hepsinde»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that»", "«bunların»", punct="،"),
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«so that it became»", "«böylece … oldu»", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("أَضْعَافًا", "dif", "noun", [KN, JT], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ ضِعْفٍ.", "«many times over» — kāna's khabar.", "«kat kat» — kâne'nin haberi."),
  naat("مُضَاعَفَةً", "mudaaf", "«multiplied»", "«fazlası»", case="nasb", tags=["ism-maful", "form-iii-verbs"], punct="،"),
  mudari("يَقُولُ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs", MB], hidden=None),
  allah_fail(),
  mazi("تَبَارَكَ", "tabaraka", "«Blessed»", "«Tebâreke»", tags=[NA, "form-vi-verbs"], hidden="هُوَ", extra_ar=" — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ"),
  tok("وَتَعَالَى", "taala", "verb", [AT, NA, "naqis-verbs", "form-vi-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَعَالَى فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and Exalted»", "«ve Teâlâ»", punct=":", segments=wa_("تَعَالَى", "taala", "verb")),
])
sen("s10", "«And Ayyūb, when he called to his Lord: Harm has touched me, and You are the most merciful of the merciful» (21:83).",
        "«Eyyûb'u da [an]: hani Rabbine: Bana zarar dokundu, sen merhametlilerin en merhametlisisin, diye seslenmişti» (21:83).", [
  *quran([
  tok("وَأَيُّوبَ", "ayyub", "propn", [AT, MB, MM, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَأَيُّوبَ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Ayyūb» — the object of an understood «remember».", "«ve Eyyûb'u» — mukadder «an» fiilinin mef'ûlü.", segments=wa_("أَيُّوبَ", "ayyub", "propn")),
  tok("إِذْ", "idh", "noun", [MF, BD], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ، بَدَلُ اشْتِمَالٍ.", "«when» — a badal of inclusion.", "«hani»"),
  mazi("نَادَى", "nada", "«he called»", "«seslendi»", tags=["naqis-verbs", "form-iii-verbs", MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  noun_pron("رَبَّهُ", "rabb", "رَبَّ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his Lord»", "«Rabbine»", tags=[MB, ID]),
  tok("أَنِّي", "anna", "part", [IW], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِبَاءٍ مُقَدَّرَةٍ (بِأَنِّي).", "«that I» — anna with the yāʾ; the clause after an understood bāʾ.", "«… diye» — enne; yâ ismi; mukadder bâ ile mecrûr.", segments=[seg("أَنِّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("مَسَّنِيَ", "massa", "verb", [IW, MB, "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«has touched me» — the nūn of protection; the yāʾ the object; the clause is anna's khabar.", "«bana dokundu» — vikâye nûnu; yâ mef'ûl; cümle enne'nin haberi.", segments=[seg("مَسَّ", "massa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("يَ", "pron-1s", "pron")]),
  fail("الضُّرُّ", "durr", "«harm»", "«zarar»"),
  tok("وَأَنْتَ", "anta", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ (أَوْ لِلْحَالِ)، وَأَنْتَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and You» — the mubtadaʾ.", "«ve sen» — mübtedâ.", segments=wa_("أَنْتَ", "anta", "pron")),
  tok("أَرْحَمُ", "arham", "noun", [MK, ID, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«the most merciful [of]» — the khabar; an elative annexed.", "«en merhametlisi» — haber; ism-i tafdîl, muzâf."),
  tok("الرَّاحِمِينَ", "rahim-active", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«of the merciful»", "«merhametlilerin»", punct="."),
  ]),
])
sen("s11", "«So We answered him and removed what was upon him of harm, and We gave him his family and the like of them with them — a mercy from Us and a reminder for the worshippers» (21:84).",
        "«Biz de ona icabet ettik; ondaki zararı giderdik; ona ailesini ve onlarla beraber bir mislini daha verdik — katımızdan bir rahmet ve kulluk edenlere bir hatırlatma olarak» (21:84).", [
  *quran([
  tok("فَاسْتَجَبْنَا", "istajaba", "verb", [AT, "hollow-verbs", "form-x-verbs"], "الْفَاءُ عَاطِفَةٌ، وَاسْتَجَبْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ — أَجْوَفُ حُذِفَتْ أَلِفُهُ.", "«so We answered» — nā the doer; the hollow's alif drops.", "«biz de icabet ettik» — nâ fâil; ecvefin elifi düşmüş.", segments=[seg("فَ", "fa", "conj"), seg("اسْتَجَبْ", "istajaba", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«him»", "«ona»"),
  tok("فَكَشَفْنَا", "kashafa", "verb", [AT, MB], "الْفَاءُ عَاطِفَةٌ، وَكَشَفْ فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ.", "«and removed»", "«ve giderdik»", segments=[seg("فَ", "fa", "conj"), seg("كَشَفْ", "kashafa", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the object.", "«… -ı» — mef'ûl."),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«was upon him» — the ṣila.", "«ondaki» — sıla.", tags=[MW]),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  majrur("ضُرٍّ", "durr", "«harm»", "«zarar»"),
  tok("وَآتَيْنَاهُ", "aataa", "verb", [AT, MX, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَآتَيْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and We gave him»", "«ve ona verdik»", segments=[seg("وَ", "wa", "conj"), seg("آتَيْ", "aataa", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  noun_pron("أَهْلَهُ", "ahl", "أَهْلَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his family» — the second object.", "«ailesini» — ikinci mef'ûl.", tags=[MB, MX, ID]),
  noun_pron("وَمِثْلَهُمْ", "mithl", "وَمِثْلَ", "هُمْ", "pron-3mp", "الْوَاوُ عَاطِفَةٌ، وَمِثْلَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«and the like of them»", "«ve bir mislini»", tags=[AT, ID]),
  prep_pron("مَعَهُمْ", "maa", "هُمْ", "pron-3mp", "«with them»", "«onlarla beraber»", extra_ar=" — مَعَ ظَرْفٌ مُضَافٌ"),
  tok("رَحْمَةً", "rahma", "noun", ["maful-lah"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a mercy» — the object of purpose.", "«bir rahmet olarak» — mef'ûlün leh."),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("عِنْدِنَا", "inda", "عِنْدِ", "نَا", "pron-1p", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«Us»", "«katımızdan»", tags=[HJ, ID]),
  tok("وَذِكْرَى", "dhikra", "noun", [AT, "maful-lah", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَذِكْرَى مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«and a reminder» — joined; a maqṣūr.", "«ve bir hatırlatma» — ma'tûf; maksûr.", segments=wa_("ذِكْرَى", "dhikra", "noun")),
  tok("لِلْعَابِدِينَ", "abid", "noun", [HJ, JS, "ism-fail"], "اللَّامُ حَرْفُ جَرٍّ، وَالْعَابِدِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«for the worshippers»", "«kulluk edenlere»", punct=".", segments=[seg("لِ", "li", "prep"), seg("الْعَابِدِينَ", "abid", "noun")]),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: afa-loathe, azza-mighty, hana-tender, khadama-serve, rahim-active, rida-contentment, salim-sound take suffixed keys; qada = قَضَاء reused)
CAND = {
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "ayyub": G("ayyub", "أَيُّوب", None, "propn", "Ayyūb (Job)", "Eyyûb", 1),
 "quran": G("quran", "قُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "namat": G("namat", "نَمَط", "ن م ط", "noun", "a kind, a type, a pattern", "tür, tarz, nemat", 3),
 "akhar": G("akhar", "آخَر", "أ خ ر", "noun", "another, other (a diptote)", "başka, diğer (gayr-i munsarıf)", 1),
 "qasas": G("qasas", "قَصَص", "ق ص ص", "noun", "stories", "kıssalar", 2),
 "mazhar": G("mazhar", "مَظْهَر", "ظ ه ر", "noun", "a manifestation", "tecelli, mazhar", 2, plural="مَظَاهِر"),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a favour", "nimet", 1, plural="نِعَم"),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant", "kul", 1, plural="عِبَاد"),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer", "mümin", 1),
 "sabir": G("sabir", "صَابِر", "ص ب ر", "noun", "patient (an active participle)", "sabreden (ism-i fâil)", 1),
 "shakir": G("shakir", "شَاكِر", "ش ك ر", "noun", "thankful", "şükreden", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "mahbub": G("mahbub", "مَحْبُوب", "ح ب ب", "noun", "beloved (a passive participle)", "sevgili, mahbûb (ism-i mef'ûl)", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "dabba": G("dabba", "دَابَّة", "د ب ب", "noun", "a beast, a creeping creature", "hayvan, canlı; haşere", 2, plural="دَوَابّ"),
 "anam": G("anam", "أَنْعَام", "ن ع م", "noun", "cattle, livestock", "davar, hayvanlar (en'âm)", 2),
 "harth": G("harth", "حَرْث", "ح ر ث", "noun", "tillage, crops", "ekin", 2),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "much, many", "çok", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child", "evlât, çocuk", 1, plural="أَوْلَاد"),
 "mardi": G("mardi", "مَرْضِيّ", "ر ض و", "noun", "pleasing, well-pleasing (a passive participle)", "hoş, razı olunan (ism-i mef'ûl)", 3),
 "ibtala": G("ibtala", "اِبْتَلَى", "ب ل و", "verb", "to try, to test (Form VIII, defective)", "sınamak, imtihan etmek (iftiâl, nâkıs)", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all", "hepsi", 1),
 "dhahaba": G("dhahaba", "ذَهَبَ", "ذ ه ب", "verb", "to go", "gitmek", 1),
 "akhir": G("akhir", "آخِر", "أ خ ر", "noun", "the last, the end", "son, sonuncu", 1),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "jasad": G("jasad", "جَسَد", "ج س د", "noun", "a body", "beden, ceset", 1),
 "baqiya": G("baqiya", "بَقِيَ", "ب ق ي", "verb", "to stay, to remain", "kalmak", 1),
 "salim-sound": G("salim-sound", "سَلِيم", "س ل م", "noun", "sound, unharmed", "sağlam, salim", 2),
 "siwa": G("siwa", "سِوَى", "س و ي", "noun", "other than, but — the exceptive noun", "… -den başka — istisnâ ismi", 2),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "the heart", "kalp", 1),
 "lisan": G("lisan", "لِسَان", "ل س ن", "noun", "the tongue", "dil", 1),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to remember, to mention", "zikretmek, anmak", 1),
 "pron-3d": G("pron-3d", "هُمَا", None, "pron", "they two / them two", "o ikisi", 1),
 "azza-mighty": G("azza-mighty", "عَزَّ", "ع ز ز", "verb", "to be mighty — عَزَّ وَجَلَّ, said of God", "aziz olmak — azze ve celle", 1),
 "jalla": G("jalla", "جَلَّ", "ج ل ل", "verb", "to be majestic — عَزَّ وَجَلَّ", "celîl olmak — azze ve celle", 1),
 "hatta": G("hatta", "حَتَّى", None, "part", "until", "öyle ki", 1),
 "afa-loathe": G("afa-loathe", "عَافَ", "ع ي ف", "verb", "to loathe, to find disgusting (hollow)", "tiksinmek (ecvef)", 3),
 "jalis": G("jalis", "جَلِيس", "ج ل س", "noun", "a companion, one who sits with", "yanında oturan, celîs", 3),
 "afrada": G("afrada", "أَفْرَدَ", "ف ر د", "verb", "to set apart, to isolate (Form IV)", "ayırmak, tek başına bırakmak (if'âl)", 3),
 "nahiya": G("nahiya", "نَاحِيَة", "ن ح و", "noun", "a side, a corner, a district", "taraf, köşe, nahiye", 2),
 "balad": G("balad", "بَلَد", "ب ل د", "noun", "a town, a country", "şehir, belde", 1),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "anyone, one", "kimse, biri", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "hana-tender": G("hana-tender", "حَنَا", "ح ن و", "verb", "to be tender, to bend over with compassion (with ʿalā)", "şefkat göstermek, üstüne eğilmek (alâ ile)", 3),
 "zawja": G("zawja", "زَوْجَة", "ز و ج", "noun", "a wife", "karısı, zevce", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "who (feminine)", "… olan", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to stand; to look after (with bi-amri)", "kalkmak; (işini) görmek", 1),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "affairs, a matter", "iş", 1),
 "ihtaja": G("ihtaja", "اِحْتَاجَ", "ح و ج", "verb", "to be in need (Form VIII, hollow)", "muhtaç olmak (iftiâl, ecvef)", 2),
 "aydan": G("aydan", "أَيْضًا", "أ ي ض", "noun", "also, too", "de, da; ayrıca", 1),
 "sara": G("sara", "صَارَ", "ص ي ر", "verb", "to become (a sister of kāna)", "olmak, … hâle gelmek (kâne'nin kardeşi)", 1),
 "khadama-serve": G("khadama-serve", "خَدَمَ", "خ د م", "verb", "to serve", "hizmet etmek", 1),
 "ajl": G("ajl", "أَجْل", "أ ج ل", "noun", "sake — مِنْ أَجْلِ: for the sake of", "uğur — min ecli: uğruna", 1),
 "raghma": G("raghma", "رَغْمَ", "ر غ م", "noun", "despite", "rağmen", 2),
 "lahija": G("lahija", "لَهِجَ", "ل ه ج", "verb", "to be ever busy with, devoted to (with bi)", "dilinden düşürmemek, düşkün olmak (bi ile)", 3),
 "dhikr": G("dhikr", "ذِكْر", "ذ ك ر", "noun", "remembrance", "zikir", 1),
 "shukr": G("shukr", "شُكْر", "ش ك ر", "noun", "thanks", "şükür", 1),
 "shaka": G("shaka", "شَكَا", "ش ك و", "verb", "to complain", "şikâyet etmek", 1),
 "taattaba": G("taattaba", "تَعَتَّبَ", "ع ت ب", "verb", "to reproach, to find fault (Form V)", "sitem etmek (tefa''ul)", 3),
 "tadhammara": G("tadhammara", "تَذَمَّرَ", "ذ م ر", "verb", "to grumble (Form V)", "söylenmek, homurdanmak (tefa''ul)", 3),
 "ghadiba": G("ghadiba", "غَضِبَ", "غ ض ب", "verb", "to be angry", "öfkelenmek", 1),
 "dama": G("dama", "دَامَ", "د و م", "verb", "to last, to go on (hollow)", "sürmek, devam etmek (ecvef)", 2),
 "sana": G("sana", "سَنَة", "س ن و", "noun", "a year", "yıl", 1, plural="سِنُونَ / سَنَوَات"),
 "tiwal": G("tiwal", "طِوَال", "ط و ل", "noun", "long (the plural of طَوِيل)", "uzun (tavîl'in çoğulu)", 2),
 "mulqa": G("mulqa", "مُلْقًى", "ل ق ي", "noun", "cast, thrown (a maqṣūr passive participle)", "atılmış (maksûr ism-i mef'ûl)", 3),
 "kunasa": G("kunasa", "كُنَاسَة", "ك ن س", "noun", "a refuse-heap, sweepings", "çöplük, süprüntü", 3),
 "banu-israil": G("banu-israil", "بَنُو إِسْرَائِيلَ", "ب ن ي", "noun", "the Children of Israel", "İsrâiloğulları", 1),
 "israil": G("israil", "إِسْرَائِيل", None, "propn", "Israel (Yaʿqūb)", "İsrâil (Yakub)", 1),
 "ikhtalafa": G("ikhtalafa", "اِخْتَلَفَ", "خ ل ف", "verb", "to go to and fro; to differ (Form VIII)", "gidip gelmek; ihtilaf etmek (iftiâl)", 2),
 "lamma": G("lamma", "لَمَّا", None, "part", "when", "… -ınca", 2),
 "tamma": G("tamma", "تَمَّ", "ت م م", "verb", "to be complete (doubled)", "tamamlanmak (muzâaf)", 2),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to will, to intend", "dilemek, murat etmek", 1),
 "ibtila": G("ibtila", "اِبْتِلَاء", "ب ل و", "noun", "trial, testing (maṣdar of Form VIII)", "sınanma, imtihan (iftiâl masdarı)", 2),
 "takmil": G("takmil", "تَكْمِيل", "ك م ل", "noun", "perfecting, completing (maṣdar of Form II)", "kemale erdirme (tef'îl masdarı)", 3),
 "raf": G("raf", "رَفْع", "ر ف ع", "noun", "raising", "yükseltme", 1),
 "daraja": G("daraja", "دَرَجَة", "د ر ج", "noun", "a degree, a rank", "derece", 1, plural="دَرَجَات"),
 "rida-contentment": G("rida-contentment", "رِضًا", "ر ض و", "noun", "contentment, acceptance (a maqṣūr maṣdar)", "rıza (maksûr masdar)", 2),
 "qada": G("qada", "قَضَاء", "ق ض ي", "noun", "the decree", "kaza, takdir", 2),
 "alhama": G("alhama", "أَلْهَمَ", "ل ه م", "verb", "to inspire (Form IV; two objects)", "ilham etmek (if'âl; iki mef'ûl)", 2),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "a prayer", "dua", 1),
 "mustajab": G("mustajab", "مُسْتَجَاب", "ج و ب", "noun", "answered (the passive participle of Form X)", "kabul edilen (istif'âl ism-i mef'ûlü)", 3),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "which", "… -ği", 1),
 "tajalla": G("tajalla", "تَجَلَّى", "ج ل و", "verb", "to show", "ortaya çıkmak", 3),
 "ajz": G("ajz", "عَجْز", "ع ج ز", "noun", "helplessness, inability", "acz", 2),
 "bus": G("bus", "بُؤْس", "ب أ س", "noun", "misery, wretchedness", "çaresizlik, sefalet", 3),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that", "… -ması", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "malja": G("malja", "مَلْجَأ", "ل ج أ", "noun", "a refuge", "sığınak, melce'", 3),
 "illa": G("illa", "إِلَّا", None, "part", "except, but", "… -den başka", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that", "… olduğu", 1),
 "qadir": G("qadir", "قَادِر", "ق د ر", "noun", "able, powerful (an active participle)", "kadir, gücü yeten (ism-i fâil)", 1),
 "afa-heal": G("afa-heal", "عَافَى", "ع ف و", "verb", "to heal, to grant health (Form III, defective)", "iyileştirmek, âfiyet vermek (müfâale, nâkıs)", 2),
 "badan": G("badan", "بَدَن", "ب د ن", "noun", "the body", "beden", 1),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "family", "aile", 1),
 "radda": G("radda", "رَدَّ", "ر د د", "verb", "to restore, to return (doubled)", "geri vermek (muzâaf)", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "wealth", "mal", 1),
 "baraka-bless": G("baraka-bless", "بَارَكَ", "ب ر ك", "verb", "to bless", "bereket vermek", 2),
 "dif": G("dif", "ضِعْف", "ض ع ف", "noun", "a double, a multiple", "kat, misil", 2, plural="أَضْعَاف"),
 "mudaaf": G("mudaaf", "مُضَاعَف", "ض ع ف", "noun", "multiplied, doubled (a passive participle of Form III)", "katlanmış, kat kat (müfâale ism-i mef'ûlü)", 2),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "tabaraka": G("tabaraka", "تَبَارَكَ", "ب ر ك", "verb", "to be blessed — تَبَارَكَ وَتَعَالَى, said of God", "mübarek olmak — tebâreke ve teâlâ", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "He is exalted", "yücedir", 1),
 "idh": G("idh", "إِذْ", None, "noun", "when", "hani", 1),
 "nada": G("nada", "نَادَى", "ن د و", "verb", "to call (Form III, defective)", "seslenmek (müfâale, nâkıs)", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "massa": G("massa", "مَسَّ", "م س س", "verb", "to touch (doubled)", "dokunmak (muzâaf)", 1),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection", "vikâye nûnu", 2),
 "durr": G("durr", "ضُرّ", "ض ر ر", "noun", "harm, affliction", "zarar, sıkıntı", 2),
 "anta": G("anta", "أَنْتَ", None, "pron", "you", "sen", 1),
 "arham": G("arham", "أَرْحَم", "ر ح م", "noun", "most merciful (an elative)", "en merhametli (ism-i tafdîl)", 1),
 "rahim-active": G("rahim-active", "رَاحِم", "ر ح م", "noun", "merciful (an active participle)", "merhamet eden (ism-i fâil)", 1),
 "istajaba": G("istajaba", "اِسْتَجَابَ", "ج و ب", "verb", "to answer (a prayer) (Form X, hollow)", "icabet etmek, kabul etmek (istif'âl, ecvef)", 2),
 "kashafa": G("kashafa", "كَشَفَ", "ك ش ف", "verb", "to remove, to uncover", "gidermek, açmak", 1),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give", "vermek", 2),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "the like of", "misil, benzer", 1),
 "maa": G("maa", "مَعَ", None, "noun", "with", "ile", 1),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "with, at", "katında", 1),
 "dhikra": G("dhikra", "ذِكْرَى", "ذ ك ر", "noun", "a reminder (a maqṣūr noun)", "hatırlatma, zikrâ (maksûr)", 2),
 "abid": G("abid", "عَابِد", "ع ب د", "noun", "a worshipper (an active participle)", "kulluk eden, âbid (ism-i fâil)", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ibtala", _sg.derived_naqis("مِنْ بَابِ الِافْتِعَالِ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِبْتَلَ", "بْتَل", "i", "اِبْتَل", "اِبْتِلَاء", "مُبْتَلٍ (الْمُبْتَلِي)", "مُبْتَلًى", "اُبْتُلِيَ", "يُبْتَلَى", "اِبْتَلَاهُ: اخْتَبَرَهُ وَامْتَحَنَهُ."))
put_morph(mo, "baqiya", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ يَائِيٌّ", _sg.BABS["samia"][1], "بَقَاء", "بَاقٍ (الْبَاقِي)", _sg.mazi_naqis_kasra("بَقِ", "بَقُوا"), _sg.mudari_naqis("َ", "بْق", "a"), _sg.amr_naqis("اِبْق", "a"), "يَبْقَى", "يَبْقَ", "تَبْقَ", None, None, None, "بَقِيَ يَبْقَى: دَامَ وَثَبَتَ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ؛ لَمْ يَبْقَ."))
put_morph(mo, "dhakara", _sg.sound1("nasara", "ذَكَر", "ذْكُر", "اُذْكُر", "ذِكْر", "ذَاكِر", "مَذْكُور", "ذُكِرَ", "يُذْكَرُ", "ذَكَرَ اللهَ: سَبَّحَهُ وَحَمِدَهُ؛ وَذَكَرَ الشَّيْءَ: جَرَى عَلَى لِسَانِهِ."))
put_morph(mo, "azza-mighty", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "عِزّ / عِزَّة", "عَزِيز", _sg.mazi14("عَزّ", "عَزَز"), _sg.mudari14("َ", "عِزّ", "عْزِز"), ["عِزَّ", "عِزَّا", "عِزُّوا", "عِزِّي", "عِزَّا", "اِعْزِزْنَ"], "يَعِزَّ", "يَعِزَّ", "تَعِزَّ", None, None, None, "عَزَّ: قَوِيَ وَامْتَنَعَ وَعَلَا — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ."))
put_morph(mo, "jalla", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "جَلَال", "جَلِيل", _sg.mazi14("جَلّ", "جَلَل"), _sg.mudari14("َ", "جِلّ", "جْلِل"), ["جِلَّ", "جِلَّا", "جِلُّوا", "جِلِّي", "جِلَّا", "اِجْلِلْنَ"], "يَجِلَّ", "يَجِلَّ", "تَجِلَّ", None, None, None, "جَلَّ: عَظُمَ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ."))
put_morph(mo, "afa-loathe", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "عَاف", "عِف", "عِيف", "عِف", "عِيف", "عِف", "عِيَافَة", "عَائِف", "مَعِيف", "عِيفَ", "يُعَافُ", "عَافَ الشَّيْءَ: كَرِهَهُ وَتَرَكَهُ."))
put_morph(mo, "afrada", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْرَد", "فْرِد", "أَفْرِد", "إِفْرَاد", "مُفْرِد", "مُفْرَد", "أُفْرِدَ", "يُفْرَدُ", "أَفْرَدَهُ: جَعَلَهُ وَحْدَهُ وَعَزَلَهُ."))
put_morph(mo, "hana-tender", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "حَنَ", "حْن", "u", "اُحْن", "حُنُوّ", "حَانٍ (الْحَانِي)", None, None, None, "حَنَا عَلَيْهِ يَحْنُو: عَطَفَ عَلَيْهِ — نَاقِصٌ وَاوِيٌّ؛ لَمْ يَحْنُ."))
put_morph(mo, "ihtaja", _sg.derived_hollow(_sg.B8, _sg.W8, "َ", "اِحْتَاج", "اِحْتَج", "حْتَاج", "حْتَج", "اِحْتَاج", "اِحْتَج", "اِحْتِيَاج", "مُحْتَاج", "مُحْتَاج إِلَيْهِ", None, None, "اِحْتَاجَ إِلَى الشَّيْءِ: افْتَقَرَ إِلَيْهِ."))
put_morph(mo, "sara", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "صَار", "صِر", "صِير", "صِر", "صِير", "صِر", "صَيْرُورَة", "صَائِر", None, None, None, "صَارَ الشَّيْءُ كَذَا: تَحَوَّلَ إِلَيْهِ — مِنْ أَخَوَاتِ كَانَ."))
put_morph(mo, "khadama-serve", _sg.sound1("daraba", "خَدَم", "خْدِم", "اِخْدِم", "خِدْمَة", "خَادِم", "مَخْدُوم", "خُدِمَ", "يُخْدَمُ", "خَدَمَهُ: قَامَ بِحَاجَتِهِ."))
put_morph(mo, "lahija", _sg.sound1("samia", "لَهِج", "لْهَج", "اِلْهَج", "لَهَج", "لَاهِج", None, None, None, "لَهِجَ بِالشَّيْءِ: أُولِعَ بِهِ وَثَابَرَ عَلَيْهِ."))
put_morph(mo, "shaka", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "شَكَ", "شْك", "u", "اُشْك", "شَكْوَى", "شَاكٍ (الشَّاكِي)", "مَشْكُوّ", "شُكِيَ", "يُشْكَى", "شَكَا يَشْكُو: أَظْهَرَ مَا بِهِ مِنْ أَلَمٍ — نَاقِصٌ وَاوِيٌّ؛ لَمْ يَشْكُ."))
put_morph(mo, "taattaba", _sg.derived(_sg.B5, _sg.W5, "َ", "تَعَتَّب", "تَعَتَّب", "تَعَتَّب", "تَعَتُّب", "مُتَعَتِّب", None, None, None, "تَعَتَّبَ عَلَيْهِ: لَامَهُ وَوَجَدَ عَلَيْهِ."))
put_morph(mo, "tadhammara", _sg.derived(_sg.B5, _sg.W5, "َ", "تَذَمَّر", "تَذَمَّر", "تَذَمَّر", "تَذَمُّر", "مُتَذَمِّر", None, None, None, "تَذَمَّرَ: تَكَلَّمَ بِالسُّخْطِ وَاللَّوْمِ."))
put_morph(mo, "ghadiba", _sg.sound1("samia", "غَضِب", "غْضَب", "اِغْضَب", "غَضَب", "غَاضِب (غَضْبَان)", "مَغْضُوب عَلَيْهِ", None, None, "غَضِبَ عَلَيْهِ: سَخِطَ."))
put_morph(mo, "dama", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "دَام", "دُم", "دُوم", "دُم", "دُوم", "دُم", "دَوَام", "دَائِم", None, None, None, "دَامَ الشَّيْءُ: ثَبَتَ وَبَقِيَ؛ وَمَا دَامَ: مِنْ أَخَوَاتِ كَانَ."))
put_morph(mo, "ikhtalafa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِخْتَلَف", "خْتَلِف", "اِخْتَلِف", "اِخْتِلَاف", "مُخْتَلِف", "مُخْتَلَف", "اُخْتُلِفَ", "يُخْتَلَفُ", "اِخْتَلَفَتِ الدَّوَابُّ فِي جَسَدِهِ: تَرَدَّدَتْ فِيهِ ذَاهِبَةً وَآيِبَةً؛ وَاخْتَلَفَ الْقَوْمُ: لَمْ يَتَّفِقُوا."))
put_morph(mo, "tamma", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "تَمَام", "تَامّ", _sg.mazi14("تَمّ", "تَمَم"), _sg.mudari14("َ", "تِمّ", "تْمِم"), ["تِمَّ", "تِمَّا", "تِمُّوا", "تِمِّي", "تِمَّا", "اِتْمِمْنَ"], "يَتِمَّ", "يَتِمَّ", "تَتِمَّ", None, None, None, "تَمَّ الشَّيْءُ: كَمُلَ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَتِمَّ."))
put_morph(mo, "alhama", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَلْهَم", "لْهِم", "أَلْهِم", "إِلْهَام", "مُلْهِم", "مُلْهَم", "أُلْهِمَ", "يُلْهَمُ", "أَلْهَمَهُ اللهُ الشَّيْءَ: أَلْقَاهُ فِي رُوعِهِ."))
put_morph(mo, "afa-heal", _sg.derived_naqis("مِنْ بَابِ الْمُفَاعَلَةِ", "فَاعَلَ يُفَاعِلُ", "ُ", "عَافَ", "عَاف", "i", "عَاف", "مُعَافَاة", "مُعَافٍ (الْمُعَافِي)", "مُعَافًى", "عُوفِيَ", "يُعَافَى", "عَافَاهُ اللهُ: وَهَبَهُ الْعَافِيَةَ وَشَفَاهُ."))
put_morph(mo, "radda", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "رَدّ", "رَادّ", _sg.mazi14("رَدّ", "رَدَد"), _sg.mudari14("َ", "رُدّ", "رْدُد"), ["رُدَّ", "رُدَّا", "رُدُّوا", "رُدِّي", "رُدَّا", "اُرْدُدْنَ"], "يَرُدَّ", "يَرُدَّ", "تَرُدَّ", "مَرْدُود", "رُدَّ", "يُرَدُّ", "رَدَّ الشَّيْءَ: أَرْجَعَهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَرُدَّ."))
put_morph(mo, "tabaraka", _sg.derived(_sg.B6, _sg.W6, "َ", "تَبَارَك", "تَبَارَك", "تَبَارَك", "تَبَارُك", "مُتَبَارِك", None, None, None, "تَبَارَكَ اللهُ: تَعَاظَمَ وَتَقَدَّسَ — لَا يُقَالُ إِلَّا لِلهِ."))
put_morph(mo, "nada", _sg.derived_naqis("مِنْ بَابِ الْمُفَاعَلَةِ", "فَاعَلَ يُفَاعِلُ", "ُ", "نَادَ", "نَاد", "i", "نَاد", "نِدَاء / مُنَادَاة", "مُنَادٍ (الْمُنَادِي)", "مُنَادًى", "نُودِيَ", "يُنَادَى", "نَادَاهُ: دَعَاهُ بِرَفْعِ الصَّوْتِ."))
put_morph(mo, "massa", _sg.entry("مِنْ بَابِ سَمِعَ يَسْمَعُ — مُضَاعَفٌ", "فَعِلَ يَفْعَلُ", "مَسّ", "مَاسّ", _sg.mazi14("مَسّ", "مَسِس"), _sg.mudari14("َ", "مَسّ", "مْسَس"), ["مَسَّ", "مَسَّا", "مَسُّوا", "مَسِّي", "مَسَّا", "اِمْسَسْنَ"], "يَمَسَّ", "يَمَسَّ", "تَمَسَّ", "مَمْسُوس", "مُسَّ", "يُمَسُّ", "مَسَّهُ الضُّرُّ: أَصَابَهُ — مُضَاعَفٌ مِنْ بَابِ سَمِعَ: مَسِسْتُ، يَمْسَسْنَ."))
put_morph(mo, "istajaba", _sg.derived_hollow(_sg.B10, _sg.W10, "َ", "اِسْتَجَاب", "اِسْتَجَب", "سْتَجِيب", "سْتَجِب", "اِسْتَجِيب", "اِسْتَجِب", "اِسْتِجَابَة", "مُسْتَجِيب", "مُسْتَجَاب", "اُسْتُجِيبَ", "يُسْتَجَابُ", "اِسْتَجَابَ لَهُ: أَجَابَهُ وَقَبِلَ دُعَاءَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch17 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 17 (print pp. 26–28; the story of Ayyūb and Yūnus opens): a different kind of story — Ayyūb's wealth and its loss (s1–s4); his patience (s5–s6); trial and gift, with 21:83–84 (s7–s11)."
ADD_TR = " On yedinci bölüm (baskı s. 26–28; Eyyûb ve Yûnus kıssası açılır): başka bir tür kıssa — Eyyûb'un serveti ve kaybı (s1–s4); sabrı (s5–s6); mihnet ve lütuf, 21:83–84 ile (s7–s11)."
write_out(17, S, TITLE, ADD_EN, ADD_TR, "Ayyūb and Yūnus §1–3", GLOSS_ADD, notes=(), related=())
report(17, S, GLOSS_ADD, ())
