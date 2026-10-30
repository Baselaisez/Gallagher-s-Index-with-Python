# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 40: «قِصَّةُ عِيسَى» §30 (a divine arrangement: the policeman orders a hot-headed Israelite youth to carry the beam), §31 («but it was made to appear so to them»: the gallows police seize the youth carrying the cross; he cries his innocence in a tongue they do not know), §32 (the sentence carried out; the Jews watch from afar in the dark, sure the crucified is the Messiah); print pp. 58–60.
python3 tools/authoring/author_qisas4_ch40.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: تَدْبِيرٌ إِلٰهِيٌّ — وَلٰكِنْ شُبِّهَ لَهُمْ", "en": "The story of ʿĪsā: a divine arrangement — «but it was made to appear so to them»", "tr": "Îsâ'nın kıssası: ilâhî bir tedbir — «fakat onlara öyle gösterildi»"}
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

# ---------------------------------------------------------------- §30 تَدْبِيرٌ إِلٰهِيٌّ (print pp. 58–59)
sen("s1", "And here the policeman in charge of him ordered an Israelite youth to carry the beam — one who was the most zealous of his fellows, the greatest of them in folly, the keenest of them to hurt the Lord Messiah and to be first at him, so that the matter might end quickly and he be rid of this exhausting responsibility.",
        "Burada ona memur edilen polis, İsrâilli bir gence tahtayı taşımasını emretti; bu genç arkadaşlarının en coşkulusu, en sefihi, Efendi Mesîh'e eziyette ve ona önce davranmakta en hırslısıydı; tâ ki iş çabuk bitsin ve bu yorucu sorumluluktan kurtulsun.", [
  tok("وَهُنَا", "huna", "pron", [AT, MF], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُنَا اسْمُ إِشَارَةٍ لِلْمَكَانِ (وَالْمَوْقِفِ) فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and here» — the demonstrative of place as a ẓarf.", "«ve burada» — mekân işaret ismi, zarf.", segments=wa_("هُنَا", "huna", "pron")),
  mazi("أَمَرَ", "amara-order", "«ordered»", "«emretti»", hidden=None),
  fail("الشُّرْطِيُّ", "shurti", "«the policeman»", "«polis»", tags=["ism-mansub"]),
  naat("الْمُوَكَّلُ", "muwakkal", "«in charge»", "«memur edilen»", case="raf", tags=["ism-maful", "form-ii-verbs"]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«of him»", "«ona»", punct="،"),
  maful_("شَابًّا", "shabb", "«a youth»", "«bir gence»", tags=["doubled-verbs"]),
  naat("إِسْرَائِيلِيًّا", "israili", "«Israelite»", "«İsrâilli»", case="nasb", tags=["ism-mansub"]),
  bi_noun("بِحَمْلِ", "haml", "«to carry»", "«taşımasını»", tags=[ID], extra="، مُضَافٌ"),
  mudaf_ilayh("الْعُودِ", "ud", "«the beam»", "«tahtayı»", punct="،"),
  wa_kana("، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الشَّابُّ)"),
  tafdil_hum("أَشَدَّ", "ashadd", "أَشَدَّ", "«the most intense [of]»", "«en çok … olanı»", wa=False, first=True) if False else tok("أَشَدَّ", "ashadd", "noun", [KN, ID, "ism-tafdil", "doubled-verbs"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ مِنَ الْمُضَاعَفِ.", "«the most intense [of]» — kāna's khabar; an elative of a doubled root.", "«en … olanı» — kâne'nin haberi; muzâaf kökten ism-i tafdîl."),
  noun_pron("زُمَلَائِهِ", "zamil", "زُمَلَائِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his fellows»", "«arkadaşlarının»", tags=[ID, JT]),
  tamyiz("حَمَاسَةً", "hamasa", "«in zeal»", "«coşkuca»", punct="،"),
  tafdil_hum("وَأَكْبَرَهُمْ", "akbar", "أَكْبَرَ", "«the greatest of them»", "«onların en büyüğü»"),
  tamyiz("سَفَاهَةً", "sifaha", "«in folly»", "«sefihlikçe»", punct="،"),
  tafdil_hum("وَأَحْرَصَهُمْ", "ahras", "أَحْرَصَ", "«the keenest of them»", "«onların en hırslısı»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("إِيذَاءِ", "idha-harm", "«hurting»", "«eziyet etmekte»", tags=[ID, "form-iv-verbs"], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("السَّيِّدِ", "sayyid", "«the Lord»", "«Efendi»"),
  tok("الْمَسِيحِ", "masih", "propn", [BD], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ.", "«Messiah»", "«Mesîh'e»", punct="،"),
  atf("وَمُبَادَرَةً", "mubadara", "«in being first»", "«ve önce davranmakta»", "nasb", tags=["tamyiz", "form-iii-verbs"], sign="بِالْفَتْحَةِ — تَمْيِيزٌ مَعْطُوفٌ عَلَى مَحَلِّ عَلَى إِيذَاءِ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«at him»", "«ona»", punct="،"),
  tok("حَتَّى", "hatta", "part", [TA], "حَرْفُ غَايَةٍ وَتَعْلِيلٍ يَنْصِبُ الْمُضَارِعَ بِأَنْ مُضْمَرَةٍ بَعْدَهُ.", "«so that» — ḥattā of purpose, governing naṣb through a concealed an.", "«tâ ki» — gizli en ile nasb eden gâye hattâ'sı."),
  tok("يَنْتَهِيَ", "intaha", "verb", [AN, "naqis-verbs", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ.", "«end» — naṣb after ḥattā; the fatḥa shows on the yāʾ.", "«bitsin» — hattâ'dan sonra mansub; fetha yâ üzerinde görünür."),
  fail("الْأَمْرُ", "amr", "«the matter»", "«iş»"),
  hal("سَرِيعًا", "sari", "«quickly»", "«çabuk»", punct="،"),
  tok("وَيَتَخَلَّصَ", "takhallasa", "verb", [AT, AN, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَتَخَلَّصَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and be rid»", "«ve kurtulsun»", segments=wa_("يَتَخَلَّصَ", "takhallasa", "verb")),
  prep("مِنْ", "min", "«of»", "«-den»"),
  tok("هٰذِهِ", "hadhihi", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("الْمَسْئُولِيَّةِ", "masuliyya", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ — مَصْدَرٌ صِنَاعِيٌّ.", "«responsibility» — a badal; an abstract nisba noun.", "«sorumluluktan» — bedel; masdar-ı sınâî."),
  naat("الْمُرْهِقَةِ", "murhiq", "«exhausting»", "«yorucu»", tags=["ism-fail", "form-iv-verbs"], punct="."),
])
# ---------------------------------------------------------------- §31 وَلٰكِنْ شُبِّهَ لَهُمْ (print p. 59)
sen("s2", "And so the procession reached the gate of the gallows; the gallows police came forward and took over the matter from the civil police; they saw the youth carrying the cross, the crowd was thrown into confusion and the clamour grew,",
        "Böylece alay darağacının kapısına vardı; darağacı polisi ilerleyip işi sivil polisten devraldı; genci çarmıhı taşırken gördüler; herkes birbirine karıştı, gürültü arttı;", [
  tok("وَهٰكَذَا", "hakadha", "part", [AT], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰكَذَا: هَا لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ — بِمَعْنَى: عَلَى هٰذَا النَّحْوِ.", "«and so» — «like this».", "«ve böylece» — «bu şekilde».", segments=wa_("هٰكَذَا", "hakadha", "part")),
  mazi("وَصَلَ", "wasala", "«reached»", "«vardı»", tags=["mithal-verbs"], hidden=None),
  fail("الْمَوْكِبُ", "mawkib", "«the procession»", "«alay»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("بَابِ", "bab", "«the gate [of]»", "«kapısına»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْمَشْنَقِ", "mashnaq", "«the gallows»", "«darağacının»", punct="،"),
  tok("فَتَقَدَّمَ", "taqaddama", "verb", [AT, "form-v-verbs"], "الْفَاءُ عَاطِفَةٌ، وَتَقَدَّمَ فِعْلٌ مَاضٍ.", "«came forward»", "«ilerledi»", segments=[seg("فَ", "fa", "conj"), seg("تَقَدَّمَ", "taqaddama", "verb")]),
  fail("شُرْطَةُ", "shurta", "«the police [of]»", "«polisi»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الْمَشْنَقِ", "mashnaq", "«the gallows»", "«darağacı»", punct="،"),
  mazi_pl("وَتَسَلَّمُوا", "tasallama", "«and took over»", "«ve devraldılar»", tags=[AT, "form-v-verbs"], wa=True),
  maful_("الْأَمْرَ", "amr", "«the matter»", "«işi»"),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  majrur("الشُّرْطَةِ", "shurta", "«the police»", "«polisten»"),
  js_naat("الْمَدَنِيِّينَ", "madani", "«civil»", "«sivil»", tags=["ism-mansub"], punct="،"),
  tok("وَرَأَوُا", "raa", "verb", [AT, MX, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَأَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ، ضُمَّتْ لِالْتِقَاءِ السَّاكِنَيْنِ (رَأَوُا الشَّابَّ) — رَأَى الْبَصَرِيَّةُ.", "«and they saw» — the group's wāw takes a ḍamma before the waṣl.", "«ve gördüler» — cemi vâvı vasl öncesi damme aldı.", segments=wa_("رَأَوُا", "raa", "verb")),
  maful_("الشَّابَّ", "shabb", "«the youth»", "«genci»", tags=["doubled-verbs"]),
  mudari("يَحْمِلُ", "hamala", "«carrying»", "«taşırken»", tags=[HL], extra_ar=" — وَالْجُمْلَةُ حَالٌ مِنَ الشَّابَّ"),
  maful_("الصَّلِيبَ", "salib", "«the cross»", "«çarmıhı»", punct="،"),
  mazi("وَاخْتَلَطَ", "ikhtalata", "«and was mixed»", "«ve karıştı»", tags=[AT, "form-viii-verbs"], wa=True, hidden=None),
  fail("الْحَابِلُ", "habil", "«the snarer»", "«tuzakçı»", tags=["ism-fail"], extra_ar=" — اخْتَلَطَ الْحَابِلُ بِالنَّابِلِ: مَثَلٌ لِاخْتِلَاطِ الْأَمْرِ"),
  bi_noun("بِالنَّابِلِ", "nabil", "«with the archer»", "«okçuyla»", tags=["ism-fail"], punct="،"),
  mazi("وَكَثُرَ", "kathura", "«and grew»", "«ve arttı»", tags=[AT], wa=True, hidden=None),
  fail("الضَّجِيجُ", "dajij", "«the clamour»", "«gürültü»", punct="،"),
])
sen("s3", "so one took the hand of the youth carrying the cross — never doubting that he was the one sentenced to crucifixion — while he shouted and clamoured, proclaiming his innocence and that he had nothing to do with the sentence and the crucifixion, having only been made to carry the beam by forced labour and injustice;",
        "bunun üzerine biri, çarmıhı taşıyan gencin elinden tuttu — onun çarmıha mahkûm edilen kişi olduğundan hiç şüphe etmeksizin — genç ise bağırıyor, feryat ediyor, masumluğunu, hükümle ve çarmıhla bir ilgisi olmadığını, tahtayı taşımakla ancak angarya ve zulümle yükümlü kılındığını ilân ediyordu;", [
  tok("فَأَخَذَ", "akhadha", "verb", [AT], "الْفَاءُ عَاطِفَةٌ، وَأَخَذَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (أَحَدُ الشُّرْطَةِ).", "«so [one] took» — the doer is one of the police.", "«bunun üzerine tuttu» — fâil polislerden biri.", segments=[seg("فَ", "fa", "conj"), seg("أَخَذَ", "akhadha", "verb")]),
  bi_noun("بِيَدِ", "yad", "«the hand [of]»", "«elinden»", tags=[ID], extra="، مُضَافٌ"),
  mudaf_ilayh("الشَّابِّ", "shabb", "«the youth»", "«gencin»", tags=["doubled-verbs"]),
  naat("الْحَامِلِ", "hamil", "«carrying»", "«taşıyan»", tags=["ism-fail"]),
  li_noun("لِلصَّلِيبِ", "salib", "«the cross»", "«çarmıhı»", extra=" — اللَّامُ لِتَقْوِيَةِ اسْمِ الْفَاعِلِ", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — يَعُودُ عَلَى الشُّرْطِيِّ.", "«while he» — a ḥāl clause about the policeman.", "«o ise» — polisle ilgili hâl cümlesi.", segments=wa_("هُوَ", "huwa", "pron")),
  la_nafiya(),
  neg_mudari("يَشُكُّ", "shakka", "«doubts»", "«şüphe eder»", tags=[MK, "doubled-verbs"], hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  fi(),
  tok("أَنَّهُ", "anna", "part", [HJ, IW], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِفِي.", "«that he»", "«onun … olduğundan»", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("هُوَ", "huwa", "pron", ["tawkid", IW], "ضَمِيرُ فَصْلٍ (أَوْ تَوْكِيدٌ لِلْهَاءِ) لَا مَحَلَّ لَهُ.", "«he» — the pronoun of separation.", "«o» — fasıl zamiri."),
  tok("الْمَحْكُومُ", "mahkum", "noun", [IW, "ism-maful"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولٍ، نَائِبُ فَاعِلِهِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«the one sentenced» — anna's khabar.", "«mahkûm edilen» — enne'nin haberi."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«against him»", "«aleyhine»"),
  bi_noun("بِالصَّلْبِ", "salb-crucifixion", "«to crucifixion»", "«çarmıha»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ — يَعُودُ عَلَى الشَّابِّ.", "«while he» — a ḥāl clause about the youth.", "«genç ise» — gençle ilgili hâl cümlesi.", segments=wa_("هُوَ", "huwa", "pron")),
  mudari("يَصِيحُ", "saha-shout", "«shouts»", "«bağırır»", tags=[MK, "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرٌ"),
  mudari_wa("وَيَضِجُّ", "dajja", "«and clamours»", "«ve feryat eder»", tags=["doubled-verbs"], punct="،"),
  mudari_wa("وَيُعْلِنُ", "alana-announce", "«and proclaims»", "«ve ilân eder»", tags=["form-iv-verbs"]),
  noun_pron("بَرَاءَتَهُ", "baraa-innocence", "بَرَاءَتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his innocence» — the object.", "«masumluğunu» — mef'ûl.", tags=[MB, ID]),
  tok("وَأَنَّهُ", "anna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى بَرَاءَتَهُ.", "«and that he» — the clause is joined to «his innocence».", "«ve … olmadığını» — «masumluğunu»ya ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  la_jins("لَا"),
  tok("شَأْنَ", "shan", "noun", ["la-nafiya-lil-jins", IW], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — وَجُمْلَةُ لَا خَبَرُ أَنَّ.", "«[no] concern» — lā's ism; lā's clause is anna's khabar.", "«ilgi [yok]» — lâ'nın ismi; lâ cümlesi enne'nin haberi."),
  li_pron("لَهُ", "هُ", "pron-3ms", "«of his» — lā's khabar.", "«onun» — lâ'nın haberi.", tags=["la-nafiya-lil-jins"], extra=" — خَبَرُ لَا"),
  bi_noun("بِالْحُكْمِ", "hukm", "«with the sentence»", "«hükümle»"),
  atf("وَالصَّلْبِ", "salb-crucifixion", "«the crucifixion»", "«ve çarmıhla»", punct="،"),
  tok("وَإِنَّمَا", "innama", "part", [AT, "qasr"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّمَا أَدَاةُ حَصْرٍ.", "«and only»", "«ve ancak»", segments=wa_("إِنَّمَا", "innama", "part")),
  tok("كُلِّفَ", "kallafa", "verb", [NF, MX, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«he was made»", "«yükümlü kılındı»"),
  maful_("حَمْلَ", "haml", "«to carry»", "«taşımakla»", tags=[MX, ID], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ."),
  mudaf_ilayh("الْعُودِ", "ud", "«the beam»", "«tahtayı»"),
  tok("سُخْرَةً", "sukhra", "noun", [HL], "حَالٌ (أَوْ مَفْعُولٌ لِأَجْلِهِ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«by forced labour» — a ḥāl.", "«angarya olarak» — hâl."),
  atf("وَظُلْمًا", "zulm", "«injustice»", "«ve zulümle»", "nasb", punct="،"),
])
sen("s4", "while the gallows police paid no heed to that, nor understood his language, for they were of the Romans and Greeks, the ruling nation.",
        "darağacı polisi ise buna aldırmıyor ve onun dilini anlamıyordu; çünkü onlar hâkim millet olan Rumlar ve Yunanlılardandı.", [
  tok("وَشُرْطَةُ", "shurta", "noun", [HL, MK, ID], "الْوَاوُ لِلْحَالِ، وَشُرْطَةُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«while the police [of]» — a ḥāl clause's mubtadaʾ.", "«polisi ise» — hâl cümlesinin mübtedâsı.", segments=wa_("شُرْطَةُ", "shurta", "noun")),
  mudaf_ilayh("الْمَشْنَقِ", "mashnaq", "«the gallows»", "«darağacı»"),
  la_nafiya(),
  khamsa("يَلْتَفِتُونَ", "iltafata", "«pay heed»", "«aldırırlar»", tags=[MK, "la-nafiya", "form-viii-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«buna»", punct="،"),
  la_nafiya("وَلَا", wa=True),
  khamsa("يَفْهَمُونَ", "fahima", "«understand»", "«anlarlar»", tags=["la-nafiya"]),
  noun_pron("لُغَتَهُ", "lugha", "لُغَتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his language» — the object.", "«onun dilini» — mef'ûl.", tags=[MB, ID], punct="،"),
  li_anna("لِأَنَّهُمْ", "هُمْ", "pron-3mp", "«because they»", "«çünkü onlar»"),
  tok("مِنَ", "min", "prep", [HJ, IW], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«of» — the phrase is anna's khabar.", "«-den» — ibare enne'nin haberi."),
  majrur("الرُّومِ", "rum", "«the Romans»", "«Rumlar»"),
  atf("وَالْيُونَانِ", "yunan", "«the Greeks»", "«ve Yunanlılar»"),
  tok("الْأُمَّةِ", "umma", "noun", [BD], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ.", "«the nation» — a badal.", "«millet» — bedel."),
  naat("الْحَاكِمَةِ", "hakim-ruler", "«ruling»", "«hâkim»", tags=["ism-fail"], punct="."),
])
# ---------------------------------------------------------------- §32 تَنْفِيذُ حُكْمٍ (print p. 60)
sen("s5", "And every criminal disowns his crime, and every criminal has his shouting and wailing;",
        "Her suçlu suçunu inkâr eder; her suçlunun bir bağırışı ve feryadı vardır;", [
  tok("وَكُلُّ", "kull", "noun", [AT, MK, ID], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and every» — the mubtadaʾ.", "«ve her» — mübtedâ.", segments=wa_("كُلُّ", "kull", "noun")),
  mudaf_ilayh("مُجْرِمٍ", "mujrim", "«criminal»", "«suçlu»", tags=["ism-fail", "form-iv-verbs"]),
  mudari("يَتَنَصَّلُ", "tanassala", "«disowns»", "«inkâr eder»", tags=[MK, "form-v-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  noun_pron("جَرِيمَتِهِ", "jarima", "جَرِيمَتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his crime»", "«suçunu»", tags=[HJ, ID], punct="،"),
  tok("وَكُلُّ", "kull", "noun", [AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and every»", "«ve her»", segments=wa_("كُلُّ", "kull", "noun")),
  mudaf_ilayh("مُجْرِمٍ", "mujrim", "«criminal»", "«suçlunun»", tags=["ism-fail", "form-iv-verbs"]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«has» — a fronted khabar of the inner sentence.", "«vardır» — iç cümlenin öne alınmış haberi.", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ خَبَرُ كُلُّ"),
  tok("صِيَاحٌ", "siyah", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«shouting» — the delayed mubtadaʾ.", "«bir bağırış» — sonraya kalan mübtedâ."),
  atf("وَعَوِيلٌ", "awil", "«wailing»", "«ve feryat»", "raf", punct="،"),
])
sen("s6", "and they took him and carried out the sentence on him, while the Jews stood at a distance, the world night and darkness, and they were wholly convinced that the crucified one was the Messiah.",
        "onu aldılar ve hükmü onun üzerinde infaz ettiler; Yahudiler uzakta duruyordu, dünya gece ve karanlıktı; onlar çarmıha gerilenin Mesîh olduğuna kesinlikle inanıyorlardı.", [
  v_pl_pron("وَأَخَذُوهُ", "akhadha", "أَخَذُو", "هُ", "pron-3ms", "«and they took him»", "«ve onu aldılar»", wa=True),
  mazi_pl("وَنَفَّذُوا", "naffadha", "«and carried out»", "«ve infaz ettiler»", tags=[AT, "form-ii-verbs"], wa=True),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«on him»", "«onun üzerinde»"),
  maful_("الْحُكْمَ", "hukm", "«the sentence»", "«hükmü»", punct="،"),
  tok("وَالْيَهُودُ", "yahud", "noun", [HL, MK], "الْوَاوُ لِلْحَالِ، وَالْيَهُودُ مُبْتَدَأٌ مَرْفُوعٌ.", "«while the Jews» — a ḥāl clause.", "«Yahudiler ise» — hâl cümlesi.", segments=wa_("الْيَهُودُ", "yahud", "noun")),
  tok("وَاقِفُونَ", "waqif", "noun", [MK, JS, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«standing» — the khabar.", "«duruyordu» — haber."),
  prep("عَلَى", "ala", "«at»", "«-de»"),
  majrur("بُعْدٍ", "bud-distance", "«a distance»", "«uzakta»", punct="،"),
  tok("وَالدُّنْيَا", "dunya", "noun", [HL, MK, "ism-maqsur-manqus"], "الْوَاوُ لِلْحَالِ، وَالدُّنْيَا مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«and the world» — a ḥāl clause's mubtadaʾ.", "«ve dünya» — hâl cümlesinin mübtedâsı.", segments=wa_("الدُّنْيَا", "dunya", "noun")),
  tok("لَيْلٌ", "layl", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«night» — the khabar.", "«gece» — haber."),
  atf("وَظَلَامٌ", "zalam", "«darkness»", "«ve karanlık»", "raf", punct="،"),
  tok("وَهُمْ", "hum", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُمْ مُبْتَدَأٌ.", "«and they»", "«ve onlar»", segments=wa_("هُمْ", "hum", "pron")),
  khamsa("يَظُنُّونَ", "zanna", "«are convinced»", "«inanıyorlardı»", tags=[MK, MX, "doubled-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرٌ؛ ظَنَّ تَنْصِبُ مَفْعُولَيْنِ سَدَّ مَسَدَّهُمَا الْمَصْدَرُ الْمُؤَوَّلُ"),
  tok("كُلَّ", "kull", "noun", ["maful-mutlaq", ID], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ، مُضَافٌ.", "«wholly» — stands in for the absolute object.", "«kesinlikle» — mef'ûl-i mutlakın nâibi."),
  mudaf_ilayh("الظَّنِّ", "zann", "«conviction»", "«zan»", tags=["doubled-verbs"]),
  tok("أَنَّ", "anna", "part", [IW, MX], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«that»", "«ki»"),
  tok("الْمَصْلُوبَ", "maslub", "noun", [IW, "ism-maful"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the crucified one» — anna's ism.", "«çarmıha gerilen» — enne'nin ismi."),
  tok("هُوَ", "huwa", "pron", ["tawkid", IW], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ مُبْتَدَأٌ وَمَا بَعْدَهُ خَبَرُهُ).", "«is» — the pronoun of separation.", "«-dır» — fasıl zamiri."),
  tok("الْمَسِيحُ", "masih", "propn", [IW], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ — [حَاشِيَةُ الْمُؤَلِّفِ: اسْتَنَدَ فِي تَفَاصِيلِ الْقِصَّةِ إِلَى الْوَثَائِقِ الْمَسِيحِيَّةِ التَّارِيخِيَّةِ وَالْقَانُونِيَّةِ الَّتِي ظَهَرَتْ فِي الْعَصْرِ الْأَخِيرِ].", "«the Messiah» — anna's khabar. [The author's footnote: the details rest on the Christian historical and legal documents published in recent times.]", "«Mesîh» — enne'nin haberi. [Yazarın dipnotu: ayrıntılar son dönemde yayımlanan Hristiyan tarihî ve hukukî belgelere dayanır.]", punct="."),
])

CAND = {
 "huna": G("huna", "هُنَا", None, "pron", "here", "burada", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "amara-order": G("amara-order", "أَمَرَ", "أ م ر", "verb", "to order, to command", "emretmek", 1),
 "shurti": G("shurti", "شُرْطِيّ", "ش ر ط", "noun", "a policeman (a nisba)", "polis (nisbet)", 1),
 "muwakkal": G("muwakkal", "مُوَكَّل", "و ك ل", "noun", "entrusted, in charge (bi: of) (a passive participle of Form II)", "memur edilen, görevli (tef'îl ism-i mef'ûlü)", 2),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "shabb": G("shabb", "شَابّ", "ش ب ب", "noun", "a youth, a young man", "genç, delikanlı", 1, plural="شُبَّان"),
 "israili": G("israili", "إِسْرَائِيلِيّ", None, "noun", "Israelite (a nisba)", "İsrâilî (nisbet)", 2, plural="إِسْرَائِيلِيُّونَ"),
 "haml": G("haml", "حَمْل", "ح م ل", "noun", "carrying", "taşıma", 1),
 "ud": G("ud", "عُود", "ع و د", "noun", "a beam, a piece of wood", "tahta, ağaç parçası", 2, plural="أَعْوَاد"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "ashadd": G("ashadd", "أَشَدّ", "ش د د", "noun", "more intense, most (an elative of a doubled root)", "daha şiddetli, en (muzâaf kökten ism-i tafdîl)", 1),
 "zamil": G("zamil", "زَمِيل", "ز م ل", "noun", "a fellow, a colleague", "arkadaş, meslektaş", 1, plural="زُمَلَاء"),
 "hamasa": G("hamasa", "حَمَاسَة", "ح م س", "noun", "zeal, enthusiasm", "coşku, heyecan", 2),
 "akbar": G("akbar", "أَكْبَر", "ك ب ر", "noun", "greater, greatest (an elative)", "daha büyük, en büyük (ism-i tafdîl)", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "sifaha": G("sifaha", "سَفَاهَة", "س ف ه", "noun", "folly, foolishness", "sefihlik, akılsızlık", 2),
 "ahras": G("ahras", "أَحْرَص", "ح ر ص", "noun", "keener, keenest (an elative)", "daha hırslı, en hırslı (ism-i tafdîl)", 2),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "idha-harm": G("idha-harm", "إِيذَاء", "أ ذ ي", "noun", "hurting, harming (the maṣdar of Form IV)", "eziyet etme (if'âl masdarı)", 2),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "mubadara": G("mubadara", "مُبَادَرَة", "ب د ر", "noun", "being first, taking the initiative (the maṣdar of Form III)", "önce davranma, girişim (müfâale masdarı)", 2),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "hatta": G("hatta", "حَتَّى", None, "part", "until; so that; even", "-e kadar; tâ ki; hatta", 1),
 "intaha": G("intaha", "اِنْتَهَى", "ن ه ي", "verb", "to end, to come to an end (Form VIII, defective)", "bitmek, sona ermek (iftiâl, nâkıs)", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1, plural="أُمُور"),
 "sari": G("sari", "سَرِيع", "س ر ع", "noun", "quick, fast", "hızlı, çabuk", 1),
 "takhallasa": G("takhallasa", "تَخَلَّصَ", "خ ل ص", "verb", "to be rid (min: of) (Form V)", "kurtulmak (tefa''ul)", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu (müennes)", 1),
 "masuliyya": G("masuliyya", "مَسْئُولِيَّة", "س أ ل", "noun", "responsibility (an abstract nisba)", "sorumluluk, mesuliyet (masdar-ı sınâî)", 1),
 "murhiq": G("murhiq", "مُرْهِق", "ر ه ق", "noun", "exhausting, burdensome (an active participle of Form IV)", "yorucu, ağır (if'âl ism-i fâili)", 2),
 "hakadha": G("hakadha", "هٰكَذَا", None, "part", "thus, like this", "böylece, işte böyle", 1),
 "wasala": G("wasala", "وَصَلَ", "و ص ل", "verb", "to reach, to arrive (an assimilated verb)", "varmak, ulaşmak (misâl fiil)", 1),
 "mawkib": G("mawkib", "مَوْكِب", "و ك ب", "noun", "a procession", "alay, kafile", 2, plural="مَوَاكِب"),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "bab": G("bab", "بَاب", "ب و ب", "noun", "a door, a gate; a chapter", "kapı; bab", 1, plural="أَبْوَاب"),
 "mashnaq": G("mashnaq", "مَشْنَق", "ش ن ق", "noun", "a gallows, a place of execution", "darağacı", 3),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "taqaddama": G("taqaddama", "تَقَدَّمَ", "ق د م", "verb", "to come forward, to advance (Form V)", "ilerlemek, öne çıkmak (tefa''ul)", 1),
 "shurta": G("shurta", "شُرْطَة", "ش ر ط", "noun", "the police", "polis, zabıta", 1),
 "tasallama": G("tasallama", "تَسَلَّمَ", "س ل م", "verb", "to take over, to receive (Form V)", "devralmak, teslim almak (tefa''ul)", 2),
 "madani": G("madani", "مَدَنِيّ", "م د ن", "noun", "civil, civilian (a nisba)", "sivil, medenî (nisbet)", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see; to deem", "görmek; saymak", 1),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry", "taşımak", 1),
 "salib": G("salib", "صَلِيب", "ص ل ب", "noun", "a cross", "çarmıh, haç", 1, plural="صُلْبَان"),
 "ikhtalata": G("ikhtalata", "اِخْتَلَطَ", "خ ل ط", "verb", "to be mixed, to be confused (Form VIII)", "karışmak (iftiâl)", 1),
 "habil": G("habil", "حَابِل", "ح ب ل", "noun", "a snarer (one who hunts with nets) — in the proverb of confusion", "tuzakçı, ağla avlanan — karışıklık atasözünde", 3),
 "nabil": G("nabil", "نَابِل", "ن ب ل", "noun", "an archer — in the proverb of confusion", "okçu — karışıklık atasözünde", 3),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, to abound", "çok olmak, çoğalmak", 1),
 "dajij": G("dajij", "ضَجِيج", "ض ج ج", "noun", "clamour, uproar", "gürültü, yaygara", 2),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take", "almak, tutmak", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1, plural="أَيْدٍ"),
 "hamil": G("hamil", "حَامِل", "ح م ل", "noun", "carrying, a carrier (an active participle)", "taşıyan (ism-i fâil)", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he / it", "o", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "shakka": G("shakka", "شَكَّ", "ش ك ك", "verb", "to doubt (fī: about) (doubled)", "şüphe etmek (muzâaf)", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "mahkum": G("mahkum", "مَحْكُوم", "ح ك م", "noun", "ruled; condemned (a passive participle)", "yönetilen; mahkûm (ism-i mef'ûl)", 2),
 "salb-crucifixion": G("salb-crucifixion", "صَلْب", "ص ل ب", "noun", "crucifixion", "çarmıha germe", 2),
 "saha-shout": G("saha-shout", "صَاحَ", "ص ي ح", "verb", "to shout, to cry out (hollow)", "bağırmak (ecvef)", 1),
 "dajja": G("dajja", "ضَجَّ", "ض ج ج", "verb", "to clamour, to make an uproar (doubled)", "feryat etmek, gürültü koparmak (muzâaf)", 2),
 "alana-announce": G("alana-announce", "أَعْلَنَ", "ع ل ن", "verb", "to announce, to proclaim (Form IV)", "ilân etmek (if'âl)", 1),
 "baraa-innocence": G("baraa-innocence", "بَرَاءَة", "ب ر أ", "noun", "innocence", "masumluk, beraat", 1),
 "shan": G("shan", "شَأْن", "ش أ ن", "noun", "an affair, a concern", "iş, durum, ilgi", 1, plural="شُؤُون"),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "a ruling, a sentence; rule", "hüküm; yönetim", 1, plural="أَحْكَام"),
 "innama": G("innama", "إِنَّمَا", None, "part", "only (inna + the restraining mā)", "ancak, yalnızca (inne + kâffe mâ)", 1),
 "kallafa": G("kallafa", "كَلَّفَ", "ك ل ف", "verb", "to charge, to lay upon (two objects) (Form II)", "yükümlü kılmak (iki mef'ûl) (tef'îl)", 1),
 "sukhra": G("sukhra", "سُخْرَة", "س خ ر", "noun", "forced labour, corvée", "angarya", 3),
 "zulm": G("zulm", "ظُلْم", "ظ ل م", "noun", "injustice, wrongdoing", "zulüm", 1),
 "iltafata": G("iltafata", "اِلْتَفَتَ", "ل ف ت", "verb", "to turn toward; (ilā) to pay heed to (Form VIII)", "dönüp bakmak; (ilâ ile) aldırmak (iftiâl)", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "fahima": G("fahima", "فَهِمَ", "ف ه م", "verb", "to understand", "anlamak", 1),
 "lugha": G("lugha", "لُغَة", "ل غ و", "noun", "a language", "dil, lügat", 1, plural="لُغَات"),
 "rum": G("rum", "الرُّوم", "ر و م", "propn", "the Romans, the Byzantines", "Rumlar, Romalılar", 1),
 "yunan": G("yunan", "يُونَان", None, "propn", "Greece, the Greeks", "Yunan", 2),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "hakim-ruler": G("hakim-ruler", "حَاكِم", "ح ك م", "noun", "a ruler, a governor; ruling (an active participle)", "yöneten, hâkim (ism-i fâil)", 1, plural="حُكَّام"),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "mujrim": G("mujrim", "مُجْرِم", "ج ر م", "noun", "a criminal (an active participle of Form IV)", "suçlu, mücrim (if'âl ism-i fâili)", 1),
 "tanassala": G("tanassala", "تَنَصَّلَ", "ن ص ل", "verb", "to disown, to disclaim (min) (Form V)", "inkâr etmek, sıyrılmak (tefa''ul)", 3),
 "jarima": G("jarima", "جَرِيمَة", "ج ر م", "noun", "a crime", "suç, cürüm", 1, plural="جَرَائِم"),
 "siyah": G("siyah", "صِيَاح", "ص ي ح", "noun", "shouting", "bağırış", 2),
 "awil": G("awil", "عَوِيل", "ع و ل", "noun", "wailing", "feryat, ağıt", 3),
 "naffadha": G("naffadha", "نَفَّذَ", "ن ف ذ", "verb", "to carry out, to execute (Form II)", "infaz etmek, yerine getirmek (tef'îl)", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "waqif": G("waqif", "وَاقِف", "و ق ف", "noun", "standing (an active participle)", "duran, ayakta (ism-i fâil)", 1),
 "bud-distance": G("bud-distance", "بُعْد", "ب ع د", "noun", "distance", "uzaklık, mesafe", 1),
 "dunya": G("dunya", "الدُّنْيَا", "د ن و", "noun", "this world", "dünya", 1),
 "layl": G("layl", "لَيْل", "ل ي ل", "noun", "night", "gece", 1),
 "zalam": G("zalam", "ظَلَام", "ظ ل م", "noun", "darkness", "karanlık", 1),
 "hum": G("hum", "هُمْ", None, "pron", "they", "onlar", 1),
 "zanna": G("zanna", "ظَنَّ", "ظ ن ن", "verb", "to think, to be convinced (two objects; doubled)", "zannetmek, sanmak (iki mef'ûl; muzâaf)", 1),
 "zann": G("zann", "ظَنّ", "ظ ن ن", "noun", "a supposition, a conviction", "zan", 1, plural="ظُنُون"),
 "maslub": G("maslub", "مَصْلُوب", "ص ل ب", "noun", "crucified (a passive participle)", "çarmıha gerilmiş (ism-i mef'ûl)", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "amara-order", _sg.sound1("nasara", "أَمَر", "أْمُر", "مُر", "أَمْر", "آمِر", "مَأْمُور", "أُمِرَ", "يُؤْمَرُ", "أَمَرَهُ بِالشَّيْءِ يَأْمُرُهُ: طَلَبَهُ مِنْهُ — مَهْمُوزُ الْفَاءِ؛ أَمْرُهُ: مُرْ (وَأُومُرْ بَعْدَ الْوَاوِ وَالْفَاءِ).", cls="مَهْمُوزُ الْفَاءِ"))
put_morph(mo, "intaha", _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِنْتَهَ", "نْتَه", "i", "اِنْتَه", "اِنْتِهَاء", "مُنْتَهٍ (الْمُنْتَهِي)", "مُنْتَهًى", "اُنْتُهِيَ", "يُنْتَهَى", "اِنْتَهَى الْأَمْرُ: بَلَغَ نِهَايَتَهُ؛ وَانْتَهَى عَنِ الشَّيْءِ: كَفَّ عَنْهُ — نَاقِصٌ: يَنْتَهِي، لَمْ يَنْتَهِ."))
put_morph(mo, "tasallama", _sg.derived(_sg.B5, _sg.W5, "َ", "تَسَلَّم", "تَسَلَّم", "تَسَلَّم", "تَسَلُّم", "مُتَسَلِّم", "مُتَسَلَّم", "تُسُلِّمَ", "يُتَسَلَّمُ", "تَسَلَّمَ الشَّيْءَ: أَخَذَهُ وَتَنَاوَلَهُ."))
put_morph(mo, "ikhtalata", _sg.derived(_sg.B8, _sg.W8, "َ", "اِخْتَلَط", "خْتَلِط", "اِخْتَلِط", "اِخْتِلَاط", "مُخْتَلِط", None, None, None, "اِخْتَلَطَ الشَّيْءُ بِغَيْرِهِ: امْتَزَجَ بِهِ."))
put_morph(mo, "shakka", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "شَكّ", "شَاكّ", _sg.mazi14("شَكّ", "شَكَك"), _sg.mudari14("َ", "شُكّ", "شْكُك"), ["شُكَّ", "شُكَّا", "شُكُّوا", "شُكِّي", "شُكَّا", "اُشْكُكْنَ"], "يَشُكَّ", "يَشُكَّ", "تَشُكَّ", "مَشْكُوك", "شُكَّ", "يُشَكُّ", "شَكَّ فِي الْأَمْرِ يَشُكُّ: ارْتَابَ فِيهِ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَشُكَّ."))
put_morph(mo, "saha-shout", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "صَاح", "صِح", "صِيح", "صِح", "صِح", "صِح", "صِيَاح", "صَائِح", None, None, None, "صَاحَ يَصِيحُ: رَفَعَ صَوْتَهُ — أَجْوَفُ يَائِيٌّ؛ لَمْ يَصِحْ."))
put_morph(mo, "dajja", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "ضَجِيج / ضَجّ", "ضَاجّ", _sg.mazi14("ضَجّ", "ضَجَج"), _sg.mudari14("َ", "ضِجّ", "ضْجِج"), ["ضِجَّ", "ضِجَّا", "ضِجُّوا", "ضِجِّي", "ضِجَّا", "اِضْجِجْنَ"], "يَضِجَّ", "يَضِجَّ", "تَضِجَّ", None, None, None, "ضَجَّ الْقَوْمُ يَضِجُّونَ: صَاحُوا وَأَجْلَبُوا — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَضِجَّ."))
put_morph(mo, "alana-announce", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْلَن", "عْلِن", "أَعْلِن", "إِعْلَان", "مُعْلِن", "مُعْلَن", "أُعْلِنَ", "يُعْلَنُ", "أَعْلَنَ الشَّيْءَ: أَظْهَرَهُ وَجَهَرَ بِهِ."))
put_morph(mo, "iltafata", _sg.derived(_sg.B8, _sg.W8, "َ", "اِلْتَفَت", "لْتَفِت", "اِلْتَفِت", "اِلْتِفَات", "مُلْتَفِت", None, None, None, "اِلْتَفَتَ إِلَيْهِ: صَرَفَ وَجْهَهُ إِلَيْهِ؛ وَاعْتَنَى بِهِ."))
put_morph(mo, "tanassala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَنَصَّل", "تَنَصَّل", "تَنَصَّل", "تَنَصُّل", "مُتَنَصِّل", None, None, None, "تَنَصَّلَ مِنَ الذَّنْبِ: تَبَرَّأَ مِنْهُ وَاعْتَذَرَ."))
put_morph(mo, "naffadha", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَفَّذ", "نَفِّذ", "نَفِّذ", "تَنْفِيذ", "مُنَفِّذ", "مُنَفَّذ", "نُفِّذَ", "يُنَفَّذُ", "نَفَّذَ الْحُكْمَ: أَمْضَاهُ وَأَجْرَاهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch40 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 40 (print pp. 58–60; ʿĪsā §30–32): the policeman orders a hot-headed Israelite youth to carry the beam (s1); at the gallows the police take the youth with the cross for the condemned — he cries his innocence in a tongue they do not know (s2–s4); every criminal disowns his crime; the sentence carried out in the dark, the Jews sure the crucified is the Messiah (s5–s6)."
ADD_TR = " Kırkıncı bölüm (baskı s. 58–60; Îsâ §30–32): polis, coşkulu bir İsrâilli gence tahtayı taşıtır (s1); darağacında polis çarmıhlı genci mahkûm sanır — genç anlamadıkları bir dille masumluğunu haykırır (s2–s4); her suçlu suçunu inkâr eder; hüküm karanlıkta infaz edilir, Yahudiler çarmıhtakinin Mesîh olduğundan emindir (s5–s6)."
write_out(40, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §30–32", GLOSS_ADD, notes=(), related=())
report(40, S, GLOSS_ADD, ())
