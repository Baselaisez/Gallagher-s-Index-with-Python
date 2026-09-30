# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 69: JINAS continued — the MUDARIʿ and the LAHIQ (a letter of another kind, first, middle or last; near
or far in makhraj), the jinas of QALB (whole, partial; the mujannah), the MUZDAWIJ, and the two things ATTACHED to the jinas
(ishtiqaq, shibh ishtiqaq). Source lines ~4445-4475 (sahifa 153-154).

  RESTORED (the source carries the step only in Turkish): s1, s2, s6, s10, s13, s15, s17, s19 (the headings of the kinds). The examples
  (s3 the saying, s4 6:26, s5 the hadith, s7 104:1, s8 40:75, s9 4:83, s11, s12 the prayer, s14, s16 27:22, s18 30:43, s20 26:168) are the
  source's printed Arabic; the Qur'an as the source prints it — the print of 4:83 opens on فَإِذَا (the mushaf: وَإِذَا) and writes سَبَأٍ
  بِنَبَأٍ (the mushaf: سَبَإٍ بِنَبَإٍ), kept as printed and said so in the attribution.

  python3 tools/authoring/author_talkhis_ch69.py
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

M = "jinas-mudari-lahiq"; Q = "jinas-qalb"; L = "mulhaq-bil-jinas"
TITLE = {"ar": "الْجِنَاسُ: الْمُضَارِعُ، وَاللَّاحِقُ، وَتَجْنِيسُ الْقَلْبِ، وَالْمُزْدَوِجُ، وَمَا يُلْحَقُ بِالْجِنَاسِ", "en": "Jinas: the mudariʿ, the lahiq, the jinas of qalb, the muzdawij, and what is attached to the jinas", "tr": "Cinâs: muzâri, lâhik, kalb cinâsı, müzdevic ve cinâsa ilhak edilenler"}
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
def aw_fi(tag, word, lex, en, tr):
    return [tok("أَوْ", "aw", "conj", [tag, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."), fi(tag), tok(word, lex, "noun", [tag, "huruf-jarr"], "مَجْرُورٌ.", en, tr)]
def place_list(tag):
    return [tok("إِمَّا", "imma", "part", [tag, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
            tok("فِي", "fi", "prep", [tag, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«at» — the jarr phrase is the khabar.", "«-de» — câr-mecrûr haber."),
            tok("الْأَوَّلِ", "awwal", "noun", [tag, "huruf-jarr"], "مَجْرُورٌ.", "«the beginning».", "«başta».")] + \
           aw_fi(tag, "الْوَسَطِ", "wasat", "«the middle».", "«ortada».") + aw_fi(tag, "الْآخِرِ", "akhir", "«the end».", "«sonda».")

# ----------- s1 — a letter of another kind: no more than one (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "And if the two differ in the KINDS of the letters, it is stipulated that the difference be by NO MORE than one letter." + R_EN,
 "tr": "Harflerin NEVİLERİNDE ayrılırlarsa, ayrılığın BİR HARFTEN FAZLA olmaması şart koşulur." + R_TR},
 "tokens": [
  wa_in(M, "وَإِنِ"),
  tok("اخْتَلَفَا","ikhtalafa","verb",[M, "in-shartiyya", "fail", "al-muthanna"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالْأَلِفُ فَاعِلٌ.", "«the two differ» — the shart verb; the alif is the doer.", "«ikisi ayrılırsa» — şart fiili; elif fâil."),
  fi(M),
  tok("أَنْوَاعِ","naw","noun",[M, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، مُضَافٌ.", "«the kinds of».", "«nevilerinde»."),
  tok("الْحُرُوفِ","harf","noun",[M, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the letters».", "«harflerin»."),
  tok("فَيُشْتَرَطُ","ishtarata","verb",[M, "naib-al-fail", "in-shartiyya", "mudari-marfu"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَيُشْتَرَطُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«then it is stipulated» — the fa of the jawab; the passive; its deputy is the clause after it.", "«şart koşulur» — cevap fâsı; meçhul; nâibi sonraki cümledir.",
      segments=[seg("فَ","fa","conj"), seg("يُشْتَرَطُ","ishtarata","verb")]),
  tok("أَلَّا","an-masdariyya","part",[M, "an-masdariyya"], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَلَا نَافِيَةٌ — أُدْغِمَتِ النُّونُ فِي اللَّامِ.", "«that … not» — an + la written as one.", "«-maması» — en + lâ bitişik.",
      segments=[seg("أَنْ","an-masdariyya","part"), seg("لَا","la-nafiya","part")]),
  tok("يَقَعَ","waqaa","verb",[M, "an-masdariyya", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — مِثَالٌ وَاوِيٌّ حُذِفَتْ وَاوُهُ.", "«fall» — mansub by an; the mithal verb whose waw drops.", "«düşsün» — en ile mansûb; vâvı düşen misal fiil."),
  tok("الِاخْتِلَافُ","ikhtilaf","noun",[M, "fail"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ اخْتَلَفَ.", "«the difference» — the doer; the masdar of ikhtalafa.", "«ayrılık» — fâil; ihtelefe'nin masdarı."),
  tok("بِأَكْثَرَ","akthar","noun",[M, "huruf-jarr", "mamnu-min-sarf", "ism-tafdil"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَكْثَرَ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«by more» — the diptote afʿal.", "«daha fazla ile» — gayr-i munsarif.",
      segments=[seg("بِ","bi","prep"), seg("أَكْثَرَ","akthar","noun")]),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  tok("حَرْفٍ","harf","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«one letter».", "«bir harf»."),
 ]})

# ----------- s2 — near in makhraj: the mudariʿ (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "Then, if the two letters are NEAR in point of articulation, it is called MUDARIʿ; and that is either at the beginning, or in the middle, or at the end." + R_EN,
 "tr": "Sonra iki harf mahreçte birbirine YAKINSA MUZÂRİ denir; bu ya başta, ya ortada, ya sonda olur." + R_TR},
 "tokens": [
  tok("ثُمَّ","thumma","conj",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.", "«then».", "«sonra»."),
  tok("إِنْ","in-shartiyya","part",[M, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("كَانَ","kana","verb",[M, "kana-wa-akhawatuha", "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ.", "«are» — kana, the shart verb.", "«olursa» — kâne, şart fiili."),
  tok("الْحَرْفَانِ","harf","noun",[M, "kana-wa-akhawatuha", "al-muthanna"], "اسْمُ كَانَ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«the two letters» — kana's ism, a dual.", "«iki harf» — kânenin ismi, tesniye."),
  tok("مُتَقَارِبَيْنِ","mutaqarib","noun",[M, "kana-wa-akhawatuha", "al-muthanna", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ — مُثَنًّى، اسْمُ فَاعِلٍ مِنْ تَقَارَبَ.", "«near to each other» — kana's khabar, a dual participle.", "«birbirine yakın» — kânenin haberi, tesniye ism-i fâil."),
  fi(M),
  tok("الْمَخْرَجِ","makhraj-harf","noun",[M, "huruf-jarr"], "مَجْرُورٌ — الْمَخْرَجُ: مَوْضِعُ خُرُوجِ الْحَرْفِ مِنَ الْفَمِ.", "«the point of articulation».", "«mahreç»."),
  summiya(M),
  tok("مُضَارِعًا","mudari-jinas","noun",[M, "mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ ضَارَعَ: شَابَهَ.", "«mudariʿ» — «resembling»: the near letters make the two words almost one.", "«muzâri» — «benzeşen»: yakın harfler iki kelimeyi neredeyse bir eder.", punct="،"),
  tok("وَهُوَ","huwa","pron",[M, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
 ] + place_list(M)})

# ----------- s3 — a dark night and an effaced road (first)
S.append({"id": "s3", "translation": {
 "en": "«Between me and my shelter is a PITCH-DARK (damis) night and an EFFACED (tamis) road.» — the dal and the ta, first.",
 "tr": "«Benimle sığınağım arasında ZİFİRÎ (dâmis) bir gece ve SİLİNMİŞ (tâmis) bir yol var.» — dâl ve tâ, başta."},
 "tokens": [
  tok("بَيْنِي","bayna","noun",[M, "maful-fih", "idafa-definiteness", "mubtada-khabar"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْيَاءُ مُضَافٌ إِلَيْهِ؛ خَبَرٌ مُقَدَّمٌ.", "«between me» — the zarf with the speaker's ya; the fronted khabar.", "«benimle» — mütekellim yâsıyla zarf; öne alınmış haber.",
      segments=[seg("بَيْنِ","bayna","noun"), seg("ي","pron-1s","pron")]),
  tok("وَبَيْنَ","bayna","noun",[M, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَعْطُوفٌ، مُضَافٌ.", "«and between» — joined, annexed.", "«ve» — atıf, muzâf.",
      segments=[seg("وَ","wa","conj"), seg("بَيْنَ","bayna","noun")]),
  tok("كِنِّي","kinn","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — وَالْيَاءُ مُضَافٌ إِلَيْهِ؛ الْكِنُّ: السِّتْرُ وَالْمَأْوَى.", "«my shelter» — annexed to: the cover one takes.", "«sığınağım» — muzâfun ileyh: sığınılan yer.",
      segments=[seg("كِنِّ","kinn","noun"), seg("ي","pron-1s","pron")]),
  tok("لَيْلٌ","layl","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a night» — the delayed mubtada.", "«bir gece» — sona bırakılmış mübtedâ."),
  tok("دَامِسٌ","damis","noun",[M, "ism-fail"], "نَعْتٌ مَرْفُوعٌ — دَامِسٌ: شَدِيدُ الظُّلْمَةِ.", "«pitch-dark» — the na't.", "«zifirî» — na't."),
  tok("وَطَرِيقٌ","tariq","noun",[M, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَطَرِيقٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a road» — joined.", "«ve bir yol» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("طَرِيقٌ","tariq","noun")]),
  tok("طَامِسٌ","tamis","noun",[M, "ism-fail"], "نَعْتٌ مَرْفُوعٌ — طَامِسٌ: مُنْدَرِسُ الْأَثَرِ.", "«effaced» — the na't: its track wiped out.", "«silinmiş» — na't: izi kaybolmuş."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "mudari", "kind2": "awwal", "pair": [ix(S[-1], "دَامِسٌ"), ix(S[-1], "طَامِسٌ")]}]

# ----------- s4 — 6:26: they forbid and keep far (middle)
S.append({"id": "s4", "translation": {
 "en": "«And they FORBID (yanhawna) from it and KEEP FAR (yan'awna) from it» (6:26) — the ha and the hamza, in the middle.",
 "tr": "«Onlar hem ondan MENEDERLER (yenhevne) hem ondan UZAKLAŞIRLAR (yen'evne)» (En'âm 26) — hâ ve hemze, ortada."},
 "tokens": [
  tok("وَهُمْ","hum","pron",[M, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُمْ مُبْتَدَأٌ.", "«and they» — the mubtada.", "«ve onlar» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُمْ","hum","pron")]),
  tok("يَنْهَوْنَ","naha","verb",[M, "mubtada-khabar", "naqis-verbs", "afal-khamsa", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ — نَاقِصٌ، وَالْوَاوُ فَاعِلٌ؛ وَالْجُمْلَةُ خَبَرٌ.", "«they forbid» — the naqis verb with its waw doer; the khabar.", "«menederler» — vâv fâilli nâkıs fiil; haber."),
  tok("عَنْهُ","an","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«from it».", "«ondan».",
      segments=[seg("عَنْ","an","part"), seg("هُ","pron-3ms","pron")]),
  tok("وَيَنْأَوْنَ","naa","verb",[M, "atf-nasaq", "naqis-verbs", "afal-khamsa", "fail"], "الْوَاوُ عَاطِفَةٌ، وَيَنْأَوْنَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ — مَهْمُوزُ الْعَيْنِ نَاقِصٌ، وَالْوَاوُ فَاعِلٌ.", "«and they keep far» — joined; a hamzated naqis verb.", "«ve uzaklaşırlar» — atıf; hemzeli nâkıs fiil.",
      segments=[seg("وَ","wa","conj"), seg("يَنْأَوْنَ","naa","verb")]),
  tok("عَنْهُ","an","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«from it».", "«ondan».",
      segments=[seg("عَنْ","an","part"), seg("هُ","pron-3ms","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "mudari", "kind2": "wasat", "pair": [ix(S[-1], "يَنْهَوْنَ"), ix(S[-1], "وَيَنْأَوْنَ")]}]

# ----------- s5 — the hadith: horses and good (last)
S.append({"id": "s5", "translation": {
 "en": "«HORSES (al-khayl): GOOD (al-khayr) is knotted in their forelocks until the Day of Rising» (hadith) — the lam and the ra, last.",
 "tr": "«ATLAR (hayl): HAYIR (hayr) kıyamet gününe kadar alınlarına bağlanmıştır» (hadis) — lâm ve râ, sonda."},
 "tokens": [
  tok("الْخَيْلُ","khayl","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ جَمْعٍ.", "«horses» — the mubtada, a collective.", "«atlar» — mübtedâ, ism-i cem'."),
  tok("مَعْقُودٌ","maqud","noun",[M, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ يَعْمَلُ عَمَلَ فِعْلِهِ.", "«knotted» — the khabar, a participle that governs.", "«bağlanmış» — haber, amel eden ism-i mef'ûl."),
  tok("بِنَوَاصِيهَا","nasiya-forelock","noun",[M, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَوَاصِيهَا مَجْرُورٌ مُضَافٌ — جَمْعُ نَاصِيَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in their forelocks».", "«alınlarına».",
      segments=[seg("بِ","bi","prep"), seg("نَوَاصِي","nasiya-forelock","noun"), seg("هَا","pron-3fs","pron")]),
  tok("الْخَيْرُ","khayr","noun",[M, "naib-al-fail"], "نَائِبُ فَاعِلٍ لِمَعْقُودٍ مَرْفُوعٌ.", "«good» — the deputy of the participle.", "«hayır» — ism-i mef'ûlün nâibi."),
  tok("إِلَى","ila","prep",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«until».", "«-e kadar»."),
  tok("يَوْمِ","yawm","noun",[M, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the Day of».", "«gününe»."),
  tok("الْقِيَامَةِ","qiyama","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Rising».", "«kıyamet»."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "mudari", "kind2": "akhir", "pair": [ix(S[-1], "الْخَيْلُ"), ix(S[-1], "الْخَيْرُ")]}]

# ----------- s6 — far in makhraj: the lahiq (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "Otherwise it is called LAHIQ; and it too is either at the beginning, or in the middle, or at the end." + R_EN,
 "tr": "Aksi hâlde LÂHİK denir; o da ya başta, ya ortada, ya sondadır." + R_TR},
 "tokens": [
  tok("وَإِلَّا","illa","part",[M, "in-shartiyya", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ الشَّرْطِيَّةُ وَلَا النَّافِيَةُ — أَيْ وَإِنْ لَمْ يَتَقَارَبَا.", "«otherwise» — in + la: if the two letters are not near.", "«yoksa» — in + lâ: iki harf yakın değilse.",
      segments=[seg("وَ","wa","conj"), seg("إِلَّا","illa","part")]),
  summiya(M),
  tok("لَاحِقًا","lahiq","noun",[M, "mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ لَحِقَ.", "«lahiq» — «attached»: the far letters leave the two words merely joined.", "«lâhik» — «bitişik»: uzak harfler iki kelimeyi yalnız bağlı bırakır.", punct="،"),
  tok("وَهُوَ","huwa","pron",[M, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("كَذَلِكَ","dhalika","pron",[M, "asma-al-ishara", "huruf-jarr", "hal"], "الْكَافُ حَرْفُ جَرٍّ، وَذَلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — حَالٌ: أَيْ مِثْلُ الْمُضَارِعِ.", "«likewise» — like the mudariʿ.", "«böylece» — muzâri gibi.",
      segments=[seg("كَ","ka","part"), seg("ذَلِكَ","dhalika","pron")]),
 ] + place_list(M)})

# ----------- s7 — 104:1: humaza lumaza (first)
S.append({"id": "s7", "translation": {
 "en": "«Woe to every BACKBITER (humaza), SLANDERER (lumaza)» (104:1) — the ha and the lam, first.",
 "tr": "«Her AYIPLAYANIN (hümeze), ÇEKİŞTİRENİN (lümeze) vay hâline» (Hümeze 1) — hâ ve lâm, başta."},
 "tokens": [
  tok("وَيْلٌ","wayl","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ جَازَ الِابْتِدَاءُ بِهَا لِأَنَّهَا دُعَاءٌ.", "«woe» — a nakira mubtada, allowed because it is a curse.", "«vay» — beddua olduğu için nekre mübtedâ."),
  tok("لِكُلِّ","kull","noun",[M, "huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«to every» — the khabar.", "«her» — haber.",
      segments=[seg("لِ","li","prep"), seg("كُلِّ","kull","noun")]),
  tok("هُمَزَةٍ","humaza","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — صِيغَةُ مُبَالَغَةٍ: كَثِيرُ الْهَمْزِ، الطَّعْنِ فِي النَّاسِ.", "«backbiter» — annexed to; the intensive: who jabs at people.", "«ayıplayan» — muzâfun ileyh; mübalağa: insanları yeren."),
  tok("لُمَزَةٍ","lumaza","noun",[M, "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ — كَثِيرُ اللَّمْزِ: الْعَيْبِ بِالْإِشَارَةِ.", "«slanderer» — the na't: who faults with a gesture.", "«çekiştiren» — na't: işaretle kusur bulan."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "lahiq", "kind2": "awwal", "pair": [ix(S[-1], "هُمَزَةٍ"), ix(S[-1], "لُمَزَةٍ")]}]

# ----------- s8 — 40:75: you exulted and you were insolent (middle)
S.append({"id": "s8", "translation": {
 "en": "«That is because you EXULTED (tafrahuna) in the earth without right, and because you were INSOLENT (tamrahuna)» (40:75) — the fa and the mim, in the middle.",
 "tr": "«Bu, yeryüzünde haksız yere ŞIMARMANIZ (tefrahûn) ve TAŞKINLIK ETMENİZ (temrahûn) sebebiyledir» (Mü'min 75) — fâ ve mîm, ortada."},
 "tokens": [
  tok("ذَلِكُمْ","dhalikum","pron",[M, "asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ — الْكَافُ وَالْمِيمُ لِلْخِطَابِ.", "«that» — the demonstrative for a plural addressee.", "«bu» — çoğul muhataba işaret."),
  tok("بِمَا","ma-masdariyya","part",[M, "huruf-jarr", "anwa-ma", "mubtada-khabar"], "الْبَاءُ لِلسَّبَبِيَّةِ، وَمَا مَصْدَرِيَّةٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«because of» — the ba of cause; the masdar-ma; the khabar.", "«sebebiyle» — sebep bâsı; masdariyye mâ; haber.",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-masdariyya","part")]),
  tok("كُنْتُمْ","kana","verb",[M, "kana-wa-akhawatuha", "anwa-ma"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ.", "«you were» — kana with its ism.", "«idiniz» — kâne ve ismi."),
  tok("تَفْرَحُونَ","fariha","verb",[M, "kana-wa-akhawatuha", "afal-khamsa", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كَانَ.", "«exulted» — kana's khabar.", "«şımarıyordunuz» — kânenin haberi."),
  fi(M),
  tok("الْأَرْضِ","ard","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the earth».", "«yeryüzünde»."),
  tok("بِغَيْرِ","ghayr","noun",[M, "huruf-jarr", "idafa-definiteness", "hal"], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ مُضَافٌ — حَالٌ.", "«without» — a hal.", "«-sız» — hâl.",
      segments=[seg("بِ","bi","prep"), seg("غَيْرِ","ghayr","noun")]),
  tok("الْحَقِّ","haqq","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«right».", "«hak»."),
  tok("وَبِمَا","ma-masdariyya","part",[M, "atf-nasaq", "huruf-jarr", "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَبِمَا جَارٌّ وَمَصْدَرِيَّةٌ.", "«and because of».", "«ve sebebiyle».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","prep"), seg("مَا","ma-masdariyya","part")]),
  tok("كُنْتُمْ","kana","verb",[M, "kana-wa-akhawatuha", "anwa-ma"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ.", "«you were».", "«idiniz»."),
  tok("تَمْرَحُونَ","mariha","verb",[M, "kana-wa-akhawatuha", "afal-khamsa", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — خَبَرُ كَانَ؛ الْمَرَحُ: شِدَّةُ الْفَرَحِ وَالْبَطَرُ.", "«were insolent» — kana's khabar: exulting past measure.", "«taşkınlık ediyordunuz» — kânenin haberi: ölçüsüz sevinç."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "lahiq", "kind2": "wasat", "pair": [ix(S[-1], "تَفْرَحُونَ"), ix(S[-1], "تَمْرَحُونَ")]}]

# ----------- s9 — 4:83: a matter of safety (last)
S.append({"id": "s9", "translation": {
 "en": "«When there comes to them a MATTER (amr) of SAFETY (al-amn)» (4:83, as the source prints it) — the ra and the nun, last.",
 "tr": "«Onlara GÜVENLİĞE (emn) dair bir HABER (emr) geldiğinde» (Nisâ 83, kaynağın bastığı gibi) — râ ve nûn, sonda."},
 "tokens": [
  tok("فَإِذَا","idha","part",[M, "idha-shartiyya", "maful-fih"], "الْفَاءُ كَمَا فِي الْمَطْبُوعِ (وَفِي الْمُصْحَفِ: وَإِذَا)، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the fa as the source prints it (the mushaf: وَإِذَا); the zarf of condition.", "«ve -ince» — fâ kaynağın baskısınca (mushaf: وَإِذَا); şart zarfı.",
      segments=[seg("فَ","fa","conj"), seg("إِذَا","idha","part")]),
  tok("جَاءَهُمْ","jaa","verb",[M, "hollow-verbs", "maful-bihi", "idha-shartiyya"], "فِعْلٌ مَاضٍ، وَهُمْ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«there comes to them» — with its object before the doer.", "«onlara gelir» — mef'ulü fâilden önce.",
      segments=[seg("جَاءَ","jaa","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("أَمْرٌ","amr","noun",[M, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a matter» — the doer.", "«bir haber» — fâil."),
  tok("مِنَ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ — فُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of».", "«-e dair»."),
  tok("الْأَمْنِ","amn","noun",[M, "huruf-jarr"], "مَجْرُورٌ — الْأَمْنُ: ضِدُّ الْخَوْفِ.", "«safety» — the opposite of fear.", "«güvenlik» — korkunun zıddı."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "lahiq", "kind2": "akhir", "pair": [ix(S[-1], "أَمْرٌ"), ix(S[-1], "الْأَمْنِ")]}]

# ----------- s10 — the order of the letters: the jinas of qalb (RESTORED)
S.append({"id": "s10", "translation": {
 "en": "And if the two differ in the ORDER of the letters, it is called the tajnis of QALB (reversal)." + R_EN,
 "tr": "Harflerin TERTİBİNDE ayrılırlarsa, KALB tecnîsi denir." + R_TR},
 "tokens": [
  wa_in(Q, "وَإِنِ"),
  tok("اخْتَلَفَا","ikhtalafa","verb",[Q, "in-shartiyya", "fail", "al-muthanna"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ، وَالْأَلِفُ فَاعِلٌ.", "«the two differ» — the shart verb.", "«ikisi ayrılırsa» — şart fiili."),
  fi(Q),
  tok("التَّرْتِيبِ","tartib","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«the order».", "«tertipte»."),
  summiya(Q),
  tok("تَجْنِيسَ","tajnis","noun",[Q, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ — التَّجْنِيسُ: الْجِنَاسُ.", "«the tajnis of» — the second object, annexed: tajnis is jinas.", "«tecnîsi» — ikinci mef'ul, muzâf: tecnîs cinastır."),
  tok("الْقَلْبِ","qalb-reversal","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْقَلْبُ: عَكْسُ التَّرْتِيبِ.", "«reversal» — the order turned round.", "«kalb» — tertibin tersine dönmesi."),
 ]})

# ----------- s11 — his sword: victory for friends, doom for enemies (qalb kull)
S.append({"id": "s11", "translation": {
 "en": "«His sword is VICTORY (fath) for his friends and DOOM (hatf) for his enemies» — every letter reversed: qalb of the whole.",
 "tr": "«Kılıcı dostlarına FETİH (feth), düşmanlarına ÖLÜMDÜR (hatf)» — her harf ters: bütünün kalbi."},
 "tokens": [
  tok("حُسَامُهُ","husam","noun",[Q, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his sword» — the mubtada.", "«kılıcı» — mübtedâ.",
      segments=[seg("حُسَامُ","husam","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فَتْحٌ","fath","noun",[Q, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«victory» — the khabar.", "«fetih» — haber."),
  tok("لِأَوْلِيَائِهِ","wali","noun",[Q, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَأَوْلِيَائِهِ مَجْرُورٌ مُضَافٌ — جَمْعُ وَلِيٍّ.", "«for his friends».", "«dostlarına».",
      segments=[seg("لِ","li","prep"), seg("أَوْلِيَاءِ","wali","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَحَتْفٌ","hatf","noun",[Q, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَحَتْفٌ مَعْطُوفٌ عَلَى الْخَبَرِ.", "«and doom» — joined to the khabar.", "«ve ölüm» — habere atıf.",
      segments=[seg("وَ","wa","conj"), seg("حَتْفٌ","hatf","noun")]),
  tok("لِأَعْدَائِهِ","aduww","noun",[Q, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَأَعْدَائِهِ مَجْرُورٌ مُضَافٌ — جَمْعُ عَدُوٍّ.", "«for his enemies».", "«düşmanlarına».",
      segments=[seg("لِ","li","prep"), seg("أَعْدَاءِ","aduww","noun"), seg("هِ","pron-3ms","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "qalb", "kind2": "kull", "pair": [ix(S[-1], "فَتْحٌ"), ix(S[-1], "وَحَتْفٌ")]}]

# ----------- s12 — the prayer: cover our faults, secure our fears (qalb baʿd)
S.append({"id": "s12", "translation": {
 "en": "«O Allah, cover our FAULTS (ʿawrat) and make secure our FEARS (rawʿat)» — part of the letters reversed: qalb of a part.",
 "tr": "«Allah'ım, AYIPLARIMIZI (avrât) ört, KORKULARIMIZI (rav'ât) emniyete al» — harflerin bir kısmı ters: kısmın kalbi."},
 "tokens": [
  tok("اللَّهُمَّ","allah","noun",[Q, "idafa-definiteness"], "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ — الْمِيمُ الْمُشَدَّدَةُ عِوَضٌ عَنْ يَاءِ النِّدَاءِ.", "«O Allah» — the vocative; the doubled mim stands for «ya».", "«Allah'ım» — münâdâ; şeddeli mîm nidâ yâsı yerine."),
  tok("اسْتُرْ","satara","verb",[Q, "maful-bihi"], "فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«cover» — the command; its doer concealed.", "«ört» — emir; fâili gizli."),
  tok("عَوْرَاتِنَا","awra","noun",[Q, "maful-bihi", "idafa-definiteness", "jam-muannath-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ.", "«our faults» — the object, a sound plural.", "«ayıplarımızı» — mef'ul, cem-i müennes sâlim.",
      segments=[seg("عَوْرَاتِ","awra","noun"), seg("نَا","pron-1p","pron")]),
  tok("وَآمِنْ","amana-secure","verb",[Q, "atf-nasaq", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَآمِنْ فِعْلُ أَمْرٍ مِنْ آمَنَ: جَعَلَهُ آمِنًا.", "«and make secure» — the command of amana «to give safety».", "«ve emniyete al» — «emin kılmak» mânâsında emir.",
      segments=[seg("وَ","wa","conj"), seg("آمِنْ","amana-secure","verb")]),
  tok("رَوْعَاتِنَا","rawa-fright","noun",[Q, "maful-bihi", "idafa-definiteness", "jam-muannath-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ — جَمْعُ رَوْعَةٍ: الْفَزْعَةُ.", "«our fears» — the object: the frights.", "«korkularımızı» — mef'ul: ürkmeler.",
      segments=[seg("رَوْعَاتِ","rawa-fright","noun"), seg("نَا","pron-1p","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "qalb", "kind2": "bad", "pair": [ix(S[-1], "عَوْرَاتِنَا"), ix(S[-1], "رَوْعَاتِنَا")]}]

# ----------- s13 — the mujannah (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And when one of the two stands at the beginning of the bayt and the other at its end, it is called MAQLUB MUJANNAH — «winged»." + R_EN,
 "tr": "İkisinden biri beytin başında, öbürü sonunda olunca MAKLÛB-İ MÜCENNAH — «kanatlı» — denir." + R_TR},
 "tokens": [
  tok("وَإِذَا","idha","part",[Q, "idha-shartiyya", "maful-fih", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve -ince».",
      segments=[seg("وَ","wa","conj"), seg("إِذَا","idha","part")]),
  tok("وَقَعَ","waqaa","verb",[Q, "idha-shartiyya", "mithal-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«stands» — the shart verb.", "«bulunursa» — şart fiili."),
  tok("أَحَدُهُمَا","ahad","noun",[Q, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«one of the two» — the doer.", "«ikisinden biri» — fâil.",
      segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")]),
  fi(Q),
  tok("أَوَّلِ","awwal","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the beginning of».", "«başında»."),
  tok("الْبَيْتِ","bayt","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْبَيْتُ: بَيْتُ الشِّعْرِ.", "«the bayt» — the verse.", "«beyit»."),
  tok("وَالْآخَرُ","akhar","noun",[Q, "atf-nasaq", "mubtada-khabar"], "الْوَاوُ لِلْحَالِ، وَالْآخَرُ مُبْتَدَأٌ.", "«and the other» — the mubtada of a hal clause.", "«öbürü de» — hâl cümlesinin mübtedâsı.",
      segments=[seg("وَ","wa","conj"), seg("الْآخَرُ","akhar","noun")]),
  tok("فِي","fi","prep",[Q, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«at» — the khabar.", "«-de» — haber."),
  tok("آخِرِهِ","akhir","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end».", "«sonunda».",
      segments=[seg("آخِرِ","akhir","noun"), seg("هِ","pron-3ms","pron")]),
  summiya(Q),
  tok("مَقْلُوبًا","maqlub","noun",[Q, "mafulayn", "ism-maful"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«maqlub» — «reversed».", "«maklûb» — «ters çevrilmiş»."),
  tok("مُجَنَّحًا","mujannah","noun",[Q, "ism-maful"], "نَعْتٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ جَنَّحَ: ذُو جَنَاحَيْنِ.", "«mujannah» — the na't: «winged», one word at each wing of the bayt.", "«mücennah» — na't: «kanatlı», beytin iki kanadında birer kelime."),
 ]})

# ----------- s14 — the lights of guidance shone: لَاحَ … حَالٍ
S.append({"id": "s14", "translation": {
 "en": "«The lights of guidance SHONE (laha) from his palm in every STATE (hal)» — the bayt opens on لَاحَ and closes on حَالٍ: the mujannah.",
 "tr": "«Hidayet nurları avucundan her HÂLDE (hâl) PARLADI (lâha)» — beyit لَاحَ ile açılır, حَالٍ ile kapanır: mücennah."},
 "tokens": [
  tok("لَاحَ","laha-verb","verb",[Q, "hollow-verbs"], "فِعْلٌ مَاضٍ أَجْوَفُ.", "«shone» — a hollow verb.", "«parladı» — ecvef fiil."),
  tok("أَنْوَارُ","nur","noun",[Q, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ نُورٍ.", "«the lights of» — the doer, annexed.", "«nurları» — fâil, muzâf."),
  tok("الْهُدَى","huda","noun",[Q, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«guidance» — a maqsur.", "«hidayet» — maksûr."),
  tok("مِنْ","min","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("كَفِّهِ","kaff-hand","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his palm».", "«avucundan».",
      segments=[seg("كَفِّ","kaff-hand","noun"), seg("هِ","pron-3ms","pron")]),
  fi(Q),
  tok("كُلِّ","kull","noun",[Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«every».", "«her»."),
  tok("حَالٍ","hal","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«state».", "«hâlde»."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "qalb", "kind2": "mujannah", "pair": [ix(S[-1], "لَاحَ"), ix(S[-1], "حَالٍ")]}]

# ----------- s15 — the muzdawij (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "And whenever one of the two paired words FOLLOWS the other directly, it is called MUZDAWIJ, MUKARRAR and MURADDAD." + R_EN,
 "tr": "İki cinaslı kelimeden biri öbürünü hemen İZLERSE, MÜZDEVİC, MÜKERRER ve MÜREDDED denir." + R_TR},
 "tokens": [
  tok("وَمَتَى","mata","noun",[Q, "atf-nasaq", "maful-fih"], "الْوَاوُ عَاطِفَةٌ، وَمَتَى اسْمُ شَرْطٍ جَازِمٌ ظَرْفُ زَمَانٍ.", "«and whenever» — the conditional noun of time.", "«ve ne zaman» — cezm eden şart ismi, zaman zarfı.",
      segments=[seg("وَ","wa","conj"), seg("مَتَى","mata","noun")]),
  tok("وَلِيَ","waliya","verb",[Q, "mithal-verbs", "in-shartiyya", "maful-bihi"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ؛ وَلِيَ الشَّيْءُ الشَّيْءَ: تَبِعَهُ بِلَا فَاصِلٍ.", "«follows directly» — the shart verb: comes right after.", "«hemen izlerse» — şart fiili: arasız gelir."),
  tok("أَحَدُ","ahad","noun",[Q, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«one of» — the doer, annexed.", "«biri» — fâil, muzâf."),
  tok("الْمُتَجَانِسَيْنِ","mutajanis","noun",[Q, "idafa-definiteness", "al-muthanna", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى، اسْمُ فَاعِلٍ مِنْ تَجَانَسَ.", "«the two paired words» — the dual participle: the two in jinas.", "«iki cinaslı kelimenin» — tesniye ism-i fâil."),
  tok("الْآخَرَ","akhar","noun",[Q, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the other» — the object.", "«öbürünü» — mef'ul."),
  summiya(Q),
  tok("مُزْدَوِجًا","muzdawij","noun",[Q, "mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنِ ازْدَوَجَ: صَارَ زَوْجًا.", "«muzdawij» — «paired».", "«müzdevic» — «çift olmuş»."),
  tok("وَمُكَرَّرًا","mukarrar","noun",[Q, "atf-nasaq", "ism-maful"], "الْوَاوُ عَاطِفَةٌ، وَمُكَرَّرًا مَعْطُوفٌ مَنْصُوبٌ.", "«and mukarrar» — «repeated».", "«ve mükerrer» — «tekrarlanmış».",
      segments=[seg("وَ","wa","conj"), seg("مُكَرَّرًا","mukarrar","noun")]),
  tok("وَمُرَدَّدًا","muraddad","noun",[Q, "atf-nasaq", "ism-maful"], "الْوَاوُ عَاطِفَةٌ، وَمُرَدَّدًا مَعْطُوفٌ مَنْصُوبٌ.", "«and muraddad» — «echoed».", "«ve müredded» — «yankılanmış».",
      segments=[seg("وَ","wa","conj"), seg("مُرَدَّدًا","muraddad","noun")]),
 ]})

# ----------- s16 — 27:22: from Saba with sure news
S.append({"id": "s16", "translation": {
 "en": "«And I have come to you from SABA (saba') with sure NEWS (naba')» (27:22, as the source prints it) — the two words side by side: muzdawij.",
 "tr": "«Sana SEBE'DEN (sebe') kesin bir HABERLE (nebe') geldim» (Neml 22, kaynağın bastığı gibi) — iki kelime yan yana: müzdevic."},
 "tokens": [
  tok("وَجِئْتُكَ","jaa","verb",[Q, "hollow-verbs", "fail", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَجِئْتُ فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«and I have come to you» — the ta is the doer, the kaf the object.", "«ve sana geldim» — tâ fâil, kâf mef'ul.",
      segments=[seg("وَ","wa","conj"), seg("جِئْتُ","jaa","verb"), seg("كَ","pron-2ms","pron")]),
  tok("مِنْ","min","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("سَبَأٍ","saba","noun",[Q, "huruf-jarr"], "مَجْرُورٌ مُنَوَّنٌ — سَبَأٌ: قَبِيلَةٌ وَبَلَدٌ بِالْيَمَنِ؛ مَصْرُوفٌ عَلَى قِرَاءَةٍ.", "«Saba» — the tribe and land in Yemen; declined with tanwin in this reading.", "«Sebe'» — Yemen'de kabile ve belde; bu kıraatte tenvinli."),
  tok("بِنَبَأٍ","naba-news","noun",[Q, "huruf-jarr", "hal"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَبَأٍ مَجْرُورٌ — حَالٌ.", "«with news» — a hal.", "«bir haberle» — hâl.",
      segments=[seg("بِ","bi","prep"), seg("نَبَأٍ","naba-news","noun")]),
  tok("يَقِينٍ","yaqin","noun",[Q, "huruf-jarr"], "نَعْتٌ مَجْرُورٌ.", "«sure» — the na't.", "«kesin» — na't."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "lahiq", "kind2": "muzdawij", "pair": [ix(S[-1], "سَبَأٍ"), ix(S[-1], "بِنَبَأٍ")]}]

# ----------- s17 — the first mulhaq: ishtiqaq (RESTORED)
S.append({"id": "s17", "translation": {
 "en": "Two things are ATTACHED to the jinas: the first is that DERIVATION (ishtiqaq) gathers the two words." + R_EN,
 "tr": "Cinâsa iki şey İLHAK edilir: birincisi, iki lafzı İŞTİKÂKIN bir araya getirmesidir." + R_TR},
 "tokens": [
  tok("وَيُلْحَقُ","alhaqa","verb",[L, "naib-al-fail", "mudari-marfu"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيُلْحَقُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and there is attached» — the passive.", "«ve ilhak edilir» — meçhul.",
      segments=[seg("وَ","wa","conj"), seg("يُلْحَقُ","alhaqa","verb")]),
  tok("بِالْجِنَاسِ","jinas","noun",[L, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْجِنَاسِ مَجْرُورٌ.", "«to the jinas».", "«cinâsa».",
      segments=[seg("بِ","bi","prep"), seg("الْجِنَاسِ","jinas","noun")]),
  tok("شَيْئَانِ","shay","noun",[L, "naib-al-fail", "al-muthanna"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«two things» — the deputy, a dual.", "«iki şey» — nâib, tesniye.", punct=":"),
  tok("أَحَدُهُمَا","ahad","noun",[L, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«the first of them» — the mubtada.", "«birincisi» — mübtedâ.",
      segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")]),
  tok("أَنْ","an-masdariyya","part",[L, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("يَجْمَعَ","jamaa","verb",[L, "an-masdariyya", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ.", "«gathers» — mansub by an.", "«bir araya getirsin» — en ile mansûb."),
  tok("اللَّفْظَيْنِ","lafz","noun",[L, "maful-bihi", "al-muthanna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ — مُثَنًّى، مُقَدَّمٌ عَلَى الْفَاعِلِ.", "«the two words» — the object, before the doer.", "«iki lafzı» — mef'ul, fâilden önce."),
  tok("الِاشْتِقَاقُ","ishtiqaq","noun",[L, "fail"], "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ — الِاشْتِقَاقُ: رُجُوعُ الْكَلِمَتَيْنِ إِلَى أَصْلٍ وَاحِدٍ.", "«derivation» — the delayed doer: the two go back to one root.", "«iştikak» — sona bırakılmış fâil: ikisi bir köke döner."),
 ]})

# ----------- s18 — 30:43: set your face to the upright religion
S.append({"id": "s18", "translation": {
 "en": "«So SET (aqim) your face toward the UPRIGHT (al-qayyim) religion» (30:43) — one root, ق و م: the ishtiqaq attached to the jinas.",
 "tr": "«Yüzünü DOSDOĞRU (kayyim) dine ÇEVİR (ekım)» (Rûm 43) — tek kök, ق و م: cinâsa ilhak edilen iştikak."},
 "tokens": [
  tok("فَأَقِمْ","aqama","verb",[L, "hollow-verbs", "maful-bihi"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَأَقِمْ فِعْلُ أَمْرٍ أَجْوَفُ — حُذِفَتْ عَيْنُهُ لِلسَّاكِنَيْنِ.", "«so set» — the hollow command with its middle letter dropped.", "«çevir» — ecvef emir; ayn harfi düşmüş.",
      segments=[seg("فَ","fa","conj"), seg("أَقِمْ","aqama","verb")]),
  tok("وَجْهَكَ","wajh","noun",[L, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your face» — the object.", "«yüzünü» — mef'ul.",
      segments=[seg("وَجْهَ","wajh","noun"), seg("كَ","pron-2ms","pron")]),
  tok("لِلدِّينِ","din","noun",[L, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالدِّينِ مَجْرُورٌ.", "«toward the religion».", "«dine».",
      segments=[seg("لِ","li","prep"), seg("الدِّينِ","din","noun")]),
  tok("الْقَيِّمِ","qayyim","noun",[L, "huruf-jarr"], "نَعْتٌ مَجْرُورٌ — الْقَيِّمُ: الْمُسْتَقِيمُ.", "«the upright» — the na't.", "«dosdoğru» — na't."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "ishtiqaq", "pair": [ix(S[-1], "فَأَقِمْ"), ix(S[-1], "الْقَيِّمِ")]}]

# ----------- s19 — the second mulhaq: shibh ishtiqaq (RESTORED)
S.append({"id": "s19", "translation": {
 "en": "The second is that RESEMBLANCE gathers them — that which looks like derivation." + R_EN,
 "tr": "İkincisi, onları BENZEŞMENİN bir araya getirmesidir — iştikâka benzeyen." + R_TR},
 "tokens": [
  tok("وَالثَّانِي","thani","noun",[L, "mubtada-khabar", "atf-nasaq", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«and the second» — the mubtada, a manqus.", "«ikincisi» — mübtedâ, manqûs.",
      segments=[seg("وَ","wa","conj"), seg("الثَّانِي","thani","noun")]),
  tok("أَنْ","an-masdariyya","part",[L, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("يَجْمَعَهُمَا","jamaa","verb",[L, "an-masdariyya", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", "«gathers them».", "«onları bir araya getirsin».",
      segments=[seg("يَجْمَعَ","jamaa","verb"), seg("هُمَا","pron-3d","pron")]),
  tok("الْمُشَابَهَةُ","mushabaha","noun",[L, "fail"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ شَابَهَ.", "«resemblance» — the doer.", "«benzeşme» — fâil.", punct="،"),
  tok("وَهِيَ","hiya","pron",[L, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«o da» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("مَا","ma-mawsula","pron",[L, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the khabar.", "«şey» — haber."),
  tok("يُشْبِهُ","ashbaha","verb",[L, "ism-mawsul", "maful-bihi", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«looks like» — the sila.", "«benzer» — sıla."),
  tok("الِاشْتِقَاقَ","ishtiqaq","noun",[L, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«derivation» — the object.", "«iştikâka» — mef'ul."),
 ]})

# ----------- s20 — 26:168: «I am of those who detest»
S.append({"id": "s20", "translation": {
 "en": "«He SAID (qala): I am, of your deed, among those who DETEST (al-qalin)» (26:168) — قَالَ and الْقَالِينَ look alike but their roots differ: shibh ishtiqaq.",
 "tr": "«DEDİ (kâle): Ben sizin işinizden NEFRET EDENLERDENİM (el-kâlîn)» (Şuarâ 168) — قَالَ ile الْقَالِينَ benzeşir, kökleri ayrıdır: şibh-i iştikak."},
 "tokens": [
  tok("قَالَ","qala","verb",[L, "hollow-verbs"], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (لُوطٌ عَلَيْهِ السَّلَامُ).", "«he said» — Lut, peace be upon him.", "«dedi» — Lût aleyhisselâm."),
  tok("إِنِّي","inna","part",[L, "inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ نَاسِخٌ، وَالْيَاءُ اسْمُهَا — خُفِّفَتِ النُّونُ.", "«I am» — inna with the speaker's ya.", "«ben» — inne ve mütekellim yâsı.",
      segments=[seg("إِنَّ","inna","part"), seg("ي","pron-1s","pron")]),
  tok("لِعَمَلِكُمْ","amal-work","noun",[L, "huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَعَمَلِكُمْ مَجْرُورٌ مُضَافٌ — مُتَعَلِّقٌ بِالْقَالِينَ.", "«of your deed» — hangs on «those who detest».", "«işinizden» — «nefret edenler»e bağlı.",
      segments=[seg("لِ","li","prep"), seg("عَمَلِ","amal-work","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("مِنَ","min","part",[L, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«among» — the jarr phrase is inna's khabar.", "«-den» — câr-mecrûr innenin haberi."),
  tok("الْقَالِينَ","qalin","noun",[L, "huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ، اسْمُ فَاعِلٍ مِنْ قَلَى: أَبْغَضَ.", "«those who detest» — the sound plural of qalin, from qala «to hate» — not from qala «to say».", "«nefret edenler» — kalâ «buğzetmek»ten ism-i fâil; kâle «demek»ten değil."),
 ]})
S[-1]["badi"] = [{"kind": "jinas", "sub": "ishtiqaq", "kind2": "shibh-ishtiqaq", "pair": [ix(S[-1], "قَالَ"), ix(S[-1], "الْقَالِينَ")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "ikhtilaf": need("ikhtilaf", "اِخْتِلَاف", "خ ل ف", "noun", "difference, disagreement (masdar of اِخْتَلَفَ)", "ihtilaf, ayrılık (اِخْتَلَفَ'nin masdarı)", 3),
 "mutaqarib": need("mutaqarib", "مُتَقَارِب", "ق ر ب", "noun", "near to one another (ism fa'il of تَقَارَبَ)", "birbirine yakın (تَقَارَبَ'nin ism-i fâili)", 4),
 "makhraj-harf": need("makhraj-harf", "مَخْرَج", "خ ر ج", "noun", "the point of articulation — where a letter comes out of the mouth", "mahreç — harfin ağızdan çıktığı yer", 4),
 "mudari-jinas": need("mudari-jinas", "مُضَارِع", "ض ر ع", "noun", "resembling (ism fa'il of ضَارَعَ); the jinas whose differing letters are near in makhraj", "benzeşen (ضَارَعَ'nin ism-i fâili); ayrı harfleri mahreçte yakın cinas", 5),
 "kinn": need("kinn", "كِنّ", "ك ن ن", "noun", "a shelter, a cover one takes", "sığınak, siper", 4),
 "damis": need("damis", "دَامِس", "د م س", "noun", "pitch-dark (of a night)", "zifirî (gece)", 5),
 "tamis": need("tamis", "طَامِس", "ط م س", "noun", "effaced, its track wiped out (of a road)", "silinmiş, izi kaybolmuş (yol)", 5),
 "hum": need("hum", "هُمْ", None, "pron", "they (masc. pl., detached)", "onlar (müzekker çoğul, munfasıl)", 1),
 "naa": need("naa", "نَأَى", "ن ء ي", "verb", "to keep far, to be distant (نَأَى يَنْأَى — a hamzated naqis verb)", "uzaklaşmak, uzak olmak (نَأَى يَنْأَى — hemzeli nâkıs fiil)", 4),
 "maqud": need("maqud", "مَعْقُود", "ع ق د", "noun", "knotted, tied (ism maf'ul of عَقَدَ)", "bağlanmış, düğümlenmiş (عَقَدَ'nin ism-i mef'ûlü)", 4),
 "nasiya-forelock": need("nasiya-forelock", "نَاصِيَة", "ن ص و", "noun", "forelock", "alın, perçem", 4, plural="نَوَاصٍ"),
 "lahiq": need("lahiq", "لَاحِق", "ل ح ق", "noun", "attached, joined on (ism fa'il of لَحِقَ); the jinas whose differing letters are far in makhraj", "bitişik, katılan (لَحِقَ'nin ism-i fâili); ayrı harfleri mahreçte uzak cinas", 5),
 "wayl": need("wayl", "وَيْل", "و ي ل", "noun", "woe, ruin (a word of cursing)", "vay, helâk (beddua kelimesi)", 3),
 "humaza": need("humaza", "هُمَزَة", "ه م ز", "noun", "backbiter — who jabs at people (an intensive on فُعَلَة)", "ayıplayan, yeren (فُعَلَة vezninde mübalağa)", 5),
 "lumaza": need("lumaza", "لُمَزَة", "ل م ز", "noun", "slanderer — who faults with a gesture (an intensive on فُعَلَة)", "çekiştiren, işaretle kusur bulan (فُعَلَة vezninde mübalağa)", 5),
 "dhalikum": need("dhalikum", "ذَلِكُمْ", None, "pron", "that (the far demonstrative, addressed to a plural)", "o, bu (çoğul muhataba uzak işaret)", 3),
 "fariha": need("fariha", "فَرِحَ", "ف ر ح", "verb", "to rejoice, to exult (فَرِحَ يَفْرَحُ)", "sevinmek, şımarmak (فَرِحَ يَفْرَحُ)", 2),
 "mariha": need("mariha", "مَرِحَ", "م ر ح", "verb", "to exult past measure, to be insolent (مَرِحَ يَمْرَحُ)", "ölçüsüz sevinmek, taşkınlık etmek (مَرِحَ يَمْرَحُ)", 4),
 "amn": need("amn", "أَمْن", "ء م ن", "noun", "safety, security — the opposite of fear", "emniyet, güvenlik — korkunun zıddı", 3),
 "tajnis": need("tajnis", "تَجْنِيس", "ج ن س", "noun", "tajnis — the jinas (masdar of جَنَّسَ)", "tecnîs — cinas (جَنَّسَ'nin masdarı)", 5),
 "qalb-reversal": need("qalb-reversal", "قَلْب", "ق ل ب", "noun", "reversal, turning round (masdar of قَلَبَ); the jinas whose letters come in reverse order", "kalb, tersine çevirme (قَلَبَ'nin masdarı); harfleri ters sırada gelen cinas", 4),
 "husam": need("husam", "حُسَام", "ح س م", "noun", "a sharp sword", "keskin kılıç", 4),
 "fath": need("fath", "فَتْح", "ف ت ح", "noun", "victory, conquest; opening (masdar of فَتَحَ)", "fetih, zafer; açma (فَتَحَ'nin masdarı)", 2),
 "satara": need("satara", "سَتَرَ", "س ت ر", "verb", "to cover, to veil (سَتَرَ يَسْتُرُ)", "örtmek, gizlemek (سَتَرَ يَسْتُرُ)", 3),
 "awra": need("awra", "عَوْرَة", "ع و ر", "noun", "a fault, a weak spot; what must be covered", "ayıp, açık; örtülmesi gereken", 3, plural="عَوْرَات"),
 "amana-secure": need("amana-secure", "آمَنَ", "ء م ن", "verb", "to make secure, to give safety (Form IV: آمَنَ يُؤْمِنُ; آمِنْ رَوْعَاتِنَا: secure our fears)", "emin kılmak, güven vermek (IV. bâb: آمَنَ يُؤْمِنُ; آمِنْ رَوْعَاتِنَا: korkularımızı emniyete al)", 4, form="IV"),
 "rawa-fright": need("rawa-fright", "رَوْعَة", "ر و ع", "noun", "a fright, a start of fear", "ürküntü, korku", 4, plural="رَوْعَات"),
 "bayt": need("bayt", "بَيْت", "ب ي ت", "noun", "a house; a verse of poetry (bayt)", "ev; beyit", 1),
 "mujannah": need("mujannah", "مُجَنَّح", "ج ن ح", "noun", "winged (ism maf'ul of جَنَّحَ); the maqlub whose two words stand at the two wings of the bayt", "kanatlı (جَنَّحَ'nin ism-i mef'ûlü); iki kelimesi beytin iki kanadında duran maklûb", 5),
 "mutajanis": need("mutajanis", "مُتَجَانِس", "ج ن س", "noun", "of one kind, in jinas with another (ism fa'il of تَجَانَسَ)", "aynı cinsten, cinaslı (تَجَانَسَ'nin ism-i fâili)", 5),
 "muzdawij": need("muzdawij", "مُزْدَوِج", "ز و ج", "noun", "paired, doubled (ism fa'il of اِزْدَوَجَ); the jinas whose two words stand side by side", "çift, müzdevic (اِزْدَوَجَ'nin ism-i fâili); iki kelimesi yan yana duran cinas", 5),
 "mukarrar": need("mukarrar", "مُكَرَّر", "ك ر ر", "noun", "repeated (ism maf'ul of كَرَّرَ)", "mükerrer, tekrarlanmış (كَرَّرَ'nin ism-i mef'ûlü)", 3),
 "muraddad": need("muraddad", "مُرَدَّد", "ر د د", "noun", "echoed, repeated back (ism maf'ul of رَدَّدَ)", "müredded, yankılanmış (رَدَّدَ'nin ism-i mef'ûlü)", 4),
 "saba": need("saba", "سَبَأ", None, "noun", "Saba — the tribe and land in Yemen (27:22)", "Sebe' — Yemen'de kabile ve belde (Neml 22)", 4),
 "naba-news": need("naba-news", "نَبَأ", "ن ب ء", "noun", "news, tidings", "haber", 3),
 "yaqin": need("yaqin", "يَقِين", "ي ق ن", "noun", "certainty; sure", "yakîn, kesinlik; kesin", 3),
 "shay": need("shay", "شَيْء", "ش ي ء", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "jamaa": need("jamaa", "جَمَعَ", "ج م ع", "verb", "to gather, to bring together (جَمَعَ يَجْمَعُ)", "toplamak, bir araya getirmek (جَمَعَ يَجْمَعُ)", 2),
 "ishtiqaq": need("ishtiqaq", "اِشْتِقَاق", "ش ق ق", "noun", "derivation — two words going back to one root (masdar of اِشْتَقَّ)", "iştikak — iki kelimenin bir köke dönmesi (اِشْتَقَّ'nin masdarı)", 4),
 "qayyim": need("qayyim", "قَيِّم", "ق و م", "noun", "upright, straight (of the religion, 30:43)", "dosdoğru (din için, Rûm 43)", 4),
 "thani": need("thani", "ثَانٍ", "ث ن ي", "noun", "second (a manqus)", "ikinci (manqûs)", 1),
 "amal-work": need("amal-work", "عَمَل", "ع م ل", "noun", "a deed, work (masdar of عَمِلَ)", "amel, iş (عَمِلَ'nin masdarı)", 2, plural="أَعْمَال"),
 "qalin": need("qalin", "قَالٍ", "ق ل ي", "noun", "one who detests (ism fa'il of قَلَى «to hate» — a manqus; الْقَالِينَ 26:168)", "nefret eden (قَلَى «buğzetmek»in ism-i fâili — manqûs; الْقَالِينَ Şuarâ 168)", 5),
}
for k in ("ikhtalafa", "naw", "harf", "ishtarata", "an-masdariyya", "la-nafiya", "waqaa", "akthar", "min", "thumma", "in-shartiyya", "kana", "samma", "huwa", "imma", "fi", "awwal",
          "wasat", "akhir", "aw", "bayna", "layl", "tariq", "naha", "an", "khayl", "khayr", "ila", "yawm", "qiyama", "illa", "dhalika", "kull", "ma-masdariyya", "ard", "ghayr", "haqq",
          "idha", "jaa", "amr", "tartib", "wali", "hatf", "aduww", "allah", "laha-verb", "nur", "huda", "kaff-hand", "hal", "mata", "waliya", "ahad", "akhar", "maqlub", "alhaqa",
          "jinas", "lafz", "aqama", "wajh", "din", "mushabaha", "hiya", "ma-mawsula", "ashbaha", "qala", "inna", "wa", "fa", "bi", "li", "ka", "pron-1s", "pron-3ms", "pron-3mp", "pron-3fs",
          "pron-3d", "pron-1p", "pron-2ms", "pron-2mp"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "naa", _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ مَهْمُوزُ الْعَيْنِ", "y", "نَأَ", "نْأ", "a", "اِنْأ", "نَأْي", "نَاءٍ (النَّائِي)", None, None, None,
                                 note="نَأَى يَنْأَى نَأْيًا: بَعُدَ — مَهْمُوزُ الْعَيْنِ نَاقِصٌ مِنْ بَابِ فَتَحَ؛ لَازِمٌ."))
put_morph(mo, "fariha", _sg.sound1("samia", "فَرِح", "فْرَح", "اِفْرَح", "فَرَح", "فَرِح", note="لَازِمٌ مِنْ بَابِ سَمِعَ: فَرِحَ يَفْرَحُ فَرَحًا."))
put_morph(mo, "mariha", _sg.sound1("samia", "مَرِح", "مْرَح", "اِمْرَح", "مَرَح", "مَرِح", note="لَازِمٌ مِنْ بَابِ سَمِعَ: مَرِحَ يَمْرَحُ مَرَحًا."))
put_morph(mo, "satara", _sg.sound1("nasara", "سَتَر", "سْتُر", "اُسْتُر", "سَتْر", "سَاتِر", "مَسْتُور", "سُتِرَ", "يُسْتَرُ"))
put_morph(mo, "jamaa", _sg.sound1("fataha", "جَمَع", "جْمَع", "اِجْمَع", "جَمْع", "جَامِع", "مَجْمُوع", "جُمِعَ", "يُجْمَعُ"))
if "amana" in mo["verbs"] and "amana-secure" not in mo["verbs"]:
    mo["verbs"]["amana-secure"] = dict(mo["verbs"]["amana"]); mo["verbs"]["amana-secure"]["note"] = "آمَنَ يُؤْمِنُ إِيمَانًا: جَعَلَهُ آمِنًا — وَبِالْبَاءِ: صَدَّقَ؛ الصَّرْفُ وَاحِدٌ."
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_M = {
 "id": "jinas-mudari-lahiq",
 "title": {"ar": "الْجِنَاسُ الْمُضَارِعُ وَاللَّاحِقُ — حَرْفٌ مِنْ نَوْعٍ آخَرَ، قَرِيبٌ أَوْ بَعِيدٌ فِي الْمَخْرَجِ", "en": "The mudariʿ and the lahiq — one letter of another kind, near or far in makhraj", "tr": "Muzâri ve lâhik cinas — başka nevden bir harf, mahreçte yakın yahut uzak"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — وإن اختلفا في أنواعها فيشترط أن لا يقع الاختلاف بأكثر من حرف، ثم إن كانا متقاربين سمي مضارعا، وهو إما في الأول كقولهم: بيني وبين كني ليل دامس وطريق طامس، أو في الوسط نحو: وهم ينهون عنه وينأون عنه، أو في الآخر نحو: الخيل معقود بنواصيها الخير؛ وإلا سمي لاحقا: وهو إما في الأول نحو: ويل لكل همزة لمزة، أو في الوسط نحو: وبما كنتم تفرحون في الأرض بغير الحق وبما كنتم تمرحون، أو في الآخر نحو: وإذا جاءهم أمر من الأمن."],
 "question": {
  "en": ["Do the two words share every letter but ONE, and is that one of ANOTHER KIND? Then the jinas is by kind, and the Talkhis asks two things: not MORE than one letter may differ, and WHERE the two letters are made in the mouth. Near in MAKHRAJ — the dal and the ta of دَامِسٌ / طَامِسٌ, the ha and the hamza of يَنْهَوْنَ / يَنْأَوْنَ, the lam and the ra of الْخَيْلُ / الْخَيْرُ — and the jinas is MUDARIʿ: the two words almost one sound.",
         "Far in makhraj — the ha and the lam of هُمَزَةٍ / لُمَزَةٍ, the fa and the mim of تَفْرَحُونَ / تَمْرَحُونَ, the ra and the nun of أَمْرٌ / الْأَمْنِ — and it is LAHIQ: the two words merely joined. Each kind is placed by the letter's seat: first, middle, last.",
         "What does the engine read? The alignment finds the one differing letter and its place; a stored makhraj table (the throat, the tongue's back, its middle, its edge, its tip, the lips) says whether the two letters are neighbours — mudariʿ — or strangers — lahiq. Two differing letters are no jinas of this kind at all."],
  "tr": ["İki kelime BİR harf dışında her harfi paylaşıyor ve o bir harf BAŞKA NEVDEN mi? Cinas nevce'dir; Telhîs iki şey ister: birden FAZLA harf ayrılmasın, ve iki harf ağızda NEREDE çıkıyor. MAHREÇTE yakın — دَامِسٌ / طَامِسٌ'in dâl ve tâsı, يَنْهَوْنَ / يَنْأَوْنَ'nin hâ ve hemzesi, الْخَيْلُ / الْخَيْرُ'nun lâm ve râsı — cinas MUZÂRİ'dir: iki kelime neredeyse tek ses.",
         "Mahreçte uzak — هُمَزَةٍ / لُمَزَةٍ'in hâ ve lâmı, تَفْرَحُونَ / تَمْرَحُونَ'nin fâ ve mîmi, أَمْرٌ / الْأَمْنِ'in râ ve nûnu — LÂHİK'tir: iki kelime yalnız bitişik. Her kısım harfin yerine göre: baş, orta, son.",
         "Motor neyi okur? Hizalama ayrılan tek harfi ve yerini bulur; saklı bir mahreç tablosu (boğaz, dil arkası, ortası, kenarı, ucu, dudaklar) iki harfin komşu — muzâri — yahut yabancı — lâhik — olduğunu söyler. İki ayrı harf bu kısımdan cinas değildir."]},
 "plain": {
  "en": "One letter of another kind. Near in makhraj: mudariʿ (دَامِسٌ / طَامِسٌ, يَنْهَوْنَ / يَنْأَوْنَ, الْخَيْلُ / الْخَيْرُ). Far: lahiq (هُمَزَةٍ / لُمَزَةٍ, تَفْرَحُونَ / تَمْرَحُونَ, أَمْرٌ / الْأَمْنِ). Never more than one letter.",
  "tr": "Başka nevden bir harf. Mahreçte yakın: muzâri (دَامِسٌ / طَامِسٌ, يَنْهَوْنَ / يَنْأَوْنَ, الْخَيْلُ / الْخَيْرُ). Uzak: lâhik (هُمَزَةٍ / لُمَزَةٍ, تَفْرَحُونَ / تَمْرَحُونَ, أَمْرٌ / الْأَمْنِ). Asla birden fazla harf değil."},
 "explanation": {
  "en": "وَإِنِ اخْتَلَفَا فِي أَنْوَاعِ الْحُرُوفِ فَيُشْتَرَطُ أَلَّا يَقَعَ الِاخْتِلَافُ بِأَكْثَرَ مِنْ حَرْفٍ. When the two letters are مُتَقَارِبَيْنِ فِي الْمَخْرَجِ the jinas is MUDARIʿ, otherwise LAHIQ; each is placed فِي الْأَوَّلِ أَوِ الْوَسَطِ أَوِ الْآخِرِ. The examples are the book's: the saying of the lost traveller, 6:26, the hadith of the horses; 104:1, 40:75, 4:83.",
  "tr": "وَإِنِ اخْتَلَفَا فِي أَنْوَاعِ الْحُرُوفِ فَيُشْتَرَطُ أَلَّا يَقَعَ الِاخْتِلَافُ بِأَكْثَرَ مِنْ حَرْفٍ. İki harf مُتَقَارِبَيْنِ فِي الْمَخْرَجِ ise cinas MUZÂRİ, değilse LÂHİK'tir; her biri فِي الْأَوَّلِ أَوِ الْوَسَطِ أَوِ الْآخِرِ. Örnekler kitabındır: yolunu yitirenin sözü, En'âm 26, atlar hadisi; Hümeze 1, Mü'min 75, Nisâ 83."},
 "examples": [
  {"ar": "بَيْنِي وَبَيْنَ كِنِّي لَيْلٌ دَامِسٌ وَطَرِيقٌ طَامِسٌ", "en": "mudariʿ, first.", "tr": "muzâri, başta.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "وَهُمْ يَنْهَوْنَ عَنْهُ وَيَنْأَوْنَ عَنْهُ", "en": "6:26 — mudariʿ, middle.", "tr": "En'âm 26 — muzâri, ortada.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "وَيْلٌ لِكُلِّ هُمَزَةٍ لُمَزَةٍ", "en": "104:1 — lahiq, first.", "tr": "Hümeze 1 — lâhik, başta.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "فَإِذَا جَاءَهُمْ أَمْرٌ مِنَ الْأَمْنِ", "en": "4:83 — lahiq, last.", "tr": "Nisâ 83 — lâhik, sonda.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«الْخَيْلُ / الْخَيْرُ lâhiktir: lâm ile râ ayrı harflerdir»",
   "right": "«Muzâridir: lâm ile râ mahreçte komşudur (dil ucu); uzak olsaydı lâhik olurdu»",
   "why": {"en": "The name turns on the makhraj, not on the mere difference.", "tr": "Ad, yalnız farka değil mahrece bağlıdır."}}],
 "relatedNotes": ["jinas", "jinas-tamm", "jinas-naqis", "jinas-qalb", "ilm-al-badi"]}

NOTE_Q = {
 "id": "jinas-qalb",
 "title": {"ar": "تَجْنِيسُ الْقَلْبِ — قَلْبُ الْكُلِّ، وَقَلْبُ الْبَعْضِ، وَالْمَقْلُوبُ الْمُجَنَّحُ؛ وَالْمُزْدَوِجُ", "en": "The jinas of qalb — the whole reversed, a part reversed, the winged maqlub; and the muzdawij", "tr": "Kalb cinâsı — bütünün kalbi, kısmın kalbi, kanatlı maklûb; ve müzdevic"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — وإن اختلفا في الترتيب سمي تجنيس القلب: حسامه فتح لأوليائه وحتف لأعدائه — قلب كل؛ اللهم استر عوراتنا وآمن روعاتنا — قلب بعض. وإذا وقع أحدهما في أول البيت والآخر في آخره سمي مقلوبا مجنحا: لاح أنوار الهدى من كفه في كل حال. ومتى ولي أحد المتجانسين الآخر سمي مزدوجا ومكررا ومرددا: وجئتك من سبإ بنبإ يقين."],
 "question": {
  "en": ["Are the letters the SAME but their ORDER turned? The jinas of QALB. The WHOLE word read backwards — فَتْحٌ becomes حَتْفٌ: victory for his friends, doom for his foes. A PART of it turned — عَوْرَاتِنَا / رَوْعَاتِنَا in the prayer «cover our faults, secure our fears». When the two words stand at the two ENDS of the bayt, the maqlub is MUJANNAH, winged: لَاحَ opens and حَالٍ closes.",
         "And whenever the two words in jinas follow one another DIRECTLY, the jinas is MUZDAWIJ — paired, repeated, echoed: سَبَأٍ بِنَبَأٍ in 27:22.",
         "What does the engine read? The letters of the two words compared as sets and as sequences: the same letters in reverse order is the qalb of the whole, a reversal inside a shared frame is the qalb of a part; the first and last words of a line give the mujannah; two paired words at neighbouring seats give the muzdawij flag."],
  "tr": ["Harfler AYNI, TERTİBİ mi dönmüş? KALB cinâsı. Kelimenin BÜTÜNÜ tersten — فَتْحٌ, حَتْفٌ olur: dostlara fetih, düşmanlara ölüm. Bir KISMI dönmüş — «ayıplarımızı ört, korkularımızı emniyete al» duasında عَوْرَاتِنَا / رَوْعَاتِنَا. İki kelime beytin iki UCUNDA durunca maklûb MÜCENNAH'tır, kanatlı: لَاحَ açar, حَالٍ kapar.",
         "Cinaslı iki kelime birbirini HEMEN izleyince cinas MÜZDEVİC'tir — çift, tekrar, yankı: Neml 22'de سَبَأٍ بِنَبَأٍ.",
         "Motor neyi okur? İki kelimenin harfleri küme ve sıra olarak karşılaştırılır: aynı harfler ters sırada bütünün kalbi, ortak çerçeve içinde bir dönüş kısmın kalbi; satırın ilk ve son kelimesi mücennahı, komşu iki cinaslı kelime müzdevic işaretini verir."]},
 "plain": {
  "en": "Qalb: same letters, reversed order — whole (فَتْحٌ / حَتْفٌ) or part (عَوْرَاتِنَا / رَوْعَاتِنَا); at the two ends of the bayt: mujannah (لَاحَ … حَالٍ). Muzdawij: the two words side by side (سَبَأٍ بِنَبَأٍ).",
  "tr": "Kalb: aynı harfler, ters sıra — bütün (فَتْحٌ / حَتْفٌ) yahut kısım (عَوْرَاتِنَا / رَوْعَاتِنَا); beytin iki ucunda: mücennah (لَاحَ … حَالٍ). Müzdevic: iki kelime yan yana (سَبَأٍ بِنَبَأٍ)."},
 "explanation": {
  "en": "وَإِنِ اخْتَلَفَا فِي التَّرْتِيبِ سُمِّيَ تَجْنِيسَ الْقَلْبِ — of the whole (قَلْبُ كُلٍّ) or of a part (قَلْبُ بَعْضٍ). وَإِذَا وَقَعَ أَحَدُهُمَا فِي أَوَّلِ الْبَيْتِ وَالْآخَرُ فِي آخِرِهِ سُمِّيَ مَقْلُوبًا مُجَنَّحًا. وَمَتَى وَلِيَ أَحَدُ الْمُتَجَانِسَيْنِ الْآخَرَ سُمِّيَ مُزْدَوِجًا وَمُكَرَّرًا وَمُرَدَّدًا — the muzdawij is not a kind of its own but a placing that any jinas may take.",
  "tr": "وَإِنِ اخْتَلَفَا فِي التَّرْتِيبِ سُمِّيَ تَجْنِيسَ الْقَلْبِ — bütünün (قَلْبُ كُلٍّ) yahut kısmın (قَلْبُ بَعْضٍ). وَإِذَا وَقَعَ أَحَدُهُمَا فِي أَوَّلِ الْبَيْتِ وَالْآخَرُ فِي آخِرِهِ سُمِّيَ مَقْلُوبًا مُجَنَّحًا. وَمَتَى وَلِيَ أَحَدُ الْمُتَجَانِسَيْنِ الْآخَرَ سُمِّيَ مُزْدَوِجًا وَمُكَرَّرًا وَمُرَدَّدًا — müzdevic başlı başına bir kısım değil, her cinasın alabileceği bir yerleşimdir."},
 "examples": [
  {"ar": "حُسَامُهُ فَتْحٌ لِأَوْلِيَائِهِ وَحَتْفٌ لِأَعْدَائِهِ", "en": "qalb of the whole.", "tr": "bütünün kalbi.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "اللَّهُمَّ اسْتُرْ عَوْرَاتِنَا وَآمِنْ رَوْعَاتِنَا", "en": "qalb of a part.", "tr": "kısmın kalbi.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "لَاحَ أَنْوَارُ الْهُدَى مِنْ كَفِّهِ فِي كُلِّ حَالٍ", "en": "the winged maqlub.", "tr": "kanatlı maklûb.", "sourceStory": "talkhis-al-miftah", "sentence": "s14"},
  {"ar": "وَجِئْتُكَ مِنْ سَبَأٍ بِنَبَأٍ يَقِينٍ", "en": "27:22 — muzdawij.", "tr": "Neml 22 — müzdevic.", "sourceStory": "talkhis-al-miftah", "sentence": "s16"}],
 "commonMistakes": [
  {"wrong": "«سَبَأٍ / نَبَأٍ kalb cinâsıdır»",
   "right": "«Lâhiktir (sîn ile nûn mahreçte uzak), yan yana durduğu için müzdevic de denir; harflerin sırası dönmemiştir»",
   "why": {"en": "Qalb needs the same letters in another order; here one letter differs and the order stands.", "tr": "Kalb aynı harfleri başka sırada ister; burada bir harf ayrıdır ve sıra yerindedir."}}],
 "relatedNotes": ["jinas", "jinas-mudari-lahiq", "aks", "ilm-al-badi"]}

NOTE_L = {
 "id": "mulhaq-bil-jinas",
 "title": {"ar": "مَا يُلْحَقُ بِالْجِنَاسِ — الِاشْتِقَاقُ، وَشِبْهُ الِاشْتِقَاقِ", "en": "What is attached to the jinas — derivation, and the look-alike of derivation", "tr": "Cinâsa ilhak edilenler — iştikak ve şibh-i iştikak"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — ويلحق بالجناس شيئان: أحدهما أن يجمع اللفظين الاشتقاق، نحو: فأقم وجهك للدين القيم؛ والثاني أن يجمعهما المشابهة، وهي ما يشبه الاشتقاق، نحو: قال إني لعملكم من القالين."],
 "question": {
  "en": ["Do the two words go back to ONE ROOT? Then no jinas proper — the likeness is DERIVATION — but the Talkhis ATTACHES it to the jinas: أَقِمْ and الْقَيِّمِ are both ق و م (30:43).",
         "Do they only LOOK derived from one root while the roots part? قَالَ «he said» is ق و ل, الْقَالِينَ «those who detest» is ق ل ي (26:168): SHIBH ISHTIQAQ, the second thing attached.",
         "What does the engine read? The RootFinder's roots for the two words: one root — ishtiqaq; two roots under one skeleton — its look-alike. The ear's likeness is the surface; the root is the sarf."],
  "tr": ["İki kelime TEK KÖKE mi dönüyor? O zaman asıl cinas yok — benzeşme İŞTİKAK'tır — ama Telhîs onu cinâsa İLHAK eder: أَقِمْ ile الْقَيِّمِ ikisi de ق و م (Rûm 43).",
         "Yalnız bir kökten türemiş GÖRÜNÜYOR da kökler ayrılıyor mu? قَالَ «dedi» ق و ل, الْقَالِينَ «nefret edenler» ق ل ي (Şuarâ 168): ŞİBH-İ İŞTİKAK, ilhak edilen ikinci şey.",
         "Motor neyi okur? RootFinder'ın iki kelime için bulduğu kökleri: tek kök — iştikak; tek iskelet altında iki kök — benzeri. Kulağın benzerliği yüzeydir; kök sarftır."]},
 "plain": {
  "en": "Two things attached to the jinas: ishtiqaq (one root: أَقِمْ / الْقَيِّمِ) and its look-alike (two roots under one skeleton: قَالَ / الْقَالِينَ).",
  "tr": "Cinâsa ilhak edilen iki şey: iştikak (tek kök: أَقِمْ / الْقَيِّمِ) ve benzeri (tek iskelet altında iki kök: قَالَ / الْقَالِينَ)."},
 "explanation": {
  "en": "وَيُلْحَقُ بِالْجِنَاسِ شَيْئَانِ: أَحَدُهُمَا أَنْ يَجْمَعَ اللَّفْظَيْنِ الِاشْتِقَاقُ, the second أَنْ يَجْمَعَهُمَا الْمُشَابَهَةُ وَهِيَ مَا يُشْبِهُ الِاشْتِقَاقَ. Both are the ear's jinas without the mind's: the first because the sense is one, the second because the roots are two.",
  "tr": "وَيُلْحَقُ بِالْجِنَاسِ شَيْئَانِ: أَحَدُهُمَا أَنْ يَجْمَعَ اللَّفْظَيْنِ الِاشْتِقَاقُ, ikincisi أَنْ يَجْمَعَهُمَا الْمُشَابَهَةُ وَهِيَ مَا يُشْبِهُ الِاشْتِقَاقَ. İkisi de zihnin değil kulağın cinasıdır: ilki mânâ bir olduğu için, ikincisi kökler iki olduğu için."},
 "examples": [
  {"ar": "فَأَقِمْ وَجْهَكَ لِلدِّينِ الْقَيِّمِ", "en": "30:43 — ishtiqaq.", "tr": "Rûm 43 — iştikak.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"},
  {"ar": "قَالَ إِنِّي لِعَمَلِكُمْ مِنَ الْقَالِينَ", "en": "26:168 — shibh ishtiqaq.", "tr": "Şuarâ 168 — şibh-i iştikak.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"}],
 "commonMistakes": [
  {"wrong": "«الْقَالِينَ, قَالَ'nin ism-i fâilidir: söyleyenler»",
   "right": "«قَلَى «buğzetmek»ten قَالٍ'nin cemidir: nefret edenler — kök ق ل ي, قَالَ'nin kökü ق و ل»",
   "why": {"en": "The sound is one, the roots are two: that is exactly the look-alike of derivation.", "tr": "Ses bir, kök iki: iştikak benzeri tam da budur."}}],
 "relatedNotes": ["jinas", "jinas-tamm", "ilm-al-badi", "ism-fail", "naqis-verbs"]}

ADD_EN = (" Chapter 69 (lines ~4445-4475, sahifa 153-154) continues the jinas: the mudariʿ (s3; 6:26 s4; the hadith of the horses s5), the lahiq "
          "(104:1 s7; 40:75 s8; 4:83 s9), the jinas of qalb — whole (s11), part (the prayer s12), the winged maqlub (s14) — the muzdawij (27:22 s16) "
          "and the two things attached to the jinas: ishtiqaq (30:43 s18) and its look-alike (26:168 s20). The headings (s1, s2, s6, s10, s13, s15, "
          "s17, s19) are RESTORED: the source carries them only in Turkish, and the Arabic is the received matn of the Talkhis; every restored "
          "sentence is marked «Restored» in its translation. The Qur'an stands as the source prints it: 4:83 opens on فَإِذَا where the mushaf "
          "reads وَإِذَا, and 27:22 writes سَبَأٍ بِنَبَأٍ where the mushaf writes سَبَإٍ بِنَبَإٍ. The `badi` frames of kind `jinas` carry the `sub` "
          "(mudari, lahiq, qalb, ishtiqaq), a `kind2` (awwal, wasat, akhir; kull, bad, mujannah; muzdawij; shibh-ishtiqaq) and the `pair`.")
ADD_TR = (" Altmış dokuzuncu bâb (satır ~4445-4475, sahife 153-154) cinâsı sürdürür: muzâri (s3; En'âm 26 s4; atlar hadisi s5), lâhik (Hümeze 1 "
          "s7; Mü'min 75 s8; Nisâ 83 s9), kalb cinâsı — bütün (s11), kısım (dua s12), kanatlı maklûb (s14) — müzdevic (Neml 22 s16) ve cinâsa ilhak "
          "edilen iki şey: iştikak (Rûm 43 s18) ve benzeri (Şuarâ 168 s20). Başlıklar (s1, s2, s6, s10, s13, s15, s17, s19) GERİ YAZILMIŞTIR: kaynak "
          "bunları yalnız Türkçe taşır; Arapça, Telhîs'in alınan metnidir; her geri yazılmış cümle tercümesinde «geri yazılmıştır» diye işaretlidir. "
          "Kur'ân kaynağın bastığı gibidir: Nisâ 83 mushafta وَإِذَا iken فَإِذَا ile açılır; Neml 22 mushafta سَبَإٍ بِنَبَإٍ iken سَبَأٍ بِنَبَأٍ yazılır. "
          "`jinas` cinsinden `badi` çerçeveleri `sub` (muzâri, lâhik, kalb, iştikak), `kind2` (evvel, vasat, âhir; küll, ba'z, mücennah; müzdevic; "
          "şibh-i iştikak) ve `pair` taşır.")
write_out(69, S, TITLE, ADD_EN, ADD_TR, "4445-4475", GLOSS_ADD, notes=(NOTE_M, NOTE_Q, NOTE_L),
          related=(("jinas", ["jinas-mudari-lahiq", "jinas-qalb", "mulhaq-bil-jinas"]), ("jinas-tamm", ["jinas-mudari-lahiq", "jinas-qalb"]),
                   ("ilm-al-badi", ["jinas-mudari-lahiq", "jinas-qalb", "mulhaq-bil-jinas"])))
report(69, S, GLOSS_ADD, (NOTE_M, NOTE_Q, NOTE_L))
