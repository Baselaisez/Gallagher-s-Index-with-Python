# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 11: the SECOND division of the nāqiṣ verb — the verbs of APPROACH (أَفْعَالُ الْمُقَارَبَةِ):
# what carries the sense of nearness, whose khabar is never anything but a muḍāriʿ; عَسَى with its khabar a muḍāriʿ mostly WITH أَنْ
# (عَسَى زَيْدٌ أَنْ يَخْرُجَ), أَنْ sometimes dropped, and عَسَى tāmm with أَنْ and the muḍāriʿ (عَسَى أَنْ يَخْرُجَ زَيْدٌ); كَادَ with its khabar
# mostly a muḍāriʿ WITHOUT أَنْ (كَادَ زَيْدٌ يَخْرُجُ), sometimes with it; كَرَبَ like كَادَ in both ways; هَلْهَلَ طَفِقَ أَخَذَ أَنْشَأَ أَقْبَلَ هَبَّ
# جَعَلَ عَلِقَ with their khabar a muḍāriʿ without أَنْ; أَوْشَكَ used like عَسَى and كَادَ; and the bar on fronting their khabars.
# Print pp. 106–107 (from «والقسم الثاني» on p. 106 to the end of p. 107). The lithograph's garbled clause before this passage (the
# substitution of إِنْ / لَمْ for مَا) stays HELD BACK with chapter 10.
#   python3 author_izhar_ch11.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "afal-al-muqaraba"
K10 = "al-fil-al-tamm-wal-naqis"
TITLE = {"ar": "أَفْعَالُ الْمُقَارَبَةِ", "en": "The verbs of approach", "tr": "Mukârebe fiilleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; MTH = "al-muthanna"; IMF = "ism-maful"
MFN = "mafulayn"; HL = "hal"; HV = "hollow-verbs"; DV = "doubled-verbs"; F4 = "form-iv-verbs"; F10 = "form-x-verbs"; NQ = "naqis-verbs"; MSD = "masdar"; MQ = "ism-maqsur-manqus"; LN = "la-nafiya"; NSB = "nawasib-wa-jawazim-al-mudari"; MM = "maful-mutlaq"; MSN = "istithna"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«… gibi» — hazfedilmiş mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def qv(form, lex, en, tr, joined=True, punct=None, tags=()):
    """a verb of approach mentioned as a word (the first annexed to نَحْوُ, the rest joined by the wāw)"""
    f = ("وَ" if joined else "") + form
    return tok(f, lex, "verb", [K, KN, HT] + ([AT] if joined else []) + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ" + ("، مَعْطُوفٌ عَلَى الْأَوَّلِ فِي مَحَلِّ جَرٍّ" if joined else "، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ") + " — مِنْ أَفْعَالِ الْمُقَارَبَةِ.", en, tr, punct=punct, segments=wa(form, lex, "verb") if joined else None)
def khabaruhu(punct=None): return tok("وَخَبَرُهُ", "khabar-predicate", "noun", [K, AT, MK, ID, KN], "الْوَاوُ عَاطِفَةٌ، وَخَبَرُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its khabar» — a mubtada.", "«ve haberi» — mübtedâ.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("خَبَرُ", "khabar-predicate", "noun"), pr3ms()])
def an_quoted(form="أَنْ", role_ar="لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ: أَنْ الْمَصْدَرِيَّةُ", en="«an» — the particle mentioned as a word", tr="«en» — lafzı kastedilen harf", punct=None, segments=None, tags=()):
    return tok(form, "an-masdariyya", "part", [K, AM, HT] + list(tags), role_ar + ".", en, tr, punct=punct, segments=segments)
def an_used(punct=None): return tok("أَنْ", "an-masdariyya", "part", [K, AM, NSB], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to» — the masdar particle, governing nasb.", "«-mesi» — nasb eden mastar harfi.", punct=punct)
def waqad(): return tok("وَقَدْ", "qad", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part"))
def yakunu(): return tok("يَكُونُ", "kana", "verb", [K, KN, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is» — its ism concealed.", "«olur» — ismi gizli.")
def bila(): return tok("بِلَا", "la-nafiya", "part", [K, HJ, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا اسْمٌ بِمَعْنَى غَيْرٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«without» — bi + lā, «other than».", "«-sız» — bi + lâ, «gayr» anlamında.", segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part")])
def zayd(form, role_ar, en, tr, punct=None, tags=()): return tok(form, "zayd", "propn", [K] + list(tags), role_ar, en, tr, punct=punct)
def mudari_naat(form="الْمُضَارِعُ", role_ar="نَعْتٌ لِلْفِعْلِ مَرْفُوعٌ", en="«the muḍāriʿ» — a naʿt", tr="«muzâri» — na't", punct=None):
    return tok(form, "mudari", "noun", [K, NA], role_ar + ".", en, tr, punct=punct)

# ----------- s1 — the second division: the verbs of approach
S.append({"id": "s1", "translation": {"en": "And the second division is what indicates the sense of nearness, and is called THE VERBS OF APPROACH; their khabars are never anything but a muḍāriʿ verb.", "tr": "İkinci kısım yakınlık mânâsına delâlet edendir ve MUKÂREBE FİİLLERİ diye adlandırılır; haberleri muzâri fiilden başka bir şey olmaz."},
 "tokens": [
  tok("وَالْقِسْمُ", "qism", "noun", [K, AT, MK, K10], "الْوَاوُ عَاطِفَةٌ، وَالْقِسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the division» — the mubtada.", "«ve kısım» — mübtedâ.", segments=wa("الْقِسْمُ", "qism", "noun")),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — مَنْقُوصٌ.", "«the second» — a naʿt.", "«ikinci» — na't."),
  tok("مَا", "ma-mawsula", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan şey» — haber."),
  tok("يَدُلُّ", "dalla", "verb", [K, MW, DV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«indicates» — the ṣila.", "«delâlet eder» — sıla."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَعْنَى", "mana", "noun", [K, HJ, ID, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ.", "«the sense of», annexed.", "«mânâsına», muzâf."),
  tok("الْقُرْبِ", "qurb", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«nearness»", "«yakınlık»"),
  tok("وَيُسَمَّى", "samma", "verb", [K, AT, NF, MFN, NQ], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — الْمَفْعُولُ الْأَوَّلُ.", "«and is called» — the deputy concealed: the first object.", "«ve adlandırılır» — nâib gizli: birinci mef'ûl.", segments=wa("يُسَمَّى", "samma", "verb")),
  tok("أَفْعَالَ", "fil", "noun", [K, MFN, ID, "jam-taksir"], "مَفْعُولٌ ثَانٍ لِيُسَمَّى مَنْصُوبٌ، مُضَافٌ.", "«the verbs of» — the second object, annexed.", "«fiilleri» — ikinci mef'ûl, muzâf."),
  tok("الْمُقَارَبَةِ", "muqaraba", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ قَارَبَ.", "«approach»", "«mukârebe»", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … olmaz»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«are» — the nāqiṣ verb.", "«olur» — nâkıs fiil."),
  tok("أَخْبَارُهَا", "khabar-predicate", "noun", [K, KN, ID, "jam-taksir"], "اسْمُ يَكُونُ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their khabars» — the ism of yakūnu.", "«haberleri» — yekûnu'nun ismi.", segments=[seg("أَخْبَارُ", "khabar-predicate", "noun"), pr3fs()]),
  tok("إِلَّا", "illa", "part", [K, MSN], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except»", "«-den başka»"),
  tok("فِعْلًا", "fil", "noun", [K, KN, MSN], "خَبَرُ يَكُونُ مَنْصُوبٌ — الِاسْتِثْنَاءُ مُفَرَّغٌ.", "«a verb» — the khabar of yakūnu.", "«bir fiil» — yekûnu'nun haberi."),
  tok("مُضَارِعًا", "mudari", "noun", [K, NA], "نَعْتٌ مَنْصُوبٌ.", "«muḍāriʿ» — a naʿt.", "«muzâri» — na't.", punct="."),
 ]})
# ----------- s2 — عَسَى
S.append({"id": "s2", "translation": {"en": "As in عَسَى: its khabar is the muḍāriʿ verb, mostly with أَنْ — as in «Zayd may well go out» — and أَنْ is sometimes dropped; and it may be tāmm, with أَنْ and the muḍāriʿ — as in «it may well be that Zayd goes out».", "tr": "Asâ gibi: haberi muzâri fiildir, çoğunlukla en ile — «Zeyd'in çıkması umulur» gibi — bazen en hazfedilir; en ve muzâri ile tâm da olabilir — «Zeyd'in çıkması umulur» (asâ en yahruce Zeydün) gibi."},
 "tokens": [
  nahw(),
  qv("عَسَى", "asa-hope", "«ʿasā — may well, it is hoped» — the verb of hope, mentioned as a word.", "«asâ — umulur ki» — recâ fiili, lafzı kastedilmiş.", joined=False, punct="،", tags=[NQ]),
  khabaruhu(),
  tok("الْفِعْلُ", "fil", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the verb» — the khabar.", "«fiil» — haber."),
  mudari_naat(),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  an_quoted(role_ar="لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ: أَنْ الْمَصْدَرِيَّةُ"),
  tok("غَالِبًا", "ghalib", "noun", [K, HL], "حَالٌ مَنْصُوبٌ — فِي الْغَالِبِ.", "«mostly» — a ḥāl.", "«çoğunlukla» — hâl.", punct="،"),
  nahw(),
  tok("عَسَى", "asa-hope", "verb", [K, KN, NQ], "فِعْلٌ مَاضٍ جَامِدٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ (الرَّجَاءِ)، يَرْفَعُ الِاسْمَ وَخَبَرُهُ أَنْ وَالْفِعْلُ.", "«it may well be» — the verb of hope.", "«umulur» — recâ fiili."),
  zayd("زَيْدٌ", "اسْمُ عَسَى مَرْفُوعٌ.", "«Zayd» — the ism of ʿasā.", "«Zeyd» — asâ'nın ismi.", tags=[KN]),
  an_used(),
  tok("يَخْرُجَ", "kharaja", "verb", [K, NSB, KN, AM], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَأَنْ وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ خَبَرُ عَسَى.", "«go out» — naṣb by an; the clause is the khabar of ʿasā.", "«çıkmak» — en ile mansûb; cümle asâ'nın haberi.", punct="،"),
  waqad(),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is dropped»", "«hazfedilir»"),
  an_quoted(role_ar="لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، نَائِبُ فَاعِلٍ فِي مَحَلِّ رَفْعٍ: أَنْ", punct="،", tags=[NF]),
  waqad(),
  yakunu(),
  tok("تَامًّا", "tamm", "noun", [K, KN], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«tāmm» — the khabar.", "«tâm» — haber."),
  an_quoted(form="بِأَنْ", role_ar="الْبَاءُ حَرْفُ جَرٍّ، وَأَنْ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ مَجْرُورٌ فِي الْمَحَلِّ", en="«with an» — the particle mentioned, under the bā", tr="«en ile» — lafzı kastedilen harf, bâ ile mecrûr", segments=[seg("بِ", "bi", "prep"), seg("أَنْ", "an-masdariyya", "part")], tags=[HJ]),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāriʿ»", "«muzâri»", punct="،"),
  nahw(),
  tok("عَسَى", "asa-hope", "verb", [K, KN, NQ, FL], "فِعْلٌ مَاضٍ جَامِدٌ تَامٌّ، وَفَاعِلُهُ أَنْ وَالْفِعْلُ.", "«it may well be» — tāmm here: the an-clause its doer.", "«umulur» — burada tâm: en'li cümle fâili."),
  an_used(),
  tok("يَخْرُجَ", "kharaja", "verb", [K, NSB, AM, FL], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَأَنْ وَالْفِعْلُ فِي تَأْوِيلِ مَصْدَرٍ فَاعِلُ عَسَى.", "«go out» — the clause the doer of ʿasā.", "«çıkmak» — cümle asâ'nın fâili."),
  zayd("زَيْدٌ", "فَاعِلُ يَخْرُجَ مَرْفُوعٌ.", "«Zayd» — the doer of «go out».", "«Zeyd» — yahruce'nin fâili.", punct=".", tags=[FL]),
 ]})
# ----------- s3 — كَادَ
S.append({"id": "s3", "translation": {"en": "And كَادَ: its khabar is mostly a muḍāriʿ without أَنْ — as in «Zayd nearly went out» — and it is sometimes with أَنْ.", "tr": "Ve kâde: haberi çoğunlukla en'siz muzâridir — «Zeyd neredeyse çıkıyordu» gibi — bazen en ile olur."},
 "tokens": [
  qv("كَادَ", "kada", "«and kāda — to be about to, nearly»", "«ve kâde — neredeyse, az kalsın»", punct="،", tags=[HV]),
  khabaruhu(),
  tok("غَالِبًا", "ghalib", "noun", [K, HL], "حَالٌ مَنْصُوبٌ — فِي الْغَالِبِ.", "«mostly» — a ḥāl.", "«çoğunlukla» — hâl."),
  tok("مُضَارِعٌ", "mudari", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«a muḍāriʿ» — the khabar.", "«muzâri» — haber."),
  bila(),
  an_quoted(role_ar="لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ: أَنْ", punct="،"),
  nahw(),
  tok("كَادَ", "kada", "verb", [K, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ.", "«nearly» — the verb of approach.", "«neredeyse» — mukârebe fiili."),
  zayd("زَيْدٌ", "اسْمُ كَادَ مَرْفُوعٌ.", "«Zayd» — the ism of kāda.", "«Zeyd» — kâde'nin ismi.", tags=[KN]),
  tok("يَخْرُجُ", "kharaja", "verb", [K, KN], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ كَادَ فِي مَحَلِّ نَصْبٍ.", "«went out» — the clause the khabar of kāda.", "«çıkıyordu» — cümle kâde'nin haberi.", punct="،"),
  waqad(),
  yakunu(),
  tok("مَعَ", "maa", "noun", [K, MF, ID, KN], "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِخَبَرِ يَكُونُ الْمَحْذُوفِ، مُضَافٌ.", "«with» — hanging on the dropped khabar.", "«ile» — hazfedilmiş habere müteallik."),
  an_quoted(role_ar="لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ: أَنْ", punct="."),
 ]})
# ----------- s4 — كَرَبَ
S.append({"id": "s4", "translation": {"en": "And كَرَبَ — it is like كَادَ in both its ways.", "tr": "Ve kerebe — iki vechinde de kâde gibidir."},
 "tokens": [
  qv("كَرَبَ", "karaba-approach", "«and karaba — to be on the point of»", "«ve kerebe — … üzere olmak»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("مِثْلُ", "mithl", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«like» — the khabar, annexed.", "«gibi» — haber, muzâf."),
  tok("كَادَ", "kada", "verb", [K, KN, HT, ID, HV], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«kāda» — mentioned as a word, annexed to.", "«kâde» — lafzı kastedilmiş, muzâfun ileyh."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("وَجْهَيْهِ", "wajh", "noun", [K, HJ, MTH, ID], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its two ways» — the dual annexed: with an and without.", "«iki vechinde» — muzâf tesniye: en'li ve en'siz.", punct=".", segments=[seg("وَجْهَيْ", "wajh", "noun"), pr3msi()]),
 ]})
# ----------- s5 — the eight whose khabar is a muḍāriʿ without أَنْ
S.append({"id": "s5", "translation": {"en": "And هَلْهَلَ, طَفِقَ, أَخَذَ, أَنْشَأَ, أَقْبَلَ, هَبَّ, جَعَلَ and عَلِقَ — their khabars are the muḍāriʿ verb without أَنْ.", "tr": "Ve helhele, tafika, ehaze, enşee, akbele, hebbe, ceale ve alika — haberleri en'siz muzâri fiildir."},
 "tokens": [
  qv("هَلْهَلَ", "halhala", "«and halhala — to be about to, to set about»", "«ve helhele — … üzere olmak»", tags=["rubai-babs"]),
  qv("طَفِقَ", "tafiqa", "«and ṭafiqa — to begin to»", "«ve tafika — başlamak»"),
  qv("أَخَذَ", "akhadha", "«and akhadha — to begin to (lit. to take)»", "«ve ehaze — başlamak (asıl: almak)»"),
  qv("أَنْشَأَ", "anshaa", "«and anshaʾa — to begin to»", "«ve enşee — başlamak»", tags=[F4]),
  qv("أَقْبَلَ", "aqbala", "«and aqbala — to set about»", "«ve akbele — koyulmak»", tags=[F4]),
  qv("هَبَّ", "habba-blow", "«and habba — to set about (lit. to blow, to rise)»", "«ve hebbe — kalkışmak (asıl: esmek)»", tags=[DV]),
  qv("جَعَلَ", "jaala", "«and jaʿala — to begin to»", "«ve ceale — başlamak»"),
  qv("عَلِقَ", "aliqa", "«and ʿaliqa — to begin to (lit. to cling)»", "«ve alika — başlamak (asıl: tutunmak)»", punct="،"),
  tok("وَأَخْبَارُهَا", "khabar-predicate", "noun", [K, AT, MK, ID, "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَأَخْبَارُهَا مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their khabars» — a mubtada.", "«ve haberleri» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("أَخْبَارُ", "khabar-predicate", "noun"), pr3fs()]),
  tok("الْفِعْلُ", "fil", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the verb» — the khabar.", "«fiil» — haber."),
  mudari_naat(),
  bila(),
  an_quoted(role_ar="لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ: أَنْ", punct="."),
 ]})
# ----------- s6 — أَوْشَكَ
S.append({"id": "s6", "translation": {"en": "And أَوْشَكَ — it is used the way عَسَى and كَادَ are used.", "tr": "Ve evşeke — asâ ve kâde'nin kullanıldığı gibi kullanılır."},
 "tokens": [
  qv("أَوْشَكَ", "awshaka", "«and awshaka — to be on the verge of»", "«ve evşeke — … üzere olmak»", punct="،", tags=[F4, "mithal-verbs"]),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("يُسْتَعْمَلُ", "istamala", "verb", [K, NF, MK, F10], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«is used» — the clause the khabar.", "«kullanılır» — cümle haber."),
  tok("اسْتِعْمَالَ", "istimal", "noun", [K, MM, ID, MSD], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِبَيَانِ النَّوْعِ، مُضَافٌ.", "«the way … is used» — the absolute object of kind, annexed.", "«… kullanılışı gibi» — nev' bildiren mef'ûl-i mutlak, muzâf."),
  tok("عَسَى", "asa-hope", "verb", [K, KN, HT, ID, NQ], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«ʿasā» — mentioned as a word, annexed to.", "«asâ» — lafzı kastedilmiş, muzâfun ileyh."),
  qv("كَادَ", "kada", "«and kāda»", "«ve kâde»", punct=".", tags=[HV]),
 ]})
# ----------- s7 — no fronting of their khabars
S.append({"id": "s7", "translation": {"en": "And it is not permitted to put the khabars of the verbs of approach before the verbs themselves.", "tr": "Mukârebe fiillerinin haberlerini fiillerin kendilerinden öne almak câiz değildir."},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, AT, LN], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … değildir»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ تَقْدِيمُ.", "«is permitted» — its doer «the fronting».", "«câiz olmaz» — fâili takdim."),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the fronting of» — the doer, annexed.", "«öne alınması» — fâil, muzâf."),
  tok("أَخْبَارِ", "khabar-predicate", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the khabars of»", "«haberlerinin»"),
  tok("أَفْعَالِ", "fil", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the verbs of»", "«fiillerinin»"),
  tok("الْمُقَارَبَةِ", "muqaraba", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«approach»", "«mukârebe»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«-den önce»"),
  tok("أَنْفُسِهَا", "nafs", "noun", [K, HJ, ID, "jam-taksir"], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — عَلَى الْأَفْعَالِ أَنْفُسِهَا.", "«themselves» — the verbs themselves.", "«kendilerinden» — fiillerin kendilerinden.", punct=".", segments=[seg("أَنْفُسِ", "nafs", "noun"), pr3fs()]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)

CAND = {
 "qism": G("qism", "قِسْم", "ق س م", "noun", "division, part", "kısım", 2, plural="أَقْسَام"),
 "thani": G("thani", "ثَانِي", "ث ن ي", "noun", "second", "ikinci", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "that which, what (relative)", "… olan şey (ism-i mevsûl)", 2),
 "dalla": G("dalla", "دَلَّ", "د ل ل", "verb", "to indicate, to point to", "delâlet etmek, göstermek", 3),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, -e", 1),
 "mana": G("mana", "مَعْنًى", "ع ن ي", "noun", "meaning, sense", "mânâ", 2, plural="مَعَانٍ"),
 "qurb": G("qurb", "قُرْب", "ق ر ب", "noun", "nearness", "yakınlık", 2),
 "samma": G("samma", "سَمَّى", "س م و", "verb", "to name, to call", "adlandırmak", 2, form="II"),
 "fil": G("fil", "فِعْل", "ف ع ل", "noun", "verb; act", "fiil", 1, plural="أَفْعَال"),
 "muqaraba": G("muqaraba", "مُقَارَبَة", "ق ر ب", "noun", "approach, nearness (masdar of qāraba) — the verbs of approach", "mukârebe, yaklaşma (kârabe'nin mastarı) — mukârebe fiilleri", 4),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (negation)", "değil, -mez (nefiy)", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak, idi", 1),
 "khabar-predicate": G("khabar-predicate", "الْخَبَر", "خ ب ر", "noun", "the khabar — the predicate of a nominal sentence", "haber — isim cümlesinin yüklemi", 2, plural="أَخْبَار"),
 "illa": G("illa", "إِلَّا", None, "part", "except", "-den başka, hariç", 1),
 "mudari": G("mudari", "الْمُضَارِع", "ض ر ع", "noun", "the muḍāriʿ (imperfect verb)", "muzâri (fiil-i muzâri)", 2),
 "nahw": G("nahw", "نَحْو", "ن ح و", "noun", "like, such as; grammar", "gibi; nahiv", 2),
 "asa-hope": G("asa-hope", "عَسَى", "ع س ي", "verb", "may well, it is hoped (a verb of hope — jāmid)", "umulur ki, belki (recâ fiili — câmid)", 3),
 "maa": G("maa", "مَعَ", None, "noun", "with (a ẓarf)", "ile, birlikte (zarf)", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "to, that (the masdar particle that puts the muḍāriʿ in naṣb)", "-mesi, -mek (muzâriyi nasb eden mastar harfi)", 2),
 "ghalib": G("ghalib", "غَالِب", "غ ل ب", "noun", "prevailing, usual; غَالِبًا mostly", "galip, çoğunlukla olan; gâliben çoğunlukla", 3),
 "zayd": G("zayd", "زَيْد", None, "propn", "Zayd (the grammarians' stock name)", "Zeyd (nahivcilerin örnek adı)", 1),
 "kharaja": G("kharaja", "خَرَجَ", "خ ر ج", "verb", "to go out", "çıkmak", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed; sometimes (with the muḍāriʿ)", "muhakkak; bazen (muzâri ile)", 2),
 "hadhafa": G("hadhafa", "حَذَفَ", "ح ذ ف", "verb", "to drop, to omit", "hazfetmek, düşürmek", 3),
 "tamm": G("tamm", "تَامّ", "ت م م", "noun", "complete, tāmm", "tam", 2),
 "bi": G("bi", "بِ", None, "prep", "with, by, in", "ile, -de", 1),
 "kada": G("kada", "كَادَ", "ك و د", "verb", "to be about to, nearly (a verb of approach)", "neredeyse, az kalsın (mukârebe fiili)", 3),
 "karaba-approach": G("karaba-approach", "كَرَبَ", "ك ر ب", "verb", "to be on the point of (a verb of approach, like kāda)", "… üzere olmak (mukârebe fiili, kâde gibi)", 4),
 "huwa": G("huwa", "هُوَ", None, "pron", "he, it", "o", 1),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "like, the like of", "gibi, misli", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "wajh": G("wajh", "وَجْه", "و ج ه", "noun", "face; way, manner", "yüz; vecih, tarz", 2, plural="وُجُوه"),
 "halhala": G("halhala", "هَلْهَلَ", "ه ل ه ل", "verb", "to be about to, to set about (a verb of approach; quadriliteral)", "… üzere olmak, koyulmak (mukârebe fiili; rubâî)", 5),
 "tafiqa": G("tafiqa", "طَفِقَ", "ط ف ق", "verb", "to begin to (a verb of beginning)", "başlamak (şürû fiili)", 4),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take; to begin to", "almak; başlamak", 1),
 "anshaa": G("anshaa", "أَنْشَأَ", "ن ش أ", "verb", "to begin to; to create, to compose", "başlamak; inşâ etmek", 3, form="IV"),
 "aqbala": G("aqbala", "أَقْبَلَ", "ق ب ل", "verb", "to come forward; to set about", "yönelmek; koyulmak", 2, form="IV"),
 "habba-blow": G("habba-blow", "هَبَّ", "ه ب ب", "verb", "to blow (wind); to rise, to set about", "esmek; kalkmak, kalkışmak", 3),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make; to begin to", "yapmak, kılmak; başlamak", 1),
 "aliqa": G("aliqa", "عَلِقَ", "ع ل ق", "verb", "to cling to; to begin to (a verb of beginning)", "tutunmak, takılmak; başlamak (şürû fiili)", 4),
 "awshaka": G("awshaka", "أَوْشَكَ", "و ش ك", "verb", "to be on the verge of (a verb of approach, used like ʿasā and kāda)", "… üzere olmak (mukârebe fiili, asâ ve kâde gibi)", 4, form="IV"),
 "istamala": G("istamala", "اِسْتَعْمَلَ", "ع م ل", "verb", "to use", "kullanmak", 2, form="X"),
 "istimal": G("istimal", "اِسْتِعْمَال", "ع م ل", "noun", "use, usage (masdar)", "kullanım, isti'mâl (mastar)", 3),
 "jaaza": G("jaaza", "جَازَ", "ج و ز", "verb", "to be permitted", "câiz olmak", 2),
 "taqdim": G("taqdim", "تَقْدِيم", "ق د م", "noun", "fronting, putting first (masdar)", "takdim, öne alma (mastar)", 3),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "self, soul", "nefis, kendi", 1, plural="أَنْفُس"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
W4 = _sg.W4
put_morph(mo, "karaba-approach", _sg.sound1("nasara", "كَرَب", "كْرُب", "اُكْرُب", "كَرْب", "كَارِب", None, None, None, "كَرَبَ يَكْرُبُ كَرْبًا: قَارَبَ — مِنْ أَفْعَالِ الْمُقَارَبَةِ، مِثْلُ كَادَ."))
put_morph(mo, "tafiqa", _sg.sound1("samia", "طَفِق", "طْفَق", "اِطْفَق", "طَفَق", "طَافِق", None, None, None, "طَفِقَ يَطْفَقُ: شَرَعَ، أَخَذَ فِي — مِنْ أَفْعَالِ الشُّرُوعِ."))
put_morph(mo, "aliqa", _sg.sound1("samia", "عَلِق", "عْلَق", "اِعْلَق", "عَلَق", "عَالِق", None, None, None, "عَلِقَ يَعْلَقُ عَلَقًا: نَشِبَ وَتَعَلَّقَ؛ وَبِمَعْنَى شَرَعَ — مِنْ أَفْعَالِ الشُّرُوعِ."))
put_morph(mo, "anshaa", _sg.derived(_sg.B4 + " — مَهْمُوزُ اللَّامِ", W4, "ُ", "أَنْشَأ", "نْشِئ", "أَنْشِئ", "إِنْشَاء", "مُنْشِئ", "مُنْشَأ", "أُنْشِئَ", "يُنْشَأُ", "أَنْشَأَ يُنْشِئُ إِنْشَاءً: أَحْدَثَ؛ وَبِمَعْنَى شَرَعَ — مِنْ أَفْعَالِ الشُّرُوعِ."))
put_morph(mo, "awshaka", _sg.derived(_sg.B4 + " — مِثَالٌ وَاوِيٌّ", W4, "ُ", "أَوْشَك", "وشِك", "أَوْشِك", "إِيشَاك", "مُوشِك", None, None, None, "أَوْشَكَ يُوشِكُ إِيشَاكًا: قَارَبَ — مِنْ أَفْعَالِ الْمُقَارَبَةِ، يُسْتَعْمَلُ اسْتِعْمَالَ عَسَى وَكَادَ؛ الْوَاوُ بَعْدَ الضَّمَّةِ مَدٌّ لَا سُكُونَ عَلَيْهَا."))
put_morph(mo, "halhala", _sg.entry("فَعْلَلَ يُفَعْلِلُ — رُبَاعِيٌّ مُجَرَّدٌ", "فَعْلَلَ يُفَعْلِلُ", "هَلْهَلَة", "مُهَلْهِل", _sg.mazi14("هَلْهَل"), _sg.mudari14("ُ", "هَلْهِل"), _sg.amr_attach("هَلْهِل"), "يُهَلْهِلَ", "يُهَلْهِلْ", "تُهَلْهِلْ", "مُهَلْهَل", "هُلْهِلَ", "يُهَلْهَلُ", "هَلْهَلَ يُهَلْهِلُ هَلْهَلَةً: قَارَبَ، كَادَ — رُبَاعِيٌّ مِنْ بَابِ دَحْرَجَ؛ مِنْ أَفْعَالِ الْمُقَارَبَةِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch11 gloss+morph ok", len(GLOSS_ADD), "verbs:", [k for k in ("karaba-approach", "tafiqa", "aliqa", "anshaa", "awshaka", "halhala", "kada", "asa-hope", "akhadha", "aqbala", "habba-blow", "jaala", "istamala", "samma", "dalla", "kharaja", "hadhafa", "jaaza") if k in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "أَفْعَالُ الْمُقَارَبَةِ — عَسَى وَكَادَ وَأَخَوَاتُهُمَا", "en": "The verbs of approach — ʿasā, kāda and their sisters", "tr": "Mukârebe fiilleri — asâ, kâde ve kardeşleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — أفعال المقاربة", "الكافية لابن الحاجب — أفعال المقاربة", "قطر الندى لابن هشام — كاد وأخواتها"],
 "amil": "أَفْعَالُ الْمُقَارَبَةِ — the second division of the nāqiṣ verb: they raise their ism, and their khabar is never anything but a muḍāriʿ verb (with أَنْ or without it, as each verb has it)",
 "question": {
  "en": ["What is the second division of the nāqiṣ verb? The verbs that carry the sense of NEARNESS — called the verbs of approach (أَفْعَالُ الْمُقَارَبَةِ).",
         "What may their khabar be? Only a muḍāriʿ verb — never a noun, never a māḍī.",
         "How does عَسَى take its khabar? Mostly WITH أَنْ: عَسَى زَيْدٌ أَنْ يَخْرُجَ (Zayd may well go out); sometimes أَنْ is dropped; and عَسَى may be tāmm with أَنْ and the muḍāriʿ as its doer: عَسَى أَنْ يَخْرُجَ زَيْدٌ.",
         "How does كَادَ take its khabar? Mostly WITHOUT أَنْ: كَادَ زَيْدٌ يَخْرُجُ (Zayd nearly went out); sometimes with it. كَرَبَ is like كَادَ in both ways.",
         "Which verbs take a muḍāriʿ with no أَنْ at all? هَلْهَلَ، طَفِقَ، أَخَذَ، أَنْشَأَ، أَقْبَلَ، هَبَّ، جَعَلَ، عَلِقَ — the verbs of beginning: طَفِقَ زَيْدٌ يَكْتُبُ.",
         "And أَوْشَكَ? It is used the way عَسَى and كَادَ are used — with أَنْ or without.",
         "May their khabar stand before them? No — unlike كَانَ's sisters, the khabars of the verbs of approach are never fronted.",
         "Why is their khabar always a verb? Because approach is about an ACT that is near — a muḍāriʿ names the act about to happen; a noun would name a state, which is كَانَ's business.",
         "What does the engine READ here? The DabtEngine raises the noun after عَسَى / كَادَ as the ism, puts the muḍāriʿ after أَنْ in naṣb and keeps it in rafʿ without أَنْ, reads a verb mentioned as a word as written, and reads عَسَى أَنْ يَخْرُجَ زَيْدٌ as the tāmm with the clause as its doer."],
  "tr": ["Nâkıs fiilin ikinci kısmı nedir? YAKINLIK mânâsı taşıyan fiiller — mukârebe fiilleri (أَفْعَالُ الْمُقَارَبَةِ) denir.",
         "Haberleri ne olabilir? Yalnız muzâri fiil — ne isim ne mâzî.",
         "Asâ haberini nasıl alır? Çoğunlukla en İLE: asâ Zeydün en yahruce (Zeyd'in çıkması umulur); bazen en hazfedilir; asâ, en ve muzâri fâili olmak üzere tâm da olabilir: asâ en yahruce Zeydün.",
         "Kâde haberini nasıl alır? Çoğunlukla en'SİZ: kâde Zeydün yahrucu (Zeyd neredeyse çıkıyordu); bazen en ile. Kerebe iki vechinde de kâde gibidir.",
         "Hangi fiiller hiç en almadan muzâri alır? Helhele, tafika, ehaze, enşee, akbele, hebbe, ceale, alika — şürû fiilleri: tafika Zeydün yektübü.",
         "Ya evşeke? Asâ ve kâde'nin kullanıldığı gibi kullanılır — en ile veya en'siz.",
         "Haberleri onlardan önce gelebilir mi? Hayır — kâne'nin kardeşlerinden farklı olarak mukârebe fiillerinin haberleri asla öne alınmaz.",
         "Haberleri neden daima fiildir? Çünkü yaklaşma, yakın olan bir FİİL hakkındadır — muzâri olmak üzere olan işi adlandırır; isim bir hâli adlandırırdı, o da kâne'nin işidir.",
         "Motor burada neyi OKUR? DabtEngine asâ / kâde'den sonraki ismi isim olarak ref eder, en'den sonraki muzâriyi nasb eder ve en'siz olanı merfû bırakır, lafzı kastedilen fiili olduğu gibi okur ve asâ en yahruce Zeydün'ü cümlesi fâil olan tâm fiil olarak okur."],
 },
 "plain": {"en": "Some sisters of «to be» say that an act is close: «Zayd may well go out», «Zayd nearly went out», «Zayd began to write». Their second word is always a verb in the present shape — with «to» (an) after ʿasā, without it after kāda and the verbs of beginning — and it never moves in front of them.",
           "tr": "«Olmak»ın bazı kardeşleri bir işin yakın olduğunu söyler: «Zeyd'in çıkması umulur», «Zeyd neredeyse çıkıyordu», «Zeyd yazmaya başladı». İkinci kelimeleri daima muzâri şeklinde bir fiildir — asâ'dan sonra «en» ile, kâde ve şürû fiillerinden sonra en'siz — ve asla onların önüne geçmez."},
 "explanation": {"en": "The second division of the nāqiṣ verb is what indicates the sense of nearness, and it is called the verbs of approach; their khabars are never anything but a muḍāriʿ verb. Such is عَسَى, whose khabar is the muḍāriʿ mostly with أَنْ — عَسَى زَيْدٌ أَنْ يَخْرُجَ — and أَنْ is sometimes dropped; and it may be tāmm, with أَنْ and the muḍāriʿ as its doer: عَسَى أَنْ يَخْرُجَ زَيْدٌ. And كَادَ, whose khabar is mostly a muḍāriʿ without أَنْ — كَادَ زَيْدٌ يَخْرُجُ — and sometimes with it. And كَرَبَ, which is like كَادَ in both ways. And هَلْهَلَ، طَفِقَ، أَخَذَ، أَنْشَأَ، أَقْبَلَ، هَبَّ، جَعَلَ، عَلِقَ, whose khabars are the muḍāriʿ without أَنْ. And أَوْشَكَ, which is used as عَسَى and كَادَ are used. It is not permitted to put the khabars of the verbs of approach before the verbs themselves.",
                 "tr": "Nâkıs fiilin ikinci kısmı yakınlık mânâsına delâlet edendir ve mukârebe fiilleri diye adlandırılır; haberleri muzâri fiilden başka bir şey olmaz. Asâ böyledir: haberi çoğunlukla en'li muzâridir — asâ Zeydün en yahruce — ve en bazen hazfedilir; en ve muzâri fâili olmak üzere tâm da olabilir: asâ en yahruce Zeydün. Kâde: haberi çoğunlukla en'siz muzâridir — kâde Zeydün yahrucu — bazen en ile. Kerebe: iki vechinde de kâde gibidir. Helhele, tafika, ehaze, enşee, akbele, hebbe, ceale, alika: haberleri en'siz muzâridir. Evşeke: asâ ve kâde gibi kullanılır. Mukârebe fiillerinin haberlerini fiillerin kendilerinden öne almak câiz değildir."},
 "examples": [
  {"ar": "وَلَا يَكُونُ أَخْبَارُهَا إِلَّا فِعْلًا مُضَارِعًا", "en": "the rule of the khabar: only a muḍāriʿ", "tr": "haberin kuralı: yalnız muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "عَسَى زَيْدٌ أَنْ يَخْرُجَ", "en": "ʿasā with its ism and its khabar with an — naṣb on the muḍāriʿ", "tr": "asâ ismi ve en'li haberiyle — muzâride nasb", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "عَسَى أَنْ يَخْرُجَ زَيْدٌ", "en": "ʿasā tāmm: the an-clause its doer, Zayd the doer of the inner verb", "tr": "asâ tâm: en'li cümle fâili, Zeyd iç fiilin fâili", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "كَادَ زَيْدٌ يَخْرُجُ", "en": "kāda with its khabar in rafʿ, no an", "tr": "kâde, haberi merfû, en'siz", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَهُوَ مِثْلُ كَادَ فِي وَجْهَيْهِ", "en": "karaba: like kāda in both ways", "tr": "kerebe: iki vechinde de kâde gibi", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَهَلْهَلَ وَطَفِقَ وَأَخَذَ وَأَنْشَأَ وَأَقْبَلَ وَهَبَّ وَجَعَلَ وَعَلِقَ", "en": "the verbs of beginning — a muḍāriʿ with no an", "tr": "şürû fiilleri — en'siz muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "وَلَا يَجُوزُ تَقْدِيمُ أَخْبَارِ أَفْعَالِ الْمُقَارَبَةِ عَلَى أَنْفُسِهَا", "en": "no fronting of their khabars", "tr": "haberleri öne alınmaz", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "عَسَى زَيْدٌ خَارِجًا", "right": "عَسَى زَيْدٌ أَنْ يَخْرُجَ", "why": {"en": "the khabar of a verb of approach is never a noun — only a muḍāriʿ verb", "tr": "mukârebe fiilinin haberi asla isim olmaz — yalnız muzâri fiil"}},
  {"wrong": "عَسَى زَيْدٌ أَنْ يَخْرُجُ", "right": "عَسَى زَيْدٌ أَنْ يَخْرُجَ", "why": {"en": "أَنْ puts the muḍāriʿ in naṣb — the fatḥa is its sign", "tr": "en muzâriyi nasb eder — fetha alâmetidir"}},
  {"wrong": "كَادَ زَيْدٌ يَخْرُجَ", "right": "كَادَ زَيْدٌ يَخْرُجُ", "why": {"en": "without أَنْ the muḍāriʿ keeps its rafʿ — nothing governs it in naṣb", "tr": "en olmayınca muzâri merfû kalır — onu nasb eden yoktur"}},
  {"wrong": "يَخْرُجُ كَادَ زَيْدٌ", "right": "كَادَ زَيْدٌ يَخْرُجُ", "why": {"en": "the khabar of a verb of approach is never put before it", "tr": "mukârebe fiilinin haberi onun önüne alınmaz"}},
 ],
}
ADD_EN = (" Chapter 11 (print pp. 106-107): the second division of the nāqiṣ verb — the verbs of approach, their khabar only a muḍāriʿ (s1); عَسَى with أَنْ, "
          "with أَنْ dropped, and tāmm (s2); كَادَ without أَنْ and with it (s3); كَرَبَ like كَادَ (s4); the eight verbs of beginning with a bare muḍāriʿ (s5); أَوْشَكَ "
          "used like عَسَى and كَادَ (s6); no fronting of their khabars (s7). The print's هلهل is kept as the lithograph writes it (the received texts have هَلْهَلَ).")
ADD_TR = (" On birinci bab (baskı s. 106-107): nâkıs fiilin ikinci kısmı — mukârebe fiilleri, haberleri yalnız muzâri (s1); en'li, en'i hazfedilmiş ve tâm asâ (s2); "
          "en'siz ve en'li kâde (s3); kâde gibi olan kerebe (s4); yalın muzâri alan sekiz şürû fiili (s5); asâ ve kâde gibi kullanılan evşeke (s6); haberlerinin "
          "öne alınmaması (s7). Baskının هلهل'i litografın yazdığı gibi tutuldu (rivâyet edilen metinlerde هَلْهَلَ).")
write_out(11, S, TITLE, ADD_EN, ADD_TR, "pp. 106-107", GLOSS_ADD, notes=(NOTE,),
          related=((KN, [K]), (K10, [K]), (AM, [K]), (NSB, [K]), ("taqdim-al-musnad", [K])))
report(11, S, GLOSS_ADD, (NOTE,))
