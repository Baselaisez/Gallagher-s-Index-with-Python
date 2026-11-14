# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 75: what attaches to the takings — the IQTIBAS (Qurʾan or hadith woven in, not as such; its two kinds; the small change
allowed), the TADMIN (another's verse woven in, flagged unless famous; the finest adds a point; istiʿana / idaʿ and rafw), the ʿAQD (prose versified
not by way of iqtibas), the HALL (verse turned to prose) and the TALMIH (a story or verse pointed at, unnamed). Source lines ~4750-4820 (sahifa 164-166).

  RESTORED (the source carries the rulings only in Turkish): s1, s2, s4, s9, s10, s12, s14, s16, s19, s20, s22, s24, s25 — the received matn, marked.
  The Qurʾanic and hadith text prints as the source prints it; two misprints of the Ottoman print are corrected and recorded: خُفَّتْ → حُفَّتْ (s8,
  the received hadith), and ذِي restored in بِوَادٍ غَيْرِ ذِي زَرْعٍ (s11, the aya and the metre both require it).

  python3 tools/authoring/author_talkhis_ch75.py
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

K = "al-iqtibas-wal-tadmin"
A = "ilm-al-arud"
QF = "al-qafiya"
TITLE = {"ar": "الِاقْتِبَاسُ وَالتَّضْمِينُ وَالْعَقْدُ وَالْحَلُّ وَالتَّلْمِيحُ", "en": "The iqtibas, the tadmin, the ʿaqd, the hall and the talmih", "tr": "İktibas, tazmin, akd, hal ve telmih"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the source gives this ruling only in Turkish; this is the received matn of the Talkhis.)"
R_TR = " (Geri yazım: kaynak bu hükmü yalnız Türkçe verir; bu, Telhîs'in alınan metnidir.)"

def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)
def span(sen, first, last):
    a, b = ix(sen, first), ix(sen, last); return list(range(a, b + 1))
