# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 46: the ranks — the human messengers, the angelic messengers, humankind, the angels. The matn's last line (93).
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch46.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "رُسُلُ الْبَشَرِ وَرُسُلُ الْمَلَائِكَةِ", "en": "The Messengers of Mankind and the Messengers of the Angels", "tr": "Beşer Resulleri ve Melek Resulleri"}
S = []
def RANK(sid, a_full, a_lex, a_en, a_tr, a_tags, b_full, b_lex, b_en, b_tr, c_full, c_lex, c_en, c_tr, c_tags, d_full, d_lex, d_en, d_tr, en, tr):
    return {"id": sid, "translation": {"en": en, "tr": tr}, "tokens": [
      MUB(a_full, a_lex, a_en, a_tr, wa="isti", mudaf=True, tags=a_tags),
      MUDI(b_full, b_lex, b_en, b_tr),
      KHA("أَفْضَلُ", "afdal", "«are better» — the elative, a diptote, with مِنْ for the thing surpassed.", "«daha üstündür» — ism-i tafdîl, gayr-i munsarif; üstün gelineni مِنْ gösterir.", tags=["ism-tafdil", "mamnu-min-sarf"]),
      PREP("مِنْ", "min", "«than».", "«-den»."),
      MAJ(c_full, c_lex, c_en, c_tr, "مِنْ", "«أَفْضَلُ»", mudaf=True, tags=c_tags),
      MUDI(d_full, d_lex, d_en, d_tr, punct=".")]}
S.append(RANK("s1", "وَرُسُلُ", "rusul", "«and the messengers of» — the plural of رَسُول.", "«ve resulleri» — رَسُول'ün çoğulu.", ["jam-taksir"],
              "الْبَشَرِ", "bashar", "«mankind».", "«beşerin».",
              "رُسُلِ", "rusul", "«the messengers of».", "«resullerinden».", ["jam-taksir"],
              "الْمَلَائِكَةِ", "malak", "«the angels» — Gabriel and his like.", "«meleklerin» — Cebrâil ve benzerleri.",
              "And the messengers of mankind are better than the messengers of the angels.", "Beşerin resulleri, meleklerin resullerinden üstündür."))
S.append(RANK("s2", "وَرُسُلُ", "rusul", "«and the messengers of».", "«ve resulleri».", ["jam-taksir"],
              "الْمَلَائِكَةِ", "malak", "«the angels».", "«meleklerin».",
              "عَامَّةِ", "amma-common", "«the generality of» — the ordinary members.", "«umûmundan» — sıradan fertleri.", [],
              "الْبَشَرِ", "bashar", "«mankind».", "«beşerin».",
              "And the messengers of the angels are better than the generality of mankind.", "Meleklerin resulleri, beşerin umûmundan üstündür."))
S.append(RANK("s3", "وَعَامَّةُ", "amma-common", "«and the generality of».", "«ve umûmu».", [],
              "الْبَشَرِ", "bashar", "«mankind» — the believers among them.", "«beşerin» — mü'min olanları.",
              "عَامَّةِ", "amma-common", "«the generality of».", "«umûmundan».", [],
              "الْمَلَائِكَةِ", "malak", "«the angels» — the matn's closing word.", "«meleklerin» — matnın son kelimesi.",
              "And the generality of mankind are better than the generality of the angels.", "Beşerin umûmu, meleklerin umûmundan üstündür."))
CAND = {
 "amma-common": need("amma-common", "عَامَّة", "ع م م", "noun", "the generality, the common run (of a class)", "umûm, bir sınıfın geneli", 3),
}
ADD_EN = " Chapter 46 (matn line 93, the matn's last): the four ranks — the human messengers, the angelic messengers, humankind, the angels. With this the Nasafī matn is consumed to its end."
ADD_TR = " Kırk altıncı bâb (matn satırı 93, matnın sonu): dört mertebe — beşer resulleri, melek resulleri, beşer, melekler. Bununla Nesefî matnı sonuna kadar işlenmiştir."
finish(46, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 46 (matn line 93")
