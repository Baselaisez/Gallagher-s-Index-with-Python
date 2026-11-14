# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 13: «الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ (١)» — §14, the Qurʾānic telling, 27:20–28:
the missing hoopoe, its report, and Sulaymān's letter; print pp. 22–23. The Qurʾānic text is given as the book prints it.
python3 tools/authoring/author_qisas4_ch13.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ (١)", "en": "The Qurʾān tells Sulaymān's story (1)", "tr": "Kur'ân Süleyman'ın kıssasını anlatır (1)"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; NT = "nun-tawkid"; TW = "tawkid"; LJN = "la-nafiya-lil-jins"; IS = "al-istifham"
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

sen("s1", "«And he inspected the birds and said: Why do I not see the hoopoe — or is he among the absent?» (27:20).",
        "«Kuşları yokladı ve dedi ki: Neden Hüdhüd'ü görmüyorum, yoksa kayıplardan mı oldu?» (27:20).", [
  *quran([
  mazi("وَتَفَقَّدَ", "tafaqqada", "«and he inspected»", "«ve yokladı»", tags=[MB, "form-v-verbs"], wa=True, hidden="هُوَ"),
  maful_("الطَّيْرَ", "tayr", "«the birds»", "«kuşları»"),
  qala(full="فَقَالَ", wa=False, hidden="هُوَ", punct=None, tags=[AT]),
  tok("مَا", "ma-istifham", "pron", [IS, MK], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the question-mā, the mubtadaʾ.", "«ne» — soru mâ'sı, mübtedâ."),
  tok("لِيَ", "li", "prep", [HJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ فِي مَحَلِّ جَرٍّ (فُتِحَتْ) — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ: مَا لِي.", "«(is it) with me» — the jarr phrase is the khabar: «why is it with me».", "«bana ne oluyor» — câr-mecrûr haber.", segments=[seg("لِ", "li", "prep"), seg("يَ", "pron-1s", "pron")]),
  la_nafiya(),
  neg_mudari("أَرَى", "raa", "«I see»", "«görüyorum»", tags=[HL, MB, "naqis-verbs"], hidden="أَنَا", extra=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْجُمْلَةُ حَالٌ"),
  maful_("الْهُدْهُدَ", "hudhud", "«the hoopoe»", "«Hüdhüd'ü»"),
  tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ — أَمِ الْمُنْقَطِعَةُ بِمَعْنَى بَلْ وَالْهَمْزَةِ.", "«or» — the disjunctive am, «nay, is he…».", "«yoksa» — munkatıa em."),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«he is» — kāna; its ism concealed.", "«oldu» — kâne; ismi gizli."),
  prep("مِنَ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  tok("الْغَائِبِينَ", "ghaib", "noun", [HJ, KN, JS, "ism-fail"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the absent» — jarr by the yāʾ.", "«kayıplar» — yâ ile mecrûr.", punct="."),
  ]),
])
sen("s2", "«I shall surely punish him with a severe punishment, or slaughter him, unless he brings me a clear warrant» (27:21).",
        "«Ona şiddetli bir azapla azap edeceğim ya da onu keseceğim; yahut bana apaçık bir delil getirecek» (27:21).", [
  *quran([
  tok("لَأُعَذِّبَنَّهُ", "adhdhaba", "verb", [TW, NT, MB, "form-ii-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَأُعَذِّبَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I shall surely punish him» — the lām of the oath's answer; built on fatḥa before the heavy nūn of emphasis; the hāʾ the object.", "«ona mutlaka azap edeceğim» — kasem cevabının lâmı; şeddeli te'kid nûnu ile fetha üzere mebnî; hâ mef'ûl.", segments=[seg("لَ", "lam-qasam", "part"), seg("أُعَذِّبَ", "adhdhaba", "verb"), seg("نَّ", "nun-tawkid", "part"), pr3ms()]),
  tok("عَذَابًا", "adhab", "noun", ["maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a punishment» — the absolute object.", "«bir azapla» — mef'ûl-i mutlak."),
  naat("شَدِيدًا", "shadid", "«severe»", "«şiddetli»", case="nasb", tags=["sifa-mushabbaha"]),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ.", "«or»", "«ya da»"),
  tok("لَأَذْبَحَنَّهُ", "dhabaha", "verb", [AT, TW, NT, MB], "اللَّامُ لِلْقَسَمِ، وَأَذْبَحَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْهَاءُ مَفْعُولٌ بِهِ — مَعْطُوفٌ.", "«or slaughter him» — joined; the same oath-lām and heavy nūn.", "«ya da onu keseceğim» — ma'tûf; aynı kasem lâmı ve te'kid nûnu.", segments=[seg("لَ", "lam-qasam", "part"), seg("أَذْبَحَ", "dhabaha", "verb"), seg("نَّ", "nun-tawkid", "part"), pr3ms()]),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ بِمَعْنَى إِلَّا أَنْ.", "«unless» (lit. or)", "«yahut»"),
  tok("لَيَأْتِيَنِّي", "ata", "verb", [AT, TW, NT, MB, "naqis-verbs"], "اللَّامُ لِلْقَسَمِ، وَيَأْتِيَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — أُدْغِمَتْ نُونُ التَّوْكِيدِ فِي نُونِ الْوِقَايَةِ.", "«he brings me» — the oath-lām and the nūn of emphasis; the nūn of protection fused; the yāʾ the object.", "«bana getirecek» — kasem lâmı ve te'kid nûnu; vikâye nûnu ile idgam; yâ mef'ûl.", segments=[seg("لَ", "lam-qasam", "part"), seg("يَأْتِيَ", "ata", "verb"), seg("نِّ", "nun-tawkid", "part"), seg("ي", "pron-1s", "pron")]),
  tok("بِسُلْطَانٍ", "sultan", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَسُلْطَانٍ مَجْرُورٌ.", "«a warrant»", "«bir delil»", segments=[seg("بِ", "bi", "prep"), seg("سُلْطَانٍ", "sultan", "noun")]),
  naat("مُبِينٍ", "mubin", "«clear»", "«apaçık»", tags=["ism-fail", "form-iv-verbs"], punct="."),
  ]),
])
sen("s3", "«But he stayed not long, and said: I have grasped what you have not grasped, and I have come to you from Sabaʾ with sure tidings» (27:22).",
        "«Çok geçmeden geldi ve dedi ki: Senin kavrayamadığını kavradım; sana Sebe'den kesin bir haber getirdim» (27:22).", [
  *quran([
  tok("فَمَكَثَ", "makatha", "verb", [AT], "الْفَاءُ عَاطِفَةٌ، وَمَكَثَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«but he stayed»", "«çok geçmeden»", segments=[seg("فَ", "fa", "conj"), seg("مَكَثَ", "makatha", "verb")]),
  tok("غَيْرَ", "ghayr", "noun", [MF, ID], "نَائِبٌ عَنِ الظَّرْفِ مَنْصُوبٌ (زَمَانًا غَيْرَ بَعِيدٍ)، مُضَافٌ.", "«not (long)» — standing for a ẓarf of time; annexed.", "«… olmayan (bir süre)» — zarf yerine; muzâf."),
  mudaf_ilayh("بَعِيدٍ", "baid", "«long» (lit. far)", "«uzun»", tags=["sifa-mushabbaha"]),
  qala(full="فَقَالَ", wa=False, hidden="هُوَ", punct=None, tags=[AT]),
  tok("أَحَطْتُ", "ahata", "verb", [HJ, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — أَجْوَفُ حُذِفَتْ أَلِفُهُ.", "«I have grasped» — the tāʾ the doer; a hollow IV whose alif drops.", "«kavradım» — tâ fâil; ecvef if'âl, elifi düşmüş.", segments=[seg("أَحَطْ", "ahata", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِمَا", "bi", "prep", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«… -ını»", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("لَمْ", "lam-jazima", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-medin»"),
  tok("تُحِطْ", "ahata", "verb", [LJ, MW, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ يَاؤُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — صِلَةٌ.", "«you have grasped» — jazm by lam; the hollow's yāʾ drops.", "«kavrayamadın» — lem ile meczum; ecvefin yâ'sı düşmüş."),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«it»", "«onu»"),
  tok("وَجِئْتُكَ", "jaa", "verb", [AT, MB, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَجِئْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«and I have come to you»", "«ve sana geldim»", segments=[seg("وَ", "wa", "conj"), seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("كَ", "pron-2ms", "pron")]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("سَبَإٍ", "saba", "«Sabaʾ»", "«Sebe'»"),
  tok("بِنَبَإٍ", "naba-news", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَنَبَإٍ مَجْرُورٌ.", "«with tidings»", "«bir haberle»", segments=[seg("بِ", "bi", "prep"), seg("نَبَإٍ", "naba-news", "noun")]),
  naat("يَقِينٍ", "yaqin", "«sure»", "«kesin»", punct="."),
  ]),
])
sen("s4", "«I found a woman ruling them; she has been given of everything, and she has a mighty throne» (27:23).",
        "«Onlara hükmeden bir kadın buldum; kendisine her şeyden verilmiş ve onun büyük bir tahtı var» (27:23).", [
  *quran([
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«şüphesiz ben»", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("وَجَدْتُ", "wajada", "verb", [IW, MB, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I found» — the tāʾ the doer; the clause is inna's khabar.", "«buldum» — tâ fâil; cümle inne'nin haberi.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("تُ", "pron-1s", "pron")]),
  maful_("امْرَأَةً", "imraa", "«a woman»", "«bir kadın»"),
  tok("تَمْلِكُهُمْ", "malaka", "verb", ["jumla-sifa", "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ لِامْرَأَةً.", "«ruling them» — a naʿt clause; hum the object.", "«onlara hükmeden» — sıfat cümlesi; hüm mef'ûl.", segments=[seg("تَمْلِكُ", "malaka", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("وَأُوتِيَتْ", "aataa", "verb", [AT, NF, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُوتِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«and she has been given» — a passive; the deputy doer concealed.", "«ve ona verilmiş» — meçhul; nâib-i fâil gizli.", segments=wa_("أُوتِيَتْ", "aataa", "verb")),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şey»"),
  tok("وَلَهَا", "li", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and she has» — a fronted khabar.", "«ve onun … var» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "li", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("عَرْشٌ", "arsh", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a throne» — the delayed mubtadaʾ.", "«bir taht» — mübtedâ."),
  naat("عَظِيمٌ", "azim", "«mighty»", "«büyük»", case="raf", tags=["sifa-mushabbaha"], punct="."),
  ]),
])
sen("s5", "«I found her and her people prostrating to the sun instead of God; Satan has made their deeds fair to them and barred them from the way, so they are not guided» (27:24).",
        "«Onu ve kavmini Allah'ı bırakıp güneşe secde eder buldum; şeytan onlara amellerini süslemiş ve onları yoldan alıkoymuş; bu yüzden doğru yolu bulamıyorlar» (27:24).", [
  *quran([
  tok("وَجَدْتُهَا", "wajada", "verb", [MX, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ أَوَّلُ.", "«I found her» — hā the first object.", "«onu buldum» — hâ ilk mef'ûl.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("تُ", "pron-1s", "pron"), seg("هَا", "pron-3fs", "pron")]),
  noun_pron("وَقَوْمَهَا", "qawm", "وَقَوْمَ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَقَوْمَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her people»", "«ve kavmini»", tags=[AT, ID]),
  khamsa("يَسْجُدُونَ", "sajada", "«prostrating»", "«secde eder»", tags=[MX, HL], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ (أَوْ حَالٌ)"),
  tok("لِلشَّمْسِ", "shams", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالشَّمْسِ مَجْرُورٌ.", "«to the sun»", "«güneşe»", segments=[seg("لِ", "li", "prep"), seg("الشَّمْسِ", "shams", "noun")]),
  prep("مِنْ", "min", "«instead»", "«… bırakıp»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«besides»", "«başka»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»"),
  mazi("وَزَيَّنَ", "zayyana", "«and has made fair»", "«ve süslemiş»", tags=[AT, MB, "form-ii-verbs"], wa=True, hidden=None),
  li_pron("لَهُمُ", "هُمُ", "pron-3mp", "«to them»", "«onlara»", extra="، ضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الشَّيْطَانُ", "shaytan", "«Satan»", "«şeytan»"),
  noun_pron("أَعْمَالَهُمْ", "amal-work", "أَعْمَالَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their deeds»", "«amellerini»", tags=[MB, ID, JT]),
  tok("فَصَدَّهُمْ", "sadda", "verb", [AT, MB, "doubled-verbs"], "الْفَاءُ عَاطِفَةٌ، وَصَدَّ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«and barred them» — hum the object.", "«ve onları alıkoymuş» — hüm mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("صَدَّ", "sadda", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("عَنِ", "an", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("السَّبِيلِ", "sabil", "«the way»", "«yoldan»"),
  tok("فَهُمْ", "hum", "pron", [AT, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«so they» — the mubtadaʾ.", "«bu yüzden onlar» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("هُمْ", "hum", "pron")]),
  la_nafiya(),
  khamsa("يَهْتَدُونَ", "ihtada", "«are guided»", "«doğru yolu bulurlar»", tags=[MK, "la-nafiya", "form-viii-verbs", "naqis-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرٌ", punct="."),
  ]),
])
sen("s6", "«— that they should not prostrate to God, who brings forth what is hidden in the heavens and the earth, and knows what you conceal and what you declare» (27:25).",
        "«— Göklerde ve yerde gizli olanı çıkaran, sizin gizlediğinizi de açığa vurduğunuzu da bilen Allah'a secde etmesinler diye» (27:25).", [
  *quran([
  tok("أَلَّا", "an-masdariyya", "part", [AN, "la-nafiya"], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَلَا نَافِيَةٌ، أُدْغِمَتِ النُّونُ فِي اللَّامِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ لِأَجْلِهِ (أَوْ بَدَلٌ مِنْ أَعْمَالَهُمْ).", "«that … not» — an fused with lā; the clause is an object of purpose.", "«… -mesinler diye» — en ile nefiy lâ'sı birleşmiş; cümle mef'ûlün leh.", segments=[seg("أَ", "an-masdariyya", "part"), seg("لَّا", "la-nafiya", "part")]),
  tok("يَسْجُدُوا", "sajada", "verb", [AN, AK], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«they should prostrate» — naṣb by the dropped nūn; the wāw the doer.", "«secde etsinler» — nûnun düşmesiyle mansub; vâv fâil."),
  tok("لِلّٰهِ", "allah", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«to God»", "«Allah'a»", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلَفْظِ الْجَلَالَةِ.", "«who» — a naʿt of the Name.", "«… olan» — lafza-i celâlin sıfatı."),
  mudari("يُخْرِجُ", "akhraja", "«brings forth»", "«çıkarır»", tags=[MW, MB, "form-iv-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  maful_("الْخَبْءَ", "khab", "«what is hidden»", "«gizli olanı»"),
  fi(), tok("السَّمَاوَاتِ", "sama", "noun", [HJ, JM], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the heavens» — a sound feminine plural.", "«göklerde» — cem'-i müennes sâlim."),
  atf("وَالْأَرْضِ", "ard", "«the earth»", "«yerde»", "jarr"),
  tok("وَيَعْلَمُ", "alima", "verb", [AT, "mudari-marfu", MB], "الْوَاوُ عَاطِفَةٌ، وَيَعْلَمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and knows»", "«ve bilir»", segments=wa_("يَعْلَمُ", "alima", "verb")),
  tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the object.", "«… -inizi» — mef'ûl."),
  khamsa("تُخْفُونَ", "akhfa", "«you conceal»", "«gizlersiniz»", tags=[MW, "naqis-verbs", "form-iv-verbs"], extra_ar=" — صِلَةٌ"),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ.", "«and what»", "«ve … -inizi»", segments=wa_("مَا", "ma-mawsula", "pron")),
  khamsa("تُعْلِنُونَ", "alana-announce", "«you declare»", "«açığa vurursunuz»", tags=[MW, "form-iv-verbs"], extra_ar=" — صِلَةٌ", punct="."),
  ]),
])
sen("s7", "«God — there is no god but He, the Lord of the mighty throne» (27:26).",
        "«Allah: O'ndan başka ilâh yoktur; büyük arşın Rabbidir» (27:26).", [
  *quran([
  tok("اللهُ", "allah", "propn", [MK], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.", "«God» — the mubtadaʾ.", "«Allah» — mübtedâ."),
  tok("لَا", "la-nafiya", "part", [LJN], "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", "«no» — the lā of absolute negation, governing like inna.", "«yoktur» — cinsi nefyeden lâ, inne gibi amel eder."),
  tok("إِلٰهَ", "ilah", "noun", [LJN], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ (مَوْجُودٌ) — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«god» — lā's ism, built on fatḥa; its khabar understood; the clause is the khabar of «God».", "«ilâh» — lâ'nın ismi, fetha üzere mebnî; haberi mahzuf; cümle mübtedânın haberi."),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ (حَصْرٍ).", "«but» — the exceptive, here of restriction.", "«… -den başka» — istisnâ (hasr) edatı."),
  tok("هُوَ", "huwa", "pron", ["istithna", BD], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ بَدَلٌ مِنْ مَحَلِّ لَا وَاسْمِهَا.", "«He» — a badal of the place of lā with its ism.", "«O» — lâ ve isminin mahallinden bedel."),
  tok("رَبُّ", "rabb", "noun", [MK, ID], "خَبَرٌ ثَانٍ (أَوْ بَدَلٌ مِنْ هُوَ) مَرْفُوعٌ، مُضَافٌ.", "«the Lord [of]» — a second khabar, annexed.", "«Rabbi» — ikinci haber, muzâf."),
  mudaf_ilayh("الْعَرْشِ", "arsh", "«the throne»", "«arşın»"),
  naat("الْعَظِيمِ", "azim", "«mighty»", "«büyük»", tags=["sifa-mushabbaha"], punct="."),
  ]),
])
sen("s8", "«He said: We shall see whether you have told the truth or are of the liars» (27:27).",
        "«Dedi ki: Bakacağız, doğru mu söyledin, yoksa yalancılardan mısın» (27:27).", [
  *quran([
  qala(hidden="هُوَ", punct=None),
  tok("سَنَنْظُرُ", "nazara", "verb", ["mudari-marfu", MB], "السِّينُ لِلِاسْتِقْبَالِ، وَنَنْظُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«we shall see» — the sīn of the future.", "«bakacağız» — istikbal sîni."),
  tok("أَصَدَقْتَ", "sadaqa-verb", "verb", [IS, MB], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَصَدَقْ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ نَنْظُرُ (مُعَلَّقٌ بِالِاسْتِفْهَامِ).", "«whether you have told the truth» — the hamza of question; the clause is the object of «see».", "«doğru mu söyledin» — soru hemzesi; cümle «bakacağız»ın mef'ûlü.", segments=[seg("أَ", "hamza-istifham", "part"), seg("صَدَقْ", "sadaqa-verb", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ.", "«or» — the connected am.", "«yoksa» — muttasıla em."),
  tok("كُنْتَ", "kana", "verb", [AT, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهُ.", "«you are» — kāna with the tāʾ as its ism.", "«sen … -sin» — kâne; tâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("تَ", "pron-2ms", "pron")]),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  tok("الْكَاذِبِينَ", "kadhib-liar", "noun", [HJ, KN, JS, "ism-fail"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the liars» — jarr by the yāʾ.", "«yalancılar» — yâ ile mecrûr.", punct="."),
  ]),
])
sen("s9", "«Go with this letter of mine and deliver it to them, then turn away from them and see what they return» (27:28).",
        "«Şu mektubumu götür, onlara bırak; sonra onlardan çekil ve ne cevap vereceklerine bak» (27:28).", [
  *quran([
  tok("اذْهَبْ", "dhahaba", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«go» — an imperative on sukūn.", "«git» — sükûn üzere mebnî emir."),
  noun_pron("بِكِتَابِي", "kitab", "بِكِتَابِ", "ي", "pron-1s", "الْبَاءُ حَرْفُ جَرٍّ، وَكِتَابِ مَجْرُورٌ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«with my letter»", "«mektubumla»", tags=[HJ, ID, "ya-al-mutakallim"]),
  tok("هٰذَا", "hadha", "pron", [NA, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ نَعْتٌ لِكِتَابِي (أَوْ بَدَلٌ).", "«this» — a naʿt of «my letter».", "«şu» — mektubun sıfatı."),
  tok("فَأَلْقِهْ", "alqa", "verb", [AT, AM, MB, "naqis-verbs", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأَلْقِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ (سَاكِنَةٌ — هَاءُ السَّكْتِ عَلَى قِرَاءَةٍ).", "«and deliver it» — an imperative built on the dropped weak letter; the hāʾ the object.", "«ve onu bırak» — illet harfinin düşmesi üzere mebnî emir; hâ mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("أَلْقِ", "alqa", "verb"), seg("هْ", "pron-3ms", "pron")]),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«to them»", "«onlara»"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  tok("تَوَلَّ", "tawalla", "verb", [AM, "naqis-verbs", "form-v-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«turn away» — an imperative on the dropped weak letter.", "«çekil» — illet harfinin düşmesi üzere mebnî emir."),
  prep_pron("عَنْهُمْ", "an", "هُمْ", "pron-3mp", "«from them»", "«onlardan»"),
  tok("فَانْظُرْ", "nazara", "verb", [AT, AM, MB], "الْفَاءُ عَاطِفَةٌ، وَانْظُرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and see»", "«ve bak»", segments=[seg("فَ", "fa", "conj"), seg("انْظُرْ", "nazara", "verb")]),
  tok("مَاذَا", "madha", "pron", [IS, MB], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ (لِيَرْجِعُونَ) — وَالْجُمْلَةُ مَفْعُولُ انْظُرْ.", "«what» — the question-word, the fronted object of «return»; the clause is the object of «see».", "«ne» — soru ismi, «dönerler»in öne alınmış mef'ûlü; cümle «bak»ın mef'ûlü."),
  khamsa("يَرْجِعُونَ", "rajaa", "«they return»", "«dönerler»", tags=[], punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: all planned keys clean; naba-news, kadhib-liar, sadaqa-verb reused)
CAND = {
 "tafaqqada": G("tafaqqada", "تَفَقَّدَ", "ف ق د", "verb", "to inspect, to look for what is missing (Form V)", "yoklamak, aramak (tefa''ul)", 3),
 "tayr": G("tayr", "طَيْر", "ط ي ر", "noun", "birds", "kuşlar", 1),
 "ma-istifham": G("ma-istifham", "مَا (الِاسْتِفْهَامِيَّة)", None, "pron", "what? — the question-mā", "ne? — soru mâ'sı", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "hudhud": G("hudhud", "هُدْهُد", "ه د ه د", "noun", "a hoopoe", "hüdhüd", 2),
 "am": G("am", "أَمْ", None, "part", "or — the am of a question, connected or disjunctive", "yoksa — soru em'i, muttasıla ya da munkatıa", 1),
 "ghaib": G("ghaib", "غَائِب", "غ ي ب", "noun", "absent (an active participle)", "kayıp, gâib (ism-i fâil)", 2),
 "adhdhaba": G("adhdhaba", "عَذَّبَ", "ع ذ ب", "verb", "to punish, to torment (Form II)", "azap etmek (tef'îl)", 2),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer", "kasem cevabının lâmı", 2),
 "nun-tawkid": G("nun-tawkid", "نَّ (نُونُ التَّوْكِيدِ)", None, "part", "the heavy nūn of emphasis", "şeddeli te'kid nûnu", 2),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment", "azap", 1),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "severe", "şiddetli", 1),
 "aw": G("aw", "أَوْ", None, "part", "or", "ya da", 1),
 "dhabaha": G("dhabaha", "ذَبَحَ", "ذ ب ح", "verb", "to slaughter", "kesmek, boğazlamak", 1),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come; to bring (with bi)", "gelmek; getirmek", 1),
 "sultan": G("sultan", "سُلْطَان", "س ل ط", "noun", "a warrant, authority; a proof", "delil, sultan, yetki", 2),
 "mubin": G("mubin", "مُبِين", "ب ي ن", "noun", "clear", "apaçık", 1),
 "makatha": G("makatha", "مَكَثَ", "م ك ث", "verb", "to stay, to tarry", "kalmak, beklemek", 2),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka; olmayan", 1),
 "baid": G("baid", "بَعِيد", "ب ع د", "noun", "far, long", "uzak, uzun", 1),
 "ahata": G("ahata", "أَحَاطَ", "ح و ط", "verb", "to encompass, to grasp fully (Form IV, hollow; with bi)", "kuşatmak, tam kavramak (if'âl, ecvef; bi ile)", 3),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "saba": G("saba", "سَبَأ", "س ب أ", "propn", "Sabaʾ", "Sebe'", 2),
 "naba-news": G("naba-news", "نَبَأ", "ن ب أ", "noun", "tidings, news", "haber", 1),
 "yaqin": G("yaqin", "يَقِين", "ي ق ن", "noun", "sure, certain; certainty", "kesin, yakîn", 2),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find", "bulmak", 1),
 "imraa": G("imraa", "اِمْرَأَة", "م ر أ", "noun", "a woman", "kadın", 1),
 "malaka": G("malaka", "مَلَكَ", "م ل ك", "verb", "to rule, to possess", "hükmetmek, sahip olmak", 1),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give (Form IV)", "vermek (if'âl)", 2),
 "arsh": G("arsh", "عَرْش", "ع ر ش", "noun", "a throne", "taht, arş", 1),
 "sajada": G("sajada", "سَجَدَ", "س ج د", "verb", "to prostrate", "secde etmek", 1),
 "zayyana": G("zayyana", "زَيَّنَ", "ز ي ن", "verb", "to make fair, to embellish (Form II)", "süslemek, güzel göstermek (tef'îl)", 2),
 "shaytan": G("shaytan", "شَيْطَان", "ش ط ن", "noun", "Satan, a devil", "şeytan", 1),
 "amal-work": G("amal-work", "عَمَل", "ع م ل", "noun", "a deed", "amel", 1, plural="أَعْمَال"),
 "sadda": G("sadda", "صَدَّ", "ص د د", "verb", "to bar, to turn away (doubled)", "alıkoymak, çevirmek (muzâaf)", 2),
 "sabil": G("sabil", "سَبِيل", "س ب ل", "noun", "a way", "yol", 1),
 "hum": G("hum", "هُمْ", None, "pron", "they", "onlar", 1),
 "ihtada": G("ihtada", "اِهْتَدَى", "ه د ي", "verb", "to be guided (Form VIII)", "hidayet bulmak (iftiâl)", 2),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "akhraja": G("akhraja", "أَخْرَجَ", "خ ر ج", "verb", "to bring forth (Form IV)", "çıkarmak (if'âl)", 1),
 "khab": G("khab", "خَبْء", "خ ب أ", "noun", "what is hidden (Qurʾānic)", "gizli olan şey (Kur'ânî)", 3),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "the sky, heaven", "gök, semâ", 1, plural="سَمَاوَات"),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "the earth", "yer", 1),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know", "bilmek", 1),
 "akhfa": G("akhfa", "أَخْفَى", "خ ف ي", "verb", "to conceal (Form IV, defective)", "gizlemek (if'âl, nâkıs)", 2),
 "alana-announce": G("alana-announce", "أَعْلَنَ", "ع ل ن", "verb", "to declare, to make public (Form IV)", "açığa vurmak, ilan etmek (if'âl)", 2),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "ilah": G("ilah", "إِلٰه", "أ ل ه", "noun", "a god", "ilâh", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except, but", "… -den başka, ancak", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he", "o", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "mighty", "büyük", 1),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look, to see", "bakmak", 1),
 "sadaqa-verb": G("sadaqa-verb", "صَدَقَ", "ص د ق", "verb", "to tell the truth", "doğru söylemek", 1),
 "hamza-istifham": G("hamza-istifham", "أَ (هَمْزَةُ الِاسْتِفْهَامِ)", None, "part", "the hamza of question", "soru hemzesi", 1),
 "kadhib-liar": G("kadhib-liar", "كَاذِب", "ك ذ ب", "noun", "a liar", "yalancı", 1),
 "dhahaba": G("dhahaba", "ذَهَبَ", "ذ ه ب", "verb", "to go", "gitmek", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a letter", "mektup", 1),
 "alqa": G("alqa", "أَلْقَى", "ل ق ي", "verb", "to deliver, to cast (Form IV, defective)", "bırakmak, atmak (if'âl, nâkıs)", 2),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "tawalla": G("tawalla", "تَوَلَّى", "و ل ي", "verb", "to turn away (Form V, defective)", "çekilmek, yüz çevirmek (tefa''ul, nâkıs)", 2),
 "madha": G("madha", "مَاذَا", None, "pron", "what? — the question-word", "ne? — soru ismi", 1),
 "rajaa": G("rajaa", "رَجَعَ", "ر ج ع", "verb", "to return; to reply", "dönmek; cevap vermek", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you (attached)", "sen (bitişik)", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "I / me (attached)", "ben / beni (bitişik)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "adhdhaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "عَذَّب", "عَذِّب", "عَذِّب", "تَعْذِيب", "مُعَذِّب", "مُعَذَّب", "عُذِّبَ", "يُعَذَّبُ", "عَذَّبَهُ: عَاقَبَهُ عِقَابًا شَدِيدًا."))
put_morph(mo, "makatha", _sg.sound1("nasara", "مَكَث", "مْكُث", "اُمْكُث", "مُكْث", "مَاكِث", None, None, None, "مَكَثَ فِي الْمَكَانِ: أَقَامَ وَلَبِثَ."))
put_morph(mo, "ahata", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَحَاط", "أَحَط", "حِيط", "حِط", "أَحِيط", "أَحِط", "إِحَاطَة", "مُحِيط", "مُحَاط", "أُحِيطَ", "يُحَاطُ", "أَحَاطَ بِالشَّيْءِ: أَحْدَقَ بِهِ؛ وَأَحَاطَ بِالْأَمْرِ عِلْمًا: عَلِمَهُ كُلَّهُ."))
put_morph(mo, "zayyana", _sg.derived(_sg.B2, _sg.W2, "ُ", "زَيَّن", "زَيِّن", "زَيِّن", "تَزْيِين", "مُزَيِّن", "مُزَيَّن", "زُيِّنَ", "يُزَيَّنُ", "زَيَّنَ الشَّيْءَ: حَسَّنَهُ وَجَمَّلَهُ."))
put_morph(mo, "alana-announce", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْلَن", "عْلِن", "أَعْلِن", "إِعْلَان", "مُعْلِن", "مُعْلَن", "أُعْلِنَ", "يُعْلَنُ", "أَعْلَنَ الشَّيْءَ: أَظْهَرَهُ وَجَهَرَ بِهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch13 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 13 (print pp. 22–23, §14 part 1): the Qurʾān's telling, 27:20–28 — the missing hoopoe, its report of Sabaʾ, and Sulaymān's letter (s1–s9)."
ADD_TR = " On üçüncü bölüm (baskı s. 22–23, 14. kısım 1. parça): Kur'ân'ın anlatımı, 27:20–28 — kayıp Hüdhüd, Sebe' haberi ve Süleyman'ın mektubu (s1–s9)."
write_out(13, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §14 (27:20–28)", GLOSS_ADD, notes=(), related=())
report(13, S, GLOSS_ADD, ())
