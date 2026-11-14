# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 26: «الْعَاصِفَة» §11 الْعَذَابُ (ʿĀd waited for rain every day and saw no scrap of cloud; one day they saw a cloud coming and rejoiced, shouting and dancing: «a rain-cloud!»; but Hūd understood that the punishment had come: «this is no cloud of mercy, but a wind with a painful punishment in it»; and so it was — a wind blew the like of which no one had seen or heard, uprooting trees, demolishing houses, carrying off the beasts; the desert sands flew, the world went dark, terror entered them, they shut their doors, children clung to mothers, people to walls, children weeping, women screaming, men crying for help — «no protector today from God's command» (11:43); seven nights and eight days; the people died and lay like fallen palm trunks, the birds eating the dead, the owls living in the ruined houses; Hūd and the believers were saved by their faith, ʿĀd perished by its unbelief and obstinacy — «ʿĀd disbelieved in their Lord; away with ʿĀd, the people of Hūd» — 11:60; the END of «the storm»). Print pp. 47–49.
python3 tools/authoring/author_qisas2_ch26.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْعَاصِفَةُ: الْعَذَابُ", "en": "The storm: the punishment", "tr": "Fırtına: azap"}
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

# ---------------------------------------------------------------- §11 الْعَذَابُ (print pp. 47–49)
sen("s1", "And ʿĀd awaited the rain every day and looked to the sky, but saw not a scrap of cloud.", "Âd her gün yağmuru bekliyor, göğe bakıyor, fakat bir bulut parçası bile görmüyordu.", [
  kana(),
  aad("raf", "اسْمُ كَانَ", "«ʿĀd» — kāna's ism", "«Âd» — kâne'nin ismi", tags=[KN]),
  khamsa("يَنْتَظِرُونَ", "intazara", "«awaited»", "«bekliyorlardı»", tags=[KN, "form-viii-verbs", MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْجَمْعُ عَلَى الْمَعْنَى"),
  maful("الْمَطَرَ", "matar", "«the rain»", "«yağmuru»"),
  tok("كُلَّ", "kull", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (بِالْإِضَافَةِ إِلَى الظَّرْفِ)، مُضَافٌ.", "«every» — a time adverbial by annexation.", "«her» — izafetle zaman zarfı."),
  mudaf_ilayh("يَوْمٍ", "yawm", "«day»", "«gün»"),
  khamsa_wa("وَيَنْظُرُونَ", "nazara", "«and looked»", "«ve bakıyorlardı»"),
  ila_(),
  majrur("السَّمَاءِ", "sama", "«the sky»", "«göğe»"),
  tok("فَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«but … not»", "«fakat … -mez»", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("يَرَوْنَ", "raa", "verb", [AK, "la-nafiya", "naqis-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ)، وَالْوَاوُ فَاعِلٌ.", "«they saw» — the defective verb before the group's wāw.", "«görmüyorlardı» — cemi vâvı önünde nâkıs fiil."),
  tok("قِطْعَةَ", "qita", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«a scrap [of]» — the object, annexed.", "«bir parçasını» — mef'ûl, muzâf."),
  mudaf_ilayh("سَحَابٍ", "sahab", "«cloud»", "«bulut»", punct="."),
])
sen("s2", "And they were in need of rain, and they had a great longing for the rain.", "Yağmura muhtaçtılar; yağmura büyük bir özlemleri vardı.", [
  kana_pl(),
  fi(),
  majrur("حَاجَةٍ", "haja", "«need» — the phrase is kāna's khabar.", "«ihtiyaçta» — câr-mecrûr kâne'nin haberi.", tags=[KN]),
  *ila_matar(punct="،"),
  kana(),
  tok("لَهُمْ", "li", "prep", [HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَهُمْ فِي مَحَلِّ جَرٍّ — خَبَرُ كَانَ مُقَدَّمٌ.", "«to them» — kāna's fronted khabar.", "«onların» — kâne'nin öne alınmış haberi.", segments=[seg("لَ", "li", "prep"), seg("هُمْ", "pron-3mp", "pron")]),
  ism_kana("شَوْقٌ", "shawq", "«a longing»", "«bir özlem»", ar="اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ."),
  naat("عَظِيمٌ", "azim", "«great»", "«büyük»", case="raf"),
  *ila_matar(punct="."),
])
sen("s3", "One day they saw a cloud coming towards them, and they rejoiced greatly.", "Bir gün kendilerine doğru gelen bir bulut gördüler ve çok sevindiler.", [
  tok("ذَاتَ", "dhat", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ (ذَاتَ يَوْمٍ: يَوْمًا مِنَ الْأَيَّامِ).", "«one» (day) — a time adverbial, annexed.", "«bir» (gün) — zaman zarfı, muzâf."),
  mudaf_ilayh("يَوْمٍ", "yawm", "«day»", "«gün»"),
  mazi_wa_alif("رَأَوْا", "raa", "«they saw»", "«gördüler»", tags=[MB]),
  maful("سَحَابَةً", "sahaba-cloud", "«a cloud»", "«bir bulut»"),
  tok("تَأْتِي", "ata", "verb", [NA, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِسَحَابَةً.", "«coming» — a ṣifa of «a cloud».", "«gelen» — «bulut»un sıfatı."),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«towards them»", "«kendilerine doğru»", punct="،"),
  mazi_pl("فَفَرِحُوا", "fariha", "«and they rejoiced»", "«ve sevindiler»", tags=[AT], wa=True),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«greatly»", "«çok»", punct="."),
])
sen("s4", "And they shouted: this is a rain-cloud! this is a rain-cloud.", "Bağırdılar: bu bir yağmur bulutu! bu bir yağmur bulutu.", [
  mazi_pl("وَصَاحُوا", "saha-shout", "«and they shouted»", "«ve bağırdılar»", tags=[AT, "hollow-verbs", MB], wa=True, punct=":"),
  *sahabat_matar("!"),
  *sahabat_matar("."),
])
sen("s5", "And the people danced for joy, and called to one another, saying: a rain-cloud! a rain-cloud!", "İnsanlar sevinçten oynadı, birbirlerine seslenip dediler: yağmur bulutu! yağmur bulutu!", [
  mazi("وَرَقَصَ", "raqasa", "«and … danced»", "«ve oynadı»", tags=[AT], hidden=None, wa=True),
  nas_fail_(),
  tok("فَرَحًا", "farah", "noun", ["maful-mutlaq"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«for joy» — the object of reason.", "«sevinçten» — mef'ûlün lieclih.", punct="،"),
  tok("وَنَادَى", "nada", "verb", [AT, "naqis-verbs", "form-iii-verbs", MB], "الْوَاوُ عَاطِفَةٌ، وَنَادَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and … called»", "«ve seslendi»", segments=wa_("نَادَى", "nada", "verb")),
  noun_pron("بَعْضُهُمْ", "baad", "بَعْضُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«some of them» — the doer.", "«kimileri» — fâil.", tags=[FL, ID]),
  maful("بَعْضًا", "baad", "«others»", "«kimilerine»"),
  qalu("وَقَالُوا", wa=True),
  *sahabat_matar_bare("!"),
  *sahabat_matar_bare("!"),
])
sen("s6", "But Hūd understood that the punishment had come.", "Fakat Hûd azabın geldiğini anladı.", [
  tok("وَلٰكِنَّ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«but»", "«fakat»", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  tok("هُودًا", "hud-prophet", "propn", [IW], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Hūd» — lākinna's ism.", "«Hûd» — lâkinne'nin ismi."),
  mazi("فَهِمَ", "fahima", "«understood»", "«anladı»", tags=[IW, MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  anna(obj_of="فَهِمَ"),
  ism_inna("الْعَذَابَ", "adhab", "«the punishment»", "«azabın»", part="أَنَّ"),
  tok("قَدْ", "qad", "part", [IW], "حَرْفُ تَحْقِيقٍ.", "«indeed»", "«gerçekten»"),
  mazi("جَاءَ", "jaa", "«had come»", "«geldi»", tags=[IW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", punct="."),
])
sen("s7", "And Hūd said to them: this is not a cloud of mercy; rather it is a wind with a painful punishment in it.", "Hûd onlara dedi: bu bir rahmet bulutu değil; bilakis o, içinde acı bir azap bulunan bir rüzgârdır.", [
  qala("وَقَالَ", wa=True, punct=None),
  la_hum(),
  hud_fail(punct=":"),
  laysa_tok(),
  tok("هٰذَا", "hadha", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ لَيْسَ.", "«this» — laysa's ism.", "«bu» — leyse'nin ismi."),
  tok("سَحَابَ", "sahab", "noun", [KN, ID], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«a cloud [of]» — laysa's khabar, annexed.", "«bulutu» — leyse'nin haberi, muzâf."),
  mudaf_ilayh("رَحْمَةٍ", "rahma", "«mercy»", "«rahmet»", punct="،"),
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ وَعَطْفٍ.", "«rather»", "«bilakis»"),
  pron_mubtada("هُوَ", "huwa", "«it»", "«o»"),
  khabar("رِيحٌ", "rih", "«[is] a wind»", "«bir rüzgârdır»"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it» — a fronted khabar of the clause that is a ṣifa of «a wind».", "«içinde» — «rüzgâr»ın sıfatı olan cümlenin öne alınmış haberi.", tags=[MK, NA], extra_ar=" — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِفَةٌ لِرِيحٌ"),
  tok("عَذَابٌ", "adhab", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a punishment» — the delayed mubtadaʾ.", "«bir azap» — sonraya bırakılmış mübtedâ."),
  naat("أَلِيمٌ", "alim-painful", "«painful»", "«acı»", case="raf", punct="."),
])
sen("s8", "And so it was: a violent wind blew, the like of which people had never seen, nor had people heard of its like.", "Öyle de oldu: insanların benzerini görmediği ve benzerini işitmediği şiddetli bir rüzgâr esti.", [
  kana(),
  tok("كَذٰلِكَ", "kadhalika", "part", [HJ, KN, "asma-al-ishara"], "الْكَافُ حَرْفُ جَرٍّ وَذٰلِكَ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ (الْأَمْرُ).", "«so» — the phrase is kāna's khabar; its ism «it (the matter)» is concealed.", "«öyle» — câr-mecrûr kâne'nin haberi; ismi gizli (durum).", punct="،"),
  tok("فَقَدْ", "qad", "part", [AT], "الْفَاءُ لِلتَّعْلِيلِ (عَاطِفَةٌ)، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«for indeed»", "«zira gerçekten»", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi_ta("هَبَّتْ", "habba-blow", "«… blew»", "«esti»", tags=["doubled-verbs"]),
  fail("رِيحٌ", "rih", "«a wind»", "«bir rüzgâr»"),
  naat("شَدِيدَةٌ", "shadid", "«violent»", "«şiddetli»", case="raf"),
  tok("مَا", "ma-nafiya", "part", ["la-nafiya", NA], "مَا نَافِيَةٌ — وَالْجُمْلَةُ بَعْدَهَا صِفَةٌ ثَانِيَةٌ لِرِيحٌ.", "«not» — the clause after it is a second ṣifa of «a wind».", "«-medi» — sonraki cümle «rüzgâr»ın ikinci sıfatı."),
  tok("رَأَى", "raa", "verb", ["la-nafiya", "naqis-verbs", MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ بَعْدَهُ.", "«had seen» — the defective māḍī; the doer follows.", "«görmedi» — nâkıs mâzî; fâil sonra."),
  nas_fail_(),
  noun_pron("مِثْلَهَا", "mithl", "مِثْلَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its like» — the object.", "«benzerini» — mef'ûl.", tags=[MB, ID], punct="،"),
  tok("وَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and … not»", "«ve … -medi»", segments=wa_("مَا", "ma-nafiya", "part")),
  mazi("سَمِعَ", "samia", "«had heard»", "«işitmedi»", tags=["la-nafiya"], hidden=None, extra_ar="، وَالْفَاعِلُ بَعْدَهُ"),
  nas_fail_(),
  tok("بِمِثْلِهَا", "mithl", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَمِثْلِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of its like»", "«benzerini»", segments=[seg("بِ", "bi", "prep"), seg("مِثْلِ", "mithl", "noun"), seg("هَا", "pron-3fs", "pron")], punct="."),
])
sen("s9", "And the storm blew, uprooting the trees, demolishing the houses, carrying the beasts and throwing them to a far place.", "Fırtına esti; ağaçları söküyor, evleri yıkıyor, hayvanları taşıyıp uzak bir yere atıyordu.", [
  mazi_ta("وَهَبَّتِ", "habba-blow", "«and … blew»", "«ve esti»", tags=[AT, "doubled-verbs"], wa=True, extra="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الْعَاصِفَةُ", "asifa", "«the storm»", "«fırtına»"),
  tok("تَقْلَعُ", "qalaa-uproot", "verb", [HL, "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«uprooting» — the clause is a ḥāl.", "«sökerek» — cümle hâl."),
  maful("الْأَشْجَارَ", "shajar", "«the trees»", "«ağaçları»", tags=[JT]),
  *wa_tafal("وَتَهْدِمُ", "hadama", "«and demolishing»", "«ve yıkarak»", "الْبُيُوتَ", "bayt", "«the houses»", "«evleri»", obj_tags=[JT]),
  *wa_tafal("وَتَحْمِلُ", "hamala", "«and carrying»", "«ve taşıyarak»", "الدَّوَابَّ", "dabba", "«the beasts»", "«hayvanları»", obj_tags=[JT]),
  tok("وَتَرْمِيهَا", "rama", "verb", [AT, "mudari-marfu", MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَرْمِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَهَا مَفْعُولٌ بِهِ.", "«and throwing them» — the defective muḍāriʿ with its object.", "«ve onları atarak» — nâkıs muzâri, mef'ûl bitişik.", segments=[seg("وَ", "wa", "conj"), seg("تَرْمِي", "rama", "verb"), seg("هَا", "pron-3fs", "pron")]),
  ila_(),
  majrur("مَكَانٍ", "makan", "«a place»", "«bir yere»"),
  naat("بَعِيدٍ", "baid", "«far»", "«uzak»", punct="."),
])
sen("s10", "And the sands of the desert flew, and the world went dark, so that no one could see anything.", "Çölün kumları uçtu, dünya karardı; insan hiçbir şey göremiyordu.", [
  mazi_ta("وَطَارَتْ", "tara", "«and … flew»", "«ve uçtu»", tags=[AT, "hollow-verbs"], wa=True),
  tok("رِمَالُ", "raml", "noun", [FL, ID, JT], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — جَمْعُ رَمْلٍ.", "«the sands [of]» — the doer.", "«kumları» — fâil."),
  mudaf_ilayh("الصَّحْرَاءِ", "sahra", "«the desert»", "«çölün»"),
  mazi_ta("وَأَظْلَمَتِ", "azlama", "«and … went dark»", "«ve karardı»", tags=[AT, "form-iv-verbs"], wa=True, extra="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  tok("الدُّنْيَا", "dunya", "noun", [FL, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the world» — the doer; its ḍamma is estimated.", "«dünya» — fâil; zammesi takdîrî."),
  tok("فَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَلَا نَافِيَةٌ.", "«so that … not»", "«artık … -mez»", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  neg_mudari("يَرَى", "raa", "«could see»", "«göremiyordu»", hidden=None, tags=["naqis-verbs", MB], extra="، وَالْفَاعِلُ بَعْدَهُ — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ"),
  fail("الْإِنْسَانُ", "insan", "«a person»", "«insan»"),
  maful("شَيْئًا", "shay", "«anything»", "«hiçbir şey»", punct="."),
])
sen("s11", "And terror entered them, so they went into their houses and shut their doors.", "Onlara dehşet girdi; evlerine girip kapılarını kapadılar.", [
  tok("وَدَخَلَهُمُ", "dakhala", "verb", [AT, MB], "الْوَاوُ عَاطِفَةٌ، وَدَخَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَهُمُ مَفْعُولٌ بِهِ (حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ)، وَالْفَاعِلُ بَعْدَهُ.", "«and … entered them» — the object aboard; the doer follows.", "«ve onlara girdi» — mef'ûl bitişik; fâil sonra.", segments=[seg("وَ", "wa", "conj"), seg("دَخَلَ", "dakhala", "verb"), seg("هُمُ", "pron-3mp", "pron")]),
  fail("الرُّعْبُ", "rub", "«terror»", "«dehşet»"),
  mazi_pl("فَدَخَلُوا", "dakhala", "«so they entered»", "«girdiler»", tags=[AT, MB], wa=True),
  noun_pron("بُيُوتَهُمْ", "bayt", "بُيُوتَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their houses» — the object.", "«evlerine» — mef'ûl.", tags=[MB, ID, JT]),
  mazi_pl("وَأَغْلَقُوا", "aghlaqa", "«and shut»", "«ve kapadılar»", tags=[AT, "form-iv-verbs", MB], wa=True),
  noun_pron("أَبْوَابَهَا", "bab", "أَبْوَابَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ بَابٍ.", "«their doors» — the object.", "«kapılarını» — mef'ûl.", tags=[MB, ID, JT], punct="."),
])
sen("s12", "And the children clung to the mothers, and the people clung to the walls, and the people went into the inner rooms.", "Çocuklar annelere sarıldı, insanlar duvarlara sarıldı ve insanlar odalara girdi.", [
  *itanaqa_("وَاعْتَنَقَ", "الْأَطْفَالُ", "tifl", "«the children»", "«çocuklar»", "بِالْأُمَّهَاتِ", "umm", "«the mothers»", "«annelere»", "،", bi_tags=[JM]),
  *itanaqa_("وَاعْتَنَقَ", "النَّاسُ", "nas", "«the people»", "«insanlar»", "بِالْجُدْرَانِ", "jidar", "«the walls»", "«duvarlara»", "،", subj_tags=()),
  mazi("وَدَخَلَ", "dakhala", "«and … went into»", "«ve girdi»", tags=[AT, MB], hidden=None, wa=True),
  nas_fail_(),
  tok("الْحُجُرَاتِ", "hujra", "noun", [MB, JM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the inner rooms» — the object; the sound feminine plural takes kasra for naṣb.", "«odalara» — mef'ûl; cem-i müennes sâlim nasbda kesre alır.", punct="."),
])
sen("s13", "The children were weeping, the women screaming, the men praying and crying for help.", "Çocuklar ağlıyor, kadınlar çığlık atıyor, erkekler dua edip yardım istiyordu.", [
  *jumla_hal_nominal("الْأَطْفَالُ", "tifl", "«the children»", "«çocuklar»", khamsa("يَبْكُونَ", "baka", "«weeping»", "«ağlıyor»", tags=[MK, "naqis-verbs"], extra_ar=" (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ) — وَالْجُمْلَةُ خَبَرٌ", punct="،")),
  *jumla_hal_nominal("وَالنِّسَاءُ", "nisa", "«the women»", "«kadınlar»", tok("يَصِحْنَ", "saha-shout", "verb", [MK, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ فَاعِلٌ — حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (يَصِيحْنَ → يَصِحْنَ)؛ وَالْجُمْلَةُ خَبَرٌ.", "«screaming» — built on sukūn before the women's nūn; the hollow middle dropped.", "«çığlık atıyor» — nisve nûnu ile sükûn üzere mebnî; ecvef ortası düşmüş.", punct="،"), wa=True),
  *jumla_hal_nominal("وَالرِّجَالُ", "rajul", "«the men»", "«erkekler»", khamsa("يَدْعُونَ", "daa", "«praying»", "«dua ediyor»", tags=[MK, "naqis-verbs"], extra_ar=" (حُذِفَتْ لَامُ الْفِعْلِ: يَدْعُو + ونَ) — وَالْجُمْلَةُ خَبَرٌ"), wa=True),
  khamsa_wa("وَيَسْتَغِيثُونَ", "istaghatha", "«and crying for help»", "«ve yardım istiyordu»", tags=["form-x-verbs", "hollow-verbs"], punct="."),
])
sen("s14", "And it was as if a sayer were saying:", "Sanki bir söyleyen şöyle diyordu:", [
  tok("وَكَأَنَّ", "kaanna", "part", [AT, IW], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ.", "«and as if» — ka-anna.", "«ve sanki» — keenne.", segments=wa_("كَأَنَّ", "kaanna", "part")),
  ism_inna("قَائِلًا", "qail", "«a sayer»", "«bir söyleyen»", part="كَأَنَّ", tags=["ism-fail"]),
  mudari("يَقُولُ", "qala", "«were saying»", "«diyordu»", tags=[IW, "hollow-verbs", MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَأَنَّ", punct=":"),
])
sen("s15", "«There is no protector today from the command of God» (11:43).", "«Bugün Allah'ın emrinden koruyacak yoktur» (11:43).", [
  *quran([
    la_jins("لَا"),
    ism_la("عَاصِمَ", "asim-protector", "«protector»", "«koruyucu»", khabar="مَوْجُودٌ"),
    tok("الْيَوْمَ", "yawm", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«today»", "«bugün»"),
    prep("مِنْ", "min", "«from»", "«-den»"),
    tok("أَمْرِ", "amr", "noun", [HJ, ID], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«the command [of]»", "«emrinden»"),
    allah_mi(punct="."),
  ]),
])
sen("s16", "That was seven nights and eight days.", "Bu, yedi gece ve sekiz gün sürdü.", [
  kana("كَانَ", wa=False),
  tok("ذٰلِكَ", "dhalika", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«that» — kāna's ism.", "«bu» — kâne'nin ismi."),
  tok("سَبْعَ", "sab-seven", "noun", [MF, ID, KN], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (خَبَرُ كَانَ)، مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُخَالِفُ الْمَعْدُودَ فِي التَّأْنِيثِ.", "«seven» — a time adverbial as kāna's khabar; the numbers three to ten take the opposite gender of what they count.", "«yedi» — kâne'nin haberi olan zaman zarfı; üçten ona kadar sayılar ma'dûdun tersi cinste."),
  tok("لَيَالٍ", "layla", "noun", [ID, JT, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — جَمْعُ لَيْلَةٍ، مَنْقُوصٌ.", "«nights» — the mudaf ilayh; a manqūṣ plural whose yāʾ drops.", "«gece» — muzâfun ileyh; yâ'sı düşen mankûs çoğul."),
  tok("وَثَمَانِيَةَ", "thamaniya", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَثَمَانِيَةَ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«and eight» — joined, annexed.", "«ve sekiz» — ma'tûf, muzâf.", segments=wa_("ثَمَانِيَةَ", "thamaniya", "noun")),
  tok("أَيَّامٍ", "yawm", "noun", [ID, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ يَوْمٍ.", "«days»", "«gün»", punct="."),
])
sen("s17", "And the people died and were like trunks of palm trees fallen on the ground; it was a very strange sight — the people dead, the birds eating them, the houses ruined, the owls dwelling in them.", "İnsanlar öldü ve yere düşmüş hurma kütükleri gibi oldular; çok garip bir manzaraydı: insanlar ölü, kuşlar onları yiyor; evler harap, baykuşlar oralarda oturuyor.", [
  mazi("وَمَاتَ", "mata-die", "«and … died»", "«ve öldü»", tags=[AT, "hollow-verbs"], hidden=None, wa=True),
  fail("الْقَوْمُ", "qawm", "«the people»", "«kavim»"),
  tok("فَكَانُوا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا.", "«and they were» — kāna; the wāw is its ism.", "«ve oldular» — kâne; vâv ismi.", segments=[seg("فَ", "fa", "conj"), seg("كَانُوا", "kana", "verb")]),
  tok("كَأَشْجَارِ", "shajar", "noun", [HJ, KN, ID, JT], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَأَشْجَارِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانُوا.", "«like trunks [of]» — the phrase is kāna's khabar.", "«kütükleri gibi» — câr-mecrûr kâne'nin haberi.", segments=[seg("كَ", "ka", "prep"), seg("أَشْجَارِ", "shajar", "noun")]),
  mudaf_ilayh("النَّخِيلِ", "nakhil", "«palm trees»", "«hurma»"),
  mazi_ta("سَقَطَتْ", "saqata", "«fallen»", "«düşmüş»", tags=[NA], extra="، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ صِفَةٌ لِأَشْجَارِ (أَوْ حَالٌ)"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("الْأَرْضِ", "ard", "«the ground»", "«yere»"),
  kana(),
  khabar_kana("مَنْظَرًا", "manzar", "«a sight»", "«bir manzara»", ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ (الْأَمْرُ)."),
  naat("غَرِيبًا", "gharib", "«strange»", "«garip»", case="nasb"),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very»", "«çok»", punct="،"),
  tok("النَّاسُ", "nas", "noun", [MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ تَفْسِيرٌ لِلْمَنْظَرِ.", "«the people» — the mubtadaʾ; the clause spells out the sight.", "«insanlar» — mübtedâ; cümle manzarayı açıklar."),
  khabar("أَمْوَاتٌ", "mayt", "«[are] dead»", "«ölüdür»", tags=[JT]),
  tok("يَأْكُلُهُمُ", "akala", "verb", [HL, "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُمُ مَفْعُولٌ بِهِ مُقَدَّمٌ (حُرِّكَتِ الْمِيمُ بِالضَّمِّ)، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ حَالٌ.", "«the birds eating them» — the object aboard; the clause is a ḥāl.", "«kuşlar onları yiyor» — mef'ûl bitişik; cümle hâl.", segments=[seg("يَأْكُلُ", "akala", "verb"), seg("هُمُ", "pron-3mp", "pron")]),
  fail("الطَّيْرُ", "tayr", "«the birds»", "«kuşlar»", punct="،"),
  tok("وَالْبُيُوتُ", "bayt", "noun", [AT, MK, JT], "الْوَاوُ عَاطِفَةٌ، وَالْبُيُوتُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and the houses» — the mubtadaʾ.", "«ve evler» — mübtedâ.", segments=wa_("الْبُيُوتُ", "bayt", "noun")),
  khabar("خَرَابٌ", "kharab", "«[are] a ruin»", "«haraptır»", tags=["masdar"]),
  tok("يَسْكُنُهَا", "sakana", "verb", [HL, "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ حَالٌ.", "«the owls dwelling in them» — the clause is a ḥāl.", "«baykuşlar oralarda oturuyor» — cümle hâl.", segments=[seg("يَسْكُنُ", "sakana", "verb"), seg("هَا", "pron-3fs", "pron")]),
  fail("الْبُومُ", "bum", "«the owls»", "«baykuşlar»", punct="."),
])
sen("s18", "And Hūd and the believers were saved by their faith, and ʿĀd perished by its unbelief and its obstinacy.", "Hûd ve müminler imanlarıyla kurtuldu; Âd küfrü ve inadıyla helâk oldu.", [
  tok("وَنَجَا", "naja-escape", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَنَجَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and … was saved» — the defective māḍī.", "«ve kurtuldu» — nâkıs mâzî.", segments=wa_("نَجَا", "naja-escape", "verb")),
  hud_fail(),
  tok("وَالْمُؤْمِنُونَ", "mumin", "noun", [AT, JS, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَالْمُؤْمِنُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the believers» — joined; rafʿ by the wāw.", "«ve müminler» — ma'tûf; vâv ile merfû.", segments=wa_("الْمُؤْمِنُونَ", "mumin", "noun")),
  tok("بِإِيمَانِهِمْ", "iman", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَإِيمَانِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«by their faith» — the bāʾ of cause.", "«imanlarıyla» — sebep bâ'sı.", segments=[seg("بِ", "bi", "prep"), seg("إِيمَانِ", "iman", "noun"), seg("هِمْ", "pron-3mp", "pron")], punct="،"),
  mazi_ta("وَهَلَكَتْ", "halaka", "«and … perished»", "«ve helâk oldu»", tags=[AT], wa=True),
  aad("raf", "فَاعِلٌ", "«ʿĀd» — the doer", "«Âd» — fâil", tags=[FL]),
  tok("بِكُفْرِهَا", "kufr", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَكُفْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«by its unbelief»", "«küfrüyle»", segments=[seg("بِ", "bi", "prep"), seg("كُفْرِ", "kufr", "noun"), seg("هَا", "pron-3fs", "pron")]),
  pron_atf("وَعِنَادِهَا", "inad", "عِنَادِ", "هَا", "pron-3fs", "«its obstinacy»", "«ve inadıyla»", case="jarr", punct="."),
])
sen("s19", "«Behold, ʿĀd disbelieved in their Lord; behold, away with ʿĀd, the people of Hūd» (11:60).", "«Bilin ki Âd Rablerini inkâr etti; bilin ki Âd — Hûd'un kavmi — rahmetten uzak olsun» (11:60).", [
  *quran([
    tok("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "أَلَا حَرْفُ تَنْبِيهٍ وَاسْتِفْتَاحٍ.", "«behold» — the particle of alerting that opens a sentence.", "«bilin ki» — tenbih ve istiftah harfi."),
    inna(),
    aad("nasb", "اسْمُ إِنَّ", "«ʿĀd» — inna's ism", "«Âd» — inne'nin ismi", tags=[IW]),
    mazi_pl("كَفَرُوا", "kafara", "«disbelieved»", "«inkâr etti»", tags=[IW, MB]),
    noun_pron("رَبَّهُمْ", "rabb", "رَبَّ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ (كَفَرَ هُنَا مُتَعَدٍّ بِنَفْسِهِ)، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — وَجُمْلَةُ كَفَرُوا خَبَرُ إِنَّ.", "«their Lord» — the object (kafara here takes a direct object); the clause is inna's khabar.", "«Rablerini» — mef'ûl; cümle inne'nin haberi.", tags=[MB, ID], punct="،"),
    tok("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "حَرْفُ تَنْبِيهٍ وَاسْتِفْتَاحٍ.", "«behold»", "«bilin ki»"),
    tok("بُعْدًا", "bud-perdition", "noun", ["maful-mutlaq", "hadhf-wa-taqdir"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (بَعُدَتْ بُعْدًا) مَنْصُوبٌ بِالْفَتْحَةِ — دُعَاءٌ عَلَيْهِمْ.", "«away with» — an absolute object of an understood verb; a curse.", "«uzak olsun» — mahzuf fiilin mef'ûl-i mutlakı; beddua."),
    tok("لِعَادٍ", "aad", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَعَادٍ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«for ʿĀd»", "«Âd'a»", segments=[seg("لِ", "li", "prep"), seg("عَادٍ", "aad", "propn")]),
    tok("قَوْمِ", "qawm", "noun", [BD, ID], "بَدَلٌ مِنْ عَادٍ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«the people [of]» — a badal of ʿĀd.", "«kavmi» — Âd'ın bedeli."),
    hud_ma(punct="."),
  ]),
])

CAND = {
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak", 1),
 "aad": G("aad", "عَاد", None, "propn", "ʿĀd — the ancient people of Hūd", "Âd", 1),
 "intazara": G("intazara", "اِنْتَظَرَ", "ن ظ ر", "verb", "to await", "beklemek", 1),
 "matar": G("matar", "مَطَر", "م ط ر", "noun", "rain", "yağmur", 1, plural="أَمْطَار"),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "every, all", "her", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "day", "gün", 1, plural="أَيَّام"),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look", "bakmak", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "sky", "gök", 1),
 "fa": G("fa", "فَ", None, "conj", "so, but", "fakat, bu yüzden", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not", "değil, -mez", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "qita": G("qita", "قِطْعَة", "ق ط ع", "noun", "a piece, a scrap", "parça", 1, plural="قِطَع"),
 "sahab": G("sahab", "سَحَاب", "س ح ب", "noun", "clouds (a collective)", "bulut (cins ismi)", 1, plural="سُحُب"),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "haja": G("haja", "حَاجَة", "ح و ج", "noun", "need", "ihtiyaç", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onlar (bitişik)", 1),
 "shawq": G("shawq", "شَوْق", "ش و ق", "noun", "longing, yearning", "özlem, şevk", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great, mighty", "büyük, azametli", 1),
 "dhat": G("dhat", "ذَات", None, "noun", "possessor of; ذَاتَ يَوْمٍ: one day", "sahibi; zâte yevmin: bir gün", 1),
 "sahaba-cloud": G("sahaba-cloud", "سَحَابَة", "س ح ب", "noun", "a cloud (the unit of سَحَاب)", "bir bulut (sehâb'ın tekili)", 1, plural="سَحَابَات"),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come", "gelmek", 1),
 "fariha": G("fariha", "فَرِحَ", "ف ر ح", "verb", "to rejoice", "sevinmek", 1),
 "jiddan": G("jiddan", "جِدًّا", "ج د د", "noun", "very", "çok", 1),
 "saha-shout": G("saha-shout", "صَاحَ", "ص ي ح", "verb", "to shout, to scream (hollow)", "bağırmak, çığlık atmak (ecvef)", 1),
 "hadhihi": G("hadhihi", "هَذِهِ", None, "pron", "this (fem.)", "bu (dişil)", 1),
 "raqasa": G("raqasa", "رَقَصَ", "ر ق ص", "verb", "to dance", "oynamak, dans etmek", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "farah": G("farah", "فَرَح", "ف ر ح", "noun", "joy", "sevinç", 1),
 "nada": G("nada", "نَادَى", "ن د و", "verb", "to call out", "seslenmek", 1),
 "baad": G("baad", "بَعْض", "ب ع ض", "noun", "some", "bazı, kimi", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "lakinna": G("lakinna", "لٰكِنَّ", None, "part", "but", "fakat", 1),
 "hud-prophet": G("hud-prophet", "هُود", None, "propn", "Hūd — the prophet sent to ʿĀd", "Hûd", 1),
 "fahima": G("fahima", "فَهِمَ", "ف ه م", "verb", "to understand", "anlamak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that", "ki", 1),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment", "azap", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed", "gerçekten", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not", "değildir", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this", "bu", 1),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "bal": G("bal", "بَلْ", None, "part", "rather", "bilakis", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "rih": G("rih", "رِيح", "ر و ح", "noun", "wind", "rüzgâr", 1, plural="رِيَاح"),
 "pron-3fs": G("pron-3fs", "ـهَا", None, "pron", "her / it / them (attached)", "onu, onları (dişil)", 1),
 "alim-painful": G("alim-painful", "أَلِيم", "أ ل م", "noun", "painful", "acı, elîm", 1),
 "kadhalika": G("kadhalika", "كَذَلِكَ", None, "part", "likewise, so", "öyle, böyle", 1),
 "habba-blow": G("habba-blow", "هَبَّ", "ه ب ب", "verb", "to blow (of wind; doubled: هَبَّ يَهُبُّ)", "esmek (rüzgâr; muzâaf: hebbe yehubbu)", 1),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "violent, severe", "şiddetli", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not", "değil, -medi", 1),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "the like of", "benzer, gibi", 1, plural="أَمْثَال"),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear", "işitmek", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "asifa": G("asifa", "عَاصِفَة", "ع ص ف", "noun", "storm, gale", "fırtına", 1, plural="عَوَاصِف"),
 "qalaa-uproot": G("qalaa-uproot", "قَلَعَ", "ق ل ع", "verb", "to uproot, to pull out", "sökmek", 1),
 "shajar": G("shajar", "شَجَر", "ش ج ر", "noun", "trees (a collective)", "ağaç (cins ismi)", 1, plural="أَشْجَار"),
 "hadama": G("hadama", "هَدَمَ", "ه د م", "verb", "to demolish", "yıkmak", 1),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "house", "ev", 1, plural="بُيُوت"),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry", "taşımak", 1),
 "dabba": G("dabba", "دَابَّة", "د ب ب", "noun", "beast, animal", "hayvan, davar", 1, plural="دَوَابّ"),
 "rama": G("rama", "رَمَى", "ر م ي", "verb", "to throw", "atmak", 1),
 "makan": G("makan", "مَكَان", "ك و ن", "noun", "place", "yer", 1),
 "baid": G("baid", "بَعِيد", "ب ع د", "noun", "far", "uzak", 1),
 "tara": G("tara", "طَارَ", "ط ي ر", "verb", "to fly (hollow)", "uçmak (ecvef)", 1),
 "raml": G("raml", "رَمْل", "ر م ل", "noun", "sand", "kum", 1, plural="رِمَال"),
 "sahra": G("sahra", "صَحْرَاء", "ص ح ر", "noun", "desert", "çöl", 1),
 "azlama": G("azlama", "أَظْلَمَ", "ظ ل م", "verb", "to grow dark (Form IV)", "kararmak (if'âl)", 1),
 "dunya": G("dunya", "الدُّنْيَا", "د ن و", "noun", "the world", "dünya", 1),
 "insan": G("insan", "إِنْسَان", "أ ن س", "noun", "man, human being", "insan", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "rub": G("rub", "رُعْب", "ر ع ب", "noun", "terror, dread", "dehşet, korku", 1),
 "aghlaqa": G("aghlaqa", "أَغْلَقَ", "غ ل ق", "verb", "to shut, to lock (Form IV)", "kapamak, kilitlemek (if'âl)", 1),
 "bab": G("bab", "بَاب", "ب و ب", "noun", "door", "kapı", 1, plural="أَبْوَاب"),
 "itanaqa": G("itanaqa", "اِعْتَنَقَ", "ع ن ق", "verb", "to embrace, to cling to (Form VIII)", "sarılmak, kucaklamak (iftiâl)", 1),
 "tifl": G("tifl", "طِفْل", "ط ف ل", "noun", "child", "çocuk", 1, plural="أَطْفَال"),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "mother", "anne", 1, plural="أُمَّهَات"),
 "jidar": G("jidar", "جِدَار", "ج د ر", "noun", "wall", "duvar", 1, plural="جُدْرَان"),
 "hujra": G("hujra", "حُجْرَة", "ح ج ر", "noun", "room, chamber", "oda, hücre", 1, plural="حُجُرَات"),
 "baka": G("baka", "بَكَى", "ب ك ي", "verb", "to weep", "ağlamak", 1),
 "nisa": G("nisa", "نِسَاء", "ن س و", "noun", "women", "kadınlar", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam, erkek", 1, plural="رِجَال"),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to pray, to call", "dua etmek, çağırmak", 1),
 "istaghatha": G("istaghatha", "اِسْتَغَاثَ", "غ و ث", "verb", "to cry for help (Form X, hollow)", "yardım istemek, imdat dilemek (istif'âl, ecvef)", 1),
 "kaanna": G("kaanna", "كَأَنَّ", None, "part", "as if", "sanki", 1),
 "qail": G("qail", "قَائِل", "ق و ل", "noun", "a sayer", "söyleyen", 1),
 "asim-protector": G("asim-protector", "عَاصِم", "ع ص م", "noun", "a protector", "koruyucu", 1),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "command, matter", "emir, iş", 1, plural="أُمُور"),
 "allah": G("allah", "اللَّه", None, "propn", "Allah", "Allah", 1),
 "dhalika": G("dhalika", "ذَلِكَ", None, "pron", "that", "o, bu", 1),
 "sab-seven": G("sab-seven", "سَبْع", "س ب ع", "noun", "seven", "yedi", 1),
 "layla": G("layla", "لَيْلَة", "ل ي ل", "noun", "night", "gece", 1, plural="لَيَالٍ"),
 "thamaniya": G("thamaniya", "ثَمَانِيَة", "ث م ن", "noun", "eight", "sekiz", 1),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die", "ölmek", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "people", "kavim", 1),
 "ka": G("ka", "كَ", None, "prep", "like", "gibi", 1),
 "nakhil": G("nakhil", "نَخِيل", "ن خ ل", "noun", "palm trees (a collective)", "hurma ağaçları (cins ismi)", 1),
 "saqata": G("saqata", "سَقَطَ", "س ق ط", "verb", "to fall", "düşmek", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "earth, ground", "yer", 1),
 "manzar": G("manzar", "مَنْظَر", "ن ظ ر", "noun", "sight, scene", "manzara", 1),
 "gharib": G("gharib", "غَرِيب", "غ ر ب", "noun", "strange", "garip", 1, plural="غُرَبَاء"),
 "mayt": G("mayt", "مَيْت", "م و ت", "noun", "dead", "ölü", 1, plural="أَمْوَات"),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "tayr": G("tayr", "طَيْر", "ط ي ر", "noun", "birds (a collective)", "kuşlar (cins ismi)", 1, plural="طُيُور"),
 "kharab": G("kharab", "خَرَاب", "خ ر ب", "noun", "ruin, devastation", "harabe, yıkıntı", 1),
 "sakana": G("sakana", "سَكَنَ", "س ك ن", "verb", "to dwell", "oturmak", 1),
 "bum": G("bum", "بُوم", "ب و م", "noun", "owl (a collective)", "baykuş", 1),
 "naja-escape": G("naja-escape", "نَجَا", "ن ج و", "verb", "to be saved", "kurtulmak", 1),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "believer", "mümin", 1, plural="مُؤْمِنُونَ"),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith", "iman", 1),
 "halaka": G("halaka", "هَلَكَ", "ه ل ك", "verb", "to perish", "helâk olmak", 1),
 "kufr": G("kufr", "كُفْر", "ك ف ر", "noun", "unbelief", "küfür", 1),
 "inad": G("inad", "عِنَاد", "ع ن د", "noun", "obstinacy", "inat", 1),
 "ala-tanbih": G("ala-tanbih", "أَلَا (التَّنْبِيه)", None, "part", "behold! (the particle of alerting)", "bilin ki! (tenbih harfi)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve", "inkâr etmek", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "bud-perdition": G("bud-perdition", "بُعْد", "ب ع د", "noun", "distance — بُعْدًا: away with!, a curse", "uzaklık — bu'den: uzak olsun, beddua", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
put_morph(mo, "raqasa", _sg.sound1("nasara", "رَقَص", "رْقُص", "اُرْقُص", "رَقْص", "رَاقِص", None, None, None, "رَقَصَ يَرْقُصُ رَقْصًا: تَحَرَّكَ وَتَمَايَلَ فَرَحًا — لَازِمٌ."))
put_morph(mo, "habba-blow", doubled("nasara", "َ", "هَبّ", "هَبَب", "هُبّ", "هْبُب", ["هُبَّ", "هُبَّا", "هُبُّوا", "هُبِّي", "هُبَّا", "اُهْبُبْنَ"], "هُبُوب", "هَابّ", None, None, None, "هَبَّتِ الرِّيحُ تَهُبُّ هُبُوبًا: ثَارَتْ وَجَرَتْ — مُضَاعَفٌ لَازِمٌ."))
put_morph(mo, "qalaa-uproot", _sg.sound1("fataha", "قَلَع", "قْلَع", "اِقْلَع", "قَلْع", "قَالِع", "مَقْلُوع", "قُلِعَ", "يُقْلَعُ", "قَلَعَ الشَّجَرَةَ يَقْلَعُهَا قَلْعًا: انْتَزَعَهَا مِنْ أَصْلِهَا — يَتَعَدَّى إِلَى مَفْعُولٍ."))
put_morph(mo, "azlama", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَظْلَم", "ظْلِم", "أَظْلِم", "إِظْلَام", "مُظْلِم", None, None, None, "أَظْلَمَ اللَّيْلُ وَالْمَكَانُ يُظْلِمُ إِظْلَامًا: صَارَ مُظْلِمًا — بَابُ الْإِفْعَالِ، لَازِمٌ."))
put_morph(mo, "aghlaqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَغْلَق", "غْلِق", "أَغْلِق", "إِغْلَاق", "مُغْلِق", "مُغْلَق", "أُغْلِقَ", "يُغْلَقُ", "أَغْلَقَ الْبَابَ يُغْلِقُهُ إِغْلَاقًا: أَوْصَدَهُ — بَابُ الْإِفْعَالِ، يَتَعَدَّى إِلَى مَفْعُولٍ."))
put_morph(mo, "itanaqa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِعْتَنَق", "عْتَنِق", "اِعْتَنِق", "اِعْتِنَاق", "مُعْتَنِق", "مُعْتَنَق", "اُعْتُنِقَ", "يُعْتَنَقُ", "اِعْتَنَقَهُ وَاعْتَنَقَ بِهِ يَعْتَنِقُهُ اعْتِنَاقًا: ضَمَّهُ إِلَى عُنُقِهِ وَصَدْرِهِ — بَابُ الِافْتِعَالِ."))
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch26 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 26 (print pp. 47–49; the storm §11): the punishment — ʿĀd awaited rain every day and saw no scrap of cloud; one day they saw a cloud coming and rejoiced, shouting and dancing «a rain-cloud!»; but Hūd understood that the punishment had come: «this is no cloud of mercy, but a wind with a painful punishment in it»; and so it was — a violent wind blew, the like of which no one had seen or heard, uprooting trees, demolishing houses, carrying off the beasts; the desert sands flew, the world went dark, terror entered them, they shut their doors, children clung to mothers and people to walls; children weeping, women screaming, men crying for help — as if a sayer said: «no protector today from the command of God» (11:43); seven nights and eight days; the people died and lay like fallen palm trunks, the birds eating the dead and the owls dwelling in the ruined houses; Hūd and the believers were saved by their faith, ʿĀd perished by its unbelief and obstinacy: «behold, ʿĀd disbelieved in their Lord; behold, away with ʿĀd, the people of Hūd» (11:60). The END of «the storm».")
ADD_TR = (" Yirmi altıncı bölüm (basılı s. 47–49; fırtına §11): azap — Âd her gün yağmuru bekledi, bir bulut parçası bile görmedi; bir gün gelen bir bulut görüp sevindiler, «yağmur bulutu!» diye bağırıp oynadılar; fakat Hûd azabın geldiğini anladı: «bu rahmet bulutu değil, içinde acı azap olan bir rüzgâr»; öyle de oldu — benzeri görülmemiş, işitilmemiş şiddetli bir rüzgâr esti; ağaçları söktü, evleri yıktı, hayvanları taşıdı; çölün kumları uçtu, dünya karardı, dehşet içlerine girdi, kapılarını kapadılar, çocuklar annelere, insanlar duvarlara sarıldı; çocuklar ağlıyor, kadınlar çığlık atıyor, erkekler yardım istiyordu — sanki biri diyordu: «bugün Allah'ın emrinden koruyacak yok» (11:43); yedi gece sekiz gün; kavim öldü, yere düşmüş hurma kütükleri gibi kaldılar; ölüleri kuşlar yiyor, harap evlerde baykuşlar oturuyordu; Hûd ve müminler imanlarıyla kurtuldu, Âd küfrü ve inadıyla helâk oldu: «bilin ki Âd Rablerini inkâr etti; bilin ki Âd, Hûd'un kavmi, rahmetten uzak olsun» (11:60). «Fırtına»nın SONU.")
write_out(26, S, TITLE, ADD_EN, ADD_TR, "the storm §11, pp. 47–49", GLOSS_ADD, notes=(), related=())
report(26, S, GLOSS_ADD, ())
