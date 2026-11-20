# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 45: the governed BY FOLLOWING — five; none fronted before its followed word, its governor its followed word's
# governor, its iʿrāb its followed word's iʿrāb. The FIRST, the ṣifa: a follower pointing to a meaning in its followed word absolutely; may be
# multiplied (جَاءَنِي الرَّجُلُ الْعَالِمُ الْفَاضِلُ); the nakira qualified by a declarative sentence with a pronoun, droppable on a clue (جَاءَنِي رَجُلٌ قَامَ
# أَبُوهُ); qualified by the state of the qualified word — following it in definiteness, number and gender (رَجُلٌ عَالِمٌ، امْرَأَةٌ صَالِحَةٌ) — or by the
# state of what belongs to it — following in the first two only (جَاءَنِي رِجَالٌ رَاكِبٌ غِلْمَانُهُمْ); the maʿrifa and the nakira defined, the maʿrifa
# six kinds. Print pp. 141–142.
#   python3 author_izhar_ch45.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"; AMS = "an-masdariyya"
NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; INS = "in-shartiyya"; JZ = "nawasib-wa-jawazim-al-mudari"; YM = "ya-al-mutakallim"; DF = "damir-fasl"
TMZ = "tamyiz"; AMT = "amma-tafsiliyya"; FK = "fa-khabar-mubtada"; TW = "tawabi-al-musnad-ilayh"; JS = "jumla-sifa"; TRF = "tarif-al-musnad-ilayh"; TNK = "tankir-al-musnad-ilayh"; SM = "sifa-mushabbaha"
K = "al-tawabi-wal-sifa"
K44 = "al-fa-fi-jawab-al-shart"
TITLE = {"ar": "الْمَعْمُولُ بِالتَّبَعِيَّةِ خَمْسَةٌ: الْأَوَّلُ الصِّفَةُ وَأَحْكَامُهَا، وَالْمَعْرِفَةُ وَالنَّكِرَةُ", "en": "The five governed by following: the first, the ṣifa and its rules; the maʿrifa and the nakira", "tr": "Tâbi olarak ma'mûl beştir: birincisi sıfat ve hükümleri; ma'rife ve nekre"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wayajuz(): return tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb"))
def jaani(gr=None): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV] + (gr or [NA]), "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")])
def wal(form, lex, en, tr, gr=None, punct=None): return tok(form, lex, "noun", [K, AT, HJ, MSD] + (gr or []), "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ مَجْرُورٌ.", en, tr, punct=punct, segments=wa(form[2:], lex, "noun"))

