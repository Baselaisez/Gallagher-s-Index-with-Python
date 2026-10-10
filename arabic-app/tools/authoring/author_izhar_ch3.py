# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 3: the OMISSION of the jarr letter. Qiyāsī in three places — the mafʿūl fīh (the time
# ẓarf, the vague place ẓarf: the six directions, عِنْدَ/لَدَى/وَسْطَ/بَيْنَ/إِزَاءَ/حِذَاءَ/تِلْقَاءَ, the measured distances;
# the exceptions جَانِبًا/وَجْهًا/وَسَطًا/خَارِجَ/دَاخِلَ/جَوْفَ, the place-noun not meaning rest, the bounded ẓarf save after
# دَخَلَ/نَزَلَ/سَكَنَ), the mafʿūl lah under its conditions, and أَنْ/أَنَّ; the samāʿī kept, not extended; ḥadhf wa-īṣāl
# (the maḥallī iʿrāb surfaces); the shādhdh that stays majrūr; no two letters of one meaning on one verb. Print pp. 91–94.
#   python3 author_izhar_ch3.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "hadhf-al-jarr"
K2 = "mahall-al-majrur"
K1 = "al-amil-wa-aqsamuh"
TITLE = {"ar": "حَذْفُ الْجَارِّ: الْقِيَاسِيُّ وَالسَّمَاعِيُّ، وَالْحَذْفُ وَالْإِيصَالُ", "en": "The omission of the governing letter — by rule and by hearing, and the omission with connection", "tr": "Câr harfinin hazfi — kıyâsî ve semâî; hazf ve îsâl"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; ML = "maful-lah"; IS = "istithna"; KN = "kana-wa-akhawatuha"; SH = "in-shartiyya"; IQ = "al-iqtibas-wal-tadmin"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def ala(punct=None): return tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzere».", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ.", "«or».", "«ya da».")
def fi(punct=None, tags=()): return tok("فِي", "fi", "prep", [K, HJ] + list(tags), "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def fi_q(full="فِي", pre="", punct=None):
    """the letter فِي mentioned as a word"""
    segs = wa("فِي", "fi", "prep") if full.startswith("وَ") else None
    return tok(full, "fi", "prep", [K, HT, ID], pre + "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«fī» — the letter quoted as a word, annexed to حَذْف.", "«fî» — hikâye edilmiş lafız, muzâfun ileyh mahallinde.", punct=punct, segments=segs)
def hadhf_fi(full="حَذْفُ", ar="مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en="«the omission of» — the mubtada, annexed.", tr="«hazfi» — mübtedâ, muzâf."):
    return tok(full, "hadhf", "noun", [K, MK, ID, "masdar"], ar, en, tr)
def quoted(full, lex, pos, en, tr, mahall_ar, mahall_en, mahall_tr, punct=None, joined=True, extra=()):
    segs = wa(full[2:], lex, pos) if joined else None
    ar = ("الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، " if joined else "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، ") + mahall_ar + "."
    return tok(full, lex, pos, [K, HT] + list(extra), ar, en + " — quoted as a word; " + mahall_en + ".", tr + " — hikâye edilmiş; " + mahall_tr + ".", punct=punct, segments=segs)
def q_raf(full, lex, en, tr, punct=None, joined=True, extra=()):
    return quoted(full, lex, "noun", en, tr, "مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ" if joined else "خَبَرٌ فِي مَحَلِّ رَفْعٍ", "joined, in the place of rafʿ" if joined else "the khabar, in the place of rafʿ", "ma'tûf, ref' mahallinde" if joined else "haber, ref' mahallinde", punct=punct, joined=joined, extra=extra)
def in_kana(full_in="إِنْ", pre_ar=""):
    return [tok(full_in, "in-shartiyya", "part", [K, SH], pre_ar + "إِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional.", "«eğer» — cezm eden şart harfi.", segments=(fa("إِنْ", "in-shartiyya", "part") if full_in.startswith("فَ") else (wa("إِنْ", "in-shartiyya", "part") if full_in.startswith("وَ") else None))),
            tok("كَانَ", "kana", "verb", [K, KN, SH], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is» — kāna, the shart verb, its ism concealed.", "«ise» — nâkıs kâne, şart fiili, ismi müstetir.")]
def zarf_x(x_full, x_lex, x_en, x_tr, tags=()):
    return [tok("ظَرْفَ", "zarf", "noun", [K, KN, ID, MF] + list(tags), "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«a ẓarf of» — kāna's khabar, annexed.", "«zarfı» — kâne'nin haberi, muzâf."),
            tok(x_full, x_lex, "noun", [K, ID, MF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", x_en, x_tr)]
def ma_lam_yathbut(neg=True):
    out = [tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the mubtada.", "«o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
           tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the relative, the khabar.", "«… olan» — ism-i mevsûl, haber.")]
    if neg:
        out += [tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — the jazim.", "«-medi» — cezm eden nefy harfi."),
                tok("يَثْبُتْ", "thabata", "verb", [K, "lam-jazim", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْجُمْلَةُ صِلَةٌ.", "«is established» — majzūm; the ṣila.", "«sâbit olmadı» — meczûm; sıla.")]
    else:
        out += [tok("ثَبَتَ", "thabata", "verb", [K, "ism-mawsul"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«is established» — the ṣila.", "«sâbit oldu» — sıla.")]
    out += [tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — الْعَائِدُ.", "«for it» — the returning pronoun.", "«ona» — âid zamir.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
            tok("اسْمٌ", "ism", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a name» — the doer.", "«bir isim» — fâil."),
            tok("بِسَبَبِ", "sabab", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَسَبَبِ مَجْرُورٌ، مُضَافٌ.", "«by reason of»", "«sebebiyle»", segments=[seg("بِ", "bi", "prep"), seg("سَبَبِ", "sabab", "noun")]),
            tok("أَمْرٍ", "amr-noun", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a matter»", "«bir husus»"),
            tok("دَاخِلٍ", "dakhil", "noun", [K, NA, "ism-fail"], "نَعْتٌ لِأَمْرٍ مَجْرُورٌ — اسْمُ فَاعِلٍ.", "«included» — the naʿt.", "«dâhil» — sıfat."),
            fi(),
            tok("مُسَمَّاهُ", "musamma", "noun", [K, HJ, ID, "ism-maqsur-manqus", "ism-maful"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what it names» — majrūr, estimated.", "«müsemmâsı» — takdîren mecrûr.", punct="،", segments=[seg("مُسَمَّا", "musamma", "noun"), pr3ms()])]
    return out
def mansub_item(full, lex, en, tr, punct=None, tags=(), ar="مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ."):
    segs = wa(full[2:], lex, "noun") if full.startswith("وَ") else None
    return tok(full, lex, "noun", [K, AT, IS] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if segs else "") + ar, en, tr, punct=punct, segments=segs)
def majrur_item(full, lex, en, tr, punct=None, tags=(), pre_ar=""):
    segs = wa(full[2:], lex, "noun") if full.startswith("وَ") else None
    return tok(full, lex, "noun", [K, AT, HJ] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if segs else "") + pre_ar + "مَعْطُوفٌ مَجْرُورٌ.", en, tr, punct=punct, segments=segs)
def cite_quran(punct=":"):
    return [tok("نَحْوَ", "nahwa", "noun", [K, MF, HT, ID, IQ], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفٌ بِمَعْنَى مِثْلَ، مُضَافٌ.", "«as in» — the citation ẓarf, annexed.", "«meselâ» — iktibas zarfı, muzâf."),
            tok("قَوْلِهِ", "qawl", "noun", [K, ID, IQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
            tok("تَعَالَى", "taala", "verb", [K, IQ, "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«Exalted is He»", "«yüce»", punct=punct)]
def ay(punct=":"): return tok("أَيْ", "ay", "part", [K, HT, "amma-tafsiliyya"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».", punct=punct)

# ----------- s1 — the letter may be omitted; two kinds
S.append({"id": "s1", "translation": {"en": "The governing letter may be omitted, and this is of two kinds: by rule (qiyāsī) and by hearing (samāʿī).", "tr": "Câr harfi hazfedilebilir; bu iki türlüdür: kıyâsî ve semâî."},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«and sometimes» — qad of rarity before a muḍāriʿ.", "«ve bazen» — muzâriyle taklîl kad'ı.", segments=wa("قَدْ", "qad", "part")),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, "naib-al-fail", HT], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is omitted» — the passive.", "«hazfedilir» — meçhul."),
  tok("الْجَارُّ", "jarr-letter", "noun", [K, "naib-al-fail", "doubled-verbs"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«the governing letter» — the deputy of the doer.", "«câr» — nâib-i fâil.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the phrase is the khabar.", "«üzere» — câr-mecrûr haber."),
  tok("نَوْعَيْنِ", "naw", "noun", [K, HJ, "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two kinds» — majrūr by the yāʾ.", "«iki tür» — yâ ile mecrûr, tesniye.", punct=":"),
  tok("قِيَاسِيٌّ", "qiyasi", "noun", [K, MK, HT, "badal"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا قِيَاسِيٌّ.", "«by rule» — the khabar of a dropped «one of them».", "«kıyâsî» — mahzûf mübtedânın haberi."),
  tok("وَسَمَاعِيٌّ", "samai", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَسَمَاعِيٌّ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَالْآخَرُ سَمَاعِيٌّ.", "«and by hearing»", "«ve semâî»", punct=".", segments=wa("سَمَاعِيٌّ", "samai", "noun")),
 ]})
# ----------- s2 — the three places; the first: the maf'ul fih of time
S.append({"id": "s2", "translation": {"en": "The one by rule is in three places. The first is the mafʿūl fīh: omitting فِي from it is the rule if it is a ẓarf of time, vague or bounded — as in «I travelled a while» and «I fasted a month»,", "tr": "Kıyâsî olan üç yerdedir. Birincisi mef'ûlün fîhtir: müphem olsun mahdûd olsun bir zaman zarfı ise ondan fî'yi hazfetmek kıyastır — «bir süre yürüdüm», «bir ay oruç tuttum» gibi;"},
 "tokens": [
  tok("فَالْقِيَاسِيُّ", "qiyasi", "noun", [K, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَالْقِيَاسِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«the one by rule» — the mubtada.", "«kıyâsî olan» — mübtedâ.", segments=fa("الْقِيَاسِيُّ", "qiyasi", "noun")),
  fi(tags=[MK]),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID, "tamyiz"], "مَجْرُورٌ بِفِي، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«three» — the phrase is the khabar.", "«üç» — câr-mecrûr haber."),
  tok("مَوَاضِعَ", "mawdi", "noun", [K, ID, "mamnu-min-sarf", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«places» — a diptote, jarr by the fatḥa.", "«yerde» — gayr-i munsarif, fetha ile mecrûr.", punct=":"),
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«birincisi» — mübtedâ."),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, MF, "ism-maful"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("فِيهِ", "fi", "prep", [K, HJ, MF], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ الْمُرَكَّبِ: الْمَفْعُولُ فِيهِ.", "«fīh» — the second half of the term's name.", "«fîh» — terimin ikinci yarısı.", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("فَإِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for» — inna.", "«çünkü» — inne.", segments=fa("إِنَّ", "inna", "part")),
  tok("حَذْفَ", "hadhf", "noun", [K, "inna-wa-akhawatuha", ID, "masdar"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the omission of» — inna's ism, annexed.", "«hazfi» — inne'nin ismi, muzâf."),
  fi_q(),
  tok("مِنْهُ", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِحَذْفَ.", "«from it»", "«ondan»", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("قِيَاسٌ", "qiyas", "noun", [K, "inna-wa-akhawatuha"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«is the rule» — inna's khabar.", "«kıyastır» — inne'nin haberi."),
  *in_kana(),
  *zarf_x("زَمَانٍ", "zaman", "«time»", "«zaman»"),
  tok("مُبْهَمًا", "mubham", "noun", [K, KN, "ism-maful"], "خَبَرُ كَانَ الثَّانِيَةِ الْمَحْذُوفَةِ مَنْصُوبٌ، وَالتَّقْدِيرُ: سَوَاءٌ كَانَ مُبْهَمًا.", "«vague» — the khabar of the next كَانَ (read: whether it be vague).", "«müphem» — sonraki kâne'nin haberi (müphem olsun)."),
  tok("كَانَ", "kana", "verb", [K, KN], "فِعْلٌ مَاضٍ نَاقِصٌ، اسْمُهُ مُسْتَتِرٌ، وَخَبَرُهُ مُبْهَمًا الْمُتَقَدِّمُ.", "«be it» — kāna with its khabar fronted.", "«olsun» — haberi öne alınmış kâne."),
  aw(),
  tok("مَحْدُودًا", "mahdud", "noun", [K, AT, "ism-maful"], "مَعْطُوفٌ عَلَى مُبْهَمًا مَنْصُوبٌ.", "«bounded» — joined.", "«mahdûd» — ma'tûf.", punct="،"),
  nahw(),
  tok("سِرْتُ", "sara-travel", "verb", [K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالتَّاءُ فَاعِلٌ.", "«I travelled»", "«yürüdüm»", segments=[seg("سِرْ", "sara-travel", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("حِينًا", "hin", "noun", [K, MF, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفُ زَمَانٍ مُبْهَمٌ حُذِفَتْ مِنْهُ فِي.", "«a while» — the mafʿūl fīh, فِي omitted.", "«bir süre» — mef'ûlün fîh, fî hazfedilmiş."),
  tok("وَصُمْتُ", "saama", "verb", [K, AT, "fail", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَصُمْتُ فِعْلٌ مَاضٍ أَجْوَفُ، وَالتَّاءُ فَاعِلٌ.", "«and I fasted»", "«ve oruç tuttum»", segments=[seg("وَ", "wa", "conj"), seg("صُمْ", "saama", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("شَهْرًا", "shahr", "noun", [K, MF, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفُ زَمَانٍ مَحْدُودٌ.", "«a month» — the bounded ẓarf.", "«bir ay» — mahdûd zarf.", punct="،"),
 ]})
# ----------- s3 — or a vague place zarf: the six directions
S.append({"id": "s3", "translation": {"en": "or a vague ẓarf of place — which is what has no name of its own by reason of something within what it names — like the six directions, namely: before, in front, behind, right, left, above, below,", "tr": "ya da müphem bir mekân zarfı ise — ki o, müsemmâsının içindeki bir husus sebebiyle kendine bir isim sâbit olmayandır — altı cihet gibi: ön, ön, arka, sağ, sol, üst, alt;"},
 "tokens": [
  aw(),
  *zarf_x("مَكَانٍ", "makan", "«place»", "«mekân»"),
  tok("مُبْهَمًا", "mubham", "noun", [K, NA, "ism-maful"], "نَعْتٌ لِظَرْفَ مَنْصُوبٌ.", "«vague» — the naʿt.", "«müphem» — sıfat.", punct="،"),
  *ma_lam_yathbut(neg=True),
  tok("كَالْجِهَاتِ", "jiha", "noun", [K, HJ, MK, "jam-muannath-salim"], "الْكَافُ حَرْفُ جَرٍّ، وَالْجِهَاتِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ كَالْجِهَاتِ.", "«like the directions» — the khabar of a dropped «and that is».", "«cihetler gibi» — mahzûf mübtedânın haberi.", segments=[seg("كَ", "ka", "prep"), seg("الْجِهَاتِ", "jiha", "noun")]),
  tok("السِّتِّ", "sitt", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«six» — the naʿt.", "«altı» — sıfat."),
  tok("وَهِيَ", "hiya", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are» — the mubtada.", "«ve onlar» — mübtedâ.", punct=":", segments=wa("هِيَ", "hiya", "pron")),
  q_raf("أَمَامُ", "amama", "«before»", "«ön»", joined=False, extra=[MF]),
  q_raf("وَقُدَّامُ", "quddam", "«in front»", "«ön»", extra=[MF]),
  q_raf("وَخَلْفُ", "khalf", "«behind»", "«arka»", extra=[MF]),
  q_raf("وَيَمِينُ", "yamin", "«right»", "«sağ»", extra=[MF]),
  q_raf("وَشِمَالُ", "shimal", "«left»", "«sol»", extra=[MF]),
  q_raf("وَفَوْقُ", "fawqa", "«above»", "«üst»", extra=[MF]),
  q_raf("وَتَحْتُ", "tahta", "«below»", "«alt»", punct="،", extra=[MF]),
 ]})
# ----------- s4 — and عند … and the measured distances
S.append({"id": "s4", "translation": {"en": "and like عِنْدَ, لَدَى, وَسْطَ with a sukūn on the sīn, بَيْنَ, إِزَاءَ, حِذَاءَ and تِلْقَاءَ; and like the measured distances — as in a farsakh, a mile, a post-stage,", "tr": "ve inde, ledâ, sin'i sâkin vasta, beyne, izâe, hizâe ve tilkâe gibi; ölçülmüş mesafeler gibi — fersah, mil, berîd;"},
 "tokens": [
  tok("وَكَعِنْدَ", "inda", "noun", [K, HJ, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ حَرْفُ جَرٍّ، وَعِنْدَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — مَعْطُوفٌ عَلَى كَالْجِهَاتِ.", "«and like ʿinda» — quoted under the kāf.", "«ve inde gibi» — kâf altında hikâye edilmiş.", segments=[seg("وَ", "wa", "conj"), seg("كَ", "ka", "prep"), seg("عِنْدَ", "inda", "noun")]),
  quoted("وَلَدَى", "lada", "noun", "«and ladā»", "«ve ledâ»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", extra=[MF]),
  quoted("وَوَسْطَ", "wast", "noun", "«and wasṭa»", "«ve vasta»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", extra=[MF]),
  tok("بِسُكُونِ", "sukun", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَسُكُونِ مَجْرُورٌ، مُضَافٌ — حَالٌ.", "«with a sukūn on»", "«sükûnuyla»", segments=[seg("بِ", "bi", "prep"), seg("سُكُونِ", "sukun", "noun")]),
  tok("السِّينِ", "sin-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sīn»", "«sin'in»"),
  quoted("وَبَيْنَ", "bayna", "noun", "«and bayna»", "«ve beyne»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", extra=[MF]),
  quoted("وَإِزَاءَ", "izaa", "noun", "«and izāʾa»", "«ve izâe»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", extra=[MF]),
  quoted("وَحِذَاءَ", "hidhaa", "noun", "«and ḥidhāʾa»", "«ve hizâe»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", extra=[MF]),
  quoted("وَتِلْقَاءَ", "tilqaa", "noun", "«and tilqāʾa»", "«ve tilkâe»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", punct="،", extra=[MF]),
  tok("وَكَالْمَقَادِيرِ", "miqdar", "noun", [K, HJ, AT, "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ حَرْفُ جَرٍّ، وَالْمَقَادِيرِ مَجْرُورٌ — مَعْطُوفٌ عَلَى كَالْجِهَاتِ.", "«and like the measures»", "«ve miktarlar gibi»", segments=[seg("وَ", "wa", "conj"), seg("كَ", "ka", "prep"), seg("الْمَقَادِيرِ", "miqdar", "noun")]),
  tok("الْمَمْسُوحَةِ", "mamsuh", "noun", [K, NA, "ism-maful"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ.", "«measured» — the naʿt.", "«ölçülmüş» — sıfat."),
  nahw(),
  tok("فَرْسَخٍ", "farsakh", "noun", [K, MK, HT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَجْرُورٌ بِإِضَافَةِ نَحْوُ: نَحْوُ لَفْظِ فَرْسَخٍ.", "«a farsakh» — annexed to نَحْوُ.", "«fersah» — nahvü'ye muzâfun ileyh."),
  majrur_item("وَمِيلٍ", "mil-mile", "«and a mile»", "«ve mil»"),
  majrur_item("وَبَرِيدٍ", "barid", "«and a post-stage»", "«ve berîd»", punct="،"),
 ]})
# ----------- s5 — the exceptions
S.append({"id": "s5", "translation": {"en": "except جَانِبًا, وَجْهًا, وَسَطًا with a fatḥa on the sīn, خَارِجَ الدَّارِ, دَاخِلَ الدَّارِ and جَوْفَ الْبَيْتِ, and every place-noun that does not mean resting — as in «the killing-place» and «the striking-place» — and likewise if it means that but what it hangs on does not — as in مَقَام and مَكَان,", "tr": "cânib, vech, sin'i fethalı vasat, hâricü'd-dâr, dâhilü'd-dâr ve cevfü'l-beyt hâriç; bir de istikrâr mânâsında olmayan her mekân ismi — «maktel», «madrab» gibi — ve bu mânâda olup da müteallakı bu mânâda olmayan — «makam», «mekân» gibi;"},
 "tokens": [
  tok("إِلَّا", "illa", "part", [K, IS], "حَرْفُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  mansub_item("جَانِبًا", "janib", "«the side»", "«cânib»", ar="مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ."),
  mansub_item("وَوَجْهًا", "wajh", "«the face»", "«vech»"),
  mansub_item("وَوَسَطًا", "wasat", "«the middle»", "«vasat»"),
  tok("بِفَتْحِ", "fath", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَفَتْحِ مَجْرُورٌ، مُضَافٌ — حَالٌ.", "«with a fatḥa on»", "«fethasıyla»", segments=[seg("بِ", "bi", "prep"), seg("فَتْحِ", "fath", "noun")]),
  tok("السِّينِ", "sin-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sīn»", "«sin'in»"),
  mansub_item("وَخَارِجَ", "kharij", "«outside of»", "«hârici»", ar="مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", tags=[ID]),
  tok("الدَّارِ", "dar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the house»", "«evin»"),
  mansub_item("وَدَاخِلَ", "dakhil", "«inside of»", "«dâhili»", ar="مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", tags=[ID]),
  tok("الدَّارِ", "dar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the house»", "«evin»"),
  mansub_item("وَجَوْفَ", "jawf", "«the inside of»", "«cevfi»", ar="مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", tags=[ID]),
  tok("الْبَيْتِ", "bayt", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the house»", "«evin»", punct="،"),
  tok("وَكُلَّ", "kull", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلَّ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and every» — joined, annexed.", "«ve her» — ma'tûf, muzâf.", segments=wa("كُلَّ", "kull", "noun")),
  tok("اسْمِ", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«noun of»", "«ismi»"),
  tok("مَكَانٍ", "makan", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«place»", "«mekân»"),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya", "jumla-sifa"], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ بَعْدَهُ صِفَةٌ لِاسْمِ مَكَانٍ.", "«not» — the clause is the ṣifa.", "«değil» — cümle sıfat."),
  tok("يَكُونُ", "kana", "verb", [K, KN, "jumla-sifa"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«is» — kāna, its ism concealed.", "«olmaz» — nâkıs, ismi müstetir."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, KN, ID, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُ.", "«in the sense of» — kāna's khabar.", "«mânâsında» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الِاسْتِقْرَارِ", "istiqrar", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«resting»", "«istikrâr»"),
  nahw(),
  tok("الْمَقْتَلِ", "maqtal", "noun", [K, MK, HT, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَفْظٌ مَحْكِيٌّ.", "«the killing-place» — annexed to نَحْوُ.", "«maktel» — nahvü'ye muzâfun ileyh."),
  majrur_item("وَالْمَضْرَبِ", "madrab", "«and the striking-place»", "«ve madrab»", punct="،"),
  tok("وَكَذَا", "kadha", "part", [K, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَالْأَمْرُ كَذَا.", "«and likewise»", "«ve böyle»", segments=wa("كَذَا", "kadha", "part")),
  *in_kana(),
  tok("بِمَعْنَاهُ", "mana", "noun", [K, HJ, KN, ID, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرُ كَانَ.", "«in its sense» — kāna's khabar.", "«onun mânâsında» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  tok("وَلَمْ", "lam", "part", [K, AT, "lam-jazim"], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ.", "«and not»", "«ve -medi»", segments=wa("لَمْ", "lam", "part")),
  tok("يَكُنْ", "kana", "verb", [K, KN, "lam-jazim"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ.", "«is not» — majzūm.", "«olmadı» — meczûm."),
  tok("مُتَعَلَّقُهُ", "mutaallaq", "noun", [K, KN, ID, "ism-maful"], "اسْمُ يَكُنْ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what it hangs on» — kāna's ism.", "«müteallakı» — kâne'nin ismi.", segments=[seg("مُتَعَلَّقُ", "mutaallaq", "noun"), pr3ms()]),
  tok("بِمَعْنَاهُ", "mana", "noun", [K, HJ, KN, ID, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَا مَجْرُورٌ تَقْدِيرًا، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرُ يَكُنْ.", "«in its sense» — the khabar.", "«onun mânâsında» — haber.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  nahw(),
  tok("مَقَامٍ", "maqam", "noun", [K, MK, HT, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَفْظٌ مَحْكِيٌّ.", "«maqām» — annexed to نَحْوُ.", "«makam» — muzâfun ileyh."),
  majrur_item("وَمَكَانٍ", "makan", "«and makān»", "«ve mekân»", punct="،"),
 ]})
# ----------- s6 — these exceptions: no omission; not «I was the side of the house»
S.append({"id": "s6", "translation": {"en": "for from these exceptions فِي may not be omitted: one does not say «I was side the house», or «striking-place Zayd», or «a station», but «in the side of the house», «in Zayd's striking-place», «in a station».", "tr": "zira bu müstesnâlardan fî hazfedilemez: «evin yanı oldum», «Zeyd'in madrabı», «bir makam» denmez; «evin yanında», «Zeyd'in madrabında», «bir makamda» denir."},
 "tokens": [
  tok("فَإِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for» — inna.", "«zira» — inne.", segments=fa("إِنَّ", "inna", "part")),
  tok("هٰذِهِ", "hadhihi", "pron", [K, "inna-wa-akhawatuha", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«these» — inna's ism.", "«bu» — inne'nin ismi."),
  tok("الْمُسْتَثْنَيَاتِ", "mustathna", "noun", [K, "badal", IS, "jam-muannath-salim"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«exceptions» — the badal, naṣb by the kasra.", "«müstesnâlar» — bedel, kesre ile mansûb."),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«not»", "«değil»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, "inna-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«is permitted» — the clause is inna's khabar.", "«câiz olmaz» — cümle inne'nin haberi."),
  hadhf_fi(ar="فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en="«omitting» — the doer, annexed.", tr="«hazfi» — fâil, muzâf."),
  fi_q(),
  tok("مِنْهَا", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«from them»", "«onlardan»", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«not»", "«değil»"),
  tok("يُقَالُ", "qala", "verb", [K, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«one says» — the passive; the quoted sentence is its deputy.", "«denmez» — meçhul; hikâye edilen cümle nâib-i fâil.", punct=":"),
  tok("كُنْتُ", "kana", "verb", [K, KN, HT], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ.", "«I was»", "«oldum»", segments=[seg("كُنْ", "kana", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("جَانِبَ", "janib", "noun", [K, KN, ID, HT], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ — ظَرْفٌ مُمْتَنِعٌ بِلَا فِي.", "«side of» — kāna's khabar, the ẓarf that may not drop فِي.", "«yanı» — kâne'nin haberi; fî'siz câiz olmayan zarf."),
  tok("الدَّارِ", "dar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the house»", "«evin»"),
  aw(),
  tok("مَضْرَبَ", "madrab", "noun", [K, AT, ID], "مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«striking-place of»", "«madrabı»"),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»"),
  aw(),
  tok("مَقَامًا", "maqam", "noun", [K, AT], "مَعْطُوفٌ مَنْصُوبٌ.", "«a station»", "«bir makam»", punct="،"),
  tok("بَلْ", "bal", "part", [K, "atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«but rather»", "«bilakis»", punct=":"),
  fi(tags=[HT]),
  tok("جَانِبِ", "janib", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the side of»", "«yanında»"),
  tok("الدَّارِ", "dar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the house»", "«evin»"),
  aw(),
  fi(),
  tok("مَضْرَبِ", "madrab", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the striking-place of»", "«madrabında»"),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»"),
  aw(),
  fi(),
  tok("مَقَامٍ", "maqam", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«a station»", "«bir makamda»", punct="."),
 ]})
# ----------- s7 — but if the governor of the last kind means resting
S.append({"id": "s7", "translation": {"en": "But if the governor of the last kind means resting, omitting فِي is permitted — as in «I stood in his place» and «I sat in his seat».", "tr": "Son kısmın âmili istikrâr mânâsında ise fî'nin hazfi câizdir — «onun makamına durdum», «onun yerine oturdum» gibi."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, "amma-tafsiliyya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«but as for» — ammā.", "«ama» — tafsîl edatı.", segments=wa("أَمَّا", "amma", "part")),
  *in_kana(),
  tok("عَامِلُ", "amil", "noun", [K, KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ.", "«the governor of» — kāna's ism.", "«âmili» — kâne'nin ismi."),
  tok("الْقِسْمِ", "qism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the kind»", "«kısmın»"),
  tok("الْأَخِيرِ", "akhir-last", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«last» — the naʿt.", "«son» — sıfat."),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, KN, ID, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ تَقْدِيرًا، مُضَافٌ — خَبَرُ كَانَ.", "«in the sense of» — kāna's khabar.", "«mânâsında» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("الِاسْتِقْرَارِ", "istiqrar", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«resting»", "«istikrâr»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, SH, "amma-tafsiliyya", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — جَوَابُ أَمَّا وَإِنْ، وَالْفَاءُ مَحْذُوفَةٌ كَمَا فِي الْمَطْبُوعِ.", "«is permitted» — the jawāb of ammā and in (the fāʾ dropped, as the print has it).", "«câizdir» — emmâ ve in'in cevabı (fâ, matbûda olduğu gibi hazfedilmiş)."),
  hadhf_fi(ar="فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en="«omitting» — the doer, annexed.", tr="«hazfi» — fâil, muzâf."),
  fi_q(punct="،"),
  nahw(),
  tok("قُمْتُ", "qama", "verb", [K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالتَّاءُ فَاعِلٌ.", "«I stood»", "«durdum»", segments=[seg("قُمْ", "qama", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مَقَامَهُ", "maqam", "noun", [K, MF, ID, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — حُذِفَتْ فِي لِأَنَّ الْعَامِلَ بِمَعْنَى الِاسْتِقْرَارِ.", "«in his place» — the mafʿūl fīh, فِي omitted.", "«onun makamına» — mef'ûlün fîh, fî hazfedilmiş.", segments=[seg("مَقَامَ", "maqam", "noun"), pr3ms()]),
  tok("وَقَعَدْتُ", "qaada", "verb", [K, AT, "fail"], "الْوَاوُ عَاطِفَةٌ، وَقَعَدْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I sat»", "«ve oturdum»", segments=[seg("وَ", "wa", "conj"), seg("قَعَدْ", "qaada", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مَكَانَهُ", "makan", "noun", [K, MF, ID, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in his seat»", "«onun yerine»", punct=".", segments=[seg("مَكَانَ", "makan", "noun"), pr3ms()]),
 ]})
# ----------- s8 — the bounded place zarf: no omission
S.append({"id": "s8", "translation": {"en": "And if it is a bounded ẓarf of place — which is what has a name of its own by reason of something within what it names, like the house and the home — فِي may not be omitted;", "tr": "Mahdûd bir mekân zarfı ise — ki o, müsemmâsının içindeki bir husus sebebiyle kendine bir isim sâbit olandır; dâr ve beyt gibi — fî hazfedilemez;"},
 "tokens": [
  *in_kana("وَإِنْ", pre_ar="الْوَاوُ عَاطِفَةٌ، وَ"),
  *zarf_x("مَكَانٍ", "makan", "«place»", "«mekân»"),
  tok("مَحْدُودًا", "mahdud", "noun", [K, NA, "ism-maful"], "نَعْتٌ لِظَرْفَ مَنْصُوبٌ.", "«bounded» — the naʿt.", "«mahdûd» — sıfat.", punct="،"),
  *ma_lam_yathbut(neg=False),
  tok("كَالدَّارِ", "dar", "noun", [K, HJ, MK], "الْكَافُ حَرْفُ جَرٍّ، وَالدَّارِ مَجْرُورٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«like the house»", "«ev gibi»", segments=[seg("كَ", "ka", "prep"), seg("الدَّارِ", "dar", "noun")]),
  majrur_item("وَالْبَيْتِ", "bayt", "«and the home»", "«ve hâne»", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, SH, "la-nafiya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَلَا نَافِيَةٌ.", "«then not» — the fāʾ of the jawāb.", "«o halde … -mez» — cevap fâsı.", segments=fa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, SH, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«is permitted» — the jawāb clause.", "«câiz olmaz» — cevap cümlesi."),
  hadhf_fi(ar="فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en="«omitting» — the doer, annexed.", tr="«hazfi» — fâil, muzâf."),
  fi_q(punct="،"),
 ]})
# ----------- s9 — not «I prayed a house», except after دخل، نزل، سكن
S.append({"id": "s9", "translation": {"en": "so one does not say «I prayed a house» but «in a house» — except with what follows دَخَلَ, نَزَلَ and سَكَنَ, as in «I entered the house», «I put up at the inn», «I settled in the town».", "tr": "«bir ev namaz kıldım» denmez, «bir evde» denir — dehale, nezele ve sekene'den sonrakiler hâriç: «eve girdim», «hana indim», «beldede oturdum» gibi."},
 "tokens": [
  tok("فَلَا", "la-nafiya", "part", [K, "la-nafiya"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not»", "«dolayısıyla … -mez»", segments=fa("لَا", "la-nafiya", "part")),
  tok("يُقَالُ", "qala", "verb", [K, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«one says» — the passive.", "«denmez» — meçhul.", punct=":"),
  tok("صَلَّيْتُ", "salla", "verb", [K, "fail", "naqis-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ فَاعِلٌ.", "«I prayed»", "«namaz kıldım»", segments=[seg("صَلَّيْ", "salla", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("دَارًا", "dar", "noun", [K, MF, HT], "مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ — وَهُوَ مُمْتَنِعٌ، لِأَنَّهُ ظَرْفُ مَكَانٍ مَحْدُودٌ.", "«a house» — the ẓarf the rule forbids.", "«bir ev» — câiz olmayan zarf."),
  tok("بَلْ", "bal", "part", [K, "atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«but»", "«bilakis»"),
  fi(tags=[HT]),
  tok("دَارٍ", "dar", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«a house»", "«bir evde»", punct="،"),
  tok("إِلَّا", "illa", "part", [K, IS], "حَرْفُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  tok("مَعَ", "maa", "noun", [K, MF, IS, ID], "ظَرْفٌ مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ، مُضَافٌ.", "«with» — the ẓarf, the mustathnā.", "«ile» — müstesnâ zarf."),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", ID], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the relative, annexed.", "«… olan» — muzâfun ileyh."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID, "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — صِلَةُ مَا.", "«after» — the ṣila.", "«sonrası» — sıla."),
  quoted("دَخَلَ", "dakhala", "verb", "«entered»", "«girdi»", "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "annexed to بَعْدَ", "muzâfun ileyh", joined=False),
  quoted("وَنَزَلَ", "nazala", "verb", "«and put up»", "«ve indi»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde"),
  quoted("وَسَكَنَ", "sakana", "verb", "«and settled»", "«ve oturdu»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", punct="،"),
  nahw(),
  tok("دَخَلْتُ", "dakhala", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I entered»", "«girdim»", segments=[seg("دَخَلْ", "dakhala", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("الدَّارَ", "dar", "noun", [K, MF, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — حُذِفَتْ فِي بَعْدَ دَخَلَ.", "«the house» — the ẓarf after دَخَلَ, فِي omitted.", "«eve» — dehale'den sonra fî hazfedilmiş."),
  tok("وَنَزَلْتُ", "nazala", "verb", [K, AT, "fail"], "الْوَاوُ عَاطِفَةٌ، وَنَزَلْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I put up»", "«ve indim»", segments=[seg("وَ", "wa", "conj"), seg("نَزَلْ", "nazala", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("الْخَانَ", "khan-inn", "noun", [K, MF, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ.", "«the inn»", "«hana»"),
  tok("وَسَكَنْتُ", "sakana", "verb", [K, AT, "fail"], "الْوَاوُ عَاطِفَةٌ، وَسَكَنْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I settled»", "«ve oturdum»", segments=[seg("وَ", "wa", "conj"), seg("سَكَنْ", "sakana", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("الْبَلَدَ", "balad", "noun", [K, MF, HT], "مَفْعُولٌ فِيهِ مَنْصُوبٌ.", "«the town»", "«beldede»", punct="."),
 ]})
# ----------- s10 — the second: the maf'ul lah
S.append({"id": "s10", "translation": {"en": "The second is the mafʿūl lah, when it is an act of the doer of the verb it explains and concurrent with it in existence — as in «I struck Zayd as a correction» — unlike «I honoured you for your honouring me» and «I came to you today for yesterday's promise».", "tr": "İkincisi mef'ûlün lehtir: ta'lil edilen fiilin fâilinin fiili ve varlıkta ona mukârin olduğunda — «Zeyd'i te'dib için dövdüm» gibi; «seni ikramın için ağırladım», «dünkü vaat için bugün sana geldim»'in aksine."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, MK, "ism-maqsur-manqus"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second» — the mubtada, a manqūṣ.", "«ikincisi» — mübtedâ, mankûs.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("الْمَفْعُولُ", "maful-noun", "noun", [K, MK, ML, "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«the mafʿūl» — the khabar.", "«mef'ûl» — haber."),
  tok("لَهُ", "li", "prep", [K, HJ, ML], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ: الْمَفْعُولُ لَهُ.", "«lah» — the second half of the term.", "«leh» — terimin ikinci yarısı.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… olduğunda»"),
  tok("كَانَ", "kana", "verb", [K, KN, "idha-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is» — kāna, its ism concealed.", "«olduğunda» — ismi müstetir."),
  tok("فِعْلًا", "fil", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«an act» — kāna's khabar.", "«bir fiil» — kâne'nin haberi."),
  tok("لِفَاعِلِ", "fail-doer", "noun", [K, HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَفَاعِلِ مَجْرُورٌ، مُضَافٌ.", "«of the doer of»", "«fâilinin»", segments=[seg("لِ", "li", "prep"), seg("فَاعِلِ", "fail-doer", "noun")]),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiilin»"),
  tok("الْمُعَلَّلِ", "muallal", "noun", [K, NA, "ism-maful"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ.", "«explained» — the naʿt.", "«ta'lil edilen» — sıfat."),
  tok("وَمُقَارِنًا", "muqarin", "noun", [K, AT, KN, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَمُقَارِنًا مَعْطُوفٌ عَلَى فِعْلًا مَنْصُوبٌ.", "«and concurrent» — joined to the khabar.", "«ve mukârin» — habere ma'tûf.", segments=wa("مُقَارِنًا", "muqarin", "noun")),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«with it»", "«ona»", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  fi(),
  tok("الْوُجُودِ", "wujud", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«existence»", "«varlıkta»", punct="،"),
  nahw(),
  tok("ضَرَبْتُ", "daraba", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("زَيْدًا", "zayd", "propn", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd»", "«Zeyd'i»"),
  tok("تَأْدِيبًا", "tadib", "noun", [K, ML, HT, "masdar"], "مَفْعُولٌ لَهُ مَنْصُوبٌ — حُذِفَتِ اللَّامُ لِأَنَّهُ فِعْلُ الْفَاعِلِ وَمُقَارِنٌ.", "«as a correction» — the mafʿūl lah, the lām omitted.", "«te'dib için» — mef'ûlün leh, lâm hazfedilmiş.", punct="،"),
  tok("بِخِلَافِ", "khilaf", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِ مَجْرُورٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«unlike»", "«… -in aksine»", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun")]),
  tok("أَكْرَمْتُكَ", "akrama", "verb", [K, "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — جُمْلَةٌ فِي مَحَلِّ جَرٍّ.", "«I honoured you»", "«seni ağırladım»", segments=[seg("أَكْرَمْ", "akrama", "verb"), seg("تُ", "pron-1s", "pron"), seg("كَ", "pron-2ms", "pron")]),
  tok("لِإِكْرَامِكَ", "ikram", "noun", [K, HJ, ML, ID, "masdar"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَإِكْرَامِ مَجْرُورٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — لَا يُحْذَفُ الْجَارُّ لِأَنَّ الْفَاعِلَ مُخْتَلِفٌ.", "«for your honouring» — the lām stays: another doer.", "«ikramın için» — lâm kalır: fâil farklı.", segments=[seg("لِ", "li", "prep"), seg("إِكْرَامِ", "ikram", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَجِئْتُكَ", "jaa", "verb", [K, AT, "fail", "maful-bihi", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَجِئْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«and I came to you»", "«ve sana geldim»", segments=[seg("وَ", "wa", "conj"), seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("كَ", "pron-2ms", "pron")]),
  tok("الْيَوْمَ", "yawm", "noun", [K, MF], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفُ زَمَانٍ.", "«today» — the ẓarf.", "«bugün» — zaman zarfı."),
  tok("لِوَعْدِ", "wad", "noun", [K, HJ, ML, ID], "اللَّامُ لِلتَّعْلِيلِ، وَوَعْدِ مَجْرُورٌ، مُضَافٌ — لَا يُحْذَفُ لِعَدَمِ الْمُقَارَنَةِ.", "«for the promise of» — the lām stays: not concurrent.", "«vaadi için» — lâm kalır: mukârenet yok.", segments=[seg("لِ", "li", "prep"), seg("وَعْدِ", "wad", "noun")]),
  tok("أَمْسِ", "ams", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ.", "«yesterday» — built on the kasra.", "«dünün» — kesre üzere mebnî.", punct="."),
 ]})
# ----------- s11 — in these two places the majrur takes nasb, or raf if a deputy
S.append({"id": "s11", "translation": {"en": "And in these two places, when the letter is omitted the majrūr takes naṣb if it is not the deputy of the doer, and rafʿ if it is the deputy — by agreement.", "tr": "Bu iki yerde câr hazfedildiğinde mecrûr, nâib-i fâil değilse nasb alır; nâib ise ittifakla ref' alır."},
 "tokens": [
  tok("وَفِي", "fi", "prep", [K, HJ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفِي حَرْفُ جَرٍّ.", "«and in»", "«ve -de»", segments=wa("فِي", "fi", "prep")),
  tok("هٰذَيْنِ", "hadhani", "pron", [K, HJ, "asma-al-ishara", "al-muthanna"], "اسْمُ إِشَارَةٍ لِلْمُثَنَّى مَجْرُورٌ بِالْيَاءِ.", "«these two» — the dual demonstrative, jarr by the yāʾ.", "«bu iki» — tesniye işaret ismi, yâ ile mecrûr."),
  tok("الْمَوْضِعَيْنِ", "mawdi", "noun", [K, "badal", "al-muthanna"], "بَدَلٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«places» — the badal, dual.", "«yerde» — bedel, tesniye."),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… -dığında»"),
  tok("حُذِفَ", "hadhafa", "verb", [K, "naib-al-fail", "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«is omitted» — the passive, the shart.", "«hazfedildiğinde» — meçhul, şart fiili."),
  tok("الْجَارُّ", "jarr-letter", "noun", [K, "naib-al-fail"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«the letter» — the deputy.", "«câr» — nâib-i fâil."),
  tok("يَنْتَصِبُ", "intasaba", "verb", [K, "idha-shartiyya", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — جَوَابُ إِذَا.", "«takes naṣb» — the jawāb.", "«nasb alır» — cevap."),
  tok("الْمَجْرُورُ", "majrur-noun", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the majrūr» — the doer.", "«mecrûr» — fâil."),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not»", "«-mezse»"),
  tok("يَكُنْ", "kana", "verb", [K, KN, SH], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is» — majzūm, the shart.", "«değilse» — meczûm şart fiili."),
  tok("نَائِبَ", "naib", "noun", [K, KN, ID], "خَبَرُ يَكُنْ مَنْصُوبٌ، مُضَافٌ.", "«the deputy of» — kāna's khabar.", "«nâibi» — kâne'nin haberi."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâilin»", punct="،"),
  tok("وَيُرْفَعُ", "rafaa", "verb", [K, AT, "naib-al-fail"], "الْوَاوُ عَاطِفَةٌ، وَيُرْفَعُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«and it takes rafʿ» — the passive.", "«ve ref' alır» — meçhul.", segments=wa("يُرْفَعُ", "rafaa", "verb")),
  tok("إِنْ", "in-shartiyya", "part", [K, SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("كَانَ", "kana", "verb", [K, KN, SH], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is» — the shart.", "«ise» — şart fiili."),
  tok("نَائِبًا", "naib", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a deputy» — kāna's khabar.", "«nâib» — kâne'nin haberi."),
  tok("بِالِاتِّفَاقِ", "ittifaq", "noun", [K, HJ, "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَالِاتِّفَاقِ مَجْرُورٌ — حَالٌ.", "«by agreement»", "«ittifakla»", punct=".", segments=[seg("بِ", "bi", "prep"), seg("الِاتِّفَاقِ", "ittifaq", "noun")]),
 ]})
# ----------- s12 — the third: أن and أنّ
S.append({"id": "s12", "translation": {"en": "The third is أَنْ and أَنَّ: the letter is omitted from them by rule — as in His word, Exalted is He, «He frowned and turned away, that the blind man came to him» (80:1–2), that is: because he came to him.", "tr": "Üçüncüsü en ve enne'dir: câr bunlardan kıyasla hazfedilir — Allah Teâlâ'nın «Yüzünü ekşitti ve döndü, kendisine âmâ geldi diye» (80:1-2) sözü gibi; yani: geldiği için."},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the third» — the mubtada.", "«üçüncüsü» — mübtedâ.", segments=wa("الثَّالِثُ", "thalith", "noun")),
  q_raf("أَنْ", "an-masdariyya", "«an»", "«en»", joined=False, extra=["an-masdariyya"]),
  q_raf("وَأَنَّ", "anna", "«and anna»", "«ve enne»", punct="،", extra=["inna-wa-akhawatuha"]),
  tok("فَالْجَارُّ", "jarr-letter", "noun", [K, MK], "الْفَاءُ لِلتَّفْرِيعِ، وَالْجَارُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«the letter» — the mubtada.", "«câr» — mübtedâ.", segments=fa("الْجَارُّ", "jarr-letter", "noun")),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, "naib-al-fail", MK], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«is omitted» — the clause is the khabar.", "«hazfedilir» — cümle haber."),
  tok("مِنْهُمَا", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَهُمَا فِي مَحَلِّ جَرٍّ.", "«from them both»", "«ikisinden»", segments=[seg("مِنْ", "min", "prep"), seg("هُمَا", "pron-3d", "pron")]),
  tok("قِيَاسًا", "qiyas", "noun", [K, "hal", "masdar"], "حَالٌ مَنْصُوبٌ — أَيْ مَقِيسًا.", "«by rule» — the ḥāl.", "«kıyasla» — hâl.", punct="،"),
  *cite_quran(),
  tok("عَبَسَ", "abasa", "verb", [K, IQ, "fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he frowned»", "«yüzünü ekşitti»"),
  tok("وَتَوَلَّى", "tawalla", "verb", [K, IQ, AT, "ism-maqsur-manqus", "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَوَلَّى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and turned away»", "«ve döndü»", segments=wa("تَوَلَّى", "tawalla", "verb")),
  tok("أَنْ", "an-masdariyya", "part", [K, IQ, "an-masdariyya", HT], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — حُذِفَ الْجَارُّ قَبْلَهُ: لِأَنْ.", "«that» — the jarr letter before it omitted.", "«diye» — câr önünden hazfedilmiş."),
  tok("جَاءَهُ", "jaa", "verb", [K, IQ, "an-masdariyya", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْحَرْفِ الْمَحْذُوفِ.", "«came to him» — the clause in the place of jarr by the omitted letter.", "«ona geldi» — mahzûf harfle cer mahallinde.", segments=[seg("جَاءَ", "jaa", "verb"), pr3ms()]),
  tok("الْأَعْمَى", "ama-blind", "noun", [K, IQ, "fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the blind man» — the doer.", "«âmâ» — fâil.", punct="،"),
  ay(),
  tok("لِأَنْ", "an-masdariyya", "part", [K, HJ, "an-masdariyya", HT], "اللَّامُ حَرْفُ جَرٍّ — الْمُقَدَّرُ — وَأَنْ حَرْفٌ مَصْدَرِيٌّ.", "«because» — the estimated lām.", "«-diği için» — takdir edilen lâm.", segments=[seg("لِ", "li", "prep"), seg("أَنْ", "an-masdariyya", "part")]),
  tok("جَاءَهُ", "jaa", "verb", [K, "an-masdariyya", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«he came to him»", "«ona geldi»", punct=".", segments=[seg("جَاءَ", "jaa", "verb"), pr3ms()]),
 ]})
# ----------- s13 — the sama'i
S.append({"id": "s13", "translation": {"en": "And the one by hearing is in whatever is other than these three: what is heard from the Arabs is kept and not reasoned from.", "tr": "Semâî olan, bu üçünün dışındakilerdedir: Araplardan işitilen ezberlenir, ona kıyas yapılmaz."},
 "tokens": [
  tok("وَالسَّمَاعِيُّ", "samai", "noun", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالسَّمَاعِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«the one by hearing» — the mubtada.", "«semâî olan» — mübtedâ.", segments=wa("السَّمَاعِيُّ", "samai", "noun")),
  tok("فِيمَا", "ma-mawsula", "pron", [K, HJ, "ism-mawsul", MK], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in what» — the phrase is the khabar.", "«… olanlardadır» — câr-mecrûr haber.", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("عَدَا", "ada-except", "verb", [K, IS, "ism-mawsul"], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةُ مَا.", "«is other than» — the exceptive verb, the ṣila.", "«dışında olan» — istisnâ fiili, sıla."),
  tok("هٰذِهِ", "hadhihi", "pron", [K, "asma-al-ishara", "maful-bihi"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«these» — the object.", "«bu» — mef'ûl."),
  tok("الثَّلَاثَةَ", "thalatha", "noun", [K, "badal"], "بَدَلٌ مَنْصُوبٌ.", "«three» — the badal.", "«üçünün» — bedel.", punct="،"),
  tok("فَمَا", "ma-mawsula", "pron", [K, MK, "ism-mawsul"], "الْفَاءُ لِلتَّفْرِيعِ، وَمَا اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«so what» — the mubtada.", "«ne ki» — mübtedâ.", segments=fa("مَا", "ma-mawsula", "pron")),
  tok("سُمِعَ", "samia", "verb", [K, "naib-al-fail", "ism-mawsul"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةٌ.", "«is heard» — the ṣila.", "«işitildi» — sıla."),
  tok("مِنَ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  tok("الْعَرَبِ", "arab", "noun", [K, HJ], "مَجْرُورٌ بِمِنْ.", "«the Arabs»", "«Araplardan»"),
  tok("فَيُحْفَظُ", "hafiza", "verb", [K, MK, "naib-al-fail", "fa-khabar-mubtada"], "الْفَاءُ زَائِدَةٌ فِي الْخَبَرِ لِتَضَمُّنِ الْمُبْتَدَإِ مَعْنَى الشَّرْطِ، وَيُحْفَظُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — خَبَرٌ.", "«is kept» — the khabar with the fāʾ of the shart-like mubtada.", "«ezberlenir» — haber; mübtedâ şart mânâsında olduğu için fâ.", segments=fa("يُحْفَظُ", "hafiza", "verb")),
  tok("وَلَا", "la-nafiya", "part", [K, AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يُقَاسُ", "qasa", "verb", [K, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«is reasoned» — the passive; the phrase after it is the deputy.", "«kıyas yapılmaz» — meçhul; câr-mecrûr nâib.", ),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ, "naib-al-fail"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — نَائِبُ الْفَاعِلِ.", "«on it» — the deputy.", "«ona» — nâib-i fâil.", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
 ]})
# ----------- s14 — hadhf wa isal
S.append({"id": "s14", "translation": {"en": "Then the rule after the omission, in other than the first two, is that you connect what the phrase hung on to the majrūr, so the iʿrāb of place surfaces — naṣb as an object or rafʿ as a deputy — and it is called omission-and-connection,", "tr": "Sonra ilk ikisi dışında hazften sonraki kaide, müteallakı mecrûra ulaştırmandır; böylece mahallî i'rab ortaya çıkar — mef'ûliyyet üzere nasb yahut nâibiyyet üzere ref' — ve buna hazf ve îsâl denir;"},
 "tokens": [
  tok("ثُمَّ", "thumma", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — اسْتِئْنَافِيَّةٌ هُنَا.", "«then»", "«sonra»"),
  tok("الْقِيَاسُ", "qiyas", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the rule» — the mubtada.", "«kaide» — mübtedâ."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("الْحَذْفِ", "hadhf", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the omission»", "«hazften»"),
  fi(),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("الْأَوَّلَيْنِ", "awwal", "noun", [K, ID, "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«the first two» — jarr by the yāʾ.", "«ilk ikisinin» — yâ ile mecrûr."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", MK], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-man» — masdar-ı müevvel haber."),
  tok("تُوصِلَ", "awsala", "verb", [K, "an-masdariyya", "form-iv-verbs", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«you connect» — manṣūb by أَنْ.", "«ulaştırman» — en ile mansûb."),
  tok("مُتَعَلَّقَهُ", "mutaallaq", "noun", [K, "maful-bihi", ID, "ism-maful"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what it hung on» — the object.", "«müteallakını» — mef'ûl.", segments=[seg("مُتَعَلَّقَ", "mutaallaq", "noun"), pr3ms()]),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْمَجْرُورِ", "majrur-noun", "noun", [K, HJ], "مَجْرُورٌ بِإِلَى.", "«the majrūr»", "«mecrûra»"),
  tok("فَيَظْهَرَ", "zahara", "verb", [K, AT, "an-masdariyya", "fa-khabar-mubtada"], "الْفَاءُ لِلسَّبَبِيَّةِ عَاطِفَةٌ، وَيَظْهَرَ مَنْصُوبٌ عَطْفًا عَلَى تُوصِلَ.", "«so that there surfaces» — manṣūb by joining.", "«ve ortaya çıksın» — atıfla mansûb.", segments=fa("يَظْهَرَ", "zahara", "verb")),
  tok("الْإِعْرَابُ", "irab", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the iʿrāb» — the doer.", "«i'rab» — fâil."),
  tok("الْمَحَلِّيُّ", "mahalli", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى الْمَحَلِّ.", "«of place» — the naʿt.", "«mahallî» — sıfat.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("النَّصْبُ", "nasb", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«naṣb» — the khabar.", "«nasb» — haber."),
  ala(),
  tok("الْمَفْعُولِيَّةِ", "mafuliyya", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«objecthood»", "«mef'ûliyyet»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«yahut»"),
  tok("الرَّفْعُ", "raf", "noun", [K, AT], "مَعْطُوفٌ مَرْفُوعٌ.", "«rafʿ»", "«ref'»"),
  ala(),
  tok("النَّائِبِيَّةِ", "naibiyya", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«deputyhood»", "«nâibiyyet»", punct="،"),
  tok("وَيُسَمَّى", "samma", "verb", [K, AT, "naib-al-fail", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is called» — the passive, its deputy concealed.", "«ve … denir» — meçhul.", segments=wa("يُسَمَّى", "samma", "verb")),
  tok("حَذْفًا", "hadhf", "noun", [K, "mafulayn", "masdar"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«omission» — the second object.", "«hazf» — ikinci mef'ûl."),
  tok("وَإِيصَالًا", "isal", "noun", [K, AT, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَإِيصَالًا مَعْطُوفٌ مَنْصُوبٌ.", "«and connection»", "«ve îsâl»", punct="،", segments=wa("إِيصَالًا", "isal", "noun")),
 ]})
# ----------- s15 — the examples: 7:155 and the sayings
S.append({"id": "s15", "translation": {"en": "as in His word, Exalted is He, «and Moses chose his people» (7:155), that is: from his people; and as in their saying «shared property» and «a settled ẓarf», that is: shared in and settled in.", "tr": "Allah Teâlâ'nın «Mûsâ kavmini seçti» (7:155) sözü gibi — yani kavminden; ve «ortak mal», «yerleşik zarf» sözleri gibi — yani içinde ortak olunan, içinde yerleşilen."},
 "tokens": [
  *cite_quran(),
  tok("وَاخْتَارَ", "ikhtara", "verb", [K, IQ, "form-viii-verbs", "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَاخْتَارَ فِعْلٌ مَاضٍ.", "«and chose»", "«ve seçti»", segments=wa("اخْتَارَ", "ikhtara", "verb")),
  tok("مُوسَى", "musa", "propn", [K, IQ, "fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«Moses» — the doer.", "«Mûsâ» — fâil."),
  tok("قَوْمَهُ", "qawm", "noun", [K, IQ, "maful-bihi", ID, HT], "مَفْعُولٌ بِهِ مَنْصُوبٌ عَلَى الْحَذْفِ وَالْإِيصَالِ — أَيْ مِنْ قَوْمِهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the object by omission-and-connection.", "«kavmini» — hazf ve îsâl ile mef'ûl.", punct="،", segments=[seg("قَوْمَ", "qawm", "noun"), pr3ms()]),
  ay(),
  tok("مِنْ", "min", "prep", [K, HJ, HT], "حَرْفُ جَرٍّ — الْمَحْذُوفُ.", "«from» — the omitted letter.", "«-den» — hazfedilen harf."),
  tok("قَوْمِهِ", "qawm", "noun", [K, HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavminden»", punct="،", segments=[seg("قَوْمِ", "qawm", "noun"), pr3msi()]),
  tok("وَنَحْوَ", "nahwa", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ — ظَرْفٌ.", "«and as in»", "«ve … gibi»", segments=wa("نَحْوَ", "nahwa", "noun")),
  tok("قَوْلِهِمْ", "qawl", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their saying»", "«sözleri»", punct=":", segments=[seg("قَوْلِ", "qawl", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("مَالٌ", "mal", "noun", [K, MK, HT], "مُبْتَدَأٌ مَرْفُوعٌ — فِي الْجُمْلَةِ الْمَحْكِيَّةِ.", "«property» — the mubtada of the quoted saying.", "«mal» — mübtedâ."),
  tok("مُشْتَرَكٌ", "mushtarak", "noun", [K, MK, HT, "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ، حُذِفَ جَارُّهُ.", "«shared» — the khabar, its letter omitted.", "«ortak» — haber."),
  tok("وَظَرْفٌ", "zarf", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَظَرْفٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and a ẓarf»", "«ve bir zarf»", segments=wa("ظَرْفٌ", "zarf", "noun")),
  tok("مُسْتَقِرٌّ", "mustaqarr", "noun", [K, MK, HT, "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«settled» — the khabar.", "«müstakar» — haber.", punct="،"),
  ay(),
  tok("مُشْتَرَكٌ", "mushtarak", "noun", [K, HT, "ism-maful"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَيْ هُوَ مُشْتَرَكٌ فِيهِ.", "«shared in»", "«içinde ortak olunan»"),
  tok("فِيهِ", "fi", "prep", [K, HJ, HT], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — نَائِبُ فَاعِلِ مُشْتَرَكٍ.", "«in it» — the deputy of the participle.", "«içinde» — nâib.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("وَمُسْتَقِرٌّ", "mustaqarr", "noun", [K, AT, HT, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَمُسْتَقِرٌّ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«and settled»", "«ve yerleşilen»", segments=wa("مُسْتَقِرٌّ", "mustaqarr", "noun")),
  tok("فِيهِ", "fi", "prep", [K, HJ, HT], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«in it»", "«içinde»", punct=".", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
 ]})
# ----------- s16 — the shadhdh: stays majrur
S.append({"id": "s16", "translation": {"en": "And it may stay majrūr, irregularly — as in «By God, I shall surely do it» (اللهِ لَأَفْعَلَنَّ), that is: by God (وَاللهِ).", "tr": "Şâz olarak mecrûr da kalabilir — «Allah'a yemin olsun, mutlaka yapacağım» (Allâhi le-ef'alenne) gibi; yani vallâhi."},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يَبْقَى", "baqiya", "verb", [K, KN, "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — أَيِ الْمَجْرُورُ.", "«it stays» — the sister of kāna, its ism concealed.", "«kalır» — kâne'nin kardeşi, ismi müstetir."),
  tok("مَجْرُورًا", "majrur-noun", "noun", [K, KN], "خَبَرُ يَبْقَى مَنْصُوبٌ.", "«majrūr» — the khabar.", "«mecrûr» — haber."),
  ala(),
  tok("الشُّذُوذِ", "shudhudh", "noun", [K, HJ, "masdar"], "مَجْرُورٌ بِعَلَى — حَالٌ: شَاذًّا.", "«irregularity» — as a ḥāl.", "«şâz olarak»", punct="،"),
  nahw(),
  tok("اللهِ", "allah", "propn", [K, HT, "anwa-al-waw"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِحَرْفِ الْقَسَمِ الْمَحْذُوفِ: وَاللهِ.", "«God» — majrūr by the omitted oath letter.", "«Allah» — mahzûf kasem harfiyle mecrûr."),
  tok("لَأَفْعَلَنَّ", "faala", "verb", [K, "nun-tawkid", "anwa-al-waw"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَأَفْعَلَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I shall surely do» — the oath's lām and the heavy nūn.", "«mutlaka yapacağım» — kasem lâmı ve tekid nûnu.", punct="،", segments=[seg("لَ", "lam-jawab", "part"), seg("أَفْعَلَنَّ", "faala", "verb")]),
  ay(),
  tok("وَاللهِ", "allah", "propn", [K, HJ, "anwa-al-waw"], "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by God» — the oath wāw.", "«vallâhi» — kasem vâvı.", punct=".", segments=[seg("وَ", "wa-qasam", "prep"), seg("اللهِ", "allah", "propn")]),
 ]})
# ----------- s17 — no two letters of one meaning on one verb
S.append({"id": "s17", "translation": {"en": "And two governing letters of one meaning may not hang on a single verb without conjunction: one does not say «I passed by Zayd by ʿAmr», nor «I struck on Friday on Saturday»,", "tr": "Bir mânâdaki iki câr harfi, atıf olmadan tek bir fiile bağlanamaz: «Zeyd'e Amr'a uğradım» denmez, «cuma günü cumartesi günü dövdüm» de denmez;"},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, "la-nafiya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is permitted»", "«câiz olmaz»"),
  tok("تَعَلُّقُ", "taalluq", "noun", [K, "fail", ID, "masdar"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the hanging of» — the doer.", "«taalluku» — fâil."),
  tok("الْجَارَّيْنِ", "jarr-letter", "noun", [K, ID, "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two letters» — dual.", "«iki cârın» — tesniye."),
  tok("بِمَعْنًى", "mana", "noun", [K, HJ, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنًى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — صِفَةٌ لِلْجَارَّيْنِ.", "«of a meaning»", "«bir mânâda»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنًى", "mana", "noun")]),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«one» — the naʿt.", "«tek» — sıfat."),
  tok("بِدُونِ", "duna", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَدُونِ مَجْرُورٌ، مُضَافٌ.", "«without»", "«olmaksızın»", segments=[seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun")]),
  tok("الْعَطْفِ", "atf", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«conjunction»", "«atıf»"),
  tok("بِفِعْلٍ", "fil", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَفِعْلٍ مَجْرُورٌ — مُتَعَلِّقٌ بِتَعَلُّقُ.", "«on a verb»", "«bir fiile»", segments=[seg("بِ", "bi", "prep"), seg("فِعْلٍ", "fil", "noun")]),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«single»", "«tek»", punct="،"),
  tok("فَلَا", "la-nafiya", "part", [K, "la-nafiya"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not»", "«dolayısıyla … -mez»", segments=fa("لَا", "la-nafiya", "part")),
  tok("يُقَالُ", "qala", "verb", [K, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«one says»", "«denmez»", punct=":"),
  tok("مَرَرْتُ", "marra", "verb", [K, "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ مُضَاعَفٌ فُكَّ إِدْغَامُهُ، وَالتَّاءُ فَاعِلٌ.", "«I passed»", "«uğradım»", segments=[seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("بِزَيْدٍ", "zayd", "propn", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ.", "«by Zayd»", "«Zeyd'e»", segments=[seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
  tok("بِعَمْرٍو", "amr-name", "propn", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَعَمْرٍو مَجْرُورٌ — وَهُوَ الْمُمْتَنِعُ: بَاءَانِ بِمَعْنًى وَاحِدٍ.", "«by ʿAmr» — the forbidden second letter.", "«Amr'a» — câiz olmayan ikinci harf.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("عَمْرٍو", "amr-name", "propn")]),
  tok("وَلَا", "la-nafiya", "part", [K, AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«nor»", "«ne de»", segments=wa("لَا", "la-nafiya", "part")),
  tok("ضَرَبْتُ", "daraba", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("يَوْمَ", "yawm", "noun", [K, MF, ID], "مَفْعُولٌ فِيهِ مَنْصُوبٌ، مُضَافٌ.", "«on the day of»", "«gününde»"),
  tok("الْجُمُعَةِ", "jumua", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Friday»", "«cuma»"),
  tok("يَوْمَ", "yawm", "noun", [K, MF, ID], "مَفْعُولٌ فِيهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ — وَهُوَ الْمُمْتَنِعُ.", "«on the day of» — the forbidden second ẓarf.", "«gününde» — câiz olmayan ikinci zarf."),
  tok("السَّبْتِ", "sabt", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Saturday»", "«cumartesi»", punct="،"),
 ]})
# ----------- s18 — unlike two letters of different meaning
S.append({"id": "s18", "translation": {"en": "unlike «I struck on Friday before the mosque» and «I ate of its fruit, of its apples».", "tr": "«cuma günü mescidin önünde dövdüm» ve «meyvesinden, elmasından yedim»'in aksine."},
 "tokens": [
  tok("بِخِلَافِ", "khilaf", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِ مَجْرُورٌ، مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«unlike»", "«… -in aksine»", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun")]),
  tok("ضَرَبْتُ", "daraba", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جُمْلَةٌ فِي مَحَلِّ جَرٍّ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("يَوْمَ", "yawm", "noun", [K, MF, ID], "مَفْعُولٌ فِيهِ مَنْصُوبٌ، مُضَافٌ — ظَرْفُ زَمَانٍ.", "«on the day of»", "«gününde»"),
  tok("الْجُمُعَةِ", "jumua", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Friday»", "«cuma»"),
  tok("أَمَامَ", "amama", "noun", [K, MF, ID], "مَفْعُولٌ فِيهِ مَنْصُوبٌ، مُضَافٌ — ظَرْفُ مَكَانٍ: مَعْنًى آخَرُ.", "«before» — a ẓarf of place: another meaning.", "«önünde» — mekân zarfı: başka mânâ."),
  tok("الْمَسْجِدِ", "masjid", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mosque»", "«mescidin»", punct="،"),
  tok("وَأَكَلْتُ", "akala", "verb", [K, AT, "fail"], "الْوَاوُ عَاطِفَةٌ، وَأَكَلْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I ate»", "«ve yedim»", segments=[seg("وَ", "wa", "conj"), seg("أَكَلْ", "akala", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.", "«of»", "«-den»"),
  tok("ثَمَرِهِ", "thamar", "noun", [K, HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its fruit»", "«meyvesinden»", segments=[seg("ثَمَرِ", "thamar", "noun"), pr3msi()]),
  tok("مِنْ", "min", "prep", [K, HJ, "badal"], "حَرْفُ جَرٍّ — بَدَلُ اشْتِمَالٍ: مِنْ ثَانِيَةٌ بِمَعْنًى آخَرَ.", "«of» — a second مِنْ of another meaning.", "«-den» — başka mânâda ikinci min."),
  tok("تُفَّاحِهِ", "tuffah", "noun", [K, HJ, ID, "badal"], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بَدَلٌ مِنْ ثَمَرِهِ.", "«its apples» — the badal.", "«elmasından» — bedel.", punct=".", segments=[seg("تُفَّاحِ", "tuffah", "noun"), pr3msi()]),
 ]})

# ---------------------------------------------------------------- the lexicon
CAND = {
 "maful-noun": G("maful-noun", "الْمَفْعُول", "ف ع ل", "noun", "the mafʿūl — the object (ism mafʿūl of فَعَلَ); الْمَفْعُولُ فِيهِ، الْمَفْعُولُ لَهُ", "mef'ûl — nesne; mef'ûlün fîh, mef'ûlün leh", 3),
 "mubham": G("mubham", "مُبْهَم", "ب ه م", "noun", "vague, unbounded (ism mafʿūl of أَبْهَمَ) — a ẓarf with no name of its own", "müphem — sınırı belirsiz zarf", 5),
 "mahdud": G("mahdud", "مَحْدُود", "ح د د", "noun", "bounded (ism mafʿūl of حَدَّ) — a ẓarf with a name of its own", "mahdûd — sınırlı zarf", 5),
 "quddam": G("quddam", "قُدَّام", "ق د م", "noun", "in front, before (a ẓarf of place)", "ön, önü (mekân zarfı)", 4),
 "wast": G("wast", "وَسْط", "و س ط", "noun", "amid, in the midst of — with a sukūn on the sīn, a ẓarf of place", "vasta — sin'i sâkin: ortasında (mekân zarfı)", 5),
 "wasat": G("wasat", "وَسَط", "و س ط", "noun", "the middle (a noun, with a fatḥa on the sīn)", "vasat — orta (fethalı: isim)", 4),
 "izaa": G("izaa", "إِزَاء", "أ ز ي", "noun", "opposite, facing (a ẓarf of place)", "izâe — karşısında", 6),
 "hidhaa": G("hidhaa", "حِذَاء", "ح ذ و", "noun", "alongside, opposite (a ẓarf of place)", "hizâe — hizasında", 6),
 "tilqaa": G("tilqaa", "تِلْقَاء", "ل ق ي", "noun", "facing, towards (a ẓarf of place)", "tilkâe — karşısına doğru", 6),
 "mamsuh": G("mamsuh", "مَمْسُوح", "م س ح", "noun", "measured, surveyed (ism mafʿūl of مَسَحَ)", "memsûh — ölçülmüş", 5),
 "farsakh": G("farsakh", "فَرْسَخ", None, "noun", "a farsakh — about three miles (a measure of distance)", "fersah — yaklaşık üç mil", 5, plural="فَرَاسِخ"),
 "mil-mile": G("mil-mile", "مِيل", "م ي ل", "noun", "a mile (a measure of distance)", "mil — uzunluk ölçüsü", 4, plural="أَمْيَال"),
 "barid": G("barid", "بَرِيد", "ب ر د", "noun", "a post-stage — four farsakhs; the post", "berîd — dört fersah; posta menzili", 5),
 "jawf": G("jawf", "جَوْف", "ج و ف", "noun", "the inside, the hollow of", "cevf — içi, boşluğu", 4),
 "istiqrar": G("istiqrar", "اسْتِقْرَار", "ق ر ر", "noun", "resting, being settled (masdar of اِسْتَقَرَّ) — the sense that lets فِي drop", "istikrâr — yerleşme (istekarra'nın masdarı)", 5),
 "maqtal": G("maqtal", "مَقْتَل", "ق ت ل", "noun", "the killing-place (a noun of place on مَفْعَل)", "maktel — öldürme yeri", 5),
 "madrab": G("madrab", "مَضْرَب", "ض ر ب", "noun", "the striking-place (a noun of place on مَفْعَل)", "madrab — vurma yeri", 5),
 "khan-inn": G("khan-inn", "خَان", None, "noun", "an inn, a caravanserai", "han — kervansaray", 4),
 "thani": G("thani", "الثَّانِي", "ث ن ي", "noun", "the second (a manqūṣ ordinal)", "ikinci (mankûs)", 2),
 "thalith": G("thalith", "الثَّالِث", "ث ل ث", "noun", "the third", "üçüncü", 2),
 "muallal": G("muallal", "مُعَلَّل", "ع ل ل", "noun", "explained by a cause (ism mafʿūl of عَلَّلَ) — the verb a mafʿūl lah gives the reason for", "muallel — sebebi gösterilen", 6),
 "muqarin": G("muqarin", "مُقَارِن", "ق ر ن", "noun", "concurrent, accompanying (ism fāʿil of قَارَنَ)", "mukârin — eşlik eden", 5),
 "hadhani": G("hadhani", "هٰذَانِ", None, "pron", "these two (the dual demonstrative; هٰذَيْنِ in naṣb and jarr)", "bu ikisi (tesniye işaret ismi; hâzeyni)", 3),
 "intasaba": G("intasaba", "انْتَصَبَ", "ن ص ب", "verb", "to take naṣb, be set in the accusative (Form VIII)", "nasb almak, mansûb olmak (infiâl)", 5),
 "ittifaq": G("ittifaq", "اتِّفَاق", "و ف ق", "noun", "agreement, consensus (masdar of اِتَّفَقَ) — بِالِاتِّفَاقِ: by agreement of all", "ittifak — bi'l-ittifak: ittifakla", 4),
 "abasa": G("abasa", "عَبَسَ", "ع ب س", "verb", "to frown, to scowl", "yüzünü ekşitmek", 4),
 "ama-blind": G("ama-blind", "أَعْمَى", "ع م ي", "noun", "blind — the blind man (an أَفْعَل adjective, a maqṣūr)", "âmâ — kör (ef'al vezninde, maksûr)", 3),
 "awsala": G("awsala", "أَوْصَلَ", "و ص ل", "verb", "to connect, to make reach (Form IV of a mithāl root)", "ulaştırmak, bağlamak (if'âl; misâl)", 5),
 "mahalli": G("mahalli", "مَحَلِّيّ", "ح ل ل", "noun", "of place — الْإِعْرَابُ الْمَحَلِّيُّ: the iʿrāb a word holds by its place, not its wording", "mahallî — mahallî i'rab", 5),
 "naibiyya": G("naibiyya", "نَائِبِيَّة", "ن و ب", "noun", "deputyhood — being the deputy of the doer", "nâibiyyet — nâib-i fâil olma", 6),
 "isal": G("isal", "إِيصَال", "و ص ل", "noun", "connection (masdar of أَوْصَلَ) — الْحَذْفُ وَالْإِيصَالُ: the letter dropped and the verb reaching the noun", "îsâl — hazf ve îsâl: harf düşer, fiil isme ulaşır", 5),
 "ikhtara": G("ikhtara", "اخْتَارَ", "خ ي ر", "verb", "to choose (Form VIII, hollow)", "seçmek (iftiâl; ecvef)", 4),
 "shudhudh": G("shudhudh", "شُذُوذ", "ش ذ ذ", "noun", "irregularity (masdar of شَذَّ) — عَلَى الشُّذُوذِ: as an irregular case", "şüzûz — şâz olarak", 5),
 "taalluq": G("taalluq", "تَعَلُّق", "ع ل ق", "noun", "hanging on, attachment (masdar of تَعَلَّقَ) — of a jarr phrase on its governor", "taalluk — câr-mecrûrun âmiline bağlanması", 5),
 "sabt": G("sabt", "سَبْت", "س ب ت", "noun", "Saturday — يَوْمُ السَّبْتِ", "cumartesi", 2),
 "tuffah": G("tuffah", "تُفَّاح", None, "noun", "apples (a collective)", "elma", 2),
}
_used = []
for s in S:
    for t in s["tokens"]:
        _used.append(t["lex"])
        for sg in t.get("segments") or []: _used.append(sg["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "intasaba", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَصَب", "نْتَصِب", "اِنْتَصِب", "اِنْتِصَاب", "مُنْتَصِب", None, None, None, "اِنْتَصَبَ يَنْتَصِبُ: صَارَ مَنْصُوبًا — بَابُ الِافْتِعَالِ، لَازِمٌ"))
put_morph(mo, "abasa", _sg.sound1("daraba", "عَبَس", "عْبِس", "اِعْبِس", "عُبُوس", "عَابِس", None, None, None, "عَبَسَ يَعْبِسُ: قَطَّبَ وَجْهَهُ — بَابُ ضَرَبَ، لَازِمٌ"))
put_morph(mo, "awsala", _sg.derived(_sg.B4 + " — مِثَالٌ وَاوِيٌّ", _sg.W4, "ُ", "أَوْصَل", "وصِل", "أَوْصِل", "إِيصَال", "مُوصِل", "مُوصَل", "أُوصِلَ", "يُوصَلُ", "أَوْصَلَ يُوصِلُ: أَبْلَغَ — بَابُ الْإِفْعَالِ، مِثَالٌ وَاوِيٌّ: يُوصِلُ بِلَا سُكُونٍ عَلَى الْوَاوِ، إِيصَالٌ بِالْيَاءِ"))
put_morph(mo, "ikhtara", _sg.derived_hollow(_sg.B8 + " — أَجْوَفُ", _sg.W8, "َ", "اِخْتَار", "اِخْتَر", "خْتَار", "خْتَر", "اِخْتَار", "اِخْتَر", "اِخْتِيَار", "مُخْتَار", "مُخْتَار", "اُخْتِيرَ", "يُخْتَارُ", "اِخْتَارَ يَخْتَارُ: اصْطَفَى — بَابُ الِافْتِعَالِ، أَجْوَفُ يَائِيٌّ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch3 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "حَذْفُ الْجَارِّ وَالْحَذْفُ وَالْإِيصَالُ", "en": "The omission of the governing letter, and omission-with-connection", "tr": "Câr harfinin hazfi; hazf ve îsâl"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — حذف الجار", "الكافية لابن الحاجب — المفعول فيه والمفعول له", "قواعد الإعراب لابن هشام"],
 "amil": "حَذْفُ الْجَارِّ قِيَاسِيٌّ فِي ثَلَاثَةِ مَوَاضِعَ وَسَمَاعِيٌّ فِيمَا عَدَاهَا — the letter drops by rule in three places and by hearing elsewhere; after the drop the verb reaches the noun (حَذْفٌ وَإِيصَالٌ)",
 "question": {
  "en": ["WHERE may the jarr letter drop by rule? In three places: the mafʿūl fīh (فِي), the mafʿūl lah (the lām) and before أَنْ / أَنَّ. Everywhere else the drop is heard, not reasoned — what the Arabs said is kept as it is.",
         "Which ẓarf of TIME may drop its فِي? Any — vague (حِينًا) or bounded (شَهْرًا). Time is always measured, so the ẓarf never needs the letter.",
         "Which ẓarf of PLACE may drop it? Only the VAGUE one: the six directions, عِنْدَ / لَدَى / وَسْطَ / بَيْنَ / إِزَاءَ / حِذَاءَ / تِلْقَاءَ, and the measured distances — and not جَانِب / وَجْه / وَسَط, nor خَارِجَ / دَاخِلَ / جَوْفَ, nor a place-noun that does not mean resting (الْمَقْتَل), nor one whose governor does not (مَقَام) — unless the governor means resting: قُمْتُ مَقَامَهُ.",
         "And the BOUNDED place (الدَّار، الْبَيْت)? Never — صَلَّيْتُ دَارًا is wrong, فِي دَارٍ is right — except after دَخَلَ، نَزَلَ، سَكَنَ: دَخَلْتُ الدَّارَ.",
         "When may the mafʿūl lah drop its lām? When it is the DOER's own act and CONCURRENT with the verb: ضَرَبْتُ زَيْدًا تَأْدِيبًا. Another's act (لِإِكْرَامِكَ) or another time (لِوَعْدِ أَمْسِ) keeps the lām.",
         "What happens to the noun once the letter is gone? The verb REACHES it — حَذْفٌ وَإِيصَالٌ — and the iʿrāb of place surfaces: naṣb as an object (وَاخْتَارَ مُوسَى قَوْمَهُ = مِنْ قَوْمِهِ), rafʿ as a deputy (مُشْتَرَكٌ فِيهِ). Before أَنْ the clause simply sits in the place of jarr: عَبَسَ وَتَوَلَّى أَنْ جَاءَهُ = لِأَنْ.",
         "Can the noun STAY majrūr after the letter drops? Only irregularly: اللهِ لَأَفْعَلَنَّ for وَاللهِ — kept, not imitated.",
         "May two letters of ONE meaning hang on one verb? Not without a conjunction: مَرَرْتُ بِزَيْدٍ بِعَمْرٍو is barred; ضَرَبْتُ يَوْمَ الْجُمُعَةِ أَمَامَ الْمَسْجِدِ is fine, because time and place are two meanings."],
  "tr": ["Cer harfi NEREDE kıyasla düşer? Üç yerde: mef'ûlün fîh (fî), mef'ûlün leh (lâm) ve en/enne'den önce. Diğer her yerde hazf işitilir, kıyas edilmez — Arapların dediği olduğu gibi tutulur.",
         "Hangi ZAMAN zarfı fî'sini düşürebilir? Hepsi — müphem (hînen) veya mahdûd (şehren). Zaman daima ölçülüdür; zarf harfe muhtaç olmaz.",
         "Hangi MEKÂN zarfı düşürebilir? Yalnız MÜPHEM olan: altı cihet, inde / ledâ / vasta / beyne / izâe / hizâe / tilkâe ve ölçülmüş mesafeler — cânib / vech / vasat değil, hâric / dâhil / cevf değil, istikrâr mânâsında olmayan mekân ismi (maktel) değil, âmili bu mânâda olmayan (makam) değil — âmil istikrâr mânâsındaysa olur: kumtü makâmehû.",
         "Ya MAHDÛD mekân (dâr, beyt)? Asla — salleytü dâran yanlış, fî dârin doğru — dehale, nezele, sekene'den sonra hâriç: dehaltü'd-dâr.",
         "Mef'ûlün leh lâmını ne zaman düşürür? FÂİLİN kendi fiili ve fiille AYNI ANDA olduğunda: darabtü Zeyden te'dîben. Başkasının fiili (li-ikrâmike) veya başka zaman (li-va'di emsi) lâmı korur.",
         "Harf gidince isme ne olur? Fiil ona ULAŞIR — hazf ve îsâl — ve mahallî i'rab ortaya çıkar: mef'ûl olarak nasb (vahtâra Mûsâ kavmehû = min kavmihî), nâib olarak ref' (müşterakün fîhi). En'den önce cümle cer mahallinde kalır: abese ve tevellâ en câehû = li-en.",
         "Harf düştükten sonra isim MECRÛR kalabilir mi? Yalnız şâz olarak: Allâhi le-ef'alenne, vallâhi yerine — ezberlenir, taklit edilmez.",
         "AYNI mânâda iki harf tek fiile bağlanır mı? Atıfsız hayır: merartü bi-Zeydin bi-Amrin yasaktır; darabtü yevme'l-cum'ati emâme'l-mescidi olur, çünkü zaman ve mekân iki mânâdır."]
 },
 "plain": {"en": "The little word before a noun (in, for, by) sometimes drops out — by rule only in three places, and then the verb takes the noun straight, so the noun shows the case its place demands.",
           "tr": "İsmin önündeki küçük kelime (-de, için, ile) bazen düşer — kıyasla yalnız üç yerde — ve o zaman fiil ismi doğrudan alır; isim, yerinin gerektirdiği hali gösterir."},
 "explanation": {"en": "Birgivī divides the omission of the jarr letter into qiyāsī and samāʿī. By rule it drops (1) from the mafʿūl fīh — always for a ẓarf of time, and for a ẓarf of place only when it is vague (the six directions, عِنْدَ and its kin, the measured distances), with the named exceptions and the bounded place that keeps فِي save after دَخَلَ / نَزَلَ / سَكَنَ; (2) from the mafʿūl lah when it is the doer's own act and concurrent with the verb; (3) before أَنْ and أَنَّ. Elsewhere the drop is heard and kept. After the drop, outside the first two places, the verb is connected to the noun (ḥadhf wa-īṣāl) and the maḥallī iʿrāb surfaces — naṣb as an object, rafʿ as a deputy; irregularly the noun may stay majrūr (اللهِ لَأَفْعَلَنَّ). Two letters of one meaning may not hang on one verb without conjunction.",
                 "tr": "Birgivî câr harfinin hazfini kıyâsî ve semâî diye ikiye ayırır. Kıyasla (1) mef'ûlün fîhten düşer — zaman zarfında daima, mekân zarfında yalnız müphem olanda (altı cihet, inde ve benzerleri, ölçülmüş mesafeler); sayılan istisnâlar ve fî'yi koruyan mahdûd mekân (dehale / nezele / sekene'den sonrası hâriç); (2) fâilin kendi fiili ve fiille aynı anda olan mef'ûlün lehten; (3) en ve enne'den önce. Başka yerde hazf işitilir ve ezberlenir. Hazften sonra, ilk iki yer dışında, fiil isme ulaştırılır (hazf ve îsâl) ve mahallî i'rab ortaya çıkar — mef'ûl olarak nasb, nâib olarak ref'; şâz olarak isim mecrûr kalabilir (Allâhi le-ef'alenne). Aynı mânâdaki iki harf atıfsız tek fiile bağlanamaz."},
 "examples": [
  {"ar": "سِرْتُ حِينًا وَصُمْتُ شَهْرًا", "en": "I travelled a while and fasted a month — the time ẓarf drops فِي, vague or bounded", "tr": "Bir süre yürüdüm, bir ay oruç tuttum — zaman zarfı fî'yi düşürür", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "لَا يُقَالُ: صَلَّيْتُ دَارًا بَلْ فِي دَارٍ", "en": "one does not say «I prayed a house»: the bounded place keeps its letter", "tr": "«bir ev namaz kıldım» denmez: mahdûd mekân harfini korur", "sourceStory": "izhar-al-asrar", "sentence": "s9"},
  {"ar": "ضَرَبْتُ زَيْدًا تَأْدِيبًا، بِخِلَافِ أَكْرَمْتُكَ لِإِكْرَامِكَ", "en": "the mafʿūl lah drops its lām only as the doer's own concurrent act", "tr": "mef'ûlün leh lâmını yalnız fâilin aynı andaki fiili olarak düşürür", "sourceStory": "izhar-al-asrar", "sentence": "s10"},
  {"ar": "وَاخْتَارَ مُوسَى قَوْمَهُ، أَيْ: مِنْ قَوْمِهِ", "en": "omission-with-connection: the verb reaches the noun and the naṣb of place surfaces", "tr": "hazf ve îsâl: fiil isme ulaşır, mahallî nasb ortaya çıkar", "sourceStory": "izhar-al-asrar", "sentence": "s15"},
  {"ar": "اللهِ لَأَفْعَلَنَّ، أَيْ: وَاللهِ", "en": "the irregular case: the noun stays majrūr after its letter is gone", "tr": "şâz hal: harfi gittikten sonra isim mecrûr kalır", "sourceStory": "izhar-al-asrar", "sentence": "s16"},
 ],
 "commonMistakes": [
  {"wrong": "صَلَّيْتُ دَارًا", "right": "صَلَّيْتُ فِي دَارٍ", "why": {"en": "a bounded ẓarf of place keeps its فِي — only the vague place and the time ẓarf drop it", "tr": "mahdûd mekân zarfı fî'sini korur — yalnız müphem mekân ve zaman zarfı düşürür"}},
  {"wrong": "أَكْرَمْتُكَ إِكْرَامَكَ", "right": "أَكْرَمْتُكَ لِإِكْرَامِكَ", "why": {"en": "the mafʿūl lah drops its lām only when it is the doer's own act, concurrent with the verb — your honouring is another's act", "tr": "mef'ûlün leh lâmını yalnız fâilin kendi, aynı andaki fiiliyse düşürür — senin ikramın başkasının fiilidir"}},
  {"wrong": "مَرَرْتُ بِزَيْدٍ بِعَمْرٍو", "right": "مَرَرْتُ بِزَيْدٍ وَبِعَمْرٍو", "why": {"en": "two letters of one meaning cannot both hang on one verb — join them, or change the meaning (a time and a place)", "tr": "aynı mânâdaki iki harf tek fiile birden bağlanamaz — atfedin, ya da mânâyı değiştirin (zaman ve mekân)"}},
 ],
}
ADD_EN = (" Chapter 3 (print pp. 91-94): the omission of the governing letter — by rule in three places: the mafʿūl fīh (the time ẓarf; the vague "
          "place ẓarf with its named exceptions; the bounded place save after دَخَلَ / نَزَلَ / سَكَنَ — s2-s9), the mafʿūl lah under its two conditions "
          "(s10-s11), and أَنْ / أَنَّ with 80:1-2 (s12); the samāʿī kept, not extended (s13); omission-with-connection and the maḥallī iʿrāb with "
          "7:155 (s14-s15); the irregular majrūr (s16); no two letters of one meaning on one verb (s17-s18). Two places the lithograph's transcription "
          "diverges from the received wording and the sense: the vague ẓarf is defined with «مَا لَمْ يَثْبُتْ لَهُ اسْمٌ» (the transcription drops the "
          "negation), and the barred example reads «كُنْتُ جَانِبَ الدَّارِ» (the transcription has كلت جانبا); both are given in the received form here. "
          "In s7 the print omits the fāʾ of أَمَّا's answer (يَجُوزُ), and the text keeps the print.")
ADD_TR = (" Üçüncü bab (baskı s. 91-94): câr harfinin hazfi — kıyasla üç yerde: mef'ûlün fîh (zaman zarfı; sayılan istisnâlarıyla müphem mekân "
          "zarfı; dehale / nezele / sekene'den sonrası hâriç mahdûd mekân — s2-s9), iki şartıyla mef'ûlün leh (s10-s11) ve 80:1-2 ile en / enne (s12); "
          "semâî ezberlenir, kıyas edilmez (s13); 7:155 ile hazf ve îsâl ve mahallî i'rab (s14-s15); şâz mecrûr (s16); aynı mânâda iki harf tek fiile "
          "bağlanmaz (s17-s18). Taşbaskının transkripsiyonu iki yerde alınan metinden ve mânâdan ayrılır: müphem zarf «mâ lem yesbut lehû ismün» ile "
          "tanımlanır (transkripsiyon olumsuzluğu düşürmüş), yasak örnek «küntü cânibe'd-dâr» okunur (transkripsiyonda kelt cânibâ); ikisi de burada "
          "alınan şekliyle verilmiştir. s7'de baskı emmâ'nın cevabındaki fâ'yı düşürmüştür (yecûzu); metin baskıyı korur.")
write_out(3, S, TITLE, ADD_EN, ADD_TR, "pp. 91-94", GLOSS_ADD, notes=(NOTE,),
          related=(("maful-fih", [K]), ("maful-lah", [K]), ("hadhf-wa-taqdir", [K]), (K2, [K]), (K1, [K])))
report(3, S, GLOSS_ADD, (NOTE,))
