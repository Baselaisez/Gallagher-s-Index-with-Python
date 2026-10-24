# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 11: «قَصْرٌ عَظِيمٌ مِنْ زُجَاجٍ» — the end of §11 (the throne fetched and altered) and
§12 (the glass palace and what it was meant to teach); print pp. 20–21.
python3 tools/authoring/author_qisas4_ch11.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قَصْرٌ عَظِيمٌ مِنْ زُجَاجٍ", "en": "A great palace of glass", "tr": "Camdan büyük bir saray"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; ML = "maful-lah"; TM = "tamyiz"
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
def fa_mazi(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra_ar=""):
    return tok(full, lex, "verb", [AT] + list(tags), "الْفَاءُ عَاطِفَةٌ (لِلتَّعْقِيبِ)، وَ" + full[2:] + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}" if hidden else "") + extra_ar + ".", "«so» + " + en + " — a māḍī after the fāʾ of sequence.", "«de/da» + " + tr + " — ta'kîb fâ'sından sonra mâzî.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])
def v_ta_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, fa=False, extra=""):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", en + " — a feminine māḍī; the pronoun is its object.", tr + " — müennes mâzî; zamir mef'ûl.", punct=punct, segments=segs)
def mudari_pron(full, lex, stem, pron_form, pron_lex, en, tr, hidden="هُوَ", punct=None, tags=(), wa=False, fa=False, extra=""):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + ["mudari-marfu", MB] + list(tags), pre + stem + f" فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", en + " — a muḍāriʿ in rafʿ; the pronoun is its object.", tr + " — merfû muzari; zamir mef'ûl.", punct=punct, segments=segs)

