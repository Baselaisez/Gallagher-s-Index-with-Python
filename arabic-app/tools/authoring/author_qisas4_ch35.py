# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 35: «قِصَّةُ عِيسَى» §14 (an old struggle: the chiefs and the rich turn away, with Sabaʾ 34:34–35), §15 (the common people and the poor believe: the fullers, the fishermen, the craftsmen) and §16 («we are the helpers of God», with 3:52–53 again); print pp. 49–51.
python3 tools/authoring/author_qisas4_ch35.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: صِرَاعٌ قَدِيمٌ، وَإِيمَانُ عَامَّةِ النَّاسِ وَفُقَرَائِهِمْ", "en": "The story of ʿĪsā: an old struggle; the common people and the poor believe", "tr": "Îsâ'nın kıssası: eski bir çatışma; halkın ve fakirlerin imanı"}
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
    return tok(full, lex, "verb", [AT, "mudari-marfu"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign + "، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", "«and» + " + en + " — a muḍāriʿ in rafʿ; the doer is concealed.", "«ve» + " + tr + " — merfû muzari; fâil gizli.", punct=punct, segments=wa_(full[2:], lex, "verb"))
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

# ---------------------------------------------------------------- §14 صِرَاعٌ قَدِيمٌ (print pp. 49–50)
sen("s1", "And there befell our master ʿĪsā what had befallen the prophets before him: the chiefs and leaders drew away from him, and the rich and strong deserted him,",
        "Efendimiz Îsâ'nın başına, ondan önceki peygamberlerin başına gelen geldi: reisler ve önderler ondan uzaklaştı; zenginler ve güçlüler onu terk etti;", [
  mazi("وَوَقَعَ", "waqaa", "«and there befell»", "«ve başına geldi»", tags=[AT, "mithal-verbs"], wa=True, hidden=None),
  tok("لِسَيِّدِنَا", "sayyid", "noun", [HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَسَيِّدِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«to our master»", "«efendimize»", segments=[seg("لِ", "li", "prep"), seg("سَيِّدِ", "sayyid", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("عِيسَى", "isa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ'nın»"),
  tok("مَا", "ma-mawsula", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«what» — the relative as the doer.", "«… şey» — fâil olan mevsûl."),
  mazi("وَقَعَ", "waqaa", "«had befallen»", "«başına gelen»", tags=[MW, "mithal-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةٌ"),
  li_noun("لِلْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberlerin»", tags=[JT]),
  noun_pron("قَبْلَهُ", "qabla", "قَبْلَ", "هُ", "pron-3ms", "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«before him»", "«ondan önceki»", tags=[MF, ID], punct="،"),
  tok("فَابْتَعَدَ", "ibtaada", "verb", [AT, "form-viii-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْصِيلِ)، وَابْتَعَدَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«so drew away» — the fāʾ opens the detail.", "«böylece uzaklaştı» — fâ tafsîli açar.", segments=[seg("فَ", "fa", "conj"), seg("ابْتَعَدَ", "ibtaada", "verb")]),
  prep_pron("عَنْهُ", "an", "هُ", "pron-3ms", "«from him»", "«ondan»"),
  fail("الرُّؤَسَاءُ", "rais", "«the chiefs»", "«reisler»", tags=[JT, MM]),
  atf("وَالزُّعَمَاءُ", "zaim", "«the leaders»", "«ve önderler»", "raf", tags=[JT, MM], punct="،"),
  v_pron("وَهَجَرَهُ", "hajara", "هَجَرَ", "هُ", "pron-3ms", "«and deserted him»", "«ve onu terk etti»", wa=True, hidden=None),
  fail("الْأَغْنِيَاءُ", "ghani", "«the rich»", "«zenginler»", tags=[JT, MM]),
  atf("وَالْأَقْوِيَاءُ", "qawi", "«the strong»", "«ve güçlüler»", "raf", tags=[JT, MM], punct="،"),
])
sen("s2", "and they saw in believing in him and following him a loss of face and a disgrace; and it weighed heavily on them to step down from what they held of leadership and chieftaincy, privilege and lordship. God Most High's word proved true:",
        "ona inanmakta ve ona uymakta bir küçülme ve ayıp gördüler; reislik ve önderlik, imtiyaz ve efendilik gibi sahip olduklarından vazgeçmek onlara ağır geldi. Allah Teâlâ'nın sözü doğru çıktı:", [
  mazi_wa_alif("وَرَأَوْا", "raa", "«and they saw»", "«ve gördüler»", wa=True, tags=[AT, MX]),
  fi(),
  majrur("الْإِيمَانِ", "iman", "«believing»", "«inanmakta»"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«in him»", "«ona»"),
  pron_atf("وَاتِّبَاعِهِ", "ittiba", "اتِّبَاعِ", "هِ", "pron-3ms", "«following him»", "«ona uymakta»", tags=["form-viii-verbs"]),
  maful_("غَضَاضَةً", "ghadada", "«a loss of face»", "«bir küçülme»"),
  atf("وَعَيْبًا", "ayb", "«a disgrace»", "«ve ayıp»", "nasb", punct="،"),
  mazi("وَشَقَّ", "shaqqa", "«and weighed heavily»", "«ve ağır geldi»", tags=[AT, "doubled-verbs"], wa=True, hidden=None),
  prep_pron("عَلَيْهِمُ", "ala", "هِمُ", "pron-3mp", "«on them»", "«onlara»", extra_ar=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("التَّنَازُلُ", "tanazul", "«stepping down»", "«vazgeçmek»", tags=["form-vi-verbs"]),
  tok("عَمَّا", "ma-mawsula", "pron", [HJ, MW], "عَنْ حَرْفُ جَرٍّ أُدْغِمَتْ نُونُهُ فِي مَا الْمَوْصُولَةِ، وَمَا فِي مَحَلِّ جَرٍّ.", "«from what» — ʿan fused into the relative mā.", "«… şeyden» — an, mevsûl mâ ile idgam edilmiş.", segments=[seg("عَ", "an", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  tok("كَانُوا", "kana", "verb", [MW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهُ — وَالْجُمْلَةُ صِلَةٌ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«they were» — the ṣila; its khabar is the following phrase.", "«idiler» — sıla; haberi sonraki ibare."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon [it]» — kāna's khabar.", "«üzerinde» — kâne'nin haberi.", tags=[KN], punct="،"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  majrur("رِئَاسَةٍ", "riasa", "«leadership»", "«reislik»"),
  atf("وَزَعَامَةٍ", "zaama", "«chieftaincy»", "«ve önderlik»", punct="،"),
  atf("وَامْتِيَازٍ", "imtiyaz", "«privilege»", "«imtiyaz»", tags=["form-viii-verbs"]),
  atf("وَسِيَادَةٍ", "siyada", "«lordship»", "«ve efendilik»", punct="،"),
  mazi("وَصَدَقَ", "sadaqa-be-true", "«and proved true»", "«ve doğru çıktı»", tags=[AT], wa=True, hidden=None),
  fail("قَوْلُ", "qawl", "«the word [of]»", "«sözü»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
])
sen("s3", "«And We never sent a warner to a town but its affluent ones said: We disbelieve in what you have been sent with.» (34:34)",
        "«Biz hangi beldeye bir uyarıcı gönderdiysek, oranın refah içinde şımaranları mutlaka: Biz sizinle gönderileni inkâr ediyoruz, dediler.» (34:34)", [
  *quran([
  tok("وَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and … never» — the negating mā.", "«ve … hiç» — nefiy mâ'sı.", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("أَرْسَلْنَا", "arsala", "verb", ["form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«We sent» — nā the doer.", "«gönderdik» — nâ fâil.", segments=[seg("أَرْسَلْ", "arsala", "verb"), seg("نَا", "pron-1p", "pron")]),
  fi(),
  majrur("قَرْيَةٍ", "qarya", "«a town»", "«bir beldeye»"),
  prep("مِنْ", "min", "«[any]»", "«bir»", ar="حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ."),
  tok("نَذِيرٍ", "nadhir", "noun", [MB], "مَفْعُولٌ بِهِ مَجْرُورٌ لَفْظًا بِمِنَ الزَّائِدَةِ مَنْصُوبٌ مَحَلًّا.", "«a warner» — the object, jarr in form by the extra min.", "«bir uyarıcı» — mef'ûl; zâid min ile lafzan mecrûr."),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — وَالْجُمْلَةُ بَعْدَهَا حَالٌ مِنْ قَرْيَةٍ (أَوْ صِفَةٌ لَهَا).", "«but» — an emptied exception; the following clause is a ḥāl of «a town».", "«mutlaka» — müferrağ istisnâ; sonraki cümle «belde»nin hâli."),
  mazi("قَالَ", "qala", "«said»", "«dediler»", tags=[HL, "hollow-verbs"], hidden=None),
  tok("مُتْرَفُوهَا", "mutraf", "noun", [FL, JS, ID, "ism-maful", "form-iv-verbs"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«its affluent ones» — the doer; rafʿ by the wāw, nūn dropped for the annexation.", "«oranın şımaranları» — fâil; vâv ile merfû, nûnu izâfet için düşmüş.", segments=[seg("مُتْرَفُو", "mutraf", "noun"), seg("هَا", "pron-3fs", "pron")]),
  tok("إِنَّا", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا — أَصْلُهُ إِنَّنَا.", "«indeed we» — inna with nā.", "«şüphesiz biz» — inne ile nâ.", segments=[seg("إِنَّ", "inna", "part"), seg("ا", "pron-1p", "pron")]),
  bi_ma(extra=" — مُتَعَلِّقٌ بِكَافِرُونَ، قُدِّمَ لِلِاهْتِمَامِ"),
  tok("أُرْسِلْتُمْ", "arsala", "verb", [MW, NF, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ صِلَةٌ.", "«you have been sent» — a passive; the ṣila.", "«gönderildiniz» — meçhul; sıla.", segments=[seg("أُرْسِلْ", "arsala", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with»", "«ile»"),
  tok("كَافِرُونَ", "kafir", "noun", [IW, JS, "ism-fail"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«disbelievers» — inna's khabar.", "«inkârcılar» — inne'nin haberi.", punct=AYA),
  ]),
])
sen("s4", "«And they said: We are greater in wealth and children, and we shall not be punished.» (34:35)",
        "«Ve dediler: Biz malca ve evlâtça daha çoğuz; biz azaba uğratılacak değiliz.» (34:35)", [
  *quran([
  mazi_pl("وَقَالُوا", "qala", "«and they said»", "«ve dediler»", tags=[AT, "hollow-verbs"], wa=True),
  tok("نَحْنُ", "nahnu", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — مَقُولُ الْقَوْلِ.", "«we» — the mubtadaʾ.", "«biz» — mübtedâ."),
  tok("أَكْثَرُ", "akthar", "noun", [MK, "ism-tafdil", MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«greater» — the khabar; an elative, a diptote.", "«daha çok» — haber; ism-i tafdîl, gayr-i munsarıf."),
  tok("أَمْوَالًا", "mal", "noun", ["tamyiz", JT], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — مُحَوَّلٌ عَنِ الْمُبْتَدَأِ: أَمْوَالُنَا أَكْثَرُ.", "«in wealth» — a tamyīz converted from the mubtadaʾ.", "«malca» — mübtedâdan dönüştürülmüş temyiz."),
  atf("وَأَوْلَادًا", "walad", "«in children»", "«ve evlâtça»", "nasb", tags=[JT, "tamyiz"]),
  tok("وَمَا", "ma-nafiya", "part", [AT, "ma-la-mushabbaha"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ (الْحِجَازِيَّةُ).", "«and … not» — the Ḥijāzī mā that governs like laysa.", "«ve … değil» — leyse gibi amel eden Hicâzî mâ.", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("نَحْنُ", "nahnu", "pron", ["ma-la-mushabbaha"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ مَا.", "«we» — mā's ism.", "«biz» — mâ'nın ismi."),
  tok("بِمُعَذَّبِينَ", "muadhdhab", "noun", [HJ, "ma-la-mushabbaha", JS, "ism-maful", "form-ii-verbs"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَمُعَذَّبِينَ خَبَرُ مَا مَجْرُورٌ لَفْظًا بِالْيَاءِ مَنْصُوبٌ مَحَلًّا.", "«punished» — mā's khabar after the extra bāʾ: jarr in form, naṣb in place.", "«azaba uğratılan» — zâid bâ'dan sonra mâ'nın haberi: lafzan mecrûr, mahallen mansub.", segments=[seg("بِ", "bi", "prep"), seg("مُعَذَّبِينَ", "muadhdhab", "noun")], punct=AYA),
  ]),
])
# ---------------------------------------------------------------- §15 إِيمَانُ عَامَّةِ النَّاسِ وَفُقَرَائِهِمْ (print pp. 50–51)
sen("s5", "And when ʿĪsā despaired of them, saw in them obstinacy and unbelief, and realized that they had denied what he had brought of clear signs and dazzling miracles that their own souls were certain of, and that they belittled him because he was not a man of power and means, he turned to the common people and the poor among them,",
        "Îsâ onlardan ümidini kesince, onlarda inat ve küfrü görünce, nefislerinin kesinlikle bildiği apaçık âyetleri ve göz kamaştırıcı mucizeleri inkâr ettiklerini ve güç ve servet sahibi olmadığı için onu küçümsediklerini anlayınca, halka ve onların fakirlerine yöneldi;", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -ınca»", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("يَئِسَ", "yaisa", "«despaired»", "«ümidini kesti»", tags=[ID], hidden=None, extra_ar=" — مَهْمُوزُ الْعَيْنِ؛ وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا"),
  tok("عِيسَى", "isa", "propn", [FL, MM, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — the doer.", "«Îsâ» — fâil."),
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«of them»", "«onlardan»", punct="،"),
  mazi("وَشَاهَدَ", "shahada-verb", "«and saw»", "«ve gördü»", tags=[AT, "form-iii-verbs"], wa=True, hidden="هُوَ"),
  prep_pron("فِيهِمُ", "fi", "هِمُ", "pron-3mp", "«in them»", "«onlarda»", extra_ar=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  maful_("الْعِنَادَ", "inad", "«obstinacy»", "«inadı»"),
  atf("وَالْكُفْرَ", "kufr", "«unbelief»", "«ve küfrü»", "nasb", punct="،"),
  mazi("وَرَأَى", "raa", "«and realized»", "«ve anladı»", tags=[AT, MX, "naqis-verbs"], wa=True, hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ؛ رَأَى هُنَا عِلْمِيَّةٌ تَنْصِبُ مَفْعُولَيْنِ سَدَّ مَسَدَّهُمَا الْمَصْدَرُ الْمُؤَوَّلُ"),
  tok("أَنَّهُمْ", "anna", "part", [IW, MX], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ اسْمُهَا.", "«that they»", "«… -diklerini»", segments=[seg("أَنَّ", "anna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«[indeed]»", "«[gerçekten]»"),
  mazi_pl("جَحَدُوا", "jahada", "«had denied»", "«inkâr ettiler»", tags=[IW]),
  bi_ma(),
  mazi("جَاءَ", "jaa", "«he had brought»", "«getirdiği»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with»", "«ile»", punct="،"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  majrur("آيَاتٍ", "aya", "«signs»", "«âyetler»", tags=[JM]),
  naat("بَيِّنَاتٍ", "bayyina", "«clear»", "«apaçık»", tags=[JM]),
  atf("وَمُعْجِزَاتٍ", "mujiza", "«miracles»", "«ve mucizeler»", tags=[JM]),
  naat("بَاهِرَاتٍ", "bahir", "«dazzling»", "«göz kamaştırıcı»", tags=[JM, "ism-fail"]),
  ta_pron("اسْتَيْقَنَتْهَا", "istayqana", "اسْتَيْقَنَتْ", "هَا", "pron-3fs", "«their souls were certain of»", "«nefislerinin kesinlikle bildiği»", tags=["jumla-sifa", "form-x-verbs"], extra=" — وَالْجُمْلَةُ نَعْتٌ"),
  noun_pron("أَنْفُسُهُمْ", "nafs", "أَنْفُسُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their souls» — the doer.", "«nefisleri» — fâil.", tags=[FL, ID, JT], punct="،"),
  v_pl_pron("وَاسْتَصْغَرُوهُ", "istasghara", "اسْتَصْغَرُو", "هُ", "pron-3ms", "«and belittled him»", "«ve onu küçümsediler»", tags=[IW, "form-x-verbs"], wa=True),
  li_anna("لِأَنَّهُ", "هُ", "pron-3ms", "«because he»", "«çünkü o»"),
  tok("لَمْ", "lam", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-madı»"),
  tok("يَكُنْ", "kana", "verb", [LJ, KN, IW, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«was» — kāna in jazm; the hollow wāw dropped.", "«idi» — meczûm kâne; ecvef vâv düştü."),
  tok("صَاحِبَ", "sahib", "noun", [KN, ID], "خَبَرُ يَكُنْ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«a man [of]» — kāna's khabar.", "«sahibi» — kâne'nin haberi."),
  mudaf_ilayh("حَوْلٍ", "hawl", "«power»", "«güç»"),
  atf("وَطَوْلٍ", "tawl", "«means»", "«ve servet»", punct="،"),
  mazi("أَقْبَلَ", "aqbala", "«he turned»", "«yöneldi»", tags=["form-iv-verbs"], hidden="هُوَ", extra_ar=" — جَوَابُ لَمَّا"),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  majrur("عَامَّةِ", "amma-public", "«the common [people]»", "«halka»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("النَّاسِ", "nas", "«people»", "«insanların»"),
  pron_atf("وَفُقَرَائِهِمْ", "faqir", "فُقَرَائِ", "هِمْ", "pron-3mp", "«the poor among them»", "«ve onların fakirlerine»", tags=[JT], punct="،"),
])
sen("s6", "whose hearts had softened and whose souls had grown pure, because they ate by the toil of their right hands and the sweat of their brows, boasting of no lineage and lording it over no one by rank or office;",
        "ki kalpleri yumuşamış, nefisleri arınmıştı; çünkü sağ ellerinin emeğiyle ve alınlarının teriyle yiyorlar, soyla övünmüyor, makam ve mevki ile büyüklenmiyorlardı;", [
  tok("وَقَدْ", "qad", "part", [HL, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]» — a ḥāl clause.", "«ve [gerçekten]» — hâl cümlesi.", segments=wa_("قَدْ", "qad", "part")),
  mazi_ta("لَانَتْ", "lana", "«had softened»", "«yumuşamıştı»", tags=[HL, "hollow-verbs"]),
  noun_pron("قُلُوبُهُمْ", "qalb", "قُلُوبُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their hearts» — the doer.", "«kalpleri» — fâil.", tags=[FL, ID, JT], punct="،"),
  tok("وَصَفَتْ", "safa-clear", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَصَفَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and had grown pure» — a defective māḍī (صَفَا): the alif drops before the feminine tāʾ.", "«ve arınmıştı» — nâkıs mâzî (صَفَا): elif te'nis tâ'sı önünde düştü.", segments=wa_("صَفَتْ", "safa-clear", "verb")),
  noun_pron("نُفُوسُهُمْ", "nafs", "نُفُوسُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their souls» — the doer.", "«nefisleri» — fâil.", tags=[FL, ID, JT], punct="،"),
  li_anna("لِأَنَّهُمْ", "هُمْ", "pron-3mp", "«because they»", "«çünkü onlar»"),
  khamsa("يَأْكُلُونَ", "akala", "«eat»", "«yiyorlar»", tags=[IW], extra_ar=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  bi_noun("بِكَدِّ", "kadd", "«by the toil [of]»", "«emeğiyle»", tags=[ID], extra="، مُضَافٌ"),
  noun_pron("يَمِينِهِمْ", "yamin", "يَمِينِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their right hands»", "«sağ ellerinin»", tags=[ID]),
  atf("وَعَرَقِ", "araq", "«the sweat [of]»", "«ve teriyle»", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  noun_pron("جَبِينِهِمْ", "jabin", "جَبِينِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their brows»", "«alınlarının»", tags=[ID], punct="،"),
  la_nafiya(),
  khamsa("يَتَفَاخَرُونَ", "tafakhara", "«they boast»", "«övünürler»", tags=[HL, "la-nafiya", "form-vi-verbs"], extra_ar=" — بَعْدَ لَا النَّافِيَةِ؛ وَالْجُمْلَةُ حَالٌ"),
  bi_noun("بِنَسَبٍ", "nasab", "«of lineage»", "«soyla»", punct="،"),
  la_nafiya("وَلَا", wa=True),
  khamsa("يَتَطَاوَلُونَ", "tatawala", "«they lord it»", "«büyüklenirler»", tags=["la-nafiya", "form-vi-verbs"]),
  bi_noun("بِجَاهٍ", "jah", "«by rank»", "«makamla»"),
  atf("وَمَنْصِبٍ", "mansib", "«office»", "«ve mevki»", punct="،"),
])
sen("s7", "so a group of them believed: among them the fullers, among them the fishermen, and among them the people of crafts and trades.",
        "böylece onlardan bir topluluk inandı: içlerinde çamaşırcılar, içlerinde balıkçılar, içlerinde zanaat ve meslek erbabı vardı.", [
  tok("فَآمَنَتْ", "aamana", "verb", [AT, "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَآمَنَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«so believed» — the fāʾ of consequence.", "«böylece inandı» — sebep fâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("آمَنَتْ", "aamana", "verb")]),
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«of them»", "«onlardan»"),
  fail("طَائِفَةٌ", "taifa", "«a group»", "«bir topluluk»", punct="،"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«among them» — a fronted khabar; the clause describes «a group».", "«içlerinde» — öne alınmış haber; cümle «topluluk»u vasfeder.", tags=[MK, "jumla-sifa"], extra_ar=" — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِفَةٌ لِطَائِفَةٌ"),
  tok("الْقَصَّارُونَ", "qassar", "noun", [MK, JS, "sighat-mubalagha"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — فَعَّال لِلْحِرْفَةِ.", "«the fullers» — the delayed mubtadaʾ; faʿʿāl of trade.", "«çamaşırcılar» — sonraya kalan mübtedâ; meslek bildiren fa''âl.", punct="،"),
  wa_fiha(),
  tok("صَيَّادُو", "sayyad", "noun", [MK, JS, ID, "sighat-mubalagha"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْوَاوِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«the catchers [of]» — the nūn dropped for the annexation.", "«avcıları» — nûnu izâfet için düşmüş."),
  mudaf_ilayh("الْأَسْمَاكِ", "samak", "«fish»", "«balık»", tags=[JT], punct="،"),
  wa_fiha(),
  tok("أَهْلُ", "ahl", "noun", [MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the people [of]»", "«erbabı»"),
  mudaf_ilayh("الْحِرَفِ", "hirfa", "«crafts»", "«zanaat»", tags=[JT]),
  atf("وَالْمِهَنِ", "mihna", "«trades»", "«ve meslek»", tags=[JT], punct="."),
])
# ---------------------------------------------------------------- §16 نَحْنُ أَنْصَارُ اللهِ (print p. 51)
sen("s8", "So they believed in the Messiah, gathered round him, put their hands in his hand and said: «We are the helpers of God». God Most High says:",
        "Mesîh'e inandılar, etrafında toplandılar, ellerini onun eline koydular ve dediler: «Biz Allah'ın yardımcılarıyız». Allah Teâlâ buyurur:", [
  tok("فَآمَنُوا", "aamana", "verb", [AT, "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَآمَنُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they believed»", "«böylece inandılar»", segments=[seg("فَ", "fa", "conj"), seg("آمَنُوا", "aamana", "verb")]),
  bi_noun("بِالْمَسِيحِ", "masih", "«in the Messiah»", "«Mesîh'e»", punct="،"),
  mazi_pl("وَالْتَفُّوا", "iltaffa", "«and gathered»", "«ve toplandılar»", tags=[AT, "doubled-verbs", "form-viii-verbs"], wa=True),
  noun_pron("حَوْلَهُ", "hawla", "حَوْلَ", "هُ", "pron-3ms", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«round him»", "«etrafında»", tags=[MF, ID], punct="،"),
  mazi_pl("وَوَضَعُوا", "wadaa", "«and put»", "«ve koydular»", tags=[AT, "mithal-verbs"], wa=True),
  noun_pron("أَيْدِيَهُمْ", "yad", "أَيْدِيَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — أَيْدٍ جَمْعُ يَدٍ، مَنْقُوصٌ.", "«their hands» — the object; a manqūṣ plural shows its fatḥa.", "«ellerini» — mef'ûl; mankûs cemi fethasını gösterir.", tags=[MB, ID, JT, "ism-maqsur-manqus"]),
  fi(),
  noun_pron("يَدِهِ", "yad", "يَدِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his hand»", "«onun eline»", tags=[HJ, ID], punct="،"),
  mazi_pl("وَقَالُوا", "qala", "«and said»", "«ve dediler»", tags=[AT, "hollow-verbs"], wa=True, punct=":"),
  tok("نَحْنُ", "nahnu", "pron", [MK, IQ], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — مَقُولُ الْقَوْلِ، وَهُوَ اقْتِبَاسٌ مِنَ الْآيَةِ (3:52).", "«we» — the mubtadaʾ; the saying quotes the āya (3:52).", "«biz» — mübtedâ; söz âyetten iktibastır (3:52)."),
  tok("أَنْصَارُ", "nasir", "noun", [MK, ID, JT], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the helpers [of]» — the khabar.", "«yardımcıları» — haber."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct="،"),
  mudari("يَقُولُ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs"], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
])
sen("s9", "«Then when ʿĪsā sensed unbelief from them, he said: Who are my helpers toward God? The disciples said: We are the helpers of God; we believe in God, and bear witness that we are Muslims.» (3:52)",
        "«Îsâ onlardan küfrü sezince dedi: Allah yolunda yardımcılarım kimler? Havârîler dediler: Biz Allah'ın yardımcılarıyız; Allah'a inandık, şahit ol ki biz müslümanlarız.» (3:52)", [
  *quran([
  tok("فَلَمَّا", "lamma", "part", [AT, MF], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«then when»", "«… -ınca»", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi("أَحَسَّ", "ahassa", "«sensed»", "«sezdi»", tags=[ID, "doubled-verbs", "form-iv-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا"),
  tok("عِيسَى", "isa", "propn", [FL, MM, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — the doer.", "«Îsâ» — fâil."),
  prep_pron("مِنْهُمُ", "min", "هُمُ", "pron-3mp", "«from them»", "«onlardan»", extra_ar=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  maful_("الْكُفْرَ", "kufr", "«unbelief»", "«küfrü»"),
  mazi("قَالَ", "qala", "«he said»", "«dedi»", tags=["hollow-verbs"], hidden="هُوَ", extra_ar=" — جَوَابُ لَمَّا"),
  tok("مَنْ", "man-istifham", "pron", [IS, MK], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the mubtadaʾ.", "«kimler» — mübtedâ."),
  tok("أَنْصَارِي", "nasir", "noun", [MK, ID, JT, "ya-al-mutakallim"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my helpers» — the khabar.", "«yardımcılarım» — haber.", segments=[seg("أَنْصَارِ", "nasir", "noun"), seg("ي", "pron-1s", "pron")]),
  prep("إِلَى", "ila", "«toward»", "«-e»", ar="حَرْفُ جَرٍّ بِمَعْنَى مَعَ، أَوْ عَلَى تَضْمِينِ أَنْصَارِي مَعْنَى الذَّاهِبِينَ."),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God»", "«Allah»"),
  mazi("قَالَ", "qala", "«said»", "«dediler»", tags=["hollow-verbs"], hidden=None),
  tok("الْحَوَارِيُّونَ", "hawari", "noun", [FL, JS], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the disciples» — the doer.", "«havârîler» — fâil."),
  tok("نَحْنُ", "nahnu", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«we»", "«biz»"),
  tok("أَنْصَارُ", "nasir", "noun", [MK, ID, JT], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the helpers [of]»", "«yardımcıları»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  amanna(),
  tok("بِاللهِ", "allah", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«in God»", "«Allah'a»", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  tok("وَاشْهَدْ", "shahida", "verb", [AT, AM], "الْوَاوُ عَاطِفَةٌ، وَاشْهَدْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and bear witness»", "«ve şahit ol»", segments=wa_("اشْهَدْ", "shahida", "verb")),
  tok("بِأَنَّا", "anna", "part", [HJ, IW], "الْبَاءُ حَرْفُ جَرٍّ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا — أَصْلُهُ بِأَنَّنَا.", "«that we»", "«… olduğumuza»", segments=[seg("بِ", "bi", "prep"), seg("أَنَّ", "anna", "part"), seg("ا", "pron-1p", "pron")]),
  tok("مُسْلِمُونَ", "muslim", "noun", [IW, JS, "ism-fail", "form-iv-verbs"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«Muslims» — anna's khabar.", "«müslümanlar» — enne'nin haberi.", punct=AYA),
  ]),
])
sen("s10", "«Our Lord, we believe in what You have sent down and we follow the Messenger, so write us among the witnesses.» (3:53)",
        "«Rabbimiz! İndirdiğine inandık ve Resul'e uyduk; bizi şahitlerle birlikte yaz.» (3:53)", [
  *quran([
  tok("رَبَّنَا", "rabb", "noun", ["vocative-munada", ID, "hadhf-wa-taqdir"], "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Lord»", "«Rabbimiz»", segments=[seg("رَبَّ", "rabb", "noun"), seg("نَا", "pron-1p", "pron")]),
  amanna(),
  bi_ma(),
  tok("أَنْزَلْتَ", "anzala", "verb", [MW, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — صِلَةٌ، وَالْعَائِدُ مَحْذُوفٌ.", "«You have sent down»", "«indirdin»", segments=[seg("أَنْزَلْ", "anzala", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("وَاتَّبَعْنَا", "ittabaa", "verb", [AT, "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاتَّبَعْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«and we follow»", "«ve uyduk»", segments=[seg("وَ", "wa", "conj"), seg("اتَّبَعْ", "ittabaa", "verb"), seg("نَا", "pron-1p", "pron")]),
  maful_("الرَّسُولَ", "rasul", "«the Messenger»", "«Resul'e»"),
  tok("فَاكْتُبْنَا", "kataba", "verb", [AT, AM, MB], "الْفَاءُ عَاطِفَةٌ، وَاكْتُبْ فِعْلُ أَمْرٍ (دُعَاءٌ) مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَنَا مَفْعُولٌ بِهِ.", "«so write us»", "«bizi yaz»", segments=[seg("فَ", "fa", "conj"), seg("اكْتُبْ", "kataba", "verb"), seg("نَا", "pron-1p", "pron")]),
  zarf("مَعَ", "maa", "«among, with»", "«ile birlikte»"),
  tok("الشَّاهِدِينَ", "shahid", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the witnesses»", "«şahitler»", punct=AYA),
  ]),
])

CAND = {
 "waqaa": G("waqaa", "وَقَعَ", "و ق ع", "verb", "to befall, to happen; to fall (an assimilated verb)", "vuku bulmak, başına gelmek; düşmek (misâl fiil)", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "-den önce", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "ibtaada": G("ibtaada", "اِبْتَعَدَ", "ب ع د", "verb", "to draw away (ʿan: from) (Form VIII)", "uzaklaşmak (iftiâl)", 2),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "rais": G("rais", "رَئِيس", "ر أ س", "noun", "a chief, a head", "reis, başkan", 1, plural="رُؤَسَاء"),
 "zaim": G("zaim", "زَعِيم", "ز ع م", "noun", "a leader", "önder, lider", 2, plural="زُعَمَاء"),
 "hajara": G("hajara", "هَجَرَ", "ه ج ر", "verb", "to desert, to abandon", "terk etmek", 1),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1, plural="أَقْوِيَاء"),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see; to deem", "görmek; saymak", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith, belief", "iman", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "ittiba": G("ittiba", "اتِّبَاع", "ت ب ع", "noun", "following (the maṣdar of Form VIII)", "uyma, tâbi olma (iftiâl masdarı)", 1),
 "ghadada": G("ghadada", "غَضَاضَة", "غ ض ض", "noun", "a loss of face, a diminishment", "küçülme, eksiklik", 3),
 "ayb": G("ayb", "عَيْب", "ع ي ب", "noun", "a fault, a disgrace", "ayıp, kusur", 1, plural="عُيُوب"),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to split; (ʿalā) to weigh heavily on (doubled)", "yarmak; (alâ ile) ağır gelmek (muzâaf)", 2),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "tanazul": G("tanazul", "تَنَازُل", "ن ز ل", "noun", "stepping down, relinquishing (ʿan: of) (the maṣdar of Form VI)", "vazgeçme, feragat (tefâul masdarı)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "riasa": G("riasa", "رِئَاسَة", "ر أ س", "noun", "leadership, presidency", "reislik, başkanlık", 2),
 "zaama": G("zaama", "زَعَامَة", "ز ع م", "noun", "chieftaincy, leadership", "önderlik", 3),
 "imtiyaz": G("imtiyaz", "اِمْتِيَاز", "م ي ز", "noun", "privilege, distinction (the maṣdar of Form VIII)", "imtiyaz, ayrıcalık (iftiâl masdarı)", 2),
 "siyada": G("siyada", "سِيَادَة", "س و د", "noun", "lordship, sovereignty", "efendilik, hâkimiyet", 2),
 "sadaqa-be-true": G("sadaqa-be-true", "صَدَقَ", "ص د ق", "verb", "to speak the truth; to prove true", "doğru söylemek; doğru çıkmak", 1),
 "qawl": G("qawl", "قَوْل", "ق و ل", "noun", "a saying, speech", "söz", 1, plural="أَقْوَال"),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā)", "değil, yok (nefiy mâ'sı)", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send (Form IV)", "göndermek (if'âl)", 1),
 "qarya": G("qarya", "قَرْيَة", "ق ر ي", "noun", "a town, a village", "belde, köy", 1, plural="قُرًى"),
 "nadhir": G("nadhir", "نَذِير", "ن ذ ر", "noun", "a warner", "uyarıcı, nezîr", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "mutraf": G("mutraf", "مُتْرَف", "ت ر ف", "noun", "one living in luxury (a passive participle of Form IV)", "refah içinde şımaran (if'âl ism-i mef'ûlü)", 3),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (pl.)", "siz / sizi / sizin", 1),
 "kafir": G("kafir", "كَافِر", "ك ف ر", "noun", "an unbeliever (an active participle)", "kâfir (ism-i fâil)", 1, plural="كَافِرُونَ"),
 "nahnu": G("nahnu", "نَحْنُ", None, "pron", "we", "biz", 1),
 "akthar": G("akthar", "أَكْثَر", "ك ث ر", "noun", "more, most (an elative)", "daha çok (ism-i tafdîl)", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "money, wealth", "mal", 1, plural="أَمْوَال"),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child, a son", "çocuk, oğul", 1, plural="أَوْلَاد"),
 "muadhdhab": G("muadhdhab", "مُعَذَّب", "ع ذ ب", "noun", "punished (a passive participle of Form II)", "azaba uğratılan (tef'îl ism-i mef'ûlü)", 2),
 "lamma": G("lamma", "لَمَّا", None, "part", "when (of the past); not yet", "-ınca, -dığı zaman; henüz … -medi", 1),
 "yaisa": G("yaisa", "يَئِسَ", "ي أ س", "verb", "to despair (min: of) (a hamza-middle verb)", "ümidini kesmek (mehmûzü'l-ayn)", 2),
 "shahada-verb": G("shahada-verb", "شَاهَدَ", "ش ه د", "verb", "to witness, to see (Form III)", "görmek, müşâhede etmek (müfâale)", 1),
 "inad": G("inad", "عِنَاد", "ع ن د", "noun", "obstinacy", "inat", 2),
 "kufr": G("kufr", "كُفْر", "ك ف ر", "noun", "unbelief", "küfür", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "jahada": G("jahada", "جَحَدَ", "ج ح د", "verb", "to deny (bi: something known)", "inkâr etmek, bile bile reddetmek", 2),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "bayyina": G("bayyina", "بَيِّنَة", "ب ي ن", "noun", "clear, evident; a clear proof", "apaçık; beyyine, kesin delil", 1, plural="بَيِّنَات"),
 "mujiza": G("mujiza", "مُعْجِزَة", "ع ج ز", "noun", "a miracle", "mucize", 1, plural="مُعْجِزَات"),
 "bahir": G("bahir", "بَاهِر", "ب ه ر", "noun", "dazzling, brilliant (an active participle)", "göz kamaştırıcı, parlak (ism-i fâil)", 2),
 "istayqana": G("istayqana", "اِسْتَيْقَنَ", "ي ق ن", "verb", "to be certain of (Form X)", "kesinlikle bilmek, yakînen inanmak (istif'âl)", 2),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "a soul, a self", "nefis, can", 1, plural="نُفُوس"),
 "istasghara": G("istasghara", "اِسْتَصْغَرَ", "ص غ ر", "verb", "to belittle, to deem small (Form X)", "küçümsemek (istif'âl)", 2),
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "sahib": G("sahib", "صَاحِب", "ص ح ب", "noun", "a companion; the owner, a man of", "sahip; arkadaş", 1, plural="أَصْحَاب"),
 "hawl": G("hawl", "حَوْل", "ح و ل", "noun", "power, might", "güç, kuvvet", 2),
 "tawl": G("tawl", "طَوْل", "ط و ل", "noun", "means, wealth, ability", "servet, imkân", 3),
 "aqbala": G("aqbala", "أَقْبَلَ", "ق ب ل", "verb", "to turn toward, to come forward (Form IV)", "yönelmek (if'âl)", 1),
 "amma-public": G("amma-public", "عَامَّة", "ع م م", "noun", "the common people, the generality", "halk, avam; genel", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "faqir": G("faqir", "فَقِير", "ف ق ر", "noun", "poor", "fakir", 1, plural="فُقَرَاء"),
 "lana": G("lana", "لَانَ", "ل ي ن", "verb", "to be soft (hollow)", "yumuşamak (ecvef)", 2),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "a heart", "kalp", 1, plural="قُلُوب"),
 "safa-clear": G("safa-clear", "صَفَا", "ص ف و", "verb", "to be clear, pure (defective)", "arınmak, saf olmak (nâkıs)", 2),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "kadd": G("kadd", "كَدّ", "ك د د", "noun", "toil, labour", "emek, çaba", 2),
 "yamin": G("yamin", "يَمِين", "ي م ن", "noun", "the right hand; an oath", "sağ el; yemin", 1),
 "araq": G("araq", "عَرَق", "ع ر ق", "noun", "sweat", "ter", 2),
 "jabin": G("jabin", "جَبِين", "ج ب ن", "noun", "the brow, the forehead", "alın", 2),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "tafakhara": G("tafakhara", "تَفَاخَرَ", "ف خ ر", "verb", "to boast (bi: of) (Form VI)", "övünmek (tefâul)", 2),
 "nasab": G("nasab", "نَسَب", "ن س ب", "noun", "lineage", "soy, nesep", 1),
 "tatawala": G("tatawala", "تَطَاوَلَ", "ط و ل", "verb", "to lord it over (bi: by) (Form VI, hollow)", "büyüklenmek (tefâul, ecvef)", 3),
 "jah": G("jah", "جَاه", "ج و ه", "noun", "rank, standing", "makam, itibar", 2),
 "mansib": G("mansib", "مَنْصِب", "ن ص ب", "noun", "an office, a post", "mevki, makam", 2, plural="مَنَاصِب"),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "taifa": G("taifa", "طَائِفَة", "ط و ف", "noun", "a group, a party", "topluluk, tâife", 1, plural="طَوَائِف"),
 "qassar": G("qassar", "قَصَّار", "ق ص ر", "noun", "a fuller, a bleacher of cloth (faʿʿāl of trade)", "çamaşırcı, kassâr (meslek fa''âl'ı)", 3),
 "sayyad": G("sayyad", "صَيَّاد", "ص ي د", "noun", "a hunter, a fisherman (faʿʿāl of trade)", "avcı, balıkçı (meslek fa''âl'ı)", 2),
 "samak": G("samak", "سَمَك", "س م ك", "noun", "fish", "balık", 1, plural="أَسْمَاك"),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "people, family; the people of", "ehil, aile; … ehli", 1),
 "hirfa": G("hirfa", "حِرْفَة", "ح ر ف", "noun", "a craft", "zanaat", 2, plural="حِرَف"),
 "mihna": G("mihna", "مِهْنَة", "م ه ن", "noun", "a trade, a profession", "meslek", 2, plural="مِهَن"),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "iltaffa": G("iltaffa", "اِلْتَفَّ", "ل ف ف", "verb", "to gather round (ḥawla) (Form VIII, doubled)", "etrafında toplanmak (iftiâl, muzâaf)", 3),
 "hawla": G("hawla", "حَوْلَ", "ح و ل", "noun", "around", "etrafında", 1),
 "wadaa": G("wadaa", "وَضَعَ", "و ض ع", "verb", "to put, to place (an assimilated verb)", "koymak (misâl fiil)", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1, plural="أَيْدٍ"),
 "nasir": G("nasir", "نَصِير", "ن ص ر", "noun", "a helper, a supporter", "yardımcı, nasîr", 1, plural="أَنْصَار"),
 "ahassa": G("ahassa", "أَحَسَّ", "ح س س", "verb", "to sense, to perceive (Form IV, doubled)", "sezmek, hissetmek (if'âl, muzâaf)", 2),
 "man-istifham": G("man-istifham", "مَنْ (الِاسْتِفْهَامِيَّة)", None, "pron", "who? (interrogative)", "kim? (istifhâm)", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "hawari": G("hawari", "حَوَارِيّ", "ح و ر", "noun", "a disciple (of ʿĪsā)", "havârî", 2, plural="حَوَارِيُّونَ"),
 "shahida": G("shahida", "شَهِدَ", "ش ه د", "verb", "to witness, to testify", "şahit olmak, şahitlik etmek", 1),
 "muslim": G("muslim", "مُسْلِم", "س ل م", "noun", "a Muslim, one who submits (an active participle of Form IV)", "müslüman (if'âl ism-i fâili)", 1, plural="مُسْلِمُونَ"),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "anzala": G("anzala", "أَنْزَلَ", "ن ز ل", "verb", "to send down (Form IV)", "indirmek (if'âl)", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "ittabaa": G("ittabaa", "اِتَّبَعَ", "ت ب ع", "verb", "to follow (Form VIII)", "uymak, tâbi olmak (iftiâl)", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resul", 1, plural="رُسُل"),
 "kataba": G("kataba", "كَتَبَ", "ك ت ب", "verb", "to write", "yazmak", 1),
 "maa": G("maa", "مَعَ", None, "noun", "with", "ile, birlikte", 1),
 "shahid": G("shahid", "شَاهِد", "ش ه د", "noun", "a witness (an active participle)", "şahit (ism-i fâil)", 1, plural="شُهُود"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ibtaada", _sg.derived(_sg.B8, _sg.W8, "َ", "اِبْتَعَد", "بْتَعِد", "اِبْتَعِد", "اِبْتِعَاد", "مُبْتَعِد", None, None, None, "اِبْتَعَدَ عَنْهُ: تَنَحَّى وَصَارَ بَعِيدًا مِنْهُ."))
put_morph(mo, "sadaqa-be-true", _sg.sound1("nasara", "صَدَق", "صْدُق", "اُصْدُق", "صِدْق", "صَادِق", "مَصْدُوق", "صُدِقَ", "يُصْدَقُ", "صَدَقَ يَصْدُقُ: قَالَ الْحَقَّ؛ وَصَدَقَ قَوْلُهُ: تَحَقَّقَ."))
put_morph(mo, "yaisa", _sg.sound1("samia", "يَئِس", "يْأَس", "اِيأَس", "يَأْس", "يَائِس", None, None, None, "يَئِسَ مِنَ الشَّيْءِ يَيْأَسُ: قَطَعَ رَجَاءَهُ مِنْهُ — مَهْمُوزُ الْعَيْنِ مِثَالٌ يَائِيٌّ.", cls="مَهْمُوزُ الْعَيْنِ"))
put_morph(mo, "jahada", _sg.sound1("fataha", "جَحَد", "جْحَد", "اِجْحَد", "جُحُود / جَحْد", "جَاحِد", "مَجْحُود", "جُحِدَ", "يُجْحَدُ", "جَحَدَ الشَّيْءَ يَجْحَدُهُ: أَنْكَرَهُ مَعَ عِلْمِهِ بِهِ."))
put_morph(mo, "istayqana", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَيْقَن", "سْتَيْقِن", "اِسْتَيْقِن", "اِسْتِيقَان", "مُسْتَيْقِن", "مُسْتَيْقَن", "اُسْتُيْقِنَ", "يُسْتَيْقَنُ", "اِسْتَيْقَنَ الشَّيْءَ: عَلِمَهُ عِلْمًا لَا شَكَّ فِيهِ."))
put_morph(mo, "istasghara", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَصْغَر", "سْتَصْغِر", "اِسْتَصْغِر", "اِسْتِصْغَار", "مُسْتَصْغِر", "مُسْتَصْغَر", "اُسْتُصْغِرَ", "يُسْتَصْغَرُ", "اِسْتَصْغَرَهُ: عَدَّهُ صَغِيرًا وَاحْتَقَرَهُ."))
put_morph(mo, "safa-clear", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "صَفَ", "صْف", "u", "اُصْف", "صَفَاء / صَفْو", "صَافٍ (الصَّافِي)", None, None, None, "صَفَا الشَّيْءُ يَصْفُو: خَلَصَ مِنَ الْكَدَرِ — نَاقِصٌ وَاوِيٌّ؛ لَمْ يَصْفُ."))
put_morph(mo, "tafakhara", _sg.derived(_sg.B6, _sg.W6, "َ", "تَفَاخَر", "تَفَاخَر", "تَفَاخَر", "تَفَاخُر", "مُتَفَاخِر", None, None, None, "تَفَاخَرَ بِالشَّيْءِ: بَاهَى بِهِ وَافْتَخَرَ."))
put_morph(mo, "tatawala", _sg.derived(_sg.B6, _sg.W6, "َ", "تَطَاوَل", "تَطَاوَل", "تَطَاوَل", "تَطَاوُل", "مُتَطَاوِل", None, None, None, "تَطَاوَلَ عَلَيْهِ: تَكَبَّرَ وَاعْتَدَى — تَفَاعُلٌ مِنَ الْأَجْوَفِ، صَحَّتْ وَاوُهُ."))
put_morph(mo, "iltaffa", _sg.entry(_sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِلْتِفَاف", "مُلْتَفّ", _sg.mazi14("اِلْتَفّ", "اِلْتَفَف"), _sg.mudari14("َ", "لْتَفّ", "لْتَفِف"), ["اِلْتَفَّ", "اِلْتَفَّا", "اِلْتَفُّوا", "اِلْتَفِّي", "اِلْتَفَّا", "اِلْتَفِفْنَ"], "يَلْتَفَّ", "يَلْتَفَّ", "تَلْتَفَّ", None, None, None, "اِلْتَفَّ الْقَوْمُ حَوْلَهُ: اجْتَمَعُوا وَأَحَاطُوا بِهِ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَلْتَفَّ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch35 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 35 (print pp. 49–51; ʿĪsā §14–16): an old struggle — the chiefs and the rich turn away, the step down from leadership too heavy (s1–s2), Sabaʾ 34:34–35 the affluent deny every warner (s3–s4); the common people and the poor believe — softened hearts, the toil of their hands, the fullers, the fishermen, the craftsmen (s5–s7); «we are the helpers of God», with 3:52–53 (s8–s10)."
ADD_TR = " Otuz beşinci bölüm (baskı s. 49–51; Îsâ §14–16): eski bir çatışma — reisler ve zenginler yüz çevirir, reislikten vazgeçmek ağır gelir (s1–s2), Sebe' 34–35 şımaranlar her uyarıcıyı inkâr eder (s3–s4); halk ve fakirler inanır — yumuşamış kalpler, el emeği, çamaşırcılar, balıkçılar, zanaatkârlar (s5–s7); «biz Allah'ın yardımcılarıyız», 3:52–53 ile (s8–s10)."
write_out(35, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §14–16", GLOSS_ADD, notes=(), related=())
report(35, S, GLOSS_ADD, ())
