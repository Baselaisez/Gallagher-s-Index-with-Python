# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 21: «عِنَايَةُ اللهِ بِالْفَتَاةِ الصَّالِحَةِ» — §4 (God's care for the righteous girl, with 3:37), §5 (an inspiration from the
Merciful Lord, with 3:38), §6 (the glad tidings of a son, with 3:41); print pp. 34–37.
python3 tools/authoring/author_qisas4_ch21.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "عِنَايَةُ اللهِ بِالْفَتَاةِ الصَّالِحَةِ وَبِشَارَةُ وَلَدٍ", "en": "God's care for the righteous girl, and the glad tidings of a son", "tr": "Allah'ın sâliha kıza inâyeti ve bir evlât müjdesi"}
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

def hal(full, lex, en, tr, punct=None, tags=(), ar="حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [HL] + list(tags), ar, en + " — a ḥāl.", tr + " — hâl.", punct=punct)
def naat2(full, lex, en, tr, case="raf", punct=None, tags=(), n="ثَانٍ"):
    C = {"jarr": "نَعْتٌ " + n + " مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ " + n + " مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ " + n + " مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — a further naʿt.", tr + " — bir sıfat daha.", punct=punct)
def la_jins(full, wa=False, punct=None):
    return tok(full, "la-nafiya", "part", ["la-nafiya-lil-jins"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", ("«and» + " if wa else "") + "«no» — the lā of the genus; it governs like inna.", ("«ve» + " if wa else "") + "«yok» — cins nefyeden lâ; inne gibi amel eder.", punct=punct, segments=(wa_("لَا", "la-nafiya", "part") if wa else None))
def ism_la(full, lex, en, tr, punct=None, tags=(), khabar="مَوْجُودٌ"):
    return tok(full, lex, "noun", ["la-nafiya-lil-jins", "hadhf-wa-taqdir"] + list(tags), f"اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ تَقْدِيرُهُ: {khabar}.", en + " — lā's ism, built on fatḥa; its khabar is understood.", tr + " — lâ'nın ismi, fetha üzere mebnî; haberi mahzuf.", punct=punct)
def v_pl_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), fa=False, wa=False):
    pre = "الْفَاءُ عَاطِفَةٌ، وَ" if fa else ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
    segs = ([seg("فَ" if fa else "وَ", "fa" if fa else "wa", "conj")] if (fa or wa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (fa or wa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", en + " — a māḍī on the group's wāw; the attached pronoun is its object.", tr + " — cemi vâvlı mâzî; bitişik zamir mef'ûl.", punct=punct, segments=segs)
def mazi_wa_alif(full, lex, en, tr, punct=None, tags=(), fa=False, wa=False, extra=""):
    pre = "الْفَاءُ عَاطِفَةٌ، وَ" if fa else ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
    body = full[2:] if (fa or wa) else full
    return tok(full, lex, "verb", ([AT] if (fa or wa) else []) + ["naqis-verbs"] + list(tags), pre + body + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ" + extra + ".", en + " — a defective māḍī before the group's wāw: its alif dropped, the fatḥa stays (أَبَوْا).", tr + " — nâkıs mâzî, cemi vâvı önünde elif düştü; fetha kaldı.", punct=punct, segments=(conj_segs(full, lex, "verb") if (fa or wa) else None))
def mazi_ta_naqis(full, lex, en, tr, punct=None, tags=(), wa=True):
    body = full[2:] if wa else full
    return tok(full, lex, "verb", ([AT] if wa else []) + ["naqis-verbs"] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + body + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", en + " — a defective māḍī (رَغَا) with the feminine tāʾ: the alif dropped before the sukūn, and the tāʾ takes a kasra before the next hamzat al-waṣl.", tr + " — nâkıs mâzî (رَغَا) + te'nis tâ'sı: elif düştü; tâ iki sâkin yüzünden kesre aldı.", punct=punct, segments=(conj_segs(full, lex, "verb") if wa else None))

def alayhi_salam(punct=None):
    return [prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon him» — the fronted khabar.", "«ona» — öne alınmış haber.", tags=[MK], extra_ar=" — خَبَرٌ مُقَدَّمٌ"),
            tok("السَّلَامُ", "salam", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«peace» — the delayed mubtadaʾ; a parenthetical prayer.", "«selâm» — sonraya bırakılmış mübtedâ; duâ cümlesi.", punct=punct)]
def ta_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), fa=False, wa=False, extra=""):
    pre = "الْفَاءُ عَاطِفَةٌ، وَ" if fa else ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
    segs = ([seg("فَ" if fa else "وَ", "fa" if fa else "wa", "conj")] if (fa or wa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (fa or wa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", en + " — a feminine māḍī; the attached pronoun is its object.", tr + " — müennes mâzî; bitişik zamir mef'ûl.", punct=punct, segments=segs)

def ma_mawsul_obj(en="«what»", tr="«… -ı»"): return tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", en + " — the relative pronoun, the object.", tr + " — ism-i mevsûl, mef'ûl.")
def yasha(wa=False, punct=None): return tok("وَيَشَاءُ" if wa else "يَشَاءُ", "shaa", "verb", ([AT] if wa else []) + ["hollow-verbs", "mudari-marfu", MW], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "يَشَاءُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", ("«and» + " if wa else "") + "«He wills» — the ṣila.", ("«ve» + " if wa else "") + "«diler» — sıla.", punct=punct, segments=(wa_("يَشَاءُ", "shaa", "verb") if wa else None))

def an_nasb(obj_of, en="«to»", tr="«… -mesini»"): return tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ " + obj_of + ".", en, tr)
def mansub(full, lex, en, tr, punct=None, tags=(), hidden="هُوَ", extra=""):
    return tok(full, lex, "verb", [AN] + list(tags), "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", en + " — naṣb by an.", tr + " — en ile mansub.", punct=punct)

# ---------------------------------------------------------------- §4 عِنَايَةُ اللهِ بِالْفَتَاةِ الصَّالِحَةِ (print p. 34)
sen("s1", "She was in the guardianship of our master Zakariyyā, because of her standing with him, and in the care of God Most High;",
        "O, ona yakınlığı sebebiyle efendimiz Zekeriyyâ'nın kefâletinde ve Allah Teâlâ'nın himâyesindeydi;", [
  tok("وَكَانَتْ", "kana", "verb", [KN, "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«and she was» — kāna; its ism concealed.", "«ve o … idi» — kâne; ismi gizli.", segments=wa_("كَانَتْ", "kana", "verb")),
  tok("فِي", "fi", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«in» — the phrase is kāna's khabar.", "«-de» — câr-mecrûr kâne'nin haberi."),
  majrur("كَفَالَةِ", "kafala-care", "«the guardianship [of]»", "«kefâletinde»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[ID]),
  tok("زَكَرِيَّا", "zakariyya", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā»", "«Zekeriyyâ'nın»"),
  noun_pron("لِمَكَانَتِهَا", "makana", "لِمَكَانَتِ", "هَا", "pron-3fs", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَمَكَانَتِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«because of her standing»", "«yakınlığı sebebiyle»", tags=[HJ, ID, TA]),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«with him»", "«ona»", punct="،"),
  tok("وَفِي", "fi", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in»", "«ve … -de»", segments=wa_("فِي", "fi", "prep")),
  majrur("رِعَايَةِ", "riaya", "«the care [of]»", "«himâyesinde»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct="،"),
])
sen("s2", "so God used to honour her with fruits and produce out of their season and out of their place; she would eat of them what she wished and give away of them what she wished.",
        "Allah ona mevsimi dışında ve yeri dışında meyveler ve yemişler ikram ederdi; onlardan dilediğini yer, dilediğini hediye ederdi.", [
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«so … used to» — kāna.", "«böylece … -erdi» — kâne.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("اللهُ", "allah", "propn", [KN], "لَفْظُ الْجَلَالَةِ اسْمُ كَانَ مَرْفُوعٌ.", "«God» — kāna's ism.", "«Allah» — kâne'nin ismi."),
  tok("يُكْرِمُهَا", "akrama", "verb", [KN, MB, "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ كَانَ.", "«honour her» — the clause is kāna's khabar.", "«ona ikram ederdi» — cümle kâne'nin haberi.", segments=[seg("يُكْرِمُ", "akrama", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("بِالْأَثْمَارِ", "thamar", "noun", [HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَالْأَثْمَارِ مَجْرُورٌ.", "«with fruits»", "«meyvelerle»", segments=[seg("بِ", "bi", "prep"), seg("الْأَثْمَارِ", "thamar", "noun")]),
  tok("وَالْفَوَاكِهِ", "fakiha", "noun", [AT, JT], "الْوَاوُ عَاطِفَةٌ، وَالْفَوَاكِهِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، وَأَلْ أَعَادَتْ إِلَيْهَا الْكَسْرَةَ.", "«and produce» — a muntahā plural; the article restores its kasra.", "«ve yemişler» — müntehe'l-cumû'; harf-i târif kesreyi geri getirir.", segments=wa_("الْفَوَاكِهِ", "fakiha", "noun")),
  fi(), majrur("غَيْرِ", "ghayr", "«out of» (lit. other than)", "«dışında»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  noun_pron("أَوَانِهَا", "awan", "أَوَانِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their season»", "«mevsimi»", tags=[ID]),
  tok("وَفِي", "fi", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and out of»", "«ve … dışında»", segments=wa_("فِي", "fi", "prep")),
  majrur("غَيْرِ", "ghayr", "«other than»", "«dışında»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  noun_pron("مَكَانِهَا", "makan", "مَكَانِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their place»", "«yeri»", tags=[ID], punct="،"),
  mudari("تَأْكُلُ", "akala", "«she would eat»", "«yerdi»", tags=[HL, MB], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«of them»", "«onlardan»"),
  ma_mawsul_obj(),
  tok("تَشَاءُ", "shaa", "verb", ["hollow-verbs", "mudari-marfu", MW], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«she wished» — the ṣila.", "«dilediği» — sıla."),
  mudari("وَتَهَبُ", "wahaba", "«and give away»", "«ve hediye ederdi»", tags=[AT, MB, "mithal-verbs"], hidden="هِيَ"),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«of them»", "«onlardan»"),
  ma_mawsul_obj(),
  tok("تَشَاءُ", "shaa", "verb", ["hollow-verbs", "mudari-marfu", MW], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — صِلَةٌ.", "«she wished»", "«dilediği»", punct="."),
])
sen("s3", "«So her Lord accepted her with a gracious acceptance and made her grow up well, and put her in Zakariyyā's charge; whenever Zakariyyā entered the sanctuary to see her, he found provision with her. He said: Maryam, from where does this come to you? She said: It is from God; indeed God provides for whom He wills without reckoning» (3:37).",
        "«Rabbi onu güzel bir kabulle kabul etti, onu güzelce yetiştirdi ve Zekeriyyâ'nın himâyesine verdi; Zekeriyyâ ne zaman mihraba, onun yanına girse yanında bir rızık bulurdu. Meryem, bu sana nereden? dedi. O: Allah katındandır; şüphesiz Allah dilediğini hesapsız rızıklandırır, dedi» (3:37).", [
  *quran([
  tok("فَتَقَبَّلَهَا", "taqabbala", "verb", [AT, MB, "form-v-verbs"], "الْفَاءُ عَاطِفَةٌ، وَتَقَبَّلَ فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«so accepted her» — the pronoun is the object, fronted.", "«onu kabul etti» — zamir öne alınmış mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("تَقَبَّلَ", "taqabbala", "verb"), seg("هَا", "pron-3fs", "pron")]),
  noun_pron("رَبُّهَا", "rabb", "رَبُّ", "هَا", "pron-3fs", "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her Lord» — the doer, delayed.", "«Rabbi» — fâil.", tags=[FL, ID]),
  tok("بِقَبُولٍ", "qabul", "noun", [HJ, "maful-mutlaq"], "الْبَاءُ حَرْفُ جَرٍّ، وَقَبُولٍ مَجْرُورٌ — نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ فِي الْمَعْنَى.", "«with an acceptance» — standing for the absolute object in sense.", "«bir kabulle» — mânen mef'ûl-i mutlak yerinde.", segments=[seg("بِ", "bi", "prep"), seg("قَبُولٍ", "qabul", "noun")]),
  naat("حَسَنٍ", "hasan-good", "«gracious»", "«güzel»"),
  tok("وَأَنْبَتَهَا", "anbata", "verb", [AT, MB, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَنْبَتَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ.", "«and made her grow»", "«ve onu yetiştirdi»", segments=[seg("وَ", "wa", "conj"), seg("أَنْبَتَ", "anbata", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("نَبَاتًا", "nabat", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ مِنْ غَيْرِ لَفْظِ فِعْلِهِ (نَبَتَ).", "«a growing» — an absolute object from the base verb's maṣdar.", "«bir yetişmeyle» — mef'ûl-i mutlak; fiilin mücerredinin masdarı."),
  naat("حَسَنًا", "hasan-good", "«good»", "«güzel»", case="nasb"),
  tok("وَكَفَّلَهَا", "kaffala", "verb", [AT, MX, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَفَّلَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ أَوَّلُ.", "«and put her in the charge [of]» — two objects; hā the first.", "«ve onu … himâyesine verdi» — iki mef'ûl; hâ birincisi.", segments=[seg("وَ", "wa", "conj"), seg("كَفَّلَ", "kaffala", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("زَكَرِيَّا", "zakariyya", "propn", [MB, MX, MM, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā» — the second object.", "«Zekeriyyâ» — ikinci mef'ûl."),
  tok("كُلَّمَا", "kullama", "noun", [MF, SH], "ظَرْفُ زَمَانٍ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ (كُلَّ + مَا الْمَصْدَرِيَّةِ الظَّرْفِيَّةِ).", "«whenever» — kull + the adverbial mā.", "«ne zaman … -sa» — küll + zarfî mâ."),
  mazi("دَخَلَ", "dakhala", "«entered»", "«girse»", tags=[SH, ID], hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ كُلَّ"),
  prep_pron("عَلَيْهَا", "ala", "هَا", "pron-3fs", "«to see her» (lit. upon her)", "«onun yanına»"),
  tok("زَكَرِيَّا", "zakariyya", "propn", [FL, MM, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā» — the doer.", "«Zekeriyyâ» — fâil."),
  tok("الْمِحْرَابَ", "mihrab", "noun", [MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ (أَوْ مَفْعُولٌ فِيهِ عَلَى نَزْعِ الْخَافِضِ).", "«the sanctuary» — the object (or an adverb of place).", "«mihraba» — mef'ûl (veya mef'ûlün fîh)."),
  mazi("وَجَدَ", "wajada", "«he found»", "«bulurdu»", tags=[SH, MB, "mithal-verbs"], hidden="هُوَ", extra_ar=" — جَوَابُ كُلَّمَا"),
  noun_pron("عِنْدَهَا", "inda", "عِنْدَ", "هَا", "pron-3fs", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«with her»", "«yanında»", tags=[MF, ID]),
  maful_("رِزْقًا", "rizq", "«provision»", "«bir rızık»"),
  qala(hidden="هُوَ"),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("مَرْيَمُ", "maryam", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Maryam» — a single-name vocative, built on ḍamma.", "«Meryem» — müfred alem münâdâ, damme üzere mebnî."),
  tok("أَنَّى", "anna-istifham", "noun", [IS, MK], "اسْمُ اسْتِفْهَامٍ بِمَعْنَى مِنْ أَيْنَ، فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ (أَوْ الْحَالِ) — خَبَرٌ مُقَدَّمٌ.", "«from where» — an interrogative noun; the fronted khabar.", "«nereden» — soru ismi; öne alınmış haber."),
  tok("لَكِ", "li", "prep", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ (لِلْمُخَاطَبَةِ) فِي مَحَلِّ جَرٍّ.", "«to you» (f.)", "«sana»", segments=[seg("لَ", "li", "prep"), seg("كِ", "pron-2fs", "pron")]),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("قَالَتْ", "qala", "verb", ["hollow-verbs", MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«she said»", "«dedi»"),
  tok("هُوَ", "huwa", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«it» — the mubtadaʾ.", "«o» — mübtedâ."),
  prep("مِنْ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ الْمُبْتَدَإِ."),
  majrur("عِنْدِ", "inda", "«[the presence of]»", "«katından»", tags=[ID, MK], ar="ظَرْفٌ مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  inna(),
  tok("اللهَ", "allah", "propn", [IW], "لَفْظُ الْجَلَالَةِ اسْمُ إِنَّ مَنْصُوبٌ.", "«God» — inna's ism.", "«Allah» — inne'nin ismi."),
  mudari("يَرْزُقُ", "razaqa", "«provides for»", "«rızıklandırır»", tags=[IW, MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  tok("مَنْ", "man-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«whom»", "«… -i»"),
  yasha(),
  tok("بِغَيْرِ", "ghayr", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«without»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  mudaf_ilayh("حِسَابٍ", "hisab", "«reckoning»", "«hesap»", punct="."),
  ]),
])
# ---------------------------------------------------------------- §5 إِلْهَامٌ مِنَ الرَّبِّ الرَّحِيمِ (print p. 35)
sen("s4", "And God inspired Zakariyyā — and he was a prophet among the prophets, and one of the wise and the keen-witted — that He who can honour a righteous girl, whose mother was sincere in vowing her and praying for her, and who was herself sincere in obedience and worship, with fruits ahead of their time or behind their season,",
        "Allah Zekeriyyâ'ya — ki o peygamberlerden bir peygamber, akıllı ve zeki kimselerdendi — şunu ilham etti: annesi onu adamakta ve ona duâda ihlâslı olan, kendisi de tâat ve ibadette ihlâslı olan sâliha bir kıza, zamanından önce veya mevsiminden sonra meyvelerle ikramda bulunmaya gücü yeten,", [
  mazi("وَأَلْهَمَ", "alhama", "«and inspired»", "«ve ilham etti»", tags=[MX, "form-iv-verbs"], wa=True, hidden=None),
  allah_fail(),
  tok("زَكَرِيَّا", "zakariyya", "propn", [MB, MX, MM, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā» — the first object.", "«Zekeriyyâ'ya» — birinci mef'ûl."),
  tok("وَهُوَ", "huwa", "pron", [HL, MK, "jumla-mutarida"], "الْوَاوُ لِلْحَالِ (اعْتِرَاضٌ)، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and he» — a parenthetical ḥāl clause's mubtadaʾ.", "«ki o» — itirâzî hâl cümlesinin mübtedâsı.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("نَبِيٌّ", "nabi", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a prophet» — the khabar.", "«bir peygamber» — haber."),
  prep("مِنَ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلتَّبْعِيضِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberler»", tags=[JT], punct="،"),
  tok("وَمِنَ", "min", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَمِنَ حَرْفُ جَرٍّ.", "«and of»", "«ve … -den»", segments=wa_("مِنَ", "min", "prep")),
  majrur("الْعُقَلَاءِ", "aqil", "«the wise»", "«akıllılar»", tags=[JT]),
  naat("الْأَذْكِيَاءِ", "dhaki", "«the keen-witted»", "«zekiler»", tags=[JT], punct="،"),
  tok("أَنَّ", "anna", "part", [IW, MX], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ ثَانٍ لِأَلْهَمَ.", "«that» — the clause is the second object of «inspired».", "«… -dığını» — müevvel masdar «ilham etti»nin ikinci mef'ûlü."),
  tok("مَنْ", "man-mawsula", "pron", [IW, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«He who» — the relative pronoun, anna's ism.", "«… kimse» — ism-i mevsûl, enne'nin ismi."),
  mudari("يَقْدِرُ", "qadara", "«can»", "«gücü yeten»", tags=[MW], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  tok("أَنْ", "an-masdariyya", "part", [AN, HJ], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«to»", "«… -maya»"),
  mansub("يُكْرِمَ", "akrama", "«honour»", "«ikramda bulunmaya»", tags=[MB, "form-iv-verbs"]),
  tok("فَتَاةً", "fata-youth", "noun", [MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — فَتَاةٌ: مُؤَنَّثُ فَتًى.", "«a girl» — the object; the feminine of fatā.", "«bir kız» — mef'ûl; fetâ'nın müennesi."),
  naat("صَالِحَةً", "salih", "«righteous»", "«sâliha»", case="nasb", tags=["ism-fail"]),
  mazi_ta("أَخْلَصَتْ", "akhlasa", "«was sincere»", "«ihlâslı oldu»", tags=["jumla-sifa", "form-iv-verbs"], extra=" — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِفَتَاةً"),
  noun_pron("أُمُّهَا", "umm", "أُمُّ", "هَا", "pron-3fs", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — وَالْهَاءُ هِيَ الرَّابِطُ.", "«her mother» — the doer; its pronoun is the clause's link.", "«annesi» — fâil; zamiri cümlenin râbıtı.", tags=[FL, ID]),
  fi(), majrur("النَّذْرِ", "nadhr", "«vowing»", "«adamakta»"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«her»", "«onu»"),
  atf("وَالدُّعَاءِ", "dua", "«praying»", "«duâda»", "jarr"),
  li_pron("لَهَا", "هَا", "pron-3fs", "«for her»", "«ona»", punct="،"),
  mazi_ta("وَأَخْلَصَتْ", "akhlasa", "«and was sincere»", "«ve ihlâslı oldu»", tags=[AT, "form-iv-verbs"], wa=True),
  tok("هِيَ", "hiya", "pron", ["tawkid"], "ضَمِيرٌ مُنْفَصِلٌ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ.", "«herself» — confirming the concealed doer.", "«kendisi» — gizli zamirin te'kidi."),
  fi(), majrur("الطَّاعَةِ", "taa", "«obedience»", "«tâatte»"),
  atf("وَالْعِبَادَةِ", "ibada", "«worship»", "«ibadette»", "jarr", punct="،"),
  tok("بِفَوَاكِهَ", "fakiha", "noun", [HJ, JT, MM], "الْبَاءُ حَرْفُ جَرٍّ، وَفَوَاكِهَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (صِيغَةُ مُنْتَهَى الْجُمُوعِ) — مُتَعَلِّقٌ بِيُكْرِمَ.", "«with fruits» — jarr by fatḥa (a muntahā plural); hangs on «honour».", "«meyvelerle» — gayr-i munsarıf, fetha ile mecrûr; «ikram»a müteallik.", segments=[seg("بِ", "bi", "prep"), seg("فَوَاكِهَ", "fakiha", "noun")]),
  naat("سَابِقَةٍ", "sabiq", "«ahead [of]»", "«önce»", tags=["ism-fail"]),
  noun_pron("لِزَمَانِهَا", "zaman", "لِزَمَانِ", "هَا", "pron-3fs", "اللَّامُ حَرْفُ جَرٍّ، وَزَمَانِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their time»", "«zamanından»", tags=[HJ, ID]),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ.", "«or»", "«veya»"),
  tok("مُتَأَخِّرَةٍ", "mutaakhkhir", "noun", [AT, NA, "ism-fail", "form-v-verbs"], "مَعْطُوفٌ عَلَى سَابِقَةٍ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ تَأَخَّرَ.", "«behind» — joined to «ahead»; the participle of taʾakhkhara.", "«sonra» — «önce»ye atıf; teahhara'nın ism-i fâili."),
  prep("عَنْ", "an", "«[their season]»", "«-den»"),
  noun_pron("أَوَانِهَا", "awan", "أَوَانِ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their season»", "«mevsiminden»", tags=[HJ, ID], punct="،"),
])
sen("s5", "can grant an old man — whom age has struck, over whom grey hair has climbed, and in whom weakness has left its mark — a son, when hope had been cut off from him by advanced age and the barrenness of his wife, and custom runs that no child is born to a man in this state.",
        "yaşı ilerlemiş, saçı ağarmış, zayıflığın izini bıraktığı bir ihtiyara — yaşın ilerlemesi ve karısının kısırlığı yüzünden ümidi kesilmişken, âdet de bu haldeki bir adama çocuk doğmaması iken — bir evlât vermeye de gücü yeter.", [
  mudari("يَقْدِرُ", "qadara", "«can»", "«gücü yeter»", tags=[IW], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  an_nasb("مَفْعُولُ يَقْدِرُ (أَوْ مَجْرُورٌ بِعَلَى مُقَدَّرَةٍ)", "«to»", "«… -meye»"),
  mansub("يَهَبَ", "wahaba", "«grant»", "«vermeye»", tags=[MX, "mithal-verbs"]),
  tok("شَيْخًا", "shaykh", "noun", [MB, MX], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«an old man» — the first object.", "«bir ihtiyara» — birinci mef'ûl."),
  tok("قَدْ", "qad", "part", ["qad-harf", "jumla-sifa"], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لِشَيْخًا.", "«[already]» — the clause describes «an old man».", "«[artık]» — cümle «ihtiyar»ın sıfatı."),
  mazi("طَعَنَ", "taana", "«has been struck» (lit. has advanced)", "«ilerlemiş»", hidden="هُوَ"),
  fi(), majrur("السِّنِّ", "sinn", "«age»", "«yaşta»"),
  tok("وَعَلَاهُ", "ala-rise", "verb", [AT, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعَلَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«and has climbed over him»", "«ve üzerine çıkmış»", segments=[seg("وَ", "wa", "conj"), seg("عَلَا", "ala-rise", "verb"), pr3ms()]),
  fail("الشَّيْبُ", "shayb-greyness", "«grey hair»", "«ak saç»"),
  mazi("وَأَثَّرَ", "aththara", "«and has left its mark»", "«ve iz bırakmış»", tags=[AT, "form-ii-verbs"], wa=True, hidden=None),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in him»", "«onda»"),
  fail("الْوَهَنُ", "wahn", "«weakness»", "«zayıflık»", punct="،"),
  tok("وَلَدًا", "walad", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a son» — the second object.", "«bir evlât» — ikinci mef'ûl."),
  tok("قَدِ", "qad", "part", ["qad-harf", HL], "حَرْفُ تَحْقِيقٍ حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ حَالٌ (أَوْ نَعْتٌ).", "«when [already]» — qad with a kasra before the next hamzat al-waṣl.", "«… -mişken» — kad, iki sâkin yüzünden kesre aldı."),
  mazi("انْقَطَعَ", "inqataa", "«had been cut off»", "«kesilmişti»", tags=["form-vii-verbs"], hidden=None),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«from him»", "«ondan»"),
  fail("الرَّجَاءُ", "raja-hope", "«hope»", "«ümit»"),
  tok("لِعُلُوِّ", "uluww", "noun", [HJ, ID, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَعُلُوِّ مَجْرُورٌ، مُضَافٌ.", "«by the advance [of]»", "«ilerlemesi yüzünden»", segments=[seg("لِ", "li", "prep"), seg("عُلُوِّ", "uluww", "noun")]),
  mudaf_ilayh("السِّنِّ", "sinn", "«age»", "«yaşın»"),
  atf("وَعُقْرِ", "uqr", "«the barrenness [of]»", "«kısırlığı»", "jarr", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الزَّوْجِ", "zawj", "«the wife»", "«karısının»", punct="،"),
  tok("وَجَرَتِ", "jara", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَجَرَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and runs» — a defective māḍī; the alif dropped before the tāʾ.", "«ve câri olmuştur» — nâkıs mâzî; tâ kesre aldı.", segments=wa_("جَرَتِ", "jara", "verb")),
  fail("الْعَادَةُ", "ada", "«custom»", "«âdet»"),
  tok("أَنْ", "an-masdariyya", "part", [AN, HJ], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَرْفٍ مَحْذُوفٍ (بِأَنْ لَا…).", "«that» — the clause after an unspoken bi.", "«… -maması» — mahzuf bâ ile mecrûr."),
  la_nafiya(),
  tok("يُولَدَ", "walada", "verb", [AN, NF, "la-nafiya", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ — فِي الْمَجْهُولِ تَعُودُ الْوَاوُ: يُولَدُ.", "«is born» — a passive muḍāriʿ in naṣb; the wāw returns in the passive (yūladu).", "«doğmaması» — meçhul muzari, mansub; meçhulde vâv geri gelir.", segments=None),
  tok("لِرَجُلٍ", "rajul", "noun", [HJ, NF], "اللَّامُ حَرْفُ جَرٍّ، وَرَجُلٍ مَجْرُورٌ — نَائِبُ الْفَاعِلِ.", "«to a man» — the deputy doer.", "«bir adama» — nâib-i fâil.", segments=[seg("لِ", "li", "prep"), seg("رَجُلٍ", "rajul", "noun")]),
  fi(), ishara("هٰذِهِ", "hadhihi", "jarr", "«this»", "«bu»"),
  tok("الْحَالِ", "hal", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ — الْحَالُ تُؤَنَّثُ وَتُذَكَّرُ.", "«state» — a badal; ḥāl may be feminine or masculine.", "«hal» — bedel; hâl müennes ve müzekker olur.", punct="."),
])
sen("s6", "So his soul surged, his resolve rose, hope revived and trust in the Lord grew strong, and his tongue overflowed with a prayer to which the angels said amen and by which God's mercy was stirred; all of it was an inspiration from the Merciful Lord and a decree from the Mighty, the All-Knowing:",
        "Bunun üzerine içi coştu, himmeti yükseldi, ümit canlandı, Rabbe güven kuvvetlendi; dili, meleklerin âmin dediği ve Allah'ın rahmetini harekete geçiren bir duâ ile taştı; bunların hepsi Rahîm Rab'den bir ilham, Azîz ve Alîm'den bir takdirdi:", [
  mazi_ta("فَجَاشَتْ", "jasha", "«so surged»", "«bunun üzerine coştu»", tags=[AT, "hollow-verbs"], wa=True),
  noun_pron("نَفْسُهُ", "nafs", "نَفْسُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his soul»", "«içi»", tags=[FL, ID], punct="،"),
  tok("وَعَلَتْ", "ala-rise", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعَلَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and rose» — a defective māḍī with the feminine tāʾ: the alif dropped.", "«ve yükseldi» — nâkıs mâzî + te'nis tâ'sı: elif düştü.", segments=wa_("عَلَتْ", "ala-rise", "verb")),
  noun_pron("هِمَّتُهُ", "himma", "هِمَّتُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his resolve»", "«himmeti»", tags=[FL, ID], punct="،"),
  mazi("وَانْتَعَشَ", "intaasha", "«and revived»", "«ve canlandı»", tags=[AT, "form-viii-verbs"], wa=True, hidden=None),
  fail("الْأَمَلُ", "amal", "«hope»", "«ümit»", punct="،"),
  tok("وَقَوِيَتِ", "qawiya", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَوِيَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — قَوِيَ: نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ.", "«and grew strong» — qawiya, a defective verb of the samiʿa class.", "«ve kuvvetlendi» — kaviye, semia bâbından nâkıs.", segments=wa_("قَوِيَتِ", "qawiya", "verb")),
  fail("الثِّقَةُ", "thiqa", "«trust»", "«güven»"),
  tok("بِالرَّبِّ", "rabb", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالرَّبِّ مَجْرُورٌ.", "«in the Lord»", "«Rabbe»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الرَّبِّ", "rabb", "noun")]),
  mazi("فَفَاضَ", "fada", "«and overflowed»", "«ve taştı»", tags=[AT, "hollow-verbs"], wa=True, hidden=None),
  noun_pron("لِسَانُهُ", "lisan", "لِسَانُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his tongue»", "«dili»", tags=[FL, ID]),
  tok("بِدُعَاءٍ", "dua", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَدُعَاءٍ مَجْرُورٌ.", "«with a prayer»", "«bir duâ ile»", segments=[seg("بِ", "bi", "prep"), seg("دُعَاءٍ", "dua", "noun")]),
  mazi_ta("أَمَّنَتْ", "ammana", "«said amen»", "«âmin dedi»", tags=["jumla-sifa", "form-ii-verbs"], extra=" — وَالْجُمْلَةُ نَعْتٌ لِدُعَاءٍ"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«to it»", "«ona»"),
  fail("الْمَلَائِكَةُ", "malak", "«the angels»", "«melekler»", tags=[JT], punct="،"),
  mazi_ta("وَتَحَرَّكَتْ", "taharraka", "«and was stirred»", "«ve harekete geçti»", tags=[AT, "form-v-verbs"], wa=True),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by it»", "«onunla»"),
  fail("رَحْمَةُ", "rahma", "«the mercy [of]»", "«rahmeti»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct="،"),
  tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and was»", "«ve … idi»", segments=wa_("كَانَ", "kana", "verb")),
  noun_pron("كُلُّهُ", "kull", "كُلُّ", "هُ", "pron-3ms", "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«all of it» — kāna's ism.", "«hepsi» — kâne'nin ismi.", tags=[KN, ID]),
  tok("إِلْهَامًا", "ilham", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«an inspiration» — kāna's khabar.", "«bir ilham» — kâne'nin haberi."),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الرَّبِّ", "rabb", "«the Lord»", "«Rab'den»"),
  naat("الرَّحِيمِ", "rahim", "«the Merciful»", "«Rahîm»", punct="،"),
  atf("وَتَقْدِيرًا", "taqdir", "«a decree»", "«bir takdir»", "nasb"),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْعَزِيزِ", "aziz", "«the Mighty»", "«Azîz»"),
  naat("الْعَلِيمِ", "alim", "«the All-Knowing»", "«Alîm»", punct=":"),
])
sen("s7", "«There Zakariyyā prayed to his Lord; he said: My Lord, grant me from Yourself a goodly offspring; indeed You hear every prayer» (3:38).",
        "«Orada Zekeriyyâ Rabbine duâ etti; dedi ki: Rabbim, bana katından temiz bir soy bağışla; şüphesiz Sen duâyı işitensin» (3:38).", [
  *quran([
  tok("هُنَالِكَ", "hunalika", "noun", [MF, "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ (أَوِ الزَّمَانِ) الْبَعِيدِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ فِيهِ.", "«there» — a demonstrative adverb.", "«orada» — işâret zarfı."),
  mazi("دَعَا", "daa", "«prayed»", "«duâ etti»", tags=[MB, "naqis-verbs"], hidden=None, extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  tok("زَكَرِيَّا", "zakariyya", "propn", [FL, MM, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā» — the doer.", "«Zekeriyyâ» — fâil."),
  noun_pron("رَبَّهُ", "rabb", "رَبَّ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his Lord»", "«Rabbine»", tags=[MB, ID]),
  qala(hidden="هُوَ"),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ.", "«my Lord»", "«Rabbim»"),
  tok("هَبْ", "wahaba", "verb", [AM, MB, "mithal-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — مِثَالٌ وَاوِيٌّ سَقَطَتْ وَاوُهُ: وَهَبَ يَهَبُ هَبْ؛ وَالْأَمْرُ لِلدُّعَاءِ.", "«grant» — the imperative of the assimilated wahaba; its wāw and the waṣl alif both fall away.", "«bağışla» — misâl fiilin emri; vâvı ve vasıl elifi düşer."),
  li_pron("لِي", "ي", "pron-1s", "«me»", "«bana»"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("لَدُنْكَ", "ladun", "لَدُنْ", "كَ", "pron-2ms", "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِمِنْ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«Yourself» (lit. from before You) — a mabnī adverb in the place of jarr.", "«katından» — mebnî zarf, mahallen mecrûr.", tags=[HJ, ID, MF]),
  maful_("ذُرِّيَّةً", "dhurriyya", "«an offspring»", "«bir soy»"),
  naat("طَيِّبَةً", "tayyib", "«goodly»", "«temiz»", case="nasb"),
  tok("إِنَّكَ", "inna", "part", [IW], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا.", "«indeed You»", "«şüphesiz Sen»", segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  khabar_inna("سَمِيعُ", "sami", "«the Hearer [of]»", "«işitensin»", tags=[ID], extra="، مُضَافٌ"),
  mudaf_ilayh("الدُّعَاءِ", "dua", "«prayer»", "«duâyı»", punct="."),
  ]),
])
# ---------------------------------------------------------------- §6 بِشَارَةُ وَلَدٍ (print p. 36)
sen("s8", "And God answered his prayer, and the glad tidings came to him of a righteous son whose birth-time had drawn near.",
        "Allah duâsına icabet etti; doğum zamanı yaklaşmış sâlih bir evlât müjdesi ona yöneldi.", [
  mazi("وَأَجَابَ", "ajaba", "«and answered»", "«ve icabet etti»", tags=[MB, "hollow-verbs", "form-iv-verbs"], wa=True, hidden=None),
  allah_fail(),
  noun_pron("دُعَاءَهُ", "dua", "دُعَاءَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his prayer»", "«duâsına»", tags=[MB, ID], punct="،"),
  mazi_ta("وَتَوَجَّهَتْ", "tawajjaha", "«and came» (lit. turned)", "«ve yöneldi»", tags=[AT, "form-v-verbs"], wa=True),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him»", "«ona»"),
  fail("الْبِشَارَةُ", "bishara", "«the glad tidings»", "«müjde»"),
  tok("بِوَلَدٍ", "walad", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَوَلَدٍ مَجْرُورٌ.", "«of a son»", "«bir evlât»", segments=[seg("بِ", "bi", "prep"), seg("وَلَدٍ", "walad", "noun")]),
  naat("صَالِحٍ", "salih", "«righteous»", "«sâlih»", tags=["ism-fail"]),
  mazi("قَرُبَ", "qaruba", "«had drawn near»", "«yaklaşmış»", tags=["jumla-sifa"], hidden=None, extra_ar=" — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِوَلَدٍ؛ قَرُبَ مِنْ بَابِ كَرُمَ"),
  fail("زَمَانُ", "zaman", "«the time [of]»", "«zamanı»", tags=[ID], extra_ar="، مُضَافٌ"),
  noun_pron("وِلَادَتِهِ", "wilada", "وِلَادَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his birth»", "«doğum»", tags=[ID], punct="."),
])
sen("s9", "And man was created of haste, so he asked for a token of the possibility of this great event and the nearness of its appearance, and said:",
        "İnsan aceleden yaratılmıştır; o da bu büyük olayın mümkün olduğuna ve ortaya çıkmasının yakınlığına bir alâmet istedi ve dedi:", [
  tok("وَخُلِقَ", "khalaqa", "verb", [NF], "الْوَاوُ لِلِاسْتِئْنَافِ، وَخُلِقَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and was created» — a passive.", "«ve yaratıldı» — meçhul.", segments=wa_("خُلِقَ", "khalaqa", "verb")),
  tok("الْإِنْسَانُ", "insan", "noun", [NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«man» — the deputy doer.", "«insan» — nâib-i fâil."),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("عَجَلٍ", "ajal-haste", "«haste»", "«acele»", punct="،"),
  mazi("فَطَلَبَ", "talaba", "«so he asked for»", "«o da istedi»", tags=[AT, MB], wa=True, hidden="هُوَ"),
  maful_("أَمَارَةً", "amara", "«a token»", "«bir alâmet»"),
  prep("عَلَى", "ala", "«of»", "«-e»"),
  majrur("إِمْكَانِ", "imkan", "«the possibility [of]»", "«mümkün olduğuna»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  ishara("هٰذَا", "hadha", "jarr", "«this»", "«bu»"),
  tok("الْحَدَثِ", "hadath", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«event» — a badal.", "«olayın» — bedel."),
  naat("الْكَبِيرِ", "kabir", "«great»", "«büyük»"),
  atf("وَقُرْبِ", "qurb", "«the nearness [of]»", "«ve yakınlığına»", "jarr", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  noun_pron("ظُهُورِهِ", "zuhur", "ظُهُورِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its appearance»", "«ortaya çıkmasının»", tags=[ID], punct="،"),
  qala("فَقَالَ", wa=True, hidden="هُوَ"),
])
sen("s10", "«My Lord, appoint me a sign. He said: Your sign is that you shall not speak to people for three days except by gesture; and remember your Lord much, and glorify Him in the evening and the early morning» (3:41).",
        "«Rabbim, bana bir alâmet ver. Buyurdu ki: Senin alâmetin, üç gün insanlarla işaretten başka türlü konuşamamandır; Rabbini çok an, akşam sabah O'nu tesbih et» (3:41).", [
  *quran([
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ.", "«my Lord»", "«Rabbim»"),
  tok("اجْعَلْ", "jaala", "verb", [AM, MX], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — لِلدُّعَاءِ.", "«appoint» — an imperative of supplication.", "«ver, kıl» — duâ emri."),
  li_pron("لِي", "ي", "pron-1s", "«me»", "«bana»"),
  maful_("آيَةً", "aya", "«a sign»", "«bir alâmet»", punct="."),
  qala(hidden="هُوَ"),
  noun_pron("آيَتُكَ", "aya", "آيَتُ", "كَ", "pron-2ms", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your sign» — the mubtadaʾ.", "«senin alâmetin» — mübtedâ.", tags=[MK, ID]),
  tok("أَلَّا", "an-masdariyya", "part", [AN, "la-nafiya", MK], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَلَا نَافِيَةٌ، أُدْغِمَتِ النُّونُ فِي اللَّامِ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْمُبْتَدَإِ.", "«that … not» — an fused with the negating lā; the clause is the khabar.", "«… -maman» — en + nefiy lâ'sı; müevvel masdar haber."),
  tok("تُكَلِّمَ", "kallama", "verb", [AN, MB, "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«you shall speak to»", "«konuşaman»"),
  maful_("النَّاسَ", "nas", "«people»", "«insanlarla»"),
  tok("ثَلَاثَةَ", "thalatha", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ (نَائِبُ ظَرْفٍ)، مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى الْجَمْعِ.", "«three» — a time adverb, annexed to its counted plural.", "«üç» — zaman zarfı; ma'dûduna muzâf."),
  mudaf_ilayh("أَيَّامٍ", "yawm", "«days»", "«gün»", tags=[JT, "tamyiz"]),
  tok("إِلَّا", "illa", "part", ["istithna", "istithna-mufarragh"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except»", "«ancak»"),
  tok("رَمْزًا", "ramz", "noun", [HL, "istithna"], "حَالٌ مَنْصُوبٌ (أَيْ: مُشِيرًا) أَوْ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«by gesture» — a ḥāl (i.e. gesturing).", "«işaretle» — hâl.", punct="."),
  tok("وَاذْكُرْ", "dhakara", "verb", [AT, AM, MB], "الْوَاوُ عَاطِفَةٌ، وَاذْكُرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and remember»", "«ve an»", segments=wa_("اذْكُرْ", "dhakara", "verb")),
  noun_pron("رَبَّكَ", "rabb", "رَبَّ", "كَ", "pron-2ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord»", "«Rabbini»", tags=[MB, ID]),
  tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ: ذِكْرًا كَثِيرًا.", "«much» — stands for the absolute object (a quality of the unspoken maṣdar).", "«çok» — mef'ûl-i mutlak yerinde."),
  tok("وَسَبِّحْ", "sabbaha", "verb", [AT, AM, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَسَبِّحْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and glorify»", "«ve tesbih et»", segments=wa_("سَبِّحْ", "sabbaha", "verb")),
  tok("بِالْعَشِيِّ", "ashiyy", "noun", [HJ, MF], "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى فِي، وَالْعَشِيِّ مَجْرُورٌ.", "«in the evening»", "«akşamleyin»", segments=[seg("بِ", "bi", "prep"), seg("الْعَشِيِّ", "ashiyy", "noun")]),
  atf("وَالْإِبْكَارِ", "ibkar", "«the early morning»", "«sabahleyin»", "jarr", punct="."),
  ]),
])
sen("s11", "So the Powerful One who can strip things of their properties, and make the speaking tongue dumb, unable to move with a word, can deposit in whichever of His creatures He wills whatever properties He wills;",
        "Şu halde eşyanın hususiyetlerini soyup alabilen, konuşan dili tek kelime kımıldayamayan dilsiz bir dil kılabilen Kadir, yaratıklarından dilediğine dilediği hususiyetleri emanet edebilir;", [
  tok("فَالْقَادِرُ", "qadir", "noun", [AT, MK, "ism-fail"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْقَادِرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the Powerful One» — the mubtadaʾ.", "«şu halde Kadir» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الْقَادِرُ", "qadir", "noun")]),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ.", "«who» — the relative pronoun, a naʿt.", "«ki o» — ism-i mevsûl, sıfat."),
  mudari("يَسْتَطِيعُ", "istataa", "«can»", "«-ebilen»", tags=[MW, "hollow-verbs", "form-x-verbs", MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  an_nasb("مَفْعُولُ يَسْتَطِيعُ"),
  mansub("يَسْلُبَ", "salaba", "«strip»", "«soyup almayı»", tags=[MX]),
  tok("خَوَاصَّ", "khassa-property", "noun", [MB, MX, JT, MM], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — جَمْعُ خَاصَّةٍ، صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«the properties [of]» — the first object; a muntahā plural.", "«hususiyetlerini» — birinci mef'ûl; müntehe'l-cumû'."),
  mudaf_ilayh("الْأَشْيَاءِ", "shay", "«things»", "«eşyanın»", tags=[JT, MM], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — أَشْيَاءُ مَمْنُوعٌ مِنَ الصَّرْفِ، وَأَلْ أَعَادَتِ الْكَسْرَةَ.", punct="،"),
  tok("فَيَجْعَلَ", "jaala", "verb", [AT, AN, MX], "الْفَاءُ عَاطِفَةٌ، وَيَجْعَلَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَسْلُبَ.", "«and make» — naṣb by being joined to «strip».", "«ve kılmayı» — atıfla mansub.", segments=[seg("فَ", "fa", "conj"), seg("يَجْعَلَ", "jaala", "verb")]),
  tok("اللِّسَانَ", "lisan", "noun", [MB, MX], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«the tongue» — the first object.", "«dili» — birinci mef'ûl."),
  naat("النَّاطِقَ", "natiq", "«speaking»", "«konuşan»", case="nasb", tags=["ism-fail"]),
  tok("أَبْكَمَ", "abkam", "noun", [MB, MX, MM], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَفْعَلُ الصِّفَةِ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«dumb» — the second object; the afʿal of defect, a diptote.", "«dilsiz» — ikinci mef'ûl; ef'al vezni, gayr-i munsarıf."),
  la_nafiya(),
  neg_mudari("يَسْتَطِيعُ", "istataa", "«unable»", "«-amayan»", hidden="هُوَ", extra=" — وَالْجُمْلَةُ نَعْتٌ لِأَبْكَمَ", tags=["jumla-sifa", "hollow-verbs", "form-x-verbs"]),
  an_nasb("مَفْعُولُ يَسْتَطِيعُ"),
  mansub("يَتَحَرَّكَ", "taharraka", "«move»", "«kımıldamayı»", tags=["form-v-verbs"]),
  tok("بِكَلِمَةٍ", "kalima", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَكَلِمَةٍ مَجْرُورٌ.", "«with a word»", "«bir kelimeyle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("كَلِمَةٍ", "kalima", "noun")]),
  mudari("يَسْتَطِيعُ", "istataa", "«can»", "«-ebilir»", tags=[MK, "hollow-verbs", "form-x-verbs", MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ"),
  an_nasb("مَفْعُولُ يَسْتَطِيعُ"),
  mansub("يُودِعَ", "awdaa", "«deposit»", "«emanet etmeyi»", tags=[MX, "mithal-verbs", "form-iv-verbs"], extra=" — أَوْدَعَ: مِثَالٌ وَاوِيٌّ مِنْ بَابِ الْإِفْعَالِ تَثْبُتُ وَاوُهُ"),
  ma_mawsul_obj("«whichever»", "«dilediğine»"),
  mazi("شَاءَ", "shaa", "«He wills»", "«diledi»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  noun_pron("مَخْلُوقَاتِهِ", "makhluq", "مَخْلُوقَاتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«His creatures»", "«yaratıklarından»", tags=[HJ, ID, JM]),
  ma_mawsul_obj("«whatever»", "«dilediğini»"),
  mazi("شَاءَ", "shaa", "«He wills»", "«diledi»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  tok("خَوَاصَّ", "khassa-property", "noun", [HJ, JT, MM], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«properties» — jarr by fatḥa (a diptote).", "«hususiyetler» — gayr-i munsarıf, fetha ile mecrûr.", punct="،"),
])
sen("s12", "and the Strong One who can withhold can give.",
        "ve vermemeye gücü yeten Kavî, vermeye de gücü yeter.", [
  tok("وَالْقَوِيُّ", "qawi", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْقَوِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the Strong One» — the mubtadaʾ.", "«ve Kavî» — mübtedâ.", segments=wa_("الْقَوِيُّ", "qawi", "noun")),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ.", "«who»", "«ki o»"),
  mudari("يَسْتَطِيعُ", "istataa", "«can»", "«gücü yeten»", tags=[MW, "hollow-verbs", "form-x-verbs", MB], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  an_nasb("مَفْعُولُ يَسْتَطِيعُ"),
  mansub("يَمْنَعَ", "manaa", "«withhold»", "«vermemeyi»"),
  mudari("يَسْتَطِيعُ", "istataa", "«can»", "«gücü yeter»", tags=[MK, "hollow-verbs", "form-x-verbs", MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ"),
  an_nasb("مَفْعُولُ يَسْتَطِيعُ"),
  tok("يُعْطِيَ", "ata-give", "verb", [AN, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«give» — naṣb by an; the fatḥa shows on the yāʾ.", "«vermeyi» — en ile mansub; fetha yâ üzerinde görünür.", punct="."),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: hasan-good, ajal-haste, kafala-care take suffixed keys; anna-istifham, tayyib, khassa-property, ala-rise, wahaba (هَبْ) reused)
CAND = {
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "kafala-care": G("kafala-care", "كَفَالَة", "ك ف ل", "noun", "guardianship, care", "kefâlet, himâye", 2),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "zakariyya": G("zakariyya", "زَكَرِيَّا", None, "propn", "Zakariyyā (Zechariah)", "Zekeriyyâ", 1),
 "makana": G("makana", "مَكَانَة", "ك و ن", "noun", "standing, position", "mevki, yakınlık, makam", 2),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "riaya": G("riaya", "رِعَايَة", "ر ع ي", "noun", "care, protection", "himâye, gözetme", 2),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "akrama": G("akrama", "أَكْرَمَ", "ك ر م", "verb", "to honour (Form IV)", "ikram etmek (if'âl)", 1),
 "thamar": G("thamar", "ثَمَر", "ث م ر", "noun", "fruit", "meyve", 1, plural="أَثْمَار"),
 "fakiha": G("fakiha", "فَاكِهَة", "ف ك ه", "noun", "fruit, produce", "meyve, yemiş", 1, plural="فَوَاكِه"),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka; gayri, -sız", 1),
 "awan": G("awan", "أَوَان", "أ و ن", "noun", "the proper time, season", "vakit, mevsim", 2),
 "makan": G("makan", "مَكَان", "ك و ن", "noun", "a place", "yer, mekân", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will (hollow, hamzated)", "dilemek (ecvef, mehmûz)", 1),
 "wahaba": G("wahaba", "وَهَبَ", "و ه ب", "verb", "to give, to grant (an assimilated verb)", "bağışlamak, vermek (misâl)", 1),
 "taqabbala": G("taqabbala", "تَقَبَّلَ", "ق ب ل", "verb", "to accept (Form V)", "kabul etmek (tefa''ul)", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "qabul": G("qabul", "قَبُول", "ق ب ل", "noun", "acceptance", "kabul", 1),
 "hasan-good": G("hasan-good", "حَسَن", "ح س ن", "noun", "good, gracious, fine", "güzel, iyi", 1),
 "anbata": G("anbata", "أَنْبَتَ", "ن ب ت", "verb", "to make grow (Form IV)", "yetiştirmek, bitirmek (if'âl)", 2),
 "nabat": G("nabat", "نَبَات", "ن ب ت", "noun", "growth; a plant", "bitki; yetişme", 1),
 "kaffala": G("kaffala", "كَفَّلَ", "ك ف ل", "verb", "to put (someone) in the charge of (Form II, two objects)", "birinin himâyesine vermek (tef'îl, iki mef'ûl)", 3),
 "kullama": G("kullama", "كُلَّمَا", None, "noun", "whenever", "her ne zaman … -sa", 1),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "mihrab": G("mihrab", "مِحْرَاب", "ح ر ب", "noun", "a sanctuary, a prayer niche", "mihrap, mâbet", 2),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find (an assimilated verb)", "bulmak (misâl)", 1),
 "inda": G("inda", "عِنْدَ", None, "noun", "with, at, in the presence of", "yanında, katında", 1),
 "rizq": G("rizq", "رِزْق", "ر ز ق", "noun", "provision", "rızık", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "anna-istifham": G("anna-istifham", "أَنَّى", None, "noun", "from where, how (an interrogative)", "nereden, nasıl (soru)", 2),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "pron-2fs": G("pron-2fs", "كِ", None, "pron", "you / your (f. sg.)", "seni / senin (müennes)", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "razaqa": G("razaqa", "رَزَقَ", "ر ز ق", "verb", "to provide for, to grant", "rızıklandırmak, vermek", 1),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "whoever, he who", "kim ki, … kimse", 1),
 "hisab": G("hisab", "حِسَاب", "ح س ب", "noun", "reckoning", "hesap", 1),
 "alhama": G("alhama", "أَلْهَمَ", "ل ه م", "verb", "to inspire (Form IV)", "ilham etmek (if'âl)", 2),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "aqil": G("aqil", "عَاقِل", "ع ق ل", "noun", "wise, rational (an active participle)", "akıllı (ism-i fâil)", 1, plural="عُقَلَاء"),
 "dhaki": G("dhaki", "ذَكِيّ", "ذ ك و", "noun", "keen-witted, intelligent", "zeki", 2, plural="أَذْكِيَاء"),
 "anna": G("anna", "أَنَّ", None, "part", "that", "-dığını", 1),
 "qadara": G("qadara", "قَدَرَ", "ق د ر", "verb", "to be able; to have power over", "güç yetirmek, muktedir olmak", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "fata-youth": G("fata-youth", "فَتًى", "ف ت ي", "noun", "a young man (a maqṣūr noun); fatāt a girl", "genç, delikanlı (maksûr); fetât kız", 1, plural="فِتْيَان"),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous (an active participle)", "sâlih (ism-i fâil)", 1),
 "akhlasa": G("akhlasa", "أَخْلَصَ", "خ ل ص", "verb", "to be sincere (Form IV)", "ihlâslı olmak (if'âl)", 2),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "nadhr": G("nadhr", "نَذْر", "ن ذ ر", "noun", "a vow", "adak, nezir", 2),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "a prayer, supplication", "duâ", 1),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it (f.)", "o (müennes)", 1),
 "taa": G("taa", "طَاعَة", "ط و ع", "noun", "obedience", "tâat, itaat", 1, plural="طَاعَات"),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet", 1),
 "sabiq": G("sabiq", "سَابِق", "س ب ق", "noun", "preceding, ahead (an active participle)", "önceki, öne geçen (ism-i fâil)", 2),
 "zaman": G("zaman", "زَمَان", "ز م ن", "noun", "time", "zaman", 1),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya", 1),
 "mutaakhkhir": G("mutaakhkhir", "مُتَأَخِّر", "أ خ ر", "noun", "late, behind (an active participle of Form V)", "gecikmiş, sonraki (tefa''ul ism-i fâili)", 2),
 "an": G("an", "عَنْ", None, "prep", "from, away from", "-den", 1),
 "shaykh": G("shaykh", "شَيْخ", "ش ي خ", "noun", "an old man; a shaykh", "ihtiyar; şeyh", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "taana": G("taana", "طَعَنَ", "ط ع ن", "verb", "to stab; (fī l-sinn) to advance in age", "saplamak; (yaşta) ilerlemek", 3),
 "sinn": G("sinn", "سِنّ", "س ن ن", "noun", "age; a tooth", "yaş; diş", 1),
 "ala-rise": G("ala-rise", "عَلَا", "ع ل و", "verb", "to rise, to climb over (defective)", "yükselmek, üstüne çıkmak (nâkıs)", 2),
 "shayb-greyness": G("shayb-greyness", "شَيْب", "ش ي ب", "noun", "grey hair, old age", "ak saç, ihtiyarlık", 2),
 "aththara": G("aththara", "أَثَّرَ", "أ ث ر", "verb", "to leave a mark, to affect (Form II)", "iz bırakmak, etkilemek (tef'îl)", 2),
 "wahn": G("wahn", "وَهْن", "و ه ن", "noun", "weakness", "zayıflık", 2),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child, a son", "evlât, çocuk", 1, plural="أَوْلَاد"),
 "inqataa": G("inqataa", "اِنْقَطَعَ", "ق ط ع", "verb", "to be cut off (Form VII)", "kesilmek (infiâl)", 2),
 "raja-hope": G("raja-hope", "رَجَاء", "ر ج و", "noun", "hope, expectation", "ümit, beklenti", 2),
 "uluww": G("uluww", "عُلُوّ", "ع ل و", "noun", "height; advance (of age)", "yükseklik; (yaşın) ilerlemesi", 2),
 "uqr": G("uqr", "عُقْر", "ع ق ر", "noun", "barrenness", "kısırlık", 3),
 "zawj": G("zawj", "زَوْج", "ز و ج", "noun", "a spouse (husband or wife)", "eş (koca veya karı)", 1),
 "jara": G("jara", "جَرَى", "ج ر ي", "verb", "to run, to flow; (al-ʿāda) to be the custom (defective)", "akmak, cereyan etmek (nâkıs)", 1),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "custom, habit", "âdet", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to give birth (an assimilated verb)", "doğurmak (misâl fiil)", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu", 1),
 "hal": G("hal", "حَال", "ح و ل", "noun", "a state, a condition", "hal, durum", 1),
 "jasha": G("jasha", "جَاشَ", "ج ي ش", "verb", "to surge, to seethe (hollow)", "coşmak, kaynamak (ecvef)", 3),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "a soul, a self", "nefis, can; kendi", 1),
 "himma": G("himma", "هِمَّة", "ه م م", "noun", "resolve, aspiration", "himmet", 2),
 "intaasha": G("intaasha", "اِنْتَعَشَ", "ن ع ش", "verb", "to revive (Form VIII)", "canlanmak (iftiâl)", 3),
 "amal": G("amal", "أَمَل", "أ م ل", "noun", "hope", "ümit, emel", 1),
 "qawiya": G("qawiya", "قَوِيَ", "ق و ي", "verb", "to grow strong (defective)", "kuvvetlenmek (nâkıs)", 2),
 "thiqa": G("thiqa", "ثِقَة", "و ث ق", "noun", "trust, confidence", "güven", 1),
 "fada": G("fada", "فَاضَ", "ف ي ض", "verb", "to overflow (hollow)", "taşmak (ecvef)", 2),
 "lisan": G("lisan", "لِسَان", "ل س ن", "noun", "a tongue", "dil", 1),
 "ammana": G("ammana", "أَمَّنَ", "أ م ن", "verb", "to say amen (Form II)", "âmin demek (tef'îl)", 3),
 "malak": G("malak", "مَلَك", "م ل ك", "noun", "an angel", "melek", 1, plural="مَلَائِكَة"),
 "taharraka": G("taharraka", "تَحَرَّكَ", "ح ر ك", "verb", "to move, to be stirred (Form V)", "harekete geçmek, kımıldamak (tefa''ul)", 2),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "ilham": G("ilham", "إِلْهَام", "ل ه م", "noun", "inspiration", "ilham", 2),
 "rahim": G("rahim", "الرَّحِيم", "ر ح م", "noun", "the Merciful", "Rahîm", 1),
 "taqdir": G("taqdir", "تَقْدِير", "ق د ر", "noun", "a decree; estimation", "takdir", 2),
 "aziz": G("aziz", "عَزِيز", "ع ز ز", "noun", "mighty; dear", "azîz, güçlü; değerli", 1),
 "alim": G("alim", "عَلِيم", "ع ل م", "noun", "all-knowing", "her şeyi bilen", 1),
 "hunalika": G("hunalika", "هُنَالِكَ", None, "noun", "there (a demonstrative of distant place)", "orada, işte orada (uzak mekân işâreti)", 2),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call; to pray (defective)", "çağırmak; duâ etmek (nâkıs)", 1),
 "ladun": G("ladun", "لَدُنْ", None, "noun", "at, from before (a mabnī adverb)", "katında, nezdinde (mebnî zarf)", 3),
 "dhurriyya": G("dhurriyya", "ذُرِّيَّة", "ذ ر ر", "noun", "offspring, progeny", "soy, zürriyet", 2),
 "tayyib": G("tayyib", "طَيِّب", "ط ي ب", "noun", "good, goodly, pure", "temiz, hoş", 1),
 "sami": G("sami", "سَمِيع", "س م ع", "noun", "all-hearing", "her şeyi işiten", 1),
 "ajaba": G("ajaba", "أَجَابَ", "ج و ب", "verb", "to answer (Form IV, hollow)", "cevap vermek, icabet etmek (if'âl, ecvef)", 1),
 "tawajjaha": G("tawajjaha", "تَوَجَّهَ", "و ج ه", "verb", "to turn toward (Form V)", "yönelmek (tefa''ul)", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "bishara": G("bishara", "بِشَارَة", "ب ش ر", "noun", "glad tidings", "müjde", 2),
 "qaruba": G("qaruba", "قَرُبَ", "ق ر ب", "verb", "to draw near (the karuma class)", "yaklaşmak (kerume bâbı)", 1),
 "wilada": G("wilada", "وِلَادَة", "و ل د", "noun", "birth", "doğum", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1),
 "insan": G("insan", "إِنْسَان", "أ ن س", "noun", "a human being", "insan", 1),
 "ajal-haste": G("ajal-haste", "عَجَل", "ع ج ل", "noun", "haste", "acele", 2),
 "talaba": G("talaba", "طَلَبَ", "ط ل ب", "verb", "to ask for, to seek", "istemek, aramak", 1),
 "amara": G("amara", "أَمَارَة", "أ م ر", "noun", "a token, a sign", "alâmet, emâre", 2),
 "imkan": G("imkan", "إِمْكَان", "م ك ن", "noun", "possibility", "imkân", 2),
 "hadath": G("hadath", "حَدَث", "ح د ث", "noun", "an event", "olay, hâdise", 2),
 "kabir": G("kabir", "كَبِير", "ك ب ر", "noun", "big, great", "büyük", 1),
 "qurb": G("qurb", "قُرْب", "ق ر ب", "noun", "nearness", "yakınlık", 1),
 "zuhur": G("zuhur", "ظُهُور", "ظ ه ر", "noun", "appearance", "ortaya çıkma, zuhur", 2),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make, to appoint", "kılmak, yapmak", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, alâmet", 1, plural="آيَات"),
 "kallama": G("kallama", "كَلَّمَ", "ك ل م", "verb", "to speak to (Form II)", "konuşmak, söz söylemek (tef'îl)", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "thalatha": G("thalatha", "ثَلَاثَة", "ث ل ث", "noun", "three (with a masculine counted noun)", "üç (müzekker ma'dûd ile)", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "ramz": G("ramz", "رَمْز", "ر م ز", "noun", "a gesture, a sign", "işaret, remiz", 2),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to remember, to mention", "anmak, zikretmek", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "much, many", "çok", 1),
 "sabbaha": G("sabbaha", "سَبَّحَ", "س ب ح", "verb", "to glorify (Form II)", "tesbih etmek (tef'îl)", 1),
 "ashiyy": G("ashiyy", "عَشِيّ", "ع ش و", "noun", "the evening", "akşam", 2),
 "ibkar": G("ibkar", "إِبْكَار", "ب ك ر", "noun", "the early morning", "sabahın erken vakti", 3),
 "qadir": G("qadir", "قَادِر", "ق د ر", "noun", "powerful, able (an active participle)", "kadir, gücü yeten (ism-i fâil)", 1),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which (m.)", "ki o, -an", 1),
 "istataa": G("istataa", "اِسْتَطَاعَ", "ط و ع", "verb", "to be able (Form X, hollow)", "gücü yetmek, -ebilmek (istif'âl, ecvef)", 1),
 "salaba": G("salaba", "سَلَبَ", "س ل ب", "verb", "to strip away, to take away", "soyup almak, selbetmek", 2),
 "khassa-property": G("khassa-property", "خَاصَّة", "خ ص ص", "noun", "a property, a peculiarity", "hususiyet, hâssa", 2, plural="خَوَاصّ"),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "natiq": G("natiq", "نَاطِق", "ن ط ق", "noun", "speaking (an active participle)", "konuşan (ism-i fâil)", 2),
 "abkam": G("abkam", "أَبْكَم", "ب ك م", "noun", "dumb, mute (the afʿal of defect)", "dilsiz (kusur ef'ali)", 2),
 "kalima": G("kalima", "كَلِمَة", "ك ل م", "noun", "a word", "kelime", 1, plural="كَلِمَات"),
 "awdaa": G("awdaa", "أَوْدَعَ", "و د ع", "verb", "to deposit, to entrust (Form IV, assimilated)", "emanet etmek, tevdî etmek (if'âl, misâl)", 3),
 "makhluq": G("makhluq", "مَخْلُوق", "خ ل ق", "noun", "a creature (a passive participle)", "yaratık, mahlûk (ism-i mef'ûl)", 1, plural="مَخْلُوقَات"),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1),
 "manaa": G("manaa", "مَنَعَ", "م ن ع", "verb", "to withhold, to prevent", "vermemek, engellemek", 1),
 "ata-give": G("ata-give", "أَعْطَى", "ع ط و", "verb", "to give (Form IV, defective)", "vermek (if'âl, nâkıs)", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "kaffala", _sg.derived(_sg.B2, _sg.W2, "ُ", "كَفَّل", "كَفِّل", "كَفِّل", "تَكْفِيل", "مُكَفِّل", "مُكَفَّل", "كُفِّلَ", "يُكَفَّلُ", "كَفَّلَهُ فُلَانًا: جَعَلَهُ كَافِلًا لَهُ — يَتَعَدَّى إِلَى مَفْعُولَيْنِ."))
put_morph(mo, "taana", _sg.sound1("fataha", "طَعَن", "طْعَن", "اِطْعَن", "طَعْن", "طَاعِن", "مَطْعُون", "طُعِنَ", "يُطْعَنُ", "طَعَنَ فِي السِّنِّ: كَبِرَ وَتَقَدَّمَ فِيهَا؛ وَطَعَنَهُ بِالرُّمْحِ: ضَرَبَهُ بِهِ."))
put_morph(mo, "aththara", _sg.derived(_sg.B2, _sg.W2, "ُ", "أَثَّر", "أَثِّر", "أَثِّر", "تَأْثِير", "مُؤَثِّر", "مُؤَثَّر فِيهِ", None, None, "أَثَّرَ فِيهِ: تَرَكَ فِيهِ أَثَرًا."))
put_morph(mo, "jasha", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "جَاش", "جِش", "جِيش", "جِش", "جِيش", "جِش", "جَيَشَان", "جَائِش", None, None, None, "جَاشَتْ نَفْسُهُ: ثَارَتْ وَفَاضَتْ — أَجْوَفُ يَائِيٌّ؛ لَمْ تَجِشْ."))
put_morph(mo, "intaasha", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَعَش", "نْتَعِش", "اِنْتَعِش", "اِنْتِعَاش", "مُنْتَعِش", None, None, None, "اِنْتَعَشَ: نَهَضَ وَعَادَتْ إِلَيْهِ قُوَّتُهُ."))
put_morph(mo, "qawiya", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ يَائِيٌّ", _sg.BABS["samia"][1], "قُوَّة", "قَوِيّ", _sg.mazi_naqis_kasra("قَوِ", "قَوُوا"), _sg.mudari_naqis("َ", "قْو", "a"), _sg.amr_naqis("اِقْو", "a"), "يَقْوَى", "يَقْوَ", "تَقْوَ", None, None, None, "قَوِيَ يَقْوَى: اشْتَدَّ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ؛ قَوِيَتْ."))
put_morph(mo, "ammana", _sg.derived(_sg.B2, _sg.W2, "ُ", "أَمَّن", "أَمِّن", "أَمِّن", "تَأْمِين", "مُؤَمِّن", "مُؤَمَّن عَلَيْهِ", None, None, "أَمَّنَ عَلَى الدُّعَاءِ: قَالَ آمِينَ."))
put_morph(mo, "awdaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَوْدَع", "وْدِع", "أَوْدِع", "إِيدَاع", "مُودِع", "مُودَع", "أُودِعَ", "يُودَعُ", "أَوْدَعَهُ الشَّيْءَ: جَعَلَهُ وَدِيعَةً عِنْدَهُ — مِثَالٌ وَاوِيٌّ تَثْبُتُ وَاوُهُ فِي بَابِ الْإِفْعَالِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch21 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 21 (print pp. 34–37): God's care for the righteous girl, with 3:37 (s1–s3); the inspiration of the Merciful Lord, with 3:38 (s4–s7); the glad tidings of a son and the sign of silence, with 3:41 (s8–s12)."
ADD_TR = " Yirmi birinci bölüm (baskı s. 34–37): Allah'ın sâliha kıza inâyeti, 3:37 ile (s1–s3); Rahîm Rab'den ilham, 3:38 ile (s4–s7); bir evlât müjdesi ve susma alâmeti, 3:41 ile (s8–s12)."
write_out(21, S, TITLE, ADD_EN, ADD_TR, "Zakariyyā §4–6", GLOSS_ADD, notes=(), related=())
report(21, S, GLOSS_ADD, ())
