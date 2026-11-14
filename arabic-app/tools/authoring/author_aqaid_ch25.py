# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 25: the creed's opening — the realities of things are established, and the five senses.
Source: research/sources/aqaid-nasafi-matn-full.txt lines 15-21 (قال أهل الحق … وبكل حاسة منها يوقف على ما وضعت هي له);
the span وأسباب العلم للخلق ثلاثة between them is already chapter 2 s2. Received vowelling (the Taftazani sharh tradition).
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch25.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "حَقَائِقُ الْأَشْيَاءِ وَالْحَوَاسُّ الْخَمْسُ", "en": "The Realities of Things, and the Five Senses", "tr": "Eşyanın Hakikatleri ve Beş Duyu"}
S = []
S.append({"id": "s1", "translation": {
 "en": "The people of the truth said: the realities of things are established, and knowledge of them is attained — contrary to the Sophists.",
 "tr": "Ehl-i hak dedi ki: eşyanın hakikatleri sabittir ve onlara dair ilim mütehakkıktır — Sofistlerin hilâfına."},
 "tokens": [
  MAZI("قَالَ", "qala", "«said» — the matn opens with the voice of Ahl al-Sunna.", "«dedi» — matn, Ehl-i Sünnet'in sesiyle açılır.", "وَالْفَاعِلُ «أَهْلُ»", tags=["fail"]),
  W("أَهْلُ", "ahl", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ، وَهُوَ مُضَافٌ.", "«the people of».", "«ehli»."),
  MUDI("الْحَقِّ", "haqq", "«the truth» — the people of the truth are Ahl al-Sunna wa-l-Jamāʿa.", "«hak» — ehl-i hak, Ehl-i Sünnet ve'l-Cemâat'tir.", punct=":"),
  MUB("حَقَائِقُ", "haqaiq", "«the realities of» — the mubtada of the quoted creed's first sentence; the whole sentence is what was said (maqūl al-qawl).", "«hakikatleri» — nakledilen akidenin ilk cümlesinin mübtedası; cümlenin bütünü makûlü'l-kavldir.", mudaf=True, tags=["jam-taksir"], extra="؛ وَالْجُمْلَةُ مَقُولُ الْقَوْلِ فِي مَحَلِّ نَصْبٍ"),
  MUDI("الْأَشْيَاءِ", "shay", "«things» — the broken plural of شَيْء.", "«eşyanın» — شَيْء'in cemi teksîri.", tags=["jam-taksir"]),
  KHA("ثَابِتَةٌ", "thabit", "«are established» — the khabar agrees with a broken plural of non-rational things in the feminine singular.", "«sabittir» — haber, gayr-i âkil cemi teksîr olan mübtedaya müfred müennes olarak uyar.", punct="،", tags=["al-jumu-wa-tanith-amiliha"]),
  MUB("وَالْعِلْمُ", "ilm", "«and knowledge» — a second sentence joined to the first.", "«ve ilim» — birinciye atfedilen ikinci bir cümle.", wa="atf"),
  PRON_J("بِهَا", "بِ", "«of them» — the jarr phrase hangs on الْعِلْمُ, a masdar with a verb's reach.", "«onlara dair» — câr-mecrûr, fiil kuvvetindeki masdar الْعِلْمُ'e müteallıktır.", "«الْعِلْمُ»", tags=["zarf-mustaqarr-wa-laghw"]),
  KHA("مُتَحَقِّقٌ", "mutahaqqiq", "«is attained» — the ism fāʿil of Form V as the khabar.", "«mütehakkıktır» — tefe'ul bâbının ism-i fâili haber olarak.", tags=["ism-fail", "form-v-verbs"]),
  W("خِلَافًا", "khilaf", "noun", ["maful-mutlaq", "hadhf-wa-taqdir"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ، أَيْ: نُخَالِفُ خِلَافًا، مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«contrary to» — the absolute object of a dropped verb: «we differ, a differing …».", "«hilâfına» — hazfedilmiş bir fiilin mef'ûl-i mutlakı: «muhalefet ederiz, bir muhalefet ki …»."),
  FUSED("لِلسُّوفِسْطَائِيَّةِ", "لِ", "sufistaiyya", "«to the Sophists» — the lām swallows the article's alif: لِ + السُّوفِسْطَائِيَّة; the nisba to the Greek sophistai.", "«Sofistlere» — lâm, elif-lâmın elifini yutar: لِ + السُّوفِسْطَائِيَّة; Yunanca sophistai'ye nispet.", "«خِلَافًا»", punct=".", inner="السُّوفِسْطَائِيَّةِ", tags=["anwa-al-lam-al-tarif", "ism-mansub"])]})
S.append({"id": "s2", "translation": {
 "en": "So the senses are five: hearing, sight, smell, touch and taste.",
 "tr": "Duyular beştir: işitme, görme, koklama, dokunma ve tatma."},
 "tokens": [
  MUB("فَالْحَوَاسُّ", "hawass", "«so the senses» — the fāʾ opens the detail of the three causes of knowledge (chapter 2).", "«duyular ise» — fâ, ilmin üç sebebinin (2. bâb) tafsiline girer.", wa="fa-tafsil", tags=["jam-taksir"]),
  KHA("خَمْسٌ", "khams", "«are five» — the number of a feminine counted noun (حَاسَّة) stands without the tāʾ.", "«beştir» — müennes ma'dûdun (حَاسَّة) sayısı tâ'sız gelir.", punct=":", tags=["asma-al-adad-fil-kafiya"]),
  BADAL("السَّمْعُ", "sam", "«hearing» — the first of the five, a badal of detail from خَمْسٌ.", "«işitme» — beşin ilki, خَمْسٌ'ten tafsil bedeli.", "خَمْسٌ", "raf", extra=" (بَدَلُ تَفْصِيلٍ)"),
  ATF("وَالْبَصَرُ", "basar", "«sight».", "«görme».", "السَّمْعُ", "raf"),
  ATF("وَالشَّمُّ", "shamm", "«smell».", "«koklama».", "السَّمْعُ", "raf"),
  ATF("وَاللَّمْسُ", "lams", "«touch».", "«dokunma».", "السَّمْعُ", "raf"),
  ATF("وَالذَّوْقُ", "dhawq", "«taste».", "«tatma».", "السَّمْعُ", "raf", punct=".")]})
S.append({"id": "s3", "translation": {
 "en": "And by every one of these senses one comes to know that for which it was made.",
 "tr": "Ve bu duyuların her biriyle, o duyunun kendisi için konulduğu şeye vâkıf olunur."},
 "tokens": [
  FUSED("وَبِكُلِّ", "بِ", "kull", "«and by every» — the jarr phrase is put first; it hangs on يُوقَفُ.", "«ve her … ile» — câr-mecrûr öne alınmıştır; يُوقَفُ'ya müteallıktır.", "«يُوقَفُ»", wa="isti", mudaf=True, inner="كُلِّ", tags=["taqdim-al-musnad"]),
  MUDI("حَاسَّةٍ", "hassa", "«sense».", "«duyu»."),
  PRON_J("مِنْهَا", "مِنْ", "«of them» — a jarr phrase after an indefinite noun is its description.", "«onlardan» — nekre isimden sonra gelen câr-mecrûr onun sıfatıdır.", None, extra="، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«حَاسَّةٍ»", tags=["naat-sifa", "jumla-sifa"]),
  W("يُوقَفُ", "waqafa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «عَلَى مَا».", "«one comes to know» — a passive whose deputy doer is the jarr phrase عَلَى مَا; وَقَفَ عَلَى الشَّيْءِ is «to come upon, to know» it.", "«vâkıf olunur» — nâib-i fâili câr-mecrûr عَلَى مَا olan meçhul; وَقَفَ عَلَى الشَّيْءِ «bir şeye vâkıf olmak, bilmek»tir."),
  PREP("عَلَى", "ala", "«upon».", "«üzerine»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "naib-al-fail", "mahall-al-majrur"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِـ«عَلَى»، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«that which» — the relative in jarr; the phrase stands as the deputy doer.", "«o şey ki» — mecrûr ism-i mevsûl; câr-mecrûr nâib-i fâil yerindedir."),
  W("وُضِعَتْ", "wadaa", "verb", ["naib-al-fail", "ism-mawsul", "al-majhul-fil-kafiya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.", "«it was made» — the passive with the tāʾ of the feminine; the ṣila of مَا.", "«konulmuştur» — tenis tâ'lı meçhul; مَا'nın sılası."),
  W("هِيَ", "pron-3fs-munfasil", "pron", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ فِي «وُضِعَتْ».", "«it (itself)» — a detached pronoun confirming the hidden deputy doer; a hidden pronoun is confirmed only by a detached one.", "«o (bizzat)» — gizli nâib-i fâili pekiştiren munfasıl zamir; gizli zamir ancak munfasıl zamirle tekid edilir."),
  PRON_J("لَهُ", "لِ", "«for it» — the returning pronoun (ʿāʾid) of مَا.", "«onun için» — مَا'nın âidi.", "«وُضِعَتْ»", punct=".")]})

CAND = {
 "haqaiq": need("haqaiq", "حَقَائِق", "ح ق ق", "noun", "realities, true natures (pl. of حَقِيقَة)", "hakikatler, mahiyetler (حَقِيقَة'nin çoğulu)", 4),
 "mutahaqqiq": need("mutahaqqiq", "مُتَحَقِّق", "ح ق ق", "noun", "attained, realised, certain (ism fāʿil of Form V)", "mütehakkık, gerçekleşmiş, sabit (tefe'ul ism-i fâili)", 4),
 "khilaf": need("khilaf", "خِلَاف", "خ ل ف", "noun", "difference, disagreement; خِلَافًا لِـ: contrary to", "hilâf, ayrılık; خِلَافًا لِـ: hilâfına", 3),
 "sufistaiyya": need("sufistaiyya", "السُّوفِسْطَائِيَّة", "س و ف س ط", "noun", "the Sophists — those who deny that realities are established or knowable", "Sofistler — hakikatlerin sabit ya da bilinebilir olduğunu inkâr edenler", 5),
 "shamm": need("shamm", "شَمّ", "ش م م", "noun", "smell, the sense of smelling (masdar)", "koklama, koku alma duyusu (masdar)", 2),
 "lams": need("lams", "لَمْس", "ل م س", "noun", "touch, the sense of touching (masdar)", "dokunma, dokunma duyusu (masdar)", 2),
 "hassa": need("hassa", "حَاسَّة", "ح س س", "noun", "a sense, a faculty of perception", "duyu, his", 3, plural="حَوَاسّ"),
}
ADD_EN = (" Chapter 25 (matn lines 15-21): the creed's opening — قَالَ أَهْلُ الْحَقِّ with the realities of things, then the five senses and"
          " what each is for; the sentence وَأَسْبَابُ الْعِلْمِ between them is chapter 2. Vowelled to the received text (the Taftāzānī sharḥ tradition).")
ADD_TR = (" Yirmi beşinci bâb (matn satırları 15-21): akidenin açılışı — قَالَ أَهْلُ الْحَقِّ ile eşyanın hakikatleri, sonra beş duyu ve her birinin"
          " neye konulduğu; aradaki وَأَسْبَابُ الْعِلْمِ cümlesi ikinci bâbdır. Alınan metne (Teftâzânî şerhi geleneği) göre harekelenmiştir.")
finish(25, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 25 (matn lines 15-21)")
