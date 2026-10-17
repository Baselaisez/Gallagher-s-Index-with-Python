# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 2: the MUTAʿALLAQ every jarr letter needs (a verb, its like, or its meaning) and the
# seven that attach to nothing; the majrur's MAHALL (the zaida and rubba leave it as it was; the exceptive letters' majrur
# is like the mustathna; lawla's and la'alla's majrur is a mubtada; the rest: maf'ul fih under في, maf'ul lah under the
# lam, maf'ul bihi ghayr sarih under the others); the muta'allaq made passive on the phrase (مُرَّ بِزَيْدٍ); fronting;
# the omitted muta'allaq — ZARF MUSTAQARR (a general verb) and ZARF LAGHW. Print pp. 89–91.
#   python3 author_izhar_ch2.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "mahall-al-majrur"
K1 = "al-amil-wa-aqsamuh"
ZL = "zarf-mustaqarr-wa-laghw"
TITLE = {"ar": "الْمُتَعَلَّقُ وَمَحَلُّ الْمَجْرُورِ وَالظَّرْفُ الْمُسْتَقِرُّ وَاللَّغْوُ", "en": "What the jarr phrase hangs on, the majrūr's place, and the settled and idle ẓarf", "tr": "Müteallak, mecrûrun mahalli, zarf-ı müstakar ve lağv"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; HJN = "huruf-jarr-nawadir"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"

def fi(punct=None, tags=()): return tok("فِي", "fi", "prep", [K, HJ] + list(tags), "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(punct=None): return tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on».", "«üzere».", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ.", "«or».", "«ya da».")
def nahw(): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted sentence.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=":")
def quoted(full, lex, pos, en, tr, mahall_ar, mahall_en, mahall_tr, punct=None, joined=True, extra=()):
    segs = wa(full[2:], lex, pos) if joined else None
    ar = ("الْوَاوُ عَاطِفَةٌ، وَالْمَعْطُوفُ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، " if joined else "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، ") + mahall_ar + "."
    return tok(full, lex, pos, [K, HT] + list(extra), ar, en + " — quoted as a word; " + mahall_en + ".", tr + " — hikâye edilmiş; " + mahall_tr + ".", punct=punct, segments=segs)
def majrur_mubt(full="وَمَجْرُورُ", en="«and the majrūr of»", tr="«ve mecrûru»", pre_ar="الْوَاوُ لِلِاسْتِئْنَافِ، "):
    segs = wa("مَجْرُورُ", "majrur-noun", "noun") if full.startswith("وَ") else fa("مَجْرُورُ", "majrur-noun", "noun")
    return tok(full, "majrur-noun", "noun", [K, MK, ID], pre_ar + "وَمَجْرُورُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", en + " — the mubtada, annexed.", tr + " — mübtedâ, muzâf.", segments=segs)
def ma_maws_j(): return tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", ID], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the relative, annexed to.", "«… olan» — mevsûl, muzâfun ileyh.")
def ada_v(full="عَدَا", obj=None, punct=None):
    segs = [seg("عَدَا", "ada-except", "verb"), seg("هُمَا", "pron-3d", "pron")] if obj else None
    return tok(full, "ada-except", "verb", [K, "istithna", "ism-mawsul"], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ" + ("، وَالضَّمِيرُ مَفْعُولٌ بِهِ" if obj else "") + " — صِلَةُ الْمَوْصُولِ.", "«other than» — the exceptive verb; the relative clause.", "«başka olan» — istisnâ fiili; sıla.", punct=punct, segments=segs)
def in_kana(full_in="إِنْ"):
    return [tok(full_in, "in-shartiyya", "part", [K, "in-shartiyya"], ("الْفَاءُ لِلتَّفْرِيعِ، وَ" if full_in.startswith("فَ") else "") + "إِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional.", "«eğer» — şart edatı.", segments=(fa("إِنْ", "in-shartiyya", "part") if full_in.startswith("فَ") else None)),
            tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha", "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.", "«is» — kāna, the shart verb.", "«ise» — nâkıs kâne, şart fiili."),
            tok("الْجَارُّ", "jarr-letter", "noun", [K, "kana-wa-akhawatuha", "doubled-verbs"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ فَاعِلٍ مِنْ جَرَّ.", "«the governing letter» — the ism of kāna.", "«câr» — kâne'nin ismi.")]
def bimanahu(punct="،"):
    return [aw(), tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", AT], "اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ.", "«what» — joined to the khabar of kāna.", "«… olan» — ma'tûf, nasb mahallinde."),
            tok("بِمَعْنَاهُ", "mana", "noun", [K, HJ, ID, "ism-maqsur-manqus", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةُ مَا.", "«in its meaning» — the relative's clause (a jarr phrase).", "«onun manasında» — sıla (câr-mecrûr).", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), pr3ms()])]
def mahall_kh(full, lex, en, tr):
    return [tok(full, lex, "noun", [K, MK, ID, "ism-maful"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — إِضَافَةٌ لَفْظِيَّةٌ.", "«" + en + "» — the khabar, annexed (a verbal idafa).", "«" + tr + "» — haber, muzâf (lafzî izâfet)."),
            tok("الْمَحَلِّ", "mahall", "noun", [K, ID, "idafa-lafziyya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«in place»", "«mahalli»")]
def ala_annahu():
    return [ala(), tok("أَنَّهُ", "anna", "part", [K, "inna-wa-akhawatuha", HJ], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ مَجْرُورٌ بِعَلَى.", "«on the ground that it» — أَنَّ with its ism.", "«… olması cihetiyle» — enne ve ismi.", segments=[seg("أَنَّ", "anna", "part"), pr3ms()])]
def bizayd(full="بِزَيْدٍ", ar="الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ لَفْظًا، مَفْعُولٌ بِهِ غَيْرُ صَرِيحٍ مَحَلًّا.", en="«by Zayd» — majrūr in wording, the object in place.", tr="«Zeyd'e» — lafzen mecrûr, mahallen mef'ûl.", punct=None, tags=()):
    return tok(full, "zayd", "propn", [K, HJ, "maful-bihi"] + list(tags), ar, en, tr, punct=punct, segments=[seg("بِ", "bi", "prep"), seg("زَيْدٍ", "zayd", "propn")])
def marartu(full="مَرَرْتُ", punct=None, ar_pre=""):
    segs = ([seg("وَ", "wa", "conj")] if full.startswith("وَ") else []) + [seg("مَرَرْ", "marra", "verb"), seg("تُ", "pron-1s", "pron")]
    return tok(full, "marra", "verb", [K, "fail", "doubled-verbs"], ar_pre + "مَاضٍ مُضَاعَفٌ، فُكَّ إِدْغَامُهُ لِاتِّصَالِ ضَمِيرِ الرَّفْعِ، وَالتَّاءُ فَاعِلٌ.", "«I passed» — the doubled verb opened before the doer's tāʾ.", "«geçtim» — muzâaf, fâil tâsı önünde idgam çözüldü.", punct=punct, segments=segs)
def zayd_dar(punct=None):
    return [tok("زَيْدٌ", "zayd", "propn", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."), fi(tags=[ZL]),
            tok("الدَّارِ", "dar", "noun", [K, HJ, ZL], "مَجْرُورٌ بِفِي.", "«the house»", "«evde»", punct=punct)]

# ----------- s1 — every jarr letter needs a muta'allaq; the zaida excepted
S.append({"id": "s1", "translation": {"en": "These letters cannot do without something to hang on — a verb, its like, or its meaning — except the extra ones among them, as in «God suffices» (كَفَى بِاللهِ) and «a dirham is enough for you» (بِحَسْبِكَ دِرْهَمٌ),", "tr": "Bu harflerin bir müteallakı olmalıdır — bir fiil, fiil benzeri ya da fiil manası — içlerinden zâid olanlar hariç; meselâ كَفَى بِاللهِ ve بِحَسْبِكَ دِرْهَمٌ,"},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, "la-nafiya-lil-jins"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", "«and there is no» — the genus-negating lā.", "«ve … yoktur» — cins nefyeden lâ.", segments=wa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«escape» — the ism of lā, built on the fatḥa.", "«çare» — lâ'nın ismi, fetha üzere mebnî."),
  tok("لِهٰذِهِ", "hadhihi", "pron", [K, HJ, "asma-al-ishara", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَهٰذِهِ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَا.", "«for these» — the jarr phrase is the khabar of lā.", "«bu … için» — câr-mecrûr lâ'nın haberi.", segments=[seg("لِ", "li", "prep"), seg("هٰذِهِ", "hadhihi", "pron")]),
  tok("الْحُرُوفِ", "harf", "noun", [K, "badal", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«letters» — the badal of the demonstrative.", "«harfler» — işaret isminin bedeli."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("مُتَعَلَّقٍ", "mutaallaq", "noun", [K, HJ, ZL, "ism-maful"], "مَجْرُورٌ بِمِنْ — مُتَعَلِّقٌ بِالْخَبَرِ: مَا يَتَعَلَّقُ بِهِ الْجَارُّ.", "«something to hang on» — what the letter attaches to.", "«müteallak» — harfin bağlandığı şey.", punct=":"),
  tok("فِعْلٍ", "fil", "noun", [K, "badal"], "بَدَلٌ مِنْ مُتَعَلَّقٍ مَجْرُورٌ — بَدَلُ تَفْصِيلٍ.", "«a verb» — the badal spelling it out.", "«bir fiil» — tafsîl bedeli."),
  aw(),
  tok("شِبْهِهِ", "shibh", "noun", [K, AT, ID], "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ الْفَاعِلِ وَنَحْوُهُ.", "«its like» — the participle and its kin.", "«benzeri» — ism-i fâil ve benzerleri.", segments=[seg("شِبْهِ", "shibh", "noun"), pr3msi()]),
  aw(),
  tok("مَعْنَاهُ", "mana", "noun", [K, AT, ID, "ism-maqsur-manqus", "mana-al-fil"], "مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَا فِيهِ مَعْنَى الْفِعْلِ كَالْإِشَارَةِ.", "«its meaning» — what carries a verb's sense.", "«manası» — fiil manası taşıyan.", punct="،", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "حَرْفُ اسْتِثْنَاءٍ.", "«except»", "«hariç»"),
  tok("الزَّائِدَ", "zaid", "noun", [K, "istithna", "ism-fail"], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ.", "«the extra one» — the mustathnā.", "«zâid olan» — müstesnâ."),
  tok("مِنْهَا", "min", "prep", [K, HJ, "hal"], "مِنْ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — حَالٌ مِنَ الزَّائِدِ.", "«among them»", "«onlardan»", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  nahw(),
  tok("كَفَى", "kafa", "verb", [K, "fail", "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ نَاقِصٌ يَائِيٌّ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ.", "«suffices» — a nāqiṣ verb.", "«kâfidir» — nâkıs fiil."),
  tok("بِاللهِ", "allah", "propn", [K, HJ, "fail", HT], "الْبَاءُ زَائِدَةٌ، وَلَفْظُ الْجَلَالَةِ فَاعِلٌ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا.", "«God» — the bāʾ is extra; the Name is the doer, majrūr in wording and marfūʿ in place.", "«Allah» — bâ zâid; lafza-i celâl lafzen mecrûr, mahallen merfû fâil.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  tok("وَبِحَسْبِكَ", "hasb-enough", "noun", [K, HJ, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ زَائِدَةٌ، وَحَسْبِ خَبَرٌ مُقَدَّمٌ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«enough for you» — the extra bāʾ on the fronted khabar.", "«sana yeter» — zâid bâ, mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("حَسْبِ", "hasb-enough", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("دِرْهَمٌ", "dirham", "noun", [K, MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a dirham» — the delayed mubtada.", "«bir dirhem» — muahhar mübtedâ.", punct="،"),
 ]})

# ----------- s2 — the seven that attach to nothing
S.append({"id": "s2", "translation": {"en": "and رُبَّ, حَاشَا, خَلَا, عَدَا, لَوْلَا and لَعَلَّ — for they attach to nothing.", "tr": "ve rubbe, hâşâ, halâ, adâ, levlâ ve lealle — çünkü bunlar hiçbir şeye bağlanmaz."},
 "tokens": [
  quoted("وَرُبَّ", "rubba", "part", "«and rubba»", "«ve rubbe»", "مَعْطُوفٌ عَلَى الزَّائِدَ فِي مَحَلِّ نَصْبٍ", "joined to «the extra one» in the place of naṣb", "«zâid»e ma'tûf, nasb mahallinde", extra=[HJ, "istithna"]),
  quoted("وَحَاشَا", "hasha", "part", "«and ḥāshā»", "«ve hâşâ»", "مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ", "joined, in the place of naṣb", "ma'tûf, nasb mahallinde", extra=[HJN]),
  quoted("وَخَلَا", "khala-except", "part", "«and khalā»", "«ve halâ»", "مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ", "joined, in the place of naṣb", "ma'tûf, nasb mahallinde", extra=[HJN]),
  quoted("وَعَدَا", "ada-except", "part", "«and ʿadā»", "«ve adâ»", "مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ", "joined, in the place of naṣb", "ma'tûf, nasb mahallinde", extra=[HJN]),
  quoted("وَلَوْلَا", "lawla", "part", "«and lawlā»", "«ve levlâ»", "مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ", "joined, in the place of naṣb", "ma'tûf, nasb mahallinde", extra=[HJN]),
  quoted("وَلَعَلَّ", "laalla", "part", "«and laʿalla»", "«ve lealle»", "مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ", "joined, in the place of naṣb", "ma'tûf, nasb mahallinde", punct="،", extra=[HJN]),
  tok("فَإِنَّهَا", "inna", "part", [K, "inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«for they» — the fā of reason; إِنَّ and its ism.", "«çünkü onlar» — ta'lîl fâsı; inne ve ismi.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3fs()]),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«not»", "«-mez»"),
  tok("تَتَعَلَّقُ", "taallaqa-hang", "verb", [K, "inna-wa-akhawatuha", ZL], "مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«attach» — the clause is the khabar of إِنَّ.", "«bağlanır» — cümle inne'nin haberi."),
  tok("بِشَيْءٍ", "shay", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«to anything»", "«bir şeye»", punct=".", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")]),
 ]})

# ----------- s3 — the zaida's and rubba's majrur stays as it was
S.append({"id": "s3", "translation": {"en": "So the majrūr of the extra letter and of رُبَّ stays as it was before they entered,", "tr": "Zâidin ve rubbe'nin mecrûru, onlar dâhil olmadan önce ne idiyse öyle kalır;"},
 "tokens": [
  majrur_mubt("فَمَجْرُورُ", "«so the majrūr of»", "«o halde … mecrûru»", "الْفَاءُ لِلتَّفْرِيعِ، "),
  tok("الزَّائِدِ", "zaid", "noun", [K, ID, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the extra one»", "«zâidin»"),
  quoted("وَرُبَّ", "rubba", "part", "«and rubba»", "«ve rubbe»", "مَعْطُوفٌ عَلَى الزَّائِدِ فِي مَحَلِّ جَرٍّ", "joined to «the extra one» in the place of jarr", "«zâid»e ma'tûf, cer mahallinde", extra=[HJ]),
  tok("بَاقٍ", "baqin", "noun", [K, MK, "ism-maqsur-manqus", "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمٌ مَنْقُوصٌ.", "«stays» — the khabar; a manqūṣ noun, its ḍamma estimated.", "«bâkîdir» — haber; manqûs isim, dammesi takdîrî."),
  ala(),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", HJ], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what» — the relative in jarr.", "«… olan şey» — mevsûl, cer mahallinde."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha", "ism-mawsul"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — صِلَةُ الْمَوْصُولِ.", "«it was» — kāna, its ism concealed; the relative clause.", "«idi» — nâkıs kâne, ismi müstetir; sıla."),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ, "kana-wa-akhawatuha"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ، وَالْهَاءُ الْعَائِدُ.", "«upon» — the jarr phrase is the khabar of kāna; the pronoun returns.", "«üzere» — câr-mecrûr kâne'nin haberi; hâ âid.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("قَبْلَ", "qabla", "noun", [K, "maful-fih", ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«before» — the ẓarf, annexed.", "«önce» — zarf, muzâf."),
  tok("دُخُولِهِمَا", "dukhul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their two entering»", "«ikisinin dâhil olmasından»", punct="،", segments=[seg("دُخُولِ", "dukhul", "noun"), seg("هِمَا", "pron-3d", "pron")]),
 ]})

# ----------- s4 — the exceptive letters' majrur
S.append({"id": "s4", "translation": {"en": "and the majrūr of the exceptive letters is like what is excepted by إِلَّا, as will come;", "tr": "istisnâ harflerinin mecrûru, geleceği üzere, illâ ile müstesnâ olan gibidir;"},
 "tokens": [
  majrur_mubt("وَمَجْرُورُ", "«and the majrūr of»", "«ve … mecrûru»", "الْوَاوُ عَاطِفَةٌ، "),
  tok("حُرُوفِ", "harf", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the letters of»", "«harflerinin»"),
  tok("الِاسْتِثْنَاءِ", "istithna", "noun", [K, ID, "istithna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«exception»", "«istisnâ»"),
  tok("كَالْمُسْتَثْنَى", "mustathna", "noun", [K, HJ, MK, "ism-maqsur-manqus", "istithna"], "الْكَافُ حَرْفُ جَرٍّ، وَالْمُسْتَثْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«like the excepted» — the jarr phrase is the khabar; a maqṣūr noun.", "«müstesnâ gibi» — câr-mecrûr haber; maksûr isim.", segments=[seg("كَ", "ka", "prep"), seg("الْمُسْتَثْنَى", "mustathna", "noun")]),
  tok("بِإِلَّا", "illa", "part", [K, HJ, HT, "istithna"], "الْبَاءُ حَرْفُ جَرٍّ، وَإِلَّا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«by illā» — the particle quoted under the bāʾ.", "«illâ ile» — bâ altında hikâye edilmiş harf.", segments=[seg("بِ", "bi", "prep"), seg("إِلَّا", "illa", "part")]),
  ala(),
  tok("مَا", "ma-mawsula", "pron", [K, HJ, "ism-mawsul"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«… üzere»"),
  tok("سَيَجِيءُ", "jaa", "verb", [K, "ism-mawsul"], "السِّينُ لِلِاسْتِقْبَالِ، وَيَجِيءُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«will come»", "«gelecek»", punct="،", segments=[seg("سَ", "sa", "part"), seg("يَجِيءُ", "jaa", "verb")]),
 ]})

# ----------- s5 — lawla's and la'alla's majrur is a mubtada
S.append({"id": "s5", "translation": {"en": "and the majrūr of لَوْلَا and لَعَلَّ is a mubtada, and what follows it is its khabar — as in «were it not for you, Zayd would have perished» and «perhaps Zayd is standing».", "tr": "levlâ ve lealle'nin mecrûru mübtedâdır, sonrası da haberidir; meselâ لَوْلَاكَ لَهَلَكَ زَيْدٌ ve لَعَلَّ زَيْدٍ قَائِمٌ."},
 "tokens": [
  majrur_mubt("وَمَجْرُورُ", "«and the majrūr of»", "«ve … mecrûru»", "الْوَاوُ عَاطِفَةٌ، "),
  quoted("لَوْلَا", "lawla", "part", "«lawlā»", "«levlâ»", "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ", "annexed to, in the place of jarr", "muzâfun ileyh, cer mahallinde", joined=False, extra=[HJN, ID]),
  quoted("وَلَعَلَّ", "laalla", "part", "«and laʿalla»", "«ve lealle»", "مَعْطُوفٌ فِي مَحَلِّ جَرٍّ", "joined, in the place of jarr", "ma'tûf, cer mahallinde", extra=[HJN]),
  tok("مُبْتَدَأٌ", "mubtada", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a mubtada» — the khabar.", "«mübtedâdır» — haber."),
  tok("وَمَا", "ma-mawsula", "pron", [K, "ism-mawsul", MK], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and what» — the relative, a second mubtada.", "«ve … olan» — mevsûl, ikinci mübtedâ.", segments=wa("مَا", "ma-mawsula", "pron")),
  tok("بَعْدَهُ", "bada", "noun", [K, "maful-fih", ID, "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«after it» — the relative's clause (a ẓarf).", "«ondan sonra» — sıla (zarf).", segments=[seg("بَعْدَ", "bada", "noun"), pr3ms()]),
  tok("خَبَرُهُ", "khabar-predicate", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its khabar» — the khabar.", "«onun haberidir» — haber.", punct="،", segments=[seg("خَبَرُ", "khabar-predicate", "noun"), pr3ms()]),
  nahw(),
  tok("لَوْلَاكَ", "lawla", "part", [K, HJN, MK, HT], "لَوْلَا حَرْفُ جَرٍّ عِنْدَ الْمُصَنِّفِ لِاتِّصَالِ الضَّمِيرِ، وَالْكَافُ مَجْرُورٌ لَفْظًا، مُبْتَدَأٌ مَحَلًّا، خَبَرُهُ مَحْذُوفٌ: مَوْجُودٌ.", "«were it not for you» — the pronoun majrūr in wording, a mubtada in place with its khabar «existing» omitted.", "«sen olmasaydın» — zamir lafzen mecrûr, mahallen mübtedâ; haberi mahzûf: mevcûd.", segments=[seg("لَوْلَا", "lawla", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَهَلَكَ", "halaka", "verb", [K, "fail", "idha-shartiyya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْلَا، وَهَلَكَ فِعْلٌ مَاضٍ.", "«would have perished» — the lām of the answer.", "«helâk olurdu» — cevap lâmı.", segments=[seg("لَ", "lam-letter", "part"), seg("هَلَكَ", "halaka", "verb")]),
  tok("زَيْدٌ", "zayd", "propn", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="،"),
  tok("وَلَعَلَّ", "laalla", "part", [K, HJN, AT], "الْوَاوُ عَاطِفَةٌ، وَلَعَلَّ حَرْفُ جَرٍّ فِي لُغَةِ عُقَيْلٍ.", "«and perhaps» — a jarr letter in ʿUqayl's dialect.", "«ve belki» — Ukayl lügatinde cer harfi.", segments=wa("لَعَلَّ", "laalla", "part")),
  tok("زَيْدٍ", "zayd", "propn", [K, HJN, MK], "مَجْرُورٌ لَفْظًا بِلَعَلَّ، مُبْتَدَأٌ مَحَلًّا.", "«Zayd» — majrūr in wording, the mubtada in place.", "«Zeyd» — lafzen mecrûr, mahallen mübtedâ."),
  tok("قَائِمٌ", "qaim", "noun", [K, MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«standing» — the khabar.", "«ayaktadır» — haber.", punct="."),
 ]})

# ----------- s6 — the rest: maf'ul fih under في
S.append({"id": "s6", "translation": {"en": "And the majrūr of the letters other than these seven is in the place of naṣb: as a mafʿūl fīh of what it hangs on, if the governing letter is فِي or what means the same — as in «I prayed in the mosque» (فِي الْمَسْجِدِ or بِالْمَسْجِدِ);", "tr": "Bu yedinin dışındaki harflerin mecrûru nasb mahallindedir: câr فِي ya da o manada bir harf ise müteallakının mef'ûlün fîhi olarak — meselâ صَلَّيْتُ فِي الْمَسْجِدِ ya da بِالْمَسْجِدِ;"},
 "tokens": [
  majrur_mubt("وَمَجْرُورُ", "«and the majrūr of»", "«ve … mecrûru»", "الْوَاوُ لِلِاسْتِئْنَافِ، "),
  ma_maws_j(), ada_v(),
  tok("هٰذِهِ", "hadhihi", "pron", [K, "istithna", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولُ عَدَا.", "«these» — the object of ʿadā.", "«bu» — adâ'nın mef'ûlü."),
  tok("السَّبْعَةَ", "saba-seven", "noun", [K, "badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«seven» — the badal.", "«yedi» — bedel."),
  *mahall_kh("مَنْصُوبُ", "mansub", "in naṣb", "mansûb"),
  *ala_annahu(),
  tok("مَفْعُولٌ", "maful-object", "noun", [K, "inna-wa-akhawatuha", "maful-fih"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«a mafʿūl» — the khabar of أَنَّ.", "«mef'ûl» — enne'nin haberi."),
  tok("فِيهِ", "fi", "prep", [K, HJ, "maful-fih"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — صِفَةٌ لِمَفْعُولٍ: مَفْعُولٌ فِيهِ.", "«in it» — the phrase names the kind: mafʿūl fīh.", "«onda» — mef'ûlün fîh adını tamamlar.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("لِمُتَعَلَّقِهِ", "mutaallaq", "noun", [K, HJ, ID, ZL], "اللَّامُ حَرْفُ جَرٍّ، وَمُتَعَلَّقِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of what it hangs on»", "«müteallakının»", segments=[seg("لِ", "li", "prep"), seg("مُتَعَلَّقِ", "mutaallaq", "noun"), pr3msi()]),
  *in_kana(),
  quoted("فِي", "fi", "prep", "«fī»", "«fî»", "خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ", "the khabar of kāna in the place of naṣb", "kâne'nin haberi, nasb mahallinde", joined=False, extra=[HJ]),
  *bimanahu(),
  nahw(),
  tok("صَلَّيْتُ", "salla", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I prayed»", "«namaz kıldım»", segments=[seg("صَلَّيْ", "salla", "verb"), seg("تُ", "pron-1s", "pron")]),
  fi(tags=["maful-fih"]),
  tok("الْمَسْجِدِ", "masjid", "noun", [K, HJ, "maful-fih"], "مَجْرُورٌ لَفْظًا، مَفْعُولٌ فِيهِ مَحَلًّا.", "«the mosque» — majrūr in wording, the mafʿūl fīh in place.", "«mescidde» — lafzen mecrûr, mahallen mef'ûlün fîh."),
  aw(),
  tok("بِالْمَسْجِدِ", "masjid", "noun", [K, HJ, "maful-fih"], "الْبَاءُ بِمَعْنَى فِي، وَالْمَسْجِدِ مَجْرُورٌ لَفْظًا مَفْعُولٌ فِيهِ مَحَلًّا.", "«in the mosque» — the bāʾ meaning fī.", "«mescidde» — fî manasında bâ.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْمَسْجِدِ", "masjid", "noun")]),
 ]})

# ----------- s7 — maf'ul lah under the lam
S.append({"id": "s7", "translation": {"en": "or as a mafʿūl lah, if the governing letter is the lām or what means the same — as in «I struck Zayd for correction» and «why did you disobey?» (كَيْمَهْ);", "tr": "ya da câr lâm veya o manada bir harf ise mef'ûlün leh olarak — meselâ ضَرَبْتُ زَيْدًا لِلتَّأْدِيبِ ve كَيْمَهْ عَصَيْتَ;"},
 "tokens": [
  aw(),
  tok("مَفْعُولٌ", "maful-object", "noun", [K, AT, "maful-lah"], "مَعْطُوفٌ عَلَى خَبَرِ أَنَّ مَرْفُوعٌ.", "«a mafʿūl» — joined to the khabar of أَنَّ.", "«mef'ûl» — enne'nin haberine ma'tûf."),
  tok("لَهُ", "li", "prep", [K, HJ, "maful-lah"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — صِفَةٌ: مَفْعُولٌ لَهُ.", "«for it» — names the kind: mafʿūl lah.", "«onun için» — mef'ûlün leh adını tamamlar.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  *in_kana(),
  tok("لَامًا", "lam-letter", "noun", [K, "kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ الْحَرْفِ.", "«a lām» — the khabar of kāna.", "«lâm» — kâne'nin haberi."),
  *bimanahu(),
  nahw(),
  tok("ضَرَبْتُ", "daraba", "verb", [K, "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("زَيْدًا", "zayd", "propn", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the object.", "«Zeyd'i» — mef'ûl."),
  tok("لِلتَّأْدِيبِ", "tadib", "noun", [K, HJ, "maful-lah", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَالتَّأْدِيبِ مَجْرُورٌ لَفْظًا، مَفْعُولٌ لَهُ مَحَلًّا.", "«for correction» — majrūr in wording, the mafʿūl lah in place.", "«te'dib için» — lafzen mecrûr, mahallen mef'ûlün leh.", punct="،", segments=[seg("لِ", "li", "prep"), seg("التَّأْدِيبِ", "tadib", "noun")]),
  tok("وَكَيْمَهْ", "kaymah", "part", [K, HJN, "maful-lah", "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَكَيْ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَمَا الِاسْتِفْهَامِيَّةُ مَجْرُورَةٌ بِهَا حُذِفَتْ أَلِفُهَا، وَالْهَاءُ لِلسَّكْتِ.", "«and why» — kay governing the interrogative mā, its alif dropped, the hāʾ of pause after it.", "«ve niçin» — key istifham mâ'sını cer eder, elifi düşmüş, sonunda sekte hâsı.", segments=[seg("وَ", "wa", "conj"), seg("كَيْ", "kay", "part"), seg("مَهْ", "ma-istifhamiyya", "pron")]),
  tok("عَصَيْتَ", "asa", "verb", [K, "fail", "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ فَاعِلٌ.", "«did you disobey»", "«isyan ettin»", punct="،", segments=[seg("عَصَيْ", "asa", "verb"), seg("تَ", "pron-2ms", "pron")]),
 ]})

# ----------- s8 — maf'ul bihi ghayr sarih under the others
S.append({"id": "s8", "translation": {"en": "and as a mafʿūl bihi that is not explicit, if the governing letter is any other — as in «I passed by Zayd».", "tr": "ve câr bu ikisinin dışında bir harf ise sarih olmayan mef'ûlün bih olarak — meselâ مَرَرْتُ بِزَيْدٍ."},
 "tokens": [
  tok("وَمَفْعُولٌ", "maful-object", "noun", [K, AT, "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَمَفْعُولٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a mafʿūl»", "«ve mef'ûl»", segments=wa("مَفْعُولٌ", "maful-object", "noun")),
  tok("بِهِ", "bi", "prep", [K, HJ, "maful-bihi"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — صِفَةٌ: مَفْعُولٌ بِهِ.", "«to it» — names the kind: mafʿūl bihi.", "«ona» — mef'ûlün bih adını tamamlar.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("غَيْرُ", "ghayr", "noun", [K, NA, ID], "صِفَةٌ لِمَفْعُولٍ مَرْفُوعَةٌ، مُضَافٌ.", "«not» — the naʿt, annexed.", "«olmayan» — sıfat, muzâf."),
  tok("صَرِيحٍ", "sarih", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«explicit»", "«sarih»"),
  *in_kana(),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", "kana-wa-akhawatuha"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«what» — the relative, the khabar of kāna.", "«… olan» — mevsûl, kâne'nin haberi."),
  ada_v("عَدَاهُمَا", obj=True, punct="،"),
  nahw(),
  marartu(),
  bizayd(punct="."),
 ]})

# ----------- s9 — the muta'allaq made passive on the phrase
S.append({"id": "s9", "translation": {"en": "And sometimes what the phrase hangs on is made to rest on the governing letter and its majrūr, so the phrase is in the place of rafʿ as the deputy of the doer — as in «Zayd was passed by» (مُرَّ بِزَيْدٍ).", "tr": "Bazen müteallak câr ile mecrûra isnad edilir; o zaman ref' mahallinde nâib-i fâil olur — meselâ مُرَّ بِزَيْدٍ."},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يُسْنَدُ", "asnada", "verb", [K, "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ.", "«is made to rest» — passive.", "«isnad edilir» — meçhul."),
  tok("الْمُتَعَلَّقُ", "mutaallaq", "noun", [K, "naib-al-fail", ZL], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«what it hangs on» — the deputy doer.", "«müteallak» — nâib-i fâil."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْجَارِّ", "jarr-letter", "noun", [K, HJ, "doubled-verbs"], "مَجْرُورٌ بِإِلَى.", "«the governing letter»", "«câr»"),
  tok("وَالْمَجْرُورِ", "majrur-noun", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالْمَجْرُورِ مَعْطُوفٌ مَجْرُورٌ.", "«and its majrūr»", "«ve mecrûra»", segments=wa("الْمَجْرُورِ", "majrur-noun", "noun")),
  tok("فَيَكُونُ", "kana", "verb", [K, "kana-wa-akhawatuha"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَكُونُ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«so it is» — kāna, its ism concealed.", "«böylece olur» — kâne, ismi müstetir.", segments=fa("يَكُونُ", "kana", "verb")),
  tok("مَرْفُوعَ", "marfu", "noun", [K, "kana-wa-akhawatuha", ID, "ism-maful"], "خَبَرُ يَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — إِضَافَةٌ لَفْظِيَّةٌ.", "«in rafʿ» — the khabar of kāna, annexed.", "«merfû» — kâne'nin haberi, muzâf."),
  tok("الْمَحَلِّ", "mahall", "noun", [K, ID, "idafa-lafziyya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«in place»", "«mahalli»"),
  *ala_annahu(),
  tok("نَائِبُ", "naib", "noun", [K, "inna-wa-akhawatuha", ID, "naib-al-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ، مُضَافٌ.", "«the deputy of» — the khabar of أَنَّ.", "«nâibi» — enne'nin haberi."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer»", "«fâilin»", punct="،"),
  nahw(),
  tok("مُرَّ", "marra", "verb", [K, "naib-al-fail", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مُضَاعَفٌ — وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«was passed» — the passive of a doubled verb; its deputy is the phrase after it.", "«geçildi» — muzâaf fiilin meçhulü; nâibi sonraki câr-mecrûr."),
  bizayd(ar="الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ لَفْظًا — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", en="«by Zayd» — the phrase is the deputy doer, in the place of rafʿ.", tr="«Zeyd'e» — câr-mecrûr ref' mahallinde nâib-i fâil.", punct=".", tags=["naib-al-fail"]),
 ]})

# ----------- s10 — fronting
S.append({"id": "s10", "translation": {"en": "And the phrase — other than this one — may be put before what it hangs on, as in «by Zayd I passed».", "tr": "Bunun dışındakinin müteallakından önce getirilmesi câizdir; meselâ بِزَيْدٍ مَرَرْتُ."},
 "tokens": [
  tok("وَيَجُوزُ", "jaaza", "verb", [K, "fail", "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("تَقْدِيمُ", "taqdim", "noun", [K, "fail", ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the fronting of» — the doer, annexed.", "«öne alınması» — fâil, muzâf."),
  ma_maws_j(), ada_v(),
  tok("هٰذَا", "hadha", "pron", [K, "istithna", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولُ عَدَا.", "«this one» — the object of ʿadā.", "«bu» — adâ'nın mef'ûlü."),
  ala(),
  tok("مُتَعَلَّقِهِ", "mutaallaq", "noun", [K, HJ, ID, ZL], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what it hangs on»", "«müteallakı»", punct="،", segments=[seg("مُتَعَلَّقِ", "mutaallaq", "noun"), pr3msi()]),
  nahw(),
  bizayd(ar="الْبَاءُ حَرْفُ جَرٍّ، وَزَيْدٍ مَجْرُورٌ — مَفْعُولٌ بِهِ غَيْرُ صَرِيحٍ مُقَدَّمٌ عَلَى عَامِلِهِ.", en="«by Zayd» — the phrase fronted before its governor.", tr="«Zeyd'e» — âmilinden önce getirilmiş."),
  marartu(punct="."),
 ]})

# ----------- s11 — the omitted muta'allaq: zarf mustaqarr
S.append({"id": "s11", "translation": {"en": "And sometimes what the phrase hangs on is omitted: if what is omitted is a general verb contained in the governing letter and its majrūr, the two are called a settled ẓarf — as in «Zayd is in the house», that is, «came to be»;", "tr": "Bazen müteallak hazfedilir: hazfedilen, câr ile mecrûrun içinde bulunan umumî bir fiil ise ikisine zarf-ı müstakar denir — meselâ زَيْدٌ فِي الدَّارِ, yani حَصَلَ;"},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَقْلِيلٍ.", "«and sometimes»", "«ve bazen»", segments=wa("قَدْ", "qad", "part")),
  tok("يُحْذَفُ", "hadhafa", "verb", [K, "naib-al-fail", HT], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is omitted» — passive.", "«hazfedilir» — meçhul."),
  tok("الْمُتَعَلَّقُ", "mutaallaq", "noun", [K, "naib-al-fail", ZL], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ.", "«what it hangs on» — the deputy doer.", "«müteallak» — nâib-i fâil.", punct="،"),
  *in_kana("فَإِنْ")[:2],
  tok("الْمَحْذُوفُ", "mahdhuf", "noun", [K, "kana-wa-akhawatuha", HT, "ism-maful"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«what is omitted» — the ism of kāna.", "«mahzûf olan» — kâne'nin ismi."),
  tok("فِعْلًا", "fil", "noun", [K, "kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a verb» — the khabar of kāna.", "«bir fiil» — kâne'nin haberi."),
  tok("عَامًّا", "amm", "noun", [K, NA, "doubled-verbs"], "صِفَةٌ لِفِعْلًا مَنْصُوبَةٌ.", "«general» — the naʿt.", "«umumî» — sıfat."),
  tok("مُتَضَمِّنًا", "mutadammin", "noun", [K, NA, "ism-fail"], "صِفَةٌ ثَانِيَةٌ مَنْصُوبَةٌ — اسْمُ فَاعِلٍ.", "«contained» — a second naʿt.", "«mündemiç» — ikinci sıfat."),
  fi(),
  tok("الْجَارِّ", "jarr-letter", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«the governing letter»", "«câr»"),
  tok("وَالْمَجْرُورِ", "majrur-noun", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَالْمَجْرُورِ مَعْطُوفٌ مَجْرُورٌ.", "«and its majrūr»", "«ve mecrûrda»", segments=wa("الْمَجْرُورِ", "majrur-noun", "noun")),
  tok("يُسَمَّيَانِ", "samma", "verb", [K, "naib-al-fail", "mafulayn", "al-muthanna", "in-shartiyya"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ — جَوَابُ الشَّرْطِ بَعْدَ شَرْطٍ مَاضٍ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ.", "«the two are called» — the answer of the shart, in rafʿ after a māḍī shart; the alif its deputy.", "«ikisine denir» — mâzî şartın cevabı, merfû; elif nâib-i fâil."),
  tok("ظَرْفًا", "zarf", "noun", [K, "mafulayn", ZL], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a ẓarf» — the second object.", "«zarf» — ikinci mef'ûl."),
  tok("مُسْتَقِرًّا", "mustaqarr", "noun", [K, NA, ZL, "ism-maful"], "صِفَةٌ لِظَرْفًا مَنْصُوبَةٌ.", "«settled» — the naʿt.", "«müstakar» — sıfat.", punct="،"),
  nahw(),
  *zayd_dar(punct="،"),
  tok("أَيْ", "ay", "part", [K], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»", punct=":"),
  tok("حَصَلَ", "hasala", "verb", [K, ZL, HT], "فِعْلٌ مَاضٍ هُوَ الْمُتَعَلَّقُ الْمُقَدَّرُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«came to be» — the estimated verb the phrase hangs on.", "«hâsıl oldu» — takdir edilen müteallak.", punct="،"),
 ]})

# ----------- s12 — zarf laghw
S.append({"id": "s12", "translation": {"en": "and if it is not so, or what it hangs on is not omitted, the two are called an idle ẓarf — as in «Zayd ate in the house» and «I passed by Zayd».", "tr": "böyle değilse ya da müteallakı hazfedilmemişse ikisine zarf-ı lağv denir — meselâ زَيْدٌ فِي الدَّارِ أَكَلَ ve مَرَرْتُ بِزَيْدٍ."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("لَمْ", "lam-jazima", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-medi»"),
  tok("يَكُنْ", "kana", "verb", [K, "kana-wa-akhawatuha", "lam-jazim", "in-shartiyya"], "مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — فِعْلُ الشَّرْطِ.", "«it is» — kāna in jazm; the shart verb.", "«olmazsa» — meczûm kâne; şart fiili."),
  tok("كَذٰلِكَ", "kadhalika", "part", [K, "kana-wa-akhawatuha", "asma-al-ishara"], "الْكَافُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُنْ.", "«so» — the khabar of kāna.", "«öyle» — kâne'nin haberi."),
  aw(),
  tok("لَمْ", "lam-jazima", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not»", "«-medi»"),
  tok("يُحْذَفْ", "hadhafa", "verb", [K, "lam-jazim", "naib-al-fail", AT], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ — مَعْطُوفٌ عَلَى فِعْلِ الشَّرْطِ.", "«is omitted» — passive in jazm, joined to the shart verb.", "«hazfedilmezse» — meczûm meçhul, şart fiiline ma'tûf."),
  tok("مُتَعَلَّقُهُ", "mutaallaq", "noun", [K, "naib-al-fail", ID, ZL], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what it hangs on» — the deputy doer.", "«müteallakı» — nâib-i fâil.", segments=[seg("مُتَعَلَّقُ", "mutaallaq", "noun"), pr3ms()]),
  tok("يُسَمَّيَانِ", "samma", "verb", [K, "naib-al-fail", "mafulayn", "al-muthanna", "in-shartiyya"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ — جَوَابُ الشَّرْطِ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ.", "«the two are called» — the answer of the shart.", "«ikisine denir» — şartın cevabı."),
  tok("ظَرْفًا", "zarf", "noun", [K, "mafulayn", ZL], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a ẓarf» — the second object.", "«zarf» — ikinci mef'ûl."),
  tok("لَغْوًا", "laghw", "noun", [K, NA, ZL], "صِفَةٌ لِظَرْفًا مَنْصُوبَةٌ — مَصْدَرٌ وُصِفَ بِهِ.", "«idle» — the naʿt, a masdar used as one.", "«lağv» — sıfat, sıfat yapılmış masdar.", punct="،"),
  nahw(),
  *zayd_dar(),
  tok("أَكَلَ", "akala", "verb", [K, MK, ZL, "anwa-al-khabar"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِهِ: ظَرْفٌ لَغْوٌ.", "«ate» — the verb clause is the khabar; the phrase hangs on it: an idle ẓarf.", "«yedi» — fiil cümlesi haber; câr-mecrûr ona bağlı: zarf-ı lağv.", punct="،"),
  marartu("وَمَرَرْتُ", ar_pre="الْوَاوُ عَاطِفَةٌ، وَ"),
  bizayd(punct="."),
 ]})

# ---------------------------------------------------------------- the lexicon
CAND = {
 "shibh": G("shibh", "شِبْه", "ش ب ه", "noun", "a like, a counterpart — شِبْهُ الْفِعْلِ: what works like a verb", "benzer — şibhü'l-fiil: fiil gibi amel eden", 5, plural="أَشْبَاه"),
 "kafa": G("kafa", "كَفَى", "ك ف ي", "verb", "to suffice, be enough (كَفَى بِاللهِ: God suffices)", "yetmek, kâfi gelmek", 4),
 "hasb-enough": G("hasb-enough", "حَسْب", "ح س ب", "noun", "sufficiency — حَسْبُكَ: enough for you", "yeter — hasbüke: sana yeter", 5),
 "mustathna": G("mustathna", "الْمُسْتَثْنَى", "ث ن ي", "noun", "the excepted thing (ism mafʿūl of اِسْتَثْنَى)", "müstesnâ — istisnâ edilen", 4),
 "mansub": G("mansub", "الْمَنْصُوب", "ن ص ب", "noun", "the manṣūb — in the accusative", "mansûb — nasb halinde", 3),
 "marfu": G("marfu", "الْمَرْفُوع", "ر ف ع", "noun", "the marfūʿ — in the nominative", "merfû — ref' halinde", 3),
 "naib": G("naib", "نَائِب", "ن و ب", "noun", "a deputy — نَائِبُ الْفَاعِلِ: the deputy doer of a passive", "nâib — nâib-i fâil", 4),
 "taqdim": G("taqdim", "تَقْدِيم", "ق د م", "noun", "putting before, fronting (masdar of قَدَّمَ)", "takdim — öne alma", 5),
 "mutadammin": G("mutadammin", "مُتَضَمِّن", "ض م ن", "noun", "containing, implying (ism fāʿil of تَضَمَّنَ)", "mütezammın — içeren", 6),
 "mustaqarr": G("mustaqarr", "مُسْتَقِرّ", "ق ر ر", "noun", "settled, resting — ظَرْفٌ مُسْتَقِرٌّ: the phrase whose governor is an omitted «is / exists»", "müstakar — müteallakı mahzûf umumî fiil olan zarf", 5),
 "laghw": G("laghw", "لَغْو", "ل غ و", "noun", "idle, void — ظَرْفٌ لَغْوٌ: the phrase hanging on a stated verb", "lağv — müteallakı zikredilmiş zarf", 5),
 "khala-except": G("khala-except", "خَلَا", None, "part", "«except» — an exceptive letter, counted among the jarr letters (خَلَا زَيْدٍ); after مَا it is a verb governing naṣb", "«hariç» — istisnâ harfi, cer harfleri arasında sayılır (halâ Zeydin); mâ'dan sonra nasb eden fiildir", 5),
 "kaymah": G("kaymah", "كَيْمَهْ", None, "part", "«why?» — كَيْ governing the interrogative مَا (its alif dropped) with the hāʾ of pause", "niçin? — key + istifham mâ'sı (elifi düşmüş) + sekte hâsı", 6),
 "jarr-letter": G("jarr-letter", "الْجَارّ", "ج ر ر", "noun", "the governing letter, «the jārr» (ism fāʿil of جَرَّ) — paired with its majrūr", "câr — cer eden harf; mecrûruyla anılır", 4),
 "mahdhuf": G("mahdhuf", "الْمَحْذُوف", "ح ذ ف", "noun", "the omitted thing (ism mafʿūl of حَذَفَ)", "mahzûf — hazfedilen", 4),
 "asnada": G("asnada", "أَسْنَدَ", "س ن د", "verb", "to make rest on, to predicate of (Form IV)", "isnad etmek, dayandırmak", 5),
 "taallaqa-hang": G("taallaqa-hang", "تَعَلَّقَ", "ع ل ق", "verb", "to hang on, attach to (بِ) — of a jarr phrase on its governor", "bağlanmak, taalluk etmek (bi)", 5),
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
put_morph(mo, "kafa", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "كَفَ", "كْف", "i", "اِكْف", "كِفَايَة", "كَافٍ", "مَكْفِيّ", "كُفِيَ", "يُكْفَى", "كَفَى يَكْفِي: أَغْنَى عَنْ غَيْرِهِ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ كَفَى بِاللهِ: الْبَاءُ زَائِدَةٌ فِي الْفَاعِلِ."))
put_morph(mo, "asnada", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْنَد", "سْنِد", "أَسْنِد", "إِسْنَاد", "مُسْنِد", "مُسْنَد (إِلَيْهِ)", "أُسْنِدَ", "يُسْنَدُ", "أَسْنَدَ الْفِعْلَ إِلَى الْفَاعِلِ يُسْنِدُ: نَسَبَهُ إِلَيْهِ — مِنَ الْإِفْعَالِ."))
put_morph(mo, "taallaqa-hang", _sg.derived(_sg.B5, _sg.W5, "َ", "تَعَلَّق", "تَعَلَّق", "تَعَلَّق", "تَعَلُّق", "مُتَعَلِّق", "مُتَعَلَّق (بِهِ)", None, None, "تَعَلَّقَ الْجَارُّ بِالْفِعْلِ يَتَعَلَّقُ: ارْتَبَطَ بِهِ — لَازِمٌ، يَتَعَدَّى بِالْبَاءِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch2 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "مُتَعَلَّقُ الْجَارِّ وَمَحَلُّ الْمَجْرُورِ", "en": "What the jarr phrase hangs on, and the place of its majrūr", "tr": "Câr-mecrûrun müteallakı ve mecrûrun mahalli"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — حروف الجر ومتعلقها", "قواعد الإعراب لابن هشام — الباب الثاني: الجار والمجرور", "العوامل للبركوي"],
 "amil": "لَا بُدَّ لِهٰذِهِ الْحُرُوفِ مِنْ مُتَعَلَّقٍ — every jarr letter's phrase hangs on a governor, and the majrūr has a place beside its wording",
 "question": {
  "en": ["What does a jarr phrase HANG ON? A verb, something like a verb (the ism fāʿil and its kin) or something with a verb's meaning (a demonstrative, a kināya) — Birgivī says لَا بُدَّ, there is no escape from it. The TaalluqEngine walks the same rule: nothing hangs in the air, and the nearest governor wins.",
         "Which letters hang on NOTHING? The extra (zāʾid) letter — the bāʾ of كَفَى بِاللهِ and of بِحَسْبِكَ دِرْهَمٌ — and six more: رُبَّ, حَاشَا, خَلَا, عَدَا, لَوْلَا and لَعَلَّ. Seven in all, and the seven are the exceptions to everything that follows.",
         "What happens to the MAJRŪR of the extra letter and of رُبَّ? It stays as it was before the letter came: بِاللهِ is the doer, بِحَسْبِكَ the fronted khabar, رُبَّ رَجُلٍ a mubtada. The letter changed the ending and nothing else — which is why the engine reads the case off the SEAT and the ending off the letter separately.",
         "And of the exceptive letters, of لَوْلَا and لَعَلَّ? The majrūr of حَاشَا, خَلَا and عَدَا is like the mustathnā of إِلَّا; the majrūr of لَوْلَا and لَعَلَّ is a MUBTADA whose khabar follows — لَوْلَاكَ لَهَلَكَ زَيْدٌ (the khabar «existing» omitted), لَعَلَّ زَيْدٍ قَائِمٌ (ʿUqayl's dialect).",
         "And of the other thirteen? Its place is NAṢB, by the letter's meaning: a mafʿūl fīh when the letter is فِي or means it (صَلَّيْتُ فِي الْمَسْجِدِ / بِالْمَسْجِدِ), a mafʿūl lah when it is the lām or means it (ضَرَبْتُ زَيْدًا لِلتَّأْدِيبِ، كَيْمَهْ عَصَيْتَ), a non-explicit mafʿūl bihi under any other (مَرَرْتُ بِزَيْدٍ). Jarr in wording, naṣb in place — the two i'rabs of one word.",
         "Can the phrase be the DEPUTY DOER? Yes: when the governor is made passive and rests on the phrase, the phrase is in the place of rafʿ — مُرَّ بِزَيْدٍ. And the phrase may be FRONTED before its governor (بِزَيْدٍ مَرَرْتُ) — all but the seven.",
         "What is a ẒARF MUSTAQARR? A phrase whose governor is OMITTED and is a general verb the phrase itself implies — زَيْدٌ فِي الدَّارِ, that is حَصَلَ «came to be»: the phrase then stands as the khabar. A ẒARF LAGHW is one whose governor is stated, or omitted but not general — زَيْدٌ فِي الدَّارِ أَكَلَ, مَرَرْتُ بِزَيْدٍ. The TaalluqEngine already branches on exactly this (stated vs. omitted governor), and this chapter is where the two names come from.",
         "What does the engine READ here? The ḍabṭ engine rebuilds the quoted examples with the chapter's own doctrine: the extra bāʾ on a doer and a fronted khabar, the majrūr of لَعَلَّ as a mubtada, the passive مُرَّ with a phrase for its deputy, the fronted بِزَيْدٍ, and the two ẓarfs; the twenty letters' entries of chapter 1 are its vocabulary."],
  "tr": ["Câr-mecrûr NEYE BAĞLANIR? Bir fiile, fiil benzerine (ism-i fâil ve kardeşleri) ya da fiil manası taşıyana (işaret ismi, kinâye) — Birgivî لَا بُدَّ der, bundan kaçış yoktur. TaalluqEngine aynı kuralı yürür: hiçbir şey havada asılı kalmaz, en yakın âmil kazanır.",
         "Hangi harfler HİÇBİR ŞEYE bağlanmaz? Zâid harf — كَفَى بِاللهِ ve بِحَسْبِكَ دِرْهَمٌ'deki bâ — ve altı harf daha: رُبَّ, حَاشَا, خَلَا, عَدَا, لَوْلَا ve لَعَلَّ. Toplam yedi; bundan sonrasının istisnası bu yedidir.",
         "Zâidin ve رُبَّ'nin MECRÛRUNA ne olur? Harf gelmeden önce ne idiyse öyle kalır: بِاللهِ fâil, بِحَسْبِكَ mukaddem haber, رُبَّ رَجُلٍ mübtedâ. Harf yalnız sonu değiştirdi — motor bu yüzden hali YERDEN, sonu harften ayrı ayrı okur.",
         "İstisnâ harflerinin, لَوْلَا ve لَعَلَّ'nin mecrûru? حَاشَا, خَلَا, عَدَا'nın mecrûru إِلَّا ile müstesnâ gibidir; لَوْلَا ve لَعَلَّ'nin mecrûru haberi sonra gelen MÜBTEDÂDIR — لَوْلَاكَ لَهَلَكَ زَيْدٌ («mevcûd» haberi mahzûf), لَعَلَّ زَيْدٍ قَائِمٌ (Ukayl lügati).",
         "Diğer on üçünün? Mahalli NASBdır, harfin manasına göre: harf فِي ya da o manada ise mef'ûlün fîh (صَلَّيْتُ فِي الْمَسْجِدِ / بِالْمَسْجِدِ), lâm ya da o manada ise mef'ûlün leh (ضَرَبْتُ زَيْدًا لِلتَّأْدِيبِ، كَيْمَهْ عَصَيْتَ), başkası ise sarih olmayan mef'ûlün bih (مَرَرْتُ بِزَيْدٍ). Lafzen cer, mahallen nasb — bir kelimenin iki i'râbı.",
         "Câr-mecrûr NÂİB-İ FÂİL olur mu? Olur: âmil meçhul kılınıp câr-mecrûra isnad edilince ref' mahallinde olur — مُرَّ بِزَيْدٍ. Ve câr-mecrûr âmilinden ÖNE alınabilir (بِزَيْدٍ مَرَرْتُ) — yedi hariç.",
         "ZARF-I MÜSTAKAR nedir? Âmili HAZFEDİLMİŞ ve câr-mecrûrun kendisinin ima ettiği umumî bir fiil olan terkip — زَيْدٌ فِي الدَّارِ, yani حَصَلَ: câr-mecrûr haber olur. ZARF-I LAĞV âmili zikredilmiş ya da umumî olmayan terkiptir — زَيْدٌ فِي الدَّارِ أَكَلَ, مَرَرْتُ بِزَيْدٍ. TaalluqEngine tam bu ayrımla dallanır (zikredilen / hazfedilen âmil); iki ismin kaynağı bu babdır.",
         "Motor burada neyi OKUR? Dabt motoru hikâye edilen örnekleri babın doktriniyle kurar: fâil ve mukaddem haber üstündeki zâid bâ, لَعَلَّ'nin mecrûru mübtedâ, nâibi câr-mecrûr olan meçhul مُرَّ, öne alınmış بِزَيْدٍ ve iki zarf; birinci babın yirmi harfi bunların sözlüğüdür."]},
 "plain": {
  "en": "A jarr phrase always hangs on a verb or a verb-like word, except seven letters that hang on nothing. Its noun is majrūr in wording but takes a place by the letter's meaning: in, for, or by. With no governor stated the phrase is a settled ẓarf (an omitted «is»); with one stated, an idle ẓarf.",
  "tr": "Câr-mecrûr daima bir fiile ya da fiil benzerine bağlanır; yedi harf hiçbir şeye bağlanmaz. İsmi lafzen mecrûrdur, mahalli ise harfin manasına göredir: -de, için, ile. Âmil zikredilmemişse zarf-ı müstakar (mahzûf «vardır»), zikredilmişse zarf-ı lağvdır."},
 "explanation": {
  "en": "وَلَا بُدَّ لِهٰذِهِ الْحُرُوفِ مِنْ مُتَعَلَّقٍ: فِعْلٍ أَوْ شِبْهِهِ أَوْ مَعْنَاهُ. The second thing the Iẓhār does with the twenty letters is to say what their phrase hangs on and where their noun stands. The hanging is the Qawāʿid al-Iʿrāb's doctrine of taʿalluq, stated as a necessity: a verb, a verb-like noun, or a word with a verb's meaning — and the seven that attach to nothing are listed by name, with the extra letter at their head. Then the majrūr is given its PLACE: unchanged after the extra letter and رُبَّ, like the excepted after the exceptive letters, a mubtada after لَوْلَا and لَعَلَّ, and after the other thirteen a seat decided by the letter's meaning — the mafʿūl fīh of فِي, the mafʿūl lah of the lām, the non-explicit object of the rest. The phrase can carry the passive's deputy (مُرَّ بِزَيْدٍ) and can be fronted. Last come the two names every later book uses: the ẓarf mustaqarr, whose omitted governor is a general verb the phrase implies, and the ẓarf laghw, whose governor is stated.",
  "tr": "وَلَا بُدَّ لِهٰذِهِ الْحُرُوفِ مِنْ مُتَعَلَّقٍ: فِعْلٍ أَوْ شِبْهِهِ أَوْ مَعْنَاهُ. İzhâr'ın yirmi harfle yaptığı ikinci iş, terkiplerinin neye bağlandığını ve isimlerinin nerede durduğunu söylemektir. Bağlanma Kavâidü'l-İ'râb'ın taalluk doktrinidir, zaruret olarak söylenir: bir fiil, fiil benzeri isim ya da fiil manalı kelime — hiçbir şeye bağlanmayan yedi, başta zâid harf olmak üzere adıyla sayılır. Sonra mecrûra YERİ verilir: zâidden ve رُبَّ'den sonra değişmez, istisnâ harflerinden sonra müstesnâ gibi, لَوْلَا ve لَعَلَّ'den sonra mübtedâ, diğer on üçten sonra harfin manasının belirlediği yer — فِي'nin mef'ûlün fîhi, lâmın mef'ûlün lehi, kalanının sarih olmayan mef'ûlü. Terkip meçhulün nâibini taşıyabilir (مُرَّ بِزَيْدٍ) ve öne alınabilir. En sonda sonraki her kitabın kullandığı iki ad gelir: hazfedilmiş âmili terkibin ima ettiği umumî fiil olan zarf-ı müstakar ve âmili zikredilmiş zarf-ı lağv."},
 "examples": [
  {"ar": "وَلَا بُدَّ لِهٰذِهِ الْحُرُوفِ مِنْ مُتَعَلَّقٍ: فِعْلٍ أَوْ شِبْهِهِ أَوْ مَعْنَاهُ", "en": "The necessity of a governor.", "tr": "Müteallakın zarureti.", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "فَمَجْرُورُ الزَّائِدِ وَرُبَّ بَاقٍ عَلَى مَا كَانَ عَلَيْهِ قَبْلَ دُخُولِهِمَا", "en": "The extra letter changes the ending only.", "tr": "Zâid harf yalnız sonu değiştirir.", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "لَوْلَاكَ لَهَلَكَ زَيْدٌ، وَلَعَلَّ زَيْدٍ قَائِمٌ", "en": "The majrūr of lawlā and laʿalla as a mubtada.", "tr": "Levlâ ve lealle'nin mecrûru mübtedâ.", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "صَلَّيْتُ فِي الْمَسْجِدِ أَوْ بِالْمَسْجِدِ", "en": "The mafʿūl fīh under fī and under a bāʾ meaning it.", "tr": "Fî ve fî manasındaki bâ altında mef'ûlün fîh.", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "مُرَّ بِزَيْدٍ", "en": "The phrase as the passive's deputy doer.", "tr": "Câr-mecrûr meçhulün nâib-i fâili.", "sourceStory": "izhar-al-asrar", "sentence": "s9"},
  {"ar": "زَيْدٌ فِي الدَّارِ، أَيْ: حَصَلَ — زَيْدٌ فِي الدَّارِ أَكَلَ", "en": "The settled ẓarf and the idle one.", "tr": "Zarf-ı müstakar ve zarf-ı lağv.", "sourceStory": "izhar-al-asrar", "sentence": "s11"}],
 "commonMistakes": [
  {"wrong": "«كَفَى بِاللهِ'de Allah lafzı mecrûrdur, fâil gizlidir»",
   "right": "«Bâ zâiddir: lafza-i celâl lafzen mecrûr, mahallen merfû FÂİLDİR»",
   "why": {"en": "The extra letter changes only the ending; the majrūr keeps the seat it had before the letter came.", "tr": "Zâid harf yalnız sonu değiştirir; mecrûr harften önceki yerini korur."}},
  {"wrong": "«Her câr-mecrûr mahallen mansûbdur»",
   "right": "«Yedi harfin mecrûru hariç: zâid ve رُبَّ'ninki olduğu gibi kalır, istisnâ harflerininki müstesnâ gibidir, لَوْلَا ve لَعَلَّ'ninki mübtedâdır»",
   "why": {"en": "The place is decided by the letter's meaning, and the seven are named exceptions.", "tr": "Mahalli harfin manası belirler; yedisi adıyla sayılmış istisnâdır."}},
  {"wrong": "«زَيْدٌ فِي الدَّارِ أَكَلَ'de فِي الدَّارِ haberdir, أَكَلَ hâldir»",
   "right": "«أَكَلَ haberdir; فِي الدَّارِ ona bağlı zarf-ı LAĞVdır»",
   "why": {"en": "A stated governor makes the phrase an idle ẓarf; only an omitted general verb makes it the settled khabar.", "tr": "Zikredilen âmil terkibi lağv kılar; yalnız hazfedilmiş umumî fiil onu müstakar haber yapar."}},
  {"wrong": "«مُرَّ بِزَيْدٍ'de Zeyd mef'ûldür»",
   "right": "«Câr-mecrûr ref' mahallinde NÂİB-İ FÂİLDİR»",
   "why": {"en": "The passive rests on the phrase itself, so the phrase takes the deputy's place.", "tr": "Meçhul terkibin kendisine isnad edilir; terkip nâibin yerini alır."}}],
 "relatedNotes": [K1, ZL, "huruf-jarr", "huruf-jarr-nawadir", "maful-fih", "maful-lah", "naib-al-fail", "hadhf-wa-taqdir"]}

ADD_EN = (" Chapter 2 (print pp. 89-91): the necessity of a governor and the seven letters that attach to nothing (s1-s2), the majrur's place after "
          "the extra letter and rubba (s3), after the exceptive letters (s4), after lawla and la'alla (s5), and after the other thirteen — maf'ul fih, "
          "maf'ul lah, the non-explicit object (s6-s8); the phrase as the passive's deputy (s9) and fronted (s10); the zarf mustaqarr and the zarf "
          "laghw (s11-s12).")
ADD_TR = (" İkinci bab (baskı s. 89-91): müteallakın zarureti ve hiçbir şeye bağlanmayan yedi harf (s1-s2), mecrûrun zâid ve rubbe'den sonraki (s3), "
          "istisnâ harflerinden sonraki (s4), levlâ ve lealle'den sonraki (s5), diğer on üçten sonraki yeri — mef'ûlün fîh, mef'ûlün leh, sarih olmayan "
          "mef'ûl (s6-s8); câr-mecrûr nâib-i fâil (s9) ve öne alınmış (s10); zarf-ı müstakar ve zarf-ı lağv (s11-s12).")
write_out(2, S, TITLE, ADD_EN, ADD_TR, "pp. 89-91", GLOSS_ADD, notes=(NOTE,),
          related=((ZL, [K]), ("huruf-jarr", [K]), ("huruf-jarr-nawadir", [K]), ("naib-al-fail", [K]), (K1, [K])))
report(2, S, GLOSS_ADD, (NOTE,))
