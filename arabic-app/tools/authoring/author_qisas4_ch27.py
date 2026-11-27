# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 27: «قِصَّةُ عِيسَى» §8 — the Messiah's birth defies the known and sensed: his birth, life, call and livelihood as a challenge to the settled senses, the current norms, the drawn laws and the Jews' ideals; born in an unfamiliar way, speaking in the cradle, raised by a poor devout mother, living among the poor and making no distinction; print pp. 44–45.
python3 tools/authoring/author_qisas4_ch27.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: وِلَادَةُ الْمَسِيحِ تَتَحَدَّى الْمَحْسُوسَ الْمَعْرُوفَ", "en": "The story of ʿĪsā: the Messiah's birth defies the sensed and the known", "tr": "Îsâ'nın kıssası: Mesîh'in doğumu bilinen ve hissedilene meydan okur"}
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

# ---------------------------------------------------------------- §8 وِلَادَةُ الْمَسِيحِ تَتَحَدَّى الْمَحْسُوسَ الْمَعْرُوفَ (print pp. 44–45)
sen("s1", "And the birth of the Messiah and his life, his call and his livelihood were a challenge to all of that,",
        "Mesîh'in doğumu ve hayatı, daveti ve geçimi bütün bunlara bir meydan okumaydı;", [
  tok("وَكَانَتْ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … was» — kāna with the feminine tāʾ.", "«ve … idi» — kâne, te'nis tâ'sı ile.", segments=wa_("كَانَتْ", "kana", "verb")),
  tok("وِلَادَةُ", "wilada", "noun", [KN, ID], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the birth [of]» — kāna's ism.", "«doğumu» — kâne'nin ismi."),
  mudaf_ilayh("الْمَسِيحِ", "masih", "«the Messiah»", "«Mesîh'in»"),
  pron_atf("وَحَيَاتُهُ", "hayat", "حَيَاتُ", "هُ", "pron-3ms", "«his life»", "«hayatı»", case="raf", punct="،"),
  pron_atf("وَدَعْوَتُهُ", "dawa", "دَعْوَتُ", "هُ", "pron-3ms", "«his call»", "«daveti»", case="raf"),
  pron_atf("وَمَعِيشَتُهُ", "maisha", "مَعِيشَتُ", "هُ", "pron-3ms", "«his livelihood»", "«geçimi»", case="raf", punct="،"),
  tahaddi(first=True),
  li_noun("لِكُلِّ", "kull", "«to all [of]»", "«bütün»", tags=[ID], extra="، مُضَافٌ"),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that»", "«bunlara»", punct="،"),
])
sen("s2", "a challenge to the settled sensed order, a challenge to the current norms, the followed customs, the drawn laws and the highest ideals in which the Jews believe, and the customs they compete in and kill one another over;",
        "yerleşik hissedilene bir meydan okuma; yaygın teamüllere, uyulan âdetlere, çizilmiş kanunlara, Yahudilerin inandığı yüce ideallere ve uğrunda yarışıp birbirlerini öldürdükleri âdetlere bir meydan okuma;", [
  tahaddi(),
  li_noun("لِلْمَحْسُوسِ", "mahsus", "«the sensed»", "«hissedilene»", tags=["ism-maful"]),
  naat("الْمُقَرَّرِ", "muqarrar", "«settled»", "«yerleşik»", tags=["ism-maful", "form-ii-verbs"], punct="،"),
  tahaddi(),
  li_noun("لِلْأَعْرَافِ", "urf", "«the norms»", "«teamüllere»", tags=[JT]),
  naat("الشَّائِعَةِ", "shai", "«current, widespread»", "«yaygın»", tags=["ism-fail"], punct="،"),
  atf("وَالْعَادَاتِ", "ada", "«the customs»", "«âdetlere»", tags=[JM]),
  naat("الْمُتَّبَعَةِ", "muttaba", "«followed»", "«uyulan»", tags=["ism-maful", "form-viii-verbs"], punct="،"),
  atf("وَالْقَوَانِينِ", "qanun", "«the laws»", "«kanunlara»", tags=[JT]),
  naat("الْمَرْسُومَةِ", "marsum", "«drawn, laid down»", "«çizilmiş»", tags=["ism-maful"], punct="،"),
  atf("وَالْمُثُلِ", "mithal", "«the ideals»", "«ideallere»", tags=[JT], sign="بِالْكَسْرَةِ — جَمْعُ مِثَالٍ بِمَعْنَى الْمَثَلِ الْأَعْلَى"),
  tok("الْعُلْيَا", "ulya", "noun", [NA, "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مُؤَنَّثُ الْأَعْلَى.", "«highest» — the naʿt; the feminine of aʿlā, a maqṣūr.", "«yüce» — sıfat; a'lâ'nın müennesi, maksûr."),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«in which» — the relative, a naʿt.", "«ki» — sıfat olan ism-i mevsûl."),
  mudari("يُؤْمِنُ", "aamana", "«believe»", "«inandığı»", tags=[MW, "form-iv-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«in them»", "«onlara»"),
  fail("الْيَهُودُ", "yahud", "«the Jews»", "«Yahudiler»", punct="،"),
  atf("وَالْعَادَاتِ", "ada", "«the customs»", "«âdetlere»", tags=[JM]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«which» — the relative, a naʿt.", "«ki» — sıfat olan ism-i mevsûl."),
  khamsa("يَتَنَافَسُونَ", "tanafasa", "«they compete»", "«yarışırlar»", tags=[MW, "form-vi-verbs"], extra_ar=" — وَالْجُمْلَةُ صِلَةٌ"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in them»", "«onlarda»", punct="،"),
  khamsa_wa("وَيَتَقَاتَلُونَ", "taqatala", "«and kill one another»", "«ve birbirlerini öldürürler»", tags=["form-vi-verbs"]),
  prep_pron("عَلَيْهَا", "ala", "هَا", "pron-3fs", "«over them»", "«uğrunda»", punct="؛"),
])
sen("s3", "so he was born in an unfamiliar way, and spoke to people in the cradle, and grew up in the arms of a poor, devout mother,",
        "alışılmamış bir yolla doğdu, beşikte insanlarla konuştu, fakir ve kendini ibadete vermiş bir annenin kucağında büyüdü;", [
  tok("فَوُلِدَ", "walada", "verb", [AT, NF, "mithal-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَوُلِدَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«so he was born» — a passive; the deputy doer is concealed.", "«böylece doğdu» — meçhul; nâib-i fâil gizli.", segments=[seg("فَ", "fa", "conj"), seg("وُلِدَ", "walada", "verb")]),
  prep("مِنْ", "min", "«by»", "«-den»"),
  majrur("طَرِيقَةٍ", "tariqa", "«a way»", "«bir yol»"),
  tok("غَيْرِ", "ghayr", "noun", [NA, ID], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«un-» — a naʿt, annexed.", "«olmayan» — muzâf sıfat."),
  mudaf_ilayh("مَأْلُوفَةٍ", "maluf", "«familiar»", "«alışılmış»", tags=["ism-maful"], punct="،"),
  mazi("وَكَلَّمَ", "kallama", "«and spoke to»", "«ve konuştu»", tags=[AT, "form-ii-verbs"], wa=True),
  maful_("النَّاسَ", "nas", "«people»", "«insanlarla»"),
  fi(),
  majrur("الْمَهْدِ", "mahd-cradle", "«the cradle»", "«beşikte»", punct="،"),
  mazi("وَنَشَأَ", "nashaa", "«and grew up»", "«ve büyüdü»", tags=[AT], wa=True, extra_ar=" — مَهْمُوزُ اللَّامِ"),
  fi(),
  majrur("أَحْضَانِ", "hidn", "«the arms [of]»", "«kucağında»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("أُمٍّ", "umm", "«a mother»", "«bir annenin»"),
  naat("فَقِيرَةٍ", "faqir", "«poor»", "«fakir»"),
  naat2("مُتَبَتِّلَةٍ", "mutabattil", "«devout, withdrawn to worship»", "«kendini ibadete vermiş»", case="jarr", tags=["ism-fail", "form-v-verbs"], punct="،"),
])
sen("s4", "and he lived in an atmosphere full of attack and slander, far from the shows of grandeur and wealth,",
        "saldırı ve karalamayla dolu, büyüklük ve zenginlik gösterilerinden uzak bir havada yaşadı;", [
  mazi("وَعَاشَ", "asha-live", "«and he lived»", "«ve yaşadı»", tags=[AT, "hollow-verbs"], wa=True),
  fi(),
  majrur("جَوٍّ", "jaww", "«an atmosphere»", "«bir havada»"),
  naat("مَلِيءٍ", "mali", "«full»", "«dolu»"),
  bi_noun("بِالطَّعْنِ", "tan", "«of attack»", "«saldırıyla»"),
  atf("وَالْقَدْحِ", "qadh", "«slander»", "«karalamayla»", punct="،"),
  naat2("بَعِيدٍ", "baid", "«far»", "«uzak»", case="jarr"),
  tok("عَنْ", "an", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  majrur("مَظَاهِرِ", "mazhar", "«the shows [of]»", "«gösterilerinden»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ لِإِضَافَتِهِ، مُضَافٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ."),
  mudaf_ilayh("الْعَظَمَةِ", "azama-greatness", "«grandeur»", "«büyüklük»"),
  atf("وَالْغِنَى", "ghina", "«wealth»", "«zenginlik»", tags=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَقْصُورٌ", punct="،"),
])
sen("s5", "sitting with the poor, eating with them, tender toward them, consoling the weak and the strangers,",
        "fakirlerle oturur, onlarla yemek yer, onlara şefkat gösterir, zayıfları ve gurbetteki kimseleri teselli ederdi;", [
  mudari("يُجَالِسُ", "jalasa-sit-with", "«sitting with»", "«oturur»", tags=[HL, "form-iii-verbs"], extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  maful_("الْفُقَرَاءَ", "faqir", "«the poor»", "«fakirlerle»", tags=[JT, MM], punct="،"),
  tok("وَيُؤَاكِلُهُمْ", "aakala", "verb", [AT, MB, "mudari-marfu", "form-iii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُؤَاكِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ — مَهْمُوزُ الْفَاءِ: آكَلَ يُؤَاكِلُ.", "«and eating with them» — the pronoun is its object; a Form III of a hamza-initial root.", "«ve onlarla yemek yer» — zamir mef'ûl; mehmûzü'l-fâ müfâale.", segments=[seg("وَ", "wa", "conj"), seg("يُؤَاكِلُ", "aakala", "verb"), seg("هُمْ", "pron-3mp", "pron")], punct="،"),
  mudari_wa("وَيَحْنُو", "hana-tender", "«tender»", "«şefkat gösterir»", tags=["naqis-verbs"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ"),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«toward them»", "«onlara»", punct="،"),
  mudari_wa("وَيُوَاسِي", "wasa", "«consoling»", "«teselli eder»", tags=["naqis-verbs", "form-iii-verbs"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ"),
  maful_("الضُّعَفَاءَ", "daif", "«the weak»", "«zayıfları»", tags=[JT, MM]),
  atf("وَالْغُرَبَاءَ", "gharib", "«the strangers»", "«gurbettekileri»", "nasb", tags=[JT, MM], punct="،"),
])
sen("s6", "and he made no distinction between poor and rich, ruler and ruled, noble and lowly.",
        "fakirle zengin, yönetenle yönetilen, soyluyla alçak arasında ayrım yapmazdı.", [
  la_nafiya("وَلَا", wa=True),
  neg_mudari("يُفَرِّقُ", "farraqa", "«he distinguishes»", "«ayrım yapar»", tags=["form-ii-verbs"], hidden="هُوَ"),
  zarf("بَيْنَ", "bayna", "«between»", "«arasında»"),
  mudaf_ilayh("فَقِيرٍ", "faqir", "«a poor man»", "«fakir»"),
  atf("وَغَنِيٍّ", "ghani", "«a rich man»", "«zengin»", punct="،"),
  atf("وَحَاكِمٍ", "hakim-ruler", "«a ruler»", "«yöneten»", tags=["ism-fail"]),
  atf("وَمَحْكُومٍ", "mahkum", "«one ruled»", "«yönetilen»", tags=["ism-maful"], punct="،"),
  atf("وَشَرِيفٍ", "sharif", "«a noble»", "«soylu»"),
  atf("وَوَضِيعٍ", "wadi", "«a lowly one»", "«alçak»", punct="."),
])

CAND = {
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "wilada": G("wilada", "وِلَادَة", "و ل د", "noun", "birth", "doğum", 1),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "hayat": G("hayat", "حَيَاة", "ح ي ي", "noun", "life", "hayat", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "a call, an invitation; a mission", "davet, çağrı", 1),
 "maisha": G("maisha", "مَعِيشَة", "ع ي ش", "noun", "livelihood, way of living", "geçim, yaşayış", 2),
 "tahaddi": G("tahaddi", "تَحَدٍّ", "ح د ي", "noun", "a challenge, a defiance (the manqūṣ maṣdar of Form V)", "meydan okuma (tefa''ul'ün mankûs masdarı)", 2),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "mahsus": G("mahsus", "مَحْسُوس", "ح س س", "noun", "sensed, perceptible (a passive participle)", "hissedilen, mahsûs (ism-i mef'ûl)", 2),
 "muqarrar": G("muqarrar", "مُقَرَّر", "ق ر ر", "noun", "settled, established (a passive participle of Form II)", "yerleşik, mukarrer (tef'îl ism-i mef'ûlü)", 2),
 "urf": G("urf", "عُرْف", "ع ر ف", "noun", "a norm, a custom", "örf, teamül", 2, plural="أَعْرَاف"),
 "shai": G("shai", "شَائِع", "ش ي ع", "noun", "widespread, current (an active participle)", "yaygın (ism-i fâil)", 2),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "a custom", "âdet", 1, plural="عَادَات"),
 "muttaba": G("muttaba", "مُتَّبَع", "ت ب ع", "noun", "followed (a passive participle of Form VIII)", "uyulan (iftiâl ism-i mef'ûlü)", 2),
 "qanun": G("qanun", "قَانُون", "ق ن ن", "noun", "a law", "kanun", 1, plural="قَوَانِين"),
 "marsum": G("marsum", "مَرْسُوم", "ر س م", "noun", "drawn, laid down (a passive participle)", "çizilmiş, belirlenmiş (ism-i mef'ûl)", 2),
 "mithal": G("mithal", "مِثَال", "م ث ل", "noun", "an example; an ideal (pl. مُثُل)", "misal, örnek; ideal (ç. مُثُل)", 1),
 "ulya": G("ulya", "عُلْيَا", "ع ل و", "noun", "highest (the feminine elative of aʿlā)", "en yüce (a'lâ'nın müennesi)", 2),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "tanafasa": G("tanafasa", "تَنَافَسَ", "ن ف س", "verb", "to compete (fī: in) (Form VI)", "yarışmak (tefâul)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "taqatala": G("taqatala", "تَقَاتَلَ", "ق ت ل", "verb", "to fight one another (Form VI)", "birbiriyle savaşmak (tefâul)", 2),
 "ala": G("ala", "عَلَى", None, "prep", "on, over", "üzerine", 1),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to give birth; (passive) to be born (an assimilated verb)", "doğurmak; (meçhul) doğmak (misâl fiil)", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "tariqa": G("tariqa", "طَرِيقَة", "ط ر ق", "noun", "a way, a manner", "yol, tarz", 1, plural="طَرَائِق"),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not, un-", "başka; gayri, -sız", 1),
 "maluf": G("maluf", "مَأْلُوف", "أ ل ف", "noun", "familiar, customary (a passive participle)", "alışılmış (ism-i mef'ûl)", 2),
 "kallama": G("kallama", "كَلَّمَ", "ك ل م", "verb", "to speak to (Form II)", "konuşmak, hitap etmek (tef'îl)", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "mahd-cradle": G("mahd-cradle", "مَهْد", "م ه د", "noun", "a cradle", "beşik", 1),
 "nashaa": G("nashaa", "نَشَأَ", "ن ش أ", "verb", "to grow up; to arise (a hamza-final verb)", "yetişmek, büyümek; ortaya çıkmak (mehmûzü'l-lâm)", 1),
 "hidn": G("hidn", "حِضْن", "ح ض ن", "noun", "the bosom, the arms", "kucak, bağır", 2, plural="أَحْضَان"),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "faqir": G("faqir", "فَقِير", "ف ق ر", "noun", "poor", "fakir", 1, plural="فُقَرَاء"),
 "mutabattil": G("mutabattil", "مُتَبَتِّل", "ب ت ل", "noun", "devoted to worship, withdrawn from the world (an active participle of Form V)", "kendini ibadete vermiş (tefa''ul ism-i fâili)", 3),
 "asha-live": G("asha-live", "عَاشَ", "ع ي ش", "verb", "to live (hollow)", "yaşamak (ecvef)", 1),
 "jaww": G("jaww", "جَوّ", "ج و و", "noun", "an atmosphere; the air", "hava, ortam", 1),
 "mali": G("mali", "مَلِيء", "م ل أ", "noun", "full (bi: of)", "dolu", 1),
 "tan": G("tan", "طَعْن", "ط ع ن", "noun", "stabbing; attack, defamation", "saldırı, ta'n; karalama", 2),
 "qadh": G("qadh", "قَدْح", "ق د ح", "noun", "slander, disparagement", "karalama, kadh", 3),
 "baid": G("baid", "بَعِيد", "ب ع د", "noun", "far, distant", "uzak", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "mazhar": G("mazhar", "مَظْهَر", "ظ ه ر", "noun", "an appearance, an outward show", "görünüş, mazhar", 2, plural="مَظَاهِر"),
 "azama-greatness": G("azama-greatness", "عَظَمَة", "ع ظ م", "noun", "grandeur, greatness", "büyüklük, azamet", 1),
 "ghina": G("ghina", "غِنًى", "غ ن ي", "noun", "wealth, self-sufficiency (a maqṣūr noun)", "zenginlik (maksûr isim)", 1),
 "jalasa-sit-with": G("jalasa-sit-with", "جَالَسَ", "ج ل س", "verb", "to sit with, to keep company with (Form III)", "birlikte oturmak (müfâale)", 2),
 "aakala": G("aakala", "آكَلَ", "أ ك ل", "verb", "to eat with (Form III, hamza-initial)", "birlikte yemek yemek (müfâale, mehmûzü'l-fâ)", 2),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "hana-tender": G("hana-tender", "حَنَا", "ح ن و", "verb", "to be tender (ʿalā: toward) (defective)", "şefkat göstermek (nâkıs)", 2),
 "wasa": G("wasa", "وَاسَى", "أ س و", "verb", "to console, to share another's burden (Form III, defective)", "teselli etmek, yardımlaşmak (müfâale, nâkıs)", 2),
 "daif": G("daif", "ضَعِيف", "ض ع ف", "noun", "weak", "zayıf", 1, plural="ضُعَفَاء"),
 "gharib": G("gharib", "غَرِيب", "غ ر ب", "noun", "a stranger; strange", "garip, yabancı", 1, plural="غُرَبَاء"),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "farraqa": G("farraqa", "فَرَّقَ", "ف ر ق", "verb", "to distinguish (bayna: between); to separate (Form II)", "ayırmak, ayrım yapmak (tef'îl)", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "hakim-ruler": G("hakim-ruler", "حَاكِم", "ح ك م", "noun", "a ruler (an active participle)", "yöneten, hâkim (ism-i fâil)", 1, plural="حُكَّام"),
 "mahkum": G("mahkum", "مَحْكُوم", "ح ك م", "noun", "ruled, governed (a passive participle)", "yönetilen, mahkûm (ism-i mef'ûl)", 2),
 "sharif": G("sharif", "شَرِيف", "ش ر ف", "noun", "noble", "şerefli, soylu", 1, plural="أَشْرَاف"),
 "wadi": G("wadi", "وَضِيع", "و ض ع", "noun", "lowly, of humble station", "alçak, aşağı tabakadan", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tanafasa", _sg.derived(_sg.B6, _sg.W6, "َ", "تَنَافَس", "تَنَافَس", "تَنَافَس", "تَنَافُس", "مُتَنَافِس", None, None, None, "تَنَافَسُوا فِي الشَّيْءِ: تَسَابَقُوا إِلَيْهِ وَرَغِبَ كُلٌّ فِيهِ."))
put_morph(mo, "taqatala", _sg.derived(_sg.B6, _sg.W6, "َ", "تَقَاتَل", "تَقَاتَل", "تَقَاتَل", "تَقَاتُل", "مُتَقَاتِل", None, None, None, "تَقَاتَلَ الْقَوْمُ: قَاتَلَ بَعْضُهُمْ بَعْضًا — بَابُ التَّفَاعُلِ لِلْمُشَارَكَةِ."))
put_morph(mo, "nashaa", _sg.sound1("fataha", "نَشَأ", "نْشَأ", "اِنْشَأ", "نَشْء / نُشُوء", "نَاشِئ", None, None, None, "نَشَأَ يَنْشَأُ: شَبَّ وَنَمَا؛ وَنَشَأَ الْأَمْرُ: حَدَثَ — مَهْمُوزُ اللَّامِ.", cls="مَهْمُوزُ اللَّامِ"))
put_morph(mo, "jalasa-sit-with", _sg.derived(_sg.B3, _sg.W3, "ُ", "جَالَس", "جَالِس", "جَالِس", "مُجَالَسَة", "مُجَالِس", "مُجَالَس", "جُولِسَ", "يُجَالَسُ", "جَالَسَهُ: قَعَدَ مَعَهُ."))
put_morph(mo, "aakala", _sg.derived(_sg.B3, _sg.W3, "ُ", "آكَل", "ؤَاكِل", "آكِل", "مُؤَاكَلَة", "مُؤَاكِل", "مُؤَاكَل", "أُوكِلَ", "يُؤَاكَلُ", "آكَلَهُ: أَكَلَ مَعَهُ — مَهْمُوزُ الْفَاءِ: الْهَمْزَتَانِ فِي الْمَاضِي صَارَتَا مَدَّةً (آكَلَ)."))
put_morph(mo, "wasa", _sg.derived_naqis(_sg.B3, _sg.W3, "ُ", "وَاسَ", "وَاس", "i", "وَاس", "مُوَاسَاة", "مُوَاسٍ (الْمُوَاسِي)", "مُوَاسًى", "وُوسِيَ", "يُوَاسَى", "وَاسَاهُ: شَارَكَهُ فِي مَالِهِ وَعَزَّاهُ — أَصْلُهُ آسَى (مِنْ أ س و)، وَالْوَاوُ مُبْدَلَةٌ مِنَ الْهَمْزَةِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch27 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 27 (print pp. 44–45; ʿĪsā §8): the Messiah's birth, life, call and livelihood as a challenge to the settled senses, the current norms, the drawn laws and the Jews' ideals (s1–s2); born in an unfamiliar way, speaking in the cradle, raised by a poor devout mother (s3); among attack and slander, far from grandeur (s4); with the poor, the weak and the strangers, making no distinction (s5–s6)."
ADD_TR = " Yirmi yedinci bölüm (baskı s. 44–45; Îsâ §8): Mesîh'in doğumu, hayatı, daveti ve geçimi yerleşik hissedilene, yaygın teamüllere, çizilmiş kanunlara ve Yahudilerin ideallerine bir meydan okuma (s1–s2); alışılmamış bir doğum, beşikte konuşma, fakir ve âbide bir annenin kucağı (s3); saldırı ve karalama içinde, büyüklükten uzak (s4); fakirler, zayıflar ve garipler arasında, ayrım gözetmeden (s5–s6)."
write_out(27, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §8", GLOSS_ADD, notes=(), related=())
report(27, S, GLOSS_ADD, ())
