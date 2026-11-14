# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 71: THE SAJʿ — its definition, its three kinds by the fasila's wazn (mutarraf, tarsiʿ, mutawazi), the finest
sajʿ by the length of its qarinas (equal; the second longer; the third longer; never the second much shorter), the pausal sukun the
asjaʿ are built on, the two qils (no «asjaʿ» in the Qurʾan; sajʿ in verse too), and the TASHTIR. Source lines ~4532-4568 (sahifa 157-158).

  RESTORED (the source carries the step only in Turkish): the definitions and rulings s1-s3, s5, s7, s9, s11, s13, s15-s16, s18-s19, s21
  — the received matn the Talkhis prints, marked «Restored» sentence by sentence. The examples are the source's own printed Arabic:
  71:13-14 (s4), al-Hariri (s6), 88:13-14 (s8), 56:28-30 (s10), 53:1-2 (s12), 69:30-31 (s14), the Arabs' saying (s17), Abu Tammam's
  two bayts (s20, s22).

  python3 tools/authoring/author_talkhis_ch71.py
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

J = "saj"
T = "tashtir"
TITLE = {"ar": "السَّجْعُ — أَقْسَامُهُ وَأَحْسَنُهُ، وَالتَّشْطِيرُ", "en": "The sajʿ — its kinds and its finest, and the tashtir", "tr": "Seci — kısımları ve en güzeli, ve taştîr"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the source gives this ruling only in Turkish; this is the received matn of the Talkhis.)"
R_TR = " (Geri yazım: kaynak bu hükmü yalnız Türkçe verir; bu, Telhîs'in alınan metnidir.)"
RB_EN = " (Restored: the source gives the bayt in Turkish with its rhyme words in Arabic; this is the received text the Talkhis cites.)"
RB_TR = " (Geri yazım: kaynak beyti Türkçe, kafiye kelimelerini Arapça verir; bu, Telhîs'in andığı alınan metindir.)"

