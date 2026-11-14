# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 5: where أَنَّ takes the FATHA (as a doer, an object, a mubtada, a muḍāf ilayh; after
# لَوْ / لَوْلَا, after the مَا of time, after a jarr letter, after the joining حَتَّى, after مُذْ / مُنْذُ); where both readings
# stand (after the fāʾ of the answer); the LIGHTENED إِنْ with its lām and the verbs of the mubtada (2:143, 26:186); the
# lightened أَنْ with the concealed pronoun of the matter, needing a verb of certainty before it and لَا / the sīn / سَوْفَ /
# قَدْ before a conjugable verb (73:20), none before a frozen verb, a condition or a prayer (7:185, 34:14, 24:9); the
# lightened كَأَنْ and لٰكِنْ. Print pp. 96–98.
#   python3 author_izhar_ch5.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "mawadi-fath-anna"
K4 = "mawadi-kasr-inna"
K1 = "al-amil-wa-aqsamuh"
IW = "inna-wa-akhawatuha"; IA = "inna-am-anna"; AM = "an-masdariyya"
TITLE = {"ar": "مَوَاضِعُ فَتْحِ أَنَّ، وَمَا جَازَ فِيهِ الْوَجْهَانِ، وَتَخْفِيفُ إِنَّ وَأَنَّ وَكَأَنَّ وَلٰكِنَّ", "en": "Where أَنَّ takes the fatḥa, where both readings stand, and the lightened إِنْ / أَنْ / كَأَنْ / لٰكِنْ", "tr": "Enne'nin fetha yerleri, iki vechin câiz olduğu yer, ve inne / enne / keenne / lâkinne'nin tahfifi"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; IQ = "al-iqtibas-wal-tadmin"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; ZN = "zanna-wa-akhawatuha"; SH = "in-shartiyya"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def cite_quran(punct=":", wa=False):
    first = tok("وَقَوْلِهِ" if wa else "قَوْلِهِ", "qawl", "noun", [K, ID, IQ] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَقَوْلِهِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ." if wa else "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ."), "«His word»" if not wa else "«and His word»", "«O'nun sözü»", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("قَوْلِ", "qawl", "noun"), pr3msi()])
    out = [] if wa else [tok("نَحْوَ", "nahwa", "noun", [K, MF, HT, ID, IQ], "مَفْعُولٌ فِيهِ مَنْصُوبٌ — ظَرْفٌ بِمَعْنَى مِثْلَ، مُضَافٌ.", "«as in» — the citation ẓarf, annexed.", "«meselâ» — iktibas zarfı, muzâf.")]
    return out + [first, tok("تَعَالَى", "taala", "verb", [K, IQ, "ism-maqsur-manqus"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«Exalted is He»", "«yüce»", punct=punct)]
def ay(punct=":"): return tok("أَيْ", "ay", "part", [K, HT, "amma-tafsiliyya"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani».", punct=punct)
def wabada(): return tok("وَبَعْدَ", "bada", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَعْدَ ظَرْفٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى فَاعِلَةً فِي الْمَعْنَى، مُضَافٌ.", "«and after» — the ẓarf, annexed.", "«ve sonra» — zarf, muzâf.", segments=wa("بَعْدَ", "bada", "noun"))
def anna(full="أَنَّ", pre_ar="", pre_en="", pre_tr="", extra=(), segs=None, punct=None):
    return tok(full, "anna", "part", [K, IW, IA] + list(extra), pre_ar + "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، مَفْتُوحَةُ الْهَمْزَةِ لِأَنَّهَا مَعَ جُمْلَتِهَا فِي حُكْمِ الْمَصْدَرِ.", pre_en + "«that» — anna with its fatḥa: the clause is a maṣdar.", pre_tr + "«-dığı» — hemzesi fethalı enne: cümle masdar hükmünde.", segments=segs, punct=punct)
def annaka(extra=()): return anna("أَنَّكَ", pre_ar="", extra=list(extra), segs=[seg("أَنَّ", "anna", "part"), seg("كَ", "pron-2ms", "pron")])
def qaim_anna(punct=None, who="كَ"): return tok("قَائِمٌ", "qaim", "noun", [K, IW, "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«standing» — the khabar of anna.", "«ayakta» — enne'nin haberi.", punct=punct)
def zaydan_anna(): return tok("زَيْدًا", "zayd", "propn", [K, IW], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the ism of anna.", "«Zeyd» — enne'nin ismi.")
def hal_x(full, lex, ar, en, tr, punct=None, extra=(), segs=None):
    """فَاعِلَةً — the ḥāl that names the seat"""
    return tok(full, lex, "noun", [K, "hal"] + list(extra), ar, en, tr, punct=punct, segments=segs)
def lil_fath(seat_ar, seat_en, seat_tr): pass

# ----------- s1 — the fath places 1-4: doer, object, mubtada, mudaf ilayh
S.append({"id": "s1", "translation": {"en": "And it takes the fatḥa as a doer — as in «it reached me that you are standing» — as an object — as in «I knew that Zayd is standing» — as a mubtada — as in «with me is that you are standing» — and annexed to — as in «sit where Zayd is sitting»,", "tr": "Fâil olarak fethalanır — «bana ulaştı ki sen ayaktasın» gibi; mef'ûl olarak — «bildim ki Zeyd ayaktadır» gibi; mübtedâ olarak — «yanımda olan, senin ayakta olmandır» gibi; muzâfun ileyh olarak — «Zeyd'in oturduğu yerde otur» gibi;"},
 "tokens": [
  tok("وَفُتِحَتْ", "fataha", "verb", [K, "naib-al-fail", AT], "الْوَاوُ عَاطِفَةٌ، وَفُتِحَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — أَنَّ.", "«and it takes the fatḥa» — the passive; its deputy doer is anna.", "«ve fethalanır» — meçhul; nâib-i fâil enne.", segments=wa("فُتِحَتْ", "fataha", "verb")),
  hal_x("فَاعِلَةً", "fail-doer", "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: حَالَ كَوْنِهَا فَاعِلَةً.", "«as a doer» — the ḥāl.", "«fâil olarak» — hâl."),
  nahw(),
  tok("بَلَغَنِي", "balagha", "verb", [K, MB, FL], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فَاعِلٌ.", "«it reached me» — the yāʾ its object; the clause after it is the doer.", "«bana ulaştı» — yâ mef'ûl; ardındaki cümle fâil.", segments=[seg("بَلَغَ", "balagha", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  annaka(extra=[FL]),
  qaim_anna(punct="،"),
  tok("وَمَفْعُولَةً", "maful-object", "noun", [K, AT, "hal"], "الْوَاوُ عَاطِفَةٌ، وَمَفْعُولَةً مَعْطُوفٌ عَلَى فَاعِلَةً مَنْصُوبٌ.", "«and as an object»", "«ve mef'ûl olarak»", segments=wa("مَفْعُولَةً", "maful-object", "noun")),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, FL, ZN, "mafulayn"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْهِ.", "«I knew» — the clause stands for its two objects.", "«bildim» — cümle iki mef'ûlün yerini tutar.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  anna(extra=[ZN, MB]),
  zaydan_anna(),
  qaim_anna(punct="،"),
  tok("وَمُبْتَدَأَةً", "mubtada", "noun", [K, AT, "hal"], "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأَةً مَعْطُوفٌ مَنْصُوبٌ.", "«and as a mubtada»", "«ve mübtedâ olarak»", segments=wa("مُبْتَدَأَةً", "mubtada", "noun")),
  nahw(),
  tok("عِنْدِي", "inda", "noun", [K, MF, ID, MK, "ya-al-mutakallim"], "ظَرْفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«with me» — the fronted khabar.", "«yanımda» — mukaddem haber.", segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  annaka(extra=[MK]),
  qaim_anna(punct="،"),
  tok("وَمُضَافًا", "mudaf", "noun", [K, AT, "hal"], "الْوَاوُ عَاطِفَةٌ، وَمُضَافًا مَعْطُوفٌ مَنْصُوبٌ.", "«and annexed»", "«ve muzâf olarak»", segments=wa("مُضَافًا", "mudaf", "noun")),
  tok("إِلَيْهَا", "ila", "prep", [K, HJ], "إِلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِمُضَافًا.", "«to it»", "«ona»", segments=[seg("إِلَيْ", "ila", "prep"), pr3fs()]),
  nahw(),
  tok("اجْلِسْ", "jalasa", "verb", [K, "imperative-amr", FL], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«sit»", "«otur»"),
  tok("حَيْثُ", "haythu", "noun", [K, MF, ID, "al-murab-wal-mabni-wal-irab"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ.", "«where» — the mabnī ẓarf, annexed to the clause.", "«… yerde» — mebnî zarf, cümleye muzâf."),
  anna(extra=[ID]),
  zaydan_anna(),
  tok("جَالِسٌ", "jalis-sitting", "noun", [K, IW, "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«sitting» — the khabar of anna.", "«oturuyor» — enne'nin haberi.", punct="،"),
 ]})
# ----------- s2 — after law, after lawla
S.append({"id": "s2", "translation": {"en": "and after لَوْ — as in «had you been standing, such-and-such would have been», that is: had your standing been established — and after لَوْلَا — as in «were it not that you are going, such-and-such would have been», that is: were your going not present,", "tr": "lev'den sonra — «sen ayakta olsaydın şöyle olurdu» gibi, yani: ayakta olman sâbit olsaydı; levlâ'dan sonra — «sen gidiyor olmasaydın şöyle olurdu» gibi, yani: gidişin mevcut olmasaydı;"},
 "tokens": [
  wabada(),
  tok("لَوْ", "law", "part", [K, ID, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«law» — quoted; the muḍāf ilayh.", "«lev» — hikâye edilmiş; muzâfun ileyh."),
  nahw(),
  tok("لَوْ", "law", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ لِامْتِنَاعِ الثَّانِي لِامْتِنَاعِ الْأَوَّلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ: لَوْ ثَبَتَ.", "«had» — the clause after it is the doer of a dropped «were established».", "«-saydı» — ardındaki cümle mahzûf «sâbit olsaydı»nın fâili."),
  annaka(extra=[FL, "in-shartiyya"]),
  qaim_anna(),
  tok("لَكَانَ", "kana", "verb", [K, KN, "in-shartiyya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«would have been» — the lām of law's answer.", "«olurdu» — lev'in cevabının lâmı.", segments=[seg("لَ", "lam-jawab", "part"), seg("كَانَ", "kana", "verb")]),
  tok("كَذَا", "kadha", "pron", [K, KN, "asma-al-ishara"], "خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ — كِنَايَةٌ عَنِ الشَّيْءِ.", "«such-and-such» — the khabar of kāna.", "«şöyle» — kâne'nin haberi.", punct="،"),
  ay(),
  tok("لَوْ", "law", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ.", "«had»", "«-saydı»"),
  tok("ثَبَتَ", "thabata", "verb", [K, FL, "in-shartiyya"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«were established» — the condition's verb.", "«sâbit olsaydı» — şart fiili."),
  tok("قِيَامُكَ", "qiyam", "noun", [K, FL, ID, "masdar"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your standing» — the doer.", "«ayakta olman» — fâil.", punct="،", segments=[seg("قِيَامُ", "qiyam", "noun"), seg("كَ", "pron-2ms", "pron")]),
  wabada(),
  tok("لَوْلَا", "lawla", "part", [K, ID, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«lawlā» — quoted; the muḍāf ilayh.", "«levlâ» — hikâye edilmiş; muzâfun ileyh."),
  nahw(),
  tok("لَوْلَا", "lawla", "part", [K, MK, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِوُجُودٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ: مَوْجُودٌ.", "«were it not» — the clause after it is a mubtada whose khabar «present» is dropped.", "«olmasaydı» — ardındaki cümle, haberi «mevcut» mahzûf bir mübtedâ."),
  annaka(extra=[MK, "in-shartiyya"]),
  tok("ذَاهِبٌ", "dhahib", "noun", [K, IW, "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«going» — the khabar of anna.", "«gidiyor» — enne'nin haberi."),
  tok("لَكَانَ", "kana", "verb", [K, KN, "in-shartiyya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْلَا، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«would have been»", "«olurdu»", segments=[seg("لَ", "lam-jawab", "part"), seg("كَانَ", "kana", "verb")]),
  tok("كَذَا", "kadha", "pron", [K, KN, "asma-al-ishara"], "خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ.", "«such-and-such»", "«şöyle»", punct="،"),
  ay(),
  tok("لَوْلَا", "lawla", "part", [K, MK, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِوُجُودٍ.", "«were it not»", "«olmasaydı»"),
  tok("ذَهَابُكَ", "dhahab-going", "noun", [K, MK, ID, "masdar"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your going» — the mubtada.", "«gidişin» — mübtedâ.", segments=[seg("ذَهَابُ", "dhahab-going", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("مَوْجُودٌ", "mawjud", "noun", [K, MK, "ism-maful"], "خَبَرٌ مَرْفُوعٌ — وَهُوَ الْخَبَرُ الَّذِي يُحْذَفُ بَعْدَ لَوْلَا وُجُوبًا.", "«present» — the khabar that lawlā always drops.", "«mevcut» — levlâ'dan sonra vâcip olarak hazfedilen haber.", punct="،"),
 ]})
# ----------- s3 — after the ma of time
S.append({"id": "s3", "translation": {"en": "and after the مَا of time that makes a maṣdar — because it is a doer, since that مَا belongs only with a verb — as in «sit as long as Zayd is standing», that is: as long as it is established that Zayd is standing, meaning: for the duration of Zayd's standing being established,", "tr": "zaman bildiren masdariyye mâ'dan sonra — zira o fâildir, çünkü masdariyye mâ yalnız fiille olur — «Zeyd ayakta olduğu sürece otur» gibi, yani: Zeyd'in ayakta olduğu sâbit olduğu sürece, Zeyd'in ayakta durmasının sübûtu müddetince mânâsında;"},
 "tokens": [
  wabada(),
  tok("مَا", "ma-masdariyya", "part", [K, ID, HT, AM], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«mā» — quoted; the muḍāf ilayh.", "«mâ» — hikâye edilmiş; muzâfun ileyh."),
  tok("الْمَصْدَرِيَّةِ", "masdari", "noun", [K, NA, "ism-mansub"], "نَعْتٌ مَجْرُورٌ — مَنْسُوبٌ إِلَى الْمَصْدَرِ.", "«that makes a maṣdar» — the naʿt.", "«masdariyye» — sıfat."),
  tok("التَّوْقِيتِيَّةِ", "tawqiti", "noun", [K, NA, "ism-mansub"], "نَعْتٌ ثَانٍ مَجْرُورٌ — مَنْسُوبٌ إِلَى التَّوْقِيتِ.", "«of time» — a second naʿt.", "«tevkîtiyye» — ikinci sıfat."),
  tok("لِأَنَّهُ", "anna", "part", [K, HJ, IW, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«because it» — the lām of cause; the hā the ism of anna.", "«zira o» — ta'lîl lâmı; hâ enne'nin ismi.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  tok("فَاعِلٌ", "fail-doer", "noun", [K, IW], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«a doer» — the khabar of anna.", "«fâildir» — enne'nin haberi."),
  tok("لِاخْتِصَاصِ", "ikhtisas", "noun", [K, HJ, ID, "masdar", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَاخْتِصَاصِ مَجْرُورٌ، مُضَافٌ.", "«because of the belonging of»", "«hâs olması sebebiyle»", segments=[seg("لِ", "li", "prep"), seg("اخْتِصَاصِ", "ikhtisas", "noun")]),
  tok("مَا", "ma-masdariyya", "part", [K, ID, HT, AM], "لَفْظٌ مَحْكِيٌّ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«mā» — quoted; the muḍāf ilayh.", "«mâ» — muzâfun ileyh."),
  tok("الْمَصْدَرِيَّةِ", "masdari", "noun", [K, NA, "ism-mansub"], "نَعْتٌ مَجْرُورٌ.", "«that makes a maṣdar»", "«masdariyye»"),
  tok("بِالْفِعْلِ", "fil", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفِعْلِ مَجْرُورٌ — مُتَعَلِّقٌ بِاخْتِصَاصِ.", "«with the verb»", "«fiile»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْفِعْلِ", "fil", "noun")]),
  nahw(),
  tok("اجْلِسْ", "jalasa", "verb", [K, "imperative-amr", FL], "فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«sit»", "«otur»"),
  tok("مَا", "ma-masdariyya", "part", [K, AM, MF], "حَرْفٌ مَصْدَرِيٌّ تَوْقِيتِيٌّ — أَيْ: مُدَّةَ.", "«as long as» — the mā of time: «for the duration».", "«-dığı sürece» — tevkît mâ'sı: «müddetince»."),
  anna(extra=[AM, FL]),
  zaydan_anna(),
  qaim_anna(punct="،"),
  ay(),
  tok("مَا", "ma-masdariyya", "part", [K, AM, MF], "حَرْفٌ مَصْدَرِيٌّ تَوْقِيتِيٌّ.", "«as long as»", "«-dığı sürece»"),
  tok("ثَبَتَ", "thabata", "verb", [K, FL, AM], "فِعْلٌ مَاضٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فَاعِلٌ.", "«it is established» — the clause after it is the doer.", "«sâbit oldu» — ardındaki cümle fâil."),
  anna(extra=[FL]),
  zaydan_anna(),
  qaim_anna(punct="،"),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«in the sense of»", "«mânâsında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("مُدَّةَ", "mudda", "noun", [K, ID, MF, HT], "مُضَافٌ إِلَيْهِ مَحْكِيٌّ عَلَى نَصْبِهِ — ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the duration of» — quoted with its naṣb, the time ẓarf, annexed.", "«müddetince» — nasbıyla hikâye edilmiş zaman zarfı, muzâf."),
  tok("ثُبُوتِ", "thubut", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the being-established of»", "«sübûtu»"),
  tok("قِيَامِ", "qiyam", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the standing of»", "«ayakta durmasının»"),
  tok("زَيْدٍ", "zayd", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd»", "«Zeyd'in»", punct="،"),
 ]})
# ----------- s4 — after the jarr letters, the joining hatta, mudh / mundhu
S.append({"id": "s4", "translation": {"en": "and after the jarr letters — as in «I marvelled at your standing» — and after the حَتَّى that joins a single word — as in «I came to know your affairs, even that you are righteous» — and after مُذْ and مُنْذُ — as in «I have not seen him since you have been standing».", "tr": "cer harflerinden sonra — «ayakta olmana şaştım» gibi; müfrede atfeden hattâ'dan sonra — «işlerini öğrendim, hattâ sâlih olduğunu» gibi; müz ve münzü'den sonra — «sen ayakta olalı onu görmedim» gibi."},
 "tokens": [
  wabada(),
  tok("حُرُوفِ", "harf", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the letters of»", "«harflerinden»"),
  tok("الْجَرِّ", "jarr", "noun", [K, ID, HJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr»", "«cer»"),
  nahw(),
  tok("عَجِبْتُ", "ajiba", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I marvelled»", "«şaştım»", segments=[seg("عَجِبْ", "ajiba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فِي مَحَلِّ جَرٍّ.", "«at» — the clause after it in the place of jarr.", "«-e» — ardındaki cümle cer mahallinde."),
  annaka(extra=[HJ]),
  qaim_anna(punct="،"),
  wabada(),
  tok("حَتَّى", "hatta", "part", [K, ID, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«ḥattā» — quoted; the muḍāf ilayh.", "«hattâ» — hikâye edilmiş; muzâfun ileyh."),
  tok("الْعَاطِفَةِ", "atif", "noun", [K, NA, AT, "ism-fail"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلٍ.", "«that joins» — the naʿt.", "«atfeden» — sıfat."),
  tok("لِلْمُفْرَدِ", "mufrad", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُفْرَدِ مَجْرُورٌ — مُتَعَلِّقٌ بِالْعَاطِفَةِ.", "«a single word»", "«müfrede»", segments=[seg("لِ", "li", "prep"), seg("الْمُفْرَدِ", "mufrad", "noun")]),
  nahw(),
  tok("عَرَفْتُ", "arafa", "verb", [K, FL, MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I came to know»", "«öğrendim»", segments=[seg("عَرَفْ", "arafa", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أُمُورَكَ", "amr-noun", "noun", [K, MB, ID, "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your affairs» — the object.", "«işlerini» — mef'ûl.", segments=[seg("أُمُورَ", "amr-noun", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("حَتَّى", "hatta", "part", [K, AT], "حَرْفُ عَطْفٍ — يَعْطِفُ الْمَصْدَرَ الْمُؤَوَّلَ عَلَى أُمُورَكَ.", "«even» — the joining ḥattā: the clause is joined to «your affairs».", "«hattâ» — atıf harfi: cümle «işlerini»ye ma'tûf."),
  annaka(extra=[AT]),
  tok("صَالِحٌ", "salih", "noun", [K, IW, "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«righteous» — the khabar of anna.", "«sâlih» — enne'nin haberi.", punct="،"),
  wabada(),
  tok("مُذْ", "mudh", "prep", [K, ID, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«mudh» — quoted; the muḍāf ilayh.", "«müz» — hikâye edilmiş."),
  tok("وَمُنْذُ", "mundhu", "prep", [K, AT, HT], "الْوَاوُ عَاطِفَةٌ، وَمُنْذُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and mundhu»", "«ve münzü»", segments=wa("مُنْذُ", "mundhu", "prep")),
  nahw(),
  tok("مَا", "ma-nafiya", "part", [K, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not»", "«-medim»"),
  tok("رَأَيْتُهُ", "raa", "verb", [K, FL, MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I have seen him»", "«onu gördüm»", segments=[seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron"), pr3ms()]),
  tok("مُذْ", "mudh", "prep", [K, HJ, MF], "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ فِي الزَّمَانِ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فِي مَحَلِّ جَرٍّ.", "«since» — the clause after it in the place of jarr.", "«-den beri» — ardındaki cümle cer mahallinde."),
  annaka(extra=[HJ]),
  qaim_anna(punct="."),
 ]})
# ----------- s5 — where both readings stand: after the fa of the answer
S.append({"id": "s5", "translation": {"en": "And wherever the two estimations are allowed, the two readings are allowed — like the one that stands after the fāʾ of the answer, as in «whoever honours me, I honour him»: if it is read with the kasra the sense is «then I honour him», and if with the fatḥa the sense is «then my honouring him is settled».", "tr": "İki takdirin câiz olduğu her yerde iki vecih de câizdir — cezâ fâsından sonra gelen gibi: «kim bana ikram ederse ben de ona ikram ederim»; kesre ile okunursa mânâ «ben de ona ikram ederim», fetha ile okunursa mânâ «ona ikramım sâbittir»."},
 "tokens": [
  tok("وَحَيْثُ", "haythu", "noun", [K, MF, "in-shartiyya", "al-murab-wal-mabni-wal-irab"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَحَيْثُ ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and wherever» — the mabnī ẓarf carrying the sense of a condition.", "«ve her nerede» — şart mânâsı taşıyan mebnî zarf.", segments=wa("حَيْثُ", "haythu", "noun")),
  tok("جَازَ", "jaaza", "verb", [K, FL, "hollow-verbs"], "فِعْلٌ مَاضٍ — فِي مَحَلِّ جَرٍّ بِإِضَافَةِ حَيْثُ.", "«are allowed»", "«câiz oldu»"),
  tok("التَّقْدِيرَانِ", "taqdir", "noun", [K, FL, "al-muthanna", "masdar"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«the two estimations» — the doer, in rafʿ by the alif.", "«iki takdir» — fâil, elifle merfû."),
  tok("جَازَ", "jaaza", "verb", [K, FL, "hollow-verbs"], "فِعْلٌ مَاضٍ — جَوَابُ حَيْثُ الشَّرْطِيَّةِ.", "«are allowed» — the answer.", "«câiz olur» — cevap."),
  tok("الْأَمْرَانِ", "amr-noun", "noun", [K, FL, "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ — أَيِ: الْكَسْرُ وَالْفَتْحُ.", "«the two readings» — the doer: the kasra and the fatḥa.", "«iki vecih» — fâil: kesre ve fetha.", punct="،"),
  tok("كَالَّتِي", "allati", "pron", [K, HJ, MW, MK], "الْكَافُ حَرْفُ جَرٍّ، وَالَّتِي اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ كَالَّتِي.", "«like the one that» — the relative after the kāf.", "«… gibi» — kâf'tan sonra ism-i mevsûl.", segments=[seg("كَ", "ka", "part"), seg("الَّتِي", "allati", "pron")]),
  tok("وَقَعَتْ", "waqaa", "verb", [K, MW, FL, "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — صِلَةُ الَّتِي.", "«stands» — the ṣila.", "«bulunan» — sıla."),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  tok("فَاءِ", "fa-letter", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the fāʾ of»", "«fâsından»"),
  tok("الْجَزَاءِ", "jaza-answer", "noun", [K, ID, "in-shartiyya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the answer»", "«cezâ»"),
  nahw(),
  tok("مَنْ", "man-shart", "pron", [K, "in-shartiyya", MK], "اسْمُ شَرْطٍ جَازِمٌ، مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«whoever» — the conditional noun, the mubtada.", "«kim» — şart ismi, mübtedâ."),
  tok("يُكْرِمْنِي", "akrama", "verb", [K, "in-shartiyya", MB, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«honours me» — the condition's verb, majzūm.", "«bana ikram ederse» — şart fiili, meczûm.", segments=[seg("يُكْرِمْ", "akrama", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("فَإِنِّي", "inna", "part", [K, IW, IA, "in-shartiyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَإِنَّ حَرْفُ تَوْكِيدٍ — تُكْسَرُ أَوْ تُفْتَحُ — وَالْيَاءُ اسْمُهَا.", "«then I» — the fāʾ of the answer; inna reads with the kasra or the fatḥa.", "«ben de» — cezâ fâsı; inne kesre ile de fetha ile de okunur.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أُكْرِمُهُ", "akrama", "verb", [K, IW, MB, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I honour him» — the khabar of inna.", "«ona ikram ederim» — inne'nin haberi.", punct="،", segments=[seg("أُكْرِمُ", "akrama", "verb"), pr3ms()]),
  tok("فَإِنْ", "in-shartiyya", "part", [K, SH], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if» — the conditional.", "«eğer» — şart harfi.", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("كُسِرَتْ", "kasara", "verb", [K, SH, "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«it is read with the kasra» — the condition's verb.", "«kesrelenirse» — şart fiili."),
  tok("فَالْمَعْنَى", "mana", "noun", [K, SH, MK, "ism-maqsur-manqus"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَالْمَعْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — وَخَبَرُهُ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«the sense is» — the mubtada; its khabar the quoted sentence.", "«mânâ» — mübtedâ; haberi hikâye edilen cümle.", punct=":", segments=fa("الْمَعْنَى", "mana", "noun")),
  tok("فَأَنَا", "ana", "pron", [K, MK, HT], "الْفَاءُ لِلْجَزَاءِ، وَأَنَا مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«then I» — the mubtada.", "«ben de» — mübtedâ.", segments=fa("أَنَا", "ana", "pron")),
  tok("أُكْرِمُهُ", "akrama", "verb", [K, MK, MB, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«honour him» — the khabar clause.", "«ona ikram ederim» — haber cümlesi.", punct="،", segments=[seg("أُكْرِمُ", "akrama", "verb"), pr3ms()]),
  tok("وَإِنْ", "in-shartiyya", "part", [K, SH, AT], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("فُتِحَتْ", "fataha", "verb", [K, SH, "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«it is read with the fatḥa»", "«fethalanırsa»"),
  tok("فَالْمَعْنَى", "mana", "noun", [K, SH, MK, "ism-maqsur-manqus"], "الْفَاءُ لِلْجَزَاءِ، وَالْمَعْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the sense is»", "«mânâ»", punct=":", segments=fa("الْمَعْنَى", "mana", "noun")),
  tok("فَإِكْرَامِي", "ikram", "noun", [K, MK, ID, "masdar", "ya-al-mutakallim"], "الْفَاءُ لِلْجَزَاءِ، وَإِكْرَامِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«then my honouring» — the mubtada: the maṣdar the fatḥa makes.", "«ikramım» — mübtedâ: fethanın yaptığı masdar.", segments=[seg("فَ", "fa", "conj"), seg("إِكْرَامِ", "ikram", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("إِيَّاهُ", "iyya", "pron", [K, MB], "ضَمِيرُ نَصْبٍ مُنْفَصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِلْمَصْدَرِ.", "«him» — the detached object pronoun, the maṣdar's object.", "«ona» — munfasıl nasb zamiri, masdarın mef'ûlü.", segments=[seg("إِيَّا", "iyya", "pron"), pr3ms()]),
  tok("ثَابِتٌ", "thabit", "noun", [K, MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«settled» — the khabar.", "«sâbittir» — haber.", punct="."),
 ]})
# ----------- s6 — the lightened inna (2:143, 26:186)
S.append({"id": "s6", "translation": {"en": "And the one with the kasra is lightened, and then the lām is required in its khabar; it may be nullified and may enter upon a verb of the verbs of the mubtada — as in His word, Exalted is He, «and indeed it was a great thing» (2:143), and «and indeed we think you one of the liars» (26:186).", "tr": "Kesreli olan tahfif edilir, o zaman haberinde lâm gerekir; ilga edilmesi ve mübtedâ fiillerinden bir fiile girmesi câizdir — Allah Teâlâ'nın «şüphesiz o büyük bir şeydi» (2:143) ve «şüphesiz biz seni yalancılardan sanıyoruz» (26:186) sözleri gibi."},
 "tokens": [
  tok("وَتُخَفَّفُ", "khaffafa", "verb", [K, "naib-al-fail", "form-ii-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتُخَفَّفُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and is lightened» — the passive.", "«ve tahfif edilir» — meçhul.", segments=wa("تُخَفَّفُ", "khaffafa", "verb")),
  tok("الْمَكْسُورَةُ", "maksur", "noun", [K, "naib-al-fail", "ism-maful"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — أَيْ: إِنَّ الْمَكْسُورَةُ.", "«the one with the kasra» — the deputy doer: إِنَّ.", "«kesreli olan» — nâib-i fâil: inne."),
  tok("فَيَلْزَمُ", "lazima", "verb", [K, FL, AT], "الْفَاءُ عَاطِفَةٌ لِلتَّرْتِيبِ، وَيَلْزَمُ مُضَارِعٌ مَرْفُوعٌ.", "«and then is required»", "«o zaman gerekir»", segments=fa("يَلْزَمُ", "lazima", "verb")),
  tok("اللَّامُ", "lam-letter", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ — لَامُ الِابْتِدَاءِ، فَارِقَةً بَيْنَ إِنَّ الْمُخَفَّفَةِ وَإِنِ النَّافِيَةِ.", "«the lām» — the doer: the lām that tells the lightened إِنْ from the negative إِنْ.", "«lâm» — fâil: tahfif edilmiş inne'yi nefy in'inden ayıran lâm."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("خَبَرِهَا", "khabar-predicate", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its khabar»", "«haberinde»", punct="،", segments=[seg("خَبَرِ", "khabar-predicate", "noun"), pr3fs()]),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, FL, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("إِلْغَاؤُهَا", "ilgha", "noun", [K, FL, ID, "masdar", "ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — هَمْزَتُهُ عَلَى وَاوٍ لِلضَّمَّةِ.", "«its nullifying» — the doer; the hamza seated on a wāw by the ḍamma.", "«ilga edilmesi» — fâil; hemzesi dammeden ötürü vâv üzerinde.", segments=[seg("إِلْغَاؤُ", "ilgha", "noun"), pr3fs()]),
  tok("وَدُخُولُهَا", "dukhul", "noun", [K, AT, ID, "masdar"], "الْوَاوُ عَاطِفَةٌ، وَدُخُولُهَا مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and its entering»", "«ve girmesi»", segments=[seg("وَ", "wa", "conj"), seg("دُخُولُ", "dukhul", "noun"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«upon»", "«üzerine»"),
  tok("فِعْلٍ", "fil", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«a verb»", "«bir fiile»"),
  tok("مِنْ", "min", "prep", [K, HJ, NA], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِفِعْلٍ.", "«of»", "«-den»"),
  tok("أَفْعَالِ", "afal", "noun", [K, HJ, ID, "jam-taksir"], "مَجْرُورٌ بِمِنْ، مُضَافٌ — جَمْعُ فِعْلٍ.", "«the verbs of»", "«fiillerinden»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID, MK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَيْ: كَانَ وَظَنَّ وَأَخَوَاتُهُمَا، الدَّاخِلَةُ عَلَى الْمُبْتَدَإِ وَالْخَبَرِ.", "«the mubtada» — kāna, ẓanna and their sisters, which enter upon the mubtada and khabar.", "«mübtedâ» — mübtedâ ve habere giren kâne, zanne ve kardeşleri.", punct="،"),
  *cite_quran(),
  tok("وَإِنْ", "inna", "part", [K, IQ, IW, "tawkid"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُلْغَاةٌ — وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ.", "«and indeed» — the lightened inna, nullified; its ism the dropped pronoun of the matter.", "«ve şüphesiz» — tahfif edilmiş, ilga edilmiş inne; ismi mahzûf şan zamiri.", segments=wa("إِنْ", "inna", "part")),
  tok("كَانَتْ", "kana", "verb", [K, IQ, KN], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«it was» — kāna, its ism concealed.", "«o idi» — kâne, ismi müstetir."),
  tok("لَكَبِيرَةً", "kabira", "noun", [K, IQ, KN, "tawkid"], "اللَّامُ الْفَارِقَةُ، وَكَبِيرَةً خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a great thing» — the telling lām; the khabar of kāna.", "«büyük bir şey» — ayırıcı lâm; kâne'nin haberi.", punct="،", segments=[seg("لَ", "lam-ibtida", "part"), seg("كَبِيرَةً", "kabira", "noun")]),
  tok("وَإِنْ", "inna", "part", [K, IQ, IW, "tawkid"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُلْغَاةٌ.", "«and indeed» — the lightened inna.", "«ve şüphesiz» — tahfif edilmiş inne.", segments=wa("إِنْ", "inna", "part")),
  tok("نَظُنُّكَ", "zanna", "verb", [K, IQ, ZN, "mafulayn", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَالْكَافُ مَفْعُولٌ أَوَّلُ.", "«we think you» — the kāf its first object.", "«seni sanıyoruz» — kâf birinci mef'ûl.", segments=[seg("نَظُنُّ", "zanna", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَمِنَ", "min", "prep", [K, IQ, HJ, "tawkid", ZN], "اللَّامُ الْفَارِقَةُ، وَمِنَ حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ.", "«one of» — the telling lām; the phrase is the second object.", "«-den» — ayırıcı lâm; câr-mecrûr ikinci mef'ûl.", segments=[seg("لَ", "lam-ibtida", "part"), seg("مِنَ", "min", "prep")]),
  tok("الْكَاذِبِينَ", "kadhib-liar", "noun", [K, IQ, HJ, "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِمِنْ، وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the liars» — in jarr by the yāʾ.", "«yalancılardan» — yâ ile mecrûr.", punct="."),
 ]})
# ----------- s7 — the lightened anna: the pronoun of the matter, a verb of certainty before it
S.append({"id": "s7", "translation": {"en": "And the one with the fatḥa is lightened, and then it governs an estimated pronoun of the matter; and a verb of the verbs of certainty must stand before it — as in «I knew that Zayd is standing»,", "tr": "Fethalı olan tahfif edilir, o zaman takdir edilen bir şan zamirinde amel eder; önünde tahkik fiillerinden bir fiil bulunması gerekir — «bildim ki Zeyd ayaktadır» gibi;"},
 "tokens": [
  tok("وَتُخَفَّفُ", "khaffafa", "verb", [K, "naib-al-fail", "form-ii-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتُخَفَّفُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and is lightened»", "«ve tahfif edilir»", segments=wa("تُخَفَّفُ", "khaffafa", "verb")),
  tok("الْمَفْتُوحَةُ", "maftuh", "noun", [K, "naib-al-fail", "ism-maful"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ — أَيْ: أَنَّ الْمَفْتُوحَةُ.", "«the one with the fatḥa» — the deputy doer: أَنَّ.", "«fethalı olan» — nâib-i fâil: enne."),
  tok("فَتَعْمَلُ", "amila", "verb", [K, FL, AT], "الْفَاءُ عَاطِفَةٌ، وَتَعْمَلُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and then governs»", "«o zaman amel eder»", segments=fa("تَعْمَلُ", "amila", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("ضَمِيرِ", "damir", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«a pronoun of»", "«zamirinde»"),
  tok("شَأْنٍ", "shan", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ضَمِيرُ الشَّأْنِ: هُوَ، أَيِ: الْأَمْرُ وَالْحَدِيثُ.", "«the matter» — the pronoun of the matter: «it», the affair in hand.", "«şan» — şan zamiri: «o», yani iş, durum."),
  tok("مُقَدَّرٍ", "muqaddar", "noun", [K, NA, "ism-maful", HT], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ.", "«estimated» — the naʿt.", "«takdir edilen» — sıfat.", punct="،"),
  tok("وَيَلْزَمُ", "lazima", "verb", [K, FL], "الْوَاوُ عَاطِفَةٌ، وَيَلْزَمُ مُضَارِعٌ مَرْفُوعٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فَاعِلٌ.", "«and it is required» — the clause after it is the doer.", "«ve gerekir» — ardındaki cümle fâil.", segments=wa("يَلْزَمُ", "lazima", "verb")),
  tok("أَنْ", "an-masdariyya", "part", [K, AM, FL], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", [K, AM, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«there be» — kāna in naṣb.", "«olması» — mansûb kâne."),
  tok("قَبْلَهَا", "qabla", "noun", [K, MF, ID, KN], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرُ يَكُونَ مُقَدَّمٌ.", "«before it» — the fronted khabar of kāna.", "«önünde» — kâne'nin mukaddem haberi.", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  tok("فِعْلٌ", "fil", "noun", [K, KN], "اسْمُ يَكُونَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a verb» — the delayed ism of kāna.", "«bir fiil» — kâne'nin muahhar ismi."),
  tok("مِنْ", "min", "prep", [K, HJ, NA], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ — صِفَةٌ لِفِعْلٌ.", "«of»", "«-den»"),
  tok("أَفْعَالِ", "afal", "noun", [K, HJ, ID, "jam-taksir"], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«the verbs of»", "«fiillerinden»"),
  tok("التَّحْقِيقِ", "tahqiq", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَيْ: أَفْعَالِ الْيَقِينِ: عَلِمَ وَتَيَقَّنَ وَأَخَوَاتُهُمَا.", "«certainty» — the verbs of sure knowing.", "«tahkik» — yakîn fiilleri.", punct="،"),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, FL, ZN, "mafulayn"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْهِ.", "«I knew»", "«bildim»", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنْ", "anna", "part", [K, IW, IA, ZN, HT], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ: أَنَّهُ.", "«that» — the lightened anna; its ism the dropped pronoun of the matter.", "«ki» — tahfif edilmiş enne; ismi mahzûf şan zamiri."),
  tok("زَيْدٌ", "zayd", "propn", [K, IW, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — لَا اسْمُ أَنْ.", "«Zayd» — a mubtada, not the ism of أَنْ.", "«Zeyd» — mübtedâ, en'in ismi değil."),
  tok("قَائِمٌ", "qaim", "noun", [K, IW, MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ أَنْ الْمُخَفَّفَةِ.", "«standing» — the khabar; the sentence is the khabar of the lightened أَنْ.", "«ayaktadır» — haber; cümle tahfif edilmiş en'in haberi.", punct="،"),
 ]})
# ----------- s8 — before a verb: la / the sin / sawfa / qad (73:20)
S.append({"id": "s8", "translation": {"en": "and it enters upon the verb without restriction; and with a conjugable verb that is neither a condition nor a prayer it requires the letter of negation — as in «I knew that you will not stand» — or the sīn — as in His word, Exalted is He, «He knew that there will be» (73:20) — or سَوْفَ, or قَدْ — as in «I knew that you may stand».", "tr": "Fiile mutlak olarak girer; şart ve dua olmayan mutasarrıf fiille birlikte nefy harfi gerekir — «bildim ki kalkmayacaksın» gibi; yahut sîn — Allah Teâlâ'nın «bildi ki olacak» (73:20) sözü gibi; yahut sevfe; yahut kad — «bildim ki kalkabilirsin» gibi."},
 "tokens": [
  tok("وَتَدْخُلُ", "dakhala", "verb", [K, FL, AT], "الْوَاوُ عَاطِفَةٌ، وَتَدْخُلُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and it enters»", "«ve girer»", segments=wa("تَدْخُلُ", "dakhala", "verb")),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«upon»", "«üzerine»"),
  tok("الْفِعْلِ", "fil", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«the verb»", "«fiile»"),
  tok("مُطْلَقًا", "mutlaq", "noun", [K, "hal", "ism-maful"], "حَالٌ مَنْصُوبٌ — أَيْ: مُتَصَرِّفًا كَانَ أَوْ غَيْرَ مُتَصَرِّفٍ.", "«without restriction» — the ḥāl.", "«mutlak olarak» — hâl.", punct="،"),
  tok("وَيَلْزَمُهَا", "lazima", "verb", [K, FL, MB], "الْوَاوُ عَاطِفَةٌ، وَيَلْزَمُ مُضَارِعٌ مَرْفُوعٌ، وَهَا مَفْعُولٌ بِهِ.", "«and it requires» — the hā its object.", "«ve ona gerekir» — hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يَلْزَمُ", "lazima", "verb"), pr3fs()]),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("الْفِعْلِ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb»", "«fiil»"),
  tok("الْمُتَصَرِّفِ", "mutasarrif", "noun", [K, NA, "ism-fail", "form-v-verbs"], "نَعْتٌ مَجْرُورٌ — الَّذِي تَخْتَلِفُ صِيَغُهُ، بِخِلَافِ الْجَامِدِ كَعَسَى.", "«conjugable» — the naʿt: a verb with changing forms, unlike the frozen عَسَى.", "«mutasarrıf» — sıfat: sîgaları değişen fiil, donmuş asâ'nın aksine."),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ ثَانٍ مَجْرُورٌ، مُضَافٌ.", "«other than» — a second naʿt, annexed.", "«olmayan» — ikinci sıfat, muzâf."),
  tok("الشَّرْطِ", "shart", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the condition»", "«şart»"),
  tok("وَالدُّعَاءِ", "dua", "noun", [K, AT, ID, "ism-mamdud"], "الْوَاوُ عَاطِفَةٌ، وَالدُّعَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and the prayer»", "«ve dua»", segments=wa("الدُّعَاءِ", "dua", "noun")),
  tok("حَرْفُ", "harf", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the letter of» — the doer.", "«harfi» — fâil."),
  tok("النَّفْيِ", "nafy", "noun", [K, ID, "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«negation»", "«nefy»"),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, FL, ZN, "mafulayn"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I knew»", "«bildim»", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنْ", "anna", "part", [K, IW, IA, ZN, HT], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ.", "«that» — the lightened anna.", "«ki» — tahfif edilmiş enne."),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ — الْفَاصِلُ بَيْنَ أَنْ الْمُخَفَّفَةِ وَالْفِعْلِ.", "«not» — the negation that parts أَنْ from the verb.", "«-ma» — en ile fiili ayıran nefy."),
  tok("تَقُومُ", "qama", "verb", [K, FL, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — لَا مَنْصُوبٌ، لِأَنَّ أَنْ هُنَا مُخَفَّفَةٌ لَا مَصْدَرِيَّةٌ؛ وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — وَالْجُمْلَةُ خَبَرُ أَنْ.", "«you will stand» — in rafʿ, not naṣb: this أَنْ is the lightened one, not the maṣdar-maker.", "«kalkacaksın» — merfû, mansûb değil: bu en masdariyye değil, tahfif edilmiştir.", punct="،"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«ya da»"),
  tok("السِّينُ", "sin-letter", "noun", [K, AT], "مَعْطُوفٌ عَلَى حَرْفُ مَرْفُوعٌ.", "«the sīn» — joined to «the letter».", "«sîn» — harfe ma'tûf."),
  *cite_quran(),
  tok("عَلِمَ", "alima", "verb", [K, IQ, FL, ZN], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«He knew»", "«bildi»"),
  tok("أَنْ", "anna", "part", [K, IQ, IW, IA, HT], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ.", "«that» — the lightened anna.", "«ki» — tahfif edilmiş enne."),
  tok("سَيَكُونُ", "kana", "verb", [K, IQ, KN, "hollow-verbs", "mudari-marfu"], "السِّينُ لِلِاسْتِقْبَالِ — الْفَاصِلَةُ — وَيَكُونُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«there will be» — the sīn of the future, the parting letter.", "«olacak» — istikbal sîni, ayırıcı.", punct="،", segments=[seg("سَ", "sa", "part"), seg("يَكُونُ", "kana", "verb")]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("سَوْفَ", "sawfa", "part", [K, AT], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«sawfa» — quoted, joined.", "«sevfe» — hikâye edilmiş, ma'tûf.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("قَدْ", "qad", "part", [K, AT, "qad-harf"], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«qad» — quoted, joined.", "«kad» — hikâye edilmiş, ma'tûf."),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, FL, ZN, "mafulayn"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I knew»", "«bildim»", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنْ", "anna", "part", [K, IW, IA, ZN, HT], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ.", "«that» — the lightened anna.", "«ki» — tahfif edilmiş enne."),
  tok("قَدْ", "qad", "part", [K, "qad-harf"], "حَرْفُ تَحْقِيقٍ — الْفَاصِلُ.", "«may» — qad, the parting letter.", "«-bilir» — kad, ayırıcı."),
  tok("تَقُومُ", "qama", "verb", [K, FL, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«you stand» — in rafʿ.", "«kalkarsın» — merfû.", punct="."),
 ]})
# ----------- s9 — the frozen verb, the condition, the prayer need no parting letter (7:185, 34:14, 24:9)
S.append({"id": "s9", "translation": {"en": "But if it is not conjugable, or is a condition, or a prayer, it needs none of these letters — as in His word, Exalted is He, «and that it may be that their term has drawn near» (7:185), and His word, «it became clear to the jinn that, had they known the unseen…» (34:14), and His word, «and the fifth, that God's wrath be upon her» (24:9).", "tr": "Mutasarrıf değilse, yahut şart veya dua ise bu harflerden hiçbirine muhtaç olmaz — Allah Teâlâ'nın «ve ecellerinin yaklaşmış olabileceğini» (7:185), «cinlere belli oldu ki gaybı bilselerdi…» (34:14) ve «beşincisi, Allah'ın gazabı onun üzerine olsun» (24:9) sözleri gibi."},
 "tokens": [
  tok("وَلَوْ", "law", "part", [K, "in-shartiyya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَوْ حَرْفُ شَرْطٍ.", "«but if»", "«eğer»", segments=wa("لَوْ", "law", "part")),
  tok("كَانَ", "kana", "verb", [K, KN, "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْفِعْلُ.", "«it is» — kāna, its ism the verb.", "«ise» — kâne, ismi fiil."),
  tok("غَيْرَ", "ghayr", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«not» — the khabar of kāna, annexed.", "«olmayan» — kâne'nin haberi, muzâf."),
  tok("مُتَصَرِّفٍ", "mutasarrif", "noun", [K, ID, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«conjugable»", "«mutasarrıf»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("شَرْطًا", "shart", "noun", [K, AT, KN], "مَعْطُوفٌ عَلَى غَيْرَ مَنْصُوبٌ.", "«a condition»", "«şart»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("دُعَاءً", "dua", "noun", [K, AT, KN, "ism-mamdud"], "مَعْطُوفٌ مَنْصُوبٌ.", "«a prayer»", "«dua»"),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya"], "حَرْفُ نَفْيٍ.", "«not»", "«-maz»"),
  tok("يَحْتَاجُ", "ihtaja", "verb", [K, FL, "form-viii-verbs", "hollow-verbs", "in-shartiyya"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جَوَابُ لَوْ.", "«it needs» — the answer of law.", "«muhtaç olur» — lev'in cevabı."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("أَحَدِ", "ahad", "noun", [K, HJ, ID], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«any of»", "«birine»"),
  tok("هٰذِهِ", "hadhihi", "pron", [K, "asma-al-ishara", ID], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«these»", "«bu»"),
  tok("الْحُرُوفِ", "harf", "noun", [K, "badal", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«letters» — the badal.", "«harflerin» — bedel.", punct="،"),
  *cite_quran(),
  tok("وَأَنْ", "anna", "part", [K, IQ, IW, IA, HT], "الْوَاوُ عَاطِفَةٌ، وَأَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ.", "«and that» — the lightened anna.", "«ve ki» — tahfif edilmiş enne.", segments=wa("أَنْ", "anna", "part")),
  tok("عَسَى", "asa-hope", "verb", [K, IQ, "ism-maqsur-manqus", KN], "فِعْلٌ مَاضٍ جَامِدٌ لِلرَّجَاءِ — غَيْرُ مُتَصَرِّفٍ، فَلَا فَاصِلَ — وَالْجُمْلَةُ خَبَرُ أَنْ.", "«it may be» — the frozen verb of hope: no parting letter; the clause is the khabar of أَنْ.", "«olabilir» — donmuş recâ fiili: ayırıcı yok; cümle en'in haberi."),
  tok("أَنْ", "an-masdariyya", "part", [K, IQ, AM], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ عَسَى.", "«that» — the clause is the doer of عَسَى.", "«-ması» — cümle asâ'nın fâili."),
  tok("يَكُونَ", "kana", "verb", [K, IQ, AM, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be»", "«olması»"),
  tok("قَدِ", "qad", "part", [K, IQ, "qad-harf"], "حَرْفُ تَحْقِيقٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«has»", "«-mış»"),
  tok("اقْتَرَبَ", "iqtaraba", "verb", [K, IQ, KN, FL, "form-viii-verbs"], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ خَبَرُ يَكُونَ.", "«drawn near» — the clause is the khabar of yakūna.", "«yaklaştı» — cümle yekûne'nin haberi."),
  tok("أَجَلُهُمْ", "ajal", "noun", [K, IQ, FL, ID, KN], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — وَاسْمُ يَكُونَ ضَمِيرُ الشَّأْنِ.", "«their term» — the doer; kāna's ism is the pronoun of the matter.", "«ecelleri» — fâil; yekûne'nin ismi şan zamiri.", punct="،", segments=[seg("أَجَلُ", "ajal", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  *cite_quran(wa=True),
  tok("تَبَيَّنَتِ", "tabayyana", "verb", [K, IQ, FL, "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«it became clear to»", "«belli oldu»"),
  tok("الْجِنُّ", "jinn", "noun", [K, IQ, FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the jinn» — the doer.", "«cinler» — fâil."),
  tok("أَنْ", "anna", "part", [K, IQ, IW, IA, HT], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ — وَجُمْلَةُ الشَّرْطِ خَبَرُهَا بِلَا فَاصِلٍ.", "«that» — the lightened anna; the conditional sentence is its khabar with no parting letter.", "«ki» — tahfif edilmiş enne; şart cümlesi ayırıcısız haberi."),
  tok("لَوْ", "law", "part", [K, IQ, "in-shartiyya"], "حَرْفُ شَرْطٍ.", "«had»", "«-saydı»"),
  tok("كَانُوا", "kana", "verb", [K, IQ, KN, "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«they been» — kāna, the wāw its ism.", "«idiler» — kâne, vâv ismi."),
  tok("يَعْلَمُونَ", "alima", "verb", [K, IQ, KN, "afal-khamsa", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كَانَ.", "«knowing» — the khabar of kāna.", "«biliyor» — kâne'nin haberi."),
  tok("الْغَيْبَ", "ghayb", "noun", [K, IQ, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the unseen» — the object.", "«gaybı» — mef'ûl.", punct="،"),
  *cite_quran(wa=True),
  tok("وَالْخَامِسَةُ", "khamis", "noun", [K, IQ, MK, AT], "الْوَاوُ عَاطِفَةٌ، وَالْخَامِسَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fifth» — the mubtada.", "«ve beşincisi» — mübtedâ.", segments=wa("الْخَامِسَةُ", "khamis", "noun")),
  tok("أَنْ", "anna", "part", [K, IQ, IW, IA, HT, MK], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْمُبْتَدَإِ؛ وَجُمْلَةُ الدُّعَاءِ خَبَرُهَا بِلَا فَاصِلٍ.", "«that» — the lightened anna; the prayer is its khabar with no parting letter (the reading أَنْ غَضِبَ).", "«ki» — tahfif edilmiş enne; dua cümlesi ayırıcısız haberi (en gadibe kıraati)."),
  tok("غَضِبَ", "ghadiba", "verb", [K, IQ, FL, "khabar-insha"], "فِعْلٌ مَاضٍ فِي مَعْنَى الدُّعَاءِ.", "«be wrathful» — the māḍī as a prayer.", "«gazap etsin» — dua mânâsında mâzî."),
  tok("اللهُ", "allah", "propn", [K, IQ, FL], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.", "«God» — the doer.", "«Allah» — fâil."),
  tok("عَلَيْهَا", "ala", "prep", [K, IQ, HJ], "عَلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«upon her»", "«onun üzerine»", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), pr3fs()]),
 ]})
# ----------- s10 — the lightened ka-anna and lakinna
S.append({"id": "s10", "translation": {"en": "And كَأَنَّ is lightened and then, in the most eloquent usage, nullified — as in «as if her two breasts were two caskets» — and لٰكِنَّ is lightened and its nullifying is then required — as in «Zayd did not come to me, but ʿAmr is present»; and both may enter upon a verb — as in «as if Zayd stood» and «Zayd did not stand, but sat».", "tr": "Keenne tahfif edilir ve en fasih kullanışta ilga edilir — «sanki iki memesi iki hokka» gibi; lâkinne tahfif edilir ve ilgası vâcip olur — «Zeyd bana gelmedi, fakat Amr hazırdır» gibi; ikisinin de fiile girmesi câizdir — «sanki Zeyd kalktı» ve «Zeyd kalkmadı, fakat oturdu» gibi."},
 "tokens": [
  tok("وَتُخَفَّفُ", "khaffafa", "verb", [K, "naib-al-fail", "form-ii-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتُخَفَّفُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is lightened»", "«ve tahfif edilir»", segments=wa("تُخَفَّفُ", "khaffafa", "verb")),
  tok("كَأَنَّ", "kaanna", "part", [K, "naib-al-fail", IW, HT, "tashbih"], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، نَائِبُ الْفَاعِلِ فِي مَحَلِّ رَفْعٍ.", "«ka-anna» — quoted; the deputy doer.", "«keenne» — hikâye edilmiş; nâib-i fâil."),
  tok("فَتُلْغَى", "algha", "verb", [K, "naib-al-fail", "form-iv-verbs", "ism-maqsur-manqus", AT], "الْفَاءُ عَاطِفَةٌ، وَتُلْغَى مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and then is nullified»", "«ve ilga edilir»", segments=fa("تُلْغَى", "algha", "verb")),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«üzere»"),
  tok("الْأَفْصَحِ", "afsah", "noun", [K, HJ, "ism-tafdil"], "مَجْرُورٌ بِعَلَى — أَفْعَلُ تَفْضِيلٍ: الْوَجْهِ الْأَفْصَحِ.", "«the most eloquent usage» — the elative.", "«en fasih olan» — ism-i tafdîl."),
  nahw(),
  tok("كَأَنْ", "kaanna", "part", [K, IW, HT, "tashbih"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُلْغَاةٌ — فَمَا بَعْدَهَا مُبْتَدَأٌ وَخَبَرٌ.", "«as if» — the lightened ka-anna, nullified: a mubtada and khabar follow.", "«sanki» — tahfif edilmiş, ilga edilmiş keenne: ardından mübtedâ ve haber."),
  tok("ثَدْيَاهُ", "thady", "noun", [K, MK, ID, "al-muthanna"], "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«her two breasts» — the mubtada, a dual in rafʿ by the alif, its nūn dropped for the annexation.", "«iki memesi» — mübtedâ, elifle merfû tesniye, izâfetle nûnu düşmüş.", segments=[seg("ثَدْيَا", "thady", "noun"), pr3ms()]),
  tok("حُقَّانِ", "huqq", "noun", [K, MK, "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two caskets» — the khabar, a dual.", "«iki hokka» — haber, tesniye.", punct="،"),
  tok("وَتُخَفَّفُ", "khaffafa", "verb", [K, "naib-al-fail", "form-ii-verbs", AT], "الْوَاوُ عَاطِفَةٌ، وَتُخَفَّفُ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is lightened»", "«ve tahfif edilir»", segments=wa("تُخَفَّفُ", "khaffafa", "verb")),
  tok("لٰكِنَّ", "lakinna", "part", [K, "naib-al-fail", IW, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، نَائِبُ الْفَاعِلِ فِي مَحَلِّ رَفْعٍ.", "«lākinna» — quoted; the deputy doer.", "«lâkinne» — hikâye edilmiş; nâib-i fâil."),
  tok("فَيَجِبُ", "wajaba", "verb", [K, FL, AT, "mithal-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَجِبُ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ وَاوِيٌّ سَقَطَتْ وَاوُهُ.", "«and then is required»", "«ve vâcip olur»", segments=fa("يَجِبُ", "wajaba", "verb")),
  tok("إِلْغَاؤُهَا", "ilgha", "noun", [K, FL, ID, "masdar", "ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its nullifying» — the doer.", "«ilgası» — fâil.", segments=[seg("إِلْغَاؤُ", "ilgha", "noun"), pr3fs()]),
  nahw(),
  tok("مَا", "ma-nafiya", "part", [K, "anwa-ma"], "حَرْفُ نَفْيٍ.", "«not»", "«-medi»"),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil."),
  tok("وَلٰكِنْ", "lakin", "part", [K, IW, "istidrak-note", MK], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُلْغَاةٌ — حَرْفُ اسْتِدْرَاكٍ.", "«but» — the lightened lākin, nullified.", "«fakat» — tahfif edilmiş, ilga edilmiş lâkin.", segments=wa("لٰكِنْ", "lakin", "part")),
  tok("عَمْرٌو", "amr-name", "propn", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — لَا اسْمُ لٰكِنْ.", "«ʿAmr» — a mubtada, not the ism of lākin.", "«Amr» — mübtedâ, lâkin'in ismi değil."),
  tok("حَاضِرٌ", "hadir", "noun", [K, MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«present» — the khabar.", "«hazırdır» — haber.", punct="،"),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, FL, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ مُضَارِعٌ مَرْفُوعٌ.", "«and it is allowed»", "«ve câizdir»", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("دُخُولُهُمَا", "dukhul", "noun", [K, FL, ID, "masdar"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their both entering» — the doer.", "«ikisinin girmesi» — fâil.", segments=[seg("دُخُولُ", "dukhul", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«upon»", "«üzerine»"),
  tok("الْفِعْلِ", "fil", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«a verb»", "«fiile»"),
  nahw(),
  tok("كَأَنْ", "kaanna", "part", [K, IW, HT, "tashbih"], "مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ مُلْغَاةٌ.", "«as if»", "«sanki»"),
  tok("قَامَ", "qama", "verb", [K, FL, "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«stood»", "«kalktı»"),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", punct="،"),
  tok("وَمَا", "ma-nafiya", "part", [K, "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and not»", "«ve -medi»", segments=wa("مَا", "ma-nafiya", "part")),
  tok("قَامَ", "qama", "verb", [K, FL, "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«stood»", "«kalktı»"),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  tok("وَلٰكِنْ", "lakin", "part", [K, IW, "istidrak-note"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ مُخَفَّفَةٌ مُلْغَاةٌ دَاخِلَةٌ عَلَى الْفِعْلِ.", "«but» — the lightened lākin before a verb.", "«fakat» — fiilin önünde tahfif edilmiş lâkin.", segments=wa("لٰكِنْ", "lakin", "part")),
  tok("قَعَدَ", "qaada", "verb", [K, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«sat»", "«oturdu»", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i] and g != "istidrak-note"]

CAND = {
 "fataha": G("fataha", "فَتَحَ", "ف ت ح", "verb", "to open; to give a fatḥa", "açmak; fethalamak", 2),
 "balagha": G("balagha", "بَلَغَ", "ب ل غ", "verb", "to reach (بَلَغَنِي أَنَّ: it reached me that)", "ulaşmak (beleğanî enne: bana ulaştı ki)", 3),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection before the speaker's yāʾ", "vikâye nûnu — mütekellim yâsından önce", 4),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masculine singular, attached)", "sen / senin (bitişik)", 1),
 "pron-3d": G("pron-3d", "هُمَا", None, "pron", "they two / their (attached)", "o ikisi / onların (bitişik)", 1),
 "inda": G("inda", "عِنْدَ", "ع ن د", "noun", "with, at (a ẓarf of place)", "yanında, nezdinde (mekân zarfı)", 2),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "jalasa": G("jalasa", "جَلَسَ", "ج ل س", "verb", "to sit", "oturmak", 1),
 "haythu": G("haythu", "حَيْثُ", None, "noun", "where — a mabnī ẓarf of place, annexed to a sentence", "haysü — cümleye muzâf, mebnî mekân zarfı", 4),
 "jalis-sitting": G("jalis-sitting", "جَالِس", "ج ل س", "noun", "sitting (ism fāʿil of جَلَسَ)", "oturan", 2),
 "law": G("law", "لَوْ", None, "part", "if, had — the condition whose answer fails because its protasis fails", "lev — şartın gerçekleşmemesi yüzünden cevabın gerçekleşmediği şart", 3),
 "lam-jawab": G("lam-jawab", "لَ (لَامُ الْجَوَابِ)", None, "part", "the lām of the answer — of لَوْ, لَوْلَا or an oath", "cevap lâmı — lev, levlâ veya kasemin", 4),
 "kadha": G("kadha", "كَذَا", None, "pron", "such-and-such, so", "şöyle, falan", 3),
 "qiyam": G("qiyam", "قِيَام", "ق و م", "noun", "standing (masdar of قَامَ)", "kıyâm — ayakta durma", 2),
 "dhahib": G("dhahib", "ذَاهِب", "ذ ه ب", "noun", "going (ism fāʿil of ذَهَبَ)", "giden", 2),
 "dhahab-going": G("dhahab-going", "ذَهَاب", "ذ ه ب", "noun", "going, departure (masdar of ذَهَبَ)", "gidiş (zehebe'nin masdarı)", 3),
 "mawjud": G("mawjud", "مَوْجُود", "و ج د", "noun", "present, existent (ism mafʿūl of وَجَدَ) — the khabar لَوْلَا always drops", "mevcut — levlâ'nın daima hazfettiği haber", 3),
 "ma-masdariyya": G("ma-masdariyya", "مَا (الْمَصْدَرِيَّة)", None, "part", "the mā that makes a maṣdar; with time: as long as", "masdariyye mâ; zamanla: -dığı sürece", 4),
 "masdari": G("masdari", "مَصْدَرِيّ", "ص د ر", "noun", "maṣdar-making (a nisba) — of مَا and أَنْ", "masdariyye — mâ ve en'in sıfatı", 5),
 "tawqiti": G("tawqiti", "تَوْقِيتِيّ", "و ق ت", "noun", "of time, timing (a nisba) — مَا التَّوْقِيتِيَّة: as long as", "tevkîtî — zaman bildiren; mâ et-tevkîtiyye: -dığı sürece", 6),
 "ikhtisas": G("ikhtisas", "اِخْتِصَاص", "خ ص ص", "noun", "belonging only to, specialisation (masdar of اخْتَصَّ)", "ihtisas — yalnız ona âit olma", 5),
 "mudda": G("mudda", "مُدَّة", "م د د", "noun", "a duration, a span of time", "müddet", 2),
 "thubut": G("thubut", "ثُبُوت", "ث ب ت", "noun", "being established, firmness (masdar of ثَبَتَ)", "sübût", 4),
 "ajiba": G("ajiba", "عَجِبَ", "ع ج ب", "verb", "to marvel at (عَجِبَ مِنْ)", "şaşmak, hayret etmek (acibe min)", 3),
 "atif": G("atif", "عَاطِف", "ع ط ف", "noun", "joining, conjunctive (ism fāʿil of عَطَفَ) — حَرْفٌ عَاطِفٌ", "atfeden — atıf harfi", 4),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, to come to know", "bilmek, tanımak", 1),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "a matter, an affair", "iş, husus", 2, plural="أُمُور"),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous, sound (ism fāʿil of صَلَحَ)", "sâlih", 2),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "taqdir": G("taqdir", "تَقْدِير", "ق د ر", "noun", "estimation — the unspoken wording a reading assumes", "takdir — bir okuyuşun varsaydığı söylenmemiş ifade", 4),
 "allati": G("allati", "الَّتِي", None, "pron", "which, that (feminine relative)", "elletî — müennes ism-i mevsûl", 2),
 "fa-letter": G("fa-letter", "فَاء", None, "noun", "the letter fāʾ — named as a noun; فَاءُ الْجَزَاءِ", "fâ harfi — isim olarak; cezâ fâsı", 4),
 "jaza-answer": G("jaza-answer", "جَزَاء", "ج ز ي", "noun", "the answer of a condition; requital", "cezâ — şartın cevabı; karşılık", 3),
 "man-shart": G("man-shart", "مَنْ (الشَّرْطِيَّة)", None, "pron", "whoever — the conditional noun", "men-i şartiyye — kim … ise", 3),
 "ikram": G("ikram", "إِكْرَام", "ك ر م", "noun", "honouring (masdar of أَكْرَمَ)", "ikram", 3),
 "iyya": G("iyya", "إِيَّا", None, "pron", "the carrier of the detached object pronoun (إِيَّاهُ، إِيَّاكَ)", "munfasıl nasb zamirinin taşıyıcısı (iyyâhu, iyyâke)", 4),
 "thabit": G("thabit", "ثَابِت", "ث ب ت", "noun", "settled, established (ism fāʿil of ثَبَتَ)", "sâbit", 3),
 "khaffafa": G("khaffafa", "خَفَّفَ", "خ ف ف", "verb", "to lighten — to drop the shadda of إِنَّ / أَنَّ / كَأَنَّ / لٰكِنَّ", "tahfif etmek — inne / enne / keenne / lâkinne'nin şeddesini düşürmek", 4),
 "maksur": G("maksur", "مَكْسُور", "ك س ر", "noun", "carrying a kasra (ism mafʿūl of كَسَرَ); الْمَكْسُورَةُ: إِنَّ", "meksûr — kesreli; el-meksûra: inne", 4),
 "maftuh": G("maftuh", "مَفْتُوح", "ف ت ح", "noun", "carrying a fatḥa (ism mafʿūl of فَتَحَ); الْمَفْتُوحَةُ: أَنَّ", "meftûh — fethalı; el-meftûha: enne", 4),
 "lazima": G("lazima", "لَزِمَ", "ل ز م", "verb", "to be required, to be necessary", "gerekmek, lâzım olmak", 3),
 "ilgha": G("ilgha", "إِلْغَاء", "ل غ و", "noun", "nullifying — stripping a governor of its work (masdar of أَلْغَى)", "ilga — âmilin amelini kaldırma", 5),
 "dukhul": G("dukhul", "دُخُول", "د خ ل", "noun", "entering (masdar of دَخَلَ)", "giriş, dâhil olma", 2),
 "afal": G("afal", "أَفْعَال", "ف ع ل", "noun", "verbs (plural of فِعْل)", "fiiller", 2),
 "kabira": G("kabira", "كَبِيرَة", "ك ب ر", "noun", "a great thing, grave (feminine of كَبِير)", "büyük, ağır şey", 2),
 "zanna": G("zanna", "ظَنَّ", "ظ ن ن", "verb", "to think, to suppose (two objects)", "sanmak, zannetmek (iki mef'ûllü)", 2),
 "kadhib-liar": G("kadhib-liar", "كَاذِب", "ك ذ ب", "noun", "a liar (ism fāʿil of كَذَبَ)", "yalancı", 2, plural="كَاذِبُونَ"),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to work; to govern (of a governor)", "çalışmak; amel etmek (âmil)", 2),
 "damir": G("damir", "ضَمِير", "ض م ر", "noun", "a pronoun; ضَمِيرُ الشَّأْنِ: the pronoun of the matter", "zamir; şan zamiri", 3),
 "shan": G("shan", "شَأْن", "ش أ ن", "noun", "the matter, the affair; ضَمِيرُ الشَّأْنِ", "şan — iş, durum; şan zamiri", 3),
 "muqaddar": G("muqaddar", "مُقَدَّر", "ق د ر", "noun", "estimated, assumed (ism mafʿūl of قَدَّرَ)", "mukadder — takdir edilen", 4),
 "mutlaq": G("mutlaq", "مُطْلَق", "ط ل ق", "noun", "unrestricted; مُطْلَقًا: without restriction", "mutlak; mutlakan: kayıtsız", 3),
 "mutasarrif": G("mutasarrif", "مُتَصَرِّف", "ص ر ف", "noun", "conjugable — a verb with changing forms, unlike the frozen عَسَى / لَيْسَ", "mutasarrıf — sîgaları değişen fiil; câmid asâ / leyse'nin aksine", 5),
 "shart": G("shart", "شَرْط", "ش ر ط", "noun", "a condition", "şart", 2),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "a prayer, a supplication", "dua", 2),
 "nafy": G("nafy", "نَفْي", "ن ف ي", "noun", "negation", "nefy — olumsuzlama", 3),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "the negating mā (with the māḍī: did not)", "nefy mâ'sı (mâzîyle: -medi)", 2),
 "aw": G("aw", "أَوْ", None, "part", "or", "yahut", 1),
 "sin-letter": G("sin-letter", "السِّين", None, "noun", "the letter sīn — here the sīn of the future (سَيَفْعَلُ)", "sîn harfi — burada istikbal sîni", 4),
 "sa": G("sa", "سَ", None, "part", "the sīn of the near future", "yakın gelecek sîni", 2),
 "sawfa": G("sawfa", "سَوْفَ", None, "part", "will (the far future)", "sevfe — uzak gelecek", 2),
 "qad": G("qad", "قَدْ", None, "part", "qad — certainty with the māḍī, possibility with the muḍāriʿ", "kad — mâzîyle tahkik, muzâriyle ihtimal", 3),
 "ihtaja": G("ihtaja", "اِحْتَاجَ", "ح و ج", "verb", "to need (اِحْتَاجَ إِلَى)", "muhtaç olmak", 3),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "one, any one", "biri, herhangi biri", 1),
 "asa-hope": G("asa-hope", "عَسَى", "ع س ي", "verb", "it may be — the frozen verb of hope", "asâ — umulur ki; câmid recâ fiili", 4),
 "iqtaraba": G("iqtaraba", "اقْتَرَبَ", "ق ر ب", "verb", "to draw near (Form VIII)", "yaklaşmak (iftiâl)", 3),
 "ajal": G("ajal", "أَجَل", "أ ج ل", "noun", "an appointed term", "ecel — belirlenmiş süre", 3, plural="آجَال"),
 "tabayyana": G("tabayyana", "تَبَيَّنَ", "ب ي ن", "verb", "to become clear (Form V)", "belli olmak, açığa çıkmak (tefa''ul)", 3),
 "jinn": G("jinn", "جِنّ", "ج ن ن", "noun", "the jinn", "cin", 2),
 "ghayb": G("ghayb", "غَيْب", "غ ي ب", "noun", "the unseen", "gayb", 2),
 "khamis": G("khamis", "خَامِس", "خ م س", "noun", "fifth", "beşinci", 2),
 "ghadiba": G("ghadiba", "غَضِبَ", "غ ض ب", "verb", "to be angry (غَضِبَ عَلَى)", "gazap etmek, kızmak", 2),
 "afsah": G("afsah", "أَفْصَح", "ف ص ح", "noun", "more / most eloquent (elative of فَصِيح)", "efsah — en fasih", 4),
 "thady": G("thady", "ثَدْي", "ث د ي", "noun", "a breast", "meme", 3, plural="أَثْدَاء"),
 "huqq": G("huqq", "حُقّ", "ح ق ق", "noun", "a small casket, a round box (of perfume)", "hokka — küçük yuvarlak kutu", 5, plural="حِقَاق"),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but — the lightened لٰكِنَّ, which does not govern", "lâkin — amel etmeyen tahfif edilmiş lâkinne", 2),
 "amr-name": G("amr-name", "عَمْرو", None, "propn", "ʿAmr — the grammarians' second stock name", "Amr — nahivcilerin ikinci örnek ismi", 2),
 "hadir": G("hadir", "حَاضِر", "ح ض ر", "noun", "present (ism fāʿil of حَضَرَ)", "hazır", 2),
 "qaada": G("qaada", "قَعَدَ", "ق ع د", "verb", "to sit down", "oturmak", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to stand", "kalkmak, ayakta durmak", 1),
 "ana": G("ana", "أَنَا", None, "pron", "I", "ben", 1),
 "ka": G("ka", "كَ", None, "part", "like, as (the kāf of comparison)", "gibi (teşbih kâfı)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "hadhihi": G("hadhihi", "هَذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "fataha", _sg.sound1("fataha", "فَتَح", "فْتَح", "اِفْتَح", "فَتْح", "فَاتِح", "مَفْتُوح", "فُتِحَ", "يُفْتَحُ", "فَتَحَ يَفْتَحُ: ضِدُّ أَغْلَقَ — بَابُ فَتَحَ؛ فُتِحَتِ الْهَمْزَةُ: قُرِئَتْ بِالْفَتْحِ"))
put_morph(mo, "khaffafa", _sg.derived(_sg.B2, _sg.W2, "ُ", "خَفَّف", "خَفِّف", "خَفِّف", "تَخْفِيف", "مُخَفِّف", "مُخَفَّف", "خُفِّفَ", "يُخَفَّفُ", "خَفَّفَ يُخَفِّفُ: جَعَلَهُ خَفِيفًا — بَابُ التَّفْعِيلِ؛ تُخَفَّفُ إِنَّ: تُحْذَفُ شَدَّتُهَا"))
put_morph(mo, "ajiba", _sg.sound1("samia", "عَجِب", "عْجَب", "اِعْجَب", "عَجَب", "عَاجِب", None, None, None, "عَجِبَ يَعْجَبُ مِنْهُ: اسْتَغْرَبَهُ — بَابُ سَمِعَ، لَازِمٌ يَتَعَدَّى بِمِنْ"))
put_morph(mo, "iqtaraba", _sg.derived(_sg.B8, _sg.W8, "َ", "اِقْتَرَب", "قْتَرِب", "اِقْتَرِب", "اِقْتِرَاب", "مُقْتَرِب", None, None, None, "اِقْتَرَبَ يَقْتَرِبُ: دَنَا — بَابُ الِافْتِعَالِ، لَازِمٌ"))
put_morph(mo, "tabayyana", _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَيَّن", "تَبَيَّن", "تَبَيَّن", "تَبَيُّن", "مُتَبَيِّن", "مُتَبَيَّن", "تُبُيِّنَ", "يُتَبَيَّنُ", "تَبَيَّنَ يَتَبَيَّنُ: ظَهَرَ وَاتَّضَحَ — بَابُ التَّفَعُّلِ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch5 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "مَوَاضِعُ فَتْحِ أَنَّ، وَالْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ", "en": "Where أَنَّ takes the fatḥa, and the lightened إِنْ / أَنْ / كَأَنْ / لٰكِنْ", "tr": "Enne'nin fetha yerleri, ve tahfif edilmiş inne / enne / keenne / lâkinne"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الحروف المشبهة بالفعل", "الكافية لابن الحاجب — إنّ وأخواتها، المخففة من الثقيلة", "مغني اللبيب لابن هشام — إنْ وأنْ وكأنْ ولكنْ المخففات"],
 "amil": "أَنَّ مَعَ جُمْلَتِهَا فِي حُكْمِ الْمَصْدَرِ — the fatḥa wherever a maṣdar can stand in; lightened, إِنْ needs the telling lām and أَنْ the pronoun of the matter",
 "question": {
  "en": ["WHERE does the hamza take the fatḥa? Wherever a maṣdar could sit: as a DOER (بَلَغَنِي أَنَّكَ قَائِمٌ = بُلُوغُ قِيَامِكَ), an OBJECT (عَلِمْتُ أَنَّ), a MUBTADA after a fronted khabar (عِنْدِي أَنَّكَ), a MUḌĀF ILAYH (حَيْثُ أَنَّ).",
         "And after which words? After لَوْ and لَوْلَا (لَوْ أَنَّكَ قَائِمٌ = لَوْ ثَبَتَ قِيَامُكَ; لَوْلَا أَنَّكَ ذَاهِبٌ = لَوْلَا ذَهَابُكَ مَوْجُودٌ), after the مَا of time (اجْلِسْ مَا أَنَّ زَيْدًا قَائِمٌ = مُدَّةَ ثُبُوتِ قِيَامِهِ), after a jarr letter (مِنْ أَنَّكَ), after the ḥattā that joins a word (حَتَّى أَنَّكَ صَالِحٌ), after مُذْ / مُنْذُ.",
         "When may BOTH stand? Wherever both estimations make sense — after the fāʾ of the answer: مَنْ يُكْرِمْنِي فَإِنِّي أُكْرِمُهُ reads «then I honour him» (kasra) or «then my honouring him is settled» (fatḥa).",
         "What happens when إِنَّ is LIGHTENED to إِنْ? Its khabar must carry the telling lām (so no one hears the negative إِنْ), it may stop governing, and it may enter upon كَانَ and ظَنَّ: وَإِنْ كَانَتْ لَكَبِيرَةً (2:143), وَإِنْ نَظُنُّكَ لَمِنَ الْكَاذِبِينَ (26:186).",
         "And أَنَّ lightened to أَنْ? It governs a concealed pronoun of the matter (أَنَّهُ), needs a verb of certainty before it, and what follows is a full sentence: عَلِمْتُ أَنْ زَيْدٌ قَائِمٌ — زَيْدٌ in RAFʿ, a mubtada, never the ism of أَنْ.",
         "May the lightened أَنْ stand before a verb? Yes, any verb — but a conjugable verb (not a condition, not a prayer) must be parted from it by لَا, the sīn, سَوْفَ or قَدْ: عَلِمْتُ أَنْ لَا تَقُومُ (تَقُومُ in rafʿ!), عَلِمَ أَنْ سَيَكُونُ (73:20), عَلِمْتُ أَنْ قَدْ تَقُومُ.",
         "And when no parting letter is needed? Before a frozen verb (وَأَنْ عَسَى أَنْ يَكُونَ — 7:185), a condition (تَبَيَّنَتِ الْجِنُّ أَنْ لَوْ كَانُوا — 34:14) and a prayer (وَالْخَامِسَةُ أَنْ غَضِبَ اللهُ عَلَيْهَا — 24:9 in the reading غَضِبَ).",
         "And كَأَنَّ / لٰكِنَّ lightened? كَأَنْ is best left ungoverning (كَأَنْ ثَدْيَاهُ حُقَّانِ — a mubtada and khabar), لٰكِنْ MUST stop governing (وَلٰكِنْ عَمْرٌو حَاضِرٌ), and both may stand before a verb (كَأَنْ قَامَ زَيْدٌ، وَلٰكِنْ قَعَدَ).",
         "What does the engine READ here? The DabtEngine keeps a noun after the lightened أَنْ / كَأَنْ / لٰكِنْ in rafʿ as a mubtada, the muḍāriʿ after أَنْ لَا / أَنْ قَدْ in rafʿ (the maṣdar-making أَنْ never takes a parting letter), and the InnaEngine's seats — doer, object, mubtada, muḍāf ilayh, لَوْ, مَا, the jarr letters, مُذْ — give the fatḥa; the fāʾ of the answer gives both."],
  "tr": ["Hemze NEREDE fetha alır? Bir masdarın oturabileceği her yerde: FÂİL olarak (beleğanî enneke kâimün = bulûğu kıyâmike), MEF'ÛL olarak (alimtü enne), mukaddem haberden sonra MÜBTEDÂ olarak (indî enneke), MUZÂFUN İLEYH olarak (haysü enne).",
         "Hangi kelimelerden sonra? Lev ve levlâ'dan sonra (lev enneke kâimün = lev sebete kıyâmüke; levlâ enneke zâhibün = levlâ zehâbüke mevcûdün), zaman mâ'sından sonra (iclis mâ enne Zeyden kâimün = müddete sübûti kıyâmihî), cer harfinden sonra (min enneke), kelime atfeden hattâ'dan sonra (hattâ enneke sâlihun), müz / münzü'den sonra.",
         "İKİSİ ne zaman câiz? İki takdirin de mânâ verdiği yerde — cezâ fâsından sonra: men yükrimnî fe-innî ükrimuhû «ben de ona ikram ederim» (kesre) ya da «ona ikramım sâbittir» (fetha) okunur.",
         "İnne, in'e TAHFİF edilince ne olur? Haberi ayırıcı lâm taşımalı (nefy in'iyle karışmasın), amelden düşebilir ve kâne ile zanne'ye girebilir: ve in kânet le-kebîraten (2:143), ve in nezunnuke le-mine'l-kâzibîn (26:186).",
         "Ya enne, en'e tahfif edilince? Gizli bir şan zamirinde amel eder (ennehû), önünde tahkik fiili gerekir ve ardından tam cümle gelir: alimtü en Zeydün kâimün — Zeydün REF'te, mübtedâ, asla en'in ismi değil.",
         "Tahfif edilmiş en fiilin önüne gelebilir mi? Evet, her fiilin — fakat mutasarrıf fiil (şart ve dua değilse) ondan lâ, sîn, sevfe veya kad ile ayrılmalı: alimtü en lâ tekûmu (tekûmu merfû!), alime en seyekûnu (73:20), alimtü en kad tekûmu.",
         "Ayırıcı ne zaman gerekmez? Câmid fiilden önce (ve en asâ en yekûne — 7:185), şarttan önce (tebeyyeneti'l-cinnü en lev kânû — 34:14) ve duadan önce (ve'l-hâmisetü en gadiba'llâhu aleyhâ — 24:9, gadibe kıraatinde).",
         "Keenne / lâkinne tahfif edilince? Keen en fasih olarak amelsiz bırakılır (keen sedyâhu hukkân — mübtedâ ve haber), lâkin amelden düşmek ZORUNDADIR (ve lâkin Amrun hâdırun), ikisi de fiilin önüne gelebilir (keen kâme Zeyd, ve lâkin kaade).",
         "Motor burada neyi OKUR? DabtEngine tahfif edilmiş en / keen / lâkin'den sonraki ismi mübtedâ olarak ref'te tutar, en lâ / en kad'dan sonraki muzâriyi ref'te (masdariyye en asla ayırıcı almaz), InnaEngine'in yerleri — fâil, mef'ûl, mübtedâ, muzâfun ileyh, lev, mâ, cer harfleri, müz — fethayı verir; cezâ fâsı ikisini de."]
 },
 "plain": {"en": "Read أَنَّ with an a wherever you could swap in a plain noun of action (that you stand → your standing). Drop its shadda and it still works, but then a little helper (لَا, سَ, سَوْفَ, قَدْ) must stand between it and an ordinary verb; drop the shadda of إِنَّ and its khabar must carry a لَ.",
           "tr": "Yerine düz bir eylem ismi koyabildiğin her yerde enne'yi a ile oku (ayakta olduğun → ayakta durman). Şeddesini düşür, yine çalışır; ama o zaman onunla sıradan fiil arasında küçük bir yardımcı (lâ, se, sevfe, kad) durmalı; inne'nin şeddesini düşürürsen haberi bir le- taşımalı."},
 "explanation": {"en": "Birgivī's list of the fatḥa seats follows from one rule — أَنَّ with its clause is a maṣdar, so the fatḥa belongs wherever a maṣdar belongs: as a doer, an object, a mubtada, a muḍāf ilayh, after لَوْ / لَوْلَا (where the dropped verb or khabar is restored: لَوْ ثَبَتَ, مَوْجُودٌ), after the مَا of time (مُدَّةَ), after a jarr letter, after the ḥattā that joins a single word, after مُذْ / مُنْذُ. Where both estimations stand both readings stand — the fāʾ of the answer. The lightened forms: إِنْ keeps the telling lām in its khabar and may enter upon كَانَ / ظَنَّ; أَنْ governs the concealed pronoun of the matter, needs a verb of certainty before it, and before a conjugable verb (not a condition, not a prayer) takes لَا, the sīn, سَوْفَ or قَدْ as a parting letter — the verb staying in rafʿ; كَأَنْ is best ungoverning, لٰكِنْ must be, and both may precede a verb.",
                 "tr": "Birgivî'nin fetha yerleri tek kuraldan çıkar — enne cümlesiyle masdardır; öyleyse fetha, masdarın bulunduğu her yerdedir: fâil, mef'ûl, mübtedâ, muzâfun ileyh olarak; lev / levlâ'dan sonra (hazfedilen fiil veya haber geri konur: lev sebete, mevcûdün), zaman mâ'sından sonra (müddete), cer harfinden sonra, müfred atfeden hattâ'dan sonra, müz / münzü'den sonra. İki takdirin durduğu yerde iki okuyuş da durur — cezâ fâsı. Tahfif edilmiş şekiller: in, haberinde ayırıcı lâmı korur ve kâne / zanne'ye girebilir; en gizli şan zamirinde amel eder, önünde tahkik fiili ister ve mutasarrıf fiilden (şart ve dua dışında) lâ, sîn, sevfe veya kad ile ayrılır — fiil ref'te kalır; keen en iyisi amelsizdir, lâkin amelsiz olmak zorundadır, ikisi de fiilin önüne gelebilir."},
 "examples": [
  {"ar": "بَلَغَنِي أَنَّكَ قَائِمٌ، وَعَلِمْتُ أَنَّ زَيْدًا قَائِمٌ، وَعِنْدِي أَنَّكَ قَائِمٌ", "en": "the clause as a doer, an object, a mubtada — fatḥa", "tr": "cümle fâil, mef'ûl, mübtedâ olarak — fetha", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "لَوْ أَنَّكَ قَائِمٌ لَكَانَ كَذَا، أَيْ: لَوْ ثَبَتَ قِيَامُكَ", "en": "after لَوْ the clause is the doer of a dropped «were established»", "tr": "lev'den sonra cümle mahzûf «sâbit olsaydı»nın fâili", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "مَنْ يُكْرِمْنِي فَإِنِّي أُكْرِمُهُ", "en": "after the fāʾ of the answer both readings stand", "tr": "cezâ fâsından sonra iki vecih de câiz", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "وَإِنْ كَانَتْ لَكَبِيرَةً", "en": "the lightened إِنْ with its telling lām (2:143)", "tr": "ayırıcı lâmıyla tahfif edilmiş in (2:143)", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "عَلِمْتُ أَنْ زَيْدٌ قَائِمٌ", "en": "the lightened أَنْ: a mubtada in rafʿ follows, the ism is the concealed pronoun of the matter", "tr": "tahfif edilmiş en: ardından ref'te mübtedâ; isim gizli şan zamiri", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
  {"ar": "عَلِمْتُ أَنْ لَا تَقُومُ، وَعَلِمَ أَنْ سَيَكُونُ", "en": "a parting لَا / sīn before a conjugable verb, which stays in rafʿ (73:20)", "tr": "mutasarrıf fiil önünde ayırıcı lâ / sîn; fiil ref'te kalır (73:20)", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "وَلٰكِنْ عَمْرٌو حَاضِرٌ", "en": "the lightened لٰكِنْ must stop governing: ʿAmr is a mubtada", "tr": "tahfif edilmiş lâkin amelden düşmek zorunda: Amr mübtedâ", "sourceStory": "izhar-al-asrar", "sentence": "s10"},
 ],
 "commonMistakes": [
  {"wrong": "عَلِمْتُ أَنْ زَيْدًا قَائِمٌ", "right": "عَلِمْتُ أَنْ زَيْدٌ قَائِمٌ", "why": {"en": "the lightened أَنْ governs only the concealed pronoun of the matter — the noun after it is a mubtada in rafʿ", "tr": "tahfif edilmiş en yalnız gizli şan zamirinde amel eder — ardındaki isim ref'te mübtedâdır"}},
  {"wrong": "عَلِمْتُ أَنْ لَا تَقُومَ", "right": "عَلِمْتُ أَنْ لَا تَقُومُ", "why": {"en": "after a verb of certainty this أَنْ is the lightened one, not the maṣdar-maker — the verb stays in rafʿ, and لَا is only the parting letter", "tr": "tahkik fiilinden sonra bu en masdariyye değil, tahfif edilmiştir — fiil ref'te kalır, lâ yalnız ayırıcıdır"}},
  {"wrong": "وَلٰكِنْ عَمْرًا حَاضِرٌ", "right": "وَلٰكِنْ عَمْرٌو حَاضِرٌ", "why": {"en": "the lightened لٰكِنْ never governs — ʿAmr is a plain mubtada", "tr": "tahfif edilmiş lâkin asla amel etmez — Amr düz mübtedâdır"}},
 ],
}
ADD_EN = (" Chapter 5 (print pp. 96-98): where أَنَّ takes the fatḥa — as a doer, an object, a mubtada, a muḍāf ilayh, after لَوْ / لَوْلَا with the "
          "restored wording, after the مَا of time, after a jarr letter, the joining حَتَّى and مُذْ / مُنْذُ (s1-s4); where both readings stand, the fāʾ of the "
          "answer (s5); the lightened إِنْ with its telling lām and the verbs of the mubtada, 2:143 and 26:186 (s6); the lightened أَنْ with the "
          "pronoun of the matter, the verb of certainty before it, the parting لَا / sīn / سَوْفَ / قَدْ before a conjugable verb with 73:20 (s7-s8), none "
          "before a frozen verb, a condition or a prayer — 7:185, 34:14 and 24:9 in the reading أَنْ غَضِبَ اللهُ that the print carries (s9); the lightened "
          "كَأَنْ and لٰكِنْ (s10). Two places the lithograph's transcription is garbled and the received wording is given: the shāhid «كَأَنْ ثَدْيَاهُ حُقَّانِ» "
          "(the transcription reads كأن ذا ناب حقا) and «فَيَجِبُ إِلْغَاؤُهَا» (the transcription reads الفاء وهما).")
ADD_TR = (" Beşinci bab (baskı s. 96-98): enne'nin fetha yerleri — fâil, mef'ûl, mübtedâ, muzâfun ileyh olarak; takdiriyle lev / levlâ'dan sonra; zaman "
          "mâ'sından, cer harfinden, atfeden hattâ'dan ve müz / münzü'den sonra (s1-s4); iki vechin câiz olduğu cezâ fâsı (s5); ayırıcı lâmı ve mübtedâ "
          "fiilleriyle tahfif edilmiş in, 2:143 ve 26:186 (s6); şan zamiri, önündeki tahkik fiili ve mutasarrıf fiil önünde ayırıcı lâ / sîn / sevfe / kad "
          "ile tahfif edilmiş en, 73:20 (s7-s8); câmid fiil, şart ve dua önünde ayırıcısız — 7:185, 34:14 ve baskının taşıdığı en gadiba'llâhu kıraatiyle "
          "24:9 (s9); tahfif edilmiş keen ve lâkin (s10). Taşbaskı transkripsiyonu iki yerde bozuk olduğundan alınan metin verilmiştir: «keen sedyâhu "
          "hukkân» şâhidi (transkripsiyon: كأن ذا ناب حقا) ve «fe-yecibü ilgâuhâ» (transkripsiyon: الفاء وهما).")
write_out(5, S, TITLE, ADD_EN, ADD_TR, "pp. 96-98", GLOSS_ADD, notes=(NOTE,),
          related=((IW, [K]), (IA, [K]), (K4, [K]), ("an-masdariyya", [K]), ("kana-wa-akhawatuha", [K]), ("zanna-wa-akhawatuha", [K])))
report(5, S, GLOSS_ADD, (NOTE,))