# ----------- s1 — the five followers and their rule
S.append({"id": "s1", "translation": {"en": "And as for the governed by following, it is five; none of them may be fronted before its followed word, its governor is the governor of its followed word, and its iʿrāb is like its iʿrāb.", "tr": "Tâbi olarak ma'mûle gelince, o beştir; hiçbiri metbûunun önüne alınamaz, âmili metbûunun âmilidir, i'râbı onun i'râbı gibidir."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, AMT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«… -e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("الْمَعْمُولُ", "mamul", "noun", [K, MK, AMT, IMF, TW], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the governed» — the mubtada.", "«ma'mûl» — mübtedâ."),
  tok("بِالتَّبَعِيَّةِ", "tabaiyya", "noun", [K, HJ, TW, NSB], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّبَعِيَّةِ مَجْرُورٌ.", "«by following»", "«tâbi olarak»", segments=[seg("بِ", "bi", "prep"), seg("التَّبَعِيَّةِ", "tabaiyya", "noun")]),
  tok("فَخَمْسَةٌ", "khamsa", "noun", [K, FK, MK], "الْفَاءُ وَاقِعَةٌ فِي الْخَبَرِ، وَخَمْسَةٌ خَبَرٌ مَرْفُوعٌ.", "«then five» — the khabar.", "«beştir» — haber.", punct="،", segments=fa("خَمْسَةٌ", "khamsa", "noun")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, LN, FL, HV, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the fronting of»", "«öne alınması»"),
  tok("شَيْءٍ", "shay", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«any»", "«hiçbirinin»"),
  tok("مِنْهَا", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مِنَ التَّوَابِعِ.", "«of them» — of the followers.", "«onlardan» — tâbilerden.", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("مَتْبُوعِهَا", "matbu", "noun", [K, HJ, ID, IMF, TW], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its followed word»", "«metbûunun»", punct="،", segments=[seg("مَتْبُوعِ", "matbu", "noun"), pr3fs()]),
  tok("وَعَامِلُهَا", "amil", "noun", [K, AT, MK, ID, IFA], "الْوَاوُ عَاطِفَةٌ، وَعَامِلُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its governor»", "«ve âmili»", segments=[seg("وَ", "wa", "conj"), seg("عَامِلُ", "amil", "noun"), pr3fs()]),
  tok("عَامِلُ", "amil", "noun", [K, MK, ID, IFA], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the governor of» — the khabar.", "«… âmilidir» — haber."),
  tok("مَتْبُوعِهَا", "matbu", "noun", [K, ID, IMF, TW], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its followed word»", "«metbûunun»", punct="،", segments=[seg("مَتْبُوعِ", "matbu", "noun"), pr3fs()]),
  tok("وَإِعْرَابُهَا", "irab", "noun", [K, AT, MK, ID, MSD, F4], "الْوَاوُ عَاطِفَةٌ، وَإِعْرَابُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its iʿrāb»", "«ve i'râbı»", segments=[seg("وَ", "wa", "conj"), seg("إِعْرَابُ", "irab", "noun"), pr3fs()]),
  tok("كَإِعْرَابِهِ", "irab", "noun", [K, HJ, ID, MK, MSD], "الْكَافُ حَرْفُ جَرٍّ، وَإِعْرَابِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«like its iʿrāb» — the followed word's.", "«onun i'râbı gibi» — metbûun.", punct=".", segments=[seg("كَ", "ka", "prep"), seg("إِعْرَابِ", "irab", "noun"), pr3msi()]),
 ]})
# ----------- s2 — the first: the ṣifa defined; multiplied
S.append({"id": "s2", "translation": {"en": "The first is the ṣifa, and it is a follower that points to a meaning in its followed word absolutely; and its multiplication is allowed — as in «there came to me the learned, excellent man»;", "tr": "Birincisi sıfattır: metbûunda bir mânâya mutlak olarak delâlet eden tâbidir; taaddüdü câizdir — «bana âlim, fâzıl adam geldi» gibi;"},
 "tokens": [
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first»", "«birincisi»"),
  tok("الصِّفَةُ", "sifa", "noun", [K, MK, NA], "خَبَرٌ مَرْفُوعٌ.", "«the ṣifa» — the khabar.", "«sıfat» — haber.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هِيَ", "hiya", "pron")),
  tok("تَابِعٌ", "tabi", "noun", [K, MK, IFA, TW], "خَبَرٌ مَرْفُوعٌ.", "«a follower» — the khabar.", "«bir tâbi» — haber."),
  tok("يَدُلُّ", "dalla", "verb", [K, NA, MR, FL, "doubled-verbs", JS], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ لِتَابِعٌ.", "«that points» — the clause a naʿt.", "«delâlet eden» — cümle sıfat."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْنًى", "mana", "noun", [K, HJ, MQ], "مَجْرُورٌ بِعَلَى بِكَسْرَةٍ مُقَدَّرَةٍ.", "«a meaning»", "«bir mânâya»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("مَتْبُوعِهِ", "matbu", "noun", [K, HJ, ID, IMF, TW], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its followed word»", "«metbûunda»", segments=[seg("مَتْبُوعِ", "matbu", "noun"), pr3msi()]),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ — فِي ذَاتِهِ أَوْ فِي مُتَعَلِّقِهِ.", "«absolutely» — in itself or in what belongs to it.", "«mutlak olarak» — kendisinde ya da müteallikinde.", punct="،"),
  wayajuz(),
  tok("تَعَدُّدُهَا", "taaddud", "noun", [K, FL, ID, MSD, F5], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its multiplication»", "«taaddüdü»", punct="،", segments=[seg("تَعَدُّدُ", "taaddud", "noun"), pr3fs()]),
  nahw(), jaani(),
  tok("الرَّجُلُ", "rajul", "noun", [K, FL, NA], "فَاعِلٌ مَرْفُوعٌ — الْمَوْصُوفُ.", "«the man» — the qualified word.", "«adam» — mevsûf."),
  tok("الْعَالِمُ", "alim-scholar", "noun", [K, NA, IFA], "نَعْتٌ أَوَّلُ مَرْفُوعٌ.", "«the learned» — the first ṣifa.", "«âlim» — ilk sıfat."),
  tok("الْفَاضِلُ", "fadil", "noun", [K, NA, IFA], "نَعْتٌ ثَانٍ مَرْفُوعٌ.", "«the excellent» — the second ṣifa.", "«fâzıl» — ikinci sıfat.", punct="،"),
 ]})
# ----------- s3 — the nakira qualified by a sentence
S.append({"id": "s3", "translation": {"en": "and qualifying the indefinite by a declarative sentence is allowed, and the pronoun is required in it — as in «there came to me a man whose father stood» — and it may be dropped on a clue;", "tr": "nekreyi haber cümlesiyle vasıflamak câizdir; onda zamir gerekir — «bana babası kalkmış bir adam geldi» gibi — karîne ile hazfedilebilir de;"},
 "tokens": [
  wayajuz(),
  tok("وَصْفُ", "wasf", "noun", [K, FL, ID, MSD, NA], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«qualifying»", "«vasıflamak»"),
  tok("النَّكِرَةِ", "nakira", "noun", [K, ID, TNK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the indefinite»", "«nekreyi»"),
  tok("بِالْجُمْلَةِ", "jumla", "noun", [K, HJ, JS], "الْبَاءُ حَرْفُ جَرٍّ، وَالْجُمْلَةِ مَجْرُورٌ.", "«by the sentence»", "«cümleyle»", segments=[seg("بِ", "bi", "prep"), seg("الْجُمْلَةِ", "jumla", "noun")]),
  tok("الْخَبَرِيَّةِ", "khabariyya", "noun", [K, NA, NSB, JS], "نَعْتٌ مَجْرُورٌ — لَا الْإِنْشَائِيَّةِ.", "«declarative» — not the performative.", "«haber cümlesi» — inşâ değil.", punct="،"),
  tok("وَيَلْزَمُ", "lazima", "verb", [K, AT, MR, FL], "الْوَاوُ عَاطِفَةٌ، وَيَلْزَمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is required»", "«ve gerekir»", segments=wa("يَلْزَمُ", "lazima", "verb")),
  tok("فِيهَا", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — فِي الْجُمْلَةِ.", "«in it» — in the sentence.", "«onda» — cümlede.", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  tok("الضَّمِيرُ", "damir", "noun", [K, FL, JS], "فَاعِلٌ مَرْفُوعٌ — الرَّابِطُ.", "«the pronoun» — the binder.", "«zamir» — râbıt.", punct="،"),
  nahw(), jaani([JS]),
  tok("رَجُلٌ", "rajul", "noun", [K, FL, JS], "فَاعِلٌ مَرْفُوعٌ — نَكِرَةٌ مَوْصُوفَةٌ بِالْجُمْلَةِ.", "«a man» — a nakira qualified by the sentence.", "«bir adam» — cümleyle vasıflanmış nekre."),
  tok("قَامَ", "qama", "verb", [K, JS, FL, HV], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ، صِفَةٌ.", "«stood» — the clause a ṣifa.", "«kalktı» — cümle sıfat."),
  tok("أَبُوهُ", "ab", "noun", [K, FL, ID, "five-nouns", JS], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الضَّمِيرُ الرَّابِطُ.", "«his father» — the pronoun binds.", "«babası» — bağlayan zamir.", punct="،", segments=[seg("أَبُو", "ab", "noun"), pr3ms()]),
  tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF, MR, HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — الضَّمِيرُ.", "«it is dropped» — the pronoun.", "«hazfedilir» — zamir."),
  tok("لِقَرِينَةٍ", "qarina", "noun", [K, HJ, HT], "اللَّامُ حَرْفُ جَرٍّ، وَقَرِينَةٍ مَجْرُورٌ.", "«on a clue»", "«karîne ile»", punct="،", segments=[seg("لِ", "li", "prep"), seg("قَرِينَةٍ", "qarina", "noun")]),
 ]})
# ----------- s4 — qualified by its own state: full agreement
S.append({"id": "s4", "translation": {"en": "and it is qualified by the state of the qualified word and by the state of what belongs to it; the first follows it in definiteness and indefiniteness, singular, dual and plural, masculine and feminine — as in «there came to me a learned man» and «there came to me a righteous woman» —", "tr": "mevsûfun kendi hâliyle ve müteallikinin hâliyle vasıflanır; ilki ona ta'rif ve tenkirde, ifrad, tesniye ve cem'de, tezkir ve te'nisde uyar — «bana âlim bir adam geldi» ve «bana sâliha bir kadın geldi» gibi —"},
 "tokens": [
  tok("وَيُوصَفُ", "wasafa", "verb", [K, AT, NF, MR, NA], "الْوَاوُ عَاطِفَةٌ، وَيُوصَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — الْمَوْصُوفُ.", "«and it is qualified» — the qualified word.", "«ve vasıflanır» — mevsûf.", segments=wa("يُوصَفُ", "wasafa", "verb")),
  tok("بِحَالِ", "hal", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَحَالِ مَجْرُورٌ، مُضَافٌ.", "«by the state of»", "«… hâliyle»", segments=[seg("بِ", "bi", "prep"), seg("حَالِ", "hal", "noun")]),
  tok("الْمَوْصُوفِ", "mawsuf", "noun", [K, ID, IMF, NA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the qualified word»", "«mevsûfun»"),
  tok("وَحَالِ", "hal", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَحَالِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and by the state of»", "«ve … hâliyle»", segments=wa("حَالِ", "hal", "noun")),
  tok("مُتَعَلِّقِهِ", "mutaalliq", "noun", [K, ID, IFA, F5], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَا يَتَّصِلُ بِهِ كَغُلَامِهِ وَأَبِيهِ.", "«what belongs to it» — its servant, its father.", "«müteallikinin» — kölesi, babası gibi.", punct="،", segments=[seg("مُتَعَلِّقِ", "mutaalliq", "noun"), pr3msi()]),
  tok("فَالْأَوَّلُ", "awwal", "noun", [K, AT, MK], "الْفَاءُ لِلتَّفْصِيلِ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the first»", "«ilki»", segments=fa("الْأَوَّلُ", "awwal", "noun")),
  tok("يَتْبَعُهُ", "tabia-follow", "verb", [K, MK, MR, FL, MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«follows it» — the clause the khabar.", "«ona uyar» — cümle haber.", segments=[seg("يَتْبَعُ", "tabia-follow", "verb"), pr3ms()]),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("التَّعْرِيفِ", "tarif", "noun", [K, HJ, MSD, F2, TRF], "مَجْرُورٌ بِفِي.", "«definiteness»", "«ta'rif»"),
  wal("وَالتَّنْكِيرِ", "tankir", "«and indefiniteness»", "«ve tenkir»", [F2, TNK]),
  wal("وَالْإِفْرَادِ", "ifrad", "«and the singular»", "«ve ifrad»", [F4]),
  wal("وَالتَّثْنِيَةِ", "tathniya", "«and the dual»", "«ve tesniye»", [F2, MTH]),
  wal("وَالْجَمْعِ", "jam", "«and the plural»", "«ve cem'»", ["jam"]),
  wal("وَالتَّذْكِيرِ", "tadhkir", "«and the masculine»", "«ve tezkir»", [F2]),
  wal("وَالتَّأْنِيثِ", "tanith", "«and the feminine»", "«ve te'nis»", [F2], punct="،"),
  nahw(), jaani(),
  tok("رَجُلٌ", "rajul", "noun", [K, FL, NA], "فَاعِلٌ مَرْفُوعٌ — الْمَوْصُوفُ.", "«a man»", "«bir adam»"),
  tok("عَالِمٌ", "alim-scholar", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ — نَكِرَةٌ مُفْرَدٌ مُذَكَّرٌ كَمَوْصُوفِهِ.", "«learned» — indefinite, singular, masculine like its noun.", "«âlim» — mevsûfu gibi nekre, müfred, müzekker."),
  tok("وَجَاءَتْنِي", "jaa", "verb", [K, AT, FL, MB, HV, NA], "الْوَاوُ عَاطِفَةٌ، وَجَاءَتْنِي فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and there came to me»", "«ve bana geldi»", segments=[seg("وَ", "wa", "conj"), seg("جَاءَتْ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("امْرَأَةٌ", "imraa", "noun", [K, FL, NA], "فَاعِلٌ مَرْفُوعٌ — الْمَوْصُوفُ.", "«a woman»", "«bir kadın»"),
  tok("صَالِحَةٌ", "salih", "noun", [K, NA, IFA], "نَعْتٌ مَرْفُوعٌ — مُؤَنَّثٌ كَمَوْصُوفِهِ.", "«righteous» — feminine like its noun.", "«sâliha» — mevsûfu gibi müennes.", punct="،"),
 ]})
# ----------- s5 — qualified by the state of what belongs to it: two agreements only
S.append({"id": "s5", "translation": {"en": "and the second in the first two only — as in «there came to me men whose servants are riding».", "tr": "ikincisi ise yalnız ilk ikisinde — «bana köleleri binmiş adamlar geldi» gibi."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — وَخَبَرُهُ مَحْذُوفٌ: يَتْبَعُهُ.", "«and the second» — «follows it» understood.", "«ikincisi» — «uyar» mahzuf.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَوَّلَيْنِ", "awwal", "noun", [K, HJ, MTH], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — التَّعْرِيفِ وَالتَّنْكِيرِ.", "«the first two» — definiteness and indefiniteness.", "«ilk ikisinde» — ta'rif ve tenkir."),
  tok("فَقَطْ", "faqat", "adv", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ.", "«only»", "«yalnız»", punct="،"),
  nahw(), jaani(),
  tok("رِجَالٌ", "rijal", "noun", [K, FL, NA, JT], "فَاعِلٌ مَرْفُوعٌ — الْمَوْصُوفُ، جَمْعٌ.", "«men» — the qualified word, a plural.", "«adamlar» — mevsûf, cemi."),
  tok("رَاكِبٌ", "rakib", "noun", [K, NA, IFA, "shurut-amal-ism-al-fail"], "نَعْتٌ مَرْفُوعٌ — مُفْرَدٌ وَمَوْصُوفُهُ جَمْعٌ، لِأَنَّهُ جَرَى عَلَى غِلْمَانِهِمْ؛ تَبِعَ فِي التَّنْكِيرِ وَالرَّفْعِ.", "«riding» — singular though its noun is plural, since it runs on «their servants»; it follows only in indefiniteness and case.", "«binmiş» — mevsûfu cemi iken müfred; çünkü gılmânihim'e göre yürür; yalnız tenkirde ve ref'te uyar."),
  tok("غِلْمَانُهُمْ", "ghulam", "noun", [K, FL, ID, JT], "فَاعِلُ رَاكِبٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — مُتَعَلِّقُ الْمَوْصُوفِ.", "«their servants» — the doer of «riding», what belongs to the qualified word.", "«köleleri» — râkibün'ün fâili; mevsûfun mütealliki.", punct=".", segments=[seg("غِلْمَانُ", "ghulam", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
 ]})
# ----------- s6 — maʿrifa and nakira defined; the maʿrifa six kinds
S.append({"id": "s6", "translation": {"en": "And the maʿrifa is what is coined for a thing in particular, and the nakira what is coined for a thing not in particular; and the maʿrifa is six kinds:", "tr": "Ma'rife, belirli bir şey için konulandır; nekre ise belirli olmayan bir şey için konulan; ma'rife altı nev'dir:"},
 "tokens": [
  tok("وَالْمَعْرِفَةُ", "marifa", "noun", [K, AT, MK, TRF], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمَعْرِفَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the maʿrifa»", "«ve ma'rife»", segments=wa("الْمَعْرِفَةُ", "marifa", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، خَبَرٌ.", "«what» — the khabar.", "«şey» — haber."),
  tok("وُضِعَ", "wadaa", "verb", [K, MAW, NF, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةُ مَا.", "«is coined»", "«konulan»"),
  tok("لِشَيْءٍ", "shay", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«for a thing»", "«bir şey için»", segments=[seg("لِ", "li", "prep"), seg("شَيْءٍ", "shay", "noun")]),
  tok("بِعَيْنِهِ", "ayn-thing", "noun", [K, HJ, ID, NA], "الْبَاءُ حَرْفُ جَرٍّ، وَعَيْنِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِفَةٌ لِشَيْءٍ: مُعَيَّنٍ.", "«in particular» — a specified thing.", "«belirli» — muayyen.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("عَيْنِ", "ayn-thing", "noun"), pr3msi()]),
  tok("وَالنَّكِرَةُ", "nakira", "noun", [K, AT, MK, TNK], "الْوَاوُ عَاطِفَةٌ، وَالنَّكِرَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the nakira»", "«ve nekre»", segments=wa("النَّكِرَةُ", "nakira", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ، خَبَرٌ.", "«what»", "«şey»"),
  tok("وُضِعَ", "wadaa", "verb", [K, MAW, NF, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is coined»", "«konulan»"),
  tok("لِشَيْءٍ", "shay", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«for a thing»", "«bir şey için»", segments=[seg("لِ", "li", "prep"), seg("شَيْءٍ", "shay", "noun")]),
  tok("لَا", "la-nafiya", "part", [K, LN, NA], "حَرْفُ نَفْيٍ.", "«not»", "«olmayan»"),
  tok("بِعَيْنِهِ", "ayn-thing", "noun", [K, HJ, ID, NA], "الْبَاءُ حَرْفُ جَرٍّ، وَعَيْنِهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in particular»", "«belirli»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("عَيْنِ", "ayn-thing", "noun"), pr3msi()]),
  tok("وَالْمَعْرِفَةُ", "marifa", "noun", [K, AT, MK, TRF], "الْوَاوُ عَاطِفَةٌ، وَالْمَعْرِفَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the maʿrifa»", "«ve ma'rife»", segments=wa("الْمَعْرِفَةُ", "marifa", "noun")),
  tok("سِتَّةُ", "sitta", "noun", [K, MK, ID, TMZ], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«six» — the khabar.", "«altı» — haber."),
  tok("أَنْوَاعٍ", "naw", "noun", [K, ID, JT, TMZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُضْمَرُ وَالْعَلَمُ وَالْمُبْهَمُ وَالْمَوْصُولُ وَالْمُعَرَّفُ بِاللَّامِ وَالْمُضَافُ إِلَيْهَا.", "«kinds» — the pronoun, the proper name, the vague noun, the relative, the lām-defined, the annexed.", "«nev'» — zamir, alem, mübhem, mevsûl, lâmla ma'rife, bunlara muzâf.", punct=":"),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "tankir": G("tankir", "تَنْكِير", "ن ك ر", "noun", "indefiniteness — making or being a nakira", "tenkir — nekrelik, nekre kılma", 4),
}
used = set()
for s in S:
    for t in s["tokens"]:
        used.add(t["lex"])
        for sg_ in t.get("segments", []): used.add(sg_["lex"])
CAND = {}
for k in sorted(used):
    if k in TG: continue
    if k in NEW: CAND[k] = NEW[k]
    elif _ic.has_gloss(k): CAND[k] = find_gloss(k)
    else: raise SystemExit(f"no gloss anywhere for {k}")
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch45 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "jaa", "dalla", "lazima", "qama", "hadhafa", "wasafa", "tabia-follow", "wadaa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "التَّوَابِعُ الْخَمْسَةُ وَحُكْمُهَا؛ الصِّفَةُ: تَعَدُّدُهَا وَالْجُمْلَةُ وَالْمُطَابَقَةُ؛ الْمَعْرِفَةُ وَالنَّكِرَةُ", "en": "The five followers and their rule; the ṣifa: multiplied, as a sentence, and its agreement; the maʿrifa and the nakira", "tr": "Beş tâbi ve hükmü; sıfat: taaddüdü, cümle oluşu ve mutâbakatı; ma'rife ve nekre"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المعمول بالتبعية: الصفة", "الكافية لابن الحاجب — التوابع: النعت", "شرح قطر الندى لابن هشام — النعت"],
 "amil": "the governed by following are five — none fronted before its followed word, its governor the followed word's governor, its iʿrāb the followed word's; the first is the ṣifa, a follower pointing to a meaning in its followed word absolutely; it may be multiplied (الرَّجُلُ الْعَالِمُ الْفَاضِلُ); a nakira may be qualified by a declarative sentence holding a pronoun, droppable on a clue (رَجُلٌ قَامَ أَبُوهُ); a ṣifa of the noun's own state follows it in definiteness, number and gender (رَجُلٌ عَالِمٌ، امْرَأَةٌ صَالِحَةٌ), a ṣifa of what belongs to it only in definiteness and case (رِجَالٌ رَاكِبٌ غِلْمَانُهُمْ); the maʿrifa is coined for a particular thing, the nakira for an unparticular one; the maʿrifa is six kinds",
 "question": {
  "en": ["What is the governed by following? A word governed through another: five kinds — the ṣifa, the ʿaṭf, the tawkīd, the badal, the ʿaṭf bayān — never fronted before the followed word, sharing its governor and its iʿrāb.",
         "What is the ṣifa? A follower that points to a meaning in its followed word, absolutely — in the word itself or in what belongs to it.",
         "May the ṣifa be multiplied? Yes: جَاءَنِي الرَّجُلُ الْعَالِمُ الْفَاضِلُ — two ṣifas of one noun.",
         "May a sentence be a ṣifa? Of a nakira, a declarative sentence with a pronoun binding it (جَاءَنِي رَجُلٌ قَامَ أَبُوهُ); the pronoun may be dropped on a clue.",
         "In what does the ṣifa agree? When it qualifies the noun's own state: definiteness, number and gender — رَجُلٌ عَالِمٌ، امْرَأَةٌ صَالِحَةٌ. When it qualifies what belongs to the noun: definiteness and case only — رِجَالٌ رَاكِبٌ غِلْمَانُهُمْ, where رَاكِبٌ runs on غِلْمَانُهُمْ.",
         "What are the maʿrifa and the nakira? The maʿrifa is coined for a particular thing, the nakira for a thing not in particular; the maʿrifa is six kinds — the pronoun, the proper name, the demonstrative, the relative, the lām-defined and what is annexed to these.",
         "What does the engine READ here? The DabtEngine reads the definite nouns after a definite doer as its naʿts in rafʿ, the verbal clause after a nakira doer as its ṣifa with أَبُوهُ raised by the wāw, the singular رَاكِبٌ after the plural رِجَالٌ as its naʿt with غِلْمَانُهُمْ its doer, and the قَدْ, وَ and فَ particles as the author wrote them."],
  "tr": ["Tâbi olarak ma'mûl nedir? Başkası aracılığıyla ma'mûl olan kelime: beş tür — sıfat, atıf, te'kîd, bedel, atf-ı beyân — metbûunun önüne alınmaz, âmilini ve i'râbını paylaşır.",
         "Sıfat nedir? Metbûunda bir mânâya mutlak olarak delâlet eden tâbi — kelimenin kendisinde ya da müteallikinde.",
         "Sıfat taaddüd eder mi? Evet: câenî'r-racülü'l-âlimü'l-fâdılü — bir ismin iki sıfatı.",
         "Cümle sıfat olabilir mi? Nekrenin sıfatı olarak, zamirle bağlı haber cümlesi (câenî racülün kâme ebûhu); zamir karîne ile hazfedilebilir.",
         "Sıfat neyde uyar? İsmin kendi hâlini vasıflarken: ta'rif, sayı ve cinsiyet — racülün âlimün, imraetün sâlihatün. İsme ait olanı vasıflarken: yalnız ta'rif ve i'râb — ricâlün râkibün gılmânühüm; râkibün gılmânühüm'e göre yürür.",
         "Ma'rife ve nekre nedir? Ma'rife belirli bir şey için, nekre belirli olmayan bir şey için konulandır; ma'rife altı nev'dir — zamir, alem, işaret, mevsûl, lâmla ma'rife ve bunlara muzâf.",
         "Motor burada neyi OKUR? DabtEngine ma'rife fâilden sonraki ma'rife isimleri ref'li na't; nekre fâilden sonraki fiil cümlesini vâv ile merfû ebûhu ile sıfat; cemi ricâlün'den sonraki müfred râkibün'ü fâili gılmânühüm olan na't; kad, ve ve fe edatlarını yazarın yazdığı gibi okur."],
 },
 "plain": {"en": "Five kinds of word «follow» another and copy its case: adjectives, «and»-links, emphasis words, substitutes, explanatory names. An adjective matches its noun in definiteness, number and gender («a learned man»), unless it describes something of the noun's («men whose servants ride»), then only in definiteness and case.",
           "tr": "Beş tür kelime bir başkasına «tâbi» olur ve hâlini alır: sıfatlar, «ve» bağları, pekiştirmeler, bedeller ve açıklayıcı adlar. Sıfat ismine belirlilik, sayı ve cinsiyette uyar («âlim bir adam»); isme ait bir şeyi anlatıyorsa («köleleri binmiş adamlar») yalnız belirlilik ve hâlde uyar."},
 "explanation": {"en": "The governed by following is five; none may be fronted before its followed word, its governor is the followed word's governor, and its iʿrāb is like its iʿrāb. The first is the ṣifa: a follower pointing to a meaning in its followed word absolutely. It may be multiplied (جَاءَنِي الرَّجُلُ الْعَالِمُ الْفَاضِلُ). A nakira may be qualified by a declarative sentence, in which the pronoun is required (جَاءَنِي رَجُلٌ قَامَ أَبُوهُ) though it may be dropped on a clue. The noun is qualified by its own state or by the state of what belongs to it: the first ṣifa follows it in definiteness and indefiniteness, singular, dual and plural, masculine and feminine (جَاءَنِي رَجُلٌ عَالِمٌ، جَاءَتْنِي امْرَأَةٌ صَالِحَةٌ); the second only in the first two — definiteness and case — (جَاءَنِي رِجَالٌ رَاكِبٌ غِلْمَانُهُمْ), since it runs on the noun that belongs. The maʿrifa is what is coined for a particular thing, the nakira what is coined for a thing not in particular; the maʿrifa is six kinds, which follow.",
                 "tr": "Tâbi olarak ma'mûl beştir; hiçbiri metbûunun önüne alınamaz, âmili metbûunun âmilidir, i'râbı onun i'râbı gibidir. Birincisi sıfattır: metbûunda bir mânâya mutlak olarak delâlet eden tâbi. Taaddüd edebilir (câenî'r-racülü'l-âlimü'l-fâdılü). Nekre, zamirin gerekli olduğu bir haber cümlesiyle vasıflanabilir (câenî racülün kâme ebûhu); zamir karîne ile hazfedilebilir. İsim kendi hâliyle ya da müteallikinin hâliyle vasıflanır: ilk sıfat ona ta'rif ve tenkirde, ifrad, tesniye ve cem'de, tezkir ve te'nisde uyar (câenî racülün âlimün, câetnî imraetün sâlihatün); ikincisi yalnız ilk ikisinde — ta'rif ve i'râbda — (câenî ricâlün râkibün gılmânühüm); çünkü ait olan isme göre yürür. Ma'rife belirli bir şey için konulan, nekre belirli olmayan bir şey için konulandır; ma'rife altı nev'dir, sırası gelir."},
 "examples": [
  {"ar": "وَأَمَّا الْمَعْمُولُ بِالتَّبَعِيَّةِ فَخَمْسَةٌ", "en": "the five followers and their rule", "tr": "beş tâbi ve hükmü", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "جَاءَنِي الرَّجُلُ الْعَالِمُ الْفَاضِلُ", "en": "the ṣifa multiplied", "tr": "sıfatın taaddüdü", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "جَاءَنِي رَجُلٌ قَامَ أَبُوهُ", "en": "the sentence as ṣifa of a nakira", "tr": "nekrenin cümle sıfatı", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "جَاءَنِي رَجُلٌ عَالِمٌ وَجَاءَتْنِي امْرَأَةٌ صَالِحَةٌ", "en": "full agreement", "tr": "tam mutâbakat", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "جَاءَنِي رِجَالٌ رَاكِبٌ غِلْمَانُهُمْ", "en": "the ṣifa of what belongs: two agreements only", "tr": "müteallikin sıfatı: yalnız iki uyum", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "وَالْمَعْرِفَةُ مَا وُضِعَ لِشَيْءٍ بِعَيْنِهِ", "en": "the maʿrifa and the nakira defined", "tr": "ma'rife ve nekrenin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي رَجُلٌ الْعَالِمُ", "right": "جَاءَنِي رَجُلٌ عَالِمٌ", "why": {"en": "the ṣifa of the noun's own state follows it in definiteness", "tr": "ismin kendi hâlinin sıfatı ta'rifte ona uyar"}},
  {"wrong": "جَاءَنِي رِجَالٌ رَاكِبُونَ غِلْمَانُهُمْ", "right": "جَاءَنِي رِجَالٌ رَاكِبٌ غِلْمَانُهُمْ", "why": {"en": "a ṣifa of what belongs to the noun agrees with its own doer in number, not with the noun", "tr": "müteallikin sıfatı sayıda isme değil kendi fâiline uyar"}},
  {"wrong": "جَاءَنِي رَجُلٌ قَامَ زَيْدٌ (as a ṣifa)", "right": "جَاءَنِي رَجُلٌ قَامَ أَبُوهُ", "why": {"en": "a sentence qualifying a nakira must carry a pronoun returning to it", "tr": "nekreyi vasıflayan cümle ona dönen bir zamir taşımalıdır"}},
 ],
}
TMZ = "tamyiz"
ADD_EN = (" Chapter 45 (print pp. 141-142): the five followers and their rule (s1), the ṣifa defined and multiplied (s2), the sentence as ṣifa of a nakira with its pronoun (s3), agreement in the noun's own state (s4) and in what belongs to it (s5), the maʿrifa and the nakira defined and the six kinds announced (s6).")
ADD_TR = (" Kırk beşinci bab (baskı s. 141-142): beş tâbi ve hükmü (s1), sıfatın tarifi ve taaddüdü (s2), zamiriyle nekrenin cümle sıfatı (s3), ismin kendi hâlinde (s4) ve müteallikinde (s5) mutâbakat, ma'rife ve nekrenin tarifi ve altı nev'in ilânı (s6).")
write_out(45, S, TITLE, ADD_EN, ADD_TR, "pp. 141-142", GLOSS_ADD, notes=(NOTE,),
          related=((K44, [K]), (NA, [K]), (TW, [K]), (JS, [K]), (TRF, [K]), (TNK, [K])))
report(45, S, GLOSS_ADD, (NOTE,))
