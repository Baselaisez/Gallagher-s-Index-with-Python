# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 40: deeds increase, faith does not increase or decrease; faith and islam are one. Source: matn line 57
(فأما الأعمال فهي تتزايد في نفسها … والإيمان والإسلام واحد); the definition of faith before it is chapter 9 s4.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch40.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْإِيمَانُ لَا يَزِيدُ وَلَا يَنْقُصُ", "en": "Faith Neither Increases nor Decreases", "tr": "Îmân Ne Artar Ne Eksilir"}
S = []
S.append({"id": "s1", "translation": {
 "en": "As for deeds, they increase in themselves; and faith neither increases nor decreases.",
 "tr": "Amellere gelince: onlar kendi içlerinde artar; îmân ise ne artar ne eksilir."},
 "tokens": [
  W("فَأَمَّا", "amma", "part", ["amma-tafsiliyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَ«أَمَّا» حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ لَا مَحَلَّ لَهُ.", "«as for» — branching off the definition of faith (chapter 9): faith is assent, so what of deeds?", "«… -e gelince» — îmân tarifinden (9. bâb) dallanır: îmân tasdiktir, peki ameller?", segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  MUB("الْأَعْمَالُ", "amal-deed", "«deeds» — the plural of عَمَل.", "«ameller» — عَمَل'in çoğulu.", tags=["jam-taksir"]),
  W("فَهِيَ", "pron-3fs-munfasil", "pron", ["amma-tafsiliyya", "mubtada-khabar", "al-marifa-al-mudmarat-wal-alam"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ«هِيَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ ثَانٍ، وَالْجُمْلَةُ خَبَرُ «الْأَعْمَالُ».", "«they» — the fāʾ of ammā's answer; a feminine singular pronoun for a plural of things.", "«onlar» — emmâ'nın cevap fâ'sı; gayr-i âkil çoğul için müfred müennes zamir.", segments=[seg("فَ", "fa", "conj"), seg("هِيَ", "pron-3fs-munfasil", "pron")]),
  MUDA("تَتَزَايَدُ", "tazayada", "«increase» — Form VI: increase upon increase.", "«artar» — tefâul bâbı: artış üstüne artış.", HIDDEN_HIYA + "، وَالْجُمْلَةُ خَبَرُ «هِيَ»", tags=["form-vi-verbs", "anwa-al-khabar"]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  ENC("نَفْسِهَا", "nafs", "«themselves» — in their own count and kind.", "«kendi içlerinde» — sayı ve cins bakımından.", "اسْمٌ مَجْرُورٌ بِـ«فِي» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هَا", att="«تَتَزَايَدُ»", punct="،"),
  MUB("وَالْإِيمَانُ", "iman", "«and faith».", "«ve îmân».", wa="isti"),
  LA("«does not».", "«-maz».", ar="حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ — وَالْجُمْلَةُ الْفِعْلِيَّةُ بَعْدَهُ خَبَرُ الْمُبْتَدَإِ."),
  MUDA("يَزِيدُ", "zada", "«increases» — faith as assent admits no more and no less; what varies is its strength and its fruits.", "«artar» — tasdik olarak îmân azlık çokluk kabul etmez; değişen kuvveti ve meyveleridir.", HIDDEN_HUWA, tags=["hollow-verbs", "anwa-al-khabar"]),
  WALA(),
  MUDA("يَنْقُصُ", "naqasa", "«decreases».", "«eksilir».", HIDDEN_HUWA, tags=["atf-nasaq"], punct=".")]})
S.append({"id": "s2", "translation": {"en": "And faith and islam are one.", "tr": "Îmân ile İslâm birdir."},
 "tokens": [
  MUB("وَالْإِيمَانُ", "iman", "«and faith».", "«ve îmân».", wa="isti"),
  ATF("وَالْإِسْلَامُ", "islam", "«and islam» — submission; the two names, one reality.", "«ve İslâm» — teslimiyet; iki isim, tek hakikat.", "الْإِيمَانُ", "raf"),
  KHA("وَاحِدٌ", "wahid", "«are one» — a singular khabar for a pair, since the pair is one thing.", "«birdir» — ikisi tek şey olduğu için tekil haber.", of="الْإِيمَانُ وَالْإِسْلَامُ", punct=".")]})

CAND = {
 "amal-deed": need("amal-deed", "عَمَل", "ع م ل", "noun", "a deed, an act, work", "amel, iş", 2, plural="أَعْمَال"),
 "tazayada": need("tazayada", "تَزَايَدَ", "ز ي د", "verb", "to increase more and more, to grow", "gittikçe artmak, çoğalmak", 4),
}
MORPH = {"tazayada": sarf.derived(sarf.B6, W6, "َ", "تَزَايَد", "تَزَايَد", "تَزَايَد", "تَزَايُد", "مُتَزَايِد", None, None, None,
                                  "تَزَايَدَ الشَّيْءُ يَتَزَايَدُ تَزَايُدًا: ازْدَادَ شَيْئًا فَشَيْئًا — مِنْ بَابِ التَّفَاعُلِ، لَازِمٌ")}
ADD_EN = " Chapter 40 (matn line 57): deeds increase in themselves, faith neither increases nor decreases, and faith and islam are one; the definition of faith is chapter 9."
ADD_TR = " Kırkıncı bâb (matn satırı 57): ameller kendi içlerinde artar, îmân ne artar ne eksilir, îmân ile İslâm birdir; îmân tarifi dokuzuncu bâbdır."
finish(40, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 40 (matn line 57)", morph=MORPH)
