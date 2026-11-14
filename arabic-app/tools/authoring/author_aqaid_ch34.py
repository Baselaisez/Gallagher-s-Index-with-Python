# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 34: the good and the ugly among the servants' acts, and what capability is. Source: matn lines 39-41
(والحسن منها برضاء الله تعالى … تعتمد هذه الاستطاعة); وَلِلْعِبَادِ أَفْعَالٌ اخْتِيَارِيَّةٌ, وَالِاسْتِطَاعَةُ مَعَ الْفِعْلِ and وَلَا يُكَلَّفُ الْعَبْدُ are chapter 7.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch34.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْحَسَنُ وَالْقَبِيحُ، وَحَقِيقَةُ الِاسْتِطَاعَةِ", "en": "The Good and the Ugly, and What Capability Is", "tr": "Hasen ile Kabîh ve İstitâatin Hakikati"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And the good among them is by God's good pleasure, and the ugly among them is not by His good pleasure.",
 "tr": "Onlardan hasen olan Allah Teâlâ'nın rızasıyladır; kabîh olan ise O'nun rızasıyla değildir."},
 "tokens": [
  MUB("وَالْحَسَنُ", "hasan-good", "«and the good» — of the servants' chosen acts (chapter 7).", "«ve hasen» — kulların ihtiyarî fiillerinden (7. bâb).", wa="isti", tags=["sifa-mushabbaha"]),
  PRON_J("مِنْهَا", "مِنْ", "«among them».", "«onlardan».", "مَحْذُوفٍ حَالٌ مِنَ «الْحَسَنُ»", tags=["hal"]),
  FUSED("بِرِضَاءِ", "بِ", "rida-pleasure", "«is by the good pleasure of» — the jarr phrase is the khabar: «comes about with God's pleasure».", "«rızasıyladır» — câr-mecrûr haberdir: «Allah'ın rızasıyla olur».", "مَحْذُوفٍ خَبَرٌ، أَيْ: كَائِنٌ بِرِضَاءِ اللهِ", mudaf=True, inner="رِضَاءِ", tags=["zarf-mustaqarr-wa-laghw", "ism-mamdud"]),
  MUDI("اللهِ", "allah", "«God».", "«Allah'ın».", pos="propn"),
  TAALA(punct="،"),
  MUB("وَالْقَبِيحُ", "qabih", "«and the ugly».", "«ve kabîh».", wa="atf", tags=["sifa-mushabbaha"]),
  PRON_J("مِنْهَا", "مِنْ", "«among them».", "«onlardan».", "مَحْذُوفٍ حَالٌ مِنَ «الْقَبِيحُ»", tags=["hal"]),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-afal-al-naqisa-fil-kafiya"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ.", "«is not».", "«değildir»."),
  ENC("بِرِضَاهُ", "rida-pleasure", "«by His good pleasure» — an extra bāʾ strengthens the negation; رِضَا is written here without its hamza, as the received text has it.", "«O'nun rızasıyla» — zâid bâ nefyi pekiştirir; رِضَا burada alınan metindeki gibi hemzesiz yazılır.", "«رِضَا» مَجْرُورٌ لَفْظًا بِالْبَاءِ الزَّائِدَةِ مَنْصُوبٌ مَحَلًّا خَبَرُ «لَيْسَ»، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ", pr="هُ", letter="بِ", tags=["huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha", "ism-maqsur-manqus"], punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And it is the true nature of the power by which the act comes to be.",
 "tr": "O (istitâat), fiilin kendisiyle meydana geldiği kudretin hakikatidir."},
 "tokens": [
  HUWA("وَهِيَ", "«and it» — capability (chapter 7: capability is with the act).", "«ve o» — istitâat (7. bâb: istitâat fiille beraberdir).", wa="atf", extra=" — أَيِ: الِاسْتِطَاعَةُ"),
  KHA("حَقِيقَةُ", "haqiqa", "«the true nature of».", "«hakikati».", mudaf=True),
  MUDI("الْقُدْرَةِ", "qudra", "«the power».", "«kudretin»."),
  MAWSUL("الَّتِي", "allati", "«by which» — the feminine relative, describing الْقُدْرَةِ.", "«ki onunla» — müennes ism-i mevsûl; الْقُدْرَةِ'nin sıfatı.", "فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«الْقُدْرَةِ»", tags=["naat-sifa"]),
  W("يَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "ism-mawsul", "mudari-marfu", "al-fil-al-tamm-wal-naqis"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.", "«comes to be» — here كَانَ is COMPLETE: «the act exists by it», not «the act is …».", "«meydana gelir» — burada كَانَ TÂMdır: «fiil onunla vâr olur», «fiil … -dır» değil."),
  PRON_J("بِهَا", "بِ", "«by it» — the returning pronoun of الَّتِي.", "«onunla» — الَّتِي'nin âidi.", "«يَكُونُ»"),
  FAIL("الْفِعْلُ", "fil", "«the act» — the doer of the complete كَانَ.", "«fiil» — tâm كَانَ'nin fâili.", punct=".", tags=["al-fil-al-tamm-wal-naqis"])]})
