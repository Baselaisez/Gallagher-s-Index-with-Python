# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 20: «قِصَّةُ زَكَرِيَّا» — the story of Zakariyyā opens: §1 (the prayer for a righteous son), §2 (the vow of ʿImrān's wife),
§3 ("Lord, I have delivered a female", with 3:35–36); print pp. 32–34.
python3 tools/authoring/author_qisas4_ch20.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ زَكَرِيَّا: دُعَاءٌ لِوَلَدٍ صَالِحٍ", "en": "The story of Zakariyyā: a prayer for a righteous son", "tr": "Zekeriyyâ'nın kıssası: sâlih bir evlât için duâ"}
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

# ---------------------------------------------------------------- §1 دُعَاءُ زَكَرِيَّا لِوَلَدٍ صَالِحٍ (print p. 32)
sen("s1", "Another colour of God's bounties upon His servants, and of the signs of His power that has encompassed everything, showed itself in Zakariyyā's prayer for a righteous son, well-pleasing, dutiful and God-fearing,",
        "Allah'ın kullarına nimetlerinin ve her şeyi kuşatan kudretinin âyetlerinin bir başka rengi, Zekeriyyâ'nın sâlih, hoşnut edici, iyi ve takvâlı bir evlât için duâsında tecelli etti;", [
  tok("وَلَوْنٌ", "lawn", "noun", [MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَوْنٌ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — سَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ وَصْفُهَا.", "«and a colour» — the mubtadaʾ; an indefinite allowed to open by its description.", "«ve bir renk» — mübtedâ; nekre, sıfatla câiz oldu.", segments=wa_("لَوْنٌ", "lawn", "noun")),
  tok("آخَرُ", "akhar", "noun", [NA, MM], "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — the naʿt; a diptote.", "«başka» — sıfat; gayr-i munsarıf."),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("آلَاءِ", "ala-bounties", "«the bounties [of]»", "«nimetlerinin»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  prep("عَلَى", "ala", "«upon»", "«-e»"),
  noun_pron("عِبَادِهِ", "abd", "عِبَادِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His servants»", "«kullarına»", tags=[HJ, ID, JT]),
  atf("وَآيَاتِ", "aya", "«the signs [of]»", "«âyetlerinin»", "jarr", tags=[ID, JM], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  noun_pron("قُدْرَتِهِ", "qudra", "قُدْرَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His power»", "«kudretinin»", tags=[ID]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِقُدْرَتِهِ.", "«that» — the relative pronoun, a naʿt of «His power».", "«ki o» — ism-i mevsûl, «kudreti»nin sıfatı."),
  mazi_ta("أَحَاطَتْ", "ahata", "«has encompassed»", "«kuşatmıştır»", tags=[MW, "hollow-verbs", "form-iv-verbs"], extra=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  tok("بِكُلِّ", "kull", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ، مُضَافٌ.", "«every»", "«her»", segments=[seg("بِ", "bi", "prep"), seg("كُلِّ", "kull", "noun")]),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeyi»", punct="،"),
  mazi("تَجَلَّى", "tajalla", "«showed itself»", "«tecelli etti»", tags=[MK, "naqis-verbs", "form-v-verbs"], hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ"),
  fi(), majrur("دُعَاءِ", "dua", "«the prayer [of]»", "«duâsında»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  tok("زَكَرِيَّا", "zakariyya", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Zakariyyā» — a foreign name ending in alif; its kasra is estimated.", "«Zekeriyyâ'nın» — elifle biten yabancı özel isim; kesresi takdirî."),
  tok("لِوَلَدٍ", "walad", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَوَلَدٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«for a son»", "«bir evlât için»", segments=[seg("لِ", "li", "prep"), seg("وَلَدٍ", "walad", "noun")]),
  naat("صَالِحٍ", "salih", "«righteous»", "«sâlih»", tags=["ism-fail"]),
  naat2("رَضِيٍّ", "radi-pleasing", "«well-pleasing»", "«hoşnut edici»", case="jarr", tags=["sifa-mushabbaha"], punct="،"),
  naat2("بَرٍّ", "barr", "«dutiful»", "«iyi»", case="jarr", n="ثَالِثٌ", tags=["sifa-mushabbaha"]),
  naat2("تَقِيٍّ", "taqi", "«God-fearing»", "«takvâlı»", case="jarr", n="رَابِعٌ", tags=["sifa-mushabbaha"], punct="،"),
])
sen("s2", "who would inherit from him and inherit from the House of Yaʿqūb, and take up the call to God —",
        "ona ve Ya'kûb ailesine vâris olacak ve Allah'a davet işini yüklenecek bir evlât —", [
  tok("يَرِثُهُ", "waritha", "verb", ["jumla-sifa", "mudari-marfu", "mithal-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ لِوَلَدٍ؛ وَرِثَ يَرِثُ: مِثَالٌ وَاوِيٌّ حُذِفَتْ وَاوُهُ فِي الْمُضَارِعِ.", "«who would inherit from him» — a muḍāriʿ; the clause describes «a son»; the assimilated wāw of waritha drops in the muḍāriʿ.", "«ona vâris olacak» — muzari; cümle «evlât»ın sıfatı; misâl fiilin vâvı muzaride düşer.", segments=[seg("يَرِثُ", "waritha", "verb"), pr3ms()]),
  mudari("وَيَرِثُ", "waritha", "«and inherit»", "«ve vâris olacak»", tags=[AT, "mithal-verbs"], hidden="هُوَ"),
  prep("مِنْ", "min", "«from»", "«-e»"),
  majrur("آلِ", "al-family", "«the House [of]»", "«ailesine»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  tok("يَعْقُوبَ", "yaqub", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yaʿqūb» — jarr by fatḥa (a diptote).", "«Ya'kûb» — gayr-i munsarıf.", punct="،"),
  mudari("وَيَقُومُ", "qama", "«and take up»", "«ve yüklenecek»", tags=[AT, "hollow-verbs"], hidden="هُوَ"),
  tok("بِالدَّعْوَةِ", "dawa", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالدَّعْوَةِ مَجْرُورٌ.", "«the call»", "«davet işini»", segments=[seg("بِ", "bi", "prep"), seg("الدَّعْوَةِ", "dawa", "noun")]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى.", "«God»", "«Allah'a»", punct="،"),
])
sen("s3", "and that was when age had advanced upon him, his bones had grown weak, grey hair had settled on him, and hope that his wife would bear had been cut off;",
        "bu da yaşı ilerlediği, kemiği zayıfladığı, saçına ak düştüğü ve karısının doğurmasından ümit kesildiği bir zamandaydı;", [
  tok("وَذٰلِكَ", "dhalika", "pron", [AT, MK, "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ (أَوْ لِلْحَالِ)، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and that» — the mubtadaʾ.", "«ve bu» — mübtedâ.", segments=wa_("ذٰلِكَ", "dhalika", "pron")),
  tok("حِينَ", "hin", "noun", [MF, MK, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ — مُتَعَلِّقٌ بِالْخَبَرِ الْمَحْذُوفِ.", "«when» — the time adverb, the khabar's seat.", "«… zamanda» — zaman zarfı, haber."),
  mazi_ta("تَقَدَّمَتْ", "taqaddama", "«had advanced»", "«ilerlemişti»", tags=[ID, "form-v-verbs"], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ حِينَ"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«upon him»", "«onun»"),
  fail("السِّنُّ", "sinn", "«age»", "«yaşı»", punct="،"),
  mazi("وَوَهَنَ", "wahana", "«and had grown weak»", "«ve zayıflamıştı»", tags=[AT, "mithal-verbs"], wa=True, hidden=None),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«his»", "«onun»"),
  fail("الْعَظْمُ", "azm", "«the bones»", "«kemiği»", punct="،"),
  mazi("وَلَجَّ", "lajja", "«and had settled»", "«ve iyice yerleşmişti»", tags=[AT, "doubled-verbs"], wa=True, hidden=None),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«on him»", "«ona»"),
  fail("الشَّيْبُ", "shayb-greyness", "«grey hair»", "«ak saç»", punct="،"),
  mazi("وَانْقَطَعَ", "inqataa", "«and had been cut off»", "«ve kesilmişti»", tags=[AT, "form-vii-verbs"], wa=True, hidden=None),
  fail("الرَّجَاءُ", "raja-hope", "«hope»", "«ümit»"),
  prep("مِنْ", "min", "«that» (lit. from)", "«-den»"),
  tok("أَنْ", "an-masdariyya", "part", [AN, HJ], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِمِنْ.", "«that» — the clause is in the place of jarr after min.", "«… -ması» — müevvel masdar min ile mecrûr."),
  tok("تَلِدَ", "walada", "verb", [AN, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — وَلَدَ يَلِدُ: مِثَالٌ وَاوِيٌّ.", "«would bear» — naṣb by an; an assimilated verb whose wāw drops.", "«doğurması» — en ile mansub; misâl fiil."),
  noun_pron("زَوْجُهُ", "zawj", "زَوْجُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — زَوْجٌ: يُقَالُ لِلْمَرْأَةِ أَيْضًا.", "«his wife» — the doer; zawj is said of the woman too.", "«karısı» — fâil; zevc kadın için de söylenir.", tags=[FL, ID], punct="،"),
])
sen("s4", "so God Most High answered his prayer, gave the lie to people's suppositions, and set aside the old experience, and granted him an upright son,",
        "Allah Teâlâ duâsına icabet etti, insanların zanlarını yalanladı, eski tecrübeleri boşa çıkardı ve ona olgun bir evlât verdi;", [
  mazi("فَأَجَابَ", "ajaba", "«so answered»", "«bunun üzerine icabet etti»", tags=[AT, MB, "hollow-verbs", "form-iv-verbs"], wa=True, hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»"),
  noun_pron("دُعَاءَهُ", "dua", "دُعَاءَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his prayer»", "«duâsına»", tags=[MB, ID], punct="،"),
  mazi("وَكَذَّبَ", "kadhdhaba", "«and gave the lie to»", "«ve yalanladı»", tags=[AT, MB, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  maful_("ظُنُونَ", "zann", "«the suppositions [of]»", "«zanlarını»", tags=[ID, JT], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ."),
  mudaf_ilayh("النَّاسِ", "nas", "«people»", "«insanların»", punct="،"),
  mazi("وَأَبْطَلَ", "abtala", "«and set aside»", "«ve boşa çıkardı»", tags=[AT, MB, "form-iv-verbs"], wa=True, hidden="هُوَ"),
  maful_("التَّجَارِبَ", "tajriba", "«the experience»", "«tecrübeleri»", tags=[JT]),
  naat("الْقَدِيمَةَ", "qadim", "«old»", "«eski»", case="nasb", punct="،"),
  v_pron("فَرَزَقَهُ", "razaqa", "رَزَقَ", "هُ", "pron-3ms", "«and granted him»", "«ve ona verdi»", fa=True, hidden="هُوَ", tags=[MX]),
  tok("وَلَدًا", "walad", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a son» — the second object.", "«bir evlât» — ikinci mef'ûl."),
  naat("رَاشِدًا", "rashid-upright", "«upright»", "«olgun»", case="nasb", tags=["ism-fail"], punct="،"),
])
sen("s5", "in whom genius and wisdom, forbearance and knowledge, and the Book came early, in childhood; and he was singled out for tenderness, righteousness, piety and dutifulness to his parents, for gentleness, a soft side and a lowered wing.",
        "onda dehâ ve hikmet, hilim ve ilim, ve Kitap daha çocuklukta erkenden belirdi; şefkat, salâh, takvâ ve ana babaya iyilikle, yumuşaklık, sığınılacak bir kanat ve alçakgönüllülükle ayrıcalandı.", [
  mazi("بَكَّرَ", "bakkara", "«came early»", "«erkenden belirdi»", tags=["jumla-sifa", "form-ii-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِوَلَدًا"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«in whom»", "«onda»"),
  fail("النُّبُوغُ", "nubugh", "«genius»", "«dehâ»"),
  atf("وَالْحِكْمَةُ", "hikma", "«wisdom»", "«hikmet»", "raf", punct="،"),
  atf("وَالْحِلْمُ", "hilm", "«forbearance»", "«hilim»", "raf"),
  atf("وَالْعِلْمُ", "ilm", "«knowledge»", "«ilim»", "raf", punct="،"),
  atf("وَالْكِتَابُ", "kitab", "«the Book»", "«Kitap»", "raf", punct="،"),
  fi(), majrur("الصِّغَرِ", "sighar", "«childhood»", "«çocuklukta»", punct="،"),
  tok("وَخُصَّ", "khassa-single-out", "verb", [AT, NF, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَخُصَّ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«and he was singled out» — a passive; the deputy doer concealed.", "«ve ayrıcalandı» — meçhul; nâib-i fâil gizli.", segments=wa_("خُصَّ", "khassa-single-out", "verb")),
  tok("بِالْحَنَانِ", "hanan", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَنَانِ مَجْرُورٌ.", "«for tenderness»", "«şefkatle»", segments=[seg("بِ", "bi", "prep"), seg("الْحَنَانِ", "hanan", "noun")]),
  atf("وَالصَّلَاحِ", "salah", "«righteousness»", "«salâh»", "jarr"),
  tok("وَالتَّقْوَى", "taqwa", "noun", [AT, "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالتَّقْوَى مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«and piety» — a maqṣūr noun, its kasra estimated.", "«ve takvâ» — maksûr isim.", segments=wa_("التَّقْوَى", "taqwa", "noun")),
  atf("وَالْبِرِّ", "birr", "«dutifulness»", "«iyilik»", "jarr"),
  tok("بِالْوَالِدَيْنِ", "walid-father", "noun", [HJ, "al-muthanna"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْوَالِدَيْنِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«to the parents» — jarr by the yāʾ (a dual).", "«ana babaya» — tesniye, yâ ile mecrûr.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْوَالِدَيْنِ", "walid-father", "noun")]),
  atf("وَالرِّقَّةِ", "riqqa", "«gentleness»", "«yumuşaklık»", "jarr"),
  atf("وَلِينِ", "lin", "«the softness [of]»", "«yumuşaklığı»", "jarr", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الْكَنَفِ", "kanaf", "«the side» (a sheltering wing)", "«kanadın, himâyenin»"),
  atf("وَخَفْضِ", "khafd", "«the lowering [of]»", "«alçaltılması»", "jarr", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الْجَنَاحِ", "janah", "«the wing» (humility)", "«kanadın» (tevâzu)", punct="."),
])
sen("s6", "And God strengthened Zakariyyā's heart and showed him signs pointing to God's vast power, and that He does what He wills,",
        "Allah Zekeriyyâ'nın kalbini pekiştirdi; ona Allah'ın geniş kudretine ve O'nun dilediğini yaptığına delâlet eden âyetler gösterdi;", [
  mazi("وَرَبَطَ", "rabata", "«and strengthened» (lit. bound)", "«ve pekiştirdi»", tags=[AT], wa=True, hidden=None),
  allah_fail(),
  prep("عَلَى", "ala", "«upon»", "«-ni»"),
  majrur("قَلْبِ", "qalb", "«the heart [of]»", "«kalbini»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  tok("زَكَرِيَّا", "zakariyya", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā»", "«Zekeriyyâ'nın»", punct="،"),
  tok("وَأَرَاهُ", "ara", "verb", [AT, MX, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَرَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and showed him» — arā takes two objects; the hāʾ is the first.", "«ve ona gösterdi» — erâ iki mef'ûl alır; hâ birincisi.", segments=[seg("وَ", "wa", "conj"), seg("أَرَى", "ara", "verb"), pr3ms()]),
  tok("آيَاتٍ", "aya", "noun", [MB, MX, JM], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«signs» — the second object; naṣb by kasra.", "«âyetler» — ikinci mef'ûl; cem-i müennes sâlim."),
  mudari("تَدُلُّ", "dalla", "«pointing»", "«delâlet eden»", tags=["jumla-sifa", "doubled-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِآيَاتٍ"),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  majrur("قُدْرَةِ", "qudra", "«the power [of]»", "«kudretine»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  naat("الْوَاسِعَةِ", "wasi-wide", "«vast»", "«geniş»", punct="،"),
  tok("وَأَنَّهُ", "anna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى قُدْرَةِ.", "«and that He» — the clause is joined to «the power».", "«ve O'nun … -dığına» — müevvel masdar «kudret»e atıf.", segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  mudari("يَفْعَلُ", "faala", "«does»", "«yapar»", tags=[IW, MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  ma_mawsul_obj(), yasha(punct="،"),
])
sen("s7", "and showed him His disposal over His creation and over the limbs of his own body: He moves what He wills and disables what He wills;",
        "ona yaratıkları üzerindeki ve kendi vücudunun uzuvları üzerindeki tasarrufunu gösterdi: dilediğini hareket ettirir, dilediğini işlemez kılar;", [
  tok("وَأَرَاهُ", "ara", "verb", [AT, MX, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَرَى فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and showed him»", "«ve ona gösterdi»", segments=[seg("وَ", "wa", "conj"), seg("أَرَى", "ara", "verb"), pr3ms()]),
  noun_pron("تَصَرُّفَهُ", "tasarruf", "تَصَرُّفَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His disposal» — the second object.", "«tasarrufunu» — ikinci mef'ûl.", tags=[MB, MX, ID]),
  fi(), noun_pron("خَلْقِهِ", "khalq", "خَلْقِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His creation»", "«yaratıkları»", tags=[HJ, ID]),
  tok("وَفِي", "fi", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and over»", "«ve … üzerinde»", segments=wa_("فِي", "fi", "prep")),
  majrur("أَعْضَاءِ", "udw", "«the limbs [of]»", "«uzuvları»", tags=[ID, JT], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  noun_pron("جِسْمِهِ", "jism", "جِسْمِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his body»", "«vücudunun»", tags=[ID]),
  mudari("يُحَرِّكُ", "harraka", "«He moves»", "«hareket ettirir»", tags=[HL, MB, "form-ii-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ (أَوْ تَفْسِيرٌ لِلتَّصَرُّفِ)"),
  ma_mawsul_obj(), yasha(),
  mudari("وَيُعَطِّلُ", "attala", "«and disables»", "«ve işlemez kılar»", tags=[AT, MB, "form-ii-verbs"], hidden="هُوَ"),
  ma_mawsul_obj(), yasha(punct="،"),
])
sen("s8", "and it became certain to him that the whole universe is in His hand: He brings the living out of the dead and the dead out of the living, and provides for whom He wills without reckoning.",
        "ve ona kesinleşti ki bütün kâinat O'nun elindedir: diriyi ölüden, ölüyü diriden çıkarır ve dilediğini hesapsız rızıklandırır.", [
  mazi("وَتَحَقَّقَ", "tahaqqaqa", "«and it became certain»", "«ve kesinleşti»", tags=[AT, "form-v-verbs"], wa=True, hidden=None),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»"),
  tok("أَنَّ", "anna", "part", [IW, FL], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ تَحَقَّقَ.", "«that» — the clause is the doer of «became certain».", "«… -dığı» — müevvel masdar «kesinleşti»nin fâili."),
  ism_inna("الْكَوْنَ", "kawn", "«the universe»", "«kâinat»", part="أَنَّ"),
  noun_pron("كُلَّهُ", "kull", "كُلَّ", "هُ", "pron-3ms", "تَوْكِيدٌ مَعْنَوِيٌّ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the whole of it» — an emphasis.", "«bütünü» — mânevî te'kid.", tags=["tawkid", ID]),
  noun_pron("بِيَدِهِ", "yad", "بِيَدِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَيَدِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«in His hand» — anna's khabar.", "«O'nun elinde» — enne'nin haberi.", tags=[HJ, ID, IW], punct="،"),
  mudari("يُخْرِجُ", "akhraja", "«He brings out»", "«çıkarır»", tags=[HL, MB, "form-iv-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  maful_("الْحَيَّ", "hayy", "«the living»", "«diriyi»"),
  prep("مِنَ", "min", "«out of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْمَيِّتِ", "mayyit", "«the dead»", "«ölüden»", punct="،"),
  mudari("وَيُخْرِجُ", "akhraja", "«and brings out»", "«ve çıkarır»", tags=[AT, MB, "form-iv-verbs"], hidden="هُوَ"),
  maful_("الْمَيِّتَ", "mayyit", "«the dead»", "«ölüyü»"),
  prep("مِنَ", "min", "«out of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْحَيِّ", "hayy", "«the living»", "«diriden»", punct="،"),
  mudari("وَيَرْزُقُ", "razaqa", "«and provides for»", "«ve rızıklandırır»", tags=[AT, MB], hidden="هُوَ"),
  tok("مَنْ", "man-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«whom» — the relative pronoun, the object.", "«… -i» — ism-i mevsûl, mef'ûl."),
  yasha(),
  tok("بِغَيْرِ", "ghayr", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«without»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  mudaf_ilayh("حِسَابٍ", "hisab", "«reckoning»", "«hesap»", punct="."),
])
# ---------------------------------------------------------------- §2 نَذْرُ امْرَأَةِ عِمْرَانَ (print p. 33)
sen("s9", "The wife of ʿImrān — of the family of our master Zakariyyā, peace be upon him; and she was a righteous woman who loved God and loved His religion — had vowed that if she bore a male she would give this child to God, for the service of His religion,",
        "İmrân'ın karısı — efendimiz Zekeriyyâ'nın (a.s.) ailesinden; Allah'ı ve O'nun dinini seven sâliha bir kadındı — bir erkek doğurursa bu çocuğu Allah'a, dininin hizmetine adayacağını adamıştı;", [
  tok("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("نَذَرَتِ", "nadhara", "verb", [MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«had vowed» — the tāʾ takes a kasra before the next hamzat al-waṣl.", "«adamıştı» — tâ iki sâkin yüzünden kesre aldı."),
  tok("امْرَأَةُ", "imraa", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — هَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«the wife [of]» — the doer; its hamza is a hamzat al-waṣl.", "«karısı» — fâil; hemzesi vasıl hemzesi."),
  tok("عِمْرَانَ", "imran", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«ʿImrān» — jarr by fatḥa (a diptote).", "«İmrân'ın» — gayr-i munsarıf."),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنِ امْرَأَةُ."),
  majrur("أُسْرَةِ", "usra-family", "«the family [of]»", "«ailesinden»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[ID]),
  tok("زَكَرِيَّا", "zakariyya", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Zakariyyā»", "«Zekeriyyâ'nın»"),
  *alayhi_salam(punct="،"),
  tok("وَكَانَتِ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ لِلْحَالِ (أَوْ عَاطِفَةٌ)، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«and she was» — kāna; its ism concealed.", "«ve o … idi» — kâne; ismi gizli.", segments=wa_("كَانَتِ", "kana", "verb")),
  tok("امْرَأَةً", "imraa", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a woman» — kāna's khabar.", "«bir kadın» — kâne'nin haberi."),
  naat("صَالِحَةً", "salih", "«righteous»", "«sâliha»", case="nasb", tags=["ism-fail"]),
  mudari("تُحِبُّ", "ahabba", "«who loved»", "«seven»", tags=["jumla-sifa", MB, "doubled-verbs", "form-iv-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ ثَانٍ"),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God»", "«Allah'ı»", punct="،"),
  mudari("وَتُحِبُّ", "ahabba", "«and loved»", "«ve seven»", tags=[AT, MB, "doubled-verbs", "form-iv-verbs"], hidden="هِيَ"),
  noun_pron("دِينَهُ", "din", "دِينَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His religion»", "«dinini»", tags=[MB, ID]),
  tok("أَنَّهَا", "anna", "part", [IW, MB], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ نَذَرَتْ.", "«that she» — the clause is the object of «had vowed».", "«… -acağını» — müevvel masdar «adadı»nın mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("إِذَا", "idha", "noun", [MF, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ.", "«if/when» — the conditional ẓarf.", "«-ırsa» — şart zarfı."),
  mazi_ta("وَلَدَتْ", "walada", "«she bore»", "«doğurursa»", tags=["idha-shartiyya", MB, "mithal-verbs"], extra=" — فِعْلُ الشَّرْطِ"),
  maful_("ذَكَرًا", "dhakar", "«a male»", "«bir erkek»"),
  mudari("تَهَبُ", "wahaba", "«she would give»", "«adayacak»", tags=[IW, MB, "mithal-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ أَنَّ، وَجَوَابُ إِذَا مَدْلُولٌ عَلَيْهِ"),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"),
  tok("الْوَلَدَ", "walad", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«child» — a badal.", "«çocuğu» — bedel."),
  tok("لِلّٰهِ", "allah", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«to God»", "«Allah'a»", punct=":", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("لِخِدْمَةِ", "khidma", "noun", [HJ, ID, BD], "اللَّامُ حَرْفُ جَرٍّ، وَخِدْمَةِ مَجْرُورٌ، مُضَافٌ — بَدَلٌ مِنْ لِلّٰهِ (بَدَلُ اشْتِمَالٍ).", "«for the service [of]» — a badal of «to God».", "«hizmetine» — «Allah'a»dan bedel.", segments=[seg("لِ", "li", "prep"), seg("خِدْمَةِ", "khidma", "noun")]),
  noun_pron("دِينِهِ", "din", "دِينِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His religion»", "«dininin»", tags=[ID], punct="،"),
])
sen("s10", "and she asked God to accept this child and to benefit His religion and His servants by him, and that he be a caller to God and an imām among the imāms of guidance:",
        "ve Allah'tan bu çocuğu kabul etmesini, onunla dinine ve kullarına fayda vermesini, onun Allah'a çağıran bir dâvetçi ve hidâyet imamlarından bir imam olmasını diledi:", [
  tok("وَسَأَلَتِ", "saala", "verb", [AT, MX], "الْوَاوُ عَاطِفَةٌ، وَسَأَلَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and she asked»", "«ve diledi»", segments=wa_("سَأَلَتِ", "saala", "verb")),
  tok("اللهَ", "allah", "propn", [MB, MX], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«God» — the first object.", "«Allah'tan» — birinci mef'ûl."),
  tok("أَنْ", "an-masdariyya", "part", [AN, MX], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ ثَانٍ.", "«to» — the clause is the second object.", "«… -mesini» — müevvel masdar ikinci mef'ûl."),
  tok("يَتَقَبَّلَ", "taqabbala", "verb", [AN, MB, "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«accept»", "«kabul etmesini»"),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"),
  tok("الْوَلَدَ", "walad", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«child»", "«çocuğu»"),
  tok("وَيَنْفَعَ", "nafaa", "verb", [AT, AN, MB], "الْوَاوُ عَاطِفَةٌ، وَيَنْفَعَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَتَقَبَّلَ.", "«and benefit» — naṣb by being joined to «accept».", "«ve fayda vermesini» — atıfla mansub.", segments=wa_("يَنْفَعَ", "nafaa", "verb")),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by him»", "«onunla»"),
  noun_pron("دِينَهُ", "din", "دِينَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His religion»", "«dinine»", tags=[MB, ID]),
  noun_pron("وَعِبَادَهُ", "abd", "وَعِبَادَ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَعِبَادَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His servants»", "«ve kullarına»", tags=[AT, ID, JT], punct="،"),
  tok("وَأَنْ", "an-masdariyya", "part", [AT, AN], "الْوَاوُ عَاطِفَةٌ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ مَعْطُوفٌ عَلَى الْأَوَّلِ.", "«and that»", "«ve … -masını»", segments=wa_("أَنْ", "an-masdariyya", "part")),
  tok("يَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«he be» — kāna's muḍāriʿ in naṣb.", "«olmasını» — kâne'nin muzarisi, mansub."),
  tok("دَاعِيًا", "dai", "noun", [KN, "ism-fail", "ism-maqsur-manqus"], "خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمٌ مَنْقُوصٌ تَظْهَرُ فَتْحَتُهُ.", "«a caller» — the khabar; a manqūṣ noun whose fatḥa shows.", "«bir dâvetçi» — haber; mankûs isim, fethası görünür."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى.", "«God»", "«Allah'a»"),
  atf("وَإِمَامًا", "imam", "«an imām»", "«bir imam»", "nasb"),
  prep("مِنْ", "min", "«among»", "«-den»"),
  majrur("أَئِمَّةِ", "imam", "«the imāms [of]»", "«imamlarından»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ — جَمْعُ إِمَامٍ."),
  tok("الْهُدَى", "huda", "noun", [ID, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "«guidance» — a maqṣūr noun.", "«hidâyet» — maksûr isim.", punct=":"),
])
# ---------------------------------------------------------------- §3 قَالَتْ رَبِّ إِنِّي وَضَعْتُهَا أُنْثَى (print pp. 33–34)
sen("s11", "The righteous woman intended one thing and God intended another, and God knows best what is good for His servants;",
        "Sâliha kadın bir şey murad etti, Allah da başka bir şey murad etti; Allah kullarının maslahatını en iyi bilendir;", [
  tok("وَأَرَادَتِ", "arada", "verb", [MB, "hollow-verbs", "form-iv-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَرَادَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and intended»", "«ve murad etti»", segments=wa_("أَرَادَتِ", "arada", "verb")),
  fail("الْمَرْأَةُ", "imraa", "«the woman»", "«kadın»", extra_ar=" — امْرَأَةٌ بِأَلْ: الْمَرْأَةُ"),
  naat("الصَّالِحَةُ", "salih", "«righteous»", "«sâliha»", case="raf", tags=["ism-fail"]),
  maful_("أَمْرًا", "amr", "«one thing»", "«bir şey»"),
  mazi("وَأَرَادَ", "arada", "«and intended»", "«da murad etti»", tags=[AT, MB, "hollow-verbs", "form-iv-verbs"], wa=True, hidden=None),
  allah_fail(),
  maful_("أَمْرًا", "amr", "«another»", "«başka bir şey»", punct="،"),
  tok("وَاللهُ", "allah", "propn", [AT, MK], "الْوَاوُ لِلْحَالِ (أَوْ عَاطِفَةٌ)، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.", "«and God» — the mubtadaʾ.", "«Allah» — mübtedâ.", segments=wa_("اللهُ", "allah", "propn")),
  tok("أَعْلَمُ", "alam-elative", "noun", [MK, "ism-tafdil", MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«knows best» — the khabar; an elative.", "«en iyi bilen» — haber; ism-i tafdîl."),
  tok("بِمَصْلَحَةِ", "maslaha", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَمَصْلَحَةِ مَجْرُورٌ، مُضَافٌ.", "«what is good [for]»", "«maslahatını»", segments=[seg("بِ", "bi", "prep"), seg("مَصْلَحَةِ", "maslaha", "noun")]),
  noun_pron("عِبَادِهِ", "abd", "عِبَادِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His servants»", "«kullarının»", tags=[ID, JT], punct="،"),
])
sen("s12", "and lo, she gives birth to a female, and grieves at that, and gloom covers her;",
        "bir de ne görsün, bir kız doğurur; buna üzülür, onu bir keder kaplar;", [
  tok("فَإِذَا", "idha-fujaiyya", "part", [AT, "huruf-tanbih"], "الْفَاءُ عَاطِفَةٌ، وَإِذَا لِلْمُفَاجَأَةِ (حَرْفٌ عِنْدَ الْأَخْفَشِ، ظَرْفُ مَكَانٍ عِنْدَ الْمُبَرِّدِ).", "«and lo» — the idhā of surprise.", "«bir de ne görsün» — mufâcee izâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha-fujaiyya", "part")]),
  tok("هِيَ", "hiya", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«she» — the mubtadaʾ.", "«o» — mübtedâ."),
  mudari("تَلِدُ", "walada", "«gives birth to»", "«doğurur»", tags=[MK, MB, "mithal-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ"),
  tok("أُنْثَى", "untha", "noun", [MB, "ism-maqsur-manqus", MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ.", "«a female» — the object; a diptote by the feminine alif.", "«bir kız» — mef'ûl; te'nis elifiyle gayr-i munsarıf.", punct="،"),
  mudari("فَتَحْزَنُ", "hazina", "«and grieves»", "«ve üzülür»", tags=[AT], hidden="هِيَ"),
  tok("لِذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«at that»", "«buna»", segments=[seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("وَتَغْشَاهَا", "ghashiya", "verb", [AT, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَغْشَى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«and covers her» — the pronoun is the object, fronted.", "«ve onu kaplar» — zamir öne alınmış mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("تَغْشَى", "ghashiya", "verb"), seg("هَا", "pron-3fs", "pron")]),
  fail("الْكَآبَةُ", "kaaba-gloom", "«gloom»", "«keder»", punct="،", extra_ar=" مُؤَخَّرٌ"),
])
sen("s13", "but the newborn girl was not like every female; rather she was stronger in worship, and higher in resolve for acts of obedience and good works, than many a young man;",
        "fakat o kız çocuğu her kız gibi değildi; aksine ibadette nice gençten daha güçlü, tâatlerde ve hayırlarda daha yüksek himmetliydi;", [
  tok("وَلٰكِنَّ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, which governs like inna.", "«fakat» — inne gibi amel eden istidrâk harfi.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  ism_inna("الْوَلِيدَةَ", "walida", "«the newborn girl»", "«kız çocuğu»", part="لٰكِنَّ"),
  tok("لَمْ", "lam-jazima", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«değildi»"),
  tok("تَكُنْ", "kana", "verb", [LJ, KN, IW, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ لٰكِنَّ.", "«was» — kāna's muḍāriʿ in jazm; its wāw dropped before the sukūn.", "«idi» — kâne'nin meczûm muzarisi; vâvı düştü."),
  tok("كَكُلِّ", "kull", "noun", [HJ, ID, KN], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَكُلِّ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ تَكُنْ.", "«like every» — the phrase is kāna's khabar.", "«her … gibi» — câr-mecrûr kâne'nin haberi.", segments=[seg("كَ", "ka", "prep"), seg("كُلِّ", "kull", "noun")]),
  tok("أُنْثَى", "untha", "noun", [ID, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«female»", "«kız»", punct="،"),
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ وَابْتِدَاءٍ.", "«rather» — the particle of turning-away.", "«aksine» — idrâb harfi."),
  tok("كَانَتْ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«she was»", "«o … idi»"),
  tok("أَقْوَى", "aqwa", "noun", [KN, "ism-tafdil", "ism-maqsur-manqus", MM], "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمُ تَفْضِيلٍ.", "«stronger» — kāna's khabar; an elative.", "«daha güçlü» — kâne'nin haberi; ism-i tafdîl."),
  prep("عَلَى", "ala", "«in»", "«-de»"),
  majrur("الْعِبَادَةِ", "ibada", "«worship»", "«ibadet»", punct="،"),
  tok("وَأَعْلَى", "ala-highest", "noun", [AT, KN, "ism-tafdil", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَأَعْلَى مَعْطُوفٌ عَلَى أَقْوَى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«and higher»", "«ve daha yüksek»", segments=wa_("أَعْلَى", "ala-highest", "noun")),
  tok("هِمَّةً", "himma", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ جِهَةَ التَّفْضِيلِ.", "«in resolve» — the tamyīz of the elative.", "«himmetçe» — ism-i tafdîlin temyizi."),
  fi(), majrur("الطَّاعَاتِ", "taa", "«acts of obedience»", "«tâatlerde»", tags=[JM]),
  atf("وَالْخَيْرَاتِ", "khayr", "«good works»", "«hayırlarda»", "jarr", tags=[JM], punct="،"),
  prep("مِنْ", "min", "«than»", "«-den»", ar="حَرْفُ جَرٍّ — مِنْ بَعْدَ اسْمِ التَّفْضِيلِ تَجُرُّ الْمُفَضَّلَ عَلَيْهِ."),
  majrur("كَثِيرٍ", "kathir", "«many»", "«nice»"),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْفِتْيَانِ", "fata-youth", "«young men»", "«gençler»", tags=[JT], punct="،"),
])
sen("s14", "and if God had decreed — for a wisdom He knows — that she be a female, while prophethood's burdens are shouldered by none but men, then God had decreed that she be mother to a righteous prophet who would have standing:",
        "ve Allah — bildiği bir hikmetle — onun kız olmasını takdir ettiyse, peygamberliğin yüklerini de ancak erkekler taşıyorsa, Allah onun büyük bir şanı olacak sâlih bir peygambere anne olmasını takdir etmişti:", [
  tok("وَإِذَا", "idha", "noun", [AT, MF, "idha-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ خَافِضٌ لِشَرْطِهِ.", "«and if» — the conditional ẓarf.", "«ve … -ise» — şart zarfı.", segments=wa_("إِذَا", "idha", "noun")),
  mazi("قَدَّرَ", "qaddara", "«decreed»", "«takdir etti»", tags=["idha-shartiyya", MB, "form-ii-verbs"], hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ"),
  allah_fail(),
  tok("لِحِكْمَةٍ", "hikma", "noun", [HJ, "jumla-mutarida"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَحِكْمَةٍ مَجْرُورٌ — اعْتِرَاضٌ.", "«for a wisdom» — a parenthesis.", "«bir hikmetle» — itirâz cümlesi.", segments=[seg("لِ", "li", "prep"), seg("حِكْمَةٍ", "hikma", "noun")]),
  tok("يَعْلَمُهَا", "alima", "verb", ["jumla-sifa", "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ لِحِكْمَةٍ.", "«He knows» — the clause describes «a wisdom».", "«bildiği» — cümle «hikmet»in sıfatı.", segments=[seg("يَعْلَمُ", "alima", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", [AN, MB], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ قَدَّرَ.", "«that» — the clause is the object of «decreed».", "«… -masını» — müevvel masdar mef'ûl."),
  tok("تَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«she be»", "«olmasını»"),
  tok("أُنْثَى", "untha", "noun", [KN, "ism-maqsur-manqus"], "خَبَرُ تَكُونَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«a female» — the khabar.", "«kız» — haber.", punct="،"),
  tok("وَالنُّبُوَّةُ", "nubuwwa", "noun", [HL, MK], "الْوَاوُ لِلْحَالِ، وَالنُّبُوَّةُ مُبْتَدَأٌ مَرْفُوعٌ — وَالْجُمْلَةُ حَالٌ.", "«while prophethood» — a circumstantial clause's mubtadaʾ.", "«peygamberlik ise» — hâl cümlesinin mübtedâsı.", segments=wa_("النُّبُوَّةُ", "nubuwwa", "noun")),
  la_nafiya(),
  mudari("يَضْطَلِعُ", "idtalaa", "«is shouldered»", "«taşınır»", tags=["la-nafiya", MK, "form-viii-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ خَبَرٌ؛ اضْطَلَعَ: افْتَعَلَ مِنْ ضَلَعَ، قُلِبَتْ تَاؤُهُ طَاءً"),
  noun_pron("بِأَعْبَائِهَا", "ib", "بِأَعْبَائِ", "هَا", "pron-3fs", "الْبَاءُ حَرْفُ جَرٍّ، وَأَعْبَائِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its burdens»", "«yüklerini»", tags=[HJ, ID, JT]),
  tok("إِلَّا", "illa", "part", ["istithna", "istithna-mufarragh"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«but» — an emptied exception.", "«ancak» — müferrağ istisnâ."),
  fail("الرِّجَالُ", "rijal", "«men»", "«erkekler»", tags=[JT], punct="،"),
  tok("فَقَدْ", "qad", "part", [AT, "qad-harf", "jawab-al-talab"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«then [indeed]» — the fāʾ of idhā's answer.", "«o halde» — izâ'nın cevap fâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("قَدَّرَ", "qaddara", "«had decreed»", "«takdir etmişti»", tags=["idha-shartiyya", MB, "form-ii-verbs"], hidden=None, extra_ar=" — جَوَابُ إِذَا"),
  allah_fail(),
  tok("أَنْ", "an-masdariyya", "part", [AN, MB], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ قَدَّرَ.", "«that»", "«… -masını»"),
  tok("تَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«she be»", "«olmasını»"),
  tok("أُمًّا", "umm", "noun", [KN], "خَبَرُ تَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«mother» — the khabar.", "«anne» — haber."),
  tok("لِنَبِيٍّ", "nabi", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَنَبِيٍّ مَجْرُورٌ.", "«to a prophet»", "«bir peygambere»", segments=[seg("لِ", "li", "prep"), seg("نَبِيٍّ", "nabi", "noun")]),
  naat("صَالِحٍ", "salih", "«righteous»", "«sâlih»", tags=["ism-fail"]),
  tok("يَكُونُ", "kana", "verb", ["jumla-sifa", KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِنَبِيٍّ.", "«who would have» — the clause is a second naʿt.", "«olacak» — ikinci sıfat cümlesi."),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him» — the fronted khabar.", "«onun» — öne alınmış haber.", tags=[KN], extra=" — خَبَرُ يَكُونُ مُقَدَّمٌ"),
  tok("شَأْنٌ", "shan", "noun", [KN], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ.", "«standing» — kāna's delayed ism.", "«bir şan» — kâne'nin ismi.", punct=":"),
])
sen("s15", "«When the wife of ʿImrān said: My Lord, I have vowed to You what is in my womb, consecrated; so accept it from me; indeed You are the All-Hearing, the All-Knowing» (3:35).",
        "«Hani İmrân'ın karısı: Rabbim, karnımdakini sırf Sana hizmet için adadım; benden kabul et; şüphesiz Sen her şeyi işiten, bilensin, demişti» (3:35).", [
  *quran([
  tok("إِذْ", "idh", "noun", [MF, "hadhf-wa-taqdir"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ.", "«when» — the object of an unspoken «remember».", "«hani» — mahzuf «an»ın mef'ûlü."),
  tok("قَالَتِ", "qala", "verb", [ID, "hollow-verbs", MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ.", "«said» — the clause is annexed to idh.", "«demişti» — cümle iz'e muzâfun ileyh."),
  tok("امْرَأَتُ", "imraa", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — رُسِمَتْ تَاؤُهَا مَفْتُوحَةً فِي الْمُصْحَفِ.", "«the wife [of]» — the doer; written with an open tāʾ in the muṣḥaf.", "«karısı» — fâil; mushafta açık tâ ile yazılır."),
  tok("عِمْرَانَ", "imran", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«ʿImrān»", "«İmrân'ın»"),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ.", "«my Lord» — a vocative annexed to the dropped yāʾ; the vocative particle is unspoken.", "«Rabbim» — münâdâ; mütekellim yâsı düşmüş; nidâ harfi mahzuf."),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«şüphesiz ben»", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("نَذَرْتُ", "nadhara", "verb", [IW, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I have vowed» — the tāʾ is the doer; the clause is inna's khabar.", "«adadım» — tâ fâil; cümle inne'nin haberi.", segments=[seg("نَذَرْ", "nadhara", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("لَكَ", "li", "prep", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ.", "«to You»", "«Sana»", segments=[seg("لَ", "li", "prep"), seg("كَ", "pron-2ms", "pron")]),
  tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the object.", "«… -ni» — mef'ûl."),
  tok("فِي", "fi", "prep", [HJ, MW], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةُ الْمَوْصُولِ.", "«in» — the ṣila.", "«-de» — sıla."),
  noun_pron("بَطْنِي", "batn", "بَطْنِ", "ي", "pron-1s", "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my womb»", "«karnım»", tags=[HJ, ID]),
  hal("مُحَرَّرًا", "muharrar", "«consecrated» (freed for the temple's service)", "«sırf hizmete adanmış»", tags=["ism-maful"]),
  tok("فَتَقَبَّلْ", "taqabbala", "verb", [AT, AM, "form-v-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَتَقَبَّلْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَالْأَمْرُ لِلدُّعَاءِ.", "«so accept» — an imperative of supplication.", "«kabul et» — duâ emri.", segments=[seg("فَ", "fa", "conj"), seg("تَقَبَّلْ", "taqabbala", "verb")]),
  tok("مِنِّي", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ جَرٍّ.", "«from me» — with the protecting nūn.", "«benden» — vikâye nûnu ile.", segments=[seg("مِنْ", "min", "prep"), seg("نِي", "pron-1s", "pron")]),
  tok("إِنَّكَ", "inna", "part", [IW], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا.", "«indeed You»", "«şüphesiz Sen»", segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَنْتَ", "anta", "pron", ["damir-fasl"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ (أَوْ مُبْتَدَأٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ).", "«You» — the pronoun of separation.", "«Sen» — fasıl zamiri."),
  khabar_inna("السَّمِيعُ", "sami", "«the All-Hearing»", "«her şeyi işiten»", tags=["sighat-mubalagha"]),
  khabar_inna("الْعَلِيمُ", "alim", "«the All-Knowing»", "«bilen»", extra=" ثَانٍ", punct="."),
  ]),
])
sen("s16", "«Then when she delivered her she said: My Lord, I have delivered a female — and God knew best what she delivered — and the male is not like the female; and I have named her Maryam, and I commend her and her offspring to Your protection from the accursed Satan» (3:36).",
        "«Onu doğurunca: Rabbim, onu kız doğurdum, dedi — Allah onun ne doğurduğunu daha iyi biliyordu — erkek kız gibi değildir; ona Meryem adını verdim; onu ve soyunu kovulmuş şeytandan Sana sığındırırım» (3:36).", [
  *quran([
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«then when»", "«… -ınca»", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  ta_pron("وَضَعَتْهَا", "wadaa", "وَضَعَتْ", "هَا", "pron-3fs", "«she delivered her»", "«onu doğurdu»", tags=["mithal-verbs", SH]),
  tok("قَالَتْ", "qala", "verb", [SH, "hollow-verbs", MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — جَوَابُ لَمَّا.", "«she said» — lammā's answer.", "«dedi» — lemmâ'nın cevabı."),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ.", "«my Lord»", "«Rabbim»"),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«ben»", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("وَضَعْتُهَا", "wadaa", "verb", [IW, MB, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I have delivered her»", "«onu doğurdum»", segments=[seg("وَضَعْ", "wadaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("هَا", "pron-3fs", "pron")]),
  hal("أُنْثَى", "untha", "«a female»", "«kız olarak»", ar="حَالٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ."),
  tok("وَاللهُ", "allah", "propn", [MK, "jumla-mutarida"], "الْوَاوُ لِلِاعْتِرَاضِ، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«and God» — a parenthetical clause.", "«Allah» — itirâz cümlesi.", segments=wa_("اللهُ", "allah", "propn")),
  tok("أَعْلَمُ", "alam-elative", "noun", [MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«knew best»", "«daha iyi bilir»"),
  tok("بِمَا", "ma-mawsula", "pron", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«ne … -duğunu»", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  mazi_ta("وَضَعَتْ", "wadaa", "«she delivered»", "«doğurdu»", tags=[MW, "mithal-verbs"], extra=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  tok("وَلَيْسَ", "laysa", "verb", [AT, KN, "ma-la-mushabbaha"], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَ فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«and is not» — laysa.", "«ve değildir» — leyse.", segments=wa_("لَيْسَ", "laysa", "verb")),
  tok("الذَّكَرُ", "dhakar", "noun", [KN], "اسْمُ لَيْسَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the male» — laysa's ism.", "«erkek» — leyse'nin ismi."),
  tok("كَالْأُنْثَى", "untha", "noun", [HJ, KN, "ism-maqsur-manqus"], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَالْأُنْثَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ.", "«like the female» — laysa's khabar.", "«kız gibi» — leyse'nin haberi.", segments=[seg("كَ", "ka", "prep"), seg("الْأُنْثَى", "untha", "noun")]),
  tok("وَإِنِّي", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ، وَالْيَاءُ اسْمُهَا.", "«and I»", "«ve ben»", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("سَمَّيْتُهَا", "samma", "verb", [IW, MX, "naqis-verbs", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ أَوَّلُ.", "«I have named her» — the hāʾ is the first object.", "«ona … adını verdim» — hâ birinci mef'ûl.", segments=[seg("سَمَّيْ", "samma", "verb"), seg("تُ", "pron-1s", "pron"), seg("هَا", "pron-3fs", "pron")]),
  tok("مَرْيَمَ", "maryam", "propn", [MB, MX, MM], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Maryam» — the second object; a diptote name.", "«Meryem» — ikinci mef'ûl; gayr-i munsarıf."),
  tok("وَإِنِّي", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ، وَالْيَاءُ اسْمُهَا.", "«and I»", "«ve ben»", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أُعِيذُهَا", "aadha", "verb", [IW, MB, "mudari-marfu", "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I commend her to protection»", "«onu sığındırırım»", segments=[seg("أُعِيذُ", "aadha", "verb"), seg("هَا", "pron-3fs", "pron")]),
  prep_pron("بِكَ", "bi", "كَ", "pron-2ms", "«to You»", "«Sana»"),
  noun_pron("وَذُرِّيَّتَهَا", "dhurriyya", "وَذُرِّيَّتَ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَذُرِّيَّتَ مَعْطُوفٌ عَلَى هَا مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her offspring»", "«ve soyunu»", tags=[AT, ID]),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الشَّيْطَانِ", "shaytan", "«Satan»", "«şeytan»"),
  naat("الرَّجِيمِ", "rajim", "«the accursed»", "«kovulmuş»", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: radi-pleasing, shayb-greyness, rashid-upright, usra-family, alam-elative, kaaba-gloom, fata-youth take suffixed keys; ala-bounties, ala-highest, khassa-single-out, walid-father, dai, huda, lakinna, imraa, alim, sami reused)
CAND = {
 "lawn": G("lawn", "لَوْن", "ل و ن", "noun", "a colour; a kind", "renk; tür", 1),
 "akhar": G("akhar", "آخَر", "أ خ ر", "noun", "another, other (a diptote)", "başka, diğer (gayr-i munsarıf)", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "ala-bounties": G("ala-bounties", "آلَاء", "أ ل و", "noun", "bounties, favours (a plural)", "nimetler (çoğul)", 3),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant", "kul", 1, plural="عِبَاد"),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, alâmet", 1, plural="آيَات"),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "ahata": G("ahata", "أَحَاطَ", "ح و ط", "verb", "to encompass (Form IV, hollow)", "kuşatmak (if'âl, ecvef)", 2),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1),
 "tajalla": G("tajalla", "تَجَلَّى", "ج ل و", "verb", "to show itself, to be manifested (Form V, defective)", "tecelli etmek (tefa''ul, nâkıs)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "a prayer, supplication", "duâ", 1),
 "zakariyya": G("zakariyya", "زَكَرِيَّا", None, "propn", "Zakariyyā (Zechariah)", "Zekeriyyâ", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child, a son", "evlât, çocuk", 1, plural="أَوْلَاد"),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous (an active participle)", "sâlih (ism-i fâil)", 1),
 "radi-pleasing": G("radi-pleasing", "رَضِيّ", "ر ض و", "noun", "well-pleasing, agreeable", "hoşnut edici, beğenilen", 3),
 "barr": G("barr", "بَرّ", "ب ر ر", "noun", "dutiful, pious", "iyi, itaatkâr", 2),
 "taqi": G("taqi", "تَقِيّ", "و ق ي", "noun", "God-fearing, pious", "takvâlı, müttaki", 2),
 "waritha": G("waritha", "وَرِثَ", "و ر ث", "verb", "to inherit (an assimilated verb)", "vâris olmak (misâl fiil)", 1),
 "al-family": G("al-family", "آل", "أ و ل", "noun", "the family, the House (of)", "âl, hânedan", 1),
 "yaqub": G("yaqub", "يَعْقُوب", None, "propn", "Yaʿqūb (Jacob)", "Ya'kûb", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to stand up; (bi-) to take up (hollow)", "kalkmak; (bi ile) üstlenmek (ecvef)", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "the call, the mission", "davet", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "hin": G("hin", "حِين", "ح ي ن", "noun", "a time, a while; when (as a ẓarf)", "zaman, vakit; -dığı zaman (zarf)", 1),
 "taqaddama": G("taqaddama", "تَقَدَّمَ", "ق د م", "verb", "to advance (Form V)", "ilerlemek (tefa''ul)", 2),
 "sinn": G("sinn", "سِنّ", "س ن ن", "noun", "age; a tooth", "yaş; diş", 1),
 "wahana": G("wahana", "وَهَنَ", "و ه ن", "verb", "to grow weak (an assimilated verb)", "zayıflamak (misâl fiil)", 3),
 "azm": G("azm", "عَظْم", "ع ظ م", "noun", "a bone", "kemik", 1),
 "lajja": G("lajja", "لَجَّ", "ل ج ج", "verb", "to persist, to settle in (doubled)", "ısrar etmek, iyice yerleşmek (muzâaf)", 3),
 "shayb-greyness": G("shayb-greyness", "شَيْب", "ش ي ب", "noun", "grey hair, old age", "ak saç, ihtiyarlık", 2),
 "inqataa": G("inqataa", "اِنْقَطَعَ", "ق ط ع", "verb", "to be cut off (Form VII)", "kesilmek (infiâl)", 2),
 "raja-hope": G("raja-hope", "رَجَاء", "ر ج و", "noun", "hope, expectation", "ümit, beklenti", 2),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to give birth (an assimilated verb)", "doğurmak (misâl fiil)", 1),
 "zawj": G("zawj", "زَوْج", "ز و ج", "noun", "a spouse (husband or wife)", "eş (koca veya karı)", 1),
 "ajaba": G("ajaba", "أَجَابَ", "ج و ب", "verb", "to answer (Form IV, hollow)", "cevap vermek, icabet etmek (if'âl, ecvef)", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "kadhdhaba": G("kadhdhaba", "كَذَّبَ", "ك ذ ب", "verb", "to give the lie to, to deny (Form II)", "yalanlamak (tef'îl)", 1),
 "zann": G("zann", "ظَنّ", "ظ ن ن", "noun", "a supposition", "zan", 1, plural="ظُنُون"),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "abtala": G("abtala", "أَبْطَلَ", "ب ط ل", "verb", "to nullify, to set aside (Form IV)", "boşa çıkarmak, geçersiz kılmak (if'âl)", 2),
 "tajriba": G("tajriba", "تَجْرِبَة", "ج ر ب", "noun", "an experience, an experiment", "tecrübe", 2, plural="تَجَارِب"),
 "qadim": G("qadim", "قَدِيم", "ق د م", "noun", "old, ancient", "eski", 1),
 "razaqa": G("razaqa", "رَزَقَ", "ر ز ق", "verb", "to provide for, to grant", "rızıklandırmak, vermek", 1),
 "rashid-upright": G("rashid-upright", "رَاشِد", "ر ش د", "noun", "upright, rightly guided (an active participle)", "olgun, doğru yolda (ism-i fâil)", 2),
 "bakkara": G("bakkara", "بَكَّرَ", "ب ك ر", "verb", "to come early (Form II)", "erken gelmek, erkenden belirmek (tef'îl)", 3),
 "nubugh": G("nubugh", "نُبُوغ", "ن ب غ", "noun", "genius, brilliance", "dehâ, üstün zekâ", 3),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "hilm": G("hilm", "حِلْم", "ح ل م", "noun", "forbearance", "hilim", 2),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a book; the Book", "kitap", 1),
 "sighar": G("sighar", "صِغَر", "ص غ ر", "noun", "childhood, smallness", "çocukluk, küçüklük", 2),
 "khassa-single-out": G("khassa-single-out", "خَصَّ", "خ ص ص", "verb", "to single out (doubled)", "tahsis etmek, ayrıcalı kılmak (muzâaf)", 2),
 "hanan": G("hanan", "حَنَان", "ح ن ن", "noun", "tenderness", "şefkat", 2),
 "salah": G("salah", "صَلَاح", "ص ل ح", "noun", "righteousness", "salâh", 1),
 "taqwa": G("taqwa", "تَقْوَى", "و ق ي", "noun", "piety (a maqṣūr noun)", "takvâ (maksûr)", 1),
 "birr": G("birr", "بِرّ", "ب ر ر", "noun", "dutifulness, kindness", "iyilik, birr", 1),
 "walid-father": G("walid-father", "وَالِد", "و ل د", "noun", "a father; (dual) the parents", "baba; (tesniye) ana baba", 1),
 "riqqa": G("riqqa", "رِقَّة", "ر ق ق", "noun", "gentleness, tenderness", "yumuşaklık, rikkat", 2),
 "lin": G("lin", "لِين", "ل ي ن", "noun", "softness", "yumuşaklık", 2),
 "kanaf": G("kanaf", "كَنَف", "ك ن ف", "noun", "a side, a sheltering wing", "kanat, himâye", 3),
 "khafd": G("khafd", "خَفْض", "خ ف ض", "noun", "lowering; (nahw) jarr", "alçaltma; (nahivde) cer", 2),
 "janah": G("janah", "جَنَاح", "ج ن ح", "noun", "a wing", "kanat", 1),
 "rabata": G("rabata", "رَبَطَ", "ر ب ط", "verb", "to bind; (ʿalā qalb) to strengthen the heart", "bağlamak; (kalbi) pekiştirmek", 2),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "a heart", "kalp", 1),
 "ara": G("ara", "أَرَى", "ر أ ي", "verb", "to show (Form IV, defective; two objects)", "göstermek (if'âl, nâkıs; iki mef'ûl)", 1),
 "dalla": G("dalla", "دَلَّ", "د ل ل", "verb", "to point to, to indicate (doubled)", "delâlet etmek (muzâaf)", 1),
 "wasi-wide": G("wasi-wide", "وَاسِع", "و س ع", "noun", "wide, vast (an active participle)", "geniş (ism-i fâil)", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that", "-dığını", 1),
 "faala": G("faala", "فَعَلَ", "ف ع ل", "verb", "to do", "yapmak", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will (hollow, hamzated)", "dilemek (ecvef, mehmûz)", 1),
 "tasarruf": G("tasarruf", "تَصَرُّف", "ص ر ف", "noun", "disposal, free action", "tasarruf", 2),
 "khalq": G("khalq", "خَلْق", "خ ل ق", "noun", "creation; creatures", "yaratma; yaratıklar", 1),
 "udw": G("udw", "عُضْو", "ع ض و", "noun", "a limb, an organ", "uzuv, organ", 2, plural="أَعْضَاء"),
 "jism": G("jism", "جِسْم", "ج س م", "noun", "a body", "beden, vücut", 1),
 "harraka": G("harraka", "حَرَّكَ", "ح ر ك", "verb", "to move (something) (Form II)", "hareket ettirmek (tef'îl)", 2),
 "attala": G("attala", "عَطَّلَ", "ع ط ل", "verb", "to disable, to put out of action (Form II)", "işlemez kılmak, atıl bırakmak (tef'îl)", 3),
 "tahaqqaqa": G("tahaqqaqa", "تَحَقَّقَ", "ح ق ق", "verb", "to make sure; (lahu) to become certain to (Form V)", "iyice anlamak; (lehû) kesinleşmek (tefa''ul)", 2),
 "kawn": G("kawn", "كَوْن", "ك و ن", "noun", "the universe; being", "kâinat; varlık", 2),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1),
 "akhraja": G("akhraja", "أَخْرَجَ", "خ ر ج", "verb", "to bring out (Form IV)", "çıkarmak (if'âl)", 1),
 "hayy": G("hayy", "حَيّ", "ح ي ي", "noun", "living, alive", "diri, canlı", 1),
 "mayyit": G("mayyit", "مَيِّت", "م و ت", "noun", "dead", "ölü", 1),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "whoever, he who", "kim ki, … kimse", 1),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not, without", "başka; gayri, -sız", 1),
 "hisab": G("hisab", "حِسَاب", "ح س ب", "noun", "reckoning", "hesap", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "nadhara": G("nadhara", "نَذَرَ", "ن ذ ر", "verb", "to vow", "adamak, nezretmek", 2),
 "imraa": G("imraa", "اِمْرَأَة", "م ر أ", "noun", "a woman, a wife (with al: الْمَرْأَة)", "kadın, karı (harf-i târifle: el-mer'e)", 1),
 "imran": G("imran", "عِمْرَان", None, "propn", "ʿImrān", "İmrân", 2),
 "usra-family": G("usra-family", "أُسْرَة", "أ س ر", "noun", "a family", "aile", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "salam": G("salam", "سَلَام", "س ل م", "noun", "peace; safety", "selâm; selâmet", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "ahabba": G("ahabba", "أَحَبَّ", "ح ب ب", "verb", "to love (Form IV, doubled)", "sevmek (if'âl, muzâaf)", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ırsa", 1),
 "dhakar": G("dhakar", "ذَكَر", "ذ ك ر", "noun", "a male", "erkek", 1),
 "wahaba": G("wahaba", "وَهَبَ", "و ه ب", "verb", "to give, to grant (an assimilated verb)", "bağışlamak, vermek (misâl)", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "khidma": G("khidma", "خِدْمَة", "خ د م", "noun", "service", "hizmet", 1),
 "saala": G("saala", "سَأَلَ", "س أ ل", "verb", "to ask", "sormak, istemek", 1),
 "taqabbala": G("taqabbala", "تَقَبَّلَ", "ق ب ل", "verb", "to accept (Form V)", "kabul etmek (tefa''ul)", 1),
 "nafaa": G("nafaa", "نَفَعَ", "ن ف ع", "verb", "to benefit", "fayda vermek", 1),
 "dai": G("dai", "دَاعٍ (الدَّاعِي)", "د ع و", "noun", "a caller, a summoner (a manqūṣ participle)", "dâvetçi, çağıran (mankûs ism-i fâil)", 2),
 "imam": G("imam", "إِمَام", "أ م م", "noun", "an imām, a leader", "imam, önder", 1, plural="أَئِمَّة"),
 "huda": G("huda", "هُدًى", "ه د ي", "noun", "guidance (a maqṣūr noun)", "hidâyet (maksûr)", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to intend, to want (Form IV, hollow)", "istemek, murad etmek (if'âl, ecvef)", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1),
 "alam-elative": G("alam-elative", "أَعْلَم", "ع ل م", "noun", "most knowing, knows best (an elative)", "en iyi bilen (ism-i tafdîl)", 1),
 "maslaha": G("maslaha", "مَصْلَحَة", "ص ل ح", "noun", "what is good, benefit", "maslahat, iyilik", 2),
 "idha-fujaiyya": G("idha-fujaiyya", "إِذَا (الْفُجَائِيَّة)", None, "part", "lo!, and suddenly — the idhā of surprise", "bir de ne görsün — mufâcee izâ'sı", 2),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it (f.)", "o (müennes)", 1),
 "untha": G("untha", "أُنْثَى", "أ ن ث", "noun", "a female (a diptote)", "dişi, kız (gayr-i munsarıf)", 1),
 "hazina": G("hazina", "حَزِنَ", "ح ز ن", "verb", "to grieve", "üzülmek", 1),
 "ghashiya": G("ghashiya", "غَشِيَ", "غ ش ي", "verb", "to cover, to overwhelm (defective)", "bürümek, kaplamak (nâkıs)", 2),
 "kaaba-gloom": G("kaaba-gloom", "كَآبَة", "ك أ ب", "noun", "gloom, dejection", "keder, kasvet", 3),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but — governs like inna", "fakat — inne gibi amel eder", 1),
 "walida": G("walida", "وَلِيدَة", "و ل د", "noun", "a newborn girl", "yeni doğmuş kız", 3),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "not (of the past) — the jazm lam", "-madı — cezm eden lem", 1),
 "ka": G("ka", "كَ", None, "prep", "like, as", "gibi", 1),
 "bal": G("bal", "بَلْ", None, "part", "rather, nay", "aksine, bilakis", 1),
 "aqwa": G("aqwa", "أَقْوَى", "ق و ي", "noun", "stronger, strongest (an elative)", "daha güçlü (ism-i tafdîl)", 2),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet", 1),
 "ala-highest": G("ala-highest", "أَعْلَى", "ع ل و", "noun", "higher, highest (an elative)", "daha yüksek, en yüce (ism-i tafdîl)", 1),
 "himma": G("himma", "هِمَّة", "ه م م", "noun", "resolve, aspiration", "himmet", 2),
 "taa": G("taa", "طَاعَة", "ط و ع", "noun", "obedience", "tâat, itaat", 1, plural="طَاعَات"),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good; (pl.) good works", "hayır; (ç.) hayırlar", 1, plural="خَيْرَات"),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "much, many", "çok", 1),
 "fata-youth": G("fata-youth", "فَتًى", "ف ت ي", "noun", "a young man (a maqṣūr noun)", "genç, delikanlı (maksûr)", 1, plural="فِتْيَان"),
 "qaddara": G("qaddara", "قَدَّرَ", "ق د ر", "verb", "to decree, to ordain (Form II)", "takdir etmek (tef'îl)", 1),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know", "bilmek", 1),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب أ", "noun", "prophethood", "peygamberlik, nübüvvet", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "idtalaa": G("idtalaa", "اِضْطَلَعَ", "ض ل ع", "verb", "to shoulder, to take on (Form VIII, with the tāʾ turned into ṭāʾ)", "yüklenmek, üstlenmek (iftiâl; tâ'sı tâ'ya dönmüş)", 3),
 "ib": G("ib", "عِبْء", "ع ب أ", "noun", "a burden", "yük", 3, plural="أَعْبَاء"),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "rijal": G("rijal", "رِجَال", "ر ج ل", "noun", "men (the plural of rajul)", "erkekler, adamlar (racül'ün çoğulu)", 1),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "shan": G("shan", "شَأْن", "ش أ ن", "noun", "standing, importance; a matter", "şan, önem; iş", 1),
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "batn": G("batn", "بَطْن", "ب ط ن", "noun", "a belly, a womb", "karın", 1),
 "muharrar": G("muharrar", "مُحَرَّر", "ح ر ر", "noun", "consecrated, set free for God's service (a passive participle of Form II)", "sırf Allah'a adanmış, âzâd edilmiş (tef'îl ism-i mef'ûlü)", 3),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (m. sg.)", "sen", 1),
 "sami": G("sami", "سَمِيع", "س م ع", "noun", "all-hearing", "her şeyi işiten", 1),
 "alim": G("alim", "عَلِيم", "ع ل م", "noun", "all-knowing", "her şeyi bilen", 1),
 "lamma": G("lamma", "لَمَّا", None, "part", "when — the ẓarf of a past condition", "-ınca, -dığı zaman", 1),
 "wadaa": G("wadaa", "وَضَعَ", "و ض ع", "verb", "to put down; to give birth (an assimilated verb)", "koymak; doğurmak (misâl)", 1),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not", "değildir", 1),
 "samma": G("samma", "سَمَّى", "س م و", "verb", "to name (Form II, defective)", "ad vermek (tef'îl, nâkıs)", 1),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "aadha": G("aadha", "أَعَاذَ", "ع و ذ", "verb", "to commend to protection, to put under (God's) shelter (Form IV, hollow)", "sığındırmak, korumasına vermek (if'âl, ecvef)", 3),
 "dhurriyya": G("dhurriyya", "ذُرِّيَّة", "ذ ر ر", "noun", "offspring, progeny", "soy, zürriyet", 2),
 "shaytan": G("shaytan", "شَيْطَان", "ش ط ن", "noun", "Satan, a devil", "şeytan", 1),
 "rajim": G("rajim", "رَجِيم", "ر ج م", "noun", "accursed, pelted (an intensive passive)", "kovulmuş, taşlanmış", 2),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "wahana", _sg.sound1("daraba", "وَهَن", "هِن", "هِن", "وَهْن", "وَاهِن", None, None, None, "وَهَنَ يَهِنُ: ضَعُفَ — مِثَالٌ وَاوِيٌّ تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ وَالْأَمْرِ.", cls="مِثَالٌ وَاوِيٌّ"))
put_morph(mo, "abtala", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْطَل", "بْطِل", "أَبْطِل", "إِبْطَال", "مُبْطِل", "مُبْطَل", "أُبْطِلَ", "يُبْطَلُ", "أَبْطَلَ الشَّيْءَ: جَعَلَهُ بَاطِلًا لَا أَثَرَ لَهُ."))
put_morph(mo, "bakkara", _sg.derived(_sg.B2, _sg.W2, "ُ", "بَكَّر", "بَكِّر", "بَكِّر", "تَبْكِير", "مُبَكِّر", None, None, None, "بَكَّرَ: جَاءَ مُبَكِّرًا فِي أَوَّلِ الْوَقْتِ."))
put_morph(mo, "rabata", _sg.sound1("daraba", "رَبَط", "رْبِط", "اِرْبِط", "رَبْط", "رَابِط", "مَرْبُوط", "رُبِطَ", "يُرْبَطُ", "رَبَطَ الشَّيْءَ: شَدَّهُ؛ وَرَبَطَ اللهُ عَلَى قَلْبِهِ: ثَبَّتَهُ وَقَوَّاهُ."))
put_morph(mo, "harraka", _sg.derived(_sg.B2, _sg.W2, "ُ", "حَرَّك", "حَرِّك", "حَرِّك", "تَحْرِيك", "مُحَرِّك", "مُحَرَّك", "حُرِّكَ", "يُحَرَّكُ", "حَرَّكَ الشَّيْءَ: جَعَلَهُ يَتَحَرَّكُ."))
put_morph(mo, "attala", _sg.derived(_sg.B2, _sg.W2, "ُ", "عَطَّل", "عَطِّل", "عَطِّل", "تَعْطِيل", "مُعَطِّل", "مُعَطَّل", "عُطِّلَ", "يُعَطَّلُ", "عَطَّلَ الشَّيْءَ: أَبْطَلَ عَمَلَهُ وَتَرَكَهُ بِلَا عَمَلٍ."))
put_morph(mo, "nadhara", _sg.sound1("nasara", "نَذَر", "نْذُر", "اُنْذُر", "نَذْر", "نَاذِر", "مَنْذُور", "نُذِرَ", "يُنْذَرُ", "نَذَرَ الشَّيْءَ لِلّٰهِ: أَوْجَبَهُ عَلَى نَفْسِهِ تَقَرُّبًا إِلَيْهِ؛ وَيُقَالُ أَيْضًا: نَذَرَ يَنْذِرُ."))
put_morph(mo, "idtalaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِضْطَلَع", "ضْطَلِع", "اِضْطَلِع", "اِضْطِلَاع", "مُضْطَلِع", "مُضْطَلَع بِهِ", None, None, "اِضْطَلَعَ بِالْأَمْرِ: قَوِيَ عَلَيْهِ وَنَهَضَ بِهِ — أَصْلُهُ اِضْتَلَعَ، قُلِبَتْ تَاءُ الِافْتِعَالِ طَاءً بَعْدَ الضَّادِ."))
put_morph(mo, "aadha", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَعَاذ", "أَعَذ", "عِيذ", "عِذ", "أَعِيذ", "أَعِذ", "إِعَاذَة", "مُعِيذ", "مُعَاذ", "أُعِيذَ", "يُعَاذُ", "أَعَاذَهُ بِاللهِ: جَعَلَهُ فِي عِيَاذِهِ وَحِفْظِهِ — أَجْوَفُ وَاوِيٌّ مِنْ بَابِ الْإِفْعَالِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch20 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 20 (print pp. 32–34; the story of Zakariyyā opens): the prayer for a righteous son and the signs of God's power (s1–s8); the vow of ʿImrān's wife (s9–s10); «I have delivered a female», with 3:35–36 (s11–s16)."
ADD_TR = " Yirminci bölüm (baskı s. 32–34; Zekeriyyâ kıssası açılır): sâlih bir evlât için duâ ve Allah'ın kudretinin âyetleri (s1–s8); İmrân'ın karısının adağı (s9–s10); «Onu kız doğurdum», 3:35–36 ile (s11–s16)."
write_out(20, S, TITLE, ADD_EN, ADD_TR, "Zakariyyā §1–3", GLOSS_ADD, notes=(), related=())
report(20, S, GLOSS_ADD, ())
