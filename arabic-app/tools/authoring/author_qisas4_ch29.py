# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 29: «قِصَّةُ عِيسَى» §10 (his call to the religion and his giving the lie to the Jews: the spirit and core of religion, the love of God, mercy and solace, pure tawḥīd) and §11 (the Jews set up war against him: slanders, abuse, his mother defamed, the rabble set on him, the roads blocked); print pp. 46–47.
python3 tools/authoring/author_qisas4_ch29.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: دَعْوَتُهُ إِلَى الدِّينِ، وَالْيَهُودُ يَنْصِبُونَ لَهُ الْحَرْبَ", "en": "The story of ʿĪsā: his call to the religion; the Jews set up war against him", "tr": "Îsâ'nın kıssası: dine daveti; Yahudiler ona savaş açar"}
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

# ---------------------------------------------------------------- §10 دَعْوَتُهُ إِلَى الدِّينِ وَتَكْذِيبُهُ الْيَهُودَ (print p. 46)
sen("s1", "And he gave the lie to the Jews in much of what they had imagined and gone to excess in, and they had forbidden what God made lawful and made lawful what God forbade,",
        "Yahudileri, hayal edip aşırıya gittikleri şeylerin çoğunda yalanladı; onlar Allah'ın helâl kıldığını haram, haram kıldığını helâl saymışlardı;", [
  mazi("وَكَذَّبَ", "kadhdhaba", "«and he gave the lie to»", "«ve yalanladı»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  maful_("الْيَهُودَ", "yahud", "«the Jews»", "«Yahudileri»"),
  fi(),
  majrur("كَثِيرٍ", "kathir", "«much»", "«çoğunda»"),
  tok("مِمَّا", "ma-mawsula", "pron", [HJ, MW], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ فِي مَا الْمَوْصُولَةِ، وَمَا فِي مَحَلِّ جَرٍّ.", "«of what» — min fused into the relative mā.", "«… şeylerin» — min, ism-i mevsûl mâ ile idgam edilmiş.", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  v_pl_pron("تَخَيَّلُوهُ", "takhayyala", "تَخَيَّلُو", "هُ", "pron-3ms", "«they had imagined»", "«hayal ettikleri»", tags=[MW, "form-v-verbs"]),
  mazi_wa_alif("وَغَلَوْا", "ghala", "«and gone to excess»", "«ve aşırıya gittikleri»", wa=True, tags=[AT, MW]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in it»", "«onda»", punct="،"),
  mazi_pl("وَحَرَّمُوا", "harrama", "«and they had forbidden»", "«ve haram saymışlardı»", tags=[AT, "form-ii-verbs"], wa=True),
  ma_mawsul_obj("«what»", "«… -ı»"),
  v_pron("أَحَلَّهُ", "ahalla", "أَحَلَّ", "هُ", "pron-3ms", "«God made lawful»", "«Allah'ın helâl kıldığı»", tags=[MW, "doubled-verbs", "form-iv-verbs"], hidden=None),
  allah_fail(punct="،"),
  mazi_pl("وَأَحَلُّوا", "ahalla", "«and made lawful»", "«ve helâl saymışlardı»", tags=[AT, "doubled-verbs", "form-iv-verbs"], wa=True),
  ma_mawsul_obj("«what»", "«… -ı»"),
  v_pron("حَرَّمَهُ", "harrama", "حَرَّمَ", "هُ", "pron-3ms", "«God forbade»", "«Allah'ın haram kıldığı»", tags=[MW, "form-ii-verbs"], hidden=None),
  allah_fail(punct="،"),
])
sen("s2", "calling them to the spirit of the religion and its core, its root and its reality, to a love of God that prevails over every love, to mercy toward humanity and respect for it, and to solace for the poor,",
        "onları dinin ruhuna ve özüne, aslına ve hakikatine, her sevgiye galip gelen bir Allah sevgisine, insanlığa merhamete ve ona saygıya, fakirlere yardıma çağırıyordu;", [
  tok("يَدْعُوهُمْ", "daa", "verb", [HL, MB, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ حَالٌ.", "«calling them» — a ḥāl clause; the pronoun is the object.", "«onları çağırarak» — hâl cümlesi; zamir mef'ûl.", segments=[seg("يَدْعُو", "daa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("رُوحِ", "ruh", "«the spirit [of]»", "«ruhuna»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الدِّينِ", "din", "«the religion»", "«dinin»"),
  pron_atf("وَلُبَابِهِ", "lubab", "لُبَابِ", "هِ", "pron-3ms", "«its core»", "«özüne»", punct="،"),
  pron_atf("وَأَصْلِهِ", "asl", "أَصْلِ", "هِ", "pron-3ms", "«its root»", "«aslına»"),
  pron_atf("وَحَقِيقَتِهِ", "haqiqa", "حَقِيقَتِ", "هِ", "pron-3ms", "«its reality»", "«hakikatine»", punct="،"),
  atf("وَالْحُبِّ", "hubb", "«love»", "«sevgiye»"),
  tok("لِلّٰهِ", "allah", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — مُتَعَلِّقٌ بِالْحُبِّ.", "«of God» — the lām with the name of God.", "«Allah'a» — lâm ile lafz-ı celâl.", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("حُبًّا", "hubb", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ لِلْمَصْدَرِ الْحُبِّ (مُبَيِّنٌ لِلنَّوْعِ بِصِفَتِهِ).", "«a love» — an absolute object of the preceding maṣdar; its clause specifies the kind.", "«bir sevgi» — önceki masdarın mef'ûl-i mutlakı; sıfatı nev'ini belirtir."),
  mudari("يَغْلِبُ", "ghalaba", "«that prevails»", "«galip gelen»", tags=["jumla-sifa"], extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِحُبًّا"),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("حُبٍّ", "hubb", "«love»", "«sevgiye»", punct="،"),
  atf("وَالرَّحْمَةِ", "rahma", "«mercy»", "«merhamete»"),
  prep("عَلَى", "ala", "«toward»", "«-e»"),
  majrur("الْإِنْسَانِيَّةِ", "insaniyya", "«humanity»", "«insanlığa»"),
  pron_atf("وَاحْتِرَامِهَا", "ihtiram", "احْتِرَامِ", "هَا", "pron-3fs", "«respect for it»", "«ona saygıya»", tags=["form-viii-verbs"], punct="،"),
  atf("وَالْمُوَاسَاةِ", "muwasat", "«solace»", "«yardıma»", tags=["form-iii-verbs"]),
  li_noun("لِلْفُقَرَاءِ", "faqir", "«for the poor»", "«fakirlere»", tags=[JT, MM], punct="،"),
])
sen("s3", "and calling them to pure tawḥīd and to the rejection of everything that had entered the prophets' religion of pagan customs and false creeds.",
        "ve onları hâlis tevhide, peygamberlerin dinine girmiş câhiliye âdetlerinin ve bâtıl akîdelerin tamamını reddetmeye çağırıyordu.", [
  tok("وَيَدْعُوهُمْ", "daa", "verb", [AT, HL, MB, "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَدْعُو فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", "«and calling them»", "«ve onları çağırarak»", segments=[seg("وَ", "wa", "conj"), seg("يَدْعُو", "daa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("التَّوْحِيدِ", "tawhid", "«tawḥīd»", "«tevhide»"),
  naat("الْخَالِصِ", "khalis", "«pure»", "«hâlis»", tags=["ism-fail"], punct="،"),
  atf("وَرَفْضِ", "rafd", "«the rejection [of]»", "«reddetmeye»", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  majrur("كُلِّ", "kull", "«all [of]»", "«tamamını»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("مَا", "ma-mawsula", "pron", [ID, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the relative as muḍāf ilayh.", "«… şeylerin» — muzâfun ileyh olan ism-i mevsûl."),
  mazi("دَخَلَ", "dakhala", "«had entered»", "«girmiş»", tags=[MW], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةٌ"),
  prep("عَلَى", "ala", "«upon»", "«-e»"),
  majrur("دِينِ", "din", "«the religion [of]»", "«dinine»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberlerin»", tags=[JT]),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ (بَيَانُ مَا)."),
  majrur("عَادَاتٍ", "ada", "«customs»", "«âdetler»", tags=[JM]),
  naat("جَاهِلِيَّةٍ", "jahili", "«pagan»", "«câhiliye»", tags=["ism-mansub"], punct="،"),
  atf("وَعَقَائِدَ", "aqida", "«creeds»", "«akîdeler»", tags=[JT, MM], sign="بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ مَمْنُوعَةٌ مِنَ الصَّرْفِ"),
  naat("بَاطِلَةٍ", "batil", "«false»", "«bâtıl»", tags=["ism-fail"], punct="."),
])
# ---------------------------------------------------------------- §11 الْيَهُودُ يَنْصِبُونَ لَهُ الْحَرْبَ (print p. 47)
sen("s4", "And all of that weighed heavily on the Jews, and they set up war against him.",
        "Bütün bunlar Yahudilere ağır geldi ve ona savaş açtılar.", [
  mazi("وَشَقَّ", "shaqqa", "«and weighed heavily»", "«ve ağır geldi»", tags=[AT, "doubled-verbs"], wa=True, hidden=None),
  fail("كُلُّ", "kull", "«all [of]»", "«bütün»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that»", "«bunlar»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilere»", punct="،"),
  mazi_pl("وَنَصَبُوا", "nasaba-set", "«and they set up»", "«ve açtılar»", tags=[AT], wa=True),
  li_pron("لَهُ", "هُ", "pron-3ms", "«against him»", "«ona»"),
  maful_("الْحَرْبَ", "harb", "«war»", "«savaş»", punct="."),
])
sen("s5", "They shot at him from a single bow, pelted him with accusations and missiles, and assailed him with foul abuse and obscene speech,",
        "Ona tek bir yaydan ok attılar, onu ithamlarla ve atılan iftiralarla taşladılar, çirkin sövgü ve edepsiz sözle ona saldırdılar;", [
  tok("وَرَمَوْهُ", "rama", "verb", [AT, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَمَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — كِنَايَةٌ عَنِ اتِّفَاقِهِمْ عَلَى عَدَاوَتِهِ.", "«and they shot at him» — a defective māḍī on the group's wāw; «from one bow» is a kināya for their united hostility.", "«ve ona ok attılar» — cemi vâvlı nâkıs mâzî; «tek yaydan» düşmanlıkta birleşmelerinden kinâye.", segments=[seg("وَ", "wa", "conj"), seg("رَمَوْ", "rama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("عَنْ", "an", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  majrur("قَوْسٍ", "qaws", "«a bow»", "«bir yaydan»"),
  naat("وَاحِدَةٍ", "wahid", "«single»", "«tek»", punct="،"),
  v_pl_pron("وَرَشَقُوهُ", "rashaqa", "رَشَقُو", "هُ", "pron-3ms", "«and pelted him»", "«ve onu taşladılar»", wa=True),
  bi_noun("بِالتُّهَمِ", "tuhma", "«with accusations»", "«ithamlarla»", tags=[JT]),
  atf("وَالْقَذَائِفِ", "qadhifa", "«missiles»", "«atılan iftiralarla»", tags=[JT], punct="،"),
  v_pl_pron("وَتَنَاوَلُوهُ", "tanawala", "تَنَاوَلُو", "هُ", "pron-3ms", "«and assailed him»", "«ve ona saldırdılar»", tags=["form-vi-verbs"], wa=True),
  bi_noun("بِالسَّبِّ", "sabb", "«with abuse»", "«sövgüyle»"),
  naat("الْقَبِيحِ", "qabih", "«foul»", "«çirkin»"),
  atf("وَالْقَوْلِ", "qawl", "«speech»", "«sözle»"),
  naat("الْبَذِيءِ", "badhi", "«obscene»", "«edepsiz»", punct="،"),
])
sen("s6", "and they assailed his mother, Maryam the Virgin, with slander and defamation; they thwarted him and hounded him, set the rabble on him, and blocked the roads in his face.",
        "annesi Bâkire Meryem'e iftira ve dil uzatmayla saldırdılar; ona karşı durdular, onu kovaladılar, ayaktakımını ona saldırttılar ve yollarını kapattılar.", [
  mazi_pl("وَتَنَاوَلُوا", "tanawala", "«and they assailed»", "«ve saldırdılar»", tags=[AT, "form-vi-verbs"], wa=True),
  noun_pron("أُمَّهُ", "umm", "أُمَّ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his mother» — the object.", "«annesine» — mef'ûl.", tags=[MB, ID]),
  tok("مَرْيَمَ", "maryam", "propn", [BD, MM], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Maryam» — a badal; a diptote name.", "«Meryem» — bedel; gayr-i munsarıf isim."),
  naat("الْبَتُولَ", "batul", "«the Virgin»", "«Bâkire»", case="nasb"),
  bi_noun("بِالْقَذْفِ", "qadhf", "«with slander»", "«iftirayla»"),
  atf("وَالطَّعْنِ", "tan", "«defamation»", "«dil uzatmayla»", punct="،"),
  v_pl_pron("وَعَاكَسُوهُ", "akasa", "عَاكَسُو", "هُ", "pron-3ms", "«and they thwarted him»", "«ve ona karşı durdular»", tags=["form-iii-verbs"], wa=True),
  v_pl_pron("وَطَارَدُوهُ", "tarada", "طَارَدُو", "هُ", "pron-3ms", "«and hounded him»", "«ve onu kovaladılar»", tags=["form-iii-verbs"], wa=True, punct="،"),
  tok("وَأَمَالُوا", "amala-tilt", "verb", [AT, "hollow-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَمَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ — أَجْوَفُ مِنْ بَابِ الْإِفْعَالِ. [الْمَطْبُوعُ: «وَأَمَالَجُوا» — تَصْحِيفٌ؛ قُرِئَ: أَمَالُوا، وَأُعْلِنَ ذٰلِكَ.]", "«and they set … on» — a hollow Form IV; the print has a garbled «amālajū», read as amālū and declared.", "«ve … saldırttılar» — ecvef if'âl; baskıda bozuk «emâlecû», emâlû diye okundu ve bildirildi.", segments=wa_("أَمَالُوا", "amala-tilt", "verb")),
  li_pron("لَهُ", "هُ", "pron-3ms", "«on him»", "«ona»"),
  maful_("الْأَوْبَاشَ", "awbash", "«the rabble»", "«ayaktakımını»", tags=[JT], punct="،"),
  mazi_pl("وَسَدُّوا", "sadda-block", "«and they blocked»", "«ve kapattılar»", tags=[AT, "doubled-verbs"], wa=True),
  fi(),
  noun_pron("وَجْهِهِ", "wajh", "وَجْهِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his face»", "«yüzüne»", tags=[HJ, ID]),
  maful_("الطُّرُقَ", "tariq", "«the roads»", "«yolları»", tags=[JT], punct="."),
])

CAND = {
 "kadhdhaba": G("kadhdhaba", "كَذَّبَ", "ك ذ ب", "verb", "to call a liar, to give the lie to (Form II)", "yalanlamak (tef'îl)", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "takhayyala": G("takhayyala", "تَخَيَّلَ", "خ ي ل", "verb", "to imagine (Form V)", "hayal etmek (tefa''ul)", 2),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "ghala": G("ghala", "غَلَا", "غ ل و", "verb", "to go to excess (fī: in) (defective)", "aşırıya gitmek (nâkıs)", 2),
 "harrama": G("harrama", "حَرَّمَ", "ح ر م", "verb", "to forbid, to make unlawful (Form II)", "haram kılmak (tef'îl)", 1),
 "ahalla": G("ahalla", "أَحَلَّ", "ح ل ل", "verb", "to make lawful (Form IV, doubled)", "helâl kılmak (if'âl, muzâaf)", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call, to summon; to pray", "çağırmak; dua etmek", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "ruh": G("ruh", "رُوح", "ر و ح", "noun", "spirit, soul", "ruh", 1, plural="أَرْوَاح"),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "lubab": G("lubab", "لُبَاب", "ل ب ب", "noun", "the core, the kernel", "öz, lübâb", 3),
 "asl": G("asl", "أَصْل", "أ ص ل", "noun", "origin, root", "asıl, kök", 1, plural="أُصُول"),
 "haqiqa": G("haqiqa", "حَقِيقَة", "ح ق ق", "noun", "reality, truth", "hakikat", 1),
 "hubb": G("hubb", "حُبّ", "ح ب ب", "noun", "love", "sevgi", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "ghalaba": G("ghalaba", "غَلَبَ", "غ ل ب", "verb", "to prevail over", "galip gelmek", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, over", "üzerine", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet, merhamet", 1),
 "insaniyya": G("insaniyya", "إِنْسَانِيَّة", "أ ن س", "noun", "humanity (an abstract nisba)", "insanlık (masdar-ı sınâî)", 2),
 "ihtiram": G("ihtiram", "اِحْتِرَام", "ح ر م", "noun", "respect (the maṣdar of Form VIII)", "saygı, ihtiram (iftiâl masdarı)", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "muwasat": G("muwasat", "مُوَاسَاة", "أ س و", "noun", "solace, mutual aid (the maṣdar of wāsā; the spelling with wāw beside مُؤَاسَاة)", "yardımlaşma, teselli (vâsâ'nın masdarı; مُؤَاسَاة yanında vâv'lı imlâ)", 3),
 "faqir": G("faqir", "فَقِير", "ف ق ر", "noun", "poor", "fakir", 1, plural="فُقَرَاء"),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "tawhid": G("tawhid", "تَوْحِيد", "و ح د", "noun", "tawḥīd, the affirming of God's oneness", "tevhid", 1),
 "khalis": G("khalis", "خَالِص", "خ ل ص", "noun", "pure, sincere (an active participle)", "hâlis, katıksız (ism-i fâil)", 1),
 "rafd": G("rafd", "رَفْض", "ر ف ض", "noun", "rejection", "reddetme", 2),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "a custom", "âdet", 1, plural="عَادَات"),
 "jahili": G("jahili", "جَاهِلِيّ", "ج ه ل", "noun", "of the Jāhiliyya, pagan (a nisba)", "câhiliye devrine ait (nisbet)", 2),
 "aqida": G("aqida", "عَقِيدَة", "ع ق د", "noun", "a creed", "akîde", 1, plural="عَقَائِد"),
 "batil": G("batil", "بَاطِل", "ب ط ل", "noun", "false, vain (an active participle)", "bâtıl (ism-i fâil)", 1),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to split; (ʿalā) to weigh heavily on (doubled)", "yarmak; (alâ ile) ağır gelmek (muzâaf)", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "nasaba-set": G("nasaba-set", "نَصَبَ", "ن ص ب", "verb", "to set up, to erect; (al-ḥarb) to wage war", "dikmek, kurmak; (savaş) açmak", 2),
 "harb": G("harb", "حَرْب", "ح ر ب", "noun", "war (feminine)", "savaş, harp (müennes)", 1, plural="حُرُوب"),
 "rama": G("rama", "رَمَى", "ر م ي", "verb", "to throw, to shoot (defective)", "atmak, ok atmak (nâkıs)", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "qaws": G("qaws", "قَوْس", "ق و س", "noun", "a bow (feminine)", "yay (müennes)", 2, plural="قِسِيّ"),
 "wahid": G("wahid", "وَاحِد", "و ح د", "noun", "one, single", "bir, tek", 1),
 "rashaqa": G("rashaqa", "رَشَقَ", "ر ش ق", "verb", "to pelt, to shoot at (bi: with)", "taşlamak, (bi ile) atmak", 3),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "tuhma": G("tuhma", "تُهْمَة", "و ه م", "noun", "an accusation, a suspicion", "itham, töhmet", 2, plural="تُهَم"),
 "qadhifa": G("qadhifa", "قَذِيفَة", "ق ذ ف", "noun", "a missile; a hurled slander", "atılan şey, mermi; iftira", 3, plural="قَذَائِف"),
 "tanawala": G("tanawala", "تَنَاوَلَ", "ن و ل", "verb", "to take; (bi) to assail with (Form VI)", "almak; (bi ile) dil uzatmak, saldırmak (tefâul)", 2),
 "sabb": G("sabb", "سَبّ", "س ب ب", "noun", "abuse, reviling", "sövme", 2),
 "qabih": G("qabih", "قَبِيح", "ق ب ح", "noun", "ugly, foul", "çirkin", 1),
 "qawl": G("qawl", "قَوْل", "ق و ل", "noun", "a saying, speech", "söz", 1, plural="أَقْوَال"),
 "badhi": G("badhi", "بَذِيء", "ب ذ أ", "noun", "obscene, foul-mouthed", "edepsiz, ağzı bozuk", 3),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "batul": G("batul", "بَتُول", "ب ت ل", "noun", "virgin, devoted to God (an epithet of Maryam)", "bâkire, Betûl (Meryem'in lakabı)", 2),
 "qadhf": G("qadhf", "قَذْف", "ق ذ ف", "noun", "slander, a charge of unchastity", "iftira, kazf", 2),
 "tan": G("tan", "طَعْن", "ط ع ن", "noun", "stabbing; attack, defamation", "saldırı, ta'n; karalama", 2),
 "akasa": G("akasa", "عَاكَسَ", "ع ك س", "verb", "to oppose, to thwart (Form III)", "karşı durmak, köstek olmak (müfâale)", 3),
 "tarada": G("tarada", "طَارَدَ", "ط ر د", "verb", "to hound, to chase (Form III)", "kovalamak, peşine düşmek (müfâale)", 2),
 "amala-tilt": G("amala-tilt", "أَمَالَ", "م ي ل", "verb", "to incline, to turn (someone against) (Form IV, hollow)", "meylettirmek, (birine karşı) yöneltmek (if'âl, ecvef)", 2),
 "awbash": G("awbash", "أَوْبَاش", "و ب ش", "noun", "the rabble, the riff-raff (a plural)", "ayaktakımı (çoğul)", 3),
 "sadda-block": G("sadda-block", "سَدَّ", "س د د", "verb", "to block, to close up (doubled)", "kapatmak, tıkamak (muzâaf)", 1),
 "wajh": G("wajh", "وَجْه", "و ج ه", "noun", "a face", "yüz", 1, plural="وُجُوه"),
 "tariq": G("tariq", "طَرِيق", "ط ر ق", "noun", "a road, a way", "yol", 1, plural="طُرُق"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "takhayyala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَخَيَّل", "تَخَيَّل", "تَخَيَّل", "تَخَيُّل", "مُتَخَيِّل", "مُتَخَيَّل", "تُخُيِّلَ", "يُتَخَيَّلُ", "تَخَيَّلَ الشَّيْءَ: تَصَوَّرَهُ وَتَوَهَّمَهُ."))
put_morph(mo, "rashaqa", _sg.sound1("nasara", "رَشَق", "رْشُق", "اُرْشُق", "رَشْق", "رَاشِق", "مَرْشُوق", "رُشِقَ", "يُرْشَقُ", "رَشَقَهُ بِالسِّهَامِ يَرْشُقُهُ: رَمَاهُ بِهَا."))
put_morph(mo, "akasa", _sg.derived(_sg.B3, _sg.W3, "ُ", "عَاكَس", "عَاكِس", "عَاكِس", "مُعَاكَسَة", "مُعَاكِس", "مُعَاكَس", "عُوكِسَ", "يُعَاكَسُ", "عَاكَسَهُ: خَالَفَهُ وَوَقَفَ فِي طَرِيقِهِ."))
put_morph(mo, "tarada", _sg.derived(_sg.B3, _sg.W3, "ُ", "طَارَد", "طَارِد", "طَارِد", "مُطَارَدَة", "مُطَارِد", "مُطَارَد", "طُورِدَ", "يُطَارَدُ", "طَارَدَهُ: تَبِعَهُ لِيُدْرِكَهُ وَيُؤْذِيَهُ."))
put_morph(mo, "amala-tilt", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَمَال", "أَمَل", "مِيل", "مِل", "أَمِل", "أَمِل", "إِمَالَة", "مُمِيل", "مُمَال", "أُمِيلَ", "يُمَالُ", "أَمَالَ الشَّيْءَ: صَرَفَهُ وَعَطَفَهُ؛ وَأَمَالَ عَلَيْهِ الْقَوْمَ: حَرَّضَهُمْ عَلَيْهِ — أَجْوَفُ يَائِيٌّ."))
put_morph(mo, "sadda-block", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "سَدّ", "سَادّ", _sg.mazi14("سَدّ", "سَدَد"), _sg.mudari14("َ", "سُدّ", "سْدُد"), ["سُدَّ", "سُدَّا", "سُدُّوا", "سُدِّي", "سُدَّا", "اُسْدُدْنَ"], "يَسُدَّ", "يَسُدَّ", "تَسُدَّ", "مَسْدُود", "سُدَّ", "يُسَدُّ", "سَدَّ الطَّرِيقَ يَسُدُّهُ: أَغْلَقَهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسُدَّ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch29 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 29 (print pp. 46–47; ʿĪsā §10–11): giving the lie to the Jews' imaginings; the call to the spirit and core of religion, the love of God, mercy and solace, pure tawḥīd (s1–s3); the Jews set up war: one bow, accusations, foul abuse, his mother defamed, the rabble set on him, the roads blocked (s4–s6)."
ADD_TR = " Yirmi dokuzuncu bölüm (baskı s. 46–47; Îsâ §10–11): Yahudilerin hayallerinin yalanlanması; dinin ruhuna ve özüne, Allah sevgisine, merhamet ve yardıma, hâlis tevhide davet (s1–s3); Yahudiler savaş açar: tek yay, ithamlar, çirkin sövgü, annesine iftira, üstüne salınan ayaktakımı, kapatılan yollar (s4–s6)."
write_out(29, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §10–11", GLOSS_ADD, notes=(), related=())
report(29, S, GLOSS_ADD, ())
