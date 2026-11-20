# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 28: the world is substances and accidents — why it is originated, and what each is.
Source: matn line 29 (إذ هو أعيان وأعراض … كالألوان والأكوان والطعوم والروائح); والعالم بجميع أجزائه محدث and the definitions of
the ʿayn, the atom and the accident are chapter 3; this chapter carries the spans chapter 3 left out.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch28.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْأَعْيَانُ وَالْأَعْرَاضُ", "en": "Substances and Accidents", "tr": "A'yân ve A'râz"}
S = []
S.append({"id": "s1", "translation": {
 "en": "— since it is substances and accidents.",
 "tr": "— çünkü o, a'yân ve a'râzdan ibarettir."},
 "tokens": [
  W("إِذْ", "idh-talil", "part", ["al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "lam-taleel"], "«إِذْ» حَرْفُ تَعْلِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ — وَقِيلَ: ظَرْفٌ لِمَا مَضَى أُشْرِبَ مَعْنَى التَّعْلِيلِ؛ وَهُوَ يُعَلِّلُ قَوْلَهُ: وَالْعَالَمُ مُحْدَثٌ.", "«since» — idh giving the reason for «the world is originated» (chapter 3); some read it as a ẓarf of the past coloured by causation.", "«çünkü» — «âlem hâdistir» (3. bâb) hükmünün gerekçesini veren iz; kimi onu ta'lîl mânâsı yüklenmiş bir mâzî zarfı sayar."),
  HUWA("هُوَ", "«it» — the world.", "«o» — âlem."),
  KHA("أَعْيَانٌ", "ayan", "«substances» — the plural of عَيْن: what stands by itself.", "«a'yân» — عَيْن'in çoğulu: kendi başına kâim olan.", tags=["jam-taksir"]),
  ATF("وَأَعْرَاضٌ", "arad", "«and accidents» — what does not stand by itself.", "«ve a'râz» — kendi başına kâim olmayan.", "أَعْيَانٌ", "raf", punct=".", tags=["jam-taksir"])]})
S.append({"id": "s2", "translation": {
 "en": "So the substances are what has subsistence by itself; and it is either composite, or non-composite like the atom.",
 "tr": "A'yân, kendi zâtıyla kâim olandır; o ya mürekkeptir ya da cevher gibi mürekkep değildir."},
 "tokens": [
  MUB("فَالْأَعْيَانُ", "ayan", "«so the substances» — the fāʾ opens the detail of the pair just named.", "«a'yân ise» — fâ, az önce anılan çiftin tafsiline girer.", wa="fa-tafsil", tags=["jam-taksir"]),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«that which» — the relative as khabar.", "«o şey ki» — haber olan ism-i mevsûl."),
  PRON_J("لَهُ", "لِ", "«has» — the jarr phrase stands first as the khabar of قِيَامٌ inside the ṣila: «to it is subsistence».", "«vardır» — sıla içinde قِيَامٌ'un öne alınmış haberi olan câr-mecrûr: «onun için kıyam vardır».", "مَحْذُوفٍ خَبَرٌ مُقَدَّمٌ لِـ«قِيَامٌ»", tags=["zarf-mustaqarr-wa-laghw", "taqdim-al-musnad"]),
  W("قِيَامٌ", "qiyam", "noun", ["mubtada-khabar", "ism-mawsul", "taqdim-al-musnad"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.", "«subsistence» — the delayed mubtada; an indefinite mubtada follows its jarr-phrase khabar.", "«kıyam» — sonraya bırakılmış mübteda; nekre mübteda, câr-mecrûr haberinden sonra gelir."),
  ENC("بِذَاتِهِ", "dhat", "«by itself» — by its own essence.", "«kendi zâtıyla».", "«ذَاتِ» مَجْرُورٌ بِالْبَاءِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", letter="بِ", att="«قِيَامٌ»", punct="،"),
  HUWA("وَهُوَ", "«and it» — the substance.", "«ve o» — ayn.", wa="atf"),
  W("إِمَّا", "imma", "part", ["aw-imma-am-la-bal-lakin-fil-kafiya"], "حَرْفُ تَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ، وَجَوَابُهُ «أَوْ».", "«either» — immā offers a division and is answered by أَوْ (or by a second إِمَّا).", "«ya» — immâ bir taksim sunar; cevabı أَوْ (ya da ikinci bir إِمَّا) gelir."),
  KHA("مُرَكَّبٌ", "murakkab", "«composite» — the ism mafʿūl of Form II.", "«mürekkep» — tef'îl ism-i mef'ûlü.", of="هُوَ", tags=["ism-maful", "form-ii-verbs"]),
  W("أَوْ", "aw", "conj", ["atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya"], "حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "«or».", "«ya da»."),
  ATF("غَيْرُ", "ghayr", "«non-» — غَيْر annexed to the thing negated.", "«olmayan» — nefyedilene muzâf غَيْر.", "مُرَكَّبٌ", "raf", letter="aw", mudaf=True),
  MUDI("مُرَكَّبٍ", "murakkab", "«composite».", "«mürekkep».", tags=["ism-maful"]),
  FUSED("كَالْجَوْهَرِ", "كَ", "jawhar", "«like the atom» — the indivisible part; the phrase describes «non-composite».", "«cevher gibi» — bölünmez parça; câr-mecrûr «mürekkep olmayan»ın sıfatıdır.", "مَحْذُوفٍ صِفَةٌ لِـ«غَيْرُ مُرَكَّبٍ»", inner="الْجَوْهَرِ", meaning=" لِلتَّشْبِيهِ", punct=".")]})
S.append({"id": "s3", "translation": {
 "en": "— and it (the accident) occurs in bodies and atoms, like colours, modes of being, tastes and smells.",
 "tr": "— ve o (araz), cisimlerde ve cevherlerde meydana gelir; renkler, oluş hâlleri, tatlar ve kokular gibi."},
 "tokens": [
  MUDA("وَيَحْدُثُ", "hadatha", "«and it occurs» — the accident; this clause continues «the accident is what does not stand by itself» (chapter 3).", "«ve meydana gelir» — araz; bu cümle «araz kendi zâtıyla kâim olmayandır» (3. bâb) hükmünü sürdürür.", HIDDEN_HUWA + " يَعُودُ عَلَى «الْعَرَضِ» — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى صِلَةِ «مَا» فِي قَوْلِهِ: وَالْعَرَضُ مَا لَا يَقُومُ بِذَاتِهِ", wa="atf", tags=["thulathi-mujarrad-babs", "atf-nasaq"]),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("الْأَجْسَامِ", "jism", "«bodies» — the plural of جِسْم.", "«cisimler» — جِسْم'in çoğulu.", "فِي", "«يَحْدُثُ»", tags=["jam-taksir"]),
  ATF("وَالْجَوَاهِرِ", "jawhar", "«and atoms» — the plural of جَوْهَر, on the diptote pattern فَوَاعِل, yet in jarr by the kasra because of the article.", "«ve cevherler» — جَوْهَر'in çoğulu; فَوَاعِل vezninde gayr-i munsarif olsa da elif-lâm sebebiyle kesre ile mecrûrdur.", "الْأَجْسَامِ", "jarr", tags=["jam-taksir", "mamnu-min-sarf"]),
  FUSED("كَالْأَلْوَانِ", "كَ", "lawn", "«like colours» — the khabar of a dropped mubtada: «and that is like …».", "«renkler gibi» — hazfedilmiş bir mübtedanın haberi: «o da … gibidir».", "مَحْذُوفٍ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: وَذَلِكَ كَائِنٌ كَالْأَلْوَانِ", inner="الْأَلْوَانِ", meaning=" لِلتَّشْبِيهِ", tags=["hadhf-wa-taqdir", "jam-taksir"]),
  ATF("وَالْأَكْوَانِ", "kawn", "«and modes of being» — the four akwān of the theologians: motion, rest, union, separation.", "«ve ekvân» — kelâmcıların dört ekvânı: hareket, sükûn, ictimâ, iftirâk.", "الْأَلْوَانِ", "jarr", tags=["jam-taksir"]),
  ATF("وَالطُّعُومِ", "tam-taste", "«tastes» — the plural of طَعْم.", "«tatlar» — طَعْم'in çoğulu.", "الْأَلْوَانِ", "jarr", tags=["jam-taksir"]),
  ATF("وَالرَّوَائِحِ", "raiha", "«and smells» — the plural of رَائِحَة.", "«ve kokular» — رَائِحَة'nin çoğulu.", "الْأَلْوَانِ", "jarr", punct=".", tags=["jam-taksir"])]})

CAND = {
 "idh-talil": need("idh-talil", "إِذْ (التَّعْلِيلِيَّة)", "إ ذ", "part", "since, because — idh giving a reason", "çünkü, zira — ta'lîl bildiren iz", 4),
 "hadatha": need("hadatha", "حَدَثَ", "ح د ث", "verb", "to occur, to come into being", "meydana gelmek, hâdis olmak", 3),
}
MORPH = {"hadatha": sarf.sound1("nasara", "حَدَث", "حْدُث", "اُحْدُث", "حُدُوث", "حَادِث", None, None, None,
                                "حَدَثَ الشَّيْءُ يَحْدُثُ حُدُوثًا: وُجِدَ بَعْدَ أَنْ لَمْ يَكُنْ — مِنْ بَابِ نَصَرَ، لَازِمٌ")}
ADD_EN = (" Chapter 28 (matn line 29): the world is substances and accidents — the reason the world is originated, the composite and the"
          " atom, and where accidents occur; the definitions of the ʿayn, the atom and the accident in the same line are chapter 3.")
ADD_TR = (" Yirmi sekizinci bâb (matn satırı 29): âlem a'yân ve a'râzdır — âlemin hudûsunun gerekçesi, mürekkep ve cevher, arazın nerede"
          " meydana geldiği; aynı satırdaki ayn, cevher ve araz tarifleri üçüncü bâbdır.")
finish(28, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 28 (matn line 29)", morph=MORPH)