def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)
def fi(tag, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def bihi(tag): return tok("بِهِ", "bi", "part", [tag, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْبَاءُ لِلسَّبَبِيَّةِ: بِسَبَبِهِ.", "«by him» — the ba of cause.", "«onunla» — sebep bâsı.",
                          segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")])
def wa_qila(tag):
    return tok("وَقِيلَ", "qala", "verb", [tag, "naib-al-fail", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَقِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ بَعْدَهُ.",
               "«and it was said» — the passive; the clause after it is the deputy.", "«ve denildi» — meçhul; ardındaki cümle nâib-i fâil.", punct=":",
               segments=[seg("وَ", "wa", "conj"), seg("قِيلَ", "qala", "verb")])

# ----------- s1 — the definition (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The SAJʿ is the AGREEMENT of the two fasilas of a prose piece upon ONE letter." + R_EN,
 "tr": "SECİ, nesrin iki fâsılasının BİR harf üzerinde BİRLEŞMESİdir." + R_TR},
 "tokens": [
  tok("السَّجْعُ", "saj", "noun", [J, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — السَّجْعُ: مِنْ سَجَعَتِ الْحَمَامَةُ.", "«the sajʿ» — the mubtada; from the dove's cooing.", "«seci» — mübtedâ; güvercinin ötüşünden.", punct=":"),
  tok("تَوَاطُؤُ", "tawatu", "noun", [J, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ تَوَاطَأَ: تَوَافَقَ.", "«the agreement of» — the khabar, a masdar of Form VI, annexed.", "«birleşmesi» — haber, tefâul masdarı, muzâf."),
  tok("الْفَاصِلَتَيْنِ", "fasila", "noun", [J, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى: الْفَاصِلَةُ آخِرُ الْقَرِينَةِ.", "«of the two fasilas» — the dual; a fasila is the clause's last word.", "«iki fâsılanın» — tesniye; fâsıla kavlin son kelimesi."),
  tok("مِنَ", "min", "prep", [J, "huruf-jarr"], "حَرْفُ جَرٍّ — كُسِرَتِ النُّونُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of» — the nun on a fatha before the sakin lam.", "«-den» — nûn sâkin lâm önünde fetha."),
  tok("النَّثْرِ", "nathr", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«prose».", "«nesrin»."),
  tok("عَلَى", "ala", "prep", [J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerinde»."),
  tok("حَرْفٍ", "harf", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«a letter».", "«bir harf»."),
  tok("وَاحِدٍ", "wahid", "noun", [J, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«one» — the naʿt.", "«tek» — na't."),
 ]})

# ----------- s2 — Sakkaki's saying (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And that is the meaning of al-Sakkaki's saying: «the asjaʿ in prose are like the qawafi in verse»." + R_EN,
 "tr": "Bu da Sekkâkî'nin şu sözünün mânâsıdır: «nesirdeki seciler şiirdeki kafiyeler gibidir»." + R_TR},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [J, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("مَعْنَى", "mana", "noun", [J, "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — مَقْصُورٌ.", "«the meaning of» — the khabar, a maqsur, annexed.", "«mânâsı» — haber, maksûr, muzâf."),
  tok("قَوْلِ", "qawl", "noun", [J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the saying of».", "«sözünün»."),
  tok("السَّكَّاكِيِّ", "sakkaki", "noun", [J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Sakkaki».", "«Sekkâkî'nin».", punct=":"),
  tok("الْأَسْجَاعُ", "saj", "noun", [J, "mubtada-khabar", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ — جَمْعُ سَجْعٍ.", "«the asjaʿ» — the mubtada; the plural of sajʿ.", "«seciler» — mübtedâ; sec'in çoğulu."),
  fi(J),
  tok("النَّثْرِ", "nathr", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«prose».", "«nesirde»."),
  tok("كَالْقَوَافِي", "qafiya", "noun", [J, "mubtada-khabar", "huruf-jarr", "ism-maqsur-manqus", "jam-taksir"], "الْكَافُ حَرْفُ جَرٍّ، وَالْقَوَافِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ بِأَلْ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "«like the qawafi» — the kaf of likeness; the manqus with its article keeps the ya; the phrase is the khabar.", "«kafiyeler gibi» — teşbih kâfı; el ile mankûs yâsını korur; câr-mecrur haber.",
      segments=[seg("كَ", "ka", "prep"), seg("الْقَوَافِي", "qafiya", "noun")]),
  fi(J),
  tok("الشِّعْرِ", "shir", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«verse».", "«şiirde»."),
 ]})

# ----------- s3 — the mutarraf (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "So if the two fasilas DIFFER in wazn, it is MUTARRAF." + R_EN,
 "tr": "İki fâsıla vezince FARKLI ise, MUTARRAF'tır." + R_TR},
 "tokens": [
  tok("فَإِنِ", "in-shartiyya", "part", [J, "in-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ — كُسِرَتِ النُّونُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«so if» — the conditional; its nun takes a kasra before the wasl alif.", "«eğer» — şart edatı; nûn vasıl elifi önünde kesre.",
      segments=[seg("فَ", "fa", "conj"), seg("إِنِ", "in-shartiyya", "part")]),
  tok("اخْتَلَفَتِ", "ikhtalafa", "verb", [J, "in-shartiyya", "form-viii-verbs"], "فِعْلُ الشَّرْطِ — مَاضٍ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ لِلتَّأْنِيثِ كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«differ» — the shart verb; the feminine ta on a kasra before the article.", "«farklı olursa» — şart fiili; te'nis tâsı elif-lâm önünde kesre."),
  tok("الْفَاصِلَتَانِ", "fasila", "noun", [J, "fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«the two fasilas» — the doer, a dual.", "«iki fâsıla» — fâil, tesniye."),
  fi(J),
  tok("الْوَزْنِ", "wazn", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«wazn».", "«vezinde»."),
  tok("فَمُطَرَّفٌ", "mutarraf", "noun", [J, "in-shartiyya", "mubtada-khabar", "ism-maful"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَمُطَرَّفٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: فَهُوَ مُطَرَّفٌ.", "«then mutarraf» — the fa of the jawab; the khabar of a dropped «it is».", "«mutarraftır» — cevap fâsı; düşmüş mübtedânın haberi.",
      segments=[seg("فَ", "fa", "conj"), seg("مُطَرَّفٌ", "mutarraf", "noun")]),
 ]})

# ----------- s4 — 71:13-14 (mutarraf)
S.append({"id": "s4", "translation": {
 "en": "«What is with you that you do not hope for MAJESTY (waqara) from Allah — while He created you in STAGES (atwara)?» (71:13-14) — waqaran and atwaran agree on the ra but differ in wazn: mutarraf.",
 "tr": "«Size ne oluyor da Allah için VAKAR (vekârâ) ummuyorsunuz — hâlbuki sizi TAVIRLARLA (etvârâ) yarattı?» (Nûh 13-14) — vekâran ile etvâran râ'da birleşir, vezince ayrılır: mutarraf."},
 "tokens": [
  tok("مَا", "ma-istifham", "pron", [J, "al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ.", "«what» — the interrogative mubtada.", "«ne» — soru ismi, mübtedâ."),
  tok("لَكُمْ", "li", "part", [J, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«is with you» — the jarr phrase is the khabar.", "«size» — câr-mecrur haber.",
      segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("لَا", "la-nafiya", "part", [J], "حَرْفُ نَفْيٍ.", "«not».", "«-me»."),
  tok("تَرْجُونَ", "raja", "verb", [J, "hal", "mudari-marfu", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ حَالٌ.", "«you hope» — one of the five verbs; the waw its doer; the clause a hal.", "«umuyorsunuz» — ef'âl-i hamse; vâv fâil; cümle hâl."),
  tok("لِلَّهِ", "allah", "noun", [J, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«from Allah».", "«Allah için».",
      segments=[seg("لِ", "li", "prep"), seg("اللَّهِ", "allah", "noun")]),
  tok("وَقَارًا", "waqar", "noun", [J, "maful-bihi", "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْفَاصِلَةُ الْأُولَى.", "«majesty» — the object; the first fasila.", "«vakar» — mef'ul; birinci fâsıla.", punct="،"),
  tok("وَقَدْ", "qad", "part", [J, "hal", "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ لِلتَّحْقِيقِ.", "«while indeed» — the waw of hal.", "«hâlbuki» — hâl vâvı.",
      segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("خَلَقَكُمْ", "khalaqa", "verb", [J, "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«He created you» — the doer concealed; the kaf the object.", "«sizi yarattı» — fâil gizli; kâf mef'ul.",
      segments=[seg("خَلَقَ", "khalaqa", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("أَطْوَارًا", "tawr", "noun", [J, "hal", "jam-taksir"], "حَالٌ مَنْصُوبٌ — جَمْعُ طَوْرٍ؛ الْفَاصِلَةُ الثَّانِيَةُ.", "«in stages» — the hal; the plural of tawr; the second fasila.", "«tavırlarla» — hâl; tavr'ın çoğulu; ikinci fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "mutarraf", "pair": [ix(S[-1], "وَقَارًا"), ix(S[-1], "أَطْوَارًا")]}]

# ----------- s5 — the tarsiʿ (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "Otherwise — if what stands in one of the two qarinas as words, or most of it, is the LIKE of what faces it in the other in wazn and in rhyme, it is TARSIʿ." + R_EN,
 "tr": "Değilse — iki karînenin birindeki lafızlar yahut çoğu, öbüründe karşısına düşenin vezin ve kafiyede BENZERİ ise, TARSÎ'dir." + R_TR},
 "tokens": [
  tok("وَإِلَّا", "illa", "part", [J, "in-shartiyya", "istithna"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ لَا — شَرْطٌ مَحْذُوفُ الْفِعْلِ: وَإِنْ لَمْ يَخْتَلِفَا.", "«otherwise» — in + la: a shart whose verb is understood.", "«değilse» — in + lâ: fiili düşmüş şart.",
      segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  tok("فَإِنْ", "in-shartiyya", "part", [J, "in-shartiyya"], "الْفَاءُ رَابِطَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«then if».", "«o hâlde eğer».",
      segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [J, "kana-wa-akhawatuha", "in-shartiyya"], "فِعْلُ الشَّرْطِ — مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«is» — kana, the shart verb.", "«ise» — kâne, şart fiili."),
  tok("مَا", "ma-mawsula", "pron", [J, "ism-mawsul", "kana-wa-akhawatuha"], "اسْمٌ مَوْصُولٌ اسْمُ كَانَ.", "«what» — the relative, kana's ism.", "«-en şey» — ism-i mevsûl, kâne'nin ismi."),
  fi(J),
  tok("إِحْدَى", "ihda", "noun", [J, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مَقْصُورٌ: مُؤَنَّثُ أَحَدٍ.", "«one of» (fem.) — a maqsur, annexed.", "«birinde» — maksûr, muzâf; ahad'ın müennesi."),
  tok("الْقَرِينَتَيْنِ", "qarina", "noun", [J, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — الْقَرِينَةُ: الْفِقْرَةُ الْمَسْجُوعَةُ.", "«the two qarinas» — a qarina is one rhymed clause.", "«iki karînenin» — karîne, secili bir cümle."),
  tok("مِنَ", "min", "prep", [J, "huruf-jarr"], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of» — the min of explanation.", "«-den» — beyan min'i."),
  tok("الْأَلْفَاظِ", "lafz", "noun", [J, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ لَفْظٍ.", "«words».", "«lafızlardan»."),
  tok("أَوْ", "aw", "part", [J, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("أَكْثَرُهُ", "akthar", "noun", [J, "atf-nasaq", "idafa-definiteness", "ism-tafdil"], "مَعْطُوفٌ عَلَى مَا مَرْفُوعٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«or most of it» — joined onto the relative.", "«yahut çoğu» — mâ'ya atıf.",
      segments=[seg("أَكْثَرُ", "akthar", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("مِثْلَ", "mithl", "noun", [J, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«the like of» — kana's khabar, annexed.", "«benzeri» — kâne'nin haberi, muzâf."),
  tok("مَا", "ma-mawsula", "pron", [J, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«what» — the relative, the mudaf ilayh.", "«-enin» — mevsûl, muzâfun ileyh."),
  tok("يُقَابِلُهُ", "qabala", "verb", [J, "jumla-sifa", "maful-bihi", "form-ii-verbs"], "صِلَةُ الْمَوْصُولِ — مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«faces it» — the sila; the ha its object.", "«karşısına düşen» — sıla; hâ mef'ul.",
      segments=[seg("يُقَابِلُ", "qabala", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("مِنَ", "min", "prep", [J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْأُخْرَى", "ukhra", "noun", [J, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«the other» — a maqsur.", "«öbüründen» — maksûr."),
  fi(J),
  tok("الْوَزْنِ", "wazn", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«wazn».", "«vezinde»."),
  tok("وَالتَّقْفِيَةِ", "taqfiya", "noun", [J, "atf-nasaq", "masdar"], "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ قَفَّى: جَعَلَ لَهُ قَافِيَةً.", "«and rhyme» — joined; the masdar of «to give a qafiya».", "«ve kafiyede» — atıf; kafiye verme masdarı.",
      segments=[seg("وَ", "wa", "conj"), seg("التَّقْفِيَةِ", "taqfiya", "noun")]),
  tok("فَتَرْصِيعٌ", "tarsi", "noun", [J, "in-shartiyya", "mubtada-khabar", "masdar"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَتَرْصِيعٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ — مَصْدَرُ رَصَّعَ: نَظَمَ الْجَوْهَرَ.", "«then tarsiʿ» — the jawab's khabar; the masdar of «to set jewels».", "«tarsî'dir» — cevabın haberi; cevher dizmek masdarı.",
      segments=[seg("فَ", "fa", "conj"), seg("تَرْصِيعٌ", "tarsi", "noun")]),
 ]})

# ----------- s6 — al-Hariri (tarsiʿ)
S.append({"id": "s6", "translation": {
 "en": "«So he STAMPS the asjaʿ with the jewels of his WORDING (lafzihi), and STRIKES the ears with the rebukes of his PREACHING (waʿzihi)» (al-Hariri) — word answers word in wazn and rhyme: tarsiʿ.",
 "tr": "«O, secileri LAFZININ (lafzihi) cevherleriyle DAMGALAR, kulakları VAAZININ (va'zihi) zecirleriyle ÇINLATIR» (Harîrî) — kelime kelimeye vezin ve kafiyede karşılık verir: tarsî'."},
 "tokens": [
  tok("فَهُوَ", "huwa", "pron", [J, "mubtada-khabar"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«so he» — the mubtada.", "«o» — mübtedâ.",
      segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("يَطْبَعُ", "tabaa", "verb", [J, "mubtada-khabar", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«stamps» — the verb clause is the khabar.", "«damgalar» — fiil cümlesi haber."),
  tok("الْأَسْجَاعَ", "saj", "noun", [J, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the asjaʿ» — the object.", "«secileri» — mef'ul."),
  tok("بِجَوَاهِرِ", "jawhar", "noun", [J, "huruf-jarr", "idafa-definiteness", "mamnu-min-sarf", "jam-taksir"], "جَارٌّ وَمَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ، مُضَافٌ — جَمْعُ جَوْهَرٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.", "«with the jewels of» — the diptote takes its kasra in the idafa.", "«cevherleriyle» — gayr-i munsarif izâfette kesre alır.",
      segments=[seg("بِ", "bi", "prep"), seg("جَوَاهِرِ", "jawhar", "noun")]),
  tok("لَفْظِهِ", "lafz", "noun", [J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْفَاصِلَةُ الْأُولَى.", "«his wording» — the first fasila.", "«lafzının» — birinci fâsıla.", punct="،",
      segments=[seg("لَفْظِ", "lafz", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("وَيَقْرَعُ", "qaraa-knock", "verb", [J, "atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَقْرَعُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and strikes».", "«ve çınlatır».",
      segments=[seg("وَ", "wa", "conj"), seg("يَقْرَعُ", "qaraa-knock", "verb")]),
  tok("الْأَسْمَاعَ", "sam", "noun", [J, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ سَمْعٍ.", "«the ears» — the object; the plural of samʿ.", "«kulakları» — mef'ul; sem'in çoğulu."),
  tok("بِزَوَاجِرِ", "zajir", "noun", [J, "huruf-jarr", "idafa-definiteness", "mamnu-min-sarf", "jam-taksir"], "جَارٌّ وَمَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ — جَمْعُ زَاجِرٍ.", "«with the rebukes of» — the plural of zajir.", "«zecirleriyle» — zâcir'in çoğulu.",
      segments=[seg("بِ", "bi", "prep"), seg("زَوَاجِرِ", "zajir", "noun")]),
  tok("وَعْظِهِ", "waz", "noun", [J, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْفَاصِلَةُ الثَّانِيَةُ.", "«his preaching» — the second fasila.", "«vaazının» — ikinci fâsıla.",
      segments=[seg("وَعْظِ", "waz", "noun"), seg("هِ", "pron-3ms", "pron")]),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "murassa", "pair": [ix(S[-1], "لَفْظِهِ"), ix(S[-1], "وَعْظِهِ")]}]

# ----------- s7 — the mutawazi (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "Otherwise it is MUTAWAZI." + R_EN,
 "tr": "Değilse MÜTEVÂZÎ'dir." + R_TR},
 "tokens": [
  tok("وَإِلَّا", "illa", "part", [J, "in-shartiyya", "istithna"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ لَا — شَرْطٌ مَحْذُوفُ الْفِعْلِ.", "«otherwise» — in + la.", "«değilse» — in + lâ.",
      segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  tok("فَمُتَوَازٍ", "mutawazi", "noun", [J, "in-shartiyya", "mubtada-khabar", "ism-maqsur-manqus", "ism-fail"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَمُتَوَازٍ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ — مَنْقُوصٌ حُذِفَتْ يَاؤُهُ وَعُوِّضَ التَّنْوِينُ.", "«then mutawazi» — the manqus drops its ya and keeps a tanwin of compensation.", "«mütevâzîdir» — mankûs yâsını düşürür, ivaz tenvini kalır.",
      segments=[seg("فَ", "fa", "conj"), seg("مُتَوَازٍ", "mutawazi", "noun")]),
 ]})

# ----------- s8 — 88:13-14 (mutawazi)
S.append({"id": "s8", "translation": {
 "en": "«Therein are couches RAISED (marfuʿa) and cups SET OUT (mawduʿa)» (88:13-14) — the two fasilas share a wazn and the rest do not: mutawazi.",
 "tr": "«Orada YÜKSELTİLMİŞ (merfûa) tahtlar ve KONULMUŞ (mevdûa) kaplar vardır» (Gâşiye 13-14) — iki fâsıla aynı vezinde, gerisi değil: mütevâzî."},
 "tokens": [
  tok("فِيهَا", "fi", "part", [J, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«therein» — the fronted khabar.", "«orada» — mukaddem haber.",
      segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("سُرُرٌ", "sarir", "noun", [J, "mubtada-khabar", "jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — جَمْعُ سَرِيرٍ.", "«couches» — the delayed mubtada; the plural of sarir.", "«tahtlar» — muahhar mübtedâ; serîr'in çoğulu."),
  tok("مَرْفُوعَةٌ", "marfua", "noun", [J, "naat-sifa", "ism-maful"], "نَعْتٌ مَرْفُوعٌ — الْفَاصِلَةُ الْأُولَى.", "«raised» — the naʿt; the first fasila.", "«yükseltilmiş» — na't; birinci fâsıla.", punct="،"),
  tok("وَأَكْوَابٌ", "kub", "noun", [J, "atf-nasaq", "jam-taksir"], "مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ كُوبٍ.", "«and cups» — joined; the plural of kub.", "«ve kaplar» — atıf; kûb'un çoğulu.",
      segments=[seg("وَ", "wa", "conj"), seg("أَكْوَابٌ", "kub", "noun")]),
  tok("مَوْضُوعَةٌ", "mawdua", "noun", [J, "naat-sifa", "ism-maful"], "نَعْتٌ مَرْفُوعٌ — الْفَاصِلَةُ الثَّانِيَةُ.", "«set out» — the naʿt; the second fasila.", "«konulmuş» — na't; ikinci fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "mutawazi", "pair": [ix(S[-1], "مَرْفُوعَةٌ"), ix(S[-1], "مَوْضُوعَةٌ")]}]

# ----------- s9 — the finest sajʿ (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "And the FINEST sajʿ is that whose qarinas are EQUAL." + R_EN,
 "tr": "Secinin EN GÜZELİ, karîneleri EŞİT olandır." + R_TR},
 "tokens": [
  tok("وَأَحْسَنُ", "ahsan", "noun", [J, "mubtada-khabar", "idafa-definiteness", "ism-tafdil"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَحْسَنُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«and the finest of» — the mubtada, an afʿal of comparison, annexed.", "«en güzeli» — mübtedâ, ism-i tafdil, muzâf.",
      segments=[seg("وَ", "wa", "conj"), seg("أَحْسَنُ", "ahsan", "noun")]),
  tok("السَّجْعِ", "saj", "noun", [J, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sajʿ».", "«secinin»."),
  tok("مَا", "ma-mawsula", "pron", [J, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«that which» — the relative, the khabar.", "«olandır» — mevsûl, haber."),
  tok("تَسَاوَتْ", "tasawa", "verb", [J, "jumla-sifa", "naqis-verbs"], "صِلَةُ الْمَوْصُولِ — مَاضٍ، نَاقِصٌ حُذِفَتْ أَلِفُهُ لِلتَّاءِ.", "«are equal» — the sila; the naqis drops its alif before the feminine ta.", "«eşittir» — sıla; nâkıs, tâ önünde elifi düşer."),
  tok("قَرَائِنُهُ", "qarina", "noun", [J, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ؛ جَمْعُ قَرِينَةٍ.", "«its qarinas» — the doer; the plural of qarina.", "«karîneleri» — fâil; karîne'nin çoğulu.",
      segments=[seg("قَرَائِنُ", "qarina", "noun"), seg("هُ", "pron-3ms", "pron")]),
 ]})

# ----------- s10 — 56:28-30 (equal qarinas)
S.append({"id": "s10", "translation": {
 "en": "«Among thornless lote-trees (makhdud), and banana-trees layered (mandud), and shade extended (mamdud)» (56:28-30) — three qarinas of one measure: the finest.",
 "tr": "«Dikensiz kirazlar (mahdûd), meyveleri istiflenmiş muz ağaçları (mendûd) ve yayılmış gölgeler (memdûd) içinde» (Vâkıa 28-30) — üç karîne bir ölçüde: en güzeli."},
 "tokens": [
  fi(J),
  tok("سِدْرٍ", "sidr", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«lote-trees».", "«kirazlar»."),
  tok("مَخْضُودٍ", "makhdud", "noun", [J, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ — الْفَاصِلَةُ الْأُولَى.", "«thornless» — the naʿt; the first fasila.", "«dikensiz» — na't; birinci fâsıla."),
  tok("وَطَلْحٍ", "talh", "noun", [J, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«and banana-trees» — joined.", "«ve muz ağaçları» — atıf.",
      segments=[seg("وَ", "wa", "conj"), seg("طَلْحٍ", "talh", "noun")]),
  tok("مَنْضُودٍ", "mandud", "noun", [J, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ — الْفَاصِلَةُ الثَّانِيَةُ.", "«layered» — the second fasila.", "«istiflenmiş» — ikinci fâsıla."),
  tok("وَظِلٍّ", "zill", "noun", [J, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«and shade» — joined.", "«ve gölge» — atıf.",
      segments=[seg("وَ", "wa", "conj"), seg("ظِلٍّ", "zill", "noun")]),
  tok("مَمْدُودٍ", "mamdud", "noun", [J, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ — الْفَاصِلَةُ الثَّالِثَةُ.", "«extended» — the third fasila.", "«yayılmış» — üçüncü fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "mutawazi", "kind2": "equal", "pair": [ix(S[-1], "مَخْضُودٍ"), ix(S[-1], "مَنْضُودٍ")]},
                 {"kind": "saj", "sub": "mutawazi", "kind2": "equal", "pair": [ix(S[-1], "مَنْضُودٍ"), ix(S[-1], "مَمْدُودٍ")]}]

# ----------- s11 — then the second longer (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "Then that whose SECOND qarina is the LONGER." + R_EN,
 "tr": "Sonra İKİNCİ karînesi UZUN olan." + R_TR},
 "tokens": [
  tok("ثُمَّ", "thumma", "part", [J, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then».", "«sonra»."),
  tok("مَا", "ma-mawsula", "pron", [J, "ism-mawsul", "atf-nasaq"], "اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "«that which» — joined onto the earlier relative.", "«olan» — önceki mevsûle atıf."),
  tok("طَالَتْ", "tala-long", "verb", [J, "jumla-sifa", "hollow-verbs"], "صِلَةُ الْمَوْصُولِ — مَاضٍ أَجْوَفُ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«is long» — the sila; a hollow verb.", "«uzundur» — sıla; ecvef."),
  tok("قَرِينَتُهُ", "qarina", "noun", [J, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its qarina» — the doer.", "«karînesi» — fâil.",
      segments=[seg("قَرِينَتُ", "qarina", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("الثَّانِيَةُ", "thani", "noun", [J, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«the second» — the naʿt.", "«ikinci» — na't."),
 ]})

# ----------- s12 — 53:1-2 (the second longer)
S.append({"id": "s12", "translation": {
 "en": "«By the star when it SETS (hawa) — your companion has not strayed, nor has he ERRED (ghawa)» (53:1-2) — the second qarina the longer.",
 "tr": "«BATTIĞI (hevâ) zaman yıldıza andolsun — arkadaşınız sapmadı, AZMADI (gavâ) da» (Necm 1-2) — ikinci karîne daha uzun."},
 "tokens": [
  tok("وَالنَّجْمِ", "najm", "noun", [J, "huruf-jarr"], "الْوَاوُ لِلْقَسَمِ حَرْفُ جَرٍّ، وَالنَّجْمِ مَجْرُورٌ — مُقْسَمٌ بِهِ.", "«by the star» — the waw of the oath governs the jarr.", "«yıldıza andolsun» — yemin vâvı cer eder.",
      segments=[seg("وَ", "wa", "conj"), seg("النَّجْمِ", "najm", "noun")]),
  tok("إِذَا", "idha", "part", [J, "maful-fih", "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ، مُضَافٌ إِلَى جُمْلَتِهِ.", "«when» — the zarf, annexed to its clause.", "«-dığı zaman» — zarf, cümlesine muzâf."),
  tok("هَوَى", "hawa-fall", "verb", [J, "naqis-verbs", "maful-fih"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْفَاصِلَةُ الْأُولَى.", "«sets» — a naqis mazi; the first fasila.", "«batar» — nâkıs mâzî; birinci fâsıla.", punct="،"),
  tok("مَا", "ma-nafiya", "part", [J, "anwa-ma"], "حَرْفُ نَفْيٍ — جَوَابُ الْقَسَمِ.", "«not» — the oath's answer.", "«-medi» — yeminin cevabı."),
  tok("ضَلَّ", "dalla-stray", "verb", [J, "doubled-verbs"], "فِعْلٌ مَاضٍ مُضَاعَفٌ.", "«has strayed» — a doubled verb.", "«sapmadı» — muzâaf."),
  tok("صَاحِبُكُمْ", "sahib", "noun", [J, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your companion» — the doer.", "«arkadaşınız» — fâil.",
      segments=[seg("صَاحِبُ", "sahib", "noun"), seg("كُمْ", "pron-2mp", "pron")]),
  tok("وَمَا", "ma-nafiya", "part", [J, "anwa-ma", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا حَرْفُ نَفْيٍ.", "«nor».", "«ve … -madı».",
      segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  tok("غَوَى", "ghawa", "verb", [J, "naqis-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْفَاصِلَةُ الثَّانِيَةُ.", "«erred» — the second fasila.", "«azmadı» — ikinci fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "mutawazi", "kind2": "second-longer", "pair": [ix(S[-1], "هَوَى"), ix(S[-1], "غَوَى")]}]

# ----------- s13 — or the third (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "Or the THIRD." + R_EN,
 "tr": "Yahut ÜÇÜNCÜSÜ." + R_TR},
 "tokens": [
  tok("أَوِ", "aw", "part", [J, "atf-nasaq"], "حَرْفُ عَطْفٍ — كُسِرَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — the waw takes a kasra before the article.", "«yahut» — vâv sâkin lâm önünde kesre."),
  tok("الثَّالِثَةُ", "thalith", "noun", [J, "atf-nasaq"], "مَعْطُوفٌ عَلَى الثَّانِيَةِ مَرْفُوعٌ.", "«the third» — joined onto «the second».", "«üçüncüsü» — ikinciye atıf."),
 ]})

# ----------- s14 — 69:30-31 (the third longer)
S.append({"id": "s14", "translation": {
 "en": "«SEIZE HIM (khudhuhu), then SHACKLE HIM (ghulluhu), then into the Blaze ROAST HIM (salluhu)» (69:30-31) — the third qarina the longer.",
 "tr": "«TUTUN ONU (huzûhu), BAĞLAYIN ONU (gullûhu), sonra alevli ateşe ATIN ONU (sallûhu)» (Hâkka 30-31) — üçüncü karîne daha uzun."},
 "tokens": [
  tok("خُذُوهُ", "akhadha", "verb", [J, "imperative-amr", "maful-bihi"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — أَمْرٌ مُخَفَّفٌ: أَصْلُهُ اؤْخُذُوا؛ الْفَاصِلَةُ الْأُولَى.", "«seize him» — the light amr of akhadha; the waw its doer; the first fasila.", "«tutun onu» — ehaze'nin hafif emri; vâv fâil; birinci fâsıla.", punct="،",
      segments=[seg("خُذُوا", "akhadha", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("فَغُلُّوهُ", "ghalla", "verb", [J, "imperative-amr", "maful-bihi", "doubled-verbs", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَغُلُّوا أَمْرٌ مُضَاعَفٌ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْفَاصِلَةُ الثَّانِيَةُ.", "«then shackle him» — a doubled amr; the second fasila.", "«bağlayın onu» — muzâaf emir; ikinci fâsıla.", punct="،",
      segments=[seg("فَ", "fa", "conj"), seg("غُلُّوا", "ghalla", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("ثُمَّ", "thumma", "part", [J, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("الْجَحِيمَ", "jahim", "noun", [J, "maful-bihi"], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ — عَلَى نَزْعِ الْخَافِضِ: فِي الْجَحِيمِ.", "«the Blaze» — the fronted object, the preposition understood.", "«alevli ateşe» — mukaddem mef'ul, harf-i cer düşmüş."),
  tok("صَلُّوهُ", "salla-roast", "verb", [J, "imperative-amr", "maful-bihi", "form-ii-verbs", "naqis-verbs"], "فِعْلُ أَمْرٍ مِنْ صَلَّى مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْفَاصِلَةُ الثَّالِثَةُ.", "«roast him» — the amr of salla (Form II); the third fasila.", "«atın onu» — sallâ'nın emri (tef'îl); üçüncü fâsıla.",
      segments=[seg("صَلُّوا", "salla-roast", "verb"), seg("هُ", "pron-3ms", "pron")]),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "mutarraf", "pair": [ix(S[-1], "خُذُوهُ"), ix(S[-1], "فَغُلُّوهُ")]},
                 {"kind": "saj", "kind2": "third-longer", "pair": [ix(S[-1], "فَغُلُّوهُ"), ix(S[-1], "صَلُّوهُ")]}]

# ----------- s15 — never the second much shorter (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "And it is not fine that the second be MUCH SHORTER than it." + R_EN,
 "tr": "İkincinin ondan ÇOK KISA olması güzel değildir." + R_TR},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [J], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا حَرْفُ نَفْيٍ.", "«and not».", "«ve … değildir».",
      segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("يَحْسُنُ", "hasuna", "verb", [J, "mudari-marfu", "an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْفَاعِلُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«it is fine» — the doer is the an-clause.", "«güzel olur» — fâil, en'li cümle."),
  tok("أَنْ", "an-masdariyya", "part", [J, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that».", "«-ması»."),
  tok("تَكُونَ", "kana", "verb", [J, "kana-wa-akhawatuha", "an-masdariyya"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be» — kana, mansub.", "«olması» — kâne, mansûb."),
  tok("الثَّانِيَةُ", "thani", "noun", [J, "kana-wa-akhawatuha"], "اسْمُ تَكُونَ مَرْفُوعٌ.", "«the second» — kana's ism.", "«ikinci» — kâne'nin ismi."),
  tok("أَقْصَرَ", "aqsar", "noun", [J, "kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ تَكُونَ مَنْصُوبٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«shorter» — kana's khabar, a diptote afʿal.", "«daha kısa» — haber, gayr-i munsarif ism-i tafdil."),
  tok("مِنْهَا", "min", "part", [J, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«than it».", "«ondan».",
      segments=[seg("مِنْ", "min", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("كَثِيرًا", "kathir", "noun", [J, "maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ: قِصَرًا كَثِيرًا.", "«much» — standing for the absolute object.", "«çok» — mef'ûl-i mutlak yerine."),
 ]})

# ----------- s16 — built on the sukun (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "And the asjaʿ are BUILT on the SUKUN of their closes." + R_EN,
 "tr": "Seciler sonlarının SÜKÛNU üzere BİNA edilir." + R_TR},
 "tokens": [
  tok("وَالْأَسْجَاعُ", "saj", "noun", [J, "mubtada-khabar", "jam-taksir"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْأَسْجَاعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the asjaʿ» — the mubtada.", "«seciler» — mübtedâ.",
      segments=[seg("وَ", "wa", "conj"), seg("الْأَسْجَاعُ", "saj", "noun")]),
  tok("مَبْنِيَّةٌ", "mabni", "noun", [J, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ بَنَى.", "«built» — the khabar; the ism mafʿul of bana.", "«bina edilmiş» — haber; benâ'nın ism-i mef'ûlü."),
  tok("عَلَى", "ala", "prep", [J, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  tok("سُكُونِ", "sukun", "noun", [J, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، مُضَافٌ.", "«the sukun of».", "«sükûnu»."),
  tok("الْأَعْجَازِ", "ajuz", "noun", [J, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ عَجُزٍ: آخِرُ الْقَرِينَةِ.", "«of the closes» — the plural of ʿajuz.", "«sonlarının» — acüz'ün çoğulu."),
 ]})

# ----------- s17 — the Arabs' saying (sukun)
S.append({"id": "s17", "translation": {
 "en": "«How far is what has PASSED (fat), and how near is what is COMING (at)!» — the Arabs' saying; both closes are read on a sukun.",
 "tr": "«GEÇEN (fât) ne kadar uzak, GELECEK olan (ât) ne kadar yakın!» — Arapların sözü; iki son da sükûn ile okunur."},
 "tokens": [
  tok("مَا", "ma-taajjub", "part", [J, "mubtada-khabar"], "مَا التَّعَجُّبِيَّةُ: نَكِرَةٌ تَامَّةٌ مُبْتَدَأٌ.", "«how!» — the ma of wonder, the mubtada.", "«ne!» — taaccüb mâ'sı, mübtedâ."),
  tok("أَبْعَدَ", "abada-far", "verb", [J, "mubtada-khabar", "form-iv-verbs"], "فِعْلُ التَّعَجُّبِ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى مَا — وَالْجُمْلَةُ خَبَرٌ.", "«far is» — the verb of wonder; the clause is the khabar.", "«ne uzak» — taaccüb fiili; cümle haber."),
  tok("مَا", "ma-mawsula", "pron", [J, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what» — the relative, the object.", "«-en şey» — mevsûl, mef'ul."),
  tok("فَاتْ", "fata", "verb", [J, "jumla-sifa", "hollow-verbs", "saj"], "صِلَةُ الْمَوْصُولِ — مَاضٍ أَجْوَفُ، سُكِّنَ آخِرُهُ لِلسَّجْعِ.", "«has passed» — the sila; its close on a sukun for the sajʿ.", "«geçti» — sıla; sonu seci için sâkin.", punct="،"),
  tok("وَمَا", "ma-taajjub", "part", [J, "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا التَّعَجُّبِيَّةُ مُبْتَدَأٌ.", "«and how!».", "«ve ne!».",
      segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-taajjub", "part")]),
  tok("أَقْرَبَ", "aqraba", "verb", [J, "mubtada-khabar", "form-iv-verbs"], "فِعْلُ التَّعَجُّبِ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«near is» — the verb of wonder.", "«ne yakın» — taaccüb fiili."),
  tok("مَا", "ma-mawsula", "pron", [J, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what» — the object.", "«-en şey» — mef'ul."),
  tok("هُوَ", "huwa", "pron", [J, "mubtada-khabar"], "مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةٌ.", "«it» — the mubtada of the sila.", "«o» — sılanın mübtedâsı."),
  tok("آتْ", "atin", "noun", [J, "mubtada-khabar", "ism-fail", "ism-maqsur-manqus", "saj"], "خَبَرٌ — اسْمُ فَاعِلٍ مِنْ أَتَى، مَنْقُوصٌ: آتٍ؛ سُكِّنَ لِلسَّجْعِ.", "«coming» — the khabar; the manqus ism faʿil, its close on a sukun for the sajʿ.", "«gelecek» — haber; mankûs ism-i fâil, seci için sâkin."),
 ]})
S[-1]["badi"] = [{"kind": "saj", "pair": [ix(S[-1], "فَاتْ"), ix(S[-1], "آتْ")]}]

# ----------- s18 — no «asjaʿ» in the Qurʾan (RESTORED)
S.append({"id": "s18", "translation": {
 "en": "And it was said: one does not say «asjaʿ» of the Qurʾan, but FAWASIL." + R_EN,
 "tr": "Denildi ki: Kur'ân'da «seci» denmez, FÂSILA denir." + R_TR},
 "tokens": [
  wa_qila(J),
  tok("لَا", "la-nafiya", "part", [J], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يُقَالُ", "qala", "verb", [J, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — أَجْوَفُ.", "«is said» — the passive of a hollow verb.", "«denir» — ecvef meçhul."),
  fi(J),
  tok("الْقُرْآنِ", "quran", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«the Qurʾan».", "«Kur'ân'da»."),
  tok("أَسْجَاعٌ", "saj", "noun", [J, "naib-al-fail", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«asjaʿ» — the deputy doer.", "«seciler» — nâib-i fâil."),
  tok("بَلْ", "bal", "part", [J, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلْإِضْرَابِ.", "«but rather».", "«bilakis»."),
  tok("فَوَاصِلُ", "fasila", "noun", [J, "atf-nasaq", "mamnu-min-sarf", "jam-taksir"], "مَعْطُوفٌ مَرْفُوعٌ بِلَا تَنْوِينٍ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«fawasil» — joined; a diptote plural.", "«fâsılalar» — atıf; gayr-i munsarif çoğul."),
 ]})
S[-1]["badi"] = [{"kind": "tibaq", "sub": "salb", "pair": [ix(S[-1], "وَقِيلَ"), ix(S[-1], "يُقَالُ")]}]

# ----------- s19 — sajʿ in verse too (RESTORED)
S.append({"id": "s19", "translation": {
 "en": "And it was said: the sajʿ is not confined to prose, but occurs in VERSE." + R_EN,
 "tr": "Denildi ki: seci nesre mahsus değildir, NAZIMDA da olur." + R_TR},
 "tokens": [
  wa_qila(J),
  tok("لَا", "la-nafiya", "part", [J], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يَخْتَصُّ", "ikhtassa", "verb", [J, "mudari-marfu", "form-viii-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مُضَاعَفٌ مِنَ الِافْتِعَالِ.", "«is confined» — a doubled Form VIII.", "«mahsus olmaz» — muzâaf iftiâl."),
  tok("السَّجْعُ", "saj", "noun", [J, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the sajʿ» — the doer.", "«seci» — fâil."),
  tok("بِالنَّثْرِ", "nathr", "noun", [J, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to prose».", "«nesre».",
      segments=[seg("بِ", "bi", "prep"), seg("النَّثْرِ", "nathr", "noun")]),
  tok("بَلْ", "bal", "part", [J, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلْإِضْرَابِ.", "«but».", "«bilakis»."),
  tok("يَكُونُ", "kana", "verb", [J, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — كَانَ التَّامَّةُ: يُوجَدُ.", "«occurs» — the full kana: «exists»; the doer concealed.", "«olur» — tam kâne: bulunur; fâil gizli."),
  fi(J),
  tok("النَّظْمِ", "nazm", "noun", [J, "huruf-jarr"], "مَجْرُورٌ.", "«verse».", "«nazımda»."),
 ]})

# ----------- s20 — Abu Tammam (sajʿ in verse)
S.append({"id": "s20", "translation": {
 "en": "«Through him my RIGHT-GUIDANCE (rushdi) shone, and my HAND (yadi) grew rich; through him my SCANT WATER (thamdi) overflowed, and my FIRE-STICK (zandi) kindled.» (Abu Tammam) — four qarinas that rhyme on the dal: sajʿ in verse." + RB_EN,
 "tr": "«Onunla RÜŞDÜM (rüşdî) açıldı, ELİM (yedî) zengin oldu; onunla AZ SUYUM (semdî) taştı, ÇAKMAĞIM (zendî) ateş çaktı.» (Ebû Temmâm) — dâl üzerinde kafiyeli dört karîne: nazımda seci." + RB_TR},
 "tokens": [
  tok("تَجَلَّى", "tajalla", "verb", [J, "naqis-verbs", "form-v-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنَ التَّفَعُّلِ.", "«shone» — a naqis Form V.", "«açıldı» — nâkıs tefe'ul."),
  bihi(J),
  tok("رُشْدِي", "rushd", "noun", [J, "fail", "idafa-definiteness", "ya-al-mutakallim", "saj"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ — الْفَاصِلَةُ الْأُولَى.", "«my right-guidance» — the doer, its damma hidden before the speaker's ya; the first fasila.", "«rüşdüm» — fâil; mütekellim yâsı önünde damme takdîrî; birinci fâsıla.", punct="،",
      segments=[seg("رُشْدِ", "rushd", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَأَثْرَتْ", "athra", "verb", [J, "atf-nasaq", "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَثْرَتْ مَاضٍ نَاقِصٌ مِنَ الْإِفْعَالِ، حُذِفَتْ أَلِفُهُ لِلتَّاءِ.", "«and grew rich» — Form IV naqis; the alif drops before the feminine ta.", "«ve zengin oldu» — if'âl nâkıs; tâ önünde elif düşer.",
      segments=[seg("وَ", "wa", "conj"), seg("أَثْرَتْ", "athra", "verb")]),
  bihi(J),
  tok("يَدِي", "yad", "noun", [J, "fail", "idafa-definiteness", "ya-al-mutakallim", "saj"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ — الْفَاصِلَةُ الثَّانِيَةُ.", "«my hand» — the doer; the second fasila.", "«elim» — fâil; ikinci fâsıla.",
      segments=[seg("يَدِ", "yad", "noun"), seg("ي", "pron-1s", "pron")], punct="*"),
  tok("وَفَاضَ", "fada", "verb", [J, "atf-nasaq", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَفَاضَ مَاضٍ أَجْوَفُ.", "«and overflowed» — a hollow verb.", "«ve taştı» — ecvef.",
      segments=[seg("وَ", "wa", "conj"), seg("فَاضَ", "fada", "verb")]),
  bihi(J),
  tok("ثَمْدِي", "thamd", "noun", [J, "fail", "idafa-definiteness", "ya-al-mutakallim", "saj"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — الثَّمْدُ: الْمَاءُ الْقَلِيلُ؛ الْفَاصِلَةُ الثَّالِثَةُ.", "«my scant water» — the doer; the third fasila.", "«az suyum» — fâil; üçüncü fâsıla.", punct="،",
      segments=[seg("ثَمْدِ", "thamd", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَأَوْرَى", "awra-kindle", "verb", [J, "atf-nasaq", "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَوْرَى مَاضٍ نَاقِصٌ مِنَ الْإِفْعَالِ: أَخْرَجَ النَّارَ.", "«and kindled» — Form IV naqis: «struck fire».", "«ve ateş çaktı» — if'âl nâkıs.",
      segments=[seg("وَ", "wa", "conj"), seg("أَوْرَى", "awra-kindle", "verb")]),
  bihi(J),
  tok("زَنْدِي", "zand", "noun", [J, "fail", "idafa-definiteness", "ya-al-mutakallim", "saj"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — الزَّنْدُ: عُودُ الْقَدْحِ؛ الْفَاصِلَةُ الرَّابِعَةُ وَالْقَافِيَةُ.", "«my fire-stick» — the doer; the fourth fasila and the rhyme.", "«çakmağım» — fâil; dördüncü fâsıla ve kafiye.",
      segments=[seg("زَنْدِ", "zand", "noun"), seg("ي", "pron-1s", "pron")]),
 ]})
S[-1]["badi"] = [{"kind": "saj", "sub": "mutarraf", "pair": [ix(S[-1], "رُشْدِي"), ix(S[-1], "يَدِي")]},
                 {"kind": "saj", "sub": "mutarraf", "pair": [ix(S[-1], "يَدِي"), ix(S[-1], "ثَمْدِي")]},
                 {"kind": "saj", "sub": "mutawazi", "pair": [ix(S[-1], "ثَمْدِي"), ix(S[-1], "زَنْدِي")]}]

# ----------- s21 — the tashtir (RESTORED)
S.append({"id": "s21", "translation": {
 "en": "And of it is what is called TASHTIR: making each of the two halves of the bayt rhymed on a sajʿ that differs from the sajʿ of the other." + R_EN,
 "tr": "Ondan biri de TAŞTÎR denilendir: beytin iki şatrından her birini, öbürünün secisinden farklı bir seci üzere secili kılmaktır." + R_TR},
 "tokens": [
  tok("وَمِنْهُ", "min", "part", [T, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنْهُ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and of it» — the fronted khabar.", "«ondan biri» — mukaddem haber.",
      segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), seg("هُ", "pron-3ms", "pron")]),
  tok("مَا", "ma-mawsula", "pron", [T, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what» — the delayed mubtada.", "«-en» — muahhar mübtedâ."),
  tok("يُسَمَّى", "samma", "verb", [T, "jumla-sifa", "naib-al-fail", "mafulayn"], "صِلَةُ الْمَوْصُولِ — مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«is called» — the passive; its deputy concealed.", "«denilen» — meçhul; nâibi gizli."),
  tok("التَّشْطِيرَ", "tashtir", "noun", [T, "mafulayn", "masdar"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — مَصْدَرُ شَطَّرَ.", "«tashtir» — the second object; the masdar of «to halve».", "«taştîr» — ikinci mef'ul; şattara'nın masdarı.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [T, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«o da» — mübtedâ.",
      segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("جَعْلُ", "jal-making", "noun", [T, "mubtada-khabar", "idafa-definiteness", "imal-al-masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرٌ عَامِلٌ عَمَلَ فِعْلِهِ.", "«making» — the khabar; a masdar governing like its verb.", "«kılmak» — haber; fiili gibi amel eden masdar."),
  tok("كُلٍّ", "kull", "noun", [T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ.", "«each» — its tanwin stands for a dropped mudaf ilayh.", "«her birini» — tenvin, düşmüş muzâfun ileyhin ivazı."),
  tok("مِنْ", "min", "prep", [T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("شَطْرَيِ", "shatr", "noun", [T, "huruf-jarr", "idafa-definiteness", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ، مُضَافٌ — مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَكُسِرَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«the two halves of» — the annexed dual drops its nun; the ya takes a kasra before the article.", "«iki şatrından» — izâfetle nûnu düşmüş tesniye; yâ elif-lâm önünde kesre."),
  tok("الْبَيْتِ", "bayt", "noun", [T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the bayt».", "«beytin»."),
  tok("مُسَجَّعًا", "musajja", "noun", [T, "imal-al-masdar", "ism-maful", "mafulayn"], "مَفْعُولٌ ثَانٍ لِلْمَصْدَرِ مَنْصُوبٌ — اسْمُ مَفْعُولٍ.", "«rhymed» — the masdar's second object; an ism mafʿul.", "«secili» — masdarın ikinci mef'ulü; ism-i mef'ûl."),
  tok("عَلَى", "ala", "prep", [T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  tok("سَجْعٍ", "saj", "noun", [T, "huruf-jarr"], "مَجْرُورٌ.", "«a sajʿ».", "«bir seci»."),
  tok("يُخَالِفُ", "khalafa", "verb", [T, "jumla-sifa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ لِسَجْعٍ.", "«that differs from» — the clause describes the sajʿ.", "«farklı olan» — cümle sec'in na'tı."),
  tok("سَجْعَ", "saj", "noun", [T, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the sajʿ of» — the object, annexed.", "«secisinden» — mef'ul, muzâf."),
  tok("الْآخَرِ", "akhar", "noun", [T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the other».", "«öbürünün»."),
 ]})

# ----------- s22 — Abu Tammam (tashtir)
S.append({"id": "s22", "translation": {
 "en": "«The planning of one who holds FAST to Allah (muʿtasim), who takes VENGEANCE for Allah (muntaqim) * who DESIRES what is with Allah (murtaghib), who WATCHES for Allah (murtaqib).» (Abu Tammam) — the first half rhymed on the mim, the second on the ba: tashtir." + RB_EN,
 "tr": "«Allah'a SIĞINAN (mu'tasım), Allah için ÖÇ ALAN (müntekım) * Allah'ta olanı DİLEYEN (mürtegıb), Allah'ı GÖZETEN (mürtekıb) bir zâtın tedbiridir.» (Ebû Temmâm) — birinci şatır mîm, ikincisi bâ üzere secili: taştîr." + RB_TR},
 "tokens": [
  tok("تَدْبِيرُ", "tadbir", "noun", [T, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُوَ تَدْبِيرُ، مُضَافٌ — مَصْدَرُ دَبَّرَ.", "«the planning of» — the khabar of a dropped «it is»; annexed.", "«tedbiridir» — düşmüş mübtedânın haberi; muzâf."),
  tok("مُعْتَصِمٍ", "mutasim", "noun", [T, "idafa-definiteness", "ism-fail", "form-viii-verbs", "saj"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ اعْتَصَمَ، وَفِيهِ تَوْرِيَةٌ بِاسْمِ الْخَلِيفَةِ الْمُعْتَصِمِ؛ الْفَاصِلَةُ الْأُولَى عَلَى الْمِيمِ.", "«one who holds fast» — the mudaf ilayh; the ism faʿil of Form VIII, and a tawriya on the caliph's name; the first fasila, on the mim.", "«sığınan» — muzâfun ileyh; iftiâl ism-i fâili, halife Mu'tasım'ın adına tevriye; mîm üzere birinci fâsıla."),
  tok("بِاللهِ", "allah", "noun", [T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — مُتَعَلِّقٌ بِمُعْتَصِمٍ.", "«to Allah».", "«Allah'a».",
      segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "noun")]),
  tok("مُنْتَقِمٍ", "muntaqim", "noun", [T, "naat-sifa", "ism-fail", "form-viii-verbs", "saj"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ انْتَقَمَ؛ الْفَاصِلَةُ الثَّانِيَةُ عَلَى الْمِيمِ.", "«who takes vengeance» — the naʿt; the second fasila, on the mim.", "«öç alan» — na't; mîm üzere ikinci fâsıla.", punct="*"),
  tok("لِلهِ", "allah", "noun", [T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — مُتَعَلِّقٌ بِمُنْتَقِمٍ.", "«for Allah».", "«Allah için».",
      segments=[seg("لِ", "li", "prep"), seg("لهِ", "allah", "noun")]),
  tok("مُرْتَغِبٍ", "murtaghib", "noun", [T, "naat-sifa", "ism-fail", "form-viii-verbs", "saj"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ ارْتَغَبَ؛ الْفَاصِلَةُ الثَّالِثَةُ عَلَى الْبَاءِ.", "«who desires» — the naʿt; the third fasila, on the ba.", "«dileyen» — na't; bâ üzere üçüncü fâsıla."),
  fi(T),
  tok("اللهِ", "allah", "noun", [T, "huruf-jarr"], "مَجْرُورٌ — مُتَعَلِّقٌ بِمُرْتَغِبٍ.", "«Allah» — what is with Him.", "«Allah'ta»."),
  tok("مُرْتَقِبِ", "murtaqib", "noun", [T, "naat-sifa", "ism-fail", "form-viii-verbs", "saj"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ ارْتَقَبَ؛ الْفَاصِلَةُ الرَّابِعَةُ عَلَى الْبَاءِ، وَكُسِرَ لِلرَّوِيِّ بِلَا تَنْوِينٍ.", "«who watches» — the naʿt; the fourth fasila, on the ba; the rhyme's kasra without tanwin.", "«gözeten» — na't; bâ üzere dördüncü fâsıla; revî için tenvinsiz kesre."),
 ]})
S[-1]["badi"] = [{"kind": "tashtir", "first": [ix(S[-1], "مُعْتَصِمٍ"), ix(S[-1], "مُنْتَقِمٍ")], "second": [ix(S[-1], "مُرْتَغِبٍ"), ix(S[-1], "مُرْتَقِبِ")]},
                 {"kind": "saj", "sub": "mutawazi", "pair": [ix(S[-1], "مُعْتَصِمٍ"), ix(S[-1], "مُنْتَقِمٍ")]},
                 {"kind": "saj", "sub": "mutawazi", "pair": [ix(S[-1], "مُرْتَغِبٍ"), ix(S[-1], "مُرْتَقِبِ")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "saj": need("saj", "سَجْع", "س ج ع", "noun", "sajʿ — rhymed prose: the agreement of two fasilas on one letter (pl. أَسْجَاع)", "seci — nesirde iki fâsılanın bir harfte birleşmesi (ç. أَسْجَاع)", 6, plural="أَسْجَاع"),
 "tawatu": need("tawatu", "تَوَاطُؤ", "و ط ء", "noun", "agreement, concurrence (masdar of Form VI تَوَاطَأَ)", "birleşme, uyuşma (tefâul masdarı)", 6),
 "fasila": need("fasila", "فَاصِلَة", "ف ص ل", "noun", "a fasila — the last word of a rhymed clause; in the Qurʾan, the close of an aya (pl. فَوَاصِل)", "fâsıla — secili cümlenin son kelimesi; Kur'ân'da âyet sonu (ç. فَوَاصِل)", 6, plural="فَوَاصِل"),
 "qafiya": need("qafiya", "قَافِيَة", "ق ف و", "noun", "the rhyme of a line of verse (pl. قَوَافٍ)", "kafiye (ç. قَوَافٍ)", 5, plural="قَوَافٍ"),
 "mutarraf": need("mutarraf", "مُطَرَّف", "ط ر ف", "noun", "mutarraf — the sajʿ whose fasilas differ in wazn (ism maf'ul of طَرَّفَ)", "mutarraf — fâsılaları vezince farklı seci (ism-i mef'ûl)", 6),
 "waqar": need("waqar", "وَقَار", "و ق ر", "noun", "gravity, majesty, dignity (a masdar)", "vakar, ağırbaşlılık (masdar)", 4),
 "tawr": need("tawr", "طَوْر", "ط و ر", "noun", "a stage, a state, a turn (pl. أَطْوَار)", "tavır, hâl, merhale (ç. أَطْوَار)", 4, plural="أَطْوَار"),
 "ihda": need("ihda", "إِحْدَى", "ء ح د", "noun", "one (feminine) — the feminine of أَحَد, a maqsur", "biri (müennes) — ehad'ın müennesi, maksûr", 3),
 "taqfiya": need("taqfiya", "تَقْفِيَة", "ق ف و", "noun", "rhyming — giving a clause its qafiya (masdar of قَفَّى)", "kafiyeleme (kaffâ'nın masdarı)", 6),
 "tarsi": need("tarsi", "تَرْصِيع", "ر ص ع", "noun", "tarsiʿ — «jewel-setting»: the sajʿ whose words answer each other in wazn and rhyme (masdar of رَصَّعَ)", "tarsî' — cevher dizme: kelimeleri vezin ve kafiyede karşılıklı seci (masdar)", 6),
 "tabaa": need("tabaa", "طَبَعَ", "ط ب ع", "verb", "to stamp, to imprint, to mint (طَبَعَ يَطْبَعُ)", "damgalamak, basmak (tabaa yatbau)", 4),
 "qaraa-knock": need("qaraa-knock", "قَرَعَ", "ق ر ع", "verb", "to strike, to knock — قَرَعَ الْأَسْمَاعَ: rang in the ears (قَرَعَ يَقْرَعُ; not قَرَأَ «to read»)", "vurmak, çalmak — kulakları çınlatmak (karaa yakrau; kara'e «okumak» değil)", 5),
 "zajir": need("zajir", "زَاجِر", "ز ج ر", "noun", "a rebuke, a deterrent (ism fa'il of زَجَرَ; pl. زَوَاجِر)", "zecreden, caydıran (ism-i fâil; ç. زَوَاجِر)", 5, plural="زَوَاجِر"),
 "waz": need("waz", "وَعْظ", "و ع ظ", "noun", "preaching, admonition (masdar of وَعَظَ)", "vaaz, öğüt (masdar)", 4),
 "mutawazi": need("mutawazi", "مُتَوَازٍ (الْمُتَوَازِي)", "و ز ي", "noun", "mutawazi — «parallel»: the sajʿ whose fasilas alone share a wazn (ism fa'il of تَوَازَى; a manqus)", "mütevâzî — yalnız fâsılaları aynı vezinde seci (ism-i fâil; mankûs)", 6),
 "sarir": need("sarir", "سَرِير", "س ر ر", "noun", "a couch, a throne (pl. سُرُر)", "taht, sedir (ç. سُرُر)", 3, plural="سُرُر"),
 "kub": need("kub", "كُوب", "ك و ب", "noun", "a cup without a handle (pl. أَكْوَاب)", "kulpsuz kap, kadeh (ç. أَكْوَاب)", 3, plural="أَكْوَاب"),
 "mawdua": need("mawdua", "مَوْضُوعَة", "و ض ع", "noun", "set out, placed (ism maf'ul of وَضَعَ, feminine)", "konulmuş (ism-i mef'ûl, müennes)", 3),
 "tasawa": need("tasawa", "تَسَاوَى", "س و ي", "verb", "to be equal to one another (Form VI; تَسَاوَى يَتَسَاوَى)", "eşit olmak, denk olmak (tefâul; tesâvâ yetesâvâ)", 5),
 "sidr": need("sidr", "سِدْر", "س د ر", "noun", "the lote-tree", "sidr ağacı, Arap kirazı", 5),
 "makhdud": need("makhdud", "مَخْضُود", "خ ض د", "noun", "thornless — its thorns cut away (ism maf'ul of خَضَدَ)", "dikeni kesilmiş, dikensiz (ism-i mef'ûl)", 6),
 "talh": need("talh", "طَلْح", "ط ل ح", "noun", "the banana-tree; the acacia", "muz ağacı; akasya", 5),
 "mandud": need("mandud", "مَنْضُود", "ن ض د", "noun", "layered, piled in order (ism maf'ul of نَضَدَ)", "istiflenmiş, üst üste dizilmiş (ism-i mef'ûl)", 6),
 "mamdud": need("mamdud", "مَمْدُود", "م د د", "noun", "extended, stretched out (ism maf'ul of مَدَّ)", "uzatılmış, yayılmış (ism-i mef'ûl)", 4),
 "tala-long": need("tala-long", "طَالَ", "ط و ل", "verb", "to be long, to grow long (hollow; طَالَ يَطُولُ)", "uzun olmak, uzamak (ecvef; tâle yetûlu)", 3),
 "hawa-fall": need("hawa-fall", "هَوَى", "ه و ي", "verb", "to fall, to set (of a star); (naqis; هَوَى يَهْوِي)", "düşmek, batmak (yıldız); (nâkıs; hevâ yehvî)", 4),
 "dalla-stray": need("dalla-stray", "ضَلَّ", "ض ل ل", "verb", "to stray, to go astray (doubled; ضَلَّ يَضِلُّ)", "sapmak, yolunu şaşırmak (muzâaf; dalle yadillu)", 3),
 "ghawa": need("ghawa", "غَوَى", "غ و ي", "verb", "to err, to be seduced from the right (naqis; غَوَى يَغْوِي)", "azmak, doğrudan sapmak (nâkıs; gavâ yagvî)", 4),
 "ghalla": need("ghalla", "غَلَّ", "غ ل ل", "verb", "to shackle, to put in irons (doubled; غَلَّ يَغُلُّ)", "bağlamak, zincire vurmak (muzâaf; galle yagullu)", 5),
 "salla-roast": need("salla-roast", "صَلَّى", "ص ل ي", "verb", "to roast, to cast into fire — صَلَّاهُ النَّارَ (Form II of صَلِيَ; not صَلَّى «to pray»)", "ateşe atmak, yakmak (tef'îl; «namaz kılmak» olan sallâ değil)", 6),
 "aqsar": need("aqsar", "أَقْصَر", "ق ص ر", "noun", "shorter (ism tafdil of قَصِير; a diptote)", "daha kısa (ism-i tafdil; gayr-i munsarif)", 3),
 "mabni": need("mabni", "مَبْنِيّ", "ب ن ي", "noun", "built (ism maf'ul of بَنَى); in nahw: mabni, unchanging in its ending", "bina edilmiş (ism-i mef'ûl); nahivde: mebnî", 4),
 "sukun": need("sukun", "سُكُون", "س ك ن", "noun", "the sukun — the absence of a vowel; stillness (masdar of سَكَنَ)", "sükûn — hareke yokluğu; durgunluk (masdar)", 3),
 "abada-far": need("abada-far", "أَبْعَدَ", "ب ع د", "verb", "to make far; مَا أَبْعَدَ: how far! (Form IV; the verb of wonder)", "uzaklaştırmak; mâ eb'ade: ne uzak! (if'âl; taaccüb fiili)", 4),
 "fata": need("fata", "فَاتَ", "ف و ت", "verb", "to pass away, to be gone, to escape (hollow; فَاتَ يَفُوتُ)", "geçmek, kaçmak, elden gitmek (ecvef; fâte yefûtu)", 4),
 "aqraba": need("aqraba", "أَقْرَبَ", "ق ر ب", "verb", "to bring near; مَا أَقْرَبَ: how near! (Form IV; the verb of wonder)", "yaklaştırmak; mâ akrabe: ne yakın! (if'âl; taaccüb fiili)", 4),
 "atin": need("atin", "آتٍ (الْآتِي)", "ء ت ي", "noun", "coming, what is to come (ism fa'il of أَتَى; a manqus)", "gelen, gelecek olan (ism-i fâil; mankûs)", 4),
 "rushd": need("rushd", "رُشْد", "ر ش د", "noun", "right guidance, maturity of mind", "rüşd, doğru yol, olgunluk", 4),
 "athra": need("athra", "أَثْرَى", "ث ر و", "verb", "to grow rich (Form IV naqis; أَثْرَى يُثْرِي)", "zengin olmak (if'âl nâkıs; esrâ yüsrî)", 5),
 "fada": need("fada", "فَاضَ", "ف ي ض", "verb", "to overflow, to flood (hollow; فَاضَ يَفِيضُ)", "taşmak, dolup taşmak (ecvef; fâda yefîdu)", 4),
 "thamd": need("thamd", "ثَمْد", "ث م د", "noun", "scant water, a little water in the ground", "az su, sızıntı su", 6),
 "awra-kindle": need("awra-kindle", "أَوْرَى", "و ر ي", "verb", "to strike fire, to make (the fire-stick) kindle (Form IV; أَوْرَى يُورِي)", "ateş çakmak, çakmağı tutuşturmak (if'âl; evrâ yûrî)", 6),
 "zand": need("zand", "زَنْد", "ز ن د", "noun", "the fire-stick — the upper stick of the pair rubbed for fire", "zend — ateş çakma çubuğu, çakmak", 6),
 "tashtir": need("tashtir", "تَشْطِير", "ش ط ر", "noun", "tashtir — halving: each half of the bayt rhymed on its own sajʿ (masdar of شَطَّرَ)", "taştîr — beytin her şatrını ayrı bir seciyle secili kılma (masdar)", 6),
 "shatr": need("shatr", "شَطْر", "ش ط ر", "noun", "a half; the half-line of a bayt (pl. أَشْطُر)", "yarım; beytin yarısı, mısra (ç. أَشْطُر)", 4, plural="أَشْطُر"),
 "musajja": need("musajja", "مُسَجَّع", "س ج ع", "noun", "rhymed, made into sajʿ (ism maf'ul of سَجَّعَ)", "secili kılınmış (ism-i mef'ûl)", 6),
 "tadbir": need("tadbir", "تَدْبِير", "د ب ر", "noun", "planning, management, direction (masdar of دَبَّرَ)", "tedbir, idare, düzenleme (masdar)", 3),
 "mutasim": need("mutasim", "مُعْتَصِم", "ع ص م", "noun", "one who holds fast, who takes refuge (ism fa'il of اعْتَصَمَ); al-Muʿtasim — the caliph's name", "sığınan, tutunan (ism-i fâil); Mu'tasım — halifenin adı", 6),
 "muntaqim": need("muntaqim", "مُنْتَقِم", "ن ق م", "noun", "one who takes vengeance (ism fa'il of انْتَقَمَ)", "öç alan, intikam alan (ism-i fâil)", 5),
 "murtaghib": need("murtaghib", "مُرْتَغِب", "ر غ ب", "noun", "one who desires, who seeks eagerly (ism fa'il of ارْتَغَبَ)", "dileyen, rağbet eden (ism-i fâil)", 6),
 "murtaqib": need("murtaqib", "مُرْتَقِب", "ر ق ب", "noun", "one who watches, who awaits (ism fa'il of ارْتَقَبَ)", "gözeten, bekleyen (ism-i fâil)", 6),
}
for k in ("nathr", "harf", "wahid", "huwa", "mana", "qawl", "sakkaki", "fi", "shir", "ka", "in-shartiyya", "ikhtalafa", "wazn", "ma-istifham", "li", "la-nafiya", "raja", "allah", "qad",
          "khalaqa", "illa", "kana", "ma-mawsula", "qarina", "min", "lafz", "aw", "akthar", "mithl", "qabala", "ukhra", "jawhar", "sam", "marfua", "ahsan", "thani", "thumma", "najm",
          "idha", "ma-nafiya", "sahib", "akhadha", "jahim", "hasuna", "an-masdariyya", "kathir", "ala", "ajuz", "ma-taajjub", "qala", "quran", "bal", "ikhtassa", "nazm", "tajalla",
          "bi", "yad", "samma", "jal-making", "kull", "bayt", "khalafa", "akhar", "thalith", "zill", "wa", "fa", "pron-3ms", "pron-2mp", "pron-3fs", "pron-1s"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

# ---------------------------------------------------------------- paradigms
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    # a DOUBLED verb of Form I: the contracted stems (L) and the fakk stems (F) before a sakin ending
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tabaa", _sg.sound1("fataha", "طَبَع", "طْبَع", "اِطْبَع", "طَبْع", "طَابِع", "مَطْبُوع", "طُبِعَ", "يُطْبَعُ"))
put_morph(mo, "qaraa-knock", _sg.sound1("fataha", "قَرَع", "قْرَع", "اِقْرَع", "قَرْع", "قَارِع", "مَقْرُوع", "قُرِعَ", "يُقْرَعُ"))
put_morph(mo, "tasawa", _sg.derived_naqis(_sg.B6, _sg.W6, "َ", "تَسَاوَ", "تَسَاو", "a", "تَسَاو", "تَسَاوٍ (التَّسَاوِي)", "مُتَسَاوٍ (الْمُتَسَاوِي)"))
put_morph(mo, "tala-long", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "طَال", "طُل", "طُول", "طُل", "طُول", "طُل", "طُول", "طَائِل"))
put_morph(mo, "fata", _sg.idgham(_sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "فَات", "فُت", "فُوت", "فُت", "فُوت", "فُت", "فَوْت", "فَائِت")))
put_morph(mo, "fada", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "فَاض", "فِض", "فِيض", "فِض", "فِيض", "فِض", "فَيْض", "فَائِض"))
put_morph(mo, "hawa-fall", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "هَوَ", "هْو", "i", "اِهْو", "هُوِيّ", "هَاوٍ (الْهَاوِي)", note="هَوَى يَهْوِي: سَقَطَ — هَوَى النَّجْمُ: غَابَ."))
put_morph(mo, "ghawa", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "غَوَ", "غْو", "i", "اِغْو", "غَيّ", "غَاوٍ (الْغَاوِي)", None, "غُوِيَ", "يُغْوَى"))
put_morph(mo, "dalla-stray", gem("daraba", "ضَلّ", "ضَلَل", "ضِلّ", "ضْلِل", ["ضِلَّ", "ضِلَّا", "ضِلُّوا", "ضِلِّي", "ضِلَّا", "اِضْلِلْنَ"], "ضَلَال", "ضَالّ", None, None, None,
                                  "مُضَاعَفٌ مِنْ بَابِ ضَرَبَ: ضَلَّ يَضِلُّ — ضَلَلْتُ، يَضْلِلْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ."))
put_morph(mo, "ghalla", gem("nasara", "غَلّ", "غَلَل", "غُلّ", "غْلُل", ["غُلَّ", "غُلَّا", "غُلُّوا", "غُلِّي", "غُلَّا", "اُغْلُلْنَ"], "غَلّ", "غَالّ", "مَغْلُول", "غُلَّ", "يُغَلُّ",
                             "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: غَلَّ يَغُلُّ — غُلُّوهُ: أَمْرٌ مَعَ الضَّمِيرِ."))
put_morph(mo, "salla-roast", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "صَلَّ", "صَلّ", "i", "صَلّ", "تَصْلِيَة", "مُصَلٍّ (الْمُصَلِّي)", "مُصَلًّى", "صُلِّيَ", "يُصَلَّى",
                                                note="صَلَّاهُ النَّارَ: أَدْخَلَهُ فِيهَا — غَيْرُ صَلَّى الصَّلَاةَ."))
put_morph(mo, "abada-far", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْعَد", "بْعِد", "أَبْعِد", "إِبْعَاد", "مُبْعِد", "مُبْعَد", "أُبْعِدَ", "يُبْعَدُ"))
put_morph(mo, "aqraba", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْرَب", "قْرِب", "أَقْرِب", "إِقْرَاب", "مُقْرِب", "مُقْرَب", "أُقْرِبَ", "يُقْرَبُ"))
put_morph(mo, "athra", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَثْرَ", "ثْر", "i", "أَثْر", "إِثْرَاء", "مُثْرٍ (الْمُثْرِي)"))
put_morph(mo, "awra-kindle", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَوْرَ", "ور", "i", "أَوْر", "إِيرَاء", "مُورٍ (الْمُورِي)", note="أَوْرَى الزَّنْدُ: أَخْرَجَ النَّارَ — مِثَالٌ نَاقِصٌ (لَفِيفٌ مَفْرُوقٌ)."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_T = {
 "id": "tashtir",
 "title": {"ar": "التَّشْطِيرُ — شَطْرَانِ عَلَى سَجْعَيْنِ", "en": "The tashtir — two halves on two sajʿs", "tr": "Taştîr — iki şatır, iki seci"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — ومنه ما يسمى التشطير وهو جعل كل من شطري البيت مسجعا على سجع يخالف الآخر"],
 "question": {
  "en": ["Does EACH half of the bayt rhyme within itself — and on a DIFFERENT letter from the other half? That is TASHTIR, «halving»: the first misraʿ of Abu Tammam's bayt closes its two clauses on the mim (مُعْتَصِمٍ … مُنْتَقِمٍ), the second on the ba (مُرْتَغِبٍ … مُرْتَقِبِ). It is filed under the sajʿ because it IS sajʿ inside verse — the qil that sajʿ is not confined to prose.",
         "What does the engine read? It cuts the bayt at the hemistich mark, reads a sajʿ inside each half with the same reader the prose uses, and requires the two rawi letters to differ — one rawi across both halves is plain sajʿ in verse, not tashtir."],
  "tr": ["Beytin HER yarısı kendi içinde — ve öbüründen FARKLI bir harfle — secili mi? Bu TAŞTÎR'dir, «yarımlama»: Ebû Temmâm'ın beytinin birinci mısraı iki cümlesini mîm ile kapatır (مُعْتَصِمٍ … مُنْتَقِمٍ), ikincisi bâ ile (مُرْتَغِبٍ … مُرْتَقِبِ). Seci babında sayılır; çünkü nazım içindeki secidir — secinin nesre mahsus olmadığı görüşü.",
         "Motor neyi okur? Beyti mısra işaretinden keser, her yarıda nesrin okuyucusuyla bir seci okur ve iki revî harfinin farklı olmasını ister — iki yarıda tek revî, nazımda düz secidir, taştîr değil."]},
 "plain": {
  "en": "Each half of the bayt rhymed on its own sajʿ, the two rhymes on different letters — Abu Tammam's mim-half and ba-half.",
  "tr": "Beytin her yarısı kendi secisiyle, iki seci farklı harflerde — Ebû Temmâm'ın mîm yarısı ve bâ yarısı."},
 "explanation": {
  "en": "وَمِنْهُ مَا يُسَمَّى التَّشْطِيرَ، وَهُوَ جَعْلُ كُلٍّ مِنْ شَطْرَيِ الْبَيْتِ مُسَجَّعًا عَلَى سَجْعٍ يُخَالِفُ سَجْعَ الْآخَرِ — the sajʿ chapter closes on the one shape that lives only in verse: a bayt whose halves are each a rhymed fiqra of their own, and whose two rhymes disagree. Abu Tammam's praise of al-Muʿtasim (the caliph's name sits inside the first word as a tawriya) runs مُعْتَصِمٍ بِاللهِ مُنْتَقِمٍ on the mim, then لِلهِ مُرْتَغِبٍ فِي اللهِ مُرْتَقِبِ on the ba — four participles of Form VIII, each with its jarr phrase, the rhyme word of the bayt closing on the rawi's bare kasra.",
  "tr": "وَمِنْهُ مَا يُسَمَّى التَّشْطِيرَ، وَهُوَ جَعْلُ كُلٍّ مِنْ شَطْرَيِ الْبَيْتِ مُسَجَّعًا عَلَى سَجْعٍ يُخَالِفُ سَجْعَ الْآخَرِ — seci babı, yalnız nazımda yaşayan bir şekille kapanır: yarıları her biri kendi secili fıkrası olan ve iki secisi birbirini tutmayan beyit. Ebû Temmâm'ın Mu'tasım methi (halifenin adı ilk kelimede tevriye olarak durur) مُعْتَصِمٍ بِاللهِ مُنْتَقِمٍ ile mîm üzere, sonra لِلهِ مُرْتَغِبٍ فِي اللهِ مُرْتَقِبِ ile bâ üzere akar — iftiâl bâbından dört ism-i fâil, her biri câr-mecrûruyla; beytin kafiye kelimesi revînin çıplak kesresiyle kapanır."},
 "examples": [
  {"ar": "تَدْبِيرُ مُعْتَصِمٍ بِاللهِ مُنْتَقِمٍ * لِلهِ مُرْتَغِبٍ فِي اللهِ مُرْتَقِبِ", "en": "Abu Tammam — the mim-half and the ba-half.", "tr": "Ebû Temmâm — mîm yarısı ve bâ yarısı.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"},
  {"ar": "تَجَلَّى بِهِ رُشْدِي وَأَثْرَتْ بِهِ يَدِي * وَفَاضَ بِهِ ثَمْدِي وَأَوْرَى بِهِ زَنْدِي", "en": "Abu Tammam — sajʿ in verse on ONE rawi: not a tashtir.", "tr": "Ebû Temmâm — TEK revî üzere nazımda seci: taştîr değil.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"}],
 "commonMistakes": [
  {"wrong": "«Beytin dört fâsılası kafiyeli: taştîr vardır»",
   "right": "«Taştîr, iki yarının İKİ AYRI seci üzere olmasıdır; dört fâsıla tek harfte birleşirse nazımda düz secidir»",
   "why": {"en": "The name says «halving»: two halves, two rhymes. One rhyme across the bayt is the sajʿ-in-verse the qil allows.", "tr": "Ad «yarımlama» der: iki yarı, iki kafiye. Beyit boyunca tek kafiye, görüşün câiz gördüğü nazımdaki secidir."}}],
 "relatedNotes": ["saj", "radd-al-ajuz", "jinas", "ilm-al-badi"]}

ADD_EN = (" Chapter 71 (lines ~4532-4568, sahifa 157-158) is the sajʿ: its definition and al-Sakkaki's saying (s1-s2), the mutarraf (s3; 71:13-14 s4), "
          "the tarsiʿ (s5; al-Hariri s6), the mutawazi (s7; 88:13-14 s8), the finest sajʿ by the qarinas' length (s9; 56:28-30 s10; s11; 53:1-2 s12; "
          "s13; 69:30-31 s14; s15), the pausal sukun (s16; the Arabs' saying s17), the two qils (s18-s19; Abu Tammam s20) and the tashtir (s21; Abu "
          "Tammam s22). The rulings are RESTORED from the received matn and marked; the examples are the source's printed Arabic, the two bayts "
          "restored from their Turkish paraphrase with the rhyme words the source prints. The `badi` frames of kind `saj` carry `sub` (mutarraf, "
          "murassa, mutawazi), the `pair` of fasilas and, where the chapter grades the length, `kind2` (equal, second-longer, third-longer); the "
          "tashtir frame carries `first` and `second`; al-Hariri's line is the tarsiʿ (a sajʿ murassaʿ), not a muwazana — its fasilas rhyme. The two "
          "sukun-built closes of s17 (فَاتْ، آتْ) are the received pausal spelling.")
ADD_TR = (" Yetmiş birinci bâb (satır ~4532-4568, sahife 157-158) secidir: tarifi ve Sekkâkî'nin sözü (s1-s2), mutarraf (s3; Nûh 13-14 s4), tarsî' "
          "(s5; Harîrî s6), mütevâzî (s7; Gâşiye 13-14 s8), karînelerin uzunluğuna göre en güzel seci (s9; Vâkıa 28-30 s10; s11; Necm 1-2 s12; s13; "
          "Hâkka 30-31 s14; s15), vakıf sükûnu (s16; Arapların sözü s17), iki görüş (s18-s19; Ebû Temmâm s20) ve taştîr (s21; Ebû Temmâm s22). "
          "Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; örnekler kaynağın basılı Arapçasıdır, iki beyit kaynağın verdiği kafiye "
          "kelimeleriyle Türkçe özetinden geri yazılmıştır. `saj` cinsinden `badi` çerçeveleri `sub` (mutarraf, murassa, mütevâzî), fâsıla `pair`i ve "
          "bâbın uzunluğu derecelendirdiği yerde `kind2` (equal, second-longer, third-longer) taşır; taştîr çerçevesi `first` ve `second` taşır; "
          "Harîrî'nin cümlesi tarsî'dir (murassa' seci), muvâzene değil — fâsılaları kafiyelidir. s17'nin sükûnla kapanan iki sonu "
          "(فَاتْ، آتْ) alınan vakıf imlâsıdır.")
write_out(71, S, TITLE, ADD_EN, ADD_TR, "4532-4568", GLOSS_ADD, notes=(NOTE_T,),
          related=(("saj", ["tashtir"]), ("radd-al-ajuz", ["tashtir"]), ("ilm-al-badi", ["tashtir"])))
report(71, S, GLOSS_ADD, (NOTE_T,))
