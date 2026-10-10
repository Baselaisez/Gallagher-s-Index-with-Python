# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 39: «قِصَّةُ عِيسَى» §27 (our master the Messiah in court: Friday before sunset, the Sabbath, the sentence of death by crucifixion), §28 (the criminal law of the age: the condemned carries his cross; the foreign police cannot tell Israelites apart; the rabble press on him), §29 (ʿĪsā bears the harm: exhausted, the cross heavy); print pp. 56–58.
python3 tools/authoring/author_qisas4_ch39.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: سَيِّدُنَا الْمَسِيحُ فِي الْمَحْكَمَةِ", "en": "The story of ʿĪsā: our master the Messiah in court", "tr": "Îsâ'nın kıssası: efendimiz Mesîh mahkemede"}
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

# ---------------------------------------------------------------- §27 سَيِّدُنَا الْمَسِيحُ فِي الْمَحْكَمَةِ (print pp. 56–57)
sen("s1", "That was on Friday after the afternoon, on the eve of the Sabbath; the Jews did no work on the Sabbath, for it was a day of rest and abstention from work;",
        "Bu, cuma günü ikindiden sonra, cumartesi gecesiydi; Yahudiler cumartesi günü hiçbir iş yapmazlardı; o, tatil ve işten el çekme günüydü;", [
  wa_kana(),
  tok("ذٰلِكَ", "dhalika", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«that» — kāna's ism.", "«bu» — kâne'nin ismi."),
  zarf("يَوْمَ", "yawm", "«on the day [of]»", "«günü»", kind="زَمَانٍ"),
  mudaf_ilayh("الْجُمُعَةِ", "juma", "«Friday»", "«cuma»"),
  zarf("بَعْدَ", "bad-after", "«after»", "«-den sonra»", kind="زَمَانٍ"),
  mudaf_ilayh("الْعَصْرِ", "asr", "«the afternoon»", "«ikindi»"),
  tok("لَيْلَةَ", "layla", "noun", [MF, ID, BD], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ — بَدَلٌ مِنْ يَوْمَ (لَيْلَةُ السَّبْتِ: الَّتِي تَلِي الْجُمُعَةَ).", "«the eve [of]» — a badal of «the day»: the night that follows Friday.", "«… gecesi» — «gün»den bedel: cumayı izleyen gece."),
  mudaf_ilayh("السَّبْتِ", "sabt", "«the Sabbath»", "«cumartesi»", punct="،"),
  wa_kana(),
  ism_kana("الْيَهُودُ", "yahud", "«the Jews»", "«Yahudiler»"),
  la_nafiya(),
  khamsa("يَعْمَلُونَ", "amila", "«did work»", "«yaparlardı»", tags=[KN, "la-nafiya"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  maful_("شَيْئًا", "shay", "«anything»", "«hiçbir şey»"),
  zarf("يَوْمَ", "yawm", "«on the day [of]»", "«günü»", kind="زَمَانٍ"),
  mudaf_ilayh("السَّبْتِ", "sabt", "«the Sabbath»", "«cumartesi»", punct="،"),
  wa_kana("، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (يَوْمُ السَّبْتِ)"),
  khabar_kana("يَوْمَ", "yawm", "«a day [of]»", "«günü»", tags=[ID], ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("عُطْلَةٍ", "utla", "«rest, holiday»", "«tatil»"),
  atf("وَكَفٍّ", "kaff", "«abstention»", "«ve el çekme»", tags=["doubled-verbs"]),
  tok("عَنِ", "an", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  majrur("الْعَمَلِ", "amal-work", "«work»", "«işten»", punct="،"),
])
sen("s2", "so they were utterly keen that the sentence be issued before the sun of Friday set, and that they be relieved of the Messiah's affair, sleep with quiet minds and wake with easy minds, nothing disturbing them.",
        "bu yüzden hükmün cuma güneşi batmadan verilmesine, Mesîh işinden kurtulup zihinleri rahat uyumaya ve gönülleri huzurlu uyanmaya, hiçbir şeyin kendilerini rahatsız etmemesine son derece hırslıydılar.", [
  tok("فَكَانُوا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَكَانُوا فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«so they were»", "«bu yüzden … idiler»", segments=[seg("فَ", "fa", "conj"), seg("كَانُوا", "kana", "verb")]),
  tok("حَرِيصِينَ", "haris", "noun", [KN, JS], "خَبَرُ كَانُوا مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«keen» — kāna's khabar.", "«hırslı» — kâne'nin haberi."),
  tok("كُلَّ", "kull", "noun", ["maful-mutlaq", ID], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ، مُضَافٌ إِلَى الْمَصْدَرِ (كُلَّ الْحِرْصِ: حِرْصًا تَامًّا).", "«utterly» — kull annexed to the maṣdar stands in for the absolute object.", "«son derece» — masdara muzâf «kül», mef'ûl-i mutlakın nâibi."),
  mudaf_ilayh("الْحِرْصِ", "hirs", "«keenness»", "«hırs»"),
  prep("عَلَى", "ala", "«that»", "«-e»"),
  an_nasb("فِي مَحَلِّ جَرٍّ بِعَلَى", "«that»", "«-mesine»"),
  tok("يَصْدُرَ", "sadara", "verb", [AN], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«be issued»", "«verilmesine»"),
  fail("الْحُكْمُ", "hukm", "«the sentence»", "«hüküm»"),
  zarf("قَبْلَ", "qabla", "«before»", "«-den önce»", kind="زَمَانٍ"),
  majrur("غُرُوبِ", "ghurub", "«the setting [of]»", "«batması»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  majrur("شَمْسِ", "shams", "«the sun [of]»", "«güneşinin»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  majrur("يَوْمِ", "yawm", "«the day [of]»", "«gününün»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْجُمُعَةِ", "juma", "«Friday»", "«cuma»", punct="،"),
  tok("وَيَسْتَرِيحُوا", "istaraha", "verb", [AT, AN, AK, "hollow-verbs", "form-x-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَسْتَرِيحُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَصْدُرَ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and be relieved» — naṣb by conjunction, the nūn dropped.", "«ve kurtulmalarına» — atıfla mansub, nûn düşmüş.", segments=wa_("يَسْتَرِيحُوا", "istaraha", "verb")),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("أَمْرِ", "amr", "«the affair [of]»", "«işinden»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْمَسِيحِ", "masih", "«the Messiah»", "«Mesîh'in»", punct="،"),
  tok("فَيَنَامُوا", "nama", "verb", [AT, AN, AK, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَنَامُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and sleep»", "«ve uyumalarına»", segments=[seg("فَ", "fa", "conj"), seg("يَنَامُوا", "nama", "verb")]),
  js_khabar("هَادِئِي", "hadi-calm", "هَادِئِ", "«quiet [of]»", "«rahat»", " — إِضَافَةٌ لَفْظِيَّةٌ", tags=[HL, "ism-fail"], role="حَالٌ"),
  mudaf_ilayh("الْبَالِ", "bal-mind", "«mind»", "«zihinli»", punct="،"),
  tok("وَيُصْبِحُوا", "asbaha", "verb", [AT, AN, AK, KN, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُصْبِحُوا فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِالْعَطْفِ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ اسْمُهُ.", "«and wake» — aṣbaḥa in naṣb.", "«ve uyanmalarına» — mansub asbaha.", segments=wa_("يُصْبِحُوا", "asbaha", "verb")),
  js_khabar("نَاعِمِي", "naim-soft", "نَاعِمِ", "«easy [of]»", "«huzurlu»", " — إِضَافَةٌ لَفْظِيَّةٌ", tags=["ism-fail"], role="خَبَرُ يُصْبِحُوا"),
  mudaf_ilayh("الْبَالِ", "bal-mind", "«mind»", "«gönüllü»", punct="،"),
  la_nafiya(),
  v_pron("يُزْعِجُهُمْ", "azaja", "يُزْعِجُ", "هُمْ", "pron-3mp", "«disturbing them»", "«onları rahatsız eder»", tags=["la-nafiya", HL, "mudari-marfu", "form-iv-verbs"], hidden=None),
  fail("شَيْءٌ", "shay", "«anything»", "«hiçbir şey»", punct="."),
])
sen("s3", "The governor was weary of the case; he had no wish in it, nor had his nation any interest in it; and the Jews had crowded in to hear the sentence, some shouting and some calling out, some mocking and some scoffing,",
        "Vali davadan bunalmıştı; onda ne kendisinin bir isteği ne de milletinin bir menfaati vardı; Yahudiler hükmü dinlemek için toplanmıştı; kimi bağırıyor, kimi sesleniyor, kimi alay ediyor, kimi hicvediyordu;", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi("ضَاقَ", "daqa", "«was weary»", "«bunaldı»", tags=["hollow-verbs"], hidden=None),
  fail("الْحَاكِمُ", "hakim-ruler", "«the governor»", "«vali»", tags=["ism-fail"]),
  bi_noun("بِالْقَضِيَّةِ", "qadiyya", "«of the case»", "«davadan»"),
  tok("ذَرْعًا", "dhar", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — ضَاقَ بِهِ ذَرْعًا: عَجَزَ عَنِ احْتِمَالِهِ (الذَّرْعُ: بَسْطُ الْيَدِ).", "«[in] capacity» — a tamyīz; the idiom «his arm-span grew narrow with it»: he could not bear it.", "«takatçe» — temyiz; «ondan daraldı» deyimi: tahammül edemedi.", punct="،"),
  tok("وَلَيْسَتْ", "laysa", "verb", [AT, KN], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَتْ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … was not» — laysa.", "«ve … yoktu» — leyse.", segments=wa_("لَيْسَتْ", "laysa", "verb")),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him» — laysa's fronted khabar.", "«onun» — leyse'nin öne alınmış haberi.", tags=[KN], extra=" — خَبَرُ لَيْسَ مُقَدَّمٌ"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it»", "«onda»"),
  tok("رَغْبَةٌ", "raghba", "noun", [KN], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a wish» — laysa's delayed ism.", "«bir istek» — leyse'nin sonraya kalan ismi."),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«nor» — lā repeating the negation.", "«ne de» — nefyi te'kid eden lâ.", segments=wa_("لَا", "la-nafiya", "part")),
  tok("لِأُمَّتِهِ", "umma", "noun", [HJ, ID, AT], "اللَّامُ حَرْفُ جَرٍّ، وَأُمَّتِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَعْطُوفٌ عَلَى لَهُ.", "«for his nation» — joined to «for him».", "«milletinin» — «onun»a ma'tûf.", segments=[seg("لِ", "li", "prep"), seg("أُمَّتِ", "umma", "noun"), seg("هِ", "pron-3ms", "pron")]),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it»", "«onda»"),
  tok("مَصْلَحَةٌ", "maslaha", "noun", [AT, KN], "مَعْطُوفٌ عَلَى رَغْبَةٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«an interest» — joined to «a wish».", "«bir menfaat» — «istek»e ma'tûf.", punct="،"),
  tok("وَقَدِ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and [indeed]» — qad takes a kasra before the waṣl.", "«ve [gerçekten]» — kad vasl öncesi kesre aldı.", segments=wa_("قَدِ", "qad", "part")),
  mazi("احْتَشَدَ", "ihtashada", "«had crowded in»", "«toplanmıştı»", tags=["form-viii-verbs"], hidden=None),
  fail("الْيَهُودُ", "yahud", "«the Jews»", "«Yahudiler»"),
  tok("لِسَمَاعِ", "samaa", "noun", [HJ, ID, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَسَمَاعِ مَجْرُورٌ، مُضَافٌ.", "«to hear»", "«dinlemek için»", segments=[seg("لِ", "li", "prep"), seg("سَمَاعِ", "samaa", "noun")]),
  mudaf_ilayh("الْحُكْمِ", "hukm", "«the sentence»", "«hükmü»", punct="،"),
  tok("وَهُمْ", "hum", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«while they» — a ḥāl clause.", "«onlar … iken» — hâl cümlesi.", segments=wa_("هُمْ", "hum", "pron")),
  zarf("بَيْنَ", "bayna", "«between»", "«arasında»"),
  mudaf_ilayh("صَائِحٍ", "saih", "«one shouting»", "«bağıran»", tags=["ism-fail", "hollow-verbs"], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبَيْنَ وَمَا بَعْدَهَا خَبَرُ الْمُبْتَدَأِ."),
  atf("وَهَاتِفٍ", "hatif", "«one calling out»", "«ve seslenen»", tags=["ism-fail"], punct="،"),
  atf("وَمُتَنَدِّرٍ", "mutanaddir", "«one mocking»", "«ve alay eden»", tags=["ism-fail", "form-v-verbs"]),
  atf("وَمُتَهَكِّمٍ", "mutahakkim", "«one scoffing»", "«ve hicveden»", tags=["ism-fail", "form-v-verbs"], punct="،"),
])
sen("s4", "and the governor was vexed, the time short, and the sun had already inclined toward setting; so he issued the sentence against him of death by crucifixion.",
        "vali sıkıntıdaydı, vakit dardı, güneş batmaya yönelmişti; bunun üzerine onun hakkında çarmıha gerilerek öldürülmesi hükmünü verdi.", [
  tok("وَالْحَاكِمُ", "hakim-ruler", "noun", [HL, MK, "ism-fail"], "الْوَاوُ لِلْحَالِ، وَالْحَاكِمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the governor» — a ḥāl clause's mubtadaʾ.", "«ve vali» — hâl cümlesinin mübtedâsı.", segments=wa_("الْحَاكِمُ", "hakim-ruler", "noun")),
  tok("مُتَضَايِقٌ", "mutadayiq", "noun", [MK, "ism-fail", "form-vi-verbs"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«vexed» — the khabar.", "«sıkıntıda» — haber.", punct="،"),
  tok("وَالْوَقْتُ", "waqt", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْوَقْتُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the time»", "«ve vakit»", segments=wa_("الْوَقْتُ", "waqt", "noun")),
  tok("قَصِيرٌ", "qasir", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«short»", "«dar»", punct="،"),
  tok("وَالشَّمْسُ", "shams", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالشَّمْسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sun»", "«ve güneş»", segments=wa_("الشَّمْسُ", "shams", "noun")),
  tok("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«already»", "«artık»"),
  mazi_ta("مَالَتْ", "mala", "«had inclined»", "«yönelmişti»", tags=[MK, "hollow-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  li_noun("لِلْغُرُوبِ", "ghurub", "«toward setting»", "«batmaya»", punct="،"),
  tok("فَأَصْدَرَ", "asdara", "verb", [AT, "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَأَصْدَرَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«so he issued»", "«bunun üzerine verdi»", segments=[seg("فَ", "fa", "conj"), seg("أَصْدَرَ", "asdara", "verb")]),
  maful_("الْحُكْمَ", "hukm", "«the sentence»", "«hükmü»"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«against him»", "«onun hakkında»"),
  bi_noun("بِالْقَتْلِ", "qatl", "«of death»", "«öldürülme»"),
  tok("صَلْبًا", "salb-crucifixion", "noun", [HL], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (مَصْدَرٌ فِي مَوْضِعِ الْحَالِ: مَصْلُوبًا)، أَوْ مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ.", "«by crucifixion» — a maṣdar as ḥāl, or an absolute object of kind.", "«çarmıha gerilerek» — hâl yerinde masdar, veya nev' bildiren mef'ûl-i mutlak.", punct="."),
])
# ---------------------------------------------------------------- §28 الْقَانُونُ الْجِنَائِيُّ فِي ذٰلِكَ الْعَصْرِ (print pp. 57–58)
sen("s5", "The criminal law of that age required that the one condemned to hanging carry his cross on which he would be crucified; and the gallows was far off, as is the custom in civilized countries;",
        "O çağın ceza kanunu, asılmaya mahkûm edilenin üzerine gerileceği çarmıhı kendisinin taşımasını gerektirirdi; darağacı, medenî ülkelerdeki âdet üzere uzaktaydı;", [
  wa_kana(),
  ism_kana("الْقَانُونُ", "qanun", "«the law»", "«kanun»"),
  naat("الْجِنَائِيُّ", "jinai", "«criminal»", "«ceza»", case="raf", tags=["ism-mansub"]),
  fi(),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«o»"),
  tok("الْعَصْرِ", "asr", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«age» — a badal.", "«çağın» — bedel."),
  mudari("يُوجِبُ", "awjaba", "«required»", "«gerektirirdi»", tags=[KN, "form-iv-verbs", "mithal-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  an_nasb("مَفْعُولٌ بِهِ لِيُوجِبُ", "«that»", "«-masını»"),
  tok("يَحْمِلَ", "hamala", "verb", [AN], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«carry»", "«taşımasını»"),
  tok("الْمَحْكُومُ", "mahkum", "noun", [FL, "ism-maful"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولٍ مِنْ حَكَمَ عَلَيْهِ، وَنَائِبُ فَاعِلِهِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«the condemned» — the doer; a participle whose own deputy doer is the phrase «against him».", "«mahkûm edilen» — fâil; nâib-i fâili sonraki «aleyhi» ibaresi olan ism-i mef'ûl."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«[sentenced] against him»", "«aleyhine»"),
  bi_noun("بِالشَّنْقِ", "shanq", "«to hanging»", "«asılmaya»", punct="،"),
  noun_pron("صَلِيبَهُ", "salib", "صَلِيبَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his cross» — the object of «carry».", "«çarmıhını» — «taşı»nın mef'ûlü.", tags=[MB, ID]),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ.", "«on which» — the relative, a naʿt.", "«ki» — sıfat olan mevsûl."),
  tok("يُصْلَبُ", "salaba-crucify", "verb", [MW, NF, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«he would be crucified» — a passive; the ṣila.", "«gerilecek» — meçhul; sıla."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on it»", "«üzerine»", punct="،"),
  wa_kana(),
  ism_kana("الْمَشْنَقُ", "mashnaq", "«the gallows»", "«darağacı»"),
  khabar_kana("بَعِيدًا", "baid", "«far off»", "«uzakta»"),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا مَصْدَرِيَّةٌ (أَوْ كَافَّةٌ).", "«as» — the kāf with the maṣdarī mā.", "«… gibi» — kâf ile masdariyye mâ."),
  tok("هِيَ", "hiya", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ (ضَمِيرُ الشَّأْنِ أَوْ ضَمِيرُ الْعَادَةِ).", "«it» — the mubtadaʾ.", "«o» — mübtedâ."),
  tok("الْعَادَةُ", "ada", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the custom» — the khabar.", "«âdet» — haber."),
  fi(),
  majrur("الْبِلَادِ", "bilad", "«the countries»", "«ülkelerde»", tags=[JT]),
  naat("الْمُتَمَدِّنَةِ", "mutamaddin", "«civilized»", "«medenî»", tags=["ism-fail", "form-v-verbs"], punct="،"),
])
sen("s6", "and the crowd was dense, people tumbling over one another; and the policemen — most of them foreigners — were men under orders, mere officials, with no wish of their own in this case,",
        "kalabalık yoğundu, insanlar birbirinin üstüne yığılıyordu; polisler — çoğu yabancıydı — emir altında memurlardı, bu davada kendi istekleri yoktu;", [
  wa_kana(),
  ism_kana("الْجَمْعُ", "jam", "«the crowd»", "«kalabalık»"),
  khabar_kana("حَاشِدًا", "hashid", "«dense»", "«yoğun»", tags=["ism-fail"]),
  mudari("يَتَسَاقَطُ", "tasaqata", "«tumbling»", "«yığılıyordu»", tags=[HL, "form-vi-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ حَالٌ؛ وَفَاعِلُهُ بَعْضُ بَعْدَهُ"),
  noun_pron("بَعْضُهُ", "bad", "بَعْضُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«some of it» — the doer.", "«bir kısmı» — fâil.", tags=[FL, ID]),
  prep("عَلَى", "ala", "«over»", "«üstüne»"),
  majrur("بَعْضٍ", "bad", "«others»", "«bir kısmının»", punct="،"),
  wa_kana(),
  ism_kana("رِجَالُ", "rajul", "«the men [of]»", "«adamları»", tags=[ID, JT], ar="اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ."),
  mudaf_ilayh("الشُّرْطَةِ", "shurta", "«the police»", "«polis»"),
  noun_pron("وَأَكْثَرُهُمْ", "akthar", "وَأَكْثَرُ", "هُمْ", "pron-3mp", "الْوَاوُ اعْتِرَاضِيَّةٌ، وَأَكْثَرُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«most of them» — the mubtadaʾ of a parenthesis.", "«çoğu» — itirâzî cümlenin mübtedâsı.", tags=[MK, ID, "jumla-mutarida", "ism-tafdil"]),
  tok("مِنَ", "min", "prep", [HJ, MK], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the phrase is the khabar.", "«-den» — ibare haber."),
  majrur("الْأَجَانِبِ", "ajnabi", "«the foreigners»", "«yabancılar»", tags=[JT], punct="،"),
  tok("مَأْمُورِينَ", "mamur", "noun", [KN, JS, "ism-maful"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«men under orders» — kāna's khabar.", "«emir altındaki memurlar» — kâne'nin haberi."),
  tok("مُوَظَّفِينَ", "muwazzaf", "noun", [KN, JS, "ism-maful", "form-ii-verbs"], "خَبَرٌ ثَانٍ (أَوْ نَعْتٌ) مَنْصُوبٌ بِالْيَاءِ.", "«officials» — a second khabar.", "«görevliler» — ikinci haber."),
  la_jins("لَا"),
  tok("رَغْبَةَ", "raghba", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — وَالْجُمْلَةُ نَعْتٌ (أَوْ حَالٌ).", "«[no] wish» — lā's ism; the clause describes them.", "«istek [yok]» — lâ'nın ismi; cümle sıfat."),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«of their own» — lā's khabar.", "«kendilerinin» — lâ'nın haberi.", tags=["la-nafiya-lil-jins"], extra=" — خَبَرُ لَا"),
  fi(),
  tok("هٰذِهِ", "hadhihi", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("الْقَضِيَّةِ", "qadiyya", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«case»", "«davada»", punct="،"),
])
sen("s7", "and to them the Israelites were all alike; their affairs were confused in their eyes, so they could not tell one from another — as foreigners are in the eyes of foreigners;",
        "İsrâilliler onların gözünde birbirine benzerdi; işleri onlara karışık gelirdi, aralarında ayırt edemezlerdi — yabancıların yabancı gözündeki durumu gibi;", [
  wa_kana(),
  tok("الْإِسْرَائِيلِيُّونَ", "israili", "noun", [KN, JS, "ism-mansub"], "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the Israelites» — kāna's ism.", "«İsrâilliler» — kâne'nin ismi."),
  khabar_kana("أَشْبَاهًا", "shabah", "«alike»", "«birbirine benzer»", tags=[JT]),
  noun_pron("عِنْدَهُمْ", "inda", "عِنْدَ", "هُمْ", "pron-3mp", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«to them»", "«onların gözünde»", tags=[MF, ID]),
  mudari("يَلْتَبِسُ", "iltabasa", "«were confused»", "«karışık gelirdi»", tags=["jumla-sifa", "form-viii-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِأَشْبَاهًا؛ وَفَاعِلُهُ أَمْرُ بَعْدَهُ"),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«to them»", "«onlara»"),
  noun_pron("أَمْرُهُمْ", "amr", "أَمْرُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their affair» — the doer.", "«işleri» — fâil.", tags=[FL, ID], punct="،"),
  tok("فَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَلَا نَافِيَةٌ.", "«so … not»", "«bu yüzden … -mez»", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  khamsa("يُمَيِّزُونَ", "mayyaza", "«they could tell apart»", "«ayırt ederlerdi»", tags=["la-nafiya", "form-ii-verbs"]),
  noun_pron("بَيْنَهُمْ", "bayna", "بَيْنَ", "هُمْ", "pron-3mp", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«between them»", "«aralarında»", tags=[MF, ID], punct="،"),
  tok("شَأْنَ", "shan", "noun", ["maful-mutlaq", ID], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ، مُضَافٌ (أَيْ: الْتِبَاسًا كَشَأْنِ الْأَجَانِبِ).", "«as is the way [of]» — stands in for an absolute object: «a confusion like the case of foreigners».", "«… durumu gibi» — mef'ûl-i mutlakın nâibi."),
  mudaf_ilayh("الْأَجَانِبِ", "ajnabi", "«foreigners»", "«yabancıların»", tags=[JT]),
  fi(),
  majrur("نَظَرِ", "nazar", "«the eyes [of]»", "«gözünde»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْأَجَانِبِ", "ajnabi", "«foreigners»", "«yabancıların»", tags=[JT], punct="،"),
])
sen("s8", "and it was evening, darkness having spread its canopy; and some of the Jews and the foolish hotheads among the youth kept pouring down upon the Lord Messiah, jostling against him, reviling him and taunting him, wanting to hurt and humiliate him.",
        "akşam olmuş, karanlık perdesini germişti; Yahudilerden bazıları ve gençlerden sefih, coşkulu olanlar Efendi Mesîh'in üzerine çullanıyor, ona doğru itişiyor, ona sövüyor, onu ayıplıyor, ona eziyet ve hakaret etmek istiyorlardı.", [
  wa_kana(),
  ism_kana("الْوَقْتُ", "waqt", "«the time»", "«vakit»"),
  khabar_kana("مَسَاءً", "masa", "«evening»", "«akşam»"),
  tok("قَدْ", "qad", "part", [HL, "qad-harf"], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ حَالٌ.", "«[already]» — the clause is a ḥāl.", "«[artık]» — cümle hâl."),
  mazi("مَدَّ", "madda", "«had spread»", "«germişti»", tags=[HL, "doubled-verbs"], hidden=None),
  fail("الظَّلَامُ", "zalam", "«darkness»", "«karanlık»"),
  noun_pron("رُوَاقَهُ", "riwaq", "رُوَاقَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْتِعَارَةٌ: الظَّلَامُ خَيْمَةٌ.", "«its canopy» — the object; darkness as a tent.", "«perdesini» — mef'ûl; karanlık bir çadır gibi.", tags=[MB, ID], punct="،"),
  wa_kana(),
  ism_kana("بَعْضُ", "bad", "«some [of]»", "«bazıları»", tags=[ID], ar="اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ."),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»"),
  atf("وَالْمُتَحَمِّسِينَ", "mutahammis", "«the hotheads»", "«ve coşkulu olanlar»", tags=[JS, "ism-fail", "form-v-verbs"], sign="بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ"),
  naat("السُّفَهَاءِ", "safih", "«foolish»", "«sefih»", tags=[JT, MM]),
  tok("مِنَ", "min", "prep", [HJ, HL], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ.", "«among»", "«-den»"),
  majrur("الشَّبَابِ", "shabab", "«the youth»", "«gençler»"),
  khamsa("يَنْهَالُونَ", "inhala", "«kept pouring down»", "«çullanıyorlardı»", tags=[KN, "hollow-verbs", "form-vii-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ؛ انْهَالَ عَلَيْهِ: انْصَبَّ وَتَتَابَعَ"),
  prep("عَلَى", "ala", "«upon»", "«üzerine»"),
  majrur("السَّيِّدِ", "sayyid", "«the Lord»", "«Efendi»"),
  tok("الْمَسِيحِ", "masih", "propn", [BD], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ.", "«Messiah»", "«Mesîh'in»", punct="،"),
  khamsa_wa("وَيَتَدَافَعُونَ", "tadafaa", "«and jostling»", "«ve itişiyorlardı»", tags=["form-vi-verbs"]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«against him»", "«ona doğru»", punct="،"),
  tok("يَسُبُّونَهُ", "sabba-revile", "verb", [HL, AK, MB, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ حَالٌ.", "«reviling him» — a ḥāl clause; the hāʾ the object.", "«ona söverek» — hâl cümlesi; hâ mef'ûl.", segments=[seg("يَسُبُّونَ", "sabba-revile", "verb"), seg("هُ", "pron-3ms", "pron")], punct="،"),
  tok("وَيُعَيِّرُونَهُ", "ayyara", "verb", [AT, AK, MB, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُعَيِّرُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and taunting him»", "«ve onu ayıplayarak»", segments=[seg("وَ", "wa", "conj"), seg("يُعَيِّرُونَ", "ayyara", "verb"), seg("هُ", "pron-3ms", "pron")], punct="،"),
  khamsa_wa("وَيُرِيدُونَ", "arada", "«and wanting»", "«ve istiyorlardı»", tags=["hollow-verbs", "form-iv-verbs"]),
  noun_pron("إِيذَاءَهُ", "idha-harm", "إِيذَاءَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ آذَى.", "«to hurt him» — the object; the maṣdar of ādhā.", "«ona eziyet etmeyi» — mef'ûl; âzâ'nın masdarı.", tags=[MB, ID, "form-iv-verbs"]),
  pron_atf("وَإِهَانَتَهُ", "ihana", "إِهَانَتَ", "هُ", "pron-3ms", "«to humiliate him»", "«ve ona hakaret etmeyi»", case="nasb", tags=["form-iv-verbs"], punct="."),
])
# ---------------------------------------------------------------- §29 عِيسَى يَتَحَمَّلُ الْأَذَى (print p. 58)
sen("s9", "And the Lord Messiah was worn out: the strain, the long standing in court and the bearing of harm had exhausted him; the cross was heavy, and he had been charged with carrying it, so he could not hurry his walk.",
        "Efendi Mesîh bitkindi; çaba, mahkemede uzun süre ayakta kalmak ve eziyete katlanmak onu tüketmişti; çarmıh ağırdı ve onu taşımakla yükümlü kılınmıştı; bu yüzden yürüyüşünü hızlandıramıyordu.", [
  wa_kana(),
  ism_kana("السَّيِّدُ", "sayyid", "«the Lord»", "«Efendi»"),
  tok("الْمَسِيحُ", "masih", "propn", [BD], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«Messiah»", "«Mesîh»"),
  khabar_kana("لَاغِبًا", "laghib", "«worn out»", "«bitkin»", tags=["ism-fail"], punct="،"),
  tok("قَدْ", "qad", "part", [HL, "qad-harf"], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ حَالٌ (أَوْ خَبَرٌ ثَانٍ).", "«[indeed]» — the clause is a ḥāl.", "«[gerçekten]» — cümle hâl."),
  tok("أَضْنَاهُ", "adna", "verb", [HL, MB, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ — أَضْنَاهُ: أَنْهَكَهُ.", "«had exhausted him» — a defective Form IV; the hāʾ the object before the doer.", "«onu tüketmişti» — nâkıs if'âl; hâ fâilden önce gelen mef'ûl.", segments=[seg("أَضْنَا", "adna", "verb"), seg("هُ", "pron-3ms", "pron")]),
  fail("الْجُهْدُ", "juhd-effort", "«the strain»", "«çaba»", punct="،"),
  atf("وَطُولُ", "tul", "«the length [of]»", "«ve uzunluğu»", "raf", tags=[ID], sign="بِالضَّمَّةِ، مُضَافٌ"),
  mudaf_ilayh("الْوُقُوفِ", "wuquf", "«standing»", "«ayakta kalmanın»"),
  fi(),
  majrur("الْمَحْكَمَةِ", "mahkama", "«the court»", "«mahkemede»", punct="،"),
  atf("وَتَحَمُّلُ", "tahammul", "«the bearing [of]»", "«ve katlanmak»", "raf", tags=[ID, "form-v-verbs"], sign="بِالضَّمَّةِ، مُضَافٌ"),
  tok("الْأَذَى", "adha", "noun", [ID, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«harm» — a maqṣūr.", "«eziyete» — maksûr.", punct="،"),
  wa_kana(),
  ism_kana("الصَّلِيبُ", "salib", "«the cross»", "«çarmıh»"),
  khabar_kana("ثَقِيلًا", "thaqil", "«heavy»", "«ağır»", punct="،"),
  tok("وَقَدْ", "qad", "part", [HL, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  tok("كُلِّفَ", "kallafa", "verb", [HL, NF, MX, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (الْمَفْعُولُ الْأَوَّلُ فِي الْأَصْلِ).", "«he had been charged» — a passive of a two-object verb.", "«yükümlü kılınmıştı» — iki mef'ûllü fiilin meçhulü."),
  noun_pron("حَمْلَهُ", "haml", "حَمْلَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with carrying it» — the second object.", "«onu taşımakla» — ikinci mef'ûl.", tags=[MX, ID], punct="،"),
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«so he was»", "«bu yüzden … idi»", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  la_nafiya(),
  neg_mudari("يَسْتَطِيعُ", "istataa", "«able»", "«gücü yetiyor»", tags=[KN, "hollow-verbs", "form-x-verbs"], hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  an_nasb("مَفْعُولٌ بِهِ لِيَسْتَطِيعُ", "«to»", "«-maya»"),
  mansub("يُسْرِعَ", "asraa", "«hurry»", "«hızlandırmaya»", tags=["form-iv-verbs"]),
  fi(),
  majrur("الْمَشْيِ", "mashy", "«walking»", "«yürüyüşünü»", punct="."),
])

CAND = {
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "juma": G("juma", "جُمُعَة", "ج م ع", "noun", "Friday", "cuma", 1),
 "bad-after": G("bad-after", "بَعْدَ", "ب ع د", "noun", "after", "-den sonra", 1),
 "asr": G("asr", "عَصْر", "ع ص ر", "noun", "an age, an era; the afternoon", "çağ, asır; ikindi", 1),
 "layla": G("layla", "لَيْلَة", "ل ي ل", "noun", "a night", "gece", 1, plural="لَيَالٍ"),
 "sabt": G("sabt", "سَبْت", "س ب ت", "noun", "Saturday, the Sabbath", "cumartesi, sebt", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to do, to work", "yapmak, çalışmak", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "utla": G("utla", "عُطْلَة", "ع ط ل", "noun", "a holiday, a day of rest", "tatil", 1),
 "kaff": G("kaff", "كَفّ", "ك ف ف", "noun", "abstention, holding back; the palm", "el çekme; avuç", 2),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "amal-work": G("amal-work", "عَمَل", "ع م ل", "noun", "work, a deed", "iş, amel", 1, plural="أَعْمَال"),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "haris": G("haris", "حَرِيص", "ح ر ص", "noun", "keen, eager (ʿalā: for)", "hırslı, istekli", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "hirs": G("hirs", "حِرْص", "ح ر ص", "noun", "keenness, eagerness", "hırs, istek", 2),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "sadara": G("sadara", "صَدَرَ", "ص د ر", "verb", "to be issued, to come forth", "sâdır olmak, çıkmak", 1),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "a ruling, a sentence; rule", "hüküm; yönetim", 1, plural="أَحْكَام"),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "-den önce", 1),
 "ghurub": G("ghurub", "غُرُوب", "غ ر ب", "noun", "setting (of the sun)", "batış, gurûb", 1),
 "shams": G("shams", "شَمْس", "ش م س", "noun", "the sun", "güneş", 1),
 "istaraha": G("istaraha", "اِسْتَرَاحَ", "ر و ح", "verb", "to rest, to be relieved (Form X, hollow)", "dinlenmek, rahatlamak (istif'âl, ecvef)", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1, plural="أُمُور"),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "nama": G("nama", "نَامَ", "ن و م", "verb", "to sleep (hollow)", "uyumak (ecvef)", 1),
 "hadi-calm": G("hadi-calm", "هَادِئ", "ه د أ", "noun", "calm, quiet (an active participle)", "sakin (ism-i fâil)", 1),
 "bal-mind": G("bal-mind", "بَال", "ب و ل", "noun", "the mind, the state of mind", "zihin, gönül, hâl", 2),
 "asbaha": G("asbaha", "أَصْبَحَ", "ص ب ح", "verb", "to become; to wake in the morning (a sister of kāna, Form IV)", "olmak; sabahlamak (kâne'nin kardeşi, if'âl)", 1),
 "naim-soft": G("naim-soft", "نَاعِم", "ن ع م", "noun", "soft, easy (an active participle)", "yumuşak, rahat (ism-i fâil)", 1),
 "azaja": G("azaja", "أَزْعَجَ", "ز ع ج", "verb", "to disturb (Form IV)", "rahatsız etmek (if'âl)", 2),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "daqa": G("daqa", "ضَاقَ", "ض ي ق", "verb", "to be narrow; (bihi dharʿan) to be unable to bear (hollow)", "daralmak; (bihi zer'an) tahammül edememek (ecvef)", 2),
 "hakim-ruler": G("hakim-ruler", "حَاكِم", "ح ك م", "noun", "a ruler, a governor (an active participle)", "yöneten, vali, hâkim (ism-i fâil)", 1, plural="حُكَّام"),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "qadiyya": G("qadiyya", "قَضِيَّة", "ق ض ي", "noun", "a case, an issue", "dava, mesele", 1, plural="قَضَايَا"),
 "dhar": G("dhar", "ذَرْع", "ذ ر ع", "noun", "an arm-span, capacity (in ḍāqa bihi dharʿan)", "kulaç, takat (dâka bihi zer'an deyiminde)", 3),
 "laysa": G("laysa", "لَيْسَ", "ل ي س", "verb", "is not (a frozen verb)", "değildir (câmid fiil)", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "raghba": G("raghba", "رَغْبَة", "ر غ ب", "noun", "a wish, a desire", "istek, arzu", 1),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "maslaha": G("maslaha", "مَصْلَحَة", "ص ل ح", "noun", "an interest, a benefit", "menfaat, maslahat", 1, plural="مَصَالِح"),
 "ihtashada": G("ihtashada", "اِحْتَشَدَ", "ح ش د", "verb", "to crowd together, to gather (Form VIII)", "toplanmak, yığılmak (iftiâl)", 2),
 "samaa": G("samaa", "سَمَاع", "س م ع", "noun", "hearing, listening", "dinleme, işitme", 1),
 "hum": G("hum", "هُمْ", None, "pron", "they", "onlar", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "saih": G("saih", "صَائِح", "ص ي ح", "noun", "one shouting (an active participle)", "bağıran (ism-i fâil)", 2),
 "hatif": G("hatif", "هَاتِف", "ه ت ف", "noun", "one calling out (an active participle)", "seslenen (ism-i fâil)", 2),
 "mutanaddir": G("mutanaddir", "مُتَنَدِّر", "ن د ر", "noun", "one mocking, jesting (an active participle of Form V)", "alay eden (tefa''ul ism-i fâili)", 3),
 "mutahakkim": G("mutahakkim", "مُتَهَكِّم", "ه ك م", "noun", "one scoffing (an active participle of Form V)", "hicveden, alaycı (tefa''ul ism-i fâili)", 3),
 "mutadayiq": G("mutadayiq", "مُتَضَايِق", "ض ي ق", "noun", "vexed, annoyed (an active participle of Form VI)", "sıkıntılı, bunalmış (tefâul ism-i fâili)", 2),
 "waqt": G("waqt", "وَقْت", "و ق ت", "noun", "time", "vakit", 1, plural="أَوْقَات"),
 "qasir": G("qasir", "قَصِير", "ق ص ر", "noun", "short", "kısa", 1),
 "mala": G("mala", "مَالَ", "م ي ل", "verb", "to incline (hollow)", "meyletmek, yönelmek (ecvef)", 1),
 "asdara": G("asdara", "أَصْدَرَ", "ص د ر", "verb", "to issue (Form IV)", "çıkarmak, (hüküm) vermek (if'âl)", 1),
 "qatl": G("qatl", "قَتْل", "ق ت ل", "noun", "killing", "öldürme", 1),
 "salb-crucifixion": G("salb-crucifixion", "صَلْب", "ص ل ب", "noun", "crucifixion", "çarmıha germe", 2),
 "qanun": G("qanun", "قَانُون", "ق ن ن", "noun", "a law", "kanun", 1, plural="قَوَانِين"),
 "jinai": G("jinai", "جِنَائِيّ", "ج ن ي", "noun", "criminal, penal (a nisba)", "cezaî, cinâî (nisbet)", 2),
 "awjaba": G("awjaba", "أَوْجَبَ", "و ج ب", "verb", "to make obligatory, to require (Form IV)", "gerektirmek, vâcip kılmak (if'âl)", 1),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry", "taşımak", 1),
 "mahkum": G("mahkum", "مَحْكُوم", "ح ك م", "noun", "ruled; condemned (a passive participle)", "yönetilen; mahkûm (ism-i mef'ûl)", 2),
 "shanq": G("shanq", "شَنْق", "ش ن ق", "noun", "hanging (the execution)", "asma, idam", 2),
 "salib": G("salib", "صَلِيب", "ص ل ب", "noun", "a cross", "çarmıh, haç", 1, plural="صُلْبَان"),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which (m.)", "ki o, -an", 1),
 "salaba-crucify": G("salaba-crucify", "صَلَبَ", "ص ل ب", "verb", "to crucify", "çarmıha germek", 2),
 "mashnaq": G("mashnaq", "مَشْنَق", "ش ن ق", "noun", "a gallows, a place of execution", "darağacı", 3),
 "baid": G("baid", "بَعِيد", "ب ع د", "noun", "far, distant", "uzak", 1),
 "kama": G("kama", "كَمَا", None, "part", "as, just as", "… gibi", 1),
 "hiya": G("hiya", "هِيَ", None, "pron", "she / it (f.)", "o (müennes)", 1),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "a custom", "âdet", 1, plural="عَادَات"),
 "bilad": G("bilad", "بِلَاد", "ب ل د", "noun", "countries, lands", "ülkeler, beldeler", 1),
 "mutamaddin": G("mutamaddin", "مُتَمَدِّن", "م د ن", "noun", "civilized (an active participle of Form V)", "medenî (tefa''ul ism-i fâili)", 2),
 "jam": G("jam", "جَمْع", "ج م ع", "noun", "a crowd; gathering; a plural", "kalabalık; toplama; çoğul", 1),
 "hashid": G("hashid", "حَاشِد", "ح ش د", "noun", "dense, crowded (an active participle)", "yoğun, kalabalık (ism-i fâil)", 2),
 "tasaqata": G("tasaqata", "تَسَاقَطَ", "س ق ط", "verb", "to tumble one upon another (Form VI)", "üst üste yığılmak, dökülmek (tefâul)", 2),
 "bad": G("bad", "بَعْض", "ب ع ض", "noun", "some, a part", "bazı, bir kısım", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1, plural="رِجَال"),
 "shurta": G("shurta", "شُرْطَة", "ش ر ط", "noun", "the police", "polis, zabıta", 1),
 "akthar": G("akthar", "أَكْثَر", "ك ث ر", "noun", "more, most (an elative)", "daha çok (ism-i tafdîl)", 1),
 "ajnabi": G("ajnabi", "أَجْنَبِيّ", "ج ن ب", "noun", "foreign, a foreigner", "yabancı", 1, plural="أَجَانِب"),
 "mamur": G("mamur", "مَأْمُور", "أ م ر", "noun", "one under orders, an official (a passive participle)", "emir altındaki, memur (ism-i mef'ûl)", 2),
 "muwazzaf": G("muwazzaf", "مُوَظَّف", "و ظ ف", "noun", "an official, an employee (a passive participle of Form II)", "memur, görevli (tef'îl ism-i mef'ûlü)", 2),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu (müennes)", 1),
 "israili": G("israili", "إِسْرَائِيلِيّ", None, "noun", "Israelite (a nisba)", "İsrâilî (nisbet)", 2, plural="إِسْرَائِيلِيُّونَ"),
 "shabah": G("shabah", "شَبَه", "ش ب ه", "noun", "a likeness; (pl. ashbāh) look-alikes", "benzer; (ç. eşbâh) birbirine benzeyenler", 2, plural="أَشْبَاه"),
 "inda": G("inda", "عِنْدَ", None, "noun", "with, at, in the presence of", "yanında, katında", 1),
 "iltabasa": G("iltabasa", "اِلْتَبَسَ", "ل ب س", "verb", "to be confused, obscure (ʿalā: to) (Form VIII)", "karışık gelmek, belirsiz olmak (iftiâl)", 2),
 "mayyaza": G("mayyaza", "مَيَّزَ", "م ي ز", "verb", "to distinguish (bayna: between) (Form II)", "ayırt etmek (tef'îl)", 1),
 "shan": G("shan", "شَأْن", "ش أ ن", "noun", "an affair, a state; (shaʾna) as is the case of", "iş, durum; (şe'ne) … durumunda olduğu gibi", 1, plural="شُؤُون"),
 "nazar": G("nazar", "نَظَر", "ن ظ ر", "noun", "sight, a view; (fī naẓar) in the eyes of", "bakış, görüş; (fî nazar) gözünde", 1),
 "masa": G("masa", "مَسَاء", "م س و", "noun", "evening", "akşam", 1),
 "madda": G("madda", "مَدَّ", "م د د", "verb", "to stretch, to spread (doubled)", "uzatmak, germek (muzâaf)", 1),
 "zalam": G("zalam", "ظَلَام", "ظ ل م", "noun", "darkness", "karanlık", 1),
 "riwaq": G("riwaq", "رُوَاق", "ر و ق", "noun", "a canopy, a portico; the front of a tent", "çadır örtüsü, revak, perde", 3),
 "mutahammis": G("mutahammis", "مُتَحَمِّس", "ح م س", "noun", "a hothead, an enthusiast (an active participle of Form V)", "coşkulu, heyecanlı (tefa''ul ism-i fâili)", 2),
 "safih": G("safih", "سَفِيه", "س ف ه", "noun", "foolish, a fool", "sefih, akılsız", 1, plural="سُفَهَاء"),
 "shabab": G("shabab", "شَبَاب", "ش ب ب", "noun", "youth; the young", "gençlik; gençler", 1),
 "inhala": G("inhala", "اِنْهَالَ", "ه ي ل", "verb", "to pour down (ʿalā: upon) (Form VII, hollow)", "üşüşmek, çullanmak (infiâl, ecvef)", 3),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "tadafaa": G("tadafaa", "تَدَافَعَ", "د ف ع", "verb", "to jostle one another (Form VI)", "itişmek (tefâul)", 2),
 "sabba-revile": G("sabba-revile", "سَبَّ", "س ب ب", "verb", "to revile, to abuse (doubled)", "sövmek (muzâaf)", 1),
 "ayyara": G("ayyara", "عَيَّرَ", "ع ي ر", "verb", "to taunt, to reproach (Form II)", "ayıplamak, kınamak (tef'îl)", 2),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend (Form IV, hollow)", "istemek (if'âl, ecvef)", 1),
 "idha-harm": G("idha-harm", "إِيذَاء", "أ ذ ي", "noun", "hurting, harming (the maṣdar of Form IV)", "eziyet etme (if'âl masdarı)", 2),
 "ihana": G("ihana", "إِهَانَة", "ه و ن", "noun", "humiliation, an insult (the maṣdar of Form IV)", "hakaret, aşağılama (if'âl masdarı)", 1),
 "laghib": G("laghib", "لَاغِب", "ل غ ب", "noun", "worn out, exhausted (an active participle)", "bitkin, yorgun (ism-i fâil)", 3),
 "adna": G("adna", "أَضْنَى", "ض ن ي", "verb", "to exhaust, to wear out (Form IV, defective)", "tüketmek, bitkin düşürmek (if'âl, nâkıs)", 3),
 "juhd-effort": G("juhd-effort", "جُهْد", "ج ه د", "noun", "effort, strain", "çaba, güç harcama", 1),
 "tul": G("tul", "طُول", "ط و ل", "noun", "length", "uzunluk", 1),
 "wuquf": G("wuquf", "وُقُوف", "و ق ف", "noun", "standing, halting", "durma, ayakta kalma", 2),
 "mahkama": G("mahkama", "مَحْكَمَة", "ح ك م", "noun", "a court of law", "mahkeme", 1, plural="مَحَاكِم"),
 "tahammul": G("tahammul", "تَحَمُّل", "ح م ل", "noun", "bearing, enduring (the maṣdar of Form V)", "katlanma, tahammül (tefa''ul masdarı)", 1),
 "adha": G("adha", "أَذًى", "أ ذ ي", "noun", "harm, injury (a maqṣūr noun)", "eziyet, ezâ (maksûr isim)", 1),
 "thaqil": G("thaqil", "ثَقِيل", "ث ق ل", "noun", "heavy", "ağır", 1),
 "kallafa": G("kallafa", "كَلَّفَ", "ك ل ف", "verb", "to charge, to lay upon (two objects) (Form II)", "yükümlü kılmak (iki mef'ûl) (tef'îl)", 1),
 "haml": G("haml", "حَمْل", "ح م ل", "noun", "carrying", "taşıma", 1),
 "istataa": G("istataa", "اِسْتَطَاعَ", "ط و ع", "verb", "to be able (Form X, hollow)", "güç yetirmek, yapabilmek (istif'âl, ecvef)", 1),
 "asraa": G("asraa", "أَسْرَعَ", "س ر ع", "verb", "to hurry (Form IV)", "hızlanmak, acele etmek (if'âl)", 1),
 "mashy": G("mashy", "مَشْي", "م ش ي", "noun", "walking", "yürüme, yürüyüş", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "sadara", _sg.sound1("nasara", "صَدَر", "صْدُر", "اُصْدُر", "صُدُور", "صَادِر", None, None, None, "صَدَرَ الْحُكْمُ يَصْدُرُ: خَرَجَ وَظَهَرَ؛ وَصَدَرَ عَنِ الْمَكَانِ: رَجَعَ."))
put_morph(mo, "istaraha", _sg.derived_hollow(_sg.B10, _sg.W10, "َ", "اِسْتَرَاح", "اِسْتَرَح", "سْتَرِيح", "سْتَرِح", "اِسْتَرِح", "اِسْتَرِح", "اِسْتِرَاحَة", "مُسْتَرِيح", None, None, None, "اِسْتَرَاحَ مِنَ الْأَمْرِ: وَجَدَ الرَّاحَةَ وَخَلَصَ مِنْهُ — أَجْوَفُ وَاوِيٌّ (ر و ح)."))
put_morph(mo, "nama", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ، عَلَى فَعِلَ يَفْعَلُ: نَامَ يَنَامُ)", "نَام", "نِم", "نَام", "نَم", "نَم", "نَم", "نَوْم", "نَائِم", None, None, None, "نَامَ يَنَامُ: اسْتَغْرَقَ فِي النَّوْمِ — أَجْوَفُ وَاوِيٌّ مِنْ بَابِ فَعِلَ يَفْعَلُ: نِمْتُ، لَمْ يَنَمْ."))
put_morph(mo, "azaja", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَزْعَج", "زْعِج", "أَزْعِج", "إِزْعَاج", "مُزْعِج", "مُزْعَج", "أُزْعِجَ", "يُزْعَجُ", "أَزْعَجَهُ: أَقْلَقَهُ وَأَقْلَعَهُ مِنْ مَكَانِهِ."))
put_morph(mo, "ihtashada", _sg.derived(_sg.B8, _sg.W8, "َ", "اِحْتَشَد", "حْتَشِد", "اِحْتَشِد", "اِحْتِشَاد", "مُحْتَشِد", None, None, None, "اِحْتَشَدَ الْقَوْمُ: اجْتَمَعُوا وَتَجَمَّعُوا."))
put_morph(mo, "mala", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "مَال", "مِل", "مِيل", "مِل", "مِل", "مِل", "مَيْل", "مَائِل", None, None, None, "مَالَ إِلَى الشَّيْءِ يَمِيلُ: انْحَرَفَ إِلَيْهِ — أَجْوَفُ يَائِيٌّ؛ لَمْ يَمِلْ."))
put_morph(mo, "asdara", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَصْدَر", "صْدِر", "أَصْدِر", "إِصْدَار", "مُصْدِر", "مُصْدَر", "أُصْدِرَ", "يُصْدَرُ", "أَصْدَرَ الْحُكْمَ: أَخْرَجَهُ وَأَعْلَنَهُ."))
put_morph(mo, "awjaba", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَوْجَب", "وجِب", "أَوْجِب", "إِيجَاب", "مُوجِب", "مُوجَب", "أُوجِبَ", "يُوجَبُ", "أَوْجَبَ الشَّيْءَ: جَعَلَهُ وَاجِبًا لَازِمًا — مِثَالٌ وَاوِيٌّ: يُوجِبُ."))
put_morph(mo, "hamala", _sg.sound1("daraba", "حَمَل", "حْمِل", "اِحْمِل", "حَمْل", "حَامِل", "مَحْمُول", "حُمِلَ", "يُحْمَلُ", "حَمَلَ الشَّيْءَ يَحْمِلُهُ: رَفَعَهُ وَنَقَلَهُ."))
put_morph(mo, "salaba-crucify", _sg.sound1("daraba", "صَلَب", "صْلِب", "اِصْلِب", "صَلْب", "صَالِب", "مَصْلُوب", "صُلِبَ", "يُصْلَبُ", "صَلَبَهُ يَصْلِبُهُ: عَلَّقَهُ عَلَى الصَّلِيبِ."))
put_morph(mo, "tasaqata", _sg.derived(_sg.B6, _sg.W6, "َ", "تَسَاقَط", "تَسَاقَط", "تَسَاقَط", "تَسَاقُط", "مُتَسَاقِط", None, None, None, "تَسَاقَطَ الْقَوْمُ: سَقَطَ بَعْضُهُمْ عَلَى بَعْضٍ."))
put_morph(mo, "iltabasa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِلْتَبَس", "لْتَبِس", "اِلْتَبِس", "اِلْتِبَاس", "مُلْتَبِس", None, None, None, "اِلْتَبَسَ عَلَيْهِ الْأَمْرُ: اخْتَلَطَ وَأَشْكَلَ."))
put_morph(mo, "mayyaza", _sg.derived(_sg.B2, _sg.W2, "ُ", "مَيَّز", "مَيِّز", "مَيِّز", "تَمْيِيز", "مُمَيِّز", "مُمَيَّز", "مُيِّزَ", "يُمَيَّزُ", "مَيَّزَ الشَّيْءَ مِنْ غَيْرِهِ: فَرَّقَ بَيْنَهُمَا."))
put_morph(mo, "inhala", _sg.derived_hollow(_sg.B7, _sg.W7, "َ", "اِنْهَال", "اِنْهَل", "نْهَال", "نْهَل", "اِنْهَل", "اِنْهَل", "اِنْهِيَال", "مُنْهَال", None, None, None, "اِنْهَالَ عَلَيْهِ: انْصَبَّ وَتَتَابَعَ — أَجْوَفُ يَائِيٌّ (ه ي ل)."))
put_morph(mo, "tadafaa", _sg.derived(_sg.B6, _sg.W6, "َ", "تَدَافَع", "تَدَافَع", "تَدَافَع", "تَدَافُع", "مُتَدَافِع", None, None, None, "تَدَافَعَ الْقَوْمُ: دَفَعَ بَعْضُهُمْ بَعْضًا."))
put_morph(mo, "sabba-revile", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "سَبّ", "سَابّ", _sg.mazi14("سَبّ", "سَبَب"), _sg.mudari14("َ", "سُبّ", "سْبُب"), ["سُبَّ", "سُبَّا", "سُبُّوا", "سُبِّي", "سُبَّا", "اُسْبُبْنَ"], "يَسُبَّ", "يَسُبَّ", "تَسُبَّ", "مَسْبُوب", "سُبَّ", "يُسَبُّ", "سَبَّهُ يَسُبُّهُ: شَتَمَهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسُبَّ."))
put_morph(mo, "ayyara", _sg.derived(_sg.B2, _sg.W2, "ُ", "عَيَّر", "عَيِّر", "عَيِّر", "تَعْيِير", "مُعَيِّر", "مُعَيَّر", "عُيِّرَ", "يُعَيَّرُ", "عَيَّرَهُ بِكَذَا: عَابَهُ بِهِ وَنَسَبَهُ إِلَيْهِ."))
put_morph(mo, "adna", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَضْنَ", "ضْن", "i", "أَضْن", "إِضْنَاء", "مُضْنٍ (الْمُضْنِي)", "مُضْنًى", "أُضْنِيَ", "يُضْنَى", "أَضْنَاهُ الْمَرَضُ: أَنْهَكَهُ وَأَثْقَلَهُ — نَاقِصٌ: يُضْنِي، لَمْ يُضْنِ."))
put_morph(mo, "asraa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْرَع", "سْرِع", "أَسْرِع", "إِسْرَاع", "مُسْرِع", None, None, None, "أَسْرَعَ فِي الْمَشْيِ: عَجِلَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch39 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 39 (print pp. 56–58; ʿĪsā §27–29): in court — Friday before sunset, the Sabbath, the Jews keen for a quick sentence, the weary governor, the crowd shouting and mocking, death by crucifixion (s1–s4); the criminal law — the condemned carries his cross, the gallows far, the foreign police, the Israelites all alike to them, darkness and the rabble (s5–s8); the Messiah worn out, the cross heavy (s9)."
ADD_TR = " Otuz dokuzuncu bölüm (baskı s. 56–58; Îsâ §27–29): mahkemede — cuma güneş batmadan, sebt, hızlı hüküm için hırslı Yahudiler, bunalmış vali, bağıran ve alay eden kalabalık, çarmıhla ölüm (s1–s4); ceza kanunu — mahkûm çarmıhını taşır, darağacı uzakta, yabancı polis, onlara birbirine benzeyen İsrâilliler, karanlık ve ayaktakımı (s5–s8); bitkin Mesîh, ağır çarmıh (s9)."
write_out(39, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §27–29", GLOSS_ADD, notes=(), related=())
report(39, S, GLOSS_ADD, ())
