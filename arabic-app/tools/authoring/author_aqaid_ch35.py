# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 35: the pain after a blow and the breaking after a strike are God's creation, with no making by the servant.
Source: matn line 43.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch35.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْأَلَمُ عَقِيبَ الضَّرْبِ", "en": "The Pain That Follows the Blow", "tr": "Vurmanın Ardından Gelen Acı"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And the pain that is found in the one struck after a man's striking, and the breaking in the glass after a man's breaking, and whatever is like it — all of that is created by God the Exalted.",
 "tr": "Bir insanın vurmasının ardından vurulanda bulunan acı, bir insanın kırmasının ardından camda bulunan kırılma ve bunlara benzeyen her şey — bunların hepsi Allah Teâlâ'nın yaratmasıdır."},
 "tokens": [
  MAWSUL("وَمَا", "ma-mawsula", "«and what» — the mubtada; its khabar is the whole sentence كُلُّ ذَلِكَ مَخْلُوقٌ, tied back by the demonstrative.", "«ve her ne ki» — mübteda; haberi, ism-i işâretle ona bağlanan كُلُّ ذَلِكَ مَخْلُوقٌ cümlesidir.", "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَةُ «كُلُّ ذَلِكَ مَخْلُوقٌ»، وَالرَّابِطُ اسْمُ الْإِشَارَةِ", wa="isti", tags=["mubtada-khabar", "anwa-al-khabar"]),
  W("يُوجَدُ", "wajada", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "ism-mawsul", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«is found» — the ṣila of مَا.", "«bulunur» — مَا'nın sılası."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of» — min of explanation, its nūn vowelled before the article.", "«-den» — beyân min'i; nûnu elif-lâm önünde harekelenir."),
  MAJ("الْأَلَمِ", "alam-pain", "«pain» — explaining what «it» is.", "«acı» — «o»nun ne olduğunu açıklar.", "مِنَ", "مَحْذُوفٍ حَالٌ مِنَ الضَّمِيرِ فِي «يُوجَدُ»", tags=["hal"]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("الْمَضْرُوبِ", "madrub", "«the one struck» — the ism mafʿūl of ضَرَبَ.", "«vurulan» — ضَرَبَ'nin ism-i mef'ûlü.", "فِي", "«يُوجَدُ»", tags=["ism-maful"]),
  W("عَقِيبَ", "aqiba-after", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ مُتَعَلِّقٌ بِـ«يُوجَدُ»، وَهُوَ مُضَافٌ.", "«right after» — a ẓarf of time, annexed to a masdar.", "«hemen ardından» — masdara muzâf zaman zarfı."),
  MUDI("ضَرْبِ", "darb", "«the striking of» — a masdar annexed to its doer.", "«vurması» — fâiline muzâf masdar.", mudaf=True, tags=["masdar", "imal-al-masdar"]),
  MUDI("إِنْسَانٍ", "insan", "«a man».", "«bir insanın».", punct="،"),
  W("وَالِانْكِسَارِ", "inkisar", "noun", ["atf-nasaq", "masdar", "form-vii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَ«الِانْكِسَارِ» مَعْطُوفٌ عَلَى «الْأَلَمِ» تَابِعٌ لَهُ فِي الْجَرِّ.", "«and the breaking» — the masdar of Form VII, the form of being acted upon.", "«ve kırılma» — mutâvaat bildiren infiâl bâbının masdarı.", segments=[seg("وَ", "wa", "conj"), seg("الِانْكِسَارِ", "inkisar", "noun")]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("الزُّجَاجِ", "zujaj", "«the glass».", "«camda».", "فِي", "«الِانْكِسَارِ»"),
  W("عَقِيبَ", "aqiba-after", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِـ«الِانْكِسَارِ»، وَهُوَ مُضَافٌ.", "«right after».", "«hemen ardından»."),
  MUDI("كَسْرِ", "kasr", "«the breaking of» — the transitive masdar, against the intransitive انْكِسَار.", "«kırması» — geçişli masdar; geçişsiz انْكِسَار'ın karşısında.", mudaf=True, tags=["masdar"]),
  MUDI("إِنْسَانٍ", "insan", "«a man».", "«bir insanın».", punct="،"),
  MAWSUL("وَمَا", "ma-mawsula", "«and whatever».", "«ve her ne ki».", "مَعْطُوفٌ عَلَى «مَا» الْأُولَى فِي مَحَلِّ رَفْعٍ", wa="atf"),
  W("أَشْبَهَهُ", "ashbaha", "verb", ["form-iv-verbs", "ism-mawsul", "al-bariz-al-muttasil"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«is like it» — Form IV with its object pronoun.", "«ona benzer» — mef'ûl zamirli if'âl bâbı.", punct="،", segments=[seg("أَشْبَهَ", "ashbaha", "verb"), seg("هُ", "pron-3ms", "pron")]),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ، وَهُوَ مُضَافٌ.", "«all of» — the second mubtada, summing the three.", "«hepsi» — üçünü toplayan ikinci mübteda."),
  ISHARA("ذَلِكَ", "dhalika", "«that» — the pronoun that ties the khabar-sentence to مَا.", "«bu» — haber cümlesini مَا'ya bağlayan zamir.", "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", tags=["idafa-definiteness"]),
  KHA("مَخْلُوقٌ", "makhluq", "«is created».", "«yaratılmıştır».", of="كُلُّ", tags=["ism-maful"]),
  FUSED("لِلهِ", "لِ", "allah", "«by God» — the lām of the creator.", "«Allah tarafından» — yaratıcı lâmı.", "«مَخْلُوقٌ»", inner="اللهِ", pos="propn"),
  TAALA(punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "The servant has no making in creating it.",
 "tr": "Onu yaratmada kulun hiçbir sun'u yoktur."},
 "tokens": [
  LAJINS(),
  W("صُنْعَ", "sun", "noun", ["la-nafiya-lil-jins"], "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«making» — the ism of lā, built on the fatḥa.", "«sun', yapma» — lâ'nın fetha üzere mebnî ismi."),
  FUSED("لِلْعَبْدِ", "لِ", "abd", "«the servant has» — the jarr phrase is lā's khabar.", "«kulun» — câr-mecrûr lâ'nın haberidir.", "مَحْذُوفٍ خَبَرُ «لَا»", inner="الْعَبْدِ", tags=["la-nafiya-lil-jins"]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  ENC("تَخْلِيقِهِ", "takhliq", "«creating it».", "«onu yaratmada».", "اسْمٌ مَجْرُورٌ بِـ«فِي» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", att="«صُنْعَ»", punct=".", tags=["masdar"])]})

CAND = {
 "alam-pain": need("alam-pain", "أَلَم", "أ ل م", "noun", "pain", "acı, elem", 3, plural="آلَام"),
 "aqiba-after": need("aqiba-after", "عَقِيبَ", "ع ق ب", "noun", "right after, immediately following (a ẓarf of time)", "hemen ardından, akabinde (zaman zarfı)", 4),
}
ADD_EN = " Chapter 35 (matn line 43): the pain after a blow and the breaking after a strike are created by God, with no making by the servant."
ADD_TR = " Otuz beşinci bâb (matn satırı 43): vurmanın ardındaki acı ve kırmanın ardındaki kırılma Allah'ın yaratmasıdır; kulun sun'u yoktur."
finish(35, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 35 (matn line 43)")
