# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 44: the FĀʾ obligatory in the requital — a nominal sentence, a non-conjugable māḍī or its like (then قَدْ, shown or
# estimated, is a must), a muḍāriʿ joined to the sīn, سَوْفَ, لَنْ or مَا, or a performative verbal sentence (command, prohibition, question, prayer):
# إِنْ ضَرَبْتَ فَأَنْتَ مَضْرُوبٌ; Āl ʿImrān 3:28, al-Nisāʾ 4:19, Yūsuf 12:26, al-Ṭalāq 65:6, Āl ʿImrān 3:85; إِنْ ضَرَبَكَ زَيْدٌ فَاضْرِبْهُ / فَلَا تَضْرِبْهُ /
# فَهَلْ تَضْرِبُهُ، إِنْ تُكْرِمْنِي فَيَرْحَمْكَ اللهُ; an affirmed muḍāriʿ or one negated by لَا: the fāʾ with rafʿ, or no fāʾ with jazm (إِنْ تَضْرِبْ أَضْرِبْ / فَأَضْرِبُ /
# لَا أَضْرِبْ / فَلَا أَضْرِبُ). Print pp. 140–141.
#   python3 author_izhar_ch44.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; FK = "fa-khabar-mubtada"; JT_ = "jawab-al-talab"; LJ = "lam-jazim"; AJ = "anwa-al-jumal"; KI = "khabar-insha"; IMP = "imperative-amr"; NH = "la-nahiya"; QH = "qad-harf"; TN = "al-fil-al-tamm-wal-naqis"; MQB = "afal-al-muqaraba"
K = "al-fa-fi-jawab-al-shart"
K43 = "al-majzum-wal-shart-wal-jaza"
TITLE = {"ar": "الْفَاءُ فِي جَوَابِ الشَّرْطِ: مَوَاضِعُ وُجُوبِهَا وَجَوَازِهَا", "en": "The fāʾ in the answer of the condition: where it is obligatory and where allowed", "tr": "Şartın cevâbında fâ: vücûb ve cevâz yerleri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def in_(gr=None, joined=None): 
    if joined == "wa": return tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS] + (gr or []), "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part"))
    if joined == "fa": return tok("فَإِنْ", "in-shartiyya", "part", [K, AT, INS] + (gr or []), "الْفَاءُ لِلِاسْتِئْنَافِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if»", "«eğer»", segments=fa("إِنْ", "in-shartiyya", "part"))
    return tok("إِنْ", "in-shartiyya", "part", [K, INS] + (gr or []), "لَفْظٌ مَحْكِيٌّ: حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»")
def fajawab(form, lex, pos, gr, ar, en, tr, punct=None, extra=None):
    return tok(form, lex, pos, [K, FK, INS] + gr, "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، " + ar, en, tr, punct=punct, segments=[seg("فَ", "fa", "conj")] + (extra or [seg(form[1:], lex, pos)]))

