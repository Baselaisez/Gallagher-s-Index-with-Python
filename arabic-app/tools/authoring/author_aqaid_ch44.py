# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 44: the prayer of the living benefits the dead; God answers prayers; the mujtahid may err and may be right.
Source: matn lines 87 and 91.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch44.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "دُعَاءُ الْأَحْيَاءِ لِلْأَمْوَاتِ، وَالْمُجْتَهِدُ", "en": "The Prayer of the Living for the Dead; the Mujtahid", "tr": "Dirilerin Ölülere Duası ve Müctehid"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And in the prayer of the living for the dead, and in their giving charity on their behalf, there is benefit for them.",
 "tr": "Dirilerin ölülere duasında ve onlar adına sadaka vermesinde, ölüler için fayda vardır."},
 "tokens": [
  W("وَفِي", "fi", "prep", ["huruf-jarr", "taqdim-al-musnad"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«فِي» حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ مُقَدَّمٌ.", "«and in» — the jarr phrase opens the sentence as a khabar put first.", "«ve … -de» — câr-mecrûr, öne alınmış haber olarak cümleyi açar.", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")]),
  MAJ("دُعَاءِ", "dua", "«the prayer of» — a masdar annexed to its doer.", "«duasında» — fâiline muzâf masdar.", "فِي", None, mudaf=True, tags=["masdar", "imal-al-masdar", "ism-mamdud"]),
  MUDI("الْأَحْيَاءِ", "hayy", "«the living» — the plural of حَيّ.", "«dirilerin» — حَيّ'in çoğulu.", tags=["jam-taksir"]),
  FUSED("لِلْأَمْوَاتِ", "لِ", "mayyit", "«for the dead» — the plural of مَيِّت.", "«ölülere» — مَيِّت'in çoğulu.", "«دُعَاءِ»", inner="الْأَمْوَاتِ", tags=["jam-taksir"]),
  ENC("وَتَصَدُّقِهِمْ", "tasadduq", "«and their giving charity» — the masdar of Form V, annexed to its doer.", "«ve sadaka vermeleri» — fâiline muzâf tefe'ul masdarı.", "مَعْطُوفٌ عَلَى «دُعَاءِ» تَابِعٌ لَهُ فِي الْجَرِّ", pr="هِمْ", wa="atf", tags=["atf-nasaq", "masdar", "form-v-verbs"]),
  PRON_J("عَنْهُمْ", "عَنْ", "«on their behalf».", "«onlar adına».", "«تَصَدُّقِهِمْ»"),
  W("نَفْعٌ", "naf", "noun", ["mubtada-khabar", "taqdim-al-musnad"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ — وَجَازَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ.", "«benefit» — the delayed mubtada; an indefinite may open a sentence once its khabar stands before it.", "«fayda» — sonraya bırakılmış mübteda; haberi önce geldiği için nekre mübteda olabilmiştir."),
  PRON_J("لَهُمْ", "لِ", "«for them» — for the dead.", "«onlar için» — ölüler için.", "مَحْذُوفٍ صِفَةٌ لِـ«نَفْعٌ»", punct=".", tags=["jumla-sifa"])]})
S.append({"id": "s2", "translation": {"en": "And God the Exalted answers prayers and fulfils needs.", "tr": "Allah Teâlâ duaları kabul eder, hâcetleri giderir."},
 "tokens": [
  MUB("وَاللهُ", "allah", "«and God».", "«ve Allah».", wa="isti", pos="propn"),
  TAALA(),
  MUDA("يُجِيبُ", "ajaba", "«answers» — Form IV of a hollow root; the sentence is the khabar.", "«kabul eder» — ecvef kökün if'âl bâbı; cümle haberdir.", HIDDEN_HUWA + "، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ", tags=["form-iv-verbs", "hollow-verbs", "anwa-al-khabar"]),
  W("الدَّعَوَاتِ", "dawa", "noun", ["maful-bihi", "jam-muannath-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْكَسْرَةُ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«prayers» — a sound feminine plural: its naṣb is by the kasra.", "«duaları» — cem'-i müennes sâlim: nasbı kesre iledir."),
  MUDA("وَيَقْضِي", "qada-verb", "«and fulfils» — a defective verb with an estimated ḍamma.", "«ve giderir» — takdirî dammeli nâkıs fiil.", HIDDEN_HUWA, wa="atf", tags=["naqis-verbs", "atf-nasaq"], sign="الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  W("الْحَاجَاتِ", "haja", "noun", ["maful-bihi", "jam-muannath-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْكَسْرَةُ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«needs».", "«hâcetleri».", punct=".")]})
S.append({"id": "s3", "translation": {"en": "And the mujtahid may err and may be right.", "tr": "Müctehid bazen hata eder, bazen isabet eder."},
 "tokens": [
  MUB("وَالْمُجْتَهِدُ", "mujtahid", "«and the mujtahid» — the one qualified to derive rulings.", "«ve müctehid» — hüküm çıkarmaya ehil olan.", wa="isti", tags=["ism-fail", "form-viii-verbs"]),
  W("قَدْ", "qad", "part", ["qad-harf", "al-tahdid-wa-qad-wal-istifham-fil-kafiya"], "حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ، مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "«may, sometimes» — qad before a muḍāriʿ lessens: sometimes.", "«bazen» — muzâri önündeki kad azaltır: ara sıra."),
  MUDA("يُخْطِئُ", "akhtaa", "«errs» — Form IV of a hamzated root.", "«hata eder» — mehmûz kökün if'âl bâbı.", HIDDEN_HUWA + "، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ", tags=["form-iv-verbs", "anwa-al-khabar"]),
  MUDA("وَيُصِيبُ", "asaba", "«and is right».", "«ve isabet eder».", HIDDEN_HUWA, wa="atf", tags=["form-iv-verbs", "hollow-verbs", "atf-nasaq"], punct=".")]})

CAND = {
 "tasadduq": need("tasadduq", "تَصَدُّق", "ص د ق", "noun", "giving charity (masdar of Form V)", "sadaka verme (tefe'ul masdarı)", 3),
 "qada-verb": need("qada-verb", "قَضَى", "ق ض ي", "verb", "to decree; to fulfil (a need); to judge", "hükmetmek; (ihtiyacı) gidermek; kaza etmek", 3),
}
MORPH = {"qada-verb": sarf.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "قَضَ", "قْض", "i", "اِقْض", "قَضَاء", "قَاضٍ", "مَقْضِيّ", "قُضِيَ", "يُقْضَى",
                                   "قَضَى الْحَاجَةَ يَقْضِيهَا قَضَاءً: أَتَمَّهَا وَأَنْفَذَهَا — مِنْ بَابِ ضَرَبَ، نَاقِصٌ يَائِيٌّ")}
ADD_EN = " Chapter 44 (matn lines 87 and 91): the prayer and charity of the living benefit the dead, God answers prayers, and the mujtahid may err and may be right."
ADD_TR = " Kırk dördüncü bâb (matn satırları 87 ve 91): dirilerin dua ve sadakası ölülere fayda verir, Allah duaları kabul eder, müctehid bazen hata bazen isabet eder."
finish(44, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 44 (matn lines 87 and 91)", morph=MORPH)
