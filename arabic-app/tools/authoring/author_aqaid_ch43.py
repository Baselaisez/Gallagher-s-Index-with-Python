# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 43: the texts on their apparent meanings; the eight kinds of unbelief. Source: matn line 83.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch43.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "النُّصُوصُ عَلَى ظَوَاهِرِهَا", "en": "The Texts on Their Apparent Meanings", "tr": "Naslar Zâhirleri Üzeredir"}
S = []
def KUFR(punct="."): return KHA("كُفْرٌ", "kufr", "«is unbelief».", "«küfürdür».", punct=punct)
S.append({"id": "s1", "translation": {"en": "And the texts are on their apparent meanings.", "tr": "Naslar zâhirleri üzeredir."},
 "tokens": [
  MUB("وَالنُّصُوصُ", "nass", "«and the texts» — the Qur'an and the Sunna; the plural of نَصّ.", "«ve naslar» — Kur'ân ve Sünnet; نَصّ'ın çoğulu.", wa="isti", tags=["jam-taksir"]),
  PREP("عَلَى", "ala", "«on».", "«üzere»."),
  ENC("ظَوَاهِرِهَا", "zahir", "«their apparent meanings» — the jarr phrase is the khabar: «are to be carried on their apparent sense».", "«zâhirleri» — câr-mecrûr haberdir: «zâhir mânâları üzere taşınır».", "اسْمٌ مَجْرُورٌ بِـ«عَلَى» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ (جَمْعٌ عَلَى فَوَاعِلَ، جُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ)", pr="هَا", att="مَحْذُوفٍ خَبَرٌ، أَيْ: مَحْمُولَةٌ عَلَى ظَوَاهِرِهَا", tags=["jam-taksir", "mamnu-min-sarf", "zarf-mustaqarr-wa-laghw"], punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "So turning away from them to meanings the people of the «inner sense» claim is heresy.",
 "tr": "Onlardan, bâtın ehlinin iddia ettiği mânâlara sapmak ilhâddır."},
 "tokens": [
  W("فَالْعُدُولُ", "udul", "noun", ["mubtada-khabar", "masdar"], "الْفَاءُ لِلتَّفْرِيعِ، وَ«الْعُدُولُ» مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«so turning away» — a consequence of the rule just stated.", "«o hâlde sapmak» — az önce konan kuralın bir sonucu.", segments=[seg("فَ", "fa", "conj"), seg("الْعُدُولُ", "udul", "noun")]),
  PRON_J("عَنْهَا", "عَنْ", "«from them».", "«onlardan».", "«الْعُدُولُ»"),
  PREP("إِلَى", "ila", "«to».", "«-e»."),
  W("مَعَانٍ", "mana", "noun", ["mahall-al-majrur", "huruf-jarr", "ism-maqsur-manqus", "mamnu-min-sarf"], "اسْمٌ مَجْرُورٌ بِـ«إِلَى» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ الْمَحْذُوفَةِ، وَالتَّنْوِينُ لِلْعِوَضِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ مَنْقُوصَةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«الْعُدُولُ».", "«meanings» — a diptote plural that is also manqūṣ: its yāʾ falls and the tanwīn stands in for it.", "«mânâlar» — hem gayr-i munsarif hem mankûs çoğul: yâ düşer, tenvin yerine geçer."),
  W("يَدَّعِيهَا", "iddaa", "verb", ["jumla-sifa", "form-viii-verbs", "al-bariz-al-muttasil"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَ«هَا» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ «أَهْلُ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«مَعَانٍ».", "«(which) … claim» — the sentence describes the indefinite مَعَانٍ.", "«iddia ettiği» — cümle, nekre مَعَانٍ'nin sıfatıdır.", segments=[seg("يَدَّعِي", "iddaa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  FAIL("أَهْلُ", "ahl", "«the people of».", "«ehli».", mudaf=True),
  MUDI("الْبَاطِنِ", "batin", "«the inner sense» — the Bāṭiniyya, who read every text as a cipher.", "«bâtın» — her nassı şifre gibi okuyan Bâtıniyye."),
  KHA("إِلْحَادٌ", "ilhad", "«is heresy» — literally a swerving from the straight way.", "«ilhâddır» — kelime anlamıyla doğru yoldan sapma.", of="الْعُدُولُ", punct=".", tags=["masdar", "form-iv-verbs"])]})
S.append({"id": "s3", "translation": {"en": "And rejecting the texts is unbelief.", "tr": "Nasları reddetmek küfürdür."},
 "tokens": [MUB("وَرَدُّ", "radd", "«and rejecting».", "«ve reddetmek».", wa="isti", mudaf=True, tags=["masdar"]), MUDI("النُّصُوصِ", "nass", "«the texts».", "«nasları».", tags=["jam-taksir"]), KUFR()]})
S.append({"id": "s4", "translation": {"en": "And deeming a sin lawful is unbelief.", "tr": "Günahı helâl saymak küfürdür."},
 "tokens": [MUB("وَاسْتِحْلَالُ", "istihlal-lawful", "«and deeming lawful».", "«ve helâl saymak».", wa="atf", mudaf=True, tags=["masdar", "form-x-verbs"]), MUDI("الْمَعْصِيَةِ", "masiya", "«the sin».", "«günahı»."), KUFR()]})
S.append({"id": "s5", "translation": {"en": "And making light of it is unbelief.", "tr": "Onu hafife almak küfürdür."},
 "tokens": [MUB("وَالِاسْتِهَانَةُ", "istihana", "«and making light» — the masdar of Form X from هَانَ.", "«ve hafife almak» — هَانَ'den istif'âl masdarı.", wa="atf", tags=["masdar", "form-x-verbs"]), PRON_J("بِهَا", "بِ", "«of it» — of the sin.", "«onu» — günahı.", "«الِاسْتِهَانَةُ»"), KUFR()]})
S.append({"id": "s6", "translation": {"en": "And mocking the Sharia is unbelief.", "tr": "Şeriatla alay etmek küfürdür."},
 "tokens": [MUB("وَالِاسْتِهْزَاءُ", "istihza", "«and mocking».", "«ve alay etmek».", wa="atf", tags=["masdar", "form-x-verbs", "ism-mamdud"]), PREP("عَلَى", "ala", "«at».", "«ile»."), MAJ("الشَّرِيعَةِ", "sharia", "«the Sharia».", "«şeriat».", "عَلَى", "«الِاسْتِهْزَاءُ»"), KUFR()]})
S.append({"id": "s7", "translation": {"en": "And despair of God the Exalted is unbelief, and feeling safe from God the Exalted is unbelief.", "tr": "Allah Teâlâ'dan ümit kesmek küfürdür; Allah Teâlâ'dan emin olmak küfürdür."},
 "tokens": [MUB("وَالْيَأْسُ", "yas", "«and despair».", "«ve ümit kesmek».", wa="atf"), W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of».", "«-den»."), MAJ("اللهِ", "allah", "«God».", "«Allah'tan».", "مِنَ", "«الْيَأْسُ»", pos="propn"), TAALA(), KUFR(punct="،"),
            MUB("وَالْأَمْنُ", "amn", "«and feeling safe» — from His plan.", "«ve emin olmak» — O'nun mekrinden.", wa="atf"), W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of».", "«-den»."), MAJ("اللهِ", "allah", "«God».", "«Allah'tan».", "مِنَ", "«الْأَمْنُ»", pos="propn"), TAALA(), KUFR()]})
S.append({"id": "s8", "translation": {"en": "And believing a soothsayer in what he tells of the unseen is unbelief.", "tr": "Kâhini gaybdan haber verdiği şeyde tasdik etmek küfürdür."},
 "tokens": [
  MUB("وَتَصْدِيقُ", "tasdiq", "«and believing» — the masdar annexed to its object.", "«ve tasdik etmek» — mef'ûlüne muzâf masdar.", wa="atf", mudaf=True, tags=["masdar", "imal-al-masdar"]),
  MUDI("الْكَاهِنِ", "kahin", "«the soothsayer».", "«kâhini»."),
  W("بِمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "mahall-al-majrur"], "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«تَصْدِيقُ».", "«in what».", "«… şeyde».", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("يُخْبِرُهُ", "akhbara", "verb", ["form-iv-verbs", "ism-mawsul", "al-bariz-al-muttasil"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ (الْكَاهِنُ)، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: يُخْبِرُهُ بِهِ.", "«he tells him» — the ṣila; the returning pronoun to مَا is dropped.", "«ona haber verir» — sıla; مَا'ya dönen âid hazfedilmiştir.", segments=[seg("يُخْبِرُ", "akhbara", "verb"), seg("هُ", "pron-3ms", "pron")]),
  PREP("عَنِ", "an", "«of».", "«-den»."),
  MAJ("الْغَيْبِ", "ghayb", "«the unseen».", "«gayb».", "عَنِ", "«يُخْبِرُهُ»"),
  KUFR()]})

CAND = {
 "udul": need("udul", "عُدُول", "ع د ل", "noun", "turning away, deviating (masdar of عَدَلَ عَنْ)", "sapma, dönme (عَدَلَ عَنْ'in masdarı)", 4),
 "batin": need("batin", "بَاطِن", "ب ط ن", "noun", "inner, hidden; the inner sense", "bâtın, iç, gizli mânâ", 3),
 "ilhad": need("ilhad", "إِلْحَاد", "ل ح د", "noun", "heresy, deviation from the straight way (masdar of Form IV)", "ilhâd, doğru yoldan sapma (if'âl masdarı)", 4),
 "masiya": need("masiya", "مَعْصِيَة", "ع ص ي", "noun", "a sin, disobedience", "günah, isyan", 2, plural="مَعَاصٍ"),
 "istihana": need("istihana", "اسْتِهَانَة", "ه و ن", "noun", "making light of, belittling (masdar of Form X)", "hafife alma, küçümseme (istif'âl masdarı)", 4),
 "kahin": need("kahin", "كَاهِن", "ك ه ن", "noun", "a soothsayer, a diviner", "kâhin", 3, plural="كُهَّان"),
}
ADD_EN = " Chapter 43 (matn line 83): the texts on their apparent meanings, the Bāṭinī turning-away as heresy, and the eight sentences on what is unbelief."
ADD_TR = " Kırk üçüncü bâb (matn satırı 83): naslar zâhirleri üzeredir, Bâtınî sapma ilhâddır ve neyin küfür olduğuna dair sekiz cümle."
finish(43, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 43 (matn line 83)")
