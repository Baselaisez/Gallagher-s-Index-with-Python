# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 31: the speech of God — an eternal attribute, not of the kind of letters and sounds.
Source: matn line 33 (وهو متكلم بكلام … آمر ناه مخبر); the Qur'an sentences after it are chapter 5 s5-s6.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch31.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "صِفَةُ الْكَلَامِ", "en": "The Attribute of Speech", "tr": "Kelâm Sıfatı"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And He speaks with a speech that is an eternal attribute of His, not of the kind of letters and sounds.",
 "tr": "O, kendisinin ezelî bir sıfatı olan, harf ve ses cinsinden olmayan bir kelâmla mütekellimdir."},
 "tokens": [
  HUWA("وَهُوَ", "«and He».", "«ve O».", wa="isti"),
  KHA("مُتَكَلِّمٌ", "mutakallim", "«speaking, a speaker» — the ism fāʿil of Form V as khabar.", "«mütekellim, konuşan» — tefe'ul ism-i fâili haber olarak.", of="هُوَ", tags=["ism-fail", "form-v-verbs"]),
  FUSED("بِكَلَامٍ", "بِ", "kalam", "«with a speech» — indefinite, so the sentence after it describes it.", "«bir kelâmla» — nekre; ardındaki cümle onun sıfatıdır.", "«مُتَكَلِّمٌ»", inner="كَلَامٍ"),
  HUWA("هُوَ", "«(which) is» — the pronoun opens a sentence that is the adjective of كَلَامٍ.", "«(ki) o» — zamir, كَلَامٍ'in sıfatı olan cümleyi açar.", extra="، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«كَلَامٍ»", tags=["jumla-sifa"]),
  KHA("صِفَةٌ", "sifa", "«an attribute».", "«bir sıfat».", of="هُوَ"),
  PRON_J("لَهُ", "لِ", "«of His».", "«O'nun».", "مَحْذُوفٍ صِفَةٌ لِـ«صِفَةٌ»", tags=["jumla-sifa"]),
  NAT("أَزَلِيَّةٌ", "azali", "«eternal» — without beginning.", "«ezelî» — başlangıçsız.", "صِفَةٌ", "raf", tags=["ism-mansub"]),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "jumla-sifa", "al-afal-al-naqisa-fil-kafiya"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِـ«كَلَامٍ».", "«is not» — the frozen verb of negation; a second adjective-sentence of the speech.", "«değildir» — nefyin câmid fiili; kelâmın ikinci sıfat cümlesi."),
  PREP("مِنْ", "min", "«of».", "«-den»."),
  MAJ("جِنْسِ", "jins", "«the kind of» — the jarr phrase is the khabar of لَيْسَ.", "«cinsinden» — câr-mecrûr لَيْسَ'nin haberidir.", "مِنْ", "مَحْذُوفٍ خَبَرُ «لَيْسَ»", mudaf=True),
  MUDI("الْحُرُوفِ", "harf", "«letters» — the plural of حَرْف.", "«harfler» — حَرْف'in çoğulu.", tags=["jam-taksir"]),
  ATF("وَالْأَصْوَاتِ", "sawt", "«and sounds» — the plural of صَوْت.", "«ve sesler» — صَوْت'un çoğulu.", "الْحُرُوفِ", "jarr", punct=".", tags=["jam-taksir"])]})
