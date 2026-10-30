# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 7: the governor in the MUḌĀRIʿ verb — two kinds, the nāṣib and the jāzim. The nāṣib is
# four letters (أَنْ of the masdar, لَنْ of the emphatic future negation, كَيْ of cause, إِذَنْ of condition and answer — with
# إِذَنْ's condition: a future verb not leaning on what precedes it, and the two failing examples); أَنْ alone may be concealed
# (زُرْنِي فَأُكْرِمَكَ). The jāzim is fifteen words: four letters that jazm one verb (لَمْ، لَمَّا، لَامُ الْأَمْرِ، لَا النَّهْيِ) and
# eleven words that jazm two muḍāriʿs — the words of requital (إِنْ، حَيْثُمَا، أَيْنَ، أَنَّى، إِذْمَا، إِذَا مَا، مَتَى، مَهْمَا، مَا، أَيٌّ، مَنْ);
# إِنْ alone may be concealed (زُرْنِي أُكْرِمْكَ). Print pp. 99–101.
#   python3 author_izhar_ch7.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "nawasib-wa-jawazim-al-mudari"
K1 = "al-amil-wa-aqsamuh"
AM = "an-masdariyya"; LA = "lam-amr"; LJz = "lam-jazim"; NH = "al-nahy-wa-wujuhuh"; SH = "in-shartiyya"; IDH = "idha-shartiyya"; MR = "mudari-marfu"
TITLE = {"ar": "الْعَامِلُ فِي الْفِعْلِ الْمُضَارِعِ: النَّاصِبُ وَالْجَازِمُ", "en": "The governor in the muḍāriʿ verb: the nāṣib and the jāzim", "tr": "Muzâri fiildeki âmil: nâsıb ve câzim"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; TM = "tamyiz"; MTH = "al-muthanna"; JT = "jawab-al-talab"; ZN = "zanna-wa-akhawatuha"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def wanahw(punct=":"): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«and as in»", "«ve meselâ»", punct=punct, segments=wa("نَحْوُ", "nahw", "noun"))
def quoted(form, lex, pos, tags, role_ar, role_en, role_tr, punct=None, segments=None):
    return tok(form, lex, pos, [K] + tags + [HT], f"لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، {role_ar}", role_en, role_tr, punct=punct, segments=segments)
def wa_quoted(form, lex, pos, tags, punct=None):
    return tok("وَ" + form, lex, pos, [K] + tags + [AT, HT], "الْوَاوُ عَاطِفَةٌ، وَاللَّفْظُ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and " + lex.split("-")[0] + "» — quoted, joined.", "«ve …» — hikâye edilmiş, ma'tûf.", punct=punct, segments=wa(form, lex, pos))
def lil(form_rest, lex, tags, ar, en, tr, punct=None):
    return tok("لِ" + form_rest, lex, "noun", [K, HJ] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=[seg("لِ", "li", "prep"), seg(form_rest, lex, "noun")])
def minha(): return tok("مِنْهَا", "min", "prep", [K, HJ, NA], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ: مِنَ الْخَمْسَ عَشْرَةَ.", "«of them» — of the fifteen; the naʿt.", "«onlardan» — on beşten; sıfat.", segments=[seg("مِنْ", "min", "prep"), pr3fs()])
def zurni(): return tok("زُرْنِي", "zara", "verb", [K, "imperative-amr", MB, "hollow-verbs", "ya-al-mutakallim"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — الطَّلَبُ.", "«visit me» — the imperative; the request the answer hangs on.", "«beni ziyaret et» — emir; cevabın bağlandığı talep.", segments=[seg("زُرْ", "zara", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])

# ----------- s1 — the governor in the mudari: two kinds
S.append({"id": "s1", "translation": {"en": "And the governor in the muḍāriʿ verb is of two kinds: a nāṣib and a jāzim.", "tr": "Muzâri fiildeki âmil iki türlüdür: nâsıb ve câzim."},
 "tokens": [
  tok("وَالْعَامِلُ", "amil", "noun", [K, MK, K1, "ism-fail"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the governor» — the mubtada.", "«âmil» — mübtedâ.", segments=wa("الْعَامِلُ", "amil", "noun")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-deki»"),
  tok("الْفِعْلِ", "fil", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the verb»", "«fiil»"),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, NA, MR], "نَعْتٌ مَجْرُورٌ.", "«muḍāriʿ» — the naʿt.", "«muzâri» — sıfat."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«üzere»"),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, MK, MTH], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«two kinds» — the dual in jarr; the phrase is the khabar.", "«iki tür» — tesniye, mecrûr; câr-mecrûr haber.", punct=":"),
  tok("نَاصِبٌ", "nasib", "noun", [K, MK, HT, "ism-fail"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا نَاصِبٌ.", "«a nāṣib» — the khabar of a dropped mubtada: one of them is a nāṣib.", "«nâsıb» — mahzûf mübtedânın haberi: biri nâsıbdır."),
  tok("وَجَازِمٌ", "jazim", "noun", [K, AT, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَجَازِمٌ مَعْطُوفٌ مَرْفُوعٌ — وَالْآخَرُ جَازِمٌ.", "«and a jāzim» — joined: and the other is a jāzim.", "«ve câzim» — ma'tûf: diğeri câzimdir.", punct=".", segments=wa("جَازِمٌ", "jazim", "noun")),
 ]})
# ----------- s2 — the nasib: four letters
S.append({"id": "s2", "translation": {"en": "So the nāṣib is four letters: أَنْ for the masdar-sense, لَنْ for the emphatic negation in the future, كَيْ for cause, and إِذَنْ for condition and answer;", "tr": "Nâsıb dört harftir: masdariyet için en, istikbâlde te'kitli nefiy için len, sebebiyet için key, şart ve cezâ için izen;"},
 "tokens": [
  tok("فَالنَّاصِبُ", "nasib", "noun", [K, MK, "fa-khabar-mubtada", "ism-fail"], "الْفَاءُ لِلتَّفْرِيعِ، وَالنَّاصِبُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the nāṣib» — the mubtada.", "«nâsıb» — mübtedâ.", segments=fa("النَّاصِبُ", "nasib", "noun")),
  tok("أَرْبَعَةُ", "arbaa", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«four» — the khabar, annexed.", "«dört» — haber, muzâf."),
  tok("أَحْرُفٍ", "harf", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِلَّةٍ لِحَرْفٍ.", "«letters» — the plural of paucity.", "«harf» — kıllet cem'i.", punct=":"),
  quoted("أَنْ", "an-masdariyya", "part", [AM, MK], "مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«an» — quoted; the mubtada.", "«en» — hikâye edilmiş; mübtedâ."),
  lil("لْمَصْدَرِيَّةِ", "masdariyya", [MK, AM, "masdar"], "الْمَصْدَرِيَّةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«for the masdar-sense» — the khabar: أَنْ with its verb equals a masdar.", "«masdariyet için» — haber: en ile fiili bir masdar eder.", punct="،"),
  wa_quoted("لَنْ", "lan", "part", [MK]),
  lil("لنَّفْيِ", "nafy", [MK, "masdar"], "النَّفْيِ مَجْرُورٌ — خَبَرٌ.", "«for the negation» — the khabar.", "«nefiy için» — haber."),
  tok("الْمُؤَكَّدِ", "muakkad", "noun", [K, NA, "ism-maful", "tawkid"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ أَكَّدَ.", "«emphatic» — the naʿt.", "«te'kitli» — sıfat."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الِاسْتِقْبَالِ", "istiqbal", "noun", [K, HJ, "masdar", "form-x-verbs"], "مَجْرُورٌ بِفِي — مَصْدَرُ اسْتَقْبَلَ: الزَّمَانُ الْآتِي.", "«the future» — the masdar of Form X: the time to come.", "«istikbâl» — istif'âl masdarı: gelecek zaman.", punct="،"),
  wa_quoted("كَيْ", "kay", "part", [MK]),
  lil("لسَّبَبِيَّةِ", "sababiyya", [MK, "lam-taleel"], "السَّبَبِيَّةِ مَجْرُورٌ — خَبَرٌ.", "«for cause» — the khabar.", "«sebebiyet için» — haber.", punct="،"),
  wa_quoted("إِذَنْ", "idhan-jawab", "part", [MK]),
  lil("لشَّرْطِ", "shart", [MK], "الشَّرْطِ مَجْرُورٌ — خَبَرٌ.", "«for condition» — the khabar.", "«şart için» — haber."),
  tok("وَالْجَزَاءِ", "jaza-answer", "noun", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَالْجَزَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and answer»", "«ve cezâ»", punct="،", segments=wa("الْجَزَاءِ", "jaza-answer", "noun")),
 ]})
# ----------- s3 — the condition of idhan's governing
S.append({"id": "s3", "translation": {"en": "and the condition of its governing is that the verb be a future one, not leaning on what comes before it;", "tr": "amelinin şartı, fiilin istikbâl fiili olması ve kendinden öncekine dayanmamasıdır;"},
 "tokens": [
  tok("وَشَرْطُ", "shart", "noun", [K, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَشَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the condition of» — the mubtada.", "«ve şartı» — mübtedâ.", segments=wa("شَرْطُ", "shart", "noun")),
  tok("عَمَلِهِ", "amal-governing", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَمَلِ إِذَنْ.", "«its governing» — of إِذَنْ.", "«amelinin» — izen'in.", segments=[seg("عَمَلِ", "amal-governing", "noun"), pr3msi()]),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, MK], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("يَكُونَ", "kana", "verb", [K, AM, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْمُضَارِعُ.", "«be» — its ism concealed: the muḍāriʿ.", "«olması» — ismi müstetir: muzâri."),
  tok("فِعْلًا", "fil", "noun", [K, KN], "خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a verb» — the khabar of kāna.", "«bir fiil» — kâne'nin haberi."),
  tok("مُسْتَقْبَلًا", "mustaqbal", "noun", [K, NA, "ism-maful", "form-x-verbs"], "نَعْتٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنَ اسْتَقْبَلَ: دَالًّا عَلَى الِاسْتِقْبَالِ.", "«future» — the naʿt: signifying the time to come.", "«istikbâl» — sıfat: gelecek zamana delâlet eden."),
  tok("غَيْرَ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«not» — a second naʿt, annexed.", "«olmayan» — ikinci sıfat, muzâf."),
  tok("مُعْتَمِدٍ", "mutamid", "noun", [K, ID, "ism-fail", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ اعْتَمَدَ.", "«leaning» — ism fāʿil of اعْتَمَدَ.", "«dayanan» — i'temede'nin ism-i fâili."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("مَا", "ma-mawsula", "pron", [K, MW, HJ], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what» — the relative.", "«şey» — ism-i mevsûl."),
  tok("قَبْلَهُ", "qabla", "noun", [K, MF, ID, MW, HT], "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةٍ مَحْذُوفَةٍ: اسْتَقَرَّ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«comes before it» — the ẓarf, its ṣila dropped.", "«ondan önce olan» — zarf, sılası mahzûf.", punct="،", segments=[seg("قَبْلَ", "qabla", "noun"), pr3ms()]),
 ]})
# ----------- s4 — the two failures
S.append({"id": "s4", "translation": {"en": "and if the present is meant by it, or it leans on what comes before it, it does not govern — as in «then I think you a liar», to one who said this saying; and as in «I, then, honour you», to one who said «I came to you».", "tr": "fiille şimdiki zaman kastedilirse yahut öncesine dayanırsa amel etmez — bu sözü söyleyene «o halde seni yalancı sanırım» demek gibi; «sana geldim» diyene «ben o halde sana ikram ederim» demek gibi."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("أُرِيدَ", "arada", "verb", [K, SH, NF, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is meant» — the condition's verb, passive.", "«kastedilirse» — şart fiili, meçhul."),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — بِالْمُضَارِعِ.", "«by it» — by the muḍāriʿ.", "«onunla» — muzâri ile.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الْحَالُ", "hal", "noun", [K, NF], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — الزَّمَانُ الْحَاضِرُ.", "«the present» — the deputy doer: the present time.", "«hâl» — nâib-i fâil: şimdiki zaman."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ — كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — its kasra for the two sukūns.", "«yahut» — iki sâkin için kesre."),
  tok("اعْتَمَدَ", "itamada", "verb", [K, SH, AT, FL, "form-viii-verbs"], "فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى أُرِيدَ فِي مَحَلِّ جَزْمٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْمُضَارِعُ.", "«it leans» — joined to the condition's verb.", "«dayanırsa» — şart fiiline ma'tûf."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("مَا", "ma-mawsula", "pron", [K, MW, HJ], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«şey»"),
  tok("قَبْلَهُ", "qabla", "noun", [K, MF, ID, MW, HT], "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةٍ مَحْذُوفَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«comes before it»", "«ondan önce olan»", segments=[seg("قَبْلَ", "qabla", "noun"), pr3ms()]),
  tok("لَمْ", "lam", "part", [K, LJz, SH], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("تَعْمَلْ", "amila", "verb", [K, LJz, SH], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ — جَوَابُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — إِذَنْ.", "«it governs» — the answer, majzūm; the doer is إِذَنْ.", "«amel eder» — cevap, meczûm; fâil izen.", punct="،"),
  nahw(),
  tok("إِذَنْ", "idhan-jawab", "part", [K, "jawab-al-talab", HT], "حَرْفُ جَوَابٍ وَجَزَاءٍ مُهْمَلٌ — لِأَنَّ الْفِعْلَ لِلْحَالِ.", "«then» — ungoverning: the verb is present.", "«o halde» — amelsiz: fiil hâl içindir."),
  tok("أَظُنُّكَ", "zanna", "verb", [K, ZN, "mafulayn", MR, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — لَمْ تَنْصِبْهُ إِذَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ أَوَّلُ.", "«I think you» — in RAFʿ: إِذَنْ did not put it in naṣb; the kāf is the first object.", "«seni sanırım» — REF'te: izen nasb etmedi; kâf birinci mef'ûl.", segments=[seg("أَظُنُّ", "zanna", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("كَاذِبًا", "kadhib-liar", "noun", [K, ZN, "mafulayn", "ism-fail"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a liar» — the second object.", "«yalancı» — ikinci mef'ûl.", punct="،"),
  tok("لِمَنْ", "man", "pron", [K, HJ, MW], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — يُقَالُ ذَلِكَ لِمَنْ.", "«to one who» — said to him who.", "«… diyene» — ona denir.", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man", "pron")]),
  tok("قَالَ", "qala", "verb", [K, MW, FL, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«said» — the ṣila.", "«söyleyen» — sıla."),
  tok("هَذَا", "hadha", "pron", [K, MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this» — the object.", "«bu» — mef'ûl."),
  tok("الْقَوْلَ", "qawl", "noun", [K, "badal", MB], "بَدَلٌ مِنْ هَذَا مَنْصُوبٌ — فَالظَّنُّ هُنَا فِي الْحَالِ.", "«saying» — the badal: the thinking is in the present.", "«sözü» — bedel: zan burada hâldedir.", punct="؛"),
  wanahw(),
  tok("أَنَا", "ana", "pron", [K, MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — اعْتَمَدَ عَلَيْهِ إِذَنْ.", "«I» — the mubtada إِذَنْ leans on.", "«ben» — izen'in dayandığı mübtedâ."),
  tok("إِذَنْ", "idhan-jawab", "part", [K, "jawab-al-talab", HT], "حَرْفُ جَوَابٍ مُهْمَلٌ — لِاعْتِمَادِ مَا بَعْدَهُ عَلَى مَا قَبْلَهُ.", "«then» — ungoverning: it leans on what precedes.", "«o halde» — amelsiz: öncesine dayanıyor."),
  tok("أُكْرِمُكَ", "akrama", "verb", [K, MK, MB, MR, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ أَنَا.", "«I honour you» — in RAFʿ; the khabar of «I».", "«sana ikram ederim» — REF'te; «ben»in haberi.", punct="،", segments=[seg("أُكْرِمُ", "akrama", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("لِمَنْ", "man", "pron", [K, HJ, MW], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who»", "«… diyene»", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man", "pron")]),
  tok("قَالَ", "qala", "verb", [K, MW, FL, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«said»", "«söyleyen»", punct=":"),
  tok("جِئْتُكَ", "jaa", "verb", [K, FL, MB, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — مَقُولُ الْقَوْلِ.", "«I came to you» — the said thing.", "«sana geldim» — makûlü'l-kavl.", punct=".", segments=[seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("كَ", "pron-2ms", "pron")]),
 ]})
# ----------- s5 — the concealed an
S.append({"id": "s5", "translation": {"en": "And the concealing of أَنْ in particular is allowed, so the muḍāriʿ takes naṣb by it — as in «visit me, so that I may honour you».", "tr": "Yalnız en'in gizlenmesi câizdir; muzâri onunla nasb olur — «beni ziyaret et ki sana ikram edeyim» gibi."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, FL, "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("إِضْمَارُ", "idmar", "noun", [K, FL, ID, "masdar", "form-iv-verbs"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ أَضْمَرَ.", "«the concealing of» — the doer; the masdar of أَضْمَرَ.", "«gizlenmesi» — fâil; admara'nın masdarı."),
  quoted("أَنْ", "an-masdariyya", "part", [AM, ID], "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«an» — quoted; the muḍāf ilayh.", "«en» — hikâye edilmiş; muzâfun ileyh."),
  tok("خَاصَّةً", "khassa", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ — دُونَ أَخَوَاتِهَا.", "«in particular» — the ḥāl: not its sisters.", "«yalnız» — hâl: kardeşleri değil."),
  tok("فَيَنْتَصِبُ", "intasaba", "verb", [K, FL, "form-viii-verbs", MR], "الْفَاءُ لِلتَّفْرِيعِ، وَيَنْتَصِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«so takes naṣb»", "«böylece nasb olur»", segments=fa("يَنْتَصِبُ", "intasaba", "verb")),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, FL, MR], "فَاعِلٌ مَرْفُوعٌ.", "«the muḍāriʿ» — the doer.", "«muzâri» — fâil."),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — بِأَنِ الْمُضْمَرَةِ.", "«by it» — by the concealed أَنْ.", "«onunla» — gizli en ile.", punct="،", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  nahw(),
  zurni(),
  tok("فَأُكْرِمَكَ", "akrama", "verb", [K, AM, JT, MB, HT, "form-iv-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَأُكْرِمَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ فَاءِ السَّبَبِيَّةِ فِي جَوَابِ الْأَمْرِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ.", "«so that I may honour you» — in NAṢB by a concealed أَنْ after the fāʾ of cause in the answer to the command.", "«ki sana ikram edeyim» — emrin cevabında sebebiyet fâsından sonra gizli en ile NASB.", punct=".", segments=[seg("فَ", "fa", "conj"), seg("أُكْرِمَ", "akrama", "verb"), seg("كَ", "pron-2ms", "pron")]),
 ]})
# ----------- s6 — the jazim: fifteen words; the four letters
S.append({"id": "s6", "translation": {"en": "And the jāzim is fifteen words: four of them are letters that put one verb in jazm, namely لَمْ and لَمَّا for the negation of the past, and the lām of command and the لَا of prohibition for request;", "tr": "Câzim on beş kelimedir: dördü tek bir fiili cezm eden harflerdir — mâzîyi nefiy için lem ve lemmâ, talep için emir lâmı ve nehiy lâ'sı;"},
 "tokens": [
  tok("وَالْجَازِمُ", "jazim", "noun", [K, MK, "ism-fail"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْجَازِمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the jāzim» — the mubtada.", "«câzim» — mübtedâ.", segments=wa("الْجَازِمُ", "jazim", "noun")),
  tok("خَمْسَ", "khams", "noun", [K, MK, TM], "خَبَرٌ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ — الْعَدَدُ الْمُرَكَّبُ.", "«fifteen» — the compound number, built on fatḥ in both parts; the khabar.", "«on beş» — mürekkep sayı, iki cüz'ü fetha üzere mebnî; haber."),
  tok("عَشْرَةَ", "ashara", "noun", [K, MK, TM], "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ، مَبْنِيٌّ عَلَى الْفَتْحِ — مُؤَنَّثٌ لِأَنَّ الْمَعْدُودَ كَلِمَةٌ.", "«-teen» — the second part, feminine because the counted noun is feminine.", "«on» — ikinci cüz', ma'dûd müennes olduğu için müennes."),
  tok("كَلِمَةً", "kalima", "noun", [K, TM], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — مُفْرَدٌ بَعْدَ الْعَدَدِ الْمُرَكَّبِ.", "«words» — the tamyīz, singular after a compound number.", "«kelime» — temyîz, mürekkep sayıdan sonra müfred.", punct=":"),
  tok("أَرْبَعَةٌ", "arbaa", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«four» — the mubtada.", "«dördü» — mübtedâ."),
  minha(),
  tok("حُرُوفٌ", "harf", "noun", [K, MK, "jam-taksir"], "خَبَرٌ مَرْفُوعٌ.", "«are letters» — the khabar.", "«harflerdir» — haber."),
  tok("تَجْزِمُ", "jazama", "verb", [K, NA, FL, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ نَعْتٌ لِحُرُوفٍ.", "«that put in jazm» — the clause is the naʿt of «letters».", "«cezm eden» — cümle «harfler»in sıfatı."),
  tok("فِعْلًا", "fil", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a verb» — the object.", "«bir fiili» — mef'ûl."),
  tok("وَاحِدًا", "wahid", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«one» — the naʿt.", "«tek» — sıfat.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are» — the mubtada.", "«ve onlar» — mübtedâ.", punct=":"),
  quoted("لَمْ", "lam", "part", [LJz, MK], "خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«lam» — quoted; the khabar.", "«lem» — hikâye edilmiş; haber."),
  wa_quoted("لَمَّا", "lamma", "part", [LJz, MK]),
  lil("لنَّفْيِ", "nafy", [MK, LJz, "masdar"], "النَّفْيِ مَجْرُورٌ — مُتَعَلِّقٌ بِحَالٍ: كَائِنَتَيْنِ لِلنَّفْيِ.", "«for the negation» — what the two are for.", "«nefiy için» — ikisinin işi."),
  tok("الْمَاضِي", "madi", "noun", [K, NA, "ism-maqsur-manqus", "ism-fail"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — نَفْيُ الْمَاضِي: لَمْ يَفْعَلْ، لَمَّا يَفْعَلْ.", "«of the past» — negation turned to the past: لَمْ يَفْعَلْ، لَمَّا يَفْعَلْ.", "«mâzîyi» — mâzîye çevrilmiş nefiy: lem yef'al, lemmâ yef'al.", punct="،"),
  tok("وَلَامُ", "lam-letter", "noun", [K, AT, ID, LA], "الْوَاوُ عَاطِفَةٌ، وَلَامُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ الْحَرْفِ.", "«and the lām of» — the letter's name, annexed.", "«ve lâmı» — harfin adı, muzâf.", segments=wa("لَامُ", "lam-letter", "noun")),
  tok("الْأَمْرِ", "amr", "noun", [K, ID, LA, "imperative-amr"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لِيَفْعَلْ.", "«command» — لِيَفْعَلْ.", "«emir» — li-yef'al."),
  tok("وَلَا", "la-nahiya", "part", [K, AT, ID, NH, HT], "الْوَاوُ عَاطِفَةٌ، وَلَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ، مُضَافٌ.", "«and the lā of» — quoted, annexed.", "«ve lâ'sı» — hikâye edilmiş, muzâf.", segments=wa("لَا", "la-nahiya", "part")),
  tok("النَّهْيِ", "nahy", "noun", [K, ID, NH, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَا تَفْعَلْ.", "«prohibition» — لَا تَفْعَلْ.", "«nehiy» — lâ tef'al."),
  lil("لطَّلَبِ", "talab", [LA, NH, "masdar"], "الطَّلَبِ مَجْرُورٌ — مُتَعَلِّقٌ بِحَالٍ: كَائِنَيْنِ لِلطَّلَبِ.", "«for request» — the command and the prohibition both ask.", "«talep için» — emir de nehiy de ister.", punct="،"),
 ]})
# ----------- s7 — the eleven words of requital
S.append({"id": "s7", "translation": {"en": "and eleven of them put two verbs in jazm if both are muḍāriʿ — they are called the words of requital — namely إِنْ for condition and answer; حَيْثُمَا, أَيْنَ and أَنَّى for place; إِذْمَا, إِذَا مَا and مَتَى for time; and مَهْمَا, مَا, أَيٌّ and مَنْ.", "tr": "on biri ise, ikisi de muzâri olduğunda iki fiili cezm eder — bunlara mücâzât kelimeleri denir — şart ve cezâ için in; mekân için haysümâ, eyne ve ennâ; zaman için izmâ, izâ mâ ve metâ; ve mehmâ, mâ, eyyün ve men."},
 "tokens": [
  tok("وَأَحَدَ", "ahad", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَأَحَدَ الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمُرَكَّبِ، مَبْنِيٌّ عَلَى الْفَتْحِ — مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and eleven» — the compound number, the mubtada.", "«on biri ise» — mürekkep sayı, mübtedâ.", segments=wa("أَحَدَ", "ahad", "noun")),
  tok("عَشَرَ", "ashar", "noun", [K, MK, TM], "الْجُزْءُ الثَّانِي، مَبْنِيٌّ عَلَى الْفَتْحِ — مُذَكَّرٌ لِأَنَّ الْمَعْدُودَ: كَلِمَاتٌ عَلَى تَأْوِيلِ شَيْءٍ.", "«-teen» — the second part (the lithograph's masculine form kept).", "«on» — ikinci cüz' (taşbaskının müzekker şekli korundu)."),
  minha(),
  tok("تَجْزِمُ", "jazama", "verb", [K, MK, FL, MR], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«put in jazm» — the clause is the khabar.", "«cezm eder» — cümle haber."),
  tok("فِعْلَيْنِ", "fil", "noun", [K, MB, MTH], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — فِعْلُ الشَّرْطِ وَجَوَابُهُ.", "«two verbs» — the dual object: the condition's verb and its answer.", "«iki fiili» — tesniye mef'ûl: şart fiili ve cevabı."),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("كَانَا", "kana", "verb", [K, SH, KN, "hollow-verbs", MTH], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ، وَالْأَلِفُ اسْمُهُ.", "«both are» — the condition's verb; the alif is its ism.", "«ikisi … olursa» — şart fiili; elif ismi.", segments=[seg("كَانَ", "kana", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("مُضَارِعَيْنِ", "mudari", "noun", [K, KN, MTH, HT], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«muḍāriʿ» — kāna's khabar; the answer is dropped, shown by what precedes.", "«muzâri» — kâne'nin haberi; cevap mahzûf, öncesi gösterir.", punct="،"),
  tok("تُسَمَّى", "samma", "verb", [K, NF, "mafulayn", "form-ii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ حَالٌ.", "«they are called» — the passive; its deputy doer concealed.", "«denir» — meçhul; nâib-i fâil müstetir."),
  tok("كَلِمَ", "kalim", "noun", [K, "mafulayn", ID, "jam-taksir"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ — اسْمُ جِنْسٍ جَمْعِيٌّ لِكَلِمَةٍ.", "«the words of» — the second object; the collective of كَلِمَة.", "«kelimeleri» — ikinci mef'ûl; kelimenin cins ismi."),
  tok("الْمُجَازَاةِ", "mujazat", "noun", [K, ID, "masdar", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ جَازَى: الشَّرْطُ وَالْجَزَاءُ.", "«requital» — the masdar of Form III: condition and answer.", "«mücâzât» — müfâale masdarı: şart ve cezâ.", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are» — the mubtada.", "«ve onlar» — mübtedâ.", punct=":"),
  quoted("إِنْ", "in-shartiyya", "part", [SH, MK], "خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«in» — quoted; the khabar.", "«in» — hikâye edilmiş; haber."),
  lil("لشَّرْطِ", "shart", [MK, SH], "الشَّرْطِ مَجْرُورٌ.", "«for condition»", "«şart için»"),
  tok("وَالْجَزَاءِ", "jaza-answer", "noun", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَالْجَزَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and answer»", "«ve cezâ»", punct="،", segments=wa("الْجَزَاءِ", "jaza-answer", "noun")),
  wa_quoted("حَيْثُمَا", "haythuma", "pron", [SH, MK]),
  wa_quoted("أَيْنَ", "ayna", "pron", [SH, MK]),
  wa_quoted("أَنَّى", "anna-shartiyya", "pron", [SH, MK]),
  lil("لْمَكَانِ", "makan", [SH, MF], "الْمَكَانِ مَجْرُورٌ — ظُرُوفُ مَكَانٍ تَضَمَّنَتْ مَعْنَى الشَّرْطِ.", "«for place» — ẓarfs of place carrying the condition.", "«mekân için» — şart mânâsı taşıyan mekân zarfları.", punct="،"),
  wa_quoted("إِذْمَا", "idhma", "part", [SH, MK]),
  tok("وَإِذَا", "idha", "part", [K, SH, IDH, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَإِذَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — لَا تَجْزِمُ إِلَّا مَعَ مَا.", "«and idhā» — quoted; it jazms only with مَا after it.", "«ve izâ» — hikâye edilmiş; yalnız ardındaki mâ ile cezm eder.", segments=wa("إِذَا", "idha", "part")),
  tok("مَا", "ma-zaida", "part", [K, SH, IDH, "anwa-ma", "tawkid"], "مَا الزَّائِدَةُ الْكَافَّةُ — بِهَا صَارَتْ إِذَا جَازِمَةً.", "«mā» — the added mā: with it إِذَا jazms.", "«mâ» — zâid mâ: onunla izâ cezm eder."),
  wa_quoted("مَتَى", "mata", "pron", [SH, MK]),
  lil("لزَّمَانِ", "zaman", [SH, MF], "الزَّمَانِ مَجْرُورٌ — ظُرُوفُ زَمَانٍ تَضَمَّنَتْ مَعْنَى الشَّرْطِ.", "«for time» — ẓarfs of time carrying the condition.", "«zaman için» — şart mânâsı taşıyan zaman zarfları.", punct="،"),
  wa_quoted("مَهْمَا", "mahma", "pron", [SH, MK]),
  wa_quoted("مَا", "ma-shartiyya", "pron", [SH, MK, "anwa-ma"]),
  wa_quoted("أَيٌّ", "ayy", "pron", [SH, MK]),
  wa_quoted("مَنْ", "man", "pron", [SH, MK], punct="."),
 ]})
# ----------- s8 — the concealed in
S.append({"id": "s8", "translation": {"en": "And the concealing of إِنْ in particular is allowed, so the muḍāriʿ is put in jazm by it — as in «visit me, I shall honour you».", "tr": "Yalnız in'in gizlenmesi câizdir; muzâri onunla cezm olur — «beni ziyaret et, sana ikram ederim» gibi."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, FL, "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("إِضْمَارُ", "idmar", "noun", [K, FL, ID, "masdar", "form-iv-verbs"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the concealing of» — the doer.", "«gizlenmesi» — fâil."),
  quoted("إِنْ", "in-shartiyya", "part", [SH, ID], "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«in» — quoted; the muḍāf ilayh.", "«in» — hikâye edilmiş; muzâfun ileyh."),
  tok("خَاصَّةً", "khassa", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ — دُونَ سَائِرِ الْجَوَازِمِ.", "«in particular» — the ḥāl: not the other jāzims.", "«yalnız» — hâl: öteki câzimler değil."),
  tok("فَيُجْزَمُ", "jazama", "verb", [K, NF, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَيُجْزَمُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«so is put in jazm» — the passive.", "«böylece cezm olur» — meçhul.", segments=fa("يُجْزَمُ", "jazama", "verb")),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, NF, MR], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«the muḍāriʿ» — the deputy doer.", "«muzâri» — nâib-i fâil."),
  tok("بِهَا", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — بِإِنِ الْمُضْمَرَةِ.", "«by it» — by the concealed إِنْ.", "«onunla» — gizli in ile.", punct="،", segments=[seg("بِ", "bi", "prep"), pr3fs()]),
  nahw(),
  zurni(),
  tok("أُكْرِمْكَ", "akrama", "verb", [K, SH, JT, MB, HT, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِإِنْ مُضْمَرَةٍ فِي جَوَابِ الطَّلَبِ: إِنْ تَزُرْنِي أُكْرِمْكَ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I shall honour you» — in JAZM by a concealed إِنْ in the answer to the request: if you visit me, I honour you.", "«sana ikram ederim» — talebin cevabında gizli in ile CEZM: beni ziyaret edersen ikram ederim.", punct=".", segments=[seg("أُكْرِمْ", "akrama", "verb"), seg("كَ", "pron-2ms", "pron")]),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i]]

CAND = {
 "nasib": G("nasib", "نَاصِب", "ن ص ب", "noun", "a nāṣib — a governor that puts the muḍāriʿ in naṣb (ism fāʿil of نَصَبَ)", "nâsıb — muzâriyi nasb eden âmil", 4),
 "jazim": G("jazim", "جَازِم", "ج ز م", "noun", "a jāzim — a governor that puts the muḍāriʿ in jazm (ism fāʿil of جَزَمَ)", "câzim — muzâriyi cezm eden âmil", 4),
 "jazama": G("jazama", "جَزَمَ", "ج ز م", "verb", "to put (a verb) in jazm; to cut off", "cezm etmek; kesmek", 4),
 "arbaa": G("arbaa", "أَرْبَعَة", "ر ب ع", "noun", "four (with a masculine counted noun)", "dört (müzekker ma'dûdla)", 1),
 "masdariyya": G("masdariyya", "الْمَصْدَرِيَّة", "ص د ر", "noun", "the masdar-sense — a letter and its verb equalling a masdar: أَنْ تَقُومَ = قِيَامُكَ", "masdariyet — harf ile fiilinin bir masdara denk gelmesi", 5),
 "lan": G("lan", "لَنْ", None, "part", "never — negates the future with emphasis; a nāṣib of the muḍāriʿ", "len — istikbâli te'kitle nefyeder; muzârinin nâsıbı", 2),
 "muakkad": G("muakkad", "مُؤَكَّد", "أ ك د", "noun", "emphatic, strengthened (ism mafʿūl of أَكَّدَ)", "müekked — te'kitli", 3),
 "istiqbal": G("istiqbal", "الِاسْتِقْبَال", "ق ب ل", "noun", "the future, the time to come (masdar of اسْتَقْبَلَ)", "istikbâl — gelecek zaman", 3),
 "sababiyya": G("sababiyya", "السَّبَبِيَّة", "س ب ب", "noun", "the sense of cause — what follows is the reason or purpose: كَيْ, فَاءُ السَّبَبِيَّةِ", "sebebiyet — sonrakinin sebep yahut gaye olması: key, sebebiyet fâsı", 5),
 "idhan-jawab": G("idhan-jawab", "إِذَنْ", None, "part", "then, in that case — the letter of answer and requital; a nāṣib of the muḍāriʿ when the verb is future and leans on nothing before it", "izen — o halde; cevap ve cezâ harfi; fiil istikbâl olup öncesine dayanmadığında muzârinin nâsıbı", 4),
 "mustaqbal": G("mustaqbal", "مُسْتَقْبَل", "ق ب ل", "noun", "future — a verb signifying the time to come (ism mafʿūl of اسْتَقْبَلَ)", "müstakbel — gelecek zamana delâlet eden", 3),
 "mutamid": G("mutamid", "مُعْتَمِد", "ع م د", "noun", "leaning on, depending on (ism fāʿil of اعْتَمَدَ)", "mu'temid — dayanan", 4),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend; (passive) to be meant", "istemek, kastetmek; (meçhul) kastedilmek", 2, form="IV"),
 "itamada": G("itamada", "اِعْتَمَدَ", "ع م د", "verb", "to lean on, to depend on (Form VIII)", "dayanmak, itimat etmek (iftiâl)", 3, form="VIII"),
 "man": G("man", "مَنْ", None, "pron", "who, whoever — the relative and conditional noun (the mīm's fatḥa tells it from مِنْ)", "kim, her kim — ism-i mevsûl ve şart ismi", 1),
 "zara": G("zara", "زَارَ", "ز و ر", "verb", "to visit", "ziyaret etmek", 2),
 "idmar": G("idmar", "إِضْمَار", "ض م ر", "noun", "concealing — leaving a governor unspoken but intended (masdar of أَضْمَرَ)", "izmâr — âmili söylemeyip kastetmek", 4),
 "khassa": G("khassa", "خَاصَّة", "خ ص ص", "noun", "in particular, specifically (as a ḥāl: خَاصَّةً)", "hâssaten, yalnız (hâl olarak: hâssaten)", 3),
 "khams": G("khams", "خَمْس", "خ م س", "noun", "five (with a feminine counted noun); خَمْسَ عَشْرَةَ fifteen", "beş (müennes ma'dûdla); hams aşrata on beş", 1),
 "ashara": G("ashara", "عَشَرَة", "ع ش ر", "noun", "ten; عَشْرَةَ the feminine second part of 13-19", "on; aşrata 13-19'un müennes ikinci cüz'ü", 1),
 "ashar": G("ashar", "عَشَرَ", "ع ش ر", "noun", "-teen — the masculine second part of 11-19", "on — 11-19'un müzekker ikinci cüz'ü", 1),
 "lam-letter": G("lam-letter", "لَام", None, "noun", "the letter lām; لَامُ الْأَمْرِ the lām of command (لِيَفْعَلْ)", "lâm harfi; lâmü'l-emr — emir lâmı (li-yef'al)", 2),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "the prohibiting lā — puts the muḍāriʿ in jazm: لَا تَفْعَلْ", "nehiy lâ'sı — muzâriyi cezm eder: lâ tef'al", 2),
 "talab": G("talab", "طَلَب", "ط ل ب", "noun", "request, demand — the command and the prohibition", "talep, isteme — emir ve nehiy", 3),
 "kalim": G("kalim", "كَلِم", "ك ل م", "noun", "words — the collective of كَلِمَة", "kelimeler — kelimenin cins ismi", 3),
 "mujazat": G("mujazat", "الْمُجَازَاة", "ج ز ي", "noun", "requital — condition and its answer (masdar of جَازَى); كَلِمُ الْمُجَازَاةِ the conditional words", "mücâzât — şart ve cezâsı; kelimü'l-mücâzât — şart kelimeleri", 5),
 "haythuma": G("haythuma", "حَيْثُمَا", None, "pron", "wherever — a conditional ẓarf of place", "nerede … -sa — şart mânâlı mekân zarfı", 3),
 "ayna": G("ayna", "أَيْنَ", None, "pron", "where; wherever (conditional)", "nerede; her nerede (şart)", 1),
 "anna-shartiyya": G("anna-shartiyya", "أَنَّى", None, "pron", "wherever, however — a conditional ẓarf", "her nerede, nasıl … -sa — şart zarfı", 3),
 "idhma": G("idhma", "إِذْمَا", None, "part", "whenever — إِذْ with مَا, a conditional letter", "ne zaman … -sa — mâ'lı iz, şart harfi", 3),
 "ma-zaida": G("ma-zaida", "مَا (الزَّائِدَة)", None, "part", "the added mā — strengthens, or lets a word govern as a condition", "zâid mâ — pekiştirir yahut kelimeye şart ameli verir", 3),
 "mata": G("mata", "مَتَى", None, "pron", "when; whenever (conditional)", "ne zaman (şart)", 2),
 "mahma": G("mahma", "مَهْمَا", None, "pron", "whatever — a conditional noun", "her ne … -sa — şart ismi", 2),
 "ma-shartiyya": G("ma-shartiyya", "مَا (الشَّرْطِيَّة)", None, "pron", "whatever — the conditional mā that jazms two verbs", "şart mâ'sı — iki fiili cezm eder", 3),
 "ayy": G("ayy", "أَيّ", None, "pron", "which, whichever — the declining conditional and interrogative noun", "hangi — i'râb alan şart ve istifhâm ismi", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "jazama", _sg.sound1("daraba", "جَزَم", "جْزِم", "اِجْزِم", "جَزْم", "جَازِم", "مَجْزُوم", "جُزِمَ", "يُجْزَمُ", "جَزَمَ يَجْزِمُ: قَطَعَ؛ وَفِي النَّحْوِ: أَسْكَنَ آخِرَ الْمُضَارِعِ — بَابُ ضَرَبَ"))
put_morph(mo, "itamada", _sg.derived(_sg.B8, _sg.W8, "َ", "اِعْتَمَد", "عْتَمِد", "اِعْتَمِد", "اِعْتِمَاد", "مُعْتَمِد", "مُعْتَمَد", "اُعْتُمِدَ", "يُعْتَمَدُ", "اِعْتَمَدَ يَعْتَمِدُ: اتَّكَأَ عَلَيْهِ — بَابُ الِافْتِعَالِ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch7 gloss+morph ok", len(GLOSS_ADD), "verbs:", [k for k in ("jazama", "itamada", "arada", "zara") if k in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "نَوَاصِبُ الْمُضَارِعِ وَجَوَازِمُهُ", "en": "The nāṣibs and the jāzims of the muḍāriʿ", "tr": "Muzârinin nâsıbları ve câzimleri"},
 "level": 4, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العامل في الفعل المضارع", "العوامل المائة للبركوي", "الكافية لابن الحاجب — عوامل الفعل"],
 "amil": "أَنْ، لَنْ، كَيْ، إِذَنْ — four nāṣibs; لَمْ، لَمَّا، لَامُ الْأَمْرِ، لَا النَّهْيِ — four jāzims of one verb; إِنْ and ten more — eleven jāzims of two verbs; أَنْ and إِنْ alone may be concealed",
 "question": {
  "en": ["How many kinds of governor enter the muḍāriʿ? Two: a NĀṢIB, which gives it the fatḥa (أَنْ يَفْعَلَ), and a JĀZIM, which takes its ḍamma away (لَمْ يَفْعَلْ).",
         "Which four letters put it in naṣb, and what does each mean? أَنْ turns the verb into a masdar (أَنْ تَقُومَ = قِيَامُكَ); لَنْ negates the future with emphasis; كَيْ gives the cause; إِذَنْ answers a speaker with «then».",
         "When does إِذَنْ govern? Only when its verb is FUTURE and leans on nothing before it. إِذَنْ أَظُنُّكَ كَاذِبًا — the thinking is in the present, so rafʿ; أَنَا إِذَنْ أُكْرِمُكَ — the verb leans on أَنَا, so rafʿ.",
         "May a nāṣib be unspoken? Only أَنْ: زُرْنِي فَأُكْرِمَكَ — after the fāʾ of cause in the answer to a command, أَنْ is concealed and the verb takes the fatḥa.",
         "What are the fifteen jāzims? Four letters that jazm ONE verb — لَمْ and لَمَّا (negation of the past), the lām of command and the لَا of prohibition (request) — and eleven words that jazm TWO verbs, the condition and its answer: إِنْ, then حَيْثُمَا أَيْنَ أَنَّى for place, إِذْمَا إِذَا مَا مَتَى for time, and مَهْمَا مَا أَيٌّ مَنْ.",
         "May a jāzim be unspoken? Only إِنْ: زُرْنِي أُكْرِمْكَ — the answer to the request is majzūm by a concealed إِنْ (إِنْ تَزُرْنِي أُكْرِمْكَ).",
         "What does the engine READ here? The DabtEngine writes the fatḥa after أَنْ, لَنْ, كَيْ and a governing إِذَنْ, the sukūn after لَمْ, لَمَّا, the lām of command, لَا of prohibition and the eleven words of requital, keeps the ḍamma on a present-tense or leaning إِذَنْ-verb, and reads the concealed أَنْ after the fāʾ of cause and the concealed إِنْ in the answer to a request."],
  "tr": ["Muzâriye kaç tür âmil girer? İki: ona fetha veren NÂSIB (en yef'ale) ve zammesini alan CÂZİM (lem yef'al).",
         "Hangi dört harf nasb eder, her biri ne anlatır? En fiili masdara çevirir (en tekûme = kıyâmüke); len istikbâli te'kitle nefyeder; key sebebi verir; izen konuşana «o halde» diye cevap verir.",
         "İzen ne zaman amel eder? Yalnız fiili İSTİKBÂL olup öncesine dayanmadığında. İzen ezunnüke kâziben — zan hâldedir, ref'; ene izen ükrimüke — fiil ene'ye dayanır, ref'.",
         "Nâsıb gizlenebilir mi? Yalnız en: zürnî fe-ükrimeke — emrin cevabında sebebiyet fâsından sonra en gizlenir ve fiil fetha alır.",
         "On beş câzim nedir? TEK fiili cezm eden dört harf — lem ve lemmâ (mâzîyi nefiy), emir lâmı ve nehiy lâ'sı (talep) — ve İKİ fiili, şartı ve cevabını cezm eden on bir kelime: in; mekân için haysümâ eyne ennâ; zaman için izmâ izâ mâ metâ; ve mehmâ mâ eyyün men.",
         "Câzim gizlenebilir mi? Yalnız in: zürnî ükrimke — talebin cevabı gizli in ile meczûmdur (in tezürnî ükrimke).",
         "Motor burada neyi OKUR? DabtEngine en, len, key ve amel eden izen'den sonra fethayı; lem, lemmâ, emir lâmı, nehiy lâ'sı ve on bir mücâzât kelimesinden sonra sükûnu yazar; hâl bildiren yahut dayanan izen-fiilinde zammeyi korur; sebebiyet fâsından sonraki gizli en'i ve talebin cevabındaki gizli in'i okur."]
 },
 "plain": {"en": "The present-tense verb has two kinds of boss: four little words (أَنْ، لَنْ، كَيْ، إِذَنْ) give it a fatḥa; fifteen (لَمْ، لَمَّا, the command lām, the prohibition لَا, and eleven condition words like إِنْ، مَنْ، مَتَى) take its ḍamma away. After «visit me» the verb bends: with a fāʾ a fatḥa, without one a sukūn.",
           "tr": "Muzâri fiilin iki tür patronu var. Dört küçük kelime (en, len, key, izen) ona fetha verir; on beş kelime zammesini alır — dördü tek fiil için (lem, lemmâ, emir lâmı, nehiy lâ'sı), on biri şart ve cevabı için (in, men, mâ, metâ…). «Beni ziyaret et» de, sonraki fiil bükülür: fâ ile fetha, fâ'sız sükûn alır."},
 "explanation": {"en": "The governor in the muḍāriʿ verb is of two kinds, a nāṣib and a jāzim. The nāṣib is four letters: أَنْ for the masdar-sense, لَنْ for the emphatic negation in the future, كَيْ for cause, and إِذَنْ for condition and answer — the last governing only when its verb is future and leans on nothing before it, so إِذَنْ أَظُنُّكَ كَاذِبًا (present) and أَنَا إِذَنْ أُكْرِمُكَ (leaning on أَنَا) stay in rafʿ; أَنْ alone may be concealed, زُرْنِي فَأُكْرِمَكَ. The jāzim is fifteen words: four letters that jazm one verb — لَمْ and لَمَّا for the negation of the past, the lām of command and the لَا of prohibition for request — and eleven words of requital that jazm two muḍāriʿs — إِنْ for condition and answer, حَيْثُمَا أَيْنَ أَنَّى for place, إِذْمَا إِذَا مَا مَتَى for time, مَهْمَا مَا أَيٌّ مَنْ; إِنْ alone may be concealed, زُرْنِي أُكْرِمْكَ.",
                 "tr": "Muzâri fiildeki âmil iki türlüdür: nâsıb ve câzim. Nâsıb dört harftir: masdariyet için en, istikbâlde te'kitli nefiy için len, sebebiyet için key, şart ve cezâ için izen — sonuncusu yalnız fiili istikbâl olup öncesine dayanmadığında amel eder; o yüzden izen ezunnüke kâziben (hâl) ve ene izen ükrimüke (ene'ye dayanır) ref'te kalır; yalnız en gizlenebilir: zürnî fe-ükrimeke. Câzim on beş kelimedir: tek fiili cezm eden dört harf — mâzîyi nefiy için lem ve lemmâ, talep için emir lâmı ve nehiy lâ'sı — ve iki muzâriyi cezm eden on bir mücâzât kelimesi — şart ve cezâ için in, mekân için haysümâ eyne ennâ, zaman için izmâ izâ mâ metâ, mehmâ mâ eyyün men; yalnız in gizlenebilir: zürnî ükrimke."},
 "examples": [
  {"ar": "أَنْ لِلْمَصْدَرِيَّةِ، وَلَنْ لِلنَّفْيِ الْمُؤَكَّدِ فِي الِاسْتِقْبَالِ، وَكَيْ لِلسَّبَبِيَّةِ، وَإِذَنْ لِلشَّرْطِ وَالْجَزَاءِ", "en": "the four nāṣibs and their meanings", "tr": "dört nâsıb ve mânâları", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "إِذَنْ أَظُنُّكَ كَاذِبًا، وَأَنَا إِذَنْ أُكْرِمُكَ", "en": "إِذَنْ ungoverning: present tense; leaning on what precedes", "tr": "amelsiz izen: hâl; öncesine dayanma", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "زُرْنِي فَأُكْرِمَكَ", "en": "the concealed أَنْ after the fāʾ of cause", "tr": "sebebiyet fâsından sonra gizli en", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "لَمْ وَلَمَّا لِلنَّفْيِ الْمَاضِي، وَلَامُ الْأَمْرِ وَلَا النَّهْيِ لِلطَّلَبِ", "en": "the four jāzims of one verb", "tr": "tek fiili cezm eden dört harf", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "زُرْنِي أُكْرِمْكَ", "en": "the concealed إِنْ in the answer to a request", "tr": "talebin cevabında gizli in", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
 ],
 "commonMistakes": [
  {"wrong": "إِذَنْ أَظُنَّكَ كَاذِبًا", "right": "إِذَنْ أَظُنُّكَ كَاذِبًا", "why": {"en": "the thinking is in the present — إِذَنْ governs only a future verb, so the ḍamma stays", "tr": "zan hâldedir — izen yalnız istikbâl fiilinde amel eder, zamme kalır"}},
  {"wrong": "أَنَا إِذَنْ أُكْرِمَكَ", "right": "أَنَا إِذَنْ أُكْرِمُكَ", "why": {"en": "the verb leans on أَنَا before it — a leaning إِذَنْ does not govern", "tr": "fiil önündeki ene'ye dayanır — dayanan izen amel etmez"}},
  {"wrong": "زُرْنِي فَأُكْرِمُكَ", "right": "زُرْنِي فَأُكْرِمَكَ", "why": {"en": "after the fāʾ of cause in the answer to a command the verb takes naṣb by a concealed أَنْ", "tr": "emrin cevabında sebebiyet fâsından sonra fiil gizli en ile nasb olur"}},
  {"wrong": "زُرْنِي أُكْرِمُكَ", "right": "زُرْنِي أُكْرِمْكَ", "why": {"en": "the answer to a request without a fāʾ is majzūm by a concealed إِنْ", "tr": "fâ'sız talep cevabı gizli in ile meczûmdur"}},
 ],
}
ADD_EN = (" Chapter 7 (print pp. 99-101): the governor in the muḍāriʿ verb — the two kinds (s1); the four nāṣibs with their senses (s2), "
          "إِذَنْ's condition and the two examples where it fails (s3-s4), the concealed أَنْ (s5); the fifteen jāzims — the four letters of one "
          "verb (s6), the eleven words of requital (s7) and the concealed إِنْ (s8). The lithograph's «أحد عشر منها» is kept in its masculine form.")
ADD_TR = (" Yedinci bab (baskı s. 99-101): muzâri fiildeki âmil — iki tür (s1); mânâlarıyla dört nâsıb (s2), izen'in şartı ve amel etmediği "
          "iki örnek (s3-s4), gizli en (s5); on beş câzim — tek fiilin dört harfi (s6), on bir mücâzât kelimesi (s7) ve gizli in (s8). "
          "Taşbaskının «أحد عشر منها» ibaresi müzekker şekliyle korundu.")
write_out(7, S, TITLE, ADD_EN, ADD_TR, "pp. 99-101", GLOSS_ADD, notes=(NOTE,),
          related=((AM, [K]), (LA, [K]), (LJz, [K]), (NH, [K]), (SH, [K]), (IDH, [K]), (MR, [K]), (JT, [K]), (K1, [K])))
report(7, S, GLOSS_ADD, (NOTE,))
