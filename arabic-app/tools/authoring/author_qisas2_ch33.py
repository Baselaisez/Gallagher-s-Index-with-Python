# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 33: «نَاقَةُ ثَمُود» §7 قَدْ أَخْطَأَ ظَنُّنَا (the people disbelieved in Ṣāliḥ; when he admonished them and kept them from idol-worship they said: O Ṣāliḥ, you were a very fine, very sensible boy; we thought you would be among the great and the notables, like so-and-so — but you became nothing; those of your age, and below you in sense, have become great men; and you took the road of poverty: our opinion of you was wrong, our hope in you failed; poor your father, he got no good from you; poor your mother, her toil over you is wasted! Ṣāliḥ heard all this and grieved for his people; whenever he passed by people they said: God have mercy on Ṣāliḥ's father, his son is lost). Print pp. 58–60.
python3 tools/authoring/author_qisas2_ch33.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "نَاقَةُ ثَمُودَ: قَدْ أَخْطَأَ ظَنُّنَا", "en": "The she-camel of Thamūd: our opinion was wrong", "tr": "Semûd'un devesi: zannımız yanıldı"}
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


# ---------------------------------------------------------------- § chapter 14's own small helpers
def ya_mutakallim_noun(full, lex, stem, ar_role, en, tr, punct=None, tags=()):
    """a noun annexed to the yāʾ of the speaker: its case vowel is estimated on the letter before the yāʾ"""
    return tok(full, lex, "noun", [ID, YM] + list(tags), ar_role + " بِحَرَكَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِكَسْرَةِ الْمُنَاسَبَةِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", en + " — annexed to the speaker's yāʾ; the case vowel is estimated.", tr + " — mütekellim yâ'sına muzâf; i'râb harekesi takdîrîdir.", punct=punct, segments=[seg(stem, lex, "noun"), seg("ي", "pron-1s", "pron")])