# ---------------------------------------------------------------- the end of §11 (print p. 20)
sen("s1", "So he wished to have her throne brought — the throne she had put strong, trusted men in charge of — and asked his council to bring him her throne before the arrival of this great procession.",
        "Bu yüzden, güçlü ve güvenilir adamları başına diktiği tahtını getirtmek istedi ve meclisinden, bu büyük alay varmadan önce tahtını kendisine getirmelerini istedi.", [
  fa_mazi("فَأَرَادَ", "arada", "«he wished»", "«istedi»", tags=["hollow-verbs", "form-iv-verbs", MB]),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَرَادَ.", "«to» — the an of naṣb; the clause is the object of «wished».", "«… -mek» — nasb eden en; cümle «istedi»nin mef'ûlü."),
  tok("يُحْضِرَ", "ahdara", "verb", [AN, MB, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«have … brought» — naṣb by an.", "«getirtmek» — en ile mansub."),
  noun_pron("عَرْشَهَا", "arsh", "عَرْشَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her throne» — the object.", "«tahtını» — mef'ûl.", tags=[MB, ID]),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِلْعَرْشِ.", "«which» — a naʿt of the throne.", "«… -diği» — tahtın sıfatı."),
  mazi_ta("وَكَّلَتْ", "wakkala", "«she had put in charge»", "«başına dikmişti»", tags=[MW, "form-ii-verbs"]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«of it»", "«ona»"),
  maful_("رِجَالًا", "rajul", "«men»", "«adamlar»", tags=[JT]),
  tok("أَقْوِيَاءَ", "qawi", "noun", [NA, JT, MM], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ تَكْسِيرٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«strong» — the naʿt; a diptote plural.", "«güçlü» — sıfat; gayr-i munsarıf."),
  tok("أُمَنَاءَ", "amin", "noun", [NA, JT, MM], "نَعْتٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«trusted» — a second naʿt; a diptote.", "«güvenilir» — ikinci sıfat; gayr-i munsarıf.", punct="،"),
  fa_mazi("فَطَلَبَ", "talaba", "«and asked»", "«ve istedi»"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  noun_pron("مَلَئِهِ", "mala-chiefs", "مَلَئِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his council»", "«meclisinden»", tags=[HJ, ID]),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ طَلَبَ.", "«to» — the clause is the object of «asked».", "«… -melerini» — cümle «istedi»nin mef'ûlü."),
  tok("يَأْتُوهُ", "ata", "verb", [AN, AK, MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«they bring him» — naṣb by the dropped nūn; the wāw the doer, the hāʾ the object.", "«ona getirmelerini» — nûnun düşmesiyle mansub; vâv fâil, hâ mef'ûl.", segments=[seg("يَأْتُو", "ata", "verb"), pr3ms()]),
  noun_pron("بِعَرْشِهَا", "arsh", "بِعَرْشِ", "هَا", "pron-3fs", "الْبَاءُ حَرْفُ جَرٍّ، وَعَرْشِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her throne»", "«tahtını»", tags=[HJ, ID]),
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«before»", "«önce»"),
  mudaf_ilayh("وُصُولِ", "wusul", "«the arrival»", "«varmadan»", tags=[ID, "masdar"], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("هٰذَا", "hadha", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this»", "«bu»"),
  tok("الْمَوْكِبِ", "mawkib", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«procession» — the badal.", "«alay» — bedel."),
  naat("الْعَظِيمِ", "azim", "«great»", "«büyük»", tags=["sifa-mushabbaha"], punct="."),
])
sen("s2", "What Sulaymān wished came true in the shortest time, and it was a miracle; Sulaymān gave an order about it and some of its features were altered, to test her recognition and her alertness on seeing it;",
        "Süleyman'ın istediği en kısa vakitte gerçekleşti ve bu bir mucizeydi; Süleyman onunla ilgili emir verdi, görünce tanıyışını ve uyanıklığını sınamak için bazı özellikleri değiştirildi;", [
  tok("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=wa_("قَدْ", "qad", "part")),
  mazi("تَحَقَّقَ", "tahaqqaqa", "«came true»", "«gerçekleşti»", tags=["form-v-verbs"], hidden=None),
  tok("مَا", "ma-mawsula", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«what» — the relative, the doer.", "«… -diği» — ism-i mevsûl, fâil."),
  mazi("أَرَادَ", "arada", "«wished»", "«istedi»", tags=[MW, "hollow-verbs", "form-iv-verbs"], hidden=None, extra_ar=" — صِلَةٌ"),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  fi(), majrur("أَقْرَبِ", "aqrab", "«the shortest»", "«en kısa»", tags=[ID, "ism-tafdil", MM], ar="مَجْرُورٌ بِفِي، مُضَافٌ — اسْمُ تَفْضِيلٍ."),
  mudaf_ilayh("وَقْتٍ", "waqt", "«time»", "«vakitte»"),
  kana(),
  tok("مُعْجِزَةً", "mujiza", "noun", [KN, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«a miracle» — kāna's khabar; its ism concealed.", "«bir mucize» — kâne'nin haberi; ismi gizli.", punct="،"),
  mazi("وَأَمَرَ", "amara-v", "«and gave an order»", "«ve emir verdi»", tags=[AT], wa=True, hidden=None),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«about it»", "«onunla ilgili»"),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  tok("فَغَيَّرَ", "ghayyara", "verb", [AT, MB, "form-ii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَغَيَّرَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (أَيْ: أَمَرَ بِتَغْيِيرِهِ).", "«and altered» — the doer concealed (he had it altered).", "«ve değiştirdi» — fâil gizli (değiştirtti).", segments=[seg("فَ", "fa", "conj"), seg("غَيَّرَ", "ghayyara", "verb")]),
  tok("بَعْضَ", "bad", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«some [of]» — the object, annexed.", "«bazı» — mef'ûl, muzâf."),
  noun_pron("صِفَاتِهِ", "sifa", "صِفَاتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«of its features»", "«özelliklerini»", tags=[ID, JM]),
  tok("لِيَخْتَبِرَ", "ikhtabara", "verb", [TA, MB, "form-viii-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَيَخْتَبِرَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«to test» — the lām of cause; naṣb by a hidden an.", "«sınamak için» — ta'lîl lâmı; gizli en ile mansub.", segments=[seg("لِ", "li", "prep"), seg("يَخْتَبِرَ", "ikhtabara", "verb")]),
  noun_pron("مَعْرِفَتَهَا", "marifa", "مَعْرِفَتَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her recognition»", "«tanıyışını»", tags=[MB, ID]),
  noun_pron("وَتَنَبُّهَهَا", "tanabbuh", "وَتَنَبُّهَ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَتَنَبُّهَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her alertness»", "«ve uyanıklığını»", tags=[AT, ID, "masdar"]),
  tok("عِنْدَ", "inda", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«on» (lit. at)", "«… -ınca»"),
  noun_pron("رُؤْيَتِهِ", "ruya", "رُؤْيَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«seeing it»", "«onu görünce»", punct="،", tags=[ID, "masdar"]),
])
sen("s3", "and if the matter should confuse her, that would be a proof of the shortness of her sight in matters finer than it and farther out of reach.",
        "eğer iş ona karışık gelirse, bu, ondan daha ince ve ulaşılması daha uzak işlerdeki bakış kısalığına delil olacaktı.", [
  tok("وَإِنِ", "in-shartiyya", "part", [AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and if» — in, kasra for the two sukūns.", "«ve eğer» — in; iki sâkin için kesre.", segments=wa_("إِنِ", "in-shartiyya", "part")),
  mazi("الْتَبَسَ", "iltabasa", "«should confuse»", "«karışık gelirse»", tags=[SH, "form-viii-verbs"], hidden=None, extra_ar=" — فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ"),
  prep_pron("عَلَيْهَا", "ala", "هَا", "pron-3fs", "«her»", "«ona»"),
  fail("الْأَمْرُ", "amr-noun", "«the matter»", "«iş»"),
  tok("كَانَ", "kana", "verb", [SH, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«that would be» — kāna as the answer of the condition.", "«olacaktı» — şartın cevabı kâne."),
  tok("دَلِيلًا", "dalil-proof", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a proof» — kāna's khabar.", "«delil» — kâne'nin haberi."),
  prep("عَلَى", "ala", "«of»", "«-e»"),
  majrur("قُصُورِ", "qusur", "«the shortness»", "«kısalığına»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  noun_pron("نَظَرِهَا", "nazar", "نَظَرِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of her sight»", "«bakışının»", tags=[ID]),
  fi(), majrur("أُمُورٍ", "amr-noun", "«matters»", "«işlerde»", tags=[JT]),
  tok("أَدَقَّ", "adaqq", "noun", [NA, "ism-tafdil", MM], "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — اسْمُ تَفْضِيلٍ.", "«finer» — the naʿt; an elative, jarr by fatḥa.", "«daha ince» — sıfat; ism-i tafdîl, fetha ile mecrûr."),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«than it»", "«ondan»"),
  tok("وَأَبْعَدَ", "abad", "noun", [AT, NA, "ism-tafdil", MM], "الْوَاوُ عَاطِفَةٌ، وَأَبْعَدَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and farther» — joined; a diptote elative.", "«ve daha uzak» — ma'tûf; gayr-i munsarıf.", segments=wa_("أَبْعَدَ", "abad", "noun")),
  tok("مَنَالًا", "manal", "noun", [TM], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«out of reach» (lit. in attainment) — a tamyīz.", "«ulaşılması» — temyiz.", punct="."),
])

# ---------------------------------------------------------------- §12 قَصْرٌ عَظِيمٌ مِنْ زُجَاجٍ (print pp. 20–21)
sen("s4", "Sulaymān ordered the builders among men and jinn, and they built her a great palace of glass and made water run beneath it;",
        "Süleyman insanlardan ve cinlerden yapıcılara emretti; ona camdan büyük bir saray yaptılar ve altından su akıttılar;", [
  mazi("وَأَمَرَ", "amara-v", "«and ordered»", "«ve emretti»", tags=[MB], wa=True, hidden=None),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  tok("الْبَنَّائِينَ", "banna", "noun", [MB, JS, "sighat-mubalagha"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the builders» — the object, naṣb by the yāʾ.", "«yapıcıları» — mef'ûl, yâ ile mansub."),
  prep("مِنَ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْإِنْسِ", "ins", "«men»", "«insanlar»"),
  atf("وَالْجِنِّ", "jinn", "«jinn»", "«cinler»", "jarr", punct="،"),
  tok("فَبَنَوْا", "bana", "verb", [AT, MB, "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَبَنَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ الْمُقَدَّرِ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ.", "«and they built» — the defective verb's alif drops before the wāw of the group.", "«ve yaptılar» — nâkıs fiilin elifi cemaat vâvından önce düşmüş.", segments=[seg("فَ", "fa", "conj"), seg("بَنَوْا", "bana", "verb")]),
  li_pron("لَهَا", "هَا", "pron-3fs", "«for her»", "«ona»"),
  maful_("قَصْرًا", "qasr", "«a palace»", "«bir saray»"),
  naat("عَظِيمًا", "azim", "«great»", "«büyük»", case="nasb", tags=["sifa-mushabbaha"]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("زُجَاجٍ", "zujaj", "«glass»", "«cam»", punct="،"),
  tok("وَأَجْرَوْا", "ajra", "verb", [AT, MB, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَجْرَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ الْمُقَدَّرِ، وَالْوَاوُ فَاعِلٌ.", "«and made run»", "«ve akıttılar»", segments=wa_("أَجْرَوْا", "ajra", "verb")),
  noun_pron("تَحْتَهُ", "tahta", "تَحْتَ", "هُ", "pron-3ms", "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«beneath it»", "«altından»", tags=[MF, ID]),
  maful_("الْمَاءَ", "ma-water", "«water»", "«su»", punct="،"),
])
sen("s5", "so whoever did not know its secret would think it water; but the glass stood between the walker and the water.",
        "işin aslını bilmeyen onu su sanırdı; fakat cam, yürüyen ile su arasında engeldi.", [
  tok("فَالَّذِي", "alladhi", "pron", [AT, MK, MW], "الْفَاءُ لِلتَّفْرِيعِ، وَالَّذِي اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«so whoever» — the relative, the mubtadaʾ.", "«… -meyen» — ism-i mevsûl, mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الَّذِي", "alladhi", "pron")]),
  la_nafiya(),
  neg_mudari("يَعْرِفُ", "arafa", "«did not know»", "«bilmez»", tags=[MW, MB], hidden="هُوَ", extra=" — صِلَةٌ"),
  noun_pron("أَمْرَهُ", "amr-noun", "أَمْرَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its secret» (lit. its matter)", "«işin aslını»", tags=[MB, ID]),
  mudari("يَحْسَبُ", "hasiba", "«would think»", "«sanır»", tags=[MK, MX, "zanna-wa-akhawatuha"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ"),
  tok("أَنَّهُ", "anna", "part", [IW, MX], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ يَحْسَبُ.", "«that it» — anna with the hāʾ; the clause stands for the two objects of «think».", "«onun … olduğunu» — enne; hâ ismi; cümle «sanır»ın iki mef'ûlü yerine geçer.", segments=[seg("أَنَّ", "anna", "part"), pr3ms()]),
  khabar_inna("مَاءٌ", "ma-water", "«water»", "«su»", part="أَنَّ", punct="،"),
  tok("وَلٰكِنَّ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — lâkinne, inne'nin kardeşi.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  ism_inna("الزُّجَاجَ", "zujaj", "«the glass»", "«cam»", part="لٰكِنَّ"),
  mudari("يَحُولُ", "hala", "«stood»", "«engel olur»", tags=[IW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ لٰكِنَّ"),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasında»"),
  tok("الْمَاشِي", "mashi", "noun", [ID, "ism-maqsur-manqus", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — مَنْقُوصٌ.", "«the walker» — a manqūṣ, the kasra estimated.", "«yürüyen» — mankûs, kesre takdîrî."),
  tok("وَبَيْنَ", "bayna", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«and»", "«ile»", segments=wa_("بَيْنَ", "bayna", "noun")),
  mudaf_ilayh("الْمَاءِ", "ma-water", "«the water»", "«su»", punct="."),
])
sen("s6", "It was certain that the queen would take it for water and bare her legs, and there she would see her error and realise the shortness of her sight and her deception by appearances;",
        "Kesin olan, kraliçenin onu su sanıp bacaklarını açacağı ve orada hatasını görüp bakışının kısalığını ve görünüşlere aldanışını anlayacağıydı;", [
  kana(),
  tok("الْمُؤَكَّدُ", "muakkad", "noun", [KN, "ism-maful"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the certain thing» — kāna's ism.", "«kesin olan» — kâne'nin ismi."),
  tok("أَنَّ", "anna", "part", [IW, KN], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«that» — anna; the clause is kāna's khabar.", "«… -ması» — enne; cümle kâne'nin haberi."),
  ism_inna("الْمَلِكَةَ", "malika", "«the queen»", "«kraliçe»", part="أَنَّ"),
  mudari_pron("تَتَوَهَّمُهُ", "tawahhama", "تَتَوَهَّمُ", "هُ", "pron-3ms", "«would take it for»", "«onu … sanır»", hidden="هِيَ", tags=[IW, MX, "form-v-verbs"], extra=" أَوَّلُ — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  tok("مَاءً", "ma-water", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«water» — the second object.", "«su» — ikinci mef'ûl."),
  tok("فَتَكْشِفُ", "kashafa", "verb", [AT, "mudari-marfu"], "الْفَاءُ عَاطِفَةٌ، وَتَكْشِفُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and bare»", "«ve açar»", segments=[seg("فَ", "fa", "conj"), seg("تَكْشِفُ", "kashafa", "verb")]),
  prep("عَنْ", "an", "«(bare) …»", "«-i»"),
  noun_pron("سَاقَيْهَا", "saq", "سَاقَيْ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«her two legs» — a dual in jarr by the yāʾ; its nūn dropped for the iḍāfa.", "«iki bacağını» — tesniye, yâ ile mecrûr; nûnu izâfet için düşmüş.", punct="،", tags=[HJ, ID, "al-muthanna"]),
  tok("وَهُنَالِكَ", "hunalika", "noun", [AT, MF, "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَهُنَالِكَ اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and there» — the far demonstrative of place, a ẓarf.", "«ve orada» — uzak mekân işareti, zarf.", segments=wa_("هُنَالِكَ", "hunalika", "noun")),
  mudari("تَتَبَيَّنُ", "tabayyana", "«she would see»", "«görür»", tags=[MB, "form-v-verbs"], hidden="هِيَ"),
  maful_("الْخَطَأَ", "khata", "«the error»", "«hatayı»"),
  tok("وَتُدْرِكُ", "adraka", "verb", [AT, "mudari-marfu", MB, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتُدْرِكُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and realise»", "«ve anlar»", segments=wa_("تُدْرِكُ", "adraka", "verb")),
  tok("قُصُورَ", "qusur", "noun", [MB, ID, "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the shortness» — the object, annexed.", "«kısalığını» — mef'ûl, muzâf."),
  noun_pron("نَظَرِهَا", "nazar", "نَظَرِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of her sight»", "«bakışının»", tags=[ID]),
  noun_pron("وَانْخِدَاعَهَا", "inkhida", "وَانْخِدَاعَ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَانْخِدَاعَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her deception»", "«ve aldanışını»", tags=[AT, ID, "masdar", "form-vii-verbs"]),
  tok("بِالْمَظَاهِرِ", "mazhar", "noun", [HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمَظَاهِرِ مَجْرُورٌ.", "«by appearances»", "«görünüşlerle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْمَظَاهِرِ", "mazhar", "noun")]),
])
sen("s7", "she and her people had been prostrating to the sun because it is the greatest manifestation of light and life, which are among the attributes of God the Exalted;",
        "o ve kavmi güneşe secde ediyorlardı; çünkü güneş, Allah Teâlâ'nın sıfatlarından olan nur ve hayatın en büyük tecellisidir;", [
  tok("وَكَانَتْ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … had been» — kāna with the feminine tāʾ.", "«ve … idi» — te'nis tâ'sı ile kâne.", segments=wa_("كَانَتْ", "kana", "verb")),
  tok("هِيَ", "hiya", "pron", [KN], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«she» — kāna's ism.", "«o» — kâne'nin ismi."),
  noun_pron("وَقَوْمُهَا", "qawm", "وَقَوْمُ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَقَوْمُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her people»", "«ve kavmi»", tags=[AT, ID]),
  khamsa("يَسْجُدُونَ", "sajada", "«prostrating»", "«secde ediyorlardı»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  tok("لِلشَّمْسِ", "shams", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالشَّمْسِ مَجْرُورٌ.", "«to the sun»", "«güneşe»", punct="،", segments=[seg("لِ", "li", "prep"), seg("الشَّمْسِ", "shams", "noun")]),
  tok("لِأَنَّهَا", "lianna", "part", [TA, IW], "اللَّامُ لِلتَّعْلِيلِ حَرْفُ جَرٍّ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا.", "«because it» — the lām of cause with anna; hā its ism.", "«çünkü o» — ta'lîl lâmı ile enne; hâ ismi.", segments=[seg("لِأَنَّ", "lianna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("أَكْبَرُ", "akbar", "noun", [IW, ID, "ism-tafdil"], "خَبَرُ أَنَّ مَرْفُوعٌ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«the greatest» — anna's khabar, annexed; an elative.", "«en büyük» — enne'nin haberi, muzâf; ism-i tafdîl."),
  mudaf_ilayh("مَظْهَرٍ", "mazhar", "«manifestation»", "«tecellisi»"),
  tok("لِلنُّورِ", "nur", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالنُّورِ مَجْرُورٌ — مُتَعَلِّقٌ بِمَظْهَرٍ.", "«of light»", "«nurun»", segments=[seg("لِ", "li", "prep"), seg("النُّورِ", "nur", "noun")]),
  atf("وَالْحَيَاةِ", "hayat", "«life»", "«hayatın»", "jarr", punct="،"),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«which» — a naʿt.", "«… olan» — sıfat."),
  tok("هِيَ", "hiya", "pron", [MW, MK], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — صِلَةٌ.", "«are» (lit. they) — the mubtadaʾ of the ṣila.", "«o» — sılanın mübtedâsı."),
  prep("مِنْ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ."),
  majrur("صِفَاتِ", "sifa", "«the attributes»", "«sıfatlarından»", tags=[ID, JM], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«the Exalted»", "«Teâlâ»", punct="،"),
])
sen("s8", "and there the veil would be lifted from her eyes, and she would know that just as she had erred in treating the glass as water and bared her legs,",
        "ve orada perde gözlerinden kalkacak; camı su gibi görmekte hata edip bacaklarını açtığı gibi,", [
  tok("وَهُنَالِكَ", "hunalika", "noun", [AT, MF, "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَهُنَالِكَ اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and there»", "«ve orada»", segments=wa_("هُنَالِكَ", "hunalika", "noun")),
  mudari("يَنْكَشِفُ", "inkashafa", "«would be lifted»", "«kalkar»", tags=["form-vii-verbs"], hidden=None),
  fail("الْغِطَاءُ", "ghita", "«the veil»", "«perde»", tags=["ism-mamdud"]),
  prep("عَنْ", "an", "«from»", "«-den»"),
  noun_pron("عَيْنَيْهَا", "ayn", "عَيْنَيْ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«her two eyes» — a dual in jarr by the yāʾ.", "«iki gözünden» — tesniye, yâ ile mecrûr.", punct="،", tags=[HJ, ID, "al-muthanna"]),
  tok("فَتَعْرِفُ", "arafa", "verb", [AT, "mudari-marfu", MB], "الْفَاءُ عَاطِفَةٌ، وَتَعْرِفُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and she would know»", "«ve bilir»", segments=[seg("فَ", "fa", "conj"), seg("تَعْرِفُ", "arafa", "verb")]),
  tok("أَنَّهَا", "anna", "part", [IW, MB], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ تَعْرِفُ.", "«that she» — anna; the clause is the object of «know».", "«… -ını» — enne; cümle «bilir»in mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«just as»", "«… gibi»"),
  mazi_ta("أَخْطَأَتْ", "akhtaa", "«she had erred»", "«hata etti»", tags=["form-iv-verbs"]),
  fi(), majrur("مُعَامَلَةِ", "muamala", "«treating»", "«görmekte»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("الزُّجَاجِ", "zujaj", "«the glass»", "«camı»"),
  tok("مُعَامَلَةَ", "muamala", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ مَنْصُوبٌ، مُضَافٌ.", "«as [water]» (lit. the treatment of) — an absolute object naming the kind.", "«… muamelesi» — nev'i bildiren mef'ûl-i mutlak."),
  mudaf_ilayh("الْمَاءِ", "ma-water", "«water»", "«su»"),
  mazi_ta("فَكَشَفَتْ", "kashafa", "«and bared»", "«ve açtı»", tags=[AT], extra=" — وَالْفَاءُ عَاطِفَةٌ"),
  prep("عَنْ", "an", "«(bared) …»", "«-i»"),
  noun_pron("سَاقَيْهَا", "saq", "سَاقَيْ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَهَا مُضَافٌ إِلَيْهِ.", "«her two legs»", "«iki bacağını»", punct="،", tags=[HJ, ID, "al-muthanna"]),
])
sen("s9", "so too had she erred in treating the sun as the Creator, prostrating to it and worshipping it; and that was more telling than a hundred sermons and a thousand proofs.",
        "güneşe Yaratıcı muamelesi yapmakta da hata edip ona secde ettiğini ve taptığını bilecekti; bu, yüz hutbeden ve bin delilden daha etkiliydi.", [
  tok("كَذٰلِكَ", "kadhalika", "part", [HJ, "asma-al-ishara"], "الْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ فِي مَحَلِّ جَرٍّ — أَيْ: مِثْلَ ذٰلِكَ.", "«so too» — the kāf with the demonstrative: like that.", "«bunun gibi» — kâf ve ism-i işâret."),
  mazi_ta("أَخْطَأَتْ", "akhtaa", "«she had erred»", "«hata etti»", tags=["form-iv-verbs"]),
  fi(), majrur("مُعَامَلَةِ", "muamala", "«treating»", "«muamelede»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("الشَّمْسِ", "shams", "«the sun»", "«güneşe»"),
  tok("مُعَامَلَةَ", "muamala", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ مَنْصُوبٌ، مُضَافٌ.", "«as [the Creator]» — an absolute object naming the kind.", "«… muamelesi» — nev'i bildiren mef'ûl-i mutlak."),
  mudaf_ilayh("الْخَالِقِ", "khaliq", "«the Creator»", "«Yaratıcı»", tags=["ism-fail"]),
  mazi_ta("فَسَجَدَتْ", "sajada", "«and prostrated»", "«ve secde etti»", tags=[AT], extra=" — وَالْفَاءُ عَاطِفَةٌ"),
  li_pron("لَهَا", "هَا", "pron-3fs", "«to it»", "«ona»"),
  v_ta_pron("وَعَبَدَتْهَا", "abada", "عَبَدَتْ", "هَا", "pron-3fs", "«and worshipped it»", "«ve ona taptı»", wa=True, punct="،"),
  kana(),
  tok("ذٰلِكَ", "dhalika", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«that» — kāna's ism.", "«bu» — kâne'nin ismi."),
  tok("أَبْلَغَ", "ablagh", "noun", [KN, "ism-tafdil", MM], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more telling» — kāna's khabar; an elative.", "«daha etkili» — kâne'nin haberi; ism-i tafdîl."),
  prep("مِنْ", "min", "«than»", "«-den»"),
  majrur("مِائَةِ", "mia", "«a hundred»", "«yüz»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("خُطْبَةٍ", "khutba", "«sermon[s]»", "«hutbe»"),
  atf("وَأَلْفِ", "alf", "«a thousand»", "«bin»", "jarr", tags=[ID]),
  mudaf_ilayh("دَلِيلٍ", "dalil-proof", "«proof[s]»", "«delil»", punct="."),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: all planned keys clean; ablagh / kadhalika / lakinna reuse their stored spellings)
CAND = {
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to wish", "istemek", 1),
 "ahdara": G("ahdara", "أَحْضَرَ", "ح ض ر", "verb", "to have brought, to bring (Form IV)", "getirtmek, hazır etmek (if'âl)", 2),
 "arsh": G("arsh", "عَرْش", "ع ر ش", "noun", "a throne", "taht, arş", 1),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "which", "ki o", 1),
 "wakkala": G("wakkala", "وَكَّلَ", "و ك ل", "verb", "to put in charge, to entrust (Form II; with bi)", "başına dikmek, vekil kılmak (tef'îl; bi ile)", 3),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1, plural="رِجَال"),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1, plural="أَقْوِيَاء"),
 "amin": G("amin", "أَمِين", "أ م ن", "noun", "trustworthy, trusted", "güvenilir, emin", 1, plural="أُمَنَاء"),
 "talaba": G("talaba", "طَلَبَ", "ط ل ب", "verb", "to ask for, to seek", "istemek, talep etmek", 1),
 "mala-chiefs": G("mala-chiefs", "مَلَأ", "م ل أ", "noun", "the chiefs, the council", "ileri gelenler, meclis", 2),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come; to bring (with bi)", "gelmek; (bi ile) getirmek", 1),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "önce", 1),
 "wusul": G("wusul", "وُصُول", "و ص ل", "noun", "arrival (a maṣdar)", "varış, ulaşma (masdar)", 2),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "mawkib": G("mawkib", "مَوْكِب", "و ك ب", "noun", "a procession, a cortège", "alay, kafile", 3),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great", "büyük", 1),
 "tahaqqaqa": G("tahaqqaqa", "تَحَقَّقَ", "ح ق ق", "verb", "to come true; to be certain of (Form V)", "gerçekleşmek; emin olmak (tefa''ul)", 2),
 "aqrab": G("aqrab", "أَقْرَب", "ق ر ب", "noun", "nearest, shortest", "en yakın, en kısa", 2),
 "waqt": G("waqt", "وَقْت", "و ق ت", "noun", "time", "vakit", 1),
 "mujiza": G("mujiza", "مُعْجِزَة", "ع ج ز", "noun", "a miracle", "mucize", 1),
 "amara-v": G("amara-v", "أَمَرَ", "أ م ر", "verb", "to order", "emretmek", 1),
 "ghayyara": G("ghayyara", "غَيَّرَ", "غ ي ر", "verb", "to change, to alter (Form II)", "değiştirmek (tef'îl)", 2),
 "bad": G("bad", "بَعْض", "ب ع ض", "noun", "some, part of", "bazı, bir kısmı", 1),
 "sifa": G("sifa", "صِفَة", "و ص ف", "noun", "a feature, an attribute", "sıfat, özellik", 1, plural="صِفَات"),
 "ikhtabara": G("ikhtabara", "اِخْتَبَرَ", "خ ب ر", "verb", "to test (Form VIII)", "sınamak (iftiâl)", 2),
 "marifa": G("marifa", "مَعْرِفَة", "ع ر ف", "noun", "recognition, knowledge", "tanıma, marifet", 1),
 "tanabbuh": G("tanabbuh", "تَنَبُّه", "ن ب ه", "noun", "alertness, attention (maṣdar of Form V)", "uyanıklık, dikkat (tefa''ul masdarı)", 3),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "at, on (the occasion of)", "-ınca, yanında", 1),
 "ruya": G("ruya", "رُؤْيَة", "ر أ ي", "noun", "seeing, sight", "görme, rüyet", 2),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if", "eğer", 1),
 "iltabasa": G("iltabasa", "اِلْتَبَسَ", "ل ب س", "verb", "to be confused, obscure (Form VIII; with ʿalā)", "karışık gelmek, anlaşılmaz olmak (iftiâl; alâ ile)", 3),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "a matter", "iş", 1, plural="أُمُور"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "dalil-proof": G("dalil-proof", "دَلِيل", "د ل ل", "noun", "a proof, evidence", "delil", 1),
 "qusur": G("qusur", "قُصُور", "ق ص ر", "noun", "shortness, falling short (a maṣdar)", "kısalık, yetersizlik (masdar)", 3),
 "nazar": G("nazar", "نَظَر", "ن ظ ر", "noun", "sight, consideration", "bakış, nazar", 1),
 "adaqq": G("adaqq", "أَدَقّ", "د ق ق", "noun", "finer, more subtle (an elative)", "daha ince (ism-i tafdîl)", 3),
 "abad": G("abad", "أَبْعَد", "ب ع د", "noun", "farther (an elative)", "daha uzak (ism-i tafdîl)", 2),
 "manal": G("manal", "مَنَال", "ن ي ل", "noun", "attainment, reach", "ulaşma, erişme", 3),
 "banna": G("banna", "بَنَّاء", "ب ن ي", "noun", "a builder (an intensive form)", "yapıcı, mimar (mübalağa sîgası)", 2),
 "ins": G("ins", "إِنْس", "أ ن س", "noun", "mankind", "insanlar", 2),
 "jinn": G("jinn", "جِنّ", "ج ن ن", "noun", "the jinn", "cinler", 1),
 "bana": G("bana", "بَنَى", "ب ن ي", "verb", "to build", "yapmak, inşa etmek", 1),
 "qasr": G("qasr", "قَصْر", "ق ص ر", "noun", "a palace", "saray", 1, plural="قُصُور"),
 "zujaj": G("zujaj", "زُجَاج", "ز ج ج", "noun", "glass", "cam", 2),
 "ajra": G("ajra", "أَجْرَى", "ج ر ي", "verb", "to make run, to make flow (Form IV, defective)", "akıtmak (if'âl, nâkıs)", 2),
 "tahta": G("tahta", "تَحْتَ", "ت ح ت", "noun", "beneath — a ẓarf of place", "altında — mekân zarfı", 1),
 "ma-water": G("ma-water", "مَاء", "م و ه", "noun", "water", "su", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know", "bilmek", 1),
 "hasiba": G("hasiba", "حَسِبَ", "ح س ب", "verb", "to think, to suppose (a verb of the heart; two objects)", "sanmak (kalp fiili; iki mef'ûl)", 2),
 "anna": G("anna", "أَنَّ", None, "part", "that", "… -dığı", 1),
 "lakinna": G("lakinna", "لٰكِنَّ", None, "part", "but — a sister of inna (istidrāk)", "fakat — inne'nin kardeşi (istidrâk)", 1),
 "hala": G("hala", "حَالَ", "ح و ل", "verb", "to stand between, to prevent (hollow; with bayna)", "arasına girmek, engel olmak (ecvef; beyne ile)", 2),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "mashi": G("mashi", "مَاشٍ", "م ش ي", "noun", "a walker (a manqūṣ active participle)", "yürüyen (mankûs ism-i fâil)", 2),
 "muakkad": G("muakkad", "مُؤَكَّد", "أ ك د", "noun", "certain, assured (a passive participle of Form II)", "kesin, muhakkak (tef'îl ism-i mef'ûlü)", 2),
 "malika": G("malika", "مَلِكَة", "م ل ك", "noun", "a queen", "kraliçe", 1),
 "tawahhama": G("tawahhama", "تَوَهَّمَ", "و ه م", "verb", "to imagine, to take for (Form V; two objects)", "sanmak, vehmetmek (tefa''ul; iki mef'ûl)", 3),
 "kashafa": G("kashafa", "كَشَفَ", "ك ش ف", "verb", "to uncover, to bare (with ʿan)", "açmak, açığa çıkarmak (an ile)", 1),
 "saq": G("saq", "سَاق", "س و ق", "noun", "a leg, a shank", "bacak, baldır", 2),
 "hunalika": G("hunalika", "هُنَالِكَ", None, "noun", "there — the far demonstrative of place", "orada — uzak mekân işareti", 1),
 "tabayyana": G("tabayyana", "تَبَيَّنَ", "ب ي ن", "verb", "to see clearly, to become clear (Form V)", "açıkça görmek, belli olmak (tefa''ul)", 3),
 "khata": G("khata", "خَطَأ", "خ ط أ", "noun", "an error", "hata", 1),
 "adraka": G("adraka", "أَدْرَكَ", "د ر ك", "verb", "to realise, to grasp (Form IV)", "idrak etmek, kavramak (if'âl)", 2),
 "inkhida": G("inkhida", "اِنْخِدَاع", "خ د ع", "noun", "being deceived (maṣdar of Form VII)", "aldanma (infiâl masdarı)", 3),
 "mazhar": G("mazhar", "مَظْهَر", "ظ ه ر", "noun", "an appearance, a manifestation", "görünüş, mazhar, tecelli", 2, plural="مَظَاهِر"),
 "hiya": G("hiya", "هِيَ", None, "pron", "she", "o", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people", "kavim", 1),
 "sajada": G("sajada", "سَجَدَ", "س ج د", "verb", "to prostrate", "secde etmek", 1),
 "shams": G("shams", "شَمْس", "ش م س", "noun", "the sun", "güneş", 1),
 "lianna": G("lianna", "لِأَنَّ", None, "part", "because", "çünkü", 1),
 "akbar": G("akbar", "أَكْبَر", "ك ب ر", "noun", "greater, greatest (an elative)", "en büyük (ism-i tafdîl)", 1),
 "nur": G("nur", "نُور", "ن و ر", "noun", "light", "nur, ışık", 1),
 "hayat": G("hayat", "حَيَاة", "ح ي ي", "noun", "life", "hayat", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which (feminine)", "ki o", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "He is exalted", "yücedir", 1),
 "inkashafa": G("inkashafa", "اِنْكَشَفَ", "ك ش ف", "verb", "to be lifted, to be revealed (Form VII)", "kalkmak, açığa çıkmak (infiâl)", 2),
 "ghita": G("ghita", "غِطَاء", "غ ط و", "noun", "a cover, a veil (a mamdūd noun)", "örtü, perde (memdûd isim)", 2),
 "ayn": G("ayn", "عَيْن", "ع ي ن", "noun", "an eye", "göz", 1),
 "kama": G("kama", "كَمَا", None, "part", "as, just as", "… gibi", 1),
 "akhtaa": G("akhtaa", "أَخْطَأَ", "خ ط أ", "verb", "to err, to be mistaken (Form IV)", "hata etmek (if'âl)", 2),
 "muamala": G("muamala", "مُعَامَلَة", "ع م ل", "noun", "treatment, dealing (maṣdar of Form III)", "muamele (müfâale masdarı)", 2),
 "kadhalika": G("kadhalika", "كَذٰلِكَ", None, "part", "likewise, so too", "bunun gibi, böylece", 1),
 "khaliq": G("khaliq", "خَالِق", "خ ل ق", "noun", "the Creator (an active participle)", "Yaratıcı (ism-i fâil)", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "tapmak", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "ablagh": G("ablagh", "أَبْلَغُ", "ب ل غ", "noun", "more telling, more eloquent (an elative)", "daha etkili, daha beliğ (ism-i tafdîl)", 2),
 "mia": G("mia", "مِائَة", "م أ ي", "noun", "a hundred", "yüz", 1),
 "khutba": G("khutba", "خُطْبَة", "خ ط ب", "noun", "a sermon, a speech", "hutbe", 1),
 "alf": G("alf", "أَلْف", "أ ل ف", "noun", "a thousand", "bin", 1),
 "sulayman": G("sulayman", "سُلَيْمَان", None, "propn", "Sulaymān", "Süleyman", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ahdara", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَحْضَر", "حْضِر", "أَحْضِر", "إِحْضَار", "مُحْضِر", "مُحْضَر", "أُحْضِرَ", "يُحْضَرُ", "أَحْضَرَ الشَّيْءَ: جَاءَ بِهِ وَجَعَلَهُ حَاضِرًا."))
put_morph(mo, "wakkala", _sg.derived(_sg.B2, _sg.W2, "ُ", "وَكَّل", "وَكِّل", "وَكِّل", "تَوْكِيل", "مُوَكِّل", "مُوَكَّل", "وُكِّلَ", "يُوَكَّلُ", "وَكَّلَ بِالشَّيْءِ فُلَانًا: جَعَلَهُ قَائِمًا عَلَيْهِ."))
put_morph(mo, "talaba", _sg.sound1("nasara", "طَلَب", "طْلُب", "اُطْلُب", "طَلَب", "طَالِب", "مَطْلُوب", "طُلِبَ", "يُطْلَبُ", "طَلَبَ الشَّيْءَ: سَعَى فِي تَحْصِيلِهِ."))
put_morph(mo, "ghayyara", _sg.derived(_sg.B2, _sg.W2, "ُ", "غَيَّر", "غَيِّر", "غَيِّر", "تَغْيِير", "مُغَيِّر", "مُغَيَّر", "غُيِّرَ", "يُغَيَّرُ", "غَيَّرَ الشَّيْءَ: بَدَّلَهُ."))
put_morph(mo, "ikhtabara", _sg.derived(_sg.B8, _sg.W8, "َ", "اِخْتَبَر", "خْتَبِر", "اِخْتَبِر", "اِخْتِبَار", "مُخْتَبِر", "مُخْتَبَر", "اُخْتُبِرَ", "يُخْتَبَرُ", "اِخْتَبَرَهُ: امْتَحَنَهُ."))
put_morph(mo, "iltabasa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِلْتَبَس", "لْتَبِس", "اِلْتَبِس", "اِلْتِبَاس", "مُلْتَبِس", None, None, None, "اِلْتَبَسَ عَلَيْهِ الْأَمْرُ: اخْتَلَطَ وَأَشْكَلَ."))
put_morph(mo, "bana", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "بَنَ", "بْن", "i", "اِبْن", "بِنَاء", "بَانٍ (الْبَانِي)", "مَبْنِيّ", "بُنِيَ", "يُبْنَى", "بَنَى يَبْنِي: شَيَّدَ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ لَمْ يَبْنِ، بَنَوْا."))
put_morph(mo, "ajra", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَجْرَ", "جْر", "i", "أَجْر", "إِجْرَاء", "مُجْرٍ (الْمُجْرِي)", "مُجْرًى", "أُجْرِيَ", "يُجْرَى", "أَجْرَى الْمَاءَ: جَعَلَهُ يَجْرِي."))
put_morph(mo, "hasiba", _sg.sound1("samia", "حَسِب", "حْسَب", "اِحْسَب", "حُسْبَان", "حَاسِب", "مَحْسُوب", "حُسِبَ", "يُحْسَبُ", "حَسِبَهُ كَذَا: ظَنَّهُ — مِنْ أَفْعَالِ الْقُلُوبِ، يَنْصِبُ مَفْعُولَيْنِ (وَبَابُهُ أَيْضًا حَسِبَ يَحْسِبُ)."))
put_morph(mo, "hala", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "حَال", "حُل", "حُول", "حُل", "حُول", "حُل", "حَيْلُولَة", "حَائِل", None, None, None, "حَالَ بَيْنَ الشَّيْئَيْنِ: حَجَزَ بَيْنَهُمَا."))
put_morph(mo, "tawahhama", _sg.derived(_sg.B5, _sg.W5, "َ", "تَوَهَّم", "تَوَهَّم", "تَوَهَّم", "تَوَهُّم", "مُتَوَهِّم", "مُتَوَهَّم", "تُوُهِّمَ", "يُتَوَهَّمُ", "تَوَهَّمَ الشَّيْءَ كَذَا: ظَنَّهُ عَلَى غَيْرِ حَقِيقَتِهِ."))
put_morph(mo, "kashafa", _sg.sound1("daraba", "كَشَف", "كْشِف", "اِكْشِف", "كَشْف", "كَاشِف", "مَكْشُوف", "كُشِفَ", "يُكْشَفُ", "كَشَفَ الشَّيْءَ وَعَنْهُ: أَظْهَرَهُ وَرَفَعَ غِطَاءَهُ."))
put_morph(mo, "adraka", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَدْرَك", "دْرِك", "أَدْرِك", "إِدْرَاك", "مُدْرِك", "مُدْرَك", "أُدْرِكَ", "يُدْرَكُ", "أَدْرَكَ الشَّيْءَ: بَلَغَهُ وَفَهِمَهُ."))
put_morph(mo, "inkashafa", _sg.derived(_sg.B7, _sg.W7, "َ", "اِنْكَشَف", "نْكَشِف", "اِنْكَشِف", "اِنْكِشَاف", "مُنْكَشِف", None, None, None, "اِنْكَشَفَ الْغِطَاءُ: ارْتَفَعَ وَزَالَ."))
put_morph(mo, "akhtaa", _sg.entry(_sg.B4 + " — مَهْمُوزُ اللَّامِ", _sg.W4, "إِخْطَاء / خَطَأ", "مُخْطِئ", ["أَخْطَأَ", "أَخْطَآ", "أَخْطَؤُوا", "أَخْطَأَتْ", "أَخْطَأَتَا", "أَخْطَأْنَ", "أَخْطَأْتَ", "أَخْطَأْتُمَا", "أَخْطَأْتُمْ", "أَخْطَأْتِ", "أَخْطَأْتُمَا", "أَخْطَأْتُنَّ", "أَخْطَأْتُ", "أَخْطَأْنَا"], ["يُخْطِئُ", "يُخْطِئَانِ", "يُخْطِئُونَ", "تُخْطِئُ", "تُخْطِئَانِ", "يُخْطِئْنَ", "تُخْطِئُ", "تُخْطِئَانِ", "تُخْطِئُونَ", "تُخْطِئِينَ", "تُخْطِئَانِ", "تُخْطِئْنَ", "أُخْطِئُ", "نُخْطِئُ"], ["أَخْطِئْ", "أَخْطِئَا", "أَخْطِئُوا", "أَخْطِئِي", "أَخْطِئَا", "أَخْطِئْنَ"], "يُخْطِئَ", "يُخْطِئْ", "تُخْطِئْ", None, None, None, "أَخْطَأَ: لَمْ يُصِبْ — مَهْمُوزُ اللَّامِ، تُرْسَمُ هَمْزَتُهُ عَلَى مَا يُنَاسِبُ حَرَكَتَهَا."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch11 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 11 (print pp. 20–21, the end of §11 and §12): the throne fetched and altered as a test (s1–s3); the glass palace and the lesson it was built to teach (s4–s9)."
ADD_TR = " On birinci bölüm (baskı s. 20–21, 11. kısmın sonu ve 12. kısım): sınama için getirtilip değiştirilen taht (s1–s3); cam saray ve onunla verilmek istenen ders (s4–s9)."
write_out(11, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §11–12", GLOSS_ADD, notes=(), related=())
report(11, S, GLOSS_ADD, ())
