# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 22: «آيَاتُ اللهِ وَقُدْرَتُهُ» — §7 (God's signs and His power, with 21:89–90), §8 (Yaḥyā shoulders the burdens of the call,
with 19:12–15); print pp. 37–38 — the END of the story of Zakariyyā.
python3 tools/authoring/author_qisas4_ch22.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "آيَاتُ اللهِ وَقُدْرَتُهُ: يَحْيَى يَضْطَلِعُ بِأَعْبَاءِ الدَّعْوَةِ", "en": "God's signs and His power: Yaḥyā shoulders the burdens of the call", "tr": "Allah'ın âyetleri ve kudreti: Yahyâ davetin yüklerini üstleniyor"}
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

# ---------------------------------------------------------------- §7 آيَاتُ اللهِ وَقُدْرَتُهُ (print p. 37)
sen("s1", "And God's signs and His power appeared in his body, then in his house and his family; Yaḥyā was born, and by him his eye was cooled, his back was strengthened and his call lived on.",
        "Allah'ın âyetleri ve kudreti önce bedeninde, sonra evinde ve ailesinde göründü; Yahyâ doğdu; onunla gözü aydın oldu, beli kuvvetlendi, daveti onunla yaşadı.", [
  mazi_ta("وَظَهَرَتْ", "zahara", "«and appeared»", "«ve göründü»", wa=True),
  fail("آيَاتُ", "aya", "«the signs [of]»", "«âyetleri»", tags=[ID, JM], extra_ar="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  noun_pron("وَقُدْرَتُهُ", "qudra", "وَقُدْرَتُ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَقُدْرَتُ مَعْطُوفٌ عَلَى الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His power»", "«ve kudreti»", tags=[AT, ID]),
  fi(), noun_pron("جِسْمِهِ", "jism", "جِسْمِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his body»", "«bedeninde»", tags=[HJ, ID]),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  fi(), noun_pron("بَيْتِهِ", "bayt", "بَيْتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his house»", "«evinde»", tags=[HJ, ID]),
  noun_pron("وَأُسْرَتِهِ", "usra-family", "وَأُسْرَتِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَأُسْرَتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his family»", "«ve ailesinde»", tags=[AT, ID], punct="،"),
  tok("وَوُلِدَ", "walada", "verb", [AT, NF, "mithal-verbs"], "الْوَاوُ عَاطِفَةٌ، وَوُلِدَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَاوُ الْمِثَالِ تَثْبُتُ فِي الْمَاضِي.", "«and was born» — the passive māḍī; the assimilated verb's wāw stays in the māḍī.", "«ve doğdu» — meçhul mâzî; misâl fiilin vâvı mâzîde kalır.", segments=wa_("وُلِدَ", "walada", "verb")),
  tok("يَحْيَى", "yahya", "propn", [NF, MM, "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yaḥyā» — the deputy doer; a diptote name on alif.", "«Yahyâ» — nâib-i fâil; elifle biten gayr-i munsarıf."),
  mazi_ta("فَقَرَّتْ", "qarra", "«and was cooled»", "«ve aydın oldu»", tags=[AT, "doubled-verbs"], wa=True),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by him»", "«onunla»"),
  noun_pron("عَيْنُهُ", "ayn", "عَيْنُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — قَرَّتْ عَيْنُهُ: كِنَايَةٌ عَنِ السُّرُورِ.", "«his eye» — the doer; «his eye was cooled» is a kināya for joy.", "«gözü» — fâil; «gözü aydın oldu» sevinçten kinâye.", tags=[FL, ID], punct="،"),
  mazi("وَاشْتَدَّ", "ishtadda", "«and was strengthened»", "«ve kuvvetlendi»", tags=[AT, "form-viii-verbs", "doubled-verbs"], wa=True, hidden=None),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by him»", "«onunla»"),
  noun_pron("أَزْرُهُ", "azr", "أَزْرُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اشْتَدَّ أَزْرُهُ: قَوِيَ ظَهْرُهُ.", "«his back» (lit. his strength)", "«beli, gücü»", tags=[FL, ID], punct="،"),
  mazi_ta("وَعَاشَتْ", "asha-live", "«and lived on»", "«ve yaşadı»", tags=[AT, "hollow-verbs"], wa=True),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by him»", "«onunla»"),
  noun_pron("دَعْوَتُهُ", "dawa", "دَعْوَتُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his call»", "«daveti»", tags=[FL, ID], punct="."),
])
sen("s2", "And hear the Qurʾān telling this story, now in brevity and now in detail; it says:",
        "Kur'ân'ı dinleyin; bu kıssayı bazen kısaca, bazen ayrıntıyla anlatır; şöyle der:", [
  tok("وَاسْمَعُوا", "samia", "verb", [AT, AM, MB], "الْوَاوُ لِلِاسْتِئْنَافِ، وَاسْمَعُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and hear» — an imperative built on dropping the nūn; the wāw is the doer.", "«ve dinleyin» — nûnun düşmesi üzere mebnî emir; vâv fâil.", segments=wa_("اسْمَعُوا", "samia", "verb")),
  maful_("الْقُرْآنَ", "quran", "«the Qurʾān»", "«Kur'ân'ı»"),
  mudari("يَحْكِي", "haka", "«telling»", "«anlatır»", tags=[HL, MB, "naqis-verbs"], hidden="هُوَ", extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْجُمْلَةُ حَالٌ"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«this»", "«bu»"),
  tok("الْقِصَّةَ", "qissa", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«story» — a badal.", "«kıssayı» — bedel."),
  tok("تَارَةً", "tara-time", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: مَرَّةً.", "«now» (lit. one time) — a time adverb.", "«bazen» — zaman zarfı."),
  fi(), majrur("إِيجَازٍ", "ijaz", "«brevity»", "«kısaca»"),
  tok("وَطَوْرًا", "tawr", "noun", [AT, MF], "الْوَاوُ عَاطِفَةٌ، وَطَوْرًا ظَرْفُ زَمَانٍ مَنْصُوبٌ — أَيْ: وَمَرَّةً أُخْرَى.", "«and now» (lit. another time)", "«ve bazen»", segments=wa_("طَوْرًا", "tawr", "noun")),
  fi(), majrur("تَفْصِيلٍ", "tafsil", "«detail»", "«ayrıntıyla»", punct="،"),
  mudari("فَيَقُولُ", "qala", "«it says»", "«şöyle der»", tags=[AT, "hollow-verbs", MB], hidden="هُوَ", punct=":"),
])
sen("s3", "«And Zakariyyā, when he called to his Lord: My Lord, do not leave me alone, and You are the best of inheritors» (21:89).",
        "«Zekeriyyâ'yı da [an]: hani Rabbine: Rabbim, beni tek başıma bırakma; Sen vârislerin en hayırlısısın, diye seslenmişti» (21:89).", [
  *quran([
  tok("وَزَكَرِيَّا", "zakariyya", "propn", [AT, MB, MM, "hadhf-wa-taqdir", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَزَكَرِيَّا مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ، مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«and [remember] Zakariyyā» — the object of an unspoken «remember».", "«Zekeriyyâ'yı da [an]» — mahzuf «an»ın mef'ûlü.", segments=wa_("زَكَرِيَّا", "zakariyya", "propn")),
  tok("إِذْ", "idh", "noun", [MF, BD], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ، بَدَلُ اشْتِمَالٍ.", "«when» — a badal of inclusion.", "«hani»"),
  mazi("نَادَى", "nada", "«he called»", "«seslendi»", tags=["naqis-verbs", "form-iii-verbs", MB, ID], hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  noun_pron("رَبَّهُ", "rabb", "رَبَّ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his Lord»", "«Rabbine»", tags=[MB, ID]),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ.", "«my Lord»", "«Rabbim»"),
  tok("لَا", "la-nahiya", "part", ["la-nahiya"], "لَا نَاهِيَةٌ جَازِمَةٌ — وَالنَّهْيُ مِنَ الْعَبْدِ لِرَبِّهِ دُعَاءٌ.", "«do not» — the prohibiting lā; from a servant to his Lord it is a plea.", "«-ma» — nehiy lâ'sı; kuldan Rabbe duâdır."),
  tok("تَذَرْنِي", "wadhara", "verb", ["la-nahiya", LJ, MB, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَذَرَ: مِثَالٌ لَا يُسْتَعْمَلُ مَاضِيهِ.", "«leave me» — jazm by lā; the protecting nūn; wadhara is an assimilated verb whose māḍī is not used.", "«beni bırakma» — lâ ile meczûm; vikâye nûnu; vezera'nın mâzîsi kullanılmaz.", segments=[seg("تَذَرْ", "wadhara", "verb"), seg("نِي", "pron-1s", "pron")]),
  hal("فَرْدًا", "fard-single", "«alone»", "«tek başıma»"),
  tok("وَأَنْتَ", "anta", "pron", [AT, MK], "الْوَاوُ لِلْحَالِ، وَأَنْتَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and You» — the mubtadaʾ.", "«ve Sen» — mübtedâ.", segments=wa_("أَنْتَ", "anta", "pron")),
  tok("خَيْرُ", "khayr", "noun", [MK, ID, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — خَيْرٌ هُنَا بِمَعْنَى أَخْيَرُ (اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ).", "«the best [of]» — the khabar; khayr as an elative (its hamza dropped).", "«en hayırlısı» — haber; hemzesi düşmüş ism-i tafdîl."),
  tok("الْوَارِثِينَ", "warith", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«inheritors» — jarr by the yāʾ.", "«vârislerin» — yâ ile mecrûr.", punct="۝"),
  ]),
])
sen("s4", "«So We answered him and granted him Yaḥyā, and made his wife fit for him; they used to hasten to good works and call upon Us in longing and in awe, and they were humble before Us» (21:90).",
        "«Biz de ona icabet ettik; ona Yahyâ'yı bağışladık ve eşini onun için ıslah ettik; onlar hayırlarda yarışır, umarak ve korkarak Bize duâ ederlerdi; Bize karşı derin saygı içindeydiler» (21:90).", [
  *quran([
  tok("فَاسْتَجَبْنَا", "istajaba", "verb", [AT, "hollow-verbs", "form-x-verbs"], "الْفَاءُ عَاطِفَةٌ، وَاسْتَجَبْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«so We answered»", "«Biz de icabet ettik»", segments=[seg("فَ", "fa", "conj"), seg("اسْتَجَبْ", "istajaba", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«him»", "«ona»"),
  tok("وَوَهَبْنَا", "wahaba", "verb", [AT, MB, "mithal-verbs"], "الْوَاوُ عَاطِفَةٌ، وَوَهَبْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«and We granted»", "«ve bağışladık»", segments=[seg("وَ", "wa", "conj"), seg("وَهَبْ", "wahaba", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«him»", "«ona»"),
  tok("يَحْيَى", "yahya", "propn", [MB, MM, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Yaḥyā» — the object.", "«Yahyâ'yı» — mef'ûl."),
  tok("وَأَصْلَحْنَا", "aslaha", "verb", [AT, MB, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَصْلَحْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«and We made fit»", "«ve ıslah ettik»", segments=[seg("وَ", "wa", "conj"), seg("أَصْلَحْ", "aslaha", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  noun_pron("زَوْجَهُ", "zawj", "زَوْجَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wife»", "«eşini»", tags=[MB, ID]),
  tok("إِنَّهُمْ", "inna", "part", [IW], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهُمْ اسْمُهَا — وَالْجُمْلَةُ تَعْلِيلِيَّةٌ.", "«indeed they» — inna's clause gives the reason.", "«şüphesiz onlar» — ta'lil cümlesi.", segments=[seg("إِنَّ", "inna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  mazi_pl("كَانُوا", "kana", "«they used to»", "«-erlerdi»", tags=[IW, KN, "hollow-verbs"]),
  khamsa("يُسَارِعُونَ", "saraa", "«hasten»", "«yarışırlar»", tags=[KN, "form-iii-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  fi(), majrur("الْخَيْرَاتِ", "khayr", "«good works»", "«hayırlarda»", tags=[JM]),
  tok("وَيَدْعُونَنَا", "daa", "verb", [AT, AK, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَدْعُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَنَا مَفْعُولٌ بِهِ.", "«and call upon Us» — one of the five verbs; nā is the object.", "«ve Bize duâ ederler» — ef'âl-i hamseden; nâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يَدْعُونَ", "daa", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("رَغَبًا", "raghab", "noun", ["maful-lah", HL], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ (أَوْ حَالٌ: رَاغِبِينَ).", "«in longing» — an object of purpose (or a ḥāl).", "«umarak» — mef'ûlün leh (veya hâl)."),
  tok("وَرَهَبًا", "rahab", "noun", [AT, "maful-lah"], "الْوَاوُ عَاطِفَةٌ، وَرَهَبًا مَعْطُوفٌ مَنْصُوبٌ.", "«and in awe»", "«ve korkarak»", segments=wa_("رَهَبًا", "rahab", "noun")),
  mazi_pl("وَكَانُوا", "kana", "«and they were»", "«ve … idiler»", wa=True, tags=[AT, KN, "hollow-verbs"]),
  tok("لَنَا", "li", "prep", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِخَاشِعِينَ.", "«before Us»", "«Bize karşı»", segments=[seg("لَ", "li", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("خَاشِعِينَ", "khashi", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«humble» — kāna's khabar; naṣb by the yāʾ.", "«huşû içinde» — kâne'nin haberi; yâ ile mansub.", punct="."),
  ]),
])
# ---------------------------------------------------------------- §8 يَحْيَى يَضْطَلِعُ بِأَعْبَاءِ الدَّعْوَةِ (print pp. 37–38)
sen("s5", "And Yaḥyā is born, and becomes the delight of his parents' eyes and a successor to his great father, and shoulders the burdens of the call to God and to the pure religion;",
        "Yahyâ doğar; ana babasının göz aydınlığı ve ulu babasının halefi olur; Allah'a ve hâlis dine davetin yüklerini üstlenir;", [
  tok("وَيُولَدُ", "walada", "verb", [NF, "mudari-marfu", "mithal-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيُولَدُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — تَعُودُ وَاوُ الْمِثَالِ فِي الْمَجْهُولِ.", "«and is born» — a passive muḍāriʿ; the historical present; the wāw returns in the passive.", "«ve doğar» — meçhul muzari (hikâye-i hâl); vâv meçhulde geri gelir.", segments=wa_("يُولَدُ", "walada", "verb")),
  tok("يَحْيَى", "yahya", "propn", [NF, MM, "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Yaḥyā»", "«Yahyâ»"),
  tok("فَيَكُونُ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and becomes»", "«ve olur»", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  tok("قُرَّةَ", "qurra", "noun", [KN, ID], "خَبَرُ يَكُونُ مَنْصُوبٌ، مُضَافٌ — قُرَّةُ عَيْنٍ: كِنَايَةٌ عَنِ الْفَرَحِ.", "«the delight [of]» — the khabar; «the eye's coolness» is a kināya for joy.", "«aydınlığı» — haber; «göz aydınlığı» sevinçten kinâye."),
  mudaf_ilayh("عَيْنٍ", "ayn", "«an eye»", "«göz»"),
  tok("لِأَبَوَيْهِ", "abawan", "noun", [HJ, "al-muthanna", ID], "اللَّامُ حَرْفُ جَرٍّ، وَأَبَوَيْ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَبَوَانِ: الْأَبُ وَالْأُمُّ تَغْلِيبًا.", "«of his parents» — a dual on the yāʾ, its nūn dropped by annexation; abawān = father and mother by taghlīb.", "«ana babasının» — tesniye; nûnu izâfetle düşmüş; ebevân: tağlîb ile ana baba.", segments=[seg("لِ", "li", "prep"), seg("أَبَوَيْ", "abawan", "noun"), pr3ms()], punct="،"),
  atf("وَخَلِيفَةً", "khalifa", "«a successor»", "«ve halefi»", "nasb"),
  noun_pron("لِوَالِدِهِ", "walid-father", "لِوَالِدِ", "هِ", "pron-3ms", "اللَّامُ حَرْفُ جَرٍّ، وَوَالِدِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his father»", "«babasının»", tags=[HJ, ID]),
  naat("الْعَظِيمِ", "azim", "«great»", "«ulu»", punct="،"),
  mudari("فَيَضْطَلِعُ", "idtalaa", "«and shoulders»", "«ve üstlenir»", tags=[AT, "form-viii-verbs"], hidden="هُوَ"),
  tok("بِأَعْبَاءِ", "ib", "noun", [HJ, ID, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَأَعْبَاءِ مَجْرُورٌ، مُضَافٌ.", "«the burdens [of]»", "«yüklerini»", segments=[seg("بِ", "bi", "prep"), seg("أَعْبَاءِ", "ib", "noun")]),
  mudaf_ilayh("الدَّعْوَةِ", "dawa", "«the call»", "«davetin»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى.", "«God»", "«Allah'a»"),
  tok("وَإِلَى", "ila", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَإِلَى حَرْفُ جَرٍّ.", "«and to»", "«ve … -e»", segments=wa_("إِلَى", "ila", "prep")),
  majrur("الدِّينِ", "din", "«the religion»", "«dine»"),
  naat("الْخَالِصِ", "khalis", "«pure»", "«hâlis»", tags=["ism-fail"], punct="،"),
])
sen("s6", "and the marks of nobility show in him from childhood: he takes to learning with passion while still a boy, adorns himself with righteousness and piety while a youth, and stands out among his peers in love, tenderness and dutifulness to his parents, so that fingers point to him for it. God Most High says, addressing him:",
        "daha çocukluktan onda asâlet izleri görünür: henüz bir çocukken ilme tutkuyla yönelir, genç bir delikanlıyken salâh ve takvâ ile süslenir; sevgide, şefkatte ve ana babaya iyilikte akranlarından ayrılır; bu yüzden parmakla gösterilir. Allah Teâlâ ona hitap ederek şöyle buyurur:", [
  mudari("وَتَظْهَرُ", "zahara", "«and show»", "«ve görünür»", tags=[AT], hidden=None),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in him»", "«onda»"),
  fail("آثَارُ", "athar", "«the marks [of]»", "«izleri»", tags=[ID, JT], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("النَّجَابَةِ", "najaba", "«nobility»", "«asâletin»"),
  tok("مُنْذُ", "mundhu", "part", [HJ], "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ فِي الزَّمَانِ.", "«from» (since)", "«-den beri»"),
  majrur("الصِّغَرِ", "sighar", "«childhood»", "«çocukluk»", punct="،"),
  mudari("فَيُقْبِلُ", "aqbala", "«he takes»", "«yönelir»", tags=[AT, "form-iv-verbs"], hidden="هُوَ"),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  majrur("الْعِلْمِ", "ilm", "«learning»", "«ilme»"),
  tok("بِشَغَفٍ", "shaghaf", "noun", [HJ, HL], "الْبَاءُ حَرْفُ جَرٍّ، وَشَغَفٍ مَجْرُورٌ — حَالٌ فِي الْمَعْنَى.", "«with passion»", "«tutkuyla»", segments=[seg("بِ", "bi", "prep"), seg("شَغَفٍ", "shaghaf", "noun")]),
  tok("وَهُوَ", "huwa", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — وَالْجُمْلَةُ حَالٌ.", "«while he» — the wāw of state; a ḥāl clause.", "«o … iken» — hâl vâvı; hâl cümlesi.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("غُلَامٌ", "ghulam", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a boy» — the khabar.", "«bir çocuk» — haber.", punct="،"),
  mudari("وَيَتَحَلَّى", "tahalla", "«and adorns himself»", "«ve süslenir»", tags=[AT, "naqis-verbs", "form-v-verbs"], hidden="هُوَ", extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ"),
  tok("بِالصَّلَاحِ", "salah", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالصَّلَاحِ مَجْرُورٌ.", "«with righteousness»", "«salâh ile»", segments=[seg("بِ", "bi", "prep"), seg("الصَّلَاحِ", "salah", "noun")]),
  tok("وَالتَّقْوَى", "taqwa", "noun", [AT, "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالتَّقْوَى مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«and piety»", "«ve takvâ»", segments=wa_("التَّقْوَى", "taqwa", "noun")),
  tok("وَهُوَ", "huwa", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ.", "«while he»", "«o … iken»", segments=wa_("هُوَ", "huwa", "pron")),
  tok("شَابٌّ", "shabb", "noun", [MK, "doubled-verbs"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a youth» — the khabar.", "«bir genç» — haber.", punct="،"),
  mudari("وَيَمْتَازُ", "imtaza", "«and stands out»", "«ve ayrılır»", tags=[AT, "hollow-verbs", "form-viii-verbs"], hidden="هُوَ"),
  prep("عَنْ", "an", "«among» (lit. from)", "«-den»"),
  noun_pron("أَقْرَانِهِ", "qirn", "أَقْرَانِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his peers»", "«akranlarından»", tags=[HJ, ID, JT]),
  fi(), majrur("الْحُبِّ", "hubb", "«love»", "«sevgide»"),
  atf("وَالْحَنَانِ", "hanan", "«tenderness»", "«şefkatte»", "jarr"),
  atf("وَالْبِرِّ", "birr", "«dutifulness»", "«iyilikte»", "jarr"),
  tok("بِالْأَبَوَيْنِ", "abawan", "noun", [HJ, "al-muthanna"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْأَبَوَيْنِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«to the parents» — a dual on the yāʾ.", "«ana babaya» — tesniye.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْأَبَوَيْنِ", "abawan", "noun")]),
  tok("يُشَارُ", "ashara-point", "verb", [NF, "mudari-marfu", "hollow-verbs", "form-iv-verbs", HL], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ (إِلَيْهِ) — وَالْجُمْلَةُ حَالٌ.", "«fingers are pointed» — a passive; the jarr phrase is its deputy doer.", "«işaret edilir» — meçhul; câr-mecrûr nâib-i fâil."),
  fi(), ishara("ذٰلِكَ", "dhalika", "jarr", "«for that»", "«bu hususta»"),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him» — the deputy doer.", "«ona» — nâib-i fâil.", tags=[NF]),
  tok("بِالْبَنَانِ", "banan", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْبَنَانِ مَجْرُورٌ — يُشَارُ إِلَيْهِ بِالْبَنَانِ: كِنَايَةٌ عَنِ الشُّهْرَةِ.", "«with fingertips» — «pointed at with fingers» is a kināya for fame.", "«parmakla» — «parmakla gösterilir» şöhretten kinâye.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْبَنَانِ", "banan", "noun")]),
  mudari("يَقُولُ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs", MB], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»"),
  hal("مُخَاطِبًا", "khataba", "«addressing»", "«hitap ederek»", tags=["ism-fail", "form-iii-verbs"]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«him»", "«ona»", punct=":"),
])
sen("s7", "«O Yaḥyā, take the Book with strength! — and We gave him judgement as a child, and tenderness from Us, and purity; and he was God-fearing, and dutiful to his parents, and he was not a tyrant, disobedient; and peace be upon him the day he was born, the day he dies, and the day he is raised alive» (19:12–15).",
        "«Ey Yahyâ, Kitab'a kuvvetle sarıl! — ona daha çocukken hikmet verdik; katımızdan bir şefkat ve temizlik verdik; o takvâlı idi, ana babasına iyilik ederdi; zorba ve âsi değildi; doğduğu gün, öleceği gün ve diri olarak kaldırılacağı gün ona selâm olsun» (19:12–15).", [
  *quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("يَحْيَى", "yahya", "propn", ["vocative-munada", MM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ.", "«Yaḥyā» — a single-name vocative, built on an estimated ḍamma.", "«Yahyâ» — münâdâ; takdirî damme üzere mebnî."),
  tok("خُذِ", "akhadha", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — أَخَذَ: مَهْمُوزُ الْفَاءِ، حُذِفَتْ هَمْزَتُهُ فِي الْأَمْرِ (خُذْ).", "«take» — an imperative; akhadha drops its hamza in the imperative (khudh); the kasra breaks the two sukūns.", "«al» — emir; ehaze'nin hemzesi emirde düşer (huz); kesre iki sâkin yüzünden."),
  maful_("الْكِتَابَ", "kitab", "«the Book»", "«Kitab'ı»"),
  tok("بِقُوَّةٍ", "quwwa", "noun", [HJ, HL], "الْبَاءُ حَرْفُ جَرٍّ، وَقُوَّةٍ مَجْرُورٌ — حَالٌ فِي الْمَعْنَى: مُجْتَهِدًا.", "«with strength» — a ḥāl in sense.", "«kuvvetle» — mânen hâl."),
  tok("وَآتَيْنَاهُ", "aataa", "verb", [AT, MX, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ (أَوْ لِلِاسْتِئْنَافِ)، وَآتَيْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and We gave him» — nā the doer; the hāʾ the first object.", "«ve ona verdik» — nâ fâil; hâ birinci mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("آتَيْ", "aataa", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  tok("الْحُكْمَ", "hukm", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«judgement» — the second object.", "«hikmeti» — ikinci mef'ûl."),
  hal("صَبِيًّا", "sabi-boy", "«as a child»", "«çocukken»", punct="۝"),
  tok("وَحَنَانًا", "hanan", "noun", [AT, MB], "الْوَاوُ عَاطِفَةٌ، وَحَنَانًا مَعْطُوفٌ عَلَى الْحُكْمَ مَنْصُوبٌ.", "«and tenderness» — joined to «judgement».", "«ve bir şefkat» — «hikmet»e atıf.", segments=wa_("حَنَانًا", "hanan", "noun")),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("لَدُنَّا", "ladun", "لَدُنْ", "نَا", "pron-1p", "ظَرْفٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — أُدْغِمَتِ النُّونُ فِي النُّونِ.", "«Us» (lit. from before Us) — the two nūns assimilate.", "«katımızdan» — iki nûn idğam edilir.", tags=[HJ, ID, MF]),
  tok("وَزَكَاةً", "zakat", "noun", [AT, MB], "الْوَاوُ عَاطِفَةٌ، وَزَكَاةً مَعْطُوفٌ مَنْصُوبٌ — أَيْ: طَهَارَةً.", "«and purity»", "«ve temizlik»", segments=wa_("زَكَاةً", "zakat", "noun")),
  tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and he was»", "«ve o … idi»", segments=wa_("كَانَ", "kana", "verb")),
  tok("تَقِيًّا", "taqi", "noun", [KN, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«God-fearing» — kāna's khabar.", "«takvâlı» — kâne'nin haberi.", punct="۝"),
  tok("وَبَرًّا", "barr", "noun", [AT, KN], "الْوَاوُ عَاطِفَةٌ، وَبَرًّا مَعْطُوفٌ عَلَى تَقِيًّا مَنْصُوبٌ.", "«and dutiful»", "«ve iyilik eder»", segments=wa_("بَرًّا", "barr", "noun")),
  tok("بِوَالِدَيْهِ", "walid-father", "noun", [HJ, "al-muthanna", ID], "الْبَاءُ حَرْفُ جَرٍّ، وَوَالِدَيْ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his parents» — a dual, its nūn dropped by annexation.", "«ana babasına» — tesniye; nûnu izâfetle düşmüş.", segments=[seg("بِ", "bi", "prep"), seg("وَالِدَيْ", "walid-father", "noun"), pr3ms()]),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … değildi»", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("يَكُنْ", "kana", "verb", [LJ, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«he was» — jazm; the wāw dropped before the sukūn.", "«idi» — meczûm; vâvı düştü."),
  tok("جَبَّارًا", "jabbar", "noun", [KN, "sighat-mubalagha"], "خَبَرُ يَكُنْ مَنْصُوبٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَعَّالٍ.", "«a tyrant» — the khabar; an intensive on faʿʿāl.", "«zorba» — haber; fa''âl mübalağa sigası."),
  naat("عَصِيًّا", "asi", "«disobedient»", "«âsi»", case="nasb", tags=["sighat-mubalagha"], punct="۝"),
  tok("وَسَلَامٌ", "salam", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَسَلَامٌ مُبْتَدَأٌ مَرْفُوعٌ — سَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ مَعْنَى الدُّعَاءِ.", "«and peace» — the mubtadaʾ; an indefinite allowed by the sense of prayer.", "«ve selâm» — mübtedâ; duâ mânâsı nekreyi câiz kılar.", segments=wa_("سَلَامٌ", "salam", "noun")),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon him» — the khabar.", "«ona» — haber.", tags=[MK], extra_ar=" — خَبَرٌ"),
  tok("يَوْمَ", "yawm", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«the day»", "«… gün»"),
  tok("وُلِدَ", "walada", "verb", [NF, ID, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ يَوْمَ.", "«he was born» — a passive; the clause is annexed to «the day».", "«doğduğu» — meçhul; cümle «gün»e muzâfun ileyh."),
  tok("وَيَوْمَ", "yawm", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَيَوْمَ ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and the day»", "«ve … gün»", segments=wa_("يَوْمَ", "yawm", "noun")),
  mudari("يَمُوتُ", "mata-die", "«he dies»", "«öleceği»", tags=[ID, "hollow-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ"),
  tok("وَيَوْمَ", "yawm", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَيَوْمَ ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and the day»", "«ve … gün»", segments=wa_("يَوْمَ", "yawm", "noun")),
  tok("يُبْعَثُ", "baatha", "verb", [NF, ID, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«he is raised» — a passive muḍāriʿ.", "«kaldırılacağı» — meçhul muzari."),
  hal("حَيًّا", "hayy", "«alive»", "«diri olarak»", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: asha-live, tara-time, fard-single, ashara-point, sabi-boy, mata-die take suffixed keys; wulida = walada's majhul)
CAND = {
 "zahara": G("zahara", "ظَهَرَ", "ظ ه ر", "verb", "to appear", "görünmek, ortaya çıkmak", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, alâmet", 1, plural="آيَات"),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "jism": G("jism", "جِسْم", "ج س م", "noun", "a body", "beden, vücut", 1),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "a house", "ev", 1),
 "usra-family": G("usra-family", "أُسْرَة", "أ س ر", "noun", "a family", "aile", 1),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to give birth; (passive) to be born (an assimilated verb)", "doğurmak; (meçhul) doğmak (misâl fiil)", 1),
 "yahya": G("yahya", "يَحْيَى", None, "propn", "Yaḥyā (John)", "Yahyâ", 1),
 "qarra": G("qarra", "قَرَّ", "ق ر ر", "verb", "to settle; (the eye) to be cooled, delighted (doubled)", "karar bulmak; (göz) aydın olmak (muzâaf)", 2),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "ayn": G("ayn", "عَيْن", "ع ي ن", "noun", "an eye; a spring", "göz; pınar", 1),
 "ishtadda": G("ishtadda", "اِشْتَدَّ", "ش د د", "verb", "to grow strong, intense (Form VIII, doubled)", "şiddetlenmek, kuvvetlenmek (iftiâl, muzâaf)", 2),
 "azr": G("azr", "أَزْر", "أ ز ر", "noun", "the back; strength", "sırt; güç, destek", 3),
 "asha-live": G("asha-live", "عَاشَ", "ع ي ش", "verb", "to live (hollow)", "yaşamak (ecvef)", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "the call, the mission", "davet", 1),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear", "işitmek, dinlemek", 1),
 "quran": G("quran", "قُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell, to relate (defective)", "anlatmak, hikâye etmek (nâkıs)", 2),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "tara-time": G("tara-time", "تَارَة", "ت و ر", "noun", "a time, once; (tāratan … ṭawran) now … now", "bir kez; (târeten … tavran) bazen … bazen", 3),
 "ijaz": G("ijaz", "إِيجَاز", "و ج ز", "noun", "brevity, concision", "îcâz, kısalık", 2),
 "tawr": G("tawr", "طَوْر", "ط و ر", "noun", "a time; a phase", "bir kez; evre", 3),
 "tafsil": G("tafsil", "تَفْصِيل", "ف ص ل", "noun", "detail", "tafsil, ayrıntı", 2),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "zakariyya": G("zakariyya", "زَكَرِيَّا", None, "propn", "Zakariyyā (Zechariah)", "Zekeriyyâ", 1),
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "nada": G("nada", "نَادَى", "ن د و", "verb", "to call out (Form III, defective)", "seslenmek (mufâale, nâkıs)", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "do not — the prohibiting lā", "-ma — nehiy lâ'sı", 1),
 "wadhara": G("wadhara", "وَذَرَ", "و ذ ر", "verb", "to leave, to let be (an assimilated verb whose māḍī is unused)", "bırakmak (mâzîsi kullanılmayan misâl fiil)", 2),
 "fard-single": G("fard-single", "فَرْد", "ف ر د", "noun", "alone, single", "tek, yalnız", 1),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (m. sg.)", "sen", 1),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good; better, best; (pl.) good works", "hayır; daha hayırlı; (ç.) hayırlar", 1, plural="خَيْرَات"),
 "warith": G("warith", "وَارِث", "و ر ث", "noun", "an inheritor (an active participle)", "vâris (ism-i fâil)", 2),
 "istajaba": G("istajaba", "اِسْتَجَابَ", "ج و ب", "verb", "to answer, to respond (Form X, hollow)", "icabet etmek, cevap vermek (istif'âl, ecvef)", 2),
 "wahaba": G("wahaba", "وَهَبَ", "و ه ب", "verb", "to give, to grant (an assimilated verb)", "bağışlamak, vermek (misâl)", 1),
 "aslaha": G("aslaha", "أَصْلَحَ", "ص ل ح", "verb", "to set right, to make fit (Form IV)", "ıslah etmek, düzeltmek (if'âl)", 1),
 "zawj": G("zawj", "زَوْج", "ز و ج", "noun", "a spouse (husband or wife)", "eş (koca veya karı)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "saraa": G("saraa", "سَارَعَ", "س ر ع", "verb", "to hasten (Form III)", "koşuşmak, yarışmak (mufâale)", 2),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call; to pray (defective)", "çağırmak; duâ etmek (nâkıs)", 1),
 "raghab": G("raghab", "رَغَب", "ر غ ب", "noun", "longing, desire", "umma, arzu", 3),
 "rahab": G("rahab", "رَهَب", "ر ه ب", "noun", "awe, fear", "korku, çekinme", 3),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "khashi": G("khashi", "خَاشِع", "خ ش ع", "noun", "humble, reverent (an active participle)", "huşû içinde olan (ism-i fâil)", 2),
 "qurra": G("qurra", "قُرَّة", "ق ر ر", "noun", "coolness; (qurrat ʿayn) delight of the eye", "serinlik; (kurretü ayn) göz aydınlığı", 2),
 "abawan": G("abawan", "أَبَوَانِ", "أ ب و", "noun", "the parents (the dual of ab, by taghlīb)", "ana baba (eb'in tesniyesi, tağlîb ile)", 2),
 "khalifa": G("khalifa", "خَلِيفَة", "خ ل ف", "noun", "a successor", "halef, halife", 1),
 "walid-father": G("walid-father", "وَالِد", "و ل د", "noun", "a father; (dual) the parents", "baba; (tesniye) ana baba", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great", "ulu, büyük", 1),
 "idtalaa": G("idtalaa", "اِضْطَلَعَ", "ض ل ع", "verb", "to shoulder, to take on (Form VIII, with the tāʾ turned into ṭāʾ)", "yüklenmek, üstlenmek (iftiâl; tâ'sı tâ'ya dönmüş)", 3),
 "ib": G("ib", "عِبْء", "ع ب أ", "noun", "a burden", "yük", 3, plural="أَعْبَاء"),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "khalis": G("khalis", "خَالِص", "خ ل ص", "noun", "pure (an active participle)", "hâlis, saf (ism-i fâil)", 1),
 "athar": G("athar", "أَثَر", "أ ث ر", "noun", "a trace, a mark", "iz, eser", 1, plural="آثَار"),
 "najaba": G("najaba", "نَجَابَة", "ن ج ب", "noun", "nobility, excellence", "asâlet, necâbet", 3),
 "mundhu": G("mundhu", "مُنْذُ", None, "part", "since, from (the time of)", "-den beri", 1),
 "sighar": G("sighar", "صِغَر", "ص غ ر", "noun", "childhood, smallness", "çocukluk, küçüklük", 2),
 "aqbala": G("aqbala", "أَقْبَلَ", "ق ب ل", "verb", "to come forward; (ʿalā) to take to (Form IV)", "yönelmek, ilerlemek (if'âl)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "shaghaf": G("shaghaf", "شَغَف", "ش غ ف", "noun", "passion, ardour", "tutku, şevk", 3),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "ghulam": G("ghulam", "غُلَام", "غ ل م", "noun", "a boy, a lad", "çocuk, oğlan", 1),
 "tahalla": G("tahalla", "تَحَلَّى", "ح ل ي", "verb", "to adorn oneself (Form V, defective)", "süslenmek, bezenmek (tefa''ul, nâkıs)", 2),
 "salah": G("salah", "صَلَاح", "ص ل ح", "noun", "righteousness", "salâh", 1),
 "taqwa": G("taqwa", "تَقْوَى", "و ق ي", "noun", "piety (a maqṣūr noun)", "takvâ (maksûr)", 1),
 "shabb": G("shabb", "شَابّ", "ش ب ب", "noun", "a youth, a young man", "genç, delikanlı", 1),
 "imtaza": G("imtaza", "اِمْتَازَ", "م ي ز", "verb", "to stand out, to be distinguished (Form VIII, hollow)", "ayrılmak, seçkin olmak (iftiâl, ecvef)", 2),
 "an": G("an", "عَنْ", None, "prep", "from, away from", "-den", 1),
 "qirn": G("qirn", "قِرْن", "ق ر ن", "noun", "a peer, an equal", "akran, denk", 3, plural="أَقْرَان"),
 "hubb": G("hubb", "حُبّ", "ح ب ب", "noun", "love", "sevgi", 1),
 "hanan": G("hanan", "حَنَان", "ح ن ن", "noun", "tenderness", "şefkat", 2),
 "birr": G("birr", "بِرّ", "ب ر ر", "noun", "dutifulness, kindness", "iyilik, birr", 1),
 "ashara-point": G("ashara-point", "أَشَارَ", "ش و ر", "verb", "to point (Form IV, hollow)", "işaret etmek (if'âl, ecvef)", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "banan": G("banan", "بَنَان", "ب ن ن", "noun", "fingertips", "parmak uçları", 3),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "khataba": G("khataba", "خَاطَبَ", "خ ط ب", "verb", "to address (Form III)", "hitap etmek (mufâale)", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take (hamzated; the imperative khudh)", "almak (mehmûz; emri huz)", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a book; the Book", "kitap", 1),
 "quwwa": G("quwwa", "قُوَّة", "ق و ي", "noun", "strength", "kuvvet", 1),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give (Form IV, defective, hamzated)", "vermek (if'âl, nâkıs, mehmûz)", 1),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "judgement, wisdom; a ruling", "hüküm, hikmet", 1),
 "sabi-boy": G("sabi-boy", "صَبِيّ", "ص ب و", "noun", "a child, a boy", "çocuk, sabî", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "ladun": G("ladun", "لَدُنْ", None, "noun", "at, from before (a mabnī adverb)", "katında, nezdinde (mebnî zarf)", 3),
 "zakat": G("zakat", "زَكَاة", "ز ك و", "noun", "purity; alms", "temizlik; zekât", 1),
 "taqi": G("taqi", "تَقِيّ", "و ق ي", "noun", "God-fearing, pious", "takvâlı, müttaki", 2),
 "barr": G("barr", "بَرّ", "ب ر ر", "noun", "dutiful, pious", "iyi, itaatkâr", 2),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "not (of the past) — the jazm lam", "-madı — cezm eden lem", 1),
 "jabbar": G("jabbar", "جَبَّار", "ج ب ر", "noun", "a tyrant (an intensive)", "zorba, cebbâr (mübalağa)", 2),
 "asi": G("asi", "عَصِيّ", "ع ص ي", "noun", "disobedient (an intensive)", "âsi (mübalağa)", 2),
 "salam": G("salam", "سَلَام", "س ل م", "noun", "peace; safety", "selâm; selâmet", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die (hollow)", "ölmek (ecvef)", 1),
 "baatha": G("baatha", "بَعَثَ", "ب ع ث", "verb", "to send; to raise (from the dead)", "göndermek; diriltmek", 1),
 "hayy": G("hayy", "حَيّ", "ح ي ي", "noun", "living, alive", "diri, canlı", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them / their", "onları / onların", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "wadhara", _sg.sound1("fataha", "وَذَر", "ذَر", "ذَر", "وَذْر", "وَاذِر", "مَوْذُور", None, None, "ذَرْهُ، لَا تَذَرْنِي: اتْرُكْهُ — مِثَالٌ وَاوِيٌّ أُمِيتَ مَاضِيهِ (وَذَرَ) فَلَا يُقَالُ فِي الْفَصِيحِ، وَيُسْتَعْمَلُ مُضَارِعُهُ يَذَرُ وَأَمْرُهُ ذَرْ بِحَذْفِ الْوَاوِ؛ وَمِثْلُهُ وَدَعَ يَدَعُ — الْجَدْوَلُ يُثْبِتُ الْمَاضِيَ الْقِيَاسِيَّ لِلْبَيَانِ.", cls="مِثَالٌ وَاوِيٌّ"))
put_morph(mo, "asha-live", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "عَاش", "عِش", "عِيش", "عِش", "عِيش", "عِش", "عَيْش / مَعَاش", "عَائِش", None, None, None, "عَاشَ يَعِيشُ: حَيِيَ — أَجْوَفُ يَائِيٌّ؛ لَمْ يَعِشْ."))
put_morph(mo, "saraa", _sg.derived(_sg.B3, _sg.W3, "ُ", "سَارَع", "سَارِع", "سَارِع", "مُسَارَعَة", "مُسَارِع", None, None, None, "سَارَعَ إِلَى الشَّيْءِ: بَادَرَ إِلَيْهِ مُسْرِعًا."))
put_morph(mo, "tahalla", _sg.derived_naqis("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَحَلَّ", "تَحَلّ", "a", "تَحَلّ", "تَحَلٍّ (التَّحَلِّي)", "مُتَحَلٍّ (الْمُتَحَلِّي)", None, None, None, "تَحَلَّى بِالشَّيْءِ: تَزَيَّنَ بِهِ."))
put_morph(mo, "imtaza", _sg.derived_hollow(_sg.B8, _sg.W8, "َ", "اِمْتَاز", "اِمْتَز", "مْتَاز", "مْتَز", "اِمْتَاز", "اِمْتَز", "اِمْتِيَاز", "مُمْتَاز", None, None, None, "اِمْتَازَ عَنْ غَيْرِهِ: انْفَرَدَ عَنْهُ بِفَضْلٍ — أَجْوَفُ يَائِيٌّ مِنْ بَابِ الِافْتِعَالِ."))
put_morph(mo, "khataba", _sg.derived(_sg.B3, _sg.W3, "ُ", "خَاطَب", "خَاطِب", "خَاطِب", "مُخَاطَبَة / خِطَاب", "مُخَاطِب", "مُخَاطَب", "خُوطِبَ", "يُخَاطَبُ", "خَاطَبَهُ: وَجَّهَ إِلَيْهِ الْكَلَامَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch22 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 22 (print pp. 37–38 — the END of the story of Zakariyyā): God's signs and His power, with 21:89–90 (s1–s4); Yaḥyā shoulders the burdens of the call, with 19:12–15 (s5–s7)."
ADD_TR = " Yirmi ikinci bölüm (baskı s. 37–38 — Zekeriyyâ kıssasının SONU): Allah'ın âyetleri ve kudreti, 21:89–90 ile (s1–s4); Yahyâ davetin yüklerini üstleniyor, 19:12–15 ile (s5–s7)."
write_out(22, S, TITLE, ADD_EN, ADD_TR, "Zakariyyā §7–8", GLOSS_ADD, notes=(), related=())
report(22, S, GLOSS_ADD, ())
