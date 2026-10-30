# -*- coding: utf-8 -*-
"""Author chapter 58 of talkhis-al-miftah — the MUQABALA (two, three and four
against their counterparts, in order; Sakkaki's addition), MURAʿAT AL-NAZIR
(the tanasub, the tawfiq), what some call TASHABUH AL-ATRAF, and IHAM AL-TANASUB
(sahifa 137-138, lines ~3976-4025).

  RESTORED (the source carries the step only in Turkish): s1, s5-s7, s10, s12, s14;
          the frames of every example.
  As printed: the ayat (9:82, 92:5-10, 55:5, 6:103, 55:5-6) and the verses of
          Abu Dulama and al-Buhturi.

The frames are authored `badi` frames of the new kinds: muqabala (two ordered
lists), muraat-al-nazir (a set with its field), tashabuh-al-atraf (the pairs that
tie the end to the beginning), iham-al-tanasub (the set, the word, its meant and
its other sense) — and the tibaq of negation hidden inside 6:103.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import sarf_gen as _sg

M = "muqabala"; N = "muraat-al-nazir"; T = "tashabuh-al-atraf"; H = "iham-al-tanasub"
TITLE = {"ar": "الْمُقَابَلَةُ، وَمُرَاعَاةُ النَّظِيرِ، وَتَشَابُهُ الْأَطْرَافِ، وَإِيهَامُ التَّنَاسُبِ",
         "en": "The Muqabala; Muraʿat al-Nazir; Tashabuh al-Atraf; Iham al-Tanasub",
         "tr": "Mukâbele; Mürâât-ı Nazîr; Teşâbüh-i Etrâf; Îhâm-ı Tenâsüb"}
S = []
def nahwa(full="نَحْوَ", tag=M, punct=":"):
    return tok(full, "nahwa", "noun", [tag, "maful-fih"], ("الْوَاوُ عَاطِفَةٌ، وَ" if full.startswith("وَ") else "") + "نَحْوَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ إِلَى الْمِثَالِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوَ.",
               "«such as» — a zarf annexed to the example; the khabar of a dropped «that is».", "«… gibi» — örneğe izâfe edilmiş zarf; hazfedilmiş «o»nun haberi.",
               segments=([seg("وَ", "wa", "conj"), seg("نَحْوَ", "nahwa", "noun")] if full.startswith("وَ") else None), punct=punct)
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)

# ----------- s1 — the muqabala defined (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the MUQABALA: that two agreeing meanings, or more, are brought, and then what COUNTERS them, IN ORDER." + R_EN,
 "tr": "Onlardan biri MUKÂBELEDİR: birbirine uygun iki yahut daha çok mânâ getirilir, sonra SIRASIYLA onların MUKÂBİLİ getirilir." + R_TR},
 "tokens": [
  tok("وَمِنْهَا","min","part",[M, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — مِنَ الْوُجُوهِ الْمَعْنَوِيَّةِ.", "«and among them» — a fronted khabar: among the figures of meaning.", "«ve onlardan» — öne alınmış haber: mânevî sanatlardan.",
      segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("الْمُقَابَلَةُ","muqabala","noun",[M, "mubtada-khabar", "masdar", "form-iii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ قَابَلَ.", "«the muqabala» — the delayed mubtada; masdar of قَابَلَ.", "«mukâbele» — sona kalmış mübtedâ; قَابَلَ'nin masdarı.", punct="،"),
  tok("وَهِيَ","hiya","pron",[M, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("أَنْ","an","part",[M, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the interpreted masdar is the khabar.", "«… -mesi» — masdariyye en; müevvel masdar haber."),
  tok("يُؤْتَى","ata","verb",[M, "an-masdariyya", "naib-al-fail", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«are brought» — the passive; its deputy doer is the phrase after it.", "«getirilir» — meçhûl; nâib-i fâili sonraki ibare."),
  tok("بِمَعْنَيَيْنِ","mana","noun",[M, "huruf-jarr", "al-muthanna"], "جَارٌّ وَمَجْرُورٌ بِالْيَاءِ — مُثَنَّى مَعْنًى.", "«two meanings» — the dual of مَعْنًى.", "«iki mânâ» — مَعْنًى'nın tesniyesi.",
      segments=[seg("بِ","bi","part"), seg("مَعْنَيَيْنِ","mana","noun")]),
  tok("مُتَوَافِقَيْنِ","mutawafiq","noun",[M, "naat-sifa", "al-muthanna", "ism-fail", "form-vi-verbs"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ — اسْمُ فَاعِلِ تَوَافَقَ.", "«agreeing» — a na't; ism fa'il of تَوَافَقَ.", "«birbirine uygun» — na't; تَوَافَقَ'nin ism-i fâili."),
  tok("أَوْ","aw","conj",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("أَكْثَرَ","akthar","noun",[M, "atf-nasaq", "ism-tafdil", "mamnu-min-sarf"], "مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more» — joined; jarr by a fatha, being diptote.", "«daha çok» — matuf; gayr-i munsarif olduğu için fetha ile mecrur.", punct="،"),
  tok("ثُمَّ","thumma","conj",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then» — the waw of order with a gap.", "«sonra» — tertip ve terâhî için atıf harfi."),
  tok("بِمَا","ma-mawsula","pron",[M, "huruf-jarr", "ism-mawsul"], "جَارٌّ وَمَجْرُورٌ مَعْطُوفٌ عَلَى بِمَعْنَيَيْنِ — مَا مَوْصُولَةٌ.", "«what» — joined onto «two meanings»; the relative ma.", "«… şey» — «iki mânâ»ya matuf; mevsûle mâ.",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُقَابِلُ","qabala","verb",[M, "ism-mawsul", "fail", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مِنَ الْمُفَاعَلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ صِلَةٌ.", "«counters» — Form III; the doer «it» concealed; the sila.", "«mukâbil olur» — III. bâb; fâil gizli «o»; sıla."),
  tok("ذَلِكَ","dhalika","pron",[M, "maful-bihi", "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«onu» — mef'ûl."),
  tok("عَلَى","ala","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  tok("التَّرْتِيبِ","tartib","noun",[M, "huruf-jarr", "masdar", "form-ii-verbs"], "مَجْرُورٌ — مَصْدَرُ رَتَّبَ: الْأَوَّلُ لِلْأَوَّلِ وَالثَّانِي لِلثَّانِي.", "«order» — masdar of رَتَّبَ: the first to the first, the second to the second.", "«tertip» — رَتَّبَ'nin masdarı: birinci birinciye, ikinci ikinciye.", punct=".")]})

# ----------- s2 — two against two: 9:82
S.append({"id": "s2", "translation": {
 "en": "The example of two: «So let them LAUGH a LITTLE and WEEP MUCH» (9:82)." + R_EN,
 "tr": "İkinin örneği: «Artık AZ GÜLSÜNLER, ÇOK AĞLASINLAR» (Tevbe 9:82)." + R_TR},
 "badi": [{"kind": "muqabala", "first": [2, 3], "second": [4, 5]}, bd("tibaq", [2, 4], sub="ijab", cls="fil"), bd("tibaq", [3, 5], sub="ijab", cls="ism")],
 "tokens": [
  tok("مِثَالُ","mithal","noun",[M, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the example of» — the mubtada; a mudaf.", "«örneği» — mübtedâ; muzâf."),
  tok("الِاثْنَيْنِ","ithnan","noun",[M, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُلْحَقٌ بِالْمُثَنَّى.", "«two» — mudaf ilayh; declined like a dual.", "«iki» — muzâfun ileyh; tesniyeye mülhak.", punct=":"),
  tok("فَلْيَضْحَكُوا","dahika","verb",[M, "lam-amr", "afal-khamsa", "fail"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لَامُ الْأَمْرِ، وَيَضْحَكُوا فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ؛ وَالْجُمْلَةُ خَبَرٌ — الْأَوَّلُ مِنَ الطَّرَفِ الْأَوَّلِ.", "«so let them laugh» — the lam of command; jazm by dropping the nun; the first of the first side.", "«artık gülsünler» — emir lâmı; nûnun hazfiyle meczûm; birinci tarafın birincisi.",
      segments=[seg("فَ","fa","conj"), seg("لْ","lam-amr","part"), seg("يَضْحَكُ","dahika","verb"), seg("وا","pron-3mp","pron")]),
  tok("قَلِيلًا","qalil","noun",[M, "maful-mutlaq", "sifa-mushabbaha"], "نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ مَنْصُوبٌ — ضَحِكًا قَلِيلًا؛ الثَّانِي مِنَ الطَّرَفِ الْأَوَّلِ.", "«a little» — a na't of a dropped masdar: «a little laughing»; the second of the first side.", "«az» — hazfedilmiş masdarın na'tı: «az bir gülme»; birinci tarafın ikincisi."),
  wa_conj("وَلْيَبْكُوا","baka","verb",[M, "lam-amr", "afal-khamsa", "naqis-verbs", "fail"], "اللَّامُ لَامُ الْأَمْرِ، وَيَبْكُوا فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — الْمُقَابِلُ الْأَوَّلُ: الْبُكَاءُ ضِدُّ الضَّحِكِ.", "«and let them weep» — the first counterpart: weeping against laughing.", "«ve ağlasınlar» — birinci mukâbil: ağlamak gülmenin zıddı.", pron=("وا","pron-3mp")),
  tok("كَثِيرًا","kathir","noun",[M, "maful-mutlaq", "sifa-mushabbaha"], "نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ مَنْصُوبٌ — الْمُقَابِلُ الثَّانِي: الْكَثِيرُ ضِدُّ الْقَلِيلِ، عَلَى التَّرْتِيبِ.", "«much» — the second counterpart: much against little, in order.", "«çok» — ikinci mukâbil: çok azın zıddı, sırasıyla.", punct=".")]})
# fix the segment split of وَلْيَبْكُوا: waw + lam + verb + pronoun
S[-1]["tokens"][4]["segments"] = [seg("وَ","wa","conj"), seg("لْ","lam-amr","part"), seg("يَبْكُ","baka","verb"), seg("وا","pron-3mp","pron")]

# ----------- s3 — three against three: Abu Dulama
S.append({"id": "s3", "translation": {
 "en": "And of three, the verse of Abu Dulama: «How FINE are RELIGION and this WORLD when they are joined — and how UGLY are UNBELIEF and BANKRUPTCY in a man!»" + R_EN,
 "tr": "Üçün örneği Ebû Dülâme'nin beyti: «DİN ile DÜNYA bir araya gelince ne GÜZELDİR — KÜFÜR ile İFLÂS bir adamda ne ÇİRKİNDİR!»" + R_TR},
 "badi": [{"kind": "muqabala", "first": [6, 7, 8], "second": [11, 12, 13]}, bd("tibaq", [6, 11], sub="ijab", cls="fil"), bd("tibaq", [7, 12], sub="ijab", cls="ism")],
 "tokens": [
  wa_conj("وَمِثَالُ","mithal","noun",[M, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "مِثَالُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the example of» — the mubtada.", "«ve örneği» — mübtedâ."),
  tok("الثَّلَاثَةِ","thalatha","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«three» — mudaf ilayh.", "«üç» — muzâfun ileyh."),
  tok("قَوْلُ","qawl","noun",[M, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the saying of» — the khabar; a mudaf.", "«sözü» — haber; muzâf."),
  tok("أَبِي","ab","noun",[M, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — one of the five nouns, jarr by the ya.", "«Ebû» — esmâ-i hamseden, yâ ile mecrur."),
  tok("دُلَامَةَ","dulama","noun",[M, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dulama» — a diptote proper name.", "«Dülâme» — gayr-i munsarif özel ad.", punct=":"),
  tok("مَا","ma-taajjub","part",[M, "mubtada-khabar", "anwa-ma"], "مَا التَّعَجُّبِيَّةُ: نَكِرَةٌ تَامَّةٌ بِمَعْنَى شَيْءٍ، مُبْتَدَأٌ.", "«how…!» — the ma of wonder, a mubtada meaning «something».", "«ne …!» — taaccüb mâsı, «bir şey» mânâsında mübtedâ."),
  tok("أَحْسَنَ","ahsana","verb",[M, "mubtada-khabar", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ التَّعَجُّبِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، يَعُودُ عَلَى مَا؛ وَالْجُمْلَةُ خَبَرٌ — الْأَوَّلُ مِنَ الثَّلَاثَةِ.", "«how fine!» — the frozen verb of wonder; its doer «it» goes back to ma; the first of the three.", "«ne güzel!» — donmuş taaccüb fiili; fâili «o», mâya râci; üçün birincisi."),
  tok("الدِّينَ","din","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الثَّانِي.", "«religion» — the object; the second.", "«din» — mef'ûl; ikincisi."),
  wa_conj("وَالدُّنْيَا","dunya","noun",[M, "atf-nasaq", "ism-maqsur-manqus"], "الدُّنْيَا مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — الثَّالِثُ.", "«and this world» — joined; the third.", "«ve dünya» — matuf; üçüncüsü."),
  tok("إِذَا","idha","part",[M, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ.", "«when» — the zarf of the future.", "«… -ince» — istikbal zarfı."),
  tok("اجْتَمَعَا","ijtamaa","verb",[M, "idha-shartiyya", "fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مِنَ الِافْتِعَالِ، وَالْأَلِفُ فَاعِلٌ — ضَمِيرُ الِاثْنَيْنِ.", "«they are joined» — Form VIII; the alif is the doer, «the two».", "«bir araya gelirler» — VIII. bâb; elif fâil, «ikisi».",
      segments=[seg("اجْتَمَعَ","ijtamaa","verb"), seg("ا","pron-3d","pron")], punct="*"),
  wa_conj("وَأَقْبَحَ","aqbaha","verb",[M, "atf-nasaq", "maful-bihi", "form-iv-verbs"], "أَقْبَحَ فِعْلُ تَعَجُّبٍ مَعْطُوفٌ عَلَى أَحْسَنَ — مَا أَقْبَحَ؛ الْمُقَابِلُ الْأَوَّلُ: الْقُبْحُ ضِدُّ الْحُسْنِ.", "«and how ugly!» — joined onto «how fine»: the first counterpart, ugliness against beauty.", "«ve ne çirkin!» — «ne güzel»e matuf: birinci mukâbil, çirkinlik güzelliğin zıddı."),
  tok("الْكُفْرَ","kufr","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُقَابِلُ الثَّانِي: الْكُفْرُ ضِدُّ الدِّينِ.", "«unbelief» — the second counterpart, against religion.", "«küfür» — ikinci mukâbil, dinin zıddı."),
  wa_conj("وَالْإِفْلَاسَ","iflas","noun",[M, "atf-nasaq", "masdar", "form-iv-verbs"], "الْإِفْلَاسَ مَعْطُوفٌ مَنْصُوبٌ — الْمُقَابِلُ الثَّالِثُ: الْإِفْلَاسُ ضِدُّ الدُّنْيَا، أَيْ: الْمَالِ.", "«and bankruptcy» — the third counterpart, against this world, that is, wealth.", "«ve iflâs» — üçüncü mukâbil, dünyanın yani malın zıddı."),
  tok("بِالرَّجُلِ","rajul","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَقْبَحَ.", "«in a man» — attached to «how ugly».", "«bir adamda» — «ne çirkin»e müteallik.",
      segments=[seg("بِ","bi","part"), seg("الرَّجُلِ","rajul","noun")], punct=".")]})

# ----------- s4 — four against four: 92:5-10
S.append({"id": "s4", "translation": {
 "en": "And of four: «As for him who GIVES and is GOD-FEARING and AFFIRMS the best — We shall ease him to EASE; and as for him who WITHHOLDS and thinks himself SELF-SUFFICIENT and DENIES the best — We shall ease him to HARDSHIP» (92:5-10)." + R_EN,
 "tr": "Dördün örneği: «Kim VERİR, SAKINIR ve en güzeli TASDİK EDERSE, ona en KOLAYI kolaylaştırırız; kim CİMRİLİK EDER, kendini MÜSTAĞNİ GÖRÜR ve en güzeli YALANLARSA, ona en GÜÇ olanı kolaylaştırırız» (Leyl 92:5-10)." + R_TR},
 "badi": [{"kind": "muqabala", "first": [4, 5, 6, 9], "second": [12, 13, 14, 17]},
          bd("tibaq", [4, 12], sub="ijab", cls="fil"), bd("tibaq", [6, 14], sub="ijab", cls="fil"), bd("tibaq", [9, 17], sub="ijab", cls="ism")],
 "tokens": [
  wa_conj("وَمِثَالُ","mithal","noun",[M, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "مِثَالُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the example of».", "«ve örneği»."),
  tok("الْأَرْبَعَةِ","arbaa","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«four».", "«dört».", punct=":"),
  tok("فَأَمَّا","amma","part",[M, "amma-tafsiliyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — amma of detail.", "«… -e gelince» — tafsîl emmâsı.",
      segments=[seg("فَ","fa","conj"), seg("أَمَّا","amma","part")]),
  tok("مَنْ","man-mawsula","pron",[M, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«him who» — the relative as mubtada.", "«kim» — mevsûl, mübtedâ."),
  tok("أَعْطَى","ata-give","verb",[M, "ism-mawsul", "fail", "form-iv-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مِنَ الرَّابِعِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ صِلَةٌ — الْأَوَّلُ.", "«gives» — Form IV; the doer concealed; the sila; the first.", "«verir» — IV. bâb; fâil gizli; sıla; birincisi."),
  wa_conj("وَاتَّقَى","ittaqa","verb",[M, "atf-nasaq", "form-viii-verbs", "naqis-verbs"], "اتَّقَى فِعْلٌ مَاضٍ مَعْطُوفٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الثَّانِي.", "«and is god-fearing» — joined; the second.", "«ve sakınır» — matuf; ikincisi."),
  wa_conj("وَصَدَّقَ","saddaqa","verb",[M, "atf-nasaq", "form-ii-verbs"], "صَدَّقَ فِعْلٌ مَاضٍ مَعْطُوفٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الثَّالِثُ.", "«and affirms» — joined; the third.", "«ve tasdik eder» — matuf; üçüncüsü."),
  tok("بِالْحُسْنَى","husna","noun",[M, "huruf-jarr", "ism-tafdil", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مُؤَنَّثُ الْأَحْسَنِ: كَلِمَةُ التَّوْحِيدِ أَوِ الْجَنَّةُ.", "«the best» — feminine of أَحْسَن: the word of unity, or the Garden.", "«en güzeli» — أَحْسَن'in müennesi: kelime-i tevhid yahut cennet.",
      segments=[seg("بِ","bi","part"), seg("الْحُسْنَى","husna","noun")]),
  tok("فَسَنُيَسِّرُهُ","yassara","verb",[M, "fa-khabar-mubtada", "maful-bihi", "form-ii-verbs", "mudari-marfu"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَالسِّينُ لِلِاسْتِقْبَالِ، وَنُيَسِّرُ فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — نَحْنُ، وَالْهَاءُ مَفْعُولٌ بِهِ؛ وَالْجُمْلَةُ خَبَرُ مَنْ.", "«We shall ease him» — the fa of amma's answer; the sin of the future; «We» concealed; the khabar of «him who».", "«onu kolaylaştırırız» — emmânın cevap fâsı; istikbal sîni; «biz» gizli; «kim»in haberi.",
      segments=[seg("فَ","fa","conj"), seg("سَ","sa-istiqbal","part"), seg("نُيَسِّرُ","yassara","verb"), seg("هُ","pron-3ms","pron")]),
  tok("لِلْيُسْرَى","yusra","noun",[M, "huruf-jarr", "ism-tafdil", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ — مُؤَنَّثُ الْأَيْسَرِ: الْخَصْلَةُ الْيُسْرَى؛ الرَّابِعُ.", "«to ease» — feminine of أَيْسَر: the easy way; the fourth.", "«en kolaya» — أَيْسَر'in müennesi: kolay yol; dördüncüsü.",
      segments=[seg("لِ","li","part"), seg("الْيُسْرَى","yusra","noun")], punct="،"),
  wa_conj("وَأَمَّا","amma","part",[M, "atf-nasaq", "amma-tafsiliyya"], "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for».", "«ve … -e gelince»."),
  tok("مَنْ","man-mawsula","pron",[M, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«him who».", "«kim»."),
  tok("بَخِلَ","bakhila","verb",[M, "ism-mawsul", "fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ؛ صِلَةٌ — الْمُقَابِلُ الْأَوَّلُ: الْبُخْلُ ضِدُّ الْإِعْطَاءِ.", "«withholds» — the first counterpart: withholding against giving.", "«cimrilik eder» — birinci mukâbil: cimrilik vermenin zıddı."),
  wa_conj("وَاسْتَغْنَى","istaghna","verb",[M, "atf-nasaq", "form-x-verbs", "naqis-verbs"], "اسْتَغْنَى فِعْلٌ مَاضٍ مِنَ الِاسْتِفْعَالِ مَعْطُوفٌ — الْمُقَابِلُ الثَّانِي: الِاسْتِغْنَاءُ ضِدُّ الِاتِّقَاءِ.", "«and thinks himself self-sufficient» — the second counterpart, against fearing God.", "«ve müstağni görür» — ikinci mukâbil, sakınmanın zıddı."),
  wa_conj("وَكَذَّبَ","kadhdhaba","verb",[M, "atf-nasaq", "form-ii-verbs"], "كَذَّبَ فِعْلٌ مَاضٍ مَعْطُوفٌ — الْمُقَابِلُ الثَّالِثُ: التَّكْذِيبُ ضِدُّ التَّصْدِيقِ.", "«and denies» — the third counterpart, against affirming.", "«ve yalanlar» — üçüncü mukâbil, tasdikin zıddı."),
  tok("بِالْحُسْنَى","husna","noun",[M, "huruf-jarr", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ.", "«the best».", "«en güzeli».",
      segments=[seg("بِ","bi","part"), seg("الْحُسْنَى","husna","noun")]),
  tok("فَسَنُيَسِّرُهُ","yassara","verb",[M, "fa-khabar-mubtada", "maful-bihi", "form-ii-verbs", "mudari-marfu"], "الْفَاءُ فِي جَوَابِ أَمَّا، وَالْجُمْلَةُ خَبَرُ مَنْ — التَّيْسِيرُ مُشْتَرَكٌ بَيْنَ الطَّرَفَيْنِ.", "«We shall ease him» — the khabar; the easing is shared by both sides.", "«onu kolaylaştırırız» — haber; kolaylaştırma iki tarafta ortak.",
      segments=[seg("فَ","fa","conj"), seg("سَ","sa-istiqbal","part"), seg("نُيَسِّرُ","yassara","verb"), seg("هُ","pron-3ms","pron")]),
  tok("لِلْعُسْرَى","usra","noun",[M, "huruf-jarr", "ism-tafdil", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ — مُؤَنَّثُ الْأَعْسَرِ: الْخَصْلَةُ الْعُسْرَى؛ الْمُقَابِلُ الرَّابِعُ: الْعُسْرَى ضِدُّ الْيُسْرَى.", "«to hardship» — feminine of أَعْسَر; the fourth counterpart, against ease.", "«en güç olana» — أَعْسَر'in müennesi; dördüncü mukâbil, kolayın zıddı.",
      segments=[seg("لِ","li","part"), seg("الْعُسْرَى","usra","noun")], punct=".")]})

# ----------- s5 — Sakkaki's addition (RESTORED matn)
S.append({"id": "s5", "translation": {
 "en": "Al-Sakkaki ADDED to it: that when a thing is made a CONDITION here, its CONTRARY is made the condition there." + R_EN,
 "tr": "Sekkâkî buna ŞUNU EKLEDİ: burada bir şey ŞART kılındığında orada onun ZIDDI şart kılınır." + R_TR},
 "tokens": [
  wa_conj("وَزَادَ","zada","verb",[M, "atf-nasaq", "fail", "hollow-verbs"], "زَادَ فِعْلٌ مَاضٍ أَجْوَفُ.", "«and added» — the hollow verb.", "«ve ekledi» — ecvef fiil."),
  tok("السَّكَّاكِيُّ","sakkaki","noun",[M, "fail", "ism-mansub"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Sakkaki» — the doer.", "«Sekkâkî» — fâil."),
  tok("فِيهَا","fi","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي الْمُقَابَلَةِ.", "«to it» — to the muqabala.", "«ona» — mukâbeleye.",
      segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("أَنَّهُ","anna","part",[M, "inna-wa-akhawatuha", "maful-bihi"], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ اسْمُهُ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ زَادَ.", "«that» — anna with the pronoun of the matter; the interpreted masdar is the object of «added».", "«şunu» — enne ve şe'n zamiri; müevvel masdar «ekledi»nin mef'ûlü.",
      segments=[seg("أَنَّ","anna","part"), seg("هُ","pron-3ms","pron")]),
  tok("إِذَا","idha","part",[M, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the zarf that carries a condition.", "«… -ığında» — şart mânâsı taşıyan zarf."),
  tok("شُرِطَ","sharata","verb",[M, "idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«is made a condition» — the passive; the shart's verb.", "«şart kılınır» — meçhûl; şart fiili."),
  tok("هُنَا","huna","noun",[M, "maful-fih", "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ الْقَرِيبِ، ظَرْفٌ — فِي الطَّرَفِ الْأَوَّلِ.", "«here» — the demonstrative of near place; a zarf: on the first side.", "«burada» — yakın mekân işareti; zarf: birinci tarafta."),
  tok("أَمْرٌ","amr","noun",[M, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a thing» — the deputy doer.", "«bir şey» — nâib-i fâil."),
  tok("شُرِطَ","sharata","verb",[M, "idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ.", "«is made the condition» — the answer.", "«şart kılınır» — cevap."),
  tok("هُنَاكَ","hunaka","noun",[M, "maful-fih", "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ، ظَرْفٌ — فِي الطَّرَفِ الثَّانِي.", "«there» — of far place: on the second side.", "«orada» — uzak mekân işareti: ikinci tarafta."),
  tok("ضِدُّهُ","didd","noun",[M, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its contrary» — the deputy doer.", "«onun zıddı» — nâib-i fâil.",
      segments=[seg("ضِدُّ","didd","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s6 — as in the aya (RESTORED matn)
S.append({"id": "s6", "translation": {
 "en": "As in the aya: since EASING was made shared among GIVING, FEARING and AFFIRMING, its contrary, HARDENING, was made shared among their contraries: WITHHOLDING, SELF-SUFFICIENCY and DENIAL." + R_EN,
 "tr": "Âyette olduğu gibi: KOLAYLAŞTIRMA, VERME, SAKINMA ve TASDİK arasında ortak kılınınca onun zıddı olan GÜÇLEŞTİRME de onların zıtları CİMRİLİK, İSTİĞNÂ ve YALANLAMA arasında ortak kılındı." + R_TR},
 "badi": [{"kind": "muqabala", "first": [6, 7, 8], "second": [13, 14, 15]}, bd("tibaq", [3, 10], sub="ijab", cls="ism")],
 "tokens": [
  tok("كَمَا","ka","part",[M, "huruf-jarr"], "الْكَافُ جَارَّةٌ، وَمَا مَصْدَرِيَّةٌ.", "«as».", "«… gibi».",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْآيَةِ","aya","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the aya».", "«âyet».", punct=":"),
  tok("لَمَّا","lamma","part",[M, "maful-fih"], "ظَرْفٌ بِمَعْنَى حِينَ، فِيهِ مَعْنَى الشَّرْطِ.", "«since / when» — the zarf of «at the time that», with a condition in it.", "«… -ınca» — «vakit» mânâsında, şart mânâlı zarf."),
  tok("جُعِلَ","jaala","verb",[M, "naib-al-fail", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مِنْ أَخَوَاتِ ظَنَّ — يَنْصِبُ مَفْعُولَيْنِ، أَوَّلُهُمَا نَائِبُ الْفَاعِلِ.", "«was made» — the passive of a two-object verb; its first object is now the deputy doer.", "«kılındı» — iki mef'ûllü fiilin meçhûlü; birinci mef'ûlü nâib-i fâil."),
  tok("التَّيْسِيرُ","taysir","noun",[M, "naib-al-fail", "masdar", "form-ii-verbs"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — مَصْدَرُ يَسَّرَ؛ أَحَدُ طَرَفَيِ الطِّبَاقِ.", "«easing» — the deputy doer; masdar of يَسَّرَ; one end of a tibaq.", "«kolaylaştırma» — nâib-i fâil; يَسَّرَ'nin masdarı; tıbâkın bir ucu."),
  tok("مُشْتَرَكًا","mushtarak","noun",[M, "mafulayn", "ism-maful", "form-viii-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ مَفْعُولِ اشْتَرَكَ.", "«shared» — the second object; ism maf'ul of اشْتَرَكَ.", "«ortak» — ikinci mef'ûl; اشْتَرَكَ'nin ism-i mef'ûlü."),
  tok("بَيْنَ","bayna","noun",[M, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«among».", "«arasında»."),
  tok("الْإِعْطَاءِ","ita","noun",[M, "idafa-definiteness", "masdar", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ أَعْطَى؛ الْأَوَّلُ.", "«giving» — masdar of أَعْطَى; the first.", "«verme» — أَعْطَى'nın masdarı; birincisi."),
  wa_conj("وَالِاتِّقَاءِ","ittiqa","noun",[M, "atf-nasaq", "masdar", "form-viii-verbs"], "الِاتِّقَاءِ مَعْطُوفٌ مَجْرُورٌ — الثَّانِي.", "«fearing» — the second.", "«sakınma» — ikincisi."),
  wa_conj("وَالتَّصْدِيقِ","tasdiq","noun",[M, "atf-nasaq", "masdar", "form-ii-verbs"], "التَّصْدِيقِ مَعْطُوفٌ مَجْرُورٌ — الثَّالِثُ.", "«affirming» — the third.", "«tasdik» — üçüncüsü.", punct="،"),
  tok("جُعِلَ","jaala","verb",[M, "naib-al-fail", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ لَمَّا.", "«was made» — the answer of «since».", "«kılındı» — lemmânın cevabı."),
  tok("ضِدُّهُ","didd","noun",[M, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«its contrary» — the deputy doer.", "«onun zıddı» — nâib-i fâil.",
      segments=[seg("ضِدُّ","didd","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("التَّعْسِيرُ","tasir","noun",[M, "badal", "masdar", "form-ii-verbs"], "بَدَلٌ مِنْ ضِدُّهُ مَرْفُوعٌ — مَصْدَرُ عَسَّرَ؛ الطَّرَفُ الْآخَرُ.", "«hardening» — badal of «its contrary»; masdar of عَسَّرَ; the other end of the tibaq.", "«güçleştirme» — «zıddı»nın bedeli; عَسَّرَ'nin masdarı; tıbâkın öbür ucu.", punct="،"),
  tok("مُشْتَرَكًا","mushtarak","noun",[M, "mafulayn", "ism-maful"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«shared».", "«ortak»."),
  tok("بَيْنَ","bayna","noun",[M, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«among».", "«arasında»."),
  tok("أَضْدَادِهَا","didd","noun",[M, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — جَمْعُ ضِدٍّ.", "«their contraries» — plural of ضِدّ.", "«onların zıtları» — ضِدّ'in çoğulu.",
      segments=[seg("أَضْدَادِ","didd","noun"), seg("هَا","pron-3fs","pron")], punct=":"),
  tok("الْبُخْلِ","bukhl","noun",[M, "badal", "masdar"], "بَدَلُ تَفْصِيلٍ مَجْرُورٌ — الْمُقَابِلُ الْأَوَّلُ.", "«withholding» — badal of detail; the first counterpart.", "«cimrilik» — tafsîl bedeli; birinci mukâbil."),
  wa_conj("وَالِاسْتِغْنَاءِ","istighna","noun",[M, "atf-nasaq", "masdar", "form-x-verbs"], "الِاسْتِغْنَاءِ مَعْطُوفٌ مَجْرُورٌ — الثَّانِي.", "«self-sufficiency» — the second.", "«istiğnâ» — ikincisi."),
  wa_conj("وَالتَّكْذِيبِ","takdhib","noun",[M, "atf-nasaq", "masdar", "form-ii-verbs"], "التَّكْذِيبِ مَعْطُوفٌ مَجْرُورٌ — الثَّالِثُ.", "«denial» — the third.", "«yalanlama» — üçüncüsü.", punct=".")]})
# the muqabala of s6 is between the masdars (8,9,10) and (18,19,20); the tibaq between 5 and 13
S[-1]["badi"] = [{"kind": "muqabala", "first": [8, 9, 10], "second": [17, 18, 19]}, bd("tibaq", [5, 13], sub="ijab", cls="ism")]

# ----------- s7 — muraʿat al-nazir defined (RESTORED matn)
S.append({"id": "s7", "translation": {
 "en": "Among them is MURAʿAT AL-NAZIR: the gathering of a thing and what SUITS it — not by contrariety; it is also called the TANASUB and the TAWFIQ." + R_EN,
 "tr": "Onlardan biri MÜRÂÂT-I NAZÎRDİR: bir şeyi zıddıyla değil, ona UYGUN OLANLA bir araya getirmek; ona TENÂSÜB ve TEVFÎK de denir." + R_TR},
 "tokens": [
  wa_conj("وَمِنْهَا","min","part",[N, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "مِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them» — a fronted khabar.", "«ve onlardan» — öne alınmış haber.", pron=("هَا","pron-3fs")),
  tok("مُرَاعَاةُ","muraat","noun",[N, "mubtada-khabar", "idafa-definiteness", "masdar", "form-iii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ رَاعَى.", "«the observing of» — the delayed mubtada; masdar of رَاعَى.", "«riayet etmek» — sona kalmış mübtedâ; رَاعَى'nın masdarı."),
  tok("النَّظِيرِ","nazir","noun",[N, "idafa-definiteness", "sifa-mushabbaha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — النَّظِيرُ: الْمِثْلُ وَالْمُنَاسِبُ.", "«the like» — mudaf ilayh: the peer, what suits.", "«nazîr» — muzâfun ileyh: benzer, münasip olan.", punct="،"),
  wa_conj("وَهِيَ","hiya","pron",[N, "mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it is».", "«ve o»."),
  tok("جَمْعُ","jam","noun",[N, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the gathering of» — the khabar.", "«bir araya getirmek» — haber."),
  tok("أَمْرٍ","amr","noun",[N, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyi»."),
  wa_conj("وَمَا","ma-mawsula","pron",[N, "atf-nasaq", "ism-mawsul"], "مَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ.", "«and what» — the relative, joined.", "«ve … şeyi» — mevsûl, matuf."),
  tok("يُنَاسِبُهُ","nasaba","verb",[N, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مِنَ الْمُفَاعَلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ؛ صِلَةٌ.", "«suits it» — Form III; the doer concealed; the sila.", "«ona uyar» — III. bâb; fâil gizli; sıla.",
      segments=[seg("يُنَاسِبُ","nasaba","verb"), seg("هُ","pron-3ms","pron")]),
  tok("لَا","la-nafiya","part",[N], "حَرْفُ نَفْيٍ — عَاطِفَةٌ لِلْإِخْرَاجِ.", "«not» — excludes the other way.", "«değil» — öbür yolu dışarıda bırakır."),
  tok("بِالتَّضَادِّ","tadadd","noun",[N, "huruf-jarr", "masdar", "form-vi-verbs"], "جَارٌّ وَمَجْرُورٌ — لَا عَلَى وَجْهِ الطِّبَاقِ.", "«by contrariety» — not in the tibaq's way.", "«tezâd ile» — tıbâk yoluyla değil.",
      segments=[seg("بِ","bi","part"), seg("التَّضَادِّ","tadadd","noun")], punct="،"),
  wa_conj("وَتُسَمَّى","samma","verb",[N, "atf-nasaq", "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "تُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — هِيَ.", "«and it is called» — the passive.", "«ve denir» — meçhûl."),
  tok("التَّنَاسُبَ","tanasub","noun",[N, "mafulayn", "masdar", "form-vi-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«the tanasub» — the second object.", "«tenâsüb» — ikinci mef'ûl."),
  wa_conj("وَالتَّوْفِيقَ","tawfiq","noun",[N, "atf-nasaq", "masdar", "form-ii-verbs"], "التَّوْفِيقَ مَعْطُوفٌ مَنْصُوبٌ.", "«and the tawfiq» — joined.", "«ve tevfîk» — matuf.", punct=".")]})

# ----------- s8 — 55:5
S.append({"id": "s8", "translation": {
 "en": "Such as: «The SUN and the MOON are by reckoning» (55:5)." + R_EN,
 "tr": "«GÜNEŞ ve AY bir hesap iledir» (Rahmân 55:5) gibi." + R_TR},
 "badi": [{"kind": "muraat-al-nazir", "set": [1, 2], "sub": "haqiqi", "field": "sky"}],
 "tokens": [
  nahwa(tag=N),
  tok("الشَّمْسُ","shams","noun",[N, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — الْأَمْرُ.", "«the sun» — the mubtada; the thing.", "«güneş» — mübtedâ; şey."),
  wa_conj("وَالْقَمَرُ","qamar","noun",[N, "atf-nasaq"], "الْقَمَرُ مَعْطُوفٌ مَرْفُوعٌ — مُنَاسِبُ الشَّمْسِ: كِلَاهُمَا مِنْ أَجْرَامِ السَّمَاءِ.", "«and the moon» — what suits the sun: both bodies of the sky.", "«ve ay» — güneşe uygun olan: ikisi de gök cismi."),
  tok("بِحُسْبَانٍ","husban","noun",[N, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ — بِحِسَابٍ مَعْلُومٍ.", "«by reckoning» — the khabar: on a known count.", "«bir hesap ile» — haber: bilinen bir hesapla.",
      segments=[seg("بِ","bi","part"), seg("حُسْبَانٍ","husban","noun")], punct=".")]})

# ----------- s9 — al-Buhturi
S.append({"id": "s9", "translation": {
 "en": "And the verse of al-Buhturi: «…like BOWS bent back — nay, like ARROWS trimmed — nay, like BOWSTRINGS»." + R_EN,
 "tr": "Ve Buhturî'nin beyti: «…eğilmiş YAYLAR gibi — hayır, yontulmuş OKLAR gibi — hayır, KİRİŞLER gibi»." + R_TR},
 "badi": [{"kind": "muraat-al-nazir", "set": [2, 5, 8], "sub": "haqiqi", "field": "bow"}],
 "tokens": [
  wa_conj("وَقَوْلِ","qawl","noun",[N, "atf-nasaq", "idafa-definiteness"], "قَوْلِ مَعْطُوفٌ عَلَى الْمِثَالِ الْمَجْرُورِ بِنَحْوَ، مُضَافٌ.", "«and the saying of» — joined onto the example.", "«ve sözü» — örneğe matuf."),
  tok("الْبُحْتُرِيِّ","buhturi","noun",[N, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Buhturi».", "«Buhturî».", punct=":"),
  tok("كَالْقِسِيِّ","qaws","noun",[N, "huruf-jarr", "tashbih", "jam-taksir"], "الْكَافُ لِلتَّشْبِيهِ، وَالْقِسِيِّ مَجْرُورٌ — جَمْعُ قَوْسٍ؛ الْأَمْرُ الْأَوَّلُ.", "«like bows» — plural of قَوْس; the first thing.", "«yaylar gibi» — قَوْس'un çoğulu; birinci şey.",
      segments=[seg("كَ","ka","part"), seg("الْقِسِيِّ","qaws","noun")]),
  tok("الْمُعَطَّفَاتِ","muattaf","noun",[N, "naat-sifa", "ism-maful", "form-ii-verbs", "jam-muannath-salim"], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، اسْمُ مَفْعُولِ عَطَّفَ.", "«bent back» — a na't; sound feminine plural of the ism maf'ul of عَطَّفَ.", "«eğilmiş» — na't; عَطَّفَ'nin ism-i mef'ûlünün cem'-i müennes-i sâlimi."),
  tok("بَلِ","bal","part",[N, "atf-nasaq"], "حَرْفُ إِضْرَابٍ وَعَطْفٍ — يَنْقُلُ الْحُكْمَ إِلَى مَا بَعْدَهُ.", "«nay» — the particle that moves the verdict to what follows.", "«hayır» — hükmü sonrasına taşıyan idrâb harfi."),
  tok("الْأَسْهُمِ","sahm","noun",[N, "atf-nasaq", "jam-taksir"], "مَعْطُوفٌ مَجْرُورٌ — جَمْعُ سَهْمٍ؛ مُنَاسِبُ الْقِسِيِّ.", "«arrows» — plural of سَهْم; what suits the bows.", "«oklar» — سَهْم'in çoğulu; yaylara uygun olan."),
  tok("مَبْرِيَّةً","mabriyy","noun",[N, "hal", "ism-maful"], "حَالٌ مَنْصُوبٌ — اسْمُ مَفْعُولِ بَرَى: مَنْحُوتَةً.", "«trimmed» — a hal; ism maf'ul of بَرَى.", "«yontulmuş» — hâl; بَرَى'nın ism-i mef'ûlü."),
  tok("بَلِ","bal","part",[N, "atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«nay».", "«hayır»."),
  tok("الْأَوْتَارِ","watar","noun",[N, "atf-nasaq", "jam-taksir"], "مَعْطُوفٌ مَجْرُورٌ — جَمْعُ وَتَرٍ؛ الثَّالِثُ مِنَ النَّظَائِرِ: الْقَوْسُ وَالسَّهْمُ وَالْوَتَرُ.", "«bowstrings» — plural of وَتَر; the third of the peers: bow, arrow, string.", "«kirişler» — وَتَر'in çoğulu; nazîrlerin üçüncüsü: yay, ok, kiriş.", punct=".")]})

# ----------- s10 — tashabuh al-atraf (RESTORED matn)
S.append({"id": "s10", "translation": {
 "en": "And of it is what some call TASHABUH AL-ATRAF: that speech be CLOSED with what SUITS its OPENING in meaning." + R_EN,
 "tr": "Bazılarının TEŞÂBÜH-İ ETRÂF dediği de ondandır: sözün, mânâca BAŞLANGICINA UYGUN olanla BİTİRİLMESİ." + R_TR},
 "tokens": [
  wa_conj("وَمِنْهُ","min","part",[T, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "مِنْهُ خَبَرٌ مُقَدَّمٌ — مِنْ مُرَاعَاةِ النَّظِيرِ.", "«and of it» — of muraʿat al-nazir.", "«ve ondan» — mürâât-ı nazîrden.", pron=("هُ","pron-3ms")),
  tok("مَا","ma-mawsula","pron",[T, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what» — the delayed mubtada.", "«… şey» — sona kalmış mübtedâ."),
  tok("يُسَمِّيهِ","samma","verb",[T, "ism-mawsul", "mafulayn", "form-ii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ؛ صِلَةٌ.", "«call it» — the first object attached.", "«ona … der» — birinci mef'ûl bitişik.",
      segments=[seg("يُسَمِّي","samma","verb"), seg("هِ","pron-3ms","pron")]),
  tok("بَعْضُهُمْ","baad","noun",[T, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«some of them» — the doer.", "«bazıları» — fâil.",
      segments=[seg("بَعْضُ","baad","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("تَشَابُهَ","tashabuh","noun",[T, "mafulayn", "idafa-definiteness", "masdar", "form-vi-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the resemblance of» — the second object.", "«benzeşmesi» — ikinci mef'ûl."),
  tok("الْأَطْرَافِ","taraf","noun",[T, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ طَرَفٍ: أَوَّلُ الْكَلَامِ وَآخِرُهُ.", "«the ends» — plural of طَرَف: the opening and the close.", "«uçlar» — طَرَف'in çoğulu: sözün başı ve sonu.", punct="،"),
  wa_conj("وَهُوَ","huwa","pron",[T, "mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o»."),
  tok("أَنْ","an","part",[T, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that».", "«… -mesi»."),
  tok("يُخْتَمَ","khatama","verb",[T, "an-masdariyya", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«be closed» — the passive.", "«bitirilsin» — meçhûl."),
  tok("الْكَلَامُ","kalam","noun",[T, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«speech» — the deputy doer.", "«söz» — nâib-i fâil."),
  tok("بِمَا","ma-mawsula","pron",[T, "huruf-jarr", "ism-mawsul"], "جَارٌّ وَمَجْرُورٌ.", "«with what».", "«… şeyle».",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُنَاسِبُ","nasaba","verb",[T, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ؛ صِلَةٌ.", "«suits».", "«uyar»."),
  tok("ابْتِدَاءَهُ","ibtida-start","noun",[T, "maful-bihi", "idafa-definiteness", "masdar", "form-viii-verbs"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — مَصْدَرُ ابْتَدَأَ.", "«its opening» — the object; masdar of ابْتَدَأَ.", "«başlangıcına» — mef'ûl; ابْتَدَأَ'nin masdarı.",
      segments=[seg("ابْتِدَاءَ","ibtida-start","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-ca»."),
  tok("الْمَعْنَى","mana","noun",[T, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«meaning».", "«mânâ».", punct=".")]})

# ----------- s11 — 6:103
S.append({"id": "s11", "translation": {
 "en": "Such as: «Sight DOES NOT REACH Him, and He REACHES all sight; and He is the SUBTLE, the AWARE» (6:103)." + R_EN,
 "tr": "«Gözler O'nu İDRAK EDEMEZ, O gözleri İDRAK EDER; O LATÎF'tir, HABÎR'dir» (En'âm 6:103) gibi." + R_TR},
 "badi": [{"kind": "tashabuh-al-atraf", "pairs": [[7, 2], [8, 5]]}, bd("tibaq", [2, 5], sub="salb", cls="fil")],
 "tokens": [
  nahwa(tag=T),
  tok("لَا","la-nafiya","part",[T], "حَرْفُ نَفْيٍ — الطَّرَفُ الْمَنْفِيُّ يَبْدَأُ.", "«not» — the opening, denied.", "«-mez» — başlangıç, nefyedilmiş."),
  tok("تُدْرِكُهُ","adraka","verb",[T, "fail", "maful-bihi", "form-iv-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مِنَ الرَّابِعِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ — اللَّطِيفُ يُنَاسِبُ هَذَا: مَا لَا يُدْرَكُ لِلُطْفِهِ.", "«reaches Him» — Form IV; the object fronted; «the Subtle» answers this: what is not reached, for its subtlety.", "«O'nu idrak eder» — IV. bâb; mef'ûl öne alınmış; «Latîf» bunu karşılar: letâfetinden idrak edilemeyen.",
      segments=[seg("تُدْرِكُ","adraka","verb"), seg("هُ","pron-3ms","pron")]),
  tok("الْأَبْصَارُ","basar","noun",[T, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ بَصَرٍ.", "«sight» — the doer; plural of بَصَر.", "«gözler» — fâil; بَصَر'in çoğulu."),
  wa_conj("وَهُوَ","huwa","pron",[T, "mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and He».", "«ve O»."),
  tok("يُدْرِكُ","adraka","verb",[T, "mubtada-khabar", "fail", "maful-bihi", "form-iv-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ؛ وَالْجُمْلَةُ خَبَرٌ — الطَّرَفُ الْمُثْبَتُ: طِبَاقُ سَلْبٍ مَعَ لَا تُدْرِكُهُ؛ وَالْخَبِيرُ يُنَاسِبُهُ.", "«reaches» — the affirmed end: a tibaq of negation with «does not reach»; «the Aware» answers it.", "«idrak eder» — isbat edilen uç: «idrak edemez» ile selb tıbâkı; «Habîr» onu karşılar."),
  tok("الْأَبْصَارَ","basar","noun",[T, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«all sight» — the object.", "«gözleri» — mef'ûl.", punct="،"),
  wa_conj("وَهُوَ","huwa","pron",[T, "mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and He is».", "«ve O»."),
  tok("اللَّطِيفُ","latif","noun",[T, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ — الْعَالِمُ بِدَقَائِقِ الْأُمُورِ: يُنَاسِبُ لَا تُدْرِكُهُ الْأَبْصَارُ.", "«the Subtle» — the khabar: He who knows the fine grain of things; it suits «sight does not reach Him».", "«Latîf» — haber: işlerin inceliklerini bilen; «gözler O'nu idrak edemez»e uyar."),
  tok("الْخَبِيرُ","khabir","noun",[T, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ ثَانٍ مَرْفُوعٌ — الْعَالِمُ بِظَوَاهِرِ الْأَشْيَاءِ: يُنَاسِبُ وَهُوَ يُدْرِكُ الْأَبْصَارَ.", "«the Aware» — a second khabar: He who knows the outward of things; it suits «He reaches all sight».", "«Habîr» — ikinci haber: eşyânın zâhirini bilen; «O gözleri idrak eder»e uyar.", punct=".")]})
S[-1]["badi"] = [{"kind": "tashabuh-al-atraf", "pairs": [[8, 2], [9, 5]]}, bd("tibaq", [2, 5], sub="salb", cls="fil")]

# ----------- s12 — iham al-tanasub (RESTORED matn)
S.append({"id": "s12", "translation": {
 "en": "And joined to it is what is called IHAM AL-TANASUB: the gathering of a thing and what suits it in ONE OF ITS TWO SENSES, not the sense that is MEANT." + R_EN,
 "tr": "Ona ilhak edilen de ÎHÂM-I TENÂSÜB denilendir: bir şeyi, KASTEDİLEN mânâsıyla değil, İKİ MÂNÂSINDAN ÖBÜRÜYLE ona uygun olanla bir araya getirmek." + R_TR},
 "tokens": [
  wa_conj("وَيُلْحَقُ","alhaqa","verb",[H, "atf-nasaq", "naib-al-fail", "form-iv-verbs", "mudari-marfu"], "يُلْحَقُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is joined» — the passive of أَلْحَقَ.", "«ve ilhak edilir» — أَلْحَقَ'nın meçhûlü."),
  tok("بِهَا","bi","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — بِمُرَاعَاةِ النَّظِيرِ.", "«to it» — to muraʿat al-nazir.", "«ona» — mürâât-ı nazîre.",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","pron",[H, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ.", "«what» — the deputy doer.", "«… şey» — nâib-i fâil."),
  tok("يُسَمَّى","samma","verb",[H, "ism-mawsul", "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ؛ صِلَةٌ.", "«is called».", "«denir»."),
  tok("إِيهَامَ","iham","noun",[H, "mafulayn", "idafa-definiteness", "masdar", "form-iv-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ — مَصْدَرُ أَوْهَمَ.", "«the suggestion of» — the second object; masdar of أَوْهَمَ.", "«îhâmı» — ikinci mef'ûl; أَوْهَمَ'nin masdarı."),
  tok("التَّنَاسُبِ","tanasub","noun",[H, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«suiting».", "«tenâsüb».", punct="،"),
  wa_conj("وَهُوَ","huwa","pron",[H, "mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o»."),
  tok("جَمْعُ","jam","noun",[H, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the gathering of».", "«bir araya getirmek»."),
  tok("الشَّيْءِ","shay","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyi»."),
  wa_conj("وَمَا","ma-mawsula","pron",[H, "atf-nasaq", "ism-mawsul"], "مَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ.", "«and what».", "«ve … şeyi»."),
  tok("يُنَاسِبُهُ","nasaba","verb",[H, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ؛ صِلَةٌ.", "«suits it».", "«ona uyar».",
      segments=[seg("يُنَاسِبُ","nasaba","verb"), seg("هُ","pron-3ms","pron")]),
  tok("بِأَحَدِ","ahad","noun",[H, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«in one of».", "«birinden».",
      segments=[seg("بِ","bi","part"), seg("أَحَدِ","ahad","noun")]),
  tok("مَعْنَيَيْهِ","mana","noun",[H, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«its two senses» — the dual, its nun dropped for the idafa.", "«iki mânâsı» — tesniye, izâfet için nûnu düşmüş.",
      segments=[seg("مَعْنَيَيْ","mana","noun"), seg("هِ","pron-3ms","pron")]),
  tok("لَا","la-nafiya","part",[H], "حَرْفُ نَفْيٍ.", "«not».", "«değil»."),
  tok("بِالْمَعْنَى","mana","noun",[H, "huruf-jarr", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«in the sense».", "«mânâsıyla».",
      segments=[seg("بِ","bi","part"), seg("الْمَعْنَى","mana","noun")]),
  tok("الْمُرَادِ","murad","noun",[H, "naat-sifa", "ism-maful", "form-iv-verbs"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولِ أَرَادَ.", "«that is meant» — a na't; ism maf'ul of أَرَادَ.", "«kastedilen» — na't; أَرَادَ'nin ism-i mef'ûlü.", punct=".")]})

# ----------- s13 — 55:5-6: three tanasubs
S.append({"id": "s13", "translation": {
 "en": "Such as: «The SUN and the MOON are by reckoning, and the HERB and the TREE bow down» (55:5-6) — «the herb» (النَّجْم) suits the sun and the moon in its OTHER sense, «the star»." + R_EN,
 "tr": "«GÜNEŞ ve AY bir hesap iledir; BİTKİ ve AĞAÇ secde eder» (Rahmân 55:5-6) gibi — «bitki» (النَّجْم), ÖBÜR mânâsı «yıldız» ile güneşe ve aya uyar." + R_TR},
 "badi": [{"kind": "muraat-al-nazir", "set": [1, 2], "sub": "haqiqi", "field": "sky"},
          {"kind": "muraat-al-nazir", "set": [4, 5], "sub": "haqiqi", "field": "plant"},
          {"kind": "iham-al-tanasub", "set": [1, 2, 4], "word": 4, "murad": {"en": "the stemless plant, the herb", "tr": "gövdesiz bitki, ot"}, "other": {"en": "the star", "tr": "yıldız"}}],
 "tokens": [
  nahwa(tag=H),
  tok("الشَّمْسُ","shams","noun",[H, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the sun».", "«güneş»."),
  wa_conj("وَالْقَمَرُ","qamar","noun",[H, "atf-nasaq"], "الْقَمَرُ مَعْطُوفٌ — التَّنَاسُبُ الْأَوَّلُ: حَقِيقَةً.", "«and the moon» — the first tanasub, real.", "«ve ay» — birinci tenâsüb, hakikaten."),
  tok("بِحُسْبَانٍ","husban","noun",[H, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ.", "«by reckoning».", "«bir hesap ile».",
      segments=[seg("بِ","bi","part"), seg("حُسْبَانٍ","husban","noun")]),
  wa_conj("وَالنَّجْمُ","najm","noun",[H, "atf-nasaq", "mubtada-khabar"], "النَّجْمُ مُبْتَدَأٌ — هُنَا: النَّبْتُ الَّذِي لَا سَاقَ لَهُ؛ وَبِمَعْنَى الْكَوْكَبِ يُنَاسِبُ الشَّمْسَ وَالْقَمَرَ: إِيهَامُ التَّنَاسُبِ.", "«and the herb» — the mubtada; here the stemless plant; in its sense «star» it suits the sun and the moon: iham al-tanasub.", "«ve bitki» — mübtedâ; burada gövdesiz bitki; «yıldız» mânâsıyla güneşe ve aya uyar: îhâm-ı tenâsüb."),
  wa_conj("وَالشَّجَرُ","shajar","noun",[H, "atf-nasaq"], "الشَّجَرُ مَعْطُوفٌ — التَّنَاسُبُ الثَّانِي: النَّجْمُ وَالشَّجَرُ، حَقِيقَةً.", "«and the tree» — the second tanasub, real.", "«ve ağaç» — ikinci tenâsüb, hakikaten."),
  tok("يَسْجُدَانِ","sajada","verb",[H, "mubtada-khabar", "fail", "afal-khamsa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ؛ وَالْجُمْلَةُ خَبَرٌ.", "«bow down» — raf' by the nun; the alif the doer; the khabar.", "«secde eder» — nûnun sübûtuyla merfû; elif fâil; haber.",
      segments=[seg("يَسْجُدَ","sajada","verb"), seg("انِ","pron-3d","pron")], punct=".")]})

# ----------- s14 — the verdict on the three (RESTORED matn)
S.append({"id": "s14", "translation": {
 "en": "In the first two there is muraʿat al-nazir IN TRUTH; in the third it is JOINED to it — for «the herb» here is the plant, and only in the sense of «the star» does it suit the sun and the moon." + R_EN,
 "tr": "İlk ikisinde mürâât-ı nazîr HAKİKATEN vardır; üçüncüsü ona MÜLHAKTIR — çünkü «necm» burada bitkidir, ancak «yıldız» mânâsıyla güneşe ve aya uyar." + R_TR},
 "tokens": [
  tok("فَفِي","fi","part",[H, "huruf-jarr", "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«so in» — a fronted khabar.", "«işte … -de» — öne alınmış haber.",
      segments=[seg("فَ","fa","conj"), seg("فِي","fi","part")]),
  tok("الْأَوَّلَيْنِ","awwal","noun",[H, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — مُثَنَّى الْأَوَّلِ.", "«the first two» — the dual.", "«ilk ikisi» — tesniye."),
  tok("مُرَاعَاةُ","muraat","noun",[H, "mubtada-khabar", "idafa-definiteness", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«muraʿat» — the delayed mubtada.", "«mürâât» — sona kalmış mübtedâ."),
  tok("النَّظِيرِ","nazir","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-nazir».", "«-ı nazîr»."),
  tok("حَقِيقَةً","haqiqa","noun",[H, "hal", "maful-mutlaq"], "حَالٌ مَنْصُوبٌ — أَوْ مَفْعُولٌ مُطْلَقٌ: تَحَقُّقًا.", "«in truth» — a hal, or an absolute object.", "«hakikaten» — hâl yahut mef'ûl-i mutlak.", punct="،"),
  wa_conj("وَفِي","fi","part",[H, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "فِي حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in».", "«ve … -de»."),
  tok("الثَّالِثِ","thalith","noun",[H, "huruf-jarr"], "مَجْرُورٌ.", "«the third».", "«üçüncüsü»."),
  tok("مُلْحَقٌ","mulhaq","noun",[H, "mubtada-khabar", "ism-maful", "form-iv-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ أَلْحَقَ؛ أَيْ: شَيْءٌ مُلْحَقٌ.", "«something joined» — the delayed mubtada; ism maf'ul of أَلْحَقَ.", "«mülhak bir şey» — sona kalmış mübtedâ; أَلْحَقَ'nın ism-i mef'ûlü."),
  tok("بِهَا","bi","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمُلْحَقٍ.", "«to it».", "«ona».",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("لِأَنَّ","anna","part",[H, "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«for».", "«çünkü».",
      segments=[seg("لِ","li","part"), seg("أَنَّ","anna","part")]),
  tok("النَّجْمَ","najm","noun",[H, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the herb» — the ism of anna.", "«necm» — ennenin ismi."),
  tok("هُنَا","huna","noun",[H, "maful-fih", "asma-al-ishara"], "ظَرْفُ مَكَانٍ.", "«here».", "«burada»."),
  tok("النَّبْتُ","nabt","noun",[H, "inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ — مَا لَا سَاقَ لَهُ مِنَ النَّبَاتِ.", "«the plant» — the khabar of anna: what has no stem.", "«bitki» — ennenin haberi: gövdesi olmayan.", punct="،"),
  wa_conj("وَإِنَّمَا","innama","part",[H, "atf-nasaq", "innama-kaffa", "qasr"], "إِنَّمَا أَدَاةُ حَصْرٍ.", "«and only» — the particle of restriction.", "«ve ancak» — hasr edatı."),
  tok("يُنَاسِبُ","nasaba","verb",[H, "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، النَّجْمُ.", "«does it suit» — the doer «it», the herb, concealed.", "«uyar» — fâil gizli «o», necm."),
  tok("الشَّمْسَ","shams","noun",[H, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the sun».", "«güneşe»."),
  wa_conj("وَالْقَمَرَ","qamar","noun",[H, "atf-nasaq"], "الْقَمَرَ مَعْطُوفٌ مَنْصُوبٌ.", "«and the moon».", "«ve aya»."),
  tok("بِمَعْنَى","mana","noun",[H, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "جَارٌّ وَمَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«in the sense of».", "«mânâsıyla».",
      segments=[seg("بِ","bi","part"), seg("مَعْنَى","mana","noun")]),
  tok("الْكَوْكَبِ","kawkab","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَعْنَى الْآخَرُ لِلنَّجْمِ.", "«the star» — the herb's other sense.", "«yıldız» — necmin öbür mânâsı.", punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "min": find_gloss("min"), "muqabala": find_gloss("muqabala"), "hiya": find_gloss("hiya"), "an": find_gloss("an"), "ata": find_gloss("ata"), "mana": find_gloss("mana"),
 "mutawafiq": G("mutawafiq", "مُتَوَافِق", "و ف ق", "noun", "agreeing with one another (ism fa'il of تَوَافَقَ)", "birbirine uygun (تَوَافَقَ'nin ism-i fâili)", 5),
 "aw": find_gloss("aw"), "akthar": find_gloss("akthar"), "thumma": find_gloss("thumma"), "ma-mawsula": find_gloss("ma-mawsula"),
 "qabala": G("qabala", "قَابَلَ", "ق ب ل", "verb", "to face, to set against, to counter (Form III)", "karşılamak, mukâbil olmak (III. bâb)", 4, form="III"),
 "dhalika": find_gloss("dhalika"), "ala": find_gloss("ala"), "tartib": find_gloss("tartib"), "mithal": find_gloss("mithal"), "ithnan": find_gloss("ithnan"),
 "dahika": find_gloss("dahika"), "qalil": find_gloss("qalil"),
 "baka": G("baka", "بَكَى", "ب ك ي", "verb", "to weep (naqis: بَكَى يَبْكِي)", "ağlamak (nâkıs: بَكَى يَبْكِي)", 2, form="I"),
 "kathir": find_gloss("kathir"), "thalatha": find_gloss("thalatha"), "qawl": find_gloss("qawl"), "ab": find_gloss("ab"),
 "dulama": G("dulama", "أَبُو دُلَامَةَ", None, "propn", "Abu Dulama — the Abbasid-era jester-poet (d. c. 161/777)", "Ebû Dülâme — Abbâsî devri nüktedan şairi (ö. 161/777 civarı)", 6),
 "ma-taajjub": G("ma-taajjub", "مَا (التَّعَجُّبِيَّة)", None, "part", "the ma of wonder: «how …!» (مَا أَحْسَنَ)", "taaccüb mâsı: «ne …!» (مَا أَحْسَنَ)", 4),
 "ahsana": find_gloss("ahsana"), "din": find_gloss("din"), "dunya": find_gloss("dunya"), "idha": find_gloss("idha"), "ijtamaa": find_gloss("ijtamaa"),
 "aqbaha": G("aqbaha", "أَقْبَحَ", "ق ب ح", "verb", "to make ugly; مَا أَقْبَحَ «how ugly!» (Form IV)", "çirkinleştirmek; مَا أَقْبَحَ «ne çirkin!» (IV. bâb)", 4, form="IV"),
 "kufr": find_gloss("kufr"),
 "iflas": G("iflas", "إِفْلَاس", "ف ل س", "noun", "bankruptcy, having no money (masdar of أَفْلَسَ)", "iflâs, parasız kalma (أَفْلَسَ'nin masdarı)", 4),
 "rajul": find_gloss("rajul"), "arbaa": find_gloss("arbaa"), "amma": find_gloss("amma"), "man-mawsula": find_gloss("man-mawsula"),
 "ata-give": G("ata-give", "أَعْطَى", "ع ط و", "verb", "to give (Form IV, naqis: أَعْطَى يُعْطِي)", "vermek (IV. bâb, nâkıs: أَعْطَى يُعْطِي)", 2, form="IV"),
 "ittaqa": find_gloss("ittaqa"),
 "saddaqa": G("saddaqa", "صَدَّقَ", "ص د ق", "verb", "to affirm as true, to believe (Form II)", "tasdik etmek, doğrulamak (II. bâb)", 3, form="II"),
 "husna": G("husna", "حُسْنَى", "ح س ن", "noun", "the best (feminine of أَحْسَن): the word of unity, the Garden", "en güzel (أَحْسَن'in müennesi): kelime-i tevhid, cennet", 4),
 "yassara": G("yassara", "يَسَّرَ", "ي س ر", "verb", "to make easy (Form II)", "kolaylaştırmak (II. bâb)", 3, form="II"),
 "sa-istiqbal": find_gloss("sa-istiqbal") if has_gloss("sa-istiqbal") else G("sa-istiqbal", "سَـ", None, "part", "the sin of the near future: «will»", "yakın istikbal sîni: «-ecek»", 2),
 "yusra": G("yusra", "يُسْرَى", "ي س ر", "noun", "the easy way (feminine of أَيْسَر)", "en kolay yol (أَيْسَر'in müennesi)", 4),
 "bakhila": find_gloss("bakhila"),
 "istaghna": G("istaghna", "اِسْتَغْنَى", "غ ن ي", "verb", "to think oneself self-sufficient, to do without (Form X, naqis)", "kendini müstağni görmek, ihtiyaç duymamak (X. bâb, nâkıs)", 4, form="X"),
 "kadhdhaba": find_gloss("kadhdhaba"),
 "usra": G("usra", "عُسْرَى", "ع س ر", "noun", "the hard way (feminine of أَعْسَر)", "en güç yol (أَعْسَر'in müennesi)", 4),
 "zada": find_gloss("zada"), "sakkaki": find_gloss("sakkaki"), "fi": find_gloss("fi"), "anna": find_gloss("anna"),
 "sharata": G("sharata", "شَرَطَ", "ش ر ط", "verb", "to stipulate, to make a condition (شَرَطَ يَشْرِطُ)", "şart koşmak (شَرَطَ يَشْرِطُ)", 4, form="I"),
 "huna": G("huna", "هُنَا", None, "noun", "here (the demonstrative of place)", "burada (mekân işareti)", 1),
 "amr": find_gloss("amr"),
 "hunaka": G("hunaka", "هُنَاكَ", None, "noun", "there (the demonstrative of far place)", "orada (uzak mekân işareti)", 1),
 "didd": find_gloss("didd"), "ka": find_gloss("ka"), "aya": find_gloss("aya"), "lamma": find_gloss("lamma"), "jaala": find_gloss("jaala"),
 "taysir": G("taysir", "تَيْسِير", "ي س ر", "noun", "easing (masdar of يَسَّرَ)", "kolaylaştırma (يَسَّرَ'nin masdarı)", 4),
 "mushtarak": find_gloss("mushtarak"), "bayna": find_gloss("bayna"),
 "ita": G("ita", "إِعْطَاء", "ع ط و", "noun", "giving (masdar of أَعْطَى)", "verme (أَعْطَى'nın masdarı)", 3),
 "ittiqa": G("ittiqa", "اِتِّقَاء", "و ق ي", "noun", "fearing God, guarding oneself (masdar of اتَّقَى)", "sakınma, ittikâ (اتَّقَى'nın masdarı)", 4),
 "tasdiq": find_gloss("tasdiq"),
 "tasir": G("tasir", "تَعْسِير", "ع س ر", "noun", "hardening, making difficult (masdar of عَسَّرَ)", "güçleştirme (عَسَّرَ'nin masdarı)", 4),
 "bukhl": find_gloss("bukhl"),
 "istighna": G("istighna", "اِسْتِغْنَاء", "غ ن ي", "noun", "self-sufficiency, doing without (masdar of اسْتَغْنَى)", "istiğnâ, müstağni görme (اسْتَغْنَى'nın masdarı)", 4),
 "takdhib": G("takdhib", "تَكْذِيب", "ك ذ ب", "noun", "denial, calling a lie (masdar of كَذَّبَ)", "yalanlama (كَذَّبَ'nin masdarı)", 3),
 "muraat": G("muraat", "مُرَاعَاة", "ر ع ي", "noun", "observing, regard (masdar of رَاعَى); مُرَاعَاةُ النَّظِيرِ", "riayet, gözetme (رَاعَى'nın masdarı); mürâât-ı nazîr", 5),
 "nazir": G("nazir", "نَظِير", "ن ظ ر", "noun", "a like, a peer, a counterpart", "nazîr, benzer, eş", 4, plural="نَظَائِر"),
 "jam": find_gloss("jam"),
 "nasaba": G("nasaba", "نَاسَبَ", "ن س ب", "verb", "to suit, to be fitting to (Form III)", "uygun olmak, münasip düşmek (III. bâb)", 4, form="III"),
 "la-nafiya": find_gloss("la-nafiya"), "tadadd": find_gloss("tadadd"), "samma": find_gloss("samma"), "tanasub": find_gloss("tanasub"), "tawfiq": find_gloss("tawfiq"),
 "nahwa": find_gloss("nahwa"), "shams": find_gloss("shams"), "qamar": find_gloss("qamar"),
 "husban": G("husban", "حُسْبَان", "ح س ب", "noun", "reckoning, a fixed count", "hesap, belli ölçü", 4),
 "buhturi": G("buhturi", "الْبُحْتُرِيّ", None, "propn", "al-Buhturi — the Abbasid poet (d. 284/897)", "Buhturî — Abbâsî şairi (ö. 284/897)", 6),
 "qaws": G("qaws", "قَوْس", "ق و س", "noun", "a bow", "yay", 3, plural="قِسِيّ"),
 "muattaf": G("muattaf", "مُعَطَّف", "ع ط ف", "noun", "bent back, curved (ism maf'ul of عَطَّفَ)", "eğilmiş, bükülmüş (عَطَّفَ'nin ism-i mef'ûlü)", 5),
 "bal": find_gloss("bal"),
 "sahm": G("sahm", "سَهْم", "س ه م", "noun", "an arrow; a share", "ok; pay", 3, plural="أَسْهُم"),
 "mabriyy": G("mabriyy", "مَبْرِيّ", "ب ر ي", "noun", "trimmed, whittled (ism maf'ul of بَرَى)", "yontulmuş (بَرَى'nın ism-i mef'ûlü)", 5),
 "watar": G("watar", "وَتَر", "و ت ر", "noun", "a bowstring; a string", "kiriş; tel", 4, plural="أَوْتَار"),
 "baad": find_gloss("baad"), "tashabuh": find_gloss("tashabuh"), "taraf": find_gloss("taraf"), "huwa": find_gloss("huwa"),
 "khatama": G("khatama", "خَتَمَ", "خ ت م", "verb", "to seal, to close (خَتَمَ يَخْتِمُ)", "mühürlemek, bitirmek (خَتَمَ يَخْتِمُ)", 3, form="I"),
 "kalam": find_gloss("kalam"),
 "ibtida-start": G("ibtida-start", "ابْتِدَاء", "ب د أ", "noun", "a beginning, an opening (masdar of ابْتَدَأَ)", "başlangıç (ابْتَدَأَ'nin masdarı)", 3),
 "adraka": find_gloss("adraka"),
 "basar": G("basar", "بَصَر", "ب ص ر", "noun", "sight; the eye", "görme; göz", 2, plural="أَبْصَار"),
 "latif": G("latif", "لَطِيف", "ل ط ف", "noun", "subtle, gentle; al-Latif — He who knows the fine grain of things", "latîf, ince; el-Latîf — işlerin inceliklerini bilen", 3),
 "khabir": G("khabir", "خَبِير", "خ ب ر", "noun", "aware, expert; al-Khabir — He who knows the outward of things", "habîr, haberdar; el-Habîr — eşyanın zâhirini bilen", 3),
 "alhaqa": G("alhaqa", "أَلْحَقَ", "ل ح ق", "verb", "to join to, to attach (Form IV)", "ilhak etmek, katmak (IV. bâb)", 4, form="IV"),
 "bi": find_gloss("bi"), "iham": find_gloss("iham"), "shay": find_gloss("shay"), "ahad": find_gloss("ahad"), "murad": find_gloss("murad"),
 "najm": find_gloss("najm"), "shajar": find_gloss("shajar"),
 "sajada": G("sajada", "سَجَدَ", "س ج د", "verb", "to bow down, prostrate (سَجَدَ يَسْجُدُ)", "secde etmek (سَجَدَ يَسْجُدُ)", 2, form="I"),
 "awwal": find_gloss("awwal"), "haqiqa": find_gloss("haqiqa"), "thalith": find_gloss("thalith"),
 "mulhaq": G("mulhaq", "مُلْحَق", "ل ح ق", "noun", "joined, appended (ism maf'ul of أَلْحَقَ)", "mülhak, eklenmiş (أَلْحَقَ'nın ism-i mef'ûlü)", 5),
 "nabt": G("nabt", "نَبْت", "ن ب ت", "noun", "a plant, herbage", "bitki, ot", 3),
 "innama": find_gloss("innama"), "kawkab": find_gloss("kawkab"),
 "wa": find_gloss("wa"), "fa": find_gloss("fa"), "li": find_gloss("li"), "lam-amr": find_gloss("lam-amr"), "ma-masdariyya": find_gloss("ma-masdariyya"),
 "pron-3ms": find_gloss("pron-3ms"), "pron-3fs": find_gloss("pron-3fs"), "pron-3mp": find_gloss("pron-3mp"), "pron-3d": find_gloss("pron-3d"),
}

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "qabala", _sg.derived(_sg.B3, _sg.W3, "ُ", "قَابَل", "قَابِل", "قَابِل", "مُقَابَلَة", "مُقَابِل", "مُقَابَل", "قُوبِلَ", "يُقَابَلُ"))
put_morph(mo, "baka", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "بَكَ", "بْك", "i", "اِبْك", "بُكَاء", "بَاكٍ (الْبَاكِي)", "مَبْكِيّ", "بُكِيَ", "يُبْكَى",
                                  note="نَاقِصٌ يَائِيٌّ: بَكَى يَبْكِي — بَكَوْا، بَكَتْ: حُذِفَتِ الْيَاءُ قَبْلَ الْوَاوِ وَالْأَلِفُ قَبْلَ التَّاءِ."))
put_morph(mo, "aqbaha", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْبَح", "قْبِح", "أَقْبِح", "إِقْبَاح", "مُقْبِح", "مُقْبَح", "أُقْبِحَ", "يُقْبَحُ",
                                    "مَا أَقْبَحَ: فِعْلُ التَّعَجُّبِ عَلَى وَزْنِ أَفْعَلَ، جَامِدٌ لَا يَتَصَرَّفُ."))
put_morph(mo, "ata-give", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَعْطَ", "عْط", "i", "أَعْط", "إِعْطَاء", "مُعْطٍ (الْمُعْطِي)", "مُعْطًى", "أُعْطِيَ", "يُعْطَى",
                                            note="نَاقِصٌ مِنَ الرَّابِعِ: أَعْطَى يُعْطِي — أَعْطَوْا، أَعْطَتْ."))
put_morph(mo, "saddaqa", _sg.derived(_sg.B2, _sg.W2, "ُ", "صَدَّق", "صَدِّق", "صَدِّق", "تَصْدِيق", "مُصَدِّق", "مُصَدَّق", "صُدِّقَ", "يُصَدَّقُ"))
put_morph(mo, "yassara", _sg.derived(_sg.B2, _sg.W2, "ُ", "يَسَّر", "يَسِّر", "يَسِّر", "تَيْسِير", "مُيَسِّر", "مُيَسَّر", "يُسِّرَ", "يُيَسَّرُ"))
put_morph(mo, "istaghna", _sg.derived_naqis(_sg.B10, _sg.W10, "َ", "اِسْتَغْنَ", "سْتَغْن", "i", "اِسْتَغْن", "اسْتِغْنَاء", "مُسْتَغْنٍ (الْمُسْتَغْنِي)", "مُسْتَغْنًى", "اسْتُغْنِيَ", "يُسْتَغْنَى",
                                             note="نَاقِصٌ مِنَ الِاسْتِفْعَالِ: اسْتَغْنَى يَسْتَغْنِي — اسْتَغْنَوْا، اسْتَغْنَتْ."))
put_morph(mo, "sharata", _sg.sound1("daraba", "شَرَط", "شْرِط", "اِشْرِط", "شَرْط", "شَارِط", "مَشْرُوط", "شُرِطَ", "يُشْرَطُ"))
put_morph(mo, "nasaba", _sg.derived(_sg.B3, _sg.W3, "ُ", "نَاسَب", "نَاسِب", "نَاسِب", "مُنَاسَبَة", "مُنَاسِب", "مُنَاسَب", "نُوسِبَ", "يُنَاسَبُ"))
put_morph(mo, "khatama", _sg.sound1("daraba", "خَتَم", "خْتِم", "اِخْتِم", "خَتْم", "خَاتِم", "مَخْتُوم", "خُتِمَ", "يُخْتَمُ"))
put_morph(mo, "alhaqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَلْحَق", "لْحِق", "أَلْحِق", "إِلْحَاق", "مُلْحِق", "مُلْحَق", "أُلْحِقَ", "يُلْحَقُ"))
put_morph(mo, "sajada", _sg.sound1("nasara", "سَجَد", "سْجُد", "اُسْجُد", "سُجُود", "سَاجِد", "مَسْجُود", "سُجِدَ", "يُسْجَدُ"))
for k in ("ata", "dahika", "ahsana", "ijtamaa", "ittaqa", "bakhila", "kadhdhaba", "zada", "jaala", "samma", "adraka"):
    if k not in mo["verbs"] and has_morph(k): mo["verbs"][k] = find_morph(k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
def _load(nid): return json.loads((GR / f"{nid}.json").read_text(encoding="utf-8"))
NOTE_M = _load("muqabala")
NOTE_M["group"] = "badi"; NOTE_M["level"] = 6
NOTE_M["classicalSources"] = ["تلخيص المفتاح — المقابلة: أن يؤتى بمعنيين متوافقين أو معان متوافقة ثم بما يقابل ذلك على الترتيب"] + [s for s in NOTE_M["classicalSources"] if "المقابلة" not in s]
NOTE_M["question"] = {
 "en": ["Are there TWO OR MORE meanings on the first side, and does EACH get its counterpart on the second — IN THE SAME ORDER? فَلْيَضْحَكُوا قَلِيلًا وَلْيَبْكُوا كَثِيرًا: laugh/weep, little/much. That is the MUQABALA; one pair alone is only a tibaq.",
        "Count the sides. Two (9:82), three (Abu Dulama: fine/ugly, religion/unbelief, world/bankruptcy), four (92:5-10: gives/withholds, fears/self-sufficient, affirms/denies, ease/hardship).",
        "Sakkaki's test: when one side is made the CONDITION of a thing, are the contraries made the condition of its CONTRARY? Giving, fearing, affirming → ease; withholding, self-sufficiency, denial → hardship."],
 "tr": ["Birinci tarafta İKİ YAHUT DAHA ÇOK mânâ var mı ve her biri ikinci tarafta AYNI SIRAYLA mukâbilini alıyor mu? فَلْيَضْحَكُوا قَلِيلًا وَلْيَبْكُوا كَثِيرًا: gül/ağla, az/çok. MUKÂBELE budur; tek çift yalnız tıbâktır.",
        "Tarafları say. İki (Tevbe 9:82), üç (Ebû Dülâme: güzel/çirkin, din/küfür, dünya/iflâs), dört (Leyl 92:5-10: verir/cimrilik eder, sakınır/müstağni görür, tasdik eder/yalanlar, kolay/güç).",
        "Sekkâkî'nin ölçüsü: bir taraf bir şeye ŞART kılınınca, zıtlar onun ZIDDINA şart kılınıyor mu? Verme, sakınma, tasdik → kolaylık; cimrilik, istiğnâ, yalanlama → güçlük."]}
if "WHAT THE ENGINE CLAIMS" not in NOTE_M["explanation"]["en"]: NOTE_M["explanation"]["en"] += " WHAT THE ENGINE CLAIMS: the BadiEngine reads a muqabala when it finds two or more tibaq pairs whose ends keep ONE ORDER — the first side's words all before the second side's, and the counterparts in the same sequence; it reports the sides as two rows and the count (two, three, four). Out of order, it reports the tibaqs but not the muqabala. It grades itself against the authored `muqabala` frames of ch58."
if "MOTORUN İDDİASI" not in NOTE_M["explanation"]["tr"]: NOTE_M["explanation"]["tr"] += " MOTORUN İDDİASI: BadiEngine, uçları TEK BİR SIRA tutan iki yahut daha çok tıbâk çifti bulduğunda mukâbeleyi okur — birinci tarafın kelimeleri ikinci tarafınkilerden önce ve mukâbiller aynı sırada; tarafları iki satır ve sayı (iki, üç, dört) olarak bildirir. Sıra bozuksa tıbâkları bildirir, mukâbeleyi değil. Kendini 58. bâbın müellif `muqabala` çerçevelerine karşı sınar."
NOTE_M["examples"] = [e for e in NOTE_M["examples"] if e.get("sourceStory")] + [
  {"ar": "فَلْيَضْحَكُوا قَلِيلًا وَلْيَبْكُوا كَثِيرًا", "en": "two against two (9:82).", "tr": "ikiye iki (Tevbe 9:82).", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "مَا أَحْسَنَ الدِّينَ وَالدُّنْيَا إِذَا اجْتَمَعَا * وَأَقْبَحَ الْكُفْرَ وَالْإِفْلَاسَ بِالرَّجُلِ", "en": "three against three.", "tr": "üçe üç.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "فَأَمَّا مَنْ أَعْطَى وَاتَّقَى وَصَدَّقَ بِالْحُسْنَى فَسَنُيَسِّرُهُ لِلْيُسْرَى وَأَمَّا مَنْ بَخِلَ وَاسْتَغْنَى وَكَذَّبَ بِالْحُسْنَى فَسَنُيَسِّرُهُ لِلْعُسْرَى", "en": "four against four (92:5-10).", "tr": "dörde dört (Leyl 92:5-10).", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "إِذَا شُرِطَ هُنَا أَمْرٌ شُرِطَ هُنَاكَ ضِدُّهُ", "en": "Sakkaki's addition.", "tr": "Sekkâkî'nin ilâvesi.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"}]
for r in ("ilm-al-badi", "tashabuh-al-atraf"):
    if r not in NOTE_M["relatedNotes"]: NOTE_M["relatedNotes"].append(r)

NOTE_N = _load("muraat-al-nazir")
NOTE_N["group"] = "badi"; NOTE_N["level"] = 6
NOTE_N["classicalSources"] = ["تلخيص المفتاح — مراعاة النظير: جمع أمر وما يناسبه لا بالتضاد، وتسمى التناسب والتوفيق"] + [s for s in NOTE_N["classicalSources"] if "مراعاة" not in s]
NOTE_N["question"] = {
 "en": ["Are two things of ONE FIELD gathered — not as contraries? الشَّمْسُ وَالْقَمَرُ (55:5): both bodies of the sky. That is MURAʿAT AL-NAZIR, the TANASUB, the TAWFIQ.",
        "Does the family grow? Buhturi's bows, then arrows, then bowstrings — bow, arrow, string, one field three deep.",
        "Is the fit real or borrowed? النَّجْم beside الشَّجَر is the herb, a real fit; beside الشَّمْس and الْقَمَر it fits only as «the star», a sense not meant — that is IHAM AL-TANASUB, joined to the figure, not of it."],
 "tr": ["TEK SAHADAN iki şey — zıt olarak değil — bir araya gelmiş mi? الشَّمْسُ وَالْقَمَرُ (Rahmân 55:5): ikisi de gök cismi. MÜRÂÂT-I NAZÎR, TENÂSÜB, TEVFÎK budur.",
        "Aile büyüyor mu? Buhturî'nin yayları, sonra okları, sonra kirişleri — yay, ok, kiriş; tek saha üç kat.",
        "Uyum gerçek mi ödünç mü? الشَّجَر yanındaki النَّجْم bitkidir, gerçek uyum; الشَّمْس ve الْقَمَر yanında yalnız kastedilmeyen «yıldız» mânâsıyla uyar — bu ÎHÂM-I TENÂSÜBDÜR, sanata mülhaktır, ondan değil."]}
if "WHAT THE ENGINE CLAIMS" not in NOTE_N["explanation"]["en"]: NOTE_N["explanation"]["en"] += " WHAT THE ENGINE CLAIMS: the BadiEngine reads muraʿat al-nazir off a STORED table of fields (the sky: sun, moon, star; the bow: bow, arrow, string; the plant: herb, tree…), keyed on lemmas: two or more words of one field in one sentence, not contraries, are reported as a set with the field's name. A word whose OTHER sense belongs to a field (النَّجْم as star) is reported as iham al-tanasub only when an authored frame says which sense is meant; the engine does not guess the meant sense. It grades itself against the authored frames of ch58."
if "MOTORUN İDDİASI" not in NOTE_N["explanation"]["tr"]: NOTE_N["explanation"]["tr"] += " MOTORUN İDDİASI: BadiEngine mürâât-ı nazîri köklere anahtarlanmış YERLEŞİK bir sahalar tablosundan (gök: güneş, ay, yıldız; yay: yay, ok, kiriş; bitki: ot, ağaç…) okur: bir cümlede tek sahadan, zıt olmayan iki yahut daha çok kelime, sahanın adıyla bir küme olarak bildirilir. ÖBÜR mânâsı bir sahaya ait olan kelime (yıldız olarak النَّجْم) ancak müellif çerçevesi hangi mânânın kastedildiğini söylüyorsa îhâm-ı tenâsüb olarak bildirilir; motor kastedilen mânâyı tahmin etmez. Kendini 58. bâbın müellif çerçevelerine karşı sınar."
NOTE_N["examples"] = [e for e in NOTE_N["examples"] if e.get("sourceStory")] + [
  {"ar": "الشَّمْسُ وَالْقَمَرُ بِحُسْبَانٍ", "en": "sun and moon (55:5).", "tr": "güneş ve ay (Rahmân 55:5).", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "كَالْقِسِيِّ الْمُعَطَّفَاتِ بَلِ الْأَسْهُمِ مَبْرِيَّةً بَلِ الْأَوْتَارِ", "en": "bow, arrow, string.", "tr": "yay, ok, kiriş.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ", "en": "herb and tree — and the herb's other sense.", "tr": "bitki ve ağaç — ve bitkinin öbür mânâsı.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"}]
for r in ("ilm-al-badi", "tashabuh-al-atraf", "iham-al-tanasub"):
    if r not in NOTE_N["relatedNotes"]: NOTE_N["relatedNotes"].append(r)

NOTE_T = {
 "id": "tashabuh-al-atraf",
 "title": {"ar": "تَشَابُهُ الْأَطْرَافِ — أَنْ يُخْتَمَ الْكَلَامُ بِمَا يُنَاسِبُ ابْتِدَاءَهُ", "en": "Tashabuh al-atraf — closing the speech with what suits its opening", "tr": "Teşâbüh-i etrâf — sözü başlangıcına uygun olanla bitirmek"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — ومنه ما يسميه بعضهم تشابه الأطراف"],
 "question": {
  "en": ["Does the END of the speech answer its BEGINNING in meaning? لَا تُدْرِكُهُ الْأَبْصَارُ … وَهُوَ اللَّطِيفُ: the Subtle is what sight cannot reach; يُدْرِكُ الْأَبْصَارَ … الْخَبِيرُ: the Aware is He who reaches. That is TASHABUH AL-ATRAF.",
         "Whose name is it? «What SOME call» — the Talkhis files it under muraʿat al-nazir: the two ends are peers, gathered.",
         "Where does the engine look? At the last words of the sentence against its first clauses: a name of God, a sifa, an epithet, whose stored field matches the verb or noun it closes."],
  "tr": ["Sözün SONU BAŞINI mânâca karşılıyor mu? لَا تُدْرِكُهُ الْأَبْصَارُ … وَهُوَ اللَّطِيفُ: Latîf, gözlerin ulaşamadığıdır; يُدْرِكُ الْأَبْصَارَ … الْخَبِيرُ: Habîr, ulaşandır. TEŞÂBÜH-İ ETRÂF budur.",
         "Kimin adı? «BAZILARININ dediği» — Telhîs onu mürâât-ı nazîrin altına koyar: iki uç nazîrdir, bir araya getirilmiştir.",
         "Motor nereye bakar? Cümlenin son kelimelerine karşı ilk cümleciklerine: yerleşik sahası kapattığı fiil yahut isimle örtüşen bir ilâhî isim, bir sıfat, bir lakap."]},
 "plain": {
  "en": "A branch of muraʿat al-nazir: the sentence closes with words that suit how it opened — «the Subtle» answers «sight does not reach Him», «the Aware» answers «He reaches all sight». The engine ties each closing epithet to the clause it echoes and draws the tie.",
  "tr": "Mürâât-ı nazîrin bir dalı: cümle, açılışına uygun kelimelerle kapanır — «Latîf», «gözler O'nu idrak edemez»i, «Habîr», «O gözleri idrak eder»i karşılar. Motor her kapanış sıfatını yankıladığı cümleciğe bağlar ve bağı çizer."},
 "explanation": {
  "en": "TASHABUH AL-ATRAF (the resemblance of the ends) is أَنْ يُخْتَمَ الْكَلَامُ بِمَا يُنَاسِبُ ابْتِدَاءَهُ فِي الْمَعْنَى — that speech be CLOSED with what SUITS its OPENING in meaning. The Talkhis gives it as what SOME call by that name and files it under muraʿat al-nazir: the two ends of the speech are peers, gathered. The example is 6:103, لَا تُدْرِكُهُ الْأَبْصَارُ وَهُوَ يُدْرِكُ الْأَبْصَارَ وَهُوَ اللَّطِيفُ الْخَبِيرُ: اللَّطِيف — He who knows the fine grain of things, Himself too fine for sight — suits لَا تُدْرِكُهُ الْأَبْصَارُ; الْخَبِير — He who knows the outward of things — suits وَهُوَ يُدْرِكُ الْأَبْصَارَ. The pairing is in ORDER: the first epithet answers the first clause, the second the second — a muqabala of peers rather than of contraries. Inside the aya there is also a tibaq of negation, لَا تُدْرِكُهُ … يُدْرِكُ. WHAT THE ENGINE CLAIMS: the BadiEngine reads tashabuh al-atraf when the sentence ENDS in one or more epithets (a sifa mushabbaha, a name of God, an ism fa'il) whose stored field matches a verb or noun of the sentence's OPENING clauses, and it draws each tie as an arc from the end back to the beginning; the order of the ties is reported. It grades itself against the authored `tashabuh-al-atraf` frame of ch58, whose pairs it must match exactly.",
  "tr": "TEŞÂBÜH-İ ETRÂF (uçların benzeşmesi) أَنْ يُخْتَمَ الْكَلَامُ بِمَا يُنَاسِبُ ابْتِدَاءَهُ فِي الْمَعْنَى'dır — sözün, mânâca BAŞLANGICINA UYGUN olanla BİTİRİLMESİ. Telhîs onu BAZILARININ bu adla andığı şey olarak verir ve mürâât-ı nazîrin altına koyar: sözün iki ucu nazîrdir, bir araya getirilmiştir. Örnek En'âm 6:103, لَا تُدْرِكُهُ الْأَبْصَارُ وَهُوَ يُدْرِكُ الْأَبْصَارَ وَهُوَ اللَّطِيفُ الْخَبِيرُ: اللَّطِيف — işlerin inceliklerini bilen, kendisi gözler için fazla ince olan — لَا تُدْرِكُهُ الْأَبْصَارُ'ya uyar; الْخَبِير — eşyanın zâhirini bilen — وَهُوَ يُدْرِكُ الْأَبْصَارَ'ya uyar. Eşleme SIRALIDIR: birinci sıfat birinci cümleciği, ikincisi ikincisini karşılar — zıtların değil nazîrlerin mukâbelesi. Âyetin içinde bir de selb tıbâkı vardır: لَا تُدْرِكُهُ … يُدْرِكُ. MOTORUN İDDİASI: BadiEngine, cümle yerleşik sahası AÇILIŞ cümleciklerinin bir fiil yahut ismiyle örtüşen bir yahut daha çok sıfatla (sıfat-ı müşebbehe, ilâhî isim, ism-i fâil) BİTTİĞİNDE teşâbüh-i etrâfı okur ve her bağı sondan başa bir yay olarak çizer; bağların sırası bildirilir. Kendini 58. bâbın müellif `tashabuh-al-atraf` çerçevesine karşı sınar; çiftlerini tam tutturması gerekir."},
 "examples": [
  {"ar": "لَا تُدْرِكُهُ الْأَبْصَارُ وَهُوَ يُدْرِكُ الْأَبْصَارَ وَهُوَ اللَّطِيفُ الْخَبِيرُ", "en": "the Subtle answers the first clause, the Aware the second (6:103).", "tr": "Latîf birinci cümleciği, Habîr ikincisini karşılar (En'âm 6:103).", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "أَنْ يُخْتَمَ الْكَلَامُ بِمَا يُنَاسِبُ ابْتِدَاءَهُ فِي الْمَعْنَى", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«اللَّطِيفُ الْخَبِيرُ yalnız iki ilâhî isimdir; âyetin başıyla ilgisi yok»",
   "right": "«Her isim başın bir cümleciğini karşılar: Latîf → idrak edilemeyen, Habîr → idrak eden»",
   "why": {"en": "The figure lives in the tie between the ends. Read the epithets as a closing formula and the tashabuh is lost.", "tr": "Sanat uçlar arasındaki bağda yaşar. Sıfatları kapanış kalıbı olarak okursan teşâbüh kaybolur."}},
  {"wrong": "«Teşâbüh-i etrâf, tıbâkın bir kısmıdır»",
   "right": "«Mürâât-ı nazîrin bir kısmıdır: uçlar zıt değil münasiptir»",
   "why": {"en": "The Talkhis places it under gathering peers. The tibaq inside 6:103 (لَا تُدْرِكُهُ / يُدْرِكُ) is a second figure, not this one.", "tr": "Telhîs onu nazîrleri bir araya getirmenin altına koyar. En'âm 6:103'teki tıbâk (لَا تُدْرِكُهُ / يُدْرِكُ) ikinci bir sanattır, bu değil."}}],
 "relatedNotes": ["muraat-al-nazir", "muqabala", "tibaq", "iham-al-tanasub", "ilm-al-badi"]}

NOTE_H = {
 "id": "iham-al-tanasub",
 "title": {"ar": "إِيهَامُ التَّنَاسُبِ — الْمُنَاسَبَةُ بِأَحَدِ مَعْنَيَيِ اللَّفْظِ لَا بِالْمُرَادِ", "en": "Iham al-tanasub — the fit that holds only through the sense not meant", "tr": "Îhâm-ı tenâsüb — yalnız kastedilmeyen mânâ yoluyla kurulan uyum"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — والثالث ملحق بمراعاة النظير، ويسمى إيهام التناسب"],
 "question": {
  "en": ["Does the word have TWO senses, and does it suit its neighbours only in the one NOT meant? النَّجْم in 55:6 is the herb (beside الشَّجَر) — but as «the star» it would sit with الشَّمْس and الْقَمَر. That is IHAM AL-TANASUB.",
         "Real or joined? In 55:5-6 the Talkhis counts three tanasubs: sun/moon and herb/tree are REAL; sun-moon-«star» is JOINED to the figure — an appearance of fit.",
         "Can the engine tell which sense is meant? No: it needs the authored frame's «murad» and «other». What it does alone is find that the word's OTHER sense belongs to the neighbours' field."],
  "tr": ["Kelimenin İKİ mânâsı var ve komşularına yalnız KASTEDİLMEYENİYLE mi uyuyor? Rahmân 55:6'daki النَّجْم bitkidir (الشَّجَر yanında) — ama «yıldız» olarak الشَّمْس ve الْقَمَر ile otururdu. ÎHÂM-I TENÂSÜB budur.",
         "Gerçek mi mülhak mı? Telhîs 55:5-6'da üç tenâsüb sayar: güneş/ay ve bitki/ağaç GERÇEKTİR; güneş-ay-«yıldız» sanata MÜLHAKTIR — bir uyum görüntüsü.",
         "Motor hangi mânânın kastedildiğini bilebilir mi? Hayır: müellif çerçevesinin «murad» ve «other» alanlarına muhtaçtır. Tek başına yaptığı, kelimenin ÖBÜR mânâsının komşuların sahasına ait olduğunu bulmaktır."]},
 "plain": {
  "en": "When a word with two senses is gathered with things that suit it only in the sense not meant — «the herb» beside the sun and the moon, which would fit as «the star». The Talkhis joins it to muraʿat al-nazir as an appearance of fit. The engine flags the word's other sense and lets the frame say which is meant.",
  "tr": "İki mânâlı bir kelime, ona yalnız kastedilmeyen mânâsıyla uyan şeylerle bir araya gelince — güneş ve ayın yanındaki «bitki», «yıldız» olarak uyardı. Telhîs onu bir uyum görüntüsü olarak mürâât-ı nazîre ilhak eder. Motor kelimenin öbür mânâsını işaretler, kastedileni çerçeveye bırakır."},
 "explanation": {
  "en": "IHAM AL-TANASUB (the suggestion of a fit) is the gathering of a thing and what suits it IN ONE OF ITS TWO SENSES, NOT THE SENSE MEANT. The Talkhis reaches it through 55:5-6, وَالشَّمْسُ وَالْقَمَرُ بِحُسْبَانٍ وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ, where it counts THREE tanasubs: (1) الشَّمْس with الْقَمَر, (2) النَّجْم with الشَّجَر, (3) الشَّمْس, الْقَمَر and النَّجْم together. In the first two there is muraʿat al-nazir IN TRUTH; the third is JOINED to it (مُلْحَق), because النَّجْم here is the stemless PLANT — that is what sits with the tree and bows down — and only in its other sense, the STAR, does it suit the sun and the moon. The hearer's mind feels the fit through a meaning the speaker does not intend: an iham, a suggestion. The figure is a cousin of the tawriya, where the far sense IS meant; here the near sense is meant and the far sense only suits. WHAT THE ENGINE CLAIMS: the BadiEngine finds the candidate on its own — a word whose lemma carries a second gloss belonging to the same stored field as its neighbours (النَّجْم: plant / star; sky: sun, moon, star) — but it does not decide which sense is meant; the authored frame's «murad» and «other» settle that, and the engine reports the set with the word lit as the borrowed member. It grades itself against the authored `iham-al-tanasub` frame of ch58.",
  "tr": "ÎHÂM-I TENÂSÜB (uyum vehmi) bir şeyi, ona İKİ MÂNÂSINDAN BİRİYLE — KASTEDİLEN MÂNÂYLA DEĞİL — uyan şeyle bir araya getirmektir. Telhîs ona Rahmân 55:5-6 üzerinden ulaşır, وَالشَّمْسُ وَالْقَمَرُ بِحُسْبَانٍ وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ; burada ÜÇ tenâsüb sayar: (1) الشَّمْس ile الْقَمَر, (2) النَّجْم ile الشَّجَر, (3) الشَّمْس, الْقَمَر ve النَّجْم birlikte. İlk ikisinde mürâât-ı nazîr HAKİKATEN vardır; üçüncüsü ona MÜLHAKTIR (مُلْحَق), çünkü النَّجْم burada gövdesiz BİTKİDİR — ağaçla oturup secde eden odur — ve ancak öbür mânâsı YILDIZ ile güneşe ve aya uyar. Dinleyenin zihni uyumu konuşanın kastetmediği bir mânâ yoluyla duyar: bir îhâm, bir vehim. Sanat tevriyenin akrabasıdır; orada uzak mânâ KASTEDİLİR, burada yakın mânâ kastedilir, uzak mânâ yalnız uyar. MOTORUN İDDİASI: BadiEngine adayı kendi başına bulur — kökü komşularıyla aynı yerleşik sahaya ait ikinci bir mânâ taşıyan kelime (النَّجْم: bitki / yıldız; gök: güneş, ay, yıldız) — fakat hangi mânânın kastedildiğine karar vermez; bunu müellif çerçevesinin «murad» ve «other» alanları belirler ve motor kümeyi, kelimeyi ödünç üye olarak aydınlatarak bildirir. Kendini 58. bâbın müellif `iham-al-tanasub` çerçevesine karşı sınar."},
 "examples": [
  {"ar": "وَالشَّمْسُ وَالْقَمَرُ بِحُسْبَانٍ وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ", "en": "three tanasubs; the third an iham (55:5-6).", "tr": "üç tenâsüb; üçüncüsü îhâm (Rahmân 55:5-6).", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "لِأَنَّ النَّجْمَ هُنَا النَّبْتُ، وَإِنَّمَا يُنَاسِبُ الشَّمْسَ وَالْقَمَرَ بِمَعْنَى الْكَوْكَبِ", "en": "the verdict.", "tr": "hüküm.", "sourceStory": "talkhis-al-miftah", "sentence": "s14"}],
 "commonMistakes": [
  {"wrong": "«النَّجْم burada yıldızdır: güneş ve ayla birlikte sayılmıştır»",
   "right": "«Burada bitkidir: ağaçla birlikte secde eder; yıldız mânâsı yalnız uyum vehmi verir»",
   "why": {"en": "The verb يَسْجُدَانِ and the partner الشَّجَر fix the meant sense. The star is the other sense, felt but not meant.", "tr": "يَسْجُدَانِ fiili ve ortak الشَّجَر kastedilen mânâyı sabitler. Yıldız öbür mânâdır; duyulur, kastedilmez."}},
  {"wrong": "«Îhâm-ı tenâsüb bir tevriyedir»",
   "right": "«Tevriyede uzak mânâ kastedilir; îhâm-ı tenâsübde yakın mânâ kastedilir, uzak mânâ yalnız komşulara uyar»",
   "why": {"en": "Both use a two-sense word; they differ in which sense the speaker means.", "tr": "İkisi de iki mânâlı kelime kullanır; konuşanın hangi mânâyı kastettiğinde ayrılırlar."}}],
 "relatedNotes": ["muraat-al-nazir", "tashabuh-al-atraf", "tibaq", "ilm-al-badi"]}

ADD_EN = (" Chapter 58 (lines ~3976-4025, sahifa 137-138) carries the muqabala (two, three and four against their counterparts; "
          "Sakkaki's addition), muraʿat al-nazir, what some call tashabuh al-atraf, and iham al-tanasub: the ayat (s2 9:82, s4 92:5-10, "
          "s8 55:5, s11 6:103, s13 55:5-6) and the verses of Abu Dulama (s3) and al-Buhturi (s9) are Arabic as the source prints them. "
          "s1, s5-s7, s10, s12, s14 and the frames of every example are RESTORATIONS, not quotations: the source carries those steps only "
          "in Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's register; each is marked «restored» "
          "in its translation. The examples carry `badi` frames of the new kinds (muqabala with its two ordered sides, muraat-al-nazir "
          "with its field, tashabuh-al-atraf with its pairs, iham-al-tanasub with the meant and the other sense) beside the tibaqs inside them.")
ADD_TR = (" Elli sekizinci bâb (satır ~3976-4025, sahife 137-138) mukâbeleyi (ikiye iki, üçe üç, dörde dört; Sekkâkî'nin ilâvesi), "
          "mürâât-ı nazîri, bazılarının teşâbüh-i etrâf dediğini ve îhâm-ı tenâsübü taşır: âyetler (s2 Tevbe 9:82, s4 Leyl 92:5-10, s8 Rahmân "
          "55:5, s11 En'âm 6:103, s13 Rahmân 55:5-6) ile Ebû Dülâme (s3) ve Buhturî (s9) beyitleri kaynağın bastığı Arapçadır. s1, s5-s7, s10, "
          "s12, s14 ve her örneğin çerçeveleri ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; "
          "Arapça, matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Örnekler, "
          "içlerindeki tıbâkların yanında yeni kısımların `badi` çerçevelerini (iki sıralı tarafıyla mukâbele, sahasıyla mürâât-ı nazîr, "
          "çiftleriyle teşâbüh-i etrâf, kastedilen ve öbür mânâsıyla îhâm-ı tenâsüb) taşır.")
write_out(58, S, TITLE, ADD_EN, ADD_TR, "3976-4025", GLOSS_ADD, notes=(NOTE_M, NOTE_N, NOTE_T, NOTE_H),
          related=(("tibaq", ["muqabala", "muraat-al-nazir"]), ("ilm-al-badi", ["muqabala", "muraat-al-nazir", "tashabuh-al-atraf"])))
report(58, S, GLOSS_ADD, (NOTE_M, NOTE_N, NOTE_T, NOTE_H))