# ----------- s1 — the nominal and the non-conjugable māḍī requital
S.append({"id": "s1", "translation": {"en": "And if the requital is a nominal sentence, or a non-conjugable māḍī one, or one in its sense — then «qad», shown or estimated, is a must —", "tr": "Cezâ isim cümlesi, mutasarrıf olmayan mâzî cümle ya da onun mânâsında ise — o zaman açık veya takdîrî bir kad zorunludur —"},
 "tokens": [
  in_(joined="wa"),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، فِعْلُ الشَّرْطِ.", "«is»", "«olursa»"),
  tok("الْجَزَاءُ", "jaza-answer", "noun", [K, KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«the requital»", "«cezâ»"),
  tok("جُمْلَةً", "jumla", "noun", [K, KN, AJ], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a sentence»", "«bir cümle»"),
  tok("اسْمِيَّةً", "ismiyya", "noun", [K, NA, NSB, AJ], "نَعْتٌ مَنْصُوبٌ.", "«nominal»", "«isim cümlesi»", punct="،"),
  aw(),
  tok("مَاضِيَةً", "madi", "noun", [K, AT, NA, AJ], "مَعْطُوفٌ عَلَى اسْمِيَّةً مَنْصُوبٌ — جُمْلَةً مَاضِيَةً.", "«a māḍī one»", "«mâzî cümle»"),
  tok("غَيْرَ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ مَنْصُوبٌ، مُضَافٌ.", "«non-»", "«olmayan»"),
  tok("مُتَصَرِّفَةٍ", "mutasarrif", "noun", [K, ID, IFA, F5], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — كَلَيْسَ وَعَسَى وَنِعْمَ.", "«conjugable» — as laysa, ʿasā, niʿma.", "«mutasarrıf» — leyse, asâ, ni'me gibi."),
  aw(),
  tok("بِمَعْنَاهُ", "mana", "noun", [K, AT, HJ, ID, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَاهُ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بِمَعْنَى الْمَاضِي غَيْرِ الْمُتَصَرِّفِ.", "«in its sense»", "«onun mânâsında»", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  tok("فَلَا", "la-nafiya", "part", [K, AT, LN], "الْفَاءُ لِلِاعْتِرَاضِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«then no»", "«o zaman … yok»", segments=fa("لَا", "la-nafiya", "part")),
  tok("بُدَّ", "budd", "noun", [K, LN, MK], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«escape» — a must.", "«çâre» — zorunlu."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("قَدْ", "qad", "part", [K, HJ, QH], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — قَدِ التَّحْقِيقِ قَبْلَ الْمَاضِي.", "«qad» — before the māḍī.", "«kad» — mâzîden önce."),
  tok("ظَاهِرَةً", "zahir", "noun", [K, "hal", IFA], "حَالٌ مَنْصُوبٌ.", "«shown»", "«açık»"),
  aw(),
  tok("مُقَدَّرَةً", "muqaddar", "noun", [K, AT, IMF, F2, HT], "مَعْطُوفٌ مَنْصُوبٌ.", "«estimated»", "«takdîrî»", punct="،"),
 ]})
# ----------- s2 — the muḍāriʿ with sīn/sawfa/lan/mā; the performative verbal sentence
S.append({"id": "s2", "translation": {"en": "or a muḍāriʿ joined to the sīn, or «sawfa», or «lan», or «mā», or a performative verbal sentence — the command, the prohibition, the question and the prayer — the entering of the fāʾ into it is obligatory;", "tr": "ya da sîn, sevfe, len veya mâ'ya bitişik bir muzâri, ya da inşâî bir fiil cümlesi — emir, nehiy, istifhâm ve duâ gibi — ise ona fâ'nın girmesi vâcibdir;"},
 "tokens": [
  aw(),
  tok("مُضَارِعًا", "mudari", "noun", [K, AT, KN], "مَعْطُوفٌ عَلَى خَبَرِ كَانَ مَنْصُوبٌ.", "«a muḍāriʿ»", "«muzâri»"),
  tok("مُقْتَرِنًا", "muqtarin", "noun", [K, NA, IFA, "form-viii-verbs"], "نَعْتٌ مَنْصُوبٌ.", "«joined»", "«bitişik»"),
  tok("بِالسِّينِ", "sin-letter", "noun", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالسِّينِ مَجْرُورٌ — سِينُ الِاسْتِقْبَالِ.", "«to the sīn» — of the future.", "«sîn'e» — istikbâl sîni.", segments=[seg("بِ", "bi", "prep"), seg("السِّينِ", "sin-letter", "noun")]),
  aw(),
  tok("سَوْفَ", "sawfa", "part", [K, AT], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«sawfa»", "«sevfe»"),
  aw(),
  tok("لَنْ", "lan", "part", [K, AT, JZ], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«lan»", "«len»"),
  aw(),
  tok("مَا", "ma-nafiya", "part", [K, AT], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مَا النَّافِيَةُ.", "«mā»", "«mâ»", punct="،"),
  aw(),
  tok("فِعْلِيَّةً", "filiyya", "noun", [K, AT, KN, AJ, NSB], "مَعْطُوفٌ عَلَى جُمْلَةً مَنْصُوبٌ — جُمْلَةً فِعْلِيَّةً.", "«a verbal one»", "«fiil cümlesi»"),
  tok("إِنْشَائِيَّةً", "inshaiyya", "noun", [K, NA, NSB, KI], "نَعْتٌ مَنْصُوبٌ.", "«performative»", "«inşâî»"),
  tok("كَالْأَمْرِيَّةِ", "amriyya", "noun", [K, HJ, NSB, IMP], "الْكَافُ حَرْفُ جَرٍّ، وَالْأَمْرِيَّةِ مَجْرُورٌ.", "«as the command»", "«emir cümlesi gibi»", segments=[seg("كَ", "ka", "prep"), seg("الْأَمْرِيَّةِ", "amriyya", "noun")]),
  tok("وَالنَّهْيِيَّةِ", "nahyiyya", "noun", [K, AT, NSB, NH], "الْوَاوُ عَاطِفَةٌ، وَالنَّهْيِيَّةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the prohibition»", "«ve nehiy»", segments=wa("النَّهْيِيَّةِ", "nahyiyya", "noun")),
  tok("وَالِاسْتِفْهَامِيَّةِ", "istifhamiyya", "noun", [K, AT, NSB, IST], "الْوَاوُ عَاطِفَةٌ، وَالِاسْتِفْهَامِيَّةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the question»", "«ve istifhâm»", segments=wa("الِاسْتِفْهَامِيَّةِ", "istifhamiyya", "noun")),
  tok("وَالدُّعَائِيَّةِ", "duaiyya", "noun", [K, AT, NSB, KI], "الْوَاوُ عَاطِفَةٌ، وَالدُّعَائِيَّةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the prayer»", "«ve duâ»", punct="،", segments=wa("الدُّعَائِيَّةِ", "duaiyya", "noun")),
  tok("يَجِبُ", "wajaba", "verb", [K, INS, MR, FL, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — جَوَابُ الشَّرْطِ بِلَا فَاءٍ لِكَوْنِهِ مُضَارِعًا مُثْبَتًا.", "«it is obligatory» — the answer, itself a fāʾ-less muḍāriʿ.", "«vâcibdir» — cevap; kendisi fâsız müsbet muzâri."),
  tok("دُخُولُ", "dukhul", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the entering of»", "«girmesi»"),
  tok("الْفَاءِ", "fa", "conj", [K, ID, FK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the fāʾ»", "«fâ'nın»"),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — فِي الْجَزَاءِ.", "«into it»", "«ona»", punct="،", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
 ]})
# ----------- s3 — the nominal requital; Āl ʿImrān 3:28
S.append({"id": "s3", "translation": {"en": "as in «if you strike, then you are struck», and as in His saying, exalted be He: «and whoever does that has nothing to do with God» (Āl ʿImrān 3:28),", "tr": "«vurursan, sen vurulansın» gibi; ve Allah Teâlâ'nın «kim bunu yaparsa Allah ile hiçbir ilgisi kalmaz» (Âl-i İmrân 3:28) sözü gibi,"},
 "tokens": [
  nahw(), in_(),
  tok("ضَرَبْتَ", "daraba", "verb", [K, INS, FL], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«you strike»", "«vurursan»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تَ", "pron-2ms", "pron")]),
  fajawab("فَأَنْتَ", "anta", "pron", [MK], "وَأَنْتَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْجَوَابُ جُمْلَةٌ اسْمِيَّةٌ.", "«then you» — a nominal answer.", "«sen» — isim cümlesi cevap."),
  tok("مَضْرُوبٌ", "madrub", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«struck»", "«vurulansın»", punct="،"),
  tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", segments=wa("نَحْوُ", "nahw", "noun")),
  tok("قَوْلِهِ", "qawl", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ.", "«exalted be He»", "«Teâlâ»", punct=":"),
  tok("وَمَنْ", "man-shartiyya", "pron", [K, AT, INS], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«and whoever» — the conditional noun.", "«ve kim» — şart ismi.", segments=wa("مَنْ", "man-shartiyya", "pron")),
  tok("يَفْعَلْ", "faala", "verb", [K, INS, FL, JZ], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«does» — the jazm'd condition.", "«yaparsa» — cezimli şart."),
  tok("ذٰلِكَ", "dhalika", "pron", [K, MB], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ.", "«that»", "«bunu»"),
  fajawab("فَلَيْسَ", "laysa", "verb", [TN, KN], "وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ غَيْرُ مُتَصَرِّفٍ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْجَوَابُ مَاضٍ غَيْرُ مُتَصَرِّفٍ.", "«then he is not» — a non-conjugable māḍī answer.", "«o … değildir» — mutasarrıf olmayan mâzî cevap."),
  tok("مِنَ", "min", "prep", [K, HJ, KN], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ.", "«of» — the phrase as khabar of laysa.", "«-den» — leyse'nin haberi."),
  tok("اللهِ", "allah", "propn", [K, HJ], "مَجْرُورٌ بِمِنْ.", "«God»", "«Allah»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("شَيْءٍ", "shay", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«anything»", "«hiçbir şey»", punct="،"),
 ]})
# ----------- s4 — al-Nisāʾ 4:19 (ʿasā), Yūsuf 12:26 (the māḍī with qad)
S.append({"id": "s4", "translation": {"en": "«and if you dislike them, then it may be that you dislike a thing» (al-Nisāʾ 4:19), «and if his shirt has been torn from the front, then she has told the truth» (Yūsuf 12:26),", "tr": "«onlardan hoşlanmazsanız, olabilir ki bir şeyden hoşlanmazsınız» (Nisâ 4:19), «eğer gömleği önden yırtılmışsa, kadın doğru söylemiştir» (Yûsuf 12:26),"},
 "tokens": [
  in_(joined="fa"),
  tok("كَرِهْتُمُوهُنَّ", "kariha", "verb", [K, INS, FL, MB], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ، وَالْوَاوُ لِلْإِشْبَاعِ، وَهُنَّ مَفْعُولٌ بِهِ.", "«you dislike them»", "«onlardan hoşlanmazsanız»", segments=[seg("كَرِهْ", "kariha", "verb"), seg("تُمُو", "pron-2mp", "pron"), seg("هُنَّ", "pron-3fp", "pron")]),
  fajawab("فَعَسَى", "asa-hope", "verb", [MQB, HV], "وَعَسَى فِعْلٌ مَاضٍ جَامِدٌ لِلرَّجَاءِ — الْجَوَابُ مَاضٍ غَيْرُ مُتَصَرِّفٍ.", "«then it may be» — the non-conjugable ʿasā.", "«olabilir ki» — mutasarrıf olmayan asâ."),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, MQB], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ.", "«that»", "«-manız»"),
  tok("تَكْرَهُوا", "kariha", "verb", [K, AMS, FL, MQB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْمَصْدَرُ فَاعِلُ عَسَى.", "«you dislike» — the maṣdar the doer of ʿasā.", "«hoşlanmazsınız» — mastar asâ'nın fâili.", segments=[seg("تَكْرَهُ", "kariha", "verb"), seg("وا", "pron-2mp", "pron")]),
  tok("شَيْئًا", "shay", "noun", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a thing»", "«bir şeyden»", punct="،"),
  in_(joined="wa"),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، فِعْلُ الشَّرْطِ.", "«is»", "«ise»"),
  tok("قَمِيصُهُ", "qamis", "noun", [K, KN, ID], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his shirt»", "«gömleği»", segments=[seg("قَمِيصُ", "qamis", "noun"), pr3ms()]),
  tok("قُدَّ", "qadda", "verb", [K, KN, NF, "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كَانَ.", "«has been torn» — the clause the khabar of kāna.", "«yırtılmış» — cümle kâne'nin haberi."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("قُبُلٍ", "qubul", "noun", [K, HJ], "مَجْرُورٌ بِمِنْ.", "«the front»", "«ön»"),
  fajawab("فَصَدَقَتْ", "sadaqa-be-true", "verb", [FL, QH], "وَصَدَقَتْ فِعْلٌ مَاضٍ مُتَصَرِّفٌ بِمَعْنَى الْمَاضِي، وَالتَّاءُ لِلتَّأْنِيثِ — الْجَوَابُ مَاضٍ مَعَ قَدٍ الْمُقَدَّرَةِ: فَقَدْ صَدَقَتْ.", "«then she has told the truth» — a māḍī answer with qad estimated: فَقَدْ صَدَقَتْ.", "«doğru söylemiştir» — takdîrî kad ile mâzî cevap: fe-kad sadakat.", punct="،", extra=[seg("صَدَقَ", "sadaqa-be-true", "verb"), seg("تْ", "ta-tanith", "part")]),
 ]})
# ----------- s5 — al-Ṭalāq 65:6 (the sīn), Āl ʿImrān 3:85 (lan)
S.append({"id": "s5", "translation": {"en": "«and if you find it hard, then another woman shall suckle for him» (al-Ṭalāq 65:6), «and whoever seeks a religion other than Islam, it shall never be accepted of him» (Āl ʿImrān 3:85),", "tr": "«güçlük çekerseniz, onun için başka bir kadın emzirecektir» (Talâk 65:6), «kim İslâm'dan başka bir din ararsa, ondan asla kabul edilmeyecektir» (Âl-i İmrân 3:85),"},
 "tokens": [
  in_(joined="wa"),
  tok("تَعَاسَرْتُمْ", "taasara", "verb", [K, INS, FL, "form-vi-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ، وَالْمِيمُ لِلْجَمْعِ.", "«you find it hard»", "«güçlük çekerseniz»", segments=[seg("تَعَاسَرْ", "taasara", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  fajawab("فَسَتُرْضِعُ", "ardaa", "verb", [MR, FL, F4], "وَالسِّينُ لِلِاسْتِقْبَالِ، وَتُرْضِعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — الْجَوَابُ مُضَارِعٌ مُقْتَرِنٌ بِالسِّينِ.", "«then shall suckle» — a muḍāriʿ with the sīn.", "«emzirecektir» — sîn'li muzâri.", extra=[seg("سَ", "sa-istiqbal", "part"), seg("تُرْضِعُ", "ardaa", "verb")]),
  tok("لَهُ", "li", "prep", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«for him»", "«onun için»", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  tok("أُخْرَى", "ukhra", "noun", [K, FL, MQ, "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«another woman»", "«başka bir kadın»", punct="،"),
  tok("وَمَنْ", "man-shartiyya", "pron", [K, AT, INS], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.", "«and whoever»", "«ve kim»", segments=wa("مَنْ", "man-shartiyya", "pron")),
  tok("يَبْتَغِ", "ibtagha", "verb", [K, INS, FL, JZ, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ حَرْفِ الْعِلَّةِ، فِعْلُ الشَّرْطِ.", "«seeks» — jazm by the dropped weak letter.", "«ararsa» — illet harfinin hazfiyle cezm."),
  tok("غَيْرَ", "ghayr", "noun", [K, MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«other than»", "«-dan başka»"),
  tok("الْإِسْلَامِ", "islam", "noun", [K, ID, MSD, F4], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Islam»", "«İslâm»"),
  tok("دِينًا", "din", "noun", [K, TMZ], "تَمْيِيزٌ مَنْصُوبٌ — أَوْ حَالٌ.", "«as a religion»", "«din olarak»"),
  fajawab("فَلَنْ", "lan", "part", [JZ], "وَلَنْ حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ — الْجَوَابُ مُضَارِعٌ مُقْتَرِنٌ بِلَنْ.", "«then never» — the answer with lan.", "«asla» — len'li cevap."),
  tok("يُقْبَلَ", "qabila", "verb", [K, JZ, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِلَنْ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«it be accepted»", "«kabul edilecek»"),
  tok("مِنْهُ", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«of him»", "«ondan»", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
 ]})
# ----------- s6 — the performative requitals
S.append({"id": "s6", "translation": {"en": "and as in «if Zayd strikes you, then strike him», or «then do not strike him», or «then do you strike him?», and «if you honour me, then may God have mercy on you»;", "tr": "«Zeyd seni vurursa onu vur», veya «onu vurma», veya «onu vurur musun?» gibi; ve «bana ikram edersen Allah sana rahmet etsin» gibi;"},
 "tokens": [
  tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«and as in»", "«ve … gibi»", punct=":", segments=wa("نَحْوُ", "nahw", "noun")),
  in_(),
  tok("ضَرَبَكَ", "daraba", "verb", [K, INS, FL, MB], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ، فِعْلُ الشَّرْطِ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«strikes you»", "«seni vurursa»", segments=[seg("ضَرَبَ", "daraba", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("زَيْدٌ", "zayd", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd»", "«Zeyd»"),
  fajawab("فَاضْرِبْهُ", "daraba", "verb", [IMP, MB], "وَاضْرِبْهُ فِعْلُ أَمْرٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجَوَابُ أَمْرِيٌّ.", "«then strike him» — a command answer.", "«onu vur» — emir cevap.", punct="،", extra=[seg("اضْرِبْ", "daraba", "verb"), pr3ms()]),
  aw(),
  fajawab("فَلَا", "la-nahiya", "part", [NH], "وَلَا نَاهِيَةٌ — الْجَوَابُ نَهْيِيٌّ.", "«then do not» — a prohibition answer.", "«… -ma» — nehiy cevap."),
  tok("تَضْرِبْهُ", "daraba", "verb", [K, NH, JZ, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«strike him»", "«onu vurma»", punct="،", segments=[seg("تَضْرِبْ", "daraba", "verb"), pr3ms()]),
  aw(),
  fajawab("فَهَلْ", "hal-istifham", "part", [IST], "وَهَلْ حَرْفُ اسْتِفْهَامٍ — الْجَوَابُ اسْتِفْهَامِيٌّ.", "«then do you?» — a question answer.", "«… mu?» — istifhâm cevap."),
  tok("تَضْرِبُهُ", "daraba", "verb", [K, IST, MR, MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«you strike him»", "«onu vurur»", punct="،", segments=[seg("تَضْرِبُ", "daraba", "verb"), pr3ms()]),
  in_(joined="wa"),
  tok("تُكْرِمْنِي", "akrama", "verb", [K, INS, FL, JZ, MB, F4], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، فِعْلُ الشَّرْطِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you honour me»", "«bana ikram edersen»", segments=[seg("تُكْرِمْ", "akrama", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  fajawab("فَيَرْحَمْكَ", "rahima", "verb", [JZ, MB, KI], "وَيَرْحَمْكَ فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي مَعْنَى الدُّعَاءِ، وَالْكَافُ مَفْعُولٌ بِهِ — الْجَوَابُ دُعَائِيٌّ.", "«then may He have mercy on you» — a prayer answer.", "«sana rahmet etsin» — duâ cevap.", extra=[seg("يَرْحَمْ", "rahima", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("اللهُ", "allah", "propn", [K, FL], "فَاعِلٌ مَرْفُوعٌ.", "«God»", "«Allah»", punct="،"),
 ]})
# ----------- s7 — the plain muḍāriʿ: fāʾ with rafʿ, none with jazm
S.append({"id": "s7", "translation": {"en": "and if it is a muḍāriʿ other than these, affirmed or negated by «lā», the fāʾ with rafʿ and its dropping with jazm are both allowed — as in «if you strike, I strike» or «then I strike», or «I do not strike» or «then I do not strike».", "tr": "bunların dışında müsbet ya da lâ ile menfî bir muzâri ise ref' ile fâ da, cezm ile fâ'nın hazfi de câizdir — «vurursan vururum» veya «o zaman vururum», veya «vurmam» veya «o zaman vurmam» gibi."},
 "tokens": [
  in_(joined="wa"),
  tok("كَانَ", "kana", "verb", [K, KN, INS, HV], "فِعْلٌ مَاضٍ نَاقِصٌ، فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْجَزَاءُ.", "«it is» — the requital.", "«olursa» — cezâ."),
  tok("مُضَارِعًا", "mudari", "noun", [K, KN], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a muḍāriʿ»", "«muzâri»"),
  tok("غَيْرَهَا", "ghayr", "noun", [K, NA, ID], "نَعْتٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — غَيْرَ الْمَذْكُورَاتِ.", "«other than these»", "«bunların dışında»", segments=[seg("غَيْرَ", "ghayr", "noun"), pr3fs()]),
  tok("مُثْبَتًا", "muthbat", "noun", [K, "hal", IMF, F4], "حَالٌ مَنْصُوبٌ.", "«affirmed»", "«müsbet»"),
  aw(),
  tok("مَنْفِيًّا", "manfi", "noun", [K, AT, IMF], "مَعْطُوفٌ مَنْصُوبٌ.", "«negated»", "«menfî»"),
  tok("بِلَا", "la-nafiya", "part", [K, HJ, LN], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«by lā»", "«lâ ile»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part")]),
  tok("فَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, MR, INS], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«then it is allowed»", "«o zaman câizdir»", segments=fa("يَجُوزُ", "jaaza", "verb")),
  tok("الْفَاءُ", "fa", "conj", [K, FL, FK], "فَاعِلٌ مَرْفُوعٌ.", "«the fāʾ»", "«fâ»"),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("الرَّفْعِ", "raf", "noun", [K, ID, MSD, MR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rafʿ»", "«ref'»"),
  tok("وَحَذْفُهُ", "hadhf", "noun", [K, AT, FL, ID, MSD, HT], "الْوَاوُ عَاطِفَةٌ، وَحَذْفُهُ مَعْطُوفٌ عَلَى الْفَاءُ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its dropping»", "«ve hazfi»", segments=[seg("وَ", "wa", "conj"), seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("الْجَزْمِ", "jazm", "noun", [K, ID, MSD, JZ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jazm»", "«cezm»", punct="،"),
  nahw(), in_(),
  tok("تَضْرِبْ", "daraba", "verb", [K, INS, JZ, FL], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، فِعْلُ الشَّرْطِ.", "«you strike»", "«vurursan»"),
  tok("أَضْرِبْ", "daraba", "verb", [K, INS, JZ, FL], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، جَوَابُ الشَّرْطِ بِلَا فَاءٍ.", "«I strike» — jazm, no fāʾ.", "«vururum» — cezm, fâsız."),
  aw(),
  fajawab("فَأَضْرِبُ", "daraba", "verb", [MR, FL], "وَأَضْرِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — الْجَوَابُ مَعَ الْفَاءِ مَرْفُوعٌ.", "«then I strike» — rafʿ with the fāʾ.", "«o zaman vururum» — fâ ile ref'.", punct="،"),
  aw(),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-mam»"),
  tok("أَضْرِبْ", "daraba", "verb", [K, LN, INS, JZ, FL], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، جَوَابُ الشَّرْطِ بِلَا فَاءٍ.", "«I strike» — jazm, no fāʾ.", "«vurmam» — cezm, fâsız."),
  aw(),
  fajawab("فَلَا", "la-nafiya", "part", [LN], "وَلَا نَافِيَةٌ.", "«then not»", "«o zaman … -mam»"),
  tok("أَضْرِبُ", "daraba", "verb", [K, LN, MR, FL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مَعَ الْفَاءِ.", "«I strike» — rafʿ with the fāʾ.", "«vururum» — fâ ile ref'.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "inshaiyya": G("inshaiyya", "إِنْشَائِيَّة", "ن ش أ", "noun", "performative (of a sentence) — commanding, asking, praying, not stating", "inşâî (cümle) — emreden, soran, duâ eden; bildirmeyen", 4),
 "amriyya": G("amriyya", "أَمْرِيَّة", "أ م ر", "noun", "of command (a sentence of the imperative)", "emir cümlesi niteliğinde", 4),
 "nahyiyya": G("nahyiyya", "نَهْيِيَّة", "ن ه ي", "noun", "of prohibition (a sentence of the prohibitive)", "nehiy cümlesi niteliğinde", 4),
 "istifhamiyya": G("istifhamiyya", "اسْتِفْهَامِيَّة", "ف ه م", "noun", "interrogative (a sentence of question)", "istifhâm cümlesi niteliğinde", 4),
 "duaiyya": G("duaiyya", "دُعَائِيَّة", "د ع و", "noun", "of prayer (a sentence of supplication)", "duâ cümlesi niteliğinde", 4),
 "qubul": G("qubul", "قُبُل", "ق ب ل", "noun", "the front, the fore part", "ön, ön taraf", 3),
 "taasara": G("taasara", "تَعَاسَرَ", "ع س ر", "verb", "to make things hard for one another, to be at odds (form VI)", "birbirine güçlük çıkarmak, anlaşamamak (VI. bab)", 4, form="VI"),
 "ardaa": G("ardaa", "أَرْضَعَ", "ر ض ع", "verb", "to suckle, to nurse a child (form IV)", "emzirmek (IV. bab)", 3, form="IV"),
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
put_morph(mo, "taasara", {"bab": "الْبَابُ السَّادِسُ تَفَاعَلَ", "wazn": "تَفَاعَلَ يَتَفَاعَلُ", "masdar": "تَعَاسُر", "ismFail": "مُتَعَاسِر",
 "mazi": ["تَعَاسَرَ", "تَعَاسَرَا", "تَعَاسَرُوا", "تَعَاسَرَتْ", "تَعَاسَرَتَا", "تَعَاسَرْنَ", "تَعَاسَرْتَ", "تَعَاسَرْتُمَا", "تَعَاسَرْتُمْ", "تَعَاسَرْتِ", "تَعَاسَرْتُمَا", "تَعَاسَرْتُنَّ", "تَعَاسَرْتُ", "تَعَاسَرْنَا"],
 "mudari": ["يَتَعَاسَرُ", "يَتَعَاسَرَانِ", "يَتَعَاسَرُونَ", "تَتَعَاسَرُ", "تَتَعَاسَرَانِ", "يَتَعَاسَرْنَ", "تَتَعَاسَرُ", "تَتَعَاسَرَانِ", "تَتَعَاسَرُونَ", "تَتَعَاسَرِينَ", "تَتَعَاسَرَانِ", "تَتَعَاسَرْنَ", "أَتَعَاسَرُ", "نَتَعَاسَرُ"],
 "amr": ["تَعَاسَرْ", "تَعَاسَرَا", "تَعَاسَرُوا", "تَعَاسَرِي", "تَعَاسَرَا", "تَعَاسَرْنَ"], "mansub": "يَتَعَاسَرَ", "majzum": "يَتَعَاسَرْ", "majzum2": "تَتَعَاسَرْ",
 "note": "تَعَاسَرَ الْقَوْمُ يَتَعَاسَرُونَ تَعَاسُرًا: شَدَّدَ بَعْضُهُمْ عَلَى بَعْضٍ — مِنَ الْبَابِ السَّادِسِ لِلْمُشَارَكَةِ، لَازِمٌ."})
put_morph(mo, "ardaa", {"bab": "الْبَابُ الرَّابِعُ أَفْعَلَ", "wazn": "أَفْعَلَ يُفْعِلُ", "masdar": "إِرْضَاع", "ismFail": "مُرْضِع",
 "mazi": ["أَرْضَعَ", "أَرْضَعَا", "أَرْضَعُوا", "أَرْضَعَتْ", "أَرْضَعَتَا", "أَرْضَعْنَ", "أَرْضَعْتَ", "أَرْضَعْتُمَا", "أَرْضَعْتُمْ", "أَرْضَعْتِ", "أَرْضَعْتُمَا", "أَرْضَعْتُنَّ", "أَرْضَعْتُ", "أَرْضَعْنَا"],
 "mudari": ["يُرْضِعُ", "يُرْضِعَانِ", "يُرْضِعُونَ", "تُرْضِعُ", "تُرْضِعَانِ", "يُرْضِعْنَ", "تُرْضِعُ", "تُرْضِعَانِ", "تُرْضِعُونَ", "تُرْضِعِينَ", "تُرْضِعَانِ", "تُرْضِعْنَ", "أُرْضِعُ", "نُرْضِعُ"],
 "amr": ["أَرْضِعْ", "أَرْضِعَا", "أَرْضِعُوا", "أَرْضِعِي", "أَرْضِعَا", "أَرْضِعْنَ"], "mansub": "يُرْضِعَ", "majzum": "يُرْضِعْ", "majzum2": "تُرْضِعْ",
 "note": "أَرْضَعَتِ الْأُمُّ وَلَدَهَا تُرْضِعُهُ إِرْضَاعًا: أَلْقَمَتْهُ ثَدْيَهَا — مِنَ الْبَابِ الرَّابِعِ، مُتَعَدٍّ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch44 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "daraba", "faala", "laysa", "kariha", "qadda", "ibtagha", "qabila", "akrama", "rahima", "jaaza", "wajaba") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْفَاءُ فِي جَوَابِ الشَّرْطِ: وُجُوبُهَا فِي الِاسْمِيَّةِ وَالْجَامِدِ وَالسِّينِ وَسَوْفَ وَلَنْ وَمَا وَالْإِنْشَاءِ، وَجَوَازُهَا فِي الْمُضَارِعِ", "en": "The fāʾ in the answer of the condition: obligatory with the nominal, the non-conjugable, the sīn, sawfa, lan, mā and the performative; allowed with the plain muḍāriʿ", "tr": "Şartın cevâbında fâ: isim cümlesi, câmid fiil, sîn, sevfe, len, mâ ve inşâ ile vâcib; düz muzâri ile câiz"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المجزوم: الفاء في الجزاء", "الكافية لابن الحاجب — الجوازم", "مغني اللبيب لابن هشام — الفاء الرابطة للجواب"],
 "amil": "the fāʾ must enter the requital when it cannot carry the jazm: a nominal sentence (إِنْ ضَرَبْتَ فَأَنْتَ مَضْرُوبٌ), a non-conjugable māḍī or its like (فَلَيْسَ، فَعَسَى) — and a conjugable māḍī requital of past sense needs قَدْ shown or estimated (فَصَدَقَتْ = فَقَدْ صَدَقَتْ) — a muḍāriʿ joined to the sīn, سَوْفَ, لَنْ or مَا (فَسَتُرْضِعُ، فَلَنْ يُقْبَلَ), or a performative verbal sentence: command, prohibition, question, prayer (فَاضْرِبْهُ، فَلَا تَضْرِبْهُ، فَهَلْ تَضْرِبُهُ، فَيَرْحَمْكَ اللهُ); a plain muḍāriʿ, affirmed or negated by لَا, takes the fāʾ with rafʿ or no fāʾ with jazm (إِنْ تَضْرِبْ أَضْرِبْ / فَأَضْرِبُ / لَا أَضْرِبْ / فَلَا أَضْرِبُ)",
 "question": {
  "en": ["Why does a requital need the fāʾ at all? Because a requital that cannot carry the jazm must be tied to its condition by a binder, and the fāʾ is that binder.",
         "Which requitals take the fāʾ of necessity? The nominal sentence (فَأَنْتَ مَضْرُوبٌ); the non-conjugable māḍī or its like (فَلَيْسَ مِنَ اللهِ، فَعَسَى أَنْ تَكْرَهُوا); the muḍāriʿ with the sīn, سَوْفَ, لَنْ or مَا (فَسَتُرْضِعُ، فَلَنْ يُقْبَلَ); and the performative — command, prohibition, question, prayer.",
         "What of a māḍī requital of truly past sense? It needs قَدْ, shown or estimated, with the fāʾ: وَإِنْ كَانَ قَمِيصُهُ قُدَّ مِنْ قُبُلٍ فَصَدَقَتْ — i.e. فَقَدْ صَدَقَتْ.",
         "Is إِنْ تُكْرِمْنِي فَيَرْحَمْكَ اللهُ a prayer? Yes — the muḍāriʿ in the sense of supplication is performative, so the fāʾ is a must, and the verb keeps its jazm form by the prayer's own sense.",
         "And the plain muḍāriʿ? Affirmed or negated by لَا it stands either way: إِنْ تَضْرِبْ أَضْرِبْ (jazm, no fāʾ) or فَأَضْرِبُ (fāʾ, rafʿ); لَا أَضْرِبْ or فَلَا أَضْرِبُ.",
         "Why rafʿ after the fāʾ? Because the fāʾ makes the requital a sentence of its own, outside the jāzim's reach — the verb is then free, and free means rafʿ.",
         "What does the engine READ here? The DabtEngine reads the fāʾ-initial word after a condition as the answer — the pronoun mubtadaʾ, the frozen لَيْسَ and عَسَى, the سَ-verb in rafʿ, the لَنْ-verb in naṣb, the command, the لَا-prohibition in jazm, the هَلْ-question in rafʿ, the prayer in jazm — and the fāʾ-less muḍāriʿ after a jazm'd condition in jazm."],
  "tr": ["Cezâ niçin fâ'ya muhtaçtır? Cezmi taşıyamayan cezâ şartına bir bağla bağlanmalıdır; o bağ fâ'dır.",
         "Hangi cezâlar zorunlu olarak fâ alır? İsim cümlesi (fe-ente madrûbun); câmid mâzî ve benzeri (fe-leyse minallâhi, fe-asâ en tekrahû); sîn, sevfe, len veya mâ'lı muzâri (fe-se-turdiu, fe-len yukbele); ve inşâî — emir, nehiy, istifhâm, duâ.",
         "Gerçekten geçmiş mânâlı mâzî cezâ? Fâ ile birlikte açık veya takdîrî kad ister: ve in kâne kamîsuhû kudde min kubulin fe-sadakat — yani fe-kad sadakat.",
         "İn tükrimnî fe-yerhamkellâh bir duâ mı? Evet — duâ mânâsındaki muzâri inşâîdir, fâ zorunludur; fiil duânın kendi mânâsıyla cezm şeklini korur.",
         "Düz muzâri? Müsbet veya lâ ile menfî iken iki türlü durur: in tadrib adrib (cezm, fâsız) veya fe-adribu (fâ, ref'); lâ adrib veya fe-lâ adribu.",
         "Fâ'dan sonra neden ref'? Çünkü fâ cezâyı câzimin ulaşamayacağı müstakil bir cümle yapar — fiil serbest kalır, serbest ise merfûdur.",
         "Motor burada neyi OKUR? DabtEngine şarttan sonraki fâ ile başlayan kelimeyi cevap okur — zamir mübtedâ, câmid leyse ve asâ, ref'li se-fiili, nasblı len-fiili, emir, cezimli lâ-nehyi, ref'li hel-sorusu, cezimli duâ — cezimli şarttan sonraki fâsız muzâriyi de cezimli okur."],
 },
 "plain": {"en": "The result of an «if» needs «then» when it cannot be cut short itself: a noun sentence («then you are struck»), a frozen verb («it may be»), a future verb with «sa», «sawfa», «lan» or «mā», or a command, prohibition, question or prayer. A plain present verb goes either way: cut short without «then», or full with it.",
           "tr": "«Eğer»in sonucu kendisi kesilemeyince «fe» ister: isim cümlesi («o zaman sen vurulansın»), câmid fiil («olabilir ki»), se, sevfe, len veya mâ'lı gelecek fiil, ya da emir, yasak, soru veya duâ. Düz muzâri iki türlü olur: fe'siz kesilmiş veya fe ile tam."},
 "explanation": {"en": "When the requital is a nominal sentence, a non-conjugable māḍī sentence or one in its sense — and then قَدْ, shown or estimated, is a must — or a muḍāriʿ joined to the sīn, سَوْفَ, لَنْ or مَا, or a performative verbal sentence such as the command, the prohibition, the question and the prayer, the entering of the fāʾ into it is obligatory: إِنْ ضَرَبْتَ فَأَنْتَ مَضْرُوبٌ; وَمَنْ يَفْعَلْ ذٰلِكَ فَلَيْسَ مِنَ اللهِ فِي شَيْءٍ (Āl ʿImrān 3:28); فَإِنْ كَرِهْتُمُوهُنَّ فَعَسَى أَنْ تَكْرَهُوا شَيْئًا (al-Nisāʾ 4:19); وَإِنْ كَانَ قَمِيصُهُ قُدَّ مِنْ قُبُلٍ فَصَدَقَتْ (Yūsuf 12:26); وَإِنْ تَعَاسَرْتُمْ فَسَتُرْضِعُ لَهُ أُخْرَى (al-Ṭalāq 65:6); وَمَنْ يَبْتَغِ غَيْرَ الْإِسْلَامِ دِينًا فَلَنْ يُقْبَلَ مِنْهُ (Āl ʿImrān 3:85); إِنْ ضَرَبَكَ زَيْدٌ فَاضْرِبْهُ، فَلَا تَضْرِبْهُ، فَهَلْ تَضْرِبُهُ; إِنْ تُكْرِمْنِي فَيَرْحَمْكَ اللهُ. When the requital is a muḍāriʿ other than these, affirmed or negated by لَا, the fāʾ with rafʿ and its dropping with jazm are both allowed: إِنْ تَضْرِبْ أَضْرِبْ or فَأَضْرِبُ, لَا أَضْرِبْ or فَلَا أَضْرِبُ.",
                 "tr": "Cezâ isim cümlesi, câmid mâzî cümle veya onun mânâsında — o zaman açık veya takdîrî kad zorunludur — ya da sîn, sevfe, len veya mâ'ya bitişik muzâri, ya da emir, nehiy, istifhâm ve duâ gibi inşâî fiil cümlesi ise fâ'nın ona girmesi vâcibdir: in darabte fe-ente madrûbun; ve men yef'al zâlike fe-leyse minallâhi fî şey'in (Âl-i İmrân 3:28); fe-in kerihtümûhünne fe-asâ en tekrahû şey'en (Nisâ 4:19); ve in kâne kamîsuhû kudde min kubulin fe-sadakat (Yûsuf 12:26); ve in teâsertüm fe-se-turdiu lehû uhrâ (Talâk 65:6); ve men yebtaği gayre'l-islâmi dînen fe-len yukbele minhu (Âl-i İmrân 3:85); in darabeke Zeydün fe'dribhu, fe-lâ tadribhu, fe-hel tadribuhû; in tükrimnî fe-yerhamkellâh. Cezâ bunların dışında müsbet veya lâ ile menfî bir muzâri ise ref' ile fâ da, cezm ile fâ'nın hazfi de câizdir: in tadrib adrib veya fe-adribu, lâ adrib veya fe-lâ adribu."},
 "examples": [
  {"ar": "إِنْ ضَرَبْتَ فَأَنْتَ مَضْرُوبٌ", "en": "the nominal requital with its fāʾ", "tr": "fâ'lı isim cümlesi cezâ", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَمَنْ يَفْعَلْ ذٰلِكَ فَلَيْسَ مِنَ اللهِ فِي شَيْءٍ", "en": "the non-conjugable māḍī requital, Āl ʿImrān 3:28", "tr": "câmid mâzî cezâ, Âl-i İmrân 3:28", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "وَإِنْ كَانَ قَمِيصُهُ قُدَّ مِنْ قُبُلٍ فَصَدَقَتْ", "en": "the māḍī requital with qad estimated, Yūsuf 12:26", "tr": "takdîrî kad'lı mâzî cezâ, Yûsuf 12:26", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "وَإِنْ تَعَاسَرْتُمْ فَسَتُرْضِعُ لَهُ أُخْرَى؛ فَلَنْ يُقْبَلَ مِنْهُ", "en": "the sīn and lan requitals, al-Ṭalāq 65:6, Āl ʿImrān 3:85", "tr": "sîn'li ve len'li cezâlar, Talâk 65:6, Âl-i İmrân 3:85", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "فَاضْرِبْهُ، فَلَا تَضْرِبْهُ، فَهَلْ تَضْرِبُهُ، فَيَرْحَمْكَ اللهُ", "en": "the performative requitals", "tr": "inşâî cezâlar", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "إِنْ تَضْرِبْ أَضْرِبْ أَوْ فَأَضْرِبُ", "en": "the plain muḍāriʿ: jazm without the fāʾ, rafʿ with it", "tr": "düz muzâri: fâsız cezm, fâ ile ref'", "sourceStory": "izhar-al-asrar", "sentence": "s7"},
 ],
 "commonMistakes": [
  {"wrong": "إِنْ ضَرَبْتَ أَنْتَ مَضْرُوبٌ", "right": "إِنْ ضَرَبْتَ فَأَنْتَ مَضْرُوبٌ", "why": {"en": "a nominal requital cannot carry the jazm and must be bound by the fāʾ", "tr": "isim cümlesi cezâ cezmi taşıyamaz; fâ ile bağlanmalıdır"}},
  {"wrong": "إِنْ تَضْرِبْ فَأَضْرِبْ", "right": "إِنْ تَضْرِبْ فَأَضْرِبُ (or أَضْرِبْ without the fāʾ)", "why": {"en": "after the fāʾ the plain muḍāriʿ is outside the jāzim's reach and takes rafʿ", "tr": "fâ'dan sonra düz muzâri câzimin erişimi dışındadır, ref' alır"}},
  {"wrong": "إِنْ ضَرَبَكَ زَيْدٌ اضْرِبْهُ", "right": "إِنْ ضَرَبَكَ زَيْدٌ فَاضْرِبْهُ", "why": {"en": "a command requital is performative and needs the fāʾ", "tr": "emir cezâ inşâîdir, fâ ister"}},
 ],
}
TMZ = "tamyiz"
ADD_EN = (" Chapter 44 (print pp. 140-141): the fāʾ obligatory in the nominal and non-conjugable requital with qad (s1), with the sīn, sawfa, lan, mā and the performative (s2), the examples with Āl ʿImrān 3:28 (s3), al-Nisāʾ 4:19 and Yūsuf 12:26 (s4), al-Ṭalāq 65:6 and Āl ʿImrān 3:85 (s5), the command, prohibition, question and prayer (s6); the plain muḍāriʿ with the fāʾ and rafʿ or jazm without it (s7).")
ADD_TR = (" Kırk dördüncü bab (baskı s. 140-141): isim cümlesi ve kad'lı câmid cezâda vâcib fâ (s1), sîn, sevfe, len, mâ ve inşâ ile (s2), Âl-i İmrân 3:28 (s3), Nisâ 4:19 ve Yûsuf 12:26 (s4), Talâk 65:6 ve Âl-i İmrân 3:85 (s5) örnekleri, emir, nehiy, istifhâm ve duâ (s6); fâ ve ref' ile veya fâsız cezm ile düz muzâri (s7).")
write_out(44, S, TITLE, ADD_EN, ADD_TR, "pp. 140-141", GLOSS_ADD, notes=(NOTE,),
          related=((K43, [K]), (FK, [K]), (JZ, [K]), (INS, [K]), (KI, [K]), (JT_, [K]), (QH, [K])))
report(44, S, GLOSS_ADD, (NOTE,))
