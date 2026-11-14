# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 15: «الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ (٣)» — §14, 27:37–44 and the story's closing line;
print pp. 23–24. The Qurʾānic text is given as the book prints it. END of the story of Dāwūd and Sulaymān.
python3 tools/authoring/author_qisas4_ch15.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ (٣)", "en": "The Qurʾān tells Sulaymān's story (3)", "tr": "Kur'ân Süleyman'ın kıssasını anlatır (3)"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; NT = "nun-tawkid"; TW = "tawkid"; IS = "al-istifham"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr"):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
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
def ya_ayyuha():
    return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "huruf-tanbih"], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَهَا لِلتَّنْبِيهِ.", "«O you»", "«ey»")]
def qalat(punct=None):
    return tok("قَالَتْ", "qala", "verb", [MB, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«she said»", "«dedi»", punct=punct)

sen("s1", "«Go back to them: we shall surely come upon them with hosts they have no power to face, and shall surely drive them out of it abased, and they will be humbled» (27:37).",
        "«Onlara dön: andolsun onlara karşı koyamayacakları ordularla geleceğiz ve onları oradan zelil olarak çıkaracağız; küçük düşmüş olacaklar» (27:37).", [
  *quran([
  tok("ارْجِعْ", "rajaa", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«go back» — an imperative on sukūn.", "«dön» — sükûn üzere mebnî emir."),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«to them»", "«onlara»"),
  tok("فَلَنَأْتِيَنَّهُمْ", "ata", "verb", [AT, TW, NT, MB, "naqis-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَنَأْتِيَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَهُمْ مَفْعُولٌ بِهِ.", "«we shall surely come upon them» — the oath's lām; built on fatḥa before the heavy nūn; hum the object.", "«andolsun onlara geleceğiz» — kasem lâmı; te'kid nûnu ile fetha üzere mebnî; hüm mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("لَ", "lam-qasam", "part"), seg("نَأْتِيَ", "ata", "verb"), seg("نَّ", "nun-tawkid", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("بِجُنُودٍ", "jund", "noun", [HJ, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَجُنُودٍ مَجْرُورٌ.", "«with hosts»", "«ordularla»", segments=[seg("بِ", "bi", "prep"), seg("جُنُودٍ", "jund", "noun")]),
  tok("لَا", "la-nafiya", "part", ["la-nafiya-lil-jins", "jumla-sifa"], "لَا النَّافِيَةُ لِلْجِنْسِ — وَالْجُمْلَةُ نَعْتٌ لِجُنُودٍ.", "«no» — the lā of absolute negation; the clause is a naʿt of the hosts.", "«hiç» — cinsi nefyeden lâ; cümle orduların sıfatı."),
  tok("قِبَلَ", "qibal", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«power» (lit. facing) — lā's ism, built on fatḥa.", "«güç» — lâ'nın ismi, fetha üzere mebnî."),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«they have» — lā's khabar.", "«onların … yok» — lâ'nın haberi.", tags=["la-nafiya-lil-jins"], extra=" — خَبَرُ لَا"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«to face them»", "«onlara karşı»"),
  tok("وَلَنُخْرِجَنَّهُمْ", "akhraja", "verb", [AT, TW, NT, MB, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لِلْقَسَمِ، وَنُخْرِجَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَهُمْ مَفْعُولٌ بِهِ.", "«and we shall surely drive them out»", "«ve onları mutlaka çıkaracağız»", segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-qasam", "part"), seg("نُخْرِجَ", "akhraja", "verb"), seg("نَّ", "nun-tawkid", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«out of it»", "«oradan»"),
  tok("أَذِلَّةً", "dhalil", "noun", [HL, JT], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«abased» — a ḥāl.", "«zelil olarak» — hâl."),
  tok("وَهُمْ", "hum", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and they» — the mubtadaʾ of a ḥāl clause.", "«ve onlar» — hâl cümlesinin mübtedâsı.", segments=wa_("هُمْ", "hum", "pron")),
  tok("صَاغِرُونَ", "saghir-abased", "noun", [MK, JS, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«humbled» — the khabar, rafʿ by the wāw.", "«küçük düşmüş» — haber, vâv ile merfû.", punct="."),
  ]),
])
sen("s2", "«He said: O chiefs, which of you will bring me her throne before they come to me in submission?» (27:38).",
        "«Dedi ki: Ey ileri gelenler, onlar bana teslim olarak gelmeden önce hanginiz bana onun tahtını getirir?» (27:38).", [
  *quran([
  qala(hidden="هُوَ", punct=None),
  *ya_ayyuha(),
  tok("الْمَلَأُ", "mala-chiefs", "noun", ["vocative-munada", NA], "نَعْتٌ لِأَيٍّ مَرْفُوعٌ.", "«chiefs»", "«ileri gelenler»"),
  noun_pron("أَيُّكُمْ", "ayy", "أَيُّ", "كُمْ", "pron-2mp", "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«which of you» — the question-word, the mubtadaʾ, annexed.", "«hanginiz» — soru ismi, mübtedâ, muzâf.", tags=[IS, MK, ID]),
  tok("يَأْتِينِي", "ata", "verb", [MK, "mudari-marfu", MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«will bring me» — the clause is the khabar; the yāʾ the object.", "«bana getirir» — cümle haber; yâ mef'ûl.", segments=[seg("يَأْتِي", "ata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  noun_pron("بِعَرْشِهَا", "arsh", "بِعَرْشِ", "هَا", "pron-3fs", "الْبَاءُ حَرْفُ جَرٍّ، وَعَرْشِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her throne»", "«onun tahtını»", tags=[HJ, ID]),
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«before»", "«önce»"),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that»", "«… -meden»"),
  tok("يَأْتُونِي", "ata", "verb", [AN, AK, MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«they come to me» — naṣb by the dropped nūn; the yāʾ the object.", "«bana gelmeleri» — nûnun düşmesiyle mansub; yâ mef'ûl.", segments=[seg("يَأْتُو", "ata", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("مُسْلِمِينَ", "muslim", "noun", [HL, JS, "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«in submission» — a ḥāl.", "«teslim olarak» — hâl.", punct="؟"),
  ]),
])
sen("s3", "«An ʿifrīt of the jinn said: I will bring it to you before you rise from your seat; and I am strong and trustworthy for it» (27:39).",
        "«Cinlerden bir ifrit dedi ki: Sen yerinden kalkmadan önce onu sana getiririm; ben buna gücü yeten, güvenilir biriyim» (27:39).", [
  *quran([
  qala(hidden=None, punct=None),
  fail("عِفْرِيتٌ", "ifrit", "«an ʿifrīt»", "«bir ifrit»"),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِعِفْرِيتٌ."),
  majrur("الْجِنِّ", "jinn", "«the jinn»", "«cinler»"),
  tok("أَنَا", "ana", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the mubtadaʾ.", "«ben» — mübtedâ."),
  tok("آتِيكَ", "ata", "verb", [MK, "mudari-marfu", MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ (أَوِ اسْمُ فَاعِلٍ خَبَرٌ).", "«will bring you» — the clause is the khabar; the kāf the object.", "«sana getiririm» — cümle haber; kâf mef'ûl.", segments=[seg("آتِي", "ata", "verb"), seg("كَ", "pron-2ms", "pron")]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«it»", "«onu»"),
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«before»", "«önce»"),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that»", "«… -madan»"),
  tok("تَقُومَ", "qama", "verb", [AN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«you rise» — naṣb by an.", "«kalkman» — en ile mansub."),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("مَقَامِكَ", "maqam", "مَقَامِ", "كَ", "pron-2ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your seat»", "«yerinden»", tags=[HJ, ID]),
  tok("وَإِنِّي", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«and indeed I»", "«ve şüphesiz ben»", segments=[seg("وَ", "wa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«for it» — attached to the khabar.", "«buna» — habere bağlı."),
  tok("لَقَوِيٌّ", "qawi", "noun", [IW], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَقَوِيٌّ خَبَرُ إِنَّ مَرْفُوعٌ.", "«surely strong» — the sliding lām; inna's khabar.", "«elbette güçlü» — kaydırılmış ibtidâ lâmı; inne'nin haberi.", segments=[seg("لَ", "lam-qasam", "part"), seg("قَوِيٌّ", "qawi", "noun")]),
  naat("أَمِينٌ", "amin", "«trustworthy»", "«güvenilir»", case="raf", punct="."),
  ]),
])
sen("s4", "«One who had knowledge of the Book said: I will bring it to you before your glance returns to you» (27:40).",
        "«Kitaptan bir bilgisi olan biri dedi ki: Gözünü kırpmadan önce onu sana getiririm» (27:40).", [
  *quran([
  qala(hidden=None, punct=None),
  tok("الَّذِي", "alladhi", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«the one who» — the relative, the doer.", "«… olan» — ism-i mevsûl, fâil."),
  noun_pron("عِنْدَهُ", "inda", "عِنْدَ", "هُ", "pron-3ms", "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِلَةٌ.", "«had» (lit. with him) — a fronted khabar; the ṣila.", "«onun … vardı» — öne alınmış haber; sıla.", tags=[MW, MF, ID, MK]),
  tok("عِلْمٌ", "ilm", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«knowledge» — the delayed mubtadaʾ.", "«bir bilgi» — mübtedâ."),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِعِلْمٌ."),
  majrur("الْكِتَابِ", "kitab", "«the Book»", "«kitap»"),
  tok("أَنَا", "ana", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«I»", "«ben»"),
  tok("آتِيكَ", "ata", "verb", [MK, "mudari-marfu", MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ — خَبَرٌ.", "«will bring you»", "«sana getiririm»", segments=[seg("آتِي", "ata", "verb"), seg("كَ", "pron-2ms", "pron")]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«it»", "«onu»"),
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«before»", "«önce»"),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that»", "«… -madan»"),
  tok("يَرْتَدَّ", "irtadda", "verb", [AN, "doubled-verbs", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — مُضَاعَفٌ.", "«returns» — naṣb by an; a doubled verb.", "«dönmeden» — en ile mansub; muzâaf."),
  prep_pron("إِلَيْكَ", "ila", "كَ", "pron-2ms", "«to you»", "«sana»"),
  noun_pron("طَرْفُكَ", "tarf", "طَرْفُ", "كَ", "pron-2ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your glance» — the doer.", "«gözün» — fâil.", punct=".", tags=[FL, ID]),
  ]),
])
sen("s5", "«When he saw it set before him he said: This is of my Lord's favour, to test me whether I give thanks or am ungrateful; whoever gives thanks, gives thanks for his own soul, and whoever is ungrateful — my Lord is rich, generous» (27:40).",
        "«Onu yanında yerleşmiş görünce dedi ki: Bu Rabbimin lütfundandır; şükür mü edeceğim yoksa nankörlük mü, beni sınamak için. Kim şükrederse ancak kendisi için şükreder; kim nankörlük ederse, Rabbim zengindir, kerimdir» (27:40).", [
  *quran([
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… -ınca»", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  tok("رَآهُ", "raa", "verb", [SH, MX, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«he saw it» — the hāʾ the object.", "«onu gördü» — hâ mef'ûl.", segments=[seg("رَآ", "raa", "verb"), pr3ms()]),
  tok("مُسْتَقِرًّا", "mustaqarr", "noun", [HL, "ism-fail", "form-x-verbs"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (أَوْ مَفْعُولٌ ثَانٍ).", "«set» — a ḥāl.", "«yerleşmiş olarak» — hâl."),
  noun_pron("عِنْدَهُ", "inda", "عِنْدَ", "هُ", "pron-3ms", "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«before him»", "«yanında»", tags=[MF, ID]),
  qala(hidden="هُوَ", punct=None, tags=[SH]),
  tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bu» — mübtedâ."),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ."),
  majrur("فَضْلِ", "fadl", "«the favour»", "«lütfu»", tags=[ID, MK], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  noun_pron("رَبِّي", "rabb", "رَبِّ", "ي", "pron-1s", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«of my Lord»", "«Rabbimin»", tags=[ID, "ya-al-mutakallim"]),
  tok("لِيَبْلُوَنِي", "bala-test", "verb", [TA, MB, "naqis-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَيَبْلُوَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«to test me» — the lām of cause; naṣb visible on the wāw; the yāʾ the object.", "«beni sınamak için» — ta'lîl lâmı; vâv üzerinde açık fetha; yâ mef'ûl.", segments=[seg("لِ", "li", "prep"), seg("يَبْلُوَ", "bala-test", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَأَشْكُرُ", "shakara", "verb", [IS, "mudari-marfu", MB], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَأَشْكُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ يَبْلُو الثَّانِي (مُعَلَّقٌ).", "«whether I give thanks» — the hamza of question; the clause is the second object of «test».", "«şükür mü edeceğim» — soru hemzesi; cümle «sına»nın ikinci mef'ûlü.", segments=[seg("أَ", "hamza-istifham", "part"), seg("أَشْكُرُ", "shakara", "verb")]),
  tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ.", "«or»", "«yoksa»"),
  mudari("أَكْفُرُ", "kafara", "«am ungrateful»", "«nankörlük mü»", tags=[AT], hidden="أَنَا"),
  tok("وَمَنْ", "man-shartiyya", "pron", [AT, SH, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and whoever» — the conditional man.", "«ve kim» — şart ismi.", segments=wa_("مَنْ", "man-shartiyya", "pron")),
  mazi("شَكَرَ", "shakara", "«gives thanks»", "«şükrederse»", tags=[SH], hidden="هُوَ", extra_ar=" — فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ"),
  tok("فَإِنَّمَا", "innama", "part", ["fa-khabar-mubtada", SH, "innama-kaffa"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّمَا أَدَاةُ حَصْرٍ.", "«then only» — the fāʾ of the answer with innamā.", "«o takdirde ancak» — cevap fâ'sı ve innemâ.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّمَا", "innama", "part")]),
  mudari("يَشْكُرُ", "shakara", "«he gives thanks»", "«şükreder»", tags=[SH], hidden="هُوَ"),
  noun_pron("لِنَفْسِهِ", "nafs", "لِنَفْسِ", "هِ", "pron-3ms", "اللَّامُ حَرْفُ جَرٍّ، وَنَفْسِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«for his own soul»", "«kendisi için»", tags=[HJ, ID]),
  tok("وَمَنْ", "man-shartiyya", "pron", [AT, SH, MK], "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ مُبْتَدَأٌ.", "«and whoever»", "«ve kim»", segments=wa_("مَنْ", "man-shartiyya", "pron")),
  mazi("كَفَرَ", "kafara", "«is ungrateful»", "«nankörlük ederse»", tags=[SH], hidden="هُوَ", extra_ar=" — فِعْلُ الشَّرْطِ"),
  tok("فَإِنَّ", "inna", "part", ["fa-khabar-mubtada", SH, IW], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«then indeed» — the fāʾ of the answer with inna.", "«o takdirde şüphesiz» — cevap fâ'sı ve inne.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")]),
  noun_pron("رَبِّي", "rabb", "رَبِّ", "ي", "pron-1s", "اسْمُ إِنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — inna's ism.", "«Rabbim» — inne'nin ismi.", tags=[IW, ID, "ya-al-mutakallim"]),
  khabar_inna("غَنِيٌّ", "ghani", "«rich»", "«zengindir»"),
  naat("كَرِيمٌ", "karim", "«generous»", "«kerimdir»", case="raf", tags=["sifa-mushabbaha"], punct="."),
  ]),
])
sen("s6", "«He said: Disguise her throne for her; we shall see whether she is guided or is of those who are not guided» (27:41).",
        "«Dedi ki: Tahtını onun için tanınmaz hâle getirin; bakalım tanıyacak mı, yoksa tanımayanlardan mı olacak» (27:41).", [
  *quran([
  qala(hidden="هُوَ", punct=None),
  tok("نَكِّرُوا", "nakkara", "verb", [AM, MB, "form-ii-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«disguise» — an imperative on the dropped nūn.", "«tanınmaz hâle getirin» — nûnun düşmesi üzere mebnî emir."),
  li_pron("لَهَا", "هَا", "pron-3fs", "«for her»", "«onun için»"),
  noun_pron("عَرْشَهَا", "arsh", "عَرْشَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her throne»", "«tahtını»", tags=[MB, ID]),
  tok("نَنْظُرْ", "nazara", "verb", ["jawab-al-talab", MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«we shall see» — jazm as the answer of the command.", "«bakalım» — talebin cevabı olarak meczum."),
  tok("أَتَهْتَدِي", "ihtada", "verb", [IS, MB, "mudari-marfu", "form-viii-verbs", "naqis-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتَهْتَدِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ مَفْعُولُ نَنْظُرْ.", "«whether she is guided» — the clause is the object of «see».", "«tanıyacak mı» — cümle «bakalım»ın mef'ûlü.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَهْتَدِي", "ihtada", "verb")]),
  tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ.", "«or»", "«yoksa»"),
  tok("تَكُونُ", "kana", "verb", [AT, KN, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«she is»", "«olacak»"),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ تَكُونُ."),
  tok("الَّذِينَ", "alladhina", "pron", [HJ, KN, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«those who»", "«… -anlar»"),
  la_nafiya(),
  khamsa("يَهْتَدُونَ", "ihtada", "«are not guided»", "«tanımazlar»", tags=[MW, "la-nafiya", "form-viii-verbs", "naqis-verbs"], extra_ar=" — صِلَةٌ", punct="."),
  ]),
])
sen("s7", "«When she came it was said: Is your throne like this? She said: It is as though it were it. And we were given knowledge before her, and we were Muslims» (27:42).",
        "«O gelince denildi ki: Senin tahtın böyle mi? Dedi ki: Sanki odur. Bize ondan önce ilim verilmişti ve biz Müslüman olmuştuk» (27:42).", [
  *quran([
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… -ınca»", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi_ta("جَاءَتْ", "jaa", "«she came»", "«geldi»", tags=[SH, "hollow-verbs"]),
  tok("قِيلَ", "qala", "verb", [SH, NF, "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ بَعْدَهُ — جَوَابُ لَمَّا.", "«it was said» — a passive; the clause after it stands as the deputy doer.", "«denildi» — meçhul; sonraki cümle nâib-i fâil."),
  tok("أَهٰكَذَا", "hakadha", "part", [IS, MK, "asma-al-ishara"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْكَافُ حَرْفُ جَرٍّ، وَذَا اسْمُ إِشَارَةٍ — خَبَرٌ مُقَدَّمٌ.", "«like this?» — the hamza of question; the kāf with the demonstrative, a fronted khabar.", "«böyle mi?» — soru hemzesi; kâf ve ism-i işâret, öne alınmış haber.", segments=[seg("أَ", "hamza-istifham", "part"), seg("هٰكَذَا", "hakadha", "part")]),
  noun_pron("عَرْشُكِ", "arsh", "عَرْشُ", "كِ", "pron-2fs", "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your throne» — the delayed mubtadaʾ.", "«senin tahtın» — mübtedâ.", tags=[MK, ID]),
  qalat(),
  tok("كَأَنَّهُ", "kaanna", "part", [IW], "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ، وَالْهَاءُ اسْمُهَا.", "«it is as though it» — kaʾanna with the hāʾ as its ism.", "«sanki o» — keenne; hâ ismi.", segments=[seg("كَأَنَّ", "kaanna", "part"), pr3ms()]),
  tok("هُوَ", "huwa", "pron", [IW], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ خَبَرُ كَأَنَّ.", "«were it» — kaʾanna's khabar.", "«odur» — keenne'nin haberi."),
  tok("وَأُوتِينَا", "aataa", "verb", [AT, NF, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأُوتِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَا نَائِبُ فَاعِلٍ.", "«and we were given» — a passive; nā the deputy doer.", "«ve bize verildi» — meçhul; nâ nâib-i fâil.", segments=[seg("وَ", "wa", "conj"), seg("أُوتِي", "aataa", "verb"), seg("نَا", "pron-1p", "pron")]),
  maful_("الْعِلْمَ", "ilm", "«knowledge»", "«ilim»", ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ (الْأَوَّلُ نَائِبُ الْفَاعِلِ)."),
  prep("مِنْ", "min", "«before» (lit. from)", "«-den»"),
  noun_pron("قَبْلِهَا", "qabla", "قَبْلِ", "هَا", "pron-3fs", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«before her»", "«ondan önce»", tags=[HJ, ID]),
  tok("وَكُنَّا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهُ.", "«and we were»", "«ve biz … idik»", segments=[seg("وَ", "wa", "conj"), seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("مُسْلِمِينَ", "muslim", "noun", [KN, JS, "ism-fail", "form-iv-verbs"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«Muslims» — kāna's khabar.", "«Müslümanlar» — kâne'nin haberi.", punct="."),
  ]),
])
sen("s8", "«And what she had been worshipping besides God had barred her; she was of a disbelieving people» (27:43).",
        "«Allah'ı bırakıp taptığı şey onu alıkoymuştu; o, kâfir bir kavimdendi» (27:43).", [
  *quran([
  tok("وَصَدَّهَا", "sadda", "verb", [AT, MB, "doubled-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَصَدَّ فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«and had barred her» — hā the object, before the doer.", "«ve onu alıkoymuştu» — hâ mef'ûl, fâilden önce.", segments=[seg("وَ", "wa", "conj"), seg("صَدَّ", "sadda", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("مَا", "ma-mawsula", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«what» — the relative, the doer.", "«… şey» — ism-i mevsûl, fâil."),
  tok("كَانَتْ", "kana", "verb", [MW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — صِلَةٌ.", "«she had been» — kāna; the ṣila.", "«idi» — kâne; sıla."),
  mudari("تَعْبُدُ", "abada", "«worshipping»", "«taptığı»", tags=[KN], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَتْ"),
  prep("مِنْ", "min", "«besides»", "«… bırakıp»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«besides»", "«başka»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»"),
  tok("إِنَّهَا", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا.", "«she» (lit. indeed she)", "«şüphesiz o»", segments=[seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("كَانَتْ", "kana", "verb", [IW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«was» — kāna; the clause is inna's khabar.", "«idi» — kâne; cümle inne'nin haberi."),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَتْ."),
  majrur("قَوْمٍ", "qawm", "«a people»", "«bir kavim»"),
  tok("كَافِرِينَ", "kafir", "noun", [NA, JS, "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«disbelieving» — the naʿt, jarr by the yāʾ.", "«kâfir» — sıfat, yâ ile mecrûr.", punct="."),
  ]),
])
sen("s9", "«It was said to her: Enter the palace. When she saw it she took it for a pool and bared her legs. He said: It is a palace paved with glass» (27:44).",
        "«Ona: Saraya gir, denildi. Onu görünce derin bir su sandı ve bacaklarını açtı. Dedi ki: O, camdan döşenmiş bir saraydır» (27:44).", [
  *quran([
  tok("قِيلَ", "qala", "verb", [NF, "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ بَعْدَهُ.", "«it was said» — a passive.", "«denildi» — meçhul."),
  li_pron("لَهَا", "هَا", "pron-3fs", "«to her»", "«ona»"),
  tok("ادْخُلِي", "dakhala", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ.", "«enter» — an imperative on the dropped nūn; the yāʾ of address is the doer.", "«gir» — nûnun düşmesi üzere mebnî emir; muhâtaba yâ'sı fâil."),
  maful_("الصَّرْحَ", "sarh", "«the palace»", "«saraya»"),
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… -ınca»", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  tok("رَأَتْهُ", "raa", "verb", [SH, MB, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ بِهِ — حُذِفَتْ أَلِفُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«she saw it» — the hāʾ the object; the alif drops before the tāʾ.", "«onu gördü» — hâ mef'ûl; elifi düşmüş.", segments=[seg("رَأَتْ", "raa", "verb"), pr3ms()]),
  tok("حَسِبَتْهُ", "hasiba", "verb", [SH, MX, "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ — جَوَابُ لَمَّا.", "«she took it for» — the hāʾ the first object; the answer of lammā.", "«onu … sandı» — hâ ilk mef'ûl; lemmâ'nın cevabı.", segments=[seg("حَسِبَتْ", "hasiba", "verb"), pr3ms()]),
  tok("لُجَّةً", "lujja", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a pool» — the second object.", "«derin bir su» — ikinci mef'ûl."),
  mazi_ta("وَكَشَفَتْ", "kashafa", "«and bared»", "«ve açtı»", tags=[AT], wa=True),
  prep("عَنْ", "an", "«(bared) …»", "«-i»"),
  noun_pron("سَاقَيْهَا", "saq", "سَاقَيْ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَهَا مُضَافٌ إِلَيْهِ.", "«her two legs»", "«iki bacağını»", tags=[HJ, ID, "al-muthanna"]),
  qala(hidden="هُوَ", punct=None),
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«it is»", "«o»", segments=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  khabar_inna("صَرْحٌ", "sarh", "«a palace»", "«bir saray»"),
  naat("مُمَرَّدٌ", "mumarrad", "«paved»", "«döşenmiş»", case="raf", tags=["ism-maful", "form-ii-verbs"]),
  prep("مِنْ", "min", "«with»", "«-den»"),
  tok("قَوَارِيرَ", "qarura", "noun", [HJ, JT, MM], "مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«glass»", "«cam»", punct="."),
  ]),
])
sen("s10", "«She said: My Lord, I have wronged myself, and I submit with Sulaymān to God, the Lord of the worlds» (27:44).",
        "«Dedi ki: Rabbim, ben nefsime zulmettim; Süleyman ile birlikte âlemlerin Rabbi Allah'a teslim oldum» (27:44).", [
  *quran([
  qalat(),
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID, "ya-al-mutakallim"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، حُذِفَ حَرْفُ النِّدَاءِ.", "«my Lord» — a munādā annexed to the dropped yāʾ.", "«Rabbim» — hazfedilmiş yâ'ya muzâf münâdâ."),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«şüphesiz ben»", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("ظَلَمْتُ", "zalama", "verb", [IW, MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — خَبَرُ إِنَّ.", "«I have wronged»", "«zulmettim»", segments=[seg("ظَلَمْ", "zalama", "verb"), seg("تُ", "pron-1s", "pron")]),
  noun_pron("نَفْسِي", "nafs", "نَفْسِ", "ي", "pron-1s", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«myself»", "«nefsime»", tags=[MB, ID, "ya-al-mutakallim"]),
  tok("وَأَسْلَمْتُ", "aslama", "verb", [AT, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَسْلَمْ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I submit»", "«ve teslim oldum»", segments=[seg("وَ", "wa", "conj"), seg("أَسْلَمْ", "aslama", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile birlikte»"),
  tok("سُلَيْمَانَ", "sulayman", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān»", "«Süleyman»"),
  tok("لِلّٰهِ", "allah", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«to God»", "«Allah'a»", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("رَبِّ", "rabb", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَجْرُورٌ، مُضَافٌ.", "«the Lord [of]»", "«Rabbi»"),
  tok("الْعَالَمِينَ", "alamin", "noun", [ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«of the worlds»", "«âlemlerin»", punct="."),
  ]),
])
sen("s11", "This is the prophet of God Sulaymān; you have seen his stances in calling to God and to His oneness, his wisdom, his fine judgment and his zeal for his religion and his creed.",
        "İşte Allah'ın peygamberi Süleyman: onun Allah'a ve tevhide davetteki duruşlarını, hikmetini, fıkhını, dini ve akidesi uğrundaki gayretini gördünüz.", [
  tok("وَهٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — the mubtadaʾ.", "«ve işte bu» — mübtedâ.", segments=wa_("هٰذَا", "hadha", "pron")),
  tok("نَبِيُّ", "nabi", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the prophet [of]» — the khabar, annexed.", "«peygamberi» — haber, muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("سُلَيْمَانُ", "sulayman", "propn", [BD, MM], "بَدَلٌ مِنْ نَبِيُّ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«Sulaymān» — the badal.", "«Süleyman» — bedel.", punct="،"),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=wa_("قَدْ", "qad", "part")),
  tok("رَأَيْتُمْ", "raa", "verb", [MB, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ.", "«you have seen» — the tāʾ the doer, the mīm of the plural.", "«gördünüz» — tâ fâil, mîm cemaat için.", segments=[seg("رَأَيْ", "raa", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  noun_pron("مَوَاقِفَهُ", "mawqif", "مَوَاقِفَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his stances»", "«duruşlarını»", tags=[MB, ID, JT]),
  fi(), majrur("الدَّعْوَةِ", "dawa", "«calling»", "«davette»", tags=["masdar"]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'a»"),
  tok("وَإِلَى", "ila", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَإِلَى حَرْفُ جَرٍّ.", "«and to»", "«ve … -e»", segments=wa_("إِلَى", "ila", "prep")),
  majrur("التَّوْحِيدِ", "tawhid", "«His oneness»", "«tevhide»", tags=["masdar"], punct="،"),
  noun_pron("وَحِكْمَتَهُ", "hikma", "وَحِكْمَتَ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَحِكْمَتَ مَعْطُوفٌ عَلَى مَوَاقِفَ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his wisdom»", "«ve hikmetini»", tags=[AT, ID]),
  noun_pron("وَفِقْهَهُ", "fiqh", "وَفِقْهَ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَفِقْهَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his judgment»", "«ve fıkhını»", tags=[AT, ID]),
  noun_pron("وَغَيْرَتَهُ", "ghayra", "وَغَيْرَتَ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَغَيْرَتَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his zeal»", "«ve gayretini»", tags=[AT, ID]),
  prep("عَلَى", "ala", "«for»", "«uğrunda»"),
  noun_pron("دِينِهِ", "din", "دِينِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his religion»", "«dini»", tags=[HJ, ID]),
  noun_pron("وَعَقِيدَتِهِ", "aqida", "وَعَقِيدَتِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَعَقِيدَتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his creed»", "«ve akidesi»", punct=".", tags=[AT, ID]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: ifrit, tarf, lujja, nakkara, qibal, saghir-abased, bima are the new keys; mustaqarr / bala-test / kaanna reused)
CAND = {
 "rajaa": G("rajaa", "رَجَعَ", "ر ج ع", "verb", "to return, to go back", "dönmek", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come; to bring", "gelmek; getirmek", 1),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer / of ibtidāʾ", "kasem cevabının lâmı / ibtidâ lâmı", 2),
 "nun-tawkid": G("nun-tawkid", "نَّ (نُونُ التَّوْكِيدِ)", None, "part", "the heavy nūn of emphasis", "şeddeli te'kid nûnu", 2),
 "jund": G("jund", "جُنْد", "ج ن د", "noun", "a host", "ordu", 2, plural="جُنُود"),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "not; no (the lā of absolute negation)", "değil; hiç (cinsi nefyeden lâ)", 1),
 "qibal": G("qibal", "قِبَل", "ق ب ل", "noun", "power to face, strength against (Qurʾānic: لَا قِبَلَ لَهُمْ بِهَا)", "karşı koyma gücü (Kur'ânî)", 3),
 "akhraja": G("akhraja", "أَخْرَجَ", "خ ر ج", "verb", "to drive out (Form IV)", "çıkarmak (if'âl)", 1),
 "dhalil": G("dhalil", "ذَلِيل", "ذ ل ل", "noun", "abased", "zelil", 2),
 "hum": G("hum", "هُمْ", None, "pron", "they", "onlar", 1),
 "saghir-abased": G("saghir-abased", "صَاغِر", "ص غ ر", "noun", "humbled, abased (an active participle)", "küçük düşmüş, zelil (ism-i fâil)", 3),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O", "ey", 1),
 "ayyuha": G("ayyuha", "أَيُّ", None, "noun", "O you", "ey", 2),
 "mala-chiefs": G("mala-chiefs", "مَلَأ", "م ل أ", "noun", "the chiefs", "ileri gelenler", 2),
 "ayy": G("ayy", "أَيّ", None, "noun", "which? — the question-word, annexed", "hangi? — soru ismi, muzâf", 1),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection", "vikâye nûnu", 2),
 "arsh": G("arsh", "عَرْش", "ع ر ش", "noun", "a throne", "taht", 1),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "önce", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that", "… -mesi", 1),
 "muslim": G("muslim", "مُسْلِم", "س ل م", "noun", "a Muslim", "Müslüman", 1),
 "ifrit": G("ifrit", "عِفْرِيت", "ع ف ر", "noun", "an ʿifrīt, a mighty jinn", "ifrit, güçlü cin", 3),
 "jinn": G("jinn", "جِنّ", "ج ن ن", "noun", "the jinn", "cinler", 1),
 "ana": G("ana", "أَنَا", None, "pron", "I", "ben", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to rise, to stand", "kalkmak", 1),
 "maqam": G("maqam", "مَقَام", "ق و م", "noun", "a seat, a place of standing", "makam, yer", 2),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1),
 "amin": G("amin", "أَمِين", "أ م ن", "noun", "trustworthy", "güvenilir", 1),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "the one who", "… olan", 1),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "with, at", "yanında", 1),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "the Book; a letter", "kitap; mektup", 1),
 "irtadda": G("irtadda", "اِرْتَدَّ", "ر د د", "verb", "to return, to turn back (Form VIII, doubled)", "dönmek, geri gelmek (iftiâl, muzâaf)", 3),
 "tarf": G("tarf", "طَرْف", "ط ر ف", "noun", "a glance, the eye", "göz kırpışı, bakış", 3),
 "lamma": G("lamma", "لَمَّا", None, "part", "when", "… -ınca", 2),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "mustaqarr": G("mustaqarr", "مُسْتَقِرّ", "ق ر ر", "noun", "set, settled (the participle of Form X)", "yerleşmiş, karar kılmış (istif'âl ism-i fâili)", 3),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "fadl": G("fadl", "فَضْل", "ف ض ل", "noun", "favour", "lütuf", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "bala-test": G("bala-test", "بَلَا", "ب ل و", "verb", "to test, to try", "sınamak", 2),
 "hamza-istifham": G("hamza-istifham", "أَ (هَمْزَةُ الِاسْتِفْهَامِ)", None, "part", "the hamza of question", "soru hemzesi", 1),
 "shakara": G("shakara", "شَكَرَ", "ش ك ر", "verb", "to give thanks", "şükretmek", 1),
 "am": G("am", "أَمْ", None, "part", "or", "yoksa", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to be ungrateful; to disbelieve", "nankörlük etmek; inkâr etmek", 1),
 "man-shartiyya": G("man-shartiyya", "مَنْ (الشَّرْطِيَّة)", None, "pron", "whoever", "kim … -se", 2),
 "innama": G("innama", "إِنَّمَا", None, "part", "only", "ancak", 2),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "self, soul", "nefis", 1),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich, self-sufficient", "zengin, müstağni", 1),
 "karim": G("karim", "كَرِيم", "ك ر م", "noun", "generous", "kerim", 1),
 "nakkara": G("nakkara", "نَكَّرَ", "ن ك ر", "verb", "to disguise, to make unrecognisable (Form II)", "tanınmaz hâle getirmek (tef'îl)", 3),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look, to see", "bakmak", 1),
 "ihtada": G("ihtada", "اِهْتَدَى", "ه د ي", "verb", "to be guided; to recognise", "hidayet bulmak; tanımak", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "those who", "… -anlar", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "hakadha": G("hakadha", "هٰكَذَا", None, "part", "like this", "böyle", 1),
 "pron-2fs": G("pron-2fs", "كِ", None, "pron", "you / your (fem. singular)", "sen / senin (müennes)", 1),
 "kaanna": G("kaanna", "كَأَنَّ", None, "part", "as though — a sister of inna", "sanki — inne'nin kardeşi", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give", "vermek", 2),
 "sadda": G("sadda", "صَدَّ", "ص د د", "verb", "to bar", "alıkoymak", 2),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "tapmak", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "besides", "başka", 2),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people", "kavim", 1),
 "kafir": G("kafir", "كَافِر", "ك ف ر", "noun", "a disbeliever", "kâfir", 1),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "sarh": G("sarh", "صَرْح", "ص ر ح", "noun", "a palace", "saray", 3),
 "hasiba": G("hasiba", "حَسِبَ", "ح س ب", "verb", "to take for, to suppose", "sanmak", 2),
 "lujja": G("lujja", "لُجَّة", "ل ج ج", "noun", "a deep pool, the deep of the sea", "derin su, engin", 3),
 "kashafa": G("kashafa", "كَشَفَ", "ك ش ف", "verb", "to bare", "açmak", 1),
 "saq": G("saq", "سَاق", "س و ق", "noun", "a leg", "bacak", 2),
 "mumarrad": G("mumarrad", "مُمَرَّد", "م ر د", "noun", "paved", "döşenmiş", 3),
 "qarura": G("qarura", "قَارُورَة", "ق ر ر", "noun", "a glass vessel", "sırça", 3),
 "zalama": G("zalama", "ظَلَمَ", "ظ ل م", "verb", "to wrong", "zulmetmek", 1),
 "aslama": G("aslama", "أَسْلَمَ", "س ل م", "verb", "to submit", "teslim olmak", 1),
 "maa": G("maa", "مَعَ", None, "noun", "with", "ile", 1),
 "sulayman": G("sulayman", "سُلَيْمَان", None, "propn", "Sulaymān", "Süleyman", 1),
 "alamin": G("alamin", "عَالَمِين", "ع ل م", "noun", "the worlds", "âlemler", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed", "gerçekten", 1),
 "mawqif": G("mawqif", "مَوْقِف", "و ق ف", "noun", "a stance, a position", "duruş, tavır", 2, plural="مَوَاقِف"),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "the call", "davet", 1),
 "tawhid": G("tawhid", "تَوْحِيد", "و ح د", "noun", "the affirmation of God's oneness", "tevhid", 1),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "fiqh": G("fiqh", "فِقْه", "ف ق ه", "noun", "fine judgment, understanding", "fıkıh", 2),
 "ghayra": G("ghayra", "غَيْرَة", "غ ي ر", "noun", "zeal, jealous honour", "gayret, izzet", 3),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "aqida": G("aqida", "عَقِيدَة", "ع ق د", "noun", "a creed", "akide", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my", "beni / benim", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you (attached)", "sen (bitişik)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we", "biz", 1),
 "pron-2mp": G("pron-2mp", "كُمْ", None, "pron", "you (plural)", "siz", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "nakkara", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَكَّر", "نَكِّر", "نَكِّر", "تَنْكِير", "مُنَكِّر", "مُنَكَّر", "نُكِّرَ", "يُنَكَّرُ", "نَكَّرَ الشَّيْءَ: غَيَّرَهُ حَتَّى لَا يُعْرَفَ."))
put_morph(mo, "irtadda", _sg.entry(_sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِرْتِدَاد", "مُرْتَدّ", _sg.mazi14("اِرْتَدّ", "اِرْتَدَد"), _sg.mudari14("َ", "رْتَدّ", "رْتَدِد"), ["اِرْتَدَّ", "اِرْتَدَّا", "اِرْتَدُّوا", "اِرْتَدِّي", "اِرْتَدَّا", "اِرْتَدِدْنَ"], "يَرْتَدَّ", "يَرْتَدَّ", "تَرْتَدَّ", None, None, None, "اِرْتَدَّ: رَجَعَ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَرْتَدَّ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch15 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 15 (print pp. 23–24, §14 part 3): the Qurʾān's telling, 27:37–44 — the throne brought in a glance, the test, the glass palace and the queen's submission (s1–s10); the story's closing line (s11). END of the story of Dāwūd and Sulaymān."
ADD_TR = " On beşinci bölüm (baskı s. 23–24, 14. kısım 3. parça): Kur'ân'ın anlatımı, 27:37–44 — göz açıp kapayıncaya kadar getirilen taht, sınama, cam saray ve kraliçenin teslimiyeti (s1–s10); kıssanın kapanış cümlesi (s11). Dâvûd ve Süleyman kıssasının SONU."
write_out(15, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §14 (27:37–44) + close", GLOSS_ADD, notes=(), related=())
report(15, S, GLOSS_ADD, ())
