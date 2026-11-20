# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 42: the saint does not reach the rank of the prophets; no servant reaches where command and prohibition
fall away; the non-existent is not a thing. Source: matn lines 81 and 85.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch42.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْوَلِيُّ وَالنَّبِيُّ، وَالْمَعْدُومُ", "en": "The Saint and the Prophet; the Non-Existent", "tr": "Velî ile Nebî ve Ma'dûm"}
S = []
S.append({"id": "s1", "translation": {"en": "And the saint does not reach the rank of the prophets.", "tr": "Velî, nebîlerin derecesine ulaşmaz."},
 "tokens": [
  W("وَلَا", "la-nafiya", "part", ["la-nafiya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«and not».", "«ve … -maz».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  MUDA("يَبْلُغُ", "balagha", "«reaches».", "«ulaşır».", "وَالْفَاعِلُ «الْوَلِيُّ»", tags=["fail"]),
  FAIL("الْوَلِيُّ", "wali", "«the saint».", "«velî»."),
  MAFUL("دَرَجَةَ", "daraja", "«the rank of».", "«derecesine».", "يَبْلُغُ", mudaf=True),
  MUDI("الْأَنْبِيَاءِ", "nabi", "«the prophets» — the plural of نَبِيّ.", "«nebîlerin» — نَبِيّ'in çoğulu.", punct=".", tags=["jam-taksir"])]})
S.append({"id": "s2", "translation": {
 "en": "And the servant does not reach a point where command and prohibition fall away from him.",
 "tr": "Kul, emir ve nehyin kendisinden düştüğü bir yere ulaşmaz."},
 "tokens": [
  W("وَلَا", "la-nafiya", "part", ["la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«and not».", "«ve … -maz».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  MUDA("يَصِلُ", "wasala", "«reaches» — the assimilated verb drops its wāw in the muḍāriʿ: وَصَلَ، يَصِلُ.", "«ulaşır» — misâl fiil muzâride vâvını düşürür: وَصَلَ، يَصِلُ.", "وَالْفَاعِلُ «الْعَبْدُ»", tags=["fail", "mithal-verbs"]),
  FAIL("الْعَبْدُ", "abd", "«the servant».", "«kul»."),
  PREP("إِلَى", "ila", "«to».", "«-e»."),
  W("حَيْثُ", "haythu", "noun", ["al-kinayat-wal-zuruf-al-mabniyya", "mahall-al-majrur", "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِـ«إِلَى»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«where» — a ẓarf built on the ḍamma, annexed to a whole sentence.", "«… -diği yer» — damme üzere mebnî, cümleye muzâf zarf."),
  MUDA("يَسْقُطُ", "saqata", "«falls away» — the sentence annexed to حَيْثُ.", "«düşer» — حَيْثُ'ya muzâf cümle.", "وَالْفَاعِلُ «الْأَمْرُ»، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", tags=["fail", "idafa-definiteness"]),
  PRON_J("عَنْهُ", "عَنْ", "«from him».", "«ondan».", "«يَسْقُطُ»"),
  FAIL("الْأَمْرُ", "amr", "«command».", "«emir»."),
  ATF("وَالنَّهْيُ", "nahy", "«and prohibition» — the Antinomian claim that a perfected servant is free of the Law is denied.", "«ve nehiy» — kâmil kulun şeriattan kurtulduğu iddiası reddedilir.", "الْأَمْرُ", "raf", punct=".")]})
S.append({"id": "s3", "translation": {"en": "And the non-existent is not a thing.", "tr": "Ma'dûm, bir şey değildir."},
 "tokens": [
  MUB("وَالْمَعْدُومُ", "madum", "«and the non-existent» — against the Muʿtazilī thesis that the non-existent is a «thing».", "«ve ma'dûm» — ma'dûmun «şey» olduğunu söyleyen Mu'tezilî teze karşı.", wa="isti", tags=["ism-maful"]),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-afal-al-naqisa-fil-kafiya"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«is not».", "«değildir»."),
  W("بِشَيْءٍ", "shay", "noun", ["huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha"], "الْبَاءُ زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ، وَ«شَيْءٍ» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ «لَيْسَ».", "«a thing» — laysa's khabar behind the extra bāʾ.", "«bir şey» — zâid bâ ardındaki leyse haberi.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")])]})

CAND = {}
ADD_EN = " Chapter 42 (matn lines 81 and 85): the saint below the prophets, no servant beyond command and prohibition, and the non-existent is not a thing."
ADD_TR = " Kırk ikinci bâb (matn satırları 81 ve 85): velî nebîlerin altındadır, hiçbir kul emir ve nehyin dışına çıkmaz, ma'dûm bir şey değildir."
finish(42, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 42 (matn lines 81 and 85)")
