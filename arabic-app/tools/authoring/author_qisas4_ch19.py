# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 19: «يُونُسُ فِي بَطْنِ الْحُوتِ» — §6 (Yūnus in the belly of the whale), §7 (God answered his prayer, with 21:87–88);
print pp. 30–31 — the END of the story of Ayyūb and Yūnus.
python3 tools/authoring/author_qisas4_ch19.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "يُونُسُ فِي بَطْنِ الْحُوتِ", "en": "Yūnus in the belly of the whale", "tr": "Yûnus balığın karnında"}
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

# ---------------------------------------------------------------- §6 يُونُسُ فِي بَطْنِ الْحُوتِ (print p. 30)
sen("s1", "As for Yūnus, peace be upon him, he went off and boarded a ship with some people; it ran aground with them,",
        "Yûnus'a (a.s.) gelince: o gitti ve bir toplulukla birlikte bir gemiye bindi; gemi onlarla birlikte yan yattı,", [
  tok("وَأَمَّا", "amma", "part", [AT, "amma-tafsiliyya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ، جَوَابُهُ مَقْرُونٌ بِالْفَاءِ.", "«as for» — the particle of detailing; its answer takes the fāʾ.", "«-e gelince» — tafsîl harfi; cevabı fâ ile gelir.", segments=wa_("أَمَّا", "amma", "part")),
  tok("يُونُسُ", "yunus", "propn", [MK, MM], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūnus» — the mubtadaʾ; a diptote name.", "«Yûnus» — mübtedâ; gayr-i munsarıf."),
  *alayhi_salam(),
  tok("فَإِنَّهُ", "inna", "part", [IW, "amma-tafsiliyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«he» — the fāʾ of ammā's answer; inna with the pronoun as its ism.", "«o» — emmâ'nın cevap fâ'sı; inne ve ismi olan zamir.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  mazi("ذَهَبَ", "dhahaba", "«went off»", "«gitti»", tags=[IW], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  mazi("فَرَكِبَ", "rakiba", "«and boarded»", "«ve bindi»", tags=[AT], wa=True, hidden="هُوَ"),
  tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile birlikte»"),
  mudaf_ilayh("قَوْمٍ", "qawm", "«some people»", "«bir topluluk»"),
  fi(), majrur("سَفِينَةٍ", "safina", "«a ship»", "«bir gemiye»", punct="،"),
  mazi_ta("فَجَنَحَتْ", "janaha", "«it ran aground» (lit. listed)", "«yan yattı / karaya oturdu»", tags=[AT], wa=True),
  prep_pron("بِهِمْ", "bi", "هِمْ", "pron-3mp", "«with them»", "«onlarla»", punct="،"),
])
sen("s2", "and they feared they would drown, so they cast lots for a man whom they would throw out from among themselves, to lighten the ship of him;",
        "boğulmaktan korktular; bunun üzerine içlerinden birini denize atmak için kura çektiler — gemiyi ondan hafifletmek için;", [
  mazi_pl("وَخَافُوا", "khafa", "«and they feared»", "«ve korktular»", wa=True, tags=[AT, "hollow-verbs", MB]),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ خَافُوا.", "«that» — the clause is the object of «they feared».", "«… -maktan» — müevvel masdar «korktular»ın mef'ûlü."),
  tok("يَغْرَقُوا", "ghariqa", "verb", [AN, AK], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«they would drown» — one of the five verbs, naṣb by dropping the nūn.", "«boğulacaklar» — ef'âl-i hamseden; nasb alâmeti nûnun düşmesi."),
  mazi_pl("فَاقْتَرَعُوا", "iqtaraa", "«so they cast lots»", "«bunun üzerine kura çektiler»", wa=True, tags=[AT, "form-viii-verbs"]),
  prep("عَلَى", "ala", "«for»", "«için»"),
  majrur("رَجُلٍ", "rajul", "«a man»", "«bir adam»"),
  tok("يُلْقُونَهُ", "alqa", "verb", [AK, "jumla-sifa", "naqis-verbs", "form-iv-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ لِرَجُلٍ.", "«whom they would throw» — one of the five verbs; the clause describes «a man».", "«atacakları» — ef'âl-i hamseden; cümle «adam»ın sıfatı.", segments=[seg("يُلْقُونَ", "alqa", "verb"), pr3ms()]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("بَيْنِهِمْ", "bayna", "بَيْنِ", "هِمْ", "pron-3mp", "ظَرْفٌ مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«among themselves»", "«aralarından»", tags=[HJ, ID]),
  khamsa("يَتَخَفَّفُونَ", "takhaffafa", "«lightening [the ship]»", "«hafiflemek için»", tags=[HL, "form-v-verbs"], extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of him»", "«ondan»", punct="،"),
])
sen("s3", "and the lot fell on Yūnus, but they refused to throw him; then they repeated it and it fell on him again; they refused; then they repeated it, and it fell on him again.",
        "kura Yûnus'a çıktı; ama onu atmaya razı olmadılar; sonra kurayı tekrarladılar, yine ona çıktı; yine razı olmadılar; sonra tekrarladılar, yine ona çıktı.", [
  tok("فَوَقَعَتِ", "waqaa", "verb", [AT, "mithal-verbs"], "الْفَاءُ عَاطِفَةٌ، وَوَقَعَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and fell» — the tāʾ takes a kasra before the next hamzat al-waṣl.", "«ve düştü / çıktı» — tâ iki sâkin yüzünden kesre aldı.", segments=[seg("فَ", "fa", "conj"), seg("وَقَعَتِ", "waqaa", "verb")]),
  fail("الْقُرْعَةُ", "qura", "«the lot»", "«kura»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  tok("يُونُسَ", "yunus", "propn", [HJ, MM], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūnus» — jarr by fatḥa (a diptote).", "«Yûnus'a» — gayr-i munsarıf, fetha ile mecrûr."),
  mazi_wa_alif("فَأَبَوْا", "aba", "«but they refused»", "«ama razı olmadılar»", fa=True, tags=[MB]),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَبَوْا.", "«to» — the clause is the object of «they refused».", "«… -mayı» — müevvel masdar mef'ûl."),
  tok("يُلْقُوهُ", "alqa", "verb", [AN, AK, "naqis-verbs", "form-iv-verbs", MB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«throw him» — naṣb by dropping the nūn; the hāʾ is the object.", "«onu atmaya» — nûnun düşmesiyle mansub; hâ mef'ûl.", punct="،", segments=[seg("يُلْقُو", "alqa", "verb"), pr3ms()]),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  tok("أَعَادُوهَا", "aada", "verb", [MB, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«they repeated it» — the wāw is the doer, hā the object.", "«onu tekrarladılar» — vâv fâil, hâ mef'ûl.", segments=[seg("أَعَادُو", "aada", "verb"), seg("هَا", "pron-3fs", "pron")]),
  mazi_ta("فَوَقَعَتْ", "waqaa", "«and it fell»", "«ve çıktı»", tags=[AT, "mithal-verbs"], wa=True),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on him»", "«ona»"),
  tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (آضَ يَئِيضُ أَيْضًا) — بِمَعْنَى: كَذٰلِكَ.", "«again» — an absolute object of an unspoken verb (āḍa).", "«yine» — mahzuf bir fiilin mef'ûl-i mutlakı (âda).", punct="،"),
  mazi_wa_alif("فَأَبَوْا", "aba", "«they refused»", "«razı olmadılar»", fa=True, punct="،"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  tok("أَعَادُوهَا", "aada", "verb", [MB, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«they repeated it»", "«onu tekrarladılar»", punct="،", segments=[seg("أَعَادُو", "aada", "verb"), seg("هَا", "pron-3fs", "pron")]),
  mazi_ta("فَوَقَعَتْ", "waqaa", "«and it fell»", "«ve çıktı»", tags=[AT, "mithal-verbs"], wa=True),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on him»", "«ona»"),
  tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ.", "«again»", "«yine»", punct="،"),
])
sen("s4", "God Most High said: «and he cast lots, and was of the losers» (37:141) — that is, the lot fell on him;",
        "Allah Teâlâ buyurdu: «kura çekti de kaybedenlerden oldu» (37:141) — yani kura ona çıktı;", [
  qala(hidden=None), allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
  *quran([
  mazi("فَسَاهَمَ", "sahama", "«and he cast lots»", "«kura çekti»", tags=[AT, "form-iii-verbs"], wa=True, hidden="هُوَ"),
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and was» — kāna; its ism is concealed.", "«ve oldu» — kâne; ismi gizli.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  tok("الْمُدْحَضِينَ", "mudhad", "noun", [HJ, JS, KN, "ism-maful"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ مَفْعُولٍ مِنْ أَدْحَضَ.", "«the losers» (lit. those made to slip) — jarr by the yāʾ; a passive participle of Form IV.", "«kaybedenler» — cem-i müzekker sâlim; if'âl ism-i mef'ûlü.", punct="،"),
  ]),
  tok("أَيْ", "ay", "part", ["atf-bayan"], "حَرْفُ تَفْسِيرٍ.", "«that is» — the letter of explanation.", "«yani» — tefsir harfi.", punct=":"),
  mazi_ta("وَقَعَتْ", "waqaa", "«fell»", "«çıktı»", tags=["mithal-verbs"]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on him»", "«ona»"),
  fail("الْقُرْعَةُ", "qura", "«the lot»", "«kura»", punct="،"),
])
sen("s5", "so Yūnus, peace be upon him, stood up and stripped off his clothes, then threw himself into the sea.",
        "bunun üzerine Yûnus (a.s.) kalktı, elbiselerini çıkardı, sonra kendini denize attı.", [
  mazi("فَقَامَ", "qama", "«so stood up»", "«bunun üzerine kalktı»", tags=[AT, "hollow-verbs"], wa=True, hidden=None),
  fail_name("يُونُسُ", "yunus", "«Yūnus»", "«Yûnus»"),
  *alayhi_salam(),
  mazi("وَتَجَرَّدَ", "tajarrada", "«and stripped»", "«ve soyundu»", tags=[AT, "form-v-verbs"], wa=True, hidden="هُوَ"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  noun_pron("ثِيَابِهِ", "thawb", "ثِيَابِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his clothes»", "«elbiselerini»", tags=[HJ, ID, JT], punct="،"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  mazi("أَلْقَى", "alqa", "«threw»", "«attı»", tags=[MB, "naqis-verbs", "form-iv-verbs"], hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  noun_pron("نَفْسَهُ", "nafs", "نَفْسَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«himself»", "«kendini»", tags=[MB, ID]),
  fi(), majrur("الْبَحْرِ", "bahr", "«the sea»", "«denize»", punct="،"),
])
sen("s6", "And God, glory be to Him, had sent a whale that cleft the seas until it arrived, and it swallowed Yūnus when he threw himself from the ship;",
        "Allah (sübhânehû) denizleri yararak gelen bir balık göndermişti; Yûnus kendini gemiden attığı anda onu yuttu;", [
  tok("وَقَدْ", "qad", "part", ["qad-harf", HL], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [already]» — the wāw of state with qad.", "«ve [zaten]» — hâl vâvı ve tahkik kad'ı.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("أَرْسَلَ", "arsala", "«had sent»", "«göndermişti»", tags=[MB, "form-iv-verbs"], hidden=None),
  allah_fail(),
  tok("سُبْحَانَهُ", "subhan", "noun", ["maful-mutlaq", "hadhf-wa-taqdir", ID], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُسَبِّحُ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«glory be to Him» — an absolute object of an unspoken verb (usabbiḥu); the hāʾ is annexed.", "«O'nu tenzih ederim» — mahzuf fiilin mef'ûl-i mutlakı; hâ muzâfun ileyh.", segments=[seg("سُبْحَانَ", "subhan", "noun"), pr3ms()]),
  maful_("حُوتًا", "hut", "«a whale»", "«bir balık»"),
  mudari("يَشُقُّ", "shaqqa", "«that cleft»", "«yararak»", tags=["jumla-sifa", "doubled-verbs", MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِحُوتًا"),
  maful_("الْبِحَارَ", "bahr", "«the seas»", "«denizleri»", tags=[JT]),
  tok("حَتَّى", "hatta", "part", [HJ], "حَرْفُ غَايَةٍ وَابْتِدَاءٍ.", "«until»", "«… -inceye kadar»"),
  mazi("جَاءَ", "jaa", "«it arrived»", "«geldi»", tags=["hollow-verbs"], hidden="هُوَ", punct="،"),
  mazi("فَالْتَقَمَ", "iltaqama", "«and swallowed»", "«ve yuttu»", tags=[AT, MB, "form-viii-verbs"], wa=True, hidden="هُوَ"),
  maful_name("يُونُسَ", "yunus", "«Yūnus»", "«Yûnus'u»"),
  tok("حِينَ", "hin", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when»", "«… -dığı anda»"),
  mazi("أَلْقَى", "alqa", "«he threw»", "«attı»", tags=[MB, "naqis-verbs", "form-iv-verbs", ID], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ حِينَ"),
  noun_pron("نَفْسَهُ", "nafs", "نَفْسَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«himself»", "«kendini»", tags=[MB, ID]),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("السَّفِينَةِ", "safina", "«the ship»", "«gemiden»", punct="،"),
])
sen("s7", "and God inspired that whale: do not eat any flesh of his, and do not break any bone of his.",
        "Allah o balığa şöyle vahyetti: onun etinden yeme, kemiğini kırma.", [
  mazi("فَأَوْحَى", "awha", "«and inspired»", "«ve vahyetti»", tags=[AT, "naqis-verbs", "form-iv-verbs"], wa=True, hidden=None, extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  allah_fail(),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  ishara("ذٰلِكَ", "dhalika", "jarr", "«that»", "«o»"),
  tok("الْحُوتِ", "hut", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ (أَوْ عَطْفُ بَيَانٍ).", "«whale» — a badal of the demonstrative.", "«balığa» — ism-i işâretten bedel."),
  tok("أَنْ", "an-masdariyya", "part", [AN, "atf-bayan"], "أَنْ تَفْسِيرِيَّةٌ بِمَعْنَى أَيْ (لِأَنَّ أَوْحَى فِيهِ مَعْنَى الْقَوْلِ دُونَ حُرُوفِهِ)، وَقِيلَ: مَصْدَرِيَّةٌ.", "«[saying] that» — the explaining an (= «that is»), since «inspired» carries the sense of saying; or the an of naṣb.", "«şöyle ki» — tefsir en'i (vahyetmek söz mânâsı taşır); masdariyye de denmiştir."),
  la_nafiya(),
  tok("تَأْكُلَ", "akala", "verb", [AN, "la-nafiya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ (عَلَى الْمَصْدَرِيَّةِ) وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَالنَّفْيُ بِلَا.", "«do not eat» — naṣb by an (on the maṣdar reading), the doer «you» concealed; the negation is lā's.", "«yeme» — en ile mansub; fâil gizli «sen»; nefiy lâ ile."),
  li_pron("لَهُ", "هُ", "pron-3ms", "«of his»", "«onun»"),
  maful_("لَحْمًا", "lahm", "«flesh»", "«et»", punct="،"),
  tok("وَلَا", "la-nahiya", "part", [AT, "la-nahiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«and do not» — the prohibiting lā, which governs jazm.", "«ve … -ma» — cezm eden nehiy lâ'sı.", segments=wa_("لَا", "la-nahiya", "part")),
  tok("تَهْشِمْ", "hashama", "verb", ["la-nahiya", LJ], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«break» — jazm by the prohibiting lā, the sign is the sukūn.", "«kırma» — nehiy lâ'sıyla meczûm; alâmeti sükûn."),
  li_pron("لَهُ", "هُ", "pron-3ms", "«of his»", "«onun»"),
  maful_("عَظْمًا", "azm", "«a bone»", "«kemik»", punct="."),
])
# ---------------------------------------------------------------- §7 وَاسْتَجَابَ اللهُ دُعَاءَهُ (print p. 31)
sen("s8", "So he was in the darkness of the whale's belly, in the darkness of the sea, in the darkness of the night — darknesses one above another;",
        "Böylece balığın karnının karanlığında, denizin karanlığında, gecenin karanlığında idi — üst üste karanlıklar;", [
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«so he was» — kāna; its ism is concealed.", "«böylece … idi» — kâne; ismi gizli.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("فِي", "fi", "prep", [HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«in» — the phrase is kāna's khabar.", "«-de» — câr-mecrûr kâne'nin haberi."),
  majrur("ظُلْمَةِ", "zulma", "«the darkness [of]»", "«karanlığında»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("بَطْنِ", "batn", "«the belly [of]»", "«karnının»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْحُوتِ", "hut", "«the whale»", "«balığın»", punct="،"),
  fi(), majrur("ظُلْمَةِ", "zulma", "«the darkness [of]»", "«karanlığında»", tags=[ID, BD], ar="بَدَلٌ مِنَ الْجَارِّ وَالْمَجْرُورِ قَبْلَهُ، مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْبَحْرِ", "bahr", "«the sea»", "«denizin»", punct="،"),
  fi(), majrur("ظُلْمَةِ", "zulma", "«the darkness [of]»", "«karanlığında»", tags=[ID, BD], ar="بَدَلٌ ثَانٍ، مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("اللَّيْلِ", "layl", "«the night»", "«gecenin»", punct="،"),
  tok("ظُلُمَاتٌ", "zulma", "noun", [MK, JM, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ ظُلُمَاتٌ، مَرْفُوعٌ بِالضَّمَّةِ.", "«darknesses» — the khabar of an unspoken mubtadaʾ (they are darknesses).", "«karanlıklar» — mahzuf mübtedânın haberi."),
  noun_pron("بَعْضُهَا", "bad", "بَعْضُ", "هَا", "pron-3fs", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِظُلُمَاتٌ.", "«some of them» — a mubtadaʾ; the clause describes «darknesses».", "«bazısı» — mübtedâ; cümle «karanlıklar»ın sıfatı.", tags=[MK, ID, "jumla-sifa"]),
  tok("فَوْقَ", "fawqa", "noun", [MF, MK, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ — مُتَعَلِّقٌ بِخَبَرٍ مَحْذُوفٍ.", "«above» — a place adverb; the khabar.", "«üstünde» — mekân zarfı; haber."),
  mudaf_ilayh("بَعْضٍ", "bad", "«another»", "«diğerinin»", punct="،"),
])
sen("s9", "how intense the darkness! and how far away the safety!",
        "ne şiddetli karanlık! ne uzak selâmet!", [
  tok("فَمَا", "ma-taajjub", "part", [AT, MK, "anwa-ma"], "الْفَاءُ لِلتَّفْرِيعِ، وَمَا التَّعَجُّبِيَّةُ: نَكِرَةٌ تَامَّةٌ بِمَعْنَى شَيْءٍ، مُبْتَدَأٌ.", "«how…!» — the mā of wonder, a mubtadaʾ meaning «something».", "«ne …!» — taaccüb mâ'sı, «bir şey» mânâsında mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-taajjub", "part")]),
  tok("أَشَدَّ", "ashadda", "verb", [MK, MB, "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ التَّعَجُّبِ (مَا أَفْعَلَهُ)، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، يَعُودُ عَلَى مَا — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«how intense!» — the frozen verb of wonder (mā afʿalahu); the clause is the khabar.", "«ne şiddetli!» — taaccüb fiili (mâ ef'alehû); cümle haber."),
  maful_("الظَّلَامَ", "zalam", "«the darkness»", "«karanlık»", ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — الْمُتَعَجَّبُ مِنْهُ.", punct="!"),
  tok("وَمَا", "ma-taajjub", "part", [AT, MK, "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا التَّعَجُّبِيَّةُ مُبْتَدَأٌ.", "«and how…!»", "«ve ne …!»", segments=wa_("مَا", "ma-taajjub", "part")),
  tok("أَبْعَدَ", "abada-far", "verb", [MK, MB, "form-iv-verbs"], "فِعْلٌ مَاضٍ جَامِدٌ لِلتَّعَجُّبِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«how far!» — the frozen verb of wonder.", "«ne uzak!» — taaccüb fiili."),
  maful_("السَّلَامَ", "salam", "«safety»", "«selâmet»", ar="مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُتَعَجَّبُ مِنْهُ.", punct="!"),
])
sen("s10", "He stayed as long as God willed him to stay; then God inspired him with the words that scatter the darknesses, lift the distresses and bring down mercy from above seven heavens;",
        "Allah'ın dilediği kadar kaldı; sonra Allah ona karanlıkları dağıtan, sıkıntıları kaldıran ve rahmeti yedi kat göğün üstünden indiren kelimeleri ilham etti;", [
  mazi("وَمَكَثَ", "makatha", "«and he stayed»", "«ve kaldı»", tags=[AT], wa=True, hidden="هُوَ"),
  tok("مَا", "ma-masdariyya", "part", ["anwa-ma", MF], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ — أَيْ: مُدَّةَ مَشِيئَةِ اللهِ.", "«as long as» — the adverbial maṣdar mā.", "«… -diği kadar» — zarfî masdar mâ'sı."),
  mazi("شَاءَ", "shaa", "«willed»", "«diledi»", tags=["hollow-verbs", MB], hidden=None),
  allah_fail(),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ شَاءَ.", "«that» — the clause is the object of «willed».", "«… -mesini» — müevvel masdar mef'ûl."),
  tok("يَمْكُثَ", "makatha", "verb", [AN], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he should stay» — naṣb by an.", "«kalmasını» — en ile mansub.", punct="،"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  v_pron("أَلْهَمَهُ", "alhama", "أَلْهَمَ", "هُ", "pron-3ms", "«inspired him»", "«ona ilham etti»", tags=[MX, "form-iv-verbs"], hidden=None),
  allah_fail(),
  tok("الْكَلِمَاتِ", "kalima", "noun", [MB, MX, JM], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the words» — the second object; naṣb by kasra (sound feminine plural).", "«kelimeleri» — ikinci mef'ûl; cem-i müennes sâlim, kesre ile mansub."),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِلْكَلِمَاتِ.", "«that» — the relative pronoun, a naʿt of «the words».", "«… -an» — ism-i mevsûl, «kelimeler»in sıfatı."),
  mudari("تُبَدِّدُ", "baddada", "«scatter»", "«dağıtan»", tags=[MW, MB, "form-ii-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  tok("الظُّلُمَاتِ", "zulma", "noun", [MB, JM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the darknesses» — naṣb by kasra.", "«karanlıkları» — kesre ile mansub.", punct="،"),
  mudari("وَتَكْشِفُ", "kashafa", "«and lift»", "«ve kaldıran»", tags=[AT, MB], hidden="هِيَ"),
  tok("الْكُرُبَاتِ", "kurba", "noun", [MB, JM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the distresses»", "«sıkıntıları»", punct="،"),
  mudari("وَتَسْتَنْزِلُ", "istanzala", "«and bring down»", "«ve indiren»", tags=[AT, MB, "form-x-verbs"], hidden="هِيَ"),
  maful_("الرَّحْمَةَ", "rahma", "«mercy»", "«rahmeti»"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("فَوْقِ", "fawqa", "«above»", "«üstünden»", tags=[ID], ar="ظَرْفٌ مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("سَبْعِ", "sab-seven", "«seven»", "«yedi»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى الْجَمْعِ."),
  tok("سَمَاوَاتٍ", "sama", "noun", [ID, JM, "tamyiz"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ؛ تَمْيِيزُ الْعَدَدِ.", "«heavens» — the counted noun, annexed; a sound feminine plural.", "«gök» — ma'dûd, muzâfun ileyh; cem-i müennes sâlim.", punct="،"),
])
sen("s11", "and hear the Qurʾān telling this strange, unparalleled story, in which there is solace for every wretched, distressed one, and every despairing, troubled one",
        "ve Kur'ân'ı dinle: bu garip, eşsiz kıssayı anlatıyor — onda her bîçâre ve kederli, her ümitsiz ve çalkantılı kimse için teselli vardır —", [
  tok("وَاسْمَعِ", "samia", "verb", [AT, AM, MB], "الْوَاوُ لِلِاسْتِئْنَافِ، وَاسْمَعْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and hear» — an imperative built on sukūn, given a kasra before the next hamzat al-waṣl.", "«ve dinle» — sükûn üzere mebnî emir; iki sâkin yüzünden kesre aldı.", segments=wa_("اسْمَعِ", "samia", "verb")),
  maful_("الْقُرْآنَ", "quran", "«the Qurʾān»", "«Kur'ân'ı»"),
  mudari("يَحْكِي", "haka", "«telling»", "«anlatıyor»", tags=[HL, MB, "naqis-verbs"], hidden="هُوَ", extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْجُمْلَةُ حَالٌ"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«this»", "«bu»"),
  tok("الْقِصَّةَ", "qissa", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«story» — a badal of the demonstrative.", "«kıssayı» — bedel."),
  naat("الْغَرِيبَةَ", "gharib", "«strange»", "«garip»", case="nasb"),
  naat2("الْفَرِيدَةَ", "farid", "«unparalleled»", "«eşsiz»", case="nasb", punct="،"),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَالِثٌ.", "«which» — the relative pronoun, a third naʿt.", "«ki onda» — ism-i mevsûl, üçüncü sıfat."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it» — the fronted khabar of the ṣila.", "«onda» — sılanın öne alınmış haberi.", tags=[MW, MK], extra_ar=" — خَبَرٌ مُقَدَّمٌ"),
  tok("سَلْوَى", "salwa", "noun", [MK, MW, "ism-maqsur-manqus"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«solace» — the delayed mubtadaʾ; a maqṣūr noun.", "«teselli» — sonraya bırakılmış mübtedâ; maksûr isim."),
  tok("لِكُلِّ", "kull", "noun", [HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ، مُضَافٌ.", "«for every»", "«her … için»", segments=[seg("لِ", "li", "prep"), seg("كُلِّ", "kull", "noun")]),
  mudaf_ilayh("بَائِسٍ", "bais", "«wretched one»", "«bîçâre»", tags=["ism-fail"]),
  naat("مَلْهُوفٍ", "malhuf", "«distressed»", "«kederli»", tags=["ism-maful"], punct="،"),
  atf("وَيَائِسٍ", "yais", "«despairing one»", "«ümitsiz»", "jarr", tags=["ism-fail"]),
  naat("مُضْطَرِبٍ", "mudtarib", "«troubled»", "«çalkantılı»", tags=["ism-fail", "form-viii-verbs"]),
])
sen("s12", "on whom the earth, for all its breadth, has closed in, and whose own soul has closed in on him, and who has seen with his own eyes that there is no refuge from God except to Him:",
        "bütün genişliğine rağmen yeryüzü ona dar gelmiş, canı da kendisine dar gelmiş ve Allah'tan yine O'na sığınmaktan başka sığınak olmadığını gözüyle görmüş olan kimse için:", [
  tok("قَدْ", "qad", "part", ["qad-harf", "jumla-sifa"], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لِيَائِسٍ.", "«[already]» — the clause after it describes «the despairing one».", "«[gerçekten]» — ardındaki cümle «ümitsiz»in sıfatı."),
  mazi_ta("ضَاقَتْ", "daqa", "«has closed in»", "«dar gelmiş»", tags=["hollow-verbs"]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on him»", "«ona»"),
  fail("الْأَرْضُ", "ard", "«the earth»", "«yeryüzü»"),
  tok("بِمَا", "ma-masdariyya", "part", [HJ, "anwa-ma"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ — أَيْ: بِرَحْبِهَا، مَعَ سَعَتِهَا.", "«for all [its breadth]» — bi + the maṣdar mā (= with its breadth).", "«bütün [genişliği]ne rağmen» — bâ + masdar mâ'sı.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  mazi_ta("رَحُبَتْ", "rahuba", "«it is broad»", "«geniş olmakla»", tags=["anwa-ma"], punct="،"),
  mazi_ta("وَضَاقَتْ", "daqa", "«and has closed in»", "«ve dar gelmiş»", tags=[AT, "hollow-verbs"], wa=True),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on him»", "«ona»"),
  noun_pron("نَفْسُهُ", "nafs", "نَفْسُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his own soul»", "«canı»", tags=[FL, ID], punct="،"),
  mazi("وَرَأَى", "raa", "«and has seen»", "«ve görmüş»", tags=[AT, MX, "naqis-verbs"], wa=True, hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  tok("عِيَانًا", "iyan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ (أَوْ حَالٌ) مَنْصُوبٌ — أَيْ: رُؤْيَةَ عِيَانٍ.", "«with his own eyes» — an absolute object (or a ḥāl).", "«gözüyle, ayan beyan» — mef'ûl-i mutlak (veya hâl)."),
  tok("أَنْ", "an-mukhaffafa", "part", [IW, "hadhf-wa-taqdir"], "أَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ رَأَى.", "«that» — an lightened from anna; its ism, the pronoun of the matter, is unspoken; the clause stands for raʾā's two objects.", "«… -dığını» — sakîleden hafifletilmiş en; ismi mahzuf şe'n zamiri."),
  la_jins("لَا"),
  ism_la("مَلْجَأَ", "malja", "«refuge»", "«sığınak»", tags=[]),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِمِنْ.", "«God»", "«Allah'tan»"),
  tok("إِلَّا", "illa", "part", ["istithna", "istithna-mufarragh"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except» — a restricting illā (an emptied exception).", "«ancak» — hasr edatı (müferrağ istisnâ)."),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Him» — lā's khabar.", "«O'na» — lâ'nın haberi.", tags=["la-nafiya-lil-jins"], extra_ar=" — خَبَرُ لَا", punct=":"),
])
sen("s13", "«And Dhū l-Nūn, when he went off in anger and thought that We would not constrain him — then he called out in the darknesses: there is no god but You; glory be to You; I have been one of the wrongdoers» (21:87).",
        "«Zünnûn'u da [an]: hani öfkeyle gitmiş ve ona güç yetiremeyeceğimizi sanmıştı; sonra karanlıklar içinde seslendi: Senden başka ilâh yoktur; Seni tenzih ederim; ben gerçekten zâlimlerden oldum» (21:87).", [
  *quran([
  tok("وَذَا", "dhu", "noun", [AT, MB, "five-nouns", ID, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَذَا مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ، مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«and [remember] the Man of» — the object of an unspoken «remember»; naṣb by the alif (one of the five nouns).", "«… sahibini de [an]» — mahzuf «an»ın mef'ûlü; esmâ-i hamseden, elif ile mansub.", segments=wa_("ذَا", "dhu", "noun")),
  mudaf_ilayh("النُّونِ", "nun-whale", "«the Whale» (al-Nūn)", "«balığın» (Nûn)"),
  tok("إِذْ", "idh", "noun", [MF, BD], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ، بَدَلُ اشْتِمَالٍ.", "«when» — a badal of inclusion.", "«hani»"),
  mazi("ذَهَبَ", "dhahaba", "«he went off»", "«gitti»", tags=[ID], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  hal("مُغَاضِبًا", "mughadib", "«in anger»", "«öfkeyle»", tags=["ism-fail", "form-iii-verbs"]),
  mazi("فَظَنَّ", "zanna", "«and thought»", "«ve sandı»", tags=[AT, MX, "doubled-verbs"], wa=True, hidden="هُوَ"),
  tok("أَنْ", "an-mukhaffafa", "part", [IW, MX, "hadhf-wa-taqdir"], "أَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ ظَنَّ.", "«that» — an lightened from anna; the clause stands for ẓanna's two objects.", "«… -ceğini» — hafifletilmiş en; cümle zanne'nin iki mef'ûlü yerinde."),
  tok("لَنْ", "lan", "part", [IW], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ — وَهُوَ الْفَاصِلُ بَيْنَ أَنْ الْمُخَفَّفَةِ وَخَبَرِهَا.", "«never» — negates the future and governs naṣb; the separator between the lightened an and its khabar.", "«asla» — nefiy, nasb ve istikbal harfi; hafifletilmiş en ile haberi arasındaki fâsıla."),
  tok("نَقْدِرَ", "qadara", "verb", [IW, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ — وَالْجُمْلَةُ خَبَرُ أَنْ؛ نَقْدِرَ عَلَيْهِ: نُضَيِّقَ عَلَيْهِ.", "«We would constrain» — naṣb by lan; the doer «We» concealed; here qadara ʿalā = to straiten.", "«güç yetireceğiz / daraltacağız» — len ile mansub; fâil gizli «biz»."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«him»", "«ona»"),
  mazi("فَنَادَى", "nada", "«then he called out»", "«sonra seslendi»", tags=[AT, "naqis-verbs", "form-iii-verbs", MB], wa=True, hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  fi(), tok("الظُّلُمَاتِ", "zulma", "noun", [HJ, JM], "مَجْرُورٌ بِفِي — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the darknesses»", "«karanlıklar içinde»"),
  tok("أَنْ", "an-masdariyya", "part", [AN, "atf-bayan"], "أَنْ تَفْسِيرِيَّةٌ (لِأَنَّ النِّدَاءَ فِيهِ مَعْنَى الْقَوْلِ)، وَقِيلَ: مَصْدَرِيَّةٌ.", "«[saying]» — the explaining an, since calling carries the sense of saying.", "«şöyle ki» — tefsir en'i."),
  la_jins("لَا"),
  ism_la("إِلٰهَ", "ilah", "«god»", "«ilâh»", khabar="مَوْجُودٌ (أَوْ: لَنَا)"),
  tok("إِلَّا", "illa", "part", ["istithna", "la-nafiya-lil-jins"], "أَدَاةُ اسْتِثْنَاءٍ.", "«but»", "«-den başka»"),
  tok("أَنْتَ", "anta", "pron", [BD, "istithna"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ بَدَلٌ مِنْ مَحَلِّ لَا وَاسْمِهَا (أَوْ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي الْخَبَرِ).", "«You» — a detached pronoun; a badal of the place of lā and its ism.", "«Sen» — munfasıl zamir; lâ ve isminin mahallinden bedel."),
  tok("سُبْحَانَكَ", "subhan", "noun", ["maful-mutlaq", "hadhf-wa-taqdir", ID], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُسَبِّحُ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«glory be to You» — an absolute object of the unspoken usabbiḥu; the kāf is annexed.", "«Seni tenzih ederim» — mahzuf fiilin mef'ûl-i mutlakı; kâf muzâfun ileyh.", segments=[seg("سُبْحَانَ", "subhan", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا (وَالنُّونُ لِلْوِقَايَةِ مُدْغَمَةٌ).", "«indeed I» — inna with the yāʾ as its ism.", "«gerçekten ben» — inne; yâ ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("كُنْتُ", "kana", "verb", [IW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهُ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I have been» — kāna with the tāʾ as its ism; the clause is inna's khabar.", "«ben … oldum» — kâne; tâ ismi; cümle inne'nin haberi.", segments=[seg("كُنْ", "kana", "verb"), seg("تُ", "pron-1s", "pron")]),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  tok("الظَّالِمِينَ", "zalim", "noun", [HJ, JS, KN, "ism-fail"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the wrongdoers» — jarr by the yāʾ.", "«zâlimler» — yâ ile mecrûr.", punct="۝"),
  ]),
])
sen("s14", "«So We answered him and saved him from the distress; and thus do We save the believers» (21:88).",
        "«Biz de ona icabet ettik ve onu gamdan kurtardık; müminleri işte böyle kurtarırız» (21:88).", [
  *quran([
  tok("فَاسْتَجَبْنَا", "istajaba", "verb", [AT, "hollow-verbs", "form-x-verbs"], "الْفَاءُ عَاطِفَةٌ، وَاسْتَجَبْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«so We answered» — nā is the doer.", "«Biz de icabet ettik» — nâ fâil.", segments=[seg("فَ", "fa", "conj"), seg("اسْتَجَبْ", "istajaba", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«him»", "«ona»"),
  tok("وَنَجَّيْنَاهُ", "najja", "verb", [AT, MB, "naqis-verbs", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَنَجَّيْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and We saved him» — nā the doer, the hāʾ the object.", "«ve onu kurtardık» — nâ fâil, hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("نَجَّيْ", "najja", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْغَمِّ", "ghamm", "«the distress»", "«gam»"),
  tok("وَكَذٰلِكَ", "kadhalika", "part", [AT, "maful-mutlaq", "asma-al-ishara"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْكَافُ لِلتَّشْبِيهِ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ: إِنْجَاءً مِثْلَ ذٰلِكَ، وَذَا اسْمُ إِشَارَةٍ مَجْرُورٌ بِالْكَافِ.", "«and thus» — the kāf of likeness standing for an absolute object (a saving like that).", "«ve işte böyle» — teşbih kâfı, mef'ûl-i mutlak yerinde.", segments=[seg("وَ", "wa", "conj"), seg("كَذٰلِكَ", "kadhalika", "part")]),
  tok("نُنْجِي", "anjaa", "verb", ["mudari-marfu", MB, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«do We save» — a defective muḍāriʿ; the doer «We» concealed.", "«kurtarırız» — nâkıs muzari; fâil gizli «biz»."),
  tok("الْمُؤْمِنِينَ", "mumin", "noun", [MB, JS, "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the believers» — naṣb by the yāʾ.", "«müminleri» — yâ ile mansub.", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: ashadda, an-mukhaffafa, nun-whale NEW; abada-far, subhan, kadhalika, ma-taajjub, bad, sab-seven reused)
CAND = {
 "amma": G("amma", "أَمَّا", None, "part", "as for", "-e gelince", 1),
 "yunus": G("yunus", "يُونُس", None, "propn", "Yūnus (Jonah)", "Yûnus", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "salam": G("salam", "سَلَام", "س ل م", "noun", "peace; safety", "selâm; selâmet", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "dhahaba": G("dhahaba", "ذَهَبَ", "ذ ه ب", "verb", "to go", "gitmek", 1),
 "rakiba": G("rakiba", "رَكِبَ", "ر ك ب", "verb", "to ride, to board", "binmek", 1),
 "maa": G("maa", "مَعَ", None, "noun", "with", "ile", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people; some people", "kavim; bir topluluk", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "safina": G("safina", "سَفِينَة", "س ف ن", "noun", "a ship", "gemi", 1),
 "janaha": G("janaha", "جَنَحَ", "ج ن ح", "verb", "to incline, to list (of a ship); to run aground", "yana yatmak, meyletmek (gemi)", 4),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "khafa": G("khafa", "خَافَ", "خ و ف", "verb", "to fear (hollow)", "korkmak (ecvef)", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "ghariqa": G("ghariqa", "غَرِقَ", "غ ر ق", "verb", "to drown", "boğulmak", 2),
 "iqtaraa": G("iqtaraa", "اِقْتَرَعَ", "ق ر ع", "verb", "to cast lots (Form VIII)", "kura çekmek (iftiâl)", 3),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1),
 "alqa": G("alqa", "أَلْقَى", "ل ق ي", "verb", "to throw, to cast (Form IV, defective)", "atmak (if'âl, nâkıs)", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between, among", "arasında", 1),
 "takhaffafa": G("takhaffafa", "تَخَفَّفَ", "خ ف ف", "verb", "to lighten oneself, to be relieved of (Form V)", "hafiflemek, yükünü atmak (tefa''ul)", 3),
 "waqaa": G("waqaa", "وَقَعَ", "و ق ع", "verb", "to fall; (of a lot) to fall on", "düşmek; (kura) çıkmak", 1),
 "qura": G("qura", "قُرْعَة", "ق ر ع", "noun", "a lot (drawn)", "kura", 2),
 "aba": G("aba", "أَبَى", "أ ب ي", "verb", "to refuse (defective)", "kabul etmemek, direnmek (nâkıs)", 2),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "aada": G("aada", "أَعَادَ", "ع و د", "verb", "to repeat, to do again (Form IV, hollow)", "tekrarlamak (if'âl, ecvef)", 2),
 "aydan": G("aydan", "أَيْضًا", "أ ي ض", "noun", "also, again", "de, yine", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "sahama": G("sahama", "سَاهَمَ", "س ه م", "verb", "to cast lots with others (Form III)", "kura çekmek, kuraya katılmak (mufâale)", 3),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "mudhad": G("mudhad", "مُدْحَض", "د ح ض", "noun", "made to slip, defeated, a loser (a passive participle of Form IV)", "kaydırılmış, mağlup, kaybeden (if'âl ism-i mef'ûlü)", 4),
 "ay": G("ay", "أَيْ", None, "part", "that is", "yani", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to stand up (hollow)", "kalkmak (ecvef)", 1),
 "tajarrada": G("tajarrada", "تَجَرَّدَ", "ج ر د", "verb", "to strip oneself of (Form V)", "soyunmak, sıyrılmak (tefa''ul)", 3),
 "thawb": G("thawb", "ثَوْب", "ث و ب", "noun", "a garment", "elbise", 1, plural="ثِيَاب"),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "a soul, a self", "nefis, can; kendi", 1),
 "bahr": G("bahr", "بَحْر", "ب ح ر", "noun", "a sea", "deniz", 1, plural="بِحَار"),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send (Form IV)", "göndermek (if'âl)", 1),
 "subhan": G("subhan", "سُبْحَان", "س ب ح", "noun", "glory (be to …) — an absolute object", "tenzih, sübhân (mef'ûl-i mutlak)", 1),
 "hut": G("hut", "حُوت", "ح و ت", "noun", "a whale, a great fish", "balık, balina", 1),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to split, to cleave (doubled)", "yarmak (muzâaf)", 2),
 "hatta": G("hatta", "حَتَّى", None, "part", "until", "-e kadar", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come (hollow, hamzated)", "gelmek (ecvef, mehmûz)", 1),
 "iltaqama": G("iltaqama", "اِلْتَقَمَ", "ل ق م", "verb", "to swallow in one gulp (Form VIII)", "lokma gibi yutmak (iftiâl)", 3),
 "hin": G("hin", "حِين", "ح ي ن", "noun", "a time, a while; when (as a ẓarf)", "zaman, vakit; -dığı zaman (zarf)", 1),
 "awha": G("awha", "أَوْحَى", "و ح ي", "verb", "to inspire, to reveal (Form IV, defective)", "vahyetmek, ilham etmek (if'âl, nâkıs)", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "do not — the prohibiting lā", "-ma — nehiy lâ'sı", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "lahm": G("lahm", "لَحْم", "ل ح م", "noun", "flesh, meat", "et", 1),
 "hashama": G("hashama", "هَشَمَ", "ه ش م", "verb", "to break, to crush", "kırmak, ezmek", 3),
 "azm": G("azm", "عَظْم", "ع ظ م", "noun", "a bone", "kemik", 1),
 "zulma": G("zulma", "ظُلْمَة", "ظ ل م", "noun", "darkness", "karanlık", 1, plural="ظُلُمَات"),
 "batn": G("batn", "بَطْن", "ب ط ن", "noun", "a belly", "karın", 1),
 "layl": G("layl", "لَيْل", "ل ي ل", "noun", "night", "gece", 1),
 "bad": G("bad", "بَعْض", "ب ع ض", "noun", "some, a part", "bazı, bir kısım", 1),
 "fawqa": G("fawqa", "فَوْقَ", "ف و ق", "noun", "above", "üstünde", 1),
 "ma-taajjub": G("ma-taajjub", "مَا (التَّعَجُّبِيَّة)", None, "part", "how …! — the mā of wonder", "ne …! — taaccüb mâ'sı", 2),
 "ashadda": G("ashadda", "أَشَدَّ", "ش د د", "verb", "how intense! — the frozen verb of wonder (mā afʿalahu)", "ne şiddetli! — taaccüb fiili (mâ ef'alehû)", 3),
 "zalam": G("zalam", "ظَلَام", "ظ ل م", "noun", "darkness", "karanlık", 1),
 "abada-far": G("abada-far", "أَبْعَدَ", "ب ع د", "verb", "to remove far; (in wonder) how far!", "uzaklaştırmak; (taaccüb) ne uzak!", 2),
 "makatha": G("makatha", "مَكَثَ", "م ك ث", "verb", "to stay, to remain", "kalmak, durmak", 2),
 "ma-masdariyya": G("ma-masdariyya", "مَا (الْمَصْدَرِيَّة)", None, "part", "the maṣdar mā (as long as; the fact that)", "masdar mâ'sı (-diği sürece; -ması)", 2),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will (hollow, hamzated)", "dilemek (ecvef, mehmûz)", 1),
 "alhama": G("alhama", "أَلْهَمَ", "ل ه م", "verb", "to inspire (Form IV)", "ilham etmek (if'âl)", 2),
 "kalima": G("kalima", "كَلِمَة", "ك ل م", "noun", "a word", "kelime", 1, plural="كَلِمَات"),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "baddada": G("baddada", "بَدَّدَ", "ب د د", "verb", "to scatter, to dispel (Form II)", "dağıtmak (tef'îl)", 3),
 "kashafa": G("kashafa", "كَشَفَ", "ك ش ف", "verb", "to remove, to uncover", "kaldırmak, açmak", 1),
 "kurba": G("kurba", "كُرْبَة", "ك ر ب", "noun", "distress, anguish", "sıkıntı, kerb", 2, plural="كُرُبَات"),
 "istanzala": G("istanzala", "اِسْتَنْزَلَ", "ن ز ل", "verb", "to call down, to bring down (Form X)", "indirmek, inmesini istemek (istif'âl)", 3),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "sab-seven": G("sab-seven", "سَبْع", "س ب ع", "noun", "seven", "yedi", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "a heaven, the sky", "gök", 1, plural="سَمَاوَات"),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear", "işitmek, dinlemek", 1),
 "quran": G("quran", "قُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell, to relate (defective)", "anlatmak, hikâye etmek (nâkıs)", 2),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "gharib": G("gharib", "غَرِيب", "غ ر ب", "noun", "strange", "garip", 1),
 "farid": G("farid", "فَرِيد", "ف ر د", "noun", "unique, unparalleled", "eşsiz, ferid", 2),
 "salwa": G("salwa", "سَلْوَى", "س ل و", "noun", "solace, consolation (a maqṣūr noun)", "teselli (maksûr isim)", 3),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "bais": G("bais", "بَائِس", "ب أ س", "noun", "wretched, miserable (an active participle)", "bîçâre, perişan (ism-i fâil)", 3),
 "malhuf": G("malhuf", "مَلْهُوف", "ل ه ف", "noun", "distressed, grieved (a passive participle)", "kederli, yanık (ism-i mef'ûl)", 3),
 "yais": G("yais", "يَائِس", "ي أ س", "noun", "despairing (an active participle)", "ümitsiz (ism-i fâil)", 2),
 "mudtarib": G("mudtarib", "مُضْطَرِب", "ض ر ب", "noun", "troubled, agitated (an active participle of Form VIII)", "çalkantılı, muztarip (iftiâl ism-i fâili)", 3),
 "daqa": G("daqa", "ضَاقَ", "ض ي ق", "verb", "to be narrow, to close in on (hollow)", "dar gelmek, daralmak (ecvef)", 2),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "the earth", "yer, yeryüzü", 1),
 "rahuba": G("rahuba", "رَحُبَ", "ر ح ب", "verb", "to be wide, spacious", "geniş olmak", 3),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "iyan": G("iyan", "عِيَان", "ع ي ن", "noun", "seeing with one's own eyes", "gözle görme, ayan", 3),
 "an-mukhaffafa": G("an-mukhaffafa", "أَنْ (الْمُخَفَّفَة)", None, "part", "that — an lightened from anna", "… -dığını — sakîleden hafifletilmiş en", 3),
 "malja": G("malja", "مَلْجَأ", "ل ج أ", "noun", "a refuge", "sığınak", 2),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "dhu": G("dhu", "ذُو", None, "noun", "the possessor of (one of the five nouns)", "sahibi (esmâ-i hamseden)", 1),
 "nun-whale": G("nun-whale", "نُون", "ن و ن", "noun", "the Whale (al-Nūn — Dhū l-Nūn, Yūnus)", "balık (Nûn — Zünnûn, Yûnus)", 3),
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "mughadib": G("mughadib", "مُغَاضِب", "غ ض ب", "noun", "angry, in anger (an active participle of Form III)", "kızgın, öfkeli (mufâale ism-i fâili)", 3),
 "zanna": G("zanna", "ظَنَّ", "ظ ن ن", "verb", "to think, to suppose (doubled)", "sanmak, zannetmek (muzâaf)", 1),
 "lan": G("lan", "لَنْ", None, "part", "never (negates the future, governs naṣb)", "asla (istikbali nefyeder, nasb eder)", 1),
 "qadara": G("qadara", "قَدَرَ", "ق د ر", "verb", "to have power over; (qadara ʿalā) to straiten", "güç yetirmek; (alâ ile) daraltmak", 1),
 "nada": G("nada", "نَادَى", "ن د و", "verb", "to call out (Form III, defective)", "seslenmek (mufâale, nâkıs)", 1),
 "ilah": G("ilah", "إِلَه", "أ ل ه", "noun", "a god", "ilâh", 1),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (m. sg.)", "sen", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "zalim": G("zalim", "ظَالِم", "ظ ل م", "noun", "a wrongdoer (an active participle)", "zâlim (ism-i fâil)", 1),
 "istajaba": G("istajaba", "اِسْتَجَابَ", "ج و ب", "verb", "to answer, to respond (Form X, hollow)", "icabet etmek, cevap vermek (istif'âl, ecvef)", 2),
 "najja": G("najja", "نَجَّى", "ن ج و", "verb", "to save, to rescue (Form II, defective)", "kurtarmak (tef'îl, nâkıs)", 1),
 "ghamm": G("ghamm", "غَمّ", "غ م م", "noun", "grief, distress", "gam, keder", 2),
 "kadhalika": G("kadhalika", "كَذَلِكَ", None, "part", "thus, likewise", "böylece, işte böyle", 1),
 "anjaa": G("anjaa", "أَنْجَى", "ن ج و", "verb", "to save (Form IV, defective)", "kurtarmak (if'âl, nâkıs)", 2),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer", "mümin", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them / their", "onları / onların", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ashadda", _sg.entry("مِنْ بَابِ الْإِفْعَالِ — مُضَاعَفٌ", "أَفْعَلَ يُفْعِلُ", "إِشْدَاد", "مُشِدّ", _sg.mazi14("أَشَدّ", "أَشْدَد"), _sg.mudari14("ُ", "شِدّ", "شْدِد"), ["أَشِدَّ", "أَشِدَّا", "أَشِدُّوا", "أَشِدِّي", "أَشِدَّا", "أَشْدِدْنَ"], "يُشِدَّ", "يُشِدَّ", "تُشِدَّ", "مُشَدّ", "أُشِدَّ", "يُشَدُّ", "أَشَدَّ الشَّيْءَ: قَوَّاهُ وَأَحْكَمَهُ — وَفِي التَّعَجُّبِ (مَا أَشَدَّ الظَّلَامَ!) فِعْلٌ جَامِدٌ لَا يَتَصَرَّفُ."))
put_morph(mo, "janaha", _sg.sound1("fataha", "جَنَح", "جْنَح", "اِجْنَح", "جُنُوح", "جَانِح", None, None, None, "جَنَحَتِ السَّفِينَةُ: مَالَتْ وَلَزِقَتْ بِالْأَرْضِ؛ وَجَنَحَ إِلَى الشَّيْءِ: مَالَ إِلَيْهِ."))
put_morph(mo, "ghariqa", _sg.sound1("samia", "غَرِق", "غْرَق", "اِغْرَق", "غَرَق", "غَارِق (غَرِيق)", None, None, None, "غَرِقَ فِي الْمَاءِ: غَاصَ فِيهِ وَهَلَكَ."))
put_morph(mo, "iqtaraa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِقْتَرَع", "قْتَرِع", "اِقْتَرِع", "اِقْتِرَاع", "مُقْتَرِع", "مُقْتَرَع عَلَيْهِ", None, None, "اِقْتَرَعُوا: ضَرَبُوا الْقُرْعَةَ بَيْنَهُمْ."))
put_morph(mo, "takhaffafa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَخَفَّف", "تَخَفَّف", "تَخَفَّف", "تَخَفُّف", "مُتَخَفِّف", None, None, None, "تَخَفَّفَ مِنَ الشَّيْءِ: أَلْقَى بَعْضَ حِمْلِهِ لِيَخِفَّ."))
put_morph(mo, "aada", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَعَاد", "أَعَد", "عِيد", "عِد", "أَعِيد", "أَعِد", "إِعَادَة", "مُعِيد", "مُعَاد", "أُعِيدَ", "يُعَادُ", "أَعَادَ الشَّيْءَ: كَرَّرَهُ وَرَدَّهُ — أَجْوَفُ وَاوِيٌّ مِنْ بَابِ الْإِفْعَالِ."))
put_morph(mo, "sahama", _sg.derived(_sg.B3, _sg.W3, "ُ", "سَاهَم", "سَاهِم", "سَاهِم", "مُسَاهَمَة", "مُسَاهِم", "مُسَاهَم", "سُوهِمَ", "يُسَاهَمُ", "سَاهَمَ الْقَوْمَ: قَارَعَهُمْ، ضَرَبَ مَعَهُمُ السِّهَامَ (الْقُرْعَةَ)."))
put_morph(mo, "tajarrada", _sg.derived(_sg.B5, _sg.W5, "َ", "تَجَرَّد", "تَجَرَّد", "تَجَرَّد", "تَجَرُّد", "مُتَجَرِّد", None, None, None, "تَجَرَّدَ مِنْ ثِيَابِهِ: خَلَعَهَا."))
put_morph(mo, "iltaqama", _sg.derived(_sg.B8, _sg.W8, "َ", "اِلْتَقَم", "لْتَقِم", "اِلْتَقِم", "اِلْتِقَام", "مُلْتَقِم", "مُلْتَقَم", "اُلْتُقِمَ", "يُلْتَقَمُ", "اِلْتَقَمَهُ: ابْتَلَعَهُ كَاللُّقْمَةِ."))
put_morph(mo, "awha", _sg.derived_naqis("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَوْحَ", "وح", "i", "أَوْح", "إِيحَاء", "مُوحٍ (الْمُوحِي)", "مُوحًى (إِلَيْهِ)", "أُوحِيَ", "يُوحَى", "أَوْحَى اللهُ إِلَيْهِ: أَعْلَمَهُ خُفْيَةً — مِثَالٌ وَاوِيٌّ نَاقِصٌ يَائِيٌّ (لَفِيفٌ مَفْرُوقٌ)."))
put_morph(mo, "hashama", _sg.sound1("daraba", "هَشَم", "هْشِم", "اِهْشِم", "هَشْم", "هَاشِم", "مَهْشُوم", "هُشِمَ", "يُهْشَمُ", "هَشَمَ الْعَظْمَ: كَسَرَهُ."))
put_morph(mo, "baddada", _sg.derived(_sg.B2, _sg.W2, "ُ", "بَدَّد", "بَدِّد", "بَدِّد", "تَبْدِيد", "مُبَدِّد", "مُبَدَّد", "بُدِّدَ", "يُبَدَّدُ", "بَدَّدَ الظُّلُمَاتِ: فَرَّقَهَا وَأَزَالَهَا."))
put_morph(mo, "istanzala", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَنْزَل", "سْتَنْزِل", "اِسْتَنْزِل", "اِسْتِنْزَال", "مُسْتَنْزِل", "مُسْتَنْزَل", "اُسْتُنْزِلَ", "يُسْتَنْزَلُ", "اِسْتَنْزَلَ الرَّحْمَةَ: طَلَبَ نُزُولَهَا."))
put_morph(mo, "daqa", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "ضَاق", "ضِق", "ضِيق", "ضِق", "ضِيق", "ضِق", "ضِيق", "ضَائِق", None, None, None, "ضَاقَ الشَّيْءُ يَضِيقُ: ضِدُّ اتَّسَعَ؛ وَضَاقَتْ عَلَيْهِ الْأَرْضُ: اشْتَدَّ بِهِ الْكَرْبُ — أَجْوَفُ يَائِيٌّ؛ لَمْ يَضِقْ."))
put_morph(mo, "rahuba", _sg.sound1("karuma", "رَحُب", "رْحُب", "اُرْحُب", "رُحْب / رَحَابَة", "رَحِيب (رَحْب)", None, None, None, "رَحُبَ الْمَكَانُ: اتَّسَعَ — مِنْ بَابِ كَرُمَ."))
put_morph(mo, "anjaa", _sg.derived_naqis("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَنْجَ", "نْج", "i", "أَنْج", "إِنْجَاء", "مُنْجٍ (الْمُنْجِي)", "مُنْجًى", "أُنْجِيَ", "يُنْجَى", "أَنْجَاهُ اللهُ: خَلَّصَهُ — نَاقِصٌ وَاوِيٌّ؛ نُنْجِي."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch19 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 19 (print pp. 30–31 — the END of the story of Ayyūb and Yūnus): Yūnus in the belly of the whale — the ship, the lots, 37:141, the whale commanded (s1–s7); the three darknesses, the words of deliverance, with 21:87–88 (s8–s14). The author's note (1) credits §6 to Ibn Kathīr's Tafsīr."
ADD_TR = " On dokuzuncu bölüm (baskı s. 30–31 — Eyyûb ve Yûnus kıssasının SONU): Yûnus balığın karnında — gemi, kura, 37:141, balığa emir (s1–s7); üç karanlık, kurtuluş kelimeleri, 21:87–88 ile (s8–s14). Yazarın (1) notu §6'yı İbn Kesîr'in Tefsîr'ine bağlar."
write_out(19, S, TITLE, ADD_EN, ADD_TR, "Ayyūb and Yūnus §6–7", GLOSS_ADD, notes=(), related=())
report(19, S, GLOSS_ADD, ())
