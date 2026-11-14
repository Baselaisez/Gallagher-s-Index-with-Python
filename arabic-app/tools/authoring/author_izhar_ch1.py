# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 1: the muqaddima (the three things every mu'rib needs), the kalima and its three kinds
# with their marks (p. 84-85), the amil's definition (p. 85), its division lafzi/ma'nawi, sama'i/qiyasi, in-the-ism/in-the-mudari,
# one-ism/two-isms (p. 88), and the TWENTY jarr letters with the meaning of each (p. 88-89).
# Source: research/sources/izhar-al-asrar-matn-lithograph.txt pages [84]-[89]. The print's الصلوة / ثلثة are given standard.
#   python3 author_izhar_ch1.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-amil-wa-aqsamuh"
TITLE = {"ar": "الْعَامِلُ وَأَقْسَامُهُ وَحُرُوفُ الْجَرِّ الْعِشْرُونَ", "en": "The governor, its divisions, and the twenty jarr letters", "tr": "Âmil, kısımları ve yirmi cer harfi"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; HJN = "huruf-jarr-nawadir"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; KK = "al-kalima-wal-kalam"

def fi(punct=None): return tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(punct=None): return tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzere».", punct=punct)
def wahuwa(what_ar, what_en, what_tr):
    return tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ " + what_ar + "، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and it» — " + what_en + "; the mubtada.", "«ve o» — " + what_tr + "; mübtedâ.", segments=wa("هُوَ", "huwa", "pron"))
def ma_khabar(): return tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", MK], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ — أَيْ: الَّذِي.", "«that which» — the relative, the khabar.", "«… olan şey» — ism-i mevsûl, haber.")
def dalla(): return tok("دَلَّ", "dalla", "verb", [K, "ism-mawsul", "doubled-verbs"], "مَاضٍ مُضَاعَفٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.", "«points» — the relative clause; its doer concealed.", "«delâlet eder» — sıla; fâili müstetir.")
def mana_j(punct=None): return tok("مَعْنًى", "mana", "noun", [K, HJ, "ism-maqsur-manqus"], "مَجْرُورٌ بِعَلَى، وَعَلَامَةُ جَرِّهِ كَسْرَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ الْمَحْذُوفَةِ — اسْمٌ مَقْصُورٌ مُنَوَّنٌ.", "«a meaning» — a maqsur noun, its kasra estimated.", "«bir mana» — maksûr isim, kesresi takdîrî.", punct=punct)
def ahad_j(full="أَحَدِ", clit=None):
    segs = [seg("بِ", "bi", "prep"), seg("أَحَدِ", "ahad", "noun")] if clit else None
    ar = ("الْبَاءُ حَرْفُ جَرٍّ، وَأَحَدِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ." if clit else "مَجْرُورٌ بِعَلَى، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ.")
    return [tok(full, "ahad", "noun", [K, HJ, ID], ar, "«one of» — annexed.", "«birine» — muzâf.", segments=segs),
            tok("الْأَزْمِنَةِ", "zaman", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ زَمَانٍ عَلَى أَفْعِلَةٍ.", "«the tenses» — the broken plural of زَمَان.", "«zamanların» — zamân'ın cem-i mükesseri."),
            tok("الثَّلَاثَةِ", "thalatha", "noun", [K, NA], "صِفَةٌ لِلْأَزْمِنَةِ مَجْرُورَةٌ بِالْكَسْرَةِ.", "«three» — the na't.", "«üç» — sıfat.", punct="،")]
def min_khawass():
    return [tok("وَمِنْ", "min", "prep", [K, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and among» — the jarr phrase is the fronted khabar.", "«ve …-dendir» — câr-mecrûr mukaddem haber.", segments=wa("مِنْ", "min", "prep")),
            tok("خَوَاصِّهِ", "khassa-property", "noun", [K, HJ, ID, "jam-taksir"], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ خَاصَّةٍ.", "«its peculiar marks» — plural of خَاصَّة.", "«hâssalarından» — hâssa'nın cem'i.", segments=[seg("خَوَاصِّ", "khassa-property", "noun"), pr3msi()]),
            tok("دُخُولُ", "dukhul", "noun", [K, MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the entering of» — the delayed mubtada, annexed.", "«dâhil olması» — muahhar mübtedâ, muzâf.")]
def quoted_j(full, lex, pos, en, tr, punct=None, first=False):
    """A particle QUOTED as a word (لَفْظٌ مَحْكِيّ) in the place of jarr: annexed to دُخُول or joined onto it."""
    segs = None if first else wa(full[2:], lex, pos)
    ar = ("مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مَبْنِيٌّ عَلَى مَا يُسْمَعُ بِهِ." if first
          else "الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ.")
    return tok(full, lex, pos, [K, "hadhf-wa-taqdir" if first else AT, ID if first else "hadhf-wa-taqdir"], ar, en + " — the word itself is quoted; it sits in the place of jarr.", tr + " — lafzı kastedilmiş (hikâye); cer mahallinde.", punct=punct, segments=segs)
def quoted_mubt(full, lex, pos, en, tr, ar_extra=""):
    """A jarr letter QUOTED as the mubtada of its own entry in the list of twenty."""
    return tok(full, lex, pos, [K, HJ, MK, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ" + ar_extra + ".", en + " — the letter quoted as a word: the mubtada of its entry.", tr + " — harf kelime olarak hikâye edilmiş: maddesinin mübtedâsı.", segments=wa(full[2:], lex, pos))
def li_khabar(full, lex, en, tr, punct=None, extra=()):
    bare_ = full[2:]
    return tok(full, lex, "noun", [K, HJ, MK, "zarf-mustaqarr-wa-laghw"] + list(extra), "اللَّامُ حَرْفُ جَرٍّ لِلِاخْتِصَاصِ، وَالِاسْمُ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ، مُتَعَلِّقٌ بِمَحْذُوفٍ: كَائِنَةٌ.", "«for " + en + "» — the jarr phrase is the khabar; its governor «being» is omitted.", "«" + tr + " içindir» — câr-mecrûr haber; müteallakı mahzûf.", punct=punct, segments=[seg("لِ", "li", "prep"), seg(bare_, lex, "noun")])
def amil_fi(what_full, what_lex, what_en, what_tr, joined=True, punct=None, extra_what=()):
    a = tok("وَعَامِلٌ" if joined else "عَامِلٌ", "amil-governor", "noun", [K, AT if joined else MK, "hadhf-wa-taqdir"],
            ("الْوَاوُ عَاطِفَةٌ، وَعَامِلٌ مَعْطُوفٌ مَرْفُوعٌ." if joined else "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: أَحَدُهُمَا عَامِلٌ — مَرْفُوعٌ بِالضَّمَّةِ."),
            "«a governor»" + ("" if joined else " — the khabar of an omitted «one of them»."), "«âmil»" + ("" if joined else " — mahzûf mübtedânın haberi."),
            segments=(wa("عَامِلٌ", "amil-governor", "noun") if joined else None))
    return [a, fi(), tok(what_full, what_lex, "noun", [K, HJ] + list(extra_what), "مَجْرُورٌ بِفِي، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«" + what_en + "»", "«" + what_tr + "»", punct=punct)]

# ----------- s1 — the hamd
S.append({"id": "s1", "translation": {"en": "Praise belongs to God, Lord of the worlds, and blessing upon Muhammad and all his family.", "tr": "Hamd, âlemlerin Rabbi Allah'adır; salât da Muhammed'e ve bütün âline olsun."},
 "tokens": [
  tok("الْحَمْدُ", "hamd", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«praise» — the mubtada.", "«hamd» — mübtedâ."),
  tok("لِلّٰهِ", "allah", "propn", [K, HJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«to God» — the jarr phrase is the khabar.", "«Allah'adır» — câr-mecrûr haber.", segments=[seg("لِ", "li", "prep"), seg("اللّٰهِ", "allah", "propn")]),
  tok("رَبِّ", "rabb", "noun", [K, NA, ID], "صِفَةٌ لِلَفْظِ الْجَلَالَةِ مَجْرُورَةٌ بِالْكَسْرَةِ، مُضَافٌ.", "«Lord» — the na't of the Name, annexed.", "«Rabbi» — lafza-i celâlin sıfatı, muzâf."),
  tok("الْعَالَمِينَ", "alam", "noun", [K, ID, "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«of the worlds» — jarr by the ya.", "«âlemlerin» — cerri yâ iledir."),
  tok("وَالصَّلَاةُ", "salat", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالصَّلَاةُ مَعْطُوفٌ عَلَى الْحَمْدِ مَرْفُوعٌ.", "«and blessing» — joined to «praise».", "«ve salât» — hamd'e ma'tûf.", segments=wa("الصَّلَاةُ", "salat", "noun")),
  ala(),
  tok("مُحَمَّدٍ", "muhammad", "propn", [K, HJ], "مَجْرُورٌ بِعَلَى، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«Muhammad»", "«Muhammed»"),
  tok("وَآلِهِ", "al-family", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَآلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his family»", "«ve âline»", segments=[seg("وَ", "wa", "conj"), seg("آلِ", "al-family", "noun"), pr3msi()]),
  tok("أَجْمَعِينَ", "ajmain", "noun", [K, "tawkid"], "تَوْكِيدٌ مَعْنَوِيٌّ لِآلِهِ مَجْرُورٌ بِالْيَاءِ.", "«all of them» — the tawkid, in jarr by the ya.", "«hepsine» — ma'nevî te'kîd, yâ ile mecrûr.", punct="."),
 ]})

# ----------- s2 — the risala
S.append({"id": "s2", "translation": {"en": "To proceed: this is a treatise on what every parser needs most urgently,", "tr": "İmdi: bu, i'râb eden herkesin en şiddetle muhtaç olduğu şeye dair bir risâledir;"},
 "tokens": [
  tok("وَبَعْدُ", "baad", "adv", [K, "hadhf-wa-taqdir", "maful-fih"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَبَعْدُ ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ لَفْظًا لَا مَعْنًى، فِي مَحَلِّ نَصْبٍ — أَيْ: أَمَّا بَعْدَ الْحَمْدِ.", "«to proceed» — the zarf built on the damma because its annex is cut off.", "«imdi» — muzâfun ileyhi kesildiği için damme üzere mebnî zarf.", punct="،", segments=wa("بَعْدُ", "baad", "adv")),
  tok("فَهٰذِهِ", "hadhihi", "pron", [K, MK, "asma-al-ishara"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا الْمُقَدَّرَةِ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the fa answers the implied أَمَّا; the demonstrative is the mubtada.", "«bu» — fâ mukadder emmâ'nın cevabında; işaret ismi mübtedâ.", segments=fa("هٰذِهِ", "hadhihi", "pron")),
  tok("رِسَالَةٌ", "risala-treatise", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a treatise» — the khabar.", "«bir risâledir» — haber."),
  tok("فِيمَا", "ma-mawsula", "pron", [K, HJ, "ism-mawsul", NA], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِرِسَالَةٍ.", "«on what» — the jarr phrase qualifies «treatise».", "«… şeye dair» — câr-mecrûr risâle'nin sıfatı.", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("يَحْتَاجُ", "ihtaja", "verb", [K, "ism-mawsul", "fail"], "مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — صِلَةُ الْمَوْصُولِ.", "«needs» — the relative clause.", "«muhtaç olur» — sıla."),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, "ism-mawsul"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَهُوَ الْعَائِدُ عَلَى مَا.", "«to it» — the pronoun returns to «what».", "«ona» — âid zamir.", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("كُلُّ", "kull", "noun", [K, "fail", ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«every» — the doer, annexed.", "«her» — fâil, muzâf."),
  tok("مُعْرِبٍ", "murib", "noun", [K, ID, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنْ أَعْرَبَ.", "«parser» — the ism fa'il of أَعْرَبَ.", "«i'râb eden» — a'rabe'nin ism-i fâili."),
  tok("أَشَدَّ", "ashadd", "noun", [K, "maful-mutlaq", ID, "mamnu-min-sarf"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ: احْتِيَاجًا أَشَدَّ الِاحْتِيَاجِ — مُضَافٌ.", "«most urgently» — stands in for the absolute object (a quality of the omitted masdar), annexed.", "«en şiddetli» — mef'ûl-i mutlaktan nâib: mahzûf masdarın sıfatı; muzâf."),
  tok("الِاحْتِيَاجِ", "ihtiyaj", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — مَصْدَرُ احْتَاجَ.", "«of need» — the masdar of اِحْتَاجَ.", "«ihtiyacın» — ihtâce'nin masdarı.", punct="،"),
 ]})

# ----------- s3 — the three things, the three babs
S.append({"id": "s3", "translation": {"en": "and that is three things: the governor, the governed, and the governing — that is, the iʿrab; so their arrangement in three chapters was necessary.", "tr": "o da üç şeydir: âmil, ma'mûl ve amel — yani i'râb; bu yüzden onları üç bab üzere tertip etmek vâcib oldu."},
 "tokens": [
  wahuwa("عَاطِفَةٌ", "the waw joins", "vâv atıf"),
  tok("ثَلَاثَةُ", "thalatha", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«three» — the khabar, annexed.", "«üç» — haber, muzâf."),
  tok("أَشْيَاءَ", "shay", "noun", [K, ID, "mamnu-min-sarf", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«things» — the diptote takes a fatha for its jarr.", "«şey» — gayr-ı munsarif: cerri fetha ile.", punct=":"),
  tok("الْعَامِلُ", "amil-governor", "noun", [K, "badal"], "بَدَلُ تَفْصِيلٍ مِنْ ثَلَاثَةُ مَرْفُوعٌ بِالضَّمَّةِ — أَوْ خَبَرُ مُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا الْعَامِلُ.", "«the governor» — the badal that spells out «three».", "«âmil» — üç'ü açan tafsîl bedeli."),
  tok("وَالْمَعْمُولُ", "mamul", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالْمَعْمُولُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the governed»", "«ve ma'mûl»", segments=wa("الْمَعْمُولُ", "mamul", "noun")),
  tok("وَالْعَمَلُ", "amal-governing", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالْعَمَلُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the governing»", "«ve amel»", segments=wa("الْعَمَلُ", "amal-governing", "noun")),
  tok("أَيِ", "ay", "part", [K, "atf-bayan"], "حَرْفُ تَفْسِيرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«that is» — the explaining particle, its sukun broken by the kasra.", "«yani» — tefsir harfi; iki sâkin için kesre."),
  tok("الْإِعْرَابُ", "irab", "noun", [K, "atf-bayan"], "عَطْفُ بَيَانٍ عَلَى الْعَمَلِ مَرْفُوعٌ — أَوْ بَدَلٌ.", "«the iʿrab» — the explicative apposition of «the governing».", "«i'râb» — amel'in atf-ı beyânı.", punct="،"),
  tok("فَوَجَبَ", "wajaba", "verb", [K, "fail"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَوَجَبَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«so it was necessary» — the fa of consequence.", "«bu yüzden vâcib oldu» — sebebiyet fâsı.", segments=fa("وَجَبَ", "wajaba", "verb")),
  tok("تَرْتِيبُهَا", "tartib", "noun", [K, "fail", ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their arrangement» — the doer, annexed.", "«onların tertibi» — fâil, muzâf.", segments=[seg("تَرْتِيبُ", "tartib", "noun"), pr3fs()]),
  ala(),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«three» — annexed.", "«üç» — muzâf."),
  tok("أَبْوَابٍ", "bab", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ بَابٍ.", "«chapters» — plural of بَاب.", "«bab» — bâb'ın cem'i.", punct="."),
 ]})

# ----------- s4 — the first bab
S.append({"id": "s4", "translation": {"en": "The first chapter: on the governor.", "tr": "Birinci bab: âmil hakkında."},
 "tokens": [
  tok("الْبَابُ", "bab", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the chapter» — the mubtada.", "«bab» — mübtedâ."),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "صِفَةٌ لِلْبَابِ مَرْفُوعَةٌ.", "«first» — the na't.", "«birinci» — sıfat."),
  fi(),
  tok("الْعَامِلِ", "amil-governor", "noun", [K, HJ, MK], "مَجْرُورٌ بِفِي — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«the governor» — the jarr phrase is the khabar.", "«âmil» — câr-mecrûr haber.", punct="."),
 ]})

# ----------- s5 — know first that the kalima is three
S.append({"id": "s5", "translation": {"en": "Know first that the word — and it is the utterance set down for a single meaning — is three:", "tr": "Önce bil ki kelime — o, müfred bir mana için konulmuş lafızdır — üçtür:"},
 "tokens": [
  tok("اعْلَمْ", "alima", "verb", [K, "fail"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«know!» — the imperative; its doer «you» concealed.", "«bil!» — emir; fâili vücûben müstetir: sen."),
  tok("أَوَّلًا", "awwal", "noun", [K, "maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: فِي الْأَوَّلِ.", "«first» — a zarf of time.", "«önce» — zaman zarfı."),
  tok("أَنَّ", "anna", "part", [K, "inna-wa-akhawatuha", "inna-am-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، مَفْتُوحُ الْهَمْزَةِ لِأَنَّهُ مَعَ مَا بَعْدَهُ فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ اعْلَمْ.", "«that» — fatha on the hamza: the clause is a masdar standing for the two objects of «know».", "«ki» — hemzesi fethalı: cümle masdar hükmünde, «bil»in iki mef'ûlü yerinde."),
  tok("الْكَلِمَةَ", "kalima", "noun", [K, "inna-wa-akhawatuha", KK], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the word» — the ism of أَنَّ.", "«kelime» — enne'nin ismi.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, MK, "jumla-mutarida"], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَهِيَ مُبْتَدَأٌ — وَالْجُمْلَةُ مُعْتَرِضَةٌ بَيْنَ اسْمِ أَنَّ وَخَبَرِهَا.", "«and it is» — a parenthetical clause between the ism and the khabar of أَنَّ.", "«o da …-dır» — enne'nin ismi ile haberi arasında mu'terize cümle.", segments=wa("هِيَ", "hiya", "pron")),
  tok("اللَّفْظُ", "lafz", "noun", [K, MK, KK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the utterance» — the khabar.", "«lafız» — haber."),
  tok("الْمَوْضُوعُ", "mawdu", "noun", [K, NA, "ism-maful"], "صِفَةٌ لِلَّفْظِ مَرْفُوعَةٌ — اسْمُ مَفْعُولٍ.", "«set down» — the na't, an ism maf'ul.", "«konulmuş» — sıfat, ism-i mef'ûl."),
  tok("لِمَعْنًى", "mana", "noun", [K, HJ, "ism-maqsur-manqus"], "اللَّامُ حَرْفُ جَرٍّ، وَمَعْنًى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مُتَعَلِّقٌ بِالْمَوْضُوعِ.", "«for a meaning» — hangs on «set down».", "«bir mana için» — mevzû'a müteallik.", segments=[seg("لِ", "li", "prep"), seg("مَعْنًى", "mana", "noun")]),
  tok("مُفْرَدٍ", "mufrad", "noun", [K, NA], "صِفَةٌ لِمَعْنًى مَجْرُورَةٌ بِالْكَسْرَةِ.", "«single» — the na't of «meaning».", "«müfred» — mana'nın sıfatı.", punct="،"),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, "inna-wa-akhawatuha", MK], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«three» — the khabar of أَنَّ.", "«üçtür» — enne'nin haberi.", punct=":"),
 ]})

# ----------- s6 — the fi'l
S.append({"id": "s6", "translation": {"en": "a verb — and it is what points by its form, by coinage, to one of the three tenses,", "tr": "fiil — o, kalıbıyla, vaz' olarak üç zamandan birine delâlet edendir;"},
 "tokens": [
  tok("فِعْلٌ", "fil", "noun", [K, "badal", KK], "بَدَلُ تَفْصِيلٍ مِنْ ثَلَاثَةٌ مَرْفُوعٌ — أَوْ خَبَرُ مُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهَا فِعْلٌ.", "«a verb» — the first of the three spelt out.", "«fiil» — üçün tafsîl bedeli.", punct="،"),
  wahuwa("لِلِاسْتِئْنَافِ", "the waw opens the definition", "vâv isti'nâf"),
  ma_khabar(), dalla(),
  tok("بِهَيْئَتِهِ", "haya-shape", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَهَيْئَةِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: بِصِيغَتِهِ.", "«by its form» — its pattern.", "«kalıbıyla» — sîgasıyla.", segments=[seg("بِ", "bi", "prep"), seg("هَيْئَةِ", "haya-shape", "noun"), pr3msi()]),
  tok("وَضْعًا", "wad-put", "noun", [K, "hal"], "مَصْدَرٌ فِي مَوْضِعِ الْحَالِ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: دَلَالَةً وَضْعِيَّةً لَا عَقْلِيَّةً.", "«by coinage» — a masdar standing as the hal: a delalat by convention, not by reason.", "«vaz' olarak» — hâl yerinde masdar: aklî değil vaz'î delâlet."),
  ala(), *ahad_j(),
 ]})

# ----------- s7 — the fi'l's marks
S.append({"id": "s7", "translation": {"en": "and among its marks is the entering of قَدْ, the sin, سَوْفَ, إِنْ, لَمْ, لَمَّا, the lam of command and the lā of prohibition; and all of it is a governor, as will come;", "tr": "hâssalarından: kad, sin, sevfe, in, lem, lemmâ, emir lâmı ve nehiy lâ'sının dâhil olmasıdır; hepsi de âmildir, geleceği üzere;"},
 "tokens": [
  *min_khawass(),
  quoted_j("قَدْ", "qad", "part", "«qad»", "«kad»", first=True),
  tok("وَالسِّينِ", "sin-letter", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالسِّينِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ الْحَرْفِ.", "«and the sin» — the letter's name, a noun.", "«ve sin» — harfin adı, isim.", segments=wa("السِّينِ", "sin-letter", "noun")),
  quoted_j("وَسَوْفَ", "sawfa", "part", "«and sawfa»", "«ve sevfe»"),
  quoted_j("وَإِنْ", "in-shartiyya", "part", "«and in»", "«ve in»"),
  quoted_j("وَلَمْ", "lam-jazima", "part", "«and lam»", "«ve lem»"),
  quoted_j("وَلَمَّا", "lamma", "part", "«and lamma»", "«ve lemmâ»"),
  tok("وَلَامِ", "lam-letter", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَلَامِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the lam of» — the letter's name, annexed.", "«ve lâmı» — harfin adı, muzâf.", segments=wa("لَامِ", "lam-letter", "noun")),
  tok("الْأَمْرِ", "amr", "noun", [K, ID, "lam-amr"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«command»", "«emrin»"),
  tok("وَلَاءِ", "la-letter", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَلَاءِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ — اسْمُ الْحَرْفِ لَا بِالْمَدِّ.", "«and the lā of» — the letter's name lengthened, annexed.", "«ve lâ'sı» — harfin medli adı, muzâf.", segments=wa("لَاءِ", "la-letter", "noun")),
  tok("النَّهْيِ", "nahy", "noun", [K, ID, "la-nahiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«prohibition»", "«nehyin»", punct="،"),
  tok("وَكُلُّهُ", "kull", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and all of it» — the mubtada.", "«ve hepsi» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("كُلُّ", "kull", "noun"), pr3ms()]),
  tok("عَامِلٌ", "amil-governor", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a governor» — the khabar.", "«âmildir» — haber."),
  ala(),
  tok("مَا", "ma-mawsula", "pron", [K, HJ, "ism-mawsul"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«what» — the relative in jarr.", "«… üzere» — mevsûl, cer mahallinde."),
  tok("سَيَجِيءُ", "jaa", "verb", [K, "ism-mawsul"], "السِّينُ لِلِاسْتِقْبَالِ، وَيَجِيءُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«will come» — the future sin; the relative clause.", "«gelecek» — istikbal sîni; sıla.", punct="؛", segments=[seg("سَ", "sa", "part"), seg("يَجِيءُ", "jaa", "verb")]),
 ]})

# ----------- s8 — the ism
S.append({"id": "s8", "translation": {"en": "and a noun — and it is what points to a meaning self-standing in the understanding, not joined to one of the three tenses,", "tr": "ve isim — o, anlayışta kendi başına duran, üç zamandan birine yakın olmayan bir manaya delâlet edendir;"},
 "tokens": [
  tok("وَاسْمٌ", "ism", "noun", [K, AT, KK], "الْوَاوُ عَاطِفَةٌ، وَاسْمٌ مَعْطُوفٌ عَلَى فِعْلٌ مَرْفُوعٌ.", "«and a noun» — joined to «a verb».", "«ve isim» — fiil'e ma'tûf.", punct="،", segments=wa("اسْمٌ", "ism", "noun")),
  wahuwa("لِلِاسْتِئْنَافِ", "the waw opens the definition", "vâv isti'nâf"),
  ma_khabar(), dalla(), ala(), mana_j(),
  tok("مُسْتَقِلٍّ", "mustaqill", "noun", [K, NA, "ism-fail"], "صِفَةٌ لِمَعْنًى مَجْرُورَةٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنِ اسْتَقَلَّ.", "«self-standing» — the na't.", "«müstakil» — sıfat."),
  tok("بِالْفَهْمِ", "fahm", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفَهْمِ مَجْرُورٌ — مُتَعَلِّقٌ بِمُسْتَقِلٍّ.", "«in the understanding» — hangs on «self-standing».", "«anlayışta» — müstakil'e müteallik.", segments=[seg("بِ", "bi", "prep"), seg("الْفَهْمِ", "fahm", "noun")]),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "صِفَةٌ ثَانِيَةٌ لِمَعْنًى مَجْرُورَةٌ، مُضَافٌ.", "«not» — a second na't, annexed.", "«olmayan» — ikinci sıfat, muzâf."),
  tok("مُقْتَرِنٍ", "muqtarin", "noun", [K, ID, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«joined» — annexed to «not».", "«yakın» — muzâfun ileyh."),
  *ahad_j("بِأَحَدِ", clit=True),
 ]})

# ----------- s9 — the ism's marks
S.append({"id": "s9", "translation": {"en": "and among its marks is the entering of the tanwin, of the jarr letter and of the lam of definition, and its being a mubtada, a doer and an annexed head;", "tr": "hâssalarından: tenvinin, cer harfinin ve tarif lâmının dâhil olması; mübtedâ, fâil ve muzâf olmasıdır;"},
 "tokens": [
  *min_khawass(),
  tok("التَّنْوِينِ", "tanwin", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the tanwin»", "«tenvinin»"),
  tok("وَحَرْفِ", "harf", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَحَرْفِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the letter of»", "«ve harfinin»", segments=wa("حَرْفِ", "harf", "noun")),
  tok("الْجَرِّ", "jarr", "noun", [K, ID, HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr»", "«cer»"),
  tok("وَلَامِ", "lam-letter", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَلَامِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the lam of»", "«ve lâmının»", segments=wa("لَامِ", "lam-letter", "noun")),
  tok("التَّعْرِيفِ", "tarif", "noun", [K, ID, "anwa-al-lam-al-tarif"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«definition»", "«tarif»"),
  tok("وَكَوْنُهُ", "kawn", "noun", [K, AT, ID, "kana-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَكَوْنُ مَعْطُوفٌ عَلَى دُخُولُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ وَهُوَ اسْمُ الْمَصْدَرِ النَّاقِصِ.", "«and its being» — the masdar of كَانَ, joined to «entering»; the pronoun is its ism.", "«ve olması» — kâne'nin masdarı, dühûl'e ma'tûf; zamir onun ismi.", segments=[seg("وَ", "wa", "conj"), seg("كَوْنُ", "kawn", "noun"), pr3ms()]),
  tok("مُبْتَدَأً", "mubtada", "noun", [K, "kana-wa-akhawatuha", MK], "خَبَرُ الْمَصْدَرِ النَّاقِصِ كَوْن مَنْصُوبٌ بِالْفَتْحَةِ.", "«a mubtada» — the khabar of «being».", "«mübtedâ» — kevn'in haberi."),
  tok("وَفَاعِلًا", "fail-doer", "noun", [K, AT, "fail"], "الْوَاوُ عَاطِفَةٌ، وَفَاعِلًا مَعْطُوفٌ مَنْصُوبٌ.", "«and a doer»", "«ve fâil»", segments=wa("فَاعِلًا", "fail-doer", "noun")),
  tok("وَمُضَافًا", "mudaf", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَمُضَافًا مَعْطُوفٌ مَنْصُوبٌ.", "«and an annexed head»", "«ve muzâf»", punct="،", segments=wa("مُضَافًا", "mudaf", "noun")),
 ]})

# ----------- s10 — some nouns govern
S.append({"id": "s10", "translation": {"en": "and some of it governs, like the ism fāʿil, and some of it does not govern, like أَنَا، أَنْتَ and الَّذِي;", "tr": "bir kısmı âmildir, ism-i fâil gibi; bir kısmı âmil değildir, ene, ente ve ellezî gibi;"},
 "tokens": [
  tok("وَبَعْضُهُ", "bad", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and some of it» — the mubtada.", "«ve bir kısmı» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("بَعْضُ", "bad", "noun"), pr3ms()]),
  tok("عَامِلٌ", "amil-governor", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«governs» — the khabar.", "«âmildir» — haber."),
  tok("كَاسْمِ", "ism", "noun", [K, HJ, ID], "الْكَافُ حَرْفُ جَرٍّ لِلتَّمْثِيلِ، وَاسْمِ مَجْرُورٌ، مُضَافٌ.", "«like the ism» — the kaf of «for instance».", "«ism-i … gibi» — temsil kâfı.", segments=[seg("كَ", "ka", "prep"), seg("اسْمِ", "ism", "noun")]),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«fāʿil»", "«fâil»"),
  tok("وَبَعْضُهُ", "bad", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and some of it»", "«ve bir kısmı»", segments=[seg("وَ", "wa", "conj"), seg("بَعْضُ", "bad", "noun"), pr3ms()]),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«not» — the khabar, annexed.", "«değildir» — haber, muzâf."),
  tok("عَامِلٍ", "amil-governor", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a governor»", "«âmil»"),
  tok("كَأَنَا", "ana", "pron", [K, HJ, "hadhf-wa-taqdir"], "الْكَافُ لِلتَّمْثِيلِ، وَأَنَا لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ.", "«like ana» — the pronoun quoted as a word, in the place of jarr.", "«ene gibi» — lafzı kastedilmiş zamir, cer mahallinde.", segments=[seg("كَ", "ka", "prep"), seg("أَنَا", "ana", "pron")]),
  tok("وَأَنْتَ", "anta", "pron", [K, AT, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَأَنْتَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and anta»", "«ve ente»", segments=wa("أَنْتَ", "anta", "pron")),
  tok("وَالَّذِي", "alladhi", "pron", [K, AT, "ism-mawsul", "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَالَّذِي لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and alladhi»", "«ve ellezî»", punct="؛", segments=wa("الَّذِي", "alladhi", "pron")),
 ]})

# ----------- s11 — the harf
S.append({"id": "s11", "translation": {"en": "and a particle — and it is what points to a meaning not self-standing in the understanding but an instrument for understanding another; some of it governs, like the jarr letter, and some does not, like هَلْ and قَدْ.", "tr": "ve harf — o, anlayışta kendi başına durmayan, başkasını anlamaya âlet olan bir manaya delâlet edendir; bir kısmı âmildir, cer harfi gibi; bir kısmı âmil değildir, hel ve kad gibi."},
 "tokens": [
  tok("وَحَرْفٌ", "harf", "noun", [K, AT, KK], "الْوَاوُ عَاطِفَةٌ، وَحَرْفٌ مَعْطُوفٌ عَلَى فِعْلٌ مَرْفُوعٌ.", "«and a particle» — joined to «a verb».", "«ve harf» — fiil'e ma'tûf.", punct="،", segments=wa("حَرْفٌ", "harf", "noun")),
  wahuwa("لِلِاسْتِئْنَافِ", "the waw opens the definition", "vâv isti'nâf"),
  ma_khabar(), dalla(), ala(), mana_j(),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "صِفَةٌ لِمَعْنًى مَجْرُورَةٌ، مُضَافٌ.", "«not» — the na't, annexed.", "«olmayan» — sıfat, muzâf."),
  tok("مُسْتَقِلٍّ", "mustaqill", "noun", [K, ID, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«self-standing»", "«müstakil»"),
  tok("بِالْفَهْمِ", "fahm", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفَهْمِ مَجْرُورٌ.", "«in the understanding»", "«anlayışta»", segments=[seg("بِ", "bi", "prep"), seg("الْفَهْمِ", "fahm", "noun")]),
  tok("بَلْ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ وَعَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«but rather» — the particle of correction.", "«bilakis» — idrâb harfi."),
  tok("آلَةٌ", "ala-tool", "noun", [K, MK, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ — أَيْ: بَلْ هُوَ آلَةٌ.", "«an instrument» — the khabar of an omitted «it is».", "«âlettir» — mahzûf mübtedânın haberi."),
  tok("لِفَهْمِ", "fahm", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَفَهْمِ مَجْرُورٌ، مُضَافٌ — مُتَعَلِّقٌ بِآلَةٌ.", "«for understanding» — annexed.", "«anlamaya» — muzâf.", segments=[seg("لِ", "li", "prep"), seg("فَهْمِ", "fahm", "noun")]),
  tok("غَيْرِهِ", "ghayr", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another»", "«başkasını»", punct="،", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("وَبَعْضُهُ", "bad", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and some of it»", "«ve bir kısmı»", segments=[seg("وَ", "wa", "conj"), seg("بَعْضُ", "bad", "noun"), pr3ms()]),
  tok("عَامِلٌ", "amil-governor", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«governs»", "«âmildir»"),
  tok("كَحَرْفِ", "harf", "noun", [K, HJ, ID], "الْكَافُ لِلتَّمْثِيلِ، وَحَرْفِ مَجْرُورٌ، مُضَافٌ.", "«like the letter of»", "«harfi gibi»", segments=[seg("كَ", "ka", "prep"), seg("حَرْفِ", "harf", "noun")]),
  tok("الْجَرِّ", "jarr", "noun", [K, ID, HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr»", "«cer»"),
  tok("وَبَعْضُهُ", "bad", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْضُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and some of it»", "«ve bir kısmı»", segments=[seg("وَ", "wa", "conj"), seg("بَعْضُ", "bad", "noun"), pr3ms()]),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«not»", "«değildir»"),
  tok("عَامِلٍ", "amil-governor", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a governor»", "«âmil»"),
  tok("كَهَلْ", "hal-istifham", "part", [K, HJ, "hadhf-wa-taqdir"], "الْكَافُ لِلتَّمْثِيلِ، وَهَلْ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ.", "«like hal» — the particle quoted as a word.", "«hel gibi» — hikâye edilmiş harf.", segments=[seg("كَ", "ka", "prep"), seg("هَلْ", "hal-istifham", "part")]),
  tok("وَقَدْ", "qad", "part", [K, AT, "hadhf-wa-taqdir", "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and qad»", "«ve kad»", punct=".", segments=wa("قَدْ", "qad", "part")),
 ]})

# ----------- s12 — the amil defined
S.append({"id": "s12", "translation": {"en": "Then the governor is what makes, through its means, the end of the word be in a specific manner of iʿrab.", "tr": "Sonra âmil, kelimenin sonunun i'râbdan belirli bir vecih üzere olmasını kendi vasıtasıyla gerektirendir."},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ الذِّكْرِيِّ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«then» — the ordering particle.", "«sonra» — tertip harfi."),
  tok("الْعَامِلُ", "amil-governor", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the governor» — the mubtada.", "«âmil» — mübtedâ."),
  tok("هُوَ", "huwa", "pron", [K, "damir-fasl", MK], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ — وَيَجُوزُ كَوْنُهُ مُبْتَدَأً ثَانِيًا.", "«it is» — the pronoun of separation (or a second mubtada).", "«o» — fasıl zamiri (ya da ikinci mübtedâ)."),
  ma_khabar(),
  tok("أَوْجَبَ", "awjaba", "verb", [K, "ism-mawsul"], "مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«makes necessary» — the relative clause.", "«gerektirir» — sıla."),
  tok("بِوَاسِطَتِهِ", "wasita", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَوَاسِطَةِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«through its means»", "«vasıtasıyla»", segments=[seg("بِ", "bi", "prep"), seg("وَاسِطَةِ", "wasita", "noun"), pr3msi()]),
  tok("كَوْنَ", "kawn", "noun", [K, "maful-bihi", ID, "kana-wa-akhawatuha"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مَصْدَرُ كَانَ النَّاقِصَةِ.", "«the being» — the object; the masdar of كَانَ, annexed.", "«olmasını» — mef'ûl; kâne'nin masdarı, muzâf."),
  tok("آخِرِ", "akhir", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — وَهُوَ اسْمُ الْمَصْدَرِ النَّاقِصِ.", "«the end of» — annexed; the ism of «being».", "«sonunun» — muzâfun ileyh; kevn'in ismi."),
  tok("الْكَلِمَةِ", "kalima", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the word»", "«kelimenin»"),
  ala(),
  tok("وَجْهٍ", "wajh", "noun", [K, HJ, "kana-wa-akhawatuha"], "مَجْرُورٌ بِعَلَى — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ الْمَصْدَرِ النَّاقِصِ.", "«a manner» — the jarr phrase is the khabar of «being».", "«bir vecih» — câr-mecrûr kevn'in haberi."),
  tok("مَخْصُوصٍ", "makhsus", "noun", [K, NA, "ism-maful"], "صِفَةٌ لِوَجْهٍ مَجْرُورَةٌ.", "«specific» — the na't.", "«belirli» — sıfat."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of» — the explaining min.", "«-den» — beyan için min."),
  tok("الْإِعْرَابِ", "irab", "noun", [K, HJ], "مَجْرُورٌ بِمِنْ.", "«iʿrab»", "«i'râb»", punct="."),
 ]})

# ----------- s13 — lafzi / ma'nawi
S.append({"id": "s13", "translation": {"en": "Then the governor is of two kinds: of the wording and of the sense.", "tr": "Sonra âmil iki türlüdür: lafzî ve ma'nevî."},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.", "«then»", "«sonra»"),
  tok("الْعَامِلُ", "amil-governor", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the governor» — the mubtada.", "«âmil» — mübtedâ."),
  ala(),
  tok("ضَرْبَيْنِ", "darb", "noun", [K, HJ, MK, "al-muthanna"], "مَجْرُورٌ بِعَلَى، وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«two kinds» — the dual, in jarr by the ya; the phrase is the khabar.", "«iki tür» — tesniye, yâ ile mecrûr; câr-mecrûr haber.", punct=":"),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, MK, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ — أَيْ: أَحَدُهُمَا لَفْظِيٌّ.", "«of the wording» — the khabar of an omitted «one of them».", "«lafzî» — mahzûf mübtedânın haberi."),
  tok("وَمَعْنَوِيٌّ", "manawi", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَمَعْنَوِيٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and of the sense»", "«ve ma'nevî»", punct=".", segments=wa("مَعْنَوِيٌّ", "manawi", "noun")),
 ]})

# ----------- s14 — the lafzi, and sama'i / qiyasi
S.append({"id": "s14", "translation": {"en": "The one of the wording is what the tongue has a share in; and it is of two kinds: heard and by rule.", "tr": "Lafzî olan, dilin onda payı olandır; o da iki türlüdür: semâî ve kıyâsî."},
 "tokens": [
  tok("فَاللَّفْظِيُّ", "lafzi", "noun", [K, MK], "الْفَاءُ لِلتَّفْصِيلِ، وَاللَّفْظِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«the one of the wording» — the fa of detailing; the mubtada.", "«lafzî olan» — tafsîl fâsı; mübtedâ.", segments=fa("اللَّفْظِيُّ", "lafzi", "noun")),
  ma_khabar(),
  tok("يَكُونُ", "kana", "verb", [K, "kana-wa-akhawatuha", "ism-mawsul"], "مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُؤَخَّرٌ: حَظٌّ — صِلَةُ الْمَوْصُولِ.", "«there is» — kāna, its ism delayed.", "«olur» — nâkıs kâne, ismi muahhar."),
  tok("لِلِّسَانِ", "lisan", "noun", [K, HJ, "kana-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ، وَاللِّسَانِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُ مُقَدَّمٌ.", "«for the tongue» — the fronted khabar of kāna.", "«dil için» — kâne'nin mukaddem haberi.", segments=[seg("لِ", "li", "prep"), seg("اللِّسَانِ", "lisan", "noun")]),
  tok("فِيهِ", "fi", "prep", [K, HJ, "ism-mawsul"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَهُوَ الْعَائِدُ.", "«in it» — the returning pronoun.", "«onda» — âid zamir.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("حَظٌّ", "hazz", "noun", [K, "kana-wa-akhawatuha"], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a share» — the delayed ism of kāna.", "«bir pay» — kâne'nin muahhar ismi.", punct="،"),
  wahuwa("عَاطِفَةٌ", "the waw joins", "vâv atıf"),
  ala(),
  tok("ضَرْبَيْنِ", "darb", "noun", [K, HJ, MK, "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«two kinds»", "«iki tür»", punct=":"),
  tok("سَمَاعِيٌّ", "samai", "noun", [K, MK, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ.", "«heard»", "«semâî»"),
  tok("وَقِيَاسِيٌّ", "qiyasi", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقِيَاسِيٌّ مَعْطُوفٌ مَرْفُوعٌ.", "«and by rule»", "«ve kıyâsî»", punct=".", segments=wa("قِيَاسِيٌّ", "qiyasi", "noun")),
 ]})

# ----------- s15 — the sama'i
S.append({"id": "s15", "translation": {"en": "The heard one is that whose governing depends on hearing; and it, too, is of two sorts: a governor in the noun and a governor in the muḍāriʿ.", "tr": "Semâî, i'mâli semâ'a bağlı olandır; o da iki nevidir: isimde âmil ve muzâride âmil."},
 "tokens": [
  tok("فَالسَّمَاعِيُّ", "samai", "noun", [K, MK], "الْفَاءُ لِلتَّفْصِيلِ، وَالسَّمَاعِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«the heard one» — the mubtada.", "«semâî» — mübtedâ.", segments=fa("السَّمَاعِيُّ", "samai", "noun")),
  tok("هُوَ", "huwa", "pron", [K, "damir-fasl", MK], "ضَمِيرُ فَصْلٍ — أَوْ مُبْتَدَأٌ ثَانٍ.", "«is» — the pronoun of separation.", "«o» — fasıl zamiri."),
  tok("الَّذِي", "alladhi", "pron", [K, "ism-mawsul", MK], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«the one that» — the relative, the khabar.", "«… olan» — mevsûl, haber."),
  tok("يَتَوَقَّفُ", "tawaqqafa", "verb", [K, "ism-mawsul", "fail"], "مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — صِلَةٌ.", "«depends» — the relative clause.", "«bağlıdır» — sıla."),
  tok("إِعْمَالُهُ", "imal", "noun", [K, "fail", ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَهُوَ الْعَائِدُ.", "«its governing» — the doer; the pronoun returns.", "«i'mâli» — fâil; zamir âid.", segments=[seg("إِعْمَالُ", "imal", "noun"), pr3ms()]),
  ala(),
  tok("السَّمَاعِ", "samaa", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«hearing»", "«semâ'a»", punct="،"),
  wahuwa("عَاطِفَةٌ", "the waw joins", "vâv atıf"),
  tok("أَيْضًا", "aydan", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ — مَنْصُوبٌ بِالْفَتْحَةِ.", "«also» — the absolute object of an omitted آضَ.", "«da» — mahzûf fiilin mef'ûl-i mutlakı."),
  ala(),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MK, "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«two sorts»", "«iki nevi»", punct=":"),
  *amil_fi("الِاسْمِ", "ism", "the noun", "isimde", joined=False),
  *amil_fi("الْمُضَارِعِ", "mudari", "the muḍāriʿ", "muzâride", punct=".", extra_what=["mudari-marfu"]),
 ]})

# ----------- s16 — in one noun / in two nouns
S.append({"id": "s16", "translation": {"en": "And the governor in the noun is, again, of two divisions: a governor in one noun and a governor in two nouns — I mean the mubtada and the khabar originally, and after the governor enters they are called its ism and its khabar.", "tr": "İsimdeki âmil de iki kısımdır: bir isimde âmil ve iki isimde âmil — aslında mübtedâ ile haberi kastediyorum; âmil dâhil olduktan sonra onun ismi ve haberi diye adlandırılırlar."},
 "tokens": [
  tok("وَالْعَامِلُ", "amil-governor", "noun", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the governor» — the mubtada.", "«âmil» — mübtedâ.", segments=wa("الْعَامِلُ", "amil-governor", "noun")),
  fi(),
  tok("الِاسْمِ", "ism", "noun", [K, HJ], "مَجْرُورٌ بِفِي — مُتَعَلِّقٌ بِالْعَامِلِ.", "«the noun»", "«isimde»"),
  tok("أَيْضًا", "aydan", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ.", "«again»", "«de»"),
  ala(),
  tok("قِسْمَيْنِ", "qism", "noun", [K, HJ, MK, "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«two divisions»", "«iki kısım»", punct=":"),
  *amil_fi("اسْمٍ", "ism", "a noun", "bir isimde", joined=False),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "صِفَةٌ لِاسْمٍ مَجْرُورَةٌ.", "«one» — the na't.", "«bir» — sıfat."),
  *amil_fi("اسْمَيْنِ", "ism", "two nouns", "iki isimde", punct="،", extra_what=["al-muthanna"]),
  tok("أَعْنِي", "ana-mean", "verb", [K, "fail", "ism-maqsur-manqus"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّفْسِيرِ.", "«I mean» — a naqis verb, its damma estimated; a parenthetical clause.", "«kastediyorum» — nâkıs fiil, dammesi takdîrî; tefsir için mu'terize."),
  tok("الْمُبْتَدَأَ", "mubtada", "noun", [K, "maful-bihi", MK], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the mubtada» — the object.", "«mübtedâyı» — mef'ûl."),
  tok("وَالْخَبَرَ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرَ مَعْطُوفٌ مَنْصُوبٌ.", "«and the khabar»", "«ve haberi»", segments=wa("الْخَبَرَ", "khabar-predicate", "noun")),
  fi(),
  tok("الْأَصْلِ", "asl", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«originally»", "«aslında»", punct="،"),
  tok("وَيُسَمَّيَانِ", "samma", "verb", [K, "naib-al-fail", "mafulayn", "al-muthanna"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّيَانِ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ — وَهُوَ الْمَفْعُولُ الْأَوَّلُ.", "«and they two are called» — passive; the alif is the deputy doer (the first object).", "«ve adlandırılırlar» — meçhul; elif nâib-i fâil (birinci mef'ûl).", segments=wa("يُسَمَّيَانِ", "samma", "verb")),
  tok("بَعْدَ", "bada", "noun", [K, "maful-fih", ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«after» — the zarf, annexed.", "«sonra» — zarf, muzâf."),
  tok("دُخُولِ", "dukhul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the entering of»", "«dâhil olmasından»"),
  tok("الْعَامِلِ", "amil-governor", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governor»", "«âmilin»"),
  tok("اسْمًا", "ism", "noun", [K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«an ism» — the second object.", "«isim» — ikinci mef'ûl."),
  tok("وَخَبَرًا", "khabar-predicate", "noun", [K, AT, "mafulayn"], "الْوَاوُ عَاطِفَةٌ، وَخَبَرًا مَعْطُوفٌ مَنْصُوبٌ.", "«and a khabar»", "«ve haber»", segments=wa("خَبَرًا", "khabar-predicate", "noun")),
  tok("لَهُ", "li", "prep", [K, HJ, NA], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِاسْمًا وَخَبَرًا.", "«its» — the jarr phrase qualifies both.", "«onun» — câr-mecrûr ikisinin sıfatı.", punct=".", segments=[seg("لَ", "li", "prep"), pr3ms()]),
 ]})

# ----------- s17 — the twenty letters announced
S.append({"id": "s17", "translation": {"en": "And the governor in one noun is letters that put it in jarr, called the letters of jarr and the letters of annexation; and they are twenty:", "tr": "Bir isimdeki âmil, onu cer eden harflerdir; cer harfleri ve izâfet harfleri diye adlandırılırlar; onlar yirmidir:"},
 "tokens": [
  tok("وَالْعَامِلُ", "amil-governor", "noun", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the governor» — the mubtada.", "«âmil» — mübtedâ.", segments=wa("الْعَامِلُ", "amil-governor", "noun")),
  fi(),
  tok("اسْمٍ", "ism", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«a noun»", "«bir isimde»"),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "صِفَةٌ لِاسْمٍ مَجْرُورَةٌ.", "«one»", "«bir»"),
  tok("حُرُوفٌ", "harf", "noun", [K, MK, "jam-taksir"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ حَرْفٍ.", "«letters» — the khabar.", "«harflerdir» — haber."),
  tok("تَجُرُّهُ", "jarra", "verb", [K, "jumla-sifa", "doubled-verbs", "maful-bihi"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِفَةٌ لِحُرُوفٌ.", "«that put it in jarr» — a clause qualifying «letters»; the ha its object.", "«onu cer eden» — hurûf'un sıfatı olan cümle; hâ mef'ûl.", segments=[seg("تَجُرُّ", "jarra", "verb"), pr3ms()]),
  tok("تُسَمَّى", "samma", "verb", [K, "jumla-sifa", "naib-al-fail", "mafulayn"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — صِفَةٌ ثَانِيَةٌ.", "«called» — passive, its deputy doer concealed; a second qualifying clause.", "«adlandırılan» — meçhul; ikinci sıfat cümlesi."),
  tok("حُرُوفَ", "harf", "noun", [K, "mafulayn", ID], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the letters of» — the second object, annexed.", "«harfleri» — ikinci mef'ûl, muzâf."),
  tok("الْجَرِّ", "jarr", "noun", [K, ID, HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr»", "«cer»"),
  tok("وَحُرُوفَ", "harf", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَحُرُوفَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and the letters of»", "«ve harfleri»", segments=wa("حُرُوفَ", "harf", "noun")),
  tok("الْإِضَافَةِ", "idafa", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«annexation»", "«izâfet»", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, MK], "الْوَاوُ عَاطِفَةٌ، وَهِيَ مُبْتَدَأٌ.", "«and they» — the mubtada.", "«ve onlar» — mübtedâ.", segments=wa("هِيَ", "hiya", "pron")),
  tok("عِشْرُونَ", "ishrun", "noun", [K, MK, "jam-mudhakkar-salim"], "خَبَرٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«twenty» — raf' by the waw.", "«yirmidir» — ref'i vâv iledir.", punct=":"),
 ]})

# ----------- s18 — the first five
S.append({"id": "s18", "translation": {"en": "The bāʾ for attachment, مِنْ for the starting point, إِلَى for the end point, عَنْ for distance and passing beyond, عَلَى for being above,", "tr": "Bâ ilsâk için, min ibtidâ için, ilâ intihâ için, an uzaklık ve mücâvezet için, alâ isti'lâ için,"},
 "tokens": [
  tok("الْبَاءُ", "ba-harf", "noun", [K, HJ, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ الْحَرْفِ.", "«the bāʾ» — the letter's name, the mubtada.", "«bâ» — harfin adı, mübtedâ."),
  li_khabar("لِلْإِلْصَاقِ", "ilsaq", "attachment", "ilsâk", punct="،"),
  quoted_mubt("وَمِنْ", "min", "prep", "«and min»", "«ve min»"),
  li_khabar("لِلِابْتِدَاءِ", "ibtida-start", "the starting point", "ibtidâ", punct="،"),
  quoted_mubt("وَإِلَى", "ila", "prep", "«and ilā»", "«ve ilâ»"),
  li_khabar("لِلِانْتِهَاءِ", "intiha", "the end point", "intihâ", punct="،"),
  quoted_mubt("وَعَنْ", "an", "prep", "«and ʿan»", "«ve an»"),
  li_khabar("لِلْبُعْدِ", "bud-distance", "distance", "uzaklık"),
  tok("وَالْمُجَاوَزَةِ", "mujawaza", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالْمُجَاوَزَةِ مَعْطُوفٌ مَجْرُورٌ.", "«and passing beyond»", "«ve mücâvezet»", punct="،", segments=wa("الْمُجَاوَزَةِ", "mujawaza", "noun")),
  quoted_mubt("وَعَلَى", "ala", "prep", "«and ʿalā»", "«ve alâ»"),
  li_khabar("لِلِاسْتِعْلَاءِ", "istila", "being above", "isti'lâ", punct="،"),
 ]})

# ----------- s19 — lam, fi, kaf, hatta, rubba, the oath's waw and ta
S.append({"id": "s19", "translation": {"en": "the lām for cause and for specification, فِي for containment, the kāf for likening, حَتَّى for the limit, رُبَّ for fewness, the wāw of the oath and its tāʾ,", "tr": "lâm ta'lîl ve tahsîs için, fî zarfiyet için, kâf teşbih için, hattâ gâye için, rubbe taklîl için, kasem vâvı ve tâsı,"},
 "tokens": [
  tok("وَاللَّامُ", "lam-letter", "noun", [K, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ الْحَرْفِ.", "«and the lām» — the letter's name, the mubtada.", "«ve lâm» — harfin adı, mübtedâ.", segments=wa("اللَّامُ", "lam-letter", "noun")),
  li_khabar("لِلتَّعْلِيلِ", "talil", "cause", "ta'lîl", extra=["lam-taleel"]),
  tok("وَالتَّخْصِيصِ", "takhsis", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالتَّخْصِيصِ مَعْطُوفٌ مَجْرُورٌ.", "«and specification»", "«ve tahsîs»", punct="،", segments=wa("التَّخْصِيصِ", "takhsis", "noun")),
  quoted_mubt("وَفِي", "fi", "prep", "«and fī»", "«ve fî»"),
  li_khabar("لِلظَّرْفِ", "zarf", "containment", "zarfiyet", punct="،"),
  tok("وَالْكَافُ", "kaf-letter", "noun", [K, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the kāf» — the mubtada.", "«ve kâf» — mübtedâ.", segments=wa("الْكَافُ", "kaf-letter", "noun")),
  li_khabar("لِلتَّشْبِيهِ", "tashbih", "likening", "teşbih", punct="،"),
  quoted_mubt("وَحَتَّى", "hatta", "part", "«and ḥattā»", "«ve hattâ»"),
  li_khabar("لِلْغَايَةِ", "ghaya", "the limit", "gâye", punct="،"),
  quoted_mubt("وَرُبَّ", "rubba", "part", "«and rubba»", "«ve rubbe»"),
  li_khabar("لِلتَّقْلِيلِ", "taqlil", "fewness", "taklîl", punct="،"),
  tok("وَوَاوُ", "waw-letter", "noun", [K, HJ, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَوَاوُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَخَبَرُهُ مَحْذُوفٌ: لِلْقَسَمِ.", "«and the wāw of» — the mubtada, annexed; its khabar «for the oath» omitted.", "«ve vâvı» — mübtedâ, muzâf; haberi mahzûf: kasem için.", segments=wa("وَاوُ", "waw-letter", "noun")),
  tok("الْقَسَمِ", "qasam", "noun", [K, ID, "anwa-al-waw"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the oath»", "«kasemin»"),
  tok("وَتَاؤُهُ", "ta-letter", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَتَاءُ مَعْطُوفٌ عَلَى وَاوُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its tāʾ» — joined to «the wāw»; annexed to the oath's pronoun.", "«ve tâsı» — vâv'a ma'tûf; zamire muzâf.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("تَاءُ", "ta-letter", "noun"), pr3ms()]),
 ]})

# ----------- s20 — hasha, mudh/mundhu, khala/ada
S.append({"id": "s20", "translation": {"en": "حَاشَا for exception; مُذْ and مُنْذُ for the starting point in past time — and they may both be nouns; خَلَا and عَدَا for exception — and they may both be verbs, which is the commoner;", "tr": "hâşâ istisnâ için; müz ve münzü geçmiş zamanda ibtidâ için — ikisi isim de olabilir; halâ ve adâ istisnâ için — ikisi fiil de olabilir, daha çok olan budur;"},
 "tokens": [
  quoted_mubt("وَحَاشَا", "hasha", "part", "«and ḥāshā»", "«ve hâşâ»"),
  li_khabar("لِلِاسْتِثْنَاءِ", "istithna", "exception", "istisnâ", punct="،", extra=["istithna"]),
  quoted_mubt("وَمُذْ", "mudh", "prep", "«and mudh»", "«ve müz»"),
  tok("وَمُنْذُ", "mundhu", "prep", [K, HJN, AT, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَمُنْذُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى مُذْ فِي مَحَلِّ رَفْعٍ.", "«and mundhu» — joined to مُذْ.", "«ve münzü» — müz'e ma'tûf.", segments=wa("مُنْذُ", "mundhu", "prep")),
  li_khabar("لِلِابْتِدَاءِ", "ibtida-start", "the starting point", "ibtidâ"),
  fi(),
  tok("الزَّمَانِ", "zaman", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«time»", "«zamanda»"),
  tok("الْمَاضِي", "madi", "noun", [K, NA, "ism-maqsur-manqus"], "صِفَةٌ لِلزَّمَانِ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.", "«past» — a manqus noun, its kasra estimated.", "«geçmiş» — manqûs isim, kesresi takdîrî."),
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«and sometimes» — qad of fewness before the muḍāriʿ.", "«bazen» — muzâri ile taklîl kad'ı.", segments=wa("قَدْ", "qad", "part")),
  tok("يَكُونَانِ", "kana", "verb", [K, "kana-wa-akhawatuha", "al-muthanna"], "مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ اسْمُهُ.", "«they two may be» — kāna; the alif is its ism.", "«ikisi olur» — kâne; elif ismi."),
  tok("اسْمَيْنِ", "ism", "noun", [K, "kana-wa-akhawatuha", "al-muthanna"], "خَبَرُ يَكُونَانِ مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُثَنًّى.", "«nouns» — the khabar of kāna, in nasb by the ya.", "«isim» — kâne'nin haberi, yâ ile mansûb.", punct="،"),
  quoted_mubt("وَخَلَا", "khala", "verb", "«and khalā»", "«ve halâ»"),
  tok("وَعَدَا", "ada-except", "part", [K, HJN, AT, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَعَدَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى خَلَا فِي مَحَلِّ رَفْعٍ.", "«and ʿadā» — joined to خَلَا.", "«ve adâ» — halâ'ya ma'tûf.", segments=wa("عَدَا", "ada-except", "part")),
  li_khabar("لِلِاسْتِثْنَاءِ", "istithna", "exception", "istisnâ", extra=["istithna"]),
  tok("وَيَكُونَانِ", "kana", "verb", [K, "kana-wa-akhawatuha", "al-muthanna"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَكُونَانِ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ اسْمُهُ.", "«and they two may be»", "«ve ikisi olur»", segments=wa("يَكُونَانِ", "kana", "verb")),
  tok("فِعْلَيْنِ", "fil", "noun", [K, "kana-wa-akhawatuha", "al-muthanna"], "خَبَرُ يَكُونَانِ مَنْصُوبٌ بِالْيَاءِ.", "«verbs» — the khabar in nasb by the ya.", "«fiil» — yâ ile mansûb haber."),
  wahuwa("لِلْحَالِ", "the waw of the hal clause", "hâl vâvı"),
  tok("الْأَكْثَرُ", "akthar", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the commoner» — the khabar.", "«daha çok olan» — haber.", punct="،"),
 ]})

# ----------- s21 — lawla, kay, la'alla
S.append({"id": "s21", "translation": {"en": "لَوْلَا for the non-occurrence of a thing because another exists, when a pronoun attaches to it; كَيْ for cause, when it enters on the interrogative مَا; and لَعَلَّ for hope, in the dialect of ʿUqayl.", "tr": "levlâ, bir şeyin başkasının varlığı yüzünden olmaması için — kendisine zamir bitiştiğinde; key, istifham mâ'sına dâhil olduğunda ta'lîl için; lealle de Ukayl lügatinde terecci için."},
 "tokens": [
  quoted_mubt("وَلَوْلَا", "lawla", "part", "«and lawlā»", "«ve levlâ»"),
  tok("لِامْتِنَاعِ", "imtina", "noun", [K, HJ, MK, ID], "اللَّامُ حَرْفُ جَرٍّ، وَامْتِنَاعِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the non-occurrence of» — the khabar, annexed.", "«olmaması için» — haber, muzâf.", segments=[seg("لِ", "li", "prep"), seg("امْتِنَاعِ", "imtina", "noun")]),
  tok("شَيْءٍ", "shay", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing»", "«bir şeyin»"),
  tok("لِوُجُودِ", "wujud", "noun", [K, HJ, ID, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَوُجُودِ مَجْرُورٌ، مُضَافٌ.", "«because of the existence of» — the lam of cause.", "«varlığı yüzünden» — ta'lîl lâmı.", segments=[seg("لِ", "li", "prep"), seg("وُجُودِ", "wujud", "noun")]),
  tok("غَيْرِهِ", "ghayr", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another»", "«başkasının»", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ.", "«when» — the conditional time-adverb.", "«-dığında» — şart manalı zarf."),
  tok("اتَّصَلَ", "ittasala", "verb", [K, "idha-shartiyya", "fail"], "مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — فِعْلُ الشَّرْطِ.", "«attaches» — the shart verb.", "«bitişir» — şart fiili."),
  tok("بِهَا", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — تَعُودُ عَلَى لَوْلَا.", "«to it» — the pronoun returns to لَوْلَا.", "«ona» — levlâ'ya âid.", segments=[seg("بِ", "bi", "prep"), pr3fs()]),
  tok("ضَمِيرٌ", "damir", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a pronoun» — the doer.", "«bir zamir» — fâil.", punct="،"),
  quoted_mubt("وَكَيْ", "kay", "part", "«and kay»", "«ve key»"),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ فِي مَحَلِّ نَصْبٍ.", "«when»", "«-dığında»"),
  tok("دَخَلَ", "dakhala", "verb", [K, "idha-shartiyya"], "مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — فِعْلُ الشَّرْطِ.", "«it enters» — the shart verb, its doer concealed.", "«dâhil olur» — şart fiili, fâili müstetir."),
  ala(),
  tok("مَا", "ma-istifhamiyya", "pron", [K, HJ, "anwa-ma", "hadhf-wa-taqdir"], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ بِعَلَى.", "«mā» — quoted as a word, in the place of jarr.", "«mâ» — hikâye edilmiş, cer mahallinde."),
  tok("الِاسْتِفْهَامِيَّةِ", "istifhami", "noun", [K, NA], "صِفَةٌ لِمَا مَجْرُورَةٌ بِالْكَسْرَةِ.", "«the interrogative» — the na't of مَا.", "«istifham» — mâ'nın sıfatı."),
  li_khabar("لِلتَّعْلِيلِ", "talil", "cause", "ta'lîl", punct="،"),
  quoted_mubt("وَلَعَلَّ", "laalla", "part", "«and laʿalla»", "«ve lealle»"),
  li_khabar("لِلتَّرَجِّي", "tarajji", "hope", "terecci", extra=["ism-maqsur-manqus"]),
  fi(),
  tok("لُغَةِ", "lugha", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the dialect of» — annexed.", "«lügatinde» — muzâf."),
  tok("عُقَيْلٍ", "uqayl", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ قَبِيلَةٍ مُنْصَرِفٌ لِإِرَادَةِ الْحَيِّ.", "«ʿUqayl» — the tribe, declined as a munsarif name.", "«Ukayl» — kabile adı, munsarif.", punct="."),
 ]})

# ---------------------------------------------------------------- the lexicon
GLOSS_ADD = {}
CAND = {
 "risala-treatise": G("risala-treatise", "رِسَالَة", "ر س ل", "noun", "a treatise, an epistle", "risâle", 5, plural="رَسَائِل"),
 "murib": G("murib", "مُعْرِب", "ع ر ب", "noun", "one who parses, who gives the iʿrab (ism fāʿil of أَعْرَبَ)", "mu'rib — i'râb eden", 6),
 "ihtiyaj": G("ihtiyaj", "اِحْتِيَاج", "ح و ج", "noun", "need (masdar of اِحْتَاجَ)", "ihtiyaç (masdar)", 5),
 "amil-governor": G("amil-governor", "الْعَامِل", "ع م ل", "noun", "the ʿāmil — the governor, what gives the word after it its case", "âmil — sonraki kelimenin sonunu belirleyen", 5, plural="عَوَامِل"),
 "mamul": G("mamul", "الْمَعْمُول", "ع م ل", "noun", "the maʿmūl — the governed word", "ma'mûl — âmilin tesir ettiği kelime", 5),
 "amal-governing": G("amal-governing", "الْعَمَل", "ع م ل", "noun", "the ʿamal — the governing, the effect of the governor; here the iʿrab itself", "amel — âmilin tesiri; burada i'râbın kendisi", 5),
 "sin-letter": G("sin-letter", "السِّين", None, "noun", "the letter sīn — named as a noun; here the prefix of the near future", "sin harfi — isim olarak; burada yakın gelecek sîni", 6),
 "la-letter": G("la-letter", "لَاء", None, "noun", "the name of the letter lā, lengthened — لَاءُ النَّهْيِ", "lâ harfinin medli adı — lâü'n-nehy", 6),
 "mustaqill": G("mustaqill", "مُسْتَقِلّ", "ق ل ل", "noun", "self-standing, independent (ism fāʿil of اِسْتَقَلَّ)", "müstakil, kendi başına duran", 5),
 "mubtada": G("mubtada", "الْمُبْتَدَأ", "ب د أ", "noun", "the mubtada — the subject a nominal sentence opens with", "mübtedâ — isim cümlesinin öznesi", 4),
 "hazz": G("hazz", "حَظّ", "ح ظ ظ", "noun", "a share, a portion", "hisse, pay", 5),
 "samai": G("samai", "سَمَاعِيّ", "س م ع", "noun", "heard — known only by transmission, not by rule (nisba)", "semâî — kuralla değil işitmekle bilinen", 5),
 "qiyasi": G("qiyasi", "قِيَاسِيّ", "ق ي س", "noun", "by rule, regular (nisba)", "kıyâsî — kurala bağlı", 5),
 "imal": G("imal", "إِعْمَال", "ع م ل", "noun", "making govern, letting a governor act (masdar of أَعْمَلَ)", "i'mâl — âmil kılma", 6),
 "mudari": G("mudari", "الْمُضَارِع", "ض ر ع", "noun", "the muḍāriʿ — the present-future verb, «the one that resembles» the noun", "muzâri — isme benzeyen geniş zaman fiili", 3),
 "khabar-predicate": G("khabar-predicate", "الْخَبَر", "خ ب ر", "noun", "the khabar — the predicate of a nominal sentence", "haber — isim cümlesinin yüklemi", 4),
 "ilsaq": G("ilsaq", "إِلْصَاق", "ل ص ق", "noun", "attachment — the bāʾ's meaning (masdar of أَلْصَقَ)", "ilsâk — yapıştırma, bâ'nın manası", 6),
 "mujawaza": G("mujawaza", "مُجَاوَزَة", "ج و ز", "noun", "passing beyond (masdar of جَاوَزَ)", "mücâvezet — aşıp geçme", 6),
 "zarf": G("zarf", "ظَرْف", "ظ ر ف", "noun", "a container; the adverb of time or place, and the sense of «in»", "zarf — kap; zaman ve mekân zarfı; «içinde» manası", 4, plural="ظُرُوف"),
 "rubba": G("rubba", "رُبَّ", None, "part", "«many a…», «sometimes» — the jarr letter of fewness", "rubbe — azlık bildiren cer harfi", 5),
 "taqlil": G("taqlil", "تَقْلِيل", "ق ل ل", "noun", "making few; the sense of fewness (masdar of قَلَّلَ)", "taklîl — azlık manası", 6),
 "qasam": G("qasam", "قَسَم", "ق س م", "noun", "an oath", "yemin, kasem", 4, plural="أَقْسَام"),
 "ta-letter": G("ta-letter", "تَاء", None, "noun", "the letter tāʾ — named as a noun; here the tāʾ of the oath (تَاللهِ)", "tâ harfi — isim olarak; burada kasem tâsı", 6),
 "hasha": G("hasha", "حَاشَا", None, "part", "«except» — the jarr letter of exception", "hâşâ — istisnâ cer harfi", 5),
 "mudh": G("mudh", "مُذْ", None, "prep", "since (the short form of مُنْذُ) — a jarr letter, or a noun", "müz — münzü'nün kısası; cer harfi ya da isim", 5),
 "madi": G("madi", "الْمَاضِي", "م ض ي", "noun", "the past; the past-tense verb (ism fāʿil of مَضَى)", "mâzî — geçmiş; geçmiş zaman fiili", 3),
 "ada-except": G("ada-except", "عَدَا", "ع د و", "part", "«except» — exceptive: a jarr letter, or more often a verb", "adâ — istisnâ: cer harfi ya da daha çok fiil", 5),
 "imtina": G("imtina", "اِمْتِنَاع", "م ن ع", "noun", "not coming about, being prevented (masdar of اِمْتَنَعَ)", "imtinâ — meydana gelmeme", 6),
 "kay": G("kay", "كَيْ", None, "part", "«so that» — a nāṣib of the muḍāriʿ; before the interrogative مَا, a jarr letter of cause", "key — muzâriyi nasb eder; istifham mâ'sından önce ta'lîl cer harfi", 4),
 "ma-istifhamiyya": G("ma-istifhamiyya", "مَا (الِاسْتِفْهَامِيَّة)", None, "pron", "what? — the interrogative mā", "ne? — istifham mâ'sı", 4),
 "istifhami": G("istifhami", "اِسْتِفْهَامِيّ", "ف ه م", "noun", "interrogative (nisba of اِسْتِفْهَام)", "istifhâmî — soru bildiren", 6),
 "tarajji": G("tarajji", "تَرَجٍّ (التَّرَجِّي)", "ر ج و", "noun", "hoping for what may come — the sense of لَعَلَّ (masdar of تَرَجَّى)", "terecci — umma, lealle'nin manası", 6),
 "uqayl": G("uqayl", "عُقَيْل", "ع ق ل", "propn", "ʿUqayl — the Arab tribe in whose dialect لَعَلَّ governs jarr", "Ukayl — lealle'nin cer ettiği lehçenin kabilesi", 6),
 "tawaqqafa": G("tawaqqafa", "تَوَقَّفَ", "و ق ف", "verb", "to depend on, to hinge on (عَلَى)", "bağlı olmak, -e mütevakkıf olmak", 5),
 "ana-mean": G("ana-mean", "عَنَى", "ع ن ي", "verb", "to mean, to intend — أَعْنِي: I mean", "demek istemek, kastetmek — a'nî: kastediyorum", 5),
}
_used = []
for s in S:
    for t in s["tokens"]:
        _used.append(t["lex"])
        for sg in t.get("segments") or []: _used.append(sg["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tawaqqafa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَوَقَّف", "تَوَقَّف", "تَوَقَّف", "تَوَقُّف", "مُتَوَقِّف", "مُتَوَقَّف (عَلَيْهِ)", None, None, "تَوَقَّفَ الشَّيْءُ عَلَى الشَّيْءِ يَتَوَقَّفُ: لَمْ يَحْصُلْ إِلَّا بِهِ — لَازِمٌ، يَتَعَدَّى بِعَلَى."))
put_morph(mo, "ana-mean", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "عَنَ", "عْن", "i", "اِعْن", "عَنْي", "عَانٍ", "مَعْنِيّ", "عُنِيَ", "يُعْنَى", "عَنَى يَعْنِي: قَصَدَ وَأَرَادَ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ أَعْنِي: أَقْصِدُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch1 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": K,
 "title": {"ar": "الْعَامِلُ وَأَقْسَامُهُ", "en": "The governor and its divisions: the Izhar's opening", "tr": "Âmil ve kısımları: İzhâr'ın açılışı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الباب الأول في العامل", "العوامل للبركوي — العوامل اللفظية السماعية", "الكافية لابن الحاجب — الكلمة وأقسامها"],
 "amil": "ثَلَاثَةُ أَشْيَاءَ: الْعَامِلُ وَالْمَعْمُولُ وَالْعَمَلُ — the three things every parser needs; this note is the first of them",
 "question": {
  "en": ["What does every parser need? Three things, says the Izhar's first sentence: the GOVERNOR (what gives a word its ending), the GOVERNED (the word that receives it) and the GOVERNING itself — that is, the iʿrab. The book's three chapters are these three things in order; this note is the first bab.",
         "What is a KALIMA, and why three kinds? An utterance set down for a single meaning. A verb points by its FORM, by coinage, to one of the three tenses; a noun points to a meaning self-standing in the understanding and joined to no tense; a particle points to a meaning that is not self-standing but an instrument for understanding another. Every verb governs; some nouns govern (the ism fāʿil) and some do not (أَنَا، أَنْتَ، الَّذِي); some particles govern (the jarr letter) and some do not (هَلْ، قَدْ).",
         "What are the MARKS of each kind? Of the verb: that قَدْ, the sīn, سَوْفَ, إِنْ, لَمْ, لَمَّا, the lām of command and the lā of prohibition enter on it. Of the noun: that the tanwīn, the jarr letter and the lām of definition enter on it, and that it stands as mubtada, as doer and as annexed head. Birgivi lists them as the KHAWĀṢṢ — what belongs to one kind and to no other — and the DabtEngine classes every row by exactly these marks.",
         "What is the ʿĀMIL? مَا أَوْجَبَ بِوَاسِطَتِهِ كَوْنَ آخِرِ الْكَلِمَةِ عَلَى وَجْهٍ مَخْصُوصٍ مِنَ الْإِعْرَابِ — what makes, through a MEANS, the end of the word take a specific manner of iʿrab. The means is the demand of iʿrab: in nouns, the arrival of the different meanings (doer-ness, object-ness, annexation) on one and the same word, which are hidden and call for visible signs; so ضَرَبَ makes the end of زَيْد a ḍamma and of غُلَام a fatḥa, and غُلَام makes the end of عَمْرو a kasra.",
         "How is the governor DIVIDED? Of the WORDING (the tongue has a share in it) or of the SENSE. The one of the wording is HEARD (its governing rests on transmission) or BY RULE. The heard one governs in the NOUN or in the MUḌĀRIʿ. The one in the noun governs ONE noun or TWO nouns — the mubtada and the khabar, which after the governor enters are called its ism and its khabar. The Izhar's whole first bab is this tree walked branch by branch.",
         "What governs ONE noun? Letters that put it in jarr, called the letters of jarr and of annexation — TWENTY: the bāʾ for attachment, مِنْ for the starting point, إِلَى for the end point, عَنْ for distance and passing beyond, عَلَى for being above, the lām for cause and specification, فِي for containment, the kāf for likening, حَتَّى for the limit, رُبَّ for fewness, the wāw and tāʾ of the oath, حَاشَا for exception, مُذْ and مُنْذُ for the starting point in past time (and both may be nouns), خَلَا and عَدَا for exception (and both may be verbs, the commoner reading), لَوْلَا for the non-occurrence of a thing because another exists (when a pronoun attaches to it), كَيْ for cause (before the interrogative مَا), and لَعَلَّ for hope (in the dialect of ʿUqayl). Each entry is «the letter, for its meaning» — a mubtada with a jarr-phrase khabar.",
         "How does a particle stand as a MUBTADA? By being quoted: in مِنْ لِلِابْتِدَاءِ the word مِنْ is mentioned as a word (لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ), built on what it is heard with, in the PLACE of raf'. The same hikāya puts كَأَنَا وَأَنْتَ and كَهَلْ وَقَدْ in the place of jarr under the kāf. The engines keep every closed-class word's own marks and never strip a quoted particle; the chapter is their test.",
         "What does the engine READ here? The DabtEngine rebuilds every ending of the chapter from the governors alone (the relative clauses after مَا, the fronted khabar وَمِنْ خَوَاصِّهِ, the dual khabars ضَرْبَيْنِ / نَوْعَيْنِ / قِسْمَيْنِ, the passive يُسَمَّيَانِ with its two objects, the twenty quoted mubtadas with their لِ-khabars) and the Qawāʿid ledger names the rule each ending keeps; the twenty letters are the HJ family the TaalluqEngine already walks."],
  "tr": ["İ'râb eden herkes neye muhtaçtır? İzhâr'ın ilk cümlesi üç şey der: ÂMİL (kelimeye sonunu veren), MA'MÛL (onu alan kelime) ve AMEL'in kendisi — yani i'râb. Kitabın üç babı bu üç şeyin sırasıdır; bu not birinci babdır.",
         "KELİME nedir, niçin üç kısım? Müfred bir mana için konulmuş lafız. Fiil KALIBIYLA, vaz' olarak üç zamandan birine delâlet eder; isim anlayışta kendi başına duran ve hiçbir zamana yakın olmayan bir manaya; harf kendi başına durmayan, başkasını anlamaya âlet olan bir manaya delâlet eder. Her fiil âmildir; isimlerin bir kısmı âmildir (ism-i fâil) bir kısmı değildir (أَنَا، أَنْتَ، الَّذِي); harflerin bir kısmı âmildir (cer harfi) bir kısmı değildir (هَلْ، قَدْ).",
         "Her kısmın ALÂMETLERİ nelerdir? Fiilin: قَدْ, sin, سَوْفَ, إِنْ, لَمْ, لَمَّا, emir lâmı ve nehiy lâ'sının ona dâhil olması. İsmin: tenvinin, cer harfinin ve tarif lâmının dâhil olması; mübtedâ, fâil ve muzâf olması. Birgivî bunları HÂSSALAR diye sayar — bir kısma mahsus olup başkasında bulunmayan; DabtEngine her satırı tam bu alâmetlerle sınıflar.",
         "ÂMİL nedir? مَا أَوْجَبَ بِوَاسِطَتِهِ كَوْنَ آخِرِ الْكَلِمَةِ عَلَى وَجْهٍ مَخْصُوصٍ مِنَ الْإِعْرَابِ — bir VASITA ile kelimenin sonunun i'râbdan belirli bir vecih üzere olmasını gerektiren. Vasıta i'râbın muktezâsıdır: isimlerde farklı manaların (fâillik, mef'ûllük, izâfet) aynı kelimeye gelmesi; bunlar gizlidir, görünür alâmet ister. Böylece ضَرَبَ, زَيْد'in sonunu damme, غُلَام'ın sonunu fetha kılar; غُلَام da عَمْرو'un sonunu kesre kılar.",
         "Âmil nasıl TAKSİM edilir? LAFZÎ (dilin onda payı vardır) ya da MA'NEVÎ. Lafzî olan SEMÂÎ (i'mâli nakle dayanır) ya da KIYÂSÎ. Semâî olan İSİMDE ya da MUZÂRİDE âmildir. İsimdeki âmil BİR isimde ya da İKİ isimde âmildir — mübtedâ ve haber; âmil dâhil olunca onun ismi ve haberi diye adlanırlar. İzhâr'ın birinci babı bu ağacın dal dal yürünmesidir.",
         "BİR ismi ne cer eder? Onu cer eden harfler — cer harfleri ve izâfet harfleri — YİRMİ: bâ ilsâk için, مِنْ ibtidâ için, إِلَى intihâ için, عَنْ uzaklık ve mücâvezet için, عَلَى isti'lâ için, lâm ta'lîl ve tahsîs için, فِي zarfiyet için, kâf teşbih için, حَتَّى gâye için, رُبَّ taklîl için, kasem vâvı ve tâsı, حَاشَا istisnâ için, مُذْ ve مُنْذُ geçmiş zamanda ibtidâ için (ikisi isim de olur), خَلَا ve عَدَا istisnâ için (ikisi fiil de olur, çoğu böyledir), لَوْلَا bir şeyin başkasının varlığı yüzünden olmaması için (zamir bitişince), كَيْ ta'lîl için (istifham mâ'sından önce), لَعَلَّ terecci için (Ukayl lügatinde). Her madde «harf, manası için»dir — mübtedâ ile câr-mecrûr haber.",
         "Bir harf nasıl MÜBTEDÂ olur? Hikâye ile: مِنْ لِلِابْتِدَاءِ'de مِنْ kelime olarak anılır (لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ), işitildiği hareke üzere mebnî, ref' MAHALLİNDE. Aynı hikâye كَأَنَا وَأَنْتَ ve كَهَلْ وَقَدْ'ı kâf altında cer mahalline koyar. Motorlar her kapalı sınıf kelimenin harekesini korur, hikâye edilen harfi asla soymaz; bab onların imtihanıdır.",
         "Motor burada neyi OKUR? DabtEngine babın her sonunu yalnız âmillerden yeniden kurar (مَا'dan sonraki sılalar, mukaddem haber وَمِنْ خَوَاصِّهِ, tesniye haberler ضَرْبَيْنِ / نَوْعَيْنِ / قِسْمَيْنِ, iki mef'ûllü meçhul يُسَمَّيَانِ, لِ-haberli yirmi hikâye mübtedâsı); Kavâid defteri her sonun koruduğu kuralı adlandırır; yirmi harf TaalluqEngine'in zaten yürüdüğü cer ailesidir."]},
 "plain": {
  "en": "A parser needs three things: the governor, the governed word, and the governing itself (the iʿrab). The governor makes a word's end take a specific case; it is of the wording or of the sense, heard or by rule, in a noun or in a verb. Twenty letters govern one noun in jarr.",
  "tr": "İ'râb eden üç şeye muhtaçtır: âmil, ma'mûl ve amelin kendisi (i'râb). Âmil kelimenin sonunu belirli bir hale getirir; lafzî ya da ma'nevî, semâî ya da kıyâsî, isimde ya da fiilde olur. Yirmi harf bir ismi cer eder."},
 "explanation": {
  "en": "فَهٰذِهِ رِسَالَةٌ فِيمَا يَحْتَاجُ إِلَيْهِ كُلُّ مُعْرِبٍ أَشَدَّ الِاحْتِيَاجِ، وَهُوَ ثَلَاثَةُ أَشْيَاءَ: الْعَامِلُ وَالْمَعْمُولُ وَالْعَمَلُ. Birgivi's Izhar al-Asrar is the Ottoman madrasah's second nahw book, read after his own Awamil and before the Kafiya, and it opens by naming its whole plan: three chapters for the three things a parser needs. The first bab is the governor. Before defining it the book defines the word and divides it into verb, noun and particle — the Kafiya's division, but stated through the MARKS (khawāṣṣ) each kind admits, which is what a parser actually sees on the page — and says of each kind whether it governs. Then the governor itself: what makes, through its means, the end of the word be in a specific manner of iʿrab. The means is the arrival of the hidden meanings (doer, object, annexed) on a word; the iʿrab is the visible sign they demand. The governor is then divided — wording / sense, heard / by rule, in the noun / in the muḍāriʿ, in one noun / in two — and the first leaf of the tree is the twenty jarr letters, each with the meaning it adds, listed as twenty tiny nominal sentences in which the letter itself is the quoted mubtada. The chapter closes with the three letters whose governing is conditioned: لَوْلَا only with a pronoun, كَيْ only before the interrogative مَا, لَعَلَّ only in the dialect of ʿUqayl.",
  "tr": "فَهٰذِهِ رِسَالَةٌ فِيمَا يَحْتَاجُ إِلَيْهِ كُلُّ مُعْرِبٍ أَشَدَّ الِاحْتِيَاجِ، وَهُوَ ثَلَاثَةُ أَشْيَاءَ: الْعَامِلُ وَالْمَعْمُولُ وَالْعَمَلُ. Birgivî'nin İzhârü'l-Esrâr'ı Osmanlı medresesinin ikinci nahiv kitabıdır — kendi Avâmil'inden sonra, Kâfiye'den önce okunur — ve bütün planını adlandırarak açılır: i'râb edenin muhtaç olduğu üç şey için üç bab. Birinci bab âmildir. Kitap âmili tarif etmeden önce kelimeyi tarif eder ve fiil, isim ve harfe böler — Kâfiye'nin taksimi, fakat her kısmın kabul ettiği ALÂMETLER (hâssalar) üzerinden; i'râb edenin sayfada gördüğü de budur — ve her kısmın âmil olup olmadığını söyler. Sonra âmilin kendisi: bir vasıta ile kelimenin sonunun i'râbdan belirli bir vecih üzere olmasını gerektiren. Vasıta gizli manaların (fâil, mef'ûl, muzâf) kelimeye gelmesidir; i'râb onların istediği görünür alâmettir. Sonra âmil taksim edilir — lafzî / ma'nevî, semâî / kıyâsî, isimde / muzâride, bir isimde / iki isimde — ve ağacın ilk yaprağı, her biri kattığı manayla sayılan yirmi cer harfidir: harfin kendisinin hikâye edilmiş mübtedâ olduğu yirmi küçük isim cümlesi. Bab, ameli şarta bağlı üç harfle kapanır: لَوْلَا yalnız zamirle, كَيْ yalnız istifham مَا'sından önce, لَعَلَّ yalnız Ukayl lügatinde."},
 "examples": [
  {"ar": "وَهُوَ ثَلَاثَةُ أَشْيَاءَ: الْعَامِلُ وَالْمَعْمُولُ وَالْعَمَلُ أَيِ الْإِعْرَابُ", "en": "The three things a parser needs — the plan of the book.", "tr": "İ'râb edenin muhtaç olduğu üç şey — kitabın planı.", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَمِنْ خَوَاصِّهِ دُخُولُ قَدْ وَالسِّينِ وَسَوْفَ وَإِنْ وَلَمْ وَلَمَّا وَلَامِ الْأَمْرِ وَلَاءِ النَّهْيِ", "en": "The verb's marks — quoted particles annexed to «entering».", "tr": "Fiilin hâssaları — dühûl'e muzâf hikâye edilmiş harfler.", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "ثُمَّ الْعَامِلُ هُوَ مَا أَوْجَبَ بِوَاسِطَتِهِ كَوْنَ آخِرِ الْكَلِمَةِ عَلَى وَجْهٍ مَخْصُوصٍ مِنَ الْإِعْرَابِ", "en": "The definition of the governor.", "tr": "Âmilin tarifi.", "sourceStory": "izhar-al-asrar", "sentence": "s12"},
  {"ar": "فَاللَّفْظِيُّ مَا يَكُونُ لِلِّسَانِ فِيهِ حَظٌّ، وَهُوَ عَلَى ضَرْبَيْنِ: سَمَاعِيٌّ وَقِيَاسِيٌّ", "en": "The division — kāna with its delayed ism, the dual khabar.", "tr": "Taksim — muahhar ismiyle kâne, tesniye haber.", "sourceStory": "izhar-al-asrar", "sentence": "s14"},
  {"ar": "الْبَاءُ لِلْإِلْصَاقِ، وَمِنْ لِلِابْتِدَاءِ، وَإِلَى لِلِانْتِهَاءِ", "en": "The first of the twenty — the letter as a quoted mubtada, its meaning as the khabar.", "tr": "Yirminin ilkleri — hikâye edilmiş mübtedâ harf, manası haber.", "sourceStory": "izhar-al-asrar", "sentence": "s18"},
  {"ar": "وَلَعَلَّ لِلتَّرَجِّي فِي لُغَةِ عُقَيْلٍ", "en": "The twentieth letter — a governor only in one tribe's dialect.", "tr": "Yirminci harf — yalnız bir kabilenin lehçesinde âmil.", "sourceStory": "izhar-al-asrar", "sentence": "s21"}],
 "commonMistakes": [
  {"wrong": "«مِنْ لِلِابْتِدَاءِ'de مِنْ cer harfidir, sonrasını cer eder»",
   "right": "«مِنْ burada hikâye edilmiş bir kelimedir: ref' mahallinde mübtedâ; لِلِابْتِدَاءِ onun haberidir»",
   "why": {"en": "A word mentioned AS a word is quoted (لَفْظٌ مَحْكِيٌّ): it keeps its own marks and takes the seat the sentence gives it. The twenty entries are nominal sentences about the letters, not phrases governed by them.", "tr": "Kelime olarak anılan kelime hikâye edilir: kendi harekesini korur, cümlenin verdiği yere oturur. Yirmi madde harfler hakkında isim cümleleridir, onların cer ettiği terkipler değil."}},
  {"wrong": "«Her isim âmildir, her harf âmildir»",
   "right": "«Her FİİL âmildir; isimlerin ve harflerin bir kısmı âmildir, bir kısmı değildir»",
   "why": {"en": "The book says it of each kind: all verbs govern; the ism fāʿil governs but أَنَا، أَنْتَ، الَّذِي do not; the jarr letter governs but هَلْ، قَدْ do not.", "tr": "Kitap her kısım için söyler: bütün fiiller âmildir; ism-i fâil âmildir ama أَنَا، أَنْتَ، الَّذِي değildir; cer harfi âmildir ama هَلْ، قَدْ değildir."}},
  {"wrong": "«لَوْلَا، كَيْ ve لَعَلَّ her yerde cer harfidir»",
   "right": "«لَوْلَا yalnız zamirle, كَيْ yalnız istifham مَا'sından önce, لَعَلَّ yalnız Ukayl lügatinde cer eder»",
   "why": {"en": "Birgivi counts them among the twenty with a condition on each; outside it لَوْلَا is the particle of imtināʿ before a sentence, كَيْ a nāṣib of the verb, لَعَلَّ a sister of إِنَّ.", "tr": "Birgivî üçünü de şartıyla yirmiye katar; şart dışında لَوْلَا cümle önünde imtinâ harfi, كَيْ fiili nasb eden, لَعَلَّ ise إِنَّ'nin kardeşidir."}},
  {"wrong": "«خَلَا ve عَدَا her zaman cer harfidir»",
   "right": "«خَلَا ve عَدَا daha çok FİİLDİR ve sonrasını nasb eder; cer ettikleri azdır»",
   "why": {"en": "The matn says وَيَكُونَانِ فِعْلَيْنِ وَهُوَ الْأَكْثَرُ — the verb reading, with its object in nasb, is the commoner one.", "tr": "Matn der: وَيَكُونَانِ فِعْلَيْنِ وَهُوَ الْأَكْثَرُ — mef'ûlü mansûb fiil okuyuşu daha çoktur."}}],
 "relatedNotes": ["huruf-jarr", "huruf-jarr-nawadir", "al-kalima-wal-kalam", "mubtada-khabar", "zarf-mustaqarr-wa-laghw", "hadhf-wa-taqdir"]}

ADD_EN = (" Chapter 1 (print pp. 84-89): the hamd (s1), the treatise and the three things every parser needs (s2-s3), the first bab (s4), the kalima and "
          "its three kinds with their marks — the verb (s5-s7), the noun (s8-s10), the particle (s11) — the amil's definition (s12), its division into "
          "lafzi/ma'nawi (s13), sama'i/qiyasi (s14), in-the-noun/in-the-mudari (s15), one-noun/two-nouns (s16), the twenty jarr letters announced (s17) "
          "and listed with their meanings (s18-s21). The print's الصلوة and ثلثة are written الصَّلَاة and ثَلَاثَة; the vowelling is the received reading.")
ADD_TR = (" Birinci bab (baskı s. 84-89): hamd (s1), risâle ve i'râb edenin muhtaç olduğu üç şey (s2-s3), birinci bab (s4), kelime ve hâssalarıyla üç kısmı "
          "— fiil (s5-s7), isim (s8-s10), harf (s11) — âmilin tarifi (s12), lafzî/ma'nevî (s13), semâî/kıyâsî (s14), isimde/muzâride (s15), bir isimde/iki "
          "isimde (s16) taksimi, yirmi cer harfinin ilânı (s17) ve manalarıyla sayılması (s18-s21). Baskının الصلوة ve ثلثة imlâsı الصَّلَاة ve ثَلَاثَة yazıldı; hareke kabul görmüş okuyuştur.")
write_out(1, S, TITLE, ADD_EN, ADD_TR, "pp. 84-89", GLOSS_ADD, notes=(NOTE,),
          related=(("huruf-jarr", [K]), ("huruf-jarr-nawadir", [K]), ("al-kalima-wal-kalam", [K]), ("mubtada-khabar", [K])))
report(1, S, GLOSS_ADD, (NOTE,))
