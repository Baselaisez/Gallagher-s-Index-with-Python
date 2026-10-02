# -*- coding: utf-8 -*-
"""Author chapter 59 of talkhis-al-miftah — the IRSAD (the tashim), the
MUSHAKALA (tahqiqan / taqdiran), the MUZAWAJA and the ʿAKS in its three shapes
(sahifa 138-140, lines ~4025-4060).

  RESTORED (the source carries the step only in Turkish): s1, s4, s7-s9, s11-s14's
          heads; the frames of every example.
  As printed: the ayat (9:70, 5:116, 2:138, 10:31, 60:10) and the verses of
          ʿAmr b. Maʿdi Karib, Abu l-Rafʿ, al-Buhturi; the ʿadat/sadat saying.

Frames: irsad (the forecaster and the fasila it forecasts), mushakala (the word,
its companion, the word that would have been said, tahqiq/taqdir), muzawaja (the
shart-side and jaza-side verbs, the one verb that follows each), aks (the two
words and their swapped order, by shape: mudaf / mutaalliq / tarafayn).
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import sarf_gen as _sg

I = "irsad"; K = "mushakala"; Z = "muzawaja"; A = "aks"
TITLE = {"ar": "الْإِرْصَادُ، وَالْمُشَاكَلَةُ، وَالْمُزَاوَجَةُ، وَالْعَكْسُ",
         "en": "The Irsad; the Mushakala; the Muzawaja; the ʿAks",
         "tr": "İrsâd; Müşâkele; Müzâvece; Aks"}
S = []
def nahwa(full="نَحْوَ", tag=I, punct=":"):
    return tok(full, "nahwa", "noun", [tag, "maful-fih"], ("الْوَاوُ عَاطِفَةٌ، وَ" if full.startswith("وَ") else "") + "نَحْوَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ إِلَى الْمِثَالِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.",
               "«such as» — a zarf annexed to the example.", "«… gibi» — örneğe izâfe edilmiş zarf.",
               segments=([seg("وَ", "wa", "conj"), seg("نَحْوَ", "nahwa", "noun")] if full.startswith("وَ") else None), punct=punct)
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def minha(tag, first=False):
    t = tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — مِنَ الْوُجُوهِ الْمَعْنَوِيَّةِ.", "«and among them» — a fronted khabar.", "«ve onlardan» — öne alınmış haber.",
            segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
    return t
def wahiya(tag):
    return tok("وَهِيَ","hiya","pron",[tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
               segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")])
def an_masd(tag):
    return tok("أَنْ","an","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the interpreted masdar is the khabar.", "«… -mesi» — müevvel masdar haber.")

# ----------- s1 — the irsad defined (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the IRSAD, which some call the TASHIM: that before the CLOSE of the prose-clause or the verse there be set what POINTS TO IT, once the rhyme-letter is known." + R_EN,
 "tr": "Onlardan biri, bazılarının TESHÎM dediği İRSÂDDIR: revî harfi bilindiğinde, fıkranın yahut beytin SONUNDAN önce ona DELÂLET EDEN bir şey konulması." + R_TR},
 "tokens": [
  minha(I),
  tok("الْإِرْصَادُ","irsad","noun",[I, "mubtada-khabar", "masdar", "form-iv-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ أَرْصَدَ: أَعَدَّ وَرَقَبَ.", "«the irsad» — the delayed mubtada; masdar of أَرْصَدَ, to lie in wait, to set ready.", "«irsâd» — sona kalmış mübtedâ; أَرْصَدَ'nin masdarı: hazırlamak, gözetlemek.", punct="،"),
  wa_conj("وَيُسَمِّيهِ","samma","verb",[I, "atf-nasaq", "mafulayn", "form-ii-verbs", "naqis-verbs"], "يُسَمِّي فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«and call it».", "«ve ona … der».", pron=("هِ","pron-3ms")),
  tok("بَعْضُهُمُ","baad","noun",[I, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْمِيمُ حُرِّكَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«some of them» — the doer; the mim voweled before the sakin.", "«bazıları» — fâil; mîm iki sâkin için harekelenmiş.",
      segments=[seg("بَعْضُ","baad","noun"), seg("هُمُ","pron-3mp","pron")]),
  tok("التَّسْهِيمَ","tashim","noun",[I, "mafulayn", "masdar", "form-ii-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ سَهَّمَ: جَعَلَهُ كَالسَّهْمِ، أَيْ خَطًّا مُسْتَقِيمًا.", "«the tashim» — the second object; masdar of سَهَّمَ: to draw a straight line, like an arrow.", "«teshîm» — ikinci mef'ûl; سَهَّمَ'nin masdarı: ok gibi düz çizgi çekmek.", punct="،"),
  wahiya(I), an_masd(I),
  tok("يُجْعَلَ","jaala","verb",[I, "an-masdariyya", "naib-al-fail", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«there be set» — the passive.", "«konulsun» — meçhûl."),
  tok("قَبْلَ","qabla","noun",[I, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«before» — a zarf.", "«… -den önce» — zarf."),
  tok("الْعَجُزِ","ajuz","noun",[I, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْعَجُزُ: آخِرُ الْبَيْتِ أَوِ الْفِقْرَةِ.", "«the close» — the last word of the verse or clause.", "«acüz» — beytin yahut fıkranın son kelimesi."),
  tok("مِنَ","min","part",[I, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-in»."),
  tok("الْفِقْرَةِ","fiqra","noun",[I, "huruf-jarr"], "مَجْرُورٌ — الْفِقْرَةُ: الْقَرِينَةُ مِنَ النَّثْرِ.", "«the prose-clause» — one member of rhymed prose.", "«fıkra» — nesirden bir cümle, secî karînesi."),
  tok("أَوِ","aw","conj",[I, "atf-nasaq"], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«yahut»."),
  tok("الْبَيْتِ","bayt","noun",[I, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«the verse».", "«beyit»."),
  tok("مَا","ma-mawsula","pron",[I, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ.", "«what» — the deputy doer.", "«… şey» — nâib-i fâil."),
  tok("يَدُلُّ","dalla","verb",[I, "ism-mawsul", "fail", "doubled-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مُضَاعَفٌ، وَالْفَاعِلُ مُسْتَتِرٌ؛ صِلَةٌ.", "«points» — the doubled verb; the sila.", "«delâlet eder» — muzâaf fiil; sıla."),
  tok("عَلَيْهِ","ala","part",[I, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — عَلَى الْعَجُزِ.", "«to it» — to the close.", "«ona» — acüze.",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")]),
  tok("إِذَا","idha","part",[I, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when, once».", "«… -diğinde»."),
  tok("عُرِفَ","arafa","verb",[I, "idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is known».", "«bilinir»."),
  tok("الرَّوِيُّ","rawiyy","noun",[I, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الرَّوِيُّ: الْحَرْفُ الَّذِي تُبْنَى عَلَيْهِ الْقَافِيَةُ.", "«the rhyme-letter» — the letter the rhyme is built on.", "«revî» — kafiyenin üzerine kurulduğu harf.", punct=".")]})

# ----------- s2 — 9:70
S.append({"id": "s2", "translation": {
 "en": "Such as: «God WOULD NOT WRONG THEM; but it was themselves they were WRONGING» (9:70)." + R_EN,
 "tr": "«Allah onlara ZULMEDECEK DEĞİLDİ; fakat onlar kendilerine ZULMEDİYORLARDI» (Tevbe 9:70) gibi." + R_TR},
 "badi": [{"kind": "irsad", "pair": [4, 8]}],
 "tokens": [
  nahwa(),
  tok("فَمَا","ma-nafiya","part",[I, "kana-wa-akhawatuha"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَمَا نَافِيَةٌ.", "«so not» — the negating ma.", "«ve … değildi» — nefiy mâsı.",
      segments=[seg("فَ","fa","conj"), seg("مَا","ma-nafiya","part")]),
  tok("كَانَ","kana","verb",[I, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«was» — kana.", "«idi» — kâne."),
  tok("اللهُ","allah","noun",[I, "kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«God» — the ism of kana.", "«Allah» — kânenin ismi."),
  tok("لِيَظْلِمَهُمْ","zalama","verb",[I, "lam-taleel", "kana-wa-akhawatuha", "maful-bihi"], "اللَّامُ لَامُ الْجُحُودِ بَعْدَ مَا كَانَ، وَيَظْلِمَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَهُمْ مَفْعُولٌ بِهِ؛ وَالْخَبَرُ مَحْذُوفٌ — الْإِرْصَادُ: يَدُلُّ عَلَى يَظْلِمُونَ.", "«to wrong them» — the lam of denial after «was not»; nasb by a hidden an — the IRSAD: it forecasts «wronging».", "«onlara zulmedecek» — «değildi»den sonra cuhûd lâmı; gizli en ile mansub — İRSÂD: «zulmediyorlardı»yı haber verir.",
      segments=[seg("لِ","li","part"), seg("يَظْلِمَ","zalama","verb"), seg("هُمْ","pron-3mp","pron")]),
  wa_conj("وَلَكِنْ","lakin","part",[I, "atf-nasaq"], "لَكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lakin, no government.", "«fakat» — muhaffef lâkin, amelsiz."),
  tok("كَانُوا","kana","verb",[I, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«they were» — the waw its ism.", "«onlar … idi» — vâv ismi.",
      segments=[seg("كَانُ","kana","verb"), seg("وا","pron-3mp","pron")]),
  tok("أَنْفُسَهُمْ","nafs","noun",[I, "maful-bihi", "idafa-definiteness", "jam-taksir", "taqdim-al-musnad"], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ — قُدِّمَ لِلْحَصْرِ.", "«themselves» — the object fronted for restriction.", "«kendilerine» — hasr için öne alınmış mef'ûl.",
      segments=[seg("أَنْفُسَ","nafs","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("يَظْلِمُونَ","zalama","verb",[I, "kana-wa-akhawatuha", "fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ؛ وَالْجُمْلَةُ خَبَرُ كَانُوا — الْعَجُزُ الْمَرْصُودُ.", "«wronging» — kana's khabar; the close that was forecast.", "«zulmediyorlardı» — kânenin haberi; haber verilen acüz.",
      segments=[seg("يَظْلِمُ","zalama","verb"), seg("ونَ","pron-3mp","pron")], punct=".")]})

# ----------- s3 — ʿAmr b. Maʿdi Karib
S.append({"id": "s3", "translation": {
 "en": "And the verse of ʿAmr b. Maʿdikarib: «When you CANNOT do a thing, leave it — and pass on to what you CAN»." + R_EN,
 "tr": "Ve Amr b. Ma'dîkerib'in beyti: «Bir işe GÜCÜN YETMEDİĞİNDE onu bırak — gücünün YETTİĞİNE geç»." + R_TR},
 "badi": [{"kind": "irsad", "pair": [5, 11]}, bd("tibaq", [5, 11], sub="salb", cls="fil")],
 "tokens": [
  wa_conj("وَقَوْلِ","qawl","noun",[I, "atf-nasaq", "idafa-definiteness"], "قَوْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve sözü»."),
  tok("عَمْرِو","amr-ibn-madikarib","noun",[I, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَمْرُو بْنُ مَعْدِي كَرِبَ الزُّبَيْدِيُّ، الْفَارِسُ الْمُخَضْرَمُ.", "«ʿAmr» — b. Maʿdi Karib al-Zubaydi, the knight who saw both ages.", "«Amr» — b. Ma'dîkerib ez-Zübeydî, muhadram süvari."),
  tok("بْنِ","ibn","noun",[I, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ، مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("مَعْدِيكَرِبَ","madikarib","noun",[I, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْفَتْحِ — مُرَكَّبٌ مَزْجِيٌّ، يُكْتَبُ كَلِمَةً وَاحِدَةً.", "«Maʿdikarib» — a compound name, fixed on the fatha, written as one word.", "«Ma'dîkerib» — mezcî mürekkeb, fetha üzere mebnî, tek kelime yazılır.", punct=":"),
  tok("إِذَا","idha","part",[I, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«… -diğinde»."),
  tok("لَمْ","lam","part",[I, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — the jazm particle.", "«-me» — cezm harfi."),
  tok("تَسْتَطِعْ","istataa","verb",[I, "lam-jazim", "form-x-verbs", "hollow-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنْتَ؛ الْإِرْصَادُ: يَدُلُّ عَلَى تَسْتَطِيعُ فِي الْعَجُزِ.", "«you cannot» — jazm by lam, the hollow ya dropped; the IRSAD forecasting «you can» at the close.", "«gücün yetmez» — lem ile meczûm, ecvef yâ düşmüş; İRSÂD, sondaki «gücün yeter»i haber verir."),
  tok("أَمْرًا","amr","noun",[I, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a thing» — the object.", "«bir işe» — mef'ûl."),
  tok("فَدَعْهُ","da-leave","verb",[I, "imperative-amr", "maful-bihi", "jawab-al-talab"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَدَعْ فِعْلُ أَمْرٍ مِنْ وَدَعَ، أُمِيتَ مَاضِيهِ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«leave it» — the fa of the answer; the imperative of وَدَعَ, whose past is dead.", "«onu bırak» — cevap fâsı; وَدَعَ'nin emri, mâzîsi ölü.",
      segments=[seg("فَ","fa","conj"), seg("دَعْ","da-leave","verb"), seg("هُ","pron-3ms","pron")], punct="*"),
  wa_conj("وَجَاوِزْهُ","jawaza3","verb",[I, "atf-nasaq", "imperative-amr", "form-iii-verbs", "maful-bihi"], "جَاوِزْ فِعْلُ أَمْرٍ مِنَ الْمُفَاعَلَةِ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and pass beyond it» — the imperative of Form III.", "«ve onu geç» — III. bâbın emri.", pron=("هُ","pron-3ms")),
  tok("إِلَى","ila","part",[I, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("مَا","ma-mawsula","pron",[I, "ism-mawsul", "huruf-jarr"], "اسْمٌ مَوْصُولٌ مَجْرُورٌ.", "«what».", "«… şeye»."),
  tok("تَسْتَطِيعُ","istataa","verb",[I, "ism-mawsul", "fail", "form-x-verbs", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنْتَ؛ صِلَةٌ — الْعَجُزُ الْمَرْصُودُ: طِبَاقُ سَلْبٍ مَعَ لَمْ تَسْتَطِعْ.", "«you can» — the forecast close; a tibaq of negation with «you cannot».", "«gücün yeter» — haber verilen acüz; «yetmez» ile selb tıbâkı.", punct=".")]})
S[-1]["badi"] = [{"kind": "irsad", "pair": [6, 12]}, bd("tibaq", [6, 12], sub="salb", cls="fil")]

# ----------- s4 — the mushakala defined (RESTORED matn)
S.append({"id": "s4", "translation": {
 "en": "Among them is the MUSHAKALA: the mention of a thing by the WORD OF ANOTHER, because it falls in that other's COMPANY — in fact, or in estimation." + R_EN,
 "tr": "Onlardan biri MÜŞÂKELEDİR: bir şeyi, BAŞKASININ SOHBETİNDE bulunduğu için — tahkîkan yahut takdîren — o başkasının LAFZIYLA anmak." + R_TR},
 "tokens": [
  minha(K),
  tok("الْمُشَاكَلَةُ","mushakala","noun",[K, "mubtada-khabar", "masdar", "form-iii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ شَاكَلَ: شَابَهَ فِي الشَّكْلِ.", "«the mushakala» — masdar of شَاكَلَ, to match in shape.", "«müşâkele» — شَاكَلَ'nin masdarı: şekilce benzemek.", punct="،"),
  wahiya(K),
  tok("ذِكْرُ","dhikr","noun",[K, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the mention of» — the khabar.", "«anmak» — haber."),
  tok("الشَّيْءِ","shay","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyi»."),
  tok("بِلَفْظِ","lafz","noun",[K, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«by the word of».", "«lafzıyla».",
      segments=[seg("بِ","bi","part"), seg("لَفْظِ","lafz","noun")]),
  tok("غَيْرِهِ","ghayr","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«another».", "«başkasının».",
      segments=[seg("غَيْرِ","ghayr","noun"), seg("هِ","pron-3ms","pron")]),
  tok("لِوُقُوعِهِ","wuqu","noun",[K, "huruf-jarr", "lam-taleel", "idafa-definiteness", "masdar"], "اللَّامُ لِلتَّعْلِيلِ، وَوُقُوعِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ وَقَعَ.", "«because it falls» — the lam of cause over the masdar.", "«bulunduğu için» — ta'lîl lâmı ve masdar.",
      segments=[seg("لِ","li","part"), seg("وُقُوعِ","wuqu","noun"), seg("هِ","pron-3ms","pron")]),
  tok("فِي","fi","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("صُحْبَتِهِ","suhba","noun",[K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — صُحْبَةِ الْغَيْرِ.", "«its company» — the other's company.", "«sohbetinde» — başkasının sohbetinde.",
      segments=[seg("صُحْبَتِ","suhba","noun"), seg("هِ","pron-3ms","pron")]),
  tok("تَحْقِيقًا","tahqiq","noun",[K, "hal", "masdar", "form-ii-verbs"], "حَالٌ مَنْصُوبٌ — أَيْ: صُحْبَةً مَذْكُورَةً فِي اللَّفْظِ.", "«in fact» — a hal: the company actually spoken.", "«tahkîkan» — hâl: sohbet lafızda zikredilmiş."),
  tok("أَوْ","aw","conj",[K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("تَقْدِيرًا","taqdir","noun",[K, "atf-nasaq", "masdar", "form-ii-verbs"], "مَعْطُوفٌ مَنْصُوبٌ — صُحْبَةً مُقَدَّرَةً غَيْرَ مَذْكُورَةٍ.", "«in estimation» — a company understood, not spoken.", "«takdîren» — takdir edilen, zikredilmemiş sohbet.", punct=".")]})

# ----------- s5 — Abu l-Rafʿ: the tahqiq
S.append({"id": "s5", "translation": {
 "en": "The example of the actual: «They said: ask for something, and we shall COOK it well for you. I said: COOK me a cloak and a shirt.»" + R_EN,
 "tr": "Tahkîkin örneği: «Dediler: bir şey iste, sana onu güzelce PİŞİRELİM. Dedim: bana bir cübbe ile bir gömlek PİŞİRİN.»" + R_TR},
 "badi": [{"kind": "mushakala", "word": 8, "companion": 6, "sub": "tahqiq", "asl": "خِيطُوا"}],
 "tokens": [
  tok("مِثَالُ","mithal","noun",[K, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — وَالْخَبَرُ الْبَيْتُ.", "«the example of».", "«örneği»."),
  tok("التَّحْقِيقِ","tahqiq","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the actual».", "«tahkîkin».", punct=":"),
  tok("قَالُوا","qala","verb",[K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«they said».", "«dediler».",
      segments=[seg("قَالُ","qala","verb"), seg("وا","pron-3mp","pron")]),
  tok("اقْتَرِحْ","iqtaraha","verb",[K, "imperative-amr", "form-viii-verbs", "maful-bihi"], "فِعْلُ أَمْرٍ مِنَ الِافْتِعَالِ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنْتَ.", "«ask for, propose» — the imperative of Form VIII.", "«iste, teklif et» — VIII. bâbın emri."),
  tok("شَيْئًا","shay","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«something».", "«bir şey»."),
  tok("نُجِدْ","ajada","verb",[K, "jawab-al-talab", "form-iv-verbs", "hollow-verbs", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ، وَالْفَاعِلُ مُسْتَتِرٌ — نَحْنُ؛ أَجَادَ الشَّيْءَ: أَحْسَنَهُ.", "«we shall do well» — jazm as the answer to the request; «We» concealed.", "«güzelce yapalım» — talebin cevabı olarak meczûm; «biz» gizli."),
  tok("لَكَ","lahu","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for you».", "«sana».",
      segments=[seg("لَ","li","part"), seg("كَ","pron-2ms","pron")]),
  tok("طَبْخَهُ","tabkh","noun",[K, "maful-bihi", "idafa-definiteness", "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — صَاحِبُ الْمُشَاكَلَةِ: لَفْظُ الطَّبْخِ الَّذِي وَقَعَ بَعْدَهُ اطْبُخُوا.", "«the cooking of it» — the COMPANION: the word of cooking after which «cook» will fall.", "«pişirmesini» — REFİK: sonrasında «pişirin»in düşeceği pişirme lafzı.",
      segments=[seg("طَبْخَ","tabkh","noun"), seg("هُ","pron-3ms","pron")], punct="*"),
  tok("قُلْتُ","qala","verb",[K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I said».", "«dedim».",
      segments=[seg("قُلْ","qala","verb"), seg("تُ","pron-1s","pron")], punct=":"),
  tok("اطْبُخُوا","tabakha","verb",[K, "imperative-amr", "fail", "maful-bihi"], "فِعْلُ أَمْرٍ، وَالْوَاوُ فَاعِلٌ — الْمُشَاكَلَةُ: أُرِيدَ خِيطُوا، فَذُكِرَ بِلَفْظِ الطَّبْخِ لِوُقُوعِهِ فِي صُحْبَتِهِ.", "«cook» — the MUSHAKALA: «sew» is meant, said with the word of cooking because it fell in its company.", "«pişirin» — MÜŞÂKELE: «dikin» kastedilmiş, pişirme sohbetinde düştüğü için onun lafzıyla söylenmiş.",
      segments=[seg("اطْبُخُ","tabakha","verb"), seg("وا","pron-2mp","pron")]),
  tok("لِي","lahu","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for me».", "«bana».",
      segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("جُبَّةً","jubba","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a cloak».", "«bir cübbe»."),
  wa_conj("وَقَمِيصًا","qamis","noun",[K, "atf-nasaq"], "قَمِيصًا مَعْطُوفٌ مَنْصُوبٌ.", "«and a shirt».", "«ve bir gömlek».", punct=".")]})
S[-1]["badi"] = [{"kind": "mushakala", "word": 9, "companion": 7, "sub": "tahqiq", "asl": "خِيطُوا"}]

# ----------- s6 — 5:116
S.append({"id": "s6", "translation": {
 "en": "And His saying, exalted is He: «You know what is in MY SOUL, and I do not know what is in YOUR SOUL» (5:116)." + R_EN,
 "tr": "Ve Allah teâlânın sözü: «Sen BENİM NEFSİMDEKİNİ bilirsin, ben SENİN NEFSİNDEKİNİ bilmem» (Mâide 5:116)." + R_TR},
 "badi": [{"kind": "mushakala", "word": 9, "companion": 4, "sub": "tahqiq", "asl": "مَا عِنْدَكَ / مَا فِي غَيْبِكَ"}, bd("tibaq", [2, 6], sub="salb", cls="fil")],
 "tokens": [
  kawa(K, "وَقَوْلِهِ"), taala(K),
  tok("تَعْلَمُ","alima","verb",[K, "fail", "maful-bihi", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنْتَ.", "«You know».", "«bilirsin»."),
  tok("مَا","ma-mawsula","pron",[K, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what».", "«… şeyi»."),
  tok("فِي","fi","part",[K, "huruf-jarr", "zarf-mustaqarr-wa-laghw"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«in».", "«-de»."),
  tok("نَفْسِي","nafs","noun",[K, "huruf-jarr", "idafa-definiteness", "ya-al-mutakallim"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — الصَّاحِبُ: قِيلَتْ فِي حَقِّ عِيسَى عَلَى الْحَقِيقَةِ.", "«my soul» — the companion: said of Jesus in its real sense.", "«nefsim» — refik: Îsâ hakkında hakikî mânâsında.",
      segments=[seg("نَفْسِ","nafs","noun"), seg("ي","pron-1s","pron")]),
  wa_conj("وَلَا","la-nafiya","part",[K, "atf-nasaq"], "لَا نَافِيَةٌ.", "«and not».", "«ve … -mem»."),
  tok("أَعْلَمُ","alima","verb",[K, "fail", "maful-bihi", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنَا؛ طِبَاقُ سَلْبٍ مَعَ تَعْلَمُ.", "«I know» — a tibaq of negation with «You know».", "«bilirim» — «bilirsin» ile selb tıbâkı."),
  tok("مَا","ma-mawsula","pron",[K, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what».", "«… şeyi»."),
  tok("فِي","fi","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("نَفْسِكَ","nafs","noun",[K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — الْمُشَاكَلَةُ: لَا نَفْسَ لِلهِ بِمَعْنَى الذَّاتِ الْمُرَكَّبَةِ؛ وَإِنَّمَا قِيلَ نَفْسِكَ لِتَقَدُّمِ نَفْسِي.", "«Your soul» — the MUSHAKALA: said only because «my soul» came before; «what is with You» is meant.", "«nefsin» — MÜŞÂKELE: yalnız «nefsim» önce geçtiği için söylenmiş; «Senin katındaki» kastedilmiş.",
      segments=[seg("نَفْسِ","nafs","noun"), seg("كَ","pron-2ms","pron")], punct=".")]})
S[-1]["badi"] = [{"kind": "mushakala", "word": 10, "companion": 5, "sub": "tahqiq", "asl": "مَا عِنْدَكَ"}, bd("tibaq", [2, 7], sub="salb", cls="fil")]

# ----------- s7 — the taqdir: 2:138 (frame RESTORED)
S.append({"id": "s7", "translation": {
 "en": "And the example of the estimated: «the DYE of God» (2:138) — that is, God's PURIFYING; for faith purifies souls." + R_EN,
 "tr": "Takdîrin örneği: «Allah'ın BOYASI» (Bakara 2:138) — yani Allah'ın TEMİZLEMESİ; çünkü iman nefisleri temizler." + R_TR},
 "badi": [{"kind": "mushakala", "word": 3, "sub": "taqdir", "asl": "تَطْهِير"}],
 "tokens": [
  wa_conj("وَمِثَالُ","mithal","noun",[K, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "مِثَالُ مُبْتَدَأٌ، مُضَافٌ.", "«and the example of».", "«ve örneği»."),
  tok("التَّقْدِيرِ","taqdir","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the estimated».", "«takdîrin».", punct=":"),
  tok("صِبْغَةَ","sibgha","noun",[K, "maful-mutlaq", "idafa-definiteness"], "مَصْدَرٌ مُؤَكِّدٌ لِقَوْلِهِ آمَنَّا بِاللهِ، مَنْصُوبٌ، مُضَافٌ — الْمُشَاكَلَةُ تَقْدِيرًا: أُرِيدَ التَّطْهِيرُ.", "«the dye of» — a masdar confirming «we believe in God»; the MUSHAKALA by estimation: purifying is meant.", "«boyası» — «Allah'a inandık»ı tekit eden masdar; takdîren MÜŞÂKELE: temizleme kastedilmiş."),
  tok("اللهِ","allah","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God».", "«Allah'ın».", punct="،"),
  tok("أَيْ","ay","part",[K], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  tok("تَطْهِيرَ","tathir-purify","noun",[K, "badal", "idafa-definiteness", "masdar", "form-ii-verbs"], "بَدَلٌ مِنْ صِبْغَةَ مَنْصُوبٌ — مَصْدَرُ طَهَّرَ: الْمَعْنَى الْمُرَادُ.", "«the purifying of» — badal of «dye»; the meant sense.", "«temizlemesi» — «boya»nın bedeli; kastedilen mânâ."),
  tok("اللهِ","allah","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God».", "«Allah'ın».", punct="؛"),
  tok("لِأَنَّ","anna","part",[K, "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«for».", "«çünkü».",
      segments=[seg("لِ","li","part"), seg("أَنَّ","anna","part")]),
  tok("الْإِيمَانَ","iman","noun",[K, "inna-wa-akhawatuha", "masdar", "form-iv-verbs"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«faith» — the ism of anna.", "«iman» — ennenin ismi."),
  tok("يُطَهِّرُ","tahhara","verb",[K, "inna-wa-akhawatuha", "fail", "maful-bihi", "form-ii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ؛ وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«purifies» — anna's khabar.", "«temizler» — ennenin haberi."),
  tok("النُّفُوسَ","nafs","noun",[K, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ نَفْسٍ.", "«souls» — the object.", "«nefisleri» — mef'ûl.", punct=".")]})
S[-1]["badi"] = [{"kind": "mushakala", "word": 2, "sub": "taqdir", "asl": "تَطْهِير"}]

# ----------- s8 — why the dye (RESTORED matn)
S.append({"id": "s8", "translation": {
 "en": "The origin of it: the Christians used to dip their children in a yellow water they called the BAPTISM and say «it is a purification for them»; so faith was named a DYE to match their wording." + R_EN,
 "tr": "Aslı şu: Hristiyanlar çocuklarını VAFTİZ dedikleri sarı bir suya batırır, «bu onlar için temizliktir» derlerdi; iman da onların sözüne uysun diye BOYA diye anıldı." + R_TR},
 "tokens": [
  wa_conj("وَأَصْلُهُ","asl","noun",[K, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "أَصْلُ مُبْتَدَأٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its origin».", "«ve aslı».", pron=("هُ","pron-3ms")),
  tok("أَنَّ","anna","part",[K, "inna-wa-akhawatuha", "mubtada-khabar"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that».", "«… olmasıdır»."),
  tok("النَّصَارَى","nasara-christians","noun",[K, "inna-wa-akhawatuha", "jam-taksir", "ism-maqsur-manqus"], "اسْمُ أَنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — جَمْعُ نَصْرَانِيٍّ.", "«the Christians» — plural of نَصْرَانِيّ.", "«Hristiyanlar» — نَصْرَانِيّ'in çoğulu."),
  tok("كَانُوا","kana","verb",[K, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«used to».", "«… -erlerdi».",
      segments=[seg("كَانُ","kana","verb"), seg("وا","pron-3mp","pron")]),
  tok("يَغْمِسُونَ","ghamasa","verb",[K, "kana-wa-akhawatuha", "fail", "maful-bihi", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ، وَالْوَاوُ فَاعِلٌ؛ خَبَرُ كَانُوا.", "«dip» — kana's khabar.", "«batırırlar» — kânenin haberi.",
      segments=[seg("يَغْمِسُ","ghamasa","verb"), seg("ونَ","pron-3mp","pron")]),
  tok("أَوْلَادَهُمْ","walad","noun",[K, "maful-bihi", "idafa-definiteness", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«their children».", "«çocuklarını».",
      segments=[seg("أَوْلَادَ","walad","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("فِي","fi","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-e»."),
  tok("مَاءٍ","ma-water","noun",[K, "huruf-jarr"], "مَجْرُورٌ.", "«a water».", "«bir su»."),
  tok("أَصْفَرَ","asfar","noun",[K, "naat-sifa", "mamnu-min-sarf", "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ — أَفْعَلُ لِلَّوْنِ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«yellow» — the colour أَفْعَل, diptote.", "«sarı» — renk için أَفْعَل, gayr-i munsarif."),
  tok("يُسَمُّونَهُ","samma","verb",[K, "jumla-sifa", "fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ؛ وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِمَاءٍ.", "«which they call» — a second na't of «water».", "«… dedikleri» — «su»yun ikinci na'tı.",
      segments=[seg("يُسَمُّ","samma","verb"), seg("ونَ","pron-3mp","pron"), seg("هُ","pron-3ms","pron")]),
  tok("الْمَعْمُودِيَّةَ","mamudiyya","noun",[K, "mafulayn", "ism-mansub"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«the baptism».", "«vaftiz»."),
  wa_conj("وَيَقُولُونَ","qala","verb",[K, "atf-nasaq", "fail", "hollow-verbs", "mudari-marfu"], "يَقُولُونَ مَعْطُوفٌ عَلَى يَغْمِسُونَ.", "«and say».", "«ve derler».", pron=("ونَ","pron-3mp"), punct=":"),
  tok("هُوَ","huwa","pron",[K, "mubtada-khabar"], "مُبْتَدَأٌ — الْغَمْسُ.", "«it» — the dipping.", "«o» — batırma."),
  tok("تَطْهِيرٌ","tathir-purify","noun",[K, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ.", "«a purification».", "«bir temizlik»."),
  tok("لَهُمْ","lahu","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for them».", "«onlar için».",
      segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")], punct="؛"),
  tok("فَسُمِّيَ","samma","verb",[K, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَسُمِّيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«so it was named» — the passive.", "«bu yüzden … diye anıldı» — meçhûl.",
      segments=[seg("فَ","fa","conj"), seg("سُمِّيَ","samma","verb")]),
  tok("الْإِيمَانُ","iman","noun",[K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«faith».", "«iman»."),
  tok("صِبْغَةً","sibgha","noun",[K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a dye».", "«boya»."),
  tok("لِلْمُشَاكَلَةِ","mushakala","noun",[K, "huruf-jarr", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَالْمُشَاكَلَةِ مَجْرُورٌ — صُحْبَةٌ مُقَدَّرَةٌ لَا مَذْكُورَةٌ.", "«for the mushakala» — a company estimated, not spoken.", "«müşâkele için» — takdir edilen, zikredilmemiş sohbet.",
      segments=[seg("لِ","li","part"), seg("الْمُشَاكَلَةِ","mushakala","noun")], punct=".")]})

# ----------- s9 — the muzawaja defined (RESTORED matn)
S.append({"id": "s9", "translation": {
 "en": "Among them is the MUZAWAJA: that in the CONDITION and its ANSWER two meanings be PAIRED — one consequence following each." + R_EN,
 "tr": "Onlardan biri MÜZÂVECEDİR: ŞART ile CEZÂDA iki mânânın ÇİFTLENMESİ — her birinin ardından aynı sonucun gelmesi." + R_TR},
 "tokens": [
  minha(Z),
  tok("الْمُزَاوَجَةُ","muzawaja","noun",[Z, "mubtada-khabar", "masdar", "form-iii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ زَاوَجَ: قَرَنَ.", "«the muzawaja» — masdar of زَاوَجَ, to pair.", "«müzâvece» — زَاوَجَ'nin masdarı: çiftlemek.", punct="،"),
  wahiya(Z), an_masd(Z),
  tok("يُزَاوَجَ","zawaja","verb",[Z, "an-masdariyya", "naib-al-fail", "form-iii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«be paired» — the passive; its deputy doer the phrase after.", "«çiftlensin» — meçhûl; nâib-i fâili sonraki ibare."),
  tok("بَيْنَ","bayna","noun",[Z, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between».", "«arasında»."),
  tok("مَعْنَيَيْنِ","mana","noun",[Z, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two meanings».", "«iki mânâ»."),
  tok("فِي","fi","part",[Z, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الشَّرْطِ","shart","noun",[Z, "huruf-jarr"], "مَجْرُورٌ.", "«the condition».", "«şart»."),
  wa_conj("وَالْجَزَاءِ","jaza-answer","noun",[Z, "atf-nasaq"], "الْجَزَاءِ مَعْطُوفٌ مَجْرُورٌ — جَوَابُ الشَّرْطِ.", "«and the answer» — the shart's jawab.", "«ve cezâ» — şartın cevabı.", punct="،"),
  tok("بِأَنْ","an","part",[Z, "huruf-jarr", "an-masdariyya"], "الْبَاءُ لِلتَّصْوِيرِ، وَأَنْ مَصْدَرِيَّةٌ.", "«by» — the ba of «in that».", "«şöyle ki».",
      segments=[seg("بِ","bi","part"), seg("أَنْ","an","part")]),
  tok("يُرَتَّبَ","rattaba","verb",[Z, "an-masdariyya", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«be made to follow».", "«tertip edilsin»."),
  tok("عَلَى","ala","part",[Z, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  tok("كُلٍّ","kull","noun",[Z, "huruf-jarr"], "مَجْرُورٌ — كُلٍّ مِنْهُمَا.", "«each» — of the two.", "«her biri» — ikisinden."),
  tok("مِنْهُمَا","min","part",[Z, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«of the two».", "«ikisinden».",
      segments=[seg("مِنْ","min","part"), seg("هُمَا","pron-3d","pron")]),
  tok("مَعْنًى","mana","noun",[Z, "naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«a meaning».", "«bir mânâ»."),
  tok("وَاحِدٌ","wahid","noun",[Z, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«one» — the same.", "«tek» — aynı.", punct=".")]})

# ----------- s10 — al-Buhturi
S.append({"id": "s10", "translation": {
 "en": "As al-Buhturi says: «Whenever the REPROACHER reproached and passion PERSISTED in me, she LISTENED to the SLANDERER and estrangement PERSISTED in her»." + R_EN,
 "tr": "Buhturî'nin dediği gibi: «KINAYAN kınayıp sevgi bende DİRETTİKÇE, o İFTİRACIYA KULAK VERDİ ve terk onda DİRETTİ»." + R_TR},
 "badi": [{"kind": "muzawaja", "first": [5, 10], "second": [7, 13]}],
 "tokens": [
  kaq(Z, "كَقَوْلِ", "pron-3ms"),
  tok("الْبُحْتُرِيِّ","buhturi","noun",[Z, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Buhturi».", "«Buhturî».", punct=":"),
  tok("إِذَا","idha","part",[Z, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«whenever».", "«… -dikçe»."),
  tok("مَا","ma-zaida","part",[Z, "anwa-ma"], "زَائِدَةٌ لِلتَّوْكِيدِ.", "«(ma) — redundant, for stress».", "«(mâ) — zâid, tekit için»."),
  tok("نَهَى","naha","verb",[Z, "idha-shartiyya", "fail", "naqis-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ: الْمَعْنَى الْأَوَّلُ.", "«reproached» — the shart's verb: the first meaning.", "«kınadı» — şart fiili: birinci mânâ."),
  tok("النَّاهِي","nahi","noun",[Z, "fail", "ism-fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the reproacher» — the doer; a manqus.", "«kınayan» — fâil; menkûs."),
  tok("فَلَجَّ","lajja","verb",[Z, "atf-nasaq", "fail", "doubled-verbs"], "الْفَاءُ عَاطِفَةٌ، وَلَجَّ فِعْلٌ مَاضٍ مُضَاعَفٌ — رُتِّبَ عَلَى الشَّرْطِ: اللَّجَاجُ.", "«and persisted» — the doubled verb, made to follow the shart: persistence.", "«ve diretti» — muzâaf fiil, şartın ardına konmuş: direnme.",
      segments=[seg("فَ","fa","conj"), seg("لَجَّ","lajja","verb")]),
  tok("بِيَ","bi","part",[Z, "huruf-jarr", "ya-al-mutakallim"], "جَارٌّ وَمَجْرُورٌ، فُتِحَتِ الْيَاءُ لِلْوَزْنِ.", "«in me» — the ya opened for the metre.", "«bende» — yâ vezin için fethalı.",
      segments=[seg("بِ","bi","part"), seg("يَ","pron-1s","pron")]),
  tok("الْهَوَى","hawa-love","noun",[Z, "fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«passion» — the doer; a maqsur.", "«sevgi, hevâ» — fâil; maksûr.", punct="*"),
  tok("أَصَاخَتْ","asakha","verb",[Z, "idha-shartiyya", "fail", "form-iv-verbs", "hollow-verbs", "jawab-al-talab"], "فِعْلٌ مَاضٍ مِنَ الرَّابِعِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — هِيَ؛ جَوَابُ الشَّرْطِ: الْمَعْنَى الثَّانِي.", "«she listened» — Form IV; the shart's answer: the second meaning.", "«kulak verdi» — IV. bâb; şartın cevabı: ikinci mânâ.",
      segments=[seg("أَصَاخَ","asakha","verb"), seg("تْ","ta-tanith","part")]),
  tok("إِلَى","ila","part",[Z, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْوَاشِي","washi","noun",[Z, "huruf-jarr", "ism-fail", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ: النَّمَّامُ.", "«the slanderer» — a manqus.", "«iftiracı» — menkûs."),
  tok("فَلَجَّ","lajja","verb",[Z, "atf-nasaq", "fail", "doubled-verbs"], "الْفَاءُ عَاطِفَةٌ، وَلَجَّ فِعْلٌ مَاضٍ — رُتِّبَ عَلَى الْجَزَاءِ الْمَعْنَى نَفْسُهُ: الْمُزَاوَجَةُ.", "«and persisted» — the same consequence made to follow the answer: the MUZAWAJA.", "«ve diretti» — aynı sonuç cezânın ardına konmuş: MÜZÂVECE.",
      segments=[seg("فَ","fa","conj"), seg("لَجَّ","lajja","verb")]),
  tok("بِهَا","bi","part",[Z, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«in her».", "«onda».",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("الْهَجْرُ","hajr","noun",[Z, "fail", "masdar"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ هَجَرَ: التَّرْكُ.", "«estrangement» — the doer; masdar of هَجَرَ.", "«terk, hicran» — fâil; هَجَرَ'nin masdarı.", punct=".")]})
S[-1]["badi"] = [{"kind": "muzawaja", "first": [4, 9], "second": [6, 12]}]

# ----------- s11 — the ʿaks defined (RESTORED matn)
S.append({"id": "s11", "translation": {
 "en": "Among them is the ʿAKS: that a part of the speech be put FIRST, then put LAST; and it falls in several shapes." + R_EN,
 "tr": "Onlardan biri AKSTİR: sözün bir cüz'ünün önce ÖNE, sonra SONA konulması; birkaç şekilde olur." + R_TR},
 "tokens": [
  minha(A),
  tok("الْعَكْسُ","aks","noun",[A, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ عَكَسَ: قَلَبَ.", "«the ʿaks» — masdar of عَكَسَ, to reverse.", "«aks» — عَكَسَ'nin masdarı: tersine çevirmek.", punct="،"),
  tok("وَهُوَ","huwa","pron",[A, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o».",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  an_masd(A),
  tok("يُقَدَّمَ","qaddama","verb",[A, "an-masdariyya", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«be put first».", "«öne alınsın»."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْكَلَامِ","kalam","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«the speech».", "«söz»."),
  tok("جُزْءٌ","juz","noun",[A, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a part».", "«bir cüz»."),
  tok("ثُمَّ","thumma","conj",[A, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("يُؤَخَّرَ","akhkhara","verb",[A, "atf-nasaq", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَعْطُوفٌ، مَبْنِيٌّ لِلْمَجْهُولِ.", "«be put last».", "«sona alınsın».", punct="،"),
  wa_conj("وَيَقَعُ","waqaa","verb",[A, "atf-nasaq", "fail", "mithal-verbs", "mudari-marfu"], "يَقَعُ فِعْلٌ مُضَارِعٌ مِثَالٌ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ.", "«and it falls» — the assimilated verb.", "«ve olur» — misâl fiil."),
  tok("عَلَى","ala","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  tok("وُجُوهٍ","wajh","noun",[A, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ وَجْهٍ.", "«several shapes».", "«birkaç şekil».", punct=".")]})

# ----------- s12 — mudaf shape (head RESTORED)
S.append({"id": "s12", "translation": {
 "en": "One: that it fall between one of a sentence's two ends and what is annexed to it — such as: «the HABITS of the MASTERS are the MASTERS of HABITS»." + R_EN,
 "tr": "Biri: cümlenin iki tarafından biriyle ona izâfe edilen arasında olması — «EFENDİLERİN ÂDETLERİ, ÂDETLERİN EFENDİLERİDİR» gibi." + R_TR},
 "badi": [{"kind": "aks", "first": [10, 11], "second": [12, 13], "sub": "mudaf"}],
 "tokens": [
  tok("مِنْهَا","min","part",[A, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — مِنَ الْوُجُوهِ.", "«one of them» — a fronted khabar.", "«onlardan biri» — öne alınmış haber.",
      segments=[seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  an_masd(A),
  tok("يَقَعَ","waqaa","verb",[A, "an-masdariyya", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، الْعَكْسُ.", "«it fall».", "«olsun»."),
  tok("بَيْنَ","bayna","noun",[A, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between».", "«arasında»."),
  tok("أَحَدِ","ahad","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«one of».", "«birinden»."),
  tok("طَرَفَيْ","taraf","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«the two ends of» — the dual, its nun dropped.", "«iki tarafı» — tesniye, nûnu düşmüş."),
  tok("جُمْلَةٍ","jumla","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a sentence».", "«bir cümlenin»."),
  wa_conj("وَمَا","ma-mawsula","pron",[A, "atf-nasaq", "ism-mawsul"], "مَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى أَحَدِ.", "«and what».", "«ve … şey»."),
  tok("أُضِيفَ","adafa","verb",[A, "ism-mawsul", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ؛ صِلَةٌ.", "«is annexed».", "«izâfe edilmiş»."),
  tok("إِلَيْهِ","ila","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to it».", "«ona».",
      segments=[seg("إِلَيْ","ila","part"), seg("هِ","pron-3ms","pron")], punct="،"),
  nahwa(tag=A),
  tok("عَادَاتُ","ada","noun",[A, "mubtada-khabar", "idafa-definiteness", "jam-muannath-salim"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — الْجُزْءُ الْمُقَدَّمُ.", "«the habits of» — the mubtada; the part put first.", "«âdetleri» — mübtedâ; öne alınan cüz."),
  tok("السَّادَاتِ","sayyid","noun",[A, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ سَادَةٍ، جَمْعِ سَيِّدٍ.", "«the masters» — plural of سَادَة, itself plural of سَيِّد.", "«efendilerin» — سَادَة'nin çoğulu, o da سَيِّد'in."),
  tok("سَادَاتُ","sayyid","noun",[A, "mubtada-khabar", "idafa-definiteness", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — الْمُضَافُ إِلَيْهِ صَارَ مُضَافًا: الْعَكْسُ.", "«the masters of» — the khabar; the mudaf ilayh now the mudaf: the ʿAKS.", "«efendileri» — haber; muzâfun ileyh muzâf olmuş: AKS."),
  tok("الْعَادَاتِ","ada","noun",[A, "idafa-definiteness", "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«habits».", "«âdetlerin».", punct=".")]})
S[-1]["badi"] = [{"kind": "aks", "first": [11, 12], "second": [13, 14], "sub": "mudaf"}]

# ----------- s13 — mutaʿalliq shape: 10:31
S.append({"id": "s13", "translation": {
 "en": "And: that it fall between the two dependents of two verbs in two sentences — such as: «He brings the LIVING out of the DEAD and brings the DEAD out of the LIVING» (10:31)." + R_EN,
 "tr": "Ve: iki cümledeki iki fiilin müteallikleri arasında olması — «ÖLÜDEN DİRİYİ çıkarır, DİRİDEN ÖLÜYÜ çıkarır» (Yûnus 10:31) gibi." + R_TR},
 "badi": [{"kind": "aks", "first": [9, 11], "second": [13, 15], "sub": "mutaalliq"}, bd("tibaq", [9, 11], sub="ijab", cls="ism")],
 "tokens": [
  wa_conj("وَمِنْهَا","min","part",[A, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "مِنْهَا خَبَرٌ مُقَدَّمٌ.", "«and one of them».", "«ve biri».", pron=("هَا","pron-3fs")),
  an_masd(A),
  tok("يَقَعَ","waqaa","verb",[A, "an-masdariyya", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ.", "«it fall».", "«olsun»."),
  tok("بَيْنَ","bayna","noun",[A, "maful-fih", "idafa-definiteness"], "ظَرْفٌ، مُضَافٌ.", "«between».", "«arasında»."),
  tok("مُتَعَلِّقَيْ","mutaalliq","noun",[A, "idafa-definiteness", "al-muthanna", "ism-fail", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ — اسْمُ فَاعِلِ تَعَلَّقَ: مَا يَتَعَلَّقُ بِالْفِعْلِ مِنْ مَفْعُولٍ وَجَارٍّ.", "«the two dependents of» — what hangs on the verb: object, preposition-phrase.", "«iki müteallikı» — fiile bağlı olan: mef'ûl, câr-mecrûr."),
  tok("فِعْلَيْنِ","fil","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two verbs».", "«iki fiilin»."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("جُمْلَتَيْنِ","jumla","noun",[A, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ.", "«two sentences».", "«iki cümle».", punct="،"),
  nahwa(tag=A),
  tok("يُخْرِجُ","akhraja","verb",[A, "fail", "maful-bihi", "form-iv-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، اللهُ.", "«He brings out».", "«çıkarır»."),
  tok("الْحَيَّ","hayy","noun",[A, "maful-bihi", "sifa-mushabbaha"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُتَعَلِّقُ الْأَوَّلُ.", "«the living» — the first dependent.", "«diriyi» — birinci müteallik."),
  tok("مِنَ","min","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«out of».", "«-den»."),
  tok("الْمَيِّتِ","mayyit","noun",[A, "huruf-jarr"], "مَجْرُورٌ — الْمُتَعَلِّقُ الثَّانِي؛ طِبَاقٌ مَعَ الْحَيِّ.", "«the dead» — the second dependent; a tibaq with «the living».", "«ölüden» — ikinci müteallik; «diri» ile tıbâk."),
  wa_conj("وَيُخْرِجُ","akhraja","verb",[A, "atf-nasaq", "fail", "maful-bihi", "form-iv-verbs", "mudari-marfu"], "يُخْرِجُ مَعْطُوفٌ.", "«and brings out».", "«ve çıkarır»."),
  tok("الْمَيِّتَ","mayyit","noun",[A, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَا كَانَ مَجْرُورًا صَارَ مَفْعُولًا: الْعَكْسُ.", "«the dead» — what was majrur is now the object: the ʿAKS.", "«ölüyü» — mecrur olan mef'ûl olmuş: AKS."),
  tok("مِنَ","min","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«out of».", "«-den»."),
  tok("الْحَيِّ","hayy","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«the living».", "«diriden».", punct=".")]})
S[-1]["badi"] = [{"kind": "aks", "first": [10, 12], "second": [14, 16], "sub": "mutaalliq"}, bd("tibaq", [10, 12], sub="ijab", cls="ism")]

# ----------- s14 — tarafayn shape: 60:10
S.append({"id": "s14", "translation": {
 "en": "And: that it fall between two words at the two ends of two sentences — such as: «THEY (the women) are not lawful for THEM, nor are THEY (the men) lawful for THEM» (60:10)." + R_EN,
 "tr": "Ve: iki cümlenin iki tarafındaki iki lafız arasında olması — «ONLAR (kadınlar) ONLARA (erkeklere) helâl değildir, ONLAR (erkekler) de ONLARA (kadınlara) helâl olmazlar» (Mümtehine 60:10) gibi." + R_TR},
 "badi": [{"kind": "aks", "first": [9, 11], "second": [13, 15], "sub": "tarafayn"}],
 "tokens": [
  wa_conj("وَمِنْهَا","min","part",[A, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "مِنْهَا خَبَرٌ مُقَدَّمٌ.", "«and one of them».", "«ve biri».", pron=("هَا","pron-3fs")),
  an_masd(A),
  tok("يَقَعَ","waqaa","verb",[A, "an-masdariyya", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ.", "«it fall».", "«olsun»."),
  tok("بَيْنَ","bayna","noun",[A, "maful-fih", "idafa-definiteness"], "ظَرْفٌ، مُضَافٌ.", "«between».", "«arasında»."),
  tok("لَفْظَيْنِ","lafz","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two words».", "«iki lafız»."),
  tok("فِي","fi","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  tok("طَرَفَيْ","taraf","noun",[A, "huruf-jarr", "idafa-definiteness", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«the two ends of».", "«iki tarafında»."),
  tok("جُمْلَتَيْنِ","jumla","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two sentences».", "«iki cümlenin».", punct="،"),
  nahwa(tag=A),
  tok("لَا","la-nafiya","part",[A, "ma-la-mushabbaha"], "لَا نَافِيَةٌ.", "«not».", "«değil»."),
  tok("هُنَّ","hunna","pron",[A, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — الْمُؤْمِنَاتُ؛ الطَّرَفُ الْأَوَّلُ لِلْجُمْلَةِ الْأُولَى.", "«they» (the women) — the mubtada; the first end of the first sentence.", "«onlar» (kadınlar) — mübtedâ; birinci cümlenin ilk tarafı."),
  tok("حِلٌّ","hill","noun",[A, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرٌ بِمَعْنَى حَلَالٍ.", "«lawful» — the khabar; a masdar meaning «permitted».", "«helâl» — haber; «helâl» mânâsında masdar."),
  tok("لَهُمْ","lahu","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْكُفَّارُ؛ الطَّرَفُ الْآخَرُ.", "«for them» (the men) — the other end.", "«onlara» (erkeklere) — öbür taraf.",
      segments=[seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  wa_conj("وَلَا","la-nafiya","part",[A, "atf-nasaq"], "لَا نَافِيَةٌ.", "«nor».", "«ve … de değil»."),
  tok("هُمْ","hum","pron",[A, "mubtada-khabar"], "مُبْتَدَأٌ — مَا كَانَ مَجْرُورًا فِي الْأُولَى صَارَ مُبْتَدَأً: الْعَكْسُ.", "«they» (the men) — what was majrur is now the mubtada: the ʿAKS.", "«onlar» (erkekler) — birincide mecrur olan mübtedâ olmuş: AKS."),
  tok("يَحِلُّونَ","halla-lawful","verb",[A, "mubtada-khabar", "fail", "doubled-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مُضَاعَفٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ؛ خَبَرٌ.", "«are lawful» — the doubled verb; the khabar.", "«helâl olurlar» — muzâaf fiil; haber.",
      segments=[seg("يَحِلُّ","halla-lawful","verb"), seg("ونَ","pron-3mp","pron")]),
  tok("لَهُنَّ","lahu","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُؤْمِنَاتُ فِي الطَّرَفِ الْآخَرِ.", "«for them» (the women) — at the other end.", "«onlara» (kadınlara) — öbür tarafta.",
      segments=[seg("لَ","li","part"), seg("هُنَّ","pron-3fp","pron")], punct=".")]})
S[-1]["badi"] = [{"kind": "aks", "first": [10, 12], "second": [14, 16], "sub": "tarafayn"}]

# ---------------------------------------------------------------- glossary
def FG(*ks): return {k: find_gloss(k) for k in ks}
GLOSS_ADD = FG("min", "hiya", "an", "samma", "baad", "jaala", "aw", "bayt", "ma-mawsula", "dalla", "ala", "idha", "arafa", "nahwa", "ma-nafiya", "kana", "allah",
               "zalama", "lakin", "nafs", "qawl", "amr-ibn-madikarib", "ibn", "madikarib", "lam", "istataa", "amr", "ila", "dhikr", "shay", "lafz", "ghayr", "fi",
               "suhba", "tahqiq", "taqdir", "mithal", "qala", "lahu", "tabkh", "alima", "ay", "anna", "iman", "asl", "walad", "ma-water", "huwa", "bayna", "mana",
               "shart", "kull", "wahid", "buhturi", "ma-zaida", "bi", "kalam", "juz", "thumma", "waqaa", "wajh", "ahad", "taraf", "jumla", "ada", "fil",
               "akhraja", "hayy", "mayyit", "hum", "hill", "aks", "qaddama", "akhkhara", "taala", "la-nafiya",
               "wa", "fa", "li", "ta-tanith", "pron-3ms", "pron-3fs", "pron-3mp", "pron-3d", "pron-1s", "pron-2ms", "pron-2mp", "pron-3fp")
GLOSS_ADD.update({
 "irsad": G("irsad", "إِرْصَاد", "ر ص د", "noun", "irsad — setting before the close what points to it (masdar of أَرْصَدَ, to lie in wait)", "irsâd — sondan önce ona delâlet edeni koymak (أَرْصَدَ'nin masdarı: gözetlemek)", 6),
 "tashim": G("tashim", "تَسْهِيم", "س ه م", "noun", "tashim — the irsad's other name: drawing a straight line, like an arrow (masdar of سَهَّمَ)", "teshîm — irsâdın öbür adı: ok gibi düz çizgi çekmek (سَهَّمَ'nin masdarı)", 6),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before (a zarf of time or place)", "… -den önce (zaman yahut mekân zarfı)", 1),
 "ajuz": G("ajuz", "عَجُز", "ع ج ز", "noun", "the close — the last word of a verse or clause; the second half of a verse", "acüz — beytin yahut fıkranın son kelimesi; beytin ikinci yarısı", 5, plural="أَعْجَاز"),
 "fiqra": G("fiqra", "فِقْرَة", "ف ق ر", "noun", "a prose-clause, one member of rhymed prose", "fıkra, secili nesrin bir cümlesi", 5, plural="فِقَر"),
 "rawiyy": G("rawiyy", "رَوِيّ", "ر و ي", "noun", "the rhyme-letter — the letter the rhyme is built on", "revî — kafiyenin üzerine kurulduğu harf", 5),
 "da-leave": G("da-leave", "دَعْ", "و د ع", "verb", "leave! (the imperative of وَدَعَ, whose past is not used)", "bırak! (وَدَعَ'nin emri, mâzîsi kullanılmaz)", 3, form="I"),
 "jawaza3": G("jawaza3", "جَاوَزَ", "ج و ز", "verb", "to pass beyond, to go past (Form III)", "geçmek, aşmak (III. bâb)", 4, form="III"),
 "mushakala": G("mushakala", "مُشَاكَلَة", "ش ك ل", "noun", "mushakala — saying a thing with another's word for its company (masdar of شَاكَلَ)", "müşâkele — bir şeyi, sohbeti yüzünden başkasının lafzıyla söylemek (شَاكَلَ'nin masdarı)", 6),
 "wuqu": G("wuqu", "وُقُوع", "و ق ع", "noun", "falling, occurring (masdar of وَقَعَ)", "vuku, düşme (وَقَعَ'nin masdarı)", 4),
 "iqtaraha": G("iqtaraha", "اِقْتَرَحَ", "ق ر ح", "verb", "to propose, to ask for something of one's choosing (Form VIII)", "teklif etmek, seçip istemek (VIII. bâb)", 5, form="VIII"),
 "ajada": G("ajada", "أَجَادَ", "ج و د", "verb", "to do a thing well (Form IV, hollow)", "güzelce yapmak (IV. bâb, ecvef)", 4, form="IV"),
 "tabakha": G("tabakha", "طَبَخَ", "ط ب خ", "verb", "to cook (طَبَخَ يَطْبُخُ)", "pişirmek (طَبَخَ يَطْبُخُ)", 2, form="I"),
 "jubba": G("jubba", "جُبَّة", "ج ب ب", "noun", "a cloak, a long outer garment", "cübbe", 3, plural="جِبَاب"),
 "qamis": G("qamis", "قَمِيص", "ق م ص", "noun", "a shirt", "gömlek", 2, plural="قُمْصَان"),
 "sibgha": G("sibgha", "صِبْغَة", "ص ب غ", "noun", "a dye, a colouring; صِبْغَةَ اللهِ — God's dye: the faith that purifies", "boya; صِبْغَةَ اللهِ — Allah'ın boyası: temizleyen iman", 4),
 "tathir-purify": G("tathir-purify", "تَطْهِير", "ط ه ر", "noun", "purifying, cleansing (masdar of طَهَّرَ)", "temizleme (طَهَّرَ'nin masdarı)", 4),
 "tahhara": G("tahhara", "طَهَّرَ", "ط ه ر", "verb", "to purify, to cleanse (Form II)", "temizlemek (II. bâb)", 3, form="II"),
 "nasara-christians": G("nasara-christians", "النَّصَارَى", "ن ص ر", "noun", "the Christians (plural of نَصْرَانِيّ)", "Hristiyanlar (نَصْرَانِيّ'in çoğulu)", 3),
 "ghamasa": G("ghamasa", "غَمَسَ", "غ م س", "verb", "to dip, to plunge into (غَمَسَ يَغْمِسُ)", "batırmak, daldırmak (غَمَسَ يَغْمِسُ)", 4, form="I"),
 "asfar": G("asfar", "أَصْفَر", "ص ف ر", "noun", "yellow (the colour أَفْعَل; feminine صَفْرَاء)", "sarı (renk için أَفْعَل; müennesi صَفْرَاء)", 2, plural="صُفْر"),
 "mamudiyya": G("mamudiyya", "مَعْمُودِيَّة", None, "noun", "the baptism (the Christians' rite of dipping)", "vaftiz (Hristiyanların suya daldırma âyini)", 6),
 "muzawaja": G("muzawaja", "مُزَاوَجَة", "ز و ج", "noun", "muzawaja — pairing two meanings in the shart and the jaza (masdar of زَاوَجَ)", "müzâvece — şart ile cezâda iki mânâyı çiftlemek (زَاوَجَ'nin masdarı)", 6),
 "zawaja": G("zawaja", "زَاوَجَ", "ز و ج", "verb", "to pair, to couple (Form III)", "çiftlemek, eşlemek (III. bâb)", 4, form="III"),
 "jaza-answer": G("jaza-answer", "جَزَاء", "ج ز ي", "noun", "the answer of a condition, the jawab; requital", "cezâ — şartın cevabı; karşılık", 3),
 "rattaba": G("rattaba", "رَتَّبَ", "ر ت ب", "verb", "to arrange, to make follow in order (Form II)", "tertip etmek, sıralamak (II. bâb)", 3, form="II"),
 "naha": G("naha", "نَهَى", "ن ه ي", "verb", "to forbid, to reproach (naqis: نَهَى يَنْهَى)", "yasaklamak, kınamak (nâkıs: نَهَى يَنْهَى)", 3, form="I"),
 "nahi": G("nahi", "نَاهٍ (النَّاهِي)", "ن ه ي", "noun", "the forbidder, the reproacher (ism fa'il of نَهَى, a manqus)", "yasaklayan, kınayan (نَهَى'nın ism-i fâili, menkûs)", 4),
 "lajja": G("lajja", "لَجَّ", "ل ج ج", "verb", "to persist, to be obstinate (doubled: لَجَّ يَلَجُّ)", "diretmek, inat etmek (muzâaf: لَجَّ يَلَجُّ)", 4, form="I"),
 "hawa-love": G("hawa-love", "هَوًى (الْهَوَى)", "ه و ي", "noun", "passion, desire, love (a maqsur noun)", "hevâ, sevgi, arzu (maksûr isim)", 3, plural="أَهْوَاء"),
 "asakha": G("asakha", "أَصَاخَ", "ص و خ", "verb", "to listen, to lend an ear (Form IV, hollow; إِلَى: to)", "kulak vermek (IV. bâb, ecvef; إِلَى: -e)", 5, form="IV"),
 "washi": G("washi", "وَاشٍ (الْوَاشِي)", "و ش ي", "noun", "the slanderer, the tale-bearer (ism fa'il of وَشَى, a manqus)", "iftiracı, gammaz (وَشَى'nın ism-i fâili, menkûs)", 5, plural="وُشَاة"),
 "hajr": G("hajr", "هَجْر", "ه ج ر", "noun", "estrangement, abandoning (masdar of هَجَرَ)", "terk, hicran (هَجَرَ'nin masdarı)", 4),
 "adafa": G("adafa", "أَضَافَ", "ض ي ف", "verb", "to annex, to put in idafa (Form IV, hollow)", "izâfe etmek (IV. bâb, ecvef)", 4, form="IV"),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 2, plural="سَادَة، سَادَات"),
 "mutaalliq": G("mutaalliq", "مُتَعَلِّق", "ع ل ق", "noun", "a dependent — what hangs on a verb: its object, its preposition-phrase (ism fa'il of تَعَلَّقَ)", "müteallik — fiile bağlı olan: mef'ûlü, câr-mecrûru (تَعَلَّقَ'nin ism-i fâili)", 5),
 "hunna": G("hunna", "هُنَّ", None, "pron", "they (feminine plural)", "onlar (müennes çoğul)", 1),
 "halla-lawful": G("halla-lawful", "حَلَّ", "ح ل ل", "verb", "to be lawful (doubled: حَلَّ يَحِلُّ); to untie; to alight", "helâl olmak (muzâaf: حَلَّ يَحِلُّ); çözmek; konmak", 3, form="I"),
})

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "jawaza3", _sg.derived_hollow(_sg.B3, _sg.W3, "ُ", "جَاوَز", "جَاوَز", "جَاوِز", "جَاوِز", "جَاوِز", "جَاوِز", "مُجَاوَزَة", "مُجَاوِز", "مُجَاوَز", "جُووِزَ", "يُجَاوَزُ"))
put_morph(mo, "iqtaraha", _sg.derived(_sg.B8, _sg.W8, "َ", "اِقْتَرَح", "قْتَرِح", "اِقْتَرِح", "اِقْتِرَاح", "مُقْتَرِح", "مُقْتَرَح", "اُقْتُرِحَ", "يُقْتَرَحُ"))
put_morph(mo, "ajada", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَجَاد", "أَجَد", "جِيد", "جِد", "أَجِيد", "أَجِد", "إِجَادَة", "مُجِيد", "مُجَاد", "أُجِيدَ", "يُجَادُ"))
put_morph(mo, "tabakha", _sg.sound1("nasara", "طَبَخ", "طْبُخ", "اُطْبُخ", "طَبْخ", "طَابِخ", "مَطْبُوخ", "طُبِخَ", "يُطْبَخُ"))
put_morph(mo, "tahhara", _sg.derived(_sg.B2, _sg.W2, "ُ", "طَهَّر", "طَهِّر", "طَهِّر", "تَطْهِير", "مُطَهِّر", "مُطَهَّر", "طُهِّرَ", "يُطَهَّرُ"))
put_morph(mo, "ghamasa", _sg.sound1("daraba", "غَمَس", "غْمِس", "اِغْمِس", "غَمْس", "غَامِس", "مَغْمُوس", "غُمِسَ", "يُغْمَسُ"))
put_morph(mo, "zawaja", _sg.derived(_sg.B3, _sg.W3, "ُ", "زَاوَج", "زَاوِج", "زَاوِج", "مُزَاوَجَة", "مُزَاوِج", "مُزَاوَج", "زُووِجَ", "يُزَاوَجُ"))
put_morph(mo, "rattaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "رَتَّب", "رَتِّب", "رَتِّب", "تَرْتِيب", "مُرَتِّب", "مُرَتَّب", "رُتِّبَ", "يُرَتَّبُ"))
put_morph(mo, "naha", _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ", "y", "نَهَ", "نْه", "a", "انْه", "نَهْي", "نَاهٍ (النَّاهِي)", "مَنْهِيّ", "نُهِيَ", "يُنْهَى",
                                  note="نَاقِصٌ مِنْ بَابِ فَتَحَ: نَهَى يَنْهَى — نَهَوْا، نَهَتْ."))
put_morph(mo, "lajja", _sg.entry(_sg.BABS["samia"][0] + " — مُضَاعَفٌ", _sg.BABS["samia"][1], "لَجَاج", "لَاجّ", _sg.mazi14("لَجّ", "لَجِج"), _sg.mudari14("َ", "لَجّ", "لْجَج"),
                                 ["لَجَّ", "لَجَّا", "لَجُّوا", "لَجِّي", "لَجَّا", "اِلْجَجْنَ"], "يَلَجَّ", "يَلَجَّ", "تَلَجَّ", "مَلْجُوج", "لُجَّ", "يُلَجُّ",
                                 note="مُضَاعَفٌ مِنْ بَابِ سَمِعَ: لَجَّ يَلَجُّ — لَجِجْتُ، يَلْجَجْنَ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ."))
put_morph(mo, "asakha", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَصَاخ", "أَصَخ", "صِيخ", "صِخ", "أَصِيخ", "أَصِخ", "إِصَاخَة", "مُصِيخ", "مُصَاخ", "أُصِيخَ", "يُصَاخُ"))
put_morph(mo, "adafa", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَضَاف", "أَضَف", "ضِيف", "ضِف", "أَضِيف", "أَضِف", "إِضَافَة", "مُضِيف", "مُضَاف", "أُضِيفَ", "يُضَافُ"))
# وَدَعَ يَدَعُ دَعْ — the mithal of bab fataha on the وَضَعَ model (the manar ch4 precedent): the waw falls in the
# mudari and returns in the passive; the books say its mazi and masdar are little used (أُمِيتَ), and the note says so.
put_morph(mo, "da-leave", _sg.sound1("fataha", "وَدَع", "دَع", "دَع", "وَدْع", "وَادِع", maful="مَوْدُوع", pmz="وُدِعَ", pmd="يُودَعُ",
                                   cls="مِثَالٌ وَاوِيٌّ",
                                   note="سَقَطَتِ الْوَاوُ فِي الْمُضَارِعِ وَالْأَمْرِ: يَدَعُ، دَعْ؛ وَالْمَاضِي وَالْمَصْدَرُ قَلِيلَا الِاسْتِعْمَالِ، يُسْتَغْنَى عَنْهُمَا بِتَرَكَ وَتَرْكٍ."))
put_morph(mo, "halla-lawful", _sg.entry(_sg.BABS["daraba"][0] + " — مُضَاعَفٌ", _sg.BABS["daraba"][1], "حِلّ", "حَالّ", _sg.mazi14("حَلّ", "حَلَل"), _sg.mudari14("َ", "حِلّ", "حْلِل"),
                                        ["حِلَّ", "حِلَّا", "حِلُّوا", "حِلِّي", "حِلَّا", "اِحْلِلْنَ"], "يَحِلَّ", "يَحِلَّ", "تَحِلَّ", "مَحْلُول", "حُلَّ", "يُحَلُّ",
                                        note="مُضَاعَفٌ مِنْ بَابِ ضَرَبَ: حَلَّ يَحِلُّ — حَلَلْتُ، يَحْلِلْنَ."))
for k in ("samma", "jaala", "dalla", "arafa", "zalama", "kana", "istataa", "qala", "alima", "waqaa", "qaddama", "akhkhara", "akhraja"):
    if k not in mo["verbs"] and has_morph(k): mo["verbs"][k] = find_morph(k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_I = {
 "id": "irsad",
 "title": {"ar": "الْإِرْصَادُ (التَّسْهِيمُ) — مَا قَبْلَ الْعَجُزِ يَدُلُّ عَلَيْهِ", "en": "The irsad (tashim) — what comes before the close forecasts it", "tr": "İrsâd (teshîm) — sondan öncesi, sonu haber verir"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الإرصاد: أن يجعل قبل العجز من الفقرة أو البيت ما يدل عليه إذا عرف الروي"],
 "question": {
  "en": ["Once the rhyme-letter is known, does something BEFORE the close already TELL YOU the close? فَمَا كَانَ اللهُ لِيَظْلِمَهُمْ … — the ear waits for يَظْلِمُونَ. That is the IRSAD, which some call the TASHIM.",
         "What forecasts? Usually the SAME ROOT earlier in the line: لِيَظْلِمَهُمْ → يَظْلِمُونَ, لَمْ تَسْتَطِعْ → تَسْتَطِيعُ. The second is the close; the first lies in wait for it.",
         "Is it a rhyme figure or a meaning figure? Both — the Talkhis lists it among the figures of MEANING: the sense leads the hearer to the word before the word arrives."],
  "tr": ["Revî harfi bilinince, sondan ÖNCE bir şey sonu zaten SÖYLÜYOR mu? فَمَا كَانَ اللهُ لِيَظْلِمَهُمْ … — kulak يَظْلِمُونَ'yi bekler. Bazılarının TESHÎM dediği İRSÂD budur.",
         "Ne haber verir? Çoğu kere mısradaki AYNI KÖK: لِيَظْلِمَهُمْ → يَظْلِمُونَ, لَمْ تَسْتَطِعْ → تَسْتَطِيعُ. İkincisi sondur; birincisi onu gözetler.",
         "Kafiye sanatı mı mânâ sanatı mı? İkisi de — Telhîs onu MÂNEVÎ sanatlar arasında sayar: mânâ, kelime gelmeden dinleyeni kelimeye götürür."]},
 "plain": {
  "en": "The irsad, also called the tashim: before the close of a clause or verse comes something that points to the close, once the rhyme-letter is known — «God would not WRONG them … they were WRONGING themselves». The engine finds the forecaster by root: the same root at the close and earlier in the line.",
  "tr": "İrsâd, teshîm de denir: revî harfi bilinince, fıkranın yahut beytin sonundan önce sonu haber veren bir şey gelir — «Allah onlara ZULMEDECEK değildi … kendilerine ZULMEDİYORLARDI». Motor haber vereni kökle bulur: sonda ve mısranın önünde aynı kök."},
 "explanation": {
  "en": "The IRSAD (from أَرْصَدَ, to set in wait), which some call the TASHIM (from سَهَّمَ, to draw straight as an arrow), is أَنْ يُجْعَلَ قَبْلَ الْعَجُزِ مِنَ الْفِقْرَةِ أَوِ الْبَيْتِ مَا يَدُلُّ عَلَيْهِ إِذَا عُرِفَ الرَّوِيُّ — that before the CLOSE (the ʿajuz: the last word) of a prose-clause or a verse there be set what POINTS TO IT, once the rhyme-letter (the rawiyy) is known. 9:70: فَمَا كَانَ اللهُ لِيَظْلِمَهُمْ وَلَكِنْ كَانُوا أَنْفُسَهُمْ يَظْلِمُونَ — لِيَظْلِمَهُمْ points to يَظْلِمُونَ: whoever knows the rhyme-letter of the passage knows the close before it comes. ʿAmr b. Maʿdi Karib: إِذَا لَمْ تَسْتَطِعْ أَمْرًا فَدَعْهُ * وَجَاوِزْهُ إِلَى مَا تَسْتَطِيعُ — لَمْ تَسْتَطِعْ points to تَسْتَطِيعُ. In both the forecaster and the close share a ROOT, and in both the close also makes a tibaq of negation with its forecaster. WHAT THE ENGINE CLAIMS: the BadiEngine reads the irsad by ROOT: the last content word of the sentence (the close) and an earlier word of the same root, at least two words apart, form the pair; it reports the forecaster and the close and draws the arc. It cannot know the rhyme-letter of a passage it sees one sentence of, so a root-repeat that is mere repetition is refused unless the close is the sentence's final word. It grades itself against the authored `irsad` frames of ch59.",
  "tr": "İRSÂD (أَرْصَدَ'den: gözetlemeye koymak), bazılarının TESHÎM (سَهَّمَ'den: ok gibi düz çizmek) dediği, أَنْ يُجْعَلَ قَبْلَ الْعَجُزِ مِنَ الْفِقْرَةِ أَوِ الْبَيْتِ مَا يَدُلُّ عَلَيْهِ إِذَا عُرِفَ الرَّوِيُّ'dir — revî (kafiye harfi) bilinince, fıkranın yahut beytin SONUNDAN (acüz: son kelime) önce ona DELÂLET EDEN bir şeyin konulması. Tevbe 9:70: فَمَا كَانَ اللهُ لِيَظْلِمَهُمْ وَلَكِنْ كَانُوا أَنْفُسَهُمْ يَظْلِمُونَ — لِيَظْلِمَهُمْ, يَظْلِمُونَ'yi haber verir: pasajın revîsini bilen, sonu gelmeden bilir. Amr b. Ma'dîkerib: إِذَا لَمْ تَسْتَطِعْ أَمْرًا فَدَعْهُ * وَجَاوِزْهُ إِلَى مَا تَسْتَطِيعُ — لَمْ تَسْتَطِعْ, تَسْتَطِيعُ'yu haber verir. İkisinde de haber veren ile son aynı KÖKÜ paylaşır ve ikisinde de son, haber vereniyle bir selb tıbâkı kurar. MOTORUN İDDİASI: BadiEngine irsâdı KÖKLE okur: cümlenin son anlamlı kelimesi (acüz) ile aynı kökten, en az iki kelime önce gelen bir kelime çifti kurar; haber vereni ve sonu bildirir, yayı çizer. Tek cümlesini gördüğü pasajın revîsini bilemez; bu yüzden salt tekrar olan kök tekrarı, son cümlenin son kelimesi değilse reddedilir. Kendini 59. bâbın müellif `irsad` çerçevelerine karşı sınar."},
 "examples": [
  {"ar": "فَمَا كَانَ اللهُ لِيَظْلِمَهُمْ وَلَكِنْ كَانُوا أَنْفُسَهُمْ يَظْلِمُونَ", "en": "the forecaster and the close (9:70).", "tr": "haber veren ve son (Tevbe 9:70).", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "إِذَا لَمْ تَسْتَطِعْ أَمْرًا فَدَعْهُ * وَجَاوِزْهُ إِلَى مَا تَسْتَطِيعُ", "en": "ʿAmr b. Maʿdi Karib.", "tr": "Amr b. Ma'dîkerib.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"}],
 "commonMistakes": [
  {"wrong": "«İrsâd yalnız kafiye tekrarıdır»",
   "right": "«Mânâ sanatıdır: önceki söz, son kelimeyi mânâca zorunlu kılar — kafiye yalnız onu doğrular»",
   "why": {"en": "The definition says «what POINTS TO the close», and asks only that the rhyme-letter be known; the pointing is by sense.", "tr": "Tarif «sona DELÂLET EDEN» der ve yalnız revînin bilinmesini ister; delâlet mânâ iledir."}},
  {"wrong": "«Aynı kökün her tekrarı irsâddır»",
   "right": "«Tekrarın ikinci ucu fıkranın yahut beytin SONU olmalıdır»",
   "why": {"en": "The figure lives at the close; a root repeated mid-line is a jinas al-ishtiqaq or plain repetition.", "tr": "Sanat sonda yaşar; mısra ortasında tekrarlanan kök cinâs-ı iştikâk yahut düz tekrardır."}}],
 "relatedNotes": ["tibaq", "saj", "jinas", "ilm-al-badi", "mushakala"]}

NOTE_K = {
 "id": "mushakala",
 "title": {"ar": "الْمُشَاكَلَةُ — ذِكْرُ الشَّيْءِ بِلَفْظِ غَيْرِهِ لِوُقُوعِهِ فِي صُحْبَتِهِ", "en": "The mushakala — saying a thing with another's word, for its company", "tr": "Müşâkele — bir şeyi, sohbeti yüzünden başkasının lafzıyla söylemek"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — المشاكلة: ذكر الشيء بلفظ غيره لوقوعه في صحبته تحقيقاً أو تقديراً"],
 "question": {
  "en": ["Is a thing named by a WORD THAT BELONGS TO ITS NEIGHBOUR? «Ask for something and we shall COOK it for you. — COOK me a cloak and a shirt.» Sewing is meant; «cook» is said because it fell in the company of cooking. That is the MUSHAKALA.",
         "Is the company SPOKEN (tahqiq) or only UNDERSTOOD (taqdir)? نَفْسِي … نَفْسِكَ (5:116): «my soul» was said, so «Your soul» follows — spoken. صِبْغَةَ اللهِ (2:138): God's «dye» for purifying — the Christians' dipping is the company, never spoken.",
         "Is it a majaz? A near cousin: the word leaves its sense, and the clue is the neighbour. The Talkhis keeps it among the figures of the badiʿ for its beauty, not among the majaz for its mechanism."],
  "tr": ["Bir şey, KOMŞUSUNA AİT BİR KELİMEYLE mi adlandırılmış? «Bir şey iste, sana PİŞİRELİM. — Bana bir cübbe ile gömlek PİŞİRİN.» Dikme kastedilmiş; «pişirin», pişirme sohbetinde düştüğü için söylenmiş. MÜŞÂKELE budur.",
         "Sohbet SÖYLENMİŞ mi (tahkîk) yalnız ANLAŞILMIŞ mı (takdîr)? نَفْسِي … نَفْسِكَ (Mâide 5:116): «nefsim» dendi, «nefsin» onu izledi — söylenmiş. صِبْغَةَ اللهِ (Bakara 2:138): temizleme için Allah'ın «boyası» — Hristiyanların daldırması sohbettir, hiç söylenmemiş.",
         "Mecaz mı? Yakın akraba: kelime mânâsından çıkar, karîne komşudur. Telhîs onu mekanizması için mecazlar arasında değil, güzelliği için bedî' sanatları arasında tutar."]},
 "plain": {
  "en": "Saying a thing with the word of its neighbour because the two fell together — «cook me a cloak» after «we shall cook for you»; «Your soul» after «my soul»; God's «dye» for the faith that purifies. The company is spoken (tahqiq) or understood (taqdir). The engine reads the spoken kind by the repeated root.",
  "tr": "Bir şeyi, ikisi bir arada düştüğü için komşusunun kelimesiyle söylemek — «sana pişirelim»den sonra «bana cübbe pişirin»; «nefsim»den sonra «nefsin»; temizleyen iman için Allah'ın «boyası». Sohbet söylenmiş (tahkîk) yahut anlaşılmıştır (takdîr). Motor söylenmiş kısmı tekrarlanan kökle okur."},
 "explanation": {
  "en": "The MUSHAKALA (from شَاكَلَ, to match in shape) is ذِكْرُ الشَّيْءِ بِلَفْظِ غَيْرِهِ لِوُقُوعِهِ فِي صُحْبَتِهِ تَحْقِيقًا أَوْ تَقْدِيرًا — the mention of a thing by the WORD OF ANOTHER, because it fell in that other's COMPANY, in fact or in estimation. IN FACT (tahqiqan): Abu l-Rafʿ — قَالُوا اقْتَرِحْ شَيْئًا نُجِدْ لَكَ طَبْخَهُ * قُلْتُ اطْبُخُوا لِي جُبَّةً وَقَمِيصًا: «sew» (خِيطُوا) is meant, and «cook» is said because it fell in the company of «cooking»; and 5:116, تَعْلَمُ مَا فِي نَفْسِي وَلَا أَعْلَمُ مَا فِي نَفْسِكَ — «Your soul» is said only because «my soul» came before; «what is with You» is meant. IN ESTIMATION (taqdiran): 2:138, صِبْغَةَ اللهِ — «God's dye», a masdar confirming «we believe in God», means God's PURIFYING, for faith purifies souls; it was named a dye because the Christians dipped their children in a yellow water they called the baptism and said it purified them — a company estimated, never spoken in the aya. WHAT THE ENGINE CLAIMS: the BadiEngine reads the mushakala of FACT when a word's ROOT has already appeared in the sentence in another role (طَبْخَهُ → اطْبُخُوا, نَفْسِي → نَفْسِكَ) and the authored frame names the word that would otherwise have been said (the «asl»); it lights the word and its companion and reports the asl. The mushakala of ESTIMATION has no companion on the surface, so the engine takes it entirely from the frame and says so. It grades itself against the authored `mushakala` frames of ch59.",
  "tr": "MÜŞÂKELE (شَاكَلَ'den: şekilce benzemek) ذِكْرُ الشَّيْءِ بِلَفْظِ غَيْرِهِ لِوُقُوعِهِ فِي صُحْبَتِهِ تَحْقِيقًا أَوْ تَقْدِيرًا'dır — bir şeyi, o başkasının SOHBETİNDE düştüğü için — tahkîkan yahut takdîren — BAŞKASININ LAFZIYLA anmak. TAHKÎKAN: Ebü'r-Ref' — قَالُوا اقْتَرِحْ شَيْئًا نُجِدْ لَكَ طَبْخَهُ * قُلْتُ اطْبُخُوا لِي جُبَّةً وَقَمِيصًا: «dikin» (خِيطُوا) kastedilmiş, «pişirin» «pişirme» sohbetinde düştüğü için söylenmiş; ve Mâide 5:116, تَعْلَمُ مَا فِي نَفْسِي وَلَا أَعْلَمُ مَا فِي نَفْسِكَ — «nefsin» yalnız «nefsim» önce geçtiği için söylenmiş; «Senin katındaki» kastedilmiş. TAKDÎREN: Bakara 2:138, صِبْغَةَ اللهِ — «Allah'ın boyası», «Allah'a inandık»ı tekit eden masdar, Allah'ın TEMİZLEMESİ demektir, çünkü iman nefisleri temizler; boya diye anılması, Hristiyanların çocuklarını vaftiz dedikleri sarı suya daldırıp «temizlik» demelerindendir — takdir edilen, âyette hiç söylenmeyen bir sohbet. MOTORUN İDDİASI: BadiEngine TAHKÎK müşâkelesini, bir kelimenin KÖKÜ cümlede başka bir rolde zaten geçmişse (طَبْخَهُ → اطْبُخُوا, نَفْسِي → نَفْسِكَ) ve müellif çerçevesi aslında söylenecek kelimeyi («asl») veriyorsa okur; kelimeyi ve refikini aydınlatır, aslı bildirir. TAKDÎR müşâkelesinin yüzeyde refiki yoktur; motor onu tamamen çerçeveden alır ve bunu söyler. Kendini 59. bâbın müellif `mushakala` çerçevelerine karşı sınar."},
 "examples": [
  {"ar": "قَالُوا اقْتَرِحْ شَيْئًا نُجِدْ لَكَ طَبْخَهُ * قُلْتُ اطْبُخُوا لِي جُبَّةً وَقَمِيصًا", "en": "in fact: «cook» for «sew».", "tr": "tahkîkan: «dikin» yerine «pişirin».", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "تَعْلَمُ مَا فِي نَفْسِي وَلَا أَعْلَمُ مَا فِي نَفْسِكَ", "en": "in fact (5:116).", "tr": "tahkîkan (Mâide 5:116).", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "صِبْغَةَ اللهِ", "en": "in estimation (2:138).", "tr": "takdîren (Bakara 2:138).", "sourceStory": "talkhis-al-miftah", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«نَفْسِكَ Allah'a nefis isnat eder»",
   "right": "«Müşâkeledir: «nefsim» dendiği için «nefsin» denmiş; kastedilen Allah'ın katındaki, gaybıdır»",
   "why": {"en": "The word is borrowed from its neighbour for the shape of the sentence, not for its sense. That is the whole figure.", "tr": "Kelime mânâsı için değil, cümlenin şekli için komşusundan ödünç alınmıştır. Sanatın bütünü budur."}},
  {"wrong": "«صِبْغَةَ اللهِ'de müşâkele yoktur, çünkü boyadan söz eden kimse yok»",
   "right": "«Takdîrî müşâkeledir: sohbet, Hristiyanların söylenmeyen vaftiz sözüdür»",
   "why": {"en": "The Talkhis defines the company as actual OR estimated; the estimated kind has no spoken companion by definition.", "tr": "Telhîs sohbeti tahkîkî YAHUT takdîrî diye tarif eder; takdîrî kısmın tarif gereği söylenmiş refiki yoktur."}}],
 "relatedNotes": ["haqiqa-majaz", "majaz-mursal", "irsad", "muzawaja", "ilm-al-badi"]}

NOTE_Z = {
 "id": "muzawaja",
 "title": {"ar": "الْمُزَاوَجَةُ — أَنْ يُزَاوَجَ بَيْنَ مَعْنَيَيْنِ فِي الشَّرْطِ وَالْجَزَاءِ", "en": "The muzawaja — one consequence made to follow both the shart and the jaza", "tr": "Müzâvece — şart ile cezânın ikisine de aynı sonucu bağlamak"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — المزاوجة: أن يزاوج بين معنيين في الشرط والجزاء"],
 "question": {
  "en": ["Does the SAME consequence follow both the CONDITION and its ANSWER? Buhturi: whenever the reproacher reproached → passion PERSISTED in me; she listened to the slanderer → estrangement PERSISTED in her. That is the MUZAWAJA.",
         "Where is the pair? Two verbs — one in the shart (نَهَى), one in the jaza (أَصَاخَتْ) — each followed by the one verb لَجَّ.",
         "How is it not a muqabala? The muqabala sets counterparts against each other; the muzawaja yokes two different acts to ONE outcome."],
  "tr": ["AYNI sonuç hem ŞARTI hem CEVABINI izliyor mu? Buhturî: kınayan kınadıkça → sevgi bende DİRETTİ; iftiracıya kulak verdi → terk onda DİRETTİ. MÜZÂVECE budur.",
         "Çift nerede? İki fiil — biri şartta (نَهَى), biri cezâda (أَصَاخَتْ) — her birinin ardında tek fiil لَجَّ.",
         "Mukâbeleden farkı? Mukâbele mukâbilleri karşı karşıya koyar; müzâvece iki ayrı işi TEK sonuca koşar."]},
 "plain": {
  "en": "In a conditional sentence two meanings — one in the condition, one in the answer — each lead to the same consequence: «whenever the reproacher reproached, passion persisted in me; she listened to the slanderer, and estrangement persisted in her». The engine finds the yoke: one verb after the shart and the jaza.",
  "tr": "Bir şart cümlesinde, biri şartta biri cevapta iki ayrı mânâ aynı sonuca bağlanır: «kınayan kınadıkça sevgi bende diretti; iftiracıya kulak verdi, terk onda diretti». Motor boyunduruğu bulur: şarttan ve cezâdan sonra tekrarlanan tek fiil."},
 "explanation": {
  "en": "The MUZAWAJA (from زَاوَجَ, to pair) is أَنْ يُزَاوَجَ بَيْنَ مَعْنَيَيْنِ فِي الشَّرْطِ وَالْجَزَاءِ — that two meanings be PAIRED in the CONDITION and its ANSWER, by making one and the same consequence follow each of them. Al-Buhturi: إِذَا مَا نَهَى النَّاهِي فَلَجَّ بِيَ الْهَوَى * أَصَاخَتْ إِلَى الْوَاشِي فَلَجَّ بِهَا الْهَجْرُ — in the shart, «the reproacher reproached», and PERSISTENCE (لَجَّ) is made to follow it: passion persisted in me; in the jaza, «she listened to the slanderer», and the same persistence is made to follow: estrangement persisted in her. The two acts differ; the yoke is one. WHAT THE ENGINE CLAIMS: the BadiEngine reads the muzawaja when a conditional (إِذَا / إِنْ / مَنْ …) carries the SAME VERB LEMMA twice, once after the shart's verb and once after the jaza's verb, each introduced by a fa of consequence; it reports the two shart/jaza verbs as the pair and the repeated verb as the yoke. It grades itself against the authored `muzawaja` frame of ch59.",
  "tr": "MÜZÂVECE (زَاوَجَ'den: çiftlemek) أَنْ يُزَاوَجَ بَيْنَ مَعْنَيَيْنِ فِي الشَّرْطِ وَالْجَزَاءِ'dir — ŞART ile CEVABINDA iki mânânın, her birinin ardına aynı sonucu koyarak ÇİFTLENMESİ. Buhturî: إِذَا مَا نَهَى النَّاهِي فَلَجَّ بِيَ الْهَوَى * أَصَاخَتْ إِلَى الْوَاشِي فَلَجَّ بِهَا الْهَجْرُ — şartta «kınayan kınadı», ardına DİRENME (لَجَّ) konur: sevgi bende diretti; cezâda «iftiracıya kulak verdi», ardına aynı direnme konur: terk onda diretti. İki iş ayrı; boyunduruk bir. MOTORUN İDDİASI: BadiEngine müzâveceyi, bir şart cümlesi (إِذَا / إِنْ / مَنْ …) AYNI FİİL KÖKÜNÜ iki kere — bir kere şart fiilinden, bir kere cezâ fiilinden sonra, her biri sonuç fâsıyla — taşıdığında okur; iki şart/cezâ fiilini çift, tekrarlanan fiili boyunduruk olarak bildirir. Kendini 59. bâbın müellif `muzawaja` çerçevesine karşı sınar."},
 "examples": [
  {"ar": "إِذَا مَا نَهَى النَّاهِي فَلَجَّ بِيَ الْهَوَى * أَصَاخَتْ إِلَى الْوَاشِي فَلَجَّ بِهَا الْهَجْرُ", "en": "al-Buhturi: one persistence after each.", "tr": "Buhturî: her birinin ardında tek direnme.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "أَنْ يُزَاوَجَ بَيْنَ مَعْنَيَيْنِ فِي الشَّرْطِ وَالْجَزَاءِ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«Beyitte mukâbele vardır: kınayan / iftiracı, sevgi / terk»",
   "right": "«Müzâvecedir: iki ayrı iş aynı لَجَّ sonucuna bağlanmıştır; mukâbilleri sıralamak değil, sonucu paylaştırmaktır»",
   "why": {"en": "The muqabala needs counterparts; here the point is the shared outcome, not the opposition of the pairs.", "tr": "Mukâbele mukâbil ister; burada asıl olan çiftlerin karşıtlığı değil, paylaşılan sonuçtur."}}],
 "relatedNotes": ["muqabala", "idha-shartiyya", "in-shartiyya", "aks", "ilm-al-badi"]}

NOTE_A = {
 "id": "aks",
 "title": {"ar": "الْعَكْسُ — أَنْ يُقَدَّمَ فِي الْكَلَامِ جُزْءٌ ثُمَّ يُؤَخَّرَ", "en": "The ʿaks — a part put first, then put last", "tr": "Aks — bir cüz'ün önce öne, sonra sona konması"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — العكس: أن يقدم في الكلام جزء ثم يؤخر"],
 "question": {
  "en": ["Do two words TRADE PLACES? عَادَاتُ السَّادَاتِ سَادَاتُ الْعَادَاتِ — the habits of the masters are the masters of habits. That is the ʿAKS.",
         "Between what and what? Three shapes: a word and what it is ANNEXED to (habits-of-masters / masters-of-habits); the two DEPENDENTS of two verbs (the living out of the dead / the dead out of the living, 10:31); two words at the two ENDS of two sentences (they … for them / they … for them, 60:10).",
         "How does the engine see it? By lemma: the pair (A, B) appears, then (B, A), with the same governing shape — idafa, verb-dependents, or sentence-ends."],
  "tr": ["İki kelime YER Mİ DEĞİŞTİRİYOR? عَادَاتُ السَّادَاتِ سَادَاتُ الْعَادَاتِ — efendilerin âdetleri, âdetlerin efendileridir. AKS budur.",
         "Ne ile ne arasında? Üç şekil: bir kelime ile İZÂFE edildiği şey (efendilerin âdetleri / âdetlerin efendileri); iki fiilin iki MÜTEALLİKİ (ölüden diriyi / diriden ölüyü, Yûnus 10:31); iki cümlenin iki UCUNDAKİ iki lafız (onlar … onlara / onlar … onlara, Mümtehine 60:10).",
         "Motor nasıl görür? Kökle: (A, B) çifti geçer, sonra (B, A), aynı âmil şekliyle — izâfet, fiil müteallikleri yahut cümle uçları."]},
 "plain": {
  "en": "A part of the speech is put first, then the same part put last: «the habits of the masters are the masters of habits»; «He brings the living out of the dead and the dead out of the living»; «they are not lawful for them, nor they for them». The engine finds the swapped pair by lemma and names the shape.",
  "tr": "Sözün bir cüz'ü önce öne, sonra sona konur: «efendilerin âdetleri âdetlerin efendileridir»; «ölüden diriyi, diriden ölüyü çıkarır»; «onlar onlara helâl değil, onlar da onlara». Motor yer değiştiren çifti kökle bulur, şekli adlandırır."},
 "explanation": {
  "en": "The ʿAKS (reversal) is أَنْ يُقَدَّمَ فِي الْكَلَامِ جُزْءٌ ثُمَّ يُؤَخَّرَ — that a part of the speech be put FIRST, then put LAST; and it falls in several SHAPES. (1) Between one of a sentence's two ends and what is ANNEXED to it: عَادَاتُ السَّادَاتِ سَادَاتُ الْعَادَاتِ — the mudaf ilayh of the mubtada is the mudaf of the khabar, and the other way round. (2) Between the two DEPENDENTS of two verbs in two sentences: يُخْرِجُ الْحَيَّ مِنَ الْمَيِّتِ وَيُخْرِجُ الْمَيِّتَ مِنَ الْحَيِّ (10:31) — the object of the first verb is the majrur of the second, and the majrur the object. (3) Between two words at the two ENDS of two sentences: لَا هُنَّ حِلٌّ لَهُمْ وَلَا هُمْ يَحِلُّونَ لَهُنَّ (60:10) — the mubtada of the first sentence is the majrur of the second, and the majrur the mubtada. WHAT THE ENGINE CLAIMS: the BadiEngine reads the ʿaks by LEMMA: it looks for an ordered pair of content words (A, B) followed later in the sentence by (B, A), and names the shape from the seats DabtEngine gives the four words — mudaf/mudaf ilayh (shape 1), maf'ul/majrur of two verbs of one lemma (shape 2), mubtada/majrur across two clauses (shape 3). A pair reversed without a matching shape is reported as a plain reversal. It grades itself against the authored `aks` frames of ch59, whose sub it must match.",
  "tr": "AKS (tersine çevirme) أَنْ يُقَدَّمَ فِي الْكَلَامِ جُزْءٌ ثُمَّ يُؤَخَّرَ'dir — sözün bir cüz'ünün önce ÖNE, sonra SONA konması; birkaç ŞEKİLDE olur. (1) Cümlenin iki tarafından biri ile ona İZÂFE edilen arasında: عَادَاتُ السَّادَاتِ سَادَاتُ الْعَادَاتِ — mübtedânın muzâfun ileyhi haberin muzâfı olur, tersi de öyle. (2) İki cümledeki iki fiilin iki MÜTEALLİKİ arasında: يُخْرِجُ الْحَيَّ مِنَ الْمَيِّتِ وَيُخْرِجُ الْمَيِّتَ مِنَ الْحَيِّ (Yûnus 10:31) — birinci fiilin mef'ûlü ikincinin mecruru, mecrur mef'ûl olur. (3) İki cümlenin iki UCUNDAKİ iki lafız arasında: لَا هُنَّ حِلٌّ لَهُمْ وَلَا هُمْ يَحِلُّونَ لَهُنَّ (Mümtehine 60:10) — birinci cümlenin mübtedâsı ikincinin mecruru, mecrur mübtedâ olur. MOTORUN İDDİASI: BadiEngine aksi KÖKLE okur: sıralı bir anlamlı kelime çifti (A, B) ve cümlede daha sonra (B, A) arar, şekli DabtEngine'in dört kelimeye verdiği makamlardan adlandırır — muzâf/muzâfun ileyh (1. şekil), tek kökten iki fiilin mef'ûl/mecruru (2. şekil), iki cümlecik boyunca mübtedâ/mecrur (3. şekil). Şekli tutmayan tersine çevrilmiş çift, düz tersine çevirme olarak bildirilir. Kendini 59. bâbın müellif `aks` çerçevelerine karşı sınar; alt kısımlarını tutturması gerekir."},
 "examples": [
  {"ar": "عَادَاتُ السَّادَاتِ سَادَاتُ الْعَادَاتِ", "en": "shape 1: the mudaf and its mudaf ilayh.", "tr": "1. şekil: muzâf ve muzâfun ileyhi.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "يُخْرِجُ الْحَيَّ مِنَ الْمَيِّتِ وَيُخْرِجُ الْمَيِّتَ مِنَ الْحَيِّ", "en": "shape 2: the dependents of two verbs (10:31).", "tr": "2. şekil: iki fiilin müteallikleri (Yûnus 10:31).", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "لَا هُنَّ حِلٌّ لَهُمْ وَلَا هُمْ يَحِلُّونَ لَهُنَّ", "en": "shape 3: the ends of two sentences (60:10).", "tr": "3. şekil: iki cümlenin uçları (Mümtehine 60:10).", "sourceStory": "talkhis-al-miftah", "sentence": "s14"}],
 "commonMistakes": [
  {"wrong": "«يُخْرِجُ الْحَيَّ مِنَ الْمَيِّتِ … yalnız bir tıbâktır»",
   "right": "«Tıbâk da vardır (diri/ölü), fakat sanat akstir: iki müteallik yer değiştirmiştir»",
   "why": {"en": "Two figures live in one aya. The tibaq is in the pair of contraries; the ʿaks is in their trading of seats.", "tr": "Bir âyette iki sanat yaşar. Tıbâk zıt çiftte, aks makam değiştirmelerindedir."}},
  {"wrong": "«Her tekrar edilen kelime çifti akstir»",
   "right": "«Sıra tersine dönmelidir: (A, B) sonra (B, A)»",
   "why": {"en": "The definition is «put first, then put last». Same order twice is repetition, not reversal.", "tr": "Tarif «önce öne, sonra sona»dır. Aynı sıranın iki kere gelmesi tekrardır, ters çevirme değil."}}],
 "relatedNotes": ["tibaq", "idafa-definiteness", "taqdim-al-musnad", "muzawaja", "ilm-al-badi"]}

ADD_EN = (" Chapter 59 (lines ~4025-4060, sahifa 138-140) carries the irsad (tashim), the mushakala in fact and in estimation, the "
          "muzawaja and the ʿaks in its three shapes: the ayat (s2 9:70, s6 5:116, s7 2:138, s13 10:31, s14 60:10), the verses of "
          "ʿAmr b. Maʿdi Karib (s3), Abu l-Rafʿ (s5) and al-Buhturi (s10) and the ʿadat/sadat saying (s12) are Arabic as the source prints "
          "them. s1, s4, s7's gloss, s8-s9, s11 and the heads of s12-s14, with the frames of every example, are RESTORATIONS, not quotations: "
          "the source carries those steps only in Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's "
          "register; each is marked «restored» in its translation. The examples carry `badi` frames (irsad pairs, mushakala with its "
          "companion and asl, muzawaja with its two sides, aks with its swapped pairs and shape) beside the tibaqs inside them.")
ADD_TR = (" Elli dokuzuncu bâb (satır ~4025-4060, sahife 138-140) irsâdı (teshîm), tahkîkî ve takdîrî müşâkeleyi, müzâveceyi ve üç "
          "şekliyle aksi taşır: âyetler (s2 Tevbe 9:70, s6 Mâide 5:116, s7 Bakara 2:138, s13 Yûnus 10:31, s14 Mümtehine 60:10), Amr b. "
          "Ma'dîkerib (s3), Ebü'r-Ref' (s5) ve Buhturî (s10) beyitleri ile âdât/sâdât sözü (s12) kaynağın bastığı Arapçadır. s1, s4, s7'nin "
          "açıklaması, s8-s9, s11 ve s12-s14'ün başları, her örneğin çerçeveleriyle birlikte, ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları "
          "yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri "
          "yazılmıştır» diye işaretlidir. Örnekler, içlerindeki tıbâkların yanında `badi` çerçeveleri (irsâd çiftleri, refiki ve aslıyla "
          "müşâkele, iki tarafıyla müzâvece, yer değiştiren çiftleri ve şekliyle aks) taşır.")
write_out(59, S, TITLE, ADD_EN, ADD_TR, "4025-4060", GLOSS_ADD, notes=(NOTE_I, NOTE_K, NOTE_Z, NOTE_A),
          related=(("tibaq", ["irsad", "aks"]), ("ilm-al-badi", ["irsad", "mushakala", "muzawaja", "aks"]), ("muqabala", ["muzawaja"]), ("haqiqa-majaz", ["mushakala"]), ("saj", ["irsad"]), ("jinas", ["irsad"])))
report(59, S, GLOSS_ADD, (NOTE_I, NOTE_K, NOTE_Z, NOTE_A))
