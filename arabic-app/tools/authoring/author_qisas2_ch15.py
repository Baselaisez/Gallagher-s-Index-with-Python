# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 15: «سَفِينَةُ نُوحٍ» §22 بَعْدَ الطُّوفَانِ (when what God willed had come to pass and the unbelievers had drowned, the sky held back and the water sank away; the ship settled on Mount al-Jūdī, «and it was said: away with the wrongdoing people» — 11:44; «O Nūḥ, go down in peace»; Nūḥ and the ship's company walk on the land in peace; the unbelievers of Nūḥ's people perished and neither sky nor earth wept for them; God blessed the offspring of Nūḥ, and they spread and filled the earth — nations, prophets and kings; «peace be upon Nūḥ among all beings» — 37:79, printed twice; the END of «سفينة نوح»). Print pp. 32–33.
python3 tools/authoring/author_qisas2_ch15.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: بَعْدَ الطُّوفَانِ", "en": "The ship of Nūḥ: after the flood", "tr": "Nûh'un gemisi: tufandan sonra"}
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


def li_noun(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".", "«to/for» + " + en, "«-e» + " + tr, punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "noun")])
def bi_noun(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [HJ] + list(tags), "الْبَاءُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".", "«by/with» + " + en, "«ile» + " + tr, punct=punct, segments=[seg("بِ", "bi", "prep"), seg(full[2:], lex, "noun")])
def zarf(full, lex, en, tr, punct=None, kind="مَكَانٍ"):
    return tok(full, lex, "noun", [MF, ID], "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", en + " — an adverbial (ẓarf), annexed.", tr + " — zarf, muzâf.", punct=punct)
def wa_prep(full, lex, en, tr, punct=None):
    return tok(full, lex, "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " حَرْفُ جَرٍّ.", "«and» + " + en, "«ve» + " + tr, punct=punct, segments=wa_(full[2:], lex, "prep"))
def fa_la(jins=False):
    body = "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ" if jins else "لَا نَافِيَةٌ لَا عَمَلَ لَهَا"
    return tok("فَلَا", "la-nafiya", "part", ["la-nafiya-lil-jins" if jins else "la-nafiya", AT], "الْفَاءُ لِلتَّفْرِيعِ (عَاطِفَةٌ)، وَ" + body + ".", "«so … no» — the fāʾ draws the consequence; " + ("the lā of the genus." if jins else "the negating lā."), "«bu yüzden … yok/-mez» — fâ sonucu bağlar; " + ("cins nefyeden lâ." if jins else "nefiy lâ'sı."), segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")])
def khamsa_wa(full, lex, en, tr, tags=(), punct=None, extra_ar=""): return khamsa(full, lex, en, tr, tags=[AT] + list(tags), punct=punct, extra_ar=extra_ar, wa=True)

def kana_pl(full="وَكَانُوا", wa=True, khabar_note=""):
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا" + khabar_note + ".", ("«and» + " if wa else "") + "«they were» — kāna; the wāw is its ism.", ("«ve» + " if wa else "") + "«idiler» — kâne; vâv ismi.", segments=(wa_("كَانُوا", "kana", "verb") if wa else None))
def pron_atf(full, lex, stem, pron_form, pron_lex, en, tr, case="jarr", punct=None, tags=()):
    C = {"jarr": "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ", "raf": "مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ"}[case]
    return tok(full, lex, "noun", [AT, ID] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + stem + " " + C + "، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«and» + " + en + " — joined; annexed to the pronoun.", "«ve» + " + tr + " — ma'tûf; zamire muzâf.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])

def mudari_wa(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, sign="بِالضَّمَّةِ", extra=""):
    return tok(full, lex, "verb", [AT, "mudari-marfu"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign + (("، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden) if hidden else "") + extra + ".", "«and» + " + en + " — a muḍāriʿ in rafʿ; the doer is concealed.", "«ve» + " + tr + " — merfû muzari; fâil gizli.", punct=punct, segments=wa_(full[2:], lex, "verb"))
def tahaddi(first=False, punct=None):
    return tok("تَحَدِّيًا", "tahaddi", "noun", ([KN] if first else [BD, "tawkid"]) + ["ism-maqsur-manqus", "form-v-verbs"], ("خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ" if first else "بَدَلٌ مُطَابِقٌ (تَوْكِيدٌ لَفْظِيٌّ بِالتَّكْرَارِ) مَنْصُوبٌ") + " — مَصْدَرُ تَحَدَّى، مَنْقُوصٌ: تَحَدٍّ، تَظْهَرُ فَتْحَتُهُ فِي النَّصْبِ.", "«a challenge» — " + ("kāna's khabar; " if first else "repeated as a badal; ") + "the manqūṣ maṣdar of taḥaddā shows its fatḥa in naṣb.", "«bir meydan okuma» — " + ("kâne'nin haberi; " if first else "tekrarla bedel; ") + "tehaddâ'nın mankûs masdarı, nasbda fethası görünür.", punct=punct)

def fa_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", extra=""):
    return tok(full, lex, "verb", [AT, "mudari-marfu"] + list(tags), "الْفَاءُ عَاطِفَةٌ، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", "«so» + " + en + " — a muḍāriʿ; the doer is concealed.", "«böylece» + " + tr + " — muzari; fâil gizli.", segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])
def bi_ma(punct=None, extra=""):
    return tok("بِمَا", "ma-mawsula", "pron", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ" + extra + ".", "«of what» — the relative after bi.", "«… şeyi» — bâ'dan sonra ism-i mevsûl.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")])
ISA_FAIL = " — يَعُودُ عَلَى عِيسَى عَلَى مَعْنَى الْآيَةِ (وَأُبْرِئُ)، وَيَصِحُّ عَوْدُهُ عَلَى اللهِ"

def wa_min(en="«and of»", tr="«ve … -den»", extra=""):
    return tok("وَمِنَ", "min", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَمِنَ حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ" + extra + ".", en, tr, segments=wa_("مِنَ", "min", "prep"))
AYA = "۝"

def bi_idhn(punct=None):
    return [bi_noun("بِإِذْنِ", "idhn", "«by the leave [of]»", "«izniyle»", tags=[ID], extra="، مُضَافٌ"),
            tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct=punct)]
def jitukum(wa=False):
    return tok(("وَ" if wa else "") + "جِئْتُكُمْ", "jaa", "verb", ([AT] if wa else [IW]) + [MB, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "جِئْتُ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — أَجْوَفُ: حُذِفَتْ عَيْنُهُ وَكُسِرَ مَا قَبْلَهَا (جِئْتُ)" + ("" if wa else "؛ وَالْجُمْلَةُ خَبَرُ أَنَّ") + ".", ("«and» + " if wa else "") + "«I have come to you» — the hollow verb drops its middle before the tāʾ; the kāf is the object.", ("«ve» + " if wa else "") + "«size geldim» — ecvef fiil tâ önünde ortasını düşürür; kâf mef'ûl.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("كُمْ", "pron-2mp", "pron")])
def bi_aya():
    return [bi_noun("بِآيَةٍ", "aya", "«with a sign»", "«bir âyetle»"), prep("مِنْ", "min", "«from»", "«-den»"),
            noun_pron("رَبِّكُمْ", "rabb", "رَبِّ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِآيَةٍ.", "«your Lord» — the phrase is a ṣifa of «a sign».", "«Rabbiniz» — ibare «âyet»in sıfatı.", tags=[HJ, ID, NA])]

def alladhina(case, role, en, tr, tags=()):
    C = {"raf": "رَفْعٍ", "nasb": "نَصْبٍ", "jarr": "جَرٍّ"}[case]
    return tok("الَّذِينَ", "alladhina", "pron", [MW] + list(tags), "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ " + C + " " + role + ".", en, tr)
def kafaru(role=" — صِلَةٌ", en="«disbelieved» — the ṣila.", tr="«inkâr ettiler» — sıla."):
    return tok("كَفَرُوا", "kafara", "verb", [MW], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ" + role + ".", en, tr)
def participle_ka(full, lex, stem, en, tr, tags=(), ar_extra="", wa=True, first=False):
    return tok(full, lex, "noun", ([AT] if wa else []) + [IW, ID, "ism-fail"] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + stem + (" خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ" if first else " مَعْطُوفٌ عَلَى خَبَرِ إِنَّ مَرْفُوعٌ") + "، مُضَافٌ إِلَى الْكَافِ (إِضَافَةٌ لَفْظِيَّةٌ: اسْمُ الْفَاعِلِ إِلَى مَفْعُولِهِ)" + ar_extra + ".", ("«and» + " if wa else "") + en + " — an active participle annexed to its object, the kāf.", ("«ve» + " if wa else "") + tr + " — mef'ûlü olan kâf'a muzâf ism-i fâil.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "noun"), seg("كَ", "pron-2ms", "pron")])

def amanna(wa=False, tags=()):
    return tok(("وَ" if wa else "") + "آمَنَّا", "aamana", "verb", ([AT] if wa else []) + ["form-iv-verbs"] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "آمَنَّا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — أُدْغِمَتْ نُونُ الْفِعْلِ فِي نُونِ الضَّمِيرِ.", ("«and» + " if wa else "") + "«we believe» — nā is the doer.", ("«ve» + " if wa else "") + "«inandık» — nâ fâil.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("آمَ", "aamana", "verb"), seg("نَّا", "pron-1p", "pron")])
def li_anna(full, pron_form, pron_lex, en, tr):
    return tok(full, "anna", "part", [HJ, IW, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ.", en + " — the lām of cause with anna; the pronoun is its ism.", tr + " — ta'lil lâmı ile enne; zamir ismi.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), seg(pron_form, pron_lex, "pron")])
def wa_fiha():
    return tok("وَفِيهَا", "fi", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in it» — a fronted khabar.", "«ve onda» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])

def kana_pl(full="وَكَانُوا", wa=True, khabar_note=""):
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا" + khabar_note + ".", ("«and» + " if wa else "") + "«they were» — kāna; the wāw is its ism.", ("«ve» + " if wa else "") + "«idiler» — kâne; vâv ismi.", segments=(wa_("كَانُوا", "kana", "verb") if wa else None))
def hal_pair(full, lex, en, tr, punct=None, tags=()):
    return hal(full, lex, en, tr, punct=punct, tags=["ism-fail"] + list(tags))

def maida_min_sama(punct=None):
    return [maful_("مَائِدَةً", "maida", "«a table»", "«bir sofra»"),
            tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
            majrur("السَّمَاءِ", "sama", "«heaven»", "«gökten»", punct=punct)]
def js_naat(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [NA, JS] + list(tags), "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", en + " — a naʿt; jarr by the yāʾ.", tr + " — sıfat; yâ ile mecrûr.", punct=punct)

def wa_la_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra=""):
    return tok(full, lex, "verb", [AT, "la-nafiya", "mudari-marfu"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ، وَ" + full[4:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", "«and … not» + " + en, "«ve … -mez» + " + tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part"), seg(full[4:], lex, "verb")])

def wa_kana(ism_note=""):
    return tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ" + ism_note + ".", "«and … was»", "«ve … idi»", segments=wa_("كَانَ", "kana", "verb"))
def ism_kana(full, lex, en, tr, punct=None, tags=(), ar="اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ."): return tok(full, lex, "noun", [KN] + list(tags), ar, en + " — kāna's ism.", tr + " — kâne'nin ismi.", punct=punct)
def khabar_kana(full, lex, en, tr, punct=None, tags=(), ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [KN] + list(tags), ar, en + " — kāna's khabar.", tr + " — kâne'nin haberi.", punct=punct)
def js_khabar(full, lex, stem, en, tr, note, punct=None, tags=(), role="خَبَرُ كَانُوا"):
    return tok(full, lex, "noun", [KN, JS, ID] + list(tags), role + " مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ" + note + ".", en + " — a sound plural in naṣb, its nūn dropped for the annexation.", tr + " — cemi müzekker sâlim, nûnu izâfet için düşmüş.", punct=punct)

def tafdil_hum(full, lex, stem, en, tr, punct=None, wa=True, first=False):
    return tok(full, lex, "noun", ([AT] if wa else []) + [KN, ID, "ism-tafdil"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + stem + (" خَبَرُ كَانَ مَنْصُوبٌ" if first else " مَعْطُوفٌ مَنْصُوبٌ") + " بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — اسْمُ تَفْضِيلٍ.", ("«and» + " if wa else "") + en + " — an elative annexed to the pronoun.", ("«ve» + " if wa else "") + tr + " — zamire muzâf ism-i tafdîl.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "noun"), seg("هُمْ", "pron-3mp", "pron")])
def tamyiz(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "noun", ["tamyiz"] + list(tags), "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — a tamyīz.", tr + " — temyiz.", punct=punct)

def qatalu_hu(full, lex, en, tr, punct=None):
    stem = full[4:len(full)-2]
    return tok(full, lex, "verb", [AT, MB, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ، وَ" + stem + "ا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and they did not» + " + en, "«ve onu» + " + tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part"), seg(stem, lex, "verb"), seg("هُ", "pron-3ms", "pron")])

def fa_qalu(punct=":"):
    return tok("فَقَالُوا", "qala", "verb", [AT, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَقَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they said»", "«bunun üzerine dediler»", segments=[seg("فَ", "fa", "conj"), seg("قَالُوا", "qala", "verb")], punct=punct)
def wa_qalu(punct=":"):
    return mazi_pl("وَقَالُوا", "qala", "«and they said»", "«ve dediler»", tags=[AT, "hollow-verbs"], wa=True, punct=punct)

# ---------------------------------------------------------------- § the chapter's own small helpers
def allah_maful(full="اللهَ", punct=None):
    return tok(full, "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object, in naṣb.", "«Allah» — lafza-i celâl, mef'ûl, mansub.", punct=punct)
def allah_mi(punct=None): return tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah'ın» — muzâfun ileyh.", punct=punct)
def group_pron(full, lex, stem, pron_form, pron_lex, en, tr, ar_tail, punct=None, tags=(), wa=False):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ""
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if wa else []) + [AK, "mudari-marfu", MB] + list(tags), pre + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + ar_tail + ".", ("«and» + " if wa else "") + en + " — a muḍāriʿ of the five; the attached pronoun is its object.", ("«ve» + " if wa else "") + tr + " — beş fiilden muzâri; bitişik zamir mef'ûl.", punct=punct, segments=segs)
def abahum(role_ar, en, tr, tags=(), punct=None):
    return noun_pron("آبَاءَهُمْ", "ab", "آبَاءَ", "هُمْ", "pron-3mp", role_ar + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ أَبٍ.", en, tr, tags=[MB, ID, JT] + list(tags), punct=punct)
def yarawnahum(punct=None):
    return tok("يَرَوْنَهُمْ", "raa", "verb", [KN, AK, "mudari-marfu", MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ: يَرَى + ونَ)، وَالْوَاوُ فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«they saw them» — the defective muḍāriʿ before the group's wāw (yarā + ūna → yarawna); the pronoun is the first object; the clause is kāna's khabar.", "«onları görürlerdi» — cemaat vâvından önce nâkıs muzâri (yerâ + ûne → yerevne); zamir birinci mef'ûl; cümle kâne'nin haberi.", punct=punct, segments=[seg("يَرَوْنَ", "raa", "verb"), seg("هُمْ", "pron-3mp", "pron")])
def indaha(punct=None): return noun_pron("عِنْدَهَا", "inda", "عِنْدَ", "هَا", "pron-3fs", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«by them» — a place adverbial, annexed to the pronoun.", "«onların yanında» — mekân zarfı, zamire muzâf.", tags=[MF, ID], punct=punct)
def saru(full="وَصَارُوا", wa=True):
    return tok(full, "sara", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "صَارُوا فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا.", ("«and» + " if wa else "") + "«they came to» — ṣāra, a sister of kāna; the wāw is its ism.", ("«ve» + " if wa else "") + "«… oldular» — kâne'nin kız kardeşi sâra; vâv ismi.", segments=(wa_("صَارُوا", "sara", "verb") if wa else None))
def idol(full, lex, en, tr, punct=None, mamnu=False):
    return tok(full, lex, "propn", [MK] + ([MM] if mamnu else []), "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ صَنَمٍ" + ("، عَلَمٌ عَلَى وَزْنِ الْفِعْلِ مَمْنُوعٌ مِنَ الصَّرْفِ" if mamnu else "") + ".", en + " — the khabar; the name of an idol" + (", a diptote on a verb's pattern" if mamnu else "") + ".", tr + " — haber; bir put adı" + (", fiil vezninde gayr-i munsarif" if mamnu else "") + ".", punct=punct)
def wa_ishara(full, lex, en, tr):
    return tok(full, lex, "pron", [AT, "asma-al-ishara", MK], "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and» + " + en + " — a demonstrative, built; the mubtada.", "«ve» + " + tr + " — ism-i işâret; mübtedâ.", segments=wa_(full[2:], lex, "pron"))
def a_li_hadha(verb_ar):
    return tok("أَلِهٰذَا", "hadha", "pron", [IS, HJ, "asma-al-ishara"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَاسْمُ الْإِشَارَةِ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ" + verb_ar + ".", "«is it for this [that]» — the denying question's hamza + the lām of cause + the demonstrative.", "«bunun için mi» — inkârî istifham hemzesi + ta'lil lâmı + ism-i işâret.", segments=[seg("أَ", "a-istifham", "part"), seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")])
def billah(punct=None): return tok("بِاللهِ", "allah", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«in God» — bi + the name of God.", "«Allah'a» — bi + lafza-i celâl.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")])
def inna_hadha_zulm(punct="!"):
    return [inna(),
            tok("هٰذَا", "hadha", "pron", [IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«this» — the demonstrative; inna's ism.", "«bu» — ism-i işâret; inne'nin ismi."),
            tok("لَظُلْمٌ", "zulm", "noun", [IW], "اللَّامُ الْمُزَحْلَقَةُ، وَظُلْمٌ خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«[is] a wrong» — the slid lām + inna's khabar.", "«bir zulümdür» — müzahlaka lâm + inne'nin haberi.", segments=[seg("لَ", "la-ibtida", "part"), seg("ظُلْمٌ", "zulm", "noun")]),
            naat("عَظِيمٌ", "azim", "«great»", "«büyük»", case="raf", punct=punct)]
def lakinna_nas_ma(full_verb, lex, en, tr, punct, tags=()):
    return [tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kız kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
            ism_inna("النَّاسَ", "nas", "«the people»", "«insanlar»", part="لٰكِنَّ"),
            tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
            tok(full_verb, lex, "verb", [IW, "la-nafiya"] + list(tags), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", en + " — a māḍī on the group's wāw; the clause is lākinna's khabar.", tr + " — cemaat vâvı üzere mâzî; cümle lâkinne'nin haberi.", punct=punct)]

# ---------------------------------------------------------------- § the small helpers shared with chapter 5
MH = "maful-fih"; IST = "istithna"
def idha(full="إِذَا", wa=False, punct=None):
    return tok(full, "idha", "part", ["idha-shartiyya"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", ("«and» + " if wa else "") + "«when» — the conditional time-adverb, built.", ("«ve» + " if wa else "") + "«-dığı zaman» — şart mânâlı zaman zarfı, mebnî.", punct=punct, segments=(wa_("إِذَا", "idha", "part") if wa else None))
def arada_allah(full="وَأَرَادَ", wa=True, fa=False):
    c = "فَ" if fa else ("وَ" if wa else "")
    body = full[2:] if c else full
    pre = {"فَ": "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَ", "وَ": "الْوَاوُ عَاطِفَةٌ، وَ", "": ""}[c]
    return [tok(full, "arada", "verb", ([AT] if c else []) + ["hollow-verbs", "form-iv-verbs"], pre + body + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ الْإِفْعَالِ (أَرَادَ يُرِيدُ).",
                ({"فَ": "«so» + ", "وَ": "«and» + ", "": ""}[c]) + "«willed» — a māḍī of Form IV, hollow.", ({"فَ": "«bunun üzerine» + ", "وَ": "«ve» + ", "": ""}[c]) + "«diledi» — if'âl bâbından ecvef mâzî.",
                segments=([seg(c, "fa" if c == "فَ" else "wa", "conj"), seg(body, "arada", "verb")] if c else None)),
            allah_fail()]
def an_yursila(full="يُرْسِلَ", obj_of="فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِأَرَادَ"):
    return [an_nasb(obj_of, "«to»", "«… -mesini»"),
            tok(full, "arsala", "verb", [AN, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«send» — naṣb by an; the doer (God) is concealed.", "«göndermesini» — en ile mansub; fâil gizli (O).")]
def yukallimuhum(wa=False, punct=None, role=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ"):
    full = "وَيُكَلِّمُهُمْ" if wa else "يُكَلِّمُهُمْ"
    return tok(full, "kallama", "verb", ([AT] if wa else []) + ["mudari-marfu", MB, "form-ii-verbs", NA], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "يُكَلِّمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ" + role + ".",
               ("«and» + " if wa else "") + "«who speaks to them» — the muḍāriʿ clause is a ṣifa of the indefinite noun before it.", ("«ve» + " if wa else "") + "«onlarla konuşan» — muzâri cümlesi, önceki nekre ismin sıfatı.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("يُكَلِّمُ", "kallama", "verb"), seg("هُمْ", "pron-3mp", "pron")])
def wa_yansah(punct="."):
    return [mudari_wa("وَيَنْصَحُ", "nasaha", "«and counsels»", "«ve öğüt verir»", tags=[NA], extra=" — مَعْطُوفٌ عَلَى جُمْلَةِ الصِّفَةِ"),
            li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«them» — the counselled, after li.", "«onlara» — li'den sonra.", punct=punct)]
def inna_allah_la(verb, lex, en, tr, tags=()):
    return [inna(), allah_ism(), la_nafiya(),
            tok(verb, lex, "verb", [IW, "la-nafiya", "mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", en + " — the verbal clause is inna's khabar.", tr + " — fiil cümlesi inne'nin haberi.")]
def wahidan_wahidan(punct):
    return [maful_("وَاحِدًا", "wahid", "«one»", "«birer»"),
            tok("وَاحِدًا", "wahid", "noun", ["tawkid"], "تَوْكِيدٌ لَفْظِيٌّ مَنْصُوبٌ بِالْفَتْحَةِ — التَّكْرَارُ لِلتَّفْصِيلِ: وَاحِدًا بَعْدَ وَاحِدٍ.", "«by one» — the repeated word: one by one.", "«birer» — tekrar: tek tek.", punct=punct)]
def inna_muluk_la(verb, lex, en, tr, tags=()):
    return [inna(), ism_inna("الْمُلُوكَ", "malik-king", "«the kings»", "«krallar»", tags=[JT]), la_nafiya(),
            khamsa(verb, lex, en, tr, tags=[IW, "la-nafiya"] + list(tags), extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ")]
def kull_ahad(case, punct=None, role=""):
    C = {"nasb": ("مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", [MB, ID]), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", [HJ, ID]), "raf": ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", [FL, ID])}[case]
    return [tok("كُلَّ" if case == "nasb" else ("كُلِّ" if case == "jarr" else "كُلُّ"), "kull", "noun", C[1], C[0] + "، مُضَافٌ" + role + ".", "«every» — annexed.", "«her» — muzâf."),
            mudaf_ilayh("أَحَدٍ", "ahad", "«one»", "«bir(i)»", punct=punct)]
def ifal_kadha(punct, wa=False):
    return [tok("افْعَلْ", "faala", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — وَهَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«do» — an imperative, built on sukūn; the doer «you» is concealed.", "«yap» — sükûn üzere mebnî emir; fâil gizli (sen)."),
            tok("كَذَا", "kadha", "part", [MB], "كِنَايَةٌ عَنِ الْفِعْلِ، فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«such-and-such» — stands for the thing to do; the object.", "«şöyle» — yapılacak şeyin yerini tutar; mef'ûl.", punct=punct)]
def yaqul_lahu(full, pl=False):
    stem = full[2:] if full.startswith("وَ") else full
    if pl: v = khamsa(full, "qala", "«saying»", "«diyerek»", tags=["hollow-verbs", HL], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ")
    else: v = tok(full, "qala", "verb", ["mudari-marfu", "hollow-verbs", HL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«saying» — the clause is a ḥāl.", "«diyerek» — cümle hâl.")
    return [v, li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»")]
def pron_mubtada(full, lex, en, tr, wa=False, punct=None):
    return tok(full, lex, "pron", ([AT] if wa else []) + [MK], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + (full[2:] if wa else full) + " ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", ("«and» + " if wa else "") + en + " — a detached pronoun; the mubtadaʾ.", ("«ve» + " if wa else "") + tr + " — munfasıl zamir; mübtedâ.", punct=punct, segments=(wa_(full[2:], lex, "pron") if wa else None))
def khabar(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [MK] + list(tags), "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ" + extra + ".", en + " — the khabar.", tr + " — haber.", punct=punct)
def idha_kana_rasul(khabar_form, lex, en, tr):
    return [idha("وَإِذَا", wa=True), kana("كَانَ", wa=False), ism_kana("الرَّسُولُ", "rasul", "«the messenger»", "«elçi»"),
            khabar_kana(khabar_form, lex, en, tr)]
def qala_nas(punct=":"):
    return [tok("قَالَ", "qala", "verb", ["hollow-verbs", MB, "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — جَوَابُ إِذَا، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«[then] say» — the answer of idhā; what is said is its object.", "«derler» — izâ'nın cevabı; söylenen söz mef'ûl."), nas_fail(punct=punct)]
def qala_jawab(punct=None):
    return tok("قَالَ", "qala", "verb", ["hollow-verbs", MB, "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جَوَابُ إِذَا، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«[then] he says» — the answer of idhā; the doer is the messenger.", "«der» — izâ'nın cevabı; fâil gizli (elçi).", punct=punct)
def mudari1(full, lex, en, tr, hidden, punct=None, tags=(), wa=False, fa=False, extra=""):
    c = "فَ" if fa else ("وَ" if wa else "")
    body = full[2:] if c else full
    pre = {"فَ": "الْفَاءُ عَاطِفَةٌ، وَ", "وَ": "الْوَاوُ عَاطِفَةٌ، وَ", "": ""}[c]
    return tok(full, lex, "verb", ([AT] if c else []) + ["mudari-marfu"] + list(tags), pre + body + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: " + hidden + extra + ".",
               ({"فَ": "«so» + ", "وَ": "«and» + ", "": ""}[c]) + en + " — a muḍāriʿ; the doer «" + {"نَحْنُ": "we", "أَنَا": "I", "أَنْتَ": "you"}[hidden] + "» is necessarily concealed.", ({"فَ": "«o hâlde» + ", "وَ": "«ve» + ", "": ""}[c]) + tr + " — muzâri; fâil vücûben gizli (" + {"نَحْنُ": "biz", "أَنَا": "ben", "أَنْتَ": "sen"}[hidden] + ").", punct=punct, segments=([seg(c, "fa" if c == "فَ" else "wa", "conj"), seg(body, lex, "verb")] if c else None))
def mudari1_pron(full, lex, stem, hidden, en, tr, punct=None, wa=False, tags=()):
    return tok(full, lex, "verb", ([AT] if wa else []) + ["mudari-marfu", MB] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: " + hidden + "، وَالْهَاءُ مَفْعُولٌ بِهِ.", ("«and» + " if wa else "") + en + " — the muḍāriʿ with its object pronoun.", ("«ve» + " if wa else "") + tr + " — mef'ûl zamirli muzâri.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "verb"), seg("هُ", "pron-3ms", "pron")])
def lana_ahl(full_li, pron_form, pron_lex, en_li, tr_li, punct=None):
    return [tok(full_li, "li", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and " + en_li + "» — a fronted khabar.", "«ve " + tr_li + "» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg(full_li[2:3] + full_li[3:4], "li", "prep"), seg(pron_form, pron_lex, "pron")]),
            tok("أَهْلٌ", "ahl", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«family» — the delayed mubtadaʾ.", "«aile» — sonraya bırakılmış mübtedâ."),
            atf("وَذُرِّيَّةٌ", "dhurriyya", "«offspring»", "«zürriyet»", case="raf", punct=punct)]
def fa_kayfa():
    return tok("فَكَيْفَ", "kayfa", "noun", [AT, IS, HL], "الْفَاءُ لِلتَّفْرِيعِ (عَاطِفَةٌ)، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«so how» — the question noun, in the place of a ḥāl.", "«o hâlde nasıl» — soru ismi, mahallen mansub hâl.", segments=[seg("فَ", "fa", "conj"), seg("كَيْفَ", "kayfa", "noun")])
def la_khamsa(full, lex, en, tr, punct=None, tags=(), wa=False):
    return khamsa(full, lex, en, tr, tags=["la-nafiya"] + list(tags), punct=punct, wa=wa)
def innaka(wa=False):
    full = "وَإِنَّكَ" if wa else "إِنَّكَ"
    return tok(full, "inna", "part", ([AT] if wa else []) + [IW], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", ("«and» + " if wa else "") + "«indeed you» — inna with its ism, the attached kāf.", ("«ve» + " if wa else "") + "«şüphesiz sen» — inne + ismi olan bitişik kâf.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")])
def la_mudari2(full, lex, en, tr, punct=None, tags=(), wa=False, first=False):
    pre = "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ، وَ" if wa else ""
    body = full[4:] if wa else full
    role = " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ" if first else ""
    return tok(full, lex, "verb", ([AT] if wa else []) + ["la-nafiya", "mudari-marfu"] + ([IW] if first else []) + list(tags), pre + body + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ" + role + ".", ("«and … not» + " if wa else "") + en + " — the doer «you» is concealed" + ("; the clause is inna's khabar." if first else "."), ("«ve … -mezsin» + " if wa else "") + tr + " — fâil gizli (sen)" + ("; cümle inne'nin haberi." if first else "."), punct=punct, segments=([seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part"), seg(body, lex, "verb")] if wa else None))
def daiman(punct=None):
    return tok("دَائِمًا", "daiman", "noun", [MH], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (صِفَةٌ نَابَتْ عَنِ الظَّرْفِ: وَقْتًا دَائِمًا).", "«always» — a time adverbial.", "«daima» — zaman zarfı.", punct=punct)

# ---------------------------------------------------------------- § the small helpers shared with chapter 7
def nuh_fail(full="نُوحٌ", punct=None): return tok(full, "nuh", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the doer.", "«Nûh» — fâil.", punct=punct)
def nuh_ism_kana(punct=None): return tok("نُوحٌ", "nuh", "propn", [KN], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«Nūḥ» — kāna's ism.", "«Nûh» — kâne'nin ismi.", punct=punct)
def qawm_pron(full, pron_form, pron_lex, ar_role, en, tr, punct=None, tags=()):
    return noun_pron(full, "qawm", full[:len(full) - len(pron_form)], pron_form, pron_lex, ar_role, en, tr, tags=list(tags), punct=punct)
DF = "damir-fasl"; YM = "ya-al-mutakallim"; VM = "vocative-munada"; AM2 = "anwa-ma"; NW = "huruf-jarr-nawadir"; TW = "tawkid"; QD = "qad-harf"
def yarawna(full="يَرَوْنَ", wa=False):
    return tok(full, "raa", "verb", [KN, AK, "mudari-marfu", "naqis-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ: يَرَى + ونَ)، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ يَسُدُّ مَسَدَّ مَفْعُولَيْهِ.", "«used to hold» — a muḍāriʿ of the five, its final yāʾ dropped before the wāw; kāna's khabar; the anna-clause fills the seat of its two objects.", "«görüyorlardı / sayıyorlardı» — beş fiilden; lâm-ı fiil düştü; kâne'nin haberi; enne cümlesi iki mef'ûlün yerini tutar.")
def yara(full="يَرَى"):
    return tok(full, "raa", "verb", [KN, "mudari-marfu", "naqis-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ يَسُدُّ مَسَدَّ مَفْعُولَيْهِ.", "«held» — the muḍāriʿ with its ḍamma estimated on the alif; kāna's khabar.", "«görüyordu / sayıyordu» — damme elif üzerinde takdîrî; kâne'nin haberi.")
def anna_(wa=False, obj="يَرَى"):
    return anna(wa=wa, obj_of=obj)
def ibadat_asnam(case="nasb", part="أَنَّ", punct=None):
    ar = {"nasb": "اسْمُ " + part + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."}[case]
    return [tok("عِبَادَةَ", "ibada", "noun", [IW, ID], ar, "«the worship [of]» — anna's ism, annexed.", "«… -e tapmak» — enne'nin ismi, muzâf."),
            mudaf_ilayh("الْأَصْنَامِ", "sanam", "«the idols»", "«putlara»", punct=punct, tags=[JT])]
def huwa_fasl(en="«is»", tr="«-dır»"):
    return tok("هُوَ", "huwa", "pron", [DF, IW], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ (وَيَجُوزُ جَعْلُهُ مُبْتَدَأً وَمَا بَعْدَهُ خَبَرُهُ) — جَاءَ مُذَكَّرًا لِأَنَّ الْخَبَرَ مُذَكَّرٌ.", "«it» — the pronoun of separation between anna's ism and khabar, with no place in iʿrāb (or a mubtadaʾ with the next word as its khabar); masculine, agreeing with the khabar.", "«o / -dır» — isim ile haber arasındaki fasıl zamiri, i'râbdan mahalli yok (ya da mübtedâ); habere uyarak müzekker.")
def khabar_anna(full, lex, en, tr, punct=None, tags=()):
    return khabar_inna(full, lex, en, tr, part="أَنَّ", punct=punct, tags=list(tags))
def fi_dalala(punct=None, role=""):
    return [fi(), majrur("ضَلَالَةٍ", "dalalah-error", "«error»", "«sapıklık»", ar="مَجْرُورٌ بِالْكَسْرَةِ" + role + "."), atf("وَسَفَاهَةٍ", "sifaha", "«folly»", "«ve beyinsizlik»", case="jarr", punct=punct)]
def asnam_maful(punct=None): return maful_("الْأَصْنَامَ", "sanam", "«the idols»", "«putlara»", punct=punct, tags=[JT])
def kanu_yabuduna(wa=False, punct=None):
    return [kana_pl("وَكَانُوا" if wa else "كَانُوا", wa=wa), khamsa("يَعْبُدُونَ", "abada", "«worship»", "«tapıyorlardı»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ")]
def ya_qawmi():
    return [tok("يَا", "ya-nida", "part", [VM], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("قَوْمِ", "qawm", "noun", [VM, ID, YM], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا.", "«my people» — the munādā, annexed to the dropped yāʾ of the speaker: the kasra marks it.", "«kavmim» — münâdâ, hazfedilmiş mütekellim yâ'sına muzâf; kesre onun delili.")]

# ---------------------------------------------------------------- § chapter 8's own small helpers
def nuh_maful(punct=None, extra=""):
    return tok("نُوحًا", "nuh", "propn", [MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ (ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ)" + extra + ".", "«Nūḥ» — the object; the name takes tanwīn (three letters, the middle one still).", "«Nûh» — mef'ûl; üç harfli, ortası sâkin olduğu için tenvinli.", punct=punct)
def haulai(case, role_ar, en, tr, punct=None, tags=()):
    return tok("هٰؤُلَاءِ", "haulai", "pron", ["asma-al-ishara"] + list(tags), "اسْمُ إِشَارَةٍ لِلْجَمْعِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ " + {"raf": "رَفْعٍ", "nasb": "نَصْبٍ", "jarr": "جَرٍّ"}[case] + " " + role_ar + ".", en, tr, punct=punct)
def masakin(case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok("الْمَسَاكِينَ" if case != "raf" else "الْمَسَاكِينُ", "miskin", "noun", [BD, JT] + list(tags), role_ar + " " + C + " — جَمْعُ مِسْكِينٍ عَلَى مَفَاعِيلَ.", en, tr, punct=punct)
def lakin_light(full="وَلٰكِنْ", punct=None):
    return tok(full, "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin: no government.", "«fakat» — tahfif edilmiş lâkin; amel etmez.", punct=punct, segments=wa_("لٰكِنْ", "lakin", "part"))
def ma_amana(full="آمَنَ", wa=False):
    toks = [tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
            mazi(full, "aamana", "«believed»", "«iman etti»", tags=["form-iv-verbs", "la-nafiya"], hidden=None, extra_ar=" (الْفَاعِلُ بَعْدَ إِلَّا)")]
    return toks
def illa_mufarragh(punct=None):
    return tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ: الْكَلَامُ مَنْفِيٌّ وَالْمُسْتَثْنَى مِنْهُ مَحْذُوفٌ، فَمَا بَعْدَهَا يَأْخُذُ إِعْرَابَ الْفِعْلِ.", "«but» — the «emptied» exception: the word after it takes the verb's own case.", "«ancak, -den başka» — müferrağ istisnâ: sonraki kelime fiilin i'râbını alır.", punct=punct)
def bad_afrad(role="فَاعِلٌ", en="«some of the individuals»", tr="«bazı kimseler»"):
    return [tok("بَعْضُ", "baad", "noun", [FL, ID], role + " مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«some [of]» — the doer (after illā), annexed.", "«bazısı» — fâil (illâ'dan sonra), muzâf."),
            mudaf_ilayh("الْأَفْرَادِ", "fard-single", en, tr, tags=[JT])]
def nuh_ism_inna_light(punct=None):
    return tok("نُوحًا", "nuh", "propn", [IW], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — lākinna's ism.", "«Nûh» — lâkinne'nin ismi.", punct=punct)


# ---------------------------------------------------------------- § chapter 9's own small helpers
def laysa_bi(full, lex, en, tr, punct=None, wa=False, tags=()):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ""
    return tok(full, lex, "noun", ([AT] if wa else []) + [HJ, KN] + list(tags), pre + "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ" + full[(4 if wa else 2):] + " مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ لَيْسَ.", ("«and» + " if wa else "") + en + " — the added bāʾ on laysa's khabar: jarr in form, naṣb by place.", ("«ve» + " if wa else "") + tr + " — leyse'nin haberine gelen zâid bâ; lafzan mecrûr, mahallen mansub.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("بِ", "bi", "prep"), seg(full[(4 if wa else 2):], lex, "noun")])
def laysa_(full="لَيْسَ", wa=False, role=""):
    return tok(full, "laysa", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"] + ([MK] if role else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ" + role + ".", ("«and» + " if wa else "") + "«is not» — laysa with its concealed ism" + (": the clause is the khabar of the mubtadaʾ." if role else "."), ("«ve» + " if wa else "") + "«değildir» — leyse, ismi gizli" + ("; cümle mübtedânın haberi." if role else "."), segments=(wa_("لَيْسَ", "laysa", "verb") if wa else None))
def na_pron(full, lex, pos, stem_lex_part, ar, en, tr, tags=(), punct=None, wa=False):
    c = conj_of(full)
    segs = ([seg(c, "wa" if c == "وَ" else "fa", "conj")] if c else []) + [seg(full[(2 if c else 0):-1], stem_lex_part, pos), seg("ا", "pron-1p", "pron")]
    return tok(full, lex, pos, ([AT] if c else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
def lana(full="لَنَا", wa=False, role=" — خَبَرٌ مُقَدَّمٌ", en="«ours [is]» — a fronted khabar.", tr="«bizimdir» — öne alınmış haber.", punct=None, tags=(MK,)):
    return tok(full, "li", "prep", ([AT] if wa else []) + [HJ] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "اللَّامُ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ" + role + ".", ("«and» + " if wa else "") + en, ("«ve» + " if wa else "") + tr, punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("لَ", "li", "prep"), seg("نَا", "pron-1p", "pron")])
def kull_mubtada(punct=None): return tok("كُلُّ", "kull", "noun", [MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«every» — the delayed mubtadaʾ, annexed.", "«her» — sonraya bırakılmış mübtedâ, muzâf.", punct=punct)
def kull_jarr(punct=None): return tok("كُلِّ", "kull", "noun", [HJ, ID], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«every» — after the preposition, annexed.", "«her» — harf-i cerden sonra, muzâf.", punct=punct)
def mina(punct=None): return tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of / from» — its nūn takes a fatḥa before the next hamzat al-waṣl.", "«-den» — nûnu iki sâkin yüzünden fetha aldı.", punct=punct)
def a_la(punct=None):
    return tok("أَلَا", "hamza-istifham", "part", [IS, "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَا نَافِيَةٌ.", "«do … not?» — the question hamza of affirmation + the negating lā.", "«… -mez misiniz?» — takrîrî istifham hemzesi + nefiy lâ'sı.", punct=punct, segments=[seg("أَ", "hamza-istifham", "part"), seg("لَا", "la-nafiya", "part")])
def tanzuruna(punct=None): return khamsa("تَنْظُرُونَ", "nazara", "«you look»", "«bakmıyor musunuz»", tags=[IS, "la-nafiya"], punct=punct)
def ila_(punct=None): return prep("إِلَى", "ila", "«to / at»", "«-e»", punct=punct)
def kum_mim(full, lex, pre_form, pre_lex, en, tr, punct=None, tags=(), letter="حَرْفُ جَرٍّ"):
    return tok(full, lex, "prep", [HJ] + list(tags), pre_form + " " + letter + "، وَكُمْ فِي مَحَلِّ جَرٍّ، حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", en + " — the mīm of «you» takes a ḍamma before the next hamzat al-waṣl.", tr + " — mîm iki sâkin yüzünden damme aldı.", punct=punct, segments=[seg(pre_form, pre_lex, "prep"), seg("كُمُ", "pron-2mp", "pron")])
def wa_jaala(): return mazi("وَجَعَلَ", "jaala", "«and made»", "«ve kıldı»", tags=[AT, MX], wa=True, extra_ar=" — يَنْصِبُ مَفْعُولَيْنِ")
def obj1(full, lex, en, tr, punct=None): return tok(full, lex, "noun", [MB, MX], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the first object.", tr + " — birinci mef'ûl.", punct=punct)
def obj2(full, lex, en, tr, punct=None): return tok(full, lex, "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the second object.", tr + " — ikinci mef'ûl.", punct=punct)
def lakinna_qawm_nuh():
    return [tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kız kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
            tok("قَوْمَ", "qawm", "noun", [IW, ID], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the people [of]» — lākinna's ism, annexed.", "«kavmi» — lâkinne'nin ismi, muzâf.", ),
            tok("نُوحٍ", "nuh", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the muḍāf ilayh.", "«Nûh'un» — muzâfun ileyh."),
            tok("لَمْ", "lam-jazima", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«did not» — lam: it negates, jazms and turns the tense back.", "«-medi» — nefiy, cezm ve kalb harfi lem.")]
def lam_khamsa(full, lex, en, tr, punct=None, tags=(), role=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"):
    return tok(full, lex, "verb", [LJ, AK] + list(tags), "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ" + role + ".", en + " — jazm by the dropped nūn; the wāw is the doer.", tr + " — nûnun hazfiyle meczûm; vâv fâil.", punct=punct)
def wa_kayfa(): return tok("وَكَيْفَ", "kayfa", "noun", [AT, IS, HL], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — the question noun, in the place of a ḥāl.", "«ve nasıl» — soru ismi; mahallen mansub hâl.", segments=wa_("كَيْفَ", "kayfa", "noun"))
def mudari_fail_after(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.", en + " — a muḍāriʿ; the doer follows.", tr + " — muzâri; fâil sonra.", punct=punct)
def man_fail(): return tok("مَنْ", "man", "pron", [MW, FL], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«one who» — the relative; the doer.", "«… kimse» — ism-i mevsûl; fâil.")
def wa_daa_nuh_qawmahu(punct="،"):
    return [tok("وَدَعَا", "daa", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ (اسْتِئْنَافِيَّةٌ)، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and … called» — the defective māḍī, its fatḥa estimated on the alif.", "«ve çağırdı» — nâkıs mâzî, fethası elif üzerinde takdîrî.", segments=wa_("دَعَا", "daa", "verb")),
            nuh_fail(),
            qawm_pron("قَوْمَهُ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the object.", "«kavmini» — mef'ûl.", tags=[MB, ID], punct=punct)]

# ---------------------------------------------------------------- § chapter 10's own small helpers
def alf_sana(role_ar="ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — الْعَدَدُ أَلْفٌ يُضَافُ إِلَى مُفْرَدٍ مَجْرُورٍ", en="«a thousand» — a time adverbial by its annexed noun; the number alf takes a singular muḍāf ilayh.", tr="«bin» — zarf; elf sayısı tekil muzâfun ileyh alır.", tags=(MF, ID)):
    return [tok("أَلْفَ", "alf", "noun", list(tags), role_ar + ".", en, tr),
            tok("سَنَةٍ", "sana", "noun", [ID, "tamyiz"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — تَمْيِيزُ الْعَدَدِ.", "«year» — the muḍāf ilayh; the number's tamyīz.", "«yıl» — muzâfun ileyh; sayının temyizi."),
            tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ — الْكَلَامُ تَامٌّ مُوجَبٌ فَالْمُسْتَثْنَى وَاجِبُ النَّصْبِ.", "«less» — the exceptive; the sentence being complete and affirmative, what follows must take naṣb.", "«eksik» — istisnâ edatı; cümle tam ve müsbet olduğundan müstesnâ mansub."),
            tok("خَمْسِينَ", "khamsun", "noun", [IST, JS], "مُسْتَثْنًى مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ (أَلْفَاظُ الْعُقُودِ).", "«fifty» — the excepted, naṣb by the yāʾ: the tens decline like the sound plural.", "«elli» — müstesnâ; ukûd lafızları cemi müzekker sâlime mülhak, yâ ile mansub."),
            tok("عَامًا", "aam-year", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — تَمْيِيزُ الْعُقُودِ مُفْرَدٌ مَنْصُوبٌ.", "«years» — the tamyīz of the tens: singular, in naṣb.", "«yıl» — ukûdun temyizi: tekil, mansub.")]
def ila_mata(fa=False):
    return [tok("فَإِلَى" if fa else "إِلَى", "ila", "prep", ([AT] if fa else []) + [HJ, IS], ("الْفَاءُ لِلتَّفْرِيعِ، وَ" if fa else "") + "إِلَى حَرْفُ جَرٍّ.", ("«so» + " if fa else "") + "«until»", ("«o hâlde» + " if fa else "") + "«-e kadar»", segments=([seg("فَ", "fa", "conj"), seg("إِلَى", "ila", "prep")] if fa else None)),
            tok("مَتَى", "mata-istifham", "pron", [IS, HJ], "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِإِلَى.", "«when» — the question noun of time, in the place of jarr after ilā.", "«ne zamana» — zaman soru ismi; ilâ'dan sonra mahallen mecrûr.")]
def yara_(tags=(MB,)): return tok("يَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«will he see» — the ḍamma estimated on the alif.", "«görecek» — damme elif üzerinde takdîrî.")
def wa_lam(): return tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not» — lam.", "«ve … -medi» — lem.", segments=wa_("لَمْ", "lam-jazima", "part"))
def allahu_akbar(punct):
    return [tok("اللهُ", "allah", "propn", [MK], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«God» — the mubtadaʾ.", "«Allah» — mübtedâ."),
            tok("أَكْبَرُ", "akbar", "noun", [MK, "ism-tafdil", MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«[is] greatest» — the khabar; the elative, a diptote.", "«en büyüktür» — haber; ism-i tafdil, gayr-i munsarıf.", punct=punct)]
def innahu(sha=False):
    return tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ " + ("ضَمِيرُ الشَّأْنِ اسْمُهَا" if sha else "ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا") + ".", ("«indeed [it is so that]» — inna with the pronoun of the matter as its ism." if sha else "«indeed he» — inna + its ism."), ("«şu muhakkak ki» — inne + ismi olan şe'n zamiri." if sha else "«şüphesiz o» — inne + ismi."), segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")])

# ---------------------------------------------------------------- § chapter 11's own small helpers
def safina_kabira(punct=None):
    return [maful_("سَفِينَةً", "safina", "«a ship»", "«bir gemi»"), naat("كَبِيرَةً", "kabir", "«great»", "«büyük»", case="nasb", punct=punct)]
def ya_nuhu(punct=None):
    return [tok("يَا", "ya-nida", "part", [VM], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("نُوحُ", "nuh", "propn", [VM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Nūḥ» — a single proper name called: built on ḍamma, in the place of naṣb.", "«Nûh» — müfred alem münâdâ; damme üzere mebnî, mahallen mansub.", punct=punct)]
def sirta_najjaran(full="صِرْتَ", fa=False, punct=None):
    return [tok(("فَ" if fa else "") + full, "sara", "verb", ([AT] if fa else []) + [KN, "hollow-verbs"], ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "") + "صِرْتَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ اسْمُهُ — أَجْوَفُ حُذِفَتْ عَيْنُهُ (صِرْتَ).", ("«so» + " if fa else "") + "«you have become» — ṣāra before the tāʾ, its ism; the hollow verb drops its middle.", ("«ve böylece» + " if fa else "") + "«oldun» — tâ'dan önce sâra; tâ ismi; ecvef ortasını düşürür.", segments=([seg("فَ", "fa", "conj")] if fa else []) + [seg("صِرْ", "sara", "verb"), seg("تَ", "pron-2ms", "pron")]),
            tok("نَجَّارًا", "najjar", "noun", [KN, "sighat-mubalagha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ — فَعَّالٌ لِلْحِرْفَةِ.", "«a carpenter» — ṣāra's khabar; the فَعَّال of trades.", "«bir marangoz» — sâra'nın haberi; meslek bildiren fa''âl.", punct=punct)]
def a_tamshi_hadhihi(wa=False):
    return [tok("أَتَمْشِي", "masha", "verb", [IS, "mudari-marfu", "naqis-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتَمْشِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ بَعْدَهُ.", "«does … walk» — the question hamza; the defective muḍāriʿ; the doer follows.", "«… yürür mü» — soru hemzesi; nâkıs muzâri; fâil sonra.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَمْشِي", "masha", "verb")]),
            tok("هٰذِهِ", "hadhihi", "pron", [FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this [one]» — the doer.", "«bu» — fâil.")]
def am_(punct=None): return tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ لِلتَّعْيِينِ بَعْدَ هَمْزَةِ الِاسْتِفْهَامِ (الْمُتَّصِلَةُ).", "«or» — the am of choice after the question hamza.", "«yoksa» — soru hemzesinden sonra tayin bildiren em.", punct=punct)
def mudari_fail_after_(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.", en + " — a muḍāriʿ; the doer follows.", tr + " — muzâri; fâil sonra.", punct=punct)
def mudari_pron_fail_after(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "verb", ["mudari-marfu", MB] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.", en + " — the object pronoun aboard; the doer follows.", tr + " — mef'ûl zamir bitişik; fâil sonra.", punct=punct, segments=[seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")])
def kana_nuh_yasmau():
    return [kana(), nuh_ism_kana(),
            mudari("يَسْمَعُ", "samia", "«used to hear»", "«işitirdi»", tags=[KN, MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ")]

# ---------------------------------------------------------------- § chapter 12's own small helpers
def doubled(bab, yv, m, mm, d, dd, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    # حَجَّ template: the merge holds while the twin stays vowelled, breaks before a sukun-initial ending
    b = _sg.BABS[bab]
    return _sg.idgham(_sg.entry(b[0] + " — مُضَاعَفٌ", b[1], masdar, fail, _sg.mazi14(m, mm), _sg.mudari14(yv, d, dd), amr,
                                "يَ" + d + "َ", "يَ" + d + "َ", "تَ" + d + "َ", maful, pmz, pmd, note))
def wa_awha_allah_ila_nuh(punct=None):
    return [tok("وَأَوْحَى", "awha", "verb", [AT, "form-iv-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَوْحَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and … revealed» — the defective Form IV māḍī.", "«ve vahyetti» — if'âl bâbından nâkıs mâzî.", segments=wa_("أَوْحَى", "awha", "verb")),
            allah_fail(), ila_(),
            tok("نُوحٍ", "nuh", "propn", [HJ], "مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ»", "«Nûh'a»", punct=punct)]
def maa_pron(full, pron_form, pron_lex, en, tr, punct=None, tags=(), extra=""):
    return noun_pron(full, "maa", "مَعَ", pron_form, pron_lex, "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ" + extra + ".", en, tr, tags=[MF, ID] + list(tags), punct=punct)
def min_kull_hayawan_watair():
    return [prep("مِنْ", "min", "«of»", "«-den»"), kull_jarr(),
            mudaf_ilayh("حَيَوَانٍ", "hayawan", "«animal»", "«hayvandan»"),
            atf("وَطَائِرٍ", "tair", "«bird»", "«kuştan»", case="jarr", tags=["ism-fail"])]
def man_amana(role_ar, en, tr, bi_form, bi_pron_form, bi_pron_lex, bi_en, bi_tr, tags=()):
    return [tok("مَنْ", "man", "pron", [MW] + list(tags), "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ " + role_ar + ".", en, tr),
            mazi("آمَنَ", "aamana", "«believed»", "«iman etmiş»", tags=[MW, "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
            tok(bi_form, "bi", "prep", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ.", bi_en, bi_tr, segments=[seg("بِ", "bi", "prep"), seg(bi_pron_form, bi_pron_lex, "pron")])]

# ---------------------------------------------------------------- § chapter 13's own small helpers
def ibn_pron(full, pron_form, pron_lex, ar_role, en, tr, punct=None, tags=()):
    return noun_pron(full, "ibn", full[:len(full) - len(pron_form)], pron_form, pron_lex, ar_role + "، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", en, tr, tags=[ID] + list(tags), punct=punct)
def maa_kafirin(punct=None, role=""):
    return [tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ" + role + ".", "«with»", "«ile beraber»"),
            tok("الْكَافِرِينَ", "kafir", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the unbelievers» — jarr by the yāʾ.", "«kâfirler» — yâ ile mecrûr.", punct=punct)]
def mina_ma(punct=None): return [mina(), majrur("الْمَاءِ", "ma-water", "«the water»", "«sudan»", punct=punct)]


# ---------------------------------------------------------------- § chapter 15's own small helpers
def qila(full="وَقِيلَ", wa=True, punct=None):
    full = conj_full(full, wa); wa = wa and bool(conj_of(full))
    return tok(full, "qala", "verb", ([AT] if wa else []) + [NF, "hollow-verbs", MB], W(wa, full) + "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى الْقَوْلِ، وَالْجُمْلَةُ بَعْدَهُ مَقُولُ الْقَوْلِ — أَجْوَفُ: كُسِرَ أَوَّلُهُ وَقُلِبَتْ أَلِفُهُ يَاءً (قُوِلَ → قِيلَ).", Wen(wa, full) + "«it was said» — the passive of the hollow verb: its first letter takes kasra and the alif turns to yāʾ; what is said follows.", Wtr(wa, full) + "«denildi» — ecvef fiilin meçhulü: ilk harfi kesre alır, elif yâ'ya döner; söylenen söz ardından gelir.", punct=punct, segments=(conj_segs(full, "qala", "verb") if wa else None))
def bi_salam(punct=None):
    return bi_noun("بِسَلَامٍ", "salam", "«peace» — the phrase is a ḥāl: «safely».", "«selâmetle» — câr-mecrûr hâl.", punct=punct, tags=[HL], extra=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ حَالٌ (سَالِمًا)")
def nuh_mi(punct=None): return tok("نُوحٍ", "nuh", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the mudaf ilayh; the name takes tanwīn.", "«Nûh'un» — muzâfun ileyh; munsarif.", punct=punct)
def fiha_khabar(): return prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it» — kāna's fronted khabar.", "«onda» — kâne'nin öne alınmış haberi.", tags=[KN], extra_ar=" — خَبَرُ كَانَ مُقَدَّمٌ")
def salam_ala_nuh(sid):
    sen(sid, "«Peace be upon Nūḥ among all beings» (37:79).", "«Âlemler içinde Nûh'a selâm olsun» (37:79).", [
      *quran([
        tok("سَلَامٌ", "salam", "noun", [MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — نَكِرَةٌ سَوَّغَ الِابْتِدَاءَ بِهَا مَعْنَى الدُّعَاءِ.", "«peace» — the mubtadaʾ; an indefinite allowed to open the sentence because it is a prayer.", "«selâm» — mübtedâ; duâ mânası taşıdığı için nekre ile başlanmıştır."),
        prep("عَلَى", "ala", "«upon»", "«-e»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ."),
        tok("نُوحٍ", "nuh", "propn", [HJ, MK], "مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«Nūḥ» — the phrase is the khabar.", "«Nûh'a» — câr-mecrûr haber."),
        fi(),
        tok("الْعَالَمِينَ", "alam", "noun", [HJ, JS], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«all beings» — jarr by the yāʾ, a word attached to the sound plural.", "«âlemler» — cem-i müzekker sâlime mülhak; yâ ile mecrûr.", punct="."),
      ]),
    ])

# ---------------------------------------------------------------- §22 بَعْدَ الطُّوفَانِ (print pp. 32–33)
sen("s1", "And when what God had willed came to pass and the unbelievers had drowned, the sky held back and the water sank away.", "Allah'ın dilediği olup kâfirler boğulunca gök tutuldu ve su çekildi.", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ يَتَضَمَّنُ مَعْنَى الشَّرْطِ (حَرْفُ وُجُودٍ لِوُجُودٍ عِنْدَ بَعْضِهِمْ)، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِجَوَابِهِ.", "«and when» — lammā, «at the time that», with a condition's sense; it hangs on its answer.", "«ve … -ınca» — lemmâ, «… zaman» mânasında, şart anlamı taşır; cevabına bağlıdır.", segments=wa_("لَمَّا", "lamma", "part")),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى حَدَثَ وَوَقَعَ، يَكْتَفِي بِفَاعِلِهِ.", "«came to pass» — the full kāna, «happened», content with its doer.", "«oldu, vuku buldu» — tam kâne; fâili ile yetinir."),
  tok("مَا", "ma-mawsula", "pron", [MW, FL], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ كَانَ التَّامَّةِ.", "«what» — the relative, the doer of the full kāna.", "«… şey» — ism-i mevsûl; tam kâne'nin fâili."),
  tok("أَرَادَهُ", "arada", "verb", [MW, MB, "form-iv-verbs", "hollow-verbs"], "أَرَادَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْهَاءُ هِيَ الْعَائِدُ.", "«God had willed it» — the ṣila; the attached hāʾ is the returning pronoun.", "«Allah'ın dilediği» — sıla; bitişik hâ âiddir.", segments=[seg("أَرَادَ", "arada", "verb"), seg("هُ", "pron-3ms", "pron")]),
  allah_fail(),
  mazi("وَغَرِقَ", "ghariqa", "«and … drowned»", "«ve boğuldu»", tags=[AT], hidden=None, wa=True),
  fail("الْكُفَّارُ", "kafir", "«the unbelievers»", "«kâfirler»", tags=[JT]),
  mazi_ta("أَمْسَكَتِ", "amsaka", "«held back»", "«tutuldu, (yağmuru) tuttu»", tags=["form-iv-verbs"], extra="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ جَوَابُ لَمَّا"),
  fail("السَّمَاءُ", "sama", "«the sky»", "«gök»"),
  mazi("وَغَارَ", "ghara", "«and … sank away»", "«ve çekildi»", tags=[AT, "hollow-verbs"], hidden=None, wa=True),
  fail("الْمَاءُ", "ma-water", "«the water»", "«su»", punct="."),
])
sen("s2", "And the ship settled on Mount al-Jūdī, «and it was said: away with the wrongdoing people» (11:44).", "Gemi Cûdî dağına oturdu, «ve denildi: zalimler topluluğu yok olsun» (11:44).", [
  mazi_ta_naqis("وَاسْتَوَتِ", "istawa", "«and … settled»", "«ve oturdu, yerleşti»", tags=["form-viii-verbs"], wa=True),
  fail("السَّفِينَةُ", "safina", "«the ship»", "«gemi»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  tok("جَبَلِ", "jabal", "noun", [HJ, ID], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«Mount [of]» — annexed.", "«dağına» — muzâf."),
  tok("الْجُودِيِّ", "judi", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ عَلَى جَبَلٍ، مَنْسُوبٌ.", "«al-Jūdī» — the mudaf ilayh; the mountain's name, a nisba form.", "«Cûdî» — muzâfun ileyh; dağın adı, nisbet yâ'lı.", punct="،"),
  *quran([
    qila(),
    tok("بُعْدًا", "bud-perdition", "noun", ["maful-mutlaq", "hadhf-wa-taqdir"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: بَعُدُوا بُعْدًا — دُعَاءٌ عَلَيْهِمْ بِالْهَلَاكِ.", "«away [with]» — an absolute object of an understood verb («may they perish far away»), a curse.", "«yok olsun, uzak olsun» — mahzuf fiilin mef'ûl-i mutlakı; beddua."),
    tok("لِلْقَوْمِ", "qawm", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْقَوْمِ مَجْرُورٌ بِالْكَسْرَةِ.", "«to the people» — li + the noun.", "«topluluğa» — li + isim.", segments=[seg("لِ", "li", "prep"), seg("الْقَوْمِ", "qawm", "noun")]),
    tok("الظَّالِمِينَ", "zalim", "noun", [NA, JS, "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the wrongdoing» — the naʿt, jarr by the yāʾ.", "«zalim» — sıfat; yâ ile mecrûr.", punct="."),
  ]),
])
sen("s3", "And it was said: O Nūḥ, go down in peace.", "Ve denildi: ey Nûh, selâmetle in.", [
  qila(punct=":"),
  *ya_nuhu(),
  tok("اهْبِطْ", "habata", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — هَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«go down» — an imperative on sukūn; its hamza is a joining hamza.", "«in» — sükûn üzere mebnî emir; hemzesi vasıl hemzesi."),
  bi_salam(punct="."),
])
sen("s4", "And Nūḥ and the ship's company went down, walking on the land in peace.", "Nûh ve gemi halkı indiler, karada selâmetle yürüyorlardı.", [
  mazi("وَهَبَطَ", "habata", "«and … went down»", "«ve indi»", tags=[AT], hidden=None, wa=True),
  nuh_fail(),
  tok("وَأَصْحَابُ", "sahib", "noun", [AT, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَأَصْحَابُ مَعْطُوفٌ عَلَى نُوحٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«and the company [of]» — joined to Nūḥ, annexed.", "«ve … halkı» — Nûh'a ma'tûf, muzâf.", segments=wa_("أَصْحَابُ", "sahib", "noun")),
  mudaf_ilayh("السَّفِينَةِ", "safina", "«the ship»", "«geminin»"),
  khamsa("يَمْشُونَ", "masha", "«walking»", "«yürüyorlardı»", tags=[HL, "naqis-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  prep("عَلَى", "ala", "«on»", "«-de»"),
  majrur("الْبَرِّ", "barr-land", "«the land»", "«karada»"),
  bi_salam(punct="."),
])
sen("s5", "And the unbelievers of Nūḥ's people perished, and neither the sky nor the earth wept for them.", "Nûh kavminin kâfirleri helâk oldu; onlara ne gök ağladı ne yer.", [
  mazi("وَهَلَكَ", "halaka", "«and … perished»", "«ve helâk oldu»", tags=[AT], hidden=None, wa=True),
  fail("الْكُفَّارُ", "kafir", "«the unbelievers»", "«kâfirler»", tags=[JT]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  tok("قَوْمِ", "qawm", "noun", [HJ, ID], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«the people [of]»", "«kavminden»"),
  nuh_mi(),
  tok("فَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْفَاءُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and … not» — the negating mā.", "«ve … -medi» — nefiy mâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  tok("بَكَتْ", "baka", "verb", ["naqis-verbs", "la-nafiya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«wept» — the defective māḍī before the feminine tāʾ: its alif dropped (بَكَى → بَكَتْ).", "«ağladı» — nâkıs mâzî, te'nis tâ'sı önünde elifi düşer (bekâ → beket)."),
  prep_pron("عَلَيْهِمُ", "ala", "هِمُ", "pron-3mp", "«for them»", "«onlara»", extra_ar="، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("السَّمَاءُ", "sama", "«the sky»", "«gök»"),
  atf("وَالْأَرْضُ", "ard", "«the earth»", "«yer»", case="raf", punct="."),
])
sen("s6", "And God blessed the offspring of Nūḥ, and they spread over the earth and filled the earth.", "Allah Nûh'un zürriyetini bereketlendirdi; yeryüzüne yayıldılar ve yeri doldurdular.", [
  mazi("وَبَارَكَ", "baraka-bless", "«and … blessed»", "«ve bereket verdi»", tags=[AT, "form-iii-verbs"], hidden=None, wa=True),
  allah_fail(),
  fi(),
  tok("ذُرِّيَّةِ", "dhurriyya", "noun", [HJ, ID], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«the offspring [of]»", "«zürriyetine»"),
  nuh_mi(),
  mazi_ta("فَانْتَشَرَتْ", "intashara", "«and they spread»", "«ve yayıldı»", tags=["form-viii-verbs"], wa=True, extra="، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ (الذُّرِّيَّةُ)"),
  fi(),
  majrur("الْأَرْضِ", "ard", "«the earth»", "«yeryüzüne»"),
  mazi_ta("وَمَلَأَتِ", "malaa", "«and filled»", "«ve doldurdu»", wa=True, extra="، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَحُرِّكَتِ التَّاءُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — مَهْمُوزُ اللَّامِ"),
  maful("الْأَرْضَ", "ard", "«the earth»", "«yeri»", punct="."),
])
sen("s7", "And in it there were nations, and in it there were prophets and kings.", "Onda ümmetler vardı; onda peygamberler ve krallar vardı.", [
  kana(),
  fiha_khabar(),
  ism_kana("أُمَمٌ", "umma", "«nations»", "«ümmetler»", tags=[JT], ar="اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ."),
  kana(),
  fiha_khabar(),
  ism_kana("أَنْبِيَاءُ", "nabi", "«prophets»", "«peygamberler»", tags=[JT, MM], ar="اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ."),
  atf("وَمُلُوكٌ", "malik-king", "«kings»", "«krallar»", case="raf", tags=[JT], punct="."),
])
salam_ala_nuh("s8")
salam_ala_nuh("s9")

CAND = {
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "lamma": G("lamma", "لَمَّا", None, "part", "when (with a past verb)", "-ınca, -dığı zaman", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (المَوْصُولَة)", None, "pron", "that which, what", "-dığı şey (mevsûle)", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to will, to want", "dilemek, istemek", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "his / its (attached pronoun)", "onun (bitişik)", 1),
 "allah": G("allah", "اللَّه", None, "propn", "Allah", "Allah", 1),
 "ghariqa": G("ghariqa", "غَرِقَ", "غ ر ق", "verb", "to drown", "boğulmak", 1),
 "kafir": G("kafir", "كَافِر", "ك ف ر", "noun", "unbeliever (ism fa'il)", "kâfir, inkârcı", 1),
 "amsaka": G("amsaka", "أَمْسَكَ", "م س ك", "verb", "to hold back, to withhold; to seize (Form IV)", "tutmak, alıkoymak (if'âl bâbı)", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "heaven, sky", "gök, semâ", 1),
 "ghara": G("ghara", "غَارَ", "غ و ر", "verb", "to sink into the ground, to subside (hollow: غَارَ الْمَاءُ يَغُورُ)", "(su) çekilmek, yere batmak (ecvef: ğâre yeğûru)", 1),
 "ma-water": G("ma-water", "مَاء", "م و ه", "noun", "water", "su", 1, plural="مِيَاه"),
 "istawa": G("istawa", "اِسْتَوَى", "س و ي", "verb", "to be equal, level; to settle (اِسْتَوَى عَلَى)", "eşit olmak; (üzerine) oturmak, yerleşmek", 1),
 "safina": G("safina", "سَفِينَة", "س ف ن", "noun", "ship", "gemi", 1, plural="سُفُن"),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, üzere", 1),
 "jabal": G("jabal", "جَبَل", "ج ب ل", "noun", "mountain", "dağ", 1, plural="جِبَال"),
 "judi": G("judi", "الْجُودِيّ", None, "propn", "al-Jūdī — the mountain on which the ship of Nūḥ settled (11:44)", "Cûdî — Nûh'un gemisinin oturduğu dağ (11:44)", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "bud-perdition": G("bud-perdition", "بُعْد", "ب ع د", "noun", "distance, remoteness — بُعْدًا: «away with …!», a curse of perdition (the absolute object of an understood verb)", "uzaklık — bu'den: «yok olsun!», helâk bedduası (mahzuf fiilin mef'ûl-i mutlakı)", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "people, folk", "kavim, topluluk", 1),
 "zalim": G("zalim", "ظَالِم", "ظ ل م", "noun", "wrongdoer (ism fa'il)", "zalim (ism-i fâil)", 1, plural="ظَالِمُونَ"),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O! (vocative)", "ey! (nidâ)", 1),
 "nuh": G("nuh", "نُوح", None, "propn", "Nūḥ (Noah)", "Nûh", 1),
 "habata": G("habata", "هَبَطَ", "ه ب ط", "verb", "to go down, to descend (هَبَطَ يَهْبِطُ)", "inmek (hebeta yehbitu)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by, in", "ile", 1),
 "salam": G("salam", "سَلَام", "س ل م", "noun", "peace", "selâm, esenlik", 1),
 "sahib": G("sahib", "صَاحِب", "ص ح ب", "noun", "companion", "arkadaş, sahip", 1, plural="أَصْحَاب"),
 "masha": G("masha", "مَشَى", "م ش ي", "verb", "to walk", "yürümek", 1),
 "barr-land": G("barr-land", "بَرّ", "ب ر ر", "noun", "dry land (as against the sea)", "kara (denizin karşıtı)", 1),
 "halaka": G("halaka", "هَلَكَ", "ه ل ك", "verb", "to perish, be destroyed", "helâk olmak", 1),
 "min": G("min", "مِنْ", None, "prep", "from; of", "-den", 1),
 "fa": G("fa", "فَ", None, "conj", "so, for (fa)", "bunun üzerine", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (negating ma)", "değil, -medi (nefiy mâ'sı)", 1),
 "baka": G("baka", "بَكَى", "ب ك ي", "verb", "to weep (naqis: بَكَى يَبْكِي)", "ağlamak (nâkıs: bekâ yebkî)", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their (attached)", "onlar, onların (bitişik)", 1),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "earth, land", "yer, yeryüzü", 1),
 "baraka-bless": G("baraka-bless", "بَارَكَ", "ب ر ك", "verb", "to bless (بَارَكَ فِي: to put blessing into)", "bereket vermek (bâreke fî)", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "dhurriyya": G("dhurriyya", "ذُرِّيَّة", "ذ ر ر", "noun", "offspring, progeny", "zürriyet, soy", 1),
 "intashara": G("intashara", "اِنْتَشَرَ", "ن ش ر", "verb", "to spread, to become widespread (Form VIII)", "yayılmak (iftiâl bâbı)", 1),
 "malaa": G("malaa", "مَلَأَ", "م ل أ", "verb", "to fill (مَلَأَ يَمْلَأُ; hamzated in its last letter)", "doldurmak (melee yemleu; lâmı hemzeli)", 1),
 "pron-3fs": G("pron-3fs", "ـهَا", None, "pron", "her / its (attached pronoun)", "onun (dişil, bitişik)", 1),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "community, umma", "ümmet", 1, plural="أُمَم"),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "prophet", "peygamber, nebî", 1, plural="أَنْبِيَاء"),
 "malik-king": G("malik-king", "مَلِك", "م ل ك", "noun", "king", "kral, melik", 1, plural="مُلُوك"),
 "alam": G("alam", "عَالَم", "ع ل م", "noun", "the world, all that exists besides God", "âlem", 1, plural="عَالَمُونَ"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
put_morph(mo, "ghara", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "غَار", "غُر", "غُور", "غُر", "غُور", "غُر", "غَوْر", "غَائِر", None, None, None, "غَارَ الْمَاءُ يَغُورُ غَوْرًا: ذَهَبَ فِي الْأَرْضِ وَنَضَبَ — لَازِمٌ."))
put_morph(mo, "habata", _sg.sound1("daraba", "هَبَط", "هْبِط", "اِهْبِط", "هُبُوط", "هَابِط", None, None, None, "هَبَطَ يَهْبِطُ هُبُوطًا: نَزَلَ — لَازِمٌ، يَتَعَدَّى بِمِنْ وَإِلَى؛ وَيُقَالُ يَهْبُطُ أَيْضًا."))
put_morph(mo, "malaa", _sg.sound1("fataha", "مَلَأ", "مْلَأ", "اِمْلَأ", "مَلْء", "مَالِئ", "مَمْلُوء", "مُلِئَ", "يُمْلَأُ", "مَلَأَ الْإِنَاءَ يَمْلَأُهُ مَلْئًا: جَعَلَهُ مُمْتَلِئًا — مَهْمُوزُ اللَّامِ، يَتَعَدَّى إِلَى مَفْعُولٍ."))
put_morph(mo, "amsaka", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَمْسَك", "مْسِك", "أَمْسِك", "إِمْسَاك", "مُمْسِك", "مُمْسَك", "أُمْسِكَ", "يُمْسَكُ", "أَمْسَكَ الشَّيْءَ: قَبَضَ عَلَيْهِ وَحَبَسَهُ؛ وَأَمْسَكَتِ السَّمَاءُ: حَبَسَتْ مَطَرَهَا — بَابُ الْإِفْعَالِ."))
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch15 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 15 (print pp. 32–33; Nūḥ §22): after the flood — when what God had willed came to pass and the unbelievers had drowned, the sky held back and the water sank away; the ship settled on Mount al-Jūdī, «and it was said: away with the wrongdoing people» (11:44); «O Nūḥ, go down in peace»; Nūḥ and the ship's company walked on the land in peace; the unbelievers of Nūḥ's people perished and neither sky nor earth wept for them; God blessed the offspring of Nūḥ, and they spread and filled the earth with nations, prophets and kings; «peace be upon Nūḥ among all beings» (37:79) — printed twice, as the book prints it. The END of «the ship of Nūḥ».")
ADD_TR = (" On beşinci bölüm (basılı s. 32–33; Nûh §22): tufandan sonra — Allah'ın dilediği olup kâfirler boğulunca gök tutuldu ve su çekildi; gemi Cûdî dağına oturdu, «ve denildi: zalimler topluluğu yok olsun» (11:44); «ey Nûh, selâmetle in»; Nûh ve gemi halkı karada selâmetle yürüdüler; Nûh kavminin kâfirleri helâk oldu, onlara ne gök ağladı ne yer; Allah Nûh'un zürriyetini bereketlendirdi, yeryüzüne yayıldılar ve yeri doldurdular: ümmetler, peygamberler ve krallar; «âlemler içinde Nûh'a selâm olsun» (37:79) — kitapta basıldığı gibi iki kez. «Nûh'un gemisi»nin SONU.")
write_out(15, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §22, pp. 32–33", GLOSS_ADD, notes=(), related=())
report(15, S, GLOSS_ADD, ())
