# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 65: HUSN AL-TA'LIL (a fine, non-real cause claimed for a quality: the quality fixed with no
customary cause / with another cause; the quality unfixed, possible / impossible; what is built on doubt, joined to it) and
TAFRI' (a ruling proved for one dependent of a thing after another). Source lines ~4250-4300 (sahifa 146-147).

  RESTORED (the source carries the step only in Turkish): s1, s2 (the definition and the four kinds), s3, s5, s7, s9, s11 (the
  kinds' headings), s13 (tafri's definition); the citation frame of s10 (the source says only that the author translated the
  bayt from Persian). The bayts (s4, s6, s8, s10, s12, s14) are the source's printed Arabic — with two readings restored to
  the received text and recorded in the attribution: الرُّحَضَاءُ (the print's الرُّخَصَاءُ) and كَأَنَّ السَّحَابَ (the print's
  كَأَنَّمَا with the accusative marks it prints).

  python3 tools/authoring/author_talkhis_ch65.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

H = "husn-al-talil"; F = "tafri"
TITLE = {"ar": "حُسْنُ التَّعْلِيلِ، وَالتَّفْرِيعُ", "en": "Husn al-taʿlil; Tafriʿ", "tr": "Hüsn-i Ta'lîl; Tefrî'"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them is» — the fronted khabar.", "«ve onlardan biri» — öne alınmış haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def wahuwa(tag):
    return tok("وَهُوَ","huwa","pron",[tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")])
def an_masd(tag):
    return tok("أَنْ","an-masdariyya","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the clause is the khabar.", "«-mak» — masdar yapan en; cümle haberdir.")
def kaqawl(tag, punct=None):
    return tok("كَقَوْلِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")], punct=punct)
def kaqh(tag):
    return tok("كَقَوْلِهِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«as in his saying».", "«onun sözü gibi».",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")], punct=":")
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def abi(tag, name, name_lex, name_ar, name_en, name_tr, punct=":"):
    return [tok("أَبِي","ab","noun",[tag, "five-nouns", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — one of the five nouns, majrur by its ya.", "«Ebû» — beş isimden, yâ ile mecrûr."),
            tok(name, name_lex, "noun", [tag, "idafa-definiteness"], name_ar, name_en, name_tr, punct=punct)]
def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)

# ----------- s1 — the definition (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is HUSN AL-TAʿLIL: that a cause be claimed for a quality — a cause that suits it by a FINE consideration which is not the real one." + R_EN,
 "tr": "Onlardan biri HÜSN-İ TA'LÎLDİR: bir vasıf için, hakikî olmayan LATÎF bir itibarla ona münasip bir illet iddia edilmesi." + R_TR},
 "tokens": [
  minha(H),
  tok("حُسْنُ","husn","noun",[H, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ.", "«the fineness of» — the delayed mubtada, annexed.", "«güzelliği» — sona bırakılmış mübtedâ, muzâf."),
  tok("التَّعْلِيلِ","talil","noun",[H, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ عَلَّلَ: ذِكْرُ الْعِلَّةِ.", "«giving a cause» — the masdar of ʿallala.", "«illet gösterme» — allele'nin masdarı.", punct="،"),
  wahuwa(H),
  an_masd(H),
  tok("يُدَّعَى","iddaa","verb",[H, "an-masdariyya", "naib-al-fail", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«it is claimed» — a passive; nasb hidden on the alif.", "«iddia edilir» — meçhul; nasb elifte gizli."),
  tok("لِوَصْفٍ","wasf","noun",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for a quality».", "«bir vasıf için».", segments=[seg("لِ","li","part"), seg("وَصْفٍ","wasf","noun")]),
  tok("عِلَّةٌ","illa","noun",[H, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a cause» — the naib al-fail.", "«bir illet» — nâib-i fâil."),
  tok("مُنَاسِبَةٌ","munasib","noun",[H, "naat-sifa", "ism-fail", "form-iii-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلِ نَاسَبَ.", "«suiting» — a na't; the ism fa'il of nasaba.", "«münasip» — na't; nâsebe'nin ism-i fâili."),
  tok("لَهُ","lahu","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمُنَاسِبَةٌ.", "«to it».", "«ona».", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("بِاعْتِبَارٍ","itibar","noun",[H, "huruf-jarr", "masdar", "form-viii-verbs"], "جَارٌّ وَمَجْرُورٌ — مَصْدَرُ اعْتَبَرَ.", "«by a consideration».", "«bir itibarla».", segments=[seg("بِ","bi","part"), seg("اعْتِبَارٍ","itibar","noun")]),
  tok("لَطِيفٍ","latif","noun",[H, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ — صِفَةٌ مُشَبَّهَةٌ.", "«fine» — a na't.", "«latîf» — na't."),
  tok("غَيْرِ","ghayr","noun",[H, "naat-sifa", "idafa-definiteness"], "نَعْتٌ ثَانٍ مَجْرُورٌ مُضَافٌ.", "«other than» — a second na't, annexed.", "«olmayan» — ikinci na't, muzâf."),
  tok("حَقِيقِيٍّ","haqiqi","noun",[H, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نِسْبَةٌ إِلَى الْحَقِيقَةِ.", "«real» — the nisba to haqiqa.", "«hakikî» — hakikate nisbet.", punct=".")]})

# ----------- s2 — the four kinds (RESTORED matn)
S.append({"id": "s2", "translation": {
 "en": "It is of four kinds, because the quality is either FIXED, and the showing of its cause is intended; or NOT fixed, and its proving is intended." + R_EN,
 "tr": "Dört kısımdır; çünkü sıfat ya SABİTTİR de illetinin beyanı kastedilir, ya SABİT DEĞİLDİR de ispatı kastedilir." + R_TR},
 "tokens": [
  wahuwa(H),
  tok("أَرْبَعَةُ","arbaa","noun",[H, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — الْعَدَدُ عَلَى خِلَافِ الْمَعْدُودِ.", "«four» — the khabar, annexed.", "«dört» — haber, muzâf."),
  tok("أَقْسَامٍ","aqsam","noun",[H, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«kinds».", "«kısım».", punct="،"),
  tok("لِأَنَّ","anna","part",[H, "lam-taleel", "inna-wa-akhawatuha"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ نَاسِخٌ.", "«because» — the lam of cause on anna.", "«çünkü» — ta'lîl lâmı enne üzerinde.", segments=[seg("لِ","li","part"), seg("أَنَّ","anna","part")]),
  tok("الصِّفَةَ","sifa","noun",[H, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the quality» — anna's ism.", "«sıfat» — enne'nin ismi."),
  tok("إِمَّا","imma","part",[H, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("ثَابِتَةٌ","thabit","noun",[H, "inna-wa-akhawatuha", "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ — اسْمُ فَاعِلِ ثَبَتَ.", "«fixed» — anna's khabar.", "«sabit» — enne'nin haberi."),
  tok("قُصِدَ","qasada","verb",[H, "naib-al-fail", "jumla-sifa"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ لِثَابِتَةٌ.", "«is intended» — a passive; the clause a na't of «fixed».", "«kastedilir» — meçhul; cümle «sabit»in na'tı."),
  tok("بَيَانُ","bayan","noun",[H, "naib-al-fail", "idafa-definiteness", "masdar"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", "«the showing» — the naib al-fail.", "«beyanı» — nâib-i fâil."),
  tok("عِلَّتِهَا","illa","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«of its cause».", "«illetinin».", segments=[seg("عِلَّتِ","illa","noun"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("أَوْ","aw","part",[H, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("غَيْرُ","ghayr","noun",[H, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى ثَابِتَةٌ مَرْفُوعٌ مُضَافٌ.", "«not» — joined to «fixed», annexed.", "«değil» — «sabit»e ma'tûf, muzâf."),
  tok("ثَابِتَةٍ","thabit","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«fixed».", "«sabit»."),
  tok("قُصِدَ","qasada","verb",[H, "naib-al-fail", "jumla-sifa"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَالْجُمْلَةُ نَعْتٌ.", "«is intended».", "«kastedilir»."),
  tok("إِثْبَاتُهَا","ithbat","noun",[H, "naib-al-fail", "idafa-definiteness", "masdar", "form-iv-verbs"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — مَصْدَرُ أَثْبَتَ.", "«its proving».", "«ispatı».", segments=[seg("إِثْبَاتُ","ithbat","noun"), seg("هَا","pron-3fs","pron")], punct=".")]})

# ----------- s3 — the first: no customary cause appears (RESTORED matn)
S.append({"id": "s3", "translation": {
 "en": "The FIRST: either no cause for it appears in custom." + R_EN, "tr": "BİRİNCİSİ: ya âdette ona bir illet görünmez." + R_TR},
 "tokens": [
  tok("فَالْأُولَى","awwal","noun",[H, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْأُولَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مُؤَنَّثُ الْأَوَّلِ.", "«the first» — the mubtada; the feminine of awwal.", "«birincisi» — mübtedâ; evvel'in müennesi.",
      segments=[seg("فَ","fa","conj"), seg("الْأُولَى","awwal","noun")]),
  tok("إِمَّا","imma","part",[H, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  an_masd(H),
  tok("لَا","la-nafiya","part",[H, "an-masdariyya"], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يَظْهَرَ","zahara","verb",[H, "an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — جَازَ تَذْكِيرُهُ لِلْفَصْلِ بَيْنَهُ وَبَيْنَ فَاعِلِهِ.", "«appears» — nasb by an; masculine allowed, the doer being parted from it.", "«görünür» — en ile mansûb; fâilinden ayrı düştüğü için müzekker câiz."),
  tok("لَهَا","lahu","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for it».", "«ona».", segments=[seg("لَ","li","part"), seg("هَا","pron-3fs","pron")]),
  tok("فِي","fi","part",[H, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْعَادَةِ","ada","noun",[H, "huruf-jarr"], "مَجْرُورٌ.", "«custom».", "«âdet»."),
  tok("عِلَّةٌ","illa","noun",[H, "fail"], "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ.", "«a cause» — the delayed doer.", "«bir illet» — sona bırakılmış fâil.", punct=".")]})

# ----------- s4 — al-Mutanabbi: the cloud fevered by his gift
S.append({"id": "s4", "translation": {
 "en": "As Abu l-Tayyib says: «The cloud did not rival your bounty — rather • it caught a FEVER from it, and what it pours is the fever's sweat»." + R_EN,
 "tr": "Ebü't-Tayyib'in dediği gibi: «Bulut senin ihsanına benzeyemedi — ancak • ondan HUMMAYA tutuldu da döktüğü, humma teridir»." + R_TR},
 "tokens": [
  kaqawl(H), *abi(H, "الطَّيِّبِ", "tayyib", "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الطَّيِّبِ: كُنْيَةُ الْمُتَنَبِّي.", "«l-Tayyib» — al-Mutanabbi's kunya.", "«'t-Tayyib» — Mütenebbî'nin künyesi."),
  tok("لَمْ","lam","part",[H, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«did not».", "«-medi»."),
  tok("يَحْكِ","haka","verb",[H, "lam-jazim", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ حَرْفِ الْعِلَّةِ — حَكَى الشَّيْءَ: شَابَهَهُ.", "«rival» — jussive by dropping the weak letter; haka: to match.", "«benzeyemedi» — illet harfinin düşmesiyle meczûm; hakâ: benzemek."),
  tok("نَائِلَكَ","nail","noun",[H, "maful-bihi", "idafa-definiteness", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — النَّائِلُ: الْعَطَاءُ.", "«your bounty» — the object; nail: the gift.", "«ihsanını» — mef'ûl; nâil: bağış.", segments=[seg("نَائِلَ","nail","noun"), seg("كَ","pron-2ms","pron")]),
  tok("السَّحَابُ","sahab","noun",[H, "fail"], "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ.", "«the cloud» — the doer, delayed.", "«bulut» — fâil, sona bırakılmış."),
  tok("وَإِنَّمَا","innama","part",[H, "innama-kaffa", "qasr"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّمَا كَافَّةٌ وَمَكْفُوفَةٌ لِلْحَصْرِ — عَلَيْهَا يَقُومُ التَّعْلِيلُ.", "«rather, only» — the restricting innama; the claimed cause rides on it.", "«ancak» — hasr innemâsı; iddia edilen illet onun üstünde.",
      segments=[seg("وَ","wa","conj"), seg("إِنَّمَا","innama","part")], punct="*"),
  tok("حُمَّتْ","humma","verb",[H, "naib-al-fail", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مُضَاعَفٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — السَّحَابُ: أُصِيبَتْ بِالْحُمَّى.", "«it caught a fever» — a doubled passive; the deputy concealed: the cloud.", "«hummaya tutuldu» — muzâaf meçhul; nâib gizli: bulut."),
  tok("بِهِ","bi","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْبَاءُ لِلسَّبَبِيَّةِ: بِنَائِلِكَ.", "«from it» — the ba of cause: from your bounty.", "«ondan» — sebep bâsı: ihsanından.", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("فَصَبِيبُهَا","sabib","noun",[H, "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ عَاطِفَةٌ، وَصَبِيبُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ — الصَّبِيبُ: مَا يَنْصَبُّ، الْمَطَرُ.", "«and what it pours» — the mubtada; sabib: what pours down, the rain.", "«ve döktüğü» — mübtedâ; sabîb: dökülen, yağmur.",
      segments=[seg("فَ","fa","conj"), seg("صَبِيبُ","sabib","noun"), seg("هَا","pron-3fs","pron")]),
  tok("الرُّحَضَاءُ","ruhada","noun",[H, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الرُّحَضَاءُ: عَرَقُ الْحُمَّى.", "«the fever's sweat» — the khabar.", "«humma teri» — haber.", punct=".")]})
S[-1]["badi"] = [{"kind": "husn-talil", "sub": "la-illa", "receipt": "innama", "word": ix(S[-1], "حُمَّتْ"), "companion": ix(S[-1], "فَصَبِيبُهَا")}]

# ----------- s5 — or a cause other than the customary one appears (RESTORED matn)
S.append({"id": "s5", "translation": {
 "en": "Or a cause for it appears, other than the one mentioned." + R_EN, "tr": "Yahut ona, zikredilenden başka bir illet görünür." + R_TR},
 "tokens": [
  tok("أَوْ","aw","part",[H, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("يَظْهَرَ","zahara","verb",[H, "atf-nasaq", "an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَعْطُوفٌ عَلَى الْمَنْصُوبِ بِأَنْ.", "«appears» — joined to the nasb.", "«görünür» — mansûba ma'tûf."),
  tok("لَهَا","lahu","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for it».", "«ona».", segments=[seg("لَ","li","part"), seg("هَا","pron-3fs","pron")]),
  tok("عِلَّةٌ","illa","noun",[H, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a cause».", "«bir illet»."),
  tok("غَيْرُ","ghayr","noun",[H, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَرْفُوعٌ مُضَافٌ.", "«other than» — a na't.", "«başka» — na't."),
  tok("الْمَذْكُورَةِ","madhkur","noun",[H, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ ذَكَرَ.", "«the one mentioned».", "«zikredilen».", punct=".")]})

# ----------- s6 — al-Mutanabbi: not the killing of enemies but the wolves' hope
S.append({"id": "s6", "translation": {
 "en": "As he says: «He has no wish to kill his enemies — but • he guards against DISAPPOINTING what the wolves hope for»." + R_EN,
 "tr": "Onun dediği gibi: «Onda düşmanlarını öldürme isteği yok — fakat • kurtların umduğunu BOŞA ÇIKARMAKTAN sakınır»." + R_TR},
 "tokens": [
  kaqh(H),
  tok("مَا","ma-nafiya","part",[H, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not».", "«yok»."),
  tok("بِهِ","bi","part",[H, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«in him» — the fronted khabar.", "«onda» — öne alınmış haber.", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("قَتْلُ","qatl","noun",[H, "mubtada-khabar", "idafa-definiteness", "masdar", "imal-al-masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ.", "«the killing of» — the delayed mubtada; a masdar annexed to its object.", "«öldürmesi» — sona bırakılmış mübtedâ; mef'ûlüne muzâf masdar."),
  tok("أَعَادِيهِ","aadin","noun",[H, "idafa-definiteness", "jam-taksir", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ عَدُوٍّ.", "«his enemies» — a manqus plural; the kasra hidden on the ya.", "«düşmanlarını» — mankûs çoğul; kesre yâda gizli.", segments=[seg("أَعَادِي","aadin","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَلَكِنْ","lakin","part",[H, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا يَعْمَلُ — عَلَيْهِ يَقُومُ التَّعْلِيلُ.", "«but» — the light lakin, no government; the claimed cause rides on it.", "«fakat» — muhaffef lâkin, amelsiz; iddia edilen illet onun üstünde.",
      segments=[seg("وَ","wa","conj"), seg("لَكِنْ","lakin","part")], punct="*"),
  tok("يَتَّقِي","ittaqa","verb",[H, "mudari-marfu", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he guards against» — raf hidden on the ya.", "«sakınır» — ref yâda gizli."),
  tok("إِخْلَافَ","ikhlaf","noun",[H, "maful-bihi", "idafa-definiteness", "masdar", "form-iv-verbs"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ — مَصْدَرُ أَخْلَفَ: أَخْلَفَ الرَّجَاءَ: لَمْ يُنْجِزْهُ.", "«disappointing» — the object; akhlafa the hope: to fail it.", "«boşa çıkarmak» — mef'ûl; ahlefe: umudu boşa çıkarmak."),
  tok("مَا","ma-mawsula","pron",[H, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the mawsul, annexed to.", "«-duğunu» — mevsûl, muzâfun ileyh."),
  tok("تَرْجُو","raja","verb",[H, "ism-mawsul", "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ — صِلَةٌ؛ وَالْعَائِدُ مَحْذُوفٌ: تَرْجُوهُ.", "«hope for» — the sila; the returning pronoun dropped.", "«umduğu» — sıla; âid hazfedilmiş."),
  tok("الذِّئَابُ","dhib","noun",[H, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ ذِئْبٍ: تَرْجُو لُحُومَ الْقَتْلَى.", "«the wolves» — the doer; they hope for the slain.", "«kurtlar» — fâil; öldürülenleri umarlar.", punct=".")]})
S[-1]["badi"] = [{"kind": "husn-talil", "sub": "ghayr-madhkura", "receipt": "lakin", "word": ix(S[-1], "يَتَّقِي"), "companion": ix(S[-1], "قَتْلُ")}]

# ----------- s7 — the second: possible (RESTORED matn)
S.append({"id": "s7", "translation": {
 "en": "The SECOND: it is either possible." + R_EN, "tr": "İKİNCİSİ: ya mümkündür." + R_TR},
 "tokens": [
  wa_conj("وَالثَّانِيَةُ","thani","noun",[H, "mubtada-khabar"], "الثَّانِيَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the second» — the mubtada.", "«ve ikincisi» — mübtedâ."),
  tok("إِمَّا","imma","part",[H, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("مُمْكِنَةٌ","mumkin","noun",[H, "mubtada-khabar", "ism-fail", "form-iv-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ أَمْكَنَ.", "«possible» — the khabar.", "«mümkün» — haber.", punct=".")]})

# ----------- s8 — Muslim b. al-Walid: the slanderer whose ill-doing was good
S.append({"id": "s8", "translation": {
 "en": "As Muslim b. al-Walid says: «O slanderer whose ill-doing turned out well for us: • the FEAR of you saved the pupil of my eye from drowning»." + R_EN,
 "tr": "Müslim b. Velîd'in dediği gibi: «Ey kötülüğü hakkımızda hayır olan gammaz: • senden KORKUM gözbebeğimi boğulmaktan kurtardı»." + R_TR},
 "tokens": [
  kaqawl(H),
  tok("مُسْلِمِ","muslim-alam","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ — مُسْلِمُ بْنُ الْوَلِيدِ: صَرِيعُ الْغَوَانِي.", "«Muslim» — Muslim b. al-Walid, «Sariʿ al-Ghawani».", "«Müslim» — Müslim b. Velîd, «Sarîu'l-Gavânî»."),
  tok("بْنِ","ibn","noun",[H, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("الْوَلِيدِ","walid-alam","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Walid».", "«Velîd».", punct=":"),
  tok("يَا","ya","part",[H, "vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("وَاشِيًا","washin","noun",[H, "vocative-munada", "ism-fail", "ism-maqsur-manqus"], "مُنَادًى نَكِرَةٌ غَيْرُ مَقْصُودَةٍ مَنْصُوبٌ — اسْمُ فَاعِلِ وَشَى: النَّمَّامُ؛ مَنْقُوصٌ يَظْهَرُ نَصْبُهُ.", "«slanderer» — an unspecified indefinite munada, mansub; the manqus shows its nasb.", "«gammaz» — kastedilmemiş nekre münâdâ, mansûb; mankûs nasbını gösterir."),
  tok("حَسُنَتْ","hasuna","verb",[H, "jumla-sifa"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ نَعْتٌ لِوَاشِيًا.", "«turned out well» — the clause a na't of the munada.", "«hayır oldu» — cümle münâdânın na'tı."),
  tok("فِينَا","fi","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي حَقِّنَا.", "«for us».", "«hakkımızda».", segments=[seg("فِي","fi","part"), seg("نَا","pron-1p","pron")]),
  tok("إِسَاءَتُهُ","isaa","noun",[H, "fail", "idafa-definiteness", "masdar", "form-iv-verbs"], "فَاعِلٌ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ أَسَاءَ.", "«his ill-doing» — the doer.", "«kötülüğü» — fâil.", segments=[seg("إِسَاءَتُ","isaa","noun"), seg("هُ","pron-3ms","pron")], punct="*"),
  tok("نَجَّى","najja","verb",[H, "form-ii-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لِلتَّعْلِيلِ: بِهَا تُدَّعَى الْعِلَّةُ.", "«saved» — a fresh sentence giving the cause: the claim rides on it.", "«kurtardı» — illeti veren müste'nef cümle: iddia onun üstünde."),
  tok("حِذَارُكَ","hidhar","noun",[H, "fail", "idafa-definiteness", "masdar"], "فَاعِلٌ مَرْفُوعٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ: الْخَوْفُ مِنْكَ.", "«the fear of you» — the doer; a masdar annexed to its object.", "«senden korkum» — fâil; mef'ûlüne muzâf masdar.", segments=[seg("حِذَارُ","hidhar","noun"), seg("كَ","pron-2ms","pron")]),
  tok("إِنْسَانِي","insan","noun",[H, "maful-bihi", "idafa-definiteness", "ya-al-mutakallim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — إِنْسَانُ الْعَيْنِ: الْحَدَقَةُ.", "«the pupil of my eye» — the object; the nasb hidden before my ya.", "«gözbebeğimi» — mef'ûl; nasb mütekellim yâsından önce gizli.", segments=[seg("إِنْسَانِ","insan","noun"), seg("ي","pron-1s","pron")]),
  tok("مِنَ","min","part",[H, "huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  tok("الْغَرَقِ","gharaq","noun",[H, "huruf-jarr", "masdar"], "مَجْرُورٌ — الْغَرَقُ فِي الدُّمُوعِ.", "«drowning» — in tears.", "«boğulmak» — gözyaşlarında.", punct=".")]})
S[-1]["badi"] = [{"kind": "husn-talil", "sub": "mumkina", "receipt": "jumla", "word": ix(S[-1], "نَجَّى"), "companion": ix(S[-1], "حَسُنَتْ")}]

# ----------- s9 — or impossible (RESTORED matn)
S.append({"id": "s9", "translation": {
 "en": "Or not possible." + R_EN, "tr": "Yahut mümkün değildir." + R_TR},
 "tokens": [
  tok("أَوْ","aw","part",[H, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("غَيْرُ","ghayr","noun",[H, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى مُمْكِنَةٌ مَرْفُوعٌ مُضَافٌ.", "«not» — joined to «possible».", "«değil» — «mümkün»e ma'tûf."),
  tok("مُمْكِنَةٍ","mumkin","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«possible».", "«mümkün».", punct=".")]})

# ----------- s10 — the author's bayt from Persian: Gemini's belt
S.append({"id": "s10", "translation": {
 "en": "As in the author's bayt, rendered from Persian: «Were the INTENT of Gemini not to serve him, • you would not see upon it the belt of one girded»." + R_EN,
 "tr": "Müellifin Farsçadan aktardığı beyitte olduğu gibi: «Cevzâ'nın NİYETİ ona hizmet olmasaydı, • üstünde kuşanmışın kemerini görmezdin»." + R_TR},
 "tokens": [
  kaqawl(H),
  tok("الْمُصَنِّفِ","musannif","noun",[H, "idafa-definiteness", "ism-fail", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ صَنَّفَ: صَاحِبُ الْكِتَابِ.", "«the author» — the ism fa'il of sannafa.", "«müellif» — sannefe'nin ism-i fâili.", punct=":"),
  tok("لَوْ","law","part",[H, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ — عَلَيْهِ يَقُومُ التَّعْلِيلُ.", "«were … not» — the unreal law; the claimed cause rides on it.", "«-saydı» — gayr-i vâki lev; iddia edilen illet onun üstünde."),
  tok("لَمْ","lam","part",[H, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me»."),
  tok("تَكُنْ","kana","verb",[H, "lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«were» — kana's jussive; its waw dropped.", "«olsaydı» — kâne'nin meczûmu; vâvı düşmüş."),
  tok("نِيَّةُ","niyya","noun",[H, "kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ تَكُنْ مَرْفُوعٌ مُضَافٌ.", "«the intent of» — kana's ism.", "«niyeti» — kâne'nin ismi."),
  tok("الْجَوْزَاءِ","jawza","noun",[H, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْجَوْزَاءُ: بُرْجٌ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ، جُرَّ بِالْكَسْرَةِ لِلْأَلِفِ وَاللَّامِ.", "«Gemini» — the constellation; a diptote by its feminine alif, given kasra by the article.", "«Cevzâ» — burç; memdûd te'nis elifiyle gayr-i munsarif, lâm-ı tarifle kesre alır."),
  tok("خِدْمَتَهُ","khidma","noun",[H, "kana-wa-akhawatuha", "idafa-definiteness", "masdar"], "خَبَرُ تَكُنْ مَنْصُوبٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to serve him» — kana's khabar.", "«ona hizmet» — kâne'nin haberi.", punct="*"),
  tok("لَمَا","ma-nafiya","part",[H, "in-shartiyya", "anwa-ma"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَمَا نَافِيَةٌ.", "«then … not» — the lam of law's answer on the negating ma.", "«-mezdin» — lev'in cevap lâmı nefiy mâsı üstünde.", segments=[seg("لَ","li","part"), seg("مَا","ma-nafiya","part")]),
  tok("رَأَيْتَ","raa","verb",[H, "in-shartiyya", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جَوَابُ لَوْ.", "«you would see» — law's answer.", "«görürdün» — lev'in cevabı."),
  tok("عَلَيْهَا","ala","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«upon it».", "«üstünde».", segments=[seg("عَلَيْ","ala","part"), seg("هَا","pron-3fs","pron")]),
  tok("عِقْدَ","iqd","noun",[H, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ — عِقْدُ الْمِنْطَقَةِ: الْحِزَامُ؛ نُجُومُ الْجَوْزَاءِ.", "«the belt» — the object; the girdle's knot: Gemini's stars.", "«kemer» — mef'ûl; kuşağın düğümü: Cevzâ'nın yıldızları."),
  tok("مُنْتَطِقٍ","muntatiq","noun",[H, "idafa-definiteness", "ism-fail", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ انْتَطَقَ: شَدَّ الْمِنْطَقَةَ.", "«of one girded» — the ism fa'il of intataqa.", "«kuşanmışın» — intataka'nın ism-i fâili.", punct=".")]})
S[-1]["badi"] = [{"kind": "husn-talil", "sub": "ghayr-mumkina", "receipt": "law", "word": ix(S[-1], "نِيَّةُ"), "companion": ix(S[-1], "عِقْدَ")}]

# ----------- s11 — what is built on doubt is joined to it (RESTORED matn)
S.append({"id": "s11", "translation": {
 "en": "And what is built on DOUBT is joined to it." + R_EN, "tr": "ŞÜPHE üzerine bina edilen de ona katılır." + R_TR},
 "tokens": [
  wa_conj("وَيُلْحَقُ","alhaqa","verb",[H, "naib-al-fail", "form-iv-verbs"], "يُلْحَقُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and is joined» — a passive.", "«ve katılır» — meçhul."),
  tok("بِهِ","bi","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to it».", "«ona».", segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("مَا","ma-mawsula","pron",[H, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ.", "«what» — the mawsul, the naib al-fail.", "«-en» — mevsûl, nâib-i fâil."),
  tok("يُبْنَى","bana","verb",[H, "ism-mawsul", "naib-al-fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is built» — the sila.", "«bina edilir» — sıla."),
  tok("عَلَى","ala","part",[H, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  tok("الشَّكِّ","shakk","noun",[H, "huruf-jarr"], "مَجْرُورٌ.", "«doubt».", "«şüphe».", punct=".")]})

# ----------- s12 — Abu Tammam: the white clouds that hid a beloved
S.append({"id": "s12", "translation": {
 "en": "As Abu Tammam says: «AS IF the white clouds had hidden beneath them • a beloved — so their tears never cease»." + R_EN,
 "tr": "Ebû Temmâm'ın dediği gibi: «SANKİ beyaz bulutlar altlarında • bir sevgiliyi gizlemişler de gözyaşları dinmiyor»." + R_TR},
 "tokens": [
  kaqawl(H), *abi(H, "تَمَّامٍ", "tammam-alam", "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو تَمَّامٍ حَبِيبُ بْنُ أَوْسٍ الطَّائِيُّ.", "«Tammam» — Abu Tammam Habib b. Aws.", "«Temmâm» — Ebû Temmâm Habîb b. Evs."),
  tok("كَأَنَّ","kaanna","part",[H, "inna-wa-akhawatuha", "tashbih"], "حَرْفٌ نَاسِخٌ لِلتَّشْبِيهِ — بِهِ يُبْنَى التَّعْلِيلُ عَلَى الشَّكِّ.", "«as if» — the likening nasikh; on it the cause stands in doubt.", "«sanki» — teşbih nâsihi; illet onunla şüphe üzerine kurulur."),
  tok("السَّحَابَ","sahab","noun",[H, "inna-wa-akhawatuha"], "اسْمُ كَأَنَّ مَنْصُوبٌ.", "«the clouds» — kaanna's ism.", "«bulutlar» — keenne'nin ismi."),
  tok("الْغُرَّ","aghar","noun",[H, "naat-sifa", "jam-taksir"], "نَعْتٌ مَنْصُوبٌ — جَمْعُ أَغَرَّ: الْأَبْيَضُ.", "«white» — a na't; the plural of agharr.", "«beyaz» — na't; eğarr'ın çoğulu."),
  tok("غَيَّبْنَ","ghayyaba","verb",[H, "inna-wa-akhawatuha", "form-ii-verbs", "fail"], "فِعْلٌ مَاضٍ، وَنُونُ النِّسْوَةِ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كَأَنَّ؛ السَّحَابُ يُعَامَلُ مُعَامَلَةَ الْجَمْعِ.", "«had hidden» — the women's nun is the doer; the clause is kaanna's khabar.", "«gizlemişler» — nisve nûnu fâil; cümle keenne'nin haberi."),
  tok("تَحْتَهَا","tahta","noun",[H, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«beneath them».", "«altlarında».", segments=[seg("تَحْتَ","tahta","noun"), seg("هَا","pron-3fs","pron")], punct="*"),
  tok("حَبِيبًا","habib","noun",[H, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a beloved» — the object.", "«bir sevgiliyi» — mef'ûl."),
  tok("فَمَا","ma-nafiya","part",[H, "anwa-ma"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَمَا نَافِيَةٌ.", "«so … not».", "«de … -miyor».", segments=[seg("فَ","fa","conj"), seg("مَا","ma-nafiya","part")]),
  tok("تَرْقَا","raqaa","verb",[H, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَصْلُهُ تَرْقَأُ، سُهِّلَتْ هَمْزَتُهُ أَلِفًا؛ رَقَأَ الدَّمْعُ: جَفَّ.", "«cease» — tarqaʾu with its hamza eased to an alif; raqaʾa: the tear dries.", "«dinmiyor» — terka'u, hemzesi elife yumuşamış; rakae: yaş kurudu."),
  tok("لَهُنَّ","lahu","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«their».", "«onların».", segments=[seg("لَ","li","part"), seg("هُنَّ","pron-3fp","pron")]),
  tok("مَدَامِعُ","madma","noun",[H, "fail", "jam-taksir", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ مَدْمَعٍ: مَجْرَى الدَّمْعِ، وَالْمُرَادُ الدُّمُوعُ مَجَازًا؛ صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«tears» — the doer; madmaʿ: the tear's channel, the tears by majaz.", "«gözyaşları» — fâil; medma': yaş yolu, mecazen yaşlar.", punct=".")]})
S[-1]["badi"] = [{"kind": "husn-talil", "sub": "shakk", "receipt": "kaanna", "word": ix(S[-1], "غَيَّبْنَ"), "companion": ix(S[-1], "تَرْقَا")}]

# ----------- s13 — tafri's definition (RESTORED matn)
S.append({"id": "s13", "translation": {
 "en": "Among them is TAFRIʿ: that a ruling be proved for one dependent of a thing after its being proved for another dependent of it." + R_EN,
 "tr": "Onlardan biri TEFRÎ'DİR: bir emrin bir müteallikine, diğer müteallikine ispat edildikten sonra bir hükmün ispat edilmesi." + R_TR},
 "tokens": [
  minha(F),
  tok("التَّفْرِيعُ","tafri","noun",[F, "mubtada-khabar", "masdar", "form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ فَرَّعَ.", "«the tafriʿ» — the delayed mubtada.", "«tefrî'» — sona bırakılmış mübtedâ.", punct="،"),
  wahuwa(F),
  an_masd(F),
  tok("يُثْبَتَ","athbata","verb",[F, "an-masdariyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be proved» — a passive under an.", "«ispat edilmesi» — en altında meçhul."),
  tok("لِمُتَعَلِّقِ","mutaalliq","noun",[F, "huruf-jarr", "idafa-definiteness", "ism-fail", "form-v-verbs"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — الْمُتَعَلِّقُ: مَا يَتَّصِلُ بِالشَّيْءِ.", "«for a dependent of» — what attaches to a thing.", "«bir müteallikine» — şeye bağlı olan.", segments=[seg("لِ","li","part"), seg("مُتَعَلِّقِ","mutaalliq","noun")]),
  tok("أَمْرٍ","amr","noun",[F, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir emrin»."),
  tok("حُكْمٌ","hukm","noun",[F, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a ruling» — the naib al-fail.", "«bir hüküm» — nâib-i fâil."),
  tok("بَعْدَ","bada","noun",[F, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ.", "«after».", "«sonra»."),
  tok("إِثْبَاتِهِ","ithbat","noun",[F, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its being proved».", "«ispat edilmesinden».", segments=[seg("إِثْبَاتِ","ithbat","noun"), seg("هِ","pron-3ms","pron")]),
  tok("لِمُتَعَلِّقٍ","mutaalliq","noun",[F, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for a dependent».", "«bir müteallikine».", segments=[seg("لِ","li","part"), seg("مُتَعَلِّقٍ","mutaalliq","noun")]),
  tok("لَهُ","lahu","part",[F, "huruf-jarr", "naat-sifa"], "جَارٌّ وَمَجْرُورٌ نَعْتٌ لِمُتَعَلِّقٍ.", "«of it» — a na't of the dependent.", "«onun» — müteallikin na'tı.", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("آخَرَ","akhar","noun",[F, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ ثَانٍ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — a diptote na't.", "«diğer» — gayr-i munsarif na't.", punct=".")]})

# ----------- s14 — al-Kumayt: your minds heal ignorance as your blood heals rabies
S.append({"id": "s14", "translation": {
 "en": "As al-Kumayt says of the Prophet's house: «Your minds are a CURE for the sickness of ignorance, • just as your blood cures rabies»." + R_EN,
 "tr": "Kümeyt'in Ehl-i Beyt hakkında dediği gibi: «Akıllarınız cehalet hastalığına ŞİFADIR, • nasıl ki kanlarınız kuduzdan şifa verir»." + R_TR},
 "tokens": [
  kaqawl(F),
  tok("الْكُمَيْتِ","kumayt-alam","noun",[F, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْكُمَيْتُ بْنُ زَيْدٍ الْأَسَدِيُّ، فِي أَهْلِ الْبَيْتِ.", "«al-Kumayt» — al-Kumayt b. Zayd al-Asadi, on the Prophet's house.", "«Kümeyt» — Kümeyt b. Zeyd el-Esedî, Ehl-i Beyt hakkında.", punct=":"),
  tok("أَحْلَامُكُمْ","hilm","noun",[F, "mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — جَمْعُ حِلْمٍ: الْعَقْلُ.", "«your minds» — the mubtada; the plural of hilm.", "«akıllarınız» — mübtedâ; hilm'in çoğulu.", segments=[seg("أَحْلَامُ","hilm","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("لِسَقَامِ","saqam","noun",[F, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ، مُتَعَلِّقٌ بِشَافِيَةٌ.", "«for the sickness of» — attached to «cure».", "«hastalığına» — «şifa»ya bağlı.", segments=[seg("لِ","li","part"), seg("سَقَامِ","saqam","noun")]),
  tok("الْجَهْلِ","jahl","noun",[F, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ignorance».", "«cehalet»."),
  tok("شَافِيَةٌ","shafin","noun",[F, "mubtada-khabar", "ism-fail", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ شَفَى، مُؤَنَّثُ شَافٍ.", "«a cure» — the khabar; the feminine ism fa'il of shafa.", "«şifa» — haber; şefâ'nın ism-i fâili, müennes.", punct="*"),
  tok("كَمَا","kama","part",[F, "huruf-jarr", "anwa-ma"], "الْكَافُ جَارَّةٌ، وَمَا مَصْدَرِيَّةٌ — عَلَيْهَا يُبْنَى التَّفْرِيعُ: الْحُكْمُ الثَّانِي عَلَى الْأَوَّلِ.", "«just as» — the ka of likeness on the masdar-ma; the tafriʿ hinges on it.", "«nasıl ki» — masdar mâsı üstünde teşbih kâfı; tefrî' onun üstünde döner.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("دِمَاؤُكُمْ","dam-blood","noun",[F, "mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — جَمْعُ دَمٍ؛ الْهَمْزَةُ عَلَى وَاوٍ لِلضَّمَّةِ.", "«your blood» — the mubtada; the plural of dam.", "«kanlarınız» — mübtedâ; dem'in çoğulu.", segments=[seg("دِمَاؤُ","dam-blood","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("تَشْفِي","shafa","verb",[F, "mubtada-khabar", "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«cures» — the clause is the khabar.", "«şifa verir» — cümle haber."),
  tok("مِنَ","min","part",[F, "huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-dan»."),
  tok("الْكَلَبِ","kalab","noun",[F, "huruf-jarr"], "مَجْرُورٌ — الْكَلَبُ: دَاءُ الْكَلْبِ، وَشِفَاؤُهُ بِدَمِ الْمُلُوكِ فِي زَعْمِ الْعَرَبِ.", "«rabies» — cured, in the Arabs' belief, by a king's blood.", "«kuduz» — Arapların inanışında kral kanıyla şifa bulur.", punct=".")]})
S[-1]["badi"] = [{"kind": "tafri", "word": ix(S[-1], "كَمَا"), "first": [ix(S[-1], "أَحْلَامُكُمْ"), ix(S[-1], "شَافِيَةٌ")], "second": [ix(S[-1], "دِمَاؤُكُمْ"), ix(S[-1], "تَشْفِي")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "husn": need("husn", "حُسْن", "ح س ن", "noun", "beauty, fineness (masdar of حَسُنَ)", "güzellik, hüsün (حَسُنَ'nin masdarı)", 2),
 "talil": need("talil", "تَعْلِيل", "ع ل ل", "noun", "giving a cause (masdar of عَلَّلَ)", "illet gösterme, ta'lîl (عَلَّلَ'nin masdarı)", 4),
 "illa": need("illa", "عِلَّة", "ع ل ل", "noun", "a cause, a reason; a sickness", "illet, sebep; hastalık", 3),
 "munasib": need("munasib", "مُنَاسِب", "ن س ب", "noun", "suitable, fitting (ism fa'il of نَاسَبَ)", "münasip, uygun (نَاسَبَ'nin ism-i fâili)", 3),
 "itibar": need("itibar", "اعْتِبَار", "ع ب ر", "noun", "a consideration, a regard (masdar of اعْتَبَرَ)", "itibar, göz önüne alma (اعْتَبَرَ'nin masdarı)", 4),
 "latif": need("latif", "لَطِيف", "ل ط ف", "noun", "fine, subtle, delicate", "latîf, ince", 3),
 "haqiqi": need("haqiqi", "حَقِيقِيّ", "ح ق ق", "noun", "real, literal (nisba of حَقِيقَة)", "hakikî, gerçek (حَقِيقَة'nin nisbesi)", 3),
 "arbaa": need("arbaa", "أَرْبَعَة", "ر ب ع", "noun", "four", "dört", 1),
 "imma": need("imma", "إِمَّا", None, "part", "either … (or); the particle of detailing", "ya … (ya da); tafsil edatı", 2),
 "thabit": need("thabit", "ثَابِت", "ث ب ت", "noun", "fixed, established (ism fa'il of ثَبَتَ)", "sabit, yerleşik (ثَبَتَ'nin ism-i fâili)", 3),
 "qasada": need("qasada", "قَصَدَ", "ق ص د", "verb", "to intend, to aim at (قَصَدَ يَقْصِدُ)", "kastetmek, yönelmek (قَصَدَ يَقْصِدُ)", 3),
 "zahara": need("zahara", "ظَهَرَ", "ظ ه ر", "verb", "to appear, to become manifest (ظَهَرَ يَظْهَرُ)", "görünmek, zâhir olmak (ظَهَرَ يَظْهَرُ)", 2),
 "madhkur": need("madhkur", "مَذْكُور", "ذ ك ر", "noun", "mentioned (ism maf'ul of ذَكَرَ)", "zikredilen, mezkûr (ذَكَرَ'nin ism-i mef'ûlü)", 3),
 "mumkin": need("mumkin", "مُمْكِن", "م ك ن", "noun", "possible (ism fa'il of أَمْكَنَ)", "mümkün (أَمْكَنَ'nin ism-i fâili)", 3),
 "tayyib": need("tayyib", "الطَّيِّب", "ط ي ب", "propn", "al-Tayyib — Abu l-Tayyib, al-Mutanabbi's kunya", "et-Tayyib — Ebü't-Tayyib, Mütenebbî'nin künyesi", 5),
 "haka": need("haka", "حَكَى", "ح ك ي", "verb", "to tell; to resemble, to match (حَكَى يَحْكِي; naqis)", "anlatmak; benzemek, denk olmak (حَكَى يَحْكِي; nâkıs)", 4),
 "nail": need("nail", "نَائِل", "ن ي ل", "noun", "a gift, bounty (ism fa'il of نَالَ used as a noun)", "bağış, ihsan (نَالَ'nin ism-i fâili, isim olarak)", 5),
 "humma": need("humma", "حُمَّ", "ح م م", "verb", "to catch a fever (a doubled passive; حُمَّ يُحَمُّ)", "hummaya tutulmak (muzâaf meçhul; حُمَّ يُحَمُّ)", 5),
 "sabib": need("sabib", "صَبِيب", "ص ب ب", "noun", "what pours down; the rain", "dökülen; yağmur", 5),
 "ruhada": need("ruhada", "رُحَضَاء", "ر ح ض", "noun", "the sweat of fever", "humma teri", 6),
 "aadin": need("aadin", "أَعَادٍ", "ع د و", "noun", "enemies (a manqus plural of عَدُوّ; الْأَعَادِي)", "düşmanlar (عَدُوّ'un mankûs çoğulu; الْأَعَادِي)", 5),
 "ikhlaf": need("ikhlaf", "إِخْلَاف", "خ ل ف", "noun", "failing a promise or a hope (masdar of أَخْلَفَ)", "sözü yahut umudu boşa çıkarma (أَخْلَفَ'nin masdarı)", 5),
 "raja": need("raja", "رَجَا", "ر ج و", "verb", "to hope for (رَجَا يَرْجُو; naqis)", "ummak (رَجَا يَرْجُو; nâkıs)", 3),
 "dhib": need("dhib", "ذِئْب", "ذ ء ب", "noun", "a wolf", "kurt", 2, plural="ذِئَاب"),
 "muslim-alam": need("muslim-alam", "مُسْلِم", None, "propn", "Muslim b. al-Walid al-Ansari, «Sariʿ al-Ghawani», the Abbasid poet (d. 208/823)", "Müslim b. Velîd el-Ensârî, «Sarîu'l-Gavânî», Abbâsî şairi (ö. 208/823)", 6),
 "walid-alam": need("walid-alam", "الْوَلِيد", None, "propn", "al-Walid — a man's name", "Velîd — erkek adı", 5),
 "ya": need("ya", "يَا", None, "part", "O (the particle of address)", "ey (nidâ edatı)", 1),
 "washin": need("washin", "وَاشٍ", "و ش ي", "noun", "a slanderer, a tale-bearer (ism fa'il of وَشَى; الْوَاشِي)", "gammaz, söz taşıyan (وَشَى'nın ism-i fâili; الْوَاشِي)", 5),
 "isaa": need("isaa", "إِسَاءَة", "س و ء", "noun", "ill-doing, an offence (masdar of أَسَاءَ)", "kötülük etme (أَسَاءَ'nin masdarı)", 4),
 "najja": need("najja", "نَجَّى", "ن ج و", "verb", "to save, to rescue (Form II, naqis; نَجَّى يُنَجِّي)", "kurtarmak (II. bâb, nâkıs; نَجَّى يُنَجِّي)", 3, form="II"),
 "hidhar": need("hidhar", "حِذَار", "ح ذ ر", "noun", "fear, wariness (a masdar of حَذِرَ)", "korku, sakınma (حَذِرَ'nin masdarı)", 5),
 "gharaq": need("gharaq", "غَرَق", "غ ر ق", "noun", "drowning (masdar of غَرِقَ)", "boğulma (غَرِقَ'nin masdarı)", 3),
 "musannif": need("musannif", "مُصَنِّف", "ص ن ف", "noun", "an author, the compiler of a book (ism fa'il of صَنَّفَ)", "müellif, musannif (صَنَّفَ'nin ism-i fâili)", 4),
 "niyya": need("niyya", "نِيَّة", "ن و ي", "noun", "an intention", "niyet", 2),
 "jawza": need("jawza", "الْجَوْزَاء", "ج و ز", "propn", "Gemini — the constellation whose belt of stars is Orion's girdle", "Cevzâ — kemer yıldızlı burç", 6),
 "khidma": need("khidma", "خِدْمَة", "خ د م", "noun", "service (masdar of خَدَمَ)", "hizmet (خَدَمَ'nin masdarı)", 2),
 "iqd": need("iqd", "عِقْد", "ع ق د", "noun", "a knot; a necklace, a belt's clasp", "düğüm; gerdanlık, kemer bağı", 4),
 "muntatiq": need("muntatiq", "مُنْتَطِق", "ن ط ق", "noun", "one girded with a belt (ism fa'il of انْتَطَقَ)", "kuşak kuşanmış (انْتَطَقَ'nın ism-i fâili)", 6),
 "alhaqa": need("alhaqa", "أَلْحَقَ", "ل ح ق", "verb", "to join, to attach to (Form IV; أَلْحَقَ يُلْحِقُ)", "katmak, ilhak etmek (IV. bâb; أَلْحَقَ يُلْحِقُ)", 4, form="IV"),
 "bana": need("bana", "بَنَى", "ب ن ي", "verb", "to build (بَنَى يَبْنِي; naqis)", "bina etmek, kurmak (بَنَى يَبْنِي; nâkıs)", 2),
 "shakk": need("shakk", "شَكّ", "ش ك ك", "noun", "doubt", "şüphe, şek", 2),
 "tammam-alam": need("tammam-alam", "تَمَّام", None, "propn", "Tammam — Abu Tammam Habib b. Aws al-Ta'i, the poet (d. 231/846)", "Temmâm — Ebû Temmâm Habîb b. Evs et-Tâî, şair (ö. 231/846)", 6),
 "aghar": need("aghar", "أَغَرّ", "غ ر ر", "noun", "white, bright-faced (its plural غُرّ)", "beyaz, alnı açık (çoğulu غُرّ)", 5, plural="غُرّ"),
 "ghayyaba": need("ghayyaba", "غَيَّبَ", "غ ي ب", "verb", "to hide, to make disappear (Form II; غَيَّبَ يُغَيِّبُ)", "gizlemek, kaybetmek (II. bâb; غَيَّبَ يُغَيِّبُ)", 4, form="II"),
 "raqaa": need("raqaa", "رَقَأَ", "ر ق ء", "verb", "to cease (of tears, of blood): to dry (رَقَأَ يَرْقَأُ)", "dinmek (yaş, kan): kurumak (رَقَأَ يَرْقَأُ)", 6),
 "madma": need("madma", "مَدْمَع", "د م ع", "noun", "the tear's channel; a tear (its plural مَدَامِع)", "yaş yolu; gözyaşı (çoğulu مَدَامِع)", 5, plural="مَدَامِع"),
 "tafri": need("tafri", "تَفْرِيع", "ف ر ع", "noun", "tafriʿ — branching a ruling (masdar of فَرَّعَ)", "tefrî' — hükmü dallandırma (فَرَّعَ'nin masdarı)", 5),
 "athbata": need("athbata", "أَثْبَتَ", "ث ب ت", "verb", "to prove, to establish (Form IV; أَثْبَتَ يُثْبِتُ)", "ispat etmek (IV. bâb; أَثْبَتَ يُثْبِتُ)", 3, form="IV"),
 "mutaalliq": need("mutaalliq", "مُتَعَلِّق", "ع ل ق", "noun", "a dependent, what attaches to a thing (ism fa'il of تَعَلَّقَ)", "müteallik, bir şeye bağlı olan (تَعَلَّقَ'nın ism-i fâili)", 4),
 "akhar": need("akhar", "آخَر", "ء خ ر", "noun", "another, other (a diptote)", "diğer, başka (gayr-i munsarif)", 2),
 "kumayt-alam": need("kumayt-alam", "الْكُمَيْت", None, "propn", "al-Kumayt b. Zayd al-Asadi, the poet of the Hashimiyyat (d. 126/744)", "Kümeyt b. Zeyd el-Esedî, Hâşimiyyât şairi (ö. 126/744)", 6),
 "hilm": need("hilm", "حِلْم", "ح ل م", "noun", "forbearance; the mind, reason (its plural أَحْلَام)", "hilim; akıl (çoğulu أَحْلَام)", 3, plural="أَحْلَام"),
 "saqam": need("saqam", "سَقَام", "س ق م", "noun", "sickness", "hastalık", 4),
 "shafin": need("shafin", "شَافٍ", "ش ف ي", "noun", "healing, a cure (ism fa'il of شَفَى; الشَّافِي)", "şifa veren (شَفَى'nın ism-i fâili; الشَّافِي)", 4),
 "shafa": need("shafa", "شَفَى", "ش ف ي", "verb", "to heal, to cure (شَفَى يَشْفِي; naqis)", "şifa vermek, iyileştirmek (شَفَى يَشْفِي; nâkıs)", 3),
 "kalab": need("kalab", "كَلَب", "ك ل ب", "noun", "rabies", "kuduz", 5),
 "ma-masdariyya": need("ma-masdariyya", "مَا", None, "part", "the masdar-making ma", "masdar yapan mâ", 3),
}
for k in ("qawl", "min", "huwa", "an-masdariyya", "fi", "li", "bi", "ka", "wa", "fa", "pron-3fs", "pron-3ms", "pron-1s", "pron-1p", "pron-2ms", "pron-2mp", "pron-3fp",
          "aw", "aqsam", "ma-mawsula", "ma-nafiya", "ab", "lam", "law", "ala", "kana", "raa", "lahu", "wasf", "iddaa", "sifa", "anna", "ghayr", "bayan", "ithbat", "awwal", "thani",
          "ada", "sahab", "innama", "lakin", "qatl", "ittaqa", "ibn", "hasuna", "insan", "kaanna", "tahta", "habib", "amr", "hukm", "bada", "jahl", "kama", "dam-blood", "la-nafiya"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
put_morph(mo, "humma", gem("nasara", "حَمّ", "حَمَم", "حُمّ", "حْمُم", ["حُمَّ", "حُمَّا", "حُمُّوا", "حُمِّي", "حُمَّا", "اُحْمُمْنَ"], "حُمَّى", "حَامّ", "مَحْمُوم", "حُمَّ", "يُحَمُّ",
                     "مُضَاعَفٌ؛ الشَّائِعُ مِنْهُ الْمَبْنِيُّ لِلْمَجْهُولِ: حُمَّ الرَّجُلُ يُحَمُّ فَهُوَ مَحْمُومٌ — أَصَابَتْهُ الْحُمَّى."))
put_morph(mo, "qasada", _sg.sound1("daraba", "قَصَد", "قْصِد", "اِقْصِد", "قَصْد", "قَاصِد", maful="مَقْصُود", pmz="قُصِدَ", pmd="يُقْصَدُ"))
put_morph(mo, "zahara", _sg.sound1("fataha", "ظَهَر", "ظْهَر", "اِظْهَر", "ظُهُور", "ظَاهِر", note="لَازِمٌ: ظَهَرَ يَظْهَرُ ظُهُورًا."))
put_morph(mo, "haka", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "حَكَ", "حْك", "i", "اِحْك", "حِكَايَة", "حَاكٍ (الْحَاكِي)", "مَحْكِيّ", "حُكِيَ", "يُحْكَى", note="حَكَى الشَّيْءَ: شَابَهَهُ — لَمْ يَحْكِ: جُزِمَ بِحَذْفِ الْيَاءِ."))
put_morph(mo, "raja", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "رَجَ", "رْج", "u", "اُرْج", "رَجَاء", "رَاجٍ (الرَّاجِي)", "مَرْجُوّ", "رُجِيَ", "يُرْجَى"))
put_morph(mo, "najja", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "نَجَّ", "نَجّ", "i", "نَجّ", "تَنْجِيَة", "مُنَجٍّ (الْمُنَجِّي)", "مُنَجًّى", "نُجِّيَ", "يُنَجَّى"))
put_morph(mo, "alhaqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَلْحَق", "لْحِق", "أَلْحِق", "إِلْحَاق", "مُلْحِق", "مُلْحَق", "أُلْحِقَ", "يُلْحَقُ"))
put_morph(mo, "bana", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "بَنَ", "بْن", "i", "اِبْن", "بِنَاء", "بَانٍ (الْبَانِي)", "مَبْنِيّ", "بُنِيَ", "يُبْنَى"))
put_morph(mo, "ghayyaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "غَيَّب", "غَيِّب", "غَيِّب", "تَغْيِيب", "مُغَيِّب", "مُغَيَّب", "غُيِّبَ", "يُغَيَّبُ"))
put_morph(mo, "raqaa", _sg.sound1("fataha", "رَقَأ", "رْقَأ", "اِرْقَأ", "رُقُوء", "رَاقِئ", note="مَهْمُوزُ اللَّامِ، لَازِمٌ: رَقَأَ الدَّمْعُ يَرْقَأُ — وَتُسَهَّلُ هَمْزَتُهُ فِي الشِّعْرِ: تَرْقَا."))
put_morph(mo, "athbata", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَثْبَت", "ثْبِت", "أَثْبِت", "إِثْبَات", "مُثْبِت", "مُثْبَت", "أُثْبِتَ", "يُثْبَتُ"))
put_morph(mo, "shafa", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "شَفَ", "شْف", "i", "اِشْف", "شِفَاء", "شَافٍ (الشَّافِي)", "مَشْفِيّ", "شُفِيَ", "يُشْفَى"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_H = {
 "id": "husn-al-talil",
 "title": {"ar": "حُسْنُ التَّعْلِيلِ — عِلَّةٌ لَطِيفَةٌ غَيْرُ حَقِيقِيَّةٍ تُدَّعَى لِوَصْفٍ", "en": "Husn al-taʿlil — a fine, unreal cause claimed for a quality", "tr": "Hüsn-i ta'lîl — bir vasfa iddia edilen latîf, gayr-i hakikî illet"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — حسن التعليل: أن يدعى لوصف علة مناسبة له باعتبار لطيف غير حقيقي؛ وهو أربعة أقسام، لأن الصفة إما ثابتة قصد بيان علتها أو غير ثابتة قصد إثباتها؛ والأولى إما أن لا يظهر لها في العادة علة أو يظهر لها علة غير المذكورة؛ والثانية إما ممكنة أو غير ممكنة؛ ويلحق به ما يبنى على الشك."],
 "question": {
  "en": ["Is a CAUSE given for a quality — a cause that is not the real one, but a fine fancy that suits it? Then it is HUSN AL-TAʿLIL.",
         "Is the quality FIXED, its cause the thing sought? Custom shows no cause at all (why does the cloud rain? — it caught a fever from your gift), or custom shows another cause (he spares his enemies — not from mercy, but so the wolves' hope is not disappointed).",
         "Is the quality UNFIXED, its very proving the aim? The claim may be possible (the slanderer's harm was good: fear of him saved my eye from drowning) or impossible (Gemini wears a belt because it meant to serve him). Built on DOUBT with كَأَنَّ, it is joined to the figure (as if the clouds had hidden a beloved).",
         "What does the engine read? The kind is the author's judgement — a DOC shortlist. The RECEIPT is on the surface: a negation answered by إِنَّمَا, the light لَكِنْ after a negation, a fresh cause-sentence after the quality, the unreal لَوْ with its لَ-answer, the doubting كَأَنَّ."],
  "tr": ["Bir vasfa bir İLLET mi veriliyor — hakikî değil, ona yakışan latîf bir hayal? O hâlde HÜSN-İ TA'LÎLDİR.",
         "Vasıf SABİT mi, aranan illeti mi? Âdet hiç illet göstermez (bulut niçin yağar? — ihsanından hummaya tutuldu), yahut âdet başka illet gösterir (düşmanlarını sağ bırakır — merhametten değil, kurtların umudu boşa çıkmasın diye).",
         "Vasıf SABİT DEĞİL mi, ispatı mı kastediliyor? İddia mümkün (gammazın zararı hayır oldu: ondan korkum gözümü boğulmaktan kurtardı) yahut imkânsız (Cevzâ kemer takar, çünkü ona hizmet niyetindeydi). كَأَنَّ ile ŞÜPHE üzerine kurulunca sanata katılır (sanki bulutlar bir sevgiliyi gizlemiş).",
         "Motor neyi okur? Kısım müellifin hükmüdür — DOC listesi. ALINDI yüzeydedir: إِنَّمَا ile cevaplanan nefiy, nefiyden sonra muhaffef لَكِنْ, vasıftan sonra müste'nef illet cümlesi, لَ-cevaplı gayr-i vâki لَوْ, şüphe veren كَأَنَّ."]},
 "plain": {
  "en": "Husn al-taʿlil claims a fine, unreal cause for a quality. Four kinds: the quality fixed with no customary cause, or with another cause; the quality unfixed and possible, or impossible. Doubt (كَأَنَّ) joins it. The engine reads the receipt: إِنَّمَا, لَكِنْ, a cause-sentence, لَوْ, كَأَنَّ.",
  "tr": "Hüsn-i ta'lîl bir vasfa latîf, gayr-i hakikî bir illet iddia eder. Dört kısım: vasıf sabit, âdette illetsiz yahut başka illetli; vasıf sabit değil, mümkün yahut imkânsız. Şüphe (كَأَنَّ) ona katılır. Motor alındıyı okur: إِنَّمَا, لَكِنْ, illet cümlesi, لَوْ, كَأَنَّ."},
 "explanation": {
  "en": "HUSN AL-TAʿLIL is أَنْ يُدَّعَى لِوَصْفٍ عِلَّةٌ مُنَاسِبَةٌ لَهُ بِاعْتِبَارٍ لَطِيفٍ غَيْرِ حَقِيقِيٍّ. Four kinds. (1) The quality FIXED, custom showing no cause: لَمْ يَحْكِ نَائِلَكَ السَّحَابُ وَإِنَّمَا حُمَّتْ بِهِ فَصَبِيبُهَا الرُّحَضَاءُ — the rain has no customary cause; the poet gives it one: the cloud's fever from your bounty. (2) The quality fixed, custom showing ANOTHER cause: مَا بِهِ قَتْلُ أَعَادِيهِ وَلَكِنْ يَتَّقِي إِخْلَافَ مَا تَرْجُو الذِّئَابُ — the customary cause of killing enemies is to repel their harm; the poet's cause is the wolves' hope. (3) The quality UNFIXED and possible: يَا وَاشِيًا حَسُنَتْ فِينَا إِسَاءَتُهُ نَجَّى حِذَارُكَ إِنْسَانِي مِنَ الْغَرَقِ — that the slanderer's harm was good is possible; the poet proves it by the fear that saved his eye from tears. (4) Unfixed and IMPOSSIBLE: لَوْ لَمْ تَكُنْ نِيَّةُ الْجَوْزَاءِ خِدْمَتَهُ لَمَا رَأَيْتَ عَلَيْهَا عِقْدَ مُنْتَطِقٍ — Gemini's belt of stars is given a cause that cannot be. What is built on DOUBT is joined to it: كَأَنَّ السَّحَابَ الْغُرَّ غَيَّبْنَ تَحْتَهَا حَبِيبًا فَمَا تَرْقَا لَهُنَّ مَدَامِعُ. The reader's card draws the QUALITY and the CLAIMED CAUSE with the arrow between them and lights the receipt-word.",
  "tr": "HÜSN-İ TA'LÎL أَنْ يُدَّعَى لِوَصْفٍ عِلَّةٌ مُنَاسِبَةٌ لَهُ بِاعْتِبَارٍ لَطِيفٍ غَيْرِ حَقِيقِيٍّ'dir. Dört kısım. (1) Vasıf SABİT, âdet illet göstermez: لَمْ يَحْكِ نَائِلَكَ السَّحَابُ وَإِنَّمَا حُمَّتْ بِهِ فَصَبِيبُهَا الرُّحَضَاءُ — yağmurun âdette illeti yoktur; şair bir illet bulur: bulutun ihsanından tuttuğu humma. (2) Vasıf sabit, âdet BAŞKA illet gösterir: مَا بِهِ قَتْلُ أَعَادِيهِ وَلَكِنْ يَتَّقِي إِخْلَافَ مَا تَرْجُو الذِّئَابُ — düşman öldürmenin âdetteki illeti zararı defetmektir; şairin illeti kurtların umudu. (3) Vasıf SABİT DEĞİL ve mümkün: يَا وَاشِيًا حَسُنَتْ فِينَا إِسَاءَتُهُ نَجَّى حِذَارُكَ إِنْسَانِي مِنَ الْغَرَقِ — gammazın zararının hayır olması mümkündür; şair bunu gözünü yaşlardan kurtaran korkuyla ispat eder. (4) Sabit değil ve İMKÂNSIZ: لَوْ لَمْ تَكُنْ نِيَّةُ الْجَوْزَاءِ خِدْمَتَهُ لَمَا رَأَيْتَ عَلَيْهَا عِقْدَ مُنْتَطِقٍ — Cevzâ'nın yıldız kemerine olamayacak bir illet verilir. ŞÜPHE üzerine kurulan ona katılır: كَأَنَّ السَّحَابَ الْغُرَّ غَيَّبْنَ تَحْتَهَا حَبِيبًا فَمَا تَرْقَا لَهُنَّ مَدَامِعُ. Okuyucunun kartı VASFI ve İDDİA EDİLEN İLLETİ aralarındaki okla çizer ve alındı kelimesini yakar."},
 "examples": [
  {"ar": "لَمْ يَحْكِ نَائِلَكَ السَّحَابُ وَإِنَّمَا * حُمَّتْ بِهِ فَصَبِيبُهَا الرُّحَضَاءُ", "en": "al-Mutanabbi — fixed, no customary cause.", "tr": "Mütenebbî — sabit, âdette illetsiz.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "مَا بِهِ قَتْلُ أَعَادِيهِ وَلَكِنْ * يَتَّقِي إِخْلَافَ مَا تَرْجُو الذِّئَابُ", "en": "al-Mutanabbi — fixed, another cause.", "tr": "Mütenebbî — sabit, başka illet.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "يَا وَاشِيًا حَسُنَتْ فِينَا إِسَاءَتُهُ * نَجَّى حِذَارُكَ إِنْسَانِي مِنَ الْغَرَقِ", "en": "Muslim b. al-Walid — unfixed, possible.", "tr": "Müslim b. Velîd — sabit değil, mümkün.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "لَوْ لَمْ تَكُنْ نِيَّةُ الْجَوْزَاءِ خِدْمَتَهُ * لَمَا رَأَيْتَ عَلَيْهَا عِقْدَ مُنْتَطِقٍ", "en": "the author, from Persian — unfixed, impossible.", "tr": "müellif, Farsçadan — sabit değil, imkânsız.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "كَأَنَّ السَّحَابَ الْغُرَّ غَيَّبْنَ تَحْتَهَا * حَبِيبًا فَمَا تَرْقَا لَهُنَّ مَدَامِعُ", "en": "Abu Tammam — built on doubt.", "tr": "Ebû Temmâm — şüphe üzerine.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"}],
 "commonMistakes": [
  {"wrong": "«لَمْ يَحْكِ نَائِلَكَ السَّحَابُ yalnız bir mübalağadır: bulut ihsanına yetişemez»",
   "right": "«Mübalağa da var, fakat sanat hüsn-i ta'lîldir: yağmura hakikî olmayan bir illet — humma teri — iddia edilmiştir»",
   "why": {"en": "The figure is named by the CAUSE claimed, not by the size of the claim.", "tr": "Sanat iddianın büyüklüğüyle değil, iddia edilen İLLETLE adlandırılır."}}],
 "relatedNotes": ["mubalagha-maqbula", "innama-kaffa", "in-shartiyya", "inna-wa-akhawatuha", "lam-taleel", "ilm-al-badi"]}

NOTE_F = {
 "id": "tafri",
 "title": {"ar": "التَّفْرِيعُ — حُكْمٌ لِمُتَعَلِّقٍ بَعْدَ إِثْبَاتِهِ لِمُتَعَلِّقٍ آخَرَ", "en": "Tafriʿ — a ruling for one dependent after it is proved for another", "tr": "Tefrî' — bir müteallike hüküm, başka bir müteallike ispatından sonra"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التفريع: أن يثبت لمتعلق أمر حكم بعد إثباته لمتعلق له آخر، كقوله: أحلامكم لسقام الجهل شافية * كما دماؤكم تشفي من الكلب."],
 "question": {
  "en": ["Are TWO dependents of one thing given ONE ruling, the second branched off the first with كَمَا? Then it is TAFRIʿ.",
         "Al-Kumayt on the Prophet's house: their MINDS heal the sickness of ignorance — كَمَا — their BLOOD heals rabies. Minds and blood belong to one house; healing is proved for the first, then branched to the second.",
         "What does the engine read? The كَمَا hinge, a subject-and-predicate on each side of it, and the SAME ROOT in both predicates (شَافِيَةٌ / تَشْفِي)."],
  "tr": ["Bir şeyin İKİ müteallikine TEK hüküm mü veriliyor, ikincisi كَمَا ile birincisinden dallandırılarak? O hâlde TEFRÎ'DİR.",
         "Kümeyt Ehl-i Beyt hakkında: AKILLARI cehalet hastalığına şifadır — كَمَا — KANLARI kuduza şifa verir. Akıl ve kan tek hanedanındır; şifa önce birine ispat edilir, sonra öbürüne dallandırılır.",
         "Motor neyi okur? كَمَا menteşesini, iki yanında birer mübtedâ-haber ve iki yüklemde AYNI KÖKÜ (شَافِيَةٌ / تَشْفِي)."]},
 "plain": {
  "en": "Tafriʿ proves one ruling for a second dependent of a thing after proving it for the first — al-Kumayt's minds that heal ignorance as their blood heals rabies. The engine reads the كَمَا hinge and the shared root of the two predicates.",
  "tr": "Tefrî', bir şeyin ikinci müteallikine, birincisine ispat ettikten sonra aynı hükmü ispat eder — Kümeyt'in cehaleti iyileştiren akılları, kuduzu iyileştiren kanları gibi. Motor كَمَا menteşesini ve iki yüklemin ortak kökünü okur."},
 "explanation": {
  "en": "TAFRIʿ is أَنْ يُثْبَتَ لِمُتَعَلِّقِ أَمْرٍ حُكْمٌ بَعْدَ إِثْبَاتِهِ لِمُتَعَلِّقٍ لَهُ آخَرَ. Al-Kumayt: أَحْلَامُكُمْ لِسَقَامِ الْجَهْلِ شَافِيَةٌ كَمَا دِمَاؤُكُمْ تَشْفِي مِنَ الْكَلَبِ — the thing is the Prophet's house; its two dependents are their minds and their blood; the ruling is healing. The first predication (أَحْلَامُكُمْ … شَافِيَةٌ) is the branch, the second (دِمَاؤُكُمْ تَشْفِي) the root it is branched from, and كَمَا is the hinge. The card draws the two predications one above the other with the hinge between them.",
  "tr": "TEFRÎ' أَنْ يُثْبَتَ لِمُتَعَلِّقِ أَمْرٍ حُكْمٌ بَعْدَ إِثْبَاتِهِ لِمُتَعَلِّقٍ لَهُ آخَرَ'dir. Kümeyt: أَحْلَامُكُمْ لِسَقَامِ الْجَهْلِ شَافِيَةٌ كَمَا دِمَاؤُكُمْ تَشْفِي مِنَ الْكَلَبِ — şey Ehl-i Beyt; iki mütealliki akılları ve kanları; hüküm şifa. İlk isnad (أَحْلَامُكُمْ … شَافِيَةٌ) dal, ikincisi (دِمَاؤُكُمْ تَشْفِي) dallandığı kök, كَمَا menteşedir. Kart iki isnadı alt alta, aralarında menteşeyle çizer."},
 "examples": [
  {"ar": "أَحْلَامُكُمْ لِسَقَامِ الْجَهْلِ شَافِيَةٌ * كَمَا دِمَاؤُكُمْ تَشْفِي مِنَ الْكَلَبِ", "en": "al-Kumayt — tafriʿ.", "tr": "Kümeyt — tefrî'.", "sourceStory": "talkhis-al-miftah", "sentence": "s14"}],
 "commonMistakes": [
  {"wrong": "«كَمَا دِمَاؤُكُمْ تَشْفِي bir teşbihtir: akıl kana benzetilmiştir»",
   "right": "«Teşbih değil, tefrî'dir: aynı hüküm (şifa) ikinci müteallike de ispat edilmektedir; كَمَا burada iki hükmü bağlar»",
   "why": {"en": "The ka does not liken two things; it branches one ruling to a second dependent.", "tr": "Kâf iki şeyi benzetmez; tek hükmü ikinci müteallike dallandırır."}}],
 "relatedNotes": ["husn-al-talil", "tashbih", "mubtada-khabar", "ilm-al-badi"]}

ADD_EN = (" Chapter 65 (lines ~4250-4300, sahifa 146-147) carries husn al-taʿlil (al-Mutanabbi s4 and s6, Muslim b. al-Walid s8, the author's bayt from Persian s10, "
          "Abu Tammam s12) and tafriʿ (al-Kumayt s14). The definitions and the kinds' headings (s1-s3, s5, s7, s9, s11, s13) and the citation frame of s10 are "
          "RESTORED: the source carries them only in Turkish, and the Arabic is the received matn of the Talkhis; every restored sentence is marked «Restored» in its "
          "translation. Two readings follow the received text against the print: الرُّحَضَاءُ (fever-sweat; the print has الرُّخَصَاءُ) and كَأَنَّ السَّحَابَ الْغُرَّ "
          "(the print writes كَأَنَّمَا yet marks the noun accusative). The examples carry `badi` frames (husn-talil with its kind as `sub`, its `receipt`, the "
          "claimed cause as `word` and the quality as `companion`; tafri with the hinge `word` and the two predications as `first`/`second`).")
ADD_TR = (" Altmış beşinci bâb (satır ~4250-4300, sahife 146-147) hüsn-i ta'lîli (Mütenebbî s4 ve s6, Müslim b. Velîd s8, müellifin Farsçadan beyti s10, Ebû Temmâm s12) "
          "ve tefrî'i (Kümeyt s14) taşır. Tarifler ve kısım başlıkları (s1-s3, s5, s7, s9, s11, s13) ile s10'un iktibas çerçevesi GERİ YAZILMIŞTIR: kaynak bunları "
          "yalnız Türkçe taşır; Arapça, Telhîs'in alınan metnidir. Her geri yazılmış cümle tercümesinde «geri yazılmıştır» diye işaretlidir. İki okuyuş baskıya karşı "
          "alınan metni izler: الرُّحَضَاءُ (humma teri; baskıda الرُّخَصَاءُ) ve كَأَنَّ السَّحَابَ الْغُرَّ (baskı كَأَنَّمَا yazar, fakat ismi mansûb harekeler). "
          "Örnekler `badi` çerçeveleri taşır (hüsn-i ta'lîl: kısmı `sub`, alındısı `receipt`, iddia edilen illet `word`, vasıf `companion`; tefrî': menteşe `word`, "
          "iki isnad `first`/`second`).")
write_out(65, S, TITLE, ADD_EN, ADD_TR, "4250-4300", GLOSS_ADD, notes=(NOTE_H, NOTE_F),
          related=(("mubalagha-maqbula", ["husn-al-talil"]), ("ilm-al-badi", ["husn-al-talil", "tafri"]), ("innama-kaffa", ["husn-al-talil"]), ("in-shartiyya", ["husn-al-talil"])))
report(65, S, GLOSS_ADD, (NOTE_H, NOTE_F))
