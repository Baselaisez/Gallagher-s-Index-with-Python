# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 33: «قِصَّةُ عِيسَى» §12 closes — Āl ʿImrân 3:55–60: «I shall take you and raise you to Me»; the unbelievers punished, the believers paid in full; «this We recite to you»; «the likeness of ʿĪsā with God is as the likeness of Ādam»; «the truth is from your Lord»; print pp. 48–49.
python3 tools/authoring/author_qisas4_ch33.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى فِي الْقُرْآنِ: إِنِّي مُتَوَفِّيكَ وَرَافِعُكَ إِلَيَّ (آل عمران ٥٥–٦٠)", "en": "The story of ʿĪsā in the Qurʾān: I shall take you and raise you to Me (3:55–60)", "tr": "Kur'ân'da Îsâ kıssası: seni vefat ettirip katıma yükselteceğim (Âl-i İmrân 55–60)"}
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

# ---------------------------------------------------------------- §12 (closing): آل عمران ٥٥–٦٠ (print pp. 48–49)
sen("s1", "«When God said: O ʿĪsā, I shall take you and raise you to Me and purify you from those who disbelieved, and set those who follow you above those who disbelieved until the Day of Resurrection; then to Me is your return, and I shall judge between you concerning what you used to differ in.» (3:55)",
        "«Hani Allah demişti: Ey Îsâ! Seni vefat ettirecek, katıma yükseltecek, inkâr edenlerden arındıracak ve sana uyanları kıyâmet gününe kadar inkâr edenlerin üstünde tutacağım. Sonra dönüşünüz banadır; ayrılığa düştüğünüz şeylerde aranızda hükmedeceğim.» (3:55)", [
  *quran([
  tok("إِذْ", "idh", "noun", [MF, "hadhf-wa-taqdir"], "ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: اذْكُرْ (أَوْ بَدَلٌ مِنْ إِذْ قَالَتِ الْمَلَائِكَةُ).", "«when» — the object of an understood «remember», or a badal of the earlier idh.", "«hani» — mukadder «hatırla»nın mef'ûlü yahut önceki iz'den bedel."),
  mazi("قَالَ", "qala", "«said»", "«dedi»", tags=[ID, "hollow-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  allah_fail(),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("عِيسَى", "isa", "propn", ["vocative-munada", MM, "ism-maqsur-manqus"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ.", "«ʿĪsā» — a single-name munādā, built on an estimated ḍamma.", "«Îsâ» — müfred alem münâdâ, takdîrî damme üzere mebnî."),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I» — inna with the yāʾ as its ism.", "«şüphesiz ben» — inne; yâ ismi.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  participle_ka("مُتَوَفِّيكَ", "mutawaffi", "مُتَوَفِّي", "«the one taking you»", "«seni vefat ettirecek olan»", tags=["form-v-verbs", "ism-maqsur-manqus"], ar_extra=" — اسْمُ فَاعِلٍ مِنْ تَوَفَّى، مَنْقُوصٌ: ظَهَرَتْ يَاؤُهُ لِلْإِضَافَةِ، وَرُفِعَ بِضَمَّةٍ مُقَدَّرَةٍ", wa=False, first=True),
  participle_ka("وَرَافِعُكَ", "rafi-raiser", "رَافِعُ", "«raising you»", "«seni yükselten»"),
  prep_pron("إِلَيَّ", "ila", "يَّ", "pron-1s", "«to Me»", "«katıma»", extra_ar=" — قُلِبَتْ أَلِفُ إِلَى يَاءً وَأُدْغِمَتْ فِي يَاءِ الْمُتَكَلِّمِ"),
  participle_ka("وَمُطَهِّرُكَ", "mutahhir", "مُطَهِّرُ", "«purifying you»", "«seni arındıran»", tags=["form-ii-verbs"]),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  alladhina("jarr", "مَجْرُورٌ بِمِنْ", "«those who»", "«… -enlerden»", tags=[HJ]),
  kafaru(),
  tok("وَجَاعِلُ", "jaail", "noun", [AT, IW, ID, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَجَاعِلُ مَعْطُوفٌ عَلَى خَبَرِ إِنَّ مَرْفُوعٌ، مُضَافٌ إِلَى الَّذِينَ بَعْدَهُ (إِضَافَةٌ لَفْظِيَّةٌ: اسْمُ الْفَاعِلِ إِلَى مَفْعُولِهِ الْأَوَّلِ).", "«and setting» — an active participle annexed to its first object, «those who follow you».", "«ve kılan» — ilk mef'ûlü olan «sana uyanlar»a muzâf ism-i fâil.", segments=[seg("وَ", "wa", "conj"), seg("جَاعِلُ", "jaail", "noun")]),
  alladhina("jarr", "مُضَافٌ إِلَيْهِ", "«those who»", "«… -enleri»", tags=[ID]),
  tok("اتَّبَعُوكَ", "ittabaa", "verb", [MW, MB, "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«follow you» — the ṣila; the kāf is the object.", "«sana uyanlar» — sıla; kâf mef'ûl.", segments=[seg("اتَّبَعُو", "ittabaa", "verb"), seg("كَ", "pron-2ms", "pron")]),
  zarf("فَوْقَ", "fawqa", "«above»", "«üstünde»"),
  alladhina("jarr", "مُضَافٌ إِلَيْهِ", "«those who»", "«… -enlerin»", tags=[ID]),
  kafaru(),
  prep("إِلَى", "ila", "«until»", "«-e kadar»", ar="حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ."),
  majrur("يَوْمِ", "yawm", "«the Day [of]»", "«gününe»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْقِيَامَةِ", "qiyama", "«Resurrection»", "«kıyâmet»"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then»", "«sonra»"),
  prep_pron("إِلَيَّ", "ila", "يَّ", "pron-1s", "«to Me» — the fronted khabar.", "«banadır» — öne alınmış haber.", tags=[MK], extra_ar=" — خَبَرٌ مُقَدَّمٌ"),
  noun_pron("مَرْجِعُكُمْ", "marji", "مَرْجِعُ", "كُمْ", "pron-2mp", "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — مَصْدَرٌ مِيمِيٌّ.", "«your return» — the delayed mubtadaʾ; a mīm-maṣdar.", "«dönüşünüz» — sonraya kalan mübtedâ; mîmli masdar.", tags=[MK, ID]),
  fa_mudari("فَأَحْكُمُ", "hakama", "«and I shall judge»", "«ve hükmederim»", hidden="أَنَا"),
  noun_pron("بَيْنَكُمْ", "bayna", "بَيْنَ", "كُمْ", "pron-2mp", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«between you»", "«aranızda»", tags=[MF, ID]),
  tok("فِيمَا", "ma-mawsula", "pron", [HJ, MW], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«concerning what»", "«… şeylerde»", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("كُنْتُمْ", "kana", "verb", [MW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهُ — وَالْجُمْلَةُ صِلَةٌ.", "«you used to» — kāna; the ṣila.", "«idiniz» — kâne; sıla.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in it»", "«onda»"),
  khamsa("تَخْتَلِفُونَ", "ikhtalafa", "«differ»", "«ayrılığa düşüyordunuz»", tags=[KN, "form-viii-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ", punct=AYA),
  ]),
])
sen("s2", "«As for those who disbelieved, I shall punish them with a severe punishment in this world and the Hereafter, and they shall have no helpers.» (3:56)",
        "«İnkâr edenlere gelince, onlara dünyada ve âhirette şiddetli bir azapla azap edeceğim; onların hiçbir yardımcısı yoktur.» (3:56)", [
  *quran([
  tok("فَأَمَّا", "amma", "part", [AT, "amma-tafsiliyya", SH], "الْفَاءُ لِلتَّفْرِيعِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — the particle of detailing.", "«-e gelince» — tafsîl edatı.", segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  alladhina("raf", "مُبْتَدَأٌ", "«those who»", "«… -enler»", tags=[MK]),
  kafaru(),
  tok("فَأُعَذِّبُهُمْ", "adhdhaba", "verb", [SH, MK, MB, "mudari-marfu", "form-ii-verbs"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَأُعَذِّبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالضَّمِيرُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«I shall punish them» — the fāʾ of ammā's answer; the clause is the khabar.", "«onlara azap edeceğim» — emmâ'nın cevap fâ'sı; cümle haber.", segments=[seg("فَ", "fa", "conj"), seg("أُعَذِّبُ", "adhdhaba", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("عَذَابًا", "adhab", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ (مُبَيِّنٌ لِلنَّوْعِ بِصِفَتِهِ).", "«with a punishment» — an absolute object.", "«bir azapla» — mef'ûl-i mutlak."),
  naat("شَدِيدًا", "shadid", "«severe»", "«şiddetli»", case="nasb"),
  fi(),
  majrur("الدُّنْيَا", "dunya", "«this world»", "«dünyada»", tags=["ism-maqsur-manqus"], ar="مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ."),
  atf("وَالْآخِرَةِ", "akhira", "«the Hereafter»", "«âhirette»"),
  tok("وَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا (كَلَا).", "«and … no» — the negating mā.", "«ve … yok» — nefiy mâ'sı.", segments=wa_("مَا", "ma-nafiya", "part")),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«for them» — the fronted khabar.", "«onların» — öne alınmış haber.", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ"),
  prep("مِنْ", "min", "«[any]»", "«hiçbir»", ar="حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ."),
  tok("نَاصِرِينَ", "nasir-helper", "noun", [MK, JS, "ism-fail"], "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا بِمِنَ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا، وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«helpers» — the delayed mubtadaʾ, jarr in form by the extra min, rafʿ in place.", "«yardımcılar» — sonraya kalan mübtedâ; zâid min ile lafzan mecrûr, mahallen merfû.", punct=AYA),
  ]),
])
sen("s3", "«And as for those who believed and did righteous deeds, He will pay them their rewards in full; and God does not love the wrongdoers.» (3:57)",
        "«İnanıp sâlih ameller işleyenlere gelince, onlara mükâfatlarını tam olarak verecektir; Allah zâlimleri sevmez.» (3:57)", [
  *quran([
  tok("وَأَمَّا", "amma", "part", [AT, "amma-tafsiliyya", SH], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«ve … -e gelince»", segments=wa_("أَمَّا", "amma", "part")),
  alladhina("raf", "مُبْتَدَأٌ", "«those who»", "«… -enler»", tags=[MK]),
  mazi_pl("آمَنُوا", "aamana", "«believed»", "«inandılar»", tags=[MW, "form-iv-verbs"]),
  mazi_pl("وَعَمِلُوا", "amila", "«and did»", "«ve işlediler»", tags=[AT, MW], wa=True),
  tok("الصَّالِحَاتِ", "salih", "noun", [MB, JM, "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: الْأَعْمَالَ الصَّالِحَاتِ.", "«righteous deeds» — a sound feminine plural: kasra for fatḥa in naṣb.", "«sâlih amelleri» — cemi müennes sâlim: nasbda fetha yerine kesre."),
  tok("فَيُوَفِّيهِمْ", "waffa", "verb", [SH, MK, MX, "mudari-marfu", "naqis-verbs", "form-ii-verbs"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَيُوَفِّي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«He will pay them in full» — ammā's answer; two objects, the pronoun the first.", "«onlara tam verecek» — emmâ'nın cevabı; iki mef'ûl, zamir ilki.", segments=[seg("فَ", "fa", "conj"), seg("يُوَفِّي", "waffa", "verb"), seg("هِمْ", "pron-3mp", "pron")]),
  noun_pron("أُجُورَهُمْ", "ajr", "أُجُورَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their rewards» — the second object.", "«mükâfatlarını» — ikinci mef'ûl.", tags=[MX, ID, JT]),
  tok("وَاللهُ", "allah", "propn", [AT, MK], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.", "«and God» — the mubtadaʾ.", "«ve Allah» — mübtedâ.", segments=wa_("اللهُ", "allah", "propn")),
  la_nafiya(),
  neg_mudari("يُحِبُّ", "ahabba", "«loves»", "«sever»", tags=[MK, "doubled-verbs", "form-iv-verbs"], hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  tok("الظَّالِمِينَ", "zalim", "noun", [MB, JS, "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the wrongdoers» — naṣb by the yāʾ.", "«zâlimleri» — yâ ile mansub.", punct=AYA),
  ]),
])
sen("s4", "«This We recite to you of the signs and the wise Reminder. Indeed the likeness of ʿĪsā with God is as the likeness of Ādam: He created him from dust, then said to him: Be! and he was. The truth is from your Lord, so be not of the doubters.» (3:58–60)",
        "«Bunu sana âyetlerden ve hikmetli Zikir'den okuyoruz. Şüphesiz Allah katında Îsâ'nın durumu Âdem'in durumu gibidir: onu topraktan yarattı, sonra ona «Ol!» dedi, o da oluverdi. Hak Rabbindendir; sakın şüphe edenlerden olma.» (3:58–60)", [
  *quran([
  tok("ذٰلِكَ", "dhalika", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bunu» — mübtedâ."),
  tok("نَتْلُوهُ", "tala-recite", "verb", [MK, MB, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«We recite it» — the khabar clause; the hāʾ the object.", "«onu okuyoruz» — haber cümlesi; hâ mef'ûl.", segments=[seg("نَتْلُو", "tala-recite", "verb"), seg("هُ", "pron-3ms", "pron")]),
  prep_pron("عَلَيْكَ", "ala", "كَ", "pron-2ms", "«to you»", "«sana»"),
  tok("مِنَ", "min", "prep", [HJ, HL], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنَ الْهَاءِ.", "«of» — explanatory; the phrase is a ḥāl of the object.", "«-den» — beyan için; ibare mef'ûlün hâli."),
  majrur("الْآيَاتِ", "aya", "«the signs»", "«âyetlerden»", tags=[JM]),
  atf("وَالذِّكْرِ", "dhikr", "«the Reminder»", "«Zikir'den»"),
  naat("الْحَكِيمِ", "hakim", "«wise»", "«hikmetli»", punct=AYA),
  inna(),
  tok("مَثَلَ", "mathal", "noun", [IW, ID], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the likeness [of]» — inna's ism.", "«durumu» — inne'nin ismi."),
  tok("عِيسَى", "isa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ'nın»"),
  zarf("عِنْدَ", "inda", "«with»", "«katında»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah»"),
  tok("كَمَثَلِ", "mathal", "noun", [HJ, IW, ID], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَثَلِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«as the likeness [of]» — the kāf phrase is inna's khabar.", "«… durumu gibi» — kâf'lı ibare inne'nin haberi.", segments=[seg("كَ", "ka", "prep"), seg("مَثَلِ", "mathal", "noun")]),
  tok("آدَمَ", "adam-prophet", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.", "«Ādam» — a diptote.", "«Âdem'in» — gayr-i munsarıf."),
  v_pron("خَلَقَهُ", "khalaqa", "خَلَقَ", "هُ", "pron-3ms", "«He created him»", "«onu yarattı»", tags=["jumla-mutarida"], hidden="هُوَ"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("تُرَابٍ", "turab", "«dust»", "«topraktan»"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then»", "«sonra»"),
  mazi("قَالَ", "qala", "«said»", "«dedi»", tags=["hollow-verbs"], hidden="هُوَ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»"),
  tok("كُنْ", "kana", "verb", [AM, KN, "hollow-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — مَقُولُ الْقَوْلِ.", "«Be!»", "«Ol!»"),
  tok("فَيَكُونُ", "kana", "verb", [AT, "mudari-marfu", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ: هُوَ — حِكَايَةُ حَالٍ مَاضِيَةٍ.", "«and he was» — a muḍāriʿ narrating a past state.", "«o da oluverdi» — geçmiş hâli hikâye eden muzari.", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")], punct=AYA),
  tok("الْحَقُّ", "haqq", "noun", [MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the truth» — the mubtadaʾ.", "«hak» — mübtedâ."),
  prep("مِنْ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ."),
  noun_pron("رَبِّكَ", "rabb", "رَبِّ", "كَ", "pron-2ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord»", "«Rabbin»", tags=[HJ, ID, MK]),
  tok("فَلَا", "la-nahiya", "part", [AT, LJ], "الْفَاءُ الْفَصِيحَةُ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«so … not» — the prohibiting lā.", "«sakın … -ma» — nehiy lâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nahiya", "part")]),
  tok("تَكُنْ", "kana", "verb", [LJ, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: أَنْتَ.", "«be» — jazm by lā; the hollow wāw drops before the sukūn.", "«olma» — lâ ile meczûm; ecvef vâv düştü."),
  tok("مِنَ", "min", "prep", [HJ, KN], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ تَكُنْ.", "«of» — the phrase is kāna's khabar.", "«-den» — ibare kâne'nin haberi."),
  tok("الْمُمْتَرِينَ", "mumtari", "noun", [HJ, JS, "ism-fail", "form-viii-verbs", "ism-maqsur-manqus"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — جَمْعُ مُمْتَرٍ، اسْمِ الْفَاعِلِ الْمَنْقُوصِ مِنِ امْتَرَى.", "«the doubters» — the plural of a manqūṣ participle.", "«şüphe edenler» — mankûs ism-i fâilin cemi.", punct=AYA),
  ]),
])

CAND = {
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "mutawaffi": G("mutawaffi", "مُتَوَفِّي", "و ف ي", "noun", "one who takes (a soul) in full (an active participle of Form V, manqūṣ)", "vefat ettiren, tam alan (tefa''ul'ün mankûs ism-i fâili)", 3),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "rafi-raiser": G("rafi-raiser", "رَافِع", "ر ف ع", "noun", "one who raises (an active participle)", "yükselten (ism-i fâil)", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "mutahhir": G("mutahhir", "مُطَهِّر", "ط ه ر", "noun", "one who purifies (an active participle of Form II)", "arındıran (tef'îl ism-i fâili)", 2),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "who, those who (pl.)", "ki onlar, … -enler", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve", "inkâr etmek, küfretmek", 1),
 "jaail": G("jaail", "جَاعِل", "ج ع ل", "noun", "one who makes, sets (an active participle)", "kılan, yapan (ism-i fâil)", 2),
 "ittabaa": G("ittabaa", "اِتَّبَعَ", "ت ب ع", "verb", "to follow (Form VIII)", "uymak, tâbi olmak (iftiâl)", 1),
 "fawqa": G("fawqa", "فَوْقَ", "ف و ق", "noun", "above", "üstünde", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "qiyama": G("qiyama", "قِيَامَة", "ق و م", "noun", "the Resurrection", "kıyâmet", 1),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "marji": G("marji", "مَرْجِع", "ر ج ع", "noun", "a return; a place of return (a mīm-maṣdar)", "dönüş; dönüş yeri (mîmli masdar)", 2),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (pl.)", "siz / sizi / sizin", 1),
 "hakama": G("hakama", "حَكَمَ", "ح ك م", "verb", "to judge", "hükmetmek", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "ikhtalafa": G("ikhtalafa", "اِخْتَلَفَ", "خ ل ف", "verb", "to differ (Form VIII)", "ihtilâf etmek, ayrılığa düşmek (iftiâl)", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "amma": G("amma", "أَمَّا", None, "part", "as for", "-e gelince", 1),
 "adhdhaba": G("adhdhaba", "عَذَّبَ", "ع ذ ب", "verb", "to punish, to torment (Form II)", "azap etmek (tef'îl)", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment, torment", "azap", 1),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "intense, severe, strong", "şiddetli, güçlü", 1),
 "dunya": G("dunya", "الدُّنْيَا", "د ن و", "noun", "this world", "dünya", 1),
 "akhira": G("akhira", "آخِرَة", "أ خ ر", "noun", "the Hereafter", "âhiret", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā)", "değil, yok (nefiy mâ'sı)", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "nasir-helper": G("nasir-helper", "نَاصِر", "ن ص ر", "noun", "a helper (an active participle)", "yardım eden (ism-i fâil)", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to do, to work", "yapmak, çalışmak", 1),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous (an active participle)", "sâlih (ism-i fâil)", 1),
 "waffa": G("waffa", "وَفَّى", "و ف ي", "verb", "to pay in full (Form II, defective)", "tam olarak vermek (tef'îl, nâkıs)", 2),
 "ajr": G("ajr", "أَجْر", "أ ج ر", "noun", "a reward, a wage", "mükâfat, ecir", 1, plural="أُجُور"),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "ahabba": G("ahabba", "أَحَبَّ", "ح ب ب", "verb", "to love (Form IV, doubled)", "sevmek (if'âl, muzâaf)", 1),
 "zalim": G("zalim", "ظَالِم", "ظ ل م", "noun", "a wrongdoer (an active participle)", "zâlim (ism-i fâil)", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "tala-recite": G("tala-recite", "تَلَا", "ت ل و", "verb", "to recite (defective)", "okumak, tilâvet etmek (nâkıs)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "dhikr": G("dhikr", "ذِكْر", "ذ ك ر", "noun", "remembrance; the Reminder", "zikir, anma", 1),
 "hakim": G("hakim", "حَكِيم", "ح ك م", "noun", "wise", "hakîm, hikmetli", 1),
 "mathal": G("mathal", "مَثَل", "م ث ل", "noun", "a likeness; a parable", "misal, durum; mesel", 1),
 "inda": G("inda", "عِنْدَ", None, "noun", "with, at, in the presence of", "yanında, katında", 1),
 "ka": G("ka", "كَ", None, "prep", "like, as", "gibi", 1),
 "adam-prophet": G("adam-prophet", "آدَم", None, "propn", "Ādam (Adam)", "Âdem", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1),
 "turab": G("turab", "تُرَاب", "ت ر ب", "noun", "dust, earth", "toprak", 1),
 "haqq": G("haqq", "الْحَقّ", "ح ق ق", "noun", "the truth; a right", "hak, gerçek", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "do not (the prohibiting lā)", "-ma (nehiy lâ'sı)", 1),
 "mumtari": G("mumtari", "مُمْتَرٍ", "م ر ي", "noun", "a doubter (an active participle of Form VIII, manqūṣ)", "şüphe eden (iftiâl'in mankûs ism-i fâili)", 3),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "waffa", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "وَفَّ", "وَفّ", "i", "وَفّ", "تَوْفِيَة", "مُوَفٍّ (الْمُوَفِّي)", "مُوَفًّى", "وُفِّيَ", "يُوَفَّى", "وَفَّاهُ حَقَّهُ: أَعْطَاهُ إِيَّاهُ وَافِيًا — نَاقِصٌ: يُوَفِّي، لَمْ يُوَفِّ."))
put_morph(mo, "tala-recite", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "تَلَ", "تْل", "u", "اُتْل", "تِلَاوَة", "تَالٍ (التَّالِي)", "مَتْلُوّ", "تُلِيَ", "يُتْلَى", "تَلَا الْكِتَابَ يَتْلُوهُ: قَرَأَهُ — نَاقِصٌ وَاوِيٌّ؛ لَمْ يَتْلُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch33 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 33 (print pp. 48–49; ʿĪsā §12 closes): Āl ʿImrān 3:55 «I shall take you and raise you to Me» — the participles annexed to the kāf (s1); 3:56 the unbelievers punished (s2); 3:57 the believers paid in full (s3); 3:58–60 «this We recite to you», the likeness of ʿĪsā and Ādam, «the truth is from your Lord» (s4)."
ADD_TR = " Otuz üçüncü bölüm (baskı s. 48–49; Îsâ §12 kapanır): Âl-i İmrân 55 «seni vefat ettirip katıma yükselteceğim» — kâf'a muzâf ism-i fâiller (s1); 56 inkârcıların azabı (s2); 57 müminlere tam mükâfat (s3); 58–60 «bunu sana okuyoruz», Îsâ ile Âdem'in durumu, «hak Rabbindendir» (s4)."
write_out(33, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā 3:55–60", GLOSS_ADD, notes=(), related=())
report(33, S, GLOSS_ADD, ())
