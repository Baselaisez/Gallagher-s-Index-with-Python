# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 10: «الْمَلِكَةُ تَسْتَشِيرُ أَرْكَانَ دَوْلَتِهَا» — §9 (the queen consults her council),
§10 (a bargaining gift) and the opening of §11 (the queen comes submissive); print pp. 18–20.
One word of print p. 18 (after حَازِمًا, illegible in the scan) is left out — declared in the chapter blurb.
python3 tools/authoring/author_qisas4_ch10.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْمَلِكَةُ تَسْتَشِيرُ أَرْكَانَ دَوْلَتِهَا", "en": "The queen consults the pillars of her state", "tr": "Kraliçe devletinin erkânına danışır"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; ML = "maful-lah"
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
def v_ta_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, fa=False, extra=""):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", en + " — a feminine māḍī; the pronoun is its object.", tr + " — müennes mâzî; zamir mef'ûl.", punct=punct, segments=segs)

# ---------------------------------------------------------------- §9 الْمَلِكَةُ تَسْتَشِيرُ أَرْكَانَ دَوْلَتِهَا (print p. 18)
sen("s1", "Sulaymān was resolute; and the woman who ruled this land was intelligent, not hasty in judgment;",
        "Süleyman kararlıydı; bu ülkeyi yöneten kadın ise akıllı, hükümde aceleci olmayan biriydi;", [
  tok("فَقَدْ", "qad", "part", ["qad-harf"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«indeed» — qad.", "«gerçekten» — kad.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«was» — kāna.", "«idi» — kâne."),
  tok("سُلَيْمَانُ", "sulayman", "propn", [KN, MM], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — kāna's ism; a diptote.", "«Süleyman» — kâne'nin ismi; gayr-i munsarıf."),
  tok("حَازِمًا", "hazim", "noun", [KN, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«resolute» — kāna's khabar.", "«kararlı» — kâne'nin haberi.", punct="،"),
  tok("وَكَانَتِ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and … was» — kāna with the feminine tāʾ, kasra for the two sukūns.", "«ve … idi» — te'nis tâ'sı; iki sâkin için kesre.", segments=wa_("كَانَتِ", "kana", "verb")),
  tok("الْمَرْأَةُ", "mara-woman", "noun", [KN], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the woman» — kāna's ism.", "«kadın» — kâne'nin ismi."),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلْمَرْأَةِ.", "«who» — a naʿt of the woman.", "«… -en» — kadının sıfatı."),
  mudari("تَحْكُمُ", "hakama", "«ruled»", "«yönetir»", tags=[MW, MB], hidden="هِيَ", extra_ar=" — صِلَةٌ"),
  tok("هٰذِهِ", "hadhihi", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this» — the object.", "«bu» — mef'ûl."),
  tok("الْبِلَادَ", "bilad", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«land» — the badal.", "«ülkeyi» — bedel."),
  tok("عَاقِلَةً", "aqil", "noun", [KN, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«intelligent» — kāna's khabar.", "«akıllı» — kâne'nin haberi."),
  tok("غَيْرَ", "ghayr", "noun", [NA, ID], "نَعْتٌ مَنْصُوبٌ (أَوْ خَبَرٌ ثَانٍ)، مُضَافٌ.", "«not» (lit. other than) — a naʿt, annexed.", "«olmayan» — sıfat, muzâf."),
  mudaf_ilayh("مُتَسَرِّعَةٍ", "mutasarri", "«hasty»", "«aceleci»", tags=["ism-fail", "form-v-verbs"]),
  fi(), majrur("الْحُكْمِ", "hukm", "«judgment»", "«hükümde»", tags=["masdar"], punct="،"),
])
sen("s2", "she had wide experience from the lives of kings and the histories of conquerors; only her mind had failed her in knowing God and worshipping Him,",
        "hükümdarların hayatlarından ve fatihlerin haberlerinden geniş tecrübeleri vardı; aklı ancak Allah'ı tanımada ve O'na kullukta ona ihanet etmişti,", [
  noun_pron("عِنْدَهَا", "inda", "عِنْدَ", "هَا", "pron-3fs", "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«she had» (lit. with her) — a fronted khabar.", "«onun … vardı» — öne alınmış haber.", tags=[MF, ID, MK]),
  tok("تَجَارِبُ", "tajriba", "noun", [MK, JT, MM], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«experience» — the delayed mubtadaʾ; a diptote plural.", "«tecrübeler» — mübtedâ; gayr-i munsarıf."),
  naat("وَاسِعَةٌ", "wasi-wide", "«wide»", "«geniş»", case="raf", tags=["ism-fail"]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("سِيَرِ", "sira", "«the lives»", "«hayatlarından»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("الْمُلُوكِ", "malik-king", "«of kings»", "«hükümdarların»", tags=[JT]),
  atf("وَأَخْبَارِ", "khabar", "«the histories»", "«haberlerinden»", "jarr", tags=[ID, JT]),
  tok("الْفَاتِحِينَ", "fatih", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«of conquerors» — jarr by the yāʾ.", "«fatihlerin» — yâ ile mecrûr.", punct="،"),
  tok("وَإِنَّمَا", "innama", "part", [AT, "innama-kaffa"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّمَا أَدَاةُ حَصْرٍ (إِنَّ الْمَكْفُوفَةُ بِمَا).", "«only» — innamā, inna restrained by mā.", "«ancak» — innemâ, mâ ile kâffe olmuş inne.", segments=wa_("إِنَّمَا", "innama", "part")),
  tok("خَانَهَا", "khana", "verb", [MB, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ.", "«had failed her» — hā the object.", "«ona ihanet etti» — hâ mef'ûl.", segments=[seg("خَانَ", "khana", "verb"), seg("هَا", "pron-3fs", "pron")]),
  noun_pron("عَقْلُهَا", "aql", "عَقْلُ", "هَا", "pron-3fs", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her mind» — the doer.", "«aklı» — fâil.", tags=[FL, ID]),
  fi(), majrur("مَعْرِفَةِ", "marifa", "«knowing»", "«tanımada»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("الْإِلٰهِ", "ilah", "«God»", "«ilâhı»"),
  noun_pron("وَعِبَادَتِهِ", "ibada", "وَعِبَادَتِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَعِبَادَتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and worshipping Him»", "«ve O'na kullukta»", punct="،", tags=[AT, ID, "masdar"]),
])
sen("s3", "so the zeal of kings did not seize her, nor did she act alone on her opinion; she showed the men of counsel among the pillars of her state this letter, which was not like other letters:",
        "bu yüzden hükümdar gayreti onu ele geçirmedi, görüşünde tek başına davranmadı; devletinin erkânından görüş sahiplerine, öteki mektuplar gibi olmayan bu mektubu gösterdi:", [
  tok("فَلَمْ", "lam-jazima", "part", [AT, LJ], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«so … not» — lam.", "«bu yüzden … -medi» — lem.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("تَأْخُذْهَا", "akhadha", "verb", [LJ, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَهَا مَفْعُولٌ بِهِ.", "«seize her» — jazm by lam; hā the object.", "«onu ele geçirdi» — lem ile meczum; hâ mef'ûl.", segments=[seg("تَأْخُذْ", "akhadha", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("حَمِيَّةُ", "hamiyya", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the zeal» — the doer, annexed.", "«gayreti» — fâil, muzâf."),
  mudaf_ilayh("الْمُلُوكِ", "malik-king", "«of kings»", "«hükümdarların»", tags=[JT], punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«nor»", "«ve … -medi»", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("تَسْتَبِدَّ", "istabadda", "verb", [LJ, "doubled-verbs", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، حُرِّكَ بِالْفَتْحِ لِلتَّخَلُّصِ مِنَ الْتِقَاءِ السَّاكِنَيْنِ (مُضَاعَفٌ)، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«act alone» — a doubled verb in jazm: fatḥa stands in for the sukūn.", "«tek başına davrandı» — muzâaf fiil, meczum: sükûn yerine fetha."),
  tok("بِالرَّأْيِ", "ray", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالرَّأْيِ مَجْرُورٌ.", "«on [her] opinion»", "«görüşünde»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الرَّأْيِ", "ray", "noun")]),
  mazi_ta("فَأَطْلَعَتْ", "atlaa", "«she showed»", "«gösterdi»", tags=[AT, MX, "form-iv-verbs"]),
  tok("أَهْلَ", "ahl", "noun", [MB, MX, ID], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ، مُضَافٌ.", "«the men [of]» — the first object, annexed.", "«ehlini» — ilk mef'ûl, muzâf."),
  mudaf_ilayh("الرَّأْيِ", "ray", "«of counsel»", "«görüş»"),
  prep("مِنْ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  majrur("أَرْكَانِ", "rukn", "«the pillars»", "«erkânından»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  noun_pron("دَوْلَتِهَا", "dawla", "دَوْلَتِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of her state»", "«devletinin»", tags=[ID]),
  prep("عَلَى", "ala", "«(showed) … this»", "«-i»", ar="حَرْفُ جَرٍّ — الْمَفْعُولُ الثَّانِي لِأَطْلَعَ يَتَعَدَّى بِعَلَى."),
  tok("هٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«this»", "«bu»"),
  tok("الْكِتَابِ", "kitab", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«letter» — the badal.", "«mektubu» — bedel."),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلْكِتَابِ.", "«which» — a naʿt of the letter.", "«… olan» — mektubun sıfatı."),
  tok("لَمْ", "lam-jazima", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-medi»"),
  tok("يَكُنْ", "kana", "verb", [LJ, KN, MW, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«was» — kāna in jazm; its wāw drops before the sukūn.", "«idi» — kâne, meczum; vâvı iki sâkin yüzünden düşmüş."),
  tok("كَسَائِرِ", "sair-rest", "noun", [HJ, ID, KN], "الْكَافُ حَرْفُ جَرٍّ، وَسَائِرِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُنْ.", "«like the rest» — the jarr phrase is kāna's khabar.", "«öteki … gibi» — câr-mecrûr kâne'nin haberi.", segments=[seg("كَ", "ka", "prep"), seg("سَائِرِ", "sair-rest", "noun")]),
  mudaf_ilayh("الْكُتُبِ", "kitab", "«of letters»", "«mektupların»", tags=[JT], punct="،"),
])
sen("s4", "it was a letter from the greatest of the kings of her time and from a prophet calling to God.",
        "o, zamanının en büyük hükümdarından ve Allah'a çağıran bir peygamberden gelen bir mektuptu.", [
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«it is indeed» — inna with the hāʾ as its ism.", "«şüphesiz o» — inne; hâ ismi.", segments=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  khabar_inna("كِتَابٌ", "kitab", "«a letter»", "«bir mektup»"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("أَعْظَمِ", "azam", "«the greatest»", "«en büyüğünden»", tags=[ID, "ism-tafdil", MM], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ — اسْمُ تَفْضِيلٍ."),
  mudaf_ilayh("الْمُلُوكِ", "malik-king", "«of the kings»", "«hükümdarların»", tags=[JT]),
  fi(), noun_pron("زَمَانِهَا", "zaman", "زَمَانِ", "هَا", "pron-3fs", "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her time»", "«zamanının»", tags=[HJ, ID]),
  tok("وَمِنْ", "min", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ.", "«and from»", "«ve … -den»", segments=wa_("مِنْ", "min", "prep")),
  majrur("نَبِيٍّ", "nabi", "«a prophet»", "«bir peygamber»"),
  tok("دَاعٍ", "dain", "noun", [NA, "ism-maqsur-manqus", "ism-fail"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ.", "«calling» — a naʿt; a manqūṣ whose yāʾ drops, the kasra estimated.", "«çağıran» — sıfat; mankûs, yâ'sı düşmüş, kesre takdîrî."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'a»", punct="."),
])
sen("s5", "And when the pillars of her state began to boast of their strength and the multitude of their armies, to please and to flatter — as the courtiers of kings and rulers do in every time and place — she did not accept their speech, nor did she agree with them on it;",
        "Devletinin erkânı, hoşnut etmek ve yaranmak için — her zaman ve mekânda hükümdarların ve yöneticilerin yanındakilerin hâli olduğu üzere — güçleriyle ve ordularının çokluğuyla övünmeye başlayınca, onların sözünü kabul etmedi ve bu konuda onlara uymadı;", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF, SH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — lammā, the conditional ẓarf.", "«ve … -ınca» — şart anlamlı zarf lemmâ.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("بَدَأَ", "badaa", "«began»", "«başladı»", tags=[SH], hidden=None),
  tok("أَرْكَانُ", "rukn", "noun", [FL, ID, JT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the pillars» — the doer.", "«erkânı» — fâil."),
  noun_pron("دَوْلَتِهَا", "dawla", "دَوْلَتِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of her state»", "«devletinin»", tags=[ID]),
  khamsa("يُدِلُّونَ", "adalla-boast", "«to boast»", "«övünmeye»", tags=[HL, "doubled-verbs", "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ بَدَأَ (أَوْ حَالٌ)"),
  noun_pron("بِقُوَّتِهِمْ", "quwwa", "بِقُوَّتِ", "هِمْ", "pron-3mp", "الْبَاءُ حَرْفُ جَرٍّ، وَقُوَّتِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«of their strength»", "«güçleriyle»", tags=[HJ, ID]),
  atf("وَكَثْرَةِ", "kathra", "«the multitude»", "«çokluğuyla»", "jarr", tags=[ID]),
  noun_pron("جُيُوشِهِمْ", "jaysh", "جُيُوشِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«of their armies»", "«ordularının»", tags=[ID, JT]),
  tok("إِرْضَاءً", "irda", "noun", [ML, "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«to please» — the object of purpose.", "«hoşnut etmek için» — mef'ûlün leh."),
  tok("وَتَمَلُّقًا", "tamalluq", "noun", [AT, ML, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَتَمَلُّقًا مَعْطُوفٌ مَنْصُوبٌ.", "«and to flatter»", "«ve yaranmak için»", segments=wa_("تَمَلُّقًا", "tamalluq", "noun")),
  tok("شَأْنَ", "shan", "noun", [ID, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (يَفْعَلُونَ شَأْنَ …) مَنْصُوبٌ، مُضَافٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«as … do» (lit. the manner of) — an absolute object of an understood verb; a parenthesis.", "«… hâli üzere» — mukadder fiilin mef'ûl-i mutlakı; mu'teriza."),
  mudaf_ilayh("جُلَسَاءِ", "jalis", "«the courtiers»", "«yanındakilerin»", tags=[ID, JT], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْمُلُوكِ", "malik-king", "«of kings»", "«hükümdarların»", tags=[JT]),
  atf("وَالْحُكَّامِ", "hakim-ruler", "«rulers»", "«yöneticilerin»", "jarr", tags=[JT]),
  fi(), majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("زَمَانٍ", "zaman", "«time»", "«zaman»"),
  atf("وَمَكَانٍ", "makan", "«place»", "«mekân»", "jarr"),
  tok("لَمْ", "lam-jazima", "part", [LJ, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — وَالْجُمْلَةُ جَوَابُ لَمَّا.", "«not» — lam; the clause is the answer of lammā.", "«-medi» — lem; cümle lemmâ'nın cevabı."),
  tok("تَقْبَلْ", "qabila", "verb", [LJ, SH, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«accept» — jazm by lam.", "«kabul etmedi» — lem ile meczum."),
  noun_pron("مَقَالَتَهُمْ", "maqala", "مَقَالَتَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their speech»", "«sözlerini»", tags=[MB, ID]),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«nor»", "«ve … -medi»", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("تُوَافِقْهُمْ", "wafaqa", "verb", [LJ, MB, "form-iii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَهُمْ مَفْعُولٌ بِهِ.", "«agree with them» — hum the object.", "«onlara uymadı» — hüm mef'ûl.", segments=[seg("تُوَافِقْ", "wafaqa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep_pron("عَلَيْهَا", "ala", "هَا", "pron-3fs", "«on it»", "«bu konuda»", punct="،"),
])
sen("s6", "rather, she warned them of the evil end and reminded them of the ways of conquering kings among the conquered nations and their fate after defeat and collapse, and said: Such will be the lot of our country and our nation;",
        "aksine onları kötü akıbete karşı uyardı; fatih hükümdarların fethedilen ümmetlerdeki tutumunu ve bu ümmetlerin yenilgi ve çöküşten sonraki akıbetini hatırlattı ve dedi ki: Ülkemizin ve ümmetimizin hâli de böyle olacak;", [
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ.", "«rather» — bal.", "«aksine» — idrâb harfi."),
  v_ta_pron("حَذَّرَتْهُمْ", "hadhdhara", "حَذَّرَتْ", "هُمْ", "pron-3mp", "«she warned them»", "«onları uyardı»", tags=["form-ii-verbs"]),
  prep("مِنْ", "min", "«of»", "«-e karşı»"),
  majrur("سُوءِ", "su", "«the evil»", "«kötü»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("الْعَاقِبَةِ", "aqiba", "«end»", "«akıbete»", punct="،"),
  v_ta_pron("وَذَكَّرَتْهُمْ", "dhakkara", "ذَكَّرَتْ", "هُمْ", "pron-3mp", "«and reminded them»", "«ve onlara hatırlattı»", tags=["form-ii-verbs"], wa=True),
  tok("بِسِيرَةِ", "sira", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَسِيرَةِ مَجْرُورٌ، مُضَافٌ.", "«of the ways»", "«tutumunu»", segments=[seg("بِ", "bi", "prep"), seg("سِيرَةِ", "sira", "noun")]),
  mudaf_ilayh("الْمُلُوكِ", "malik-king", "«of kings»", "«hükümdarların»", tags=[JT]),
  tok("الْفَاتِحِينَ", "fatih", "noun", [NA, JS, "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«conquering» — the naʿt, jarr by the yāʾ.", "«fatih» — sıfat, yâ ile mecrûr."),
  fi(), majrur("الْأُمَمِ", "umma", "«the nations»", "«ümmetlerdeki»", tags=[JT]),
  naat("الْمَفْتُوحَةِ", "maftuh", "«conquered»", "«fethedilen»", tags=["ism-maful"]),
  noun_pron("وَمَصِيرِهَا", "masir-fate", "وَمَصِيرِ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَمَصِيرِ مَعْطُوفٌ عَلَى سِيرَةِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their fate»", "«ve akıbetini»", tags=[AT, ID]),
  tok("بَعْدَ", "bada", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  mudaf_ilayh("الْهَزِيمَةِ", "hazima", "«defeat»", "«yenilgi»"),
  atf("وَالِانْكِسَارِ", "inkisar", "«collapse»", "«çöküş»", "jarr", tags=["masdar", "form-vii-verbs"], punct="،"),
  tok("وَقَالَتْ", "qala", "verb", [AT, MB, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَالَ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«and she said»", "«ve dedi»", punct=":", segments=wa_("قَالَتْ", "qala", "verb")),
  tok("سَيَكُونُ", "kana", "verb", [KN, "hollow-verbs", "mudari-marfu"], "السِّينُ لِلِاسْتِقْبَالِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«will be» — the sīn of the future with kāna.", "«olacak» — istikbal sîni ile kâne."),
  tok("هٰذَا", "hadha", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُونُ مُقَدَّمٌ.", "«such» — kāna's fronted khabar.", "«böyle» — kâne'nin öne alınmış haberi."),
  tok("شَأْنُ", "shan", "noun", [KN, ID], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the lot» — kāna's delayed ism.", "«hâli» — kâne'nin ismi, muzâf."),
  noun_pron("بِلَادِنَا", "bilad", "بِلَادِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«of our country»", "«ülkemizin»", tags=[ID, JT]),
  noun_pron("وَأُمَّتِنَا", "umma", "وَأُمَّتِ", "نَا", "pron-1p", "الْوَاوُ عَاطِفَةٌ، وَأُمَّتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«and our nation»", "«ve ümmetimizin»", punct="،", tags=[AT, ID]),
])
sen("s7", "and she said to them: I shall send Sulaymān gifts and curiosities and test him with them; if he accepts the gift he is a king, so fight him; and if he does not accept it he is a prophet, so follow him.",
        "ve onlara dedi ki: Süleyman'a hediyeler ve nadide şeyler gönderip onu bunlarla sınayacağım; hediyeyi kabul ederse o bir hükümdardır, onunla savaşın; kabul etmezse o bir peygamberdir, ona uyun.", [
  tok("وَقَالَتْ", "qala", "verb", [AT, MB, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَالَ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and she said»", "«ve dedi»", segments=wa_("قَالَتْ", "qala", "verb")),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»", punct=":"),
  tok("إِنَّنِي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ اسْمُهَا.", "«indeed I» — inna with the nūn of protection and the yāʾ as its ism.", "«şüphesiz ben» — inne; vikâye nûnu; yâ ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("سَأُرْسِلُ", "arsala", "verb", [IW, "mudari-marfu", "form-iv-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَأُرْسِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I shall send» — the clause is inna's khabar.", "«göndereceğim» — cümle inne'nin haberi."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("سُلَيْمَانَ", "sulayman", "propn", [HJ, MM], "مَجْرُورٌ بِإِلَى بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — jarr by fatḥa.", "«Süleyman'a» — fetha ile mecrûr."),
  tok("بِهَدَايَا", "hadiyya", "noun", [HJ, JT, MM], "الْبَاءُ حَرْفُ جَرٍّ، وَهَدَايَا مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«gifts» — a diptote plural, the fatḥa estimated on the alif.", "«hediyelerle» — gayr-i munsarıf; elif üzerinde takdîrî fetha.", segments=[seg("بِ", "bi", "prep"), seg("هَدَايَا", "hadiyya", "noun")]),
  atf("وَطُرَفٍ", "turfa", "«curiosities»", "«nadide şeyler»", "jarr", tags=[JT]),
  tok("فَأَمْتَحِنُهُ", "imtahana", "verb", [AT, MB, "mudari-marfu", "form-viii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأَمْتَحِنُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and test him» — the hāʾ the object.", "«ve onu sınarım» — hâ mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("أَمْتَحِنُ", "imtahana", "verb"), pr3ms()]),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«with them»", "«bunlarla»", punct="،"),
  tok("فَإِنْ", "in-shartiyya", "part", [AT, SH], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional in.", "«eğer» — şart edatı in.", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("قَبِلَ", "qabila", "verb", [SH, MB], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he accepts» — the shart verb.", "«kabul ederse» — şart fiili."),
  maful_("الْهَدِيَّةَ", "hadiyya", "«the gift»", "«hediyeyi»"),
  tok("فَهُوَ", "huwa", "pron", ["fa-khabar-mubtada", SH, MK], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«then he» — the fāʾ binding the answer; the mubtadaʾ.", "«o zaman o» — cevap fâ'sı; mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("مَلِكٌ", "malik-king", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a king» — the khabar.", "«bir hükümdar» — haber."),
  tok("فَقَاتِلُوهُ", "qatala-fight", "verb", [AT, AM, MB, "form-iii-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَقَاتِلُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«so fight him» — an imperative on the dropped nūn; the wāw the doer, the hāʾ the object.", "«onunla savaşın» — nûnun düşmesi üzere mebnî emir; vâv fâil, hâ mef'ûl.", punct="،", segments=[seg("فَ", "fa", "conj"), seg("قَاتِلُو", "qatala-fight", "verb"), pr3ms()]),
  tok("وَإِنْ", "in-shartiyya", "part", [AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa_("إِنْ", "in-shartiyya", "part")),
  tok("لَمْ", "lam-jazima", "part", [LJ, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mezse»"),
  tok("يَقْبَلْهَا", "qabila", "verb", [LJ, SH, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ فِعْلُ الشَّرْطِ، وَهَا مَفْعُولٌ بِهِ.", "«accept it» — the shart verb in jazm; hā the object.", "«onu kabul etmezse» — şart fiili; hâ mef'ûl.", segments=[seg("يَقْبَلْ", "qabila", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("فَهُوَ", "huwa", "pron", ["fa-khabar-mubtada", SH, MK], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَهُوَ مُبْتَدَأٌ.", "«then he»", "«o zaman o»", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("نَبِيٌّ", "nabi", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a prophet» — the khabar.", "«bir peygamber» — haber."),
  tok("فَاتَّبِعُوهُ", "ittabaa", "verb", [AT, AM, MB, "form-viii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَاتَّبِعُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«so follow him»", "«ona uyun»", punct=".", segments=[seg("فَ", "fa", "conj"), seg("اتَّبِعُو", "ittabaa", "verb"), pr3ms()]),
])

# ---------------------------------------------------------------- §10 هَدِيَّةُ مُسَاوَمَةٍ (print p. 19)
sen("s8", "She sent him a magnificent gift worthy of kings; when it reached Sulaymān he turned away from it and had no desire for it, and said:",
        "Ona hükümdarlara yaraşır muhteşem bir hediye gönderdi; hediye Süleyman'a ulaşınca ondan yüz çevirdi, ona rağbet etmedi ve dedi ki:", [
  mazi_ta("وَبَعَثَتْ", "baatha", "«and she sent»", "«ve gönderdi»", tags=[AT], wa=True),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him»", "«ona»"),
  tok("بِهَدِيَّةٍ", "hadiyya", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَدِيَّةٍ مَجْرُورٌ.", "«a gift»", "«bir hediye»", segments=[seg("بِ", "bi", "prep"), seg("هَدِيَّةٍ", "hadiyya", "noun")]),
  naat("عَظِيمَةٍ", "azim", "«magnificent»", "«muhteşem»", tags=["sifa-mushabbaha"]),
  naat("لَائِقَةٍ", "laiq", "«worthy»", "«yaraşır»", tags=["ism-fail"]),
  tok("بِالْمُلُوكِ", "malik-king", "noun", [HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمُلُوكِ مَجْرُورٌ — مُتَعَلِّقٌ بِلَائِقَةٍ.", "«of kings» — attached to «worthy».", "«hükümdarlara» — «yaraşır»a bağlı.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْمُلُوكِ", "malik-king", "noun")]),
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — lammā.", "«… -ınca» — lemmâ.", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi_ta("وَصَلَتْ", "wasala", "«it reached»", "«ulaştı»", tags=[SH, "mithal-verbs"]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("سُلَيْمَانَ", "sulayman", "propn", [HJ, MM], "مَجْرُورٌ بِإِلَى بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān»", "«Süleyman'a»"),
  mazi("أَعْرَضَ", "arada-turn", "«he turned away»", "«yüz çevirdi»", tags=[SH, "form-iv-verbs"], hidden="هُوَ", extra_ar=" — جَوَابُ لَمَّا"),
  prep_pron("عَنْهَا", "an", "هَا", "pron-3fs", "«from it»", "«ondan»"),
  mazi("وَزَهِدَ", "zahida", "«and had no desire»", "«ve rağbet etmedi»", tags=[AT], wa=True, hidden="هُوَ"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«for it»", "«ona»", punct="،"),
  qala(full="وَقَالَ", wa=True, hidden="هُوَ"),
])
sen("s9", "Do you offer me wealth so that I leave you to your idolatry and your dominion? What God has given me of kingdom, wealth and hosts is better than what you are in;",
        "Sizi şirkinizle ve mülkünüzle baş başa bırakayım diye bana mal mı sunuyorsunuz? Allah'ın bana verdiği mülk, mal ve ordular sizin içinde bulunduğunuzdan daha hayırlıdır;", [
  tok("أَتُمِدُّونَنِي", "amadda", "verb", ["al-istifham", AK, "mudari-marfu", MB, "doubled-verbs", "form-iv-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتُمِدُّونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«do you offer me» — the hamza of denial; one of the five verbs; the nūn of protection; the yāʾ the object.", "«bana … mı sunuyorsunuz?» — inkâr hemzesi; ef'âl-i hamseden; vikâye nûnu; yâ mef'ûl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تُمِدُّونَ", "amadda", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("بِمَالٍ", "mal", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَالٍ مَجْرُورٌ.", "«wealth»", "«mal»", segments=[seg("بِ", "bi", "prep"), seg("مَالٍ", "mal", "noun")]),
  tok("لِأَتْرُكَكُمْ", "taraka", "verb", [TA, MB], "اللَّامُ لِلتَّعْلِيلِ، وَأَتْرُكَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَكُمْ مَفْعُولٌ بِهِ.", "«so that I leave you» — the lām of cause; naṣb by a hidden an; kum the object.", "«sizi bırakayım diye» — ta'lîl lâmı; gizli en ile mansub; küm mef'ûl.", segments=[seg("لِ", "li", "prep"), seg("أَتْرُكَ", "taraka", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  prep("عَلَى", "ala", "«to»", "«… ile»"),
  noun_pron("شِرْكِكُمْ", "shirk", "شِرْكِ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your idolatry»", "«şirkiniz»", tags=[HJ, ID]),
  noun_pron("وَمُلْكِكُمْ", "mulk", "وَمُلْكِ", "كُمْ", "pron-2mp", "الْوَاوُ عَاطِفَةٌ، وَمُلْكِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«and your dominion»", "«ve mülkünüz»", punct="؟", tags=[AT, ID]),
  tok("وَالَّذِي", "alladhi", "pron", [MK, MW], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالَّذِي اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and what» — the relative, the mubtadaʾ.", "«ve … -diği» — ism-i mevsûl, mübtedâ.", segments=wa_("الَّذِي", "alladhi", "pron")),
  tok("أَعْطَانِيَ", "aata", "verb", [MW, MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ — صِلَةٌ.", "«has given me» — the ṣila; the yāʾ the first object.", "«bana verdi» — sıla; yâ ilk mef'ûl.", segments=[seg("أَعْطَا", "aata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("يَ", "pron-1s", "pron")]),
  allah_fail(),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْمُلْكِ", "mulk", "«kingdom»", "«mülk»"),
  atf("وَالْمَالِ", "mal", "«wealth»", "«mal»", "jarr"),
  atf("وَالْجُنُودِ", "jund", "«hosts»", "«ordular»", "jarr", tags=[JT], punct="،"),
  tok("خَيْرٌ", "khayr", "noun", [MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.", "«better» — the khabar; an elative with its hamza dropped.", "«daha hayırlı» — haber; hemzesi düşmüş ism-i tafdîl."),
  tok("مِمَّا", "ma-mawsula", "pron", [HJ, MW], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ فِي مَا الْمَوْصُولَةِ، وَمَا فِي مَحَلِّ جَرٍّ.", "«than what» — min fused into the relative mā.", "«… -den» — min, ism-i mevsûl mâ ile idgam edilmiş.", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  tok("أَنْتُمْ", "antum", "pron", [MW, MK], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — صِلَةٌ.", "«you» — the mubtadaʾ of the ṣila.", "«siz» — sılanın mübtedâsı."),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«are in» — the khabar.", "«içindesiniz» — haber.", tags=[MK], punct="،"),
])
sen("s10", "the matter is earnest, not jest; the issue is one of a call and obedience, not one of bargaining. And he threatened them with marching against their kingdom.",
        "iş ciddidir, şaka değildir; mesele bir davet ve itaat meselesidir, pazarlık meselesi değildir. Ve onları mülklerine yürümekle tehdit etti.", [
  tok("وَالْأَمْرُ", "amr-noun", "noun", [AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْأَمْرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the matter» — the mubtadaʾ.", "«ve iş» — mübtedâ.", segments=wa_("الْأَمْرُ", "amr-noun", "noun")),
  tok("جِدٌّ", "jidd", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«earnest» — the khabar.", "«ciddi» — haber."),
  tok("لَيْسَ", "laysa", "verb", [KN, "ma-la-mushabbaha"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is not» — laysa; its ism concealed.", "«değildir» — leyse; ismi gizli."),
  tok("بِهَزْلٍ", "hazl", "noun", [HJ, KN], "الْبَاءُ زَائِدَةٌ، وَهَزْلٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "«jest» — laysa's khabar under a redundant bāʾ: jarr in form, naṣb in place.", "«şaka» — zâid bâ ile leyse'nin haberi: lafzan mecrûr, mahallen mansub.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("هَزْلٍ", "hazl", "noun")]),
  tok("وَالْقَضِيَّةُ", "qadiyya", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْقَضِيَّةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the issue» — the mubtadaʾ.", "«ve mesele» — mübtedâ.", segments=wa_("الْقَضِيَّةُ", "qadiyya", "noun")),
  tok("قَضِيَّةُ", "qadiyya", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«an issue [of]» — the khabar, annexed.", "«… meselesi» — haber, muzâf."),
  mudaf_ilayh("دَعْوَةٍ", "dawa", "«a call»", "«davet»"),
  atf("وَطَاعَةٍ", "taa", "«obedience»", "«itaat»", "jarr", punct="،"),
  tok("لَيْسَتْ", "laysa", "verb", [KN, "ma-la-mushabbaha"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«it is not» — laysa with the feminine tāʾ.", "«değildir» — te'nis tâ'sı ile leyse."),
  tok("قَضِيَّةَ", "qadiyya", "noun", [KN, ID], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«an issue [of]» — laysa's khabar, in naṣb.", "«… meselesi» — leyse'nin haberi, mansub."),
  mudaf_ilayh("مُسَاوَمَةٍ", "musawama", "«bargaining»", "«pazarlık»", tags=["masdar"], punct="،"),
  tok("وَتَوَعَّدَهُمْ", "tawaada", "verb", [AT, MB, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَوَعَّدَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«and he threatened them» — hum the object.", "«ve onları tehdit etti» — hüm mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("تَوَعَّدَ", "tawaada", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  noun_pron("بِقَصْدِهِ", "qasd", "بِقَصْدِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَقَصْدِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with his coming for»", "«onlara yönelmekle»", tags=[HJ, ID, "masdar"]),
  noun_pron("وَزَحْفِهِ", "zahf", "وَزَحْفِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَزَحْفِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and marching»", "«ve yürümekle»", tags=[AT, ID, "masdar"]),
  prep("عَلَى", "ala", "«against»", "«-e»"),
  noun_pron("مُلْكِهِمْ", "mulk", "مُلْكِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their kingdom»", "«mülklerine»", punct=".", tags=[HJ, ID]),
])

# ---------------------------------------------------------------- §11 الْمَلِكَةُ تَأْتِي خَاضِعَةً (print pp. 19–20)
sen("s11", "When this delegation returned to the queen of Sabaʾ and told her the story, she and her people heard and obeyed, and she set out towards him among her hosts, submissive;",
        "Bu heyet Sebe' kraliçesine dönüp olanları anlatınca, o ve kavmi dinleyip itaat ettiler; kraliçe orduları içinde boyun eğmiş olarak ona doğru yola çıktı;", [
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ لِلِاسْتِئْنَافِ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — lammā.", "«… -ınca» — lemmâ.", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi_ta("رَجَعَتْ", "rajaa", "«returned»", "«döndü»", tags=[SH]),
  tok("هٰذِهِ", "hadhihi", "pron", [FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this» — the doer.", "«bu» — fâil."),
  tok("الْبِعْثَةُ", "bitha", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ.", "«delegation» — the badal.", "«heyet» — bedel."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("مَلِكَةِ", "malika", "«the queen»", "«kraliçesine»", tags=[ID], ar="مَجْرُورٌ بِإِلَى، مُضَافٌ."),
  mudaf_ilayh("سَبَإٍ", "saba", "«of Sabaʾ»", "«Sebe'»", punct="،"),
  mazi_ta("وَحَكَتْ", "haka", "«and told»", "«ve anlattı»", tags=[AT, "naqis-verbs"], wa=True, extra="، حُذِفَتْ أَلِفُهُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  li_pron("لَهَا", "هَا", "pron-3fs", "«her»", "«ona»"),
  maful_("الْقِصَّةَ", "qissa", "«the story»", "«olanları»", punct="،"),
  mazi_ta("سَمِعَتْ", "samia", "«she heard»", "«dinledi»", tags=[SH], extra=" — جَوَابُ لَمَّا"),
  mazi_ta("وَأَطَاعَتْ", "ataa", "«and obeyed»", "«ve itaat etti»", tags=[AT, "hollow-verbs", "form-iv-verbs"], wa=True),
  tok("هِيَ", "hiya", "pron", ["tawkid"], "ضَمِيرٌ مُنْفَصِلٌ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ (لِيَصِحَّ الْعَطْفُ عَلَيْهِ).", "«she» — a detached pronoun confirming the concealed one, so that the joining is sound.", "«o» — atıf sahih olsun diye gizli zamiri pekiştiren munfasıl zamir."),
  noun_pron("وَقَوْمُهَا", "qawm", "وَقَوْمُ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَقَوْمُ مَعْطُوفٌ عَلَى الضَّمِيرِ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her people»", "«ve kavmi»", punct="،", tags=[AT, ID]),
  mazi_ta("وَأَقْبَلَتْ", "aqbala", "«and she set out»", "«ve yola koyuldu»", tags=[AT, "form-iv-verbs"], wa=True),
  mudari("تَسِيرُ", "sara-travel", "«travelling»", "«giderek»", tags=[HL, "hollow-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«towards him»", "«ona doğru»"),
  fi(), noun_pron("جُنُودِهَا", "jund", "جُنُودِ", "هَا", "pron-3fs", "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her hosts»", "«orduları»", tags=[HJ, ID, JT]),
  tok("خَاضِعَةً", "khadi-submissive", "noun", [HL, "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«submissive» — a ḥāl.", "«boyun eğmiş olarak» — hâl.", punct="،"),
])
sen("s12", "and when Sulaymān, peace be upon him, was certain of their coming to him, he rejoiced at it and praised God, and wished to show her a sign among the signs of God, so that it would point all the more to the power of God and His favours on Sulaymān;",
        "Süleyman — selâm üzerine olsun — onların kendisine geldiğinden emin olunca buna sevindi, Allah'a hamd etti ve ona Allah'ın âyetlerinden bir âyet göstermek istedi; tâ ki bu, Allah'ın kudretine ve Süleyman'a olan nimetlerine daha çok delâlet etsin;", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF, SH], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — lammā.", "«ve … -ınca» — lemmâ.", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("تَحَقَّقَ", "tahaqqaqa", "«was certain of»", "«emin oldu»", tags=[SH, MB, "form-v-verbs"], hidden=None),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon him» — a fronted khabar of a parenthetical prayer.", "«üzerine» — mu'teriza duâ cümlesinin öne alınmış haberi.", tags=[MK]),
  tok("السَّلَامُ", "salam", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«peace» — the delayed mubtadaʾ of the prayer.", "«selâm» — duâ cümlesinin mübtedâsı."),
  noun_pron("قُدُومَهُمْ", "qudum", "قُدُومَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their coming» — the object.", "«gelişlerini» — mef'ûl.", tags=[MB, ID, "masdar"]),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him»", "«kendisine»"),
  mazi("فَرِحَ", "fariha", "«he rejoiced»", "«sevindi»", tags=[SH], hidden="هُوَ", extra_ar=" — جَوَابُ لَمَّا"),
  tok("بِذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَذٰلِكَ فِي مَحَلِّ جَرٍّ.", "«at it»", "«buna»", segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  mazi("وَحَمِدَ", "hamida", "«and praised»", "«ve hamd etti»", tags=[AT, MB], wa=True, hidden="هُوَ"),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'a» — mef'ûl.", punct="،"),
  mazi("وَأَرَادَ", "arada", "«and wished»", "«ve istedi»", tags=[AT, "hollow-verbs", "form-iv-verbs", MB], wa=True, hidden="هُوَ"),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَرَادَ.", "«to» — the an of naṣb; the clause is the object of «wished».", "«… -mek» — nasb eden en; cümle «istedi»nin mef'ûlü."),
  tok("يُرِيَهَا", "ara", "verb", [AN, MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ أَوَّلُ.", "«show her» — naṣb by an, the fatḥa visible on the yāʾ; hā the first object.", "«ona göstermek» — en ile mansub, yâ üzerinde açık fetha; hâ ilk mef'ûl.", segments=[seg("يُرِيَ", "ara", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("آيَةً", "aya", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a sign» — the second object.", "«bir âyet» — ikinci mef'ûl."),
  prep("مِنْ", "min", "«among»", "«-den»"),
  majrur("آيَاتِ", "aya", "«the signs»", "«âyetlerinden»", tags=[ID, JM], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»", punct="،"),
  tok("لِيَكُونَ", "kana", "verb", [TA, KN, "hollow-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَيَكُونَ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«so that … would be» — the lām of cause with kāna in naṣb.", "«… olsun diye» — ta'lîl lâmı ile mansub kâne.", segments=[seg("لِ", "li", "prep"), seg("يَكُونَ", "kana", "verb")]),
  tok("ذٰلِكَ", "dhalika", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُونَ.", "«it» — kāna's ism.", "«bu» — kâne'nin ismi."),
  tok("أَدَلَّ", "adall", "noun", [KN, "ism-tafdil", MM], "خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more indicative» — kāna's khabar; an elative, a diptote.", "«daha çok delâlet eden» — kâne'nin haberi; ism-i tafdîl, gayr-i munsarıf."),
  prep("عَلَى", "ala", "«of»", "«-e»"),
  majrur("قُدْرَةِ", "qudra", "«the power»", "«kudretine»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  noun_pron("وَنِعَمِهِ", "nima", "وَنِعَمِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَنِعَمِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His favours»", "«ve nimetlerine»", tags=[AT, ID, JT]),
  prep("عَلَى", "ala", "«on»", "«-e olan»"),
  tok("سُلَيْمَانَ", "sulayman", "propn", [HJ, MM], "مَجْرُورٌ بِعَلَى بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān»", "«Süleyman'a»", punct="،"),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: mara-woman, sair-rest, qatala-fight, sara-travel, khadi-submissive take suffixed keys; ataa = أَطَاعَ, tawaada = تَوَعَّدَ, qabila = قَبِلَ are reused)
CAND = {
 "hazim": G("hazim", "حَازِم", "ح ز م", "noun", "resolute, firm (an active participle)", "kararlı, azimli (ism-i fâil)", 3),
 "mara-woman": G("mara-woman", "مَرْأَة", "م ر أ", "noun", "a woman", "kadın", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (feminine)", "ki o (müennes)", 1),
 "hakama": G("hakama", "حَكَمَ", "ح ك م", "verb", "to rule, to judge", "hükmetmek, yönetmek", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "bilad": G("bilad", "بِلَاد", "ب ل د", "noun", "a country, lands", "ülke", 1),
 "aqil": G("aqil", "عَاقِل", "ع ق ل", "noun", "intelligent, sensible (an active participle)", "akıllı (ism-i fâil)", 1),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka; olmayan", 1),
 "mutasarri": G("mutasarri", "مُتَسَرِّع", "س ر ع", "noun", "hasty (the active participle of Form V)", "aceleci (tefa''ul ism-i fâili)", 3),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "judgment", "hüküm", 1),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "with, at — a ẓarf of place; «to have»", "yanında — mekân zarfı; «-in … var»", 1),
 "tajriba": G("tajriba", "تَجْرِبَة", "ج ر ب", "noun", "an experience, a trial", "tecrübe", 2, plural="تَجَارِب"),
 "wasi-wide": G("wasi-wide", "وَاسِع", "و س ع", "noun", "wide", "geniş", 1),
 "sira": G("sira", "سِيرَة", "س ي ر", "noun", "a life, a biography; a way of conduct", "hayat hikâyesi, siyer; tutum", 2, plural="سِيَر"),
 "malik-king": G("malik-king", "مَلِك", "م ل ك", "noun", "a king", "hükümdar", 1, plural="مُلُوك"),
 "khabar": G("khabar", "خَبَر", "خ ب ر", "noun", "news, a report; a history", "haber", 1, plural="أَخْبَار"),
 "fatih": G("fatih", "فَاتِح", "ف ت ح", "noun", "a conqueror (an active participle)", "fatih (ism-i fâil)", 2),
 "innama": G("innama", "إِنَّمَا", None, "part", "only — inna restrained by mā, a particle of restriction", "ancak — mâ ile kâffe olmuş inne, hasr edatı", 2),
 "khana": G("khana", "خَانَ", "خ و ن", "verb", "to betray, to fail (hollow)", "ihanet etmek, yarı yolda bırakmak (ecvef)", 2),
 "aql": G("aql", "عَقْل", "ع ق ل", "noun", "mind, reason", "akıl", 1),
 "marifa": G("marifa", "مَعْرِفَة", "ع ر ف", "noun", "knowing, knowledge", "bilme, tanıma, marifet", 1),
 "ilah": G("ilah", "إِلٰه", "أ ل ه", "noun", "a god; God", "ilâh", 1),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet", 1),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take; to seize", "almak; ele geçirmek", 1),
 "hamiyya": G("hamiyya", "حَمِيَّة", "ح م ي", "noun", "zeal, pride", "hamiyet, gayret", 3),
 "istabadda": G("istabadda", "اِسْتَبَدَّ", "ب د د", "verb", "to act alone, to be despotic (Form X, doubled; with bi)", "tek başına davranmak, istibdat etmek (istif'âl, muzâaf; bi ile)", 3),
 "ray": G("ray", "رَأْي", "ر أ ي", "noun", "an opinion, counsel", "görüş, rey", 1),
 "atlaa": G("atlaa", "أَطْلَعَ", "ط ل ع", "verb", "to show, to acquaint (Form IV; with ʿalā)", "göstermek, haberdar etmek (if'âl; alâ ile)", 3),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "the people (of); family", "ehil; aile", 1),
 "rukn": G("rukn", "رُكْن", "ر ك ن", "noun", "a pillar", "rükün, erkân", 2, plural="أَرْكَان"),
 "dawla": G("dawla", "دَوْلَة", "د و ل", "noun", "a state", "devlet", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a letter; a book", "mektup; kitap", 1, plural="كُتُب"),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "which, who", "ki o", 1),
 "sair-rest": G("sair-rest", "سَائِر", "س أ ر", "noun", "the rest of, all other", "öteki, diğer, bütün", 2),
 "ka": G("ka", "كَ", None, "prep", "like — the kāf of likeness", "gibi — teşbih kâfı", 1),
 "azam": G("azam", "أَعْظَم", "ع ظ م", "noun", "greater, greatest (an elative)", "en büyük (ism-i tafdîl)", 2),
 "zaman": G("zaman", "زَمَان", "ز م ن", "noun", "time", "zaman", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1),
 "dain": G("dain", "دَاعٍ", "د ع و", "noun", "one who calls (a manqūṣ active participle)", "çağıran, davetçi (mankûs ism-i fâil)", 2),
 "lamma": G("lamma", "لَمَّا", None, "part", "when — the ẓarf that joins a cause to its sequel", "… -ınca — lemmâ", 2),
 "badaa": G("badaa", "بَدَأَ", "ب د أ", "verb", "to begin", "başlamak", 1),
 "adalla-boast": G("adalla-boast", "أَدَلَّ", "د ل ل", "verb", "to boast of, to presume on (Form IV, doubled; with bi)", "övünmek, güvenip böbürlenmek (if'âl, muzâaf; bi ile)", 3),
 "quwwa": G("quwwa", "قُوَّة", "ق و ي", "noun", "strength, power", "güç, kuvvet", 1),
 "kathra": G("kathra", "كَثْرَة", "ك ث ر", "noun", "abundance, multitude", "çokluk", 1),
 "jaysh": G("jaysh", "جَيْش", "ج ي ش", "noun", "an army", "ordu", 1, plural="جُيُوش"),
 "irda": G("irda", "إِرْضَاء", "ر ض و", "noun", "pleasing, giving satisfaction (maṣdar of Form IV)", "hoşnut etme (if'âl masdarı)", 3),
 "tamalluq": G("tamalluq", "تَمَلُّق", "م ل ق", "noun", "flattery (maṣdar of Form V)", "yaranma, dalkavukluk (tefa''ul masdarı)", 3),
 "shan": G("shan", "شَأْن", "ش أ ن", "noun", "a matter; the manner, the way (of)", "iş; hâl, tutum", 1),
 "jalis": G("jalis", "جَلِيس", "ج ل س", "noun", "a companion in sitting, a courtier", "yanında oturan, nedim", 3, plural="جُلَسَاء"),
 "hakim-ruler": G("hakim-ruler", "حَاكِم", "ح ك م", "noun", "a ruler", "yönetici, hâkim", 2, plural="حُكَّام"),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "every", "her", 1),
 "makan": G("makan", "مَكَان", "ك و ن", "noun", "a place", "mekân", 1),
 "qabila": G("qabila", "قَبِلَ", "ق ب ل", "verb", "to accept", "kabul etmek", 1),
 "maqala": G("maqala", "مَقَالَة", "ق و ل", "noun", "a saying, speech", "söz, makale", 2),
 "wafaqa": G("wafaqa", "وَافَقَ", "و ف ق", "verb", "to agree with (Form III)", "uymak, muvafakat etmek (müfâale)", 2),
 "bal": G("bal", "بَلْ", None, "part", "rather", "aksine", 2),
 "hadhdhara": G("hadhdhara", "حَذَّرَ", "ح ذ ر", "verb", "to warn (Form II; with min)", "uyarmak (tef'îl; min ile)", 2),
 "su": G("su", "سُوء", "س و أ", "noun", "evil, badness", "kötülük", 1),
 "aqiba": G("aqiba", "عَاقِبَة", "ع ق ب", "noun", "the end, the outcome", "akıbet, son", 2),
 "dhakkara": G("dhakkara", "ذَكَّرَ", "ذ ك ر", "verb", "to remind (Form II; with bi)", "hatırlatmak (tef'îl; bi ile)", 2),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation", "ümmet", 1, plural="أُمَم"),
 "maftuh": G("maftuh", "مَفْتُوح", "ف ت ح", "noun", "conquered; opened (a passive participle)", "fethedilmiş; açık (ism-i mef'ûl)", 2),
 "masir-fate": G("masir-fate", "مَصِير", "ص ي ر", "noun", "fate, destiny", "akıbet, son", 2),
 "bada": G("bada", "بَعْدَ", "ب ع د", "noun", "after", "sonra", 1),
 "hazima": G("hazima", "هَزِيمَة", "ه ز م", "noun", "defeat", "yenilgi, hezimet", 2),
 "inkisar": G("inkisar", "اِنْكِسَار", "ك س ر", "noun", "collapse, being broken (maṣdar of Form VII)", "kırılma, çöküş (infiâl masdarı)", 3),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send (Form IV)", "göndermek (if'âl)", 1),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection before the speaker's yāʾ", "mütekellim yâ'sından önceki vikâye nûnu", 2),
 "hadiyya": G("hadiyya", "هَدِيَّة", "ه د ي", "noun", "a gift", "hediye", 1, plural="هَدَايَا"),
 "turfa": G("turfa", "طُرْفَة", "ط ر ف", "noun", "a curiosity, a rare and precious thing", "nadide şey, tuhfe", 3, plural="طُرَف"),
 "imtahana": G("imtahana", "اِمْتَحَنَ", "م ح ن", "verb", "to test, to try (Form VIII)", "sınamak, imtihan etmek (iftiâl)", 2),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if — the conditional particle", "eğer — şart edatı", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "qatala-fight": G("qatala-fight", "قَاتَلَ", "ق ت ل", "verb", "to fight (Form III)", "savaşmak (müfâale)", 1),
 "ittabaa": G("ittabaa", "اِتَّبَعَ", "ت ب ع", "verb", "to follow (Form VIII)", "uymak (iftiâl)", 2),
 "baatha": G("baatha", "بَعَثَ", "ب ع ث", "verb", "to send", "göndermek", 2),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great, magnificent", "büyük, muhteşem", 1),
 "laiq": G("laiq", "لَائِق", "ل ي ق", "noun", "worthy, fitting (an active participle)", "yaraşır, lâyık (ism-i fâil)", 2),
 "wasala": G("wasala", "وَصَلَ", "و ص ل", "verb", "to arrive, to reach", "ulaşmak", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to wish (Form IV, hollow)", "istemek (if'âl, ecvef)", 1),
 "arada-turn": G("arada-turn", "أَعْرَضَ", "ع ر ض", "verb", "to turn away (Form IV; with ʿan)", "yüz çevirmek (if'âl; an ile)", 2),
 "zahida": G("zahida", "زَهِدَ", "ز ه د", "verb", "to have no desire for, to renounce (with fī)", "rağbet etmemek, zühd etmek (fî ile)", 3),
 "amadda": G("amadda", "أَمَدَّ", "م د د", "verb", "to supply, to offer (Form IV, doubled; with bi)", "sunmak, yardım etmek (if'âl, muzâaf; bi ile)", 3),
 "hamza-istifham": G("hamza-istifham", "أَ (هَمْزَةُ الِاسْتِفْهَامِ)", None, "part", "the hamza of interrogation", "soru hemzesi", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "wealth, property", "mal", 1),
 "taraka": G("taraka", "تَرَكَ", "ت ر ك", "verb", "to leave", "bırakmak", 1),
 "shirk": G("shirk", "شِرْك", "ش ر ك", "noun", "idolatry, associating partners with God", "şirk", 1),
 "aata": G("aata", "أَعْطَى", "ع ط و", "verb", "to give (Form IV, defective; two objects)", "vermek (if'âl, nâkıs; iki mef'ûl)", 1),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good; better", "hayır; daha hayırlı", 1),
 "antum": G("antum", "أَنْتُمْ", None, "pron", "you (masc. plural)", "siz", 1),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "a matter", "iş", 1),
 "jidd": G("jidd", "جِدّ", "ج د د", "noun", "earnestness, seriousness", "ciddiyet", 2),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not — the frozen verb of negation, a sister of kāna", "değildir — câmid nefiy fiili, kâne'nin kardeşi", 1),
 "hazl": G("hazl", "هَزْل", "ه ز ل", "noun", "jest, joking", "şaka", 2),
 "qadiyya": G("qadiyya", "قَضِيَّة", "ق ض ي", "noun", "an issue, a case", "mesele, dava", 2),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "a call", "davet", 1),
 "taa": G("taa", "طَاعَة", "ط و ع", "noun", "obedience", "itaat", 1),
 "musawama": G("musawama", "مُسَاوَمَة", "س و م", "noun", "bargaining, haggling (maṣdar of Form III)", "pazarlık (müfâale masdarı)", 3),
 "tawaada": G("tawaada", "تَوَعَّدَ", "و ع د", "verb", "to threaten (Form V)", "tehdit etmek (tefa''ul)", 3),
 "qasd": G("qasd", "قَصْد", "ق ص د", "noun", "coming for, aiming at; intent", "yönelme, kasıt", 2),
 "zahf": G("zahf", "زَحْف", "ز ح ف", "noun", "a march, an advance (of an army)", "ordu yürüyüşü, ilerleme", 3),
 "mulk": G("mulk", "مُلْك", "م ل ك", "noun", "a kingdom", "mülk", 2),
 "rajaa": G("rajaa", "رَجَعَ", "ر ج ع", "verb", "to return", "dönmek", 1),
 "bitha": G("bitha", "بِعْثَة", "ب ع ث", "noun", "a delegation, a mission", "heyet, elçi topluluğu", 3),
 "malika": G("malika", "مَلِكَة", "م ل ك", "noun", "a queen", "kraliçe", 1),
 "saba": G("saba", "سَبَأ", "س ب أ", "propn", "Sabaʾ", "Sebe'", 2),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell", "anlatmak", 2),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear, to listen", "dinlemek, işitmek", 1),
 "ataa": G("ataa", "أَطَاعَ", "ط و ع", "verb", "to obey (Form IV, hollow)", "itaat etmek (if'âl, ecvef)", 1),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it", "o (müennes)", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people", "kavim", 1),
 "aqbala": G("aqbala", "أَقْبَلَ", "ق ب ل", "verb", "to set out, to come forward (Form IV)", "yönelmek, yola koyulmak (if'âl)", 2),
 "sara-travel": G("sara-travel", "سَارَ", "س ي ر", "verb", "to travel, to go (hollow)", "yola gitmek, yürümek (ecvef)", 1),
 "jund": G("jund", "جُنْد", "ج ن د", "noun", "a host", "ordu", 2, plural="جُنُود"),
 "khadi-submissive": G("khadi-submissive", "خَاضِع", "خ ض ع", "noun", "submissive (an active participle)", "boyun eğmiş (ism-i fâil)", 2),
 "tahaqqaqa": G("tahaqqaqa", "تَحَقَّقَ", "ح ق ق", "verb", "to be certain of, to verify (Form V)", "emin olmak, doğrulamak (tefa''ul)", 2),
 "salam": G("salam", "سَلَام", "س ل م", "noun", "peace", "selâm", 1),
 "qudum": G("qudum", "قُدُوم", "ق د م", "noun", "coming, arrival (a maṣdar)", "geliş (masdar)", 2),
 "fariha": G("fariha", "فَرِحَ", "ف ر ح", "verb", "to rejoice (with bi)", "sevinmek (bi ile)", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "hamida": G("hamida", "حَمِدَ", "ح م د", "verb", "to praise", "hamd etmek", 1),
 "ara": G("ara", "أَرَى", "ر أ ي", "verb", "to show (Form IV, defective; two objects)", "göstermek (if'âl, nâkıs; iki mef'ûl)", 2),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "adall": G("adall", "أَدَلّ", "د ل ل", "noun", "more indicative, a clearer proof (an elative)", "daha çok delâlet eden (ism-i tafdîl)", 3),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power", "kudret", 2),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a favour", "nimet", 1, plural="نِعَم"),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our", "biz / bizi / bizim", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "pron-2mp": G("pron-2mp", "كُمْ", None, "pron", "you / your (masc. plural)", "siz / sizin", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "khana", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "خَان", "خُن", "خُون", "خُن", "خُون", "خُن", "خِيَانَة", "خَائِن", "مَخُون", "خِينَ", "يُخَانُ", "خَانَهُ: لَمْ يَفِ لَهُ وَغَدَرَ بِهِ؛ خَانَهُ عَقْلُهُ: لَمْ يُسْعِفْهُ."))
put_morph(mo, "istabadda", _sg.entry(_sg.B10 + " — مُضَاعَفٌ", _sg.W10, "اِسْتِبْدَاد", "مُسْتَبِدّ", _sg.mazi14("اِسْتَبَدّ", "اِسْتَبْدَد"), _sg.mudari14("َ", "سْتَبِدّ", "سْتَبْدِد"), ["اِسْتَبِدَّ", "اِسْتَبِدَّا", "اِسْتَبِدُّوا", "اِسْتَبِدِّي", "اِسْتَبِدَّا", "اِسْتَبْدِدْنَ"], "يَسْتَبِدَّ", "يَسْتَبِدَّ", "تَسْتَبِدَّ", None, None, None, "اِسْتَبَدَّ بِالْأَمْرِ: انْفَرَدَ بِهِ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسْتَبِدَّ."))
put_morph(mo, "atlaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْلَع", "طْلِع", "أَطْلِع", "إِطْلَاع", "مُطْلِع", "مُطْلَع", "أُطْلِعَ", "يُطْلَعُ", "أَطْلَعَهُ عَلَى الشَّيْءِ: أَعْلَمَهُ بِهِ."))
put_morph(mo, "badaa", _sg.entry("مِنْ بَابِ فَتَحَ يَفْتَحُ — مَهْمُوزُ اللَّامِ", "فَعَلَ يَفْعَلُ", "بَدْء", "بَادِئ", ["بَدَأَ", "بَدَآ", "بَدَؤُوا", "بَدَأَتْ", "بَدَأَتَا", "بَدَأْنَ", "بَدَأْتَ", "بَدَأْتُمَا", "بَدَأْتُمْ", "بَدَأْتِ", "بَدَأْتُمَا", "بَدَأْتُنَّ", "بَدَأْتُ", "بَدَأْنَا"], ["يَبْدَأُ", "يَبْدَآنِ", "يَبْدَؤُونَ", "تَبْدَأُ", "تَبْدَآنِ", "يَبْدَأْنَ", "تَبْدَأُ", "تَبْدَآنِ", "تَبْدَؤُونَ", "تَبْدَئِينَ", "تَبْدَآنِ", "تَبْدَأْنَ", "أَبْدَأُ", "نَبْدَأُ"], ["اِبْدَأْ", "اِبْدَآ", "اِبْدَؤُوا", "اِبْدَئِي", "اِبْدَآ", "اِبْدَأْنَ"], "يَبْدَأَ", "يَبْدَأْ", "تَبْدَأْ", "مَبْدُوء", "بُدِئَ", "يُبْدَأُ", "بَدَأَ الشَّيْءَ وَبِهِ: شَرَعَ فِيهِ — مَهْمُوزُ اللَّامِ، تُرْسَمُ هَمْزَتُهُ عَلَى مَا يُنَاسِبُ حَرَكَتَهَا."))
put_morph(mo, "adalla-boast", _sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "إِدْلَال", "مُدِلّ", _sg.mazi14("أَدَلّ", "أَدْلَل"), _sg.mudari14("ُ", "دِلّ", "دْلِل"), ["أَدِلَّ", "أَدِلَّا", "أَدِلُّوا", "أَدِلِّي", "أَدِلَّا", "أَدْلِلْنَ"], "يُدِلَّ", "يُدِلَّ", "تُدِلَّ", None, None, None, "أَدَلَّ بِالشَّيْءِ: افْتَخَرَ بِهِ وَوَثِقَ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُدِلَّ."))
put_morph(mo, "wafaqa", _sg.derived(_sg.B3, _sg.W3, "ُ", "وَافَق", "وَافِق", "وَافِق", "مُوَافَقَة", "مُوَافِق", "مُوَافَق", "وُوفِقَ", "يُوَافَقُ", "وَافَقَهُ عَلَى الْأَمْرِ: رَضِيَ بِهِ مَعَهُ."))
put_morph(mo, "hadhdhara", _sg.derived(_sg.B2, _sg.W2, "ُ", "حَذَّر", "حَذِّر", "حَذِّر", "تَحْذِير", "مُحَذِّر", "مُحَذَّر", "حُذِّرَ", "يُحَذَّرُ", "حَذَّرَهُ مِنَ الشَّيْءِ: خَوَّفَهُ مِنْهُ."))
put_morph(mo, "dhakkara", _sg.derived(_sg.B2, _sg.W2, "ُ", "ذَكَّر", "ذَكِّر", "ذَكِّر", "تَذْكِير", "مُذَكِّر", "مُذَكَّر", "ذُكِّرَ", "يُذَكَّرُ", "ذَكَّرَهُ بِالشَّيْءِ: جَعَلَهُ يَذْكُرُهُ."))
put_morph(mo, "imtahana", _sg.derived(_sg.B8, _sg.W8, "َ", "اِمْتَحَن", "مْتَحِن", "اِمْتَحِن", "اِمْتِحَان", "مُمْتَحِن", "مُمْتَحَن", "اُمْتُحِنَ", "يُمْتَحَنُ", "اِمْتَحَنَهُ: اخْتَبَرَهُ."))
put_morph(mo, "qatala-fight", _sg.derived(_sg.B3, _sg.W3, "ُ", "قَاتَل", "قَاتِل", "قَاتِل", "قِتَال / مُقَاتَلَة", "مُقَاتِل", "مُقَاتَل", "قُوتِلَ", "يُقَاتَلُ", "قَاتَلَهُ: حَارَبَهُ."))
put_morph(mo, "arada-turn", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْرَض", "عْرِض", "أَعْرِض", "إِعْرَاض", "مُعْرِض", None, None, None, "أَعْرَضَ عَنِ الشَّيْءِ: صَدَّ عَنْهُ وَتَرَكَهُ."))
put_morph(mo, "zahida", _sg.sound1("samia", "زَهِد", "زْهَد", "اِزْهَد", "زُهْد", "زَاهِد", None, None, None, "زَهِدَ فِي الشَّيْءِ: لَمْ يَرْغَبْ فِيهِ."))
put_morph(mo, "amadda", _sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "إِمْدَاد", "مُمِدّ", _sg.mazi14("أَمَدّ", "أَمْدَد"), _sg.mudari14("ُ", "مِدّ", "مْدِد"), ["أَمِدَّ", "أَمِدَّا", "أَمِدُّوا", "أَمِدِّي", "أَمِدَّا", "أَمْدِدْنَ"], "يُمِدَّ", "يُمِدَّ", "تُمِدَّ", "مُمَدّ", "أُمِدَّ", "يُمَدُّ", "أَمَدَّهُ بِالشَّيْءِ: أَعَانَهُ بِهِ وَأَعْطَاهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُمِدَّ."))
put_morph(mo, "rajaa", _sg.sound1("daraba", "رَجَع", "رْجِع", "اِرْجِع", "رُجُوع", "رَاجِع", "مَرْجُوع", "رُجِعَ", "يُرْجَعُ", "رَجَعَ إِلَى الْمَكَانِ: عَادَ إِلَيْهِ."))
put_morph(mo, "aqbala", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْبَل", "قْبِل", "أَقْبِل", "إِقْبَال", "مُقْبِل", None, None, None, "أَقْبَلَ عَلَى الشَّيْءِ: تَوَجَّهَ إِلَيْهِ."))
put_morph(mo, "sara-travel", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "سَار", "سِر", "سِير", "سِر", "سِير", "سِر", "سَيْر", "سَائِر", None, None, None, "سَارَ: مَشَى وَذَهَبَ."))
put_morph(mo, "tahaqqaqa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَقَّق", "تَحَقَّق", "تَحَقَّق", "تَحَقُّق", "مُتَحَقِّق", "مُتَحَقَّق", "تُحُقِّقَ", "يُتَحَقَّقُ", "تَحَقَّقَ الْأَمْرَ: تَيَقَّنَهُ؛ وَتَحَقَّقَ الْأَمْرُ: ثَبَتَ وَصَحَّ."))
put_morph(mo, "fariha", _sg.sound1("samia", "فَرِح", "فْرَح", "اِفْرَح", "فَرَح", "فَرِح (فَرْحَان)", None, None, None, "فَرِحَ بِالشَّيْءِ: سُرَّ بِهِ."))
put_morph(mo, "hamida", _sg.sound1("samia", "حَمِد", "حْمَد", "اِحْمَد", "حَمْد", "حَامِد", "مَحْمُود", "حُمِدَ", "يُحْمَدُ", "حَمِدَ اللهَ: أَثْنَى عَلَيْهِ وَشَكَرَهُ."))
put_morph(mo, "ara", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَرَ", "ر", "i", "أَر", "إِرَاءَة", "مُرٍ (الْمُرِي)", "مُرًى", "أُرِيَ", "يُرَى", "أَرَاهُ الشَّيْءَ: جَعَلَهُ يَرَاهُ — إِفْعَالٌ مِنْ رَأَى، حُذِفَتْ هَمْزَتُهُ فِي الْمُضَارِعِ: يُرِي."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch10 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 10 (print pp. 18–20, §9–11): the queen consults her council and tests Sulaymān with a gift (s1–s7); the bargaining gift refused (s8–s10); the queen comes submissive and Sulaymān wishes to show her a sign (s11–s12). One word of print p. 18, after حَازِمًا, is illegible in the scan and left out."
ADD_TR = " Onuncu bölüm (baskı s. 18–20, 9–11. kısımlar): kraliçe erkânına danışır ve Süleyman'ı bir hediyeyle sınar (s1–s7); pazarlık hediyesi reddedilir (s8–s10); kraliçe boyun eğerek gelir, Süleyman ona bir âyet göstermek ister (s11–s12). Baskı s. 18'de حَازِمًا'dan sonraki bir kelime taramada okunamadığından alınmamıştır."
write_out(10, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §9–11", GLOSS_ADD, notes=(), related=())
report(10, S, GLOSS_ADD, ())
