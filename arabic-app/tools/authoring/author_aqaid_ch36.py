# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 36: the slain dies at his term; death is created by God; the term is one. Source: matn line 45.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch36.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الْمَقْتُولُ مَيِّتٌ بِأَجَلِهِ", "en": "The Slain Dies at His Term", "tr": "Maktûl Eceliyle Ölmüştür"}
S = []
S.append({"id": "s1", "translation": {"en": "And the slain dies at his term.", "tr": "Maktûl, eceliyle ölmüştür."},
 "tokens": [
  MUB("وَالْمَقْتُولُ", "maqtul", "«and the slain» — the ism mafʿūl of قَتَلَ.", "«ve maktûl» — قَتَلَ'nin ism-i mef'ûlü.", wa="isti", tags=["ism-maful"]),
  KHA("مَيِّتٌ", "mayyit", "«dead, dies» — on فَيْعِل; the Muʿtazila said the killer cut the term short, Ahl al-Sunna say no.", "«ölmüştür» — فَيْعِل vezninde; Mu'tezile kâtil eceli kısalttı der, Ehl-i Sünnet reddeder.", of="الْمَقْتُولُ"),
  ENC("بِأَجَلِهِ", "ajal", "«at his term» — the bāʾ of circumstance: with his fixed term, not before it.", "«eceliyle» — mülâbeset bâ'sı: belirlenmiş eceliyle, ondan önce değil.", "«أَجَلِ» مَجْرُورٌ بِالْبَاءِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ", pr="هِ", letter="بِ", att="«مَيِّتٌ»", punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And death, subsisting in the dead, is created by God the Exalted — the servant has no making in it, neither as creating nor as acquiring.",
 "tr": "Ölüde kâim olan ölüm Allah Teâlâ'nın yaratmasıdır; onda kulun ne yaratma ne de kesb cihetinden bir sun'u vardır."},
 "tokens": [
  MUB("وَالْمَوْتُ", "mawt", "«and death».", "«ve ölüm».", wa="isti"),
  KHA("قَائِمٌ", "qaim", "«subsisting» — the first khabar.", "«kâim» — birinci haber.", of="الْمَوْتُ", tags=["ism-fail"]),
  FUSED("بِالْمَيِّتِ", "بِ", "mayyit", "«in the dead».", "«ölüde».", "«قَائِمٌ»", inner="الْمَيِّتِ"),
  W("مَخْلُوقٌ", "makhluq", "noun", ["mubtada-khabar", "ism-maful", "anwa-al-khabar"], "خَبَرٌ ثَانٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", "«created» — a second khabar.", "«yaratılmış» — ikinci haber."),
  FUSED("لِلهِ", "لِ", "allah", "«by God».", "«Allah tarafından».", "«مَخْلُوقٌ»", inner="اللهِ", pos="propn"),
  TAALA(punct="،"),
  LAJINS(),
  W("صُنْعَ", "sun", "noun", ["la-nafiya-lil-jins"], "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«making».", "«sun'»."),
  FUSED("لِلْعَبْدِ", "لِ", "abd", "«the servant has».", "«kulun».", "مَحْذُوفٍ خَبَرُ «لَا»", inner="الْعَبْدِ", tags=["la-nafiya-lil-jins"]),
  W("تَخْلِيقًا", "takhliq", "noun", ["tamyiz", "masdar"], "تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — أَيْ: لَا صُنْعَ لَهُ مِنْ جِهَةِ التَّخْلِيقِ.", "«as creating» — a tamyīz: no making from the side of creating.", "«yaratma cihetinden» — temyiz: yaratma yönünden bir sun'u yok."),
  WALA(),
  W("اكْتِسَابًا", "iktisab", "noun", ["atf-nasaq", "tamyiz", "masdar", "form-viii-verbs"], "مَعْطُوفٌ عَلَى «تَخْلِيقًا» تَابِعٌ لَهُ فِي النَّصْبِ.", "«nor as acquiring» — kasb, the servant's share in his own acts; death is not even that.", "«ne de kesb cihetinden» — kesb, kulun kendi fiillerindeki payı; ölüm o bile değildir.", punct=".")]})
S.append({"id": "s3", "translation": {"en": "And the term is one.", "tr": "Ve ecel birdir."},
 "tokens": [
  MUB("وَالْأَجَلُ", "ajal", "«and the term» — the appointed time of death.", "«ve ecel» — ölümün belirlenmiş vakti.", wa="isti"),
  KHA("وَاحِدٌ", "wahid", "«is one» — not two, one for the natural death and one for the killing.", "«birdir» — biri tabiî ölüm biri öldürülme için olmak üzere iki değil.", of="الْأَجَلُ", punct=".")]})

CAND = {
 "maqtul": need("maqtul", "مَقْتُول", "ق ت ل", "noun", "slain, killed (ism mafʿūl of قَتَلَ)", "maktûl, öldürülmüş (قَتَلَ'nin ism-i mef'ûlü)", 3),
 "iktisab": need("iktisab", "اكْتِسَاب", "ك س ب", "noun", "acquisition, kasb — the servant's share in his act (masdar of Form VIII)", "iktisâb, kesb — kulun fiilindeki payı (iftiâl masdarı)", 4),
}
ADD_EN = " Chapter 36 (matn line 45): the slain dies at his term; death subsists in the dead and is God's creation with no making by the servant; the term is one."
ADD_TR = " Otuz altıncı bâb (matn satırı 45): maktûl eceliyle ölmüştür; ölüm ölüde kâimdir, Allah'ın yaratmasıdır, kulun sun'u yoktur; ecel birdir."
finish(36, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 36 (matn line 45)")
