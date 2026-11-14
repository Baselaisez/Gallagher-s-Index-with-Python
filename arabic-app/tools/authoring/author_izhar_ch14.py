# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 14: the seventh QIYĀSĪ governor — the ANNEXED NOUN (الِاسْمُ الْمُضَافُ), which governs jarr: its
# condition — a noun bare of its tanwīn and of what stands for it, for the annexation's sake; not equal to the muḍāf ilayh in generality
# and particularity, nor more particular than it absolutely. Two kinds: the MAʿNAWIYYA (the muḍāf is not an adjective annexed to its
# governed word: غُلَامِ زَيْدٍ، ضَارِبِ عَمْرٍو أَمْسِ; its condition the muḍāf bare of definiteness; in the sense of مِنْ when the muḍāf ilayh
# is a genus that covers the muḍāf and more — خَاتَمِ فِضَّةٍ — or of the lām elsewhere, which is commoner — غُلَامِ زَيْدٍ، رَأْسِ عَمْرٍو; it
# makes definite when the muḍāf ilayh is definite and the muḍāf is not غَيْر, its like, or مِثْل, which are never made definite by
# annexation), and the LAFẒIYYA (an adjective annexed to its governed word, lightening the utterance only: ضَارِبِ زَيْدٍ، حَسَنِ الْوَجْهِ،
# مَعْمُولِ الدَّارِ، الضَّارِبَا زَيْدٍ، الضَّارِبُو زَيْدٍ; الضَّارِبِ زَيْدٍ barred for no lightening, الضَّارِبُ الرَّجُلِ allowed on the analogy of
# الْحَسَنُ الْوَجْهِ, whose origin is الْحَسَنُ وَجْهُهُ). Print pp. 110–111.
#   python3 author_izhar_ch14.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-mudaf-wa-nawa-al-idafa"
K12 = "shurut-amal-ism-al-fail"
TITLE = {"ar": "الِاسْمُ الْمُضَافُ وَنَوْعَا الْإِضَافَةِ", "en": "The annexed noun and the two kinds of annexation", "tr": "Muzâf isim ve izâfetin iki türü"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
MM = "maful-mutlaq"; HL = "hal"; HV = "hollow-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; F8 = "form-viii-verbs"; NQ = "naqis-verbs"; MSD = "masdar"; LN = "la-nafiya"; SH = "in-shartiyya"; IN = "inna-wa-akhawatuha"; SM = "sifa-mushabbaha"; IL = "idafa-lafziyya"; TB = "tarif-bil-idafa"; JMS = "jam-mudhakkar-salim"; MQ = "ism-maqsur-manqus"; MST = "istithna"; LT = "anwa-al-lam-al-tarif"; MFL = "maful-lah"; BD = "badal"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«… gibi» — hazfedilmiş mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def ex_head(form, lex, en, tr, joined=False, punct=None, tags=(), segments=None):
    """an annexing head quoted after نَحْوُ: (in jarr as the mudaf ilayh of نَحْو, itself a mudaf)"""
    return tok(form, lex, "noun", [K, ID, HT] + ([AT] if joined else []) + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "لَفْظٌ مَحْكِيٌّ: " + ("مَعْطُوفٌ عَلَى الْأَوَّلِ مَجْرُورٌ" if joined else "مُضَافٌ إِلَيْهِ مَجْرُورٌ") + "، مُضَافٌ.", en, tr, punct=punct, segments=segments)
def ex_member(form, lex, en, tr, punct=None, tags=(), role="مُضَافٌ إِلَيْهِ مَجْرُورٌ"): return tok(form, lex, "noun" if lex != "zayd" and lex != "amr-name" else "propn", [K, ID] + list(tags), role + ".", en, tr, punct=punct)
def mudaf_tok(form, role_ar, en, tr, punct=None, tags=(), segments=None): return tok(form, "mudaf", "noun", [K] + list(tags), role_ar, en, tr, punct=punct, segments=segments)
def yakuna(role="فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ"): return tok("يَكُونَ", "kana", "verb", [K, KN, AM], role + ".", "«it be» — naṣb by an.", "«olmak» — en ile mansûb.")

# ----------- s1 — the seventh: the annexed noun and its condition
S.append({"id": "s1", "translation": {"en": "And the seventh is the ANNEXED NOUN; it governs jarr, and its condition is that it be a noun bare of its tanwīn and of what stands for it, for the sake of the annexation, and that it not be equal to the muḍāf ilayh in generality and particularity, nor more particular than it absolutely.", "tr": "Yedincisi MUZÂF İSİM'dir; cer ameli yapar; şartı, izâfet için tenvininden ve tenvinin nâibinden yalın bir isim olması, muzâfun ileyhe umum ve hususta müsâvi olmaması ve mutlak olarak ondan ehass olmamasıdır."},
 "tokens": [
  tok("وَالسَّابِعُ", "sabi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the seventh» — the mubtada.", "«yedincisi» — mübtedâ.", segments=wa("السَّابِعُ", "sabi", "noun")),
  tok("الِاسْمُ", "ism", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the noun» — the khabar.", "«isim» — haber."),
  mudaf_tok("الْمُضَافُ", "نَعْتٌ مَرْفُوعٌ — الِاسْمُ الْمُضَافُ: الْعَامِلُ السَّابِعُ.", "«annexed» — a naʿt: the annexed noun, the seventh governor.", "«muzâf» — na't: muzâf isim, yedinci âmil.", punct="،", tags=[NA, ID, IMF]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("يَعْمَلُ", "amila", "verb", [K, MK, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«works» — the khabar clause.", "«amel eder» — haber cümlesi."),
  tok("الْجَرَّ", "jarr", "noun", [K, MB, MSD], "مَفْعُولٌ بِهِ مَنْصُوبٌ (أَوْ مَفْعُولٌ مُطْلَقٌ) — عَمَلُ الْجَرِّ.", "«jarr» — the object: the work of jarr.", "«cer» — mef'ûl: cer ameli.", punct="،"),
  tok("وَشَرْطُهُ", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its condition» — a mubtada.", "«ve şartı» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the an-clause the khabar.", "«-ması» — en cümlesi haber."),
  yakuna(role="فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ"),
  tok("اسْمًا", "ism", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«a noun» — the khabar.", "«bir isim» — haber."),
  tok("مُجَرَّدًا", "mujarrad", "noun", [K, NA, IMF], "نَعْتٌ مَنْصُوبٌ.", "«bare» — a naʿt.", "«yalın» — na't."),
  tok("عَنْ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("تَنْوِينِهِ", "tanwin", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its tanwīn»", "«tenvininden»", segments=[seg("تَنْوِينِ", "tanwin", "noun"), pr3msi()]),
  tok("وَنَائِبِهِ", "naib", "noun", [K, AT, ID, JMS, MTH], "الْوَاوُ عَاطِفَةٌ، وَنَائِبِهِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — نُونُ التَّثْنِيَةِ وَالْجَمْعِ.", "«and of what stands for it» — the nūn of the dual and the plural.", "«ve nâibinden» — tesniye ve cem' nûnu.", segments=[seg("وَ", "wa", "conj"), seg("نَائِبِ", "naib", "noun"), pr3msi()]),
  tok("لِأَجْلِ", "ajl", "noun", [K, HJ, ID, MFL], "اللَّامُ حَرْفُ جَرٍّ، وَأَجْلِ مَجْرُورٌ، مُضَافٌ — لِلتَّعْلِيلِ.", "«for the sake of»", "«… için»", segments=[seg("لِ", "li", "prep"), seg("أَجْلِ", "ajl", "noun")]),
  tok("الْإِضَافَةِ", "idafa", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the annexation»", "«izâfet»", punct="،"),
  tok("وَأَنْ", "an-masdariyya", "part", [K, AT, AM], "الْوَاوُ عَاطِفَةٌ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — مَعْطُوفٌ عَلَى الْأَوَّلِ.", "«and that»", "«ve … -ması»", segments=wa("أَنْ", "an-masdariyya", "part")),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«değil»"),
  yakuna(role="فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ"),
  tok("مُسَاوِيًا", "musawin", "noun", [K, KN, MQ, IFA], "خَبَرُ يَكُونَ مَنْصُوبٌ — مَنْقُوصٌ ظَهَرَتْ فَتْحَتُهُ.", "«equal» — the khabar; the manqūṣ shows its fatḥa.", "«müsâvi» — haber; mankûsun fethası görünür."),
  mudaf_tok("لِلْمُضَافِ", "اللَّامُ حَرْفُ جَرٍّ، وَالْمُضَافِ مَجْرُورٌ.", "«to the muḍāf»", "«muzâfa»", tags=[HJ, ID], segments=[seg("لِ", "li", "prep"), seg("الْمُضَافِ", "mudaf", "noun")]),
  tok("إِلَيْهِ", "ilayhi", "part", [K, HJ, ID], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْمُضَافُ إِلَيْهِ.", "«to it» — the muḍāf ilayh.", "«ileyh» — muzâfun ileyh.", segments=[seg("إِلَى", "ila", "prep"), pr3msi()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْعُمُومِ", "umum", "noun", [K, HJ, MSD], "مَجْرُورٌ بِفِي.", "«generality»", "«umumda»"),
  tok("وَالْخُصُوصِ", "khusus", "noun", [K, AT, MSD], "الْوَاوُ عَاطِفَةٌ، وَالْخُصُوصِ مَعْطُوفٌ مَجْرُورٌ.", "«and particularity»", "«ve hususta»", segments=wa("الْخُصُوصِ", "khusus", "noun")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor»", "«ne de»", segments=wa("لَا", "la-nafiya", "part")),
  tok("أَخَصَّ", "akhass", "noun", [K, AT, "ism-tafdil", "mamnu-min-sarf"], "مَعْطُوفٌ عَلَى مُسَاوِيًا مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more particular» — joined to «equal»; a diptote elative.", "«ehass» — müsâviyen'e ma'tûf; gayr-i munsarif ism-i tafdîl."),
  tok("مِنْهُ", "min", "prep", [K, HJ, "ism-tafdil"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«than it»", "«ondan»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, HL, IMF], "حَالٌ مَنْصُوبٌ.", "«absolutely» — a ḥāl.", "«mutlak olarak» — hâl.", punct="."),
 ]})
# ----------- s2 — two kinds
S.append({"id": "s2", "translation": {"en": "And it is of two kinds: maʿnawiyya and lafẓiyya.", "tr": "Ve o iki türdür: ma'nevî ve lafzî."},
 "tokens": [
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْإِضَافَةُ.", "«and it» — the annexation, the mubtada.", "«ve o» — izâfet, mübtedâ.", segments=wa("هِيَ", "hiya", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the jarr phrase the khabar.", "«üzere» — câr-mecrûr haber."),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two kinds»", "«iki tür»", punct=":"),
  tok("مَعْنَوِيَّةٌ", "manawi", "noun", [K, MK, BD], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ (أَحَدُهُمَا) مَرْفُوعٌ — أَوْ بَدَلُ تَفْصِيلٍ.", "«maʿnawiyya» — the first kind: a khabar of «one of them».", "«ma'nevî» — birinci tür.", ),
  tok("وَلَفْظِيَّةٌ", "lafzi", "noun", [K, AT, BD], "الْوَاوُ عَاطِفَةٌ، وَلَفْظِيَّةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and lafẓiyya»", "«ve lafzî»", punct=".", segments=wa("لَفْظِيَّةٌ", "lafzi", "noun")),
 ]})
# ----------- s3 — the maʿnawiyya and its condition
S.append({"id": "s3", "translation": {"en": "The maʿnawiyya is that the muḍāf is not an adjective annexed to its governed word — as in «Zayd's servant», «the one who struck ʿAmr yesterday» — and its condition is that the muḍāf be stripped of definiteness.", "tr": "Ma'nevî olan, muzâfın ma'mûlüne muzâf bir sıfat olmamasıdır — «Zeyd'in kölesi», «dün Amr'a vuran» gibi — ve şartı muzâfın ta'rîften soyulmasıdır."},
 "tokens": [
  tok("فَالْمَعْنَوِيَّةُ", "manawi", "noun", [K, AT, MK], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمَعْنَوِيَّةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the maʿnawiyya» — the mubtada.", "«ma'nevî olan» — mübtedâ.", segments=fa("الْمَعْنَوِيَّةُ", "manawi", "noun")),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the an-clause the khabar.", "«-ması» — en cümlesi haber."),
  yakuna(),
  mudaf_tok("الْمُضَافُ", "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the muḍāf» — the ism of yakūna.", "«muzâf» — yekûne'nin ismi.", tags=[KN, ID]),
  tok("غَيْرَ", "ghayr", "noun", [K, KN, ID], "خَبَرُ يَكُونَ مَنْصُوبٌ، مُضَافٌ.", "«not» — the khabar, annexed.", "«… olmayan» — haber, muzâf."),
  tok("صِفَةٍ", "sifa", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«an adjective»", "«sıfat»"),
  mudaf_tok("مُضَافَةٍ", "نَعْتٌ لِصِفَةٍ مَجْرُورٌ.", "«annexed» — a naʿt of «adjective».", "«muzâf» — sıfatın na'ti.", tags=[NA, ID, IMF]),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْمُولِهَا", "mamul", "noun", [K, HJ, ID, IMF], "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its governed word»", "«ma'mûlüne»", punct="،", segments=[seg("مَعْمُولِ", "mamul", "noun"), pr3fs()]),
  nahw(),
  ex_head("غُلَامِ", "ghulam", "«the servant of» — the example's head, annexed.", "«kölesi» — örneğin muzâfı."),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'in»"),
  ex_head("وَضَارِبِ", "darib", "«and the striker of» — an adjective annexed to a word it does NOT govern (the sense is past: a maʿnawiyya)", "«ve vuran» — amel etmediği kelimeye muzâf sıfat (mânâ mâzî: ma'nevî)", joined=True, tags=[IFA], segments=wa("ضَارِبِ", "darib", "noun")),
  ex_member("عَمْرٍو", "amr-name", "«ʿAmr»", "«Amr'ın»"),
  tok("أَمْسِ", "ams", "noun", [K, MF, "al-murab-wal-mabni-wal-irab"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ — بِهِ يَتَبَيَّنُ أَنَّ ضَارِبًا بِمَعْنَى الْمَاضِي.", "«yesterday» — a built ẓarf: the striking is past, so the annexation is maʿnawiyya.", "«dün» — mebnî zarf: vurma mâzîdir, izâfet ma'nevîdir.", punct="،"),
  tok("وَشَرْطُهَا", "shart", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its condition» — a mubtada.", "«ve şartı» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("شَرْطُ", "shart", "noun"), pr3fs()]),
  tok("تَجْرِيدُ", "tajrid", "noun", [K, MK, ID, MSD], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ جَرَّدَ.", "«the stripping of» — the khabar, annexed.", "«soyulması» — haber, muzâf."),
  mudaf_tok("الْمُضَافِ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَفْعُولُ الْمَصْدَرِ.", "«the muḍāf» — the maṣdar's object.", "«muzâfın» — mastarın mef'ûlü.", tags=[ID]),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("التَّعْرِيفِ", "tarif", "noun", [K, HJ, MSD, TB], "مَجْرُورٌ بِمِنْ — أَيْ مِنَ اللَّامِ.", "«definiteness» — the article.", "«ta'rîften» — lâmdan.", punct="."),
 ]})
# ----------- s4 — in the sense of مِنْ or of the lām
S.append({"id": "s4", "translation": {"en": "And it is either in the sense of مِنْ, if the muḍāf ilayh is a genus that includes the muḍāf and others — as in «a ring of silver» — or in the sense of the lām elsewhere, and that is the commoner — as in «Zayd's servant», «ʿAmr's head».", "tr": "Ve o ya min mânâsındadır — muzâfun ileyh muzâfı ve başkasını kapsayan bir cins ise — «gümüş yüzük» gibi; ya da başka yerde lâm mânâsındadır, ki bu daha çoktur — «Zeyd'in kölesi», «Amr'ın başı» gibi."},
 "tokens": [
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هِيَ", "hiya", "pron")),
  tok("إِمَّا", "imma", "part", [K, AT], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MK, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in the sense of» — the khabar.", "«mânâsında» — haber.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("مِنْ", "min", "prep", [K, HT, ID], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ: حَرْفُ مِنْ.", "«min» — the letter mentioned as a word.", "«min» — lafzı kastedilen harf."),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "شَرْطِيَّةٌ جَازِمَةٌ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, KN, SH], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«is» — the shart verb.", "«ise» — şart fiili."),
  mudaf_tok("الْمُضَافُ", "اسْمُ كَانَ مَرْفُوعٌ.", "«the muḍāf» — the ism of kāna.", "«muzâf» — kâne'nin ismi.", tags=[KN, ID]),
  tok("إِلَيْهِ", "ilayhi", "part", [K, HJ, ID], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْمُضَافُ إِلَيْهِ.", "«to it» — the muḍāf ilayh.", "«ileyh» — muzâfun ileyh.", segments=[seg("إِلَى", "ila", "prep"), pr3msi()]),
  tok("جِنْسًا", "jins", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a genus» — the khabar.", "«bir cins» — haber."),
  tok("شَامِلًا", "shamil", "noun", [K, NA, IFA], "نَعْتٌ مَنْصُوبٌ — اسْمُ فَاعِلٍ عَامِلٌ.", "«including» — a naʿt: an ism fāʿil that governs.", "«kapsayan» — na't: amel eden ism-i fâil."),
  mudaf_tok("لِلْمُضَافِ", "اللَّامُ حَرْفُ جَرٍّ، وَالْمُضَافِ مَجْرُورٌ — مُتَعَلِّقٌ بِشَامِلًا.", "«the muḍāf» — hanging on «including».", "«muzâfı» — şâmilen'e müteallik.", tags=[HJ, ID], segments=[seg("لِ", "li", "prep"), seg("الْمُضَافِ", "mudaf", "noun")]),
  tok("وَغَيْرِهِ", "ghayr", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرِهِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and others»", "«ve başkasını»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  nahw(),
  ex_head("خَاتَمِ", "khatam", "«a ring of» — the example's head: the ring is OF silver (the sense of min).", "«yüzüğü» — örneğin muzâfı: yüzük gümüşTEN (min mânâsı)."),
  ex_member("فِضَّةٍ", "fidda", "«silver» — the genus.", "«gümüş» — cins.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, AT, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مَعْطُوفٌ عَلَى الْخَبَرِ.", "«in the sense of»", "«mânâsında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("اللَّامِ", "lam-letter", "noun", [K, ID, LT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَامِ الْمِلْكِ وَالِاخْتِصَاصِ.", "«the lām» — the lām of possession.", "«lâm» — mülkiyet lâmı."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("غَيْرِهِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — فِي غَيْرِ ذٰلِكَ.", "«elsewhere»", "«başka yerde»", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْأَكْثَرُ", "akthar", "noun", [K, MK, "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ.", "«the commoner» — the khabar.", "«daha çok olan» — haber.", punct="،"),
  nahw(),
  ex_head("غُلَامِ", "ghulam", "«the servant of»", "«kölesi»"),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'in»"),
  ex_head("وَرَأْسِ", "ras", "«and the head of»", "«ve başı»", joined=True, segments=wa("رَأْسِ", "ras", "noun")),
  ex_member("عَمْرٍو", "amr-name", "«ʿAmr»", "«Amr'ın»", punct="."),
 ]})
# ----------- s5 — it makes definite, save غَيْر and its like
S.append({"id": "s5", "translation": {"en": "And it gives definiteness if the muḍāf ilayh is definite and the muḍāf is not غَيْر, its like, or مِثْل — for these are not made definite by annexation — as in «Zayd's servant».", "tr": "Muzâfun ileyh ma'rife ise ve muzâf gayr, benzeri veya misl değilse ta'rîf ifade eder — çünkü bunlar izâfetle ma'rife olmaz — «Zeyd'in kölesi» gibi."},
 "tokens": [
  tok("وَتُفِيدُ", "afada", "verb", [K, AT, FL, F4, HV], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتُفِيدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ (الْإِضَافَةُ).", "«and it gives» — the annexation its doer.", "«ve ifade eder» — fâili izâfet.", segments=wa("تُفِيدُ", "afada", "verb")),
  tok("تَعْرِيفًا", "tarif", "noun", [K, MB, MSD, TB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«definiteness» — the object.", "«ta'rîf» — mef'ûl."),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "شَرْطِيَّةٌ جَازِمَةٌ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, KN, SH], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«is» — the shart verb.", "«ise» — şart fiili."),
  mudaf_tok("الْمُضَافُ", "اسْمُ كَانَ مَرْفُوعٌ.", "«the muḍāf» — the ism of kāna.", "«muzâf» — kâne'nin ismi.", tags=[KN, ID]),
  tok("إِلَيْهِ", "ilayhi", "part", [K, HJ, ID], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْمُضَافُ إِلَيْهِ.", "«to it» — the muḍāf ilayh.", "«ileyh» — muzâfun ileyh.", segments=[seg("إِلَى", "ila", "prep"), pr3msi()]),
  tok("مَعْرِفَةً", "marifa", "noun", [K, KN, TB], "خَبَرُ كَانَ مَنْصُوبٌ.", "«definite» — the khabar.", "«ma'rife» — haber."),
  mudaf_tok("وَالْمُضَافُ", "الْوَاوُ لِلْحَالِ، وَالْمُضَافُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the muḍāf» — a mubtada (a ḥāl clause).", "«ve muzâf» — mübtedâ (hâl cümlesi).", tags=[AT, MK, ID], segments=wa("الْمُضَافُ", "mudaf", "noun")),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — وَقُرِئَ بِالنَّصْبِ عَلَى الْحَالِ.", "«other than» — read in naṣb as the ḥāl of the muḍāf; annexed.", "«… dışında» — muzâfın hâli olarak mansûb; muzâf."),
  tok("غَيْرٍ", "ghayr", "noun", [K, ID, HT, TB], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ إِلَيْهِ مَجْرُورٌ — كَلِمَةُ غَيْرٍ.", "«ghayr» — the word mentioned.", "«gayr» — lafız olarak."),
  tok("وَشِبْهِهِ", "shibh", "noun", [K, AT, ID, TB], "الْوَاوُ عَاطِفَةٌ، وَشِبْهِهِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — نَحْوُ سِوًى.", "«and its like» — such as سِوَى.", "«ve benzeri» — sivâ gibi.", segments=[seg("وَ", "wa", "conj"), seg("شِبْهِ", "shibh", "noun"), pr3msi()]),
  tok("وَمِثْلٍ", "mithl", "noun", [K, AT, HT, TB], "الْوَاوُ عَاطِفَةٌ، وَمِثْلٍ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ مَجْرُورٌ.", "«and mithl» — the word mentioned.", "«ve misl» — lafız olarak.", punct="،", segments=wa("مِثْلٍ", "mithl", "noun")),
  tok("فَإِنَّهَا", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا فِي مَحَلِّ نَصْبٍ — هٰذِهِ الْكَلِمَاتُ.", "«for they» — inna with its pronoun ism.", "«çünkü onlar» — inne, zamir ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3fs()]),
  tok("لَا", "la-nafiya", "part", [K, LN], "نَافِيَةٌ.", "«not»", "«-maz»"),
  tok("تَتَعَرَّفُ", "taarrafa", "verb", [K, IN, F5, TB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«become definite» — the khabar of inna.", "«ma'rife olur» — inne'nin haberi."),
  tok("بِالْإِضَافَةِ", "idafa", "noun", [K, HJ, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَالْإِضَافَةِ مَجْرُورٌ.", "«by annexation»", "«izâfetle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْإِضَافَةِ", "idafa", "noun")]),
  nahw(),
  ex_head("غُلَامِ", "ghulam", "«the servant of» — made definite by Zayd.", "«kölesi» — Zeyd ile ma'rife."),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'in»", punct="."),
 ]})
# ----------- s6 — the lafẓiyya
S.append({"id": "s6", "translation": {"en": "And the lafẓiyya is that the muḍāf is an adjective annexed to its governed word; it gives nothing but a lightening in the utterance — as in «the striker of Zayd», «the handsome of face», «the one at work in the house», «the two strikers of Zayd», «the strikers of Zayd».", "tr": "Lafzî olan, muzâfın ma'mûlüne muzâf bir sıfat olmasıdır; lafızda hafiflikten başka bir şey ifade etmez — «Zeyd'e vuran», «yüzü güzel», «evde çalışan», «Zeyd'e vuran ikisi», «Zeyd'e vuranlar» gibi."},
 "tokens": [
  tok("وَاللَّفْظِيَّةُ", "lafzi", "noun", [K, AT, MK, IL], "الْوَاوُ عَاطِفَةٌ، وَاللَّفْظِيَّةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the lafẓiyya» — the mubtada.", "«lafzî olan» — mübtedâ.", segments=wa("اللَّفْظِيَّةُ", "lafzi", "noun")),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the an-clause the khabar.", "«-ması» — en cümlesi haber."),
  yakuna(),
  mudaf_tok("الْمُضَافُ", "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the muḍāf» — the ism of yakūna.", "«muzâf» — yekûne'nin ismi.", tags=[KN, ID]),
  tok("صِفَةً", "sifa", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«an adjective» — the khabar.", "«sıfat» — haber."),
  mudaf_tok("مُضَافَةً", "نَعْتٌ لِصِفَةً مَنْصُوبٌ.", "«annexed» — a naʿt.", "«muzâf» — na't.", tags=[NA, ID, IMF]),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْمُولِهَا", "mamul", "noun", [K, HJ, ID, IMF], "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its governed word»", "«ma'mûlüne»", punct="،", segments=[seg("مَعْمُولِ", "mamul", "noun"), pr3fs()]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("تُفِيدُ", "afada", "verb", [K, FL, F4, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«gives»", "«ifade eder»"),
  tok("إِلَّا", "illa", "part", [K, MST, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«but»", "«-den başka»"),
  tok("تَخْفِيفًا", "takhfif", "noun", [K, MB, MSD, IL], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a lightening» — the object.", "«hafiflik» — mef'ûl."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("اللَّفْظِ", "lafz", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the utterance»", "«lafızda»", punct="،"),
  nahw(),
  ex_head("ضَارِبِ", "darib", "«the striker of» — an adjective annexed to its object: lafẓiyya.", "«vuranı» — mef'ûlüne muzâf sıfat: lafzî.", tags=[IFA, IL]),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'e»"),
  ex_head("وَحَسَنِ", "hasan-adj", "«and the handsome of» — the ṣifa mushabbaha annexed to its doer.", "«ve güzeli» — fâiline muzâf sıfat-ı müşebbehe.", joined=True, tags=[SM, IL], segments=wa("حَسَنِ", "hasan-adj", "noun")),
  ex_member("الْوَجْهِ", "wajh", "«the face»", "«yüzü»"),
  ex_head("وَمَعْمُولِ", "mamul", "«and the one at work in» — the ism mafʿūl annexed to its deputy-doer.", "«ve işleneni» — nâib-i fâiline muzâf ism-i mef'ûl.", joined=True, tags=[IMF, IL], segments=wa("مَعْمُولِ", "mamul", "noun")),
  ex_member("الدَّارِ", "dar", "«the house»", "«evin»"),
  tok("وَالضَّارِبَا", "darib", "noun", [K, AT, ID, HT, MTH, IL], "الْوَاوُ عَاطِفَةٌ، وَالضَّارِبَا لَفْظٌ مَحْكِيٌّ: مَعْطُوفٌ مَجْرُورٌ فِي الْمَحَلِّ — مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«and the two strikers of» — the dual with its nūn dropped for the annexation.", "«ve iki vuranı» — izâfet için nûnu düşmüş tesniye.", segments=wa("الضَّارِبَا", "darib", "noun")),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'e»"),
  tok("وَالضَّارِبُو", "darib", "noun", [K, AT, ID, HT, JMS, IL], "الْوَاوُ عَاطِفَةٌ، وَالضَّارِبُو لَفْظٌ مَحْكِيٌّ: مَعْطُوفٌ مَجْرُورٌ فِي الْمَحَلِّ — جَمْعٌ مُذَكَّرٌ سَالِمٌ حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«and the strikers of» — the sound plural with its nūn dropped.", "«ve vuranları» — nûnu düşmüş cem'-i müzekker sâlim.", segments=wa("الضَّارِبُو", "darib", "noun")),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'e»", punct="."),
 ]})
# ----------- s7 — the barred and the allowed
S.append({"id": "s7", "translation": {"en": "And the like of «the striker of Zayd» (with the article on the singular) is barred, for want of lightening; while «the striker of the man» is allowed, on the analogy of «the handsome of the face», whose origin is «the handsome his face».", "tr": "«ed-Dâribi Zeydin» gibisi, hafiflik olmadığından yasaktır; «ed-Dâribü'r-raculi» ise «el-Hasenü'l-vechi»ye kıyasla câizdir — onun aslı «el-Hasenü vechühu»dur."},
 "tokens": [
  tok("وَامْتَنَعَ", "imtanaa", "verb", [K, AT, FL, F8], "الْوَاوُ لِلِاسْتِئْنَافِ، وَامْتَنَعَ فِعْلٌ مَاضٍ.", "«and … is barred»", "«ve … yasaktır»", segments=wa("امْتَنَعَ", "imtanaa", "verb")),
  tok("نَحْوُ", "nahw", "noun", [K, FL, ID, HT], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ إِلَى الْمِثَالِ.", "«the like of» — the doer, annexed to the example.", "«… gibisi» — fâil, örneğe muzâf.", punct=":"),
  tok("الضَّارِبِ", "darib", "noun", [K, ID, HT, IFA, LT], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — اسْمُ فَاعِلٍ مُفْرَدٌ بِاللَّامِ، مُضَافٌ.", "«the striker of» — the singular with the article.", "«vuranı» — lâmlı müfred.", ),
  ex_member("زَيْدٍ", "zayd", "«Zayd»", "«Zeyd'e»"),
  tok("لِعَدَمِ", "adam", "noun", [K, HJ, ID, MFL], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَعَدَمِ مَجْرُورٌ، مُضَافٌ.", "«for want of» — the lām of cause.", "«… olmadığından» — ta'lîl lâmı.", segments=[seg("لِ", "li", "prep"), seg("عَدَمِ", "adam", "noun")]),
  tok("التَّخْفِيفِ", "takhfif", "noun", [K, ID, MSD, IL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَا تَنْوِينَ يُحْذَفُ مَعَ اللَّامِ.", "«lightening» — no tanwīn to drop under the article.", "«hafiflik» — lâm varken düşecek tenvin yok.", punct="،"),
  tok("وَجَازَ", "jaaza", "verb", [K, AT, FL, HV], "الْوَاوُ عَاطِفَةٌ، وَجَازَ فِعْلٌ مَاضٍ.", "«and … is allowed»", "«ve … câizdir»", segments=wa("جَازَ", "jaaza", "verb")),
  tok("الضَّارِبُ", "darib", "noun", [K, FL, ID, HT, IFA, LT], "لَفْظٌ مَحْكِيٌّ: فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the striker of» — the doer of «is allowed».", "«vuranı» — câze'nin fâili."),
  tok("الرَّجُلِ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مُضَافٌ إِلَيْهِ بِاللَّامِ، فَيَخِفُّ.", "«the man» — a muḍāf ilayh with the article: the nūn would have dropped.", "«adamı» — lâmlı muzâfun ileyh."),
  tok("حَمْلًا", "haml", "noun", [K, MFL, MSD], "مَفْعُولٌ لَهُ مَنْصُوبٌ.", "«by analogy» — the object of cause.", "«kıyasla» — mef'ûlün leh."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("الْحَسَنِ", "hasan-adj", "noun", [K, HJ, ID, HT, SM, LT], "لَفْظٌ مَحْكِيٌّ: مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«the handsome of»", "«güzeli»"),
  tok("الْوَجْهِ", "wajh", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the face»", "«yüzü»", punct="،"),
  tok("أَصْلُهُ", "asl", "noun", [K, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its origin» — the mubtada.", "«aslı» — mübtedâ.", segments=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  tok("الْحَسَنُ", "hasan-adj", "noun", [K, MK, HT, SM], "لَفْظٌ مَحْكِيٌّ: خَبَرٌ مَرْفُوعٌ — الصِّفَةُ الْمُشَبَّهَةُ رَافِعَةً فَاعِلَهَا.", "«the handsome» — the khabar: the ṣifa mushabbaha raising its doer.", "«güzel» — haber: fâilini ref eden sıfat-ı müşebbehe."),
  tok("وَجْهُهُ", "wajh", "noun", [K, FL, ID, SM], "فَاعِلٌ لِلْحَسَنُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his face» — the doer.", "«yüzü» — fâil.", punct=".", segments=[seg("وَجْهُ", "wajh", "noun"), pr3ms()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

CAND = {
 "sabi": G("sabi", "سَابِع", "س ب ع", "noun", "seventh", "yedinci", 2),
 "ism": G("ism", "اِسْم", "س م و", "noun", "noun; name", "isim", 1, plural="أَسْمَاء"),
 "mudaf": G("mudaf", "مُضَاف", "ض ي ف", "noun", "annexed (the muḍāf, the first term of an iḍāfa)", "muzâf (izâfetin birinci terimi)", 2),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to work, to act; (of a governor) to govern", "çalışmak, yapmak; (âmil) amel etmek", 1),
 "jarr": G("jarr", "جَرّ", "ج ر ر", "noun", "the genitive (jarr)", "cer (-in hâli)", 2),
 "shart": G("shart", "شَرْط", "ش ر ط", "noun", "condition", "şart", 2, plural="شُرُوط"),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "to, that (the masdar particle that puts the muḍāriʿ in naṣb)", "-mesi, -mek (muzâriyi nasb eden mastar harfi)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak, idi", 1),
 "mujarrad": G("mujarrad", "مُجَرَّد", "ج ر د", "noun", "bare, stripped of", "mücerred, yalın", 3),
 "an": G("an", "عَنْ", None, "prep", "from, about, of", "-den, hakkında", 1),
 "tanwin": G("tanwin", "تَنْوِين", "ن و ن", "noun", "tanwīn (nunation)", "tenvin", 2),
 "naib": G("naib", "نَائِب", "ن و ب", "noun", "deputy, substitute", "nâib, vekil", 3),
 "ajl": G("ajl", "أَجْل", "أ ج ل", "noun", "sake — لِأَجْلِ for the sake of", "uğur — li-ecli … için", 2),
 "idafa": G("idafa", "إِضَافَة", "ض ي ف", "noun", "annexation (iḍāfa, the construct)", "izâfet (isim tamlaması)", 2),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (negation)", "değil, -mez (nefiy)", 1),
 "musawin": G("musawin", "مُسَاوٍ", "س و ي", "noun", "equal (to)", "müsâvi, eşit", 3),
 "ilayhi": G("ilayhi", "إِلَيْهِ", None, "part", "to him, to it", "ona", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "umum": G("umum", "عُمُوم", "ع م م", "noun", "generality", "umum, genellik", 3),
 "khusus": G("khusus", "خُصُوص", "خ ص ص", "noun", "particularity, specificity", "husus, özellik", 3),
 "akhass": G("akhass", "أَخَصّ", "خ ص ص", "noun", "more particular (elative)", "daha hususî, ehass", 3),
 "min": G("min", "مِنْ", None, "prep", "from, of; than", "-den", 1),
 "mutlaq": G("mutlaq", "مُطْلَق", "ط ل ق", "noun", "absolute, unrestricted", "mutlak", 3),
 "hiya": G("hiya", "هِيَ", None, "pron", "she, it", "o (diş.)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, -e", 1),
 "naw": G("naw", "نَوْع", "ن و ع", "noun", "kind, sort", "nev', tür", 2),
 "manawi": G("manawi", "مَعْنَوِيّ", "ع ن ي", "noun", "of meaning (maʿnawī)", "ma'nevî", 3),
 "lafzi": G("lafzi", "لَفْظِيّ", "ل ف ظ", "noun", "of utterance, verbal (lafẓī)", "lafzî", 3),
 "sifa": G("sifa", "صِفَة", "و ص ف", "noun", "adjective, attribute (ṣifa)", "sıfat", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e, -a", 1),
 "mamul": G("mamul", "الْمَعْمُول", "ع م ل", "noun", "the governed word (maʿmūl)", "ma'mûl — amel edilen kelime", 3),
 "nahw": G("nahw", "نَحْو", "ن ح و", "noun", "like, such as; grammar", "gibi; nahiv", 2),
 "ghulam": G("ghulam", "غُلَام", "غ ل م", "noun", "boy, servant", "oğlan, köle", 1, plural="غِلْمَان"),
 "zayd": G("zayd", "زَيْد", None, "propn", "Zayd (the grammarians' stock name)", "Zeyd (nahivcilerin örnek adı)", 1),
 "darib": G("darib", "ضَارِب", "ض ر ب", "noun", "striking, a striker (ism fāʿil of ḍaraba)", "vuran, vurucu (darabe'nin ism-i fâili)", 2),
 "amr-name": G("amr-name", "عَمْرو", None, "propn", "ʿAmr (the grammarians' second stock name)", "Amr (nahivcilerin ikinci örnek adı)", 1),
 "ams": G("ams", "أَمْسِ", None, "noun", "yesterday (built on the kasra)", "dün (kesre üzere mebnî)", 2),
 "tajrid": G("tajrid", "تَجْرِيد", "ج ر د", "noun", "stripping, divesting", "tecrîd, soyma", 3),
 "tarif": G("tarif", "تَعْرِيف", "ع ر ف", "noun", "definiteness; making definite", "ta'rîf, belirlilik", 2),
 "imma": G("imma", "إِمَّا", None, "part", "either … (or)", "ya … (ya da)", 2),
 "mana": G("mana", "مَعْنًى", "ع ن ي", "noun", "meaning, sense", "mânâ", 2, plural="مَعَانٍ"),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (the conditional particle)", "eğer (şart edatı)", 2),
 "jins": G("jins", "جِنْس", "ج ن س", "noun", "genus, kind", "cins", 2),
 "shamil": G("shamil", "شَامِل", "ش م ل", "noun", "including, comprehensive", "kapsayan, şâmil", 3),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka, gayr; değil", 1),
 "khatam": G("khatam", "خَاتَم", "خ ت م", "noun", "ring, seal-ring", "yüzük, mühür", 2),
 "fidda": G("fidda", "فِضَّة", "ف ض ض", "noun", "silver", "gümüş", 2),
 "aw": G("aw", "أَوْ", None, "part", "or", "veya", 1),
 "lam-letter": G("lam-letter", "لَام", None, "noun", "the letter lām; the lām (the article, the lām of jarr…)", "lâm harfi; lâm (ta'rîf lâmı, cer lâmı…)", 3),
 "akthar": G("akthar", "أَكْثَر", "ك ث ر", "noun", "more, most", "daha çok, çoğu", 2),
 "ras": G("ras", "رَأْس", "ر أ س", "noun", "head", "baş", 1),
 "afada": G("afada", "أَفَادَ", "ف ي د", "verb", "to give (a meaning), to convey; to benefit", "ifade etmek, kazandırmak; fayda vermek", 2, form="IV"),
 "marifa": G("marifa", "مَعْرِفَة", "ع ر ف", "noun", "a definite noun (maʿrifa); knowledge", "ma'rife (belirli isim); bilgi", 2),
 "shibh": G("shibh", "شِبْه", "ش ب ه", "noun", "the like of, quasi-", "benzeri, şibh", 2),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "like, the like of", "gibi, misli", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed, verily (puts its noun in naṣb)", "muhakkak, şüphesiz (ismini nasb eder)", 1),
 "taarrafa": G("taarrafa", "تَعَرَّفَ", "ع ر ف", "verb", "to become definite; to get to know", "ma'rife olmak; tanımak", 3, form="V"),
 "illa": G("illa", "إِلَّا", None, "part", "except", "-den başka, hariç", 1),
 "takhfif": G("takhfif", "تَخْفِيف", "خ ف ف", "noun", "lightening, alleviation", "hafifletme, tahfîf", 3),
 "lafz": G("lafz", "لَفْظ", "ل ف ظ", "noun", "utterance, wording", "lafız", 2),
 "hasan-adj": G("hasan-adj", "حَسَن", "ح س ن", "noun", "handsome, good", "güzel, iyi", 1),
 "wajh": G("wajh", "وَجْه", "و ج ه", "noun", "face; way, manner", "yüz; vecih, tarz", 2, plural="وُجُوه"),
 "dar": G("dar", "دَار", "د و ر", "noun", "house", "ev", 1, plural="دُور"),
 "imtanaa": G("imtanaa", "اِمْتَنَعَ", "م ن ع", "verb", "to refuse; to be impossible, to be barred", "imtina etmek; mümkün olmamak, yasak olmak", 3, form="VIII"),
 "adam": G("adam", "عَدَم", "ع د م", "noun", "absence, non-existence, want of", "yokluk, adem", 2),
 "jaaza": G("jaaza", "جَازَ", "ج و ز", "verb", "to be permitted", "câiz olmak", 2),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam", 1, plural="رِجَال"),
 "haml": G("haml", "حَمْل", "ح م ل", "noun", "carrying; analogy (ḥaml ʿalā — treating like)", "yüklenme; haml (kıyas)", 3),
 "asl": G("asl", "أَصْل", "أ ص ل", "noun", "origin, root, basis", "asıl, kök", 1, plural="أُصُول"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "taarrafa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَعَرَّف", "تَعَرَّف", "تَعَرَّف", "تَعَرُّف", "مُتَعَرِّف", "مُتَعَرَّف", "تُعُرِّفَ", "يُتَعَرَّفُ", "تَعَرَّفَ يَتَعَرَّفُ تَعَرُّفًا: صَارَ مَعْرِفَةً؛ عَرَفَ شَيْئًا فَشَيْئًا."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch14 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("amila", "kana", "afada", "taarrafa", "imtanaa", "jaaza") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الِاسْمُ الْمُضَافُ عَامِلًا، وَالْإِضَافَةُ الْمَعْنَوِيَّةُ وَاللَّفْظِيَّةُ", "en": "The annexed noun as a governor, and the maʿnawī and lafẓī annexation", "tr": "Âmil olarak muzâf isim; ma'nevî ve lafzî izâfet"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العوامل القياسية: الاسم المضاف", "الكافية لابن الحاجب — المضاف إليه", "قطر الندى لابن هشام — الإضافة المعنوية واللفظية"],
 "amil": "الِاسْمُ الْمُضَافُ — governs jarr in the noun after it (the muḍāf ilayh); its own tanwīn, or the nūn that stands for it, falls for the annexation",
 "question": {
  "en": ["What is the seventh qiyāsī governor? The ANNEXED NOUN — it governs jarr in the noun after it.",
         "What is its condition? That it be a noun stripped of its tanwīn, or of the nūn that stands for it (the dual's and the sound plural's), for the sake of the annexation: غُلَامُ زَيْدٍ, ضَارِبَا زَيْدٍ, ضَارِبُو زَيْدٍ.",
         "What else may it not be? Equal to the muḍāf ilayh in generality and particularity, nor more particular than it absolutely — you do not annex a word to itself.",
         "What are the two kinds? MAʿNAWIYYA — the muḍāf is not an adjective annexed to what it governs (غُلَامُ زَيْدٍ; ضَارِبُ عَمْرٍو أَمْسِ, where the striking is past, so the participle does not govern); LAFẒIYYA — an adjective annexed to its own governed word (ضَارِبُ زَيْدٍ, حَسَنُ الْوَجْهِ, مَعْمُولُ الدَّارِ).",
         "What sense does the maʿnawiyya carry? مِنْ when the muḍāf ilayh is a genus that includes the muḍāf and others (خَاتَمُ فِضَّةٍ — a ring OF silver); the lām elsewhere, and that is the commoner (غُلَامُ زَيْدٍ — the servant belonging TO Zayd).",
         "Does the maʿnawiyya make definite? Yes, when the muḍāf ilayh is definite — except غَيْر, its like (سِوَى) and مِثْل, which annexation never makes definite; and its muḍāf must itself be bare of the article.",
         "What does the lafẓiyya give? Nothing but a lightening of the utterance — the tanwīn or the nūn drops; the sense is unchanged, so its muḍāf may carry the article: الضَّارِبَا زَيْدٍ, الضَّارِبُو زَيْدٍ.",
         "Why is الضَّارِبِ زَيْدٍ barred? A singular with the article has no tanwīn to drop — nothing is lightened; الضَّارِبُ الرَّجُلِ is allowed by analogy with الْحَسَنُ الْوَجْهِ, whose origin is الْحَسَنُ وَجْهُهُ.",
         "What does the engine READ here? The DabtEngine takes the tanwīn or the nūn off the head of a chain and writes jarr on its member, declines the five nouns, the dual and the sound plural by their letters in annexation, and reads an adjective with the article annexed to an article-noun as a lafẓī chain."],
  "tr": ["Yedinci kıyâsî âmil nedir? MUZÂF İSİM — ardındaki isimde (muzâfun ileyh) cer ameli yapar.",
         "Şartı nedir? İzâfet için tenvininden veya tenvinin nâibi olan nûndan (tesniye ve cem'-i sâlim nûnu) soyulmuş bir isim olması: gulâmu Zeydin, dâribâ Zeydin, dâribû Zeydin.",
         "Başka ne olmamalıdır? Muzâfun ileyhe umum ve hususta müsâvi, mutlak olarak ondan ehass olmamalıdır — bir kelime kendisine muzâf olmaz.",
         "İki türü nedir? MA'NEVÎ — muzâf, amel ettiği kelimeye muzâf bir sıfat değildir (gulâmu Zeydin; dâribu Amrin emsi — vurma mâzîdir, sîga amel etmez); LAFZÎ — kendi ma'mûlüne muzâf sıfat (dâribu Zeydin, hasenü'l-vechi, ma'mûlü'd-dâri).",
         "Ma'nevî hangi mânâyı taşır? Muzâfun ileyh, muzâfı ve başkasını kapsayan bir cins ise min (hâtemu fıddatin — gümüşTEN yüzük); başka yerde lâm, ki daha çoktur (gulâmu Zeydin — Zeyd'E ait köle).",
         "Ma'nevî izâfet ma'rife yapar mı? Evet, muzâfun ileyh ma'rife ise — gayr, benzeri (sivâ) ve misl hariç; bunlar izâfetle hiç ma'rife olmaz; muzâfı da lâmdan yalın olmalıdır.",
         "Lafzî izâfet ne verir? Lafızda hafiflikten başka bir şey değil — tenvin veya nûn düşer; mânâ değişmez, bu yüzden muzâfı lâm alabilir: ed-dâribâ Zeydin, ed-dâribû Zeydin.",
         "ed-Dâribi Zeydin neden yasak? Lâmlı müfredin düşecek tenvini yoktur — hiçbir şey hafiflemez; ed-dâribü'r-raculi ise el-hasenü'l-vechi'ye kıyasla câizdir, onun aslı el-hasenü vechühu'dur.",
         "Motor burada neyi OKUR? DabtEngine zincirin başından tenvini veya nûnu kaldırır ve üyesine cer yazar, izâfette beş ismi, tesniyeyi ve cem'-i sâlimi harfleriyle çeker, lâmlı bir isme muzâf lâmlı sıfatı lafzî zincir olarak okur."],
 },
 "plain": {"en": "When one noun leans on another («Zayd's servant»), the first loses its tanwīn and the second takes the -i ending. It can mean «of» (a ring of silver) or «belonging to» (Zayd's servant), and makes the first word definite. When an adjective leans on the word it governs («handsome of face»), nothing changes but the sound.",
           "tr": "Bir isim diğerine dayanınca («Zeyd'in kölesi») birincisi tenvinini kaybeder, ikincisi -i ekini alır. «-den» (gümüşten yüzük) ya da «-e ait» (Zeyd'in kölesi) anlamı taşır ve birinci kelimeyi belirli yapar. Bir sıfat kendi ma'mûlüne dayanınca («yüzü güzel») sesten başka bir şey değişmez."},
 "explanation": {"en": "The seventh qiyāsī governor is the annexed noun; it governs jarr. Its condition is that it be a noun bare of its tanwīn and of what stands for it, for the annexation's sake, and that it not be equal to the muḍāf ilayh in generality and particularity, nor more particular than it absolutely. It is of two kinds. The maʿnawiyya: the muḍāf is not an adjective annexed to its governed word (غُلَامُ زَيْدٍ، ضَارِبُ عَمْرٍو أَمْسِ); its condition is the muḍāf stripped of definiteness; it is in the sense of مِنْ when the muḍāf ilayh is a genus including the muḍāf and others (خَاتَمُ فِضَّةٍ), or of the lām elsewhere, which is commoner (غُلَامُ زَيْدٍ، رَأْسُ عَمْرٍو); it gives definiteness when the muḍāf ilayh is definite and the muḍāf is not غَيْر, its like or مِثْل, which annexation does not make definite. The lafẓiyya: the muḍāf is an adjective annexed to its governed word, and gives nothing but a lightening of the utterance (ضَارِبُ زَيْدٍ، حَسَنُ الْوَجْهِ، مَعْمُولُ الدَّارِ، الضَّارِبَا زَيْدٍ، الضَّارِبُو زَيْدٍ); الضَّارِبِ زَيْدٍ is barred for want of lightening, and الضَّارِبُ الرَّجُلِ is allowed on the analogy of الْحَسَنُ الْوَجْهِ, whose origin is الْحَسَنُ وَجْهُهُ.",
                 "tr": "Yedinci kıyâsî âmil muzâf isimdir; cer ameli yapar. Şartı, izâfet için tenvininden ve tenvinin nâibinden yalın bir isim olması, muzâfun ileyhe umum ve hususta müsâvi olmaması ve mutlak olarak ondan ehass olmamasıdır. İki türdür. Ma'nevî: muzâf, ma'mûlüne muzâf bir sıfat değildir (gulâmu Zeydin, dâribu Amrin emsi); şartı muzâfın ta'rîften soyulmasıdır; muzâfun ileyh muzâfı ve başkasını kapsayan bir cins ise min mânâsında (hâtemu fıddatin), yoksa — ki daha çoktur — lâm mânâsındadır (gulâmu Zeydin, ra'su Amrin); muzâfun ileyh ma'rife ise ve muzâf gayr, benzeri veya misl değilse ta'rîf ifade eder, çünkü bunlar izâfetle ma'rife olmaz. Lafzî: muzâf, ma'mûlüne muzâf bir sıfattır ve lafızda hafiflikten başka bir şey ifade etmez (dâribu Zeydin, hasenü'l-vechi, ma'mûlü'd-dâri, ed-dâribâ Zeydin, ed-dâribû Zeydin); ed-dâribi Zeydin hafiflik olmadığından yasaktır, ed-dâribü'r-raculi ise aslı el-hasenü vechühu olan el-hasenü'l-vechi'ye kıyasla câizdir."},
 "examples": [
  {"ar": "وَشَرْطُهُ أَنْ يَكُونَ اسْمًا مُجَرَّدًا عَنْ تَنْوِينِهِ وَنَائِبِهِ لِأَجْلِ الْإِضَافَةِ", "en": "the muḍāf bare of its tanwīn and of its nūn", "tr": "tenvininden ve nûnundan yalın muzâf", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "غُلَامِ زَيْدٍ وَضَارِبِ عَمْرٍو أَمْسِ", "en": "the maʿnawiyya: a plain noun, and a past-sense participle", "tr": "ma'nevî: düz isim ve mâzî mânâlı sîga", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "خَاتَمِ فِضَّةٍ", "en": "in the sense of min: a ring of silver", "tr": "min mânâsında: gümüşten yüzük", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "غُلَامِ زَيْدٍ وَرَأْسِ عَمْرٍو", "en": "in the sense of the lām: the commoner", "tr": "lâm mânâsında: daha çok olan", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَالْمُضَافُ غَيْرَ غَيْرٍ وَشِبْهِهِ وَمِثْلٍ فَإِنَّهَا لَا تَتَعَرَّفُ بِالْإِضَافَةِ", "en": "ghayr, siwā and mithl never made definite", "tr": "gayr, sivâ ve misl ma'rife olmaz", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "ضَارِبِ زَيْدٍ وَحَسَنِ الْوَجْهِ وَمَعْمُولِ الدَّارِ وَالضَّارِبَا زَيْدٍ وَالضَّارِبُو زَيْدٍ", "en": "the lafẓiyya: the adjective annexed to its governed word", "tr": "lafzî: ma'mûlüne muzâf sıfat", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "وَجَازَ الضَّارِبُ الرَّجُلِ حَمْلًا عَلَى الْحَسَنِ الْوَجْهِ", "en": "the article on both terms, by analogy", "tr": "iki terimde lâm, kıyasla", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "غُلَامٌ زَيْدٍ", "right": "غُلَامُ زَيْدٍ", "why": {"en": "the muḍāf loses its tanwīn — the annexation is what takes it", "tr": "muzâf tenvinini kaybeder — onu alan izâfettir"}},
  {"wrong": "ضَارِبَانِ زَيْدٍ", "right": "ضَارِبَا زَيْدٍ", "why": {"en": "the nūn of the dual stands for the tanwīn and falls with it", "tr": "tesniye nûnu tenvinin nâibidir ve onunla düşer"}},
  {"wrong": "الْغُلَامُ زَيْدٍ", "right": "غُلَامُ زَيْدٍ", "why": {"en": "a maʿnawī muḍāf is bare of the article — the annexation itself makes it definite", "tr": "ma'nevî muzâf lâm almaz — onu ma'rife yapan izâfetin kendisidir"}},
  {"wrong": "الضَّارِبِ زَيْدٍ", "right": "الضَّارِبُ زَيْدًا / ضَارِبُ زَيْدٍ", "why": {"en": "a singular with the article has no tanwīn to drop, so the lafẓī annexation lightens nothing and is barred", "tr": "lâmlı müfredin düşecek tenvini yok; lafzî izâfet hiçbir şeyi hafifletmez, yasaktır"}},
 ],
}
ADD_EN = (" Chapter 14 (print pp. 110-111): the annexed noun as the seventh governor and its condition (s1); its two kinds (s2); the maʿnawiyya, its condition (s3), "
          "its sense of min or of the lām (s4) and its giving definiteness save in ghayr, its like and mithl (s5); the lafẓiyya and its examples (s6); the barred and the allowed (s7). "
          "The ḥāl reading of غَيْرَ in s5 follows the received text's naṣb.")
ADD_TR = (" On dördüncü bab (baskı s. 110-111): yedinci âmil olarak muzâf isim ve şartı (s1); iki türü (s2); ma'nevî, şartı (s3), min veya lâm mânâsı (s4) ve gayr, benzeri ve misl "
          "dışında ta'rîf ifade etmesi (s5); lafzî ve örnekleri (s6); yasak ve câiz olan (s7). s5'teki غَيْرَ'nin hâl okunuşu rivâyet edilen metnin nasbına uyar.")
write_out(14, S, TITLE, ADD_EN, ADD_TR, "pp. 110-111", GLOSS_ADD, notes=(NOTE,),
          related=((ID, [K]), (IL, [K]), (TB, [K]), (K12, [K]), (JMS, [K]), (MTH, [K])))
report(14, S, GLOSS_ADD, (NOTE,))
