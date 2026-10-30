# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 28: «قِصَّةُ عِيسَى» §9 — the Messiah's miracles: prophethood, revelation, the Injīl, the Holy Spirit; healing the sick, the blind and the leper, raising the dead, the clay bird, telling what is eaten and stored; the trust in the Torah's reports restored, the worship of sense and experiment refuted; the deniers decree «nothing new, nothing more»; print pp. 45–46.
python3 tools/authoring/author_qisas4_ch28.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: مُعْجِزَاتُ الْمَسِيحِ", "en": "The story of ʿĪsā: the miracles of the Messiah", "tr": "Îsâ'nın kıssası: Mesîh'in mucizeleri"}
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

# ---------------------------------------------------------------- §9 مُعْجِزَاتُ الْمَسِيحِ (print pp. 45–46)
sen("s1", "And God honoured him with prophethood and revelation, gave him the Injīl, and backed him with the Holy Spirit and dazzling miracles:",
        "Allah ona peygamberlik ve vahiyle ikram etti, ona İncil'i verdi, onu Rûhu'l-Kudüs ve göz kamaştırıcı mucizelerle destekledi:", [
  v_pron("وَأَكْرَمَهُ", "akrama", "أَكْرَمَ", "هُ", "pron-3ms", "«and honoured him»", "«ve ona ikram etti»", tags=["form-iv-verbs"], wa=True, hidden=None),
  allah_fail(),
  bi_noun("بِالنُّبُوَّةِ", "nubuwwa", "«with prophethood»", "«peygamberlikle»"),
  atf("وَالْوَحْيِ", "wahy", "«revelation»", "«vahiyle»", punct="،"),
  tok("وَآتَاهُ", "aata-bring", "verb", [AT, MX, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَآتَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ — يَنْصِبُ مَفْعُولَيْنِ.", "«and gave him» — ātā takes two objects; the hāʾ is the first.", "«ve ona verdi» — âtâ iki mef'ûl alır; hâ ilk mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("آتَا", "aata-bring", "verb"), seg("هُ", "pron-3ms", "pron")]),
  maful_("الْإِنْجِيلَ", "injil", "«the Injīl»", "«İncil'i»", tags=[MX], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", punct="،"),
  v_pron("وَأَيَّدَهُ", "ayyada", "أَيَّدَ", "هُ", "pron-3ms", "«and backed him»", "«ve onu destekledi»", tags=["form-ii-verbs"], wa=True),
  bi_noun("بِرُوحِ", "ruh", "«with the Spirit [of]»", "«Rûh'uyla»", tags=[ID], extra="، مُضَافٌ"),
  mudaf_ilayh("الْقُدُسِ", "qudus", "«Holiness»", "«Kudüs'ün»", punct="،"),
  atf("وَالْمُعْجِزَاتِ", "mujiza", "«the miracles»", "«mucizelerle»", tags=[JM]),
  naat("الْبَاهِرَةِ", "bahir", "«dazzling»", "«göz kamaştırıcı»", tags=["ism-fail"], punct="،"),
])
sen("s2", "through him God heals the sick whom the physicians were unable to treat, and he cures the blind-born and the leper, and gives life to the dead by God's leave,",
        "Allah onun eliyle, hekimlerin tedavisinden âciz kaldığı hastaları iyileştirir; o, anadan doğma körü ve alacalıyı iyi eder, Allah'ın izniyle ölüleri diriltir;", [
  tok("يَشْفِي", "shafa", "verb", [HL, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — وَالْجُمْلَةُ حَالٌ (أَوِ اسْتِئْنَافٌ بَيَانِيٌّ).", "«heals» — rafʿ by an estimated ḍamma; a ḥāl clause unfolding the miracles.", "«iyileştirir» — takdîrî damme; mucizeleri açan hâl cümlesi."),
  allah_fail(),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«through him»", "«onun eliyle»"),
  maful_("الْمَرْضَى", "marid", "«the sick»", "«hastaları»", tags=[JT, "ism-maqsur-manqus"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — جَمْعُ مَرِيضٍ عَلَى فَعْلَى."),
  tok("الَّذِينَ", "alladhina", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ نَعْتٌ.", "«whom» — the relative, a naʿt.", "«ki» — sıfat olan ism-i mevsûl."),
  mazi("عَجَزَ", "ajaza", "«were unable»", "«âciz kaldı»", tags=[MW], hidden=None, extra_ar=" — وَالْجُمْلَةُ صِلَةٌ"),
  tok("عَنْ", "an", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  noun_pron("مُدَاوَاتِهِمُ", "mudawat", "مُدَاوَاتِ", "هِمُ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ، ضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — مَصْدَرُ دَاوَى.", "«treating them» — the maṣdar of dāwā; the mīm takes a ḍamma before the waṣl.", "«onları tedavi etmekten» — dâvâ'nın masdarı; mîm vasl öncesi damme aldı.", tags=[HJ, ID, "form-iii-verbs"]),
  fail("الْأَطِبَّاءُ", "tabib", "«the physicians»", "«hekimler»", tags=[JT], punct="،"),
  mudari_wa("وَيُبْرِئُ", "abraa", "«and he cures»", "«ve iyi eder»", tags=["form-iv-verbs"], extra=ISA_FAIL + " — مَهْمُوزُ اللَّامِ"),
  maful_("الْأَكْمَهَ", "akmah", "«the blind-born»", "«anadan doğma körü»"),
  atf("وَالْأَبْرَصَ", "abras", "«the leper»", "«alacalıyı»", "nasb", punct="،"),
  mudari_wa("وَيُحْيِي", "ahya", "«and gives life to»", "«ve diriltir»", tags=["naqis-verbs", "form-iv-verbs"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ"),
  maful_("الْمَوْتَى", "mayyit", "«the dead»", "«ölüleri»", tags=[JT, "ism-maqsur-manqus"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — جَمْعُ مَيِّتٍ عَلَى فَعْلَى."),
  bi_noun("بِإِذْنِ", "idhn", "«by the leave [of]»", "«izniyle»", tags=[ID], extra="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct="،"),
])
sen("s3", "and he fashions for people out of clay the likeness of a bird, then breathes into it and it becomes a bird by God's leave, and he tells of what people eat and store in their houses.",
        "insanlar için çamurdan kuş biçiminde bir şey yapar, ona üfler ve o, Allah'ın izniyle kuş oluverir; insanların yediklerini ve evlerinde biriktirdiklerini haber verir.", [
  mudari_wa("وَيَخْلُقُ", "khalaqa", "«and he fashions»", "«ve yapar»", extra=" — خَلَقَ هُنَا بِمَعْنَى: صَوَّرَ وَقَدَّرَ"),
  li_noun("لِلنَّاسِ", "nas", "«for people»", "«insanlar için»"),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«out of» — its sukūn turns to fatḥa before the article.", "«-den» — sükûnu harf-i târif önünde fethaya döndü."),
  majrur("الطِّينِ", "tin", "«clay»", "«çamurdan»"),
  tok("كَهَيْئَةِ", "haya-shape", "noun", [HJ, ID, MB], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَهَيْئَةِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَوْضِعِ الْمَفْعُولِ بِهِ عَلَى حَذْفِ مَوْصُوفٍ: شَيْئًا كَهَيْئَةِ الطَّيْرِ (وَمَنْ جَعَلَ الْكَافَ اسْمًا بِمَعْنَى مِثْل أَعْرَبَهَا مَفْعُولًا).", "«the likeness [of]» — the kāf phrase stands as the object of an understood «a thing»; some read the kāf as a noun, «the like of».", "«… biçiminde» — kâf'lı ibare mahzuf bir mevsûfun yerinde mef'ûl: «kuş biçiminde bir şey»; bazıları kâf'ı «misl» anlamında isim sayar.", segments=[seg("كَ", "ka", "prep"), seg("هَيْئَةِ", "haya-shape", "noun")]),
  mudaf_ilayh("الطَّيْرِ", "tayr", "«a bird»", "«kuşun»", punct="،"),
  fa_mudari("فَيَنْفُخُ", "nafakha", "«then breathes»", "«sonra üfler»"),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«into it»", "«ona»"),
  tok("فَيَكُونُ", "kana", "verb", [AT, KN, "hollow-verbs", "mudari-marfu"], "الْفَاءُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and it becomes» — the muḍāriʿ of kāna; its ism is concealed.", "«ve … olur» — kâne'nin muzarisi; ismi gizli.", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  tok("طَيْرًا", "tayr", "noun", [KN], "خَبَرُ يَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a bird» — kāna's khabar.", "«kuş» — kâne'nin haberi."),
  bi_noun("بِإِذْنِ", "idhn", "«by the leave [of]»", "«izniyle»", tags=[ID], extra="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct="،"),
  mudari_wa("وَيُنَبِّئُ", "nabbaa", "«and he tells»", "«ve haber verir»", tags=["form-ii-verbs"], extra=" — مَهْمُوزُ اللَّامِ"),
  bi_ma(),
  tok("يَأْكُلُهُ", "akala", "verb", [MW, MB, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ صِلَةٌ.", "«eat» — the hāʾ is the fronted object; the ṣila.", "«yedikleri» — hâ öne alınmış mef'ûl; sıla.", segments=[seg("يَأْكُلُ", "akala", "verb"), seg("هُ", "pron-3ms", "pron")]),
  fail("النَّاسُ", "nas", "«people»", "«insanlar»"),
  tok("وَيَدَّخِرُونَهُ", "iddakhara", "verb", [AT, AK, MB, MW, "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَدَّخِرُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — أَصْلُهُ يَذْتَخِرُ: قُلِبَتِ التَّاءُ دَالًا وَالذَّالُ دَالًا ثُمَّ أُدْغِمَتَا.", "«and store» — one of the five verbs; Form VIII of ذ خ ر with its tāʾ turned to dāl and assimilated.", "«ve biriktirdikleri» — ef'âl-i hamseden; ذ خ ر kökünün iftiâli, tâ dâl'a dönüp idgam edildi.", segments=[seg("وَ", "wa", "conj"), seg("يَدَّخِرُونَ", "iddakhara", "verb"), seg("هُ", "pron-3ms", "pron")]),
  fi(),
  noun_pron("بُيُوتِهِمْ", "bayt", "بُيُوتِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their houses»", "«evlerinde»", tags=[HJ, ID, JT], punct="."),
])
sen("s4", "So by all this he restores trust in what the Torah had brought of the reports of the messengers' miracles and the reports of the divine power, renews faith in it, and gives the lie to the worship of sense and experiment;",
        "Bütün bunlarla Tevrat'ta gelen resullerin mucizeleri ve ilâhî kudret haberlerine güveni geri getirir, onlara imanı yeniler, duyuya ve deneye tapmayı yalanlar;", [
  tok("فَيُعِيدُ", "aada", "verb", [AT, "mudari-marfu", "hollow-verbs", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَيُعِيدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — أَجْوَفُ مِنْ بَابِ الْإِفْعَالِ.", "«so he restores» — a hollow Form IV muḍāriʿ.", "«böylece geri getirir» — ecvef if'âl muzarisi.", segments=[seg("فَ", "fa", "conj"), seg("يُعِيدُ", "aada", "verb")]),
  bi_noun("بِكُلِّ", "kull", "«by all [of]»", "«bütün»", tags=[ID], extra="، مُضَافٌ"),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that»", "«bunlarla»"),
  maful_("الثِّقَةَ", "thiqa", "«trust»", "«güveni»"),
  bi_ma(),
  mazi("جَاءَ", "jaa", "«had come»", "«gelen»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةٌ"),
  fi(),
  majrur("التَّوْرَاةِ", "tawrat", "«the Torah»", "«Tevrat'ta»"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ (بَيَانُ مَا)."),
  majrur("خَبَرِ", "khabar", "«the report [of]»", "«haberinden»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("مُعْجِزَاتِ", "mujiza", "«the miracles [of]»", "«mucizelerinin»", tags=[ID, JM], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الرُّسُلِ", "rasul", "«the messengers»", "«resullerin»", tags=[JT], punct="،"),
  atf("وَأَخْبَارِ", "khabar", "«the reports [of]»", "«haberlerine»", tags=[ID, JT], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الْقُدْرَةِ", "qudra", "«the power»", "«kudretin»"),
  naat("الْإِلٰهِيَّةِ", "ilahi", "«divine»", "«ilâhî»", tags=["ism-mansub"], punct="،"),
  mudari_wa("وَيُجَدِّدُ", "jaddada", "«and renews»", "«ve yeniler»", tags=["form-ii-verbs"]),
  maful_("الْإِيمَانَ", "iman", "«faith»", "«imanı»"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«in them»", "«onlara»", punct="،"),
  mudari_wa("وَيُكَذِّبُ", "kadhdhaba", "«and gives the lie to»", "«ve yalanlar»", tags=["form-ii-verbs"]),
  maful_("الْعِبَادَةَ", "ibada", "«the worship»", "«tapmayı»"),
  li_noun("لِلْحِسِّ", "hiss", "«of sense»", "«duyuya»"),
  atf("وَالتَّجْرِبَةِ", "tajriba", "«experiment»", "«deneye»", punct="،"),
])
sen("s5", "so those who deny the breadth of the divine power and the strength of the Lord's will rose up, and decreed that there is nothing new and nothing more beyond what they had learnt and witnessed.",
        "bunun üzerine ilâhî kudretin genişliğini ve rabbânî irâdenin gücünü inkâr edenler ayağa kalktı ve bildikleri ve gördüklerinin ötesinde yeni ve fazla bir şey olmadığına hükmettiler.", [
  tok("فَقَامَ", "qama", "verb", [AT, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَقَامَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ.", "«so rose up» — a hollow māḍī.", "«bunun üzerine ayağa kalktı» — ecvef mâzî.", segments=[seg("فَ", "fa", "conj"), seg("قَامَ", "qama", "verb")]),
  tok("الَّذِينَ", "alladhina", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«those who» — the relative as the doer.", "«… edenler» — fâil olan ism-i mevsûl."),
  khamsa("يُنْكِرُونَ", "ankara", "«deny»", "«inkâr ederler»", tags=[MW, "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ صِلَةٌ"),
  maful_("سَعَةَ", "saa", "«the breadth [of]»", "«genişliğini»", tags=[ID, "mithal-verbs"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مَصْدَرُ وَسِعَ، حُذِفَتْ فَاؤُهُ وَعُوِّضَ عَنْهَا بِالتَّاءِ."),
  mudaf_ilayh("الْقُدْرَةِ", "qudra", "«the power»", "«kudretin»"),
  naat("الْإِلٰهِيَّةِ", "ilahi", "«divine»", "«ilâhî»", tags=["ism-mansub"], punct="،"),
  atf("وَقُوَّةَ", "quwwa", "«the strength [of]»", "«gücünü»", "nasb", tags=[ID], sign="بِالْفَتْحَةِ، مُضَافٌ"),
  mudaf_ilayh("الْإِرَادَةِ", "irada", "«the will»", "«irâdenin»"),
  naat("الرَّبَّانِيَّةِ", "rabbani", "«of the Lord»", "«rabbânî»", tags=["ism-mansub"], punct="،"),
  tok("فَقَرَّرُوا", "qarrara", "verb", [AT, "form-ii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَقَرَّرُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«and decreed» — the wāw is the doer.", "«ve hükmettiler» — vâv fâil.", segments=[seg("فَ", "fa", "conj"), seg("قَرَّرُوا", "qarrara", "verb")]),
  tok("أَنْ", "an-mukhaffafa", "part", [IW, "hadhf-wa-taqdir"], "أَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، وَجُمْلَةُ لَا جَدِيدَ خَبَرُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ قَرَّرُوا.", "«that» — the lightened an; its ism is the deleted pronoun of the matter, the lā clause its khabar.", "«… -dığına» — muhaffef en; ismi mahzuf zamîr-i şe'n, lâ cümlesi haberi."),
  la_jins("لَا"),
  ism_la("جَدِيدَ", "jadid", "«[no] new thing»", "«yeni [bir şey yok]»"),
  tok("وَأَنْ", "an-mukhaffafa", "part", [AT, IW, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَأَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ.", "«and that» — a second lightened an.", "«ve … -dığına» — ikinci muhaffef en.", segments=wa_("أَنْ", "an-mukhaffafa", "part")),
  la_jins("لَا"),
  ism_la("مَزِيدَ", "mazid", "«[no] more»", "«fazla [bir şey yok]»"),
  tok("فِيمَا", "ma-mawsula", "pron", [HJ, MW], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ.", "«in what» — the relative after fī, attached to lā's understood khabar.", "«… şeyde» — fî'den sonra ism-i mevsûl; lâ'nın mahzuf haberine bağlı.", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  v_pl_pron("عَلِمُوهُ", "alima", "عَلِمُو", "هُ", "pron-3ms", "«they had learnt»", "«bildikleri»", tags=[MW]),
  v_pl_pron("وَشَاهَدُوهُ", "shahada-verb", "شَاهَدُو", "هُ", "pron-3ms", "«and witnessed»", "«ve gördükleri»", tags=["form-iii-verbs"], wa=True, punct="."),
])

CAND = {
 "akrama": G("akrama", "أَكْرَمَ", "ك ر م", "verb", "to honour (Form IV)", "ikram etmek (if'âl)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب أ", "noun", "prophethood", "nübüvvet", 1, plural="نُبُوَّات"),
 "wahy": G("wahy", "وَحْي", "و ح ي", "noun", "revelation", "vahiy", 1),
 "aata-bring": G("aata-bring", "آتَى", "أ ت ي", "verb", "to give, to bring (two objects; Form IV, defective)", "vermek (iki mef'ûl; if'âl, nâkıs)", 1),
 "injil": G("injil", "إِنْجِيل", None, "propn", "the Injīl (the Gospel)", "İncil", 1),
 "ayyada": G("ayyada", "أَيَّدَ", "أ ي د", "verb", "to back, to support (Form II)", "desteklemek, te'yid etmek (tef'îl)", 2),
 "ruh": G("ruh", "رُوح", "ر و ح", "noun", "spirit, soul", "ruh", 1, plural="أَرْوَاح"),
 "qudus": G("qudus", "قُدُس", "ق د س", "noun", "holiness; (rūḥ al-qudus) the Holy Spirit", "kutsallık; (rûhu'l-kudüs) Cebrâil", 2),
 "mujiza": G("mujiza", "مُعْجِزَة", "ع ج ز", "noun", "a miracle", "mucize", 1, plural="مُعْجِزَات"),
 "bahir": G("bahir", "بَاهِر", "ب ه ر", "noun", "dazzling, brilliant (an active participle)", "göz kamaştırıcı, parlak (ism-i fâil)", 2),
 "shafa": G("shafa", "شَفَى", "ش ف ي", "verb", "to heal (defective)", "şifa vermek, iyileştirmek (nâkıs)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "marid": G("marid", "مَرِيض", "م ر ض", "noun", "sick, ill", "hasta", 1, plural="مَرْضَى"),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "who, those who (pl.)", "ki onlar, … -enler", 1),
 "ajaza": G("ajaza", "عَجَزَ", "ع ج ز", "verb", "to be unable (ʿan: to)", "âciz kalmak", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "mudawat": G("mudawat", "مُدَاوَاة", "د و ي", "noun", "treating, medical treatment (the maṣdar of Form III)", "tedavi (müfâale masdarı)", 2),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "tabib": G("tabib", "طَبِيب", "ط ب ب", "noun", "a physician", "hekim, tabip", 1, plural="أَطِبَّاء"),
 "abraa": G("abraa", "أَبْرَأَ", "ب ر أ", "verb", "to cure (Form IV, hamza-final)", "iyileştirmek (if'âl, mehmûzü'l-lâm)", 2),
 "akmah": G("akmah", "أَكْمَه", "ك م ه", "noun", "blind from birth", "anadan doğma kör", 3),
 "abras": G("abras", "أَبْرَص", "ب ر ص", "noun", "a leper", "alacalı, cüzamlı", 3),
 "ahya": G("ahya", "أَحْيَا", "ح ي ي", "verb", "to give life (Form IV, defective)", "diriltmek (if'âl, nâkıs)", 1),
 "mayyit": G("mayyit", "مَيِّت", "م و ت", "noun", "dead", "ölü", 1, plural="مَوْتَى"),
 "idhn": G("idhn", "إِذْن", "أ ذ ن", "noun", "leave, permission", "izin", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create; to fashion", "yaratmak; şekil vermek", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "tin": G("tin", "طِين", "ط ي ن", "noun", "clay", "çamur", 1),
 "ka": G("ka", "كَ", None, "prep", "like, as", "gibi", 1),
 "haya-shape": G("haya-shape", "هَيْئَة", "ه ي أ", "noun", "a form, a shape", "biçim, şekil, heyet", 2),
 "tayr": G("tayr", "طَيْر", "ط ي ر", "noun", "a bird; birds", "kuş", 1, plural="طُيُور"),
 "nafakha": G("nafakha", "نَفَخَ", "ن ف خ", "verb", "to breathe (fī: into), to blow", "üflemek", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "nabbaa": G("nabbaa", "نَبَّأَ", "ن ب أ", "verb", "to inform, to tell (bi: of) (Form II, hamza-final)", "haber vermek (tef'îl, mehmûzü'l-lâm)", 2),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "iddakhara": G("iddakhara", "اِدَّخَرَ", "ذ خ ر", "verb", "to store up, to hoard (Form VIII of ذ خ ر, assimilated)", "biriktirmek, saklamak (iftiâl, idgamlı)", 2),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "a house", "ev", 1, plural="بُيُوت"),
 "aada": G("aada", "أَعَادَ", "ع و د", "verb", "to restore, to bring back (Form IV, hollow)", "geri getirmek, iade etmek (if'âl, ecvef)", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "thiqa": G("thiqa", "ثِقَة", "و ث ق", "noun", "trust, confidence", "güven", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "tawrat": G("tawrat", "التَّوْرَاة", None, "propn", "the Torah", "Tevrat", 1),
 "khabar": G("khabar", "خَبَر", "خ ب ر", "noun", "a report, news", "haber", 1, plural="أَخْبَار"),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resul", 1, plural="رُسُل"),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "ilahi": G("ilahi", "إِلٰهِيّ", "أ ل ه", "noun", "divine (a nisba)", "ilâhî (nisbet)", 1),
 "jaddada": G("jaddada", "جَدَّدَ", "ج د د", "verb", "to renew (Form II)", "yenilemek (tef'îl)", 1),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith, belief", "iman", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "kadhdhaba": G("kadhdhaba", "كَذَّبَ", "ك ذ ب", "verb", "to call a liar, to give the lie to (Form II)", "yalanlamak (tef'îl)", 1),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet, tapma", 1, plural="عِبَادَات"),
 "hiss": G("hiss", "حِسّ", "ح س س", "noun", "sense, sensation", "duyu, his", 2),
 "tajriba": G("tajriba", "تَجْرِبَة", "ج ر ب", "noun", "an experience, an experiment", "tecrübe, deney", 2, plural="تَجَارِب"),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to rise, to stand (hollow)", "kalkmak, ayağa kalkmak (ecvef)", 1),
 "ankara": G("ankara", "أَنْكَرَ", "ن ك ر", "verb", "to deny (Form IV)", "inkâr etmek (if'âl)", 1),
 "saa": G("saa", "سَعَة", "و س ع", "noun", "breadth, capacity (the maṣdar of wasiʿa, its wāw dropped)", "genişlik, kapasite (vesia'nın vâvı düşmüş masdarı)", 2),
 "quwwa": G("quwwa", "قُوَّة", "ق و ي", "noun", "strength, power", "güç, kuvvet", 1, plural="قُوًى"),
 "irada": G("irada", "إِرَادَة", "ر و د", "noun", "will, volition", "irâde", 1),
 "rabbani": G("rabbani", "رَبَّانِيّ", "ر ب ب", "noun", "of the Lord, divine (a nisba with the added ān)", "rabbânî (nisbet)", 2),
 "qarrara": G("qarrara", "قَرَّرَ", "ق ر ر", "verb", "to decide, to decree (Form II)", "karar vermek, hükmetmek (tef'îl)", 1),
 "an-mukhaffafa": G("an-mukhaffafa", "أَنْ (الْمُخَفَّفَة)", None, "part", "that — the lightened an (from anna)", "… -dığı — muhaffef en (enne'den)", 2),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "jadid": G("jadid", "جَدِيد", "ج د د", "noun", "new", "yeni", 1),
 "mazid": G("mazid", "مَزِيد", "ز ي د", "noun", "more, an increase", "fazla, ziyade", 2),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know, to learn", "bilmek", 1),
 "shahada-verb": G("shahada-verb", "شَاهَدَ", "ش ه د", "verb", "to witness, to see (Form III)", "görmek, müşâhede etmek (müfâale)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "aata-bring", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "آتَ", "ؤْت", "i", "آت", "إِيتَاء", "مُؤْتٍ (الْمُؤْتِي)", "مُؤْتًى", "أُوتِيَ", "يُؤْتَى", "آتَاهُ الشَّيْءَ: أَعْطَاهُ إِيَّاهُ — إِفْعَالٌ مِنْ أَتَى، مَهْمُوزُ الْفَاءِ نَاقِصٌ: آتَى يُؤْتِي، أُوتِيَ."))
put_morph(mo, "abraa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْرَأ", "بْرِئ", "أَبْرِئ", "إِبْرَاء", "مُبْرِئ", "مُبْرَأ", "أُبْرِئَ", "يُبْرَأُ", "أَبْرَأَهُ مِنَ الْمَرَضِ: شَفَاهُ — مَهْمُوزُ اللَّامِ."))
put_morph(mo, "nafakha", _sg.sound1("nasara", "نَفَخ", "نْفُخ", "اُنْفُخ", "نَفْخ", "نَافِخ", "مَنْفُوخ", "نُفِخَ", "يُنْفَخُ", "نَفَخَ فِي الشَّيْءِ يَنْفُخُ: أَخْرَجَ الرِّيحَ مِنْ فَمِهِ فِيهِ."))
put_morph(mo, "nabbaa", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَبَّأ", "نَبِّئ", "نَبِّئ", "تَنْبِئَة", "مُنَبِّئ", "مُنَبَّأ", "نُبِّئَ", "يُنَبَّأُ", "نَبَّأَهُ بِالْأَمْرِ: أَخْبَرَهُ بِهِ — مَهْمُوزُ اللَّامِ."))
put_morph(mo, "iddakhara", _sg.derived(_sg.B8 + " — أُبْدِلَتْ تَاءُ الِافْتِعَالِ دَالًا بَعْدَ الذَّالِ وَأُدْغِمَتَا", _sg.W8, "َ", "اِدَّخَر", "دَّخِر", "اِدَّخِر", "اِدِّخَار", "مُدَّخِر", "مُدَّخَر", "اُدُّخِرَ", "يُدَّخَرُ", "اِدَّخَرَ الشَّيْءَ: خَبَّأَهُ لِوَقْتِ الْحَاجَةِ — أَصْلُهُ اِذْتَخَرَ."))
put_morph(mo, "jaddada", _sg.derived(_sg.B2, _sg.W2, "ُ", "جَدَّد", "جَدِّد", "جَدِّد", "تَجْدِيد", "مُجَدِّد", "مُجَدَّد", "جُدِّدَ", "يُجَدَّدُ", "جَدَّدَ الشَّيْءَ: صَيَّرَهُ جَدِيدًا."))
put_morph(mo, "qarrara", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَرَّر", "قَرِّر", "قَرِّر", "تَقْرِير", "مُقَرِّر", "مُقَرَّر", "قُرِّرَ", "يُقَرَّرُ", "قَرَّرَ الْأَمْرَ: ثَبَّتَهُ وَحَكَمَ بِهِ."))
put_morph(mo, "ajaza", _sg.sound1("daraba", "عَجَز", "عْجِز", "اِعْجِز", "عَجْز", "عَاجِز", None, None, None, "عَجَزَ عَنِ الشَّيْءِ يَعْجِزُ: لَمْ يَقْدِرْ عَلَيْهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch28 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 28 (print pp. 45–46; ʿĪsā §9): prophethood, revelation, the Injīl and the Holy Spirit (s1); healing the sick, the blind-born and the leper, raising the dead (s2); the clay bird and telling what is eaten and stored (s3); trust in the Torah's reports restored, the worship of sense and experiment refuted (s4); the deniers decree «nothing new, nothing more» (s5)."
ADD_TR = " Yirmi sekizinci bölüm (baskı s. 45–46; Îsâ §9): peygamberlik, vahiy, İncil ve Rûhu'l-Kudüs (s1); hastaların, anadan doğma körün ve alacalının iyileştirilmesi, ölülerin diriltilmesi (s2); çamurdan kuş, yenen ve biriktirilenin haberi (s3); Tevrat haberlerine güvenin yenilenmesi, duyu ve deneye tapmanın yalanlanması (s4); inkârcıların «yeni ve fazla bir şey yok» hükmü (s5)."
write_out(28, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §9", GLOSS_ADD, notes=(), related=())
report(28, S, GLOSS_ADD, ())