S.append({"id": "s3", "translation": {
 "en": "And this name falls upon the soundness of the causes, the instruments and the limbs.",
 "tr": "Bu isim, sebeplerin, âletlerin ve organların sağlamlığına da verilir."},
 "tokens": [
  MUDA("وَيَقَعُ", "waqaa", "«and falls» — the name «capability» is also used for …", "«ve düşer» — «istitâat» adı … için de kullanılır.", "وَالْفَاعِلُ «هَذَا الِاسْمُ»", wa="isti", tags=["mithal-verbs", "fail"]),
  ISHARA("هَذَا", "hadha", "«this».", "«bu».", "فِي مَحَلِّ رَفْعٍ فَاعِلٌ", tags=["fail"], bina="السُّكُونِ"),
  BADAL("الِاسْمُ", "ism", "«name» — the noun after a demonstrative is its badal (or its explanatory apposition).", "«isim» — ism-i işâretten sonraki isim onun bedelidir (ya da atf-ı beyânı).", "هَذَا", "raf", extra=" (وَيُقَالُ: عَطْفُ بَيَانٍ)"),
  PREP("عَلَى", "ala", "«upon».", "«üzerine»."),
  MAJ("سَلَامَةِ", "salama", "«the soundness of».", "«sağlamlığına».", "عَلَى", "«يَقَعُ»", mudaf=True),
  MUDI("الْأَسْبَابِ", "sabab", "«the causes».", "«sebeplerin».", tags=["jam-taksir"]),
  ATF("وَالْآلَاتِ", "alat", "«the instruments» — a sound feminine plural: its jarr is by the kasra.", "«âletlerin» — cem'-i müennes sâlim: cerri kesre iledir.", "الْأَسْبَابِ", "jarr", tags=["jam-muannath-salim"]),
  ATF("وَالْجَوَارِحِ", "jariha", "«and the limbs» — the plural of جَارِحَة.", "«ve organların» — جَارِحَة'nin çoğulu.", "الْأَسْبَابِ", "jarr", punct=".", tags=["jam-taksir"])]})
S.append({"id": "s4", "translation": {
 "en": "And the validity of obligation rests on this capability.",
 "tr": "Teklifin sıhhati bu istitâate dayanır."},
 "tokens": [
  MUB("وَصِحَّةُ", "sihha", "«and the validity of».", "«ve sıhhati».", wa="isti", mudaf=True),
  MUDI("التَّكْلِيفِ", "taklif", "«obligation» — charging the servant with a duty (masdar of Form II).", "«teklifin» — kula bir yükümlülük yüklemek (tef'îl masdarı).", tags=["masdar", "form-ii-verbs"]),
  MUDA("تَعْتَمِدُ", "itamada", "«rests on» — Form VIII; the verbal sentence is the khabar.", "«dayanır» — iftiâl bâbı; fiil cümlesi haberdir.", HIDDEN_HIYA + "، وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ", tags=["form-viii-verbs", "anwa-al-khabar"]),
  ISHARA("هَذِهِ", "hadhihi", "«this».", "«bu».", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", tags=["maful-bihi"], bina="الْكَسْرِ"),
  BADAL("الِاسْتِطَاعَةَ", "istitaa", "«capability» — the badal in naṣb.", "«istitâate» — mansûb bedel.", "هَذِهِ", "nasb", punct=".")]})

CAND = {
 "hasan-good": need("hasan-good", "حَسَن", "ح س ن", "noun", "good, fine (a ṣifa mushabbaha)", "hasen, güzel, iyi (sıfat-ı müşebbehe)", 2),
 "rida-pleasure": need("rida-pleasure", "رِضَاء", "ر ض و", "noun", "good pleasure, approval (also written رِضَا)", "rızâ, hoşnutluk (رِضَا da yazılır)", 3),
 "allati": need("allati", "الَّتِي", "", "pron", "which, who (feminine singular relative)", "ki o (müfred müennes ism-i mevsûl)", 2),
 "salama": need("salama", "سَلَامَة", "س ل م", "noun", "soundness, being intact", "selâmet, sağlamlık", 3),
 "alat": need("alat", "آلَة", "أ و ل", "noun", "an instrument, a tool", "âlet", 3, plural="آلَات"),
 "jariha": need("jariha", "جَارِحَة", "ج ر ح", "noun", "a limb, an organ of the body", "organ, uzuv", 4, plural="جَوَارِح"),
 "taklif": need("taklif", "تَكْلِيف", "ك ل ف", "noun", "obligation — charging with a duty (masdar of Form II)", "teklif, yükümlü kılma (tef'îl masdarı)", 4),
}
ADD_EN = (" Chapter 34 (matn lines 39-41): the good is by God's pleasure and the ugly is not; capability is the true nature of the power by which"
          " the act exists, the name also used for sound causes, instruments and limbs, and the validity of obligation rests on it; the"
          " sentences around them are chapter 7.")
ADD_TR = (" Otuz dördüncü bâb (matn satırları 39-41): hasen Allah'ın rızasıyladır, kabîh değildir; istitâat fiilin kendisiyle var olduğu"
          " kudretin hakikatidir, ad sağlam sebep, âlet ve organlar için de kullanılır ve teklifin sıhhati ona dayanır; çevresindeki cümleler"
          " yedinci bâbdır.")
finish(34, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 34 (matn lines 39-41)")
