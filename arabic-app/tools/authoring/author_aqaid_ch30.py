# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 30: the attributes are neither He nor other than He; the eight attributes named. Source: matn line 33
(وهي لا هو ولا غيره … والكلام); وَلَهُ صِفَاتٌ أَزَلِيَّةٌ قَائِمَةٌ بِذَاتِهِ before it is chapter 5 s4; the supplier's bracketed gloss is not matn.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch30.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "الصِّفَاتُ الْأَزَلِيَّةُ", "en": "The Eternal Attributes", "tr": "Ezelî Sıfatlar"}
S = []
S.append({"id": "s1", "translation": {
 "en": "And they are neither He nor other than He.",
 "tr": "Onlar ne O'dur ne de O'ndan başkadır."},
 "tokens": [
  HUWA("وَهِيَ", "«and they» — the eternal attributes just named (chapter 5); a feminine singular pronoun for a plural of things.", "«ve onlar» — az önce anılan ezelî sıfatlar (5. bâb); gayr-i âkil çoğul için müfred müennes zamir.", wa="isti", tags=["al-jumu-wa-tanith-amiliha"]),
  LA("«not» — the negation before a noun, governing nothing.", "«değil» — isim önünde amelsiz nefiy."),
  W("هُوَ", "pron-3ms-munfasil", "pron", ["mubtada-khabar", "al-marifa-al-mudmarat-wal-alam"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«He» — the khabar: the attributes are not the Essence.", "«O» — haber: sıfatlar Zât değildir."),
  WALA(),
  ENC("غَيْرُهُ", "ghayr", "«other than He» — nor are they a thing apart from Him; the famous formula of Ahl al-Sunna.", "«O'ndan başka» — O'ndan ayrı bir şey de değildir; Ehl-i Sünnet'in meşhur ifadesi.", "مَعْطُوفٌ عَلَى «هُوَ» تَابِعٌ لَهُ فِي الرَّفْعِ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ", pr="هُ", tags=["atf-nasaq"], punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "And they are: knowledge, power, life, strength, hearing, sight, will, wish, action, creating, providing and speech.",
 "tr": "Onlar şunlardır: ilim, kudret, hayat, kuvvet, işitme, görme, irade, meşîet, fiil, tahlîk, terzîk ve kelâm."},
 "tokens": [
  HUWA("وَهِيَ", "«and they are».", "«ve onlar».", wa="isti", punct=":"),
  KHA("الْعِلْمُ", "ilm", "«knowledge».", "«ilim».", of="هِيَ"),
  ATF("وَالْقُدْرَةُ", "qudra", "«power».", "«kudret».", "الْعِلْمُ", "raf"),
  ATF("وَالْحَيَاةُ", "hayat", "«life».", "«hayat».", "الْعِلْمُ", "raf"),
  ATF("وَالْقُوَّةُ", "quwwa", "«strength».", "«kuvvet».", "الْعِلْمُ", "raf"),
  ATF("وَالسَّمْعُ", "sam", "«hearing».", "«işitme».", "الْعِلْمُ", "raf"),
  ATF("وَالْبَصَرُ", "basar", "«sight».", "«görme».", "الْعِلْمُ", "raf"),
  ATF("وَالْإِرَادَةُ", "irada", "«will».", "«irade».", "الْعِلْمُ", "raf"),
  ATF("وَالْمَشِيئَةُ", "mashia", "«wish» — the Māturīdīs read will and wish as one attribute under two names.", "«meşîet» — Mâtürîdîler irade ile meşîeti iki isimli tek sıfat sayar.", "الْعِلْمُ", "raf"),
  ATF("وَالْفِعْلُ", "fil", "«action».", "«fiil».", "الْعِلْمُ", "raf"),
  ATF("وَالتَّخْلِيقُ", "takhliq", "«creating» — the masdar of Form II; with تَرْزِيق a branch of takwīn (chapter 6).", "«tahlîk, yaratma» — tef'îl masdarı; تَرْزِيق ile birlikte tekvînin (6. bâb) bir şubesi.", "الْعِلْمُ", "raf", tags=["masdar", "form-ii-verbs"]),
  ATF("وَالتَّرْزِيقُ", "tarziq", "«providing».", "«terzîk, rızık verme».", "الْعِلْمُ", "raf", tags=["masdar", "form-ii-verbs"]),
  ATF("وَالْكَلَامُ", "kalam", "«and speech».", "«ve kelâm».", "الْعِلْمُ", "raf", punct=".")]})

CAND = {
 "takhliq": need("takhliq", "تَخْلِيق", "خ ل ق", "noun", "creating, bringing into being (masdar of Form II)", "tahlîk, yaratma (tef'îl masdarı)", 4),
 "tarziq": need("tarziq", "تَرْزِيق", "ر ز ق", "noun", "providing sustenance (masdar of Form II)", "terzîk, rızık verme (tef'îl masdarı)", 4),
}
ADD_EN = (" Chapter 30 (matn line 33): the attributes are neither He nor other than He, and the eight (with their branches) named; the"
          " supplier's bracketed gloss [أي صفاته ثابتة لذاته] is a note, not matn, and is not authored.")
ADD_TR = (" Otuzuncu bâb (matn satırı 33): sıfatlar ne O'dur ne O'ndan başkadır; sekiz sıfat (şubeleriyle) sayılır; nüshadaki köşeli"
          " parantezli [أي صفاته ثابتة لذاته] açıklaması matn değildir, yazılmamıştır.")
finish(30, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 30 (matn line 33)")
