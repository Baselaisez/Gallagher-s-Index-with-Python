# -*- coding: utf-8 -*-
"""Author chapter 57 of talkhis-al-miftah — the closing faṣl of the bayan and
the opening of the BADIʿ (sahifa 136-137, lines ~3941-3975): the majaz and the
kinaya outrank the plain word, the istiʿara the tashbih (a claim brought with
its proof); the third fann defined; its two divisions; the MUTABAQA (tibaq) —
two contraries gathered, in nouns, verbs, particles or across the two, and its
two kinds, of affirmation and of negation.

  RESTORED (the source carries the step only in Turkish): s1-s3, s5-s6, s11; the
          frames of s7-s10, s12-s13.
  As printed: the badiʿ's definition (s4), the ayat (18:18, 2:258, 2:286, 6:122,
          30:6-7, 5:44).

The tibaqs carry authored `badi` frames: the figure, its two words by index, its
kind (ijab / salb) and the class of the pair (ism / fil / harf / mixed).
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import sarf_gen as _sg

P = "fadl-al-majaz-wal-kinaya"; D = "ilm-al-badi"; Q = "tibaq"
TITLE = {"ar": "فَضْلُ الْمَجَازِ وَالْكِنَايَةِ عَلَى الْحَقِيقَةِ وَالتَّصْرِيحِ، وَعِلْمُ الْبَدِيعِ، وَالْمُطَابَقَةُ",
         "en": "Why the Majaz and the Kinaya Outrank the Plain Word; the Science of the Badiʿ; the Mutabaqa",
         "tr": "Mecaz ve Kinâyenin Hakikat ve Tasrihe Üstünlüğü; Bedî' İlmi; Mutâbakat"}
S = []
def nahwa(full="نَحْوَ", tag=Q, punct=":"):
    return tok(full, "nahwa", "noun", [tag, "maful-fih"], ("الْوَاوُ عَاطِفَةٌ، وَ" if full.startswith("وَ") else "") + "نَحْوَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ إِلَى الْمِثَالِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوَ.",
               "«such as» — a zarf annexed to the example; the khabar of a dropped «that is».", "«… gibi» — örneğe izâfe edilmiş zarf; hazfedilmiş «o»nun haberi.",
               segments=([seg("وَ", "wa", "conj"), seg("نَحْوَ", "nahwa", "noun")] if full.startswith("وَ") else None), punct=punct)

# ----------- s1 — the fasl (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "A section. The masters of eloquence agreed that the MAJAZ and the KINAYA are more eloquent than the plain word and the plain statement." + R_EN,
 "tr": "Fasıl. Belâgat erbâbı, MECAZ ve KİNÂYENİN hakikat ve tasrihten daha beliğ olduğunda ittifak etti." + R_TR},
 "tokens": [
  tok("فَصْلٌ","fasl","noun",[P, "mubtada-khabar"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«a section».", "«fasıl».", punct=":"),
  tok("أَطْبَقَ","atbaqa","verb",[P, "fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ مِنَ الرَّابِعِ — أَطْبَقُوا عَلَى كَذَا: أَجْمَعُوا عَلَيْهِ.", "«agreed unanimously» — Form IV: «they closed ranks on it».", "«ittifak etti» — IV. bâb: «üzerinde birleştiler»."),
  tok("الْبُلَغَاءُ","baligh","noun",[P, "fail", "jam-taksir", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ بَلِيغٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«the masters of eloquence» — the doer; plural of بَلِيغ on فُعَلَاء, barred from tanwin.", "«belâgat erbâbı» — fâil; بَلِيغ'in فُعَلَاء çoğulu, gayr-i munsarif."),
  tok("عَلَى","ala","part",[P, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerinde»."),
  tok("أَنَّ","anna","part",[P, "inna-wa-akhawatuha"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِعَلَى.", "«that» — the interpreted masdar is majrur by «on».", "«… olduğunda» — müevvel masdar «üzerinde» ile mecrur."),
  tok("الْمَجَازَ","majaz","noun",[P, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the majaz» — the ism of anna.", "«mecaz» — ennenin ismi."),
  tok("وَالْكِنَايَةَ","kinaya","noun",[P, "atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«and the kinaya» — joined.", "«ve kinâye» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("الْكِنَايَةَ","kinaya","noun")]),
  tok("أَبْلَغُ","ablagh","noun",[P, "inna-wa-akhawatuha", "ism-tafdil"], "خَبَرُ أَنَّ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«more eloquent» — the khabar of anna; an ism tafdil.", "«daha beliğ» — ennenin haberi; ism-i tafdîl."),
  tok("مِنَ","min","part",[P, "huruf-jarr", "ism-tafdil"], "حَرْفُ جَرٍّ — مِنْ بَعْدَ أَفْعَلِ التَّفْضِيلِ.", "«than» — the min after the tafdil.", "«-den» — ism-i tafdîlden sonraki min."),
  tok("الْحَقِيقَةِ","haqiqa","noun",[P, "huruf-jarr"], "مَجْرُورٌ.", "«the plain word».", "«hakikat»."),
  tok("وَالتَّصْرِيحِ","tasrih","noun",[P, "atf-nasaq", "masdar"], "مَعْطُوفٌ مَجْرُورٌ.", "«and the plain statement» — joined.", "«ve tasrih» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("التَّصْرِيحِ","tasrih","noun")], punct=".")]})

# ----------- s2 — the istiʿara over the tashbih (RESTORED matn)
S.append({"id": "s2", "translation": {
 "en": "And that the ISTIʿARA is more eloquent than the TASHBIH, because it is a kind of majaz." + R_EN,
 "tr": "Ve İSTİÂRENİN, mecazın bir nev'i olduğu için TEŞBİHTEN daha beliğ olduğunda." + R_TR},
 "tokens": [
  tok("وَأَنَّ","anna","part",[P, "inna-wa-akhawatuha", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — مَعْطُوفٌ عَلَى الْمَصْدَرِ الْأَوَّلِ.", "«and that» — joined onto the first interpreted masdar.", "«ve … olduğunda» — ilk müevvel masdara matuf.",
      segments=[seg("وَ","wa","conj"), seg("أَنَّ","anna","part")]),
  tok("الِاسْتِعَارَةَ","istiara","noun",[P, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the istiʿara» — the ism of anna.", "«istiâre» — ennenin ismi."),
  tok("أَبْلَغُ","ablagh","noun",[P, "inna-wa-akhawatuha", "ism-tafdil"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«more eloquent» — the khabar.", "«daha beliğ» — haber."),
  tok("مِنَ","min","part",[P, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  tok("التَّشْبِيهِ","tashbih","noun",[P, "huruf-jarr"], "مَجْرُورٌ.", "«the tashbih».", "«teşbih».", punct="،"),
  tok("لِأَنَّهَا","anna","part",[P, "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهُ.", "«because it» — the lam of cause over anna with its ism.", "«çünkü o» — ta'lîl lâmı, enne ve ismi.",
      segments=[seg("لِ","li","part"), seg("أَنَّ","anna","part"), seg("هَا","pron-3fs","pron")]),
  tok("نَوْعٌ","naw","noun",[P, "inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«a kind» — the khabar of anna.", "«bir nevi» — ennenin haberi."),
  tok("مِنَ","min","part",[P, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("الْمَجَازِ","majaz","noun",[P, "huruf-jarr"], "مَجْرُورٌ.", "«majaz».", "«mecaz».", punct=".")]})

# ----------- s3 — the reason: a claim with its proof (RESTORED matn)
S.append({"id": "s3", "translation": {
 "en": "Because in both the passage is from the entailer to the entailment, and so it is LIKE CLAIMING A THING WITH ITS PROOF." + R_EN,
 "tr": "Çünkü ikisinde de intikal melzûmdan lâzımadır; bu, BİR ŞEYİ DELİLİYLE İDDİA ETMEK GİBİDİR." + R_TR},
 "tashbih": {"kind": "mursal-mujmal", "mushabbah": [7], "bihi": [8, 9, 10], "adat": 8, "wajh": []},
 "tokens": [
  tok("لِأَنَّ","anna","part",[P, "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«because».", "«çünkü».",
      segments=[seg("لِ","li","part"), seg("أَنَّ","anna","part")]),
  tok("الِانْتِقَالَ","intiqal","noun",[P, "inna-wa-akhawatuha", "masdar"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the passage» — the ism of anna.", "«intikal» — ennenin ismi."),
  tok("فِيهِمَا","fi","part",[P, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي الْمَجَازِ وَالْكِنَايَةِ.", "«in both» — in the majaz and the kinaya.", "«ikisinde» — mecaz ve kinâyede.",
      segments=[seg("فِي","fi","part"), seg("هِمَا","pron-3d","pron")]),
  tok("مِنَ","min","part",[P, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«from» — the phrase is the khabar of anna.", "«-den» — ibare ennenin haberi."),
  tok("الْمَلْزُومِ","malzum","noun",[P, "huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«the entailer».", "«melzûm»."),
  tok("إِلَى","ila","part",[P, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("اللَّازِمِ","lazim","noun",[P, "huruf-jarr", "ism-fail"], "مَجْرُورٌ.", "«the entailment».", "«lâzım».", punct="،"),
  tok("فَهُوَ","huwa","pron",[P, "mubtada-khabar"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَهُوَ مُبْتَدَأٌ — الْمُشَبَّهُ: هَذَا الِانْتِقَالُ.", "«and so it» — the mubtada; the mushabbah: this passage.", "«ve o» — mübtedâ; müşebbeh: bu intikal.",
      segments=[seg("فَ","fa","conj"), seg("هُوَ","huwa","pron")]),
  tok("كَدَعْوَى","dawa-claim","noun",[P, "huruf-jarr", "idafa-definiteness", "tashbih", "ism-maqsur-manqus"], "الْكَافُ لِلتَّشْبِيهِ — أَدَاةُ التَّشْبِيهِ؛ وَدَعْوَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — الْمُشَبَّهُ بِهِ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«like the claiming of» — the kaf of likening, the adat; the maqsur مُشَبَّه بِه; the phrase is the khabar.", "«iddia etmek gibi» — teşbih kâfı, edat; maksûr müşebbehün bih; ibare haber.",
      segments=[seg("كَ","ka","part"), seg("دَعْوَى","dawa-claim","noun")]),
  tok("الشَّيْءِ","shay","noun",[P, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing» — mudaf ilayh.", "«bir şeyi» — muzâfun ileyh."),
  tok("بِبَيِّنَةٍ","bayyina","noun",[P, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِدَعْوَى — الدَّلِيلُ.", "«with a proof» — attached to «claiming»: the evidence.", "«bir delille» — «iddia»ya müteallik: delil.",
      segments=[seg("بِ","bi","part"), seg("بَيِّنَةٍ","bayyina","noun")], punct=".")]})

# ----------- s4 — the badiʿ defined (as printed)
S.append({"id": "s4", "translation": {
 "en": "THE THIRD ART: the science of the BADIʿ. It is a science by which are known the ways of BEAUTIFYING speech, after the fitting of the words to the situation and the plainness of the meaning have been observed.",
 "tr": "ÜÇÜNCÜ FEN: BEDÎ' ilmi. Sözü GÜZELLEŞTİRMENİN vecihlerinin, hâle mutâbakata ve delâletin açıklığına riayetten sonra kendisiyle bilindiği ilimdir."},
 "tokens": [
  tok("الْفَنُّ","fann","noun",[D, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the art» — the mubtada.", "«fen» — mübtedâ."),
  tok("الثَّالِثُ","thalith","noun",[D, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«the third» — a na't.", "«üçüncü» — na't.", punct=":"),
  tok("عِلْمُ","ilm","noun",[D, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the science of» — the khabar; a mudaf.", "«ilmi» — haber; muzâf."),
  tok("الْبَدِيعِ","badi","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْبَدِيعُ: الْمُبْتَدَعُ الْحَسَنُ.", "«the badiʿ» — mudaf ilayh: the newly-made, the fine.", "«bedî'» — muzâfun ileyh: yeni yapılmış, güzel.", punct="،"),
  tok("وَهُوَ","huwa","pron",[D, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("عِلْمٌ","ilm","noun",[D, "mubtada-khabar", "jumla-sifa"], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ بَعْدَهُ صِفَةٌ.", "«a science» — the khabar; the clause after it describes it.", "«bir ilim» — haber; sonraki cümle sıfatı."),
  tok("يُعْرَفُ","arafa","verb",[D, "jumla-sifa", "naib-al-fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«are known» — the passive.", "«bilinir» — meçhûl."),
  tok("بِهِ","bi","part",[D, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«by it».", "«kendisiyle».",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("وُجُوهُ","wajh","noun",[D, "naib-al-fail", "idafa-definiteness", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ — جَمْعُ وَجْهٍ.", "«the ways of» — the deputy doer; plural of وَجْه.", "«vecihleri» — nâib-i fâil; وَجْه'in çoğulu."),
  tok("تَحْسِينِ","tahsin","noun",[D, "idafa-definiteness", "masdar", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ حَسَّنَ.", "«beautifying» — masdar of حَسَّنَ.", "«güzelleştirme» — حَسَّنَ'nin masdarı."),
  tok("الْكَلَامِ","kalam","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«speech» — mudaf ilayh.", "«sözü» — muzâfun ileyh."),
  tok("بَعْدَ","bada","noun",[D, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after» — a zarf.", "«… -den sonra» — zarf."),
  tok("رِعَايَةِ","riaya","noun",[D, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«observing» — mudaf ilayh, a mudaf.", "«riayet» — muzâfun ileyh, muzâf."),
  tok("الْمُطَابَقَةِ","mutabaqa","noun",[D, "idafa-definiteness", "masdar", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مُطَابَقَةُ الْكَلَامِ لِمُقْتَضَى الْحَالِ: عِلْمُ الْمَعَانِي.", "«the fitting» — of speech to the situation: the science of maʿani.", "«mutâbakat» — sözün hâlin gereğine uyması: meânî ilmi."),
  tok("وَوُضُوحِ","wuduh","noun",[D, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the plainness of» — joined; a mudaf.", "«ve açıklığı» — matuf; muzâf.",
      segments=[seg("وَ","wa","conj"), seg("وُضُوحِ","wuduh","noun")]),
  tok("الدَّلَالَةِ","dalala","noun",[D, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عِلْمُ الْبَيَانِ.", "«the meaning» — the science of bayan.", "«delâletin» — beyân ilmi.", punct=".")]})

# ----------- s5 — two divisions (RESTORED matn)
S.append({"id": "s5", "translation": {
 "en": "They are of two sorts: of the MEANING and of the WORDING." + R_EN,
 "tr": "Bunlar iki türlüdür: MÂNEVÎ ve LAFZÎ." + R_TR},
 "tokens": [
  tok("وَهِيَ","hiya","pron",[D, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ — الْوُجُوهُ.", "«and they» — the ways.", "«ve onlar» — vecihler.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("ضَرْبَانِ","darb","noun",[D, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two sorts» — the khabar; raf' by the alif.", "«iki tür» — haber; elifle merfû.", punct=":"),
  tok("مَعْنَوِيٌّ","manawi","noun",[D, "badal", "ism-mansub"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ.", "«of the meaning» — badal of detail.", "«mânevî» — tafsîl bedeli."),
  tok("وَلَفْظِيٌّ","lafzi","noun",[D, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ.", "«and of the wording» — joined.", "«ve lafzî» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("لَفْظِيٌّ","lafzi","noun")], punct=".")]})

# ----------- s6 — the mutabaqa (RESTORED matn)
S.append({"id": "s6", "translation": {
 "en": "As for the meaning-figures, among them is the MUTABAQA: the gathering of two contraries — two opposed meanings — in one sentence; it is also called the TIBAQ and the TADADD." + R_EN,
 "tr": "Mânevîlere gelince, onlardan biri MUTÂBAKATTIR: iki zıddın — birbirine karşılık iki mânânın — bir cümlede toplanması; ona TIBÂK ve TEZÂD da denir." + R_TR},
 "tokens": [
  tok("أَمَّا","amma","part",[Q, "amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for».", "«… -e gelince»."),
  tok("الْمَعْنَوِيُّ","manawi","noun",[Q, "amma-tafsiliyya", "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the meaning-figure» — the mubtada.", "«mânevî olan» — mübtedâ."),
  tok("فَمِنْهُ","min","part",[Q, "amma-tafsiliyya", "huruf-jarr", "mubtada-khabar"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«among it is» — the fa of amma's answer; a fronted khabar.", "«onlardan biri» — emmânın cevap fâsı; öne alınmış haber.",
      segments=[seg("فَ","fa","conj"), seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")]),
  tok("الْمُطَابَقَةُ","mutabaqa","noun",[Q, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the mutabaqa» — the delayed mubtada.", "«mutâbakat» — sona kalmış mübtedâ.", punct="،"),
  tok("وَهِيَ","hiya","pron",[Q, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("الْجَمْعُ","jam","noun",[Q, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ جَمَعَ.", "«the gathering» — the khabar.", "«toplamak» — haber."),
  tok("بَيْنَ","bayna","noun",[Q, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between».", "«arasını»."),
  tok("مُتَضَادَّيْنِ","mutadadd","noun",[Q, "idafa-definiteness", "al-muthanna", "ism-fail", "form-vi-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنَّى مُتَضَادٍّ، اسْمِ فَاعِلِ تَضَادَّ.", "«two contraries» — the dual of the ism fa'il of تَضَادَّ.", "«iki zıt» — تَضَادَّ'nin ism-i fâilinin tesniyesi.", punct="،"),
  tok("أَيْ","ay","part",[Q], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  tok("مَعْنَيَيْنِ","mana","noun",[Q, "badal", "al-muthanna"], "بَدَلٌ مِنْ مُتَضَادَّيْنِ مَجْرُورٌ بِالْيَاءِ — مُثَنَّى مَعْنًى، رُدَّتْ أَلِفُهُ يَاءً.", "«two meanings» — badal; the dual of مَعْنًى, its alif turned to a ya.", "«iki mânâ» — bedel; مَعْنًى'nın tesniyesi, elifi yâya dönmüş."),
  tok("مُتَقَابِلَيْنِ","mutaqabil","noun",[Q, "naat-sifa", "al-muthanna", "ism-fail", "form-vi-verbs"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ.", "«opposed» — a na't in the dual.", "«karşılıklı» — tesniye na't."),
  tok("فِي","fi","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْجُمْلَةِ","jumla","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«the sentence».", "«cümle».", punct="،"),
  tok("وَتُسَمَّى","samma","verb",[Q, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — هِيَ.", "«and it is called» — the passive; its deputy doer concealed «it».", "«ve denir» — meçhûl; nâib-i fâil gizli «o».",
      segments=[seg("وَ","wa","conj"), seg("تُسَمَّى","samma","verb")]),
  tok("الطِّبَاقَ","tibaq","noun",[Q, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«the tibaq» — the second object.", "«tıbâk» — ikinci mef'ûl."),
  tok("وَالتَّضَادَّ","tadadd","noun",[Q, "atf-nasaq", "masdar"], "مَعْطُوفٌ مَنْصُوبٌ.", "«and the tadadd» — joined.", "«ve tezâd» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("التَّضَادَّ","tadadd","noun")], punct=".")]})

# ----------- s7 — two nouns: 18:18 (frame RESTORED, aya as printed)
S.append({"id": "s7", "translation": {
 "en": "It comes with two words of one kind — two nouns, such as: «And you would think them AWAKE, while they are ASLEEP» (18:18)." + R_EN,
 "tr": "Bir nevden iki lafızla olur — iki isim; «Onları UYANIK sanırsın, hâlbuki onlar UYKUDADIRLAR» (Kehf 18:18) gibi." + R_TR},
 "badi": [bd("tibaq", [8, 10], sub="ijab", cls="ism")],
 "tokens": [
  tok("وَيَكُونُ","kana","verb",[Q, "kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — هُوَ، الطِّبَاقُ.", "«and it comes» — kana; its ism concealed: the tibaq.", "«ve olur» — kâne; ismi gizli: tıbâk.",
      segments=[seg("وَ","wa","conj"), seg("يَكُونُ","kana","verb")]),
  tok("بِلَفْظَيْنِ","lafz","noun",[Q, "huruf-jarr", "kana-wa-akhawatuha", "al-muthanna"], "جَارٌّ وَمَجْرُورٌ بِالْيَاءِ خَبَرُ يَكُونُ — مُثَنًّى.", "«with two words» — the dual; kana's khabar.", "«iki lafızla» — tesniye; kânenin haberi.",
      segments=[seg("بِ","bi","part"), seg("لَفْظَيْنِ","lafz","noun")]),
  tok("مِنْ","min","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("نَوْعٍ","naw","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«a kind».", "«bir nev»."),
  tok("وَاحِدٍ","wahid","noun",[Q, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«one» — a na't.", "«tek» — na't.", punct=":"),
  tok("اسْمَيْنِ","ism","noun",[Q, "badal", "al-muthanna"], "بَدَلٌ مِنْ لَفْظَيْنِ مَجْرُورٌ بِالْيَاءِ.", "«two nouns» — badal of «two words».", "«iki isim» — «iki lafız»ın bedeli.", punct="،"),
  nahwa(),
  tok("وَتَحْسَبُهُمْ","hasiba","verb",[Q, "mafulayn", "mudari-marfu"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَتَحْسَبُ فِعْلٌ مُضَارِعٌ مِنْ أَفْعَالِ الْقُلُوبِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا — أَنْتَ، وَهُمْ مَفْعُولٌ أَوَّلُ.", "«and you would think them» — a verb of the heart; «you» concealed of necessity; «them» the first object.", "«ve onları sanırsın» — kalp fiili; «sen» vücûben gizli; «onları» birinci mef'ûl.",
      segments=[seg("وَ","wa","conj"), seg("تَحْسَبُ","hasiba","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("أَيْقَاظًا","yaqzan","noun",[Q, "mafulayn", "jam-taksir"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — جَمْعُ يَقْظَانَ؛ أَحَدُ طَرَفَيِ الطِّبَاقِ.", "«awake» — the second object; plural of يَقْظَان: one end of the tibaq.", "«uyanık» — ikinci mef'ûl; يَقْظَان'ın çoğulu: tıbâkın bir ucu."),
  tok("وَهُمْ","hum","pron",[Q, "hal", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَهُمْ مُبْتَدَأٌ — وَالْجُمْلَةُ حَالٌ.", "«while they» — the waw of the hal; the mubtada.", "«hâlbuki onlar» — hâl vâvı; mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُمْ","hum","pron")]),
  tok("رُقُودٌ","raqid","noun",[Q, "mubtada-khabar", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ — جَمْعُ رَاقِدٍ؛ الطَّرَفُ الْآخَرُ: بَيْنَ الْيَقَظَةِ وَالرُّقَادِ تَقَابُلُ الْعَدَمِ وَالْمَلَكَةِ.", "«asleep» — the khabar; plural of رَاقِد: the other end — between waking and sleep, the opposition of a state and its lack.", "«uykuda» — haber; رَاقِد'in çoğulu: öteki uç — uyanıklıkla uyku arasında adem ve meleke tekabülü.", punct=".")]})

# ----------- s8 — two verbs: 2:258
S.append({"id": "s8", "translation": {
 "en": "Or two verbs, such as: «He GIVES LIFE and CAUSES DEATH» (2:258)." + R_EN,
 "tr": "Yahut iki fiil; «DİRİLTİR ve ÖLDÜRÜR» (Bakara 2:258) gibi." + R_TR},
 "badi": [bd("tibaq", [3, 4], sub="ijab", cls="fil")],
 "tokens": [
  tok("أَوْ","aw","conj",[Q, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("فِعْلَيْنِ","fil","noun",[Q, "atf-nasaq", "al-muthanna"], "مَعْطُوفٌ عَلَى اسْمَيْنِ مَجْرُورٌ بِالْيَاءِ.", "«two verbs» — joined onto «two nouns».", "«iki fiil» — «iki isim»e matuf.", punct="،"),
  nahwa(),
  tok("يُحْيِي","ahya","verb",[Q, "fail", "form-iv-verbs", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، اللهُ.", "«He gives life» — raf' estimated on the ya; the doer «He» concealed.", "«diriltir» — zamme yâ üzerinde takdîrî; fâil gizli «O»."),
  tok("وَيُمِيتُ","amata","verb",[Q, "atf-nasaq", "form-iv-verbs", "hollow-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيُمِيتُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ؛ الطَّرَفُ الْآخَرُ.", "«and causes death» — joined; a hollow verb; the other end.", "«ve öldürür» — matuf; ecvef; öteki uç.",
      segments=[seg("وَ","wa","conj"), seg("يُمِيتُ","amata","verb")], punct=".")]})

# ----------- s9 — two particles: 2:286
S.append({"id": "s9", "translation": {
 "en": "Or two particles, such as: «FOR it is what it earned, and AGAINST it is what it deserved» (2:286)." + R_EN,
 "tr": "Yahut iki harf; «Kazandığı LEHİNE, işlediği ALEYHİNEDİR» (Bakara 2:286) gibi." + R_TR},
 "badi": [bd("tibaq", [3, 6], sub="ijab", cls="harf")],
 "tokens": [
  tok("أَوْ","aw","conj",[Q, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("حَرْفَيْنِ","harf","noun",[Q, "atf-nasaq", "al-muthanna"], "مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ.", "«two particles» — joined.", "«iki harf» — matuf.", punct="،"),
  nahwa(),
  tok("لَهَا","lahu","part",[Q, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — اللَّامُ لِلنَّفْعِ: أَحَدُ طَرَفَيِ الطِّبَاقِ.", "«for it» — the fronted khabar; the lam of benefit: one end of the tibaq.", "«lehine» — öne alınmış haber; fayda lâmı: tıbâkın bir ucu.",
      segments=[seg("لَ","li","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","pron",[Q, "mubtada-khabar", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what» — the delayed mubtada.", "«şey» — sona kalmış mübtedâ."),
  tok("كَسَبَتْ","kasaba","verb",[Q, "ism-mawsul", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — هِيَ، النَّفْسُ؛ وَالْجُمْلَةُ صِلَةٌ.", "«it earned» — the doer «it» (the soul) concealed; the sila.", "«kazandı» — fâil gizli «o» (nefis); sıla.",
      segments=[seg("كَسَبَ","kasaba","verb"), seg("تْ","ta-tanith","part")]),
  tok("وَعَلَيْهَا","ala","part",[Q, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَعَلَيْهَا خَبَرٌ مُقَدَّمٌ — عَلَى لِلضَّرَرِ: الطَّرَفُ الْآخَرُ.", "«and against it» — a fronted khabar; ʿala of harm: the other end.", "«ve aleyhine» — öne alınmış haber; zarar alâsı: öteki uç.",
      segments=[seg("وَ","wa","conj"), seg("عَلَيْ","ala","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","pron",[Q, "mubtada-khabar", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what» — the delayed mubtada.", "«şey» — mübtedâ."),
  tok("اكْتَسَبَتْ","iktasaba","verb",[Q, "ism-mawsul", "form-viii-verbs"], "فِعْلٌ مَاضٍ مِنَ الِافْتِعَالِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — هِيَ.", "«it deserved» — Form VIII; the doer concealed.", "«işledi» — VIII. bâb; fâil gizli.",
      segments=[seg("اكْتَسَبَ","iktasaba","verb"), seg("تْ","ta-tanith","part")], punct=".")]})

# ----------- s10 — of two kinds: 6:122
S.append({"id": "s10", "translation": {
 "en": "Or with two words of two kinds, such as: «Is he who was DEAD, and We GAVE HIM LIFE…?» (6:122)." + R_EN,
 "tr": "Yahut iki nevden iki lafızla; «ÖLÜ iken kendisini DİRİLTTİĞİMİZ kimse mi…?» (En'âm 6:122) gibi." + R_TR},
 "badi": [bd("tibaq", [6, 7], sub="ijab", cls="mixed")],
 "majaz": [mj(7, "istiara", "mushabaha", {"en": "We gave him life", "tr": "onu dirilttik"}, {"en": "We guided him — misguidance is a death, guidance a life", "tr": "ona hidâyet ettik — dalâlet ölüm, hidâyet hayattır"},
              istiara=ist("tabaiyya", ends="wifaqiyya", seat="maful"))],
 "tokens": [
  tok("أَوْ","aw","conj",[Q, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("مِنْ","min","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى مِنْ نَوْعٍ.", "«of» — joined onto «of one kind».", "«-den» — «bir nevden»e matuf."),
  tok("نَوْعَيْنِ","naw","noun",[Q, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two kinds» — the dual.", "«iki nev» — tesniye.", punct="،"),
  nahwa(),
  tok("أَوَمَنْ","man-mawsula","pron",[Q, "ism-mawsul", "mubtada-khabar", "al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«is he who» — the hamza of denial, the waw, and the relative as mubtada.", "«… kimse mi» — inkâr hemzesi, vâv ve mübtedâ olan ism-i mevsûl.",
      segments=[seg("أَ","hamza-istifham","part"), seg("وَ","wa","conj"), seg("مَنْ","man-mawsula","pron")]),
  tok("كَانَ","kana","verb",[Q, "ism-mawsul", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ صِلَةٌ.", "«was» — kana; its ism concealed; the sila.", "«idi» — kâne; ismi gizli; sıla."),
  tok("مَيْتًا","mayt","noun",[Q, "kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ — اسْمٌ؛ أَحَدُ طَرَفَيِ الطِّبَاقِ.", "«dead» — kana's khabar; a NOUN: one end of the tibaq.", "«ölü» — kânenin haberi; İSİM: tıbâkın bir ucu."),
  tok("فَأَحْيَيْنَاهُ","ahya","verb",[Q, "atf-nasaq", "form-iv-verbs", "naqis-verbs", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَأَحْيَيْنَا فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — فِعْلٌ؛ الطَّرَفُ الْآخَرُ: طِبَاقٌ بَيْنَ اسْمٍ وَفِعْلٍ.", "«and We gave him life» — a VERB, «We» its doer, «him» its object: the other end — a tibaq between a noun and a verb.", "«ve onu dirilttik» — FİİL, «biz» fâili, «onu» mef'ûlü: öteki uç — isimle fiil arasında tıbâk.",
      segments=[seg("فَ","fa","conj"), seg("أَحْيَيْ","ahya","verb"), seg("نَا","pron-1p","pron"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s11 — two kinds (RESTORED matn)
S.append({"id": "s11", "translation": {
 "en": "It is of two kinds: the tibaq OF AFFIRMATION, as in what has passed, and the tibaq OF NEGATION." + R_EN,
 "tr": "İki kısımdır: geçenlerdeki gibi ÎCÂB tıbâkı ve SELB tıbâkı." + R_TR},
 "tokens": [
  tok("وَهُوَ","huwa","pron",[Q, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("ضَرْبَانِ","darb","noun",[Q, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds» — the khabar.", "«iki kısım» — haber.", punct=":"),
  tok("طِبَاقُ","tibaq","noun",[Q, "badal", "idafa-definiteness"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ، مُضَافٌ.", "«the tibaq of» — badal of detail; a mudaf.", "«tıbâkı» — tafsîl bedeli; muzâf."),
  tok("الْإِيجَابِ","ijab-affirm","noun",[Q, "idafa-definiteness", "masdar", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ أَوْجَبَ.", "«affirmation» — mudaf ilayh; masdar of أَوْجَبَ.", "«îcâb» — muzâfun ileyh; أَوْجَبَ'nin masdarı."),
  tok("كَمَا","ka","part",[Q, "huruf-jarr"], "الْكَافُ جَارَّةٌ وَمَا مَصْدَرِيَّةٌ — كَالَّذِي مَرَّ.", "«as» — the kaf over the masdar-making ma.", "«… gibi» — kâf ve masdariyye mâ.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("مَرَّ","marra","verb",[Q, "doubled-verbs"], "فِعْلٌ مَاضٍ مُضَاعَفٌ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ.", "«has passed» — the doubled verb; the doer concealed.", "«geçti» — muzâaf fiil; fâil gizli.", punct="،"),
  tok("وَطِبَاقُ","tibaq","noun",[Q, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَطِبَاقُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and the tibaq of» — joined; a mudaf.", "«ve tıbâkı» — matuf; muzâf.",
      segments=[seg("وَ","wa","conj"), seg("طِبَاقُ","tibaq","noun")]),
  tok("السَّلْبِ","salb","noun",[Q, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ سَلَبَ: النَّفْيُ.", "«negation» — mudaf ilayh; masdar of سَلَبَ.", "«selb» — muzâfun ileyh; سَلَبَ'nin masdarı: nefiy.", punct=".")]})

# ----------- s12 — 30:6-7
S.append({"id": "s12", "translation": {
 "en": "Such as: «…but most people DO NOT KNOW. They KNOW an outward part of the life of this world» (30:6-7)." + R_EN,
 "tr": "«…fakat insanların çoğu BİLMEZLER. Onlar dünya hayatının dış yüzünü BİLİRLER» (Rûm 30:6-7) gibi." + R_TR},
 "badi": [bd("tibaq", [5, 6], sub="salb", cls="fil")],
 "tokens": [
  nahwa(),
  tok("وَلَكِنَّ","lakinna","part",[Q, "inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَلَكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ.", "«but» — the sister of inna that corrects.", "«fakat» — innenin istidrâk kardeşi.",
      segments=[seg("وَ","wa","conj"), seg("لَكِنَّ","lakinna","part")]),
  tok("أَكْثَرَ","akthar","noun",[Q, "inna-wa-akhawatuha", "idafa-definiteness", "ism-tafdil"], "اسْمُ لَكِنَّ مَنْصُوبٌ، مُضَافٌ.", "«most of» — the ism of lakinna; a mudaf.", "«çoğu» — lâkinnenin ismi; muzâf."),
  tok("النَّاسِ","nas","noun",[Q, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«people» — mudaf ilayh.", "«insanların» — muzâfun ileyh."),
  tok("لَا","la-nafiya","part",[Q, "inna-wa-akhawatuha"], "حَرْفُ نَفْيٍ — بِهِ يَكُونُ الطِّبَاقُ سَلْبًا.", "«not» — the negation that makes the tibaq one of negation.", "«-mez» — tıbâkı selb yapan nefiy."),
  tok("يَعْلَمُونَ","alima","verb",[Q, "inna-wa-akhawatuha", "fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ؛ وَالْجُمْلَةُ خَبَرُ لَكِنَّ — الطَّرَفُ الْمَنْفِيُّ.", "«they know» — raf' by the nun; the waw its doer; lakinna's khabar — the negated end.", "«bilirler» — nûnun sübûtuyla merfû; vâv fâil; lâkinnenin haberi — nefyedilen uç.",
      segments=[seg("يَعْلَمُ","alima","verb"), seg("ونَ","pron-3mp","pron")], punct="."),
  tok("يَعْلَمُونَ","alima","verb",[Q, "fail", "mudari-marfu", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — الطَّرَفُ الْمُثْبَتُ: طِبَاقُ السَّلْبِ بَيْنَ نَفْيِ الْفِعْلِ وَإِثْبَاتِهِ.", "«they know» — the affirmed end: a tibaq of negation between a verb denied and the same verb affirmed.", "«bilirler» — isbat edilen uç: fiilin nefyi ile isbatı arasında selb tıbâkı.",
      segments=[seg("يَعْلَمُ","alima","verb"), seg("ونَ","pron-3mp","pron")]),
  tok("ظَاهِرًا","zahir","noun",[Q, "maful-bihi", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«an outward part» — the object.", "«dış yüzünü» — mef'ûl."),
  tok("مِنَ","min","part",[Q, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("الْحَيَاةِ","hayat","noun",[Q, "huruf-jarr"], "مَجْرُورٌ.", "«the life».", "«hayatın»."),
  tok("الدُّنْيَا","dunya","noun",[Q, "naat-sifa", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«of this world» — a na't; the maqsur.", "«dünya» — na't; maksûr.", punct=".")]})

# ----------- s13 — 5:44
S.append({"id": "s13", "translation": {
 "en": "And such as: «So DO NOT FEAR the people, but FEAR ME» (5:44)." + R_EN,
 "tr": "Ve «İnsanlardan KORKMAYIN, BENDEN KORKUN» (Mâide 5:44) gibi." + R_TR},
 "badi": [bd("tibaq", [2, 4], sub="salb", cls="fil")],
 "tokens": [
  nahwa("وَنَحْوَ"),
  tok("فَلَا","la-nahiya","part",[Q, "la-nahiya"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«so do not» — the la of prohibition.", "«öyleyse … -mayın» — nehiy lâsı.",
      segments=[seg("فَ","fa","conj"), seg("لَا","la-nahiya","part")]),
  tok("تَخْشَوُا","khashiya","verb",[Q, "la-nahiya", "naqis-verbs", "afal-khamsa", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، ضُمَّتْ لِالْتِقَاءِ السَّاكِنَيْنِ — الطَّرَفُ الْمَنْفِيُّ.", "«fear» — jazm by dropping the nun; the waw its doer, given a damma where two sakins meet: the negated end.", "«korkun» — nûnun düşmesiyle meczum; vâv fâil, iki sâkin buluşunca zamme almış: nefyedilen uç.",
      segments=[seg("تَخْشَ","khashiya","verb"), seg("وُا","pron-2mp","pron")]),
  tok("النَّاسَ","nas","noun",[Q, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the people» — the object.", "«insanlardan» — mef'ûl."),
  tok("وَاخْشَوْنِ","khashiya","verb",[Q, "imperative-amr", "naqis-verbs", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَاخْشَوْا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ الْمَحْذُوفَةُ مَفْعُولٌ بِهِ — الطَّرَفُ الْمُثْبَتُ.", "«but fear Me» — the amr built on the dropped nun; the guarding nun; the speaker's ya, dropped, its object: the affirmed end.", "«ve benden korkun» — nûnun düşmesi üzere mebnî emir; vikâye nûnu; hazfedilmiş mütekellim yâsı mef'ûl: isbat edilen uç.",
      segments=[seg("وَ","wa","conj"), seg("اخْشَ","khashiya","verb"), seg("وْ","pron-2mp","pron"), seg("نِ","pron-1s","pron")], punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "fasl": find_gloss("fasl"),
 "atbaqa": G("atbaqa", "أَطْبَقَ", "ط ب ق", "verb", "to agree unanimously (عَلَى: on); to close, cover (Form IV)", "ittifak etmek (عَلَى: üzerinde); kapamak (IV. bâb)", 5, form="IV"),
 "baligh": find_gloss("baligh"), "ala": find_gloss("ala"), "anna": find_gloss("anna"), "majaz": find_gloss("majaz"), "kinaya": find_gloss("kinaya"),
 "ablagh": find_gloss("ablagh"), "min": find_gloss("min"), "haqiqa": find_gloss("haqiqa"), "tasrih": find_gloss("tasrih"), "istiara": find_gloss("istiara"),
 "tashbih": find_gloss("tashbih"), "li": find_gloss("li"), "naw": find_gloss("naw"), "intiqal": find_gloss("intiqal"), "fi": find_gloss("fi"),
 "malzum": find_gloss("malzum"), "ila": find_gloss("ila"), "lazim": find_gloss("lazim"), "huwa": find_gloss("huwa"),
 "dawa-claim": G("dawa-claim", "دَعْوَى", "د ع و", "noun", "a claim (a maqsur noun)", "iddia, dâvâ (maksûr isim)", 4, plural="دَعَاوَى"),
 "shay": find_gloss("shay"), "bayyina": find_gloss("bayyina"), "bi": find_gloss("bi"),
 "fann": G("fann", "فَنّ", "ف ن ن", "noun", "an art, a branch of knowledge", "fen, ilim dalı", 3, plural="فُنُون"),
 "thalith": find_gloss("thalith"), "ilm": find_gloss("ilm"), "badi": find_gloss("badi"), "arafa": find_gloss("arafa"), "wajh": find_gloss("wajh"),
 "tahsin": G("tahsin", "تَحْسِين", "ح س ن", "noun", "beautifying (masdar of حَسَّنَ)", "güzelleştirme (حَسَّنَ'nin masdarı)", 4),
 "kalam": find_gloss("kalam"), "bada": find_gloss("bada"), "riaya": find_gloss("riaya"), "mutabaqa": find_gloss("mutabaqa"), "wuduh": find_gloss("wuduh"), "dalala": find_gloss("dalala"),
 "hiya": find_gloss("hiya"), "darb": find_gloss("darb"), "manawi": find_gloss("manawi"), "lafzi": find_gloss("lafzi"), "amma": find_gloss("amma"),
 "jam": G("jam", "جَمْع", "ج م ع", "noun", "gathering (masdar of جَمَعَ); the plural", "toplama (جَمَعَ'nin masdarı); cemi", 3),
 "bayna": find_gloss("bayna"),
 "mutadadd": G("mutadadd", "مُتَضَادّ", "ض د د", "noun", "contrary, opposed (ism fa'il of تَضَادَّ)", "zıt, birbirine karşıt (تَضَادَّ'nin ism-i fâili)", 5),
 "ay": find_gloss("ay"), "mana": find_gloss("mana"),
 "mutaqabil": G("mutaqabil", "مُتَقَابِل", "ق ب ل", "noun", "facing, opposed (ism fa'il of تَقَابَلَ)", "karşılıklı (تَقَابَلَ'nin ism-i fâili)", 4),
 "jumla": find_gloss("jumla"), "samma": find_gloss("samma"),
 "tibaq": G("tibaq", "طِبَاق", "ط ب ق", "noun", "tibaq — two contraries gathered in one sentence (masdar of طَابَقَ)", "tıbâk — bir cümlede toplanmış iki zıt (طَابَقَ'nin masdarı)", 5),
 "tadadd": find_gloss("tadadd"), "kana": find_gloss("kana"), "lafz": find_gloss("lafz"), "wahid": find_gloss("wahid"), "ism": find_gloss("ism"),
 "nahwa": G("nahwa", "نَحْوَ", "ن ح و", "noun", "such as, like (the noun نَحْو annexed to an example)", "… gibi (örneğe izâfe edilmiş نَحْو ismi)", 2),
 "hasiba": find_gloss("hasiba"),
 "yaqzan": G("yaqzan", "يَقْظَان", "ي ق ظ", "noun", "awake (the فَعْلَان sifa of يَقِظَ)", "uyanık (يَقِظَ'nin فَعْلَان sıfatı)", 4, plural="أَيْقَاظ"),
 "hum": find_gloss("hum"),
 "raqid": G("raqid", "رَاقِد", "ر ق د", "noun", "asleep (ism fa'il of رَقَدَ)", "uyuyan (رَقَدَ'nin ism-i fâili)", 4, plural="رُقُود"),
 "aw": find_gloss("aw"), "fil": find_gloss("fil"), "ahya": find_gloss("ahya"), "amata": find_gloss("amata"), "harf": find_gloss("harf"), "lahu": find_gloss("lahu"),
 "ma-mawsula": find_gloss("ma-mawsula"),
 "kasaba": G("kasaba", "كَسَبَ", "ك س ب", "verb", "to earn, acquire (كَسَبَ يَكْسِبُ)", "kazanmak (كَسَبَ يَكْسِبُ)", 2, form="I"),
 "iktasaba": G("iktasaba", "اِكْتَسَبَ", "ك س ب", "verb", "to earn for oneself, incur (Form VIII)", "kazanmak, işlemek (VIII. bâb)", 4, form="VIII"),
 "man-mawsula": find_gloss("man-mawsula"), "hamza-istifham": find_gloss("hamza-istifham"),
 "mayt": G("mayt", "مَيْت", "م و ت", "noun", "dead (a lightened مَيِّت)", "ölü (hafifletilmiş مَيِّت)", 3, plural="أَمْوَات"),
 "ijab-affirm": G("ijab-affirm", "إِيجَاب", "و ج ب", "noun", "affirmation (masdar of أَوْجَبَ) — the tibaq of affirmation", "îcâb, isbat (أَوْجَبَ'nin masdarı) — îcâb tıbâkı", 4),
 "ka": find_gloss("ka"), "ma-masdariyya": find_gloss("ma-masdariyya"), "marra": find_gloss("marra"),
 "salb": G("salb", "سَلْب", "س ل ب", "noun", "negation (masdar of سَلَبَ) — the tibaq of negation", "selb, nefiy (سَلَبَ'nin masdarı) — selb tıbâkı", 4),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but — the corrective sister of inna", "fakat — innenin istidrâk kardeşi", 2),
 "akthar": find_gloss("akthar"), "nas": find_gloss("nas"), "la-nafiya": find_gloss("la-nafiya"), "alima": find_gloss("alima"), "zahir": find_gloss("zahir"),
 "hayat": find_gloss("hayat"), "dunya": find_gloss("dunya"), "la-nahiya": find_gloss("la-nahiya"),
 "khashiya": G("khashiya", "خَشِيَ", "خ ش ي", "verb", "to fear, dread (naqis: خَشِيَ يَخْشَى)", "korkmak (nâkıs: خَشِيَ يَخْشَى)", 3, form="I"),
 "wa": find_gloss("wa"), "fa": find_gloss("fa"), "pron-3ms": find_gloss("pron-3ms"), "pron-3fs": find_gloss("pron-3fs"), "pron-3mp": find_gloss("pron-3mp"),
 "pron-2mp": find_gloss("pron-2mp"), "pron-1p": find_gloss("pron-1p"), "pron-1s": find_gloss("pron-1s"), "pron-3d": find_gloss("pron-3d"), "ta-tanith": find_gloss("ta-tanith"),
}

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "atbaqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْبَق", "طْبِق", "أَطْبِق", "إِطْبَاق", "مُطْبِق", "مُطْبَق", "أُطْبِقَ", "يُطْبَقُ",
                                    "أَطْبَقُوا عَلَى الشَّيْءِ: أَجْمَعُوا عَلَيْهِ."))
put_morph(mo, "kasaba", _sg.sound1("daraba", "كَسَب", "كْسِب", "اِكْسِب", "كَسْب", "كَاسِب", "مَكْسُوب", "كُسِبَ", "يُكْسَبُ"))
put_morph(mo, "iktasaba", _sg.derived(_sg.B8, _sg.W8, "َ", "اِكْتَسَب", "كْتَسِب", "اِكْتَسِب", "اِكْتِسَاب", "مُكْتَسِب", "مُكْتَسَب", "اُكْتُسِبَ", "يُكْتَسَبُ"))
# خَشِيَ is the KASRA-type naqis (بَقِيَ، خَفِيَ): naqis1 builds the alif type (رَمَى) and would ship *خَشِى — the
# ch8 lesson, paid again by the regeneration gate; built through entry() with mazi_naqis_kasra
put_morph(mo, "khashiya", _sg.entry(
    _sg.BABS["samia"][0] + " — نَاقِصٌ يَائِيٌّ", _sg.BABS["samia"][1], "خَشْيَة", "خَاشٍ (الْخَاشِي)",
    _sg.mazi_naqis_kasra("خَشِ", "خَشُوا"), _sg.mudari_naqis("َ", "خْش", "a"), _sg.amr_naqis("اِخْش", "a"),
    "يَخْشَى", "يَخْشَ", "تَخْشَ", "مَخْشِيّ", "خُشِيَ", "يُخْشَى",
    note="نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ: خَشِيَ يَخْشَى — تَخْشَوُا، اخْشَوْنِ: حُذِفَتِ الْأَلِفُ قَبْلَ وَاوِ الْجَمَاعَةِ."))
for k in ("arafa", "hasiba", "ahya", "amata", "alima", "marra", "samma", "kana"):
    if k not in mo["verbs"] and has_morph(k): mo["verbs"][k] = find_morph(k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_P = {
 "id": "fadl-al-majaz-wal-kinaya",
 "title": {"ar": "فَضْلُ الْمَجَازِ وَالْكِنَايَةِ — كَدَعْوَى الشَّيْءِ بِبَيِّنَةٍ", "en": "Why the majaz and the kinaya outrank the plain word — a claim with its proof", "tr": "Mecaz ve kinâyenin üstünlüğü — deliliyle bir iddia"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — فصل: أطبق البلغاء على أن المجاز والكناية أبلغ من الحقيقة والتصريح"],
 "question": {
  "en": ["Which says MORE — «he is generous» or «his ash is much»? The plain word asserts; the kinaya hands over the evidence (much ash → many guests) and lets the hearer draw the claim. That is why the masters agreed the majaz and the kinaya are more eloquent.",
         "Why is the ISTIʿARA above the TASHBIH? Because it is a kind of majaz: «I saw a lion» drops the likening and asserts the lion.",
         "What is the mechanism? In both, the mind passes FROM THE ENTAILER TO THE ENTAILMENT — like claiming a thing with its proof in hand."],
  "tr": ["Hangisi DAHA ÇOK söyler — «cömerttir» mi, «külü çoktur» mu? Hakikat iddia eder; kinâye delili verir (çok kül → çok misafir) ve iddiayı dinleyene çıkarttırır. Üstatların mecaz ve kinâyeyi daha beliğ saymalarının sebebi budur.",
         "İSTİÂRE neden TEŞBİHİN üstündedir? Çünkü mecazın bir nev'idir: «bir arslan gördüm», benzetmeyi düşürüp arslanı iddia eder.",
         "Mekanizma nedir? İkisinde de zihin MELZÛMDAN LÂZIMA geçer — elde deliliyle bir şeyi iddia etmek gibi."]},
 "plain": {
  "en": "The bayan closes with its verdict: the majaz and the kinaya are more eloquent than the plain word, and the istiʿara more than the tashbih, because each states a thing by what entails it — a claim carried with its proof. The engine marks the bridge and the ladder as that proof: the clue, the rungs.",
  "tr": "Beyân hükmüyle kapanır: mecaz ve kinâye hakikatten, istiâre teşbihten daha beliğdir; çünkü her biri bir şeyi onu gerektirenle söyler — deliliyle taşınan bir iddia. Motor köprüyü ve merdiveni o delil olarak işaretler: karîne, basamaklar."},
 "explanation": {
  "en": "The masters of eloquence AGREED (أَطْبَقَ الْبُلَغَاءُ) that the MAJAZ and the KINAYA are MORE ELOQUENT than the plain word (الْحَقِيقَة) and the plain statement (التَّصْرِيح), and that the ISTIʿARA is more eloquent than the TASHBIH, because it is a kind of majaz. The REASON: in both the passage is FROM THE ENTAILER TO THE ENTAILMENT (مِنَ الْمَلْزُومِ إِلَى اللَّازِمِ) — the speaker names the thing that entails what he means, and the hearer's own mind supplies the meant — and that is LIKE CLAIMING A THING WITH ITS PROOF (كَدَعْوَى الشَّيْءِ بِبَيِّنَةٍ): «his ash is much» carries the guests inside it as «he is generous» does not; «I saw a lion» carries the bravery as «he is like a lion» does not, having dropped the likening. WHAT THE ENGINE CLAIMS: it draws the proof the chapter speaks of — on the majaz bridge the CLUE that bars the literal sense, on the kinaya ladder the RUNGS the mind climbs — and it reports for every frame which of the two it holds: a clue (majaz) or an open literal sense (kinaya). It does not rank the eloquence of a sentence; that verdict is the chapter's, stated once for all.",
  "tr": "Belâgat erbâbı, MECAZ ve KİNÂYENİN hakikat (الْحَقِيقَة) ve tasrihten (التَّصْرِيح) DAHA BELİĞ olduğunda ve İSTİÂRENİN, mecazın bir nev'i olduğu için TEŞBİHTEN daha beliğ olduğunda İTTİFAK ETTİ (أَطْبَقَ الْبُلَغَاءُ). SEBEP: ikisinde de intikal MELZÛMDAN LÂZIMADIR (مِنَ الْمَلْزُومِ إِلَى اللَّازِمِ) — konuşan, kastettiğini gerektiren şeyi adlandırır, kastedileni dinleyenin kendi zihni tamamlar — ve bu, BİR ŞEYİ DELİLİYLE İDDİA ETMEK GİBİDİR (كَدَعْوَى الشَّيْءِ بِبَيِّنَةٍ): «külü çoktur», «cömerttir»in taşımadığı misafirleri içinde taşır; «bir arslan gördüm», benzetmeyi düşürmüş olarak, «arslan gibidir»in taşımadığı cesareti taşır. MOTORUN İDDİASI: bâbın söz ettiği delili çizer — mecaz köprüsünde hakikati engelleyen KARÎNEYİ, kinâye merdiveninde zihnin çıktığı BASAMAKLARI — ve her çerçeve için ikisinden hangisini tuttuğunu bildirir: bir karîne (mecaz) yahut açık kalan hakikî mânâ (kinâye). Bir cümlenin belâgatini sıralamaz; o hüküm bâbındır, bir kere herkes için verilmiştir."},
 "examples": [
  {"ar": "أَطْبَقَ الْبُلَغَاءُ عَلَى أَنَّ الْمَجَازَ وَالْكِنَايَةَ أَبْلَغُ مِنَ الْحَقِيقَةِ وَالتَّصْرِيحِ", "en": "the verdict.", "tr": "hüküm.", "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "فَهُوَ كَدَعْوَى الشَّيْءِ بِبَيِّنَةٍ", "en": "the reason, as a likening.", "tr": "sebep, bir benzetme olarak.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"}],
 "commonMistakes": [
  {"wrong": "«Kinâye, mecazdan daha beliğdir: çünkü hakikati de câiz bırakır»",
   "right": "«Telhîs ikisini birlikte hakikat ve tasrihin üstüne koyar; aralarında bir sıralama yapmaz»",
   "why": {"en": "The chapter's verdict has two sides only: majaz-and-kinaya above the plain, istiʿara above tashbih. Nothing in it ranks the kinaya against the majaz.", "tr": "Bâbın hükmü iki yönlüdür: mecaz-ve-kinâye hakikatin üstünde, istiâre teşbihin üstünde. Kinâyeyi mecaza karşı sıralayan bir şey yok."}},
  {"wrong": "«Teşbih de bir mecazdır, o hâlde hakikatten beliğdir»",
   "right": "«Teşbih hakikattir: her kelimesi kendi mânâsındadır; mecaz olan, benzetmeyi düşürmüş istiâredir»",
   "why": {"en": "In «Zayd is like a lion» no word leaves its meaning. Only when the likening is dropped and the lion asserted does the word move — and that move is the istiʿara's rank.", "tr": "«Zeyd arslan gibidir»de hiçbir kelime mânâsından ayrılmaz. Benzetme düşüp arslan iddia edilince kelime kayar — o kayış istiârenin rütbesidir."}}],
 "relatedNotes": ["kinaya", "farq-al-kinaya-wal-majaz", "haqiqa-majaz", "istiara", "tashbih", "kinaya-qariba-baida", "ilm-al-badi"]}
NOTE_D = {
 "id": "ilm-al-badi",
 "title": {"ar": "عِلْمُ الْبَدِيعِ — وُجُوهُ تَحْسِينِ الْكَلَامِ", "en": "The science of the badiʿ — the ways of beautifying speech", "tr": "Bedî' ilmi — sözü güzelleştirmenin vecihleri"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الفن الثالث: علم البديع"],
 "question": {
  "en": ["Has the speech already FITTED the situation (the maʿani) and made its meaning PLAIN (the bayan)? Only then does the badiʿ begin: it is the science of the ways of BEAUTIFYING speech after those two are observed.",
         "Is the beauty in the MEANING or in the WORDING? The figures of the badiʿ are two sorts: maʿnawi — the tibaq, the muqabala, the muraʿat al-nazir — and lafzi — the jinas, the sajʿ.",
         "Is the figure the point, or the ornament? The definition's «after» keeps the order: a figure that breaks the fit or clouds the meaning is no beauty."],
  "tr": ["Söz hâle UYMUŞ (meânî) ve mânâsı AÇIK mı (beyân)? Bedî' ancak o zaman başlar: bu ikisine riayetten sonra sözü GÜZELLEŞTİRMENİN vecihlerinin ilmidir.",
         "Güzellik MÂNÂDA mı LAFIZDA mı? Bedî' sanatları iki türlüdür: mânevî — tıbâk, mukabele, mürâât-ı nazîr — ve lafzî — cinas, seci.",
         "Sanat mı asıl, süs mü? Tarifteki «sonra» sırayı korur: uyumu bozan yahut mânâyı bulandıran sanat güzellik değildir."]},
 "plain": {
  "en": "The third art: the science of the ways of beautifying speech, once it already fits its situation and says its meaning plainly. Its figures are of the meaning or of the wording. The engine reads the first of them, the tibaq, off the sentence: two contraries gathered, or one verb denied and affirmed.",
  "tr": "Üçüncü fen: hâline uymuş ve mânâsını açıkça söylemiş sözü güzelleştirmenin vecihlerinin ilmi. Sanatları mânevî yahut lafzîdir. Motor ilkini, tıbâkı, cümleden okur: toplanmış iki zıt, yahut nefyedilip isbat edilmiş bir fiil."},
 "explanation": {
  "en": "THE THIRD ART is the SCIENCE OF THE BADIʿ: عِلْمٌ يُعْرَفُ بِهِ وُجُوهُ تَحْسِينِ الْكَلَامِ بَعْدَ رِعَايَةِ الْمُطَابَقَةِ وَوُضُوحِ الدَّلَالَةِ — a science by which are known the ways of BEAUTIFYING SPEECH, AFTER the FITTING of the speech to the situation (the matter of the first art, the maʿani) and the PLAINNESS of its meaning (the matter of the second, the bayan) have been observed. The order is the definition's point: the badiʿ comes last and adorns what is already right. Its ways are of TWO SORTS — of the MEANING (مَعْنَوِيّ: the tibaq, the muqabala, the muraʿat al-nazir, the irsad, the mushakala, the tawriya…) and of the WORDING (لَفْظِيّ: the jinas, the sajʿ, the radd al-ʿajuz…). The Talkhis opens the meaning-figures with the MUTABAQA. WHAT THE ENGINE CLAIMS: the badiʿ door opens with the BadiEngine, which reads the tibaq off the sentence — the tibaq of negation by the surface alone (one verb denied and the same verb affirmed), the tibaq of affirmation from a stored table of contraries — and grades itself against the authored frames. The rest of the figures are the chapters to come.",
  "tr": "ÜÇÜNCÜ FEN BEDÎ' İLMİDİR: عِلْمٌ يُعْرَفُ بِهِ وُجُوهُ تَحْسِينِ الْكَلَامِ بَعْدَ رِعَايَةِ الْمُطَابَقَةِ وَوُضُوحِ الدَّلَالَةِ — sözün hâle UYMASINA (birinci fennin, meânînin işi) ve mânâsının AÇIKLIĞINA (ikincinin, beyânın işi) riayetten SONRA sözü GÜZELLEŞTİRMENİN vecihlerinin kendisiyle bilindiği ilim. Sıra tarifin can noktasıdır: bedî' en son gelir ve zaten doğru olanı süsler. Vecihleri İKİ TÜRLÜDÜR — MÂNEVÎ (مَعْنَوِيّ: tıbâk, mukabele, mürâât-ı nazîr, irsâd, müşâkele, tevriye…) ve LAFZÎ (لَفْظِيّ: cinas, seci, reddü'l-acüz…). Telhîs mânevî sanatları MUTÂBAKATLA açar. MOTORUN İDDİASI: bedî' kapısı BadiEngine ile açılır; tıbâkı cümleden okur — selb tıbâkını yalnız yüzeyden (bir fiil nefyedilmiş ve aynı fiil isbat edilmiş), îcâb tıbâkını yerleşik bir zıtlar tablosundan — ve kendini müellif çerçevelerine karşı sınar. Kalan sanatlar gelecek bâblardır."},
 "examples": [
  {"ar": "عِلْمٌ يُعْرَفُ بِهِ وُجُوهُ تَحْسِينِ الْكَلَامِ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "وَهِيَ ضَرْبَانِ: مَعْنَوِيٌّ وَلَفْظِيٌّ", "en": "the two sorts.", "tr": "iki tür.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«Bedî', belâgatin kendisidir: sanat ne kadar çoksa söz o kadar beliğdir»",
   "right": "«Bedî' üçüncü fendir: mutâbakat ve vuzuhtan SONRA gelir; onları bozan sanat güzellik değildir»",
   "why": {"en": "The definition's «after» is a rule of rank. A figure bought at the price of fit or clarity is counted a fault by the same science.", "tr": "Tarifteki «sonra» bir rütbe kuralıdır. Uyum yahut açıklık pahasına alınan sanat, aynı ilimce kusur sayılır."}}],
 "relatedNotes": ["tibaq", "fadl-al-majaz-wal-kinaya", "muqabala", "ilm-al-bayan", "fasaha-balagha"]}
NOTE_Q = {
 "id": "tibaq",
 "title": {"ar": "الْمُطَابَقَةُ — الطِّبَاقُ وَالتَّضَادُّ؛ طِبَاقُ الْإِيجَابِ وَطِبَاقُ السَّلْبِ", "en": "The mutabaqa — the tibaq: two contraries in one sentence, by affirmation or by negation", "tr": "Mutâbakat — tıbâk: bir cümlede iki zıt, îcâbla yahut selble"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — المطابقة: الجمع بين متضادين"],
 "question": {
  "en": ["Are two CONTRARIES gathered in the sentence? أَيْقَاظًا … رُقُودٌ (18:18), يُحْيِي وَيُمِيتُ (2:258), لَهَا … وَعَلَيْهَا (2:286) — two nouns, two verbs, two particles; or across the kinds, مَيْتًا فَأَحْيَيْنَاهُ (6:122), a noun against a verb. That is the TIBAQ.",
         "Are both ends AFFIRMED? Then the tibaq of AFFIRMATION. Is one end the SAME word denied — لَا يَعْلَمُونَ … يَعْلَمُونَ (30:6-7), لَا تَخْشَوُا … وَاخْشَوْنِ (5:44)? Then the tibaq of NEGATION.",
         "Which of the two can the engine settle alone? The negation: the same lemma, once under لَا/مَا/لَمْ and once free, is a surface fact. The affirmation needs to know that «awake» and «asleep» are contraries — a stored table."],
  "tr": ["Cümlede iki ZIT toplanmış mı? أَيْقَاظًا … رُقُودٌ (Kehf 18:18), يُحْيِي وَيُمِيتُ (Bakara 2:258), لَهَا … وَعَلَيْهَا (Bakara 2:286) — iki isim, iki fiil, iki harf; yahut türler arası, مَيْتًا فَأَحْيَيْنَاهُ (En'âm 6:122), bir isim bir fiile karşı. TIBÂK budur.",
         "İki uç da İSBAT mı? Öyleyse ÎCÂB tıbâkı. Bir uç AYNI kelimenin nefyi mi — لَا يَعْلَمُونَ … يَعْلَمُونَ (Rûm 30:6-7), لَا تَخْشَوُا … وَاخْشَوْنِ (Mâide 5:44)? Öyleyse SELB tıbâkı.",
         "Motor ikisinden hangisini tek başına çözer? Selbi: aynı kök bir kere لَا/مَا/لَمْ altında, bir kere serbest — yüzey gerçeği. Îcâb, «uyanık» ile «uykuda»nın zıt olduğunu bilmeyi ister — yerleşik tablo."]},
 "plain": {
  "en": "The tibaq gathers two opposites (contraries) in one sentence — nouns, verbs, particles, or a noun against a verb. When both ends are affirmed it is a tibaq of affirmation; when one is the same word denied, of negation. The engine settles the negation from the surface and reads the affirmation off a table of contraries.",
  "tr": "Tıbâk bir cümlede iki zıddı toplar — isimler, fiiller, harfler yahut bir isimle bir fiil. İki uç da isbat edilmişse îcâb tıbâkı; biri aynı kelimenin nefyi ise selb tıbâkı. Motor selbi yüzeyden çözer, îcâbı bir zıtlar tablosundan okur."},
 "explanation": {
  "en": "The MUTABAQA is الْجَمْعُ بَيْنَ مُتَضَادَّيْنِ — the GATHERING OF TWO CONTRARIES, that is, of two OPPOSED MEANINGS, in one sentence; it is also called the TIBAQ and the TADADD. It comes with two words OF ONE KIND: two NOUNS — وَتَحْسَبُهُمْ أَيْقَاظًا وَهُمْ رُقُودٌ (18:18), where waking and sleep stand in the opposition of a state and its lack; two VERBS — يُحْيِي وَيُمِيتُ (2:258); two PARTICLES — لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا اكْتَسَبَتْ (2:286), the lam of benefit against the ʿala of harm; or with two words OF TWO KINDS — أَوَمَنْ كَانَ مَيْتًا فَأَحْيَيْنَاهُ (6:122), the noun «dead» against the verb «We gave life». It is of TWO KINDS: the tibaq of AFFIRMATION (طِبَاقُ الْإِيجَابِ), as in all of these, where both ends are affirmed; and the tibaq of NEGATION (طِبَاقُ السَّلْبِ) — وَلَكِنَّ أَكْثَرَ النَّاسِ لَا يَعْلَمُونَ يَعْلَمُونَ ظَاهِرًا مِنَ الْحَيَاةِ الدُّنْيَا (30:6-7), and فَلَا تَخْشَوُا النَّاسَ وَاخْشَوْنِ (5:44) — where one end is the SAME verb DENIED and the other the same verb affirmed. WHAT THE ENGINE CLAIMS: the BadiEngine reads the tibaq of NEGATION from the surface alone — one lemma appearing twice, once under لَا / مَا / لَمْ / لَنْ (or the la of prohibition) and once free — and names the pair with its class (verb, noun). The tibaq of AFFIRMATION it reads off a STORED table of contraries (life/death, waking/sleep, for/against, white/black…), keyed on lemmas; a pair outside the table is not found, and the engine says so. It grades both against the authored `badi` frames.",
  "tr": "MUTÂBAKAT الْجَمْعُ بَيْنَ مُتَضَادَّيْنِ'dir — bir cümlede İKİ ZIDDIN, yani iki KARŞIT MÂNÂNIN TOPLANMASI; ona TIBÂK ve TEZÂD da denir. BİR NEVDEN iki lafızla olur: iki İSİM — وَتَحْسَبُهُمْ أَيْقَاظًا وَهُمْ رُقُودٌ (Kehf 18:18), uyanıklıkla uyku adem-meleke tekabülünde; iki FİİL — يُحْيِي وَيُمِيتُ (Bakara 2:258); iki HARF — لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا اكْتَسَبَتْ (Bakara 2:286), fayda lâmı zarar alâsına karşı; yahut İKİ NEVDEN iki lafızla — أَوَمَنْ كَانَ مَيْتًا فَأَحْيَيْنَاهُ (En'âm 6:122), «ölü» ismi «dirilttik» fiiline karşı. İKİ KISIMDIR: bunların hepsindeki gibi iki ucun da isbat edildiği ÎCÂB tıbâkı (طِبَاقُ الْإِيجَابِ); ve bir ucun AYNI fiilin NEFYİ, öbürünün aynı fiilin isbatı olduğu SELB tıbâkı (طِبَاقُ السَّلْبِ) — وَلَكِنَّ أَكْثَرَ النَّاسِ لَا يَعْلَمُونَ يَعْلَمُونَ ظَاهِرًا مِنَ الْحَيَاةِ الدُّنْيَا (Rûm 30:6-7) ve فَلَا تَخْشَوُا النَّاسَ وَاخْشَوْنِ (Mâide 5:44). MOTORUN İDDİASI: BadiEngine SELB tıbâkını yalnız yüzeyden okur — bir kök iki kere, bir kere لَا / مَا / لَمْ / لَنْ (yahut nehiy lâsı) altında, bir kere serbest — ve çifti sınıfıyla (fiil, isim) adlandırır. ÎCÂB tıbâkını köklere anahtarlanmış YERLEŞİK bir zıtlar tablosundan (hayat/ölüm, uyanıklık/uyku, leh/aleyh, ak/kara…) okur; tablonun dışındaki çift bulunmaz ve motor bunu söyler. İkisini de müellifin `badi` çerçevelerine karşı sınar."},
 "examples": [
  {"ar": "وَتَحْسَبُهُمْ أَيْقَاظًا وَهُمْ رُقُودٌ", "en": "two nouns; affirmation.", "tr": "iki isim; îcâb.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "يُحْيِي وَيُمِيتُ", "en": "two verbs.", "tr": "iki fiil.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا اكْتَسَبَتْ", "en": "two particles.", "tr": "iki harf.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "أَوَمَنْ كَانَ مَيْتًا فَأَحْيَيْنَاهُ", "en": "a noun against a verb.", "tr": "isim fiile karşı.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "لَا يَعْلَمُونَ يَعْلَمُونَ", "en": "the tibaq of negation.", "tr": "selb tıbâkı.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"}],
 "commonMistakes": [
  {"wrong": "«لَا يَعْلَمُونَ يَعْلَمُونَ tekrardır, tıbâk değil»",
   "right": "«Selb tıbâkıdır: aynı fiil bir kere nefyedilmiş, bir kere isbat edilmiş — nefiy ile isbat iki zıttır»",
   "why": {"en": "The contraries need not be two words; denial and affirmation of one act are themselves opposed meanings. That is the whole of the second kind.", "tr": "Zıtların iki kelime olması gerekmez; bir fiilin nefyi ile isbatı kendileri karşıt mânâlardır. İkinci kısmın bütünü budur."}},
  {"wrong": "«İki zıt ancak iki isim yahut iki fiil arasında olur»",
   "right": "«Bir isimle bir fiil arasında da olur: مَيْتًا فَأَحْيَيْنَاهُ — iki nevden iki lafız»",
   "why": {"en": "The Talkhis lists the mixed case on purpose: what is gathered is two meanings, and the parts of speech that carry them may differ.", "tr": "Telhîs karışık hâli bilerek sayar: toplanan iki mânâdır; onları taşıyan kelime türleri farklı olabilir."}}],
 "relatedNotes": ["ilm-al-badi", "muqabala", "la-nafiya", "lam-jazim", "fadl-al-majaz-wal-kinaya"]}

ADD_EN = (" Chapter 57 (lines ~3941-3975, sahifa 136-137) carries the faṣl on the rank of the majaz and the kinaya, the "
          "definition of the science of the badiʿ and the mutabaqa: the definition (s4) and the ayat (s7 18:18, s8 2:258, s9 2:286, "
          "s10 6:122, s12 30:6-7, s13 5:44) are Arabic as the source prints them. s1-s3, s5-s6, s11 and the frames of the "
          "examples are RESTORATIONS, not quotations: the source carries those steps only in Ottoman-Turkish paraphrase, and the "
          "Arabic restores the matn's wording in the musannif's register; each is marked «restored» in its translation. s3 carries "
          "a tashbih frame; s7-s10, s12-s13 carry `badi` frames (the tibaq, its two words, its kind and class).")
ADD_TR = (" Elli yedinci bâb (satır ~3941-3975, sahife 136-137) mecaz ve kinâyenin rütbesi faslını, bedî' ilminin tarifini ve "
          "mutâbakatı taşır: tarif (s4) ve âyetler (s7 Kehf 18:18, s8 Bakara 2:258, s9 Bakara 2:286, s10 En'âm 6:122, s12 Rûm "
          "30:6-7, s13 Mâide 5:44) kaynağın bastığı Arapçadır. s1-s3, s5-s6, s11 ve örneklerin çerçeveleri ALINTI DEĞİL GERİ "
          "YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda "
          "geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. s3 bir teşbih çerçevesi; s7-s10, s12-s13 `badi` "
          "çerçevesi (tıbâk, iki kelimesi, kısmı ve sınıfı) taşır.")
write_out(57, S, TITLE, ADD_EN, ADD_TR, "3941-3975", GLOSS_ADD, notes=(NOTE_P, NOTE_D, NOTE_Q),
          related=(("kinaya", ["fadl-al-majaz-wal-kinaya"]), ("haqiqa-majaz", ["fadl-al-majaz-wal-kinaya"]), ("muqabala", ["tibaq", "ilm-al-badi"]), ("ilm-al-bayan", ["ilm-al-badi"])))
report(57, S, GLOSS_ADD, (NOTE_P, NOTE_D, NOTE_Q))
