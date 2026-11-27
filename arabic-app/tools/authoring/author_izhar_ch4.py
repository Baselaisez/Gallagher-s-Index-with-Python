# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 4: the governor in TWO nouns, first division — the eight letters whose mansub precedes
# their marfu; the six called "letters resembling the verb" (three letters or more, a fatha at the end, a verb's meaning):
# إِنَّ / أَنَّ (taḥqīq), كَأَنَّ (tashbīh), لٰكِنَّ (istidrāk), لَيْتَ (tamannī), لَعَلَّ (tarajjī). Their place is the front of
# speech save أَنَّ; مَا nullifies them (إِنَّمَا ضَرَبَ زَيْدٌ). إِنَّ leaves the clause a clause, أَنَّ turns it into a masdar —
# hence KASR where a clause stands and FATH where a mufrad stands. The ten kasr places with their examples (28:76, 8:5).
# Print pp. 94–96.
#   python3 author_izhar_ch4.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "mawadi-kasr-inna"
K1 = "al-amil-wa-aqsamuh"
IW = "inna-wa-akhawatuha"; IA = "inna-am-anna"; IK = "innama-kaffa"
TITLE = {"ar": "الْعَامِلُ فِي اسْمَيْنِ: الْحُرُوفُ الْمُشَبَّهَةُ بِالْفِعْلِ وَمَوَاضِعُ كَسْرِ إِنَّ", "en": "The governor in two nouns — the letters resembling the verb, and where إِنَّ takes the kasra", "tr": "İki isimde âmil — fiile benzeyen harfler ve inne'nin kesre yerleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; IS = "istithna"; IQ = "al-iqtibas-wal-tadmin"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def cite_quran(punct=":"):
    return [tok("نَحْوَ", "nahwa", "noun", [K, MF, HT, ID, IQ], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفٌ بِمَعْنَى مِثْلَ، مُضَافٌ.", "«as in» — the citation ẓarf, annexed.", "«meselâ» — iktibas zarfı, muzâf."),
            tok("قَوْلِهِ", "qawl", "noun", [K, ID, IQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
            tok("تَعَالَى", "taala", "verb", [K, IQ, "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«Exalted is He»", "«yüce»", punct=punct)]
def fi(punct=None, tags=()): return tok("فِي", "fi", "prep", [K, HJ] + list(tags), "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def wafi(tags=()): return tok("وَفِي", "fi", "prep", [K, AT, HJ] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى فِي الِابْتِدَاءِ.", "«and in»", "«ve -de»", segments=wa("فِي", "fi", "prep"))
def wabada(): return tok("وَبَعْدَ", "bada", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْدَ ظَرْفٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى فِي الِابْتِدَاءِ، مُضَافٌ.", "«and after» — the ẓarf, annexed.", "«ve sonra» — zarf, muzâf.", segments=wa("بَعْدَ", "bada", "noun"))
def q_mub(full, lex, en, tr, punct=None, joined=True, extra=()):
    """a particle quoted as a word, the mubtada (in the place of raf') — إِنَّ لِلتَّحْقِيقِ"""
    segs = wa(full[2:], lex, "part") if joined else None
    ar = ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ."
    return tok(full, lex, "part", [K, IW, MK, HT] + list(extra), ar, en + " — quoted as a word; the mubtada.", tr + " — hikâye edilmiş; mübtedâ.", punct=punct, segments=segs)
def lil(full, lex, en, tr, punct, extra=()):
    """لِلتَّحْقِيقِ — the lam phrase that is the khabar"""
    return tok(full, lex, "noun", [K, HJ, MK] + list(extra), "اللَّامُ حَرْفُ جَرٍّ، وَالِاسْمُ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", en + " — the jarr phrase is the khabar.", tr + " — câr-mecrûr haber.", punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "noun")])
def inna(full="إِنَّ", pre_ar="", pre_en="", pre_tr="", extra=(), segs=None, punct=None):
    return tok(full, "inna", "part", [K, IW, IA] + list(extra), pre_ar + "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، مَكْسُورَةُ الْهَمْزَةِ.", pre_en + "«indeed» — inna with its kasra.", pre_tr + "«şüphesiz» — hemzesi kesreli inne.", segments=segs, punct=punct)
def zaydan(): return tok("زَيْدًا", "zayd", "propn", [K, IW], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the ism of inna.", "«Zeyd» — inne'nin ismi.")
def qaim(punct, full="قَائِمٌ", pre_ar="", segs=None, extra=()):
    return tok(full, "qaim", "noun", [K, IW, "ism-fail"] + list(extra), pre_ar + "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«standing» — the khabar of inna.", "«ayaktadır» — inne'nin haberi.", punct=punct, segments=segs)
def inna_zayd_qaim(punct="،"): return [inna(), zaydan(), qaim(punct)]
def harf_x(x_full, x_lex, x_en, x_tr, punct=None, extra=()):
    return [tok("حُرُوفِ", "harf", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — جَمْعُ حَرْفٍ.", "«the letters of»", "«harflerinden»"),
            tok(x_full, x_lex, "noun", [K, ID] + list(extra), "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", x_en, x_tr, punct=punct)]

# ----------- s1 — the governor in two nouns: two divisions
S.append({"id": "s1", "translation": {"en": "And the governor in two nouns is, again, of two divisions: a division whose manṣūb comes before its marfūʿ, and a division the other way round.", "tr": "İki isimde âmil de iki kısımdır: mansûbu merfûundan önce gelen bir kısım ve bunun aksi olan bir kısım."},
 "tokens": [
  tok("وَالْعَامِلُ", "amil-governor", "noun", [K, K1, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَامِلُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and the governor» — the mubtada.", "«âmil» — mübtedâ.", segments=wa("الْعَامِلُ", "amil-governor", "noun")),
  fi(),
  tok("اسْمَيْنِ", "ism", "noun", [K, HJ, "al-muthanna"], "مَجْرُورٌ بِفِي، وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى — مُتَعَلِّقٌ بِالْعَامِلِ.", "«two nouns» — majrūr by the yāʾ.", "«iki isimde» — yâ ile mecrûr."),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the phrase is the khabar.", "«üzere» — câr-mecrûr haber."),
  tok("قِسْمَيْنِ", "qism", "noun", [K, HJ, "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two divisions»", "«iki kısım»"),
  tok("أَيْضًا", "aydan", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ — مَنْصُوبٌ بِالْفَتْحَةِ.", "«again» — the absolute object of an omitted آضَ.", "«de» — mahzûf fiilin mef'ûl-i mutlakı.", punct=":"),
  tok("قِسْمٌ", "qism", "noun", [K, MK, HT, "badal"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا قِسْمٌ — مَرْفُوعٌ بِالضَّمَّةِ.", "«a division» — the khabar of a dropped «one of them».", "«bir kısım» — mahzûf mübtedânın haberi."),
  tok("مَنْصُوبٌ", "mansub", "noun", [K, MK, NA, "jumla-sifa"], "مُبْتَدَأٌ مَرْفُوعٌ، أَيْ: مَنْصُوبُهُ — وَالظَّرْفُ بَعْدَهُ خَبَرُهُ، وَالْجُمْلَةُ نَعْتٌ لِقِسْمٌ.", "«its manṣūb» — the mubtada of a qualifying clause; the ẓarf is its khabar.", "«mansûbu» — sıfat cümlesinin mübtedâsı; zarf haberi."),
  tok("قَبْلَ", "qabla", "noun", [K, MF, ID, MK], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — خَبَرٌ.", "«before» — the ẓarf, annexed; the khabar.", "«önce» — zarf, muzâf; haber."),
  tok("مَرْفُوعِهِ", "marfu", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its marfūʿ»", "«merfûundan»", punct="،", segments=[seg("مَرْفُوعِ", "marfu", "noun"), pr3msi()]),
  tok("وَقِسْمٌ", "qism", "noun", [K, AT, MK, HT], "الْوَاوُ عَاطِفَةٌ، وَقِسْمٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَالْآخَرُ قِسْمٌ.", "«and a division»", "«ve bir kısım»", segments=wa("قِسْمٌ", "qism", "noun")),
  tok("عَلَى", "ala", "prep", [K, HJ, NA], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِقِسْمٌ.", "«on» — the phrase qualifies «division».", "«üzere» — câr-mecrûr sıfat."),
  tok("الْعَكْسِ", "aks", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«the reverse»", "«aksi»", punct="."),
 ]})
# ----------- s2 — the first division: eight letters, six resembling the verb
S.append({"id": "s2", "translation": {"en": "The first division is eight letters; six of them are called letters resembling the verb, because they are of three letters or more, their ends carry a fatḥa, and a verb's meaning is found in each of them:", "tr": "Birinci kısım sekiz harftir; bunların altısı fiile benzeyen harfler diye adlandırılır — üç ve daha fazla harfli olmaları, sonlarının fethalı olması ve her birinde bir fiil mânâsı bulunması sebebiyle:"},
 "tokens": [
  tok("الْقِسْمُ", "qism", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the division» — the mubtada.", "«kısım» — mübtedâ."),
  tok("الْأَوَّلُ", "awwal", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«first» — the naʿt.", "«birinci» — sıfat."),
  tok("ثَمَانِيَةُ", "thamaniya", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«eight» — the khabar, annexed.", "«sekiz» — haber, muzâf."),
  tok("أَحْرُفٍ", "harf", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِلَّةٍ.", "«letters» — a plural of paucity.", "«harf» — cem'-i kıllet.", punct="،"),
  tok("سِتَّةٌ", "sitta", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«six» — the mubtada.", "«altısı» — mübtedâ."),
  tok("مِنْهَا", "min", "prep", [K, HJ, NA], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — نَعْتٌ لِسِتَّةٌ.", "«of them» — qualifying «six».", "«onlardan» — sıfat.", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  tok("تُسَمَّى", "samma", "verb", [K, MK, "naib-al-fail", "mafulayn"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«are called» — passive; the clause is the khabar.", "«adlandırılır» — meçhul; cümle haber."),
  tok("حُرُوفًا", "harf", "noun", [K, "mafulayn", "jam-taksir"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«letters» — the second object.", "«harfler» — ikinci mef'ûl."),
  tok("مُشَبَّهَةً", "mushabbah", "noun", [K, NA, "ism-maful"], "نَعْتٌ مَنْصُوبٌ — اسْمُ مَفْعُولٍ.", "«resembling» — the naʿt, an ism mafʿūl.", "«benzeyen» — sıfat, ism-i mef'ûl."),
  tok("بِالْفِعْلِ", "fil", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفِعْلِ مَجْرُورٌ — مُتَعَلِّقٌ بِمُشَبَّهَةً.", "«to the verb»", "«fiile»", segments=[seg("بِ", "bi", "prep"), seg("الْفِعْلِ", "fil", "noun")]),
  tok("لِكَوْنِهَا", "kawn", "noun", [K, HJ, ID, "masdar", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَكَوْنِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — اسْمُ كَانَ.", "«because of their being» — the lām of cause; the masdar annexed to its ism.", "«olmaları sebebiyle» — ta'lîl lâmı; masdar ismine muzâf.", segments=[seg("لِ", "li", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ, "kana-wa-akhawatuha"], "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَوْنِ.", "«of» — the phrase is the khabar of the masdar.", "«üzere» — masdarın haberi."),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«three»", "«üç»"),
  tok("أَحْرُفٍ", "harf", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«letters»", "«harf»"),
  tok("فَصَاعِدًا", "said-rising", "noun", [K, "hal", "ism-fail"], "الْفَاءُ عَاطِفَةٌ، وَصَاعِدًا حَالٌ مَنْصُوبٌ: فَذَاهِبًا الْعَدَدُ صَاعِدًا.", "«and upward» — the ḥāl.", "«ve yukarısı» — hâl.", punct="،", segments=fa("صَاعِدًا", "said-rising", "noun")),
  tok("وَفَتْحِ", "fath", "noun", [K, AT, ID, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَفَتْحِ مَعْطُوفٌ عَلَى كَوْنِ مَجْرُورٌ، مُضَافٌ.", "«and the fatḥa of» — joined to «their being».", "«ve fethalı olması» — kevn'e ma'tûf.", segments=wa("فَتْحِ", "fath", "noun")),
  tok("أَوَاخِرِهَا", "akhir", "noun", [K, ID, "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِإِضَافَتِهِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ آخِرٍ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«their ends» — a diptote plural, in jarr by the kasra because annexed.", "«sonlarının» — gayr-i munsarif cemi, izâfetle kesreli.", punct="،", segments=[seg("أَوَاخِرِ", "akhir", "noun"), pr3fs()]),
  tok("وَوُجُودِ", "wujud", "noun", [K, AT, ID, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَوُجُودِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the presence of»", "«ve bulunması»", segments=wa("وُجُودِ", "wujud", "noun")),
  tok("مَعْنَى", "mana", "noun", [K, ID, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the meaning of» — estimated jarr.", "«mânâsı» — takdîren mecrûr."),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»"),
  fi(),
  tok("كُلٍّ", "kull", "noun", [K, HJ], "مَجْرُورٌ بِفِي، مُنَوَّنٌ لِقَطْعِهِ عَنِ الْإِضَافَةِ لَفْظًا.", "«each» — cut from its annexation, so it carries tanwīn.", "«her biri» — izâfetten lafzan kesilmiş, tenvinli."),
  tok("مِنْهَا", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«of them»", "«onlardan»", punct=":", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
 ]})
# ----------- s3 — the six and their meanings
S.append({"id": "s3", "translation": {"en": "إِنَّ and أَنَّ are for confirmation, كَأَنَّ for likening, لٰكِنَّ for rectification, لَيْتَ for the wish, and لَعَلَّ for hope.", "tr": "İnne ve enne tahkik için, keenne teşbih için, lâkinne istidrak için, leyte temennî için, lealle terecci içindir."},
 "tokens": [
  q_mub("إِنَّ", "inna", "«inna»", "«inne»", joined=False, extra=[IA]),
  q_mub("وَأَنَّ", "anna", "«and anna»", "«ve enne»", extra=[IA]),
  lil("لِلتَّحْقِيقِ", "tahqiq", "«for confirmation»", "«tahkik için»", "،", extra=["masdar"]),
  q_mub("وَكَأَنَّ", "kaanna", "«and ka-anna»", "«ve keenne»", extra=["tashbih"]),
  lil("لِلتَّشْبِيهِ", "tashbih", "«for likening»", "«teşbih için»", "،", extra=["masdar", "tashbih"]),
  q_mub("وَلٰكِنَّ", "lakinna", "«and lākinna»", "«ve lâkinne»"),
  lil("لِلِاسْتِدْرَاكِ", "istidrak", "«for rectification»", "«istidrak için»", "،", extra=["masdar"]),
  q_mub("وَلَيْتَ", "layta", "«and layta»", "«ve leyte»", extra=["insha-wa-tamanni"]),
  lil("لِلتَّمَنِّي", "tamanni", "«for the wish»", "«temennî için»", "،", extra=["masdar", "ism-maqsur-manqus", "insha-wa-tamanni"]),
  q_mub("وَلَعَلَّ", "laalla", "«and laʿalla»", "«ve lealle»"),
  lil("لِلتَّرَجِّي", "tarajji", "«for hope»", "«terecci için»", ".", extra=["masdar", "ism-maqsur-manqus"]),
 ]})
# ----------- s4 — the front of speech, save أَنَّ
S.append({"id": "s4", "translation": {"en": "And the front of the speech belongs to them — except أَنَّ, which never stands at the front at all.", "tr": "Kelâmın başı onlarındır — enne hâriç: o hiçbir zaman başta bulunmaz."},
 "tokens": [
  tok("وَلَهَا", "li", "prep", [K, HJ, MK, "taqdim-al-musnad"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and to them belongs» — the fronted khabar.", "«onlarındır» — mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "li", "prep"), pr3fs()]),
  tok("صَدْرُ", "sadr", "noun", [K, MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the front of» — the delayed mubtada, annexed.", "«başı» — muahhar mübtedâ, muzâf."),
  tok("الْكَلَامِ", "kalam", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the speech»", "«kelâmın»"),
  tok("غَيْرَ", "ghayr", "noun", [K, IS, ID], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — أَيْ: إِلَّا أَنَّ.", "«except» — the excepted noun, annexed.", "«hâriç» — müstesnâ, muzâf."),
  tok("أَنَّ", "anna", "part", [K, IS, ID, HT, IW], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«anna» — quoted; the muḍāf ilayh.", "«enne» — hikâye edilmiş; muzâfun ileyh.", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, "la-nafiya"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so it does not»", "«o hâlde -mez»", segments=fa("لَا", "la-nafiya", "part")),
  tok("تَقَعُ", "waqaa", "verb", [K, FL, "mithal-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — مِثَالٌ وَاوِيٌّ سَقَطَتْ وَاوُهُ.", "«stand» — its doer concealed; the assimilated wāw dropped.", "«bulunmaz» — fâili müstetir; misâl fiil, vâvı düşmüş."),
  fi(),
  tok("الصَّدْرِ", "sadr", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the front»", "«başta»"),
  tok("أَصْلًا", "asl", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — أَيْ: لَا تَقَعُ وُقُوعًا أَصْلِيًّا: لَا تَقَعُ الْبَتَّةَ.", "«at all» — the absolute object of emphasis.", "«asla» — te'kid için mef'ûl-i mutlak.", punct="."),
 ]})
# ----------- s5 — ما attaches and nullifies them
S.append({"id": "s5", "translation": {"en": "And مَا has joined them, so they are stripped of their governing and come before verbs — as in «Zayd only struck».", "tr": "Mâ onlara bitişmiştir; o zaman amelden düşerler ve fiillerin önüne gelirler — «Zeyd ancak dövdü» gibi."},
 "tokens": [
  tok("وَلَحِقَهَا", "lahiqa", "verb", [K, IK, MB], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَحِقَ فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ.", "«and there has joined them» — the māḍī; the hā its object.", "«ve onlara bitişti» — mâzî; hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("لَحِقَ", "lahiqa", "verb"), pr3fs()]),
  tok("مَا", "ma-kaffa", "part", [K, IK, FL, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فَاعِلٌ فِي مَحَلِّ رَفْعٍ — مَا الْكَافَّةُ.", "«mā» — quoted; the doer — the mā that restrains.", "«mâ» — hikâye edilmiş; fâil — kâffe mâ."),
  tok("فَتُلْغَى", "algha", "verb", [K, IK, "naib-al-fail", "form-iv-verbs", "ism-maqsur-manqus"], "الْفَاءُ عَاطِفَةٌ، وَتُلْغَى مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«so they are nullified» — passive, the ḍamma estimated on the alif.", "«o zaman ilga edilir» — meçhul; dammesi elif üzerinde takdîrî.", segments=fa("تُلْغَى", "algha", "verb")),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  tok("الْعَمَلِ", "amal-governing", "noun", [K, HJ], "مَجْرُورٌ بِعَنْ.", "«governing»", "«amelden»"),
  tok("وَتَدْخُلُ", "dakhala", "verb", [K, AT, FL], "الْوَاوُ عَاطِفَةٌ، وَتَدْخُلُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and they come» — its doer concealed.", "«ve gelirler» — fâili müstetir.", segments=wa("تَدْخُلُ", "dakhala", "verb")),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«üzerine»"),
  tok("الْأَفْعَالِ", "fil", "noun", [K, HJ, "jam-taksir"], "مَجْرُورٌ بِعَلَى — جَمْعُ فِعْلٍ.", "«verbs»", "«fiillerin»", punct="،"),
  nahw(),
  tok("إِنَّمَا", "innama", "part", [K, IK, IW], "إِنَّ حَرْفُ تَوْكِيدٍ كُفَّ عَنِ الْعَمَلِ بِمَا الزَّائِدَةِ — أَدَاةُ حَصْرٍ.", "«only» — inna restrained by mā: the tool of restriction.", "«ancak» — mâ ile amelden düşmüş inne: hasr edatı.", segments=[seg("إِنَّ", "inna", "part"), seg("مَا", "ma-kaffa", "part")]),
  tok("ضَرَبَ", "daraba", "verb", [K, IK, FL], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«struck»", "«dövdü»"),
  tok("زَيْدٌ", "zayd", "propn", [K, IK, FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="."),
 ]})
# ----------- s6 — inna keeps the clause, anna makes a masdar; hence kasr and fath
S.append({"id": "s6", "translation": {"en": "Now إِنَّ does not change the meaning of the sentence, while أَنَّ with its sentence has the standing of a maṣdar; and from there it became necessary to use the kasra in the place of sentences and the fatḥa in the place of the single word.", "tr": "İnne cümlenin mânâsını değiştirmez; enne ise cümlesiyle birlikte masdar hükmündedir. Bundan dolayı cümlelerin yerinde kesre, müfredin yerinde fetha vâcip oldu."},
 "tokens": [
  tok("فَإِنَّ", "inna", "part", [K, IA, IW, MK, HT], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«for inna» — quoted; the mubtada.", "«zira inne» — hikâye edilmiş; mübtedâ.", segments=fa("إِنَّ", "inna", "part")),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«does not»", "«-mez»"),
  tok("تُغَيِّرُ", "ghayyara", "verb", [K, MK, FL, "form-ii-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«change» — the clause is the khabar.", "«değiştirir» — cümle haber."),
  tok("مَعْنَى", "mana", "noun", [K, MB, ID, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the meaning of» — the object, estimated.", "«mânâsını» — mef'ûl, takdîren."),
  tok("الْجُمْلَةِ", "jumla", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence»", "«cümlenin»", punct="،"),
  tok("وَأَنَّ", "anna", "part", [K, IA, IW, AT, MK, HT], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and anna» — quoted; the mubtada.", "«enne ise» — mübtedâ.", segments=wa("أَنَّ", "anna", "part")),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«with» — the ẓarf, annexed.", "«ile» — zarf, muzâf."),
  tok("جُمْلَتِهَا", "jumla", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its sentence»", "«cümlesi»", segments=[seg("جُمْلَتِ", "jumla", "noun"), pr3fs()]),
  fi(tags=[MK]),
  tok("حُكْمِ", "hukm", "noun", [K, HJ, ID, MK], "مَجْرُورٌ بِفِي، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«the standing of» — the phrase is the khabar.", "«hükmünde» — câr-mecrûr haber."),
  tok("الْمَصْدَرِ", "masdar-noun", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the maṣdar»", "«masdar»", punct="،"),
  tok("وَمِنْ", "min", "prep", [K, HJ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنْ حَرْفُ جَرٍّ.", "«and from»", "«ve -den»", segments=wa("مِنْ", "min", "prep")),
  tok("ثَمَّةَ", "thamma", "noun", [K, HJ, MF, "al-murab-wal-mabni-wal-irab"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ بِمِنْ — أَيْ: مِنْ هُنَاكَ، مِنْ أَجْلِ ذَلِكَ.", "«there» — a mabnī ẓarf in the place of jarr: «from there», that is, for that reason.", "«oradan» — mebnî zarf, cer mahallinde: bundan dolayı."),
  tok("وَجَبَ", "wajaba", "verb", [K, FL, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«became necessary»", "«vâcip oldu»"),
  tok("الْكَسْرُ", "kasr", "noun", [K, FL, "masdar"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the kasra» — the doer.", "«kesre» — fâil."),
  fi(),
  tok("مَوْضِعِ", "mawdi", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the place of»", "«yerinde»"),
  tok("الْجُمَلِ", "jumla", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ جُمْلَةٍ.", "«sentences»", "«cümlelerin»"),
  tok("وَالْفَتْحُ", "fath", "noun", [K, AT, FL, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالْفَتْحُ مَعْطُوفٌ عَلَى الْكَسْرُ مَرْفُوعٌ.", "«and the fatḥa» — joined to «the kasra».", "«ve fetha» — kesre'ye ma'tûf.", segments=wa("الْفَتْحُ", "fath", "noun")),
  fi(),
  tok("مَوْضِعِ", "mawdi", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the place of»", "«yerinde»"),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the single word»", "«müfredin»", punct="."),
 ]})
# ----------- s7 — kasr places 1-2: the opening, the oath's answer
S.append({"id": "s7", "translation": {"en": "So it takes the kasra at the opening — as in «indeed Zayd is standing» — and in the answer of an oath — as in «by God, indeed Zayd is standing»,", "tr": "Böylece başlangıçta kesrelenir — «şüphesiz Zeyd ayaktadır» gibi; kasemin cevabında — «vallâhi, şüphesiz Zeyd ayaktadır» gibi;"},
 "tokens": [
  tok("فَكُسِرَتْ", "kasara", "verb", [K, "naib-al-fail"], "الْفَاءُ لِلتَّفْرِيعِ، وَكُسِرَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — إِنَّ.", "«so it takes the kasra» — the passive; its deputy doer is inna.", "«böylece kesrelenir» — meçhul; nâib-i fâil inne.", segments=fa("كُسِرَتْ", "kasara", "verb")),
  fi(),
  tok("الِابْتِدَاءِ", "ibtida-start", "noun", [K, HJ, "masdar"], "مَجْرُورٌ بِفِي.", "«the opening»", "«başlangıçta»"),
  nahw(),
  *inna_zayd_qaim(),
  wafi(),
  tok("جَوَابِ", "jawab", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the answer of»", "«cevabında»"),
  tok("الْقَسَمِ", "qasam", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath»", "«kasemin»"),
  nahw(),
  tok("وَاللهِ", "allah", "propn", [K, "huruf-jarr", "qasam-note"], "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَجُمْلَةُ إِنَّ جَوَابُ الْقَسَمِ.", "«by God» — the oath wāw; inna's clause is the oath's answer.", "«vallâhi» — kasem vâvı; inne cümlesi kasemin cevabı.", segments=[seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  *inna_zayd_qaim(),
 ]})
S[-1]["tokens"][-6]["grammar"] = [K, HJ, "qasam-note"]
# ----------- s8 — kasr place 3: the sila (28:76)
S.append({"id": "s8", "translation": {"en": "and in the relative clause — as in His word, Exalted is He, «and We gave him of the treasures that whose keys would weigh down a band of strong men» (28:76),", "tr": "sılada — Allah Teâlâ'nın «Ona hazinelerden öylesini verdik ki anahtarları güçlü bir topluluğa ağır gelirdi» (28:76) sözü gibi;"},
 "tokens": [
  wafi(),
  tok("الصِّلَةِ", "sila", "noun", [K, HJ, MW], "مَجْرُورٌ بِفِي.", "«the relative clause»", "«sılada»"),
  *cite_quran(),
  tok("وَآتَيْنَاهُ", "aataa", "verb", [K, IQ, FL, "mafulayn", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَآتَيْ فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«and We gave him» — nā the doer, the hā the first object.", "«ve ona verdik» — nâ fâil, hâ birinci mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("آتَيْ", "aataa", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  tok("مِنَ", "min", "prep", [K, IQ, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  tok("الْكُنُوزِ", "kanz", "noun", [K, IQ, HJ, "jam-taksir"], "مَجْرُورٌ بِمِنْ — جَمْعُ كَنْزٍ.", "«the treasures»", "«hazinelerden»"),
  tok("مَا", "ma-mawsula", "pron", [K, IQ, MW, "mafulayn"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ.", "«that which» — the relative; the second object.", "«öylesini ki» — ism-i mevsûl; ikinci mef'ûl."),
  inna(extra=[IQ, MW], pre_ar="", pre_en="", pre_tr=""),
  tok("مَفَاتِحَهُ", "maftah", "noun", [K, IQ, IW, ID, "jam-taksir", "mamnu-min-sarf"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ مِفْتَحٍ.", "«its keys» — the ism of inna, annexed.", "«anahtarları» — inne'nin ismi, muzâf.", segments=[seg("مَفَاتِحَ", "maftah", "noun"), pr3ms()]),
  tok("لَتَنُوءُ", "naa-weigh", "verb", [K, IQ, IW, FL, "hollow-verbs", "tawkid"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَتَنُوءُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ، وَجُمْلَةُ إِنَّ صِلَةُ مَا.", "«would weigh down» — the slid lām; the clause is inna's khabar, and inna's clause is the ṣila.", "«ağır gelirdi» — kayan lâm; cümle inne'nin haberi; inne cümlesi sıla.", segments=[seg("لَ", "lam-ibtida", "part"), seg("تَنُوءُ", "naa-weigh", "verb")]),
  tok("بِالْعُصْبَةِ", "usba", "noun", [K, IQ, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْعُصْبَةِ مَجْرُورٌ.", "«a band of men»", "«bir topluluğa»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْعُصْبَةِ", "usba", "noun")]),
 ]})
# ----------- s9 — kasr places 4-5: the khabar of a concrete noun; the lam of ibtida on its khabar
S.append({"id": "s9", "translation": {"en": "and in the khabar about a concrete noun — as in «Zayd, indeed he is standing» — and in a sentence whose khabar the lām of ibtidāʾ has entered — as in «I know that Zayd is indeed standing»,", "tr": "zât isminin haberinde — «Zeyd, şüphesiz o ayaktadır» gibi; haberine ibtidâ lâmı girmiş cümlede — «bildim ki Zeyd gerçekten ayaktadır» gibi;"},
 "tokens": [
  wafi(),
  tok("الْخَبَرِ", "khabar-predicate", "noun", [K, HJ, MK], "مَجْرُورٌ بِفِي.", "«the khabar»", "«haberinde»"),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — مُتَعَلِّقٌ بِالْخَبَرِ.", "«about»", "«hakkında»"),
  tok("اسْمِ", "ism", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَنْ، مُضَافٌ.", "«a noun of»", "«isminin»"),
  tok("عَيْنٍ", "ayn-thing", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْعَيْنِ: مَا دَلَّ عَلَى ذَاتٍ، بِخِلَافِ اسْمِ الْمَعْنَى.", "«a concrete thing» — a noun of a thing, not of a meaning.", "«zât» — zât ismi, mânâ ismi değil."),
  nahw(),
  tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  inna("إِنَّهُ", pre_ar="", extra=[MK], segs=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  qaim("،", pre_ar="", extra=[MK]),
  wafi(),
  tok("جُمْلَةٍ", "jumla", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«a sentence»", "«cümlede»"),
  tok("دَخَلَتْ", "dakhala", "verb", [K, "jumla-sifa", FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ صِفَةٌ لِجُمْلَةٍ.", "«has entered» — the clause qualifies «a sentence».", "«girmiş» — cümle sıfat."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«upon»", "«üzerine»"),
  tok("خَبَرِهَا", "khabar-predicate", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its khabar»", "«haberine»", segments=[seg("خَبَرِ", "khabar-predicate", "noun"), pr3fs()]),
  tok("لَامُ", "lam-letter", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the lām of» — the doer, annexed.", "«lâmı» — fâil, muzâf."),
  tok("الِابْتِدَاءِ", "ibtida-start", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ibtidāʾ»", "«ibtidâ»"),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, FL, "zanna-wa-akhawatuha", "mafulayn"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَجُمْلَةُ إِنَّ سَدَّتْ مَسَدَّ مَفْعُولَيْهِ، وَعُلِّقَ الْفِعْلُ بِاللَّامِ.", "«I know» — the clause of inna stands for its two objects; the lām suspends the verb.", "«bildim» — inne cümlesi iki mef'ûlün yerini tutar; lâm fiili ta'lîk eder.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  inna(pre_ar="", extra=["zanna-wa-akhawatuha", "tawkid"]),
  zaydan(),
  qaim("،", full="لَقَائِمٌ", pre_ar="اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَقَائِمٌ ", segs=[seg("لَ", "lam-ibtida", "part"), seg("قَائِمٌ", "qaim", "noun")], extra=["tawkid"]),
 ]})
# ----------- s10 — kasr places 6-7: after the saying bare of doubt; after hatta of opening
S.append({"id": "s10", "translation": {"en": "and after the saying bare of doubt — as in «say: indeed God is one» — and after the حَتَّى of opening — as in «do we say that, so that indeed Zayd says it?»,", "tr": "zandan ârî kavlden sonra — «de ki: şüphesiz Allah birdir» gibi; ibtidâ hattâ'sından sonra — «bunu biz mi söyleriz ki Zeyd bile söylüyor?» gibi;"},
 "tokens": [
  wabada(),
  tok("الْقَوْلِ", "qawl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the saying»", "«kavlden»"),
  tok("الْعَرِيِّ", "ari", "noun", [K, NA, "sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ — صِفَةٌ مُشَبَّهَةٌ.", "«bare» — the naʿt.", "«ârî» — sıfat."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — مُتَعَلِّقٌ بِالْعَرِيِّ.", "«of»", "«-den»"),
  tok("الظَّنِّ", "zann", "noun", [K, HJ, "masdar", "zanna-wa-akhawatuha"], "مَجْرُورٌ بِعَنْ.", "«doubt» — supposing.", "«zan»"),
  nahw(),
  tok("قُلْ", "qala", "verb", [K, "imperative-amr", FL, "hollow-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَجُمْلَةُ إِنَّ مَقُولُ الْقَوْلِ فِي مَحَلِّ نَصْبٍ.", "«say» — the command; inna's clause is what is said, in the place of naṣb.", "«de ki» — emir; inne cümlesi mekûl-i kavl, nasb mahallinde."),
  inna(extra=["imperative-amr", MB]),
  tok("اللهَ", "allah", "propn", [K, IW], "لَفْظُ الْجَلَالَةِ اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«God» — the ism of inna.", "«Allah» — inne'nin ismi."),
  tok("وَاحِدٌ", "wahid", "noun", [K, IW], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«one» — the khabar of inna.", "«birdir» — inne'nin haberi.", punct="،"),
  wabada(),
  tok("حَتَّى", "hatta", "part", [K, ID, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«ḥattā» — quoted; the muḍāf ilayh.", "«hattâ» — hikâye edilmiş; muzâfun ileyh."),
  tok("الِابْتِدَائِيَّةِ", "ibtidai", "noun", [K, NA, "ism-mansub"], "نَعْتٌ مَجْرُورٌ — مَنْسُوبٌ إِلَى الِابْتِدَاءِ.", "«of opening» — the naʿt, a nisba.", "«ibtidâiyye» — sıfat, nisbet."),
  nahw(),
  tok("أَنَقُولُ", "qala", "verb", [K, "al-istifham", FL, "hollow-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَنَقُولُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«do we say» — the question hamza; the doer concealed.", "«biz mi söyleriz» — istifham hemzesi; fâil müstetir.", segments=[seg("أَ", "hamza-istifham", "part"), seg("نَقُولُ", "qala", "verb")]),
  tok("ذَلِكَ", "dhalika", "pron", [K, "asma-al-ishara", MB], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«bunu» — mef'ûl."),
  tok("حَتَّى", "hatta", "part", [K, "huruf-tanbih"], "حَرْفُ ابْتِدَاءٍ — تُسْتَأْنَفُ بَعْدَهُ الْجُمْلَةُ.", "«so that even» — the ḥattā of opening: a new sentence follows.", "«hattâ» — ibtidâ hattâ'sı: ardından yeni cümle."),
  inna(extra=["huruf-tanbih"]),
  zaydan(),
  tok("يَقُولُهُ", "qala", "verb", [K, IW, FL, MB, "hollow-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«says it» — the clause is inna's khabar.", "«onu söylüyor» — cümle inne'nin haberi.", punct="،", segments=[seg("يَقُولُ", "qala", "verb"), pr3ms()]),
 ]})
# ----------- s11 — kasr places 8-9: after the letters of assent; after the letters of opening
S.append({"id": "s11", "translation": {"en": "and after the letters of assent — as in «yes, indeed Zayd is standing» — and after the letters of opening — as in «lo, indeed Zayd is standing»,", "tr": "tasdik harflerinden sonra — «evet, şüphesiz Zeyd ayaktadır» gibi; iftitah harflerinden sonra — «dikkat, şüphesiz Zeyd ayaktadır» gibi;"},
 "tokens": [
  wabada(),
  *harf_x("التَّصْدِيقِ", "tasdiq", "«assent»", "«tasdik»", extra=["masdar"]),
  nahw(),
  tok("نَعَمْ", "naam", "part", [K, "jawab-al-talab"], "حَرْفُ جَوَابٍ وَتَصْدِيقٍ.", "«yes» — the letter of assent.", "«evet» — tasdik harfi."),
  *inna_zayd_qaim(),
  wabada(),
  *harf_x("الِافْتِتَاحِ", "iftitah", "«opening»", "«iftitah»", extra=["masdar"]),
  nahw(),
  tok("أَلَا", "ala-tanbih", "part", [K, "huruf-tanbih"], "حَرْفُ افْتِتَاحٍ وَتَنْبِيهٍ.", "«lo» — the letter of opening and alert.", "«dikkat» — iftitah ve tenbih harfi."),
  *inna_zayd_qaim(),
 ]})
# ----------- s12 — kasr place 10: after the waw of hal (8:5)
S.append({"id": "s12", "translation": {"en": "and after the wāw of the ḥāl — as in His word, Exalted is He, «while indeed a party of the believers were averse» (8:5).", "tr": "hâl vâvından sonra — Allah Teâlâ'nın «mü'minlerden bir grup elbette isteksizdi» (8:5) sözü gibi."},
 "tokens": [
  wabada(),
  tok("وَاوِ", "waw-letter", "noun", [K, ID, "anwa-al-waw"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the wāw of»", "«vâvından»"),
  tok("الْحَالِ", "hal", "noun", [K, ID, "hal", "anwa-al-waw"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ḥāl»", "«hâl»"),
  *cite_quran(),
  inna("وَإِنَّ", pre_ar="الْوَاوُ لِلْحَالِ، وَ", pre_en="the wāw of the ḥāl; ", pre_tr="hâl vâvı; ", extra=[IQ, "hal", "anwa-al-waw"], segs=wa("إِنَّ", "inna", "part")),
  tok("فَرِيقًا", "fariq", "noun", [K, IQ, IW], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a party» — the ism of inna.", "«bir grup» — inne'nin ismi."),
  tok("مِنَ", "min", "prep", [K, IQ, HJ, NA], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِفَرِيقًا.", "«of» — the phrase qualifies «a party».", "«-den» — câr-mecrûr sıfat."),
  tok("الْمُؤْمِنِينَ", "mumin", "noun", [K, IQ, HJ, "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِمِنْ، وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the believers» — in jarr by the yāʾ.", "«mü'minlerden» — yâ ile mecrûr."),
  tok("لَكَارِهُونَ", "karih", "noun", [K, IQ, IW, "jam-mudhakkar-salim", "ism-fail", "tawkid"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَكَارِهُونَ خَبَرُ إِنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«averse» — the slid lām; inna's khabar, in rafʿ by the wāw.", "«isteksizdi» — kayan lâm; inne'nin haberi, vâv ile merfû.", punct=".", segments=[seg("لَ", "lam-ibtida", "part"), seg("كَارِهُونَ", "karih", "noun")]),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i] and g != "qasam-note"]

CAND = {
 "thamaniya": G("thamaniya", "ثَمَانِيَة", "ث م ن", "noun", "eight (with a masculine counted noun)", "sekiz (müzekker ma'dûdla)", 2),
 "mushabbah": G("mushabbah", "مُشَبَّه", "ش ب ه", "noun", "likened, made to resemble (ism mafʿūl of شَبَّهَ); الْحُرُوفُ الْمُشَبَّهَةُ بِالْفِعْلِ", "müşebbeh — benzetilen; fiile benzeyen harfler", 4),
 "said-rising": G("said-rising", "صَاعِد", "ص ع د", "noun", "rising, going up (ism fāʿil of صَعِدَ); فَصَاعِدًا: and upward", "sâid — yükselen; fe-sâiden: ve yukarısı", 4),
 "tahqiq": G("tahqiq", "تَحْقِيق", "ح ق ق", "noun", "confirmation, verification (masdar of حَقَّقَ) — the meaning of إِنَّ and أَنَّ", "tahkik — gerçekleme; inne ve enne'nin mânâsı", 4),
 "istidrak": G("istidrak", "اسْتِدْرَاك", "د ر ك", "noun", "rectification, correcting a prior impression (masdar of اسْتَدْرَكَ) — the meaning of لٰكِنَّ", "istidrak — önceki yargıyı düzeltme; lâkinne'nin mânâsı", 5),
 "tamanni": G("tamanni", "تَمَنٍّ (التَّمَنِّي)", "م ن ي", "noun", "the wish, longing for what is unlikely (masdar of تَمَنَّى) — the meaning of لَيْتَ", "temennî — olması zor şeyi dileme; leyte'nin mânâsı", 5),
 "kaanna": G("kaanna", "كَأَنَّ", None, "part", "as if, as though — the sister of إِنَّ that likens", "keenne — sanki; benzetme bildiren inne kardeşi", 3),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but, yet — the sister of إِنَّ that rectifies", "lâkinne — fakat; istidrak bildiren inne kardeşi", 3),
 "layta": G("layta", "لَيْتَ", None, "part", "would that — the sister of إِنَّ of the wish", "leyte — keşke; temennî bildiren inne kardeşi", 3),
 "sadr": G("sadr", "صَدْر", "ص د ر", "noun", "the front, the chest; صَدْرُ الْكَلَامِ: the head of the sentence", "sadr — baş, göğüs; sadru'l-kelâm: cümlenin başı", 3, plural="صُدُور"),
 "kalam": G("kalam", "كَلَام", "ك ل م", "noun", "speech — a compound that conveys a complete sense", "kelâm — tam bir mânâ veren söz", 2),
 "asl": G("asl", "أَصْل", "أ ص ل", "noun", "the origin, the root; أَصْلًا: at all", "asıl — kök; aslen/aslâ: hiç", 3, plural="أُصُول"),
 "waqaa": G("waqaa", "وَقَعَ", "و ق ع", "verb", "to fall, to occur, to stand (in a place)", "vuku bulmak, düşmek, (bir yerde) bulunmak", 3),
 "lahiqa": G("lahiqa", "لَحِقَ", "ل ح ق", "verb", "to catch up with, to join, to attach to", "yetişmek, bitişmek, katılmak", 4),
 "ma-kaffa": G("ma-kaffa", "مَا (الْكَافَّة)", None, "part", "the mā that restrains — attached to إِنَّ and its sisters it stops their governing", "kâffe mâ — inne ve kardeşlerine bitişip amellerini durduran mâ", 5),
 "algha": G("algha", "أَلْغَى", "ل غ و", "verb", "to nullify, to cancel (a governor's work)", "ilga etmek, (ameli) geçersiz kılmak", 5),
 "amal-governing": G("amal-governing", "الْعَمَل", "ع م ل", "noun", "the governing — the effect a governor produces", "amel — âmilin meydana getirdiği tesir", 4),
 "innama": G("innama", "إِنَّمَا", None, "part", "only — إِنَّ restrained by مَا: the tool of restriction", "innemâ — ancak; mâ ile kâffe olmuş inne: hasr edatı", 3),
 "ghayyara": G("ghayyara", "غَيَّرَ", "غ ي ر", "verb", "to change, to alter", "değiştirmek", 3),
 "jumla": G("jumla", "جُمْلَة", "ج م ل", "noun", "a sentence, a clause", "cümle", 2, plural="جُمَل"),
 "maa": G("maa", "مَعَ", None, "noun", "with, together with (a ẓarf)", "ile, beraber (zarf)", 2),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "the ruling, the standing; فِي حُكْمِ الْمَصْدَرِ: counted as a maṣdar", "hüküm; masdar hükmünde", 3, plural="أَحْكَام"),
 "masdar-noun": G("masdar-noun", "مَصْدَر", "ص د ر", "noun", "the maṣdar — the verbal noun; أَنَّ with its clause stands in for one", "masdar — mastar; enne cümlesiyle masdar hükmündedir", 3, plural="مَصَادِر"),
 "thamma": G("thamma", "ثَمَّةَ", None, "noun", "there — a mabnī ẓarf of place; مِنْ ثَمَّةَ: from there, hence", "orada — mebnî mekân zarfı; min semmete: bundan dolayı", 5),
 "kasr": G("kasr", "كَسْر", "ك س ر", "noun", "the kasra — reading the hamza of إِنَّ with an i", "kesr — inne'nin hemzesini kesreli okuma", 3),
 "kasara": G("kasara", "كَسَرَ", "ك س ر", "verb", "to break; to give a kasra", "kırmak; kesrelemek", 3),
 "jawab": G("jawab", "جَوَاب", "ج و ب", "noun", "the answer — of an oath, a condition, a question", "cevap — kasemin, şartın, sorunun", 3, plural="أَجْوِبَة"),
 "sila": G("sila", "صِلَة", "و ص ل", "noun", "the relative clause — the clause that completes a mawṣūl", "sıla — mevsûlü tamamlayan cümle", 4),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give (with two objects)", "vermek (iki mef'ûllü)", 4),
 "kanz": G("kanz", "كَنْز", "ك ن ز", "noun", "a treasure", "hazine", 3, plural="كُنُوز"),
 "maftah": G("maftah", "مِفْتَح", "ف ت ح", "noun", "a key (also مِفْتَاح); the plural مَفَاتِح is a diptote", "anahtar (miftâh da denir); cemi mefâtih gayr-i munsarif", 5, plural="مَفَاتِح"),
 "naa-weigh": G("naa-weigh", "نَاءَ", "ن و أ", "verb", "to weigh down, to make stagger under a load (نَاءَ بِهِ)", "ağır gelmek, yükü altında sendeletmek", 6),
 "usba": G("usba", "عُصْبَة", "ع ص ب", "noun", "a band of men — ten to forty strong men", "usbe — on ile kırk arası güçlü topluluk", 5),
 "ayn-thing": G("ayn-thing", "عَيْن", "ع ي ن", "noun", "a concrete thing; اسْمُ عَيْنٍ: the noun of a thing (not of a meaning)", "ayn — somut şey; ism-i ayn: zât ismi", 4),
 "lam-letter": G("lam-letter", "لَام", None, "noun", "the letter lām — named as a noun", "lâm harfi — isim olarak", 4),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know (two objects)", "bilmek (iki mef'ûllü)", 2),
 "zann": G("zann", "ظَنّ", "ظ ن ن", "noun", "supposition, doubt — the opinion short of certainty", "zan — kesinliğe varmayan kanaat", 3),
 "ari": G("ari", "عَرِيّ", "ع ر ي", "noun", "bare, stripped of (عَرِيٌّ عَنْ) — a ṣifa mushabbaha", "ârî — -den sıyrılmış; sıfat-ı müşebbehe", 6),
 "ibtidai": G("ibtidai", "ابْتِدَائِيّ", "ب د أ", "noun", "of opening — حَتَّى الِابْتِدَائِيَّة, the ḥattā that opens a new sentence", "ibtidâî — yeni cümle açan hattâ", 5),
 "dhalika": G("dhalika", "ذَلِكَ", None, "pron", "that", "o, şu", 1),
 "tasdiq": G("tasdiq", "تَصْدِيق", "ص د ق", "noun", "assent, affirming as true; حُرُوفُ التَّصْدِيقِ: نَعَمْ، بَلَى، أَجَلْ", "tasdik; tasdik harfleri: neam, belâ, ecel", 4),
 "naam": G("naam", "نَعَمْ", None, "part", "yes", "evet", 1),
 "iftitah": G("iftitah", "افْتِتَاح", "ف ت ح", "noun", "the opening; حُرُوفُ الِافْتِتَاحِ: أَلَا، أَمَا — letters that open and alert", "iftitah; iftitah harfleri: elâ, emâ", 5),
 "ala-tanbih": G("ala-tanbih", "أَلَا (التَّنْبِيه)", None, "part", "lo, behold — the letter of opening and alert", "elâ — dikkat; iftitah ve tenbih harfi", 4),
 "waw-letter": G("waw-letter", "وَاو", None, "noun", "the letter wāw — named as a noun", "vâv harfi — isim olarak", 4),
 "hal": G("hal", "حَال", "ح و ل", "noun", "the state; the ḥāl — the circumstantial qualifier", "hâl — durum; hâl bildiren öğe", 2),
 "fariq": G("fariq", "فَرِيق", "ف ر ق", "noun", "a party, a group", "fırka, grup", 3),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer", "mü'min", 1, plural="مُؤْمِنُونَ"),
 "karih": G("karih", "كَارِه", "ك ر ه", "noun", "averse, unwilling (ism fāʿil of كَرِهَ)", "kârih — isteksiz, hoşlanmayan", 4, plural="كَارِهُونَ"),
 "wujud": G("wujud", "وُجُود", "و ج د", "noun", "existence, presence", "vücûd — varlık, bulunma", 3),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "each, every, all", "her, bütün", 1),
 "mana": G("mana", "مَعْنًى", "ع ن ي", "noun", "meaning", "mânâ", 2),
 "akhir": G("akhir", "آخِر", "أ خ ر", "noun", "the end, the last", "âhir — son", 2, plural="أَوَاخِر"),
 "aks": G("aks", "عَكْس", "ع ك س", "noun", "the reverse, the opposite", "aks — ters", 3),
 "thalatha": G("thalatha", "ثَلَاثَة", "ث ل ث", "noun", "three", "üç", 1),
 "sitta": G("sitta", "سِتَّة", "س ت ت", "noun", "six", "altı", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "bi": G("bi", "بِ", None, "prep", "by, with", "ile", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "that which — the relative", "mâ-i mevsûle", 3),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our", "biz", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben", 1),
 "hamza-istifham": G("hamza-istifham", "أَ (الِاسْتِفْهَام)", None, "part", "the question hamza", "istifham hemzesi", 2),
 "lam-ibtida": G("lam-ibtida", "لَ (لَامُ الِابْتِدَاءِ)", None, "part", "the lām of ibtidāʾ — slid onto the khabar of إِنَّ", "ibtidâ lâmı — inne'nin haberine kayan lâm", 4),
 "wa-qasam": G("wa-qasam", "وَ (الْقَسَم)", None, "part", "the wāw of the oath", "kasem vâvı", 3),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "lahiqa", _sg.sound1("samia", "لَحِق", "لْحَق", "اِلْحَق", "لُحُوق", "لَاحِق", "مَلْحُوق", "لُحِقَ", "يُلْحَقُ", "لَحِقَ يَلْحَقُ: أَدْرَكَهُ وَاتَّصَلَ بِهِ — بَابُ سَمِعَ"))
put_morph(mo, "algha", _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ", "أَلْغَ", "لْغ", "i", "أَلْغ", "إِلْغَاء", "مُلْغٍ", "مُلْغًى", "أُلْغِيَ", "يُلْغَى", "أَلْغَى يُلْغِي: أَبْطَلَ — نَاقِصٌ مِنَ الْإِفْعَالِ: تُلْغَى عَنِ الْعَمَلِ بِضَمَّةٍ مُقَدَّرَةٍ"))
put_morph(mo, "naa-weigh", _sg.entry(_sg.BABS["nasara"][0] + " — أَجْوَفُ وَاوِيٌّ مَهْمُوزُ اللَّامِ", _sg.BABS["nasara"][1], "نَوْء", "نَائِئ",
    ["نَاءَ", "نَاءَا", "نَاءُوا", "نَاءَتْ", "نَاءَتَا", "نُؤْنَ", "نُؤْتَ", "نُؤْتُمَا", "نُؤْتُمْ", "نُؤْتِ", "نُؤْتُمَا", "نُؤْتُنَّ", "نُؤْتُ", "نُؤْنَا"],
    ["يَنُوءُ", "يَنُوءَانِ", "يَنُوءُونَ", "تَنُوءُ", "تَنُوءَانِ", "يَنُؤْنَ", "تَنُوءُ", "تَنُوءَانِ", "تَنُوءُونَ", "تَنُوئِينَ", "تَنُوءَانِ", "تَنُؤْنَ", "أَنُوءُ", "نَنُوءُ"],
    ["نُؤْ", "نُوءَا", "نُوءُوا", "نُوئِي", "نُوءَا", "نُؤْنَ"],
    "يَنُوءَ", "يَنُؤْ", "تَنُؤْ", note="أَجْوَفُ وَاوِيٌّ مَهْمُوزُ اللَّامِ: نَاءَ يَنُوءُ ← لَمْ يَنُؤْ؛ نَاءَ بِالْحِمْلِ: نَهَضَ بِهِ مُثْقَلًا، وَنَاءَ بِهِ الْحِمْلُ: أَثْقَلَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch4 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "مَوَاضِعُ كَسْرِ إِنَّ — حَيْثُ تَبْقَى الْجُمْلَةُ جُمْلَةً", "en": "Where إِنَّ takes the kasra — wherever the clause stays a clause", "tr": "İnne'nin kesre yerleri — cümlenin cümle kaldığı her yer"},
 "level": 4, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الحروف المشبهة بالفعل", "الكافية لابن الحاجب — إنّ وأخواتها", "مغني اللبيب لابن هشام — إنّ المكسورة والمفتوحة"],
 "amil": "إِنَّ لَا تُغَيِّرُ مَعْنَى الْجُمْلَةِ وَأَنَّ مَعَ جُمْلَتِهَا فِي حُكْمِ الْمَصْدَرِ — the kasra stands where a SENTENCE is wanted, the fatḥa where a single word (a maṣdar) is wanted",
 "question": {
  "en": ["WHICH letters govern two nouns with the manṣūb first? Eight; six of them resemble the verb — three letters or more, a fatḥa at the end, a verb's meaning inside: إِنَّ / أَنَّ confirm, كَأَنَّ likens, لٰكِنَّ rectifies, لَيْتَ wishes, لَعَلَّ hopes.",
         "WHERE do they stand? At the front of the speech — all but أَنَّ, which never opens a sentence. And when مَا clings to them they lose their governing and may precede a verb: إِنَّمَا ضَرَبَ زَيْدٌ.",
         "WHY kasra here and fatḥa there? إِنَّ leaves the sentence a sentence; أَنَّ turns it into a maṣdar. So read the hamza with an i wherever a SENTENCE belongs, with an a wherever a single WORD belongs.",
         "The TEST: can you swap in a maṣdar? عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ = عَلِمْتُ قِيَامَ زَيْدٍ → fatḥa. إِنَّ زَيْدًا قَائِمٌ at the opening — no maṣdar can start a speech that way → kasra.",
         "The TEN kasra places: (1) the opening; (2) the answer of an oath — وَاللهِ إِنَّ; (3) the ṣila — مَا إِنَّ مَفَاتِحَهُ لَتَنُوءُ (28:76); (4) the khabar of a concrete noun — زَيْدٌ إِنَّهُ قَائِمٌ; (5) when the lām of ibtidāʾ sits on its khabar — عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ.",
         "…(6) after قَالَ bare of doubt — قُلْ إِنَّ اللهَ وَاحِدٌ; (7) after the ḥattā of opening — حَتَّى إِنَّ زَيْدًا يَقُولُهُ; (8) after نَعَمْ; (9) after أَلَا; (10) after the wāw of the ḥāl — وَإِنَّ فَرِيقًا مِنَ الْمُؤْمِنِينَ لَكَارِهُونَ (8:5).",
         "What does the lām of ibtidāʾ DO to the hamza? It forces the kasra: a lām cannot sit inside a maṣdar, so عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ — and the verb عَلِمَ is suspended (مُعَلَّق) by that lām.",
         "What does the engine READ here? The DabtEngine finds إِنَّ by its three letters and sets the ism in naṣb and the khabar in rafʿ, keeps the slid لَ as a prefix of the khabar (لَقَائِمٌ, لَكَارِهُونَ), reads the quoted particles as mubtadas with لِ-khabars, and hands the kasra/fatḥa choice to the rule above: a sentence seat → إِنَّ, a word seat → أَنَّ."],
  "tr": ["Mansûbu önce gelen iki isimde HANGİ harfler âmildir? Sekiz; altısı fiile benzer — üç ve daha fazla harf, sonda fetha, içinde fiil mânâsı: inne / enne tahkik, keenne teşbih, lâkinne istidrak, leyte temennî, lealle terecci.",
         "NEREDE bulunurlar? Kelâmın başında — enne hâriç: o hiçbir zaman cümle açmaz. Mâ bitişince amelden düşer ve fiilin önüne gelebilirler: innemâ darabe Zeyd.",
         "NEDEN burada kesre, orada fetha? İnne cümleyi cümle bırakır; enne onu masdar yapar. Öyleyse CÜMLE'nin yerinde hemzeyi i ile, tek KELİME'nin yerinde a ile oku.",
         "TEST: yerine masdar koyabiliyor musun? Alimtü enne Zeyden kâimün = alimtü kıyâme Zeydin → fetha. Başta inne Zeyden kâimün — hiçbir masdar kelâmı öyle açamaz → kesre.",
         "ON kesre yeri: (1) başlangıç; (2) kasemin cevabı — vallâhi inne; (3) sıla — mâ inne mefâtihahû le-tenûu (28:76); (4) zât isminin haberi — Zeydün innehû kâimün; (5) haberinde ibtidâ lâmı varsa — alimtü inne Zeyden le-kâimün.",
         "…(6) zandan ârî kâle'den sonra — kul inne'llâhe vâhidün; (7) ibtidâ hattâ'sından sonra — hattâ inne Zeyden yekûluhû; (8) neam'dan sonra; (9) elâ'dan sonra; (10) hâl vâvından sonra — ve inne ferîkan mine'l-mü'minîne le-kârihûn (8:5).",
         "İbtidâ lâmı hemzeye NE YAPAR? Kesreyi zorunlu kılar: lâm bir masdarın içinde duramaz; alimtü inne Zeyden le-kâimün — ve alime fiili o lâmla ta'lîk edilir.",
         "Motor burada neyi OKUR? DabtEngine inne'yi üç harfinden bulur, ismini nasb, haberini ref' eder, kayan lâm'ı haberin öneki olarak tutar (le-kâimün, le-kârihûn), hikâye edilen harfleri li-haberli mübtedâ okur ve kesre/fetha seçimini yukarıdaki kurala bırakır: cümle yeri → inne, kelime yeri → enne."]
 },
 "plain": {"en": "Six little words (إِنَّ and its sisters) grab two nouns: the first goes into naṣb, the second into rafʿ. Read إِنَّ with an i wherever a whole sentence is wanted, with an a wherever a single word would do.",
           "tr": "Altı küçük kelime (inne ve kardeşleri) iki isim yakalar: birincisi nasb, ikincisi ref' olur. Tam bir cümle istenen yerde inne'yi i ile, tek kelime yeterli olan yerde a ile oku."},
 "explanation": {"en": "Birgivī's first division of the governor in two nouns: eight letters whose manṣūb precedes their marfūʿ. Six resemble the verb — إِنَّ / أَنَّ for confirmation, كَأَنَّ for likening, لٰكِنَّ for rectification, لَيْتَ for the wish, لَعَلَّ for hope. They claim the front of the speech (all but أَنَّ), and مَا attached to them cancels their governing (إِنَّمَا ضَرَبَ زَيْدٌ). Because إِنَّ keeps the sentence a sentence while أَنَّ turns it into a maṣdar, the kasra is required wherever a sentence belongs and the fatḥa wherever a single word belongs. The kasra places: the opening; the answer of an oath; the ṣila (28:76); the khabar of a concrete noun; a sentence whose khabar carries the lām of ibtidāʾ; after a قَوْل bare of doubt; after the ḥattā of opening; after the letters of assent; after the letters of opening; after the wāw of the ḥāl (8:5).",
                 "tr": "Birgivî'nin iki isimdeki âmilin birinci kısmı: mansûbu merfûundan önce gelen sekiz harf. Altısı fiile benzer — inne / enne tahkik, keenne teşbih, lâkinne istidrak, leyte temennî, lealle terecci. Kelâmın başı onlarındır (enne hâriç); onlara bitişen mâ amellerini kaldırır (innemâ darabe Zeyd). İnne cümleyi cümle bıraktığı, enne ise masdar yaptığı için, cümle yerinde kesre, kelime yerinde fetha vâciptir. Kesre yerleri: başlangıç; kasemin cevabı; sıla (28:76); zât isminin haberi; haberinde ibtidâ lâmı bulunan cümle; zandan ârî kavlden sonra; ibtidâ hattâ'sından sonra; tasdik harflerinden sonra; iftitah harflerinden sonra; hâl vâvından sonra (8:5)."},
 "examples": [
  {"ar": "إِنَّ وَأَنَّ لِلتَّحْقِيقِ، وَكَأَنَّ لِلتَّشْبِيهِ، وَلٰكِنَّ لِلِاسْتِدْرَاكِ، وَلَيْتَ لِلتَّمَنِّي، وَلَعَلَّ لِلتَّرَجِّي", "en": "the six letters resembling the verb, with their meanings", "tr": "fiile benzeyen altı harf ve mânâları", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "إِنَّمَا ضَرَبَ زَيْدٌ", "en": "مَا restrains إِنَّ: no governing, and a verb may follow", "tr": "mâ inne'yi kâffe yapar: amel yok, fiil gelebilir", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "وَاللهِ إِنَّ زَيْدًا قَائِمٌ", "en": "the oath's answer is a sentence — kasra", "tr": "kasemin cevabı cümledir — kesre", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "مَا إِنَّ مَفَاتِحَهُ لَتَنُوءُ بِالْعُصْبَةِ", "en": "the ṣila is a sentence — kasra (28:76)", "tr": "sıla cümledir — kesre (28:76)", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ", "en": "the lām of ibtidāʾ on the khabar forces the kasra and suspends عَلِمَ", "tr": "haberdeki ibtidâ lâmı kesreyi zorlar ve alime'yi ta'lîk eder", "sourceStory": "izhar-al-asrar", "sentence": "s9"},
  {"ar": "وَإِنَّ فَرِيقًا مِنَ الْمُؤْمِنِينَ لَكَارِهُونَ", "en": "after the wāw of the ḥāl — kasra (8:5)", "tr": "hâl vâvından sonra — kesre (8:5)", "sourceStory": "izhar-al-asrar", "sentence": "s12"},
 ],
 "commonMistakes": [
  {"wrong": "عَلِمْتُ أَنَّ زَيْدًا لَقَائِمٌ", "right": "عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ", "why": {"en": "the lām of ibtidāʾ cannot live inside a maṣdar — once the khabar carries لَ, the hamza must take the kasra", "tr": "ibtidâ lâmı masdarın içinde yaşayamaz — haber le- taşıyınca hemze kesre almak zorundadır"}},
  {"wrong": "أَنَّ زَيْدًا قَائِمٌ", "right": "إِنَّ زَيْدًا قَائِمٌ", "why": {"en": "أَنَّ never opens a speech — the front of the sentence belongs to إِنَّ", "tr": "enne hiçbir zaman kelâm açmaz — cümlenin başı inne'nindir"}},
  {"wrong": "إِنَّمَا زَيْدًا قَائِمٌ", "right": "إِنَّمَا زَيْدٌ قَائِمٌ", "why": {"en": "مَا has stripped إِنَّ of its governing — the noun after إِنَّمَا is a plain mubtada", "tr": "mâ inne'nin amelini kaldırmıştır — innemâ'dan sonraki isim düz mübtedâdır"}},
 ],
}
ADD_EN = (" Chapter 4 (print pp. 94-96): the governor in two nouns, first division — the eight letters whose manṣūb precedes their marfūʿ; the six "
          "letters resembling the verb and their meanings (s1-s3); the front of speech save أَنَّ, and the restraining مَا with إِنَّمَا ضَرَبَ زَيْدٌ (s4-s5); "
          "إِنَّ keeps the sentence while أَنَّ makes a maṣdar, hence the kasra in a sentence's place and the fatḥa in a word's (s6); the ten kasra places "
          "with 28:76 and 8:5 (s7-s12). Two readings of the lithograph's transcription: before «لَهَا صَدْرُ الْكَلَامِ» it carries an unclear «ومعها», "
          "which the text leaves out; and «ولحقها ما» is read as the māḍī «وَلَحِقَهَا مَا» with the conditional sense the received wording carries.")
ADD_TR = (" Dördüncü bab (baskı s. 94-96): iki isimde âmilin birinci kısmı — mansûbu merfûundan önce gelen sekiz harf; fiile benzeyen altı harf ve "
          "mânâları (s1-s3); enne hâriç kelâmın başı, ve innemâ darabe Zeyd ile kâffe mâ (s4-s5); inne cümleyi korur, enne masdar yapar; bu yüzden cümle "
          "yerinde kesre, kelime yerinde fetha (s6); 28:76 ve 8:5 ile on kesre yeri (s7-s12). Taşbaskı transkripsiyonunda iki okuma: «lehâ sadru'l-kelâm» "
          "önünde anlaşılmaz bir «ومعها» vardır, metin bunu almamıştır; «ولحقها ما» ise alınan metnin şart mânâsıyla «ve lahikahâ mâ» mâzîsi olarak okunmuştur.")
write_out(4, S, TITLE, ADD_EN, ADD_TR, "pp. 94-96", GLOSS_ADD, notes=(NOTE,),
          related=((IW, [K]), (IA, [K]), (IK, [K]), ("an-masdariyya", [K]), (K1, [K]), ("hadhf-al-jarr", [K])))
report(4, S, GLOSS_ADD, (NOTE,))
