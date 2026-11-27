# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 23: «قِصَّةُ عِيسَى» — the story of ʿĪsā opens: §1 (a story that breaks the ordinary course, with 36:82, 59:24, 3:59),
§2 (a matter wholly wondrous); print pp. 39–40.
python3 tools/authoring/author_qisas4_ch23.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: قِصَّةٌ خَارِقَةٌ لِلْعَادَةِ", "en": "The story of ʿĪsā: a story that breaks the ordinary course", "tr": "Îsâ'nın kıssası: âdeti aşan bir kıssa"}
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

def ka_prep(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [HJ] + list(tags), "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ.", "«like» + " + en, "«gibi» + " + tr, punct=punct, segments=[seg("كَ", "ka", "prep"), seg(full[2:], lex, "noun")])

# ---------------------------------------------------------------- §1 قِصَّةٌ خَارِقَةٌ لِلْعَادَةِ (print p. 39)
sen("s1", "And now comes the turn of our master ʿĪsā — he is the last of the messengers before our Prophet Muḥammad, the Messenger of God, may God bless him and grant him peace —",
        "Şimdi sıra efendimiz Îsâ'ya gelir — o, Peygamberimiz Muhammed Resûlullah'tan (s.a.v.) önceki son resuldür —", [
  mudari("وَيَجِيءُ", "jaa", "«and comes»", "«ve gelir»", tags=["hollow-verbs"], hidden=None),
  fail("دَوْرُ", "dawr", "«the turn [of]»", "«sırası»", tags=[ID], extra_ar="، مُضَافٌ"),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[ID]),
  tok("عِيسَى", "isa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«ʿĪsā» — a foreign maqṣūr name.", "«Îsâ'nın» — yabancı maksûr özel isim.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [HL, MK, "jumla-mutarida"], "الْوَاوُ لِلْحَالِ (اعْتِرَاضٌ)، وَهُوَ مُبْتَدَأٌ.", "«and he» — a parenthetical ḥāl clause.", "«ve o» — itirâzî hâl cümlesi.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("آخِرُ", "akhir", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the last [of]» — the khabar.", "«sonuncusu» — haber."),
  mudaf_ilayh("الرُّسُلِ", "rasul", "«the messengers»", "«resullerin»", tags=[JT]),
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«before»", "«-den önce»"),
  noun_pron("نَبِيِّنَا", "nabi", "نَبِيِّ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Prophet»", "«Peygamberimiz»", tags=[ID]),
  tok("مُحَمَّدٍ", "muhammad", "propn", [BD], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ عَرَبِيٌّ مُنْصَرِفٌ.", "«Muḥammad» — a badal; an Arabic name, fully declined.", "«Muhammed» — bedel; munsarıf Arapça isim."),
  majrur("رَسُولِ", "rasul", "«the Messenger [of]»", "«Resûlü»", tags=[ID, BD], ar="بَدَلٌ ثَانٍ (أَوْ نَعْتٌ) مَجْرُورٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  mazi("صَلَّى", "salla", "«may bless»", "«salât etsin»", tags=["naqis-verbs", "form-ii-verbs"], hidden=None, extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ؛ جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ"),
  allah_fail(),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«him»", "«ona»"),
  mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm etsin»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ", punct="،"),
])
sen("s2", "and it is a story in which God's overpowering will, God's absolute power and God's exact wisdom showed themselves;",
        "ve o, Allah'ın kahredici irâdesinin, mutlak kudretinin ve ince hikmetinin tecelli ettiği bir kıssadır;", [
  tok("وَهِيَ", "hiya", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and it» — the mubtadaʾ.", "«ve o» — mübtedâ.", segments=wa_("هِيَ", "hiya", "pron")),
  tok("قِصَّةٌ", "qissa", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a story» — the khabar.", "«bir kıssa» — haber."),
  mazi_ta("تَجَلَّتْ", "tajalla", "«showed themselves»", "«tecelli etti»", tags=["jumla-sifa", "naqis-verbs", "form-v-verbs"], extra=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْجُمْلَةُ نَعْتٌ لِقِصَّةٌ"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in which»", "«onda»"),
  fail("إِرَادَةُ", "irada", "«the will [of]»", "«irâdesi»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  naat("الْقَاهِرَةُ", "qahir", "«overpowering»", "«kahredici»", case="raf", tags=["ism-fail"], punct="،"),
  atf("وَقُدْرَةُ", "qudra", "«the power [of]»", "«kudreti»", "raf", tags=[ID], sign="بِالضَّمَّةِ، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  naat("الْمُطْلَقَةُ", "mutlaq", "«absolute»", "«mutlak»", case="raf", tags=["ism-maful"], punct="،"),
  atf("وَحِكْمَةُ", "hikma", "«the wisdom [of]»", "«hikmeti»", "raf", tags=[ID], sign="بِالضَّمَّةِ، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  naat("الدَّقِيقَةُ", "daqiq", "«exact»", "«ince»", case="raf", punct="؛"),
])
sen("s3", "so his whole matter breaks the ordinary course, and his birth breaks the ordinary course: minds were bewildered by it, and in it the laws of nature were set aside,",
        "onun işi baştan sona âdeti aşar; doğumu âdeti aşar: akıllar onda şaşkına döndü, tabiat kanunları onda yürürlükten kalktı;", [
  noun_pron("فَأَمْرُهُ", "amr", "فَأَمْرُ", "هُ", "pron-3ms", "الْفَاءُ لِلتَّفْرِيعِ، وَأَمْرُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«so his matter» — the mubtadaʾ.", "«onun işi» — mübtedâ.", tags=[AT, MK, ID]),
  noun_pron("كُلُّهُ", "kull", "كُلُّ", "هُ", "pron-3ms", "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«all of it» — an emphasis.", "«baştan sona» — mânevî te'kid.", tags=["tawkid", ID]),
  tok("خَارِقٌ", "khariq", "noun", [MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ فَاعِلٍ مِنْ خَرَقَ.", "«breaking» — the khabar; the participle of kharaqa.", "«aşan, yırtan» — haber; haraka'nın ism-i fâili."),
  tok("لِلْعَادَةِ", "ada", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ (لِتَقْوِيَةِ الْعَامِلِ)، وَالْعَادَةِ مَجْرُورٌ — مَفْعُولُ خَارِقٍ فِي الْمَعْنَى.", "«the ordinary course» — the lām strengthens the participle's government.", "«âdeti» — lâm âmili takviye eder.", segments=[seg("لِ", "li", "prep"), seg("لْعَادَةِ", "ada", "noun")], punct="،"),
  noun_pron("وَوِلَادَتُهُ", "wilada", "وَوِلَادَتُ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَوِلَادَتُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his birth» — a mubtadaʾ.", "«ve doğumu» — mübtedâ.", tags=[AT, MK, ID]),
  tok("خَارِقَةٌ", "khariq", "noun", [MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«breaking» — the khabar.", "«aşan» — haber."),
  tok("لِلْعَادَةِ", "ada", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْعَادَةِ مَجْرُورٌ.", "«the ordinary course»", "«âdeti»", segments=[seg("لِ", "li", "prep"), seg("لْعَادَةِ", "ada", "noun")], punct="،"),
  mazi_ta("حَارَتْ", "hara", "«were bewildered»", "«şaşkına döndü»", tags=["jumla-sifa", "hollow-verbs"], extra=" — وَالْجُمْلَةُ نَعْتٌ (أَوْ حَالٌ)"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«by it»", "«onda»"),
  fail("الْأَلْبَابُ", "lubb", "«minds»", "«akıllar»", tags=[JT], punct="،"),
  tok("وَنُسِخَتْ", "nasakha", "verb", [AT, NF], "الْوَاوُ عَاطِفَةٌ، وَنُسِخَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and were set aside» — a passive.", "«ve yürürlükten kalktı» — meçhul.", segments=wa_("نُسِخَتْ", "nasakha", "verb")),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it»", "«onda»"),
  tok("الْقَوَانِينُ", "qanun", "noun", [NF, JT], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«the laws» — the deputy doer; a muntahā plural.", "«kanunlar» — nâib-i fâil; müntehe'l-cumû'."),
  naat("الطَّبِيعِيَّةُ", "tabii", "«of nature»", "«tabiat»", case="raf", tags=["ism-mansub"], punct="،"),
])
sen("s4", "and belief in it and assent to it weighed heavily on whoever believed in the laws of nature as a god that never ceases and never changes, and believed in experiment and observation and in the rulings of medicine and nature as a law that never alters and never shifts,",
        "ona inanmak ve onu tasdik etmek, tabiat kanunlarına yok olmaz ve değişmez bir ilâh gibi inanan, tecrübeye, gözleme, tıbbın ve tabiatın hükümlerine değişmez ve bozulmaz bir yasa gibi inanan kimseye ağır geldi;", [
  mazi("وَشَقَّ", "shaqqa", "«and weighed heavily»", "«ve ağır geldi»", tags=[AT, "doubled-verbs"], wa=True, hidden=None),
  fail("الْإِيمَانُ", "iman", "«belief»", "«inanmak»"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«in it»", "«ona»"),
  atf("وَالتَّصْدِيقُ", "tasdiq", "«assent»", "«tasdik»", "raf"),
  li_pron("لَهَا", "هَا", "pron-3fs", "«to it»", "«onu»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  tok("مَنْ", "man-mawsula", "pron", [HJ, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«whoever» — the relative pronoun in the place of jarr.", "«… kimseye» — ism-i mevsûl, mahallen mecrûr."),
  mazi("آمَنَ", "aamana", "«believed»", "«inanan»", tags=[MW, "form-iv-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  tok("بِالْقَوَانِينِ", "qanun", "noun", [HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَالْقَوَانِينِ مَجْرُورٌ بِالْكَسْرَةِ — أَلْ أَعَادَتِ الْكَسْرَةَ إِلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.", "«in the laws» — the article restores the kasra to the muntahā plural.", "«kanunlara» — harf-i târif müntehe'l-cumû'a kesreyi geri getirir.", segments=[seg("بِ", "bi", "prep"), seg("الْقَوَانِينِ", "qanun", "noun")]),
  naat("الطَّبِيعِيَّةِ", "tabii", "«of nature»", "«tabiat»", tags=["ism-mansub"]),
  ka_prep("كَإِلٰهٍ", "ilah", "«a god»", "«bir ilâh»", tags=[HL]),
  la_nafiya(),
  neg_mudari("يَزُولُ", "zala", "«never ceases»", "«yok olmaz»", hidden="هُوَ", extra=" — وَالْجُمْلَةُ نَعْتٌ لِإِلٰهٍ", tags=["jumla-sifa", "hollow-verbs"]),
  la_nafiya(wa=True),
  neg_mudari("يَحُولُ", "hala", "«never changes»", "«değişmez»", hidden="هُوَ", tags=[AT, "hollow-verbs"], punct="،"),
  mazi("وَآمَنَ", "aamana", "«and believed»", "«ve inanan»", tags=[AT, "form-iv-verbs"], wa=True, hidden="هُوَ"),
  tok("بِالتَّجْرِبَةِ", "tajriba", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّجْرِبَةِ مَجْرُورٌ.", "«in experiment»", "«tecrübeye»", segments=[seg("بِ", "bi", "prep"), seg("التَّجْرِبَةِ", "tajriba", "noun")]),
  atf("وَالْمُشَاهَدَةِ", "mushahada", "«observation»", "«gözleme»", "jarr"),
  tok("وَبِأَحْكَامِ", "hukm", "noun", [AT, HJ, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَأَحْكَامِ مَجْرُورٌ، مُضَافٌ.", "«and in the rulings [of]»", "«ve … hükümlerine»", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("أَحْكَامِ", "hukm", "noun")]),
  mudaf_ilayh("الطِّبِّ", "tibb", "«medicine»", "«tıbbın»"),
  atf("وَالطَّبِيعَةِ", "tabia", "«nature»", "«ve tabiatın»", "jarr"),
  ka_prep("كَنَامُوسٍ", "namus", "«a law»", "«bir yasa»", tags=[HL]),
  la_nafiya(),
  neg_mudari("يَتَغَيَّرُ", "taghayyara", "«never alters»", "«değişmez»", hidden="هُوَ", extra=" — وَالْجُمْلَةُ نَعْتٌ لِنَامُوسٍ", tags=["jumla-sifa", "form-v-verbs"]),
  la_nafiya(wa=True),
  neg_mudari("يَتَبَدَّلُ", "tabaddala", "«never shifts»", "«bozulmaz»", hidden="هُوَ", tags=[AT, "form-v-verbs"], punct="،"),
])
sen("s5", "and was ignorant of God's power that has encompassed everything and prevailed over everything, and of His will before which nothing stands: «His command, when He wills a thing, is only to say to it: Be — and it is» (36:82).",
        "ve her şeyi kuşatan, her şeye galip gelen Allah'ın kudretinden, önünde hiçbir şeyin duramadığı irâdesinden habersiz olan kimseye; «O bir şeyi dilediğinde emri yalnızca ona: Ol, demektir; o da oluverir» (36:82).", [
  mazi("وَجَهِلَ", "jahila", "«and was ignorant of»", "«ve habersiz olan»", tags=[AT, MB], wa=True, hidden="هُوَ"),
  maful_("قُدْرَةَ", "qudra", "«the power [of]»", "«kudretinden»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِقُدْرَةَ.", "«that» — a naʿt of «the power».", "«ki o» — «kudret»in sıfatı."),
  mazi_ta("أَحَاطَتْ", "ahata", "«has encompassed»", "«kuşatan»", tags=[MW, "hollow-verbs", "form-iv-verbs"], extra=" — صِلَةٌ"),
  tok("بِكُلِّ", "kull", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ، مُضَافٌ.", "«every»", "«her»", segments=[seg("بِ", "bi", "prep"), seg("كُلِّ", "kull", "noun")]),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeyi»", punct="،"),
  mazi_ta("وَغَلَبَتْ", "ghalaba", "«and prevailed»", "«ve galip gelen»", tags=[AT], wa=True),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeye»", punct="،"),
  noun_pron("وَإِرَادَتَهُ", "irada", "وَإِرَادَتَ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَإِرَادَتَ مَعْطُوفٌ عَلَى قُدْرَةَ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His will»", "«ve irâdesinden»", tags=[AT, ID]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ.", "«before which»", "«ki önünde»"),
  la_nafiya(),
  neg_mudari("يَحُولُ", "hala", "«stands» (lit. comes between)", "«duramaz»", hidden=None, extra=" — صِلَةٌ", tags=[MW, "hollow-verbs"]),
  noun_pron("دُونَهَا", "duna", "دُونَ", "هَا", "pron-3fs", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«before it»", "«önünde»", tags=[MF, ID]),
  fail("شَيْءٌ", "shay", "«nothing» (lit. a thing)", "«hiçbir şey»", punct="،"),
  *quran([
  tok("إِنَّمَا", "innama", "part", ["innama-kaffa"], "إِنَّ الْمَكْفُوفَةُ بِمَا عَنِ الْعَمَلِ — أَدَاةُ حَصْرٍ.", "«only» — inna restrained by mā; a restricting tool.", "«yalnızca» — mâ ile amelden düşmüş inne; hasr edatı."),
  noun_pron("أَمْرُهُ", "amr", "أَمْرُ", "هُ", "pron-3ms", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His command» — the mubtadaʾ.", "«emri» — mübtedâ.", tags=[MK, ID]),
  tok("إِذَا", "idha", "noun", [MF, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-dığında»"),
  mazi("أَرَادَ", "arada", "«He wills»", "«dilediğinde»", tags=["idha-shartiyya", MB, "hollow-verbs", "form-iv-verbs"], hidden="هُوَ", extra_ar=" — فِعْلُ الشَّرْطِ"),
  maful_("شَيْئًا", "shay", "«a thing»", "«bir şeyi»"),
  tok("أَنْ", "an-masdariyya", "part", [AN, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْمُبْتَدَإِ: أَمْرُهُ قَوْلُهُ.", "«to» — the clause is the khabar (His command is His saying).", "«… -mektir» — müevvel masdar haber."),
  mansub("يَقُولَ", "qala", "«say»", "«demek»", tags=["hollow-verbs", MB]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to it»", "«ona»"),
  tok("كُنْ", "kana", "verb", [AM, KN, "hollow-verbs"], "فِعْلُ أَمْرٍ تَامٌّ مَبْنِيٌّ عَلَى السُّكُونِ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — مَقُولُ الْقَوْلِ.", "«Be» — kāna's imperative as a full verb; its wāw dropped.", "«ol» — tam kâne'nin emri; vâvı düştü."),
  tok("فَيَكُونُ", "kana", "verb", [AT, KN, "hollow-verbs", "mudari-marfu"], "الْفَاءُ لِلِاسْتِئْنَافِ (أَوْ عَاطِفَةٌ)، وَيَكُونُ فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فَهُوَ يَكُونُ.", "«and it is» — a full kāna in rafʿ (not naṣb by the fāʾ): the khabar of an unspoken «so it».", "«o da oluverir» — tam kâne, merfû (fâ ile mansub değil): mahzuf «o» mübtedâsının haberi.", punct="."),
  ]),
])
sen("s6", "And this belief came easy to whoever believed in God as a god who is able and willing, a creator and maker: «He is God, the Creator, the Originator, the Shaper; His are the most beautiful names; whatever is in the heavens and the earth glorifies Him, and He is the Mighty, the Wise» (59:24).",
        "Bu iman, Allah'a kadir ve murad eden, yaratan ve yapan bir ilâh olarak inanan kimseye kolay geldi: «O, yaratan, var eden, şekil veren Allah'tır; en güzel isimler O'nundur; göklerde ve yerde ne varsa O'nu tesbih eder; O Azîz'dir, Hakîm'dir» (59:24).", [
  mazi("وَهَانَ", "hana", "«and came easy»", "«ve kolay geldi»", tags=["hollow-verbs"], wa=True, hidden=None),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("الْإِيمَانُ", "iman", "noun", [BD, FL], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ — وَالْمُشَارُ إِلَيْهِ هُوَ الْفَاعِلُ.", "«belief» — a badal; the demonstrative is the doer.", "«iman» — bedel; ism-i işâret fâildir."),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  tok("مَنْ", "man-mawsula", "pron", [HJ, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«whoever»", "«… kimseye»"),
  mazi("آمَنَ", "aamana", "«believed»", "«inanan»", tags=[MW, "form-iv-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  tok("بِاللهِ", "allah", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«in God»", "«Allah'a»", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  ka_prep("كَإِلٰهٍ", "ilah", "«a god»", "«bir ilâh»", tags=[HL]),
  naat("قَادِرٍ", "qadir", "«able»", "«kadir»", tags=["ism-fail"]),
  naat2("مُرِيدٍ", "murid", "«willing»", "«murad eden»", case="jarr", tags=["ism-fail", "form-iv-verbs"], punct="،"),
  naat2("خَالِقٍ", "khaliq", "«a creator»", "«yaratan»", case="jarr", n="ثَالِثٌ", tags=["ism-fail"]),
  naat2("صَانِعٍ", "sani", "«a maker»", "«yapan»", case="jarr", n="رَابِعٌ", tags=["ism-fail"], punct="،"),
  *quran([
  tok("هُوَ", "huwa", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«He» — the mubtadaʾ.", "«O» — mübtedâ."),
  tok("اللهُ", "allah", "propn", [MK], "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ.", "«God» — the khabar.", "«Allah'tır» — haber."),
  naat("الْخَالِقُ", "khaliq", "«the Creator»", "«yaratan»", case="raf", tags=["ism-fail"]),
  naat2("الْبَارِئُ", "bari-creator", "«the Originator»", "«var eden»", case="raf", tags=["ism-fail"]),
  naat2("الْمُصَوِّرُ", "musawwir", "«the Shaper»", "«şekil veren»", case="raf", n="ثَالِثٌ", tags=["ism-fail", "form-ii-verbs"]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«His» — the fronted khabar.", "«O'nundur» — öne alınmış haber.", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ"),
  tok("الْأَسْمَاءُ", "ism", "noun", [MK, JT], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the names» — the delayed mubtadaʾ.", "«isimler» — sonraya bırakılmış mübtedâ."),
  tok("الْحُسْنَى", "husna", "noun", [NA, "ism-maqsur-manqus", "ism-tafdil"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مُؤَنَّثُ الْأَحْسَنِ.", "«the most beautiful» — the naʿt; the feminine of al-aḥsan.", "«en güzel» — sıfat; el-ahsen'in müennesi."),
  mudari("يُسَبِّحُ", "sabbaha", "«glorifies»", "«tesbih eder»", tags=["form-ii-verbs"], hidden=None),
  li_pron("لَهُ", "هُ", "pron-3ms", "«Him»", "«O'nu»"),
  tok("مَا", "ma-mawsula", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«whatever» — the relative pronoun, the doer.", "«ne varsa» — ism-i mevsûl, fâil."),
  tok("فِي", "fi", "prep", [HJ, MW], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةُ الْمَوْصُولِ.", "«in» — the ṣila.", "«-de» — sıla."),
  majrur("السَّمَاوَاتِ", "sama", "«the heavens»", "«göklerde»", tags=[JM]),
  atf("وَالْأَرْضِ", "ard", "«the earth»", "«ve yerde»", "jarr"),
  tok("وَهُوَ", "huwa", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and He»", "«ve O»", segments=wa_("هُوَ", "huwa", "pron")),
  tok("الْعَزِيزُ", "aziz", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Mighty» — the khabar.", "«Azîz'dir» — haber."),
  tok("الْحَكِيمُ", "hakim", "noun", [MK], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«the Wise» — a second khabar.", "«Hakîm'dir» — ikinci haber.", punct="."),
  ]),
])
sen("s7", "And he believed in the creation of Ādam from water and clay, with neither mother nor father; and a birth from a mother without a father is easier and lighter to accept than a birth without mother or father — and for that God Most High says:",
        "Ve Âdem'in sudan ve çamurdan, annesiz ve babasız yaratıldığına inandı; bir anneden babasız doğum, annesiz ve babasız doğumdan tasdik etmesi daha kolay ve daha yalındır; bunun için Allah Teâlâ şöyle buyurur:", [
  mazi("وَآمَنَ", "aamana", "«and he believed»", "«ve inandı»", tags=[AT, "form-iv-verbs"], wa=True, hidden="هُوَ"),
  tok("بِخَلْقِ", "khalq", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَخَلْقِ مَجْرُورٌ، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ.", "«in the creation [of]» — a maṣdar annexed to its object.", "«yaratılışına» — mef'ûlüne muzâf masdar.", segments=[seg("بِ", "bi", "prep"), seg("خَلْقِ", "khalq", "noun")]),
  tok("آدَمَ", "adam-prophet", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ādam» — jarr by fatḥa (a diptote).", "«Âdem'in» — gayr-i munsarıf."),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("مَاءٍ", "ma-water", "«water»", "«su»"),
  atf("وَطِينٍ", "tin", "«clay»", "«çamur»", "jarr", punct="،"),
  tok("وَمِنْ", "min", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ.", "«and with» (lit. from)", "«ve … -sız»", segments=wa_("مِنْ", "min", "prep")),
  majrur("غَيْرِ", "ghayr", "«neither» (lit. other than)", "«olmaksızın»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("أُمٍّ", "umm", "«mother»", "«anne»"),
  atf("وَأَبٍ", "ab", "«father»", "«ve baba»", "jarr", punct="،"),
  tok("وَوِلَادَةٌ", "wilada", "noun", [AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَوِلَادَةٌ مُبْتَدَأٌ مَرْفُوعٌ — سَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ وَصْفُهَا بِالْجَارِّ وَالْمَجْرُورِ.", "«and a birth» — the mubtadaʾ; an indefinite allowed by its description.", "«ve bir doğum» — mübtedâ; sıfatla câiz nekre.", segments=wa_("وِلَادَةٌ", "wilada", "noun")),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("أُمٍّ", "umm", "«a mother»", "«bir anneden»"),
  prep("مِنْ", "min", "«without» (lit. from)", "«-sız»"),
  majrur("غَيْرِ", "ghayr", "«other than»", "«olmaksızın»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("أَبٍ", "ab", "«a father»", "«baba»"),
  tok("أَهْوَنُ", "ahwan", "noun", [MK, "ism-tafdil", MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«easier» — the khabar; an elative.", "«daha kolay» — haber; ism-i tafdîl."),
  tok("وَأَيْسَرُ", "aysar", "noun", [AT, MK, "ism-tafdil", MM], "الْوَاوُ عَاطِفَةٌ، وَأَيْسَرُ مَعْطُوفٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«and lighter»", "«ve daha yalın»", segments=wa_("أَيْسَرُ", "aysar", "noun")),
  tok("لِلتَّصْدِيقِ", "tasdiq", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالتَّصْدِيقِ مَجْرُورٌ.", "«to accept»", "«tasdik için»", segments=[seg("لِ", "li", "prep"), seg("لتَّصْدِيقِ", "tasdiq", "noun")]),
  prep("مِنْ", "min", "«than»", "«-den»", ar="حَرْفُ جَرٍّ — تَجُرُّ الْمُفَضَّلَ عَلَيْهِ بَعْدَ اسْمِ التَّفْضِيلِ."),
  majrur("وِلَادَةٍ", "wilada", "«a birth»", "«bir doğum»"),
  prep("مِنْ", "min", "«without»", "«-sız»"),
  majrur("غَيْرِ", "ghayr", "«other than»", "«olmaksızın»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("أُمٍّ", "umm", "«mother»", "«anne»"),
  atf("وَأَبٍ", "ab", "«father»", "«ve baba»", "jarr", punct="،"),
  tok("وَلِذٰلِكَ", "dhalika", "pron", [AT, HJ, "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«and for that»", "«ve bunun için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  mudari("يَقُولُ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs", MB], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
])
sen("s8", "«Indeed the likeness of ʿĪsā with God is as the likeness of Ādam: He created him from dust, then said to him: Be — and he was» (3:59).",
        "«Allah katında Îsâ'nın durumu Âdem'in durumu gibidir: onu topraktan yarattı, sonra ona: Ol, dedi; o da oluverdi» (3:59).", [
  *quran([
  inna(),
  ism_inna("مَثَلَ", "mathal", "«the likeness [of]»", "«durumu»", extra="، مُضَافٌ", tags=[ID]),
  tok("عِيسَى", "isa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ'nın»"),
  tok("عِنْدَ", "inda", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ — مُتَعَلِّقٌ بِالْخَبَرِ.", "«with»", "«katında»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("كَمَثَلِ", "mathal", "noun", [HJ, ID, IW], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَثَلِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«as the likeness [of]» — inna's khabar.", "«durumu gibidir» — inne'nin haberi.", segments=[seg("كَ", "ka", "prep"), seg("مَثَلِ", "mathal", "noun")]),
  tok("آدَمَ", "adam-prophet", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ādam»", "«Âdem'in»"),
  v_pron("خَلَقَهُ", "khalaqa", "خَلَقَ", "هُ", "pron-3ms", "«He created him»", "«onu yarattı»", hidden="هُوَ", tags=["jumla-mutarida"]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("تُرَابٍ", "turab", "«dust»", "«toprak»"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  qala(hidden="هُوَ", punct=None),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»"),
  tok("كُنْ", "kana", "verb", [AM, KN, "hollow-verbs"], "فِعْلُ أَمْرٍ تَامٌّ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — مَقُولُ الْقَوْلِ.", "«Be»", "«ol»"),
  tok("فَيَكُونُ", "kana", "verb", [AT, KN, "hollow-verbs", "mudari-marfu"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ — حِكَايَةُ حَالٍ مَاضِيَةٍ.", "«and he was» — the muḍāriʿ telling a past state.", "«o da oluverdi» — hikâye-i hâl-i mâziye.", punct="."),
  ]),
])
# ---------------------------------------------------------------- §2 أَمْرٌ كُلُّهُ عَجَبٌ (print p. 40)
sen("s9", "And the matter of our master ʿĪsā is wholly a wonder: his birth fell in an age in which «Greece» had reached its zenith in the rational and mathematical sciences, and medicine had a dominion and a sway.",
        "Efendimiz Îsâ'nın işi baştan sona hayrettir: doğumu, «Yunan»ın aklî ve riyâzî ilimlerde zirveye ulaştığı, tıbbın bir devleti ve saltanatı olduğu bir çağa rastladı.", [
  tok("وَأَمْرُ", "amr", "noun", [MK, ID], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمْرُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the matter [of]» — the mubtadaʾ.", "«ve … işi» — mübtedâ.", segments=wa_("أَمْرُ", "amr", "noun")),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[ID]),
  tok("عِيسَى", "isa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ'nın»"),
  noun_pron("كُلُّهُ", "kull", "كُلُّ", "هُ", "pron-3ms", "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«all of it»", "«baştan sona»", tags=["tawkid", ID]),
  tok("عَجَبٌ", "ajab", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — مَصْدَرٌ وُصِفَ بِهِ لِلْمُبَالَغَةِ.", "«a wonder» — the khabar; a maṣdar used as a description for emphasis.", "«hayret» — haber; mübalağa için masdarla vasıf.", punct="،"),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("كَانَتْ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«was»", "«idi»"),
  noun_pron("وِلَادَتُهُ", "wilada", "وِلَادَتُ", "هُ", "pron-3ms", "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his birth» — kāna's ism.", "«doğumu» — kâne'nin ismi.", tags=[KN, ID]),
  tok("فِي", "fi", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«in» — kāna's khabar.", "«-de» — kâne'nin haberi."),
  majrur("عَصْرٍ", "asr", "«an age»", "«bir çağda»"),
  mazi_ta("بَلَغَتْ", "balagha", "«had reached»", "«ulaştığı»", tags=["jumla-sifa", MB], extra=" — وَالْجُمْلَةُ نَعْتٌ لِعَصْرٍ"),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in which»", "«onda»"),
  tok("يُونَانُ", "yunan", "propn", [FL, MM], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Greece» — the doer; a foreign feminine name, a diptote.", "«Yunan» — fâil; yabancı müennes özel isim, gayr-i munsarıf."),
  noun_pron("أَوْجَهَا", "awj", "أَوْجَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its zenith»", "«zirvesine»", tags=[MB, ID]),
  fi(), majrur("الْعُلُومِ", "ilm", "«the sciences»", "«ilimlerde»", tags=[JT]),
  naat("الْعَقْلِيَّةِ", "aqli", "«rational»", "«aklî»", tags=["ism-mansub"]),
  tok("وَالرِّيَاضِيَّةِ", "riyadi", "noun", [AT, NA, "ism-mansub"], "الْوَاوُ عَاطِفَةٌ، وَالرِّيَاضِيَّةِ مَعْطُوفٌ عَلَى النَّعْتِ مَجْرُورٌ.", "«and mathematical»", "«ve riyâzî»", segments=wa_("الرِّيَاضِيَّةِ", "riyadi", "noun"), punct="،"),
  tok("وَكَانَتْ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and there was»", "«ve … vardı»", segments=wa_("كَانَتْ", "kana", "verb")),
  tok("لِلطِّبِّ", "tibb", "noun", [HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَالطِّبِّ مَجْرُورٌ — خَبَرُ كَانَ مُقَدَّمٌ.", "«medicine had» — kāna's fronted khabar.", "«tıbbın … vardı» — kâne'nin öne alınmış haberi.", segments=[seg("لِ", "li", "prep"), seg("لطِّبِّ", "tibb", "noun")]),
  tok("دَوْلَةٌ", "dawla", "noun", [KN], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a dominion» — kāna's delayed ism.", "«bir devleti» — kâne'nin ismi."),
  atf("وَصَوْلَةٌ", "sawla", "«a sway»", "«ve saltanatı»", "raf", punct="."),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: bari-creator, adam-prophet take suffixed keys; zala, hana reused)
CAND = {
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come (hollow, hamzated)", "gelmek (ecvef, mehmûz)", 1),
 "dawr": G("dawr", "دَوْر", "د و ر", "noun", "a turn; a role", "sıra; rol", 2),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "akhir": G("akhir", "آخِر", "أ خ ر", "noun", "the last, the end", "son, sonuncu", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resul, elçi", 1, plural="رُسُل"),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "önce", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "muhammad": G("muhammad", "مُحَمَّد", "ح م د", "propn", "Muḥammad", "Muhammed", 1),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "salla": G("salla", "صَلَّى", "ص ل و", "verb", "to pray; (God) to bless (Form II, defective)", "namaz kılmak; (Allah) salât etmek (tef'îl, nâkıs)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "sallama": G("sallama", "سَلَّمَ", "س ل م", "verb", "to greet, to grant peace (Form II)", "selâm vermek (tef'îl)", 1),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it (f.)", "o (müennes)", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "tajalla": G("tajalla", "تَجَلَّى", "ج ل و", "verb", "to show itself, to be manifested (Form V, defective)", "tecelli etmek (tefa''ul, nâkıs)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "irada": G("irada", "إِرَادَة", "ر و د", "noun", "will", "irâde", 1),
 "qahir": G("qahir", "قَاهِر", "ق ه ر", "noun", "overpowering, subduing (an active participle)", "kahredici, kahhâr (ism-i fâil)", 2),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "mutlaq": G("mutlaq", "مُطْلَق", "ط ل ق", "noun", "absolute, unrestricted (a passive participle of Form IV)", "mutlak (if'âl ism-i mef'ûlü)", 2),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "daqiq": G("daqiq", "دَقِيق", "د ق ق", "noun", "fine, exact, minute", "ince, dakik", 2),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "khariq": G("khariq", "خَارِق", "خ ر ق", "noun", "breaking through, extraordinary (an active participle)", "yırtan, aşan; hârika (ism-i fâil)", 2),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "custom, the ordinary course", "âdet", 1),
 "wilada": G("wilada", "وِلَادَة", "و ل د", "noun", "birth", "doğum", 1),
 "hara": G("hara", "حَارَ", "ح ي ر", "verb", "to be bewildered (hollow)", "şaşırmak, hayrete düşmek (ecvef)", 2),
 "lubb": G("lubb", "لُبّ", "ل ب ب", "noun", "the core; the mind", "öz; akıl", 2, plural="أَلْبَاب"),
 "nasakha": G("nasakha", "نَسَخَ", "ن س خ", "verb", "to abrogate, to set aside; to copy", "neshetmek, yürürlükten kaldırmak; kopyalamak", 2),
 "qanun": G("qanun", "قَانُون", "ق ن ن", "noun", "a law", "kanun", 1, plural="قَوَانِين"),
 "tabii": G("tabii", "طَبِيعِيّ", "ط ب ع", "noun", "natural (a nisba)", "tabiî (nisbet)", 2),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to split; (ʿalā) to weigh heavily on (doubled)", "yarmak; (alâ ile) ağır gelmek (muzâaf)", 2),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith, belief", "iman", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "tasdiq": G("tasdiq", "تَصْدِيق", "ص د ق", "noun", "assent, affirming as true", "tasdik", 2),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "whoever, he who", "kim ki, … kimse", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "ka": G("ka", "كَ", None, "prep", "like, as", "gibi", 1),
 "ilah": G("ilah", "إِلَه", "أ ل ه", "noun", "a god", "ilâh", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "zala": G("zala", "زَالَ", "ز و ل", "verb", "to cease, to pass away (hollow)", "yok olmak, zevâl bulmak (ecvef)", 2),
 "hala": G("hala", "حَالَ", "ح و ل", "verb", "to change; (dūna) to come between (hollow)", "değişmek; (dûne ile) engel olmak (ecvef)", 2),
 "tajriba": G("tajriba", "تَجْرِبَة", "ج ر ب", "noun", "an experience, an experiment", "tecrübe", 2, plural="تَجَارِب"),
 "mushahada": G("mushahada", "مُشَاهَدَة", "ش ه د", "noun", "observation", "gözlem, müşâhede", 2),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "a ruling, judgement", "hüküm", 1, plural="أَحْكَام"),
 "tibb": G("tibb", "طِبّ", "ط ب ب", "noun", "medicine", "tıp", 1),
 "tabia": G("tabia", "طَبِيعَة", "ط ب ع", "noun", "nature", "tabiat", 1),
 "namus": G("namus", "نَامُوس", "ن م س", "noun", "a law, an ordinance", "yasa, nâmus", 3),
 "taghayyara": G("taghayyara", "تَغَيَّرَ", "غ ي ر", "verb", "to alter, to change (Form V)", "değişmek (tefa''ul)", 1),
 "tabaddala": G("tabaddala", "تَبَدَّلَ", "ب د ل", "verb", "to shift, to be replaced (Form V)", "değişmek, bozulmak (tefa''ul)", 2),
 "jahila": G("jahila", "جَهِلَ", "ج ه ل", "verb", "to be ignorant of", "bilmemek, câhil olmak", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "ahata": G("ahata", "أَحَاطَ", "ح و ط", "verb", "to encompass (Form IV, hollow)", "kuşatmak (if'âl, ecvef)", 2),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "ghalaba": G("ghalaba", "غَلَبَ", "غ ل ب", "verb", "to prevail over", "galip gelmek", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "below; before, short of", "aşağısında; önünde, -den başka", 1),
 "innama": G("innama", "إِنَّمَا", None, "part", "only (inna + the restraining mā)", "ancak, yalnızca (inne + kâffe mâ)", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ırsa", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to intend, to want (Form IV, hollow)", "istemek, murad etmek (if'âl, ecvef)", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "hana": G("hana", "هَانَ", "ه و ن", "verb", "to be easy, light (hollow)", "kolay olmak, hafif gelmek (ecvef)", 2),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "qadir": G("qadir", "قَادِر", "ق د ر", "noun", "powerful, able (an active participle)", "kadir, gücü yeten (ism-i fâil)", 1),
 "murid": G("murid", "مُرِيد", "ر و د", "noun", "willing, intending (an active participle of Form IV)", "murad eden, irâde eden (if'âl ism-i fâili)", 2),
 "khaliq": G("khaliq", "خَالِق", "خ ل ق", "noun", "a creator; the Creator", "yaratan, Hâlık", 1),
 "sani": G("sani", "صَانِع", "ص ن ع", "noun", "a maker (an active participle)", "yapan, sâni' (ism-i fâil)", 2),
 "bari-creator": G("bari-creator", "بَارِئ", "ب ر أ", "noun", "the Originator (an active participle)", "var eden, Bârî (ism-i fâil)", 2),
 "musawwir": G("musawwir", "مُصَوِّر", "ص و ر", "noun", "the Shaper (an active participle of Form II)", "şekil veren, Musavvir (tef'îl ism-i fâili)", 2),
 "ism": G("ism", "اِسْم", "س م و", "noun", "a name", "isim", 1, plural="أَسْمَاء"),
 "husna": G("husna", "حُسْنَى", "ح س ن", "noun", "most beautiful (the feminine elative of aḥsan)", "en güzel (ahsen'in müennesi)", 2),
 "sabbaha": G("sabbaha", "سَبَّحَ", "س ب ح", "verb", "to glorify (Form II)", "tesbih etmek (tef'îl)", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "a heaven, the sky", "gök", 1, plural="سَمَاوَات"),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "the earth", "yer, yeryüzü", 1),
 "aziz": G("aziz", "عَزِيز", "ع ز ز", "noun", "mighty; dear", "azîz, güçlü; değerli", 1),
 "hakim": G("hakim", "حَكِيم", "ح ك م", "noun", "wise", "hakîm, hikmetli", 1),
 "khalq": G("khalq", "خَلْق", "خ ل ق", "noun", "creation; creatures", "yaratma; yaratıklar", 1),
 "adam-prophet": G("adam-prophet", "آدَم", None, "propn", "Ādam (Adam)", "Âdem", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "ma-water": G("ma-water", "مَاء", "م و ه", "noun", "water", "su", 1),
 "tin": G("tin", "طِين", "ط ي ن", "noun", "clay", "çamur", 1),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not, without", "başka; gayri, -sız", 1),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "ab": G("ab", "أَب", "أ ب و", "noun", "a father (one of the five nouns)", "baba (esmâ-i hamseden)", 1),
 "ahwan": G("ahwan", "أَهْوَن", "ه و ن", "noun", "easier, lighter (an elative)", "daha kolay (ism-i tafdîl)", 2),
 "aysar": G("aysar", "أَيْسَر", "ي س ر", "noun", "easier, simpler (an elative)", "daha kolay, daha yalın (ism-i tafdîl)", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "mathal": G("mathal", "مَثَل", "م ث ل", "noun", "a likeness; a parable", "misal, durum; mesel", 1),
 "inda": G("inda", "عِنْدَ", None, "noun", "with, at, in the presence of", "yanında, katında", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1),
 "turab": G("turab", "تُرَاب", "ت ر ب", "noun", "dust, earth", "toprak", 1),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "ajab": G("ajab", "عَجَب", "ع ج ب", "noun", "a wonder, astonishment", "hayret, şaşılacak şey", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "asr": G("asr", "عَصْر", "ع ص ر", "noun", "an age, an era; the afternoon", "çağ, asır; ikindi", 1),
 "balagha": G("balagha", "بَلَغَ", "ب ل غ", "verb", "to reach", "ulaşmak", 1),
 "yunan": G("yunan", "يُونَان", None, "propn", "Greece, the Greeks", "Yunan", 2),
 "awj": G("awj", "أَوْج", "أ و ج", "noun", "the zenith, the peak", "zirve, evc", 3),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge; a science", "ilim", 1, plural="عُلُوم"),
 "aqli": G("aqli", "عَقْلِيّ", "ع ق ل", "noun", "rational (a nisba)", "aklî (nisbet)", 2),
 "riyadi": G("riyadi", "رِيَاضِيّ", "ر و ض", "noun", "mathematical (a nisba)", "riyâzî, matematiksel (nisbet)", 2),
 "dawla": G("dawla", "دَوْلَة", "د و ل", "noun", "a state; dominion", "devlet; hâkimiyet", 1),
 "sawla": G("sawla", "صَوْلَة", "ص و ل", "noun", "sway, might", "saltanat, güç gösterisi", 3),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "nasakha", _sg.sound1("fataha", "نَسَخ", "نْسَخ", "اِنْسَخ", "نَسْخ", "نَاسِخ", "مَنْسُوخ", "نُسِخَ", "يُنْسَخُ", "نَسَخَ الْحُكْمَ: أَبْطَلَهُ وَأَزَالَهُ؛ وَنَسَخَ الْكِتَابَ: نَقَلَهُ."))
put_morph(mo, "hara", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "حَار", "حِر", "حِير", "حِر", "حِير", "حِر", "حَيْرَة", "حَائِر", None, None, None, "حَارَ يَحَارُ أَوْ يَحِيرُ: تَرَدَّدَ وَلَمْ يَهْتَدِ — الْجَدْوَلُ عَلَى يَحِيرُ."))
put_morph(mo, "hala", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "حَال", "حُل", "حُول", "حُل", "حُول", "حُل", "حَوْل / حُؤُول", "حَائِل", None, None, None, "حَالَ الشَّيْءُ: تَغَيَّرَ؛ وَحَالَ دُونَهُ: مَنَعَ مِنْهُ — أَجْوَفُ وَاوِيٌّ؛ لَمْ يَحُلْ."))
put_morph(mo, "ghalaba", _sg.sound1("daraba", "غَلَب", "غْلِب", "اِغْلِب", "غَلَبَة / غَلَب", "غَالِب", "مَغْلُوب", "غُلِبَ", "يُغْلَبُ", "غَلَبَهُ: قَهَرَهُ وَفَاقَهُ."))
put_morph(mo, "jahila", _sg.sound1("samia", "جَهِل", "جْهَل", "اِجْهَل", "جَهْل", "جَاهِل", "مَجْهُول", "جُهِلَ", "يُجْهَلُ", "جَهِلَ الشَّيْءَ: لَمْ يَعْلَمْهُ."))
put_morph(mo, "tabaddala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَدَّل", "تَبَدَّل", "تَبَدَّل", "تَبَدُّل", "مُتَبَدِّل", None, None, None, "تَبَدَّلَ الشَّيْءُ: تَغَيَّرَ وَصَارَ غَيْرَ مَا كَانَ."))
put_morph(mo, "balagha", _sg.sound1("nasara", "بَلَغ", "بْلُغ", "اُبْلُغ", "بُلُوغ", "بَالِغ", "مَبْلُوغ", "بُلِغَ", "يُبْلَغُ", "بَلَغَ الْمَكَانَ: وَصَلَ إِلَيْهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch23 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 23 (print pp. 39–40; the story of ʿĪsā opens): a story that breaks the ordinary course — the laws of nature as a false god, with 36:82, 59:24 and 3:59 (s1–s8); a matter wholly wondrous: the age of Greek science (s9)."
ADD_TR = " Yirmi üçüncü bölüm (baskı s. 39–40; Îsâ kıssası açılır): âdeti aşan bir kıssa — sahte ilâh olarak tabiat kanunları, 36:82, 59:24 ve 3:59 ile (s1–s8); baştan sona hayret olan bir iş: Yunan ilminin çağı (s9)."
write_out(23, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §1–2", GLOSS_ADD, notes=(), related=())
report(23, S, GLOSS_ADD, ())
