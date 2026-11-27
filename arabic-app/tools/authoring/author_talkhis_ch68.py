# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 68: the LAFZI MUHASSINAT open — JINAS: its definition; the TAMM (mumathil, mustawfa; the murakkab's
mutashabih and mafruq), the MUHARRAF, the NAQIS (the extra letter first, middle, last = mutarraf; more than one letter = mudhayyal).
Source lines ~4395-4445 (sahifa 152-153).

  RESTORED (the source carries the step only in Turkish): s1 (the definition), s2 (the tamm), s3, s5, s7, s9, s11, s15, s19 (the
  headings of the kinds). The examples (s4 30:55, s6 Abu Tammam, s8 al-Busti, s10 al-Busti, s12-s14 the sayings, s16 75:29-30, s17,
  s18 Abu Tammam, s20 al-Khansa) are the source's printed Arabic; the Qur'an as the source prints it. The verb يَحْيَى (s6) is
  written with the alif maqsura as the source prints it — the jinas of the two يَحْيَى is in the script too.

  python3 tools/authoring/author_talkhis_ch68.py
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

T = "jinas-tamm"; N = "jinas-naqis"
TITLE = {"ar": "الْمُحَسِّنَاتُ اللَّفْظِيَّةُ: الْجِنَاسُ — التَّامُّ، وَالْمُحَرَّفُ، وَالنَّاقِصُ", "en": "The lafzi muhassinat: jinas — the tamm, the muharraf, the naqis", "tr": "Lafzî muhassinât: cinâs — tam, muharref, nâkıs"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)
def wa_in(tag, full="وَإِنْ", punct=None):
    return tok(full, "in-shartiyya", "part", [tag, "in-shartiyya", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if» — the conditional in.", "«ve eğer» — şart edatı in.",
               segments=[seg("وَ", "wa", "conj"), seg(full[1:], "in-shartiyya", "part")], punct=punct)
def fi(tag): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».")
def summiya(tag):
    return tok("سُمِّيَ", "samma", "verb", [tag, "naib-al-fail", "mafulayn", "in-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (الْجِنَاسُ) — الْمَفْعُولُ الْأَوَّلُ.",
               "«it is called» — the passive; the jawab; its deputy (the jinas) concealed — the first of two objects.", "«adlanır» — meçhul; cevap; nâibi (cinas) gizli — iki mef'ulün ilki.")
def ikhtalafa_dual(tag):
    return tok("اخْتَلَفَا", "ikhtalafa", "verb", [tag, "in-shartiyya", "fail", "al-muthanna"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالْأَلِفُ فَاعِلٌ (اللَّفْظَانِ).",
               "«the two differ» — the shart verb; the alif is the doer (the two words).", "«ikisi ayrılırsa» — şart fiili; elif fâil (iki lafız).")
def al_huruf(tag): return tok("الْحُرُوفِ", "harf", "noun", [tag, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ تَكْسِيرٍ.", "«of the letters».", "«harflerin».")

# ----------- s1 — the definition (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "JINAS between two words is their RESEMBLANCE in utterance." + R_EN,
 "tr": "İki lafız arasında CİNÂS, telaffuzda birbirine BENZEMELERİDİR." + R_TR},
 "tokens": [
  tok("الْجِنَاسُ","jinas","noun",[T, "mubtada-khabar", "jinas"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«jinas» — the mubtada.", "«cinâs» — mübtedâ."),
  tok("بَيْنَ","bayna","noun",[T, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ — مُتَعَلِّقٌ بِالْجِنَاسِ.", "«between» — the zarf, annexed.", "«arasında» — zarf, muzâf."),
  tok("اللَّفْظَيْنِ","lafz","noun",[T, "al-muthanna", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«the two words» — a dual, annexed to.", "«iki lafzın» — tesniye, muzâfun ileyh."),
  tok("تَشَابُهُهُمَا","tashabuh","noun",[T, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their resemblance» — the khabar; the dual pronoun annexed.", "«birbirine benzemeleri» — haber; tesniye zamiri muzâfun ileyh.",
      segments=[seg("تَشَابُهُ","tashabuh","noun"), seg("هُمَا","pron-3d","pron")]),
  fi(T),
  tok("اللَّفْظِ","lafz","noun",[T, "huruf-jarr"], "مَجْرُورٌ — فِي اللَّفْظِ: فِي النُّطْقِ، لَا فِي الْمَعْنَى.", "«in the utterance» — in the sound, not the sense.", "«lafızda» — seste, mânâda değil."),
 ]})

# ----------- s2 — the tamm (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "The COMPLETE (tamm) of it is that the two agree in the KINDS of the letters, their NUMBER, their SHAPES and their ORDER." + R_EN,
 "tr": "Bunun TAMMI, ikisinin harflerin NEVİLERİNDE, SAYILARINDA, ŞEKİLLERİNDE ve TERTİBİNDE birleşmeleridir." + R_TR},
 "tokens": [
  tok("وَالتَّامُّ","tamm","noun",[T, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالتَّامُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the complete» — the mubtada.", "«ve tam olanı» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("التَّامُّ","tamm","noun")]),
  tok("مِنْهُ","min","part",[T, "huruf-jarr", "hal"], "جَارٌّ وَمَجْرُورٌ — حَالٌ مِنَ التَّامِّ (أَيِ التَّامُّ مِنَ الْجِنَاسِ).", "«of it» — of the jinas.", "«ondan» — cinastan.",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("أَنْ","an-masdariyya","part",[T, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the clause is the khabar.", "«-ması» — masdariyye en; cümle haber."),
  tok("يَتَّفِقَا","ittafaqa","verb",[T, "an-masdariyya", "fail", "al-muthanna", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِحَذْفِ النُّونِ — مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْأَلِفُ فَاعِلٌ.", "«the two agree» — mansub by the nun's fall; the alif is the doer.", "«ikisi birleşsin» — nûnun düşmesiyle mansûb; elif fâil."),
  fi(T),
  tok("أَنْوَاعِ","naw","noun",[T, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، مُضَافٌ — جَمْعُ نَوْعٍ.", "«the kinds of» — annexed.", "«nevilerinde» — muzâf."),
  al_huruf(T),
  tok("وَأَعْدَادِهَا","adad","noun",[T, "atf-nasaq", "idafa-definiteness", "jam-taksir"], "مَعْطُوفٌ عَلَى أَنْوَاعِ مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and their number» — joined.", "«ve sayılarında» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("أَعْدَادِ","adad","noun"), seg("هَا","pron-3fs","pron")]),
  tok("وَهَيْئَاتِهَا","haya-shape","noun",[T, "atf-nasaq", "idafa-definiteness", "jam-muannath-salim"], "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ.", "«and their shapes» — the vowels and the shadda.", "«ve şekillerinde» — hareke ve şedde.",
      segments=[seg("وَ","wa","conj"), seg("هَيْئَاتِ","haya-shape","noun"), seg("هَا","pron-3fs","pron")]),
  tok("وَتَرْتِيبِهَا","tartib","noun",[T, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and their order».", "«ve tertibinde».",
      segments=[seg("وَ","wa","conj"), seg("تَرْتِيبِ","tartib","noun"), seg("هَا","pron-3fs","pron")]),
 ]})

# ----------- s3 — the mumathil (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "If the two are of ONE kind — as two nouns — it is called MUMATHIL." + R_EN,
 "tr": "İkisi BİR nevidense — iki isim gibi — MÜMÂSİL denir." + R_TR},
 "tokens": [
  tok("فَإِنْ","in-shartiyya","part",[T, "in-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if» — the fa of detail; in.", "«eğer» — tefrî fâsı; in.",
      segments=[seg("فَ","fa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("كَانَا","kana","verb",[T, "kana-wa-akhawatuha", "in-shartiyya", "al-muthanna"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ، وَالْأَلِفُ اسْمُهُ (اللَّفْظَانِ).", "«the two are» — kana; the alif its ism.", "«ikisi olursa» — kâne; elif ismi."),
  tok("مِنْ","min","part",[T, "huruf-jarr", "kana-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«of» — the jarr phrase is kana's khabar.", "«-den» — câr-mecrûr kânenin haberi."),
  tok("نَوْعٍ","naw","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«a kind».", "«bir nevi»."),
  tok("وَاحِدٍ","wahid","noun",[T, "huruf-jarr"], "نَعْتٌ مَجْرُورٌ.", "«one» — the na't.", "«bir» — na't."),
  tok("كَاسْمَيْنِ","ism","noun",[T, "huruf-jarr", "al-muthanna"], "الْكَافُ لِلتَّمْثِيلِ، وَاسْمَيْنِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«as two nouns» — the kaf of «for instance»; a dual.", "«iki isim gibi» — temsil kâfı; tesniye.",
      segments=[seg("كَ","ka","part"), seg("اسْمَيْنِ","ism","noun")]),
  summiya(T),
  tok("مُمَاثِلًا","mumathil","noun",[T, "mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ مَاثَلَ.", "«mumathil» — the second object: «matching».", "«mümâsil» — ikinci mef'ul: «denk»."),
 ]})

# ----------- s4 — 30:55: the Hour and an hour
S.append({"id": "s4", "translation": {
 "en": "«And the DAY the HOUR rises, the criminals swear they tarried not an HOUR» (30:55).",
 "tr": "«KIYAMET SAATİ koptuğu GÜN, mücrimler bir SAATTEN fazla kalmadıklarına yemin ederler» (Rûm 55)."},
 "tokens": [
  tok("وَيَوْمَ","yawm","noun",[T, "maful-fih", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيَوْمَ ظَرْفُ زَمَانٍ مَنْصُوبٌ — مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ، مُتَعَلِّقٌ بِيُقْسِمُ.", "«and the day» — the zarf, annexed to the clause.", "«ve gün» — zarf, cümleye muzâf.",
      segments=[seg("وَ","wa","conj"), seg("يَوْمَ","yawm","noun")]),
  tok("تَقُومُ","qama","verb",[T, "hollow-verbs", "mudari-marfu", "idafa-definiteness"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«rises» — the clause is annexed to.", "«kopar» — cümle muzâfun ileyh."),
  tok("السَّاعَةُ","saa-hour","noun",[T, "fail"], "فَاعِلٌ مَرْفُوعٌ — السَّاعَةُ: الْقِيَامَةُ.", "«the Hour» — the doer: the Resurrection.", "«saat» — fâil: kıyamet."),
  tok("يُقْسِمُ","aqsama","verb",[T, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«swear».", "«yemin eder»."),
  tok("الْمُجْرِمُونَ","mujrim","noun",[T, "fail", "jam-mudhakkar-salim"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the criminals» — the doer, a sound plural.", "«mücrimler» — fâil, cem-i müzekker sâlim."),
  tok("مَا","ma-nafiya","part",[T, "anwa-ma"], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ.", "«not» — the clause answers the oath.", "«-madı» — cümle yeminin cevabı."),
  tok("لَبِثُوا","labitha","verb",[T, "fail"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«they tarried» — the waw is the doer.", "«kaldılar» — vâv fâil."),
  tok("غَيْرَ","ghayr","noun",[T, "maful-fih", "idafa-definiteness"], "نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ مَنْصُوبٌ، مُضَافٌ — أَيْ غَيْرَ سَاعَةٍ مِنَ الزَّمَانِ.", "«other than» — standing for the time-zarf, annexed.", "«-den başka» — zaman zarfı yerine, muzâf."),
  tok("سَاعَةٍ","saa-hour","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — سَاعَةٍ: جُزْءٌ مِنَ الزَّمَانِ.", "«an hour» — a span of time.", "«bir saat» — zamandan bir parça."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "tamm", "kind2": "mumathil", "pair": [ix(S[-1], "السَّاعَةُ"), ix(S[-1], "سَاعَةٍ")]}]

# ----------- s5 — the mustawfa (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "And if they are of TWO kinds, it is called MUSTAWFA." + R_EN,
 "tr": "İKİ nevidenseler, MÜSTEVFÂ denir." + R_TR},
 "tokens": [
  wa_in(T),
  tok("كَانَا","kana","verb",[T, "kana-wa-akhawatuha", "in-shartiyya", "al-muthanna"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ، وَالْأَلِفُ اسْمُهُ.", "«the two are» — kana; the alif its ism.", "«ikisi olursa» — kâne; elif ismi."),
  tok("مِنْ","min","part",[T, "huruf-jarr", "kana-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«of» — kana's khabar.", "«-den» — kânenin haberi."),
  tok("نَوْعَيْنِ","naw","noun",[T, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى: كَفِعْلٍ وَاسْمٍ.", "«two kinds» — a dual: a verb and a noun.", "«iki nevi» — tesniye: fiil ve isim gibi."),
  summiya(T),
  tok("مُسْتَوْفًى","mustawfa","noun",[T, "mafulayn", "ism-maqsur-manqus", "ism-maful"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — اسْمُ مَفْعُولٍ مَقْصُورٌ مِنَ اسْتَوْفَى.", "«mustawfa» — the second object: «brought in full»; a maqsur.", "«müstevfâ» — ikinci mef'ul: «tam alınmış»; maksûr."),
 ]})

# ----------- s6 — Abu Tammam: يَحْيَى the verb, يَحْيَى the man
S.append({"id": "s6", "translation": {
 "en": "«What has died of the generosity of the age — it LIVES (yahya) with YAHYA son of ʿAbdallah.» (Abu Tammam)",
 "tr": "«Zamanın kereminden ölen — YAHYÂ b. Abdullah'ın yanında DİRİLİR (yahyâ).» (Ebû Temmâm)"},
 "tokens": [
  tok("مَا","ma-mawsula","pron",[T, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«what» — the mawsul, the mubtada.", "«şey» — mevsûl, mübtedâ."),
  tok("مَاتَ","mata-die","verb",[T, "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«has died» — the sila; its doer concealed.", "«ölen» — sıla; fâili gizli."),
  tok("مِنْ","min","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("كَرَمِ","karam","noun",[T, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the generosity of».", "«kereminden»."),
  tok("الزَّمَانِ","zaman","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the age».", "«zamanın»."),
  tok("فَإِنَّهُ","inna","part",[T, "inna-wa-akhawatuha", "fa-khabar-mubtada"], "الْفَاءُ دَاخِلَةٌ فِي خَبَرِ الْمَوْصُولِ لِشَبَهِهِ بِالشَّرْطِ، وَإِنَّ حَرْفُ تَوْكِيدٍ نَاسِخٌ، وَالْهَاءُ اسْمُهَا.", "«— it» — the fa on the mawsul's khabar (shart-like); inna with its ism.", "«— o» — mevsûlün haberindeki fâ (şart benzeri); inne ve ismi.",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part"), seg("هُ","pron-3ms","pron")], punct="*"),
  tok("يَحْيَى","hayiya","verb",[T, "inna-wa-akhawatuha", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — نَاقِصٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«lives» — the mudari of حَيِيَ; the clause is inna's khabar.", "«yaşar» — حَيِيَ'nin muzârii; cümle innenin haberi."),
  tok("لَدَى","lada","noun",[T, "maful-fih", "idafa-definiteness", "ism-maqsur-manqus"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ — بِمَعْنَى عِنْدَ.", "«with, at» — the zarf «lada», annexed.", "«yanında» — zarf «ledâ», muzâf."),
  tok("يَحْيَى","yahya","noun",[T, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ الْمُقَدَّرَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ.", "«Yahya» — the name, annexed to; a diptote (a name on a verb's pattern).", "«Yahyâ» — özel ad, muzâfun ileyh; gayr-i munsarif."),
  tok("بْنِ","ibn","noun",[T, "idafa-definiteness"], "نَعْتٌ (أَوْ بَدَلٌ) مَجْرُورٌ، مُضَافٌ — تُحْذَفُ هَمْزَتُهُ بَيْنَ عَلَمَيْنِ.", "«son of» — the na't, annexed; its hamza dropped between two names.", "«oğlu» — na't, muzâf; iki ad arasında hemzesi düşer."),
  tok("عَبْدِ","abd","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«ʿAbd-» — annexed to, itself annexed.", "«Abd-» — muzâfun ileyh, muzâf."),
  tok("اللهِ","allah","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«-allah».", "«-ullah»."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "tamm", "kind2": "mustawfa", "pair": [ix(S[-1], "يَحْيَى", 1), ix(S[-1], "يَحْيَى", 2)]}]

# ----------- s7 — the murakkab and the mutashabih (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "And if ONE of the two words is COMPOSITE, it is called the jinas of TARKIB; then if they agree in SCRIPT it is singled out by the name MUTASHABIH." + R_EN,
 "tr": "İki lafızdan BİRİ MÜREKKEP ise, TERKİP cinâsı denir; YAZIDA birleşirlerse MÜTEŞÂBİH adıyla anılır." + R_TR},
 "tokens": [
  wa_in(T),
  tok("كَانَ","kana","verb",[T, "kana-wa-akhawatuha", "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ.", "«is» — kana, the shart verb.", "«olursa» — kâne, şart fiili."),
  tok("أَحَدُ","ahad","noun",[T, "kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ.", "«one of» — kana's ism, annexed.", "«biri» — kânenin ismi, muzâf."),
  tok("اللَّفْظَيْنِ","lafz","noun",[T, "al-muthanna", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two words».", "«iki lafzın»."),
  tok("مُرَكَّبًا","murakkab","noun",[T, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ كَانَ مَنْصُوبٌ — اسْمُ مَفْعُولٍ.", "«composite» — kana's khabar.", "«mürekkep» — kânenin haberi."),
  summiya(T),
  tok("جِنَاسَ","jinas","noun",[T, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the jinas of» — the second object, annexed.", "«cinâsı» — ikinci mef'ul, muzâf."),
  tok("التَّرْكِيبِ","tarkib","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«composition».", "«terkip».", punct="،"),
  tok("فَإِنِ","in-shartiyya","part",[T, "in-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ — كُسِرَتْ نُونُهَا لِالْتِقَاءِ السَّاكِنَيْنِ.", "«then if» — in, its nun given a kasra before the wasl.", "«sonra eğer» — in; nûnu iki sâkin buluşunca kesreli.",
      segments=[seg("فَ","fa","conj"), seg("إِنِ","in-shartiyya","part")]),
  tok("اتَّفَقَا","ittafaqa","verb",[T, "in-shartiyya", "fail", "al-muthanna"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالْأَلِفُ فَاعِلٌ.", "«the two agree» — the shart verb; the alif is the doer.", "«ikisi birleşirse» — şart fiili; elif fâil."),
  fi(T),
  tok("الْخَطِّ","khatt","noun",[T, "huruf-jarr"], "مَجْرُورٌ — الْخَطُّ: الْكِتَابَةُ.", "«the script» — the writing.", "«hat» — yazı."),
  tok("خُصَّ","khassa-verb","verb",[T, "naib-al-fail", "doubled-verbs", "in-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — مُضَاعَفٌ، جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it is singled out» — the passive of a doubled verb; the jawab.", "«tahsis edilir» — muzâaf fiilin meçhulü; cevap."),
  tok("بِاسْمِ","ism","noun",[T, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمِ مَجْرُورٌ مُضَافٌ.", "«by the name of».", "«adıyla».",
      segments=[seg("بِ","bi","prep"), seg("اسْمِ","ism","noun")]),
  tok("الْمُتَشَابِهِ","mutashabih-jinas","noun",[T, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ تَشَابَهَ.", "«the mutashabih» — «the resembling»: alike in script too.", "«müteşâbih» — «benzeşen»: yazıda da bir."),
 ]})

# ----------- s8 — al-Busti: ذَا هِبَةٍ / ذَاهِبَةٌ
S.append({"id": "s8", "translation": {
 "en": "«When a king is not a POSSESSOR OF GIFTS (dha hiba), leave him — for his dominion is DEPARTING (dhahiba).» (Abu l-Fath al-Busti)",
 "tr": "«Bir hükümdar İHSAN SAHİBİ (zâ hibe) değilse onu bırak — devleti GİDİCİDİR (zâhibe).» (Ebü'l-Feth el-Büstî)"},
 "tokens": [
  tok("إِذَا","idha","part",[T, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the zarf of the future that carries a condition.", "«-ince» — şart mânâlı zaman zarfı."),
  tok("مَلِكٌ","malik-king","noun",[T, "fail", "idha-shartiyya"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ (إِذَا كَانَ مَلِكٌ) — وَقِيلَ مُبْتَدَأٌ.", "«a king» — the doer of a verb the next explains (or a mubtada).", "«bir hükümdar» — sonrakinin açıkladığı fiilin fâili (yahut mübtedâ)."),
  tok("لَمْ","lam-jazima","part",[T, "in-shartiyya"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — jazm on the mudari.", "«-medi» — cezm eder."),
  tok("يَكُنْ","kana","verb",[T, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — حُذِفَتْ وَاوُهُ لِلسَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«is» — kana majzum, its waw dropped; ism concealed.", "«değilse» — meczûm kâne, vâvı düşmüş; ismi gizli."),
  tok("ذَا","dhu","noun",[T, "kana-wa-akhawatuha", "five-nouns", "idafa-definiteness"], "خَبَرُ يَكُنْ مَنْصُوبٌ بِالْأَلِفِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«possessor of» — kana's khabar, one of the five nouns.", "«sahibi» — kânenin haberi, beş isimden."),
  tok("هِبَةٍ","hiba","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«gift» — annexed to.", "«hibe» — muzâfun ileyh.", punct="*"),
  tok("فَدَعْهُ","da-leave","verb",[T, "idha-shartiyya", "maful-bihi", "jawab-al-talab"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَدَعْ فِعْلُ أَمْرٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«then leave him» — the fa of the jawab; the command; its object.", "«onu bırak» — cevap fâsı; emir; mef'ulü.",
      segments=[seg("فَ","fa","conj"), seg("دَعْ","da-leave","verb"), seg("هُ","pron-3ms","pron")]),
  tok("فَدَوْلَتُهُ","dawla","noun",[T, "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ لِلتَّعْلِيلِ، وَدَوْلَتُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«for his dominion» — the fa of the reason; the mubtada.", "«çünkü devleti» — talil fâsı; mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("دَوْلَتُ","dawla","noun"), seg("هُ","pron-3ms","pron")]),
  tok("ذَاهِبَةٌ","dhahib","noun",[T, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مُؤَنَّثٌ.", "«departing» — the khabar; the feminine participle.", "«gidici» — haber; müennes ism-i fâil."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "murakkab", "kind2": "mutashabih", "first": [ix(S[-1], "ذَا"), ix(S[-1], "هِبَةٍ")], "second": [ix(S[-1], "ذَاهِبَةٌ")]}]

# ----------- s9 — the mafruq (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "Otherwise it is singled out by the name MAFRUQ." + R_EN,
 "tr": "Aksi hâlde MEFRÛK adıyla anılır." + R_TR},
 "tokens": [
  tok("وَإِلَّا","illa","part",[T, "in-shartiyya", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ الشَّرْطِيَّةُ وَلَا النَّافِيَةُ — أَيْ وَإِنْ لَمْ يَتَّفِقَا فِي الْخَطِّ.", "«otherwise» — in + la: if they do not agree in script.", "«yoksa» — in + lâ: yazıda birleşmezlerse.",
      segments=[seg("وَ","wa","conj"), seg("إِلَّا","illa","part")]),
  tok("خُصَّ","khassa-verb","verb",[T, "naib-al-fail", "doubled-verbs", "in-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it is singled out» — the passive; the jawab.", "«tahsis edilir» — meçhul; cevap."),
  tok("بِاسْمِ","ism","noun",[T, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمِ مَجْرُورٌ مُضَافٌ.", "«by the name of».", "«adıyla».",
      segments=[seg("بِ","bi","prep"), seg("اسْمِ","ism","noun")]),
  tok("الْمَفْرُوقِ","mafruq","noun",[T, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ: الْمُفْتَرِقُ فِي الْخَطِّ.", "«the mafruq» — «parted»: apart in the script.", "«mefrûk» — «ayrılmış»: yazıda ayrı."),
 ]})

# ----------- s10 — al-Busti: جَامَ لَنَا / جَامَلَنَا
S.append({"id": "s10", "translation": {
 "en": "«Each of you has taken the cup, and NO CUP FOR US (la jama lana): what harm to the passer of the cup, had he TREATED US KINDLY (jamalana)?» (al-Busti)",
 "tr": "«Hepiniz kadehi aldınız, BİZE KADEH YOK (lâ câme lenâ): kadehi dolaştıran, BİZE LÜTFETSEYDİ (câmelenâ) ne zarar görürdü?» (Büstî)"},
 "tokens": [
  tok("كُلُّكُمْ","kull","noun",[T, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«each of you» — the mubtada.", "«hepiniz» — mübtedâ.",
      segments=[seg("كُلُّ","kull","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("قَدْ","qad","part",[T], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«gerçekten»."),
  tok("أَخَذَ","akhadha","verb",[T, "mubtada-khabar", "fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«has taken» — the clause is the khabar.", "«aldı» — cümle haber."),
  tok("الْجَامَ","jam-cup","noun",[T, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْجَامُ: الْكَأْسُ.", "«the cup» — the object.", "«kadehi» — mef'ul."),
  tok("وَلَا","la-nafiya-lil-jins","part",[T, "la-nafiya-lil-jins", "hal"], "الْوَاوُ لِلْحَالِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«while no» — the waw of the hal; la of genus-denial.", "«hâlbuki hiç» — hâl vâvı; cins nefyeden lâ.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya-lil-jins","part")]),
  tok("جَامَ","jam-cup","noun",[T, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«cup» — la's ism, built on the fatha.", "«kadeh» — lânın ismi, fetha üzere mebnî."),
  tok("لَنَا","li","part",[T, "la-nafiya-lil-jins", "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — خَبَرُ لَا.", "«for us» — la's khabar.", "«bize» — lânın haberi.",
      segments=[seg("لَ","li","prep"), seg("نَا","pron-1p","pron")], punct="*"),
  tok("مَا","ma-istifham","pron",[T, "al-istifham", "mubtada-khabar", "anwa-ma"], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ.", "«what» — the question-ma, the mubtada.", "«ne» — istifham mâsı, mübtedâ."),
  tok("الَّذِي","alladhi","pron",[T, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«is it that» — the mawsul, the khabar.", "«-dır ki» — mevsûl, haber."),
  tok("ضَرَّ","darra","verb",[T, "ism-mawsul", "doubled-verbs"], "فِعْلٌ مَاضٍ مُضَاعَفٌ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«harmed» — the sila; the doer concealed.", "«zarar verdi» — sıla; fâili gizli."),
  tok("مُدِيرَ","mudir","noun",[T, "maful-bihi", "idafa-definiteness", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — اسْمُ فَاعِلٍ مِنْ أَدَارَ.", "«the passer of» — the object, annexed: who sends the cup round.", "«dolaştıranı» — mef'ul, muzâf: kadehi dolaştıran."),
  tok("الْجَامِ","jam-cup","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the cup».", "«kadehi»."),
  tok("لَوْ","law","part",[T], "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ — وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«had» — law; its jawab is what went before.", "«-seydi» — lev; cevabı öncekidir."),
  tok("جَامَلَنَا","jamala","verb",[T, "maful-bihi", "fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا مَفْعُولٌ بِهِ — جَامَلَ: عَامَلَ بِالْجَمِيلِ.", "«he treated us kindly» — with «us» its object.", "«bize lütfetseydi» — «biz» mef'ulü.",
      segments=[seg("جَامَلَ","jamala","verb"), seg("نَا","pron-1p","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "murakkab", "kind2": "mafruq", "first": [ix(S[-1], "جَامَ"), ix(S[-1], "لَنَا")], "second": [ix(S[-1], "جَامَلَنَا")]}]

# ----------- s11 — the muharraf (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "And if the two differ ONLY in the SHAPES of the letters, it is called MUHARRAF." + R_EN,
 "tr": "İkisi YALNIZ harflerin ŞEKİLLERİNDE ayrılırlarsa, MUHARREF denir." + R_TR},
 "tokens": [
  wa_in(T, "وَإِنِ"),
  ikhtalafa_dual(T),
  fi(T),
  tok("هَيْئَاتِ","haya-shape","noun",[T, "huruf-jarr", "idafa-definiteness", "jam-muannath-salim"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the shapes of» — the vowels.", "«şekillerinde» — harekeler."),
  al_huruf(T),
  tok("فَقَطْ","faqat","part",[T], "الْفَاءُ زَائِدَةٌ لِتَزْيِينِ اللَّفْظِ، وَقَطْ بِمَعْنَى حَسْبُ.", "«only» — «and enough».", "«yalnız» — «bu kadar»."),
  summiya(T),
  tok("مُحَرَّفًا","muharraf","noun",[T, "mafulayn", "ism-maful"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ حَرَّفَ.", "«muharraf» — «altered»: the vowels turned.", "«muharref» — «değiştirilmiş»: harekeleri çevrilmiş."),
 ]})

# ----------- s12 — the wool cloak
S.append({"id": "s12", "translation": {
 "en": "«The jubba of the CLOAK (burd) is a shield against the COLD (bard).»",
 "tr": "«HIRKANIN (bürd) cübbesi SOĞUĞA (berd) kalkandır.»"},
 "tokens": [
  tok("جُبَّةُ","jubba","noun",[T, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the jubba of» — the mubtada, annexed.", "«cübbesi» — mübtedâ, muzâf."),
  tok("الْبُرْدِ","burd","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْبُرْدُ: كِسَاءٌ مُخَطَّطٌ.", "«the striped cloak».", "«çizgili hırka»."),
  tok("جُنَّةُ","junna","noun",[T, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — الْجُنَّةُ: مَا يُسْتَتَرُ بِهِ، التُّرْسُ.", "«a shield against» — the khabar: what one hides behind.", "«kalkanı» — haber: siper."),
  tok("الْبَرْدِ","bard","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the cold».", "«soğuğun»."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "muharraf", "pair": [ix(S[-1], "الْبُرْدِ"), ix(S[-1], "الْبَرْدِ")]}]

# ----------- s13 — the ignorant overdoes or falls short
S.append({"id": "s13", "translation": {
 "en": "«The ignorant either OVERSHOOTS (mufrit) or FALLS SHORT (mufarrit).» — the doubled letter counts as undoubled.",
 "tr": "«Câhil ya AŞIRI GİDER (müfrit) ya da GERİ KALIR (müferrit).» — şeddeli harf şeddesiz hükmündedir."},
 "tokens": [
  tok("الْجَاهِلُ","jahil","noun",[T, "mubtada-khabar", "ism-fail"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the ignorant» — the mubtada.", "«câhil» — mübtedâ."),
  tok("إِمَّا","imma","part",[T, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("مُفْرِطٌ","mufrit","noun",[T, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ أَفْرَطَ: جَاوَزَ الْحَدَّ.", "«overshooting» — the khabar: who passes the bound.", "«aşırı giden» — haber: haddi aşan."),
  tok("أَوْ","aw","conj",[T, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  tok("مُفَرِّطٌ","mufarrit","noun",[T, "atf-nasaq", "ism-fail"], "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ فَرَّطَ: قَصَّرَ.", "«falling short» — joined: who neglects.", "«geri kalan» — atıf: ihmal eden."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "muharraf", "pair": [ix(S[-1], "مُفْرِطٌ"), ix(S[-1], "مُفَرِّطٌ")]}]

# ----------- s14 — the snare of shirk
S.append({"id": "s14", "translation": {
 "en": "«Innovation is the SNARE (sharak) of SHIRK.»",
 "tr": "«Bid'at ŞİRKİN TUZAĞIDIR (şerek).»"},
 "tokens": [
  tok("الْبِدْعَةُ","bida","noun",[T, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«innovation» — the mubtada.", "«bid'at» — mübtedâ."),
  tok("شَرَكُ","sharak","noun",[T, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — الشَّرَكُ: حِبَالَةُ الصَّائِدِ.", "«the snare of» — the khabar: the hunter's net.", "«tuzağı» — haber: avcının ağı."),
  tok("الشِّرْكِ","shirk","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«shirk».", "«şirkin»."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "muharraf", "pair": [ix(S[-1], "شَرَكُ"), ix(S[-1], "الشِّرْكِ")]}]

# ----------- s15 — the naqis and its three places (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "And if they differ in the NUMBER of the letters, it is called NAQIS; that is either at the BEGINNING, or in the MIDDLE, or at the END." + R_EN,
 "tr": "Harflerin SAYISINDA ayrılırlarsa NÂKIS denir; bu ya BAŞTA, ya ORTADA, ya SONDA olur." + R_TR},
 "tokens": [
  wa_in(N, "وَإِنِ"),
  ikhtalafa_dual(N),
  fi(N),
  tok("أَعْدَادِ","adad","noun",[N, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، مُضَافٌ — جَمْعُ عَدَدٍ.", "«the number of».", "«sayılarında»."),
  al_huruf(N),
  summiya(N),
  tok("نَاقِصًا","naqis","noun",[N, "mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«naqis» — «lacking»: one word has a letter the other has not.", "«nâkıs» — «eksik»: birinde öbüründe olmayan bir harf var.", punct="،"),
  tok("وَذَلِكَ","dhalika","pron",[N, "asma-al-ishara", "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَلِكَ مُبْتَدَأٌ.", "«and that» — the mubtada.", "«ve bu» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("ذَلِكَ","dhalika","pron")]),
  tok("إِمَّا","imma","part",[N, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("فِي","fi","prep",[N, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«at» — the jarr phrase is the khabar.", "«-de» — câr-mecrûr haber."),
  tok("الْأَوَّلِ","awwal","noun",[N, "huruf-jarr"], "مَجْرُورٌ.", "«the beginning».", "«başta»."),
  tok("أَوْ","aw","conj",[N, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  fi(N),
  tok("الْوَسَطِ","wasat","noun",[N, "huruf-jarr"], "مَجْرُورٌ.", "«the middle».", "«ortada»."),
  tok("أَوْ","aw","conj",[N, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  fi(N),
  tok("الْآخِرِ","akhir","noun",[N, "huruf-jarr"], "مَجْرُورٌ.", "«the end».", "«sonda»."),
 ]})

# ----------- s16 — 75:29-30: the shank and the driving
S.append({"id": "s16", "translation": {
 "en": "«And the SHANK (saq) is wound about the shank — to your Lord that day is the DRIVING (masaq)» (75:29-30).",
 "tr": "«BALDIR (sâk) baldıra dolanır — o gün SEVK (mesâk) Rabbinedir» (Kıyâme 29-30)."},
 "tokens": [
  tok("وَالْتَفَّتِ","iltaffa","verb",[N, "doubled-verbs", "fail"], "الْوَاوُ عَاطِفَةٌ، وَالْتَفَّتِ فِعْلٌ مَاضٍ مُضَاعَفٌ مِنَ الِافْتِعَالِ، وَالتَّاءُ لِلتَّأْنِيثِ — كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and is wound» — Form VIII of a doubled root; the feminine ta with the wasl kasra.", "«ve dolanır» — muzâaf kökün iftiâli; müennes tâsı vasıl kesresiyle.",
      segments=[seg("وَ","wa","conj"), seg("الْتَفَّتِ","iltaffa","verb")]),
  tok("السَّاقُ","saq","noun",[N, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the shank» — the doer.", "«baldır» — fâil."),
  tok("بِالسَّاقِ","saq","noun",[N, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالسَّاقِ مَجْرُورٌ.", "«about the shank».", "«baldıra».",
      segments=[seg("بِ","bi","prep"), seg("السَّاقِ","saq","noun")]),
  tok("إِلَى","ila","prep",[N, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«to» — the fronted khabar.", "«-e» — öne alınmış haber."),
  tok("رَبِّكَ","rabb","noun",[N, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord».", "«Rabbine».",
      segments=[seg("رَبِّ","rabb","noun"), seg("كَ","pron-2ms","pron")]),
  tok("يَوْمَئِذٍ","yawmaidhin","noun",[N, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى إِذْ — وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ.", "«that day» — the zarf annexed to idh; the tanwin stands for a clause.", "«o gün» — iz'e muzâf zarf; tenvin cümle yerine."),
  tok("الْمَسَاقُ","masaq","noun",[N, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرٌ مِيمِيٌّ.", "«the driving» — the delayed mubtada; a mimi masdar.", "«sevk» — sona bırakılmış mübtedâ; mîmî masdar."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "naqis", "kind2": "awwal", "pair": [ix(S[-1], "السَّاقُ"), ix(S[-1], "الْمَسَاقُ")]}]

# ----------- s17 — my fortune is my toil
S.append({"id": "s17", "translation": {
 "en": "«My FORTUNE (jaddi) is my TOIL (jahdi).»",
 "tr": "«BAHTIM (ceddî) ÇABAMDIR (cehdî).»"},
 "tokens": [
  tok("جَدِّي","jadd","noun",[N, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — وَيَاءُ الْمُتَكَلِّمِ مُضَافٌ إِلَيْهِ؛ الْجَدُّ: الْحَظُّ.", "«my fortune» — the mubtada; jadd: luck, wealth.", "«bahtım» — mübtedâ; cedd: talih.",
      segments=[seg("جَدِّ","jadd","noun"), seg("ي","pron-1s","pron")]),
  tok("جَهْدِي","juhd","noun",[N, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — الْجَهْدُ: الطَّاقَةُ وَالْمَشَقَّةُ.", "«my toil» — the khabar.", "«çabam» — haber.",
      segments=[seg("جَهْدِ","juhd","noun"), seg("ي","pron-1s","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "naqis", "kind2": "wasat", "pair": [ix(S[-1], "جَدِّي"), ix(S[-1], "جَهْدِي")]}]

# ----------- s18 — Abu Tammam: hands that rebel and protect (mutarraf)
S.append({"id": "s18", "translation": {
 "en": "«They stretch out from hands that REBEL (ʿawasin) and PROTECT (ʿawasim)» (Abu Tammam) — an extra letter at the END: the mutarraf.",
 "tr": "«İSYAN EDEN (avâsın) ve KORUYAN (avâsım) ellerden uzatırlar» (Ebû Temmâm) — SONDA fazla harf: mutarraf."},
 "tokens": [
  tok("يَمُدُّونَ","madda","verb",[N, "doubled-verbs", "fail", "mudari-marfu", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ — مُضَاعَفٌ، وَالْوَاوُ فَاعِلٌ.", "«they stretch out» — a doubled verb; the waw is the doer.", "«uzatırlar» — muzâaf; vâv fâil."),
  tok("مِنْ","min","part",[N, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("أَيْدٍ","yad","noun",[N, "huruf-jarr", "ism-maqsur-manqus", "jam-taksir"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ، جَمْعُ قِلَّةٍ لِيَدٍ.", "«hands» — a manqus, the plural of few.", "«eller» — manqûs, kıllet cemi."),
  tok("عَوَاصٍ","awasin","noun",[N, "huruf-jarr", "ism-maqsur-manqus", "jam-taksir"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ، جَمْعُ عَاصِيَةٍ.", "«rebelling» — the na't; a manqus plural of ʿasiya.", "«isyan eden» — na't; âsiye'nin manqûs cemi."),
  tok("عَوَاصِمِ","awasim","noun",[N, "huruf-jarr", "mamnu-min-sarf", "jam-taksir"], "نَعْتٌ ثَانٍ مَجْرُورٌ — مَمْنُوعٌ مِنَ الصَّرْفِ (صِيغَةُ مُنْتَهَى الْجُمُوعِ)، وَكُسِرَ لِلرَّوِيِّ؛ جَمْعُ عَاصِمَةٍ.", "«protecting» — the second na't; a diptote plural given the rhyme's kasra.", "«koruyan» — ikinci na't; gayr-i munsarif cemi, revî kesresiyle."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "naqis", "kind2": "akhir", "pair": [ix(S[-1], "عَوَاصٍ"), ix(S[-1], "عَوَاصِمِ")]}]

# ----------- s19 — the mudhayyal (RESTORED)
S.append({"id": "s19", "translation": {
 "en": "And if the addition is by MORE than one letter, it is called MUDHAYYAL." + R_EN,
 "tr": "Ziyade bir harften FAZLA ise, MÜZEYYEL denir." + R_TR},
 "tokens": [
  wa_in(N),
  tok("كَانَتِ","kana","verb",[N, "kana-wa-akhawatuha", "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ، وَالتَّاءُ لِلتَّأْنِيثِ كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«is» — kana; the feminine ta with the wasl kasra.", "«olursa» — kâne; müennes tâsı vasıl kesresiyle."),
  tok("الزِّيَادَةُ","ziyada","noun",[N, "kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the addition» — kana's ism.", "«ziyade» — kânenin ismi."),
  tok("بِأَكْثَرَ","akthar","noun",[N, "huruf-jarr", "kana-wa-akhawatuha", "mamnu-min-sarf", "ism-tafdil"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَكْثَرَ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«by more» — the diptote afʿal; kana's khabar.", "«daha fazla ile» — gayr-i munsarif; kânenin haberi.",
      segments=[seg("بِ","bi","prep"), seg("أَكْثَرَ","akthar","noun")]),
  tok("مِنْ","min","part",[N, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  tok("حَرْفٍ","harf","noun",[N, "huruf-jarr"], "مَجْرُورٌ.", "«one letter».", "«bir harf»."),
  summiya(N),
  tok("مُذَيَّلًا","mudhayyal","noun",[N, "mafulayn", "ism-maful"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ ذَيَّلَ: جُعِلَ لَهُ ذَيْلٌ.", "«mudhayyal» — «given a tail».", "«müzeyyel» — «kuyruk verilmiş»."),
 ]})

# ----------- s20 — al-Khansa: the grief between the ribs (mudhayyal)
S.append({"id": "s20", "translation": {
 "en": "«Weeping is the cure for the BURNING GRIEF (jawa) between the RIBS (jawanih)» (al-Khansa).",
 "tr": "«Ağlamak, KABURGALAR (cevânih) arasındaki YANGININ (cevâ) şifasıdır» (Hansâ)."},
 "tokens": [
  tok("إِنَّ","inna","part",[N, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ نَاسِخٌ.", "«truly».", "«muhakkak»."),
  tok("الْبُكَاءَ","buka","noun",[N, "inna-wa-akhawatuha", "ism-mamdud"], "اسْمُ إِنَّ مَنْصُوبٌ — مَمْدُودٌ.", "«weeping» — inna's ism, a mamdud.", "«ağlamak» — innenin ismi, memdûd."),
  tok("هُوَ","huwa","pron",[N, "damir-fasl"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ.", "«it is» — the pronoun of separation.", "«işte o» — fasıl zamiri."),
  tok("الشِّفَاءُ","shifa","noun",[N, "inna-wa-akhawatuha", "ism-mamdud"], "خَبَرُ إِنَّ مَرْفُوعٌ — مَمْدُودٌ.", "«the cure» — inna's khabar.", "«şifa» — innenin haberi."),
  tok("مِنَ","min","part",[N, "huruf-jarr"], "حَرْفُ جَرٍّ — فُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its nun opened before the article.", "«-den» — nûnu iki sâkin buluşunca fethalı."),
  tok("الْجَوَى","jawa","noun",[N, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ؛ الْجَوَى: حُرْقَةُ الْحُزْنِ.", "«the burning grief» — a maqsur.", "«yangın» — maksûr; gizli dert."),
  tok("بَيْنَ","bayna","noun",[N, "maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between» — the zarf, annexed.", "«arasında» — zarf, muzâf."),
  tok("الْجَوَانِحِ","janiha","noun",[N, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ جَانِحَةٍ: الضُّلُوعُ تَحْتَ التَّرَائِبِ.", "«the ribs» — the plural of janiha.", "«kaburgalar» — câniha'nın cemi."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "naqis", "kind2": "mudhayyal", "pair": [ix(S[-1], "الْجَوَى"), ix(S[-1], "الْجَوَانِحِ")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "jinas": need("jinas", "جِنَاس", "ج ن س", "noun", "jinas — paronomasia: two words alike in sound (masdar of جَانَسَ)", "cinâs — seste birbirine benzeyen iki lafız (جَانَسَ'nin masdarı)", 5),
 "tamm": need("tamm", "تَامّ", "ت م م", "noun", "complete, full (the ism fa'il of تَمَّ)", "tam, eksiksiz (تَمَّ'nin ism-i fâili)", 3),
 "ittafaqa": need("ittafaqa", "اِتَّفَقَ", "و ف ق", "verb", "to agree, to coincide (Form VIII; اِتَّفَقَ يَتَّفِقُ)", "uyuşmak, birleşmek (VIII. bâb; اِتَّفَقَ يَتَّفِقُ)", 4, form="VIII"),
 "adad": need("adad", "عَدَد", "ع د د", "noun", "number, count", "sayı, adet", 2, plural="أَعْدَاد"),
 "wahid": need("wahid", "وَاحِد", "و ح د", "noun", "one, single", "bir, tek", 1),
 "mumathil": need("mumathil", "مُمَاثِل", "م ث ل", "noun", "matching, of the same kind (ism fa'il of مَاثَلَ); the jinas of two words of one class", "mümâsil, aynı cinsten (مَاثَلَ'nin ism-i fâili); aynı sınıftan iki lafzın cinâsı", 5),
 "saa-hour": need("saa-hour", "سَاعَة", "س و ع", "noun", "an hour, a span of time; the Hour (the Resurrection)", "saat, bir zaman parçası; Kıyamet saati", 2, plural="سَاعَات"),
 "mujrim": need("mujrim", "مُجْرِم", "ج ر م", "noun", "criminal, sinner (ism fa'il of أَجْرَمَ)", "mücrim, günahkâr (أَجْرَمَ'nin ism-i fâili)", 3, plural="مُجْرِمُونَ"),
 "labitha": need("labitha", "لَبِثَ", "ل ب ث", "verb", "to tarry, to remain (لَبِثَ يَلْبَثُ)", "kalmak, eğlenmek (لَبِثَ يَلْبَثُ)", 3),
 "mustawfa": need("mustawfa", "مُسْتَوْفًى", "و ف ي", "noun", "taken in full (ism maf'ul of اِسْتَوْفَى); the jinas of a verb and a noun", "tam alınmış (اِسْتَوْفَى'nın ism-i mef'ûlü); fiil ile ismin cinâsı", 5),
 "zaman": need("zaman", "زَمَان", "ز م ن", "noun", "time, the age", "zaman, devir", 2),
 "hayiya": need("hayiya", "حَيِيَ", "ح ي ي", "verb", "to live (حَيِيَ يَحْيَى — written with the alif maqsura; the naqis of bab samiʿa)", "yaşamak (حَيِيَ يَحْيَى — elif-i maksûre ile yazılır; semia bâbından nâkıs)", 3),
 "lada": need("lada", "لَدَى", "ل د ي", "noun", "with, at, in the presence of (a zarf like عِنْدَ; لَدَيْهِ before a pronoun)", "yanında, nezdinde (عِنْدَ gibi bir zarf; zamirden önce لَدَيْهِ)", 4),
 "yahya": need("yahya", "يَحْيَى", None, "propn", "Yahya (a name; a diptote on the verb's pattern) — Yahya b. ʿAbdallah, the praised of Abu Tammam", "Yahyâ (özel ad; fiil vezninde gayr-i munsarif) — Ebû Temmâm'ın memdûhu Yahyâ b. Abdullah", 5),
 "tarkib": need("tarkib", "تَرْكِيب", "ر ك ب", "noun", "composition, compounding (masdar of رَكَّبَ)", "terkip, birleştirme (رَكَّبَ'nin masdarı)", 4),
 "khatt": need("khatt", "خَطّ", "خ ط ط", "noun", "script, writing; a line", "hat, yazı; çizgi", 3),
 "khassa-verb": need("khassa-verb", "خَصَّ", "خ ص ص", "verb", "to single out, to set apart (a doubled verb: خَصَّ يَخُصُّ; خُصَّ بِـ: it is reserved for)", "tahsis etmek, ayırmak (muzâaf: خَصَّ يَخُصُّ; خُصَّ بِـ: ona tahsis edilir)", 4),
 "mutashabih-jinas": need("mutashabih-jinas", "مُتَشَابِه", "ش ب ه", "noun", "resembling — the murakkab jinas whose two words are one in script", "müteşâbih — iki lafzı yazıda bir olan mürekkep cinas", 5),
 "hiba": need("hiba", "هِبَة", "و ه ب", "noun", "a gift, a grant", "hibe, bağış", 3),
 "dawla": need("dawla", "دَوْلَة", "د و ل", "noun", "dominion, fortune that turns; a state", "devlet, dönen talih", 3),
 "dhahib": need("dhahib", "ذَاهِب", "ذ ه ب", "noun", "departing, going away (ism fa'il of ذَهَبَ)", "giden, gidici (ذَهَبَ'nin ism-i fâili)", 2),
 "jam-cup": need("jam-cup", "جَام", "ج و م", "noun", "a cup, a goblet", "kadeh, cam", 4),
 "mudir": need("mudir", "مُدِير", "د و ر", "noun", "one who sends round, who passes (the cup) — ism fa'il of أَدَارَ", "dolaştıran, (kadehi) döndüren — أَدَارَ'nin ism-i fâili", 4),
 "jamala": need("jamala", "جَامَلَ", "ج م ل", "verb", "to treat kindly, to be courteous to (Form III)", "lütufla davranmak, iyi geçinmek (III. bâb)", 4, form="III"),
 "ikhtalafa": need("ikhtalafa", "اِخْتَلَفَ", "خ ل ف", "verb", "to differ, to disagree (Form VIII; اِخْتَلَفَ يَخْتَلِفُ)", "ayrılmak, farklı olmak (VIII. bâb; اِخْتَلَفَ يَخْتَلِفُ)", 3, form="VIII"),
 "faqat": need("faqat", "فَقَطْ", "ق ط ط", "part", "only, and no more (the fa of embellishment + قَطْ «enough»)", "yalnız, ancak (süs fâsı + قَطْ «yeter»)", 2),
 "muharraf": need("muharraf", "مُحَرَّف", "ح ر ف", "noun", "altered, turned (ism maf'ul of حَرَّفَ); the jinas whose words differ in vowels only", "muharref, çevrilmiş (حَرَّفَ'nin ism-i mef'ûlü); lafızları yalnız harekede ayrılan cinas", 5),
 "junna": need("junna", "جُنَّة", "ج ن ن", "noun", "a shield, a screen — what one hides behind", "kalkan, siper — arkasına gizlenilen", 4),
 "bard": need("bard", "بَرْد", "ب ر د", "noun", "cold, coldness", "soğuk", 2),
 "mufrit": need("mufrit", "مُفْرِط", "ف ر ط", "noun", "one who overshoots the bound (ism fa'il of أَفْرَطَ)", "haddi aşan, ifrata giden (أَفْرَطَ'nin ism-i fâili)", 4),
 "mufarrit": need("mufarrit", "مُفَرِّط", "ف ر ط", "noun", "one who falls short, who neglects (ism fa'il of فَرَّطَ)", "geri kalan, ihmal eden (فَرَّطَ'nin ism-i fâili)", 4),
 "sharak": need("sharak", "شَرَك", "ش ر ك", "noun", "a snare, a hunter's net", "tuzak, avcı ağı", 4),
 "wasat": need("wasat", "وَسَط", "و س ط", "noun", "the middle", "orta", 2),
 "iltaffa": need("iltaffa", "اِلْتَفَّ", "ل ف ف", "verb", "to be wound about, to twist together (Form VIII of a doubled root)", "dolanmak, birbirine sarılmak (muzâaf kökün VIII. bâbı)", 4, form="VIII"),
 "saq": need("saq", "سَاق", "س و ق", "noun", "the shank, the leg; (75:29) the shank wound about the shank — the death agony", "baldır, bacak; (Kıyâme 29) baldırın baldıra dolanması — ölüm sıkıntısı", 3, plural="سُوق"),
 "yawmaidhin": need("yawmaidhin", "يَوْمَئِذٍ", "ي و م", "noun", "on that day (يَوْمَ annexed to إِذْ; the tanwin stands for a clause)", "o gün (إِذْ'e muzâf يَوْمَ; tenvin cümle yerine)", 3),
 "jadd": need("jadd", "جَدّ", "ج د د", "noun", "fortune, luck; wealth (also: a grandfather)", "baht, talih; zenginlik (ayrıca: dede)", 3),
 "juhd": need("juhd", "جَهْد", "ج ه د", "noun", "toil, effort, exertion", "çaba, gayret, meşakkat", 3),
 "madda": need("madda", "مَدَّ", "م د د", "verb", "to stretch out, to extend (a doubled verb: مَدَّ يَمُدُّ)", "uzatmak, germek (muzâaf: مَدَّ يَمُدُّ)", 3),
 "awasin": need("awasin", "عَوَاصٍ", "ع ص ي", "noun", "rebelling, disobedient (the plural of the ism fa'il عَاصِيَة; a manqus)", "isyan eden, âsi (عَاصِيَة'nin cemi; manqûs)", 5),
 "awasim": need("awasim", "عَوَاصِم", "ع ص م", "noun", "protecting, guarding (the plural of the ism fa'il عَاصِمَة; a diptote)", "koruyan (عَاصِمَة'nin cemi; gayr-i munsarif)", 5),
 "mudhayyal": need("mudhayyal", "مُذَيَّل", "ذ ي ل", "noun", "given a tail (ism maf'ul of ذَيَّلَ); the naqis jinas with more than one extra letter", "kuyruk verilmiş (ذَيَّلَ'nin ism-i mef'ûlü); birden fazla harfi fazla olan nâkıs cinas", 5),
 "buka": need("buka", "بُكَاء", "ب ك ي", "noun", "weeping (a mamdud masdar)", "ağlama (memdûd masdar)", 3),
 "shifa": need("shifa", "شِفَاء", "ش ف ي", "noun", "cure, healing (a mamdud)", "şifa (memdûd)", 3),
 "jawa": need("jawa", "جَوًى", "ج و ي", "noun", "burning grief, hidden ardour (a maqsur)", "gizli yangın, iç derdi (maksûr)", 5),
}
for k in ("lafz", "tashabuh", "fi", "bayna", "min", "an-masdariyya", "naw", "harf", "haya-shape", "tartib", "in-shartiyya", "kana", "ism", "samma", "yawm", "qama", "aqsama",
          "ma-nafiya", "ghayr", "ma-mawsula", "mata-die", "karam", "inna", "ibn", "abd", "allah", "ahad", "murakkab", "mafruq", "idha", "malik-king", "lam-jazima", "dhu", "da-leave",
          "illa", "kull", "qad", "akhadha", "la-nafiya-lil-jins", "li", "ma-istifham", "alladhi", "darra", "law", "jubba", "burd", "jahil", "imma", "aw", "bida", "shirk",
          "naqis", "dhalika", "awwal", "akhir", "ila", "rabb", "masaq", "yad", "ziyada", "akthar", "huwa", "janiha", "wa", "fa", "bi", "ka", "pron-3d", "pron-3ms", "pron-3fs",
          "pron-2mp", "pron-1p", "pron-2ms", "pron-1s"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
put_morph(mo, "ittafaqa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِتَّفَق", "تَّفِق", "اِتَّفِق", "اِتِّفَاق", "مُتَّفِق", "مُتَّفَق", "اُتُّفِقَ", "يُتَّفَقُ",
                                       note="مِثَالٌ وَاوِيٌّ فِي الِافْتِعَالِ: تُقْلَبُ الْوَاوُ تَاءً وَتُدْغَمُ — اِتَّفَقَ يَتَّفِقُ."))
put_morph(mo, "ikhtalafa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِخْتَلَف", "خْتَلِف", "اِخْتَلِف", "اِخْتِلَاف", "مُخْتَلِف", "مُخْتَلَف", "اُخْتُلِفَ", "يُخْتَلَفُ"))
put_morph(mo, "jamala", _sg.derived(_sg.B3, _sg.W3, "ُ", "جَامَل", "جَامِل", "جَامِل", "مُجَامَلَة", "مُجَامِل", "مُجَامَل", "جُومِلَ", "يُجَامَلُ"))
put_morph(mo, "labitha", _sg.sound1("samia", "لَبِث", "لْبَث", "اِلْبَث", "لُبْث", "لَابِث", note="لَازِمٌ مِنْ بَابِ سَمِعَ: لَبِثَ يَلْبَثُ لُبْثًا."))
put_morph(mo, "khassa-verb", gem("nasara", "خَصّ", "خَصَص", "خُصّ", "خْصُص", ["خُصَّ", "خُصَّا", "خُصُّوا", "خُصِّي", "خُصَّا", "اُخْصُصْنَ"], "خَصّ", "خَاصّ", "مَخْصُوص", "خُصَّ", "يُخَصُّ",
                             "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: خَصَّ يَخُصُّ — خَصَصْتُ، يَخْصُصْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ."))
put_morph(mo, "madda", gem("nasara", "مَدّ", "مَدَد", "مُدّ", "مْدُد", ["مُدَّ", "مُدَّا", "مُدُّوا", "مُدِّي", "مُدَّا", "اُمْدُدْنَ"], "مَدّ", "مَادّ", "مَمْدُود", "مُدَّ", "يُمَدُّ",
                             "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: مَدَّ يَمُدُّ — مَدَدْتُ، يَمْدُدْنَ."))
put_morph(mo, "iltaffa", _sg.entry(_sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِلْتِفَاف", "مُلْتَفّ", _sg.mazi14("اِلْتَفّ", "اِلْتَفَف"), _sg.mudari14("َ", "لْتَفّ", "لْتَفِف"),
                                    ["اِلْتَفَّ", "اِلْتَفَّا", "اِلْتَفُّوا", "اِلْتَفِّي", "اِلْتَفَّا", "اِلْتَفِفْنَ"], "يَلْتَفَّ", "يَلْتَفَّ", "تَلْتَفَّ", None, None, None,
                                    note="مُضَاعَفٌ مِنَ الِافْتِعَالِ: اِلْتَفَّ يَلْتَفُّ — اِلْتَفَفْتُ، يَلْتَفِفْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ؛ لَازِمٌ."))
put_morph(mo, "hayiya", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ", _sg.BABS["samia"][1], "حَيَاة", "حَيّ",
                                   _sg.mazi_naqis_kasra("حَيِ", "حَيُوا"), _sg.mudari_naqis("َ", "حْي", "a"), _sg.amr_naqis("اِحْي", "a"),
                                   "يَحْيَى", "يَحْيَ", "تَحْيَ", note="نَاقِصٌ مِنْ بَابِ سَمِعَ: حَيِيَ يَحْيَى — مِثْلُ بَقِيَ يَبْقَى؛ وَتُكْتَبُ أَلِفُهُ مَقْصُورَةً."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_T = {
 "id": "jinas-tamm",
 "title": {"ar": "الْجِنَاسُ التَّامُّ — الْمُمَاثِلُ، وَالْمُسْتَوْفَى، وَالْمُرَكَّبُ (الْمُتَشَابِهُ وَالْمَفْرُوقُ)؛ وَالْمُحَرَّفُ", "en": "The complete jinas — mumathil, mustawfa, the composite (mutashabih, mafruq); and the muharraf", "tr": "Tam cinas — mümâsil, müstevfâ, mürekkep (müteşâbih, mefrûk); ve muharref"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الجناس بين اللفظين هو تشابههما في اللفظ، والتام منه أن يتفقا في أنواع الحروف وأعدادها وهيئاتها وترتيبها؛ فإن كانا من نوع واحد كاسمين سمي مماثلا، وإن كانا من نوعين سمي مستوفى، وإن كان أحد اللفظين مركبا سمي جناس التركيب: فإن اتفقا في الخط خص باسم المتشابه وإلا خص باسم المفروق. وإن اختلفا في هيئات الحروف فقط سمي محرفا."],
 "question": {
  "en": ["Do two words SOUND alike while they MEAN differently? That is JINAS — the first of the lafzi muhassinat, the ornaments of the WORDING. Count what the two share: the KINDS of letters, their NUMBER, their SHAPES (the vowels and the shadda), their ORDER. All four alike: the jinas is TAMM.",
         "Then look at the CLASS of the two words. Both nouns, both verbs: MUMATHIL — السَّاعَةُ (the Hour) and سَاعَةٍ (an hour) in 30:55. A verb and a noun: MUSTAWFA — يَحْيَى «lives» and يَحْيَى the man in Abu Tammam. One of them made of TWO words: the jinas of TARKIB — and if the script is one too (ذَا هِبَةٍ / ذَاهِبَةٌ) it is MUTASHABIH, if the script parts them (جَامَ لَنَا / جَامَلَنَا) it is MAFRUQ.",
         "Only the VOWELS differ? MUHARRAF: الْبُرْدِ / الْبَرْدِ, شَرَكُ / الشِّرْكِ, مُفْرِطٌ / مُفَرِّطٌ — and in this door a doubled letter counts as undoubled.",
         "What does the engine read? The JinasEngine aligns the two words letter by letter, strips the article and the pronoun, and names the kind from the alignment: tamm when the skeletons and the vowels are one, muharraf when only the vowels part them; the class test (noun / verb) gives mumathil or mustawfa; a pair authored as murakkab is shown as its two halves against the one word. Which sound is a jinas and which is a plain repeat stays the author's judgement."],
  "tr": ["İki kelime SESTE benzerken MÂNÂDA ayrılıyor mu? Bu CİNÂS'tır — lafzî muhassinâtın, LAFZI süsleyen sanatların ilki. İkisinin ortak olanını say: harflerin NEVİLERİ, SAYILARI, ŞEKİLLERİ (hareke ve şedde), TERTİBİ. Dördü de bir: cinas TAMdır.",
         "Sonra iki kelimenin SINIFINA bak. İkisi de isim, ikisi de fiil: MÜMÂSİL — Rûm 55'te السَّاعَةُ (Kıyamet saati) ile سَاعَةٍ (bir saat). Bir fiil, bir isim: MÜSTEVFÂ — Ebû Temmâm'da يَحْيَى «yaşar» ile Yahyâ. Biri İKİ kelimeden: TERKİP cinası — yazı da bir ise (ذَا هِبَةٍ / ذَاهِبَةٌ) MÜTEŞÂBİH, yazı ayırıyorsa (جَامَ لَنَا / جَامَلَنَا) MEFRÛK.",
         "Yalnız HAREKELER mi ayrı? MUHARREF: الْبُرْدِ / الْبَرْدِ, شَرَكُ / الشِّرْكِ, مُفْرِطٌ / مُفَرِّطٌ — bu bapta şeddeli harf şeddesiz hükmündedir.",
         "Motor neyi okur? JinasEngine iki kelimeyi harf harf hizalar, harf-i tarifi ve zamiri soyar, hizadan kısmı adlandırır: iskelet ve hareke bir ise tam, yalnız hareke ayırıyorsa muharref; sınıf testi (isim / fiil) mümâsil yahut müstevfâyı verir; mürekkep yazılmış çift, iki yarısı tek kelimeye karşı gösterilir. Hangi sesin cinas, hangisinin düz tekrar olduğu müellifin hükmüdür."]},
 "plain": {
  "en": "Jinas: two words alike in sound, different in meaning. Tamm when letters, number, vowels and order all agree; mumathil (same class), mustawfa (noun and verb), tarkib (one word is two) — mutashabih if the script is one, mafruq if not. Muharraf: only the vowels differ.",
  "tr": "Cinas: seste bir, mânâda ayrı iki kelime. Harf, sayı, hareke ve tertip hep bir ise tam; mümâsil (aynı sınıf), müstevfâ (isim ve fiil), terkip (biri iki kelime) — yazı bir ise müteşâbih, değilse mefrûk. Muharref: yalnız hareke ayrı."},
 "explanation": {
  "en": "The Talkhis opens the MUHASSINAT LAFZIYYA with the jinas: الْجِنَاسُ بَيْنَ اللَّفْظَيْنِ تَشَابُهُهُمَا فِي اللَّفْظِ. The TAMM asks four agreements — أَنْوَاعُ الْحُرُوفِ وَأَعْدَادُهَا وَهَيْئَاتُهَا وَتَرْتِيبُهَا — and is named by the CLASS of its two words: MUMATHIL (مِنْ نَوْعٍ وَاحِدٍ), MUSTAWFA (مِنْ نَوْعَيْنِ). If one word is COMPOSITE the jinas is of TARKIB, and the SCRIPT decides its name: MUTASHABIH when the two look the same on the page (ذَا هِبَةٍ / ذَاهِبَةٌ — al-Busti), MAFRUQ when they part (جَامَ لَنَا / جَامَلَنَا). The MUHARRAF keeps every letter and changes only the HAY'A — the vowels — as in جُبَّةُ الْبُرْدِ جُنَّةُ الْبَرْدِ; a shadda does not count as a letter (مُفْرِطٌ / مُفَرِّطٌ).",
  "tr": "Telhîs MUHASSİNÂT-I LAFZİYYE'yi cinasla açar: الْجِنَاسُ بَيْنَ اللَّفْظَيْنِ تَشَابُهُهُمَا فِي اللَّفْظِ. TAM cinas dört uyum ister — أَنْوَاعُ الْحُرُوفِ وَأَعْدَادُهَا وَهَيْئَاتُهَا وَتَرْتِيبُهَا — ve iki kelimesinin SINIFIYLA adlanır: MÜMÂSİL (مِنْ نَوْعٍ وَاحِدٍ), MÜSTEVFÂ (مِنْ نَوْعَيْنِ). Kelimelerden biri MÜREKKEPSE cinas TERKİP cinasıdır ve adını YAZI belirler: sayfada ikisi aynı görünüyorsa MÜTEŞÂBİH (ذَا هِبَةٍ / ذَاهِبَةٌ — Büstî), ayrılıyorsa MEFRÛK (جَامَ لَنَا / جَامَلَنَا). MUHARREF her harfi korur, yalnız HEY'ET'i — harekeleri — değiştirir: جُبَّةُ الْبُرْدِ جُنَّةُ الْبَرْدِ; şedde harf sayılmaz (مُفْرِطٌ / مُفَرِّطٌ)."},
 "examples": [
  {"ar": "وَيَوْمَ تَقُومُ السَّاعَةُ يُقْسِمُ الْمُجْرِمُونَ مَا لَبِثُوا غَيْرَ سَاعَةٍ", "en": "30:55 — tamm mumathil.", "tr": "Rûm 55 — tam mümâsil.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "مَا مَاتَ مِنْ كَرَمِ الزَّمَانِ فَإِنَّهُ * يَحْيَى لَدَى يَحْيَى بْنِ عَبْدِ اللهِ", "en": "Abu Tammam — tamm mustawfa.", "tr": "Ebû Temmâm — tam müstevfâ.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "إِذَا مَلِكٌ لَمْ يَكُنْ ذَا هِبَةٍ * فَدَعْهُ فَدَوْلَتُهُ ذَاهِبَةٌ", "en": "al-Busti — tarkib, mutashabih.", "tr": "Büstî — terkip, müteşâbih.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "جُبَّةُ الْبُرْدِ جُنَّةُ الْبَرْدِ", "en": "muharraf.", "tr": "muharref.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"}],
 "commonMistakes": [
  {"wrong": "«السَّاعَةُ ile سَاعَةٍ aynı kelimenin tekrarıdır, cinas değil»",
   "right": "«Cinâs-ı tam mümâsildir: seste bir, mânâda ayrı — Kıyamet saati ve bir zaman parçası»",
   "why": {"en": "Jinas needs two MEANINGS under one sound; a plain repeat has one.", "tr": "Cinas tek ses altında iki MÂNÂ ister; düz tekrarda bir mânâ vardır."}},
  {"wrong": "«مُفْرِطٌ / مُفَرِّطٌ harf sayısı ayrı olduğu için nâkıstır»",
   "right": "«Muharreftir: bu bapta şeddeli harf şeddesiz hükmündedir; yalnız hey'et ayrılır»",
   "why": {"en": "The Talkhis says it in so many words: the doubled letter counts as undoubled in this door.", "tr": "Telhîs açıkça söyler: bu bapta şeddeli harf şeddesiz hükmündedir."}}],
 "relatedNotes": ["jinas", "jinas-naqis", "ilm-al-badi", "al-muthanna", "five-nouns"]}

NOTE_N = {
 "id": "jinas-naqis",
 "title": {"ar": "الْجِنَاسُ النَّاقِصُ — الزِّيَادَةُ فِي الْأَوَّلِ أَوِ الْوَسَطِ أَوِ الْآخِرِ (الْمُطَرَّفُ)؛ وَبِأَكْثَرَ مِنْ حَرْفٍ (الْمُذَيَّلُ)", "en": "The naqis jinas — the extra letter first, middle or last (mutarraf); more than one (mudhayyal)", "tr": "Nâkıs cinas — fazla harf başta, ortada yahut sonda (mutarraf); birden fazla (müzeyyel)"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — وإن اختلفا في أعداد الحروف سمي ناقصا، وذلك إما بحرف في الأول نحو: والتفت الساق بالساق إلى ربك يومئذ المساق، أو في الوسط كقولهم: جدي جهدي، أو في الآخر كقوله: يمدون من أيد عواص عواصم — ويسمى مطرفا؛ أو بأكثر كقولها: إن البكاء هو الشفاء من الجوى بين الجوانح — ويسمى مذيلا."],
 "question": {
  "en": ["Are the two words alike but for a LETTER one of them has and the other has not? NAQIS. Find WHERE the extra letter sits: at the BEGINNING — السَّاقُ / الْمَسَاقُ (75:29-30, the mim); in the MIDDLE — جَدِّي / جَهْدِي (the ha); at the END — عَوَاصٍ / عَوَاصِمِ (Abu Tammam, the mim), and this last is the MUTARRAF, «lined at the edge».",
         "Is the addition MORE than one letter? MUDHAYYAL, «given a tail»: الْجَوَى / الْجَوَانِحِ in al-Khansa.",
         "What does the engine read? The alignment counts the letters the two share in order; one letter over on one side names the naqis and its PLACE (first, middle, last); two or more name the mudhayyal. The engine also refuses a pair whose skeletons share too little to be a jinas at all."],
  "tr": ["İki kelime, birinde olup öbüründe olmayan bir HARF dışında bir mi? NÂKIS. Fazla harfin YERİNİ bul: BAŞTA — السَّاقُ / الْمَسَاقُ (Kıyâme 29-30, mîm); ORTADA — جَدِّي / جَهْدِي (hâ); SONDA — عَوَاصٍ / عَوَاصِمِ (Ebû Temmâm, mîm); bu sonuncusu MUTARRAF, «kenarı işlenmiş».",
         "Ziyade BİRDEN FAZLA harf mi? MÜZEYYEL, «kuyruk verilmiş»: Hansâ'da الْجَوَى / الْجَوَانِحِ.",
         "Motor neyi okur? Hizalama, ikisinin sırayla paylaştığı harfleri sayar; bir yanda fazla bir harf nâkısı ve YERİNİ (baş, orta, son) adlandırır; iki ve daha fazlası müzeyyeli. İskeletleri cinas olamayacak kadar az ortak olan çifti motor reddeder."]},
 "plain": {
  "en": "Naqis: the two words differ by a letter. First (السَّاقُ / الْمَسَاقُ), middle (جَدِّي / جَهْدِي), last = mutarraf (عَوَاصٍ / عَوَاصِمِ); more than one letter = mudhayyal (الْجَوَى / الْجَوَانِحِ).",
  "tr": "Nâkıs: iki kelime bir harfle ayrılır. Başta (السَّاقُ / الْمَسَاقُ), ortada (جَدِّي / جَهْدِي), sonda = mutarraf (عَوَاصٍ / عَوَاصِمِ); birden fazla harf = müzeyyel (الْجَوَى / الْجَوَانِحِ)."},
 "explanation": {
  "en": "When the two words differ in the NUMBER of letters — وَإِنِ اخْتَلَفَا فِي أَعْدَادِ الْحُرُوفِ — the jinas is NAQIS, and the Talkhis sorts it by the PLACE of the extra letter: فِي الْأَوَّلِ (the mim of الْمَسَاقُ against السَّاقُ), فِي الْوَسَطِ (the ha of جَهْدِي against جَدِّي), فِي الْآخِرِ (the mim of عَوَاصِمِ against عَوَاصٍ) — the last is the MUTARRAF. When the addition is بِأَكْثَرَ مِنْ حَرْفٍ, the jinas is MUDHAYYAL: الْجَوَانِحِ carries two letters more than الْجَوَى.",
  "tr": "İki kelime harflerin SAYISINDA ayrılınca — وَإِنِ اخْتَلَفَا فِي أَعْدَادِ الْحُرُوفِ — cinas NÂKIS'tır ve Telhîs onu fazla harfin YERİNE göre ayırır: فِي الْأَوَّلِ (السَّاقُ karşısında الْمَسَاقُ'un mîmi), فِي الْوَسَطِ (جَدِّي karşısında جَهْدِي'nin hâsı), فِي الْآخِرِ (عَوَاصٍ karşısında عَوَاصِمِ'in mîmi) — sonuncusu MUTARRAF. Ziyade بِأَكْثَرَ مِنْ حَرْفٍ olunca cinas MÜZEYYEL'dir: الْجَوَانِحِ, الْجَوَى'dan iki harf fazla taşır."},
 "examples": [
  {"ar": "وَالْتَفَّتِ السَّاقُ بِالسَّاقِ إِلَى رَبِّكَ يَوْمَئِذٍ الْمَسَاقُ", "en": "75:29-30 — naqis, first.", "tr": "Kıyâme 29-30 — nâkıs, başta.", "sourceStory": "talkhis-al-miftah", "sentence": "s16"},
  {"ar": "جَدِّي جَهْدِي", "en": "naqis, middle.", "tr": "nâkıs, ortada.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"},
  {"ar": "يَمُدُّونَ مِنْ أَيْدٍ عَوَاصٍ عَوَاصِمِ", "en": "Abu Tammam — mutarraf.", "tr": "Ebû Temmâm — mutarraf.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"},
  {"ar": "إِنَّ الْبُكَاءَ هُوَ الشِّفَاءُ * مِنَ الْجَوَى بَيْنَ الْجَوَانِحِ", "en": "al-Khansa — mudhayyal.", "tr": "Hansâ — müzeyyel.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"}],
 "commonMistakes": [
  {"wrong": "«عَوَاصٍ / عَوَاصِمِ müzeyyeldir: kuyruk sonda»",
   "right": "«Mutarraftır: tek harf fazladır; müzeyyel birden fazla harf ister»",
   "why": {"en": "The count decides, not the place: one letter at the end is the mutarraf.", "tr": "Yer değil sayı belirler: sonda tek harf mutarraftır."}}],
 "relatedNotes": ["jinas", "jinas-tamm", "ilm-al-badi", "ism-maqsur-manqus", "mamnu-min-sarf"]}

ADD_EN = (" Chapter 68 (lines ~4395-4445, sahifa 152-153) opens the lafzi muhassinat with the jinas: the tamm mumathil (30:55 s4), the mustawfa "
          "(Abu Tammam s6), the tarkib's mutashabih (al-Busti s8) and mafruq (al-Busti s10), the muharraf (s12-s14), the naqis at the beginning "
          "(75:29-30 s16), the middle (s17), the end — the mutarraf (Abu Tammam s18) — and the mudhayyal (al-Khansa s20). The definition and the "
          "headings (s1-s3, s5, s7, s9, s11, s15, s19) are RESTORED: the source carries them only in Turkish, and the Arabic is the received matn "
          "of the Talkhis; every restored sentence is marked «Restored» in its translation. The verb يَحْيَى (s6) is written with the alif maqsura "
          "as the source prints it. The examples carry `badi` frames of kind `jinas` with the `sub` (tamm, murakkab, muharraf, naqis), a `kind2` "
          "(mumathil, mustawfa, mutashabih, mafruq; awwal, wasat, akhir, mudhayyal) and the `pair` — or `first`/`second` for the murakkab.")
ADD_TR = (" Altmış sekizinci bâb (satır ~4395-4445, sahife 152-153) lafzî muhassinâtı cinasla açar: tam mümâsil (Rûm 55 s4), müstevfâ (Ebû "
          "Temmâm s6), terkibin müteşâbihi (Büstî s8) ve mefrûku (Büstî s10), muharref (s12-s14), başta nâkıs (Kıyâme 29-30 s16), ortada (s17), "
          "sonda — mutarraf (Ebû Temmâm s18) — ve müzeyyel (Hansâ s20). Tarif ve başlıklar (s1-s3, s5, s7, s9, s11, s15, s19) GERİ YAZILMIŞTIR: "
          "kaynak bunları yalnız Türkçe taşır; Arapça, Telhîs'in alınan metnidir; her geri yazılmış cümle tercümesinde «geri yazılmıştır» diye "
          "işaretlidir. يَحْيَى fiili (s6) kaynağın bastığı gibi elif-i maksûre ile yazılmıştır. Örnekler `jinas` cinsinden `badi` çerçeveleri taşır: "
          "`sub` (tam, mürekkep, muharref, nâkıs), `kind2` (mümâsil, müstevfâ, müteşâbih, mefrûk; evvel, vasat, âhir, müzeyyel) ve `pair` — "
          "mürekkep için `first`/`second`.")
write_out(68, S, TITLE, ADD_EN, ADD_TR, "4395-4445", GLOSS_ADD, notes=(NOTE_T, NOTE_N),
          related=(("jinas", ["jinas-tamm", "jinas-naqis"]), ("ilm-al-badi", ["jinas-tamm", "jinas-naqis"])))
report(68, S, GLOSS_ADD, (NOTE_T, NOTE_N))
