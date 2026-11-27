# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 30: «قِصَّةُ عِيسَى» §12 opens — the plot to kill him foiled, God raises and honours him; «read his story in the Qurʾān»: Āl ʿImrān 3:45–47 (the angels' tidings to Maryam, the Messiah's titles, speaking in the cradle, «how shall I have a son», «Be — and it is»); print p. 47.
python3 tools/authoring/author_qisas4_ch30.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى فِي الْقُرْآنِ: بِشَارَةُ الْمَلَائِكَةِ (آل عمران ٤٥–٤٧)", "en": "The story of ʿĪsā in the Qurʾān: the angels' tidings (3:45–47)", "tr": "Kur'ân'da Îsâ kıssası: meleklerin müjdesi (Âl-i İmrân 45–47)"}
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

# ---------------------------------------------------------------- §12 قِصَّةُ عِيسَى فِي الْقُرْآنِ (print p. 47)
sen("s1", "Then they wanted to kill him and be rid of him, but God protected him and turned their plot back on them, and raised him to Himself and honoured him. Read his story in the Qurʾān:",
        "Sonra onu öldürmek ve ondan kurtulmak istediler; Allah onu korudu, tuzaklarını kendilerine çevirdi, onu katına yükseltti ve ona ikram etti. Onun kıssasını Kur'ân'da okuyun:", [
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then» — sequence with a gap.", "«sonra» — tertip ve terâhî için."),
  mazi_pl("أَرَادُوا", "arada", "«they wanted»", "«istediler»", tags=["hollow-verbs", "form-iv-verbs"]),
  noun_pron("قَتْلَهُ", "qatl", "قَتْلَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to kill him» — the object, a maṣdar.", "«onu öldürmeyi» — mef'ûl, masdar.", tags=[MB, ID]),
  atf("وَالتَّخَلُّصَ", "takhallus", "«to be rid»", "«kurtulmayı»", "nasb", tags=["form-v-verbs"]),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of him»", "«ondan»", punct="،"),
  tok("فَحَمَاهُ", "hama-protect", "verb", [AT, MB, "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَحَمَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«but God protected him» — a defective māḍī; the hāʾ is the object, before the doer.", "«Allah onu korudu» — nâkıs mâzî; hâ, fâilden önce gelen mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("حَمَا", "hama-protect", "verb"), seg("هُ", "pron-3ms", "pron")]),
  allah_fail(),
  mazi("وَرَدَّ", "radda", "«and turned back»", "«ve çevirdi»", tags=[AT, "doubled-verbs"], wa=True, hidden="هُوَ"),
  noun_pron("كَيْدَهُمْ", "kayd", "كَيْدَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their plot» — the object.", "«tuzaklarını» — mef'ûl.", tags=[MB, ID]),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«on them»", "«kendilerine»", punct="،"),
  v_pron("وَرَفَعَهُ", "rafaa", "رَفَعَ", "هُ", "pron-3ms", "«and raised him»", "«ve onu yükseltti»", wa=True),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Himself»", "«katına»"),
  v_pron("وَكَرَّمَهُ", "karrama", "كَرَّمَ", "هُ", "pron-3ms", "«and honoured him»", "«ve ona ikram etti»", tags=["form-ii-verbs"], wa=True, punct="،"),
  tok("اقْرَؤُوا", "qaraa", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَهْمُوزُ اللَّامِ؛ رُسِمَتْ هَمْزَتُهُ عَلَى وَاوٍ (وَتُرْسَمُ أَيْضًا اقْرَءُوا).", "«read» — an imperative built on dropping the nūn; the hamza sits on a wāw here (also written اقْرَءُوا).", "«okuyun» — nûnun hazfi üzere mebnî emir; hemzesi burada vâv üzerinde (اقْرَءُوا imlâsı da vardır)."),
  noun_pron("قِصَّتَهُ", "qissa", "قِصَّتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his story» — the object.", "«onun kıssasını» — mef'ûl.", tags=[MB, ID]),
  fi(),
  majrur("الْقُرْآنِ", "quran", "«the Qurʾān»", "«Kur'ân'da»", punct=":"),
])
sen("s2", "«When the angels said: O Maryam, God gives you glad tidings of a Word from Him, whose name is the Messiah, ʿĪsā son of Maryam — eminent in this world and the Hereafter, and one of those brought near;» (3:45)",
        "«Hani melekler demişti: Ey Meryem! Allah seni kendinden bir kelime ile müjdeliyor; adı Mesîh Îsâ b. Meryem'dir; dünyada ve âhirette itibarlı ve Allah'a yakın kılınanlardandır.» (3:45)", [
  *quran([
  tok("إِذْ", "idh", "noun", [MF, "hadhf-wa-taqdir"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ.", "«when» — the past ẓarf, the object of an understood «remember».", "«hani» — mâzî zarfı; mukadder «hatırla» fiilinin mef'ûlü."),
  tok("قَالَتِ", "qala", "verb", [ID, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ.", "«said» — the clause is annexed to idh; the tāʾ takes a kasra before the waṣl.", "«dedi» — cümle iz'e muzâfun ileyh; tâ vasl öncesi kesre aldı.", segments=[seg("قَالَتِ", "qala", "verb")]),
  fail("الْمَلَائِكَةُ", "malak", "«the angels»", "«melekler»", tags=[JT]),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("مَرْيَمُ", "maryam", "propn", ["vocative-munada", MM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Maryam» — a single proper-name munādā, built on ḍamma.", "«Meryem» — müfred alem münâdâ, damme üzere mebnî."),
  inna(),
  tok("اللهَ", "allah", "propn", [IW], "لَفْظُ الْجَلَالَةِ اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«God» — inna's ism.", "«Allah» — inne'nin ismi."),
  tok("يُبَشِّرُكِ", "bashshara", "verb", [IW, MB, "mudari-marfu", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْكَافُ مَفْعُولٌ بِهِ (مَكْسُورَةٌ لِلْمُؤَنَّثَةِ) — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«gives you glad tidings» — inna's khabar; the feminine kāf is the object.", "«seni müjdeliyor» — inne'nin haberi; müennes kâf mef'ûl.", segments=[seg("يُبَشِّرُ", "bashshara", "verb"), seg("كِ", "pron-2fs", "pron")]),
  bi_noun("بِكَلِمَةٍ", "kalima", "«of a Word»", "«bir kelime ile»"),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«from Him» — a ṣifa of «a Word».", "«kendinden» — kelimenin sıfatı.", tags=[NA], extra_ar=" — صِفَةٌ لِكَلِمَةٍ"),
  noun_pron("اسْمُهُ", "ism", "اسْمُ", "هُ", "pron-3ms", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِكَلِمَةٍ؛ ذُكِّرَ الضَّمِيرُ لِأَنَّ الْمُرَادَ بِالْكَلِمَةِ عِيسَى.", "«whose name» — a mubtadaʾ; the clause is a second ṣifa; the pronoun is masculine because the Word is ʿĪsā.", "«adı» — mübtedâ; cümle ikinci sıfat; zamir müzekker, çünkü kelime ile Îsâ kastedilir.", tags=[MK, ID, "jumla-sifa"]),
  tok("الْمَسِيحُ", "masih", "propn", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — the khabar.", "«Mesîh» — haber."),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — a badal.", "«Îsâ» — bedel."),
  tok("ابْنُ", "ibn", "noun", [BD, ID], "بَدَلٌ ثَانٍ (أَوْ نَعْتٌ) مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — ثَبَتَتْ أَلِفُهُ عَلَى الرَّسْمِ الْعُثْمَانِيِّ.", "«son [of]» — a further badal; its alif is kept in the ʿUthmānic orthography.", "«oğlu» — bir bedel daha; elifi Osmânî resimde sabit."),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Maryam» — a diptote muḍāf ilayh.", "«Meryem'in» — gayr-i munsarıf muzâfun ileyh."),
  hal("وَجِيهًا", "wajih", "«eminent»", "«itibarlı»", ar="حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ مِنْ كَلِمَةٍ (عَلَى الْمَعْنَى) — صِفَةٌ مُشَبَّهَةٌ."),
  fi(),
  majrur("الدُّنْيَا", "dunya", "«this world»", "«dünyada»", tags=["ism-maqsur-manqus"], ar="مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ."),
  atf("وَالْآخِرَةِ", "akhira", "«the Hereafter»", "«âhirette»"),
  wa_min(extra=" — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى وَجِيهًا فِي مَوْضِعِ الْحَالِ"),
  tok("الْمُقَرَّبِينَ", "muqarrab", "noun", [HJ, JS, HL, "ism-maful", "form-ii-verbs"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«those brought near» — jarr by the yāʾ.", "«yakın kılınanlar» — yâ ile mecrûr.", punct=AYA),
  ]),
])
sen("s3", "«and he will speak to people in the cradle and in maturity, and will be one of the righteous.» (3:46)",
        "«Beşikte ve yetişkinlikte insanlarla konuşacak ve sâlihlerden olacaktır.» (3:46)", [
  *quran([
  mudari_wa("وَيُكَلِّمُ", "kallama", "«and he speaks»", "«ve konuşur»", tags=[HL, "form-ii-verbs"], extra=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى وَجِيهًا فِي مَوْضِعِ الْحَالِ"),
  maful_("النَّاسَ", "nas", "«people»", "«insanlarla»"),
  fi(),
  majrur("الْمَهْدِ", "mahd-cradle", "«the cradle»", "«beşikte»", ar="مَجْرُورٌ بِالْكَسْرَةِ — مُتَعَلِّقٌ بِحَالٍ مَحْذُوفَةٍ: كَائِنًا فِي الْمَهْدِ."),
  tok("وَكَهْلًا", "kahl", "noun", [AT, HL], "الْوَاوُ عَاطِفَةٌ، وَكَهْلًا حَالٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى مَحَلِّ فِي الْمَهْدِ.", "«and in maturity» — a ḥāl joined to the phrase «in the cradle».", "«ve yetişkin olarak» — «beşikte» ibaresinin mahalline ma'tûf hâl.", segments=wa_("كَهْلًا", "kahl", "noun")),
  wa_min(extra=" — مَعْطُوفٌ عَلَى وَجِيهًا"),
  tok("الصَّالِحِينَ", "salih", "noun", [HJ, JS, "ism-fail"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the righteous»", "«sâlihler»", punct=AYA),
  ]),
])
sen("s4", "«She said: My Lord, how shall I have a son when no man has touched me? He said: Thus — God creates what He wills; when He decrees a matter, He only says to it: Be! and it is.» (3:47)",
        "«Dedi: Rabbim! Bana bir insan dokunmamışken benim nasıl çocuğum olur? Dedi: İşte böyle; Allah dilediğini yaratır. Bir işe hükmettiğinde ona yalnız «Ol!» der, o da oluverir.» (3:47)", [
  *quran([
  mazi_ta("قَالَتْ", "qala", "«she said»", "«dedi»", tags=["hollow-verbs"], extra=" — وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ (مَرْيَمُ)"),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID, "ya-al-mutakallim", "hadhf-wa-taqdir"], "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ اكْتِفَاءً بِالْكَسْرَةِ.", "«my Lord» — a munādā with the vocative particle and the speaker's yāʾ both dropped; the kasra stands for the yāʾ.", "«Rabbim» — nidâ harfi ve mütekellim yâ'sı hazfedilmiş münâdâ; kesre yâ'ya delâlet eder."),
  tok("أَنَّى", "anna-istifham", "pron", [IS, HL], "اسْمُ اسْتِفْهَامٍ بِمَعْنَى كَيْفَ (أَوْ: مِنْ أَيْنَ) مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ حَالٌ (أَوْ ظَرْفٌ).", "«how» — an interrogative noun, «how» or «whence», in the place of a ḥāl.", "«nasıl» — «nasıl» veya «nereden» anlamında istifhâm ismi; hâl mahallinde."),
  tok("يَكُونُ", "kana", "verb", [KN, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ بِمَعْنَى يُوجَدُ (وَيَجُوزُ نَقْصُهُ وَخَبَرُهُ لِي).", "«shall there be» — a complete kāna, «come to exist» (or incomplete, with «to me» as its khabar).", "«olur» — tam kâne, «var olur» (nâkıs sayılırsa haberi «bana»)."),
  li_pron("لِي", "ي", "pron-1s", "«to me»", "«benim»", extra=" — مُتَعَلِّقٌ بِيَكُونُ"),
  fail("وَلَدٌ", "walad", "«a son»", "«bir çocuk»", extra_ar=" — فَاعِلُ يَكُونُ التَّامَّةِ"),
  tok("وَلَمْ", "lam", "part", [HL, LJ], "الْوَاوُ لِلْحَالِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«while … not» — the wāw of ḥāl with lam.", "«… -mamışken» — hâl vâvı ile lem.", segments=wa_("لَمْ", "lam", "part")),
  tok("يَمْسَسْنِي", "massa", "verb", [LJ, MB, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ — فُكَّ إِدْغَامُ الْمُضَاعَفِ لِلْجَزْمِ (يَمْسَسْ)، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«has touched me» — jazm by sukūn: the doubled verb unfolds (yamsas); the nūn of protection, then the yāʾ as object.", "«bana dokundu» — sükûn ile meczûm: muzâaf çözüldü (yemses); vikâye nûnu, yâ mef'ûl.", segments=[seg("يَمْسَسْ", "massa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  fail("بَشَرٌ", "bashar", "«a man»", "«bir insan»"),
  mazi("قَالَ", "qala", "«He said»", "«dedi»", tags=["hollow-verbs"], hidden="هُوَ", extra_ar=" — أَيِ: اللهُ (أَوِ الْمَلَكُ)"),
  tok("كَذٰلِكِ", "kadhalika", "part", [MK, "hadhf-wa-taqdir", "asma-al-ishara"], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ، وَكَافُ الْخِطَابِ مَكْسُورَةٌ لِخِطَابِ الْمُؤَنَّثَةِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ مُبْتَدَأٍ مَحْذُوفٍ: الْأَمْرُ كَذٰلِكِ.", "«thus» — the kāf of comparison with the demonstrative; the address-kāf takes a kasra for the woman addressed; the phrase is the khabar of an understood «the matter is».", "«işte böyle» — teşbih kâf'ı ile işaret ismi; hitap kâf'ı müennese kesreli; ibare mahzuf «iş böyledir» mübtedâsının haberi."),
  tok("اللهُ", "allah", "propn", [MK], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«God» — the mubtadaʾ.", "«Allah» — mübtedâ."),
  mudari("يَخْلُقُ", "khalaqa", "«creates»", "«yaratır»", tags=[MK], extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  ma_mawsul_obj("«what»", "«… -ı»"),
  yasha(),
  tok("إِذَا", "idha", "part", ["idha-shartiyya", MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَنْصُوبٌ بِجَوَابِهِ.", "«when» — the conditional ẓarf of the future.", "«-dığında» — şart mânası taşıyan istikbâl zarfı."),
  mazi("قَضَى", "qada-judge", "«He decrees»", "«hükmettiğinde»", tags=["idha-shartiyya", ID, "naqis-verbs"], hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ؛ فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا"),
  maful_("أَمْرًا", "amr", "«a matter»", "«bir işe»"),
  tok("فَإِنَّمَا", "innama", "part", ["idha-shartiyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَإِنَّمَا كَافَّةٌ وَمَكْفُوفَةٌ: أَدَاةُ حَصْرٍ.", "«He only» — the fāʾ opens the answer; innamā restricts.", "«o yalnız» — fâ cevabı açar; innemâ hasr edatı.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّمَا", "innama", "part")]),
  mudari("يَقُولُ", "qala", "«says»", "«der»", tags=["hollow-verbs", "idha-shartiyya"], extra_ar=" — وَالْجُمْلَةُ جَوَابُ إِذَا"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to it»", "«ona»"),
  tok("كُنْ", "kana", "verb", [AM, KN, "hollow-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُذِفَتْ عَيْنُهُ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ (عَلَى التَّمَامِ) مُسْتَتِرٌ: أَنْتَ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "«Be!» — the imperative of kāna: the hollow wāw drops before the sukūn.", "«Ol!» — kâne'nin emri; ecvef vâv iki sâkin yüzünden düştü."),
  tok("فَيَكُونُ", "kana", "verb", [AT, "mudari-marfu", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَيَكُونُ فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ: هُوَ — قُرِئَ بِالرَّفْعِ هُنَا.", "«and it is» — a complete kāna in rafʿ here.", "«o da oluverir» — tam kâne, burada merfû.", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")], punct=AYA),
  ]),
])

CAND = {
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend (Form IV, hollow)", "istemek (if'âl, ecvef)", 1),
 "qatl": G("qatl", "قَتْل", "ق ت ل", "noun", "killing", "öldürme", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "takhallus": G("takhallus", "تَخَلُّص", "خ ل ص", "noun", "getting rid (min: of) (the maṣdar of Form V)", "kurtulma (tefa''ul masdarı)", 2),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "hama-protect": G("hama-protect", "حَمَى", "ح م ي", "verb", "to protect (defective)", "korumak (nâkıs)", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "radda": G("radda", "رَدَّ", "ر د د", "verb", "to return, to turn back (doubled)", "geri çevirmek (muzâaf)", 1),
 "kayd": G("kayd", "كَيْد", "ك ي د", "noun", "a plot, scheming", "tuzak, hile", 2),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "rafaa": G("rafaa", "رَفَعَ", "ر ف ع", "verb", "to raise", "yükseltmek", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "karrama": G("karrama", "كَرَّمَ", "ك ر م", "verb", "to honour (Form II)", "ikram etmek, şereflendirmek (tef'îl)", 1),
 "qaraa": G("qaraa", "قَرَأَ", "ق ر أ", "verb", "to read, to recite", "okumak", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa, hikâye", 1, plural="قِصَص"),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "quran": G("quran", "الْقُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "malak": G("malak", "مَلَك", "م ل ك", "noun", "an angel", "melek", 1, plural="مَلَائِكَة"),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "bashshara": G("bashshara", "بَشَّرَ", "ب ش ر", "verb", "to give glad tidings (Form II)", "müjdelemek (tef'îl)", 1),
 "pron-2fs": G("pron-2fs", "كِ", None, "pron", "you / your (f. sg.)", "sen / seni / senin (müennes)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "kalima": G("kalima", "كَلِمَة", "ك ل م", "noun", "a word", "kelime", 1, plural="كَلِمَات"),
 "ism": G("ism", "اِسْم", "س م و", "noun", "a name", "isim", 1, plural="أَسْمَاء"),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "ibn": G("ibn", "ابْن", "ب ن ي", "noun", "a son", "oğul", 1, plural="أَبْنَاء"),
 "wajih": G("wajih", "وَجِيه", "و ج ه", "noun", "eminent, of high standing", "itibarlı, seçkin", 2),
 "dunya": G("dunya", "الدُّنْيَا", "د ن و", "noun", "this world", "dünya", 1),
 "akhira": G("akhira", "آخِرَة", "أ خ ر", "noun", "the Hereafter", "âhiret", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "muqarrab": G("muqarrab", "مُقَرَّب", "ق ر ب", "noun", "brought near (a passive participle of Form II)", "yakınlaştırılmış, mukarreb (tef'îl ism-i mef'ûlü)", 2),
 "kallama": G("kallama", "كَلَّمَ", "ك ل م", "verb", "to speak to (Form II)", "konuşmak, hitap etmek (tef'îl)", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "mahd-cradle": G("mahd-cradle", "مَهْد", "م ه د", "noun", "a cradle", "beşik", 1),
 "kahl": G("kahl", "كَهْل", "ك ه ل", "noun", "a man of mature age", "olgun yaştaki adam, yetişkin", 2),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous (an active participle)", "sâlih (ism-i fâil)", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "anna-istifham": G("anna-istifham", "أَنَّى", None, "pron", "how, whence (interrogative)", "nasıl, nereden (istifhâm)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child, a son", "çocuk, oğul", 1, plural="أَوْلَاد"),
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "massa": G("massa", "مَسَّ", "م س س", "verb", "to touch (doubled)", "dokunmak (muzâaf)", 1),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection before the speaker's yāʾ", "mütekellim yâ'sından önceki vikâye nûnu", 2),
 "bashar": G("bashar", "بَشَر", "ب ش ر", "noun", "a human being, mankind", "insan, beşer", 1),
 "kadhalika": G("kadhalika", "كَذَلِكَ", None, "part", "thus, likewise", "böylece, işte böyle", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will (hollow)", "dilemek (ecvef)", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ırsa", 1),
 "qada-judge": G("qada-judge", "قَضَى", "ق ض ي", "verb", "to decree, to judge (defective)", "hükmetmek, karar vermek (nâkıs)", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1, plural="أُمُور"),
 "innama": G("innama", "إِنَّمَا", None, "part", "only (inna + the restraining mā)", "ancak, yalnızca (inne + kâffe mâ)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "hama-protect", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "حَمَ", "حْم", "i", "اِحْم", "حِمَايَة", "حَامٍ (الْحَامِي)", "مَحْمِيّ", "حُمِيَ", "يُحْمَى", "حَمَاهُ يَحْمِيهِ: مَنَعَهُ وَدَفَعَ عَنْهُ — نَاقِصٌ يَائِيٌّ؛ لَمْ يَحْمِ."))
put_morph(mo, "karrama", _sg.derived(_sg.B2, _sg.W2, "ُ", "كَرَّم", "كَرِّم", "كَرِّم", "تَكْرِيم", "مُكَرِّم", "مُكَرَّم", "كُرِّمَ", "يُكَرَّمُ", "كَرَّمَهُ: عَظَّمَهُ وَشَرَّفَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch30 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 30 (print p. 47; ʿĪsā §12 opens): the plot to kill him foiled, God raises and honours him (s1); Āl ʿImrān 3:45 the angels' tidings and the Messiah's titles (s2), 3:46 speaking in the cradle and in maturity (s3), 3:47 «how shall I have a son» — «Be! and it is» (s4)."
ADD_TR = " Otuzuncu bölüm (baskı s. 47; Îsâ §12 açılır): öldürme tuzağı boşa çıkar, Allah onu yükseltir ve şereflendirir (s1); Âl-i İmrân 45 meleklerin müjdesi ve Mesîh'in unvanları (s2), 46 beşikte ve yetişkinlikte konuşması (s3), 47 «benim nasıl çocuğum olur» — «Ol! o da olur» (s4)."
write_out(30, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §12 + 3:45–47", GLOSS_ADD, notes=(), related=())
report(30, S, GLOSS_ADD, ())
