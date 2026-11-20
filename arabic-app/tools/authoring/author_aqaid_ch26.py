# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 26: the two kinds of true report — the mutawātir as a cause of necessary knowledge, and the
Messenger's report confirmed by the miracle. Source: matn lines 23-25 (وهو موجب للعلم الضروري … في التيقن والثبات);
the definition of the mutawātir before it is chapter 2 s3.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch26.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "نَوْعَا الْخَبَرِ الصَّادِقِ", "en": "The Two Kinds of True Report", "tr": "Sâdık Haberin İki Nev'i"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And it (the mutawātir report) necessitates necessary knowledge — like the knowledge of the bygone kings in past ages and of far-off lands.",
 "tr": "Ve o (mütevâtir haber), zarûrî ilmi gerektirir — geçmiş zamanlardaki gelip geçmiş hükümdarları ve uzak beldeleri bilmek gibi."},
 "tokens": [
  HUWA("وَهُوَ", "«and it» — the mutawātir report just defined.", "«ve o» — az önce tarif edilen mütevâtir haber.", wa="atf"),
  KHA("مُوجِبٌ", "mujib", "«necessitates» — the ism fāʿil of Form IV (أَوْجَبَ) as khabar, governing a jarr phrase like its verb.", "«gerektirir» — if'âl bâbının (أَوْجَبَ) ism-i fâili haber olarak; fiili gibi câr-mecrûra amel eder.", tags=["ism-fail", "form-iv-verbs", "shurut-amal-ism-al-fail"]),
  FUSED("لِلْعِلْمِ", "لِ", "ilm", "«knowledge» — the object of the ism fāʿil, reached through the lām.", "«ilmi» — ism-i fâilin lâm ile ulaştığı mef'ûlü.", "«مُوجِبٌ»", inner="الْعِلْمِ"),
  NAT("الضَّرُورِيِّ", "daruri", "«necessary» — knowledge that comes without reasoning and cannot be pushed away.", "«zarûrî» — istidlâlsiz gelen ve def'i mümkün olmayan ilim.", "الْعِلْمِ", "jarr", punct="،", tags=["ism-mansub"]),
  FUSED("كَالْعِلْمِ", "كَ", "ilm", "«like the knowledge» — the kāf of likeness; the phrase hangs on a dropped khabar: «and that is like …».", "«bilmek gibi» — teşbih kâfı; câr-mecrûr hazfedilmiş bir habere bağlıdır: «o da … gibidir».", "مَحْذُوفٍ، أَيْ: وَذَلِكَ كَائِنٌ كَالْعِلْمِ", inner="الْعِلْمِ", meaning=" لِلتَّشْبِيهِ", tags=["hadhf-wa-taqdir"]),
  FUSED("بِالْمُلُوكِ", "بِ", "malik-king", "«of the kings» — the masdar's object through the bāʾ; مُلُوك is the broken plural of مَلِك.", "«hükümdarları» — masdarın bâ ile mef'ûlü; مُلُوك, مَلِك'in cemi teksîri.", "«الْعِلْمِ»", inner="الْمُلُوكِ", tags=["jam-taksir"]),
  NAT("الْخَالِيَةِ", "khali", "«bygone» — a manqūṣ noun (خَالٍ) in its feminine, where the yāʾ comes back.", "«gelip geçmiş» — mankûs ismin (خَالٍ) müennesi; yâ geri gelir.", "الْمُلُوكِ", "jarr", tags=["ism-fail", "ism-maqsur-manqus", "al-jumu-wa-tanith-amiliha"]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("الْأَزْمِنَةِ", "zaman", "«ages» — the plural of زَمَان.", "«zamanlar» — زَمَان'ın çoğulu.", "فِي", "«الْخَالِيَةِ»", tags=["jam-taksir"]),
  NAT("الْمَاضِيَةِ", "madi", "«past».", "«geçmiş».", "الْأَزْمِنَةِ", "jarr", tags=["ism-fail", "ism-maqsur-manqus"]),
  ATF("وَالْبُلْدَانِ", "balad", "«and the lands» — joined to الْمُلُوكِ, not to الْأَزْمِنَةِ: knowledge OF far lands, not knowledge IN them.", "«ve beldeler» — الْأَزْمِنَةِ'ye değil الْمُلُوكِ'e atfedilir: uzak beldeleri BİLMEK, onların İÇİNDE bilmek değil.", "الْمُلُوكِ", "jarr", tags=["jam-taksir"]),
  NAT("النَّائِيَةِ", "nai", "«far-off» — from نَأَى «to be distant»; the feminine of the manqūṣ نَاءٍ.", "«uzak» — نَأَى «uzak olmak»tan; mankûs نَاءٍ'nin müennesi.", "الْبُلْدَانِ", "jarr", punct=".", tags=["ism-fail", "ism-maqsur-manqus"])]})