S.append({"id": "s2", "translation": {
 "en": "And it is an attribute incompatible with silence and with defect.",
 "tr": "O, sükûta ve âfete aykırı bir sıfattır."},
 "tokens": [
  HUWA("وَهُوَ", "«and it» — the speech.", "«ve o» — kelâm.", wa="atf"),
  KHA("صِفَةٌ", "sifa", "«an attribute».", "«bir sıfat».", of="هُوَ"),
  NAT("مُنَافِيَةٌ", "munafi", "«incompatible» — the ism fāʿil of Form III (نَافَى) in the feminine, agreeing with صِفَةٌ.", "«aykırı, zıt» — müfâale (نَافَى) ism-i fâilinin müennesi; صِفَةٌ'e uyar.", "صِفَةٌ", "raf", tags=["ism-fail", "form-iii-verbs"]),
  FUSED("لِلسُّكُوتِ", "لِ", "sukut", "«with silence».", "«sükûta».", "«مُنَافِيَةٌ»", inner="السُّكُوتِ"),
  ATF("وَالْآفَةِ", "aafa", "«and defect» — muteness and the like; speech in Him is neither silence nor impediment.", "«ve âfete» — dilsizlik ve benzeri; O'nda kelâm ne sükûttur ne de bir engel.", "السُّكُوتِ", "jarr", punct=".")]})
S.append({"id": "s3", "translation": {
 "en": "And God the Exalted speaks by it — commanding, forbidding, informing.",
 "tr": "Allah Teâlâ onunla mütekellimdir: emreden, nehyeden, haber veren."},
 "tokens": [
  MUB("وَاللهُ", "allah", "«and God».", "«ve Allah».", wa="isti", pos="propn"),
  TAALA(),
  KHA("مُتَكَلِّمٌ", "mutakallim", "«speaks» — the first of four khabars.", "«mütekellimdir» — dört haberin ilki.", tags=["ism-fail", "form-v-verbs"]),
  PRON_J("بِهَا", "بِ", "«by it» — by that attribute.", "«onunla» — o sıfatla.", "«مُتَكَلِّمٌ»"),
  W("آمِرٌ", "aamir", "noun", ["mubtada-khabar", "ism-fail", "anwa-al-khabar"], "خَبَرٌ ثَانٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«commanding» — the ism fāʿil of أَمَرَ; the madda is hamza + alif.", "«emreden» — أَمَرَ'nin ism-i fâili; med, hemze + eliftir."),
  W("نَاهٍ", "nahin", "noun", ["mubtada-khabar", "ism-fail", "ism-maqsur-manqus"], "خَبَرٌ ثَالِثٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ الْمَحْذُوفَةِ.", "«forbidding» — an indefinite manqūṣ in rafʿ: the yāʾ falls and the tanwīn stands in for it.", "«nehyeden» — ref'te nekre mankûs: yâ düşer, tenvin yerine geçer."),
  W("مُخْبِرٌ", "mukhbir", "noun", ["mubtada-khabar", "ism-fail", "form-iv-verbs"], "خَبَرٌ رَابِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«informing» — the ism fāʿil of Form IV.", "«haber veren» — if'âl ism-i fâili.", punct=".")]})

CAND = {
 "munafi": need("munafi", "مُنَافٍ", "ن ف ي", "noun", "incompatible with, contrary to (ism fāʿil of Form III)", "aykırı, zıt, bağdaşmaz (müfâale ism-i fâili)", 5),
 "aafa": need("aafa", "آفَة", "أ و ف", "noun", "defect, blight, impediment", "âfet, kusur, engel", 4),
 "aamir": need("aamir", "آمِر", "أ م ر", "noun", "commanding, one who commands (ism fāʿil of أَمَرَ)", "emreden (أَمَرَ'nin ism-i fâili)", 4),
 "nahin": need("nahin", "نَاهٍ", "ن ه ي", "noun", "forbidding, one who forbids (ism fāʿil of نَهَى)", "nehyeden (نَهَى'nın ism-i fâili)", 4),
}
ADD_EN = (" Chapter 31 (matn line 33): the attribute of speech — eternal, not of the kind of letters and sounds, incompatible with silence and"
          " defect, and God commanding, forbidding and informing by it; the Qur'an sentences that follow are chapter 5.")
ADD_TR = (" Otuz birinci bâb (matn satırı 33): kelâm sıfatı — ezelî, harf ve ses cinsinden değil, sükût ve âfete aykırı; Allah onunla emreder,"
          " nehyeder, haber verir; ardından gelen Kur'ân cümleleri beşinci bâbdır.")
finish(31, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 31 (matn line 33)")
