# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 24: «قِصَّةُ عِيسَى» §3 — the Jews' submission to the apparent causes: the sciences of the age, the denial of the spirit, the materialist reading of everything; the miracles as the age's medicine; the crust without the core; hardened hearts; the Roman rule breeding hypocrisy and conspiracy (print pp. 40–42).
python3 tools/authoring/author_qisas4_ch24.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: خُضُوعُ الْيَهُودِ لِلْأَسْبَابِ الظَّاهِرَةِ", "en": "The story of ʿĪsā: the Jews' submission to the apparent causes", "tr": "Îsâ'nın kıssası: Yahudilerin zâhirî sebeplere boyun eğmesi"}
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

# ---------------------------------------------------------------- §3 خُضُوعُ الْيَهُودِ لِلْأَسْبَابِ الظَّاهِرَةِ (print pp. 40–42)
sen("s1", "And the Jews — and they were a nation in which the prophets had been many — submitted to the sciences that prevailed in their age,",
        "Yahudiler — ki onlar, içinde peygamberlerin çoğaldığı bir ümmetti — çağlarında hâkim olan ilimlere boyun eğdiler;", [
  mazi("وَخَضَعَ", "khadaa-submit", "«and submitted»", "«ve boyun eğdi»", tags=[AT], wa=True, hidden=None),
  fail("الْيَهُودُ", "yahud", "«the Jews»", "«Yahudiler»"),
  tok("وَهُمْ", "hum", "pron", [HL, MK, "jumla-mutarida"], "الْوَاوُ لِلْحَالِ (اعْتِرَاضٌ)، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and they» — a parenthetical ḥāl clause: its mubtadaʾ.", "«ve onlar» — itirâzî hâl cümlesinin mübtedâsı.", segments=wa_("هُمْ", "hum", "pron")),
  tok("أُمَّةٌ", "umma", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a nation» — the khabar.", "«bir ümmet» — haber."),
  mazi("كَثُرَ", "kathura", "«had been many»", "«çoğaldı»", tags=["jumla-sifa"], hidden=None, extra_ar=" — مِنْ بَابِ حَسُنَ؛ وَالْجُمْلَةُ نَعْتٌ لِأُمَّةٌ"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in which»", "«içinde»"),
  fail("الْأَنْبِيَاءُ", "nabi", "«the prophets»", "«peygamberler»", tags=[JT]),
  li_noun("لِلْعُلُومِ", "ilm", "«the sciences»", "«ilimlere»", tags=[JT], extra=" — مُتَعَلِّقٌ بِخَضَعَ"),
  naat("السَّائِدَةِ", "saaid", "«prevailing»", "«hâkim olan»", tags=["ism-fail"]),
  fi(),
  noun_pron("عَصْرِهِمْ", "asr", "عَصْرِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their age»", "«çağlarında»", tags=[HJ, ID], punct="،"),
])
sen("s2", "and the denial of the spirit and of whatever is connected with it became widespread among them, and they grew used to explaining everything they saw by a materialist explanation,",
        "aralarında ruhu ve ona bağlı olan her şeyi inkâr yayıldı; gördükleri her şeyi maddî bir yorumla yorumlamaya alıştılar;", [
  mazi("وَاشْتَهَرَ", "ishtahara", "«and became widespread»", "«ve yayıldı, meşhur oldu»", tags=[AT, "form-viii-verbs"], wa=True, hidden=None),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«among them»", "«aralarında»"),
  fail("إِنْكَارُ", "inkar", "«the denial [of]»", "«inkârı»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الرُّوحِ", "ruh", "«the spirit»", "«ruhu»"),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مَعْطُوفٌ عَلَى الرُّوحِ.", "«and whatever» — a relative pronoun joined to «the spirit».", "«ve … şeyi» — ruh'a ma'tûf ism-i mevsûl.", segments=wa_("مَا", "ma-mawsula", "pron")),
  mudari("يَتَّصِلُ", "ittasala", "«is connected»", "«bağlanır, ilgilidir»", tags=[MW, "form-viii-verbs"], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«with it»", "«ona»", punct="،"),
  mazi_pl("وَاعْتَادُوا", "itada", "«and they grew used»", "«ve alıştılar»", tags=[AT, "hollow-verbs", "form-viii-verbs"], wa=True),
  an_nasb("مَفْعُولٌ بِهِ لِاعْتَادُوا", "«to»", "«-meye»"),
  tok("يُفَسِّرُوا", "fassara", "verb", [AN, AK, "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«explain» — one of the five verbs: naṣb by dropping the nūn; the wāw is the doer.", "«yorumlamaya» — ef'âl-i hamseden; nûnun düşmesiyle mansub; vâv fâil."),
  maful_("كُلَّ", "kull", "«every[thing]»", "«her»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  tok("مَا", "ma-mawsula", "pron", [ID, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — a relative pronoun as the muḍāf ilayh.", "«… şeyi» — muzâfun ileyh olan ism-i mevsûl."),
  tok("يَرَوْنَهُ", "raa", "verb", [AK, MB, MW, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةٌ؛ حُذِفَتْ لَامُ الْفِعْلِ (الْأَلِفُ) لِالْتِقَاءِ السَّاكِنَيْنِ.", "«they see» — one of the five verbs; the hāʾ is its object; the defective alif dropped before the wāw.", "«gördükleri» — ef'âl-i hamseden; hâ mef'ûl; nâkıs elif vâv önünde düştü.", segments=[seg("يَرَوْنَ", "raa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("تَفْسِيرًا", "tafsir", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مُبَيِّنٌ لِلنَّوْعِ بِنَعْتِهِ.", "«an explanation» — an absolute object; its naʿt specifies the kind.", "«bir yorumla» — mef'ûl-i mutlak; sıfatı nev'ini belirtir."),
  naat("مَادِّيًّا", "maddi", "«materialist»", "«maddî»", case="nasb", tags=["ism-mansub"], punct="،"),
])
sen("s3", "so with them nothing has existence and no event is possible except by the cause and the reason;",
        "bu yüzden onlara göre hiçbir şeyin varlığı yoktur ve hiçbir hâdise sebep ve illet olmaksızın mümkün değildir;", [
  fa_la(jins=True),
  ism_la("وُجُودَ", "wujud", "«[no] existence»", "«varlık [yok]»", khabar="كَائِنٌ"),
  li_noun("لِشَيْءٍ", "shay", "«for anything»", "«bir şeyin»", extra=" — مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ"),
  noun_pron("عِنْدَهُمْ", "inda", "عِنْدَ", "هُمْ", "pron-3mp", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«with them»", "«onlara göre»", tags=[MF, ID]),
  la_jins("وَلَا", wa=True),
  ism_la("إِمْكَانَ", "imkan", "«[no] possibility»", "«imkân [yok]»", khabar="كَائِنٌ"),
  li_noun("لِحَادِثٍ", "hadith-event", "«for an event»", "«bir hâdisenin»", tags=["ism-fail"]),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — مَا بَعْدَهَا مُتَعَلِّقٌ بِمَا قَبْلَهَا.", "«except» — an emptied exception: what follows attaches to the negated clause.", "«ancak» — müferrağ istisnâ; sonrası öncesine bağlanır."),
  bi_noun("بِالسَّبَبِ", "sabab", "«by the cause»", "«sebeple»"),
  atf("وَالْعِلَّةِ", "illah", "«the reason»", "«illetle»", punct="؛"),
])
sen("s4", "so the miracles with which God honoured our master ʿĪsā were a medicine for the narrow materialist mind, and the need of the age and the call of the time.",
        "bu yüzden Allah'ın efendimiz Îsâ'ya ikram ettiği mucizeler, dar maddeci akla bir ilâç; çağın ihtiyacı ve zamanın çağrısı idi.", [
  tok("فَكَانَتِ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«so … were» — kāna; the feminine tāʾ takes a kasra before the next waṣl.", "«bu yüzden … idi» — kâne; te'nis tâ'sı sonraki vasl öncesinde kesre aldı.", segments=[seg("فَ", "fa", "conj"), seg("كَانَتِ", "kana", "verb")]),
  tok("الْمُعْجِزَاتُ", "mujiza", "noun", [KN, JM], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the miracles» — kāna's ism; a sound feminine plural.", "«mucizeler» — kâne'nin ismi; cemi müennes sâlim."),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلْمُعْجِزَاتُ.", "«which» — the relative, a naʿt.", "«ki o» — sıfat olan ism-i mevsûl."),
  mazi("أَكْرَمَ", "akrama", "«honoured»", "«ikram etti»", tags=[MW, "form-iv-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  allah_fail(),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«with them»", "«onlarla»"),
  noun_pron("سَيِّدَنَا", "sayyid", "سَيِّدَ", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master» — the object.", "«efendimiz» — mef'ûl.", tags=[MB, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«ʿĪsā» — a badal; a foreign maqṣūr name.", "«Îsâ» — bedel; yabancı maksûr isim."),
  tok("عِلَاجًا", "ilaj", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a medicine» — kāna's khabar.", "«bir ilâç» — kâne'nin haberi."),
  li_noun("لِلْعَقْلِ", "aql", "«the mind»", "«akla»"),
  naat("الْمَادِّيِّ", "maddi", "«materialist»", "«maddeci»", tags=["ism-mansub"]),
  naat2("الضَّيِّقِ", "dayyiq", "«narrow»", "«dar»", case="jarr", punct="،"),
  atf("وَحَاجَةَ", "haja", "«the need [of]»", "«ihtiyacı»", "nasb", tags=[ID, KN], sign="بِالْفَتْحَةِ عَلَى خَبَرِ كَانَ، مُضَافٌ"),
  mudaf_ilayh("الْعَصْرِ", "asr", "«the age»", "«çağın»"),
  atf("وَنِدَاءَ", "nida", "«the call [of]»", "«çağrısı»", "nasb", tags=[ID, KN], sign="بِالْفَتْحَةِ، مُضَافٌ"),
  mudaf_ilayh("الزَّمَانِ", "zaman", "«the time»", "«zamanın»", punct="."),
])
sen("s5", "And the Jews went deep into halting at the outward, into clinging to the husks without the core, and into grasping at appearances without the reality,",
        "Yahudiler zâhirde durmakta, özü bırakıp kabuklara tutunmakta, hakikati bırakıp görünüşlere yapışmakta ileri gittiler;", [
  mazi("وَأَمْعَنَ", "amana-persist", "«and went deep»", "«ve ileri gitti»", tags=[AT, "form-iv-verbs"], wa=True, hidden=None),
  fail("الْيَهُودُ", "yahud", "«the Jews»", "«Yahudiler»"),
  fi(),
  majrur("الْوُقُوفِ", "wuquf", "«halting»", "«durmakta»"),
  zarf("عِنْدَ", "inda", "«at»", "«-de»"),
  mudaf_ilayh("الظَّاهِرِ", "zahir", "«the outward»", "«zâhir»", tags=["ism-fail"]),
  atf("وَالتَّمَسُّكِ", "tamassuk", "«clinging»", "«tutunmak»"),
  bi_noun("بِالْقُشُورِ", "qishr", "«to the husks»", "«kabuklara»", tags=[JT]),
  zarf("دُونَ", "duna", "«without»", "«-sız, bırakıp»"),
  mudaf_ilayh("اللُّبَابِ", "lubab", "«the core»", "«özü»", punct="،"),
  atf("وَالتَّشَبُّثِ", "tashabbuth", "«grasping»", "«yapışmak»"),
  bi_noun("بِالْمَظَاهِرِ", "mazhar", "«at appearances»", "«görünüşlere»", tags=[JT], extra=" — صِيغَةُ مُنْتَهَى الْجُمُوعِ، أَلْ أَعَادَتِ الْكَسْرَةَ"),
  zarf("دُونَ", "duna", "«without»", "«-sız, bırakıp»"),
  mudaf_ilayh("الْحَقِيقَةِ", "haqiqa", "«the reality»", "«hakikati»", punct="،"),
])
sen("s6", "and they went to excess in sanctifying race and blood, and in love of money and matter, and they plunged into [this] life with an excessive plunging,",
        "soyu ve kanı kutsamakta, malı ve maddeyi sevmekte aşırıya gittiler; hayata aşırı bir dalışla daldılar;", [
  mazi_wa_alif("وَغَلَوْا", "ghala", "«and they went to excess»", "«ve aşırıya gittiler»", wa=True, tags=[AT]),
  fi(),
  majrur("تَقْدِيسِ", "taqdis", "«sanctifying»", "«kutsamakta»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْعُنْصُرِ", "unsur", "«race, stock»", "«soyu»"),
  atf("وَالدَّمِ", "dam", "«blood»", "«kanı»", punct="،"),
  wa_prep("وَفِي", "fi", "«in»", "«-de»"),
  majrur("حُبِّ", "hubb", "«love [of]»", "«sevmekte»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْمَالِ", "mal", "«money»", "«malı»"),
  atf("وَالْمَادَّةِ", "madda-matter", "«matter»", "«maddeyi»", punct="،"),
  mazi_pl("وَانْهَمَكُوا", "inhamaka", "«and they plunged»", "«ve daldılar»", tags=[AT, "form-vii-verbs"], wa=True),
  fi(),
  majrur("الْحَيَاةِ", "hayat", "«life»", "«hayata»"),
  tok("انْهِمَاكًا", "inhimak", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ انْهَمَكَ، مُبَيِّنٌ لِلنَّوْعِ.", "«a plunging» — the absolute object, the verb's own maṣdar.", "«bir dalışla» — fiilin kendi masdarı, mef'ûl-i mutlak."),
  naat("زَائِدًا", "zaid", "«excessive»", "«aşırı»", case="nasb", tags=["ism-fail"]),
])
sen("s7", "and their hearts hardened, and their natures dried up, so they feel no tenderness for the weak and no compassion for the poor,",
        "kalpleri katılaştı, tabiatları kurudu; artık zayıfa yumuşamaz, fakire şefkat etmezler;", [
  tok("وَقَسَتْ", "qasa-harden", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَسَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and hardened» — a defective māḍī (قَسَا): the alif drops before the feminine tāʾ.", "«ve katılaştı» — nâkıs mâzî (قَسَا): elif te'nis tâ'sı önünde düştü.", segments=wa_("قَسَتْ", "qasa-harden", "verb")),
  noun_pron("قُلُوبُهُمْ", "qalb", "قُلُوبُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their hearts» — the doer.", "«kalpleri» — fâil.", tags=[FL, ID, JT], punct="،"),
  mazi_ta("وَجَفَّتْ", "jaffa", "«and dried up»", "«ve kurudu»", tags=[AT, "doubled-verbs"], wa=True),
  noun_pron("طَبَائِعُهُمْ", "tabia", "طَبَائِعُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«their natures» — the doer; a muntahā plural.", "«tabiatları» — fâil; müntehe'l-cumû'.", tags=[FL, ID, JT], punct="،"),
  fa_la(),
  khamsa("يَرِقُّونَ", "raqqa", "«they feel tenderness»", "«yumuşarlar»", tags=["doubled-verbs"], extra_ar=" — مُضَاعَفٌ: رَقَّ يَرِقُّ"),
  li_noun("لِلضَّعِيفِ", "daif", "«for the weak»", "«zayıfa»"),
  la_nafiya("وَلَا", wa=True),
  khamsa("يَعْطِفُونَ", "atafa", "«they feel compassion»", "«şefkat ederler»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("الْفَقِيرِ", "faqir", "«the poor»", "«fakire»", punct="،"),
])
sen("s8", "and they treat whoever has no Israelite blood running in his veins as animals and dogs are treated, or as the lifeless things in which there is no spirit,",
        "damarlarında İsrâil kanı akmayan kimseye hayvanlara ve köpeklere, yahut içinde ruh olmayan cansızlara davranılır gibi davranırlar;", [
  khamsa_wa("وَيُعَامِلُونَ", "amala", "«and they treat»", "«ve … davranırlar»", tags=["form-iii-verbs"]),
  tok("مَنْ", "man-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«whoever» — the relative, the object.", "«… kimseye» — ism-i mevsûl, mef'ûl."),
  la_nafiya(),
  tok("يَجْرِي", "jara", "verb", ["la-nafiya", "mudari-marfu", "naqis-verbs", MW], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«runs» — rafʿ by an estimated ḍamma on the yāʾ; the ṣila.", "«akar» — yâ üzerinde takdîrî damme; sıla."),
  fi(),
  noun_pron("عُرُوقِهِ", "irq", "عُرُوقِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his veins»", "«damarlarında»", tags=[HJ, ID, JT]),
  fail("الدَّمُ", "dam", "«the blood»", "«kan»"),
  naat("الْإِسْرَائِيلِيُّ", "israili", "«Israelite»", "«İsrâil»", case="raf", tags=["ism-mansub"]),
  tok("مُعَامَلَةَ", "muamala", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ (مُبَيِّنٌ لِلنَّوْعِ بِإِضَافَتِهِ)، مُضَافٌ.", "«[with] the treatment [of]» — an absolute object, specified by annexation.", "«… muamelesiyle» — izâfetle nev'i belirtilen mef'ûl-i mutlak.", "،" if False else None),
  mudaf_ilayh("الْحَيَوَانَاتِ", "hayawan", "«the animals»", "«hayvanların»", tags=[JM]),
  atf("وَالْكِلَابِ", "kalb", "«the dogs»", "«köpeklerin»", tags=[JT]),
  tok("أَوِ", "aw", "part", [AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — its sukūn turned to kasra before the article.", "«yahut» — sükûnu harf-i târif önünde kesreye döndü."),
  tok("الْجَمَادَاتِ", "jamad", "noun", [AT, JM], "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the lifeless things» — joined by aw; a sound feminine plural.", "«cansızların» — ev ile ma'tûf; cemi müennes sâlim."),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«in which» — the relative, a naʿt.", "«ki» — sıfat olan ism-i mevsûl."),
  la_jins("لَا"),
  tok("رُوحَ", "ruh", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«[no] spirit» — lā's ism, built on fatḥa.", "«ruh [yok]» — lâ'nın ismi, fetha üzere mebnî."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in them» — attached to lā's understood khabar.", "«içinde» — lâ'nın mahzuf haberine bağlı.", tags=["la-nafiya-lil-jins", "hadhf-wa-taqdir"], extra_ar=" — مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ", punct="،"),
])
sen("s9", "and they submit to the strong and rich, and lord it over the small and poor, and they are hard when they have power and soft when they are helpless;",
        "güçlü zenginlere boyun eğer, küçük fakirlere zorbalık ederler; güç ellerindeyken katılaşır, âcizken yumuşarlar;", [
  khamsa_wa("وَيَخْضَعُونَ", "khadaa-submit", "«and they submit»", "«ve boyun eğerler»"),
  li_noun("لِلْأَقْوِيَاءِ", "qawi", "«to the strong»", "«güçlülere»", tags=[JT]),
  naat("الْأَغْنِيَاءِ", "ghani", "«rich»", "«zenginlere»", tags=[JT], punct="،"),
  khamsa_wa("وَيَتَجَبَّرُونَ", "tajabbara", "«and they lord it»", "«ve zorbalık ederler»", tags=["form-v-verbs"]),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("الصِّغَارِ", "saghir", "«the small»", "«küçüklere»", tags=[JT]),
  naat("الْفُقَرَاءِ", "faqir", "«poor»", "«fakirlere»", tags=[JT], punct="،"),
  khamsa_wa("وَيَقْسُونَ", "qasa-harden", "«and they are hard»", "«ve katılaşırlar»", tags=["naqis-verbs"], extra_ar=" — حُذِفَتْ لَامُ الْفِعْلِ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ: يَقْسُو + ونَ"),
  zarf("عِنْدَ", "inda", "«at [the time of]»", "«-de»"),
  mudaf_ilayh("الْقُدْرَةِ", "qudra", "«power»", "«güç»", punct="،"),
  khamsa_wa("وَيَلِينُونَ", "lana", "«and they are soft»", "«ve yumuşarlar»", tags=["hollow-verbs"]),
  zarf("عِنْدَ", "inda", "«at [the time of]»", "«-de»"),
  mudaf_ilayh("الْعَجْزِ", "ajz", "«helplessness»", "«acz»", punct="،"),
])
sen("s10", "the life of humiliation and servitude that they lived under the Roman rule — which lasted a long time in Syria and Palestine — had bred in them hypocrisy and servility, cunning and guile, and recourse to conspiracy and secrecy.",
        "Suriye ve Filistin'de uzun süre devam eden Roma yönetimi altında yaşadıkları zillet ve kölelik hayatı, onlarda nifak ve boyun eğişi, hile ve kurnazlığı, komplo ve gizliliğe başvurmayı doğurmuştu.", [
  tok("قَدْ", "qad", "part", ["qad-harf", HL], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ حَالٌ (أَوِ اسْتِئْنَافٌ).", "«[indeed]» — the clause after it is a ḥāl (or a fresh start).", "«[gerçekten]» — sonraki cümle hâl (veya isti'nâf)."),
  mazi_ta("وَلَدَتْ", "walada", "«had bred»", "«doğurmuştu»", tags=["mithal-verbs"]),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«in them»", "«onlarda»"),
  fail("حَيَاةُ", "hayat", "«the life [of]»", "«hayatı»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الذُّلِّ", "dhull", "«humiliation»", "«zilletin»"),
  atf("وَالْعُبُودِيَّةِ", "ubudiyya", "«servitude»", "«köleliğin»"),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِحَيَاةُ.", "«which» — the relative, a naʿt.", "«ki» — sıfat olan ism-i mevsûl."),
  v_pl_pron("عَاشُوهَا", "asha-live", "عَاشُو", "هَا", "pron-3fs", "«they lived it»", "«yaşadıkları»", tags=[MW, "hollow-verbs"]),
  fi(),
  majrur("الْحُكْمِ", "hukm", "«the rule»", "«yönetimi»"),
  naat("الرُّومَانِيِّ", "rumani", "«Roman»", "«Roma»", tags=["ism-mansub"]),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلْحُكْمِ.", "«which» — the relative, a naʿt of «the rule».", "«ki» — yönetimin sıfatı olan ism-i mevsûl."),
  mazi("دَامَ", "dama", "«lasted»", "«devam etti»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — فِعْلٌ تَامٌّ هُنَا؛ وَالْجُمْلَةُ صِلَةٌ"),
  tok("مُدَّةً", "mudda", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«for a time» — an adverb of time.", "«bir süre» — zaman zarfı."),
  naat("طَوِيلَةً", "tawil-long", "«long»", "«uzun»", case="nasb"),
  fi(),
  tok("سُورِيَا", "suriya", "propn", [HJ, MM, "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Syria» — jarr by an estimated kasra; a foreign name.", "«Suriye» — takdîrî kesre; yabancı özel isim."),
  atf("وَفَلَسْطِينَ", "filastin", "«Palestine»", "«Filistin»", tags=[MM], pos="propn", sign="بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", punct="،"),
  maful_("النِّفَاقَ", "nifaq", "«hypocrisy»", "«nifakı»", ar="مَفْعُولٌ بِهِ لِوَلَدَتْ مَنْصُوبٌ بِالْفَتْحَةِ — أُخِّرَ عَنِ الْفَاعِلِ وَمَا تَعَلَّقَ بِهِ."),
  atf("وَالْخُنُوعَ", "khunu", "«servility»", "«boyun eğişi»", "nasb", punct="،"),
  atf("وَالتَّحَيُّلَ", "tahayyul", "«cunning»", "«hileyi»", "nasb"),
  atf("وَالدَّهَاءَ", "daha", "«guile»", "«kurnazlığı»", "nasb", punct="،"),
  atf("وَاللُّجُوءَ", "luju", "«recourse»", "«başvurmayı»", "nasb"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("الْمُؤَامَرَةِ", "muamara", "«conspiracy»", "«komplo»"),
  atf("وَالسِّرِّيَّةِ", "sirriyya", "«secrecy»", "«gizliliğe»", punct="."),
])

CAND = {
 "khadaa-submit": G("khadaa-submit", "خَضَعَ", "خ ض ع", "verb", "to submit, to bow (li: to)", "boyun eğmek (li ile)", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "hum": G("hum", "هُمْ", None, "pron", "they", "onlar", 1),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, to abound", "çok olmak, çoğalmak", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge; a science", "ilim", 1, plural="عُلُوم"),
 "saaid": G("saaid", "سَائِد", "س و د", "noun", "prevailing, dominant (an active participle of a hollow root)", "hâkim, egemen (ecvef kökün ism-i fâili)", 2),
 "asr": G("asr", "عَصْر", "ع ص ر", "noun", "an age, an era", "çağ, asır", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "ishtahara": G("ishtahara", "اِشْتَهَرَ", "ش ه ر", "verb", "to become well known, to spread (Form VIII)", "meşhur olmak, yayılmak (iftiâl)", 2),
 "inkar": G("inkar", "إِنْكَار", "ن ك ر", "noun", "denial", "inkâr", 1),
 "ruh": G("ruh", "رُوح", "ر و ح", "noun", "spirit, soul", "ruh", 1, plural="أَرْوَاح"),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "ittasala": G("ittasala", "اِتَّصَلَ", "و ص ل", "verb", "to be connected (bi: with) (Form VIII)", "bağlanmak, ilgili olmak (iftiâl)", 2),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "itada": G("itada", "اعْتَادَ", "ع و د", "verb", "to grow used to (Form VIII, hollow)", "alışmak (iftiâl, ecvef)", 2),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "fassara": G("fassara", "فَسَّرَ", "ف س ر", "verb", "to explain, to interpret (Form II)", "açıklamak, tefsir etmek (tef'îl)", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "tafsir": G("tafsir", "تَفْسِير", "ف س ر", "noun", "an explanation, an interpretation", "tefsir, yorum", 1),
 "maddi": G("maddi", "مَادِّيّ", "م د د", "noun", "material, materialist (a nisba)", "maddî, maddeci (nisbet)", 2),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "wujud": G("wujud", "وُجُود", "و ج د", "noun", "existence", "varlık, vücut", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "inda": G("inda", "عِنْدَ", None, "noun", "with, at, in the presence of", "yanında, katında", 1),
 "imkan": G("imkan", "إِمْكَان", "م ك ن", "noun", "possibility", "imkân", 2),
 "hadith-event": G("hadith-event", "حَادِث", "ح د ث", "noun", "an event, an occurrence (an active participle)", "hâdise, olay (ism-i fâil)", 2, plural="حَوَادِث"),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "sabab": G("sabab", "سَبَب", "س ب ب", "noun", "a cause, a means", "sebep", 1, plural="أَسْبَاب"),
 "illah": G("illah", "عِلَّة", "ع ل ل", "noun", "a cause, a reason; an ailment", "illet, sebep", 1, plural="عِلَل"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "mujiza": G("mujiza", "مُعْجِزَة", "ع ج ز", "noun", "a miracle", "mucize", 1, plural="مُعْجِزَات"),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "akrama": G("akrama", "أَكْرَمَ", "ك ر م", "verb", "to honour (Form IV)", "ikram etmek (if'âl)", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "ilaj": G("ilaj", "عِلَاج", "ع ل ج", "noun", "a remedy, a medicine; treatment", "ilâç, tedavi", 1),
 "aql": G("aql", "عَقْل", "ع ق ل", "noun", "the mind, reason", "akıl", 1, plural="عُقُول"),
 "dayyiq": G("dayyiq", "ضَيِّق", "ض ي ق", "noun", "narrow", "dar", 1),
 "haja": G("haja", "حَاجَة", "ح و ج", "noun", "a need", "ihtiyaç", 1),
 "nida": G("nida", "نِدَاء", "ن د و", "noun", "a call", "çağrı, nidâ", 1),
 "zaman": G("zaman", "زَمَان", "ز م ن", "noun", "time, an age", "zaman", 1),
 "amana-persist": G("amana-persist", "أَمْعَنَ", "م ع ن", "verb", "to go deep (fī: into), to persist (Form IV)", "derinleşmek, ileri gitmek (if'âl)", 3),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "wuquf": G("wuquf", "وُقُوف", "و ق ف", "noun", "standing, halting", "durma, vakfetme", 2),
 "zahir": G("zahir", "ظَاهِر", "ظ ه ر", "noun", "the outward, the apparent (an active participle)", "zâhir, görünen (ism-i fâil)", 1),
 "tamassuk": G("tamassuk", "تَمَسُّك", "م س ك", "noun", "clinging (bi: to) (the maṣdar of Form V)", "tutunma, temessük (tefa''ul masdarı)", 2),
 "qishr": G("qishr", "قِشْر", "ق ش ر", "noun", "a husk, a peel", "kabuk", 2, plural="قُشُور"),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "below; without, short of", "aşağısında; -sız, -den başka", 1),
 "lubab": G("lubab", "لُبَاب", "ل ب ب", "noun", "the core, the kernel", "öz, lübâb", 3),
 "tashabbuth": G("tashabbuth", "تَشَبُّث", "ش ب ث", "noun", "grasping at, clinging (the maṣdar of Form V)", "yapışma, sarılma (tefa''ul masdarı)", 3),
 "mazhar": G("mazhar", "مَظْهَر", "ظ ه ر", "noun", "an appearance, an outward show", "görünüş, mazhar", 2, plural="مَظَاهِر"),
 "haqiqa": G("haqiqa", "حَقِيقَة", "ح ق ق", "noun", "reality, truth", "hakikat", 1),
 "ghala": G("ghala", "غَلَا", "غ ل و", "verb", "to go to excess (fī: in) (defective)", "aşırıya gitmek, haddi aşmak (nâkıs)", 2),
 "taqdis": G("taqdis", "تَقْدِيس", "ق د س", "noun", "sanctifying (the maṣdar of Form II)", "kutsama, takdis (tef'îl masdarı)", 2),
 "unsur": G("unsur", "عُنْصُر", "ع ن ص ر", "noun", "an element; race, stock", "unsur; soy", 2, plural="عَنَاصِر"),
 "dam": G("dam", "دَم", "د م و", "noun", "blood", "kan", 1, plural="دِمَاء"),
 "hubb": G("hubb", "حُبّ", "ح ب ب", "noun", "love", "sevgi", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "money, wealth", "mal", 1, plural="أَمْوَال"),
 "madda-matter": G("madda-matter", "مَادَّة", "م د د", "noun", "matter, material", "madde", 1, plural="مَوَادّ"),
 "inhamaka": G("inhamaka", "اِنْهَمَكَ", "ه م ك", "verb", "to plunge (fī: into), to be absorbed (Form VII)", "dalmak, kendini kaptırmak (infiâl)", 3),
 "hayat": G("hayat", "حَيَاة", "ح ي ي", "noun", "life", "hayat", 1),
 "inhimak": G("inhimak", "اِنْهِمَاك", "ه م ك", "noun", "plunging into, absorption (the maṣdar of Form VII)", "dalma, kendini kaptırma (infiâl masdarı)", 3),
 "zaid": G("zaid", "زَائِد", "ز ي د", "noun", "excessive, extra (an active participle)", "aşırı, fazla (ism-i fâil)", 2),
 "qasa-harden": G("qasa-harden", "قَسَا", "ق س و", "verb", "to harden, to be hard (defective)", "katılaşmak, sertleşmek (nâkıs)", 2),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "a heart", "kalp", 1, plural="قُلُوب"),
 "jaffa": G("jaffa", "جَفَّ", "ج ف ف", "verb", "to dry up (doubled)", "kurumak (muzâaf)", 2),
 "tabia": G("tabia", "طَبِيعَة", "ط ب ع", "noun", "nature", "tabiat", 1, plural="طَبَائِع"),
 "raqqa": G("raqqa", "رَقَّ", "ر ق ق", "verb", "to be tender, to soften (li: toward) (doubled)", "yumuşamak, acımak (muzâaf)", 2),
 "daif": G("daif", "ضَعِيف", "ض ع ف", "noun", "weak", "zayıf", 1),
 "atafa": G("atafa", "عَطَفَ", "ع ط ف", "verb", "to incline; (ʿalā) to feel compassion for", "eğilmek; (alâ ile) şefkat etmek", 2),
 "ala": G("ala", "عَلَى", None, "prep", "on, over", "üzerine", 1),
 "faqir": G("faqir", "فَقِير", "ف ق ر", "noun", "poor", "fakir", 1, plural="فُقَرَاء"),
 "amala": G("amala", "عَامَلَ", "ع م ل", "verb", "to treat, to deal with (Form III)", "muamele etmek (müfâale)", 1),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "whoever, he who", "kim ki, … kimse", 1),
 "jara": G("jara", "جَرَى", "ج ر ي", "verb", "to run, to flow", "akmak, koşmak", 1),
 "irq": G("irq", "عِرْق", "ع ر ق", "noun", "a vein; a root", "damar; kök", 2, plural="عُرُوق"),
 "israili": G("israili", "إِسْرَائِيلِيّ", None, "noun", "Israelite (a nisba)", "İsrâilî (nisbet)", 2),
 "muamala": G("muamala", "مُعَامَلَة", "ع م ل", "noun", "treatment, dealing (the maṣdar of Form III)", "muamele (müfâale masdarı)", 1),
 "hayawan": G("hayawan", "حَيَوَان", "ح ي ي", "noun", "an animal", "hayvan", 1),
 "kalb": G("kalb", "كَلْب", "ك ل ب", "noun", "a dog", "köpek", 1, plural="كِلَاب"),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya", 1),
 "jamad": G("jamad", "جَمَاد", "ج م د", "noun", "an inanimate thing", "cansız, cemâd", 2),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1, plural="أَقْوِيَاء"),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "tajabbara": G("tajabbara", "تَجَبَّرَ", "ج ب ر", "verb", "to act tyrannically (ʿalā: over) (Form V)", "zorbalık etmek, cebbarlık taslamak (tefa''ul)", 3),
 "saghir": G("saghir", "صَغِير", "ص غ ر", "noun", "small, little", "küçük", 1, plural="صِغَار"),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "lana": G("lana", "لَانَ", "ل ي ن", "verb", "to be soft (hollow)", "yumuşamak (ecvef)", 2),
 "ajz": G("ajz", "عَجْز", "ع ج ز", "noun", "weakness, helplessness", "acz", 2),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to give birth; to breed (an assimilated verb)", "doğurmak (misâl fiil)", 1),
 "dhull": G("dhull", "ذُلّ", "ذ ل ل", "noun", "humiliation, abasement", "zillet", 2),
 "ubudiyya": G("ubudiyya", "عُبُودِيَّة", "ع ب د", "noun", "servitude, bondage", "kölelik, ubûdiyet", 2),
 "asha-live": G("asha-live", "عَاشَ", "ع ي ش", "verb", "to live (hollow)", "yaşamak (ecvef)", 1),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "a ruling; rule, government", "hüküm; yönetim", 1, plural="أَحْكَام"),
 "rumani": G("rumani", "رُومَانِيّ", None, "noun", "Roman (a nisba)", "Roma'ya ait, Romalı (nisbet)", 2),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which (m.)", "ki o, -an", 1),
 "dama": G("dama", "دَامَ", "د و م", "verb", "to last, to go on (hollow)", "sürmek, devam etmek (ecvef)", 2),
 "mudda": G("mudda", "مُدَّة", "م د د", "noun", "a period, a span of time", "müddet, süre", 1, plural="مُدَد"),
 "tawil-long": G("tawil-long", "طَوِيل", "ط و ل", "noun", "long, tall", "uzun", 1),
 "suriya": G("suriya", "سُورِيَا", None, "propn", "Syria", "Suriye", 1),
 "filastin": G("filastin", "فِلَسْطِين", None, "propn", "Palestine", "Filistin", 1),
 "nifaq": G("nifaq", "نِفَاق", "ن ف ق", "noun", "hypocrisy", "nifak, ikiyüzlülük", 1),
 "khunu": G("khunu", "خُنُوع", "خ ن ع", "noun", "servility, cringing submission", "boyun eğiş, zillete rıza", 3),
 "tahayyul": G("tahayyul", "تَحَيُّل", "ح و ل", "noun", "cunning, resorting to tricks (the maṣdar of Form V)", "hile, hileye başvurma (tefa''ul masdarı)", 3),
 "daha": G("daha", "دَهَاء", "د ه ي", "noun", "guile, shrewdness", "kurnazlık, dehâ", 3),
 "luju": G("luju", "لُجُوء", "ل ج أ", "noun", "recourse, resorting (ilā: to)", "sığınma, başvurma", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "muamara": G("muamara", "مُؤَامَرَة", "أ م ر", "noun", "a conspiracy (the maṣdar of Form III)", "komplo, müâmere (müfâale masdarı)", 2),
 "sirriyya": G("sirriyya", "سِرِّيَّة", "س ر ر", "noun", "secrecy (an abstract nisba)", "gizlilik (masdar-ı sınâî)", 2),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "khadaa-submit", _sg.sound1("fataha", "خَضَع", "خْضَع", "اِخْضَع", "خُضُوع", "خَاضِع", None, None, None, "خَضَعَ لَهُ يَخْضَعُ: ذَلَّ وَانْقَادَ."))
put_morph(mo, "amana-persist", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَمْعَن", "مْعِن", "أَمْعِن", "إِمْعَان", "مُمْعِن", None, None, None, "أَمْعَنَ فِي الشَّيْءِ: بَالَغَ فِيهِ وَأَبْعَدَ؛ وَأَمْعَنَ النَّظَرَ: أَطَالَهُ."))
put_morph(mo, "ghala", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "غَلَ", "غْل", "u", "اُغْل", "غُلُوّ", "غَالٍ (الْغَالِي)", None, None, None, "غَلَا فِي الْأَمْرِ يَغْلُو: جَاوَزَ فِيهِ الْحَدَّ — نَاقِصٌ وَاوِيٌّ؛ لَمْ يَغْلُ."))
put_morph(mo, "inhamaka", _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْهَمَك", "نْهَمِك", "اِنْهَمِك", "اِنْهِمَاك", "مُنْهَمِك", None, None, None, "اِنْهَمَكَ فِي الْأَمْرِ: جَدَّ فِيهِ وَلَجَّ وَاسْتَغْرَقَ."))
put_morph(mo, "qasa-harden", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "قَسَ", "قْس", "u", "اُقْس", "قَسْوَة / قَسَاوَة", "قَاسٍ (الْقَاسِي)", None, None, None, "قَسَا الْقَلْبُ يَقْسُو: صَلُبَ وَغَلُظَ — نَاقِصٌ وَاوِيٌّ؛ لَمْ يَقْسُ."))
put_morph(mo, "jaffa", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "جَفَاف", "جَافّ", _sg.mazi14("جَفّ", "جَفَف"), _sg.mudari14("َ", "جِفّ", "جْفِف"), ["جِفَّ", "جِفَّا", "جِفُّوا", "جِفِّي", "جِفَّا", "اِجْفِفْنَ"], "يَجِفَّ", "يَجِفَّ", "تَجِفَّ", None, None, None, "جَفَّ الشَّيْءُ يَجِفُّ: يَبِسَ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَجِفَّ."))
put_morph(mo, "raqqa", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "رِقَّة", "رَقِيق", _sg.mazi14("رَقّ", "رَقَق"), _sg.mudari14("َ", "رِقّ", "رْقِق"), ["رِقَّ", "رِقَّا", "رِقُّوا", "رِقِّي", "رِقَّا", "اِرْقِقْنَ"], "يَرِقَّ", "يَرِقَّ", "تَرِقَّ", None, None, None, "رَقَّ لَهُ يَرِقُّ: لَانَ قَلْبُهُ وَعَطَفَ عَلَيْهِ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَرِقَّ."))
put_morph(mo, "atafa", _sg.sound1("daraba", "عَطَف", "عْطِف", "اِعْطِف", "عَطْف", "عَاطِف", "مَعْطُوف", "عُطِفَ", "يُعْطَفُ", "عَطَفَ عَلَيْهِ يَعْطِفُ: أَشْفَقَ عَلَيْهِ وَحَنَا؛ وَعَطَفَ الشَّيْءَ: ثَنَاهُ."))
put_morph(mo, "tajabbara", _sg.derived(_sg.B5, _sg.W5, "َ", "تَجَبَّر", "تَجَبَّر", "تَجَبَّر", "تَجَبُّر", "مُتَجَبِّر", None, None, None, "تَجَبَّرَ عَلَى النَّاسِ: تَكَبَّرَ وَطَغَى."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch24 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 24 (print pp. 40–42; ʿĪsā §3): the Jews' submission to the apparent causes — the sciences of the age, the denial of the spirit, the materialist reading of everything (s1–s3); the miracles as the age's medicine (s4); the husks without the core, race and blood, hardened hearts, the treatment of the non-Israelite (s5–s9); the Roman rule breeding hypocrisy and conspiracy (s10)."
ADD_TR = " Yirmi dördüncü bölüm (baskı s. 40–42; Îsâ §3): Yahudilerin zâhirî sebeplere boyun eğmesi — çağın ilimleri, ruhun inkârı, her şeyin maddeci yorumu (s1–s3); çağın ilâcı olarak mucizeler (s4); özü bırakıp kabuklar, soy ve kan, katılaşmış kalpler, İsrâilli olmayana muamele (s5–s9); nifak ve komplo doğuran Roma yönetimi (s10)."
write_out(24, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §3", GLOSS_ADD, notes=(), related=())
report(24, S, GLOSS_ADD, ())