S.append({"id": "s2", "translation": {
 "en": "And the second kind is the report of the Messenger confirmed by the miracle, and it necessitates inferential knowledge.",
 "tr": "İkinci nev', mûcize ile teyit edilmiş Resûl'ün haberidir; o, istidlâlî ilmi gerektirir."},
 "tokens": [
  MUB("وَالنَّوْعُ", "naw", "«and the kind».", "«ve nev'».", wa="isti"),
  NAT("الثَّانِي", "thani", "«second» — a definite manqūṣ: the ḍamma is estimated on the yāʾ, too heavy to show.", "«ikinci» — marife mankûs: damme yâ üzerinde takdirîdir, ağırlığından gösterilmez.", "النَّوْعُ", "raf", tags=["ism-maqsur-manqus"], extra=" الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  KHA("خَبَرُ", "khabar", "«the report of».", "«haberi».", mudaf=True),
  MUDI("الرَّسُولِ", "rasul", "«the Messenger».", "«Resûl'ün»."),
  NAT("الْمُؤَيَّدِ", "muayyad", "«confirmed» — the ism mafʿūl of Form II (أَيَّدَ); its agent is reached by the bāʾ.", "«teyit edilmiş» — tef'îl bâbının (أَيَّدَ) ism-i mef'ûlü; fâili bâ ile gelir.", "الرَّسُولِ", "jarr", tags=["ism-maful", "form-ii-verbs"]),
  FUSED("بِالْمُعْجِزَةِ", "بِ", "mujiza", "«by the miracle».", "«mûcize ile».", "«الْمُؤَيَّدِ»", inner="الْمُعْجِزَةِ", punct="،"),
  HUWA("وَهُوَ", "«and it».", "«ve o».", wa="atf"),
  MUDA("يُوجِبُ", "awjaba", "«necessitates» — Form IV; the verbal sentence is the khabar.", "«gerektirir» — if'âl bâbı; fiil cümlesi haberdir.", HIDDEN_HUWA + "، وَالْجُمْلَةُ خَبَرُ «هُوَ»", tags=["form-iv-verbs", "anwa-al-khabar"]),
  MAFUL("الْعِلْمَ", "ilm", "«knowledge».", "«ilmi».", "يُوجِبُ"),
  NAT("الِاسْتِدْلَالِيَّ", "istidlali", "«inferential» — the nisba of اسْتِدْلَال, the masdar of Form X.", "«istidlâlî» — istif'âl masdarı اسْتِدْلَال'a nispet.", "الْعِلْمَ", "nasb", punct=".", tags=["ism-mansub"])]})
S.append({"id": "s3", "translation": {
 "en": "And the knowledge established by it resembles the knowledge established by necessity in certainty and firmness.",
 "tr": "Onunla sabit olan ilim, yakîn ve sebatta zarûretle sabit olan ilme denktir."},
 "tokens": [
  MUB("وَالْعِلْمُ", "ilm", "«and the knowledge».", "«ve ilim».", wa="isti"),
  NAT("الثَّابِتُ", "thabit", "«established».", "«sabit olan».", "الْعِلْمُ", "raf", tags=["ism-fail"]),
  PRON_J("بِهِ", "بِ", "«by it» — by the Messenger's report.", "«onunla» — Resûl'ün haberiyle.", "«الثَّابِتُ»"),
  MUDA("يُضَاهِي", "dahaa", "«resembles» — Form III of a defective root; the yāʾ carries an estimated ḍamma.", "«denktir, benzer» — nâkıs kökün müfâale bâbı; yâ üzerinde takdirî damme.", HIDDEN_HUWA + "، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ", tags=["form-iii-verbs", "naqis-verbs", "anwa-al-khabar"], sign="الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  MAFUL("الْعِلْمَ", "ilm", "«the knowledge».", "«ilme».", "يُضَاهِي"),
  NAT("الثَّابِتَ", "thabit", "«established».", "«sabit olan».", "الْعِلْمَ", "nasb", tags=["ism-fail"]),
  FUSED("بِالضَّرُورَةِ", "بِ", "darura", "«by necessity».", "«zarûretle».", "«الثَّابِتَ»", inner="الضَّرُورَةِ"),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("التَّيَقُّنِ", "tayaqqun", "«certainty» — the masdar of Form V.", "«yakîn, kesinlik» — tefe'ul masdarı.", "فِي", "«يُضَاهِي»", tags=["masdar", "form-v-verbs"]),
  ATF("وَالثَّبَاتِ", "thabat", "«and firmness».", "«ve sebat».", "التَّيَقُّنِ", "jarr", punct=".", tags=["masdar"])]})

CAND = {
 "daruri": need("daruri", "ضَرُورِيّ", "ض ر ر", "noun", "necessary, self-evident (of knowledge: reached without reasoning)", "zarûrî, bedîhî (ilim için: istidlâlsiz hâsıl olan)", 4),
 "khali": need("khali", "خَالٍ", "خ ل و", "noun", "bygone, past; empty", "gelip geçmiş; boş", 3),
 "madi": need("madi", "الْمَاضِي", "م ض ي", "noun", "past, bygone", "geçmiş", 2),
 "nai": need("nai", "نَاءٍ", "ن أ ي", "noun", "far-off, remote (ism fāʿil of نَأَى)", "uzak (نَأَى'nın ism-i fâili)", 4),
 "muayyad": need("muayyad", "مُؤَيَّد", "أ ي د", "noun", "confirmed, supported (ism mafʿūl of Form II)", "teyit edilmiş, desteklenmiş (tef'îl ism-i mef'ûlü)", 4),
 "istidlali": need("istidlali", "اسْتِدْلَالِيّ", "د ل ل", "noun", "inferential, reached by reasoning", "istidlâlî, akıl yürütmeyle elde edilen", 4),
 "dahaa": need("dahaa", "ضَاهَى", "ض ه ي", "verb", "to resemble, to be on a par with", "benzemek, denk olmak", 5),
 "tayaqqun": need("tayaqqun", "تَيَقُّن", "ي ق ن", "noun", "certainty, being sure (masdar of Form V)", "yakîn, kesin olma (tefe'ul masdarı)", 4),
 "thabat": need("thabat", "ثَبَات", "ث ب ت", "noun", "firmness, steadiness (masdar)", "sebat, sağlamlık (masdar)", 3),
}
MORPH = {"dahaa": sarf.derived_naqis(sarf.B3 + " — نَاقِصٌ", W3, "ُ", "ضَاهَ", "ضَاه", "i", "ضَاه", "مُضَاهَاة", "مُضَاهٍ", "مُضَاهًى", "ضُوهِيَ", "يُضَاهَى",
                                     "ضَاهَى الشَّيْءَ يُضَاهِيهِ مُضَاهَاةً: شَابَهَهُ — مِنْ بَابِ الْمُفَاعَلَةِ، نَاقِصٌ يَائِيٌّ")}
ADD_EN = (" Chapter 26 (matn lines 23-25): the mutawātir as the cause of necessary knowledge, and the Messenger's report confirmed by the"
          " miracle; the definition of the mutawātir before it is chapter 2.")
ADD_TR = (" Yirmi altıncı bâb (matn satırları 23-25): zarûrî ilmin sebebi olarak mütevâtir ve mûcize ile teyit edilmiş Resûl haberi; öncesindeki"
          " mütevâtir tarifi ikinci bâbdır.")
finish(26, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 26 (matn lines 23-25)", morph=MORPH)