def fi(tag, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
def ka_qawl(name_toks, tag=None, wa=False):
    full = "وَكَقَوْلِ" if wa else "كَقَوْلِ"
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun")]
    return [tok(full, "qawl", "noun", [tag or K, "huruf-jarr", "idafa-definiteness"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، مُضَافٌ.", "«as the saying of».", "«… sözü gibi».", segments=segs)] + name_toks
def name1(full, lex, en, tr, tags=()): return [tok(full, lex, "propn", [K, "idafa-definiteness"] + list(tags), "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", en, tr, punct=":")]
def abu(second_full, second_lex, en2, tr2, note_ar):
    return [tok("أَبِي", "ab", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
            tok(second_full, second_lex, "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — " + note_ar, en2, tr2, punct=":")]
def ibn(second_full, second_lex, en2, tr2, note_ar):
    return [tok("ابْنِ", "ibn", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«Ibn».", "«İbn»."),
            tok(second_full, second_lex, "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — " + note_ar, en2, tr2, punct=":")]
def IQ(sub, ids, source, kind2="ghayr-manqul", changed=False):
    d = {"kind": "iqtibas", "sub": sub, "set": ids, "source": source, "kind2": kind2}
    if changed: d["kind2"] = "ghayr-manqul"
    return d

# ----------- s1 — what attaches to the takings (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "And of what attaches to the takings: the discourse on the IQTIBAS, the TADMIN, the ʿAQD, the HALL and the TALMIH." + R_EN,
 "tr": "Sirkatlere bitişenlerden: İKTİBAS, TAZMİN, AKD, HAL ve TELMİH üzerine söz." + R_TR},
 "tokens": [
  tok("وَمِمَّا", "min", "prep", [K, "huruf-jarr", "ism-mawsul", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنْ حَرْفُ جَرٍّ أُدْغِمَتْ نُونُهُ فِي مَا الْمَوْصُولَةِ — خَبَرٌ مُقَدَّمٌ.", "«and of what» — min + ma, the fronted khabar.", "«ve … şeylerden» — min + mâ, öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "noun")]),
  tok("يَتَّصِلُ", "ittasala", "verb", [K, "ism-mawsul", "form-viii-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةُ مَا.", "«attaches» — the sila.", "«bitişen» — sıla."),
  tok("بِالسَّرِقَاتِ", "sariqa", "noun", [K, "huruf-jarr", "jam-muannath-salim"], "الْبَاءُ حَرْفُ جَرٍّ، وَالسَّرِقَاتِ مَجْرُورٌ — جَمْعُ سَرِقَةٍ.", "«to the takings».", "«sirkatlere».", segments=[seg("بِ", "bi", "prep"), seg("السَّرِقَاتِ", "sariqa", "noun")]),
  tok("الشِّعْرِيَّةِ", "shiri", "noun", [K, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — نِسْبَةٌ إِلَى الشِّعْرِ.", "«poetic» — the nisba.", "«şiirle ilgili» — nisbe.", punct=":"),
  tok("الْقَوْلُ", "qawl", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the discourse» — the delayed mubtada.", "«söz» — sona bırakılmış mübtedâ."),
  tok("فِي", "fi", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  tok("الِاقْتِبَاسِ", "iqtibas", "noun", [K, "huruf-jarr", "masdar", "form-viii-verbs"], "مَجْرُورٌ — مَصْدَرُ اقْتَبَسَ: أَخَذَ قَبَسًا مِنَ النَّارِ.", "«the iqtibas» — the masdar of Form VIII: taking a brand from the fire.", "«iktibas» — iftiâl masdarı: ateşten kor alma."),
  tok("وَالتَّضْمِينِ", "tadmin", "noun", [K, "atf-nasaq", "masdar", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَالتَّضْمِينِ مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ ضَمَّنَ.", "«and the tadmin».", "«ve tazmin».", segments=[seg("وَ", "wa", "conj"), seg("التَّضْمِينِ", "tadmin", "noun")]),
  tok("وَالْعَقْدِ", "aqd", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالْعَقْدِ مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ عَقَدَ.", "«and the ʿaqd».", "«ve akd».", segments=[seg("وَ", "wa", "conj"), seg("الْعَقْدِ", "aqd", "noun")]),
  tok("وَالْحَلِّ", "hall-nathr", "noun", [K, "atf-nasaq", "masdar", "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَالْحَلِّ مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ حَلَّ.", "«and the hall».", "«ve hal».", segments=[seg("وَ", "wa", "conj"), seg("الْحَلِّ", "hall-nathr", "noun")]),
  tok("وَالتَّلْمِيحِ", "talmih", "noun", [K, "atf-nasaq", "masdar", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَالتَّلْمِيحِ مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ لَمَّحَ.", "«and the talmih».", "«ve telmih».", segments=[seg("وَ", "wa", "conj"), seg("التَّلْمِيحِ", "talmih", "noun")], punct="."),
 ]})

# ----------- s2 — the iqtibas defined (RESTORED) + al-Hariri
S.append({"id": "s2", "translation": {
 "en": "The iqtibas: that the speech be made to carry something of the Qurʾan or the hadith, not as being from it — in prose or in verse — as the saying of al-Hariri:" + R_EN,
 "tr": "İktibas: söze, ondan olduğu belirtilmeden, Kur'ân'dan yahut hadisten bir şey katılmasıdır — nesirde de nazımda da — Harîrî'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("فَالِاقْتِبَاسُ", "iqtibas", "noun", [K, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالِاقْتِبَاسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the iqtibas».", "«iktibas».", segments=[seg("فَ", "fa", "conj"), seg("الِاقْتِبَاسُ", "iqtibas", "noun")], punct=":"),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that» — the khabar.", "«-sıdır» — haber."),
  tok("يُضَمَّنَ", "dammana", "verb", [K, "an-masdariyya", "naib-al-fail", "form-ii-verbs", "mafulayn"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ — ضَمَّنَ الشَّيْءَ الشَّيْءَ: جَعَلَهُ يَتَضَمَّنُهُ.", "«be made to carry» — Form II passive, two objects.", "«taşıtılması» — tef'îl meçhûlü, iki mef'ûl."),
  tok("الْكَلَامُ", "kalam", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the speech».", "«söz»."),
  tok("شَيْئًا", "shay", "noun", [K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«something» — the second object.", "«bir şey» — ikinci mef'ûl."),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — فُتِحَتْ نُونُهُ قَبْلَ لَامِ التَّعْرِيفِ.", "«of».", "«-den»."),
  tok("الْقُرْآنِ", "quran", "propn", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the Qurʾan».", "«Kur'ân»."),
  tok("أَوِ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ — كُسِرَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — its waw takes kasra before the article.", "«yahut» — vâvı iki sâkin yüzünden kesre."),
  tok("الْحَدِيثِ", "hadith", "noun", [K, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«the hadith».", "«hadis»."),
  tok("لَا", "la-nafiya", "part", [K], "حَرْفُ نَفْيٍ.", "«not».", "«değil»."),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«as».", "«… olarak»."),
  tok("أَنَّهُ", "anna", "part", [K, "inna-am-anna", "huruf-jarr"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ مَجْرُورٌ بِعَلَى.", "«that it».", "«onun».", segments=[seg("أَنَّ", "anna", "part"), pr3ms()]),
  tok("مِنْهُ", "min", "prep", [K, "huruf-jarr", "inna-am-anna"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرُ أَنَّ.", "«is from it» — anna's khabar.", "«ondandır» — ennenin haberi.", segments=[seg("مِنْ", "min", "prep"), pr3ms()], punct="،"),
  tok("نَثْرًا", "nathr", "noun", [K, "kana-wa-akhawatuha", "masdar"], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ.", "«prose» — kana's fronted khabar.", "«nesir» — kânenin öne alınmış haberi."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — أَيِ الْكَلَامُ.", "«it be» — the speech.", "«olsun» — söz."),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("شِعْرًا", "shir", "noun", [K, "atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«verse».", "«nazım».", punct="،"),
 ] + ka_qawl(name1("الْحَرِيرِيِّ", "hariri", "«al-Hariri» — the author of the Maqamat (d. 516 AH).", "«Harîrî» — Makâmât'ın yazarı (ö. 516)."))})

# ----------- s3 — al-Hariri (prose): كَلَمْحِ الْبَصَرِ أَوْ هُوَ أَقْرَبُ
S.append({"id": "s3", "translation": {
 "en": "«And it was but as the twinkling of an eye, or nearer — until he recited and did strangely» — «as the twinkling of an eye, or nearer» is taken from the Qurʾan (al-Nahl 77).",
 "tr": "«Göz açıp kapayıncaya kadar yahut daha az bir zamandı — şiir söyleyip garip kılana kadar» — «göz açıp kapayıncaya kadar yahut daha az» Kur'ân'dan (Nahl 77) alınmıştır."},
 "tokens": [
  tok("فَلَمْ", "lam", "part", [K, "lam-jazim"], "الْفَاءُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ.", "«and … not».", "«ve … -medi».", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam", "part")]),
  tok("يَكُنْ", "kana", "verb", [K, "lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَجْزُومٌ، وَاسْمُهُ مُسْتَتِيرٌ.", "«it was».", "«idi»."),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ حَصْرٍ — اسْتِثْنَاءٌ مُفَرَّغٌ.", "«but» — the emptied exception.", "«ancak» — müferrağ istisnâ."),
  tok("كَلَمْحِ", "lamh", "noun", [K, "huruf-jarr", "idafa-definiteness", "kana-wa-akhawatuha", "masdar"], "الْكَافُ حَرْفُ جَرٍّ، وَلَمْحِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُنْ.", "«as the twinkling of» — the khabar.", "«… gibi» — haber.", segments=[seg("كَ", "ka", "part"), seg("لَمْحِ", "lamh", "noun")]),
  tok("الْبَصَرِ", "basar", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«an eye».", "«gözün»."),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("هُوَ", "huwa", "pron", [K, "mubtada-khabar"], "مُبْتَدَأٌ.", "«it».", "«o»."),
  tok("أَقْرَبُ", "aqrab", "noun", [K, "mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ. وَالْجُمْلَةُ مَعْطُوفَةٌ.", "«nearer».", "«daha yakın».", punct="،"),
  tok("حَتَّى", "hatta", "part", [K, "huruf-jarr"], "حَرْفُ غَايَةٍ وَابْتِدَاءٍ.", "«until».", "«-e kadar»."),
  tok("أَنْشَدَ", "anshada", "verb", [K, "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنْشَدَ الشِّعْرَ: قَرَأَهُ.", "«he recited».", "«şiir okudu»."),
  tok("وَأَغْرَبَ", "aghraba", "verb", [K, "atf-nasaq", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَغْرَبَ فِعْلٌ مَاضٍ — أَتَى بِالْغَرِيبِ.", "«and did strangely» — brought the rare.", "«ve garip kıldı».", segments=[seg("وَ", "wa", "conj"), seg("أَغْرَبَ", "aghraba", "verb")], punct="."),
 ]})
S[-1]["badi"] = [IQ("quran", span(S[-1], "كَلَمْحِ", "أَقْرَبُ"), "النَّحْل ٧٧")]

# ----------- s4 — Abu l-Qasim (RESTORED)
S.append({"id": "s4", "translation": {"en": "And as the saying of Abu l-Qasim:" + R_EN, "tr": "Ve Ebü'l-Kâsım'ın şu sözü gibi:" + R_TR},
 "tokens": ka_qawl(abu("الْقَاسِمِ", "qasim", "«l-Qasim» — Abu l-Qasim, the poet the Talkhis cites here.", "«l-Kâsım» — Telhîs'in burada andığı şair Ebü'l-Kâsım.", "أَبُو الْقَاسِمِ."), wa=True)})
S.append({"id": "s5", "translation": {
 "en": "«If you have resolved on forsaking us * for no crime at all — then fair patience» (sarīʿ) — «then fair patience» is from the Qurʾan (Yusuf 83).",
 "tr": "«Hiçbir suç olmaksızın * bizi terke karar verdiysen — güzel bir sabır» (serî') — «güzel bir sabır» Kur'ân'dandır (Yûsuf 83)."},
 "tokens": [
  tok("إِنْ", "in-shartiyya", "part", [K, A, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("كُنْتِ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ الْمَكْسُورَةُ اسْمُهُ — لِلْمُخَاطَبَةِ.", "«you (f.) have» — the kasra: a woman addressed.", "«sen (dişil)» — kesre: muhâtaba.", segments=[seg("كُنْ", "kana", "verb"), seg("تِ", "pron-2fs", "pron")]),
  tok("أَزْمَعْتِ", "azmaa", "verb", [K, "kana-wa-akhawatuha", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — خَبَرُ كُنْتِ؛ أَزْمَعَ الْأَمْرَ: عَزَمَ عَلَيْهِ.", "«resolved» — kana's khabar.", "«karar verdin» — kânenin haberi.", segments=[seg("أَزْمَعْ", "azmaa", "verb"), seg("تِ", "pron-2fs", "pron")]),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  tok("هَجْرِنَا", "hajr", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«forsaking us».", "«bizi terk».", segments=[seg("هَجْرِ", "hajr", "noun"), pr1p()], punct="*"),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  tok("غَيْرِ", "ghayr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«no».", "«olmaksızın»."),
  tok("مَا", "ma-zaida", "part", [K, "hadhf-wa-taqdir"], "زَائِدَةٌ لِلتَّوْكِيدِ — مِنْ غَيْرِ مَا جُرْمٍ: مِنْ غَيْرِ جُرْمٍ.", "«at all» — the extra ma.", "«hiç» — zâid mâ."),
  tok("جُرْمٍ", "jurm", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«crime».", "«suç»."),
  tok("فَصَبْرٌ", "sabr", "noun", [K, "in-shartiyya", "mubtada-khabar", "hadhf-wa-taqdir"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَصَبْرٌ مُبْتَدَأٌ مَرْفُوعٌ خَبَرُهُ مَحْذُوفٌ: فَأَمْرِي صَبْرٌ جَمِيلٌ.", "«then patience» — the jawab; a mubtada whose khabar is dropped.", "«o hâlde sabır» — cevap; haberi mahzûf mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("صَبْرٌ", "sabr", "noun")]),
  tok("جَمِيلٌ", "jamil", "noun", [K, QF, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ. الرَّوِيُّ اللَّامُ.", "«fair» — rhyme: rawi lam.", "«güzel» — kafiye: revî lâm."),
 ]})
S[-1]["badi"] = [IQ("quran", span(S[-1], "فَصَبْرٌ", "جَمِيلٌ"), "يُوسُف ٨٣")]
S.append({"id": "s6", "translation": {
 "en": "«And if you have exchanged us for another * — then God is sufficient for us, and excellent the Trustee» — from the Qurʾan (Al ʿImran 173).",
 "tr": "«Ve bizi başkasıyla değiştirdiysen * — Allah bize yeter, ne güzel vekildir» — Kur'ân'dandır (Âl-i İmrân 173)."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, A, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("تَبَدَّلْتِ", "tabaddala", "verb", [K, "in-shartiyya", "form-v-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ فَاعِلٌ — تَبَدَّلَ بِهِ غَيْرَهُ: أَخَذَهُ بَدَلَهُ.", "«you have exchanged».", "«değiştirdin».", segments=[seg("تَبَدَّلْ", "tabaddala", "verb"), seg("تِ", "pron-2fs", "pron")]),
  tok("بِنَا", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَا مَجْرُورٌ.", "«us».", "«bizi».", segments=[seg("بِ", "bi", "prep"), pr1p()]),
  tok("غَيْرَنَا", "ghayr", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«for another than us».", "«bizden başkasıyla».", segments=[seg("غَيْرَ", "ghayr", "noun"), pr1p()], punct="*"),
  tok("فَحَسْبُنَا", "hasb", "noun", [K, "in-shartiyya", "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَحَسْبُ مُبْتَدَأٌ مَرْفُوعٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«then our sufficiency» — the mubtada.", "«bize yeten» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("حَسْبُ", "hasb", "noun"), pr1p()]),
  tok("اللهُ", "allah", "propn", [K, "mubtada-khabar"], "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ.", "«is God».", "«Allah'tır»."),
  tok("وَنِعْمَ", "nima-verb", "verb", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَنِعْمَ فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ.", "«and excellent is» — the verb of praise.", "«ve ne güzeldir» — medih fiili.", segments=[seg("وَ", "wa", "conj"), seg("نِعْمَ", "nima-verb", "verb")]),
  tok("الْوَكِيلْ", "wakil", "noun", [K, QF, "fail"], "فَاعِلُ نِعْمَ مَرْفُوعٌ، سُكِّنَ لِلْقَافِيَةِ — وَالْمَخْصُوصُ بِالْمَدْحِ مَحْذُوفٌ: اللهُ. الرَّوِيُّ اللَّامُ.", "«the Trustee» — the doer of niʿma, its vowel stilled for the rhyme.", "«vekil» — ni'me'nin fâili, kafiye için sâkin.", "«vekil»."),
 ]})
S[-1]["badi"] = [IQ("quran", span(S[-1], "فَحَسْبُنَا", "الْوَكِيلْ"), "آل عِمْرَان ١٧٣")]

# ----------- s7 — al-Hariri (prose): شَاهَتِ الْوُجُوهُ — from the hadith
S.append({"id": "s7", "translation": {
 "en": "And as al-Hariri's: «We said: may the faces be disfigured, and ugly be the base one and whoever hopes in him» — «may the faces be disfigured» is taken from the hadith.",
 "tr": "Ve Harîrî'nin: «Dedik ki: yüzler çirkinleşsin, alçak ve ondan umanlar kötü olsun» sözü gibi — «yüzler çirkinleşsin» hadisten alınmıştır."},
 "tokens": ka_qawl(name1("الْحَرِيرِيِّ", "hariri", "«al-Hariri».", "«Harîrî»."), wa=True) + [
  tok("قُلْنَا", "qala", "verb", [K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ.", "«we said».", "«dedik».", segments=[seg("قُلْ", "qala", "verb"), pr1p()], punct=":"),
  tok("شَاهَتِ", "shaha", "verb", [K, "hollow-verbs", "insha-wa-tamanni"], "فِعْلٌ مَاضٍ فِي مَعْنَى الدُّعَاءِ، وَالتَّاءُ لِلتَّأْنِيثِ كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — شَاهَ الْوَجْهُ: قَبُحَ.", "«may … be disfigured» — a mazi as a curse.", "«çirkinleşsin» — dua manasında mâzî."),
  tok("الْوُجُوهُ", "wajh", "noun", [K, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ وَجْهٍ.", "«the faces».", "«yüzler»."),
  tok("وَقُبِحَ", "qabuha", "verb", [K, "atf-nasaq", "naib-al-fail"], "الْوَاوُ عَاطِفَةٌ، وَقُبِحَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَعْنَى الدُّعَاءِ.", "«and ugly be».", "«ve kötü olsun».", segments=[seg("وَ", "wa", "conj"), seg("قُبِحَ", "qabuha", "verb")]),
  tok("اللُّكَعُ", "luka", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — اللُّكَعُ: اللَّئِيمُ.", "«the base one».", "«alçak»."),
  tok("وَمَنْ", "man", "noun", [K, "atf-nasaq", "ism-mawsul"], "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and whoever».", "«ve … kimse».", segments=[seg("وَ", "wa", "conj"), seg("مَنْ", "man", "noun")]),
  tok("يَرْجُوهُ", "raja", "verb", [K, "ism-mawsul", "naqis-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْهَاءُ مَفْعُولٌ — صِلَةٌ.", "«hopes in him».", "«ondan uman».", segments=[seg("يَرْجُو", "raja", "verb"), pr3ms()], punct="."),
 ]})
S[-1]["badi"] = [IQ("hadith", span(S[-1], "شَاهَتِ", "الْوُجُوهُ"), "حَدِيث")]

# ----------- s8 — Ibn ʿAbbad: الْجَنَّةُ حُفَّتْ بِالْمَكَارِهِ
S.append({"id": "s8", "translation": {
 "en": "And as Ibn ʿAbbad's: «He said to me: my watcher is ill-natured, so humour him. * I said: leave me — your face is the Garden, hedged about with hateful things» (kāmil) — «the Garden is hedged with hateful things» is from the hadith.",
 "tr": "Ve İbn Abbâd'ın: «Bana dedi: bekçim kötü huyludur, onu idare et. * Dedim: bırak beni — yüzün cennettir, hoşa gitmeyenlerle çevrili» (kâmil) sözü gibi — «cennet hoşa gitmeyenlerle çevrilidir» hadistendir."},
 "tokens": ka_qawl(ibn("عَبَّادٍ", "abbad", "«ʿAbbad» — al-Sahib b. ʿAbbad, the Buyid vizier (d. 385 AH).", "«Abbâd» — Büveyhî veziri Sâhib b. Abbâd (ö. 385).", "الصَّاحِبُ بْنُ عَبَّادٍ."), wa=True) + [
  tok("قَالَ", "qala", "verb", [K, A, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«he said».", "«dedi»."),
  tok("لِي", "li", "prep", [K, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ.", "«to me».", "«bana».", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  tok("إِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«şüphesiz»."),
  tok("رَقِيبِي", "raqib", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness", "ya-al-mutakallim"], "اسْمُ إِنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my watcher» — inna's ism, the case hidden by «my».", "«bekçim» — innenin ismi.", segments=[seg("رَقِيبِ", "raqib", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("سَيِّئُ", "sayyi", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ إِنَّ مَرْفُوعٌ، مُضَافٌ.", "«ill of» — inna's khabar.", "«kötü …-lu» — innenin haberi."),
  tok("الْخُلْقِ", "khuluq", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«nature».", "«huy»."),
  tok("فَدَارِهِ", "dara-iii", "verb", [K, "atf-nasaq", "form-iii-verbs", "naqis-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَدَارِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ الْيَاءِ، وَالْهَاءُ مَفْعُولٌ — دَارَى: لَاطَفَ.", "«so humour him» — the amr of the naqis Form III.", "«onu idare et» — nâkıs mufâalenin emri.", segments=[seg("فَ", "fa", "conj"), seg("دَارِ", "dara-iii", "verb"), pr3msi()], punct="*"),
  tok("قُلْتُ", "qala", "verb", [K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I said».", "«dedim».", segments=[seg("قُلْ", "qala", "verb"), seg("تُ", "pron-1s", "pron")], punct=":"),
  tok("دَعْنِي", "daa", "verb", [K, "imperative-amr", "naqis-verbs", "ya-al-mutakallim"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ.", "«leave me».", "«bırak beni».", segments=[seg("دَعْ", "daa", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("وَجْهُكَ", "wajh", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَوَجْهُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your face».", "«yüzün».", segments=[seg("وَجْهُ", "wajh", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("الْجَنَّةُ", "janna", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is the Garden».", "«cennettir»."),
  tok("حُفَّتْ", "haffa", "verb", [K, "naib-al-fail", "doubled-verbs", "hal"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ حَالٌ. الْمَطْبُوعُ: خُفَّتْ، وَالْحَدِيثُ: حُفَّتْ.", "«hedged about» — the print shows خُفَّتْ; the hadith reads حُفَّتْ.", "«çevrilmiş» — baskı خُفَّتْ yazar; hadis حُفَّتْ."),
  tok("بِالْمَكَارِهِ", "makrah", "noun", [K, QF, "huruf-jarr", "jam-taksir", "mamnu-min-sarf"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمَكَارِهِ مَجْرُورٌ — جَمْعُ مَكْرَهٍ، صِيغَةُ مُنْتَهَى الْجُمُوعِ جُرَّتْ بِالْكَسْرَةِ لِلْأَلِفِ وَاللَّامِ. الرَّوِيُّ الْهَاءُ.", "«with hateful things» — the diptote plural takes kasra under the article; rawi ha.", "«hoşa gitmeyenlerle» — gayr-i munsarif cemi, lâm-ı tarif ile kesre; revî hâ.", segments=[seg("بِ", "bi", "prep"), seg("الْمَكَارِهِ", "makrah", "noun")]),
 ]})
S[-1]["badi"] = [IQ("hadith", span(S[-1], "الْجَنَّةُ", "بِالْمَكَارِهِ"), "حَدِيث")]

# ----------- s9-s10 — the two kinds (RESTORED) + Ibn al-Rumi
S.append({"id": "s9", "translation": {
 "en": "And it is of two sorts: one in which what is taken is not moved from its original meaning — as has passed;" + R_EN,
 "tr": "O da iki türlüdür: biri, alınanın asıl manasından nakledilmediği — geçtiği gibi;" + R_TR},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it».", "«o da».", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("ضَرْبَانِ", "darb", "noun", [K, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«two sorts».", "«iki türlüdür».", punct=":"),
  tok("أَحَدُهُمَا", "ahad", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them».", "«biri».", segments=[seg("أَحَدُ", "ahad", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that in which».", "«… olandır»."),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-me-»."),
  tok("يُنْقَلْ", "naqala", "verb", [K, "lam-jazim", "naib-al-fail", "ism-mawsul"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ — صِلَةٌ.", "«is moved».", "«nakledilmemiş»."),
  tok("فِيهِ", "fi", "prep", [K, "huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«in it» — the returning pronoun.", "«onda» — âid.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("الْمُقْتَبَسُ", "muqtabas", "noun", [K, "naib-al-fail", "ism-maful", "form-viii-verbs"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — اسْمُ مَفْعُولِ اقْتَبَسَ.", "«what is taken» — the ism mafʿul.", "«alınan» — ism-i mef'ûl."),
  tok("عَنْ", "an", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("مَعْنَاهُ", "mana", "noun", [K, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its meaning».", "«manasından».", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  tok("الْأَصْلِيِّ", "asli", "noun", [K, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — نِسْبَةٌ إِلَى الْأَصْلِ.", "«original».", "«asıl».", punct="،"),
  tok("كَمَا", "kama", "part", [K, "huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as».", "«… gibi».", segments=[seg("كَ", "ka", "part"), seg("مَا", "ma-masdariyya", "part")]),
  tok("مَرَّ", "marra", "verb", [K, "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — مُضَاعَفٌ.", "«has passed».", "«geçti».", punct="؛"),
 ]})
S.append({"id": "s10", "translation": {"en": "and the second is its contrary — as the saying of Ibn al-Rumi:" + R_EN, "tr": "ikincisi bunun aksidir — İbnü'r-Rûmî'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second».", "«ve ikincisi».", segments=[seg("وَ", "wa", "conj"), seg("الثَّانِي", "thani", "noun")]),
  tok("خِلَافُهُ", "khilaf", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its contrary».", "«bunun aksidir».", segments=[seg("خِلَافُ", "khilaf", "noun"), pr3ms()], punct="،"),
 ] + ka_qawl(ibn("الرُّومِيِّ", "rumi", "«l-Rumi» — Ibn al-Rumi, the ʿAbbasid poet (d. 283 AH).", "«r-Rûmî» — Abbâsî şairi İbnü'r-Rûmî (ö. 283).", "ابْنُ الرُّومِيِّ."))})
S.append({"id": "s11", "translation": {
 "en": "«If I erred in praising you, you erred not in refusing me: * I have set down my needs in a valley without tillage» (ṭawīl) — «in a valley without tillage» is from the Qurʾan (Ibrahim 37), moved from its meaning: there a valley with no water and no plant, here a place of no profit and no good.",
 "tr": "«Seni övmekte hata ettiysem, sen beni geri çevirmekte hata etmedin: * ihtiyaçlarımı ekini olmayan bir vadiye bıraktım» (tavîl) — «ekini olmayan vadi» Kur'ân'dandır (İbrâhîm 37), manasından nakledilmiş: orada susuz otsuz vadi, burada faydasız hayırsız yer."},
 "tokens": [
  tok("لَئِنْ", "in-shartiyya", "part", [K, A, "in-shartiyya", "tawkid"], "اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَإِنْ حَرْفُ شَرْطٍ.", "«if indeed» — the lam paving the oath.", "«eğer» — kasem lâmı.", segments=[seg("لَ", "la-ibtida", "part"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("أَخْطَأْتُ", "akhtaa", "verb", [K, "in-shartiyya", "form-iv-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ فَاعِلٌ — فِعْلُ الشَّرْطِ.", "«I erred».", "«hata ettiysem».", segments=[seg("أَخْطَأْ", "akhtaa", "verb"), seg("تُ", "pron-1s", "pron")]),
  fi(K),
  tok("مَدْحِكَ", "madh", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«praising you».", "«seni övmekte».", segments=[seg("مَدْحِ", "madh", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("مَا", "ma-nafiya", "part", [K, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not».", "«-me-»."),
  tok("أَخْطَأْتَ", "akhtaa", "verb", [K, "in-shartiyya", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ الْمَفْتُوحَةُ فَاعِلٌ — جَوَابُ الْقَسَمِ سَادٌّ مَسَدَّ جَوَابِ الشَّرْطِ.", "«you erred» — the oath's answer standing for the jawab.", "«hata etmedin» — kasemin cevabı şartın cevabı yerine.", segments=[seg("أَخْطَأْ", "akhtaa", "verb"), seg("تَ", "pron-2ms", "pron")]),
  fi(K),
  tok("مَنْعِي", "man-refusal", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar", "ya-al-mutakallim"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«refusing me».", "«beni geri çevirmekte».", segments=[seg("مَنْعِ", "man-refusal", "noun"), seg("ي", "pron-1s", "pron")], punct="*"),
  tok("لَقَدْ", "qad", "part", [K, "qad-harf", "tawkid"], "اللَّامُ لِلْقَسَمِ، وَقَدْ لِلتَّحْقِيقِ.", "«indeed».", "«gerçekten».", segments=[seg("لَ", "la-ibtida", "part"), seg("قَدْ", "qad", "part")]),
  tok("أَنْزَلْتُ", "anzala", "verb", [K, "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I have set down».", "«bıraktım».", segments=[seg("أَنْزَلْ", "anzala", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("حَاجَاتِي", "haja", "noun", [K, "maful-bihi", "idafa-definiteness", "jam-muannath-salim", "ya-al-mutakallim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my needs».", "«ihtiyaçlarımı».", segments=[seg("حَاجَاتِ", "haja", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("بِوَادٍ", "wadi-valley", "noun", [K, "huruf-jarr", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَوَادٍ مَجْرُورٌ — مَنْقُوصٌ حُذِفَتْ يَاؤُهُ لِلتَّنْوِينِ.", "«in a valley» — the manqus drops its ya before the tanwin.", "«bir vadiye» — mankûs, tenvin önünde yâsı düşer.", segments=[seg("بِ", "bi", "prep"), seg("وَادٍ", "wadi-valley", "noun")]),
  tok("غَيْرِ", "ghayr", "noun", [K, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ، مُضَافٌ.", "«without».", "«olmayan»."),
  tok("ذِي", "dhu", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ — أَسْقَطَهُ الْمَطْبُوعُ، وَالْآيَةُ وَالْوَزْنُ يُثْبِتَانِهِ.", "«possessed of» — the print drops it; the aya and the metre keep it.", "«sahibi» — baskı düşürmüş; âyet ve vezin gerektirir."),
  tok("زَرْعِ", "zar", "noun", [K, QF, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الْعَيْنُ.", "«tillage» — rhyme: rawi ʿayn.", "«ekin» — kafiye: revî ayn."),
 ]})
S[-1]["badi"] = [IQ("quran", span(S[-1], "بِوَادٍ", "زَرْعِ"), "إِبْرَاهِيم ٣٧", kind2="manqul")]

# ----------- s12-s13 — the small change allowed (RESTORED) + a Maghribi
S.append({"id": "s12", "translation": {
 "en": "And there is no harm in a small change of what is taken, for the metre or for another cause — as the saying of one of the Maghribis:" + R_EN,
 "tr": "Alınanda vezin için yahut başka bir sebeple küçük değişiklik yapmakta beis yoktur — Mağriblilerden birinin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no».", "«ve … yoktur».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("بَأْسَ", "bas", "noun", [K, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«harm» — la's ism, its khabar dropped.", "«beis» — lâ'nın ismi, haberi mahzûf."),
  tok("بِتَغْيِيرٍ", "taghyir", "noun", [K, "huruf-jarr", "masdar", "form-ii-verbs"], "الْبَاءُ حَرْفُ جَرٍّ، وَتَغْيِيرٍ مَجْرُورٌ.", "«in a change».", "«değişiklikte».", segments=[seg("بِ", "bi", "prep"), seg("تَغْيِيرٍ", "taghyir", "noun")]),
  tok("يَسِيرٍ", "yasir", "noun", [K, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ.", "«small».", "«küçük»."),
  fi(K),
  tok("الْمُقْتَبَسِ", "muqtabas", "noun", [K, "huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«what is taken».", "«alınanda»."),
  tok("لِلْوَزْنِ", "wazn", "noun", [K, "huruf-jarr", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَالْوَزْنِ مَجْرُورٌ.", "«for the metre».", "«vezin için».", segments=[seg("لِ", "li", "prep"), seg("الْوَزْنِ", "wazn", "noun")]),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("لِغَيْرِهِ", "ghayr", "noun", [K, "huruf-jarr", "atf-nasaq", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«for another».", "«başkası için».", segments=[seg("لِ", "li", "prep"), seg("غَيْرِ", "ghayr", "noun"), pr3msi()], punct="،"),
 ] + ka_qawl([tok("بَعْضِ", "bad", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«one of».", "«birinin»."),
              tok("الْمَغَارِبَةِ", "maghribi", "noun", [K, "idafa-definiteness", "jam-taksir", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ مَغْرِبِيٍّ.", "«the Maghribis».", "«Mağriblilerin».", punct=":")])})
S.append({"id": "s13", "translation": {
 "en": "«What I feared would be has come to be: * to God are we returning» (rajaz) — from the Qurʾan (al-Baqara 156), with a small change.",
 "tr": "«Olmasından korktuğum şey oldu: * biz Allah'a dönücüleriz» (recez) — Kur'ân'dandır (Bakara 156), küçük bir değişiklikle."},
 "tokens": [
  tok("قَدْ", "qad", "part", [K, A, "qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«gerçekten»."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى حَدَثَ.", "«has come to be» — the full kana, «happened».", "«oldu» — tam kâne."),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ فَاعِلٌ.", "«what».", "«şey»."),
  tok("خِفْتُ", "khafa", "verb", [K, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — صِلَةٌ؛ خَافَ يَخَافُ.", "«I feared».", "«korktuğum».", segments=[seg("خِفْ", "khafa", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ.", "«that».", "«-masından»."),
  tok("يَكُونَا", "kana", "verb", [K, "an-masdariyya", "kana-wa-akhawatuha"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ — أُلْحِقَتْ بِهِ أَلِفُ الْإِطْلَاقِ، وَهُوَ تَامٌّ.", "«would be» — with the alif of release.", "«olmasından» — ıtlâk elifi ile.", punct="*"),
  tok("إِنَّا", "inna", "part", [K, "inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَنَا اسْمُهَا.", "«we».", "«biz».", segments=[seg("إِنَّ", "inna", "part"), pr1p()]),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("اللهِ", "allah", "propn", [K, "huruf-jarr"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God».", "«Allah'a»."),
  tok("رَاجِعُونَا", "raji", "noun", [K, QF, "inna-wa-akhawatuha", "jam-mudhakkar-salim", "ism-fail"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالْوَاوِ — جَمْعُ مُذَكَّرٍ سَالِمٌ، أُلْحِقَتْ بِهِ أَلِفُ الْإِطْلَاقِ. الرَّوِيُّ النُّونُ.", "«returning» — the sound plural with the alif of release; rawi nun.", "«dönücüleriz» — cem-i müzekker sâlim, ıtlâk elifi; revî nûn."),
 ]})
S[-1]["badi"] = [IQ("quran", span(S[-1], "إِنَّا", "رَاجِعُونَا"), "الْبَقَرَة ١٥٦", changed=True)]

# ----------- s14-s15 — the tadmin defined (RESTORED) + al-Hariri / al-ʿArji
S.append({"id": "s14", "translation": {
 "en": "And the TADMIN: that the verse be made to carry something of another's verse — with a note upon it, if it is not famous among the eloquent — as the saying of al-Hariri:" + R_EN,
 "tr": "TAZMİN: şiire başkasının şiirinden bir şey katılmasıdır — belâgat ehli arasında meşhur değilse üzerine bir uyarıyla — Harîrî'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَالتَّضْمِينُ", "tadmin", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالتَّضْمِينُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the tadmin».", "«ve tazmin».", segments=[seg("وَ", "wa", "conj"), seg("التَّضْمِينُ", "tadmin", "noun")], punct=":"),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-sıdır»."),
  tok("يُضَمَّنَ", "dammana", "verb", [K, "an-masdariyya", "naib-al-fail", "form-ii-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ.", "«be made to carry».", "«katılması»."),
  tok("الشِّعْرُ", "shir", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the verse».", "«şiir»."),
  tok("شَيْئًا", "shay", "noun", [K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«something».", "«bir şey»."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("شِعْرِ", "shir", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the verse of».", "«şiirinden»."),
  tok("الْغَيْرِ", "ghayr", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَيْ غَيْرِ الشَّاعِرِ.", "«another».", "«başkasının»."),
  tok("مَعَ", "maa", "noun", [K, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«… ile»."),
  tok("التَّنْبِيهِ", "tanbih", "noun", [K, "idafa-definiteness", "masdar", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ نَبَّهَ.", "«a note».", "«uyarı»."),
  tok("عَلَيْهِ", "ala", "prep", [K, "huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«upon it».", "«üzerine».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("إِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«değil»."),
  tok("يَكُنْ", "kana", "verb", [K, "lam-jazim", "kana-wa-akhawatuha", "in-shartiyya"], "مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ.", "«it be».", "«ise»."),
  tok("مَشْهُورًا", "mashhur", "noun", [K, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«famous».", "«meşhur»."),
  tok("عِنْدَ", "inda", "noun", [K, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«among».", "«yanında»."),
  tok("الْبُلَغَاءِ", "baligh", "noun", [K, "idafa-definiteness", "jam-taksir", "ism-mamdud"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ بَلِيغٍ.", "«the eloquent».", "«belâgat ehlinin».", punct="،"),
 ] + ka_qawl(name1("الْحَرِيرِيِّ", "hariri", "«al-Hariri».", "«Harîrî»."))})
S.append({"id": "s15", "translation": {
 "en": "«Though I shall recite, at my sale: * they have lost me — and what a youth they have lost!» (wāfir) — the second hemistich is al-ʿArji's, woven in: a tadmin of idaʿ.",
 "tr": "«Gerçi satıldığımda şunu okuyacağım: * beni ziyan ettiler — ve nasıl bir genci ziyan ettiler!» (vâfir) — ikinci mısra Arcî'nindir, katılmış: îdâ' tazmini."},
 "tokens": [
  tok("عَلَى", "ala", "prep", [K, A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«though» — ʿala + anna: «notwithstanding».", "«gerçi» — alâ + enne."),
  tok("أَنِّي", "anna", "part", [K, "inna-am-anna", "ya-al-mutakallim"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا — أُدْغِمَتِ النُّونُ.", "«that I».", "«ben».", segments=[seg("أَنِّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("سَأُنْشِدُ", "anshada", "verb", [K, "inna-am-anna", "form-iv-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَأُنْشِدُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — خَبَرُ أَنَّ.", "«I shall recite» — anna's khabar.", "«okuyacağım» — ennenin haberi.", segments=[seg("سَ", "sa", "part"), seg("أُنْشِدُ", "anshada", "verb")]),
  tok("عِنْدَ", "inda", "noun", [K, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«at».", "«-de»."),
  tok("بَيْعِي", "bay", "noun", [K, "idafa-definiteness", "masdar", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my sale».", "«satılmam».", segments=[seg("بَيْعِ", "bay", "noun"), seg("ي", "pron-1s", "pron")], punct="*"),
  tok("أَضَاعُونِي", "adaa-lose", "verb", [K, "fail", "form-iv-verbs", "hollow-verbs", "ya-al-mutakallim"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ — أَضَاعَ يُضِيعُ.", "«they have lost me».", "«beni ziyan ettiler».", segments=[seg("أَضَاعُو", "adaa-lose", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("وَأَيَّ", "ayy", "noun", [K, "maful-bihi", "idafa-definiteness", "al-istifham"], "الْوَاوُ عَاطِفَةٌ، وَأَيَّ مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ — لِلتَّعَجُّبِ، مُضَافٌ.", "«and what a» — the fronted object of wonder.", "«ve nasıl bir» — öne alınmış taaccüp mef'ûlü.", segments=[seg("وَ", "wa", "conj"), seg("أَيَّ", "ayy", "noun")]),
  tok("فَتًى", "fatan", "noun", [K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ مُنَوَّنٌ.", "«youth».", "«genç»."),
  tok("أَضَاعُوا", "adaa-lose", "verb", [K, QF, "fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ. الرَّوِيُّ الْعَيْنُ، وَالْوَاوُ وَصْلٌ.", "«they have lost» — rhyme: rawi ʿayn, the waw its wasl.", "«ziyan ettiler» — kafiye: revî ayn, vâv vasl."),
 ]})
S[-1]["badi"] = [{"kind": "tadmin", "sub": "idaa", "set": span(S[-1], "أَضَاعُونِي", "أَضَاعُوا"), "source": "الْعَرْجِيّ"}]

# ----------- s16-s18 — the finest tadmin adds a point (RESTORED) + Ibn Abi l-Isbaʿ / al-Mutanabbi
S.append({"id": "s16", "translation": {
 "en": "And the finest of it is what adds a point upon the original — as the saying of Ibn Abi l-Isbaʿ:" + R_EN,
 "tr": "En güzeli, asıl üzerine bir nükte ekleyendir — İbn Ebi'l-İsba'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَأَحْسَنُهُ", "ahsan", "noun", [K, "mubtada-khabar", "ism-tafdil", "idafa-definiteness"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَحْسَنُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and the finest of it».", "«ve en güzeli».", segments=[seg("وَ", "wa", "conj"), seg("أَحْسَنُ", "ahsan", "noun"), pr3ms()]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what».", "«… olandır»."),
  tok("زَادَ", "zada", "verb", [K, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«adds».", "«ekleyen»."),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  tok("الْأَصْلِ", "asl", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the original».", "«aslın»."),
  tok("بِنُكْتَةٍ", "nukta", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَنُكْتَةٍ مَجْرُورٌ.", "«a point».", "«bir nükte».", segments=[seg("بِ", "bi", "prep"), seg("نُكْتَةٍ", "nukta", "noun")], punct="،"),
 ] + ka_qawl(ibn("أَبِي", "ab", "«Abi».", "«Ebi».", "مُضَافٌ.")[:1] + [tok("أَبِي", "ab", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abi».", "«Ebi»."),
                         tok("الْإِصْبَعِ", "isba-name", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ابْنُ أَبِي الْإِصْبَعِ الْمِصْرِيُّ، صَاحِبُ تَحْرِيرِ التَّحْبِيرِ.", "«l-Isbaʿ» — Ibn Abi l-Isbaʿ al-Misri, author of Tahrir al-Tahbir (d. 654 AH).", "«l-İsba'» — Tahrîrü't-Tahbîr'in yazarı İbn Ebi'l-İsba' el-Mısrî (ö. 654).", punct=":")])})
S.append({"id": "s17", "translation": {
 "en": "«When fancy shows me her dark lip and her teeth, * I remember what lies between al-ʿUdhayb and Bariq» (ṭawīl) —",
 "tr": "«Vehim bana onun koyu dudağını ve dişlerini gösterdiğinde, * Uzeyb ile Bârık arasındakini hatırlarım» (tavîl) —"},
 "tokens": [
  tok("إِذَا", "idha", "part", [K, A, "idha-shartiyya"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  tok("الْوَهْمُ", "wahm", "noun", [K, "fail", "hadhf-wa-taqdir"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ — إِذَا لَا يَلِيهَا إِلَّا الْفِعْلُ.", "«fancy» — the doer of a verb the next explains; idha wants a verb.", "«vehim» — mahzûf fiilin fâili; izâ fiil ister."),
  tok("أَبْدَى", "abda", "verb", [K, "form-iv-verbs", "naqis-verbs", "mafulayn"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — أَبْدَى يُبْدِي: أَظْهَرَ.", "«shows».", "«gösterdi»."),
  tok("لِي", "li", "prep", [K, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ.", "«to me».", "«bana».", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  tok("لَمَاهَا", "lama-lip", "noun", [K, "maful-bihi", "idafa-definiteness", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَهَا مُضَافٌ إِلَيْهِ — اللَّمَى: سُمْرَةُ الشَّفَةِ.", "«her dark lip» — lama: the lip's darkness.", "«koyu dudağını» — lemâ: dudak esmerliği.", segments=[seg("لَمَا", "lama-lip", "noun"), seg("هَا", "pron-3fs", "pron")]),
  tok("وَثَغْرَهَا", "thaghr", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَثَغْرَ مَعْطُوفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her teeth».", "«ve dişlerini».", segments=[seg("وَ", "wa", "conj"), seg("ثَغْرَ", "thaghr", "noun"), seg("هَا", "pron-3fs", "pron")], punct="*"),
  tok("تَذَكَّرْتُ", "tadhakkara", "verb", [K, "idha-shartiyya", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جَوَابُ إِذَا.", "«I remember» — the jawab.", "«hatırlarım» — cevap.", segments=[seg("تَذَكَّرْ", "tadhakkara", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what».", "«… şeyi»."),
  tok("بَيْنَ", "bayna", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — صِلَةُ مَا.", "«between».", "«arasında»."),
  tok("الْعُذَيْبِ", "udhayb", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَاءٌ لِبَنِي تَمِيمٍ.", "«al-ʿUdhayb» — a water of Tamim.", "«Uzeyb» — Temîm'in bir suyu."),
  tok("وَبَارِقِ", "bariq", "propn", [K, QF, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَبَارِقِ مَعْطُوفٌ مَجْرُورٌ — مَوْضِعٌ. الرَّوِيُّ الْقَافُ.", "«and Bariq» — a place; rawi qaf.", "«ve Bârık» — bir yer; revî kâf.", segments=[seg("وَ", "wa", "conj"), seg("بَارِقِ", "bariq", "propn")]),
 ]})
S[-1]["badi"] = [{"kind": "tadmin", "sub": "idaa", "set": span(S[-1], "تَذَكَّرْتُ", "وَبَارِقِ"), "source": "أَبُو الطَّيِّبِ"}]
S.append({"id": "s18", "translation": {
 "en": "«And it reminds me, by her figure and my tears, * of the trailing of our lances and the coursing of the racers» — al-Mutanabbi's bayt woven in: a tadmin of istiʿana, bettered by a tawriya and a tashbih.",
 "tr": "«Ve onun boyu ile gözyaşlarımdan bana * mızraklarımızın sürüklenişini ve yarış atlarının koşuşunu hatırlatır» — Mütenebbî'nin beyti katılmış: istiâne tazmini, tevriye ve teşbih ile güzelleştirilmiş."},
 "tokens": [
  tok("وَيُذْكِرُنِي", "dhakkara-iv", "verb", [K, A, "atf-nasaq", "form-iv-verbs", "mafulayn", "ya-al-mutakallim"], "الْوَاوُ عَاطِفَةٌ، وَيُذْكِرُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: الْوَهْمُ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ أَوَّلُ — أَذْكَرَ يُذْكِرُ.", "«and it reminds me» — Form IV, two objects.", "«ve bana hatırlatır» — if'âl, iki mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يُذْكِرُ", "dhakkara-iv", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«-den»."),
  tok("قَدِّهَا", "qadd", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — الْقَدُّ: الْقَامَةُ.", "«her figure».", "«boyundan».", segments=[seg("قَدِّ", "qadd", "noun"), seg("هَا", "pron-3fs", "pron")]),
  tok("وَمَدَامِعِي", "madma", "noun", [K, "atf-nasaq", "idafa-definiteness", "jam-taksir", "ya-al-mutakallim"], "الْوَاوُ عَاطِفَةٌ، وَمَدَامِعِ مَعْطُوفٌ مَجْرُورٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ مَدْمَعٍ.", "«and my tears».", "«ve gözyaşlarımdan».", segments=[seg("وَ", "wa", "conj"), seg("مَدَامِعِ", "madma", "noun"), seg("ي", "pron-1s", "pron")], punct="*"),
  tok("مَجَرَّ", "majarr", "noun", [K, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ — مَصْدَرٌ مِيمِيٌّ مِنْ جَرَّ.", "«the trailing of» — the second object.", "«sürüklenişini» — ikinci mef'ûl."),
  tok("عَوَالِينَا", "aliya", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ عَالِيَةٍ: صَدْرُ الرُّمْحِ.", "«our lances» — the spear-tops.", "«mızraklarımızın» — mızrak başları.", segments=[seg("عَوَالِي", "aliya", "noun"), pr1p()]),
  tok("وَمَجْرَى", "majra", "noun", [K, "atf-nasaq", "idafa-definiteness", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَمَجْرَى مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«and the coursing of».", "«ve koşuşunu».", segments=[seg("وَ", "wa", "conj"), seg("مَجْرَى", "majra", "noun")]),
  tok("السَّوَابِقِ", "sabiq", "noun", [K, QF, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ سَابِقَةٍ: الْخَيْلُ السَّابِقَةُ. الرَّوِيُّ الْقَافُ.", "«the racers» — rawi qaf.", "«yarış atlarının» — revî kâf."),
 ]})
S[-1]["badi"] = [{"kind": "tadmin", "sub": "istiana", "set": list(range(4, 8)), "source": "أَبُو الطَّيِّبِ", "with": "s17"}]

# ----------- s19 — the small change; istiʿana / idaʿ and rafw (RESTORED)
S.append({"id": "s19", "translation": {
 "en": "And a small change does no harm. And the weaving-in of a bayt or more is called ISTIʿANA (seeking aid), and of a hemistich or less IDAʿ (a deposit) and RAFW (a darning)." + R_EN,
 "tr": "Küçük değişiklik zarar vermez. Bir beyit yahut fazlasının tazminine İSTİÂNE, bir mısra yahut azının tazminine ÎDÂ' (emanet) ve REFV (yama) denir." + R_TR},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and … not».", "«ve … -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("يَضُرُّ", "darra", "verb", [K, "doubled-verbs"], "مُضَارِعٌ مَرْفُوعٌ — ضَرَّ يَضُرُّ.", "«does harm».", "«zarar verir»."),
  tok("التَّغْيِيرُ", "taghyir", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the change».", "«değişiklik»."),
  tok("الْيَسِيرُ", "yasir", "noun", [K, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«small».", "«küçük».", punct="."),
  tok("وَيُسَمَّى", "samma", "verb", [K, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيُسَمَّى مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and is called».", "«ve … denir».", segments=[seg("وَ", "wa", "conj"), seg("يُسَمَّى", "samma", "verb")]),
  tok("تَضْمِينُ", "tadmin", "noun", [K, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«the weaving-in of».", "«tazmini»."),
  tok("الْبَيْتِ", "bayt", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a bayt».", "«beytin»."),
  tok("فَمَا", "ma-mawsula", "noun", [K, "atf-nasaq", "ism-mawsul"], "الْفَاءُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ.", "«or what».", "«yahut … olanın».", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-mawsula", "noun")]),
  tok("زَادَ", "zada", "verb", [K, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«exceeds».", "«fazla olan»."),
  tok("اسْتِعَانَةً", "istiana", "noun", [K, "mafulayn", "masdar", "form-x-verbs", "hollow-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ اسْتَعَانَ.", "«istiʿana» — the second object.", "«istiâne» — ikinci mef'ûl.", punct="،"),
  tok("وَتَضْمِينُ", "tadmin", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَتَضْمِينُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the weaving-in of».", "«ve … tazmini».", segments=[seg("وَ", "wa", "conj"), seg("تَضْمِينُ", "tadmin", "noun")]),
  tok("الْمِصْرَاعِ", "misra", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمِصْرَاعُ: نِصْفُ الْبَيْتِ.", "«a hemistich».", "«mısraın»."),
  tok("فَمَا", "ma-mawsula", "noun", [K, "atf-nasaq", "ism-mawsul"], "الْفَاءُ عَاطِفَةٌ، وَمَا مَعْطُوفٌ.", "«or what».", "«yahut … olanın».", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-mawsula", "noun")]),
  tok("دُونَهُ", "duna", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةٌ.", "«is less».", "«azı olan».", segments=[seg("دُونَ", "duna", "noun"), pr3ms()]),
  tok("إِيدَاعًا", "ida-deposit", "noun", [K, "mafulayn", "masdar", "form-iv-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ أَوْدَعَ.", "«idaʿ».", "«îdâ'»."),
  tok("وَرَفْوًا", "rafw", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَرَفْوًا مَعْطُوفٌ مَنْصُوبٌ — الرَّفْوُ: إِصْلَاحُ الثَّوْبِ.", "«and rafw» — the darning of a garment.", "«ve refv» — giysiyi yamama.", segments=[seg("وَ", "wa", "conj"), seg("رَفْوًا", "rafw", "noun")], punct="."),
 ]})

# ----------- s20-s21 — the ʿaqd (RESTORED) + Abu l-ʿAtahiya
S.append({"id": "s20", "translation": {
 "en": "And the ʿAQD: that prose be put into verse, not by way of the iqtibas — as the saying of Abu l-ʿAtahiya:" + R_EN,
 "tr": "AKD: iktibas yolu olmaksızın nesrin nazma çekilmesidir — Ebü'l-Atâhiye'nin şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَالْعَقْدُ", "aqd", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْعَقْدُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the ʿaqd».", "«ve akd».", segments=[seg("وَ", "wa", "conj"), seg("الْعَقْدُ", "aqd", "noun")], punct=":"),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-sıdır»."),
  tok("يُنْظَمَ", "nazama", "verb", [K, "an-masdariyya", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ.", "«be put into verse».", "«nazma çekilmesi»."),
  tok("نَثْرٌ", "nathr", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«prose».", "«nesir»."),
  tok("لَا", "la-nafiya", "part", [K], "حَرْفُ نَفْيٍ.", "«not».", "«değil»."),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«üzere»."),
  tok("طَرِيقِ", "tariq", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the way of».", "«yolu»."),
  tok("الِاقْتِبَاسِ", "iqtibas", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the iqtibas».", "«iktibas».", punct="،"),
 ] + ka_qawl(abu("الْعَتَاهِيَةِ", "atahiya", "«l-ʿAtahiya» — the ʿAbbasid poet of zuhd (d. 211 AH).", "«l-Atâhiye» — zühd şairi (ö. 211).", "أَبُو الْعَتَاهِيَةِ إِسْمَاعِيلُ بْنُ الْقَاسِمِ."))})
S.append({"id": "s21", "translation": {
 "en": "«What ails one whose beginning is a drop * and whose end is a carcass, that he should boast?» (sarīʿ) — ʿAli's saying versified: «what has the son of Adam to do with boasting? his beginning is a drop and his end a carcass».",
 "tr": "«Başı bir damla * sonu leş olanın nesi var ki övünür?» (serî') — Hz. Ali'nin sözü nazma çekilmiş: «Âdemoğlunun övünmekle ne işi var? başı bir damla, sonu bir leştir»."},
 "tokens": [
  tok("مَا", "ma-istifham", "noun", [K, A, "al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ — لِلتَّعَجُّبِ.", "«what» — the question of wonder.", "«ne» — taaccüp istifhâmı."),
  tok("بَالُ", "bal-state", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — مَا بَالُهُ: مَا شَأْنُهُ.", "«ails» — the khabar: «what is the state of».", "«… nesi var» — haber."),
  tok("مَنْ", "man", "noun", [K, "idafa-definiteness", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«one who».", "«… kimsenin»."),
  tok("أَوَّلُهُ", "awwal", "noun", [K, "ism-mawsul", "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةٌ.", "«whose beginning».", "«başı».", segments=[seg("أَوَّلُ", "awwal", "noun"), pr3ms()]),
  tok("نُطْفَةٌ", "nutfa", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a drop».", "«bir damladır».", punct="*"),
  tok("وَجِيفَةٌ", "jifa", "noun", [K, "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَجِيفَةٌ خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«and a carcass» — the fronted khabar.", "«ve leş» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("جِيفَةٌ", "jifa", "noun")]),
  tok("آخِرُهُ", "akhir", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his end».", "«sonu».", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  tok("يَفْخَرُ", "fakhara", "verb", [K, QF, "hal"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ حَالٌ مِنْ مَنْ. الرَّوِيُّ الرَّاءُ.", "«boasting» — the hal clause; rawi ra.", "«övünür» — hâl cümlesi; revî râ."),
 ]})
S[-1]["badi"] = [{"kind": "aqd", "set": list(range(0, 8)), "source": "قَوْلُ عَلِيٍّ: مَا لِابْنِ آدَمَ وَالْفَخْرِ، وَإِنَّمَا أَوَّلُهُ نُطْفَةٌ وَآخِرُهُ جِيفَةٌ"}]

# ----------- s22-s24 — the hall (RESTORED) + al-Mutanabbi and the Maghribi's prose (RESTORED)
S.append({"id": "s22", "translation": {
 "en": "And the HALL: that verse be put into prose — as one of the Maghribis put into prose the saying of Abu l-Tayyib:" + R_EN,
 "tr": "HAL: nazmın nesre çevrilmesidir — Mağriblilerden birinin Ebü't-Tayyib'in şu sözünü nesre çevirmesi gibi:" + R_TR},
 "tokens": [
  tok("وَالْحَلُّ", "hall-nathr", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْحَلُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the hall».", "«ve hal».", segments=[seg("وَ", "wa", "conj"), seg("الْحَلُّ", "hall-nathr", "noun")], punct=":"),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-sıdır»."),
  tok("يُنْثَرَ", "nathara", "verb", [K, "an-masdariyya", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ.", "«be put into prose».", "«nesre çevrilmesi»."),
  tok("نَظْمٌ", "nazm", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«verse».", "«nazım».", punct="،"),
  tok("كَمَا", "kama", "part", [K, "huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as».", "«… gibi».", segments=[seg("كَ", "ka", "part"), seg("مَا", "ma-masdariyya", "part")]),
  tok("نَثَرَ", "nathara", "verb", [K, "fail"], "فِعْلٌ مَاضٍ.", "«put into prose».", "«nesre çevirdi»."),
  tok("بَعْضُ", "bad", "noun", [K, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«one of».", "«biri»."),
  tok("الْمَغَارِبَةِ", "maghribi", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Maghribis».", "«Mağriblilerin»."),
  tok("قَوْلَ", "qawl", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the saying of».", "«sözünü»."),
  tok("أَبِي", "ab", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
  tok("الطَّيِّبِ", "abu-tayyib", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«l-Tayyib».", "«t-Tayyib».", punct=":"),
 ]})
S.append({"id": "s23", "translation": {
 "en": "«When a man's deeds are foul, his thoughts turn foul, * and he believes the delusion he is used to» (ṭawīl).",
 "tr": "«Kişinin fiili kötü olunca zanları da kötü olur, * ve alıştığı vehmi doğrular» (tavîl)."},
 "tokens": [
  tok("إِذَا", "idha", "part", [K, A, "idha-shartiyya"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ınca»."),
  tok("سَاءَ", "saa-bad", "verb", [K, "idha-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ — سَاءَ يَسُوءُ: قَبُحَ.", "«is foul».", "«kötü oldu»."),
  tok("فِعْلُ", "fil", "noun", [K, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the deed of».", "«fiili»."),
  tok("الْمَرْءِ", "mar", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a man».", "«kişinin»."),
  tok("سَاءَتْ", "saa-bad", "verb", [K, "idha-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — جَوَابُ إِذَا.", "«turn foul» — the jawab.", "«kötü olur» — cevap."),
  tok("ظُنُونُهُ", "zann", "noun", [K, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ ظَنٍّ.", "«his thoughts».", "«zanları».", segments=[seg("ظُنُونُ", "zann", "noun"), pr3ms()], punct="*"),
  tok("وَصَدَّقَ", "saddaqa", "verb", [K, "atf-nasaq", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَصَدَّقَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and he believes».", "«ve doğrular».", segments=[seg("وَ", "wa", "conj"), seg("صَدَّقَ", "saddaqa", "verb")]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what».", "«… şeyi»."),
  tok("يَعْتَادُهُ", "itada", "verb", [K, "ism-mawsul", "form-viii-verbs", "hollow-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ — صِلَةٌ؛ اعْتَادَ يَعْتَادُ.", "«he is used to».", "«alıştığı».", segments=[seg("يَعْتَادُ", "itada", "verb"), pr3ms()]),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — لِلْبَيَانِ.", "«of».", "«-den»."),
  tok("تَوَهُّمِ", "tawahhum", "noun", [K, QF, "huruf-jarr", "masdar", "form-v-verbs"], "مَجْرُورٌ — مَصْدَرُ تَوَهَّمَ؛ أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الْمِيمُ.", "«delusion» — rawi mim.", "«vehim» — revî mîm."),
 ]})
S.append({"id": "s24", "translation": {
 "en": "«For when his deeds turned ugly and his palms bore colocynth, ill thought did not cease to lead him, and to confirm the delusion he was used to» — the bayt put into prose: a hall." + R_EN,
 "tr": "«Fiilleri çirkinleşip hurmaları Ebû Cehil karpuzuna dönünce, sûizan onu sürüklemekten ve alıştığı vehmini doğrulamaktan geri durmadı» — beyit nesre çevrilmiş: hal." + R_TR},
 "tokens": [
  tok("فَإِنَّهُ", "inna", "part", [K, "inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«for he».", "«çünkü o».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("لَمَّا", "lamma", "part", [K, "maful-fih"], "ظَرْفٌ بِمَعْنَى حِينَ.", "«when».", "«-ınca»."),
  tok("قَبُحَتْ", "qabuha", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«turned ugly».", "«çirkinleşti»."),
  tok("فَعَلَاتُهُ", "fala", "noun", [K, "fail", "idafa-definiteness", "jam-muannath-salim"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ فَعْلَةٍ.", "«his deeds».", "«fiilleri».", segments=[seg("فَعَلَاتُ", "fala", "noun"), pr3ms()]),
  tok("وَحَنْظَلَتْ", "hanzala", "verb", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَحَنْظَلَتْ فِعْلٌ مَاضٍ رُبَاعِيٌّ — صَارَتْ حَنْظَلًا.", "«and bore colocynth» — a four-radical verb.", "«ve acı karpuza döndü» — rubâî fiil.", segments=[seg("وَ", "wa", "conj"), seg("حَنْظَلَتْ", "hanzala", "verb")]),
  tok("نَخَلَاتُهُ", "nakhla", "noun", [K, "fail", "idafa-definiteness", "jam-muannath-salim"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ نَخْلَةٍ.", "«his palms».", "«hurmaları».", segments=[seg("نَخَلَاتُ", "nakhla", "noun"), pr3ms()], punct="،"),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-me-»."),
  tok("يَزَلْ", "zala", "verb", [K, "lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — مَا زَالَ: خَبَرُ إِنَّ.", "«did cease» — inna's khabar.", "«durmadı» — innenin haberi."),
  tok("سُوءُ", "su", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَزَلْ مَرْفُوعٌ، مُضَافٌ.", "«ill» — the ism.", "«sû-i» — isim."),
  tok("الظَّنِّ", "zann", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«thought».", "«zan»."),
  tok("يَقْتَادُهُ", "iqtada", "verb", [K, "kana-wa-akhawatuha", "form-viii-verbs", "hollow-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ — خَبَرُ يَزَلْ؛ اقْتَادَ: قَادَ.", "«lead him» — the khabar.", "«onu sürükler» — haber.", segments=[seg("يَقْتَادُ", "iqtada", "verb"), pr3ms()]),
  tok("وَيُصَدِّقُ", "saddaqa", "verb", [K, "atf-nasaq", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُصَدِّقُ مُضَارِعٌ مَرْفُوعٌ.", "«and confirm».", "«ve doğrular».", segments=[seg("وَ", "wa", "conj"), seg("يُصَدِّقُ", "saddaqa", "verb")]),
  tok("تَوَهُّمَهُ", "tawahhum", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his delusion».", "«vehmini».", segments=[seg("تَوَهُّمَ", "tawahhum", "noun"), pr3ms()]),
  tok("الَّذِي", "alladhi", "noun", [K, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ.", "«which».", "«-diği»."),
  tok("يَعْتَادُهُ", "itada", "verb", [K, "ism-mawsul", "form-viii-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ — صِلَةٌ.", "«he is used to».", "«alıştığı».", segments=[seg("يَعْتَادُ", "itada", "verb"), pr3ms()], punct="."),
 ]})
S[-1]["badi"] = [{"kind": "hall", "set": list(range(0, 15)), "with": "s23", "source": "أَبُو الطَّيِّبِ"}]

# ----------- s25-s28 — the talmih (RESTORED) + Abu Tammam twice + the famous bayt
S.append({"id": "s25", "translation": {
 "en": "And the TALMIH: that a story or a verse be pointed at without its mention — as the saying of Abu Tammam:" + R_EN,
 "tr": "TELMİH: bir kıssaya yahut şiire, anılmaksızın işaret edilmesidir — Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَالتَّلْمِيحُ", "talmih", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالتَّلْمِيحُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the talmih».", "«ve telmih».", segments=[seg("وَ", "wa", "conj"), seg("التَّلْمِيحُ", "talmih", "noun")], punct=":"),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-sıdır»."),
  tok("يُشَارَ", "ashara-point", "verb", [K, "an-masdariyya", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«be pointed».", "«işaret edilmesi»."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-e»."),
  tok("قِصَّةٍ", "qissa", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«a story».", "«bir kıssaya»."),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("شِعْرٍ", "shir", "noun", [K, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«a verse».", "«bir şiire»."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«without».", "«-sızın»."),
  tok("غَيْرِ", "ghayr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«without».", "«olmaksızın»."),
  tok("ذِكْرِهِ", "dhikr", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its mention».", "«anılması».", segments=[seg("ذِكْرِ", "dhikr", "noun"), pr3msi()], punct="،"),
 ] + ka_qawl(abu("تَمَّامٍ", "abu-tammam", "«Tammam».", "«Temmâm».", "أَبُو تَمَّامٍ."))})
S.append({"id": "s26", "translation": {
 "en": "«By God, I know not whether a sleeper's dreams * have visited us, or whether Joshua was in the caravan» (ṭawīl) — a talmih to Joshua's story: the sun held back for him.",
 "tr": "«Vallahi bilmem: bir uyuyanın rüyaları mı * bize uğradı, yoksa kafilede Yûşa' mı vardı» (tavîl) — Yûşa' kıssasına telmih: güneş onun için durduruldu."},
 "tokens": [
  tok("فَوَاللهِ", "allah", "propn", [K, A, "huruf-jarr"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَالْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by God» — the waw of the oath.", "«vallahi» — kasem vâvı.", segments=[seg("فَ", "fa", "conj"), seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  tok("مَا", "ma-nafiya", "part", [K, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not».", "«-me-»."),
  tok("أَدْرِي", "dara", "verb", [K, "anwa-ma", "naqis-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — دَرَى يَدْرِي.", "«I know».", "«bilirim»."),
  tok("أَأَحْلَامُ", "hulm", "noun", [K, "al-istifham", "mubtada-khabar", "idafa-definiteness", "jam-taksir"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَأَحْلَامُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ حُلْمٍ؛ وَالْجُمْلَةُ سَدَّتْ مَسَدَّ مَفْعُولَيْ أَدْرِي.", "«is it the dreams of» — the question; the clause fills the two objects of «know».", "«rüyaları mı» — istifhâm; cümle iki mef'ûl yerine geçer.", segments=[seg("أَ", "hamza-istifham", "part"), seg("أَحْلَامُ", "hulm", "noun")]),
  tok("نَائِمٍ", "naim-sleeper", "noun", [K, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ نَامَ.", "«a sleeper».", "«bir uyuyanın».", punct="*"),
  tok("أَلَمَّتْ", "alamma", "verb", [K, "mubtada-khabar", "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — خَبَرٌ؛ أَلَمَّ بِهِ: نَزَلَ بِهِ.", "«have visited» — the khabar.", "«uğradı» — haber."),
  tok("بِنَا", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَا مَجْرُورٌ.", "«us».", "«bize».", segments=[seg("بِ", "bi", "prep"), pr1p()]),
  tok("أَمْ", "am", "part", [K, "atf-nasaq", "al-istifham"], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ، مُعَادِلَةُ الْهَمْزَةِ.", "«or» — the am matching the hamza.", "«yoksa» — hemzenin muâdili em."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«was».", "«vardı»."),
  fi(K),
  tok("الرَّكْبِ", "rakb", "noun", [K, "huruf-jarr", "kana-wa-akhawatuha"], "مَجْرُورٌ — خَبَرُ كَانَ مُقَدَّمٌ؛ الرَّكْبُ: أَصْحَابُ الْإِبِلِ فِي السَّفَرِ.", "«the caravan» — kana's fronted khabar.", "«kafilede» — kânenin öne alınmış haberi."),
  tok("يُوشَعُ", "yusha", "propn", [K, QF, "kana-wa-akhawatuha", "mamnu-min-sarf"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ. الرَّوِيُّ الْعَيْنُ.", "«Joshua» — a foreign name, diptote; rawi ʿayn.", "«Yûşa'» — yabancı ad, gayr-i munsarif; revî ayn."),
 ]})
S[-1]["badi"] = [{"kind": "talmih", "set": [ix(S[-1], "يُوشَعُ")], "source": "قِصَّةُ يُوشَعَ: رَدُّ الشَّمْسِ"}]
S.append({"id": "s27", "translation": {
 "en": "And as his saying: «Truly ʿAmr, beside the burning sand and the blazing fire, * is gentler and kinder than you in the hour of distress» — a talmih to the famous bayt:",
 "tr": "Ve onun şu sözü gibi: «Amr, kızgın kumla alevlenen ateşin yanında, * sıkıntı saatinde senden daha yumuşak ve daha şefkatlidir» — şu meşhur beyte telmih:"},
 "tokens": [tok("وَكَقَوْلِهِ", "qawl", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and as his saying».", "«ve onun sözü gibi».", segments=[seg("وَ", "wa", "conj"), seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), pr3msi()], punct=":")] + [
  tok("لَعَمْرٌو", "amr-name", "propn", [K, A, "mubtada-khabar", "tawkid"], "اللَّامُ لِلِابْتِدَاءِ، وَعَمْرٌو مُبْتَدَأٌ مَرْفُوعٌ — زِيدَتْ وَاوُهُ خَطًّا لِلْفَرْقِ مِنْ عُمَرَ.", "«truly ʿAmr» — the written waw tells it from ʿUmar.", "«Amr» — yazıdaki vâv Ömer'den ayırır.", segments=[seg("لَ", "la-ibtida", "part"), seg("عَمْرٌو", "amr-name", "propn")]),
  tok("مَعَ", "maa", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«beside».", "«… ile»."),
  tok("الرَّمْضَاءِ", "ramda", "noun", [K, "idafa-definiteness", "ism-mamdud"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الرَّمْضَاءُ: الْأَرْضُ الشَّدِيدَةُ الْحَرِّ.", "«the burning sand».", "«kızgın kum»."),
  tok("وَالنَّارِ", "nar", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالنَّارِ مَعْطُوفٌ مَجْرُورٌ.", "«and the fire».", "«ve ateş».", segments=[seg("وَ", "wa", "conj"), seg("النَّارِ", "nar", "noun")]),
  tok("تَلْتَظِي", "iltaza", "verb", [K, "hal", "form-viii-verbs", "naqis-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ حَالٌ؛ الْتَظَتِ النَّارُ: الْتَهَبَتْ.", "«blazing» — the hal clause.", "«alevlenen» — hâl cümlesi.", punct="*"),
  tok("أَرَقُّ", "araqq", "noun", [K, "mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ مِنْ رَقَّ.", "«gentler» — the khabar.", "«daha yumuşak» — haber."),
  tok("وَأَحْفَى", "ahfa", "noun", [K, "atf-nasaq", "ism-tafdil", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَأَحْفَى مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مِنْ حَفِيَ بِهِ: بَالَغَ فِي إِكْرَامِهِ.", "«and kinder».", "«ve daha şefkatli».", segments=[seg("وَ", "wa", "conj"), seg("أَحْفَى", "ahfa", "noun")]),
  tok("مِنْكَ", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْكَافُ مَجْرُورٌ.", "«than you».", "«senden».", segments=[seg("مِنْ", "min", "prep"), seg("كَ", "pron-2ms", "pron")]),
  fi(K),
  tok("سَاعَةِ", "saa-hour", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the hour of».", "«saatinde»."),
  tok("الْكَرْبِ", "karb", "noun", [K, QF, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْكَرْبُ: الْحُزْنُ الشَّدِيدُ. الرَّوِيُّ الْبَاءُ.", "«distress» — rawi ba.", "«sıkıntı» — revî bâ."),
 ]})
S[-1]["badi"] = [{"kind": "talmih", "set": span(S[-1], "لَعَمْرٌو", "وَالنَّارِ"), "source": "الْمُسْتَجِيرُ بِعَمْرٍو عِنْدَ كُرْبَتِهِ", "with": "s28"}]
S.append({"id": "s28", "translation": {
 "en": "«He who seeks refuge with ʿAmr in his distress * is like one who seeks refuge from the burning sand in the fire» (basīṭ).",
 "tr": "«Sıkıntısında Amr'a sığınan, * kızgın kumdan ateşe sığınan gibidir» (basît)."},
 "tokens": [
  tok("الْمُسْتَجِيرُ", "mustajir", "noun", [K, A, "mubtada-khabar", "ism-fail", "form-x-verbs"], "مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلِ اسْتَجَارَ: طَلَبَ الْجِوَارَ.", "«he who seeks refuge».", "«sığınan»."),
  tok("بِعَمْرٍو", "amr-name", "propn", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَعَمْرٍو مَجْرُورٌ.", "«with ʿAmr».", "«Amr'a».", segments=[seg("بِ", "bi", "prep"), seg("عَمْرٍو", "amr-name", "propn")]),
  tok("عِنْدَ", "inda", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«in».", "«-de»."),
  tok("كُرْبَتِهِ", "kurba", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his distress».", "«sıkıntısında».", segments=[seg("كُرْبَتِ", "kurba", "noun"), pr3msi()], punct="*"),
  tok("كَالْمُسْتَجِيرِ", "mustajir", "noun", [K, "huruf-jarr", "mubtada-khabar", "ism-fail"], "الْكَافُ حَرْفُ جَرٍّ، وَالْمُسْتَجِيرِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is like one who seeks refuge» — the khabar.", "«sığınan gibidir» — haber.", segments=[seg("كَ", "ka", "part"), seg("الْمُسْتَجِيرِ", "mustajir", "noun")]),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الرَّمْضَاءِ", "ramda", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the burning sand».", "«kızgın kumdan»."),
  tok("بِالنَّارِ", "nar", "noun", [K, QF, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالنَّارِ مَجْرُورٌ. الرَّوِيُّ الرَّاءُ، وَالْأَلِفُ رِدْفٌ.", "«in the fire» — rawi ra, alif ridf.", "«ateşe» — revî râ, elif ridf.", segments=[seg("بِ", "bi", "prep"), seg("النَّارِ", "nar", "noun")]),
 ]})

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "iqtibas": need("iqtibas", "اقْتِبَاس", "ق ب س", "noun", "iqtibas — taking a brand from the fire (masdar of Form VIII اقْتَبَسَ); in the badiʿ: weaving Qurʾan or hadith into one's speech", "iktibas — ateşten kor alma (iftiâl masdarı); bedî'de: söze Kur'ân yahut hadis katma", 5),
 "tadmin": need("tadmin", "تَضْمِين", "ض م ن", "noun", "tadmin — making a thing carry another (masdar of Form II ضَمَّنَ); in the badiʿ: another's verse woven into one's own", "tazmin — bir şeye başka bir şey yükleme (tef'îl masdarı); bedî'de: başkasının şiirini kendi şiirine katma", 5),
 "aqd": need("aqd", "عَقْد", "ع ق د", "noun", "ʿaqd — a tying, a knot (masdar of عَقَدَ); in the badiʿ: prose put into verse", "akd — bağlama, düğüm (akade masdarı); bedî'de: nesri nazma çekme", 4),
 "hall-nathr": need("hall-nathr", "حَلّ", "ح ل ل", "noun", "hall — an untying (masdar of حَلَّ); in the badiʿ: verse put into prose", "hal — çözme (halle masdarı); bedî'de: nazmı nesre çevirme", 4),
 "talmih": need("talmih", "تَلْمِيح", "ل م ح", "noun", "talmih — a glancing hint (masdar of Form II لَمَّحَ); in the badiʿ: a story or verse pointed at, unnamed", "telmih — göz ucuyla işaret (tef'îl masdarı); bedî'de: bir kıssaya yahut şiire anmadan işaret", 5),
 "dammana": need("dammana", "ضَمَّنَ", "ض م ن", "verb", "to make a thing carry or contain another (Form II; ضَمَّنَ يُضَمِّنُ — two objects)", "bir şeye başka şey yükletmek, içermesini sağlamak (tef'îl; dammene yudamminu — iki mef'ûl)", 5),
 "hariri": need("hariri", "الْحَرِيرِيّ", None, "propn", "al-Hariri — al-Qasim b. ʿAli, author of the Maqamat (d. 516 AH)", "Harîrî — Makâmât'ın yazarı Kâsım b. Ali (ö. 516)", 5),
 "lamh": need("lamh", "لَمْح", "ل م ح", "noun", "a glance, a twinkling (masdar of لَمَحَ) — لَمْحُ الْبَصَرِ: the twinkling of an eye", "bakış, göz kırpma (lemaha masdarı) — lemhu'l-basar: göz açıp kapama", 4),
 "anshada": need("anshada", "أَنْشَدَ", "ن ش د", "verb", "to recite verse (Form IV; أَنْشَدَ يُنْشِدُ)", "şiir okumak (if'âl; enşede yunşidu)", 4),
 "aghraba": need("aghraba", "أَغْرَبَ", "غ ر ب", "verb", "to bring something rare or strange (Form IV; أَغْرَبَ يُغْرِبُ)", "garip, nadir bir şey getirmek (if'âl; agrabe yugribu)", 5),
 "qasim": need("qasim", "الْقَاسِم", None, "propn", "al-Qasim — in the kunya Abu l-Qasim", "Kâsım — Ebü'l-Kâsım künyesinde", 5),
 "azmaa": need("azmaa", "أَزْمَعَ", "ز م ع", "verb", "to resolve firmly on (Form IV; أَزْمَعَ الْأَمْرَ / عَلَيْهِ)", "kesin karar vermek (if'âl; ezmea'l-emre / aleyhi)", 6),
 "ma-zaida": need("ma-zaida", "مَا (الزَّائِدَة)", None, "part", "the extra ma — added for emphasis, governing nothing (مِنْ غَيْرِ مَا جُرْمٍ)", "zâid mâ — te'kîd için eklenir, amel etmez (min gayri mâ curmin)", 5),
 "jurm": need("jurm", "جُرْم", "ج ر م", "noun", "a crime, an offence (pl. أَجْرَام)", "suç, cürüm (ç. أَجْرَام)", 4, plural="أَجْرَام"),
 "tabaddala": need("tabaddala", "تَبَدَّلَ", "ب د ل", "verb", "to take in exchange (Form V; تَبَدَّلَ بِهِ غَيْرَهُ)", "değiştirmek, yerine almak (tefa''ul; tebeddele bihi gayrahu)", 5),
 "hasb": need("hasb", "حَسْب", "ح س ب", "noun", "sufficiency — حَسْبُنَا اللهُ: God is enough for us", "yeterlik — hasbunallâh: Allah bize yeter", 4),
 "nima-verb": need("nima-verb", "نِعْمَ", "ن ع م", "verb", "«how excellent is …» — the frozen verb of praise", "«ne güzeldir …» — câmid medih fiili", 3),
 "wakil": need("wakil", "وَكِيل", "و ك ل", "noun", "a trustee, one relied upon (فَعِيل; pl. وُكَلَاء)", "vekil, güvenilip iş bırakılan (fa'îl; ç. وُكَلَاء)", 4, plural="وُكَلَاء"),
 "shaha": need("shaha", "شَاهَ", "ش و ه", "verb", "to be disfigured, to turn ugly (hollow; شَاهَ يَشُوهُ)", "çirkinleşmek, bozulmak (ecvef; şâhe yeşûhu)", 6),
 "qabuha": need("qabuha", "قَبُحَ", "ق ب ح", "verb", "to be ugly (قَبُحَ يَقْبُحُ)", "çirkin olmak (kabuha yakbuhu)", 4),
 "luka": need("luka", "لُكَع", "ل ك ع", "noun", "a base, ignoble man (فُعَل)", "alçak, soysuz adam (fu'al)", 6),
 "abbad": need("abbad", "عَبَّاد", None, "propn", "ʿAbbad — in Ibn ʿAbbad, the Sahib, Buyid vizier and man of letters (d. 385 AH)", "Abbâd — İbn Abbâd adında; Sâhib, Büveyhî veziri ve edîb (ö. 385)", 6),
 "raqib": need("raqib", "رَقِيب", "ر ق ب", "noun", "a watcher, a chaperon (فَعِيل)", "gözcü, bekçi (fa'îl)", 4),
 "dara-iii": need("dara-iii", "دَارَى", "د ر ي", "verb", "to humour, to treat gently (Form III, naqis; دَارَى يُدَارِي)", "idare etmek, yumuşak davranmak (mufâale, nâkıs; dârâ yudârî)", 5),
 "haffa": need("haffa", "حَفَّ", "ح ف ف", "verb", "to surround, to hedge about (doubled; حَفَّ يَحُفُّ)", "çevrelemek, kuşatmak (muzâaf; haffe yehuffu)", 5),
 "makrah": need("makrah", "مَكْرَه", "ك ر ه", "noun", "a hateful thing (masdar mimi; pl. مَكَارِه)", "hoşa gitmeyen şey (mimli masdar; ç. مَكَارِه)", 5, plural="مَكَارِه"),
 "ahad": need("ahad", "أَحَد", "أ ح د", "noun", "one — أَحَدُهُمَا: one of the two", "biri — ahaduhumâ: ikisinden biri", 2),
 "muqtabas": need("muqtabas", "مُقْتَبَس", "ق ب س", "noun", "what is taken over (ism maf'ul of Form VIII اقْتَبَسَ)", "iktibas edilen (iftiâl ism-i mef'ûlü)", 5),
 "asli": need("asli", "أَصْلِيّ", "أ ص ل", "noun", "original (the nisba of أَصْل)", "asıl, aslî (asl'ın nisbesi)", 3),
 "marra": need("marra", "مَرَّ", "م ر ر", "verb", "to pass (doubled; مَرَّ يَمُرُّ) — كَمَا مَرَّ: as has passed", "geçmek (muzâaf; merre yemurru) — kemâ merre: geçtiği gibi", 3),
 "khilaf": need("khilaf", "خِلَاف", "خ ل ف", "noun", "the contrary, the opposite; disagreement", "aksi, zıddı; ihtilaf", 3),
 "rumi": need("rumi", "الرُّومِيّ", None, "propn", "al-Rumi — in Ibn al-Rumi, the ʿAbbasid poet (d. 283 AH)", "Rûmî — İbnü'r-Rûmî adında, Abbâsî şairi (ö. 283)", 5),
 "akhtaa": need("akhtaa", "أَخْطَأَ", "خ ط أ", "verb", "to err, to miss the mark (Form IV; أَخْطَأَ يُخْطِئُ)", "hata etmek, ıskalamak (if'âl; ahtae yuhtiu)", 3),
 "man-refusal": need("man-refusal", "مَنْع", "م ن ع", "noun", "refusal, withholding (masdar of مَنَعَ)", "men, geri çevirme, vermeme (menea masdarı)", 3),
 "wadi-valley": need("wadi-valley", "وَادٍ", "و د ي", "noun", "a valley (manqus; pl. أَوْدِيَة)", "vadi (mankûs; ç. أَوْدِيَة)", 3, plural="أَوْدِيَة"),
 "zar": need("zar", "زَرْع", "ز ر ع", "noun", "tillage, sown crop (masdar of زَرَعَ)", "ekin, ekme (zerea masdarı)", 3),
 "bas": need("bas", "بَأْس", "ب أ س", "noun", "harm; might — لَا بَأْسَ: no harm", "beis, sakınca; güç — lâ be'se: sakınca yok", 3),
 "yasir": need("yasir", "يَسِير", "ي س ر", "noun", "small, slight, easy (فَعِيل)", "küçük, az, kolay (fa'îl)", 3),
 "wazn": need("wazn", "وَزْن", "و ز ن", "noun", "the metre; weight, measure (masdar of وَزَنَ)", "vezin; ağırlık, ölçü (vezene masdarı)", 3),
 "maghribi": need("maghribi", "مَغْرِبِيّ", "غ ر ب", "noun", "a Maghribi, a westerner (nisba of الْمَغْرِب; pl. مَغَارِبَة)", "Mağribli (Mağrib'in nisbesi; ç. مَغَارِبَة)", 4, plural="مَغَارِبَة"),
 "raji": need("raji", "رَاجِع", "ر ج ع", "noun", "returning (ism fa'il of رَجَعَ; pl. رَاجِعُونَ)", "dönen (racea'nın ism-i fâili; ç. رَاجِعُونَ)", 3, plural="رَاجِعُونَ"),
 "tanbih": need("tanbih", "تَنْبِيه", "ن ب ه", "noun", "a note, an alerting (masdar of Form II نَبَّهَ)", "uyarı, tenbih (tef'îl masdarı)", 3),
 "mashhur": need("mashhur", "مَشْهُور", "ش ه ر", "noun", "famous (ism maf'ul of شَهَرَ)", "meşhur (şehera'nın ism-i mef'ûlü)", 3),
 "baligh": need("baligh", "بَلِيغ", "ب ل غ", "noun", "eloquent (فَعِيل; pl. بُلَغَاء)", "beliğ, belâgatli (fa'îl; ç. بُلَغَاء)", 4, plural="بُلَغَاء"),
 "bay": need("bay", "بَيْع", "ب ي ع", "noun", "a sale (masdar of بَاعَ)", "satış (bâa masdarı)", 2),
 "adaa-lose": need("adaa-lose", "أَضَاعَ", "ض ي ع", "verb", "to lose, to let go to waste (Form IV, hollow; أَضَاعَ يُضِيعُ)", "ziyan etmek, kaybetmek (if'âl, ecvef; edâa yudîu)", 4),
 "ayy": need("ayy", "أَيّ", None, "noun", "which; what a … (annexed; أَيَّ فَتًى: what a youth!)", "hangi; ne … (muzâf; eyye feten: ne genç!)", 3),
 "ahsan": need("ahsan", "أَحْسَن", "ح س ن", "noun", "finer, finest (the elative of حَسَن)", "daha güzel, en güzel (hasen'in ism-i tafdîli)", 2),
 "isba-name": need("isba-name", "الْإِصْبَع", None, "propn", "al-Isbaʿ — in Ibn Abi l-Isbaʿ al-Misri, author of Tahrir al-Tahbir (d. 654 AH)", "İsba' — İbn Ebi'l-İsba' el-Mısrî adında, Tahrîrü't-Tahbîr'in yazarı (ö. 654)", 6),
 "wahm": need("wahm", "وَهْم", "و ه م", "noun", "fancy, imagination; a false notion (pl. أَوْهَام)", "vehim, kuruntu; hayal (ç. أَوْهَام)", 4, plural="أَوْهَام"),
 "abda": need("abda", "أَبْدَى", "ب د و", "verb", "to show, to reveal (Form IV, naqis; أَبْدَى يُبْدِي)", "göstermek, açığa vurmak (if'âl, nâkıs; ebdâ yubdî)", 4),
 "lama-lip": need("lama-lip", "لَمًى", "ل م ي", "noun", "the darkness of the lip, prized as beauty (maqsur)", "dudak esmerliği, güzellik sayılır (maksûr)", 6),
 "tadhakkara": need("tadhakkara", "تَذَكَّرَ", "ذ ك ر", "verb", "to remember (Form V; تَذَكَّرَ يَتَذَكَّرُ)", "hatırlamak (tefa''ul; tezekkere yetezekkeru)", 3),
 "udhayb": need("udhayb", "الْعُذَيْب", None, "propn", "al-ʿUdhayb — a water on the road to Kufa", "Uzeyb — Kûfe yolunda bir su", 6),
 "bariq": need("bariq", "بَارِق", None, "propn", "Bariq — a place near Kufa", "Bârık — Kûfe yakınında bir yer", 6),
 "dhakkara-iv": need("dhakkara-iv", "أَذْكَرَ", "ذ ك ر", "verb", "to remind of (Form IV; أَذْكَرَهُ الشَّيْءَ — two objects)", "hatırlatmak (if'âl; ezkerehu'ş-şey'e — iki mef'ûl)", 4),
 "majarr": need("majarr", "مَجَرّ", "ج ر ر", "noun", "a dragging, a trailing (masdar mimi of جَرَّ)", "sürükleme, çekme (cerre'nin mimli masdarı)", 6),
 "aliya": need("aliya", "عَالِيَة", "ع ل و", "noun", "the upper part of a spear (pl. عَوَالٍ)", "mızrağın üst kısmı (ç. عَوَالٍ)", 6, plural="عَوَالٍ"),
 "majra": need("majra", "مَجْرَى", "ج ر ي", "noun", "a course, a running (masdar mimi of جَرَى; maqsur)", "akış, koşu (cerâ'nın mimli masdarı; maksûr)", 4),
 "darra": need("darra", "ضَرَّ", "ض ر ر", "verb", "to harm (doubled; ضَرَّ يَضُرُّ)", "zarar vermek (muzâaf; darre yedurru)", 3),
 "bayt": need("bayt", "بَيْت", "ب ي ت", "noun", "a bayt, a verse of two hemistichs; a house (pl. أَبْيَات)", "beyit; ev (ç. أَبْيَات)", 2, plural="أَبْيَات"),
 "istiana": need("istiana", "اسْتِعَانَة", "ع و ن", "noun", "istiʿana — seeking aid (masdar of Form X اسْتَعَانَ); of the tadmin: a whole bayt or more woven in", "istiâne — yardım isteme (istif'âl masdarı); tazminde: bir beyit yahut fazlasının katılması", 5),
 "misra": need("misra", "مِصْرَاع", "ص ر ع", "noun", "a hemistich, half a bayt (pl. مَصَارِيع)", "mısra, beytin yarısı (ç. مَصَارِيع)", 4, plural="مَصَارِيع"),
 "ida-deposit": need("ida-deposit", "إِيدَاع", "و د ع", "noun", "idaʿ — a depositing (masdar of Form IV أَوْدَعَ); of the tadmin: a hemistich or less woven in", "îdâ' — emanet bırakma (if'âl masdarı); tazminde: bir mısra yahut azının katılması", 5),
 "rafw": need("rafw", "رَفْو", "ر ف و", "noun", "rafw — darning a garment (masdar of رَفَا); of the tadmin: the small piece woven in", "refv — giysiyi yamama (refâ masdarı); tazminde: katılan küçük parça", 6),
 "nazama": need("nazama", "نَظَمَ", "ن ظ م", "verb", "to string, to put into verse (نَظَمَ يَنْظِمُ)", "dizmek, nazma çekmek (nazame yanzimu)", 3),
 "tariq": need("tariq", "طَرِيق", "ط ر ق", "noun", "a way, a road (pl. طُرُق)", "yol (ç. طُرُق)", 2, plural="طُرُق"),
 "atahiya": need("atahiya", "الْعَتَاهِيَة", None, "propn", "al-ʿAtahiya — in Abu l-ʿAtahiya, the ʿAbbasid poet of renunciation (d. 211 AH)", "Atâhiye — Ebü'l-Atâhiye adında, zühd şairi (ö. 211)", 5),
 "ma-istifham": need("ma-istifham", "مَا (الِاسْتِفْهَامِيَّة)", None, "noun", "the interrogative ma — «what?»", "istifhâm mâ'sı — «ne?»", 2),
 "bal-state": need("bal-state", "بَال", "ب و ل", "noun", "state, condition — مَا بَالُهُ: what ails him", "hâl, durum — mâ bâluhu: nesi var", 4),
 "jifa": need("jifa", "جِيفَة", "ج ي ف", "noun", "a carcass (pl. جِيَف)", "leş (ç. جِيَف)", 4, plural="جِيَف"),
 "akhir": need("akhir", "آخِر", "أ خ ر", "noun", "the end, the last", "son, âhir", 2),
 "fakhara": need("fakhara", "فَخَرَ", "ف خ ر", "verb", "to boast (فَخَرَ يَفْخَرُ)", "övünmek (fahara yefharu)", 3),
 "nathara": need("nathara", "نَثَرَ", "ن ث ر", "verb", "to scatter; to put into prose (نَثَرَ يَنْثُرُ)", "saçmak; nesre çevirmek (nesera yensuru)", 3),
 "saa-bad": need("saa-bad", "سَاءَ", "س و أ", "verb", "to be bad, to turn foul (hollow; سَاءَ يَسُوءُ)", "kötü olmak, fena olmak (ecvef; sâe yesûu)", 3),
 "itada": need("itada", "اعْتَادَ", "ع و د", "verb", "to be used to (Form VIII, hollow; اعْتَادَ يَعْتَادُ)", "alışmak (iftiâl, ecvef; i'tâde ya'tâdu)", 4),
 "tawahhum": need("tawahhum", "تَوَهُّم", "و ه م", "noun", "delusion, fancying (masdar of Form V تَوَهَّمَ)", "vehim, kuruntu (tefa''ul masdarı)", 4),
 "lamma": need("lamma", "لَمَّا (الْحِينِيَّة)", None, "part", "lamma «when» — the zarf of time before a mazi", "lemmâ «-ınca» — mâzî önünde zaman zarfı", 3),
 "fala": need("fala", "فَعْلَة", "ف ع ل", "noun", "a deed, a single act (pl. فَعَلَات)", "bir fiil, tek edim (ç. فَعَلَات)", 4, plural="فَعَلَات"),
 "hanzala": need("hanzala", "حَنْظَلَ", "ح ن ظ ل", "verb", "to bear colocynth, to turn bitter (a four-radical verb)", "Ebû Cehil karpuzu vermek, acılaşmak (rubâî fiil)", 6),
 "nakhla": need("nakhla", "نَخْلَة", "ن خ ل", "noun", "a palm tree (pl. نَخَلَات / نَخْل)", "hurma ağacı (ç. نَخَلَات / نَخْل)", 3, plural="نَخَلَات"),
 "zala": need("zala", "زَالَ", "ز و ل", "verb", "to cease (hollow; زَالَ يَزَالُ — مَا زَالَ: did not cease, a sister of كَانَ)", "son bulmak (ecvef; zâle yezâlu — mâ zâle: devam etti, kânenin kız kardeşi)", 3),
 "zann": need("zann", "ظَنّ", "ظ ن ن", "noun", "a thought, a supposition (masdar of ظَنَّ; pl. ظُنُون)", "zan, sanı (zanne masdarı; ç. ظُنُون)", 3, plural="ظُنُون"),
 "su": need("su", "سُوء", "س و أ", "noun", "evil, ill — سُوءُ الظَّنِّ: ill thought", "kötülük — sûü'z-zann: sûizan", 3),
 "iqtada": need("iqtada", "اقْتَادَ", "ق و د", "verb", "to lead along (Form VIII, hollow; اقْتَادَ يَقْتَادُ)", "sürüklemek, çekip götürmek (iftiâl, ecvef; iktâde yaktâdu)", 5),
 "ashara-point": need("ashara-point", "أَشَارَ", "ش و ر", "verb", "to point at, to indicate (Form IV, hollow; أَشَارَ إِلَيْهِ يُشِيرُ)", "işaret etmek (if'âl, ecvef; eşâra ileyhi yuşîru)", 3),
 "qissa": need("qissa", "قِصَّة", "ق ص ص", "noun", "a story (pl. قِصَص)", "kıssa, hikâye (ç. قِصَص)", 2, plural="قِصَص"),
 "wa-qasam": need("wa-qasam", "وَ (الْقَسَم)", None, "part", "the waw of the oath — وَاللهِ: by God", "kasem vâvı — vallâhi", 3),
 "hulm": need("hulm", "حُلْم", "ح ل م", "noun", "a dream (pl. أَحْلَام)", "rüya (ç. أَحْلَام)", 3, plural="أَحْلَام"),
 "naim-sleeper": need("naim-sleeper", "نَائِم", "ن و م", "noun", "a sleeper (ism fa'il of نَامَ)", "uyuyan (nâme'nin ism-i fâili)", 3),
 "alamma": need("alamma", "أَلَمَّ", "ل م م", "verb", "to alight upon, to visit (Form IV, doubled; أَلَمَّ بِهِ يُلِمُّ)", "uğramak, gelip çatmak (if'âl, muzâaf; elemme bihi yulimmu)", 5),
 "am": need("am", "أَمْ", None, "part", "or — the am that answers an interrogative hamza", "yoksa — hemzeye muâdil em", 3),
 "rakb": need("rakb", "رَكْب", "ر ك ب", "noun", "a caravan of riders (a collective; pl. رُكُوب)", "kervan, binitliler (topluluk ismi; ç. رُكُوب)", 4),
 "yusha": need("yusha", "يُوشَع", None, "propn", "Joshua (Yushaʿ b. Nun), for whom the sun was held back — a diptote foreign name", "Yûşa' b. Nûn, güneş onun için durdurulmuştu — gayr-i munsarif yabancı ad", 5),
 "amr-name": need("amr-name", "عَمْرو", None, "propn", "ʿAmr — a man's name, spelt with a silent waw to tell it from ʿUmar", "Amr — Ömer'den ayırmak için yazıda sessiz vâv alan erkek adı", 4),
 "ramda": need("ramda", "رَمْضَاء", "ر م ض", "noun", "burning sand, ground scorched by the sun (mamdud)", "kızgın kum, güneşten yanmış yer (memdûd)", 5),
 "iltaza": need("iltaza", "الْتَظَى", "ل ظ ي", "verb", "to blaze, to flare (Form VIII, naqis; الْتَظَتِ النَّارُ)", "alevlenmek (iftiâl, nâkıs; iltezati'n-nâr)", 6),
 "araqq": need("araqq", "أَرَقّ", "ر ق ق", "noun", "gentler, more tender (the elative of رَقِيق)", "daha yumuşak, daha nazik (rakîk'in ism-i tafdîli)", 4),
 "ahfa": need("ahfa", "أَحْفَى", "ح ف و", "noun", "kinder, more attentive (the elative of حَفِيّ; maqsur)", "daha şefkatli, daha ilgili (hafî'nin ism-i tafdîli; maksûr)", 5),
 "saa-hour": need("saa-hour", "سَاعَة", "س و ع", "noun", "an hour, a while (pl. سَاعَات)", "saat, bir süre (ç. سَاعَات)", 2, plural="سَاعَات"),
 "karb": need("karb", "كَرْب", "ك ر ب", "noun", "distress, anguish (pl. كُرُوب)", "sıkıntı, keder (ç. كُرُوب)", 4, plural="كُرُوب"),
 "mustajir": need("mustajir", "مُسْتَجِير", "ج و ر", "noun", "one who seeks refuge (ism fa'il of Form X اسْتَجَارَ)", "sığınan, himaye isteyen (istif'âl ism-i fâili)", 5),
 "kurba": need("kurba", "كُرْبَة", "ك ر ب", "noun", "a distress (pl. كُرَب)", "sıkıntı, tasa (ç. كُرَب)", 4, plural="كُرَب"),
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

# ---------------------------------------------------------------- paradigms
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "dammana", _sg.derived(_sg.B2, _sg.W2, "ُ", "ضَمَّن", "ضَمِّن", "ضَمِّن", "تَضْمِين", "مُضَمِّن", "مُضَمَّن", "ضُمِّنَ", "يُضَمَّنُ", "ضَمَّنَ يُضَمِّنُ — يَتَعَدَّى إِلَى مَفْعُولَيْنِ."))
put_morph(mo, "anshada", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْشَد", "نْشِد", "أَنْشِد", "إِنْشَاد", "مُنْشِد", "مُنْشَد", "أُنْشِدَ", "يُنْشَدُ", "أَنْشَدَ يُنْشِدُ الشِّعْرَ."))
put_morph(mo, "aghraba", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَغْرَب", "غْرِب", "أَغْرِب", "إِغْرَاب", "مُغْرِب", None, None, None, "أَغْرَبَ يُغْرِبُ: أَتَى بِالْغَرِيبِ."))
put_morph(mo, "azmaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَزْمَع", "زْمِع", "أَزْمِع", "إِزْمَاع", "مُزْمِع", "مُزْمَع", "أُزْمِعَ", "يُزْمَعُ", "أَزْمَعَ يُزْمِعُ: عَزَمَ."))
put_morph(mo, "tabaddala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَدَّل", "تَبَدَّل", "تَبَدَّل", "تَبَدُّل", "مُتَبَدِّل", "مُتَبَدَّل", "تُبُدِّلَ", "يُتَبَدَّلُ", "تَبَدَّلَ يَتَبَدَّلُ."))
put_morph(mo, "shaha", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "شَاه", "شُه", "شُوه", "شُه", "شُوه", "شُه", "شَوْه", "شَائِه", None, None, None, "شَاهَ يَشُوهُ: قَبُحَ — أَجْوَفٌ وَاوِيٌّ."))
put_morph(mo, "qabuha", _sg.sound1("karuma", "قَبُح", "قْبُح", "اُقْبُح", "قُبْح", "قَبِيح", None, "قُبِحَ", "يُقْبَحُ", "قَبُحَ يَقْبُحُ — مِنْ بَابِ حَسُنَ؛ صِفَتُهُ قَبِيحٌ."))
put_morph(mo, "haffa", gem("nasara", "حَفّ", "حَفَف", "حُفّ", "حْفُف", ["حُفَّ", "حُفَّا", "حُفُّوا", "حُفِّي", "حُفَّا", "اُحْفُفْنَ"], "حَفّ", "حَافّ", "مَحْفُوف", "حُفَّ", "يُحَفُّ", "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: حَفَّ يَحُفُّ — مَجْهُولُهُ حُفَّ."))
put_morph(mo, "marra", gem("nasara", "مَرّ", "مَرَر", "مُرّ", "مْرُر", ["مُرَّ", "مُرَّا", "مُرُّوا", "مُرِّي", "مُرَّا", "اُمْرُرْنَ"], "مُرُور", "مَارّ", None, None, None, "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: مَرَّ يَمُرُّ."))
put_morph(mo, "akhtaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَخْطَأ", "خْطِئ", "أَخْطِئ", "إِخْطَاء", "مُخْطِئ", "مُخْطَأ", "أُخْطِئَ", "يُخْطَأُ", "أَخْطَأَ يُخْطِئُ — مَهْمُوزُ اللَّامِ."))
put_morph(mo, "darra", gem("nasara", "ضَرّ", "ضَرَر", "ضُرّ", "ضْرُر", ["ضُرَّ", "ضُرَّا", "ضُرُّوا", "ضُرِّي", "ضُرَّا", "اُضْرُرْنَ"], "ضَرّ", "ضَارّ", "مَضْرُور", "ضُرَّ", "يُضَرُّ", "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: ضَرَّ يَضُرُّ."))
put_morph(mo, "nazama", _sg.sound1("daraba", "نَظَم", "نْظِم", "اِنْظِم", "نَظْم", "نَاظِم", "مَنْظُوم", "نُظِمَ", "يُنْظَمُ", "نَظَمَ يَنْظِمُ — مِنْ بَابِ ضَرَبَ؛ مَجْهُولُهُ يُنْظَمُ."))
put_morph(mo, "fakhara", _sg.sound1("fataha", "فَخَر", "فْخَر", "اِفْخَر", "فَخْر", "فَاخِر", None, None, None, "فَخَرَ يَفْخَرُ — مِنْ بَابِ فَتَحَ."))
put_morph(mo, "nathara", _sg.sound1("nasara", "نَثَر", "نْثُر", "اُنْثُر", "نَثْر", "نَاثِر", "مَنْثُور", "نُثِرَ", "يُنْثَرُ", "نَثَرَ يَنْثُرُ — مِنْ بَابِ نَصَرَ؛ مَجْهُولُهُ يُنْثَرُ."))
put_morph(mo, "saa-bad", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "سَاء", "سُؤ", "سُوء", "سُؤ", "سُوء", "سُؤ", "سَوْء", "سَيِّئ", None, None, None, "سَاءَ يَسُوءُ: قَبُحَ — أَجْوَفٌ وَاوِيٌّ مَهْمُوزُ اللَّامِ."))
put_morph(mo, "itada", _sg.derived_hollow("الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِعْتَاد", "اِعْتَد", "عْتَاد", "عْتَد", "اِعْتَاد", "اِعْتَد", "اعْتِيَاد", "مُعْتَاد", "مُعْتَاد", "اعْتِيدَ", "يُعْتَادُ", "اعْتَادَ يَعْتَادُ — أَجْوَفٌ مِنْ بَابِ الِافْتِعَالِ."))
put_morph(mo, "hanzala", _sg.derived("الرُّبَاعِيُّ الْمُجَرَّدُ: فَعْلَلَ يُفَعْلِلُ", "فَعْلَلَ يُفَعْلِلُ", "ُ", "حَنْظَل", "حَنْظِل", "حَنْظِل", "حَنْظَلَة", "مُحَنْظِل", None, None, None, "حَنْظَلَ يُحَنْظِلُ: صَارَ حَنْظَلًا — رُبَاعِيٌّ مُجَرَّدٌ."))
put_morph(mo, "iqtada", _sg.derived_hollow("الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِقْتَاد", "اِقْتَد", "قْتَاد", "قْتَد", "اِقْتَاد", "اِقْتَد", "اقْتِيَاد", "مُقْتَاد", "مُقْتَاد", "اقْتِيدَ", "يُقْتَادُ", "اقْتَادَ يَقْتَادُ — أَجْوَفٌ مِنْ بَابِ الِافْتِعَالِ."))
put_morph(mo, "ashara-point", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَشَار", "أَشَر", "شِير", "شِر", "أَشِير", "أَشِر", "إِشَارَة", "مُشِير", "مُشَار (إِلَيْهِ)", "أُشِيرَ", "يُشَارُ", "أَشَارَ يُشِيرُ — أَجْوَفٌ مِنْ بَابِ الْإِفْعَالِ."))
_al = _sg.derived_hollow(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "ُ", "أَلَمّ", "أَلْمَم", "لِمّ", "لْمِم", "أَلِمّ", "أَلْمِم", "إِلْمَام", "مُلِمّ", "مُلَمّ (بِهِ)", None, None, "أَلَمَّ يُلِمُّ بِهِ: نَزَلَ بِهِ — مُضَاعَفٌ مِنْ بَابِ الْإِفْعَالِ.")
_al["amr"][0] = "أَلِمَّ"; _al["majzum"] = "يُلِمَّ"; _al["majzum2"] = "تُلِمَّ"
put_morph(mo, "alamma", _al)
# نِعْمَ: the frozen verb of praise — a mazi that never leaves the third person (نِعْمَ الرَّجُلُ، نِعْمَتِ الْمَرْأَةُ، نِعْمَا، نِعْمُوا، نِعْمَتَا، نِعْمْنَ)
put_morph(mo, "nima-verb", {"jamid": True, "bab": "فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ", "wazn": "فَعِلَ (أَصْلُهُ نَعِمَ)",
  "mazi": ["نِعْمَ", "نِعْمَا", "نِعْمُوا", "نِعْمَتْ", "نِعْمَتَا", "نِعْمْنَ", "—", "—", "—", "—", "—", "—", "—", "—"],
  "note": "جَامِدٌ: لَا مُضَارِعَ لَهُ وَلَا أَمْرَ وَلَا مَصْدَرَ، وَلَا يُسْنَدُ إِلَى الْمُخَاطَبِ وَلَا الْمُتَكَلِّمِ — فَاعِلُهُ مُعَرَّفٌ بِأَلْ أَوْ مُضَافٌ إِلَى مَا فِيهِ أَلْ أَوْ ضَمِيرٌ مُسْتَتِرٌ يُفَسِّرُهُ تَمْيِيزٌ، وَبَعْدَهُ الْمَخْصُوصُ بِالْمَدْحِ."})
put_morph(mo, "dara-iii", _sg.derived_naqis(_sg.B3, _sg.W3, "ُ", "دَارَ", "دَار", "i", "دَار", "مُدَارَاة", "مُدَارٍ (الْمُدَارِي)", "مُدَارًى", "دُورِيَ", "يُدَارَى", "دَارَى يُدَارِي: لَاطَفَ — نَاقِصٌ مِنْ بَابِ الْمُفَاعَلَةِ؛ أَمْرُهُ دَارِ."))
put_morph(mo, "abda", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَبْدَ", "بْد", "i", "أَبْد", "إِبْدَاء", "مُبْدٍ (الْمُبْدِي)", "مُبْدًى", "أُبْدِيَ", "يُبْدَى", "أَبْدَى يُبْدِي: أَظْهَرَ — نَاقِصٌ مِنْ بَابِ الْإِفْعَالِ."))
put_morph(mo, "dhakkara-iv", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَذْكَر", "ذْكِر", "أَذْكِر", "إِذْكَار", "مُذْكِر", "مُذْكَر", "أُذْكِرَ", "يُذْكَرُ", "أَذْكَرَ يُذْكِرُ — يَتَعَدَّى إِلَى مَفْعُولَيْنِ."))
put_morph(mo, "tadhakkara", _sg.derived(_sg.B5, _sg.W5, "َ", "تَذَكَّر", "تَذَكَّر", "تَذَكَّر", "تَذَكُّر", "مُتَذَكِّر", "مُتَذَكَّر", "تُذُكِّرَ", "يُتَذَكَّرُ", "تَذَكَّرَ يَتَذَكَّرُ."))
put_morph(mo, "adaa-lose", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَضَاع", "أَضَع", "ضِيع", "ضِع", "أَضِيع", "أَضِع", "إِضَاعَة", "مُضِيع", "مُضَاع", "أُضِيعَ", "يُضَاعُ", "أَضَاعَ يُضِيعُ — أَجْوَفٌ مِنْ بَابِ الْإِفْعَالِ."))
put_morph(mo, "iltaza", _sg.derived_naqis("الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِلْتَظَ", "لْتَظ", "i", "اِلْتَظ", "الْتِظَاء", "مُلْتَظٍ (الْمُلْتَظِي)", None, None, None, "الْتَظَى يَلْتَظِي: الْتَهَبَ — نَاقِصٌ مِنْ بَابِ الِافْتِعَالِ."))
put_morph(mo, "zala", _sg.hollow1("samia", "أَجْوَفُ يَائِيٌّ", "زَال", "زِل", "زَال", "زَل", "زَال", "زَل", "زَوَال", "زَائِل", None, None, None, "زَالَ يَزَالُ — أَجْوَفٌ مِنْ بَابِ سَمِعَ؛ مَا زَالَ مِنْ أَخَوَاتِ كَانَ."))
for _k, _v in GLOSS_ADD.items():
    if _k == "nima-verb": continue   # a frozen verb: no paradigm
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note
NOTE = {
 "id": "al-iqtibas-wal-tadmin",
 "title": {"ar": "الِاقْتِبَاسُ وَالتَّضْمِينُ وَالْعَقْدُ وَالْحَلُّ وَالتَّلْمِيحُ", "en": "The iqtibas, the tadmin, the ʿaqd, the hall and the talmih", "tr": "İktibas, tazmin, akd, hal ve telmih"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الخاتمة: ومما يتصل بالسرقات الشعرية القول في الاقتباس والتضمين والعقد والحل والتلميح"],
 "question": {
  "en": ["What is the IQTIBAS? Qurʾan or hadith woven into one's speech without saying it is from there — in prose (al-Hariri's «as the twinkling of an eye, or nearer», «may the faces be disfigured») or in verse (Abu l-Qasim's «then fair patience», «God is sufficient for us, and excellent the Trustee»; Ibn ʿAbbad's «the Garden is hedged with hateful things»). Two kinds: the taken words keep their meaning (all of these) or are MOVED from it (Ibn al-Rumi's «a valley without tillage» — no water in the aya, no profit in the bayt). A small change for the metre is allowed («to God are we returning» for «to Him»).",
         "What is the TADMIN? Another's VERSE woven into one's own, flagged if it is not famous: al-Hariri weaves al-ʿArji's hemistich «they have lost me — and what a youth they have lost»; Ibn Abi l-Isbaʿ weaves al-Mutanabbi's whole bayt and betters it with a tawriya and a tashbih. A bayt or more is ISTIʿANA; a hemistich or less is IDAʿ or RAFW.",
         "What are the ʿAQD, the HALL and the TALMIH? The ʿaqd: prose put into verse, not as an iqtibas (Abu l-ʿAtahiya versifies ʿAli's «what has the son of Adam to do with boasting?»). The hall: verse put into prose (a Maghribi unties al-Mutanabbi's «when a man's deeds are foul, his thoughts turn foul»). The talmih: a story or verse pointed at without naming it (Joshua and the halted sun; «he who seeks refuge with ʿAmr»).",
         "What does the engine read? The IqtibasEngine keeps a table of received spans (the ayas and hadiths the chapters cite) and finds them in the sentence, one word at a time, reporting the source, whether the words were changed, and — for the tadmin — whether a whole bayt (istiʿana) or a part (idaʿ) was woven in. The ʿaqd, hall and talmih are authored frames the engine confirms by the source they name."],
  "tr": ["İKTİBAS nedir? Kur'ân yahut hadisin, oradan olduğu söylenmeden söze katılması — nesirde (Harîrî'nin «göz açıp kapayıncaya kadar yahut daha az», «yüzler çirkinleşsin») yahut nazımda (Ebü'l-Kâsım'ın «güzel bir sabır», «Allah bize yeter, ne güzel vekildir»; İbn Abbâd'ın «cennet hoşa gitmeyenlerle çevrilidir»). İki tür: alınan lafız manasını korur (bunların hepsi) yahut manasından NAKLEDİLİR (İbnü'r-Rûmî'nin «ekini olmayan vadi»si — âyette su yok, beyitte fayda yok). Vezin için küçük değişiklik câizdir («Allah'a dönücüleriz»).",
         "TAZMİN nedir? Başkasının ŞİİRİNİN kendi şiirine katılması, meşhur değilse uyarıyla: Harîrî Arcî'nin «beni ziyan ettiler — ne genci ziyan ettiler» mısraını katar; İbn Ebi'l-İsba' Mütenebbî'nin bütün beytini katar, tevriye ve teşbihle güzelleştirir. Bir beyit yahut fazlası İSTİÂNE; bir mısra yahut azı ÎDÂ' yahut REFV.",
         "AKD, HAL ve TELMİH nedir? Akd: nesrin iktibas olmaksızın nazma çekilmesi (Ebü'l-Atâhiye, Hz. Ali'nin «Âdemoğlunun övünmekle ne işi var»ını nazmeder). Hal: nazmın nesre çevrilmesi (bir Mağribli Mütenebbî'nin «kişinin fiili kötü olunca zanları kötü olur»unu çözer). Telmih: bir kıssaya yahut şiire anmadan işaret (Yûşa' ve durdurulan güneş; «Amr'a sığınan»).",
         "Motor neyi okur? IqtibasEngine alınan pasajların tablosunu tutar (bâbların andığı âyet ve hadisler) ve onları cümlede kelime kelime bulur; kaynağı, lafzın değişip değişmediğini ve tazminde bütün beyit (istiâne) mi yoksa parça (îdâ') mı katıldığını bildirir. Akd, hal ve telmih yazarın çerçeveleridir; motor adlandırdıkları kaynakla doğrular."]},
 "plain": {
  "en": "Quoting scripture or hadith into your own words is iqtibas; quoting another poet is tadmin; versifying prose is ʿaqd; prosing verse is hall; hinting at a story without naming it is talmih.",
  "tr": "Kendi sözüne Kur'ân yahut hadis katmak iktibas; başka şairden katmak tazmin; nesri nazma çekmek akd; nazmı nesre çevirmek hal; bir kıssaya anmadan işaret telmihtir."},
 "explanation": {
  "en": "وَمِمَّا يَتَّصِلُ بِالسَّرِقَاتِ الشِّعْرِيَّةِ: الْقَوْلُ فِي الِاقْتِبَاسِ وَالتَّضْمِينِ وَالْعَقْدِ وَالْحَلِّ وَالتَّلْمِيحِ. After the takings the Talkhis lists five ways of building on another's words that are no theft: the Qurʾan and hadith woven in without attribution (iqtibas), another poet's verse woven in and flagged (tadmin), prose versified (ʿaqd), verse prosed (hall), a story or verse hinted at (talmih). The rulings are RESTORED from the received matn and marked; the Qurʾanic text prints as the source prints it, with two Ottoman misprints corrected and recorded. The reader lights the received span inside the sentence and names its source.",
  "tr": "وَمِمَّا يَتَّصِلُ بِالسَّرِقَاتِ الشِّعْرِيَّةِ: الْقَوْلُ فِي الِاقْتِبَاسِ وَالتَّضْمِينِ وَالْعَقْدِ وَالْحَلِّ وَالتَّلْمِيحِ. Sirkatlerden sonra Telhîs, başkasının sözü üzerine kurulan ve hırsızlık olmayan beş yolu sayar: nispet edilmeden katılan Kur'ân ve hadis (iktibas), uyarıyla katılan başka şairin şiiri (tazmin), nazma çekilen nesir (akd), nesre çevrilen nazım (hal), işaret edilen kıssa yahut şiir (telmih). Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; Kur'ân metni kaynağın basılı şekliyledir, Osmanlıca baskının iki yanlışı düzeltilip kaydedilmiştir. Okuyucu alınan pasajı cümle içinde yakar ve kaynağını adlandırır."},
 "examples": [
  {"ar": "فَلَمْ يَكُنْ إِلَّا كَلَمْحِ الْبَصَرِ أَوْ هُوَ أَقْرَبُ، حَتَّى أَنْشَدَ وَأَغْرَبَ", "en": "al-Hariri — an iqtibas from al-Nahl 77, in prose.", "tr": "Harîrî — Nahl 77'den iktibas, nesirde.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "لَقَدْ أَنْزَلْتُ حَاجَاتِي بِوَادٍ غَيْرِ ذِي زَرْعِ", "en": "Ibn al-Rumi — the taken words moved from their meaning.", "tr": "İbnü'r-Rûmî — alınan lafız manasından nakledilmiş.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "عَلَى أَنِّي سَأُنْشِدُ عِنْدَ بَيْعِي * أَضَاعُونِي وَأَيَّ فَتًى أَضَاعُوا", "en": "al-Hariri — a tadmin of idaʿ: al-ʿArji's hemistich.", "tr": "Harîrî — îdâ' tazmini: Arcî'nin mısraı.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"},
  {"ar": "مَا بَالُ مَنْ أَوَّلُهُ نُطْفَةٌ * وَجِيفَةٌ آخِرُهُ يَفْخَرُ", "en": "Abu l-ʿAtahiya — an ʿaqd of ʿAli's saying.", "tr": "Ebü'l-Atâhiye — Hz. Ali'nin sözünün akdi.", "sourceStory": "talkhis-al-miftah", "sentence": "s21"},
  {"ar": "فَوَاللهِ مَا أَدْرِي أَأَحْلَامُ نَائِمٍ * أَلَمَّتْ بِنَا أَمْ كَانَ فِي الرَّكْبِ يُوشَعُ", "en": "Abu Tammam — a talmih to Joshua's halted sun.", "tr": "Ebû Temmâm — Yûşa'ın durdurulan güneşine telmih.", "sourceStory": "talkhis-al-miftah", "sentence": "s26"}],
 "commonMistakes": [
  {"wrong": "«Şair âyeti şiirine koydu: bu bir sirkattir»",
   "right": "«لَا عَلَى أَنَّهُ مِنْهُ — Kur'ân'dan olduğu söylenmeden katılan iktibastır, sirkat değil»",
   "why": {"en": "The iqtibas is defined by not attributing; it is a figure, and the book lists it beside the takings precisely to set it apart.", "tr": "İktibas nispet edilmemekle tanımlanır; bir sanattır, kitap onu sirkatlerden ayırmak için yanlarında sayar."}},
  {"wrong": "«Başkasının bir mısraını almak istiânedir»",
   "right": "«تَضْمِينُ الْبَيْتِ فَمَا زَادَ اسْتِعَانَةٌ، وَالْمِصْرَاعِ فَمَا دُونَهُ إِيدَاعٌ — bir mısra yahut azı îdâ' ve refvdir»",
   "why": {"en": "The two names are cut by length: a whole bayt or more is istiʿana, a hemistich or less is idaʿ / rafw.", "tr": "İki ad uzunlukla ayrılır: bir beyit yahut fazlası istiâne, bir mısra yahut azı îdâ' / refv."}}],
 "relatedNotes": ["sariqat-shiriyya", "sariqat-ghayr-zahira", "ilm-al-arud"]}

ADD_EN = (" Chapter 75 (lines ~4750-4820, sahifa 164-166): the iqtibas (s1-s13; al-Hariri, Abu l-Qasim, Ibn ʿAbbad, Ibn al-Rumi, a Maghribi), the tadmin "
          "(s14-s19; al-Hariri / al-ʿArji, Ibn Abi l-Isbaʿ / al-Mutanabbi), the ʿaqd (s20-s21; Abu l-ʿAtahiya / ʿAli), the hall (s22-s24; al-Mutanabbi and "
          "the Maghribi's prose, RESTORED) and the talmih (s25-s28; Abu Tammam). The rulings are RESTORED from the received matn and marked. Two misprints "
          "of the Ottoman print are corrected and recorded: خُفَّتْ → حُفَّتْ (s8, the received hadith) and ذِي restored in بِوَادٍ غَيْرِ ذِي زَرْعٍ (s11, the aya and the metre). "
          "The `badi` frames iqtibas / tadmin / aqd / hall / talmih carry the received span in `set` and its `source`.")
ADD_TR = (" Yetmiş beşinci bâb (satır ~4750-4820, sahife 164-166): iktibas (s1-s13; Harîrî, Ebü'l-Kâsım, İbn Abbâd, İbnü'r-Rûmî, bir Mağribli), tazmin "
          "(s14-s19; Harîrî / Arcî, İbn Ebi'l-İsba' / Mütenebbî), akd (s20-s21; Ebü'l-Atâhiye / Hz. Ali), hal (s22-s24; Mütenebbî ve Mağriblinin nesri, GERİ "
          "YAZILMIŞ) ve telmih (s25-s28; Ebû Temmâm). Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir. Osmanlıca baskının iki yanlışı düzeltilip "
          "kaydedilmiştir: خُفَّتْ → حُفَّتْ (s8, alınan hadis) ve بِوَادٍ غَيْرِ ذِي زَرْعٍ'de ذِي geri konmuştur (s11, âyet ve vezin). `badi` çerçeveleri iqtibas / tadmin / aqd / hall / "
          "talmih alınan pasajı `set`te ve kaynağını `source`ta taşır.")
write_out(75, S, TITLE, ADD_EN, ADD_TR, "4750-4820", GLOSS_ADD, notes=(NOTE,),
          related=(("sariqat-shiriyya", ["al-iqtibas-wal-tadmin"]), ("sariqat-ghayr-zahira", ["al-iqtibas-wal-tadmin"]), ("ilm-al-badi", ["al-iqtibas-wal-tadmin"])))
report(75, S, GLOSS_ADD, (NOTE,))
