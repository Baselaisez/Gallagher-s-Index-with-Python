# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 8: THE LIMIT-WORDS AND THE REST OF THE BUILT ADVERBS. The tamyiz of كَمْ dropped where a clue stands (commentary);
the adverbs cut off from annexation (قَبْلُ، بَعْدُ، تَحْتُ، فَوْقُ، قُدَّامُ، خَلْفُ، وَرَاءُ) built on the damm, with لَا غَيْرُ and حَسْبُ in their
place; حَيْثُ annexed to a sentence (rarely to a single word); لَدَى and لَدُنْ for عِنْدَ; قَطُّ for the negated past, عَوْضُ for the
negated future; the adverb annexed to a sentence or to إِذْ may be built on the fath (al-Ma'ida 5:119, Hud 11:66), and so may
غَيْر and مِثْل before مَا، أَنْ and أَنَّ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~208-209 of the transcription.

  VERBATIM from the notebook's Arabic: every example and both ayas (as it cites them).
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s2, s4, s5, s6, s7, s9, s11.
  COMMENTARY (the notebook's own explanation): s1, s3, s8, s10, s12 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch8.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"
K3 = "al-mabni-wal-mudmar"
K7 = "al-kinayat-wal-zuruf-al-mabniyya"
MQ = "al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"
JB = "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"
TITLE = {"ar": "الْغَايَاتُ وَبَقِيَّةُ الظُّرُوفِ الْمَبْنِيَّةِ", "en": "The limit-words and the rest of the built adverbs", "tr": "Gâyeler ve mebnî zarfların geri kalanı"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
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
def kam_ex(full_tam, lex_tam, tam_ar, tam_en, tam_tr, verb_full, verb_lex, verb_segs, verb_en, verb_tr, punct):
    return [W("كَمْ", "kam", "pron", [K7, "mubtada-khabar"], "لَفْظٌ مَحْكِيٌّ؛ فِي الْمِثَالِ اسْمُ اسْتِفْهَامٍ أَوْ خَبَرٍ.", "«how many».", "«kaç / nice».")]

# ----------- s1 (COMMENTARY): the dropped tamyiz
S.append({"id": "s1", "translation": {
 "en": "And the tamyīz is sometimes dropped where a clue stands — as in «how much is your wealth?» and «how many times did you beat?», that is, كَمْ دِرْهَمًا مَالُكَ and كَمْ مَرَّةً ضَرَبْتَ." + C_EN,
 "tr": "Karîne bulununca temyîz bazen hazfedilir — «malın ne kadar?» ve «kaç kere dövdün?» gibi; yani كَمْ دِرْهَمًا مَالُكَ ve كَمْ مَرَّةً ضَرَبْتَ." + C_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("يُحْذَفُ", "hadhafa", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is dropped».", "«hazfedilir»."),
  W("الْمُمَيِّزُ", "mumayyiz", "noun", ["naib-al-fail", "tamyiz"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«the tamyīz» — the deputy doer.", "«temyîz» — nâib-i fâil."),
  W("لِقَرِينَةٍ", "qarina", "noun", ["huruf-jarr", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَقَرِينَةٍ مَجْرُورٌ.", "«for a clue».", "«bir karîne için».", punct="،", segments=[seg("لِ", "lam-taleel", "part"), seg("قَرِينَةٍ", "qarina", "noun")]),
  nahwu(),
  W("كَمْ", "kam", "pron", [K7, "mubtada-khabar", "hadhf-wa-taqdir"], "لَفْظٌ مَحْكِيٌّ؛ فِي الْمِثَالِ مُبْتَدَأٌ، وَمُمَيِّزُهَا مَحْذُوفٌ: دِرْهَمًا أَوْ دِرْهَمٍ.", "«how much» — its tamyīz understood.", "«ne kadar» — temyîzi takdir edilmiş."),
  W("مَالُكَ", "mal", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«is your wealth».", "«malın».", punct="؟", segments=[seg("مَالُ", "mal", "noun"), pr2ms()]),
  cited_wa("وَكَمْ", "kam", "pron", [K7, "maful-mutlaq", "hadhf-wa-taqdir"], "كَمْ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ مُطْلَقٌ، وَمُمَيِّزُهَا مَحْذُوفٌ: مَرَّةً أَوْ مَرَّةٍ.", "«and how many» — the absolute object, its tamyīz understood.", "«ve kaç» — mef'ûl-i mutlak, temyîzi takdir edilmiş.", "كَمْ"),
  W("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you beat».", "«dövdün».", punct="؟", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
  W("أَيْ", "ay-tafsir", "part", ["al-mabni-wal-mudmar"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».", punct=":"),
  cited("كَمْ", "kam", "pron", [K7], "مُبْتَدَأٌ.", "«how many».", "«kaç»."),
  W("دِرْهَمًا", "dirham", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — الْمَحْذُوفُ مُقَدَّرًا.", "«dirhams» — the dropped tamyīz restored.", "«dirhem» — hazfedilen temyîz geri konmuş."),
  W("مَالُكَ", "mal", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ.", "«is your wealth».", "«malın».", segments=[seg("مَالُ", "mal", "noun"), pr2ms()]),
  cited_wa("وَكَمْ", "kam", "pron", [K7, "maful-mutlaq"], "كَمْ مَفْعُولٌ مُطْلَقٌ.", "«and how many».", "«ve kaç».", "كَمْ"),
  W("مَرَّةً", "marra-once", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«times».", "«kere»."),
  W("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«did you beat».", "«dövdün».", punct=".", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
 ]})

# ----------- s2 (RESTORED): the cut-off adverbs
S.append({"id": "s2", "translation": {
 "en": "And the adverbs cut off from annexation are built on the ḍamm — as in قَبْلُ، بَعْدُ، تَحْتُ، فَوْقُ، قُدَّامُ، خَلْفُ and وَرَاءُ." + R_EN,
 "tr": "İzâfetten kesilen zarflar damm üzere mebnîdir — قَبْلُ، بَعْدُ، تَحْتُ، فَوْقُ، قُدَّامُ، خَلْفُ ve وَرَاءُ gibi." + R_TR},
 "tokens": [
  atf_wa("وَالظُّرُوفُ", "zarf", "noun", ["mubtada-khabar", "jam-taksir", MQ], "الظُّرُوفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the adverbs» — the mubtada.", "«ve zarflar» — mübtedâ.", "الظُّرُوفُ"),
  W("الْمَقْطُوعَةُ", "qataa", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ — اسْمُ مَفْعُولٍ.", "«cut off».", "«kesilmiş»."),
  W("عَنِ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  W("الْإِضَافَةِ", "idafa", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«annexation».", "«izâfetten»."),
  W("مَبْنِيَّةٌ", "mabni", "noun", ["mubtada-khabar", K3, MQ], "خَبَرٌ مَرْفُوعٌ.", "«are built» — the khabar.", "«mebnîdir» — haber."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الضَّمِّ", "damm", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the ḍamm».", "«damm».", punct="،"),
  nahwu(),
  cited("قَبْلُ", "qablu", "noun", ["idafa-definiteness", MQ], "فِي مَحَلِّ جَرٍّ — مَبْنِيٌّ عَلَى الضَّمِّ، حُذِفَ مُضَافُهُ إِلَيْهِ وَنُوِيَ مَعْنَاهُ.", "«before» — built on the ḍamm, its muḍāf ilayh dropped and its meaning kept.", "«önce» — damm üzere mebnî; muzâfun ileyhi hazfedilmiş, manası niyet edilmiş."),
  cited_wa("وَبَعْدُ", "badu-after", "noun", [MQ], "بَعْدُ مَعْطُوفٌ.", "«and after».", "«ve sonra».", "بَعْدُ"),
  cited_wa("وَتَحْتُ", "tahta", "noun", [MQ], "تَحْتُ مَعْطُوفٌ.", "«and below».", "«ve alt».", "تَحْتُ"),
  cited_wa("وَفَوْقُ", "fawqa", "noun", [MQ], "فَوْقُ مَعْطُوفٌ.", "«and above».", "«ve üst».", "فَوْقُ"),
  cited_wa("وَقُدَّامُ", "quddam", "noun", [MQ], "قُدَّامُ مَعْطُوفٌ.", "«and in front».", "«ve ön».", "قُدَّامُ"),
  cited_wa("وَخَلْفُ", "khalf", "noun", [MQ], "خَلْفُ مَعْطُوفٌ.", "«and behind».", "«ve arka».", "خَلْفُ"),
  cited_wa("وَوَرَاءُ", "waraa", "noun", [MQ], "وَرَاءُ مَعْطُوفٌ.", "«and beyond».", "«ve öte».", "وَرَاءُ", punct="."),
 ]})

# ----------- s3 (COMMENTARY)
S.append({"id": "s3", "translation": {
 "en": "And لَا غَيْرُ، لَيْسَ غَيْرُ and حَسْبُ are used in their manner, the muḍāf ilayh dropped and the word built on the ḍamm." + C_EN,
 "tr": "لَا غَيْرُ، لَيْسَ غَيْرُ ve حَسْبُ de onların yolunda kullanılır: muzâfun ileyh hazfedilir ve kelime damm üzere mebnî olur." + C_TR},
 "tokens": [
  atf_wa("وَيُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "يُسْتَعْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is used».", "«ve kullanılır».", "يُسْتَعْمَلُ"),
  cited("لَا", "la", "part", ["naib-al-fail", "la-nafiya"], "لَا غَيْرُ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«no other» — the deputy doer, cited.", "«lâ gayru» — nâib-i fâil, hikâye."),
  W("غَيْرُ", "ghayr", "noun", [MQ, "idafa-definiteness"], "مَبْنِيٌّ عَلَى الضَّمِّ — حُذِفَ مُضَافُهُ إِلَيْهِ.", "«other» — built on the ḍamm, its muḍāf ilayh dropped.", "«gayru» — damm üzere mebnî; muzâfun ileyhi hazfedilmiş."),
  cited_wa("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha"], "لَيْسَ غَيْرُ مَعْطُوفٌ.", "«and not other».", "«ve leyse gayru».", "لَيْسَ"),
  W("غَيْرُ", "ghayr", "noun", [MQ], "مَبْنِيٌّ عَلَى الضَّمِّ.", "«other».", "«gayru»."),
  cited_wa("وَحَسْبُ", "hasb-enough", "noun", [MQ], "حَسْبُ مَعْطُوفٌ — بِمَعْنَى كَافٍ، مَبْنِيٌّ عَلَى الضَّمِّ.", "«and enough» — built on the ḍamm.", "«ve hasbü» — damm üzere mebnî.", "حَسْبُ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  W("طَرِيقَتِهَا", "tariqa", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«their manner».", "«onların yolunda».", punct="،", segments=[seg("طَرِيقَتِ", "tariqa", "noun"), pr3fs()]),
  W("يُحْذَفُ", "hadhafa", "verb", ["naib-al-fail", "hal"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ حَالٌ.", "«dropped» — a ḥāl clause.", "«hazfedilir» — hâl cümlesi."),
  W("الْمُضَافُ", "mudaf", "noun", ["naib-al-fail"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«the muḍāf».", "«muzâf»."),
  W("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«ilayh».", "«ileyh».", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  atf_wa("وَتُبْنَى", "bana", "verb", ["naib-al-fail", "naqis-verbs"], "تُبْنَى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is built».", "«ve mebnî kılınır».", "تُبْنَى"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الضَّمِّ", "damm", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the ḍamm».", "«damm».", punct="."),
 ]})

# ----------- s4 (RESTORED): haythu
S.append({"id": "s4", "translation": {
 "en": "And حَيْثُ is built on the ḍamm, and it is mostly annexed to a sentence — as in «sit where Zayd is sitting» — and sometimes to a single word, as in «do you not see where Suhayl is?»." + R_EN,
 "tr": "حَيْثُ damm üzere mebnîdir ve çoğunlukla bir cümleye muzâf olur — «Zeyd'in oturduğu yere otur» gibi — bazen bir müfrede muzâf olur, «Süheyl'in yerini görmez misin?» gibi." + R_TR},
 "tokens": [
  cited_wa("وَحَيْثُ", "haythu", "noun", ["mubtada-khabar", K7], "حَيْثُ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and حَيْثُ» — the mubtada.", "«ve haysü» — mübtedâ.", "حَيْثُ"),
  W("مَبْنِيَّةٌ", "mabni", "noun", ["mubtada-khabar", K3], "خَبَرٌ مَرْفُوعٌ.", "«is built».", "«mebnîdir»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الضَّمِّ", "damm", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the ḍamm».", "«damm».", punct="،"),
  atf_wa("وَتُضَافُ", "adafa", "verb", ["naib-al-fail", "form-iv-verbs"], "تُضَافُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and it is annexed».", "«ve muzâf olur».", "تُضَافُ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«a sentence».", "«cümleye»."),
  W("غَالِبًا", "ghalib", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«mostly».", "«çoğunlukla».", punct="،"),
  nahwu(),
  W("اجْلِسْ", "jalasa", "verb", ["imperative-amr"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا.", "«sit!».", "«otur!»."),
  W("حَيْثُ", "haythu", "noun", [K7, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ.", "«where» — annexed to the clause.", "«... yerde» — cümleye muzâf."),
  W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«Zayd» — the mubtada of the annexed clause.", "«Zeyd» — muzâf cümlenin mübtedâsı."),
  W("جَالِسٌ", "jalis-sitting", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«is sitting».", "«oturmaktadır».", punct="،"),
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("تُضَافُ", "adafa", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it is annexed».", "«muzâf olur»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْمُفْرَدِ", "mufrad", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«a single word».", "«müfrede».", punct="،"),
  nahwu(),
  W("أَمَا", "ama", "part", ["al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَمَا نَافِيَةٌ.", "«do you not».", "«... mez misin»."),
  W("تَرَى", "raa", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«you see».", "«görürsün»."),
  W("حَيْثُ", "haythu", "noun", [K7, "maful-bihi", "idafa-definiteness"], "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، مُضَافٌ إِلَى الْمُفْرَدِ.", "«where» — annexed to a single noun.", "«yerini» — müfrede muzâf."),
  W("سُهَيْلٍ", "suhayl", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Suhayl» — the star Canopus.", "«Süheyl» — yıldız.", punct="؟"),
 ]})

# ----------- s5 (RESTORED): lada, ladun
S.append({"id": "s5", "translation": {
 "en": "And لَدَى and لَدُنْ have the meaning of عِنْدَ — as in «the wealth is with Zayd»." + R_EN,
 "tr": "لَدَى ve لَدُنْ, عِنْدَ manasındadır — «mal Zeyd'in yanındadır» gibi." + R_TR},
 "tokens": [
  cited_wa("وَلَدَى", "lada", "noun", ["mubtada-khabar", K7], "لَدَى مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and لَدَى» — the mubtada.", "«ve ledâ» — mübtedâ.", "لَدَى"),
  cited_wa("وَلَدُنْ", "ladun", "noun", [K7], "لَدُنْ مَعْطُوفٌ — وَفِيهَا لُغَاتٌ: لَدْنِ، لَدَنْ، لُدْنِ، لَدْ، لُدْ، لَدُ.", "«and لَدُنْ» — with its dialect forms.", "«ve ledün» — lehçe şekilleriyle.", "لَدُنْ"),
  W("بِمَعْنَى", "mana", "noun", ["huruf-jarr", "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in the meaning of» — the khabar.", "«manasındadır» — haber.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  cited("عِنْدَ", "inda", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«عِنْدَ».", "«inde».", punct="،"),
  nahwu(),
  W("الْمَالُ", "mal", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the wealth».", "«mal»."),
  W("لَدَى", "lada", "noun", [K7, "maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ خَبَرٌ، وَهُوَ مُضَافٌ — لِلْحَاضِرِ بِالْفِعْلِ.", "«is with» — the khabar: for what is actually present.", "«yanındadır» — haber: bilfiil hâzır olan için."),
  W("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd».", punct="."),
 ]})

# ----------- s6 (RESTORED): qattu, awdu
S.append({"id": "s6", "translation": {
 "en": "And قَطُّ for the negated past, as in «I have never seen him»; and عَوْضُ for the negated future, as in «I shall never see him»." + R_EN,
 "tr": "قَطُّ menfî mâzî içindir, «onu hiç görmedim» gibi; عَوْضُ menfî gelecek içindir, «onu asla görmem» gibi." + R_TR},
 "tokens": [
  cited_wa("وَقَطُّ", "qattu", "noun", ["mubtada-khabar", K7], "قَطُّ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى الضَّمِّ.", "«and قَطُّ» — the mubtada.", "«ve kattu» — mübtedâ.", "قَطُّ"),
  li_("لِلْمَاضِي", "madi", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "الْمَاضِي مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the past» — the khabar.", "«mâzî için» — haber.", "الْمَاضِي", segs=[seg("لِ", "li", "prep"), seg("الْمَاضِي", "madi", "noun")]),
  W("الْمَنْفِيِّ", "manfi", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«negated».", "«menfî».", punct="،"),
  nahwu(),
  W("مَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not».", "«-medim»."),
  W("رَأَيْتُهُ", "raa", "verb", ["fail", "maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I saw him».", "«onu gördüm».", segments=[seg("رَأَيْ", "raa", "verb"), prT(), pr3ms()]),
  W("قَطُّ", "qattu", "noun", [K7, "maful-fih"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — لِاسْتِغْرَاقِ الْمَاضِي.", "«ever» — the whole past.", "«hiç» — bütün geçmiş.", punct="؛"),
  cited_wa("وَعَوْضُ", "awd-adverb", "noun", ["mubtada-khabar", K7], "عَوْضُ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى الضَّمِّ.", "«and عَوْضُ» — the mubtada.", "«ve avdu» — mübtedâ.", "عَوْضُ"),
  li_("لِلْمُسْتَقْبَلِ", "mustaqbal", "noun", ["mubtada-khabar"], "الْمُسْتَقْبَلِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the future» — the khabar.", "«gelecek için» — haber.", "الْمُسْتَقْبَلِ", segs=[seg("لِ", "li", "prep"), seg("الْمُسْتَقْبَلِ", "mustaqbal", "noun")]),
  W("الْمَنْفِيِّ", "manfi", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«negated».", "«menfî».", punct="،"),
  nahwu(),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«-mem»."),
  W("أَرَاهُ", "raa", "verb", ["fail", "maful-bihi", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I see him».", "«onu görürüm».", segments=[seg("أَرَا", "raa", "verb"), pr3ms()]),
  W("عَوْضُ", "awd-adverb", "noun", [K7, "maful-fih"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — لِاسْتِغْرَاقِ الْمُسْتَقْبَلِ.", "«ever» — the whole future.", "«asla» — bütün gelecek.", punct="."),
 ]})

# ----------- s7 (RESTORED): the optional building before a clause
S.append({"id": "s7", "translation": {
 "en": "And the adverb annexed to a sentence or to إِذْ may be built on the fatḥ — as in «the day their truthfulness benefits the truthful» and «from the disgrace of that day»." + R_EN,
 "tr": "Bir cümleye ya da إِذْ'e muzâf olan zarfın feth üzere mebnî olması câizdir — «doğruluklarının doğrulara fayda vereceği gün» ve «o günün rezilliğinden» gibi." + R_TR},
 "tokens": [
  atf_wa("وَالظَّرْفُ", "zarf", "noun", ["mubtada-khabar", JB], "الظَّرْفُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the adverb» — the mubtada.", "«ve zarf» — mübtedâ.", "الظَّرْفُ"),
  W("الْمُضَافُ", "mudaf", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«annexed».", "«muzâf olan»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«a sentence».", "«cümleye»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  cited("إِذْ", "idh", "part", ["huruf-jarr", K7], "فِي مَحَلِّ جَرٍّ.", "«إِذْ».", "«iz»."),
  W("يَجُوزُ", "jaaza", "verb", ["mubtada-khabar", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«may» — the khabar clause.", "«câizdir» — haber cümlesi."),
  W("بِنَاؤُهُ", "bina", "noun", ["fail", "idafa-definiteness", "masdar", JB], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its being built» — the doer.", "«mebnî olması» — fâil.", segments=[seg("بِنَاؤُ", "bina", "noun"), pr3ms()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْفَتْحِ", "fath", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the fatḥ».", "«feth».", punct="،"),
  nahwu(),
  W("يَوْمَ", "yawm", "noun", [JB, "maful-fih", "idafa-definiteness", "al-iqtibas-wal-tadmin"], "ظَرْفٌ مُضَافٌ إِلَى الْجُمْلَةِ — مَبْنِيٌّ عَلَى الْفَتْحِ أَوْ مَنْصُوبٌ (الْمَائِدَة ١١٩).", "«the day» — built on the fatḥ or in naṣb, both allowed (al-Māʾida 5:119).", "«gün» — feth üzere mebnî ya da mansûb; ikisi de câiz (Mâide 5:119)."),
  W("يَنْفَعُ", "nafaa", "verb", ["fail", "idafa-definiteness"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«benefits» — the annexed clause.", "«fayda verir» — muzâf cümle."),
  W("الصَّادِقِينَ", "sadiq", "noun", ["maful-bihi", "jam-mudhakkar-salim"], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِالْيَاءِ.", "«the truthful» — the fronted object.", "«doğrulara» — öne alınmış mef'ûl."),
  W("صِدْقُهُمْ", "sidq", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their truthfulness» — the doer.", "«doğrulukları» — fâil.", punct="،", segments=[seg("صِدْقُ", "sidq", "noun"), pr3mp()]),
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr", "al-iqtibas-wal-tadmin"], "مِنْ حَرْفُ جَرٍّ (هُود ٦٦).", "«and from» (Hūd 11:66).", "«ve -den» (Hûd 11:66).", "مِنْ"),
  W("خِزْيِ", "khizy", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the disgrace of».", "«rezilliğinden»."),
  W("يَوْمَئِذٍ", "yawmaidhin", "noun", [JB, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ — يَوْمَ مُضَافٌ إِلَى إِذْ، مَبْنِيٌّ عَلَى الْفَتْحِ فِي قِرَاءَةٍ وَمَجْرُورٌ فِي الْمُصْحَفِ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْجُمْلَةِ.", "«that day» — يَوْمَ annexed to إِذْ: built on the fatḥ in one reading, in jarr in the muṣḥaf; the tanwīn stands for the dropped clause.", "«o gün» — إِذْ'e muzâf يَوْمَ: bir kıraatte feth üzere mebnî, mushafta mecrûr; tenvin hazfedilen cümlenin ivazı.", punct=".", segments=[seg("يَوْمَ", "yawm", "noun"), seg("ئِذٍ", "idh", "part")]),
 ]})
for _t in S[6]["tokens"]:
    if _t["surface"]["full"] == "صِدْقُهُمْ": _t["quoteAfter"] = "﴾"
    if _t["surface"]["full"] == "يَوْمَئِذٍ": _t["quoteAfter"] = "﴾"
S[6]["tokens"][12]["quoteBefore"] = "﴿"; S[6]["tokens"][16]["quoteBefore"] = "﴿"

# ----------- s8 (COMMENTARY)
S.append({"id": "s8", "translation": {
 "en": "But in the Qurʾān it is declined, يَوْمِئِذٍ, with the kasra." + C_EN,
 "tr": "Ancak Kur'ân-ı Kerîm'de kesre ile mu'reb olarak يَوْمِئِذٍ okunur." + C_TR},
 "tokens": [
  W("لٰكِنَّهُ", "lakinna", "part", ["inna-wa-akhawatuha"], "حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهُ.", "«but it».", "«ancak o».", segments=[seg("لٰكِنَّ", "lakinna", "part"), pr3ms()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْقُرْآنِ", "quran", "propn", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the Qurʾān».", "«Kur'ân»."),
  W("مُعْرَبٌ", "murab", "noun", ["inna-wa-akhawatuha", "ism-maful"], "خَبَرُ لٰكِنَّ مَرْفُوعٌ.", "«is declined» — the khabar.", "«mu'rebdir» — haber."),
  W("بِالْكَسْرِ", "kasr", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْكَسْرِ مَجْرُورٌ.", "«with the kasra».", "«kesre ile».", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْكَسْرِ", "kasr", "noun")]),
  cited("يَوْمِئِذٍ", "yawmaidhin", "noun", [JB, "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ — مُعْرَبٌ.", "«that day» — declined.", "«o gün» — mu'reb.", punct=".", segments=[seg("يَوْمِ", "yawm", "noun"), seg("ئِذٍ", "idh", "part")]),
 ]})

# ----------- s9 (RESTORED): ghayr and mithl
S.append({"id": "s9", "translation": {
 "en": "And so may غَيْر and مِثْل with مَا، أَنْ and أَنَّ — as in «my standing is like Zayd's standing», «like that Zayd should stand», «like that you stand»." + R_EN,
 "tr": "مَا، أَنْ ve أَنَّ ile birlikte غَيْر ve مِثْل için de böyledir — «benim kalkışım Zeyd'in kalkışı gibi», «Zeyd'in kalkması gibi», «senin kalkman gibi» gibi." + R_TR},
 "tokens": [
  atf_wa("وَكَذٰلِكَ", "dhalika", "pron", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh", "asma-al-ishara"], "الْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ فِي مَحَلِّ جَرٍّ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and likewise» — the fronted khabar.", "«ve böyledir» — öne alınmış haber.", "ذٰلِكَ", extra_segs=[seg("كَ", "ka", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  cited("غَيْرُ", "ghayr", "noun", ["mubtada-khabar", JB], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«غَيْر» — the delayed mubtada.", "«gayr» — mübtedâ."),
  cited_wa("وَمِثْلُ", "mithl", "noun", [JB], "مِثْلُ مَعْطُوفٌ مَرْفُوعٌ.", "«and مِثْل».", "«ve misl».", "مِثْلُ"),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  cited("مَا", "ma-mawsula", "pron", ["idafa-definiteness", "anwa-ma"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«مَا».", "«mâ»."),
  cited_wa("وَأَنْ", "an-masdariyya", "part", ["an-masdariyya"], "أَنْ مَعْطُوفٌ.", "«and أَنْ».", "«ve en».", "أَنْ"),
  cited_wa("وَأَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "أَنَّ مَعْطُوفٌ.", "«and أَنَّ».", "«ve enne».", "أَنَّ", punct="،"),
  nahwu(),
  W("قِيَامِي", "qiyam", "noun", ["mubtada-khabar", "idafa-definiteness", "masdar"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my standing» — the mubtada.", "«kalkışım» — mübtedâ.", segments=[seg("قِيَامِ", "qiyam", "noun"), seg("ي", "pron-1s", "pron")]),
  W("مِثْلَ", "mithl", "noun", [JB, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى مَا — وَيَجُوزُ رَفْعُهُ.", "«like» — the khabar, built on the fatḥ before مَا; rafʿ is allowed too.", "«gibi» — haber; مَا'dan önce feth üzere mebnî; ref' de câiz."),
  W("مَا", "ma-masdariyya", "part", ["anwa-ma", "idafa-definiteness"], "مَا الْمَصْدَرِيَّةُ، وَالْجُمْلَةُ بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مُضَافٌ إِلَيْهِ.", "«that» — the maṣdar مَا; the clause is the muḍāf ilayh.", "«-ması» — masdariyye mâ; cümle muzâfun ileyh."),
  W("قَامَ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«stood».", "«kalktı»."),
  W("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="،"),
  W("قِيَامِي", "qiyam", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ.", "«my standing».", "«kalkışım».", segments=[seg("قِيَامِ", "qiyam", "noun"), seg("ي", "pron-1s", "pron")]),
  W("مِثْلَ", "mithl", "noun", [JB, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى أَنْ.", "«like» — built on the fatḥ before أَنْ.", "«gibi» — أَنْ'den önce feth üzere mebnî."),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "idafa-definiteness"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ.", "«that».", "«-ması»."),
  W("يَقُومَ", "qama", "verb", ["an-masdariyya", "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ.", "«should stand» — naṣb by أَنْ.", "«kalksın» — en ile mansûb."),
  W("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="،"),
  W("قِيَامِي", "qiyam", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ.", "«my standing».", "«kalkışım».", segments=[seg("قِيَامِ", "qiyam", "noun"), seg("ي", "pron-1s", "pron")]),
  W("مِثْلَ", "mithl", "noun", [JB, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى أَنَّ.", "«like» — built on the fatḥ before أَنَّ.", "«gibi» — أَنَّ'den önce feth üzere mebnî."),
  W("أَنَّكَ", "anna", "part", ["inna-wa-akhawatuha", "idafa-definiteness"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا.", "«that you».", "«senin».", segments=[seg("أَنَّ", "anna", "part"), pr2ms()]),
  W("تَقُومُ", "qama", "verb", ["inna-wa-akhawatuha", "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«stand» — the khabar of أَنَّ.", "«kalkman» — enne'nin haberi.", punct="."),
 ]})

# ----------- s10 (COMMENTARY)
S.append({"id": "s10", "translation": {
 "en": "For in these examples مِثْل may be built on the fatḥ, and may be declined and take rafʿ as the khabar." + C_EN,
 "tr": "Çünkü bu örneklerde مِثْل'in feth üzere mebnî olması da, mu'reb olup haber olarak merfû olması da câizdir." + C_TR},
 "tokens": [
  W("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«çünkü».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")]),
  cited("مِثْلَ", "mithl", "noun", ["inna-wa-akhawatuha", JB], "اسْمُ إِنَّ فِي مَحَلِّ نَصْبٍ.", "«مِثْل» — the ism of إِنَّ.", "«misl» — inne'nin ismi."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("هٰذِهِ", "hadhihi", "pron", ["huruf-jarr", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«these».", "«bu»."),
  W("الْأَمْثِلَةِ", "mithal", "noun", ["badal", "jam-taksir"], "بَدَلٌ مِنْ هٰذِهِ مَجْرُورٌ.", "«examples».", "«örneklerde»."),
  W("يَجُوزُ", "jaaza", "verb", ["inna-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«may» — the khabar of إِنَّ.", "«câizdir» — inne'nin haberi."),
  W("بِنَاؤُهُ", "bina", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its being built».", "«mebnî olması».", segments=[seg("بِنَاؤُ", "bina", "noun"), pr3ms()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْفَتْحِ", "fath", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the fatḥ».", "«feth».", punct="،"),
  atf_wa("وَإِعْرَابُهُ", "irab", "noun", ["fail", "idafa-definiteness"], "إِعْرَابُ مَعْطُوفٌ عَلَى بِنَاؤُهُ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its being declined».", "«ve mu'reb olması».", "إِعْرَابُ", extra_segs=[seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  W("مَرْفُوعًا", "marfu", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«in rafʿ».", "«merfû olarak»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«as».", "«olarak»."),
  W("الْخَبَرِيَّةِ", "khabariyya", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ — أَيْ: عَلَى أَنَّهُ خَبَرٌ.", "«the khabar».", "«haber».", punct="."),
 ]})

# ---------------------------------------------------------------- NFC
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
 "suhayl": need("suhayl", "سُهَيْل", None, "propn", "Suhayl — Canopus, the southern star; أَمَا تَرَى حَيْثُ سُهَيْلٍ: the proverb's single-word annex to حَيْثُ", "Süheyl — güney yıldızı Canopus; emâ terâ haysü Süheylin: haysü'nün müfrede muzâf olduğu darb-ı mesel", 6),
 "tariqa": need("tariqa", "طَرِيقَة", "ط ر ق", "noun", "way, manner", "yol, tarz", 3),
 "istamala": need("istamala", "اسْتَعْمَلَ", "ع م ل", "verb", "to use, to employ (Form X)", "kullanmak (istif'âl)", 3),
 "ay-tafsir": need("ay-tafsir", "أَيْ", None, "part", "that is, i.e. (the particle of explanation)", "yani (tefsir harfi)", 2),
 "lakinna": need("lakinna", "لٰكِنَّ", None, "part", "but (the sister of إِنَّ that corrects)", "fakat (inne'nin istidrâk bildiren kardeşi)", 2),
 "quran": need("quran", "الْقُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "murab": need("murab", "مُعْرَب", "ع ر ب", "noun", "declined — a word whose ending a governor changes (ism maf'ul of أَعْرَبَ)", "mu'reb — sonunu âmilin değiştirdiği kelime (a'rabe'nin ism-i mef'ûlü)", 3),
 "kasr": need("kasr", "كَسْر", "ك س ر", "noun", "the kasr — the vowel i as a building mark", "kesr — bina alâmeti olarak i sesi", 3),
 "mithal": need("mithal", "مِثَال", "م ث ل", "noun", "example", "örnek, misâl", 2, plural="أَمْثِلَة"),
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
put_morph(mo, "istamala", find_morph("istamala"))   # an identity copy: the key is owned elsewhere
report(8, S, GLOSS_ADD, (NOTE,))
