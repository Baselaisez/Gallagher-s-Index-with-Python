# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 4: «مَا نَفْقَهُ كَثِيرًا مِمَّا تَقُولُ» — sections 8–9 of the story of Shuʿayb (print pp. 7–8):
the people feign not to understand, excuse themselves by his weakness and his clan, and Shuʿayb marvels (11:91–92).
python3 tools/authoring/author_qisas4_ch4.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "مَا نَفْقَهُ كَثِيرًا مِمَّا تَقُولُ", "en": "We understand little of what you say", "tr": "Söylediklerinin çoğunu anlamıyoruz"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; SH = "in-shartiyya"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def atf_majrur(full, lex, en, tr, punct=None, tags=(), ar="مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَالِاسْمُ " + ar, en, tr, punct=punct, segments=wa_(full[2:], lex, "noun"))
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr"):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def annahu(full="وَأَنَّهُ", wa=True, pre_ar="الْوَاوُ عَاطِفَةٌ، وَ", en="«and that he»", tr="«ve onun»", extra=()):
    return tok(full, "anna", "part", [IW] + ([AT] if wa else []) + list(extra), pre_ar + "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", en + " — anna with its ism.", tr + " — enne ve ismi.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("أَنَّ", "anna", "part"), pr3ms()])
def kaannahu(full="كَأَنَّهُ", wa=False):
    return tok(full, "kaanna", "part", [IW, "tashbih"] + ([AT] if wa else []), W(wa) + "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ، وَالْهَاءُ اسْمُهَا.", Wen(wa) + "«as though he» — ka-anna with its ism.", Wtr(wa) + "«sanki o» — keenne ve ismi.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("كَأَنَّ", "kaanna", "part"), pr3ms()])
def maa_annahu():
    return [tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ.", "«although» — literally «with [the fact] that».", "«hâlbuki» — «… olmasıyla birlikte»."),
            tok("أَنَّهُ", "anna", "part", [IW, ID], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«he» — the clause annexed to «with».", "«onun» — cümle maa'ya muzâf.", segments=[seg("أَنَّ", "anna", "part"), pr3ms()])]

# ---------------------------------------------------------------- §8
sen("s1", "And the people feigned ignorance of what Shuʿayb meant, as though he were speaking to them in a foreign tongue — although he was a son of the town and the people's brother —",
        "Kavim, Şuayb'ın ne demek istediğini anlamazlıktan geldi; sanki onlarla yabancı bir dilde konuşuyordu — hâlbuki o beldenin oğlu ve kavmin kardeşiydi;", [
  tok("وَتَجَاهَلَ", "tajahala", "verb", [AT, MB, "form-vi-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتَجَاهَلَ فِعْلٌ مَاضٍ.", "«and feigned ignorance of»", "«ve anlamazlıktan geldi»", segments=wa_("تَجَاهَلَ", "tajahala", "verb")),
  tok("الْقَوْمُ", "qawm", "noun", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — the doer.", "«kavim» — fâil."),
  tok("مَا", "ma-mawsula", "pron", [MW, MB], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the object.", "«… şeyi» — mef'ûl."),
  tok("أَرَادَهُ", "arada", "verb", [MW, MB, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«meant» — the ṣila.", "«kastettiği» — sıla.", segments=[seg("أَرَادَ", "arada", "verb"), pr3ms()]),
  tok("شُعَيْبٌ", "shuayb", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ.", "«Shuʿayb» — the doer.", "«Şuayb» — fâil.", punct="،"),
  kaannahu(),
  tok("كَانَ", "kana", "verb", [IW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كَأَنَّ.", "«were» — kāna; the khabar of ka-anna.", "«idi» — kâne; keenne'nin haberi."),
  tok("يَتَكَلَّمُ", "takallama", "verb", [KN, "mudari-marfu", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — خَبَرُ كَانَ.", "«speaking» — kāna's khabar.", "«konuşuyor» — kâne'nin haberi."),
  prep_pron("مَعَهُمْ", "maa", "هُمْ", "pron-3mp", "«with them»", "«onlarla»", extra_ar=" — مَعَ ظَرْفٌ مُضَافٌ"),
  fi(), majrur("لُغَةٍ", "lugha", "«a tongue»", "«bir dilde»"), naat("أَجْنَبِيَّةٍ", "ajnabi", "«foreign»", "«yabancı»", punct="،", tags=["ism-mansub"]),
  *maa_annahu(),
  tok("ابْنُ", "ibn", "noun", [IW, ID], "خَبَرُ أَنَّ مَرْفُوعٌ، مُضَافٌ.", "«a son of» — the khabar of anna.", "«oğlu» — enne'nin haberi."),
  mudaf_ilayh("الْبَلَدِ", "balad", "«the town»", "«beldenin»"),
  tok("وَأَخُو", "akh", "noun", [AT, ID, "five-nouns"], "الْوَاوُ عَاطِفَةٌ، وَأَخُو مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«and the brother of» — one of the five nouns, in rafʿ by the wāw.", "«ve kardeşi» — esmâ-i hamseden, vâv ile merfû.", segments=wa_("أَخُو", "akh", "noun")),
  mudaf_ilayh("الْقَوْمِ", "qawm", "«the people»", "«kavmin»", punct="،"),
])
sen("s2", "and as though he were not clear in his speech, not eloquent — although he was among the most eloquent of them in speech and the clearest in expression;",
        "ve sanki sözünde açık değil, fasih değildi — hâlbuki o, söz bakımından en beliğleri ve beyan bakımından en fasihleri arasındaydı;", [
  kaannahu("وَكَأَنَّهُ", wa=True),
  tok("كَانَ", "kana", "verb", [IW, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — خَبَرُ كَأَنَّ.", "«were»", "«idi»"),
  tok("غَيْرَ", "ghayr", "noun", [KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«not» — kāna's khabar, annexed.", "«değil» — kâne'nin haberi, muzâf."),
  mudaf_ilayh("مُبِينٍ", "mubin", "«clear»", "«açık»", tags=["ism-fail", "form-iv-verbs"]),
  fi(), tok("كَلَامِهِ", "kalam", "noun", [HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his speech»", "«sözünde»", segments=[seg("كَلَامِ", "kalam", "noun"), pr3msi()]),
  tok("غَيْرَ", "ghayr", "noun", [KN, ID, "badal"], "خَبَرٌ ثَانٍ أَوْ بَدَلٌ مَنْصُوبٌ، مُضَافٌ.", "«not» — a second khabar.", "«değil» — ikinci haber."),
  mudaf_ilayh("مُفْصِحٍ", "mufsih", "«eloquent»", "«fasih»", punct="،", tags=["ism-fail", "form-iv-verbs"]),
  *maa_annahu(),
  tok("مِنْ", "min", "prep", [HJ, IW], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«among» — the khabar of anna.", "«-den» — enne'nin haberi."),
  tok("أَبْلَغِهِمْ", "ablagh", "noun", [HJ, ID, "ism-tafdil"], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — أَفْعَلُ تَفْضِيلٍ.", "«the most eloquent of them» — the elative.", "«en beliğleri» — ism-i tafdîl.", segments=[seg("أَبْلَغِ", "ablagh", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("كَلَامًا", "kalam", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«in speech» — the tamyīz.", "«söz bakımından» — temyiz."),
  tok("وَأَفْصَحِهِمْ", "afsah", "noun", [AT, ID, "ism-tafdil"], "الْوَاوُ عَاطِفَةٌ، وَأَفْصَحِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the clearest of them»", "«ve en fasihleri»", segments=[seg("وَ", "wa", "conj"), seg("أَفْصَحِ", "afsah", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("بَيَانًا", "bayan", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in expression» — the tamyīz.", "«beyan bakımından» — temyiz.", punct="،"),
])
sen("s3", "and this is what people say when counsel weighs heavy on them and the work is hard for them.", "insanlar, nasihat ağır gelip iş zor gelince hep böyle derler.", [
  tok("وَهٰكَذَا", "hakadha", "part", [AT, "asma-al-ishara", "maful-mutlaq"], "الْوَاوُ عَاطِفَةٌ، وَهٰكَذَا: الْهَاءُ لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ — أَيْ: قَوْلًا كَهٰذَا.", "«and thus» — «a saying like this».", "«ve böyle» — «bunun gibi bir söz».", segments=wa_("هٰكَذَا", "hakadha", "part")),
  tok("يَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«say»", "«der»"), nas_fail(),
  tok("إِذَا", "idha", "part", ["idha-shartiyya", MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، جَوَابُهُ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«when»", "«-ince»"),
  tok("كَبُرَتْ", "kabura", "verb", ["idha-shartiyya"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«weighs heavy»", "«ağır gelir»"),
  prep_pron("عَلَيْهِمُ", "ala", "هِمُ", "pron-3mp", "«on them»", "«onlara»", extra_ar="، حُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  tok("النَّصِيحَةُ", "nasiha", "noun", [FL], "فَاعِلٌ مَرْفُوعٌ.", "«counsel» — the doer.", "«nasihat» — fâil."),
  tok("وَشَقَّ", "shaqqa", "verb", [AT, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَشَقَّ فِعْلٌ مَاضٍ.", "«and is hard»", "«ve zor gelir»", segments=wa_("شَقَّ", "shaqqa", "verb")),
  prep_pron("عَلَيْهِمُ", "ala", "هِمُ", "pron-3mp", "«for them»", "«onlara»"),
  tok("الْعَمَلُ", "amal-work", "noun", [FL], "فَاعِلٌ مَرْفُوعٌ.", "«the work» — the doer.", "«iş» — fâil.", punct="."),
])
# ---------------------------------------------------------------- §9
sen("s4", "And they excused themselves by his weakness and his being alone, and that were it not for his clan and their kinship to him they would have stoned him and been rid of him;",
        "Onun zayıflığını ve yalnızlığını bahane ettiler; akrabaları ve onlarla hısımlığı olmasa onu taşlar ve ondan kurtulurlardı;", [
  tok("وَتَعَلَّلُوا", "taallala", "verb", [AT, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَعَلَّلُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«and they excused themselves»", "«ve bahane ettiler»", segments=wa_("تَعَلَّلُوا", "taallala", "verb")),
  tok("بِضَعْفِهِ", "daf", "noun", [HJ, ID, "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَضَعْفِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«by his weakness»", "«zayıflığıyla»", segments=[seg("بِ", "bi", "prep"), seg("ضَعْفِ", "daf", "noun"), pr3msi()]),
  tok("وَوَحْدَتِهِ", "wahda-loneliness", "noun", [AT, ID, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَوَحْدَةِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and his being alone»", "«ve yalnızlığıyla»", segments=[seg("وَ", "wa", "conj"), seg("وَحْدَتِ", "wahda-loneliness", "noun"), pr3msi()]),
  annahu(),
  tok("لَوْلَا", "lawla", "part", [IW, MK, SH], "حَرْفُ امْتِنَاعٍ لِوُجُودٍ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«were it not for» — the clause is anna's khabar.", "«olmasaydı» — cümle enne'nin haberi."),
  tok("عَشِيرَتُهُ", "ashira", "noun", [MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرُهُ مَحْذُوفٌ وُجُوبًا: مَوْجُودَةٌ.", "«his clan» — the mubtada whose khabar lawlā drops.", "«akrabaları» — haberi vâcip olarak mahzûf mübtedâ.", segments=[seg("عَشِيرَتُ", "ashira", "noun"), pr3ms()]),
  tok("وَقَرَابَتُهُمْ", "qaraba", "noun", [AT, ID], "الْوَاوُ عَاطِفَةٌ، وَقَرَابَةُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«and their kinship»", "«ve onların hısımlığı»", segments=[seg("وَ", "wa", "conj"), seg("قَرَابَتُ", "qaraba", "noun"), pr3mp()]),
  prep_pron("لَهُ", "li", "هُ", "pron-3ms", "«to him»", "«ona»"),
  tok("لَرَجَمُوهُ", "rajama", "verb", [SH, MB, "in-shartiyya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْلَا، وَرَجَمُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«they would have stoned him» — the lām of lawlā's answer.", "«onu taşlarlardı» — levlâ'nın cevabının lâmı.", segments=[seg("لَ", "lam-jawab", "part"), seg("رَجَمُو", "rajama", "verb"), pr3ms()]),
  tok("بِالْحِجَارَةِ", "hijara", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحِجَارَةِ مَجْرُورٌ.", "«with stones»", "«taşlarla»", segments=[seg("بِ", "bi", "prep"), seg("الْحِجَارَةِ", "hijara", "noun")]),
  tok("وَتَخَلَّصُوا", "takhallasa", "verb", [AT, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَخَلَّصُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«and been rid»", "«ve kurtulurlardı»", segments=wa_("تَخَلَّصُوا", "takhallasa", "verb")),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of him»", "«ondan»", punct="،"),
])
sen("s5", "and Shuʿayb found that monstrous, and marvelled that God — the Mighty, the Able, the Strong, the Subduer — should weigh less with them than a clan that is exposed to disease and death, weakness and helplessness.",
        "Şuayb bunu çirkin buldu ve Azîz, Kâdir, Kavî, Kahhâr olan Allah'ın, onların gözünde hastalığa, ölüme, zayıflığa ve âcizliğe açık bir akraba topluluğundan daha önemsiz olmasına şaştı.", [
  tok("وَقَدِ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and indeed»", "«ve gerçekten»", segments=wa_("قَدِ", "qad", "part")),
  tok("اسْتَنْكَرَ", "istankara", "verb", [MB, "form-x-verbs"], "فِعْلٌ مَاضٍ.", "«found monstrous»", "«çirkin buldu»"),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", MB], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«bunu» — mef'ûl."),
  tok("شُعَيْبٌ", "shuayb", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ.", "«Shuʿayb» — the doer.", "«Şuayb» — fâil."),
  tok("وَتَعَجَّبَ", "taajjaba", "verb", [AT, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَعَجَّبَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and marvelled»", "«ve şaştı»", segments=wa_("تَعَجَّبَ", "taajjaba", "verb")),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فِي مَحَلِّ جَرٍّ.", "«that» — the clause after it in jarr.", "«-e» — ardındaki cümle cer mahallinde."),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", ["an-masdariyya", KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«should be» — kāna in naṣb.", "«olması» — mansûb kâne."),
  tok("اللهُ", "allah", "propn", [KN], "لَفْظُ الْجَلَالَةِ اسْمُ يَكُونَ مَرْفُوعٌ.", "«God» — the ism of kāna.", "«Allah» — kâne'nin ismi."),
  naat("الْعَزِيزُ", "aziz", "«the Mighty»", "«Azîz»", case="raf"), naat("الْقَادِرُ", "qadir", "«the Able»", "«Kâdir»", case="raf", tags=["ism-fail"]),
  tok("وَالْقَوِيُّ", "qawi", "noun", [AT], "الْوَاوُ عَاطِفَةٌ، وَالْقَوِيُّ مَعْطُوفٌ مَرْفُوعٌ.", "«the Strong»", "«Kavî»", segments=wa_("الْقَوِيُّ", "qawi", "noun")),
  naat("الْقَاهِرُ", "qahir", "«the Subduer»", "«Kahhâr»", case="raf", punct="،", tags=["ism-fail"]),
  tok("أَهْوَنَ", "ahwan", "noun", [KN, "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ — أَفْعَلُ تَفْضِيلٍ.", "«of less weight» — kāna's khabar, an elative.", "«daha önemsiz» — kâne'nin haberi, ism-i tafdîl."),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«with them»", "«onlara»"),
  tok("مِنْ", "min", "prep", [HJ], "حَرْفُ جَرٍّ — مِنْ التَّفْضِيلِيَّةُ.", "«than»", "«-den»"),
  majrur("عَشِيرَةٍ", "ashira", "«a clan»", "«bir akraba topluluğu»"),
  tok("هِيَ", "hiya", "pron", [MK, NA], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — وَالْجُمْلَةُ صِفَةٌ لِعَشِيرَةٍ.", "«that is» — the mubtada of a qualifying clause.", "«… olan» — sıfat cümlesinin mübtedâsı."),
  tok("عُرْضَةٌ", "urda", "noun", [MK], "خَبَرٌ مَرْفُوعٌ.", "«exposed» — the khabar.", "«açık, maruz» — haber."),
  tok("لِلْأَمْرَاضِ", "marad", "noun", [HJ, "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَمْرَاضِ مَجْرُورٌ.", "«to diseases»", "«hastalıklara»", segments=[seg("لِ", "li", "prep"), seg("الْأَمْرَاضِ", "marad", "noun")]),
  atf_majrur("وَالْهَلَاكِ", "halak", "«and death»", "«ve ölüme»", tags=["masdar"]), atf_majrur("وَالضَّعْفِ", "daf", "«weakness»", "«zayıflığa»", tags=["masdar"]), atf_majrur("وَالْعَجْزِ", "ajz", "«and helplessness»", "«ve âcizliğe»", punct=".", tags=["masdar"]),
])
sen("s6", "They said: «O Shuʿayb, we understand little of what you say, and we see you weak among us; were it not for your clan we would have stoned you, and you are not mighty against us» (11:91).",
        "Dediler ki: «Ey Şuayb, söylediklerinin çoğunu anlamıyoruz ve seni aramızda zayıf görüyoruz; akrabaların olmasaydı seni taşlardık; sen bize karşı güçlü de değilsin» (11:91).", [
  qalu(punct=":"), *quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("شُعَيْبُ", "shuayb", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ.", "«Shuʿayb» — the munādā on the ḍamma.", "«Şuayb» — damme üzere münâdâ."),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "حَرْفُ نَفْيٍ.", "«not»", "«-miyoruz»"),
  tok("نَفْقَهُ", "faqiha", "verb", ["mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«we understand»", "«anlıyoruz»"),
  maful_("كَثِيرًا", "kathir", "«much»", "«çoğunu»"),
  tok("مِمَّا", "ma-mawsula", "pron", [HJ, MW], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ فِي مَا الْمَوْصُولَةِ، وَمَا فِي مَحَلِّ جَرٍّ.", "«of what» — min fused with mā.", "«… şeyden» — min, mâ'ya idgam edilmiş.", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  tok("تَقُولُ", "qala", "verb", [MW, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — صِلَةٌ.", "«you say» — the ṣila.", "«söylediğin» — sıla."),
  tok("وَإِنَّا", "inna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا.", "«and indeed we»", "«ve şüphesiz biz»", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("ا", "pron-1p", "pron")]),
  tok("لَنَرَاكَ", "raa", "verb", [IW, MB, "naqis-verbs", "mudari-marfu", "tawkid"], "اللَّامُ الْمُزَحْلَقَةُ، وَنَرَى مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْكَافُ مَفْعُولٌ أَوَّلُ — خَبَرُ إِنَّ.", "«we see you» — the slid lām; the khabar of inna.", "«seni görüyoruz» — kayan lâm; inne'nin haberi.", segments=[seg("لَ", "lam-ibtida", "part"), seg("نَرَا", "raa", "verb"), seg("كَ", "pron-2ms", "pron")]),
  prep_pron("فِينَا", "fi", "نَا", "pron-1p", "«among us»", "«aramızda»"),
  tok("ضَعِيفًا", "daif", "noun", ["mafulayn", "hal"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — أَوْ حَالٌ إِنْ كَانَتْ رَأَى بَصَرِيَّةً.", "«weak» — the second object, or a ḥāl.", "«zayıf» — ikinci mef'ûl ya da hâl."),
  tok("وَلَوْلَا", "lawla", "part", [AT, SH, MK], "الْوَاوُ عَاطِفَةٌ، وَلَوْلَا حَرْفُ امْتِنَاعٍ لِوُجُودٍ.", "«and were it not for»", "«ve olmasaydı»", segments=wa_("لَوْلَا", "lawla", "part")),
  tok("رَهْطُكَ", "raht", "noun", [MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرُهُ مَحْذُوفٌ وُجُوبًا.", "«your clan» — the mubtada.", "«akrabaların» — mübtedâ.", segments=[seg("رَهْطُ", "raht", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَرَجَمْنَاكَ", "rajama", "verb", [SH, MB, "in-shartiyya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْلَا، وَرَجَمْ فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«we would have stoned you»", "«seni taşlardık»", segments=[seg("لَ", "lam-jawab", "part"), seg("رَجَمْ", "rajama", "verb"), seg("نَا", "pron-1p", "pron"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَمَا", "ma-hijaziyya", "part", [AT, "ma-la-mushabbaha"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ.", "«and not» — the Ḥijāzī mā.", "«ve değil» — Hicâzî mâ.", segments=wa_("مَا", "ma-hijaziyya", "part")),
  tok("أَنْتَ", "anta", "pron", ["ma-la-mushabbaha"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ مَا.", "«you» — the ism of mā.", "«sen» — mâ'nın ismi."),
  prep_pron("عَلَيْنَا", "ala", "نَا", "pron-1p", "«against us»", "«bize karşı»"),
  tok("بِعَزِيزٍ", "aziz", "noun", [HJ, "ma-la-mushabbaha", "huruf-jarr-nawadir"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَعَزِيزٍ خَبَرُ مَا مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "«mighty» — the khabar of mā after the added bāʾ.", "«güçlü» — zâid bâ'dan sonra mâ'nın haberi.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("عَزِيزٍ", "aziz", "noun")]),
  ]),
])
sen("s7", "He said: «O my people, is my clan mightier with you than God, whom you have cast behind your backs? Indeed my Lord encompasses what you do» (11:92).",
        "Dedi ki: «Ey kavmim, akrabalarım size göre Allah'tan daha mı güçlü ki O'nu arkanıza atıp unuttunuz? Şüphesiz Rabbim yaptıklarınızı kuşatmıştır» (11:92).", [
  qala(punct=":"), *quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("قَوْمِ", "qawm", "noun", ["vocative-munada", ID, "ya-al-mutakallim"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ.", "«my people»", "«kavmim»"),
  tok("أَرَهْطِي", "raht", "noun", ["al-istifham", MK, ID, "ya-al-mutakallim"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَرَهْطُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«is my clan» — the question hamza; the mubtada.", "«akrabalarım mı» — istifham hemzesi; mübtedâ.", segments=[seg("أَ", "hamza-istifham", "part"), seg("رَهْطِ", "raht", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("أَعَزُّ", "aazz", "noun", [MK, "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — أَفْعَلُ تَفْضِيلٍ.", "«mightier» — the khabar, an elative.", "«daha güçlü» — haber, ism-i tafdîl."),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«with you»", "«size göre»"),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — مِنْ التَّفْضِيلِيَّةُ.", "«than»", "«-den»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'tan»"),
  tok("وَاتَّخَذْتُمُوهُ", "ittakhadha", "verb", [AT, MB, "mafulayn", "form-viii-verbs"], "الْوَاوُ لِلْحَالِ، وَاتَّخَذْ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ، وَالْوَاوُ لِلْإِشْبَاعِ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«while you have cast Him» — the hā the first object; the wāw after the mīm lengthens it.", "«O'nu … atmışken» — hâ birinci mef'ûl; mîmden sonraki vâv işbâ içindir.", segments=[seg("وَ", "wa", "conj"), seg("اتَّخَذْ", "ittakhadha", "verb"), seg("تُمُو", "pron-2mp", "pron"), pr3ms()]),
  tok("وَرَاءَكُمْ", "waraa", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«behind you»", "«arkanıza»", segments=[seg("وَرَاءَ", "waraa", "noun"), pr2mp()]),
  tok("ظِهْرِيًّا", "zihri", "noun", ["mafulayn", "ism-mansub"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — أَيْ: مَنْسِيًّا مَنْبُوذًا.", "«cast away» — the second object: forgotten.", "«unutulmuş» — ikinci mef'ûl."),
  tok("إِنَّ", "inna", "part", [IW], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«indeed»", "«şüphesiz»"),
  tok("رَبِّي", "rabb", "noun", [IW, ID, "ya-al-mutakallim"], "اسْمُ إِنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the ism of inna.", "«Rabbim» — inne'nin ismi.", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("بِمَا", "ma-mawsula", "pron", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِمُحِيطٌ.", "«what» — hangs on «encompasses».", "«… şeyi» — «kuşatmıştır»a bağlı.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  khamsa("تَعْمَلُونَ", "amila", "«you do» — the ṣila.", "«yaptığınız» — sıla.", tags=[MW]),
  tok("مُحِيطٌ", "muhit", "noun", [IW, "ism-fail"], "خَبَرُ إِنَّ مَرْفُوعٌ.", "«encompasses» — the khabar of inna.", "«kuşatıcıdır» — inne'nin haberi.", punct="."),
  ]),
])

CAND = {
 "tajahala": G("tajahala", "تَجَاهَلَ", "ج ه ل", "verb", "to feign ignorance of (Form VI)", "bilmezlikten gelmek (tefâul)", 4),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend (Form IV)", "istemek (if'âl)", 1),
 "kaanna": G("kaanna", "كَأَنَّ", None, "part", "as if, as though — the sister of إِنَّ that likens", "keenne — sanki; benzetme bildiren inne kardeşi", 3),
 "takallama": G("takallama", "تَكَلَّمَ", "ك ل م", "verb", "to speak (Form V)", "konuşmak (tefa''ul)", 1),
 "maa": G("maa", "مَعَ", None, "noun", "with, together with (a ẓarf)", "ile, beraber (zarf)", 2),
 "lugha": G("lugha", "لُغَة", "ل غ و", "noun", "a language, a tongue", "dil", 1),
 "ajnabi": G("ajnabi", "أَجْنَبِيّ", "ج ن ب", "noun", "foreign (a nisba)", "yabancı", 2),
 "ibn": G("ibn", "ابْن", "ب ن و", "noun", "son", "oğul", 1),
 "balad": G("balad", "بَلَد", "ب ل د", "noun", "a town, a country", "belde, şehir", 1),
 "akh": G("akh", "أَخ", "أ خ و", "noun", "brother", "kardeş", 1, plural="إِخْوَة"),
 "mubin": G("mubin", "مُبِين", "ب ي ن", "noun", "clear, making clear (ism fāʿil of أَبَانَ)", "açık, apaçık", 2),
 "kalam": G("kalam", "كَلَام", "ك ل م", "noun", "speech", "söz, kelâm", 2),
 "mufsih": G("mufsih", "مُفْصِح", "ف ص ح", "noun", "eloquent, speaking plainly (ism fāʿil of أَفْصَحَ)", "fasih konuşan", 4),
 "ablagh": G("ablagh", "أَبْلَغ", "ب ل غ", "noun", "more / most eloquent (elative of بَلِيغ)", "daha beliğ, en beliğ", 4),
 "afsah": G("afsah", "أَفْصَح", "ف ص ح", "noun", "more / most eloquent (elative of فَصِيح)", "efsah — en fasih", 4),
 "bayan": G("bayan", "بَيَان", "ب ي ن", "noun", "expression, clarity of speech", "beyan", 3),
 "hakadha": G("hakadha", "هٰكَذَا", None, "part", "thus, like this", "böyle", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if — the conditional ẓarf of the future", "-dığı zaman, -sa — istikbal şart zarfı", 2),
 "kabura": G("kabura", "كَبُرَ", "ك ب ر", "verb", "to be great; كَبُرَ عَلَيْهِ: to weigh heavy on him", "büyük olmak; kebura aleyhi: ona ağır gelmek", 2),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to split; شَقَّ عَلَيْهِ: to be hard on him", "yarmak; şakka aleyhi: ona zor gelmek", 3),
 "amal-work": G("amal-work", "عَمَل", "ع م ل", "noun", "work, action", "iş, amel", 1),
 "taallala": G("taallala", "تَعَلَّلَ", "ع ل ل", "verb", "to make excuses (تَعَلَّلَ بِ) (Form V)", "bahane etmek (tefa''ul)", 4),
 "daf": G("daf", "ضَعْف", "ض ع ف", "noun", "weakness", "zayıflık", 2),
 "wahda-loneliness": G("wahda-loneliness", "وَحْدَة", "و ح د", "noun", "being alone, loneliness; unity", "yalnızlık; birlik", 3),
 "lawla": G("lawla", "لَوْلَا", None, "part", "were it not for — its mubtada's khabar is always dropped", "levlâ — olmasaydı; mübtedâsının haberi daima mahzûf", 3),
 "ashira": G("ashira", "عَشِيرَة", "ع ش ر", "noun", "a clan, kinsfolk", "aşiret, akraba", 3),
 "qaraba": G("qaraba", "قَرَابَة", "ق ر ب", "noun", "kinship", "hısımlık, akrabalık", 3),
 "rajama": G("rajama", "رَجَمَ", "ر ج م", "verb", "to stone", "taşlamak", 2),
 "lam-jawab": G("lam-jawab", "لَ (لَامُ الْجَوَابِ)", None, "part", "the lām of the answer — of لَوْ, لَوْلَا or an oath", "cevap lâmı — lev, levlâ veya kasemin", 4),
 "hijara": G("hijara", "حِجَارَة", "ح ج ر", "noun", "stones", "taşlar", 2),
 "takhallasa": G("takhallasa", "تَخَلَّصَ", "خ ل ص", "verb", "to get rid of (تَخَلَّصَ مِنْ) (Form V)", "kurtulmak (tefa''ul)", 3),
 "istankara": G("istankara", "اِسْتَنْكَرَ", "ن ك ر", "verb", "to find monstrous, to disapprove (Form X)", "çirkin bulmak, kınamak (istif'âl)", 4),
 "taajjaba": G("taajjaba", "تَعَجَّبَ", "ع ج ب", "verb", "to marvel (تَعَجَّبَ مِنْ) (Form V)", "şaşmak, hayret etmek (tefa''ul)", 3),
 "aziz": G("aziz", "عَزِيز", "ع ز ز", "noun", "mighty, dear", "azîz — güçlü, değerli", 2),
 "qadir": G("qadir", "قَادِر", "ق د ر", "noun", "able, powerful (ism fāʿil of قَدَرَ)", "kâdir — güç yetiren", 2),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1, plural="أَقْوِيَاء"),
 "qahir": G("qahir", "قَاهِر", "ق ه ر", "noun", "subduing, the Subduer (ism fāʿil of قَهَرَ)", "kahir — kahreden", 3),
 "ahwan": G("ahwan", "أَهْوَن", "ه و ن", "noun", "lighter, of less weight (elative of هَيِّن)", "daha önemsiz, daha hafif", 4),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it", "o", 1),
 "urda": G("urda", "عُرْضَة", "ع ر ض", "noun", "exposed to, a target for (عُرْضَةٌ لِ)", "maruz, açık (urdatün li-)", 4),
 "marad": G("marad", "مَرَض", "م ر ض", "noun", "disease, illness", "hastalık", 1, plural="أَمْرَاض"),
 "halak": G("halak", "هَلَاك", "ه ل ك", "noun", "perishing, death, ruin", "helâk, ölüm", 2),
 "ajz": G("ajz", "عَجْز", "ع ج ز", "noun", "helplessness, inability", "âcizlik", 2),
 "faqiha": G("faqiha", "فَقِهَ", "ف ق ه", "verb", "to understand", "anlamak, kavramak", 2),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "daif": G("daif", "ضَعِيف", "ض ع ف", "noun", "weak", "zayıf", 1),
 "raht": G("raht", "رَهْط", "ر ه ط", "noun", "a clan, a band of kinsmen", "raht — akraba topluluğu", 3),
 "ma-hijaziyya": G("ma-hijaziyya", "مَا (الْحِجَازِيَّة)", None, "part", "the Ḥijāzī mā — the negating mā that governs like لَيْسَ", "Hicâzî mâ — leyse gibi amel eden nefy mâ'sı", 5),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (masculine singular)", "sen", 1),
 "aazz": G("aazz", "أَعَزّ", "ع ز ز", "noun", "mightier, dearer (elative of عَزِيز)", "daha güçlü, daha değerli", 3),
 "ittakhadha": G("ittakhadha", "اِتَّخَذَ", "أ خ ذ", "verb", "to take (as), to adopt (two objects) (Form VIII)", "edinmek (iki mef'ûllü; iftiâl)", 2),
 "waraa": G("waraa", "وَرَاءَ", "و ر ي", "noun", "behind (a ẓarf)", "arkasında (zarf)", 2),
 "zihri": G("zihri", "ظِهْرِيّ", "ظ ه ر", "noun", "cast behind one's back, forgotten (a nisba of ظَهْر)", "arkaya atılmış, unutulmuş", 5),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to work; to do", "çalışmak, yapmak", 1),
 "muhit": G("muhit", "مُحِيط", "ح و ط", "noun", "encompassing (ism fāʿil of أَحَاطَ)", "kuşatıcı", 3),
 "lam-ibtida": G("lam-ibtida", "لَ (لَامُ الِابْتِدَاءِ)", None, "part", "the lām of ibtidāʾ — slid onto the khabar of إِنَّ", "ibtidâ lâmı — inne'nin haberine kayan lâm", 4),
 "hamza-istifham": G("hamza-istifham", "أَ (الِاسْتِفْهَام)", None, "part", "the question hamza", "istifham hemzesi", 2),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masculine singular, attached)", "sen / senin (bitişik)", 1),
 "shuayb": G("shuayb", "شُعَيْب", None, "propn", "Shuʿayb — the prophet of Madyan", "Şuayb — Medyen'in peygamberi", 1),
 "ghayr": G("ghayr", "غَيْر", None, "noun", "other than; except", "başka, gayri", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tajahala", _sg.derived(_sg.B6, _sg.W6, "َ", "تَجَاهَل", "تَجَاهَل", "تَجَاهَل", "تَجَاهُل", "مُتَجَاهِل", "مُتَجَاهَل", "تُجُوهِلَ", "يُتَجَاهَلُ", "تَجَاهَلَ يَتَجَاهَلُ: أَظْهَرَ الْجَهْلَ بِهِ — بَابُ التَّفَاعُلِ"))
put_morph(mo, "kabura", _sg.sound1("karuma", "كَبُر", "كْبُر", "اُكْبُر", "كِبَر", "كَبِير", None, None, None, "كَبُرَ يَكْبُرُ: عَظُمَ — بَابُ حَسُنَ؛ كَبُرَ عَلَيْهِ: شَقَّ"))
put_morph(mo, "taallala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَعَلَّل", "تَعَلَّل", "تَعَلَّل", "تَعَلُّل", "مُتَعَلِّل", None, None, None, "تَعَلَّلَ بِكَذَا يَتَعَلَّلُ: اعْتَذَرَ بِهِ — بَابُ التَّفَعُّلِ"))
put_morph(mo, "rajama", _sg.sound1("nasara", "رَجَم", "رْجُم", "اُرْجُم", "رَجْم", "رَاجِم", "مَرْجُوم", "رُجِمَ", "يُرْجَمُ", "رَجَمَ يَرْجُمُ: رَمَى بِالْحِجَارَةِ — بَابُ نَصَرَ"))
put_morph(mo, "takhallasa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَخَلَّص", "تَخَلَّص", "تَخَلَّص", "تَخَلُّص", "مُتَخَلِّص", None, None, None, "تَخَلَّصَ مِنْهُ يَتَخَلَّصُ: نَجَا — بَابُ التَّفَعُّلِ"))
put_morph(mo, "istankara", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَنْكَر", "سْتَنْكِر", "اِسْتَنْكِر", "اِسْتِنْكَار", "مُسْتَنْكِر", "مُسْتَنْكَر", "اُسْتُنْكِرَ", "يُسْتَنْكَرُ", "اِسْتَنْكَرَ يَسْتَنْكِرُ: عَدَّهُ مُنْكَرًا — بَابُ الِاسْتِفْعَالِ"))
put_morph(mo, "faqiha", _sg.sound1("samia", "فَقِه", "فْقَه", "اِفْقَه", "فِقْه", "فَقِيه", "مَفْقُوه", "فُقِهَ", "يُفْقَهُ", "فَقِهَ يَفْقَهُ: فَهِمَ — بَابُ سَمِعَ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch4 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 4 (print pp. 7–8, sections 8–9): the people feign not to understand (s1–s3), excuse themselves by his weakness and his clan, Shuʿayb marvels, with 11:91–92 (s4–s7)."
ADD_TR = " Dördüncü bölüm (baskı s. 7–8, 8–9. kısımlar): kavim anlamazlıktan gelir (s1–s3), onun zayıflığını ve akrabasını bahane eder, Şuayb şaşar; 11:91–92 ile (s4–s7)."
write_out(4, S, TITLE, ADD_EN, ADD_TR, "sections 8–9", GLOSS_ADD, notes=(), related=())
report(4, S, GLOSS_ADD, ())
