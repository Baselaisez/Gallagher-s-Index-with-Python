# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 45: the signs of the Hour the Prophet told of are true. Source: matn line 89; the supplied text reads
«من المساء» for the received «مِنَ السَّمَاءِ» — a transcription slip, corrected and recorded.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch45.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "أَشْرَاطُ السَّاعَةِ", "en": "The Signs of the Hour", "tr": "Kıyâmet Alâmetleri"}
S = []
def DIPTOTE_NAME(full, lex, en, tr):
    return W(full, lex, "propn", ["atf-nasaq", "mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"], f"الْوَاوُ عَاطِفَةٌ، وَ«{full[2:]}» مَعْطُوفٌ عَلَى «خُرُوجِ» مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ — أَيْ: وَخُرُوجِ {full[2:]}.", en, tr, segments=[seg("وَ", "wa", "conj"), seg(full[2:], lex, "propn")])
S.append({"id": "s1", "translation": {
 "en": "And what the Prophet — upon him be blessing and peace — told of the signs of the Hour: the coming of the Dajjāl, the Beast of the Earth, Gog and Magog, the descent of Jesus — upon him be peace — from the sky, and the rising of the sun from its west — it is true.",
 "tr": "Peygamber'in — ona salât ve selâm olsun — kıyâmet alâmetlerinden haber verdiği şeyler: Deccâl'in çıkışı, Dâbbetü'l-arz, Ye'cûc ve Me'cûc, Îsâ'nın — ona selâm olsun — gökten inişi ve güneşin batısından doğuşu — hepsi haktır."},
 "tokens": [
  MAWSUL("وَمَا", "ma-mawsula", "«and what» — the mubtada of a long sentence; its khabar is فَهُوَ حَقٌّ at the end.", "«ve her ne ki» — uzun bir cümlenin mübtedası; haberi sondaki فَهُوَ حَقٌّ'tur.", "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَدَخَلَتِ الْفَاءُ فِي خَبَرِهِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ", wa="isti", tags=["mubtada-khabar", "al-fa-fi-khabar-al-mubtada", "anwa-ma"]),
  MAZI("أَخْبَرَ", "akhbara", "«told» — the ṣila.", "«haber verdi» — sıla.", "وَالْفَاعِلُ «النَّبِيُّ» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ", tags=["ism-mawsul", "form-iv-verbs", "fail"]),
  PRON_J("بِهِ", "بِ", "«of it» — the returning pronoun of مَا.", "«onu» — مَا'nın âidi.", "«أَخْبَرَ»"),
  FAIL("النَّبِيُّ", "nabi", "«the Prophet».", "«Peygamber»."),
  *SALAWAT(),
  PREP("مِنْ", "min", "«of» — explaining what «it» is.", "«-den» — «o»nun ne olduğunu açıklar."),
  MAJ("أَشْرَاطِ", "ashrat", "«the signs of» — the plural of شَرَط.", "«alâmetlerinden» — شَرَط'ın çoğulu.", "مِنْ", "مَحْذُوفٍ حَالٌ مِنَ الْهَاءِ فِي «بِهِ»", mudaf=True, tags=["jam-taksir", "hal"]),
  MUDI("السَّاعَةِ", "saa-hour", "«the Hour» — the Resurrection.", "«kıyâmetin» — Saat.", punct="،"),
  PREP("مِنْ", "min", "«of» — a second min, detailing the signs.", "«-den» — alâmetleri tafsil eden ikinci min.", extra=" — بَدَلٌ مِنْ «مِنْ أَشْرَاطِ»، بَيَانٌ لِلْأَشْرَاطِ"),
  MAJ("خُرُوجِ", "khuruj", "«the coming out of».", "«çıkışı».", "مِنْ", None, mudaf=True, tags=["masdar", "badal"]),
  MUDI("الدَّجَّالِ", "dajjal", "«the Dajjāl» — the great deceiver.", "«Deccâl» — büyük yalancı."),
  ATF("وَدَابَّةِ", "dabba", "«and the Beast of».", "«ve Dâbbe'si».", "خُرُوجِ", "jarr", mudaf=True),
  MUDI("الْأَرْضِ", "ard", "«the Earth».", "«yerin»."),
  DIPTOTE_NAME("وَيَأْجُوجَ", "yajuj", "«and Gog» — a foreign proper name, barred from tanwīn: its jarr is by the fatḥa.", "«ve Ye'cûc» — acemî alem, gayr-i munsarif: cerri fetha iledir."),
  DIPTOTE_NAME("وَمَأْجُوجَ", "majuj", "«and Magog».", "«ve Me'cûc»."),
  ATF("وَنُزُولِ", "nuzul", "«and the descent of».", "«ve inişi».", "خُرُوجِ", "jarr", mudaf=True, tags=["masdar"]),
  W("عِيسَى", "isa", "propn", ["idafa-definiteness", "ism-maqsur-manqus", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ، مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.", "«Jesus» — a maqṣūr diptote: its fatḥa of jarr is estimated on the alif.", "«Îsâ'nın» — maksûr gayr-i munsarif: cer fethası elif üzerinde takdirîdir."),
  *SALAWAT(salat=False),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  MAJ("السَّمَاءِ", "sama", "«the sky» — the supplied transcription reads المساء, a slip for the received السَّمَاءِ.", "«gök» — nüsha المساء yazar; alınan metindeki السَّمَاءِ'nin yazım hatası.", "مِنَ", "«نُزُولِ»", tags=["ism-mamdud"]),
  ATF("وَطُلُوعِ", "tulu", "«and the rising of».", "«ve doğuşu».", "خُرُوجِ", "jarr", mudaf=True, tags=["masdar"]),
  MUDI("الشَّمْسِ", "shams", "«the sun».", "«güneşin»."),
  PREP("مِنْ", "min", "«from».", "«-den»."),
  ENC("مَغْرِبِهَا", "maghrib", "«its west» — the place of its setting.", "«batısından» — batış yeri.", "اسْمٌ مَجْرُورٌ بِـ«مِنْ» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هَا", att="«طُلُوعِ»", punct="،"),
  FA_HUWA("مَا", "«it» — the fāʾ of the khabar returns to the opening مَا.", "«o» — haber fâ'sı baştaki مَا'ya döner."),
  KHA("حَقٌّ", "haqq", "«is true».", "«haktır».", of="هُوَ", punct=".")]})

CAND = {
 "ashrat": need("ashrat", "أَشْرَاط", "ش ر ط", "noun", "signs, portents (pl. of شَرَط) — the signs of the Hour", "alâmetler (شَرَط'ın çoğulu) — kıyâmet alâmetleri", 4),
 "saa-hour": need("saa-hour", "سَاعَة", "س و ع", "noun", "the Hour — the Resurrection; an hour", "Saat — kıyâmet; saat", 2, plural="سَاعَات"),
 "yajuj": need("yajuj", "يَأْجُوج", "", "propn", "Gog — of the peoples whose coming out is a sign of the Hour", "Ye'cûc — çıkışı kıyâmet alâmeti olan kavimlerden", 3),
 "majuj": need("majuj", "مَأْجُوج", "", "propn", "Magog", "Me'cûc", 3),
 "nuzul": need("nuzul", "نُزُول", "ن ز ل", "noun", "descent, coming down (masdar)", "iniş, nüzûl (masdar)", 3),
 "tulu": need("tulu", "طُلُوع", "ط ل ع", "noun", "rising (of the sun) (masdar)", "doğuş, tulû (masdar)", 3),
}
ADD_EN = (" Chapter 45 (matn line 89): the signs of the Hour the Prophet told of — the Dajjāl, the Beast, Gog and Magog, Jesus's descent, the"
          " sun from its west — are true. Divergence: the supplied text reads «من المساء»; the received «مِنَ السَّمَاءِ» is used.")
ADD_TR = (" Kırk beşinci bâb (matn satırı 89): Peygamber'in haber verdiği kıyâmet alâmetleri — Deccâl, Dâbbe, Ye'cûc ve Me'cûc, Îsâ'nın inişi,"
          " güneşin batıdan doğuşu — haktır. Fark: nüsha «من المساء» yazar; alınan «مِنَ السَّمَاءِ» kullanılmıştır.")
finish(45, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 45 (matn line 89)")
