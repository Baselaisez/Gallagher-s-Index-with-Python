# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 34: THE VERB-LIKE PARTICLES (I) — the six; why «like the verb»; the head of speech (all but أَنَّ); the مَا that
stops them; إِنَّ leaves the sentence a sentence while أَنَّ makes it a single noun — so kasra where a sentence fits (the opening, after a
verb of saying without opinion, after a relative — 28:76) and fatḥa where a single noun fits (doer, object, delayed mubtada, muḍāf ilayh,
after لَوْلَا and لَوْ); both where both fit (after the fāʾ of the answer, after إِذَا of surprise — the verse of the slave of the nape).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~338-339 of the transcription.

  VERBATIM: s1. COMMENTARY (the notebook): s2-s10 — marked C_EN/C_TR. Qurʾānic text as the source prints it (28:76 cited in the received وَآتَيْنَاهُ).
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch34.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-huruf-al-mushabbaha-bil-fil-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "الْحُرُوفُ الْمُشَبَّهَةُ بِالْفِعْلِ: إِنَّ وَأَنَّ", "en": "The verb-like particles — the six, and the hamza of inna", "tr": "Fiile benzeyen harfler — altısı ve inne'nin hemzesi"}
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
HM = "inna-am-anna"
def INN(full="إِنَّ", lex="inna", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ — مَكْسُورَةٌ.", en="«indeed».", tr="«muhakkak».", punct=None, segs=None, tags=()):
    return cited(full, lex, "part", [K, IN, HM] + list(tags), ar, en, tr, punct=punct, segments=segs)
def ANN(full="أَنَّ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ — مَفْتُوحَةٌ، وَهِيَ مَعَ جُمْلَتِهَا فِي تَأْوِيلِ مَصْدَرٍ.", en="«that».", tr="«-dığı».", punct=None, segs=None, tags=()):
    return cited(full, "anna", "part", [K, IN, HM] + list(tags), ar, en, tr, punct=punct, segments=segs)
def ISM(full, lex, en, tr, pos="propn", punct=None, segs=None, tags=()): return cited(full, lex, pos, [IN] + list(tags), "اسْمُ الْحَرْفِ مَنْصُوبٌ.", en, tr, punct=punct, segments=segs)
def KHB(full, lex, en, tr, pos="noun", punct=None, ar="خَبَرُ الْحَرْفِ مَرْفُوعٌ.", tags=()): return cited(full, lex, pos, [IN] + list(tags), ar, en, tr, punct=punct)
def AYQ(): return W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».")

S.append({"id": "s1", "translation": {
 "en": "The particles likened to the verb: إِنَّ, أَنَّ, كَأَنَّ, لَكِنَّ, لَيْتَ and لَعَلَّ.",
 "tr": "Fiile benzeyen harfler: إِنَّ, أَنَّ, كَأَنَّ, لَكِنَّ, لَيْتَ ve لَعَلَّ'dir."},
 "tokens": [
  W("الْحُرُوفُ", "harf", "noun", ["mubtada-khabar", "jam-taksir", IN], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the particles».", "«harfler»."),
  W("الْمُشَبَّهَةُ", "mushabbah", "noun", ["naat-sifa", "ism-maful", IN], "صِفَةٌ مَرْفُوعَةٌ.", "«likened».", "«benzeyen»."),
  bi_("بِالْفِعْلِ", "fil", "noun", [], "الْفِعْلِ مَجْرُورٌ.", "«to the verb».", "«fiile».", "الْفِعْلِ", punct=":"),
  INN(ar="خَبَرٌ — حَرْفٌ مَحْكِيٌّ.", en="«inna».", tr="«inne».", tags=["mubtada-khabar"]),
  cited_wa("وَأَنَّ", "anna", "part", [K, IN], "أَنَّ مَعْطُوفٌ — حَرْفٌ مَحْكِيٌّ.", "«anna».", "«enne».", "أَنَّ"),
  cited_wa("وَكَأَنَّ", "kaanna", "part", [K, IN], "كَأَنَّ مَعْطُوفٌ.", "«ka-anna».", "«keenne».", "كَأَنَّ"),
  cited_wa("وَلَكِنَّ", "lakinna", "part", [K, IN], "لَكِنَّ مَعْطُوفٌ.", "«lākinna».", "«lâkinne».", "لَكِنَّ"),
  cited_wa("وَلَيْتَ", "layta", "part", [K, IN], "لَيْتَ مَعْطُوفٌ.", "«layta».", "«leyte».", "لَيْتَ"),
  cited_wa("وَلَعَلَّ", "laalla", "part", [K, IN], "لَعَلَّ مَعْطُوفٌ.", "«and laʿalla».", "«ve lealle».", "لَعَلَّ", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And they were called «likened to the verb» because they are of three, four or five letters, built on the fatḥa, and in each of them is the meaning of a verb." + C_EN,
 "tr": "«Fiile benzeyen» diye adlandırıldılar, çünkü üç, dört ya da beş harflidirler, fetha üzere mebnîdirler ve her birinde bir fiil mânâsı vardır." + C_TR},
 "tokens": [
  atf_wa("وَسُمِّيَتْ", "samma", "verb", ["naib-al-fail", "form-ii-verbs"], "سُمِّيَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and they were called».", "«ve adlandırıldılar».", "سُمِّيَتْ"),
  W("مُشَبَّهَةً", "mushabbah", "noun", ["mafulayn", "ism-maful"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«likened».", "«benzeyen»."),
  bi_("بِالْفِعْلِ", "fil", "noun", [], "الْفِعْلِ مَجْرُورٌ.", "«to the verb».", "«fiile».", "الْفِعْلِ"),
  W("لِأَنَّهَا", "lianna", "part", [IN, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because they».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("ثُلَاثِيَّةٌ", "thulathi", "noun", [IN], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«of three letters».", "«üç harfli»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("رُبَاعِيَّةٌ", "rubai", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«four».", "«dört»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("خُمَاسِيَّةٌ", "khumasi", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«five».", "«beş harfli».", punct="،"),
  W("مَبْنِيَّةٌ", "mabni", "noun", [IN, "al-murab-wal-mabni-wal-irab"], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«built».", "«mebnî»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْفَتْحِ", "fath", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the fatḥa».", "«fetha».", punct="،"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "فِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in».", "«ve ... -de».", "فِي"),
  W("كُلٍّ", "kull", "noun", ["huruf-jarr"], "مَجْرُورٌ — نُوِّنَ لِقَطْعِهِ عَنِ الْإِضَافَةِ.", "«each».", "«her birinde»."),
  W("مِنْهَا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ.", "«of them».", "«onlardan».", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  W("مَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus", "mana-al-fil"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the meaning of».", "«mânâsı»."),
  W("فِعْلٍ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«bir fiil».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And they have the head of speech, so that its kind — emphasis, likeness, correction, wish or hope — is known from the first; except أَنَّ, for it does not stand at the head of speech." + C_EN,
 "tr": "Sadr-ı kelâm onlarındır, tâ ki kelâmın nev'i — te'kid, teşbih, istidrak, temennî ya da tereccî — ilk anda bilinsin; أَنَّ hariç, zira o kelâmın başında bulunmaz." + C_TR},
 "tokens": [
  atf_wa("وَلَهَا", "li", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and they have».", "«ve ... onlarındır».", "لَهَا", extra_segs=[seg("لَ", "li", "prep"), pr3fs()]),
  W("صَدْرُ", "sadr", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«sadr-ı»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness", "al-kalima-wal-kalam"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«speech».", "«kelâm»."),
  li_("لِيُعْلَمَ", "alima", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "naib-al-fail"], "يُعْلَمَ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ لَامِ التَّعْلِيلِ.", "«so that … is known».", "«tâ ki ... bilinsin».", "يُعْلَمَ", segs=[seg("لِ", "lam-taleel", "part"), seg("يُعْلَمَ", "alima", "verb")]),
  W("أَوَّلًا", "awwalan", "adv", ["maful-fih"], "ظَرْفٌ مَنْصُوبٌ.", "«from the first».", "«ilk anda»."),
  W("نَوْعُهُ", "naw", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْكَلَامُ.", "«its kind».", "«nev'i».", segments=[seg("نَوْعُ", "naw", "noun"), pr3ms()]),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْيِينِ.", "«—».", "«—»."),
  W("تَوْكِيدٍ", "tawkid", "noun", ["huruf-jarr", IN], "مَجْرُورٌ — مَعْنَى إِنَّ وَأَنَّ.", "«emphasis».", "«te'kid»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«,».", "«,»."),
  W("تَشْبِيهٍ", "tashbih", "noun", ["atf-nasaq", IN], "مَعْطُوفٌ — مَعْنَى كَأَنَّ.", "«likeness».", "«teşbih»."),
  W("أَوِ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«,».", "«,»."),
  W("اسْتِدْرَاكٍ", "istidrak", "noun", ["atf-nasaq", IN], "مَعْطُوفٌ — مَعْنَى لَكِنَّ.", "«correction».", "«istidrak»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«,».", "«,»."),
  W("تَمَنٍّ", "tamanni", "noun", ["atf-nasaq", IN, "ism-maqsur-manqus"], "مَعْطُوفٌ مَجْرُورٌ — مَنْقُوصٌ؛ مَعْنَى لَيْتَ.", "«wish».", "«temennî»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("تَرَجٍّ", "tarajji", "noun", ["atf-nasaq", IN, "ism-maqsur-manqus"], "مَعْطُوفٌ مَجْرُورٌ — مَنْقُوصٌ؛ مَعْنَى لَعَلَّ.", "«hope».", "«tereccî».", punct="،"),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«hariç»."),
  ANN(ar="مُسْتَثْنًى مَنْصُوبٌ — الْحَرْفُ مَحْكِيٌّ.", en="«anna».", tr="«enne».", tags=["istithna"]),
  W("فَإِنَّهَا", "inna", "part", [IN, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«for it».", "«zira o».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3fs()]),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  W("تَقَعُ", "waqaa", "verb", [IN, "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«does stand».", "«bulunmaz»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("صَدْرِ", "sadr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«başında»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«speech».", "«kelâmın».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the مَا that stops them attaches to them, so they are held back from governing on the most eloquent usage and enter on the verb — as إِنَّمَا قَامَ زَيْدٌ." + C_EN,
 "tr": "Onlara mâ-i kâffe bitişir; bu durumda en fasih kullanışa göre amelden alıkonurlar ve fiil üzerine girerler — إِنَّمَا قَامَ زَيْدٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتَلْحَقُهَا", "lahiqa", "verb", ["fail", "maful-bihi"], "تَلْحَقُ فِعْلٌ مُضَارِعٌ، وَهَا مَفْعُولٌ بِهِ.", "«and attaches to them».", "«ve onlara bitişir».", "تَلْحَقُ", extra_segs=[seg("تَلْحَقُ", "lahiqa", "verb"), pr3fs()]),
  cited("مَا", "ma-kaffa", "part", ["fail", "anwa-ma"], "فَاعِلٌ — الْحَرْفُ مَحْكِيٌّ.", "«the mā».", "«mâ»."),
  W("الْكَافَّةُ", "ma-kaffa-adj", "noun", ["naat-sifa", "ism-fail", "anwa-ma"], "صِفَةٌ مَرْفُوعَةٌ.", "«that stops them».", "«kâffe».", punct="،"),
  W("فَتُكَفُّ", "kaffa", "verb", ["naib-al-fail", "doubled-verbs", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتُكَفُّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«so they are held back».", "«alıkonurlar».", segments=[seg("فَ", "fa", "conj"), seg("تُكَفُّ", "kaffa", "verb")]),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  W("الْعَمَلِ", "amal", "noun", ["huruf-jarr", "al-amil-wa-aqsamuh"], "مَجْرُورٌ.", "«governing».", "«amelden»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«göre»."),
  W("الْأَفْصَحِ", "afsah", "noun", ["huruf-jarr", "ism-tafdil"], "مَجْرُورٌ — اسْمُ تَفْضِيلٍ.", "«the most eloquent usage».", "«en fasih kullanışa»."),
  atf_wa("وَتَدْخُلُ", "dakhala", "verb", ["fail"], "تَدْخُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and enter».", "«ve girerler».", "تَدْخُلُ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الْفِعْلِ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the verb».", "«fiil».", punct="،"),
  nahwu(),
  cited("إِنَّمَا", "inna", "part", [K, IN, "anwa-ma", "qasr"], "إِنَّ مَكْفُوفَةٌ بِمَا عَنِ الْعَمَلِ — أَدَاةُ حَصْرٍ.", "«only».", "«ancak».", segments=[seg("إِنَّ", "inna", "part"), seg("مَا", "ma-kaffa", "part")]),
  cited("قَامَ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ — دَخَلَتْ عَلَيْهِ إِنَّمَا.", "«stood».", "«kalktı»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And إِنَّ does not change the meaning of the sentence, while أَنَّ with its sentence is in the standing of a single noun; so the kasra is required where a sentence fits, and the fatḥa where a single noun fits." + C_EN,
 "tr": "إِنَّ cümlenin mânâsını değiştirmez; أَنَّ ise cümlesiyle birlikte müfred hükmündedir; bu yüzden cümlenin uygun düştüğü yerde kesre, müfredin uygun düştüğü yerde fetha vâcibdir." + C_TR},
 "tokens": [
  INN(full="وَإِنَّ", ar="الْوَاوُ عَاطِفَةٌ، وَإِنَّ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en="«and inna».", tr="«ve inne».", segs=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part")], tags=["mubtada-khabar"]),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mez»."),
  W("تُغَيِّرُ", "ghayyara", "verb", ["mubtada-khabar", "fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«does change».", "«değiştirmez»."),
  W("مَعْنَى", "mana", "noun", ["maful-bihi", "idafa-definiteness", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the meaning of».", "«mânâsını»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«cümlenin».", punct="،"),
  ANN(full="وَأَنَّ", ar="الْوَاوُ عَاطِفَةٌ، وَأَنَّ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en="«while anna».", tr="«enne ise».", segs=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part")], tags=["mubtada-khabar"]),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile birlikte»."),
  W("جُمْلَتِهَا", "jumla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its sentence».", "«cümlesi».", segments=[seg("جُمْلَتِ", "jumla", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is in».", "«-dedir»."),
  W("حُكْمِ", "hukm", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the standing of».", "«hükmü»."),
  W("الْمُفْرَدِ", "mufrad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a single noun».", "«müfred».", punct="؛"),
  W("فَتَجِبُ", "wajaba", "verb", ["fail", "al-fa-fi-khabar-al-mubtada", "mithal-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَجِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«so is required».", "«bu yüzden ... vâcibdir».", segments=[seg("فَ", "fa", "conj"), seg("تَجِبُ", "wajaba", "verb")]),
  W("الْكَسْرَةُ", "kasra", "noun", ["fail", HM], "فَاعِلٌ مَرْفُوعٌ.", "«the kasra».", "«kesre»."),
  W("حَيْثُ", "haythu", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ.", "«where».", "«... yerde»."),
  W("تَصْلُحُ", "saluha-karuma", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«fits».", "«uygun düştüğü»."),
  W("الْجُمْلَةُ", "jumla", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a sentence».", "«cümlenin».", punct="،"),
  atf_wa("وَالْفَتْحَةُ", "fatha", "noun", ["atf-nasaq", HM], "الْفَتْحَةُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the fatḥa».", "«ve fetha».", "الْفَتْحَةُ"),
  W("حَيْثُ", "haythu", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ.", "«where».", "«... yerde»."),
  W("يَصْلُحُ", "saluha-karuma", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«fits».", "«uygun düştüğü»."),
  W("الْمُفْرَدُ", "mufrad", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a single noun».", "«müfredin».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "So it was given the kasra at the opening — as إِنَّ زَيْدًا قَائِمٌ; after a verb of saying free of opinion — as قُلْ إِنَّ اللهَ وَاحِدٌ; and after a relative — as وَآتَيْنَاهُ مِنَ الْكُنُوزِ مَا إِنَّ مَفَاتِحَهُ لَتَنُوءُ بِالْعُصْبَةِ." + C_EN,
 "tr": "Bu yüzden ibtidâ hâlinde kesre okundu — إِنَّ زَيْدًا قَائِمٌ gibi; zandan uzak kavl maddesinden sonra — قُلْ إِنَّ اللهَ وَاحِدٌ gibi; ve ism-i mevsûlden sonra — وَآتَيْنَاهُ مِنَ الْكُنُوزِ مَا إِنَّ مَفَاتِحَهُ لَتَنُوءُ بِالْعُصْبَةِ gibi." + C_TR},
 "tokens": [
  W("فَكُسِرَتْ", "kasara", "verb", ["naib-al-fail", "al-fa-fi-khabar-al-mubtada", HM], "الْفَاءُ لِلتَّفْرِيعِ، وَكُسِرَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: إِنَّ.", "«so it was given the kasra».", "«bu yüzden kesre okundu».", segments=[seg("فَ", "fa", "conj"), seg("كُسِرَ", "kasara", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("الِابْتِدَاءِ", "ibtida-start", "noun", ["huruf-jarr", HM], "مَجْرُورٌ.", "«the opening».", "«ibtidâ hâlinde».", punct="،"),
  nahwu(),
  INN(), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."), KHB("قَائِمٌ", "qaim", "«is standing».", "«ayaktadır».", punct="؛"),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("الْقَوْلِ", "qawl", "noun", ["idafa-definiteness", HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb of saying».", "«kavl maddesinden»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا — بِلَا بِمَعْنَى مِنْ غَيْرِ.", "«free of».", "«-sız».", "لَا"),
  W("ظَنٍّ", "zann", "noun", ["huruf-jarr", "zanna-wa-akhawatuha"], "مَجْرُورٌ.", "«opinion».", "«zan».", punct="،"),
  nahwu(),
  cited("قُلْ", "qala", "verb", ["fail", "hollow-verbs"], "فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«say».", "«de ki»."),
  INN(ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ — مَكْسُورَةٌ بَعْدَ الْقَوْلِ."), ISM("اللهَ", "allah", "«God».", "«Allah»."), KHB("وَاحِدٌ", "wahid", "«is One».", "«birdir».", punct="؛"),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("الْمَوْصُولِ", "mawsul", "noun", ["idafa-definiteness", "ism-mawsul", HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a relative».", "«ism-i mevsûlden».", punct="،"),
  nahwu(),
  cited("وَآتَيْنَاهُ", "aata-give", "verb", ["fail", "maful-bihi", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَآتَيْنَا فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and We gave him».", "«ve ona verdik».", segments=[seg("وَ", "wa", "conj"), seg("آتَيْ", "aata-give", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  cited("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.", "«of».", "«-den»."),
  cited("الْكُنُوزِ", "kanz", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ كَنْزٍ.", "«the treasures».", "«hazinelerden»."),
  cited("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ.", "«such that».", "«öyle ki»."),
  INN(ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ — مَكْسُورَةٌ بَعْدَ الْمَوْصُولِ؛ الْجُمْلَةُ صِلَةٌ.", en="«indeed».", tr="«muhakkak»."),
  ISM("مَفَاتِحَهُ", "maftah", "«its keys».", "«anahtarları».", pos="noun", segs=[seg("مَفَاتِحَ", "maftah", "noun"), pr3ms()], tags=["idafa-definiteness", "jam-taksir"]),
  KHB("لَتَنُوءُ", "naa-weigh", "«would weigh down».", "«ağır gelirdi».", pos="verb", ar="اللَّامُ الْمُزَحْلَقَةُ، وَتَنُوءُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", tags=["hollow-verbs"]),
  bi_("بِالْعُصْبَةِ", "usba", "noun", [], "الْعُصْبَةِ مَجْرُورٌ.", "«a band of men».", "«güçlü bir topluluğa».", "الْعُصْبَةِ", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And it was given the fatḥa where it is a doer — as بَلَغَنِي أَنَّكَ قَائِمٌ, that is, قِيَامُكَ; or an object — as عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ, that is, قِيَامَ زَيْدٍ; or a delayed mubtada — as عِنْدِي أَنَّكَ قَائِمٌ, that is, قِيَامُكَ; or a muḍāf ilayh — as اجْلِسْ حَيْثُ أَنَّ زَيْدًا جَالِسٌ, that is, مَكَانَ جُلُوسِ زَيْدٍ." + C_EN,
 "tr": "Fâil olduğu yerde fetha okundu — بَلَغَنِي أَنَّكَ قَائِمٌ gibi, yani قِيَامُكَ; ya da mef'ûl — عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ gibi, yani قِيَامَ زَيْدٍ; ya da muahhar mübtedâ — عِنْدِي أَنَّكَ قَائِمٌ gibi, yani قِيَامُكَ; ya da muzâfun ileyh — اجْلِسْ حَيْثُ أَنَّ زَيْدًا جَالِسٌ gibi, yani مَكَانَ جُلُوسِ زَيْدٍ." + C_TR},
 "tokens": [
  atf_wa("وَفُتِحَتْ", "fataha", "verb", ["naib-al-fail", HM], "فُتِحَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and it was given the fatḥa».", "«ve fetha okundu».", "فُتِحَتْ", extra_segs=[seg("فُتِحَ", "fataha", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("حَيْثُ", "haythu", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ.", "«where».", "«... yerde»."),
  W("هِيَ", "hiya", "pron", ["mubtada-khabar"], "مُبْتَدَأٌ — الْمَصْدَرُ الْمُؤَوَّلُ.", "«it».", "«o»."),
  W("فَاعِلٌ", "fail-doer", "noun", ["mubtada-khabar", "fail"], "خَبَرٌ مَرْفُوعٌ.", "«is a doer».", "«fâil olduğu».", punct="،"),
  nahwu(),
  cited("بَلَغَنِي", "balagha", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«it reached me».", "«bana ulaştı».", segments=[seg("بَلَغَ", "balagha", "verb"), pr1s()]),
  ANN(full="أَنَّكَ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ بَلَغَ.", en="«that you».", tr="«senin».", segs=[seg("أَنَّ", "anna", "part"), pr2ms()]),
  KHB("قَائِمٌ", "qaim", "«are standing».", "«ayakta olduğun».", punct="،"),
  AYQ(),
  cited("قِيَامُكَ", "qiyam", "noun", ["fail", "idafa-definiteness", "hadhf-wa-taqdir"], "فَاعِلٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — التَّأْوِيلُ.", "«your standing».", "«ayakta durman».", punct="؛", segments=[seg("قِيَامُ", "qiyam", "noun"), pr2ms()]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَفْعُولٌ", "maful-object", "noun", ["atf-nasaq", "maful-bihi"], "مَعْطُوفٌ عَلَى فَاعِلٌ مَرْفُوعٌ.", "«an object».", "«mef'ûl».", punct="،"),
  nahwu(),
  cited("عَلِمْتُ", "alima", "verb", ["fail", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I knew».", "«bildim».", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
  ANN(ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَلِمَ."), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd'in»."), KHB("قَائِمٌ", "qaim", "«is standing».", "«ayakta olduğunu».", punct="،"),
  AYQ(),
  cited("قِيَامَ", "qiyam", "noun", ["maful-bihi", "idafa-definiteness", "hadhf-wa-taqdir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ — التَّأْوِيلُ.", "«the standing of».", "«... ayakta durmasını»."),
  cited("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'in».", punct="؛"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُبْتَدَأٌ", "mubtada", "noun", ["atf-nasaq", "mubtada-khabar"], "مَعْطُوفٌ مَرْفُوعٌ.", "«a mubtada».", "«mübtedâ»."),
  W("مُؤَخَّرٌ", "muakhkhar", "noun", ["naat-sifa", "taqdim-al-musnad"], "صِفَةٌ مَرْفُوعَةٌ.", "«delayed».", "«muahhar».", punct="،"),
  nahwu(),
  cited("عِنْدِي", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«with me is».", "«bence».", segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  ANN(full="أَنَّكَ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ مُؤَخَّرٌ.", en="«that you».", tr="«senin».", segs=[seg("أَنَّ", "anna", "part"), pr2ms()]),
  KHB("قَائِمٌ", "qaim", "«are standing».", "«ayakta olduğun».", punct="،"),
  AYQ(),
  cited("قِيَامُكَ", "qiyam", "noun", ["mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — التَّأْوِيلُ.", "«your standing».", "«ayakta durman».", punct="؛", segments=[seg("قِيَامُ", "qiyam", "noun"), pr2ms()]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُضَافٌ", "mudaf", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ.", "«a muḍāf».", "«muzâfun»."),
  W("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«ilayh».", "«ileyh».", punct="،", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  nahwu(),
  cited("اجْلِسْ", "jalasa", "verb", ["fail"], "فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«sit».", "«otur»."),
  cited("حَيْثُ", "haythu", "noun", ["maful-fih", "idafa-definiteness", "al-mabni-wal-mudmar"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَهُوَ مُضَافٌ.", "«where».", "«... yerde»."),
  ANN(ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُضَافٌ إِلَيْهِ.", tags=["idafa-definiteness"]), ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd'in»."), KHB("جَالِسٌ", "jalis-sitting", "«is sitting».", "«oturduğu».", punct="،"),
  AYQ(),
  cited("مَكَانَ", "makan", "noun", ["maful-fih", "idafa-definiteness", "hadhf-wa-taqdir"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — التَّأْوِيلُ.", "«the place of».", "«yerinde»."),
  cited("جُلُوسِ", "julus", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the sitting of».", "«oturduğu»."),
  cited("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'in».", punct="."),
 ]})

S.append({"id": "s8", "translation": {
 "en": "And it was given the fatḥa after لَوْلَا, because what follows it is a mubtada — as لَوْلَا أَنَّكَ; and after لَوْ, because what follows it is a doer — as لَوْ أَنَّكَ." + C_EN,
 "tr": "لَوْلَا'dan sonra fetha okundu, çünkü mâba'di mübtedâdır — لَوْلَا أَنَّكَ gibi; لَوْ'den sonra da, çünkü mâba'di fâildir — لَوْ أَنَّكَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَفُتِحَتْ", "fataha", "verb", ["naib-al-fail", HM], "فُتِحَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and it was given the fatḥa».", "«ve fetha okundu».", "فُتِحَتْ", extra_segs=[seg("فُتِحَ", "fataha", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-dan sonra»."),
  cited("لَوْلَا", "lawla", "part", ["idafa-definiteness", "hadhf-wa-taqdir"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«lawlā».", "«levlâ»."),
  W("لِأَنَّ", "lianna", "part", [IN, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("مَا", "ma-mawsula", "pron", [IN, "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«what».", "«... olan»."),
  W("بَعْدَهَا", "bada", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — صِلَةٌ.", "«follows it».", "«mâba'di».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("مُبْتَدَأٌ", "mubtada", "noun", [IN, "mubtada-khabar"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is a mubtada».", "«mübtedâdır».", punct="،"),
  nahwu(),
  cited("لَوْلَا", "lawla", "part", [K, "hadhf-wa-taqdir"], "حَرْفُ امْتِنَاعٍ لِوُجُودٍ.", "«had it not been that».", "«... olmasaydı»."),
  ANN(full="أَنَّكَ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — وَالْمَصْدَرُ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ وُجُوبًا.", en="«you».", tr="«sen».", segs=[seg("أَنَّ", "anna", "part"), pr2ms()], punct="؛"),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«and after».", "«ve ... -den sonra».", "بَعْدَ"),
  cited("لَوْ", "law", "part", ["idafa-definiteness", "al-majzum-wal-shart-wal-jaza"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«law».", "«lev»."),
  W("لِأَنَّ", "lianna", "part", [IN, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("مَا", "ma-mawsula", "pron", [IN, "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«what».", "«... olan»."),
  W("بَعْدَهَا", "bada", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — صِلَةٌ.", "«follows it».", "«mâba'di».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("فَاعِلٌ", "fail-doer", "noun", [IN, "fail"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is a doer».", "«fâildir».", punct="،"),
  nahwu(),
  cited("لَوْ", "law", "part", [K, "al-majzum-wal-shart-wal-jaza"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«if».", "«... olsaydı»."),
  ANN(full="أَنَّكَ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — وَالْمَصْدَرُ فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ: ثَبَتَ.", en="«you».", tr="«sen».", segs=[seg("أَنَّ", "anna", "part"), pr2ms()], punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And where both readings are allowed, both are allowed — the kasra and the fatḥa: in مَنْ يُكْرِمْنِي فَإِنِّي أُكْرِمُهُ, after the fāʾ of the answer, the kasra is required if فَأَنَا أُكْرِمُهُ is meant, and the fatḥa if فَجَزَاؤُهُ أَنِّي أُكْرِمُهُ is meant." + C_EN,
 "tr": "İki takdirin câiz olduğu yerde iki iş — kesre ve fetha — câizdir: مَنْ يُكْرِمْنِي فَإِنِّي أُكْرِمُهُ'de, cezâ fâsından sonra, فَأَنَا أُكْرِمُهُ kastedilirse kesre, فَجَزَاؤُهُ أَنِّي أُكْرِمُهُ kastedilirse fetha vâcib olur." + C_TR},
 "tokens": [
  atf_wa("وَحَيْثُ", "haythu", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "حَيْثُ ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and where».", "«ve ... yerde».", "حَيْثُ"),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«are allowed».", "«câiz olduğu»."),
  W("التَّقْدِيرَانِ", "taqdir", "noun", ["fail", "al-muthanna", "hadhf-wa-taqdir"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ — الْمُفْرَدُ وَالْجُمْلَةُ.", "«both readings».", "«iki takdirin»."),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — جَوَابُ حَيْثُ.", "«are allowed».", "«câizdir»."),
  W("الْأَمْرَانِ", "amr", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ.", "«both».", "«iki iş»."),
  W("الْكَسْرَةُ", "kasra", "noun", ["badal", HM], "بَدَلٌ مِنَ الْأَمْرَانِ مَرْفُوعٌ.", "«the kasra».", "«kesre»."),
  atf_wa("وَالْفَتْحَةُ", "fatha", "noun", ["atf-nasaq", HM], "الْفَتْحَةُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the fatḥa».", "«ve fetha».", "الْفَتْحَةُ", punct=":"),
  W("فَفِي", "fi", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«in».", "«-de».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  cited("مَنْ", "man", "pron", ["huruf-jarr", "al-majzum-wal-shart-wal-jaza", "mubtada-khabar"], "الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — مَنْ شَرْطِيَّةٌ مُبْتَدَأٌ.", "«whoever».", "«kim»."),
  cited("يُكْرِمْنِي", "akrama", "verb", ["al-majzum-wal-shart-wal-jaza", "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«honours me».", "«bana ikram ederse».", segments=[seg("يُكْرِمْ", "akrama", "verb"), pr1s()]),
  INN(full="فَإِنِّي", ar="الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا — تُكْسَرُ أَوْ تُفْتَحُ.", en="«then I».", tr="«ben de».", segs=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")], tags=["al-fa-fi-jawab-al-shart"]),
  KHB("أُكْرِمُهُ", "akrama", "«honour him».", "«ona ikram ederim».", pos="verb", ar="فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", punct="،", tags=["form-iv-verbs"]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-dan sonra»."),
  W("فَاءِ", "fa-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the fāʾ of».", "«fâsı»."),
  W("الْجَزَاءِ", "jaza-answer", "noun", ["idafa-definiteness", "al-fa-fi-jawab-al-shart"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the answer».", "«cezâ».", punct="،"),
  W("تَجِبُ", "wajaba", "verb", ["fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is required».", "«vâcib olur»."),
  W("الْكَسْرَةُ", "kasra", "noun", ["fail", HM], "فَاعِلٌ مَرْفُوعٌ.", "«the kasra».", "«kesre»."),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-se»."),
  W("أُرِيدَ", "arada", "verb", ["in-shartiyya", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ.", "«is meant».", "«kastedilirse»."),
  cited("فَأَنَا", "ana", "pron", ["naib-al-fail", "mubtada-khabar", "al-mabni-wal-mudmar"], "الْفَاءُ رَابِطَةٌ، وَأَنَا مُبْتَدَأٌ — الْجُمْلَةُ الْمَحْكِيَّةُ نَائِبُ فَاعِلٍ.", "«then I».", "«ben de».", segments=[seg("فَ", "fa", "conj"), seg("أَنَا", "ana", "pron")]),
  cited("أُكْرِمُهُ", "akrama", "verb", ["mubtada-khabar", "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرٌ.", "«honour him».", "«ona ikram ederim».", punct="،", segments=[seg("أُكْرِمُ", "akrama", "verb"), pr3ms()]),
  atf_wa("وَتَجِبُ", "wajaba", "verb", ["fail", "mithal-verbs"], "تَجِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is required».", "«ve ... vâcib olur».", "تَجِبُ"),
  W("الْفَتْحَةُ", "fatha", "noun", ["fail", HM], "فَاعِلٌ مَرْفُوعٌ.", "«the fatḥa».", "«fetha»."),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-se»."),
  W("أُرِيدَ", "arada", "verb", ["in-shartiyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ.", "«is meant».", "«kastedilirse»."),
  cited("فَجَزَاؤُهُ", "jaza-answer", "noun", ["naib-al-fail", "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ رَابِطَةٌ، وَجَزَاؤُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«then his reward».", "«onun cezâsı».", segments=[seg("فَ", "fa", "conj"), seg("جَزَاؤُ", "jaza-answer", "noun"), pr3ms()]),
  ANN(full="أَنِّي", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْمُبْتَدَإِ.", en="«that I».", tr="«benim».", segs=[seg("أَنَّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  KHB("أُكْرِمُهُ", "akrama", "«honour him».", "«ona ikram etmemdir».", pos="verb", ar="فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرُ أَنَّ.", punct="."),
 ]})

S.append({"id": "s10", "translation": {
 "en": "And in كُنْتُ أُرَى زَيْدًا كَمَا قِيلَ سَيِّدًا • إِذَا إِنَّهُ عَبْدُ الْقَفَا وَاللَّهَازِمِ, after إِذَا of surprise, the kasra is allowed by reading a sentence, and the fatḥa by reading a mubtada whose khabar is dropped." + C_EN,
 "tr": "كُنْتُ أُرَى زَيْدًا كَمَا قِيلَ سَيِّدًا • إِذَا إِنَّهُ عَبْدُ الْقَفَا وَاللَّهَازِمِ'de, mufâcee إِذَا'sından sonra, cümle takdiriyle kesre, haberi mahzûf bir mübtedâ takdiriyle fetha câizdir." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  cited("كُنْتُ", "kana", "verb", ["huruf-jarr", "kana-wa-akhawatuha", "hollow-verbs"], "الْبَيْتُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهَا.", "«I used to».", "«... idim».", segments=[seg("كُنْ", "kana", "verb"), prT()]),
  cited("أُرَى", "raa", "verb", ["kana-wa-akhawatuha", "naib-al-fail", "zanna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: أَنَا — بِمَعْنَى أَظُنُّ؛ وَالْجُمْلَةُ خَبَرُ كَانَ.", "«think».", "«sanırdım»."),
  cited("زَيْدًا", "zayd", "propn", ["mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«Zayd».", "«Zeyd'i»."),
  ka_("كَمَا", "ma-masdariyya", "part", ["anwa-ma", "an-masdariyya"], "مَا مَصْدَرِيَّةٌ — كَالْمَقُولِ.", "«as».", "«denildiği gibi».", "مَا"),
  cited("قِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«was said».", "«denildiği»."),
  cited("سَيِّدًا", "sayyid", "noun", ["mafulayn"], "مَفْعُولٌ ثَالِثٌ مَنْصُوبٌ.", "«a master».", "«efendi».", punct="•"),
  cited("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا لِلْمُفَاجَأَةِ.", "«when lo».", "«meğer»."),
  INN(full="إِنَّهُ", ar="حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — تُكْسَرُ بِتَقْدِيرِ الْجُمْلَةِ وَتُفْتَحُ بِتَقْدِيرِ الْمُفْرَدِ.", en="«he».", tr="«o».", segs=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  KHB("عَبْدُ", "abd", "«is a slave of».", "«kulu».", ar="خَبَرُ إِنَّ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", tags=["idafa-definiteness"]),
  cited("الْقَفَا", "qafa", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the nape».", "«ensesinin»."),
  cited_wa("وَاللَّهَازِمِ", "lahazim", "noun", ["atf-nasaq", "jam-taksir", "mamnu-min-sarf"], "اللَّهَازِمِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ لِأَجْلِ اللَّامِ — جَمْعُ لِهْزِمَةٍ.", "«and the jaws».", "«ve çenelerinin».", "اللَّهَازِمِ", punct="،"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-dan sonra»."),
  cited("إِذَا", "idha", "part", ["idafa-definiteness", "idha-shartiyya"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«idhā».", "«izâ»."),
  W("الْمُفَاجَأَةِ", "mufajaa", "noun", ["idafa-definiteness", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ فَاجَأَ.", "«of surprise».", "«mufâcee».", punct="،"),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is allowed».", "«câizdir»."),
  W("الْكَسْرُ", "kasr", "noun", ["fail", HM], "فَاعِلٌ مَرْفُوعٌ.", "«the kasra».", "«kesre»."),
  bi_("بِتَقْدِيرِ", "taqdir", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"], "تَقْدِيرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by reading».", "«... takdiriyle».", "تَقْدِيرِ"),
  W("الْجُمْلَةِ", "jumla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a sentence».", "«cümle».", punct="،"),
  atf_wa("وَالْفَتْحُ", "fath", "noun", ["atf-nasaq", HM], "الْفَتْحُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the fatḥa».", "«ve fetha».", "الْفَتْحُ"),
  bi_("بِتَقْدِيرِ", "taqdir", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"], "تَقْدِيرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by reading».", "«... takdiriyle».", "تَقْدِيرِ"),
  W("مُبْتَدَإٍ", "mubtada", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a mubtada».", "«bir mübtedâ»."),
  W("مَحْذُوفِ", "mahdhuf", "noun", ["naat-sifa", "hadhf-wa-taqdir", "idafa-definiteness"], "صِفَةٌ مَجْرُورَةٌ، وَهُوَ مُضَافٌ — إِضَافَةٌ لَفْظِيَّةٌ.", "«whose … is dropped».", "«... mahzûf»."),
  W("الْخَبَرِ", "khabar", "noun", ["idafa-definiteness", "mubtada-khabar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«khabar».", "«haberi».", punct="."),
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
 "lahazim": need("lahazim", "لِهْزِمَة", "ل ه ز م", "noun", "the jaw-corner, the jowl; plural لَهَازِم — the «slave of the nape and the jowls» is a glutton", "çene köşesi, gerdan; cem'i لَهَازِم — «ense ve gerdan kulu» obur demektir", 5),
 "saluha-karuma": need("saluha-karuma", "صَلُحَ", "ص ل ح", "verb", "to be fit, to suit, to be sound (bāb karuma)", "uygun olmak, yakışmak, sâlih olmak (kerume bâbı)", 3),
 "aata-give": need("aata-give", "آتَى", "أ ت ي", "verb", "to give, to bring (Form IV of أَتَى; defective and hamzated)", "vermek, getirmek (etâ'nın if'âli; nâkıs ve mehmûz)", 3),
 "kasr": need("kasr", "كَسْر", "ك س ر", "noun", "reading with a kasra — the maṣdar of كَسَرَ", "kesre ile okuma — kesera'nın masdarı", 3),
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
put_morph(mo, "saluha-karuma", _nfc(_sg.sound1("karuma", "صَلُح", "صْلُح", "اُصْلُح", "صَلَاح", "صَالِح", None, None, None, "صَلُحَ الشَّيْءُ: كَانَ صَالِحًا، وَصَلُحَ لِكَذَا: نَاسَبَهُ — بَابُ كَرُمَ، لَازِمٌ.")))
put_morph(mo, "aata-give", _nfc(_sg.derived_naqis(_sg.B4 + " — نَاقِصٌ مَهْمُوزُ الْفَاءِ", _sg.W4, "ُ", "آتَ", "ؤْت", "i", "آت", "إِيتَاء", "مُؤْتٍ", "مُؤْتًى", "أُوتِيَ", "يُؤْتَى", "آتَاهُ الشَّيْءَ: أَعْطَاهُ إِيَّاهُ — بَابُ الْإِفْعَالِ؛ مَهْمُوزُ الْفَاءِ نَاقِصٌ: آتَى يُؤْتِي.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch34 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْحُرُوفُ الْمُشَبَّهَةُ بِالْفِعْلِ فِي الْكَافِيَةِ: إِنَّ وَأَنَّ", "en": "The verb-like particles in the Kafiya: the six, why «verb-like», the head of speech, the mā that disarms them, and the hamza of inna — kasra where a sentence fits, fatḥa where a noun fits, both where both fit", "tr": "Kâfiye'de fiile benzeyen harfler: altısı, neden «fiile benzer», sadr-ı kelâm, onları silahsızlandıran mâ ve inne'nin hemzesi — cümlenin uyduğu yerde kesre, ismin uyduğu yerde fetha, ikisinin uyduğu yerde ikisi"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الحروف المشبهة بالفعل: إن وأن وكأن ولكن وليت ولعل؛ لها صدر الكلام إلا أن؛ تلحقها ما الكافة؛ إن لا تغير معنى الجملة وأن مع جملتها في حكم المفرد", "ضياء صونغور اوغلى — دفتر الكافية: وجه التسمية؛ مواضع الكسر والفتح والوجهين؛ آية الكنوز؛ لولا أنك ولو أنك؛ من يكرمني فإني أكرمه؛ بيت عبد القفا واللهازم"],
 "question": {
  "en": ["Why are these six «like the verb»? They look like one — three to five letters, ending in a fatḥa as a māḍī does — and each carries a verb's meaning: أَكَّدْتُ, شَبَّهْتُ, اسْتَدْرَكْتُ, تَمَنَّيْتُ, تَرَجَّيْتُ. That is why they govern as a verb governs: ism in naṣb, khabar in rafʿ.",
         "Why must they open the sentence? So the hearer knows at once which kind of speech is coming — emphasis, likeness, correction, wish, hope. أَنَّ is the exception because it never opens: it turns its clause into a noun that some other word must hold.",
         "What does مَا do to them? Attached, it stops their government and lets them enter on a verb: إِنَّمَا قَامَ زَيْدٌ. The MaEngine reads the fused spelling as kāffa, and the qaṣr note takes it from there.",
         "How do I choose between إِنَّ and أَنَّ? One test: إِنَّ leaves the sentence a sentence; أَنَّ makes it a single noun. So read kasra wherever a sentence can stand — the opening, after «say» with no opinion, after a relative — and fatḥa wherever a noun is wanted: as doer (بَلَغَنِي أَنَّكَ = قِيَامُكَ), object (عَلِمْتُ أَنَّ = قِيَامَ زَيْدٍ), delayed mubtada (عِنْدِي أَنَّكَ), muḍāf ilayh (حَيْثُ أَنَّ), after لَوْلَا and لَوْ.",
         "When are both right? When both readings are: after the fāʾ of a conditional answer (فَإِنِّي أُكْرِمُهُ = «then I honour him» / «then his reward is my honouring him») and after إِذَا of surprise, where the verse of the slave of the nape may be read either way. The engine keeps both faces and says which reading each implies.",
         "What does the engine do? The kernel's INNA table pushes [ism-naṣb, khabar-rafʿ] at each of the six; the inna-am-anna note and the Hamza game drill the kasra/fatḥa rule; the Qawāʿid's «after a verb of saying» exception lives in the analyzer's walk back to the nearest verb."],
  "tr": ["Bu altısı neden «fiile benzer»? Fiile benzerler — üç ila beş harf, mâzî gibi fetha ile biten — ve her biri bir fiil mânâsı taşır: أَكَّدْتُ, شَبَّهْتُ, اسْتَدْرَكْتُ, تَمَنَّيْتُ, تَرَجَّيْتُ. Fiilin yönettiği gibi yönetmeleri bundandır: isim nasbda, haber ref'te.",
         "Neden cümleyi açmalıdırlar? Dinleyen hangi tür kelâmın geldiğini hemen bilsin diye — te'kid, teşbih, istidrak, temennî, tereccî. أَنَّ istisnadır çünkü hiç açmaz: cümlesini başka bir kelimenin tutması gereken bir isme çevirir.",
         "مَا onlara ne yapar? Bitişince amellerini durdurur ve fiil üzerine girmelerine izin verir: إِنَّمَا قَامَ زَيْدٌ. MaEngine bitişik yazımı kâffe okur, kasr notu oradan devralır.",
         "إِنَّ ile أَنَّ arasında nasıl seçerim? Tek test: إِنَّ cümleyi cümle bırakır; أَنَّ onu tek bir isim yapar. Öyleyse cümlenin durabildiği her yerde kesre oku — ibtidâ, zansız «de» fiilinden sonra, ism-i mevsûlden sonra — isim istenen her yerde fetha: fâil (بَلَغَنِي أَنَّكَ = قِيَامُكَ), mef'ûl (عَلِمْتُ أَنَّ = قِيَامَ زَيْدٍ), muahhar mübtedâ (عِنْدِي أَنَّكَ), muzâfun ileyh (حَيْثُ أَنَّ), لَوْلَا ve لَوْ'den sonra.",
         "İkisi ne zaman doğrudur? İki okuyuş da doğruyken: şart cevabının fâsından sonra (فَإِنِّي أُكْرِمُهُ = «ben de ona ikram ederim» / «cezâsı ona ikram etmemdir») ve mufâcee إِذَا'sından sonra; ense kulu beyti iki türlü de okunabilir. Motor iki yüzü de tutar ve her okuyuşun neyi ima ettiğini söyler.",
         "Motor ne yapar? Çekirdeğin INNA tablosu altısının her birinde [isim-nasb, haber-ref'] iter; inna-am-anna notu ve Hemze oyunu kesre/fetha kuralını çalıştırır; Kavâid'in «kavl fiilinden sonra» istisnası analizörün en yakın fiile geri yürüyüşünde yaşar."]},
 "plain": {
  "en": "Six little words — inna, anna, ka-anna, lākinna, layta, laʿalla — behave like verbs: a subject in naṣb, a predicate in rafʿ, and first place. The hard pair is inna/anna: inna keeps a sentence a sentence («indeed Zayd stands»), anna folds it into a noun («that Zayd stands»), and the vowel on the hamza tells you which.",
  "tr": "Altı küçük kelime — inne, enne, keenne, lâkinne, leyte, lealle — fiil gibi davranır: nasbda özne, ref'te yüklem, ve önce gelirler. Çetin çift inne/enne: inne cümleyi cümle bırakır («muhakkak Zeyd ayaktadır»), enne onu isme katlar («Zeyd'in ayakta olduğu»); hangisi olduğunu hemzedeki hareke söyler."},
 "explanation": {
  "en": "The Kafiya's list is verbatim, and the notebook's first gloss is the etymology of the name — shape and meaning both verb-like — which is also the reason for their government. Two general rules follow: the head of speech, with أَنَّ excepted and the reason given, and the kāffa مَا, which the notebook ties to the «most eloquent» usage because a minority let إِنَّمَا keep governing. The chapter's centre is the hamza of إِنَّ, and the notebook teaches it as a single principle before it lists cases: إِنَّ preserves the sentence, أَنَّ reduces it to a noun, so the vowel follows what the position wants. Three kasra positions and six fatḥa positions are each given with a sentence and, for the fatḥa, with the paraphrase that proves the noun reading (قِيَامُكَ, قِيَامَ زَيْدٍ, مَكَانَ جُلُوسِ زَيْدٍ); لَوْلَا and لَوْ are explained by what follows them, a mubtada and a doer. The two-way positions close the chapter — the fāʾ of the answer, where the speaker's intention decides, and إِذَا of surprise, where the verse is read both ways. The aya 28:76 is cited in its received وَآتَيْنَاهُ where the notebook writes وَأَتَيْنَاهُ; the manifest records it.",
  "tr": "Kâfiye'nin listesi aynendir ve defterin ilk şerhi adın etimolojisidir — şekil ve mânâ, ikisi de fiile benzer — ki bu amellerinin de sebebidir. İki genel kural izler: sebebi verilerek أَنَّ istisna edilen sadr-ı kelâm ve defterin «en fasih» kullanışa bağladığı mâ-i kâffe, çünkü bir azınlık إِنَّمَا'nın amel etmesine izin verir. Bâbın merkezi إِنَّ'nin hemzesidir ve defter onu hâlleri saymadan önce tek bir ilke olarak öğretir: إِنَّ cümleyi korur, أَنَّ onu isme indirger; dolayısıyla hareke mevkinin istediğini izler. Üç kesre mevkii ve altı fetha mevkii birer cümleyle, fetha için ayrıca isim okuyuşunu kanıtlayan takdirle verilir (قِيَامُكَ, قِيَامَ زَيْدٍ, مَكَانَ جُلُوسِ زَيْدٍ); لَوْلَا ve لَوْ ardlarından gelenle, mübtedâ ve fâille açıklanır. İki yönlü mevkiler bâbı kapar — konuşanın niyetinin belirlediği cevap fâsı ve beytin iki türlü okunduğu mufâcee إِذَا'sı. 28:76 âyeti defterin وَأَتَيْنَاهُ yazdığı yerde alınan وَآتَيْنَاهُ ile zikredilir; manifest bunu kaydeder."},
 "examples": [
  {"ar": "إِنَّ وَأَنَّ وَكَأَنَّ وَلَكِنَّ وَلَيْتَ وَلَعَلَّ", "en": "The six.", "tr": "Altısı.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "إِنَّمَا قَامَ زَيْدٌ", "en": "Disarmed by mā.", "tr": "Mâ ile silahsızlanmış.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "قُلْ إِنَّ اللهَ وَاحِدٌ — مَا إِنَّ مَفَاتِحَهُ لَتَنُوءُ بِالْعُصْبَةِ", "en": "Kasra after saying and after a relative.", "tr": "Kavlden ve mevsûlden sonra kesre.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "بَلَغَنِي أَنَّكَ قَائِمٌ — عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ — اجْلِسْ حَيْثُ أَنَّ زَيْدًا جَالِسٌ", "en": "Fatḥa as doer, object and muḍāf ilayh.", "tr": "Fâil, mef'ûl ve muzâfun ileyh olarak fetha.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "مَنْ يُكْرِمْنِي فَإِنِّي أُكْرِمُهُ", "en": "Both readings after the fāʾ of the answer.", "tr": "Cevap fâsından sonra iki okuyuş.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "إِذَا إِنَّهُ عَبْدُ الْقَفَا وَاللَّهَازِمِ", "en": "Both readings after idhā of surprise.", "tr": "Mufâcee izâ'sından sonra iki okuyuş.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«أَنَّ زَيْدًا قَائِمٌ» (cümle başında)",
   "right": "«إِنَّ زَيْدًا قَائِمٌ — enne sadr-ı kelâmda bulunmaz»",
   "why": {"en": "Anna needs a word before it to hold the noun it makes.", "tr": "Enne, yaptığı ismi tutacak önceki bir kelime ister."}},
  {"wrong": "«عَلِمْتُ إِنَّ زَيْدًا قَائِمٌ»",
   "right": "«عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ — mef'ûl mevkiinde fetha»",
   "why": {"en": "Where a single noun is wanted, the hamza takes the fatḥa.", "tr": "Müfred istenen yerde hemze fetha alır."}},
  {"wrong": "«قُلْ أَنَّ اللهَ وَاحِدٌ»",
   "right": "«قُلْ إِنَّ اللهَ وَاحِدٌ — zansız kavlden sonra kesre»",
   "why": {"en": "Speech is quoted whole; the sentence stays a sentence.", "tr": "Söz bütün olarak nakledilir; cümle cümle kalır."}},
  {"wrong": "«إِنَّمَا زَيْدًا قَائِمٌ»",
   "right": "«إِنَّمَا زَيْدٌ قَائِمٌ — kâffe mâ ameli durdurur»",
   "why": {"en": "On the most eloquent usage inna-mā governs nothing.", "tr": "En fasih kullanışa göre innemâ hiçbir şeyi yönetmez."}}],
 "relatedNotes": ["inna-wa-akhawatuha", "inna-am-anna", "an-masdariyya", "anwa-ma", "qasr", "al-afal-al-naqisa-fil-kafiya"]}

ADD_EN = (" Chapter 34 (notebook lines ~338-339): the verb-like particles listed in the notebook's own Arabic (s1); the name, the head of speech, the kāffa mā, and the hamza of inna in its kasra, fatḥa and two-way positions (28:76; the verse of the slave of the nape) — the notebook's exposition, kept as commentary (s2-s10). Qurʾānic text as the source prints it. "
          "DIVERGENCE: the notebook writes وَأَتَيْنَاهُ; the chapter cites the received وَآتَيْنَاهُ.")
ADD_TR = (" Otuz dördüncü bâb (defter satırları ~338-339): fiile benzeyen harfler defterin kendi Arapçasıyla sayılır (s1); ad, sadr-ı kelâm, mâ-i kâffe ve inne'nin hemzesi kesre, fetha ve iki yönlü mevkileriyle (28:76; ense kulu beyti) — defterin açıklaması, şerh olarak (s2-s10). Kur'ân metni kaynağın bastığı gibi. "
          "FARK: defter وَأَتَيْنَاهُ yazar; bâb alınan وَآتَيْنَاهُ'yu zikreder.")
write_out(34, S, TITLE, ADD_EN, ADD_TR, "338-339", GLOSS_ADD, notes=(NOTE,),
          related=(("inna-wa-akhawatuha", [K]), ("inna-am-anna", [K])))
report(34, S, GLOSS_ADD, (NOTE,))
