# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 37: the forbidden is provision; everyone takes his own provision in full, lawful or forbidden.
Source: matn line 47.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch37.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْحَرَامُ رِزْقٌ", "en": "The Forbidden Is Provision", "tr": "Haram da Rızıktır"}
S = []
S.append({"id": "s1", "translation": {"en": "And the forbidden is provision.", "tr": "Haram da rızıktır."},
 "tokens": [
  MUB("وَالْحَرَامُ", "haram", "«and the forbidden» — against the Muʿtazila, who said only the lawful is provision.", "«ve haram» — yalnız helâlin rızık olduğunu söyleyen Mu'tezile'ye karşı.", wa="isti"),
  KHA("رِزْقٌ", "rizq", "«is provision» — what a living being actually consumes.", "«rızıktır» — canlının fiilen yiyip içtiği şey.", of="الْحَرَامُ", punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And everyone takes his own provision in full, whether it be lawful or forbidden.",
 "tr": "Herkes kendi rızkını — helâl olsun haram olsun — tam olarak alır."},
 "tokens": [
  W("وَكُلٌّ", "kull", "noun", ["mubtada-khabar", "hadhf-al-mudaf-wal-mudaf-ilayh"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«كُلٌّ» مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ: كُلُّ أَحَدٍ.", "«and everyone» — كُلّ with its tanwīn standing in for a dropped «one»: every one.", "«ve herkes» — tenvini hazfedilmiş muzâfun ileyhin yerine duran كُلّ: her bir kişi.", segments=[seg("وَ", "wa", "conj"), seg("كُلٌّ", "kull", "noun")]),
  MUDA("يَسْتَوْفِي", "istawfa", "«takes in full» — Form X of وفي, a defective verb; the ḍamma is estimated.", "«tam olarak alır» — وفي kökünün istif'âl bâbı, nâkıs fiil; damme takdirîdir.", HIDDEN_HUWA + "، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ", tags=["form-x-verbs", "naqis-verbs", "anwa-al-khabar"], sign="الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  MAFUL("رِزْقَ", "rizq", "«the provision of».", "«rızkını».", "يَسْتَوْفِي", mudaf=True),
  ENC("نَفْسِهِ", "nafs", "«his own self».", "«kendi».", "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", punct="،"),
  W("حَلَالًا", "halal", "noun", ["kana-wa-akhawatuha", "taqdim-al-musnad", "hal"], "خَبَرُ «كَانَ» مُقَدَّمٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — وَجُمْلَةُ «كَانَ» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «رِزْقَ».", "«lawful» — kāna's khabar put before it; the kāna-sentence is a ḥāl of the provision.", "«helâl» — kâne'nin öne alınmış haberi; kâne cümlesi rızkın hâlidir."),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hal"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ عَلَى الرِّزْقِ.", "«whether it be».", "«olsun»."),
  AW(),
  W("حَرَامًا", "haram", "noun", ["atf-nasaq", "kana-wa-akhawatuha"], "مَعْطُوفٌ عَلَى «حَلَالًا» تَابِعٌ لَهُ فِي النَّصْبِ.", "«or forbidden».", "«ya da haram».", punct=".")]})
S.append({"id": "s3", "translation": {
 "en": "And it is not conceivable that a man should not eat his provision, or that another should eat his provision.",
 "tr": "Bir insanın kendi rızkını yememesi ya da başkasının onun rızkını yemesi tasavvur olunamaz."},
 "tokens": [
  W("وَلَا", "la-nafiya", "part", ["la-nafiya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَا» حَرْفُ نَفْيٍ لَا مَحَلَّ لَهُ.", "«and not».", "«ve … -maz».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُتَصَوَّرُ", "tasawwara", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-v-verbs", "an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ» وَمَا بَعْدَهَا.", "«is conceivable» — a passive whose deputy doer is the an-clause: «a man's not eating … is not conceivable».", "«tasavvur olunur» — nâib-i fâili en'li masdar olan meçhul: «insanın yememesi tasavvur olunmaz»."),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«that» — the an that turns its clause into a masdar.", "«… -ması» — cümlesini masdar yapan en."),
  LA("«not» — the negation inside the masdar: «a not-eating».", "«-me-» — masdarın içindeki nefiy: «yememe»."),
  W("يَأْكُلَ", "akala", "verb", ["nawasib-wa-jawazim-al-mudari", "an-masdariyya", "fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«eat» — in naṣb by an.", "«yesin» — en ile mansûb."),
  FAIL("إِنْسَانٌ", "insan", "«a man».", "«bir insan»."),
  ENC("رِزْقَهُ", "rizq", "«his provision».", "«rızkını».", "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", pr="هُ", punct="،", tags=["maful-bihi"]),
  AW(),
  W("يَأْكُلَ", "akala", "verb", ["atf-nasaq", "nawasib-wa-jawazim-al-mudari", "fail"], "مَعْطُوفٌ عَلَى «يَأْكُلَ» الْأُولَى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«(or that) … eat» — joined to the first verb inside the masdar.", "«yesin» — masdar içindeki ilk fiile atıf."),
  ENC("غَيْرُهُ", "ghayr", "«another than he».", "«başkası».", "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ", pr="هُ", tags=["fail"]),
  ENC("رِزْقَهُ", "rizq", "«his provision».", "«onun rızkını».", "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", pr="هُ", punct=".", tags=["maful-bihi"])]})

CAND = {
 "istawfa": need("istawfa", "اِسْتَوْفَى", "و ف ي", "verb", "to take in full, to receive the whole of", "tam olarak almak, istîfâ etmek", 4),
}
MORPH = {"istawfa": sarf.derived_naqis(sarf.B10 + " — مِثَالٌ نَاقِصٌ", W10, "َ", "اِسْتَوْفَ", "سْتَوْف", "i", "اِسْتَوْف", "اِسْتِيفَاء", "مُسْتَوْفٍ", "مُسْتَوْفًى", "اُسْتُوفِيَ", "يُسْتَوْفَى",
                                        "اِسْتَوْفَى حَقَّهُ يَسْتَوْفِيهِ اسْتِيفَاءً: أَخَذَهُ تَامًّا — مِنْ بَابِ الِاسْتِفْعَالِ، لَفِيفٌ مَفْرُوقٌ")}
ADD_EN = " Chapter 37 (matn line 47): the forbidden is provision; everyone takes his own provision in full, lawful or forbidden, and no one eats another's."
ADD_TR = " Otuz yedinci bâb (matn satırı 47): haram da rızıktır; herkes helâl ya da haram kendi rızkını tam alır, kimse başkasınınkini yemez."
finish(37, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 37 (matn line 47)", morph=MORPH)
