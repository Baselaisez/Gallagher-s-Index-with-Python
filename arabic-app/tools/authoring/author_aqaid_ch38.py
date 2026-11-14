# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 38: God misguides whom He wills and guides whom He wills; the best for the servant is not incumbent on Him.
Source: matn line 49.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch38.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْإِضْلَالُ وَالْهِدَايَةُ، وَالْأَصْلَحُ", "en": "Misguiding and Guiding, and «the Best»", "tr": "İdlâl ve Hidâyet, ve Aslah"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And God the Exalted misguides whom He wills and guides whom He wills.",
 "tr": "Allah Teâlâ dilediğini saptırır, dilediğine hidâyet eder."},
 "tokens": [
  MUB("وَاللهُ", "allah", "«and God».", "«ve Allah».", wa="isti", pos="propn"),
  TAALA(),
  MUDA("يُضِلُّ", "adalla", "«misguides» — Form IV of a doubled root; the verbal sentence is the khabar.", "«saptırır» — muzaaf kökün if'âl bâbı; fiil cümlesi haberdir.", HIDDEN_HUWA + "، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ", tags=["form-iv-verbs", "doubled-verbs", "anwa-al-khabar"]),
  MAWSUL("مَنْ", "man-mawsula", "«whom» — the relative as object.", "«kimi» — mef'ûl olan ism-i mevsûl.", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", tags=["maful-bihi"]),
  MUDA("يَشَاءُ", "shaa", "«He wills» — the ṣila; its returning pronoun is dropped: whom He wills to misguide.", "«diler» — sıla; âidi hazfedilmiştir: saptırmayı dilediğini.", HIDDEN_HUWA + " — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: مَنْ يَشَاءُ إِضْلَالَهُ", tags=["ism-mawsul", "hollow-verbs"]),
  MUDA("وَيَهْدِي", "hada", "«and guides» — a defective verb with an estimated ḍamma.", "«ve hidâyet eder» — takdirî dammeli nâkıs fiil.", HIDDEN_HUWA, wa="atf", tags=["naqis-verbs", "atf-nasaq"], sign="الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  MAWSUL("مَنْ", "man-mawsula", "«whom».", "«kimi».", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", tags=["maful-bihi"]),
  MUDA("يَشَاءُ", "shaa", "«He wills».", "«diler».", HIDDEN_HUWA + " — صِلَةُ الْمَوْصُولِ", tags=["ism-mawsul"], punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And what is the best for the servant — that is not incumbent on God the Exalted.",
 "tr": "Kul için en uygun (aslah) olan — o, Allah Teâlâ'ya vâcip değildir."},
 "tokens": [
  MAWSUL("وَمَا", "ma-mawsula", "«and what» — the mubtada; the fāʾ enters its khabar because it has the sense of a condition.", "«ve her ne ki» — mübteda; şart mânâsı taşıdığı için haberine fâ girer.", "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَدَخَلَتِ الْفَاءُ فِي خَبَرِهِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ", wa="isti", tags=["mubtada-khabar", "al-fa-fi-khabar-al-mubtada", "anwa-ma"]),
  HUWA("هُوَ", "«is» — a pronoun opening the ṣila.", "«o» — sılayı açan zamir.", extra="، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا", tags=["ism-mawsul"]),
  KHA("الْأَصْلَحُ", "aslah", "«the best, the most fitting» — the Muʿtazilī thesis that God must do what is best for the servant.", "«aslah, en uygun» — Allah'ın kul için en iyiyi yapmak zorunda olduğunu söyleyen Mu'tezilî tez.", of="هُوَ", tags=["ism-tafdil"]),
  FUSED("لِلْعَبْدِ", "لِ", "abd", "«for the servant».", "«kul için».", "«الْأَصْلَحُ»", inner="الْعَبْدِ"),
  W("فَلَيْسَ", "laysa", "verb", ["al-fa-fi-khabar-al-mubtada", "kana-wa-akhawatuha", "al-afal-al-naqisa-fil-kafiya"], "الْفَاءُ دَاخِلَةٌ فِي خَبَرِ الْمُبْتَدَإِ لِتَضَمُّنِهِ مَعْنَى الشَّرْطِ، وَ«لَيْسَ» فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ — وَالْجُمْلَةُ خَبَرُ «مَا».", "«then … is not» — the fāʾ of the khabar; the laysa-sentence is the khabar of مَا.", "«o hâlde … değildir» — haber fâ'sı; leyse cümlesi مَا'nın haberidir.", segments=[seg("فَ", "fa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  ISHARA("ذَلِكَ", "dhalika", "«that» — the ism of laysa, pointing back at مَا.", "«o» — leyse'nin ismi; مَا'ya işaret eder.", "فِي مَحَلِّ رَفْعٍ اسْمُ «لَيْسَ»", tags=["kana-wa-akhawatuha"]),
  W("بِوَاجِبٍ", "wajib", "noun", ["huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha", "ism-fail"], "الْبَاءُ زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ، وَ«وَاجِبٍ» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ «لَيْسَ».", "«incumbent» — laysa's khabar behind an extra bāʾ: in jarr on the page, in naṣb in place.", "«vâcip» — zâid bâ ardındaki leyse haberi: lafzan mecrûr, mahallen mansûb.", segments=[seg("بِ", "bi", "prep"), seg("وَاجِبٍ", "wajib", "noun")]),
  PREP("عَلَى", "ala", "«on».", "«üzerine»."),
  MAJ("اللهِ", "allah", "«God».", "«Allah'a».", "عَلَى", "«وَاجِبٍ»", pos="propn"),
  TAALA(punct=".")]})

CAND = {}
ADD_EN = " Chapter 38 (matn line 49): God misguides and guides whom He wills; what is best for the servant is not incumbent on Him (against the Muʿtazilī aṣlaḥ)."
ADD_TR = " Otuz sekizinci bâb (matn satırı 49): Allah dilediğini saptırır, dilediğine hidâyet eder; kul için aslah olan O'na vâcip değildir (Mu'tezile'nin aslah tezine karşı)."
finish(38, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 38 (matn line 49)")