def laysa_tok(full="لَيْسَ", ar_tail="", en_tail="", tr_tail="", tags=(), wa=False, punct=None):
    full = conj_full(full, wa); wa = wa and bool(conj_of(full))
    return tok(full, "laysa", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"] + list(tags), W(wa, full) + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + ar_tail + ".", Wen(wa, full) + "«is not» — laysa, the frozen verb of the kāna family" + en_tail + ".", Wtr(wa, full) + "«değildir» — leyse, kâne ailesinin câmid fiili" + tr_tail + ".", punct=punct, segments=(conj_segs(full, "laysa", "verb") if wa else None))
def inni(punct=None):
    return tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«indeed I» — inna with the speaker's yāʾ as its ism.", "«şüphesiz ben» — inne; yâ ismi.", punct=punct, segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")])
def rabbi(punct=None):
    return tok("رَبِّ", "rabb", "noun", [VM, ID, YM, "hadhf-wa-taqdir"], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا — وَحَرْفُ النِّدَاءِ مَحْذُوفٌ (يَا رَبِّ).", "«my Lord» — a vocative annexed to the elided yāʾ of the speaker; the kasra points to it, and «yā» is understood.", "«Rabbim» — mahzuf mütekellim yâ'sına muzâf münâdâ; kesre ona delâlet eder; nidâ harfi mahzuf.", punct=punct)
def bihi(punct=None, role=""):
    return prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«of it»" + role, "«ona dair»", punct=punct)
def ilm_ism_laysa(punct=None):
    return tok("عِلْمٌ", "ilm", "noun", [KN], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«knowledge» — laysa's delayed ism.", "«bilgi» — leyse'nin sonraya bırakılmış ismi.", punct=punct)
def ma_laysa_ilm(li_full, li_pron_form, li_pron_lex, li_en, li_tr, punct=None):
    """مَا لَيْسَ لَكَ / لِي بِهِ عِلْمٌ — the relative with laysa, its fronted khabar and its delayed ism"""
    return [ma_mawsul_obj(),
            laysa_tok(ar_tail=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا", en_tail="; the clause is the relative's ṣila", tr_tail="; cümle sıladır", tags=[MW]),
            tok(li_full, "li", "prep", [HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ مُقَدَّمٌ.", li_en + " — laysa's fronted khabar.", li_tr + " — leyse'nin öne alınmış haberi.", segments=[seg("لِ" if li_full.startswith("لِ") else "لَ", "li", "prep"), seg(li_pron_form, li_pron_lex, "pron")]),
            bihi(role=" — the returning pronoun"),
            ilm_ism_laysa(punct=punct)]


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


# ---------------------------------------------------------------- § chapter 16's own small helpers (the storm — ʿĀd)
def aad(case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok({"raf": "عَادٌ", "nasb": "عَادًا", "jarr": "عَادٍ"}[case], "aad", "propn", list(tags), role_ar + " " + C + " — عَلَمٌ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ، مُنْصَرِفٌ (عَادٌ، عَادًا، عَادٍ).", en + " — ʿĀd; a three-letter name with a quiescent middle, so it takes tanwīn.", tr + " — Âd; ortası sâkin üç harfli özel isim, munsarif.", punct=punct)
def aad_mi(punct=None): return aad("jarr", "مُضَافٌ إِلَيْهِ", "«[of] ʿĀd» — the mudaf ilayh", "«Âd'ın» — muzâfun ileyh", punct=punct, tags=[ID])
def kanat(full="وَكَانَتْ", wa=True, ism_note=""):
    full = conj_full(full, wa); wa = wa and bool(conj_of(full))
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], W(wa, full) + "كَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ" + ism_note + ".", Wen(wa, full) + "«was / were» — kāna with the feminine tāʾ.", Wtr(wa, full) + "«idi» — te'nis tâ'lı kâne.", segments=(conj_segs(full, "kana", "verb") if wa else None))
def tamlau(obj_full, obj_lex, obj_en, obj_tr, punct=None, obj_tags=()):
    return [tok("تَمْلَأُ", "malaa", "verb", [KN, "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَتْ؛ مَهْمُوزُ اللَّامِ.", "«fill» — the muḍāriʿ; the clause is kāna's khabar.", "«doldurur(du)» — muzâri; cümle kâne'nin haberi."),
            maful(obj_full, obj_lex, obj_en, obj_tr, tags=list(obj_tags), punct=punct)]
def ism_kanat_idafa(full, lex, en, tr, tags=()):
    return tok(full, lex, "noun", [KN, ID] + list(tags), "اسْمُ كَانَتْ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en + " — kāna's ism, annexed.", tr + " — kâne'nin ismi, muzâf.")
def manzar_jamil(li_full, pron_form, pron_lex, li_en, li_tr, punct=None):
    return [tok("كَانَ", "kana", "verb", [KN, "hollow-verbs", "idha-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ — جَوَابُ إِذَا.", "«there was» — kāna, the answer of idhā.", "«… olurdu» — izâ'nın cevabı kâne."),
            tok(li_full, "li", "prep", [HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — خَبَرُ كَانَ مُقَدَّمٌ.", li_en + " — kāna's fronted khabar.", li_tr + " — kâne'nin öne alınmış haberi.", segments=[seg("لَ", "li", "prep"), seg(pron_form, pron_lex, "pron")]),
            ism_kana("مَنْظَرٌ", "manzar", "«a sight»", "«bir manzara»", ar="اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ."),
            naat("جَمِيلٌ", "jamil", "«beautiful»", "«güzel»", case="raf"),
            tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (يَجْمُلُ جَمَالًا جِدًّا)، أَوْ صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ.", "«very» — standing in for an absolute object.", "«çok» — mef'ûl-i mutlakın nâibi.", punct=punct)]


# ---------------------------------------------------------------- § chapter 17's own small helpers
def khamsa_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, extra=""):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ""
    body = full[2:] if wa else full
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if wa else []) + [AK, "mudari-marfu", MB] + list(tags), pre + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", ("«and» + " if wa else "") + en + " — one of the five verbs; the attached pronoun is its object.", ("«ve» + " if wa else "") + tr + " — ef'âl-i hamseden; bitişik zamir mef'ûl.", punct=punct, segments=segs)
def asnam_maful_(punct=None, tags=()): return maful("الْأَصْنَامَ", "sanam", "«the idols»", "«putlara»", tags=[JT] + list(tags), punct=punct)
def ummat_nuh(case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return [tok({"raf": "أُمَّةُ", "jarr": "أُمَّةِ"}[case], "umma", "noun", [ID] + list(tags), role_ar + " " + C + "، مُضَافٌ.", en + " — annexed.", tr + " — muzâf."),
            tok("نُوحٍ", "nuh", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ»", "«Nûh'un»", punct=punct)]
def uqul_ism_kanat():
    return noun_pron("عُقُولُهُمْ", "aql", "عُقُولُ", "هُمْ", "pron-3mp", "اسْمُ كَانَتْ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ عَقْلٍ.", "«their minds» — kāna's ism.", "«akılları» — kâne'nin ismi.", tags=[KN, ID, JT])


# ---------------------------------------------------------------- § chapter 18's own small helpers
def sarat(full="وَصَارَتْ", wa=True):
    full = conj_full(full, wa); wa = wa and bool(conj_of(full))
    return tok(full, "sara", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], W(wa, full) + "صَارَتْ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ — يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", Wen(wa, full) + "«became» — ṣāra, a sister of kāna, with the feminine tāʾ.", Wtr(wa, full) + "«oldu» — kâne'nin kardeşi sâre, te'nis tâ'lı.", segments=(conj_segs(full, "sara", "verb") if wa else None))
def wabal_ala_nas(punct="."):
    return [khabar_kana("وَبَالًا", "wabal", "«a curse»", "«bir vebal»", ar="خَبَرُ صَارَتْ مَنْصُوبٌ بِالْفَتْحَةِ."),
            prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«on them»", "«onlara»"),
            wa_prep("وَعَلَى", "ala", "«on»", "«-e»"),
            majrur("النَّاسِ", "nas", "«people»", "«insanlara»", punct=punct)]
def madha_yamnauhum(full_madha, min_obj_full, min_obj_lex, en_obj, tr_obj, punct="؟"):
    c = conj_of(full_madha)
    return [tok(full_madha, "madha", "pron", ([AT] if c else []) + [IS, MK], W(bool(c), full_madha) + "مَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", Wen(bool(c), full_madha) + "«what» — the question noun as the mubtadaʾ.", Wtr(bool(c), full_madha) + "«ne» — mübtedâ olan soru ismi.", segments=(conj_segs(full_madha, "madha", "pron") if c else None)),
            tok("يَمْنَعُهُمْ", "manaa", "verb", [MK, "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (يَعُودُ عَلَى مَاذَا)، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«keeps them» — the muḍāriʿ with its object; the clause is the khabar.", "«onları alıkoyar» — mef'ûl zamirli muzâri; cümle haber.", segments=[seg("يَمْنَعُ", "manaa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
            mina(),
            majrur(min_obj_full, min_obj_lex, en_obj, tr_obj, punct=punct)]
def minhumu(): return prep_pron("مِنْهُمُ", "min", "هُمُ", "pron-3mp", "«among them»", "«onlardan»", extra_ar="، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ")
def ka_noun(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [HJ] + list(tags), "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".", "«like» + " + en, "«gibi» + " + tr, punct=punct, segments=[seg("كَ", "ka", "prep"), seg(full[2:], lex, "noun")])


# ---------------------------------------------------------------- § chapter 20's own small helpers
def rasulan(punct=None, extra=""): return maful("رَسُولًا", "rasul", "«a messenger»", "«bir elçi»", punct=punct, extra_ar=extra)
def inna_allah_la_(verb, lex, en, tr, obj_full, obj_lex, obj_en, obj_tr, tags=(), tail=None, punct=None):
    return [inna(), allah_ism(), la_nafiya(),
            neg_mudari(verb, lex, en, tr, hidden="هُوَ", tags=[IW] + list(tags), extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ")] + (tail or []) + [maful(obj_full, obj_lex, obj_en, obj_tr, punct=punct)]
def akl_shurb_lahw_laib(case="jarr", punct=None, tail=()):
    C = "jarr"
    return [tok("الْأَكْلِ", "akl", "noun", [HJ, "masdar"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«eating»", "«yemekte»"),
            atf("وَالشُّرْبِ", "shurb", "«drinking»", "«içmekte»", case=C, tags=["masdar"]),
            atf("وَاللَّهْوِ", "lahw", "«amusement»", "«eğlencede»", case=C, tags=["masdar"]),
            atf("وَاللَّعِبِ", "laib", "«play»", "«oyunda»", case=C, tags=["masdar"], punct=(punct if not tail else None))] + list(tail)
def uqalaa_aghbiya(punct="،"):
    return [tok("عُقَلَاءَ", "aqil", "noun", [KN, JT, MM], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (فُعَلَاء)؛ جَمْعُ عَاقِلٍ.", "«clever» — kāna's khabar; a diptote plural.", "«akıllı» — kâne'nin haberi; gayr-i munsarif cemi."),
            fi(), tok("الدُّنْيَا", "dunya", "noun", [HJ, "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the world»", "«dünyada»"),
            tok("أَغْبِيَاءَ", "ghabi", "noun", [KN, JT, MM], "خَبَرٌ ثَانٍ لِكَانَ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (أَفْعِلَاء)؛ جَمْعُ غَبِيٍّ.", "«dull» — a second khabar of kāna.", "«ahmak» — kâne'nin ikinci haberi."),
            fi(), majrur("الدِّينِ", "din", "«religion»", "«dinde»", punct=punct)]


# ---------------------------------------------------------------- § chapter 21's own small helpers
def hud_fail(punct=None): return tok("هُودٌ", "hud-prophet", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ، مُنْصَرِفٌ.", "«Hūd» — the doer; the name takes tanwīn.", "«Hûd» — fâil; munsarif.", punct=punct)
def kum_obj_verb(full, lex, stem, en, tr, punct=None, tags=(), wa=False, extra=""):
    """a māḍī with the addressees' كُمْ as its object, the doer concealed (He)"""
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ""
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "verb"), seg("كُمْ", "pron-2mp", "pron")]
    return tok(full, lex, "verb", ([AT] if wa else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَكُمْ مَفْعُولٌ بِهِ" + extra + ".", ("«and» + " if wa else "") + en + " — a māḍī; «you» (pl.) is its object.", ("«ve» + " if wa else "") + tr + " — mâzî; «sizi» mef'ûl.", punct=punct, segments=segs)
def a_raaytum(full, en, tr):
    c = full[2:4]
    return tok(full, "raa", "verb", [IS, AT, MB, "naqis-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَ" + ("الْفَاءُ بَعْدَهَا" if c == "فَ" else "الْوَاوُ بَعْدَهَا") + " عَاطِفَةٌ، وَرَأَيْتُمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ.", en + " — the denying question hamza + the conjunction + «you have seen» with the doer's tāʾ.", tr + " — inkârî soru hemzesi + atıf + fâil tâ'lı «gördünüz».", segments=[seg("أَ", "hamza-istifham", "part"), seg(c, "fa" if c == "فَ" else "wa", "conj"), seg("رَأَيْتُمْ", "raa", "verb")])
def hayawanan(punct=None): return maful("حَيَوَانًا", "hayawan", "«an animal»", "«bir hayvan»", punct=punct)
def sifa_mudari(full, lex, en, tr, of, punct=None, tags=()):
    return mudari(full, lex, en, tr, tags=[NA] + list(tags), hidden="هُوَ", punct=punct, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِ" + of)
def mina_hayawan(punct=None): return [mina(), majrur("الْحَيَوَانِ", "hayawan", "«the animal»", "«hayvandan»", punct=punct)]


# ---------------------------------------------------------------- § chapter 22's own small helpers
def inna_na(full="إِنَّا", wa=False, punct=None):
    full = conj_full(full, wa); wa = wa and bool(conj_of(full))
    return na_pron(full, "inna", "part", "inna", W(wa, full) + "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا (إِنَّنَا → إِنَّا بِحَذْفِ إِحْدَى النُّونَيْنِ).", Wen(wa, full) + "«indeed we» — inna with «us» as its ism; one nūn is dropped (إِنَّنَا → إِنَّا).", Wtr(wa, full) + "«şüphesiz biz» — inne + ismi olan «biz»; nûnlardan biri düşmüş.", tags=[IW], punct=punct, wa=wa)
def la_tawkid_verb(full, lex, stem, en, tr, punct=None, tags=(), extra=""):
    """لَنَرَاكَ / لَنَظُنُّكَ — the lām of emphasis on inna's verbal khabar, the addressee's كَ as object, the doer «we» concealed"""
    return tok(full, lex, "verb", [IW, "mudari-marfu", MB, "tawkid"] + list(tags), "اللَّامُ لَامُ الِابْتِدَاءِ (الْمُزَحْلَقَةُ) لِلتَّوْكِيدِ، وَ" + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ، وَالْكَافُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ" + extra + ".", en + " — the lām of emphasis slid onto inna's khabar; «we» is concealed, «you» is the object.", tr + " — inne'nin haberine kaymış tekit lâmı; fâil gizli (biz), kâf mef'ûl.", punct=punct, segments=[seg("لَ", "lam-ibtida", "part"), seg(stem, lex, "verb"), seg("كَ", "pron-2ms", "pron")])
def hud_ma(punct=None):
    return tok("هُودٍ", "hud-prophet", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Hūd»", "«Hûd'un»", punct=punct)


# ---------------------------------------------------------------- § chapter 23's own small helpers
def verb_ni(full, lex, stem, ar_body, en, tr, punct=None, tags=()):
    """a verb carrying the nūn of protection + the speaker's yāʾ as its object"""
    return tok(full, lex, "verb", [MB, YM] + list(tags), ar_body + "، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", en + " — the nūn of protection shields the verb from the speaker's yāʾ, which is its object.", tr + " — vikâye nûnu; mütekellim yâ'sı mef'ûl.", punct=punct, segments=[seg(stem, lex, "verb"), seg("نِي", "pron-1s", "pron")])
def la_kum(full="لَكُمْ", punct=None, tags=(), extra=""):
    return tok(full, "li", "prep", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ فِي مَحَلِّ جَرٍّ" + extra + ".", "«to you»", "«size»", punct=punct, segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")])
def la_hum(punct=None, tags=()):
    return tok("لَهُمْ", "li", "prep", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَهُمْ فِي مَحَلِّ جَرٍّ.", "«to them»", "«onlara»", punct=punct, segments=[seg("لَ", "li", "prep"), seg("هُمْ", "pron-3mp", "pron")])
def amantum(tags=(), punct=None, extra=""):
    return tok("آمَنْتُمْ", "aamana", "verb", ["form-iv-verbs"] + list(tags), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ" + extra + ".", "«you believe» — the māḍī with the doer's tāʾ.", "«inanırsanız» — fâil tâ'lı mâzî.", punct=punct)
def inna_allah_verb(verb_tok, punct=None): return [inna(), allah_ism(), verb_tok]
def ifal_kadha_(punct):
    return [tok("افْعَلْ", "faala", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — مَقُولُ الْقَوْلِ.", "«do» — an imperative; what is said.", "«yap» — emir; söylenen söz."),
            tok("كَذَا", "kadha", "part", [MB], "كِنَايَةٌ عَنْ عَمَلٍ غَيْرِ مُعَيَّنٍ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ (أَوْ مَفْعُولٌ مُطْلَقٌ).", "«such and such» — a stand-in for an unnamed act, as the object.", "«şunu şunu» — belirsiz işin kinâyesi; mef'ûl.", punct=punct)]


# ---------------------------------------------------------------- § chapter 25's own small helpers
def ya_hudu(wa=False, punct=None):
    return [tok("وَيَا" if wa else "يَا", "ya-nida", "part", ([AT] if wa else []) + [VM], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "يَا حَرْفُ نِدَاءٍ.", ("«and» + " if wa else "") + "«O»", ("«ve» + " if wa else "") + "«ey»", segments=(wa_("يَا", "ya-nida", "part") if wa else None)),
            tok("هُودُ", "hud-prophet", "propn", [VM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Hūd» — a single-name vocative, built on ḍamma.", "«Hûd» — müfred alem münâdâ, zamme üzere mebnî.", punct=punct)]
def daat_fihim(full_what, lex_what, en_what, tr_what, punct):
    return [mazi_ta("ضَاعَتْ", "daa-lose", "«… was lost»", "«boşa gitti»", tags=["hollow-verbs"]),
            prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«on them»", "«onlarda»"),
            tok(full_what, lex_what, "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en_what + " — the doer, annexed.", tr_what + " — fâil, muzâf."),
            hud_ma(punct=punct)]
def alihatana(case="nasb", role="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", en="«our gods» — the object.", tr="«ilâhlarımızı» — mef'ûl.", tags=(MB,)):
    return noun_pron({"nasb": "آلِهَتَنَا", "jarr": "آلِهَتِنَا"}[case], "ilah", {"nasb": "آلِهَتَ", "jarr": "آلِهَتِ"}[case], "نَا", "pron-1p", role + "، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ إِلٰهٍ.", en, tr, tags=[ID] + list(tags))


# ---------------------------------------------------------------- § chapter 26's own small helpers
def sahabat_matar(punct):
    return [tok("هٰذِهِ", "hadhihi", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bu» — mübtedâ."),
            tok("سَحَابَةُ", "sahaba-cloud", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«[is] a cloud [of]» — the khabar, annexed.", "«bulutu» — haber, muzâf."),
            mudaf_ilayh("مَطَرٍ", "matar", "«rain»", "«yağmur»", punct=punct)]
def sahabat_matar_bare(punct):
    return [tok("سَحَابَةُ", "sahaba-cloud", "noun", [MK, ID, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ (هٰذِهِ) مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«a cloud [of]» — the khabar of an understood «this».", "«bulutu» — mahzuf mübtedânın haberi."),
            mudaf_ilayh("مَطَرٍ", "matar", "«rain»", "«yağmur»", punct=punct)]
def ila_matar(punct=None): return [ila_(), majrur("الْمَطَرِ", "matar", "«the rain»", "«yağmura»", punct=punct)]
def nas_fail_(punct=None): return fail("النَّاسُ", "nas", "«the people»", "«insanlar»", punct=punct)
def wa_tafal(full, lex, en, tr, obj_full, obj_lex, obj_en, obj_tr, obj_tags=(), punct=None, extra=""):
    """وَتَهْدِمُ الْبُيُوتَ — the storm's joined muḍāriʿ (she) + its object"""
    return [mudari_wa(full, lex, en, tr, hidden="هِيَ", extra=extra), maful(obj_full, obj_lex, obj_en, obj_tr, tags=list(obj_tags), punct=punct)]
def itanaqa_(full, subj_full, subj_lex, subj_en, subj_tr, bi_full, bi_lex, bi_en, bi_tr, punct, subj_tags=(JT,), bi_tags=(JT,)):
    return [mazi(full, "itanaqa", "«and … clung»", "«ve sarıldı»", tags=[AT, "form-viii-verbs"], hidden=None, wa=True),
            fail(subj_full, subj_lex, subj_en, subj_tr, tags=list(subj_tags)),
            bi_noun(bi_full, bi_lex, bi_en, bi_tr, tags=list(bi_tags), punct=punct)]
def jumla_hal_nominal(subj_full, subj_lex, subj_en, subj_tr, verb_tok, punct=None, wa=False, subj_tags=(JT,)):
    return [tok(subj_full, subj_lex, "noun", ([AT] if wa else []) + [MK] + list(subj_tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + (subj_full[2:] if wa else subj_full) + " مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", ("«and» + " if wa else "") + subj_en + " — the mubtadaʾ.", ("«ve» + " if wa else "") + subj_tr + " — mübtedâ.", segments=(wa_(subj_full[2:], subj_lex, "noun") if wa else None)), verb_tok]


# ---------------------------------------------------------------- § chapter 27's own small helpers (Thamūd — a diptote name)
def thamud(case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ"}[case]
    return tok({"raf": "ثَمُودُ", "nasb": "ثَمُودَ", "jarr": "ثَمُودَ"}[case], "thamud", "propn", [MM] + list(tags), role_ar + " " + C + " — عَلَمٌ عَلَى الْقَبِيلَةِ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ (وَقَدْ يُصْرَفُ عَلَى إِرَادَةِ الْحَيِّ).", en + " — Thamūd; a tribe's name, a diptote (feminine proper name), so no tanwīn and fatḥa for jarr.", tr + " — Semûd; kabile adı, gayr-i munsarif (alemiyyet ve te'nis): tenvin almaz, cerde fetha.", punct=punct)
def thamud_mi(punct=None): return thamud("jarr", "مُضَافٌ إِلَيْهِ", "«[of] Thamūd» — the mudaf ilayh", "«Semûd'un» — muzâfun ileyh", punct=punct, tags=[ID])
def ummat_nuh_nasb(punct=None):
    return [tok("أُمَّةَ", "umma", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the nation [of]» — the object, annexed.", "«ümmetine» — mef'ûl, muzâf."), nuh_mi(punct=punct)]
def kama_(): return tok("كَمَا", "kama", "part", [HJ, "masdar"], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا مَصْدَرِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ.", "«as» — the kāf of likening + the masdar-making mā.", "«… gibi» — teşbih kâfı + masdariyye mâ.")
def jadat(subj_full, subj_lex, subj_en, subj_tr, bi_full, bi_lex, bi_en, bi_tr, punct, wa=False, subj_tags=(), bi_tags=(), tail=()):
    return [mazi_ta("وَجَادَتْ" if wa else "جَادَتْ", "jada", "«… gave generously»", "«cömertçe verdi»", tags=([AT] if wa else []) + ["hollow-verbs"], wa=wa),
            prep_pron("لَهُمُ", "li", "هُمُ", "pron-3mp", "«to them»", "«onlara»", extra_ar="، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ"),
            fail(subj_full, subj_lex, subj_en, subj_tr, tags=list(subj_tags)),
            bi_noun(bi_full, bi_lex, bi_en, bi_tr, tags=list(bi_tags), punct=(None if tail else punct))] + list(tail)
def raa_(punct=None, tags=(), extra=""):
    return tok("رَأَى", "raa", "verb", ["naqis-verbs", MB] + list(tags), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ" + extra + ".", "«he saw» — the defective māḍī.", "«gördü» — nâkıs mâzî.", punct=punct)
def kaannama_(): return tok("كَأَنَّمَا", "ka-annama", "part", [NA, IW], "كَأَنَّ الْمَكْفُوفَةُ بِمَا، تَدْخُلُ عَلَى الْجُمْلَةِ الْفِعْلِيَّةِ — وَالْجُمْلَةُ بَعْدَهَا صِفَةٌ.", "«as if» — ka-anna restrained by mā; the clause is a ṣifa.", "«sanki» — kâffe mâ'lı keenne; cümle sıfattır.", segments=[seg("كَأَنَّ", "kaanna", "part"), seg("مَا", "ma-kaffa", "part")])

# ---------------------------------------------------------------- § chapter 30's own small helpers (Ṣāliḥ — a name that takes tanwīn)
def salih(case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok({"raf": "صَالِحٌ", "nasb": "صَالِحًا", "jarr": "صَالِحٍ"}[case], "salih-nabi", "propn", list(tags), role_ar + " " + C + " — عَلَمٌ مُنْصَرِفٌ.", en + " — Ṣāliḥ; the name takes tanwīn.", tr + " — Sâlih; munsarif.", punct=punct)
def salih_fail(punct=None): return salih("raf", "فَاعِلٌ", "«Ṣāliḥ» — the doer", "«Sâlih» — fâil", punct=punct, tags=[FL])
def sayakunu_lahu(full_what, lex_what, en_what, tr_what, punct):
    return [tok("سَيَكُونُ", "kana", "verb", [KN, "mudari-marfu", "hollow-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«there will be» — the future sīn + kāna.", "«olacak» — istikbal sîni + kâne."),
            tok("لَهُ", "li", "prep", [HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرُ يَكُونُ مُقَدَّمٌ.", "«to him» — kāna's fronted khabar.", "«onun» — kâne'nin öne alınmış haberi.", segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
            ism_kana(full_what, lex_what, en_what, tr_what, ar="اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", punct=punct)]
def kana_waladan(full_naat, lex_naat, en_naat, tr_naat, wa=True, punct=None):
    return [kana("وَكَانَ" if wa else "كَانَ", wa=wa), khabar_kana("وَلَدًا", "walad", "«a boy»", "«bir çocuk»", ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ."),
            naat(full_naat, lex_naat, en_naat, tr_naat, case="nasb"),
            tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very»", "«çok»", punct=punct)]
def hadha_salih(punct):
    return [tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bu» — mübtedâ."),
            salih("raf", "خَبَرٌ", "«[is] Ṣāliḥ» — the khabar", "«Sâlih'tir» — haber", punct=punct, tags=[MK])]
def hadha_ibn_fulan(punct):
    return [tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bu» — mübtedâ."),
            tok("ابْنُ", "ibn", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«[is] the son [of]» — the khabar, annexed.", "«oğludur» — haber, muzâf."),
            tok("فُلَانٍ", "fulan", "noun", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — كِنَايَةٌ عَنْ عَلَمٍ.", "«so-and-so» — a stand-in for a name.", "«falanca» — ad yerine kinâye.", punct=punct)]
def yaqulun(wa=True, punct=":"):
    return khamsa("وَيَقُولُونَ" if wa else "يَقُولُونَ", "qala", "«and they say»" if wa else "«they say»", "«ve derler»" if wa else "«derler»", tags=([AT] if wa else []) + ["hollow-verbs", MB], wa=wa, punct=punct)

# ---------------------------------------------------------------- § chapter 31's own small helpers
def yakunu_hadha_rasulan(punct):
    return [tok("يَكُونُ", "kana", "verb", [KN, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«can … be» — kāna's muḍāriʿ.", "«olur mu» — kâne'nin muzârii."),
            tok("هٰذَا", "hadha", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُونُ.", "«this one» — the ism of yakūnu.", "«bu» — yekûnu'nun ismi."),
            khabar_kana("رَسُولًا", "rasul", "«a messenger»", "«bir elçi»", ar="خَبَرُ يَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ.", punct=punct)]
def ma_lakum_min_ilah(punct="."):
    return [tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not» — the negating mā.", "«yoktur» — nefiy mâ'sı."),
            tok("لَكُمْ", "li", "prep", [HJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«to you» — a fronted khabar.", "«sizin» — öne alınmış haber.", segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")]),
            tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ.", "«(any)» — the added min that strengthens the negation.", "«hiçbir» — nefyi pekiştiren zâid min."),
            tok("إِلٰهٍ", "ilah", "noun", [MK, HJ], "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا بِمِنِ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا.", "«god» — the delayed mubtadaʾ: jarr in form after the added min, rafʿ by place.", "«ilâh» — sonraya bırakılmış mübtedâ; lafzan mecrûr, mahallen merfû."),
            noun_pron("غَيْرُهُ", "ghayr", "غَيْرُ", "هُ", "pron-3ms", "نَعْتٌ لِإِلٰهٍ عَلَى الْمَحَلِّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«other than Him» — a naʿt following the place of «god» (rafʿ).", "«O'ndan başka» — «ilâh»ın mahalline uyan sıfat (merfû).", tags=[NA, ID], punct=punct)]
def ubudu_allah():
    return [tok("اعْبُدُوا", "abada", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«worship» — an imperative on the dropped nūn; the wāw is the doer.", "«kulluk edin» — nûnun hazfi üzere mebnî emir; vâv fâil."),
            allah_maful()]
def wala_zaida():
    return tok("وَلَا", "la-nafiya", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«and no» — the wāw joins; lā only restates the negation.", "«ne de» — vâv atıf; lâ nefyi pekiştiren zâid.", segments=wa_("لَا", "la-nafiya", "part"))
def mubtada_muakhkhar(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [MK] + list(tags), "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — the delayed mubtadaʾ.", tr + " — sonraya bırakılmış mübtedâ.", punct=punct)
def matuf_raf(full, lex, en, tr, of, punct=None, tags=()):
    return tok(full, lex, "noun", [AT] + list(tags), "مَعْطُوفٌ عَلَى " + of + " مَرْفُوعٌ بِالضَّمَّةِ.", en + " — joined to «" + of + "».", tr + " — «" + of + "»a ma'tûf.", punct=punct)
# ---------------------------------------------------------------- § chapter 32's own small helpers (the rich men's propaganda, 23:33–38)
def ma_hasr():
    return tok("مَا", "ma-nafiya", "part", ["la-nafiya", IQ], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا (لِانْتِقَاضِ النَّفْيِ بِإِلَّا).", "«not» — the negating mā; it does not govern, because illā breaks the negation.", "«değil» — nefiy mâ'sı; illâ nefyi bozduğu için amel etmez.")
def in_hasr():
    return tok("إِنْ", "in-nafiya", "part", ["la-nafiya", IQ], "إِنْ نَافِيَةٌ بِمَعْنَى مَا، لَا عَمَلَ لَهَا لِانْتِقَاضِ النَّفْيِ بِإِلَّا.", "«not» — the negating in, like mā; illā breaks the negation.", "«değil» — mâ mânasında nefiy in'i; illâ nefyi bozar.")
def illa_hasr():
    return tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ مُلْغَاةٌ (لِلْحَصْرِ).", "«but / only» — the exceptive, here of restriction.", "«… -den başka / ancak» — hasr edatı.")
def mimma():
    return tok("مِمَّا", "ma-mawsula", "pron", [HJ, MW], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ نُونُهُ فِي مِيمِ مَا، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«of what» — min merged into the relative mā.", "«… -den» — min, mâ'ya idgamlı; mâ ism-i mevsûl.", segments=[seg("مِمَّ", "min", "prep"), seg("ا", "ma-mawsula", "pron")])
def annakum(full="أَنَّكُمْ", role_ar="", en="«that you»", tr="«sizin … -ınızı»", tags=(), wa=False):
    return tok(full, "anna", "part", ([AT] if wa else []) + ["inna-wa-akhawatuha", IW] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَكُمْ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا" + role_ar + ".", ("«and» + " if wa else "") + en + " — anna with the addressees' pronoun as its ism.", ("«ve» + " if wa else "") + tr + " — enne; muhatap zamiri ismi.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("أَنَّ", "anna", "part"), seg("كُمْ", "pron-2mp", "pron")])
def bi_khabar_nafy(full, lex, stem, en, tr, punct=None, tags=()):
    """بِمَبْعُوثِينَ / بِمُؤْمِنِينَ — the added bāʾ on the khabar of a negated nominal sentence"""
    return tok(full, lex, "noun", [HJ, MK, JS] + list(tags), "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ" + stem + " خَبَرُ الْمُبْتَدَأِ مَجْرُورٌ لَفْظًا بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، مَرْفُوعٌ مَحَلًّا.", en + " — the added bāʾ on the khabar: jarr in form, rafʿ by place.", tr + " — haber üzerindeki zâid bâ: lafzan mecrûr, mahallen merfû.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg(stem, lex, "noun")])
def nahnu_mubtada(full="نَحْنُ", wa=False):
    return pron_mubtada(full, "nahnu", "«we»", "«biz»", wa=wa)
# ---------------------------------------------------------------- § chapter 33's own small helpers (the addressee Ṣāliḥ — كُنْتَ، أَنَّكَ، فِيكَ)
def ya_salihu(punct=None):
    return [tok("يَا", "ya-nida", "part", [VM], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("صَالِحُ", "salih-nabi", "propn", [VM, "vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Ṣāliḥ» — a single-name vocative, built on ḍamma.", "«Sâlih» — müfred alem münâdâ, zamme üzere mebnî.", punct=punct)]
def kunta(full="كُنْتَ", wa=False):
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كُنْتَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ اسْمُهَا — حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", ("«and» + " if wa else "") + "«you were» — kāna with the tāʾ as its ism; the hollow verb drops its middle letter.", ("«ve» + " if wa else "") + "«idin» — kâne; tâ ismi; ecvef ortasını düşürür.", segments=(wa_("كُنْتَ", "kana", "verb") if wa else None))
def waladan_naat(naat_full, naat_lex, naat_en, naat_tr, punct=None):
    return [khabar_kana("وَلَدًا", "walad", "«a boy»", "«bir çocuk»"),
            naat(naat_full, naat_lex, naat_en, naat_tr, case="nasb"),
            tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very»", "«çok»", punct=punct)]
def kunna_nazunnu(wa=True):
    return [tok("وَكُنَّا" if wa else "كُنَّا", "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كُنَّا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا اسْمُهَا.", ("«and» + " if wa else "") + "«we used to» — kāna with «we» as its ism.", ("«ve» + " if wa else "") + "«… -dık» — kâne; «biz» ismi.", segments=(wa_("كُنَّا", "kana", "verb") if wa else None)),
            tok("نَظُنُّ", "zanna", "verb", [KN, "mudari-marfu", "doubled-verbs", AK], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ يَسُدُّ مَسَدَّ مَفْعُولَيْهِ.", "«think» — the doubled muḍāriʿ; kāna's khabar; the anna-clause fills the seat of its two objects.", "«sanırdık» — muzâaf muzâri; kâne'nin haberi; enne cümlesi iki mef'ûlün yerini tutar.")]
def annaka():
    return tok("أَنَّكَ", "anna", "part", ["inna-wa-akhawatuha", IW], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«that you» — anna with the addressee's kāf as its ism.", "«senin» — enne; muhatap kâfı ismi.", segments=[seg("أَنَّ", "anna", "part"), seg("كَ", "pron-2ms", "pron")])
def satakunu():
    return tok("سَتَكُونُ", "kana", "verb", [IW, KN, "mudari-marfu", "hollow-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَتَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهُ مُسْتَتِرٌ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«you would be» — the future sīn + kāna's muḍāriʿ; anna's khabar.", "«olacaksın» — istikbal sîni + kâne'nin muzârii; enne'nin haberi.")
def fika(punct=None):
    return tok("فِيكَ", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ.", "«in you / about you»", "«sende / senin hakkında»", punct=punct, segments=[seg("فِي", "fi", "prep"), seg("كَ", "pron-2ms", "pron")])
def qad_mazi(full, lex, en, tr, punct=None, tags=(), hidden=None, la=False, wa=False):
    """قَدْ / لَقَدْ + a māḍī written as two tokens"""
    if la:
        q = tok("لَقَدْ", "qad", "part", ["qad-harf", "tawkid"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«surely» — the lām of an unspoken oath + qad of certainty.", "«andolsun ki» — mukadder kasem cevabının lâmı + tahkik kad'ı.", segments=[seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")])
    else:
        q = tok("وَقَدْ" if wa else "قَدْ", "qad", "part", ["qad-harf"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "قَدْ حَرْفُ تَحْقِيقٍ.", ("«and» + " if wa else "") + "«indeed» — qad before the māḍī.", ("«ve» + " if wa else "") + "«gerçekten» — mâzî önünde kad.", segments=(wa_("قَدْ", "qad", "part") if wa else None))
    return [q, mazi(full, lex, en, tr, tags=list(tags), hidden=hidden, punct=punct)]
def miskin_ab_umm(m_full, who_full, who_lex, who_stem, ar_who, en_who, tr_who, punct="،"):
    return [tok(m_full, "miskin", "noun", [MK], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«poor» — the fronted khabar.", "«zavallı» — öne alınmış haber."),
            noun_pron(who_full, who_lex, who_stem, "كَ", "pron-2ms", "مُبْتَدَأٌ مُؤَخَّرٌ " + ar_who + "، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", en_who, tr_who, tags=[MK, ID], punct=punct)]

# ---------------------------------------------------------------- §7 قَدْ أَخْطَأَ ظَنُّنَا (print pp. 58–60)
sen("s1", "And the people disbelieved in Ṣāliḥ and did not believe him.", "İnsanlar Sâlih'i inkâr etti ve ona iman etmediler.", [
  mazi("وَكَفَرَ", "kafara", "«and … disbelieved»", "«ve inkâr etti»", tags=[AT], hidden=None, wa=True),
  nas_fail(),
  tok("بِصَالِحٍ", "salih-nabi", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَصَالِحٍ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«in Ṣāliḥ» — the name takes tanwīn.", "«Sâlih'i» — munsarif alem.", segments=[seg("بِ", "bi", "prep"), seg("صَالِحٍ", "salih-nabi", "propn")]),
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and did not» — the jussive lam.", "«ve -medi» — cezm eden lem.", segments=wa_("لَمْ", "lam", "part")),
  lam_khamsa("يُؤْمِنُوا", "aamana", "«believe»", "«iman etmediler»", tags=["form-iv-verbs"], role=""),
  bihi(punct=".", role=" — in him"),
])
sen("s2", "And when Ṣāliḥ admonished them and kept them from the worship of the idols, they said:", "Sâlih onlara öğüt verip onları putlara tapmaktan alıkoyunca dediler:", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ يَتَضَمَّنُ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«and when» — the time adverbial with a conditional sense.", "«ve … -ınca» — şart mânası taşıyan zaman zarfı.", segments=wa_("لَمَّا", "lamma", "part")),
  v_pron("وَعَظَهُمْ", "waaza", "وَعَظَ", "هُمْ", "pron-3mp", "«admonished them»", "«onlara öğüt verdi»", tags=["mithal-verbs"], hidden=None),
  salih_fail(),
  v_pron("وَمَنَعَهُمْ", "manaa", "مَنَعَ", "هُمْ", "pron-3mp", "«and kept them»", "«ve onları alıkoydu»", wa=True),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("عِبَادَةِ", "ibada", "noun", [HJ, ID, "masdar"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«the worship [of]»", "«… tapmaktan»"),
  mudaf_ilayh("الْأَصْنَامِ", "sanam", "«the idols»", "«putlara»", tags=[JT]),
  qalu("قَالُوا", punct=":"),
])
sen("s3", "O Ṣāliḥ, you were a very fine boy, and you were a very sensible boy, and we used to think you would be among the great of the people and their notables.", "Ey Sâlih, sen çok soylu bir çocuktun, çok akıllı bir çocuktun; senin, insanların büyüklerinden ve ileri gelenlerinden olacağını sanırdık.", [
  *ya_salihu(),
  kunta(),
  *waladan_naat("نَجِيبًا", "najib", "«fine, of noble promise»", "«soylu»", punct="،"),
  kunta("وَكُنْتَ", wa=True),
  *waladan_naat("رَشِيدًا", "rashid", "«sensible»", "«akıllı»"),
  *kunna_nazunnu(),
  annaka(),
  satakunu(),
  tok("مِنْ", "min", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ تَكُونُ.", "«among» — the phrase is kāna's khabar.", "«-den» — câr-mecrûr kâne'nin haberi."),
  tok("كِبَارِ", "kabir", "noun", [HJ, ID, JT], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — جَمْعُ كَبِيرٍ.", "«the great [of]» — annexed; a broken plural.", "«büyüklerinden» — muzâf; cemi mükesser."),
  mudaf_ilayh("النَّاسِ", "nas", "«the people»", "«insanların»"),
  pron_atf("وَأَشْرَافِهِمْ", "sharif", "أَشْرَافِ", "هِمْ", "pron-3mp", "«their notables»", "«ileri gelenlerinden»", case="jarr", tags=[JT], punct="."),
])
sen("s4", "And we used to think you would be like so-and-so and so-and-so — but you became nothing.", "Senin falanca ve filanca gibi olacağını sanırdık — ama hiçbir şey olmadın.", [
  *kunna_nazunnu(),
  annaka(),
  satakunu(),
  tok("مِثْلَ", "mithl", "noun", [KN, ID], "خَبَرُ تَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«like» — kāna's khabar, annexed.", "«gibi» — kâne'nin haberi, muzâf."),
  mudaf_ilayh("فُلَانٍ", "fulan", "«so-and-so»", "«falanca»"),
  atf("وَفُلَانٍ", "fulan", "«and so-and-so»", "«ve filanca»", case="jarr"),
  tok("فَلَمْ", "lam", "part", [AT, LJ], "الْفَاءُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«but … not» — the jussive lam.", "«ama -medi» — cezm eden lem.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam", "part")]),
  tok("تَكُنْ", "kana", "verb", [LJ, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ مُسْتَتِرٌ: أَنْتَ — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«you became» — kāna in jazm after lam; the hollow verb loses its middle letter.", "«olmadın» — lem ile meczum kâne; ecvef ortasını düşürür."),
  khabar_kana("شَيْئًا", "shay", "«anything»", "«hiçbir şey»", ar="خَبَرُ تَكُنْ مَنْصُوبٌ بِالْفَتْحَةِ.", punct="."),
])
sen("s5", "And those who were of your age, and were below you in sense, have become great men.", "Senin yaşında olanlar, akılca senden aşağı olanlar, büyük adamlar oldular.", [
  tok("وَالَّذِينَ", "alladhina", "pron", [AT, MW, MK], "الْوَاوُ عَاطِفَةٌ (اسْتِئْنَافِيَّةٌ)، وَالَّذِينَ اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and those who» — the relative as the mubtadaʾ.", "«ve … olanlar» — mübtedâ olan ism-i mevsûl.", segments=wa_("الَّذِينَ", "alladhina", "pron")),
  kana_pl("كَانُوا", wa=False, khabar_note=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  fi(),
  noun_pron("سِنِّكَ", "sinn", "سِنِّ", "كَ", "pron-2ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«your age» — the phrase is kāna's khabar.", "«senin yaşında» — câr-mecrûr kâne'nin haberi.", tags=[HJ, ID, KN], punct="،"),
  kana_pl("وَكَانُوا", wa=True),
  noun_pron("دُونَكَ", "duna", "دُونَ", "كَ", "pron-2ms", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرُ كَانَ.", "«below you» — kāna's khabar.", "«senden aşağı» — kâne'nin haberi.", tags=[MF, ID, KN]),
  fi(),
  majrur("الْعَقْلِ", "aql", "«sense»", "«akılca»"),
  tok("أَصْبَحُوا", "asbaha", "verb", [KN, "form-iv-verbs", MK], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ (الَّذِينَ).", "«have become» — aṣbaḥa, a sister of kāna; the clause is the khabar of «those who».", "«oldular» — kâne'nin kız kardeşi asbaha; cümle «olanlar»ın haberi."),
  khabar_kana("رِجَالًا", "rajul", "«men»", "«adamlar»", tags=[JT], ar="خَبَرُ أَصْبَحَ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ رَجُلٍ."),
  naat("كِبَارًا", "kabir", "«great»", "«büyük»", case="nasb", punct="."),
])
sen("s6", "And you, O Ṣāliḥ, took the road of poverty; our opinion of you was wrong, our hope in you has failed.", "Sen ise, ey Sâlih, fakirlik yolunu tuttun; sana dair zannımız yanıldı, sana dair ümidimiz boşa çıktı.", [
  pron_mubtada("وَأَنْتَ", "anta", "«and you»", "«sen ise»", wa=True),
  *ya_salihu(),
  tok("أَخَذْتَ", "akhadha", "verb", [MK, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.", "«took» — the tāʾ is the doer; the clause is the khabar of «you».", "«tuttun» — tâ fâil; cümle «sen»in haberi."),
  tok("سَبِيلَ", "sabil", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the road [of]» — the object, annexed.", "«yolunu» — mef'ûl, muzâf."),
  mudaf_ilayh("الْفَقْرِ", "faqr", "«poverty»", "«fakirlik»", punct="؛"),
  *qad_mazi("أَخْطَأَ", "akhtaa", "«has erred»", "«yanıldı»", tags=["form-iv-verbs"]),
  noun_pron("ظَنُّنَا", "zann", "ظَنُّ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our opinion» — the doer.", "«zannımız» — fâil.", tags=[FL, ID]),
  fika(punct="،"),
  *qad_mazi("خَابَ", "khaba", "«has failed»", "«boşa çıktı»", tags=["hollow-verbs"]),
  noun_pron("رَجَاؤُنَا", "rajaa-hope", "رَجَاؤُ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — كُتِبَتِ الْهَمْزَةُ عَلَى وَاوٍ لِلضَّمَّةِ.", "«our hope» — the doer; the hamza sits on a wāw for the ḍamma.", "«ümidimiz» — fâil; hemze damme için vâv üzerine yazıldı.", tags=[FL, ID]),
  fika(punct="."),
])
sen("s7", "Poor your father: he got no good from you.", "Zavallı baban: senden bir hayır görmedi.", [
  *miskin_ab_umm("مِسْكِينٌ", "أَبُوكَ", "ab", "أَبُو", "مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "«your father» — rafʿ by the wāw of the five nouns.", "«baban» — esmâ-i hamseden; vâv ile merfû.", punct="،"),
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not»", "«-medi»"),
  mazi("نَالَ", "nala", "«he got»", "«elde etti»", tags=["hollow-verbs"], hidden="هُوَ"),
  maful("خَيْرًا", "khayr", "«any good»", "«bir hayır»"),
  tok("مِنْكَ", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ.", "«from you»", "«senden»", punct=".", segments=[seg("مِنْ", "min", "prep"), seg("كَ", "pron-2ms", "pron")]),
])
sen("s8", "Poor your mother: her toil over you has gone to waste!", "Zavallı annen: senin için çektiği emek boşa gitti!", [
  *miskin_ab_umm("مِسْكِينَةٌ", "أُمُّكَ", "umm", "أُمُّ", "مَرْفُوعٌ بِالضَّمَّةِ", "«your mother»", "«annen»", punct="،"),
  *qad_mazi("ضَاعَ", "daa-lose", "«has gone to waste»", "«boşa gitti»", tags=["hollow-verbs"], la=True),
  noun_pron("تَعَبُهَا", "taab", "تَعَبُ", "هَا", "pron-3fs", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her toil» — the doer.", "«onun emeği» — fâil.", tags=[FL, ID]),
  fika(punct="!"),
])
sen("s9", "Ṣāliḥ heard all this and grieved for his people;", "Sâlih bunların hepsini duydu ve kavmi için üzüldü;", [
  mazi("سَمِعَ", "samia", "«heard»", "«duydu»", hidden=None),
  salih_fail(),
  tok("كُلَّ", "kull", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«all [of]» — the object, annexed.", "«hepsini» — mef'ûl, muzâf."),
  ishara("هٰذَا", "hadha", "jarr", "«this»", "«bunların»", tags=[ID]),
  mazi("وَتَأَسَّفَ", "taassafa", "«and grieved»", "«ve üzüldü»", tags=[AT, "form-v-verbs"], hidden="هُوَ", wa=True),
  prep("عَلَى", "ala", "«for»", "«… için»"),
  noun_pron("قَوْمِهِ", "qawm", "قَوْمِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavmi»", tags=[HJ, ID], punct="؛"),
])
sen("s10", "and whenever Ṣāliḥ passed by some people they said: God have mercy on Ṣāliḥ's father — his son is lost.", "ve Sâlih bir topluluğun yanından geçince derlerdi: Allah Sâlih'in babasına rahmet etsin — oğlu kayboldu.", [
  idha("وَإِذَا", wa=True),
  mazi("مَرَّ", "marra", "«passed»", "«geçti»", tags=[SH, "doubled-verbs"], hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا"),
  salih_fail(),
  bi_noun("بِقَوْمٍ", "qawm", "«by some people»", "«bir topluluğa»"),
  tok("قَالُوا", "qala", "verb", [SH, "hollow-verbs", MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ — جَوَابُ إِذَا لَا مَحَلَّ لَهُ.", "«they said» — the answer of idhā.", "«derlerdi» — izâ'nın cevabı.", punct=":"),
  mazi("رَحِمَ", "rahima", "«may … have mercy»", "«rahmet etsin»", hidden=None, extra_ar=" — دُعَاءٌ بِلَفْظِ الْخَبَرِ"),
  allah_fail(),
  tok("أَبَا", "ab", "noun", [MB, ID, "five-nouns"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«the father [of]» — naṣb by the alif of the five nouns.", "«babasına» — esmâ-i hamseden; elif ile mansub."),
  salih("jarr", "مُضَافٌ إِلَيْهِ", "«Ṣāliḥ»", "«Sâlih'in»", tags=[ID]),
  *qad_mazi("ضَاعَ", "daa-lose", "«is lost»", "«kayboldu»", tags=["hollow-verbs"], la=True),
  ibn_pron("ابْنُهُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "«his son» — the doer.", "«oğlu» — fâil.", tags=[FL], punct="."),
])

CAND = {
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve", "inkâr etmek", 1),
 "nas": G("nas", "النَّاس", "ن و س", "noun", "the people", "insanlar", 1),
 "bi": G("bi", "بِ", None, "prep", "by, with", "ile", 1),
 "salih-nabi": G("salih-nabi", "صَالِح", "ص ل ح", "propn", "Ṣāliḥ — the prophet sent to Thamūd (a name that takes tanwīn)", "Sâlih — Semûd'a gönderilen peygamber (tenvinli ad)", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "lam": G("lam", "لَمْ", None, "part", "did not — the jussive lam", "-medi — cezm eden lem", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe", "inanmak", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "his / him", "onu, onun", 1),
 "lamma": G("lamma", "لَمَّا", None, "part", "when", "-ınca", 1),
 "waaza": G("waaza", "وَعَظَ", "و ع ظ", "verb", "to admonish, to exhort (an assimilated verb: وَعَظَ يَعِظُ)", "öğüt vermek, vaaz etmek (misâl fiil: veaza yeizu)", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them", "onlar (bitişik)", 1),
 "manaa": G("manaa", "مَنَعَ", "م ن ع", "verb", "to prevent, to keep from", "engellemek, alıkoymak", 1),
 "min": G("min", "مِنْ", None, "prep", "of", "-den", 1),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet, kulluk", 1),
 "sanam": G("sanam", "صَنَم", "ص ن م", "noun", "idol", "put", 1, plural="أَصْنَام"),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O!", "ey!", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "boy, child", "çocuk", 1, plural="أَوْلَاد"),
 "najib": G("najib", "نَجِيب", "ن ج ب", "noun", "fine, of noble promise, gifted", "soylu, seçkin, kabiliyetli", 1, plural="نُجَبَاء"),
 "jiddan": G("jiddan", "جِدًّا", "ج د د", "noun", "very", "çok", 1),
 "rashid": G("rashid", "رَشِيد", "ر ش د", "noun", "sensible, rightly guided", "olgun, akıllı, reşit", 1),
 "zanna": G("zanna", "ظَنَّ", "ظ ن ن", "verb", "to think, to suppose", "sanmak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "pron-2ms": G("pron-2ms", "ـكَ", None, "pron", "you (masc. sing., attached)", "sen, senin (bitişik)", 1),
 "kabir": G("kabir", "كَبِير", "ك ب ر", "noun", "great, big", "büyük", 1, plural="كِبَار"),
 "sharif": G("sharif", "شَرِيف", "ش ر ف", "noun", "noble; (pl.) the notables", "şerefli; (ç.) ileri gelenler", 1, plural="أَشْرَاف"),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "the like of, similar to", "benzer, gibi", 1, plural="أَمْثَال"),
 "fulan": G("fulan", "فُلَان", None, "noun", "so-and-so (a stand-in for a name)", "falanca", 1),
 "fa": G("fa", "فَ", None, "conj", "and, so", "ve", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "those who", "… -enler", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "sinn": G("sinn", "سِنّ", "س ن ن", "noun", "age; a tooth", "yaş; diş", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "besides", "başka", 2),
 "aql": G("aql", "عَقْل", "ع ق ل", "noun", "sense, mind", "akıl", 1, plural="عُقُول"),
 "asbaha": G("asbaha", "أَصْبَحَ", "ص ب ح", "verb", "to become (a sister of kāna, Form IV)", "olmak, hâline gelmek (kâne'nin kardeşi, if'âl)", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1, plural="رِجَال"),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (masc. sing., detached)", "sen (munfasıl)", 1),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take (its amr is خُذْ)", "almak (emri خُذْ)", 1),
 "sabil": G("sabil", "سَبِيل", "س ب ل", "noun", "way, path", "yol", 1, plural="سُبُل"),
 "faqr": G("faqr", "فَقْر", "ف ق ر", "noun", "poverty", "fakirlik, yoksulluk", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed", "gerçekten", 1),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer", "kasem cevabının lâmı", 2),
 "akhtaa": G("akhtaa", "أَخْطَأَ", "خ ط أ", "verb", "to err, to miss the mark (Form IV; أَخْطَأَهُ: it missed him)", "hata etmek; ıskalamak (if'âl)", 1),
 "zann": G("zann", "ظَنّ", "ظ ن ن", "noun", "supposition, doubt — the opinion short of certainty", "zan — kesinliğe varmayan kanaat", 3),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our (attached)", "biz / bizi / bizim (bitişik)", 1),
 "khaba": G("khaba", "خَابَ", "خ ي ب", "verb", "to fail, to come to nothing (hollow: خَابَ يَخِيبُ)", "boşa çıkmak, hüsrana uğramak (ecvef: hâbe yehîbu)", 1),
 "rajaa-hope": G("rajaa-hope", "رَجَاء", "ر ج و", "noun", "hope (maṣdar of رَجَا)", "ümit (recâ'nın masdarı)", 2),
 "miskin": G("miskin", "مِسْكِين", "س ك ن", "noun", "poor, destitute", "yoksul, miskin", 1, plural="مَسَاكِين"),
 "ab": G("ab", "أَب", "أ ب و", "noun", "father (one of the five nouns)", "baba (esmâ-i hamseden)", 1, plural="آبَاء"),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not", "değil, -medi", 1),
 "nala": G("nala", "نَالَ", "ن ي ل", "verb", "to reach, to attain", "elde etmek, nail olmak", 1),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good", "hayır, iyilik", 1),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "mother", "anne", 1, plural="أُمَّهَات"),
 "daa-lose": G("daa-lose", "ضَاعَ", "ض ي ع", "verb", "to be lost, to be wasted", "boşa gitmek, kaybolmak", 1),
 "taab": G("taab", "تَعَب", "ت ع ب", "noun", "toil, weariness", "emek, yorgunluk", 1),
 "pron-3fs": G("pron-3fs", "ـهَا", None, "pron", "her / them (fem.)", "onun, onları (dişil)", 1),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear", "duymak", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "hepsi, her", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this", "bu", 1),
 "taassafa": G("taassafa", "تَأَسَّفَ", "أ س ف", "verb", "to grieve, to regret (Form V)", "üzülmek, hayıflanmak (tefa''ul)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, for", "üzerine, için", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "people", "kavim", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ınca", 1),
 "marra": G("marra", "مَرَّ", "م ر ر", "verb", "to pass (by)", "geçmek, uğramak", 1),
 "rahima": G("rahima", "رَحِمَ", "ر ح م", "verb", "to have mercy", "merhamet etmek", 1),
 "allah": G("allah", "اللَّه", None, "propn", "Allah", "Allah", 1),
 "ibn": G("ibn", "ابْن", "ب ن ي", "noun", "son", "oğul", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "khaba", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "خَاب", "خِب", "خِيب", "خِب", "خِيب", "خِب", "خَيْبَة", "خَائِب", None, None, None, "خَابَ يَخِيبُ خَيْبَةً: لَمْ يَنَلْ مَا طَلَبَ، وَخَسِرَ — لَازِمٌ؛ أَجْوَفُ يَائِيٌّ مِثْلُ ضَاعَ يَضِيعُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch33 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 33 (print pp. 58–60; Thamūd §7): «our opinion was wrong» — the people disbelieved in Ṣāliḥ; when he admonished them and kept them from idol-worship they said: O Ṣāliḥ, you were a very fine, very sensible boy; we thought you would be among the great and the notables, like so-and-so, but you became nothing; those of your age, below you in sense, have become great men; you took the road of poverty: our opinion of you was wrong, our hope in you failed; poor your father, he got no good from you; poor your mother, her toil over you is wasted! Ṣāliḥ heard all this and grieved for his people; whenever he passed by people they said: God have mercy on Ṣāliḥ's father, his son is lost.")
ADD_TR = (" Otuz üçüncü bölüm (basılı s. 58–60; Semûd §7): «zannımız yanıldı» — insanlar Sâlih'i inkâr etti; onlara öğüt verip putlara tapmaktan alıkoyunca dediler: ey Sâlih, sen çok soylu, çok akıllı bir çocuktun; büyüklerden ve ileri gelenlerden, falanca gibi olacağını sanırdık, ama hiçbir şey olmadın; senin yaşındakiler, akılca senden aşağı olanlar büyük adamlar oldular; sen fakirlik yolunu tuttun: sana dair zannımız yanıldı, ümidimiz boşa çıktı; zavallı baban, senden hayır görmedi; zavallı annen, emeği boşa gitti! Sâlih bunları duydu ve kavmi için üzüldü; bir topluluğun yanından geçince derlerdi: Allah Sâlih'in babasına rahmet etsin, oğlu kayboldu.")
write_out(33, S, TITLE, ADD_EN, ADD_TR, "Thamūd §7, pp. 58–60", GLOSS_ADD, notes=(), related=())
report(33, S, GLOSS_ADD, ())
