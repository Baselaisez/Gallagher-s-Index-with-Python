# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 72: the MUWAZANA and its MUMATHALA (the fasilas agree in wazn, not in rhyme; most words answering),
the QALB (the line reads the same from its last letter), the TASHRIʿ (a bayt on two rhymes), LUZUM MA LA YALZAM (the letter before the
rawi kept), and the closing principle of the lafzi embellishments: the words follow the meanings. Source lines ~4569-4612 (sahifa 158-159).

  RESTORED (the source carries the rule only in Turkish): s1, s3, s6, s9, s11, s16 — the received matn, marked sentence by sentence.
  The examples are the source's own printed Arabic: 88:15-16 (s2), 37:117-118 (s4), Abu Tammam (s5), al-Arrajani (s7), 74:3 (s8),
  al-Hariri (s10), 93:9-10 (s12), Abu Tammam's three bayts (s13-s15).

  python3 tools/authoring/author_talkhis_ch72.py
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

M = "muwazana"
Q = "qalb-al-kull"
T = "tashri"
L = "luzum-ma-la-yalzam"
TITLE = {"ar": "الْمُوَازَنَةُ وَالْقَلْبُ وَالتَّشْرِيعُ وَلُزُومُ مَا لَا يَلْزَمُ", "en": "The muwazana, the qalb, the tashriʿ and luzum ma la yalzam", "tr": "Muvâzene, kalb, teşrî' ve lüzûm-i mâ lâ yelzem"}
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
def fi(tag, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def pr3ms(): return seg("هُ", "pron-3ms", "pron")

# ----------- s1 — the muwazana (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "And the MUWAZANA is the equality of the two fasilas in WAZN without the rhyme." + R_EN,
 "tr": "MUVÂZENE, iki fâsılanın kafiye olmaksızın VEZİNDE eşit olmasıdır." + R_TR},
 "tokens": [
  tok("وَالْمُوَازَنَةُ", "muwazana", "noun", [M, "mubtada-khabar", "masdar", "form-iii-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُوَازَنَةُ مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ وَازَنَ.", "«and the muwazana» — the mubtada; the masdar of Form III.", "«ve muvâzene» — mübtedâ; mufâale masdarı.",
      segments=[seg("وَ", "wa", "conj"), seg("الْمُوَازَنَةُ", "muwazana", "noun")]),
  tok("تَسَاوِي", "tasawi", "noun", [M, "mubtada-khabar", "idafa-definiteness", "masdar", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — مَصْدَرُ تَسَاوَى، مَنْقُوصٌ يَرُدُّ يَاءَهُ فِي الْإِضَافَةِ.", "«the equality of» — the khabar; the manqus keeps its ya as a mudaf.", "«eşitliği» — haber; mankûs, muzâf olunca yâsını korur."),
  tok("الْفَاصِلَتَيْنِ", "fasila", "noun", [M, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«the two fasilas» — the dual in jarr.", "«iki fâsılanın» — tesniye, mecrur."),
  fi(M),
  tok("الْوَزْنِ", "wazn", "noun", [M, "huruf-jarr"], "مَجْرُورٌ.", "«wazn».", "«vezinde»."),
  tok("دُونَ", "duna", "noun", [M, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«without» — the zarf.", "«-sız» — zarf, muzâf."),
  tok("التَّقْفِيَةِ", "taqfiya", "noun", [M, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the rhyme».", "«kafiye»."),
 ]})

# ----------- s2 — 88:15-16
S.append({"id": "s2", "translation": {
 "en": "«And cushions RANGED (masfufa), and carpets SPREAD (mabthutha)» (88:15-16) — masfufa and mabthutha share the wazn مَفْعُولَة and end on different letters (fa, tha): a muwazana, not a sajʿ.",
 "tr": "«Ve sıra sıra DİZİLMİŞ (masfûfe) yastıklar, ve SERİLMİŞ (mebsûse) döşekler» (Gâşiye 15-16) — masfûfe ile mebsûse مَفْعُولَة veznini paylaşır, farklı harflerle biter (fâ, sâ): muvâzene, seci değil."},
 "tokens": [
  tok("وَنَمَارِقُ", "numruqa", "noun", [M, "mubtada-khabar", "jam-taksir", "mamnu-min-sarf", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَنَمَارِقُ مُبْتَدَأٌ مَرْفُوعٌ مُؤَخَّرٌ — جَمْعُ نُمْرُقَةٍ، صِيغَةُ مُنْتَهَى الْجُمُوعِ لَا تُنَوَّنُ.", "«and cushions» — the delayed mubtada; the plural of نُمْرُقَة, a diptote.", "«ve yastıklar» — muahhar mübtedâ; نُمْرُقَة'nin cem'i, gayr-ı munsarif.",
      segments=[seg("وَ", "wa", "conj"), seg("نَمَارِقُ", "numruqa", "noun")]),
  tok("مَصْفُوفَةٌ", "masfufa", "noun", [M, "naat-sifa", "ism-maful", "saj"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ صَفَّ؛ الْفَاصِلَةُ الْأُولَى.", "«ranged» — the naʿt; the first fasila.", "«dizilmiş» — na't; birinci fâsıla.", punct="،"),
  tok("وَزَرَابِيُّ", "zarbiyya", "noun", [M, "mubtada-khabar", "jam-taksir", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَزَرَابِيُّ مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ زَرْبِيَّةٍ.", "«and carpets» — joined; the plural of زَرْبِيَّة.", "«ve döşekler» — atıf; زَرْبِيَّة'nin cem'i.",
      segments=[seg("وَ", "wa", "conj"), seg("زَرَابِيُّ", "zarbiyya", "noun")]),
  tok("مَبْثُوثَةٌ", "mabthutha", "noun", [M, "naat-sifa", "ism-maful", "saj"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ بَثَّ؛ الْفَاصِلَةُ الثَّانِيَةُ.", "«spread» — the naʿt; the second fasila.", "«serilmiş» — na't; ikinci fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "muwazana", "pair": [ix(S[-1], "مَصْفُوفَةٌ"), ix(S[-1], "مَبْثُوثَةٌ")]}]

# ----------- s3 — the mumathala (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "So if what is in one of the two qarinas of words, or most of it, is like what faces it in the other in WAZN, it is singled out with the name MUMATHALA." + R_EN,
 "tr": "İki karîneden birindeki lafızlar yahut çoğu, öbüründe karşısına düşenin VEZİNCE misli olursa, MÜMÂSELE adıyla ayrılır." + R_TR},
 "tokens": [
  tok("فَإِنْ", "in-shartiyya", "part", [M, "in-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if» — the conditional.", "«eğer» — şart edatı.",
      segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [M, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ — مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«is» — the shart verb, of the kana family.", "«ise» — şart fiili, kâne."),
  tok("مَا", "ma-mawsula", "pron", [M, "ism-mawsul", "kana-wa-akhawatuha"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«what» — the relative, ism of كَانَ.", "«…olan şey» — ism-i mevsûl, kâne'nin ismi."),
  fi(M),
  tok("إِحْدَى", "ihda", "noun", [M, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مَقْصُورٌ.", "«one of» — the maqsur, annexed.", "«birinde» — maksûr, muzâf."),
  tok("الْقَرِينَتَيْنِ", "qarina", "noun", [M, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two qarinas».", "«iki karînenin»."),
  tok("مِنَ", "min", "prep", [M, "huruf-jarr"], "حَرْفُ جَرٍّ — بَيَانِيَّةٌ.", "«of» — explanatory.", "«-den» — beyâniyye."),
  tok("الْأَلْفَاظِ", "lafz", "noun", [M, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ لَفْظٍ.", "«words».", "«lafızlardan»."),
  tok("أَوْ", "aw", "conj", [M, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("أَكْثَرُهُ", "akthar", "noun", [M, "atf-nasaq", "ism-tafdil"], "مَعْطُوفٌ عَلَى مَا مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«most of it» — joined to مَا.", "«çoğu» — mâ'ya atıf.",
      segments=[seg("أَكْثَرُ", "akthar", "noun"), pr3ms()]),
  tok("مِثْلَ", "mithl", "noun", [M, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«like» — the khabar of كَانَ.", "«misli» — kâne'nin haberi."),
  tok("مَا", "ma-mawsula", "pron", [M, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the mudaf ilayh.", "«…olanın» — muzâfun ileyh."),
  tok("يُقَابِلُهُ", "qabala", "verb", [M, "jumla-sifa", "maful-bihi", "form-iii-verbs"], "صِلَةُ الْمَوْصُولِ — مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«faces it» — the sila.", "«ona karşı düşen» — sıla.",
      segments=[seg("يُقَابِلُ", "qabala", "verb"), pr3ms()]),
  tok("مِنَ", "min", "prep", [M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْأُخْرَى", "ukhra", "noun", [M, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«the other».", "«öbüründe»."),
  fi(M),
  tok("الْوَزْنِ", "wazn", "noun", [M, "huruf-jarr"], "مَجْرُورٌ.", "«wazn».", "«vezinde»."),
  tok("خُصَّ", "khassa-verb", "verb", [M, "in-shartiyya", "naib-al-fail", "doubled-verbs"], "جَوَابُ الشَّرْطِ — مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«it is singled out» — the jawab; the passive of the doubled خَصَّ, its deputy hidden.", "«ayrılır» — cevap; muzâaf خَصَّ'nin meçhulü, nâibi gizli."),
  tok("بِاسْمِ", "ism", "noun", [M, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمِ مَجْرُورٌ، مُضَافٌ.", "«with the name of».", "«adıyla».",
      segments=[seg("بِ", "bi", "prep"), seg("اسْمِ", "ism", "noun")]),
  tok("الْمُمَاثَلَةِ", "mumathala", "noun", [M, "idafa-definiteness", "masdar", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ مَاثَلَ.", "«the mumathala» — the masdar of Form III.", "«mümâsele» — mufâale masdarı."),
 ]})

# ----------- s4 — 37:117-118 (mumathala)
S.append({"id": "s4", "translation": {
 "en": "«And We gave the two of them the CLEAR (mustabin) Book, and We guided the two of them to the STRAIGHT (mustaqim) path» (37:117-118) — kitab/sirat, mustabin/mustaqim answer each other in wazn: a mumathala.",
 "tr": "«Ve ikisine AÇIK (müstebîn) Kitab'ı verdik, ve ikisini DOĞRU (müstakîm) yola ilettik» (Sâffât 117-118) — kitâb/sırât, müstebîn/müstakîm vezince karşılıklıdır: mümâsele."},
 "tokens": [
  tok("وَآتَيْنَاهُمَا", "aata", "verb", [M, "fail", "maful-bihi", "mafulayn", "form-iv-verbs", "naqis-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَآتَيْنَا مَاضٍ نَاقِصٌ مِنَ الْإِفْعَالِ، وَنَا فَاعِلٌ، وَهُمَا مَفْعُولٌ بِهِ أَوَّلُ.", "«and We gave the two of them» — Form IV آتَى, two objects; the pronoun is the first.", "«ve ikisine verdik» — if'âl âtâ, iki mef'ûl; zamir birincisi.",
      segments=[seg("وَ", "wa", "conj"), seg("آتَيْنَا", "aata", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  tok("الْكِتَابَ", "kitab", "noun", [M, "mafulayn", "saj"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«the Book» — the second object.", "«Kitab'ı» — ikinci mef'ûl."),
  tok("الْمُسْتَبِينَ", "mustabin", "noun", [M, "naat-sifa", "ism-fail", "form-x-verbs", "saj"], "نَعْتٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنَ اسْتَبَانَ؛ الْفَاصِلَةُ الْأُولَى.", "«the clear» — the naʿt; the first fasila.", "«açık» — na't; birinci fâsıla.", punct="،"),
  tok("وَهَدَيْنَاهُمَا", "hada", "verb", [M, "fail", "maful-bihi", "atf-nasaq", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَهَدَيْنَا مَاضٍ نَاقِصٌ، وَنَا فَاعِلٌ، وَهُمَا مَفْعُولٌ بِهِ أَوَّلُ.", "«and We guided the two of them» — joined; the pronoun the first object.", "«ve ikisini ilettik» — atıf; zamir birinci mef'ûl.",
      segments=[seg("وَ", "wa", "conj"), seg("هَدَيْنَا", "hada", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  tok("الصِّرَاطَ", "sirat", "noun", [M, "mafulayn", "saj"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — هَدَى يَتَعَدَّى إِلَى الثَّانِي بِنَفْسِهِ.", "«the path» — the second object; هَدَى reaches it directly.", "«yola» — ikinci mef'ûl; hedâ doğrudan ulaşır."),
  tok("الْمُسْتَقِيمَ", "mustaqim", "noun", [M, "naat-sifa", "ism-fail", "form-x-verbs", "saj"], "نَعْتٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنَ اسْتَقَامَ؛ الْفَاصِلَةُ الثَّانِيَةُ.", "«the straight» — the naʿt; the second fasila.", "«doğru» — na't; ikinci fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "muwazana", "sub": "mumathala", "pair": [ix(S[-1], "الْمُسْتَبِينَ"), ix(S[-1], "الْمُسْتَقِيمَ")]}]

# ----------- s5 — Abu Tammam (mumathala)
S.append({"id": "s5", "translation": {
 "en": "«Wild oryxes — except that THESE are companionable; * spears of al-Khatt — except that THOSE are withered.» (Abu Tammam) — maha/qana, wahsh/khatt, awanis/dhawabil answer in wazn: a mumathala.",
 "tr": "«Yaban ceylanları — şu kadar ki BUNLAR munistir; * Hatt mızrakları — şu kadar ki ONLAR solgundur.» (Ebû Temmâm) — mehâ/kanâ, vahş/hatt, evânis/zevâbil vezince karşılıklı: mümâsele."},
 "tokens": [
  tok("مَهَا", "maha-oryx", "noun", [M, "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُنَّ مَهَا — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«oryxes» — the khabar of an omitted «they are»; the maqsur, annexed.", "«ceylanlar» — hazfedilmiş «onlar»ın haberi; maksûr, muzâf."),
  tok("الْوَحْشِ", "wahsh", "noun", [M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of the wild».", "«yabanın»."),
  tok("إِلَّا", "illa", "part", [M, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُنْقَطِعٍ: بِمَعْنَى لَكِنَّ.", "«except that» — a disjoined exception: «but».", "«şu kadar ki» — munkatı' istisnâ: lâkin."),
  tok("أَنَّ", "anna", "part", [M, "inna-wa-akhawatuha", "istithna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«that».", "«ki»."),
  tok("هَاتَا", "hata", "pron", [M, "inna-wa-akhawatuha", "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمُؤَنَّثِ (هَذِهِ) مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«these» — the feminine demonstrative, ism of أَنَّ.", "«bunlar» — müennes ism-i işâret, enne'nin ismi."),
  tok("أَوَانِسُ", "anisa", "noun", [M, "inna-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf", "saj"], "خَبَرُ أَنَّ مَرْفُوعٌ — جَمْعُ آنِسَةٍ، لَا يُنَوَّنُ؛ الْفَاصِلَةُ الْأُولَى.", "«companionable» — the khabar of أَنَّ; a diptote plural; the first fasila.", "«munis» — enne'nin haberi; gayr-ı munsarif cem'; birinci fâsıla.", punct="*"),
  tok("قَنَا", "qana", "noun", [M, "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هِيَ قَنَا — مَقْصُورٌ، مُضَافٌ.", "«spears» — the khabar of an omitted «they are»; annexed.", "«mızraklar» — hazfedilmiş «onlar»ın haberi; muzâf."),
  tok("الْخَطِّ", "khatt-place", "noun", [M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْخَطُّ: مَوْضِعٌ تُنْسَبُ إِلَيْهِ الرِّمَاحُ.", "«of al-Khatt» — the place the spears are named for.", "«Hatt'ın» — mızrakların nispet edildiği yer."),
  tok("إِلَّا", "illa", "part", [M, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُنْقَطِعٍ.", "«except that».", "«şu kadar ki»."),
  tok("أَنَّ", "anna", "part", [M, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«that».", "«ki»."),
  tok("تِلْكَ", "tilka", "pron", [M, "inna-wa-akhawatuha", "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«those» — ism of أَنَّ.", "«onlar» — enne'nin ismi."),
  tok("ذَوَابِلُ", "dhabil", "noun", [M, "inna-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf", "saj"], "خَبَرُ أَنَّ مَرْفُوعٌ — جَمْعُ ذَابِلٍ، لَا يُنَوَّنُ؛ الْفَاصِلَةُ الثَّانِيَةُ.", "«withered» — the khabar of أَنَّ; a diptote plural; the second fasila.", "«solgun» — enne'nin haberi; gayr-ı munsarif; ikinci fâsıla."),
 ]})
S[-1]["badi"] = [{"kind": "muwazana", "sub": "mumathala", "pair": [ix(S[-1], "أَوَانِسُ"), ix(S[-1], "ذَوَابِلُ")]}]

# ----------- s6 — the qalb (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And the QALB is that the wording be read from its end as it is read from its beginning." + R_EN,
 "tr": "KALB, lafzın sonundan başından okunduğu gibi okunmasıdır." + R_TR},
 "tokens": [
  tok("وَالْقَلْبُ", "qalb-figure", "noun", [Q, "mubtada-khabar", "masdar", "atf-nasaq"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْقَلْبُ مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ قَلَبَ.", "«and the qalb» — the mubtada; «reversal».", "«ve kalb» — mübtedâ; «tersine çevirme».",
      segments=[seg("وَ", "wa", "conj"), seg("الْقَلْبُ", "qalb-figure", "noun")]),
  tok("أَنْ", "an-masdariyya", "part", [Q, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar clause is the khabar.", "«-ması» — te'vîlli masdar haberdir."),
  tok("يُقْرَأَ", "qaraa", "verb", [Q, "an-masdariyya", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be read» — the passive, in nasb by أَنْ.", "«okunması» — meçhul, en ile mansub."),
  tok("اللَّفْظُ", "lafz", "noun", [Q, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the wording» — the deputy doer.", "«lafız» — nâib-i fâil."),
  tok("مِنْ", "min", "prep", [Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("آخِرِهِ", "akhir", "noun", [Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end».", "«sonundan».",
      segments=[seg("آخِرِ", "akhir", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("كَمَا", "kama", "part", [Q, "huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ جَرٍّ وَمَا مَصْدَرِيَّةٌ: كَقِرَاءَتِهِ.", "«as» — the kaf with the masdar-ma.", "«gibi» — kâf ile masdariyye mâ.",
      segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  tok("يُقْرَأُ", "qaraa", "verb", [Q, "naib-al-fail", "mudari-marfu"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«it is read» — the passive, its deputy hidden.", "«okunur» — meçhul, nâibi gizli."),
  tok("مِنْ", "min", "prep", [Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("أَوَّلِهِ", "awwal", "noun", [Q, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its beginning».", "«başından».",
      segments=[seg("أَوَّلِ", "awwal", "noun"), seg("هِ", "pron-3ms", "pron")]),
 ]})
S[-1]["badi"] = [{"kind": "tibaq", "sub": "ijab", "pair": [ix(S[-1], "آخِرِهِ"), ix(S[-1], "أَوَّلِهِ")]}]

# ----------- s7 — al-Arrajani
S.append({"id": "s7", "translation": {
 "en": "«His love endures through every terror * — and does everyone's love endure?» (al-Arrajani) — read the letters backwards and the line returns: a qalb of the whole.",
 "tr": "«Onun sevgisi her korkuda sürer * — ya herkesin sevgisi sürer mi?» (Errecânî) — harfler tersten okununca mısra aynen döner: bütünün kalbi."},
 "tokens": [
  tok("مَوَدَّتُهُ", "mawadda", "noun", [Q, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his love» — the mubtada.", "«onun sevgisi» — mübtedâ.",
      segments=[seg("مَوَدَّتُ", "mawadda", "noun"), pr3ms()]),
  tok("تَدُومُ", "dama", "verb", [Q, "mubtada-khabar", "hollow-verbs", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«endures» — the verb clause is the khabar.", "«sürer» — fiil cümlesi haberdir."),
  tok("لِكُلِّ", "kull", "noun", [Q, "huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ، مُضَافٌ.", "«through every».", "«her … -da».",
      segments=[seg("لِ", "li", "prep"), seg("كُلِّ", "kull", "noun")]),
  tok("هَوْلٍ", "hawl", "noun", [Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«terror».", "«korkuda».", punct="*"),
  tok("وَهَلْ", "hal-istifham", "part", [Q, "al-istifham"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهَلْ حَرْفُ اسْتِفْهَامٍ.", "«and does…?» — the question particle.", "«ya … mı?» — istifham harfi.",
      segments=[seg("وَ", "wa", "conj"), seg("هَلْ", "hal-istifham", "part")]),
  tok("كُلٌّ", "kull", "noun", [Q, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — نُوِّنَ لِقَطْعِهِ عَنِ الْإِضَافَةِ: كُلُّ أَحَدٍ.", "«everyone» — the mubtada; its tanwin stands for the cut annex.", "«herkes» — mübtedâ; tenvîni kesilen izâfetin yerinedir."),
  tok("مَوَدَّتُهُ", "mawadda", "noun", [Q, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his love» — the second mubtada.", "«sevgisi» — ikinci mübtedâ.",
      segments=[seg("مَوَدَّتُ", "mawadda", "noun"), pr3ms()]),
  tok("تَدُومُ", "dama", "verb", [Q, "mubtada-khabar", "hollow-verbs", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — خَبَرُ الثَّانِي، وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.", "«endures» — the khabar of the second, the whole the khabar of the first.", "«sürer» — ikincinin haberi; cümle birincinin haberi."),
 ]})
S[-1]["badi"] = [{"kind": "qalb-kull", "pair": [0, len(S[-1]["tokens"]) - 1]}]

# ----------- s8 — 74:3
S.append({"id": "s8", "translation": {
 "en": "«And your Lord — magnify!» (74:3) — rabbaka fakabbir: ر ب ك ف ك ب ر, the same letters from either end.",
 "tr": "«Ve Rabbini yücelt!» (Müddessir 3) — rabbeke fekebbir: ر ب ك ف ك ب ر, iki uçtan aynı harfler."},
 "tokens": [
  tok("وَرَبَّكَ", "rabb", "noun", [Q, "maful-bihi", "idafa-definiteness", "taqdim-al-musnad"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَرَبَّ مَفْعُولٌ بِهِ مُقَدَّمٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ (اشْتِغَالٌ)، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«and your Lord» — the fronted object of an elided verb the next one explains (ishtighal).", "«ve Rabbini» — hazfedilmiş bir fiilin öne alınmış mef'ûlü, sonraki açıklar (iştigâl).",
      segments=[seg("وَ", "wa", "conj"), seg("رَبَّ", "rabb", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("فَكَبِّرْ", "kabbara", "verb", [Q, "imperative-amr", "form-ii-verbs"], "الْفَاءُ زَائِدَةٌ (أَوْ رَابِطَةٌ لِجَوَابِ أَمَّا الْمُقَدَّرَةِ)، وَكَبِّرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«magnify!» — the amr of Form II; the fa is extra (or answers an estimated أَمَّا).", "«yücelt!» — tef'îl emri; fâ zâidedir (yahut takdîrî emmâ'nın cevabı).",
      segments=[seg("فَ", "fa", "conj"), seg("كَبِّرْ", "kabbara", "verb")]),
 ]})
S[-1]["badi"] = [{"kind": "qalb-kull", "pair": [0, 1]}]

# ----------- s9 — the tashriʿ (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "And the TASHRIʿ is the building of the bayt upon two rhymes, the sense being sound at a stop upon either of them." + R_EN,
 "tr": "TEŞRÎ', beytin iki kafiye üzerine kurulması ve her birinde durulunca mananın tam olmasıdır." + R_TR},
 "tokens": [
  tok("وَالتَّشْرِيعُ", "tashri", "noun", [T, "mubtada-khabar", "masdar", "form-ii-verbs", "atf-nasaq"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالتَّشْرِيعُ مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ شَرَّعَ.", "«and the tashriʿ» — the mubtada; the masdar of Form II.", "«ve teşrî'» — mübtedâ; tef'îl masdarı.",
      segments=[seg("وَ", "wa", "conj"), seg("التَّشْرِيعُ", "tashri", "noun")]),
  tok("بِنَاءُ", "bina", "noun", [T, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the building of» — the khabar.", "«kurulması» — haber, muzâf."),
  tok("الْبَيْتِ", "bayt", "noun", [T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the bayt».", "«beytin»."),
  tok("عَلَى", "ala", "prep", [T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  tok("قَافِيَتَيْنِ", "qafiya", "noun", [T, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two rhymes».", "«iki kafiye»."),
  tok("يَصِحُّ", "sahha", "verb", [T, "jumla-sifa", "doubled-verbs", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِفَةٌ لِقَافِيَتَيْنِ.", "«is sound» — the clause describes the two rhymes.", "«tam olur» — cümle iki kafiyenin sıfatı."),
  tok("الْمَعْنَى", "mana", "noun", [T, "fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the sense» — the doer.", "«mana» — fâil."),
  tok("عِنْدَ", "inda", "noun", [T, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«at».", "«-de» — zarf."),
  tok("الْوُقُوفِ", "wuquf", "noun", [T, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ وَقَفَ.", "«the stop».", "«durulunca»."),
  tok("عَلَى", "ala", "prep", [T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerinde»."),
  tok("كُلٍّ", "kull", "noun", [T, "huruf-jarr"], "مَجْرُورٌ — نُوِّنَ لِقَطْعِهِ عَنِ الْإِضَافَةِ.", "«each» — its tanwin for the cut annex.", "«her biri»."),
  tok("مِنْهُمَا", "min", "part", [T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of the two».", "«ikisinden».",
      segments=[seg("مِنْ", "min", "prep"), seg("هُمَا", "pron-3d", "pron")]),
 ]})

# ----------- s10 — al-Hariri (tashriʿ)
S.append({"id": "s10", "translation": {
 "en": "«O suitor of the base world — it is * the snare of ruin and the seat of sorrows.» (al-Hariri) — stop at «the base» (al-daniyya) or at «sorrows» (al-akdar): either way the sense is whole.",
 "tr": "«Ey alçak dünyanın tâlibi — o, * helâk tuzağı ve kederlerin karargâhıdır.» (Harîrî) — «alçak»ta (ed-deniyye) yahut «kederler»de (el-ekdâr) durulsun, mana tamdır."},
 "tokens": [
  tok("يَا", "ya", "part", [T, "vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("خَاطِبَ", "khatib", "noun", [T, "vocative-munada", "idafa-definiteness", "ism-fail"], "مُنَادًى مُضَافٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ خَطَبَ: طَلَبَ.", "«suitor of» — the annexed munada, in nasb.", "«tâlibi» — muzâf münâdâ, mansub."),
  tok("الدُّنْيَا", "dunya", "noun", [T, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the world».", "«dünyanın»."),
  tok("الدَّنِيَّةِ", "daniyya", "noun", [T, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ — الْقَافِيَةُ الْأُولَى: يَتِمُّ الْمَعْنَى عِنْدَهَا.", "«the base» — the naʿt; the first rhyme, the sense whole here.", "«alçak» — na't; birinci kafiye, mana burada tam."),
  tok("إِنَّهَا", "inna", "part", [T, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«it is» — إِنَّ with its ism.", "«o» — inne ve ismi.", punct="*",
      segments=[seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  tok("شَرَكُ", "sharak", "noun", [T, "inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ إِنَّ مَرْفُوعٌ، مُضَافٌ.", "«the snare of» — the khabar of إِنَّ.", "«tuzağı» — inne'nin haberi."),
  tok("الرَّدَى", "rada", "noun", [T, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — الرَّدَى: الْهَلَاكُ.", "«ruin».", "«helâk»."),
  tok("وَقَرَارَةُ", "qarara", "noun", [T, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَرَارَةُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the seat of» — joined.", "«ve karargâhı» — atıf.",
      segments=[seg("وَ", "wa", "conj"), seg("قَرَارَةُ", "qarara", "noun")]),
  tok("الْأَكْدَارِ", "kadar", "noun", [T, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ كَدَرٍ؛ الْقَافِيَةُ الثَّانِيَةُ.", "«sorrows» — the second rhyme.", "«kederlerin» — ikinci kafiye."),
 ]})
S[-1]["badi"] = [{"kind": "tashri", "pair": [ix(S[-1], "الدَّنِيَّةِ"), ix(S[-1], "الْأَكْدَارِ")]}]

# ----------- s11 — luzum ma la yalzam (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "And LUZUM MA LA YALZAM is that there come, before the rawi letter or what stands in its sense from the fasila, what is not required in the sajʿ." + R_EN,
 "tr": "LÜZÛM-İ MÂ LÂ YELZEM, revî harfinden yahut fâsıladan onun mânâsında olandan önce, secide gerekli olmayanın gelmesidir." + R_TR},
 "tokens": [
  tok("وَلُزُومُ", "luzum", "noun", [L, "mubtada-khabar", "idafa-definiteness", "masdar", "atf-nasaq"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلُزُومُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ لَزِمَ.", "«and the requiring of» — the mubtada, annexed.", "«ve lüzûmu» — mübtedâ, muzâf.",
      segments=[seg("وَ", "wa", "conj"), seg("لُزُومُ", "luzum", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [L, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the mudaf ilayh.", "«…olanın» — muzâfun ileyh."),
  tok("لَا", "la-nafiya", "part", [L, "jumla-sifa"], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يَلْزَمُ", "lazima", "verb", [L, "jumla-sifa", "mudari-marfu"], "صِلَةُ الْمَوْصُولِ — مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«is required» — the sila.", "«gerekmez» — sıla."),
  tok("أَنْ", "an-masdariyya", "part", [L, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar clause is the khabar.", "«-mesi» — te'vîlli masdar haberdir."),
  tok("يَجِيءَ", "jaa", "verb", [L, "an-masdariyya", "hollow-verbs"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ.", "«there come» — in nasb.", "«gelmesi» — mansub."),
  tok("قَبْلَ", "qabla", "noun", [L, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«before».", "«önce» — zarf."),
  tok("حَرْفِ", "harf", "noun", [L, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the letter of».", "«harfinden»."),
  tok("الرَّوِيِّ", "rawiyy", "noun", [L, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the rawi».", "«revî»."),
  tok("أَوْ", "aw", "conj", [L, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("مَا", "ma-mawsula", "pron", [L, "ism-mawsul", "atf-nasaq"], "اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى حَرْفِ فِي مَحَلِّ جَرٍّ.", "«what» — joined to «the letter».", "«…olan» — harf'e atıf."),
  fi(L),
  tok("مَعْنَاهُ", "mana", "noun", [L, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةُ الْمَوْصُولِ شِبْهُ جُمْلَةٍ.", "«its sense» — the sila is a phrase.", "«mânâsında» — sıla, şibh cümle.",
      segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  tok("مِنَ", "min", "prep", [L, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْفَاصِلَةِ", "fasila", "noun", [L, "huruf-jarr"], "مَجْرُورٌ.", "«the fasila».", "«fâsıladan»."),
  tok("مَا", "ma-mawsula", "pron", [L, "ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلُ يَجِيءَ.", "«what» — the doer of «come».", "«…olan» — «gelmesi»nin fâili."),
  tok("لَيْسَ", "laysa", "verb", [L, "kana-wa-akhawatuha", "jumla-sifa"], "صِلَةُ الْمَوْصُولِ — فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«is not» — the sila; its ism hidden.", "«değil» — sıla; ismi gizli."),
  tok("بِلَازِمٍ", "lazim", "noun", [L, "kana-wa-akhawatuha", "huruf-jarr", "ism-fail"], "الْبَاءُ زَائِدَةٌ، وَلَازِمٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "«required» — the khabar of لَيْسَ under the extra ba.", "«gerekli» — zâid bâ ile leyse'nin haberi.",
      segments=[seg("بِ", "bi", "prep"), seg("لَازِمٍ", "lazim", "noun")]),
  fi(L),
  tok("السَّجْعِ", "saj", "noun", [L, "huruf-jarr"], "مَجْرُورٌ.", "«the sajʿ».", "«secide»."),
 ]})

# ----------- s12 — 93:9-10
S.append({"id": "s12", "translation": {
 "en": "«So as for the orphan — do not OPPRESS (taqhar); and as for the beggar — do not REBUKE (tanhar)» (93:9-10) — the fasilas end on the ra; the ha before it, which the sajʿ did not require, is kept in both: luzum ma la yalzam.",
 "tr": "«Öyleyse yetime gelince — EZME (takhar); dilenciye gelince — AZARLAMA (tenhar)» (Duhâ 9-10) — fâsılalar râ ile biter; secinin gerektirmediği ondan önceki hâ ikisinde de korunur: lüzûm-i mâ lâ yelzem."},
 "tokens": [
  tok("فَأَمَّا", "amma", "part", [L, "amma-tafsiliyya"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«so as for» — the particle of detailing.", "«öyleyse … -e gelince» — tafsil edatı.",
      segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("الْيَتِيمَ", "yatim", "noun", [L, "maful-bihi", "amma-tafsiliyya"], "مَفْعُولٌ بِهِ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ — اشْتِغَالٌ: لَا تَقْهَرِ الْيَتِيمَ.", "«the orphan» — the object of an elided verb the next explains (ishtighal).", "«yetimi» — hazfedilmiş fiilin mef'ûlü, sonraki açıklar (iştigâl)."),
  tok("فَلَا", "la-nahiya", "part", [L, "la-nahiya", "amma-tafsiliyya"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«do not» — the fa of أَمَّا's answer, the prohibiting la.", "«-me» — emmâ'nın cevap fâsı, nehiy lâsı.",
      segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nahiya", "part")]),
  tok("تَقْهَرْ", "qahara", "verb", [L, "la-nahiya", "lam-jazim", "saj"], "مُضَارِعٌ مَجْزُومٌ بِلَا، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ؛ الْفَاصِلَةُ الْأُولَى: قْهَرْ.", "«oppress» — in jazm; the first fasila.", "«ezme» — meczum; birinci fâsıla.", punct="،"),
  tok("وَأَمَّا", "amma", "part", [L, "amma-tafsiliyya", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for».", "«ve … -e gelince».",
      segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("السَّائِلَ", "sail", "noun", [L, "maful-bihi", "amma-tafsiliyya", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ — اشْتِغَالٌ.", "«the beggar» — the fronted object (ishtighal).", "«dilenciyi» — iştigâl mef'ûlü."),
  tok("فَلَا", "la-nahiya", "part", [L, "la-nahiya"], "الْفَاءُ رَابِطَةٌ، وَلَا نَاهِيَةٌ.", "«do not».", "«-me».",
      segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nahiya", "part")]),
  tok("تَنْهَرْ", "nahara-rebuke", "verb", [L, "la-nahiya", "lam-jazim", "saj"], "مُضَارِعٌ مَجْزُومٌ بِلَا، وَالْفَاعِلُ مُسْتَتِرٌ؛ الْفَاصِلَةُ الثَّانِيَةُ: نْهَرْ — الْهَاءُ قَبْلَ الرَّاءِ هِيَ اللُّزُومُ.", "«rebuke» — the second fasila; the ha before the ra is the luzum.", "«azarlama» — ikinci fâsıla; râ'dan önceki hâ lüzûmdur."),
 ]})
S[-1]["badi"] = [{"kind": "luzum", "pair": [ix(S[-1], "تَقْهَرْ"), ix(S[-1], "تَنْهَرْ")], "letter": "ه"},
                 {"kind": "saj", "sub": "mutawazi", "pair": [ix(S[-1], "تَقْهَرْ"), ix(S[-1], "تَنْهَرْ")]}]

# ----------- s13-s15 — Abu Tammam's three bayts (the lam before the ta)
S.append({"id": "s13", "translation": {
 "en": "«I shall thank ʿAmr, if my death is delayed, * for favours not grudged, though they were great.» (Abu Tammam) — the rhyme on the ta, and the lam before it kept through all three bayts.",
 "tr": "«Ecelim gecikirse Amr'a şükredeceğim, * başa kakılmayan, büyük olsalar da, ihsanları için.» (Ebû Temmâm) — kafiye tâ üzere; ondan önceki lâm üç beyitte de korunur."},
 "tokens": [
  tok("سَأَشْكُرُ", "shakara", "verb", [L, "mudari-marfu", "fail"], "السِّينُ لِلِاسْتِقْبَالِ، وَأَشْكُرُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I shall thank» — the sin of the future.", "«şükredeceğim» — istikbal sîni.",
      segments=[seg("سَ", "sa", "part"), seg("أَشْكُرُ", "shakara", "verb")]),
  tok("عَمْرًا", "amr-name", "noun", [L, "maful-bihi"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ — عَمْرٌو: تَسْقُطُ وَاوُهُ فِي النَّصْبِ.", "«ʿAmr» — the first object; the silent waw is dropped in nasb.", "«Amr'a» — birinci mef'ûl; nasbda sessiz vâv düşer."),
  tok("إِنْ", "in-shartiyya", "part", [L, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ — وَالْجُمْلَةُ مُعْتَرِضَةٌ.", "«if» — the conditional, parenthetical.", "«-se» — şart, mu'tarıza."),
  tok("تَرَاخَتْ", "tarakha", "verb", [L, "in-shartiyya", "form-vi-verbs", "naqis-verbs"], "فِعْلُ الشَّرْطِ — مَاضٍ نَاقِصٌ مِنَ التَّفَاعُلِ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«is delayed» — the shart verb, Form VI.", "«gecikirse» — şart fiili, tefâul."),
  tok("مَنِيَّتِي", "maniyya", "noun", [L, "fail", "ya-al-mutakallim"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ.", "«my death» — the doer, before the speaker's ya.", "«ecelim» — fâil, mütekellim yâsı.", punct="*",
      segments=[seg("مَنِيَّتِ", "maniyya", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("أَيَادِيَ", "ayadi", "noun", [L, "mafulayn", "ism-maqsur-manqus", "jam-taksir"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — الْمَنْقُوصُ يُظْهِرُ فَتْحَتَهُ؛ جَمْعُ الْجَمْعِ: أَيْدٍ ثُمَّ أَيَادٍ.", "«favours» — the second object; the manqus shows its fatha.", "«ihsanları» — ikinci mef'ûl; mankûs fethasını gösterir."),
  tok("لَمْ", "lam-jazim", "part", [L, "lam-jazim", "jumla-sifa"], "حَرْفُ نَفْيٍ وَجَزْمٍ — وَالْجُمْلَةُ صِفَةٌ لِأَيَادِيَ.", "«not» — the clause describes the favours.", "«-me» — cümle ihsanların sıfatı."),
  tok("تُمْنَنْ", "manna", "verb", [L, "lam-jazim", "naib-al-fail", "doubled-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ، فُكَّ إِدْغَامُهُ لِلسُّكُونِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«were grudged» — the passive, its doubling opened for the sukun.", "«başa kakıldı» — meçhul, sükûn için idgamı çözülmüş."),
  tok("وَإِنْ", "in-shartiyya", "part", [L, "in-shartiyya"], "الْوَاوُ لِلْحَالِ، وَإِنْ وَصْلِيَّةٌ: وَلَوْ.", "«though» — the concessive إِنْ.", "«olsalar da» — vasliyye in.",
      segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("هِيَ", "hiya", "pron", [L, "fail"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ: وَإِنْ جَلَّتْ هِيَ.", "«they» — the doer of an elided verb the next explains.", "«onlar» — hazfedilmiş fiilin fâili, sonraki açıklar."),
  tok("جَلَّتِ", "jalla", "verb", [L, "in-shartiyya", "doubled-verbs"], "مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — كُسِرَتْ لِلرَّوِيِّ: جَلَّتْ؛ اللَّامُ قَبْلَ التَّاءِ هِيَ اللُّزُومُ.", "«were great» — the ta takes the rhyme's kasra; the lam before it is the luzum.", "«büyük idiler» — tâ, kafiye kesresini alır; ondan önceki lâm lüzûmdur."),
 ]})
S[-1]["badi"] = [{"kind": "luzum", "word": ix(S[-1], "جَلَّتِ"), "letter": "ل"}]

S.append({"id": "s14", "translation": {
 "en": "«A young man whose wealth is not veiled from his friend, * nor does he show complaint when the sandal slips.» (Abu Tammam)",
 "tr": "«Zenginliği dostundan gizlenmeyen, * nalın kaydığında şikâyet göstermeyen bir yiğit.» (Ebû Temmâm)"},
 "tokens": [
  tok("فَتًى", "fatan", "noun", [L, "mubtada-khabar", "ism-maqsur-manqus"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُوَ فَتًى — مَقْصُورٌ مُنَوَّنٌ.", "«a young man» — the khabar of an omitted «he is».", "«bir yiğit» — hazfedilmiş «o»nun haberi."),
  tok("غَيْرُ", "ghayr", "noun", [L, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَرْفُوعٌ، مُضَافٌ.", "«not» — the naʿt, annexed.", "«-meyen» — na't, muzâf."),
  tok("مَحْجُوبِ", "mahjub", "noun", [L, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — اسْمُ مَفْعُولٍ مِنْ حَجَبَ.", "«veiled of» — the ism maf'ul, annexed to its doer.", "«gizlenmiş» — ism-i mef'ûl, fâiline muzâf."),
  tok("الْغِنَى", "ghina", "noun", [L, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — إِضَافَةُ اسْمِ الْمَفْعُولِ إِلَى نَائِبِ فَاعِلِهِ.", "«wealth» — the ism maf'ul annexed to its deputy doer.", "«zenginliği» — ism-i mef'ûl nâib-i fâiline muzâf."),
  tok("عَنْ", "an", "prep", [L, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("صَدِيقِهِ", "sadiq", "noun", [L, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his friend».", "«dostundan».", punct="*",
      segments=[seg("صَدِيقِ", "sadiq", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("وَلَا", "la-nafiya", "part", [L, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor» — the la repeats the negation.", "«ne de» — nefyi pekiştiren lâ.",
      segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("مُظْهِرِ", "muzhir", "noun", [L, "atf-nasaq", "idafa-definiteness", "ism-fail", "form-iv-verbs"], "مَعْطُوفٌ عَلَى مَحْجُوبِ مَجْرُورٌ، مُضَافٌ — اسْمُ فَاعِلٍ مِنْ أَظْهَرَ.", "«showing of» — joined to «veiled».", "«gösteren» — mahcûb'a atıf."),
  tok("الشَّكْوَى", "shakwa", "noun", [L, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«complaint».", "«şikâyeti»."),
  tok("إِذَا", "idha", "part", [L, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the zarf with the shart's sense.", "«-diğinde» — şart mânâlı zarf."),
  tok("النَّعْلُ", "nal", "noun", [L, "fail", "idha-shartiyya"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ: إِذَا زَلَّتِ النَّعْلُ.", "«the sandal» — the doer of an elided verb the next explains.", "«nalın» — hazfedilmiş fiilin fâili."),
  tok("زَلَّتِ", "zalla-slip", "verb", [L, "idha-shartiyya", "doubled-verbs"], "مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — كُسِرَتْ لِلرَّوِيِّ؛ اللَّامُ قَبْلَ التَّاءِ هِيَ اللُّزُومُ.", "«slips» — the rhyme's kasra; the lam before the ta.", "«kaydı» — kafiye kesresi; tâ'dan önceki lâm."),
 ]})
S[-1]["badi"] = [{"kind": "luzum", "word": ix(S[-1], "زَلَّتِ"), "letter": "ل"}]

S.append({"id": "s15", "translation": {
 "en": "«He saw my want from where its place lies hidden, * and it was a mote in his eyes until it cleared.» (Abu Tammam)",
 "tr": "«Yerinin gizli olduğu yerden fakirliğimi gördü, * ve o giderilinceye kadar gözlerinde bir çöp oldu.» (Ebû Temmâm)"},
 "tokens": [
  tok("رَأَى", "raa", "verb", [L, "fail", "maful-bihi", "naqis-verbs"], "مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he saw».", "«gördü»."),
  tok("خَلَّتِي", "khalla", "noun", [L, "maful-bihi", "ya-al-mutakallim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — الْخَلَّةُ: الْفَقْرُ.", "«my want» — the object, before the speaker's ya.", "«fakirliğimi» — mef'ûl, mütekellim yâsı.",
      segments=[seg("خَلَّتِ", "khalla", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("مِنْ", "min", "prep", [L, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("حَيْثُ", "haythu", "noun", [L, "huruf-jarr", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَى الْجُمْلَةِ.", "«where» — the mabni zarf, annexed to a clause.", "«yerden» — mebnî zarf, cümleye muzâf."),
  tok("يَخْفَى", "khafiya", "verb", [L, "idafa-definiteness", "naqis-verbs", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهِ.", "«lies hidden» — the clause is the mudaf ilayh.", "«gizlenir» — cümle muzâfun ileyh."),
  tok("مَكَانُهَا", "makan", "noun", [L, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its place» — the doer.", "«yeri» — fâil.", punct="*",
      segments=[seg("مَكَانُ", "makan", "noun"), seg("هَا", "pron-3fs", "pron")]),
  tok("فَكَانَتْ", "kana", "verb", [L, "kana-wa-akhawatuha", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَكَانَتْ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ (الْخَلَّةُ).", "«and it was» — كَانَ, its ism hidden: the want.", "«ve oldu» — kâne, ismi gizli: fakirlik.",
      segments=[seg("فَ", "fa", "conj"), seg("كَانَتْ", "kana", "verb")]),
  tok("قَذَى", "qadha", "noun", [L, "kana-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ — الْقَذَى: مَا يَقَعُ فِي الْعَيْنِ.", "«a mote» — the khabar of كَانَ; what falls into the eye.", "«çöp» — kâne'nin haberi; göze düşen şey."),
  tok("عَيْنَيْهِ", "ayn", "noun", [L, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his two eyes» — the dual, its nun dropped for the annex.", "«iki gözünde» — tesniye, izâfet için nûnu düşmüş.",
      segments=[seg("عَيْنَيْ", "ayn", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("حَتَّى", "hatta", "part", [L, "huruf-jarr"], "حَرْفُ ابْتِدَاءٍ وَغَايَةٍ — يَلِيهِ الْمَاضِي.", "«until» — of the end-point, before a mazi.", "«-inceye kadar» — gaye harfi, mâzî öncesi."),
  tok("تَجَلَّتِ", "tajalla", "verb", [L, "form-v-verbs", "naqis-verbs"], "مَاضٍ نَاقِصٌ مِنَ التَّفَعُّلِ، وَالتَّاءُ لِلتَّأْنِيثِ — كُسِرَتْ لِلرَّوِيِّ؛ اللَّامُ قَبْلَ التَّاءِ هِيَ اللُّزُومُ.", "«it cleared» — Form V; the rhyme's kasra; the lam before the ta.", "«giderildi» — tefe'ul; kafiye kesresi; tâ'dan önceki lâm."),
 ]})
S[-1]["badi"] = [{"kind": "luzum", "word": ix(S[-1], "تَجَلَّتِ"), "letter": "ل"}]

# ----------- s16 — the closing principle (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "And the root of beauty in all of this is that the WORDS be followers of the MEANINGS, not the meanings followers of the words." + R_EN,
 "tr": "Bütün bunlarda güzelliğin aslı, LAFIZLARIN MÂNÂLARA tâbi olması, mânâların lafızlara tâbi olmaması." + R_TR},
 "tokens": [
  tok("وَأَصْلُ", "asl", "noun", [M, "mubtada-khabar", "idafa-definiteness", "atf-nasaq"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَصْلُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the root of» — the mubtada.", "«ve … aslı» — mübtedâ.",
      segments=[seg("وَ", "wa", "conj"), seg("أَصْلُ", "asl", "noun")]),
  tok("الْحُسْنِ", "husn", "noun", [M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«beauty».", "«güzelliğin»."),
  fi(M),
  tok("جَمِيعِ", "jami", "noun", [M, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«all of».", "«bütün»."),
  tok("ذَلِكَ", "dhalika", "pron", [M, "idafa-definiteness", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this».", "«bunların»."),
  tok("أَنْ", "an-masdariyya", "part", [M, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar clause is the khabar.", "«-ması» — te'vîlli masdar haberdir."),
  tok("تَكُونَ", "kana", "verb", [M, "kana-wa-akhawatuha", "an-masdariyya"], "مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be» — كَانَ in nasb.", "«olması» — mansub kâne."),
  tok("الْأَلْفَاظُ", "lafz", "noun", [M, "kana-wa-akhawatuha", "jam-taksir"], "اسْمُ تَكُونَ مَرْفُوعٌ.", "«the words» — the ism.", "«lafızlar» — ismi."),
  tok("تَوَابِعَ", "tabi", "noun", [M, "kana-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf"], "خَبَرُ تَكُونَ مَنْصُوبٌ — جَمْعُ تَابِعٍ، لَا يُنَوَّنُ.", "«followers» — the khabar; a diptote plural.", "«tâbi» — haberi; gayr-ı munsarif cem'."),
  tok("لِلْمَعَانِي", "mana", "noun", [M, "huruf-jarr", "jam-taksir", "ism-maqsur-manqus"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمَعَانِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ مُعَرَّفٌ يُثْبِتُ يَاءَهُ.", "«of the meanings» — the definite manqus keeps its ya.", "«mânâlara» — marife mankûs yâsını korur.", punct="،",
      segments=[seg("لِ", "li", "prep"), seg("الْمَعَانِي", "mana", "noun")]),
  tok("لَا", "la-nafiya", "part", [M, "atf-nasaq"], "حَرْفُ عَطْفٍ يُفِيدُ النَّفْيَ عَنِ الثَّانِي.", "«not» — the joining la that denies the second.", "«değil» — ikinciden nefyeden atıf lâsı."),
  tok("الْمَعَانِي", "mana", "noun", [M, "atf-nasaq", "jam-taksir", "ism-maqsur-manqus"], "مَعْطُوفٌ عَلَى الْأَلْفَاظُ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the meanings» — joined to «the words».", "«mânâlar» — lafızlara atıf."),
  tok("تَوَابِعَ", "tabi", "noun", [M, "kana-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf"], "خَبَرٌ لِتَكُونَ الْمُقَدَّرَةِ مَنْصُوبٌ.", "«followers» — the khabar of an estimated «be».", "«tâbi» — takdîrî «olması»nın haberi."),
  tok("لِلْأَلْفَاظِ", "lafz", "noun", [M, "huruf-jarr", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَلْفَاظِ مَجْرُورٌ.", "«of the words».", "«lafızlara».",
      segments=[seg("لِ", "li", "prep"), seg("الْأَلْفَاظِ", "lafz", "noun")]),
 ]})
S[-1]["badi"] = [{"kind": "aks", "first": [ix(S[-1], "الْأَلْفَاظُ"), ix(S[-1], "تَوَابِعَ")], "second": [ix(S[-1], "تَوَابِعَ", 2), ix(S[-1], "لِلْأَلْفَاظِ")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "muwazana": need("muwazana", "مُوَازَنَة", "و ز ن", "noun", "muwazana — the fasilas agree in wazn but not in rhyme (masdar of Form III وَازَنَ)", "muvâzene — fâsılaların vezinde birleşip kafiyede birleşmemesi (mufâale masdarı)", 6),
 "tasawi": need("tasawi", "تَسَاوٍ", "س و ي", "noun", "equality, being alike (masdar of Form VI تَسَاوَى; a manqus)", "eşitlik, denklik (tefâul masdarı; mankûs)", 5),
 "duna": need("duna", "دُونَ", "د و ن", "noun", "without; below (a zarf, always annexed)", "-sız; altında (dâimâ muzâf zarf)", 4),
 "numruqa": need("numruqa", "نُمْرُقَة", "ن م ر ق", "noun", "a cushion (pl. نَمَارِق, a diptote)", "yastık (ç. نَمَارِق, gayr-ı munsarif)", 6, plural="نَمَارِق"),
 "masfufa": need("masfufa", "مَصْفُوفَة", "ص ف ف", "noun", "ranged in rows, set in order (ism maf'ul of صَفَّ, feminine)", "sıra sıra dizilmiş (ism-i mef'ûl, müennes)", 5),
 "zarbiyya": need("zarbiyya", "زَرْبِيَّة", "ز ر ب", "noun", "a carpet, a rug (pl. زَرَابِيّ)", "halı, döşek (ç. زَرَابِيّ)", 6, plural="زَرَابِيّ"),
 "mabthutha": need("mabthutha", "مَبْثُوثَة", "ب ث ث", "noun", "spread out, scattered (ism maf'ul of بَثَّ, feminine)", "yayılmış, serilmiş (ism-i mef'ûl, müennes)", 5),
 "ihda": need("ihda", "إِحْدَى", "و ح د", "noun", "one (of two, feminine) — annexed", "biri (iki müennesten) — muzâf", 4),
 "khassa-verb": need("khassa-verb", "خَصَّ", "خ ص ص", "verb", "to single out, to set apart (doubled; خَصَّ يَخُصُّ)", "tahsis etmek, ayırmak (muzâaf; hassa yehussu)", 4),
 "mumathala": need("mumathala", "مُمَاثَلَة", "م ث ل", "noun", "mumathala — the muwazana in which most words of the two clauses answer in wazn (masdar of Form III مَاثَلَ)", "mümâsele — iki cümlenin çoğu kelimesinin vezince karşılıklı olduğu muvâzene (mufâale masdarı)", 6),
 "aata": need("aata", "آتَى", "أ ت ي", "verb", "to give, to bring to (Form IV of أَتَى; آتَى يُؤْتِي إِيتَاءً)", "vermek, getirmek (if'âl; âtâ yu'tî îtâen)", 4),
 "mustabin": need("mustabin", "مُسْتَبِين", "ب ي ن", "noun", "clear, made plain (ism fa'il of اسْتَبَانَ)", "açık, belli (istif'âl ism-i fâili)", 6),
 "maha-oryx": need("maha-oryx", "مَهَاة", "م ه و", "noun", "the wild cow, the oryx (pl. مَهًا) — the poets' figure for the beautiful eye", "yaban ineği, ceylan (ç. مَهًا) — güzel gözün şairce sûreti", 6, plural="مَهًا"),
 "hata": need("hata", "هَاتَا", None, "pron", "these (feminine plural or singular): هَا of alerting + تَا, a form of هَذِهِ", "bunlar / bu (müennes): tenbih hâ'sı + tâ, هَذِهِ'nin bir şekli", 6),
 "anisa": need("anisa", "آنِسَة", "أ ن س", "noun", "companionable, sociable (a woman) (pl. أَوَانِس, a diptote)", "munis, uysal (kadın) (ç. أَوَانِس, gayr-ı munsarif)", 6, plural="أَوَانِس"),
 "qana": need("qana", "قَنَاة", "ق ن و", "noun", "a spear-shaft, a spear (pl. قَنًا)", "mızrak (ç. قَنًا)", 6, plural="قَنًا"),
 "khatt-place": need("khatt-place", "الْخَطّ", None, "propn", "al-Khatt — the coast of Bahrain where the spears were traded; «Khatti spears»", "el-Hatt — mızrakların satıldığı Bahreyn sahili; «Hatt mızrakları»", 6),
 "dhabil": need("dhabil", "ذَابِل", "ذ ب ل", "noun", "withered, wilted; of a spear: slender (pl. ذَوَابِل)", "solgun, kurumuş; mızrakta: ince (ç. ذَوَابِل)", 6, plural="ذَوَابِل"),
 "qalb-figure": need("qalb-figure", "قَلْب", "ق ل ب", "noun", "the qalb — reversal: the line that reads the same from either end (masdar of قَلَبَ)", "kalb — tersine çevirme: iki uçtan aynı okunan mısra (kalebe masdarı)", 6),
 "kama": need("kama", "كَمَا", None, "part", "as, just as (the kaf with the masdar-ma)", "gibi, -dığı gibi (kâf ile masdariyye mâ)", 3),
 "hal-istifham": need("hal-istifham", "هَلْ", None, "part", "the question particle: «is it so?»", "istifham harfi: «mı?»", 2),
 "hawl": need("hawl", "هَوْل", "ه و ل", "noun", "terror, dread (pl. أَهْوَال)", "korku, dehşet (ç. أَهْوَال)", 5, plural="أَهْوَال"),
 "kabbara": need("kabbara", "كَبَّرَ", "ك ب ر", "verb", "to magnify, to say «Allahu akbar» (Form II)", "yüceltmek, tekbir getirmek (tef'îl)", 3),
 "tashri": need("tashri", "تَشْرِيع", "ش ر ع", "noun", "tashriʿ — a bayt built on two rhymes (masdar of Form II شَرَّعَ)", "teşrî' — iki kafiye üzerine kurulu beyit (tef'îl masdarı)", 6),
 "wuquf": need("wuquf", "وُقُوف", "و ق ف", "noun", "stopping, a stop (masdar of وَقَفَ)", "durma, vakıf (vakafe masdarı)", 4),
 "ya": need("ya", "يَا", None, "part", "O — the particle of calling", "ey — nidâ harfi", 1),
 "khatib": need("khatib", "خَاطِب", "خ ط ب", "noun", "a suitor, one who seeks (ism fa'il of خَطَبَ)", "tâlip, isteyen (ism-i fâil)", 5),
 "daniyya": need("daniyya", "دَنِيَّة", "د ن و", "noun", "base, low, mean (feminine of دَنِيّ)", "alçak, aşağılık (دَنِيّ'nin müennesi)", 5),
 "rada": need("rada", "رَدًى", "ر د ي", "noun", "ruin, death (a maqsur)", "helâk, ölüm (maksûr)", 5),
 "qarara": need("qarara", "قَرَارَة", "ق ر ر", "noun", "a resting place, the seat of a thing", "karargâh, bir şeyin durduğu yer", 5),
 "kadar": need("kadar", "كَدَر", "ك د ر", "noun", "turbidity; sorrow, trouble (pl. أَكْدَار)", "bulanıklık; keder (ç. أَكْدَار)", 5, plural="أَكْدَار"),
 "luzum": need("luzum", "لُزُوم", "ل ز م", "noun", "requiring, necessity (masdar of لَزِمَ) — luzum ma la yalzam: keeping a letter the rhyme did not require", "lüzûm, gereklilik (lezime masdarı) — lüzûm-i mâ lâ yelzem: kafiyenin gerektirmediği harfi korumak", 6),
 "lazim": need("lazim", "لَازِم", "ل ز م", "noun", "required, necessary (ism fa'il of لَزِمَ)", "gerekli, lâzım (ism-i fâil)", 4),
 "laysa": need("laysa", "لَيْسَ", None, "verb", "is not — the jamid sister of كَانَ", "değil — kâne'nin câmid kız kardeşi", 2),
 "amma": need("amma", "أَمَّا", None, "part", "as for … — the particle of detailing, its answer takes a fa", "-e gelince — tafsil edatı, cevabı fâ alır", 4),
 "qahara": need("qahara", "قَهَرَ", "ق ه ر", "verb", "to oppress, to overpower (قَهَرَ يَقْهَرُ)", "ezmek, kahretmek (kahera yakheru)", 4),
 "nahara-rebuke": need("nahara-rebuke", "نَهَرَ", "ن ه ر", "verb", "to rebuke, to drive away with harsh words (نَهَرَ يَنْهَرُ)", "azarlamak, azarlayıp kovmak (nehera yenheru)", 5),
 "shakara": need("shakara", "شَكَرَ", "ش ك ر", "verb", "to thank (شَكَرَ يَشْكُرُ)", "şükretmek, teşekkür etmek (şekera yeşkuru)", 2),
 "sa": need("sa", "سَ", None, "part", "the sin of the near future on a mudari", "muzâriye gelen yakın gelecek sîni", 2),
 "amr-name": need("amr-name", "عَمْرو", None, "propn", "ʿAmr — a man's name; written with a silent waw to tell it from ʿUmar", "Amr — erkek adı; Ömer'den ayırmak için sessiz vâv ile yazılır", 4),
 "tarakha": need("tarakha", "تَرَاخَى", "ر خ و", "verb", "to be delayed, to slacken (Form VI; تَرَاخَى يَتَرَاخَى)", "gecikmek, gevşemek (tefâul; terâhâ yeterâhâ)", 6),
 "manna": need("manna", "مَنَّ", "م ن ن", "verb", "to grant a favour; to remind of a favour, to grudge it (doubled; مَنَّ يَمُنُّ)", "ihsan etmek; ihsanı başa kakmak (muzâaf; menne yemunnu)", 5),
 "jalla": need("jalla", "جَلَّ", "ج ل ل", "verb", "to be great, majestic (doubled; جَلَّ يَجِلُّ)", "büyük olmak, yüce olmak (muzâaf; celle yecillu)", 4),
 "fatan": need("fatan", "فَتًى", "ف ت ي", "noun", "a young man; a generous man (a maqsur; pl. فِتْيَان)", "genç, yiğit (maksûr; ç. فِتْيَان)", 4, plural="فِتْيَان"),
 "mahjub": need("mahjub", "مَحْجُوب", "ح ج ب", "noun", "veiled, hidden away (ism maf'ul of حَجَبَ)", "perdelenmiş, gizlenmiş (ism-i mef'ûl)", 5),
 "an": need("an", "عَنْ", None, "prep", "from, away from", "-den, -den uzak", 1),
 "muzhir": need("muzhir", "مُظْهِر", "ظ ه ر", "noun", "one who shows, displays (ism fa'il of أَظْهَرَ)", "gösteren, açığa vuran (if'âl ism-i fâili)", 5),
 "shakwa": need("shakwa", "شَكْوَى", "ش ك و", "noun", "a complaint (a maqsur)", "şikâyet (maksûr)", 4),
 "nal": need("nal", "نَعْل", "ن ع ل", "noun", "a sandal (pl. نِعَال)", "nalın, ayakkabı (ç. نِعَال)", 4, plural="نِعَال"),
 "zalla-slip": need("zalla-slip", "زَلَّ", "ز ل ل", "verb", "to slip, to stumble (doubled; زَلَّ يَزِلُّ)", "kaymak, sürçmek (muzâaf; zelle yezillu)", 4),
 "qadha": need("qadha", "قَذًى", "ق ذ ي", "noun", "a mote, what falls into the eye (a maqsur)", "göze düşen çöp (maksûr)", 6),
 "tabi": need("tabi", "تَابِع", "ت ب ع", "noun", "a follower, what follows (ism fa'il of تَبِعَ; pl. تَوَابِع, a diptote)", "tâbi, uyan (ism-i fâil; ç. تَوَابِع, gayr-ı munsarif)", 4, plural="تَوَابِع"),
 "dhalika": need("dhalika", "ذَلِكَ", None, "pron", "that (masculine, far)", "o, şu (müzekker, uzak)", 1),
}
for k in ("fasila", "fi", "wazn", "taqfiya", "wa", "in-shartiyya", "kana", "ma-mawsula", "qarina", "min", "lafz", "aw", "akthar", "mithl", "qabala", "ukhra", "ism", "bi", "kitab", "hada",
          "sirat", "mustaqim", "wahsh", "illa", "anna", "tilka", "qaraa", "akhir", "ka", "ma-masdariyya", "awwal", "mawadda", "dama", "li", "kull", "rabb", "fa", "bina", "bayt", "ala",
          "qafiya", "sahha", "mana", "inda", "dunya", "sharak", "lazima", "harf", "rawiyy", "saj", "jaa", "qabla", "yatim", "sail", "maniyya", "ayadi", "lam-jazim", "hiya", "ghayr",
          "ghina", "sadiq", "la-nafiya", "idha", "raa", "khalla", "haythu", "khafiya", "makan", "ayn", "hatta", "tajalla", "asl", "husn", "jami", "la-nahiya", "an-masdariyya", "inna",
          "pron-3ms", "pron-3fs", "pron-3d", "pron-2ms", "pron-1s"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

# ---------------------------------------------------------------- paradigms
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "khassa-verb", gem("nasara", "خَصّ", "خَصَص", "خُصّ", "خْصُص", ["خُصَّ", "خُصَّا", "خُصُّوا", "خُصِّي", "خُصَّا", "اُخْصُصْنَ"], "خُصُوص", "خَاصّ", "مَخْصُوص", "خُصَّ", "يُخَصُّ",
                                 "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: خَصَّ يَخُصُّ — خُصَّ بِاسْمٍ: مَجْهُولُهُ."))
_e = _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "آتَ", "ؤْت", "i", "آت", "إِيتَاء", "مُؤْتٍ (الْمُؤْتِي)", "مُؤْتًى", "أُوتِيَ", "يُؤْتَى",
                       note="آتَى يُؤْتِي: أَعْطَى — مَهْمُوزُ الْفَاءِ نَاقِصٌ؛ أُوتِي: تُقْلَبُ الْهَمْزَةُ السَّاكِنَةُ وَاوًا بَعْدَ الضَّمَّةِ.")
def _fixhamza(x):
    if isinstance(x, str): return x.replace("أُؤْت", "أُوت")
    if isinstance(x, list): return [_fixhamza(y) for y in x]
    if isinstance(x, dict): return {k: _fixhamza(v) for k, v in x.items()}
    return x
put_morph(mo, "aata", _fixhamza(_e))
put_morph(mo, "kabbara", _sg.derived(_sg.B2, _sg.W2, "ُ", "كَبَّر", "كَبِّر", "كَبِّر", "تَكْبِير", "مُكَبِّر", "مُكَبَّر", "كُبِّرَ", "يُكَبَّرُ"))
put_morph(mo, "qahara", _sg.sound1("fataha", "قَهَر", "قْهَر", "اِقْهَر", "قَهْر", "قَاهِر", "مَقْهُور", "قُهِرَ", "يُقْهَرُ"))
put_morph(mo, "nahara-rebuke", _sg.sound1("fataha", "نَهَر", "نْهَر", "اِنْهَر", "نَهْر", "نَاهِر", "مَنْهُور", "نُهِرَ", "يُنْهَرُ"))
put_morph(mo, "shakara", _sg.sound1("nasara", "شَكَر", "شْكُر", "اُشْكُر", "شُكْر", "شَاكِر", "مَشْكُور", "شُكِرَ", "يُشْكَرُ"))
put_morph(mo, "tarakha", _sg.derived_naqis(_sg.B6, _sg.W6, "َ", "تَرَاخَ", "تَرَاخ", "a", "تَرَاخ", "تَرَاخٍ (التَّرَاخِي)", "مُتَرَاخٍ (الْمُتَرَاخِي)"))
put_morph(mo, "manna", _sg.idgham(gem("nasara", "مَنّ", "مَنَن", "مُنّ", "مْنُن", ["مُنَّ", "مُنَّا", "مُنُّوا", "مُنِّي", "مُنَّا", "اُمْنُنْنَ"], "مَنّ", "مَانّ", "مَمْنُون", "مُنَّ", "يُمَنُّ",
                           "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: مَنَّ يَمُنُّ — لَمْ تُمْنَنْ: مَجْزُومٌ مَفْكُوكُ الْإِدْغَامِ.")))
put_morph(mo, "jalla", gem("daraba", "جَلّ", "جَلَل", "جِلّ", "جْلِل", ["جِلَّ", "جِلَّا", "جِلُّوا", "جِلِّي", "جِلَّا", "اِجْلِلْنَ"], "جَلَال", "جَالّ", None, None, None,
                           "مُضَاعَفٌ مِنْ بَابِ ضَرَبَ: جَلَّ يَجِلُّ — عَظُمَ."))
put_morph(mo, "zalla-slip", gem("daraba", "زَلّ", "زَلَل", "زِلّ", "زْلِل", ["زِلَّ", "زِلَّا", "زِلُّوا", "زِلِّي", "زِلَّا", "اِزْلِلْنَ"], "زَلَل", "زَالّ", None, None, None,
                                "مُضَاعَفٌ مِنْ بَابِ ضَرَبَ: زَلَّ يَزِلُّ — زَلَّتِ النَّعْلُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_M = {
 "id": "muwazana",
 "title": {"ar": "الْمُوَازَنَةُ وَالْمُمَاثَلَةُ — تَسَاوِي الْفَاصِلَتَيْنِ فِي الْوَزْنِ", "en": "The muwazana and the mumathala — the fasilas equal in wazn", "tr": "Muvâzene ve mümâsele — fâsılaların vezinde eşitliği"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الموازنة: تساوي الفاصلتين في الوزن دون التقفية؛ فإن كان ما في إحدى القرينتين من الألفاظ أو أكثره مثل ما يقابله من الأخرى في الوزن خص باسم المماثلة"],
 "question": {
  "en": ["Do the two clauses' last words share a WAZN but end on DIFFERENT letters? That is MUWAZANA — مَصْفُوفَةٌ / مَبْثُوثَةٌ (88:15-16), both مَفْعُولَة, one on the fa and one on the tha. Had the letters agreed too, it would be sajʿ.",
         "Do MOST of the words of one clause answer the other's in wazn — الْكِتَابَ الْمُسْتَبِينَ / الصِّرَاطَ الْمُسْتَقِيمَ (37:117-118), مَهَا الْوَحْشِ … أَوَانِسُ / قَنَا الْخَطِّ … ذَوَابِلُ? Then it is singled out as MUMATHALA.",
         "What does the engine read? It cuts the clauses as the sajʿ reader does (the author's pauses honoured), compares the fasilas' wazn by their vowel pattern, REFUSES the pair when the rawi letters agree (that is the sajʿ's), and counts the answering words for the mumathala."],
  "tr": ["İki cümlenin son kelimeleri bir VEZNİ paylaşıp FARKLI harflerle mi biter? Bu MUVÂZENE'dir — مَصْفُوفَةٌ / مَبْثُوثَةٌ (Gâşiye 15-16), ikisi de مَفْعُولَة, biri fâ biri sâ ile. Harfler de birleşseydi seci olurdu.",
         "Bir cümlenin kelimelerinin ÇOĞU öbürününkine vezince karşılık veriyor mu — الْكِتَابَ الْمُسْتَبِينَ / الصِّرَاطَ الْمُسْتَقِيمَ (Sâffât 117-118), مَهَا الْوَحْشِ … أَوَانِسُ / قَنَا الْخَطِّ … ذَوَابِلُ? O zaman MÜMÂSELE adıyla ayrılır.",
         "Motor neyi okur? Cümleleri seci okuyucusu gibi keser (yazarın duraklarına uyar), fâsılaların veznini hareke örgüsüyle karşılaştırır, revî harfleri birleşince çifti REDDEDER (o secinindir) ve mümâsele için karşılık veren kelimeleri sayar."]},
 "plain": {
  "en": "Two clauses whose last words match in wazn but not in rhyme — and, when most of their words match, the mumathala.",
  "tr": "Son kelimeleri vezince eş, kafiyece eş olmayan iki cümle — ve kelimelerinin çoğu eşleşince mümâsele."},
 "explanation": {
  "en": "الْمُوَازَنَةُ تَسَاوِي الْفَاصِلَتَيْنِ فِي الْوَزْنِ دُونَ التَّقْفِيَةِ. The sajʿ asked for two things of the fasilas — one wazn and one rawi; the muwazana keeps the first and drops the second, so what the ear hears is a measured cadence without a rhyme. Where the answering runs through the clause — most words of one weighing like their partners in the other — the Talkhis gives the figure its own name, the mumathala: وَآتَيْنَاهُمَا الْكِتَابَ الْمُسْتَبِينَ وَهَدَيْنَاهُمَا الصِّرَاطَ الْمُسْتَقِيمَ, where الْكِتَابَ answers الصِّرَاطَ and الْمُسْتَبِينَ answers الْمُسْتَقِيمَ. The engine's wazn is the vowel pattern over the bare letters, madd letters counted and consonantal waws not — مَوْضُوعَة and مَرْفُوعَة weigh alike though one wears a radical waw.",
  "tr": "الْمُوَازَنَةُ تَسَاوِي الْفَاصِلَتَيْنِ فِي الْوَزْنِ دُونَ التَّقْفِيَةِ. Seci fâsılalardan iki şey isterdi — bir vezin ve bir revî; muvâzene birincisini tutar ikincisini bırakır, kulağın duyduğu kafiyesiz ölçülü bir âhenktir. Karşılık cümle boyunca sürerse — birinin çoğu kelimesi öbüründeki eşi gibi tartılırsa — Telhîs sanata kendi adını verir, mümâsele: وَآتَيْنَاهُمَا الْكِتَابَ الْمُسْتَبِينَ وَهَدَيْنَاهُمَا الصِّرَاطَ الْمُسْتَقِيمَ; burada الْكِتَابَ, الصِّرَاطَ'a ve الْمُسْتَبِينَ, الْمُسْتَقِيمَ'e karşılık verir. Motorun vezni çıplak harfler üzerindeki hareke örgüsüdür; med harfleri sayılır, sessiz vâvlar sayılmaz — مَوْضُوعَة ile مَرْفُوعَة biri aslî vâv taşısa da aynı tartılır."},
 "examples": [
  {"ar": "وَنَمَارِقُ مَصْفُوفَةٌ وَزَرَابِيُّ مَبْثُوثَةٌ", "en": "88:15-16 — muwazana: one wazn, two letters.", "tr": "Gâşiye 15-16 — muvâzene: bir vezin, iki harf.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "وَآتَيْنَاهُمَا الْكِتَابَ الْمُسْتَبِينَ وَهَدَيْنَاهُمَا الصِّرَاطَ الْمُسْتَقِيمَ", "en": "37:117-118 — mumathala: most words answer.", "tr": "Sâffât 117-118 — mümâsele: çoğu kelime karşılıklı.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "فِيهَا سُرُرٌ مَرْفُوعَةٌ وَأَكْوَابٌ مَوْضُوعَةٌ", "en": "88:13-14 — NOT a muwazana: the fasilas rhyme (the ʿayn), so it is the sajʿ mutawazi.", "tr": "Gâşiye 13-14 — muvâzene DEĞİL: fâsılalar kafiyelidir (ayn), mütevâzî secidir."}],
 "commonMistakes": [
  {"wrong": "«مَرْفُوعَةٌ / مَوْضُوعَةٌ muvâzenedir: ikisi de مَفْعُولَة»",
   "right": "«Vezin eş, fakat revî de eş (ayn): bu seci mütevâzîdir; muvâzene, vezin eş revî FARKLI olandır»",
   "why": {"en": "The muwazana is defined by what it lacks: دُونَ التَّقْفِيَةِ. A shared rawi makes it sajʿ, whatever the wazn.", "tr": "Muvâzene eksiğiyle tanımlanır: دُونَ التَّقْفِيَةِ. Ortak revî, vezin ne olursa olsun, onu seci yapar."}}],
 "relatedNotes": ["saj", "tashtir", "ilm-al-badi"]}

NOTE_Q = {
 "id": "qalb-al-kull",
 "title": {"ar": "قَلْبُ الْكُلِّ — اللَّفْظُ يُقْرَأُ مِنْ آخِرِهِ", "en": "The qalb of the whole — the line read from its end", "tr": "Kalb-i küll — mısra sonundan okunur"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — والقلب: أن يكون اللفظ يقرأ من آخره كما يقرأ من أوله"],
 "question": {
  "en": ["Do the bare letters of the line read the same BACKWARDS? مَوَدَّتُهُ تَدُومُ لِكُلِّ هَوْلٍ وَهَلْ كُلٌّ مَوَدَّتُهُ تَدُومُ (al-Arrajani) — strip the marks and the spaces and reverse: the same string. So too وَرَبَّكَ فَكَبِّرْ (74:3): ر ب ك ف ك ب ر.",
         "What does the engine read? Only letters — hamza seats folded, the ta marbuta as ha, a joining waw on the first word set aside (it is not of the line) — and it claims the figure only when the whole string, or a whole hemistich, is a palindrome. A near-miss is nothing."],
  "tr": ["Mısraın çıplak harfleri TERSTEN de aynı okunuyor mu? مَوَدَّتُهُ تَدُومُ لِكُلِّ هَوْلٍ وَهَلْ كُلٌّ مَوَدَّتُهُ تَدُومُ (Errecânî) — harekeleri ve boşlukları at, tersine çevir: aynı dizi. وَرَبَّكَ فَكَبِّرْ (Müddessir 3) de öyle: ر ب ك ف ك ب ر.",
         "Motor neyi okur? Yalnız harfleri — hemze oturakları katlanır, tâ-i merbûta hâ sayılır, ilk kelimedeki atıf vâvı bir yana konur (mısradan değildir) — ve sanatı ancak bütün dizi yahut bütün bir mısra palindrom ise iddia eder. Az kaçırmak hiçtir."]},
 "plain": {
  "en": "A line whose letters read the same from either end.",
  "tr": "Harfleri iki uçtan aynı okunan bir mısra."},
 "explanation": {
  "en": "وَالْقَلْبُ أَنْ يُقْرَأَ اللَّفْظُ مِنْ آخِرِهِ كَمَا يُقْرَأُ مِنْ أَوَّلِهِ. The jinas of qalb (jinas-qalb) reverses the letters of ONE word into another (فَتْح / حَتْف); the qalb of the whole reverses a whole utterance into itself. It is the one figure of wording an engine can settle with no lexicon at all: the letters are the claim and the letters are the proof. Al-Arrajani's bayt and the aya وَرَبَّكَ فَكَبِّرْ are the book's two examples; the waw of وَرَبَّكَ is the joiner and stands outside the mirror.",
  "tr": "وَالْقَلْبُ أَنْ يُقْرَأَ اللَّفْظُ مِنْ آخِرِهِ كَمَا يُقْرَأُ مِنْ أَوَّلِهِ. Kalb cinâsı (jinas-qalb) BİR kelimenin harflerini başka bir kelimeye çevirir (فَتْح / حَتْف); bütünün kalbi bütün bir sözü kendisine çevirir. Motorun hiç sözlüksüz kesebildiği tek lafız sanatıdır: harfler iddiadır, harfler delildir. Errecânî'nin beyti ve وَرَبَّكَ فَكَبِّرْ âyeti kitabın iki örneğidir; وَرَبَّكَ'nin vâvı atıf vâvıdır, aynanın dışında durur."},
 "examples": [
  {"ar": "مَوَدَّتُهُ تَدُومُ لِكُلِّ هَوْلٍ وَهَلْ كُلٌّ مَوَدَّتُهُ تَدُومُ", "en": "al-Arrajani — the whole bayt.", "tr": "Errecânî — bütün beyit.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "وَرَبَّكَ فَكَبِّرْ", "en": "74:3 — seven letters, mirrored.", "tr": "Müddessir 3 — yedi harf, aynalı.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"}],
 "commonMistakes": [
  {"wrong": "«كُلٌّ فِي فَلَكٍ palindromdur, öyleyse kalb-i küll»",
   "right": "«Evet: ك ل ف ي ف ل ك — Yâsîn 40'ın bu parçası da bütünün kalbidir; motor onu da harflerinden okur»",
   "why": {"en": "The test is mechanical; the book's list is not exhaustive. Any string that mirrors is a qalb.", "tr": "Ölçü mekaniktir; kitabın listesi tüketici değildir. Aynalanan her dizi kalbdir."}}],
 "relatedNotes": ["jinas-qalb", "jinas", "ilm-al-badi"]}

NOTE_T = {
 "id": "tashri",
 "title": {"ar": "التَّشْرِيعُ — بَيْتٌ عَلَى قَافِيَتَيْنِ", "en": "The tashriʿ — a bayt on two rhymes", "tr": "Teşrî' — iki kafiyeli beyit"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التشريع: بناء البيت على قافيتين يصح المعنى عند الوقوف على كل منهما"],
 "question": {
  "en": ["Can the bayt stop EARLY and still be whole? يَا خَاطِبَ الدُّنْيَا الدَّنِيَّةِ — a complete call; إِنَّهَا شَرَكُ الرَّدَى وَقَرَارَةُ الْأَكْدَارِ — the full bayt. Two rhymes (the ya-ta, the ra), and the sense holds at either: TASHRIʿ.",
         "What does the engine read? Where the sense is whole is meaning, so the two stops are the author's; the engine confirms the surface — the two stops end on different rhyme letters, the second closes the bayt, the first stands inside the first hemistich — and refuses anything else."],
  "tr": ["Beyit ERKEN durup yine de tam kalabiliyor mu? يَا خَاطِبَ الدُّنْيَا الدَّنِيَّةِ — tam bir nidâ; إِنَّهَا شَرَكُ الرَّدَى وَقَرَارَةُ الْأَكْدَارِ — bütün beyit. İki kafiye (yâ-tâ, râ), mana ikisinde de tutar: TEŞRÎ'.",
         "Motor neyi okur? Mananın nerede tam olduğu mana işidir, iki durak yazarındır; motor yüzeyi doğrular — iki durak farklı revî harfleriyle biter, ikincisi beyti kapar, birincisi birinci mısraın içinde durur — ve gerisini reddeder."]},
 "plain": {
  "en": "A bayt built so that it can stop at an earlier rhyme and still make sense.",
  "tr": "Daha önceki bir kafiyede durabilen ve yine mana veren bir beyit."},
 "explanation": {
  "en": "وَالتَّشْرِيعُ بِنَاءُ الْبَيْتِ عَلَى قَافِيَتَيْنِ يَصِحُّ الْمَعْنَى عِنْدَ الْوُقُوفِ عَلَى كُلٍّ مِنْهُمَا. Al-Hariri's line can be recited as a short bayt of one metre ending at الدَّنِيَّةِ, or as the long bayt ending at الْأَكْدَارِ — the poet «legislated» two roads through one line, whence the name. The figure lives in the metre and the sense together, which is why the app shows the two stops and does not pretend to compute where a sense is whole.",
  "tr": "وَالتَّشْرِيعُ بِنَاءُ الْبَيْتِ عَلَى قَافِيَتَيْنِ يَصِحُّ الْمَعْنَى عِنْدَ الْوُقُوفِ عَلَى كُلٍّ مِنْهُمَا. Harîrî'nin mısraı الدَّنِيَّةِ'de biten kısa bir beyit olarak da الْأَكْدَارِ'da biten uzun beyit olarak da okunabilir — şair tek mısrada iki yol «teşrî' etmiştir», ad bundandır. Sanat vezinle mana birlikte yaşar; bu yüzden uygulama iki durağı gösterir ve mananın nerede tam olduğunu hesaplar gibi yapmaz."},
 "examples": [
  {"ar": "يَا خَاطِبَ الدُّنْيَا الدَّنِيَّةِ إِنَّهَا * شَرَكُ الرَّدَى وَقَرَارَةُ الْأَكْدَارِ", "en": "al-Hariri — stop at الدَّنِيَّةِ or at الْأَكْدَارِ.", "tr": "Harîrî — الدَّنِيَّةِ'de yahut الْأَكْدَارِ'da dur.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«Beyitte iki kafiye kelimesi var: teşrî'»",
   "right": "«Teşrî', ilk kafiyede DURULUNCA mananın tam olmasıdır; kafiye kelimelerinin çokluğu değil»",
   "why": {"en": "The figure is a property of the sense at the stop, not of the sounds; two rhyme words with a broken sense at the first are ordinary verse.", "tr": "Sanat, seslerin değil, duraktaki mananın vasfıdır; ilkinde manası kırık iki kafiye kelimesi sıradan nazımdır."}}],
 "relatedNotes": ["saj", "tashtir", "ilm-al-badi"]}

NOTE_L = {
 "id": "luzum-ma-la-yalzam",
 "title": {"ar": "لُزُومُ مَا لَا يَلْزَمُ — حَرْفٌ قَبْلَ الرَّوِيِّ", "en": "Luzum ma la yalzam — a letter kept before the rawi", "tr": "Lüzûm-i mâ lâ yelzem — revîden önce korunan harf"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — لزوم ما لا يلزم: أن يجيء قبل حرف الروي أو ما في معناه من الفاصلة ما ليس بلازم في السجع"],
 "question": {
  "en": ["What does the sajʿ REQUIRE of two fasilas? The rawi letter alone. What does the poet keep beyond it? فَلَا تَقْهَرْ … فَلَا تَنْهَرْ (93:9-10) end on the ra — and both keep the HA before it, which nothing required: luzum ma la yalzam, «requiring what is not required».",
         "In Abu Tammam's three bayts the rhyme is the ta (جَلَّتِ، زَلَّتِ، تَجَلَّتِ) and the LAM before it is kept through all three.",
         "What does the engine read? Which pair is a rhyme is the author's (a bayt's rhymes lie across sentences); the engine takes the authored rhyme words, reads the pausal form's last letter as the rawi and the letter before it as the kept one, refuses a madd letter there (that is the ridf every rhyme may carry), and confirms the other bayts of the chapter keep the same letter."],
  "tr": ["Seci iki fâsıladan ne İSTER? Yalnız revî harfini. Şair onun ötesinde neyi korur? فَلَا تَقْهَرْ … فَلَا تَنْهَرْ (Duhâ 9-10) râ ile biter — ve ikisi de ondan önceki HÂ'yı korur, hiçbir şey istemediği halde: lüzûm-i mâ lâ yelzem, «gerekmeyeni gerektirmek».",
         "Ebû Temmâm'ın üç beytinde kafiye tâ'dır (جَلَّتِ، زَلَّتِ، تَجَلَّتِ) ve ondan önceki LÂM üçünde de korunur.",
         "Motor neyi okur? Hangi çiftin kafiye olduğu yazarındır (beyit kafiyeleri cümleler arasında yatar); motor yazılmış kafiye kelimelerini alır, vakıf şeklinin son harfini revî, öncekini korunan harf olarak okur, orada med harfini reddeder (o her kafiyenin taşıyabildiği ridftir) ve bâbın öbür beyitlerinin aynı harfi koruduğunu doğrular."]},
 "plain": {
  "en": "Keeping, before the rhyme letter, a letter the rhyme never asked for — in every fasila of the piece.",
  "tr": "Kafiye harfinden önce, kafiyenin hiç istemediği bir harfi — parçanın her fâsılasında — korumak."},
 "explanation": {
  "en": "وَلُزُومُ مَا لَا يَلْزَمُ أَنْ يَجِيءَ قَبْلَ حَرْفِ الرَّوِيِّ أَوْ مَا فِي مَعْنَاهُ مِنَ الْفَاصِلَةِ مَا لَيْسَ بِلَازِمٍ فِي السَّجْعِ. The rawi is the letter the rhyme is built on — the ra of تَقْهَرْ, the ta of جَلَّتِ; the letter before it is free, and a poet who binds it too has taken on a constraint the art did not impose. Abu al-ʿAlaʾ built a whole diwan on it (the Luzumiyyat). The madd letter before a rawi (the ridf: the waw of مَخْضُودٍ) is not this figure — every rhyme may carry it.",
  "tr": "وَلُزُومُ مَا لَا يَلْزَمُ أَنْ يَجِيءَ قَبْلَ حَرْفِ الرَّوِيِّ أَوْ مَا فِي مَعْنَاهُ مِنَ الْفَاصِلَةِ مَا لَيْسَ بِلَازِمٍ فِي السَّجْعِ. Revî, kafiyenin üzerine kurulduğu harftir — تَقْهَرْ'ın râ'sı, جَلَّتِ'nin tâ'sı; ondan önceki harf serbesttir, onu da bağlayan şair sanatın yüklemediği bir kayıt yüklenmiştir. Ebü'l-Alâ bütün bir dîvânı bunun üzerine kurdu (Lüzûmiyyât). Revîden önceki med harfi (ridf: مَخْضُودٍ'in vâvı) bu sanat değildir — her kafiye onu taşıyabilir."},
 "examples": [
  {"ar": "فَأَمَّا الْيَتِيمَ فَلَا تَقْهَرْ وَأَمَّا السَّائِلَ فَلَا تَنْهَرْ", "en": "93:9-10 — the ha before the ra.", "tr": "Duhâ 9-10 — râ'dan önceki hâ.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "سَأَشْكُرُ عَمْرًا إِنْ تَرَاخَتْ مَنِيَّتِي * أَيَادِيَ لَمْ تُمْنَنْ وَإِنْ هِيَ جَلَّتِ", "en": "Abu Tammam — the lam before the ta, kept for three bayts.", "tr": "Ebû Temmâm — tâ'dan önceki lâm, üç beyit boyunca.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"}],
 "commonMistakes": [
  {"wrong": "«مَخْضُودٍ / مَنْضُودٍ'de dâl'dan önceki vâv korunuyor: lüzûm»",
   "right": "«O vâv med harfidir (ridf) ve kafiyenin olağan taşıyıcısıdır; lüzûm, med olmayan bir harfin korunmasıdır»",
   "why": {"en": "The ridf belongs to the rhyme's own machinery; the figure is a constraint beyond it, and the engine refuses a madd letter in the kept seat for exactly this reason.", "tr": "Ridf kafiyenin kendi düzeneğindendir; sanat onun ötesinde bir kayıttır ve motor tam bu yüzden korunan yerde med harfini reddeder."}}],
 "relatedNotes": ["saj", "radd-al-ajuz", "ilm-al-badi"]}

ADD_EN = (" Chapter 72 (lines ~4569-4612, sahifa 158-159) closes the lafzi embellishments: the muwazana (s1; 88:15-16 s2) and its mumathala "
          "(s3; 37:117-118 s4; Abu Tammam s5), the qalb of the whole (s6; al-Arrajani s7; 74:3 s8), the tashriʿ (s9; al-Hariri s10), luzum ma la "
          "yalzam (s11; 93:9-10 s12; Abu Tammam's three bayts s13-s15) and the closing principle that the words follow the meanings (s16). The "
          "rulings are RESTORED from the received matn and marked; the examples are the source's printed Arabic. The `badi` frames: `muwazana` "
          "(with `sub` mumathala where the chapter says so) carries the `pair` of fasilas; `qalb-kull` the `pair` of the line's first and last "
          "words; `tashri` the `pair` of stops; `luzum` a `pair` within a sentence (s12) or the rhyme `word` of each bayt with the kept `letter`.")
ADD_TR = (" Yetmiş ikinci bâb (satır ~4569-4612, sahife 158-159) lafzî muhassinâtı kapatır: muvâzene (s1; Gâşiye 15-16 s2) ve mümâselesi (s3; "
          "Sâffât 117-118 s4; Ebû Temmâm s5), bütünün kalbi (s6; Errecânî s7; Müddessir 3 s8), teşrî' (s9; Harîrî s10), lüzûm-i mâ lâ yelzem "
          "(s11; Duhâ 9-10 s12; Ebû Temmâm'ın üç beyti s13-s15) ve lafızların mânâlara tâbi olduğu kapanış ilkesi (s16). Hükümler alınan metinden "
          "GERİ YAZILMIŞ ve işaretlenmiştir; örnekler kaynağın basılı Arapçasıdır. `badi` çerçeveleri: `muwazana` (bâbın dediği yerde `sub` "
          "mumathala ile) fâsıla `pair`ini; `qalb-kull` mısraın ilk ve son kelimesinin `pair`ini; `tashri` durakların `pair`ini; `luzum` bir "
          "cümle içindeki `pair`i (s12) yahut her beytin kafiye `word`ünü korunan `letter` ile taşır.")
write_out(72, S, TITLE, ADD_EN, ADD_TR, "4569-4612", GLOSS_ADD, notes=(NOTE_M, NOTE_Q, NOTE_T, NOTE_L),
          related=(("saj", ["muwazana", "tashri", "luzum-ma-la-yalzam"]), ("jinas-qalb", ["qalb-al-kull"]), ("tashtir", ["tashri"]),
                   ("radd-al-ajuz", ["luzum-ma-la-yalzam"]), ("ilm-al-badi", ["muwazana", "qalb-al-kull", "tashri", "luzum-ma-la-yalzam"])))
report(72, S, GLOSS_ADD, (NOTE_M, NOTE_Q, NOTE_T, NOTE_L))
