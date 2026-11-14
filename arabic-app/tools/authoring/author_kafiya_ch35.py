# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 35: QUESTIONS ON INNA — coordination in rafʿ on the place of إِنَّ's ism (in word and in standing), its condition that
the khabar come first (in word or in reckoning; the two-governor argument; the Kufans; al-Mubarrad and al-Kisāʾī on a mabnī ism);
لَكِنَّ likewise; the lām of inception on the khabar, on the ism after a separation, and on what stands between (never with أَنَّ, weak
with لَكِنَّ); إِنْ lightened — its lām against the negating إِنْ, its lost government, its entry on the verbs of mubtada and khabar (2:143,
26:186; the Kufans' verse); أَنْ lightened — the pronoun of the matter (10:10), the shādhdh أَنْكَ, and the four signs it needs before a
conjugating verb (73:20; the verse of the man's knowledge; 72:28; 20:89).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~339-340 of the transcription.

  COMMENTARY (the notebook): s1-s10 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch35.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "masail-inna-wal-mukhaffafa-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "مَسَائِلُ إِنَّ: الْعَطْفُ عَلَى الْمَحَلِّ وَلَامُ الِابْتِدَاءِ وَالْمُخَفَّفَةُ", "en": "Questions on inna — coordination on the ism's place, the lām of inception, and the lightened inna and anna", "tr": "İnne meseleleri — ismin mahalline atıf, ibtidâ lâmı ve muhaffefe inne ile enne"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "part"), seg(inner, lex, pos)]))
def jw(full): return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full

IN = "inna-wa-akhawatuha"
AT = "atf-nasaq"
def INN(full="إِنَّ", lex="inna", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", en="«indeed».", tr="«muhakkak».", punct=None, segs=None, tags=()):
    return cited(full, lex, "part", [K, IN] + list(tags), ar, en, tr, punct=punct, segments=segs)
def ISM(full, lex, en, tr, pos="propn", punct=None, segs=None, tags=(), ar="اسْمُ الْحَرْفِ مَنْصُوبٌ."): return cited(full, lex, pos, [IN] + list(tags), ar, en, tr, punct=punct, segments=segs)
def KHB(full, lex, en, tr, pos="noun", punct=None, ar="خَبَرُ الْحَرْفِ مَرْفُوعٌ.", tags=(), segs=None): return cited(full, lex, pos, [IN] + list(tags), ar, en, tr, punct=punct, segments=segs)
def AMR_ATF(punct=None, ar="الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مَعْطُوفٌ عَلَى مَحَلِّ اسْمِ إِنَّ مَرْفُوعٌ."): return cited_wa("وَعَمْرٌو", "amr-name", "propn", [K, AT, IN], ar, "«and ʿAmr».", "«ve Amr».", "عَمْرٌو", punct=punct)
def AYQ(): return W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».")

S.append({"id": "s1", "translation": {
 "en": "And coordination in rafʿ on the place of the ism of إِنَّ is permitted — in word and in standing — because it does not change the sentence's meaning: in word, as إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو; in standing — and that is أَنَّ after عَلِمَ — as عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ وَعَمْرٌو; and it is not permitted on the place of the ism of أَنَّ." + C_EN,
 "tr": "إِنَّ'nin isminin mahalline ref' ile atıf câizdir — lafzen ve hükmen — çünkü cümlenin mânâsını değiştirmez: lafzen, إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو gibi; hükmen — ki o عَلِمَ'den sonraki أَنَّ'dir — عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ وَعَمْرٌو gibi; أَنَّ'nin isminin mahalline câiz değildir." + C_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is permitted».", "«ve câizdir».", "يَجُوزُ"),
  W("الْعَطْفُ", "atf", "noun", ["fail", AT], "فَاعِلٌ مَرْفُوعٌ.", "«coordination».", "«atıf»."),
  bi_("بِالرَّفْعِ", "raf", "noun", [], "الرَّفْعِ مَجْرُورٌ.", "«in rafʿ».", "«ref' ile».", "الرَّفْعِ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness", "al-murab-wal-mabni-wal-irab"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahalline»."),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the ism of».", "«isminin»."),
  INN(ar="مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", en="«inna».", tr="«inne».", tags=["idafa-definiteness"]),
  W("لَفْظًا", "lafz", "noun", ["hal"], "حَالٌ مَنْصُوبٌ: كَائِنَةً لَفْظًا.", "«in word».", "«lafzen»."),
  atf_wa("وَحُكْمًا", "hukm", "noun", ["hal"], "حُكْمًا مَعْطُوفٌ مَنْصُوبٌ.", "«and in standing».", "«ve hükmen».", "حُكْمًا", punct="،"),
  W("لِأَنَّهَا", "lianna", "part", [IN, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because it».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mez»."),
  W("تُغَيِّرُ", "ghayyara", "verb", [IN, "fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«does change».", "«değiştirmez»."),
  W("مَعْنَى", "mana", "noun", ["maful-bihi", "idafa-definiteness", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the meaning of».", "«mânâsını»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«cümlenin».", punct=":"),
  W("فَلَفْظًا", "lafz", "noun", ["hal", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْصِيلِ، وَلَفْظًا حَالٌ.", "«in word».", "«lafzen».", segments=[seg("فَ", "fa", "conj"), seg("لَفْظًا", "lafz", "noun")]),
  nahwu(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."), KHB("قَائِمٌ", "qaim", "«is standing».", "«ayaktadır»."), AMR_ATF(punct="؛"),
  atf_wa("وَحُكْمًا", "hukm", "noun", ["hal"], "حُكْمًا حَالٌ مَعْطُوفٌ.", "«in standing».", "«hükmen».", "حُكْمًا"),
  W("—", "dash", "punct", [], "", "", "") if False else W("وَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and that is».", "«ki o».", segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")]),
  cited("أَنَّ", "anna", "part", ["mubtada-khabar", K, IN], "خَبَرٌ — الْحَرْفُ مَحْكِيٌّ.", "«anna».", "«enne»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonraki»."),
  cited("عَلِمَ", "alima", "verb", ["idafa-definiteness", "zanna-wa-akhawatuha"], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«ʿalima».", "«alime».", punct="—"),
  nahwu(),
  cited("عَلِمْتُ", "alima", "verb", ["fail", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I knew».", "«bildim».", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
  cited("أَنَّ", "anna", "part", [K, IN, "inna-am-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — فِي حُكْمِ إِنَّ بَعْدَ عَلِمَ.", "«that».", "«-dığını»."),
  ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."), KHB("قَائِمٌ", "qaim", "«is standing».", "«ayakta olduğunu»."), AMR_ATF(punct="؛", ar="الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مَعْطُوفٌ عَلَى مَحَلِّ اسْمِ أَنَّ الَّتِي فِي حُكْمِ إِنَّ."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... değildir».", "لَا"),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: الْعَطْفُ.", "«is it permitted».", "«câiz»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahalline»."),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the ism of».", "«isminin»."),
  cited("أَنَّ", "anna", "part", ["idafa-definiteness", K, IN], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«anna».", "«enne'nin».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And its condition is that the khabar come first, in word or in reckoning: in word, as إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو; in reckoning, as إِنَّ زَيْدًا وَعَمْرٌو قَائِمٌ, that is, إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو قَائِمٌ — for were the khabar not first, two governors would meet on one iʿrāb, as in إِنَّ زَيْدًا وَعَمْرٌو ذَاهِبَانِ, and that is void." + C_EN,
 "tr": "Şartı haberin lafzen ya da takdiren önce geçmesidir: lafzen, إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو gibi; takdiren, إِنَّ زَيْدًا وَعَمْرٌو قَائِمٌ gibi, yani إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو قَائِمٌ — zira haber geçmemiş olsa bir i'rabda iki âmil toplanır, إِنَّ زَيْدًا وَعَمْرٌو ذَاهِبَانِ'deki gibi, ve bu bâtıldır." + C_TR},
 "tokens": [
  atf_wa("وَشَرْطُهُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness"], "شَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its condition».", "«ve şartı».", "شَرْطُ", extra_segs=[seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  W("تَقْدِيمُ", "taqdim", "noun", ["mubtada-khabar", "idafa-definiteness", "taqdim-al-musnad"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«that … come first».", "«... önce geçmesidir»."),
  W("الْخَبَرِ", "khabar", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar».", "«haberin»."),
  W("لَفْظًا", "lafz", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«in word».", "«lafzen»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("تَقْدِيرًا", "taqdir", "noun", [AT, "hal", "hadhf-wa-taqdir"], "مَعْطُوفٌ مَنْصُوبٌ.", "«in reckoning».", "«takdiren».", punct=":"),
  W("فَلَفْظًا", "lafz", "noun", ["hal", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْصِيلِ، وَلَفْظًا حَالٌ.", "«in word».", "«lafzen».", segments=[seg("فَ", "fa", "conj"), seg("لَفْظًا", "lafz", "noun")]),
  nahwu(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."), KHB("قَائِمٌ", "qaim", "«is standing».", "«ayaktadır»."), AMR_ATF(punct="؛"),
  atf_wa("وَتَقْدِيرًا", "taqdir", "noun", ["hal", "hadhf-wa-taqdir"], "تَقْدِيرًا حَالٌ مَعْطُوفٌ.", "«in reckoning».", "«takdiren».", "تَقْدِيرًا"),
  nahwu(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."),
  AMR_ATF(ar="الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مَعْطُوفٌ عَلَى الْمَحَلِّ — وَالْخَبَرُ مُقَدَّمٌ تَقْدِيرًا."),
  KHB("قَائِمٌ", "qaim", "«are standing».", "«ayaktadır».", punct="،"),
  AYQ(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."), KHB("قَائِمٌ", "qaim", "«is standing».", "«ayaktadır»."),
  AMR_ATF(ar="الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مُبْتَدَأٌ مَرْفُوعٌ — التَّقْدِيرُ."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "خَبَرٌ مَرْفُوعٌ — الْمُقَدَّرُ.", "«is standing».", "«ayaktadır».", punct="—"),
  W("لِأَنَّ", "lianna", "part", [IN, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«zira».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الْخَبَرَ", "khabar", "noun", [IN], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the khabar».", "«haber»."),
  W("لَوْ", "law", "part", ["al-majzum-wal-shart-wal-jaza"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«were».", "«-sa»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me-»."),
  W("يَتَقَدَّمْ", "taqaddama", "verb", ["nawasib-wa-jawazim-al-mudari", "fail", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ — فِعْلُ لَوْ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«come first».", "«geçmemiş olsa»."),
  W("لَاجْتَمَعَ", "ijtamaa", "verb", ["fail", "form-viii-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَاجْتَمَعَ فِعْلٌ مَاضٍ.", "«would meet».", "«toplanırdı».", segments=[seg("لَ", "lam-jawab", "part"), seg("اجْتَمَعَ", "ijtamaa", "verb")]),
  W("عَامِلَانِ", "amil", "noun", ["fail", "al-muthanna", "al-amil-wa-aqsamuh"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two governors».", "«iki âmil»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-de»."),
  W("إِعْرَابٍ", "irab", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«iʿrāb».", "«i'rab»."),
  W("وَاحِدٍ", "wahid", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«one».", "«bir».", punct="،"),
  ka_("كَمَا", "ma-mawsula", "pron", ["ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«as».", "«... gibi».", "مَا"),
  W("فِي", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — صِلَةٌ.", "«in».", "«-deki»."),
  INN(ar="الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ."), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."),
  AMR_ATF(ar="الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مَعْطُوفٌ قَبْلَ الْخَبَرِ — الْمَمْنُوعُ."),
  cited("ذَاهِبَانِ", "dhahib", "noun", [IN, "al-muthanna", "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — يَطْلُبُهُ عَامِلَانِ: إِنَّ وَالِابْتِدَاءُ.", "«are going».", "«gidiyorlar».", punct="،"),
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and that».", "«ve bu».", "هُوَ"),
  W("بَاطِلٌ", "batil", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«is void».", "«bâtıldır».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And for the Kufans the khabar's coming first is not a condition; and al-Mubarrad and al-Kisāʾī permitted the coordination before the khabar when the ism of إِنَّ is mabnī — as إِنَّكَ وَزَيْدٌ ذَاهِبَانِ — which for the majority is not permitted." + C_EN,
 "tr": "Kûfelilere göre haberin önce geçmesi şart değildir; Müberred ile Kisâî, إِنَّ'nin ismi mebnî olduğunda haberden önce atfı câiz gördüler — إِنَّكَ وَزَيْدٌ ذَاهِبَانِ gibi — ki bu cumhûra göre câiz değildir." + C_TR},
 "tokens": [
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرُ لَيْسَ مُقَدَّمٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْكُوفِيِّينَ", "kufi", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Kufans».", "«Kûfelilere»."),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«is not».", "«değildir»."),
  W("تَقْدِيمُ", "taqdim", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ لَيْسَ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the coming first of».", "«önce geçmesi»."),
  W("الْخَبَرِ", "khabar", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar».", "«haberin»."),
  bi_("بِشَرْطٍ", "shart", "noun", ["kana-wa-akhawatuha"], "شَرْطٍ مَجْرُورٌ لَفْظًا — خَبَرُ لَيْسَ، وَالْبَاءُ زَائِدَةٌ.", "«a condition».", "«şart».", "شَرْطٍ", punct="؛"),
  atf_wa("وَجَوَّزَ", "jawwaza", "verb", ["fail", "form-ii-verbs"], "جَوَّزَ فِعْلٌ مَاضٍ.", "«and permitted».", "«ve câiz gördüler».", "جَوَّزَ"),
  W("الْمُبَرِّدُ", "mubarrad", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Mubarrad».", "«Müberred»."),
  atf_wa("وَالْكِسَائِيُّ", "kisai", "propn", [AT], "الْكِسَائِيُّ مَعْطُوفٌ مَرْفُوعٌ.", "«and al-Kisāʾī».", "«ile Kisâî».", "الْكِسَائِيُّ"),
  W("الْعَطْفَ", "atf", "noun", ["maful-bihi", AT], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the coordination».", "«atfı»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«-den önce»."),
  W("الْخَبَرِ", "khabar", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar».", "«haberden»."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("كَانَ", "kana", "verb", ["idha-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«olduğunda»."),
  W("اسْمُ", "ism", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", IN], "اسْمُ كَانَ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the ism of».", "«ismi»."),
  INN(ar="مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", en="«inna».", tr="«inne'nin».", tags=["idafa-definiteness"]),
  W("مَبْنِيًّا", "mabni", "noun", ["kana-wa-akhawatuha", "al-murab-wal-mabni-wal-irab"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«mabnī».", "«mebnî».", punct="،"),
  nahwu(),
  INN(full="إِنَّكَ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — مَبْنِيٌّ.", en="«you».", tr="«sen».", segs=[seg("إِنَّ", "inna", "part"), pr2ms()]),
  cited_wa("وَزَيْدٌ", "zayd", "propn", [K, AT, IN], "الْوَاوُ عَاطِفَةٌ، وَزَيْدٌ مَعْطُوفٌ عَلَى مَحَلِّ الْكَافِ قَبْلَ الْخَبَرِ.", "«and Zayd».", "«ve Zeyd».", "زَيْدٌ"),
  cited("ذَاهِبَانِ", "dhahib", "noun", [IN, "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«are going».", "«gidiyorsunuz».", punct="—"),
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«which».", "«ki bu».", "هُوَ"),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْجُمْهُورِ", "jumhur", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the majority».", "«cumhûra»."),
  W("غَيْرُ", "ghayr", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«not».", "«... değildir»."),
  W("جَائِزٍ", "jaiz", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«permitted».", "«câiz».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And لَكِنَّ, in the coordination on the place of its ism, is like إِنَّ — as لَمْ يَخْرُجْ زَيْدٌ لَكِنَّ عَمْرًا خَارِجٌ وَبَكْرٌ." + C_EN,
 "tr": "لَكِنَّ, isminin mahalline atıfta إِنَّ gibidir — لَمْ يَخْرُجْ زَيْدٌ لَكِنَّ عَمْرًا خَارِجٌ وَبَكْرٌ gibi." + C_TR},
 "tokens": [
  cited_wa("وَلَكِنَّ", "lakinna", "part", ["mubtada-khabar", K, IN], "لَكِنَّ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and lākinna».", "«ve lâkinne».", "لَكِنَّ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْعَطْفِ", "atf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«the coordination».", "«atıfta»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahalline»."),
  W("اسْمِهَا", "ism", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ism».", "«isminin».", segments=[seg("اسْمِ", "ism", "noun"), pr3fs()]),
  ka_("كَإِنَّ", "inna", "part", ["mubtada-khabar", IN], "إِنَّ فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«is like inna».", "«inne gibidir».", "إِنَّ", punct="،"),
  nahwu(),
  cited("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-medi»."),
  cited("يَخْرُجْ", "kharaja", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ.", "«did go out».", "«çıkmadı»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("لَكِنَّ", "lakinna", "part", [K, IN], "حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ.", "«but».", "«fakat»."),
  ISM("عَمْرًا", "amr-name", "«ʿAmr».", "«Amr»."),
  KHB("خَارِجٌ", "kharij", "«is out».", "«çıktı».", tags=["ism-fail"]),
  cited_wa("وَبَكْرٌ", "bakr", "propn", [K, AT, IN], "الْوَاوُ عَاطِفَةٌ، وَبَكْرٌ مَعْطُوفٌ عَلَى مَحَلِّ اسْمِ لَكِنَّ مَرْفُوعٌ.", "«and Bakr».", "«ve Bekir».", "بَكْرٌ", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And the lām of inception may enter with إِنَّ, not with أَنَّ — on its khabar, as إِنَّ زَيْدًا لَقَائِمٌ; on its ism when something separates them, as إِنَّ فِي الدَّارِ لَزَيْدًا; and on what falls between its ism and its khabar, as إِنَّ زَيْدًا لَطَعَامَكَ آكِلٌ; and its entering with لَكِنَّ is weak." + C_EN,
 "tr": "İbtidâ lâmı إِنَّ ile girebilir, أَنَّ ile giremez — haberine, إِنَّ زَيْدًا لَقَائِمٌ gibi; arası ayrıldığında ismine, إِنَّ فِي الدَّارِ لَزَيْدًا gibi; ismi ile haberi arasına düşen kelimeye, إِنَّ زَيْدًا لَطَعَامَكَ آكِلٌ gibi; لَكِنَّ ile girmesi zayıftır." + C_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and may».", "«ve câizdir».", "يَجُوزُ"),
  W("دُخُولُ", "dukhul", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the entering of».", "«girmesi»."),
  W("لَامِ", "lam-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the lām of».", "«lâmının»."),
  W("الِابْتِدَاءِ", "ibtida-start", "noun", ["idafa-definiteness", K], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«inception».", "«ibtidâ»."),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  INN(ar="مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", en="«inna».", tr="«inne».", tags=["idafa-definiteness"]),
  W("دُونَ", "dun", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«not with».", "«... ile değil»."),
  cited("أَنَّ", "anna", "part", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«anna».", "«enne».", punct="—"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("خَبَرِهَا", "khabar", "noun", ["huruf-jarr", "idafa-definiteness", IN], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its khabar».", "«haberine».", punct="،", segments=[seg("خَبَرِ", "khabar", "noun"), pr3fs()]),
  nahwu(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."),
  KHB("لَقَائِمٌ", "qaim", "«is surely standing».", "«elbette ayaktadır».", ar="اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَقَائِمٌ خَبَرُ إِنَّ مَرْفُوعٌ.", tags=[K], segs=[seg("لَ", "lam-ibtida", "part"), seg("قَائِمٌ", "qaim", "noun")], punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ.", "«on».", "«... -ine».", "عَلَى"),
  W("اسْمِهَا", "ism", "noun", ["huruf-jarr", "idafa-definiteness", IN], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ism».", "«ismine».", segments=[seg("اسْمِ", "ism", "noun"), pr3fs()]),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("فُصِلَ", "fasala", "verb", ["idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«something separates».", "«arası ayrıldığında»."),
  W("بَيْنَهُمَا", "bayna", "adv", ["naib-al-fail", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ — نَائِبُ فَاعِلٍ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«them».", "«ikisinin».", punct="،", segments=[seg("بَيْنَ", "bayna", "adv"), pr3d()]),
  nahwu(),
  INN(),
  cited("فِي", "fi", "prep", ["huruf-jarr", IN, "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ مُقَدَّمٌ، فَاصِلٌ.", "«in».", "«-de»."),
  cited("الدَّارِ", "dar", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the house».", "«evde»."),
  ISM("لَزَيْدًا", "zayd", "«is surely Zayd».", "«elbette Zeyd».", ar="اللَّامُ لَامُ الِابْتِدَاءِ، وَزَيْدًا اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ.", segs=[seg("لَ", "lam-ibtida", "part"), seg("زَيْدًا", "zayd", "propn")], tags=[K], punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ.", "«and on».", "«ve ... -e».", "عَلَى"),
  W("مَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what».", "«... kelimeye»."),
  W("بَيْنَ", "bayna", "adv", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — صِلَةٌ.", "«falls between».", "«arasına düşen»."),
  W("اسْمِهَا", "ism", "noun", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ism».", "«ismi».", segments=[seg("اسْمِ", "ism", "noun"), pr3fs()]),
  atf_wa("وَخَبَرِهَا", "khabar", "noun", [AT, "idafa-definiteness", IN], "خَبَرِ مَعْطُوفٌ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its khabar».", "«ile haberi».", "خَبَرِ", extra_segs=[seg("خَبَرِ", "khabar", "noun"), pr3fs()], punct="،"),
  nahwu(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."),
  cited("لَطَعَامَكَ", "taam", "noun", [K, "maful-bihi", "idafa-definiteness", "taqdim-al-musnad"], "اللَّامُ لَامُ الِابْتِدَاءِ، وَطَعَامَ مَفْعُولٌ بِهِ لِآكِلٌ مُقَدَّمٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your food».", "«senin yemeğini».", segments=[seg("لَ", "lam-ibtida", "part"), seg("طَعَامَ", "taam", "noun"), pr2ms()]),
  KHB("آكِلٌ", "akil", "«is eating».", "«yiyendir».", tags=["ism-fail", "shurut-amal-ism-al-fail"], punct="؛"),
  atf_wa("وَدُخُولُهَا", "dukhul", "noun", ["mubtada-khabar", "idafa-definiteness"], "دُخُولُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its entering».", "«ve girmesi».", "دُخُولُ", extra_segs=[seg("دُخُولُ", "dukhul", "noun"), pr3fs()]),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile»."),
  cited("لَكِنَّ", "lakinna", "part", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«lākinna».", "«lâkinne»."),
  W("ضَعِيفٌ", "daif", "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ.", "«is weak».", "«zayıftır».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And إِنَّ is lightened and remains إِنْ, and the lām must stand in its khabar so that it is not confused with the negating إِنْ; then it may be stripped of government, and may enter on a verb of the mubtada-and-khabar verbs — as وَإِنْ كَانَتْ لَكَبِيرَةً, and وَإِنْ نَظُنُّكَ لَمِنَ الْكَاذِبِينَ." + C_EN,
 "tr": "إِنَّ hafifletilir, إِنْ kalır; nâfiye إِنْ ile karışmaması için haberinde lâm bulunması lâzım gelir; o zaman amelden bozulması ve mübtedâ-haber fiillerinden bir fiil üzerine girmesi câizdir — وَإِنْ كَانَتْ لَكَبِيرَةً ve وَإِنْ نَظُنُّكَ لَمِنَ الْكَاذِبِينَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتُخَفَّفُ", "khaffafa", "verb", ["naib-al-fail", "form-ii-verbs"], "تُخَفَّفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is lightened».", "«ve hafifletilir».", "تُخَفَّفُ"),
  INN(ar="نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", en="«inna».", tr="«inne».", tags=["naib-al-fail"]),
  W("فَتَبْقَى", "baqiya", "verb", ["fail", "ism-maqsur-manqus", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَبْقَى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and remains».", "«ve ... kalır».", segments=[seg("فَ", "fa", "conj"), seg("تَبْقَى", "baqiya", "verb")]),
  cited("إِنْ", "in-harf", "part", [K, IN, "inna-wa-akhawatuha"], "إِنْ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ — فِي مَحَلِّ نَصْبٍ خَبَرُ تَبْقَى.", "«in».", "«in».", punct="،"),
  atf_wa("وَيَلْزَمُ", "lazima", "verb", ["fail"], "يَلْزَمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and must stand».", "«ve ... lâzım gelir».", "يَلْزَمُ"),
  W("خَبَرَهَا", "khabar", "noun", ["maful-bihi", "idafa-definiteness", IN], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«in its khabar».", "«haberinde».", segments=[seg("خَبَرَ", "khabar", "noun"), pr3fs()]),
  W("اللَّامُ", "lam-letter", "noun", ["fail"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the lām».", "«lâm»."),
  li_("لِلْفَرْقِ", "farq", "noun", ["lam-taleel"], "الْفَرْقِ مَجْرُورٌ — لَامُ التَّعْلِيلِ.", "«to tell it».", "«ayırmak için».", "الْفَرْقِ", segs=[seg("لِ", "lam-taleel", "part"), seg("لْفَرْقِ", "farq", "noun")]),
  W("بَيْنَهَا", "bayna", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«from».", "«onu».", segments=[seg("بَيْنَ", "bayna", "adv"), pr3fs()]),
  atf_wa("وَبَيْنَ", "bayna", "adv", [AT, "maful-fih", "idafa-definiteness"], "بَيْنَ مَعْطُوفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«—».", "«—».", "بَيْنَ"),
  cited("إِنِ", "in-harf", "part", ["idafa-definiteness", "la-nafiya"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«the in».", "«in»."),
  W("النَّافِيَةِ", "nafi", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«negating».", "«nâfiyeden».", punct="؛"),
  atf_wa("وَحِينَئِذٍ", "hina", "noun", ["maful-fih", "idafa-definiteness"], "حِينَ ظَرْفٌ مَنْصُوبٌ، وَإِذٍ مُضَافٌ إِلَيْهِ، نُوِّنَ عِوَضًا عَنِ الْجُمْلَةِ.", "«then».", "«o zaman».", "حِينَئِذٍ", extra_segs=[seg("حِينَ", "hina", "noun"), seg("ئِذٍ", "idh", "part")]),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it may».", "«câizdir»."),
  W("تَرْكُ", "tark", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«be stripped of».", "«bozulması»."),
  W("عَمَلِهَا", "amal", "noun", ["idafa-definiteness", "al-amil-wa-aqsamuh"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its government».", "«amelden».", punct="،", segments=[seg("عَمَلِ", "amal", "noun"), pr3fs()]),
  atf_wa("وَدُخُولُهَا", "dukhul", "noun", [AT, "idafa-definiteness"], "دُخُولُ مَعْطُوفٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and may enter».", "«ve girmesi».", "دُخُولُ", extra_segs=[seg("دُخُولُ", "dukhul", "noun"), pr3fs()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("فِعْلٍ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«bir fiil»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.", "«of».", "«-den»."),
  W("أَفْعَالِ", "fil", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the verbs of».", "«fiillerinden»."),
  W("الْمُبْتَدَإِ", "mubtada", "noun", ["idafa-definiteness", "kana-wa-akhawatuha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtada».", "«mübtedâ»."),
  atf_wa("وَالْخَبَرِ", "khabar", "noun", [AT, "kana-wa-akhawatuha"], "الْخَبَرِ مَعْطُوفٌ مَجْرُورٌ — كَانَ وَظَنَّ وَأَخَوَاتُهُمَا.", "«and the khabar».", "«haber».", "الْخَبَرِ", punct="،"),
  nahwu(),
  cited("وَإِنْ", "in-harf", "part", [K, IN, "inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُهْمَلَةٌ.", "«and indeed».", "«ve muhakkak».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-harf", "part")]),
  cited("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«it was».", "«o ... idi».", segments=[seg("كَانَ", "kana", "verb"), seg("تْ", "ta-tanith", "part")]),
  cited("لَكَبِيرَةً", "kabira", "noun", ["kana-wa-akhawatuha", K], "اللَّامُ الْفَارِقَةُ، وَكَبِيرَةً خَبَرُ كَانَتْ مَنْصُوبٌ.", "«surely hard».", "«elbette büyük».", punct="،", segments=[seg("لَ", "lam-ibtida", "part"), seg("كَبِيرَةً", "kabira", "noun")]),
  cited_wa("وَإِنْ", "in-harf", "part", [K, IN, "inna-wa-akhawatuha"], "إِنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُهْمَلَةٌ.", "«and indeed».", "«ve muhakkak».", "إِنْ"),
  cited("نَظُنُّكَ", "zanna", "verb", ["zanna-wa-akhawatuha", "fail", "mafulayn", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَالْكَافُ مَفْعُولٌ أَوَّلُ.", "«we think you».", "«biz seni sanıyoruz».", segments=[seg("نَظُنُّ", "zanna", "verb"), pr2ms()]),
  cited("لَمِنَ", "min", "prep", [K, "huruf-jarr", "mafulayn"], "اللَّامُ الْفَارِقَةُ، وَمِنْ حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ مَفْعُولٌ ثَانٍ.", "«surely among».", "«elbette ... -den».", segments=[seg("لَ", "lam-ibtida", "part"), seg("مِنَ", "min", "prep")]),
  cited("الْكَاذِبِينَ", "kadhib-liar", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِالْيَاءِ.", "«the liars».", "«yalancılardan».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And the Kufans differed from the Basrans and made the verb general, their proof the poet's بِاللهِ رَبِّكَ إِنْ قَتَلْتَ لَمُسْلِمًا." + C_EN,
 "tr": "Kûfeliler Basralılara muhalefet edip fiili umumî kıldılar; delilleri şairin بِاللهِ رَبِّكَ إِنْ قَتَلْتَ لَمُسْلِمًا sözüdür." + C_TR},
 "tokens": [
  atf_wa("وَخَالَفَ", "khalafa", "verb", ["fail", "form-iii-verbs"], "خَالَفَ فِعْلٌ مَاضٍ.", "«and differed».", "«ve muhalefet etti».", "خَالَفَ"),
  W("الْكُوفِيُّونَ", "kufi", "noun", ["fail", "jam-mudhakkar-salim"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ.", "«the Kufans».", "«Kûfeliler»."),
  W("الْبَصْرِيِّينَ", "basri", "noun", ["maful-bihi", "jam-mudhakkar-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«from the Basrans».", "«Basralılara»."),
  W("فَجَعَلُوا", "jaala", "verb", ["fail", "mafulayn"], "الْفَاءُ عَاطِفَةٌ، وَجَعَلُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«and made».", "«ve kıldılar».", segments=[seg("فَ", "fa", "conj"), seg("جَعَلُ", "jaala", "verb"), seg("وا", "pron-3mp", "pron")]),
  W("الْفِعْلَ", "fil", "noun", ["mafulayn"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ.", "«the verb».", "«fiili»."),
  W("عَامًّا", "amm", "noun", ["mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«general».", "«umumî».", punct="،"),
  atf_wa("وَدَلِيلُهُمْ", "dalil-proof", "noun", ["mubtada-khabar", "idafa-definiteness"], "دَلِيلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their proof».", "«delilleri».", "دَلِيلُ", extra_segs=[seg("دَلِيلُ", "dalil-proof", "noun"), pr3mp()]),
  W("قَوْلُ", "qawl", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the saying of».", "«... sözüdür»."),
  W("الشَّاعِرِ", "shair", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the poet».", "«şairin».", punct=":"),
  cited("بِاللهِ", "allah", "propn", ["huruf-jarr", "huruf-al-qasam-fil-kafiya"], "الْبَاءُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by God».", "«Allah'a».", segments=[seg("بِ", "ba-qasam", "prep"), seg("اللهِ", "allah", "propn")]),
  cited("رَبِّكَ", "rabb", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord».", "«Rabbine».", segments=[seg("رَبِّ", "rabb", "noun"), pr2ms()]),
  cited("إِنْ", "in-harf", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ دَخَلَتْ عَلَى فِعْلٍ مُتَصَرِّفٍ — حُجَّةُ الْكُوفِيِّينَ.", "«indeed».", "«muhakkak»."),
  cited("قَتَلْتَ", "qatala", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you killed».", "«öldürdün».", segments=[seg("قَتَلْ", "qatala", "verb"), prTa()]),
  cited("لَمُسْلِمًا", "muslim", "noun", [K, "maful-bihi", "ism-fail"], "اللَّامُ الْفَارِقَةُ، وَمُسْلِمًا مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«surely a Muslim».", "«elbette bir müslümanı».", punct=".", segments=[seg("لَ", "lam-ibtida", "part"), seg("مُسْلِمًا", "muslim", "noun")]),
 ]})

S.append({"id": "s8", "translation": {
 "en": "And أَنَّ is lightened and remains أَنْ, and governs a hidden pronoun of the matter — it is its ism, in the place of naṣb, and the sentence after it explains it and is its khabar, in the place of rafʿ — as وَآخِرُ دَعْوَاهُمْ أَنِ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ; and its governing other than the pronoun of the matter is irregular, as أَظُنُّ أَنْكَ قَائِمٌ." + C_EN,
 "tr": "أَنَّ hafifletilir, أَنْ kalır ve gizli bir şan zamirinde amel eder — o ismidir, mahallen mansûb; ardındaki cümle onu tefsir eder ve haberidir, mahallen merfû — وَآخِرُ دَعْوَاهُمْ أَنِ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ gibi; şan zamirinden başkasında amel etmesi şâzdır, أَظُنُّ أَنْكَ قَائِمٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتُخَفَّفُ", "khaffafa", "verb", ["naib-al-fail", "form-ii-verbs"], "تُخَفَّفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is lightened».", "«ve hafifletilir».", "تُخَفَّفُ"),
  cited("أَنَّ", "anna", "part", ["naib-al-fail", K, IN], "نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", "«anna».", "«enne»."),
  W("فَتَبْقَى", "baqiya", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَبْقَى فِعْلٌ مُضَارِعٌ.", "«and remains».", "«ve ... kalır».", segments=[seg("فَ", "fa", "conj"), seg("تَبْقَى", "baqiya", "verb")]),
  cited("أَنْ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "أَنْ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ — خَبَرُ تَبْقَى.", "«an».", "«en».", punct="،"),
  atf_wa("وَتَعْمَلُ", "amila", "verb", ["fail"], "تَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and governs».", "«ve amel eder».", "تَعْمَلُ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-de»."),
  W("ضَمِيرِ", "damir", "noun", ["huruf-jarr", "idafa-definiteness", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«a pronoun of».", "«zamirinde»."),
  W("شَأْنٍ", "shan", "noun", ["idafa-definiteness", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the matter».", "«şan»."),
  W("مُقَدَّرٍ", "muqaddar", "noun", ["naat-sifa", "hadhf-wa-taqdir", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«hidden».", "«gizli».", punct="—"),
  W("هُوَ", "huwa", "pron", ["mubtada-khabar"], "مُبْتَدَأٌ.", "«it».", "«o»."),
  W("اسْمُهَا", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", IN], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its ism».", "«ismidir».", segments=[seg("اسْمُ", "ism", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallen»."),
  W("نَصْبٍ", "nasb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naṣb».", "«mansûb».", punct="،"),
  atf_wa("وَالْجُمْلَةُ", "jumla", "noun", ["mubtada-khabar"], "الْجُمْلَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sentence».", "«ve cümle».", "الْجُمْلَةُ"),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ardındaki».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("تُفَسِّرُهُ", "fassara", "verb", ["mubtada-khabar", "fail", "maful-bihi", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ خَبَرٌ.", "«explains it».", "«onu tefsir eder».", segments=[seg("تُفَسِّرُ", "fassara", "verb"), pr3ms()]),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("خَبَرُهَا", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness", IN], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its khabar».", "«haberidir».", segments=[seg("خَبَرُ", "khabar", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallen»."),
  W("رَفْعٍ", "raf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rafʿ».", "«merfû».", punct="—"),
  nahwu(),
  cited("وَآخِرُ", "akhir", "noun", ["mubtada-khabar", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَآخِرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the last of».", "«ve sonu».", segments=[seg("وَ", "wa", "conj"), seg("آخِرُ", "akhir", "noun")]),
  cited("دَعْوَاهُمْ", "dawa-claim", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their call».", "«dualarının».", segments=[seg("دَعْوَا", "dawa-claim", "noun"), pr3mp()]),
  cited("أَنِ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«is that».", "«şudur ki»."),
  cited("الْحَمْدُ", "hamd", "noun", ["mubtada-khabar", IN], "مُبْتَدَأٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ أَنْ.", "«praise».", "«hamd»."),
  cited("لِلَّهِ", "allah", "propn", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — خَبَرٌ.", "«is to God».", "«Allah'adır».", segments=[seg("لِ", "li", "prep"), seg("لَّهِ", "allah", "propn")]),
  cited("رَبِّ", "rabb", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ مَجْرُورَةٌ، وَهُوَ مُضَافٌ.", "«Lord of».", "«Rabbi»."),
  cited("الْعَالَمِينَ", "alamin", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the worlds».", "«âlemlerin».", punct="؛"),
  atf_wa("وَعَمَلُهَا", "amal", "noun", ["mubtada-khabar", "idafa-definiteness"], "عَمَلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its governing».", "«ve amel etmesi».", "عَمَلُ", extra_segs=[seg("عَمَلُ", "amal", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-de»."),
  W("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«other than».", "«... başkasında»."),
  W("ضَمِيرِ", "damir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the pronoun of».", "«zamirinden»."),
  W("الشَّأْنِ", "shan", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the matter».", "«şan»."),
  W("شَاذٌّ", "shadhdh", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is irregular».", "«şâzdır».", punct="،"),
  nahwu(),
  cited("أَظُنُّ", "zanna", "verb", ["fail", "zanna-wa-akhawatuha", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I think».", "«sanıyorum»."),
  cited("أَنْكَ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ عَمِلَتْ فِي ضَمِيرٍ بَارِزٍ — شَاذٌّ؛ وَالْكَافُ اسْمُهَا.", "«that you».", "«senin».", segments=[seg("أَنْ", "an-mukhaffafa", "part"), pr2ms()]),
  cited("قَائِمٌ", "qaim", "noun", [IN], "خَبَرُ أَنْ مَرْفُوعٌ.", "«are standing».", "«ayakta olduğunu».", punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And أَنْ, with a conjugating verb that is neither a condition nor a prayer, needs one of four: the sīn — as عَلِمَ أَنْ سَيَكُونُ مِنْكُمْ مَرْضَى; or سَوْفَ — as وَاعْلَمْ فَعِلْمُ الْمَرْءِ يَنْفَعُهُ • أَنْ سَوْفَ يَأْتِي كُلُّ مَا قُدِرَا." + C_EN,
 "tr": "أَنْ'e, şart ve dua olmayan mutasarrıf fiille birlikte dört şeyden biri lâzım gelir: sîn — عَلِمَ أَنْ سَيَكُونُ مِنْكُمْ مَرْضَى gibi; ya da سَوْفَ — وَاعْلَمْ فَعِلْمُ الْمَرْءِ يَنْفَعُهُ • أَنْ سَوْفَ يَأْتِي كُلُّ مَا قُدِرَا gibi." + C_TR},
 "tokens": [
  atf_wa("وَيَلْزَمُ", "lazima", "verb", ["fail"], "يَلْزَمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and needs».", "«ve ... lâzım gelir».", "يَلْزَمُ"),
  cited("أَنْ", "an-mukhaffafa", "part", ["maful-bihi", K, IN, "inna-wa-akhawatuha"], "مَفْعُولٌ بِهِ — الْحَرْفُ مَحْكِيٌّ.", "«an».", "«en'e»."),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile birlikte»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«fiille»."),
  W("الْمُتَصَرِّفِ", "mutasarrif", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«conjugating».", "«mutasarrıf»."),
  W("غَيْرِ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ، وَهُوَ مُضَافٌ.", "«that is neither».", "«... olmayan»."),
  W("الشَّرْطِ", "shart", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a condition».", "«şart»."),
  atf_wa("وَالدُّعَاءِ", "dua", "noun", [AT], "الدُّعَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«nor a prayer».", "«ve dua».", "الدُّعَاءِ"),
  W("أَحَدُ", "ahad", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«one of».", "«... -den biri»."),
  W("أَرْبَعَةٍ", "arbaa", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«four».", "«dört şey».", punct=":"),
  W("السِّينُ", "sin-letter", "noun", ["badal"], "بَدَلٌ مِنْ أَحَدُ مَرْفُوعٌ.", "«the sīn».", "«sîn».", punct="،"),
  nahwu(),
  cited("عَلِمَ", "alima", "verb", ["fail", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«He knew».", "«bildi»."),
  cited("أَنْ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ.", "«that».", "«-ceğini»."),
  cited("سَيَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", K], "السِّينُ لِلِاسْتِقْبَالِ — الْفَاصِلُ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«there will be».", "«olacak».", segments=[seg("سَ", "sin-istiqbal", "part"), seg("يَكُونُ", "kana", "verb")]),
  cited("مِنْكُمْ", "min", "prep", ["huruf-jarr", "kana-wa-akhawatuha"], "مِنْ حَرْفُ جَرٍّ، وَكُمْ مَجْرُورٌ — خَبَرُ يَكُونُ مُقَدَّمٌ.", "«among you».", "«sizden».", segments=[seg("مِنْ", "min", "prep"), pr2mp()]),
  cited("مَرْضَى", "marid", "noun", ["kana-wa-akhawatuha", "jam-taksir", "ism-maqsur-manqus"], "اسْمُ يَكُونُ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — جَمْعُ مَرِيضٍ.", "«sick ones».", "«hastalar».", punct="؛"),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("سَوْفَ", "sawfa", "part", [AT, K], "مَعْطُوفٌ عَلَى السِّينُ — الْحَرْفُ مَحْكِيٌّ.", "«sawfa».", "«sevfe».", punct="،"),
  nahwu(),
  cited("وَاعْلَمْ", "alima", "verb", ["fail"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاعْلَمْ فِعْلُ أَمْرٍ.", "«and know».", "«ve bil».", segments=[seg("وَ", "wa", "conj"), seg("اعْلَمْ", "alima", "verb")]),
  cited("فَعِلْمُ", "ilm", "noun", ["mubtada-khabar", "idafa-definiteness"], "الْفَاءُ لِلتَّعْلِيلِ، وَعِلْمُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«for the knowledge of».", "«zira ... bilgisi».", segments=[seg("فَ", "fa", "conj"), seg("عِلْمُ", "ilm", "noun")]),
  cited("الْمَرْءِ", "mar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a man».", "«kişinin»."),
  cited("يَنْفَعُهُ", "nafaa", "verb", ["mubtada-khabar", "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ خَبَرٌ.", "«profits him».", "«ona fayda verir».", punct="•", segments=[seg("يَنْفَعُ", "nafaa", "verb"), pr3ms()]),
  cited("أَنْ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ — بَدَلٌ مِنْ عِلْمُ.", "«that».", "«-ceğini»."),
  cited("سَوْفَ", "sawfa", "part", [K], "حَرْفُ اسْتِقْبَالٍ — الْفَاصِلُ.", "«will».", "«-ecek»."),
  cited("يَأْتِي", "ata", "verb", ["fail", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«come».", "«gelecek»."),
  cited("كُلُّ", "kull", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«all».", "«her»."),
  cited("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that».", "«... şey»."),
  cited("قُدِرَا", "qaddara", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْأَلِفُ لِلْإِطْلَاقِ — صِلَةٌ.", "«was decreed».", "«takdir edilen».", punct="."),
 ]})

S.append({"id": "s10", "translation": {
 "en": "Or قَدْ — as لِيَعْلَمَ أَنْ قَدْ أَبْلَغُوا رِسَالَاتِ رَبِّهِمْ; or a particle of negation — as أَفَلَا يَرَوْنَ أَنْ لَا يَرْجِعُ إِلَيْهِمْ قَوْلًا." + C_EN,
 "tr": "Ya da قَدْ — لِيَعْلَمَ أَنْ قَدْ أَبْلَغُوا رِسَالَاتِ رَبِّهِمْ gibi; ya da bir nefy harfi — أَفَلَا يَرَوْنَ أَنْ لَا يَرْجِعُ إِلَيْهِمْ قَوْلًا gibi." + C_TR},
 "tokens": [
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("قَدْ", "qad", "part", [AT, K], "مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«qad».", "«kad».", punct="،"),
  nahwu(),
  cited("لِيَعْلَمَ", "alima", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "fail"], "اللَّامُ لِلتَّعْلِيلِ، وَيَعْلَمَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«that He may know».", "«bilmesi için».", segments=[seg("لِ", "lam-taleel", "part"), seg("يَعْلَمَ", "alima", "verb")]),
  cited("أَنْ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ.", "«that».", "«-lerini»."),
  cited("قَدْ", "qad", "part", [K], "حَرْفُ تَحْقِيقٍ — الْفَاصِلُ.", "«indeed».", "«muhakkak»."),
  cited("أَبْلَغُوا", "ablagha", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«they have delivered».", "«tebliğ ettiler».", segments=[seg("أَبْلَغُ", "ablagha", "verb"), seg("وا", "pron-3mp", "pron")]),
  cited("رِسَالَاتِ", "risala", "noun", ["maful-bihi", "idafa-definiteness", "jam-muannath-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، وَهُوَ مُضَافٌ.", "«the messages of».", "«risaletlerini»."),
  cited("رَبِّهِمْ", "rabb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their Lord».", "«Rablerinin».", punct="؛", segments=[seg("رَبِّ", "rabb", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("حَرْفُ", "harf", "noun", [AT, "idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«a particle of».", "«harfi»."),
  W("نَفْيٍ", "nafy", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«negation».", "«nefy».", punct="،"),
  nahwu(),
  cited("أَفَلَا", "la-nafiya", "part", ["adawat-al-tasawwur", "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«do they not».", "«... görmüyorlar mı».", segments=[seg("أَ", "hamza-istifham", "part"), seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  cited("يَرَوْنَ", "raa", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«see».", "«görmüyorlar»."),
  cited("أَنْ", "an-mukhaffafa", "part", [K, IN, "inna-wa-akhawatuha"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ.", "«that».", "«-diğini»."),
  cited("لَا", "la-nafiya", "part", [K, "la-nafiya"], "نَافِيَةٌ — الْفَاصِلُ.", "«not».", "«-me-»."),
  cited("يَرْجِعُ", "rajaa", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْعِجْلُ.", "«it returns».", "«dönmediğini»."),
  cited("إِلَيْهِمْ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَهِمْ مَجْرُورٌ.", "«to them».", "«onlara».", segments=[seg("إِلَيْ", "ila", "prep"), seg("هِمْ", "pron-3mp", "pron")]),
  cited("قَوْلًا", "qawl", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a word».", "«bir söz».", punct="."),
 ]})

def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "an-mukhaffafa": need("an-mukhaffafa", "أَنْ (الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ)", "أ ن", "part", "an lightened from anna — governs a hidden pronoun of the matter; its khabar is the following sentence", "enne'den hafifletilmiş en — gizli şan zamirinde amel eder; haberi ardındaki cümledir", 5),
 "in-harf": need("in-harf", "إِنْ (الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ)", "إ ن", "part", "in lightened from inna — stripped of government, marked by the lām in its khabar", "inne'den hafifletilmiş in — amelden bozulmuş, haberindeki lâmla ayırt edilir", 5),
 "sin-istiqbal": need("sin-istiqbal", "سَ (الِاسْتِقْبَال)", "س", "part", "the sīn of the future prefixed to the muḍāriʿ", "muzârie gelen istikbâl sîni", 2),
 "hamza-istifham": need("hamza-istifham", "أَ (الِاسْتِفْهَام)", "أ", "part", "the hamza of interrogation", "istifham hemzesi", 2),
 "hina": need("hina", "حِين", "ح ي ن", "noun", "a time, a while; حِينَئِذٍ «then, at that time»", "an, vakit; حِينَئِذٍ «o zaman»", 2),
 "tark": need("tark", "تَرْك", "ت ر ك", "noun", "leaving, abandoning — the maṣdar of تَرَكَ", "terk, bırakma — tereke'nin masdarı", 2),
 "muqaddar": need("muqaddar", "مُقَدَّر", "ق د ر", "noun", "understood, supplied in the reckoning — the ism mafʿūl of قَدَّرَ", "takdir edilen, mukadder — kaddera'nın ism-i mef'ûlü", 4),
}
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch35 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "مَسَائِلُ إِنَّ فِي الْكَافِيَةِ: الْعَطْفُ عَلَى الْمَحَلِّ وَلَامُ الِابْتِدَاءِ وَالْمُخَفَّفَةُ", "en": "Questions on inna in the Kafiya: coordination on the ism's place and its condition, the lām of inception's three seats, inna lightened to in, anna lightened to an and the four signs it needs", "tr": "Kâfiye'de inne meseleleri: ismin mahalline atıf ve şartı, ibtidâ lâmının üç yeri, in'e hafifleyen inne, en'e hafifleyen enne ve ihtiyaç duyduğu dört işaret"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — يجوز العطف على محل اسم إن بالرفع بعد الخبر؛ ولام الابتداء مع إن؛ وتخفف إن فتلزم اللام؛ وتخفف أن فتعمل في ضمير الشأن", "ضياء صونغور اوغلى — دفتر الكافية: لفظا وحكما؛ اجتماع العاملين؛ الكوفيون والمبرد والكسائي؛ لكن كإن؛ مواضع اللام الثلاثة؛ إن كانت لكبيرة؛ إن نظنك لمن الكاذبين؛ بيت الكوفيين؛ وآخر دعواهم أن الحمد لله؛ أنك قائم شاذ؛ السين وسوف وقد والنفي"],
 "question": {
  "en": ["May a word be joined to inna's ism in rafʿ? Yes — on its PLACE, which is the mubtada's place, because inna does not change the sentence's sense: إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو. The same holds for anna after a verb of knowing, which stands in inna's standing; it never holds for the ordinary anna, which has made its clause a noun.",
         "Why must the khabar come first? Because otherwise one khabar would be claimed by two governors — inna for Zayd and the inception for ʿAmr — and one iʿrāb cannot have two governors: إِنَّ زَيْدًا وَعَمْرٌو ذَاهِبَانِ is void. The khabar may come first in reckoning too (إِنَّ زَيْدًا وَعَمْرٌو قَائِمٌ, each with his own قَائِمٌ). The Kufans drop the condition; al-Mubarrad and al-Kisāʾī allow it when the ism is a pronoun.",
         "Where may the lām of inception go? Three seats, all with inna and none with anna: on the khabar (لَقَائِمٌ), on the ism when a khabar-phrase separates them (إِنَّ فِي الدَّارِ لَزَيْدًا), and on a word standing between ism and khabar (لَطَعَامَكَ آكِلٌ). With lākinna it is weak.",
         "What happens when inna is lightened? It becomes in, and its khabar MUST carry the lām — otherwise it reads as the negating in. It may then stop governing and enter on kāna or ẓanna: إِنْ كَانَتْ لَكَبِيرَةً, إِنْ نَظُنُّكَ لَمِنَ الْكَاذِبِينَ. The Kufans extend it to any verb on the strength of إِنْ قَتَلْتَ لَمُسْلِمًا.",
         "And anna lightened? It becomes an, and governs a hidden pronoun of the matter — its ism in the place of naṣb — while the whole sentence after it is its khabar: أَنِ الْحَمْدُ لِلَّهِ. Governing a visible pronoun (أَنْكَ قَائِمٌ) is irregular.",
         "What must follow the lightened an? Before a conjugating verb that is not a condition or a prayer, one of four separators: the sīn (أَنْ سَيَكُونُ), sawfa (أَنْ سَوْفَ يَأْتِي), qad (أَنْ قَدْ أَبْلَغُوا) or a negation (أَنْ لَا يَرْجِعُ). The separator is what tells this an from the an that governs the muḍāriʿ in naṣb — the analyzer's an-masdariyya branch tests for exactly these four."],
  "tr": ["İnne'nin ismine ref' ile bir kelime atfedilebilir mi? Evet — mübtedânın mahalli olan MAHALLİNE, çünkü inne cümlenin mânâsını değiştirmez: إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو. Aynısı inne hükmünde olan, bilme fiilinden sonraki enne için de geçerlidir; cümlesini isim yapmış olan sıradan enne için asla.",
         "Haber neden önce gelmelidir? Çünkü aksi hâlde bir haberi iki âmil ister — Zeyd için inne, Amr için ibtidâ — ve bir i'rabın iki âmili olamaz: إِنَّ زَيْدًا وَعَمْرٌو ذَاهِبَانِ bâtıldır. Haber takdiren de önce gelebilir (إِنَّ زَيْدًا وَعَمْرٌو قَائِمٌ, her birinin kendi قَائِمٌ'ü). Kûfeliler şartı düşürür; Müberred ile Kisâî isim zamirse izin verir.",
         "İbtidâ lâmı nereye girebilir? Üç yere, hepsi inne ile, hiçbiri enne ile değil: habere (لَقَائِمٌ), bir haber ibaresi araya girdiğinde isme (إِنَّ فِي الدَّارِ لَزَيْدًا) ve isimle haber arasında duran kelimeye (لَطَعَامَكَ آكِلٌ). Lâkinne ile zayıftır.",
         "İnne hafifleyince ne olur? İn olur ve haberi lâm taşımak ZORUNDADIR — yoksa nâfiye in okunur. O zaman amelden kesilebilir ve kâne ya da zanne üzerine girebilir: إِنْ كَانَتْ لَكَبِيرَةً, إِنْ نَظُنُّكَ لَمِنَ الْكَاذِبِينَ. Kûfeliler إِنْ قَتَلْتَ لَمُسْلِمًا'ya dayanarak bunu her fiile yayar.",
         "Ya hafifleyen enne? En olur ve gizli bir şan zamirinde amel eder — mahallen mansûb ismi — ardındaki bütün cümle ise haberidir: أَنِ الْحَمْدُ لِلَّهِ. Açık bir zamirde amel etmesi (أَنْكَ قَائِمٌ) şâzdır.",
         "Hafif en'in ardından ne gelmeli? Şart ya da dua olmayan mutasarrıf bir fiilden önce dört ayırıcıdan biri: sîn (أَنْ سَيَكُونُ), sevfe (أَنْ سَوْفَ يَأْتِي), kad (أَنْ قَدْ أَبْلَغُوا) ya da nefy (أَنْ لَا يَرْجِعُ). Bu en'i muzârii nasb eden en'den ayıran ayırıcıdır — analizörün en-i masdariyye dalı tam bu dördünü test eder."]},
 "plain": {
  "en": "Four fine points about inna: you may add «and ʿAmr» in rafʿ after inna's sentence is complete; the emphatic lām may sit on the predicate, on a delayed subject, or on a word between them; a lightened in must show that lām; and a lightened an hides its subject and needs «will», «already» or «not» before its verb.",
  "tr": "İnne hakkında dört ince nokta: inne'nin cümlesi tamamlanınca «ve Amr»ı ref' ile ekleyebilirsin; te'kid lâmı yüklemde, sonraya kalmış öznede ya da aralarındaki kelimede oturabilir; hafiflemiş in o lâmı göstermelidir; hafiflemiş en öznesini gizler ve fiilinden önce «-ecek», «muhakkak» ya da «değil» ister."},
 "explanation": {
  "en": "This is the Kafiya's fine print on إِنَّ, and the notebook keeps every holder's name. Coordination on the place of the ism is licensed by the same principle that fixed the hamza in the previous chapter — إِنَّ leaves the sentence a sentence — and its condition, the khabar first, is argued rather than asserted: two governors may not share one iʿrāb. The notebook gives the Kufan dissent and the narrower dissent of al-Mubarrad and al-Kisāʾī for a mabnī ism, and extends the rule to لَكِنَّ. The lām of inception follows with its three seats and its two exclusions. The two lightenings are then set against each other: إِنْ loses its government and keeps a lām as a badge against the negative إِنْ, entering on كَانَ and ظَنَّ (the Basran limit) or on any verb (the Kufan one, with its verse); أَنْ keeps its government but spends it on the pronoun of the matter, so that a whole sentence can be its khabar, and before a conjugating verb it must be separated from the verb by one of four markers — each given its Qurʾānic or poetic case. For the parser the last rule is the useful one: the four markers are what distinguish this أَنْ from the أَنْ that puts the muḍāriʿ in naṣb.",
  "tr": "Bu, Kâfiye'nin إِنَّ üzerine ince yazısıdır ve defter her görüş sahibinin adını tutar. İsmin mahalline atıf, önceki bâbda hemzeyi belirleyen aynı ilkeyle meşrulaşır — إِنَّ cümleyi cümle bırakır — ve şartı, haberin önce gelmesi, iddia edilmez, kanıtlanır: iki âmil bir i'rabı paylaşamaz. Defter Kûfe muhalefetini ve mebnî isim için Müberred ile Kisâî'nin daha dar muhalefetini verir, kuralı لَكِنَّ'ye uzatır. İbtidâ lâmı üç yeri ve iki istisnasıyla izler. Sonra iki hafifleme karşı karşıya konur: إِنْ amelini kaybeder ve nâfiye إِنْ'e karşı nişan olarak lâmı tutar, كَانَ ve ظَنَّ üzerine girer (Basra sınırı) ya da her fiile (Kûfe sınırı, beytiyle); أَنْ amelini korur ama onu şan zamirine harcar, böylece bütün bir cümle haberi olabilir; mutasarrıf bir fiilden önce fiilden dört işaretten biriyle ayrılmalıdır — her biri Kur'ânî ya da şiirî örneğiyle verilir. Çözümleyici için son kural faydalıdır: dört işaret bu أَنْ'i muzârii nasb eden أَنْ'den ayıran şeydir."},
 "examples": [
  {"ar": "إِنَّ زَيْدًا قَائِمٌ وَعَمْرٌو — عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ وَعَمْرٌو", "en": "Coordination on the place, in word and in standing.", "tr": "Mahalle atıf, lafzen ve hükmen.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "إِنَّ زَيْدًا وَعَمْرٌو ذَاهِبَانِ", "en": "The void case: two governors on one iʿrāb.", "tr": "Bâtıl hâl: bir i'rabda iki âmil.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "إِنَّ فِي الدَّارِ لَزَيْدًا — إِنَّ زَيْدًا لَطَعَامَكَ آكِلٌ", "en": "The lām's second and third seats.", "tr": "Lâmın ikinci ve üçüncü yeri.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "وَإِنْ كَانَتْ لَكَبِيرَةً", "en": "Inna lightened, with its lām.", "tr": "Lâmıyla hafiflemiş inne.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَآخِرُ دَعْوَاهُمْ أَنِ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ", "en": "Anna lightened on the pronoun of the matter.", "tr": "Şan zamirinde hafiflemiş enne.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "عَلِمَ أَنْ سَيَكُونُ مِنْكُمْ مَرْضَى — أَنْ قَدْ أَبْلَغُوا — أَنْ لَا يَرْجِعُ", "en": "The four separators.", "tr": "Dört ayırıcı.", "sourceStory": "al-kafiya", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«إِنَّ زَيْدًا وَعَمْرٌو ذَاهِبَانِ»",
   "right": "«إِنَّ زَيْدًا وَعَمْرًا ذَاهِبَانِ — ya da haberden sonra: إِنَّ زَيْدًا ذَاهِبٌ وَعَمْرٌو»",
   "why": {"en": "Before the khabar the coordinate must follow inna's naṣb.", "tr": "Haberden önce ma'tûf inne'nin nasbına uymalıdır."}},
  {"wrong": "«عَلِمْتُ أَنَّ زَيْدًا لَقَائِمٌ»",
   "right": "«عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ — ibtidâ lâmı enne ile girmez»",
   "why": {"en": "The lām of inception belongs to inna's sentence, not to anna's noun-clause.", "tr": "İbtidâ lâmı inne'nin cümlesine aittir, enne'nin isim cümlesine değil."}},
  {"wrong": "«وَإِنْ كَانَتْ كَبِيرَةً — kıblenin değişmesi büyük olmadı»",
   "right": "«وَإِنْ كَانَتْ لَكَبِيرَةً — lâm, hafif inne'yi nâfiye in'den ayırır: elbette büyüktü»",
   "why": {"en": "Without the lām the sentence reads as a negation.", "tr": "Lâm olmadan cümle nefy okunur."}},
  {"wrong": "«عَلِمَ أَنْ يَكُونَ مِنْكُمْ مَرْضَى»",
   "right": "«عَلِمَ أَنْ سَيَكُونُ مِنْكُمْ مَرْضَى — hafif en'den sonra sîn gelir ve fiil merfû kalır»",
   "why": {"en": "After a verb of knowing, an is the lightened anna, not the an of naṣb; the separator marks it.", "tr": "Bilme fiilinden sonra en, nasb eden en değil hafiflemiş enne'dir; ayırıcı bunu işaretler."}}],
 "relatedNotes": ["al-huruf-al-mushabbaha-bil-fil-fil-kafiya", "inna-wa-akhawatuha", "inna-am-anna", "an-masdariyya", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan", "atf-nasaq"]}

ADD_EN = (" Chapter 35 (notebook lines ~339-340): coordination on the place of inna's ism and its condition, the lām of inception, and the lightened in and an (2:143, 26:186, 10:10, 73:20, 72:28, 20:89; the Kufans' verse and the verse of the man's knowledge) — the notebook's exposition, kept as commentary (s1-s10). Qurʾānic text as the source prints it.")
ADD_TR = (" Otuz beşinci bâb (defter satırları ~339-340): inne'nin isminin mahalline atıf ve şartı, ibtidâ lâmı ve hafiflemiş in ile en (2:143, 26:186, 10:10, 73:20, 72:28, 20:89; Kûfelilerin beyti ve kişinin bilgisi beyti) — defterin açıklaması, şerh olarak (s1-s10). Kur'ân metni kaynağın bastığı gibi.")
write_out(35, S, TITLE, ADD_EN, ADD_TR, "339-340", GLOSS_ADD, notes=(NOTE,),
          related=(("al-huruf-al-mushabbaha-bil-fil-fil-kafiya", [K]), ("inna-wa-akhawatuha", [K])))
report(35, S, GLOSS_ADD, (NOTE,))
